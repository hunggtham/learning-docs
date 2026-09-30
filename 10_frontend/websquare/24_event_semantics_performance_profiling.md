# 24 — sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론), Reentrancy & hiệu năng (performance / 성능) Profiling

> **Mạch đọc:** Đặt **24 — sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론), Reentrancy & hiệu năng (performance / 성능) Profiling** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. sự kiện (event / 이벤트) không phải nghiệp vụ (business / 비즈니스) intent** sang **2. User-driven thay đổi (change / 변경) và programmatic thay đổi (change / 변경) có thể khác ngữ nghĩa (semantics / 의미론)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


WebSquare screen thường trông “event-driven”: người dùng (user / 사용자) click, thành phần (component / 컴포넌트) phát sự kiện (event / 이벤트), handler sửa DataCollection, binding cập nhật UI, Submission chạy, callback lại sửa mô hình (model / 모델). Khi dự án (project / 프로젝트) nhỏ, chuỗi này có vẻ tuyến tính. Khi dự án (project / 프로젝트) lớn, một mutation có thể kích hoạt nhiều sự kiện (event / 이벤트)/binding/kết xuất (render / 렌더링) đường dẫn (path / 경로) và timing trở thành nguyên nhân của bug hoặc hiệu năng (performance / 성능) regression.

Chapter này xây mô hình tư duy (mental model / 사고 모델) để phân biệt **người dùng (user / 사용자) sự kiện (event / 이벤트), khung phần mềm (framework / 프레임워크) sự kiện (event / 이벤트), mô hình (model / 모델) sự kiện (event / 이벤트), kết xuất (render / 렌더링) tác động (effect / 효과) và async continuation**, sau đó đo hiệu năng (performance / 성능) theo bằng chứng (evidence / 증거) thay vì tối ưu bằng cảm giác.

---

## 1. sự kiện (event / 이벤트) không phải nghiệp vụ (business / 비즈니스) intent

Một click có thể đại diện nghiệp vụ (business / 비즈니스) intent “Save”, nhưng click sự kiện (event / 이벤트) chỉ là một đầu vào (input / 입력) tín hiệu (signal / 신호).

```text
DOM/browser interaction
→ WebSquare component event
→ page handler
→ validation
→ model mutation
→ Submission
→ server result
→ model update
→ render
```

Nghiệp vụ (business / 비즈니스) intent nằm ở orchestration tầng (layer / 계층), không nằm trong raw sự kiện (event / 이벤트) đối tượng (object / 객체).

Điều này quan trọng vì cùng một intent có thể đến từ keyboard shortcut, button, menu hoặc bản địa (native / 네이티브) cầu nối (bridge / 브리지). Nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) gắn chặt vào `btnSave_onclick`, reuse/testability giảm.

Mẫu (pattern / 패턴) tốt hơn:

```javascript
scwin.btnSave_onclick = function () {
    scwin.requestSave();
};

scwin.requestSave = function () {
    // validate → snapshot → execute command
};
```

Handler chuyển tín hiệu (signal / 신호) thành command; command mới sở hữu workflow.

---

## 2. User-driven thay đổi (change / 변경) và programmatic thay đổi (change / 변경) có thể khác ngữ nghĩa (semantics / 의미론)

Một số WebSquare thành phần (component / 컴포넌트) phân biệt sự kiện (event / 이벤트) do người dùng (user / 사용자) tương tác (interaction / 상호작용) với giá trị (value / 값) thay đổi bằng script. Official guide của một số thành phần (component / 컴포넌트) mô tả `onviewchange` chỉ phát khi người dùng (user / 사용자) thay đổi view, không nhất thiết khi script set giá trị (value / 값).

Vì vậy không được giả định:

```text
setValue(x)
→ luôn phát cùng event như user chọn x
```

Nếu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) phụ thuộc sự kiện (event / 이벤트) tự phát sau programmatic mutation, mã (code / 코드) dễ break khi thành phần (component / 컴포넌트)/bản dựng (build / 빌드) khác hành vi (behavior / 동작).

Quy tắc (rule / 규칙) tốt hơn:

```text
programmatic command
→ gọi explicit domain/page function cần thiết
```

Sự kiện (event / 이벤트) nên quan sát tương tác (interaction / 상호작용), không nên là hidden control-flow bus.

---

## 3. sự kiện (event / 이벤트) thứ tự (ordering / 순서) là đặc tả hợp đồng (contract / 계약) version-sensitive

Grid editing là ví dụ rõ. SP5 bản phát hành (release / 릴리스) notes có thuộc tính (property / 속성) `viewChangeAfterEdit` liên quan thứ tự `onviewchange` và `onafteredit` ở các bản dựng (build / 빌드) tương ứng.

Bài học không phải nhớ một default. Bài học là:

```text
event A exists
+ event B exists
≠ ordering luôn bất biến
```

Nếu tính đúng đắn (correctness / 정확성) phụ thuộc A luôn trước B, hãy:

1. kiểm tra chính xác (exact / 정확한) bản dựng (build / 빌드)/cấu hình (config / 설정);
2. viết regression kiểm thử (test / 테스트) cho thứ tự (ordering / 순서);
3. tốt hơn nữa, giảm phụ thuộc (dependency / 의존성) vào implicit thứ tự (ordering / 순서) bằng tường minh (explicit / 명시적) chuyển tiếp trạng thái (state transition / 상태 전이).

Upgrade engine có thể thay hành vi (behavior / 동작) dù nguồn (source / 소스) page không đổi.

---

## 4. Reentrancy: handler có thể kích hoạt chính hệ thống sự kiện (event / 이벤트) nó đang xử lý

Ví dụ conceptual:

```text
onchange
→ normalize value
→ setValue(normalized)
→ onchange?
```

Tùy thành phần (component / 컴포넌트)/API, có thể không phát lại, phát sự kiện (event / 이벤트) khác, hoặc trigger binding/kết xuất (render / 렌더링) đường dẫn (path / 경로). Nếu handler không idempotent, reentrancy tạo vòng lặp (loop / 루프) hoặc duplicate công việc (work / 작업).

Một normalization hàm (function / 함수) tốt nên thỏa:

```text
normalize(normalize(x)) = normalize(x)
```

Tức idempotent về giá trị.

Nếu cần guard:

```javascript
if (scwin.isNormalizing) return;
scwin.isNormalizing = true;
try {
    // mutation
} finally {
    scwin.isNormalizing = false;
}
```

Guard là an toàn (safety / 안전) net; thiết kế (design / 설계) tốt hơn là tách pure normalization khỏi sự kiện (event / 이벤트) wiring.

---

## 5. sự kiện (event / 이벤트) storm và amplification

Một người dùng (user / 사용자) hành động (action / 동작) có thể sửa 1 DataMap trường dữ liệu (field / 필드). Binding cập nhật (update / 업데이트) 5 thành phần (component / 컴포넌트). Mỗi thành phần (component / 컴포넌트) có formatter/validator/sự kiện (event / 이벤트). Một handler lại sửa 10 DataList row.

Công việc (work / 작업) amplification:

```text
1 user action
→ N model mutations
→ N × M binding/render callbacks
→ formatter/expression calls
```

Hiệu năng (performance / 성능) issue không nằm ở “JavaScript chậm” chung chung mà ở amplification factor.

Khi profiling, đếm:

```text
bao nhiêu handler chạy?
bao nhiêu row/cell mutation?
bao nhiêu formatter/expression call?
bao nhiêu render/update?
```

---

## 6. Binding là convenience nhưng vẫn có chi phí (cost / 비용)

Binding giúp mô hình (model / 모델) là nguồn chuẩn (source of truth / 정본), nhưng mỗi bound thành phần (component / 컴포넌트) cần synchronization công việc (work / 작업).

Nếu mã (code / 코드) làm:

```text
for 10.000 rows:
  setCellData(...)
```

và mỗi mutation tạo sự kiện (event / 이벤트)/kết xuất (render / 렌더링) công việc (work / 작업), tổng chi phí (cost / 비용) khác hoàn toàn bulk set một snapshot rồi kết xuất (render / 렌더링) một lần.

Chính xác (exact / 정확한) bulk API tùy DataList/bản dựng (build / 빌드); mô hình tư duy (mental model / 사고 모델) là:

```text
mutation granularity
× observer count
× render cost
```

Cần tối ưu dominant multiplication, không chỉ micro-optimize callback cú pháp (syntax / 문법).

---

## 7. Đừng dùng DOM trực tiếp để “tối ưu” WebSquare thành phần (component / 컴포넌트)

SP5 best-practice guide cảnh báo việc trực tiếp điều khiển DOM/trình duyệt (browser / 브라우저) sự kiện (event / 이벤트) của thành phần (component / 컴포넌트) WebSquare và khuyến nghị dùng khung phần mềm (framework / 프레임워크) lớp trừu tượng (abstraction / 추상화). Lý do không chỉ style.

Engine có thể giữ trạng thái (state / 상태) ngoài DOM. Nếu nhà phát triển (developer / 개발자) sửa DOM trực tiếp:

```text
DOM display
≠ component state
≠ DataCollection state
```

UI có thể trông nhanh/đúng tạm thời nhưng lần kết xuất (render / 렌더링) sau engine ghi đè, khả năng tiếp cận (accessibility / 접근성)/focus bị phá hoặc cleanup không biết tham chiếu (reference / 참조) mới.

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) không được phá quyền sở hữu (ownership / 소유권) mô hình (model / 모델).

---

## 8. sự kiện (event / 이벤트) handler ngân sách (budget / 예산)

Một sự kiện (event / 이벤트) chạy trên trình duyệt (browser / 브라우저) main luồng thực thi (thread / 스레드). Nếu handler làm 80 ms synchronous công việc (work / 작업), đầu vào (input / 입력)/kết xuất (render / 렌더링) khác phải chờ.

Mô hình tư duy (mental model / 사고 모델):

```text
input latency
= queue wait
+ handler synchronous work
+ framework/model propagation
+ render/layout/paint
```

Không cần một con số “chuẩn” cho mọi screen. Cần đo tương tác (interaction / 상호작용) quan trọng và giữ long tác vụ (task / 작업) khỏi đường găng (critical path / 임계 경로).

Heavy transformation có thể được chuyển khỏi hot sự kiện (event / 이벤트), precompute, bộ nhớ đệm (cache / 캐시) hoặc server-side tùy quyền sở hữu (ownership / 소유권).

---

## 9. Formatter và expression là đường xử lý nóng (hot path / 핫 패스) tiềm ẩn

Grid formatter/expression nhìn nhỏ vì hàm (function / 함수) ngắn. Nhưng nếu gọi cho hàng nghìn cell, độ phức tạp (complexity / 복잡도) nhân lên.

Ví dụ:

```text
5.000 rows × 20 columns = 100.000 cell evaluations
```

Nếu mỗi formatter lại scan một DataList 5.000 row:

```text
100.000 × O(5.000)
```

thì bottleneck là algorithmic amplification.

Cấp cao (senior / 시니어) ghi chú (note / 노트): formatter nên gần pure, cheap và tránh mạng (network / 네트워크)/toàn cục (global / 전역) lookup. Lookup map nên được chuẩn bị trước nếu cần.

---

## 10. Sort/filter/group làm thay đổi cả chi phí (cost / 비용) lẫn định danh (identity / 식별자)

Sort/filter không chỉ đổi vị trí row. Nó có thể:

```text
recompute view
invalidate cached index
rerun formatter
rerender visible region
change selection/focus mapping
```

Vì vậy hiệu năng (performance / 성능) kiểm thử (test / 테스트) Grid phải bao gồm tương tác (interaction / 상호작용) thật: sort, filter, edit, scroll, select, không chỉ đo initial tải (load / 로드).

Chapter 13 giải thích định danh (identity / 식별자); chapter này thêm chi phí (cost / 비용) mô hình (model / 모델).

---

## 11. hiệu năng (performance / 성능) ngân sách (budget / 예산) theo stage

Đừng đo “screen mất 3 giây”. Chia:

```text
T_total
= T_resource
+ T_engine/page init
+ T_submission
+ T_server/network
+ T_parse/map
+ T_model mutation
+ T_render
+ T_post-render
```

Với tương tác (interaction / 상호작용):

```text
T_interaction
= T_event queue
+ T_handler
+ T_model propagation
+ T_render/layout/paint
```

Khi stage rõ, tối ưu hóa (optimization / 최적화) mới có mục tiêu (target / 대상).

---

## 12. WebSquare hiệu năng (performance / 성능) instrumentation

Một số SP5 bản dựng (build / 빌드) cung cấp hiệu năng (performance / 성능) instrumentation và `WebSquare.util.setPerformanceUse(...)`; bản phát hành (release / 릴리스) notes cũng mô tả engine hiệu năng (performance / 성능) mark/measure có screen URL detail ở các bản dựng (build / 빌드) tương ứng.

Đây là bằng chứng (evidence / 증거) bổ sung, không thay trình duyệt (browser / 브라우저) profiler.

Kết hợp:

```text
WebSquare performance marks
+ Chrome Performance trace
+ Network timing
+ server correlation timing
+ custom business marks
```

để nối khung phần mềm (framework / 프레임워크) stage với trình duyệt (browser / 브라우저)/máy chủ (server / 서버) stage.

Chính xác (exact / 정확한) API/đầu ra (output / 출력) phải kiểm tra engine bản dựng (build / 빌드).

---

## 13. Custom mark phải đo nghiệp vụ (business / 비즈니스) stage, không chỉ hàm (function / 함수)

Tên mark hữu ích:

```text
employeeSearch:intent
employeeSearch:request-start
employeeSearch:response
employeeSearch:model-ready
employeeSearch:grid-ready
```

Tên ít hữu ích:

```text
fn1-start
fn1-end
```

Môi trường vận hành (production / 운영 환경) question là “người dùng (user / 사용자) chờ ở stage nào?”, không phải “hàm (function / 함수) nào có tên fn1”.

---

## 14. mạng (network / 네트워크) timing phải tách máy chủ (server / 서버) khỏi máy khách (client / 클라이언트)

DevTools thấy yêu cầu (request / 요청) 1.5 s nhưng không tự nói máy chủ (server / 서버) xử lý 1.5 s.

Có thể gồm:

```text
queue/stalled
connection/TLS
request upload
server wait
response download
client parse/mapping
```

Correlation ID + máy chủ (server / 서버) timing giúp phân biệt.

Nếu phản hồi (response / 응답) về 200 ms nhưng Grid usable sau 2 s, backend không phải dominant term.

---

## 15. Payload kích thước (size / 크기) là hiệu năng (performance / 성능) kiến trúc (architecture / 아키텍처)

Một Grid chỉ hiển thị 30 row nhưng endpoint trả 50.000 row. Tối ưu formatter 20% không giải quyết mạng (network / 네트워크)/bộ nhớ (memory / 메모리)/kết xuất (render / 렌더링) kiến trúc (architecture / 아키텍처).

Các lựa chọn:

```text
server paging
server filtering
projection ít column hơn
lazy/detail fetch
chunk loading
```

SP5 có DataList/large-data năng lực (capability / 역량) thay đổi theo bản dựng (build / 빌드), nhưng first principle vẫn là **không vận chuyển trạng thái (state / 상태) máy khách (client / 클라이언트) không cần sở hữu**.

---

## 16. Chunk loading không miễn phí consistency

Tải (load / 로드) dữ liệu (data / 데이터) theo chunk giảm peak độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리) nhưng tạo trạng thái (state / 상태):

```text
loaded range
pending range
failed range
sort/filter version
query version
```

Nếu người dùng (user / 사용자) đổi filter giữa chunk 2 và 3, chunk cũ không được append vào truy vấn (query / 쿼리) mới.

Cần truy vấn (query / 쿼리)/phiên bản (version / 버전) định danh (identity / 식별자) giống stale Submission guard.

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) tạo thêm vòng đời (lifecycle / 생명주기); vòng đời (lifecycle / 생명주기) mới cần tính đúng đắn (correctness / 정확성) mô hình (model / 모델).

---

## 17. DataList siêu dữ liệu (metadata / 메타데이터) và large-data bộ nhớ (memory / 메모리)

SP5 bản phát hành (release / 릴리스) notes mới có tối ưu hóa (optimization / 최적화) giảm rowStatus/cellStatus array element không cần thiết khi set large dữ liệu (data / 데이터). Điều này nhắc rằng DataList không chỉ chứa nghiệp vụ (business / 비즈니스) values.

Bộ nhớ (memory / 메모리) mô hình (model / 모델) gần hơn:

```text
business cell values
+ row metadata
+ cell metadata
+ binding observers
+ Grid/render structures
+ formatter/cache objects
```

Do đó “JSON chỉ 10 MB” không có nghĩa vùng nhớ động (heap / 힙) tăng 10 MB.

---

## 18. động (dynamic / 동적) Submission có vòng đời (lifecycle / 생명주기) chi phí (cost / 비용)

Official hiệu năng (performance / 성능) guide khuyến nghị khai báo Submission cần thiết ở nghiệp vụ (business / 비즈니스) screen và cảnh báo động (dynamic / 동적) creation phải kiểm tra duplicate ID.

Động (dynamic / 동적) Submission có use trường hợp (case / 사례), nhưng tạo mọi yêu cầu (request / 요청) bằng generic factory có thể làm:

```text
ownership khó thấy
workflow linkage khó đọc
duplicate ID/lifetime khó kiểm soát
profiling/log identity kém ổn định
```

Hiệu năng (performance / 성능) và maintainability gặp nhau ở đây: static/declarative đối tượng (object / 객체) khi phù hợp làm thực thi (execution / 실행) đồ thị (graph / 그래프) dễ quan sát hơn.

---

## 19. Debounce, throttle và coalescing giải quyết ba vấn đề khác nhau

Search-as-you-type có thể cần debounce: chỉ chạy sau khi người dùng (user / 사용자) ngừng gõ một khoảng.

Scroll/resize có thể cần throttle: giới hạn tần suất xử lý.

Nhiều mô hình (model / 모델) mutation có thể cần coalescing/batching: gom cập nhật (update / 업데이트) thành một logical lần ghi nhận (commit / 커밋).

Không dùng ba thuật ngữ như nhau.

Quan trọng hơn, debounce không thay stale-result guard. yêu cầu (request / 요청) cũ vẫn có thể về sau yêu cầu (request / 요청) mới.

---

## 20. Repeated listener registration là tính đúng đắn (correctness / 정확성) + hiệu năng (performance / 성능) bug

Page/tab mở nhiều lần và mỗi `onload` add listener vào toàn cục (global / 전역) mục tiêu (target / 대상) nhưng không remove:

```text
open #1 → 1 handler
open #2 → 2 handlers
open #10 → 10 handlers
```

Một click chạy lô-gic (logic / 논리) 10 lần. người dùng (user / 사용자) thấy “app càng dùng càng chậm”.

Đây là thời gian tồn tại (lifetime / 수명) leak, không phải chỉ bộ nhớ (memory / 메모리) leak.

Kiểm thử (test / 테스트):

```text
open → interact → close × 30
```

đo handler invocation count, vùng nhớ động (heap / 힙) và pending timers/listeners.

---

## 21. Timer vòng lặp (loop / 루프) phải có đơn vị sở hữu (owner / 오너)

`setInterval` polling trong page nhưng page close không clear:

```text
closed screen
→ timer alive
→ Submission alive
→ callback closure giữ scope
```

Hậu quả gồm mạng (network / 네트워크) tải (load / 로드), bộ nhớ (memory / 메모리) retention và stale mutation.

Timer cần đơn vị sở hữu (owner / 오너)/thời gian tồn tại (lifetime / 수명) đặc tả hợp đồng (contract / 계약):

```text
create on active
pause on hidden/background nếu phù hợp
dispose on close
```

Chapter 21 mở rộng điều này cho polling/real-time liên kết (connection / 연결).

---

## 22. Spinner và tiến trình (process / 프로세스) message có thể che độ trễ (latency / 지연 시간) nhưng không sửa độ trễ (latency / 지연 시간)

Tiến trình (process / 프로세스) message tốt cho UX khi thao tác (operation / 연산) thật sự cần chờ. Nhưng “thêm loading” không phải hiệu năng (performance / 성능) fix.

Nếu tương tác (interaction / 상호작용) 150 ms, spinner có thể gây visual flicker. Nếu 8 s, cần stage timing và cancellation/thử lại (retry / 재시도) chính sách (policy / 정책).

UX phản hồi (feedback / 피드백) và hệ thống (system / 시스템) hiệu năng (performance / 성능) là hai trục liên quan nhưng khác nhau.

---

## 23. hiệu năng (performance / 성능) kiểm thử (test / 테스트) phải giữ production-like shape

Kiểm thử (test / 테스트) 100 row rồi môi trường vận hành (production / 운영 환경) 30.000 row không cho bằng chứng (evidence / 증거) hữu ích.

Dataset cần đại diện:

```text
row count
column count
text length
formatter complexity
editability
selection/accessibility mode
sort/filter pattern
```

Khả năng tiếp cận (accessibility / 접근성) có thể thay rendering cấu hình (configuration / 구성) ở Grid bản dựng (build / 빌드) tương ứng, vì vậy benchmark phải dùng chế độ (mode / 모드) môi trường vận hành (production / 운영 환경) thật.

---

## 24. Measure warm và cold đường dẫn (path / 경로) riêng

Cold đường dẫn (path / 경로) có thể gồm:

```text
resource load
W-Pack/module load
component creation
first formatter/cache initialization
first network/TLS
```

Warm đường dẫn (path / 경로) có thể reuse bộ nhớ đệm (cache / 캐시)/đối tượng (object / 객체).

Nếu chỉ benchmark lần thứ 10, startup regression bị bỏ qua. Nếu chỉ benchmark cold tải (load / 로드), tương tác (interaction / 상호작용) thường ngày bị che.

---

## 25. hiệu năng (performance / 성능) regression guard

Không cần mọi chỉ số (metric / 지표) thành hard threshold. Nhưng đường găng (critical path / 임계 경로) nên có baseline:

```text
screen ready
search usable
Grid render after response
Save round-trip
heap after repeated open/close
number of requests
payload size
```

Khi engine upgrade hoặc thành phần (component / 컴포넌트) cấu hình (config / 설정) đổi, compare baseline trước/sau.

Hiệu năng (performance / 성능) regression kiểm thử (test / 테스트) đặc biệt quan trọng vì nguồn (source / 소스) nghiệp vụ (business / 비즈니스) mã (code / 코드) có thể không đổi nhưng engine/kết xuất (render / 렌더링) hành vi (behavior / 동작) đổi.

---

## 26. trường hợp (case / 사례) study — `onchange` làm tìm kiếm (search / 검색) chạy hai lần

Một dùng chung (common / 공통) handler normalize mã (code / 코드) rồi programmatically cập nhật (update / 업데이트) thành phần (component / 컴포넌트). Một sự kiện (event / 이벤트) đường dẫn (path / 경로) khác cũng gọi tìm kiếm (search / 검색).

Người dùng (user / 사용자) thay một trường dữ liệu (field / 필드) nhưng hai Submission chạy.

Gỡ lỗi (debug / 디버그) bằng:

```text
event trace
handler invocation count
requestId
stack/call path
```

Fix không phải disable yêu cầu (request / 요청) thứ hai ngẫu nhiên; cần một command đơn vị sở hữu (owner / 오너) duy nhất cho tìm kiếm (search / 검색).

---

## 27. trường hợp (case / 사례) study — Grid 2.000 row chậm sau thêm formatter

Formatter mới lookup label bằng cách scan mã (code / 코드) DataList cho từng cell.

```text
rows 2.000
× columns 8
× code rows 500
```

Hàng triệu comparison phát sinh.

Fix:

```text
prepare codeMap once
→ O(1)-like lookup per cell
```

hoặc bind/lookup cơ chế (mechanism / 메커니즘) phù hợp của khung phần mềm (framework / 프레임워크).

Bằng chứng (evidence / 증거) phải cho thấy formatter đường xử lý nóng (hot path / 핫 패스) giảm, không chỉ cảm giác “nhanh hơn”.

---

## 28. trường hợp (case / 사례) study — Engine upgrade làm edit hành vi (behavior / 동작) đổi

Sau upgrade, kiểm tra hợp lệ (validation / 검증) chạy trước/after sự kiện (event / 이벤트) khác với giả định (assumption / 가정) cũ do thuộc tính (property / 속성)/default/sự kiện (event / 이벤트) thứ tự (ordering / 순서) thay đổi.

Nguồn (source / 소스) page không đổi nhưng hành vi (behavior / 동작) đổi.

Nguyên nhân gốc (root cause / 근본 원인) đồ thị (graph / 그래프):

```text
engine build
→ event semantics
→ handler assumption
→ business behavior
```

Regression suite cần capture sự kiện (event / 이벤트) thứ tự (ordering / 순서) quan trọng và tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) phải coi sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론) là upgrade surface.

---

## 29. trường hợp (case / 사례) study — tìm kiếm (search / 검색) nhanh nhưng screen vẫn treo

Mạng (network / 네트워크) 300 ms. DataList ánh xạ (mapping / 매핑) 100 ms. Grid kết xuất (render / 렌더링) 2.4 s.

Nhóm (team / 팀) tối ưu SQL từ 180 ms xuống 120 ms, người dùng (user / 사용자) gần như không cảm nhận.

Dominant term là kết xuất (render / 렌더링).

Hiệu năng (performance / 성능) ngân sách (budget / 예산) buộc nhóm (team / 팀) sửa đúng tầng (layer / 계층): row count, column độ phức tạp (complexity / 복잡도), formatter, kết xuất (render / 렌더링) chiến lược (strategy / 전략) hoặc paging.

---

## 30. Profiling playbook

Khi screen chậm:

```text
1. Xác định user-visible interval.
2. Gắn intent/request/build/screen identity.
3. Đo Network và server timing.
4. Đo response parse/model mapping.
5. Record browser Performance trace.
6. Tìm long task/hot handler/formatter.
7. Đếm mutation/render amplification.
8. Kiểm tra payload/dataset shape.
9. Kiểm tra repeated listener/timer/request.
10. Thay đổi một dominant factor.
11. Đo lại cùng dataset/build/config.
12. Tạo regression guard.
```

Không bắt đầu bằng việc rewrite hàm (function / 함수) dài nhất nếu chưa có bằng chứng (evidence / 증거) nó nằm trên đường găng (critical path / 임계 경로).

---

## 31. sự kiện (event / 이벤트) kiến trúc (architecture / 아키텍처) rà soát (review / 검토) checklist
Phần “31. sự kiện (event / 이벤트) kiến trúc (architecture / 아키텍처) rà soát (review / 검토) checklist” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Event này là user signal hay business command?
Programmatic mutation có dựa vào implicit event không?
Ordering giữa event có build-dependent không?
Handler có thể re-enter không?
Handler có idempotent không?
Một intent có tạo duplicate command không?
Model mutation có amplification lớn không?
Formatter/expression có chạy trong hot path không?
Listener/timer có owner và cleanup không?
Async callback có stale-intent guard không?
```

---

## 32. hiệu năng (performance / 성능) rà soát (review / 검토) checklist
Phần “32. hiệu năng (performance / 성능) rà soát (review / 검토) checklist” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
User-visible budget được chia stage chưa?
Dominant term là network/server/model/render ở đâu?
Payload có lớn hơn state UI cần không?
Grid dataset production shape là bao nhiêu?
Có server paging/filtering phù hợp không?
Bulk mutation có đang thành hàng nghìn fine-grained mutation không?
Code lookup có complexity ẩn trong formatter không?
Cold/warm path đã đo riêng chưa?
Engine/build/config identity có được ghi lại không?
Repeated lifecycle có tăng heap/listener/request count không?
Optimization đã được đo lại bằng cùng scenario chưa?
```

---

## 33. Master synthesis

Event-driven WebSquare app có thể nhìn như đồ thị (graph / 그래프):

```text
Signal graph
browser/user/native
→ component event
→ command

State graph
command
→ DataCollection mutation
→ binding
→ render

Async graph
command
→ Submission/workflow
→ continuation
→ state convergence

Cost graph
handler
→ observers
→ formatter/expression
→ render/layout/paint
```

Bug tính đúng đắn (correctness / 정확성) thường đến từ đồ thị (graph / 그래프) crossing sai định danh (identity / 식별자) hoặc thứ tự (ordering / 순서). Bug hiệu năng (performance / 성능) thường đến từ amplification giữa các đồ thị (graph / 그래프).

Ở mức Master, nhà phát triển (developer / 개발자) không hỏi “sự kiện (event / 이벤트) nào chạy?” một cách cô lập. Họ hỏi:

```text
signal nào đại diện intent nào,
command owner là ai,
state transition nào xảy ra,
observer nào bị kích hoạt,
ordering nào là contract,
work được khuếch đại bao nhiêu lần,
và evidence nào chứng minh critical path.
```

Đó là khác biệt giữa biết sự kiện (event / 이벤트) API và hiểu hành vi thời gian chạy (runtime behavior / 런타임 동작).

---

## 34. Nguồn kiểm chứng theo bản dựng (build / 빌드)

Chính xác (exact / 정확한) sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론), Grid sự kiện (event / 이벤트) thứ tự (ordering / 순서), hiệu năng (performance / 성능) instrumentation và thành phần (component / 컴포넌트) rendering hành vi (behavior / 동작) phải đối chiếu WebSquare5 SP5 Development Guide/API tham chiếu (reference / 참조)/bản phát hành (release / 릴리스) Notes đúng engine bản dựng (build / 빌드). Các bản phát hành (release / 릴리스) ghi chú (note / 노트) liên quan `viewChangeAfterEdit`, engine hiệu năng (performance / 성능) mark/measure, `WebSquare.util.setPerformanceUse`, DataList large-data bộ nhớ (memory / 메모리) tối ưu hóa (optimization / 최적화) và hiệu năng (performance / 성능) best-practice là nguồn đặc biệt hữu ích.

Không bản sao (copy / 복사) private API từ một bản dựng (build / 빌드) sang chuẩn gốc (canonical / 정본) mã (code / 코드). Dùng API công khai (public API / 공개 API) và regression bằng chứng (evidence / 증거) để bảo vệ hành vi (behavior / 동작) cần thiết.

> **Bàn giao:** Sau **34. Nguồn kiểm chứng theo bản dựng (build / 빌드)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 platform runtime page model](./01_platform_runtime_page_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
