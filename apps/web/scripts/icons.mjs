// Génère les icônes PNG de la PWA à partir de public/icons/icon.svg
import sharp from 'sharp';
const src = 'public/icons/icon.svg';
await sharp(src).resize(192, 192).png().toFile('public/icons/icon-192.png');
await sharp(src).resize(512, 512).png().toFile('public/icons/icon-512.png');
// Version « maskable » : marge de sécurité de 20 %
const inner = await sharp(src).resize(360, 360).png().toBuffer();
await sharp({ create: { width: 512, height: 512, channels: 4, background: '#1B2550' } })
  .composite([{ input: inner, left: 76, top: 76 }]).png().toFile('public/icons/icon-maskable-512.png');
console.log('icônes générées');
