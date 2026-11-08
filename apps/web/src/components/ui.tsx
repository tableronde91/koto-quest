import { ReactNode } from 'react';
import { speak, speechSupported } from '../lib/speech';
import { T } from '../i18n';

/** Texte japonais avec lecture facultative (furigana) affichée au-dessus. */
export function Jp({ text, reading, furigana, className = '' }: { text: string; reading?: string | null; furigana: boolean; className?: string }) {
  // Les furigana ne servent qu'au-dessus des kanji : sur un mot en kana, ils décaleraient la ligne pour rien.
  const show = furigana && reading && reading !== text && /[\u4e00-\u9faf\u3005]/.test(text);
  if (!show) return <span lang="ja" className={`jp ${className}`}>{text}</span>;
  return (
    <ruby lang="ja" className={`jp ${className}`}>
      {text}
      <rp>(</rp>
      <rt>{reading}</rt>
      <rp>)</rp>
    </ruby>
  );
}

export function SpeakButtons({ text, size = 'md' }: { text: string; size?: 'md' | 'lg' }) {
  if (!speechSupported()) return <p className="text-sm text-ink-soft">{T("La synthèse vocale n’est pas disponible sur ce navigateur.")}</p>;
  const big = size === 'lg';
  return (
    <div className="flex items-center gap-2">
      <button type="button" className={`btn btn-quiet ${big ? 'min-h-14 px-6 text-lg' : ''}`} onClick={() => speak(text)} aria-label={T("Écouter")}>
        <SoundIcon />{' '}{T("Écouter")}</button>
      <button type="button" className="btn btn-quiet" onClick={() => speak(text, true)} aria-label={T("Écouter lentement")}>{T("Lentement")}</button>
    </div>
  );
}

export function SoundIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor" />
      <path d="M16 8.5a5 5 0 010 7M18.5 6a8.5 8.5 0 010 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
    </svg>
  );
}

export function ProgressBar({ value, max, label, tone = 'ink' }: { value: number; max: number; label: string; tone?: 'ink' | 'gold' | 'ok' }) {
  const pct = max > 0 ? Math.min(100, Math.round((value / max) * 100)) : 0;
  const color = tone === 'gold' ? 'var(--gold)' : tone === 'ok' ? 'var(--ok)' : 'var(--ink)';
  return (
    <div role="progressbar" aria-label={label} aria-valuenow={value} aria-valuemin={0} aria-valuemax={max} className="h-3 w-full overflow-hidden rounded-full bg-surface-2">
      <div className="h-full rounded-full transition-[width] duration-500" style={{ width: `${pct}%`, background: color }} />
    </div>
  );
}

export function Spinner({ label = T("Chargement…") }: { label?: string }) {
  return (
    <div role="status" className="flex items-center gap-3 p-8 text-ink-soft">
      <span className="h-5 w-5 animate-spin rounded-full border-[3px] border-line border-t-ink" aria-hidden="true" />
      {label}
    </div>
  );
}

export function ErrorBox({ error, onRetry }: { error: unknown; onRetry?: () => void }) {
  const msg = error instanceof Error ? error.message : T("Une erreur est survenue.");
  return (
    <div role="alert" className="rounded-2xl border-2 border-ko bg-ko-bg p-4">
      <p className="font-bold">{msg}</p>
      {onRetry && (
        <button className="btn btn-quiet mt-3" onClick={onRetry}>{T("Réessayer")}</button>
      )}
    </div>
  );
}

export function PageTitle({ children, sub }: { children: ReactNode; sub?: ReactNode }) {
  return (
    <header className="mb-6">
      <h1 className="text-3xl sm:text-4xl">{children}</h1>
      {sub && <p className="mt-1 max-w-[60ch] text-ink-soft">{sub}</p>}
    </header>
  );
}
