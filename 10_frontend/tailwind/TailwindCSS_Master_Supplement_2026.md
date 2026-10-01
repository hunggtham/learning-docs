# Tailwind CSS — Master Supplement, bản giải thích đầy đủ

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tailwind CSS v4.3: trình biên dịch (compiler / 컴파일러) mô hình (model / 모델), design-system kiến trúc (architecture / 아키텍처), phát hiện nguồn (source detection), custom APIs, chuyển đổi (migration) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Quy ước thuật ngữ Việt–Anh** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Tailwind CSS v4.3: trình biên dịch (compiler / 컴파일러) mô hình (model / 모델), design-system kiến trúc (architecture / 아키텍처), phát hiện nguồn (source detection), custom APIs, chuyển đổi (migration) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)

> tệp (file / 파일) này đọc sau `TailwindCSS_Beginner_to_Senior_2026.md`.
>
> tệp (file / 파일) Beginner → cấp cao (senior / 시니어) giúp bạn dùng Tailwind rất chắc trong môi trường vận hành (production / 운영 환경). tệp (file / 파일) này đi sâu hơn vào những phần mà một Tailwind specialist, design-system engineer hoặc frontend cấp cao (senior / 시니어) cần hiểu khi dự án (project / 프로젝트) lớn lên: Tailwind bản dựng (build / 빌드) engine nhìn nguồn (source / 소스) như thế nào, `@theme` trở thành giao diện công khai (public API) ra sao, custom các tiện ích (utilities) được resolve thế nào, nguồn (source / 소스) boundaries ảnh hưởng bundle như thế nào, vì sao lớp (class / 클래스) xung đột (conflict / 충돌) không thể giải thích bằng thứ tự lớp (class / 클래스) trong HTML, và khi nào Tailwind bắt đầu trở thành một phần của gói (package / 패키지) kiến trúc (architecture / 아키텍처) chứ không chỉ là công cụ styling.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **Tailwind CSS v4.3: trình biên dịch (compiler / 컴파일러) mô hình (model / 모델), design-system kiến trúc (architecture / 아키텍처), phát hiện nguồn (source detection), custom APIs, chuyển đổi (migration) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)** nêu điều cần giải thích; **Quy ước thuật ngữ Việt–Anh** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **1. Tại sao cần một Master Supplement riêng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ Tailwind được diễn đạt bằng tiếng Việt trước rồi giữ từ gốc bên cạnh khi cần đối chiếu. Ví dụ: **mô hình ưu tiên tiện ích (utility-first)**, **tiện ích (utility)**, **biến thể trạng thái (state variant)**, **giá trị tùy ý (arbitrary value)**, **điểm ngắt (breakpoint)**, **truy vấn vùng chứa (container query)**, **phát hiện nguồn (source detection)**, **biên dịch tức thời (JIT, just-in-time)** và **cấu hình ưu tiên CSS (CSS-first configuration)**. Tên lớp (class / 클래스), directive và utility literal trong mã (code / 코드) luôn được giữ nguyên.

# PHẦN I — TỪ “DÙNG TAILWIND” ĐẾN “HIỂU HỆ THỐNG TAILWIND”

> **Chuyển mạch:** Glossary giữ cách gọi ổn định; Master Supplement bắt đầu bằng diagnosis từ utility → generated CSS → browser behavior để giải thích runtime thật.

## 1. Tại sao cần một Master Supplement riêng?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **1A. Master diagnosis: tiện ích (utility) → generated CSS → trình duyệt (browser / 브라우저) hành vi (behavior / 동작)** tiếp nhận điểm tựa từ **1. Tại sao cần một Master Supplement riêng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. Tailwind v4 là một compiler-oriented authoring hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1A. Master diagnosis: tiện ích (utility) → generated CSS → trình duyệt (browser / 브라우저) hành vi (behavior / 동작)

Ở mức (level / 수준) master, một tiện ích (utility) phải dấu vết (trace / 추적) được theo hai chiều. Chiều xuôi bắt đầu từ lớp (class / 클래스) candidate, qua nguồn (source / 소스) scanner, biến thể (variant)/theme resolver, tới generated CSS rồi trình duyệt (browser / 브라우저) bố cục (layout / 레이아웃)/rendering. Chiều ngược bắt đầu từ UI bug trong DevTools, truy computed style và bố cục (layout / 레이아웃) ngữ cảnh (context / 맥락) để tìm candidate/bản dựng (build / 빌드) quy tắc (rule / 규칙) gây hành vi (behavior / 동작).

Ví dụ `min-w-0` resolve thành `min-width: 0`; trình duyệt (browser / 브라우저) dùng giá trị (value / 값) này khi tính minimum inline kích thước (size / 크기) của flex/phần tử Grid (grid item), cho phép item co nhỏ hơn intrinsic content width. Nếu ellipsis hoạt động sau khi thêm `min-w-0`, nguyên nhân là bố cục (layout / 레이아웃) ràng buộc (constraint / 제약조건) thay đổi chứ không phải Tailwind có truncate magic. `md:hover:bg-brand` cũng phải tách thành điểm ngắt (breakpoint) điều kiện (condition / 조건) + hover bộ chọn (selector) + theme color đơn vị từ (token / 토큰). Nếu quy tắc (rule / 규칙) không được generate, gỡ lỗi (debug / 디버그) nguồn (source / 소스)/theme; nếu quy tắc (rule / 규칙) có nhưng inactive, gỡ lỗi (debug / 디버그) conditions; nếu apply nhưng visual vẫn sai, gỡ lỗi (debug / 디버그) cơ chế phân tầng (cascade)/blending/trình duyệt (browser / 브라우저) CSS.

Phiên bản (version / 버전) đường cơ sở (baseline) vẫn là **Tailwind CSS v4.3** tại kiểm tra (audit / 감사) 2026-09-21. Khi migrate v3/early-v4, hãy xem đây là kiến trúc (architecture / 아키텍처) thay đổi (change / 변경): JS config-first → ưu tiên CSS (CSS-first) `@theme`; `content` globs → automatic detection/`@source`; simple custom plugin tiện ích (utility) → `@utility`; repeated bộ chọn (selector) trạng thái (state / 상태) → `@custom-variant` khi phù hợp. chuyển đổi (migration) cần diff generated CSS, trình duyệt (browser / 브라우저) đường cơ sở (baseline) và hồi quy giao diện (visual regression), không chỉ tìm kiếm (search / 검색)/replace cú pháp (syntax / 문법).

Khi mới học Tailwind, vấn đề thường là “lớp (class / 클래스) nào tạo padding?”, “làm responsive thế nào?”, “dark chế độ (mode / 모드) viết ra sao?”. Khi đã làm môi trường vận hành (production / 운영 환경) vài tháng, câu hỏi thay đổi. Bạn bắt đầu gặp những trường hợp (case / 사례) như: lớp (class / 클래스) có trong JSX nhưng CSS không được generate; cùng một thành phần (component / 컴포넌트) hoạt động trong app A nhưng thất bại (fail / 실패) khi được publish thành gói (package / 패키지); một giá trị tùy ý (arbitrary value) nhìn đúng nhưng IntelliSense không hiểu vì không gian tên (namespace / 네임스페이스) ambiguous; `px-2` và `px-4` cùng xuất hiện nhưng lớp (class / 클래스) viết sau trong `className` không thắng; một biểu định kiểu (stylesheet / 스타일시트) dùng `@apply` trong Vue scoped style không nhận custom theme; hoặc một microfrontend import Tailwind làm hỏng reset của host page.

Những vấn đề đó không còn là “học thêm tiện ích (utility)”. Chúng nằm ở ranh giới giữa mã nguồn (source code / 소스 코드), quy trình bản dựng (build / 빌드) (build pipeline), generated CSS và trình duyệt (browser / 브라우저). Vì vậy ở cấp độ master, mô hình tư duy (mental model / 사고 모델) phải mở rộng thành:

```text
Application source
→ Candidate detection
→ Tailwind utility/variant resolution
→ CSS generation
→ Cascade layers
→ Browser style/layout/rendering
```

Mỗi lỗi cần được định vị vào đúng tầng trước khi sửa. Đây là kỹ năng giúp bạn tránh mất hàng giờ thay lớp (class / 클래스) ngẫu nhiên.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **2. Tailwind v4 là một compiler-oriented authoring hệ thống (system / 시스템)** tiếp nhận điểm tựa từ **1A. Master diagnosis: tiện ích (utility) → generated CSS → trình duyệt (browser / 브라우저) hành vi (behavior / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. phát hiện ứng viên lớp (candidate detection) không phải JavaScript evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Tailwind v4 là một compiler-oriented authoring hệ thống (system / 시스템)

Tailwind v4 không nên được hình dung như một tệp (file / 파일) `tailwind.css` chứa sẵn hàng chục nghìn lớp (class / 클래스). Nó hoạt động giống một trình biên dịch (compiler / 컴파일러) chuỗi xử lý (pipeline / 파이프라인): đọc CSS điểm vào (entrypoint / 진입점), đọc các Tailwind directives, phát hiện lớp (class / 클래스) candidates trong nguồn (source / 소스), resolve candidate đó thành tiện ích (utility)/biến thể (variant) và generate CSS cần thiết.

Ví dụ nguồn (source / 소스) có:

```html
<div class="flex gap-4 rounded-xl">
```

Tailwind scanner phát hiện các đơn vị từ (token / 토큰) có khả năng là lớp (class / 클래스). Resolver nhận ra `flex`, `gap-4`, `rounded-xl` là các tiện ích (utilities) hợp lệ. Sau đó Tailwind generate CSS quy tắc (rule / 규칙) tương ứng.

Nếu nguồn (source / 소스) chứa:

```text
something-that-looks-like-a-class
```

nhưng không map khóa–giá trị (map) tới tiện ích (utility) nào, nó bị bỏ qua.

Điểm quan trọng là Tailwind **không cần hiểu ngữ nghĩa (semantics / 의미론) của React thành phần (component / 컴포넌트) hoặc lô-gic nghiệp vụ (business logic / 비즈니스 로직)**. Nó chỉ cần complete candidate strings.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **3. phát hiện ứng viên lớp (candidate detection) không phải JavaScript evaluation** tiếp nhận điểm tựa từ **2. Tailwind v4 là một compiler-oriented authoring hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Static ánh xạ (mapping / 매핑) là một mẫu thiết kế (design pattern / 디자인 패턴) chứ không chỉ workaround** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. phát hiện ứng viên lớp (candidate detection) không phải JavaScript evaluation

Hãy xem mã (code / 코드):

```jsx
const color = "blue";

return (
  <div className={`bg-${color}-600`} />
);
```

Một JavaScript thời gian chạy (runtime / 런타임) có thể dễ dàng evaluate ra `bg-blue-600`. Nhưng Tailwind phát hiện nguồn (source detection) không chạy ứng dụng (application / 애플리케이션) như JavaScript trình thông dịch (interpreter / 인터프리터). Nó nhìn nguồn (source / 소스) như văn bản (text / 텍스트).

Vì string `bg-blue-600` không tồn tại nguyên vẹn trong nguồn (source / 소스), scanner không thể dựa vào thời gian chạy (runtime / 런타임) kiến thức (knowledge / 지식) để generate lớp (class / 클래스) đó.

Cách đúng:

```jsx
const backgroundClasses = {
  blue: "bg-blue-600",
  green: "bg-green-600",
  red: "bg-red-600",
};

return (
  <div className={backgroundClasses[color]} />
);
```

Ở đây các complete candidates tồn tại literal trong nguồn (source / 소스).

Đây không chỉ là limitation của scanner. Nó còn thúc đẩy kiến trúc (architecture / 아키텍처) tốt hơn vì thành phần (component / 컴포넌트) có finite visual API.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **4. Static ánh xạ (mapping / 매핑) là một mẫu thiết kế (design pattern / 디자인 패턴) chứ không chỉ workaround** tiếp nhận điểm tựa từ **3. phát hiện ứng viên lớp (candidate detection) không phải JavaScript evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Automatic phát hiện nguồn (source detection) thực sự mang lại điều gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Static ánh xạ (mapping / 매핑) là một mẫu thiết kế (design pattern / 디자인 패턴) chứ không chỉ workaround

Giả sử Button nhận:

```tsx
<Button variant="danger" />
```

Bạn map khóa–giá trị (map):

```ts
const variants = {
  primary:
    "bg-blue-600 text-white hover:bg-blue-700",

  danger:
    "bg-red-600 text-white hover:bg-red-700",

  secondary:
    "bg-white text-gray-900 ring-1 ring-gray-300",
};
```

Mẫu (pattern / 패턴) này tạo ra ba lợi ích cùng lúc.

Thứ nhất, Tailwind scanner nhìn thấy toàn bộ complete lớp (class / 클래스) names. Thứ hai, TypeScript có thể biến key thành finite union. Thứ ba, bên tiêu thụ (consumer / 소비자) chỉ biết mang tính ngữ nghĩa (semantic / 의미적) biến thể (variant) chứ không phụ thuộc palette hiện thực (implementation / 구현).

Nếu mai thiết kế (design / 설계) đổi `danger` từ `red-600` sang `rose-700`, thành phần (component / 컴포넌트) bên tiêu thụ (consumer / 소비자) không cần sửa.

Ở cấp độ master, bạn nên nhìn static lớp (class / 클래스) ánh xạ (mapping / 매핑) như **giao diện công khai (public API) ranh giới (boundary / 경계)**, không chỉ scanner hack.

---

# PHẦN II — phát hiện nguồn (source detection) NHƯ MỘT PHẦN CỦA kiến trúc (architecture / 아키텍처)

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **4. Static ánh xạ (mapping / 매핑) là một mẫu thiết kế (design pattern / 디자인 패턴) chứ không chỉ workaround** nêu điều cần giải thích; **5. Automatic phát hiện nguồn (source detection) thực sự mang lại điều gì?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. @source không chỉ là “fix lớp (class / 클래스) bị thiếu”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Automatic phát hiện nguồn (source detection) thực sự mang lại điều gì?

Tailwind v4 tự động scan dự án (project / 프로젝트) trong phần lớn setup. Nó cố tình bỏ qua nhiều nguồn không có giá trị cho tiện ích (utility) detection như nhị phân (binary / 이진) files, CSS files, dùng chung (common / 공통) lockfiles, `node_modules` và nhiều đường dẫn (path / 경로) bị ignore bởi Git.

Điều này tốt cho hiệu năng (performance / 성능) và setup đơn giản. Nhưng khi app bắt đầu dùng monorepo hoặc gói (package / 패키지) chứa thành phần (component / 컴포넌트) nguồn (source / 소스), automatic detection không còn đủ.

Ví dụ:

```text
apps/web
packages/ui
```

Nếu `packages/ui` chứa JSX với Tailwind classes nhưng app bản dựng (build / 빌드) không tự scan gói (package / 패키지) đó, CSS cần cho UI gói (package / 패키지) có thể thiếu.

Khi đó nguồn (source / 소스) ranh giới (boundary / 경계) trở thành một phần của kiến trúc bản dựng (build / 빌드).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **5. Automatic phát hiện nguồn (source detection) thực sự mang lại điều gì?** nêu điều cần giải thích; **6. @source không chỉ là “fix lớp (class / 클래스) bị thiếu”** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. cơ sở (base / 기반) đường dẫn (path / 경로) với source()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. `@source` không chỉ là “fix lớp (class / 클래스) bị thiếu”

Bạn có thể register nguồn (source / 소스):

```css
@import "tailwindcss";

@source "../../packages/ui/src";
```

Hoặc phụ thuộc (dependency / 의존성):

```css
@source "../node_modules/@acme/ui-lib";
```

Tư duy beginner là: “lớp (class / 클래스) không generate thì thêm `@source`”.

Tư duy cấp cao (senior / 시니어)/master là: “biểu định kiểu (stylesheet / 스타일시트) này chịu trách nhiệm generate CSS cho nguồn (source / 소스) lĩnh vực (domain / 도메인) nào?”

Một app admin có thể không cần scan storefront. Một storefront bundle không nên generate tiện ích (utility) cho nội bộ (internal / 내부) admin công cụ (tool / 도구). Vì vậy `@source` giúp xác định quyền sở hữu (ownership / 소유권) của CSS bundle.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **6. @source không chỉ là “fix lớp (class / 클래스) bị thiếu”** nêu điều cần giải thích; **7. cơ sở (base / 기반) đường dẫn (path / 경로) với source()** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. @source not và việc loại bỏ source không cần thiết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. cơ sở (base / 기반) đường dẫn (path / 경로) với `source()`

Trong monorepo, bản dựng (build / 빌드) command thường chạy từ gốc (root / 루트):

```text
repo/
├─ apps/
│  ├─ web/
│  └─ admin/
└─ packages/
```

Nếu phát hiện nguồn (source detection) phụ thuộc hiện tại (current / 현재) working directory một cách vô tình, bản dựng (build / 빌드) có thể khác giữa cục bộ (local / 로컬) và CI.

Bạn có thể xác định cơ sở (base / 기반) đường dẫn (path / 경로):

```css
@import "tailwindcss"
  source("../src");
```

Điều này làm nguồn (source / 소스) resolution gần biểu định kiểu (stylesheet / 스타일시트) hơn và predictable hơn.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **7. cơ sở (base / 기반) đường dẫn (path / 경로) với source()** nêu điều cần giải thích; **8. @source not và việc loại bỏ source không cần thiết** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. source(none) và multiple Tailwind bundles** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. `@source not` và việc loại bỏ source không cần thiết
Phần này nối mạch bài học với “8. `@source not` và việc loại bỏ source không cần thiết”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@source not "../src/legacy";
```

Không phải mọi folder chứa HTML/JS đều nên scan.

Một folder legacy lớn có thể:
- không dùng Tailwind,
- chứa strings giống lớp (class / 클래스) khiến candidate noise,
- tăng file-watching/vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용).

Explicitly exclude làm intent rõ và bản dựng (build / 빌드) ranh giới (boundary / 경계) sạch hơn.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **8. @source not và việc loại bỏ source không cần thiết** nêu điều cần giải thích; **9. source(none) và multiple Tailwind bundles** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. danh sách ép giữ (safelist) bằng @source inline()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. `source(none)` và multiple Tailwind bundles

Một app lớn có thể cần:

```text
admin.css
storefront.css
marketing.css
```

Nếu mỗi biểu định kiểu (stylesheet / 스타일시트) automatic scan toàn repo, ba bundle có thể generate nhiều CSS overlap.

Admin:

```css
@import "tailwindcss"
  source(none);

@source "../admin";
@source "../shared";
```

Storefront:

```css
@import "tailwindcss"
  source(none);

@source "../storefront";
@source "../shared";
```

Bây giờ mỗi bundle có tường minh (explicit / 명시적) candidate universe.

Đây là một bước chuyển từ “khung phần mềm (framework / 프레임워크) cấu hình (config / 설정)” sang **asset kiến trúc (architecture / 아키텍처)**.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **9. source(none) và multiple Tailwind bundles** nêu điều cần giải thích; **10. danh sách ép giữ (safelist) bằng @source inline()** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Brace expansion và combinatorial explosion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. danh sách ép giữ (safelist) bằng `@source inline()`

Có những tiện ích (utility) không xuất hiện trong normal nguồn (source / 소스) nhưng bạn vẫn muốn generate.

Ví dụ HTML được tạo bởi hệ thống template bên ngoài biết lớp (class / 클래스) `underline`.

Bạn có thể force candidate bằng `@source inline(...)`.

Điều quan trọng ở cấp độ master là hiểu danh sách ép giữ (safelist) làm tăng **candidate set**. Nếu bạn danh sách ép giữ (safelist) mọi color, điểm ngắt (breakpoint), hover, focus, dark biến thể (variant) “cho chắc”, bạn đang chủ động bỏ usage-driven generation.

danh sách ép giữ (safelist) nên finite và business-driven.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **10. danh sách ép giữ (safelist) bằng @source inline()** nêu điều cần giải thích; **11. Brace expansion và combinatorial explosion** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. biến chủ đề (theme variable) không chỉ là CSS custom thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Brace expansion và combinatorial explosion

Hiện tại (current / 현재) source-inline APIs có khả năng generate ranges/các biến thể (variants) rất mạnh. Nhưng cú pháp (syntax / 문법) mạnh thường dẫn tới abuse.

Nếu bạn generate:

```text
20 colors
× 10 shades
× 5 breakpoints
× 4 states
```

bạn đã tạo hàng nghìn candidates trước khi ứng dụng (application / 애플리케이션) thực sự dùng.

Trình biên dịch (compiler / 컴파일러) làm đúng; kiến trúc (architecture / 아키텍처) sai.

Cấp cao (senior / 시니어) cần luôn hỏi:

```text
Có bao nhiêu candidate thực tế?
Có bao nhiêu CSS rules?
Bundle tăng bao nhiêu?
```

---

# PHẦN III — `@theme` NHƯ công khai (public / 공개) DESIGN-SYSTEM API

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **12. biến chủ đề (theme variable) không chỉ là CSS custom thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **11. Brace expansion và combinatorial explosion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. không gian tên chủ đề (theme namespace) quyết định vocabulary** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. biến chủ đề (theme variable) không chỉ là CSS custom thuộc tính (property / 속성)

Normal CSS:

```css
:root {
  --brand: #2563eb;
}
```

chỉ tạo thời gian chạy (runtime / 런타임) biến (variable).

Tailwind:

```css
@theme {
  --color-brand: #2563eb;
}
```

có hai tác dụng.

Tác dụng đầu tiên là Tailwind trình biên dịch (compiler / 컴파일러) hiểu `brand` thuộc color không gian tên (namespace / 네임스페이스), nên generate APIs như:

```text
bg-brand
text-brand
border-brand
fill-brand
```

Tác dụng thứ hai là CSS biến (variable) theme cũng tồn tại trong generated CSS để trình duyệt (browser / 브라우저) hoặc custom CSS sử dụng.

Vì vậy `@theme` vừa là:
- trình biên dịch (compiler / 컴파일러) cấu hình (configuration / 구성),
- thời gian chạy (runtime / 런타임) đơn vị từ (token / 토큰) khai báo (declaration).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **13. không gian tên chủ đề (theme namespace) quyết định vocabulary** tiếp nhận điểm tựa từ **12. biến chủ đề (theme variable) không chỉ là CSS custom thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Versioning theme vocabulary** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. không gian tên chủ đề (theme namespace) quyết định vocabulary

Nếu bạn tạo:

```css
@theme {
  --radius-card: .75rem;
}
```

bạn đang thêm tiện ích (utility):

```text
rounded-card
```

Nếu tạo:

```css
@theme {
  --breakpoint-wide: 90rem;
}
```

bạn đang tạo responsive vocabulary liên quan điểm ngắt (breakpoint).

Vì thế đơn vị từ (token / 토큰) name trong Tailwind không chỉ là nội bộ (internal / 내부) hiện thực (implementation / 구현). Nó xuất hiện trong markup trên toàn dự án (project / 프로젝트).

Đổi:

```text
--radius-card
```

thành:

```text
--radius-panel
```

có thể yêu cầu sửa hàng trăm `rounded-card`.

Đó là lý do không gian tên chủ đề (theme namespace) là **giao diện công khai (public API)**.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **14. Versioning theme vocabulary** tiếp nhận điểm tựa từ **13. không gian tên chủ đề (theme namespace) quyết định vocabulary** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. thành phần nguyên thủy (primitive / 기본 요소) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) nên coexist thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Versioning theme vocabulary

Nếu hệ thống thiết kế (design system) được publish như gói (package / 패키지), theme đơn vị từ (token / 토큰) rename có thể là breaking thay đổi (change / 변경).

Một mang tính ngữ nghĩa (semantic / 의미적) versioning mindset hợp lý là:
- thêm đơn vị từ (token / 토큰) mới nhưng giữ cũ: thường backward-compatible,
- đổi giá trị (value / 값) nhẹ: có thể visual thay đổi (change / 변경) nhưng không API break,
- xóa/rename đơn vị từ (token / 토큰): API break,
- đổi điểm ngắt (breakpoint) đơn vị từ (token / 토큰): hành vi (behavior / 동작) break rộng.

CSS không có TypeScript trình biên dịch (compiler / 컴파일러) báo mọi bên tiêu thụ (consumer / 소비자) bị vỡ, nên trạng thái ngừng khuyến nghị (deprecation)/versioning càng quan trọng.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **15. thành phần nguyên thủy (primitive / 기본 요소) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) nên coexist thế nào?** tiếp nhận điểm tựa từ **14. Versioning theme vocabulary** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) cần đủ chính xác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. thành phần nguyên thủy (primitive / 기본 요소) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) nên coexist thế nào?

Thành phần nguyên thủy (primitive / 기본 요소):

```text
blue-500
blue-600
gray-100
gray-900
```

mô tả visual quy mô (scale / 규모).

mang tính ngữ nghĩa (semantic / 의미적):

```text
action-bg
action-fg
surface
text-muted
danger-border
```

mô tả role.

Một app nhỏ có thể dùng thành phần nguyên thủy (primitive / 기본 요소) directly:

```text
bg-blue-600
hover:bg-blue-700
```

Một hệ thống thiết kế (design system) nhiều brand/theme thường cần mang tính ngữ nghĩa (semantic / 의미적) tầng (layer / 계층):

```css
:root {
  --action-bg:
    var(--color-blue-600);

  --action-fg:
    var(--color-white);
}
```

Thành phần (component / 컴포넌트):

```html
<button
  class="
    bg-(--action-bg)
    text-(color:--action-fg)
  "
>
```

Điểm mạnh là thành phần (component / 컴포넌트) không còn biết palette hiện thực (implementation / 구현).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **16. đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) cần đủ chính xác** tiếp nhận điểm tựa từ **15. thành phần nguyên thủy (primitive / 기본 요소) và đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) nên coexist thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Reset không gian tên (namespace / 네임스페이스) để enforce hệ thống thiết kế (design system)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) cần đủ chính xác

Một đơn vị từ (token / 토큰):

```text
danger
```

có vẻ mang tính ngữ nghĩa (semantic / 의미적) nhưng quá rộng.

Nếu map khóa–giá trị (map) tới `--color-danger`, Tailwind có thể cho dev viết:

```text
bg-danger
text-danger
border-danger
```

Trong thiết kế (design / 설계) thực tế, danger background có thể là red rất nhạt, văn bản (text / 텍스트) là red đậm, border ở giữa.

Nên vocabulary có thể cần:

```text
danger-bg
danger-fg
danger-border
```

Đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) tốt không phải đơn vị từ (token / 토큰) ít; nó là đơn vị từ (token / 토큰) có role rõ.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **17. Reset không gian tên (namespace / 네임스페이스) để enforce hệ thống thiết kế (design system)** tiếp nhận điểm tựa từ **16. đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) cần đủ chính xác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. chi phí (cost / 비용) của strict theme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Reset không gian tên (namespace / 네임스페이스) để enforce hệ thống thiết kế (design system)

Tailwind mặc định có palette lớn. nhà phát triển (developer / 개발자) rất dễ chọn:

```text
blue-500
indigo-600
violet-500
```

theo cảm tính.

Strict hệ thống (system / 시스템) có thể reset:

```css
@theme {
  --color-*: initial;

  --color-surface: ...;
  --color-text: ...;
  --color-action: ...;
  --color-danger-bg: ...;
  --color-danger-fg: ...;
}
```

Bây giờ các tiện ích (utility) default không được backed bởi đơn vị từ (token / 토큰) sẽ biến mất.

Đây là cách biến Tailwind từ “huge toolbox” thành **constrained thiết kế (design / 설계) ngôn ngữ (language / 언어)**.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **18. chi phí (cost / 비용) của strict theme** tiếp nhận điểm tựa từ **17. Reset không gian tên (namespace / 네임스페이스) để enforce hệ thống thiết kế (design system)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. @theme inline và CSS biến (variable) resolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. chi phí (cost / 비용) của strict theme

Strict theme làm consistency tốt hơn nhưng có chi phí (cost / 비용).

Thành phần (component / 컴포넌트) example từ internet:

```text
bg-slate-100
text-gray-700
```

có thể không hoạt động.

Third-party Tailwind nguồn (source / 소스) gói (package / 패키지) có thể assume default tokens.

Do đó strict không gian tên (namespace / 네임스페이스) phù hợp khi:
- hệ thống thiết kế (design system) đã mature,
- gói (package / 패키지) quyền sở hữu (ownership / 소유권) rõ,
- nhóm (team / 팀) muốn enforce vocabulary.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **19. @theme inline và CSS biến (variable) resolution** tiếp nhận điểm tựa từ **18. chi phí (cost / 비용) của strict theme** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. @theme static** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. `@theme inline` và CSS biến (variable) resolution

Giả sử:

```css
@theme {
  --font-sans:
    var(--font-inter);
}
```

CSS custom các thuộc tính (properties) resolve theo cơ chế phân tầng (cascade)/phạm vi (scope / 범위) của element nơi chúng được dùng. Indirection đôi khi khiến biến (variable) referenced không có giá trị (value / 값) ở phạm vi (scope / 범위) expected.

`@theme inline` cho Tailwind generate tiện ích (utility) với referenced expression trực tiếp hơn:

```css
@theme inline {
  --font-sans:
    var(--font-inter);
}
```

Đây là công cụ để kiểm soát **thời gian chạy (runtime / 런타임) CSS biến (variable) indirection**, không chỉ hiệu năng (performance / 성능) cú pháp (syntax / 문법).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **20. @theme static** tiếp nhận điểm tựa từ **19. @theme inline và CSS biến (variable) resolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. @utility là gì ở mức sâu hơn?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. `@theme static`

Tailwind có thể tối ưu biến chủ đề (theme variable) đầu ra (output / 출력) theo usage.

Nếu một bên ngoài (external / 외부) JavaScript thư viện (library / 라이브러리) cần:

```text
--color-brand
```

nhưng không tiện ích (utility) nào dùng brand trong scanned nguồn (source / 소스), biến (variable) có thể không được emit theo normal usage-driven chiến lược (strategy / 전략).

`@theme static` ép generate đầy đủ theme các khai báo (declarations).

Use:
- theme gói (package / 패키지),
- JS reads tokens,
- documentation công cụ (tool / 도구),
- animation hệ thống (system / 시스템).

Đổi lại CSS đầu ra (output / 출력) lớn hơn.

---

# PHẦN IV — CUSTOM tiện ích (utility) Ở CẤP trình biên dịch (compiler / 컴파일러) API

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **21. @utility là gì ở mức sâu hơn?** tiếp nhận điểm tựa từ **20. @theme static** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. tiện ích (utility) tốt phải “atomic” theo nghĩa mang tính ngữ nghĩa (semantic / 의미적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. `@utility` là gì ở mức sâu hơn?

Simple:

```css
@utility content-auto {
  content-visibility: auto;
}
```

Bạn không chỉ viết một CSS lớp (class / 클래스). Bạn đăng ký một tiện ích (utility) với Tailwind để nó tham gia:
- biến thể (variant) hệ thống (system / 시스템),
- candidate generation,
- tiện ích (utility) sorting.

Use:

```text
content-auto
lg:content-auto
hover:content-auto
```

nếu điều kiện (condition / 조건) hợp lý.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **22. tiện ích (utility) tốt phải “atomic” theo nghĩa mang tính ngữ nghĩa (semantic / 의미적)** tiếp nhận điểm tựa từ **21. @utility là gì ở mức sâu hơn?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Functional tiện ích (utility)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. tiện ích (utility) tốt phải “atomic” theo nghĩa mang tính ngữ nghĩa (semantic / 의미적)

Atomic không có nghĩa đúng một CSS khai báo (declaration) trong mọi trường hợp. Tailwind cốt lõi (core / 핵심) có các tiện ích (utilities) dùng custom các thuộc tính (properties) hoặc nhiều khai báo (declaration) để tạo một tác động (effect / 효과).

Điều quan trọng là tiện ích (utility) biểu diễn **một concern**.

Ví dụ:
- `truncate` có nhiều các khai báo (declarations) nhưng một concern: single-line truncation.
- `ring-2` có hiện thực (implementation / 구현) phức tạp nhưng một concern: ring width.

Một custom tiện ích (utility) tên `dashboard-card-primary` chứa bố cục (layout / 레이아웃), color, hover và typography cùng lúc không còn atomic. Nó là thành phần (component / 컴포넌트).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **23. Functional tiện ích (utility)** tiếp nhận điểm tựa từ **22. tiện ích (utility) tốt phải “atomic” theo nghĩa mang tính ngữ nghĩa (semantic / 의미적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Theme giá trị (value / 값) resolver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Functional tiện ích (utility)
Phần này nối mạch bài học với “23. Functional tiện ích (utility)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Tailwind nhìn candidate `tab-github`, `tab-4` hoặc `tab-[12]`, rồi thử resolver.

Bạn có thể hình dung functional tiện ích (utility) như một mini grammar:

```text
prefix
+ value grammar
+ optional modifier grammar
→ CSS declaration
```

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **24. Theme giá trị (value / 값) resolver** tiếp nhận điểm tựa từ **23. Functional tiện ích (utility)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Bare giá trị (value) resolver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Theme giá trị (value / 값) resolver

Nếu:

```css
@theme {
  --tab-size-github: 8;
}
```

và tiện ích (utility) resolver có:

```css
--value(--tab-size-*)
```

candidate:

```text
tab-github
```

map khóa–giá trị (map) tới theme đơn vị từ (token / 토큰).

Điều này giúp custom tiện ích (utility) family integrate với design-token hệ thống (system / 시스템) thay vì hard-code lookup bảng (table / 테이블) riêng.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **25. Bare giá trị (value) resolver** tiếp nhận điểm tựa từ **24. Theme giá trị (value / 값) resolver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. giá trị tùy ý (arbitrary value) resolver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Bare giá trị (value) resolver
Phần này nối mạch bài học với “25. Bare giá trị (value) resolver”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
--value(integer)
```

cho phép candidate như:

```text
tab-2
tab-4
tab-8
```

resolve trực tiếp integer.

Bare các giá trị (values) nên được giới hạn theo CSS/thuộc tính (property / 속성) ngữ nghĩa (semantics / 의미론). Không phải mọi arbitrary văn bản (text / 텍스트) nên được accepted.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **26. giá trị tùy ý (arbitrary value) resolver** tiếp nhận điểm tựa từ **25. Bare giá trị (value) resolver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Nhiều resolver trong cùng tiện ích (utility)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. giá trị tùy ý (arbitrary value) resolver
Phần này nối mạch bài học với “26. giá trị tùy ý (arbitrary value) resolver”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
--value([integer])
```

cho bracket cú pháp (syntax / 문법).

Tailwind functional tiện ích (utility) có thể hiểu các kiểu (type / 타입) CSS-oriented như:
- length,
- color,
- percentage,
- angle,
- ratio,
- number,
- integer.

Typed giá trị tùy ý (arbitrary value) giúp parser biết bạn muốn gì và tránh ambiguity.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **27. Nhiều resolver trong cùng tiện ích (utility)** tiếp nhận điểm tựa từ **26. giá trị tùy ý (arbitrary value) resolver** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Transform giá trị (value / 값) theo nguồn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Nhiều resolver trong cùng tiện ích (utility)
Phần này nối mạch bài học với “27. Nhiều resolver trong cùng tiện ích (utility)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Tailwind thử các resolution forms theo grammar.

Khi tự thiết kế API, hãy chọn thứ tự (order / 순서)/accepted forms sao cho nhà phát triển (developer / 개발자) dự đoán được. Một tiện ích (utility) quá “thông minh” nhận 10 loại giá trị (value / 값) khác nhau có thể trở nên khó dùng hơn raw CSS.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **27. Nhiều resolver trong cùng tiện ích (utility)** nêu điều cần giải thích; **28. Transform giá trị (value / 값) theo nguồn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **29. Negative custom tiện ích (utility)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Transform giá trị (value / 값) theo nguồn

Bạn có thể cần:
- percentage arbitrary giữ nguyên,
- integer bare chuyển sang percentage,
- theme đơn vị từ (token / 토큰) dùng trực tiếp.

Multiple các khai báo (declarations) với `--value()` có thể được Tailwind resolve selectively.

Đây là tính năng (feature / 기능) dành cho framework-level tiện ích (utility) authoring. Normal app hiếm khi cần custom parser phức tạp.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **28. Transform giá trị (value / 값) theo nguồn** nêu điều cần giải thích; **29. Negative custom tiện ích (utility)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **30. --default() trong v4.3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Negative custom tiện ích (utility)

Tailwind không tự cho rằng mọi thuộc tính (property / 속성) có negative biến thể (variant).

Ví dụ padding không thể âm, opacity không có nghĩa âm.

Nếu custom tiện ích (utility) đại diện inset, bạn có thể đăng ký:
- positive family,
- negative family.

Điều này làm API tường minh (explicit / 명시적) và phù hợp CSS validity.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **30. --default() trong v4.3** tiếp nhận điểm tựa từ **29. Negative custom tiện ích (utility)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Modifier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. `--default()` trong v4.3

Một tiện ích (utility):

```css
@utility tab-* {
  tab-size:
    --value(
      integer,
      --default(4)
    );
}
```

có thể hỗ trợ bare:

```text
tab
```

với default 4.

`tab-2` vẫn tường minh (explicit / 명시적) 2.

Bare default chỉ nên được thêm khi người đọc tiện ích (utility) có thể đoán reasonable meaning. Nếu `surface` không rõ default màu gì, đừng tạo implicit default chỉ vì khung phần mềm (framework / 프레임워크) hỗ trợ (support / 지원).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **31. Modifier** tiếp nhận điểm tựa từ **30. --default() trong v4.3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Custom tiện ích (utility) sorting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Modifier

Một tiện ích (utility):

```text
text-lg/7
```

có:
- main giá trị (value / 값) `lg`,
- modifier `7`.

Modifier phù hợp khi có relationship rõ giữa primary và secondary giá trị (value / 값).

Custom API có thể dùng `--modifier()`, nhưng cấp cao (senior / 시니어) cần tránh cú pháp (syntax / 문법) clever. tiện ích (utility) grammar nên gần cách cốt lõi (core / 핵심) Tailwind được đọc.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **32. Custom tiện ích (utility) sorting** tiếp nhận điểm tựa từ **31. Modifier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. biến thể (variant) không phải văn bản (text / 텍스트) prefix** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Custom tiện ích (utility) sorting

Một hiểu nhầm là custom tiện ích (utility) được cơ chế phân tầng (cascade) đúng theo vị trí bạn viết trong tệp (file / 파일).

Tailwind có utility-layer thứ tự (ordering / 순서)/sorting hành vi (behavior / 동작) riêng để các tiện ích (utilities) compose predictable hơn, và v4 có lô-gic (logic / 논리) liên quan số lượng các thuộc tính (properties) cho custom các tiện ích (utilities).

Do đó:
- không dựa vào thứ tự nguồn (source order) cục bộ (local / 로컬) để giải xung đột (conflict / 충돌),
- inspect generated CSS nếu hành vi (behavior / 동작) quan trọng,
- thành phần (component / 컴포넌트) override nên dùng kiến trúc (architecture / 아키텍처) rõ.

---

# PHẦN V — biến thể (variant) ALGEBRA

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **33. biến thể (variant) không phải văn bản (text / 텍스트) prefix** tiếp nhận điểm tựa từ **32. Custom tiện ích (utility) sorting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. biến thể (variant) stacking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. biến thể (variant) không phải văn bản (text / 텍스트) prefix

`hover:` không chỉ “thêm chữ hover vào lớp (class / 클래스)”. Nó transform CSS bộ chọn (selector).

`md:` không transform bộ chọn (selector), mà wrap quy tắc (rule / 규칙) trong truy vấn môi trường (media query).

`supports-*:` wrap trong `@supports`.

`group-hover:` tạo ancestor relationship.

`peer-invalid:` tạo sibling relationship.

Một biến thể (variant) vì vậy có thể được hiểu như **hàm (function / 함수) biến đổi CSS ngữ cảnh (context / 맥락)**.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **34. biến thể (variant) stacking** tiếp nhận điểm tựa từ **33. biến thể (variant) không phải văn bản (text / 텍스트) prefix** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. @custom-variant là reusable điều kiện (condition / 조건) API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. biến thể (variant) stacking
Phần này nối mạch bài học với “34. biến thể (variant) stacking”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
dark:md:hover:bg-blue-600
```

là composition của ba transformations:
- dark điều kiện (condition / 조건),
- responsive media điều kiện (condition / 조건),
- hover bộ chọn (selector).

Khi stacked biến thể (variant) không chạy, gỡ lỗi (debug / 디버그) từng điều kiện (condition / 조건):
- dark trạng thái (state / 상태) active?
- vùng nhìn (viewport) đạt md?
- thiết bị (device / 장치) hỗ trợ hover?
- element thật sự hover?

Đừng coi toàn lớp (class / 클래스) như một black box.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **35. @custom-variant là reusable điều kiện (condition / 조건) API** tiếp nhận điểm tựa từ **34. biến thể (variant) stacking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Naming custom biến thể (variant)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. `@custom-variant` là reusable điều kiện (condition / 조건) API

Nếu dự án (project / 프로젝트) lặp bộ chọn (selector):

```text
[&:where([data-density=compact] *)]
```

nhiều nơi, hãy tạo:

```css
@custom-variant density-compact
  (&:where([data-density="compact"] *));
```

Markup:

```text
density-compact:py-1
```

Bây giờ thiết kế (design / 설계) vocabulary biểu diễn mang tính ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) thay vì raw bộ chọn (selector).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **36. Naming custom biến thể (variant)** tiếp nhận điểm tựa từ **35. @custom-variant là reusable điều kiện (condition / 조건) API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. @variant trong custom CSS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Naming custom biến thể (variant)

Một dự án (project / 프로젝트) nội bộ có thể dùng:

```text
compact:
midnight:
authenticated:
```

Một design-system gói (package / 패키지) được dùng ngoài dự án (project / 프로젝트) nên cân nhắc không gian tên (namespace / 네임스페이스):

```text
ds-compact:
ds-brand-a:
```

vì Tailwind cốt lõi (core / 핵심) có thể thêm các biến thể (variants) trong tương lai.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **37. @variant trong custom CSS** tiếp nhận điểm tựa từ **36. Naming custom biến thể (variant)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Vì sao class order trong HTML không đảm bảo winner?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. `@variant` trong custom CSS

Bạn đã quyết định custom bộ chọn (selector) là rõ nhất:

```css
.third-party-button {
  ...
}
```

nhưng vẫn muốn dark trạng thái (state / 상태) giống Tailwind:

```css
.third-party-button {
  @variant dark {
    ...
  }
}
```

V4.3 nâng cấp stacked/compound `@variant`, nên Tailwind biến thể (variant) hệ thống (system / 시스템) có thể được reuse bên trong CSS chứ không chỉ markup.

---

# PHẦN VI — cơ chế phân tầng (cascade) VÀ xung đột (conflict / 충돌) Ở MỨC MASTER

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **38. Vì sao class order trong HTML không đảm bảo winner?** tiếp nhận điểm tựa từ **37. @variant trong custom CSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Conflict-aware merge libraries giải quyết vấn đề gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Vì sao class order trong HTML không đảm bảo winner?
Phần này nối mạch bài học với “38. Vì sao class order trong HTML không đảm bảo winner?”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="px-2 px-4">
```

Nhiều người nghĩ `px-4` viết sau nên thắng. Nhưng CSS cơ chế phân tầng (cascade) không biết thứ tự đơn vị từ (token / 토큰) trong lớp (class / 클래스) attribute như thứ tự nguồn (source order) của các khai báo (declarations).

Trình duyệt (browser / 브라우저) nhìn biểu định kiểu (stylesheet / 스타일시트):

```css
.px-2 { ... }
.px-4 { ... }
```

Quy tắc (rule / 규칙) nào được generate ở vị trí/tầng (layer / 계층) nào mới ảnh hưởng thứ tự nguồn (source order).

Vì thế động (dynamic / 동적) lớp (class / 클래스) composition không nên dựa vào string append thứ tự (order / 순서).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **39. Conflict-aware merge libraries giải quyết vấn đề gì?** tiếp nhận điểm tựa từ **38. Vì sao class order trong HTML không đảm bảo winner?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Prettier Tailwind lớp (class / 클래스) sorting không phải xung đột (conflict / 충돌) engine** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Conflict-aware merge libraries giải quyết vấn đề gì?

Trong thành phần (component / 컴포넌트):

```text
base: px-4
caller: px-2
```

Bạn muốn caller override.

Một Tailwind-aware merge helper có thể nhận ra `px-4` và `px-2` thuộc cùng tiện ích (utility) group rồi giữ intended winner trong normalized lớp (class / 클래스) string.

Nó không thay CSS engine; nó xử lý xung đột (conflict / 충돌) trước khi markup kết xuất (render / 렌더링).

Use phù hợp ở reusable thành phần (component / 컴포넌트) thư viện (library / 라이브러리) boundaries.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **40. Prettier Tailwind lớp (class / 클래스) sorting không phải xung đột (conflict / 충돌) engine** tiếp nhận điểm tựa từ **39. Conflict-aware merge libraries giải quyết vấn đề gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. các lớp phân tầng (cascade layers)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Prettier Tailwind lớp (class / 클래스) sorting không phải xung đột (conflict / 충돌) engine

Tailwind-aware formatter sắp lớp (class / 클래스) để readability ổn định.

Nếu formatter đổi thứ tự văn bản (text / 텍스트) mà UI đổi hành vi (behavior / 동작), bạn đang dựa vào một giả định (assumption / 가정) không an toàn. Hãy kiểm tra xung đột (conflict / 충돌)/cơ chế phân tầng (cascade).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **41. các lớp phân tầng (cascade layers)** tiếp nhận điểm tựa từ **40. Prettier Tailwind lớp (class / 클래스) sorting không phải xung đột (conflict / 충돌) engine** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Unlayered CSS có thể gây surprise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. các lớp phân tầng (cascade layers)

Tailwind v4 dùng bản địa (native / 네이티브) layers:

```text
theme
base
components
utilities
```

Một quy tắc (rule / 규칙) trong các tiện ích (utilities) có tầng (layer / 계층) priority cao hơn components trong normal cơ chế phân tầng (cascade).

Điều này cho phép:

```css
@layer components {
  .card {
    padding: 1rem;
  }
}
```

và markup:

```html
<div class="card p-8">
```

tiện ích (utility) override thành phần (component / 컴포넌트) without cuộc chiến độ đặc hiệu (specificity war).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **42. Unlayered CSS có thể gây surprise** tiếp nhận điểm tựa từ **41. các lớp phân tầng (cascade layers)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Per-utility important** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Unlayered CSS có thể gây surprise

Bản địa (native / 네이티브) CSS cơ chế phân tầng (cascade) có hành vi (behavior / 동작) đặc biệt khi layered và unlayered author styles coexist. Normal unlayered quy tắc (rule / 규칙) có thể có priority cao hơn layered normal styles.

Nếu bạn import một vendor CSS unlayered sau/bên cạnh Tailwind, tiện ích (utility) có thể không override như bạn dự đoán.

Cấp cao (senior / 시니어) phải inspect:
- tầng (layer / 계층),
- origin,
- độ đặc hiệu (specificity),
- importance.

Không tăng `!important` ngay.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **43. Per-utility important** tiếp nhận điểm tựa từ **42. Unlayered CSS có thể gây surprise** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. toàn cục (global / 전역) important chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Per-utility important

V4 preferred:

```text
bg-red-500!
```

Use targeted exception.

Nếu bạn dùng important modifier khắp app, bạn đã phá advantage của predictable layered cơ chế phân tầng (cascade).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **44. toàn cục (global / 전역) important chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **43. Per-utility important** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Preflight (lớp reset nền của Tailwind) trong greenfield app** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. toàn cục (global / 전역) important chiến lược (strategy / 전략)

Tailwind có kiến trúc (architecture / 아키텍처) options để generate các tiện ích (utilities) important trong một bundle/import scenario.

Đây có thể là chuyển đổi (migration) công cụ (tool / 도구) khi host legacy CSS cực kỳ specific.

Nhưng toàn cục (global / 전역) important làm:
- third-party override khó,
- thành phần (component / 컴포넌트) theming khó,
- người dùng (user / 사용자) styles tương tác (interaction / 상호작용) phức tạp.

Hãy xem nó như temporary anti-corruption tầng (layer / 계층), không phải default.

---

# PHẦN VII — Preflight (lớp reset nền của Tailwind), EMBEDDING VÀ MICROFRONTENDS

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **45. Preflight (lớp reset nền của Tailwind) trong greenfield app** tiếp nhận điểm tựa từ **44. toàn cục (global / 전역) important chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Preflight (lớp reset nền của Tailwind) trong legacy host** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Preflight (lớp reset nền của Tailwind) trong greenfield app

Trong app mới, Preflight (lớp reset nền của Tailwind) giúp:
- normalize defaults,
- predictable border box/reset hành vi (behavior / 동작),
- Tailwind các tiện ích (utilities) có nền consistent.

Ở đây full import là hợp lý.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **46. Preflight (lớp reset nền của Tailwind) trong legacy host** tiếp nhận điểm tựa từ **45. Preflight (lớp reset nền của Tailwind) trong greenfield app** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Disable Preflight (lớp reset nền của Tailwind) cho embedded widget** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Preflight (lớp reset nền của Tailwind) trong legacy host

Legacy app có thể assume:
- h1 mặc định lớn,
- ul có bullet,
- button có bản địa (native / 네이티브) border,
- body có margin/reset khác.

Import Tailwind Preflight (lớp reset nền của Tailwind) có thể thay đổi toàn host.

Đừng sửa bằng hàng trăm override trước khi xác nhận nguyên nhân gốc (root cause / 근본 원인) là reset collision.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **47. Disable Preflight (lớp reset nền của Tailwind) cho embedded widget** tiếp nhận điểm tựa từ **46. Preflight (lớp reset nền của Tailwind) trong legacy host** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Prefixing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Disable Preflight (lớp reset nền của Tailwind) cho embedded widget

Một widget được inject vào host page nên tránh toàn cục (global / 전역) reset.

Kiến trúc (architecture / 아키텍처) có thể:
- import theme,
- import các tiện ích (utilities),
- omit Preflight (lớp reset nền của Tailwind),
- prefix classes,
- phạm vi (scope / 범위) phát hiện nguồn (source detection).

Mục tiêu là widget không làm thay đổi host typography/forms.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **48. Prefixing** tiếp nhận điểm tựa từ **47. Disable Preflight (lớp reset nền của Tailwind) cho embedded widget** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Microfrontend** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Prefixing

Prefix giúp:
- tránh lớp (class / 클래스) collisions,
- tránh CSS biến (variable) naming collisions tùy import chiến lược (strategy / 전략),
- coexist nhiều Tailwind các hệ thống (systems / 시스템들).

Chi phí (cost / 비용):
- markup dài,
- docs/examples khác tiêu chuẩn (standard / 표준),
- thành phần (component / 컴포넌트) packages phải biết prefix đặc tả hợp đồng (contract / 계약).

Dùng cho cô lập (isolation) yêu cầu (requirement / 요구사항) thật, không phải mặc định.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **49. Microfrontend** tiếp nhận điểm tựa từ **48. Prefixing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. thời gian chạy (runtime / 런타임) dữ liệu (data / 데이터) không nên trở thành thời gian chạy (runtime / 런타임) lớp (class / 클래스) grammar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Microfrontend

Nếu nhiều microfrontend cùng chạy trên một document, ba nguy cơ lớn là:
- nhiều Preflight (lớp reset nền của Tailwind),
- duplicate các biến chủ đề (theme variables),
- tầng (layer / 계층) thứ tự (ordering / 순서) không thống nhất.

Ba chiến lược phổ biến là:
- share một Tailwind/theme bản dựng (build / 빌드),
- mỗi app dùng prefixed isolated bundle,
- Shadow DOM (cây DOM đóng gói) cô lập (isolation).

Không có một đáp án universal; quyết định phụ thuộc triển khai (deployment / 배포) quyền sở hữu (ownership / 소유권).

---

# PHẦN VIII — thời gian chạy (runtime / 런타임) các giá trị (values) VÀ TAILWIND BUILD-TIME

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **49. Microfrontend** nêu điều cần giải thích; **50. thời gian chạy (runtime / 런타임) dữ liệu (data / 데이터) không nên trở thành thời gian chạy (runtime / 런타임) lớp (class / 클래스) grammar** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **51. thời gian chạy (runtime) color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. thời gian chạy (runtime / 런타임) dữ liệu (data / 데이터) không nên trở thành thời gian chạy (runtime / 런타임) lớp (class / 클래스) grammar

API trả về:

```json
{
  "progress": 73
}
```

Bad:

```jsx
className={`w-[${progress}%]`}
```

Good:

```jsx
<div
  style={{ "--progress": `${progress}%` }}
  className="w-(--progress)"
/>
```

Lớp (class / 클래스) remains static, giá trị (value / 값) thời gian chạy (runtime / 런타임).

Đây là một trong những ranh giới (boundary / 경계) mẫu (pattern / 패턴) quan trọng nhất.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **50. thời gian chạy (runtime / 런타임) dữ liệu (data / 데이터) không nên trở thành thời gian chạy (runtime / 런타임) lớp (class / 클래스) grammar** nêu điều cần giải thích; **51. thời gian chạy (runtime) color** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **52. Khi nào inline style vẫn hoàn toàn hợp lý?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. thời gian chạy (runtime) color
Phần này nối mạch bài học với “51. thời gian chạy (runtime) color”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```jsx
<div
  style={{
    "--card-bg": color,
  }}
  className="bg-(--card-bg)"
/>
```

Nếu không gian tên (namespace / 네임스페이스) ambiguous:

```text
text-(color:--text)
```

nói rõ parser ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **52. Khi nào inline style vẫn hoàn toàn hợp lý?** tiếp nhận điểm tựa từ **51. thời gian chạy (runtime) color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. CSP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Khi nào inline style vẫn hoàn toàn hợp lý?

Tailwind không có mục tiêu cấm inline styles.

Động (dynamic / 동적):
- x/y coordinate,
- progress,
- người dùng (user / 사용자) color,
- canvas dimension
có thể hợp lý qua inline custom các thuộc tính (properties).

tiện ích (utility) lớp (class / 클래스) dùng để consume biến (variable) và kết hợp các trạng thái (states)/responsive.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **53. CSP** tiếp nhận điểm tựa từ **52. Khi nào inline style vẫn hoàn toàn hợp lý?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. Utility-pair dark mode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. CSP

Một bảo mật (security / 보안) chính sách (policy / 정책) nghiêm ngặt có thể hạn chế inline style attributes.

Khi đó thời gian chạy (runtime / 런타임) CSS biến (variable) chiến lược (strategy / 전략) cần phối hợp CSP:
- nonce,
- safe biểu định kiểu (stylesheet / 스타일시트) injection,
- predefined lớp (class / 클래스) các trạng thái (states),
tùy app.

Tailwind không bypass Content bảo mật (security / 보안) chính sách (policy / 정책).

---

# PHẦN IX — DARK chế độ (mode / 모드) VÀ MULTI-THEME Ở quy mô (scale / 규모) LỚN

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **54. Utility-pair dark mode** tiếp nhận điểm tựa từ **53. CSP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. Khi dark pairs bắt đầu lặp quá nhiều** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Utility-pair dark mode
Phần này nối mạch bài học với “54. Utility-pair dark mode”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Rất tường minh (explicit / 명시적) và tốt trong app nhỏ/trung bình.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **55. Khi dark pairs bắt đầu lặp quá nhiều** tiếp nhận điểm tựa từ **54. Utility-pair dark mode** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. FOUC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Khi dark pairs bắt đầu lặp quá nhiều

Nếu mọi thành phần (component / 컴포넌트) có 8 cặp:

```text
bg-x dark:bg-y
text-a dark:text-b
border-c dark:border-d
```

và bạn còn brand A, brand B, độ tương phản cao (high contrast), theme seasonal, lớp (class / 클래스) strings phình mạnh.

Lúc đó mang tính ngữ nghĩa (semantic / 의미적) thời gian chạy (runtime / 런타임) tokens có thể tốt hơn:

```css
[data-theme="light"] {
  --surface: ...;
}

[data-theme="dark"] {
  --surface: ...;
}
```

Thành phần (component / 컴포넌트) chỉ:

```text
bg-(--surface)
```

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **56. FOUC** tiếp nhận điểm tựa từ **55. Khi dark pairs bắt đầu lặp quá nhiều** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. ARIA là mang tính ngữ nghĩa (semantic) contract** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. FOUC

Manual theme thường cần JS đọc cục bộ (local / 로컬) lưu trữ (storage / 저장소).

Nếu script chạy sau page paint:
- trình duyệt (browser / 브라우저) kết xuất (render / 렌더링) light,
- JS thêm `.dark`,
- page nhảy dark.

Đây là Flash of Unstyled/Incorrect Theme.

Fix ở initialization/SSR tầng (layer / 계층):
- máy chủ (server / 서버) knows theme,
- early script,
- hệ thống (system / 시스템) preference phương án dự phòng (fallback).

Tailwind generated CSS không thể tự quyết định persisted app preference.

---

# PHẦN X — ARIA, dữ liệu (data / 데이터), GROUP, PEER, HAS Ở MỨC kiến trúc (architecture / 아키텍처)

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **57. ARIA là mang tính ngữ nghĩa (semantic) contract** tiếp nhận điểm tựa từ **56. FOUC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. Data attribute là presentation/application trạng thái (state) hook** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. ARIA là mang tính ngữ nghĩa (semantic) contract
Phần này nối mạch bài học với “57. ARIA là mang tính ngữ nghĩa (semantic) contract”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
aria-expanded
aria-selected
aria-pressed
```

không phải chỉ là convenient CSS các trạng thái (states).

Nếu thành phần (component / 컴포넌트) có true khả năng tiếp cận (accessibility / 접근성) ngữ nghĩa (semantics / 의미론), Tailwind aria biến thể (variant) là tuyệt vời.

Nếu trạng thái (state / 상태) chỉ là “loading skeleton visible”, dùng `data-loading` có thể đúng hơn `aria-*` tùy ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **58. Data attribute là presentation/application trạng thái (state) hook** tiếp nhận điểm tựa từ **57. ARIA là mang tính ngữ nghĩa (semantic) contract** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. Group quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. Data attribute là presentation/application trạng thái (state) hook
Phần này nối mạch bài học với “58. Data attribute là presentation/application trạng thái (state) hook”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  data-state="open"
  class="data-[state=open]:opacity-100"
>
```

JS:

```text
state=open
```

Tailwind:

```text
visual response
```

Đây là separation tốt.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **59. Group quyền sở hữu (ownership / 소유권)** tiếp nhận điểm tựa từ **58. Data attribute là presentation/application trạng thái (state) hook** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. in- convenience vs precision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. Group quyền sở hữu (ownership / 소유권)

`group` là ancestor marker.

Trong nested UIs:

```text
group/card
group/menu
group/tooltip
```

giúp child mục tiêu (target / 대상) đúng ancestor.

Không name groups trong cấu trúc (structure / 구조) phức tạp có thể làm hover/focus style bị kích hoạt bởi ancestor xa.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **60. in- convenience vs precision** tiếp nhận điểm tựa từ **59. Group quyền sở hữu (ownership / 소유권)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **61. Peer là sibling direction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. `in-*` convenience vs precision

`in-*` bỏ tường minh (explicit / 명시적) marker và tìm ancestor trạng thái (state / 상태).

Nó giảm markup nhưng tăng implicit phụ thuộc (dependency / 의존성).

Cấp cao (senior / 시니어) chọn:
- shallow/simple → `in-*` okay,
- nested reusable thành phần (component / 컴포넌트) → named group.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **61. Peer là sibling direction** tiếp nhận điểm tựa từ **60. in- convenience vs precision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **62. has- không thay lô-gic nghiệp vụ (business logic / 비즈니스 로직)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 61. Peer là sibling direction

CSS sibling bộ chọn (selector) không quay ngược.

```html
<input class="peer">
<p class="peer-invalid:block">
```

works.

Nếu paragraph đứng trước đầu vào (input / 입력), peer mẫu (pattern / 패턴) không thể mục tiêu (target / 대상) backward.

Use:
- parent `has-*`,
- DOM restructure,
- ứng dụng (application / 애플리케이션) trạng thái (state / 상태)
tùy trường hợp (case / 사례).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **62. has- không thay lô-gic nghiệp vụ (business logic / 비즈니스 로직)** tiếp nhận điểm tựa từ **61. Peer là sibling direction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **63. các biến thể tùy ý (arbitrary variants) phù hợp với integration nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 62. `has-*` không thay lô-gic nghiệp vụ (business logic / 비즈니스 로직)

`:has()` nhìn DOM relationship.

Good:
- parent contains checked đầu vào (input / 입력),
- form group contains invalid đầu vào (input / 입력).

Không dùng `:has()` để suy nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) không được biểu diễn trong DOM. trạng thái (state / 상태) nghiệp vụ (business / 비즈니스) vẫn phải đến từ app mô hình (model / 모델).

---

# PHẦN XI — THIRD-PARTY tích hợp (integration / 통합)

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **63. các biến thể tùy ý (arbitrary variants) phù hợp với integration nhỏ** tiếp nhận điểm tựa từ **62. has- không thay lô-gic nghiệp vụ (business logic / 비즈니스 로직)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **64. Khi tích hợp (integration / 통합) nên có biểu định kiểu (stylesheet / 스타일시트) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 63. các biến thể tùy ý (arbitrary variants) phù hợp với integration nhỏ
Phần này nối mạch bài học với “63. các biến thể tùy ý (arbitrary variants) phù hợp với integration nhỏ”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
[&_.vendor-item]:p-2
```

một hoặc vài bộ chọn (selector) là fine.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **64. Khi tích hợp (integration / 통합) nên có biểu định kiểu (stylesheet / 스타일시트) riêng** tiếp nhận điểm tựa từ **63. các biến thể tùy ý (arbitrary variants) phù hợp với integration nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **65. @apply ở integration layer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 64. Khi tích hợp (integration / 통합) nên có biểu định kiểu (stylesheet / 스타일시트) riêng

Nếu bạn có:

```text
vendor root
vendor item
vendor active item
vendor dropdown
vendor search
vendor disabled
vendor nested menu
```

Lớp (class / 클래스) attribute sẽ trở thành bộ chọn (selector) ngôn ngữ (language / 언어) khó đọc.

Tạo:

```text
styles/integrations/vendor.css
```

và viết normal CSS hoặc `@apply` targeted.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **65. @apply ở integration layer** tiếp nhận điểm tựa từ **64. Khi tích hợp (integration / 통합) nên có biểu định kiểu (stylesheet / 스타일시트) riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **66. @reference trong isolated style contexts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 65. `@apply` ở integration layer
Phần này nối mạch bài học với “65. `@apply` ở integration layer”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
.vendor-dropdown {
  @apply rounded-xl bg-white shadow-xl;
}
```

Trong trường hợp (case / 사례) markup không điều khiển (control / 제어), `@apply` thực sự có giá trị vì giúp use same Tailwind theme/tiện ích (utility) các giá trị (values).

Đây khác với việc tự recreate mọi nội bộ (internal / 내부) app thành phần (component / 컴포넌트) bằng `.btn-primary`.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, sau nội dung của **65. @apply ở integration layer**, **66. @reference trong isolated style contexts** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **67. Một dự án (project / 프로젝트) có thể có quá nhiều styling layers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 66. `@reference` trong isolated style contexts

Nếu tích hợp (integration / 통합) CSS/thành phần (component / 컴포넌트) style được xử lý riêng, `@reference` có thể expose theme/custom APIs mà không duplicate CSS.

Điều này đặc biệt hữu ích trong:
- Vue SFC,
- Svelte,
- CSS Modules.

Nhưng nếu chỉ dùng one đơn vị từ (token / 토큰), direct `var(--color-...)` đơn giản hơn.

---

# PHẦN XII — TAILWIND + SCSS / CSS MODULES / Shadow DOM (cây DOM đóng gói)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **67. Một dự án (project / 프로젝트) có thể có quá nhiều styling layers** tiếp nhận điểm tựa từ **66. @reference trong isolated style contexts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **68. Tailwind + SCSS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 67. Một dự án (project / 프로젝트) có thể có quá nhiều styling layers

Ví dụ:

```text
SCSS variable
→ emits CSS var
→ Tailwind @theme alias
→ custom utility
→ @apply
→ CSS Module
→ component className
```

Kỹ thuật thì có thể hoạt động, nhưng gỡ lỗi (debugging) trở nên khó.

Mastery là biết **bỏ bớt tầng (layer / 계층)**.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **68. Tailwind + SCSS** tiếp nhận điểm tựa từ **67. Một dự án (project / 프로젝트) có thể có quá nhiều styling layers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **69. Tailwind + CSS Modules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 68. Tailwind + SCSS

SCSS vẫn mạnh nếu dự án (project / 프로젝트) cần:
- thời điểm biên dịch (compile-time) các map khóa–giá trị (maps),
- các hàm (functions),
- legacy Sass thư viện (library / 라이브러리) cấu hình (configuration / 구성).

Tailwind v4 đã có:
- theme CSS vars,
- ưu tiên CSS (CSS-first) các tiện ích (utilities),
- bản địa (native / 네이티브) lồng cú pháp (nesting) ecosystem,
- các biến thể (variants).

Greenfield Tailwind dự án (project / 프로젝트) có thể không cần Sass.

Nếu dùng cả hai, hãy chọn một nguồn chuẩn (source of truth / 정본) cho tokens.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **69. Tailwind + CSS Modules** tiếp nhận điểm tựa từ **68. Tailwind + SCSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **70. Shadow DOM (cây DOM đóng gói)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 69. Tailwind + CSS Modules

Tailwind:
- atomic styling in markup.

CSS Modules:
- cục bộ (local / 로컬) scoped bộ chọn (selector).

Cả hai coexist tốt khi responsibilities khác nhau.

Nếu CSS mô-đun (module / 모듈) chỉ có:

```css
.title {
  @apply text-red-500;
}
```

thì bạn đang thêm một lớp trừu tượng (abstraction / 추상화) mà không có giá trị (value / 값).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **70. Shadow DOM (cây DOM đóng gói)** tiếp nhận điểm tựa từ **69. Tailwind + CSS Modules** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **71. Design-system gói (package / 패키지) có thể ship cái gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 70. Shadow DOM (cây DOM đóng gói)

Tailwind generated biểu định kiểu (stylesheet / 스타일시트) ở document không pierce shadow gốc (root / 루트).

Web thành phần (component / 컴포넌트) cần:
- own biểu định kiểu (stylesheet / 스타일시트),
- adopted biểu định kiểu (stylesheet / 스타일시트),
- custom các thuộc tính (properties),
- `::part`
tùy API.

Tailwind không thay Shadow DOM (cây DOM đóng gói) đóng gói (encapsulation).

---

# PHẦN XIII — gói (package / 패키지) thiết kế (design / 설계)

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **71. Design-system gói (package / 패키지) có thể ship cái gì?** tiếp nhận điểm tựa từ **70. Shadow DOM (cây DOM đóng gói)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **72. Ship nguồn (source / 소스) components** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 71. Design-system gói (package / 패키지) có thể ship cái gì?

Một Tailwind hệ thống thiết kế (design system) có thể ship:
- nguồn (source / 소스) React/Vue components chứa Tailwind classes,
- compiled CSS,
- theme CSS,
- custom các tiện ích (utilities).

Mỗi lựa chọn có coupling khác nhau.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **71. Design-system gói (package / 패키지) có thể ship cái gì?** nêu điều cần giải thích; **72. Ship nguồn (source / 소스) components** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **73. Ship compiled CSS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 72. Ship nguồn (source / 소스) components

Bên tiêu thụ (consumer / 소비자) bản dựng (build / 빌드) Tailwind dựa trên gói (package / 패키지) nguồn (source / 소스).

Ưu:
- tiện ích (utility) generation theo usage.

Yêu cầu:
- bên tiêu thụ (consumer / 소비자) `@source` gói (package / 패키지),
- compatible Tailwind phiên bản (version / 버전),
- compatible theme vocabulary.

Tailwind trở thành peer/bản dựng (build / 빌드) đặc tả hợp đồng (contract / 계약).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **72. Ship nguồn (source / 소스) components** nêu điều cần giải thích; **73. Ship compiled CSS** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **74. Ship theme-only gói (package / 패키지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 73. Ship compiled CSS

Bên tiêu thụ (consumer / 소비자) không cần scan gói (package / 패키지).

Ưu:
- framework-neutral dễ dùng.

Nhược:
- CSS bundle static,
- potential duplicate reset/theme,
- theming cần công khai (public / 공개) CSS vars,
- tầng (layer / 계층) tích hợp (integration / 통합) cần thiết kế (design / 설계).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **74. Ship theme-only gói (package / 패키지)** tiếp nhận điểm tựa từ **73. Ship compiled CSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **75. phiên bản (version / 버전) tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 74. Ship theme-only gói (package / 패키지)

V4 rất phù hợp:

```text
@company/theme.css
```

chứa `@theme`.

Nhiều apps share:
- colors,
- typography,
- các điểm ngắt (breakpoints),
- radii.

Theme gói (package / 패키지) có thể phiên bản (version / 버전) độc lập với thành phần (component / 컴포넌트) gói (package / 패키지).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **75. phiên bản (version / 버전) tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **74. Ship theme-only gói (package / 패키지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **76. Scrollbar các tiện ích (utilities)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 75. phiên bản (version / 버전) tính tương thích (compatibility / 호환성)

Nếu thư viện (library / 라이브러리) dùng tính năng (feature / 기능) v4.3 như:
- `@container-size`,
- scrollbar các tiện ích (utilities),
- `zoom-*`,
- new functional tiện ích (utility) defaults,

docs nên nói rõ minimum Tailwind phiên bản (version / 버전).

Nếu không, bên tiêu thụ (consumer / 소비자) v4.1 có thể compile thất bại (fail / 실패) hoặc thiếu lớp (class / 클래스).

---

# PHẦN XIV — V4.3 FEATURES VÀ Ý NGHĨA KIẾN TRÚC

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **76. Scrollbar các tiện ích (utilities)** tiếp nhận điểm tựa từ **75. phiên bản (version / 버전) tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **77. @container-size** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 76. Scrollbar các tiện ích (utilities)

V4.3 đưa scrollbar styling vào cốt lõi (core / 핵심) tốt hơn.

Điều này có hai tác dụng:
- giảm nhu cầu community plugin/custom tiện ích (utility),
- làm đơn vị từ (token / 토큰) thiết kế (design token) tích hợp (integration / 통합) dễ hơn.

Nhưng scrollbar vẫn là nền tảng (platform / 플랫폼) UI. Visual hành vi (behavior / 동작) đa trình duyệt (cross-browser)/OS không tuyệt đối giống nhau.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **77. @container-size** tiếp nhận điểm tựa từ **76. Scrollbar các tiện ích (utilities)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **78. zoom-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 77. `@container-size`

Đây không chỉ là thêm một lớp (class / 클래스). Nó phản ánh CSS nền tảng (platform / 플랫폼) đã đi sâu hơn vào component-local responsiveness.

Bạn có thể truy vấn (query / 쿼리) khối (block / 블록) kích thước (size / 크기)/height-dependent contexts, nhưng kích thước (size / 크기) containment có bố cục (layout / 레이아웃) consequences. Vì vậy đây là công cụ (tool / 도구) advanced.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **78. zoom-** tiếp nhận điểm tựa từ **77. @container-size** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **79. tab-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 78. `zoom-*`

V4.3 tiện ích (utility) cho CSS `zoom` xuất hiện sau khi trình duyệt (browser / 브라우저) interoperability tốt hơn.

Use cases:
- preview,
- editor canvas,
- document miniature.

Không thay responsive bố cục (layout / 레이아웃).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **79. tab-** tiếp nhận điểm tựa từ **78. zoom-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **80. Stacked/compound @variant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 79. `tab-*`

`tab-size` trở thành first-class tiện ích (utility).

Use:
- mã (code / 코드) rendering,
- nguồn (source / 소스) editor,
- preformatted blocks.

Một tính năng (feature / 기능) nhỏ nhưng minh họa triết lý Tailwind: khi CSS thuộc tính (property / 속성) trở nên đủ phổ biến, cốt lõi (core / 핵심) tiện ích (utility) API mở rộng để giảm custom CSS.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **80. Stacked/compound @variant** tiếp nhận điểm tựa từ **79. tab-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **81. chuyển đổi (migration) không phải chỉ search-and-replace** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 80. Stacked/compound `@variant`

Trước đây nhiều nhà phát triển (developer / 개발자) nghĩ các biến thể (variants) chỉ dành lớp (class / 클래스) markup. V4.3 làm custom CSS biến thể (variant) reuse mạnh hơn.

Điều này giúp third-party/custom thành phần (component / 컴포넌트) CSS vẫn participate cùng trạng thái (state / 상태) vocabulary của dự án (project / 프로젝트).

---

# PHẦN XV — chuyển đổi (migration) V3 → V4 SÂU HƠN

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **81. chuyển đổi (migration) không phải chỉ search-and-replace** tiếp nhận điểm tựa từ **80. Stacked/compound @variant** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **82. Upgrade công cụ (tool / 도구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 81. chuyển đổi (migration) không phải chỉ search-and-replace

V3 kiến trúc (architecture / 아키텍처) thường gom:
- content paths,
- theme,
- plugins,
- danh sách ép giữ (safelist)
vào JS cấu hình (config / 설정).

V4 đưa nhiều phần về CSS.

Do đó chuyển đổi (migration) là cơ hội hỏi:
- theme tokens công khai (public / 공개) nào?
- nguồn (source / 소스) quyền sở hữu (ownership / 소유권) thế nào?
- custom plugin nào giờ chỉ cần `@utility`?
- danh sách ép giữ (safelist) nào là technical debt?
- thành phần (component / 컴포넌트) nào đang động (dynamic / 동적) lớp (class / 클래스) synthesis?

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **82. Upgrade công cụ (tool / 도구)** tiếp nhận điểm tựa từ **81. chuyển đổi (migration) không phải chỉ search-and-replace** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **83. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) trước khi migrate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 82. Upgrade công cụ (tool / 도구)

Official upgrade tooling có thể tự động phần lớn chuyển đổi (migration) mechanics.

Nhưng công cụ (tool / 도구) không thể quyết định:
- đơn vị từ (token / 토큰) ngữ nghĩa (semantic token) thiết kế (design / 설계),
- monorepo nguồn (source / 소스) quyền sở hữu (ownership / 소유권),
- công khai (public / 공개) giao diện thành phần (component API),
- custom tiện ích (utility) kiến trúc (architecture / 아키텍처).

Run công cụ (tool / 도구), sau đó rà soát (review / 검토).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **83. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) trước khi migrate** tiếp nhận điểm tựa từ **82. Upgrade công cụ (tool / 도구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **84. @config như chuyển đổi (migration) bridge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 83. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) trước khi migrate

Tailwind v4 dùng hiện đại (modern / 현대적) CSS đường cơ sở (baseline) và có minimum trình duyệt (browser / 브라우저) targets cao hơn v3.

Nếu sản phẩm (product / 제품) còn hỗ trợ trình duyệt (browser / 브라우저) cũ, upgrade có thể là sản phẩm (product / 제품) quyết định (decision / 결정) chứ không chỉ gói (package / 패키지) cập nhật (update / 업데이트).

Đây là lý do khung phần mềm (framework / 프레임워크) major phiên bản (version / 버전) phải được đánh giá cùng trình duyệt (browser / 브라우저) chính sách (policy / 정책).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **84. @config như chuyển đổi (migration) bridge** tiếp nhận điểm tựa từ **83. mức hỗ trợ trình duyệt (browser support / 브라우저 지원) trước khi migrate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **85. Custom plugin chuyển đổi (migration)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 84. `@config` như chuyển đổi (migration) bridge
Phần này nối mạch bài học với “84. `@config` như chuyển đổi (migration) bridge”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```css
@config "../../tailwind.config.js";
```

giúp giữ legacy JS cấu hình (config / 설정).

Nếu 2 năm sau dự án (project / 프로젝트) vẫn có:
- half CSS theme,
- half JS cấu hình (config / 설정),
- half plugins
thì chuyển đổi (migration) chưa hoàn thành về kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **85. Custom plugin chuyển đổi (migration)** tiếp nhận điểm tựa từ **84. @config như chuyển đổi (migration) bridge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **86. danh sách ép giữ (safelist) chuyển đổi (migration)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 85. Custom plugin chuyển đổi (migration)

Một v3 plugin chỉ tạo simple tiện ích (utility) có thể chuyển sang `@utility`.

Plugin chỉ tạo biến thể (variant) có thể chuyển sang `@custom-variant`.

Complex JS plugin có lô-gic (logic / 논리)/gói (package / 패키지) tích hợp (integration / 통합) vẫn có thể giữ plugin.

Mục tiêu không phải loại bỏ JS plugin bằng mọi giá, mà dùng simplest cơ chế (mechanism / 메커니즘).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **86. danh sách ép giữ (safelist) chuyển đổi (migration)** tiếp nhận điểm tựa từ **85. Custom plugin chuyển đổi (migration)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **87. Tailwind hiệu năng (performance / 성능) cần đo ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 86. danh sách ép giữ (safelist) chuyển đổi (migration)

Old danh sách ép giữ (safelist) thường tích tụ “mysterious classes” qua năm tháng.

Khi chuyển sang `@source inline()`, hãy kiểm tra (audit / 감사) từng set:
- nguồn (source / 소스) thật sự ở đâu?
- CMS có finite các giá trị (values) không?
- có thể static map khóa–giá trị (map) không?

Đừng mechanically bản sao (copy / 복사) universe danh sách ép giữ (safelist).

---

# PHẦN XVI — hiệu năng (performance / 성능)

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **87. Tailwind hiệu năng (performance / 성능) cần đo ở đâu?** tiếp nhận điểm tựa từ **86. danh sách ép giữ (safelist) chuyển đổi (migration)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **88. Cold bản dựng (build / 빌드) và incremental bản dựng (build / 빌드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 87. Tailwind hiệu năng (performance / 성능) cần đo ở đâu?

Có ba loại chi phí (cost / 비용):
- nguồn (source / 소스) scanning,
- CSS generation/bản dựng (build / 빌드) thời gian (time / 시간),
- final CSS bytes.

Ngoài ra trình duyệt (browser / 브라우저) vẫn chịu CSS/kết xuất (render / 렌더링) chi phí (cost / 비용) như bình thường.

Một nguồn (source / 소스) cây (tree / 트리) lớn nhưng candidate ít có chi phí (cost / 비용) scanning. Một danh sách ép giữ (safelist) lớn có chi phí (cost / 비용) generation/đầu ra (output / 출력). Một giant CSS bundle có mạng (network / 네트워크)/parse chi phí (cost / 비용).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **88. Cold bản dựng (build / 빌드) và incremental bản dựng (build / 빌드)** tiếp nhận điểm tựa từ **87. Tailwind hiệu năng (performance / 성능) cần đo ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **89. Unique các giá trị tùy ý (arbitrary values)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 88. Cold bản dựng (build / 빌드) và incremental bản dựng (build / 빌드)

Khi dự án (project / 프로젝트) lớn, đo:
- first clean bản dựng (build / 빌드),
- rebuild khi đổi tệp (file / 파일) không tạo candidate mới,
- rebuild khi thêm candidate,
- CI bản dựng (build / 빌드).

V4 được tối ưu mạnh cho incremental generation, nhưng monorepo/file-watching cấu hình (config / 설정) sai vẫn có thể dominate.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **89. Unique các giá trị tùy ý (arbitrary values)** tiếp nhận điểm tựa từ **88. Cold bản dựng (build / 빌드) và incremental bản dựng (build / 빌드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **90. @theme static và đầu ra (output / 출력) kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 89. Unique các giá trị tùy ý (arbitrary values)
Phần này nối mạch bài học với “89. Unique các giá trị tùy ý (arbitrary values)”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```text
top-[117px]
```

one-off không vấn đề.

Data-driven generation của hàng nghìn các giá trị (values) mới là vấn đề.

Mẫu (pattern / 패턴) đúng cho dữ liệu (data / 데이터):
- CSS biến (variable),
- one static tiện ích (utility) bên tiêu thụ (consumer / 소비자).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **90. @theme static và đầu ra (output / 출력) kích thước (size / 크기)** tiếp nhận điểm tựa từ **89. Unique các giá trị tùy ý (arbitrary values)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **91. Nhiều CSS điểm vào (entrypoint / 진입점)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 90. `@theme static` và đầu ra (output / 출력) kích thước (size / 크기)

Static theme giúp consumers ngoài tiện ích (utility) hệ thống (system / 시스템) nhìn thấy tất cả tokens.

Nhưng nếu theme có hàng nghìn các biến (variables), đầu ra (output / 출력) tăng.

Hãy quyết định dựa usage:
- design-token gói (package / 패키지) cần full surface → hợp lý,
- app nhỏ chỉ dùng vài đơn vị từ (token / 토큰) → normal emission tốt hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **91. Nhiều CSS điểm vào (entrypoint / 진입점)** tiếp nhận điểm tựa từ **90. @theme static và đầu ra (output / 출력) kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **92. @apply trong hàng nghìn thành phần (component / 컴포넌트) style blocks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 91. Nhiều CSS điểm vào (entrypoint / 진입점)

Hai điểm vào (entrypoint / 진입점) đều:

```css
@import "tailwindcss";
```

có thể mỗi cái chứa:
- Preflight (lớp reset nền của Tailwind),
- theme,
- overlapping các tiện ích (utilities).

Nếu cả hai tải (load / 로드) cùng page, CSS duplicate.

Master cần kiểm tra (audit / 감사) biểu định kiểu (stylesheet / 스타일시트) đồ thị (graph / 그래프) giống kiểm tra (audit / 감사) JS bundle đồ thị (graph / 그래프).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **92. @apply trong hàng nghìn thành phần (component / 컴포넌트) style blocks** tiếp nhận điểm tựa từ **91. Nhiều CSS điểm vào (entrypoint / 진입점)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **93. Bước 1: xác định CSS có tồn tại không** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 92. `@apply` trong hàng nghìn thành phần (component / 컴포넌트) style blocks

Mỗi isolated style ngữ cảnh (context / 맥락) cần Tailwind processing/tham chiếu (reference / 참조) resolution.

Nếu chỉ cần đơn vị từ (token / 토큰) color:

```css
color: var(--color-red-500);
```

rẻ và rõ hơn `@apply text-red-500`.

Không micro-optimize một thành phần (component / 컴포넌트); nhưng kiến trúc (architecture / 아키텍처) hàng nghìn components thì khác.

---

# PHẦN XVII — gỡ lỗi (debugging) Ở CẤP MASTER

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **93. Bước 1: xác định CSS có tồn tại không** tiếp nhận điểm tựa từ **92. @apply trong hàng nghìn thành phần (component / 컴포넌트) style blocks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **94. gỡ lỗi (debug / 디버그) phát hiện nguồn (source detection)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 93. Bước 1: xác định CSS có tồn tại không

DevTools/tìm kiếm (search / 검색) generated CSS.

Nếu `.bg-brand` không tồn tại:
- scanner,
- theme đơn vị từ (token / 토큰),
- nguồn (source / 소스),
- tiện ích (utility) registration.

Nếu tồn tại:
- Tailwind bản dựng (build / 빌드) đã làm việc,
- chuyển sang cơ chế phân tầng (cascade)/bố cục (layout / 레이아웃) gỡ lỗi (debugging).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **93. Bước 1: xác định CSS có tồn tại không** nêu điều cần giải thích; **94. gỡ lỗi (debug / 디버그) phát hiện nguồn (source detection)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **95. gỡ lỗi (debug / 디버그) custom theme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 94. gỡ lỗi (debug / 디버그) phát hiện nguồn (source detection)

Kiểm tra lớp (class / 클래스) có literal complete không.

Kiểm tra tệp (file / 파일):
- có bị ignored?
- nằm phụ thuộc (dependency / 의존성)?
- nằm ngoài cơ sở (base / 기반) đường dẫn (path / 경로)?
- biểu định kiểu (stylesheet / 스타일시트) bundle này có scan nguồn (source / 소스) đó?

Nếu gói (package / 패키지) nguồn (source / 소스), kiểm tra `@source`.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **94. gỡ lỗi (debug / 디버그) phát hiện nguồn (source detection)** nêu điều cần giải thích; **95. gỡ lỗi (debug / 디버그) custom theme** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **96. gỡ lỗi (debug / 디버그) custom tiện ích (utility)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 95. gỡ lỗi (debug / 디버그) custom theme

`bg-brand` không generate?

Check:

```css
@theme {
  --color-brand: ...
}
```

Nếu bạn chỉ đặt:

```css
:root {
  --color-brand: ...
}
```

thì thời gian chạy (runtime / 런타임) biến (variable) tồn tại nhưng Tailwind không gian tên chủ đề (theme namespace) có thể không đăng ký tiện ích (utility) như bạn tưởng.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **96. gỡ lỗi (debug / 디버그) custom tiện ích (utility)** tiếp nhận điểm tựa từ **95. gỡ lỗi (debug / 디버그) custom theme** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **97. gỡ lỗi (debug / 디버그) biến thể (variant)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 96. gỡ lỗi (debug / 디버그) custom tiện ích (utility)

Candidate correct nhưng quy tắc (rule / 규칙) không có?

Check:
- `@utility` cú pháp (syntax / 문법),
- functional resolver kiểu (type / 타입),
- theme key,
- default/modifier,
- giá trị (value / 값) có resolve được không.

Build-time Tailwind có thể drop khai báo (declaration) không resolve.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **97. gỡ lỗi (debug / 디버그) biến thể (variant)** tiếp nhận điểm tựa từ **96. gỡ lỗi (debug / 디버그) custom tiện ích (utility)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **98. gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 97. gỡ lỗi (debug / 디버그) biến thể (variant)

`group-hover` không chạy?

Kiểm tra:
- ancestor thật sự có `group`,
- named group match,
- child trong correct descendant relationship,
- hover môi trường (environment / 환경).

`peer-invalid` không chạy?

Kiểm tra:
- peer trước mục tiêu (target / 대상),
- đầu vào (input / 입력) thật sự invalid,
- bộ chọn (selector) quan hệ (relation / 관계).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **98. gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너)** tiếp nhận điểm tựa từ **97. gỡ lỗi (debug / 디버그) biến thể (variant)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **99. gỡ lỗi (debug / 디버그) lớp (class / 클래스) xung đột (conflict / 충돌)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 98. gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너)

`@md:` không chạy?

Kiểm tra:
- ancestor có `@container`,
- nearest bộ chứa (container / 컨테이너) có đủ width,
- nếu named truy vấn (query / 쿼리) thì name đúng,
- `@container-size` chỉ cần cho block-size use trường hợp (case / 사례).

Không nhìn vùng nhìn (viewport) width để kết luận bộ chứa (container / 컨테이너) biến thể (variant).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **99. gỡ lỗi (debug / 디버그) lớp (class / 클래스) xung đột (conflict / 충돌)** tiếp nhận điểm tựa từ **98. gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **100. gỡ lỗi (debug / 디버그) z-index** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 99. gỡ lỗi (debug / 디버그) lớp (class / 클래스) xung đột (conflict / 충돌)

Mở computed style.

Tìm thuộc tính (property / 속성):

```text
padding-left
padding-right
```

xem quy tắc (rule / 규칙) nào winner.

Đừng chỉ nhìn:

```html
class="px-4 px-2"
```

rồi đoán.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **100. gỡ lỗi (debug / 디버그) z-index** tiếp nhận điểm tựa từ **99. gỡ lỗi (debug / 디버그) lớp (class / 클래스) xung đột (conflict / 충돌)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **101. khả năng tiếp cận (accessibility / 접근성) phải được thiết kế thành hợp đồng thành phần (component contract)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 100. gỡ lỗi (debug / 디버그) z-index

Nếu tiện ích (utility) quy tắc (rule / 규칙) `z-50` apply mà modal vẫn dưới:
- parent ngữ cảnh xếp chồng (stacking context / 쌓임 맥락),
- lớp trên cùng (top layer),
- transform/filter/opacity/cô lập (isolation).

Tailwind không thể phá CSS stacking rules.

---

# PHẦN XVIII — khả năng tiếp cận (accessibility / 접근성) VÀ UI trạng thái (state / 상태) Ở quy mô (scale / 규모)

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **101. khả năng tiếp cận (accessibility / 접근성) phải được thiết kế thành hợp đồng thành phần (component contract)** tiếp nhận điểm tựa từ **100. gỡ lỗi (debug / 디버그) z-index** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **102. trạng thái (state / 상태) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 101. khả năng tiếp cận (accessibility / 접근성) phải được thiết kế thành hợp đồng thành phần (component contract)

Button thành phần (component / 컴포넌트) nên có:
- actual `<button>`,
- disabled hành vi (behavior / 동작),
- focus-visible style,
- loading ngữ nghĩa (semantics / 의미론),
- accessible label khi icon-only.

Tailwind các tiện ích (utilities) làm hiện thực (implementation / 구현) concise, nhưng đặc tả hợp đồng (contract / 계약) nằm ở thành phần (component / 컴포넌트) thiết kế (design / 설계).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **102. trạng thái (state / 상태) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **101. khả năng tiếp cận (accessibility / 접근성) phải được thiết kế thành hợp đồng thành phần (component contract)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **103. giảm chuyển động (reduced motion) không phải optional polish** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 102. trạng thái (state / 상태) ma trận (matrix / 행렬)

Một mature thành phần (component / 컴포넌트) không chỉ kiểm thử (test / 테스트) default.

Button có thể có:

```text
variant × size ×
hover/focus/active/disabled/loading
× light/dark
× forced colors
```

Tailwind giúp encode combinations, nhưng trạng thái (state / 상태) không gian (space / 공간) vẫn tồn tại.

hồi quy giao diện (visual regression) rất hữu ích.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **103. giảm chuyển động (reduced motion) không phải optional polish** tiếp nhận điểm tựa từ **102. trạng thái (state / 상태) ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **104. màu cưỡng bức (forced colors)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 103. giảm chuyển động (reduced motion) không phải optional polish

Nếu thành phần (component / 컴포넌트) có transform/animation lớn:
- add `motion-reduce`,
- hoặc thiết kế motion hệ thống (system / 시스템) toàn cục (global / 전역).

Người dùng (user / 사용자) preference là đầu vào (input / 입력) giống vùng nhìn (viewport)/theme, không phải afterthought.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **104. màu cưỡng bức (forced colors)** tiếp nhận điểm tựa từ **103. giảm chuyển động (reduced motion) không phải optional polish** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **105. Static tests** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 104. màu cưỡng bức (forced colors)

Colors có thể bị trình duyệt (browser / 브라우저) override.

Nếu custom điều khiển (control / 제어) chỉ biểu diễn selected trạng thái (state / 상태) bằng subtle background color, màu cưỡng bức (forced colors) chế độ (mode / 모드) có thể mất distinction.

Kiểm thử (test / 테스트) actual forced-colors hành vi (behavior / 동작) và use mang tính ngữ nghĩa (semantic / 의미적) border/hệ thống (system / 시스템) color phương án dự phòng (fallback) khi cần.

---

# PHẦN XIX — TESTING

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **105. Static tests** tiếp nhận điểm tựa từ **104. màu cưỡng bức (forced colors)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **106. thành phần (component / 컴포넌트) tests** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 105. Static tests

Static tooling có thể bắt:
- invalid lớp (class / 클래스),
- đã ngừng khuyến nghị (deprecated) lớp (class / 클래스),
- động (dynamic / 동적) concatenation patterns,
- arbitrary-value chính sách (policy / 정책).

IDE IntelliSense giúp phản hồi (feedback / 피드백) sớm.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **106. thành phần (component / 컴포넌트) tests** tiếp nhận điểm tựa từ **105. Static tests** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **107. hồi quy giao diện (visual regression)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 106. thành phần (component / 컴포넌트) tests

Kiểm thử (test / 테스트) hành vi (behavior / 동작):
- disabled thật sự không click,
- aria-expanded thay đổi,
- data-state chuyển tiếp (transition / 전이) đúng.

Đừng kiểm thử (test / 테스트) chỉ lớp (class / 클래스) string nếu hành vi (behavior / 동작) mới là đặc tả hợp đồng (contract / 계약).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **107. hồi quy giao diện (visual regression)** tiếp nhận điểm tựa từ **106. thành phần (component / 컴포넌트) tests** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **108. Tại sao chính xác (exact / 정확한) lớp (class / 클래스) snapshot thường brittle?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 107. hồi quy giao diện (visual regression)

CSS bug thường không throw exception.

Capture screenshots cho:
- mobile,
- tablet,
- desktop,
- dark,
- focus,
- long văn bản (text / 텍스트),
- RTL.

Với thành phần (component / 컴포넌트) thư viện (library / 라이브러리), thêm:
- loading,
- empty,
- lỗi (error / 오류),
- disabled.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **108. Tại sao chính xác (exact / 정확한) lớp (class / 클래스) snapshot thường brittle?** tiếp nhận điểm tựa từ **107. hồi quy giao diện (visual regression)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **109. Không nhận raw Tailwind lớp (class / 클래스) từ người dùng (user / 사용자) nếu không cần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 108. Tại sao chính xác (exact / 정확한) lớp (class / 클래스) snapshot thường brittle?

Nếu kiểm thử (test / 테스트):

```text
expect(button.className)
  .toBe("flex px-4 ...")
```

formatter hoặc harmless refactor làm kiểm thử (test / 테스트) thất bại (fail / 실패).

Prefer mang tính ngữ nghĩa (semantic / 의미적)/visual tests.

Lớp (class / 클래스) snapshot chỉ hợp lý nếu lớp (class / 클래스) đầu ra (output / 출력) là giao diện công khai (public API) hoặc bạn đang kiểm thử (test / 테스트) class-merging tiện ích (utility).

---

# PHẦN XX — bảo mật (security / 보안) VÀ CMS

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **109. Không nhận raw Tailwind lớp (class / 클래스) từ người dùng (user / 사용자) nếu không cần** tiếp nhận điểm tựa từ **108. Tại sao chính xác (exact / 정확한) lớp (class / 클래스) snapshot thường brittle?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **110. giá trị tùy ý (arbitrary value) từ untrusted đầu vào (input / 입력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 109. Không nhận raw Tailwind lớp (class / 클래스) từ người dùng (user / 사용자) nếu không cần

CMS có option “danger”.

Bad dữ liệu (data / 데이터):

```text
bg-red-500
```

Better dữ liệu (data / 데이터):

```text
danger
```

App map khóa–giá trị (map):

```text
danger → bg-red-500 text-white
```

Bạn giữ:
- thiết kế (design / 설계) quản trị (governance / 거버넌스),
- scanner visibility,
- ranh giới bảo mật (security boundary / 보안 경계).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **110. giá trị tùy ý (arbitrary value) từ untrusted đầu vào (input / 입력)** tiếp nhận điểm tựa từ **109. Không nhận raw Tailwind lớp (class / 클래스) từ người dùng (user / 사용자) nếu không cần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **111. CSS nguồn chuẩn (source of truth / 정본) phải là một nơi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 110. giá trị tùy ý (arbitrary value) từ untrusted đầu vào (input / 입력)

Không concatenate người dùng (user / 사용자) đầu vào (input / 입력) vào:

```text
[background:url(...)]
```

hoặc thuộc tính tùy ý (arbitrary property).

Tailwind không sanitize CSS intent.

Whitelist các giá trị (values) hoặc validate dữ liệu (data / 데이터) rồi expose qua safe thời gian chạy (runtime / 런타임) biến (variable).

---

# PHẦN XXI — TƯ DUY gói (package / 패키지) VÀ ENTERPRISE

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **110. giá trị tùy ý (arbitrary value) từ untrusted đầu vào (input / 입력)** nêu điều cần giải thích; **111. CSS nguồn chuẩn (source of truth / 정본) phải là một nơi** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **112. bên ngoài (external / 외부) đơn vị từ (token / 토큰) thiết kế (design token) chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 111. CSS nguồn chuẩn (source of truth / 정본) phải là một nơi

Một hệ thống dễ hỏng nếu cùng color tồn tại độc lập trong:
- Tailwind `@theme`,
- Sass `$map`,
- CSS `:root`,
- TypeScript constants,
- Figma export.

Enterprise nên có một đơn vị từ (token / 토큰) nguồn (source / 소스) chính, sau đó generate/alias cho các nền tảng (platform / 플랫폼).

Tailwind v4 phù hợp làm bên tiêu thụ (consumer / 소비자)/đầu ra (output / 출력) của đơn vị từ (token / 토큰) chuỗi xử lý (pipeline / 파이프라인).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **111. CSS nguồn chuẩn (source of truth / 정본) phải là một nơi** nêu điều cần giải thích; **112. bên ngoài (external / 외부) đơn vị từ (token / 토큰) thiết kế (design token) chuỗi xử lý (pipeline / 파이프라인)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **113. Tailwind là hiện thực (implementation / 구현) detail của thành phần (component / 컴포넌트) thư viện (library / 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 112. bên ngoài (external / 외부) đơn vị từ (token / 토큰) thiết kế (design token) chuỗi xử lý (pipeline / 파이프라인)

Ví dụ:

```text
tokens.json
→ build transform
→ theme.css
→ @theme
→ Tailwind utilities
```

và cùng nguồn (source / 소스) có thể generate:
- iOS tokens,
- Android resources,
- TypeScript constants.

Không nên parse JSON bằng CSS/Tailwind tricks.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **112. bên ngoài (external / 외부) đơn vị từ (token / 토큰) thiết kế (design token) chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **113. Tailwind là hiện thực (implementation / 구현) detail của thành phần (component / 컴포넌트) thư viện (library / 라이브러리)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **114. Complex rich-text styling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 113. Tailwind là hiện thực (implementation / 구현) detail của thành phần (component / 컴포넌트) thư viện (library / 라이브러리)

Bên tiêu thụ (consumer / 소비자):

```tsx
<Button variant="primary" />
```

không nên cần biết:

```text
bg-blue-600
```

Nếu sau này nhóm (team / 팀) đổi sang CSS Modules hoặc vanilla CSS, giao diện thành phần (component API) vẫn giữ.

Đây là lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) khỏe mạnh.

---

# PHẦN XXII — KHI NÀO KHÔNG NÊN DÙNG TAILWIND

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **114. Complex rich-text styling** tiếp nhận điểm tựa từ **113. Tailwind là hiện thực (implementation / 구현) detail của thành phần (component / 컴포넌트) thư viện (library / 라이브러리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **115. Third-party DOM sâu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 114. Complex rich-text styling

Một article renderer có nested:
- h2,
- blockquote,
- tables,
- mã (code / 코드),
- các danh sách (lists),
- links
từ CMS.

Viết lớp (class / 클래스) vào từng generated element không practical.

Scoped mang tính ngữ nghĩa (semantic / 의미적) CSS hoặc typography solution hợp lý hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **115. Third-party DOM sâu** tiếp nhận điểm tựa từ **114. Complex rich-text styling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **116. CSS tính năng (feature / 기능) có cú pháp (syntax / 문법) phức tạp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 115. Third-party DOM sâu

Một editor thư viện (library / 라이브러리) có nội bộ (internal / 내부) DOM cây (tree / 트리) thay đổi theo phiên bản (version / 버전). Một biểu định kiểu (stylesheet / 스타일시트) tích hợp (integration / 통합) rõ ràng tốt hơn biến thể tùy ý (arbitrary variant) cực dài trong gốc (root / 루트) lớp (class / 클래스).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **116. CSS tính năng (feature / 기능) có cú pháp (syntax / 문법) phức tạp** tiếp nhận điểm tựa từ **115. Third-party DOM sâu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **117. Chọn đúng lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 116. CSS tính năng (feature / 기능) có cú pháp (syntax / 문법) phức tạp

Animation keyframes, advanced bộ chọn (selector) hoặc print biểu định kiểu (stylesheet / 스타일시트) có thể đọc tốt hơn khi viết CSS trực tiếp.

Tailwind hỗ trợ arbitrary/custom API, nhưng không phải mọi CSS nên được convert thành tiện ích (utility).

---

# PHẦN XXIII — MASTER quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **117. Chọn đúng lớp trừu tượng (abstraction / 추상화)** tiếp nhận điểm tựa từ **116. CSS tính năng (feature / 기능) có cú pháp (syntax / 문법) phức tạp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **118. Lab: scanner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 117. Chọn đúng lớp trừu tượng (abstraction / 추상화)

Nếu vấn đề là atomic styling với cốt lõi (core / 핵심) CSS thuộc tính (property / 속성), dùng tiện ích (utility).

Nếu giá trị (value / 값) là exception một lần, dùng giá trị tùy ý (arbitrary value).

Nếu giá trị (value / 값) lặp thành thiết kế (design / 설계) vocabulary, dùng `@theme`.

Nếu giá trị (value / 값) thay đổi thời gian chạy (runtime / 런타임), dùng CSS custom thuộc tính (property / 속성).

Nếu dự án (project / 프로젝트) thiếu một atomic tiện ích (utility) reusable, dùng `@utility`.

Nếu điều kiện (condition / 조건) bộ chọn (selector) lặp lại, dùng `@custom-variant`.

Nếu bộ chọn (selector) phức tạp nhưng cục bộ (local / 로컬)/mang tính ngữ nghĩa (semantic / 의미적), dùng CSS.

Nếu cấu trúc (structure / 구조) + style + trạng thái (state / 상태) lặp lại, extract thành phần (component / 컴포넌트).

Nếu nguồn (source / 소스) nằm ngoài automatic scan, dùng `@source`.

Đây là cách cấp cao (senior / 시니어) tránh “mọi thứ thành tiện ích (utility)” hoặc “mọi thứ thành custom CSS”.

---

# PHẦN XXIV — MASTER LABS

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **117. Chọn đúng lớp trừu tượng (abstraction / 추상화)** cho ta quy tắc; **118. Lab: scanner** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **119. Lab: strict theme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 118. Lab: scanner

Tạo bốn trường hợp:
- literal `bg-blue-600`,
- động (dynamic / 동적) ``bg-${color}-600``,
- static map khóa–giá trị (map),
- lớp (class / 클래스) trong workspace gói (package / 패키지).

Bản dựng (build / 빌드) và inspect generated CSS. Mục tiêu là tự nhìn thấy scanner ranh giới (boundary / 경계).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **118. Lab: scanner** cho ta quy tắc; **119. Lab: strict theme** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **120. Lab: functional tiện ích (utility)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 119. Lab: strict theme

Reset color không gian tên (namespace / 네임스페이스), chỉ define:
- surface,
- văn bản (text / 텍스트),
- hành động (action / 동작),
- danger.

Sau đó thử dùng `bg-blue-500` và quan sát API không còn. Mục tiêu là hiểu `@theme` điều khiển tiện ích (utility) vocabulary.

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **119. Lab: strict theme** cho ta quy tắc; **120. Lab: functional tiện ích (utility)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **121. Lab: nguồn (source / 소스) split** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 120. Lab: functional tiện ích (utility)

Tạo `tab-*` hỗ trợ:
- theme giá trị (value / 값),
- integer,
- arbitrary,
- bare default.

Sau đó inspect generated CSS cho từng form.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **120. Lab: functional tiện ích (utility)** cho ta quy tắc; **121. Lab: nguồn (source / 소스) split** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **122. Lab: thời gian chạy (runtime / 런타임) CSS biến (variable)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 121. Lab: nguồn (source / 소스) split

Tạo admin/storefront bundles với `source(none)`.

Đo:
- CSS raw kích thước (size / 크기),
- overlap,
- candidate count.

Mục tiêu là hiểu phát hiện nguồn (source detection) như bundle kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **121. Lab: nguồn (source / 소스) split** cho ta quy tắc; **122. Lab: thời gian chạy (runtime / 런타임) CSS biến (variable)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **123. Lab: bộ chứa (container / 컨테이너) thành phần (component / 컴포넌트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 122. Lab: thời gian chạy (runtime / 런타임) CSS biến (variable)

API giá trị (value / 값):
- width,
- color.

Không dùng động (dynamic / 동적) arbitrary lớp (class / 클래스).

Cầu nối (bridge / 브리지) bằng CSS vars và static các tiện ích (utilities).

---

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **122. Lab: thời gian chạy (runtime / 런타임) CSS biến (variable)** cho ta quy tắc; **123. Lab: bộ chứa (container / 컨테이너) thành phần (component / 컴포넌트)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **124. Lab: v3 chuyển đổi (migration)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 123. Lab: bộ chứa (container / 컨테이너) thành phần (component / 컴포넌트)

Cùng một ProfileCard đặt trong:
- sidebar 280px,
- content 600px,
- modal 900px.

Dùng truy vấn vùng chứa (container query) thay vùng nhìn (viewport) điểm ngắt (breakpoint) cho nội bộ (internal / 내부) bố cục (layout / 레이아웃).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **123. Lab: bộ chứa (container / 컨테이너) thành phần (component / 컴포넌트)** cho ta quy tắc; **124. Lab: v3 chuyển đổi (migration)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **125. Lab: embedded widget** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 124. Lab: v3 chuyển đổi (migration)

Lấy dự án (project / 프로젝트) có:
- `tailwind.config.js`,
- content,
- danh sách ép giữ (safelist),
- custom tiện ích (utility) plugin.

Migrate từng phần sang v4 ưu tiên CSS (CSS-first), nhưng giữ hồi quy giao diện (visual regression) snapshots để đảm bảo hành vi (behavior / 동작) không đổi.

---

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **124. Lab: v3 chuyển đổi (migration)** cho ta quy tắc; **125. Lab: embedded widget** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **126. Bạn đã đạt mức master khi nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125. Lab: embedded widget

Nhúng widget vào một legacy page.

Thử:
- full Tailwind import,
- disable Preflight (lớp reset nền của Tailwind),
- prefix,
- isolate sources.

Quan sát host page bị ảnh hưởng thế nào.

---

# PHẦN XXV — MASTER SELF-CHECK

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **125. Lab: embedded widget** cho ta quy tắc; **126. Bạn đã đạt mức master khi nào?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **127. Trước khi merge một Tailwind tính năng (feature / 기능) lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126. Bạn đã đạt mức master khi nào?

Bạn chưa cần nhớ mọi tiện ích (utility). Thay vào đó, bạn nên có thể giải thích bằng lời của mình vì sao Tailwind không generate động (dynamic / 동적) interpolated lớp (class / 클래스); tại sao `@theme` là trình biên dịch (compiler / 컴파일러) API chứ không chỉ CSS các biến (variables); tại sao theme đơn vị từ (token / 토큰) rename có thể là breaking thay đổi (change / 변경); tại sao nguồn (source / 소스) boundaries nên thiết kế theo bundle quyền sở hữu (ownership / 소유권); vì sao `@container-size` không nên thay toàn bộ `@container`; functional tiện ích (utility) resolver hoạt động ở bản dựng (build / 빌드) thời gian (time / 시간) ra sao; vì sao HTML lớp (class / 클래스) thứ tự (order / 순서) không phải CSS thứ tự nguồn (source order); `@reference` có role gì trong isolated biểu định kiểu (stylesheet / 스타일시트); tại sao thời gian chạy (runtime / 런타임) dữ liệu (data / 데이터) nên đi qua CSS biến (variable); vì sao ARIA và dữ liệu (data / 데이터) attributes không interchangeable về ngữ nghĩa (semantics / 의미론); và khi nào Tailwind lớp trừu tượng (abstraction / 추상화) bắt đầu làm mã (code / 코드) khó hiểu hơn plain CSS.

Bạn cũng nên gỡ lỗi (debug / 디버그) được một issue theo chuỗi xử lý (pipeline / 파이프라인):

```text
source
→ candidate
→ generated rule
→ cascade
→ layout
```

thay vì thêm lớp (class / 클래스) thử từng cái.

---

# PHẦN XXVI — môi trường vận hành (production / 운영 환경) CHECK

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **127. Trước khi merge một Tailwind tính năng (feature / 기능) lớn** tiếp nhận điểm tựa từ **126. Bạn đã đạt mức master khi nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **128. tính tương thích (compatibility / 호환성) boundaries: v3 codebase, v4 codebase và gói (package / 패키지) contracts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127. Trước khi merge một Tailwind tính năng (feature / 기능) lớn

Hãy đọc thành phần (component / 컴포넌트) như một hệ thống. Xác định quyền sở hữu hành vi đáp ứng (responsive ownership) thuộc vùng nhìn (viewport) hay bộ chứa (container / 컨테이너). Xác định trạng thái (state / 상태) là bản địa (native / 네이티브), ARIA, dữ liệu (data / 데이터) hay nghiệp vụ (business / 비즈니스) trạng thái (state / 상태). Kiểm tra các giá trị tùy ý (arbitrary values) có đang lặp thành hidden đơn vị từ (token / 토큰) hay không. Kiểm tra focus, disabled, giảm chuyển động (reduced motion). Với thành phần (component / 컴포넌트) reusable, xác định lớp (class / 클래스) override chính sách (policy / 정책). Với monorepo/gói (package / 패키지), xác định nguồn (source / 소스) scanner có nhìn thấy lớp (class / 클래스) hay không. Sau cùng, inspect generated CSS khi có custom tiện ích (utility)/biến thể (variant) hoặc xung đột (conflict / 충돌) khó.

Đây không phải checklist để tick máy móc; đây là cách cấp cao (senior / 시니어) đọc hiện thực (implementation / 구현) trước khi PR trở thành technical debt.

---

# PHẦN XXVII — TÀI LIỆU CHÍNH THỨC

Tailwind CSS documentation:

https://tailwindcss.com/docs

Tailwind CSS v4.3 bản phát hành (release / 릴리스):

https://tailwindcss.com/blog/tailwindcss-v4-3

các biến chủ đề (theme variables):

https://tailwindcss.com/docs/theme

Detecting classes in nguồn (source / 소스) files:

https://tailwindcss.com/docs/detecting-classes-in-source-files

các hàm (functions) and directives:

https://tailwindcss.com/docs/functions-and-directives

thiết kế đáp ứng (responsive design) and các truy vấn vùng chứa (container queries):

https://tailwindcss.com/docs/responsive-design

Styling các tiện ích (utilities):

https://tailwindcss.com/docs/styling-with-utility-classes

Upgrade guide:

https://tailwindcss.com/docs/upgrade-guide

---

---

# PHẦN XXVIII — phiên bản (version / 버전) BOUNDARIES VÀ CSS ánh xạ (mapping / 매핑) Ở MỨC MASTER

> **Chuyển mạch:** Trong **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **128. tính tương thích (compatibility / 호환성) boundaries: v3 codebase, v4 codebase và gói (package / 패키지) contracts** tiếp nhận điểm tựa từ **127. Trước khi merge một Tailwind tính năng (feature / 기능) lớn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **129. tiện ích (utility) ánh xạ (mapping / 매핑) phải dừng ở CSS khi khung phần mềm (framework / 프레임워크) đã hoàn thành nhiệm vụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 128. tính tương thích (compatibility / 호환성) boundaries: v3 codebase, v4 codebase và gói (package / 패키지) contracts

Một design-system/gói (package / 패키지) không nên chỉ nói “dùng Tailwind”. Nếu nguồn (source / 소스) gói (package / 패키지) dựa `@theme`, functional `@utility`, `@container-size` hoặc v4.3 các tiện ích (utilities), bên tiêu thụ (consumer / 소비자) minimum phiên bản (version / 버전) là một phần của gói (package / 패키지) đặc tả hợp đồng (contract / 계약). Ngược lại, một gói (package / 패키지) viết cho v3 có thể phụ thuộc JS plugin/cấu hình (config / 설정)/content ngữ nghĩa (semantics / 의미론) mà v4 bên tiêu thụ (consumer / 소비자) cần chuyển đổi (migration) cầu nối (bridge / 브리지).

V3 và v4 khác ở quyền sở hữu (ownership / 소유권) mô hình (model / 모델). V3 thường tập trung cấu hình (configuration / 구성) trong JavaScript; v4 đưa theme/nguồn (source / 소스)/customization vào CSS điểm vào (entrypoint / 진입점). Vì vậy thư viện (library / 라이브러리) chuyển đổi (migration) phải quyết định gói (package / 패키지) ship nguồn (source / 소스) components, compiled CSS hay theme-only CSS. Mỗi lựa chọn tạo coupling khác nhau với bên tiêu thụ (consumer / 소비자) Tailwind phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **129. tiện ích (utility) ánh xạ (mapping / 매핑) phải dừng ở CSS khi khung phần mềm (framework / 프레임워크) đã hoàn thành nhiệm vụ** tiếp nhận điểm tựa từ **128. tính tương thích (compatibility / 호환성) boundaries: v3 codebase, v4 codebase và gói (package / 패키지) contracts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **130. Upgrade chiến lược (strategy / 전략) cho Tailwind môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 129. tiện ích (utility) ánh xạ (mapping / 매핑) phải dừng ở CSS khi khung phần mềm (framework / 프레임워크) đã hoàn thành nhiệm vụ

Master gỡ lỗi (debugging) cần một “handoff quy tắc (rule / 규칙)”: nếu tiện ích (utility) candidate được generate và computed khai báo (declaration) đúng, dừng gỡ lỗi (debug / 디버그) Tailwind. Từ thời điểm đó, dùng CSS mô hình tư duy (mental model / 사고 모델): lớp phân tầng (cascade layer), khối chứa tham chiếu (containing block / 컨테이닝 블록), định cỡ nội tại (intrinsic sizing / 내재 크기 결정), ngữ cảnh định dạng (formatting context / 서식 컨텍스트), stacking, overflow, paint/composite. khung phần mềm (framework / 프레임워크) không có tầng (layer / 계층) bí mật phía sau trình duyệt (browser / 브라우저).

Điều này đặc biệt quan trọng với `flex-1`, `min-w-0`, `grid-cols-*`, `sticky`, `z-*`, `truncate`, `aspect-*`, bộ chứa (container / 컨테이너) các biến thể (variants) và motion các tiện ích (utilities). Mỗi lớp (class / 클래스) chỉ là authoring API cho CSS hành vi (behavior / 동작) đã tồn tại. Biết handoff điểm (point / 지점) giúp nhóm (team / 팀) phân loại bug nhanh và viết docs/components không thần bí hóa Tailwind.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tailwind CSS — Master Supplement, bản giải thích đầy đủ**, **130. Upgrade chiến lược (strategy / 전략) cho Tailwind môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **129. tiện ích (utility) ánh xạ (mapping / 매핑) phải dừng ở CSS khi khung phần mềm (framework / 프레임워크) đã hoàn thành nhiệm vụ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 130. Upgrade chiến lược (strategy / 전략) cho Tailwind môi trường vận hành (production / 운영 환경)

Khi nâng minor/major phiên bản (version / 버전), hãy kiểm tra (audit / 감사) theo ba lớp. Lớp trình biên dịch (compiler / 컴파일러) gồm phát hiện ứng viên lớp (candidate detection), nguồn (source / 소스) quyền sở hữu (ownership / 소유권), custom các tiện ích (utilities)/các biến thể (variants) và plugin tích hợp (integration / 통합). Lớp generated CSS gồm Preflight (lớp reset nền của Tailwind), layers, các biến chủ đề (theme variables), naming/trạng thái ngừng khuyến nghị (deprecation) và bundle kích thước (size / 크기). Lớp trình duyệt (browser / 브라우저) gồm hồi quy giao diện (visual regression), khả năng tiếp cận (accessibility / 접근성) các trạng thái (states) và mức hỗ trợ trình duyệt (browser support / 브라우저 지원) của CSS tính năng (feature / 기능) mới.

Tính đến 21/09/2026, Tailwind blog vẫn ghi v4.3 là bản phát hành (release / 릴리스) khung phần mềm (framework / 프레임워크) mới nhất; vì vậy chuẩn gốc (canonical / 정본) ghi chú (note / 노트) giữ v4.3 làm đường cơ sở (baseline) nhưng phiên bản (version / 버전) evolution phải được hiểu theo generation, không hard-code giả định (assumption / 가정) rằng API hôm nay sẽ bất biến. Mỗi lần upgrade, đọc chuyển đổi (migration)/bản phát hành (release / 릴리스) notes và diff đầu ra (output / 출력) thay vì chỉ chạy `npm install`.

---

# KẾT LUẬN

Ở mức (level / 수준) beginner, Tailwind có vẻ là:

```text
class → CSS property
```

Ở mức (level / 수준) cấp cao (senior / 시니어), Tailwind trở thành:

```text
utility composition
+ state variants
+ component architecture
+ design tokens
```

Ở mức (level / 수준) master, bạn nhìn thấy toàn chuỗi xử lý (pipeline / 파이프라인):

```text
source ownership
→ candidate detection
→ theme/public API
→ custom utility grammar
→ variant algebra
→ cascade layers
→ browser
```

Điểm quan trọng nhất là không để Tailwind trở thành black box. Nếu khung phần mềm (framework / 프레임워크) làm bạn khó hiểu CSS hơn, lớp trừu tượng (abstraction / 추상화) đang bị dùng sai. Nếu Tailwind giúp thiết kế (design / 설계) vocabulary rõ hơn, nguồn (source / 소스) gần thành phần (component / 컴포넌트) hơn, responsive/trạng thái (state / 상태) declarative hơn và bản dựng (build / 빌드) đầu ra (output / 출력) predictable hơn, bạn đang dùng nó đúng ở mức cấp cao (senior / 시니어)/master.

> **Bàn giao:** Sau **130. Upgrade chiến lược (strategy / 전략) cho Tailwind môi trường vận hành (production / 운영 환경)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
