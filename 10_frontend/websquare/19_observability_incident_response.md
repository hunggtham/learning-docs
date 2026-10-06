# 19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Debugging và khả năng quan sát (observability / 관측 가능성) không giống nhau** biến nhận định thành tiêu chí kiểm tra hoặc cách gỡ lỗi; sau đó sang **2. WebSquare ứng dụng (application / 애플리케이션) có nhiều lớp bằng chứng (evidence / 증거)** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này nối observability với debugging, evidence và incident response, để biến dấu hiệu rời rạc thành giả thuyết có thể kiểm tra.

## 1. Debugging và khả năng quan sát (observability / 관측 가능성) không giống nhau

Debugging (gỡ lỗi / 디버깅) là quá trình điều tra một vấn đề cụ thể. khả năng quan sát (observability / 관측 가능성) là khả năng suy ra trạng thái bên trong của hệ thống từ bằng chứng (evidence / 증거) mà hệ thống tạo ra.

Một nhà phát triển (developer / 개발자) có thể gỡ lỗi (debug / 디버그) tốt trên máy cục bộ (local / 로컬) nhưng môi trường vận hành (production / 운영 환경) vẫn khó hỗ trợ (support / 지원) nếu không có correlation ID, bản dựng (build / 빌드) định danh (identity / 식별자), timing và structured lỗi (error / 오류).

Mô hình tư duy (mental model / 사고 모델):

```text
incident
  ↓
evidence
  ↓
hypothesis
  ↓
experiment / comparison
  ↓
root cause
  ↓
fix + regression guard
```

Không bắt đầu bằng sửa mã (code / 코드). Bắt đầu bằng bằng chứng (evidence / 증거).

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **1. Debugging và khả năng quan sát (observability / 관측 가능성) không giống nhau** đặt vấn đề; **2. WebSquare ứng dụng (application / 애플리케이션) có nhiều lớp bằng chứng (evidence / 증거)** đối chiếu bằng chứng, rồi **3. Correlation ID là xương sống của tracing** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. WebSquare ứng dụng (application / 애플리케이션) có nhiều lớp bằng chứng (evidence / 증거)

Một screen lỗi có thể liên quan:

```text
browser/WebView
WebSquare engine
page scope/scwin
component/GridView
DataCollection
Submission
network
WebSquare server module/config
application backend
DB/external service
build/cache/CDN
native shell nếu hybrid
```

Nếu chỉ nhìn console JavaScript, bạn mới thấy một phần hệ thống.

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **2. WebSquare ứng dụng (application / 애플리케이션) có nhiều lớp bằng chứng (evidence / 증거)** đặt vấn đề; **3. Correlation ID là xương sống của tracing** đối chiếu bằng chứng, rồi **4. Log sự kiện (event / 이벤트), không log câu chuyện mơ hồ** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Correlation ID là xương sống của tracing

Một người dùng (user / 사용자) hành động (action / 동작) như Save nên có định danh (identity / 식별자) xuyên tầng (layer / 계층):

```text
click Save
→ client requestId
→ HTTP header/payload
→ gateway/backend log
→ DB/service call log
→ response
→ client completion log
```

Không cần full phân tán (distributed / 분산) tracing nền tảng (platform / 플랫폼) mới áp dụng được nguyên tắc này. Một yêu cầu (request / 요청) ID nhất quán đã giảm đáng kể thời gian điều tra.

> **Nối mạch:** Correlation ID nối request với trace; event log tiếp theo ghi state transition có cấu trúc, thay vì kể chuyện mơ hồ hoặc đổ toàn bộ DataList vào log.

## 4. Log sự kiện (event / 이벤트), không log câu chuyện mơ hồ

Log kiểu:

```text
save error
```

ít giá trị.

Log tốt hơn có cấu trúc (structure / 구조):

```text
event=USER_SAVE_FAILED
requestId=REQ-123
screen=USER_DETAIL
submission=sbmSave
stage=BUSINESS_RESPONSE
code=OPTIMISTIC_LOCK_CONFLICT
elapsedMs=842
```

Message cho người đọc, trường dữ liệu (field / 필드) cho tìm kiếm (search / 검색)/aggregation.

> **Nối mạch:** Event log cần có cấu trúc; tránh log toàn bộ DataList để bảo vệ PII và giảm noise, rồi chọn `$p.log()`/WebSquare log theo môi trường.

## 5. Không log toàn bộ DataList theo thói quen

DataList có thể chứa PII, account dữ liệu (data / 데이터) hoặc hàng nghìn row. Dump toàn bộ đối tượng (object / 객체) vừa chậm vừa nguy hiểm.

Log summary:

```text
rowCount
changedRowCount
selected business key đã mask
status distribution C/U/D
schema/version
```

Chỉ bật payload detail có kiểm soát trong môi trường phù hợp.

> **Nối mạch:** Log API quyết định sink và mức chi tiết; client debug config tiếp theo phải bật có chủ đích, tránh leak dữ liệu hoặc biến production thành trace mode.

## 6. `$p.log()` và WebSquare log

WebSquare cung cấp logging/gỡ lỗi (debug / 디버그) facility; tài liệu hiệu năng (performance / 성능)/gỡ lỗi (debug / 디버그) mô tả log do `$p.log()` tạo với timestamp, elapsed thời gian (time / 시간) giữa log và elapsed thời gian (time / 시간) từ log đầu tiên.

Điều này hữu ích để đọc startup/kết xuất (render / 렌더링) chuỗi (sequence / 시퀀스):

```text
STEP1 engine load
STEP2 engine complete
STEP3 resources loaded
STEP4 object creation
...
```

Đừng chỉ đọc message; elapsed thời gian (time / 시간) giữa step giúp xác định bottleneck nằm ở engine/tài nguyên (resource / 자원)/đối tượng (object / 객체) creation hay nghiệp vụ (business / 비즈니스) yêu cầu (request / 요청).

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **7. máy khách (client / 클라이언트) gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성)** nối từ **6. $p.log() và WebSquare log** sang **8. gỡ lỗi (debug / 디버그) ngữ cảnh (context / 맥락) menu là bằng chứng (evidence / 증거) công cụ (tool / 도구)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. máy khách (client / 클라이언트) gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성)

Trong các bản dựng (build / 빌드) tương ứng, `client.config.xml` có các setting như `debug`, `console`, `errorConsole`, `remoteConsole`, `debugKey`, `debugMenu`.

`remoteConsole` có thể cho phép `WebSquare.logger.sendRemoteLog` ghi log về WAS theo cấu hình tương ứng.

Nhưng gỡ lỗi (debug / 디버그) setting là operational chính sách (policy / 정책). Không bật mức verbose môi trường vận hành (production / 운영 환경) vô hạn chỉ vì cần điều tra một bug.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **7. máy khách (client / 클라이언트) gỡ lỗi (debug / 디버그) cấu hình (configuration / 구성)** đặt vấn đề; **8. gỡ lỗi (debug / 디버그) ngữ cảnh (context / 맥락) menu là bằng chứng (evidence / 증거) công cụ (tool / 도구)** đối chiếu bằng chứng, rồi **9. Scope-aware debugging** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. gỡ lỗi (debug / 디버그) ngữ cảnh (context / 맥락) menu là bằng chứng (evidence / 증거) công cụ (tool / 도구)

WebSquare hỗ trợ ngữ cảnh (context / 맥락) gỡ lỗi (debug / 디버그) menu trong các setup phù hợp, cho phép xem log và DataCollection hiện tại. Đây là cách tốt để kiểm tra mô hình (model / 모델) trạng thái (state / 상태) mà không sửa nguồn (source / 소스) thêm `alert()`.

Khi dùng production-like môi trường (environment / 환경), đảm bảo gỡ lỗi (debug / 디버그) menu không làm lộ dữ liệu cho người dùng (user / 사용자) không phù hợp.

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **8. gỡ lỗi (debug / 디버그) ngữ cảnh (context / 맥락) menu là bằng chứng (evidence / 증거) công cụ (tool / 도구)** đặt vấn đề; **9. Scope-aware debugging** đối chiếu bằng chứng, rồi **10. Server-side WebSquare log** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. Scope-aware debugging

Trong WFrame/phạm vi (scope / 범위) app, nhìn thấy DOM element chưa đủ để biết đối tượng (object / 객체) thuộc page nào.

Gỡ lỗi (debug / 디버그) utility như:

```javascript
$p.debug.getScope($0)
$p.debug.getFrame($0)
```

ở các bản dựng (build / 빌드) hỗ trợ giúp map DOM đang inspect về WebSquare phạm vi (scope / 범위)/frame.

Workflow:

```text
Inspect broken element
→ identify frame/scope
→ inspect scwin/DataCollection/component trong đúng scope
→ trace Submission/event
```

Điều này tốt hơn thử `$p.top()` cho tới khi tìm thấy đối tượng (object / 객체).

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **10. Server-side WebSquare log** nối từ **9. Scope-aware debugging** sang **11. Engine kiểu (type / 타입) ảnh hưởng khả năng gỡ lỗi (debug / 디버그)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Server-side WebSquare log

`server.config.xml`/engine cấu hình (configuration / 구성) có log mục tiêu (target / 대상), mức (level / 수준), tệp (file / 파일), retention và các option như line/luồng thực thi (thread / 스레드) tùy bản dựng (build / 빌드). Tài liệu chính thức lưu ý line number/luồng thực thi (thread / 스레드) logging có tài nguyên (resource / 자원) chi phí (cost / 비용) và không nên bật tùy tiện ở môi trường vận hành (production / 운영 환경).

Operational principle:

```text
log level càng chi tiết
→ evidence tăng
→ I/O + storage + CPU + noise tăng
```

Chọn mức (level / 수준) theo mục tiêu và thời gian điều tra.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **11. Engine kiểu (type / 타입) ảnh hưởng khả năng gỡ lỗi (debug / 디버그)** nối từ **10. Server-side WebSquare log** sang **12. bản dựng (build / 빌드) định danh (identity / 식별자) là telemetry**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Engine kiểu (type / 타입) ảnh hưởng khả năng gỡ lỗi (debug / 디버그)

WebSquare engine có các `engineType` với mức remapping/gỡ lỗi (debug / 디버그)/log khác nhau ở các dòng engine tương ứng. Một số kiểu (type / 타입) loại bỏ gỡ lỗi (debug / 디버그) info hoặc logger để giảm kích thước (size / 크기).

Vì vậy “môi trường vận hành (production / 운영 환경) không có log giống dev” có thể là hành vi (behavior / 동작) của sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정), không phải logger mã (code / 코드) bị lỗi.

Sự cố (incident / 인시던트) report phải ghi engine bản dựng (build / 빌드)/kiểu (type / 타입).

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **12. bản dựng (build / 빌드) định danh (identity / 식별자) là telemetry** nối từ **11. Engine kiểu (type / 타입) ảnh hưởng khả năng gỡ lỗi (debug / 디버그)** sang **13. bộ nhớ đệm (cache / 캐시) mismatch signature**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. bản dựng (build / 빌드) định danh (identity / 식별자) là telemetry

Một môi trường vận hành (production / 운영 환경) lỗi (error / 오류) chỉ hữu ích khi biết mã (code / 코드) nào đang chạy.

Bản ghi (record / 레코드) tối thiểu:

```text
application release
Git commit/build ID
WebSquare engine build
W-Pack artifact version
client config version
server config version
native app version nếu hybrid
```

Nếu trình duyệt (browser / 브라우저) đang bộ nhớ đệm (cache / 캐시) sản phẩm tạo ra (artifact / 산출물) cũ, Git main mới nhất không phải bằng chứng (evidence / 증거) về mã (code / 코드) người dùng (user / 사용자) đang chạy.

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **13. bộ nhớ đệm (cache / 캐시) mismatch signature** nối từ **12. bản dựng (build / 빌드) định danh (identity / 식별자) là telemetry** sang **14. mạng (network / 네트워크) waterfall là phân tán (distributed / 분산) timeline**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. bộ nhớ đệm (cache / 캐시) mismatch signature

Một thất bại (failure / 실패) sau deploy có mẫu (pattern / 패턴):

```text
HTML/shell mới
+ JS/W-Pack cũ
+ config mới
→ API/component mismatch
```

Hoặc ngược lại.

Khi lỗi chỉ xảy ra ở một số người dùng (user / 사용자) sau deploy, kiểm tra bộ nhớ đệm (cache / 캐시)/tài nguyên (resource / 자원) phiên bản (version / 버전) trước khi suy lô-gic nghiệp vụ (business logic / 비즈니스 로직).

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **14. mạng (network / 네트워크) waterfall là phân tán (distributed / 분산) timeline** nối từ **13. bộ nhớ đệm (cache / 캐시) mismatch signature** sang **15. Submission telemetry**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. mạng (network / 네트워크) waterfall là phân tán (distributed / 분산) timeline

Mạng (network / 네트워크) tab cho biết:

```text
request start
queue/stall
DNS/TLS khi có
request upload
TTFB
response download
status/header/body
```

Nếu click → yêu cầu (request / 요청) start đã mất 2 giây, vấn đề có thể nằm máy khách (client / 클라이언트) JS/kết xuất (render / 렌더링). Nếu yêu cầu (request / 요청) start ngay nhưng TTFB 5 giây, focus backend/mạng (network / 네트워크).

Đừng gọi mọi thứ là “WebSquare chậm”.

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **15. Submission telemetry** nối từ **14. mạng (network / 네트워크) waterfall là phân tán (distributed / 분산) timeline** sang **16. vận chuyển (transport / 전송) success và nghiệp vụ (business / 비즈니스) thất bại (failure / 실패) phải tách chỉ số (metric / 지표)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Submission telemetry

Một wrapper Submission có thể emit vòng đời (lifecycle / 생명주기) sự kiện (event / 이벤트):

```text
SUBMISSION_STARTED
SUBMISSION_SUCCEEDED
SUBMISSION_FAILED
SUBMISSION_CANCELLED
SUBMISSION_STALE_IGNORED
```

Fields nên gồm submission ID, yêu cầu (request / 요청) ID, screen ID, elapsed thời gian (time / 시간), kết quả (result / 결과) lớp (class / 클래스) và payload kích thước (size / 크기) summary khi có thể.

Không cần log payload raw.

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **16. vận chuyển (transport / 전송) success và nghiệp vụ (business / 비즈니스) thất bại (failure / 실패) phải tách chỉ số (metric / 지표)** nối từ **15. Submission telemetry** sang **17. Grid bằng chứng hiệu năng (performance evidence / 성능 증거)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. vận chuyển (transport / 전송) success và nghiệp vụ (business / 비즈니스) thất bại (failure / 실패) phải tách chỉ số (metric / 지표)

Nếu HTTP 200 nhưng nghiệp vụ (business / 비즈니스) phản hồi (response / 응답) trả kiểm tra hợp lệ (validation / 검증)/khóa (lock / 잠금) xung đột (conflict / 충돌), vận chuyển (transport / 전송) dashboard sẽ nhìn “100% success” trong khi người dùng (user / 사용자) thấy lỗi.

Tách chỉ số (metric / 지표):

```text
transport_error_rate
protocol_mapping_error_rate
business_rejection_rate
```

Ba chỉ số (metric / 지표) trả lời ba loại vấn đề khác nhau.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **16. vận chuyển (transport / 전송) success và nghiệp vụ (business / 비즈니스) thất bại (failure / 실패) phải tách chỉ số (metric / 지표)** đặt vấn đề; **17. Grid bằng chứng hiệu năng (performance evidence / 성능 증거)** đối chiếu bằng chứng, rồi **18. người dùng (user / 사용자) timing mark** mở rộng hệ quả hoặc giới hạn liên quan.

## 17. Grid bằng chứng hiệu năng (performance evidence / 성능 증거)

Grid lag cần đo:

```text
row count
column count
visible row count
formatter/expression count
render/update duration
browser memory
long task
```

Nếu Grid chỉ 100 row nhưng formatter gọi heavy hàm (function / 함수) hàng chục nghìn lần do redraw, row count không phải nguyên nhân gốc (root cause / 근본 원인).

Hiệu năng (performance / 성능) chapter và Grid internals đã giải thích cơ chế (mechanism / 메커니즘); khả năng quan sát (observability / 관측 가능성) chapter yêu cầu biến cơ chế (mechanism / 메커니즘) thành measurable bằng chứng (evidence / 증거).

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **17. Grid bằng chứng hiệu năng (performance evidence / 성능 증거)** đặt vấn đề; **18. người dùng (user / 사용자) timing mark** đối chiếu bằng chứng, rồi **19. Long tác vụ (task / 작업) và UI freeze** mở rộng hệ quả hoặc giới hạn liên quan.

## 18. người dùng (user / 사용자) timing mark

Với luồng (flow / 흐름) quan trọng có thể tạo timing mark ở ứng dụng (application / 애플리케이션) tầng (layer / 계층):

```text
SEARCH_CLICK
REQUEST_SENT
RESPONSE_RECEIVED
MODEL_UPDATED
GRID_READY
```

Sau đó tính:

```text
T_network = RESPONSE_RECEIVED - REQUEST_SENT
T_client  = GRID_READY - RESPONSE_RECEIVED
T_total   = GRID_READY - SEARCH_CLICK
```

Không cần khung phần mềm (framework / 프레임워크) APM phức tạp để có decomposition cơ bản.

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **19. Long tác vụ (task / 작업) và UI freeze** nối từ **18. người dùng (user / 사용자) timing mark** sang **20. bộ nhớ (memory / 메모리) sự cố (incident / 인시던트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Long tác vụ (task / 작업) và UI freeze

Trình duyệt (browser / 브라우저) main luồng thực thi (thread / 스레드) freeze có thể đến từ:

```text
large JSON parse
DataList bulk mutation
Grid redraw
formatter loop
synchronous request
large DOM work
custom JavaScript loop
```

Nếu mạng (network / 네트워크) nhanh nhưng click không phản hồi, capture hiệu năng (performance / 성능) profile thay vì tối ưu SQL.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **20. bộ nhớ (memory / 메모리) sự cố (incident / 인시던트)** nối từ **19. Long tác vụ (task / 작업) và UI freeze** sang **21. lỗi (error / 오류) taxonomy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. bộ nhớ (memory / 메모리) sự cố (incident / 인시던트)

SPA/hybrid app chạy lâu có thể leak dần.

Bằng chứng (evidence / 증거) nên so sánh:

```text
open screen 1 lần
close
open/close 20 lần
heap/object/listener count có quay về baseline không?
```

Nếu mỗi vòng tăng cố định, tìm retained tham chiếu (reference / 참조): toàn cục (global / 전역) bộ nhớ đệm (cache / 캐시), timer, document listener, stale WFrame phạm vi (scope / 범위), large DataList closure hoặc bản địa (native / 네이티브) callback registry.

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **21. lỗi (error / 오류) taxonomy** nối từ **20. bộ nhớ (memory / 메모리) sự cố (incident / 인시던트)** sang **22. sự cố (incident / 인시던트) severity không đồng nghĩa exception severity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. lỗi (error / 오류) taxonomy

Đừng dùng một lỗi (error / 오류) mã (code / 코드) `SYSTEM_ERROR` cho mọi thứ.

Một taxonomy hữu ích:

```text
CLIENT_SCRIPT
CLIENT_VALIDATION
SCOPE_LIFECYCLE
NETWORK
TIMEOUT
AUTHENTICATION
AUTHORIZATION
PROTOCOL_MAPPING
BUSINESS_REJECTION
CONCURRENCY_CONFLICT
SERVER_EXCEPTION
DEPENDENCY_FAILURE
FILE_STORAGE
NATIVE_BRIDGE
CONFIG_ARTIFACT_MISMATCH
```

Taxonomy giúp dashboard và runbook map symptom sang đơn vị sở hữu (owner / 오너).

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **22. sự cố (incident / 인시던트) severity không đồng nghĩa exception severity** nối từ **21. lỗi (error / 오류) taxonomy** sang **23. First phản hồi (response / 응답): bảo toàn bằng chứng (evidence / 증거)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. sự cố (incident / 인시던트) severity không đồng nghĩa exception severity

Một console exception trên optional widget có thể low impact. Một silent stale-response bug hiển thị sai account dữ liệu (data / 데이터) có thể high impact dù không throw exception.

Severity dựa trên người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스) impact:

```text
scope
criticality
data integrity
security
recoverability
```

Không dựa chỉ vào dấu vết ngăn xếp (stack trace / 스택 트레이스) dài.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **22. sự cố (incident / 인시던트) severity không đồng nghĩa exception severity** đặt vấn đề; **23. First phản hồi (response / 응답): bảo toàn bằng chứng (evidence / 증거)** đối chiếu bằng chứng, rồi **24. Reproduce theo bất biến (invariant / 불변식), không theo click chuỗi (sequence / 시퀀스) duy nhất** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. First phản hồi (response / 응답): bảo toàn bằng chứng (evidence / 증거)

Khi môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) xảy ra, trước khi restart/clear bộ nhớ đệm (cache / 캐시) mọi thứ hãy thu bằng chứng (evidence / 증거) đủ:

```text
exact time/timezone
user/session/request ID đã mask
screen/URL
steps
expected vs actual
browser/WebView/app version
release/build ID
network request/response metadata
client/server logs
screenshot/video nếu hữu ích
```

Restart có thể làm symptom biến mất nhưng cũng xóa trạng thái (state / 상태) giúp tìm nguyên nhân gốc (root cause / 근본 원인).

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **23. First phản hồi (response / 응답): bảo toàn bằng chứng (evidence / 증거)** đặt vấn đề; **24. Reproduce theo bất biến (invariant / 불변식), không theo click chuỗi (sequence / 시퀀스) duy nhất** đối chiếu bằng chứng, rồi **25. Differential diagnosis** mở rộng hệ quả hoặc giới hạn liên quan.

## 24. Reproduce theo bất biến (invariant / 불변식), không theo click chuỗi (sequence / 시퀀스) duy nhất

Nếu bug xảy ra “sau khi mở tab A rồi B rồi quay lại A”, hãy hỏi bất biến (invariant / 불변식) nào bị phá:

```text
scope identity?
stale reference?
global mutable state?
late Submission response?
DataList shared nhầm?
```

Sau đó tạo minimal reproduction tập trung bất biến (invariant / 불변식) đó.

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **24. Reproduce theo bất biến (invariant / 불변식), không theo click chuỗi (sequence / 시퀀스) duy nhất** đặt đầu vào cho **25. Differential diagnosis**, rồi **26. tìm kiếm nhị phân (binary search / 이진 탐색) cấu hình (configuration / 구성)** mở rộng hệ quả hoặc giới hạn liên quan.

## 25. Differential diagnosis

So sánh môi trường/điều kiện giúp giảm tìm kiếm (search / 검색) không gian (space / 공간):

```text
user A fail / user B pass
Chrome fail / Edge pass
fresh cache pass / warm cache fail
main page pass / WFrame fail
small data pass / large data fail
app 5.4 pass / app 5.2 fail
```

Mỗi contrast là bằng chứng (evidence / 증거) về tầng (layer / 계층) có khả năng liên quan.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **26. tìm kiếm nhị phân (binary search / 이진 탐색) cấu hình (configuration / 구성)** nối từ **25. Differential diagnosis** sang **27. môi trường vận hành (production / 운영 환경) hotfix phải có quay lui (rollback / 롤백) đường dẫn (path / 경로)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. tìm kiếm nhị phân (binary search / 이진 탐색) cấu hình (configuration / 구성)

Khi nghi cấu hình (config / 설정)/bản dựng (build / 빌드), đừng đổi 10 option cùng lúc. Thay một dimension hoặc bisect phiên bản (version / 버전).

```text
engine build N pass
engine build N+4 fail
→ test N+2
→ thu hẹp release introducing behavior
```

Đây là phiên bản (version / 버전) bisection, áp dụng được cho engine, dùng chung (common / 공통) JS và app bản dựng (build / 빌드).

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **26. tìm kiếm nhị phân (binary search / 이진 탐색) cấu hình (configuration / 구성)** đặt đầu vào cho **27. môi trường vận hành (production / 운영 환경) hotfix phải có quay lui (rollback / 롤백) đường dẫn (path / 경로)**, rồi **28. Runbook theo symptom** mở rộng hệ quả hoặc giới hạn liên quan.

## 27. môi trường vận hành (production / 운영 환경) hotfix phải có quay lui (rollback / 롤백) đường dẫn (path / 경로)

Một hotfix không nên chỉ hỏi “fix được chưa?” mà còn:

```text
rollback artifact nào?
cache invalidation thế nào?
config có backward compatible không?
DB migration có reversible không?
native app có thể rollback không?
```

Web tài nguyên (resource / 자원) quay lui (rollback / 롤백) nhanh hơn bản địa (native / 네이티브) store bản phát hành (release / 릴리스), nên hybrid tính tương thích (compatibility / 호환성) càng quan trọng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **27. môi trường vận hành (production / 운영 환경) hotfix phải có quay lui (rollback / 롤백) đường dẫn (path / 경로)** đặt đầu vào cho **28. Runbook theo symptom**, rồi **29. Runbook: Save quay mãi** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. Runbook theo symptom

Runbook tốt bắt đầu từ symptom người dùng (user / 사용자) thấy.

Ví dụ “Grid trống sau tìm kiếm (search / 검색)”:

```text
1. event có chạy?
2. Submission có start?
3. request payload đúng?
4. response có rows?
5. target DataList rowCount?
6. Grid bind đúng DataList?
7. filter/view state?
8. scope đúng instance?
```

Runbook encode kiến thức (knowledge / 지식) để on-call không cần nhớ mọi API.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **29. Runbook: Save quay mãi** nối từ **28. Runbook theo symptom** sang **30. Runbook: chỉ lỗi sau deploy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Runbook: Save quay mãi

```text
button/loading state hiện gì?
request có gửi không?
request pending hay completed?
submitdone/submiterror có chạy?
business response parse được không?
callback throw exception trước cleanup không?
stale request guard có drop callback không?
loading reset ở finally-equivalent path không?
```

Nếu mạng (network / 네트워크) không có yêu cầu (request / 요청), đừng điều tra DB.

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **30. Runbook: chỉ lỗi sau deploy** nối từ **29. Runbook: Save quay mãi** sang **31. Runbook: hybrid callback không về**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Runbook: chỉ lỗi sau deploy

```text
build ID user đang chạy?
W-Pack artifact đúng release?
engine/config version?
cache headers/ETag?
service worker/PWA cache nếu có?
CDN node khác nhau?
API contract deploy order?
```

Triển khai (deployment / 배포) sự cố (incident / 인시던트) thường là sản phẩm tạo ra (artifact / 산출물) đồ thị (graph / 그래프) bài toán (problem / 문제), không chỉ mã nguồn (source code / 소스 코드) bài toán (problem / 문제).

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **31. Runbook: hybrid callback không về** nối từ **30. Runbook: chỉ lỗi sau deploy** sang **32. bảo mật (security / 보안) sự cố (incident / 인시던트) logging**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Runbook: hybrid callback không về

```text
JS requestId được tạo?
bridge dispatch thành công?
native log nhận request?
permission/capability state?
operation complete?
native callback emitted?
WebView/page còn alive?
requestId registry còn entry?
deep link/callback route đúng?
web build ↔ native version compatible?
```

Dấu vết (trace / 추적) theo ranh giới (boundary / 경계) thay vì restart app nhiều lần.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **32. bảo mật (security / 보안) sự cố (incident / 인시던트) logging** nối từ **31. Runbook: hybrid callback không về** sang **33. Metrics nên gắn với người dùng (user / 사용자) journey**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. bảo mật (security / 보안) sự cố (incident / 인시던트) logging

Bảo mật (security / 보안) log cần đủ để kiểm tra (audit / 감사) nhưng không tự tạo dữ liệu (data / 데이터) leak.

Không log:

```text
password
access/refresh token
full resident/identity number
raw biometric/eKYC image
private document body
```

Có thể log masked identifier, băm (hash / 해시)/đơn vị từ (token / 토큰) fingerprint hoặc nội bộ (internal / 내부) yêu cầu (request / 요청) ID tùy chính sách (policy / 정책).

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **33. Metrics nên gắn với người dùng (user / 사용자) journey** nối từ **32. bảo mật (security / 보안) sự cố (incident / 인시던트) logging** sang **34. SLO và lỗi (error / 오류) ngân sách (budget / 예산) ở mức thực dụng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Metrics nên gắn với người dùng (user / 사용자) journey

Khung phần mềm (framework / 프레임워크) chỉ số (metric / 지표) hữu ích, nhưng nghiệp vụ (business / 비즈니스) journey chỉ số (metric / 지표) còn quan trọng hơn:

```text
search success latency
save completion rate
upload completion rate
export job completion time
eKYC completion/drop-off
```

Nếu engine khỏe nhưng 30% người dùng (user / 사용자) không hoàn thành Save, hệ thống vẫn có vấn đề.

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **34. SLO và lỗi (error / 오류) ngân sách (budget / 예산) ở mức thực dụng** nối từ **33. Metrics nên gắn với người dùng (user / 사용자) journey** sang **35. Alert phải actionable**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. SLO và lỗi (error / 오류) ngân sách (budget / 예산) ở mức thực dụng

Không cần bắt đầu bằng hệ thống SRE lớn. Có thể định nghĩa:

```text
99% Search hoàn thành < 2s
99.9% Save không có transport/system failure
99% screen load < 3s
```

Sau đó đo và xem regression theo bản phát hành (release / 릴리스).

SLO buộc nhóm (team / 팀) định nghĩa “nhanh” và “ổn định” bằng số thay vì cảm giác.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **35. Alert phải actionable** nối từ **34. SLO và lỗi (error / 오류) ngân sách (budget / 예산) ở mức thực dụng** sang **36. nguyên nhân gốc (root cause / 근본 원인) vs trigger**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Alert phải actionable

Alert “lỗi (error / 오류) count > 10” có thể noisy. Alert tốt gắn với impact và ngữ cảnh (context / 맥락):

```text
Save system failure rate > 2% trong 5 phút
AND traffic > minimum threshold
```

Alert nên dẫn tới dashboard/runbook có yêu cầu (request / 요청) IDs và bản phát hành (release / 릴리스) phiên bản (version / 버전).

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **36. nguyên nhân gốc (root cause / 근본 원인) vs trigger** nối từ **35. Alert phải actionable** sang **37. Five-whys phải dừng ở actionable hệ thống (system / 시스템) cause**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. nguyên nhân gốc (root cause / 근본 원인) vs trigger

Ví dụ sự cố (incident / 인시던트) xảy ra sau khi người dùng (user / 사용자) double-click Save.

Trigger là double-click.

Nguyên nhân gốc (root cause / 근본 원인) có thể là mutation endpoint không idempotent.

Nếu fix chỉ disable button, automation/thử lại (retry / 재시도) khác vẫn tạo duplicate. nguyên nhân gốc (root cause / 근본 원인) fix phải bảo vệ bất biến (invariant / 불변식) ở authoritative tầng (layer / 계층).

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **37. Five-whys phải dừng ở actionable hệ thống (system / 시스템) cause** nối từ **36. nguyên nhân gốc (root cause / 근본 원인) vs trigger** sang **38. Regression guard sau sự cố (incident / 인시던트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Five-whys phải dừng ở actionable hệ thống (system / 시스템) cause

Đừng kết thúc RCA bằng “nhà phát triển (developer / 개발자) quên check null”. Hỏi tại sao null có thể đi tới đây mà không đặc tả hợp đồng (contract / 계약)/kiểm thử (test / 테스트)/guard.

RCA tốt dẫn tới điều khiển (control / 제어):

```text
schema validation
contract test
lint/static check
central wrapper
monitoring
release guard
```

Không biến RCA thành blame document.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **38. Regression guard sau sự cố (incident / 인시던트)** nối từ **37. Five-whys phải dừng ở actionable hệ thống (system / 시스템) cause** sang **39. bằng chứng (evidence / 증거) bundle cho hỗ trợ (support / 지원)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Regression guard sau sự cố (incident / 인시던트)

Mỗi serious sự cố (incident / 인시던트) nên để lại ít nhất một guard phù hợp:

```text
automated test
metric/alert
runtime validation
runbook
architecture constraint
migration checklist
```

Nếu hệ thống có thể tái phát y hệt mà không ai phát hiện sớm hơn, sự cố (incident / 인시던트) chưa thực sự được “học”.

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **38. Regression guard sau sự cố (incident / 인시던트)** đặt vấn đề; **39. bằng chứng (evidence / 증거) bundle cho hỗ trợ (support / 지원)** đối chiếu bằng chứng, rồi **40. Master sự cố (incident / 인시던트) mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

## 39. bằng chứng (evidence / 증거) bundle cho hỗ trợ (support / 지원)

Một hỗ trợ (support / 지원) bundle có thể gồm:

```text
release/build metadata
engine/config metadata
screen + scope/frame identity
request IDs
selected WebSquare logs
network HAR đã sanitize
console errors
backend log slice
performance trace nếu là latency
```

Bundle chuẩn hóa giúp chuyển issue giữa frontend/backend/nền tảng (platform / 플랫폼) mà không mất ngữ cảnh (context / 맥락).

> **Nối mạch:** Đặt trong câu hỏi lớn của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, các dấu vết trong **39. bằng chứng (evidence / 증거) bundle cho hỗ trợ (support / 지원)** được đọc cùng nhau ở **40. Master sự cố (incident / 인시던트) mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **41. Kết nối** mở rộng hệ quả hoặc giới hạn liên quan.

## 40. Master sự cố (incident / 인시던트) mô hình tư duy (mental model / 사고 모델)

Khi nhận bug môi trường vận hành (production / 운영 환경), đi theo thứ tự:

```text
1. Xác định impact và invariant bị phá.
2. Xác định exact instance/build/environment.
3. Dựng timeline từ user action đến outcome.
4. Tách client, transport, server, storage/native boundary.
5. Thu evidence ở boundary nghi ngờ.
6. So sánh case pass/fail.
7. Thu hẹp hypothesis.
8. Fix authoritative cause.
9. Thêm regression guard.
10. Cập nhật runbook/telemetry nếu evidence ban đầu thiếu.
```

Đây là môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) quan trọng hơn việc nhớ thêm một API.

> **Nối mạch:** Trong **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **41. Kết nối** tổng hợp từ **40. Master sự cố (incident / 인시던트) mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **42. Mastery checkpoint** mở rộng hệ quả hoặc giới hạn liên quan.

## 41. Kết nối

Chapter này tổng hợp bằng chứng (evidence / 증거) từ [06 — Debugging, Performance & Security](06_debugging_performance_security.md), vòng đời (lifecycle / 생명주기) từ [10 — Rendering & Lifetime](10_rendering_lazy_loading_lifetime.md), regression từ [11 — Testing](11_testing_testability_regression.md), sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) từ [12 — Build/Deployment](12_build_config_deployment.md), backend consistency từ [15](15_backend_contract_transaction_concurrency.md), tệp (file / 파일) chuỗi xử lý (pipeline / 파이프라인) từ [17](17_file_excel_upload_download_pipeline.md) và hybrid ranh giới (boundary / 경계) từ [18](18_hybrid_webview_native_bridge.md).

Các mô hình tư duy (mental model / 사고 모델) này được hợp nhất thành quy trình cấp cao (senior / 시니어)/master ở [16 — Master Production Playbook](16_master_production_playbook.md).

> **Nối mạch:** Ở chặng này của **19 — khả năng quan sát (observability / 관측 가능성), Logging & sự cố (incident / 인시던트) phản hồi (response / 응답)**, **42. Mastery checkpoint** nối từ **41. Kết nối** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 42. Mastery checkpoint

Bạn đã master khả năng quan sát (observability / 관측 가능성) khi một bug “thỉnh thoảng xảy ra ở môi trường vận hành (production / 운영 환경)” không còn khiến bạn bắt đầu bằng thêm `alert()` hoặc đoán API. Bạn biết yêu cầu bản dựng (build / 빌드) định danh (identity / 식별자), dựng timeline, phân loại miền lỗi (failure domain / 장애 도메인), dùng correlation ID, đo độ trễ (latency / 지연 시간) theo stage, bảo toàn bằng chứng (evidence / 증거) và biến mỗi sự cố (incident / 인시던트) nghiêm trọng thành kiểm thử (test / 테스트)/chỉ số (metric / 지표)/runbook để lần sau phát hiện sớm hơn.

> **Bàn giao:** Sau **42. Mastery checkpoint**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
