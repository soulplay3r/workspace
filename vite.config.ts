import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Repo is deployed to GitHub Pages at https://<owner>.github.io/<repo>/
// Base path is read from an env var set by the Pages workflow so local dev stays at "/".
export default defineConfig({
  plugins: [react()],
  base: process.env.VITE_BASE_PATH ?? "/",
});
