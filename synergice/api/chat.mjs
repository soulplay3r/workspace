// Optional LLM backend for the Synergice assistant (retrieval-augmented).
//
// The browser retrieves the most relevant passages from the site's own
// search index and POSTs { question, passages: [{ title, url, text }] } here.
// Claude writes a short answer grounded only in those passages.
//
// Deploy as a serverless function that speaks Web Request/Response
// (Vercel, Netlify Functions v2, Cloudflare Workers with nodejs_compat),
// set ANTHROPIC_API_KEY, then build the site with
//   CHAT_ENDPOINT=https://<your-host>/api/chat python3 build.py
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const ALLOWED_ORIGIN = process.env.ALLOWED_ORIGIN || "*";

const SYSTEM = `You are the Synergice assistant on the B2B website of Synergice, the partnering platform of Strides Pharma Science Limited.
Answer the visitor's question using only the passages provided from the website. If the passages do not contain the answer, say so in one sentence and suggest contacting the partnering team through the enquiry form.
Audience: pharmaceutical business partners (licensing, regulatory, sourcing teams), not patients.
Rules:
- Keep answers to 2-4 short sentences in plain British English. No headings, no bullet lists, no markdown.
- Never give personal medical advice or dosing for an individual; refer people to a healthcare professional.
- Never state prices, minimum order quantities, lead times, availability or registration status; direct those questions to the partnering team.
- Do not invent facts, dates or numbers that are not in the passages.`;

const cors = {
  "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json", ...cors } });

export default async function handler(req) {
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
  if (req.method !== "POST") return json({ error: "Method not allowed" }, 405);

  let payload;
  try {
    payload = await req.json();
  } catch {
    return json({ error: "Invalid JSON" }, 400);
  }
  const question = String(payload.question || "").slice(0, 500).trim();
  const passages = Array.isArray(payload.passages) ? payload.passages.slice(0, 6) : [];
  if (!question) return json({ error: "Missing question" }, 400);

  const context = passages
    .map((p, i) => `<passage index="${i + 1}" title="${String(p.title).slice(0, 200)}">\n${String(p.text).slice(0, 2500)}\n</passage>`)
    .join("\n");

  try {
    const response = await client.beta.messages.create({
      model: "claude-opus-5-5",
      max_tokens: 1024,
      output_config: { effort: "low" },
      betas: ["server-side-fallback-2026-07-01"],
      fallbacks: "default",
      system: SYSTEM,
      messages: [{ role: "user", content: `${context}\n\nQuestion: ${question}` }],
    });

    if (response.stop_reason === "refusal") {
      return json({ answer: "I can't help with that here. Please contact the partnering team through the enquiry form." });
    }
    const answer = response.content
      .filter((b) => b.type === "text")
      .map((b) => b.text)
      .join("")
      .trim();
    return json({ answer });
  } catch (error) {
    if (error instanceof Anthropic.RateLimitError) return json({ error: "Busy, try again shortly" }, 429);
    if (error instanceof Anthropic.APIError) return json({ error: "Assistant unavailable" }, 502);
    throw error;
  }
}
