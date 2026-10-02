# DNS Resolution Internals trên Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **DNS Resolution Internals trên Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ứng dụng (application / 애플리케이션) không nhất thiết gọi DNS trực tiếp** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **/etc/nsswitch.conf và thứ tự lookup** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối DNS query với cache, delegation và authoritative server, giúp xác định độ trễ hoặc câu trả lời sai phát sinh ở lớp nào.

Khi ứng dụng (application / 애플리케이션) gọi một hostname như:

```text
api.example.com
```

nó không thể tự gửi packet tới “tên miền”. mạng (network / 네트워크) ngăn xếp (stack / 스택) cần địa chỉ IP. Quá trình chuyển hostname thành address gọi là **phân giải tên (name resolution)**.

DNS thường được mô tả đơn giản là “đổi lĩnh vực (domain / 도메인) thành IP”, nhưng trong Linux thực tế còn có `/etc/hosts`, NSS, stub resolver, cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시), DNS máy chủ (server / 서버), tìm kiếm (search / 검색) lĩnh vực (domain / 도메인), TTL, nhiều bản ghi (record / 레코드) types và IPv4/IPv6 preference.

Hiểu các lớp này rất quan trọng khi gặp lỗi kiểu:

```text
Could not resolve host
Temporary failure in name resolution
UnknownHostException
SERVFAIL
NXDOMAIN
```

## Ứng dụng (application / 애플리케이션) không nhất thiết gọi DNS trực tiếp

Một chương trình C thường gọi hàm như:

```c
getaddrinfo()
```

Java có API tương ứng như:

```java
InetAddress.getByName("api.example.com")
```

Ứng dụng (application / 애플리케이션) yêu cầu hệ thống phân giải tên. Resolver thư viện (library / 라이브러리) sau đó mới quyết định nguồn dữ liệu nào được dùng.

Do đó câu “DNS lỗi” đôi khi chưa chính xác: lỗi có thể nằm ở `/etc/hosts`, NSS chính sách (policy / 정책), cục bộ (local / 로컬) resolver hoặc upstream DNS.

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **/etc/nsswitch.conf và thứ tự lookup** tiếp nhận điểm tựa từ **Ứng dụng (application / 애플리케이션) không nhất thiết gọi DNS trực tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **/etc/hosts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/etc/nsswitch.conf` và thứ tự lookup

Linux dùng **Name dịch vụ (service / 서비스) Switch (NSS)** để xác định nguồn dữ liệu cho nhiều loại lookup.

Kiểm tra:

```bash
grep '^hosts:' /etc/nsswitch.conf
```

Ví dụ:

```text
hosts: files dns
```

nghĩa là resolver có thể kiểm tra `/etc/hosts` trước rồi mới DNS.

Một hệ thống dùng systemd-resolved có thể có dòng khác như:

```text
hosts: files myhostname resolve [!UNAVAIL=return] dns
```

Chi tiết phụ thuộc phân phối (distribution / 분포).

Điểm quan trọng là hostname resolution không nhất thiết đi thẳng ra DNS máy chủ (server / 서버).

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **/etc/hosts** tiếp nhận điểm tựa từ **/etc/nsswitch.conf và thứ tự lookup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **/etc/resolv.conf** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/etc/hosts`

Tệp (file / 파일) `/etc/hosts` cung cấp ánh xạ tĩnh:

```text
127.0.0.1 localhost
10.0.0.20 internal-api
```

Nếu ứng dụng (application / 애플리케이션) resolve `internal-api`, entry cục bộ (local / 로컬) có thể override DNS tùy NSS thứ tự (order / 순서).

Gỡ lỗi (debug / 디버그):

```bash
getent hosts internal-api
```

`getent` rất hữu ích vì nó đi qua NSS và gần với cách nhiều ứng dụng (application / 애플리케이션) resolve hơn `dig`.

Đây là khác biệt quan trọng:

```bash
dig internal-api
```

hỏi DNS trực tiếp, còn:

```bash
getent hosts internal-api
```

phản ánh hệ thống (system / 시스템) resolver/NSS.

Nếu hai command trả kết quả khác nhau, vấn đề có thể nằm trước DNS truy vấn (query / 쿼리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, **/etc/resolv.conf** tiếp nhận điểm tựa từ **/etc/hosts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tìm kiếm (search / 검색) lĩnh vực (domain / 도메인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/etc/resolv.conf`

Tệp (file / 파일) này truyền thống chứa resolver cấu hình (configuration / 구성):

```bash
cat /etc/resolv.conf
```

Có thể thấy:

```text
nameserver 10.0.0.2
search corp.example.com
options timeout:2 attempts:2
```

Nhưng trên nhiều distro hiện đại, `/etc/resolv.conf` có thể là symlink tới tệp (file / 파일) được quản lý bởi systemd-resolved, NetworkManager hoặc công cụ (tool / 도구) khác.

Kiểm tra:

```bash
ls -l /etc/resolv.conf
```

Không nên edit trực tiếp tệp (file / 파일) generated nếu mạng (network / 네트워크) manager sẽ ghi đè lại.

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **Tìm kiếm (search / 검색) lĩnh vực (domain / 도메인)** tiếp nhận điểm tựa từ **/etc/resolv.conf** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Recursive resolver và authoritative máy chủ (server / 서버)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm (search / 검색) lĩnh vực (domain / 도메인)

Nếu cấu hình (config / 설정) có:

```text
search corp.example.com
```

và ứng dụng (application / 애플리케이션) resolve:

```text
db01
```

resolver có thể thử:

```text
db01.corp.example.com
```

Điều này tiện trong mạng nội bộ nhưng cũng tạo ambiguity. Một hostname ngắn có thể resolve khác nhau giữa servers tùy tìm kiếm (search / 검색) lĩnh vực (domain / 도메인).

Trong môi trường vận hành (production / 운영 환경) cấu hình (config / 설정), FQDN rõ ràng thường giảm surprise.

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **Recursive resolver và authoritative máy chủ (server / 서버)** tiếp nhận điểm tựa từ **Tìm kiếm (search / 검색) lĩnh vực (domain / 도메인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TTL và bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Recursive resolver và authoritative máy chủ (server / 서버)

DNS hierarchy có nhiều vai trò.

Ứng dụng (application / 애플리케이션) thường gửi truy vấn (query / 쿼리) tới **recursive resolver**. Resolver này có thể hỏi các DNS servers khác và bộ nhớ đệm (cache / 캐시) kết quả.

Authoritative DNS máy chủ (server / 서버) chịu trách nhiệm trả lời records cho zone mà nó quản lý.

Mô hình tư duy (mental model / 사고 모델):

```text
application
    ↓
stub resolver
    ↓
recursive DNS resolver
    ↓
root / TLD / authoritative chain nếu cache miss
```

Trong doanh nghiệp, recursive resolver có thể là corporate DNS, cloud resolver hoặc cục bộ (local / 로컬) dịch vụ (service / 서비스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, **TTL và bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Recursive resolver và authoritative máy chủ (server / 서버)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java DNS caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TTL và bộ nhớ đệm (cache / 캐시)

DNS bản ghi (record / 레코드) có **TTL — thời gian (time / 시간) To Live**, chỉ thời gian bộ nhớ đệm (cache / 캐시) có thể giữ answer.

```bash
dig api.example.com
```

Đầu ra (output / 출력) hiển thị TTL.

Nếu DNS bản ghi (record / 레코드) đổi từ IP A sang IP B, máy khách (client / 클라이언트) không nhất thiết thấy B ngay. Resolver bộ nhớ đệm (cache / 캐시) vẫn có thể trả A cho tới khi TTL hết.

Nhưng actual caching còn có thể tồn tại ở nhiều tầng (layer / 계층):

- recursive resolver;
- OS/cục bộ (local / 로컬) resolver;
- JVM;
- ứng dụng (application / 애플리케이션) bộ nhớ đệm (cache / 캐시);
- trình duyệt (browser / 브라우저);
- proxy.

Do đó “DNS TTL là 60 giây” không đảm bảo mọi ứng dụng (application / 애플리케이션) refresh sau đúng 60 giây nếu thời gian chạy (runtime / 런타임) có bộ nhớ đệm (cache / 캐시) riêng.

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **Java DNS caching** tiếp nhận điểm tựa từ **TTL và bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bản ghi (record / 레코드) A và AAAA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java DNS caching

JVM có cơ chế bộ nhớ đệm (cache / 캐시) DNS kết quả (result / 결과). hành vi (behavior / 동작) phụ thuộc JVM/bảo mật (security / 보안) properties/phiên bản (version / 버전).

Điều này có impact khi backend phụ thuộc (dependency / 의존성) thay IP nhưng ứng dụng (application / 애플리케이션) giữ liên kết (connection / 연결) hoặc DNS kết quả (result / 결과) quá lâu.

Không nên tùy tiện đặt DNS TTL JVM cực thấp hoặc bằng 0; DNS truy vấn (query / 쿼리) volume và phụ thuộc (dependency / 의존성) hành vi (behavior / 동작) cũng cần cân nhắc.

Khi điều tra Java `UnknownHostException`, cần phân biệt:

- resolver thực sự không trả IP;
- JVM bộ nhớ đệm (cache / 캐시) negative kết quả (result / 결과);
- mạng (network / 네트워크) tới DNS máy chủ (server / 서버) lỗi;
- hostname cấu hình (config / 설정) sai.

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **Bản ghi (record / 레코드) A và AAAA** tiếp nhận điểm tựa từ **Java DNS caching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CNAME** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản ghi (record / 레코드) A và AAAA

`A` bản ghi (record / 레코드) chứa IPv4 address.

`AAAA` bản ghi (record / 레코드) chứa IPv6 address.

```bash
dig A example.com
dig AAAA example.com
```

Một hostname có thể có cả hai. ứng dụng (application / 애플리케이션)/thời gian chạy (runtime / 런타임) có thể thử IPv6 trước hoặc dùng Happy Eyeballs hành vi (behavior / 동작).

Nếu IPv6 address resolve được nhưng IPv6 routing không hoạt động, liên kết (connection / 연결) có thể delay/thất bại (fail / 실패) theo cách khó hiểu.

Vì vậy DNS success không đồng nghĩa mạng (network / 네트워크) reachability success.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, **CNAME** tiếp nhận điểm tựa từ **Bản ghi (record / 레코드) A và AAAA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MX, TXT, SRV và các bản ghi (record / 레코드) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CNAME

**CNAME** tạo alias tới chuẩn gốc (canonical / 정본) name.

Ví dụ:

```text
api.example.com CNAME lb.example.net
```

Resolver tiếp tục resolve chuẩn gốc (canonical / 정본) mục tiêu (target / 대상).

CNAME thường dùng cho CDN/bộ cân bằng tải (load balancer / 로드 밸런서) dịch vụ (service / 서비스), nhưng chuỗi (chain / 사슬) dài có thể tăng resolution công việc (work / 작업) và tạo phụ thuộc (dependency / 의존성) vào nhiều zones.

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **MX, TXT, SRV và các bản ghi (record / 레코드) khác** tiếp nhận điểm tựa từ **CNAME** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NXDOMAIN và SERVFAIL khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MX, TXT, SRV và các bản ghi (record / 레코드) khác

DNS không chỉ lưu IP.

- `MX`: mail exchange;
- `TXT`: arbitrary văn bản (text / 텍스트), thường dùng SPF/lĩnh vực (domain / 도메인) xác minh (verification / 확인);
- `SRV`: dịch vụ (service / 서비스) location với cổng (port / 포트)/priority;
- `NS`: authoritative name servers;
- `PTR`: reverse DNS.

Khám phá dịch vụ (service discovery / 서비스 디스커버리) các hệ thống (systems / 시스템들) có thể dùng SRV hoặc custom DNS schemes.

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **NXDOMAIN và SERVFAIL khác nhau** tiếp nhận điểm tựa từ **MX, TXT, SRV và các bản ghi (record / 레코드) khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Negative caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NXDOMAIN và SERVFAIL khác nhau

`NXDOMAIN` nghĩa tên được hỏi không tồn tại theo DNS phản hồi (response / 응답).

`SERVFAIL` nghĩa resolver/máy chủ (server / 서버) không thể hoàn thành truy vấn (query / 쿼리), ví dụ upstream/DNSSEC/delegation issue.

Hai lỗi này cần lập luận (reasoning / 추론) khác nhau.

```bash
dig nonexistent.example.com
```

Xem status trong header:

```text
status: NXDOMAIN
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, **Negative caching** tiếp nhận điểm tựa từ **NXDOMAIN và SERVFAIL khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **systemd-resolved** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Negative caching

Không chỉ successful answers được bộ nhớ đệm (cache / 캐시). Kết quả “không tồn tại” cũng có thể được bộ nhớ đệm (cache / 캐시) theo DNS rules.

Do đó nếu bản ghi (record / 레코드) vừa được tạo sau khi máy khách (client / 클라이언트) đã nhận NXDOMAIN, máy khách (client / 클라이언트)/resolver có thể tiếp tục thấy thất bại (failure / 실패) một thời gian.

Đây là lý do “tôi vừa thêm DNS bản ghi (record / 레코드) rồi nhưng app vẫn không resolve” không nhất thiết do cập nhật (update / 업데이트) thất bại.

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **systemd-resolved** tiếp nhận điểm tựa từ **Negative caching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Split DNS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## systemd-resolved

Một số Linux distributions dùng `systemd-resolved`.

Kiểm tra:

```bash
systemctl status systemd-resolved
resolvectl status
```

`resolvectl` có thể cho biết DNS máy chủ (server / 서버) theo giao diện (interface / 인터페이스), tìm kiếm (search / 검색) domains và hiện tại (current / 현재) resolver trạng thái (state / 상태).

Truy vấn (query / 쿼리):

```bash
resolvectl query api.example.com
```

Điều này đặc biệt hữu ích khi VPN/giao diện (interface / 인터페이스) khác nhau có DNS máy chủ (server / 서버) riêng.

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **Split DNS** tiếp nhận điểm tựa từ **systemd-resolved** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **dig, host, nslookup, getent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Split DNS

Doanh nghiệp/VPN thường dùng **split DNS**: một số domains được resolve qua DNS nội bộ, các domains khác qua công khai (public / 공개) resolver.

Ví dụ:

```text
*.corp.example.com → VPN DNS
other domains      → normal DNS
```

Nếu VPN tuyến (route / 경로) hoạt động nhưng DNS routing/cấu hình (config / 설정) không đúng, người dùng (user / 사용자) có thể ping nội bộ (internal / 내부) IP nhưng không resolve nội bộ (internal / 내부) hostname.

Đây là một ví dụ mạng (network / 네트워크) routing và name resolution là hai điều khiển (control / 제어) planes khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, **dig, host, nslookup, getent** tiếp nhận điểm tựa từ **Split DNS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tracing DNS bằng packet capture** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `dig`, `host`, `nslookup`, `getent`

Các tools trả lời câu hỏi khác nhau.

`dig` cho DNS giao thức (protocol / 프로토콜) details:

```bash
dig api.example.com
```

`dig @server` hỏi resolver cụ thể:

```bash
dig @8.8.8.8 example.com
```

`getent hosts` đi qua NSS:

```bash
getent hosts api.example.com
```

`host` và `nslookup` tiện cho lookup nhanh nhưng `dig` thường chi tiết hơn.

Khi ứng dụng (application / 애플리케이션) thất bại (fail / 실패) nhưng `dig` success, hãy thử `getent` trước khi kết luận ứng dụng (application / 애플리케이션) bug.

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **Tracing DNS bằng packet capture** tiếp nhận điểm tựa từ **dig, host, nslookup, getent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DNS và bộ chứa (container / 컨테이너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tracing DNS bằng packet capture

DNS truyền thống thường dùng UDP 53, và TCP trong một số trường hợp. DNS over TLS/HTTPS thay đổi vận chuyển (transport / 전송).

Với cục bộ (local / 로컬) resolver thông thường:

```bash
sudo tcpdump -ni any port 53
```

Sau đó chạy:

```bash
getent hosts api.example.com
```

Nếu không thấy packet DNS, answer có thể đến từ `/etc/hosts`, cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시) hoặc resolver đường dẫn (path / 경로) khác.

Nếu truy vấn (query / 쿼리) đi ra nhưng không có phản hồi (response / 응답), phạm vi (scope / 범위) chuyển sang tuyến (route / 경로)/firewall/DNS máy chủ (server / 서버).

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **DNS và bộ chứa (container / 컨테이너)** tiếp nhận điểm tựa từ **Tracing DNS bằng packet capture** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kubernetes liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DNS và bộ chứa (container / 컨테이너)

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) thường inject `/etc/resolv.conf` riêng vào bộ chứa (container / 컨테이너).

```bash
cat /etc/resolv.conf
```

bên host và bộ chứa (container / 컨테이너) có thể khác.

Docker có embedded DNS ở một số mạng (network / 네트워크) modes; Kubernetes thường dùng CoreDNS và dịch vụ (service / 서비스) names.

Do đó “host resolve được nhưng bộ chứa (container / 컨테이너) không resolve” không mâu thuẫn. Chúng đang dùng resolver ngữ cảnh (context / 맥락) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, sau nội dung của **DNS và bộ chứa (container / 컨테이너)**, **Kubernetes liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **DNS và tải (load / 로드) balancing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kubernetes liên kết (connection / 연결)

Trong Kubernetes, hostname như:

```text
service.namespace.svc.cluster.local
```

được cluster DNS resolve tới dịch vụ (service / 서비스) virtual IP hoặc records thích hợp.

Nếu CoreDNS unhealthy hoặc pod DNS cấu hình (config / 설정) sai, ứng dụng (application / 애플리케이션) có thể báo phụ thuộc (dependency / 의존성) thất bại (failure / 실패) dù mạng (network / 네트워크) tuyến (route / 경로) tới raw IP vẫn hoạt động.

Linux DNS fundamentals vẫn áp dụng; Kubernetes chỉ thêm service-discovery tầng (layer / 계층).

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **DNS và tải (load / 로드) balancing** tiếp nhận điểm tựa từ **Kubernetes liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trường hợp (case / 사례): curl resolve được nhưng Java không** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DNS và tải (load / 로드) balancing

Một DNS name có thể trả nhiều A/AAAA records:

```text
api.example.com → 10.0.0.10
                  10.0.0.11
                  10.0.0.12
```

Máy khách (client / 클라이언트) hành vi (behavior / 동작) quyết định nó dùng address nào và failover ra sao.

DNS round-robin không có health-awareness đầy đủ như ứng dụng (application / 애플리케이션) bộ cân bằng tải (load balancer / 로드 밸런서). máy khách (client / 클라이언트) có thể bộ nhớ đệm (cache / 캐시) một IP đã unhealthy.

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **DNS và tải (load / 로드) balancing** cho ta quy tắc; **Trường hợp (case / 사례): curl resolve được nhưng Java không** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례): resolve chậm 5 giây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): `curl` resolve được nhưng Java không

Kiểm tra Java tiến trình (process / 프로세스) có đang dùng hostname giống hệt không, thời gian chạy (runtime / 런타임) bộ nhớ đệm (cache / 캐시) thế nào, bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스) nào và resolver cấu hình (config / 설정) nào.

Có thể kiểm tra OS:

```bash
getent ahosts api.example.com
```

rồi JVM/log ứng dụng (application / 애플리케이션).

Không nên restart JVM chỉ để flush DNS mà chưa hiểu TTL/bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책); restart có thể che kiến trúc (architecture / 아키텍처) issue.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, **Trường hợp (case / 사례): curl resolve được nhưng Java không** cho ta quy tắc; **Trường hợp (case / 사례): resolve chậm 5 giây** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **DNSSEC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): resolve chậm 5 giây

Potential causes:

- DNS máy chủ (server / 서버) đầu tiên hết thời gian chờ (timeout / 타임아웃) rồi resolver thử máy chủ (server / 서버) thứ hai;
- IPv6/AAAA hành vi (behavior / 동작);
- tìm kiếm (search / 검색) lĩnh vực (domain / 도메인) tạo nhiều queries;
- unreachable resolver qua VPN;
- packet drop/firewall;
- DNS máy chủ (server / 서버) overloaded.

Quan sát:

```bash
time getent hosts api.example.com
resolvectl status
sudo tcpdump -ni any port 53
```

Timeline packet thường cho thấy truy vấn (query / 쿼리) nào chờ hết thời gian chờ (timeout / 타임아웃).

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **Trường hợp (case / 사례): resolve chậm 5 giây** cho ta quy tắc; **DNSSEC** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DNSSEC

DNSSEC thêm cryptographic kiểm tra hợp lệ (validation / 검증) để chống giả mạo dữ liệu DNS trong trust chuỗi (chain / 사슬). Nếu kiểm tra hợp lệ (validation / 검증) thất bại (fail / 실패), resolver có thể trả `SERVFAIL` dù authoritative dữ liệu (data / 데이터) tồn tại.

DNSSEC không mã hóa truy vấn (query / 쿼리); nó bảo vệ tính xác thực/toàn vẹn của DNS dữ liệu (data / 데이터).

Không nên nhầm DNSSEC với DNS over HTTPS (DoH) hoặc DNS over TLS (DoT), vốn tập trung vào vận chuyển (transport / 전송) confidentiality/integrity giữa máy khách (client / 클라이언트) và resolver.

> **Chuyển mạch:** Ở chặng này của **DNS Resolution Internals trên Linux**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **DNSSEC** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Khi resolve hostname, hãy nghĩ theo chuỗi:

```text
application
   ↓
NSS / resolver library
   ↓
/etc/hosts hoặc local resolver/cache
   ↓
configured recursive DNS
   ↓
DNS hierarchy / authoritative server
   ↓
A/AAAA/CNAME/... answer
   ↓
application cache
```

Sau khi có IP, networking mới tiếp tục với tuyến (route / 경로)/TCP/TLS.

DNS success chỉ giải quyết câu hỏi “địa chỉ nào?”, không giải quyết câu hỏi “có kết nối được không?”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DNS Resolution Internals trên Linux**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Xem thêm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“`dig` success nghĩa ứng dụng (application / 애플리케이션) chắc chắn resolve được.”** ứng dụng (application / 애플리케이션) có thể đi qua NSS/bộ nhớ đệm (cache / 캐시)/thời gian chạy (runtime / 런타임) khác.

**“DNS bản ghi (record / 레코드) đổi là mọi máy khách (client / 클라이언트) thấy ngay.”** TTL và nhiều lớp bộ nhớ đệm (cache / 캐시) làm propagation có độ trễ.

**“NXDOMAIN và hết thời gian chờ (timeout / 타임아웃) là cùng lỗi DNS.”** Một bên là negative answer; bên kia có thể là vận chuyển (transport / 전송)/resolver thất bại (failure / 실패).

**“Host resolve được thì bộ chứa (container / 컨테이너) cũng resolve được.”** Resolver cấu hình (configuration / 구성) có thể khác theo không gian tên (namespace / 네임스페이스)/thời gian chạy (runtime / 런타임).

**“DNS chỉ có A bản ghi (record / 레코드).”** DNS là hệ thống dữ liệu phân tán với nhiều bản ghi (record / 레코드) types.

**“DNSSEC mã hóa DNS.”** DNSSEC xác thực dữ liệu, không cung cấp vận chuyển (transport / 전송) encryption theo nghĩa DoH/DoT.

> **Chuyển mạch:** Trong **DNS Resolution Internals trên Linux**, **Xem thêm** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Xem thêm

Các liên kết này là bước bàn giao sang cơ chế liên quan. Hãy mở chúng theo câu hỏi còn bỏ ngỏ, không coi danh sách link là phần kết luận tự thân.

- [Networking, DNS, sockets và ports](./networking_dns_sockets_ports.md)
- [IP routing, NAT và conntrack](./ip_routing_nat_conntrack.md)
- [TCP, HTTP và TLS](./tcp_http_tls.md)
- [Reverse proxy và load balancing](./reverse_proxy_load_balancing.md)
- [Java backend incident playbook](../09_production/java_backend_incident_playbook.md)

> **Bàn giao:** Sau **Xem thêm**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
