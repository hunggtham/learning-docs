# JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**. Route đi từ heap reachability và ownership → async/concurrency và event loop → performance/memory → security boundaries → architecture, observability và production debugging, để senior code được đánh giá bằng runtime behavior và evidence.

> **Mục tiêu của phần này**: giúp nhà phát triển (developer / 개발자) đã hiểu JavaScript cốt lõi (core / 핵심) có thể chịu trách nhiệm cho mã (code / 코드) môi trường vận hành (production / 운영 환경). cấp cao (senior / 시니어) JavaScript không phải người nhớ nhiều API nhất; cấp cao (senior / 시니어) là người hiểu hành vi thời gian chạy (runtime behavior / 런타임 동작), quản lý vòng đời (lifecycle / 생명주기)/tài nguyên (resource / 자원), kiểm soát async/tính đồng thời (concurrency / 동시성), đo hiệu năng (performance / 성능), thiết kế ranh giới bảo mật (security boundary / 보안 경계), tổ chức kiến trúc (architecture / 아키텍처) và gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경) bằng bằng chứng (evidence / 증거).
>
> Phần này nối trực tiếp từ Intermediate. Những concept như closure, `this`, prototype, Promise, vòng lặp sự kiện (event loop / 이벤트 루프), trạng thái (state / 상태) modeling và patterns được coi là nền tảng đã biết.

---

<!-- VERSION-GUIDE-BEGIN -->
# Phiên bản (version / 버전) và tính tương thích (compatibility / 호환성) ở mức (level / 수준) cấp cao (senior / 시니어): bốn lớp phải tách riêng

Ở mức (level / 수준) cấp cao (senior / 시니어), nói “tính năng (feature / 기능) này là JavaScript mới” là chưa đủ. Bạn phải tách **yearly tiêu chuẩn (standard / 표준) snapshot**, **latest specification/proposal trạng thái (state / 상태)**, **engine hiện thực (implementation / 구현)**, và **triển khai (deployment / 배포) mục tiêu (target / 대상) thực tế**. Snapshot chính thức mới nhất hiện tại là **ECMAScript 2026, ECMA-262 17th edition**, được Ecma International phê duyệt ngày 30 tháng 6 năm 2026. Trong khi đó `tc39.es/ecma262` là tài liệu cập nhật liên tục và có thể chứa cả finished proposals đã Stage 4 sau snapshot gần nhất để chuẩn bị cho yearly snapshot tiếp theo.

Engine như V8, SpiderMonkey và JavaScriptCore có lịch triển khai riêng. Một tính năng (feature / 기능) có thể được engine triển khai trước khi yearly edition được xuất bản, nhưng một Android WebView embedded trong ứng dụng enterprise vẫn có thể không hỗ trợ (support / 지원) nó nhiều năm sau. Vì thế câu hỏi môi trường vận hành (production / 운영 환경) nên là: **tính năng (feature / 기능) đã final chưa; trình duyệt (browser / 브라우저)/nút (node / 노드)/WebView targets của sản phẩm hỗ trợ (support / 지원) đến đâu; bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) có thể transpile/polyfill phần nào; fallback có cần thiết không?**.

MDN thường dùng nhãn **Baseline** để mô tả độ phổ biến trên trình duyệt (browser / 브라우저) hiện đại. Baseline hữu ích hơn ECMAScript year khi đánh giá front-end tính tương thích (compatibility / 호환성), nhưng nó vẫn không thay mục tiêu (target / 대상) ma trận (matrix / 행렬) của sản phẩm. “Baseline 2025” có thể vẫn quá mới đối với thiết bị doanh nghiệp khóa WebView cũ.

Stage của TC39 cũng phải được hiểu chính xác. Stage 3 là candidate đủ chín để hiện thực (implementation / 구현) thử nghiệm rộng hơn. Stage 4 là finished proposal và là dấu mốc để proposal đi vào tiêu chuẩn (standard / 표준) snapshot kế tiếp. Ví dụ **Temporal đạt Stage 4 vào tháng 7 năm 2026**, sau khi ES2026 đã được phê duyệt; vì vậy đừng gọi Temporal là “tính năng (feature / 기능) ES2026” chỉ vì nó hoàn tất trong năm 2026. Hãy gọi nó là post-ES2026 Stage-4/next-snapshot tính năng (feature / 기능) cho đến khi yearly snapshot tương ứng được xuất bản, đồng thời vẫn kiểm tra thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원).

Cấp cao (senior / 시니어) cũng cần phân biệt **transpile cú pháp (syntax / 문법)** với **polyfill thời gian chạy (runtime / 런타임) API**. bản dựng (build / 빌드) công cụ (tool / 도구) có thể rewrite optional chaining thành cú pháp (syntax / 문법) cũ, nhưng một built-in mới như `Promise.withResolvers()` hoặc `RegExp.escape()` cần hiện thực (implementation / 구현)/polyfill tương ứng. Web APIs như Trusted Types, AbortSignal extensions hay Workers còn phụ thuộc nền tảng trình duyệt (browser platform / 브라우저 플랫폼) và không thể được đánh giá chỉ bằng ECMA-262 edition.

Vì vậy phiên bản (version / 버전) notes trong tệp (file / 파일) cấp cao (senior / 시니어) không nhằm biến tài liệu thành changelog. Chúng đánh dấu nơi phiên bản (version / 버전) ảnh hưởng architectural choice, tính tương thích (compatibility / 호환성), bảo mật (security / 보안) hoặc bản dựng (build / 빌드) chiến lược (strategy / 전략). cốt lõi (core / 핵심) ideas như quyền sở hữu (ownership / 소유권), cancellation, bounded tính đồng thời (concurrency / 동시성), khả năng quan sát (observability / 관측 가능성) và thất bại (failure / 실패) modeling vẫn giữ nguyên dù ECMAScript tiếp tục ra yearly releases.
<!-- VERSION-GUIDE-END -->

---

# Chương 1 — JavaScript Engine mô hình tư duy (mental model / 사고 모델)

JavaScript nguồn (source / 소스) không được thực thi theo kiểu “trình duyệt (browser / 브라우저) đọc từng dòng và chạy ngay” một cách đơn giản. Engine như V8, SpiderMonkey hoặc JavaScriptCore parse nguồn (source / 소스), tạo biểu diễn (representation / 표현) nội bộ, thực thi bằng trình thông dịch (interpreter / 인터프리터)/baseline trình biên dịch (compiler / 컴파일러), thu thập thời gian chạy (runtime / 런타임) thông tin (information / 정보) và có thể JIT-optimize những hot paths.

Mô hình tư duy (mental model / 사고 모델) high-level:

```text
Source Code
↓
Parse
↓
Internal Representation / AST-like structures
↓
Baseline execution
↓
Runtime profiling
↓
JIT optimization
↓
Optimized machine code
```

Bạn không cần phụ thuộc vào chi tiết một engine cụ thể. Điều quan trọng là hiểu engine có thể tối ưu mã (code / 코드) dựa trên các giả định (assumptions / 가정들) và có thể deoptimize khi các giả định (assumptions / 가정들) không còn đúng.

### Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Không micro-optimize dựa trên blog “V8 trick” nếu profiler chưa chứng minh hotspot. Stable dữ liệu (data / 데이터) contracts, algorithms đúng và kiến trúc (architecture / 아키텍처) rõ thường cho lợi ích lớn hơn hidden-engine tricks.

---

# Chương 2 — Parsing, startup công việc (work / 작업) và top-level side effects

Khi mô-đun (module / 모듈) được tải (load / 로드), top-level mã (code / 코드) chạy trong quá trình mô-đun (module / 모듈) evaluation.

```js
const index = buildHugeSearchIndex();
```

Nếu `buildHugeSearchIndex()` tốn 500ms, startup bị chậm dù tính năng (feature / 기능) chưa dùng chỉ mục (index / 인덱스).

Lazy initialization:

```js
let index;

function getIndex() {
  index ??= buildHugeSearchIndex();
  return index;
}
```

Sự đánh đổi (trade-off / 트레이드오프) là chuyển chi phí (cost / 비용) từ startup sang first-use.

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — Lazy Initialization

Lazy init tốt khi tài nguyên (resource / 자원) expensive và có thể không được dùng. Nhưng nếu người dùng (user / 사용자) chắc chắn cần ngay sau startup, lazy chỉ dời độ trễ (latency / 지연 시간) sang tương tác (interaction / 상호작용) đầu tiên. cấp cao (senior / 시니어) phải tối ưu theo UX đường dẫn (path / 경로), không theo chỉ số (metric / 지표) đơn lẻ.

---

# Chương 3 — JIT, Shapes và predictable dữ liệu (data / 데이터)

Hiện đại (modern / 현대적) engines thường optimize đối tượng (object / 객체) truy cập (access / 접근) dựa trên nội bộ (internal / 내부) shapes/hidden-class-like structures. Bạn không cần biết tên nội bộ (internal / 내부) chính xác của từng engine, nhưng cần hiểu đối tượng (object / 객체) được xây nhất quán thường dễ optimize hơn đối tượng (object / 객체) thay shape ngẫu nhiên.

Consistent factory:

```js
function createUser(id, name) {
  return {
    id,
    name,
    active: true
  };
}
```

Thay vì nhiều lời gọi (call / 호출) sites tạo cùng ngữ nghĩa (semantic / 의미적) đối tượng (object / 객체) với thuộc tính (property / 속성) thứ tự (order / 순서)/shape khác nhau và types thay đổi liên tục.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Stable shape là lợi ích phụ. Lý do chính vẫn là đặc tả hợp đồng (contract / 계약) rõ, dễ maintain và dễ validate. Không reorder properties chỉ để chase microbenchmark.

---

# Chương 4 — Inline bộ nhớ đệm (cache / 캐시) và megamorphic call-sites ở mức khái niệm

Thuộc tính (property / 속성) truy cập (access / 접근) `user.name` xảy ra hàng triệu lần trong app. Engine có thể bộ nhớ đệm (cache / 캐시) lookup chiến lược (strategy / 전략) dựa trên observed shapes. Nếu một call-site luôn nhận cùng shape, tối ưu hóa (optimization / 최적화) dễ hơn. Nếu nhận rất nhiều đối tượng (object / 객체) shapes không liên quan, engine có thể fallback sang generic đường dẫn (path / 경로).

Takeaway không phải “tránh polymorphism”. Takeaway là nếu một hàm (function / 함수) nhận 20 kinds of unrelated objects, kiến trúc (architecture / 아키텍처)/dữ liệu (data / 데이터) modeling có thể đã quá broad. Fix thiết kế (design / 설계) trước khi nghĩ JIT.

---

# Chương 5 — Deoptimization và nguyên tắc profile-before-optimize

Optimized các giả định (assumptions / 가정들) có thể bị invalidated khi types/shapes/prototype hành vi (behavior / 동작) thay đổi. Nhưng deopt là hiện thực (implementation / 구현) detail. môi trường vận hành (production / 운영 환경) tối ưu hóa (optimization / 최적화) phải theo quy trình:

```text
measure
↓
identify hotspot
↓
form hypothesis
↓
change
↓
measure again
```

Nếu mã (code / 코드) unreadable hơn để tiết kiệm vài nanoseconds ở đường dẫn (path / 경로) không quan trọng, đó là tối ưu hóa (optimization / 최적화) sai.

---

# Chương 6 — bộ nhớ (memory / 메모리) mô hình (model / 모델) và Reachability

Garbage Collector không biết “nhà phát triển (developer / 개발자) không còn cần đối tượng (object / 객체)”. Nó chỉ biết đối tượng (object / 객체) còn reachable từ roots hay không. Roots có thể gồm toàn cục (global / 전역) references, ngăn xếp lời gọi (call stack / 호출 스택), active closures, DOM/thời gian chạy (runtime / 런타임) references, callbacks và các host resources.

```js
let user = {
  id: 1,
  hugeData: new Array(1_000_000)
};

user = null;
```

Nếu không còn tham chiếu (reference / 참조) khác, đối tượng (object / 객체) có thể trở thành collectible. Nhưng GC timing không deterministic.

## Hãy hình dung vùng nhớ động (heap / 힙) như một đồ thị (graph / 그래프) reachability

Thay vì nghĩ “biến hết phạm vi (scope / 범위) thì đối tượng (object / 객체) bị xóa”, hãy hình dung đối tượng (object / 객체) trên vùng nhớ động (heap / 힙) tạo thành đồ thị (graph / 그래프) references:

```text
GC roots
  ↓
global/module state
  ↓
store/cache/listener
  ↓
closure
  ↓
large object graph
```

Nếu vẫn còn bất kỳ strong-reference đường dẫn (path / 경로) nào từ gốc (root / 루트) đến đối tượng (object / 객체), đối tượng (object / 객체) chưa collectible. Khi mọi đường dẫn (path / 경로) bị cắt, đối tượng (object / 객체) có thể được GC thu hồi vào một thời điểm engine lựa chọn.

Circular references tự chúng **không phải bộ nhớ (memory / 메모리) leak**:

```js
let a = {};
let b = {};

a.other = b;
b.other = a;

a = null;
b = null;
```

Hai đối tượng (object / 객체) vẫn tham chiếu (reference / 참조) nhau nhưng nếu không còn đường dẫn (path / 경로) từ GC roots tới cycle, tracing GC có thể collect cả cycle. Đây là khác biệt với reference-counting mô hình (model / 모델) đơn giản mà người mới thường hình dung.

> **Nối mạch:** Trong **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, sau nội dung của **Hãy hình dung vùng nhớ động (heap / 힙) như một đồ thị (graph / 그래프) reachability**, **Strong tham chiếu (reference / 참조) thường đến từ quyền sở hữu (ownership / 소유권) bị quên** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Closure retention phải được nhìn theo retainer đường dẫn (path / 경로)** mở rộng hệ quả hoặc giới hạn liên quan.

## Strong tham chiếu (reference / 참조) thường đến từ quyền sở hữu (ownership / 소유권) bị quên

Ví dụ toàn cục (global / 전역) Map:

```js
const cache = new Map();

function remember(user) {
  cache.set(user.id, user);
}
```

Nếu bộ nhớ đệm (cache / 캐시) không có eviction, mỗi người dùng (user / 사용자) được thêm vào có thể sống cho thời gian tồn tại (lifetime / 수명) của page. Đây không phải “GC không chạy”; app vẫn cố ý giữ strong tham chiếu (reference / 참조) trong Map.

Tương tự, DOM nút (node / 노드) có thể đã remove khỏi document nhưng vẫn sống nếu JavaScript còn giữ tham chiếu (reference / 참조):

```js
const node = document.querySelector("#panel");
node.remove();

// node vẫn reachable qua binding node
```

Detached DOM chỉ thành leak khi tham chiếu (reference / 참조) sống lâu hơn intended vòng đời (lifecycle / 생명주기).

> **Nối mạch:** Ở chặng này của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Strong tham chiếu (reference / 참조) thường đến từ quyền sở hữu (ownership / 소유권) bị quên** đặt đầu vào cho **Closure retention phải được nhìn theo retainer đường dẫn (path / 경로)**, rồi **Allocation tỷ lệ (rate / 비율) cũng là hiệu năng (performance / 성능) tín hiệu (signal / 신호)** mở rộng hệ quả hoặc giới hạn liên quan.

## Closure retention phải được nhìn theo retainer đường dẫn (path / 경로)

Closure có thể giữ bindings, nhưng không nên kết luận “closure = leak”. Câu hỏi đúng là:

```text
Closure nào còn reachable?
Ai giữ callback đó?
Callback cần giữ object nào?
Owner có cleanup đúng lifecycle không?
```

Ví dụ listener trên `window` thường có thời gian tồn tại (lifetime / 수명) page-wide, nên callback attached vào đó có thể giữ page/thành phần (component / 컴포넌트) dữ liệu (data / 데이터) nếu không remove khi thành phần (component / 컴포넌트)/page lô-gic (logic / 논리) kết thúc.

### Cấp cao (senior / 시니어) mô hình tư duy (mental model / 사고 모델)

Bộ nhớ (memory / 메모리) leak trong garbage-collected ngôn ngữ (language / 언어) thường là **accidental reachability**: đối tượng (object / 객체) vẫn còn một đường tham chiếu (reference / 참조) từ gốc (root / 루트) dù nghiệp vụ (business / 비즈니스) đã “không dùng nữa”.

---

# Chương 7 — Garbage Collection: điều cần biết và điều không nên đoán

Hiện đại (modern / 현대적) engines có generational/incremental/concurrent strategies khác nhau. Bạn không cần thuộc thuật toán GC cụ thể để viết ứng dụng (application / 애플리케이션) mã (code / 코드) tốt.

Bạn cần biết ba điều: allocation có chi phí (cost / 비용), GC có chi phí (cost / 비용), và timing GC không phải Đặc tả API (API contract / API 계약). Không viết lô-gic (logic / 논리) kiểu “đặt tham chiếu (reference / 참조) null rồi GC chắc chắn chạy trong 2 giây”. Không dùng finalizer để đảm bảo nghiệp vụ (business / 비즈니스) cleanup.

> **Nối mạch:** Đặt trong câu hỏi lớn của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Closure retention phải được nhìn theo retainer đường dẫn (path / 경로)** đặt đầu vào cho **Allocation tỷ lệ (rate / 비율) cũng là hiệu năng (performance / 성능) tín hiệu (signal / 신호)**, rồi **Leak diagnosis: tìm “ai đang giữ nó”, không đoán từ đối tượng (object / 객체) kích thước (size / 크기)** mở rộng hệ quả hoặc giới hạn liên quan.

## Allocation tỷ lệ (rate / 비율) cũng là hiệu năng (performance / 성능) tín hiệu (signal / 신호)

Ngay cả khi không leak, mã (code / 코드) tạo lượng lớn temporary objects/arrays/strings có thể tăng GC pressure:

```js
function process(rows) {
  return rows
    .map(expensiveMap)
    .filter(expensiveFilter)
    .map(expensiveNormalize);
}
```

Mã (code / 코드) có thể hoàn toàn đúng, nhưng trên dataset lớn nó tạo intermediate arrays. Không nên lập tức rewrite thành vòng lặp (loop / 루프) vì “vòng lặp (loop / 루프) nhanh hơn”; hãy profile allocation/CPU trước. Nếu hotspot thực sự nằm ở chuỗi xử lý (pipeline / 파이프라인) này, bạn mới cân nhắc lazy iteration, fused vòng lặp (loop / 루프), worker hoặc thuật toán (algorithm / 알고리즘) khác.

GC pause/overhead là **hậu quả của tải công việc (workload / 워크로드)/allocation/reachability**, không phải thứ nên optimize bằng superstition.

---

# Chương 8 — bộ nhớ (memory / 메모리) Leaks phổ biến trong frontend

Các leak phổ biến gồm sự kiện (event / 이벤트) listener không remove, timer không clear, subscription không unsubscribe, Map/bộ nhớ đệm (cache / 캐시) tăng vô hạn, detached DOM còn tham chiếu (reference / 참조), Worker không terminate, WebSocket không close, closure giữ dữ liệu (data / 데이터) lớn, pending async vòng đời (lifecycle / 생명주기) tiếp tục giữ references.

Listener leak:

```js
function mount() {
  window.addEventListener(
    "resize",
    handleResize
  );
}
```

Nếu mount nhiều lần mà không cleanup:

```js
function unmount() {
  window.removeEventListener(
    "resize",
    handleResize
  );
}
```

Timer:

```js
const intervalId = setInterval(
  refresh,
  5000
);
```

cleanup:

```js
clearInterval(intervalId);
```

> **Nối mạch:** Allocation rate là performance signal; leak diagnosis tiếp theo truy nguyên retaining path thay vì suy đoán từ object size. Pending async work mở rộng diagnosis sang stale lifecycle và cancellation.

## Leak diagnosis: tìm “ai đang giữ nó”, không đoán từ đối tượng (object / 객체) kích thước (size / 크기)

Một workflow thực tế với DevTools bộ nhớ (memory / 메모리):

```text
1. Reproduce lifecycle nhiều lần
   open → close → open → close

2. Force/observe GC khi tooling cho phép

3. Chụp heap snapshots hoặc allocation profile

4. Tìm object/DOM nodes tăng sau mỗi cycle

5. Xem Retainers / retaining path

6. Tìm owner thật: listener, cache, closure, timer, subscription, framework registry...

7. Fix ownership/cleanup

8. Re-run cùng scenario
```

Nếu vùng nhớ động (heap / 힙) tăng trong lúc tính năng (feature / 기능) hoạt động rồi giảm sau GC/vòng đời (lifecycle / 생명주기) cleanup, đó có thể chỉ là normal allocation. Leak thường thể hiện **baseline retained bộ nhớ (memory / 메모리) tăng qua những vòng đời (lifecycle / 생명주기) lặp lại**.

> **Nối mạch:** Ở chặng này của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Leak diagnosis: tìm “ai đang giữ nó”, không đoán từ đối tượng (object / 객체) kích thước (size / 크기)** đặt đầu vào cho **Pending async công việc (work / 작업) và stale vòng đời (lifecycle / 생명주기)**, rồi **Trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) là JavaScript engine + host môi trường (environment / 환경)** mở rộng hệ quả hoặc giới hạn liên quan.

## Pending async công việc (work / 작업) và stale vòng đời (lifecycle / 생명주기)

Yêu cầu (request / 요청) pending không phải tự động leak vĩnh viễn. Nhưng nếu page/thành phần (component / 컴포넌트) bị destroy trong khi callback giữ references rồi một registry/controller khác vẫn giữ thao tác (operation / 연산), dữ liệu (data / 데이터) có thể sống lâu không cần thiết. Cancellation vừa cải thiện tính đúng đắn (correctness / 정확성), vừa có thể rút ngắn tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명).

```js
const controller = new AbortController();

loadLargeData({
  signal: controller.signal
});

// khi owner bị destroy
controller.abort();
```

### Cấp cao (senior / 시니어) mẫu (pattern / 패턴) — tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권)

Ai tạo tài nguyên (resource / 자원) phải biết ai sở hữu và khi nào bản phát hành (release / 릴리스). vòng đời (lifecycle / 생명주기) không nên phụ thuộc vào “nhà phát triển (developer / 개발자) nhớ cleanup”. API tốt làm cleanup đường dẫn (path / 경로) tường minh (explicit / 명시적).

---

# Chương 9 — WeakRef, FinalizationRegistry và vì sao chúng là niche tools

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2021:** `WeakRef` và `FinalizationRegistry` được chuẩn hóa ở ES2021, mới hơn nhiều so với WeakMap/WeakSet ES2015. hỗ trợ (support / 지원) không phải lý do để dùng chúng; tính đúng đắn (correctness / 정확성) vẫn không được phụ thuộc vào thời điểm GC/finalizer.

`WeakRef` cho phép giữ weak tham chiếu (reference / 참조):

```js
const ref = new WeakRef(object);
const value = ref.deref();
```

Giá trị (value / 값) có thể là đối tượng (object / 객체) hoặc `undefined` nếu đối tượng (object / 객체) đã bị GC.

`FinalizationRegistry` có thể nhận notification khi đối tượng (object / 객체) được collected, nhưng timing không guarantee. Nó không phù hợp để bản phát hành (release / 릴리스) trọng yếu (critical / 중요) khóa (lock / 잠금), payment trạng thái (state / 상태) hay tài nguyên (resource / 자원) cần deterministic cleanup.

### Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Nếu nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성) phụ thuộc đối tượng (object / 객체) “chắc còn sống” hoặc finalizer “chắc chạy”, thiết kế (design / 설계) sai. Weak references chỉ phù hợp cho optional bộ nhớ đệm (cache / 캐시)/metadata-like scenarios nơi absence vẫn hợp lệ.

---

# Chương 10 — tường minh (explicit / 명시적) tài nguyên (resource / 자원) Management và deterministic cleanup

> **phiên bản (version / 버전)/proposal ghi chú (note / 노트):** tường minh (explicit / 명시적) tài nguyên (resource / 자원) Management (`using`, `await using`, `Symbol.dispose`, `DisposableStack`...) là nhóm tính năng (feature / 기능) rất mới. Trước khi dùng môi trường vận hành (production / 운영 환경), hãy kiểm tra snapshot/proposal status hiện hành và trình duyệt (browser / 브라우저)/thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원), đặc biệt với WebView. Đừng đánh đồng Stage 4/post-snapshot với universal availability.

JavaScript hiện đại có tường minh (explicit / 명시적) resource-management concepts như `using`, `await using`, `Symbol.dispose`, `Symbol.asyncDispose`, `DisposableStack` và `AsyncDisposableStack` ở runtimes hỗ trợ.

Concept:

```js
{
  using resource = acquireResource();
  // use resource
}
// resource disposed at scope exit
```

Custom disposable:

```js
class Subscription {
  constructor(unsubscribe) {
    this.unsubscribe = unsubscribe;
  }

  [Symbol.dispose]() {
    this.unsubscribe();
  }
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Tính năng (feature / 기능) này giúp deterministic cleanup nhưng không thay thế quyền sở hữu (ownership / 소유권) thiết kế (design / 설계). Trong trình duyệt (browser / 브라우저)/WebView enterprise cũ, luôn check thời gian chạy (runtime / 런타임)/toolchain tính tương thích (compatibility / 호환성) trước khi áp dụng cú pháp (syntax / 문법) mới.

---

# Chương 11 — vòng lặp sự kiện (event loop / 이벤트 루프) sâu hơn và rendering opportunities

Trình duyệt (browser / 브라우저) vòng lặp sự kiện (event loop / 이벤트 루프) phối hợp tasks, microtasks và rendering. Simplified mô hình tư duy (mental model / 사고 모델):

```text
run a task
↓
run synchronous JS
↓
drain microtasks
↓
rendering opportunity
↓
next task
```

Nếu một tác vụ (task / 작업) chạy 300ms synchronous, trình duyệt (browser / 브라우저) không thể phản hồi đầu vào (input / 입력)/kết xuất (render / 렌더링) mượt trong thời gian đó.

```js
const start = performance.now();

while (
  performance.now() - start < 300
) {
}
```

Kết quả (result / 결과) có thể là đầu vào (input / 입력) lag và animation freeze.

> **Nối mạch:** Đặt trong câu hỏi lớn của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Pending async công việc (work / 작업) và stale vòng đời (lifecycle / 생명주기)** đặt đầu vào cho **Trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) là JavaScript engine + host môi trường (environment / 환경)**, rồi **Main luồng thực thi (thread / 스레드) là dùng chung (shared / 공유) tài nguyên (resource / 자원) của UI** mở rộng hệ quả hoặc giới hạn liên quan.

## Trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) là JavaScript engine + host môi trường (environment / 환경)

Để gỡ lỗi (debug / 디버그) frontend ở mức (level / 수준) cấp cao (senior / 시니어), hãy tách các tầng (layer / 계층):

```text
ECMAScript language
  values / functions / Promise / modules

JavaScript engine
  parser / interpreter / JIT / GC

Web platform host
  DOM / timers / fetch / events / storage / workers

Browser rendering/network processes
  style / layout / paint / composite / network stack

Application/framework
  React / WebSquare / your modules
```

`setTimeout`, `fetch`, DOM events và `requestAnimationFrame` không phải magic bên trong ECMAScript engine. trình duyệt (browser / 브라우저) host đăng ký công việc (work / 작업), nhận OS/mạng (network / 네트워크)/đầu vào (input / 입력) signals và sau đó đưa callbacks/continuations trở lại mô hình thực thi (execution model / 실행 모델) theo web-platform rules.

Điều này giúp phân loại lỗi. Ví dụ:

```text
SyntaxError khi parse
→ language/parser

Long synchronous loop
→ JS main-thread execution

Fetch 500
→ network/server contract

Layout thrashing
→ rendering pipeline interaction

WebView thiếu API
→ host/runtime compatibility
```

> **Nối mạch:** Trong **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) là JavaScript engine + host môi trường (environment / 환경)** đặt vấn đề; **Main luồng thực thi (thread / 스레드) là dùng chung (shared / 공유) tài nguyên (resource / 자원) của UI** đối chiếu bằng chứng, rồi **Fetch không “chạy JavaScript trên mạng (network / 네트워크) luồng thực thi (thread / 스레드)” theo cách ứng dụng (application / 애플리케이션) cần quản lý** mở rộng hệ quả hoặc giới hạn liên quan.

## Main luồng thực thi (thread / 스레드) là dùng chung (shared / 공유) tài nguyên (resource / 자원) của UI

Trong trình duyệt (browser / 브라우저) page thông thường, nhiều việc cạnh tranh main luồng thực thi (thread / 스레드):

```text
JavaScript task
DOM event handlers
style/layout work
paint preparation
some browser callbacks
```

Vì vậy “hàm (function / 함수) chỉ mất 30ms” không thể đánh giá riêng nếu nó chạy liên tục trên đầu vào (input / 입력) đường dẫn (path / 경로) hoặc nằm giữa nhiều tasks khác. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) phải nhìn entire người dùng (user / 사용자) tương tác (interaction / 상호작용).

> **Nối mạch:** Ở chặng này của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Main luồng thực thi (thread / 스레드) là dùng chung (shared / 공유) tài nguyên (resource / 자원) của UI** đặt vấn đề; **Fetch không “chạy JavaScript trên mạng (network / 네트워크) luồng thực thi (thread / 스레드)” theo cách ứng dụng (application / 애플리케이션) cần quản lý** đối chiếu bằng chứng, rồi **Lab profile và Real người dùng (user / 사용자) Monitoring trả lời hai câu hỏi khác nhau** mở rộng hệ quả hoặc giới hạn liên quan.

## Fetch không “chạy JavaScript trên mạng (network / 네트워크) luồng thực thi (thread / 스레드)” theo cách ứng dụng (application / 애플리케이션) cần quản lý

Khi gọi:

```js
const response = await fetch(url);
```

Trình duyệt (browser / 브라우저) mạng (network / 네트워크) ngăn xếp (stack / 스택) làm mạng (network / 네트워크) I/O ngoài JS ngăn xếp lời gọi (call stack / 호출 스택). Nhưng khi Promise continuation của `await` chạy, JavaScript của bạn lại cần thực thi (execution / 실행) opportunity. JSON parsing lớn, ánh xạ (mapping / 매핑) lớn và rendering sau phản hồi (response / 응답) vẫn có thể khối (block / 블록) main luồng thực thi (thread / 스레드).

```js
const data = await response.json();
const normalized = expensiveNormalize(data);
render(normalized);
```

Mạng (network / 네트워크) async không đồng nghĩa post-processing async/non-blocking.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

`async function` không tự làm CPU-heavy vòng lặp (loop / 루프) non-blocking. Nếu computation synchronous nằm trong async hàm (function / 함수), nó vẫn khối (block / 블록) main luồng thực thi (thread / 스레드) cho tới khi mã (code / 코드) yield.

---

# Chương 12 — Long Tasks và chunking

Giả sử xử lý 100.000 records:

```js
for (const item of hugeData) {
  expensiveProcess(item);
}
```

Nếu tác vụ (task / 작업) quá dài, UI freeze. Các chiến lược (strategy / 전략) gồm thuật toán (algorithm / 알고리즘) improvement, chunking, Web Worker, lazy processing hoặc virtualization.

Illustrative chunking:

```js
async function processInChunks(
  items,
  chunkSize = 100
) {
  for (
    let i = 0;
    i < items.length;
    i += chunkSize
  ) {
    processChunk(
      items.slice(
        i,
        i + chunkSize
      )
    );

    await new Promise(
      (resolve) =>
        setTimeout(resolve, 0)
    );
  }
}
```

Đây chỉ là chiến lược (strategy / 전략) minh họa; scheduling môi trường vận hành (production / 운영 환경) cần cân nhắc UX, tác vụ (task / 작업) priorities và available APIs.

---

# Chương 13 — Main-thread ngân sách (budget / 예산) và hiệu năng (performance / 성능) thinking

Cấp cao (senior / 시니어) không chỉ nhìn Big-O. Một O(n) vòng lặp (loop / 루프) vẫn có thể chậm nếu n lớn và mỗi iteration expensive. Câu hỏi phải là: n bao nhiêu, chạy khi nào, trên thiết bị (device / 장치) nào, có đang khối (block / 블록) đầu vào (input / 입력) không, có thể precompute/worker/lazy không?

Hiệu năng (performance / 성능) là tương tác (interaction / 상호작용) giữa thuật toán (algorithm / 알고리즘), tải công việc (workload / 워크로드), thiết bị (device / 장치) và scheduling.

---

# Chương 14 — `requestAnimationFrame` và visual scheduling

`requestAnimationFrame` schedule callback cho visual cập nhật (update / 업데이트) trước rendering opportunity phù hợp.

```js
function animate() {
  position += velocity;

  element.style.transform =
    `translateX(${position}px)`;

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

Animation lô-gic (logic / 논리) nên dùng elapsed thời gian (time / 시간) nếu cần consistency giữa displays/frame rates.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

`rAF` không phải chính xác (exact / 정확한) 16.67ms timer. Background tabs bị throttle và refresh tỷ lệ (rate / 비율) thiết bị khác nhau.

---

# Chương 15 — Web Workers: chuyển CPU công việc (work / 작업) khỏi main luồng thực thi (thread / 스레드)

Worker chạy JavaScript ở luồng thực thi (thread / 스레드) riêng và không truy cập (access / 접근) DOM trực tiếp.

Main:

```js
const worker = new Worker(
  "./worker.js",
  {
    type: "module"
  }
);

worker.postMessage({
  type: "PROCESS",
  payload: data
});

worker.onmessage = (event) => {
  render(event.data);
};
```

Worker:

```js
self.onmessage = (event) => {
  const result = expensiveCompute(
    event.data.payload
  );

  self.postMessage(result);
};
```

Worker phù hợp CPU-heavy parsing, tìm kiếm (search / 검색)/indexing, ảnh (image / 이미지)/dữ liệu (data / 데이터) processing. Nó không làm mạng (network / 네트워크) fetch “nhanh hơn” chỉ vì ở luồng thực thi (thread / 스레드) khác.

### Trade-offs

Worker startup, message serialization và bộ nhớ (memory / 메모리) duplication có chi phí (cost / 비용). Không spawn worker cho tiny thao tác (operation / 연산).

---

# Chương 16 — Structured Clone và Transferable Objects

> **phiên bản (version / 버전) ghi chú (note / 노트):** Structured clone là web/nền tảng (platform / 플랫폼) thuật toán (algorithm / 알고리즘) đã tồn tại lâu; ES2024 chuẩn hóa thêm các resizable/transfer-related ArrayBuffer facilities ở ngôn ngữ (language / 언어) built-ins. `structuredClone()` bản thân có tính tương thích (compatibility / 호환성) timeline của host/toàn cục (global / 전역) API, nên không nên gán toàn chương này cho một ES year duy nhất.

`structuredClone()` clone nhiều JavaScript types tốt hơn JSON và hỗ trợ cycles.

```js
const copy = structuredClone(original);
```

Khi chuyển large nhị phân (binary / 이진) dữ liệu (data / 데이터) giữa worker/main, bản sao (copy / 복사) có thể expensive. Một số objects như ArrayBuffer có thể transfer quyền sở hữu (ownership / 소유권):

```js
worker.postMessage(
  { buffer },
  [buffer]
);
```

Sau transfer, original buffer có thể bị detached.

### Cấp cao (senior / 시니어) mẫu (pattern / 패턴) — Move instead of bản sao (copy / 복사)

Useful cho large nhị phân (binary / 이진) payload/ảnh (image / 이미지)/dữ liệu (data / 데이터) processing. Nhưng quyền sở hữu (ownership / 소유권) sau transfer phải rõ.

---

# Chương 17 — SharedArrayBuffer và Atomics: khi message passing không đủ

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2017 cốt lõi (core / 핵심):** dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và Atomics được đưa vào ES2017. Trên web, `SharedArrayBuffer` còn chịu bảo mật (security / 보안)/cross-origin-isolation requirements của nền tảng Web (web platform / 웹 플랫폼); “nằm trong ECMAScript” chưa đủ để kết luận triển khai (deployment / 배포) dùng được.

`SharedArrayBuffer` cho nhiều agents/workers truy cập (access / 접근) cùng bộ nhớ (memory / 메모리). Điều này mở ra race conditions và memory-ordering độ phức tạp (complexity / 복잡도).

```js
const buffer = new SharedArrayBuffer(4);
const view = new Int32Array(buffer);

Atomics.add(view, 0, 1);
```

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) chỉ nên dùng khi hiệu năng (performance / 성능) use trường hợp (case / 사례) thật sự cần. Với phần lớn frontend, message passing dễ lập luận (reasoning / 추론) và an toàn hơn.

### Bảo mật (security / 보안)/nền tảng (platform / 플랫폼) ghi chú (note / 노트)

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) trên web còn liên quan cross-origin isolation requirements trong nhiều scenarios.

---

# Chương 18 — Streams và vì sao tải (load / 로드) toàn bộ dữ liệu (data / 데이터) trước không luôn tốt

Streams xử lý dữ liệu (data / 데이터) theo chunks.

```js
const response = await fetch(url);
const reader = response.body.getReader();

while (true) {
  const { value, done } = await reader.read();

  if (done) {
    break;
  }

  processChunk(value);
}
```

Benefits: lower peak bộ nhớ (memory / 메모리), progressive processing và độ trễ (latency / 지연 시간) tốt hơn cho large payloads.

Web Streams có `ReadableStream`, `WritableStream`, `TransformStream`. cấp cao (senior / 시니어) cần hiểu producer/bên tiêu thụ (consumer / 소비자) relationship và backpressure.

---

# Chương 19 — Backpressure

Backpressure xảy ra khi producer tạo dữ liệu (data / 데이터) nhanh hơn bên tiêu thụ (consumer / 소비자) xử lý. Nếu hàng đợi (queue / 큐) cứ tăng:

```text
memory tăng
latency tăng
GC pressure tăng
```

Stream APIs có cơ chế (mechanism / 메커니즘) để bên tiêu thụ (consumer / 소비자) tín hiệu (signal / 신호) pace. Cùng concept xuất hiện trong sự kiện (event / 이벤트) queues, mạng (network / 네트워크) pipelines và background jobs.

### Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Unbounded hàng đợi (queue / 큐) là một dạng bộ nhớ (memory / 메모리) leak có lô-gic (logic / 논리). Mọi thứ có thể tăng mãi — hàng đợi (queue / 큐), bộ nhớ đệm (cache / 캐시), thử lại (retry / 재시도), tính đồng thời (concurrency / 동시성), logs — cần ranh giới (boundary / 경계).

---

# Chương 20 — Async Iterators và streaming abstractions

Async generator có thể mô hình (model / 모델) paginated/streaming nguồn (source / 소스):

```js
async function* pages() {
  let page = 1;

  while (true) {
    const result = await loadPage(page);

    if (result.items.length === 0) {
      return;
    }

    yield result.items;
    page += 1;
  }
}
```

Bên tiêu thụ (consumer / 소비자):

```js
for await (const items of pages()) {
  process(items);
}
```

Async iteration cho bên tiêu thụ (consumer / 소비자) kiểm soát pace tốt hơn một API push vô hạn.

---

# Chương 21 — Bounded tính đồng thời (concurrency / 동시성)

Đây là distinction rất quan trọng. `Promise.all(items.map(apiCall))` start toàn bộ operations gần như cùng lúc. Với 50.000 items, bạn có thể tạo 50.000 requests/tasks.

Cần tính đồng thời (concurrency / 동시성) limit:

```js
async function mapLimit(
  items,
  limit,
  worker
) {
  const results = new Array(
    items.length
  );

  let nextIndex = 0;

  async function run() {
    while (true) {
      const index = nextIndex;
      nextIndex += 1;

      if (index >= items.length) {
        return;
      }

      results[index] = await worker(
        items[index],
        index
      );
    }
  }

  const workers = Array.from(
    {
      length: Math.min(
        limit,
        items.length
      )
    },
    run
  );

  await Promise.all(workers);
  return results;
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Tính đồng thời (concurrency / 동시성) limit khác tỷ lệ (rate / 비율) limit. More tính đồng thời (concurrency / 동시성) không luôn faster; máy chủ (server / 서버)/mạng (network / 네트워크)/tài nguyên (resource / 자원) bottleneck quyết định optimum.

---

# Chương 22 — Cancellation kiến trúc (architecture / 아키텍처)

Cancellation nên đi xuyên lớp trừu tượng (abstraction / 추상화) layers thay vì dịch vụ (service / 서비스) tự giữ hidden cancellation trạng thái (state / 상태) nếu caller mới là đơn vị sở hữu (owner / 오너) vòng đời (lifecycle / 생명주기).

```js
async function loadUser(
  id,
  { signal } = {}
) {
  const response = await fetch(
    `/api/users/${id}`,
    { signal }
  );

  return response.json();
}
```

Caller:

```js
const controller = new AbortController();

loadUser(1, {
  signal: controller.signal
});

controller.abort();
```

### Composition

Hiện đại (modern / 현대적) AbortSignal APIs có thể compose hết thời gian chờ (timeout / 타임아웃)/manual cancellation ở runtimes hỗ trợ. Dù API cụ thể nào, kiến trúc (architecture / 아키텍처) principle vẫn là caller sở hữu thời gian tồn tại (lifetime / 수명) và downstream nhận tín hiệu (signal / 신호).

---

# Chương 23 — Debounce và Throttle

Debounce đợi sự kiện (event / 이벤트) im lặng một khoảng thời gian rồi chạy. tìm kiếm (search / 검색) đầu vào (input / 입력) là example điển hình.

```js
function debounce(fn, delay) {
  let timeoutId;

  return (...args) => {
    clearTimeout(timeoutId);

    timeoutId = setTimeout(
      () => fn(...args),
      delay
    );
  };
}
```

Throttle giới hạn tần suất chạy, ví dụ scroll/mousemove.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Môi trường vận hành (production / 운영 환경) debounce có thể cần leading/trailing/cancel/flush/maxWait. Nếu ngăn xếp (stack / 스택) đã có hiện thực (implementation / 구현) mature, đừng tự viết bản phức tạp rồi tạo subtle bug.

---

# Chương 24 — thử lại (retry / 재시도), Exponential Backoff và Jitter

Naive thử lại (retry / 재시도) ngay lập tức có thể làm máy chủ (server / 서버) đang overload càng overload. Exponential backoff tăng delay:

```text
300ms
600ms
1200ms
2400ms
```

Jitter thêm randomness để hàng nghìn clients không thử lại (retry / 재시도) đồng bộ.

```js
const delay =
  baseDelay * 2 ** attempt;

const jitter =
  Math.random() * delay * 0.25;
```

### Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Thử lại (retry / 재시도) chỉ cho transient/retryable failures. Respect máy chủ (server / 서버) hints như `Retry-After` khi đặc tả hợp đồng (contract / 계약) hỗ trợ. thử lại (retry / 재시도) vòng lặp (loop / 루프) cũng phải cancellable.

---

# Chương 25 — Idempotency và vì sao thử lại (retry / 재시도) payment rất nguy hiểm

Idempotent thao tác (operation / 연산) có thể repeat mà tác động (effect / 효과) tương đương một lần. GET thường có idempotent intent. Payment creation hoặc transfer không thể blind thử lại (retry / 재시도) nếu máy chủ (server / 서버) có thể đã nhận yêu cầu (request / 요청) nhưng phản hồi (response / 응답) bị mất.

Backend có thể hỗ trợ idempotency key. Frontend thử lại (retry / 재시도) chiến lược (strategy / 전략) phải hiểu endpoint ngữ nghĩa (semantics / 의미론), không chỉ HTTP status.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

“yêu cầu (request / 요청) failed” không luôn có nghĩa “máy chủ (server / 서버) chưa làm gì”. mạng (network / 네트워크) thất bại (failure / 실패) có thể xảy ra sau khi side tác động (effect / 효과) đã lần ghi nhận (commit / 커밋) server-side.

---

# Chương 26 — Circuit Breaker và Bulkhead concepts

Circuit breaker có states như closed/open/half-open. Khi phụ thuộc (dependency / 의존성) thất bại (fail / 실패) liên tục, hệ thống (system / 시스템) thất bại (fail / 실패) fast thay vì tiếp tục hammer phụ thuộc (dependency / 의존성).

Trình duyệt (browser / 브라우저) app ít cần full circuit breaker như backend, nhưng concept hữu ích cho polling/bản địa (native / 네이티브) cầu nối (bridge / 브리지)/third-party SDK.

Bulkhead là thất bại (failure / 실패) isolation: analytics thất bại (failure / 실패) không được khối (block / 블록) payment nếu analytics non-critical; third-party widget lỗi không làm main luồng (flow / 흐름) crash.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Resilience mẫu (pattern / 패턴) chỉ có giá trị nếu match dạng thất bại (failure mode / 실패 모드). Đừng implement circuit breaker để “enterprise-looking”.

---

# Chương 27 — bộ nhớ đệm (cache / 캐시) kiến trúc (architecture / 아키텍처)

Bộ nhớ đệm (cache / 캐시) cần trả lời: bộ nhớ đệm (cache / 캐시) gì, key là gì, TTL bao lâu, vô hiệu hóa (invalidation / 무효화) khi nào, max kích thước (size / 크기) bao nhiêu, stale dữ liệu (data / 데이터) có acceptable không, nguồn chuẩn (source of truth / 정본) ở đâu.

Simple TTL bộ nhớ đệm (cache / 캐시):

```js
function createCache({ ttlMs }) {
  const map = new Map();

  return {
    get(key) {
      const entry = map.get(key);

      if (!entry) {
        return undefined;
      }

      if (
        Date.now() > entry.expiresAt
      ) {
        map.delete(key);
        return undefined;
      }

      return entry.value;
    },

    set(key, value) {
      map.set(key, {
        value,
        expiresAt: Date.now() + ttlMs
      });
    }
  };
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화) là tính đúng đắn (correctness / 정확성) bài toán (problem / 문제), không chỉ hiệu năng (performance / 성능). Với dữ liệu (data / 데이터) nhạy cảm như balance/permission, stale bộ nhớ đệm (cache / 캐시) có thể nguy hiểm.

---

# Chương 28 — Memoization khác bộ nhớ đệm (cache / 캐시) như thế nào?

Memoization thường bộ nhớ đệm (cache / 캐시) pure/deterministic hàm (function / 함수) đầu ra (output / 출력) theo đầu vào (input / 입력). bộ nhớ đệm (cache / 캐시) là concept rộng hơn, có TTL, stale ngữ nghĩa (semantics / 의미론), authorization phạm vi (scope / 범위), source-of-truth concerns.

Đừng gọi mọi Map là “memoization”. mạng (network / 네트워크) bộ nhớ đệm (cache / 캐시) và computed selector bộ nhớ đệm (cache / 캐시) có thất bại (failure / 실패) modes rất khác nhau.

---

# Chương 29 — HTTP bộ nhớ đệm (cache / 캐시) và dùng nền tảng (platform / 플랫폼) trước custom bộ nhớ đệm (cache / 캐시)

Trình duyệt (browser / 브라우저)/HTTP caching có `Cache-Control`, `ETag`, `Last-Modified`, `304`, `max-age`, `no-cache`, `no-store`. Nếu HTTP bộ nhớ đệm (cache / 캐시) đã giải quyết static/tài nguyên (resource / 자원)/dữ liệu (data / 데이터) use trường hợp (case / 사례), custom JS bộ nhớ đệm (cache / 캐시) có thể chỉ thêm độ phức tạp (complexity / 복잡도).

Cấp cao (senior / 시니어) ưu tiên nền tảng (platform / 플랫폼) mechanisms trước khi tự xây bộ nhớ đệm (cache / 캐시) nếu ngữ nghĩa (semantics / 의미론) phù hợp.

---

# Chương 30 — Stale-While-Revalidate concept

SWR-like luồng (flow / 흐름):

```text
show cached/stale data immediately
↓
fetch fresh data
↓
update UI
```

Tốt cho content/profile/danh sách (list / 목록) nơi stale dữ liệu (data / 데이터) ngắn hạn acceptable. Không phù hợp nếu stale permission hoặc giao dịch (transaction / 트랜잭션) balance dẫn tới quyết định sai.

---

# Chương 31 — hiệu năng (performance / 성능) đo lường (measurement / 측정): đo trước khi tối ưu

Dùng `performance.now()` cho duration:

```js
const start = performance.now();
run();
const duration = performance.now() - start;
```

Hiệu năng (performance / 성능) marks:

```js
performance.mark("load-start");

await load();

performance.mark("load-end");

performance.measure(
  "load-duration",
  "load-start",
  "load-end"
);
```

Microbenchmarks dễ bị JIT, GC, warmup và unrealistic tải công việc (workload / 워크로드) làm lệch. User-perceived scenario quan trọng hơn tiny vòng lặp (loop / 루프) benchmark.

> **Nối mạch:** Đặt trong câu hỏi lớn của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Fetch không “chạy JavaScript trên mạng (network / 네트워크) luồng thực thi (thread / 스레드)” theo cách ứng dụng (application / 애플리케이션) cần quản lý** nêu quy tắc; **Lab profile và Real người dùng (user / 사용자) Monitoring trả lời hai câu hỏi khác nhau** thử quy tắc trong tình huống, rồi **Kiểm tra hợp lệ (validation / 검증), encoding và sanitization không phải cùng một việc** mở rộng hệ quả.

## Lab profile và Real người dùng (user / 사용자) Monitoring trả lời hai câu hỏi khác nhau

DevTools/lab giúp bạn reproduce, inspect flame chart, vùng nhớ động (heap / 힙), waterfall trong môi trường kiểm soát. môi trường vận hành (production / 운영 환경) telemetry/RUM cho biết vấn đề có thật trên người dùng (user / 사용자) devices hay không.

Một tối ưu hóa (optimization / 최적화) workflow tốt:

```text
production symptom / UX metric
↓
reproduce representative case
↓
profile CPU / memory / network / rendering
↓
identify dominant cost
↓
change one hypothesis
↓
measure again
↓
watch production regression
```

Đừng tối ưu hàm (function / 함수) vì nó “trông chậm”. hiệu năng (performance / 성능) ngân sách (budget / 예산) nên gắn với người dùng (user / 사용자) tương tác (interaction / 상호작용), ví dụ startup, tìm kiếm (search / 검색) độ trễ (latency / 지연 시간), click-to-render hoặc bộ nhớ (memory / 메모리) sau nhiều điều hướng (navigation / 내비게이션) cycles.

---

# Chương 32 — bố cục (layout / 레이아웃), Paint, Composite và bố cục (layout / 레이아웃) Thrashing

High-level rendering chuỗi xử lý (pipeline / 파이프라인):

```text
style
↓
layout
↓
paint
↓
composite
```

Interleave bố cục (layout / 레이아웃) read/ghi (write / 쓰기):

```js
for (const item of items) {
  const width = item.offsetWidth;
  item.style.width =
    `${width * 2}px`;
}
```

có thể force repeated bố cục (layout / 레이아웃).

Better batch reads:

```js
const widths = items.map(
  (item) => item.offsetWidth
);

for (
  let i = 0;
  i < items.length;
  i += 1
) {
  items[i].style.width =
    `${widths[i] * 2}px`;
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Hiện đại (modern / 현대적) browsers optimize nhiều thứ. Đừng cargo-cult “DOM luôn chậm”; profile realistic page.

---

# Chương 33 — Large DOM và virtualization

Kết xuất (render / 렌더링) 100.000 rows vào DOM thường tạo chi phí (cost / 비용) bố cục (layout / 레이아웃), bộ nhớ (memory / 메모리) và tương tác (interaction / 상호작용). Virtualization chỉ kết xuất (render / 렌더링) visible cửa sổ (window / 윈도우) + buffer.

Concept:

```text
100,000 data rows
↓
viewport cần 30 rows
↓
render khoảng 40-60 rows
```

Đây là kiến trúc (architecture / 아키텍처) tối ưu hóa (optimization / 최적화) lớn hơn micro-optimizing vòng lặp (loop / 루프) cú pháp (syntax / 문법).

---

# Chương 34 — High-frequency events

Events như scroll, resize, pointermove có thể fire rất nhiều. Strategies gồm throttle/debounce, passive listeners khi đúng, rAF cho visual công việc (work / 작업) và delegation.

```js
window.addEventListener(
  "scroll",
  handleScroll,
  {
    passive: true
  }
);
```

`passive: true` nói listener không gọi `preventDefault`; dùng sai sẽ làm hành vi (behavior / 동작) khác.

---

# Chương 35 — mạng (network / 네트워크) hiệu năng (performance / 성능) và yêu cầu (request / 요청) waterfall

Independent requests không nên vô tình chạy sequential:

```js
const a = await loadA();
const b = await loadB();
const c = await loadC();
```

Nếu independent:

```js
const [a, b, c] = await Promise.all([
  loadA(),
  loadB(),
  loadC()
]);
```

Nhưng parallelism cũng cần limit nếu số lượng lớn. mạng (network / 네트워크) hiệu năng (performance / 성능) còn phụ thuộc payload kích thước (size / 크기), compression, caching, duplicate requests, yêu cầu (request / 요청) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và backend độ trễ (latency / 지연 시간).

---

# Chương 36 — Bundle chiến lược (strategy / 전략), mã (code / 코드) Splitting và Lazy Loading

> **phiên bản (version / 버전) ghi chú (note / 노트):** Static modules có nền từ ES2015; động (dynamic / 동적) `import()` thuộc ES2020; import attributes/JSON-module hỗ trợ (support / 지원) thuộc ES2025. mã (code / 코드) splitting và cây (tree / 트리) shaking là build-tool hành vi (behavior / 동작), không phải guarantee trực tiếp của ECMAScript.

Động (dynamic / 동적) import:

```js
const { openEditor } = await import(
  "./editor.js"
);
```

Bundler có thể tạo separate chunk. Lợi ích initial bundle nhỏ; sự đánh đổi (trade-off / 트레이드오프) first-use độ trễ (latency / 지연 시간)/chunk thất bại (failure / 실패) độ phức tạp (complexity / 복잡도).

Cây (tree / 트리) shaking loại unused exports khi static phân tích (analysis / 분석) cho phép. Side effects, CommonJS/động (dynamic / 동적) hành vi (behavior / 동작) có thể hạn chế cây (tree / 트리) shaking.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Cây (tree / 트리) shaking là bundler hành vi (behavior / 동작), không phải guarantee của JavaScript ngôn ngữ (language / 언어). Bundle chiến lược (strategy / 전략) phải đo trên real loading waterfall.

---

# Chương 37 — Serialization chi phí (cost / 비용)

`JSON.stringify` và `JSON.parse` là synchronous CPU công việc (work / 작업). Large payload có thể khối (block / 블록) main luồng thực thi (thread / 스레드).

Cross-worker structured clone cũng có chi phí (cost / 비용). Transferable giúp một số nhị phân (binary / 이진) cases.

Nếu serialization chi phí (cost / 비용) lớn, xem xét smaller payload, pagination, streams, workers hoặc nhị phân (binary / 이진) biểu diễn (representation / 표현) tùy use trường hợp (case / 사례).

---

# Chương 38 — bảo mật (security / 보안) mô hình tư duy (mental model / 사고 모델)

Ranh giới bảo mật (security boundary / 보안 경계) bắt đầu từ giả định (assumption / 가정): bất kỳ dữ liệu nào từ người dùng (user / 사용자), URL, lưu trữ (storage / 저장소), mạng (network / 네트워크), `postMessage`, third-party script hoặc bản địa (native / 네이티브) cầu nối (bridge / 브리지) đều có thể malformed hoặc malicious.

Mô hình tư duy (mental model / 사고 모델):

```text
source
↓
transformations
↓
sink
↓
privilege/effect
```

Cấp cao (senior / 시니어) phải biết dữ liệu (data / 데이터) đi vào từ đâu và cuối cùng được dùng ở sink nào.

> **Nối mạch:** Trong **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Lab profile và Real người dùng (user / 사용자) Monitoring trả lời hai câu hỏi khác nhau** nêu quy tắc; **Kiểm tra hợp lệ (validation / 검증), encoding và sanitization không phải cùng một việc** thử quy tắc trong tình huống, rồi **Nguồn (source / 소스) đáng tin cậy về nghiệp vụ (business / 비즈니스) không đồng nghĩa safe cho sink** mở rộng hệ quả.

## Kiểm tra hợp lệ (validation / 검증), encoding và sanitization không phải cùng một việc

**kiểm tra hợp lệ (validation / 검증)** trả lời “dữ liệu (data / 데이터) có đúng shape/phạm vi (range / 범위)/allowlist mà thao tác (operation / 연산) chấp nhận không?”. Ví dụ `action` chỉ được là `"SAVE"` hoặc `"CANCEL"`.

**Encoding/escaping** biến dữ liệu (data / 데이터) để nó được hiểu như dữ liệu chứ không trở thành cú pháp (syntax / 문법) trong ngữ cảnh (context / 맥락) cụ thể, ví dụ HTML/URL/JavaScript ngữ cảnh (context / 맥락).

**Sanitization** loại/neutralize dangerous structures khi bạn chủ đích cho phép rich content như HTML subset.

Đừng dùng một helper “sanitize string” chung cho mọi sink. bảo mật (security / 보안) luôn phụ thuộc ngữ cảnh (context / 맥락) nơi dữ liệu (data / 데이터) được interpret.

> **Nối mạch:** Ở chặng này của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Kiểm tra hợp lệ (validation / 검증), encoding và sanitization không phải cùng một việc** đặt vấn đề; **Nguồn (source / 소스) đáng tin cậy về nghiệp vụ (business / 비즈니스) không đồng nghĩa safe cho sink** đối chiếu bằng chứng, rồi **Hãy coi message như một RPC yêu cầu (request / 요청) qua trust ranh giới (boundary / 경계)** mở rộng hệ quả hoặc giới hạn liên quan.

## Nguồn (source / 소스) đáng tin cậy về nghiệp vụ (business / 비즈니스) không đồng nghĩa safe cho sink

API nội bộ có thể trả display name do người dùng (user / 사용자) nhập trước đó. Khi đưa vào `textContent`, nó là văn bản (text / 텍스트). Khi đưa vào `innerHTML`, cùng giá trị (value / 값) có thể trở thành markup. bảo mật (security / 보안) classification phải theo **luồng dữ liệu (data flow / 데이터 흐름) tới sink**, không chỉ theo “máy chủ (server / 서버) của mình”.

### Môi trường vận hành (production / 운영 환경) rà soát (review / 검토) mẫu (pattern / 패턴)

Với mỗi privileged/dangerous sink, dấu vết (trace / 추적) ngược:

```text
sink
↑
transformations
↑
validation/sanitization
↑
source/trust boundary
```

Nếu không thể giải thích chuỗi (chain / 사슬) này, mã (code / 코드) security-critical chưa đủ rõ.

---

# Chương 39 — XSS và DOM XSS

Dangerous:

```js
element.innerHTML = userInput;
```

Safer plain văn bản (text / 텍스트):

```js
element.textContent = userInput;
```

Sources có thể là `location.search`, `location.hash`, API phản hồi (response / 응답), localStorage, postMessage. Sinks gồm `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, eval-like APIs.

DOM XSS không cần backend template; chỉ cần frontend đưa untrusted string vào executable/HTML sink.

### Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

API phản hồi (response / 응답) không tự trusted chỉ vì “do máy chủ (server / 서버) mình trả”. Compromised dữ liệu (data / 데이터), stored payload hoặc backend escaping các giả định (assumptions / 가정들) vẫn có thể tạo XSS.

---

# Chương 40 — CSP và defense-in-depth

Content bảo mật (security / 보안) chính sách (policy / 정책) là trình duyệt (browser / 브라우저) bảo mật (security / 보안) điều khiển (control / 제어) qua HTTP header, giúp giới hạn scripts/styles/resources và giảm impact của XSS.

Strict CSP thường dựa trên nonce/băm (hash / 해시) và hạn chế unsafe inline script. Deploy cần report-only/testing chiến lược (strategy / 전략) vì CSP sai có thể break app.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

CSP không thay safe rendering. Nó là defense-in-depth, không phải lý do để tiếp tục dùng unsafe sinks.

---

# Chương 41 — Trusted Types

> **nền tảng (platform / 플랫폼) phiên bản (version / 버전) ghi chú (note / 노트):** Trusted Types là Web bảo mật (security / 보안) API/CSP tích hợp (integration / 통합), không phải ECMAScript ngôn ngữ (language / 언어) tính năng (feature / 기능). hỗ trợ (support / 지원) phụ thuộc trình duyệt (browser / 브라우저)/WebView và triển khai (deployment / 배포) chính sách (policy / 정책), nên mục tiêu (target / 대상) thời gian chạy (runtime / 런타임) quan trọng hơn ES edition.

Trusted Types giúp kiểm soát dangerous DOM injection sinks. mô hình tư duy (mental model / 사고 모델):

```text
untrusted string
↓
approved policy/sanitizer
↓
TrustedHTML-like value
↓
dangerous sink
```

Nếu enforce đúng, raw string assignment vào protected sink bị chặn.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Trusted Types chính sách (policy / 정책) viết sai vẫn có thể nguy hiểm. Tốt nhất giảm số dangerous sinks trước, sau đó dùng chính sách (policy / 정책) có kiểm soát.

---

# Chương 42 — Prototype Pollution

Unsafe động (dynamic / 동적) thuộc tính (property / 속성) assignment/deep merge có thể cho attacker chạm keys như `__proto__`, `constructor`, `prototype`.

```js
function setValue(
  target,
  key,
  value
) {
  target[key] = value;
}
```

Nếu `key` arbitrary bên ngoài (external / 외부) đầu vào (input / 입력), cần lược đồ (schema / 스키마)/key kiểm tra hợp lệ (validation / 검증).

Defenses gồm validate allowed keys, tránh generic unsafe deep merge, dùng Map cho arbitrary dictionaries khi phù hợp, đối tượng (object / 객체).create(null) trong một số cases, keep dependencies updated.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Prototype pollution là lý do prototype internals từ Intermediate có bảo mật (security / 보안) giá trị (value / 값) thực tế.

---

# Chương 43 — CSRF mô hình tư duy (mental model / 사고 모델)

CSRF lợi dụng trình duyệt (browser / 브라우저) tự gửi credentials/cookies tới mục tiêu (target / 대상) origin để thực hiện state-changing yêu cầu (request / 요청) ngoài ý muốn người dùng (user / 사용자).

Mitigations thuộc kiến trúc (architecture / 아키텍처) backend/trình duyệt (browser / 브라우저): SameSite cookies, CSRF tokens, Origin/Referer checks, API thiết kế (design / 설계). Frontend cần gửi đơn vị từ (token / 토큰)/header theo đặc tả hợp đồng (contract / 계약), nhưng backend phải enforce trust ranh giới (boundary / 경계).

---

# Chương 44 — đơn vị từ (token / 토큰) lưu trữ (storage / 저장소): không có câu trả lời một dòng

“localStorage luôn xấu” hoặc “cookie luôn tốt” đều quá đơn giản. sự đánh đổi (trade-off / 트레이드오프) phụ thuộc XSS threat mô hình (model / 모델), CSRF mô hình (model / 모델), same-origin kiến trúc (architecture / 아키텍처), refresh-token thiết kế (design / 설계), backend hỗ trợ (support / 지원) và hybrid bộ chứa (container / 컨테이너).

Cấp cao (senior / 시니어) không chọn đơn vị từ (token / 토큰) lưu trữ (storage / 저장소) bằng blog snippet; nó là hệ thống (system / 시스템) bảo mật (security / 보안) quyết định (decision / 결정).

---

# Chương 45 — `postMessage` bảo mật (security / 보안)

Sender:

```js
window.postMessage(
  data,
  "https://trusted.example.com"
);
```

Tránh `"*"` cho sensitive dữ liệu (data / 데이터).

Receiver:

```js
window.addEventListener(
  "message",
  (event) => {
    if (
      event.origin !==
      "https://trusted.example.com"
    ) {
      return;
    }

    validateMessage(event.data);
  }
);
```

Cần validate `origin`, `source`, message kiểu (type / 타입)/lược đồ (schema / 스키마) và authorization/năng lực (capability / 역량). Origin đúng không tự chứng minh thao tác (operation / 연산) requested là allowed.

> **Nối mạch:** Đặt trong câu hỏi lớn của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Nguồn (source / 소스) đáng tin cậy về nghiệp vụ (business / 비즈니스) không đồng nghĩa safe cho sink** đặt tiêu chí; **Hãy coi message như một RPC yêu cầu (request / 요청) qua trust ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Cầu nối (bridge / 브리지) nên giống versioned RPC giao thức (protocol / 프로토콜) hơn là toàn cục (global / 전역) God đối tượng (object / 객체)** mở rộng hệ quả.

## Hãy coi message như một RPC yêu cầu (request / 요청) qua trust ranh giới (boundary / 경계)

Một message môi trường vận hành (production / 운영 환경) nên có shape ổn định:

```js
{
  version: 1,
  type: "OPEN_DOCUMENT",
  requestId: "...",
  payload: {
    documentId: "..."
  }
}
```

Receiver nên kiểm tra theo thứ tự:

```text
expected source/window?
expected origin?
known protocol version?
known message type?
payload schema valid?
operation được authorize/capability cho sender này?
```

Chỉ check `origin` rồi gọi privileged handler vẫn có thể tạo **confused-deputy** style bài toán (problem / 문제) nếu trusted page bị attacker điều khiển để gửi command mà nó không nên có quyền yêu cầu.

---

# Chương 46 — bản địa (native / 네이티브) cầu nối (bridge / 브리지) / WebView ranh giới bảo mật (security boundary / 보안 경계)

Hybrid app cầu nối (bridge / 브리지) có privileges vượt web page. Nếu web có thể gọi bản địa (native / 네이티브) phương thức (method / 메서드) để mở camera, eKYC, tệp (file / 파일) hệ thống (system / 시스템) hoặc payment, đó là privileged API.

Wrap cầu nối (bridge / 브리지):

```js
const kycBridge = {
  start(params) {
    validateKycParams(params);
    return nativeBridge.startKyc(
      params
    );
  }
};
```

Questions cấp cao (senior / 시니어) phải hỏi: page/origin nào được gọi cầu nối (bridge / 브리지), payload được validate ở đâu, điều hướng (navigation / 내비게이션) restriction có ở bản địa (native / 네이티브) side không, callback/deep link có yêu cầu (request / 요청) ID không, cầu nối (bridge / 브리지) expose capabilities tối thiểu chưa.

> **Nối mạch:** Trong **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Hãy coi message như một RPC yêu cầu (request / 요청) qua trust ranh giới (boundary / 경계)** đặt tiêu chí; **Cầu nối (bridge / 브리지) nên giống versioned RPC giao thức (protocol / 프로토콜) hơn là toàn cục (global / 전역) God đối tượng (object / 객체)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): tách chính sách (policy / 정책) khỏi cơ chế (mechanism / 메커니즘)** mở rộng hệ quả.

## Cầu nối (bridge / 브리지) nên giống versioned RPC giao thức (protocol / 프로토콜) hơn là toàn cục (global / 전역) God đối tượng (object / 객체)

Bad mô hình tư duy (mental model / 사고 모델):

```text
window.nativeBridge
→ web muốn gọi gì cũng được
```

Tốt hơn:

```text
web feature
↓
small JS adapter
↓
versioned message/command
↓
native validation + authorization
↓
minimal native capability
↓
versioned result/error callback
```

Ví dụ yêu cầu (request / 요청):

```js
{
  version: 2,
  type: "KYC_START",
  requestId: "req-123",
  payload: {
    sessionId: "..."
  }
}
```

Kết quả (result / 결과):

```js
{
  version: 2,
  type: "KYC_RESULT",
  requestId: "req-123",
  status: "success",
  payload: {
    verificationId: "..."
  }
}
```

`requestId` giúp correlation và tránh callback của yêu cầu (request / 요청) cũ cập nhật luồng (flow / 흐름) mới. giao thức (protocol / 프로토콜) phiên bản (version / 버전) giúp bản địa (native / 네이티브)/web releases tiến hóa có kiểm soát. kiểm tra hợp lệ (validation / 검증) phải tồn tại ở bản địa (native / 네이티브) side nữa; JavaScript kiểm tra hợp lệ (validation / 검증) không phải ranh giới bảo mật (security boundary / 보안 경계) nếu attacker có thể gọi cầu nối (bridge / 브리지) trực tiếp qua compromised page/thời gian chạy (runtime / 런타임).

---

# Chương 47 — `eval`, `Function` và động (dynamic / 동적) mã (code / 코드) thực thi (execution / 실행)

Avoid:

```js
eval(userInput);
new Function(userInput);
```

Risks gồm mã (code / 코드) injection, CSP incompatibility, hard-to-audit luồng (flow / 흐름) và tối ưu hóa (optimization / 최적화)/gỡ lỗi (debug / 디버그) problems.

Nếu cần động (dynamic / 동적) hành vi (behavior / 동작), thường dùng data-driven chiến lược (strategy / 전략) registry/parser/cấu hình (config / 설정) thay vì động (dynamic / 동적) mã (code / 코드) thực thi (execution / 실행).

---

# Chương 48 — RegExp an toàn (safety / 안전)

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2025:** `RegExp.escape()` được chuẩn hóa ở ES2025 để escape string dùng như literal trong động (dynamic / 동적) RegExp. Nó xử lý nhiều edge cases hơn helper tự viết; với WebView cũ, hãy dùng maintained polyfill/helper thay vì tự thêm backslash vài ký tự.

Động (dynamic / 동적) regex từ người dùng (user / 사용자) đầu vào (input / 입력):

```js
new RegExp(userInput);
```

có thể thay ngữ nghĩa (semantics / 의미론) hoặc throw invalid mẫu (pattern / 패턴). Với intent literal tìm kiếm (search / 검색), hiện đại (modern / 현대적) runtimes có `RegExp.escape()`; older targets cần compatible escaping chiến lược (strategy / 전략).

Ngoài injection còn có ReDoS/catastrophic backtracking khi mẫu (pattern / 패턴) nhà phát triển (developer / 개발자) viết có nested ambiguous quantifiers.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Nếu chỉ cần substring tìm kiếm (search / 검색), `includes()` thường đơn giản và safer hơn regex.

---

# Chương 49 — Supply-chain bảo mật (security / 보안)

Third-party gói (package / 패키지) chạy với privileges của app. Risks: malicious gói (package / 패키지), compromised maintainer, typosquatting, vulnerable transitive phụ thuộc (dependency / 의존성), postinstall scripts, CDN compromise.

Practices: lockfile, phụ thuộc (dependency / 의존성) rà soát (review / 검토), vulnerability scanning, cập nhật (update / 업데이트) chính sách (policy / 정책), giảm random micro-packages, gói (package / 패키지) provenance/reputation, SRI khi phù hợp cho CDN resources.

Cấp cao (senior / 시니어) hiểu phụ thuộc (dependency / 의존성) không chỉ là convenience; nó là trusted mã (code / 코드) added vào attack surface.

---

# Chương 50 — API thiết kế (design / 설계): công khai (public / 공개) surface phải nhỏ và khó dùng sai

Một API tốt trả lời rõ inputs, outputs, mutability, errors, cancellation, vòng đời (lifecycle / 생명주기), quyền sở hữu (ownership / 소유권).

```js
export function createUserService({
  repository,
  logger
}) {
  return {
    load,
    update
  };
}
```

Không export mọi helper nội bộ (internal / 내부). API công khai (public API / 공개 API) nhỏ cho phép refactor hiện thực (implementation / 구현) mà không phá consumers.

> **Nối mạch:** Ở chặng này của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Cầu nối (bridge / 브리지) nên giống versioned RPC giao thức (protocol / 프로토콜) hơn là toàn cục (global / 전역) God đối tượng (object / 객체)** đặt đầu vào cho **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): tách chính sách (policy / 정책) khỏi cơ chế (mechanism / 메커니즘)**, rồi **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): functional cốt lõi (core / 핵심), effectful shell** mở rộng hệ quả hoặc giới hạn liên quan.

## Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): tách chính sách (policy / 정책) khỏi cơ chế (mechanism / 메커니즘)

Ví dụ generic HTTP máy khách (client / 클라이언트) nên biết cơ chế (mechanism / 메커니즘):

```text
URL
headers
HTTP status
JSON parsing
AbortSignal
```

Nó không nên biết nghiệp vụ (business / 비즈니스) chính sách (policy / 정책) kiểu “403 của KYC thì chuyển screen 7”. chính sách (policy / 정책) đó thuộc tính năng (feature / 기능)/lĩnh vực (domain / 도메인) orchestration.

Tương tự, bộ nhớ đệm (cache / 캐시) cơ chế (mechanism / 메커니즘) có thể biết TTL/eviction, còn “balance có được stale 30 giây không” là lĩnh vực (domain / 도메인) chính sách (policy / 정책).

Sự tách biệt này giúp lớp trừu tượng (abstraction / 추상화) reusable mà không biến thành God dịch vụ (service / 서비스).

> **Nối mạch:** Đặt trong câu hỏi lớn của **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): tách chính sách (policy / 정책) khỏi cơ chế (mechanism / 메커니즘)** đặt đầu vào cho **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): functional cốt lõi (core / 핵심), effectful shell**, rồi **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): tường minh (explicit / 명시적) quyền sở hữu (ownership / 소유권) đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả hoặc giới hạn liên quan.

## Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): functional cốt lõi (core / 핵심), effectful shell

Một luồng (flow / 흐름) có thể tổ chức:

```text
external DTO / user event
↓
validate + normalize
↓
pure/domain calculation
↓
decide command/effect
↓
network/storage/native adapter
↓
map result
↓
state transition/render
```

Không cần áp dụng rigid kiến trúc (architecture / 아키텍처) cho tính năng (feature / 기능) nhỏ. Nhưng khi lô-gic nghiệp vụ (business logic / 비즈니스 로직) có giá trị kiểm thử (test / 테스트)/reuse, giữ nó khỏi DOM/mạng (network / 네트워크) side effects làm mã (code / 코드) dễ reason hơn.

> **Nối mạch:** Trong **JavaScript cấp cao (senior / 시니어) — thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안) và kiến trúc (architecture / 아키텍처)**, sau nội dung của **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): functional cốt lõi (core / 핵심), effectful shell**, **Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): tường minh (explicit / 명시적) quyền sở hữu (ownership / 소유권) đặc tả hợp đồng (contract / 계약)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Hiện đại (modern / 현대적) vs legacy: đọc mã (code / 코드) theo “bài toán (problem / 문제) được giải quyết”, không theo tuổi cú pháp (syntax / 문법)** mở rộng hệ quả hoặc giới hạn liên quan.

## Môi trường vận hành (production / 운영 환경) mẫu (pattern / 패턴): tường minh (explicit / 명시적) quyền sở hữu (ownership / 소유권) đặc tả hợp đồng (contract / 계약)

Nếu API tạo tài nguyên (resource / 자원), công khai (public / 공개) surface nên giúp caller biết cleanup:

```js
const subscription = subscribeToUpdates(handler);

// later
subscription.dispose();
```

hoặc:

```js
const unsubscribe = subscribe(handler);
unsubscribe();
```

Hidden toàn cục (global / 전역) registration mà caller không có cleanup đường dẫn (path / 경로) là môi trường vận hành (production / 운영 환경) smell.

### Cấp cao (senior / 시니어) question

Caller cần biết gì? Caller có thể misuse gì? tài nguyên (resource / 자원) ai sở hữu? thao tác (operation / 연산) cancel thế nào? lỗi (error / 오류) đặc tả hợp đồng (contract / 계약) là gì?

---

# Chương 51 — mô-đun (module / 모듈) Boundaries và phụ thuộc (dependency / 의존성) Direction

Tính năng (feature / 기능) cấu trúc (structure / 구조):

```text
user/
  domain.js
  api.js
  service.js
  view.js
  index.js
```

Bên tiêu thụ (consumer / 소비자) import API công khai (public API / 공개 API) từ `index.js`, không deep-import arbitrary internals.

Phụ thuộc (dependency / 의존성) direction lý tưởng thường giữ lĩnh vực (domain / 도메인)/pure lô-gic (logic / 논리) không phụ thuộc DOM/fetch/khung phần mềm (framework / 프레임워크) khi benefit rõ.

Bad:

```js
// domain/pricing.js
import {
  getCurrentUser
} from "../api.js";
```

Better:

```js
function calculatePrice(
  order,
  user
) {
}
```

Caller đưa dữ liệu (data / 데이터) vào.

---

# Chương 52 — lĩnh vực (domain / 도메인) Modeling

Thành phần nguyên thủy (primitive / 기본 요소) soup:

```js
transfer(
  from,
  to,
  value,
  status,
  type,
  flag
);
```

Khó hiểu. Cohesive đối tượng (object / 객체):

```js
createTransfer({
  sourceAccount,
  destinationAccount,
  amount,
  currency
});
```

Lĩnh vực (domain / 도메인) modeling tập trung identities, valid states, transitions, units và invariants.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Kiến trúc (architecture / 아키텍처) không bắt đầu bằng folder cấu trúc (structure / 구조). Nó bắt đầu bằng boundaries và dependencies phản ánh lĩnh vực (domain / 도메인).

---

# Chương 53 — trạng thái (state / 상태) Machines cho complex UI luồng (flow / 흐름)

eKYC/payment/multi-step form có nhiều states và transitions. tường minh (explicit / 명시적) máy trạng thái (state machine / 상태 머신):

```text
idle
↓ START
opening
↓ OPENED
waiting
├ SUCCESS → success
└ FAIL    → error
```

Đối tượng (object / 객체) chuyển tiếp (transition / 전이) bảng (table / 테이블):

```js
const transitions = {
  idle: {
    START: "opening"
  },

  opening: {
    OPENED: "waiting",
    FAIL: "error"
  },

  waiting: {
    SUCCESS: "success",
    FAIL: "error"
  }
};
```

Máy trạng thái (state machine / 상태 머신) giảm impossible transitions và giúp kiểm thử (test / 테스트) luồng (flow / 흐름).

---

# Chương 54 — Event-driven kiến trúc (architecture / 아키텍처): lợi ích và chi phí

Events hữu ích khi nhiều consumers phản ứng với “something happened”. Nhưng event-driven các hệ thống (systems / 시스템들) có hidden luồng (flow / 흐름), thứ tự (ordering / 순서) các giả định (assumptions / 가정들), duplicate handling và debugging độ phức tạp (complexity / 복잡도).

Cấp cao (senior / 시니어) quy tắc (rule / 규칙): dùng direct hàm (function / 함수) lời gọi (call / 호출) khi direct phụ thuộc (dependency / 의존성) rõ và đơn giản. sự kiện (event / 이벤트) không tự làm kiến trúc (architecture / 아키텍처) tốt hơn.

---

# Chương 55 — Repository / Gateway và Anti-Corruption tầng (layer / 계층)

Repository ranh giới (boundary / 경계):

```js
function createUserRepository({
  api
}) {
  return {
    async findById(id) {
      const dto = await api.getUser(id);
      return mapUser(dto);
    }
  };
}
```

App/lĩnh vực (domain / 도메인) không biết vận chuyển (transport / 전송) DTO.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Nếu repository chỉ forward 1:1 API lời gọi (call / 호출) không thêm lớp trừu tượng (abstraction / 추상화) benefit, tầng (layer / 계층) có thể thừa. Hãy thêm tầng (layer / 계층) khi nó bảo vệ ngữ nghĩa (semantics / 의미론), ánh xạ (mapping / 매핑) hoặc substitutability thực tế.

---

# Chương 56 — Command / truy vấn (query / 쿼리) Separation

Command thay đổi trạng thái (state / 상태); truy vấn (query / 쿼리) đọc trạng thái (state / 상태).

```js
await updateUser(command);
const user = await getUser(query);
```

Separation giúp lập luận (reasoning / 추론) side effects, caching và thử lại (retry / 재시도) an toàn (safety / 안전). Không cần full CQRS kiến trúc (architecture / 아키텍처) cho frontend nhỏ; chỉ cần API intent rõ.

---

# Chương 57 — Middleware / chuỗi xử lý (pipeline / 파이프라인) kiến trúc (architecture / 아키텍처)

HTTP chuỗi xử lý (pipeline / 파이프라인) có thể là:

```text
trace
↓
auth
↓
retry
↓
transport
↓
response mapping
```

Thứ tự (order / 순서) là hành vi (behavior / 동작). thử lại (retry / 재시도) nằm ngoài/inside auth refresh cho ngữ nghĩa (semantics / 의미론) khác. Logging phải redact secrets. Hidden mutation yêu cầu (request / 요청) đối tượng (object / 객체) gây bugs; immutable-ish transformation thường dễ reason hơn.

---

# Chương 58 — Plugin kiến trúc (architecture / 아키텍처)

Plugin các hệ thống (systems / 시스템들) cần đặc tả hợp đồng (contract / 계약): name, phiên bản (version / 버전), capabilities, init/run/dispose, tính tương thích (compatibility / 호환성) và lỗi (error / 오류) isolation.

```js
const plugins = new Map();

export function registerPlugin(
  name,
  plugin
) {
  if (plugins.has(name)) {
    throw new Error(
      `Plugin already registered: ${name}`
    );
  }

  plugins.set(name, plugin);
}
```

Cấp cao (senior / 시니어) phải phiên bản (version / 버전) giao diện (interface / 인터페이스) và giới hạn privileges nếu plugin không fully trusted.

---

# Chương 59 — Feature Flags và lifecycle của flag
Phần này nối mạch bài học với “Chương 59 — Feature Flags và lifecycle của flag”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
if (flags.newCheckout) {
  runNewCheckout();
} else {
  runOldCheckout();
}
```

Flag tốt cho rollout/experiments nhưng long-lived flags tạo dead mã (code / 코드) và combinatorial testing states.

Vòng đời (lifecycle / 생명주기):

```text
create
rollout
observe
complete
remove
```

---

# Chương 60 — cấu hình (configuration / 구성) kiến trúc (architecture / 아키텍처)

Cấu hình (config / 설정) là đầu vào (input / 입력), cần validate ở ranh giới (boundary / 경계).

```js
const config = {
  apiBaseUrl:
    runtimeConfig.apiBaseUrl,

  timeoutMs:
    runtimeConfig.timeoutMs
};
```

Kiểm tra hợp lệ (validation / 검증) startup:

```js
function validateConfig(config) {
  if (!config.apiBaseUrl) {
    throw new Error(
      "apiBaseUrl required"
    );
  }
}
```

Frontend bundle không thể giữ secret thực sự chỉ bằng môi trường (environment / 환경) variable; trình duyệt (browser / 브라우저) cuối cùng phải nhận giá trị (value / 값) để dùng.

---

# Chương 61 — lỗi (error / 오류) Taxonomy

Categories có thể gồm kiểm tra hợp lệ (validation / 검증), nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙), authentication, authorization, not found, xung đột (conflict / 충돌), mạng (network / 네트워크), hết thời gian chờ (timeout / 타임아웃), cancellation, máy chủ (server / 서버)/phụ thuộc (dependency / 의존성) errors.

```js
class AppError extends Error {
  constructor(
    message,
    {
      code,
      cause,
      retryable = false,
      details
    } = {}
  ) {
    super(message, { cause });
    this.code = code;
    this.retryable = retryable;
    this.details = details;
  }
}
```

Stable machine-readable mã (code / 코드) tốt hơn parse message.

---

# Chương 62 — Resilience Toolbox

Hết thời gian chờ (timeout / 타임아웃), cancellation, thử lại (retry / 재시도), backoff, jitter, fallback, bộ nhớ đệm (cache / 캐시), circuit breaker, bulkhead, graceful degradation không phải checklist cần áp dụng hết. Chọn theo dạng thất bại (failure mode / 실패 모드), criticality, idempotency, độ trễ (latency / 지연 시간) ngân sách (budget / 예산) và UX expectation.

Cấp cao (senior / 시니어) thiết kế (design / 설계) resilience bằng scenarios, không bằng mẫu (pattern / 패턴) count.

---

# Chương 63 — khả năng quan sát (observability / 관측 가능성): môi trường vận hành (production / 운영 환경) phải trả lời được “chuyện gì đã xảy ra?”

Khả năng quan sát (observability / 관측 가능성) gồm logs, metrics, traces, lỗi (error / 오류) reports và hiệu năng (performance / 성능) telemetry.

Một môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) cần biết: bản phát hành (release / 릴리스)/phiên bản (version / 버전) nào, page/tuyến (route / 경로) nào, yêu cầu (request / 요청) nào, phụ thuộc (dependency / 의존성) nào thất bại (fail / 실패), mất bao lâu, người dùng (user / 사용자) hành động (action / 동작) nào dẫn tới đó.

Nếu tính năng (feature / 기능) trọng yếu (critical / 중요) nhưng không có cách quan sát môi trường vận hành (production / 운영 환경), đó là thiết kế (design / 설계) thiếu.

---

# Chương 64 — Structured Logging

Bad:

```js
console.log("error");
```

Better:

```js
logger.error(
  "user_load_failed",
  {
    userId,
    status: error.status,
    requestId
  }
);
```

Không log password, truy cập (access / 접근) đơn vị từ (token / 토큰), refresh đơn vị từ (token / 토큰) hoặc sensitive PII không cần thiết.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Logging là dữ liệu (data / 데이터) quản trị (governance / 거버넌스) concern. Log quá nhiều tạo noise/chi phí (cost / 비용)/privacy rủi ro (risk / 위험).

---

# Chương 65 — Metrics và high-cardinality bài toán (problem / 문제)

Metrics examples: yêu cầu (request / 요청) success tỷ lệ (rate / 비율), độ trễ (latency / 지연 시간), JS lỗi (error / 오류) tỷ lệ (rate / 비율), tìm kiếm (search / 검색) thất bại (failure / 실패) tỷ lệ (rate / 비율), checkout thất bại (failure / 실패) tỷ lệ (rate / 비율), long-task frequency.

Chỉ số (metric / 지표) labels cần kiểm soát cardinality. Dùng người dùng (user / 사용자) ID làm chỉ số (metric / 지표) label có thể tạo hàng triệu series. Per-request detail phù hợp log/dấu vết (trace / 추적) hơn.

---

# Chương 66 — Tracing và Correlation ID

Phân tán (distributed / 분산) luồng (flow / 흐름):

```text
user click
↓
frontend request
↓
gateway
↓
service
↓
database
```

Correlation/yêu cầu (request / 요청) ID giúp nối logs giữa layers.

```js
const requestId = crypto.randomUUID();
```

Nếu organization đã dùng tiêu chuẩn (standard / 표준) tracing headers, follow tiêu chuẩn (standard / 표준) thay vì tự tạo hệ thống cạnh tranh.

---

# Chương 67 — môi trường vận hành (production / 운영 환경) lỗi (error / 오류) Reporting và nguồn (source / 소스) Maps

Minified ngăn xếp (stack / 스택) `app.abcd.js:1:20291` khó gỡ lỗi (debug / 디버그). nguồn (source / 소스) maps map generated mã (code / 코드) về nguồn (source / 소스).

Lỗi (error / 오류) report nên có ngăn xếp (stack / 스택), bản phát hành (release / 릴리스) phiên bản (version / 버전), tuyến (route / 경로), trình duyệt (browser / 브라우저)/thời gian chạy (runtime / 런타임), breadcrumbs và relevant mạng (network / 네트워크) ngữ cảnh (context / 맥락), nhưng phải filter sensitive dữ liệu (data / 데이터).

Nguồn (source / 소스) maps có thể private upload vào lỗi (error / 오류) nền tảng (platform / 플랫폼) thay vì công khai (public / 공개) expose tùy bảo mật (security / 보안) chính sách (policy / 정책).

---

# Chương 68 — Testing chiến lược (strategy / 전략) ở mức (level / 수준) cấp cao (senior / 시니어)

Câu hỏi là “rủi ro (risk / 위험) nào cần kiểm thử (test / 테스트)?”, không phải “coverage 100% chưa?”. Layers có đơn vị (unit / 단위), tích hợp (integration / 통합), đặc tả hợp đồng (contract / 계약), E2E, visual, hiệu năng (performance / 성능) và bảo mật (security / 보안) testing.

Pure nghiệp vụ (business / 비즈니스) rules có đơn vị (unit / 단위) tests rẻ. API/dịch vụ (service / 서비스) tích hợp (integration / 통합) có mock máy chủ (server / 서버). trọng yếu (critical / 중요) người dùng (user / 사용자) journeys có E2E. đặc tả hợp đồng (contract / 계약) tests bắt backend/bản địa (native / 네이티브)/plugin lược đồ (schema / 스키마) drift.

Kiểm thử (test / 테스트) chiến lược (strategy / 전략) tối ưu confidence / maintenance chi phí (cost / 비용).

---

# Chương 69 — đặc tả hợp đồng (contract / 계약) Testing

Frontend ↔ backend đặc tả hợp đồng (contract / 계약) có shape, types, lỗi (error / 오류) codes, optional fields và phiên bản (version / 버전).

Nếu backend đổi `user_nm` thành `name` mà frontend mapper vẫn expect cũ, đặc tả hợp đồng (contract / 계약)/kiểm thử tích hợp (integration test / 통합 테스트) nên thất bại (fail / 실패) trước môi trường vận hành (production / 운영 환경).

Hybrid app càng cần đặc tả hợp đồng (contract / 계약) tests giữa WebView JS và bản địa (native / 네이티브) cầu nối (bridge / 브리지) vì bản phát hành (release / 릴리스) cycles có thể khác nhau.

---

# Chương 70 — tích hợp (integration / 통합) Testing và Mock máy chủ (server / 서버)

Thay vì mock `fetch` hiện thực (implementation / 구현) details, kiểm thử (test / 테스트) dịch vụ (service / 서비스) + mapper + trạng thái (state / 상태) cùng mock HTTP máy chủ (server / 서버) thường gần môi trường vận hành (production / 운영 환경) hơn.

Bạn verify URL, phương thức (method / 메서드), payload, phản hồi (response / 응답) parsing, lỗi (error / 오류) ánh xạ (mapping / 매핑) và cancellation hành vi (behavior / 동작) như một tích hợp (integration / 통합) đơn vị (unit / 단위).

---

# Chương 71 — E2E Testing

E2E kiểm thử (test / 테스트) trọng yếu (critical / 중요) journey: login → tìm kiếm (search / 검색) → select → submit → confirmation. Nó cho tích hợp (integration / 통합) confidence cao nhưng chậm/flaky nếu thiết kế (design / 설계) poor.

Keep E2E focused vào business-critical paths, đừng duplicate toàn bộ đơn vị (unit / 단위) kiểm thử (test / 테스트) cases qua trình duyệt (browser / 브라우저).

---

# Chương 72 — Property-based và Mutation Testing concepts

Property-based testing generate nhiều inputs để kiểm thử (test / 테스트) bất biến (invariant / 불변식), ví dụ normalize idempotence hoặc encode/decode round-trip.

Mutation testing thay operator/mã (code / 코드) để xem tests có bắt không. Nếu `>` thành `>=` mà tests vẫn pass, suite có thể yếu.

Đây là tools nâng cao, dùng cho lô-gic (logic / 논리) trọng yếu (critical / 중요) chứ không phải mọi hàm (function / 함수).

---

# Chương 73 — Deterministic Async Tests

Avoid kiểm thử (test / 테스트) sleep thật 2 giây. Dùng fake timers, controllable promises, mock máy chủ (server / 서버) và tường minh (explicit / 명시적) events/trạng thái (state / 상태) conditions.

Race điều kiện (condition / 조건) tests cần chủ động điều khiển phản hồi (response / 응답) thứ tự (order / 순서) để reproduce stale kết quả (result / 결과). Cancellation tests verify abort tín hiệu (signal / 신호) và cleanup.

---

# Chương 74 — hiện đại (modern / 현대적) JavaScript Toolbox và tính tương thích (compatibility / 호환성) mindset

> **Current-version ghi chú (note / 노트):** tệp (file / 파일) này được cập nhật khi ES2026 là snapshot chính thức mới nhất. Các hiện đại (modern / 현대적) APIs trong phần sau chủ yếu đến từ ES2024–ES2025 vì đây là nhóm đã vào tiêu chuẩn (standard / 표준) nhưng vẫn có tính tương thích (compatibility / 호환성) gap đáng chú ý. Khi đọc lại sau vài năm, hãy giữ cách đánh giá này và kiểm tra spec/MDN hiện tại.

Hiện đại (modern / 현대적) ECMAScript/thời gian chạy (runtime / 런타임) có các features như immutable array methods, Iterator helpers, Set operations, `Promise.withResolvers`, `Promise.try`, `RegExp.escape`, tường minh (explicit / 명시적) tài nguyên (resource / 자원) management và ngày càng nhiều Intl/ArrayBuffer APIs.

Cấp cao (senior / 시니어) không cần chạy theo mọi tính năng (feature / 기능) mới. Với trình duyệt (browser / 브라우저)/WebView enterprise, luôn hỏi mục tiêu (target / 대상) thời gian chạy (runtime / 런타임) versions, transpiler/polyfill feasibility và fallback. Stage-4/standardized không có nghĩa mọi WebView cũ đã hỗ trợ (support / 지원).

> **Nối mạch:** Production pattern phải bắt đầu từ explicit ownership và contract; vì vậy modern/legacy được đánh giá theo problem solved, không theo tuổi syntax.

## Hiện đại (modern / 현대적) vs legacy: đọc mã (code / 코드) theo “bài toán (problem / 문제) được giải quyết”, không theo tuổi cú pháp (syntax / 문법)

Legacy cú pháp (syntax / 문법) không mặc định là mã (code / 코드) xấu; nó thường phản ánh thời gian chạy (runtime / 런타임)/toolchain tại thời điểm mã (code / 코드) được viết. Khi migrate, hãy hiểu ngữ nghĩa (semantic / 의미적) reason trước khi replace.

Một số ánh xạ (mapping / 매핑) thường gặp:

```text
var
→ let / const
reason: block scope + binding intent rõ hơn

function callback + var self = this
→ arrow callback
reason: lexical this cho callback case

arguments
→ rest parameters (...args)
reason: real Array-like collection semantics rõ hơn

string concatenation
→ template literals
reason: interpolation/readability

manual property extraction
→ destructuring
reason: binding intent ngắn hơn

constructor function + prototype methods
→ class syntax
reason: standard syntax cho cùng prototype model

IIFE/global namespace
→ ES modules
reason: lexical module scope + explicit dependency graph

callback pyramids / Deferred APIs
→ Promise
reason: standardized async composition

Promise chains cho sequential flow
→ async/await
reason: control flow dễ đọc hơn, semantics vẫn Promise-based

indexOf(...) !== -1
→ includes(...)
reason: membership intent rõ

sort() + copy thủ công
→ toSorted()
reason: non-mutating collection operation
```

### Di chuyển (migration / 마이그레이션) quy tắc (rule / 규칙)

Không mass-rewrite legacy mã (code / 코드) chỉ vì cú pháp (syntax / 문법) mới đẹp hơn. Ưu tiên thay đổi khi có một trong các lợi ích thực:

```text
fix correctness bug
reduce scope/this ambiguity
remove global coupling
make async ownership clearer
improve module boundary
reduce mutation risk
meet supported runtime/toolchain standard
```

Một stable legacy mô-đun (module / 모듈) đang chạy môi trường vận hành (production / 운영 환경) có thể đáng giữ hơn một rewrite lớn không có tests. Adapter + incremental di chuyển (migration / 마이그레이션) thường an toàn hơn.

---

# Chương 75 — `Promise.withResolvers()` và bên ngoài (external / 외부) completion

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2024:** `Promise.withResolvers()` thuộc ES2024. `Promise.try()` là API khác và thuộc ES2025; nó normalize callback có thể return giá trị (value / 값), throw synchronously hoặc return Promise.

Traditional mẫu (pattern / 패턴):

```js
let resolve;
let reject;

const promise = new Promise(
  (res, rej) => {
    resolve = res;
    reject = rej;
  }
);
```

Hiện đại (modern / 현대적) `Promise.withResolvers()` ở supporting runtimes trả `{ promise, resolve, reject }` trực tiếp. Useful cho event-to-promise bridges/queues, nhưng bên ngoài (external / 외부) resolver làm vòng đời (lifecycle / 생명주기) phức tạp. Prefer ordinary async composition nếu không cần.

---

# Chương 76 — Iterator Helpers và lazy pipelines

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2025:** toàn cục (global / 전역) `Iterator` và helpers như `map`, `filter`, `take`, `drop`, `flatMap`, `some`, `every`, `reduce`, `toArray` thuộc ES2025. Chúng mới hơn iterator giao thức (protocol / 프로토콜) ES2015 một thập kỷ, nên tính tương thích (compatibility / 호환성) check vẫn có ý nghĩa với embedded runtimes.

Iterator helpers cho phép operations lazy như map/filter/take trên iterators ở supporting runtimes. Lợi ích là tránh intermediate arrays và stop early.

Đừng rewrite ordinary arrays chỉ để dùng iterator helpers. Use khi lazy ngữ nghĩa (semantics / 의미론)/dữ liệu (data / 데이터) volume thật sự có giá trị.

---

# Chương 77 — RegExp.escape và literal động (dynamic / 동적) regex

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2025:** `RegExp.escape()` là ES2025. Trên trình duyệt (browser / 브라우저) hiện đại nó đã trở nên broadly available, nhưng embedded/enterprise WebViews có thể chậm hơn; security-sensitive mã (code / 코드) không nên silently assume hỗ trợ (support / 지원).

Nếu người dùng (user / 사용자) nhập từ khóa (keyword / 키워드) và bạn muốn regex literal tìm kiếm (search / 검색), escaping metacharacters là bắt buộc. `RegExp.escape()` cung cấp bản địa (native / 네이티브) solution ở hiện đại (modern / 현대적) runtimes. Với older WebViews, cần tính tương thích (compatibility / 호환성) chiến lược (strategy / 전략).

```js
const regex = new RegExp(
  RegExp.escape(keyword),
  "i"
);
```

Nếu chỉ cần substring, `includes()` đơn giản hơn.

---

# Chương 78 — cấp cao (senior / 시니어) Anti-patterns

Framework-shaped thinking: dùng React/WebSquare concept cho mọi JavaScript bài toán (problem / 문제). Premature tối ưu hóa (optimization / 최적화): viết unreadable mã (code / 코드) vì benchmark giả. kiến trúc (architecture / 아키텍처) astronaut: Factory/Repository/Manager cho 10 dòng CRUD. God dịch vụ (service / 서비스): một dịch vụ (service / 서비스) biết mọi lĩnh vực (domain / 도메인), DOM, lưu trữ (storage / 저장소), mạng (network / 네트워크). Fire-and-forget async không quyền sở hữu (ownership / 소유권). Unbounded Promise.all. thử lại (retry / 재시도) mọi thất bại (failure / 실패). bộ nhớ đệm (cache / 캐시) không vô hiệu hóa (invalidation / 무효화). sự kiện (event / 이벤트) bus như toàn cục (global / 전역) goto. dùng chung (shared / 공유) mutable toàn cục (global / 전역) trạng thái (state / 상태). Deep inheritance. Generic deep merge trên untrusted dữ liệu (data / 데이터). `eval`. Logging secrets. 15 booleans thay trạng thái (state / 상태) mô hình (model / 모델). Optional chaining để che bất biến (invariant / 불변식) violation.

Cấp cao (senior / 시니어) mã (code / 코드) không phải mã (code / 코드) nhiều mẫu (pattern / 패턴) nhất; là mã (code / 코드) có **minimum necessary độ phức tạp (complexity / 복잡도)** cho độ tin cậy (reliability / 신뢰성) và changeability cần thiết.

---

# Chương 79 — môi trường vận hành (production / 운영 환경) rà soát (review / 검토) Checklist dưới dạng tư duy

Khi rà soát (review / 검토) tính năng (feature / 기능), hãy tự hỏi: startup có heavy top-level công việc (work / 작업) không; listener/timer/worker/yêu cầu (request / 요청) ai cleanup; bộ nhớ đệm (cache / 캐시)/hàng đợi (queue / 큐)/tính đồng thời (concurrency / 동시성) có bound không; async thao tác (operation / 연산) có cancellation và stale-result protection không; thử lại (retry / 재시도) có idempotency không; DOM có unsafe sink không; postMessage/bản địa (native / 네이티브) cầu nối (bridge / 브리지) có kiểm tra hợp lệ (validation / 검증) không; ranh giới mô-đun (module boundary / 모듈 경계) có rõ không; DTO có leak khắp lĩnh vực (domain / 도메인) không; lỗi (error / 오류) taxonomy có stable không; môi trường vận hành (production / 운영 환경) thất bại (failure / 실패) có logs/correlation/nguồn (source / 소스) maps không; tests cover trọng yếu (critical / 중요) hành vi (behavior / 동작) không.

Checklist không thay lập luận (reasoning / 추론), nhưng giúp tránh bỏ sót category quan trọng.

---

# Chương 80 — cấp cao (senior / 시니어) Exit Criteria

Bạn có thể coi mình đạt senior-ready JavaScript khi có thể xử lý các trường hợp (case / 사례) sau bằng lập luận (reasoning / 추론) chứ không bằng đoán. UI freeze: phân biệt CPU/main-thread/kết xuất (render / 렌더링)/mạng (network / 네트워크) và biết profile. bộ nhớ (memory / 메모리) tăng sau điều hướng (navigation / 내비게이션): tìm listener/timer/subscription/DOM/bộ nhớ đệm (cache / 캐시)/closure retainer. tìm kiếm (search / 검색) hiện kết quả (result / 결과) cũ: nhận ra race và dùng abort/versioning. 5.000 requests cùng lúc: hiểu bounded tính đồng thời (concurrency / 동시성). Payment hết thời gian chờ (timeout / 타임아웃): hỏi idempotency trước thử lại (retry / 재시도). API string đưa vào innerHTML: nhận ra XSS. bản địa (native / 네이티브) cầu nối (bridge / 브리지): nghĩ origin/năng lực (capability / 역량)/lược đồ (schema / 스키마)/phiên bản (version / 버전)/vòng đời (lifecycle / 생명주기). môi trường vận hành (production / 운영 환경) bug không reproduce cục bộ (local / 로컬): dùng bản phát hành (release / 릴리스) logs, correlation, mạng (network / 네트워크) ngữ cảnh (context / 맥락) và nguồn (source / 소스) maps. Complex trạng thái (state / 상태): dùng reducer/máy trạng thái (state machine / 상태 머신) thay boolean explosion. kiến trúc (architecture / 아키텍처) rà soát (review / 검토): biết phụ thuộc (dependency / 의존성) direction, API công khai (public API / 공개 API), quyền sở hữu (ownership / 소유권), lỗi (error / 오류)/cancellation/khả năng quan sát (observability / 관측 가능성)/testing contracts.

Cấp cao (senior / 시니어) không cần nhớ mọi API. cấp cao (senior / 시니어) cần biết **bài toán (problem / 문제) thuộc tầng (layer / 계층) nào, dạng thất bại (failure mode / 실패 모드) nào có thể xảy ra và cách chứng minh hypothesis bằng bằng chứng (evidence / 증거)**.

---

# Chương 81 — Từ JavaScript cấp cao (senior / 시니어) sang React/WebSquare/TypeScript

Khi sang React, closure trở thành hook/stale-closure issue, immutability thành trạng thái (state / 상태) cập nhật (update / 업데이트) discipline, vòng đời (lifecycle / 생명주기) thành tác động (effect / 효과) cleanup, máy trạng thái (state machine / 상태 머신)/reducer thành UI trạng thái (state / 상태) management, cancellation thành tác động (effect / 효과)/yêu cầu (request / 요청) thời gian tồn tại (lifetime / 수명).

Khi sang WebSquareJS, JavaScript phạm vi (scope / 범위) map sang page/script phạm vi (scope / 범위), sự kiện (event / 이벤트) vòng đời (lifecycle / 생명주기) map sang thành phần (component / 컴포넌트)/page vòng đời (lifecycle / 생명주기), adapter map sang submission/bản địa (native / 네이티브) plugin wrappers, trạng thái (state / 상태) modeling map sang DataList/DataMap/page trạng thái (state / 상태), hybrid bảo mật (security / 보안) map sang bản địa (native / 네이티브) cầu nối (bridge / 브리지)/WebView/deep link contracts.

Khi sang TypeScript, thời gian chạy (runtime / 런타임) concepts không thay đổi. TypeScript chỉ cho bạn encode static relationships tốt hơn. Nếu chưa hiểu JavaScript closure, prototype, async và thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계), TypeScript types không thể thay thế nền tảng đó.

---

# Phụ lục — Cách tự cập nhật phiên bản (version / 버전) notes sau ES2026 mà không phải học lại JavaScript

Khi ES2027, ES2028 hoặc phiên bản sau xuất hiện, bạn không cần tạo lại một khóa “JavaScript mới” từ đầu. Hãy xem yearly edition như lớp bổ sung trên nền đã học. Nếu tính năng (feature / 기능) mới giải quyết bài toán (problem / 문제) của Array, nó được ghi thêm vào chương Array; nếu là Promise helper, thêm ở Promise/tính đồng thời (concurrency / 동시성); nếu là mô-đun (module / 모듈) cú pháp (syntax / 문법), thêm ở mô-đun (module / 모듈) chapter. Closure, prototype, `this`, đối tượng (object / 객체) định danh (identity / 식별자), vòng lặp sự kiện (event loop / 이벤트 루프) mô hình tư duy (mental model / 사고 모델) và tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) không mất giá trị chỉ vì số năm tăng.

Quy trình cập nhật chuẩn là: trước hết xem TC39/ECMA-262 để biết tính năng (feature / 기능) đã final và nằm ở snapshot nào; tiếp theo xem MDN tính tương thích (compatibility / 호환성)/Baseline để biết mức hỗ trợ (support / 지원) trình duyệt (browser / 브라우저); cuối cùng đối chiếu mục tiêu (target / 대상) ma trận (matrix / 행렬) của dự án (project / 프로젝트). Với hybrid app, mục tiêu (target / 대상) ma trận (matrix / 행렬) phải bao gồm Android hệ thống (system / 시스템) WebView/WKWebView thật mà app ship, không chỉ Chrome mới trên máy nhà phát triển (developer / 개발자).

Khi một bài viết nói “ESNext”, hãy chuyển câu hỏi thành: tính năng (feature / 기능) tên gì, proposal Stage mấy, đã Stage 4 chưa, đã nằm trong yearly snapshot nào, và thời gian chạy (runtime / 런타임) của tôi hỗ trợ (support / 지원) chưa? Chỉ cần giữ workflow này, tài liệu sẽ vẫn dễ đọc dù JavaScript thay đổi qua nhiều yearly releases.

Nguồn nên dùng để cập nhật là `https://tc39.es/ecma262/` cho specification cập nhật, Ecma International cho yearly snapshots đã phê duyệt, TC39 proposals repository cho proposal status, và MDN cho trình duyệt (browser / 브라우저) tính tương thích (compatibility / 호환성)/Baseline.

---

# Kết luận

JavaScript cấp cao (senior / 시니어) không phải mức (level / 수준) “học thêm cú pháp nâng cao”. Đây là mức (level / 수준) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링). Bạn phải nhìn một tính năng (feature / 기능) và đồng thời nghĩ về thời gian chạy (runtime / 런타임) chi phí (cost / 비용), vòng đời (lifecycle / 생명주기), bộ nhớ (memory / 메모리), cancellation, stale dữ liệu (data / 데이터), bảo mật (security / 보안) boundaries, phụ thuộc (dependency / 의존성) direction, lỗi (error / 오류) ngữ nghĩa (semantics / 의미론), khả năng quan sát (observability / 관측 가능성) và testing.

Một câu hỏi cấp cao (senior / 시니어) không dừng ở “mã (code / 코드) chạy chưa?”. Nó tiếp tục: nếu người dùng (user / 사용자) rời page thì sao, yêu cầu (request / 요청) cũ trả về muộn thì sao, máy chủ (server / 서버) overloaded thì sao, bộ nhớ đệm (cache / 캐시) stale thì sao, đầu vào (input / 입력) malicious thì sao, worker không terminate thì sao, môi trường vận hành (production / 운영 환경) thất bại (fail / 실패) thì biết bằng cách nào, và nhóm (team / 팀) khác sửa sau một năm có hiểu quyền sở hữu (ownership / 소유권)/dependencies không.

Nếu bạn có thể trả lời những câu hỏi đó một cách có hệ thống, JavaScript core của bạn đã đủ mạnh để đi sâu vào framework và system architecture mà không bị phụ thuộc vào “framework magic”.

> **Bàn giao:** Sau **Hiện đại (modern / 현대적) vs legacy: đọc mã (code / 코드) theo “bài toán (problem / 문제) được giải quyết”, không theo tuổi cú pháp (syntax / 문법)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
