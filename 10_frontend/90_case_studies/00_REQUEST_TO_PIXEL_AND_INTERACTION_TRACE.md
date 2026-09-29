# Yêu cầu (request / 요청) → Điểm ảnh (pixel / 픽셀) → Tương tác (interaction / 상호작용) Dấu vết (trace / 추적) — một màn hình web thực sự chạy như thế nào?

Một lỗi frontend thường được mô tả bằng câu rất ngắn: “page tải (load / 로드) chậm”, “React kết xuất (render / 렌더링) sai”, “CSS bị lag”, “API trả rồi nhưng màn hình chưa cập nhật (update / 업데이트)”, hoặc “môi trường vận hành (production / 운영 환경) khác cục bộ (local / 로컬)”. Các câu này mô tả **triệu chứng**, chưa mô tả cơ chế.

Trường hợp (case / 사례) này lấy một màn hình giả định đủ quen thuộc để nối toàn bộ lĩnh vực (domain / 도메인):

```text
/users
```

Màn hình có:

- header và điều hướng (navigation / 내비게이션);
- biểu định kiểu (stylesheet / 스타일시트) chính;
- JavaScript bundle;
- danh sách người dùng (user / 사용자) tải từ `/api/users`;
- ô filter;
- nút mở modal detail;
- avatar ảnh (image / 이미지);
- loading trạng thái (state / 상태) và lỗi (error / 오류) trạng thái (state / 상태).

Không quan trọng app viết bằng vanilla JavaScript, React hay WebSquare. Mục tiêu là truy được cùng một chuỗi nguyên lý nền tảng (first principles / 제일 원리):

```text
URL
→ request
→ response bytes
→ parser
→ DOM / CSSOM
→ style
→ layout
→ paint
→ composite
→ event
→ JavaScript scheduling
→ state transition
→ network request
→ stale/cancel/error handling
→ next render
→ deployed artifact evidence
```

Trường hợp (case / 사례) này không thay các chapter HTML, CSS hay JavaScript. Nó kiểm tra xem các chapter đó có nối thành một mô hình tư duy (mental model / 사고 모델) hay chưa.

---

# 1. Bắt đầu bằng câu hỏi đúng: trình duyệt (browser / 브라우저) đang chạy cái gì?

Giả sử người dùng nhập:

```text
https://example.com/users
```

Sai lầm phổ biến là bắt đầu lập luận (reasoning / 추론) ngay từ thành phần (component / 컴포넌트) `UsersPage`.

Nhưng thành phần (component / 컴포넌트) chưa tồn tại ở thời điểm trình duyệt (browser / 브라우저) bắt đầu điều hướng (navigation / 내비게이션).

Câu hỏi đầu tiên phải là:

```text
Browser nhận URL nào?
URL đó resolve tới origin nào?
Document request nào được gửi?
Response nào tạo ra document hiện tại?
Artifact nào browser thực sự tải?
```

Điều này đặc biệt quan trọng khi môi trường vận hành (production / 운영 환경) dùng CDN, reverse proxy, dịch vụ (service / 서비스) worker, bộ nhớ đệm (cache / 캐시) hoặc frontend bản dựng (build / 빌드) có hashed filename.

Nguồn (source / 소스) tệp (file / 파일) trong Git không phải thứ trình duyệt (browser / 브라우저) chạy trực tiếp.

Ta cần tách:

```text
Source code
→ build graph
→ generated artifact
→ deployed artifact
→ cached artifact
→ resource browser actually executes
```

Nếu không tách được năm lớp này, câu “mã (code / 코드) đã deploy rồi” chưa phải bằng chứng (evidence / 증거).

---

# 2. Điều hướng (navigation / 내비게이션) không giống `fetch`

Document điều hướng (navigation / 내비게이션) tới `/users` và JavaScript gọi:

```js
fetch('/api/users')
```

đều dùng mạng (network / 네트워크), nhưng ngữ nghĩa (semantic / 의미적) khác nhau.

Điều hướng (navigation / 내비게이션) có thể tạo hoặc thay document. Nó kích hoạt document loading, parsing và vòng đời (lifecycle / 생명주기) liên quan page.

`fetch()` chỉ là một yêu cầu (request / 요청) do script khởi tạo trong document hiện tại. Nó không tự tạo DOM mới, không tự kết xuất (render / 렌더링) dữ liệu và không tự thay trạng thái (state / 상태) của khung phần mềm (framework / 프레임워크).

Mô hình tư duy (mental model / 사고 모델):

```text
Navigation response
→ bytes that can become a Document

API response
→ bytes/data delivered to JavaScript
→ application decides what state changes
→ rendering may happen afterward
```

Đây là lý do “API đã trả 200” không đồng nghĩa “UI phải hiện ngay”. Giữa phản hồi (response / 응답) và điểm ảnh (pixel / 픽셀) còn nhiều bước.

---

# 3. Document phản hồi (response / 응답): status mã (code / 코드) chưa đủ

Giả sử document yêu cầu (request / 요청) trả `200 OK`.

Ta vẫn phải hỏi:

```text
Content-Type là gì?
encoding là gì?
cache policy là gì?
CSP/security headers là gì?
HTML body thực tế là version nào?
```

Một status `200` chỉ nói yêu cầu (request / 요청) thành công theo HTTP đặc tả hợp đồng (contract / 계약) ở một mức nào đó. Nó không chứng minh:

- phản hồi (response / 응답) là sản phẩm tạo ra (artifact / 산출물) đúng phiên bản (version / 버전);
- HTML tham chiếu bundle đúng;
- CDN không trả tệp (file / 파일) cũ;
- script không bị CSP chặn;
- biểu định kiểu (stylesheet / 스타일시트) không 404;
- hydration/thời gian chạy (runtime / 런타임) không thất bại (fail / 실패) sau đó.

Gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경) vì vậy phải dấu vết (trace / 추적) **tài nguyên (resource / 자원) đồ thị (graph / 그래프)**, không dừng ở document yêu cầu (request / 요청).

---

# 4. Trình duyệt (browser / 브라우저) nhận bytes, không nhận DOM

Máy chủ (server / 서버) gửi HTML văn bản (text / 텍스트)/bytes. DOM chưa tồn tại sẵn trong phản hồi (response / 응답).

Ví dụ phản hồi (response / 응답):

```html
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="/assets/app.abc123.css">
    <script type="module" src="/assets/app.def456.js"></script>
  </head>
  <body>
    <main id="app"></main>
  </body>
</html>
```

Trình duyệt (browser / 브라우저) phải parse nguồn (source / 소스) này thành cây (tree / 트리).

Mô hình tư duy (mental model / 사고 모델):

```text
HTML source
≠ DOM tree
```

Parser có rules riêng, có thể repair markup, insert implied nodes hoặc xử lý các content chế độ (mode / 모드) khác nhau.

Vì vậy khi DOM nhìn khác nguồn (source / 소스), đừng lập tức kết luận khung phần mềm (framework / 프레임워크) sửa HTML. Có thể chính HTML parser đã tạo cây (tree / 트리) khác nguồn (source / 소스) văn bản (text / 텍스트).

---

# 5. Parser gặp tài nguyên (resource / 자원): loading và parsing bắt đầu đan xen

Trong khi parse HTML, trình duyệt (browser / 브라우저) phát hiện tài nguyên (resource / 자원) như biểu định kiểu (stylesheet / 스타일시트), script, ảnh (image / 이미지), font.

Document loading không phải:

```text
download full HTML
→ parse all HTML
→ download CSS
→ download JS
→ render
```

Nhiều việc overlap.

Một mental timeline đơn giản hơn:

```text
HTML bytes arrive
→ parser advances
→ discover CSS / JS / image
→ initiate dependent requests
→ continue or pause according to resource semantics
```

Chi tiết blocking phụ thuộc tài nguyên (resource / 자원) kiểu (type / 타입) và cách khai báo, nên không nên học một quy tắc (rule / 규칙) đơn giản kiểu “mọi script khối (block / 블록) parser”.

Điểm cần giữ là **tài nguyên (resource / 자원) discovery thời gian (time / 시간) ảnh hưởng đường găng (critical path / 임계 경로)**.

Nếu một biểu định kiểu (stylesheet / 스타일시트) quan trọng chỉ được phát hiện sau khi JavaScript chạy rồi inject link, trình duyệt (browser / 브라우저) không thể tải nó trước khi có discovery đó.

---

# 6. DOM và CSSOM là hai cấu trúc khác nhau

HTML tạo DOM.

CSS được parse thành cấu trúc quy tắc (rule / 규칙)/style thông tin (information / 정보) thường được lập luận (reasoning / 추론) dưới mô hình tư duy (mental model / 사고 모델) CSSOM.

Ta có thể hình dung:

```text
DOM
+
CSS rules / cascade inputs
→ computed style
```

Nhưng đừng biến nó thành công thức quá cơ học. Style resolution còn phụ thuộc:

- origin;
- cascade tầng (layer / 계층);
- importance;
- specificity;
- phạm vi (scope / 범위)/proximity;
- inheritance;
- nguồn (source / 소스) thứ tự (order / 순서);
- môi trường (environment / 환경) như viewport/media/bộ chứa (container / 컨테이너) trạng thái (state / 상태).

Do đó lỗi “CSS lớp (class / 클래스) có trong DOM nhưng không có style mong muốn” là câu hỏi cascade trước khi là câu hỏi khung phần mềm (framework / 프레임워크).

---

# 7. Style không phải bố cục (layout / 레이아웃)

Sau khi trình duyệt (browser / 브라우저) biết style liên quan, nó còn phải xác định hình học (geometry / 기하학).

Ví dụ:

```css
.user-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

CSS declaration không chứa trực tiếp điểm ảnh (pixel / 픽셀) position cuối của từng card.

Bố cục (layout / 레이아웃) phải giải quyết ràng buộc (constraint / 제약조건) từ:

- available kích thước (size / 크기);
- intrinsic kích thước (size / 크기);
- ngữ cảnh định dạng (formatting context / 서식 컨텍스트);
- font metrics;
- content;
- replaced elements;
- min/max các ràng buộc (constraints / 제약조건들);
- scrollbars;
- viewport/bộ chứa (container / 컨테이너) kích thước (size / 크기).

Vì vậy:

```text
computed style
≠ final geometry
```

Một ảnh (image / 이미지) tải (load / 로드) muộn có thể thay intrinsic kích thước (size / 크기) và kéo theo bố cục (layout / 레이아웃) mới nếu dimension không được reserve.

Một web font tải (load / 로드) cũng có thể thay văn bản (text / 텍스트) metrics và hình học (geometry / 기하학).

---

# 8. Bố cục (layout / 레이아웃) không phải paint

Biết một box ở đâu chưa có nghĩa điểm ảnh (pixel / 픽셀) đã xuất hiện trên màn hình.

Bố cục (layout / 레이아웃) trả lời gần với:

```text
box nào ở đâu, kích thước bao nhiêu?
```

Paint trả lời gần với:

```text
box/text/border/background/shadow nào cần được vẽ theo thứ tự nào?
```

Compositing lại liên quan cách các painted results/layers được kết hợp để tạo frame cuối.

Đừng học chuỗi xử lý (pipeline / 파이프라인) như ba API công khai (public / 공개) mà trình duyệt (browser / 브라우저) bắt buộc implement y hệt nhau. Đây là mô hình tư duy (mental model / 사고 모델) để lập luận (reasoning / 추론) hiệu năng (performance / 성능).

Điều quan trọng:

```text
style work
layout work
paint work
composite work
```

không có cùng chi phí (cost / 비용) và không bị invalidate bởi cùng loại thay đổi.

---

# 9. “Transform chạy trên GPU” không phải kết luận hiệu năng (performance / 성능)

Một câu rất hay gặp:

> Dùng `transform` nhanh vì GPU.

Đây là shortcut nguy hiểm.

Ngay cả khi một animation có thể tránh bố cục (layout / 레이아웃)/paint trong một hiện thực (implementation / 구현) cụ thể, tổng hiệu năng (performance / 성능) còn phụ thuộc:

- tầng (layer / 계층) creation/promotion;
- texture bộ nhớ (memory / 메모리);
- rasterization;
- upload/composite chi phí (cost / 비용);
- kích thước (size / 크기) của tầng (layer / 계층);
- số lượng tầng (layer / 계층);
- main-thread scripting;
- concurrent công việc (work / 작업) khác;
- thiết bị (device / 장치)/trình duyệt (browser / 브라우저)/thời gian chạy (runtime / 런타임) trạng thái (state / 상태).

Do đó môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) phải là:

```text
Hypothesis
→ record trace
→ identify actual work
→ change one variable
→ record again
```

chứ không phải:

```text
CSS property name
→ assume cost
```

Lab kế tiếp sẽ biến nguyên tắc này thành workflow đo.

---

# 10. JavaScript bundle tải xong chưa có nghĩa app sẵn sàng

Giả sử `/assets/app.def456.js` download xong.

Trình duyệt (browser / 브라우저) vẫn có thể cần:

- parse JavaScript;
- compile/prepare thực thi (execution / 실행);
- resolve/import mô-đun (module / 모듈) đồ thị (graph / 그래프);
- execute initialization;
- register listeners;
- create ứng dụng (application / 애플리케이션) trạng thái (state / 상태);
- mount/hydrate khung phần mềm (framework / 프레임워크) cây (tree / 트리);
- schedule additional công việc (work / 작업).

Vì vậy mạng (network / 네트워크) waterfall chỉ là một lớp của startup.

Nếu bundle download nhanh nhưng main luồng thực thi (thread / 스레드) bận execute vài trăm millisecond, người dùng (user / 사용자) vẫn có thể cảm thấy app chưa interactive.

Ta cần phân biệt:

```text
Resource download time
vs
Main-thread execution time
vs
Rendering work
vs
Interaction latency
```

---

# 11. Initial ứng dụng (application / 애플리케이션) trạng thái (state / 상태) có đơn vị sở hữu (owner / 오너)

Giả sử thời gian chạy (runtime / 런타임) tạo trạng thái (state / 상태):

```js
{
  users: [],
  loading: true,
  error: null,
  filter: '',
  selectedUserId: null
}
```

Không nên chỉ hỏi trạng thái (state / 상태) “nằm trong React hay store nào”.

Hỏi sâu hơn:

```text
Ai sở hữu state này?
Lifetime bằng document, page, component hay request?
State nào canonical?
State nào derived?
State nào chỉ là UI affordance?
```

Ví dụ filtered danh sách (list / 목록) nên thường là derived từ:

```text
users + filter
```

Nếu app lưu riêng cả `users`, `filter`, `filteredUsers`, ta đã tạo khả năng hai nguồn dữ liệu lệch nhau.

Quy tắc (rule / 규칙) tổng quát:

```text
Derived state không nên trở thành source of truth mới nếu có thể tính đáng tin từ canonical state.
```

---

# 12. API yêu cầu (request / 요청) bắt đầu: cần gắn định danh (identity / 식별자) cho thao tác (operation / 연산)

App gọi `/api/users`.

Naive mô hình (model / 모델):

```text
request
→ response
→ setUsers(response)
```

Môi trường vận hành (production / 운영 환경) mô hình (model / 모델) phải nghĩ thêm:

```text
operation identity
owner
lifetime
cancellation
stale-result policy
error policy
retry policy
```

Ví dụ người dùng (user / 사용자) đổi filter không nhất thiết cần yêu cầu (request / 요청) mới nếu filter client-side. Nhưng nếu tìm kiếm (search / 검색) server-side:

```text
query=a
→ request A
query=ab
→ request B
```

Nếu B trả trước A:

```text
B response
→ UI shows "ab"
A response arrives later
→ naive code overwrites with stale "a"
```

Đây không phải mạng (network / 네트워크) bug. Đây là **thứ tự (ordering / 순서) + quyền sở hữu (ownership / 소유권) bug**.

Bất biến (invariant / 불변식) cần là:

```text
Only result belonging to current intent may update current state.
```

Hiện thực (implementation / 구현) có thể dùng abort/cancellation, yêu cầu (request / 요청) ID, chuỗi (sequence / 시퀀스) number hoặc thư viện (library / 라이브러리) lớp trừu tượng (abstraction / 추상화). Nhưng bất biến (invariant / 불변식) mới là kiến thức chuẩn gốc (canonical / 정본).

---

# 13. Promise completion không đồng nghĩa điểm ảnh (pixel / 픽셀) cập nhật ngay lập tức

Giả sử phản hồi (response / 응답) về và Promise continuation chạy:

```js
state.users = data
state.loading = false
```

Người mới dễ nghĩ:

```text
set state
→ pixel đổi tức thì
```

Thực tế trạng thái (state / 상태) mutation/cập nhật (update / 업데이트) có thể làm khung phần mềm (framework / 프레임워크) schedule rendering công việc (work / 작업). Trình duyệt (browser / 브라우저) còn phải đi qua phần cần thiết của style/bố cục (layout / 레이아웃)/paint/composite trước khi frame mới xuất hiện.

Tùy khung phần mềm (framework / 프레임워크) và scheduling mô hình (model / 모델), nhiều trạng thái (state / 상태) cập nhật (update / 업데이트) có thể được batch hoặc deferred.

Mô hình tư duy (mental model / 사고 모델) nên là:

```text
Data becomes available
→ application state transition
→ rendering work becomes eligible/scheduled
→ DOM/style consequences
→ browser rendering work
→ frame presented
```

Không nên gỡ lỗi (debug / 디버그) timing bằng cách chỉ thêm `setTimeout(..., 0)` cho tới khi “hết lỗi”.

---

# 14. Vòng lặp sự kiện (event loop / 이벤트 루프): phải dấu vết (trace / 추적) thứ tự (ordering / 순서), không học slogan

Giả sử người dùng (user / 사용자) gõ vào filter đầu vào (input / 입력).

Có thể có:

```text
input event
→ handler
→ state update
→ Promise/microtask continuation
→ framework scheduling
→ render opportunity
→ paint
```

Nhưng timeline thực tế còn phụ thuộc công việc (work / 작업) đang chờ, khung phần mềm (framework / 프레임워크), trình duyệt (browser / 브라우저) và mã (code / 코드).

Điều cần học là cách hỏi:

```text
Callback nào đang chạy?
Nó được enqueue từ đâu?
Có microtask nào tiếp tục trước khi browser có cơ hội render?
Có long task nào đang giữ main thread không?
```

Một microtask chuỗi (chain / 사슬) quá dài có thể trì hoãn rendering dù mỗi Promise callback riêng lẻ nhìn nhỏ.

Do đó `async` không đồng nghĩa “không khối (block / 블록) UI”. JavaScript continuation vẫn có thể chạy trên main luồng thực thi (thread / 스레드) và tiêu tốn ngân sách (budget / 예산).

---

# 15. Filter 10.000 rows: bottleneck nằm ở đâu?

Giả sử filter danh sách (list / 목록) gồm 10.000 người dùng (user / 사용자).

Triệu chứng: gõ một ký tự bị lag.

Có ít nhất bốn họ nguyên nhân khác nhau:

```text
A. computation
filter/sort quá nặng

B. framework reconciliation/render
quá nhiều component work

C. DOM mutation + style/layout
quá nhiều node hoặc geometry invalidation

D. paint/composite
visual effect/layer/raster cost lớn
```

Không thể nhìn lag rồi kết luận ngay “React kết xuất (render / 렌더링) quá nhiều”.

Quy trình đúng:

```text
record interaction
→ find long work
→ split scripting vs rendering
→ inspect call stack / invalidation
→ count affected nodes/work
→ form hypothesis
```

Nếu computation chiếm 80 ms nhưng bố cục (layout / 레이아웃) chỉ 2 ms, CSS không phải mục tiêu (target / 대상) đầu tiên.

Nếu JavaScript chỉ 4 ms nhưng bố cục (layout / 레이아웃) 70 ms trên hàng nghìn nút (node / 노드), memoization thành phần (component / 컴포넌트) không giải quyết cốt lõi (core / 핵심) bài toán (problem / 문제).

---

# 16. DOM kích thước (size / 크기) là multiplier chứ không phải tội lỗi tuyệt đối

“DOM lớn chậm” là một heuristic, không phải định luật đủ để gỡ lỗi (debug / 디버그).

DOM lớn có thể tăng chi phí (cost / 비용) cho:

- selector/style calculation;
- bố cục (layout / 레이아웃);
- cây khả năng tiếp cận (accessibility tree / 접근성 트리);
- bộ nhớ (memory / 메모리);
- sự kiện (event / 이벤트)/listener kiến trúc (architecture / 아키텍처);
- mutation/cập nhật (update / 업데이트) phạm vi (scope / 범위).

Nhưng chi phí (cost / 비용) thực tế còn phụ thuộc cấu trúc (structure / 구조) và thao tác (operation / 연산).

Virtualization có giá trị khi UI chỉ cần kết xuất (render / 렌더링) subset visible, nhưng virtualization cũng tạo độ phức tạp (complexity / 복잡도):

- scroll đo lường (measurement / 측정);
- focus/khả năng tiếp cận (accessibility / 접근성);
- động (dynamic / 동적) row height;
- selection;
- keyboard điều hướng (navigation / 내비게이션);
- trạng thái (state / 상태) preservation.

Tối ưu hóa (optimization / 최적화) phải gắn với bottleneck thật, không phải checklist trend.

---

# 17. Modal: visual tầng (layer / 계층) và tương tác (interaction / 상호작용) tầng (layer / 계층) phải thống nhất

Người dùng (user / 사용자) bấm một card và mở detail modal.

Nếu chỉ nhìn điểm ảnh (pixel / 픽셀), modal có thể “đúng”. Nhưng công khai (public / 공개) hành vi (behavior / 동작) còn gồm:

- focus chuyển vào modal hợp lý;
- background không nhận tương tác (interaction / 상호작용) ngoài ý muốn;
- keyboard điều hướng (navigation / 내비게이션);
- accessible name/role;
- Escape/close hành vi (behavior / 동작);
- focus restoration sau close;
- scroll hành vi (behavior / 동작);
- portal/tầng (layer / 계층) quyền sở hữu (ownership / 소유권);
- async detail yêu cầu (request / 요청) cancellation nếu modal đóng sớm.

Đây là ví dụ vì sao khả năng tiếp cận (accessibility / 접근성) không phải phần trang trí cuối chuỗi xử lý (pipeline / 파이프라인).

Ngữ nghĩa (semantics / 의미론) và focus là tính đúng đắn (correctness / 정확성) của tương tác (interaction / 상호작용) mô hình (model / 모델).

---

# 18. Portal không phá DOM rules

React portal hoặc khung phần mềm (framework / 프레임워크) popup lớp trừu tượng (abstraction / 추상화) có thể kết xuất (render / 렌더링) nút (node / 노드) ra vị trí DOM khác logical thành phần (component / 컴포넌트) parent.

Điều này tạo hai cây (tree / 트리) cần phân biệt:

```text
Logical application/component tree
vs
Physical DOM tree
```

Sự kiện (event / 이벤트), CSS inheritance, ngữ cảnh xếp chồng (stacking context / 쌓임 맥락), focus và khả năng tiếp cận (accessibility / 접근성) có thể phụ thuộc cây (tree / 트리)/ranh giới (boundary / 경계) khác nhau.

Khi gỡ lỗi (debug / 디버그) modal, phải biết mình đang lập luận (reasoning / 추론) cây (tree / 트리) nào.

Nói “modal là child của UsersPage” có thể đúng trong thành phần (component / 컴포넌트) mô hình (model / 모델) nhưng sai nếu dùng để suy luận CSS khối chứa tham chiếu (containing block / 컨테이닝 블록) hoặc DOM ancestry.

---

# 19. Ngữ cảnh xếp chồng (stacking context / 쌓임 맥락): `z-index: 999999` không phải universal fix

Modal nằm sau header.

Naive fix:

```css
z-index: 999999;
```

Nhưng `z-index` được interpret trong ngữ cảnh xếp chồng (stacking context / 쌓임 맥락). Nếu ancestor tạo ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) khác, tăng số trong ngữ cảnh (context / 맥락) con không nhất thiết vượt sibling ngữ cảnh (context / 맥락) bên ngoài.

Gỡ lỗi (debug / 디버그) phải hỏi:

```text
Node nào tạo stacking context?
Modal physical DOM nằm ở đâu?
Containing/stacking ancestry là gì?
```

Đây là ví dụ điển hình của việc khung phần mềm (framework / 프레임워크) cây (tree / 트리) không thay CSS rendering rules.

---

# 20. Ảnh (image / 이미지) loading và bố cục (layout / 레이아웃) stability

Avatar xuất hiện sau.

Nếu ảnh (image / 이미지) không reserve không gian (space / 공간), tải (load / 로드) hoàn tất có thể đổi bố cục (layout / 레이아웃).

Nếu người dùng (user / 사용자) chuẩn bị click nút nhưng content dịch chuyển, đây không chỉ là “visual annoyance”; nó thay tương tác (interaction / 상호작용) mục tiêu (target / 대상) position.

Mô hình tư duy (mental model / 사고 모델):

```text
resource timing
→ intrinsic size becomes known
→ geometry may invalidate
→ new layout
→ repaint/composite as needed
```

Giải pháp tốt thường bắt đầu từ đặc tả hợp đồng (contract / 계약) kích thước/aspect ratio, không phải JavaScript đo rồi sửa sau mỗi tải (load / 로드) nếu không cần.

---

# 21. Font là tài nguyên (resource / 자원) có thể thay hình học (geometry / 기하학)

Font tải (load / 로드) không chỉ đổi “style chữ”.

Font metrics có thể đổi:

- line break;
- line height;
- element width/height;
- downstream bố cục (layout / 레이아웃).

Vì vậy font chiến lược (strategy / 전략) là giao điểm giữa mạng (network / 네트워크), typography, bố cục (layout / 레이아웃) và visual stability.

Nếu môi trường vận hành (production / 운영 환경) font CDN chậm còn cục bộ (local / 로컬) dùng installed font, bố cục (layout / 레이아웃) bug có thể chỉ xuất hiện môi trường vận hành (production / 운영 환경) dù CSS nguồn (source / 소스) giống nhau.

---

# 22. API lỗi (error / 오류): lỗi (error / 오류) trạng thái (state / 상태) không phải `console.error`

Giả sử `/api/users` trả 500.

Đặc tả ứng dụng (application contract / 애플리케이션 계약) cần quyết định:

```text
loading kết thúc khi nào?
error nào public cho user?
retry có safe không?
partial data có giữ không?
telemetry ghi gì?
request ID/correlation nào giúp backend trace?
```

`console.error(error)` không phải lỗi (error / 오류) handling hoàn chỉnh.

Frontend cũng không nên tự suy rằng thử lại (retry / 재시도) mọi yêu cầu (request / 요청) là tốt. Một GET idempotent có đặc tính khác mutation có side tác động (effect / 효과).

Ranh giới (boundary / 경계) với Backend phải giữ ngữ nghĩa (semantic / 의미적) của thao tác (operation / 연산).

---

# 23. `401` và `403`: UI không phải authorization engine

Nếu API trả auth lỗi (error / 오류), frontend có thể:

- redirect login;
- refresh session theo đặc tả hợp đồng (contract / 계약);
- hide/disable năng lực (capability / 역량);
- hiển thị message.

Nhưng frontend không quyết định bảo mật (security / 보안) truth cuối cùng.

Quy tắc (rule / 규칙):

```text
UI capability hint
≠ server authorization
```

Button bị ẩn không bảo vệ API.

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) giúp UX và giảm yêu cầu (request / 요청) sai, nhưng không thay server-side authorization/kiểm tra hợp lệ (validation / 검증).

---

# 24. CORS bug không phải “backend API chết”

Nếu trình duyệt (browser / 브라우저) chặn cross-origin truy cập (access / 접근), có thể máy chủ (server / 서버) thực tế vẫn trả phản hồi (response / 응답) ở mạng (network / 네트워크) mức (level / 수준).

CORS là trình duyệt (browser / 브라우저) bảo mật (security / 보안) chính sách (policy / 정책) quanh việc script có được đọc/use phản hồi (response / 응답) cross-origin theo đặc tả hợp đồng (contract / 계약) hay không.

Gỡ lỗi (debug / 디버그) cần phân biệt:

```text
DNS/connect failure
HTTP failure
CORS policy failure
application parsing failure
state/render failure
```

Gộp tất cả thành “API lỗi” làm mất ranh giới (boundary / 경계).

---

# 25. Bộ nhớ đệm (cache / 캐시): phiên bản (version / 버전) cũ có thể tồn tại đúng theo chính sách (policy / 정책)

Môi trường vận hành (production / 운영 환경) bug:

> Tôi đã deploy JS mới nhưng người dùng (user / 사용자) vẫn chạy mã (code / 코드) cũ.

Đừng bắt đầu bằng “clear bộ nhớ đệm (cache / 캐시) thử”. Trước hết cần biết caching mô hình (model / 모델):

```text
HTML cache policy
hashed asset cache policy
CDN cache
browser HTTP cache
service worker/cache storage nếu có
runtime config cache
```

Một mẫu (pattern / 패턴) phổ biến là HTML có chính sách (policy / 정책) cho phép cập nhật nhanh, còn hashed immutable assets bộ nhớ đệm (cache / 캐시) dài. Khi HTML mới trỏ băm (hash / 해시) mới, đồ thị (graph / 그래프) chuyển phiên bản (version / 버전).

Nếu HTML cũ bị bộ nhớ đệm (cache / 캐시) sai, nó vẫn có thể tiếp tục trỏ bundle cũ hoàn toàn hợp lô-gic (logic / 논리).

Do đó sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) phải quan sát được.

---

# 26. Dịch vụ (service / 서비스) worker tạo thêm một mạng (network / 네트워크) đơn vị sở hữu (owner / 오너)

Nếu app có dịch vụ (service / 서비스) worker, đường đi của yêu cầu (request path / 요청 경로) có thể không đơn giản là:

```text
browser → network
```

Mà có thể là:

```text
page
→ service worker fetch handling
→ cache and/or network
→ response
```

Môi trường vận hành (production / 운영 환경) debugging phải hỏi dịch vụ (service / 서비스) worker phiên bản (version / 버전) nào đang điều khiển (control / 제어) page.

Nếu không, DevTools Mạng (network / 네트워크) nhìn thấy một phản hồi (response / 응답) nhưng ta có thể hiểu sai nguồn thực tế của nó.

---

# 27. Bản đồ mã nguồn (source map / 소스 맵): nguồn (source / 소스) dễ đọc không phải mã (code / 코드) trình duyệt (browser / 브라우저) execute

Môi trường vận hành (production / 운영 환경) dấu vết ngăn xếp (stack trace / 스택 트레이스) có thể map về TypeScript/JSX/nguồn (source / 소스) thông qua bản đồ mã nguồn (source map / 소스 맵).

Điều đó hữu ích, nhưng mô hình tư duy (mental model / 사고 모델) phải giữ:

```text
Mapped source location
≠ bytes executed directly by runtime
```

Bản dựng (build / 빌드) transform có thể thay mô-đun (module / 모듈), cú pháp (syntax / 문법), chunking, minification và đường đi mã (code path / 코드 경로).

Khi bug chỉ xảy ra môi trường vận hành (production / 운영 환경), cần giữ cả hai view:

- nguồn (source / 소스) view để lập luận (reasoning / 추론) lô-gic (logic / 논리);
- generated sản phẩm tạo ra (artifact / 산출물) view để lập luận (reasoning / 추론) thời gian chạy (runtime / 런타임)/bản dựng (build / 빌드) issue.

---

# 28. Build-time cấu hình (config / 설정) và thời gian chạy (runtime / 런타임) cấu hình (config / 설정) khác nhau

Ví dụ:

```text
API_BASE_URL
FEATURE_FLAG
BUILD_ID
```

Một giá trị có thể được bake vào bundle lúc bản dựng (build / 빌드) hoặc được tải thời gian chạy (runtime / 런타임).

Hai mô hình có operational consequence khác nhau.

Nếu build-time:

```text
config change
→ rebuild artifact
```

Nếu thời gian chạy (runtime / 런타임):

```text
same artifact
+ different runtime config
```

Khi môi trường vận hành (production / 운영 환경) sai endpoint, cần biết cấu hình (config / 설정) quyền sở hữu (ownership / 소유권) trước khi sửa mã (code / 코드).

---

# 29. Một dấu vết (trace / 추적) đúng phải có nhiều clock/timeline liên quan

Đừng chỉ giữ một screenshot waterfall.

Trường hợp (case / 사례) này nên được dấu vết (trace / 추적) trên ít nhất các lớp:

```text
Navigation/network timeline
Main-thread task timeline
Rendering timeline
Application state timeline
User-intent timeline
Deployment/artifact timeline
```

Ví dụ:

```text
T0 user navigates
T1 HTML response starts
T2 CSS discovered
T3 JS discovered
T4 first DOM content exists
T5 JS initialization starts
T6 API request starts
T7 initial frame shown
T8 API response arrives
T9 state update scheduled
T10 layout/paint
T11 user types filter
T12 filter computation
T13 next frame
```

Các timestamp cụ thể tùy run. Giá trị của diagram là buộc ta nói rõ **nhân quả (causal / 인과적) thứ tự (ordering / 순서)**.

---

# 30. Worked thất bại (failure / 실패) A — API nhanh nhưng màn hình chậm

Observation:

```text
/api/users response: 80 ms
UI list visible: 900 ms later
```

Naive conclusion:

> React chậm.

Kiểm tra (audit / 감사) luồng (flow / 흐름):

1. Xác định phản hồi (response / 응답) complete thời gian (time / 시간).
2. Xem Promise continuation chạy lúc nào.
3. Tìm long tác vụ (task / 작업) giữa phản hồi (response / 응답) và next paint.
4. Tách scripting/style/bố cục (layout / 레이아웃)/paint.
5. Kiểm tra số nút (node / 노드) được tạo.
6. Kiểm tra synchronous transform/sort/avatar processing.
7. Kiểm tra khung phần mềm (framework / 프레임워크) profiler nếu khung phần mềm (framework / 프레임워크) công việc (work / 작업) là phần lớn chi phí (cost / 비용).

Có thể cuối cùng nguyên nhân là:

```text
response
→ synchronous sort/group 250 ms
→ create 10k rows
→ style/layout 300 ms
→ paint 120 ms
```

Trong trường hợp (case / 사례) này “API nhanh” đúng, nhưng chưa nói bottleneck nằm ở khung phần mềm (framework / 프레임워크) reconciliation hay trình duyệt (browser / 브라우저) rendering.

---

# 31. Worked thất bại (failure / 실패) B — cục bộ (local / 로컬) đúng, môi trường vận hành (production / 운영 환경) sai CSS

Observation:

```text
local modal correct
production modal under header
```

Hypotheses hợp lý hơn random z-index:

```text
CSS build order khác?
chunk bị thiếu?
minifier/build transform thay output?
production-only class/content detection bỏ rule?
runtime portal target khác?
feature flag tạo ancestor stacking context khác?
old cached stylesheet?
```

Bằng chứng (evidence / 증거) cần:

- computed style;
- matched quy tắc (rule / 규칙)/nguồn (source / 소스);
- actual loaded biểu định kiểu (stylesheet / 스타일시트) băm (hash / 해시);
- DOM ancestry;
- ngữ cảnh xếp chồng (stacking context / 쌓임 맥락);
- bản dựng (build / 빌드) ID.

Chỉ so nguồn (source / 소스) SCSS chưa đủ.

---

# 32. Worked thất bại (failure / 실패) C — kết quả tìm kiếm (search / 검색) quay ngược

Timeline:

```text
T0 query="a"  → request A
T1 query="ab" → request B
T2 B returns   → state="ab results"
T3 A returns   → state="a results"
```

Mạng (network / 네트워크) hoạt động đúng. Backend có thể cũng đúng.

Bug là ứng dụng (application / 애플리케이션) không encode current-intent bất biến (invariant / 불변식).

Fix không phải “delay tìm kiếm (search / 검색) thêm 500 ms” như một luật universal.

Debounce có thể giảm yêu cầu (request / 요청) nhưng không tự giải quyết mọi stale thứ tự (ordering / 순서) nếu requests vẫn overlap.

Need:

```text
operation identity + cancellation/stale-result guard
```

---

# 33. Worked thất bại (failure / 실패) D — click lag nhưng animation vẫn mượt

Có thể compositor animation tiếp tục chạy tương đối mượt trong khi main luồng thực thi (thread / 스레드) bị long tác vụ (task / 작업), nên người dùng (user / 사용자) thấy một phần UI chuyển động nhưng click handler phản hồi chậm.

Bài học:

```text
visual motion quality
≠ main-thread responsiveness
```

Một chỉ số (metric / 지표)/symptom không đại diện toàn bộ responsiveness.

Cần bản ghi (record / 레코드) tương tác (interaction / 상호작용) và main-thread công việc (work / 작업).

---

# 34. Worked thất bại (failure / 실패) E — scroll jank chỉ khi mở DevTools hoặc máy yếu

Hiệu năng (performance / 성능) phụ thuộc môi trường (environment / 환경).

Một profile phải ghi ít nhất:

```text
browser/version
hardware class
viewport
network condition nếu relevant
data size
feature flags
build ID
profile method
```

Không cần giả lập chính xác mọi người dùng (user / 사용자), nhưng không được báo kết quả benchmark mà thiếu thực thi (execution / 실행) ngữ cảnh (context / 맥락).

---

# 35. Framework-specific lập luận (reasoning / 추론) chỉ bắt đầu sau nền tảng (platform / 플랫폼) bằng chứng (evidence / 증거)

Nếu app dùng React, ta có thể tiếp tục hỏi:

```text
component nào render?
state/props identity nào thay?
memo boundary có hợp lý không?
effect có duplicate work không?
hydration/concurrency có liên quan không?
```

Nếu dùng WebSquare:

```text
scope/page lifecycle nào?
DataCollection/Submission state nào?
Grid rendering/formatter có amplify work không?
WFrame ownership/lifetime nào?
```

Nhưng trước đó vẫn cần nền tảng (platform / 플랫폼) dấu vết (trace / 추적):

```text
network
DOM
style/layout/paint
main-thread tasks
```

Khung phần mềm (framework / 프레임워크) profiler không thay trình duyệt (browser / 브라우저) profiler; trình duyệt (browser / 브라우저) profiler cũng không giải thích hết khung phần mềm (framework / 프레임워크) logical quyền sở hữu (ownership / 소유권). Hai lớp bổ sung nhau.

---

# 36. Từ symptom tới hypothesis

Khi gặp lỗi, đừng nhảy từ symptom thẳng sang fix.

Dùng chuỗi (chain / 사슬):

```text
Symptom
→ observation
→ boundary
→ hypothesis
→ expected evidence
→ measurement
→ conclusion
→ smallest corrective change
→ re-measure
```

Ví dụ:

```text
Symptom: typing lag
Observation: 120 ms long task per keystroke
Boundary: JavaScript + rendering
Hypothesis: full list sort + rerender 10k rows
Expected evidence: sort stack + node/layout growth
Measurement: trace/profile
Change: pre-index + virtualization
Re-measure: interaction + memory + accessibility regression
```

Điểm quan trọng là fix phải nối với bằng chứng (evidence / 증거).

---

# 37. Thất bại (failure / 실패) ma trận (matrix / 행렬) cho màn hình `/users`

Không cần ghi nhớ bảng. Hãy dùng nó như mẫu (pattern / 패턴) lập luận (reasoning / 추론):

| Symptom | Có thể nằm ở | Bằng chứng (evidence / 증거) đầu tiên |
|---|---|---|
| Blank page | document/script/thời gian chạy (runtime / 런타임)/bảo mật (security / 보안) | document + console + loaded sản phẩm tạo ra (artifact / 산출물) |
| Unstyled page | CSS discovery/bộ nhớ đệm (cache / 캐시)/bản dựng (build / 빌드)/cascade | biểu định kiểu (stylesheet / 스타일시트) yêu cầu (request / 요청) + matched rules |
| Bố cục (layout / 레이아웃) shift | ảnh (image / 이미지)/font/động (dynamic / 동적) content hình học (geometry / 기하학) | timeline + element hình học (geometry / 기하학) |
| API dữ liệu (data / 데이터) không hiện | async/trạng thái (state / 상태)/kết xuất (render / 렌더링) | mạng (network / 네트워크) + chuyển tiếp trạng thái (state transition / 상태 전이) + tác vụ (task / 작업) dấu vết (trace / 추적) |
| Typing lag | compute/khung phần mềm (framework / 프레임워크)/DOM/bố cục (layout / 레이아웃)/paint | tương tác (interaction / 상호작용) dấu vết (trace / 추적) |
| Modal sau header | ngữ cảnh xếp chồng (stacking context / 쌓임 맥락)/portal/đầu ra (output / 출력) CSS | DOM + computed style + stacking ancestry |
| Người dùng (user / 사용자) cũ hiện sau tìm kiếm (search / 검색) mới | stale async thứ tự (ordering / 순서) | yêu cầu (request / 요청) + intent timeline |
| Môi trường vận hành (production / 운영 환경) khác cục bộ (local / 로컬) | bản dựng (build / 빌드)/cấu hình (config / 설정)/bộ nhớ đệm (cache / 캐시)/phiên bản (version / 버전) | bản dựng (build / 빌드) ID + tài nguyên (resource / 자원) hashes + cấu hình (config / 설정) |

Một symptom có nhiều candidate. Bằng chứng (evidence / 증거) dùng để loại dần, không phải intuition chọn ngay một nguyên nhân.

---

# 38. Sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) phải là một phần khả năng quan sát (observability / 관측 가능성)

Một môi trường vận hành (production / 운영 환경) frontend tốt nên có cách xác định phiên bản (version / 버전) đang chạy.

Ví dụ conceptual:

```text
commit SHA
build ID
deploy ID
bundle hash
runtime config version
```

Không nhất thiết expose mọi thứ công khai cho end người dùng (user / 사용자), nhưng kỹ thuật (engineering / 엔지니어링) telemetry/gỡ lỗi (debug / 디버그) info phải cho phép trả lời:

> Người dùng (user / 사용자) gặp lỗi này đang chạy sản phẩm tạo ra (artifact / 산출물) nào?

Nếu không, quay lui (rollback / 롤백) và sự cố (incident / 인시던트) correlation trở nên mơ hồ.

---

# 39. Hiệu năng (performance / 성능) ngân sách (budget / 예산) phải map tới người dùng (user / 사용자) công việc (work / 작업)

Không nên dùng một ngân sách (budget / 예산) chỉ vì công cụ (tool / 도구) có chỉ số (metric / 지표) đó.

Hãy map:

```text
startup
→ document/resource critical path
→ initialization
→ first useful content

interaction
→ input event
→ JavaScript work
→ rendering work
→ next presented frame

list update
→ data size
→ computation
→ DOM/framework work
→ layout/paint
```

Chỉ số (metric / 지표) là proxy cho người dùng (user / 사용자) experience và hệ thống (system / 시스템) công việc (work / 작업); không phải mục tiêu độc lập.

---

# 40. Một end-to-end dấu vết (trace / 추적) hoàn chỉnh nên trả lời được gì?

Sau trường hợp (case / 사례) này, người đọc phải có thể chọn một màn hình thật và trả lời:

```text
1. Document nào tạo page?
2. Resource graph nào tạo CSS/JS/font/image?
3. Artifact/version nào đang chạy?
4. Parser tạo DOM nào?
5. CSS nào thắng cascade và tại sao?
6. Geometry phụ thuộc constraint nào?
7. Thay đổi nào invalidate style/layout/paint?
8. Main thread đang làm work gì khi user chờ?
9. Event/Promise/request ordering là gì?
10. State canonical nằm ở đâu?
11. Async operation nào có identity/lifetime nào?
12. Accessibility contract nào phải giữ?
13. Security/trust boundary ở đâu?
14. Backend/DevOps domain sở hữu phần nào?
15. Evidence nào xác nhận hypothesis?
```

Nếu trả lời được 15 câu này, khung phần mềm (framework / 프레임워크) trở thành một lớp có thể lập luận (reasoning / 추론) chứ không còn là magic.

---

# 41. Bài thực hành bắt buộc

Chọn một page trong dự án (project / 프로젝트) thật.

Không bắt đầu bằng sửa mã (code / 코드). Trước tiên tạo tệp (file / 파일) dấu vết (trace / 추적) với cấu trúc (structure / 구조):

```text
A. User intent
B. URL/document request
C. dependent resource graph
D. DOM/CSS owner map
E. main-thread timeline
F. application state transitions
G. async operations and stale-result rules
H. rendering evidence
I. accessibility interaction contract
J. build/deploy artifact identity
K. top three failure hypotheses
L. measurement needed to distinguish them
```

Sau đó cố ý tạo một regression, ví dụ:

- bỏ ảnh (image / 이미지) dimension;
- kết xuất (render / 렌더링) gấp 10 lần rows;
- thêm synchronous sort nặng;
- tạo stale yêu cầu (request / 요청) race;
- thêm ancestor ngữ cảnh xếp chồng (stacking context / 쌓임 맥락);
- deploy HTML bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) không phù hợp trong môi trường (environment / 환경) kiểm thử (test / 테스트).

Quan sát dấu vết (trace / 추적) thay đổi ở đâu.

Đây là cách biến mô hình tư duy (mental model / 사고 모델) thành debugging skill.

---

# 42. Exit gate

Trường hợp (case / 사례) hoàn thành khi người học không còn nói các câu quá rộng như:

```text
"Frontend chậm"
"React lỗi"
"CSS lag"
"API chưa load"
```

mà có thể chuyển chúng thành statement có ranh giới (boundary / 경계) và bằng chứng (evidence / 증거):

```text
"Input event bắt đầu lúc T0; handler tạo một 96 ms main-thread task,
trong đó 61 ms là synchronous filtering và 24 ms là style/layout trên
8.400 row nodes. Network không nằm trên interaction critical path."
```

hoặc:

```text
"Production document đang tải app.OLDHASH.js từ cached HTML version cũ;
source branch đã mới nhưng browser không chạy artifact mới."
```

Độ sâu (depth / 깊이) của Frontend nằm ở khả năng chuyển symptom thành nhân quả (causal / 인과적) dấu vết (trace / 추적) như vậy.

## Cross-link

Đọc song song:

- [`../README.md`](../README.md) để giữ lĩnh vực (domain / 도메인) map;
- [`../COVERAGE_AUDIT.md`](../COVERAGE_AUDIT.md) để biết đơn vị sở hữu (owner / 오너) và remaining gaps;
- JavaScript Cấp cao (senior / 시니어)/Master cho vòng lặp sự kiện (event loop / 이벤트 루프), networking, hiệu năng (performance / 성능) và triển khai (deployment / 배포) ranh giới (boundary / 경계);
- CSS Master cho rendering/cascade/bố cục (layout / 레이아웃) bằng chứng (evidence / 증거);
- HTML Master cho parser, ngữ nghĩa (semantics / 의미론), tài nguyên (resource / 자원) loading và khả năng tiếp cận (accessibility / 접근성);
- React/WebSquare nhánh học (track / 트랙) khi cần map nền tảng (platform / 플랫폼) dấu vết (trace / 추적) sang khung phần mềm (framework / 프레임워크) quyền sở hữu (ownership / 소유권).

Tiếp theo làm [Rendering Performance Measurement Lab](./01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md) để biến phần style/bố cục (layout / 레이아웃)/paint/composite thành quy trình đo lặp lại được.
