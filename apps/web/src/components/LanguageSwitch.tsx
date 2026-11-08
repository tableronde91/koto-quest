import { useState } from 'react';
import type { Locale } from '@koto/shared';
import { LOCAL, put } from '../api/client';
import { LOCALES, T, locale, setLocale } from '../i18n';

/**
 * Choix de la langue de l'interface (français / anglais). Connecté, le choix est aussi
 * enregistré sur le compte pour suivre le joueur sur ses autres appareils.
 */
export function LanguageSwitch({ saveToAccount = false, compact = false }: { saveToAccount?: boolean; compact?: boolean }) {
  const [busy, setBusy] = useState(false);
  async function choose(next: Locale) {
    if (next === locale || busy) return;
    setBusy(true);
    try {
      if (saveToAccount && !LOCAL) await put('/me/preferences', { locale: next }).catch(() => undefined);
    } finally {
      try {
        sessionStorage.setItem('koto-locale-sync', next);
      } catch {
        /* stockage indisponible */
      }
      setLocale(next);
    }
  }
  return (
    <div role="radiogroup" aria-label={T('Langue')} className={`inline-flex rounded-full border-2 border-line bg-surface p-1 ${compact ? 'text-sm' : ''}`}>
      {LOCALES.map((l) => (
        <button
          key={l.code}
          type="button"
          role="radio"
          aria-checked={l.code === locale}
          lang={l.code}
          disabled={busy}
          onClick={() => choose(l.code)}
          className={`rounded-full px-3 py-1.5 font-bold ${l.code === locale ? 'bg-ink text-paper' : 'text-ink-soft'}`}
        >
          {compact ? l.short : l.label}
        </button>
      ))}
    </div>
  );
}
