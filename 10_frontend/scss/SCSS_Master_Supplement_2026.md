# SCSS Master Supplement — Dart Sass Deep Dive (2026)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**. Route đi từ thuật ngữ và quy tắc Sass → module, function, mixin và flow control → compilation, CSS output và debugging → modern Dart Sass migration → patterns nâng cao, để supplement mở rộng handbook bằng cơ chế thật.

> Đọc sau:
>
> ```văn bản (text / 텍스트)
> SCSS_Beginner_to_Senior_2026.md
> ```
>
> tệp (file / 파일) này không lặp cú pháp (syntax / 문법) cơ bản. Nó bổ sung các phần cần để đi từ **cấp cao (senior / 시니어) SCSS → Sass thư viện (library / 라이브러리)/tooling specialist**:
>
> ```văn bản (text / 텍스트)
> mô-đun (module / 모듈) định danh (identity / 식별자)
> chuẩn gốc (canonical / 정본) URLs
> cấu hình (configuration / 구성) lifecycle
> advanced meta programming
> bộ chọn (selector) algebra
> deep các danh sách (lists)/các map khóa–giá trị (maps)
> recursion
> Sass giá trị (value / 값) mô hình (model / 모델)
> calculations
> CSS tính tương thích (compatibility / 호환성)
> deprecations
> migrator
> JS API
> custom importers/các hàm (functions)
> embedded protocol awareness
> gói (package / 패키지)/thư viện (library / 라이브러리) thiết kế (design / 설계)
> testing
> hiệu năng (performance / 성능)
> bản phát hành (release / 릴리스) engineering
> ```

---

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ Sass/SCSS được viết theo hướng tiếng Việt dễ hiểu nhưng vẫn giữ từ gốc để tra cứu. Ví dụ: **thời điểm biên dịch (compile-time)**, **thời gian chạy (runtime / 런타임)**, **phạm vi (scope / 범위)**, **không gian tên (namespace / 네임스페이스)**, **đồ thị mô-đun (module graph)**, **nội suy (interpolation)**, **che khuất biến (shadowing)**, **luồng điều khiển (control flow)** và **hợp nhất bộ chọn (selector unification)**. Những tên directive, hàm (function / 함수), mô-đun (module / 모듈) và cú pháp Sass nằm trong mã vẫn được giữ nguyên.

# 0. Mastery ranh giới (boundary / 경계)

# 0A. hiện đại (modern / 현대적) Sass status — kiểm tra (audit / 감사) 2026-09

Chuẩn gốc (canonical / 정본) notes này lấy **Dart Sass 1.104.1** làm hiện thực (implementation / 구현)/tham chiếu (reference / 참조) hiện tại. LibSass và Ruby Sass không còn là mục tiêu (target / 대상) cho mã (code / 코드) mới. hiện đại (modern / 현대적) Sass đang chủ động tiến gần CSS nền tảng (platform / 플랫폼): Sass `@import` và toàn cục (global / 전역) built-in các hàm (functions) đã đã ngừng khuyến nghị (deprecated) từ 1.80.0; mã (code / 코드) mới dùng `@use`, `@forward` và built-in modules như `sass:math`, `sass:map`, `sass:color`. Legacy `if()` cũng đang trên lộ trình trạng thái ngừng khuyến nghị (deprecation) để tránh xung đột với CSS `if()` mới.

đồ thị mô-đun (module graph) là phần kiến trúc (architecture / 아키텍처) cốt lõi. Mỗi `@use` tải (load / 로드) mô-đun (module / 모듈) một lần theo chuẩn gốc (canonical / 정본) URL, members được namespaced và private members không rò ra ngoài. `@forward` cho phép gói (package / 패키지) tách hiện thực (implementation / 구현) thành nhiều tệp (file / 파일) thành phần (partial)/mô-đun (module / 모듈) nhưng xuất một facade ổn định. Khi kiểm tra (audit / 감사) thư viện (library / 라이브러리), hãy phân biệt công cụ (tool / 도구) mô-đun (module / 모듈) không emit CSS, style mô-đun (module / 모듈) có tác dụng phụ (side effect) CSS và entry/facade mô-đun (module / 모듈) quyết định bề mặt công khai (public surface)/phụ thuộc (dependency / 의존성) thứ tự (order / 순서).

Mọi lớp trừu tượng (abstraction / 추상화) Sass cuối cùng phải được đánh giá bằng generated CSS. thời điểm biên dịch (compile-time) cleverness không được phép tạo bộ chọn (selector) explosion, duplicate các khai báo (declarations), độ đặc hiệu (specificity) escalation hoặc bundle vượt ngân sách (budget / 예산). Sass mastery là biết khi nào thời điểm biên dịch (compile-time) lớp trừu tượng (abstraction / 추상화) có giá trị và khi nào bản địa (native / 네이티브) CSS/custom các thuộc tính (properties)/các truy vấn vùng chứa (container queries)/các lớp phân tầng (cascade layers) đã là công cụ phù hợp hơn.

Để “master SCSS” cần phân biệt 3 tầng (layer / 계층):

```text
Sass Language
→ Sass Compiler / Module Loader
→ Generated CSS / Browser
```

Và khi tích hợp bản dựng (build / 빌드):

```text
SCSS
→ Dart Sass
→ PostCSS / transforms
→ minification
→ bundler
→ browser
```

Nhiều bug được gán “SCSS” thực ra nằm ở:
- tải (load / 로드) resolution,
- CSS cơ chế phân tầng (cascade),
- bundler,
- đã ngừng khuyến nghị (deprecated) phụ thuộc (dependency / 의존성),
- bản đồ mã nguồn (source map / 소스 맵),
- post-processing.

---

# 1. Dart Sass as ngôn ngữ (language / 언어) tham chiếu (reference / 참조)

Hiện đại (modern / 현대적) Sass development thực tế xoay quanh Dart Sass.

Các hiện thực (implementation / 구현) cũ:
```text
Ruby Sass
LibSass / node-sass
```

không hỗ trợ đầy đủ hệ mô-đun (module system) hiện đại.

> **Chuyển mạch:** Thuật ngữ thống nhất giúp đọc Sass rule chính xác; mental model tiếp theo nối source syntax, compiler evaluation và CSS output.

## Master quy tắc (rule / 규칙)

Nếu một gói (package / 패키지) vẫn yêu cầu node-sass/LibSass tính tương thích (compatibility / 호환성):
- treat as legacy ràng buộc (constraint / 제약조건),
- don't let it define new kiến trúc (architecture / 아키텍처).

---

# 2. CSS tính tương thích (compatibility / 호환성) Is a cốt lõi (core / 핵심) Sass thiết kế (design / 설계) ràng buộc (constraint / 제약조건)

Sass cố gắng là CSS-compatible superset.

Khi CSS thêm cú pháp (syntax / 문법) mới:
- slash separators,
- bản địa (native / 네이티브) lồng cú pháp (nesting),
- Color 4,
- CSS hàm (function / 함수) names,

Sass đôi khi phải deprecate old ngôn ngữ (language / 언어) hành vi (behavior / 동작).

Đây là nguồn của nhiều breaking changes.

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Master quy tắc (rule / 규칙)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Thư viện (library / 라이브러리)/tooling concern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
CSS evolves
→ syntax conflict appears
→ Sass warns/deprecates
→ Sass changes semantics
```

---

# 3. mô-đun (module / 모듈) định danh (identity / 식별자) [DEEP]

`@use` không đơn thuần paste tệp (file / 파일).

Trình biên dịch (compiler / 컴파일러) resolves URL tới **chuẩn gốc (canonical / 정본) mô-đun (module / 모듈) định danh (identity / 식별자)**.

Một mô-đun (module / 모듈) canonicalized giống nhau:
- tải (load / 로드) once,
- execute once,
- CSS emit once.

Điều này làm hệ mô-đun (module system) predictable hơn `@import`.

---

# 4. chuẩn gốc (canonical / 정본) URLs [DEEP]

Importer resolves người dùng (user / 사용자) URL:

```text
"tokens"
```

thành chuẩn gốc (canonical / 정본) URL đại diện mô-đun (module / 모듈) duy nhất.

Nếu cùng vật lý (physical / 물리적) mô-đun (module / 모듈) được canonicalize thành 2 URLs khác nhau:
- duplicate mô-đun (module / 모듈) tải (load / 로드) có thể xảy ra,
- CSS/cấu hình (config / 설정)/trạng thái (state / 상태) có thể khác expectation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Thư viện (library / 라이브러리)/tooling concern** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Mẫu thiết kế (design pattern / 디자인 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thư viện (library / 라이브러리)/tooling concern

Custom importers phải implement canonicalization đúng.

---

# 5. mô-đun (module / 모듈) mô hình thực thi (execution model / 실행 모델) [DEEP]

Một Sass mô-đun (module / 모듈):
1. dependencies tải (load / 로드),
2. top-level statements execute,
3. members defined,
4. CSS generated,
5. mô-đun (module / 모듈) cached.

Import đồ thị (graph / 그래프) gần giống programming-language modules hơn văn bản (text / 텍스트) includes.

---

# 6. cấu hình (configuration / 구성) Timing [MUST]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
@use "theme" with (
  $brand: red
);
```

Cấu hình (configuration / 구성) áp khi mô-đun (module / 모듈) **first loaded**.

Nếu mô-đun (module / 모듈) đã tải (load / 로드) earlier:

```scss
@use "theme";
@use "theme" with (...);
```

Cấu hình (configuration / 구성) xung đột (conflict / 충돌)/lỗi (error / 오류).

> **Chuyển mạch:** Trong **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Mẫu thiết kế (design pattern / 디자인 패턴)** tiếp nhận điểm tựa từ **Thư viện (library / 라이브러리)/tooling concern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu thiết kế (design pattern / 디자인 패턴)

Centralize cấu hình (configuration / 구성) in one điểm vào (entrypoint / 진입점).

---

# 7. cấu hình (configuration / 구성) quyền sở hữu (ownership / 소유권) [ARCH]

Bad:

```text
component A configures theme
component B also configures theme
```

Good:

```text
application entrypoint
→ configures design system once
→ components @use configured module
```

---

# 8. Forward-before-use mẫu (pattern / 패턴) [ARCH]

Facade:

```scss
@forward "core" with (...);
@use "core";
```

Reason:
- downstream cấu hình (config / 설정) can reach forward first,
- hiện tại (current / 현재) mô-đun (module / 모듈) can then use same configured instance.

---

# 9. Private cấu hình (configuration / 구성) trạng thái ngừng khuyến nghị (deprecation) [2026]

Hiện đại (modern / 현대적) Dart Sass deprecates configuring private các biến (variables) via `with`.

Private members are hiện thực (implementation / 구현) details.

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Mẫu thiết kế (design pattern / 디자인 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Công cụ (tool / 도구) mô-đun (module / 모듈)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy tắc (rule / 규칙)

If consumers need to configure giá trị (value / 값):
- make it công khai (public / 공개) intentionally,
- document it.

Do not use private naming and still expose cấu hình (config / 설정).

---

# 10. giao diện công khai (public API) Surface kiểm tra (audit / 감사) [ARCH]

For each mô-đun (module / 모듈) danh sách (list / 목록):

```text
public variables
public mixins
public functions
forwarded members
configuration variables
CSS side effects
```

Treat emitted CSS itself as part of công khai (public / 공개) hành vi (behavior / 동작).

---

# 11. CSS Side-effect Modules vs công cụ (tool / 도구) Modules [ARCH]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Công cụ (tool / 도구) mô-đun (module / 모듈)** tiếp nhận điểm tựa từ **Quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CSS side-effect mô-đun (module / 모듈)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Công cụ (tool / 도구) mô-đun (module / 모듈)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
functions
mixins
variables
no CSS emitted on load
```

> **Chuyển mạch:** Trong **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **CSS side-effect mô-đun (module / 모듈)** tiếp nhận điểm tựa từ **Công cụ (tool / 도구) mô-đun (module / 모듈)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Warning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSS side-effect mô-đun (module / 모듈)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```scss
.button { ... }
```

emits CSS when used.

Separate them where practical.

Mẫu (pattern / 패턴):

```text
tools/
components/
```

Prevents accidental CSS emission from tiện ích (utility) imports.

---

# 12. Side-effect-free đơn vị từ (token / 토큰) mô-đun (module / 모듈) [ARCH]

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```scss
// _tokens.scss
$spacing: (...);
$colors: (...);

@function ... {}
```

No bộ chọn (selector) đầu ra (output / 출력).

Any bên tiêu thụ (consumer / 소비자) can `@use` safely.

---

# 13. CSS Emission Entry điểm (point / 지점) [ARCH]

Thư viện (library / 라이브러리) may expose:

```text
library
library/css
library/tools
```

Concept:
- tools for Sass consumers,
- CSS điểm vào (entrypoint / 진입점) for full styles.

Avoid surprising bên tiêu thụ (consumer / 소비자):
> I used one hàm (function / 함수) and 200KB CSS appeared.

---

# 14. `meta.load-css()` Deep Use [ADV]

`meta.load-css()` loads CSS from mô-đun (module / 모듈) in động (dynamic / 동적) ngữ cảnh (context / 맥락).

Unlike `@use`:
- useful inside các khối trộn tái sử dụng (mixins),
- designed for CSS loading, not member truy cập (access / 접근).

Mẫu (pattern / 패턴):
```text
Configuration/condition
→ meta.load-css()
→ conditional CSS emission
```

Use sparingly.

---

# 15. `meta.module-variables()` [ADV]

Reflection over loaded mô-đun (module / 모듈) công khai (public / 공개) members.

Concept:

```scss
@use "sass:meta";
@use "tokens";

$vars:
  meta.module-variables("tokens");
```

Returns map khóa–giá trị (map) of các biến (variables).

Use cases:
- đơn vị từ (token / 토큰) export tooling,
- documentation generation,
- kiểm tra hợp lệ (validation / 검증).

---

# 16. `meta.module-functions()` [ADV]

Get các hàm (functions) exposed by mô-đun (module / 모듈).

Can bản dựng (build / 빌드) generic plugin/dispatch các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Warning** tiếp nhận điểm tựa từ **CSS side-effect mô-đun (module / 모듈)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Warning

Reflection increases lớp trừu tượng (abstraction / 추상화) chi phí (cost / 비용).

Normal apps usually do not need.

---

# 17. `meta.module-mixins()` [ADV]

Hiện đại (modern / 현대적) Dart Sass can expose khối trộn tái sử dụng (mixin) references from mô-đun (module / 모듈).

Use:
- framework-level composition,
- introspection tooling.

Don't dynamically lời gọi (call / 호출) everything just because possible.

---

# 18. First-class các hàm (functions) [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```scss
$fn:
  meta.get-function("scale");
```

Then:

```scss
$result:
  meta.call($fn, ...);
```

Mẫu (pattern / 패턴):
- chiến lược (strategy / 전략) hàm (function / 함수),
- ánh xạ (mapping / 매핑) chuỗi xử lý (pipeline / 파이프라인).

---

# 19. First-class các khối trộn tái sử dụng (mixins) [ADV]

Hiện đại (modern / 현대적) Sass supports khối trộn tái sử dụng (mixin) references via meta APIs.

Concept:
```text
retrieve mixin
→ meta.apply
```

Useful advanced thư viện (library / 라이브러리) technique.

---

# 20. chiến lược (strategy / 전략) mẫu (pattern / 패턴) in Sass [ARCH]

Different transform các hàm (functions):

```text
linear
modular
fluid
```

Select hàm (function / 함수) tham chiếu (reference / 참조) from cấu hình (config / 설정).

Then apply generic generator.

Equivalent to chiến lược (strategy / 전략) mẫu (pattern / 패턴) at compile thời gian (time / 시간).

---

# 21. Higher-order Sass mẫu (pattern / 패턴) [ADV]

Hàm (function / 함수) receiving/using hàm (function / 함수) tham chiếu (reference / 참조):

```text
data
+ transformation function
→ transformed data
```

Useful:
- đơn vị từ (token / 토큰) processors,
- quy mô (scale / 규모) generation.

Keep API narrow.

---

# 22. Argument các danh sách (lists) as dữ liệu (data / 데이터) [DEEP]

`$args...` is special argument-list giá trị (value / 값).

It can retain:
- positional arguments,
- từ khóa (keyword / 키워드) arguments.

`meta.keywords($args)` returns từ khóa (keyword / 키워드) map khóa–giá trị (map).

This is more than ordinary danh sách (list / 목록) ngữ nghĩa (semantics / 의미론).

---

# 23. Rest Argument Placement Deprecations [2026]

Hiện đại (modern / 현대적) Sass tightened rules around misplaced rest arguments.

Quy tắc (rule / 규칙):
- arbitrary/rest arguments belong where signature/lời gọi (call / 호출) cú pháp (syntax / 문법) expects,
- don't rely on permissive historical parsing.

Treat trạng thái ngừng khuyến nghị (deprecation) warnings as errors-to-fix.

---

# 24. từ khóa (keyword / 키워드) Argument tính tương thích (compatibility / 호환성) [ARCH]

Công khai (public / 공개) hàm (function / 함수):

```scss
@function token(
  $name,
  $fallback: null
) {}
```

Consumers may lời gọi (call / 호출):

```scss
token(
  $name: brand,
  $fallback: red
)
```

Rename `$fallback`:
→ potentially breaking API.

Thư viện (library / 라이브러리) chuyển đổi (migration):
- temporarily accept old từ khóa (keyword / 키워드) where possible,
- issue warning,
- document major bản phát hành (release / 릴리스).

---

# 25. Sass danh sách (list / 목록) mô hình (model / 모델) [DEEP]

A danh sách (list / 목록) carries:
- elements,
- separator: không gian (space / 공간)/comma/slash,
- bracketed flag.

Examples:

```text
a b c
a, b, c
a / b
[a, b]
```

These are not always interchangeable.

---

# 26. Single các giá trị (values) Are List-like [DEEP]

Sass danh sách (list / 목록) các hàm (functions) may treat:

```scss
10px
```

as a one-element danh sách (list / 목록).

This can surprise kiểm tra hợp lệ (validation / 검증) lô-gic (logic / 논리).

Don't detect “is danh sách (list / 목록)” merely with naive các giả định (assumptions / 가정들).

---

# 27. các map khóa–giá trị (maps) Are List-like [DEEP]

map khóa–giá trị (map):

```scss
(a: 1, b: 2)
```

can behave as danh sách (list / 목록) of two-element pairs in danh sách (list / 목록) các hàm (functions).

Powerful but dangerous for generic mã (code / 코드).

Prefer map khóa–giá trị (map) APIs when ngữ nghĩa (semantics / 의미론) are map khóa–giá trị (map).

---

# 28. Empty danh sách (list / 목록) / Empty map khóa–giá trị (map) Ambiguity [DEEP]

Historically `()` can represent empty danh sách (list / 목록)/map khóa–giá trị (map) ngữ nghĩa (semantics / 의미론) depending ngữ cảnh (context / 맥락).

Reflection/kiểu (type / 타입) hành vi (behavior / 동작) must be understood when building generic các hàm (functions).

Avoid API relying on ambiguous emptiness.

---

# 29. Slash-separated các danh sách (lists) [DEEP]

Hiện đại (modern / 현대적) Sass treats `/` as CSS-friendly separator direction.

Create intentionally with appropriate danh sách (list / 목록) APIs where needed.

Do not use `/` arithmetic.

---

# 30. Immutability mô hình tư duy (mental model / 사고 모델) [ADV]

Sass danh sách (list / 목록)/map khóa–giá trị (map) các hàm (functions) generally return modified copies rather than mutate in place.

```scss
$new:
  map.set(
    $old,
    key,
    value
  );
```

Think functional dữ liệu (data / 데이터) transformations.

---

# 31. Deep map khóa–giá trị (map) Operations [ADV]

Hiện đại (modern / 현대적) `sass:map` supports nested operations:
- nested `get`,
- `set`,
- deep merge,
- deep remove.

Good for hierarchical đơn vị từ (token / 토큰) các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **Warning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adjust** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy tắc (rule / 규칙)

If nested độ sâu (depth / 깊이) > 3–4 and every lời gọi (call / 호출) uses long key paths:
- reconsider đơn vị từ (token / 토큰) mô hình dữ liệu (data model / 데이터 모델).

---

# 32. Deep Merge ngữ nghĩa (semantics / 의미론) [ADV]

Need define:
- does nested map khóa–giá trị (map) recursively merge?
- does scalar replace map khóa–giá trị (map)?
- what happens key collision?

Do not use deep merge blindly for themes.

Kiểm thử (test / 테스트) resulting map khóa–giá trị (map).

---

# 33. Recursive các hàm (functions) [ADV]

Sass allows recursive các hàm (functions)/các khối trộn tái sử dụng (mixins).

Use:
- flatten nested tokens,
- cây (tree / 트리) processing.

Example conceptual:

```scss
@function flatten($map, $prefix: null) {
  ...
}
```

---

# 34. Recursion Risks [ADV]

Risks:
- hard gỡ lỗi (debug / 디버그),
- trình biên dịch (compiler / 컴파일러) công việc (work / 작업),
- accidental infinite recursion,
- unclear đầu ra (output / 출력).

Prefer iterative `@each` for shallow known structures.

---

# 35. Recursive đơn vị từ (token / 토큰) Flattener mẫu (pattern / 패턴) [ARCH]

Đầu vào (input / 입력):

```scss
(
  color: (
    text: (
      default: #111
    )
  )
)
```

Đầu ra (output / 출력) conceptual:

```text
color-text-default: #111
```

Useful:
- CSS biến (variable) export,
- JSON-like đơn vị từ (token / 토큰) nguồn (source / 소스).

But if đơn vị từ (token / 토큰) thiết kế (design token) hệ thống (system / 시스템) already has bên ngoài (external / 외부) tooling, don't duplicate it in Sass.

---

# 36. Sass giá trị (value / 값) Equality [DEEP]

`==` compares Sass các giá trị (values) semantically according to Sass rules.

Units/colors can create interesting equivalences/conversions.

Do not assume string biểu diễn (representation / 표현) equality.

---

# 37. Numbers with Units as Algebra [DEEP]

Sass internally tracks numerator/denominator units.

Operations can produce compound units.

Example conceptual:

```text
px * px
px / s
```

Not all compound units valid CSS đầu ra (output / 출력).

các hàm (functions) should validate đầu ra (output / 출력) expectations.

---

# 38. `math.compatible()` [ADV]

Use before arithmetic requiring compatible units.

Example:
```scss
@if not math.compatible($a, $b) {
  @error "...";
}
```

Good robust thư viện (library / 라이브러리) thiết kế (design / 설계).

---

# 39. Unitless Zero Pitfall [DEEP]

CSS often allows unitless `0`.

But Sass đơn vị (unit / 단위) algebra:
```text
0
0px
```
can differ in hàm (function / 함수) tính tương thích (compatibility / 호환성)/kiểu (type / 타입) lô-gic (logic / 논리).

Don't strip units blindly.

---

# 40. CSS Calculations as Sass các giá trị (values) [DEEP]

Hiện đại (modern / 현대적) Sass represents calculation expressions such as:
- `calc`,
- `min`,
- `max`,
- `clamp`,
and may simplify compatible parts.

Do not assume every hàm (function / 함수) lời gọi (call / 호출) returns plain number.

Generic thư viện (library / 라이브러리) mã (code / 코드) may need `meta.type-of()` awareness.

---

# 41. Calculation Preservation [ADV]

Goal:
- simplify thời điểm biên dịch (compile-time) known math,
- preserve browser-dependent math.

Example:

```scss
$gutter: 2rem;

.container {
  width:
    calc(100% - #{$gutter});
}
```

Hiện đại (modern / 현대적) Sass often supports interpolation-free calculation cú pháp (syntax / 문법) too; prefer hiện tại (current / 현재) clean cú pháp (syntax / 문법) if trình biên dịch (compiler / 컴파일러) handles it.

---

# 42. CSS hàm (function / 함수) Name Collisions [DEEP]

CSS keeps adding các hàm (functions).

Sass historically had toàn cục (global / 전역) các hàm (functions) with same names.

This is one reason:
- mô-đun (module / 모듈) các không gian tên (namespaces),
- toàn cục (global / 전역) built-in trạng thái ngừng khuyến nghị (deprecation),
- plain CSS hàm (function / 함수) handling evolve.

Master quy tắc (rule / 규칙):
> namespaced Sass hàm (function / 함수) when you mean Sass computation.

---

# 43. Legacy `if()` hàm (function / 함수) trạng thái ngừng khuyến nghị (deprecation) [2026]

Sass has historically had legacy `if()` hàm (function / 함수) cú pháp (syntax / 문법).

Hiện đại (modern / 현대적) CSS is developing bản địa (native / 네이티브) conditional/giá trị (value / 값) các hàm (functions), creating tính tương thích (compatibility / 호환성) pressure.

Recent Sass deprecates legacy `if()` form toward newer cú pháp (syntax / 문법)/ngữ nghĩa (semantics / 의미론).

Quy tắc (rule / 규칙):
- follow hiện tại (current / 현재) Dart Sass chuyển đổi (migration) guidance,
- don't bản dựng (build / 빌드) new thư viện (library / 라이브러리) API around đã ngừng khuyến nghị (deprecated) legacy form.

---

# 44. các hàm (functions)/các khối trộn tái sử dụng (mixins) Beginning `--` [2026]

Sass đã ngừng khuyến nghị (deprecated) người dùng (user / 사용자) Sass hàm (function / 함수)/khối trộn tái sử dụng (mixin) names beginning with `--`.

Reason:
- reserve tính tương thích (compatibility / 호환성) không gian (space / 공간) for possible bản địa (native / 네이티브) CSS các hàm (functions)/các khối trộn tái sử dụng (mixins) style cú pháp (syntax / 문법).

Do not define:

```scss
@mixin --foo {}
@function --bar() {}
```

---

# 45. Adjacent Compound bộ chọn (selector) Changes [2026]

Recent/coming Sass changes tighten các bộ chọn (selectors) with adjacent compounds to match CSS parsing/bộ chọn (selector) tính tương thích (compatibility / 호환성).

If mã (code / 코드) relies on exotic generated bộ chọn (selector) concatenation:
- run deprecation-clean bản dựng (build / 빌드),
- inspect hiện tại (current / 현재) breaking changes docs.

---

# 46. bộ chọn (selector) Algebra [DEEP]

`sass:selector` treats các bộ chọn (selectors) structurally, not strings.

Operations:
- unify,
- extend,
- replace,
- nest,
- append.

This is effectively bộ chọn (selector) algebra.

---

# 47. `selector.unify()` [ADV]

Goal:
find bộ chọn (selector) matching elements that match both inputs.

Concept:

```text
.foo + .bar
```

may unify depending cấu trúc (structure / 구조).

Useful for advanced khối trộn tái sử dụng (mixin) generation.

---

# 48. `selector.is-superselector()` [ADV]

Checks if all elements matched by bộ chọn (selector) B are also matched by A.

Useful:
- khung phần mềm (framework / 프레임워크) kiểm tra hợp lệ (validation / 검증),
- bộ chọn (selector) relationship lập luận (reasoning / 추론).

---

# 49. Avoid String-built các bộ chọn (selectors) [MASTER]

Bad advanced mã (code / 코드):
```scss
$selector:
  ".foo" + " > " + ".bar";
```

Better:
- nội suy (interpolation) for simple known trường hợp (case / 사례),
- `sass:selector` for structural manipulation.

Strings lose bộ chọn (selector) ngữ nghĩa (semantics / 의미론).

---

# 50. `@extend` thuật toán (algorithm / 알고리즘) Awareness [DEEP]

Extend performs bộ chọn (selector) transformation across biểu định kiểu (stylesheet / 스타일시트)/mô-đun (module / 모듈) extension phạm vi (scope / 범위).

It may:
- unify compound các bộ chọn (selectors),
- generate permutations,
- trim redundant các bộ chọn (selectors).

This độ phức tạp (complexity / 복잡도) explains đầu ra (output / 출력) surprises.

---

# 51. Extend phạm vi (scope / 범위) under hệ mô-đun (module system) [ADV]

hệ mô-đun (module system) makes extension hành vi (behavior / 동작) more controlled than toàn cục (global / 전역) legacy imports.

Still:
- extension crosses certain mô-đun (module / 모듈) relationships,
- understand phụ thuộc (dependency / 의존성) direction.

Avoid designing công khai (public / 공개) thư viện (library / 라이브러리) where consumers depend heavily on hidden extends.

---

# 52. Optional Extend [ADV]

`@extend ... !optional` avoids lỗi (error / 오류) if mục tiêu (target / 대상) not found.

Use:
- khung phần mềm (framework / 프레임워크) extension hooks where mục tiêu (target / 대상) genuinely optional.

Don't use to hide typo silently.

---

# 53. `@at-root` truy vấn (query / 쿼리) cú pháp (syntax / 문법) [DEEP]

Advanced `@at-root` can include/exclude quy tắc (rule / 규칙) types.

Concept:

```scss
@at-root
  (without: media) {
  ...
}
```

or with quy tắc (rule / 규칙) categories depending cú pháp (syntax / 문법).

Useful thư viện (library / 라이브러리) metaprogramming.

Rare app-level need.

---

# 54. Bubbling At-rules [DEEP]

Sass historically “bubbles” nested at-rules such as media/supports outward while preserving bộ chọn (selector) ngữ cảnh (context / 맥락).

Example nguồn (source / 소스):

```scss
.card {
  @media (...) {
    color: red;
  }
}
```

Trình biên dịch (compiler / 컴파일러) emits media wrapping `.card`.

Understand this when đầu ra (output / 출력) thứ tự (order / 순서) matters.

---

# 55. CSS bản địa (native / 네이티브) lồng cú pháp (nesting) tính tương thích (compatibility / 호환성) [MASTER]

SCSS lồng cú pháp (nesting) and bản địa (native / 네이티브) CSS lồng cú pháp (nesting) overlap but are not identical languages historically.

Hiện đại (modern / 현대적) Sass continually aligns CSS tính tương thích (compatibility / 호환성).

If publishing plain CSS nguồn (source / 소스):
- don't assume SCSS lồng cú pháp (nesting) cú pháp (syntax / 문법) always equals trình duyệt (browser / 브라우저) lồng cú pháp (nesting) ngữ nghĩa (semantics / 의미론).

Compile SCSS.

---

# 56. nội suy (interpolation) Changes ngữ nghĩa (semantics / 의미론) [DEEP]

Inside some Sass contexts, nội suy (interpolation) can turn typed các giá trị (values) into unquoted strings.

Example:
```scss
#{$number}

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
```

may lose numeric ngữ nghĩa (semantics / 의미론) for subsequent Sass operations.

Quy tắc (rule / 규칙):
- interpolate at đầu ra (output / 출력) ranh giới (boundary / 경계),
- keep typed Sass các giá trị (values) internally.

---

# 57. Stringification ranh giới (boundary / 경계) mẫu (pattern / 패턴) [ARCH]

Nội bộ (internal / 내부):
```text
typed number/color/map
```

Only final:
```text
interpolate into selector/custom property/name
```

Equivalent:
> stringify late.

---

# 58. hiện đại (modern / 현대적) Color 4 mô hình (model / 모델) [MUST]

Colors now have:
- color không gian (space / 공간),
- channels,
- potentially missing channels,
- gamut differences.

Old giả định (assumption / 가정):
```text
color = RGB-like tuple
```
is insufficient.

---

# 59. `color.channel()` [ADV]

Use tường minh (explicit / 명시적) không gian (space / 공간) where ambiguity exists.

Concept:

```scss
color.channel(
  $color,
  "red",
  $space: rgb
)
```

Different from display-p3 red channel.

---

# 60. `color.to-space()` [ADV]

Convert biểu diễn (representation / 표현) to mục tiêu (target / 대상) color không gian (space / 공간) where supported.

Use:
- thư viện (library / 라이브러리) transforms,
- tường minh (explicit / 명시적) palette calculations.

Conversion may alter gamut biểu diễn (representation / 표현).

---

# 61. `color.adjust()` vs `color.scale()` [ADV]

> **Chuyển mạch:** Trong **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Adjust** tiếp nhận điểm tựa từ **Quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adjust

Adds/subtracts channel amount.

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Quy mô (scale / 규모)** tiếp nhận điểm tựa từ **Adjust** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Use Sass biến (variable) when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy mô (scale / 규모)

Moves channel proportionally toward min/max.

For thiết kế (design / 설계) các hệ thống (systems / 시스템들), `scale` often behaves more consistently across starting các giá trị (values).

But choose based on desired math, not rule-of-thumb.

---

# 62. Gamut ánh xạ (mapping / 매핑) Awareness [DEEP]

Wide-gamut colors may not display in mục tiêu (target / 대상) gamut.

Sass/trình duyệt (browser / 브라우저) conversion can involve out-of-gamut channels or ánh xạ (mapping / 매핑) concerns.

Master color tooling should:
- choose color không gian (space / 공간) explicitly,
- kiểm thử (test / 테스트) đầu ra (output / 출력) on actual browsers/displays.

---

# 63. thời điểm biên dịch (compile-time) Color vs thời gian chạy (runtime / 런타임) Color [MASTER]

If nguồn (source / 소스) is:

```css
var(--brand)
```

Sass does not know actual thời gian chạy (runtime / 런타임) color.

Cannot do:

```scss
color.scale(var(--brand), ...)
```

as if it were Sass color.

Use CSS:
- `color-mix`,
- relative colors,
- thời gian chạy (runtime / 런타임) color các hàm (functions).

---

# 64. động (dynamic / 동적) CSS biến (variable) Generator [ADV]

Hàm (function / 함수)/khối trộn tái sử dụng (mixin) should preserve:
- numbers with units,
- strings,
- colors,
- booleans/null ngữ nghĩa (semantics / 의미론).

Need define:
- how to serialize danh sách (list / 목록)?
- how to serialize map khóa–giá trị (map) leaf?
- should null skip?
- should quoted string keep quotes?

A môi trường vận hành (production / 운영 환경) generator needs tường minh (explicit / 명시적) chính sách (policy / 정책).

---

# 65. CSS biến (variable) Serialization chính sách (policy / 정책) [ARCH]

Example rules:

```text
number → emit as-is
color  → emit as-is
string → emit controlled interpolation
null   → skip
map    → recurse
list   → emit only if explicitly allowed
```

Don't rely on accidental `inspect()` đầu ra (output / 출력) as môi trường vận hành (production / 운영 환경) format.

---

# 66. đơn vị từ (token / 토큰) Collision Detection [ADV]

Flatten:

```text
color-text
```

could arise from:
```text
(color: (text: ...))
```

and another nguồn (source / 소스) key.

Generator should detect duplicates and `@error`.

---

# 67. đơn vị từ (token / 토큰) lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) [ARCH]

Validate:
- required groups,
- allowed types,
- naming,
- no null where forbidden.

Sass has no static hệ kiểu (type system / 타입 시스템), so thư viện (library / 라이브러리) must enforce contracts manually.

---

# 68. Sass as a Weakly Typed DSL [MASTER]

Sass supports typed thời gian chạy (runtime / 런타임) các giá trị (values) but no thời điểm biên dịch (compile-time) giao diện (interface / 인터페이스)/kiểu (type / 타입) các khai báo (declarations) like TypeScript.

Therefore robust thư viện (library / 라이브러리) relies on:
- `meta.type-of`,
- đơn vị (unit / 단위) checks,
- map khóa–giá trị (map) key checks,
- tường minh (explicit / 명시적) errors.

---

# 69. Defensive hàm (function / 함수) mẫu (pattern / 패턴) [ARCH]

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```scss
@function require-number(
  $value,
  $name
) {
  @if meta.type-of($value) != "number" {
    @error "#{$name} must be number.";
  }

  @return $value;
}
```

Use for reusable thư viện (library / 라이브러리) boundaries, not every cục bộ (local / 로컬) helper.

---

# 70. lỗi (error / 오류) Message thiết kế (design / 설계) [ARCH]

Bad:
```text
invalid
```

Good:
```text
token("space", 99):
unknown spacing key `99`.
Expected one of: 0,1,2,4,6.
```

Trình biên dịch (compiler / 컴파일러) errors are nhà phát triển (developer / 개발자) UX.

---

# 71. trạng thái ngừng khuyến nghị (deprecation) API thiết kế (design / 설계) [ARCH]

If own thư viện (library / 라이브러리) replaces API:

```scss
@mixin old-button(...) {
  @warn "old-button() is deprecated. Use button().";
  @include button(...);
}
```

Maintain cầu nối (bridge / 브리지) for one phiên bản (version / 버전) cửa sổ (window / 윈도우) when feasible.

---

# 72. trạng thái ngừng khuyến nghị (deprecation) Warnings as sản phẩm (product / 제품) UX [MASTER]

A warning should say:
1. what đã ngừng khuyến nghị (deprecated),
2. replacement,
3. removal phiên bản (version / 버전)/cửa sổ (window / 윈도우) if known,
4. chuyển đổi (migration) link if thư viện (library / 라이브러리) has docs.

---

# 73. Sass Migrator kiến trúc (architecture / 아키텍처) [ADV]

Sass Migrator can mechanically rewrite nguồn (source / 소스) for supported migrations.

Typical:
- mô-đun (module / 모듈) chuyển đổi (migration),
- division chuyển đổi (migration).

It operates on phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) with flags for dependencies/tải (load / 로드) paths.

Always:
- lần ghi nhận (commit / 커밋) first,
- migrate,
- inspect diff,
- compile,
- hồi quy giao diện (visual regression).

---

# 74. mô-đun (module / 모듈) chuyển đổi (migration) Is Architectural [MASTER]

Mechanical:
```text
@import → @use
```

but real questions:
- các không gian tên (namespaces)?
- giao diện công khai (public API)?
- circular dependencies?
- cấu hình (configuration / 구성) đơn vị sở hữu (owner / 오너)?
- CSS các tác dụng phụ (side effects)?
- private các biến (variables)?
- extend relationships?

Don't accept auto đầu ra (output / 출력) without redesign.

---

# 75. Circular phụ thuộc (dependency / 의존성) [DEEP]

Mô-đun (module / 모듈) các hệ thống (systems / 시스템들) generally cannot hỗ trợ (support / 지원) arbitrary cycles like văn bản (text / 텍스트) import did.

Example:

```text
A @use B
B @use A
```

indicates kiến trúc (architecture / 아키텍처) bài toán (problem / 문제).

Fix:
- extract dùng chung (shared / 공유) C,
- invert phụ thuộc (dependency / 의존성),
- move cấu hình (config / 설정).

---

# 76. phụ thuộc (dependency / 의존성) Inversion in Sass [ARCH]

Bad:
```text
tokens → components
components → tokens
```

Good:
```text
settings/tokens
↓
tools
↓
components
```

Dependencies điểm (point / 지점) downward.

---

# 77. Layered Sass phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) [ARCH]

Recommended:

```text
settings
  ↓
tools
  ↓
runtime-token emission
  ↓
base/layout/components/utilities
```

A lower tầng (layer / 계층) shouldn't depend on upper thành phần (component / 컴포넌트).

---

# 78. CSS lớp phân tầng (cascade layer) + Sass mô-đun (module / 모듈) tầng (layer / 계층) [MASTER]

They solve different problems.

Sass mô-đun (module / 모듈):
```text
compile-time visibility/dependency
```

CSS `@layer`:
```text
runtime cascade precedence
```

Can combine:

```scss
@use "components/button";

@layer components {
  // emitted styles
}
```

Or thành phần (component / 컴포넌트) files themselves emit within designated CSS tầng (layer / 계층).

---

# 79. Avoid Naming Collision: “mô-đun (module / 모듈)” vs “tầng (layer / 계층)”

Keep vocabulary:

```text
Sass module = @use/@forward
CSS layer   = @layer
```

They are orthogonal.

---

# 80. Sass JS API [ADV]

Dart Sass exposes JavaScript APIs for programmatic compilation.

Hiện đại (modern / 현대적) APIs include concepts:
- compile / compileString,
- async các biến thể (variants),
- importers,
- custom các hàm (functions),
- logger,
- options.

Avoid legacy JS API.

---

# 81. hiện đại (modern / 현대적) JS API vs Legacy JS API [MUST for tooling]

Legacy nút (node / 노드) Sass-style APIs have been đã ngừng khuyến nghị (deprecated).

For new tooling:
- use Dart Sass hiện đại (modern / 현대적) API.

Check hiện tại (current / 현재) JS API docs for chính xác (exact / 정확한) signatures.

---

# 82. Programmatic Compile mẫu (pattern / 패턴)

Concept:

```js
import * as sass from "sass";

const result =
  sass.compile("src/main.scss", {
    style: "compressed"
  });

console.log(result.css);
```

Chính xác (exact / 정확한) gói (package / 패키지)/mô-đun (module / 모듈) cú pháp (syntax / 문법) depends dự án (project / 프로젝트) môi trường (environment / 환경).

---

# 83. `compileString()` Use trường hợp (case / 사례)

Compile dynamically generated Sass string:
- playground,
- editor,
- kiểm thử (test / 테스트) harness.

Do not compile user-controlled Sass server-side without bảo mật (security / 보안)/tài nguyên (resource / 자원) considerations.

---

# 84. Custom các hàm (functions) from JS [ADV]

Host ngôn ngữ (language / 언어) can expose hàm (function / 함수) to Sass.

Use cases:
- read đơn vị từ (token / 토큰) thiết kế (design token) nguồn (source / 소스),
- integrate bản dựng (build / 빌드) siêu dữ liệu (metadata / 메타데이터),
- domain-specific computation.

Rủi ro (risk / 위험):
- bản dựng (build / 빌드) becomes non-portable,
- hàm (function / 함수) unavailable outside custom toolchain.

---

# 85. Custom hàm (function / 함수) ranh giới (boundary / 경계) [ARCH]

Before adding JS custom hàm (function / 함수) ask:

```text
Could data be generated before Sass?
Could CSS variable solve runtime need?
Could Sass map solve compile-time need?
```

Custom host các hàm (functions) should be last-mile tích hợp (integration / 통합).

---

# 86. Custom Importers [ADV]

Importer controls mô-đun (module / 모듈) URL resolution/loading.

Use:
- virtual modules,
- gói (package / 패키지) aliases,
- custom lưu trữ (storage / 저장소).

Requires correct:
- canonicalization,
- loading,
- cú pháp (syntax / 문법) identification.

Tooling-specialist territory.

---

# 87. Importer Canonicalization đặc tả hợp đồng (contract / 계약) [DEEP]

If importer returns inconsistent chuẩn gốc (canonical / 정본) URL:
- same mô-đun (module / 모듈) may tải (load / 로드) multiple times,
- cấu hình (configuration / 구성) ngữ nghĩa (semantics / 의미론) break,
- CSS duplicate.

Chuẩn gốc (canonical / 정본) URL must represent stable mô-đun (module / 모듈) định danh (identity / 식별자).

---

# 88. tệp (file / 파일) Importer vs Custom Importer

Hiện đại (modern / 현대적) JS API distinguishes importer styles depending use trường hợp (case / 사례).

Choose simplest built-in/tệp (file / 파일) importer/tải (load / 로드) đường dẫn (path / 경로) before custom mã (code / 코드).

---

# 89. Logger API [ADV]

Programmatic Sass compilation can intercept:
- warnings,
- gỡ lỗi (debug / 디버그) messages,
- deprecations.

CI can:
- collect,
- classify,
- thất bại (fail / 실패) on first-party warnings.

---

# 90. trạng thái ngừng khuyến nghị (deprecation) Controls [ADV]

Dart Sass offers controls for:
- silence selected deprecations,
- future/fatal deprecations,
- phụ thuộc (dependency / 의존성) warning hành vi (behavior / 동작),

through CLI/API depending phiên bản (version / 버전).

Chính sách (policy / 정책):
- never global-silence indefinitely.

---

# 91. CI trạng thái ngừng khuyến nghị (deprecation) ngân sách (budget / 예산) mẫu (pattern / 패턴) [ARCH]

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
first-party warnings = 0
dependency warnings  = tracked separately
```

Then:
- upgrade dependencies,
- maintain allowlist with expiry.

---

# 92. Compilation hiệu năng (performance / 성능) [ADV]

Factors:
- đồ thị mô-đun (module graph),
- tệp (file / 파일) I/O,
- huge loops,
- bộ chọn (selector) extension,
- recursion,
- generated CSS volume,
- custom importers/các hàm (functions).

hệ mô-đun (module system) loads once, improving duplication compared to legacy imports.

---

# 93. Measure Compile thời gian (time / 시간) [MASTER]

Do not optimize by guess.

Nhánh học (track / 트랙):
```text
cold build
warm watch rebuild
CSS bytes
source map bytes
module count
```

Set regression thresholds for very large thiết kế (design / 설계) các hệ thống (systems / 시스템들).

---

# 94. Generator hiệu năng (performance / 성능) [ADV]

Nested loops:

```text
N × M × K
```

can explode compile công việc (work / 작업)/đầu ra (output / 출력).

Example:
```text
20 colors
× 20 states
× 10 breakpoints
= 4000 rule families
```

Ask whether bên tiêu thụ (consumer / 소비자) needs all combinations.

---

# 95. Lazy Generation mẫu (pattern / 패턴) [ARCH]

Instead of generate every tiện ích (utility):
- tường minh (explicit / 명시적) enabled tiện ích (utility) groups,
- generated from used thiết kế (design / 설계) quy mô (scale / 규모),
- separate entrypoints.

Sass itself doesn't automatically tree-shake mang tính ngữ nghĩa (semantic / 의미적) loops.

---

# 96. CSS đầu ra (output / 출력) ngân sách (budget / 예산) [MASTER]

Define ngân sách (budget / 예산):

```text
base CSS <= X KB gzip
utilities <= Y KB
single component <= Z KB
```

Numbers project-specific.

Inspect compiled kết quả (result / 결과), not SCSS lines.

---

# 97. bản đồ mã nguồn (source map / 소스 맵) chi phí (cost / 비용) [ADV]

Development:
- useful detailed các map khóa–giá trị (maps).

Môi trường vận hành (production / 운영 환경):
- bản đồ mã nguồn (source map / 소스 맵) chính sách (policy / 정책) depends gỡ lỗi (debugging)/bảo mật (security / 보안)/triển khai (deployment / 배포).

Sass các bản đồ mã nguồn (source maps) can be further transformed by downstream tools; ensure chuỗi (chain / 사슬) stays correct.

---

# 98. quy trình bản dựng (build / 빌드) (build pipeline) thứ tự (ordering / 순서) [MASTER]

Dùng chung (common / 공통):

```text
SCSS
→ Sass
→ PostCSS
→ prefix
→ optimize/minify
```

Why Sass first?
PostCSS expects CSS, not Sass ngôn ngữ (language / 언어), unless special parser/plugin used.

Khung phần mềm (framework / 프레임워크) tooling may encapsulate this.

---

# 99. Browserslist Isn't Sass [MUST]

Dart Sass does not decide vendor prefixes from browserslist.

That belongs:
- PostCSS/Autoprefixer,
- bundler transformations.

Don't expect Sass cập nhật (update / 업데이트) to fix prefix chính sách (policy / 정책).

---

# 100. Sass + bản địa (native / 네이티브) CSS Modernization chiến lược (strategy / 전략) [MASTER]

As CSS grows:
- reduce Sass-only abstractions that bản địa (native / 네이티브) CSS now handles better.

Candidates:
```text
runtime variables → CSS vars
responsive component → @container
nesting → native CSS if toolchain allows
color runtime → color-mix/relative colors
```

Keep Sass for:
```text
module/package API
compile-time data
generation
validation
```

---

# 101. chuyển đổi (migration) from Sass các biến (variables) to CSS các biến (variables)

Before:

```scss
$brand: #2563eb;

.button {
  color: $brand;
}
```

After:

```scss
:root {
  --brand: #2563eb;
}

.button {
  color: var(--brand);
}
```

Do when:
- theme/thời gian chạy (runtime / 런타임) override matters.

Don't migrate build-only constants with no thời gian chạy (runtime / 런타임) giá trị (value / 값) just for fashion.

---

# 102. Hybrid đơn vị từ (token / 토큰) mẫu (pattern / 패턴) [MASTER]

Sass nguồn (source / 소스):

```scss
$tokens: (...);
```

Emit:
```css
:root {
  --...: ...;
}
```

Sass các hàm (functions) can also use same map khóa–giá trị (map) for generated static fallbacks/các tiện ích (utilities).

Single nguồn (source / 소스) can serve:
- thời điểm biên dịch (compile-time) generation,
- thời gian chạy (runtime / 런타임) CSS.

---

# 103. bên ngoài (external / 외부) đơn vị từ (token / 토큰) thiết kế (design tokens) [MASTER]

Large các hệ thống (systems / 시스템들) may use JSON/DTCG-like tokens outside Sass.

Chuỗi xử lý (pipeline / 파이프라인):

```text
token source
→ generator
→ SCSS maps
→ CSS custom properties
→ platform outputs
```

At quy mô (scale / 규모), Sass may be **bên tiêu thụ (consumer / 소비자)**, not nguồn chuẩn (source of truth / 정본).

---

# 104. Don't Parse JSON in Sass [MASTER]

If dữ liệu (data / 데이터) nguồn (source / 소스) is JSON:
- transform with công cụ bản dựng (build / 빌드) (build tool),
- generate Sass/CSS.

Don't invent JSON parser with string các hàm (functions) in Sass.

Use right ngôn ngữ (language / 언어) for bản dựng (build / 빌드) tác vụ (task / 작업).

---

# 105. Testing Sass các hàm (functions) [ADV]

Pure các hàm (functions) can be tested with:
- compile fixtures,
- assertion thư viện (library / 라이브러리)/ecosystem,
- expected CSS/lỗi (error / 오류) snapshots.

Important cases:
- valid,
- ranh giới (boundary / 경계),
- invalid kiểu (type / 타입),
- invalid đơn vị (unit / 단위),
- unknown key.

---

# 106. Golden CSS Tests [ADV]

Đầu vào (input / 입력) SCSS:

```text
fixture.scss
```

Expected:
```text
fixture.css
```

Compile and compare.

Good for:
- các khối trộn tái sử dụng (mixins),
- generators,
- bộ chọn (selector) manipulation.

Normalize formatting when appropriate.

---

# 107. lỗi (error / 오류) Tests [ADV]

Ensure:

```scss
token(unknown)
```

fails with expected diagnostic.

Công khai (public / 공개) thư viện (library / 라이브러리) chất lượng (quality / 품질) includes hành vi khi thất bại (failure behavior / 실패 동작).

---

# 108. Visual Tests Still Required [MASTER]

Sass đơn vị (unit / 단위) kiểm thử (test / 테스트) can prove:
- generated CSS cấu trúc (structure / 구조).

Cannot prove:
- trình duyệt (browser / 브라우저) bố cục (layout / 레이아웃) correct,
- accessible tương tác (interaction / 상호작용),
- đa trình duyệt (cross-browser) rendering.

Need CSS visual/thành phần (component / 컴포넌트) tests.

---

# 109. Snapshot kiểm thử (test / 테스트) Pitfall

Generated CSS snapshot can be huge/noisy.

Prefer:
- targeted fixture,
- mang tính ngữ nghĩa (semantic / 의미적) assertions,
- stable formatting.

Don't snapshot entire 500KB bundle for every đơn vị (unit / 단위) kiểm thử (test / 테스트).

---

# 110. Linting SCSS [MUST]

Stylelint with SCSS-aware cấu hình (config / 설정)/plugins can check:
- Sass at-rules,
- lồng cú pháp (nesting),
- naming,
- đã ngừng khuyến nghị (deprecated) patterns.

Rules should align kiến trúc (architecture / 아키텍처).

---

# 111. Ban Legacy Constructs [ARCH]

Possible chính sách (policy / 정책):
```text
no Sass @import
no slash division
no global map-get
no old color helpers
no !global
restricted @extend
max nesting
```

Tooling hỗ trợ (support / 지원) varies; CI grep/custom lint can supplement.

---

# 112. gói (package / 패키지) Publishing [ARCH]

Sass gói (package / 패키지) should expose stable entrypoints.

Example conceptual:
```text
package/
├─ scss/
│  ├─ _index.scss
│  └─ ...
└─ dist/
   └─ styles.css
```

Consumers may want:
- precompiled CSS,
- Sass API.

Document both.

---

# 113. gói (package / 패키지) Resolution [ADV]

Nút (node / 노드) gói (package / 패키지) Sass imports may be resolved via bundler/importer/gói (package / 패키지) conventions.

Don't rely on undocumented resolution magic.

Publish clear import examples tested in dùng chung (common / 공통) toolchains.

---

# 114. phiên bản (version / 버전) tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) [ARCH]

Thư viện (library / 라이브러리) docs:

```text
Library 3.x
requires Dart Sass >= X
```

Needed when using newer:
- mô-đun (module / 모듈) APIs,
- map khóa–giá trị (map) các hàm (functions),
- color APIs,
- meta các khối trộn tái sử dụng (mixins),
- CSS tính tương thích (compatibility / 호환성) changes.

---

# 115. LibSass tính tương thích (compatibility / 호환성) Is a chi phí (cost / 비용)

Supporting old hiện thực (implementation / 구현) means losing:
- `@use`,
- `@forward`,
- built-in mô-đun (module / 모듈) APIs,
- newer ngôn ngữ (language / 언어) features.

For hiện đại (modern / 현대적) thư viện (library / 라이브러리):
- don't hỗ trợ (support / 지원) dead trình biên dịch (compiler / 컴파일러) unless nghiệp vụ (business / 비즈니스) ràng buộc (constraint / 제약조건) tường minh (explicit / 명시적).

---

# 116. Breaking thay đổi (change / 변경) Monitoring [MASTER]

Nhánh học (track / 트랙) official Sass breaking changes.

Recent/hiện tại (current / 현재) themes include:
- imports/toàn cục (global / 전역) các hàm (functions),
- Color 4 APIs,
- legacy JS API,
- mixed các khai báo (declarations),
- private cấu hình (configuration / 구성),
- legacy if,
- rest args,
- bộ chọn (selector) parsing,
- CSS hàm (function / 함수) names.

Upgrade Sass proactively in CI.

---

# 117. Pinning vs Floating trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전)

Lockfile should make builds reproducible.

But also have periodic phụ thuộc (dependency / 의존성) cập nhật (update / 업데이트) tiến trình (process / 프로세스):
- renovate/dependabot/manual,
- CI on new Sass bản phát hành (release / 릴리스) if trọng yếu (critical / 중요) thư viện (library / 라이브러리).

Avoid surprise after 2 years frozen.

---

# 118. Upgrade kiểm thử (test / 테스트) ma trận (matrix / 행렬) [ARCH]

On Sass upgrade:

```text
compile
deprecation warnings
unit fixtures
visual regression
bundle size
compile time
```

Especially for hệ thống thiết kế (design system).

---

# 119. Mixed khai báo (declaration) chuyển đổi (migration) [2026]

Old Sass historically reordered các khai báo (declarations) around nested rules.

Hiện đại (modern / 현대적) Sass follows CSS hành vi (behavior / 동작)/thứ tự (order / 순서).

chuyển đổi (migration) chiến lược (strategy / 전략):
- keep cơ sở (base / 기반) các khai báo (declarations) grouped,
- avoid relying on historical hoisting,
- inspect compiled thứ tự (order / 순서).

---

# 120. toàn cục (global / 전역) Built-in chuyển đổi (migration) [2026]

Mechanical idea:

```scss
map-get(...)
```

→

```scss
@use "sass:map";
map.get(...)
```

Likewise:
- danh sách (list / 목록),
- math,
- color,
- string,
- meta.

Benefit is ngôn ngữ (language / 언어) tính tương thích (compatibility / 호환성), not just style.

---

# 121. Color chuyển đổi (migration) [2026]

Old:
```scss
lighten($brand, 10%)
```

Don't mechanically replace with arbitrary hàm (function / 함수) without intent.

Decide:
- adjust absolute lightness?
- quy mô (scale / 규모) toward white?
- operate in HSL or Oklch?
- thời gian chạy (runtime / 런타임) or thời điểm biên dịch (compile-time)?

Color chuyển đổi (migration) is thiết kế (design / 설계) quyết định (decision / 결정).

---

# 122. Slash chuyển đổi (migration) [2026]

Arithmetic:
```scss
math.div(...)
```

CSS separator remains:
```scss
grid-row: 1 / 3;
```

các danh sách (lists) may need tường minh (explicit / 명시적) slash separator APIs for computed Sass danh sách (list / 목록) generation.

---

# 123. Avoid trạng thái ngừng khuyến nghị (deprecation) Cargo Cult

Don't rewrite mã (code / 코드) solely to silence warning without understanding mang tính ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경).

Tiến trình (process / 프로세스):
```text
read warning
→ read breaking-change page
→ reproduce
→ migrate
→ test output
```

---

# 124. Master phản mẫu (anti-pattern) — Sass khung phần mềm (framework / 프레임워크) Inside App

Symptoms:
- 100 generic các khối trộn tái sử dụng (mixins),
- hàm (function / 함수) dispatch,
- recursive cấu hình (config / 설정),
- bộ chọn (selector) DSL,
- huge generated các tiện ích (utilities),
- no one knows đầu ra (output / 출력).

If app isn't publishing style khung phần mềm (framework / 프레임워크):
simplify.

---

# 125. Master phản mẫu (anti-pattern) — thời gian chạy (runtime / 런타임) lô-gic (logic / 논리) in Sass

Bad expectation:
```text
if viewport > ...
if user selected dark...
if server data...
```

Sass runs before trình duyệt (browser / 브라우저).

Use CSS/JS thời gian chạy (runtime / 런타임).

---

# 126. Master phản mẫu (anti-pattern) — CSS Hidden Behind các khối trộn tái sử dụng (mixins)

Nguồn (source / 소스):

```scss
@include card-everything(
  compact,
  elevated,
  responsive
);
```

Reviewer can't see:
- display,
- overflow,
- focus,
- motion.

Use các khối trộn tái sử dụng (mixins) for orthogonal reusable concerns, not whole thành phần (component / 컴포넌트) hành vi (behavior / 동작) unless thư viện (library / 라이브러리) lớp trừu tượng (abstraction / 추상화) explicitly warrants.

---

# 127. Master phản mẫu (anti-pattern) — Over-normalized đơn vị từ (token / 토큰) các map khóa–giá trị (maps)

Example:
```text
tokens.component.button.state.hover.color.background.default...
```

Every lookup 7 keys deep.

This mirrors cơ sở dữ liệu (database / 데이터베이스) normalization, not useful styling.

Prefer mang tính ngữ nghĩa (semantic / 의미적) flatness where practical.

---

# 128. Master mẫu (pattern / 패턴) — Stable mang tính ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계)

Inside thư viện (library / 라이브러리) can thay đổi (change / 변경):
- color math,
- spacing formula,
- map khóa–giá trị (map) cấu trúc (structure / 구조).

Công khai (public / 공개) đặc tả hợp đồng (contract / 계약) stays:
```text
token("color-action")
@mixin focus-ring
$radius-default config
```

đóng gói (encapsulation) matters even in Sass.

---

# 129. Master mẫu (pattern / 패턴) — Build-time Adapter

Bên ngoài (external / 외부) đơn vị từ (token / 토큰) nguồn (source / 소스)/vendor:

```text
upstream API
→ adapter module
→ internal canonical values
```

All weird tính tương thích (compatibility / 호환성) localized.

---

# 130. Master mẫu (pattern / 패턴) — thời điểm biên dịch (compile-time) tính năng (feature / 기능) Flags

Cấu hình (config / 설정):

```scss
$enable-grid-utilities: true !default;
```

Generator:

```scss
@if $enable-grid-utilities {
  ...
}
```

Good for thư viện (library / 라이브러리) optional CSS bundles.

Bad for thời gian chạy (runtime / 런타임) tính năng (feature / 기능) trạng thái (state / 상태).

---

# 131. cờ tính năng (feature flag / 기능 플래그) ngân sách (budget / 예산)

Too many flags create combinatorial kiểm thử (test / 테스트) ma trận (matrix / 행렬).

Expose only high-value bản dựng (build / 빌드) options.

---

# 132. Master mẫu (pattern / 패턴) — tường minh (explicit / 명시적) CSS các tác dụng phụ (side effects)

Document mô-đun (module / 모듈):

```text
@use "library/tools"
→ emits no CSS

@use "library/components"
→ emits components
```

Bên tiêu thụ (consumer / 소비자) can reason bundle chi phí (cost / 비용).

---

# 133. Master mẫu (pattern / 패턴) — Layer-aware thư viện (library / 라이브러리)

Thư viện (library / 라이브러리) can emit CSS in named tầng (layer / 계층):

```scss
@layer ds.components {
  ...
}
```

Bên tiêu thụ (consumer / 소비자) controls toàn cục (global / 전역) tầng (layer / 계층) thứ tự (order / 순서).

This is often better than high độ đặc hiệu (specificity).

---

# 134. thư viện (library / 라이브러리) tầng (layer / 계층) đặc tả hợp đồng (contract / 계약)

Document:
```text
ds.reset
ds.base
ds.components
ds.utilities
```

Consumers can define tầng (layer / 계층) thứ tự (ordering / 순서) early.

Don't hide tầng (layer / 계층) hành vi (behavior / 동작).

---

# 135. Sass cấu hình (config / 설정) vs CSS đơn vị từ (token / 토큰) Override API

Công khai (public / 공개) thư viện (library / 라이브러리) might offer both:

thời điểm biên dịch (compile-time):
```scss
@use "lib" with (
  $enable-legacy: false
);
```

Thời gian chạy (runtime / 런타임):
```css
:root {
  --lib-brand: ...;
}
```

Different responsibilities.

---

# 136. Master quyết định (decision / 결정) ma trận (matrix / 행렬)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Use Sass biến (variable) when:** tiếp nhận điểm tựa từ **Quy mô (scale / 규모)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CSS biến (variable) when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Use Sass biến (variable) when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- thời điểm biên dịch (compile-time) only,
- generation,
- gói (package / 패키지) cấu hình (config / 설정).

> **Chuyển mạch:** Trong **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **CSS biến (variable) when:** tiếp nhận điểm tựa từ **Use Sass biến (variable) when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sass hàm (function) when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSS biến (variable) when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- thời gian chạy (runtime) theme,
- cơ chế phân tầng (cascade),
- thành phần (component / 컴포넌트) override.

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Sass hàm (function) when:** tiếp nhận điểm tựa từ **CSS biến (variable) when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CSS hàm (function) when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sass hàm (function) when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- thời điểm biên dịch (compile-time) giá trị (value) transformation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **CSS hàm (function) when:** tiếp nhận điểm tựa từ **Sass hàm (function) when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **khối trộn tái sử dụng (mixin) when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSS hàm (function) when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- layout/thời gian chạy (runtime) giá trị (value).

> **Chuyển mạch:** Trong **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **khối trộn tái sử dụng (mixin) when:** tiếp nhận điểm tựa từ **CSS hàm (function) when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tiện ích (utility) when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## khối trộn tái sử dụng (mixin) when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- reusable style generation.

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **tiện ích (utility) when:** tiếp nhận điểm tựa từ **khối trộn tái sử dụng (mixin) when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **@forward when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tiện ích (utility) when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- thời gian chạy (runtime) composition.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **@forward when:** tiếp nhận điểm tựa từ **tiện ích (utility) when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **@extend when:** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `@forward` when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- package facade.

> **Chuyển mạch:** Trong **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **@extend when:** tiếp nhận điểm tựa từ **@forward when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Senior SCSS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `@extend` when:

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- true bộ chọn (selector) mang tính ngữ nghĩa (semantic) extension.

---

# 137. hiệu năng (performance / 성능) quyết định (decision / 결정) ma trận (matrix / 행렬)

Before generator:
```text
How many selectors?
How many declarations?
How many media variants?
Will users use them?
Can downstream purge safely?
```

Before khối trộn tái sử dụng (mixin):
```text
How many include sites?
How large block?
Would runtime class be smaller?
```

---

# 138. gỡ lỗi (debugging) Compile Errors [MASTER]

Workflow:

```text
1. read full Sass diagnostic
2. identify source span
3. check module namespace
4. inspect types with meta.type-of
5. inspect values with @debug/meta.inspect
6. reduce reproduction
7. check deprecation/breaking-change docs
8. inspect generated CSS after fix
```

---

# 139. gỡ lỗi (debugging) mô-đun (module / 모듈) Errors

Check:
- wrong URL,
- tải (load / 로드) đường dẫn (path / 경로),
- không gian tên (namespace / 네임스페이스) collision,
- mô-đun (module / 모듈) configured twice,
- thành viên riêng tư (private member) truy cập (access / 접근),
- circular phụ thuộc (dependency / 의존성),
- importer canonicalization.

---

# 140. gỡ lỗi (debugging) “Wrong CSS”

Determine tầng (layer / 계층):

```text
SCSS source wrong?
Compiler output wrong?
PostCSS transformed?
Minifier changed?
Browser cascade?
```

Always inspect generated CSS before blaming Sass.

---

# 141. gỡ lỗi (debugging) kiểu (type / 타입) Errors

Print:

```scss
@debug meta.type-of($value);
@debug meta.inspect($value);
```

Check:
- number units,
- map khóa–giá trị (map) vs danh sách (list / 목록),
- quoted string,
- null,
- calculation.

---

# 142. gỡ lỗi (debugging) map khóa–giá trị (map) API

Before `map.get`:
```scss
@debug map.keys($map);
```

Validate nested keys.

Don't let missing map khóa–giá trị (map) key silently propagate `null` into style unless intentional.

---

# 143. gỡ lỗi (debugging) Color API

Check:
- color không gian (space / 공간),
- channel name,
- đơn vị (unit / 단위),
- whether giá trị (value / 값) is Sass color or CSS thời gian chạy (runtime / 런타임) string/var.

Hiện đại (modern / 현대적) Color 4 makes implicit các giả định (assumptions / 가정들) riskier.

---

# 144. Master Lab 1 — đồ thị mô-đun (module graph)

Bản dựng (build / 빌드):
```text
settings
tools
tokens
components
facade
application
```

Verify:
- no cycles,
- cấu hình (config / 설정) once,
- CSS emitted once.

---

# 145. Master Lab 2 — Sass thư viện (library / 라이브러리) API

Expose:
- 3 cấu hình (config / 설정) vars,
- 2 các hàm (functions),
- 2 các khối trộn tái sử dụng (mixins),
- facade prefix,
- one private helper.

Ghi (write / 쓰기) bên tiêu thụ (consumer / 소비자) examples.

---

# 146. Master Lab 3 — Deep đơn vị từ (token / 토큰) trình biên dịch (compiler / 컴파일러)

Đầu vào (input / 입력) nested map khóa–giá trị (map).

Features:
- flatten,
- validate,
- collision detect,
- skip null,
- emit CSS vars.

Add tests.

---

# 147. Master Lab 4 — Color 4 Palette

Use:
- Oklch,
- `color.scale`,
- `color.channel`,
- tường minh (explicit / 명시적) spaces.

Compare đầu ra (output / 출력) with CSS thời gian chạy (runtime / 런타임) color-mix.

---

# 148. Master Lab 5 — bộ chọn (selector) Algebra

Use:
- unify,
- nest,
- superselector checks.

Inspect đầu ra (output / 출력) and document why not string nội suy (interpolation).

---

# 149. Master Lab 6 — Migrate Legacy dự án (project / 프로젝트)

Legacy:
```text
@import
map-get
lighten
slash division
global variables
```

Migrate to:
- modules,
- built-ins,
- hiện đại (modern / 현대적) color,
- `math.div`.

Visual diff.

---

# 150. Master Lab 7 — JS API

Programmatically:
- compile tệp (file / 파일),
- capture warning,
- custom logger,
- bản đồ mã nguồn (source map / 소스 맵) awareness.

---

# 151. Master Lab 8 — Custom hàm (function / 함수)

Expose one safe JS custom hàm (function / 함수).

Then ghi (write / 쓰기) alternative bản dựng (build / 빌드) step and compare coupling.

---

# 152. Master Lab 9 — Custom Importer

Implement virtual mô-đun (module / 모듈) resolver.

Verify same logical mô-đun (module / 모듈) canonicalizes once.

Tooling-specialist exercise.

---

# 153. Master Lab 10 — đầu ra (output / 출력) ngân sách (budget / 예산)

Create tiện ích (utility) generator.

Measure:
- compile thời gian (time / 시간),
- raw CSS,
- gzip,
- coverage.

Reduce đầu ra (output / 출력) 30% without losing required API.

---

# 154. Master Self-Test

1. chuẩn gốc (canonical / 정본) mô-đun (module / 모듈) URL là gì?
2. Vì sao mô-đun (module / 모듈) tải (load / 로드) once?
3. cấu hình (configuration / 구성) được áp lúc nào?
4. Vì sao configure-after-load thất bại (fail / 실패)?
5. công cụ (tool / 도구) mô-đun (module / 모듈) khác CSS side-effect mô-đun (module / 모듈)?
6. `meta.load-css` khác `@use`?
7. Reflection APIs phù hợp khi nào?
8. Argument danh sách (list / 목록) khác normal danh sách (list / 목록)?
9. map khóa–giá trị (map) list-like hành vi (behavior / 동작) có pitfall gì?
10. Deep merge cần chính sách (policy / 정책) gì?
11. đơn vị (unit / 단위) algebra ảnh hưởng hàm (function / 함수) thiết kế (design / 설계) ra sao?
12. Sass calculation khác number?
13. Vì sao interpolate late?
14. Color không gian (space / 공간) làm old color helpers problematic thế nào?
15. hợp nhất bộ chọn (selector unification) là gì?
16. `@extend` không phải khai báo (declaration) bản sao (copy / 복사) vì sao?
17. mô-đun (module / 모듈) phụ thuộc (dependency / 의존성) cycle sửa thế nào?
18. Sass mô-đun (module / 모듈) vs CSS tầng (layer / 계층)?
19. hiện đại (modern / 현대적) JS API dùng cho gì?
20. Custom importer cần canonicalize vì sao?
21. Custom hàm (function / 함수) có portability chi phí (cost / 비용) gì?
22. Compile hiệu năng (performance / 성능) bottleneck nào?
23. Vì sao nguồn (source / 소스) kích thước (size / 크기) không đại diện đầu ra (output / 출력) kích thước (size / 크기)?
24. Sass Migrator không thay kiến trúc (architecture / 아키텍처) rà soát (review / 검토) vì sao?
25. Private cấu hình (config / 설정) trạng thái ngừng khuyến nghị (deprecation) nói gì về API thiết kế (design / 설계)?
26. toàn cục (global / 전역) built-in trạng thái ngừng khuyến nghị (deprecation) liên quan CSS tính tương thích (compatibility / 호환성) thế nào?
27. Legacy `if()` trạng thái ngừng khuyến nghị (deprecation) liên quan CSS evolution ra sao?
28. `--` Sass hàm (function / 함수)/khối trộn tái sử dụng (mixin) names vì sao đã ngừng khuyến nghị (deprecated)?
29. đơn vị từ (token / 토큰) lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) thiết kế sao?
30. Generated CSS serialization chính sách (policy / 정책) cần gì?
31. bên ngoài (external / 외부) đơn vị từ (token / 토큰) nguồn (source / 소스) nên integrate thế nào?
32. Sass testing khác visual testing?
33. gói (package / 패키지) nên expose Sass + CSS entrypoints ra sao?
34. phiên bản (version / 버전) ma trận (matrix / 행렬) cần khi nào?
35. Upgrade Sass cần kiểm thử (test / 테스트) gì?
36. khối trộn tái sử dụng (mixin) duplication vs tiện ích (utility) tradeoff?
37. cờ tính năng (feature flag / 기능 플래그) thời điểm biên dịch (compile-time) khác thời gian chạy (runtime / 런타임)?
38. Layer-aware Sass thư viện (library / 라이브러리) có lợi gì?
39. Khi nào Sass lớp trừu tượng (abstraction / 추상화) đã quá mức?
40. Khi nào bỏ Sass để dùng bản địa (native / 네이티브) CSS?

---

# 155. Mastery Rubric

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Senior SCSS** tiếp nhận điểm tựa từ **@extend when:** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sass Library Engineer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Senior SCSS

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- modern modules,
- các khối trộn tái sử dụng (mixins)/các hàm (functions),
- các map khóa–giá trị (maps),
- kiến trúc (architecture / 아키텍처),
- clean deprecations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Sass Library Engineer** tiếp nhận điểm tựa từ **Senior SCSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sass Tooling Specialist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sass Library Engineer

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- facade API,
- cấu hình (configuration / 구성),
- kiểm tra hợp lệ (validation / 검증),
- các bộ chọn (selectors)/meta,
- tests,
- versioning.

> **Chuyển mạch:** Trong **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Sass Tooling Specialist** tiếp nhận điểm tựa từ **Sass Library Engineer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Master** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sass Tooling Specialist

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
- JS API,
- importer,
- custom các hàm (functions),
- chuẩn gốc (canonical / 정본) URLs,
- compile diagnostics/hiệu năng (performance / 성능).

> **Chuyển mạch:** Ở chặng này của **SCSS Master Supplement — Dart Sass Deep Dive (2026)**, **Master** tiếp nhận điểm tựa từ **Sass Tooling Specialist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Master
Có thể:
- thiết kế thời điểm biên dịch (compile-time) API,
- migrate legacy hệ thống (system / 시스템),
- explain trình biên dịch (compiler / 컴파일러)/mô-đun (module / 모듈) hành vi (behavior / 동작),
- predict đầu ra (output / 출력) chi phí (cost / 비용),
- respond to CSS/Sass ngôn ngữ (language / 언어) evolution,
- biết khi nào **không dùng Sass**.

---

# 156. hiện đại (modern / 현대적) 2026 Watchlist

Theo dõi official Sass Breaking Changes cho:
```text
@import removal path
global built-in removal
Color 4 APIs
legacy JS API
private config
legacy if()
rest argument rules
selector parsing
plain CSS function compatibility
mixed declaration semantics
```

Đừng học version-specific workaround như permanent mẫu (pattern / 패턴).

---

# 157. môi trường vận hành (production / 운영 환경) Checklist

Before merge:

```text
[ ] no Sass @import
[ ] no slash arithmetic
[ ] namespaced built-ins
[ ] no deprecated color helper
[ ] no first-party warnings
[ ] module graph acyclic
[ ] public config intentional
[ ] private internals not leaked
[ ] nesting reasonable
[ ] @extend reviewed
[ ] generated output inspected
[ ] bundle size acceptable
[ ] source maps work
[ ] CSS visual tests pass
[ ] browser behavior tested
```

---

# 158. tham chiếu (reference / 참조) map khóa–giá trị (map)

Official:
- https://sass-lang.com/documentation/
- https://sass-lang.com/documentation/at-rules/use/
- https://sass-lang.com/documentation/at-rules/forward/
- https://sass-lang.com/documentation/at-rules/mixin/
- https://sass-lang.com/documentation/at-rules/hàm (function / 함수)/
- https://sass-lang.com/documentation/modules/
- https://sass-lang.com/documentation/modules/meta/
- https://sass-lang.com/documentation/modules/selector/
- https://sass-lang.com/documentation/js-api/
- https://sass-lang.com/documentation/breaking-changes/
- https://sass-lang.com/documentation/breaking-changes/import/
- https://sass-lang.com/documentation/breaking-changes/slash-div/
- https://sass-lang.com/documentation/breaking-changes/color-functions/

---

---

# 161. đồ thị mô-đun (module graph) rà soát (review / 검토) — checklist ở mức thư viện (library / 라이브러리)/tooling specialist

Khi rà soát (review / 검토) một Sass gói (package / 패키지), hãy vẽ phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) thay vì chỉ nhìn folder cây (tree / 트리). Mỗi nút (node / 노드) nên được phân loại: tool-only, style-emitting, cấu hình (configuration / 구성) nguồn (source / 소스) hay facade/entry điểm (point / 지점). Cycle hoặc phụ thuộc (dependency / 의존성) ngược từ low-level đơn vị từ (token / 토큰) mô-đun (module / 모듈) lên thành phần (component / 컴포넌트) mô-đun (module / 모듈) là dấu hiệu ranh giới (boundary / 경계) sai. Nếu một công cụ (tool / 도구) mô-đun (module / 모듈) cần thành phần (component / 컴포넌트) biến (variable) để hoạt động, quyền sở hữu (ownership / 소유권) đang bị đảo.

`@use` bảo đảm mô-đun (module / 모듈) được evaluate một lần theo chuẩn gốc (canonical / 정본) URL, nhưng canonicalization/importer hành vi (behavior / 동작) vẫn quan trọng trong thư viện (library / 라이브러리) tooling. Hai URL khác nhau trỏ cùng logical mô-đun (module / 모듈) cần được importer canonicalize đúng để tránh duplicate mô-đun (module / 모듈) identities. Đây là lý do custom importer/gói (package / 패키지) thiết kế (design / 설계) thuộc master-level Sass chứ không chỉ cú pháp (syntax / 문법).

chuyển đổi (migration) từ `@import` nên được làm theo đồ thị (graph / 그래프): xác định globals thật sự là công khai (public / 공개) cấu hình (config / 설정), globals nào là accidental coupling, tách facade, rồi mới chạy migrator/replace cú pháp (syntax / 문법). Chuyển máy móc `@import` thành `@use as *` giữ lại toàn cục (global / 전역) không gian tên (namespace / 네임스페이스) bài toán (problem / 문제) và bỏ lỡ phần lớn lợi ích hệ mô-đun (module system).

Generated CSS là acceptance kiểm thử (test / 테스트) cuối cùng. Sau chuyển đổi (migration), diff bộ chọn (selector) count, khai báo (declaration) duplication, tầng (layer / 계층)/thứ tự nguồn (source order) và bundle bytes; compile success không đủ chứng minh hành vi (behavior / 동작) giữ nguyên.

---

# Kết luận

“Master SCSS” không có nghĩa biến Sass thành programming ngôn ngữ (language / 언어) phức tạp nhất có thể.

Maturity đường dẫn (path / 경로):

```text
Beginner:
use variables/nesting

Intermediate:
mixins/maps/functions

Senior:
modules + architecture + output discipline

Master:
compiler/module model
+ library API
+ migration
+ tooling
+ compatibility
+ know when native CSS is better
```

Nguyên tắc cuối:

```text
Use Sass to make CSS authoring safer.
Never make CSS behavior harder to understand
just because Sass can generate it.
```

> **Bàn giao:** Sau **Master**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
