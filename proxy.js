// lalalin AI proxy - bridges lalalin.xyz frontend to OpenClaw Gateway
// Usage: node proxy.js
// Listens on :8790, forwards to OpenClaw Gateway :28789
// Sets CORS headers so lalalin.xyz can call it

const http = require('http');
const GATEWAY = 'http://127.0.0.1:28789';
const PORT = 8790;
const TOKEN = '16ae1a3dff0492b482bdf8bc20ebd0acf7b75ff871e9d91f';

const server = http.createServer((req, res) => {
  // CORS
  const origin = req.headers.origin || '*';
  res.setHeader('Access-Control-Allow-Origin', origin);
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type,Authorization');
  res.setHeader('Access-Control-Max-Age', '86400');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // Forward to gateway with auth token
  const fwdHeaders = Object.assign({}, req.headers);
  delete fwdHeaders.host;
  delete fwdHeaders.origin;
  delete fwdHeaders.referer;
  fwdHeaders.authorization = 'Bearer ' + TOKEN;

  const proxy = http.request(GATEWAY + req.url, {
    method: req.method,
    headers: fwdHeaders
  }, (proxyRes) => {
    res.writeHead(proxyRes.statusCode, proxyRes.headers);
    proxyRes.pipe(res);
  });

  proxy.on('error', (e) => {
    res.writeHead(502);
    res.end(JSON.stringify({error:{message:'Gateway unreachable: '+e.message}}));
  });

  req.pipe(proxy);
});

server.listen(PORT, '127.0.0.1', () => {
  console.log('Lalalin AI Proxy running on http://127.0.0.1:' + PORT);
  console.log('Forwarding to OpenClaw Gateway at ' + GATEWAY);
});
