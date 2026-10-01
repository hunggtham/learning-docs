# Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hiện đại (modern / 현대적) Tailwind CSS v4.3 — học từ nền tảng đến kiến trúc vận hành (production architecture / 운영 아키텍처)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Quy ước thuật ngữ Việt–Anh** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Hiện đại (modern / 현대적) Tailwind CSS v4.3 — học từ nền tảng đến kiến trúc vận hành (production architecture / 운영 아키텍처)

> Đây là bản viết lại hoàn toàn của tài liệu Tailwind trước. Tài liệu được viết cho người muốn **học để hiểu**, không phải người đã biết Tailwind và chỉ cần cheat sheet.
>
> đường cơ sở (baseline) của tài liệu là **Tailwind CSS v4.3** — vẫn là bản phát hành (release / 릴리스) Tailwind CSS mới nhất được Tailwind công bố tính đến kiểm tra (audit / 감사) 2026-09-21. Khi một nội dung liên quan trực tiếp đến CSS, tài liệu sẽ giải thích CSS cần thiết ngay tại chỗ thay vì yêu cầu bạn quay về tài liệu CSS khác.
>
> Cách đọc xuyên suốt tài liệu:
>
> ```văn bản (text / 텍스트)
> Tailwind cú pháp (syntax / 문법)
> → Tailwind hiểu lớp (class / 클래스) đó như thế nào
> → CSS được sinh ra có ý nghĩa gì
> → trình duyệt (browser / 브라우저) xử lý CSS đó ra sao
> → ví dụ thực tế
> → mẫu (pattern / 패턴) / cấp cao (senior / 시니어) note
> ```
>
> Mục tiêu sau khi học xong tệp (file / 파일) này là bạn có thể đọc một thành phần (component / 컴포넌트) Tailwind môi trường vận hành (production / 운영 환경), tự thiết kế bố cục (layout / 레이아웃), responsive UI, form, trạng thái (state / 상태), dark chế độ (mode / 모드), truy vấn vùng chứa (container query), theme, custom tiện ích (utility) và biết khi nào nên dùng Tailwind, khi nào nên quay về CSS thuần.

---

> **Chuyển mạch:** Dùng thuật ngữ Việt–Anh nhất quán để đọc Tailwind v4.3; phần tiếp theo định nghĩa utility engine trước khi đi vào production architecture.

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ Tailwind được diễn đạt bằng tiếng Việt trước rồi giữ từ gốc bên cạnh khi cần đối chiếu. Ví dụ: **mô hình ưu tiên tiện ích (utility-first)**, **tiện ích (utility)**, **biến thể trạng thái (state variant)**, **giá trị tùy ý (arbitrary value)**, **điểm ngắt (breakpoint)**, **truy vấn vùng chứa (container query)**, **phát hiện nguồn (source detection)**, **biên dịch tức thời (JIT, just-in-time)** và **cấu hình ưu tiên CSS (CSS-first configuration)**. Tên lớp (class / 클래스), directive và utility literal trong mã (code / 코드) luôn được giữ nguyên.

# PHẦN I — HIỂU TAILWIND TỪ GỐC

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **1. Tailwind CSS thực sự là gì?** tiếp nhận điểm tựa từ **Quy ước thuật ngữ Việt–Anh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1A. Cách đọc Tailwind mà không cần nhớ CSS notes trước đó** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. Tailwind CSS thực sự là gì?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **1A. Cách đọc Tailwind mà không cần nhớ CSS notes trước đó** tiếp nhận điểm tựa từ **1. Tailwind CSS thực sự là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. ưu tiên tiện ích (utility-first) khác “inline style” như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1A. Cách đọc Tailwind mà không cần nhớ CSS notes trước đó

Tài liệu luôn liên hệ Tailwind với CSS nhưng không giả định bạn còn nhớ định nghĩa từ CSS thư viện (library / 라이브러리). Với mỗi tiện ích (utility), hãy hỏi bốn câu: tiện ích (utility) generate thuộc tính (property / 속성)/cơ chế (mechanism / 메커니즘) CSS nào; thuộc tính (property / 속성) đó tác động lên chính element hay quan hệ parent/children; bố cục (layout / 레이아웃) ngữ cảnh (context / 맥락) nào phải tồn tại để thuộc tính (property / 속성) có ý nghĩa; và biến thể (variant) phía trước lớp (class / 클래스) biến bộ chọn (selector) hay thêm media/bộ chứa (container / 컨테이너) điều kiện (condition / 조건) nào.

Ví dụ `items-center` không có nghĩa chung chung là “căn giữa”. Nó generate `align-items: center` và chỉ có hành vi (behavior / 동작) mong đợi khi element là Flex/Grid bộ chứa (container / 컨테이너). Trong `flex-row`, trục chéo (cross axis) thường theo chiều khối (block / 블록)/dọc; trong `flex-col`, trục đổi. Vì vậy phải hiểu bộ chứa (container / 컨테이너) thuật toán (algorithm / 알고리즘) + axis + generated CSS, không học `items-center = center`.

`absolute` tương tự: tiện ích (utility) generate `position: absolute`, đưa box ra khỏi luồng bố cục thông thường (normal flow / 일반 흐름) và position theo khối chứa tham chiếu (containing block / 컨테이닝 블록). `top-0` chỉ đặt inset sau khi khối chứa tham chiếu (containing block / 컨테이닝 블록) đã được xác định. Nếu khối chứa tham chiếu (containing block / 컨테이닝 블록) sai, thêm nhiều inset lớp (class / 클래스) không sửa nguyên nhân gốc (root cause / 근본 원인).

Responsive tiện ích (utility) cũng chỉ tạo conditional CSS. `md:grid-cols-2` đặt Grid tiện ích (utility) trong vùng nhìn (viewport) media điều kiện (condition / 조건); `@md:flex-row` dùng truy vấn vùng chứa (container query) điều kiện (condition / 조건). trình duyệt (browser / 브라우저) vẫn chạy Grid/Flexbox bình thường. `hover:*` biến tương tác (interaction / 상호작용) bộ chọn (selector); `group-hover:*` tạo ancestor relationship; `peer-invalid:*` dựa sibling relationship.

Dấu vết (trace / 추적) gỡ lỗi (debug / 디버그) chuẩn gốc (canonical / 정본) là:

```text
complete class candidate có tồn tại trong source?
→ Tailwind có generate rule không?
→ variant condition có active không?
→ rule có thắng cascade không?
→ generated CSS đang ở layout context nào?
→ sizing / overflow / containing block / stacking có đúng không?
```

Hai bước đầu thường là Tailwind/bản dựng (build / 빌드) bài toán (problem / 문제). Các bước sau là trình duyệt (browser / 브라우저) hành vi (behavior / 동작), nhưng mỗi section trong tệp (file / 파일) phải giải thích hành vi (behavior / 동작) đó tại chỗ. Đây là cách học ưu tiên tiện ích (utility-first) mà không biến lớp (class / 클래스) names thành magic.

Tailwind CSS là một khung phần mềm (framework / 프레임워크) CSS theo hướng **ưu tiên tiện ích (utility-first)**. “tiện ích (utility)” ở đây có nghĩa là một lớp (class / 클래스) thường làm một nhiệm vụ tương đối nhỏ và rõ ràng. Ví dụ, `flex` bật Flexbox, `items-center` căn các phần tử Flex (flex item) theo trục chéo (cross axis), `p-4` tạo padding, còn `rounded-xl` tạo bo góc. Thay vì đặt một lớp (class / 클래스) có tên theo thành phần (component / 컴포넌트) rồi viết toàn bộ CSS trong một tệp (file / 파일) riêng, Tailwind khuyến khích bạn ghép các tiện ích (utility) trực tiếp tại nơi bạn viết markup.

Ví dụ với CSS truyền thống, bạn có thể viết:

```css
.profile-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  border-radius: 0.75rem;
  background: white;
  box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
}
```

Sau đó HTML chỉ cần:

```html
<div class="profile-card">
  ...
</div>
```

Trong Tailwind, cùng ý tưởng đó có thể được viết:

```html
<div
  class="
    flex
    items-center
    gap-4
    rounded-xl
    bg-white
    p-6
    shadow-sm
  "
>
  ...
</div>
```

Điểm cần hiểu là Tailwind không tạo ra một cơ chế bố cục (layout / 레이아웃) mới. `flex` vẫn trở thành CSS `display: flex`; `gap-4` vẫn trở thành CSS `gap`; trình duyệt (browser / 브라우저) vẫn chạy đúng các thuật toán Flexbox, Grid, cơ chế phân tầng (cascade), sizing và painting của CSS. Tailwind chỉ thay đổi **cách bạn author CSS**.

Một mô hình tư duy (mental model / 사고 모델) rất quan trọng là:

```text
Tailwind = ngôn ngữ đặt tên utility ở tầng authoring
CSS      = ngôn ngữ thực thi ở browser
```

Nếu một bố cục (layout / 레이아웃) không hoạt động mặc dù lớp (class / 클래스) Tailwind đã được generate, nguyên nhân thường không còn là Tailwind nữa mà nằm ở CSS thật bên dưới. cấp cao (senior / 시니어) Tailwind vì vậy phải biết khi nào gỡ lỗi (debug / 디버그) khung phần mềm (framework / 프레임워크) và khi nào gỡ lỗi (debug / 디버그) trình duyệt (browser / 브라우저).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **2. ưu tiên tiện ích (utility-first) khác “inline style” như thế nào?** tiếp nhận điểm tựa từ **1A. Cách đọc Tailwind mà không cần nhớ CSS notes trước đó** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Tailwind v4.3 khác Tailwind v3 như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. ưu tiên tiện ích (utility-first) khác “inline style” như thế nào?

Nhìn bề ngoài, một element có nhiều lớp (class / 클래스) Tailwind có thể làm bạn liên tưởng đến inline style:

```html
<button class="rounded-lg bg-blue-600 px-4 py-2 text-white">
```

Nhưng tiện ích (utility) lớp (class / 클래스) không giống:

```html
<button
  style="
    border-radius: .5rem;
    background: blue;
    padding: .5rem 1rem;
    color: white;
  "
>
```

Inline style là khai báo (declaration) gắn trực tiếp trên element. Nó không có cách tự nhiên để viết `:hover`, `:focus-visible`, `@media`, `@container`, `prefers-reduced-motion` hoặc bộ chọn (selector) quan hệ như `:has()`.

Tailwind tiện ích (utility) thì có thể kết hợp biến thể (variant):

```html
<button
  class="
    rounded-lg
    bg-blue-600
    px-4
    py-2
    text-white
    hover:bg-blue-700
    focus-visible:outline-2
    md:px-6
    dark:bg-blue-500
  "
>
```

Tailwind sẽ generate CSS tương đương với các lớp giả (pseudo-class) và truy vấn môi trường (media query) cần thiết. Vì vậy ưu tiên tiện ích (utility-first) vẫn là stylesheet-based CSS, chỉ khác cách bạn gọi các quy tắc (rule / 규칙).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **3. Tailwind v4.3 khác Tailwind v3 như thế nào?** tiếp nhận điểm tựa từ **2. ưu tiên tiện ích (utility-first) khác “inline style” như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Cài Tailwind và hiểu quy trình bản dựng (build / 빌드) (build pipeline)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Tailwind v4.3 khác Tailwind v3 như thế nào?

Nếu bạn tìm tutorial cũ, bạn sẽ thấy Tailwind v3 thường cấu hình bằng `tailwind.config.js`:

```js
export default {
  content: ["./src/**/*.{html,js,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: "#2563eb",
      },
    },
  },
};
```

Tailwind v4 chuyển mạnh sang **cấu hình ưu tiên CSS (CSS-first configuration)**. Một dự án (project / 프로젝트) mới thường bắt đầu bằng:

```css
@import "tailwindcss";
```

Sau đó đơn vị từ (token / 토큰) thiết kế (design token) có thể được khai báo trực tiếp bằng `@theme`:

```css
@theme {
  --color-brand: #2563eb;
}
```

Khi đơn vị từ (token / 토큰) `--color-brand` thuộc không gian tên (namespace / 네임스페이스) `--color-*`, Tailwind hiểu đây là color đơn vị từ (token / 토큰) và từ đó có thể tạo các tiện ích (utility) như:

```text
bg-brand
text-brand
border-brand
fill-brand
stroke-brand
```

V4 cũng có automatic phát hiện nguồn (source detection), nghĩa là phần lớn dự án (project / 프로젝트) không còn cần liệt kê `content` glob như v3. Khi cần nguồn (source / 소스) đặc biệt, bạn dùng `@source`.

Custom tiện ích (utility) và custom biến thể (variant) cũng chuyển sang ưu tiên CSS (CSS-first):

```css
@utility content-auto {
  content-visibility: auto;
}

@custom-variant theme-midnight
  (&:where([data-theme="midnight"] *));
```

Bạn vẫn có thể gặp `@config` và `@plugin` để tương thích với hệ sinh thái hoặc migrate dự án (project / 프로젝트) v3, nhưng tư duy nên học cho mã (code / 코드) mới là ưu tiên CSS (CSS-first).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **3. Tailwind v4.3 khác Tailwind v3 như thế nào?** xác định đầu vào; **4. Cài Tailwind và hiểu quy trình bản dựng (build / 빌드) (build pipeline)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. @import "tailwindcss" và các lớp phân tầng (cascade layer)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Cài Tailwind và hiểu quy trình bản dựng (build / 빌드) (build pipeline)

Với Vite, setup cơ bản hiện đại thường là:

```bash
npm install tailwindcss @tailwindcss/vite
```

Sau đó thêm plugin:

```js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

Trong biểu định kiểu (stylesheet / 스타일시트) chính:

```css
@import "tailwindcss";
```

Nếu dùng CLI:

```bash
npm install tailwindcss @tailwindcss/cli
```

và compile bằng:

```bash
npx @tailwindcss/cli \
  -i ./src/input.css \
  -o ./dist/output.css \
  --watch
```

Điểm cần hiểu là Tailwind không chạy trong trình duyệt (browser / 브라우저) để đọc lớp (class / 클래스) rồi style element. Tailwind chạy ở **bản dựng (build / 빌드) thời gian (time / 시간)**. Nó scan mã nguồn (source code / 소스 코드), nhận ra các lớp (class / 클래스) có khả năng là Tailwind tiện ích (utility), generate CSS cần thiết và trình duyệt (browser / 브라우저) chỉ nhận biểu định kiểu (stylesheet / 스타일시트) cuối.

Chuỗi xử lý (pipeline / 파이프라인) có thể hình dung:

```text
HTML / JSX / Vue / Svelte
        │
        ▼
Tailwind source scanner
        │
        ▼
utility + variant resolver
        │
        ▼
generated CSS
        │
        ▼
browser
```

Vì vậy nếu bạn viết một lớp (class / 클래스) mà Tailwind không nhận ra ở bản dựng (build / 빌드) thời gian (time / 시간), CSS tương ứng sẽ không tồn tại dù string đó xuất hiện thời gian chạy (runtime / 런타임).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **4. Cài Tailwind và hiểu quy trình bản dựng (build / 빌드) (build pipeline)** xác định đầu vào; **5. @import "tailwindcss" và các lớp phân tầng (cascade layer)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. Preflight (lớp reset nền của Tailwind) là gì và tại sao HTML trông “khác bình thường”?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. `@import "tailwindcss"` và các lớp phân tầng (cascade layer)

Một dòng:

```css
@import "tailwindcss";
```

không đơn giản là import một tệp (file / 파일) CSS tĩnh khổng lồ. Tailwind v4 dùng các bản địa (native / 네이티브) CSS lớp phân tầng (cascade layer) quan trọng như:

```text
theme
base
components
utilities
```

`theme` chứa đơn vị từ (token / 토큰) thiết kế (design tokens). `base` chứa Preflight (lớp reset nền của Tailwind) và cơ sở (base / 기반) rules. `components` dành cho component-level custom styles. `utilities` chứa tiện ích (utility) rules.

CSS lớp phân tầng (cascade layer) giải quyết thứ tự ưu tiên giữa các nhóm quy tắc (rule / 규칙). Trong cùng author origin với normal các khai báo (declarations), tầng (layer / 계층) xuất hiện sau thường có priority cao hơn tầng (layer / 계층) trước. Vì các tiện ích (utilities) nằm sau components, một tiện ích (utility) như `p-6` có thể override padding được đặt trong thành phần (component / 컴포넌트) tầng (layer / 계층) mà không cần tăng độ đặc hiệu (specificity).

Điều này giải thích một nguyên tắc cấp cao (senior / 시니어): Tailwind cố gắng thắng bằng **kiến trúc (architecture / 아키텍처) của cơ chế phân tầng (cascade)** thay vì tạo bộ chọn (selector) độ đặc hiệu (specificity) rất cao.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **6. Preflight (lớp reset nền của Tailwind) là gì và tại sao HTML trông “khác bình thường”?** tiếp nhận điểm tựa từ **5. @import "tailwindcss" và các lớp phân tầng (cascade layer)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Cấu trúc một Tailwind lớp (class / 클래스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Preflight (lớp reset nền của Tailwind) là gì và tại sao HTML trông “khác bình thường”?

Tailwind import mặc định bao gồm một cơ sở (base / 기반) reset gọi là **Preflight (lớp reset nền của Tailwind)**. trình duyệt (browser / 브라우저) vốn có user-agent biểu định kiểu (stylesheet / 스타일시트), nghĩa là `<h1>` tự có font-size và margin, `<ul>` tự có bullet, `<body>` có margin mặc định, button/đầu vào (input / 입력) có một số style bản địa (native / 네이티브).

Preflight (lớp reset nền của Tailwind) normalize nhiều thứ để UI bắt đầu từ nền tảng dễ kiểm soát hơn. Vì vậy nếu bạn viết:

```html
<h1>Hello</h1>
```

và thấy nó không to, đậm, có margin giống HTML thuần, đó là hành vi (behavior / 동작) có chủ ý. Tailwind muốn bạn nói rõ thiết kế (design / 설계):

```html
<h1 class="text-3xl font-bold tracking-tight">
  Hello
</h1>
```

Preflight (lớp reset nền của Tailwind) rất tiện trong app mới, nhưng có thể gây xung đột khi nhúng Tailwind vào một hệ thống cũ đã có reset hoặc một widget chạy bên trong host page. Trong trường hợp đó, cấp cao (senior / 시니어) cần cân nhắc import các phần Tailwind một cách có kiểm soát thay vì mặc định dùng full Preflight (lớp reset nền của Tailwind).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **7. Cấu trúc một Tailwind lớp (class / 클래스)** tiếp nhận điểm tựa từ **6. Preflight (lớp reset nền của Tailwind) là gì và tại sao HTML trông “khác bình thường”?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Spacing quy mô (scale / 규모) và vì sao p-4 không phải “4px”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Cấu trúc một Tailwind lớp (class / 클래스)

Hãy phân tích:

```text
md:hover:bg-blue-600/80
```

Phần `bg-blue-600` là tiện ích (utility) chính. `bg-` nói rằng tiện ích (utility) ảnh hưởng background; `blue-600` là theme giá trị (value / 값). `/80` là modifier opacity/alpha trong family này. `hover:` thêm điều kiện hover. `md:` thêm điều kiện responsive điểm ngắt (breakpoint).

Bạn nên đọc từ ngoài vào trong theo ý nghĩa:

```text
khi viewport đạt md
và element đang hover
thì background dùng blue-600 với alpha 80%
```

Một lớp (class / 클래스) khác:

```text
w-[37rem]
```

có tiện ích (utility) family `w-` và giá trị tùy ý (arbitrary value) `[37rem]`.

Một lớp (class / 클래스):

```text
text-(color:--label)
```

dùng CSS biến (variable) `--label` và kiểu (type / 타입) hint `color` để nói rõ rằng `text-*` ở đây là văn bản (text / 텍스트) color chứ không phải font-size.

Tailwind lớp (class / 클래스) vì vậy có grammar tương đối nhất quán. Khi hiểu grammar, bạn không cần thuộc mọi lớp (class / 클래스).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **8. Spacing quy mô (scale / 규모) và vì sao p-4 không phải “4px”** tiếp nhận điểm tựa từ **7. Cấu trúc một Tailwind lớp (class / 클래스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. các giá trị tùy ý (arbitrary values): escape hatch cần thiết nhưng không phải hệ thống thiết kế (design system)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Spacing quy mô (scale / 규모) và vì sao `p-4` không phải “4px”

Một trong những hiểu nhầm đầu tiên là nghĩ `p-4` bằng `padding: 4px`. Trong Tailwind v4, nhiều spacing các tiện ích (utilities) được derive từ cơ sở (base / 기반) spacing theme. Mặc định, `--spacing` thường có basis là `0.25rem`.

Do đó:

```text
p-1 ≈ 0.25rem
p-2 ≈ 0.5rem
p-4 ≈ 1rem
p-6 ≈ 1.5rem
p-8 ≈ 2rem
```

Nếu gốc (root / 루트) font-size mặc định là 16px thì `1rem` thường tương ứng 16 CSS pixels, nhưng hãy nhớ `rem` là font-relative đơn vị (unit / 단위), không phải hard-coded px.

Tailwind v4 linh hoạt hơn v3 trong nhiều numeric tiện ích (utility) families. Những giá trị (value / 값) như:

```text
mt-17
w-29
```

có thể được derive từ spacing hệ thống (system / 시스템) nếu tiện ích (utility) family đó hỗ trợ. Điều này rất tiện, nhưng cấp cao (senior / 시니어) không nên biến sự linh hoạt của trình biên dịch (compiler / 컴파일러) thành một hệ thống thiết kế (design system) hỗn loạn. khung phần mềm (framework / 프레임워크) cho phép `p-13` không có nghĩa UI nên có spacing 13 ở khắp nơi.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **9. các giá trị tùy ý (arbitrary values): escape hatch cần thiết nhưng không phải hệ thống thiết kế (design system)** tiếp nhận điểm tựa từ **8. Spacing quy mô (scale / 규모) và vì sao p-4 không phải “4px”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. các thuộc tính tùy ý (arbitrary properties)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. các giá trị tùy ý (arbitrary values): escape hatch cần thiết nhưng không phải hệ thống thiết kế (design system)

Khi tiện ích (utility) đơn vị từ (token / 토큰) không có đúng giá trị (value / 값) bạn cần, Tailwind cho phép giá trị tùy ý (arbitrary value):

```html
<div class="top-[117px]">
```

CSS được generate về bản chất là:

```css
top: 117px;
```

Bạn vẫn dùng biến thể (variant) bình thường:

```html
<div class="top-[117px] lg:top-[344px]">
```

giá trị tùy ý (arbitrary value) rất phù hợp cho những exception như vị trí một decorative illustration, một grid template phức tạp hoặc kích thước được quy định chính xác bởi asset.

Nhưng nếu toàn dự án (project / 프로젝트) có:

```text
rounded-[11px]
text-[15px]
p-[13px]
gap-[18px]
```

lặp đi lặp lại, bạn đang mất lợi ích của đơn vị từ (token / 토큰) thiết kế (design token). Khi một giá trị tùy ý (arbitrary value) bắt đầu trở thành vocabulary lặp lại, hãy promote nó thành theme đơn vị từ (token / 토큰).

Ví dụ:

```css
@theme {
  --radius-card: 11px;
}
```

Sau đó:

```html
<div class="rounded-card">
```

Đây là mẫu (pattern / 패턴):

```text
one-off exception
→ xuất hiện lặp lại
→ trở thành token
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **10. các thuộc tính tùy ý (arbitrary properties)** tiếp nhận điểm tựa từ **9. các giá trị tùy ý (arbitrary values): escape hatch cần thiết nhưng không phải hệ thống thiết kế (design system)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. các biến thể tùy ý (arbitrary variants)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. các thuộc tính tùy ý (arbitrary properties)

Không phải mọi CSS thuộc tính (property / 속성) đều cần một named Tailwind tiện ích (utility). Bạn có thể viết thuộc tính (property / 속성) trực tiếp:

```html
<div class="[mask-type:luminance]">
```

Tailwind generate:

```css
mask-type: luminance;
```

Có thể kết hợp trạng thái (state / 상태):

```html
<div class="hover:[mask-type:alpha]">
```

Hoặc đặt CSS biến (variable):

```html
<div class="[--header-offset:56px] lg:[--header-offset:72px]">
```

thuộc tính tùy ý (arbitrary property) là cách rất mạnh để dùng ngay CSS nền tảng (platform / 플랫폼) mà không phải viết custom plugin cho một trường hợp (case / 사례) nhỏ.

Cấp cao (senior / 시니어) cần tránh một cực đoan khác: đừng biến lớp (class / 클래스) attribute thành một biểu định kiểu (stylesheet / 스타일시트) hoàn chỉnh bằng hàng chục các thuộc tính tùy ý (arbitrary properties). Nếu một quy tắc (rule / 규칙) phức tạp rõ ràng hơn khi viết CSS, hãy viết CSS.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **11. các biến thể tùy ý (arbitrary variants)** tiếp nhận điểm tựa từ **10. các thuộc tính tùy ý (arbitrary properties)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. CSS biến (variable) shorthand và thời gian chạy (runtime / 런타임) giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. các biến thể tùy ý (arbitrary variants)

biến thể tùy ý (arbitrary variant) cho phép bạn viết bộ chọn (selector) điều kiện (condition / 조건) trực tiếp.

```html
<div class="[&>p]:mt-4">
  <p>...</p>
</div>
```

`&` đại diện cho element hiện tại. Ý nghĩa gần:

```css
.current > p {
  margin-top: 1rem;
}
```

Một bộ chọn (selector) phức tạp hơn:

```html
<ul class="[&_li:nth-child(odd)]:bg-gray-50">
```

Tailwind thay `_` thành whitespace khi phù hợp, nên bộ chọn (selector) gần:

```css
.current li:nth-child(odd) {
  background-color: ...;
}
```

các biến thể tùy ý (arbitrary variants) tuyệt vời cho tích hợp (integration / 통합) ngắn hoặc markup bạn không kiểm soát. Nhưng nếu bộ chọn (selector) lặp đi lặp lại, hãy cân nhắc `@custom-variant`, thành phần (component / 컴포넌트) lớp trừu tượng (abstraction / 추상화) hoặc biểu định kiểu (stylesheet / 스타일시트) tích hợp (integration / 통합) riêng.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **12. CSS biến (variable) shorthand và thời gian chạy (runtime / 런타임) giá trị (value / 값)** tiếp nhận điểm tựa từ **11. các biến thể tùy ý (arbitrary variants)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Tailwind scan nguồn (source / 소스) như văn bản (text / 텍스트), không chạy mã (code / 코드) của bạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. CSS biến (variable) shorthand và thời gian chạy (runtime / 런타임) giá trị (value / 값)

Một mẫu (pattern / 패턴) cực quan trọng là kết hợp Tailwind static tiện ích (utility) với CSS biến (variable) động (dynamic / 동적) giá trị (value / 값).

Ví dụ:

```html
<div class="w-(--panel-width)">
```

Tailwind hiểu gần như:

```css
width: var(--panel-width);
```

React có thể set biến (variable):

```jsx
<div
  style={{ "--panel-width": `${width}px` }}
  className="w-(--panel-width)"
/>
```

Điểm mạnh là lớp (class / 클래스) `w-(--panel-width)` tồn tại hoàn chỉnh ở nguồn (source / 소스) nên Tailwind generate được CSS, trong khi giá trị `width` có thể thay đổi thời gian chạy (runtime / 런타임).

Mẫu (pattern / 패턴) này tốt hơn:

```jsx
className={`w-[${width}px]`}
```

vì string arbitrary lớp (class / 클래스) thời gian chạy (runtime / 런타임) có thể không được scanner nhìn thấy.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **12. CSS biến (variable) shorthand và thời gian chạy (runtime / 런타임) giá trị (value / 값)** nêu điều cần giải thích; **13. Tailwind scan nguồn (source / 소스) như văn bản (text / 텍스트), không chạy mã (code / 코드) của bạn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. display: hiểu block, inline, flex, grid trước khi dùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Tailwind scan nguồn (source / 소스) như văn bản (text / 텍스트), không chạy mã (code / 코드) của bạn

Đây là kiến thức bắt buộc.

Mã (code / 코드) sai:

```jsx
function Button({ color }) {
  return (
    <button
      className={`bg-${color}-600`}
    />
  );
}
```

Khi scan nguồn (source / 소스), Tailwind chỉ thấy các fragment `bg-`, `${color}`, `-600`. Nó không biết thời gian chạy (runtime / 런타임) prop sẽ là `blue`, `red` hay `green`.

Cách đúng:

```jsx
const colorVariants = {
  blue:
    "bg-blue-600 hover:bg-blue-700 text-white",
  red:
    "bg-red-600 hover:bg-red-700 text-white",
};

function Button({ color }) {
  return (
    <button className={colorVariants[color]} />
  );
}
```

Các complete lớp (class / 클래스) strings đã nằm trong nguồn (source / 소스), nên scanner nhận được.

Đây đồng thời là thành phần (component / 컴포넌트) thiết kế (design / 설계) tốt hơn: thành phần (component / 컴포넌트) chỉ cho phép một tập biến thể (variant) hữu hạn thay vì cho caller tạo arbitrary Tailwind lớp (class / 클래스).

---

# PHẦN II — bố cục (layout / 레이아웃) VÀ mô hình hộp (box model / 박스 모델) TRONG TAILWIND

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **13. Tailwind scan nguồn (source / 소스) như văn bản (text / 텍스트), không chạy mã (code / 코드) của bạn** nêu điều cần giải thích; **14. display: hiểu block, inline, flex, grid trước khi dùng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. hidden, invisible, opacity-0 khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. `display`: hiểu `block`, `inline`, `flex`, `grid` trước khi dùng

CSS `display` quyết định element tham gia bố cục (layout / 레이아웃) theo kiểu nào. Tailwind cung cấp những tiện ích (utility) trực tiếp như:

```text
block
inline
inline-block
flex
inline-flex
grid
inline-grid
flow-root
contents
hidden
```

`block` tạo block-level box, thường chiếm available inline width theo luồng bố cục thông thường (normal flow / 일반 흐름). `inline` chạy trong dòng văn bản (text / 텍스트) và width/height không hoạt động giống khối (block / 블록). `inline-block` giữ khả năng đứng trong inline luồng (flow / 흐름) nhưng có box sizing giống khối (block / 블록) hơn.

`flex` tạo flex bộ chứa (container / 컨테이너). Children trực tiếp trở thành các phần tử Flex (flex items). `grid` tạo grid bộ chứa (container / 컨테이너). `hidden` đặt `display: none`, nghĩa là element bị loại khỏi bố cục (layout / 레이아웃); đây khác hoàn toàn với `invisible` hay `opacity-0`.

Ví dụ responsive visibility:

```html
<nav class="hidden md:block">
  ...
</nav>
```

Ở cơ sở (base / 기반)/mobile, nav không có box. Từ điểm ngắt (breakpoint) `md`, Tailwind generate quy tắc (rule / 규칙) `display: block`.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **15. hidden, invisible, opacity-0 khác nhau** tiếp nhận điểm tựa từ **14. display: hiểu block, inline, flex, grid trước khi dùng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Box sizing: box-border và box-content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. `hidden`, `invisible`, `opacity-0` khác nhau

Ba tiện ích (utility) này thường bị dùng như nhau nhưng hành vi (behavior / 동작) rất khác.

```text
hidden
```

tương đương `display:none`. Element không chiếm bố cục (layout / 레이아웃) và thông thường không tham gia cây khả năng tiếp cận (accessibility tree / 접근성 트리) như element hiển thị.

```text
invisible
```

tương đương `visibility:hidden`. Box vẫn chiếm chỗ, nhưng không được vẽ/tương tác (interaction / 상호작용) bình thường.

```text
opacity-0
```

tương đương `opacity:0`. Element vẫn tồn tại trong bố cục (layout / 레이아웃) và có thể vẫn nhận pointer/focus tùy ngữ nghĩa (semantics / 의미론).

Nếu bạn muốn animate fade, `opacity-0` thường phù hợp hơn vì `display:none` không đơn giản chuyển tiếp (transition / 전이) như opacity. Nếu bạn muốn bỏ element khỏi bố cục (layout / 레이아웃), `hidden` phù hợp hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **16. Box sizing: box-border và box-content** tiếp nhận điểm tựa từ **15. hidden, invisible, opacity-0 khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Position: relative, absolute, fixed, sticky** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Box sizing: `box-border` và `box-content`

CSS width mặc định theo content box có thể gây nhầm. Nếu element:

```css
width: 300px;
padding: 20px;
border: 1px solid;
```

với `content-box`, tổng outer width lớn hơn 300px.

Tailwind Preflight (lớp reset nền của Tailwind) thường làm sizing predictable hơn, nhưng bạn vẫn nên hiểu:

```text
box-border
→ box-sizing:border-box
```

và:

```text
box-content
→ box-sizing:content-box
```

Với `border-box`, declared width đã bao gồm padding và border. Đây là mô hình (model / 모델) thường dễ dùng hơn trong UI.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **17. Position: relative, absolute, fixed, sticky** tiếp nhận điểm tựa từ **16. Box sizing: box-border và box-content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Inset và logical inset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Position: `relative`, `absolute`, `fixed`, `sticky`

`relative` thường được dùng để tạo positioning ngữ cảnh (context / 맥락) cho `absolute` child:

```html
<div class="relative">
  <span
    class="
      absolute
      right-2
      top-2
    "
  >
    New
  </span>
</div>
```

Parent vẫn nằm trong luồng bố cục thông thường (normal flow / 일반 흐름). Child `absolute` được lấy ra khỏi luồng bố cục thông thường (normal flow / 일반 흐름) và offset theo khối chứa tham chiếu (containing block / 컨테이닝 블록) phù hợp, ở đây thường là parent `relative`.

`fixed` thường gắn theo vùng nhìn (viewport) và dùng cho full-screen overlay, floating button hoặc persistent UI.

`sticky` rất hay bị hiểu sai. Nó không đơn giản là “fixed khi scroll”. Sticky phụ thuộc vùng chứa cuộn (scroll container) và inset. Ví dụ:

```html
<header class="sticky top-0">
```

cần `top-0` làm sticky threshold. Nếu ancestor có overflow tạo vùng chứa cuộn (scroll container) khác, sticky sẽ liên quan bộ chứa (container / 컨테이너) đó. Khi `sticky` không chạy, hãy kiểm tra vùng chứa cuộn (scroll container) trước khi thêm lớp (class / 클래스) ngẫu nhiên.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **18. Inset và logical inset** tiếp nhận điểm tựa từ **17. Position: relative, absolute, fixed, sticky** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. z- và ngữ cảnh xếp chồng (stacking context / 쌓임 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Inset và logical inset

Các lớp (class / 클래스):

```text
top-4
right-4
bottom-4
left-4
inset-0
inset-x-4
inset-y-4
```

map khóa–giá trị (map) trực tiếp tới CSS positional offsets.

V4.2+ có logical các tiện ích (utilities) như:

```text
inset-s-4
inset-e-4
inset-bs-4
inset-be-4
```

`inline-start` trong giao diện LTR thường là trái, nhưng trong RTL có thể là phải. Vì vậy logical các tiện ích (utilities) phù hợp với app đa ngôn ngữ.

Nếu mục tiêu là “icon ở cuối dòng” chứ không phải “icon luôn ở cạnh phải vật lý”, logical tiện ích (utility) tốt hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **19. z- và ngữ cảnh xếp chồng (stacking context / 쌓임 맥락)** tiếp nhận điểm tựa từ **18. Inset và logical inset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Overflow và vùng chứa cuộn (scroll container)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. `z-*` và ngữ cảnh xếp chồng (stacking context / 쌓임 맥락)

Tailwind cung cấp:

```text
z-0
z-10
z-20
...
z-50
z-auto
z-[999]
```

Nhưng `z-index` chỉ có ý nghĩa trong stacking mô hình (model / 모델) của CSS. Một child `z-[9999]` vẫn có thể nằm dưới một element khác nếu parent của nó đang nằm trong ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) thấp hơn.

Do đó khi modal/dropdown bị che, đừng tăng `z-index` vô hạn. Hãy kiểm tra ancestor có:
- transform,
- opacity,
- cô lập (isolation),
- positioned + z-index,
- filter,
hay thuộc tính (property / 속성) khác tạo ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) hay không.

Trong hệ thống thiết kế (design system) lớn, nên có mang tính ngữ nghĩa (semantic / 의미적) tầng (layer / 계층) đặc tả hợp đồng (contract / 계약) cho dropdown, sticky header, overlay, modal và toast thay vì mỗi thành phần (component / 컴포넌트) chọn số tùy ý.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **19. z- và ngữ cảnh xếp chồng (stacking context / 쌓임 맥락)** xác định đầu vào; **20. Overflow và vùng chứa cuộn (scroll container)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **21. Width: w- không chỉ có px** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Overflow và vùng chứa cuộn (scroll container)

Tailwind có:

```text
overflow-auto
overflow-hidden
overflow-clip
overflow-visible
overflow-scroll
overflow-x-auto
overflow-y-auto
```

`overflow-auto` tạo scroll khi content thực sự vượt box. `overflow-hidden` clip content và có scroll-container ngữ nghĩa (semantics / 의미론) khác `overflow-clip`. `overflow-clip` chỉ clip theo intent mạnh hơn, không phải là một vùng chứa cuộn (scroll container) như hidden.

Một mẫu (pattern / 패턴) cực phổ biến cho bảng:

```html
<div class="overflow-x-auto">
  <table class="min-w-full">
    ...
  </table>
</div>
```

Wrapper chịu horizontal scroll thay vì làm cả page overflow.

Cấp cao (senior / 시니어) phải nhớ overflow ảnh hưởng nhiều thứ khác ngoài scrollbar, đặc biệt là sticky positioning và clipping.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **20. Overflow và vùng chứa cuộn (scroll container)** xác định đầu vào; **21. Width: w- không chỉ có px** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. Height và vùng nhìn (viewport) units: h-screen không phải lúc nào cũng tốt nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Width: `w-*` không chỉ có px

Tailwind width family bao gồm spacing-derived các giá trị (values), fraction, percentages, vùng nhìn (viewport) và định cỡ nội tại (intrinsic sizing / 내재 크기 결정).

```text
w-4
w-64
w-full
w-1/2
w-screen
w-dvw
w-min
w-max
w-fit
w-[37rem]
```

`w-full` thường là `width:100%` của khối chứa tham chiếu (containing block / 컨테이닝 블록). `w-screen` là vùng nhìn (viewport) width kiểu `100vw`; `w-dvw` dùng động (dynamic / 동적) vùng nhìn (viewport) width.

`w-min` tương ứng intrinsic `min-content`. `w-max` tương ứng `max-content`. `w-fit` dùng `fit-content`.

Khi bạn chọn width, hãy nghĩ “ràng buộc (constraint / 제약조건) nào cần?” thay vì mặc định đặt số px.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **22. Height và vùng nhìn (viewport) units: h-screen không phải lúc nào cũng tốt nhất** tiếp nhận điểm tựa từ **21. Width: w- không chỉ có px** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. max-w- và readable content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Height và vùng nhìn (viewport) units: `h-screen` không phải lúc nào cũng tốt nhất

`h-screen` tương đương classic `100vh`. Trên mobile trình duyệt (browser / 브라우저), UI chrome như address bar có thể làm vùng nhìn (viewport) thay đổi và `100vh` gây bố cục (layout / 레이아웃) không đúng như mong muốn.

Hiện đại (modern / 현대적) các tiện ích (utilities):

```text
h-dvh
h-svh
h-lvh
min-h-dvh
```

liên hệ tới động (dynamic / 동적), small và large vùng nhìn (viewport) units.

Một full-page mobile bố cục (layout / 레이아웃) thường tốt hơn với:

```html
<div class="min-h-dvh">
```

thay vì ép `h-screen`, vì minimum height cho phép content dài thêm và `dvh` phản ánh vùng nhìn (viewport) động tốt hơn.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **23. max-w- và readable content** tiếp nhận điểm tựa từ **22. Height và vùng nhìn (viewport) units: h-screen không phải lúc nào cũng tốt nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. min-w-0: một lớp (class / 클래스) nhỏ nhưng cực kỳ cấp cao (senior / 시니어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. `max-w-*` và readable content

Tailwind có các max width đơn vị từ (token / 토큰) như:

```text
max-w-sm
max-w-md
max-w-lg
max-w-7xl
max-w-prose
max-w-full
max-w-none
```

`max-w-prose` rất hữu ích cho văn bản (text / 텍스트) body vì một dòng quá dài sẽ khó đọc. Đây không phải magic “prose thành phần (component / 컴포넌트)”, mà chỉ là width ràng buộc (constraint / 제약조건) được thiết kế quanh readable line measure.

Page bộ chứa (container / 컨테이너) thường:

```html
<div class="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8">
  ...
</div>
```

`w-full` cho phép full available width, `max-w-7xl` cap lại, `mx-auto` center khi còn không gian dư (free space), còn `px-*` tạo gutter.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **24. min-w-0: một lớp (class / 클래스) nhỏ nhưng cực kỳ cấp cao (senior / 시니어)** tiếp nhận điểm tựa từ **23. max-w- và readable content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. min-h-0: phiên bản vertical của cùng vấn đề** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. `min-w-0`: một lớp (class / 클래스) nhỏ nhưng cực kỳ cấp cao (senior / 시니어)

Hãy xem:

```html
<div class="flex gap-3">
  <img class="size-10 shrink-0">

  <div class="flex-1">
    <p class="truncate">
      A very very very long text...
    </p>
  </div>
</div>
```

Nhiều dev nghĩ `truncate` sẽ tự ellipsis. Nhưng phần tử Flex (flex item) có kích thước tối thiểu tự động (automatic minimum size) dựa trên intrinsic content. Child `.flex-1` có thể từ chối co nhỏ hơn content cần, khiến `truncate` không hoạt động như mong đợi.

Fix:

```html
<div class="min-w-0 flex-1">
```

`min-w-0` nói rằng minimum width được phép là 0 thay vì content-based mức tối thiểu tự động (automatic minimum). Sau đó overflow/ellipsis mới có không gian để hoạt động.

Đây là một trong những tiện ích (utility) bạn nên hiểu bản chất thay vì học thuộc.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **25. min-h-0: phiên bản vertical của cùng vấn đề** tiếp nhận điểm tựa từ **24. min-w-0: một lớp (class / 클래스) nhỏ nhưng cực kỳ cấp cao (senior / 시니어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Margin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. `min-h-0`: phiên bản vertical của cùng vấn đề

Một bố cục (layout / 레이아웃) dashboard:

```html
<div class="flex h-dvh flex-col">
  <header class="shrink-0">
    ...
  </header>

  <main class="min-h-0 flex-1 overflow-auto">
    ...
  </main>
</div>
```

Nếu `main` không có `min-h-0`, kích thước tối thiểu tự động (automatic minimum size) trong flex column có thể làm main không chịu co và toàn page overflow. `min-h-0` cho phép vùng còn lại co đúng để `overflow-auto` tạo scroller nội bộ.

Mẫu (pattern / 패턴) này rất phổ biến trong:
- app shell,
- modal body,
- sidebar panel,
- chat giao diện (interface / 인터페이스).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **26. Margin** tiếp nhận điểm tựa từ **25. min-h-0: phiên bản vertical của cùng vấn đề** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Padding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Margin

Tailwind margin:

```text
m-4
mx-4
my-4
mt-4
mr-4
mb-4
ml-4
ms-4
me-4
-mt-4
mx-auto
```

`m-*` áp mọi cạnh. `mx-*` và `my-*` là shorthand hai trục. `ms-*` và `me-*` là logical inline start/end. Prefix `-` tạo negative margin khi CSS thuộc tính (property / 속성) cho phép.

`mx-auto` là idiom center một khối (block / 블록) đã có width/max-width:

```html
<div class="mx-auto max-w-4xl">
```

Negative margin nên dùng có chủ ý, thường cho overlap/visual composition. Nếu bạn liên tục cần negative margin để “sửa vị trí”, có thể bố cục (layout / 레이아웃) kiến trúc (architecture / 아키텍처) đang sai.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **27. Padding** tiếp nhận điểm tựa từ **26. Margin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. gap- nên được ưu tiên cho Flex/Grid spacing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Padding

Padding các tiện ích (utilities) tương tự:

```text
p-4
px-4
py-4
pt-4
pr-4
pb-4
pl-4
ps-4
pe-4
```

Padding thuộc box của chính element và không thể âm. Khi button cần touch mục tiêu (target / 대상), padding thường là phần làm thành phần (component / 컴포넌트) dễ bấm chứ không chỉ tạo khoảng cách đẹp.

Một button:

```html
<button class="min-h-11 rounded-lg px-4 py-2">
```

`min-h-11` đảm bảo chiều cao tối thiểu, còn `px/py` tạo nội bộ (internal / 내부) không gian (space / 공간).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **28. gap- nên được ưu tiên cho Flex/Grid spacing** tiếp nhận điểm tựa từ **27. Padding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. divide- khác gap-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. `gap-*` nên được ưu tiên cho Flex/Grid spacing

Ví dụ:

```html
<div class="flex flex-col gap-4">
```

`gap-4` map khóa–giá trị (map) tới CSS `gap`, nghĩa là spacing thuộc **bộ chứa (container / 컨테이너) bố cục (layout / 레이아웃)**, không phải margin của từng child.

So với:

```html
<div>
  <div class="mb-4">...</div>
  <div class="mb-4">...</div>
</div>
```

`gap` dễ maintain hơn vì:
- không cần `last:mb-0`,
- spacing responsibility thuộc parent,
- hoạt động tốt với wrapping Flex/Grid.

Tailwind vẫn có `space-y-*` và `space-x-*`, sử dụng bộ chọn (selector)/margin để tạo spacing giữa siblings. Chúng hữu ích trong một số normal-flow cases, nhưng với Flex/Grid mới, `gap` thường là lựa chọn đầu tiên.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **29. divide- khác gap-** tiếp nhận điểm tựa từ **28. gap- nên được ưu tiên cho Flex/Grid spacing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Flexbox: phải hiểu bộ chứa (container / 컨테이너) và item** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. `divide-*` khác `gap-*`
Phần này nối mạch bài học với “29. `divide-*` khác `gap-*`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<ul class="divide-y divide-gray-200">
  ...
</ul>
```

`divide-y` tạo border giữa children. Nó không tạo khoảng trống như gap.

Bạn có thể hình dung:

```text
gap
→ empty space between items

divide
→ visual separator between items
```

Một danh sách (list / 목록) có thể dùng cả hai nếu thiết kế (design / 설계) cần, nhưng thường `divide` đã đóng vai trò divider.

---

# PHẦN III — FLEXBOX TRONG TAILWIND

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **30. Flexbox: phải hiểu bộ chứa (container / 컨테이너) và item** tiếp nhận điểm tựa từ **29. divide- khác gap-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. justify-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Flexbox: phải hiểu bộ chứa (container / 컨테이너) và item

Khi viết:

```html
<div class="flex">
```

element này trở thành **flex bộ chứa (container / 컨테이너)**, và các child trực tiếp trở thành **các phần tử Flex (flex items)**.

Flexbox có hai trục:
- trục chính (main axis),
- trục chéo (cross axis).

`flex-row` đặt trục chính (main axis) theo row. `flex-col` đặt trục chính (main axis) theo column.

```html
<div class="flex flex-row">
```

children xếp theo hàng.

```html
<div class="flex flex-col">
```

children xếp theo cột.

Điều này rất quan trọng vì `justify-*` hoạt động theo trục chính (main axis), còn `items-*` hoạt động theo trục chéo (cross axis). Nếu bạn đổi row thành column, ý nghĩa trực quan của justify/items cũng đổi.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **31. justify-** tiếp nhận điểm tựa từ **30. Flexbox: phải hiểu bộ chứa (container / 컨테이너) và item** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. items- và đường cơ sở (baseline)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. `justify-*`

Các tiện ích (utility) chính:

```text
justify-start
justify-center
justify-end
justify-between
justify-around
justify-evenly
```

Với `flex-row`, `justify-center` thường center theo ngang. Với `flex-col`, nó center theo dọc vì trục chính (main axis) đã đổi.

Ví dụ center hai chiều:

```html
<div class="flex items-center justify-center">
```

Nhưng nếu chỉ cần center content đơn giản, Grid thường ngắn hơn:

```html
<div class="grid place-items-center">
```

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **32. items- và đường cơ sở (baseline)** tiếp nhận điểm tựa từ **31. justify-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. flex-wrap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. `items-*` và đường cơ sở (baseline)

`items-center` rất phổ biến:

```html
<div class="flex items-center gap-2">
  <svg>...</svg>
  <span>Label</span>
</div>
```

Nó align item theo cross-axis center.

Nhưng text-heavy UI đôi khi phù hợp với:

```text
items-baseline
```

đường cơ sở (baseline) alignment căn dựa trên typography đường cơ sở (baseline) chứ không phải geometric box center. Ví dụ hai văn bản (text / 텍스트) có font-size khác nhau có thể trông tự nhiên hơn với đường cơ sở (baseline).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **33. flex-wrap** tiếp nhận điểm tựa từ **32. items- và đường cơ sở (baseline)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. flex-1 không giống grow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. `flex-wrap`

Mặc định Flexbox thường nowrap. Tailwind:

```text
flex-nowrap
flex-wrap
flex-wrap-reverse
```

Tags/chips:

```html
<div class="flex flex-wrap gap-2">
  ...
</div>
```

Nếu không wrap, content có thể overflow hoặc items shrink mạnh.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **34. flex-1 không giống grow** tiếp nhận điểm tựa từ **33. flex-wrap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. shrink và shrink-0** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. `flex-1` không giống `grow`

`grow` chỉ thay đổi `flex-grow`.

```text
grow
→ flex-grow:1
```

Trong khi `flex-1` là flex shorthand và thay đổi nhiều thành phần flex sizing, về khái niệm giúp item chia không gian khả dụng (available space) với basis kiểu zero-ish.

Ví dụ:

```html
<div class="flex">
  <aside class="w-64 shrink-0">...</aside>
  <main class="min-w-0 flex-1">...</main>
</div>
```

`aside` giữ width, `main` lấy phần còn lại.

Nếu bạn chỉ viết `grow`, basis vẫn có thể khác và hành vi (behavior / 동작) không luôn giống `flex-1`.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **35. shrink và shrink-0** tiếp nhận điểm tựa từ **34. flex-1 không giống grow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. basis-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. `shrink` và `shrink-0`

Mặc định phần tử Flex (flex item) có thể shrink.

Avatar:

```html
<img class="size-12 shrink-0">
```

Nếu thiếu `shrink-0`, trong row quá chật avatar có thể bị co nhỏ hơn expected.

`shrink-0` đặc biệt phù hợp cho:
- icon,
- avatar,
- fixed sidebar,
- hành động (action / 동작) button
mà bạn không muốn bị co để nhường chỗ cho văn bản (text / 텍스트).

Sau đó văn bản (text / 텍스트) bộ chứa (container / 컨테이너) thường dùng:

```text
min-w-0 flex-1
```

Đây là pair rất thực tế.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **36. basis-** tiếp nhận điểm tựa từ **35. shrink và shrink-0** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. self-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. `basis-*`

`flex-basis` là kích thước khởi điểm theo trục chính (main axis) trước khi grow/shrink phân phối không gian dư (free space).

Tailwind:

```text
basis-64
basis-1/2
basis-auto
basis-full
```

Nếu bạn muốn sidebar “ban đầu khoảng 16rem nhưng có flex lô-gic (logic / 논리)”, `basis-64` có thể thích hợp hơn `w-64` trong một số flex kiến trúc (architecture / 아키텍처).

Cấp cao (senior / 시니어) nên hiểu width và flex-basis có thể cùng tham gia sizing; không thêm cả hai nếu không biết cái nào đang quyết định.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **37. self-** tiếp nhận điểm tựa từ **36. basis-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Flex pattern: Media Object** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. `self-*`

Bộ chứa (container / 컨테이너) đặt:

```text
items-center
```

nhưng một item có thể override:

```html
<div class="self-start">
```

`self-*` map khóa–giá trị (map) tới `align-self`.

Use khi một child thật sự có cross-axis alignment khác phần còn lại, không dùng để vá alignment ngẫu nhiên.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **38. Flex pattern: Media Object** tiếp nhận điểm tựa từ **37. self-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Grid khác Flexbox ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Flex pattern: Media Object
Phần này nối mạch bài học với “38. Flex pattern: Media Object”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="flex gap-4">
  <img
    class="
      size-12
      shrink-0
      rounded-full
      object-cover
    "
  >

  <div class="min-w-0 flex-1">
    <h3 class="truncate font-semibold">
      User name
    </h3>

    <p class="text-sm text-gray-600">
      Description
    </p>
  </div>
</div>
```

Đây là mẫu (pattern / 패턴) avatar/media + content kinh điển. `shrink-0` bảo vệ media, `min-w-0 flex-1` làm body linh hoạt.

---

# PHẦN IV — CSS GRID TRONG TAILWIND

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **39. Grid khác Flexbox ở đâu?** tiếp nhận điểm tựa từ **38. Flex pattern: Media Object** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. grid-cols- và minmax(0,1fr)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Grid khác Flexbox ở đâu?

Flexbox mạnh khi bạn nghĩ theo một trục chính: row hoặc column. Grid mạnh khi bạn cần kiểm soát hàng và cột như một hệ thống.

Bật Grid:

```html
<div class="grid">
```

Sau đó:

```text
grid-cols-1
grid-cols-2
grid-cols-3
...
grid-cols-12
```

định nghĩa số cột bằng equal fractional tracks.

Ví dụ card bố cục (layout / 레이아웃):

```html
<div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
```

Cơ sở (base / 기반) một cột, md hai cột, lg ba cột.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **40. grid-cols- và minmax(0,1fr)** tiếp nhận điểm tựa từ **39. Grid khác Flexbox ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Arbitrary grid template** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. `grid-cols-*` và `minmax(0,1fr)`

Tailwind equal grid column các tiện ích (utilities) thường dùng nhánh học (track / 트랙) kiểu `minmax(0, 1fr)` thay vì plain `1fr`.

Điều này quan trọng vì phần tử Grid (grid item) có intrinsic minimum kích thước (size / 크기). `minmax(0,1fr)` cho nhánh học (track / 트랙) permission co xuống 0 minimum, giúp giảm overflow do content dài.

Đây là tư duy tương tự `min-w-0` trong Flexbox.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **41. Arbitrary grid template** tiếp nhận điểm tựa từ **40. grid-cols- và minmax(0,1fr)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. col-span-, col-start-, col-end-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Arbitrary grid template

Dashboard:

```html
<div
  class="
    grid
    grid-cols-[16rem_minmax(0,1fr)]
    gap-6
  "
>
  <aside>...</aside>
  <main class="min-w-0">...</main>
</div>
```

Tailwind `_` trong giá trị tùy ý (arbitrary value) trở thành whitespace, nên CSS tương đương:

```css
grid-template-columns:
  16rem minmax(0, 1fr);
```

Arbitrary grid template là một trong những giá trị tùy ý (arbitrary value) use cases tốt nhất vì bố cục (layout / 레이아웃) template thường mang tính cấu trúc (structure / 구조) hơn design-token quy mô (scale / 규모).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **42. col-span-, col-start-, col-end-** tiếp nhận điểm tựa từ **41. Arbitrary grid template** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Grid rows và row placement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. `col-span-*`, `col-start-*`, `col-end-*`

Nếu grid có 12 cột:

```html
<div class="grid grid-cols-12">
  <aside class="col-span-3">
  <main class="col-span-9">
</div>
```

`col-span-3` nói item span ba tracks. Bạn cũng có thể đặt line trực tiếp:

```text
col-start-2
col-end-6
```

`col-span-full` thường span từ first tới last tường minh (explicit / 명시적) grid line.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **43. Grid rows và row placement** tiếp nhận điểm tựa từ **42. col-span-, col-start-, col-end-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Auto-placement và grid-flow-dense** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Grid rows và row placement

Tương tự columns:

```text
grid-rows-3
row-span-2
row-start-1
row-end-3
```

Use khi bố cục (layout / 레이아웃) thật sự cần row tracks rõ ràng. Nếu content height tự nhiên, không nên ép rows chỉ vì có tiện ích (utility).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **43. Grid rows và row placement** xác định đầu vào; **44. Auto-placement và grid-flow-dense** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **45. Subgrid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Auto-placement và `grid-flow-dense`

Tailwind có:

```text
grid-flow-row
grid-flow-col
grid-flow-dense
```

`dense` cho trình duyệt (browser / 브라우저) backfill holes trong grid. Nó có thể làm **visual thứ tự (order / 순서) khác DOM thứ tự (order / 순서)**.

Vì screen reader/focus điều hướng (navigation / 내비게이션) thường dựa trên DOM thứ tự (order / 순서), hãy cẩn thận dùng dense cho interactive content. Decorative gallery có thể ổn; form hoặc điều hướng (navigation / 내비게이션) có thể gây confusion.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **44. Auto-placement và grid-flow-dense** xác định đầu vào; **45. Subgrid** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **46. Intrinsic auto grid không cần điểm ngắt (breakpoint)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Subgrid
Phần này nối mạch bài học với “45. Subgrid”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="grid-cols-subgrid">
```

map khóa–giá trị (map) tới:

```css
grid-template-columns: subgrid;
```

Subgrid cho child grid reuse tracks của parent thay vì tự tạo một hệ cột độc lập.

Use khi nhiều cards cần:
- title,
- body,
- hành động (action / 동작)
align theo dùng chung (shared / 공유) tracks.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **46. Intrinsic auto grid không cần điểm ngắt (breakpoint)** tiếp nhận điểm tựa từ **45. Subgrid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Font family** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Intrinsic auto grid không cần điểm ngắt (breakpoint)

Một advanced mẫu (pattern / 패턴):

```html
<div
  class="
    grid
    grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]
    gap-6
  "
>
```

Ý nghĩa CSS: trình duyệt (browser / 브라우저) tự fit nhiều cột nhất có thể, mỗi cột tối thiểu khoảng 18rem nhưng không rộng hơn bộ chứa (container / 컨테이너) ở mobile.

Điểm quan trọng: responsive không nhất thiết phải luôn `sm:`, `md:`, `lg:`. CSS bố cục nội tại (intrinsic layout) đôi khi responsive tự nhiên hơn điểm ngắt (breakpoint).

---

# PHẦN V — TYPOGRAPHY

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **47. Font family** tiếp nhận điểm tựa từ **46. Intrinsic auto grid không cần điểm ngắt (breakpoint)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Font kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Font family

Tailwind default families:

```text
font-sans
font-serif
font-mono
```

Chúng lấy giá trị (value / 값) từ các biến chủ đề (theme variables) như `--font-sans`.

Custom:

```css
@theme {
  --font-brand:
    "Pretendard",
    "Noto Sans KR",
    sans-serif;
}
```

Use:

```html
<body class="font-brand">
```

Đừng chỉ nghĩ font family là tên font. phương án dự phòng (fallback) chuỗi (chain / 사슬) rất quan trọng khi webfont chưa tải (load / 로드) hoặc glyph ngôn ngữ không có trong font đầu tiên.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **48. Font kích thước (size / 크기)** tiếp nhận điểm tựa từ **47. Font family** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Font weight** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Font kích thước (size / 크기)

Các tiện ích (utility):

```text
text-xs
text-sm
text-base
text-lg
text-xl
text-2xl
...
text-9xl
```

lấy từ theme kiểu (type / 타입) quy mô (scale / 규모).

Arbitrary:

```text
text-[17px]
```

nhưng nếu 17px là body tiêu chuẩn (standard / 표준) của sản phẩm (product / 제품), hãy thêm đơn vị từ (token / 토큰) thay vì arbitrary ở mọi nơi.

Tailwind hỗ trợ compact cú pháp (syntax / 문법) cho line-height:

```text
text-lg/7
```

nghĩa là font-size `text-lg` với leading giá trị (value / 값) tương ứng `7`.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **49. Font weight** tiếp nhận điểm tựa từ **48. Font kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Line height** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Font weight
Phần này nối mạch bài học với “49. Font weight”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
font-thin
font-light
font-normal
font-medium
font-semibold
font-bold
font-extrabold
font-black
```

Arbitrary:

```text
font-[650]
```

rất hữu ích với biến (variable) fonts hỗ trợ intermediate weights.

Không phải font nào cũng có thực glyph ở mọi weight. trình duyệt (browser / 브라우저) có thể synthesize weight nếu tệp (file / 파일)/font không hỗ trợ (support / 지원), nên hệ thống thiết kế (design system) cần tải (load / 로드) font các biến thể (variants) đúng.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **50. Line height** tiếp nhận điểm tựa từ **49. Font weight** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Letter spacing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Line height
Phần này nối mạch bài học với “50. Line height”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
leading-none
leading-tight
leading-snug
leading-normal
leading-relaxed
leading-loose
leading-6
leading-[1.65]
```

Line-height ảnh hưởng khoảng cách hộp dòng (line box), không phải margin giữa paragraphs.

Heading thường cần tighter leading; body văn bản (text / 텍스트) thường cần rộng hơn.

Ví dụ:

```html
<h1 class="text-4xl font-bold leading-tight">
```

và:

```html
<p class="text-base leading-relaxed">
```

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **51. Letter spacing** tiếp nhận điểm tựa từ **50. Line height** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Text alignment và logical alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Letter spacing
Phần này nối mạch bài học với “51. Letter spacing”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
tracking-tighter
tracking-tight
tracking-normal
tracking-wide
tracking-wider
tracking-widest
```

Large display heading đôi khi đẹp hơn với tracking hơi âm, uppercase label đôi khi cần tracking dương.

Đừng áp `tracking-wide` toàn cục (global / 전역) chỉ vì “trông thoáng”; Korean, English và font khác nhau có visual density khác nhau.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **52. Text alignment và logical alignment** tiếp nhận điểm tựa từ **51. Letter spacing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. White-space và văn bản (text / 텍스트) wrapping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Text alignment và logical alignment
Phần này nối mạch bài học với “52. Text alignment và logical alignment”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
text-left
text-center
text-right
text-justify
text-start
text-end
```

`text-start`/`text-end` phù hợp international UI hơn left/right khi alignment mang ý nghĩa theo reading direction.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **53. White-space và văn bản (text / 텍스트) wrapping** tiếp nhận điểm tựa từ **52. Text alignment và logical alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. truncate: hiểu đầy đủ ba điều kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. White-space và văn bản (text / 텍스트) wrapping

các tiện ích (utilities) quan trọng:

```text
whitespace-normal
whitespace-nowrap
whitespace-pre
whitespace-pre-line
whitespace-pre-wrap
```

`whitespace-nowrap` thường đi với single-line điều khiển (control / 제어)/ellipsis.

`whitespace-pre-wrap` phù hợp user-generated văn bản (text / 텍스트) cần giữ newline/không gian (space / 공간) nhưng vẫn wrap.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **54. truncate: hiểu đầy đủ ba điều kiện** tiếp nhận điểm tựa từ **53. White-space và văn bản (text / 텍스트) wrapping** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. Multi-line clamp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. `truncate`: hiểu đầy đủ ba điều kiện

Tailwind `truncate` là bundle gần:

```css
overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;
```

Nhưng nó chỉ hoạt động khi element có width ràng buộc (constraint / 제약조건) thực tế. Trong flex bố cục (layout / 레이아웃), bạn thường còn cần `min-w-0`.

Mẫu (pattern / 패턴):

```html
<div class="min-w-0 flex-1">
  <p class="truncate">
    ...
  </p>
</div>
```

Nếu văn bản (text / 텍스트) vẫn không ellipsis, kiểm tra sizing ngữ cảnh (context / 맥락) thay vì thêm nhiều `overflow-hidden`.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **55. Multi-line clamp** tiếp nhận điểm tựa từ **54. truncate: hiểu đầy đủ ba điều kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. Word breaking và Korean/CJK** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Multi-line clamp
Phần này nối mạch bài học với “55. Multi-line clamp”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<p class="line-clamp-3">
  ...
</p>
```

giới hạn nội dung theo số dòng.

Dùng tốt cho:
- card preview,
- tìm kiếm (search / 검색) kết quả (result / 결과) summary,
- feed snippet.

Không dùng để giấu phần nội dung người dùng (user / 사용자) bắt buộc phải đọc mà không có “Show more”.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **56. Word breaking và Korean/CJK** tiếp nhận điểm tựa từ **55. Multi-line clamp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. text-balance và text-pretty** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. Word breaking và Korean/CJK

Tailwind có các các tiện ích (utilities) liên quan:

```text
break-normal
break-words
break-all
break-keep
```

`break-keep` map khóa–giá trị (map) tới hành vi (behavior / 동작) `word-break: keep-all` và thường hữu ích cho Korean/CJK khi bạn muốn tránh break giữa characters như `break-all`.

Ví dụ:

```html
<p class="break-keep text-pretty">
  한국어로 긴 문장을 표시합니다...
</p>
```

Nhưng văn bản (text / 텍스트) rất dài không có không gian (space / 공간) như URL vẫn cần overflow chiến lược (strategy / 전략). Hãy kiểm thử (test / 테스트) content thật thay vì áp một quy tắc (rule / 규칙) toàn cục (global / 전역) cho mọi ngôn ngữ.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **57. text-balance và text-pretty** tiếp nhận điểm tựa từ **56. Word breaking và Korean/CJK** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. văn bản (text / 텍스트) decoration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. `text-balance` và `text-pretty`

`text-balance` map khóa–giá trị (map) tới hiện đại (modern / 현대적) `text-wrap: balance`, hữu ích cho headings ngắn nhiều dòng vì trình duyệt (browser / 브라우저) cố cân độ dài các dòng.

```html
<h1 class="text-balance text-5xl font-bold">
```

`text-pretty` hướng tới line breaking đẹp hơn, thường phù hợp paragraph.

Đây là cải tiến lũy tiến (progressive enhancement); mức hỗ trợ trình duyệt (browser support / 브라우저 지원) mục tiêu (target / 대상) vẫn cần được xem xét nếu sản phẩm (product / 제품) hỗ trợ trình duyệt (browser / 브라우저) cũ.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **58. văn bản (text / 텍스트) decoration** tiếp nhận điểm tựa từ **57. text-balance và text-pretty** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. Text transform** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. văn bản (text / 텍스트) decoration

Tailwind cung cấp các tiện ích (utilities) cho:
- underline,
- overline,
- line-through,
- decoration color,
- thickness,
- underline offset,
- decoration style.

Ví dụ link:

```html
<a
  class="
    underline
    decoration-blue-400
    decoration-2
    underline-offset-4
    hover:decoration-blue-600
  "
>
```

Văn bản (text / 텍스트) decoration tốt cho link khả năng tiếp cận (accessibility / 접근성) hơn việc chỉ đổi màu khi link cần nhận biết rõ.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **59. Text transform** tiếp nhận điểm tựa từ **58. văn bản (text / 텍스트) decoration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. OpenType numeric features** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. Text transform
Phần này nối mạch bài học với “59. Text transform”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
uppercase
lowercase
capitalize
normal-case
```

đây là visual transform. nguồn (source / 소스) văn bản (text / 텍스트)/accessible name vẫn có ngữ nghĩa (semantics / 의미론) riêng.

Nếu acronym cần uppercase vì nội dung thật sự là acronym, tốt hơn nguồn (source / 소스) cũng đúng thay vì dựa hoàn toàn vào CSS transform.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **60. OpenType numeric features** tiếp nhận điểm tựa từ **59. Text transform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **61. Color hệ thống (system / 시스템) và palette** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. OpenType numeric features
Phần này nối mạch bài học với “60. OpenType numeric features”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
tabular-nums
lining-nums
oldstyle-nums
slashed-zero
```

`tabular-nums` cực hữu ích cho:
- financial dashboard,
- bảng (table / 테이블),
- countdown,
- metrics
vì mỗi chữ số có cùng advance width, giúp số không “nhảy” khi thay đổi.

V4.2+ có `font-features-*` cho low-level `font-feature-settings`, nhưng hãy ưu tiên high-level tiện ích (utility) nếu có mang tính ngữ nghĩa (semantic / 의미적) equivalent.

---

# PHẦN VI — COLOR, BACKGROUND, BORDER, SHADOW

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **61. Color hệ thống (system / 시스템) và palette** tiếp nhận điểm tựa từ **60. OpenType numeric features** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **62. Alpha modifier /** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 61. Color hệ thống (system / 시스템) và palette

Tailwind v4 dùng hiện đại (modern / 현대적) color hệ thống (system / 시스템) với palette rộng. hiện tại (current / 현재) bản phát hành (release / 릴리스) có các neutral families như:

```text
slate
gray
zinc
neutral
stone
mauve
olive
mist
taupe
```

và chromatic families như red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose.

Quy mô (scale / 규모) thường chạy từ `50` sáng tới `950` tối.

Ví dụ:

```text
bg-blue-600
text-gray-900
border-gray-200
```

Nhưng numeric shade không có mang tính ý nghĩa (semantic meaning / 의미적 뜻) nghiệp vụ (business / 비즈니스). Một hệ thống thiết kế (design system) lớn nên bổ sung mang tính ngữ nghĩa (semantic / 의미적) tokens như hành động (action / 동작), surface, danger thay vì để mọi thành phần (component / 컴포넌트) tự chọn palette.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **62. Alpha modifier /** tiếp nhận điểm tựa từ **61. Color hệ thống (system / 시스템) và palette** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **63. Background** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 62. Alpha modifier `/`
Phần này nối mạch bài học với “62. Alpha modifier `/`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="bg-blue-600/50">
```

nghĩa là background blue-600 với alpha 50%.

Tương tự:

```text
text-black/70
border-gray-900/10
shadow-black/20
```

Arbitrary:

```text
bg-pink-500/[71.37%]
```

Alpha modifier giúp tránh cần tạo riêng hàng loạt opacity color đơn vị từ (token / 토큰).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **63. Background** tiếp nhận điểm tựa từ **62. Alpha modifier /** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **64. độ dốc (gradient / 기울기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 63. Background

Ngoài color:

```text
bg-cover
bg-contain
bg-center
bg-top
bg-no-repeat
bg-repeat
bg-fixed
```

map khóa–giá trị (map) tới background-size, background-position, background-repeat và attachment.

Ảnh hero:

```html
<section
  class="
    bg-cover
    bg-center
    bg-no-repeat
  "
>
```

Nếu background ảnh (image / 이미지) URL là one-off:

```html
<div class="bg-[url('/images/hero.webp')]">
```

Nhưng với động (dynamic / 동적) URL từ API, inline style/CSS biến (variable) có thể thích hợp hơn source-generated arbitrary lớp (class / 클래스).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **64. độ dốc (gradient / 기울기)** tiếp nhận điểm tựa từ **63. Background** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **65. Border width, style và color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 64. độ dốc (gradient / 기울기)

Tailwind hỗ trợ độ dốc (gradient / 기울기) các tiện ích (utilities) và độ dốc (gradient / 기울기) color stops. Tư duy quan trọng không phải thuộc mọi tên lớp (class / 클래스) mà hiểu:
- độ dốc (gradient / 기울기) là `background-image`,
- direction/shape là hàm (function / 함수) argument,
- from/via/to xác định color stops.

Một độ dốc (gradient / 기울기) UI nên dùng đơn vị từ (token / 토큰)/mang tính ngữ nghĩa (semantic / 의미적) colors nếu là part của brand hệ thống (system / 시스템), không hard-code arbitrary color khắp thành phần (component / 컴포넌트).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **65. Border width, style và color** tiếp nhận điểm tựa từ **64. độ dốc (gradient / 기울기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **66. Border radius** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 65. Border width, style và color

Ví dụ:

```html
<div class="border border-gray-200">
```

`border` đặt default border width; `border-gray-200` đặt color.

Có directional các tiện ích (utilities):

```text
border-t
border-b
border-x
border-y
```

và logical v4 các tiện ích (utilities) như block-start/end trong relevant naming families.

Styles:

```text
border-solid
border-dashed
border-dotted
border-double
border-none
```

Divider nên đặt ở parent với `divide-*` nếu mục tiêu là separator giữa children, thay vì mỗi child tự thêm border rồi xử lý `last:`.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **66. Border radius** tiếp nhận điểm tựa từ **65. Border width, style và color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **67. Outline và focus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 66. Border radius
Phần này nối mạch bài học với “66. Border radius”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
rounded-none
rounded-sm
rounded
rounded-md
rounded-lg
rounded-xl
rounded-2xl
rounded-3xl
rounded-full
```

`rounded-full` tạo cực lớn radius, thường dùng pill hoặc circle nếu width/height bằng nhau.

Có directional/logical corner các tiện ích (utilities). Khi app cần RTL, tránh chỉ suy nghĩ `rounded-l-*`/`rounded-r-*` nếu ý nghĩa là start/end.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **67. Outline và focus** tiếp nhận điểm tựa từ **66. Border radius** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **68. Ring các tiện ích (utilities)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 67. Outline và focus

Accessible focus mẫu (pattern / 패턴):

```html
<button
  class="
    focus-visible:outline-2
    focus-visible:outline-offset-2
    focus-visible:outline-blue-600
  "
>
```

`focus-visible` khác `focus`: trình duyệt (browser / 브라우저) cố chỉ hiển thị focus treatment khi đầu vào (input / 입력) modality phù hợp, ví dụ keyboard điều hướng (navigation / 내비게이션), thay vì mọi mouse click.

Không viết:

```text
outline-none
```

mà không có replacement chỉ báo tiêu điểm (focus indicator). Làm mất focus visible là khả năng tiếp cận (accessibility / 접근성) regression.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **68. Ring các tiện ích (utilities)** tiếp nhận điểm tựa từ **67. Outline và focus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **69. Box shadow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 68. Ring các tiện ích (utilities)

Tailwind có `ring-*`, nhưng CSS không có thuộc tính (property / 속성) tên `ring`. Tailwind implement ring bằng shadow/custom các thuộc tính (properties).

Ví dụ:

```html
<div class="ring-1 ring-black/10">
```

Card subtle border-like tác động (effect / 효과) rất đẹp bằng ring.

Focus có thể dùng ring:

```html
<input class="focus:ring-2 focus:ring-blue-500/30">
```

Nhưng outline có lợi thế mang tính ngữ nghĩa (semantic / 의미적)/direct và không bị box-shadow composition ảnh hưởng giống ring. cấp cao (senior / 시니어) chọn theo thiết kế (design / 설계)/tương tác (interaction / 상호작용) ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **69. Box shadow** tiếp nhận điểm tựa từ **68. Ring các tiện ích (utilities)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **70. văn bản (text / 텍스트) shadow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 69. Box shadow
Phần này nối mạch bài học với “69. Box shadow”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
shadow-xs
shadow-sm
shadow-md
shadow-lg
shadow-xl
shadow-2xl
shadow-none
```

Shadow mô tả elevation hoặc visual separation. Đừng dùng càng lớn càng “premium”. Một hệ thống thiết kế (design system) nên có elevation quy mô (scale / 규모) rõ.

Tint:

```text
shadow-black/10
shadow-blue-500/20
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **70. văn bản (text / 텍스트) shadow** tiếp nhận điểm tựa từ **69. Box shadow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **71. Opacity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 70. văn bản (text / 텍스트) shadow

Hiện tại (current / 현재) Tailwind v4 có text-shadow tiện ích (utility) family. Nó map khóa–giá trị (map) trực tiếp tới CSS `text-shadow`.

Use:
- decorative display văn bản (text / 텍스트),
- văn bản (text / 텍스트) trên ảnh khó đọc.

Không dùng heavy văn bản (text / 텍스트) shadow cho body văn bản (text / 텍스트) vì giảm readability.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **71. Opacity** tiếp nhận điểm tựa từ **70. văn bản (text / 텍스트) shadow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **72. Blend và cô lập (isolation)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 71. Opacity
Phần này nối mạch bài học với “71. Opacity”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
opacity-0
opacity-50
opacity-100
```

`opacity` áp cho toàn rendered subtree, không chỉ background.

Nếu bạn muốn background trong suốt mà văn bản (text / 텍스트) vẫn opaque:

```text
bg-white/50
```

tốt hơn:

```text
opacity-50
```

trên bộ chứa (container / 컨테이너).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **72. Blend và cô lập (isolation)** tiếp nhận điểm tựa từ **71. Opacity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **73. Filters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 72. Blend và cô lập (isolation)

Tailwind có `mix-blend-*`, `bg-blend-*`, `isolate`.

`mix-blend-mode` cho element blend với backdrop. `isolation:isolate` tạo cô lập (isolation) ngữ cảnh (context / 맥락) để giới hạn blending/stacking hành vi (behavior / 동작).

Đây là advanced visual công cụ (tool / 도구), không phải normal bố cục (layout / 레이아웃) cơ chế (mechanism / 메커니즘).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **73. Filters** tiếp nhận điểm tựa từ **72. Blend và cô lập (isolation)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **74. Backdrop filter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 73. Filters

Dùng chung (common / 공통):

```text
blur-*
brightness-*
contrast-*
grayscale
hue-rotate-*
invert
saturate-*
sepia
drop-shadow-*
```

`drop-shadow` là filter dựa trên alpha shape của rendered element, khác `box-shadow` luôn dựa box.

Hiệu năng (performance / 성능) của filter lớn, đặc biệt blur trên vùng rộng/animate liên tục, có thể đáng kể. kiểm thử (test / 테스트) bằng DevTools thay vì assume.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **74. Backdrop filter** tiếp nhận điểm tựa từ **73. Filters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **75. Mask các tiện ích (utilities)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 74. Backdrop filter

Glass UI:

```html
<div
  class="
    bg-white/70
    backdrop-blur-xl
    ring-1
    ring-black/5
  "
>
```

`backdrop-blur-*` blur nội dung **phía sau** element, không phải element itself.

Backdrop filter có thể tốn kết xuất (render / 렌더링) chi phí (cost / 비용), đặc biệt trên vùng full-screen hoặc mobile. Use có chọn lọc.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **75. Mask các tiện ích (utilities)** tiếp nhận điểm tựa từ **74. Backdrop filter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **76. aspect-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 75. Mask các tiện ích (utilities)

Mask kiểm soát transparency bằng ảnh (image / 이미지)/độ dốc (gradient / 기울기)/luminance. Nó khác `clip-path`: clip thường quyết định vùng visible cứng hơn, mask cho phép alpha độ dốc (gradient / 기울기).

Tailwind hiện tại (current / 현재) docs có tiện ích (utility) families cho:
- mask ảnh (image / 이미지),
- kích thước (size / 크기),
- position,
- repeat,
- origin,
- clip,
- chế độ (mode / 모드),
- composite,
- kiểu (type / 타입).

Nếu một option hiếm không có named tiện ích (utility) bạn nhớ, thuộc tính tùy ý (arbitrary property):

```html
<div class="[mask-type:luminance]">
```

là cách hợp lệ.

---

# PHẦN VII — IMAGES, SVG, TABLES VÀ CONTENT

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **76. aspect-** tiếp nhận điểm tựa từ **75. Mask các tiện ích (utilities)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **77. object-cover và object-contain** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 76. `aspect-*`
Phần này nối mạch bài học với “76. `aspect-*`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
aspect-square
aspect-video
aspect-3/2
aspect-[4/3]
aspect-auto
```

map khóa–giá trị (map) tới `aspect-ratio`.

Avatar:

```html
<img
  class="
    aspect-square
    w-16
    rounded-full
    object-cover
  "
>
```

Aspect ratio reserve shape của box; `object-cover` quyết định tài nguyên (resource / 자원) bên trong fit/crop như thế nào.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **77. object-cover và object-contain** tiếp nhận điểm tựa từ **76. aspect-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **78. size-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 77. `object-cover` và `object-contain`

Ảnh 4:3 đặt trong box 1:1.

`object-cover` phóng tài nguyên (resource / 자원) đủ để phủ toàn box và crop phần dư.

`object-contain` thu/phóng để toàn tài nguyên (resource / 자원) nhìn thấy, có thể để khoảng trống.

```html
<img class="size-20 object-cover">
```

rất phù hợp thumbnail.

Focal điểm (point / 지점):

```text
object-top
object-center
object-[50%_20%]
```

giúp kiểm soát vùng crop.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **78. size-** tiếp nhận điểm tựa từ **77. object-cover và object-contain** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **79. SVG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 78. `size-*`
Phần này nối mạch bài học với “78. `size-*`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="size-10">
```

là shorthand width + height cùng giá trị (value / 값).

Use cực nhiều cho:
- avatar,
- icon button,
- square placeholder.

Nó không thay `aspect-square` hoàn toàn: `size-*` đặt cả hai dimension; `aspect-square` chỉ giữ ratio khi một dimension được quyết định bởi ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **79. SVG** tiếp nhận điểm tựa từ **78. size-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **80. Tables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 79. SVG

Một icon inline SVG thường:

```html
<svg
  class="size-5 text-blue-600"
  fill="currentColor"
>
```

`currentColor` làm fill follow CSS `color`.

Tailwind cũng có:

```text
fill-current
fill-blue-600
fill-none
stroke-current
stroke-blue-600
stroke-1
stroke-2
```

Inline SVG style được bởi CSS. SVG dùng qua `<img src="icon.svg">` là replaced tài nguyên (resource / 자원) và nội bộ (internal / 내부) SVG không được biểu định kiểu (stylesheet / 스타일시트) document mục tiêu (target / 대상) giống inline SVG.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **80. Tables** tiếp nhận điểm tựa từ **79. SVG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **81. Multi-column và fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 80. Tables

Wrapper responsive:

```html
<div class="overflow-x-auto">
  <table class="min-w-full table-auto">
```

`table-auto` dùng content-sensitive bảng (table / 테이블) bố cục (layout / 레이아웃). `table-fixed` cho column sizing predictable hơn khi bảng (table / 테이블) width đã constrained.

`border-collapse` merge adjacent borders; `border-separate` giữ separate border mô hình (model / 모델) và có thể dùng `border-spacing-*`.

Dữ liệu (data / 데이터) bảng (table / 테이블) lớn nên ưu tiên mang tính ngữ nghĩa (semantic / 의미적) `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>` thay vì recreate bằng div chỉ để styling dễ.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **81. Multi-column và fragmentation** tiếp nhận điểm tựa từ **80. Tables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **82. Translate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 81. Multi-column và fragmentation

Tailwind có `columns-*` cho CSS multi-column bố cục (layout / 레이아웃). Đây không phải Grid columns. trình duyệt (browser / 브라우저) luồng (flow / 흐름) văn bản (text / 텍스트)/content từ cột này sang cột tiếp theo.

Fragmentation các tiện ích (utilities) như:

```text
break-inside-avoid
break-before-page
break-after-page
```

hữu ích cho print/editorial bố cục (layout / 레이아웃).

---

# PHẦN VIII — TRANSFORM, chuyển tiếp (transition / 전이), ANIMATION

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **82. Translate** tiếp nhận điểm tựa từ **81. Multi-column và fragmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **83. Scale, rotate, skew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 82. Translate
Phần này nối mạch bài học với “82. Translate”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
translate-x-4
translate-y-2
-translate-x-1/2
-translate-y-1/2
```

Classic absolute center:

```html
<div
  class="
    absolute
    left-1/2
    top-1/2
    -translate-x-1/2
    -translate-y-1/2
  "
>
```

Ở đây `left-1/2 top-1/2` đặt top-left điểm (point / 지점) vào center parent, còn negative translate 50% own kích thước (size / 크기) kéo element về center thật.

Nếu chỉ cần center normal bố cục (layout / 레이아웃), Grid:

```text
grid place-items-center
```

thường đơn giản hơn.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **83. Scale, rotate, skew** tiếp nhận điểm tựa từ **82. Translate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **84. Transform origin, perspective và 3D** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 83. Scale, rotate, skew
Phần này nối mạch bài học với “83. Scale, rotate, skew”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
scale-95
scale-100
scale-105
rotate-45
-rotate-6
skew-x-6
```

Transform không giống bố cục (layout / 레이아웃) sizing. quy mô (scale / 규모) làm rendered element to/nhỏ nhưng normal bố cục (layout / 레이아웃) không gian (space / 공간) ban đầu thường không được reflow giống width/height.

Hover microinteraction:

```html
<button
  class="
    transition-transform
    hover:scale-105
  "
>
```

Nên respect giảm chuyển động (reduced motion) nếu movement đáng kể.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **84. Transform origin, perspective và 3D** tiếp nhận điểm tựa từ **83. Scale, rotate, skew** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **85. zoom- trong v4.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 84. Transform origin, perspective và 3D

các tiện ích (utilities):

```text
origin-center
origin-top-left
perspective-*
perspective-origin-*
transform-3d
transform-flat
backface-hidden
```

3D transform nên dùng cho purposeful tương tác (interaction / 상호작용) như flip card, carousel hoặc visual editor. Đây không phải thứ cần rải khắp normal form/dashboard.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **85. zoom- trong v4.3** tiếp nhận điểm tựa từ **84. Transform origin, perspective và 3D** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **86. chuyển tiếp (transition / 전이) thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 85. `zoom-*` trong v4.3

Tailwind v4.3 có:

```text
zoom-75
zoom-100
zoom-125
zoom-[1.1]
zoom-(--preview-zoom)
```

map khóa–giá trị (map) tới CSS `zoom`.

`zoom` khác `transform: scale()` vì zoom ảnh hưởng bố cục (layout / 레이아웃) metrics theo cách khác. Một document preview có thể hợp lý:

```html
<div class="zoom-(--preview-scale)">
```

Nhưng responsive app không nên dùng zoom để “thu nhỏ desktop UI cho mobile”.

CSS `zoom` cũng không phải trình duyệt (browser / 브라우저) người dùng (user / 사용자) zoom. Không bao giờ cố chống lại người dùng (user / 사용자) zoom vì khả năng tiếp cận (accessibility / 접근성).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **86. chuyển tiếp (transition / 전이) thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **85. zoom- trong v4.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **87. Duration, delay và easing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 86. chuyển tiếp (transition / 전이) thuộc tính (property / 속성)

Tailwind có:

```text
transition
transition-all
transition-colors
transition-opacity
transition-shadow
transition-transform
transition-none
```

`transition-all` tiện nhưng quá rộng. Nếu width, top, filter hoặc expensive thuộc tính (property / 속성) vô tình thay đổi, tất cả đều animate.

Cấp cao (senior / 시니어) thường chọn mục tiêu (target / 대상) rõ:

```html
<button
  class="
    transition-colors
    duration-150
    ease-out
  "
>
```

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **87. Duration, delay và easing** tiếp nhận điểm tựa từ **86. chuyển tiếp (transition / 전이) thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **88. Built-in animations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 87. Duration, delay và easing
Phần này nối mạch bài học với “87. Duration, delay và easing”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
duration-75
duration-150
duration-300
delay-75
ease-linear
ease-in
ease-out
ease-in-out
```

Microinteraction UI thường ở khoảng nhanh. Modal/page chuyển tiếp (transition / 전이) có thể dài hơn.

Không có “thời lượng chuẩn Tailwind” cho mọi UX. thiết kế (design / 설계) motion hệ thống (system / 시스템) nên consistent.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **88. Built-in animations** tiếp nhận điểm tựa từ **87. Duration, delay và easing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **89. Custom animation bằng @theme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 88. Built-in animations

Dùng chung (common / 공통):

```text
animate-spin
animate-ping
animate-pulse
animate-bounce
animate-none
```

Loading spinner:

```html
<svg class="animate-spin">
```

Skeleton:

```html
<div class="animate-pulse">
  ...
</div>
```

Không phải animation nào cũng phải vòng lặp (loop / 루프). Animation nên communicate trạng thái (state / 상태), không chỉ trang trí.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **89. Custom animation bằng @theme** tiếp nhận điểm tựa từ **88. Built-in animations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **90. giảm chuyển động (reduced motion)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 89. Custom animation bằng `@theme`
Phần này nối mạch bài học với “89. Custom animation bằng `@theme`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@theme {
  --animate-fade-in:
    fade-in 180ms ease-out;

  @keyframes fade-in {
    from {
      opacity: 0;
      transform: translateY(.25rem);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
}
```

Use:

```html
<div class="animate-fade-in">
```

Theme đơn vị từ (token / 토큰) cho animation biến animation name/giá trị (value / 값) thành reusable tiện ích (utility) API.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **90. giảm chuyển động (reduced motion)** tiếp nhận điểm tựa từ **89. Custom animation bằng @theme** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **91. Cursor không tạo ngữ nghĩa (semantics)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 90. giảm chuyển động (reduced motion)
Phần này nối mạch bài học với “90. giảm chuyển động (reduced motion)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  class="
    transition-transform
    hover:scale-105
    motion-reduce:transition-none
    motion-reduce:hover:scale-100
  "
>
```

`motion-reduce:` map khóa–giá trị (map) tới truy vấn môi trường (media query) `prefers-reduced-motion: reduce`.

Nếu motion chỉ là decoration, giảm/tắt nó cho người dùng đã yêu cầu giảm chuyển động (reduced motion).

---

# PHẦN IX — FORMS VÀ tương tác (interaction / 상호작용)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **91. Cursor không tạo ngữ nghĩa (semantics)** tiếp nhận điểm tựa từ **90. giảm chuyển động (reduced motion)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **92. Pointer events** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 91. Cursor không tạo ngữ nghĩa (semantics)
Phần này nối mạch bài học với “91. Cursor không tạo ngữ nghĩa (semantics)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
cursor-pointer
cursor-default
cursor-not-allowed
```

chỉ đổi mouse cursor.

Sai:

```html
<div class="cursor-pointer">
  Submit
</div>
```

nếu nó thật sự là button.

Đúng:

```html
<button class="cursor-pointer">
  Submit
</button>
```

mang tính ngữ nghĩa (semantic / 의미적) HTML mang keyboard hành vi (behavior / 동작), khả năng tiếp cận (accessibility / 접근성) role và form ngữ nghĩa (semantics / 의미론) mà lớp (class / 클래스) không tạo được.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **92. Pointer events** tiếp nhận điểm tựa từ **91. Cursor không tạo ngữ nghĩa (semantics)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **93. User select** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 92. Pointer events
Phần này nối mạch bài học với “92. Pointer events”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
pointer-events-none
pointer-events-auto
```

`pointer-events-none` khiến element không nhận pointer targeting.

Nó không phải mang tính ngữ nghĩa (semantic / 의미적) disabled. Một button disabled nên có:

```html
<button
  disabled
  class="
    disabled:cursor-not-allowed
    disabled:opacity-50
  "
>
```

`disabled` attribute quyết định hành vi (behavior / 동작); Tailwind chỉ style trạng thái (state / 상태) đó.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **93. User select** tiếp nhận điểm tựa từ **92. Pointer events** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **94. Appearance và native controls** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 93. User select
Phần này nối mạch bài học với “93. User select”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
select-none
select-text
select-all
select-auto
```

`select-none` hợp lý cho drag handle/icon điều khiển (control / 제어). Không disable selection toàn page vì người dùng (user / 사용자) có thể cần bản sao (copy / 복사) văn bản (text / 텍스트).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **94. Appearance và native controls** tiếp nhận điểm tựa từ **93. User select** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **95. accent-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 94. Appearance và native controls
Phần này nối mạch bài học với “94. Appearance và native controls”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
appearance-none
appearance-auto
```

`appearance-none` loại bỏ bản địa (native / 네이티브) skin của form điều khiển (control / 제어). Khi làm vậy, bạn nhận trách nhiệm style:
- focus,
- checked,
- disabled,
- màu cưỡng bức (forced colors),
- hover,
- high-contrast.

Đừng custom bản địa (native / 네이티브) controls sâu chỉ vì có thể.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **95. accent-** tiếp nhận điểm tựa từ **94. Appearance và native controls** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **96. trường dữ liệu (field / 필드) sizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 95. `accent-*`
Phần này nối mạch bài học với “95. `accent-*`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="checkbox"
  class="accent-blue-600"
>
```

`accent-color` là cách rất hiệu quả để theme checkbox/radio/phạm vi (range / 범위) bản địa (native / 네이티브) mà vẫn giữ bản địa (native / 네이티브) hành vi (behavior / 동작).

Nhiều trường hợp (case / 사례) không cần recreate checkbox bằng div/SVG.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **95. accent-** nêu điều cần giải thích; **96. trường dữ liệu (field / 필드) sizing** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **97. Resize** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 96. trường dữ liệu (field / 필드) sizing

Hiện đại (modern / 현대적) Tailwind có các tiện ích (utilities) liên quan `field-sizing`.

`field-sizing: content` cho phép đầu vào (input / 입력)/textarea trong mức hỗ trợ trình duyệt (browser support / 브라우저 지원) phù hợp kích thước (size / 크기) theo content.

Textarea:

```html
<textarea
  class="
    field-sizing-content
    min-h-24
    max-h-80
  "
></textarea>
```

Bạn vẫn nên đặt min/max ràng buộc (constraint / 제약조건) để content không làm bố cục (layout / 레이아웃) phát triển vô hạn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **96. trường dữ liệu (field / 필드) sizing** nêu điều cần giải thích; **97. Resize** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **98. Smooth scroll** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 97. Resize
Phần này nối mạch bài học với “97. Resize”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
resize
resize-x
resize-y
resize-none
```

Textarea thường nên cho phép ít nhất vertical resize:

```html
<textarea class="resize-y">
```

`resize-none` có thể làm UX kém nếu người dùng (user / 사용자) cần mở rộng vùng nhập liệu.

---

# PHẦN X — SCROLL, TOUCH VÀ vùng nhìn (viewport) tương tác (interaction / 상호작용)

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **98. Smooth scroll** tiếp nhận điểm tựa từ **97. Resize** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **99. Scroll snap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 98. Smooth scroll
Phần này nối mạch bài học với “98. Smooth scroll”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
scroll-smooth
scroll-auto
```

`scroll-smooth` đặt CSS `scroll-behavior: smooth`.

Nếu animation gây vấn đề motion preference, bạn có thể combine:

```text
motion-reduce:scroll-auto
```

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **99. Scroll snap** tiếp nhận điểm tựa từ **98. Smooth scroll** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **100. Overscroll** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 99. Scroll snap

Carousel:

```html
<div
  class="
    flex
    snap-x
    snap-mandatory
    gap-4
    overflow-x-auto
  "
>
  <article class="min-w-80 snap-start">
    ...
  </article>
</div>
```

`scroll-snap-type` đặt trên vùng chứa cuộn (scroll container); `snap-start`, `snap-center`, `snap-end` đặt trên items.

`mandatory` mạnh hơn `proximity`. Use carefully để không làm scrolling người dùng (user / 사용자) khó chịu.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **100. Overscroll** tiếp nhận điểm tựa từ **99. Scroll snap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **101. Scroll margin và sticky headers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 100. Overscroll

Nested modal scroller:

```html
<div
  class="
    max-h-[70dvh]
    overflow-auto
    overscroll-contain
  "
>
```

`overscroll-contain` giúp hạn chế truyền chuỗi cuộn (scroll chaining) ra page khi scroller bên trong đến ranh giới (boundary / 경계).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **101. Scroll margin và sticky headers** tiếp nhận điểm tựa từ **100. Overscroll** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **102. Touch action** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 101. Scroll margin và sticky headers

Anchor mục tiêu (target / 대상):

```html
<section
  id="billing"
  class="scroll-mt-20"
>
```

Khi trình duyệt (browser / 브라우저) scroll tới `#billing`, `scroll-margin-top` tạo khoảng tránh sticky header che mất heading.

Đây thường sạch hơn thêm fake padding/margin vào mọi section.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **102. Touch action** tiếp nhận điểm tựa từ **101. Scroll margin và sticky headers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **103. Scrollbar các tiện ích (utilities) v4.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 102. Touch action
Phần này nối mạch bài học với “102. Touch action”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
touch-auto
touch-none
touch-pan-x
touch-pan-y
touch-pinch-zoom
touch-manipulation
```

Custom carousel drag ngang trong page scroll dọc có thể dùng `touch-pan-y` để trình duyệt (browser / 브라우저) biết vertical scroll vẫn được phép.

`touch-none` rất mạnh và có thể phá bản địa (native / 네이티브) scroll/zoom khả năng tiếp cận (accessibility / 접근성). Chỉ dùng nếu thành phần (component / 컴포넌트) thực sự implement gesture thay thế đúng.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **103. Scrollbar các tiện ích (utilities) v4.3** tiếp nhận điểm tựa từ **102. Touch action** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **104. Mobile-first thật sự nghĩa là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 103. Scrollbar các tiện ích (utilities) v4.3

Tailwind v4.3 thêm first-party scrollbar các tiện ích (utilities).

Width:

```text
scrollbar-auto
scrollbar-thin
scrollbar-none
```

Color:

```text
scrollbar-thumb-slate-700
scrollbar-track-slate-100
```

Alpha modifier cũng có thể được dùng trong relevant color các tiện ích (utilities).

Gutter:

```text
scrollbar-gutter-auto
scrollbar-gutter-stable
scrollbar-gutter-both
```

`stable` reserve không gian (space / 공간) cho classic scrollbar để giảm dịch chuyển bố cục (layout shift) khi scrollbar xuất hiện.

Scrollbar rendering vẫn phụ thuộc trình duyệt (browser / 브라우저)/OS. Tailwind không biến scrollbar thành pixel-identical cross-platform điều khiển (control / 제어).

---

# PHẦN XI — thiết kế đáp ứng (responsive design)

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **104. Mobile-first thật sự nghĩa là gì?** tiếp nhận điểm tựa từ **103. Scrollbar các tiện ích (utilities) v4.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **105. điểm ngắt (breakpoint) names không phải thiết bị (device / 장치) names** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 104. Mobile-first thật sự nghĩa là gì?
Phần này nối mạch bài học với “104. Mobile-first thật sự nghĩa là gì?”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  class="
    grid
    grid-cols-1
    md:grid-cols-2
    xl:grid-cols-4
  "
>
```

Cơ sở (base / 기반) style chạy ở mọi width trừ khi bị override.

`md:grid-cols-2` nghĩa:

```text
từ md trở lên
→ 2 columns
```

Nó không nghĩa “chỉ ở md”.

`xl:grid-cols-4` tiếp tục override từ xl trở lên.

Đây là mobile-first min-width mô hình (model / 모델).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **105. điểm ngắt (breakpoint) names không phải thiết bị (device / 장치) names** tiếp nhận điểm tựa từ **104. Mobile-first thật sự nghĩa là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **106. Range responsive các biến thể (variants)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 105. điểm ngắt (breakpoint) names không phải thiết bị (device / 장치) names

Default Tailwind có:

```text
sm
md
lg
xl
2xl
```

Bạn không nên học chúng như:

```text
sm = phone
md = tablet
lg = laptop
```

Bố cục (layout / 레이아웃) nên chuyển khi **content cần**, không phải khi gặp tên thiết bị (device / 장치).

Custom điểm ngắt (breakpoint):

```css
@theme {
  --breakpoint-content-wide: 72rem;
}
```

Nếu nhóm (team / 팀) muốn mang tính ngữ nghĩa (semantic / 의미적) điểm ngắt (breakpoint) name, có thể dùng, nhưng đừng tạo `iphone-15:` hoặc `ipad-pro:` nếu sản phẩm (product / 제품) không thật sự phụ thuộc một thiết bị (device / 장치) cụ thể.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **106. Range responsive các biến thể (variants)** tiếp nhận điểm tựa từ **105. điểm ngắt (breakpoint) names không phải thiết bị (device / 장치) names** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **107. Vì sao truy vấn vùng chứa (container query) quan trọng hơn thêm điểm ngắt (breakpoint)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 106. Range responsive các biến thể (variants)
Phần này nối mạch bài học với “106. Range responsive các biến thể (variants)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="md:max-xl:grid">
```

nghĩa là quy tắc (rule / 규칙) active từ `md` đến dưới `xl`.

One-off:

```text
min-[520px]:
max-[760px]:
```

Arbitrary điểm ngắt (breakpoint) hợp lý cho cục bộ (local / 로컬) exception, nhưng nếu cùng threshold lặp ở nhiều thành phần (component / 컴포넌트), promote thành theme điểm ngắt (breakpoint) hoặc bộ chứa (container / 컨테이너) đơn vị từ (token / 토큰).

---

# PHẦN XII — các truy vấn vùng chứa (container queries)

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **107. Vì sao truy vấn vùng chứa (container query) quan trọng hơn thêm điểm ngắt (breakpoint)** tiếp nhận điểm tựa từ **106. Range responsive các biến thể (variants)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **108. truy vấn vùng chứa (container query) các điểm ngắt (breakpoints)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 107. Vì sao truy vấn vùng chứa (container query) quan trọng hơn thêm điểm ngắt (breakpoint)

Một Card có thể được kết xuất (render / 렌더링):
- full-width main content,
- narrow sidebar,
- modal,
- dashboard grid.

Nếu Card chỉ nhìn vùng nhìn (viewport) bằng `md:`, nó có thể nghĩ “desktop” dù chính Card chỉ rộng 300px.

truy vấn vùng chứa (container query) hỏi:

> bộ chứa (container / 컨테이너) của thành phần (component / 컴포넌트) hiện rộng bao nhiêu?

Mark bộ chứa (container / 컨테이너):

```html
<div class="@container">
```

Child:

```html
<article
  class="
    flex
    flex-col
    @md:flex-row
  "
>
```

`@md:` ở đây không phải vùng nhìn (viewport) `md:`. Nó là truy vấn vùng chứa (container query) threshold.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **108. truy vấn vùng chứa (container query) các điểm ngắt (breakpoints)** tiếp nhận điểm tựa từ **107. Vì sao truy vấn vùng chứa (container query) quan trọng hơn thêm điểm ngắt (breakpoint)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **109. bộ chứa (container / 컨테이너) max/phạm vi (range / 범위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 108. truy vấn vùng chứa (container query) các điểm ngắt (breakpoints)

Tailwind có các bộ chứa (container / 컨테이너) kích thước (size / 크기) các biến thể (variants) như:

```text
@3xs
@2xs
@xs
@sm
@md
@lg
@xl
...
```

Hiện tại (current / 현재) default bộ chứa (container / 컨테이너) quy mô (scale / 규모) bắt đầu từ các kích thước (size / 크기) nhỏ như 16rem và tăng dần.

Bạn không cần thuộc từng số ngay. Điều quan trọng là hiểu không gian tên (namespace / 네임스페이스) `--container-*` quyết định truy vấn vùng chứa (container query) các biến thể (variants).

Custom:

```css
@theme {
  --container-card-wide: 36rem;
}
```

Sau đó API bộ chứa (container / 컨테이너) có thể dùng đơn vị từ (token / 토큰) đó theo supported naming ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **109. bộ chứa (container / 컨테이너) max/phạm vi (range / 범위)** tiếp nhận điểm tựa từ **108. truy vấn vùng chứa (container query) các điểm ngắt (breakpoints)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **110. @container-size trong v4.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 109. bộ chứa (container / 컨테이너) max/phạm vi (range / 범위)

Bạn có thể viết:

```text
@max-md:
@sm:@max-md:
@min-[475px]:
@max-[960px]:
```

Điều này cho component-local ranges.

Đừng lạm dụng phạm vi (range / 범위) nếu bố cục (layout / 레이아웃) có thể được giải bằng intrinsic Grid/Flex.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **110. @container-size trong v4.3** tiếp nhận điểm tựa từ **109. bộ chứa (container / 컨테이너) max/phạm vi (range / 범위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **111. Hover** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 110. `@container-size` trong v4.3

Regular:

```text
@container
```

tạo inline-size bộ chứa (container / 컨테이너), chủ yếu truy vấn (query / 쿼리) width/inline dimension.

V4.3:

```text
@container-size
```

tạo kích thước (size / 크기) bộ chứa (container / 컨테이너), cho phép dimension liên quan block-size/height.

Ví dụ:

```html
<div class="@container-size">
  <div class="h-[50cqb]">
```

`cqb` cần khối (block / 블록) kích thước (size / 크기) của truy vấn (query / 쿼리) bộ chứa (container / 컨테이너).

Kích thước (size / 크기) containment có ảnh hưởng sizing mạnh hơn inline containment, nên đừng đổi tất cả bộ chứa (container / 컨테이너) sang `@container-size` chỉ vì nó “mạnh hơn”.

---

# PHẦN XIII — các biến thể trạng thái (state variants)

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **111. Hover** tiếp nhận điểm tựa từ **110. @container-size trong v4.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **112. Focus và focus-visible** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 111. Hover
Phần này nối mạch bài học với “111. Hover”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<button class="bg-blue-600 hover:bg-blue-700">
```

Tailwind generate hover bộ chọn (selector) cùng handling cho hover-capable môi trường (environment / 환경).

Điều này quan trọng trên touch thiết bị (device / 장치) vì “hover” không có cùng nghĩa như mouse desktop.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **112. Focus và focus-visible** tiếp nhận điểm tựa từ **111. Hover** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **113. Active** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 112. Focus và `focus-visible`
Phần này nối mạch bài học với “112. Focus và `focus-visible`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
focus:
focus-visible:
focus-within:
```

`focus:` style chính element khi focused.

`focus-visible:` style khi trình duyệt (browser / 브라우저) xác định cần visible chỉ báo tiêu điểm (focus indicator).

`focus-within:` style parent khi chính nó hoặc descendant focus.

Form group:

```html
<label
  class="
    rounded-lg
    focus-within:ring-2
    focus-within:ring-blue-500/20
  "
>
```

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **113. Active** tiếp nhận điểm tựa từ **112. Focus và focus-visible** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **114. Structural các biến thể (variants)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 113. Active
Phần này nối mạch bài học với “113. Active”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
active:
```

map khóa–giá trị (map) tới `:active`, thường là thời điểm pointer/button đang được activate.

Micro phản hồi (feedback / 피드백):

```html
<button class="active:scale-[.98]">
```

Nếu motion không cần thiết, respect giảm chuyển động (reduced motion).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **114. Structural các biến thể (variants)** tiếp nhận điểm tựa từ **113. Active** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **115. nth-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 114. Structural các biến thể (variants)

Tailwind có các biến thể (variants) như:

```text
first:
last:
only:
odd:
even:
empty:
first-of-type:
last-of-type:
```

Danh sách (list / 목록) divider:

```html
<li class="border-b last:border-b-0">
```

Những bộ chọn (selector) này nên mô tả cấu trúc (structure / 구조) thật. Nếu trạng thái (state / 상태) nghiệp vụ (business / 비즈니스) là “selected row”, hãy dùng `data-selected`/ARIA chứ không dùng `nth-child` để giả trạng thái (state / 상태).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **115. nth-** tiếp nhận điểm tựa từ **114. Structural các biến thể (variants)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **116. Form các biến thể trạng thái (state variants)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 115. `nth-*`

Hiện tại (current / 현재) Tailwind supports expressive nth các biến thể (variants).

```text
nth-3:
nth-last-2:
nth-of-type-4:
```

Arbitrary:

```text
nth-[2n+1_of_li]:
```

map khóa–giá trị (map) tới CSS `:nth-child(...)` family.

Use cho zebra striping hoặc bố cục (layout / 레이아웃) mẫu (pattern / 패턴) dựa structural thứ tự (order / 순서).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **116. Form các biến thể trạng thái (state variants)** tiếp nhận điểm tựa từ **115. nth-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **117. group-: style child theo parent trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 116. Form các biến thể trạng thái (state variants)

Tailwind có nhiều các biến thể trạng thái (state variants):

```text
required:
optional:
valid:
invalid:
user-valid:
user-invalid:
disabled:
enabled:
checked:
indeterminate:
read-only:
placeholder-shown:
in-range:
out-of-range:
autofill:
```

Ví dụ:

```html
<input
  class="
    border-gray-300
    user-invalid:border-red-500
    disabled:cursor-not-allowed
    disabled:bg-gray-100
    disabled:text-gray-500
  "
>
```

`user-invalid` thường tạo UX tốt hơn `invalid` trong form vì tránh hiển thị lỗi quá sớm trước khi người dùng (user / 사용자) tương tác (interaction / 상호작용), tùy trình duyệt (browser / 브라우저) ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **117. group-: style child theo parent trạng thái (state / 상태)** tiếp nhận điểm tựa từ **116. Form các biến thể trạng thái (state variants)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **118. peer-: style sibling theo sibling trạng thái (state)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 117. `group-*`: style child theo parent trạng thái (state / 상태)

Parent:

```html
<a class="group">
```

Child:

```html
<span class="group-hover:text-blue-600">
```

Tailwind generate bộ chọn (selector) liên hệ child với `.group:hover`.

Nested components nên dùng named group:

```html
<div class="group/card">
  <button class="group-hover/card:opacity-100">
```

Nếu không name, một child sâu có thể vô tình react với wrong ancestor group.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **118. peer-: style sibling theo sibling trạng thái (state)** tiếp nhận điểm tựa từ **117. group-: style child theo parent trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **119. has-: parent-aware styling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 118. `peer-*`: style sibling theo sibling trạng thái (state)
Phần này nối mạch bài học với “118. `peer-*`: style sibling theo sibling trạng thái (state)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="email"
  class="peer"
/>

<p
  class="
    invisible
    peer-invalid:visible
  "
>
  Invalid email
</p>
```

CSS sibling bộ chọn (selector) hoạt động từ element trước sang element sau, nên mục tiêu (target / 대상) phải xuất hiện sau peer trong DOM.

Nếu mục tiêu (target / 대상) cần style previous sibling, dùng parent `has-*` hoặc restructure DOM thay vì cố ép peer.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **119. has-: parent-aware styling** tiếp nhận điểm tựa từ **118. peer-: style sibling theo sibling trạng thái (state)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **120. in-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 119. `has-*`: parent-aware styling
Phần này nối mạch bài học với “119. `has-*`: parent-aware styling”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<label class="has-checked:bg-blue-50">
  <input type="radio">
  ...
</label>
```

các map khóa–giá trị (maps) conceptually tới:

```css
label:has(:checked)
```

`:has()` giúp style parent dựa trên child trạng thái (state / 상태) mà không cần JS lớp (class / 클래스) toggle.

Use tốt cho:
- checked điều khiển (control / 제어),
- invalid child,
- optional slot existence,
- focus child.

Nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) không tồn tại trong DOM vẫn cần ứng dụng (application / 애플리케이션) lô-gic (logic / 논리).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **120. in-** tiếp nhận điểm tựa từ **119. has-: parent-aware styling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **121. Child các biến thể (variants) : và :** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 120. `in-*`

`in-*` cho phép respond tới ancestor trạng thái (state / 상태) mà không mark tường minh (explicit / 명시적) `.group`.

Điều này tiện trong shallow UI, nhưng càng nested càng khó biết ancestor nào kích hoạt.

Cấp cao (senior / 시니어) preference: nếu quyền sở hữu (ownership / 소유권) quan trọng, named `group` rõ hơn implicit `in-*`.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **121. Child các biến thể (variants) : và :** tiếp nhận điểm tựa từ **120. in-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **122. ARIA các biến thể (variants)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 121. Child các biến thể (variants) `*:` và `**:`
Phần này nối mạch bài học với “121. Child các biến thể (variants) `*:` và `**:`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<ul class="*:rounded-md *:px-3">
```

`*:` mục tiêu (target / 대상) direct children.

`**:` mục tiêu (target / 대상) descendants sâu hơn.

Đây là convenience khi parent kiểm soát uniform child style. Nếu một child cần nhiều exception, lớp (class / 클래스) đặt trực tiếp trên child thường dễ lập luận (reasoning / 추론) hơn.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **122. ARIA các biến thể (variants)** tiếp nhận điểm tựa từ **121. Child các biến thể (variants) : và :** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **123. Data các biến thể (variants)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 122. ARIA các biến thể (variants)
Phần này nối mạch bài học với “122. ARIA các biến thể (variants)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<button
  aria-pressed="true"
  class="
    aria-pressed:bg-blue-600
    aria-pressed:text-white
  "
>
```

ARIA trạng thái (state / 상태) vừa có ngữ nghĩa (semantics / 의미론) khả năng tiếp cận (accessibility / 접근성) vừa là bộ chọn (selector) hook.

Nhưng không được set ARIA sai chỉ để style. Ví dụ random `<div aria-selected="true">` không nằm trong widget ngữ nghĩa (semantics / 의미론) có thể misleading cho assistive technology.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **123. Data các biến thể (variants)** tiếp nhận điểm tựa từ **122. ARIA các biến thể (variants)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **124. Dark mode mặc định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 123. Data các biến thể (variants)
Phần này nối mạch bài học với “123. Data các biến thể (variants)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  data-state="open"
  class="
    opacity-0
    data-[state=open]:opacity-100
  "
>
```

Mẫu (pattern / 패턴) cấp cao (senior / 시니어):

```text
business/application state
→ data-* attribute

accessibility semantic state
→ aria-* attribute

Tailwind
→ presentation
```

JS không cần hard-code visual CSS; Tailwind/CSS không cần biết lô-gic nghiệp vụ (business logic / 비즈니스 로직).

---

# PHẦN XIV — DARK chế độ (mode / 모드) VÀ người dùng (user / 사용자) PREFERENCES

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **124. Dark mode mặc định** tiếp nhận điểm tựa từ **123. Data các biến thể (variants)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125. Manual dark chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 124. Dark mode mặc định
Phần này nối mạch bài học với “124. Dark mode mặc định”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  class="
    bg-white
    text-gray-950
    dark:bg-gray-950
    dark:text-gray-50
  "
>
```

By default, `dark:` có thể dựa trên hệ thống (system / 시스템) `prefers-color-scheme` theo Tailwind cấu hình (configuration / 구성)/default chiến lược (strategy / 전략) hiện hành.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **125. Manual dark chế độ (mode / 모드)** tiếp nhận điểm tựa từ **124. Dark mode mặc định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126. hệ thống (system / 시스템) / Light / Dark ba trạng thái** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125. Manual dark chế độ (mode / 모드)

Nếu app có theme switcher:

```css
@custom-variant dark
  (&:where(.dark, .dark *));
```

Sau đó gốc (root / 루트):

```html
<html class="dark">
```

activate `dark:*`.

Dữ liệu (data / 데이터) attribute biến thể (variant):

```css
@custom-variant dark
  (&:where(
    [data-theme=dark],
    [data-theme=dark] *
  ));
```

Gốc (root / 루트):

```html
<html data-theme="dark">
```

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **126. hệ thống (system / 시스템) / Light / Dark ba trạng thái** tiếp nhận điểm tựa từ **125. Manual dark chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127. motion-reduce, contrast, màu cưỡng bức (forced colors)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126. hệ thống (system / 시스템) / Light / Dark ba trạng thái

Một app thường có:
- light,
- dark,
- hệ thống (system / 시스템).

Tailwind không quản lý lưu trữ (storage / 저장소) hay app preference cho bạn. JS/máy chủ (server / 서버) xác định gốc (root / 루트) trạng thái (state / 상태). Tailwind chỉ style theo điều kiện (condition / 조건).

Kiến trúc (architecture / 아키텍처):

```text
user preference
→ storage/server
→ root class/data attribute
→ dark variant
→ generated CSS
```

Nếu gốc (root / 루트) trạng thái (state / 상태) set quá muộn sau first paint, bạn có thể thấy flash sai theme. Đó là theme initialization issue, không phải Tailwind tiện ích (utility) issue.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **126. hệ thống (system / 시스템) / Light / Dark ba trạng thái** đã nêu tiêu chí phân biệt, còn **127. motion-reduce, contrast, màu cưỡng bức (forced colors)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **128. @theme khác :root như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127. `motion-reduce`, contrast, màu cưỡng bức (forced colors)

Tailwind các biến thể (variants) cho người dùng (user / 사용자)/môi trường (environment / 환경) preferences như:

```text
motion-reduce:
motion-safe:
contrast-more:
contrast-less:
forced-colors:
print:
portrait:
landscape:
pointer-fine:
pointer-coarse:
```

Use những điều kiện (condition / 조건) phản ánh năng lực (capability / 역량)/preference thật thay vì đoán loại thiết bị (device / 장치).

---

# PHẦN XV — `@theme` VÀ đơn vị từ (token / 토큰) thiết kế (design tokens)

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **127. motion-reduce, contrast, màu cưỡng bức (forced colors)** đã nêu tiêu chí phân biệt, còn **128. @theme khác :root như thế nào?** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **129. không gian tên (namespace / 네임스페이스) là API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 128. `@theme` khác `:root` như thế nào?

Normal CSS:

```css
:root {
  --brand: #2563eb;
}
```

Trình duyệt (browser / 브라우저) biết `--brand`, nhưng Tailwind không tự hiểu nó là color đơn vị từ (token / 토큰) để tạo `bg-brand`.

Tailwind:

```css
@theme {
  --color-brand: #2563eb;
}
```

`--color-*` thuộc color không gian tên (namespace / 네임스페이스), nên Tailwind vừa emit CSS biến (variable) vừa tạo relevant tiện ích (utility) APIs.

Đây là lý do `@theme` không chỉ là “CSS các biến (variables) cú pháp (syntax / 문법) khác”.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **129. không gian tên (namespace / 네임스페이스) là API** tiếp nhận điểm tựa từ **128. @theme khác :root như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **130. thành phần nguyên thủy (primitive / 기본 요소) đơn vị từ (token / 토큰) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 129. không gian tên (namespace / 네임스페이스) là API

Một số không gian tên (namespace / 네임스페이스) quan trọng:

```text
--color-*
--font-*
--text-*
--font-weight-*
--tracking-*
--leading-*
--spacing-*
--radius-*
--shadow-*
--blur-*
--ease-*
--animate-*
--breakpoint-*
--container-*
--tab-size-*
```

Bạn không cần nhớ mọi không gian tên (namespace / 네임스페이스) ngay. Nhưng cần hiểu mẫu (pattern / 패턴): không gian tên (namespace / 네임스페이스) quyết định tiện ích (utility) family.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **130. thành phần nguyên thủy (primitive / 기본 요소) đơn vị từ (token / 토큰) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token)** tiếp nhận điểm tựa từ **129. không gian tên (namespace / 네임스페이스) là API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **131. Theme đơn vị từ (token / 토큰) không nhất thiết nên dùng cho mọi thuộc tính (property / 속성) role** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 130. thành phần nguyên thủy (primitive / 기본 요소) đơn vị từ (token / 토큰) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token)

Thành phần nguyên thủy (primitive / 기본 요소):

```text
blue-600
gray-200
radius-lg
```

mang tính ngữ nghĩa (semantic / 의미적):

```text
action-primary
surface-default
text-muted
danger-bg
danger-fg
```

Thành phần nguyên thủy (primitive / 기본 요소) thuận tiện cho composition nhanh. mang tính ngữ nghĩa (semantic / 의미적) thuận tiện cho rebrand/theme.

Một hệ thống lớn có thể dùng:

```css
@theme {
  --color-brand-500: ...;
  --color-brand-600: ...;
}
```

và thêm thời gian chạy (runtime / 런타임) mang tính ngữ nghĩa (semantic / 의미적) vars:

```css
:root {
  --button-primary-bg:
    var(--color-brand-600);
}
```

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **131. Theme đơn vị từ (token / 토큰) không nhất thiết nên dùng cho mọi thuộc tính (property / 속성) role** tiếp nhận điểm tựa từ **130. thành phần nguyên thủy (primitive / 기본 요소) đơn vị từ (token / 토큰) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **132. Reset không gian tên (namespace) cho strict hệ thống thiết kế (design system)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 131. Theme đơn vị từ (token / 토큰) không nhất thiết nên dùng cho mọi thuộc tính (property / 속성) role

Nếu:

```css
@theme {
  --color-danger: red;
}
```

Tailwind có thể expose:
- `bg-danger`,
- `text-danger`,
- `border-danger`.

Nhưng hệ thống thiết kế (design system) có thể cần:
- danger background nhạt,
- danger văn bản (text / 텍스트) đậm,
- danger border trung gian.

Khi đó đơn vị từ (token / 토큰) nên chi tiết:

```text
danger-bg
danger-fg
danger-border
```

Cấp cao (senior / 시니어) đơn vị từ (token / 토큰) thiết kế (design / 설계) quan tâm ngữ nghĩa (semantics / 의미론), không chỉ màu.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **132. Reset không gian tên (namespace) cho strict hệ thống thiết kế (design system)** tiếp nhận điểm tựa từ **131. Theme đơn vị từ (token / 토큰) không nhất thiết nên dùng cho mọi thuộc tính (property / 속성) role** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **133. @utility: đăng ký tiện ích (utility) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 132. Reset không gian tên (namespace) cho strict hệ thống thiết kế (design system)
Phần này nối mạch bài học với “132. Reset không gian tên (namespace) cho strict hệ thống thiết kế (design system)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@theme {
  --color-*: initial;

  --color-surface: ...;
  --color-text: ...;
  --color-action: ...;
  --color-danger: ...;
}
```

Điều này remove default palette API và chỉ giữ approved colors.

Lợi là dev không “chọn đại blue-500”. Hại là generic examples/thư viện (library / 라이브러리) mã (code / 코드) dựa default palette có thể không công việc (work / 작업).

Strict theme phù hợp hệ thống thiết kế (design system) mature hơn beginner app.

---

# PHẦN XVI — CUSTOMIZATION API CỦA TAILWIND V4

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **133. @utility: đăng ký tiện ích (utility) riêng** tiếp nhận điểm tựa từ **132. Reset không gian tên (namespace) cho strict hệ thống thiết kế (design system)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **134. Khi nào nên tạo custom tiện ích (utility)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 133. `@utility`: đăng ký tiện ích (utility) riêng
Phần này nối mạch bài học với “133. `@utility`: đăng ký tiện ích (utility) riêng”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@utility content-auto {
  content-visibility: auto;
}
```

Use:

```html
<div class="content-auto">
```

Vì đã đăng ký bằng `@utility`, bạn có thể dùng các biến thể (variants):

```text
lg:content-auto
```

Khác với:

```css
.content-auto {
  content-visibility:auto;
}
```

là một normal lớp (class / 클래스), không nhất thiết tham gia Tailwind tiện ích (utility) resolution giống nhau.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **134. Khi nào nên tạo custom tiện ích (utility)?** tiếp nhận điểm tựa từ **133. @utility: đăng ký tiện ích (utility) riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **135. Functional @utility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 134. Khi nào nên tạo custom tiện ích (utility)?

Custom tiện ích (utility) phù hợp khi concern:
- atomic,
- reusable,
- dự án (project / 프로젝트)/cốt lõi (core / 핵심) chưa có tiện ích (utility) rõ,
- cần các biến thể (variants).

Ví dụ `content-visibility` thành phần nguyên thủy (primitive / 기본 요소) là tiện ích (utility) tốt.

Một `super-dashboard-card` chứa 15 các thuộc tính (properties), hover, child các bộ chọn (selectors) và trạng thái (state / 상태) thì không còn là atomic tiện ích (utility); đó là thành phần (component / 컴포넌트)/custom CSS.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **135. Functional @utility** tiếp nhận điểm tựa từ **134. Khi nào nên tạo custom tiện ích (utility)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **136. --default() trong v4.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 135. Functional `@utility`

V4 cho phép tiện ích (utility) family:

```css
@utility tab-* {
  tab-size:
    --value(
      --tab-size-*,
      integer,
      [integer]
    );
}
```

Một definition có thể hỗ trợ (support / 지원):
- theme đơn vị từ (token / 토큰),
- bare numeric giá trị (value / 값),
- giá trị tùy ý (arbitrary value).

`--value()` là **Tailwind build-time resolver**. trình duyệt (browser / 브라우저) không biết hàm (function / 함수) này.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **136. --default() trong v4.3** tiếp nhận điểm tựa từ **135. Functional @utility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **137. Modifier và --modifier()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 136. `--default()` trong v4.3
Phần này nối mạch bài học với “136. `--default()` trong v4.3”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@utility tab-* {
  tab-size:
    --value(
      integer,
      --default(4)
    );
}
```

Now:

```text
tab
```

có default 4, còn:

```text
tab-2
```

resolve 2.

Use bare tiện ích (utility) default khi ý nghĩa mặc định thật sự tự nhiên.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **137. Modifier và --modifier()** tiếp nhận điểm tựa từ **136. --default() trong v4.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **138. @custom-variant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 137. Modifier và `--modifier()`

Một candidate như:

```text
text-lg/7
```

có main giá trị (value / 값) `lg` và modifier `7`.

Custom tiện ích (utility) cũng có thể dùng modifier cho secondary dimension.

Đừng tạo API với slash modifier nếu relationship không intuitive, vì tiện ích (utility) sẽ trở nên khó đoán.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **138. @custom-variant** tiếp nhận điểm tựa từ **137. Modifier và --modifier()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **139. @variant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 138. `@custom-variant`

Nếu app có theme/trạng thái (state / 상태) repeated:

```css
@custom-variant theme-midnight
  (&:where([data-theme="midnight"] *));
```

Use:

```html
<div class="theme-midnight:bg-black">
```

Bạn đã biến một bộ chọn (selector) phức tạp thành mang tính ngữ nghĩa (semantic / 의미적) biến thể (variant).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **139. @variant** tiếp nhận điểm tựa từ **138. @custom-variant** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **140. @apply** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 139. `@variant`

Trong custom CSS:

```css
.button-shell {
  @variant dark {
    background: black;
  }
}
```

V4.3 hỗ trợ (support / 지원) compound/stacked biến thể (variant) forms tốt hơn, ví dụ:

```css
@variant hover:focus {
  ...
}
```

và multiple:

```css
@variant hover, focus {
  ...
}
```

`@variant` hữu ích khi bạn đã chọn custom CSS nhưng vẫn muốn reuse Tailwind biến thể (variant) lô-gic (logic / 논리).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **140. @apply** tiếp nhận điểm tựa từ **139. @variant** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **141. @reference** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 140. `@apply`
Phần này nối mạch bài học với “140. `@apply`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
.select2-dropdown {
  @apply rounded-lg bg-white shadow-lg;
}
```

`@apply` inline Tailwind các tiện ích (utilities) vào custom CSS bộ chọn (selector).

Use trường hợp (case / 사례) tốt:
- third-party markup,
- CMS/editor đầu ra (output / 출력),
- legacy bộ chọn (selector),
- thành phần (component / 컴포넌트) style ngữ cảnh (context / 맥락) không thể đặt tiện ích (utility) trực tiếp.

Use trường hợp (case / 사례) xấu là tạo lại toàn bộ mang tính ngữ nghĩa (semantic / 의미적) CSS kiến trúc (architecture / 아키텍처) cũ:

```css
.btn-primary {
  @apply ...;
}
```

cho mọi button trong React app, rồi markup lại quay về `.btn-primary`. Nếu thành phần (component / 컴포넌트) lớp trừu tượng (abstraction / 추상화) đã tồn tại, hãy compose các tiện ích (utilities) trong thành phần (component / 컴포넌트).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, sau nội dung của **140. @apply**, **141. @reference** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **142. Automatic phát hiện nguồn (source detection)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 141. `@reference`

Trong Vue/Svelte/CSS Modules, một style khối (block / 블록) riêng có thể không nhìn thấy custom theme/các tiện ích (utilities) của main biểu định kiểu (stylesheet / 스타일시트).

```css
@reference "../../app.css";

.title {
  @apply text-2xl font-bold;
}
```

`@reference` cho Tailwind processing ngữ cảnh (context / 맥락) biết definitions mà không duplicate CSS đầu ra (output / 출력).

Nếu chỉ cần một đơn vị từ (token / 토큰):

```css
.title {
  color: var(--color-red-500);
}
```

thường đơn giản hơn.

---

# PHẦN XVII — phát hiện nguồn (source detection)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **141. @reference** nêu điều cần giải thích; **142. Automatic phát hiện nguồn (source detection)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **143. @source** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 142. Automatic phát hiện nguồn (source detection)

Tailwind v4 scan dự án (project / 프로젝트) nhưng bỏ qua nhiều loại nguồn (source / 소스) không cần thiết như `node_modules`, nhị phân (binary / 이진), CSS tệp (file / 파일), ignored files.

Vì vậy phụ thuộc (dependency / 의존성) chứa Tailwind classes có thể cần tường minh (explicit / 명시적) nguồn (source / 소스) registration.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **142. Automatic phát hiện nguồn (source detection)** nêu điều cần giải thích; **143. @source** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **144. source() base path** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 143. `@source`
Phần này nối mạch bài học với “143. `@source`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@source "../node_modules/@acme/ui-lib";
```

nói Tailwind scan gói (package / 패키지) đó.

Monorepo:

```css
@source "../../packages/ui/src";
```

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **143. @source** nêu điều cần giải thích; **144. source() base path** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **145. Ignore path** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 144. `source()` base path
Phần này nối mạch bài học với “144. `source()` base path”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@import "tailwindcss"
  source("../src");
```

Dùng khi hiện tại (current / 현재) working directory của bản dựng (build / 빌드) khác ứng dụng (application / 애플리케이션) nguồn (source / 소스) gốc (root / 루트).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **144. source() base path** nêu điều cần giải thích; **145. Ignore path** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **146. source(none)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 145. Ignore path
Phần này nối mạch bài học với “145. Ignore path”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@source not "../src/legacy";
```

Nếu folder lớn không có Tailwind candidates, loại khỏi scan có thể giúp nguồn (source / 소스) quyền sở hữu (ownership / 소유권) rõ và giảm công việc (work / 작업).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **145. Ignore path** nêu điều cần giải thích; **146. source(none)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **147. danh sách ép giữ (safelist) bằng @source inline()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 146. `source(none)`
Phần này nối mạch bài học với “146. `source(none)`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@import "tailwindcss"
  source(none);

@source "../admin";
@source "../shared";
```

Tắt automatic detection để bundle chỉ scan tường minh (explicit / 명시적) roots.

Rất hữu ích khi dự án (project / 프로젝트) có:
- admin.css,
- storefront.css,
- nhiều microfrontend.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **146. source(none)** nêu điều cần giải thích; **147. danh sách ép giữ (safelist) bằng @source inline()** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **148. Khi nào lớp (class / 클래스) dài là bình thường?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 147. danh sách ép giữ (safelist) bằng `@source inline()`

Khi cần force generate lớp (class / 클래스) không nằm literal trong normal nguồn (source / 소스), v4 dùng nguồn (source / 소스) inline API.

Ví dụ conceptual:

```css
@source inline("underline");
```

Bạn có thể danh sách ép giữ (safelist) các biến thể (variants)/ranges bằng brace expansion theo docs.

Nhưng broad danh sách ép giữ (safelist) làm Tailwind mất lợi ích usage-driven CSS generation.

---

# PHẦN XVIII — thành phần (component / 컴포넌트) kiến trúc (architecture / 아키텍처)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **147. danh sách ép giữ (safelist) bằng @source inline()** nêu điều cần giải thích; **148. Khi nào lớp (class / 클래스) dài là bình thường?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **149. Extract thành phần (component / 컴포넌트) chứ không nhất thiết extract CSS lớp (class / 클래스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 148. Khi nào lớp (class / 클래스) dài là bình thường?

Một button:

```html
<button
  class="
    inline-flex
    items-center
    justify-center
    gap-2
    rounded-lg
    bg-blue-600
    px-4
    py-2
    text-sm
    font-semibold
    text-white
    transition-colors
    hover:bg-blue-700
    focus-visible:outline-2
    focus-visible:outline-offset-2
    disabled:cursor-not-allowed
    disabled:opacity-50
  "
>
```

không tự động là “bad” chỉ vì nhiều lớp (class / 클래스). Bạn đang nhìn toàn bộ visual hành vi (behavior / 동작) ngay tại thành phần (component / 컴포넌트).

Nó trở thành vấn đề khi same cấu trúc (structure / 구조) + same style + same các trạng thái (states) được bản sao (copy / 복사) vào nhiều nơi.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **149. Extract thành phần (component / 컴포넌트) chứ không nhất thiết extract CSS lớp (class / 클래스)** tiếp nhận điểm tựa từ **148. Khi nào lớp (class / 클래스) dài là bình thường?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **150. biến thể (variant) API nên mang tính ngữ nghĩa (semantic / 의미적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 149. Extract thành phần (component / 컴포넌트) chứ không nhất thiết extract CSS lớp (class / 클래스)

React:

```jsx
function Button({
  variant = "primary",
  size = "md",
  children,
}) {
  const variants = {
    primary:
      "bg-blue-600 text-white hover:bg-blue-700",
    danger:
      "bg-red-600 text-white hover:bg-red-700",
  };

  const sizes = {
    sm:
      "min-h-9 px-3 text-sm",
    md:
      "min-h-10 px-4 text-sm",
    lg:
      "min-h-12 px-5 text-base",
  };

  return (
    <button
      className={`
        inline-flex
        items-center
        justify-center
        rounded-lg
        font-semibold
        focus-visible:outline-2
        ${variants[variant]}
        ${sizes[size]}
      `}
    >
      {children}
    </button>
  );
}
```

Bên tiêu thụ (consumer / 소비자):

```jsx
<Button variant="danger" size="lg">
  Delete
</Button>
```

Bên tiêu thụ (consumer / 소비자) không cần biết Tailwind classes.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **150. biến thể (variant) API nên mang tính ngữ nghĩa (semantic / 의미적)** tiếp nhận điểm tựa từ **149. Extract thành phần (component / 컴포넌트) chứ không nhất thiết extract CSS lớp (class / 클래스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **151. lớp (class / 클래스) xung đột (conflict / 충돌)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 150. biến thể (variant) API nên mang tính ngữ nghĩa (semantic / 의미적)

Bad:

```jsx
<Button color="red-600">
```

Better:

```jsx
<Button variant="danger">
```

Nếu thiết kế (design / 설계) đổi từ red-600 sang rose-700, caller không thay đổi.

Tương tự:

```text
density="compact"
```

tốt hơn:

```text
padding="p-2"
```

nếu thành phần (component / 컴포넌트) là công khai (public / 공개) design-system thành phần (component / 컴포넌트).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **151. lớp (class / 클래스) xung đột (conflict / 충돌)** tiếp nhận điểm tựa từ **150. biến thể (variant) API nên mang tính ngữ nghĩa (semantic / 의미적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **152. className escape hatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 151. lớp (class / 클래스) xung đột (conflict / 충돌)

Bạn có thể compose:

```text
px-4
```

ở cơ sở (base / 기반) và caller truyền:

```text
px-2
```

Một lỗi tư duy là nghĩ lớp (class / 클래스) viết sau trong attribute chắc chắn thắng.

CSS cơ chế phân tầng (cascade) dùng thứ tự (order / 순서) của generated biểu định kiểu (stylesheet / 스타일시트), độ đặc hiệu (specificity) và layers, không đơn giản dùng đơn vị từ (token / 토큰) thứ tự (order / 순서) trong HTML lớp (class / 클래스) attribute.

Thành phần (component / 컴포넌트) thư viện (library / 라이브러리) thường dùng conflict-aware merge helper để normalize Tailwind tiện ích (utility) groups nếu muốn caller override.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **152. className escape hatch** tiếp nhận điểm tựa từ **151. lớp (class / 클래스) xung đột (conflict / 충돌)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **153. Tailwind không tạo khả năng tiếp cận (accessibility / 접근성) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 152. `className` escape hatch

Một reusable thành phần (component / 컴포넌트) thường vẫn nhận:

```jsx
<Button className="w-full">
```

mang tính ngữ nghĩa (semantic / 의미적) biến thể (variant) quyết định cốt lõi (core / 핵심) visual đặc tả hợp đồng (contract / 계약). `className` cho cục bộ (local / 로컬) bố cục (layout / 레이아웃) override.

Bạn cần document:
- caller override gì,
- xung đột (conflict / 충돌) merge thế nào,
- nội bộ (internal / 내부) classes hay caller classes ưu tiên.

---

# PHẦN XIX — khả năng tiếp cận (accessibility / 접근성)

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **153. Tailwind không tạo khả năng tiếp cận (accessibility / 접근성) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **152. className escape hatch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **154. sr-only** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 153. Tailwind không tạo khả năng tiếp cận (accessibility / 접근성) ngữ nghĩa (semantics / 의미론)

Tailwind có các tiện ích (utilities) tuyệt vời cho focus, motion, ARIA trạng thái (state / 상태), nhưng nó không biến:

```html
<div class="cursor-pointer">
```

thành button.

mang tính ngữ nghĩa (semantic / 의미적) HTML vẫn phải chọn đúng element.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **154. sr-only** tiếp nhận điểm tựa từ **153. Tailwind không tạo khả năng tiếp cận (accessibility / 접근성) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **155. Focus visible** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 154. `sr-only`
Phần này nối mạch bài học với “154. `sr-only`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<button>
  <svg aria-hidden="true">...</svg>
  <span class="sr-only">
    Close dialog
  </span>
</button>
```

`sr-only` dùng visually-hidden CSS mẫu (pattern / 패턴) để văn bản (text / 텍스트) không nhìn thấy nhưng vẫn có accessible content.

`not-sr-only` restore style.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **155. Focus visible** tiếp nhận điểm tựa từ **154. sr-only** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **156. Disabled** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 155. Focus visible

Đừng xóa chỉ báo tiêu điểm (focus indicator).

Good:

```html
<button
  class="
    focus-visible:outline-2
    focus-visible:outline-offset-2
    focus-visible:outline-blue-600
  "
>
```

Focus ring color phải có contrast đủ với surrounding background.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **156. Disabled** tiếp nhận điểm tựa từ **155. Focus visible** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **157. màu cưỡng bức (forced colors)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 156. Disabled

Use:

```html
<button
  disabled
  class="
    disabled:cursor-not-allowed
    disabled:opacity-50
  "
>
```

Style không thay mang tính ngữ nghĩa (semantic / 의미적) disabled.

Nếu custom điều khiển (control / 제어) không hỗ trợ (support / 지원) bản địa (native / 네이티브) `disabled`, ARIA/lô-gic nghiệp vụ (business logic / 비즈니스 로직) cần được thiết kế đúng chứ không chỉ thêm `opacity-50`.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **157. màu cưỡng bức (forced colors)** tiếp nhận điểm tựa từ **156. Disabled** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **158. Tailwind CSS đầu ra (output / 출력) không tỷ lệ trực tiếp với số lớp (class / 클래스) trong HTML** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 157. màu cưỡng bức (forced colors)

độ tương phản cao (high contrast)/màu cưỡng bức (forced colors) chế độ (mode / 모드) có thể override colors.

Tailwind có forced-color related các biến thể (variants)/các tiện ích (utilities). Default nên cho trình duyệt (browser / 브라우저) adapt.

Chỉ dùng `forced-color-adjust-none` targeted khi automatic override thực sự làm mất meaning.

---

# PHẦN XX — hiệu năng (performance / 성능) VÀ gỡ lỗi (debugging)

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **158. Tailwind CSS đầu ra (output / 출력) không tỷ lệ trực tiếp với số lớp (class / 클래스) trong HTML** tiếp nhận điểm tựa từ **157. màu cưỡng bức (forced colors)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **159. giá trị tùy ý (arbitrary value) cardinality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 158. Tailwind CSS đầu ra (output / 출력) không tỷ lệ trực tiếp với số lớp (class / 클래스) trong HTML

Nếu 100 buttons đều có `px-4`, generated CSS chỉ cần một `.px-4` tiện ích (utility) quy tắc (rule / 규칙), không phải 100 copies.

Điều làm CSS tăng là số **unique candidates** và các biến thể (variants).

Ví dụ:

```text
bg-red-500
hover:bg-red-500
md:bg-red-500
dark:bg-red-500
```

là các generated contexts khác nhau.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **159. giá trị tùy ý (arbitrary value) cardinality** tiếp nhận điểm tựa từ **158. Tailwind CSS đầu ra (output / 출력) không tỷ lệ trực tiếp với số lớp (class / 클래스) trong HTML** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **160. Monorepo scanning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 159. giá trị tùy ý (arbitrary value) cardinality

Một:

```text
w-[317px]
```

không phải hiệu năng (performance / 성능) disaster.

Nhưng nếu dữ liệu (data / 데이터) tạo:

```text
w-[1px]
w-[2px]
...
w-[1000px]
```

thì bạn có hàng nghìn unique rules.

Động (dynamic / 동적) numeric dữ liệu (data / 데이터) nên dùng CSS biến (variable).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **160. Monorepo scanning** tiếp nhận điểm tựa từ **159. giá trị tùy ý (arbitrary value) cardinality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **161. gỡ lỗi (debug / 디버그) lớp (class / 클래스) không được generate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 160. Monorepo scanning

Không scan cả monorepo khổng lồ nếu app chỉ dùng một phần.

Use:
- `source()`,
- `@source`,
- `@source not`,
- `source(none)`.

phát hiện nguồn (source detection) không chỉ là cấu hình (config / 설정); nó là bundle quyền sở hữu (ownership / 소유권) kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **161. gỡ lỗi (debug / 디버그) lớp (class / 클래스) không được generate** tiếp nhận điểm tựa từ **160. Monorepo scanning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **162. gỡ lỗi (debug / 디버그) lớp (class / 클래스) có quy tắc (rule / 규칙) nhưng UI sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 161. gỡ lỗi (debug / 디버그) lớp (class / 클래스) không được generate

Hỏi lần lượt:

```text
Class có xuất hiện complete trong source không?
File có được scan không?
File có nằm node_modules/ignored path không?
Có cần @source không?
Utility có tồn tại ở v4.3 không?
Theme token cần thiết có tồn tại không?
Custom @utility có được register không?
```

Nếu generated CSS không có quy tắc (rule / 규칙), chưa cần gỡ lỗi (debug / 디버그) trình duyệt (browser / 브라우저) bố cục (layout / 레이아웃).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **162. gỡ lỗi (debug / 디버그) lớp (class / 클래스) có quy tắc (rule / 규칙) nhưng UI sai** tiếp nhận điểm tựa từ **161. gỡ lỗi (debug / 디버그) lớp (class / 클래스) không được generate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **163. Tailwind + React** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 162. gỡ lỗi (debug / 디버그) lớp (class / 클래스) có quy tắc (rule / 규칙) nhưng UI sai

Khi DevTools cho thấy tiện ích (utility) CSS tồn tại, chuyển mô hình tư duy (mental model / 사고 모델) sang CSS:

```text
computed style
cascade/layer
specificity
parent layout
min/max sizing
overflow
stacking context
browser support
```

Đây là ranh giới giữa Tailwind gỡ lỗi (debugging) và CSS gỡ lỗi (debugging).

---

# PHẦN XXI — TAILWIND + FRAMEWORKS

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **163. Tailwind + React** tiếp nhận điểm tựa từ **162. gỡ lỗi (debug / 디버그) lớp (class / 클래스) có quy tắc (rule / 규칙) nhưng UI sai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **164. Tailwind + Vue/Svelte** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 163. Tailwind + React

React dùng `className`.

Static ánh xạ (mapping / 매핑) mẫu (pattern / 패턴):

```jsx
const sizeClasses = {
  sm: "px-3 py-1.5 text-sm",
  md: "px-4 py-2 text-base",
  lg: "px-5 py-3 text-lg",
};
```

Tránh thời gian chạy (runtime / 런타임) lớp (class / 클래스) synthesis.

Extract thành phần (component / 컴포넌트) khi combination lặp lại.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **164. Tailwind + Vue/Svelte** tiếp nhận điểm tựa từ **163. Tailwind + React** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **165. Tailwind + CSS Modules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 164. Tailwind + Vue/Svelte

các tiện ích (utilities) trong template hoạt động tương tự HTML.

Nếu dùng component-scoped `<style>` và `@apply`, bạn có thể cần `@reference` để Tailwind biết theme/custom APIs của biểu định kiểu (stylesheet / 스타일시트) chính.

Nhưng đừng dùng scoped CSS + `@apply` chỉ để thay một color; CSS biến (variable) trực tiếp thường đơn giản hơn.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **165. Tailwind + CSS Modules** tiếp nhận điểm tựa từ **164. Tailwind + Vue/Svelte** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **166. Tailwind + SCSS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 165. Tailwind + CSS Modules

Bạn có thể dùng Tailwind trong markup và CSS Modules cho bộ chọn (selector) phức tạp/cục bộ (local / 로컬) style.

Không có luật bắt buộc phải chọn một trong hai.

Nhưng nếu cùng một concern được bọc qua:

```text
CSS Module
→ @apply
→ Tailwind utility
→ theme token
```

chỉ để đặt một `color`, lớp trừu tượng (abstraction / 추상화) đã quá nhiều.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **166. Tailwind + SCSS** tiếp nhận điểm tựa từ **165. Tailwind + CSS Modules** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **167. Tư duy chuyển đổi (migration)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 166. Tailwind + SCSS

Tailwind v4 là ưu tiên CSS (CSS-first), nên nhiều dự án (project / 프로젝트) Tailwind-heavy không còn cần SCSS.

Nếu vẫn dùng SCSS, phân trách nhiệm rõ:

```text
Tailwind
→ utilities, variants, theme API

SCSS
→ compile-time maps/functions/mixins nếu project thực sự cần
```

Đừng maintain cùng một color đơn vị từ (token / 토큰) độc lập ở:
- Sass map khóa–giá trị (map),
- Tailwind `@theme`,
- CSS `:root`
cùng lúc.

---

# PHẦN XXII — chuyển đổi (migration) TỪ V3

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **167. Tư duy chuyển đổi (migration)** tiếp nhận điểm tựa từ **166. Tailwind + SCSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **168. @config** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 167. Tư duy chuyển đổi (migration)

V3:

```text
tailwind.config.js
content
theme.extend
plugin
safelist
```

V4 hướng tới:

```text
@theme
automatic source detection
@source
@utility
@custom-variant
@source inline()
```

chuyển đổi (migration) không chỉ đổi cú pháp (syntax / 문법); nó là cơ hội gom cấu hình (configuration / 구성) về ưu tiên CSS (CSS-first) kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **168. @config** tiếp nhận điểm tựa từ **167. Tư duy chuyển đổi (migration)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **169. @plugin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 168. `@config`
Phần này nối mạch bài học với “168. `@config`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@config "../../tailwind.config.js";
```

cho phép dùng legacy JS cấu hình (config / 설정) trong v4 chuyển đổi (migration).

Nó là cầu nối (bridge / 브리지), không nhất thiết là mục tiêu (target / 대상) cuối cho greenfield dự án (project / 프로젝트).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **169. @plugin** tiếp nhận điểm tựa từ **168. @config** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **170. Important cú pháp (syntax / 문법)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 169. `@plugin`
Phần này nối mạch bài học với “169. `@plugin`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@plugin "@tailwindcss/typography";
```

dùng legacy plugin ecosystem khi cần.

Project-owned simple custom tiện ích (utility)/biến thể (variant) nên cân nhắc API ưu tiên CSS (CSS-first) trước.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **170. Important cú pháp (syntax / 문법)** tiếp nhận điểm tựa từ **169. @plugin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **171. Page container** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 170. Important cú pháp (syntax / 문법)

V4 preferred:

```text
flex!
bg-red-500!
```

thay vì old leading `!` style trong mã (code / 코드) cũ.

---

# PHẦN XXIII — các mẫu dùng trong môi trường vận hành (production / 운영 환경) (production patterns)

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **171. Page container** tiếp nhận điểm tựa từ **170. Important cú pháp (syntax / 문법)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **172. Stack** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 171. Page container
Phần này nối mạch bài học với “171. Page container”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  class="
    mx-auto
    w-full
    max-w-7xl
    px-4
    sm:px-6
    lg:px-8
  "
>
```

Đây là composition của:
- fluid width,
- max ràng buộc (constraint / 제약조건),
- centering,
- responsive gutters.

Bạn không cần `.container-custom` nếu mẫu (pattern / 패턴) chỉ dùng vài nơi, nhưng nếu app có universal page shell thì extract thành phần (component / 컴포넌트) là hợp lý.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **172. Stack** tiếp nhận điểm tựa từ **171. Page container** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **173. Cluster** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 172. Stack
Phần này nối mạch bài học với “172. Stack”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="flex flex-col gap-4">
```

Ngăn xếp (stack / 스택) là vertical composition thành phần nguyên thủy (primitive / 기본 요소).

Use cho:
- form,
- settings section,
- card body.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **173. Cluster** tiếp nhận điểm tựa từ **172. Stack** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **174. Responsive card grid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 173. Cluster
Phần này nối mạch bài học với “173. Cluster”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="flex flex-wrap items-center gap-2">
```

Cluster là inline-like flexible group.

Use cho:
- tags,
- actions,
- filters,
- toolbar.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **174. Responsive card grid** tiếp nhận điểm tựa từ **173. Cluster** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **175. Sticky app header** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 174. Responsive card grid
Phần này nối mạch bài học với “174. Responsive card grid”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  class="
    grid
    grid-cols-1
    gap-6
    sm:grid-cols-2
    lg:grid-cols-3
  "
>
```

Simple viewport-responsive grid.

Nếu thành phần (component / 컴포넌트) ngữ cảnh (context / 맥락) thay đổi mạnh, cân nhắc truy vấn vùng chứa (container query) hoặc intrinsic auto-fit grid.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **175. Sticky app header** tiếp nhận điểm tựa từ **174. Responsive card grid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **176. Dialog shell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 175. Sticky app header
Phần này nối mạch bài học với “175. Sticky app header”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<header
  class="
    sticky
    top-0
    z-40
    border-b
    border-gray-200
    bg-white/90
    backdrop-blur
  "
>
```

Cấp cao (senior / 시니어) checks:
- sticky vùng chứa cuộn (scroll container),
- backdrop hiệu năng (performance / 성능),
- z-index đặc tả hợp đồng (contract / 계약),
- dark chế độ (mode / 모드) đơn vị từ (token / 토큰).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **176. Dialog shell** tiếp nhận điểm tựa từ **175. Sticky app header** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **177. Form field** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 176. Dialog shell

Use bản địa (native / 네이티브) `<dialog>` hoặc accessible dialog thành phần nguyên thủy (primitive / 기본 요소).

```html
<dialog
  class="
    m-auto
    max-h-[80dvh]
    w-[min(90vw,40rem)]
    overflow-auto
    rounded-2xl
    bg-white
    p-0
    shadow-2xl
    backdrop:bg-black/50
  "
>
```

Tailwind style không tự cung cấp quản lý tiêu điểm (focus management) hay ứng dụng (application / 애플리케이션) trạng thái (state / 상태). hành vi (behavior / 동작) vẫn thuộc bản địa (native / 네이티브)/nền tảng (platform / 플랫폼)/thành phần (component / 컴포넌트) tầng (layer / 계층).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **177. Form field** tiếp nhận điểm tựa từ **176. Dialog shell** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **178. Truncated row** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 177. Form field
Phần này nối mạch bài học với “177. Form field”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<label class="grid gap-1.5">
  <span class="text-sm font-medium">
    Email
  </span>

  <input
    type="email"
    class="
      rounded-lg
      border
      border-gray-300
      px-3
      py-2
      outline-none
      transition
      focus:border-blue-500
      focus:ring-2
      focus:ring-blue-500/20
      user-invalid:border-red-500
      disabled:bg-gray-100
      disabled:text-gray-500
    "
  >
</label>
```

Mỗi lớp (class / 클래스) có responsibility rõ: box, spacing, focus, kiểm tra hợp lệ (validation / 검증), disabled.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **178. Truncated row** tiếp nhận điểm tựa từ **177. Form field** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **179. Khi nào dùng tiện ích (utility), giá trị tùy ý (arbitrary value), theme, custom CSS?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 178. Truncated row
Phần này nối mạch bài học với “178. Truncated row”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="flex items-center gap-3">
  <img
    class="
      size-10
      shrink-0
      rounded-full
      object-cover
    "
  >

  <div class="min-w-0 flex-1">
    <p class="truncate font-medium">
      Long customer name...
    </p>
  </div>

  <button class="shrink-0">
    ...
  </button>
</div>
```

Đây là mẫu (pattern / 패턴) môi trường vận hành (production / 운영 환경) bạn nên thuộc vì nó kết hợp đúng định cỡ nội tại (intrinsic sizing / 내재 크기 결정) và flex hành vi (behavior / 동작).

---

# PHẦN XXIV — TƯ DUY cấp cao (senior / 시니어)

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **179. Khi nào dùng tiện ích (utility), giá trị tùy ý (arbitrary value), theme, custom CSS?** tiếp nhận điểm tựa từ **178. Truncated row** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **180. Tailwind không thay hệ thống thiết kế (design system)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 179. Khi nào dùng tiện ích (utility), giá trị tùy ý (arbitrary value), theme, custom CSS?

Dùng cốt lõi (core / 핵심) tiện ích (utility) khi concern đã có vocabulary chuẩn:

```text
flex
gap-4
rounded-lg
```

Dùng giá trị tùy ý (arbitrary value) khi giá trị (value / 값) thực sự one-off:

```text
top-[117px]
```

Dùng `@theme` khi giá trị (value / 값) lặp lại và thuộc thiết kế (design / 설계) vocabulary:

```text
--radius-card
--color-action
```

Dùng CSS biến (variable) khi giá trị (value / 값) phải thay đổi thời gian chạy (runtime / 런타임).

Dùng `@utility` khi muốn thêm atomic reusable tiện ích (utility) family.

Dùng plain CSS khi bộ chọn (selector)/hành vi (behavior / 동작) đọc dễ hơn bằng CSS.

Dùng thành phần (component / 컴포넌트) lớp trừu tượng (abstraction / 추상화) khi cấu trúc (structure / 구조) + style + trạng thái (state / 상태) lặp lại.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **180. Tailwind không thay hệ thống thiết kế (design system)** tiếp nhận điểm tựa từ **179. Khi nào dùng tiện ích (utility), giá trị tùy ý (arbitrary value), theme, custom CSS?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **181. Tailwind cấp cao (senior / 시니어) phải biết khi nào không dùng Tailwind** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 180. Tailwind không thay hệ thống thiết kế (design system)

Tailwind cho rất nhiều lớp (class / 클래스), nhưng một sản phẩm (product / 제품) tốt vẫn cần quyết định:
- color roles,
- typography quy mô (scale / 규모),
- spacing rhythm,
- border radius,
- shadows,
- thành phần (component / 컴포넌트) các biến thể (variants),
- các trạng thái (states).

Nếu mọi nhà phát triển (developer / 개발자) tùy ý chọn `blue-500`, `blue-600`, `indigo-500`, `violet-600`, Tailwind vẫn compile hoàn hảo nhưng thiết kế (design / 설계) không nhất quán.

Khung phần mềm (framework / 프레임워크) là công cụ (tool / 도구); thiết kế (design / 설계) quản trị (governance / 거버넌스) là kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **181. Tailwind cấp cao (senior / 시니어) phải biết khi nào không dùng Tailwind** tiếp nhận điểm tựa từ **180. Tailwind không thay hệ thống thiết kế (design system)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **182. Beginner phase** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 181. Tailwind cấp cao (senior / 시니어) phải biết khi nào không dùng Tailwind

Một bộ chọn (selector):

```css
.rich-text
  > h2
  + p:first-letter {
  ...
}
```

có thể rõ hơn rất nhiều so với biến thể tùy ý (arbitrary variant) dài.

Một third-party editor có hàng chục nội bộ (internal / 내부) các bộ chọn (selectors) nên có tích hợp (integration / 통합) biểu định kiểu (stylesheet / 스타일시트).

Một custom CSS animation phức tạp có thể rõ hơn 20 các tiện ích (utilities).

Cấp cao (senior / 시니어) Tailwind không theo ideology “không được viết CSS”. cấp cao (senior / 시니어) chọn biểu diễn (representation / 표현) dễ hiểu, dễ kiểm thử (test / 테스트) và dễ maintain nhất.

---

# PHẦN XXV — ROADMAP HỌC

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **182. Beginner phase** tiếp nhận điểm tựa từ **181. Tailwind cấp cao (senior / 시니어) phải biết khi nào không dùng Tailwind** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **183. Intermediate phase** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 182. Beginner phase

Ở giai đoạn đầu, hãy tập trung bố cục (layout / 레이아웃) và visual foundation. Bạn cần có thể nhìn một mockup và tự viết được spacing, sizing, typography, color, border, Flexbox, Grid và responsive các biến thể (variants) mà không liên tục bản sao (copy / 복사) từ example.

Một bài tập tốt là bản dựng (build / 빌드) ba thành phần (component / 컴포넌트) từ đầu: profile card, navbar và login form. Không dùng thành phần (component / 컴포넌트) thư viện (library / 라이브러리). Sau đó resize vùng nhìn (viewport) và sửa overflow bằng chính kiến thức sizing đã học.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **183. Intermediate phase** tiếp nhận điểm tựa từ **182. Beginner phase** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **184. cấp cao (senior / 시니어) phase** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 183. Intermediate phase

Sau khi basic các tiện ích (utilities) đã tự nhiên, học:
- các giá trị tùy ý (arbitrary values),
- group/peer/has,
- dark chế độ (mode / 모드),
- các truy vấn vùng chứa (container queries),
- `@theme`,
- phát hiện nguồn (source detection),
- thành phần (component / 컴포넌트) các biến thể (variants).

Ở giai đoạn này mục tiêu không còn là “làm cho đẹp”, mà là tạo thành phần (component / 컴포넌트) reusable trong nhiều ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **184. cấp cao (senior / 시니어) phase** tiếp nhận điểm tựa từ **183. Intermediate phase** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **185. Kiểm tra kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 184. cấp cao (senior / 시니어) phase

Cấp cao (senior / 시니어) cần thiết kế:
- mang tính ngữ nghĩa (semantic / 의미적) thành phần (component / 컴포넌트) APIs,
- theme/đơn vị từ (token / 토큰) vocabulary,
- nguồn (source / 소스) quyền sở hữu (ownership / 소유권),
- monorepo/gói (package / 패키지) tích hợp (integration / 통합),
- khả năng tiếp cận (accessibility / 접근성) các trạng thái (states),
- thời gian chạy (runtime / 런타임) CSS biến (variable) cầu nối (bridge / 브리지),
- custom các tiện ích (utilities)/các biến thể (variants),
- CSS kiến trúc (architecture / 아키텍처).

Bạn cũng phải đọc DevTools generated CSS và giải thích vì sao một tiện ích (utility) đang thắng/thua trong cơ chế phân tầng (cascade).

---

# PHẦN XXVI — SELF kiểm thử (test / 테스트)

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **185. Kiểm tra kiến thức** tiếp nhận điểm tựa từ **184. cấp cao (senior / 시니어) phase** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **186. Đọc Tailwind theo CSS subsystem, không theo danh sách lớp (class / 클래스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 185. Kiểm tra kiến thức

Sau khi học xong, bạn nên tự trả lời được bằng lời của mình: Tailwind khác inline style ở điểm nào; tại sao động (dynamic / 동적) lớp (class / 클래스) string có thể không được generate; `@theme` khác normal CSS biến (variable) ra sao; tại sao `min-w-0` sửa ellipsis trong Flexbox; tại sao `md:` và `@md:` là hai loại responsive điều kiện (condition / 조건) khác nhau; `group`, `peer`, `has` khác nhau theo bộ chọn (selector) relationship ra sao; `aria-*` và `data-*` nên dùng cho loại trạng thái (state / 상태) nào; khi nào giá trị tùy ý (arbitrary value) nên trở thành đơn vị từ (token / 토큰); tại sao HTML lớp (class / 클래스) thứ tự (order / 순서) không tự quyết định CSS winner; `@utility`, `@custom-variant`, `@apply`, `@reference` giải quyết các vấn đề khác nhau thế nào; và khi nào plain CSS tốt hơn Tailwind.

Nếu bạn chỉ nhớ lớp (class / 클래스) nhưng không trả lời được “CSS bên dưới đang làm gì?”, bạn chưa đạt cấp cao (senior / 시니어). Nếu bạn có thể dự đoán hành vi (behavior / 동작), thiết kế API thành phần (component / 컴포넌트), gỡ lỗi (debug / 디버그) generated CSS và chọn đúng lớp trừu tượng (abstraction / 추상화), bạn đã có nền Tailwind rất mạnh.

---

# PHẦN XXVII — TÀI LIỆU CHÍNH THỨC

Tailwind CSS documentation:

https://tailwindcss.com/docs

Tailwind v4.3 bản phát hành (release / 릴리스):

https://tailwindcss.com/blog/tailwindcss-v4-3

các biến chủ đề (theme variables):

https://tailwindcss.com/docs/theme

phát hiện nguồn (source detection):

https://tailwindcss.com/docs/detecting-classes-in-source-files

các hàm (functions) and directives:

https://tailwindcss.com/docs/functions-and-directives

thiết kế đáp ứng (responsive design) and các truy vấn vùng chứa (container queries):

https://tailwindcss.com/docs/responsive-design

các trạng thái (states) and các biến thể (variants):

https://tailwindcss.com/docs/hover-focus-and-other-states

Upgrade guide:

https://tailwindcss.com/docs/upgrade-guide

---

---

# PHẦN XXVIII — UNDERLYING CSS ánh xạ (mapping / 매핑) VÀ phiên bản (version / 버전) EVOLUTION

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **186. Đọc Tailwind theo CSS subsystem, không theo danh sách lớp (class / 클래스)** tiếp nhận điểm tựa từ **185. Kiểm tra kiến thức** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **187. ánh xạ (mapping / 매핑) môi trường vận hành (production / 운영 환경) bug từ Tailwind về CSS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 186. Đọc Tailwind theo CSS subsystem, không theo danh sách lớp (class / 클래스)

Tailwind chỉ dễ master khi lớp (class / 클래스) names được quy về CSS subsystem bên dưới. Khi thấy `flex items-center gap-4`, đừng dịch từng đơn vị từ (token / 토큰) rồi dừng lại. Hãy đọc: element trở thành flex ngữ cảnh định dạng (formatting context / 서식 컨텍스트); direct children là các phần tử Flex (flex items); cross-axis alignment dùng `align-items:center`; spacing giữa items do `gap`; main-axis hành vi (behavior / 동작) vẫn phụ thuộc `flex-direction`, item basis/grow/shrink và không gian khả dụng (available space).

Tương tự, `grid grid-cols-[16rem_minmax(0,1fr)]` không phải “hai lớp (class / 클래스) bố cục (layout / 레이아웃)”. Nó tạo Grid ngữ cảnh định dạng (formatting context / 서식 컨텍스트) và một tường minh (explicit / 명시적) two-track template. nhánh học (track / 트랙) thứ hai dùng `minmax(0,1fr)` để bỏ automatic intrinsic minimum của plain flexible nhánh học (track / 트랙) trong nhiều overflow cases. Nếu main content vẫn overflow, bạn tiếp tục kiểm nested grid/phần tử Flex (flex item) min-size chứ không tìm “Tailwind overflow lớp (class / 클래스)” ngẫu nhiên.

`relative`/`absolute` phải đọc bằng khối chứa tham chiếu (containing block / 컨테이닝 블록). `sticky top-0` phải đọc bằng vùng chứa cuộn (scroll container) + sticky inset + available scroll phạm vi (range / 범위). `truncate` phải đọc như `overflow:hidden + text-overflow:ellipsis + white-space:nowrap`, và trong Flex/Grid bạn còn phải đảm bảo item có thể co, thường bằng `min-w-0`. `h-dvh` phải đọc như động (dynamic / 동적) vùng nhìn (viewport) sizing chứ không phải một Tailwind-specific full-screen chế độ (mode / 모드).

các biến thể trạng thái (state variants) cũng là CSS transformations. `hover:bg-*` tạo hover bộ chọn (selector); `focus-visible:*` dùng lớp giả (pseudo-class) cho keyboard-like focus indication; `group-hover:*` tạo ancestor-state bộ chọn (selector) relationship; `peer-invalid:*` dựa subsequent sibling quan hệ (relation / 관계); `has-*` dùng `:has()` relationship. Responsive các biến thể (variants) tạo at-rule conditions: `md:*` là vùng nhìn (viewport) truy vấn môi trường (media query), còn `@md:*` là truy vấn vùng chứa (container query). Khi biến thể (variant) không chạy, hãy gỡ lỗi (debug / 디버그) relationship/điều kiện (condition / 조건) trước khi đổi tiện ích (utility).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **187. ánh xạ (mapping / 매핑) môi trường vận hành (production / 운영 환경) bug từ Tailwind về CSS** tiếp nhận điểm tựa từ **186. Đọc Tailwind theo CSS subsystem, không theo danh sách lớp (class / 클래스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **188. Tailwind phiên bản (version / 버전) evolution — thay đổi programming mô hình (model / 모델), không chỉ thêm tiện ích (utility)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 187. ánh xạ (mapping / 매핑) môi trường vận hành (production / 운영 환경) bug từ Tailwind về CSS

Một bug Tailwind nên được phân loại thành hai nửa. Nếu lớp (class / 클래스) candidate không xuất hiện trong đầu ra (output / 출력), vấn đề nằm ở phát hiện nguồn (source detection), không gian tên chủ đề (theme namespace), tiện ích (utility) registration hoặc động (dynamic / 동적) string construction. Nếu generated quy tắc (rule / 규칙) có mặt và khai báo (declaration) apply nhưng UI vẫn sai, vấn đề đã chuyển sang CSS/trình duyệt (browser / 브라우저).

```text
Tailwind/build side
candidate → source scan → resolver/theme/variant → generated rule

Browser side
generated rule → cascade → computed value → formatting context → layout → paint/composite
```

Ví dụ `z-50` có trong computed style nhưng dropdown vẫn nằm dưới header. Tailwind đã hoàn thành nhiệm vụ; nguyên nhân gốc (root cause / 근본 원인) có thể là parent ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) hoặc top-layer hành vi (behavior / 동작). `w-full` apply nhưng panel vẫn quá rộng; nguyên nhân gốc (root cause / 근본 원인) có thể là khối chứa tham chiếu (containing block / 컨테이닝 블록), padding, min-content hoặc flex minimum. `md:flex-row` có CSS quy tắc (rule / 규칙) nhưng bố cục (layout / 레이아웃) vẫn column; kiểm media điều kiện (condition / 조건), competing `flex-col`, tầng (layer / 계층)/cơ chế phân tầng (cascade) và thành phần (component / 컴포넌트) trạng thái (state / 상태).

Cách gỡ lỗi (debug / 디버그) này giúp bạn không đổ mọi lỗi styling cho khung phần mềm (framework / 프레임워크).

> **Chuyển mạch:** Trong **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **188. Tailwind phiên bản (version / 버전) evolution — thay đổi programming mô hình (model / 모델), không chỉ thêm tiện ích (utility)** tiếp nhận điểm tựa từ **187. ánh xạ (mapping / 매핑) môi trường vận hành (production / 운영 환경) bug từ Tailwind về CSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **189. chuyển đổi (migration) v3 → v4 theo responsibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 188. Tailwind phiên bản (version / 버전) evolution — thay đổi programming mô hình (model / 모델), không chỉ thêm tiện ích (utility)

Tailwind đời đầu phổ biến ưu tiên tiện ích (utility-first) như một authoring style nhưng generation vẫn gắn nhiều với pre-generated/configured biểu định kiểu (stylesheet / 스타일시트) mindset. Sang thế hệ JIT (biên dịch tức thời), đặc biệt từ giai đoạn v2.x JIT (biên dịch tức thời) rồi v3, Tailwind chuyển mạnh sang **generate các tiện ích (utilities) theo candidates thực sự xuất hiện trong nguồn (source / 소스)**. Hệ quả lập trình quan trọng là các giá trị tùy ý (arbitrary values)/các biến thể (variants) trở nên practical hơn, bản dựng (build / 빌드) đầu ra (output / 출력) dựa usage hơn, và complete static lớp (class / 클래스) strings trở thành đặc tả hợp đồng (contract / 계약) giữa mã nguồn (source code / 소스 코드) với trình biên dịch (compiler / 컴파일러).

Tailwind v3 đưa JIT (biên dịch tức thời) engine thành mặc định và củng cố mô hình tư duy (mental model / 사고 모델) `content → candidates → generated CSS`. cấu hình (config / 설정) vẫn chủ yếu JS-first qua `tailwind.config.js`, `content`, `theme.extend`, plugins và danh sách ép giữ (safelist). Nhiều codebase enterprise hiện tại vẫn ở generation này, nên bạn phải đọc được cả config-driven theme/plugin kiến trúc (architecture / 아키텍처).

Tailwind v4 là thay đổi kiến trúc (architecture / 아키텍처) lớn hơn cú pháp (syntax / 문법). khung phần mềm (framework / 프레임워크) chuyển sang cấu hình ưu tiên CSS (CSS-first configuration): `@import "tailwindcss"`, `@theme`, automatic phát hiện nguồn (source detection), `@source`, ưu tiên CSS (CSS-first) `@utility`/`@custom-variant`, bản địa (native / 네이티브) lớp phân tầng (cascade layer) tích hợp (integration / 통합) và các biến chủ đề (theme variables) trở thành CSS các biến (variables) thực sự. Đây là thay đổi từ “JavaScript cấu hình (config / 설정) điều khiển CSS generator” sang “CSS điểm vào (entrypoint / 진입점) vừa định nghĩa thiết kế (design / 설계) vocabulary vừa điều khiển generator”. Khi migrate, bạn nên thiết kế lại quyền sở hữu (ownership / 소유권) của theme/nguồn (source / 소스)/custom các tiện ích (utilities) thay vì giữ toàn bộ v3 mô hình tư duy (mental model / 사고 모델) qua tính tương thích (compatibility / 호환성) bridges.

Tailwind v4.2 và v4.3 tiếp tục mở rộng API theo CSS nền tảng (platform / 플랫폼) thay vì đổi cốt lõi (core / 핵심) mô hình tư duy (mental model / 사고 모델). v4.2 bổ sung logical thuộc tính (property / 속성) các tiện ích (utilities), `font-features-*` và first-party webpack tích hợp (integration / 통합). v4.3 bổ sung scrollbar các tiện ích (utilities), `@container-size`, `zoom-*`, `tab-*`, stacked/compound `@variant` và default các giá trị (values) cho functional các tiện ích (utilities). Tính đến 21/09/2026, Tailwind blog vẫn liệt kê **v4.3** là bản phát hành (release / 릴리스) khung phần mềm (framework / 프레임워크) mới nhất. Những tính năng (feature / 기능) này quan trọng vì chúng giảm custom plugin/CSS ở edge cases, nhưng cách học vẫn là tiện ích (utility) → CSS cơ chế (mechanism / 메커니즘) → trình duyệt (browser / 브라우저) hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **189. chuyển đổi (migration) v3 → v4 theo responsibility** tiếp nhận điểm tựa từ **188. Tailwind phiên bản (version / 버전) evolution — thay đổi programming mô hình (model / 모델), không chỉ thêm tiện ích (utility)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **190. mẫu dùng trong môi trường vận hành (production / 운영 환경) (production pattern): mang tính ngữ nghĩa (semantic / 의미적) giao diện thành phần (component API), Tailwind là hiện thực (implementation / 구현) detail** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 189. chuyển đổi (migration) v3 → v4 theo responsibility

Đừng migrate bằng ánh xạ (mapping / 매핑) cú pháp (syntax / 문법) một-một. Hãy nhóm theo responsibility. Theme các giá trị (values)/cấu hình (config / 설정) chuyển dần sang `@theme`; nguồn (source / 소스) quyền sở hữu (ownership / 소유권) chuyển từ `content` glob sang automatic detection + `@source` khi cần; simple custom các tiện ích (utilities) chuyển sang `@utility`; repeated bộ chọn (selector) conditions có thể trở thành `@custom-variant`; legacy JS plugins giữ lại qua tính tương thích (compatibility / 호환성) cơ chế (mechanism / 메커니즘) chỉ khi chúng thật sự cần JS lô-gic (logic / 논리).

Sau chuyển đổi (migration), kiểm generated CSS diff, Preflight (lớp reset nền của Tailwind) hành vi (behavior / 동작), biến chủ đề (theme variable) đầu ra (output / 출력), nguồn (source / 소스) gói (package / 패키지) scanning, arbitrary candidates, dark-mode chiến lược (strategy / 전략) và hồi quy giao diện (visual regression). Một dự án (project / 프로젝트) “compile được” nhưng mất lớp (class / 클래스) từ dùng chung (shared / 공유) gói (package / 패키지) vẫn là chuyển đổi (migration) thất bại (fail / 실패).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Beginner → cấp cao (senior / 시니어), bản giải thích đầy đủ**, **190. mẫu dùng trong môi trường vận hành (production / 운영 환경) (production pattern): mang tính ngữ nghĩa (semantic / 의미적) giao diện thành phần (component API), Tailwind là hiện thực (implementation / 구현) detail** tiếp nhận điểm tựa từ **189. chuyển đổi (migration) v3 → v4 theo responsibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 190. mẫu dùng trong môi trường vận hành (production / 운영 환경) (production pattern): mang tính ngữ nghĩa (semantic / 의미적) giao diện thành phần (component API), Tailwind là hiện thực (implementation / 구현) detail

Reusable thành phần (component / 컴포넌트) nên expose `variant="danger"`, `size="md"`, `density="compact"` thay vì `color="red-600"` hoặc `padding="p-4"`. Tailwind classes nằm trong static ánh xạ (mapping / 매핑) để scanner nhìn thấy và để thiết kế (design / 설계) hiện thực (implementation / 구현) có thể thay đổi mà caller không đổi.

Thời gian chạy (runtime / 런타임) các giá trị (values) như progress width, user-selected color hoặc canvas coordinate nên đi qua CSS custom thuộc tính (property / 속성) với static Tailwind bên tiêu thụ (consumer / 소비자). Điều này vừa scanner-safe vừa giữ CSS thời gian chạy (runtime / 런타임) đúng chỗ. Theme lớn nên dùng mang tính ngữ nghĩa (semantic / 의미적) CSS các biến (variables)/tokens thay vì lặp `dark:*` cho mọi thuộc tính (property / 속성) trên mọi thành phần (component / 컴포넌트) khi number of themes tăng.

Khả năng tiếp cận (accessibility / 접근성) vẫn nằm ngoài tiện ích (utility) cú pháp (syntax / 문법): bản địa (native / 네이티브) element/ARIA/trạng thái (state / 상태) ngữ nghĩa (semantics / 의미론) phải đúng trước. Tailwind chỉ style `focus-visible`, `disabled`, `aria-*`, `motion-reduce` và forced-colors paths. hiệu năng (performance / 성능) cũng phải đo unique candidates, nguồn (source / 소스) scan boundaries, duplicate entrypoints và trình duyệt (browser / 브라우저) chi phí kết xuất (rendering cost); ưu tiên tiện ích (utility-first) không tự động làm app nhanh.

---

# KẾT LUẬN

Cách học sai là:

```text
flex = flex
p-4 = padding
bg-blue-500 = blue
```

rồi cố nhớ hàng nghìn lớp (class / 클래스).

Cách học đúng là:

```text
UI requirement
→ CSS behavior cần thiết
→ Tailwind utility biểu diễn behavior đó
→ variants/token/component architecture
```

Khi đạt cấp cao (senior / 시니어), bạn nhìn:

```html
<div class="min-w-0 flex-1 truncate">
```

và không chỉ biết “đây là vài lớp (class / 클래스) Tailwind”. Bạn hiểu rằng Flexbox có kích thước tối thiểu tự động (automatic minimum size), `min-w-0` thay ràng buộc (constraint / 제약조건), `flex-1` nhận không gian khả dụng (available space), còn `truncate` chỉ có thể ellipsis khi box thật sự được phép co.

Đó là mức hiểu Tailwind mà tài liệu này hướng tới.

> **Bàn giao:** Sau **190. mẫu dùng trong môi trường vận hành (production / 운영 환경) (production pattern): mang tính ngữ nghĩa (semantic / 의미적) giao diện thành phần (component API), Tailwind là hiện thực (implementation / 구현) detail**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
