import * as Speech from 'expo-speech';
import { scriptAccents, textLanguage } from '@koto/shared';

/**
 * Prononciation japonaise ou coréenne par la synthèse vocale du téléphone.
 * Comme sur le web : une voix par langue choisie une fois (installée et de meilleure qualité d'abord),
 * un court délai quand une lecture était en cours (l'arrêt est asynchrone et coupait la phrase
 * suivante), et seule la dernière demande est jouée.
 */
type Lang = 'ja' | 'ko' | 'en' | 'zh' | 'es' | 'de';
const LOCALE: Record<Lang, string> = { ja: 'ja-JP', ko: 'ko-KR', en: 'en-GB', zh: 'zh-CN', es: 'es-ES', de: 'de-DE' };
const voiceId: Partial<Record<Lang, string>> = {};
/** Voix par variante régionale de l'anglais (en-US, en-GB, en-AU, en-CA) pour les écoutes TOEIC */
const localeVoiceId: Record<string, string | undefined> = {};
let voiceLoad: Promise<void> | null = null;
let speaking = false;
let request = 0;

function loadVoice(): Promise<void> {
  voiceLoad ??= Speech.getAvailableVoicesAsync()
    .then((voices) => {
      for (const lang of ['ja', 'ko', 'en', 'zh', 'es', 'de'] as const) {
        // Chinois : mandarin (zh-CN, zh-TW), pas le cantonais (zh-HK)
        const mine = voices.filter((v) => v.language.toLowerCase().replace('_', '-').startsWith(lang) && !/zh-hk|yue/.test(v.language.toLowerCase().replace('_', '-')));
        const best = mine.sort((a, b) => (b.quality === Speech.VoiceQuality.Enhanced ? 1 : 0) - (a.quality === Speech.VoiceQuality.Enhanced ? 1 : 0))[0];
        voiceId[lang] = best?.identifier;
      }
      for (const v of voices) {
        const l = v.language.replace('_', '-');
        if (l.toLowerCase().startsWith('en-') && (!localeVoiceId[l] || v.quality === Speech.VoiceQuality.Enhanced)) localeVoiceId[l] = v.identifier;
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
  locale?: string;
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
    // Langue reconnue à l'écriture : hangeul → coréen, kana et kanji → japonais, alphabet latin → anglais.
    const lang: Lang = textLanguage(list.map((p) => p.text).join(' '));
    list.forEach((p, i) =>
      Speech.speak(p.text, {
        language: lang === 'en' && p.locale ? p.locale : LOCALE[lang],
        voice: (lang === 'en' && p.locale && (localeVoiceId[p.locale] ?? (p.locale === 'en-CA' ? localeVoiceId['en-US'] : undefined))) || voiceId[lang],
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
  // En anglais, comme au TOEIC : un accent par rôle (américain, britannique, australien, canadien).
  const accents = textLanguage(lines.map((l) => l.text).join(' ')) === 'en' ? scriptAccents(script) : null;
  say(lines.map((l) => ({ text: l.text, pitch: l.who === 'M' ? 0.7 : l.who === 'F' ? 1.4 : 1, locale: accents?.[l.who] })), onEnd);
}

export function stopSpeech() {
  request++;
  speaking = false;
  Speech.stop();
}
