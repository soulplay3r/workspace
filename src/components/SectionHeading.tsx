interface Props {
  eyebrow: string;
  title: string;
  dek?: string;
  align?: "left" | "center";
}

export default function SectionHeading({ eyebrow, title, dek, align = "left" }: Props) {
  return (
    <div className={align === "center" ? "text-center max-w-prose mx-auto" : "max-w-prose"}>
      <p className="section-eyebrow mb-3">{eyebrow}</p>
      <h2 className="section-heading">{title}</h2>
      {dek && <p className="mt-4 text-ink-600 text-lg leading-relaxed">{dek}</p>}
    </div>
  );
}
