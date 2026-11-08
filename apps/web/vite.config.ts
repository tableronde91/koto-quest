import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import { viteSingleFile } from 'vite-plugin-singlefile';
import { fileURLToPath } from 'url';

// Les paquets du monorepo sont lus depuis leurs sources TypeScript :
// pas de copie compilée à reconstruire, ni de cache Vite périmé après une mise à jour du moteur.
const src = (pkg: string) => fileURLToPath(new URL(`../../packages/${pkg}/src/index.ts`, import.meta.url));

// Deux modes :
//  - par défaut : application connectée à l'API (/api via proxy en développement) ;
//  - « offline » (vite build --mode offline) : un seul fichier HTML autonome, sans serveur ni base de données.
export default defineConfig(({ mode }) => {
  const offline = mode === 'offline';
  return {
    plugins: [react(), tailwindcss(), ...(offline ? [viteSingleFile()] : [])],
    base: offline ? './' : '/',
    resolve: { alias: { '@koto/learning-engine': src('learning-engine'), '@koto/shared': src('shared') } },
    server: {
      port: 5173,
      proxy: offline ? undefined : { '/api': { target: process.env.API_URL ?? 'http://localhost:3000', changeOrigin: false } },
    },
    preview: {
      port: 5173,
      proxy: offline ? undefined : { '/api': { target: process.env.API_URL ?? 'http://localhost:3000', changeOrigin: false } },
    },
    build: {
      outDir: offline ? 'dist-offline' : 'dist',
    },
  };
});
