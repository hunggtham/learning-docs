# CSS Master Supplement 2026

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **CSS Master Supplement 2026**. Route đi từ handbook prerequisite → terminology and modern Dart/CSS conventions → browser layout/paint/compositing → cascade layers, container queries, nesting và performance → migration/accessibility, để supplement đào sâu browser behavior mà không lặp canonical track.

## Những phần chuyên sâu sau `CSS_Beginner_to_Senior_2026.md`

> **Mục tiêu:** tệp (file / 파일) này **không lặp lại** handbook chuẩn gốc (canonical / 정본) Beginner → cấp cao (senior / 시니어).
> Nó bổ sung những phần cần thiết để chuyển từ **“cấp cao (senior / 시니어) CSS thực chiến”** sang **“master CSS / hiểu browser-level hành vi (behavior / 동작)”**.
>
> Hãy đọc tệp (file / 파일) này **sau** `CSS_Beginner_to_Senior_2026.md`.
>
> Ký hiệu:
> - **[MUST]**: cấp cao (senior / 시니어)/master phải hiểu.
> - **[DEEP]**: trình duyệt (browser / 브라우저) internals / edge cases.
> - **[hiện đại (modern / 현대적)]**: CSS hiện đại.
> - **[2026]**: tính năng (feature / 기능) đặc biệt đáng chú ý trong nền tảng Web (web platform / 웹 플랫폼) 2026.
> - **⚠**: mức hỗ trợ trình duyệt (browser support / 브라우저 지원) / khả năng tiếp cận (accessibility / 접근성) / interoperability cần kiểm tra.
>
> mô hình tư duy (mental model / 사고 모델):
>
> ```văn bản (text / 텍스트)
> chuẩn gốc (canonical / 정본) Beginner → Cấp cao (senior / 시니어)
> ├─ biết CSS ngôn ngữ (language / 언어)
> ├─ bố cục (layout / 레이아웃)
> ├─ các mẫu thành phần (component patterns)
> └─ kiến trúc (architecture / 아키텍처)
>
> Supplement
> ├─ trình duyệt (browser / 브라우저) mô hình định dạng (formatting model / 포매팅 모델)
> ├─ thuộc tính (property / 속성) giá trị (value / 값) vòng đời (lifecycle / 생명주기)
> ├─ sizing algorithms
> ├─ lớp trên cùng (top layer) / advanced UI
> ├─ CSS APIs
> ├─ Shadow DOM (cây DOM đóng gói) / SVG
> ├─ advanced typography / scroll / print
> ├─ testing / tính tương thích (compatibility / 호환성)
> └─ hiện đại (modern / 현대적) 2026 features
> ```

---

> **Nối mạch:** Beginner-to-Senior đã thiết lập thuật ngữ và mental model; supplement chỉ mở rộng các boundary còn thiếu. Canonical route tiếp theo xác định phần nào đã có owner để supplement không lặp lại.

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ chuyên môn được ưu tiên diễn đạt bằng tiếng Việt tự nhiên và giữ thuật ngữ gốc bên cạnh để dễ đối chiếu. Ví dụ: **cơ chế phân tầng (cascade)**, **độ đặc hiệu (specificity)**, **kế thừa (inheritance)**, **mô hình hộp (box model / 박스 모델)**, **luồng bố cục thông thường (normal flow / 일반 흐름)**, **ngữ cảnh định dạng (formatting context / 서식 컨텍스트)**, **khối chứa tham chiếu (containing block / 컨테이닝 블록)**, **định cỡ nội tại (intrinsic sizing / 내재 크기 결정)** và **ngữ cảnh xếp chồng (stacking context / 쌓임 맥락)**. Tên thuộc tính (property / 속성), giá trị (value / 값), selector, at-rule và API khi xuất hiện dưới dạng mã vẫn được giữ nguyên để không làm sai cú pháp.

# 0. chuẩn gốc (canonical / 정본) Beginner → cấp cao (senior / 시니어) đã đủ đến đâu?

# 0A. Master dấu vết (trace / 추적): từ bộ chọn (selector) matching đến rendering

Ở mức master, CSS là một chuỗi xử lý (pipeline / 파이프라인) có phụ thuộc (dependency / 의존성) chứ không phải một bộ thuộc tính (property / 속성). trình duyệt (browser / 브라우저) xây DOM/CSSOM, match bộ chọn (selector), áp cơ chế phân tầng (cascade) để tìm specified các giá trị (values), default/inherit những phần còn thiếu, tính computed/used các giá trị (values), tạo formatting cây (tree / 트리) và boxes, chạy thuật toán bố cục (layout algorithm), sau đó paint và composite. Một bug ở mỗi tầng có biểu hiện khác nhau: khai báo (declaration) bị crossed-out là cơ chế phân tầng (cascade) bài toán (problem / 문제); computed giá trị (value / 값) đúng nhưng hình học (geometry / 기하학) sai thường là sizing/bố cục (layout / 레이아웃) bài toán (problem / 문제); hình học (geometry / 기하학) đúng nhưng element bị che liên quan stacking/lớp trên cùng (top layer)/clip; frame chậm cần đo style/bố cục (layout / 레이아웃)/paint/composite.

Hiệu năng (performance / 성능) cũng nên được hiểu theo vô hiệu hóa (invalidation / 무효화) phạm vi (scope / 범위). Thay lớp (class / 클래스) ở ancestor có thể làm tính lại style (style recalculation) cho descendants liên quan; font metrics có thể thay kích thước nội tại (intrinsic size) và kéo bố cục (layout / 레이아웃); hình học (geometry / 기하학) changes có thể reflow; shadow/filter lớn có thể tăng chi phí vẽ (paint cost). `transform`/`opacity` thường phù hợp cho animation vì có thể tránh bố cục (layout / 레이아웃) trong nhiều trường hợp, nhưng tầng (layer / 계층) promotion không miễn phí. `contain` và `content-visibility` có thể giảm công việc (work / 작업) khi subtree thật sự độc lập, đồng thời chúng cũng thay đổi bố cục (layout / 레이아웃)/containment ngữ nghĩa (semantics / 의미론) nên không nên dùng như một “hiệu năng (performance / 성능) lớp (class / 클래스)” mặc định.

Khi rà soát (review / 검토) CSS môi trường vận hành (production / 운영 환경), hãy trả lời được bốn câu: khai báo (declaration) nào thắng, box/ngữ cảnh định dạng (formatting context / 서식 컨텍스트) nào được tạo, thuật toán bố cục (layout algorithm) nào quyết định hình học (geometry / 기하학), và thay đổi này invalidate phần nào của chuỗi xử lý kết xuất (rendering pipeline). Khi bốn câu đó rõ, phần lớn CSS trường hợp biên (edge case / 경계 사례) trở thành hành vi (behavior / 동작) có thể dự đoán.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, sau nội dung của **Quy ước thuật ngữ Việt–Anh**, **Chuẩn gốc (canonical / 정본) Beginner → cấp cao (senior / 시니어) đã cover rất tốt** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Nhưng “master CSS” còn cần** mở rộng hệ quả hoặc giới hạn liên quan.

## Chuẩn gốc (canonical / 정본) Beginner → cấp cao (senior / 시니어) đã cover rất tốt

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
selectors
cascade fundamentals
specificity
inheritance
box model
position
stacking context
Flexbox
Grid
Subgrid
responsive
container queries
custom properties
@layer
@scope
nesting
animation
transition
scroll-driven animations
view transitions
anchor positioning
modern colors
accessibility
performance
architecture
idioms
coding patterns
design patterns
```

Đó là đủ để:
- làm môi trường vận hành (production / 운영 환경) UI,
- đọc CSS khung phần mềm (framework / 프레임워크),
- gỡ lỗi (debug / 디버그) phần lớn bố cục (layout / 레이아웃) bugs,
- thiết kế thành phần (component / 컴포넌트) hệ thống (system / 시스템),
- rà soát (review / 검토) CSS ở mức cấp cao (senior / 시니어).

> **Nối mạch:** Canonical handbook đã cover syntax và patterns; supplement đi sâu vào declared value, computed value và used value để giải thích cascade thật.

## Nhưng “master CSS” còn cần

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
1. Visual Formatting Model sâu hơn
2. Property value processing
3. Intrinsic sizing algorithms
4. Replaced elements
5. Line boxes / inline formatting
6. Formatting contexts / fragmentation
7. Cascade origins + animation/transition precedence
8. Modern pseudo-classes / pseudo-elements
9. Dialog / Popover / Top Layer
10. Customizable native controls
11. Scroll containers / scrollbars / overscroll
12. Environment variables / safe areas / foldable screens
13. Advanced typography
14. Wide-gamut color / contrast-color()
15. Motion Path / additive animation
16. Advanced View Transition
17. CSSOM / Typed OM
18. Constructable Stylesheets
19. Shadow DOM styling
20. Custom Highlight API
21. SVG + CSS
22. Print / paged media / fragmentation
23. Counters / custom counter styles
24. Advanced feature queries
25. Browser compatibility strategy
26. Visual regression / CSS testing
27. CSS linting / dead-CSS strategy
28. Performance profiling methodology
```

---

---

# 0B. Priority thứ tự (order / 순서) của Master Supplement

Supplement này tiếp tục đúng trục của chuẩn gốc (canonical / 정본) ghi chú (note / 노트) nhưng chỉ mở sâu những chỗ quyết định khả năng gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경). Ưu tiên đầu tiên vẫn là cơ chế phân tầng (cascade): origin, importance, tầng (layer / 계층), độ đặc hiệu (specificity), độ gần phạm vi (scope proximity) và thứ tự nguồn (source order) phải được đọc như một quyết định (decision / 결정) hệ thống (system / 시스템). Sau đó mới tới thuộc tính (property / 속성) giá trị (value / 값) vòng đời (lifecycle / 생명주기), formatting cây (tree / 트리), định cỡ nội tại (intrinsic sizing / 내재 크기 결정) và các thuật toán bố cục (layout algorithms). Flex/Grid nâng cao chỉ có ý nghĩa khi bạn đã xác định đúng khối chứa tham chiếu (containing block / 컨테이닝 블록), available kích thước (size / 크기) và mức tối thiểu tự động (automatic minimum) các ràng buộc (constraints / 제약조건들).

Responsive ở mức master là vấn đề quyền sở hữu (ownership / 소유권): vùng nhìn (viewport) điều kiện (condition / 조건) thuộc page/môi trường (environment / 환경); bộ chứa (container / 컨테이너) điều kiện (condition / 조건) thuộc reusable thành phần (component / 컴포넌트); người dùng (user / 사용자) preferences thuộc khả năng tiếp cận (accessibility / 접근성)/môi trường (environment / 환경). hiện đại (modern / 현대적) CSS được chọn theo khả năng thay thế độ phức tạp (complexity / 복잡도) cũ chứ không theo độ mới. hiệu năng (performance / 성능) được đánh giá bằng style/bố cục (layout / 레이아웃)/paint/composite vô hiệu hóa (invalidation / 무효화) và khả năng tiếp cận (accessibility / 접근성) được coi là một ràng buộc (constraint / 제약조건) của bố cục (layout / 레이아웃)/trạng thái (state / 상태), không phải kiểm tra (audit / 감사) sau cùng.

Khi đọc bất kỳ chapter nào trong supplement, hãy luôn trả lời bốn câu: trình duyệt (browser / 브라우저) đang quyết định giá trị (value / 값) ở stage nào, box nào/ngữ cảnh định dạng (formatting context / 서식 컨텍스트) nào đang chịu trách nhiệm, API hiện đại có giảm độ phức tạp (complexity / 복잡도) hay chỉ đổi cú pháp (syntax / 문법), và hành vi (behavior / 동작) này có ảnh hưởng tới keyboard/zoom/chi phí kết xuất (rendering cost) không.

---

# 1. thuộc tính (property / 속성) giá trị (value / 값) vòng đời (lifecycle / 생명주기) [MUST][DEEP]

Một khai báo (declaration) không đi thẳng từ mã nguồn (source code / 소스 코드) đến pixels.

Mô hình tư duy (mental model / 사고 모델):

```text
Declared Value
→ Cascaded Value
→ Specified Value
→ Computed Value
→ Used Value
→ Actual Value
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **1.1 Declared giá trị (value / 값)** nối từ **Nhưng “master CSS” còn cần** sang **1.2 Cascaded giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.1 Declared giá trị (value / 값)

Tất cả các khai báo (declarations) có thể áp dụng:

```css
.card {
  width: 50%;
}

.card {
  width: 20rem;
}
```

Cả hai là declared các giá trị (values).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **1.2 Cascaded giá trị (value / 값)** nối từ **1.1 Declared giá trị (value / 값)** sang **1.3 Specified giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.2 Cascaded giá trị (value / 값)

cơ chế phân tầng (cascade) chọn khai báo (declaration) thắng.

```css
.card {
  width: 20rem;
}
```

có thể trở thành cascaded giá trị (value / 값).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **1.3 Specified giá trị (value / 값)** nối từ **1.2 Cascaded giá trị (value / 값)** sang **1.4 Computed giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.3 Specified giá trị (value / 값)

Nếu không có khai báo (declaration):
- inherit nếu thuộc tính (property / 속성) inherited,
- initial nếu không inherited,
- hoặc các defaulting quy tắc (rule / 규칙) khác.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **1.4 Computed giá trị (value / 값)** nối từ **1.3 Specified giá trị (value / 값)** sang **1.5 Used giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.4 Computed giá trị (value / 값)

Trình duyệt (browser / 브라우저) resolve những gì có thể resolve trước bố cục (layout / 레이아웃).

Ví dụ:

```css
font-size: 2em;
```

có thể computed thành:

```text
32px
```

nếu parent font-size = 16px.

Nhưng:

```css
width: 50%;
```

có thể chưa resolve thành px cho đến khi bố cục (layout / 레이아웃) ngữ cảnh (context / 맥락) rõ.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **1.5 Used giá trị (value / 값)** nối từ **1.4 Computed giá trị (value / 값)** sang **1.6 Actual giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.5 Used giá trị (value / 값)

Trình duyệt (browser / 브라우저) thực sự dùng trong bố cục (layout / 레이아웃).

Ví dụ:

```css
width: 50%;
```

Bộ chứa (container / 컨테이너) 800px:

```text
used width = 400px
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **1.6 Actual giá trị (value / 값)** nối từ **1.5 Used giá trị (value / 값)** sang **Cấp cao (senior / 시니어) lesson**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1.6 Actual giá trị (value / 값)

Giá trị cuối sau:
- rounding,
- thiết bị (device / 장치) điểm ảnh (pixel / 픽셀) các ràng buộc (constraints / 제약조건들),
- rendering hiện thực (implementation / 구현).

---

# 2. Invalid at Computed-Value thời gian (time / 시간) [DEEP]

Custom thuộc tính (property / 속성) có thể khiến khai báo (declaration) **parse hợp lệ nhưng computed invalid**.

Ví dụ:

```css
:root {
  --size: red;
}

.box {
  width: var(--size);
}
```

`var(--size)` parse được, nhưng:

```text
width: red
```

không hợp lệ.

Trình duyệt (browser / 브라우저) không nhất thiết phương án dự phòng (fallback) về khai báo (declaration) trước theo cách beginner thường nghĩ.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) lesson** nối từ **1.6 Actual giá trị (value / 값)** sang **Cấp cao (senior / 시니어) mẫu (pattern / 패턴)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) lesson

phương án dự phòng (fallback) phải nằm trong `var()` khi cần:

```css
.box {
  width: var(--size, 10rem);
}
```

Nhưng phương án dự phòng (fallback) chỉ dùng nếu custom thuộc tính (property / 속성):
- không tồn tại,
- hoặc invalid theo custom thuộc tính (property / 속성) ngữ nghĩa (semantics / 의미론) phù hợp.

`@property` giúp kiểu (type / 타입) custom thuộc tính (property / 속성) từ sớm.

---

# 3. cơ chế phân tầng (cascade) Origins — Full mô hình tư duy (mental model / 사고 모델) [MUST]

Chuẩn gốc (canonical / 정본) ghi chú (note / 노트) đã giải thích cơ chế phân tầng (cascade); ở mức master cần hiểu **origin precedence**.

Nguồn CSS:

```text
User-agent styles
User styles
Author styles
Animations
Important declarations
Transitions
```

Simplified precedence từ thấp → cao:

```text
user-agent normal
user normal
author normal
keyframe animations
author !important
user !important
user-agent !important
transitions
```

Điểm rất dễ quên:

> chuyển tiếp (transition / 전이) các giá trị (values) có precedence cực cao trong cơ chế phân tầng (cascade) khi chuyển tiếp (transition / 전이) đang chạy.

---

# 4. các lớp phân tầng (cascade layers) và `!important` đảo thứ tự [DEEP]

Normal tầng (layer / 계층) thứ tự (order / 순서):

```css
@layer reset, base, components, utilities;
```

Normal các khai báo (declarations):

```text
reset
< base
< components
< utilities
< unlayered
```

Nhưng với `!important`, thứ tự tầng (layer / 계층) **đảo lại**.

Điều này tồn tại để:
- bảo vệ foundational important rules,
- tránh tầng (layer / 계층) mới dễ override important defaults.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) mẫu (pattern / 패턴)** nối từ **Cấp cao (senior / 시니어) lesson** sang **Important**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) mẫu (pattern / 패턴)

Nếu buộc phải maintain third-party important CSS:

```css
@layer importantOverrides {
  ...
}
```

Đừng rải `!important` vào mọi tầng (layer / 계층).

---

# 5. độ gần phạm vi (scope proximity) [hiện đại (modern / 현대적)][DEEP]

Trong `@scope`, nếu:
- origin bằng nhau,
- tầng (layer / 계층) bằng nhau,
- độ đặc hiệu (specificity) bằng nhau,

Trình duyệt (browser / 브라우저) có thể xét **độ gần phạm vi (scope proximity)** trước thứ tự nguồn (source order).

Concept:

```css
@scope (.outer) {
  .title {
    color: blue;
  }
}

@scope (.inner) {
  .title {
    color: red;
  }
}
```

Nếu `.title` gần `.inner` phạm vi (scope / 범위) gốc (root / 루트) hơn, scoped quy tắc (rule / 규칙) gần hơn có thể thắng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Important** nối từ **Cấp cao (senior / 시니어) mẫu (pattern / 패턴)** sang **Master lesson**, vì cơ chế trước tạo đầu vào cho bước sau.

## Important

`@scope` **không tự tăng độ đặc hiệu (specificity)**.

Nhưng tường minh (explicit / 명시적) `:scope` thì có độ đặc hiệu (specificity) như lớp giả (pseudo-class).

---

# 6. Direct mục tiêu (target / 대상) vs kế thừa (inheritance) [DEEP]

Quy tắc (rule / 규칙) trực tiếp mục tiêu (target / 대상) element luôn thắng inherited giá trị (value / 값).

```css
#parent {
  color: green;
}

h1 {
  color: purple;
}
```

`h1` màu purple.

Không quan trọng:

```text
#parent specificity rất cao

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.
```

vì inherited giá trị (value / 값) không cạnh tranh độ đặc hiệu (specificity) trực tiếp với quy tắc (rule / 규칙) mục tiêu (target / 대상) `h1`.

---

# 7. Formatting cây (tree / 트리) vs DOM cây (tree / 트리) [MUST][DEEP]

CSS bố cục (layout / 레이아웃) không hoàn toàn chạy trên DOM cây (tree / 트리).

Trình duyệt (browser / 브라우저) tạo **box cây (tree / 트리) / formatting cấu trúc (structure / 구조)**.

Một element có thể:
- tạo một box,
- tạo nhiều boxes,
- không tạo box,
- tạo anonymous boxes.

Ví dụ:

```css
display: contents;
```

element box có thể biến mất nhưng children vẫn bố cục (layout / 레이아웃).

các phần tử giả (pseudo-elements):

```css
::before
::after
```

tạo generated boxes dù không có DOM nút (node / 노드) tương ứng như element bình thường.

---

# 8. Anonymous Boxes [DEEP]

Trình duyệt (browser / 브라우저) có thể tạo box không có corresponding HTML element.

Ví dụ mixed khối (block / 블록)/inline content có thể tạo anonymous khối (block / 블록) boxes.

Bạn hiếm khi style trực tiếp anonymous box, nhưng nó giải thích:
- bố cục (layout / 레이아웃) hành vi (behavior / 동작) khó hiểu,
- các hộp dòng (line boxes),
- bảng (table / 테이블) anonymous wrappers.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Master lesson** nối từ **Important** sang **BFC giải quyết**, vì cơ chế trước tạo đầu vào cho bước sau.

## Master lesson

DOM cây (tree / 트리) ≠ bố cục (layout / 레이아웃) cây (tree / 트리).

Khi CSS hành vi (behavior / 동작) lạ, đừng assume mỗi HTML element = đúng 1 rectangle.

---

# 9. các ngữ cảnh định dạng (formatting contexts) [MUST]

Các các ngữ cảnh định dạng (formatting contexts) quan trọng:

```text
Block Formatting Context (BFC)
Inline Formatting Context (IFC)
Flex Formatting Context
Grid Formatting Context
Table Formatting Context
Ruby Formatting Context
```

Ngữ cảnh định dạng (formatting context / 서식 컨텍스트) định nghĩa:
- children bố cục (layout / 레이아웃) như thế nào,
- margin tương tác (interaction / 상호작용),
- float hành vi (behavior / 동작),
- alignment,
- đường cơ sở (baseline).

---

# 10. ngữ cảnh định dạng khối (block formatting context) (BFC) [MUST]

BFC là một vùng bố cục (layout / 레이아웃) khối (block / 블록) tương đối độc lập.

Một số cách tạo BFC:

```css
display: flow-root;
overflow: auto;
overflow: hidden;
float: left;
position: absolute;
display: inline-block;
display: flex; /* flex container creates its own context */
display: grid;
```

Không phải mọi cách tạo BFC đều có ngữ nghĩa (semantics / 의미론) giống nhau.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **BFC giải quyết** nối từ **Master lesson** sang **Idiom**, vì cơ chế trước tạo đầu vào cho bước sau.

## BFC giải quyết

### Float containment

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.container {
  display: flow-root;
}
```

### Tránh văn bản (text / 텍스트) wrap quanh float ngoài ý muốn

BFC mới không wrap quanh bên ngoài (external / 외부) float theo cách normal khối (block / 블록) có thể làm.

### Margin tương tác (interaction / 상호작용)

BFC ảnh hưởng gộp lề (margin collapsing) hành vi (behavior / 동작).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Idiom** nối từ **BFC giải quyết** sang **Inline icon alignment**, vì cơ chế trước tạo đầu vào cho bước sau.

## Idiom

Nếu chỉ muốn tạo BFC:

```css
display: flow-root;
```

thường rõ nghĩa hơn:

```css
overflow: hidden;
```

vì `overflow:hidden` có thêm clipping tác dụng phụ (side effect).

---

# 11. ngữ cảnh định dạng nội dòng (inline formatting context) & các hộp dòng (line boxes) [MUST][DEEP]

Văn bản (text / 텍스트) inline không bố cục (layout / 레이아웃) như Flexbox.

Trình duyệt (browser / 브라우저) tạo **các hộp dòng (line boxes)**.

Trong một paragraph:

```html
<p>
  Hello <strong>world</strong> this is text.
</p>
```

Trình duyệt (browser / 브라우저):
- split inline content,
- tạo các hộp dòng (line boxes),
- align inline-level boxes theo đường cơ sở (baseline).

Các các thuộc tính (properties) quan trọng:

```text
line-height
vertical-align
font metrics
white-space
word-break
overflow-wrap
text-align
```

---

# 12. `vertical-align` — thuộc tính (property / 속성) thường bị hiểu sai [MUST]

`vertical-align` **không phải general-purpose vertical centering thuộc tính (property / 속성)**.

Nó chủ yếu áp dụng cho:
- inline-level boxes,
- bảng (table / 테이블) cells.

các giá trị (values):

```text
baseline
middle
top
bottom
text-top
text-bottom
sub
super
<length>
<percentage>
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Inline icon alignment** nối từ **Idiom** sang **Không nên**, vì cơ chế trước tạo đầu vào cho bước sau.

## Inline icon alignment

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.icon {
  vertical-align: -0.125em;
}
```

có thể dùng để optical align icon với văn bản (text / 텍스트).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Không nên** nối từ **Inline icon alignment** sang **Cấp cao (senior / 시니어) ghi chú (note / 노트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Không nên

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
div {
  vertical-align: middle;
}
```

mong khối (block / 블록) element tự center trong parent.

Dùng Flex/Grid cho bố cục (layout / 레이아웃) center.

---

# 13. đường cơ sở (baseline) Alignment [DEEP]

Flex/Grid hỗ trợ:

```css
align-items: baseline;
```

Nhưng đường cơ sở (baseline) được lấy từ content/font/box rules.

Đây là lý do:

```css
.icon + label
```

có thể trông không thẳng dù geometric center giống nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) ghi chú (note / 노트)** nối từ **Không nên** sang **Điểm đặc biệt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) ghi chú (note / 노트)

Typography alignment ≠ geometric center.

UI có văn bản (text / 텍스트) thường cần **đường cơ sở (baseline) alignment** hơn center alignment.

---

# 14. các phần tử thay thế (replaced elements) [MUST]

phần tử thay thế (replaced element) là element mà nội dung kết xuất (render / 렌더링) bên trong được thay bởi bên ngoài (external / 외부) tài nguyên (resource / 자원)/content.

Dùng chung (common / 공통):

```text
<img>
<video>
<iframe>
<embed>
```

Một số cases khác tùy element/kiểu (type / 타입).

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Điểm đặc biệt** nối từ **Cấp cao (senior / 시니어) ghi chú (note / 노트)** sang **Mẫu (pattern / 패턴)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Điểm đặc biệt

các phần tử thay thế (replaced elements) có thể có:
- intrinsic width,
- intrinsic height,
- intrinsic aspect ratio.

Ví dụ ảnh (image / 이미지) tệp (file / 파일):

```text
1200 × 800
```

intrinsic ratio:

```text
3 / 2
```

---

# 15. kích thước nội tại (intrinsic dimensions) [MUST]

Đối với `<img>`:

```html
<img src="photo.jpg" alt="">
```

nếu không CSS sizing, trình duyệt (browser / 브라우저) có thể dùng kích thước nội tại (intrinsic dimensions).

Nếu HTML có:

```html
<img
  src="photo.jpg"
  width="1200"
  height="800"
  alt=""
>
```

Trình duyệt (browser / 브라우저) có thể reserve aspect ratio sớm, giảm CLS.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Mẫu (pattern / 패턴)** nối từ **Điểm đặc biệt** sang **object-position**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
img {
  max-width: 100%;
  height: auto;
}
```

giữ intrinsic aspect ratio khi co.

---

# 16. phần tử thay thế (replaced element) + `object-fit` [DEEP]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.media {
  width: 300px;
  height: 200px;
  object-fit: cover;
}
```

Phân biệt:

```text
element box size
vs
content object size
```

`object-fit` thay đổi cách **tài nguyên (resource / 자원) bên trong box** fit.

Nó không thay bố cục (layout / 레이아웃) kích thước (size / 크기) của element như `width`/`height`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **object-position** nối từ **Mẫu (pattern / 패턴)** sang **Cấp cao (senior / 시니어) gỡ lỗi (debugging) question**, vì cơ chế trước tạo đầu vào cho bước sau.

## `object-position`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
img {
  object-fit: cover;
  object-position: 50% 20%;
}
```

Useful giữ khuôn mặt ở vùng crop mong muốn.

---

# 17. Definite vs kích thước chưa xác định (indefinite size) [MUST][DEEP]

Một kích thước (size / 크기) có thể là **definite** hoặc không.

Điều này ảnh hưởng:
- percentage resolution,
- Grid/Flex sizing,
- percentage height,
- định cỡ nội tại (intrinsic sizing / 내재 크기 결정).

Ví dụ:

```css
.parent {
  height: auto;
}

.child {
  height: 50%;
}
```

`50%` có thể không resolve như người dùng (user / 사용자) mong đợi vì parent block-size không definite.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) gỡ lỗi (debugging) question** nối từ **object-position** sang **Intrinsic**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) gỡ lỗi (debugging) question

> khối chứa tham chiếu (containing block / 컨테이닝 블록) có kích thước xác định (definite size) trên axis này không?

---

# 18. Intrinsic vs định cỡ ngoại tại (extrinsic sizing) [MUST]

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Intrinsic** nối từ **Cấp cao (senior / 시니어) gỡ lỗi (debugging) question** sang **Extrinsic**, vì cơ chế trước tạo đầu vào cho bước sau.

## Intrinsic

Kích thước (size / 크기) dựa trên content:

```text
min-content
max-content
fit-content
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Extrinsic** nối từ **Intrinsic** sang **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Extrinsic

Kích thước (size / 크기) bị bên ngoài (external / 외부) ràng buộc (constraint / 제약조건) quyết định:

```css
width: 20rem;
width: 50%;
```

Cấp cao (senior / 시니어) cần hiểu hai loại đang cạnh tranh.

---

# 19. `min-content` sâu hơn [DEEP]

`min-content` gần với:

> kích thước nhỏ nhất content có thể co theo wrapping opportunities tự nhiên.

Văn bản (text / 텍스트):

```text
CSS is awesome
```

min-content width thường gần longest unbreakable segment.

Nếu có:

```css
overflow-wrap: anywhere;
```

min-content contribution có thể khác.

---

# 20. `max-content` sâu hơn [DEEP]

`max-content` gần với:

> kích thước (size / 크기) nếu content không wrap vì không gian khả dụng (available space).

Có thể gây overflow mạnh với:
- long labels,
- tables,
- mã (code / 코드),
- URLs.

---

# 21. `fit-content` sâu hơn [DEEP]

Conceptually nó clamp giữa intrinsic extremes và không gian khả dụng (available space).

Mô hình tư duy (mental model / 사고 모델) gần:

```text
min(
  max-content,
  max(min-content, available-size)
)
```

Đây không phải replacement chính xác cho mọi spec formula, nhưng là mô hình (model / 모델) học tốt.

---

# 22. Shrink-to-fit Sizing [DEEP]

Một số boxes như:
- floats,
- absolute positioned elements với auto width,
- inline-block,

có thể dùng hành vi (behavior / 동작) gần **shrink-to-fit**.

Mô hình tư duy (mental model / 사고 모델):

```text
không rộng hơn available space
không nhỏ hơn min-content
không vượt quá max-content nếu không cần
```

Đây là lý do:

```css
display: inline-block;
```

không chiếm full width như khối (block / 블록).

---

# 23. kích thước tối thiểu tự động (automatic minimum size) in Flex/Grid [MUST]

Chuẩn gốc (canonical / 정본) ghi chú (note / 노트) đã có `min-width:0`.

Master cần hiểu **vì sao**.

Flex/phần tử Grid (grid item) có kích thước tối thiểu tự động (automatic minimum size) hành vi (behavior / 동작) để tránh content bị ép quá mức.

Do đó:

```css
.item {
  min-width: auto;
}
```

có thể effectively dựa vào content contribution.

Fix:

```css
.item {
  min-width: 0;
}
```

nói với sizing thuật toán (algorithm / 알고리즘):

> item được phép co xuống dưới content-based mức tối thiểu tự động (automatic minimum).

---

# 24. Percentage Resolution Edge Cases [DEEP]

`%` không có một quy tắc (rule / 규칙) universal.

Nó phụ thuộc thuộc tính (property / 속성).

Ví dụ:
- width `%` thường relative khối chứa tham chiếu (containing block / 컨테이닝 블록) inline kích thước (size / 크기).
- percentage transforms relative transform tham chiếu (reference / 참조) box.
- percentage border-radius relative box dimension.
- percentage translate relative element itself.
- percentage background-position có thuật toán (algorithm / 알고리즘) riêng.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nối từ **Extrinsic** sang **Không collapse giữa flex/các phần tử Grid (grid items)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Không học `%` như đơn vị (unit / 단위).

Học `%` **theo từng thuộc tính (property / 속성) family**.

---

# 25. gộp lề (margin collapse) — Deep Cases [DEEP]

Vertical margins có thể collapse:
- adjacent siblings,
- parent + first/last child trong conditions phù hợp,
- empty blocks.

Negative margins cũng tham gia collapsing thuật toán (algorithm / 알고리즘).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Không collapse giữa flex/các phần tử Grid (grid items)** nối từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sang **Mẫu (pattern / 패턴)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Không collapse giữa flex/các phần tử Grid (grid items)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.container {
  display: flex;
}
```

child margins không collapse như normal khối (block / 블록) luồng (flow / 흐름).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Mẫu (pattern / 패턴)** nối từ **Không collapse giữa flex/các phần tử Grid (grid items)** sang **Print / columns**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mẫu (pattern / 패턴)

Cho spacing hệ thống (system / 시스템):

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
```

`gap` predictable hơn gộp lề (margin collapse).

---

# 26. Float — đúng bản chất [DEEP]

Float không chỉ là legacy bố cục (layout / 레이아웃).

Use trường hợp (case / 사례) thực sự:

> cho văn bản (text / 텍스트) inline wrap xung quanh đối tượng (object / 객체).

```css
.article img {
  float: inline-start;
  margin-inline-end: 1rem;
  margin-block-end: .5rem;
}
```

`shape-outside` có thể thay vùng wrap:

```css
figure {
  float: left;
  shape-outside: circle(50%);
}
```

---

# 27. Fragmentation [DEEP]

Content có thể bị split qua:
- pages,
- columns,
- regions/fragmentainers.

các thuộc tính (properties):

```text
break-before
break-after
break-inside
orphans
widows
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Print / columns** nối từ **Mẫu (pattern / 패턴)** sang **Privacy ghi chú (note / 노트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Print / columns

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card {
  break-inside: avoid;
}
```

Có thể giúp card không bị chia giữa cột/page.

Không phải trình duyệt (browser / 브라우저) luôn đảm bảo 100% nếu ràng buộc (constraint / 제약조건) không thể thỏa.

---

# 28. `orphans` và `widows` [ADV]

Dùng trong paged/multicol typography.

```css
p {
  orphans: 3;
  widows: 3;
}
```

- `orphans`: minimum lines ở cuối fragment trước break.
- `widows`: minimum lines ở đầu fragment sau break.

Useful:
- print,
- long-form publishing.

---

# 29. Advanced các bộ chọn (selectors) — `:nth-child(... of S)` [hiện đại (modern / 현대적)]

Có thể filter subset trước khi đếm.

```css
.item:nth-child(2n of .visible) {
  background: #f5f5f5;
}
```

Khác:

```css
.item.visible:nth-child(2n)
```

Câu đầu:
- đếm **chỉ `.visible`**.

Đây là rất hữu ích cho zebra stripes khi có hidden/filter rows.

---

# 30. `:dir()` [ADV]

Match directionality:

```css
:dir(rtl) .icon-next {
  rotate: 180deg;
}
```

Tốt hơn tự gắn `.rtl` trong nhiều trường hợp (case / 사례).

---

# 31. `:lang()` [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
:lang(ko) {
  word-break: keep-all;
}

:lang(ja) {
  line-break: strict;
}
```

Styling theo document ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론).

---

# 32. Link các lớp giả (pseudo-classes) sâu hơn

Dùng chung (common / 공통):

```text
:any-link
:link
:visited
```

`:any-link` match link có href bất kể visited trạng thái (state / 상태).

```css
:any-link {
  text-underline-offset: .15em;
}
```

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Privacy ghi chú (note / 노트)** nối từ **Print / columns** sang **:user-invalid**, vì cơ chế trước tạo đầu vào cho bước sau.

## Privacy ghi chú (note / 노트)

`:visited` bị trình duyệt (browser / 브라우저) hạn chế style/truy vấn (query / 쿼리) vì lịch sử (history / 이력) privacy.

Đừng dựa vào computed visited styles cho ứng dụng (application / 애플리케이션) lô-gic (logic / 논리).

---

# 33. Form trạng thái (state / 상태) các lớp giả (pseudo-classes) mở rộng [ADV]

Ngoài chuẩn gốc (canonical / 정본) Beginner → cấp cao (senior / 시니어):

```text
:user-valid
:user-invalid
:indeterminate
:default
:in-range
:out-of-range
:read-write
:autofill
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **:user-invalid** nối từ **Privacy ghi chú (note / 노트)** sang **:open**, vì cơ chế trước tạo đầu vào cho bước sau.

## `:user-invalid`

Khác `:invalid`:

- `:invalid` có thể match ngay.
- `:user-invalid` phản ánh invalidity sau người dùng (user / 사용자) tương tác (interaction / 상호작용) theo trình duyệt (browser / 브라우저) hành vi (behavior / 동작).

Mẫu (pattern / 패턴):

```css
input:user-invalid {
  border-color: var(--color-danger);
}
```

UX thường tốt hơn đỏ form ngay khi page tải (load / 로드).

---

# 34. Element Display trạng thái (state / 상태) các lớp giả (pseudo-classes) [2026]

Quan trọng:

```text
:open
:popover-open
:modal
:fullscreen
:picture-in-picture
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **:open** nối từ **:user-invalid** sang **:popover-open**, vì cơ chế trước tạo đầu vào cho bước sau.

## `:open`

Match element có open/closed trạng thái (state / 상태) và hiện đang open.

Ví dụ:

```css
details:open > summary {
  font-weight: 700;
}
```

Hoặc hiện đại (modern / 현대적) bản địa (native / 네이티브) controls/open UI khi applicable.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **:popover-open** nối từ **:open** sang **:modal**, vì cơ chế trước tạo đầu vào cho bước sau.

## `:popover-open`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
[popover]:popover-open {
  opacity: 1;
}
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **:modal** nối từ **:popover-open** sang **Mẫu thiết kế (design pattern / 디자인 패턴) — Presentation phạm vi (range / 범위)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `:modal`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
dialog:modal {
  border: 0;
}
```

---

# 35. Media trạng thái (state / 상태) các lớp giả (pseudo-classes) [2026]

Interop 2026 chú ý tới media các lớp giả (pseudo-classes):

```text
:playing
:paused
:seeking
:buffering
:stalled
:muted
:volume-locked
```

Concept:

```css
video:playing {
  outline-color: green;
}
```

Use trường hợp (case / 사례):
- custom media UI,
- declarative visual trạng thái (state / 상태).

⚠ Kiểm tra trình duyệt (browser / 브라우저) mục tiêu (target / 대상) vì đây là vùng interoperability đang tiếp tục cải thiện.

---

# 36. Highlight các phần tử giả (pseudo-elements) [hiện đại (modern / 현대적)]

Ngoài `::selection`:

```text
::target-text
::spelling-error
::grammar-error
::highlight(name)
```

Ví dụ:

```css
::spelling-error {
  text-decoration: wavy red underline;
}
```

Hỗ trợ (support / 지원)/allowed các thuộc tính (properties) có giới hạn tùy highlight kiểu (type / 타입).

---

# 37. CSS API tô sáng tùy chỉnh (Custom Highlight API) [hiện đại (modern / 현대적)]

Cho phép style arbitrary văn bản (text / 텍스트) ranges **không cần wrap thêm span**.

JS:

```js
const range = new Range();
range.setStart(textNode, 10);
range.setEnd(textNode, 20);

const highlight = new Highlight(range);
CSS.highlights.set("search-result", highlight);
```

CSS:

```css
::highlight(search-result) {
  background: gold;
  color: black;
}
```

Use cases:
- editor,
- tìm kiếm (search / 검색) results,
- cú pháp (syntax / 문법) tooling,
- collaboration annotations.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Mẫu thiết kế (design pattern / 디자인 패턴) — Presentation phạm vi (range / 범위)** nối từ **:modal** sang **Important**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mẫu thiết kế (design pattern / 디자인 패턴) — Presentation phạm vi (range / 범위)

Không mutate DOM chỉ để highlight văn bản (text / 텍스트).

```text
Range model
→ Highlight registry
→ CSS presentation
```

⚠ Highlight không tự tạo mang tính ý nghĩa (semantic meaning / 의미적 뜻) cho khả năng tiếp cận (accessibility / 접근성).

---

# 38. lớp trên cùng (top layer) [MUST][hiện đại (modern / 현대적)]

Trình duyệt (browser / 브라우저) có một rendering concept gọi là **lớp trên cùng (top layer)**.

Elements như:
- modal dialog,
- popovers,
- fullscreen element,

có thể nằm ở lớp trên cùng (top layer).

Điều này giúp tránh:

```text
z-index war
overflow clipping ancestor
stacking context traps
```

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Important** nối từ **Mẫu thiết kế (design pattern / 디자인 패턴) — Presentation phạm vi (range / 범위)** sang **Dialog sizing mẫu (pattern / 패턴)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Important

lớp trên cùng (top layer) không phải:

```css
z-index: 999999;
```

Nó là riêng một browser-managed tầng (layer / 계층) ngoài document các ngữ cảnh xếp chồng (stacking contexts) thông thường.

---

# 39. `<dialog>` Styling sâu hơn [MUST]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
dialog {
  border: 0;
  border-radius: 1rem;
}

dialog::backdrop {
  background: rgb(0 0 0 / .5);
}
```

Trạng thái (state / 상태):

```css
dialog:modal {}
dialog:open {}
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Dialog sizing mẫu (pattern / 패턴)** nối từ **Important** sang **Cấp cao (senior / 시니어) lesson**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dialog sizing mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
dialog {
  inline-size: min(90vw, 40rem);
  max-block-size: 80dvh;
  overflow: auto;
}
```

---

# 40. Popover Styling [MUST][hiện đại (modern / 현대적)]

Popover:

```html
<div id="menu" popover>...</div>
```

CSS:

```css
[popover] {
  border: 0;
}

[popover]:popover-open {
  opacity: 1;
}
```

Popover được trình duyệt (browser / 브라우저) xử lý:
- lớp trên cùng (top layer),
- dismiss hành vi (behavior / 동작) tùy chế độ (mode / 모드),
- stacking.

2026 còn có hướng mở rộng như `popover="hint"` cho tooltip-like hierarchy.

---

# 41. Entry / chuyển tiếp khi rời đi (exit transition) cho lớp trên cùng (top layer) [hiện đại (modern / 현대적)]

Vấn đề:

```text
display:none
→ element xuất hiện
```

trước đây khó chuyển tiếp (transition / 전이) clean.

Hiện đại (modern / 현대적) toolset:

```text
@starting-style
transition-behavior: allow-discrete
overlay
display
```

Concept:

```css
dialog {
  opacity: 1;
  transition:
    opacity .2s,
    display .2s allow-discrete,
    overlay .2s allow-discrete;
}

@starting-style {
  dialog:open {
    opacity: 0;
  }
}
```

Exit/entry chính xác (exact / 정확한) cú pháp (syntax / 문법) cần kiểm thử (test / 테스트) theo mục tiêu (target / 대상) browsers.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) lesson** nối từ **Dialog sizing mẫu (pattern / 패턴)** sang **Picker**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) lesson

Đừng fake dialog chuyển tiếp (transition / 전이) bằng JS hết thời gian chờ (timeout / 타임아웃) nếu nền tảng (platform / 플랫폼) đã hỗ trợ (support / 지원) vòng đời (lifecycle / 생명주기) declaratively.

---

# 42. Customizable `<select>` [2026][hiện đại (modern / 현대적)]

Hiện đại (modern / 현대적) CSS cho phép opt-in vào customizable select trong mức hỗ trợ trình duyệt (browser support / 브라우저 지원) phù hợp.

```css
select,
::picker(select) {
  appearance: base-select;
}
```

Key pieces:

```text
appearance: base-select
::picker(select)
::picker-icon
::checkmark
:open
:checked
```

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Picker** nối từ **Cấp cao (senior / 시니어) lesson** sang **Option**, vì cơ chế trước tạo đầu vào cho bước sau.

## Picker

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
::picker(select) {
  border: 1px solid #ddd;
  border-radius: .75rem;
}
```

Picker hoạt động giống top-layer popover.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Option** nối từ **Picker** sang **Mẫu (pattern / 패턴) — Native-first customization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Option

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
option:checked {
  font-weight: 700;
}
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Mẫu (pattern / 패턴) — Native-first customization** nối từ **Option** sang **hidden**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mẫu (pattern / 패턴) — Native-first customization

Trước:
- recreate select bằng div + JS + ARIA.

Hiện đại (modern / 현대적) chiến lược (strategy / 전략):
1. dùng bản địa (native / 네이티브) `<select>`,
2. customize khi hỗ trợ (support / 지원),
3. phương án dự phòng (fallback) bản địa (native / 네이티브) style khi không hỗ trợ (support / 지원).

---

# 43. Feature-detect Custom Select

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@supports (appearance: base-select) {
  select,
  ::picker(select) {
    appearance: base-select;
  }
}
```

Mẫu thiết kế (design pattern / 디자인 패턴):

```text
Native semantics
→ progressive visual enhancement
```

Rất đáng ưu tiên hơn custom widget nếu requirements cho phép.

---

# 44. `field-sizing` [hiện đại (modern / 현대적)]

Cho form điều khiển (control / 제어) kích thước (size / 크기) theo content trong hỗ trợ (support / 지원) phù hợp.

Concept:

```css
textarea {
  field-sizing: content;
}
```

Use cases:
- auto-growing textarea,
- content-sized đầu vào (input / 입력).

⚠ Cần các ràng buộc (constraints / 제약조건들):

```css
textarea {
  field-sizing: content;
  min-height: 4lh;
  max-height: 12lh;
}
```

---

# 45. vùng chứa cuộn (scroll container) mô hình tư duy (mental model / 사고 모델) [MUST]

Element có overflow có thể trở thành vùng chứa cuộn (scroll container).

Điều này ảnh hưởng:
- sticky,
- scroll snap,
- hoạt ảnh điều khiển bằng cuộn (scroll-driven animation),
- overscroll,
- scroll padding.

Gỡ lỗi (debug / 디버그):

```text
Element nào thực sự scroll?
Viewport hay ancestor?
```

---

# 46. `overflow: hidden` vs `clip` [DEEP]

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **hidden** nối từ **Mẫu (pattern / 패턴) — Native-first customization** sang **clip**, vì cơ chế trước tạo đầu vào cho bước sau.

## `hidden`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
overflow: hidden;
```

- clip content,
- có vùng chứa cuộn (scroll container) ngữ nghĩa (semantics / 의미론) trong nhiều contexts,
- programmatic scrolling có thể liên quan.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **clip** nối từ **hidden** sang **Mẫu (pattern / 패턴) — Modal scroll containment**, vì cơ chế trước tạo đầu vào cho bước sau.

## `clip`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
overflow: clip;
```

- clip overflow,
- không tạo vùng chứa cuộn (scroll container) giống `hidden`.

Nếu mục tiêu chỉ là clipping:

```css
overflow: clip;
```

có thể mang tính ngữ nghĩa (semantic / 의미적) hơn.

---

# 47. Overscroll hành vi (behavior / 동작) [ADV]

các thuộc tính (properties):

```text
overscroll-behavior
overscroll-behavior-x
overscroll-behavior-y
overscroll-behavior-inline
overscroll-behavior-block
```

các giá trị (values):

```text
auto
contain
none
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Mẫu (pattern / 패턴) — Modal scroll containment** nối từ **clip** sang **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mẫu (pattern / 패턴) — Modal scroll containment

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.modal-body {
  overflow: auto;
  overscroll-behavior: contain;
}
```

Ngăn scroll chuỗi (chain / 사슬) ra page trong nhiều cases.

---

# 48. Scrollbar Gutter [hiện đại (modern / 현대적)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
html {
  scrollbar-gutter: stable;
}
```

Mục tiêu:
- reserve scrollbar không gian (space / 공간),
- giảm dịch chuyển bố cục (layout shift) khi scrollbar xuất hiện.

Giá trị (value / 값) hữu ích:

```text
auto
stable
stable both-edges
```

⚠ Overlay scrollbar platforms có hành vi (behavior / 동작) khác classic scrollbar platforms.

---

# 49. Scrollbar Styling

Tiêu chuẩn (standard / 표준) các thuộc tính (properties):

```css
* {
  scrollbar-width: thin;
  scrollbar-color: #888 transparent;
}
```

Browser-specific legacy các phần tử giả (pseudo-elements) như:

```css
::-webkit-scrollbar
```

vẫn thấy trong mã (code / 코드) cũ nhưng không phải portable tiêu chuẩn (standard / 표준) API.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nối từ **Mẫu (pattern / 패턴) — Modal scroll containment** sang **scroll-margin**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Scrollbar styling là enhancement, không được làm scrollbar khó nhìn/khó dùng.

---

# 50. neo vị trí cuộn (scroll anchoring) [ADV]

Trình duyệt (browser / 브라우저) có thể giữ vùng nhìn (viewport) ổn định khi content phía trên thay đổi.

Thuộc tính (property / 속성):

```css
overflow-anchor
```

Ví dụ opt-out:

```css
.dynamic-region {
  overflow-anchor: none;
}
```

Chỉ dùng khi neo vị trí cuộn (scroll anchoring) tự động gây UX sai.

Đừng disable toàn cục (global / 전역).

---

# 51. `scroll-margin` vs `scroll-padding` [MUST]

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **scroll-margin** nối từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sang **scroll-padding**, vì cơ chế trước tạo đầu vào cho bước sau.

## `scroll-margin`

Set trên mục tiêu (target / 대상):

```css
section {
  scroll-margin-top: 5rem;
}
```

Useful khi sticky header che anchor.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **scroll-padding** nối từ **scroll-margin** sang **font-variant-**, vì cơ chế trước tạo đầu vào cho bước sau.

## `scroll-padding`

Set trên vùng chứa cuộn (scroll container):

```css
html {
  scroll-padding-top: 5rem;
}
```

Nói:

> optimal visible scrollport bắt đầu sau 5rem.

---

# 52. `touch-action` [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.carousel {
  touch-action: pan-y;
}
```

Cho trình duyệt (browser / 브라우저) biết gestures nào được phép.

các giá trị (values) dùng chung (common / 공통):

```text
auto
none
pan-x
pan-y
pinch-zoom
manipulation
```

Cực quan trọng với custom drag/gesture components.

⚠ `touch-action:none` có thể phá bản địa (native / 네이티브) zoom/scroll khả năng tiếp cận (accessibility / 접근성).

---

# 53. môi trường (environment / 환경) các biến (variables) `env()` [MUST][hiện đại (modern / 현대적)]

Khác CSS custom thuộc tính (property / 속성):

```css
var(--token)
```

`env()` lấy môi trường (environment / 환경) biến (variable) từ trình duyệt (browser / 브라우저)/thiết bị (device / 장치).

Example:

```css
padding-bottom:
  env(safe-area-inset-bottom);
```

---

# 54. vùng an toàn (safe area) Insets [MUST]

Trên devices có notch/home indicator:

```text
safe-area-inset-top
safe-area-inset-right
safe-area-inset-bottom
safe-area-inset-left
```

Mẫu (pattern / 패턴):

```css
.bottom-bar {
  padding-bottom:
    max(1rem, env(safe-area-inset-bottom));
}
```

Đảm bảo controls không chạm home indicator.

---

# 55. Foldable / Multi-segment Viewports [ADV]

Môi trường (environment / 환경) các biến (variables) có thể expose:

```text
viewport-segment-width
viewport-segment-height
viewport-segment-top
viewport-segment-right
viewport-segment-bottom
viewport-segment-left
```

Use trường hợp (case / 사례):
- foldable thiết bị (device / 장치),
- dual-screen bố cục (layout / 레이아웃).

Không cần ưu tiên học sớm, nhưng master CSS phải biết nền tảng (platform / 플랫폼) có concept này.

---

# 56. Advanced Typography — Font tính năng (feature / 기능) điều khiển (control / 제어) [ADV]

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **font-variant-** nối từ **scroll-padding** sang **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `font-variant-*`

Ưu tiên high-level các thuộc tính (properties) khi có:

```css
font-variant-numeric: tabular-nums;
```

Options thường gặp:

```text
lining-nums
oldstyle-nums
proportional-nums
tabular-nums
diagonal-fractions
slashed-zero
```

Dashboard:

```css
.metric {
  font-variant-numeric: tabular-nums;
}
```

giúp số align đẹp.

---

# 57. `font-feature-settings` [DEEP]

Low-level OpenType controls:

```css
font-feature-settings: "liga" 1, "tnum" 1;
```

Chỉ dùng khi high-level `font-variant-*` không đủ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nối từ **font-variant-** sang **Korean line breaking**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Ưu tiên mang tính ngữ nghĩa (semantic / 의미적)/high-level thuộc tính (property / 속성).

Low-level tính năng (feature / 기능) tags:
- khó đọc,
- font-dependent,
- dễ làm portability kém.

---

# 58. biến (variable) Fonts [ADV]

các thuộc tính (properties):

```text
font-weight
font-stretch
font-style
font-variation-settings
```

Low-level custom axes:

```css
.title {
  font-variation-settings:
    "wght" 650,
    "wdth" 90;
}
```

High-level các thuộc tính (properties) nên được ưu tiên nếu axis tiêu chuẩn (standard / 표준).

---

# 59. `font-optical-sizing`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
body {
  font-optical-sizing: auto;
}
```

biến (variable) fonts có optical kích thước (size / 크기) axis có thể tự tối ưu glyph theo rendered font kích thước (size / 크기).

---

# 60. `font-size-adjust`

Giúp phương án dự phòng (fallback) font giữ perceived x-height tương đối gần.

Useful giảm visual jump khi custom font tải (load / 로드).

Concept:

```css
body {
  font-size-adjust: 0.5;
}
```

Cần calibrate theo font.

---

# 61. East Asian Typography [ADV]

các thuộc tính (properties) cần biết khi làm Korean/Japanese/Chinese UI:

```text
word-break
line-break
text-emphasis
text-combine-upright
writing-mode
text-orientation
ruby-position
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Korean line breaking** nối từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sang **Mẫu (pattern / 패턴)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Korean line breaking

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
:lang(ko) {
  word-break: keep-all;
  overflow-wrap: break-word;
}
```

Cần kiểm thử (test / 테스트) content thực tế; không áp blindly cho mọi site.

---

# 62. `text-emphasis` [ADV]

East Asian emphasis marks:

```css
.emphasis {
  text-emphasis: filled dot;
}
```

Có:
- `text-emphasis-style`
- `text-emphasis-color`
- `text-emphasis-position`

---

# 63. Ruby Annotation [ADV]

Ruby markup dùng cho pronunciation/annotation trong East Asian văn bản (text / 텍스트).

CSS:
- `ruby-position`
- ruby display mô hình (model / 모델).

Không phải daily CSS, nhưng quan trọng cho international publishing.

---

# 64. Wide-Gamut Color [ADV]

Hiện đại (modern / 현대적) displays có thể kết xuất (render / 렌더링) ngoài sRGB.

Example:

```css
color: color(display-p3 1 0.2 0.1);
```

phương án dự phòng (fallback):

```css
.button {
  background: rgb(255 70 60);
  background: color(display-p3 1 .25 .18);
}
```

Unsupported khai báo (declaration) bị bỏ; phương án dự phòng (fallback) trước vẫn còn.

---

# 65. `color-gamut` truy vấn môi trường (media query) [ADV]

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
@media (color-gamut: p3) {
  .hero {
    --brand: color(display-p3 1 .2 .3);
  }
}
```

các giá trị (values):
- `srgb`
- `p3`
- `rec2020`

Use only when extra gamut thực sự mang giá trị.

---

# 66. Color nội suy (interpolation) không gian (space / 공간) [DEEP]

Độ dốc (gradient / 기울기)/color mixing có thể trông khác tùy nội suy (interpolation) color không gian (space / 공간).

Example:

```css
background:
  linear-gradient(
    in oklab,
    blue,
    red
  );
```

Hiện đại (modern / 현대적) hệ thống thiết kế (design system) nên hiểu:
- sRGB nội suy (interpolation),
- perceptual spaces như Oklab/Oklch.

---

# 67. `contrast-color()` [2026]

Interop 2026 tập trung hàm (function / 함수) này.

Concept:

```css
.button {
  background: var(--button-bg);
  color: contrast-color(var(--button-bg));
}
```

Mục tiêu:
- chọn contrasting color cho background/foreground.

⚠ Đây là tính năng (feature / 기능) hiện đại; tương thích trình duyệt (browser compatibility) phải được check trước môi trường vận hành (production / 운영 환경).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Mẫu (pattern / 패턴)** nối từ **Korean line breaking** sang **Use trường hợp (case / 사례)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mẫu (pattern / 패턴)

phương án dự phòng (fallback):

```css
.button {
  color: white;
}

@supports (color: contrast-color(black)) {
  .button {
    color: contrast-color(var(--button-bg));
  }
}
```

---

# 68. Typed `attr()` [2026]

Classic:

```css
.badge::after {
  content: attr(data-label);
}
```

Hiện đại (modern / 현대적) typed `attr()` cho phép đọc attribute như typed CSS giá trị (value / 값).

Concept:

```css
.progress {
  width: attr(data-progress type(<percentage>), 0%);
}
```

Hoặc đơn vị (unit / 단위)/kiểu (type / 타입) cú pháp (syntax / 문법) theo mức hỗ trợ trình duyệt (browser support / 브라우저 지원).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Mẫu (pattern / 패턴)** nêu quy tắc; **Use trường hợp (case / 사례)** thử quy tắc trong tình huống, rồi **replace** mở rộng hệ quả.

## Use trường hợp (case / 사례)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
HTML data
→ CSS typed value
```

giảm JS glue trong presentation-only cases.

⚠ 2026 là focus interoperability; luôn feature-test.

---

# 69. Advanced CSS Math [ADV]

Ngoài:

```text
calc
min
max
clamp
```

CSS specs/nền tảng (platform / 플랫폼) hiện đại có thêm nhiều math các hàm (functions) tùy hỗ trợ (support / 지원):

```text
round()
mod()
rem()
abs()
sign()
sin()
cos()
tan()
asin()
acos()
atan()
atan2()
sqrt()
pow()
hypot()
log()
exp()
```

Không cần thuộc mọi hàm (function / 함수).

Master lesson:

> CSS ngày càng trở thành ràng buộc (constraint / 제약조건)/math ngôn ngữ (language / 언어), không chỉ thuộc tính (property / 속성) danh sách (list / 목록).

Check tính tương thích (compatibility / 호환성) trước khi dùng non-core math các hàm (functions).

---

# 70. `interpolate-size` [hiện đại (modern / 현대적)]

Cho phép nội suy (interpolation) tới/from kích thước nội tại (intrinsic size) keywords trong hỗ trợ (support / 지원) phù hợp.

Concept:

```css
:root {
  interpolate-size: allow-keywords;
}
```

Sau đó transitions có thể animate kích thước (size / 크기) tới:

```text
auto
min-content
max-content
fit-content
```

tùy hỗ trợ (support / 지원)/spec.

---

# 71. `calc-size()` [EXPERIMENTAL]

Cho calculation với kích thước nội tại (intrinsic size) keywords.

Concept:

```css
height: calc-size(auto, size + 2rem);
```

Nó giải quyết trường hợp (case / 사례) `calc()` thường không làm được với `auto`.

⚠ Limited availability: không dùng trọng yếu (critical / 중요) môi trường vận hành (production / 운영 환경) UI nếu targets chưa hỗ trợ (support / 지원).

---

# 72. đường chuyển động (motion path) [ADV]

các thuộc tính (properties):

```text
offset-path
offset-distance
offset-position
offset-anchor
offset-rotate
offset
```

Example:

```css
.dot {
  offset-path:
    path("M 0 0 C 100 0 100 100 200 100");
  animation: move 3s linear infinite;
}

@keyframes move {
  to {
    offset-distance: 100%;
  }
}
```

---

# 73. `shape()` hàm (function / 함수) [2026]

Hiện đại (modern / 현대적) CSS `shape()` cho basic shapes/path-like commands bằng CSS cú pháp (syntax / 문법).

Example concept:

```css
.element {
  clip-path:
    shape(
      from 0 0,
      line to 100% 0,
      line to 50% 100%,
      close
    );
}
```

Có thể dùng với:
- `clip-path`,
- `offset-path`,
- shape-related các thuộc tính (properties) trong hỗ trợ (support / 지원) tương ứng.

Ưu điểm so với SVG `path()` cú pháp (syntax / 문법):
- CSS units,
- percentages,
- CSS math.

---

# 74. Animation Composition [ADV]

Khi nhiều animations ảnh hưởng cùng thuộc tính (property / 속성):

```css
animation-composition:
  replace;
```

các giá trị (values):

```text
replace
add
accumulate
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Use trường hợp (case / 사례)** nêu quy tắc; **replace** thử quy tắc trong tình huống, rồi **add** mở rộng hệ quả.

## `replace`

Tác động (effect / 효과) mới thay underlying giá trị (value / 값).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **add** nối từ **replace** sang **accumulate**, vì cơ chế trước tạo đầu vào cho bước sau.

## `add`

Bản dựng (build / 빌드) trên underlying giá trị (value / 값).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **accumulate** nối từ **add** sang **Mẫu thiết kế (design pattern / 디자인 패턴) — Style ngữ cảnh (context / 맥락)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `accumulate`

Combine theo animation kiểu (type / 타입).

Example:

```css
.icon {
  transform: rotate(10deg);
  animation: pulse 1s infinite;
  animation-composition: add;
}
```

Useful cho composable animation các hệ thống (systems / 시스템들).

---

# 75. Multiple Animation các danh sách (lists) [DEEP]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
animation:
  fade 200ms ease,
  slide 300ms ease,
  pulse 2s linear infinite;
```

Mỗi animation-* thuộc tính (property / 속성) là comma-separated danh sách (list / 목록).

Nếu danh sách (list / 목록) lengths khác nhau, các giá trị (values) có thể cycle theo spec rules.

Cấp cao (senior / 시니어) bug nguồn (source / 소스):
- animation-name có 3 các giá trị (values),
- duration có 2 các giá trị (values),
- trình duyệt (browser / 브라우저) các map khóa–giá trị (maps)/cycles unexpectedly với dev.

---

# 76. Negative Animation Delay [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
animation-delay: -500ms;
```

Animation bắt đầu như thể đã chạy 500ms.

Useful:
- stagger simulations,
- synchronized loaders,
- initial progress.

---

# 77. `steps()` Deep Dive

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
animation-timing-function:
  steps(5, end);
```

Useful:
- sprite animation,
- frame-by-frame UI.

Variations include jump hành vi (behavior / 동작).

Không dùng `steps()` nếu bạn thực sự cần smooth nội suy (interpolation).

---

# 78. Named Scroll Timelines [ADV]

Thay vì anonymous:

```css
animation-timeline: scroll();
```

có thể define timeline conceptually:

```css
.scroller {
  scroll-timeline-name: --page-scroll;
  scroll-timeline-axis: block;
}

.progress {
  animation-timeline: --page-scroll;
}
```

Similarly view timelines:
- `view-timeline-name`
- `view-timeline-axis`
- `view-timeline-inset`

Check chính xác (exact / 정확한) hỗ trợ (support / 지원)/hiện tại (current / 현재) cú pháp (syntax / 문법).

---

# 79. `animation-range` [hiện đại (modern / 현대적)]

Cho scroll/view timeline biết animation active trong đoạn nào.

```css
.card {
  animation-timeline: view();
  animation-range:
    entry 0%
    cover 40%;
}
```

Cấp cao (senior / 시니어) use:
- reveal animation,
- parallax,
- reading progress.

Khả năng tiếp cận (accessibility / 접근성):
- respect giảm chuyển động (reduced motion).

---

# 80. Cross-document chuyển cảnh giao diện (view transitions) [2026]

chuyển cảnh giao diện (view transitions) không chỉ SPA trạng thái (state / 상태).

Hiện đại (modern / 현대적) nền tảng (platform / 플랫폼) hướng tới cross-document transitions giữa pages cùng origin/eligible điều hướng (navigation / 내비게이션).

CSS concepts:
- `view-transition-name`
- chuyển tiếp (transition / 전이) các phần tử giả (pseudo-elements)
- `@view-transition`
- chuyển tiếp (transition / 전이) types/trạng thái (state / 상태) các bộ chọn (selectors) theo hỗ trợ (support / 지원).

⚠ 2026 vẫn là focus interoperability.

---

# 81. chuyển cảnh giao diện (view transition) phần tử giả (pseudo-element) cây (tree / 트리) [DEEP]

Conceptual cây (tree / 트리):

```text
::view-transition
└─ ::view-transition-group(name)
   └─ ::view-transition-image-pair(name)
      ├─ ::view-transition-old(name)
      └─ ::view-transition-new(name)
```

Hiểu cây (tree / 트리) này giúp:
- animate old/new snapshots khác nhau,
- điều khiển (control / 제어) dùng chung (shared / 공유) element chuyển tiếp (transition / 전이).

---

# 82. định vị theo điểm neo (anchor positioning) — Deeper mô hình (model / 모델) [ADV]

Chuẩn gốc (canonical / 정본) ghi chú (note / 노트) giới thiệu định vị theo điểm neo (anchor positioning).

Master cần biết ecosystem:

```text
anchor-name
position-anchor
anchor()
anchor-size()
position-area
position-try-fallbacks
position-try-order
@position-try
```

Concept:
- tham chiếu (reference / 참조) anchor,
- preferred placement,
- phương án dự phòng (fallback) placement khi collision.

Use trường hợp (case / 사례):
- tooltip,
- dropdown,
- ngữ cảnh (context / 맥락) menu.

---

# 83. Position phương án dự phòng (fallback) mẫu (pattern / 패턴) [hiện đại (modern / 현대적)]

Mental mẫu (pattern / 패턴):

```text
prefer bottom
→ nếu không đủ space: top
→ nếu vẫn không đủ: side
```

định vị theo điểm neo (anchor positioning) hướng tới declarative collision phương án dự phòng (fallback) thay vì JS đo vùng nhìn (viewport) + set coordinates.

---

# 84. bộ chứa (container / 컨테이너) Style Queries — Deeper [2026]

Kích thước (size / 크기) truy vấn (query / 쿼리):

```css
@container (width > 30rem) {}
```

Style truy vấn (query / 쿼리):

```css
@container style(--density: compact) {}
```

Mẫu (pattern / 패턴):

```css
.panel {
  --density: compact;
}

@container style(--density: compact) {
  .row {
    padding-block: .25rem;
  }
}
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Mẫu thiết kế (design pattern / 디자인 패턴) — Style ngữ cảnh (context / 맥락)** nối từ **accumulate** sang **Pitfall**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mẫu thiết kế (design pattern / 디자인 패턴) — Style ngữ cảnh (context / 맥락)

Thành phần (component / 컴포넌트) hành vi (behavior / 동작) có thể phụ thuộc mang tính ngữ nghĩa (semantic / 의미적) style trạng thái (state / 상태) của ancestor, không chỉ width.

---

# 85. `@supports selector()` [ADV]

Chuẩn gốc (canonical / 정본) ghi chú (note / 노트) có `@supports`; ở mức master cần hiểu hàm (function / 함수) truy vấn (query / 쿼리).

```css
@supports selector(:has(*)) {
  .card:has(img) {
    ...
  }
}
```

Dùng để detect bộ chọn (selector) cú pháp (syntax / 문법).

---

# 86. `@supports font-tech()` / `font-format()` [ADV]

Concept:

```css
@supports font-tech(color-COLRv1) {
  ...
}
```

Useful khi:
- color fonts,
- advanced font tech,
- biến (variable) font scenarios.

Không cần daily CSS nhưng có giá trị cho thiết kế (design / 설계)/publishing products.

---

# 87. CSSOM [MUST for frontend cấp cao (senior / 시니어)]

CSS không chỉ là biểu định kiểu (stylesheet / 스타일시트) văn bản (text / 텍스트).

JavaScript có **CSS mô hình đối tượng (object model / 객체 모델)**.

Dùng chung (common / 공통) APIs:

```text
document.styleSheets
CSSStyleSheet
CSSRule
CSSStyleRule
CSSMediaRule
CSSSupportsRule
getComputedStyle()
CSS.supports()
```

---

# 88. `getComputedStyle()` [MUST]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```js
const styles =
  getComputedStyle(element);

console.log(styles.width);
console.log(styles.color);
```

Nó expose resolved computed style biểu diễn (representation / 표현).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Pitfall** nối từ **Mẫu thiết kế (design pattern / 디자인 패턴) — Style ngữ cảnh (context / 맥락)** sang **Limitation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Pitfall

Đừng dùng liên tục trong tight vòng lặp (loop / 루프) sau DOM writes.

Có thể force style/bố cục (layout / 레이아웃) synchronization tùy thuộc tính (property / 속성)/ngữ cảnh (context / 맥락).

Mẫu (pattern / 패턴):

```text
batch reads
→ batch writes
```

---

# 89. `CSS.supports()` [ADV]

JS equivalent của truy vấn hỗ trợ tính năng (feature query):

```js
CSS.supports("display", "grid");
```

bộ chọn (selector):

```js
CSS.supports("selector(:has(*))");
```

Useful khi JS hành vi (behavior / 동작) cũng phụ thuộc nền tảng (platform / 플랫폼) năng lực (capability / 역량).

---

# 90. biểu định kiểu (stylesheet / 스타일시트) Manipulation

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```js
const sheet =
  document.styleSheets[0];
```

Rules:

```js
sheet.cssRules;
```

Có:
- `insertRule()`
- `deleteRule()`

Use carefully:
- cross-origin biểu định kiểu (stylesheet / 스타일시트) truy cập (access / 접근) restrictions,
- maintainability.

---

# 91. các biểu định kiểu (stylesheet / 스타일시트) có thể khởi tạo (constructable stylesheets) [ADV]

Concept:

```js
const sheet =
  new CSSStyleSheet();

sheet.replaceSync(`
  :host {
    display: block;
  }
`);

shadowRoot.adoptedStyleSheets = [sheet];
```

Useful:
- Web Components,
- share one biểu định kiểu (stylesheet / 스타일시트) đối tượng (object / 객체) giữa nhiều shadow roots.

Mẫu (pattern / 패턴):

```text
Create once
→ adopt many
```

---

# 92. CSS Typed OM (mô hình đối tượng CSS có kiểu) [ADV]

Traditional:

```js
element.style.width = "10px";
```

Typed OM (mô hình đối tượng CSS có kiểu):

```js
element.attributeStyleMap.set(
  "width",
  CSS.px(10)
);
```

Computed:

```js
element.computedStyleMap();
```

Mục tiêu:
- CSS các giá trị (values) như typed JS objects,
- ít string parsing,
- clearer numerical manipulation.

---

# 93. Typed OM (mô hình đối tượng CSS có kiểu) Example

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```js
const map =
  element.computedStyleMap();

const width =
  map.get("width");

console.log(width.value);
console.log(width.unit);
```

Useful cho:
- editor tools,
- animation các hệ thống (systems / 시스템들),
- bố cục (layout / 레이아웃) tooling,
- browser-heavy UI frameworks.

Không phải yêu cầu (requirement / 요구사항) cho mọi frontend app.

---

# 94. Shadow DOM (cây DOM đóng gói) Styling [MUST for Web Components]

Shadow DOM (cây DOM đóng gói) tạo ranh giới style (style boundary).

Inside thành phần (component / 컴포넌트):

```css
:host {
  display: block;
}
```

Host trạng thái (state / 상태):

```css
:host([disabled]) {
  opacity: .5;
}
```

---

# 95. `::slotted()` [ADV]

Style phân tán (distributed / 분산) light-DOM children qua `<slot>`.

```css
::slotted(img) {
  border-radius: 50%;
}
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Pitfall** đặt tiêu chí; **Limitation** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Mẫu thiết kế (design pattern / 디자인 패턴) — tường minh (explicit / 명시적) Styling Surface** mở rộng hệ quả.

## Limitation

`::slotted()` mục tiêu (target / 대상) slotted element, không arbitrary deep descendants.

Đừng expect:

```css
::slotted(div span)
```

hoạt động như normal descendant bộ chọn (selector).

---

# 96. `::part()` [MUST]

Thành phần (component / 컴포넌트) expose nội bộ (internal / 내부) part:

```html
<button part="control">
```

Bên tiêu thụ (consumer / 소비자):

```css
my-button::part(control) {
  border-radius: 999px;
}
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Limitation** đặt tiêu chí; **Mẫu thiết kế (design pattern / 디자인 패턴) — tường minh (explicit / 명시적) Styling Surface** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Inline SVG** mở rộng hệ quả.

## Mẫu thiết kế (design pattern / 디자인 패턴) — tường minh (explicit / 명시적) Styling Surface

Web thành phần (component / 컴포넌트) không expose toàn nội bộ (internal / 내부) DOM.

Nó expose:
- CSS custom các thuộc tính (properties),
- `::part()` hooks.

Đây là thành phần (component / 컴포넌트) CSS API.

---

# 97. Custom các thuộc tính (properties) qua Shadow ranh giới (boundary / 경계)

CSS custom các thuộc tính (properties) inherit qua shadow ranh giới (boundary / 경계) theo normal kế thừa (inheritance) mô hình (model / 모델) phù hợp.

Host bên tiêu thụ (consumer / 소비자):

```css
my-button {
  --button-bg: rebeccapurple;
}
```

Inside shadow:

```css
button {
  background: var(--button-bg);
}
```

Mẫu (pattern / 패턴):

```text
Custom property = theming API
::part = structural styling API
```

---

# 98. SVG + CSS [MUST]

Inline SVG có thể style bằng CSS:

```css
.icon {
  fill: currentColor;
  stroke: none;
}
```

SVG các thuộc tính (properties):
- `fill`
- `stroke`
- `stroke-width`
- `stroke-linecap`
- `stroke-linejoin`

---

# 99. SVG `currentColor` mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```svg
<svg class="icon" ...>
  ...
</svg>
```

```css
.icon {
  color: var(--icon-color);
  fill: currentColor;
}
```

Icon follow văn bản (text / 텍스트) color/theme automatically.

---

# 100. Inline SVG vs `<img src="icon.svg">`

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Inline SVG** nối từ **Mẫu thiết kế (design pattern / 디자인 패턴) — tường minh (explicit / 명시적) Styling Surface** sang **SVG qua <img>**, vì cơ chế trước tạo đầu vào cho bước sau.

## Inline SVG

CSS có thể mục tiêu (target / 대상) nội bộ SVG.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **SVG qua <img>** nối từ **Inline SVG** sang **Cấp cao (senior / 시니어) choice**, vì cơ chế trước tạo đầu vào cho bước sau.

## SVG qua `<img>`

Document CSS không style nội bộ (internal / 내부) SVG DOM như inline cây (tree / 트리).

Đây là replaced-resource ranh giới (boundary / 경계).

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) choice** nối từ **SVG qua <img>** sang **clip-path**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) choice

Inline SVG khi:
- động (dynamic / 동적) fill/stroke,
- animation,
- accessible interactive graphic.

Ảnh (image / 이미지) SVG khi:
- static asset,
- bộ nhớ đệm (cache / 캐시)/tài nguyên (resource / 자원) simplicity.

---

# 101. SVG `viewBox` và CSS kích thước (size / 크기)

SVG nội bộ (internal / 내부) coordinate hệ thống (system / 시스템):

```html
<svg viewBox="0 0 24 24">
```

CSS:

```css
.icon {
  width: 1em;
  height: 1em;
}
```

Mẫu (pattern / 패턴) icon:

```css
.icon {
  inline-size: 1em;
  block-size: 1em;
  flex: none;
}
```

---

# 102. Mask-based Icon mẫu (pattern / 패턴) [ADV]

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.icon {
  width: 1em;
  height: 1em;
  background: currentColor;
  mask:
    url("/icons/search.svg")
    center / contain
    no-repeat;
}
```

Useful:
- monochrome icon hệ thống (system / 시스템),
- color via `currentColor`.

---

# 103. Advanced Masks [ADV]

các thuộc tính (properties):

```text
mask-image
mask-mode
mask-repeat
mask-position
mask-size
mask-origin
mask-clip
mask-composite
mask
```

Mask khác clip:
- clip = binary-ish visible region.
- mask = có alpha/luminance gradients.

---

# 104. `clip-path` vs `mask`

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) choice** đặt đầu vào cho **clip-path**, rồi **mask** mở rộng hệ quả hoặc giới hạn liên quan.

## `clip-path`

Good:
- hard geometric ranh giới (boundary / 경계).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **clip-path** đặt đầu vào cho **mask**, rồi **Dùng chung (common / 공통) print adjustments** mở rộng hệ quả hoặc giới hạn liên quan.

## `mask`

Good:
- feathered transparency,
- độ dốc (gradient / 기울기) reveal,
- alpha ảnh (image / 이미지) shapes.

---

# 105. Print CSS [MUST for master]

CSS không chỉ screen.

```css
@media print {
  nav,
  button {
    display: none;
  }
}
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Dùng chung (common / 공통) print adjustments** nối từ **mask** sang **auto**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) print adjustments

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@media print {
  body {
    color: black;
    background: white;
  }

  a[href]::after {
    content: " (" attr(href) ")";
  }
}
```

Đừng append URL cho nội bộ (internal / 내부) điều hướng (navigation / 내비게이션)/buttons blindly.

---

# 106. `@page` [ADV]

Concept:

```css
@page {
  size: A4;
  margin: 20mm;
}
```

Paged media điều khiển (control / 제어) khác nhau theo trình duyệt (browser / 브라우저)/print engine.

Use trường hợp (case / 사례):
- reports,
- invoices,
- printable documents.

---

# 107. `print-color-adjust` [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.report-chart {
  print-color-adjust: exact;
}
```

Nói trình duyệt (browser / 브라우저) cố gắng giữ colors.

⚠ người dùng (user / 사용자)/trình duyệt (browser / 브라우저) vẫn có quyền print preferences; không assume tuyệt đối.

---

# 108. Multi-column Advanced [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.article {
  column-width: 18rem;
  column-gap: 2rem;
}
```

Fragmentation controls:

```css
h2 {
  break-after: avoid;
}

figure {
  break-inside: avoid;
}
```

---

# 109. CSS Counters [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.chapter {
  counter-reset: section;
}

.chapter h2 {
  counter-increment: section;
}

.chapter h2::before {
  content:
    counter(section)
    ". ";
}
```

Useful:
- legal docs,
- documentation,
- generated numbering.

---

# 110. Nested Counters

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
ol {
  counter-reset: item;
}

li {
  counter-increment: item;
}

li::marker {
  content:
    counters(item, ".")
    ". ";
}
```

Can generate:

```text
1.
1.1
1.1.1
```

---

# 111. `@counter-style` [ADV]

Custom marker hệ thống (system / 시스템):

```css
@counter-style thumbs {
  system: cyclic;
  symbols: "👍" "🔥" "⭐";
  suffix: " ";
}
```

Use:

```css
ul {
  list-style: thumbs;
}
```

Niche nhưng useful cho publishing/thiết kế (design / 설계) các hệ thống (systems / 시스템들).

---

# 112. Tables — Deep bố cục (layout / 레이아웃) [ADV]

`table-layout`:

```css
table {
  table-layout: fixed;
}
```

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **auto** nối từ **Dùng chung (common / 공통) print adjustments** sang **fixed**, vì cơ chế trước tạo đầu vào cho bước sau.

## `auto`

Column width influenced bởi content.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **fixed** nối từ **auto** sang **Cấp cao (senior / 시니어) lesson**, vì cơ chế trước tạo đầu vào cho bước sau.

## `fixed`

Column sizing dựa nhiều hơn vào tường minh (explicit / 명시적) bảng (table / 테이블)/column widths và first-row info; bố cục (layout / 레이아웃) predictable hơn.

Useful:
- large dữ liệu (data / 데이터) bảng (table / 테이블),
- fixed dashboard columns.

---

# 113. Border Collapsing mô hình (model / 모델) [DEEP]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
table {
  border-collapse: collapse;
}
```

Adjacent cell borders compete theo border giải quyết xung đột (conflict resolution / 충돌 해결) rules.

Đây là lý do:
- border của th/td có lúc không giống simple box stacking.

Nếu muốn fully predictable spacing:

```css
border-collapse: separate;
border-spacing: .5rem;
```

---

# 114. Advanced Grid — đường cơ sở (baseline) / Masonry Awareness

Grid có đường cơ sở (baseline) alignment và advanced định cỡ dải lưới (track sizing) rất sâu.

Master không cần memorize toàn spec thuật toán (algorithm / 알고리즘), nhưng phải biết:

```text
track sizing
intrinsic contributions
spanning items
min/max track sizing
automatic minimums
baseline alignment
```

Khi grid width bất ngờ:
- check `min-content`,
- `minmax(0,1fr)`,
- spanning item contributions.

---

# 115. Subpixel bố cục (layout / 레이아웃) / điểm ảnh (pixel / 픽셀) Rounding [DEEP]

CSS pixels có thể thành fractional các giá trị (values):

```text
33.333333px
```

Trình duyệt (browser / 브라우저) cuối cùng map khóa–giá trị (map) tới thiết bị (device / 장치) pixels.

3-column grid:

```css
grid-template-columns:
  repeat(3, 1fr);
```

Bộ chứa (container / 컨테이너) width không chia hết → nhánh học (track / 트랙) kết xuất (render / 렌더링) có thể rounding.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Cấp cao (senior / 시니어) lesson** nối từ **fixed** sang **zoom vs transform**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cấp cao (senior / 시니어) lesson

Đừng assume:

```text
layout luôn integer px
```

Tránh JS comparison strict với rounded dimensions nếu không cần.

---

# 116. thiết bị (device / 장치) điểm ảnh (pixel / 픽셀) Ratio mô hình tư duy (mental model / 사고 모델)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
CSS pixel
≠
physical device pixel
```

High-DPI:

```text
1 CSS px có thể map tới nhiều physical pixels
```

Điều này ảnh hưởng:
- hairline rendering,
- canvas,
- screenshots,
- hồi quy giao diện (visual regression) tolerance.

---

# 117. CSS `zoom` [2026]

`zoom` quy mô (scale / 규모) element và ảnh hưởng bố cục (layout / 레이아웃) khác `transform: scale()`.

Concept:

```css
.preview {
  zoom: 0.8;
}
```

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **zoom vs transform** nối từ **Cấp cao (senior / 시니어) lesson** sang **cải tiến lũy tiến (progressive enhancement)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `zoom` vs transform

`transform: scale()`:
- transforms painted kết quả (result / 결과),
- normal bố cục (layout / 레이아웃) không gian (space / 공간) thường không co tương ứng.

`zoom`:
- ảnh hưởng bố cục (layout / 레이아웃) sizing.

Interop 2026 tiếp tục cải thiện đa trình duyệt (cross-browser) hành vi (behavior / 동작).

⚠ Chỉ dùng khi hiểu khả năng tiếp cận (accessibility / 접근성)/bố cục (layout / 레이아웃) consequences.

---

# 118. `forced-color-adjust` [ADV]

High-contrast / màu cưỡng bức (forced colors) chế độ (mode / 모드):

```css
.logo {
  forced-color-adjust: none;
}
```

`none` nói trình duyệt (browser / 브라우저) không override colors.

⚠ Dùng rất ít.

Chỉ opt-out khi automatic màu cưỡng bức (forced colors) thực sự phá meaning, ví dụ:
- brand ảnh (image / 이미지),
- color-coded graphic có alternate accessible cue.

---

# 119. màu cưỡng bức (forced colors) mẫu thiết kế (design pattern / 디자인 패턴)

Default:
- để trình duyệt (browser / 브라우저) adapt.

Sau đó targeted fixes:

```css
@media (forced-colors: active) {
  .control {
    border: 1px solid CanvasText;
  }
}
```

Hệ thống (system / 시스템) colors:
- `Canvas`
- `CanvasText`
- `ButtonFace`
- `ButtonText`
- `Highlight`
- `HighlightText`

---

# 120. tương thích trình duyệt (browser compatibility) chiến lược (strategy / 전략) [MUST]

Master CSS không hỏi:

> "tính năng (feature / 기능) này hỗ trợ (support / 지원) không?"

mà hỏi:

```text
Target browsers nào?
Feature là critical hay enhancement?
Fallback tự nhiên có acceptable không?
Có thể feature-detect không?
Baseline status?
Interop risk?
```

---

# 121. cải tiến lũy tiến (progressive enhancement) ma trận (matrix / 행렬)

Ví dụ glass tác động (effect / 효과):

```css
.card {
  background: rgb(255 255 255 / .95);
}

@supports (backdrop-filter: blur(1rem)) {
  .card {
    background: rgb(255 255 255 / .7);
    backdrop-filter: blur(1rem);
  }
}
```

Nếu tính năng (feature / 기능) thất bại (fail / 실패):
- UI vẫn usable.

Đó là cải tiến lũy tiến (progressive enhancement) đúng.

---

# 122. suy giảm có kiểm soát (graceful degradation) vs cải tiến lũy tiến (progressive enhancement)

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **cải tiến lũy tiến (progressive enhancement)** nối từ **zoom vs transform** sang **suy giảm có kiểm soát (graceful degradation)**, vì cơ chế trước tạo đầu vào cho bước sau.

## cải tiến lũy tiến (progressive enhancement)

Start simple:
```text
usable base
→ add advanced behavior
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **suy giảm có kiểm soát (graceful degradation)** nối từ **cải tiến lũy tiến (progressive enhancement)** sang **Mức (level / 수준) 1 — Static checks**, vì cơ chế trước tạo đầu vào cho bước sau.

## suy giảm có kiểm soát (graceful degradation)

Start advanced:
```text
advanced app
→ ensure acceptable fallback
```

CSS hiện đại (modern / 현대적) thường rất phù hợp cải tiến lũy tiến (progressive enhancement) vì unsupported khai báo (declaration)/quy tắc (rule / 규칙) có thể bị ignore.

---

# 123. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) Tiers

Có thể định nghĩa trong dự án (project / 프로젝트):

```text
Tier A
latest evergreen browsers

Tier B
older supported enterprise browsers

Tier C
unsupported but readable fallback
```

Sau đó tính năng (feature / 기능) chính sách (policy / 정책) rõ:

```text
Anchor positioning:
Tier A enhancement

Dialog:
required

View transition:
optional
```

---

# 124. đường cơ sở (baseline) chiến lược (strategy / 전략) [2026]

Khi research hiện đại (modern / 현대적) CSS:
- xem MDN đường cơ sở (baseline) status,
- xem Nền tảng Web (web platform / 웹 플랫폼) Status,
- xem dự án (project / 프로젝트) trình duyệt (browser / 브라우저) ma trận (matrix / 행렬).

Không sử dụng tính năng (feature / 기능) chỉ vì:
```text
Chrome của dev chạy được
```

---

# 125. CSS Testing Pyramid [MUST]

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Mức (level / 수준) 1 — Static checks** nối từ **suy giảm có kiểm soát (graceful degradation)** sang **Mức (level / 수준) 2 — thành phần (component / 컴포넌트) tests**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 1 — Static checks

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- stylelint,
- cú pháp (syntax / 문법),
- naming,
- banned patterns.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Mức (level / 수준) 2 — thành phần (component / 컴포넌트) tests** nối từ **Mức (level / 수준) 1 — Static checks** sang **Mức (level / 수준) 3 — hồi quy giao diện (visual regression)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 2 — thành phần (component / 컴포넌트) tests

Check các trạng thái (states):
- default,
- hover,
- focus,
- disabled,
- loading,
- long văn bản (text / 텍스트),
- RTL.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Mức (level / 수준) 3 — hồi quy giao diện (visual regression)** nối từ **Mức (level / 수준) 2 — thành phần (component / 컴포넌트) tests** sang **Mức (level / 수준) 4 — đa trình duyệt (cross-browser) / thiết bị (device / 장치)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 3 — hồi quy giao diện (visual regression)

Screenshot compare.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Mức (level / 수준) 4 — đa trình duyệt (cross-browser) / thiết bị (device / 장치)** nối từ **Mức (level / 수준) 3 — hồi quy giao diện (visual regression)** sang **Mức (level / 수준) 5 — khả năng tiếp cận (accessibility / 접근성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 4 — đa trình duyệt (cross-browser) / thiết bị (device / 장치)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- Chromium,
- Firefox,
- Safari,
- mobile.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Mức (level / 수준) 5 — khả năng tiếp cận (accessibility / 접근성)** nối từ **Mức (level / 수준) 4 — đa trình duyệt (cross-browser) / thiết bị (device / 장치)** sang **Công khai (public / 공개)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 5 — khả năng tiếp cận (accessibility / 접근성)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- keyboard,
- zoom,
- màu cưỡng bức (forced colors),
- giảm chuyển động (reduced motion).

---

# 126. hồi quy giao diện (visual regression) Testing [MUST]

CSS bugs thường không throw exception.

hồi quy giao diện (visual regression) catches:
- 2px shifts,
- wrapping,
- missing border,
- color đơn vị từ (token / 토큰) regression,
- responsive break.

Typical tools/ecosystems:
- Playwright screenshots,
- Storybook visual workflows,
- hosted diff services.

Mẫu (pattern / 패턴):

```text
component states
× viewport widths
× themes
```

---

# 127. CSS kiểm thử (test / 테스트) Fixture thiết kế (design / 설계)

Một thành phần (component / 컴포넌트) kiểm thử (test / 테스트) page nên có:

```text
short text
long text
very long unbreakable string
0 items
1 item
many items
large image
missing image
loading
error
RTL
200% zoom-like constraints
```

Cấp cao (senior / 시니어) không chỉ kiểm thử (test / 테스트) happy đường dẫn (path / 경로).

---

# 128. Stylelint chiến lược (strategy / 전략) [MUST]

Useful quy tắc (rule / 규칙) categories:

```text
invalid syntax
duplicate properties
unknown properties
selector complexity
specificity limits
!important restrictions
naming convention
property ordering
browser compatibility plugin if needed
```

Đừng bật 100 rules chỉ để CI đỏ.

Rules phải enforce kiến trúc (architecture / 아키텍처).

---

# 129. độ đặc hiệu (specificity) ngân sách (budget / 예산) [ADV]

Có thể enforce guideline:

```text
No IDs in component CSS
Max 2 classes per selector
Max nesting depth 2–3
No !important except designated layer
```

Không cần exactly như trên.

Quan trọng là **nhóm (team / 팀) đặc tả hợp đồng (contract / 계약) measurable**.

---

# 130. Dead CSS / Unused CSS [MUST]

Sources:
- old components,
- động (dynamic / 동적) lớp (class / 클래스) generation,
- abandoned experiments,
- third-party styles.

Strategies:
- component-scoped CSS,
- CSS Modules,
- bản dựng (build / 빌드) phân tích (analysis / 분석),
- coverage,
- tiện ích (utility) cây (tree / 트리) shaking,
- delete styles with mã (code / 코드).

⚠ Automatic unused CSS tools có thể miss động (dynamic / 동적) thời gian chạy (runtime / 런타임) các bộ chọn (selectors).

---

# 131. CSS Coverage in DevTools [ADV]

Trình duyệt (browser / 브라우저) DevTools Coverage có thể cho thấy biểu định kiểu (stylesheet / 스타일시트) bytes unused trong scenario đang chạy.

Không đồng nghĩa:
```text
unused = safe delete
```

Vì trạng thái (state / 상태)/page khác có thể dùng.

Use as investigation tín hiệu (signal / 신호).

---

# 132. trọng yếu (critical / 중요) CSS [ADV]

Above-the-fold CSS có thể inline/extract để giảm kết xuất (render / 렌더링) blocking.

Nhưng hiện đại (modern / 현대적) apps cần balance:
- caching,
- độ phức tạp (complexity / 복잡도),
- hydration,
- duplicate CSS.

Không automatically inline toàn CSS.

---

# 133. tính lại style (style recalculation) chi phí (cost / 비용) [DEEP]

Trình duyệt (browser / 브라우저) có thể cần recompute styles khi:
- lớp (class / 클래스) changes,
- DOM changes,
- trạng thái (state / 상태) changes,
- inherited custom thuộc tính (property / 속성) changes.

High-level concern:
- huge DOM,
- broad invalidations,
- frequent mutations.

Đừng micro-optimize `.class` vs `div.class` trước khi profile.

---

# 134. dao động bố cục do đọc/ghi xen kẽ (layout thrashing) [MUST]

Mẫu (pattern / 패턴) xấu JS:

```js
element.style.width = "100px";
const width = element.offsetWidth;

element.style.width = "200px";
const width2 = element.offsetWidth;
```

Read-after-write có thể force synchronous bố cục (layout / 레이아웃).

Better:

```text
batch reads
→ compute
→ batch writes
```

CSS hiệu năng (performance / 성능) không thể tách rời JS bố cục (layout / 레이아웃) hành vi (behavior / 동작).

---

# 135. Containment chiến lược (strategy / 전략) [ADV]

`contain` là hiệu năng (performance / 성능) + kiến trúc (architecture / 아키텍처) công cụ (tool / 도구).

Possible:
- `layout`
- `paint`
- `size`
- `inline-size`
- `style`

Dùng khi thành phần (component / 컴포넌트):
- tương đối independent,
- có known sizing chiến lược (strategy / 전략).

⚠ `size` containment có thể làm định cỡ nội tại (intrinsic sizing / 내재 크기 결정) biến mất.

---

# 136. `content-visibility` Deep Usage [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.section {
  content-visibility: auto;
  contain-intrinsic-size: auto 600px;
}
```

Good:
- long document,
- large off-screen sections.

Bad:
- tiny danh sách (list / 목록) items,
- content requiring immediate đo lường (measurement / 측정),
- cases khiến focus/tìm kiếm (search / 검색) UX bất ngờ nếu hiện thực (implementation / 구현)/trình duyệt (browser / 브라우저) các ràng buộc (constraints / 제약조건들).

Profile before/after.

---

# 137. chi phí vẽ (paint cost) [ADV]

Expensive visual effects có thể gồm:
- huge blur,
- backdrop-filter,
- giant box-shadow,
- large fixed backgrounds,
- complex masks,
- frequently animating filters.

Không có universal quy tắc (rule / 규칙).

DevTools hiệu năng (performance / 성능)/Paint flashing mới là nguồn chuẩn (source of truth / 정본).

---

# 138. tầng (layer / 계층) Promotion Myth

Không phải cứ:

```css
transform: translateZ(0);
```

là "tối ưu".

Unnecessary compositing:
- tốn GPU bộ nhớ (memory / 메모리),
- tạo layers dư,
- có thể blur văn bản (text / 텍스트)/produce artifacts.

`will-change` cũng tương tự:
- hint,
- không phải magic speed switch.

---

# 139. thành phần (component / 컴포넌트) CSS đặc tả hợp đồng (contract / 계약) [MASTER]

Một reusable thành phần (component / 컴포넌트) nên xác định:

```text
DOM contract
styling hooks
tokens
variants
states
slots
responsive owner
focus behavior
overflow behavior
motion policy
browser fallback
```

Ví dụ Button API:

```text
data-variant
data-size
disabled
aria-pressed
--button-bg
--button-fg
--button-radius
```

Nội bộ (internal / 내부) hiện thực (implementation / 구현) không nên bị bên tiêu thụ (consumer / 소비자) phụ thuộc.

---

# 140. công khai (public / 공개) vs Private CSS API

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Công khai (public / 공개)** nối từ **Mức (level / 수준) 5 — khả năng tiếp cận (accessibility / 접근성)** sang **Private**, vì cơ chế trước tạo đầu vào cho bước sau.

## Công khai (public / 공개)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
documented class
data variant
ARIA state
custom property
::part
```

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Private** nối từ **Công khai (public / 공개)** sang **Lab 1 — cơ chế phân tầng (cascade) origins**, vì cơ chế trước tạo đầu vào cho bước sau.

## Private

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
internal wrapper classes
DOM depth
anonymous child order
temporary utility
```

Cấp cao (senior / 시니어) rà soát (review / 검토):
> bên tiêu thụ (consumer / 소비자) có đang override private hiện thực (implementation / 구현) không?

---

# 141. Override Hooks mẫu (pattern / 패턴)

Bad:

```css
.app .third-party-widget
  > div:nth-child(2)
  > span {
  ...
}
```

Better nếu thành phần (component / 컴포넌트) controlled:

```css
.widget {
  --widget-accent: var(--brand);
}
```

Hoặc Web thành phần (component / 컴포넌트):

```css
widget-x::part(title) {}
```

---

# 142. CSS kiến trúc (architecture / 아키텍처) for Micro-frontends [ADV]

Bài toán (problem / 문제):
- nhiều teams,
- nhiều frameworks,
- toàn cục (global / 전역) CSS collision.

Strategies:
- các lớp phân tầng (cascade layers),
- không gian tên (namespace / 네임스페이스)/gốc (root / 루트) phạm vi (scope / 범위),
- CSS Modules,
- Shadow DOM (cây DOM đóng gói),
- đơn vị từ (token / 토큰) đặc tả hợp đồng (contract / 계약),
- no toàn cục (global / 전역) resets inside child app.

Example:

```css
@scope (#payments-app) {
  ...
}
```

Hoặc gốc (root / 루트) không gian tên (namespace / 네임스페이스):

```css
.payments-app .button {}
```

depending nền tảng (platform / 플랫폼)/hỗ trợ (support / 지원).

---

# 143. Third-party CSS Containment mẫu (pattern / 패턴)

Import vendor vào low-priority tầng (layer / 계층):

```css
@layer vendor, app;

@import url("vendor.css")
  layer(vendor);
```

App:

```css
@layer app {
  ...
}
```

Giảm độ đặc hiệu (specificity) fighting.

---

# 144. Legacy CSS chuyển đổi (migration) mẫu (pattern / 패턴)

Khi codebase có:

```text
IDs
!important
nested selectors
global element overrides
```

Không rewrite toàn bộ một lần.

chuyển đổi (migration):

```text
1. establish layer order
2. put legacy into layer
3. write new components low-specificity
4. expose tokens
5. gradually remove old overrides
```

---

# 145. CSS Refactor an toàn (safety / 안전)

Trước refactor:
- screenshot các trạng thái (states),
- capture major routes,
- bản ghi (record / 레코드) computed styles for sensitive components.

Sau refactor:
- visual diff,
- keyboard kiểm thử (test / 테스트),
- responsive kiểm thử (test / 테스트).

CSS refactor không có trình biên dịch (compiler / 컴파일러) bảo vệ ngữ nghĩa (semantics / 의미론).

---

# 146. hiện đại (modern / 현대적) bản địa (native / 네이티브) UI chiến lược (strategy / 전략) [MASTER]

Trước đây frontend thường recreate:
- dialog,
- dropdown,
- tooltip,
- select.

2026 nền tảng (platform / 플랫폼) có:
- `<dialog>`,
- Popover API,
- định vị theo điểm neo (anchor positioning),
- customizable select,
- `:open`,
- lớp trên cùng (top layer),
- `@starting-style`.

Cấp cao (senior / 시니어) quyết định (decision / 결정):

```text
Use platform primitive
→ style/enhance
→ custom JS only for missing behavior
```

---

# 147. hiện đại (modern / 현대적) CSS vs JavaScript ranh giới (boundary / 경계)

Use CSS khi bài toán (problem / 문제) là:

```text
layout
presentation
responsive adaptation
visual state
animation
style condition
```

Use JS khi bài toán (problem / 문제) là:

```text
business state
data
network
complex measurement unavailable declaratively
focus management logic
application workflow
```

Hiện đại (modern / 현대적) CSS đang kéo ranh giới (boundary / 경계) xa hơn với:
- `:has()`
- các truy vấn vùng chứa (container queries)
- định vị theo điểm neo (anchor positioning)
- typed `attr()`
- scroll timelines.

---

# 148. dùng chung (common / 공통) “Master-Level” gỡ lỗi (debug / 디버그) Questions

Khi bug khó, hỏi:

```text
1. Declaration đang ở origin/layer nào?
2. Computed value thực tế là gì?
3. Value có invalid ở computed-value time không?
4. Element tạo box nào?
5. Formatting context nào đang active?
6. Containing block là ai?
7. Size definite hay indefinite?
8. Intrinsic contribution là bao nhiêu?
9. Item có automatic minimum không?
10. Element là replaced element không?
11. Scroll container thật sự là ai?
12. Stacking context nào chứa nó?
13. Nó có đang ở top layer không?
14. Writing mode / direction là gì?
15. Fragmentation context có tồn tại không?
16. Browser có support syntax/value này không?
17. User preference có override expectation không?
18. Có forced colors/reduced motion không?
19. JS có đang force layout không?
20. Bug có chỉ xuất hiện do rounding/subpixel không?
```

---

# 149. Master CSS Practical Lab — 25 bài nâng cao

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Private** nêu quy tắc; **Lab 1 — cơ chế phân tầng (cascade) origins** thử quy tắc trong tình huống, rồi **Lab 2 — tầng (layer / 계층) inversion** mở rộng hệ quả.

## Lab 1 — cơ chế phân tầng (cascade) origins

Tạo cùng thuộc tính (property / 속성) từ:
- inline,
- biểu định kiểu (stylesheet / 스타일시트),
- animation,
- chuyển tiếp (transition / 전이),
- `!important`.

Quan sát DevTools winner.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, sau khi thấy quy trình trong **Lab 1 — cơ chế phân tầng (cascade) origins**, **Lab 2 — tầng (layer / 계층) inversion** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **Lab 3 — độ gần phạm vi (scope proximity)** mở rộng hệ quả hoặc giới hạn liên quan.

## Lab 2 — tầng (layer / 계층) inversion

Kiểm thử (test / 테스트) normal + important across 3 layers.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 2 — tầng (layer / 계층) inversion** nêu quy tắc; **Lab 3 — độ gần phạm vi (scope proximity)** thử quy tắc trong tình huống, rồi **Lab 4 — Computed giá trị (value / 값)** mở rộng hệ quả.

## Lab 3 — độ gần phạm vi (scope proximity)

Tạo nested scopes và equal độ đặc hiệu (specificity).

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 3 — độ gần phạm vi (scope proximity)** nêu quy tắc; **Lab 4 — Computed giá trị (value / 값)** thử quy tắc trong tình huống, rồi **Lab 5 — Replaced ảnh (image / 이미지)** mở rộng hệ quả.

## Lab 4 — Computed giá trị (value / 값)

So sánh:
- nguồn (source / 소스) khai báo (declaration),
- computed style,
- used điểm ảnh (pixel / 픽셀) kích thước (size / 크기).

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 4 — Computed giá trị (value / 값)** nêu quy tắc; **Lab 5 — Replaced ảnh (image / 이미지)** thử quy tắc trong tình huống, rồi **Lab 6 — Flex mức tối thiểu tự động (automatic minimum)** mở rộng hệ quả.

## Lab 5 — Replaced ảnh (image / 이미지)

Kiểm thử (test / 테스트):
- intrinsic ảnh (image / 이미지),
- width only,
- height only,
- aspect-ratio,
- object-fit.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 5 — Replaced ảnh (image / 이미지)** nêu quy tắc; **Lab 6 — Flex mức tối thiểu tự động (automatic minimum)** thử quy tắc trong tình huống, rồi **Lab 7 — Grid intrinsic nhánh học (track / 트랙)** mở rộng hệ quả.

## Lab 6 — Flex mức tối thiểu tự động (automatic minimum)

Long unbreakable content:
- trước `min-width:0`,
- sau `min-width:0`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 6 — Flex mức tối thiểu tự động (automatic minimum)** nêu quy tắc; **Lab 7 — Grid intrinsic nhánh học (track / 트랙)** thử quy tắc trong tình huống, rồi **Lab 8 — Inline đường cơ sở (baseline)** mở rộng hệ quả.

## Lab 7 — Grid intrinsic nhánh học (track / 트랙)

Compare:
```css
1fr
```

với:

```css
minmax(0,1fr)
```

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 7 — Grid intrinsic nhánh học (track / 트랙)** nêu quy tắc; **Lab 8 — Inline đường cơ sở (baseline)** thử quy tắc trong tình huống, rồi **Lab 9 — BFC** mở rộng hệ quả.

## Lab 8 — Inline đường cơ sở (baseline)

Align icon + văn bản (text / 텍스트):
- center,
- đường cơ sở (baseline),
- vertical-align.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 8 — Inline đường cơ sở (baseline)** nêu quy tắc; **Lab 9 — BFC** thử quy tắc trong tình huống, rồi **Lab 10 — Fragmentation** mở rộng hệ quả.

## Lab 9 — BFC

Float ảnh (image / 이미지) + văn bản (text / 텍스트):
- normal khối (block / 블록),
- `flow-root`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 9 — BFC** nêu quy tắc; **Lab 10 — Fragmentation** thử quy tắc trong tình huống, rồi **Lab 11 — lớp trên cùng (top layer)** mở rộng hệ quả.

## Lab 10 — Fragmentation

3-column article:
- `break-inside`,
- heading breaks.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 10 — Fragmentation** nêu quy tắc; **Lab 11 — lớp trên cùng (top layer)** thử quy tắc trong tình huống, rồi **Lab 12 — Popover** mở rộng hệ quả.

## Lab 11 — lớp trên cùng (top layer)

Compare:
- div modal z-index,
- bản địa (native / 네이티브) dialog.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 11 — lớp trên cùng (top layer)** nêu quy tắc; **Lab 12 — Popover** thử quy tắc trong tình huống, rồi **Lab 13 — chuyển tiếp khi xuất hiện (entry transition)** mở rộng hệ quả.

## Lab 12 — Popover

Bản dựng (build / 빌드) menu dùng Popover API + `:popover-open`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 12 — Popover** nêu quy tắc; **Lab 13 — chuyển tiếp khi xuất hiện (entry transition)** thử quy tắc trong tình huống, rồi **Lab 14 — Custom select** mở rộng hệ quả.

## Lab 13 — chuyển tiếp khi xuất hiện (entry transition)

Use:
- `@starting-style`,
- discrete chuyển tiếp (transition / 전이).

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 13 — chuyển tiếp khi xuất hiện (entry transition)** nêu quy tắc; **Lab 14 — Custom select** thử quy tắc trong tình huống, rồi **Lab 15 — truyền chuỗi cuộn (scroll chaining)** mở rộng hệ quả.

## Lab 14 — Custom select

Progressively enhance bản địa (native / 네이티브) select với `base-select`.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 14 — Custom select** nêu quy tắc; **Lab 15 — truyền chuỗi cuộn (scroll chaining)** thử quy tắc trong tình huống, rồi **Lab 16 — vùng an toàn (safe area)** mở rộng hệ quả.

## Lab 15 — truyền chuỗi cuộn (scroll chaining)

Nested scroller + `overscroll-behavior`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 15 — truyền chuỗi cuộn (scroll chaining)** nêu quy tắc; **Lab 16 — vùng an toàn (safe area)** thử quy tắc trong tình huống, rồi **Lab 17 — biến (variable) font** mở rộng hệ quả.

## Lab 16 — vùng an toàn (safe area)

Bản dựng (build / 빌드) fixed mobile bottom nav dùng `env()`.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 16 — vùng an toàn (safe area)** nêu quy tắc; **Lab 17 — biến (variable) font** thử quy tắc trong tình huống, rồi **Lab 18 — Display P3 color** mở rộng hệ quả.

## Lab 17 — biến (variable) font

Animate/thay đổi (change / 변경) tiêu chuẩn (standard / 표준) font axis.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 17 — biến (variable) font** nêu quy tắc; **Lab 18 — Display P3 color** thử quy tắc trong tình huống, rồi **Lab 19 — Custom Highlight** mở rộng hệ quả.

## Lab 18 — Display P3 color

Create phương án dự phòng (fallback) + wide-gamut enhancement.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 18 — Display P3 color** nêu quy tắc; **Lab 19 — Custom Highlight** thử quy tắc trong tình huống, rồi **Lab 20 — đường chuyển động (motion path)** mở rộng hệ quả.

## Lab 19 — Custom Highlight

Tìm kiếm (search / 검색) match without adding `<mark>` nodes.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 19 — Custom Highlight** nêu quy tắc; **Lab 20 — đường chuyển động (motion path)** thử quy tắc trong tình huống, rồi **Lab 21 — hoạt ảnh cộng dồn (additive animation)** mở rộng hệ quả.

## Lab 20 — đường chuyển động (motion path)

Animate element along `offset-path`.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 20 — đường chuyển động (motion path)** nêu quy tắc; **Lab 21 — hoạt ảnh cộng dồn (additive animation)** thử quy tắc trong tình huống, rồi **Lab 22 — Shadow DOM (cây DOM đóng gói)** mở rộng hệ quả.

## Lab 21 — hoạt ảnh cộng dồn (additive animation)

Use `animation-composition:add`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 21 — hoạt ảnh cộng dồn (additive animation)** nêu quy tắc; **Lab 22 — Shadow DOM (cây DOM đóng gói)** thử quy tắc trong tình huống, rồi **Lab 23 — CSSOM** mở rộng hệ quả.

## Lab 22 — Shadow DOM (cây DOM đóng gói)

Expose:
- custom thuộc tính (property / 속성),
- `::part`,
- slotted content.

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 22 — Shadow DOM (cây DOM đóng gói)** nêu quy tắc; **Lab 23 — CSSOM** thử quy tắc trong tình huống, rồi **Lab 24 — Print** mở rộng hệ quả.

## Lab 23 — CSSOM

Read computed các giá trị (values) + construct biểu định kiểu (stylesheet / 스타일시트).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Lab 23 — CSSOM** nêu quy tắc; **Lab 24 — Print** thử quy tắc trong tình huống, rồi **Lab 25 — hồi quy giao diện (visual regression)** mở rộng hệ quả.

## Lab 24 — Print

Create printable report:
- A4,
- page margins,
- avoid split cards.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Lab 24 — Print** nêu quy tắc; **Lab 25 — hồi quy giao diện (visual regression)** thử quy tắc trong tình huống, rồi **Mức (level / 수준) 1 — cú pháp (syntax / 문법) người dùng (user / 사용자)** mở rộng hệ quả.

## Lab 25 — hồi quy giao diện (visual regression)

Capture thành phần (component / 컴포넌트) ma trận (matrix / 행렬):
- light/dark,
- 320/768/1440,
- long văn bản (text / 텍스트),
- focus,
- RTL.

---

# 150. Master CSS Interview / Self-test Questions

Bạn nên trả lời được không nhìn tài liệu:

1. Declared, cascaded, specified, computed, used, actual giá trị (value / 값) khác gì?
2. Khi nào custom thuộc tính (property / 속성) gây invalid at computed-value thời gian (time / 시간)?
3. Origin precedence khác độ đặc hiệu (specificity) như thế nào?
4. Tại sao `!important` đảo lớp phân tầng (cascade layer) thứ tự (order / 순서)?
5. `@scope` proximity được xét khi nào?
6. DOM cây (tree / 트리) và box cây (tree / 트리) khác nhau ở đâu?
7. Anonymous box là gì?
8. BFC là gì? `flow-root` giải quyết gì?
9. ngữ cảnh định dạng nội dòng (inline formatting context) hoạt động theo hộp dòng (line box) thế nào?
10. `vertical-align` thực sự áp dụng cho gì?
11. phần tử thay thế (replaced element) là gì?
12. kích thước nội tại (intrinsic dimension)/ratio khác CSS aspect-ratio thế nào?
13. kích thước xác định (definite size) ảnh hưởng percentage height thế nào?
14. `min-content`, `max-content`, `fit-content` khác nhau thế nào?
15. Shrink-to-fit xuất hiện trong những bố cục (layout / 레이아웃) nào?
16. Vì sao `min-width:0` fix flex overflow?
17. Vì sao `%` không thể học như một đơn vị (unit / 단위) universal?
18. Float ngày nay còn use trường hợp (case / 사례) gì?
19. Fragmentation là gì?
20. `:nth-child(2n of .x)` khác `.x:nth-child(2n)`?
21. `:user-invalid` hơn `:invalid` ở UX nào?
22. `:open`, `:popover-open`, `:modal` khác nhau?
23. lớp trên cùng (top layer) khác z-index thế nào?
24. `@starting-style` giải quyết bài toán (problem / 문제) nào?
25. `appearance:base-select` là gì?
26. vùng chứa cuộn (scroll container) ảnh hưởng sticky thế nào?
27. `overflow:hidden` và `overflow:clip` khác nhau gì?
28. `overscroll-behavior` dùng khi nào?
29. `scrollbar-gutter` giải quyết bài toán (problem / 문제) gì?
30. `env(safe-area-inset-bottom)` dùng làm gì?
31. `font-variant-numeric:tabular-nums` hữu ích khi nào?
32. Wide gamut P3 khác sRGB?
33. `contrast-color()` giải quyết gì?
34. Typed `attr()` mở ra use trường hợp (case / 사례) nào?
35. `interpolate-size` và `calc-size()` là gì?
36. đường chuyển động (motion path) gồm thuộc tính (property / 속성) nào?
37. `animation-composition` các giá trị (values) là gì?
38. chuyển cảnh giao diện (view transition) phần tử giả (pseudo-element) cây (tree / 트리) hoạt động conceptually thế nào?
39. định vị theo điểm neo (anchor positioning) phương án dự phòng (fallback) giải quyết collision ra sao?
40. bộ chứa (container / 컨테이너) style truy vấn (query / 쿼리) khác kích thước (size / 크기) truy vấn (query / 쿼리)?
41. `@supports selector()` dùng khi nào?
42. CSSOM là gì?
43. Typed OM (mô hình đối tượng CSS có kiểu) khác `element.style` string API?
44. biểu định kiểu (stylesheet / 스타일시트) có thể khởi tạo (constructable stylesheet) là gì?
45. `:host`, `::slotted`, `::part` khác nhau?
46. CSS custom thuộc tính (property / 속성) qua Shadow DOM (cây DOM đóng gói) dùng như API thế nào?
47. Inline SVG khác SVG `<img>` khi styling?
48. `mask` khác `clip-path`?
49. `@page` dùng khi nào?
50. `break-inside` ảnh hưởng print/multicol ra sao?
51. CSS counter dùng cho trường hợp (case / 사례) gì?
52. `zoom` khác `transform:scale()`?
53. màu cưỡng bức (forced colors) nên xử lý thế nào?
54. cải tiến lũy tiến (progressive enhancement) khác suy giảm có kiểm soát (graceful degradation)?
55. hồi quy giao diện (visual regression) kiểm thử (test / 테스트) CSS ra sao?
56. độ đặc hiệu (specificity) ngân sách (budget / 예산) là gì?
57. Dead CSS detect sao mà không xoá nhầm động (dynamic / 동적) classes?
58. dao động bố cục do đọc/ghi xen kẽ (layout thrashing) liên quan CSS ra sao?
59. `contain:size` có tác dụng phụ (side effect) gì?
60. công khai (public / 공개) CSS API của thành phần (component / 컴포넌트) nên gồm gì?

Nếu trả lời chắc khoảng **50+/60 câu** và làm được 20+/25 labs mà không bản sao (copy / 복사) solution, nền CSS của bạn đã ở mức rất cao.

---

# 151. Mastery Rubric

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Lab 25 — hồi quy giao diện (visual regression)** nêu quy tắc; **Mức (level / 수준) 1 — cú pháp (syntax / 문법) người dùng (user / 사용자)** thử quy tắc trong tình huống, rồi **Mức (level / 수준) 2 — UI nhà phát triển (developer / 개발자)** mở rộng hệ quả.

## Mức (level / 수준) 1 — cú pháp (syntax / 문법) người dùng (user / 사용자)

Biết:
- thuộc tính (property / 속성),
- bộ chọn (selector),
- Flex/Grid.

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Mức (level / 수준) 2 — UI nhà phát triển (developer / 개발자)** nối từ **Mức (level / 수준) 1 — cú pháp (syntax / 문법) người dùng (user / 사용자)** sang **Mức (level / 수준) 3 — cấp cao (senior / 시니어) CSS**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 2 — UI nhà phát triển (developer / 개발자)

Biết:
- responsive,
- thành phần (component / 컴포넌트),
- forms,
- animation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **Mức (level / 수준) 3 — cấp cao (senior / 시니어) CSS** nối từ **Mức (level / 수준) 2 — UI nhà phát triển (developer / 개발자)** sang **Mức (level / 수준) 4 — CSS Specialist**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 3 — cấp cao (senior / 시니어) CSS

Biết:
- cơ chế phân tầng (cascade),
- định cỡ nội tại (intrinsic sizing / 내재 크기 결정),
- stacking,
- kiến trúc (architecture / 아키텍처),
- khả năng tiếp cận (accessibility / 접근성),
- hiệu năng (performance / 성능).

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **Mức (level / 수준) 4 — CSS Specialist** nối từ **Mức (level / 수준) 3 — cấp cao (senior / 시니어) CSS** sang **Mức (level / 수준) 5 — CSS Master**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 4 — CSS Specialist

Biết:
- mô hình định dạng (formatting model / 포매팅 모델),
- các hộp dòng (line boxes),
- các phần tử thay thế (replaced elements),
- lớp trên cùng (top layer),
- advanced sizing,
- trình duyệt (browser / 브라우저) APIs,
- Shadow DOM (cây DOM đóng gói).

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Mức (level / 수준) 5 — CSS Master** nối từ **Mức (level / 수준) 4 — CSS Specialist** sang **MDN**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mức (level / 수준) 5 — CSS Master

Có thể:
- đọc specification khi docs không đủ,
- explain trình duyệt (browser / 브라우저) bố cục (layout / 레이아웃) hành vi (behavior / 동작),
- thiết kế (design / 설계) CSS kiến trúc (architecture / 아키텍처) cho multi-team hệ thống (system / 시스템),
- gỡ lỗi (debug / 디버그) đa trình duyệt (cross-browser) trường hợp biên (edge case / 경계 사례),
- chọn cải tiến lũy tiến (progressive enhancement) chiến lược (strategy / 전략),
- bản dựng (build / 빌드) thành phần (component / 컴포넌트) CSS APIs,
- profile rendering,
- rà soát (review / 검토) nền tảng (platform / 플랫폼) changes mà không chạy theo trend.

---

# 152. Những thứ KHÔNG cần học thuộc để master CSS

Không cần memorize:

```text
mọi property hiếm
mọi formal grammar
mọi vendor pseudo-element
mọi browser quirk lịch sử
mọi CSS Working Draft
```

Cần biết:
- concept tồn tại,
- khi nào cần lookup,
- tài liệu chuẩn ở đâu,
- cách đọc cú pháp (syntax / 문법)/formal definition.

---

# 153. Cách đọc MDN thuộc tính (property / 속성) page như cấp cao (senior / 시니어)

Khi lookup thuộc tính (property / 속성), đừng chỉ đọc example.

Check:

```text
Initial value
Applies to
Inherited?
Percentage basis
Computed value
Animation type
Creates stacking context?
Formal syntax
Browser compatibility
Specifications
```

Ví dụ `offset-path`:
- applies to transformable elements,
- creates ngữ cảnh xếp chồng (stacking context / 쌓임 맥락),
- animation kiểu (type / 타입) theo computed kiểu (type / 타입).

Các siêu dữ liệu (metadata / 메타데이터) này giải thích nhiều edge cases.

---

# 154. Cách đọc CSS Specification

Không cần đọc spec từ đầu đến cuối.

Workflow:

```text
1. MDN để hiểu overview.
2. Reproduce bug nhỏ.
3. DevTools computed styles.
4. Search spec section đúng concept.
5. Đọc definitions / algorithm / notes.
6. Check browser bug trackers nếu behavior lệch.
```

---

# 155. Source-of-truth hierarchy

Khi tài liệu mâu thuẫn:

```text
1. Current CSS specification / WHATWG integration specs
2. Web Platform Tests / implementation reality
3. MDN
4. web.dev / browser vendor docs
5. high-quality articles
6. StackOverflow/blog posts
```

Không bản sao (copy / 복사) old CSS hacks từ article 2015 nếu không hiểu vì sao.

---

# 156. 2026 hiện đại (modern / 현대적) CSS Watchlist

Các tính năng (feature / 기능) đáng theo dõi trong 2026:

```text
Anchor positioning interoperability
Container style queries
Dialog / Popover improvements
:open
popover="hint"
Scroll-driven animations
Cross-document View Transitions
:active-view-transition-type()
Typed attr()
contrast-color()
Custom Highlight API
Media state pseudo-classes
shape()
zoom interoperability
Customizable select
Intrinsic-size interpolation
```

Không đồng nghĩa tất cả đều nên dùng ngay môi trường vận hành (production / 운영 환경).

Quy tắc (rule / 규칙):

```text
Baseline / project support
→ progressive enhancement
→ fallback
```

---

# 157. CSS + SCSS ranh giới (boundary / 경계)

Sau supplement này, SCSS không giúp bạn hiểu trình duyệt (browser / 브라우저) thêm.

SCSS giải quyết **authoring/build-time lớp trừu tượng (abstraction / 추상화)**:

```text
modules
mixins
functions
loops
maps
generation
compile-time variables
```

CSS giải quyết **thời gian chạy (runtime / 런타임) styling mô hình (model / 모델)**:

```text
cascade
inheritance
layout
browser state
custom properties
media/container queries
animation
```

Cấp cao (senior / 시니어) phải phân biệt:

```text
SCSS abstraction problem
vs
CSS runtime problem
```

Không dùng khối trộn tái sử dụng (mixin) để che việc chưa hiểu Flex/Grid/cơ chế phân tầng (cascade).

---

# 158. Final CSS kiến thức (knowledge / 지식) map khóa–giá trị (map)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
CSS MASTER
│
├─ LANGUAGE
│  ├─ syntax
│  ├─ selectors
│  ├─ cascade
│  ├─ values
│  └─ functions
│
├─ FORMATTING MODEL
│  ├─ box tree
│  ├─ BFC / IFC
│  ├─ line boxes
│  ├─ replaced elements
│  └─ fragmentation
│
├─ SIZING
│  ├─ definite / indefinite
│  ├─ intrinsic
│  ├─ min/max-content
│  ├─ fit-content
│  └─ automatic minimum
│
├─ LAYOUT
│  ├─ normal flow
│  ├─ position
│  ├─ float
│  ├─ flex
│  ├─ grid
│  ├─ table
│  └─ multicol
│
├─ RENDERING
│  ├─ paint
│  ├─ stacking
│  ├─ top layer
│  ├─ clipping
│  ├─ masks
│  └─ compositing
│
├─ RESPONSIVE
│  ├─ media
│  ├─ container
│  ├─ env()
│  ├─ writing modes
│  └─ user preferences
│
├─ MOTION
│  ├─ transition
│  ├─ keyframes
│  ├─ additive composition
│  ├─ motion paths
│  ├─ scroll timelines
│  └─ view transitions
│
├─ COMPONENT PLATFORM
│  ├─ dialog
│  ├─ popover
│  ├─ customizable controls
│  ├─ Shadow DOM
│  └─ CSS APIs
│
├─ ARCHITECTURE
│  ├─ layers
│  ├─ scope
│  ├─ tokens
│  ├─ component API
│  └─ override contract
│
└─ ENGINEERING
   ├─ accessibility
   ├─ performance
   ├─ compatibility
   ├─ linting
   ├─ testing
   └─ visual regression
```

---

# 159. Đánh giá cuối cùng

Sau khi học:

1. `CSS_Beginner_to_Senior_2026.md`
2. `CSS_Master_Supplement_2026.md`

thì phần kiến thức lý thuyết đã **gần đầy đủ cho CSS từ beginner → cấp cao (senior / 시니어) → specialist/master**.

Nhưng “master” không thể chỉ đạt bằng đọc.

Phải có vòng:

```text
Read
→ Implement
→ Break
→ Debug
→ Inspect browser
→ Compare browsers
→ Refactor
→ Review
```

Mốc thực tế:

```text
Canonical Beginner → Senior
→ đủ để làm senior production CSS

Canonical Beginner → Senior + Supplement
→ đủ knowledge map để hướng tới CSS specialist/master

Canonical Beginner → Senior + Supplement + 20–30 advanced labs + project thật
→ mastery thực tế
```

---

# 160. Tài liệu chuẩn để tiếp tục tra cứu

> **Nối mạch:** Đặt trong câu hỏi lớn của **CSS Master Supplement 2026**, **MDN** nối từ **Mức (level / 수준) 5 — CSS Master** sang **web.dev**, vì cơ chế trước tạo đầu vào cho bước sau.

## MDN

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- CSS Reference  
  https://developer.mozilla.org/en-US/docs/Web/CSS/Reference

- CSS Guides
  https://nhà phát triển (developer / 개발자).mozilla.org/en-US/docs/Web/CSS/Guides

- CSS cơ chế phân tầng (cascade)
  https://nhà phát triển (developer / 개발자).mozilla.org/en-US/docs/Web/CSS/Guides/Cascade

- CSS API tô sáng tùy chỉnh (Custom Highlight API)
  https://nhà phát triển (developer / 개발자).mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API

- CSS Typed OM (mô hình đối tượng CSS có kiểu)
  https://nhà phát triển (developer / 개발자).mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API

- Customizable Select
  https://nhà phát triển (developer / 개발자).mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select

> **Nối mạch:** Trong **CSS Master Supplement 2026**, **web.dev** nối từ **MDN** sang **Specifications / tính tương thích (compatibility / 호환성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## web.dev

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- Learn CSS  
  https://web.dev/learn/css/

- Interop 2026
  https://web.dev/blog/interop-2026/

> **Nối mạch:** Ở chặng này của **CSS Master Supplement 2026**, **Specifications / tính tương thích (compatibility / 호환성)** nối từ **web.dev** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Specifications / tính tương thích (compatibility / 호환성)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- W3C CSS  
  https://www.w3.org/Style/CSS/

- Nền tảng Web (web platform / 웹 플랫폼) Tests
  https://wpt.fyi/

- Nền tảng Web (web platform / 웹 플랫폼) Status
  https://webstatus.dev/

- Can I Use
  https://caniuse.com/

---

# Kết luận ngắn

Nếu chỉ đọc chuẩn gốc (canonical / 정본) Beginner → cấp cao (senior / 시니어):

```text
Beginner → Senior: YES
Master CSS: chưa hoàn toàn
```

Nếu học thêm tệp (file / 파일) supplement này:

```text
Language
+ Browser model
+ Advanced layout
+ Modern platform
+ CSS APIs
+ Architecture
+ Testing
+ Compatibility
```

thì **kiến thức (knowledge / 지식) coverage đã đủ rộng để gọi là roadmap master CSS**.

Phần còn lại không phải thêm thuộc tính (property / 속성) nữa.

Phần còn lại là:

```text
practice
browser bugs
cross-browser behavior
large-codebase experience
spec reading
```

> **Bàn giao:** Sau **Specifications / tính tương thích (compatibility / 호환성)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
