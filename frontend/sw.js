const CACHE = 'ti-shell-v1';
const SHELL_ASSETS = ['/', '/static/logo.png', '/static/logo-white.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL_ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  // Only cache GET requests for shell assets; let API calls pass through
  if (e.request.method !== 'GET') return;
  if (url.pathname.startsWith('/ask') || url.pathname.startsWith('/tts') ||
      url.pathname.startsWith('/upload') || url.pathname.startsWith('/feedback')) return;
  e.respondWith(
    fetch(e.request).catch(() => caches.match(e.request))
  );
});
