# TLS, PKI và vòng đời chứng chỉ

Khi một ứng dụng truy cập `https://service.example.com`, việc “dùng HTTPS” thực tế là kết quả của nhiều cơ chế phối hợp: phân giải DNS, kết nối TCP, bắt tay TLS, kiểm tra chứng chỉ, thương lượng thuật toán mật mã, thiết lập khóa phiên rồi mới truyền HTTP đã mã hóa.

Trong production, các lỗi như `certificate expired`, `unknown CA`, `hostname verification failed`, `handshake_failure`, `unable to find valid certification path` hoặc `SSLHandshakeException` thường không nằm ở HTTP logic. Chúng thuộc lớp **TLS và hạ tầng khóa công khai (Public Key Infrastructure - PKI)**.

## TLS giải quyết những gì?

TLS chủ yếu cung cấp ba thuộc tính:

- **bí mật (confidentiality)**: bên thứ ba trên đường truyền không dễ đọc nội dung;
- **toàn vẹn (integrity)**: dữ liệu bị sửa đổi có thể được phát hiện;
- **xác thực (authentication)**: client có cơ chế kiểm tra danh tính của server, và trong mTLS server cũng có thể kiểm tra client.

TLS không tự bảo đảm application đúng, server không bị xâm nhập hay dữ liệu lưu trữ an toàn. Nó bảo vệ một phần đường truyền và danh tính endpoint theo trust model của PKI.

## Vì sao chỉ mã hóa là chưa đủ?

Nếu client mã hóa dữ liệu cho một attacker mà tưởng đó là server thật, confidentiality không giúp nhiều. Vì vậy client cần biết public key đang dùng thực sự thuộc endpoint nào.

PKI giải bài toán này bằng chuỗi tin cậy (chain of trust).

## Chứng chỉ X.509

Chứng chỉ TLS server thường là chứng chỉ **X.509** chứa các thông tin như:

- public key;
- subject/issuer;
- thời hạn hiệu lực;
- serial number;
- extensions;
- Subject Alternative Name (SAN);
- chữ ký của CA phát hành.

Kiểm tra file chứng chỉ:

```bash
openssl x509 -in server.crt -noout -text
```

Xem ngày hiệu lực:

```bash
openssl x509 -in server.crt -noout -dates
```

## Private key và certificate khác nhau

Chứng chỉ có thể được phân phối công khai; private key phải được bảo vệ.

Mental model:

```text
private key
    -> chứng minh quyền sở hữu identity key

certificate
    -> public key + identity metadata + CA signature
```

Nếu private key bị lộ, attacker có thể giả mạo endpoint trong nhiều tình huống phù hợp. Thay certificate nhưng giữ private key đã bị lộ không giải quyết được sự cố.

## CA là gì?

**Tổ chức chứng thực (Certificate Authority - CA)** ký chứng chỉ và đóng vai trò bên thứ ba được trust.

Client thường có **trust store** chứa các root CA được tin cậy. Server không cần certificate trực tiếp do root CA ký; thường có intermediate CA ở giữa.

```text
Root CA
   ↓ ký
Intermediate CA
   ↓ ký
Server certificate
```

Client xác minh từng chữ ký trong chain cho tới một trust anchor nó đã tin.

## Tại sao cần intermediate CA?

Root private key có giá trị cực lớn và nên được bảo vệ rất chặt. Thay vì dùng root trực tiếp hàng ngày, tổ chức dùng intermediate CA để phát hành certificate.

Nếu intermediate có vấn đề, có thể thu hồi hoặc thay intermediate mà không nhất thiết thay root trust anchor trên toàn bộ client.

## Server phải gửi chain nào?

Server thường gửi:

```text
leaf/server certificate
+
intermediate certificate(s)
```

Root certificate thường không cần gửi vì client đã có trong trust store.

Một lỗi production phổ biến là server chỉ cấu hình leaf certificate mà quên intermediate. Một số browser vẫn có thể hoạt động do cache/intermediate fetching, nhưng Java hoặc client khác thất bại.

Kiểm tra chain server:

```bash
openssl s_client -connect service.example.com:443 -servername service.example.com -showcerts
```

`-servername` gửi SNI, rất quan trọng khi nhiều hostname dùng chung IP.

## Hostname verification

Client không chỉ kiểm tra certificate do CA tin cậy ký; nó còn phải kiểm tra hostname đang truy cập có nằm trong certificate không.

Hiện nay **Subject Alternative Name (SAN)** là trường quan trọng cho hostname/IP identity.

Ví dụ certificate có:

```text
DNS:api.example.com
DNS:*.internal.example.com
```

thì truy cập hostname khác có thể fail dù certificate chưa hết hạn và CA hợp lệ.

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

**Server Name Indication (SNI)** cho phép client gửi hostname trong TLS handshake để reverse proxy/load balancer chọn certificate phù hợp trước khi HTTP Host header được đọc.

```text
client -> TCP connect tới IP
client -> TLS ClientHello + SNI=api.example.com
server -> chọn certificate cho api.example.com
```

Nếu client không gửi SNI hoặc gửi hostname sai, server có thể trả certificate mặc định không match.

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

Chi tiết thực tế phức tạp hơn, nhưng mental model này đủ để phân lớp lỗi.

## TLS 1.2 và TLS 1.3

TLS 1.3 loại bỏ nhiều thuật toán cũ, đơn giản hóa handshake và giảm round trip trong nhiều trường hợp. Một số cấu hình legacy chỉ hỗ trợ TLS 1.0/1.1 hoặc cipher cũ có thể không tương thích với client hiện đại.

Kiểm tra:

```bash
openssl s_client -connect host:443 -servername host -tls1_2
openssl s_client -connect host:443 -servername host -tls1_3
```

Tùy phiên bản OpenSSL và server.

## Cipher suite

Cipher suite mô tả tập thuật toán dùng cho các phần của TLS. Trong TLS 1.3, cấu trúc tên đơn giản hơn so với TLS 1.2.

Không nên chọn cipher chỉ vì “mạnh nhất” theo cảm giác. Cần cân bằng:

- security policy;
- client compatibility;
- hardware acceleration;
- compliance;
- protocol version.

## Forward secrecy

Các cơ chế trao đổi khóa tạm thời như ECDHE giúp đạt **bí mật chuyển tiếp (forward secrecy)**: nếu long-term private key bị lộ trong tương lai, attacker không dễ giải mã lại các session cũ đã capture trước đó.

Đây là lý do modern TLS ưu tiên ephemeral key exchange.

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

Let's Encrypt/ACME giúp tự động hóa certificate public, nhưng hệ thống private PKI cũng cần workflow tương tự.

Một hệ thống tốt phải kiểm tra cả việc renewal đã tạo certificate mới **và** service đã thực sự dùng certificate mới.

## Reload certificate

Nhiều reverse proxy có thể reload certificate mà không downtime lớn:

```bash
nginx -t && systemctl reload nginx
```

Nhưng semantics phụ thuộc ứng dụng. Một Java service có thể cần restart nếu keystore chỉ được đọc lúc startup.

## Java trust store và key store

Trong Java, **trust store** chứa certificate/CA mà JVM tin. **Key store** thường chứa private key và certificate identity của chính ứng dụng khi cần server TLS hoặc mTLS client authentication.

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

thường cần kiểm tra trust chain/trust store thay vì disable certificate verification.

## Không tắt TLS verification để “fix” production

Các lựa chọn như `curl -k`, trust-all `X509TrustManager` hoặc tắt hostname verification chỉ nên dùng trong chẩn đoán có kiểm soát.

Nếu đưa vào production, bạn đã loại bỏ phần authentication quan trọng của TLS và mở đường cho man-in-the-middle.

## mTLS

Trong **mutual TLS (mTLS)**, server yêu cầu client certificate.

```text
client verify server certificate
+
server verify client certificate
```

mTLS cung cấp identity ở transport layer, thường dùng service-to-service hoặc internal infrastructure.

Nhưng mTLS không tự mô hình hóa authorization nghiệp vụ. Một client có certificate hợp lệ chưa chắc được phép gọi mọi API.

## Certificate revocation

Nếu private key bị compromise trước khi certificate hết hạn, cần cơ chế thu hồi.

Hai khái niệm truyền thống:

- CRL (Certificate Revocation List);
- OCSP (Online Certificate Status Protocol).

Trong thực tế, behavior kiểm tra revocation phụ thuộc client/platform và policy. Không nên giả định mọi client luôn kiểm tra OCSP giống nhau.

## OCSP stapling

Server có thể lấy OCSP response rồi “đính kèm” vào handshake để client không cần tự query CA responder cho mỗi connection.

Điều này có thể giảm latency và cải thiện privacy/reliability.

## TLS termination

Trong architecture có load balancer:

```text
client
  ↓ TLS
load balancer
  ↓ HTTP hoặc TLS lần nữa
backend
```

TLS có thể terminate ở load balancer. Nếu backend nhận HTTP plaintext, traffic vẫn được bảo vệ bên ngoài nhưng không mã hóa đoạn nội bộ.

Nếu compliance hoặc threat model yêu cầu, backend hop có thể dùng TLS/mTLS riêng.

## End-to-end TLS không luôn nghĩa một session

Một request có thể đi qua nhiều TLS session:

```text
client --TLS A--> edge
edge   --TLS B--> internal proxy
proxy  --TLS C--> backend
```

Mỗi hop có certificate/trust store và failure mode riêng.

## ALPN và HTTP/2

**Application-Layer Protocol Negotiation (ALPN)** cho phép client/server chọn protocol ứng dụng như HTTP/2 trong TLS handshake.

Kiểm tra bằng OpenSSL tùy phiên bản:

```bash
openssl s_client -connect host:443 -servername host -alpn h2,http/1.1
```

Nếu HTTP/2 không được thương lượng, nguyên nhân có thể nằm ở TLS/ALPN config chứ không phải HTTP application code.

## Session resumption

TLS session resumption giảm chi phí handshake cho connection mới bằng cách tái sử dụng thông tin phiên trước qua session ticket/PSK tùy protocol.

Điều này giảm CPU và latency trong hệ thống connection churn cao.

## Handshake CPU cost

Public-key cryptography trong handshake tốn CPU hơn symmetric encryption sau khi session key đã được thiết lập. Nếu server tạo lượng lớn connection TLS mới mỗi giây, handshake có thể trở thành bottleneck CPU.

Connection reuse, TLS session resumption và hardware acceleration có thể ảnh hưởng capacity.

## TLS failure theo tầng

Một flow chẩn đoán:

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

Corporate proxy hoặc security appliance đôi khi giải mã TLS bằng cách phát certificate từ private enterprise CA. Máy công ty trust CA này nên browser hoạt động, nhưng JVM/container không có CA đó có thể fail.

Đây là failure mode rất phổ biến khi “browser vào được nhưng Java không gọi được”.

Giải pháp đúng là hiểu trust chain và cài CA phù hợp theo policy, không phải tắt verification.

## Certificate pinning

Một số client pin public key/certificate cụ thể để giảm phụ thuộc trust store rộng. Pinning tăng security trong một threat model nhưng làm rotation phức tạp; cấu hình sai có thể tự gây outage khi certificate/key đổi.

## Secrets và file permission

Private key cần quyền hạn chế:

```bash
chmod 600 server.key
chown root:service server.key
```

Quyền chính xác phụ thuộc service model. Không nên để private key world-readable.

## Mô hình tư duy

TLS có thể xem là hai bài toán lồng nhau:

```text
1. xác minh identity qua PKI
2. thiết lập session keys để bảo vệ data
```

Nếu chỉ nhìn “port 443 mở” thì ta mới xác minh tầng TCP, chưa chứng minh TLS trust đã hoạt động.

## Những hiểu lầm phổ biến

**“HTTPS hoạt động thì certificate chắc đúng.”** Có thể browser đang trust enterprise CA, cache intermediate hoặc bỏ qua cảnh báo mà client khác không có.

**“Certificate hết hạn mới là lỗi TLS phổ biến nhất.”** Chain thiếu, hostname mismatch, trust store khác nhau và clock sai cũng rất thường gặp.

**“Root CA phải được server gửi xuống.”** Thường client đã có root; server nên gửi leaf và intermediate cần thiết.

**“`curl -k` sửa được lỗi certificate.”** Nó chỉ bỏ xác minh, che đi lỗi trust thực tế.

**“mTLS thay thế authorization.”** Nó xác thực client identity ở transport layer nhưng policy ứng dụng vẫn cần riêng.

**“TLS termination ở load balancer nghĩa backend cũng đang dùng TLS.”** Hai hop là hai connection khác nhau.

## Kết nối kiến thức

Đọc cùng [TCP/HTTP/TLS](./tcp_http_tls.md), [reverse proxy/load balancing](./reverse_proxy_load_balancing.md), [DNS internals](./dns_resolution_internals.md), [time/NTP](../05_system/time_clock_ntp.md) và [Java backend incident playbook](../09_production/java_backend_incident_playbook.md). TLS là điểm giao giữa networking, security, runtime configuration và lifecycle automation.