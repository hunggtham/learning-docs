# 21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vẽ topology trước khi gỡ lỗi (debug / 디버그)** biến nhận định thành tiêu chí kiểm tra hoặc cách gỡ lỗi; sau đó sang **2. Frontend ranh giới (boundary / 경계) không nên mirror microservice topology** để soi ranh giới và điểm dễ nhầm. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

WebSquare page cuối cùng luôn sống trong một topology lớn hơn chính nó. Một Submission có thể đi thẳng vào monolith, qua reverse proxy, API Gateway, BFF, nhiều microservice, hoặc một adapter legacy. Một screen có thể đồng thời nhận HTTP phản hồi (response / 응답), polling cập nhật (update / 업데이트), máy chủ (server / 서버) push và bản địa (native / 네이티브) callback.

Nếu nhà phát triển (developer / 개발자) chỉ nhìn `sbmSearch.action`, nhiều dạng thất bại (failure mode / 실패 모드) môi trường vận hành (production / 운영 환경) sẽ bị quy thành “API lỗi” hoặc “WebSquare lỗi” dù nguyên nhân nằm ở topology, quyền sở hữu (ownership / 소유권) hoặc thứ tự (ordering / 순서).

> mô hình tư duy (mental model / 사고 모델) chính: **frontend không gọi “backend”; frontend gửi intent qua một tích hợp (integration / 통합) topology có nhiều hop, đặc tả hợp đồng (contract / 계약) và miền lỗi (failure domain / 장애 도메인)**.

## 1. Vẽ topology trước khi gỡ lỗi (debug / 디버그)

Một luồng (flow / 흐름) đơn giản:

```text
WebSquare Page
→ Submission
→ Web Server / Reverse Proxy
→ Application Server
→ Service
→ Database
```

Một luồng (flow / 흐름) enterprise:

```text
WebSquare Shell
→ Submission
→ API Gateway
→ BFF
├─ Customer Service
├─ Order Service
├─ Code Service
└─ Legacy Adapter
   → Mainframe / External API
```

Độ trễ (latency / 지연 시간), hết thời gian chờ (timeout / 타임아웃), auth, thử lại (retry / 재시도) và lỗi (error / 오류) ánh xạ (mapping / 매핑) có thể phát sinh ở từng hop.

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **1. Vẽ topology trước khi gỡ lỗi (debug / 디버그)** đã nêu tiêu chí phân biệt, còn **2. Frontend ranh giới (boundary / 경계) không nên mirror microservice topology** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. WebSquare SP5 và MSA hỗ trợ (support / 지원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Frontend ranh giới (boundary / 경계) không nên mirror microservice topology

Anti-pattern là mỗi page biết tên và URL của mọi microservice.

Khi dịch vụ (service / 서비스) topology thay đổi, hàng trăm XML/Submission phải sửa. Frontend cũng phải tự aggregate dữ liệu (data / 데이터) và xử lý partial thất bại (failure / 실패) phức tạp.

BFF hoặc stable API ranh giới (boundary / 경계) có thể giảm coupling:

```text
Screen intent
→ stable frontend contract
→ backend orchestration
→ internal services
```

Không phải mọi hệ thống cần BFF, nhưng **frontend đặc tả hợp đồng (contract / 계약) nên phản ánh người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스) năng lực (capability / 역량) hơn triển khai (deployment / 배포) topology**.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **2. Frontend ranh giới (boundary / 경계) không nên mirror microservice topology** đã nêu tiêu chí phân biệt, còn **3. WebSquare SP5 và MSA hỗ trợ (support / 지원)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. msaCommon không biến frontend thành dịch vụ (service / 서비스) registry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. WebSquare SP5 và MSA hỗ trợ (support / 지원)

Các SP5 bản dựng (build / 빌드) hiện đại có cấu hình (configuration / 구성)/API liên quan MSA như `msaCommon`, `msaServerName`, `msaName` cho một số tài nguyên (resource / 자원)/thành phần (component / 컴포넌트)/API. Đây là tính năng (feature / 기능) build-dependent và phải đối chiếu bản phát hành (release / 릴리스) ghi chú (note / 노트)/API tham chiếu (reference / 참조) đúng engine.

Mô hình tư duy (mental model / 사고 모델) cần giữ:

```text
logical resource/service name
→ configuration resolves target server/path
→ WebSquare loads/submits resource
```

Không hard-code giả định (assumption / 가정) rằng mọi bản dựng (build / 빌드) SP5 đều có cùng thuộc tính (property / 속성) hoặc default.

> **Chuyển mạch:** WebSquare SP5 có thể hỗ trợ MSA nhưng msaCommon không phải frontend service registry; resource topology và business API topology tiếp theo cần được vẽ riêng.

## 4. `msaCommon` không biến frontend thành dịch vụ (service / 서비스) registry

MSA tài nguyên (resource / 자원) cấu hình (configuration / 구성) giúp tải (load / 로드) dùng chung (common / 공통) mô-đun (module / 모듈)/thành phần (component / 컴포넌트) từ máy chủ (server / 서버) logical tương ứng. Nó không có nghĩa nghiệp vụ (business / 비즈니스) page nên tự discovery dịch vụ (service / 서비스) instance, health-check pod hoặc implement bộ cân bằng tải (load balancer / 로드 밸런서).

Khám phá dịch vụ (service discovery / 서비스 디스커버리), routing, circuit breaker và instance health thường thuộc hạ tầng (infrastructure / 인프라)/gateway/dịch vụ (service / 서비스) tầng (layer / 계층).

Frontend chỉ nên biết đặc tả hợp đồng (contract / 계약) cần thiết.

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **4. msaCommon không biến frontend thành dịch vụ (service / 서비스) registry** nêu điều cần giải thích; **5. tài nguyên (resource / 자원) topology và nghiệp vụ (business / 비즈니스) API topology khác nhau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Contract-first tích hợp (integration / 통합)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. tài nguyên (resource / 자원) topology và nghiệp vụ (business / 비즈니스) API topology khác nhau

Có hai đồ thị (graph / 그래프) dễ bị trộn:

```text
Resource graph
XML / JS / UDC / language pack / W-Pack artifact

Business request graph
Submission / API / transaction / service
```

Một page có thể tải (load / 로드) JS từ MSA tài nguyên (resource / 자원) máy chủ (server / 서버) nhưng gửi nghiệp vụ (business / 비즈니스) Submission sang gateway khác.

Khi lỗi “screen không mở”, kiểm tra tài nguyên (resource / 자원) đồ thị (graph / 그래프). Khi screen mở nhưng tìm kiếm (search / 검색) thất bại (fail / 실패), kiểm tra yêu cầu (request / 요청) đồ thị (graph / 그래프).

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **5. tài nguyên (resource / 자원) topology và nghiệp vụ (business / 비즈니스) API topology khác nhau** nêu điều cần giải thích; **6. Contract-first tích hợp (integration / 통합)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. API Gateway không sửa đặc tả hợp đồng (contract / 계약) xấu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Contract-first tích hợp (integration / 통합)

Một Submission đặc tả hợp đồng (contract / 계약) tốt mô tả:

```text
intent
request schema
response schema
error taxonomy
idempotency
version/concurrency field
pagination/order semantics
security requirement
observability identity
```

Không chỉ mô tả URL.

URL là routing detail; đặc tả hợp đồng (contract / 계약) mới là ngữ nghĩa (semantic / 의미적) phụ thuộc (dependency / 의존성).

> **Chuyển mạch:** Contract-first đặt boundary trước; API Gateway chỉ route/policy, không chữa contract xấu. BFF tiếp theo chỉ có giá trị khi cần composition theo client.

## 7. API Gateway không sửa đặc tả hợp đồng (contract / 계약) xấu

Gateway có thể routing, TLS termination, tỷ lệ (rate / 비율) limiting, authentication tích hợp (integration / 통합) hoặc chính sách (policy / 정책). Nó không tự giải quyết:

```text
field semantics mơ hồ
null vs missing
partial success không định nghĩa
retry unsafe
version conflict không biểu diễn
business error trả HTTP 200 nhưng không có code chuẩn
```

Frontend vẫn cần đặc tả hợp đồng (contract / 계약) rõ như chapter 15.

> **Chuyển mạch:** BFF composition giảm coupling ở client; đổi lại fan-out tạo partial failure, nên client phải có policy fallback và timeout riêng.

## 8. BFF khi nào có giá trị

BFF hữu ích khi một screen cần aggregate nhiều nguồn hoặc cần shape riêng cho UI.

Ví dụ Employee Detail cần:

```text
employee
organization
permissions
code labels
recent activity
```

Nếu page gửi năm yêu cầu (request / 요청) và tự coordinate, nó sở hữu nhiều miền lỗi (failure domain / 장애 도메인). BFF có thể aggregate và trả view-oriented đặc tả hợp đồng (contract / 계약).

Sự đánh đổi (trade-off / 트레이드오프) là BFF thêm một dịch vụ (service / 서비스) cần vận hành và phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **9. máy khách (client / 클라이언트) fan-out và partial thất bại (failure / 실패)** tiếp nhận điểm tựa từ **8. BFF khi nào có giá trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. ngân sách thời gian chờ (timeout budget / 타임아웃 예산) theo hop** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. máy khách (client / 클라이언트) fan-out và partial thất bại (failure / 실패)

Nếu vẫn cần nhiều Submission song song:

```text
A = employee
B = code list
C = permission
```

Không được coi “Promise.all-like success” là lựa chọn duy nhất.

Hỏi:

```text
A fail thì screen có usable không?
B fail có thể show raw code không?
C fail có được default allow không? — thường là không.
request nào critical, request nào optional?
```

Thiết kế degraded chế độ (mode / 모드) phải theo nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **10. ngân sách thời gian chờ (timeout budget / 타임아웃 예산) theo hop** tiếp nhận điểm tựa từ **9. máy khách (client / 클라이언트) fan-out và partial thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. ngân sách thời gian chờ (timeout budget / 타임아웃 예산) theo hop

Nếu frontend hết thời gian chờ (timeout / 타임아웃) 5 giây nhưng gateway hết thời gian chờ (timeout / 타임아웃) 30 giây và downstream 60 giây, yêu cầu (request / 요청) có thể tiếp tục chạy sau khi UI đã báo thất bại (fail / 실패).

Mô hình tư duy (mental model / 사고 모델):

```text
T_frontend
T_gateway
T_BFF
T_service
T_external
```

Hết thời gian chờ (timeout / 타임아웃) phải được thiết kế theo ngân sách (budget / 예산), không đặt độc lập.

Mutating thao tác (operation / 연산) càng cần idempotency/reconciliation vì máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) không chứng minh máy chủ (server / 서버) chưa lần ghi nhận (commit / 커밋).

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, sau nội dung của **10. ngân sách thời gian chờ (timeout budget / 타임아웃 예산) theo hop**, **11. thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **12. Circuit breaker thuộc đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)

Một yêu cầu (request / 요청) có thể bị thử lại (retry / 재시도) ở:

```text
browser/page
common Submission layer
gateway
service client
message broker consumer
```

Nếu mọi tầng (layer / 계층) đều thử lại (retry / 재시도) 3 lần, một thất bại (failure / 실패) có thể khuếch đại thành nhiều yêu cầu (request / 요청).

Thử lại (retry / 재시도) chính sách (policy / 정책) phải có đơn vị sở hữu (owner / 오너) rõ và phân biệt read vs ghi (write / 쓰기).

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **12. Circuit breaker thuộc đâu?** tiếp nhận điểm tựa từ **11. thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Bulkhead và screen isolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Circuit breaker thuộc đâu?

Circuit breaker thường có giá trị ở dịch vụ (service / 서비스)/gateway tầng (layer / 계층) nơi có visibility về downstream health. Frontend có thể có UX backoff hoặc stop spam yêu cầu (request / 요청), nhưng không nên tự giả lập hạ tầng (infrastructure / 인프라) circuit breaker bằng toàn cục (global / 전역) boolean tùy tiện.

Frontend concern là:

```text
fail fast UX
backoff polling
prevent duplicate action
show degraded state
resume/reload safely
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **13. Bulkhead và screen isolation** tiếp nhận điểm tựa từ **12. Circuit breaker thuộc đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Real-time không đồng nghĩa WebSocket** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Bulkhead và screen isolation

Một dịch vụ (service / 서비스) chậm không nên freeze toàn shell.

Nếu mã (code / 코드) dịch vụ (service / 서비스) thất bại (fail / 실패), có thể chỉ một selector bị degraded thay vì khối (block / 블록) toàn app. Nếu auth dịch vụ (service / 서비스) thất bại (fail / 실패), protected command có thể phải khối (block / 블록) rộng hơn.

Đây là **failure-domain thiết kế (design / 설계)**.

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **14. Real-time không đồng nghĩa WebSocket** tiếp nhận điểm tựa từ **13. Bulkhead và screen isolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. WebSquare ranh giới (boundary / 경계) cho real-time** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Real-time không đồng nghĩa WebSocket

Có nhiều vận chuyển (transport / 전송) mẫu (pattern / 패턴):

```text
manual refresh
polling
long polling
Server-Sent Events (SSE)
WebSocket
native push → app event
```

Chọn theo yêu cầu (requirement / 요구사항), không theo độ “hiện đại (modern / 현대적)”.

Nếu cập nhật (update / 업데이트) mỗi 5 phút, polling đơn giản có thể tốt hơn WebSocket.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **14. Real-time không đồng nghĩa WebSocket** đã nêu tiêu chí phân biệt, còn **15. WebSquare ranh giới (boundary / 경계) cho real-time** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. Polling vòng đời (lifecycle / 생명주기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. WebSquare ranh giới (boundary / 경계) cho real-time

WebSquare-specific concern không phải tự invent socket API. Concern là **sự kiện (event / 이벤트) từ vận chuyển (transport / 전송) cập nhật phạm vi (scope / 범위)/DataCollection/Grid như thế nào và vòng đời (lifecycle / 생명주기) ai sở hữu subscription**.

Một adapter tốt:

```text
transport adapter
→ normalized domain event
→ screen/application event bus
→ owner checks identity/version
→ update/requery DataCollection
→ Grid renders from model
```

Không để raw socket callback đi thẳng sửa DOM.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **15. WebSquare ranh giới (boundary / 경계) cho real-time** đã nêu tiêu chí phân biệt, còn **16. Polling vòng đời (lifecycle / 생명주기)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Overlapping polling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Polling vòng đời (lifecycle / 생명주기)

Polling thường bị coi nhẹ nhưng gây leak phổ biến.

```text
page open
→ start timer
→ tab hidden
→ page close
```

Phải quyết định:

```text
hidden có poll tiếp không?
interval bao lâu?
request trước chưa xong thì có gửi request mới không?
close cleanup ở đâu?
resume có immediate refresh không?
```

Chapter 10 về thời gian tồn tại (lifetime / 수명) áp dụng trực tiếp.

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **16. Polling vòng đời (lifecycle / 생명주기)** xác định đầu vào; **17. Overlapping polling** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **18. SSE mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Overlapping polling

Anti-pattern:

```javascript
setInterval(function () {
    search();
}, 5000);
```

Nếu tìm kiếm (search / 검색) mất 8 giây, yêu cầu (request / 요청) chồng nhau.

Mẫu (pattern / 패턴) tốt hơn về mô hình tư duy (mental model / 사고 모델):

```text
request complete
→ wait/backoff
→ next request
```

hoặc guard `inFlight` nếu ngữ nghĩa (semantics / 의미론) cho phép.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **18. SSE mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **17. Overlapping polling** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **19. WebSocket mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. SSE mô hình tư duy (mental model / 사고 모델)

SSE phù hợp máy chủ (server / 서버) → máy khách (client / 클라이언트) stream một chiều qua HTTP. Frontend cần xử lý:

```text
connection state
last event identity
reconnect
duplicate event
out-of-order event
screen ownership
logout cleanup
```

Không assume reconnect đồng nghĩa không mất sự kiện (event / 이벤트); đặc tả hợp đồng (contract / 계약) phải định nghĩa replay/resume nếu cần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **19. WebSocket mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **18. SSE mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **20. liên kết (connection / 연결) quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. WebSocket mô hình tư duy (mental model / 사고 모델)

WebSocket là long-lived bidirectional channel. Nó tạo thêm vòng đời (lifecycle / 생명주기):

```text
DISCONNECTED
→ CONNECTING
→ CONNECTED
→ DEGRADED
→ RECONNECTING
→ CLOSED
```

Một socket liên kết (connection / 연결) không nên mặc định thuộc từng page nếu app có nhiều screen dùng chung. Có thể app shell sở hữu liên kết (connection / 연결) và screen subscribe lĩnh vực (domain / 도메인) sự kiện (event / 이벤트).

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **20. liên kết (connection / 연결) quyền sở hữu (ownership / 소유권)** gom các mảnh từ **19. WebSocket mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **21. sự kiện (event / 이벤트) định danh (identity / 식별자) quan trọng hơn arrival thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. liên kết (connection / 연결) quyền sở hữu (ownership / 소유권)

Hai lựa chọn:

**Page-owned liên kết (connection / 연결)** phù hợp năng lực (capability / 역량) hoàn toàn cục bộ (local / 로컬) và thời gian tồn tại (lifetime / 수명) ngắn.

**Shell-owned liên kết (connection / 연결)** phù hợp notification hoặc dùng chung (shared / 공유) sự kiện (event / 이벤트) stream toàn app.

Sai quyền sở hữu (ownership / 소유권) dẫn đến duplicate liên kết (connection / 연결), leak hoặc sự kiện (event / 이벤트) gửi vào page đã disposed.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **21. sự kiện (event / 이벤트) định danh (identity / 식별자) quan trọng hơn arrival thứ tự (order / 순서)** tiếp nhận điểm tựa từ **20. liên kết (connection / 연결) quyền sở hữu (ownership / 소유권)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Requery vs patch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. sự kiện (event / 이벤트) định danh (identity / 식별자) quan trọng hơn arrival thứ tự (order / 순서)

Real-time sự kiện (event / 이벤트) có thể duplicate hoặc out of thứ tự (order / 순서).

Một sự kiện (event / 이벤트) nên có định danh (identity / 식별자)/phiên bản (version / 버전) phù hợp:

```text
eventId
entityId
entityVersion / sequence
eventType
occurredAt
correlationId
```

Frontend không nên “sự kiện (event / 이벤트) đến sau thì mới hơn” nếu vận chuyển (transport / 전송) không đảm bảo thứ tự (ordering / 순서) toàn cục.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **22. Requery vs patch** tiếp nhận điểm tựa từ **21. sự kiện (event / 이벤트) định danh (identity / 식별자) quan trọng hơn arrival thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Grid sort/filter và real-time patch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Requery vs patch

Khi nhận `ORDER_CHANGED`, có hai chiến lược.

**Patch**: cập nhật (update / 업데이트) DataList row trực tiếp. Nhanh nhưng cần sự kiện (event / 이벤트) payload/phiên bản (version / 버전) đủ mạnh.

**Requery**: dùng sự kiện (event / 이벤트) như vô hiệu hóa (invalidation / 무효화) tín hiệu (signal / 신호) rồi Submission lấy chuẩn gốc (canonical / 정본) trạng thái (state / 상태). Chậm hơn nhưng đơn giản và an toàn hơn trong nhiều hệ thống.

Hybrid chiến lược (strategy / 전략) thường hiệu quả: patch optimistic cho UX, requery khi bất biến (invariant / 불변식) phức tạp.

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **23. Grid sort/filter và real-time patch** tiếp nhận điểm tựa từ **22. Requery vs patch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Grid sort/filter và real-time patch

Nếu row đang bị filter hoặc sort, patch một trường dữ liệu (field / 필드) có thể làm row đổi vị trí hoặc biến mất khỏi view.

Do đó nghiệp vụ (business / 비즈니스) key phải được dùng để locate mô hình (model / 모델) row, rồi để Grid/view tầng (layer / 계층) reconcile. Không giữ view chỉ mục (index / 인덱스) từ trước sự kiện (event / 이벤트).

Chapter 13 giải thích định danh (identity / 식별자) này sâu hơn.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **24. Backpressure** tiếp nhận điểm tựa từ **23. Grid sort/filter và real-time patch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. sự kiện (event / 이벤트) storm và formatter chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Backpressure

Nếu máy chủ (server / 서버) gửi 1.000 sự kiện (event / 이벤트)/giây nhưng Grid kết xuất (render / 렌더링) mỗi sự kiện (event / 이벤트), UI freeze.

Cần chiến lược (strategy / 전략):

```text
buffer
coalesce theo entity
batch apply
throttle render
invalidate + requery
```

Backpressure là mismatch giữa producer tỷ lệ (rate / 비율) và bên tiêu thụ (consumer / 소비자) sức chứa (capacity / 용량).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **25. sự kiện (event / 이벤트) storm và formatter chi phí (cost / 비용)** tiếp nhận điểm tựa từ **24. Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Offline và reconnect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. sự kiện (event / 이벤트) storm và formatter chi phí (cost / 비용)

Ngay cả DataList cập nhật (update / 업데이트) rẻ, Grid formatter/summary/expression có thể chạy lại rất nhiều. Real-time kiến trúc (architecture / 아키텍처) phải đo kết xuất (render / 렌더링) chi phí (cost / 비용), không chỉ mạng (network / 네트워크) thông lượng (throughput / 처리량).

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **26. Offline và reconnect** tiếp nhận điểm tựa từ **25. sự kiện (event / 이벤트) storm và formatter chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. lược đồ (schema / 스키마) evolution trong sự kiện (event / 이벤트) stream** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Offline và reconnect

Khi trình duyệt (browser / 브라우저)/mobile offline:

```text
transport disconnect
pending mutation uncertain
local state stale
```

Reconnect không nên tự động replay mọi command. truy vấn (query / 쿼리) có thể refresh; mutation cần idempotency/reconciliation.

Hybrid app cần nối thêm bản địa (native / 네이티브) mạng (network / 네트워크) trạng thái (state / 상태) nhưng không được tin bản địa (native / 네이티브) “online” là API reachable.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **27. lược đồ (schema / 스키마) evolution trong sự kiện (event / 이벤트) stream** tiếp nhận điểm tựa từ **26. Offline và reconnect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Frontend phiên bản (version / 버전) skew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. lược đồ (schema / 스키마) evolution trong sự kiện (event / 이벤트) stream

Long-lived máy khách (client / 클라이언트) có thể đang chạy bản dựng (build / 빌드) cũ trong khi máy chủ (server / 서버) deploy sự kiện (event / 이벤트) lược đồ (schema / 스키마) mới.

Sự kiện (event / 이벤트) đặc tả hợp đồng (contract / 계약) cần backward tính tương thích (compatibility / 호환성) hoặc tường minh (explicit / 명시적) versioning.

Không rename trường dữ liệu (field / 필드) và assume tất cả trình duyệt (browser / 브라우저) đã reload.

Đây là lý do trình duyệt (browser / 브라우저) máy khách (client / 클라이언트) khác máy chủ (server / 서버) tiến trình (process / 프로세스): máy khách (client / 클라이언트) phiên bản (version / 버전) rollout kéo dài.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **28. Frontend phiên bản (version / 버전) skew** tiếp nhận điểm tựa từ **27. lược đồ (schema / 스키마) evolution trong sự kiện (event / 이벤트) stream** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. MSA dùng chung (common / 공통) tài nguyên (resource / 자원) phiên bản (version / 버전) skew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Frontend phiên bản (version / 버전) skew

Trong môi trường vận hành (production / 운영 환경) cùng lúc có thể tồn tại:

```text
browser A → W-Pack v41
browser B → W-Pack v42
server → API v43 compatible mode
```

Đặc tả hợp đồng (contract / 계약) di chuyển (migration / 마이그레이션) phải chịu được overlap cửa sổ (window / 윈도우).

Chapter 22 sẽ đi sâu sản phẩm tạo ra (artifact / 산출물)/bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자).

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **28. Frontend phiên bản (version / 버전) skew** nêu điều cần giải thích; **29. MSA dùng chung (common / 공통) tài nguyên (resource / 자원) phiên bản (version / 버전) skew** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **30. Cross-origin và credential ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. MSA dùng chung (common / 공통) tài nguyên (resource / 자원) phiên bản (version / 버전) skew

Nếu shell tải (load / 로드) dùng chung (common / 공통) thành phần (component / 컴포넌트) từ logical MSA tài nguyên (resource / 자원) máy chủ (server / 서버), phiên bản (version / 버전) của dùng chung (common / 공통) mô-đun (module / 모듈) cũng trở thành phụ thuộc (dependency / 의존성).

Cần biết:

```text
shell artifact version
common component version
engine build
config routing
```

“main đã deploy” không đủ chứng minh thời gian chạy (runtime / 런타임) composition đồng nhất.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **29. MSA dùng chung (common / 공통) tài nguyên (resource / 자원) phiên bản (version / 버전) skew** đã nêu tiêu chí phân biệt, còn **30. Cross-origin và credential ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **31. tệp (file / 파일)/upload trong MSA topology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Cross-origin và credential ranh giới (boundary / 경계)

Nếu tài nguyên (resource / 자원)/API nằm khác origin, trình duyệt (browser / 브라우저) CORS, cookie chính sách (policy / 정책) và bảo mật (security / 보안) header trở thành một phần topology.

Không workaround CORS bằng disable trình duyệt (browser / 브라우저) bảo mật (security / 보안) hoặc JSONP-like hack. Origin chính sách (policy / 정책) phải được giải quyết ở kiến trúc (architecture / 아키텍처)/máy chủ (server / 서버)/gateway.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **30. Cross-origin và credential ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **31. tệp (file / 파일)/upload trong MSA topology** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **32. Auth trong multi-service topology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. tệp (file / 파일)/upload trong MSA topology

Upload có thể đi vào tệp (file / 파일) dịch vụ (service / 서비스) khác nghiệp vụ (business / 비즈니스) API. Khi đó attachment siêu dữ liệu (metadata / 메타데이터) và nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션) càng cần correlation định danh (identity / 식별자).

```text
uploadSessionId
fileId
businessEntityId
requestId
```

Chapter 17 đã giải thích consistency giữa nhị phân (binary / 이진) và DB trạng thái (state / 상태).

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **32. Auth trong multi-service topology** tiếp nhận điểm tựa từ **31. tệp (file / 파일)/upload trong MSA topology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. khả năng quan sát (observability / 관측 가능성) xuyên topology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Auth trong multi-service topology

Frontend không nên gửi role tự khai báo để mỗi dịch vụ (service / 서비스) tin theo. Credential/bảo mật (security / 보안) ngữ cảnh (context / 맥락) phải được gateway/dịch vụ (service / 서비스) validate theo kiến trúc (architecture / 아키텍처).

Frontend năng lực (capability / 역량) vẫn chỉ phục vụ UX.

Chapter 20 là prerequisite cho phần này.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **33. khả năng quan sát (observability / 관측 가능성) xuyên topology** tiếp nhận điểm tựa từ **32. Auth trong multi-service topology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. thất bại (failure / 실패) taxonomy theo hop** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. khả năng quan sát (observability / 관측 가능성) xuyên topology

Một yêu cầu (request / 요청) cần correlation xuyên:

```text
screenInstanceKey
→ requestId
→ gateway trace
→ BFF trace
→ service trace
→ database/external call
```

Frontend không cần biết mọi nội bộ (internal / 내부) span, nhưng hỗ trợ (support / 지원) cần đủ định danh (identity / 식별자) để nối trình duyệt (browser / 브라우저) symptom với máy chủ (server / 서버) bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **34. thất bại (failure / 실패) taxonomy theo hop** tiếp nhận điểm tựa từ **33. khả năng quan sát (observability / 관측 가능성) xuyên topology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Testing topology bằng fault injection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. thất bại (failure / 실패) taxonomy theo hop

Nên phân biệt:

```text
CLIENT_VALIDATION
CLIENT_LIFECYCLE
DNS_NETWORK
GATEWAY_REJECT
AUTH_FAILURE
UPSTREAM_TIMEOUT
SERVICE_UNAVAILABLE
BUSINESS_REJECT
CONCURRENCY_CONFLICT
SCHEMA_MISMATCH
REALTIME_DISCONNECTED
STALE_EVENT
```

Taxonomy giúp sự cố (incident / 인시던트) triage nhanh hơn generic `SYSTEM_ERROR`.

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **35. Testing topology bằng fault injection** tiếp nhận điểm tựa từ **34. thất bại (failure / 실패) taxonomy theo hop** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. trường hợp (case / 사례) study — mã (code / 코드) dịch vụ (service / 서비스) chậm làm màn hình không mở** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Testing topology bằng fault injection

Không chỉ mock success.

Kiểm thử (test / 테스트):

```text
gateway timeout
BFF trả partial data
service A nhanh, B chậm
response cũ về sau mới
polling overlap
socket disconnect/reconnect
duplicate event
out-of-order event
1.000 event burst
schema field mới/thiếu
browser client cũ với server mới
```

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **35. Testing topology bằng fault injection** cho ta quy tắc; **36. trường hợp (case / 사례) study — mã (code / 코드) dịch vụ (service / 서비스) chậm làm màn hình không mở** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **37. trường hợp (case / 사례) study — Polling tạo 12 yêu cầu (request / 요청) cùng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. trường hợp (case / 사례) study — mã (code / 코드) dịch vụ (service / 서비스) chậm làm màn hình không mở

Employee dữ liệu (data / 데이터) đã về nhưng page chờ mã (code / 코드) danh sách (list / 목록) trước kết xuất (render / 렌더링) toàn bộ.

Câu hỏi kiến trúc (architecture / 아키텍처):

```text
code list có critical không?
có cache hợp lý không?
có thể render raw code rồi hydrate label không?
BFF nên aggregate không?
```

Fix tốt không nhất thiết là tăng hết thời gian chờ (timeout / 타임아웃).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **36. trường hợp (case / 사례) study — mã (code / 코드) dịch vụ (service / 서비스) chậm làm màn hình không mở** cho ta quy tắc; **37. trường hợp (case / 사례) study — Polling tạo 12 yêu cầu (request / 요청) cùng lúc** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **38. trường hợp (case / 사례) study — WebSocket sự kiện (event / 이벤트) cập nhật (update / 업데이트) sai row** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. trường hợp (case / 사례) study — Polling tạo 12 yêu cầu (request / 요청) cùng lúc

Tab background bị throttled rồi resume; timer fire mẫu (pattern / 패턴) và yêu cầu (request / 요청) overlap tạo burst.

Fix bằng lifecycle-aware scheduler, in-flight guard/backoff và immediate reconciliation sau resume.

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **37. trường hợp (case / 사례) study — Polling tạo 12 yêu cầu (request / 요청) cùng lúc** cho ta quy tắc; **38. trường hợp (case / 사례) study — WebSocket sự kiện (event / 이벤트) cập nhật (update / 업데이트) sai row** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **39. trường hợp (case / 사례) study — Deploy dịch vụ (service / 서비스) mới làm trình duyệt (browser / 브라우저) cũ crash** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. trường hợp (case / 사례) study — WebSocket sự kiện (event / 이벤트) cập nhật (update / 업데이트) sai row

Callback giữ `selectedRowIndex` từ lúc subscribe. người dùng (user / 사용자) sort Grid, sự kiện (event / 이벤트) về sau và patch chỉ mục (index / 인덱스) cũ.

Nguyên nhân gốc (root cause / 근본 원인) là định danh (identity / 식별자) ranh giới (boundary / 경계). sự kiện (event / 이벤트) phải mang `orderId`; locate DataList bằng nghiệp vụ (business / 비즈니스) key.

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **38. trường hợp (case / 사례) study — WebSocket sự kiện (event / 이벤트) cập nhật (update / 업데이트) sai row** cho ta quy tắc; **39. trường hợp (case / 사례) study — Deploy dịch vụ (service / 서비스) mới làm trình duyệt (browser / 브라우저) cũ crash** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **40. Master checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. trường hợp (case / 사례) study — Deploy dịch vụ (service / 서비스) mới làm trình duyệt (browser / 브라우저) cũ crash

Máy chủ (server / 서버) đổi phản hồi (response / 응답) trường dữ liệu (field / 필드) từ `employeeId` thành `id`, nhưng nhiều trình duyệt (browser / 브라우저) vẫn chạy W-Pack cũ do bộ nhớ đệm (cache / 캐시).

Nguyên nhân gốc (root cause / 근본 원인) là lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) không hỗ trợ phiên bản (version / 버전) overlap. Fix bằng backward-compatible đặc tả hợp đồng (contract / 계약) hoặc coordinated versioning; không chỉ “clear bộ nhớ đệm (cache / 캐시) người dùng (user / 사용자)”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **39. trường hợp (case / 사례) study — Deploy dịch vụ (service / 서비스) mới làm trình duyệt (browser / 브라우저) cũ crash** cho ta quy tắc; **40. Master checklist** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **41. liên kết (connection / 연결) map** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Master checklist

```text
Topology thực tế có những hop nào?
Frontend phụ thuộc contract hay deployment URL?
Request nào critical/optional?
Timeout budget được phân bổ ra sao?
Retry owner là layer nào?
Mutation có idempotency không?
Resource MSA và business API MSA có bị trộn không?
Real-time connection owner là page hay shell?
Event có identity/version không?
Duplicate/out-of-order xử lý thế nào?
Backpressure có thể freeze Grid không?
Client cũ/server mới coexist thế nào?
Correlation ID đi xuyên topology tới đâu?
```

> **Chuyển mạch:** Trong **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, sau nội dung của **40. Master checklist**, **41. liên kết (connection / 연결) map** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **42. Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. liên kết (connection / 연결) map

Submission: [03 — DataCollection & Submission](03_data_collection_submission.md).

Vòng đời (lifecycle / 생명주기): [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

Triển khai (deployment / 배포): [12 — Build, Configuration & Deployment](12_build_config_deployment.md).

Grid định danh (identity / 식별자): [13 — GridView Editing, Identity & View Internals](13_gridview_editing_identity_internals.md).

Backend đặc tả hợp đồng (contract / 계약): [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md).

Tệp (file / 파일) chuỗi xử lý (pipeline / 파이프라인): [17 — File, Excel, Upload & Download](17_file_excel_upload_download_pipeline.md).

Authentication/session: [20 — Authentication, Session, SSO & Security Lifecycle](20_authentication_session_sso_security_lifecycle.md).

> **Chuyển mạch:** Ở chặng này của **21 — tích hợp (integration / 통합) Topology, MSA, Real-Time & Resilience**, **42. Kết luận** gom các mảnh từ **41. liên kết (connection / 연결) map** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 42. Kết luận

Tích hợp (integration / 통합) Master không nhìn một Submission như “AJAX lời gọi (call / 호출)”. Họ nhìn nó như một edge trong đồ thị (graph / 그래프):

```text
User intent
→ Screen owner
→ Submission contract
→ Routing topology
→ Service transaction
→ Response/event
→ Identity/version reconciliation
→ DataCollection
→ Render
→ Evidence
```

Khi có real-time, đồ thị (graph / 그래프) không còn request-response tuyến tính. Vì vậy **quyền sở hữu (ownership / 소유권), định danh (identity / 식별자), thứ tự (ordering / 순서), backpressure, phiên bản (version / 버전) skew và vòng đời (lifecycle / 생명주기)** trở thành những bất biến (invariant / 불변식) quan trọng hơn việc nhớ vận chuyển (transport / 전송) API.

> **Bàn giao:** Sau **42. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
