# TLS, PKI và vòng đời chứng chỉ

> **Mạch đọc:** Đọc **TLS, PKI và vòng đời chứng chỉ** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **TLS giải quyết những gì?** sang **Vì sao chỉ mã hóa là chưa đủ?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi một ứng dụng truy cập `https://service.example.com`, việc “dùng HTTPS” thực tế là kết quả của nhiều cơ chế phối hợp: phân giải DNS, kết nối TCP, bắt tay TLS, kiểm tra chứng chỉ, thương lượng thuật toán mật mã, thiết lập khóa phiên rồi mới truyền HTTP đã mã hóa.

Trong môi trường vận hành (production / 운영 환경), các lỗi như `certificate expired`, `unknown CA`, `hostname verification failed`, `handshake_failure`, `unable to find valid certification path` hoặc `SSLHandshakeException` thường không nằm ở HTTP lô-gic (logic / 논리). Chúng thuộc lớp **TLS và hạ tầng khóa công khai (Public Key Infrastructure - PKI)**.

## TLS giải quyết những gì?

TLS chủ yếu cung cấp ba thuộc tính:

- **bí mật (confidentiality)**: bên thứ ba trên đường truyền không dễ đọc nội dung;
- **toàn vẹn (integrity)**: dữ liệu bị sửa đổi có thể được phát hiện;
- **xác thực (authentication)**: máy khách (client / 클라이언트) có cơ chế kiểm tra danh tính của máy chủ (server / 서버), và trong mTLS máy chủ (server / 서버) cũng có thể kiểm tra máy khách (client / 클라이언트).

TLS không tự bảo đảm ứng dụng (application / 애플리케이션) đúng, máy chủ (server / 서버) không bị xâm nhập hay dữ liệu lưu trữ an toàn. Nó bảo vệ một phần đường truyền và danh tính endpoint theo trust mô hình (model / 모델) của PKI.

## Vì sao chỉ mã hóa là chưa đủ?

Nếu máy khách (client / 클라이언트) mã hóa dữ liệu cho một attacker mà tưởng đó là máy chủ (server / 서버) thật, confidentiality không giúp nhiều. Vì vậy máy khách (client / 클라이언트) cần biết công khai (public / 공개) key đang dùng thực sự thuộc endpoint nào.

PKI giải bài toán này bằng chuỗi tin cậy (chain of trust).

## Chứng chỉ X.509

Chứng chỉ TLS máy chủ (server / 서버) thường là chứng chỉ **X.509** chứa các thông tin như:

- công khai (public / 공개) key;
- subject/issuer;
- thời hạn hiệu lực;
- serial number;
- extensions;
- Subject Alternative Name (SAN);
- chữ ký của CA phát hành.

Kiểm tra tệp (file / 파일) chứng chỉ:

```bash
openssl x509 -in server.crt -noout -text
```

Xem ngày hiệu lực:

```bash
openssl x509 -in server.crt -noout -dates
```

## Private key và certificate khác nhau

Chứng chỉ có thể được phân phối công khai; private key phải được bảo vệ.

Mô hình tư duy (mental model / 사고 모델):

```text
private key
    -> chứng minh quyền sở hữu identity key

certificate
    -> public key + identity metadata + CA signature
```

Nếu private key bị lộ, attacker có thể giả mạo endpoint trong nhiều tình huống phù hợp. Thay certificate nhưng giữ private key đã bị lộ không giải quyết được sự cố.

## CA là gì?

**Tổ chức chứng thực (Certificate Authority - CA)** ký chứng chỉ và đóng vai trò bên thứ ba được trust.

Máy khách (client / 클라이언트) thường có **trust store** chứa các gốc (root / 루트) CA được tin cậy. máy chủ (server / 서버) không cần certificate trực tiếp do gốc (root / 루트) CA ký; thường có intermediate CA ở giữa.

```text
Root CA
   ↓ ký
Intermediate CA
   ↓ ký
Server certificate
```

Máy khách (client / 클라이언트) xác minh từng chữ ký trong chuỗi (chain / 사슬) cho tới một trust anchor nó đã tin.

## Tại sao cần intermediate CA?

Gốc (root / 루트) private key có giá trị cực lớn và nên được bảo vệ rất chặt. Thay vì dùng gốc (root / 루트) trực tiếp hàng ngày, tổ chức dùng intermediate CA để phát hành certificate.

Nếu intermediate có vấn đề, có thể thu hồi hoặc thay intermediate mà không nhất thiết thay gốc (root / 루트) trust anchor trên toàn bộ máy khách (client / 클라이언트).

## Máy chủ (server / 서버) phải gửi chuỗi (chain / 사슬) nào?

Máy chủ (server / 서버) thường gửi:

```text
leaf/server certificate
+
intermediate certificate(s)
```

Gốc (root / 루트) certificate thường không cần gửi vì máy khách (client / 클라이언트) đã có trong trust store.

Một lỗi môi trường vận hành (production / 운영 환경) phổ biến là máy chủ (server / 서버) chỉ cấu hình leaf certificate mà quên intermediate. Một số trình duyệt (browser / 브라우저) vẫn có thể hoạt động do bộ nhớ đệm (cache / 캐시)/intermediate fetching, nhưng Java hoặc máy khách (client / 클라이언트) khác thất bại.

Kiểm tra chuỗi (chain / 사슬) máy chủ (server / 서버):

```bash
openssl s_client -connect service.example.com:443 -servername service.example.com -showcerts
```

`-servername` gửi SNI, rất quan trọng khi nhiều hostname dùng chung IP.

## Hostname xác minh (verification / 확인)

Máy khách (client / 클라이언트) không chỉ kiểm tra certificate do CA tin cậy ký; nó còn phải kiểm tra hostname đang truy cập có nằm trong certificate không.

Hiện nay **Subject Alternative Name (SAN)** là trường quan trọng cho hostname/IP định danh (identity / 식별자).

Ví dụ certificate có:

```text
DNS:api.example.com
DNS:*.internal.example.com
```

thì truy cập hostname khác có thể thất bại (fail / 실패) dù certificate chưa hết hạn và CA hợp lệ.

## Wildcard certificate

`*.example.com` thường match một cấp như:

```text
api.example.com
www.example.com
```

nhưng không nhất thiết match:

```text
a.b.example.com
```

Không nên coi wildcard là “mọi hostname phía dưới”.

## SNI

**máy chủ (server / 서버) Name Indication (SNI)** cho phép máy khách (client / 클라이언트) gửi hostname trong TLS handshake để reverse proxy/bộ cân bằng tải (load balancer / 로드 밸런서) chọn certificate phù hợp trước khi HTTP Host header được đọc.

```text
client -> TCP connect tới IP
client -> TLS ClientHello + SNI=api.example.com
server -> chọn certificate cho api.example.com
```

Nếu máy khách (client / 클라이언트) không gửi SNI hoặc gửi hostname sai, máy chủ (server / 서버) có thể trả certificate mặc định không match.

## TLS handshake ở mức khái niệm

Một TLS 1.3 handshake đơn giản hóa có thể hình dung:

```text
ClientHello
  - phiên bản hỗ trợ
  - cipher suites
  - key share
  - SNI
       ↓
ServerHello
  - lựa chọn tham số
  - key share
       ↓
server certificate + proof
       ↓
client verify chain/hostname
       ↓
hai phía suy ra session keys
       ↓
encrypted application data
```

Chi tiết thực tế phức tạp hơn, nhưng mô hình tư duy (mental model / 사고 모델) này đủ để phân lớp lỗi.

## TLS 1.2 và TLS 1.3

TLS 1.3 loại bỏ nhiều thuật toán cũ, đơn giản hóa handshake và giảm round trip trong nhiều trường hợp. Một số cấu hình legacy chỉ hỗ trợ TLS 1.0/1.1 hoặc cipher cũ có thể không tương thích với máy khách (client / 클라이언트) hiện đại.

Kiểm tra:

```bash
openssl s_client -connect host:443 -servername host -tls1_2
openssl s_client -connect host:443 -servername host -tls1_3
```

Tùy phiên bản OpenSSL và máy chủ (server / 서버).

## Cipher suite

Cipher suite mô tả tập thuật toán dùng cho các phần của TLS. Trong TLS 1.3, cấu trúc tên đơn giản hơn so với TLS 1.2.

Không nên chọn cipher chỉ vì “mạnh nhất” theo cảm giác. Cần cân bằng:

- bảo mật (security / 보안) chính sách (policy / 정책);
- máy khách (client / 클라이언트) tính tương thích (compatibility / 호환성);
- hardware acceleration;
- compliance;
- giao thức (protocol / 프로토콜) phiên bản (version / 버전).

## Forward secrecy

Các cơ chế trao đổi khóa tạm thời như ECDHE giúp đạt **bí mật chuyển tiếp (forward secrecy)**: nếu long-term private key bị lộ trong tương lai, attacker không dễ giải mã lại các session cũ đã capture trước đó.

Đây là lý do hiện đại (modern / 현대적) TLS ưu tiên ephemeral key exchange.

## Certificate expiration

Certificate chỉ hợp lệ trong khoảng thời gian xác định.

```bash
openssl s_client -connect host:443 -servername host </dev/null 2>/dev/null \
  | openssl x509 -noout -dates
```

Nếu clock hệ thống sai, certificate hợp lệ vẫn có thể bị xem là “chưa hiệu lực” hoặc “đã hết hạn”. Vì vậy TLS liên hệ trực tiếp với [Time, clock và NTP](../05_system/time_clock_ntp.md).

## Renewal và automation

Certificate có vòng đời. Vấn đề vận hành không phải “cài certificate một lần”, mà là:

```text
issue
→ deploy
→ monitor expiration
→ renew
→ reload/restart an toàn
→ verify
→ revoke khi cần
```

Let's Encrypt/ACME giúp tự động hóa certificate công khai (public / 공개), nhưng hệ thống private PKI cũng cần workflow tương tự.

Một hệ thống tốt phải kiểm tra cả việc renewal đã tạo certificate mới **và** dịch vụ (service / 서비스) đã thực sự dùng certificate mới.

## Reload certificate

Nhiều reverse proxy có thể reload certificate mà không downtime lớn:

```bash
nginx -t && systemctl reload nginx
```

Nhưng ngữ nghĩa (semantics / 의미론) phụ thuộc ứng dụng. Một Java dịch vụ (service / 서비스) có thể cần restart nếu keystore chỉ được đọc lúc startup.

## Java trust store và key store

Trong Java, **trust store** chứa certificate/CA mà JVM tin. **Key store** thường chứa private key và certificate định danh (identity / 식별자) của chính ứng dụng khi cần máy chủ (server / 서버) TLS hoặc mTLS máy khách (client / 클라이언트) authentication.

Các định dạng thường gặp:

```text
JKS
PKCS12 (.p12/.pfx)
PEM
```

Java hiện đại thường hỗ trợ PKCS12 rộng rãi.

Liệt kê keystore:

```bash
keytool -list -v -keystore app.p12
```

Nếu Java báo:

```text
PKIX path building failed
```

thường cần kiểm tra trust chuỗi (chain / 사슬)/trust store thay vì disable certificate xác minh (verification / 확인).

## Không tắt TLS xác minh (verification / 확인) để “fix” môi trường vận hành (production / 운영 환경)

Các lựa chọn như `curl -k`, trust-all `X509TrustManager` hoặc tắt hostname xác minh (verification / 확인) chỉ nên dùng trong chẩn đoán có kiểm soát.

Nếu đưa vào môi trường vận hành (production / 운영 환경), bạn đã loại bỏ phần authentication quan trọng của TLS và mở đường cho man-in-the-middle.

## mTLS

Trong **mutual TLS (mTLS)**, máy chủ (server / 서버) yêu cầu máy khách (client / 클라이언트) certificate.

```text
client verify server certificate
+
server verify client certificate
```

mTLS cung cấp định danh (identity / 식별자) ở tầng vận chuyển (transport layer / 전송 계층), thường dùng service-to-service hoặc nội bộ (internal / 내부) hạ tầng (infrastructure / 인프라).

Nhưng mTLS không tự mô hình hóa authorization nghiệp vụ. Một máy khách (client / 클라이언트) có certificate hợp lệ chưa chắc được phép gọi mọi API.

## Certificate revocation

Nếu private key bị compromise trước khi certificate hết hạn, cần cơ chế thu hồi.

Hai khái niệm truyền thống:

- CRL (Certificate Revocation List);
- OCSP (Online Certificate Status protocol).

Trong thực tế, hành vi (behavior / 동작) kiểm tra revocation phụ thuộc máy khách (client / 클라이언트)/nền tảng (platform / 플랫폼) và chính sách (policy / 정책). Không nên giả định mọi máy khách (client / 클라이언트) luôn kiểm tra OCSP giống nhau.

## OCSP stapling

Máy chủ (server / 서버) có thể lấy OCSP phản hồi (response / 응답) rồi “đính kèm” vào handshake để máy khách (client / 클라이언트) không cần tự truy vấn (query / 쿼리) CA responder cho mỗi liên kết (connection / 연결).

Điều này có thể giảm độ trễ (latency / 지연 시간) và cải thiện privacy/độ tin cậy (reliability / 신뢰성).

## TLS termination

Trong kiến trúc (architecture / 아키텍처) có bộ cân bằng tải (load balancer / 로드 밸런서):

```text
client
  ↓ TLS
load balancer
  ↓ HTTP hoặc TLS lần nữa
backend
```

TLS có thể terminate ở bộ cân bằng tải (load balancer / 로드 밸런서). Nếu backend nhận HTTP plaintext, traffic vẫn được bảo vệ bên ngoài nhưng không mã hóa đoạn nội bộ.

Nếu compliance hoặc threat mô hình (model / 모델) yêu cầu, backend hop có thể dùng TLS/mTLS riêng.

## End-to-end TLS không luôn nghĩa một session

Một yêu cầu (request / 요청) có thể đi qua nhiều TLS session:

```text
client --TLS A--> edge
edge   --TLS B--> internal proxy
proxy  --TLS C--> backend
```

Mỗi hop có certificate/trust store và dạng thất bại (failure mode / 실패 모드) riêng.

## ALPN và HTTP/2

**Application-Layer giao thức (protocol / 프로토콜) Negotiation (ALPN)** cho phép máy khách (client / 클라이언트)/máy chủ (server / 서버) chọn giao thức (protocol / 프로토콜) ứng dụng như HTTP/2 trong TLS handshake.

Kiểm tra bằng OpenSSL tùy phiên bản:

```bash
openssl s_client -connect host:443 -servername host -alpn h2,http/1.1
```

Nếu HTTP/2 không được thương lượng, nguyên nhân có thể nằm ở TLS/ALPN cấu hình (config / 설정) chứ không phải HTTP ứng dụng (application / 애플리케이션) mã (code / 코드).

## Session resumption

TLS session resumption giảm chi phí handshake cho liên kết (connection / 연결) mới bằng cách tái sử dụng thông tin phiên trước qua session ticket/PSK tùy giao thức (protocol / 프로토콜).

Điều này giảm CPU và độ trễ (latency / 지연 시간) trong hệ thống liên kết (connection / 연결) churn cao.

## Handshake CPU chi phí (cost / 비용)

Public-key cryptography trong handshake tốn CPU hơn symmetric encryption sau khi session key đã được thiết lập. Nếu máy chủ (server / 서버) tạo lượng lớn liên kết (connection / 연결) TLS mới mỗi giây, handshake có thể trở thành bottleneck CPU.

Liên kết (connection / 연결) reuse, TLS session resumption và hardware acceleration có thể ảnh hưởng sức chứa (capacity / 용량).

## TLS thất bại (failure / 실패) theo tầng

Một luồng (flow / 흐름) chẩn đoán:

```text
DNS resolve được?
↓
TCP connect được?
↓
TLS ClientHello/ServerHello xảy ra?
↓
server trả certificate nào?
↓
chain hợp lệ?
↓
hostname match?
↓
time hợp lệ?
↓
protocol/cipher tương thích?
↓
client certificate cần không?
```

Công cụ:

```bash
dig host
nc -vz host 443
openssl s_client -connect host:443 -servername host -showcerts
curl -v https://host/
```

## Proxy có thể thay certificate

Corporate proxy hoặc bảo mật (security / 보안) appliance đôi khi giải mã TLS bằng cách phát certificate từ private enterprise CA. Máy công ty trust CA này nên trình duyệt (browser / 브라우저) hoạt động, nhưng JVM/bộ chứa (container / 컨테이너) không có CA đó có thể thất bại (fail / 실패).

Đây là dạng thất bại (failure mode / 실패 모드) rất phổ biến khi “trình duyệt (browser / 브라우저) vào được nhưng Java không gọi được”.

Giải pháp đúng là hiểu trust chuỗi (chain / 사슬) và cài CA phù hợp theo chính sách (policy / 정책), không phải tắt xác minh (verification / 확인).

## Certificate pinning

Một số máy khách (client / 클라이언트) pin công khai (public / 공개) key/certificate cụ thể để giảm phụ thuộc trust store rộng. Pinning tăng bảo mật (security / 보안) trong một threat mô hình (model / 모델) nhưng làm rotation phức tạp; cấu hình sai có thể tự gây outage khi certificate/key đổi.

## Secrets và tệp (file / 파일) permission

Private key cần quyền hạn chế:

```bash
chmod 600 server.key
chown root:service server.key
```

Quyền chính xác phụ thuộc dịch vụ (service / 서비스) mô hình (model / 모델). Không nên để private key world-readable.

## Mô hình tư duy

TLS có thể xem là hai bài toán lồng nhau:

```text
1. xác minh identity qua PKI
2. thiết lập session keys để bảo vệ data
```

Nếu chỉ nhìn “cổng (port / 포트) 443 mở” thì ta mới xác minh tầng TCP, chưa chứng minh TLS trust đã hoạt động.

## Những hiểu lầm phổ biến

**“HTTPS hoạt động thì certificate chắc đúng.”** Có thể trình duyệt (browser / 브라우저) đang trust enterprise CA, bộ nhớ đệm (cache / 캐시) intermediate hoặc bỏ qua cảnh báo mà máy khách (client / 클라이언트) khác không có.

**“Certificate hết hạn mới là lỗi TLS phổ biến nhất.”** chuỗi (chain / 사슬) thiếu, hostname mismatch, trust store khác nhau và clock sai cũng rất thường gặp.

**“gốc (root / 루트) CA phải được máy chủ (server / 서버) gửi xuống.”** Thường máy khách (client / 클라이언트) đã có gốc (root / 루트); máy chủ (server / 서버) nên gửi leaf và intermediate cần thiết.

**“`curl -k` sửa được lỗi certificate.”** Nó chỉ bỏ xác minh, che đi lỗi trust thực tế.

**“mTLS thay thế authorization.”** Nó xác thực máy khách (client / 클라이언트) định danh (identity / 식별자) ở tầng vận chuyển (transport layer / 전송 계층) nhưng chính sách (policy / 정책) ứng dụng vẫn cần riêng.

**“TLS termination ở bộ cân bằng tải (load balancer / 로드 밸런서) nghĩa backend cũng đang dùng TLS.”** Hai hop là hai liên kết (connection / 연결) khác nhau.

## Kết nối kiến thức

Đọc cùng [TCP/HTTP/TLS](./tcp_http_tls.md), [reverse proxy/load balancing](./reverse_proxy_load_balancing.md), [DNS internals](./dns_resolution_internals.md), [time/NTP](../05_system/time_clock_ntp.md) và [Java backend incident playbook](../09_production/java_backend_incident_playbook.md). TLS là điểm giao giữa networking, bảo mật (security / 보안), thời gian chạy (runtime / 런타임) cấu hình (configuration / 구성) và vòng đời (lifecycle / 생명주기) automation.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [dns resolution internals](./dns_resolution_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
