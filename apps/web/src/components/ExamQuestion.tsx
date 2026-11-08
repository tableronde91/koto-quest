import { Fragment, useEffect, useRef, useState } from 'react';
import type { IssuedQuestionDto } from '@koto/shared';
import { scriptText, speak, speakScript, speechSupported } from '../lib/speech';
import { Jp } from './ui';
import { T } from '../i18n';

const JP_RE = /[぀-ヿ一-龯]/;

/** Phrase d'examen : {{…}} est souligné (comme sur la copie du JLPT), ★ et ＿＿ sont des cases. */
export function ExamSentence({ text, className = '' }: { text: string; className?: string }) {
  const parts = text.split(/(\{\{.*?\}\}|★|＿＿)/);
  return (
    <span lang="ja" className={`jp ${className}`}>
      {parts.map((p, i) =>
        p.startsWith('{{') ? (
          <u key={i} className="decoration-2 underline-offset-[6px]">{p.slice(2, -2)}</u>
        ) : p === '★' ? (
          <span key={i} className="mx-0.5 inline-flex h-[1.4em] min-w-[2.6em] items-center justify-center border-b-2 border-ink align-middle text-gold-ink">★</span>
        ) : p === '＿＿' ? (
          <span key={i} aria-label="case" className="mx-0.5 inline-block h-[1.4em] min-w-[2.6em] border-b-2 border-ink align-middle" />
        ) : (
          <Fragment key={i}>{p}</Fragment>
        ),
      )}
    </span>
  );
}

/** Lecteur d'un document sonore, avec un nombre d'écoutes limité (comme le jour de l'examen). */
function AudioPlayer({ script, maxPlays, qid }: { script: string; maxPlays?: number; qid: string }) {
  const [plays, setPlays] = useState(0);
  const [playing, setPlaying] = useState(false);
  const left = maxPlays === undefined ? Infinity : maxPlays - plays;
  const auto = useRef<string | null>(null);
  const play = () => {
    if (left <= 0) return;
    setPlays((p) => p + 1);
    setPlaying(true);
    // Filet de sécurité : certaines voix ne signalent pas la fin de lecture.
    const fallback = window.setTimeout(() => setPlaying(false), 2000 + script.length * 160);
    if (!speakScript(script, () => { window.clearTimeout(fallback); setPlaying(false); })) setPlaying(false);
  };
  // Lecture automatique à l'affichage (compte comme une écoute, une seule fois par question)
  useEffect(() => {
    if (auto.current === qid) return;
    auto.current = qid;
    if (speechSupported()) play();
    return () => {
      if (speechSupported()) speechSynthesis.cancel();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [qid]);
  if (!speechSupported())
    return <p className="whitespace-pre-line text-left">{T("Ce navigateur ne peut pas lire l’audio japonais. Transcription :")}{' '}{'\n'}<span lang="ja" className="jp">{scriptText(script)}</span></p>;
  return (
    <div className="flex flex-col items-center gap-2">
      <button type="button" className="btn btn-quiet min-h-14 px-6 text-lg" onClick={play} disabled={left <= 0 || playing}>
        {playing ? T("🔊 Écoute en cours…") : left <= 0 ? T("Plus d’écoute disponible") : T("🔊 Écouter")}
      </button>
      {maxPlays !== undefined && <p className="text-sm text-ink-soft">{T("{0} écoute{1} restante{2} sur {3}", [Math.max(0, left) , left > 1 ? 's' : '' , left > 1 ? 's' : '' , maxPlays])}</p>}
    </div>
  );
}

/**
 * Question d'épreuve : la réponse est sélectionnée (et modifiable) sans correction immédiate.
 * La copie entière est corrigée par le serveur à la fin.
 */
export function ExamQuestion({ q, value, onChange, number }: { q: IssuedQuestionDto; value: string | string[] | undefined; onChange: (v: string | string[] | undefined) => void; number?: number }) {
  const d = q.display ?? {};
  const script = q.type === 'listening_choice' && q.audio ? q.audio : null;
  const legacyListening = script && !script.includes('|');
  useEffect(() => {
    if (legacyListening && q.audio) speak(q.audio);
  }, [q.id, legacyListening, q.audio]);

  const audioChoices = !!d.audioChoices;
  const compact = !audioChoices && q.choices?.every((c) => [...c].length <= 4);
  const grid = audioChoices
    ? 'grid-cols-1 sm:grid-cols-3'
    : compact
      ? q.choices!.length === 3 ? 'grid-cols-3' : q.choices!.length === 2 ? 'grid-cols-2' : 'grid-cols-2 sm:grid-cols-4'
      : q.choices && q.choices.length % 2 === 0 && q.choices.every((c) => [...c].length <= 18) ? 'grid-cols-1 sm:grid-cols-2' : 'grid-cols-1';

  return (
    <fieldset className="flex flex-col gap-4" data-testid="exam-question" data-qid={q.id} data-type={q.type}>
      {d.part && <p lang="ja" className="jp -mb-2 text-sm font-bold text-ink-soft">{d.part}</p>}
      <legend className="mb-1 text-lg font-bold">
        {number !== undefined && <span className="mr-2 text-ink-soft">{number}.</span>}
        <span lang={JP_RE.test(q.prompt) ? 'ja' : 'fr'} className={JP_RE.test(q.prompt) ? 'jp' : undefined}>{q.prompt}</span>
      </legend>

      {script ? (
        <div className="flex flex-col items-center gap-3 rounded-3xl bg-surface-2 p-5">
          {legacyListening ? (
            speechSupported() ? <button type="button" className="btn btn-quiet min-h-14 px-6 text-lg" onClick={() => q.audio && speak(q.audio)}>{T("Écouter")}</button> : <Jp text={q.audio ?? ''} furigana={false} className="text-3xl" />
          ) : (
            <AudioPlayer script={script} maxPlays={d.maxPlays} qid={q.id} />
          )}
          {d.text && <p lang="ja" className="jp text-center text-xl font-bold">{d.text}</p>}
        </div>
      ) : d.passage ? (
        <div className="flex flex-col gap-3">
          <div lang="ja" className="jp whitespace-pre-line rounded-2xl border-2 border-line bg-surface p-5 text-lg leading-loose">{d.passage}</div>
          {d.text && <p lang="ja" className="jp text-xl font-bold">{d.text}</p>}
        </div>
      ) : d.lines ? (
        <div className="flex flex-col gap-2 rounded-3xl bg-surface-2 p-5">
          {d.lines.map((l, i) => (
            <p key={i} className="grid grid-cols-[4.5rem_1fr] items-baseline gap-3">
              <span className="text-sm font-bold text-ink-soft">{l.speaker}</span>
              <Jp text={l.jp} furigana={false} className="text-2xl" />
            </p>
          ))}
          {d.text && <p className="text-ink-soft">{d.text}</p>}
        </div>
      ) : d.jp || d.text ? (
        <div className="flex min-h-24 flex-col items-center justify-center gap-1 rounded-3xl bg-surface-2 p-5 text-center">
          {d.jp && !(q.type === 'true_false' && d.text) &&
            (d.part ? (
              <ExamSentence text={d.jp} className="text-2xl leading-loose sm:text-3xl" />
            ) : (
              <Jp text={d.jp.replace(/＿+/g, '（　）')} furigana={false} className={`${[...d.jp].length <= 3 ? 'text-6xl' : 'text-3xl'} font-bold`} />
            ))}
          {d.text && <p className={d.jp && q.type !== 'true_false' ? 'text-ink-soft' : 'jp text-2xl font-bold'}>{d.text}</p>}
        </div>
      ) : null}

      {q.choices && (
        <div className={`grid gap-3 ${grid}`}>
          {q.choices.map((c, i) => {
            const selected = value === c;
            const jp = JP_RE.test(c);
            return (
              <label key={c} className="flex min-h-14 cursor-pointer items-center gap-3 rounded-2xl border-2 bg-surface px-4 py-2" style={{ borderColor: selected ? 'var(--ink)' : 'var(--line)', background: selected ? 'var(--surface-2)' : 'var(--surface)' }}>
                <input type="radio" name={q.id} checked={selected} onChange={() => onChange(c)} className="h-5 w-5 accent-[var(--ink)]" aria-label={audioChoices ? T("Réponse {0}", [i + 1]) : undefined} />
                {audioChoices ? (
                  <span className="flex flex-1 items-center justify-between gap-2">
                    <span className="font-display text-xl">{i + 1}</span>
                    <button type="button" className="rounded-full bg-surface-2 px-3 py-1.5 text-sm font-bold" onClick={(e) => { e.preventDefault(); speak(c); }} aria-label={T("Écouter la réponse {0}", [i + 1])}>{T("🔊 Écouter")}</button>
                  </span>
                ) : (
                  <span lang={jp ? 'ja' : 'fr'} className={jp ? `jp ${compact ? 'text-2xl' : 'text-lg'}` : 'text-lg'}>{c}</span>
                )}
              </label>
            );
          })}
        </div>
      )}

      {q.type === 'sentence_order' && q.tokens && <OrderPicker tokens={q.tokens} value={Array.isArray(value) ? value : []} onChange={(v) => onChange(v.length ? v : undefined)} />}
    </fieldset>
  );
}

function OrderPicker({ tokens, value, onChange }: { tokens: string[]; value: string[]; onChange: (v: string[]) => void }) {
  // On retrouve les indices utilisés à partir des valeurs choisies (les segments peuvent se répéter).
  const used: number[] = [];
  for (const v of value) {
    const i = tokens.findIndex((t, k) => t === v && !used.includes(k));
    if (i >= 0) used.push(i);
  }
  return (
    <div className="flex flex-col gap-3">
      <div className="flex min-h-16 flex-wrap items-center gap-2 rounded-2xl border-2 border-line bg-surface p-3" aria-label={T("Ta phrase")}>
        {value.length === 0 && <span className="text-ink-soft">{T("Touche les morceaux dans le bon ordre.")}</span>}
        {used.map((i, k) => (
          <button key={k} type="button" onClick={() => onChange(value.filter((_, j) => j !== k))} className="jp min-h-11 rounded-xl bg-ink px-3 text-xl text-paper">{tokens[i]}</button>
        ))}
      </div>
      <div className="flex flex-wrap justify-center gap-2" data-testid="token-bank">
        {tokens.map((t, i) =>
          used.includes(i) ? (
            <span key={i} aria-hidden="true" className="jp min-h-11 rounded-xl border-2 border-dashed border-line px-3 text-xl text-transparent">{t}</span>
          ) : (
            <button key={i} type="button" onClick={() => onChange([...value, t])} className="jp min-h-11 rounded-xl border-2 border-line bg-surface px-3 text-xl">{t}</button>
          ),
        )}
      </div>
    </div>
  );
}
