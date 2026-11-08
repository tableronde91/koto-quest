/**
 * Personnage et cosmétiques (phase 2) : règles pures partagées par le serveur, la version
 * hors ligne et l'interface. Les récompenses sont purement cosmétiques : elles s'obtiennent
 * avec des pièces gagnées en étudiant, ou en battant les gardiens de fin de monde.
 */

export type CosmeticSlot = 'outfit' | 'hat' | 'accessory' | 'background';
export const COSMETIC_SLOTS: CosmeticSlot[] = ['outfit', 'hat', 'accessory', 'background'];

export interface CosmeticItem {
  sku: string;
  slot: CosmeticSlot;
  name: string;
  description: string;
  /** Prix en pièces (0 = gratuit ou trophée). */
  price: number;
  /** Trophée : obtenu en battant le gardien de ce monde. */
  unlockBoss?: string;
}

export interface CosmeticCatalog {
  version: string;
  slots: { slot: CosmeticSlot; label: string }[];
  defaults: Partial<Record<CosmeticSlot, string>>;
  items: CosmeticItem[];
}

/** Apparence de base, toujours gratuite. */
export const AVATAR_OPTIONS = {
  skin: 5,
  hair: ['short', 'long', 'bun', 'spiky', 'bob', 'none'] as const,
  hairColor: 6,
  eyes: ['round', 'happy', 'calm'] as const,
};

export interface AvatarConfig {
  skin: number;
  hair: (typeof AVATAR_OPTIONS.hair)[number];
  hairColor: number;
  eyes: (typeof AVATAR_OPTIONS.eyes)[number];
  outfit: string | null;
  hat: string | null;
  accessory: string | null;
  background: string | null;
}

export const DEFAULT_AVATAR: AvatarConfig = {
  skin: 1,
  hair: 'short',
  hairColor: 0,
  eyes: 'round',
  outfit: 'outfit-tshirt',
  hat: null,
  accessory: null,
  background: 'bg-paper',
};

/** Un objet gratuit sans condition fait partie de la garde-robe de départ. */
export const isStarterItem = (item: CosmeticItem) => item.price === 0 && !item.unlockBoss;

export function ownedSkus(catalog: CosmeticCatalog, purchased: Iterable<string>): Set<string> {
  const owned = new Set(purchased);
  for (const i of catalog.items) if (isStarterItem(i)) owned.add(i.sku);
  return owned;
}

export type AcquireError = 'unknown_item' | 'already_owned' | 'boss_required' | 'not_enough_coins' | 'not_for_sale';

/**
 * Peut-on obtenir cet objet ? Les objets payants s'achètent avec des pièces ;
 * les trophées se réclament gratuitement une fois le gardien vaincu.
 */
export function checkAcquire(
  catalog: CosmeticCatalog,
  sku: string,
  ctx: { coins: number; owned: Set<string>; defeatedBosses: Set<string> },
): { ok: true; item: CosmeticItem; cost: number } | { ok: false; error: AcquireError } {
  const item = catalog.items.find((i) => i.sku === sku);
  if (!item) return { ok: false, error: 'unknown_item' };
  if (ctx.owned.has(sku)) return { ok: false, error: 'already_owned' };
  if (item.unlockBoss) {
    return ctx.defeatedBosses.has(item.unlockBoss) ? { ok: true, item, cost: 0 } : { ok: false, error: 'boss_required' };
  }
  if (item.price <= 0) return { ok: false, error: 'not_for_sale' };
  if (ctx.coins < item.price) return { ok: false, error: 'not_enough_coins' };
  return { ok: true, item, cost: item.price };
}

export const ACQUIRE_ERRORS_FR: Record<AcquireError, string> = {
  unknown_item: 'Objet inconnu.',
  already_owned: 'Tu possèdes déjà cet objet.',
  boss_required: 'Cet objet est un trophée : bats d’abord le gardien correspondant.',
  not_enough_coins: 'Pas assez de pièces pour cet achat.',
  not_for_sale: 'Cet objet n’est pas en vente.',
};

/**
 * Valide une apparence : options de base dans les bornes, objets équipés possédés
 * et placés dans le bon emplacement. Renvoie la liste des erreurs (vide si valide).
 */
export function validateAvatar(config: unknown, catalog: CosmeticCatalog, owned: Set<string>): string[] {
  const errors: string[] = [];
  const c = config as Partial<AvatarConfig> | null;
  if (!c || typeof c !== 'object') return ['Apparence invalide.'];
  const int = (v: unknown, max: number) => Number.isInteger(v) && (v as number) >= 0 && (v as number) < max;
  if (!int(c.skin, AVATAR_OPTIONS.skin)) errors.push('Teinte de peau invalide.');
  if (!int(c.hairColor, AVATAR_OPTIONS.hairColor)) errors.push('Couleur de cheveux invalide.');
  if (!AVATAR_OPTIONS.hair.includes(c.hair as AvatarConfig['hair'])) errors.push('Coiffure invalide.');
  if (!AVATAR_OPTIONS.eyes.includes(c.eyes as AvatarConfig['eyes'])) errors.push('Yeux invalides.');
  for (const slot of COSMETIC_SLOTS) {
    const sku = c[slot];
    if (sku === null || sku === undefined) continue;
    const item = catalog.items.find((i) => i.sku === sku);
    if (typeof sku !== 'string' || !item) errors.push(`Objet inconnu : ${String(sku)}.`);
    else if (item.slot !== slot) errors.push(`${item.name} ne se porte pas à cet emplacement.`);
    else if (!owned.has(sku)) errors.push(`Tu ne possèdes pas encore : ${item.name}.`);
  }
  return errors;
}

/** Normalise une apparence (champs manquants complétés par défaut). */
export function normalizeAvatar(config: Partial<AvatarConfig> | null | undefined): AvatarConfig {
  return { ...DEFAULT_AVATAR, ...(config ?? {}) };
}

// ───────── Économie de pièces ─────────

export const COINS = {
  lessonFirstCompletion: 10,
  perfectLessonBonus: 5,
  questCompleted: 5,
} as const;
