# SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**. Route đi từ compile-time CSS authoring và syntax → variables, nesting, selectors và modules → mixins/functions/control flow → architecture, responsive systems và debugging → modern Sass migration, để lộ trình tăng độ sâu theo cơ chế.

> **Mục tiêu:** học SCSS như một **thời điểm biên dịch (compile-time) ngôn ngữ (language / 언어) để author CSS**, không dùng Sass để che việc chưa hiểu CSS.
>
> Tài liệu này nối tiếp:
>
> ```văn bản (text / 텍스트)
> CSS_Beginner_to_Senior_2026.md
> CSS_Master_Supplement_2026.md
> ```
>
> đường cơ sở (baseline) (audit 2026-09):
> - Dùng **Dart Sass 1.104.1** làm mốc tài liệu hiện tại.
> - Ưu tiên **`@use` / `@forward`**.
> - Không xây mã (code / 코드) mới dựa trên Sass `@import`.
> - Ưu tiên built-in modules: `sass:math`, `sass:color`, `sass:list`, `sass:map`, `sass:string`, `sass:selector`, `sass:meta`.
>
> Ký hiệu:
> - **[cốt lõi (core / 핵심)]**: phải biết.
> - **[ADV]**: cấp cao (senior / 시니어) nên thành thạo.
> - **[ARCH]**: kiến trúc (architecture / 아키텍처) / thư viện (library / 라이브러리) thiết kế (design / 설계).
> - **⚠ PITFALL**: lỗi thường gặp.
> - **Idiom**: cách viết Sass quen thuộc.
> - **mẫu lập trình (coding pattern / 코딩 패턴)**: mẫu (pattern / 패턴) hiện thực (implementation / 구현).
> - **mẫu thiết kế (design pattern / 디자인 패턴)**: kiến trúc (architecture / 아키텍처) mẫu (pattern / 패턴).

---

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ Sass/SCSS được viết theo hướng tiếng Việt dễ hiểu nhưng vẫn giữ từ gốc để tra cứu. Ví dụ: **thời điểm biên dịch (compile-time)**, **thời gian chạy (runtime / 런타임)**, **phạm vi (scope / 범위)**, **không gian tên (namespace / 네임스페이스)**, **đồ thị mô-đun (module graph)**, **nội suy (interpolation)**, **che khuất biến (shadowing)**, **luồng điều khiển (control flow)** và **hợp nhất bộ chọn (selector unification)**. Những tên directive, hàm (function / 함수), mô-đun (module / 모듈) và cú pháp Sass nằm trong mã vẫn được giữ nguyên.

# 0. SCSS thực sự là gì?

# 0A. mô hình tư duy (mental model / 사고 모델) xuyên suốt: SCSS là chương trình chạy trước CSS

SCSS phải được học như một thời điểm biên dịch (compile-time) ngôn ngữ (language / 언어) dùng để author/generate CSS. `$variables`, các map khóa–giá trị (maps), loops, các khối trộn tái sử dụng (mixins), các hàm (functions) và đồ thị mô-đun (module graph) được Dart Sass xử lý trước khi trình duyệt (browser / 브라우저) nhìn thấy trang. Kết quả cuối cùng chỉ là CSS. Vì vậy Sass biến (variable) không cơ chế phân tầng (cascade), không inherit và không thay đổi thời gian chạy (runtime / 런타임); CSS custom thuộc tính (property / 속성) thì có thể tham gia cơ chế phân tầng (cascade), kế thừa (inheritance) và thời gian chạy (runtime / 런타임) overrides.

Trục học chuẩn gốc (canonical / 정본) của SCSS là:

```text
Sass values / variables
→ nesting + selector generation
→ mixins / functions như compile-time abstraction
→ lists / maps / control flow để generate CSS
→ @use / @forward tạo module graph
→ partials + entry points tổ chức source
→ @extend như selector unification, không phải OOP inheritance
→ architecture + public API
→ compiler deprecations / migration
→ CSS output quality + compile performance
```

Khi đọc SCSS, luôn hỏi trình biên dịch (compiler / 컴파일러) sẽ emit CSS gì, bao nhiêu quy tắc (rule / 규칙), bộ chọn (selector) nào và ở vị trí nào. khối trộn tái sử dụng (mixin) include nhiều lần có thể duplicate các khai báo (declarations). vòng lặp (loop / 루프) có thể tạo hàng nghìn rules. lồng cú pháp (nesting) sâu có thể sinh bộ chọn (selector) độ đặc hiệu (specificity) cao và coupling với DOM. nguồn (source / 소스) ngắn hơn không đồng nghĩa đầu ra (output / 출력) tốt hơn.

các biến (variables) phù hợp với thời điểm biên dịch (compile-time) calculation/generation. CSS custom các thuộc tính (properties) phù hợp với thời gian chạy (runtime / 런타임) theme, cascade-based thành phần (component / 컴포넌트) contracts và các giá trị (values) cần override trong DevTools/thời gian chạy (runtime / 런타임). các khối trộn tái sử dụng (mixins) nên mô tả khai báo (declaration) set hoặc content wrapper có parameterization rõ. các hàm (functions) nên trả giá trị (value / 값) và tránh tác dụng phụ (side effect). các map khóa–giá trị (maps) hữu ích khi thực sự biểu diễn structured cấu hình (configuration / 구성); map khóa–giá trị (map) lồng sâu chỉ để “gom mọi thứ” thường biến API thành khó dùng.

Hiện đại (modern / 현대적) hệ mô-đun (module system) là `@use` và `@forward`. `@use` tạo không gian tên (namespace / 네임스페이스), phạm vi (scope / 범위) members trong tệp (file / 파일) dùng và tải (load / 로드) mô-đun (module / 모듈) một lần. `@forward` tạo facade/bề mặt công khai (public surface). các tệp (file / 파일) thành phần (partials) chỉ là tổ chức nguồn (source / 소스); chúng không tự tạo kiến trúc mô-đun (module architecture) nếu mã (code / 코드) vẫn nối bằng legacy `@import`. Sass `@import` và toàn cục (global / 전역) built-ins đã đã ngừng khuyến nghị (deprecated) từ Dart Sass 1.80.0 nên mã (code / 코드) mới không nên xây trên toàn cục (global / 전역) không gian tên (namespace / 네임스페이스) cũ.

`@extend` cũng không phải kế thừa (inheritance) kiểu Java. Sass thực hiện hợp nhất bộ chọn (selector unification) để các bộ chọn (selector) mở rộng cùng nhận rules, vì thế đầu ra (output / 출력) có thể xuất hiện xa nơi gọi và khó dự đoán. Placeholder `%foo` có use trường hợp (case / 사례), nhưng khối trộn tái sử dụng (mixin), tiện ích (utility)/composition hoặc CSS kiến trúc (architecture / 아키텍처) thường tường minh (explicit / 명시적) hơn. SCSS tốt phải làm CSS đầu ra (output / 출력) dễ hiểu hơn, không che CSS đi.

Sass là biểu định kiểu (stylesheet / 스타일시트) ngôn ngữ (language / 언어) compile thành CSS.

SCSS là cú pháp (syntax / 문법) của Sass có hình thức gần CSS:

```scss
$brand: #2563eb;

.button {
  color: $brand;

  &:hover {
    color: white;
  }
}
```

Compile thành:

```css
.button {
  color: #2563eb;
}

.button:hover {
  color: white;
}
```

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Mô hình tư duy (mental model / 사고 모델) quan trọng** gom các mảnh từ **Quy ước thuật ngữ Việt–Anh** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델) quan trọng

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
SCSS source
→ Sass compiler
→ CSS output
→ Browser
```

Trình duyệt (browser / 브라우저) **không biết**:
- `$variable`,
- `@mixin`,
- `@function`,
- Sass map khóa–giá trị (map),
- Sass vòng lặp (loop / 루프).

Trình duyệt (browser / 브라우저) chỉ nhận CSS cuối.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델) quan trọng** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Sass biến (variable)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Nếu hành vi (behavior / 동작) phụ thuộc thời gian chạy (runtime / 런타임):
- theme,
- cơ chế phân tầng (cascade),
- kế thừa (inheritance),
- bộ chứa (container / 컨테이너),
- người dùng (user / 사용자) preference,

thường CSS custom thuộc tính (property / 속성) phù hợp hơn Sass biến (variable).

---

# 1. SCSS vs CSS Custom các thuộc tính (properties) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Sass variables được resolve lúc compile; CSS custom properties tồn tại ở runtime, nên senior rules phải chọn đúng boundary giữa hai loại.

## Sass biến (variable)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$space-4: 1rem;
```

thời điểm biên dịch (compile-time).

Sau compile:

```css
/* $space-4 biến mất */
```

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **CSS custom thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **Sass biến (variable)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) — thời điểm biên dịch (compile-time) constants + thời gian chạy (runtime / 런타임) tokens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSS custom thuộc tính (property / 속성)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
:root {
  --space-4: 1rem;
}
```

Tồn tại thời gian chạy (runtime / 런타임).

Có:
- cơ chế phân tầng (cascade),
- kế thừa (inheritance),
- thời gian chạy (runtime / 런타임) override,
- DevTools visibility.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Mẫu (pattern / 패턴) — thời điểm biên dịch (compile-time) constants + thời gian chạy (runtime / 런타임) tokens** tiếp nhận điểm tựa từ **CSS custom thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) — thời điểm biên dịch (compile-time) constants + thời gian chạy (runtime / 런타임) tokens

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```scss
$prefix: "app";

:root {
  --color-brand: #2563eb;
}
```

Sass:
- generate cấu trúc (structure / 구조),
- bản dựng (build / 빌드) đơn vị từ (token / 토큰) tables,
- tiện ích (utility) generation.

CSS các biến (variables):
- theme/thời gian chạy (runtime / 런타임) hợp đồng thành phần (component contract).

---

# 2. Cài đặt và CLI [cốt lõi (core / 핵심)]

Nút (node / 노드) dự án (project / 프로젝트):

```bash
npm install --save-dev sass
```

Compile:

```bash
npx sass src/styles.scss dist/styles.css
```

Watch:

```bash
npx sass --watch src:dist
```

Compressed đầu ra (output / 출력):

```bash
npx sass src/styles.scss dist/styles.css --style=compressed
```

Bản đồ mã nguồn (source map / 소스 맵) hành vi (behavior / 동작) tùy CLI/bản dựng (build / 빌드) tích hợp (integration / 통합).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) — thời điểm biên dịch (compile-time) constants + thời gian chạy (runtime / 런타임) tokens** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Idiom** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙)

Trong app hiện đại thường Sass chạy thông qua:
- Vite,
- webpack,
- Angular CLI,
- khung phần mềm (framework / 프레임워크) bundler.

Không cần tự chạy CLI nếu công cụ bản dựng (build / 빌드) (build tool) đã quản lý.

---

# 3. tệp (file / 파일) Naming: các tệp (file / 파일) thành phần (partials) [cốt lõi (core / 핵심)]

Tệp (file / 파일) private/nội bộ (internal / 내부) thường bắt đầu `_`:

```text
_variables.scss
_mixins.scss
_button.scss
```

Tải (load / 로드):

```scss
@use "variables";
```

Không cần viết:
- `_variables.scss`,
- extension `.scss`.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Idiom** tiếp nhận điểm tựa từ **Môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Naming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Idiom

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
styles/
├─ _tokens.scss
├─ _mixins.scss
├─ components/
│  ├─ _button.scss
│  └─ _card.scss
└─ main.scss
```

---

# 4. Comments [cốt lõi (core / 핵심)]

Silent comment:

```scss
// only in SCSS source
```

Không xuất CSS.

Loud comment:

```scss
/* may be emitted */
```

Có thể xuất CSS tùy đầu ra (output / 출력) chế độ (mode / 모드).

License/preserved comment:

```scss
/*!
 * License
 */
```

Thường được giữ kể cả compressed đầu ra (output / 출력).

---

# 5. Sass các biến (variables) [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$brand: #2563eb;
$radius: 0.75rem;
$spacing-unit: 0.25rem;
```

Use:

```scss
.button {
  border-radius: $radius;
}
```

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Naming** tiếp nhận điểm tựa từ **Idiom** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어) ghi chú (note / 노트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Naming

Hyphen và underscore lịch sử được Sass coi tương đương trong identifiers:

```scss
$font-size
$font_size
```

có thể refer cùng name ngữ nghĩa (semantics / 의미론).

**Không lợi dụng điều này.** Chọn một convention: thường kebab-case.

---

# 6. biến (variable) phạm vi (scope / 범위) [cốt lõi (core / 핵심)]

Top-level:

```scss
$brand: blue;

.button {
  color: $brand;
}
```

Cục bộ (local / 로컬):

```scss
.component {
  $gap: 1rem;
  gap: $gap;
}
```

Cục bộ (local / 로컬) biến (variable) không nên assume available toàn cục (global / 전역).

---

# 7. che khuất biến (shadowing) [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$color: blue;

.card {
  $color: red;
  color: $color;
}

.link {
  color: $color;
}
```

Đầu ra (output / 출력):
- card red,
- link blue.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) ghi chú (note / 노트)** tiếp nhận điểm tựa từ **Naming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **⚠ PITFALL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) ghi chú (note / 노트)

che khuất biến (shadowing) quá nhiều khiến SCSS khó reason.

Ưu tiên:
- cục bộ (local / 로컬) biến (variable) tên rõ,
- mô-đun (module / 모듈) các không gian tên (namespaces).

---

# 8. `!default` [cốt lõi (core / 핵심)][ARCH]

Thư viện (library / 라이브러리) biến (variable):

```scss
$button-radius: 0.5rem !default;
```

Ý nghĩa:
> set giá trị (value / 값) nếu biến (variable) chưa được configured/set theo mô-đun (module / 모듈) ngữ nghĩa (semantics / 의미론).

Dùng cho **configurable thư viện (library / 라이브러리) defaults**.

Không dùng `!default` cho mọi biến (variable).

---

# 9. `!global` [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$flag: false;

@mixin enable {
  $flag: true !global;
}
```

Có thể modify toàn cục (global / 전역) biến (variable).

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ PITFALL** tiếp nhận điểm tựa từ **Cấp cao (senior / 시니어) ghi chú (note / 노트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠ PITFALL

`!global` tạo hidden trạng thái có thể thay đổi (mutable state).

Cấp cao (senior / 시니어) quy tắc (rule / 규칙):
- tránh trong ứng dụng (application / 애플리케이션) SCSS,
- ưu tiên các hàm (functions) return giá trị (value / 값),
- mô-đun (module / 모듈) cấu hình (config / 설정) rõ ràng.

---

# 10. Sass dữ liệu (data / 데이터) Types [cốt lõi (core / 핵심)]

Sass các giá trị (values) gồm:

```text
numbers
strings
colors
lists
maps
booleans
null
calculation values
function references
```

---

# 11. Numbers & Units [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$size: 16px;
$ratio: 1.5;
$angle: 45deg;
$duration: 200ms;
```

Sass hiểu units mathematically.

```scss
@use "sass:math";

$half: math.div(20px, 2);
```

Kết quả (result / 결과):

```text
10px
```

---

# 12. Division — dùng `math.div()` [cốt lõi (core / 핵심)]

Không viết Sass arithmetic mới:

```scss
$half: 20px / 2;
```

Dùng:

```scss
@use "sass:math";

$half: math.div(20px, 2);
```

Lý do:
- `/` trong CSS ngày càng là separator.
- Grid, hiện đại (modern / 현대적) colors, ratios dùng `/`.

CSS đầu ra (output / 출력) vẫn có thể chứa slash:

```scss
.item {
  grid-row: span 3 / 7;
}
```

---

# 13. Numeric Operators [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$a: 10px + 5px;
$b: 10px - 2px;
$c: 4 * 3;
```

Division:
```scss
math.div(...)
```

Comparisons:

```scss
$a > $b
$a >= $b
$a == $b
$a != $b
```

---

# 14. đơn vị (unit / 단위) tính tương thích (compatibility / 호환성) [ADV]

Sass có đơn vị (unit / 단위) arithmetic.

Valid:

```scss
1in + 96px
```

vì convertible.

Không phải mọi units compatible:

```text
px + s
```

là conceptual lỗi (error / 오류).

Useful `sass:math`:

```scss
math.compatible(1cm, 10mm)
```

---

# 15. Strings [cốt lõi (core / 핵심)]

Quoted:

```scss
$name: "Inter";
```

Unquoted:

```scss
$display: block;
```

nội suy (interpolation):

```scss
.#{$name} {}
```

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **⚠ PITFALL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **⚠ PITFALL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy tắc (rule / 규칙)

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này giải thích cơ chế SCSS trước khi đưa ra rule hoặc code. Hãy theo dõi compile-time behavior, CSS output, scope và edge case khi tích hợp vào project lớn.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

Không quote mọi identifier nếu CSS cần identifier.

---

# 16. nội suy (interpolation) `#{}` [cốt lõi (core / 핵심)]

bộ chọn (selector):

```scss
$variant: danger;

.button-#{$variant} {
  color: red;
}
```

Thuộc tính (property / 속성):

```scss
$side: left;

margin-#{$side}: 1rem;
```

String:

```scss
$url: "hero";

background-image:
  url("/images/#{$url}.jpg");
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ PITFALL** tiếp nhận điểm tựa từ **Quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) — Optional khai báo (declaration)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠ PITFALL

nội suy (interpolation) là powerful nhưng dễ biến Sass thành template spaghetti.

Đừng generate arbitrary các bộ chọn (selectors) nếu mang tính ngữ nghĩa (semantic / 의미적) lớp (class / 클래스) rõ hơn.

---

# 17. Booleans [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$enabled: true;
$disabled: false;
```

Used:

```scss
@if $enabled {
  ...
}
```

---

# 18. `null` [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$value: null;
```

Sass thường không emit khai báo (declaration) nếu giá trị (value / 값) là `null`.

```scss
$border: null;

.card {
  border: $border;
}
```

Có thể compile mà khai báo (declaration) không xuất.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Mẫu (pattern / 패턴) — Optional khai báo (declaration)** tiếp nhận điểm tựa từ **⚠ PITFALL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Important** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) — Optional khai báo (declaration)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```scss
@mixin box($radius: null) {
  @if $radius != null {
    border-radius: $radius;
  }
}
```

---

# 19. các danh sách (lists) [cốt lõi (core / 핵심)]

Space-separated:

```scss
$spacing: 4px 8px 16px;
```

Comma-separated:

```scss
$fonts: Inter, Arial, sans-serif;
```

Bracketed:

```scss
$list: [a, b, c];
```

Slash-separated các giá trị (values) cũng tồn tại.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Important** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) — Optional khai báo (declaration)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **⚠ PITFALL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Important

Sass danh sách (list / 목록) không giống JS Array hoàn toàn.

- separator là siêu dữ liệu (metadata / 메타데이터),
- bracketed/unbracketed matter,
- individual giá trị (value / 값) cũng có list-like hành vi (behavior / 동작).

---

# 20. `sass:list` [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@use "sass:list";

$items: red, green, blue;
```

Dùng chung (common / 공통):

```scss
list.length($items)
list.nth($items, 1)
list.append($items, orange)
list.index($items, green)
list.join($a, $b)
list.separator($items)
```

Hiện đại (modern / 현대적) mô-đun (module / 모듈) API ưu tiên không gian tên (namespace / 네임스페이스).

---

# 21. danh sách (list / 목록) Indexing [cốt lõi (core / 핵심)]

Sass historically indexes từ **1**, không phải 0.

```scss
list.nth($items, 1)
```

→ first item.

Negative chỉ mục (index / 인덱스) có thể refer từ cuối tùy hàm (function / 함수) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ PITFALL** tiếp nhận điểm tựa từ **Important** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠ PITFALL

Dev từ JS/Java dễ nhầm 0-based.

---

# 22. các map khóa–giá trị (maps) [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$colors: (
  primary: #2563eb,
  danger: #dc2626,
  success: #16a34a
);
```

map khóa–giá trị (map) = key/giá trị (value / 값) collection.

Use:

```scss
@use "sass:map";

.button {
  color: map.get($colors, primary);
}
```

---

# 23. `sass:map` [cốt lõi (core / 핵심)]

Dùng chung (common / 공통):

```scss
map.get($map, $key)
map.has-key($map, $key)
map.keys($map)
map.values($map)
map.merge($map1, $map2)
map.remove($map, $keys...)
map.set(...)
map.deep-merge(...)
map.deep-remove(...)
```

Availability của deep APIs cần Dart Sass hiện đại.

---

# 24. Nested các map khóa–giá trị (maps) [cốt lõi (core / 핵심)/ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$theme: (
  colors: (
    primary: #2563eb,
    danger: #dc2626
  ),
  radius: (
    sm: .25rem,
    md: .5rem
  )
);
```

Get:

```scss
map.get($theme, colors, primary)
```

Hiện đại (modern / 현대적) Dart Sass hỗ trợ nested keys ở mô-đun (module / 모듈) các hàm (functions) phù hợp.

---

# 25. map khóa–giá trị (map) as cấu hình (configuration / 구성) [ARCH]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$button-sizes: (
  sm: (
    padding: .375rem .625rem,
    font-size: .875rem
  ),
  md: (
    padding: .5rem .875rem,
    font-size: 1rem
  )
);
```

Generate styles:

```scss
@each $name, $config in $button-sizes {
  .button--#{$name} {
    padding: map.get($config, padding);
    font-size: map.get($config, font-size);
  }
}
```

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **⚠ PITFALL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **⚠ Legacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

map khóa–giá trị (map) tốt khi:
- finite thiết kế (design / 설계) dữ liệu (data / 데이터),
- generation có quy luật.

map khóa–giá trị (map) xấu khi:
- recreate entire DOM/thành phần (component / 컴포넌트) cây (tree / 트리) as cấu hình (configuration / 구성).

---

# 26. Colors [cốt lõi (core / 핵심)]

Sass understands colors.

```scss
$brand: #2563eb;
```

Hiện đại (modern / 현대적) CSS color spaces:
- rgb,
- hsl,
- hwb,
- lab/lch,
- oklab/oklch,
- display-p3,
- others.

Hiện đại (modern / 현대적) Sass color APIs phải xét color không gian (space / 공간) rõ hơn trước đây.

---

# 27. `sass:color` [cốt lõi (core / 핵심)/ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@use "sass:color";
```

Dùng chung (common / 공통) hiện đại (modern / 현대적) APIs:

```scss
color.adjust(...)
color.scale(...)
color.change(...)
color.channel(...)
color.to-space(...)
color.is-powerless(...)
```

Example:

```scss
$hover:
  color.scale(
    #2563eb,
    $lightness: -12%,
    $space: oklch
  );
```

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ Legacy** tiếp nhận điểm tựa từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pattern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠ Legacy

Các toàn cục (global / 전역)/legacy các hàm (functions) như:
- `lighten()`,
- `darken()`,
- old channel getters,

không nên là default cho mã (code / 코드) mới.

---

# 28. Sass vs CSS Color các hàm (functions) [ADV]

Nếu muốn thời gian chạy (runtime / 런타임) color derived từ CSS biến (variable):

```css
background:
  color-mix(
    in oklab,
    var(--brand),
    black 10%
  );
```

Sass không thể thời điểm biên dịch (compile-time) resolve thời gian chạy (runtime / 런타임) custom thuộc tính (property / 속성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Pattern** tiếp nhận điểm tựa từ **⚠ Legacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pattern
Phần này nối kiến thức vừa học với “Pattern”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
Static design generation → Sass color APIs
Runtime theme color       → CSS color functions
```

---

# 29. lồng cú pháp (nesting) [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
.card {
  padding: 1rem;

  .title {
    font-weight: 700;
  }
}
```

Đầu ra (output / 출력):

```css
.card {
  padding: 1rem;
}

.card .title {
  font-weight: 700;
}
```

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Pattern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **⚠ PITFALL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

lồng cú pháp (nesting) không phải mục tiêu của Sass.

lồng cú pháp (nesting) chỉ nên giúp:
- các trạng thái (states),
- pseudo các bộ chọn (selectors),
- cục bộ (local / 로컬) slots,
- contextual rules.

---

# 30. Parent bộ chọn (selector) `&` [cốt lõi (core / 핵심)]

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```scss
.button {
  &:hover {}
  &:focus-visible {}
}
```

Đầu ra (output / 출력):

```css
.button:hover {}
.button:focus-visible {}
```

biến thể (variant):

```scss
.button {
  &--danger {}
}
```

Đầu ra (output / 출력):

```css
.button--danger {}
```

---

# 31. Parent bộ chọn (selector) ngữ cảnh (context / 맥락) [ADV]

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```scss
.button {
  .theme-dark & {
    color: white;
  }
}
```

Đầu ra (output / 출력):

```css
.theme-dark .button {}
```

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ PITFALL** tiếp nhận điểm tựa từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Recommendation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠ PITFALL

Ngữ cảnh (context / 맥락) inversion dễ tạo hidden coupling.

Theme hiện đại thường tốt hơn qua CSS các biến (variables):

```css
[data-theme="dark"] {
  --button-bg: ...;
}
```

---

# 32. thuộc tính (property / 속성) lồng cú pháp (nesting) [ADV/LEGACY AWARENESS]

Sass có cú pháp (syntax / 문법) nested các thuộc tính (properties) lịch sử:

```scss
font: {
  family: Inter;
  size: 1rem;
}
```

Có thể compile thành:
- `font-family`,
- `font-size`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Recommendation** tiếp nhận điểm tựa từ **⚠ PITFALL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Recommendation

Không ưu tiên cú pháp (syntax / 문법) này cho mã (code / 코드) mới.

Plain các khai báo (declarations) dễ tìm kiếm (search / 검색)/read hơn.

---

# 33. Mixed các khai báo (declarations) + Nested Rules [cốt lõi (core / 핵심)]

Hiện đại (modern / 현대적) Sass đã align hành vi (behavior / 동작) với CSS lồng cú pháp (nesting):
các khai báo (declarations) giữ thứ tự xuất hiện ngay cả khi interleaved với nested rules.

```scss
.example {
  color: red;

  &--serious {
    font-weight: bold;
  }

  font-weight: normal;
}
```

Đừng assume Sass tự hoist các khai báo (declarations) như historical versions.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Recommendation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Viết các khai báo (declarations) có thứ tự (order / 순서) rõ:
- cơ sở (base / 기반) các khai báo (declarations) trước,
- nested các bộ chọn (selectors)/trạng thái (state / 상태) sau,

nếu không có lý do cần interleave.

---

# 34. Placeholder các bộ chọn (selectors) `%` [ADV]

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```scss
%control-base {
  border: 1px solid;
  border-radius: .5rem;
}
```

Extend:

```scss
.button {
  @extend %control-base;
}
```

Placeholder tự nó không emit bộ chọn (selector) nếu không được extend.

---

# 35. `@extend` [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
.error {
  color: red;
}

.validation-error {
  @extend .error;
}
```

Sass **merges các bộ chọn (selectors)**, không bản sao (copy / 복사) các khai báo (declarations) đơn giản.

Đầu ra (output / 출력) có thể:

```css
.error,
.validation-error {
  color: red;
}
```

---

# 36. `@extend` mô hình tư duy (mental model / 사고 모델) [ADV]

`@extend` nói:

> bộ chọn (selector) A phải behave như một instance của bộ chọn (selector) B.

Nó là hợp nhất bộ chọn (selector unification)/rewriting.

Không nghĩ:

> bản sao (copy / 복사) khối (block / 블록) CSS của B vào A.

---

# 37. `@extend` Pitfalls [ADV]

Có thể:
- tạo bộ chọn (selector) đầu ra (output / 출력) lớn,
- nối các bộ chọn (selectors) xa nhau,
- coupling khó thấy,
- khó predict trong legacy toàn cục (global / 전역) imports.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Ưu tiên:
1. dùng chung (shared / 공유) lớp (class / 클래스),
2. khối trộn tái sử dụng (mixin),
3. tiện ích (utility),
4. đơn vị từ (token / 토큰),

trước `@extend` nếu ngữ nghĩa (semantics / 의미론) không thật sự là bộ chọn (selector) kế thừa (inheritance).

---

# 38. Placeholder + Extend mẫu (pattern / 패턴) [ADV]

Nếu cần extend, placeholder thường an toàn hơn extend concrete lớp (class / 클래스):

```scss
%button-base {
  display: inline-flex;
  align-items: center;
}

.button {
  @extend %button-base;
}
```

Không làm `.button` trở thành mang tính ngữ nghĩa (semantic / 의미적) extension của công khai (public / 공개) lớp (class / 클래스) khác.

---

# 39. các khối trộn tái sử dụng (mixins) [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@mixin visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
}
```

Use:

```scss
.sr-only {
  @include visually-hidden;
}
```

---

# 40. khối trộn tái sử dụng (mixin) Arguments [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@mixin square($size) {
  width: $size;
  height: $size;
}
```

```scss
.avatar {
  @include square(3rem);
}
```

---

# 41. Default Arguments [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@mixin focus-ring(
  $width: 3px,
  $offset: 3px
) {
  outline: $width solid currentColor;
  outline-offset: $offset;
}
```

---

# 42. từ khóa (keyword / 키워드) Arguments [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@include focus-ring(
  $offset: 4px,
  $width: 2px
);
```

Useful khi:
- nhiều optional params,
- boolean params,
- API clarity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thiết kế (design / 설계) lesson** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)

Renaming công khai (public / 공개) khối trộn tái sử dụng (mixin) argument có thể là breaking thay đổi (change / 변경) vì callers dùng từ khóa (keyword / 키워드) arguments.

---

# 43. Arbitrary Arguments `$args...` [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@mixin box-shadow($shadows...) {
  box-shadow: $shadows;
}
```

Lời gọi (call / 호출):

```scss
@include box-shadow(
  0 1px 2px #0002,
  0 8px 24px #0002
);
```

---

# 44. Passing các danh sách (lists)/các map khóa–giá trị (maps) as Arguments [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$args: 1rem, 2rem;

@include some-mixin($args...);
```

map khóa–giá trị (map) có thể expand từ khóa (keyword / 키워드) arguments:

```scss
$options: (
  $size: 2rem,
  $radius: .5rem
);

@include box($options...);
```

Use carefully; tường minh (explicit / 명시적) arguments thường readable hơn.

---

# 45. Content Blocks `@content` [cốt lõi (core / 핵심)/ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@mixin hover-capable {
  @media (hover: hover) {
    &:hover {
      @content;
    }
  }
}
```

Use:

```scss
.button {
  @include hover-capable {
    transform: translateY(-1px);
  }
}
```

---

# 46. Content khối (block / 블록) Arguments [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@mixin media-types($types...) {
  @each $type in $types {
    @media #{$type} {
      @content($type);
    }
  }
}
```

Caller:

```scss
@include media-types(screen, print)
using ($type) {
  ...
}
```

Advanced thư viện (library / 라이브러리) technique.

---

# 47. Content phạm vi (scope / 범위) [ADV]

`@content` khối (block / 블록) is lexically scoped:
- sees các biến (variables) at include site,
- không automatically see khối trộn tái sử dụng (mixin) cục bộ (local / 로컬) các biến (variables) như động (dynamic / 동적) phạm vi (scope / 범위).

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Thiết kế (design / 설계) lesson** tiếp nhận điểm tựa từ **Thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết kế (design / 설계) lesson

khối trộn tái sử dụng (mixin) content khối (block / 블록) giống thời điểm biên dịch (compile-time) higher-order style khối (block / 블록).

---

# 48. các hàm (functions) [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@function rem($px, $base: 16px) {
  @return math.div($px, $base) * 1rem;
}
```

Use:

```scss
.title {
  font-size: rem(24px);
}
```

Need:

```scss
@use "sass:math";
```

---

# 49. hàm (function / 함수) vs khối trộn tái sử dụng (mixin) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Hàm (function / 함수)** tiếp nhận điểm tựa từ **Thiết kế (design / 설계) lesson** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **khối trộn tái sử dụng (mixin)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm (function / 함수)

Return **giá trị (value / 값)**:

```scss
@function space($step) {
  @return $step * .25rem;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **khối trộn tái sử dụng (mixin)** tiếp nhận điểm tựa từ **Hàm (function / 함수)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rule** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## khối trộn tái sử dụng (mixin)

Emit **styles/rules**:

```scss
@mixin stack($gap) {
  display: flex;
  flex-direction: column;
  gap: $gap;
}
```

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Rule** tiếp nhận điểm tựa từ **khối trộn tái sử dụng (mixin)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pattern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rule
Phần này nối kiến thức vừa học với “Rule”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
Value transformation → function
Style generation     → mixin
```

---

# 50. hàm (function / 함수) thiết kế (design / 설계) [ADV]

Good hàm (function / 함수):
- deterministic,
- return giá trị (value / 값),
- kiểm tra hợp lệ (validation / 검증) rõ,
- tên nói mang tính ngữ nghĩa (semantic / 의미적) intent.

Bad:

```scss
@function do-everything(...) { ... }
```

Không bản dựng (build / 빌드) mini ứng dụng (application / 애플리케이션) ngôn ngữ (language / 언어) trong Sass nếu CSS/custom các thuộc tính (properties) đủ.

---

# 51. Private Members [cốt lõi (core / 핵심)][ARCH]

Names bắt đầu `_` hoặc `-` historically treated private mô-đun (module / 모듈) members:

```scss
$_internal-scale: ...;

@function _helper(...) {}
```

Bên tiêu thụ (consumer / 소비자) mô-đun (module / 모듈) không nên truy cập (access / 접근).

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Pattern** tiếp nhận điểm tựa từ **Rule** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pattern
Mẫu này phân biệt public và private member, giúp người mới hiểu phần nào có thể dùng từ bên ngoài module và phần nào chỉ phục vụ nội bộ.

```text
Public:
$tokens
@mixin button
@function space

Private:
$_raw-data
@function _normalize
```

---

# 52. `@if` / `@else` [CORE]
Phần này nối kiến thức vừa học với “52. `@if` / `@else` [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@mixin surface($elevated: false) {
  background: white;

  @if $elevated {
    box-shadow: 0 8px 24px #0002;
  }
}
```

Else:

```scss
@if $theme == dark {
  ...
} @else {
  ...
}
```

---

# 53. Truthiness [cốt lõi (core / 핵심)]

Trong Sass:
- `false`,
- `null`

là falsey.

Nhiều giá trị (value / 값) khác truthy, kể cả:
- `0`,
- empty strings/các danh sách (lists) theo Sass ngữ nghĩa (semantics / 의미론).

Đừng assume JS truthiness.

---

# 54. `@each` [cốt lõi (core / 핵심)]

Danh sách (list / 목록):

```scss
$sizes: sm, md, lg;

@each $size in $sizes {
  .text-#{$size} {
    ...
  }
}
```

map khóa–giá trị (map):

```scss
@each $name, $value in $colors {
  .text-#{$name} {
    color: $value;
  }
}
```

---

# 55. `@for` [cốt lõi (core / 핵심)]

Exclusive `to`:

```scss
@for $i from 1 to 4 {
  ...
}
```

→ 1,2,3.

Inclusive `through`:

```scss
@for $i from 1 through 4 {
  ...
}
```

→ 1,2,3,4.

---

# 56. `@while` [ADV]
Phần này nối kiến thức vừa học với “56. `@while` [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
$i: 1;

@while $i <= 3 {
  .order-#{$i} {
    order: $i;
  }

  $i: $i + 1;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Pattern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu thiết kế (design pattern / 디자인 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

`@while` hiếm khi cần.

Nếu `@each`/`@for` đủ, dùng chúng vì predictable hơn.

---

# 57. vòng lặp (loop / 루프) Generation Pitfall [ADV]

Có thể generate:

```scss
@for $i from 1 through 1000 {
  .m-#{$i} { ... }
}
```

Nhưng compile được ≠ nên làm.

Concern:
- CSS kích thước (size / 크기),
- dead các tiện ích (utilities),
- API explosion.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Mẫu thiết kế (design pattern / 디자인 패턴)** tiếp nhận điểm tựa từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **⚠ PITFALL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu thiết kế (design pattern / 디자인 패턴)

Generate từ **bounded thiết kế (design / 설계) quy mô (scale / 규모)**, không từ mọi possible number.

---

# 58. Error Handling: `@error` [CORE/ADV]
Phần này nối kiến thức vừa học với “58. Error Handling: `@error` [CORE/ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@function spacing($step) {
  @if $step < 0 {
    @error "spacing step must be >= 0";
  }

  @return $step * .25rem;
}
```

Good thư viện (library / 라이브러리) API:
- thất bại (fail / 실패) fast,
- message useful.

---

# 59. `@warn` [ADV]
Phần này nối kiến thức vừa học với “59. `@warn` [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@warn "Deprecated mixin. Use new-name().";
```

Use:
- chuyển đổi (migration) notice,
- suspicious but compilable đầu vào (input / 입력).

Không spam warning cho normal usage.

---

# 60. `@debug` [CORE]
Phần này nối kiến thức vừa học với “60. `@debug` [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@debug $tokens;
```

Useful:
- inspect các map khóa–giá trị (maps)/các danh sách (lists),
- hàm (function / 함수) development.

Không xem đầu ra (output / 출력) format như stable môi trường vận hành (production / 운영 환경) API.

---

# 61. `@use` — Modern hệ mô-đun (module system) [CORE]
Phần này nối kiến thức vừa học với “61. `@use` — Modern hệ mô-đun (module system) [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@use "tokens";
```

Members accessed by không gian tên (namespace / 네임스페이스):

```scss
.button {
  color: tokens.$brand;
}
```

khối trộn tái sử dụng (mixin):

```scss
@include tokens.some-mixin;
```

Hàm (function / 함수):

```scss
width: tokens.some-function(...);
```

---

# 62. mô-đun (module / 모듈) Loaded Once [cốt lõi (core / 핵심)]

`@use` mô-đun (module / 모듈):
- execute once,
- CSS emit once,
- dùng chung (shared / 공유) mô-đun (module / 모듈) định danh (identity / 식별자).

Đây là khác biệt lớn so với legacy `@import`.

---

# 63. không gian tên (namespace) Alias [CORE]
Phần này nối kiến thức vừa học với “63. không gian tên (namespace) Alias [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@use "design/tokens" as t;
```

```scss
.button {
  color: t.$brand;
}
```

Good khi mô-đun (module / 모듈) name dài.

---

# 64. `as *` [ADV]
Phần này nối kiến thức vừa học với “64. `as *` [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@use "tokens" as *;
```

Members vào cục bộ (local / 로컬) không gian tên (namespace / 네임스페이스).

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ PITFALL** tiếp nhận điểm tựa từ **Mẫu thiết kế (design pattern / 디자인 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Important** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠ PITFALL

Làm mất provenance:

```scss
color: $brand;
```

Không biết `$brand` từ đâu.

Cấp cao (senior / 시니어) quy tắc (rule / 규칙):
- ứng dụng (application / 애플리케이션) small tệp (file / 파일) có thể dùng có kiểm soát,
- thư viện (library / 라이브러리)/large codebase nên giữ không gian tên (namespace / 네임스페이스).

---

# 65. mô-đun (module / 모듈) cấu hình (configuration / 구성) `with` [cốt lõi (core / 핵심)][ARCH]

Mô-đun (module / 모듈):

```scss
// _theme.scss
$brand: #2563eb !default;
$radius: .5rem !default;
```

Bên tiêu thụ (consumer / 소비자):

```scss
@use "theme" with (
  $brand: rebeccapurple,
  $radius: 1rem
);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Important** tiếp nhận điểm tựa từ **⚠ PITFALL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Important

Mô-đun (module / 모듈) must be configured **before first tải (load / 로드)**.

Mô-đun (module / 모듈) is loaded once.

---

# 66. cấu hình (configuration / 구성) đặc tả hợp đồng (contract / 계약) [ARCH]

Configurable biến (variable):
- giao diện công khai (public API),
- nên có `!default`,
- naming stable,
- docs rõ.

Đừng expose every nội bộ (internal / 내부) constant.

---

# 67. `@forward` [cốt lõi (core / 핵심)][ARCH]

Thư viện (library / 라이브러리) facade:

```scss
// _index.scss
@forward "tokens";
@forward "mixins";
@forward "functions";
```

Bên tiêu thụ (consumer / 소비자):

```scss
@use "design-system";
```

Có một điểm vào (entrypoint / 진입점) thay vì 20 imports.

---

# 68. `@forward` vs `@use` [cốt lõi (core / 핵심)]

`@forward`:
- re-export công khai (public / 공개) members cho downstream.

`@use`:
- use members trong hiện tại (current / 현재) mô-đun (module / 모듈).

Nếu tệp (file / 파일) cần cả hai:

```scss
@forward "theme";
@use "theme";
```

Thường forward trước để cấu hình (configuration / 구성) luồng (flow / 흐름) predictable.

---

# 69. Forward Prefix [ADV]
Phần này nối kiến thức vừa học với “69. Forward Prefix [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@forward "list" as list-*;
```

Mô-đun (module / 모듈) member:

```scss
reset
```

Downstream:

```scss
library.list-reset
```

Useful:
- giao diện công khai (public API) clarity,
- avoid collisions.

---

# 70. `show` / `hide` [ADV]
Phần này nối kiến thức vừa học với “70. `show` / `hide` [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@forward "internal"
  show $brand, button;
```

Hoặc:

```scss
@forward "internal"
  hide _helper;
```

Use giao diện công khai (public API) curation.

---

# 71. Forward cấu hình (configuration / 구성) [ADV][ARCH]

Facade có thể set opinionated defaults:

```scss
@forward "library" with (
  $radius: .75rem !default
);
```

Downstream vẫn có thể override nếu forward cấu hình (config / 설정) cho phép.

Mẫu (pattern / 패턴):
```text
Core library
→ opinionated facade
→ application config
```

---

# 72. chỉ mục (index / 인덱스) Files [cốt lõi (core / 핵심)]

Directory:

```text
tokens/
├─ _color.scss
├─ _spacing.scss
└─ _index.scss
```

`_index.scss`:

```scss
@forward "color";
@forward "spacing";
```

Bên tiêu thụ (consumer / 소비자):

```scss
@use "tokens";
```

---

# 73. tải (load / 로드) Paths [ADV]

Trình biên dịch (compiler / 컴파일러) có thể configure tải (load / 로드) paths.

Thay vì:

```scss
@use "../../../shared/tokens";
```

có thể:

```scss
@use "shared/tokens";
```

Cấu hình (configuration / 구성) tùy:
- CLI,
- bundler,
- JS API.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Important** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **mô hình tư duy (mental model)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Avoid ambiguous mô-đun (module / 모듈) resolution.
Document tải (load / 로드) paths.

---

# 74. Built-in Modules Overview [CORE]
Phần này nối kiến thức vừa học với “74. Built-in Modules Overview [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@use "sass:math";
@use "sass:string";
@use "sass:color";
@use "sass:list";
@use "sass:map";
@use "sass:selector";
@use "sass:meta";
```

Toàn cục (global / 전역) built-ins là legacy direction.
Dùng namespaced mô-đun (module / 모듈) APIs cho mã (code / 코드) mới.

---

# 75. `sass:math` [cốt lõi (core / 핵심)]

Useful:

```text
math.div
math.max
math.min
math.round
math.ceil
math.floor
math.abs
math.clamp
math.compatible
math.is-unitless
math.unit
math.percentage
```

Có thêm constants/các hàm (functions) nâng cao tùy Dart Sass phiên bản (version / 버전).

Example:

```scss
@use "sass:math";

@function fluid-step($min, $max, $ratio) {
  @return $min + ($max - $min) * $ratio;
}
```

---

# 76. CSS `min()` vs Sass `math.min()` [ADV]

CSS:

```css
width: min(100%, 70rem);
```

Thời gian chạy (runtime / 런타임) trình duyệt (browser / 브라우저) calculation.

Sass:

```scss
math.min(10px, 20px)
```

thời điểm biên dịch (compile-time) numeric hàm (function / 함수).

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **mô hình tư duy (mental model)** gom các mảnh từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Pattern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## mô hình tư duy (mental model)
Phần này nối kiến thức vừa học với “mô hình tư duy (mental model)”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
Known at compile time → sass:math
Depends on layout     → CSS math function
```

---

# 77. `sass:string` [ADV]

Dùng chung (common / 공통):

```text
string.quote
string.unquote
string.index
string.insert
string.slice
string.to-upper-case
string.to-lower-case
string.unique-id
```

Use cases:
- generated names,
- parsing limited thời điểm biên dịch (compile-time) tokens,
- thư viện (library / 라이브러리) các tiện ích (utilities).

Don't bản dựng (build / 빌드) complex văn bản (text / 텍스트) processing engine in Sass.

---

# 78. `sass:selector` [ADV]

Powerful bộ chọn (selector) engine API:

```text
selector.is-superselector
selector.append
selector.extend
selector.nest
selector.parse
selector.replace
selector.unify
selector.simple-selectors
```

Example:

```scss
@use "sass:selector";

$result:
  selector.unify(
    ".alert",
    ".danger"
  );
```

Useful for library-level bộ chọn (selector) metaprogramming.

---

# 79. bộ chọn (selector) các hàm (functions) — Use Carefully [ADV]

If you frequently need động (dynamic / 동적) bộ chọn (selector) manipulation:
- kiến trúc (architecture / 아키텍처) may be too clever.

Good:
- khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) lớp trừu tượng (abstraction / 추상화).

Bad:
- normal app thành phần (component / 컴포넌트).

---

# 80. `sass:meta` [ADV]

Reflection/introspection.

Useful APIs include concepts:

```text
meta.type-of
meta.inspect
meta.module-variables
meta.module-functions
meta.module-mixins
meta.function-exists
meta.mixin-exists
meta.variable-exists
meta.global-variable-exists
meta.get-function
meta.call
meta.apply
meta.keywords
meta.load-css
```

Availability depends Dart Sass phiên bản (version / 버전).

---

# 81. `meta.type-of()` [ADV]
Phần này nối kiến thức vừa học với “81. `meta.type-of()` [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@use "sass:meta";

@debug meta.type-of(10px); // number
@debug meta.type-of(#fff); // color
```

Useful kiểm tra hợp lệ (validation / 검증).

---

# 82. Dynamic hàm (function) References [ADV]
Phần này nối kiến thức vừa học với “82. Dynamic hàm (function) References [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
$fn: meta.get-function("some-function");
$result: meta.call($fn, ...);
```

Useful:
- generic đơn vị từ (token / 토큰) transforms,
- plugin-like thời điểm biên dịch (compile-time) patterns.

Use sparingly.

---

# 83. `meta.load-css()` [ADV]

Tải (load / 로드) mô-đun (module / 모듈) CSS dynamically in khối trộn tái sử dụng (mixin)/ngữ cảnh (context / 맥락).

Use trường hợp (case / 사례):
- conditional CSS emission,
- advanced thư viện (library / 라이브러리) kiến trúc (architecture / 아키텍처).

Not replacement for normal `@use`.

---

# 84. Sass kiến trúc (architecture / 아키텍처) — 7-1 Awareness [ARCH]

Classic 7-1 mẫu (pattern / 패턴):

```text
abstracts/
base/
components/
layout/
pages/
themes/
vendors/
main.scss
```

Useful as historical organization mô hình (model / 모델).

But don't apply mechanically.

Hiện đại (modern / 현대적) modules allow more tính năng (feature / 기능)/component-oriented cấu trúc (structure / 구조).

---

# 85. Recommended Modern SCSS Structure [ARCH]
Phần này nối kiến thức vừa học với “85. Recommended Modern SCSS Structure [ARCH]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
styles/
├─ settings/
│  ├─ _tokens.scss
│  ├─ _config.scss
│  └─ _index.scss
│
├─ tools/
│  ├─ _functions.scss
│  ├─ _mixins.scss
│  └─ _index.scss
│
├─ base/
│  ├─ _reset.scss
│  └─ _typography.scss
│
├─ layout/
│  ├─ _stack.scss
│  ├─ _cluster.scss
│  └─ _container.scss
│
├─ components/
│  ├─ _button.scss
│  ├─ _card.scss
│  └─ _dialog.scss
│
├─ utilities/
│  └─ _index.scss
│
└─ main.scss
```

---

# 86. Feature-oriented cấu trúc (structure / 구조) [ARCH]

Trong thành phần (component / 컴포넌트) app:

```text
features/
├─ profile/
│  ├─ _tokens.scss
│  ├─ _profile-card.scss
│  └─ _index.scss
└─ checkout/
   └─ ...
```

Good khi:
- thành phần (component / 컴포넌트)/lĩnh vực (domain / 도메인) quyền sở hữu (ownership / 소유권) quan trọng hơn toàn cục (global / 전역) style categories.

---

# 87. Entry điểm (point / 지점) mẫu (pattern / 패턴) [ARCH]

`main.scss` chỉ compose modules:

```scss
@use "base/reset";
@use "base/typography";
@use "layout";
@use "components";
@use "utilities";
```

Đừng đặt 1000 lines thành phần (component / 컴포넌트) CSS trong `main.scss`.

---

# 88. Library Facade Pattern [ARCH]
Phần này nối kiến thức vừa học với “88. Library Facade Pattern [ARCH]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
design-system/
├─ _index.scss
├─ _tokens.scss
├─ _mixins.scss
├─ _functions.scss
└─ components/
```

`_index.scss`:

```scss
@forward "tokens";
@forward "mixins";
@forward "functions";
```

Bên tiêu thụ (consumer / 소비자):

```scss
@use "design-system" as ds;
```

---

# 89. Sass Token map khóa–giá trị (map) Pattern [CORE/ARCH]
Phần này nối kiến thức vừa học với “89. Sass Token map khóa–giá trị (map) Pattern [CORE/ARCH]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
$spacing: (
  0: 0,
  1: .25rem,
  2: .5rem,
  3: .75rem,
  4: 1rem,
  6: 1.5rem
);
```

Hàm (function / 함수):

```scss
@function space($step) {
  @if not map.has-key($spacing, $step) {
    @error "Unknown spacing step: #{$step}";
  }

  @return map.get($spacing, $step);
}
```

---

# 90. Generate CSS các biến (variables) from Sass map khóa–giá trị (map) [CORE/ARCH]
Phần này nối kiến thức vừa học với “90. Generate CSS các biến (variables) from Sass map khóa–giá trị (map) [CORE/ARCH]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@use "sass:map";

$colors: (
  brand: #2563eb,
  danger: #dc2626,
  surface: #fff
);

:root {
  @each $name, $value in $colors {
    --color-#{$name}: #{$value};
  }
}
```

Đầu ra (output / 출력) thời gian chạy (runtime / 런타임) tokens.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Pattern** gom các mảnh từ **mô hình tư duy (mental model)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Decision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pattern
Phần này nối kiến thức vừa học với “Pattern”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
Sass data source
→ generated CSS custom properties
→ browser runtime theming
```

---

# 91. Nested Token Generation [ADV]
Phần này nối kiến thức vừa học với “91. Nested Token Generation [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
$tokens: (
  color: (
    brand: #2563eb,
    danger: #dc2626
  ),
  space: (
    1: .25rem,
    2: .5rem
  )
);
```

Có thể viết recursive generator.

Nhưng recursion belongs more in master supplement.

---

# 92. tiện ích (utility) Generation Pattern [CORE/ADV]
Phần này nối kiến thức vừa học với “92. tiện ích (utility) Generation Pattern [CORE/ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
$spaces: (
  1: .25rem,
  2: .5rem,
  4: 1rem
);

@each $name, $value in $spaces {
  .gap-#{$name} {
    gap: $value;
  }
}
```

Cấp cao (senior / 시니어) concern:
- CSS đầu ra (output / 출력) kích thước (size / 크기),
- design-system phạm vi (scope / 범위),
- naming consistency.

---

# 93. điểm ngắt (breakpoint) khối trộn tái sử dụng (mixin) mẫu (pattern / 패턴) [cốt lõi (core / 핵심)]

Cấu hình (config / 설정):

```scss
$breakpoints: (
  sm: 36rem,
  md: 48rem,
  lg: 64rem
);
```

khối trộn tái sử dụng (mixin):

```scss
@mixin up($name) {
  $value: map.get($breakpoints, $name);

  @if $value == null {
    @error "Unknown breakpoint #{$name}";
  }

  @media (width >= $value) {
    @content;
  }
}
```

Use:

```scss
.card {
  @include up(md) {
    display: grid;
  }
}
```

---

# 94. điểm ngắt (breakpoint) khối trộn tái sử dụng (mixin) — cấp cao (senior / 시니어) Caveat [ADV]

Không biến mọi truy vấn môi trường (media query) thành opaque khối trộn tái sử dụng (mixin).

Bản địa (native / 네이티브):

```scss
@media (width >= 48rem) {}
```

đôi khi rõ hơn.

khối trộn tái sử dụng (mixin) đáng dùng khi:
- enforce thiết kế (design / 설계) điểm ngắt (breakpoint) đặc tả hợp đồng (contract / 계약),
- dùng chung (shared / 공유) ngữ nghĩa (semantics / 의미론),
- kiểm tra hợp lệ (validation / 검증).

---

# 95. Responsive hiện đại (modern / 현대적) mẫu (pattern / 패턴) [ADV]

Sass điểm ngắt (breakpoint) map khóa–giá trị (map) cho **page các điểm ngắt (breakpoints)**.

các truy vấn vùng chứa (container queries) vẫn nên viết CSS:

```scss
.card-shell {
  container-type: inline-size;
}

@container (width >= 30rem) {
  ...
}
```

Không compile bộ chứa (container / 컨테이너) dimensions thành vùng nhìn (viewport) kiến trúc (architecture / 아키텍처).

---

# 96. khối trộn tái sử dụng (mixin) for Repeated khai báo (declaration) Set [cốt lõi (core / 핵심)]

Good:

```scss
@mixin focus-ring {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

Bad:

```scss
@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

không hẳn luôn bad, nhưng tiện ích (utility)/bố cục (layout / 레이아웃) lớp (class / 클래스) có thể reusable thời gian chạy (runtime / 런타임) tốt hơn nếu dùng nhiều.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Decision** tiếp nhận điểm tựa từ **Pattern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **⚠ Caveat** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decision
Phần này nối kiến thức vừa học với “Decision”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
Need CSS class composition? → utility/layout primitive
Need compile-time inline style set? → mixin
```

---

# 97. truy vấn môi trường (media query) Content khối trộn tái sử dụng (mixin) Idiom [CORE]
Phần này nối kiến thức vừa học với “97. truy vấn môi trường (media query) Content khối trộn tái sử dụng (mixin) Idiom [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@mixin reduced-motion {
  @media (prefers-reduced-motion: reduce) {
    @content;
  }
}
```

```scss
.motion {
  animation: pulse 1s infinite;

  @include reduced-motion {
    animation: none;
  }
}
```

Readable nếu nhóm (team / 팀) dùng convention này.

---

# 98. trạng thái (state / 상태) khối trộn tái sử dụng (mixin) phản mẫu (anti-pattern) [ADV]

Avoid:

```scss
@mixin hover-active-focus-disabled-loading {
  ...
}
```

Nếu khối trộn tái sử dụng (mixin) abstracts mang tính ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) quá sâu, đầu ra (output / 출력) khó inspect.

CSS các trạng thái (states) nên remain visible trong thành phần (component / 컴포넌트) nguồn (source / 소스) khi có thể.

---

# 99. Function-based Scale Pattern [ADV]
Phần này nối kiến thức vừa học với “99. Function-based Scale Pattern [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@function pow-scale($base, $ratio, $step) {
  $value: $base;

  @for $i from 1 through $step {
    $value: $value * $ratio;
  }

  @return $value;
}
```

Could generate kiểu (type / 타입) quy mô (scale / 규모).

But static đơn vị từ (token / 토큰) thiết kế (design tokens) may be easier to rà soát (review / 검토).

Cấp cao (senior / 시니어) asks:
> generation adds giá trị (value / 값) or hides thiết kế (design / 설계) decisions?

---

# 100. BEM + SCSS [CORE/ADV]
Phần này nối kiến thức vừa học với “100. BEM + SCSS [CORE/ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
.card {
  &__title {}
  &__body {}
  &--featured {}
}
```

Works.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ Caveat** tiếp nhận điểm tựa từ **Decision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Use cases** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠ Caveat

Renaming `.card` changes generated các bộ chọn (selectors):
- convenient,
- but searchability less direct.

For large teams, tường minh (explicit / 명시적) các bộ chọn (selectors) may sometimes be clearer:

```scss
.card {}
.card__title {}
.card__body {}
```

SCSS does not require BEM lồng cú pháp (nesting).

---

# 101. CUBE / tiện ích (utility) Composition + SCSS [ARCH]

SCSS can define:
- thiết kế (design / 설계) scales,
- tiện ích (utility) generator,
- thành phần (component / 컴포넌트) tools.

But actual kiến trúc (architecture / 아키텍처) may prefer:
- composition classes,
- các tiện ích (utilities),
- blocks,
- exceptions.

Don't let Sass lồng cú pháp (nesting) push dự án (project / 프로젝트) toward deeply coupled BEM trees.

---

# 102. SCSS mẫu thiết kế (design pattern / 디자인 패턴) — thời điểm biên dịch (compile-time) API [ARCH]

Treat mô-đun (module / 모듈) members as API:

Công khai (public / 공개):
```text
$configuration !default
mixins
functions
forwarded tokens
```

Private:
```text
helper functions
raw maps
implementation mixins
temporary data
```

Consumers should not depend on private internals.

---

# 103. SCSS mẫu thiết kế (design pattern / 디자인 패턴) — Facade mô-đun (module / 모듈) [ARCH]

Nội bộ (internal / 내부) modules:

```text
_color.scss
_spacing.scss
_type.scss
```

Facade:

```scss
@forward "color";
@forward "spacing";
@forward "type";
```

Bên tiêu thụ (consumer / 소비자):

```scss
@use "tokens";
```

Equivalent kiến trúc (architecture / 아키텍처) concept:
- Facade mẫu (pattern / 패턴).

---

# 104. SCSS mẫu thiết kế (design pattern / 디자인 패턴) — cấu hình (configuration / 구성) đối tượng (object / 객체) [ARCH]

Instead of 20 globals:

```scss
$theme: (
  radius: .5rem,
  density: comfortable,
  features: (
    shadows: true,
    gradients: false
  )
);
```

các hàm (functions) truy cập (access / 접근) cấu hình (config / 설정).

But mô-đun (module / 모듈) cấu hình (configuration / 구성) via tường minh (explicit / 명시적) các biến (variables) may be clearer for giao diện công khai (public API).

Use map khóa–giá trị (map) when cấu hình (configuration / 구성) is naturally hierarchical.

---

# 105. SCSS mẫu thiết kế (design pattern / 디자인 패턴) — Generator [ARCH]

Dữ liệu (data / 데이터):

```scss
$utilities: (...);
```

Generator:

```scss
@mixin generate-utilities($config) {
  ...
}
```

Đầu ra (output / 출력):
```text
CSS utility classes
```

Useful for:
- nội bộ (internal / 내부) tiện ích (utility) khung phần mềm (framework / 프레임워크),
- token-derived APIs.

Rủi ro (risk / 위험):
- khung phần mềm (framework / 프레임워크) within khung phần mềm (framework / 프레임워크).

---

# 106. SCSS mẫu thiết kế (design pattern / 디자인 패턴) — Adapter [ARCH]

Third-party thư viện (library / 라이브러리) expects cấu hình (config / 설정):

```scss
$library-primary: ...;
```

Your hệ thống (system / 시스템) uses:
```scss
$tokens: (...);
```

Create adapter mô-đun (module / 모듈):

```scss
$library-primary:
  map.get($tokens, color, brand);
```

Keep vendor ánh xạ (mapping / 매핑) isolated.

---

# 107. SCSS mẫu thiết kế (design pattern / 디자인 패턴) — Anti-Corruption tầng (layer / 계층) [ARCH]

Do not let Bootstrap/vendor names spread across app đơn vị từ (token / 토큰) hệ thống (system / 시스템).

```text
App semantic tokens
→ vendor adapter
→ third-party Sass config
```

This keeps replacement possible later.

---

# 108. `@at-root` [ADV]

Moves nested quy tắc (rule / 규칙) out of hiện tại (current / 현재) lồng cú pháp (nesting) ngữ cảnh (context / 맥락).

```scss
.component {
  @at-root .global-helper {
    ...
  }
}
```

Advanced truy vấn (query / 쿼리) forms can điều khiển (control / 제어) which at-rules/các bộ chọn (selectors) stay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **⚠ Caveat** cho ta quy tắc; **Use cases** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **⚠** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Use cases
Phần này nối kiến thức vừa học với “Use cases”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- thư viện (library / 라이브러리) bộ chọn (selector) generation,
- escape contextual lồng cú pháp (nesting).

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Use cases** cho ta quy tắc; **⚠** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ⚠

Frequent `@at-root` means lồng cú pháp (nesting) kiến trúc (architecture / 아키텍처) may be wrong.

---

# 109. At-rule lồng cú pháp (nesting) [CORE]
Phần này nối kiến thức vừa học với “109. At-rule lồng cú pháp (nesting) [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
.card {
  @media (width >= 48rem) {
    display: grid;
  }
}
```

Sass handles nested at-rules.

Hiện đại (modern / 현대적) CSS lồng cú pháp (nesting) now supports much of this natively, so Sass giá trị (value / 값) here is less unique than before.

---

# 110. Unknown At-rules [cốt lõi (core / 핵심)]

Sass generally passes through CSS at-rules it doesn't specially interpret:

```scss
@container ...
@layer ...
@scope ...
@property ...
@starting-style ...
```

SCSS should remain CSS-compatible.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **⚠** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Don't invent Sass workaround for bản địa (native / 네이티브) CSS tính năng (feature / 기능) if Sass already passes it through.

---

# 111. CSS Custom các thuộc tính (properties) in SCSS [CORE]
Phần này nối kiến thức vừa học với “111. CSS Custom các thuộc tính (properties) in SCSS [CORE]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
:root {
  --brand: #{$brand};
}
```

nội suy (interpolation) may be needed when embedding Sass các giá trị (values) in custom thuộc tính (property / 속성) văn bản (text / 텍스트), depending expression/giá trị (value / 값) ngữ cảnh (context / 맥락).

Example:

```scss
$brand: #2563eb;

:root {
  --brand: #{$brand};
}
```

---

# 112. Custom thuộc tính (property / 속성) Gotcha [ADV]

CSS custom thuộc tính (property / 속성) các giá trị (values) are parsed with CSS custom-property ngữ nghĩa (semantics / 의미론).

When mixing Sass các biến (variables)/các hàm (functions):
- nội suy (interpolation) may be necessary,
- preserve thời gian chạy (runtime / 런타임) cú pháp (syntax / 문법) like `var()`, `calc()`, `color-mix()`.

Don't accidentally make Sass evaluate something intended for trình duyệt (browser / 브라우저).

---

# 113. Sass Calculations vs CSS Calculations [ADV]

Hiện đại (modern / 현대적) Sass understands CSS calculations more intelligently.

Examples:

```scss
width: calc(100% - 2rem);
font-size: clamp(1rem, 2vw, 2rem);
```

Sass may simplify only when mathematically safe/known.

Cấp cao (senior / 시니어) quy tắc (rule / 규칙):
> Keep layout-dependent math in CSS thời gian chạy (runtime / 런타임).

---

# 114. Sass Color 4 Awareness [ADV]

Hiện đại (modern / 현대적) Sass supports CSS Color 4 spaces.

Legacy các giả định (assumptions / 가정들):
```text
every color convertible to simple RGB/HSL
```

are no longer universally safe.

Prefer:
```scss
color.channel(..., $space: ...)
color.adjust(..., $space: ...)
color.scale(..., $space: ...)
color.to-space(...)
```

when color-space ngữ nghĩa (semantics / 의미론) matter.

---

# 115. trạng thái ngừng khuyến nghị (deprecation): Sass `@import` [MUST]

Legacy:

```scss
@import "variables";
@import "mixins";
```

Problems:
- toàn cục (global / 전역) không gian tên (namespace / 네임스페이스),
- repeated thực thi (execution / 실행),
- unclear provenance,
- extend coupling.

Hiện đại (modern / 현대적):

```scss
@use "variables";
@use "mixins";
```

For thư viện (library / 라이브러리) facade:

```scss
@forward ...
```

---

# 116. toàn cục (global / 전역) Built-in hàm (function / 함수) trạng thái ngừng khuyến nghị (deprecation) [MUST]

Legacy:

```scss
map-get($map, key);
lighten($color, 10%);
```

Hiện đại (modern / 현대적):

```scss
@use "sass:map";
@use "sass:color";

map.get($map, key);
color.scale(...);
```

Benefits:
- provenance,
- less CSS hàm (function / 함수) collision,
- future tính tương thích (compatibility / 호환성).

---

# 117. Legacy Slash Division [MUST]

Legacy:

```scss
$half: $size / 2;
```

Hiện đại (modern / 현대적):

```scss
@use "sass:math";

$half: math.div($size, 2);
```

---

# 118. Legacy Color các hàm (functions) [MUST]

Avoid building new APIs around:

```text
red()
green()
blue()
hue()
saturation()
lightness()
lighten()
darken()
```

Use `sass:color` hiện đại (modern / 현대적) APIs with tường minh (explicit / 명시적) color-space thinking.

---

# 119. Sass Migrator [cốt lõi (core / 핵심)/ADV]

Official Sass Migrator helps migrate:
- `@import` → hệ mô-đun (module system),
- division,
- other deprecations/features supported by migrator.

Typical command ecosystem:

```bash
sass-migrator module ...
```

Chính xác (exact / 정확한) installation/flags should be checked against hiện tại (current / 현재) docs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Cấp cao (senior / 시니어) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Token layers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy tắc (rule / 규칙)

chuyển đổi (migration) công cụ (tool / 도구):
- accelerates mechanical changes,
- does not replace kiến trúc (architecture / 아키텍처) rà soát (review / 검토).

---

# 120. trạng thái ngừng khuyến nghị (deprecation) Warnings [cốt lõi (core / 핵심)]

Treat warnings as future bản dựng (build / 빌드) failures.

CI chiến lược (strategy / 전략):
```text
warnings visible
→ inventory
→ migrate
→ optionally fatal for selected deprecations
```

Don't permanently silence all deprecations.

---

# 121. phụ thuộc (dependency / 의존성) Warnings [ADV]

Bản dựng (build / 빌드) can distinguish:
- your mã (code / 코드),
- phụ thuộc (dependency / 의존성) mã (code / 코드).

Useful to silence noisy phụ thuộc (dependency / 의존성) warnings selectively while keeping first-party warnings.

But cập nhật (update / 업데이트) dependencies rather than hiding warnings forever.

---

# 122. các bản đồ mã nguồn (source maps) [cốt lõi (core / 핵심)]

SCSS gỡ lỗi (debugging) needs ánh xạ (mapping / 매핑):

```text
compiled CSS line
↔ SCSS source line
```

Bundlers usually generate các bản đồ mã nguồn (source maps) in dev.

Without them:
- DevTools points to generated CSS,
- kiến trúc (architecture / 아키텍처) gỡ lỗi (debugging) harder.

---

# 123. đầu ra (output / 출력) Styles [cốt lõi (core / 핵심)]

Typical:
- expanded,
- compressed.

Development:
```text
expanded + source map
```

Môi trường vận hành (production / 운영 환경):
```text
compressed/minified via pipeline
```

Your bundler may minify after Sass.

---

# 124. Sass Does Not Autoprefix [MUST]

Sass trình biên dịch (compiler / 컴파일러):
- compiles Sass to CSS.

It does **not inherently replace**:
- Autoprefixer,
- browserslist-based transforms,
- CSS minifier,
- PostCSS chuỗi xử lý (pipeline / 파이프라인).

Typical:

```text
SCSS
→ Sass
→ PostCSS/Autoprefixer
→ minifier
→ CSS
```

depending ngăn xếp (stack / 스택).

---

# 125. SCSS + PostCSS [ADV]

Complementary:

Sass:
- modules,
- các map khóa–giá trị (maps),
- các hàm (functions),
- thời điểm biên dịch (compile-time) generation.

PostCSS ecosystem:
- vendor prefixes,
- transformations,
- lint/plugins,
- bản dựng (build / 빌드) processing.

Don't treat them as competitors by default.

---

# 126. SCSS + CSS Modules [ADV]

Example:

```text
Button.module.scss
```

Two layers:

```text
SCSS
→ compile CSS
→ CSS Modules scopes class names
```

Still can use:
- `@use`,
- tokens,
- các hàm (functions).

Cấp cao (senior / 시니어) ghi chú (note / 노트):
CSS Modules already gives scoping; don't overbuild BEM naming solely for collision avoidance.

---

# 127. SCSS + thành phần (component / 컴포넌트) Frameworks [ADV]

React/Vue/Svelte/etc:

Prefer styles close to quyền sở hữu (ownership / 소유권).

Possible:
```text
component.scss
Component.module.scss
feature/_index.scss
```

Toàn cục (global / 전역) Sass:
- tokens,
- tools,
- cơ sở (base / 기반).

Thành phần (component / 컴포넌트) Sass:
- component-specific CSS.

---

# 128. Sass các biến (variables) vs đơn vị từ (token / 토큰) thiết kế (design tokens) [MUST]

Bad:

```scss
$blue: #2563eb;
```

everywhere.

Better:

```scss
$color-action-primary: #2563eb;
```

Best for thời gian chạy (runtime / 런타임) themes:
generate:

```css
--color-action-primary: ...
```

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Token layers** tiếp nhận điểm tựa từ **Quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **@extend** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Token layers
Phần này nối kiến thức vừa học với “Token layers”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
primitive Sass data
→ semantic token
→ CSS custom property
→ component token
```

---

# 129. Theme Generation Pattern [ADV]
Phần này nối kiến thức vừa học với “129. Theme Generation Pattern [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
$themes: (
  light: (
    surface: white,
    text: #111
  ),
  dark: (
    surface: #111,
    text: #f5f5f5
  )
);

@each $theme-name, $tokens in $themes {
  [data-theme="#{$theme-name}"] {
    @each $token, $value in $tokens {
      --#{$token}: #{$value};
    }
  }
}
```

Good when themes static thời điểm biên dịch (compile-time) set.

---

# 130. Theme Generation Caveat [ADV]

If theme dữ liệu (data / 데이터) comes thời gian chạy (runtime / 런타임)/máy chủ (server / 서버)/người dùng (user / 사용자):
Sass cannot help after compile.

Use CSS các biến (variables)/thời gian chạy (runtime / 런타임) JS/máy chủ (server / 서버) CSS.

---

# 131. Validation hàm (function) Pattern [ADV]
Phần này nối kiến thức vừa học với “131. Validation hàm (function) Pattern [ADV]”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@function token($map, $key) {
  @if not map.has-key($map, $key) {
    @error "Unknown token `#{$key}`.";
  }

  @return map.get($map, $key);
}
```

Thất bại (fail / 실패) fast prevents silent inconsistent thiết kế (design / 설계).

---

# 132. Recursive map khóa–giá trị (map) truy cập (access / 접근) mẫu (pattern / 패턴) [ADV]

Could ghi (write / 쓰기) helper:

```scss
@function get-in($map, $keys...) {
  $current: $map;

  @each $key in $keys {
    $current: map.get($current, $key);
  }

  @return $current;
}
```

But hiện đại (modern / 현대적) `sass:map` nested APIs may already solve this.

Don't reinvent tiêu chuẩn (standard / 표준) các hàm (functions).

---

# 133. Recursive CSS biến (variable) Generator [ADV]

Concept:

```scss
@mixin emit-vars(
  $map,
  $prefix: ""
) {
  @each $key, $value in $map {
    $name:
      if(
        $prefix == "",
        $key,
        "#{$prefix}-#{$key}"
      );

    @if meta.type-of($value) == "map" {
      @include emit-vars($value, $name);
    } @else {
      --#{$name}: #{$value};
    }
  }
}
```

Use:
```scss
:root {
  @include emit-vars($tokens);
}
```

Master supplement sẽ nói deeper về recursion/meta/deprecations.

---

# 134. bộ chọn (selector) Explosion [ADV]

lồng cú pháp (nesting) + `@extend` + loops có thể multiply các bộ chọn (selectors).

Example rủi ro (risk / 위험):

```scss
@each ...
  @extend ...
```

Đầu ra (output / 출력) may be far larger than nguồn (source / 소스).

Always inspect compiled CSS.

---

# 135. nguồn (source / 소스) kích thước (size / 크기) ≠ đầu ra (output / 출력) kích thước (size / 크기) [MUST]

10 lines SCSS có thể generate 10,000 lines CSS.

Cấp cao (senior / 시니어) rà soát (review / 검토):
- compile đầu ra (output / 출력),
- bundle report,
- coverage.

SCSS lớp trừu tượng (abstraction / 추상화) chi phí (cost / 비용) phải đo ở **CSS đầu ra (output / 출력)**.

---

# 136. khối trộn tái sử dụng (mixin) Duplication chi phí (cost / 비용) [ADV]

khối trộn tái sử dụng (mixin):

```scss
@mixin card-base {
  padding: 1rem;
  border: 1px solid;
}
```

Included 100 times:
→ các khai báo (declarations) emitted 100 times.

Dùng chung (shared / 공유) lớp (class / 클래스):
```css
.card-base {}
```
→ one ruleset, but markup composes lớp (class / 클래스).

Tradeoff:
- CSS kích thước (size / 크기),
- ngữ nghĩa (semantics / 의미론),
- thời gian chạy (runtime / 런타임) lớp (class / 클래스) composition,
- đóng gói (encapsulation).

---

# 137. Extend vs khối trộn tái sử dụng (mixin) vs tiện ích (utility) [MUST]

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **@extend** tiếp nhận điểm tựa từ **Token layers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **@mixin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `@extend`

bộ chọn (selector) relationship.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **@mixin** tiếp nhận điểm tựa từ **@extend** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tiện ích (utility) lớp (class / 클래스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `@mixin`

khai báo (declaration)/quy tắc (rule / 규칙) duplication at compile thời gian (time / 시간).

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **tiện ích (utility) lớp (class / 클래스)** tiếp nhận điểm tựa từ **@mixin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 1–3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tiện ích (utility) lớp (class / 클래스)

Dùng chung (shared / 공유) thời gian chạy (runtime / 런타임) lớp (class / 클래스).

Quyết định (decision / 결정):

```text
Same semantic selector identity? → extend maybe
Need generated declarations?     → mixin
Reusable runtime behavior?       → utility/class
```

---

# 138. SCSS rà soát mã (code review / 코드 리뷰) Checklist [cấp cao (senior / 시니어)]

Check:

```text
Does Sass add real value?
Could native CSS do this more clearly?
Are module namespaces clear?
Any deprecated APIs?
Any global mutable state?
Nested > 3 levels?
Map too complex?
Generated CSS too large?
Mixin duplicated heavily?
@extend output predictable?
Public configuration documented?
Runtime concerns wrongly solved compile-time?
```

---

# 139. lồng cú pháp (nesting) độ sâu (depth / 깊이) ngân sách (budget / 예산) [cấp cao (senior / 시니어)]

Suggested:

```text
0–2 levels: normal
3: review
4+: strong smell
```

Not hard quy tắc (rule / 규칙).

các trạng thái (states)/at-rules don't count the same as DOM descendant lồng cú pháp (nesting) conceptually.

---

# 140. giao diện công khai (public API) Stability [ARCH]

If building Sass thư viện (library / 라이브러리):

Changing:
- công khai (public / 공개) biến (variable),
- khối trộn tái sử dụng (mixin) name,
- hàm (function / 함수) name,
- từ khóa (keyword / 키워드) argument name,
- forwarded prefix,
- default cấu hình (configuration / 구성),

can be breaking thay đổi (change / 변경).

Treat Sass mô-đun (module / 모듈) like mã (code / 코드) thư viện (library / 라이브러리).

---

# 141. mang tính ngữ nghĩa (semantic / 의미적) Versioning [ARCH]

Thư viện (library / 라이브러리) releases:

```text
PATCH
bugfix output without API break

MINOR
new backward-compatible mixin/function/token

MAJOR
rename/remove/change public config/output contract
```

CSS visual changes may also be breaking even if Sass API same.

---

# 142. Naming công khai (public / 공개) các khối trộn tái sử dụng (mixins) [ARCH]

Bad:
```scss
@mixin blue-shadow-12 {}
```

Better:
```scss
@mixin elevated-surface {}
```

Expose ngữ nghĩa (semantics / 의미론), not hiện tại (current / 현재) hiện thực (implementation / 구현) details.

---

# 143. Avoid Boolean Explosion [ADV]

Bad:

```scss
@mixin button(
  $small: false,
  $rounded: false,
  $danger: false,
  $loading: false,
  $outline: false
) {}
```

Combinations explode.

Better:
- separate biến thể (variant)/trạng thái (state / 상태) tokens,
- các map khóa–giá trị (maps),
- CSS các bộ chọn (selectors)/dữ liệu (data / 데이터) attributes,
- smaller các khối trộn tái sử dụng (mixins).

---

# 144. Sass Isn't a thành phần (component / 컴포넌트) máy trạng thái (state machine / 상태 머신) [MUST]

Thời gian chạy (runtime / 런타임) các trạng thái (states):
```text
open
loading
selected
disabled
error
```

belong in HTML/JS attributes/classes.

Sass can generate style APIs but cannot know thời gian chạy (runtime / 런타임) trạng thái (state / 상태).

---

# 145. Prefer bản địa (native / 네이티브) CSS Features [cấp cao (senior / 시니어)]

Historically Sass solved:
- các biến (variables),
- lồng cú pháp (nesting),
- color transforms,
- calculations.

Hiện đại (modern / 현대적) CSS now has:
- custom các thuộc tính (properties),
- bản địa (native / 네이티브) lồng cú pháp (nesting),
- `color-mix`,
- `calc`,
- `min/max/clamp`,
- các truy vấn vùng chứa (container queries).

Use Sass only where thời điểm biên dịch (compile-time) lớp trừu tượng (abstraction / 추상화) adds giá trị (value / 값).

---

# 146. When Sass Is Still Strong [cấp cao (senior / 시니어)]

Excellent use cases:

```text
module organization
library public APIs
token data processing
bounded utility generation
compile-time validation
maps/lists
mixins with content blocks
functions
third-party Sass configuration
build-time adapters
```

---

# 147. When Sass Is Overkill [cấp cao (senior / 시니어)]

If dự án (project / 프로젝트) only needs:

```text
nesting
variables
simple imports
```

Hiện đại (modern / 현대적) bản địa (native / 네이티브) CSS + bundler may be enough.

Do not choose Sass only from habit.

---

# 148. Beginner Practice

Bản dựng (build / 빌드):
1. các biến (variables),
2. nested các bộ chọn (selectors),
3. các khối trộn tái sử dụng (mixins),
4. simple hàm (function / 함수),
5. map khóa–giá trị (map),
6. `@each`,
7. `@use`.

Dự án (project / 프로젝트):
- button các biến thể (variants) from map khóa–giá trị (map),
- spacing các tiện ích (utilities),
- compile to CSS.

---

# 149. Intermediate Practice

Bản dựng (build / 빌드):
1. đơn vị từ (token / 토큰) mô-đun (module / 모듈),
2. điểm ngắt (breakpoint) khối trộn tái sử dụng (mixin),
3. thành phần (component / 컴포넌트) facade,
4. biến chủ đề (theme variable) generator,
5. CSS Modules + SCSS,
6. chuyển đổi (migration) from `@import`.

---

# 150. cấp cao (senior / 시니어) Practice

Bản dựng (build / 빌드):
1. Sass thư viện (library / 라이브러리) giao diện công khai (public API),
2. configurable mô-đun (module / 모듈),
3. `@forward show/hide/prefix`,
4. vendor adapter,
5. đơn vị từ (token / 토큰) kiểm tra hợp lệ (validation / 검증),
6. tiện ích (utility) generator with đầu ra (output / 출력) ngân sách (budget / 예산),
7. các bản đồ mã nguồn (source maps)/quy trình bản dựng (build / 빌드) (build pipeline),
8. deprecation-clean CI.

---

# 151. 30-Day SCSS Roadmap

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 1–3** tiếp nhận điểm tựa từ **tiện ích (utility) lớp (class / 클래스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 4–6** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 1–3
Phần này nối kiến thức vừa học với “Days 1–3”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- syntax,
- các biến (variables),
- dữ liệu (data / 데이터) types,
- lồng cú pháp (nesting).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 4–6** tiếp nhận điểm tựa từ **Days 1–3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 7–9** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 4–6
Phần này nối kiến thức vừa học với “Days 4–6”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- các danh sách (lists),
- các map khóa–giá trị (maps),
- built-in modules.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 7–9** tiếp nhận điểm tựa từ **Days 4–6** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 10–12** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 7–9
Phần này nối kiến thức vừa học với “Days 7–9”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- các khối trộn tái sử dụng (mixins),
- arguments,
- `@content`.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 10–12** tiếp nhận điểm tựa từ **Days 7–9** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 13–15** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 10–12
Phần này nối kiến thức vừa học với “Days 10–12”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- các hàm (functions),
- luồng điều khiển (control flow),
- kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 13–15** tiếp nhận điểm tựa từ **Days 10–12** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 16–18** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 13–15
Phần này nối kiến thức vừa học với “Days 13–15”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- `@use`,
- không gian tên (namespace / 네임스페이스),
- cấu hình (configuration / 구성).

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 16–18** tiếp nhận điểm tựa từ **Days 13–15** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 19–21** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 16–18
Phần này nối kiến thức vừa học với “Days 16–18”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- `@forward`,
- facade,
- công khai (public / 공개)/private API.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 19–21** tiếp nhận điểm tựa từ **Days 16–18** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 22–23** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 19–21
Phần này nối kiến thức vừa học với “Days 19–21”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- token system,
- generators.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 22–23** tiếp nhận điểm tựa từ **Days 19–21** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 24–25** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 22–23
Phần này nối kiến thức vừa học với “Days 22–23”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- CSS các biến (variables) integration,
- thời gian chạy (runtime)/thời điểm biên dịch (compile-time) boundary.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 24–25** tiếp nhận điểm tựa từ **Days 22–23** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Days 26–27** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 24–25
Phần này nối kiến thức vừa học với “Days 24–25”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- kiến trúc (architecture),
- component ownership.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Days 26–27** tiếp nhận điểm tựa từ **Days 24–25** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Day 28** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Days 26–27
Phần này nối kiến thức vừa học với “Days 26–27”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- legacy chuyển đổi (migration),
- deprecations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Day 28** tiếp nhận điểm tựa từ **Days 26–27** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Day 29** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Day 28
Phần này nối kiến thức vừa học với “Day 28”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- output/hiệu năng (performance) inspection.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Day 29** tiếp nhận điểm tựa từ **Day 28** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Day 30** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Day 29
Phần này nối kiến thức vừa học với “Day 29”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- library API review.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Day 30** tiếp nhận điểm tựa từ **Day 29** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **giao diện công khai (public API) và cấu hình (configuration / 구성) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Day 30
Phần này nối kiến thức vừa học với “Day 30”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

- final design-system project.

---

# 152. cấp cao (senior / 시니어) Self-Test

Bạn phải trả lời được:

1. Sass biến (variable) khác CSS custom thuộc tính (property / 속성) thế nào?
2. SCSS compile ở thời điểm nào?
3. Vì sao `@import` đã ngừng khuyến nghị (deprecated)?
4. `@use` tải (load / 로드) mô-đun (module / 모듈) mấy lần?
5. `@forward` khác `@use`?
6. `!default` dùng cho gì?
7. không gian tên (namespace / 네임스페이스) giúp gì?
8. Vì sao `as *` nên hạn chế?
9. công khai (public / 공개)/private Sass member là gì?
10. khối trộn tái sử dụng (mixin) khác hàm (function / 함수)?
11. `@content` dùng khi nào?
12. từ khóa (keyword / 키워드) args ảnh hưởng API tính tương thích (compatibility / 호환성) thế nào?
13. `@extend` thực sự làm gì?
14. Placeholder bộ chọn (selector) có lợi gì?
15. `math.div()` vì sao thay `/`?
16. `sass:map` khác old `map-get`?
17. hiện đại (modern / 현대적) color API vì sao cần tường minh (explicit / 명시적) không gian (space / 공간)?
18. map khóa–giá trị (map) phù hợp cho loại dữ liệu (data / 데이터) nào?
19. Khi nào vòng lặp (loop / 루프) generation là phản mẫu (anti-pattern)?
20. nguồn (source / 소스) SCSS nhỏ có đảm bảo CSS nhỏ?
21. khối trộn tái sử dụng (mixin) có duplication chi phí (cost / 비용) gì?
22. tiện ích (utility) lớp (class / 클래스) khác khối trộn tái sử dụng (mixin) ra sao?
23. Sass cấu hình (config / 설정) và thời gian chạy (runtime / 런타임) theme khác nhau?
24. `@forward show/hide` giải quyết gì?
25. Forward prefix dùng khi nào?
26. Sass không thay Autoprefixer vì sao?
27. CSS Modules và SCSS có xung đột (conflict / 충돌) không?
28. bản địa (native / 네이티브) CSS lồng cú pháp (nesting) có làm Sass vô dụng không?
29. Khi nào nên chọn plain CSS thay Sass?
30. Sass thư viện (library / 라이브러리) giao diện công khai (public API) nên phiên bản (version / 버전) thế nào?

---

# 153. Cheat Sheet
Phần này nối kiến thức vừa học với “153. Cheat Sheet”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```scss
@use "sass:math";
@use "sass:map";
@use "sass:color";

// variable
$space-unit: .25rem;

// map
$spaces: (
  1: .25rem,
  2: .5rem,
  4: 1rem
);

// function
@function space($step) {
  @if not map.has-key($spaces, $step) {
    @error "Unknown spacing: #{$step}";
  }

  @return map.get($spaces, $step);
}

// mixin
@mixin focus-ring(
  $width: 3px,
  $offset: 3px
) {
  outline: $width solid currentColor;
  outline-offset: $offset;
}

// content mixin
@mixin up($width) {
  @media (width >= $width) {
    @content;
  }
}

// generation
@each $name, $value in $spaces {
  .gap-#{$name} {
    gap: $value;
  }
}

// CSS runtime token
:root {
  --space-card: #{space(4)};
}

.card {
  gap: var(--space-card);

  &:focus-visible {
    @include focus-ring;
  }

  @include up(48rem) {
    display: grid;
  }
}
```

---

# 154. Recommended Production kiến trúc (architecture)
Phần này nối kiến thức vừa học với “154. Recommended Production kiến trúc (architecture)”, giúp người mới hiểu mục đích, cách dùng và giới hạn trước khi xem ví dụ bên dưới.

```text
SCSS
│
├─ settings
│  ├─ primitive design data
│  └─ library config
│
├─ tools
│  ├─ functions
│  └─ mixins
│
├─ CSS runtime tokens
│
├─ base
│
├─ layout primitives
│
├─ components
│
├─ utilities
│
└─ entrypoint
```

Rules:

```text
@use namespaces
@forward facades
no Sass @import
no global built-in API
no slash division
low nesting
bounded generators
runtime state stays in CSS/HTML/JS
```

---

# 155. References

Official Sass:
- https://sass-lang.com/documentation/
- https://sass-lang.com/documentation/at-rules/use/
- https://sass-lang.com/documentation/at-rules/forward/
- https://sass-lang.com/documentation/at-rules/mixin/
- https://sass-lang.com/documentation/at-rules/hàm (function / 함수)/
- https://sass-lang.com/documentation/modules/
- https://sass-lang.com/documentation/breaking-changes/
- https://sass-lang.com/documentation/breaking-changes/import/
- https://sass-lang.com/documentation/breaking-changes/slash-div/
- https://sass-lang.com/documentation/breaking-changes/color-functions/

---

---

# 156. SCSS kiến trúc (architecture / 아키텍처) — thiết kế đồ thị mô-đun (module graph) trước khi thiết kế folder [cấp cao (senior / 시니어)/ARCH]

Một codebase SCSS lớn không nên bắt đầu từ câu hỏi “dùng 7-1 hay chia folder thế nào?”, mà từ câu hỏi **mô-đun (module / 모듈) nào sở hữu API nào và mô-đun (module / 모듈) nào được phép emit CSS**. Folder chỉ là biểu diễn (representation / 표현) của phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프). Nếu mọi tệp (file / 파일) có thể truy cập toàn cục (global / 전역) các biến (variables)/các khối trộn tái sử dụng (mixins) và emit rules khi import, cấu trúc (structure / 구조) nhìn đẹp nhưng kiến trúc (architecture / 아키텍처) vẫn toàn cục (global / 전역).

Hiện đại (modern / 현대적) Sass với `@use` và `@forward` cho phép bạn thiết kế đồ thị (graph / 그래프) rõ hơn. Một công cụ (tool / 도구) mô-đun (module / 모듈) chứa các biến (variables)/các hàm (functions)/các khối trộn tái sử dụng (mixins) nên lý tưởng không emit CSS. Một style mô-đun (module / 모듈) cố ý emit cơ sở (base / 기반)/thành phần (component / 컴포넌트) rules. Một facade mô-đun (module / 모듈) dùng `@forward` để expose bề mặt công khai (public surface) ổn định. Entry điểm (point / 지점) `@use`s các facade/style modules theo phụ thuộc (dependency / 의존성) thứ tự (order / 순서) mà ứng dụng (application / 애플리케이션) cần.

```text
_tokens.scss      → values / configuration
_math.scss        → functions, no CSS output
_button-tools.scss→ mixins, no CSS output
_button.scss      → emits component CSS
_index.scss       → @forward public API
app.scss          → entry point, @use style/facade modules
```

Điểm quan trọng là “tệp (file / 파일) thành phần (partial)” không tự làm mã (code / 코드) modular. `_tokens.scss` vẫn có thể là toàn cục (global / 전역) soup nếu được kéo bằng legacy `@import`. ranh giới mô-đun (module boundary / 모듈 경계) đến từ không gian tên (namespace / 네임스페이스), private members, single evaluation và giao diện công khai (public API) discipline của `@use`/`@forward`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Day 30** đã nêu tiêu chí phân biệt, còn **giao diện công khai (public API) và cấu hình (configuration / 구성) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Side-effect CSS phải có quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## giao diện công khai (public API) và cấu hình (configuration / 구성) ranh giới (boundary / 경계)

Thư viện (library / 라이브러리) Sass nên expose ít thứ hơn nội bộ (internal / 내부) hiện thực (implementation / 구현). Nếu bên tiêu thụ (consumer / 소비자) cần configure brand color, spacing quy mô (scale / 규모) hoặc cờ tính năng (feature flag / 기능 플래그) thời điểm biên dịch (compile-time), expose `$variable: default !default` có chủ đích và configure qua `@use ... with (...)`. Đừng expose mọi nội bộ (internal / 내부) map khóa–giá trị (map) chỉ vì “sau này có thể cần”; khi bên tiêu thụ (consumer / 소비자) phụ thuộc vào shape của nested map khóa–giá trị (map), refactor nội bộ biến thành breaking thay đổi (change / 변경).

`@forward ... show/hide` hoặc prefixing giúp facade chỉ xuất phần ổn định. Private members nên thực sự private. công khai (public / 공개) khối trộn tái sử dụng (mixin)/hàm (function / 함수) name, parameter ngữ nghĩa (semantics / 의미론) và generated CSS đặc tả hợp đồng (contract / 계약) đều là API cần versioning.

> **Chuyển mạch:** Trong **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **giao diện công khai (public API) và cấu hình (configuration / 구성) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **Side-effect CSS phải có quyền sở hữu (ownership / 소유권)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **@extend không phải kế thừa (inheritance) kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Side-effect CSS phải có quyền sở hữu (ownership / 소유권)

Một dùng chung (common / 공통) bug là `@use` một helper mô-đun (module / 모듈) chỉ để gọi hàm (function / 함수) nhưng mô-đun (module / 모듈) đó cũng emit reset/components. Vì mô-đun (module / 모듈) tải (load / 로드) một lần, duplication được giảm so với `@import`, nhưng tác dụng phụ (side effect) vẫn tồn tại. Tách công cụ (tool / 도구) modules khỏi style modules làm phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) predictable hơn và giúp thư viện (library / 라이브러리) bên tiêu thụ (consumer / 소비자) dùng lô-gic (logic / 논리) mà không kéo CSS ngoài ý muốn.

> **Chuyển mạch:** Ở chặng này của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **@extend không phải kế thừa (inheritance) kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Side-effect CSS phải có quyền sở hữu (ownership / 소유권)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sass vs bản địa (native / 네이티브) CSS responsibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `@extend` không phải kế thừa (inheritance) kiến trúc (architecture / 아키텍처)

`@extend` hợp nhất các bộ chọn (selectors) trong trình biên dịch (compiler / 컴파일러). Nó không bản sao (copy / 복사) các khai báo (declarations) như khối trộn tái sử dụng (mixin) và không tạo kiểu (type / 타입) hierarchy như Java. Vì hợp nhất bộ chọn (selector unification) có thể tạo đầu ra (output / 출력) ở nơi xa lời gọi (call / 호출) site và coupling giữa modules, hãy giới hạn `@extend` cho placeholder contracts rất controlled. Nếu bạn cần parameterization, khối trộn tái sử dụng (mixin) thường rõ hơn; nếu chỉ cần dùng chung (shared / 공유) visual primitives, composition/tiện ích (utility) lớp (class / 클래스) hoặc bản địa (native / 네이티브) CSS tầng (layer / 계층)/đơn vị từ (token / 토큰) thường dễ dự đoán hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS — Beginner → cấp cao (senior / 시니어) Handbook (Modern Dart Sass, 2026)**, **Sass vs bản địa (native / 네이티브) CSS responsibility** tiếp nhận điểm tựa từ **@extend không phải kế thừa (inheritance) kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Sass vs bản địa (native / 네이티브) CSS responsibility

Sass mạnh ở thời điểm biên dịch (compile-time) generation: transform dữ liệu (data / 데이터) structures, validate cấu hình (config / 설정), tạo repetitive API và gói (package / 패키지) reusable authoring tools. bản địa (native / 네이티브) CSS mạnh ở thời gian chạy (runtime / 런타임): custom các thuộc tính (properties), các lớp phân tầng (cascade layers), lồng cú pháp (nesting), các truy vấn vùng chứa (container queries), `:has()`, thuộc tính lô-gic (logic / 논리) (logical properties) và theming theo môi trường (environment / 환경)/trạng thái (state / 상태). Một kiến trúc (architecture / 아키텍처) hiện đại nên để thời gian chạy (runtime / 런타임) concerns ở CSS nếu trình duyệt (browser / 브라우저) đã giải được trực tiếp, thay vì generate hàng trăm các biến thể (variants) thời điểm biên dịch (compile-time) bằng loops.

SCSS tốt không làm CSS biến mất khỏi mô hình tư duy (mental model / 사고 모델). Nó làm nguồn (source / 소스) dễ maintain hơn trong khi generated CSS vẫn nhỏ, độ đặc hiệu (specificity) thấp và dễ inspect.

---

# Kết luận

SCSS cấp cao (senior / 시니어) không phải người viết lồng cú pháp (nesting)/khối trộn tái sử dụng (mixin) nhiều nhất.

SCSS cấp cao (senior / 시니어) biết:

```text
what should happen at compile time
vs
what should remain runtime CSS
```

và dùng Sass để:

```text
organize
validate
generate
encapsulate
configure
```

mà không làm compiled CSS:
- khó đọc,
- quá lớn,
- coupling,
- đã ngừng khuyến nghị (deprecated),
- khó migrate.

Mô hình tư duy (mental model / 사고 모델) cuối:

```text
CSS knowledge first
→ Sass as authoring language
→ module API
→ controlled generation
→ inspect compiled output
```

> **Bàn giao:** Sau **Sass vs bản địa (native / 네이티브) CSS responsibility**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
