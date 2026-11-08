// Crée apps/api/.env à partir de .env.example si besoin, puis génère des clés VAPID si elles sont absentes.
const fs = require('fs');
const path = require('path');
const webpush = require('web-push');

const envPath = path.join(__dirname, '..', '.env');
if (!fs.existsSync(envPath)) fs.copyFileSync(path.join(__dirname, '..', '.env.example'), envPath);
let env = fs.readFileSync(envPath, 'utf8');
if (/^VAPID_PUBLIC_KEY="?[A-Za-z0-9_-]{20,}/m.test(env)) {
  console.log('Clés VAPID déjà présentes.');
} else {
  const keys = webpush.generateVAPIDKeys();
  const set = (k, v) => {
    const re = new RegExp(`^${k}=.*$`, 'm');
    env = re.test(env) ? env.replace(re, `${k}="${v}"`) : `${env}\n${k}="${v}"`;
  };
  set('VAPID_PUBLIC_KEY', keys.publicKey);
  set('VAPID_PRIVATE_KEY', keys.privateKey);
  fs.writeFileSync(envPath, env);
  console.log('✔ Clés VAPID générées dans apps/api/.env');
}
