# 16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. mô hình tư duy (mental model / 사고 모델) Master: năm đồ thị (graph / 그래프) chạy đồng thời** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **2. Sáu định danh (identity / 식별자) phải luôn được đặt tên** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối mental model với identity, lifecycle, state và evidence, giúp chuyển một sự cố WebSquare thành chuỗi kiểm chứng có thể lặp lại.

Đạt mức Master với WebSquare không có nghĩa nhớ nhiều thuộc tính (property / 속성) hơn. Nó nghĩa là khi gặp một screen lạ hoặc sự cố (incident / 인시던트) môi trường vận hành (production / 운영 환경), bạn có thể dựng lại **trạng thái (state / 상태) mô hình (model / 모델), vòng đời (lifecycle / 생명주기), định danh (identity / 식별자), đặc tả hợp đồng (contract / 계약) và bằng chứng (evidence / 증거) chuỗi (chain / 사슬)** mà không bị lớp trừu tượng (abstraction / 추상화) của khung phần mềm (framework / 프레임워크) làm mất phương hướng.

Chapter này không thêm một nhóm API mới. Nó hợp nhất toàn thư viện (library / 라이브러리) thành phương pháp lập luận (reasoning / 추론) có thể dùng khi thiết kế (design / 설계), rà soát mã (code review / 코드 리뷰), gỡ lỗi (debug / 디버그), hiệu năng (performance / 성능) tuning, di chuyển (migration / 마이그레이션) và sự cố (incident / 인시던트) phản hồi (response / 응답).

## 1. mô hình tư duy (mental model / 사고 모델) Master: năm đồ thị (graph / 그래프) chạy đồng thời

Một WebSquare ứng dụng (application / 애플리케이션) lớn có thể được hiểu bằng năm đồ thị (graph / 그래프).

**Page đồ thị (graph / 그래프)** mô tả shell, WFrame, tab, popup, parent/child phạm vi (scope / 범위).

**dữ liệu (data / 데이터) đồ thị (graph / 그래프)** mô tả DataMap, DataList, binding, derived view và đơn vị sở hữu (owner / 오너) của nghiệp vụ (business / 비즈니스) trạng thái (state / 상태).

**sự kiện (event / 이벤트) đồ thị (graph / 그래프)** mô tả người dùng (user / 사용자) sự kiện (event / 이벤트), thành phần (component / 컴포넌트) sự kiện (event / 이벤트), DataList sự kiện (event / 이벤트), callback và async continuation.

**yêu cầu (request / 요청) đồ thị (graph / 그래프)** mô tả Submission, phụ thuộc (dependency / 의존성), máy chủ (server / 서버) command, giao dịch (transaction / 트랜잭션) và phản hồi (response / 응답).

**thời gian tồn tại (lifetime / 수명) đồ thị (graph / 그래프)** mô tả đối tượng (object / 객체) nào tạo đối tượng (object / 객체) nào, tham chiếu (reference / 참조) nào giữ đối tượng (object / 객체) sống, khi nào cleanup.

Một bug khó thường là giao điểm của ít nhất hai đồ thị (graph / 그래프).

```text
Popup đóng nhưng request cũ ghi đè Grid
= page/lifetime graph + request graph

Sort xong error map sai row
= data identity graph + event/request graph

Tab mở lại thấy state tab khác
= page instance graph + global data graph
```

Master debugging là tìm đồ thị (graph / 그래프) nào bị trộn ranh giới (boundary / 경계).

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **2. Sáu định danh (identity / 식별자) phải luôn được đặt tên** tổng hợp từ **1. mô hình tư duy (mental model / 사고 모델) Master: năm đồ thị (graph / 그래프) chạy đồng thời** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **3. Bốn readiness trạng thái (state / 상태) thay cho từ “loaded”** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Sáu định danh (identity / 식별자) phải luôn được đặt tên

Trong dự án (project / 프로젝트) lớn, từ “ID” quá mơ hồ. Hãy phân biệt:

```text
component logical ID
runtime frame/scope ID
screen definition ID
screen instance/navigation key
business entity key
request/transaction correlation ID
```

Nếu log chỉ ghi `id=123`, sự cố (incident / 인시던트) investigation sẽ rất chậm. Nếu mã (code / 코드) truyền một `index`/`id` qua nhiều tầng (layer / 계층) mà không biết loại định danh (identity / 식별자), thiết kế (design / 설계) dễ sai.

> **Nối mạch:** Sáu identity giúp trace một release; readiness state tiếp theo tách boot, data, UI và interaction, rồi ba trust boundary xác định nơi cần kiểm soát.

## 3. Bốn readiness trạng thái (state / 상태) thay cho từ “loaded”

Không nói “page tải (load / 로드) xong” nếu chưa chỉ rõ:

```text
source-ready
object/scope-ready
render-ready
business-data-ready
```

Một WFrame có thể object-ready nhưng initial Submission chưa xong. Một tab preload có `scwin` nhưng UI chưa kết xuất (render / 렌더링). Một Grid kết xuất (render / 렌더링) xong nhưng mã (code / 코드) danh sách (list / 목록) chưa tải (load / 로드) nên display label chưa đúng.

Mỗi cross-page đặc tả hợp đồng (contract / 계약) phải yêu cầu readiness đúng mức.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **3. Bốn readiness trạng thái (state / 상태) thay cho từ “loaded”** đặt tiêu chí; **4. Ba trust ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **5. Ba loại quyền sở hữu trạng thái (state ownership / 상태 소유권)** mở rộng hệ quả.

## 4. Ba trust ranh giới (boundary / 경계)

WebSquare nhà phát triển (developer / 개발자) cần nhìn rõ:

```text
browser/client state = untrusted
server application = policy/business enforcement
persistent data/external systems = transaction/integration boundary
```

DataList, hidden trường dữ liệu (field / 필드), disabled button, row status và menu permission đều nằm phía máy khách (client / 클라이언트). Chúng giúp UX/orchestration nhưng không thay máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증)/authorization.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **4. Ba trust ranh giới (boundary / 경계)** đặt tiêu chí; **5. Ba loại quyền sở hữu trạng thái (state ownership / 상태 소유권)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **6. thiết kế (design / 설계) một screen từ bất biến (invariant / 불변식) trước thành phần (component / 컴포넌트)** mở rộng hệ quả.

## 5. Ba loại quyền sở hữu trạng thái (state ownership / 상태 소유권)

Một trạng thái (state / 상태) nên có một đơn vị sở hữu (owner / 오너) chính.

**Presentation trạng thái (state / 상태)**: focus, expanded group, hiện tại (current / 현재) tab, spinner.

**máy khách (client / 클라이언트) nghiệp vụ (business / 비즈니스) working trạng thái (state / 상태)**: DataMap/DataList đang edit, dirty status, tìm kiếm (search / 검색) snapshot.

**chuẩn gốc (canonical / 정본) nghiệp vụ (business / 비즈니스) trạng thái (state / 상태)**: máy chủ (server / 서버)/cơ sở dữ liệu (database / 데이터베이스) hoặc authoritative backend dịch vụ (service / 서비스).

Bug xuất hiện khi presentation trạng thái (state / 상태) được dùng làm nghiệp vụ (business / 비즈니스) truth, hoặc máy khách (client / 클라이언트) working trạng thái (state / 상태) được coi là chuẩn gốc (canonical / 정본) sau khi máy chủ (server / 서버) đã normalize/thay đổi (change / 변경).

> **Nối mạch:** State ownership quyết định ai được ghi; thiết kế screen từ invariant tiếp theo biến ownership đó thành guard trước khi chọn component.

## 6. thiết kế (design / 설계) một screen từ bất biến (invariant / 불변식) trước thành phần (component / 컴포넌트)

Trước khi kéo Grid/đầu vào (input / 입력) trong Studio, viết bất biến (invariant / 불변식):

```text
Order ID immutable sau create.
Amount > 0.
Chỉ APPROVED request mới được export.
Hai user không được silently overwrite nhau.
Save không được duplicate khi retry.
```

Sau đó map đơn vị sở hữu (owner / 오너):

```text
UI filter/feedback → WebSquare
working edit state → DataList
cross-field validation → page/domain function
concurrency/idempotency/authorization → server
```

Thành phần (component / 컴포넌트)/API được chọn sau khi đơn vị sở hữu (owner / 오너) rõ.

> **Nối mạch:** Invariant dẫn tới page contract; coi page như service contract giúp thiết kế submission theo failure path trước khi tối ưu success path.

## 7. thiết kế (design / 설계) page đặc tả hợp đồng (contract / 계약) như dịch vụ (service / 서비스) đặc tả hợp đồng (contract / 계약)

Mỗi reusable screen/UDC/popup nên có:

```text
input
public commands
observable output/events
owned state
side effects
lifecycle/cleanup
```

Ví dụ thứ tự (order / 순서) Detail:

```text
Input: { orderId, mode }
Command: reload(), canClose()
Output: ORDER_CHANGED / close result
Owned state: dmOrder, validation state, pending save
Side effect: sbmLoad, sbmSave
Cleanup: timer/listener/pending result guard
```

Nếu bên tiêu thụ (consumer / 소비자) cần biết `inputOrderId` hoặc `grdLine`, đặc tả hợp đồng (contract / 계약) chưa đủ tốt.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **8. thiết kế (design / 설계) Submission từ thất bại (failure / 실패) trước success** nối từ **7. thiết kế (design / 설계) page đặc tả hợp đồng (contract / 계약) như dịch vụ (service / 서비스) đặc tả hợp đồng (contract / 계약)** sang **9. Debugging playbook: từ symptom đến ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. thiết kế (design / 설계) Submission từ thất bại (failure / 실패) trước success

Happy đường dẫn (path / 경로) dễ viết. môi trường vận hành (production / 운영 환경) thiết kế (design / 설계) nên bắt đầu bằng câu hỏi:

```text
Nếu timeout sau server commit thì sao?
Nếu response cũ về sau response mới thì sao?
Nếu user double-click thì sao?
Nếu session expire thì sao?
Nếu partial batch fail thì sao?
Nếu page đóng khi request pending thì sao?
```

Sau khi trả lời được, success đường dẫn (path / 경로) thường tự rõ.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **8. thiết kế (design / 설계) Submission từ thất bại (failure / 실패) trước success** đặt tiêu chí; **9. Debugging playbook: từ symptom đến ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **10. hiệu năng (performance / 성능) playbook: chia độ trễ (latency / 지연 시간) thành ngân sách (budget / 예산)** mở rộng hệ quả.

## 9. Debugging playbook: từ symptom đến ranh giới (boundary / 경계)

Khi sự cố (incident / 인시던트) xảy ra, không đọc toàn codebase. Đi theo bằng chứng (evidence / 증거) chuỗi (chain / 사슬).

```text
1. Reproduce và ghi user intent.
2. Xác định screen instance/scope.
3. Snapshot client model trước action.
4. Trace event/call path đến Submission.
5. Inspect request payload thực tế.
6. Inspect HTTP status/body/timing.
7. Correlate server trace nếu có.
8. Inspect target/model sau response.
9. Inspect rendering/selection/focus.
10. Kiểm tra callback stale hoặc cleanup/lifetime.
```

Nếu bước 4 chưa có yêu cầu (request / 요청), đừng gỡ lỗi (debug / 디버그) SQL. Nếu phản hồi (response / 응답) đúng và DataList đúng, đừng blame API.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **9. Debugging playbook: từ symptom đến ranh giới (boundary / 경계)** đặt tiêu chí; **10. hiệu năng (performance / 성능) playbook: chia độ trễ (latency / 지연 시간) thành ngân sách (budget / 예산)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **11. bộ nhớ (memory / 메모리) playbook: reachability thay vì “đã close”** mở rộng hệ quả.

## 10. hiệu năng (performance / 성능) playbook: chia độ trễ (latency / 지연 시간) thành ngân sách (budget / 예산)

Một tìm kiếm (search / 검색) screen:

```text
T_total
= T_event
+ T_validation
+ T_request_queue
+ T_network_server
+ T_download_parse
+ T_mapping
+ T_render
+ T_post_render
```

Đo từng phần. “Grid chậm” có thể thật ra là 8 MB phản hồi (response / 응답) hoặc formatter O(n²).

Hiệu năng (performance / 성능) fix phải giảm dominant term, không giảm term dễ sửa nhất.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **11. bộ nhớ (memory / 메모리) playbook: reachability thay vì “đã close”** nối từ **10. hiệu năng (performance / 성능) playbook: chia độ trễ (latency / 지연 시간) thành ngân sách (budget / 예산)** sang **12. bảo mật (security / 보안) playbook: giả định máy khách (client / 클라이언트) bị sửa**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. bộ nhớ (memory / 메모리) playbook: reachability thay vì “đã close”

Garbage collector chỉ giải phóng đối tượng (object / 객체) không còn reachable.

Một closed page vẫn sống nếu:

```text
global registry → scope
document listener → closure → scope
setInterval → callback → DataList
pending promise/callback → page object
third-party widget → DOM/component
```

Kiểm thử (test / 테스트) bằng repeated vòng đời (lifecycle / 생명주기):

```text
open → interact → close × 30
```

Sau mỗi vòng quan sát vùng nhớ động (heap / 힙), listener/yêu cầu (request / 요청) count. Một vùng nhớ động (heap / 힙) snapshot đơn lẻ không đủ chứng minh leak.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **12. bảo mật (security / 보안) playbook: giả định máy khách (client / 클라이언트) bị sửa** nối từ **11. bộ nhớ (memory / 메모리) playbook: reachability thay vì “đã close”** sang **13. di chuyển (migration / 마이그레이션) playbook: preserve bất biến (invariant / 불변식), replace cơ chế (mechanism / 메커니즘)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. bảo mật (security / 보안) playbook: giả định máy khách (client / 클라이언트) bị sửa

Khi rà soát (review / 검토) Save luồng (flow / 흐름), tưởng tượng người dùng (user / 사용자) đã:

```text
unhide hidden field
enable disabled button
change DataList directly
forge row status
modify request payload
replay request
change entity ID
```

Nếu máy chủ (server / 서버) vẫn giữ bất biến (invariant / 불변식), kiến trúc (architecture / 아키텍처) đúng. Nếu chỉ UI ngăn được, đó là bảo mật (security / 보안) gap.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **12. bảo mật (security / 보안) playbook: giả định máy khách (client / 클라이언트) bị sửa** đặt đầu vào cho **13. di chuyển (migration / 마이그레이션) playbook: preserve bất biến (invariant / 불변식), replace cơ chế (mechanism / 메커니즘)**, rồi **14. bản phát hành (release / 릴리스) playbook: nguồn (source / 소스) không phải sản phẩm tạo ra (artifact / 산출물)** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. di chuyển (migration / 마이그레이션) playbook: preserve bất biến (invariant / 불변식), replace cơ chế (mechanism / 메커니즘)

Khi migrate legacy `$w`, IFrame, toàn cục (global / 전역) variable, jQuery DOM hack hoặc synchronous Submission, đừng rewrite chỉ vì cú pháp (syntax / 문법) cũ.

Quy trình:

```text
identify current behavior/invariant
→ capture regression evidence
→ identify hidden dependency
→ choose modern boundary
→ migrate one boundary
→ compare behavior/performance
→ remove compatibility layer khi evidence đủ
```

Ví dụ `window.parent.grdA...` không nên đổi máy móc thành `$p.parent().grdA...`. Mục tiêu là thay direct nội bộ (internal / 내부) truy cập (access / 접근) bằng page đặc tả hợp đồng (contract / 계약) nếu có thể.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **13. di chuyển (migration / 마이그레이션) playbook: preserve bất biến (invariant / 불변식), replace cơ chế (mechanism / 메커니즘)** đặt vấn đề; **14. bản phát hành (release / 릴리스) playbook: nguồn (source / 소스) không phải sản phẩm tạo ra (artifact / 산출물)** đối chiếu bằng chứng, rồi **15. trường hợp (case / 사례) study A — tìm kiếm (search / 검색) kết quả (result / 결과) thỉnh thoảng quay về dữ liệu cũ** mở rộng hệ quả hoặc giới hạn liên quan.

## 14. bản phát hành (release / 릴리스) playbook: nguồn (source / 소스) không phải sản phẩm tạo ra (artifact / 산출물)

Một bản phát hành (release / 릴리스) phải dấu vết (trace / 추적) được:

```text
Git commit
→ W-Pack/build tool + config
→ artifact hash/version
→ deployed environment
→ cache/CDN/browser response
→ runtime engine/config identity
```

Nếu người dùng (user / 사용자) thấy UI cũ, “lần ghi nhận (commit / 커밋) đã merge” không phải bằng chứng (evidence / 증거) đủ. mạng (network / 네트워크) phản hồi (response / 응답)/sản phẩm tạo ra (artifact / 산출물) phiên bản (version / 버전) mới là bằng chứng (evidence / 증거) trình duyệt (browser / 브라우저) đang chạy gì.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **14. bản phát hành (release / 릴리스) playbook: nguồn (source / 소스) không phải sản phẩm tạo ra (artifact / 산출물)** nêu quy tắc; **15. trường hợp (case / 사례) study A — tìm kiếm (search / 검색) kết quả (result / 결과) thỉnh thoảng quay về dữ liệu cũ** thử quy tắc trong tình huống, rồi **16. trường hợp (case / 사례) study B — Save đôi lúc gửi giá trị cũ của cell cuối** mở rộng hệ quả.

## 15. trường hợp (case / 사례) study A — tìm kiếm (search / 검색) kết quả (result / 결과) thỉnh thoảng quay về dữ liệu cũ

Symptom: người dùng (user / 사용자) tìm kiếm (search / 검색) `Kim`, đổi nhanh thành `Lee`; đôi lúc Grid cuối cùng lại hiển thị `Kim`.

Page đồ thị (graph / 그래프) không có vấn đề. dữ liệu (data / 데이터) đồ thị (graph / 그래프) có một mục tiêu (target / 대상) `dlUser`. yêu cầu (request / 요청) đồ thị (graph / 그래프) có A và B chạy async.

```text
A(Kim) sent
B(Lee) sent
B response → dlUser = Lee
A response → dlUser = Kim
```

Nguyên nhân gốc (root cause / 근본 원인) là latest-intent bất biến (invariant / 불변식) thiếu. Fix ranh giới (boundary / 경계) có thể là cancel yêu cầu (request / 요청) cũ nếu API/bản dựng (build / 빌드) hỗ trợ hoặc yêu cầu (request / 요청) generation đơn vị từ (token / 토큰) để stale callback không apply kết quả (result / 결과).

Regression kiểm thử (test / 테스트) phải cố tình làm A chậm hơn B. Debounce chỉ giảm tần suất, không chứng minh thứ tự (ordering / 순서).

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **15. trường hợp (case / 사례) study A — tìm kiếm (search / 검색) kết quả (result / 결과) thỉnh thoảng quay về dữ liệu cũ** nêu quy tắc; **16. trường hợp (case / 사례) study B — Save đôi lúc gửi giá trị cũ của cell cuối** thử quy tắc trong tình huống, rồi **17. trường hợp (case / 사례) study C — Popup save xong refresh nhầm tab** mở rộng hệ quả.

## 16. trường hợp (case / 사례) study B — Save đôi lúc gửi giá trị cũ của cell cuối

Symptom: người dùng (user / 사용자) gõ `100`, click Save ngay; máy chủ (server / 서버) nhận `90`.

Đừng thêm delay. dấu vết (trace / 추적) editing vòng đời (lifecycle / 생명주기):

```text
editor value = 100
DataList value = 90
Save handler executes
Submission serializes DataList
```

Nguyên nhân gốc (root cause / 근본 원인) nằm ở edit lần ghi nhận (commit / 커밋) ranh giới (boundary / 경계). Fix bằng công khai (public / 공개) vòng đời (lifecycle / 생명주기)/API/convention để hiện tại (current / 현재) edit lần ghi nhận (commit / 커밋) trước serialization, sau đó kiểm thử (test / 테스트) trực tiếp “edit rồi click Save không blur trước”.

Đây là ví dụ editor trạng thái (state / 상태) khác chuẩn gốc (canonical / 정본) máy khách (client / 클라이언트) mô hình (model / 모델).

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **16. trường hợp (case / 사례) study B — Save đôi lúc gửi giá trị cũ của cell cuối** nêu quy tắc; **17. trường hợp (case / 사례) study C — Popup save xong refresh nhầm tab** thử quy tắc trong tình huống, rồi **18. trường hợp (case / 사례) study D — Grid 50.000 row tải (load / 로드) nhanh mạng (network / 네트워크) nhưng UI freeze** mở rộng hệ quả.

## 17. trường hợp (case / 사례) study C — Popup save xong refresh nhầm tab

Có hai thứ tự (order / 순서) danh sách (list / 목록) tab với filter khác nhau. Detail popup dùng `$p.top()` tìm `grdOrder` và cập nhật (update / 업데이트) row chỉ mục (index / 인덱스) 4.

Bug có ba định danh (identity / 식별자) bị trộn:

```text
screen instance identity
business order identity
row index
```

Fix kiến trúc (architecture / 아키텍처): popup trả `{orderId, changed:true}` về đơn vị sở hữu (owner / 오너)/caller. Caller quyết định re-query hoặc patch bằng nghiệp vụ (business / 비즈니스) key. Không traverse top để tìm Grid.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **17. trường hợp (case / 사례) study C — Popup save xong refresh nhầm tab** nêu quy tắc; **18. trường hợp (case / 사례) study D — Grid 50.000 row tải (load / 로드) nhanh mạng (network / 네트워크) nhưng UI freeze** thử quy tắc trong tình huống, rồi **19. trường hợp (case / 사례) study E — Mở/đóng tab nhiều lần yêu cầu (request / 요청) tăng gấp đôi** mở rộng hệ quả.

## 18. trường hợp (case / 사례) study D — Grid 50.000 row tải (load / 로드) nhanh mạng (network / 네트워크) nhưng UI freeze

Mạng (network / 네트워크) 150 ms, phản hồi (response / 응답) 6 MB, parse + DataList + kết xuất (render / 렌더링) 3.5 s. hiệu năng (performance / 성능) dấu vết (trace / 추적) cho thấy formatter và summary chạy nhiều.

Possible chiến lược (strategy / 전략):

```text
server paging/filter để giảm row
simplify formatter hot path
reduce derived recalculation
use appropriate Grid rendering strategy
avoid eager hidden tabs
```

Đừng chỉ bật virtual scroll rồi kết luận xong; parse/mô hình (model / 모델) bộ nhớ (memory / 메모리) vẫn còn nếu full payload giữ nguyên.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **18. trường hợp (case / 사례) study D — Grid 50.000 row tải (load / 로드) nhanh mạng (network / 네트워크) nhưng UI freeze** nêu quy tắc; **19. trường hợp (case / 사례) study E — Mở/đóng tab nhiều lần yêu cầu (request / 요청) tăng gấp đôi** thử quy tắc trong tình huống, rồi **20. trường hợp (case / 사례) study F — môi trường vận hành (production / 운영 환경) lỗi nhưng UAT đúng** mở rộng hệ quả.

## 19. trường hợp (case / 사례) study E — Mở/đóng tab nhiều lần yêu cầu (request / 요청) tăng gấp đôi

Lần đầu một polling yêu cầu (request / 요청)/30s. Sau 10 lần mở/đóng, mạng (network / 네트워크) thấy 10 yêu cầu (request / 요청)/30s.

Hypothesis mạnh: timer/listener vòng đời (lifecycle / 생명주기) leak.

Dấu vết (trace / 추적) thời gian tồn tại (lifetime / 수명) đồ thị (graph / 그래프) cho thấy `setInterval` giữ closure `scwin.refresh`. Tab close không clear timer. Fix ở cleanup ranh giới (boundary / 경계), không ở backend tỷ lệ (rate / 비율) limit.

Regression kiểm thử (test / 테스트) lặp open/close và assert active timer/yêu cầu (request / 요청) count không tăng.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **19. trường hợp (case / 사례) study E — Mở/đóng tab nhiều lần yêu cầu (request / 요청) tăng gấp đôi** nêu quy tắc; **20. trường hợp (case / 사례) study F — môi trường vận hành (production / 운영 환경) lỗi nhưng UAT đúng** thử quy tắc trong tình huống, rồi **21. trường hợp (case / 사례) study G — Batch Save 100 row, 3 row lỗi** mở rộng hệ quả.

## 20. trường hợp (case / 사례) study F — môi trường vận hành (production / 운영 환경) lỗi nhưng UAT đúng

Nguồn (source / 소스) lần ghi nhận (commit / 커밋) giống nhau. Đừng dừng ở Git.

So sánh:

```text
engine build
W-Pack artifact hash
client/server config
context root
proxy/cache header
browser artifact response
backend API version
```

Nếu PROD còn sản phẩm tạo ra (artifact / 산출물) cũ, fix triển khai (deployment / 배포)/bộ nhớ đệm (cache / 캐시). Nếu engine bản dựng (build / 빌드) khác, kiểm tra bản phát hành (release / 릴리스) ghi chú (note / 노트)/regression. Nếu cấu hình (config / 설정) khác, tìm cấu hình (config / 설정) drift.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **20. trường hợp (case / 사례) study F — môi trường vận hành (production / 운영 환경) lỗi nhưng UAT đúng** nêu quy tắc; **21. trường hợp (case / 사례) study G — Batch Save 100 row, 3 row lỗi** thử quy tắc trong tình huống, rồi **22. trường hợp (case / 사례) study H — người dùng (user / 사용자) không có menu nhưng vẫn gọi được Save API** mở rộng hệ quả.

## 21. trường hợp (case / 사례) study G — Batch Save 100 row, 3 row lỗi

Nếu backend all-or-nothing, máy khách (client / 클라이언트) phải giữ 100 row chưa lần ghi nhận (commit / 커밋) và show 3 nguyên nhân. Nếu backend partial, 97 row cần normalize/reset, 3 row giữ dirty/lỗi (error / 오류).

Không thể thiết kế UI đúng nếu giao dịch (transaction / 트랜잭션) đặc tả hợp đồng (contract / 계약) chưa rõ. Đây là ví dụ “frontend bug” thực ra là đặc tả hợp đồng (contract / 계약) ambiguity.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **21. trường hợp (case / 사례) study G — Batch Save 100 row, 3 row lỗi** nêu quy tắc; **22. trường hợp (case / 사례) study H — người dùng (user / 사용자) không có menu nhưng vẫn gọi được Save API** thử quy tắc trong tình huống, rồi **23. trường hợp (case / 사례) study I — Excel export lộ cột nhạy cảm** mở rộng hệ quả.

## 22. trường hợp (case / 사례) study H — người dùng (user / 사용자) không có menu nhưng vẫn gọi được Save API

Ẩn menu chỉ là điều hướng (navigation / 내비게이션) UX. Nếu endpoint không check authorization, attacker có thể forge yêu cầu (request / 요청).

Fix máy chủ (server / 서버) authorization. Frontend vẫn có thể ẩn/disable để UX phù hợp, nhưng bảo mật (security / 보안) kiểm thử (test / 테스트) phải gọi yêu cầu (request / 요청) không qua UI và kỳ vọng máy chủ (server / 서버) reject.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **22. trường hợp (case / 사례) study H — người dùng (user / 사용자) không có menu nhưng vẫn gọi được Save API** nêu quy tắc; **23. trường hợp (case / 사례) study I — Excel export lộ cột nhạy cảm** thử quy tắc trong tình huống, rồi **24. trường hợp (case / 사례) study J — Engine upgrade làm sự kiện (event / 이벤트) thứ tự (order / 순서) thay đổi** mở rộng hệ quả.

## 23. trường hợp (case / 사례) study I — Excel export lộ cột nhạy cảm

Grid ẩn `PERSONAL_ID`, nhưng DataList vẫn có trường dữ liệu (field / 필드) và export cấu hình (config / 설정) lấy nguồn (source / 소스) dữ liệu (data / 데이터) rộng hơn visible view.

Nguyên nhân gốc (root cause / 근본 원인): hidden presentation bị nhầm với dữ liệu (data / 데이터) authorization/export đặc tả hợp đồng (contract / 계약).

Fix bằng tường minh (explicit / 명시적) export lược đồ (schema / 스키마)/whitelist và máy chủ (server / 서버) chính sách (policy / 정책) nếu export được tạo server-side. Regression kiểm thử (test / 테스트) tệp (file / 파일) đầu ra (output / 출력), không chỉ screenshot Grid.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **23. trường hợp (case / 사례) study I — Excel export lộ cột nhạy cảm** nêu quy tắc; **24. trường hợp (case / 사례) study J — Engine upgrade làm sự kiện (event / 이벤트) thứ tự (order / 순서) thay đổi** thử quy tắc trong tình huống, rồi **25. rà soát mã (code review / 코드 리뷰) ở mức Master** mở rộng hệ quả.

## 24. trường hợp (case / 사례) study J — Engine upgrade làm sự kiện (event / 이벤트) thứ tự (order / 순서) thay đổi

Một screen phụ thuộc `onviewchange` chạy trước/after edit theo giả định (assumption / 가정) cũ. Engine/bản dựng (build / 빌드) mới có thuộc tính (property / 속성)/default khác.

Di chuyển (migration / 마이그레이션) luồng (flow / 흐름):

```text
capture old event trace
read release note/API reference
set explicit config nếu cần
update regression test
remove reliance on ambiguous order nếu có thể
```

Đây là lý do thư viện (library / 라이브러리) ưu tiên cơ chế (mechanism / 메커니즘) và bằng chứng (evidence / 증거) hơn học thuộc default.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **24. trường hợp (case / 사례) study J — Engine upgrade làm sự kiện (event / 이벤트) thứ tự (order / 순서) thay đổi** nêu quy tắc; **25. rà soát mã (code review / 코드 리뷰) ở mức Master** thử quy tắc trong tình huống, rồi **26. Master checklist cho một screen mới** mở rộng hệ quả.

## 25. rà soát mã (code review / 코드 리뷰) ở mức Master

Một rà soát (review / 검토) tốt không chỉ tìm cú pháp (syntax / 문법) lỗi. Nó hỏi:

```text
State owner là ai?
Identity nào đang được truyền?
Index có sống lâu hơn event không?
Async result có stale guard không?
Page contract có xuyên internals không?
Dirty state có thể mất khi navigation không?
Server contract có concurrency/idempotency không?
Failure path có terminal cleanup không?
Bulk operation có event/render storm không?
Generated/private API có bị phụ thuộc không?
Test nào chứng minh invariant này?
Production evidence nào giúp debug nếu nó fail?
```

Nếu PR không trả lời được các câu liên quan, rà soát (review / 검토) chưa kết thúc ở mức kiến trúc (architecture / 아키텍처).

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **26. Master checklist cho một screen mới** nối từ **25. rà soát mã (code review / 코드 리뷰) ở mức Master** sang **27. Capstone Master — xây một mini enterprise ứng dụng (application / 애플리케이션)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Master checklist cho một screen mới

### Trước khi mã (code / 코드)

Xác định screen purpose, đầu vào (input / 입력)/đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약), DataCollection đơn vị sở hữu (owner / 오너), máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약), định danh (identity / 식별자) và giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론).

### Khi mã (code / 코드)

Giữ handler mỏng, lĩnh vực (domain / 도메인) hàm (function / 함수) có tên, mô hình (model / 모델) là nguồn chuẩn (source of truth / 정본), phạm vi (scope / 범위) phụ thuộc (dependency / 의존성) tường minh (explicit / 명시적), async vòng đời (lifecycle / 생명주기) có guard và cleanup.

### Trước khi merge

Kiểm thử (test / 테스트) success/lỗi (error / 오류)/hết thời gian chờ (timeout / 타임아웃)/double-click/stale phản hồi (response / 응답)/unsaved điều hướng (navigation / 내비게이션); kiểm tra keyboard/khả năng tiếp cận (accessibility / 접근성); đo dataset/hiệu năng (performance / 성능) hợp lý; không log secret/PII.

### Trước khi deploy

Biết sản phẩm tạo ra (artifact / 산출물)/bản dựng (build / 빌드)/cấu hình (config / 설정) định danh (identity / 식별자), regression trên engine tương ứng, bộ nhớ đệm (cache / 캐시) chiến lược (strategy / 전략) và quay lui (rollback / 롤백) đường dẫn (path / 경로).

### Khi môi trường vận hành (production / 운영 환경) lỗi

Lấy bằng chứng (evidence / 증거) trước khi sửa. Xác định ranh giới (boundary / 경계) rồi mới thay mã (code / 코드).

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **27. Capstone Master — xây một mini enterprise ứng dụng (application / 애플리케이션)** nối từ **26. Master checklist cho một screen mới** sang **28. Cách tiếp tục sau thư viện (library / 라이브러리) này**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Capstone Master — xây một mini enterprise ứng dụng (application / 애플리케이션)

Capstone nên có:

```text
App shell
├─ menu
├─ multi-tab navigation
├─ Employee Search
├─ Employee Detail
└─ reusable EmployeePicker UDC
```

Employee tìm kiếm (search / 검색) dùng `dmSearch → sbmSearch → dlEmployee → GridView`, máy chủ (server / 서버) paging và truy vấn (query / 쿼리) snapshot. Detail mở bằng điều hướng (navigation / 내비게이션) key theo employee ID, có optimistic locking và unsaved-change guard. EmployeePicker expose thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트), không biết parent internals.

Thêm fault injection:

```text
search A response về sau B
Save double-click
timeout sau commit
version conflict
session expiration
partial batch failure
Excel import invalid row
tab close khi request pending
30 lần open/close để test leak
stale W-Pack cache ở environment giả lập
```

Nếu bạn có thể giải thích đơn vị sở hữu (owner / 오너), định danh (identity / 식별자), vòng đời (lifecycle / 생명주기), bằng chứng (evidence / 증거) và fix ranh giới (boundary / 경계) của từng trường hợp (case / 사례), bạn đã đi qua thư viện (library / 라이브러리) theo đúng mục tiêu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **28. Cách tiếp tục sau thư viện (library / 라이브러리) này** nối từ **27. Capstone Master — xây một mini enterprise ứng dụng (application / 애플리케이션)** sang **29. Bản đồ quay lại chapter gốc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Cách tiếp tục sau thư viện (library / 라이브러리) này

Sau mức Master, giá trị cao nhất không đến từ thêm 500 thuộc tính (property / 속성) GridView vào ghi chú (note / 노트). Nó đến từ đọc API/bản phát hành (release / 릴리스) ghi chú (note / 노트) đúng bản dựng (build / 빌드) khi cần, quan sát codebase thực, và bổ sung trường hợp (case / 사례) study khi gặp một dạng thất bại (failure mode / 실패 모드) mới có tính khái quát.

Một topic chỉ nên được thêm vào chuẩn gốc (canonical / 정본) thư viện (library / 라이브러리) nếu nó tạo mô hình tư duy (mental model / 사고 모델) hoặc lập luận (reasoning / 추론) reusable. Project-specific ID, endpoint và workaround nên ở dự án (project / 프로젝트) docs/runbook, không làm loãng chuẩn gốc (canonical / 정본) WebSquare kiến thức (knowledge / 지식).

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **29. Bản đồ quay lại chapter gốc** nối từ **28. Cách tiếp tục sau thư viện (library / 라이브러리) này** sang **30. Kết luận**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Bản đồ quay lại chapter gốc

Khi thiếu thời gian chạy (runtime / 런타임)/page mô hình tư duy (mental model / 사고 모델), quay lại [01](01_platform_runtime_page_model.md) và [02](02_components_events_binding.md).

Khi lỗi dữ liệu (data / 데이터)/yêu cầu (request / 요청), quay lại [03](03_data_collection_submission.md) và [15](15_backend_contract_transaction_concurrency.md).

Khi lỗi phạm vi (scope / 범위)/điều hướng (navigation / 내비게이션), quay lại [04](04_scope_wframe_popup_spa.md) và [14](14_application_shell_navigation_state.md).

Khi lỗi Grid/edit/chỉ mục (index / 인덱스), quay lại [05](05_gridview_crud_patterns.md) và [13](13_gridview_editing_identity_internals.md).

Khi lỗi môi trường vận hành (production / 운영 환경)/hiệu năng (performance / 성능)/bảo mật (security / 보안), quay lại [06](06_debugging_performance_security.md), [10](10_rendering_lazy_loading_lifetime.md) và [12](12_build_config_deployment.md).

Khi refactor/migrate/kiểm thử (test / 테스트), quay lại [07](07_legacy_modern_migration.md), [08](08_reusable_architecture_udc_common_modules.md) và [11](11_testing_testability_regression.md).

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **30. Kết luận** tổng hợp từ **29. Bản đồ quay lại chapter gốc** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **31. Master extension — thêm ba đồ thị (graph / 그래프) cho tệp (file / 파일), bản địa (native / 네이티브) và bằng chứng (evidence / 증거)** mở rộng hệ quả hoặc giới hạn liên quan.

## 30. Kết luận

Mô hình tư duy (mental model / 사고 모델) cuối cùng của WebSquare enterprise development là:

```text
Intent
→ Screen instance
→ Event
→ Canonical client state
→ Contract
→ Server transaction
→ Canonical result
→ Reconciliation
→ Render
→ Evidence
```

Bao quanh luồng (flow / 흐름) đó là phạm vi (scope / 범위), thời gian tồn tại (lifetime / 수명), bảo mật (security / 보안), hiệu năng (performance / 성능), testing và triển khai (deployment / 배포) định danh (identity / 식별자).

Khi bạn có thể giữ tất cả ranh giới (boundary / 경계) này rõ trong đầu, WebSquare không còn là một tập API khó nhớ. Nó trở thành một thời gian chạy (runtime / 런타임) có quy tắc mà bạn có thể lập luận (reasoning / 추론), đo, kiểm thử (test / 테스트) và vận hành một cách có hệ thống.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **30. Kết luận** đặt vấn đề; **31. Master extension — thêm ba đồ thị (graph / 그래프) cho tệp (file / 파일), bản địa (native / 네이티브) và bằng chứng (evidence / 증거)** đối chiếu bằng chứng, rồi **32. định danh (identity / 식별자) mô hình (model / 모델) mở rộng** mở rộng hệ quả hoặc giới hạn liên quan.

## 31. Master extension — thêm ba đồ thị (graph / 그래프) cho tệp (file / 파일), bản địa (native / 네이티브) và bằng chứng (evidence / 증거)

Khi thư viện (library / 라이브러리) mở rộng sang tệp (file / 파일) transfer, hybrid app và khả năng quan sát (observability / 관측 가능성), năm đồ thị (graph / 그래프) ban đầu vẫn đúng nhưng chưa đủ chi tiết cho môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) hiện đại. Hãy bổ sung ba đồ thị (graph / 그래프) chuyên biệt.

**sản phẩm tạo ra (artifact / 산출물) đồ thị (graph / 그래프)** theo dõi tệp (file / 파일)/upload/export sản phẩm tạo ra (artifact / 산출물) từ trình duyệt (browser / 브라우저) đến lưu trữ (storage / 저장소), siêu dữ liệu (metadata / 메타데이터) và nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너).

**bản địa (native / 네이티브) năng lực (capability / 역량) đồ thị (graph / 그래프)** theo dõi WebSquare intent → cầu nối (bridge / 브리지) yêu cầu (request / 요청) → bản địa (native / 네이티브)/plugin thao tác (operation / 연산) → callback/deep link → WebSquare reconciliation.

**bằng chứng (evidence / 증거) đồ thị (graph / 그래프)** theo dõi người dùng (user / 사용자) hành động (action / 동작) → yêu cầu (request / 요청)/correlation ID → máy khách (client / 클라이언트) log → mạng (network / 네트워크) → máy chủ (server / 서버)/bản địa (native / 네이티브) log → chỉ số (metric / 지표)/dấu vết (trace / 추적).

Một sự cố (incident / 인시던트) có thể giao cả ba:

```text
User export report trong hybrid app
→ server tạo file
→ native download
→ app background
→ callback về page cũ
→ log không có requestId
```

Nếu chỉ nhìn Submission đồ thị (graph / 그래프), bạn sẽ bỏ lỡ lưu trữ (storage / 저장소)/bản địa (native / 네이티브)/thời gian tồn tại (lifetime / 수명) ranh giới (boundary / 경계).

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **31. Master extension — thêm ba đồ thị (graph / 그래프) cho tệp (file / 파일), bản địa (native / 네이티브) và bằng chứng (evidence / 증거)** đặt vấn đề; **32. định danh (identity / 식별자) mô hình (model / 모델) mở rộng** đối chiếu bằng chứng, rồi **33. trường hợp (case / 사례) study K — Upload thành công nhưng Save thất bại (fail / 실패)** mở rộng hệ quả hoặc giới hạn liên quan.

## 32. định danh (identity / 식별자) mô hình (model / 모델) mở rộng

Master nhánh học (track / 트랙) mới cần phân biệt thêm:

```text
attachment/file ID
physical storage key
upload session/intent ID
export job ID
native operation request ID
app/web build ID
correlation/trace ID
```

`fileName`, `rowIndex`, `URL` hay callback hàm (function / 함수) name không phải định danh (identity / 식별자) ổn định cho các thao tác (operation / 연산) dài.

Quy tắc (rule / 규칙) tổng quát:

```text
identity phải sống ít nhất lâu bằng operation mà nó đại diện
```

Nếu thao tác (operation / 연산) sống qua page reload/background, định danh (identity / 식별자) không thể chỉ là cục bộ (local / 로컬) variable trong page.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **32. định danh (identity / 식별자) mô hình (model / 모델) mở rộng** nêu quy tắc; **33. trường hợp (case / 사례) study K — Upload thành công nhưng Save thất bại (fail / 실패)** thử quy tắc trong tình huống, rồi **34. trường hợp (case / 사례) study L — Excel import “thành công” nhưng dữ liệu sai cột** mở rộng hệ quả.

## 33. trường hợp (case / 사례) study K — Upload thành công nhưng Save thất bại (fail / 실패)

Người dùng (user / 사용자) upload ba attachment, sau đó Save đặc tả hợp đồng (contract / 계약) bị optimistic khóa (lock / 잠금) xung đột (conflict / 충돌). lưu trữ (storage / 저장소) đã có tệp (file / 파일) nhưng đặc tả hợp đồng (contract / 계약) giao dịch (transaction / 트랜잭션) quay lui (rollback / 롤백).

Nếu hệ thống không có staging/cleanup, ba tệp (file / 파일) trở thành orphan.

Lập luận (reasoning / 추론):

```text
file transfer success ≠ business commit success
```

Fix kiến trúc (architecture / 아키텍처) có thể là upload session/staging + promote sau lần ghi nhận (commit / 커밋) hoặc compensating cleanup có expiry. Regression kiểm thử (test / 테스트) phải kiểm tra lưu trữ (storage / 저장소)/siêu dữ liệu (metadata / 메타데이터) sau failed Save, không chỉ UI message.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **33. trường hợp (case / 사례) study K — Upload thành công nhưng Save thất bại (fail / 실패)** nêu quy tắc; **34. trường hợp (case / 사례) study L — Excel import “thành công” nhưng dữ liệu sai cột** thử quy tắc trong tình huống, rồi **35. trường hợp (case / 사례) study M — Hybrid eKYC callback về sau khi người dùng (user / 사용자) đóng screen** mở rộng hệ quả.

## 34. trường hợp (case / 사례) study L — Excel import “thành công” nhưng dữ liệu sai cột

Người dùng (user / 사용자) thêm một column ở đầu template. Import mã (code / 코드) map theo chỉ mục (index / 인덱스) nên `CUSTOMER_NAME` nhận giá trị của column khác. Parser không throw exception.

Đây là silent ngữ nghĩa (semantic / 의미적) corruption, nguy hiểm hơn parse thất bại (failure / 실패).

Fix:

```text
version/header validation
→ explicit column mapping
→ type conversion
→ business validation
→ preview/error report
→ commit
```

Kiểm thử (test / 테스트) phải bao gồm reordered/missing/extra header, không chỉ happy template.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **34. trường hợp (case / 사례) study L — Excel import “thành công” nhưng dữ liệu sai cột** nêu quy tắc; **35. trường hợp (case / 사례) study M — Hybrid eKYC callback về sau khi người dùng (user / 사용자) đóng screen** thử quy tắc trong tình huống, rồi **36. trường hợp (case / 사례) study N — Web deploy mới phá app bản địa (native / 네이티브) cũ** mở rộng hệ quả.

## 35. trường hợp (case / 사례) study M — Hybrid eKYC callback về sau khi người dùng (user / 사용자) đóng screen

Page A start camera với `nativeRequestId=R1`. người dùng (user / 사용자) chuyển screen. bản địa (native / 네이티브) SDK hoàn tất và callback R1.

Nếu cầu nối (bridge / 브리지) gateway gọi trực tiếp `scwin.onSuccess`, stale phạm vi (scope / 범위) có thể không còn hoặc callback cập nhật (update / 업데이트) nhầm screen instance mới.

Fix ranh giới (boundary / 경계):

```text
native callback
→ gateway
→ resolve request owner/session
→ owner còn valid?
   ├─ yes → deliver result
   └─ no  → persist/ignore theo workflow contract
```

Đây là stale Submission bài toán (problem / 문제) mở rộng qua bản địa (native / 네이티브) ranh giới (boundary / 경계).

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **35. trường hợp (case / 사례) study M — Hybrid eKYC callback về sau khi người dùng (user / 사용자) đóng screen** nêu quy tắc; **36. trường hợp (case / 사례) study N — Web deploy mới phá app bản địa (native / 네이티브) cũ** thử quy tắc trong tình huống, rồi **37. trường hợp (case / 사례) study O — môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) không reproduce được vì thiếu bản dựng (build / 빌드) định danh (identity / 식별자)** mở rộng hệ quả.

## 36. trường hợp (case / 사례) study N — Web deploy mới phá app bản địa (native / 네이티브) cũ

Web bản dựng (build / 빌드) mới gọi plugin API V2 nhưng nhiều người dùng (user / 사용자) chưa cập nhật (update / 업데이트) app và chỉ có V1.

Nguồn (source / 소스) web đúng, backend đúng, trình duyệt (browser / 브라우저) desktop đúng, chỉ hybrid app cũ thất bại (fail / 실패).

Nguyên nhân gốc (root cause / 근본 원인) là bản phát hành (release / 릴리스) đồ thị (graph / 그래프) không chứa tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬).

Fix kiến trúc (architecture / 아키텍처):

```text
capability/version handshake
→ compatible adapter path
→ minimum supported app policy
→ telemetry appVersion + webBuildId
```

Web và bản địa (native / 네이티브) bản phát hành (release / 릴리스) cadence phải được coi là phân tán (distributed / 분산) triển khai (deployment / 배포).

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **36. trường hợp (case / 사례) study N — Web deploy mới phá app bản địa (native / 네이티브) cũ** nêu quy tắc; **37. trường hợp (case / 사례) study O — môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) không reproduce được vì thiếu bản dựng (build / 빌드) định danh (identity / 식별자)** thử quy tắc trong tình huống, rồi **38. Master thiết kế (design / 설계) rà soát (review / 검토) cho tệp (file / 파일)/hybrid/khả năng quan sát (observability / 관측 가능성)** mở rộng hệ quả.

## 37. trường hợp (case / 사례) study O — môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) không reproduce được vì thiếu bản dựng (build / 빌드) định danh (identity / 식별자)

Người dùng (user / 사용자) báo Save treo. nhóm (team / 팀) kiểm tra nguồn (source / 소스) mới nhất và không thấy bug. Sau đó mới phát hiện trình duyệt (browser / 브라우저) đang dùng W-Pack sản phẩm tạo ra (artifact / 산출물) cũ từ bộ nhớ đệm (cache / 캐시) nút (node / 노드) khác.

Nguyên nhân gốc (root cause / 근본 원인) không phải chỉ bộ nhớ đệm (cache / 캐시); nguyên nhân gốc (root cause / 근본 원인) operational là bằng chứng (evidence / 증거) không ghi sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자).

Sau sự cố (incident / 인시던트) cần thêm:

```text
build ID visible trong diagnostics
resource version/cache policy
correlation ID
release dashboard
runbook kiểm tra artifact trước source
```

Một fix tốt thay đổi khả năng phát hiện lần sau, không chỉ xóa bộ nhớ đệm (cache / 캐시) một lần.

> **Nối mạch:** Trong **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **37. trường hợp (case / 사례) study O — môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) không reproduce được vì thiếu bản dựng (build / 빌드) định danh (identity / 식별자)** nêu quy tắc; **38. Master thiết kế (design / 설계) rà soát (review / 검토) cho tệp (file / 파일)/hybrid/khả năng quan sát (observability / 관측 가능성)** thử quy tắc trong tình huống, rồi **39. Master capstone mở rộng** mở rộng hệ quả.

## 38. Master thiết kế (design / 설계) rà soát (review / 검토) cho tệp (file / 파일)/hybrid/khả năng quan sát (observability / 관측 가능성)

Khi PR thêm upload/export/bản địa (native / 네이티브) năng lực (capability / 역량), rà soát (review / 검토) thêm các câu:

```text
File content, metadata và business row có cùng transaction không?
Orphan cleanup ở đâu?
Filename/path có được tin từ client không?
Large export chạy client hay server và vì sao?
Native callback có request identity không?
Page đóng/background thì operation ra sao?
Web build có compatible với app cũ không?
Bridge expose capability tối thiểu chưa?
Sensitive data có đi qua log/JS global không?
Nếu incident xảy ra, request/build/file/native identity nào giúp trace?
```

Đây là những câu hỏi kiến trúc (architecture / 아키텍처), không phải khung phần mềm (framework / 프레임워크) trivia.

> **Nối mạch:** Ở chặng này của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **39. Master capstone mở rộng** nối từ **38. Master thiết kế (design / 설계) rà soát (review / 검토) cho tệp (file / 파일)/hybrid/khả năng quan sát (observability / 관측 가능성)** sang **40. Master definition sau khi mở rộng đến chapter 19**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Master capstone mở rộng

Mở rộng mini enterprise app ở section 27 bằng ba năng lực (capability / 역량).

Thứ nhất, thêm attachment staging cho Employee Detail. Upload trước Save, thất bại (fail / 실패) Save bằng phiên bản (version / 버전) xung đột (conflict / 충돌) và chứng minh orphan cleanup đúng.

Thứ hai, thêm Excel import cho Employee tìm kiếm (search / 검색). tệp (file / 파일) phải qua header/lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증), preview invalid rows và chỉ lần ghi nhận (commit / 커밋) khi người dùng (user / 사용자) xác nhận.

Thứ ba, giả lập hybrid định danh (identity / 식별자) xác minh (verification / 확인). Fake bản địa (native / 네이티브) cầu nối (bridge / 브리지) trả callback chậm, callback sau page close, permission denied và app-version mismatch.

Cuối cùng thêm khả năng quan sát (observability / 관측 가능성):

```text
screenInstanceKey
requestId
uploadSessionId
nativeRequestId
webBuildId
engineBuild
elapsed stage timings
```

Tạo ba runbook và fault-inject để người khác có thể điều tra mà không đọc nguồn (source / 소스) trước.

Nếu capstone chỉ chạy happy đường dẫn (path / 경로) thì chưa phải Master.

> **Nối mạch:** Đặt trong câu hỏi lớn của **16 — Master môi trường vận hành (production / 운영 환경) Playbook & End-to-End trường hợp (case / 사례) Studies**, **40. Master definition sau khi mở rộng đến chapter 19** nối từ **39. Master capstone mở rộng** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 40. Master definition sau khi mở rộng đến chapter 19

Một WebSquare engineer ở mức Master không được định nghĩa bởi số API nhớ được. Người đó có thể:

```text
mô hình hóa state và owner;
phân biệt identity theo lifetime;
thiết kế page/data/server/file/native contract;
reason async ordering và transaction ambiguity;
đo performance thay vì đoán;
coi browser/native client là untrusted;
thiết kế compatibility giữa engine/web/native/backend;
truy vết incident bằng correlation và artifact identity;
biến incident thành regression guard/runbook;
đọc official API/release note đúng build khi exact behavior cần xác minh.
```

Từ đây, chapter mới chỉ nên được thêm nếu nó mở một ranh giới (boundary / 경계) hoặc mô hình tư duy (mental model / 사고 모델) chưa được thư viện (library / 라이브러리) giải thích. Danh sách API dài, workaround riêng của một dự án (project / 프로젝트) hoặc bản sao (copy / 복사) nguyên tham chiếu (reference / 참조) không làm tăng mastery.

> **Bàn giao:** Sau **40. Master definition sau khi mở rộng đến chapter 19**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
