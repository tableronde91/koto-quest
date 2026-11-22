import { describe, expect, it } from 'vitest';
import { isEnglish, joinTokens } from '../src';

describe('anglais', () => {
  it('les segments anglais se recollent avec des espaces', () => {
    expect(joinTokens(['My', 'name', 'is', 'Sam.'])).toBe('My name is Sam.');
    expect(joinTokens(['わたし', 'は', 'がくせい'])).toBe('わたしはがくせい');
    expect(joinTokens(['저는', '학생이에요.'])).toBe('저는 학생이에요.');
    expect(isEnglish('hello')).toBe(true);
    expect(isEnglish('こんにちは')).toBe(false);
  });
});
