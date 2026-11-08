import * as Speech from 'expo-speech';

/** Prononciation japonaise par la synthèse vocale du téléphone. */
export function speak(text: string, slow = false) {
  Speech.stop();
  Speech.speak(text.replace(/＿/g, ''), { language: 'ja-JP', rate: slow ? 0.6 : 0.9 });
}
