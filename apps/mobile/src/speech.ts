import * as Speech from 'expo-speech';
import { hasHangul } from '@koto/shared';

/**
 * Prononciation japonaise ou coréenne par la synthèse vocale du téléphone.
 * Comme sur le web : une voix par langue choisie une fois (installée et de meilleure qualité d'abord),
 * un court délai quand une lecture était en cours (l'arrêt est asynchrone et coupait la phrase
 * suivante), et seule la dernière demande est jouée.
 */
type Lang = 'ja' | 'ko';
const voiceId: Partial<Record<Lang, string>> = {};
let voiceLoad: Promise<void> | null = null;
let speaking = false;
let request = 0;

function loadVoice(): Promise<void> {
  voiceLoad ??= Speech.getAvailableVoicesAsync()
    .then((voices) => {
      for (const lang of ['ja', 'ko'] as const) {
        const mine = voices.filter((v) => v.language.toLowerCase().replace('_', '-').startsWith(lang));
        const best = mine.sort((a, b) => (b.quality === Speech.VoiceQuality.Enhanced ? 1 : 0) - (a.quality === Speech.VoiceQuality.Enhanced ? 1 : 0))[0];
        voiceId[lang] = best?.identifier;
      }
    })
    .catch(() => undefined);
  return voiceLoad;
}
loadVoice();

interface Part {
  text: string;
  rate?: number;
  pitch?: number;
}

function say(parts: Part[], onEnd?: () => void) {
  const list = parts.map((p) => ({ ...p, text: p.text.replace(/＿/g, '') })).filter((p) => p.text.trim());
  if (!list.length) return;
  const my = ++request;
  const wasBusy = speaking;
  Speech.stop();
  speaking = false;
  const go = () => {
    if (my !== request) return;
    speaking = true;
    // Le coréen se reconnaît au hangeul : la même phrase n'est jamais lue avec une voix japonaise.
    const lang: Lang = list.some((p) => hasHangul(p.text)) ? 'ko' : 'ja';
    list.forEach((p, i) =>
      Speech.speak(p.text, {
        language: lang === 'ko' ? 'ko-KR' : 'ja-JP',
        voice: voiceId[lang],
        rate: p.rate ?? 0.9,
        pitch: p.pitch ?? 1,
        onDone: i === list.length - 1 ? () => { if (my === request) { speaking = false; onEnd?.(); } } : undefined,
        onStopped: i === list.length - 1 ? () => { if (my === request) speaking = false; } : undefined,
        onError: () => { if (my === request) speaking = false; },
      }),
    );
  };
  loadVoice().then(() => (wasBusy ? setTimeout(go, 120) : go()));
}

export function speak(text: string, slow = false) {
  say([{ text, rate: slow ? 0.6 : 0.9 }]);
}

/**
 * Document d'écoute d'examen : lignes « N|… » (narrateur), « M|… » (homme), « F|… » (femme),
 * lues à la suite ; les rôles se distinguent par la hauteur de voix.
 */
export function speakScript(script: string, onEnd?: () => void) {
  const lines = script.split('\n').map((l) => (l[1] === '|' ? { who: l[0], text: l.slice(2) } : { who: 'N', text: l }));
  say(lines.map((l) => ({ text: l.text, pitch: l.who === 'M' ? 0.7 : l.who === 'F' ? 1.4 : 1 })), onEnd);
}

export function stopSpeech() {
  request++;
  speaking = false;
  Speech.stop();
}
