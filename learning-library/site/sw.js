const SHELL_CACHE = 'study-shelf-shell-v3';
const CONTENT_CACHE = 'study-shelf-content-v3';
const USER_CACHE = 'study-shelf-user-v1';
const SHELL = [
  './',
  './index.html',
  './styles.css',
  './learning-os.css',
  './app.js',
  './learning-os.js',
  './manifest.webmanifest',
  './library/library.json'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(SHELL_CACHE).then(cache => cache.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keep = new Set([SHELL_CACHE, CONTENT_CACHE, USER_CACHE]);
    const keys = await caches.keys();
    await Promise.all(keys.filter(key => key.startsWith('study-shelf-') && !keep.has(key)).map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});

async function networkFirst(request) {
  const cache = await caches.open(CONTENT_CACHE);
  try {
    const response = await fetch(request);
    if (response.ok) cache.put(request, response.clone());
    return response;
  } catch {
    return (await cache.match(request)) || (await caches.match(request));
  }
}

async function staleWhileRevalidate(request) {
  const cache = await caches.open(CONTENT_CACHE);
  const cached = await cache.match(request) || await caches.match(request);
  const update = fetch(request).then(response => {
    if (response.ok) cache.put(request, response.clone());
    return response;
  }).catch(() => null);
  return cached || update;
}

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  if (event.request.mode === 'navigate') {
    event.respondWith(networkFirst(event.request).then(response => response || caches.match('./index.html')));
    return;
  }

  if (url.pathname.endsWith('/library/library.json') || url.pathname.endsWith('/library/search-index.json') || url.pathname.endsWith('/library/graph.json')) {
    event.respondWith(networkFirst(event.request));
    return;
  }

  if (url.pathname.includes('/library/files/')) {
    event.respondWith(staleWhileRevalidate(event.request));
    return;
  }

  if (/\.(?:js|css|webmanifest|png|svg|ico)$/i.test(url.pathname)) {
    event.respondWith(staleWhileRevalidate(event.request));
  }
});

self.addEventListener('message', event => {
  if (event.data?.type !== 'CACHE_URL' || !event.data.url) return;
  event.waitUntil(caches.open(USER_CACHE).then(cache => cache.add(event.data.url)));
});
