// Rend le fichier HTML hors ligne totalement autonome (icône incluse) et le renomme.
import { readFileSync, writeFileSync, rmSync, readdirSync } from 'fs';
const dir = 'dist-offline';
const svg = readFileSync('public/icons/icon.svg', 'utf8');
const dataUri = `data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}`;
let html = readFileSync(`${dir}/index.html`, 'utf8');
html = html
  .replace(/<link rel="manifest"[^>]*>\s*/g, '')
  .replace(/<link rel="apple-touch-icon"[^>]*>\s*/g, '')
  .replaceAll('/icons/icon.svg', dataUri)
  .replaceAll('./icons/icon.svg', dataUri);
writeFileSync(`${dir}/KotoQuest.html`, html);
for (const f of readdirSync(dir)) if (f !== 'KotoQuest.html') rmSync(`${dir}/${f}`, { recursive: true, force: true });
console.log(`✔ ${dir}/KotoQuest.html (${Math.round(html.length / 1024)} Ko) : double-cliquez pour l'ouvrir`);
