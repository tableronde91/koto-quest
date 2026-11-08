/// <reference types="vite/client" />
interface ImportMetaEnv {
  /** "1" pour la version hors ligne (sans serveur ni base de données). */
  readonly VITE_LOCAL?: string;
}
