# Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Proxy là gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vì sao cần reverse proxy?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối reverse proxy với load balancing, health check và backpressure, để truy nguyên request bị định tuyến hoặc dồn tải sai.

Một backend môi trường vận hành (production / 운영 환경) hiếm khi để máy khách (client / 클라이언트) kết nối trực tiếp tới Java tiến trình (process / 프로세스). yêu cầu (request / 요청) thường đi qua nhiều lớp:

```text
client
  ↓
DNS
  ↓
CDN / WAF
  ↓
load balancer
  ↓
reverse proxy
  ↓
application server
  ↓
database / downstream service
```

Mỗi lớp thêm khả năng kiểm soát, nhưng cũng thêm trạng thái (state / 상태), hết thời gian chờ (timeout / 타임아웃) và dạng thất bại (failure mode / 실패 모드). Khi người dùng (user / 사용자) nhận `502`, `504` hoặc yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃), muốn chẩn đoán đúng cần hiểu từng lớp đang làm gì.

## Proxy là gì?

**Proxy** là thành phần đứng giữa hai phía và chuyển tiếp traffic.

Có hai khái niệm thường gặp:

- **forward proxy** đại diện cho máy khách (client / 클라이언트) khi đi ra ngoài;
- **reverse proxy** đại diện cho máy chủ (server / 서버)/ứng dụng (application / 애플리케이션) khi nhận traffic từ máy khách (client / 클라이언트).

Reverse proxy như Nginx, HAProxy, Envoy hoặc cloud bộ cân bằng tải (load balancer / 로드 밸런서) thường nhận yêu cầu (request / 요청) trước backend.

Máy khách (client / 클라이언트) nhìn thấy proxy như endpoint chính, còn proxy biết backend thật.

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Vì sao cần reverse proxy?** tiếp nhận điểm tựa từ **Proxy là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reverse proxy không phải “chỉ forward packet”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao cần reverse proxy?

Một Java ứng dụng (application / 애플리케이션) có thể tự terminate TLS và serve HTTP trực tiếp. Nhưng reverse proxy cho phép tách nhiều trách nhiệm:

- TLS termination;
- routing theo hostname/đường dẫn (path / 경로);
- tải (load / 로드) balancing;
- liên kết (connection / 연결) management;
- compression;
- tỷ lệ (rate / 비율) limiting;
- truy cập (access / 접근) logging;
- health checks;
- static tệp (file / 파일) serving;
- yêu cầu (request / 요청)/phản hồi (response / 응답) header normalization.

Việc tách này giúp ứng dụng (application / 애플리케이션) tập trung lô-gic nghiệp vụ (business logic / 비즈니스 로직), nhưng kiến trúc (architecture / 아키텍처) trở thành multi-hop.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Reverse proxy không phải “chỉ forward packet”** tiếp nhận điểm tựa từ **Vì sao cần reverse proxy?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tầng (layer / 계층) 4 và tầng (layer / 계층) 7 tải (load / 로드) balancing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reverse proxy không phải “chỉ forward packet”

Ở tầng (layer / 계층) 7, proxy có thể terminate TCP/TLS, parse HTTP rồi tạo một liên kết (connection / 연결) khác tới backend.

Ví dụ:

```text
client TCP connection
    ↓
Nginx
    ↓
backend TCP connection
```

Hai liên kết (connection / 연결) này độc lập về hết thời gian chờ (timeout / 타임아웃), keep-alive và socket trạng thái (state / 상태).

Do đó máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) 30 giây không nhất thiết bằng backend hết thời gian chờ (timeout / 타임아웃) 30 giây.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Tầng (layer / 계층) 4 và tầng (layer / 계층) 7 tải (load / 로드) balancing** tiếp nhận điểm tựa từ **Reverse proxy không phải “chỉ forward packet”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tải (load / 로드) balancing giải quyết vấn đề gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tầng (layer / 계층) 4 và tầng (layer / 계층) 7 tải (load / 로드) balancing

**tầng (layer / 계층) 4 bộ cân bằng tải (load balancer / 로드 밸런서)** thường cân bằng theo TCP/UDP liên kết (connection / 연결) mà không cần hiểu HTTP ngữ nghĩa (semantics / 의미론) sâu.

**tầng (layer / 계층) 7 bộ cân bằng tải (load balancer / 로드 밸런서)** hiểu HTTP hostname, đường dẫn (path / 경로), headers và có thể tuyến (route / 경로):

```text
/api/users  → user-service
/api/orders → order-service
```

Tầng (layer / 계층) 7 cho flexibility cao hơn nhưng cần nhiều processing và giao thức (protocol / 프로토콜) awareness hơn.

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Tải (load / 로드) balancing giải quyết vấn đề gì?** tiếp nhận điểm tựa từ **Tầng (layer / 계층) 4 và tầng (layer / 계층) 7 tải (load / 로드) balancing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Round robin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드) balancing giải quyết vấn đề gì?

Một backend instance có sức chứa (capacity / 용량) hữu hạn. Nếu toàn bộ traffic vào một tiến trình (process / 프로세스), nó có thể trở thành single điểm (point / 지점) of thất bại (failure / 실패) và bottleneck.

Bộ cân bằng tải (load balancer / 로드 밸런서) phân phối yêu cầu (request / 요청)/connections tới nhiều upstreams:

```text
             ┌─ app-1
client → LB ─┼─ app-2
             └─ app-3
```

Nhưng “chia đều” không phải lúc nào cũng tối ưu. yêu cầu (request / 요청) chi phí (cost / 비용) có thể khác nhau, liên kết (connection / 연결) có thể sống lâu và instance sức chứa (capacity / 용량) có thể không đồng nhất.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Round robin** tiếp nhận điểm tựa từ **Tải (load / 로드) balancing giải quyết vấn đề gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Least connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Round robin

Thuật toán đơn giản là lần lượt chọn backend:

```text
request 1 → A
request 2 → B
request 3 → C
request 4 → A
```

Round robin hoạt động tốt khi yêu cầu (request / 요청) chi phí (cost / 비용) tương đối tương đồng và backend có sức chứa (capacity / 용량) gần nhau.

Nhưng nếu một yêu cầu (request / 요청) chạy 30 giây còn yêu cầu (request / 요청) khác 10 ms, số yêu cầu (request / 요청) không phản ánh hiện tại (current / 현재) tải (load / 로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Least connections** tiếp nhận điểm tựa từ **Round robin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weighted balancing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Least connections

**Least connections** chọn backend đang có ít active connections hơn.

Cách này có thể phù hợp với long-lived connections hơn round robin, nhưng liên kết (connection / 연결) count vẫn không nói đầy đủ CPU/bộ nhớ (memory / 메모리)/nghiệp vụ (business / 비즈니스) chi phí (cost / 비용).

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Weighted balancing** tiếp nhận điểm tựa từ **Least connections** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Consistent hashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weighted balancing

Nếu máy chủ (server / 서버) A mạnh gấp đôi máy chủ (server / 서버) B, có thể dùng weight:

```text
A weight 2
B weight 1
```

A nhận tỷ lệ traffic cao hơn.

Weight là mô hình (model / 모델) sức chứa (capacity / 용량) gần đúng, không phải guarantee hiệu năng (performance / 성능).

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Consistent hashing** tiếp nhận điểm tựa từ **Weighted balancing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Session affinity và vấn đề stateful ứng dụng (application / 애플리케이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consistent hashing

Một số hệ thống muốn cùng key/máy khách (client / 클라이언트) thường đi tới cùng backend để tăng bộ nhớ đệm (cache / 캐시) locality hoặc session affinity.

Consistent hashing giảm số keys bị remap khi backend thay đổi so với modulo hashing đơn giản.

Nhưng sticky routing tạo sự đánh đổi (trade-off / 트레이드오프): phân phối (distribution / 분포) có thể kém đều và thất bại (failure / 실패) khôi phục (recovery / 복구) phức tạp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Session affinity và vấn đề stateful ứng dụng (application / 애플리케이션)** tiếp nhận điểm tựa từ **Consistent hashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Health check** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Session affinity và vấn đề stateful ứng dụng (application / 애플리케이션)

Nếu người dùng (user / 사용자) session chỉ tồn tại trong bộ nhớ (memory / 메모리) của một ứng dụng (application / 애플리케이션) instance:

```text
request 1 → app-A → session exists
request 2 → app-B → session missing
```

Bộ cân bằng tải (load balancer / 로드 밸런서) có thể dùng sticky session, nhưng solution tốt hơn trong nhiều hệ thống là đưa session/trạng thái (state / 상태) ra dùng chung (shared / 공유) store hoặc dùng stateless đơn vị từ (token / 토큰) khi phù hợp.

Tải (load / 로드) balancing hoạt động tốt nhất khi ứng dụng (application / 애플리케이션) instance có thể thay thế lẫn nhau.

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Health check** tiếp nhận điểm tựa từ **Session affinity và vấn đề stateful ứng dụng (application / 애플리케이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Passive health và active health** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Health check

Bộ cân bằng tải (load balancer / 로드 밸런서) không nên gửi traffic tới instance chết.

Health check có thể kiểm tra:

```http
GET /health
```

Nhưng thiết kế health endpoint cần cẩn thận.

Nếu health check phụ thuộc cơ sở dữ liệu (database / 데이터베이스)/downstream và phụ thuộc (dependency / 의존성) tạm chậm, mọi app instances có thể đồng loạt bị đánh dấu unhealthy, làm outage nặng hơn.

Cần phân biệt:

- **liveness**: tiến trình (process / 프로세스) còn sống hay không;
- **readiness**: instance có sẵn sàng nhận traffic hay không;
- **phụ thuộc (dependency / 의존성) health**: downstream có khỏe không.

Không nên gộp tất cả vào một boolean đơn giản.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Passive health và active health** tiếp nhận điểm tựa từ **Health check** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **502 Bad Gateway** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Passive health và active health

**Active health check** gửi yêu cầu (request / 요청) định kỳ tới backend.

**Passive health check** quan sát thất bại (failure / 실패) từ traffic thật, ví dụ consecutive liên kết (connection / 연결) errors.

Kết hợp hai cách có thể phản ánh trạng thái (state / 상태) tốt hơn, nhưng cần tránh flap khi backend chỉ có transient độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **502 Bad Gateway** tiếp nhận điểm tựa từ **Passive health và active health** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **504 Gateway hết thời gian chờ (timeout / 타임아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 502 Bad Gateway

HTTP `502 Bad Gateway` thường nghĩa proxy nhận phản hồi (response / 응답) không hợp lệ hoặc không thể thiết lập/duy trì communication đúng với upstream.

Các nguyên nhân có thể gồm:

- backend tiến trình (process / 프로세스) không listen;
- liên kết (connection / 연결) refused;
- backend reset liên kết (connection / 연결);
- TLS upstream mismatch;
- giao thức (protocol / 프로토콜) mismatch;
- malformed phản hồi (response / 응답).

`502` chỉ là symptom ở proxy tầng (layer / 계층). Cần xem proxy log và backend trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **504 Gateway hết thời gian chờ (timeout / 타임아웃)** tiếp nhận điểm tựa từ **502 Bad Gateway** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hết thời gian chờ (timeout / 타임아웃) phải được thiết kế theo chuỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 504 Gateway hết thời gian chờ (timeout / 타임아웃)

`504 Gateway Timeout` thường nghĩa proxy đã chờ upstream vượt hết thời gian chờ (timeout / 타임아웃).

Backend có thể:

- xử lý quá lâu;
- chờ cơ sở dữ liệu (database / 데이터베이스) khóa (lock / 잠금);
- chờ downstream API;
- luồng thực thi (thread / 스레드) pool exhausted;
- mạng (network / 네트워크) packet mất mát (loss / 손실);
- hết thời gian chờ (timeout / 타임아웃) chuỗi (chain / 사슬) cấu hình không hợp lý.

Không nên chỉ tăng proxy hết thời gian chờ (timeout / 타임아웃). Nếu nguyên nhân gốc (root cause / 근본 원인) là phụ thuộc (dependency / 의존성) độ trễ (latency / 지연 시간), tăng hết thời gian chờ (timeout / 타임아웃) có thể làm connections tích tụ lâu hơn và tạo tài nguyên (resource / 자원) exhaustion.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **504 Gateway hết thời gian chờ (timeout / 타임아웃)** xác định đầu vào; **Hết thời gian chờ (timeout / 타임아웃) phải được thiết kế theo chuỗi** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Thử lại (retry / 재시도) có thể khuếch đại sự cố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hết thời gian chờ (timeout / 타임아웃) phải được thiết kế theo chuỗi

Giả sử:

```text
client timeout     = 30s
load balancer      = 60s
Nginx proxy timeout= 90s
Java DB timeout    = 120s
```

Máy khách (client / 클라이언트) đã bỏ cuộc ở giây 30 nhưng backend có thể tiếp tục giữ luồng thực thi (thread / 스레드)/DB liên kết (connection / 연결) thêm nhiều chục giây.

Một thiết kế (design / 설계) thường hợp lý hơn là hết thời gian chờ (timeout / 타임아웃) phía trong nhỏ hơn hoặc aligned với yêu cầu (request / 요청) ngân sách (budget / 예산) tổng, tùy kiến trúc (architecture / 아키텍처).

Mô hình tư duy (mental model / 사고 모델):

```text
request deadline
   ↓
proxy budget
   ↓
application budget
   ↓
dependency budget
```

Hết thời gian chờ (timeout / 타임아웃) nên phản ánh end-to-end độ trễ (latency / 지연 시간) mục tiêu (objective / 목표), không phải các con số độc lập.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Hết thời gian chờ (timeout / 타임아웃) phải được thiết kế theo chuỗi** xác định đầu vào; **Thử lại (retry / 재시도) có thể khuếch đại sự cố** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Idempotency và thử lại (retry / 재시도) POST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thử lại (retry / 재시도) có thể khuếch đại sự cố

Nếu proxy thử lại (retry / 재시도) yêu cầu (request / 요청) thất bại (fail / 실패) sang backend khác, độ tin cậy (reliability / 신뢰성) có thể tăng với transient thất bại (failure / 실패).

Nhưng khi upstream chậm, thử lại (retry / 재시도) tạo thêm traffic:

```text
100 requests
× 3 retries
= tối đa 300 attempts
```

Đây là **thử lại (retry / 재시도) amplification**.

Nếu nhiều layers đều thử lại (retry / 재시도), amplification có thể nhân lên mạnh.

Thử lại (retry / 재시도) cần:

- giới hạn attempts;
- hết thời gian chờ (timeout / 타임아웃) nhỏ;
- exponential backoff khi phù hợp;
- jitter;
- chỉ thử lại (retry / 재시도) idempotent operations nếu không có deduplication ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Idempotency và thử lại (retry / 재시도) POST** tiếp nhận điểm tựa từ **Thử lại (retry / 재시도) có thể khuếch đại sự cố** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Keep-alive và liên kết (connection / 연결) pooling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Idempotency và thử lại (retry / 재시도) POST

Thử lại (retry / 재시도) `GET` thường ít nguy hiểm hơn thử lại (retry / 재시도) một thao tác (operation / 연산) tạo payment/thứ tự (order / 순서).

Nếu máy khách (client / 클라이언트) gửi:

```http
POST /payments
```

rồi hết thời gian chờ (timeout / 타임아웃) nhưng máy chủ (server / 서버) đã xử lý thành công, thử lại (retry / 재시도) có thể tạo duplicate payment.

Giải pháp có thể dùng **idempotency key**:

```http
Idempotency-Key: abc123
```

Backend lưu kết quả và nhận diện thử lại (retry / 재시도) cùng thao tác (operation / 연산).

Đây là liên kết (connection / 연결) giữa networking độ tin cậy (reliability / 신뢰성) và nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성).

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, sau nội dung của **Idempotency và thử lại (retry / 재시도) POST**, **Keep-alive và liên kết (connection / 연결) pooling** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Hàng đợi (queue / 큐) tại proxy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Keep-alive và liên kết (connection / 연결) pooling

Proxy thường giữ persistent liên kết (connection / 연결) tới backend để giảm TCP/TLS handshake overhead.

Nếu keep-alive pool quá nhỏ, liên kết (connection / 연결) churn tăng. Nếu quá lớn, backend có thể bị giữ quá nhiều sockets.

Các metrics cần nhìn:

- active connections;
- idle keep-alive connections;
- liên kết (connection / 연결) creation tỷ lệ (rate / 비율);
- TIME_WAIT;
- upstream độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Hàng đợi (queue / 큐) tại proxy** tiếp nhận điểm tựa từ **Keep-alive và liên kết (connection / 연결) pooling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) tại proxy

Khi upstream sức chứa (capacity / 용량) đầy, proxy có thể có pending requests/connections.

Hàng đợi (queue / 큐) không tự động xấu. Một hàng đợi (queue / 큐) nhỏ hấp thụ burst. Nhưng khi arrival tỷ lệ (rate / 비율) > dịch vụ (service / 서비스) tỷ lệ (rate / 비율) kéo dài, hàng đợi (queue / 큐) tăng liên tục và độ trễ (latency / 지연 시간) tăng.

Đây là ứng dụng (application / 애플리케이션) của queueing lý thuyết (theory / 이론).

Xem thêm: [Capacity planning](../09_production/capacity_planning_server_sizing.md).

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Backpressure** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) tại proxy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tỷ lệ (rate / 비율) limiting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backpressure

**Backpressure** là cơ chế để hệ thống phía sau báo rằng nó không thể nhận công việc (work / 작업) vô hạn.

Nếu bộ cân bằng tải (load balancer / 로드 밸런서)/proxy cứ tiếp tục nhận mọi yêu cầu (request / 요청) và xếp hàng đợi (queue / 큐) vô hạn, bộ nhớ (memory / 메모리)/độ trễ (latency / 지연 시간) cuối cùng collapse.

Better hành vi (behavior / 동작) có thể là reject sớm bằng `429`/`503` khi sức chứa (capacity / 용량) đã đạt threshold phù hợp.

Thất bại (fail / 실패) fast đôi khi bảo vệ hệ thống (system / 시스템) tốt hơn “cố xử lý tất cả”.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Backpressure** đã nêu tiêu chí phân biệt, còn **Tỷ lệ (rate / 비율) limiting** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **TLS termination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tỷ lệ (rate / 비율) limiting

Proxy có thể giới hạn yêu cầu (request / 요청) tỷ lệ (rate / 비율) theo IP, người dùng (user / 사용자)/đơn vị từ (token / 토큰) hoặc endpoint.

Tỷ lệ (rate / 비율) limiting giúp chống abuse và bảo vệ backend, nhưng threshold phải dựa traffic mô hình (model / 모델).

Một endpoint login và một endpoint tệp (file / 파일) download có chi phí (cost / 비용) khác nhau; chỉ dùng requests/second không phản ánh mọi tài nguyên (resource / 자원) chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Tỷ lệ (rate / 비율) limiting** đã nêu tiêu chí phân biệt, còn **TLS termination** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **X-Forwarded- headers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLS termination

Reverse proxy thường terminate TLS:

```text
client HTTPS
   ↓
proxy terminates TLS
   ↓
HTTP hoặc HTTPS tới backend
```

Nếu proxy→backend dùng HTTP, traffic nội bộ không được TLS bảo vệ. Có phù hợp hay không phụ thuộc trust ranh giới (boundary / 경계).

Một số môi trường (environment / 환경) dùng TLS ở cả hai đoạn hoặc mTLS.

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **X-Forwarded- headers** tiếp nhận điểm tựa từ **TLS termination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Máy khách (client / 클라이언트) IP và nhiều proxy hops** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## X-Forwarded-* headers

Khi proxy tạo liên kết (connection / 연결) mới tới backend, backend nhìn nguồn (source / 소스) IP của proxy thay vì máy khách (client / 클라이언트) thật.

Proxy có thể thêm:

```text
X-Forwarded-For
X-Forwarded-Proto
X-Forwarded-Host
```

hoặc tiêu chuẩn (standard / 표준) `Forwarded` header.

Ứng dụng (application / 애플리케이션) chỉ nên tin các headers này từ proxy đáng tin cậy. Nếu máy khách (client / 클라이언트) internet có thể tự set header và app tin vô điều kiện, kiểm tra (audit / 감사)/bảo mật (security / 보안) lô-gic (logic / 논리) có thể bị giả mạo.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Máy khách (client / 클라이언트) IP và nhiều proxy hops** tiếp nhận điểm tựa từ **X-Forwarded- headers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reverse proxy và WebSocket** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Máy khách (client / 클라이언트) IP và nhiều proxy hops

`X-Forwarded-For` có thể là danh sách (list / 목록):

```text
client, proxy1, proxy2
```

Muốn lấy máy khách (client / 클라이언트) IP đúng cần biết số trusted proxy hops và khung phần mềm (framework / 프레임워크) cấu hình (configuration / 구성).

Không nên đơn giản chọn giá trị đầu/cuối mà không hiểu topology.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Reverse proxy và WebSocket** tiếp nhận điểm tựa từ **Máy khách (client / 클라이언트) IP và nhiều proxy hops** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HTTP/2 multiplexing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reverse proxy và WebSocket

WebSocket bắt đầu bằng HTTP upgrade rồi chuyển sang long-lived bidirectional liên kết (connection / 연결).

Proxy phải hỗ trợ upgrade headers và hết thời gian chờ (timeout / 타임아웃) phù hợp.

Long-lived connections cũng làm tải (load / 로드) balancing theo yêu cầu (request / 요청) count kém meaningful hơn.

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **HTTP/2 multiplexing** tiếp nhận điểm tựa từ **Reverse proxy và WebSocket** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nginx upstream example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HTTP/2 multiplexing

Một HTTP/2 liên kết (connection / 연결) có thể mang nhiều concurrent streams.

Do đó liên kết (connection / 연결) count máy khách (client / 클라이언트)→proxy không trực tiếp tương đương yêu cầu (request / 요청) tính đồng thời (concurrency / 동시성).

Nếu proxy dùng HTTP/1.1 tới backend, một HTTP/2 máy khách (client / 클라이언트) liên kết (connection / 연결) có thể fan out thành nhiều upstream connections/requests.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **HTTP/2 multiplexing** cho ta quy tắc; **Nginx upstream example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Proxy buffering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nginx upstream example

Ví dụ đơn giản:

```nginx
upstream app_backend {
    server 10.0.0.11:8080;
    server 10.0.0.12:8080;
}

server {
    listen 443 ssl;

    location / {
        proxy_pass http://app_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Đây chỉ là skeleton. môi trường vận hành (production / 운영 환경) cần hết thời gian chờ (timeout / 타임아웃), TLS, health hành vi (behavior / 동작), logging, buffering và bảo mật (security / 보안) settings phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Nginx upstream example** cho ta quy tắc; **Proxy buffering** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Bộ cân bằng tải (load balancer / 로드 밸런서) ở cloud** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proxy buffering

Một reverse proxy có thể buffer yêu cầu (request / 요청)/phản hồi (response / 응답) thay vì stream ngay.

Buffering có lợi vì backend có thể trả nhanh rồi proxy gửi chậm cho máy khách (client / 클라이언트). Nhưng với streaming/SSE/large upload, buffering có thể gây độ trễ (latency / 지연 시간) hoặc bộ nhớ (memory / 메모리)/disk use không mong muốn.

Hành vi (behavior / 동작) cần align tải công việc (workload / 워크로드).

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Bộ cân bằng tải (load balancer / 로드 밸런서) ở cloud** tiếp nhận điểm tựa từ **Proxy buffering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kubernetes dịch vụ (service / 서비스) và Ingress** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ cân bằng tải (load balancer / 로드 밸런서) ở cloud

AWS ALB/NLB, GCP bộ cân bằng tải (load balancer / 로드 밸런서), Azure bộ cân bằng tải (load balancer / 로드 밸런서) hay Kubernetes Ingress đều cung cấp lớp trừu tượng (abstraction / 추상화) khác nhau nhưng các nguyên lý vẫn giống:

- listener;
- mục tiêu (target / 대상)/backend pool;
- health check;
- routing;
- liên kết (connection / 연결) hết thời gian chờ (timeout / 타임아웃);
- TLS;
- khả năng quan sát (observability / 관측 가능성).

Không nên học từng vendor như hệ thống hoàn toàn riêng. Hãy map chúng về mạng (network / 네트워크)/proxy mô hình tư duy (mental model / 사고 모델).

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Kubernetes dịch vụ (service / 서비스) và Ingress** tiếp nhận điểm tựa từ **Bộ cân bằng tải (load balancer / 로드 밸런서) ở cloud** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gỡ lỗi (debug / 디버그) 502/504 theo tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kubernetes dịch vụ (service / 서비스) và Ingress

Kubernetes `Service` cung cấp stable virtual endpoint cho pods. Ingress/Gateway xử lý tầng (layer / 계층) 7 routing tùy hiện thực (implementation / 구현).

Đường đi của yêu cầu (request path / 요청 경로) có thể là:

```text
external LB
 → ingress controller
 → Kubernetes Service
 → Pod
```

Mỗi tầng (layer / 계층) có logs/metrics/trạng thái (state / 상태) riêng. `curl podIP` thành công không chứng minh bên ngoài (external / 외부) ingress đường dẫn (path / 경로) đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Gỡ lỗi (debug / 디버그) 502/504 theo tầng (layer / 계층)** tiếp nhận điểm tựa từ **Kubernetes dịch vụ (service / 서비스) và Ingress** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truy cập (access / 접근) log như structured bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gỡ lỗi (debug / 디버그) 502/504 theo tầng (layer / 계층)

Bắt đầu từ proxy host:

```bash
curl -v http://backend-ip:8080/health
```

Nếu thất bại (fail / 실패), vấn đề nằm backend/mạng (network / 네트워크) giữa proxy và backend.

Kiểm tra listener backend:

```bash
ss -lntp | grep ':8080'
```

Xem proxy log:

```bash
journalctl -u nginx
```

hoặc truy cập (access / 접근)/lỗi (error / 오류) logs.

Sau đó correlate timestamp với backend logs.

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Gỡ lỗi (debug / 디버그) 502/504 theo tầng (layer / 계층)** nêu điều cần giải thích; **Truy cập (access / 접근) log như structured bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Yêu cầu (request / 요청) ID propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy cập (access / 접근) log như structured bằng chứng (evidence / 증거)

Một proxy truy cập (access / 접근) log tốt nên có:

- yêu cầu (request / 요청) timestamp;
- phương thức (method / 메서드)/đường dẫn (path / 경로);
- status;
- total yêu cầu (request / 요청) thời gian (time / 시간);
- upstream address;
- upstream connect thời gian (time / 시간);
- upstream phản hồi (response / 응답) thời gian (time / 시간);
- yêu cầu (request / 요청) ID.

Ví dụ nếu total thời gian (time / 시간) 10s nhưng upstream thời gian (time / 시간) 9.9s, proxy overhead ít khả năng là bottleneck chính.

Nếu connect thời gian (time / 시간) cao, liên kết (connection / 연결) establishment/mạng (network / 네트워크)/upstream accept đường dẫn (path / 경로) đáng điều tra.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Truy cập (access / 접근) log như structured bằng chứng (evidence / 증거)** nêu điều cần giải thích; **Yêu cầu (request / 요청) ID propagation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Yêu cầu (request / 요청) ID propagation

Proxy có thể tạo hoặc forward yêu cầu (request / 요청) ID:

```text
X-Request-ID: 7f8a...
```

Backend log cùng ID giúp nối:

```text
proxy access log
 ↔ application log
 ↔ downstream log
```

Đây là nền tảng phân tán (distributed / 분산) tracing đơn giản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Yêu cầu (request / 요청) ID propagation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Reverse proxy/bộ cân bằng tải (load balancer / 로드 밸런서) là **một ứng dụng (application / 애플리케이션) mạng có trạng thái (state / 상태) và tài nguyên (resource / 자원) riêng**, không phải “đường ống trong suốt”.

Khi yêu cầu (request / 요청) đi qua proxy, hãy theo dõi:

```text
DNS
 ↓
client→proxy connection
 ↓
TLS / HTTP parsing
 ↓
routing / load-balancing decision
 ↓
proxy→backend connection
 ↓
backend processing
 ↓
response path
```

Mỗi mũi tên có hết thời gian chờ (timeout / 타임아웃), hàng đợi (queue / 큐) và dạng thất bại (failure mode / 실패 모드) riêng.

> **Chuyển mạch:** Trong **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Xem thêm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“502 nghĩa backend mã (code / 코드) trả 502.”** Thường 502 được proxy tạo vì upstream communication thất bại (failure / 실패).

**“504 chỉ cần tăng hết thời gian chờ (timeout / 타임아웃).”** Nếu backend thực sự saturated, tăng hết thời gian chờ (timeout / 타임아웃) có thể làm tình hình tệ hơn.

**“Round robin luôn chia tải đều.”** yêu cầu (request / 요청) chi phí (cost / 비용) và liên kết (connection / 연결) thời gian tồn tại (lifetime / 수명) khác nhau.

**“Health endpoint càng kiểm tra nhiều phụ thuộc (dependency / 의존성) càng tốt.”** Health check quá coupled có thể tạo cascading thất bại (failure / 실패).

**“thử lại (retry / 재시도) luôn tăng độ tin cậy (reliability / 신뢰성).”** thử lại (retry / 재시도) không kiểm soát có thể tạo amplification và duplicate side effects.

**“Proxy không ảnh hưởng hiệu năng (performance / 성능).”** Proxy có liên kết (connection / 연결) pools, buffers, TLS chi phí (cost / 비용), queues và tài nguyên (resource / 자원) limits riêng.

> **Chuyển mạch:** Ở chặng này của **Reverse Proxy, tải (load / 로드) Balancing và đường đi của HTTP yêu cầu (request / 요청)**, **Xem thêm** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Xem thêm

Các liên kết này là bước bàn giao sang cơ chế liên quan. Hãy mở chúng theo câu hỏi còn bỏ ngỏ, không coi danh sách link là phần kết luận tự thân.

- [DNS resolution internals](./dns_resolution_internals.md)
- [IP routing, NAT và conntrack](./ip_routing_nat_conntrack.md)
- [TCP, HTTP và TLS](./tcp_http_tls.md)
- [Java backend incident playbook](../09_production/java_backend_incident_playbook.md)
- [Capacity planning và server sizing](../09_production/capacity_planning_server_sizing.md)

> **Bàn giao:** Sau **Xem thêm**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
