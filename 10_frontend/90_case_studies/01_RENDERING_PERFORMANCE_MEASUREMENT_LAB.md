# Rendering hiệu năng (performance / 성능) đo lường (measurement / 측정) Lab — đo style, bố cục (layout / 레이아웃), paint và composite thay vì đoán

> **Mạch đọc:** Đặt **Rendering hiệu năng (performance / 성능) đo lường (measurement / 측정) Lab — đo style, bố cục (layout / 레이아웃), paint và composite thay vì đoán** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **dấu vết (trace / 추적) A — tương tác (interaction / 상호작용)** sang **dấu vết (trace / 추적) B — tải (load / 로드)/cập nhật (update / 업데이트)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Frontend hiệu năng (performance / 성능) rất dễ bị biến thành folklore:

```text
transform = nhanh
box-shadow = chậm
React render = xấu
DOM lớn = luôn chậm
GPU = tốt
will-change = tối ưu
```

Một số câu có thể đúng trong một ngữ cảnh (context / 맥락) cụ thể, nhưng không câu nào đủ để thay đo lường (measurement / 측정).

Lab này tập trung vào một nguyên tắc:

```text
Không tối ưu rendering bằng tên property.
Tối ưu bằng trace của work thực tế.
```

Mục tiêu không phải học thuộc internals của một trình duyệt (browser / 브라우저) engine cụ thể. Mục tiêu là xây workflow có thể lặp lại:

```text
Symptom
→ reproducible scenario
→ baseline
→ trace
→ classify work
→ identify invalidation / owner
→ hypothesis
→ one change
→ re-measure
→ regression guard
```

---

# 1. hiệu năng (performance / 성능) là câu hỏi về đường găng (critical path / 임계 경로)

Một page có thể làm rất nhiều công việc (work / 작업) nhưng người dùng (user / 사용자) chỉ bị khối (block / 블록) bởi phần nằm trên đường găng (critical path / 임계 경로) của intent hiện tại.

Ví dụ người dùng (user / 사용자) click “Open detail”. Ta quan tâm:

```text
input
→ event dispatch
→ application handler
→ state transition
→ DOM/style consequences
→ layout/paint/composite if needed
→ next useful frame
```

Nếu đồng thời background analytics chạy 20 ms sau frame, nó vẫn là chi phí (cost / 비용) đáng quan tâm nhưng không nhất thiết là nguyên nhân chính của click độ trễ (latency / 지연 시간) đó.

Do đó trước khi profile phải xác định:

```text
User action nào?
Expected visible result nào?
Start và end của interaction ở đâu?
```

Không có phạm vi (scope / 범위) này, dấu vết (trace / 추적) dễ biến thành một ảnh đầy màu nhưng không có câu hỏi.

---

# 2. Chọn scenario có thể tái tạo

Không profile một page bằng cách “click thử vài thứ”.

Định nghĩa scenario:

```text
Dataset: 5.000 rows
Viewport: desktop 1440×900
State: page đã load, cache warm
Action: gõ một ký tự vào filter
Expected result: list cập nhật và input vẫn responsive
Runs: ít nhất vài lần cùng điều kiện
```

Hoặc:

```text
State: modal đóng
Action: click Open Detail
Expected result: overlay + dialog visible, focus moved inside
```

Scenario phải đủ cụ thể để before/after có thể so.

---

# 3. Ghi môi trường (environment / 환경) trước khi ghi chỉ số (metric / 지표)

Hiệu năng (performance / 성능) kết quả (result / 결과) không có ngữ cảnh (context / 맥락) thì rất khó tái tạo.

Ghi:

```text
browser + version
OS
device/hardware class
viewport/device scale nếu relevant
build ID / commit
feature flags
data volume
network/cache condition
CPU/network throttling nếu có
```

Không cần mọi benchmark phải lab-grade. Nhưng cần đủ ngữ cảnh (context / 맥락) để biết hai run có đang so cùng một hệ thống hay không.

---

# 4. Warm bộ nhớ đệm (cache / 캐시) và cold bộ nhớ đệm (cache / 캐시) là hai câu hỏi khác nhau

Cold tải (load / 로드) có thể bị chi phối bởi mạng (network / 네트워크)/tài nguyên (resource / 자원) startup.

Warm tương tác (interaction / 상호작용) có thể bị chi phối bởi JavaScript/rendering.

Đừng gộp:

```text
page load performance
interaction performance
```

thành một con số “frontend speed”.

Nếu mục tiêu là rendering khi filter rows, warm page trước rồi đo tương tác (interaction / 상호작용). Nếu mục tiêu là first điều hướng (navigation / 내비게이션), cold/warm bộ nhớ đệm (cache / 캐시) phải được ghi rõ.

---

# 5. Baseline trước tối ưu hóa (optimization / 최적화)

Trước khi sửa mã (code / 코드), ghi baseline.

Ví dụ:

```text
Interaction duration: 140 ms
Scripting: 72 ms
Style: 18 ms
Layout: 31 ms
Paint/composite-related work: 12 ms
Other: 7 ms
Affected DOM nodes: ~5.000
```

Các con số chỉ là ví dụ. công cụ (tool / 도구)/trình duyệt (browser / 브라우저) có thể nhóm công việc (work / 작업) khác nhau.

Điểm quan trọng là decomposition.

Nếu không có baseline, sau tối ưu hóa (optimization / 최적화) ta chỉ biết “cảm giác nhanh hơn”.

---

# 6. Scripting, style, bố cục (layout / 레이아웃), paint và composite là categories, không phải blame labels

Khi thấy bố cục (layout / 레이아웃) lớn, đừng kết luận CSS nhóm (team / 팀) sai.

Bố cục (layout / 레이아웃) có thể bị kích hoạt bởi JavaScript mutation.

Khi thấy scripting lớn, đừng kết luận khung phần mềm (framework / 프레임워크) sai.

Scripting có thể là app nghiệp vụ (business / 비즈니스) transform hoặc third-party mã (code / 코드).

Lập luận (reasoning / 추론) phải nối:

```text
Who caused invalidation?
What work became necessary?
How large was affected scope?
```

Đơn vị sở hữu (owner / 오너) của **cause** và đơn vị sở hữu (owner / 오너) của **công việc (work / 작업) category** có thể khác nhau.

---

# 7. Style vô hiệu hóa (invalidation / 무효화)

Một DOM/lớp (class / 클래스)/trạng thái (state / 상태) thay đổi (change / 변경) có thể làm trình duyệt (browser / 브라우저) phải tính lại style cho một phạm vi (scope / 범위) nào đó.

Ví dụ:

```js
document.body.classList.add('dark')
```

Nếu theme selector ảnh hưởng phần lớn cây (tree / 트리), style công việc (work / 작업) có thể rộng.

Nhưng không nên nói:

> đổi lớp (class / 클래스) body luôn chậm.

Chi phí (cost / 비용) phụ thuộc:

- selector đồ thị (graph / 그래프);
- số affected nodes;
- hiện thực (implementation / 구현);
- trạng thái hiện tại (current state / 현재 상태);
- follow-up bố cục (layout / 레이아웃)/paint.

Dấu vết (trace / 추적) mới trả lời scenario cụ thể.

---

# 8. bố cục (layout / 레이아웃) vô hiệu hóa (invalidation / 무효화)

Bố cục (layout / 레이아웃) công việc (work / 작업) xảy ra khi hình học (geometry / 기하학) cần được xác định lại.

Các thay đổi liên quan kích thước (size / 크기)/luồng (flow / 흐름) có thể kéo theo bố cục (layout / 레이아웃), nhưng phạm vi (scope / 범위) không phải lúc nào cũng toàn document.

Câu hỏi đúng:

```text
Geometry nào đổi?
Ancestor/descendant/sibling nào phụ thuộc geometry đó?
Formatting context nào bị ảnh hưởng?
```

Một thành phần (component / 컴포넌트) được isolate tốt có thể giới hạn propagation tốt hơn một cây (tree / 트리) có phụ thuộc (dependency / 의존성) rộng.

---

# 9. Forced synchronous bố cục (layout / 레이아웃) là thứ tự (ordering / 순서) bài toán (problem / 문제)

Mẫu (pattern / 패턴) kinh điển:

```js
el.style.width = '200px';
const width = el.offsetWidth;
```

Mã (code / 코드) vừa mutation có khả năng invalidate bố cục (layout / 레이아웃), sau đó ngay lập tức đọc hình học (geometry / 기하학) cần giá trị cập nhật.

Trình duyệt (browser / 브라우저) có thể buộc phải resolve pending bố cục (layout / 레이아웃) trước khi trả kết quả read.

Đây không đơn giản là:

```text
offsetWidth = slow
```

Vấn đề là **read/ghi (write / 쓰기) thứ tự (ordering / 순서)**.

Một read riêng lẻ khi bố cục (layout / 레이아웃) already clean có thể rẻ hơn nhiều.

Mô hình tư duy (mental model / 사고 모델):

```text
write that invalidates geometry
→ geometry read before normal rendering opportunity
→ synchronous layout may be forced
```

---

# 10. bố cục (layout / 레이아웃) thrashing

Xấu hơn là xen kẽ read/ghi (write / 쓰기) trong vòng lặp (loop / 루프):

```js
for (const item of items) {
  item.style.width = computeWidth(item);
  total += item.offsetWidth;
}
```

Potential mẫu (pattern / 패턴):

```text
write
→ force layout
→ write
→ force layout
→ ...
```

Một chiến lược (strategy / 전략) tốt hơn có thể batch reads rồi writes nếu ngữ nghĩa (semantic / 의미적) cho phép.

Nhưng đừng refactor chỉ vì thấy mẫu (pattern / 패턴). Profile để xác nhận bố cục (layout / 레이아웃) thực sự đáng kể trong scenario.

---

# 11. Paint chi phí (cost / 비용) phụ thuộc vùng và visual độ phức tạp (complexity / 복잡도)

Paint không phải nhị phân (binary / 이진) “thuộc tính (property / 속성) A paint, thuộc tính (property / 속성) B không paint”.

Chi phí (cost / 비용) còn phụ thuộc:

- area bị invalidate;
- number of elements;
- clipping;
- effects;
- văn bản (text / 텍스트);
- images;
- scrolling;
- raster quy mô (scale / 규모).

Một tác động (effect / 효과) đắt trên full-screen tầng (layer / 계층) khác hoàn toàn cùng tác động (effect / 효과) trên icon 20×20.

Do đó khi kiểm tra (audit / 감사) paint, hỏi:

```text
What region repainted?
Why?
How often?
How large/complex?
```

---

# 12. Composite không miễn phí

Nếu trình duyệt (browser / 브라우저) có thể composite một tầng (layer / 계층) mà không repaint content, điều đó có thể hữu ích.

Nhưng layers có chi phí (cost / 비용):

- bộ nhớ (memory / 메모리);
- management;
- raster surfaces;
- transfer/upload depending on kiến trúc (architecture / 아키텍처);
- composition độ phức tạp (complexity / 복잡도).

Nếu promote hàng nghìn element “để GPU chạy”, ta có thể đổi một bottleneck sang bottleneck khác.

Vì vậy:

```text
more layers
≠ automatically faster
```

---

# 13. `will-change` là hint, không phải turbo button

`will-change` có thể cho trình duyệt (browser / 브라우저) biết một thuộc tính (property / 속성) có khả năng thay đổi, giúp chuẩn bị tối ưu hóa (optimization / 최적화) trong một số trường hợp (case / 사례).

Nhưng giữ nó rộng/lâu trên nhiều nút (node / 노드) có thể tăng tài nguyên (resource / 자원) chi phí (cost / 비용).

Workflow đúng:

```text
measured bottleneck
→ specific animation/update
→ test whether will-change improves trace
→ remove if no evidence / avoid global blanket use
```

Không thêm `will-change: transform` vào mọi thành phần (component / 컴포넌트) như default reset.

---

# 14. Animation lab A — `top/left` và `transform`

Tạo một box di chuyển 300 px trong 500 ms.

Phiên bản (version / 버전) A thay `left`.

Phiên bản (version / 버전) B dùng `transform: translateX(...)`.

Không bắt đầu bằng kết luận B thắng.

Bản ghi (record / 레코드):

```text
main-thread work
style/layout
paint
composite/layer behavior
frame consistency
memory/layers if observable
```

Trong nhiều môi trường (environment / 환경), transform animation có thể tránh bố cục (layout / 레이아웃) tốt hơn. Nhưng lab chỉ đạt khi người học có thể **show bằng chứng (evidence / 증거)**, không chỉ lặp câu này.

Sau đó tăng:

```text
1 box
→ 100 boxes
→ 2.000 boxes
```

Quan sát scaling. Một tối ưu hóa (optimization / 최적화) ở quy mô (scale / 규모) 1 có thể có sự đánh đổi (trade-off / 트레이드오프) khác ở quy mô (scale / 규모) lớn.

---

# 15. Animation lab B — visual tác động (effect / 효과) lớn

Tạo card lớn có shadow/filter và animate.

Thử:

- animate hình học (geometry / 기하학);
- animate opacity;
- animate transform;
- thay kích thước (size / 크기) vùng tác động (effect / 효과).

Mục tiêu không phải lập bảng universal thuộc tính (property / 속성) chi phí (cost / 비용).

Mục tiêu là thấy:

```text
same property family
× different area/count/device
→ different total cost
```

Hiệu năng (performance / 성능) là thuộc tính (property / 속성) của tải công việc (workload / 워크로드), không chỉ cú pháp (syntax / 문법).

---

# 16. danh sách (list / 목록) lab — 100, 1.000, 10.000 rows

Kết xuất (render / 렌더링) cùng thành phần (component / 컴포넌트) với dataset tăng dần.

Ghi:

```text
DOM node count
initial render time
filter interaction
style/layout time
memory trend
scroll behavior
```

Sau đó kiểm thử (test / 테스트) một số intervention:

```text
reduce rendered columns
avoid expensive synchronous transform
virtualize visible rows
memoize only proven repeated computation
change DOM structure
```

Không apply tất cả cùng lúc. Mỗi run chỉ nên thay đủ ít để attribution còn rõ.

---

# 17. khung phần mềm (framework / 프레임워크) kết xuất (render / 렌더링) và trình duyệt (browser / 브라우저) rendering phải tách

Trong React, “kết xuất (render / 렌더링)” thường được dùng cho khung phần mềm (framework / 프레임워크) kết xuất (render / 렌더링)/reconciliation.

Trình duyệt (browser / 브라우저) rendering lại có style/bố cục (layout / 레이아웃)/paint/composite.

Hai từ giống nhau nhưng khác tầng (layer / 계층).

Có thể có trường hợp (case / 사례):

```text
React render nhiều
but DOM output nearly unchanged
→ browser layout small
```

Hoặc:

```text
React work nhỏ
but one DOM mutation invalidates large layout
→ browser rendering large
```

Vì vậy report phải nói rõ:

```text
framework render/reconciliation
vs
browser rendering pipeline
```

---

# 18. Measure lần ghi nhận (commit / 커밋)/đầu ra (output / 출력), không chỉ hàm (function / 함수) calls

Một thành phần (component / 컴포넌트) hàm (function / 함수) chạy 20 lần chưa tự nói người dùng (user / 사용자) bị chậm bao nhiêu.

Cần biết:

- mỗi run làm công việc (work / 작업) gì;
- đầu ra (output / 출력) có thay không;
- lần ghi nhận (commit / 커밋)/mutation nào xảy ra;
- trình duyệt (browser / 브라우저) công việc (work / 작업) sau lần ghi nhận (commit / 커밋) là gì.

Count là tín hiệu (signal / 신호), không phải verdict.

---

# 19. Memoization có chi phí (cost / 비용) và ngữ nghĩa (semantic / 의미적) rủi ro (risk / 위험)

Memoization có thể tránh computation/kết xuất (render / 렌더링) công việc (work / 작업) lặp lại, nhưng cũng có:

- bộ nhớ (memory / 메모리);
- comparison chi phí (cost / 비용);
- phụ thuộc (dependency / 의존성) độ phức tạp (complexity / 복잡도);
- stale giá trị (value / 값) bug nếu phụ thuộc (dependency / 의존성) mô hình (model / 모델) sai;
- cognitive chi phí (cost / 비용).

Do đó:

```text
profile → find repeat expensive work → memoize candidate → remeasure
```

thay vì:

```text
component → memo everywhere
```

---

# 20. sự kiện (event / 이벤트) handler độ trễ (latency / 지연 시간) và rendering độ trễ (latency / 지연 시간) khác nhau

Một đầu vào (input / 입력) handler có thể chạy 5 ms nhưng frame xuất hiện 80 ms sau vì rendering công việc (work / 작업).

Ngược lại handler có thể chạy 70 ms nhưng DOM thay đổi (change / 변경) nhỏ.

Dấu vết (trace / 추적) tương tác (interaction / 상호작용) phải giữ cả hai.

Một useful decomposition:

```text
input delay
processing time
presentation delay
```

Tên cụ thể trong chỉ số (metric / 지표)/công cụ (tool / 도구) có thể khác theo nền tảng (platform / 플랫폼), nhưng mô hình tư duy (mental model / 사고 모델) giúp không đổ mọi độ trễ (latency / 지연 시간) cho handler.

---

# 21. Long tác vụ (task / 작업): ranh giới (boundary / 경계) hữu ích nhưng không phải nguyên nhân gốc (root cause / 근본 원인)

Nếu main luồng thực thi (thread / 스레드) bị một tác vụ (task / 작업) dài, người dùng (user / 사용자) đầu vào (input / 입력) có thể phải chờ.

Nhưng “long tác vụ (task / 작업)” chỉ nói bộ chứa (container / 컨테이너) công việc (work / 작업) dài.

Bên trong có thể là:

- ứng dụng (application / 애플리케이션) JavaScript;
- JSON transform;
- khung phần mềm (framework / 프레임워크) rendering;
- style/bố cục (layout / 레이아웃) forced synchronously;
- third-party mã (code / 코드);
- logging/instrumentation.

Drill down ngăn xếp lời gọi (call stack / 호출 스택)/timeline để tìm đơn vị sở hữu (owner / 오너).

---

# 22. Microtask starvation

Mã (code / 코드) có thể không có một synchronous vòng lặp (loop / 루프) lớn nhưng vẫn chuỗi (chain / 사슬) Promise/microtask liên tục.

Nếu microtasks tiếp tục tạo microtask mới, trình duyệt (browser / 브라우저) có thể bị trì hoãn trước rendering opportunity hoặc other tác vụ (task / 작업).

Lab nhỏ:

```js
function spin() {
  Promise.resolve().then(spin);
}
spin();
```

Không chạy vô hạn trong môi trường vận hành (production / 운영 환경). Đây chỉ là conceptual warning rằng:

```text
Promise-based
≠ automatically cooperative with rendering
```

Scheduling ngữ nghĩa (semantics / 의미론) quan trọng.

---

# 23. `requestAnimationFrame` không sửa thuật toán (algorithm / 알고리즘) nặng

`requestAnimationFrame` giúp schedule callback quanh rendering cycle, hữu ích cho visual updates.

Nhưng nếu callback làm 80 ms computation:

```text
rAF
→ 80 ms work
→ missed frames
```

API đúng không cứu tải công việc (workload / 워크로드) quá lớn.

Nếu computation có thể split/offload, cần lập luận (reasoning / 추론) riêng về scheduling/worker/dữ liệu (data / 데이터) transfer.

---

# 24. Worker không phải miễn phí

Web Worker có thể đưa CPU công việc (work / 작업) khỏi main luồng thực thi (thread / 스레드), nhưng có chi phí (cost / 비용):

- message serialization/structured clone;
- transfer;
- worker startup;
- duplicated trạng thái (state / 상태)/coordination;
- kiến trúc (architecture / 아키텍처) độ phức tạp (complexity / 복잡도).

Dùng worker khi tải công việc (workload / 워크로드) và độ trễ (latency / 지연 시간) justify, không phải vì “multithreading luôn nhanh hơn”.

Measure end-to-end:

```text
main thread freed
vs
communication overhead
vs
total latency
```

---

# 25. Scroll hiệu năng (performance / 성능)

Scroll jank có thể liên quan:

- main-thread sự kiện (event / 이벤트) công việc (work / 작업);
- bố cục (layout / 레이아웃) during scroll;
- large paint area;
- sticky/fixed effects;
- ảnh (image / 이미지) decode/raster;
- huge DOM;
- third-party listeners.

Đừng chỉ tìm kiếm (search / 검색) mã (code / 코드) `scroll` listener.

Bản ghi (record / 레코드) scroll session và xem công việc (work / 작업) thực tế.

Nếu listener không xuất hiện đáng kể mà paint dominates, tối ưu listener không giải quyết vấn đề.

---

# 26. Resize hiệu năng (performance / 성능)

Resize là kiểm thử sức chịu tải (stress test / 스트레스 테스트) tốt cho responsive bố cục (layout / 레이아웃).

Một bố cục (layout / 레이아웃) có thể ổn khi static nhưng resize gây:

```text
repeated JS measurement
+
DOM write
+
forced layout
```

Nếu mã (code / 코드) resize handler tự đo/mutate liên tục, khung phần mềm (framework / 프레임워크)/CSS responsive features có thể bị vô hiệu hóa bởi ứng dụng (application / 애플리케이션) vòng lặp (loop / 루프).

Dấu vết (trace / 추적) để biết bottleneck ở CSS bố cục (layout / 레이아웃) hay JS đo lường (measurement / 측정) mẫu (pattern / 패턴).

---

# 27. ảnh (image / 이미지) decode và raster là phần user-visible chuỗi xử lý (pipeline / 파이프라인)

Ảnh (image / 이미지) yêu cầu (request / 요청) complete không nhất thiết điểm ảnh (pixel / 픽셀) đã sẵn sàng ngay.

Trình duyệt (browser / 브라우저) còn cần decode/raster/tiến trình (process / 프로세스) tùy format/đường dẫn (path / 경로).

Với gallery lớn, mạng (network / 네트워크) có thể nhanh nhưng xử lý ảnh (image processing / 이미지 처리) + bộ nhớ (memory / 메모리) vẫn gây jank.

Tối ưu hóa (optimization / 최적화) có thể gồm:

- đúng resolution;
- lazy loading phù hợp;
- reserve dimensions;
- avoid decoding huge nguồn (source / 소스) chỉ để display thumbnail;
- reduce simultaneous heavy công việc (work / 작업).

Nhưng lại phải đo tải công việc (workload / 워크로드) cụ thể.

---

# 28. Font hiệu năng (performance / 성능)

Font ảnh hưởng cả mạng (network / 네트워크) lẫn bố cục (layout / 레이아웃).

Lab:

1. bản ghi (record / 레코드) page với fallback only;
2. bản ghi (record / 레코드) web font;
3. quan sát font yêu cầu (request / 요청);
4. quan sát văn bản (text / 텍스트)/bố cục (layout / 레이아웃) shift nếu có;
5. kiểm tra font kích thước (size / 크기)/weight subsets và usage.

Mục tiêu là thấy font quyết định (decision / 결정) không chỉ là thiết kế (design / 설계) choice.

---

# 29. Hidden công việc (work / 작업)

Một element invisible với người dùng (user / 사용자) chưa chắc không tạo chi phí (cost / 비용).

Tùy cách hide:

- nó có thể không participate bố cục (layout / 레이아웃);
- có thể vẫn giữ subtree/trạng thái (state / 상태)/listeners;
- có thể vẫn được khung phần mềm (framework / 프레임워크) cập nhật (update / 업데이트);
- có thể giữ media/tài nguyên (resource / 자원).

Không suy từ “không thấy trên màn hình” rằng công việc (work / 작업) bằng 0.

Measure thành phần (component / 컴포넌트)/ứng dụng (application / 애플리케이션) hành vi (behavior / 동작).

---

# 30. CSS selector folklore

Hiện đại (modern / 현대적) engines có nhiều tối ưu hóa (optimization / 최적화); selector cú pháp (syntax / 문법) đơn lẻ hiếm khi là nơi nên bắt đầu nếu không có bằng chứng (evidence / 증거).

Nếu style recalculation lớn, inspect:

- affected nút (node / 노드) count;
- vô hiệu hóa (invalidation / 무효화) nguồn (source / 소스);
- selector/cascade cấu trúc (structure / 구조);
- DOM phạm vi (scope / 범위);
- frequency.

Không dành hàng giờ đổi `.parent .child` thành `.child` nếu dấu vết (trace / 추적) cho thấy 90% chi phí (cost / 비용) là JavaScript computation.

---

# 31. Containment và isolation

CSS/nền tảng (platform / 플랫폼) có các cơ chế giúp giới hạn phạm vi (scope / 범위) bố cục (layout / 레이아웃)/rendering trong một số scenario.

Nhưng containment thay ngữ nghĩa (semantic / 의미적)/bố cục (layout / 레이아웃) hành vi (behavior / 동작) và cần hiểu đặc tả hợp đồng (contract / 계약).

Không thêm chỉ vì benchmark nhỏ đẹp hơn.

Kiểm tra:

```text
layout correctness
size behavior
overflow
accessibility
sticky/positioning interaction
```

Tối ưu hóa (optimization / 최적화) không được phá bất biến (invariant / 불변식).

---

# 32. hiệu năng (performance / 성능) fix có thể tạo khả năng tiếp cận (accessibility / 접근성) regression

Virtualization hoặc custom scrolling có thể cải thiện frame thời gian (time / 시간) nhưng phá:

- keyboard điều hướng (navigation / 내비게이션);
- screen-reader traversal;
- find-in-page;
- focus restoration;
- ngữ nghĩa (semantic / 의미적) bảng (table / 테이블)/danh sách (list / 목록) cấu trúc (structure / 구조).

Do đó before/after không chỉ là timing.

Regression ma trận (matrix / 행렬) phải gồm công khai (public / 공개) hành vi (behavior / 동작).

---

# 33. hiệu năng (performance / 성능) fix có thể tạo tính đúng đắn (correctness / 정확성) regression

Debounce tìm kiếm (search / 검색) giúp giảm công việc (work / 작업) nhưng thay ngữ nghĩa (semantics / 의미론).

Nếu người dùng (user / 사용자) kiểu (type / 타입) rồi immediately submit, pending debounced trạng thái (state / 상태) có được lần ghi nhận (commit / 커밋) đúng không?

Nếu filter là accessibility-critical phản hồi (feedback / 피드백), delay có hợp lý không?

Tối ưu hóa (optimization / 최적화) không được được đánh giá riêng khỏi hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약).

---

# 34. hiệu năng (performance / 성능) fix có thể chuyển chi phí (cost / 비용) sang máy chủ (server / 서버)/mạng (network / 네트워크)

Client-side filter 100k records chậm.

Ta chuyển sang máy chủ (server / 서버) tìm kiếm (search / 검색).

Máy khách (client / 클라이언트) nhẹ hơn, nhưng hệ thống (system / 시스템) có thêm:

- yêu cầu (request / 요청) độ trễ (latency / 지연 시간);
- máy chủ (server / 서버) tải (load / 로드);
- cancellation/stale race;
- pagination;
- bộ nhớ đệm (cache / 캐시);
- offline/lỗi (error / 오류) hành vi (behavior / 동작).

Đây có thể vẫn là kiến trúc tốt, nhưng phải đánh giá end-to-end chứ không tuyên bố “frontend nhanh hơn” rồi dừng.

---

# 35. Production-like dữ liệu (data / 데이터) quan trọng hơn toy dữ liệu (data / 데이터)

Một bảng (table / 테이블) 20 rows không reveal bottleneck của bảng (table / 테이블) 20.000 rows.

Hiệu năng (performance / 성능) kiểm thử (test / 테스트) cần dữ liệu (data / 데이터) phân phối (distribution / 분포) gần use trường hợp (case / 사례):

```text
row count
text length
image count
column count
nested components
error/empty/loading states
```

Không cần bản sao (copy / 복사) dữ liệu nhạy cảm; synthetic dataset có cùng shape/phân phối (distribution / 분포) là đủ tốt hơn toy demo.

---

# 36. Tail độ trễ (latency / 지연 시간)

Average tương tác (interaction / 상호작용) 30 ms nhưng thỉnh thoảng 250 ms vẫn gây vấn đề.

Do đó đừng chỉ report mean.

Có thể xem phân phối (distribution / 분포):

```text
median
p75
p95/p99 khi sample đủ
worst observed with context
```

Không cần dùng percentile nếu mẫu (sample / 표본) quá nhỏ để có ý nghĩa. Nhưng principle là hiệu năng (performance / 성능) có phân phối (distribution / 분포).

---

# 37. Run-to-run variance

Garbage collection, background tiến trình (process / 프로세스), bộ nhớ đệm (cache / 캐시), JIT/thời gian chạy (runtime / 런타임) trạng thái (state / 상태) và OS scheduling có thể làm run khác nhau.

Đừng kết luận từ một run:

```text
Before 102 ms
After 98 ms
→ 4% faster!
```

Nếu variance tự nhiên ±15 ms, kết luận đó không đáng tin.

Lặp run và nhìn tác động (effect / 효과) kích thước (size / 크기) so với noise.

---

# 38. Synthetic lab và trường dữ liệu (field / 필드) telemetry trả lời câu hỏi khác nhau

Cục bộ (local / 로컬) dấu vết (trace / 추적) giúp nhân quả (causal / 인과적) debugging sâu.

Trường dữ liệu (field / 필드) telemetry/RUM giúp biết người dùng (user / 사용자) population thực gặp gì.

Mô hình tư duy (mental model / 사고 모델):

```text
Lab profiling
→ Why does this scenario cost what it costs?

Field telemetry
→ How often, for whom, on what devices/network, does this problem happen?
```

Một lab fix tốt nên sau đó được monitor trường dữ liệu (field / 필드) nếu app có telemetry.

---

# 39. Third-party scripts

Analytics, chat widget, tag manager hoặc ad/monitoring SDK có thể chiếm main luồng thực thi (thread / 스레드)/mạng (network / 네트워크).

Không loại chúng khỏi dấu vết (trace / 추적) chỉ vì “không phải mã (code / 코드) nhóm (team / 팀) mình”.

Người dùng (user / 사용자) trả chi phí (cost / 비용) của toàn page.

Nếu third-party là bottleneck, mitigation có thể là:

- defer/lazy tải (load / 로드);
- reduce provider count;
- conditional tải (load / 로드);
- isolate;
- renegotiate yêu cầu (requirement / 요구사항).

Kiến trúc (architecture / 아키텍처) includes bên ngoài (external / 외부) dependencies.

---

# 40. bộ nhớ (memory / 메모리) và GC

Rendering hiệu năng (performance / 성능) không chỉ frame timing.

Nếu thành phần (component / 컴포넌트)/danh sách (list / 목록) leak bộ nhớ (memory / 메모리):

```text
navigation count ↑
→ retained objects ↑
→ GC pressure ↑
→ long pauses / eventual crash
```

Lab dài hơn có thể repeat open/close modal hoặc tuyến (route / 경로) điều hướng (navigation / 내비게이션) nhiều lần, sau đó inspect retention trend.

Một fast first run không chứng minh thời gian chạy (runtime / 런타임) stable sau hai giờ sử dụng.

---

# 41. Modal leak experiment

Scenario:

```text
open modal
close modal
repeat 100 times
```

Nhánh học (track / 트랙):

- detached DOM nodes nếu observable;
- retained listeners/subscriptions;
- đối tượng (object / 객체) count/bộ nhớ (memory / 메모리) trend;
- mạng (network / 네트워크)/subscription duplication;
- later tương tác (interaction / 상호작용) độ trễ (latency / 지연 시간).

Nếu bộ nhớ (memory / 메모리) tăng không quay lại ngay, chưa chắc leak vì GC timing. Cần inspect retention/tham chiếu (reference / 참조) đường dẫn (path / 경로) thay vì chỉ nhìn một bộ nhớ (memory / 메모리) number.

---

# 42. Large bảng (table / 테이블) experiment

Tạo three versions:

```text
A. render all rows
B. paginate
C. virtualize
```

So:

```text
startup
filter/update
scroll
memory
a11y/keyboard
complexity
```

Không có winner universal.

Pagination thay thông tin (information / 정보) kiến trúc (architecture / 아키텍처). Virtualization giữ continuous danh sách (list / 목록) feel nhưng tăng hiện thực (implementation / 구현) độ phức tạp (complexity / 복잡도). kết xuất (render / 렌더링) all có thể hoàn toàn đủ cho 200 rows.

Tối ưu hóa (optimization / 최적화) phải phù hợp quy mô (scale / 규모) thực tế.

---

# 43. bố cục (layout / 레이아웃) shift experiment

Tạo card với ảnh (image / 이미지) không có reserved kích thước (size / 크기).

Bản ghi (record / 레코드).

Sau đó thêm width/height/aspect-ratio đặc tả hợp đồng (contract / 계약) phù hợp.

Bản ghi (record / 레코드) lại.

Quan sát:

```text
geometry stability
layout work
user target movement
```

Bài này nối hiệu năng (performance / 성능) với tính đúng đắn (correctness / 정확성)/UX mà không cần khung phần mềm (framework / 프레임워크).

---

# 44. Stacking/overlay experiment

Tạo modal trong ancestor có transform/ngữ cảnh xếp chồng (stacking context / 쌓임 맥락).

Thử tăng z-index rồi quan sát vì sao không vượt ngữ cảnh (context / 맥락) ngoài.

Sau đó thay vật lý (physical / 물리적) DOM placement/stacking kiến trúc (architecture / 아키텍처) phù hợp.

Đây không phải hiệu năng (performance / 성능) lab trực tiếp, nhưng nó dạy nguyên tắc chung:

```text
đừng tối ưu hoặc sửa dựa trên property folklore;
trace tree/boundary thực tế.
```

---

# 45. hiện vật bản dựng (build artifact / 빌드 산출물) experiment

Profile cục bộ (local / 로컬) dev bản dựng (build / 빌드) và môi trường vận hành (production / 운영 환경) bản dựng (build / 빌드).

Không giả định môi trường vận hành (production / 운영 환경) luôn nhanh hơn.

So:

```text
bundle graph
source maps/debug overhead
minification/tree shaking
runtime flags
code splitting
cache
initialization work
```

Nếu production-specific bug/perf regression xuất hiện, cần artifact-level bằng chứng (evidence / 증거).

---

# 46. One-change quy tắc (rule / 규칙)

Khi benchmark, tránh lần ghi nhận (commit / 커밋) cùng lúc:

```text
virtualization
+ memoization
+ CSS rewrite
+ API pagination
+ image lazy-load
```

Nếu kết quả (result / 결과) tốt hơn, không biết phần nào tạo tác động (effect / 효과).

Thực tế kỹ thuật (engineering / 엔지니어링) đôi khi phải bundle fixes, nhưng học tập (learning / 학습)/research phase nên cô lập variable càng nhiều càng tốt.

---

# 47. hiệu năng (performance / 성능) report template

Mỗi experiment nên có:

```text
Question
Scenario
Environment
Build/artifact
Baseline
Trace observation
Hypothesis
Change
After measurement
Variance / uncertainty
Correctness regression check
Accessibility regression check
Conclusion
Next action
```

Không report chỉ:

```text
Before: slow
After: fast
```

---

# 48. Ví dụ report ngắn

```text
Question:
Why does filtering 5k rows exceed the interaction budget?

Baseline:
Median ~145 ms across 8 local runs.
Main cost: 68–75 ms JS filter/sort, 35–42 ms layout.

Hypothesis:
Repeated full sort and rendering all rows dominate.

Change 1:
Precompute normalized searchable field.

After:
JS cost reduced ~25 ms; layout unchanged.

Change 2:
Virtualize visible rows.

After:
Layout and paint reduced materially; keyboard/a11y behavior retested.

Conclusion:
Two independent bottlenecks existed: compute and rendered-node scale.
Memoization alone would not have solved layout cost.
```

Con số chỉ minh họa format, không phải threshold universal.

---

# 49. hiệu năng (performance / 성능) ngân sách (budget / 예산) phải có đơn vị sở hữu (owner / 오너)

Nếu nhóm (team / 팀) đặt ngân sách (budget / 예산):

```text
filter interaction < X
bundle < Y
layout work < Z
```

phải có đơn vị sở hữu (owner / 오너) và đo lường (measurement / 측정) đường dẫn (path / 경로).

Một ngân sách (budget / 예산) không được đo trong CI/telemetry/profile routine sẽ nhanh chóng thành documentation stale.

Nếu automation không ổn định, ít nhất cần checklist bản phát hành (release / 릴리스)/profile rõ.

---

# 50. Không tối ưu khi không có người dùng (user / 사용자) bài toán (problem / 문제) hoặc hệ thống (system / 시스템) rủi ro (risk / 위험)

Hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) có opportunity chi phí (cost / 비용).

Không phải mọi 5 ms đều cần tối ưu.

Prioritize theo:

```text
user impact
frequency
scale
resource cost
business criticality
regression risk
```

Độ sâu không có nghĩa micro-optimize mọi hàm (function / 함수). Độ sâu là biết **khi nào tối ưu hóa (optimization / 최적화) có bằng chứng đủ mạnh để đáng làm**.

---

# 51. Exit gate

Lab được xem là hoàn thành khi người học có thể đưa ra statement kiểu:

```text
"Interaction lag không đến từ network. Trong 10 run production-like,
main-thread work sau input có median khoảng N ms. Phần lớn đến từ X;
Y gây layout invalidation cho khoảng M nodes. Sau thay đổi Z,
category X giảm rõ so với run variance, trong khi keyboard/focus contract
vẫn pass."
```

thay vì:

```text
"Dùng transform vì GPU nhanh hơn."
```

Hoặc:

```text
"React render nhiều nên thêm memo."
```

Không có dấu vết (trace / 추적)/bằng chứng (evidence / 증거) thì chưa đạt gate.

---

# 52. Bài tập cuối

Chọn một page thật và tạo hai dấu vết (trace / 추적):

## Dấu vết (trace / 추적) A — tương tác (interaction / 상호작용)

Ví dụ filter/tìm kiếm (search / 검색)/open modal.

Bắt buộc tách:

```text
input/event
scripting
style
layout
paint/composite
next useful frame
```


> **Chuyển mạch:** Từ **dấu vết (trace / 추적) A — tương tác (interaction / 상호작용)**, ta sang **dấu vết (trace / 추적) B — tải (load / 로드)/cập nhật (update / 업데이트)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dấu vết (trace / 추적) B — tải (load / 로드)/cập nhật (update / 업데이트)

Ví dụ điều hướng (navigation / 내비게이션) hoặc API dữ liệu (data / 데이터) cập nhật (update / 업데이트).

Bắt buộc tách:

```text
network/resource
parse/execute
state transition
DOM changes
rendering work
artifact/build identity
```

Sau đó chọn **một** bottleneck có bằng chứng (evidence / 증거) mạnh nhất, sửa và remeasure.

Cuối cùng ghi một đoạn post-mortem:

```text
What did I initially assume?
What did the trace actually show?
Which boundary was the real owner?
What regression guard should remain?
```

Nếu câu trả lời ban đầu và bằng chứng (evidence / 증거) khác nhau, đó không phải thất bại. Đó chính là lý do hiệu năng (performance / 성능) profiling tồn tại.


> **Chuyển mạch:** Từ **dấu vết (trace / 추적) B — tải (load / 로드)/cập nhật (update / 업데이트)**, ta sang **Cross-link** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cross-link

- [Request → Pixel → Interaction Trace](./00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md)
- [`../COVERAGE_AUDIT.md`](../COVERAGE_AUDIT.md)
- CSS Master/Supplement cho cascade, bố cục (layout / 레이아웃), paint/composite lập luận (reasoning / 추론).
- JavaScript cấp cao (senior / 시니어)/Master cho vòng lặp sự kiện (event loop / 이벤트 루프), long tác vụ (task / 작업), worker, hiệu năng (performance / 성능) và sản phẩm tạo ra (artifact / 산출물) ranh giới (boundary / 경계).
- React/WebSquare profiling chapter khi cần map trình duyệt (browser / 브라우저) bằng chứng (evidence / 증거) sang framework-specific quyền sở hữu (ownership / 소유권).

> **Bàn giao:** Sau **Cross-link**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 REQUEST TO PIXEL AND INTERACTION TRACE](./00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
