# DNS, HTTP, TLS và một web request end-to-end

Gõ một URL nhìn như một action đơn giản, nhưng browser phải resolve name, establish route/transport/security context, speak HTTP, receive data và execute/render. Chapter này dùng web request để nối nhiều layers.

## URL decomposition

`https://example.com:443/path?q=1` chứa scheme `https`, host `example.com`, optional port, path và query. Scheme quyết định protocol expectations; hostname không trực tiếp là IP address.

## DNS

Domain Name System (도메인 이름 시스템) là distributed hierarchical naming system. Resolver tìm records như A/AAAA/CNAME/MX/TXT qua cache và recursive/authoritative infrastructure.

DNS caching dùng TTL để giảm latency/load. Vì cache tồn tại, record change không globally immediate. Negative responses cũng có caching semantics.

DNS over UDP/TCP and encrypted transports DoH/DoT exist; exact path depends client/network.

DNS round-robin/load-balancing is not same as strong health-aware routing by itself; caches and resolver behavior matter.

## Establish transport

Sau khi có destination address và route, client opens transport connection. Với classic HTTPS over TCP, TCP handshake establishes connection, then TLS handshake authenticates server and negotiates keys. With HTTP/3, QUIC combines transport/security mechanisms over UDP.

Connection reuse reduces repeated handshake cost.

## TLS goals

Transport Layer Security provides confidentiality, integrity and peer authentication (typically server authentication via certificate PKI; client cert optional). Certificate binds public key/identity claims through trust chain accepted by client.

TLS does not guarantee application is honest or authorization correct. It protects channel properties under assumptions.

### Symmetric + public-key cryptography

Public-key mechanisms authenticate/establish shared secret; bulk data uses efficient symmetric AEAD keys. Modern TLS uses ephemeral key exchange to provide forward secrecy in common configurations.

Xem [Cryptography foundations](../07_security_reliability/01_cryptography_foundations.md).

## HTTP semantics

HTTP request has method, target, headers and optional body. Response has status, headers, body. Methods carry semantics such as safe/idempotent conventions, but server implementation can violate them.

HTTP/1.1 uses textual framing with persistent connections; HTTP/2 multiplexes binary frames/streams on one connection; HTTP/3 maps HTTP semantics onto QUIC streams. Application semantics remain recognizable while transport/framing evolves.

## Caching

Browser, CDN, proxy and origin can cache responses according to Cache-Control, validators like ETag/Last-Modified and request semantics. Cache turns network call into local/edge response but creates freshness/invalidation trade-off.

`Cache-Control: max-age` defines freshness window; revalidation can use conditional requests and 304. Sensitive/user-specific content requires careful `private`, `no-store`, `Vary` semantics.

## Cookies và sessions

HTTP is request/response; application session state can be maintained via cookies/tokens. Cookie attributes Secure, HttpOnly, SameSite affect transport/script/cross-site behavior. Cookie is not inherently authentication; it is storage/transport mechanism often carrying session identifier.

## Proxies, CDN và load balancers

Request may terminate TLS at CDN/load balancer, then be forwarded to backend via separate connection. Client-visible peer is edge endpoint. Headers like Forwarded/X-Forwarded-* carry original context by convention and must be trusted only from controlled proxies.

## A request end-to-end

Conceptually:

```text
URL
 ↓
DNS name resolution
 ↓
IP routing / ARP-ND / link frames
 ↓
TCP or QUIC connection
 ↓
TLS authentication + key establishment
 ↓
HTTP request
 ↓
reverse proxy / app / database/cache
 ↓
HTTP response
 ↓
TLS/transport/IP/link back
 ↓
browser parse/render/execute
```

Each arrow is a boundary with independent failure/latency/security behavior.

## Mental Model

> A web request is not “HTTP goes to server”. It is a **stack of state machines and trust boundaries**, plus caches/proxies that may terminate one connection and create another.

## Common Misconceptions

**“HTTPS means website is safe.”** TLS secures channel/identity under PKI; application can still be malicious/vulnerable.

**“DNS maps one domain to one server.”** Multiple records, CDNs, anycast, load balancers and caching make mapping dynamic/many-to-many.

**“HTTP is stateless, therefore app cannot have session.”** Session state is layered via cookies/tokens/server storage.

## Kết nối

This chapter is expanded end-to-end again in [Browser → Database Request](../90_connections/01_browser_to_database_request.md). Security details at [identity/auth](../07_security_reliability/02_identity_authentication_and_authorization.md), database access at [query execution](../05_data_databases/03_indexes_and_query_execution.md).
