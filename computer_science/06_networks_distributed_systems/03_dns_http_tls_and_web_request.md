# DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **URL decomposition** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **DNS** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Gõ một URL nhìn như một hành động (action / 동작) đơn giản, nhưng trình duyệt (browser / 브라우저) phải resolve name, establish tuyến (route / 경로)/vận chuyển (transport / 전송)/bảo mật (security / 보안) ngữ cảnh (context / 맥락), speak HTTP, receive dữ liệu (data / 데이터) và execute/kết xuất (render / 렌더링). Chapter này dùng web yêu cầu (request / 요청) để nối nhiều layers.

## URL decomposition

`https://example.com:443/path?q=1` chứa scheme `https`, host `example.com`, optional cổng (port / 포트), đường dẫn (path / 경로) và truy vấn (query / 쿼리). Scheme quyết định giao thức (protocol / 프로토콜) expectations; hostname không trực tiếp là IP address.

> **Chuyển mạch:** URL decomposition xác định host và resource; DNS tìm địa chỉ, transport thiết lập kênh, TLS xác thực/mã hóa, rồi HTTP mang request qua toàn bộ đường đi.

## DNS

Lĩnh vực (domain / 도메인) Name hệ thống (system / 시스템) là phân tán (distributed / 분산) hierarchical naming hệ thống (system / 시스템). Resolver tìm records như A/AAAA/CNAME/MX/TXT qua bộ nhớ đệm (cache / 캐시) và recursive/authoritative hạ tầng (infrastructure / 인프라).

DNS caching dùng TTL để giảm độ trễ (latency / 지연 시간)/tải (load / 로드). Vì bộ nhớ đệm (cache / 캐시) tồn tại, bản ghi (record / 레코드) thay đổi (change / 변경) không globally immediate. Negative responses cũng có caching ngữ nghĩa (semantics / 의미론).

DNS over UDP/TCP and encrypted transports DoH/DoT exist; chính xác (exact / 정확한) đường dẫn (path / 경로) depends máy khách (client / 클라이언트)/mạng (network / 네트워크).

DNS round-robin/load-balancing is not same as strong health-aware routing by itself; caches and resolver hành vi (behavior / 동작) matter.

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **Establish vận chuyển (transport / 전송)** tiếp nhận điểm tựa từ **DNS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TLS goals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Establish vận chuyển (transport / 전송)

Sau khi có destination address và tuyến (route / 경로), máy khách (client / 클라이언트) opens vận chuyển (transport / 전송) liên kết (connection / 연결). Với classic HTTPS over TCP, TCP handshake establishes liên kết (connection / 연결), then TLS handshake authenticates máy chủ (server / 서버) and negotiates keys. With HTTP/3, QUIC combines vận chuyển (transport / 전송)/bảo mật (security / 보안) mechanisms over UDP.

Liên kết (connection / 연결) reuse reduces repeated handshake chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **TLS goals** tiếp nhận điểm tựa từ **Establish vận chuyển (transport / 전송)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HTTP ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLS goals

Tầng vận chuyển (transport layer / 전송 계층) bảo mật (security / 보안) provides confidentiality, integrity and peer authentication (typically server authentication via certificate PKI; client cert optional). Certificate binds công khai (public / 공개) key/định danh (identity / 식별자) claims through trust chuỗi (chain / 사슬) accepted by máy khách (client / 클라이언트).

TLS does not guarantee ứng dụng (application / 애플리케이션) is honest or authorization correct. It protects channel properties under các giả định (assumptions / 가정들).

### Symmetric + public-key cryptography

Public-key mechanisms authenticate/establish dùng chung (shared / 공유) secret; bulk dữ liệu (data / 데이터) uses efficient symmetric AEAD keys. hiện đại (modern / 현대적) TLS uses ephemeral key exchange to provide forward secrecy in dùng chung (common / 공통) configurations.

Xem [Cryptography foundations](../07_security_reliability/01_cryptography_foundations.md).

> **Chuyển mạch:** Trong **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **HTTP ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **TLS goals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HTTP ngữ nghĩa (semantics / 의미론)

HTTP yêu cầu (request / 요청) has phương thức (method / 메서드), mục tiêu (target / 대상), headers and optional body. phản hồi (response / 응답) has status, headers, body. Methods carry ngữ nghĩa (semantics / 의미론) such as safe/idempotent conventions, but máy chủ (server / 서버) hiện thực (implementation / 구현) can violate them.

HTTP/1.1 uses textual framing with persistent connections; HTTP/2 multiplexes nhị phân (binary / 이진) frames/streams on one liên kết (connection / 연결); HTTP/3 maps HTTP ngữ nghĩa (semantics / 의미론) onto QUIC streams. ứng dụng (application / 애플리케이션) ngữ nghĩa (semantics / 의미론) remain recognizable while vận chuyển (transport / 전송)/framing evolves.

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **Caching** tiếp nhận điểm tựa từ **HTTP ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cookies và sessions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Caching

Trình duyệt (browser / 브라우저), CDN, proxy and origin can bộ nhớ đệm (cache / 캐시) responses according to Cache-Control, validators like ETag/Last-Modified and yêu cầu (request / 요청) ngữ nghĩa (semantics / 의미론). bộ nhớ đệm (cache / 캐시) turns mạng (network / 네트워크) lời gọi (call / 호출) into cục bộ (local / 로컬)/edge phản hồi (response / 응답) but creates freshness/vô hiệu hóa (invalidation / 무효화) sự đánh đổi (trade-off / 트레이드오프).

`Cache-Control: max-age` defines freshness cửa sổ (window / 윈도우); revalidation can use conditional requests and 304. Sensitive/user-specific content requires careful `private`, `no-store`, `Vary` ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **Cookies và sessions** tiếp nhận điểm tựa từ **Caching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proxies, CDN và tải (load / 로드) balancers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cookies và sessions

HTTP is yêu cầu (request / 요청)/phản hồi (response / 응답); ứng dụng (application / 애플리케이션) session trạng thái (state / 상태) can be maintained via cookies/tokens. Cookie attributes Secure, HttpOnly, SameSite affect vận chuyển (transport / 전송)/script/cross-site hành vi (behavior / 동작). Cookie is not inherently authentication; it is lưu trữ (storage / 저장소)/vận chuyển (transport / 전송) cơ chế (mechanism / 메커니즘) often carrying session identifier.

> **Chuyển mạch:** Trong **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **Proxies, CDN và tải (load / 로드) balancers** tiếp nhận điểm tựa từ **Cookies và sessions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **A yêu cầu (request / 요청) end-to-end** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proxies, CDN và tải (load / 로드) balancers

Yêu cầu (request / 요청) may terminate TLS at CDN/bộ cân bằng tải (load balancer / 로드 밸런서), then be forwarded to backend via separate liên kết (connection / 연결). Client-visible peer is edge endpoint. Headers like Forwarded/X-Forwarded-* carry original ngữ cảnh (context / 맥락) by convention and must be trusted only from controlled proxies.

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **A yêu cầu (request / 요청) end-to-end** tiếp nhận điểm tựa từ **Proxies, CDN và tải (load / 로드) balancers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## A yêu cầu (request / 요청) end-to-end

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

Each arrow is a ranh giới (boundary / 경계) with independent thất bại (failure / 실패)/độ trễ (latency / 지연 시간)/bảo mật (security / 보안) hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **A yêu cầu (request / 요청) end-to-end** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> A web yêu cầu (request / 요청) is not “HTTP goes to máy chủ (server / 서버)”. It is a **ngăn xếp (stack / 스택) of trạng thái (state / 상태) machines and trust boundaries**, plus caches/proxies that may terminate one liên kết (connection / 연결) and create another.

> **Chuyển mạch:** Trong **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“HTTPS means website is safe.”** TLS secures channel/định danh (identity / 식별자) under PKI; ứng dụng (application / 애플리케이션) can still be malicious/vulnerable.

**“DNS maps one lĩnh vực (domain / 도메인) to one máy chủ (server / 서버).”** Multiple records, CDNs, anycast, tải (load / 로드) balancers and caching make ánh xạ (mapping / 매핑) động (dynamic / 동적)/many-to-many.

**“HTTP is stateless, therefore app cannot have session.”** Session trạng thái (state / 상태) is layered via cookies/tokens/máy chủ (server / 서버) lưu trữ (storage / 저장소).

> **Chuyển mạch:** Ở chặng này của **DNS, HTTP, TLS và một web yêu cầu (request / 요청) end-to-end**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

This chapter is expanded end-to-end again in [Browser → Database Request](../90_connections/01_browser_to_database_request.md). bảo mật (security / 보안) details at [identity/auth](../07_security_reliability/02_identity_authentication_and_authorization.md), cơ sở dữ liệu (database / 데이터베이스) truy cập (access / 접근) at [query execution](../05_data_databases/03_indexes_and_query_execution.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
