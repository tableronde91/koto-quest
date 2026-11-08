/* Service Worker Koto Quest : cache de l'interface + notifications push. */
const CACHE = 'koto-shell-v1';
const SHELL = ['/', '/manifest.webmanifest', '/icons/icon-192.png'];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()),
  );
});

// Réseau d'abord pour la navigation et les fichiers, cache en secours (hors ligne). L'API n'est jamais mise en cache.
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== self.location.origin || url.pathname.startsWith('/api/')) return;
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        if (res.ok && (event.request.mode === 'navigate' || url.pathname.startsWith('/assets/'))) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(event.request.mode === 'navigate' ? '/' : event.request, copy));
        }
        return res;
      })
      .catch(() => caches.match(event.request.mode === 'navigate' ? '/' : event.request)),
  );
});

self.addEventListener('push', (event) => {
  let data = { title: 'Koto Quest', body: 'Un petit défi japonais t’attend !', url: '/' };
  try { data = { ...data, ...event.data.json() }; } catch (_) {}
  event.waitUntil(
    self.registration.showNotification(data.title, {
      body: data.body,
      icon: '/icons/icon-192.png',
      badge: '/icons/icon-192.png',
      tag: 'koto-challenge',
      renotify: true,
      data: { url: data.url },
      actions: [{ action: 'open', title: 'Répondre' }],
    }),
  );
});

// Ouvre le mini-quiz ciblé (réutilise un onglet existant si possible).
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const target = new URL(event.notification.data?.url || '/', self.location.origin).href;
  event.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then((wins) => {
      for (const w of wins) {
        if (w.url.startsWith(self.location.origin) && 'focus' in w) {
          w.navigate(target);
          return w.focus();
        }
      }
      return self.clients.openWindow(target);
    }),
  );
});
