import { describe, expect, it } from 'vitest';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import { CosmeticCatalog, DEFAULT_AVATAR, checkAcquire, ownedSkus, validateAvatar } from '../src';

const catalog = JSON.parse(readFileSync(resolve(__dirname, '../../../content/cosmetics/catalog.json'), 'utf8')) as CosmeticCatalog;

describe('cosmétiques', () => {
  it('le catalogue est cohérent (skus uniques, emplacements connus, défauts gratuits)', () => {
    const skus = catalog.items.map((i) => i.sku);
    expect(new Set(skus).size).toBe(skus.length);
    for (const [slot, sku] of Object.entries(catalog.defaults)) {
      const item = catalog.items.find((i) => i.sku === sku)!;
      expect(item.slot).toBe(slot);
      expect(item.price).toBe(0);
    }
    expect(validateAvatar(DEFAULT_AVATAR, catalog, ownedSkus(catalog, []))).toEqual([]);
  });

  it('achat : pièces suffisantes, pas de double achat', () => {
    const owned = ownedSkus(catalog, []);
    expect(checkAcquire(catalog, 'hat-kasa', { coins: 10, owned, defeatedBosses: new Set() })).toEqual({ ok: false, error: 'not_enough_coins' });
    expect(checkAcquire(catalog, 'hat-kasa', { coins: 50, owned, defeatedBosses: new Set() })).toMatchObject({ ok: true, cost: 50 });
    expect(checkAcquire(catalog, 'hat-kasa', { coins: 500, owned: new Set([...owned, 'hat-kasa']), defeatedBosses: new Set() })).toEqual({ ok: false, error: 'already_owned' });
    expect(checkAcquire(catalog, 'outfit-tshirt', { coins: 0, owned: new Set(), defeatedBosses: new Set() })).toEqual({ ok: false, error: 'not_for_sale' });
    expect(checkAcquire(catalog, 'nope', { coins: 0, owned, defeatedBosses: new Set() })).toEqual({ ok: false, error: 'unknown_item' });
  });

  it('les trophées exigent le gardien vaincu et sont gratuits', () => {
    const owned = ownedSkus(catalog, []);
    expect(checkAcquire(catalog, 'hat-kitsune', { coins: 9999, owned, defeatedBosses: new Set() })).toEqual({ ok: false, error: 'boss_required' });
    expect(checkAcquire(catalog, 'hat-kitsune', { coins: 0, owned, defeatedBosses: new Set(['n5-w3']) })).toMatchObject({ ok: true, cost: 0 });
  });

  it('refuse une apparence avec un objet non possédé ou mal placé', () => {
    const owned = ownedSkus(catalog, ['hat-kasa']);
    expect(validateAvatar({ ...DEFAULT_AVATAR, hat: 'hat-kasa' }, catalog, owned)).toEqual([]);
    expect(validateAvatar({ ...DEFAULT_AVATAR, hat: 'hat-oni' }, catalog, owned)[0]).toMatch(/ne possèdes pas/);
    expect(validateAvatar({ ...DEFAULT_AVATAR, hat: 'bg-sakura' }, catalog, ownedSkus(catalog, ['bg-sakura']))[0]).toMatch(/emplacement/);
    expect(validateAvatar({ ...DEFAULT_AVATAR, skin: 99, hair: 'mohawk' }, catalog, owned)).toHaveLength(2);
  });
});
