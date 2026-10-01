# CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Quy ước thuật ngữ Việt–Anh** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **1. thuộc tính (property / 속성) / cú pháp (syntax / 문법)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> Mục tiêu: đây không phải là danh sách thuộc tính (property / 속성) để học thuộc. Tài liệu được tổ chức theo **mô hình tư duy (mental model / 사고 모델) của trình duyệt (browser / 브라우저)**, sau đó mới đến thuộc tính (property / 속성), bố cục (layout / 레이아웃), responsive, kiến trúc (architecture / 아키텍처) và CSS hiện đại.
> Nếu đọc + tự mã (code / 코드) lại toàn bộ ví dụ + làm các bài tập cuối mỗi phần, bạn sẽ có nền tảng CSS đủ để làm môi trường vận hành (production / 운영 환경) frontend ở mức cấp cao (senior / 시니어).
>
> Ký hiệu:
> - **[cốt lõi (core / 핵심)]**: phải biết và dùng thường xuyên.
> - **[ADV]**: kiến thức nâng cao, cấp cao (senior / 시니어) cần hiểu bản chất.
> - **[hiện đại (modern / 현대적)]**: CSS hiện đại, nên dùng khi mức hỗ trợ trình duyệt (browser support / 브라우저 지원) của dự án (project / 프로젝트) cho phép.
> - **⚠ Pitfall**: lỗi thường gặp.
> - **cấp cao (senior / 시니어) ghi chú (note / 노트)**: cách suy nghĩ/thiết kế CSS trong dự án (project / 프로젝트) thật.

---

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ chuyên môn được ưu tiên diễn đạt bằng tiếng Việt tự nhiên và giữ thuật ngữ gốc bên cạnh để dễ đối chiếu. Ví dụ: **cơ chế phân tầng (cascade)**, **độ đặc hiệu (specificity)**, **kế thừa (inheritance)**, **mô hình hộp (box model / 박스 모델)**, **luồng bố cục thông thường (normal flow / 일반 흐름)**, **ngữ cảnh định dạng (formatting context / 서식 컨텍스트)**, **khối chứa tham chiếu (containing block / 컨테이닝 블록)**, **định cỡ nội tại (intrinsic sizing / 내재 크기 결정)** và **ngữ cảnh xếp chồng (stacking context / 쌓임 맥락)**. Tên thuộc tính (property / 속성), giá trị (value / 값), selector, at-rule và API khi xuất hiện dưới dạng mã vẫn được giữ nguyên để không làm sai cú pháp.

# Cách đọc tài liệu chuẩn gốc (canonical / 정본)

Mỗi nhóm kiến thức quan trọng được đọc theo 4 tầng tư duy:

```text
Property / Syntax
→ Language Idiom
→ Coding / Programming Pattern
→ Design / Architecture Pattern
```

> **Chuyển mạch:** Thuật ngữ và syntax xác định cách đọc một declaration; CSS idiom tiếp theo cho thấy declaration được nhóm, cascade và tổ chức thành pattern bảo trì được thế nào.

## 1. thuộc tính (property / 속성) / cú pháp (syntax / 문법)

Đây là tầng thấp nhất: thuộc tính (property / 속성) làm gì, nhận giá trị (value / 값) nào, computed hành vi (behavior / 동작) ra sao.

Ví dụ:

```css
display: flex;
gap: 1rem;
```

> **Chuyển mạch:** Property và syntax là primitives; CSS idiom tiếp theo tổ chức chúng thành pattern dễ đọc, dễ cascade và dễ bảo trì.

## 2. CSS lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구)

**Idiom** là một cách viết CSS ngắn, quen thuộc, lặp đi lặp lại vì nó phù hợp với cách trình duyệt (browser / 브라우저) bố cục (layout / 레이아웃) hoạt động.

Ví dụ:

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

Đây là idiom **fluid centered bộ chứa (container / 컨테이너)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **3. Coding / mẫu lập trình (programming pattern / 프로그래밍 패턴)** tiếp nhận điểm tựa từ **2. CSS lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. CSS thiết kế (design / 설계) / kiến trúc (architecture / 아키텍처) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Coding / mẫu lập trình (programming pattern / 프로그래밍 패턴)

Mẫu (pattern / 패턴) ở tầng này giải quyết một bài toán hiện thực (implementation / 구현) lặp lại.

Ví dụ **Media đối tượng (object / 객체)**:

```css
.media {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 1rem;
}
```

Dùng cho:
- avatar + content,
- icon + văn bản (text / 텍스트),
- thumbnail + description.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4. CSS thiết kế (design / 설계) / kiến trúc (architecture / 아키텍처) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **3. Coding / mẫu lập trình (programming pattern / 프로그래밍 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cơ chế phân tầng (cascade) trước, độ đặc hiệu (specificity) sau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. CSS thiết kế (design / 설계) / kiến trúc (architecture / 아키텍처) mẫu (pattern / 패턴)

Không nên hiểu "mẫu thiết kế (design pattern / 디자인 패턴) trong CSS" theo nghĩa GoF của Java.

Trong CSS, mẫu thiết kế (design pattern / 디자인 패턴) thường là:
- cách tổ chức cơ chế phân tầng (cascade),
- cách định nghĩa hợp đồng thành phần (component contract),
- cách thiết kế đơn vị từ (token / 토큰),
- cách quản lý các biến thể (variants)/các trạng thái (states),
- cách chia bố cục (layout / 레이아웃) thành phần nguyên thủy (primitive / 기본 요소),
- cách isolate style,
- cách responsive thành phần (component / 컴포넌트).

Ví dụ:

```text
Global Token
→ Semantic Token
→ Component Token
→ Component Variant
```

Mỗi mục quan trọng có thêm:

```text
CSS Idiom
Coding Pattern
Design Pattern
Senior Note
Pitfall
```

Mục tiêu là học được **cách cấp cao (senior / 시니어) ghép các thuộc tính (property / 속성) thành hệ thống**, không chỉ nhớ tên thuộc tính (property / 속성).

---

# 0. Bản đồ học CSS

# 0A. mô hình tư duy (mental model / 사고 모델) xuyên suốt: từ khai báo (declaration) tới điểm ảnh (pixel / 픽셀) trên màn hình

CSS dễ bị học thành một danh sách thuộc tính (property / 속성) rời rạc, nhưng trình duyệt (browser / 브라우저) không xử lý CSS theo cách đó. Khi HTML và biểu định kiểu (stylesheet / 스타일시트) được tải (load / 로드), trình duyệt (browser / 브라우저) trước tiên phải xác định bộ chọn (selector) nào match element. Sau đó cơ chế phân tầng (cascade) chọn khai báo (declaration) thắng cho từng thuộc tính (property / 속성). Chỉ sau khi cơ chế phân tầng (cascade)/defaulting hoàn tất, kế thừa (inheritance) mới cung cấp giá trị (value / 값) cho những thuộc tính (property / 속성) có cơ chế thừa hưởng. trình duyệt (browser / 브라우저) tiếp tục tạo box, xác định luồng bố cục thông thường (normal flow / 일반 흐름) và ngữ cảnh định dạng (formatting context / 서식 컨텍스트), resolve khối chứa tham chiếu (containing block / 컨테이닝 블록), intrinsic/available kích thước (size / 크기) và positioning, chạy thuật toán bố cục (layout algorithm) như Flexbox/Grid, rồi mới paint và composite.

Trục học chuẩn gốc (canonical / 정본) của CSS vì vậy là:

```text
selector matching
→ cascade
→ specificity / scope proximity / source order
→ inheritance + initial/defaulting
→ box model + sizing
→ normal flow
→ formatting context
→ positioning + containing block
→ Flexbox / Grid / other layout algorithms
→ responsive conditions
→ paint / composite / performance
```

Khi CSS “không chạy”, hãy truy theo đúng trục này thay vì đổi thuộc tính (property / 속성) ngẫu nhiên. Ví dụ `.card { width: 100% }` có thể không cho kết quả mong muốn vì bộ chọn (selector) không match, quy tắc (rule / 규칙) ở tầng (layer / 계층) khác thắng, percentage resolve theo khối chứa tham chiếu (containing block / 컨테이닝 블록) khác, phần tử Flex (flex item) bị kích thước tối thiểu tự động (automatic minimum size) chặn co, hoặc parent tạo overflow/ngữ cảnh định dạng (formatting context / 서식 컨텍스트) khác với giả định (assumption / 가정). Thêm `!important` chỉ giải quyết một nhánh rất nhỏ của cây nguyên nhân.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4. CSS thiết kế (design / 설계) / kiến trúc (architecture / 아키텍처) mẫu (pattern / 패턴)** xác định đầu vào; **cơ chế phân tầng (cascade) trước, độ đặc hiệu (specificity) sau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **kế thừa (inheritance) không phải “độ đặc hiệu (specificity) của parent truyền xuống con”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cơ chế phân tầng (cascade) trước, độ đặc hiệu (specificity) sau

độ đặc hiệu (specificity) không phải luật đầu tiên của CSS. cơ chế phân tầng (cascade) trước tiên xét relevance, nguồn và mức quan trọng (origin/importance) và lớp phân tầng (cascade layer). độ đặc hiệu (specificity) chỉ được so giữa những khai báo (declaration) vẫn còn cạnh tranh trong cùng ngữ cảnh (context / 맥락) precedence. Nếu độ đặc hiệu (specificity) bằng nhau, `@scope` có thể đưa scoping proximity vào quyết định; thứ tự nguồn (source order) là tie-breaker cuối. Vì thế kiến trúc (architecture / 아키텍처) với `@layer`, bộ chọn (selector) nhẹ và thành phần (component / 컴포넌트) ranh giới (boundary / 경계) thường bền hơn cuộc chiến độ đặc hiệu (specificity war).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **cơ chế phân tầng (cascade) trước, độ đặc hiệu (specificity) sau** xác định đầu vào; **kế thừa (inheritance) không phải “độ đặc hiệu (specificity) của parent truyền xuống con”** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình hộp (box model / 박스 모델) phải được đặt trong ngữ cảnh định dạng (formatting context / 서식 컨텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kế thừa (inheritance) không phải “độ đặc hiệu (specificity) của parent truyền xuống con”

Một `color` trên parent thường truyền xuống child vì `color` là inherited thuộc tính (property / 속성); `padding` thì không. Nếu child có quy tắc (rule / 규칙) trực tiếp mục tiêu (target / 대상) nó, direct giá trị (value / 값) thắng inherited giá trị (value / 값) bất kể bộ chọn (selector) của parent mạnh đến đâu. Khi gỡ lỗi (debug / 디버그) typography, custom thuộc tính (property / 속성) hoặc theme, hãy luôn phân biệt khai báo (declaration) thắng trên chính element với giá trị (value / 값) inherited từ ancestor.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mô hình hộp (box model / 박스 모델) phải được đặt trong ngữ cảnh định dạng (formatting context / 서식 컨텍스트)** tiếp nhận điểm tựa từ **kế thừa (inheritance) không phải “độ đặc hiệu (specificity) của parent truyền xuống con”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Luồng bố cục thông thường (normal flow / 일반 흐름) là đường cơ sở (baseline) của positioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình hộp (box model / 박스 모델) phải được đặt trong ngữ cảnh định dạng (formatting context / 서식 컨텍스트)

`content`, `padding`, `border`, `margin` chỉ mô tả box. Cách box được đặt phụ thuộc ngữ cảnh định dạng (formatting context / 서식 컨텍스트). ngữ cảnh định dạng khối (block formatting context) có rules về khối (block / 블록) luồng (flow / 흐름), floats và margin tương tác (interaction / 상호작용); ngữ cảnh định dạng nội dòng (inline formatting context) tạo các hộp dòng (line boxes) và đường cơ sở (baseline); Flexbox/Grid chạy sizing/placement thuật toán (algorithm / 알고리즘) riêng. Đây là lý do cùng `width`, `margin:auto` hay alignment thuộc tính (property / 속성) có thể hành xử khác ở các ngữ cảnh (context / 맥락) khác nhau.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mô hình hộp (box model / 박스 모델) phải được đặt trong ngữ cảnh định dạng (formatting context / 서식 컨텍스트)** xác định đầu vào; **Luồng bố cục thông thường (normal flow / 일반 흐름) là đường cơ sở (baseline) của positioning** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Responsive chỉ đổi điều kiện; bộ máy bố cục (layout engine) vẫn là CSS bố cục (layout / 레이아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng bố cục thông thường (normal flow / 일반 흐름) là đường cơ sở (baseline) của positioning

Trước `absolute`, `fixed`, `sticky`, cần hiểu luồng bố cục thông thường (normal flow / 일반 흐름). `position: relative` vẫn giữ slot trong luồng (flow / 흐름) rồi offset visual box. `absolute` rời luồng bố cục thông thường (normal flow / 일반 흐름) và tìm khối chứa tham chiếu (containing block / 컨테이닝 블록). `fixed` thường liên hệ vùng nhìn (viewport)/top-level containing ngữ cảnh (context / 맥락). `sticky` vẫn tham gia luồng (flow / 흐름) nhưng bị ràng buộc bởi vùng chứa cuộn (scroll container), inset và scroll phạm vi (range / 범위). Khi positioning sai, câu hỏi đúng là “khối chứa tham chiếu (containing block / 컨테이닝 블록)/vùng chứa cuộn (scroll container) là ai?” trước khi hỏi “top bao nhiêu px?”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Luồng bố cục thông thường (normal flow / 일반 흐름) là đường cơ sở (baseline) của positioning** xác định đầu vào; **Responsive chỉ đổi điều kiện; bộ máy bố cục (layout engine) vẫn là CSS bố cục (layout / 레이아웃)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Rendering/hiệu năng (performance / 성능) là phần cuối của cùng mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Responsive chỉ đổi điều kiện; bộ máy bố cục (layout engine) vẫn là CSS bố cục (layout / 레이아웃)

truy vấn môi trường (media query) bật/tắt các khai báo (declarations) theo vùng nhìn (viewport), đầu vào (input / 입력) năng lực (capability / 역량), motion preference hoặc color scheme. truy vấn vùng chứa (container query) làm điều tương tự nhưng truy vấn (query / 쿼리) bộ chứa (container / 컨테이너) thay vì vùng nhìn (viewport). Bên trong điều kiện đó, bố cục (layout / 레이아웃) vẫn do luồng bố cục thông thường (normal flow / 일반 흐름), Flexbox, Grid và sizing algorithms thực thi. Responsive tốt thường bắt đầu bằng fluid/intrinsic các ràng buộc (constraints / 제약조건들), rồi điểm ngắt (breakpoint) chỉ xuất hiện ở nơi hành vi (behavior / 동작) thực sự cần đổi.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Rendering/hiệu năng (performance / 성능) là phần cuối của cùng mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Responsive chỉ đổi điều kiện; bộ máy bố cục (layout engine) vẫn là CSS bố cục (layout / 레이아웃)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Thứ tự ưu tiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rendering/hiệu năng (performance / 성능) là phần cuối của cùng mô hình tư duy (mental model / 사고 모델)

Sau bố cục (layout / 레이아웃), trình duyệt (browser / 브라우저) paint văn bản (text / 텍스트), background, border, shadow/effects rồi composite. Thay đổi hình học (geometry / 기하학) như `width` hoặc font metrics có thể kéo theo style/bố cục (layout / 레이아웃)/paint; `transform` và `opacity` thường thuận lợi hơn cho compositor animation nhưng không miễn phí. Blur/backdrop-filter lớn, quá nhiều các lớp tổng hợp (compositing layers) hoặc `will-change` bừa bãi có thể tăng bộ nhớ (memory / 메모리)/kết xuất (render / 렌더링) chi phí (cost / 비용). hiệu năng (performance / 성능) phải được đo theo chuỗi xử lý kết xuất (rendering pipeline), không tối ưu bằng mẹo truyền miệng.

Khi gỡ lỗi (debug / 디버그) môi trường vận hành (production / 운영 환경), dấu vết (trace / 추적) chuẩn là: bộ chọn (selector) match → khai báo (declaration) valid → cơ chế phân tầng (cascade)/tầng (layer / 계층)/độ đặc hiệu (specificity) → computed giá trị (value / 값) → kế thừa (inheritance)/defaulting → ngữ cảnh định dạng (formatting context / 서식 컨텍스트)/khối chứa tham chiếu (containing block / 컨테이닝 블록) → intrinsic/min/max/overflow → stacking/paint/composite. Đây là xương sống nối mọi chapter còn lại.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Thứ tự ưu tiên** gom các mảnh từ **Rendering/hiệu năng (performance / 성능) là phần cuối của cùng mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델) quan trọng nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ tự ưu tiên

1. **cú pháp (syntax / 문법) → bộ chọn (selector) → cơ chế phân tầng (cascade) → độ đặc hiệu (specificity) → kế thừa (inheritance)**
2. **mô hình hộp (box model / 박스 모델) → Sizing → luồng bố cục thông thường (normal flow / 일반 흐름) → Display**
3. **Position → khối chứa tham chiếu (containing block / 컨테이닝 블록) → ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) → z-index**
4. **Typography → Color → Background → Border**
5. **Flexbox**
6. **Grid**
7. **thiết kế đáp ứng (responsive design) → truy vấn môi trường (media query) → truy vấn vùng chứa (container query)**
8. **Transform → chuyển tiếp (transition / 전이) → Animation**
9. **Custom các thuộc tính (properties) → đơn vị từ (token / 토큰) thiết kế (design tokens)**
10. **kiến trúc (architecture / 아키텍처) → khả năng tiếp cận (accessibility / 접근성) → hiệu năng (performance / 성능) → gỡ lỗi (debugging)**
11. **CSS hiện đại:** lồng cú pháp (nesting), các lớp phân tầng (cascade layers), `@scope`, `:has()`, Subgrid, định vị theo điểm neo (anchor positioning), hoạt ảnh điều khiển bằng cuộn (scroll-driven animations), chuyển cảnh giao diện (view transitions), `@property`, hiện đại (modern / 현대적) color.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mô hình tư duy (mental model / 사고 모델) quan trọng nhất** gom các mảnh từ **Thứ tự ưu tiên** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **1.1 quy tắc (rule / 규칙) cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델) quan trọng nhất

Khi CSS "không chạy", đừng thử thêm `!important` ngay. Kiểm tra theo thứ tự:

```text
Selector có match không?
→ Declaration có valid không?
→ Cascade chọn declaration nào?
→ Specificity/source order/layer ra sao?
→ Property có inherit không?
→ Element đang ở formatting context nào?
→ Containing block là ai?
→ Kích thước available/intrinsic là bao nhiêu?
→ Có overflow/stacking context/transform nào ảnh hưởng không?
```

Đây là khác biệt lớn giữa người "biết CSS" và người gỡ lỗi (debug / 디버그) CSS nhanh.

---

# 1. CSS cú pháp (syntax / 문법) & cách trình duyệt (browser / 브라우저) áp dụng CSS [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **1.1 quy tắc (rule / 규칙) cơ bản** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델) quan trọng nhất** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **1.2 Cách đưa CSS vào HTML** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1.1 quy tắc (rule / 규칙) cơ bản

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card {
  color: #222;
  padding: 16px;
}
```

- `.card`: bộ chọn (selector).
- `color`, `padding`: thuộc tính (property / 속성).
- `#222`, `16px`: giá trị (value / 값).
- `color: #222`: khai báo (declaration).
- Toàn bộ `{ ... }`: khai báo (declaration) khối (block / 블록).

Nếu một khai báo (declaration) sai, trình duyệt (browser / 브라우저) thường bỏ khai báo (declaration) đó:

```css
.card {
  color: red;
  padding: abc; /* invalid → ignored */
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **1.2 Cách đưa CSS vào HTML** tiếp nhận điểm tựa từ **1.1 quy tắc (rule / 규칙) cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1.3 Comment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1.2 Cách đưa CSS vào HTML

### Bên ngoài (external / 외부) biểu định kiểu (stylesheet / 스타일시트) — nên dùng môi trường vận hành (production / 운영 환경)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```html
<link rel="stylesheet" href="/styles/app.css">
```

### Nội bộ (internal / 내부) CSS

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```html
<style>
  body { margin: 0; }
</style>
```

### Inline style

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```html
<div style="color: red">...</div>
```

Inline style có độ đặc hiệu (specificity) cao và khó maintain. Chỉ nên dùng khi:
- style được generate động thực sự,
- email HTML,
- khung phần mềm (framework / 프레임워크)/thời gian chạy (runtime / 런타임) buộc phải dùng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **1.3 Comment** tiếp nhận điểm tựa từ **1.2 Cách đưa CSS vào HTML** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1.4 Shorthand và longhand** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1.3 Comment

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
/* Comment */
```

CSS không hỗ trợ `//` như JavaScript/SCSS.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **1.4 Shorthand và longhand** tiếp nhận điểm tựa từ **1.3 Comment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — các bộ chọn (selectors)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1.4 Shorthand và longhand

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
margin: 10px 20px;
```

tương đương:

```css
margin-top: 10px;
margin-right: 20px;
margin-bottom: 10px;
margin-left: 20px;
```

### Quy tắc 1–4 giá trị

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
margin: 10px;             /* all */
margin: 10px 20px;        /* top/bottom | left/right */
margin: 10px 20px 30px;   /* top | left/right | bottom */
margin: 10px 20px 30px 40px; /* top | right | bottom | left */
```

⚠ Shorthand có thể reset longhand mà bạn không để ý:

```css
.box {
  background-color: red;
  background: url(bg.png); /* background-color cũng bị reset */
}
```

**cấp cao (senior / 시니어) ghi chú (note / 노트):** với thành phần (component / 컴포넌트) phức tạp, dùng shorthand khi bạn thực sự muốn set/reset cả nhóm.

---

# 2. các bộ chọn (selectors) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — các bộ chọn (selectors)** tiếp nhận điểm tựa từ **1.4 Shorthand và longhand** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Descendant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — các bộ chọn (selectors)

### CSS Idiom — trạng thái (state / 상태) bằng attribute thay vì lớp (class / 클래스) tạm

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.tabs [aria-selected="true"] {
  font-weight: 700;
}

.menu[data-state="open"] {
  opacity: 1;
}
```

Ưu điểm:
- trạng thái (state / 상태) gần với ngữ nghĩa (semantics / 의미론) hơn,
- JS không cần maintain thêm nhiều lớp (class / 클래스),
- DevTools đọc trạng thái (state / 상태) rõ.

### Mẫu lập trình (coding pattern / 코딩 패턴) — Low-specificity thành phần (component / 컴포넌트) các bộ chọn (selectors)

Ưu tiên:

```css
.card {}
.card-title {}
.card-actions {}
```

thay vì:

```css
.page main section .card > header > h3 {}
```

Mẫu (pattern / 패턴) này giảm coupling với DOM.

### Mẫu thiết kế (design pattern / 디자인 패턴) — bộ chọn (selector) as API

Hãy coi bộ chọn (selector) như giao diện công khai (public API).

Nếu CSS viết:

```css
.profile-card > div:nth-child(2) > span {}
```

thì DOM cấu trúc (structure / 구조) trở thành API ngầm và rất brittle.

Nếu viết:

```css
.profile-card__name {}
```

hoặc:

```css
.profile-card [data-slot="name"] {}
```

thì đặc tả hợp đồng (contract / 계약) rõ hơn.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

bộ chọn (selector) tốt thường:
- đủ cụ thể để không leak,
- đủ yếu để override,
- không encode quá nhiều DOM cấu trúc (structure / 구조),
- phản ánh role/trạng thái (state / 상태) thay vì vị trí ngẫu nhiên.

# 2.1 Universal bộ chọn (selector)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
* {
  box-sizing: border-box;
}
```

`*` match mọi element.

Thường dùng trong reset:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

# 2.2 kiểu (type / 타입) bộ chọn (selector)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
button {}
p {}
article {}
```

độ đặc hiệu (specificity) thấp, phù hợp cơ sở (base / 기반) styles.

# 2.3 lớp (class / 클래스) bộ chọn (selector)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.card {}
.btn-primary {}
```

Đây nên là bộ chọn (selector) chính trong thành phần (component / 컴포넌트) CSS.

# 2.4 ID bộ chọn (selector)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
#header {}

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
```

ID có độ đặc hiệu (specificity) rất cao.

**cấp cao (senior / 시니어) quy tắc (rule / 규칙):** tránh dùng ID cho styling reusable.

# 2.5 Attribute các bộ chọn (selectors)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
input[type="text"] {}
button[disabled] {}
[data-state="open"] {}
```

Các operator:

```css
[attr]          /* tồn tại */
[attr="value"]  /* bằng chính xác */
[attr~="value"] /* word trong danh sách space-separated */
[attr|="en"]    /* en hoặc en-* */
[attr^="abc"]   /* bắt đầu bằng */
[attr$=".pdf"]  /* kết thúc bằng */
[attr*="foo"]   /* chứa substring */
```

Case-insensitive:

```css
a[href$=".PDF" i] {}
```

**Thực tế:** trạng thái (state / 상태) styling rất tốt với `data-*`.

```css
.menu[data-state="open"] {
  opacity: 1;
}
```

---

# 3. Combinators [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Descendant** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — các bộ chọn (selectors)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Child >** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Descendant

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card p {}
```

Match `p` ở bất kỳ độ sâu (depth / 깊이) nào trong `.card`.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Child >** tiếp nhận điểm tựa từ **Descendant** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adjacent sibling +** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Child `>`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card > p {}
```

Chỉ match con trực tiếp.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Adjacent sibling +** tiếp nhận điểm tựa từ **Child >** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **General sibling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adjacent sibling `+`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
label + input {}
```

Match `input` ngay sau `label`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **General sibling** tiếp nhận điểm tựa từ **Adjacent sibling +** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4.1 tương tác (interaction / 상호작용) các trạng thái (states)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## General sibling `~`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
h2 ~ p {}
```

Match các `p` cùng parent đứng sau `h2`.

**cấp cao (senior / 시니어) ghi chú (note / 노트):** bộ chọn (selector) càng phụ thuộc sâu vào DOM càng fragile.

Không nên:

```css
.page .main .content .card .header span {}
```

Nên:

```css
.card-title {}
```

---

# 4. các lớp giả (pseudo-classes) [cốt lõi (core / 핵심) → ADV]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4.1 tương tác (interaction / 상호작용) các trạng thái (states)** tiếp nhận điểm tựa từ **General sibling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4.2 Form các trạng thái (states)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4.1 tương tác (interaction / 상호작용) các trạng thái (states)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
a:hover {}
button:active {}
input:focus {}
input:focus-visible {}
```

### `:focus` vs `:focus-visible`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- `:focus`: element đang focus.
- `:focus-visible`: trình duyệt (browser / 브라우저) xác định cần hiện chỉ báo tiêu điểm (focus indicator), thường khi keyboard điều hướng (navigation / 내비게이션).

Môi trường vận hành (production / 운영 환경):

```css
.button:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

Không nên:

```css
*:focus {
  outline: none;
}
```

vì phá keyboard khả năng tiếp cận (accessibility / 접근성).

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4.2 Form các trạng thái (states)** tiếp nhận điểm tựa từ **4.1 tương tác (interaction / 상호작용) các trạng thái (states)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4.3 Structural các bộ chọn (selectors)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4.2 Form các trạng thái (states)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
input:checked {}
input:disabled {}
input:enabled {}
input:required {}
input:optional {}
input:valid {}
input:invalid {}
input:placeholder-shown {}
input:read-only {}
```

Ví dụ:

```css
input:invalid:not(:placeholder-shown) {
  border-color: crimson;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4.3 Structural các bộ chọn (selectors)** tiếp nhận điểm tựa từ **4.2 Form các trạng thái (states)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4.4 :not()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4.3 Structural các bộ chọn (selectors)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
:first-child
:last-child
:only-child
:first-of-type
:last-of-type
:nth-child(...)
:nth-of-type(...)
```

Ví dụ:

```css
tr:nth-child(even) {
  background: #f7f7f7;
}

.item:nth-child(3n + 1) {}
```

Công thức `an+b`:

```text
2n      → phần tử chẵn
2n+1    → phần tử lẻ
3n      → 3, 6, 9...
-n+3    → 3 phần tử đầu
n+4     → từ phần tử 4 trở đi
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4.4 :not()** tiếp nhận điểm tựa từ **4.3 Structural các bộ chọn (selectors)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4.5 :is() [ADV]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4.4 `:not()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
button:not([disabled]) {}
```

Có thể nhận bộ chọn (selector) danh sách (list / 목록):

```css
input:not([type="checkbox"], [type="radio"]) {}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4.5 :is() [ADV]** tiếp nhận điểm tựa từ **4.4 :not()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4.6 :where() [ADV]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4.5 `:is()` [ADV]

Gom bộ chọn (selector):

```css
:is(h1, h2, h3) {
  line-height: 1.2;
}
```

Thay cho:

```css
h1, h2, h3 {}
```

Hữu ích với bộ chọn (selector) dài:

```css
.article :is(h2, h3, h4) {}
```

độ đặc hiệu (specificity) của `:is()` lấy độ đặc hiệu (specificity) cao nhất trong arguments.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4.6 :where() [ADV]** tiếp nhận điểm tựa từ **4.5 :is() [ADV]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4.7 :has() [ADV/hiện đại (modern / 현대적)]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4.6 `:where()` [ADV]

Cú pháp (syntax / 문법) tương tự `:is()` nhưng **độ đặc hiệu (specificity) = 0**.

```css
:where(.content) h2 {
  margin-block-start: 2rem;
}
```

Rất hữu ích khi xây cơ sở (base / 기반)/theme dễ override.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4.7 :has() [ADV/hiện đại (modern / 현대적)]** tiếp nhận điểm tựa từ **4.6 :where() [ADV]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **::before / ::after** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4.7 `:has()` [ADV/hiện đại (modern / 현대적)]

bộ chọn (selector) "parent-aware":

```css
.card:has(img) {
  padding-top: 0;
}
```

Form group có đầu vào (input / 입력) invalid:

```css
.field:has(input:invalid) .error {
  display: block;
}
```

Checkbox điều khiển (control / 제어) parent:

```css
.row:has(input:checked) {
  background: #eef6ff;
}
```

**cấp cao (senior / 시니어) ghi chú (note / 노트):** `:has()` giảm nhu cầu thêm lớp (class / 클래스)/trạng thái (state / 상태) bằng JavaScript cho nhiều UI trạng thái (state / 상태) đơn giản.

---

# 5. các phần tử giả (pseudo-elements) [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
::before
::after
::first-letter
::first-line
::selection
::marker
::placeholder
::file-selector-button
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **::before / ::after** tiếp nhận điểm tựa từ **4.7 :has() [ADV/hiện đại (modern / 현대적)]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **::marker** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `::before` / `::after`

Cần `content`:

```css
.badge::before {
  content: "NEW";
}
```

Decoration:

```css
.link::after {
  content: "";
  display: inline-block;
  width: 0.5em;
  height: 0.5em;
}
```

Không dùng phần tử giả (pseudo-element) cho content quan trọng về ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **::marker** tiếp nhận điểm tựa từ **::before / ::after** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **::selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `::marker`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
li::marker {
  color: tomato;
  font-weight: 700;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **::selection** tiếp nhận điểm tựa từ **::marker** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — cơ chế phân tầng (cascade)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `::selection`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
::selection {
  background: gold;
  color: black;
}
```

---

# 6. cơ chế phân tầng (cascade) — nền tảng sống còn của CSS [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **::selection** xác định đầu vào; **Mẫu (pattern / 패턴) notes — cơ chế phân tầng (cascade)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6.1 độ đặc hiệu (specificity)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — cơ chế phân tầng (cascade)

### CSS Idiom — Win by kiến trúc (architecture / 아키텍처), not by độ đặc hiệu (specificity)

Không sửa kiểu:

```css
.page .dialog .button.primary {
  color: white !important;
}
```

nếu có thể sửa kiến trúc:

```css
@layer base, components, utilities;

@layer components {
  .button[data-variant="primary"] {
    color: white;
  }
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Default → biến thể (variant) → trạng thái (state / 상태)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.button {
  /* default */
}

.button[data-variant="danger"] {
  /* variant */
}

.button:hover {
  /* interaction state */
}

.button:disabled {
  /* disabled state */
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Layered cơ chế phân tầng (cascade)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
reset
→ tokens
→ base
→ layout
→ components
→ utilities
→ overrides
```

Mục tiêu:
- override predictable,
- không cuộc chiến độ đặc hiệu (specificity war),
- vendor CSS có chỗ riêng,
- thành phần (component / 컴포넌트) CSS dễ reason.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Nếu phải hỏi "bộ chọn (selector) nào mạnh hơn" quá thường xuyên, vấn đề thường nằm ở kiến trúc (architecture / 아키텍처) chứ không phải thiếu kiến thức độ đặc hiệu (specificity).

cơ chế phân tầng (cascade) quyết định khai báo (declaration) nào thắng.

Các yếu tố chính:

1. nguồn và mức quan trọng (origin/importance).
2. lớp phân tầng (cascade layer).
3. độ đặc hiệu (specificity).
4. độ gần phạm vi (scope proximity) trong scoped CSS.
5. thứ tự nguồn (source order).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — cơ chế phân tầng (cascade)** xác định đầu vào; **6.1 độ đặc hiệu (specificity)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6.2 thứ tự nguồn (source order)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.1 độ đặc hiệu (specificity)

Có thể tư duy gần đúng:

```text
Inline      → 1-0-0-0
ID          → 0-1-0-0
Class,
attribute,
pseudo-class → 0-0-1-0
Element,
pseudo-element → 0-0-0-1
```

Ví dụ:

```css
#app .card p {}

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
```

cao hơn:

```css
.card p {}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **6.1 độ đặc hiệu (specificity)** nêu điều cần giải thích; **6.2 thứ tự nguồn (source order)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6.3 !important** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.2 thứ tự nguồn (source order)

Nếu độ đặc hiệu (specificity) bằng nhau, quy tắc (rule / 규칙) viết sau thắng:

```css
.btn { color: blue; }
.btn { color: red; } /* thắng */
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **6.2 thứ tự nguồn (source order)** nêu điều cần giải thích; **6.3 !important** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6.4 toàn cục (global / 전역) keywords** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.3 `!important`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
color: red !important;
```

Không nên dùng như cách fix mặc định.

Chỉ hợp lý khi:
- tiện ích (utility) API có chủ đích,
- override bên ngoài (external / 외부) styles khó kiểm soát,
- khả năng tiếp cận (accessibility / 접근성)/người dùng (user / 사용자) override đặc biệt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **6.4 toàn cục (global / 전역) keywords** tiếp nhận điểm tựa từ **6.3 !important** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Absolute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.4 toàn cục (global / 전역) keywords

Các thuộc tính (property / 속성) thường chấp nhận:

```css
inherit
initial
unset
revert
revert-layer
```

### `inherit`

Ép lấy computed giá trị (value / 값) từ parent.

```css
button {
  font: inherit;
}
```

### `initial`

Về initial giá trị (value / 값) theo specification.

### `unset`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- thuộc tính (property) có inherit → behave như `inherit`;
- không inherit → behave như `initial`.

### `revert`

Quay về style của cơ chế phân tầng (cascade) origin trước.

### `revert-layer`

Bỏ khai báo (declaration) trong lớp phân tầng (cascade layer) hiện tại để quay về tầng (layer / 계층) thấp hơn.

---

# 7. các lớp phân tầng (cascade layers) `@layer` [ADV/hiện đại (modern / 현대적)]

Dùng để quản lý precedence theo kiến trúc thay vì cuộc chiến độ đặc hiệu (specificity war).

```css
@layer reset, base, components, utilities;

@layer reset {
  * { box-sizing: border-box; }
}

@layer base {
  body { font-family: system-ui; }
}

@layer components {
  .button { padding: 0.75rem 1rem; }
}

@layer utilities {
  .hidden { display: none; }
}
```

Tầng (layer / 계층) khai báo sau trong thứ tự (order / 순서) có precedence cao hơn trong normal các khai báo (declarations).

**cấp cao (senior / 시니어) kiến trúc (architecture / 아키텍처):**

```text
reset
tokens
base
layout
components
utilities
overrides
```

Ưu điểm:
- giảm `!important`,
- CSS từ vendor dễ kiểm soát,
- predictable override.

---

# 8. kế thừa (inheritance) [cốt lõi (core / 핵심)]

Một số thuộc tính (property / 속성) inherit mặc định:

```text
color
font-family
font-size
font-style
font-weight
line-height
text-align
visibility
cursor
```

Nhiều thuộc tính (property / 속성) bố cục (layout / 레이아웃) không inherit:

```text
margin
padding
border
width
height
display
position
```

Ví dụ:

```css
body {
  color: #222;
  font-family: system-ui;
}
```

Con thường tự kế thừa.

---

# 9. các giá trị (values) & Units [cốt lõi (core / 핵심)]

# 9.1 Length units

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Absolute** tiếp nhận điểm tựa từ **6.4 toàn cục (global / 전역) keywords** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Font-relative** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Absolute

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
px
cm
mm
in
pt
pc
```

Web UI gần như chủ yếu dùng `px`.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Font-relative** tiếp nhận điểm tựa từ **Absolute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **vùng nhìn (viewport) units** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Font-relative

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
em   → dựa trên font-size hiện tại/parent tùy property
rem  → dựa trên root font-size
ch   → width gần bằng ký tự "0"
ex   → x-height
lh   → line-height hiện tại
rlh  → root line-height
```

### `rem`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card {
  padding: 1rem;
}
```

Tốt cho spacing/kiểu (type / 타입) quy mô (scale / 규모) toàn app.

### `em`

Hữu ích khi thành phần (component / 컴포넌트) cần quy mô (scale / 규모) theo font:

```css
.icon {
  width: 1em;
  height: 1em;
}
```

⚠ nested `em` cho `font-size` có thể compound.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **vùng nhìn (viewport) units** tiếp nhận điểm tựa từ **Font-relative** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **truy vấn vùng chứa (container query) units** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## vùng nhìn (viewport) units

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
vw, vh
vmin, vmax
svw, svh
lvw, lvh
dvw, dvh
```

- `svh`: small vùng nhìn (viewport).
- `lvh`: large vùng nhìn (viewport).
- `dvh`: động (dynamic / 동적) vùng nhìn (viewport).

Mobile full-screen:

```css
.page {
  min-height: 100dvh;
}
```

Thường tốt hơn `100vh` trên mobile trình duyệt (browser / 브라우저) có thanh address thay đổi kích thước.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **truy vấn vùng chứa (container query) units** tiếp nhận điểm tựa từ **vùng nhìn (viewport) units** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **calc()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## truy vấn vùng chứa (container query) units

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
cqw, cqh
cqi, cqb
cqmin, cqmax
```

Ví dụ:

```css
.card-title {
  font-size: clamp(1rem, 5cqi, 2rem);
}
```

---

# 10. Percentages

Ý nghĩa `%` phụ thuộc thuộc tính (property / 속성).

```css
width: 50%;
```

thường dựa vào khối chứa tham chiếu (containing block / 컨테이닝 블록) width.

Classic pitfall:

```css
padding-top: 10%;
```

Percentage padding truyền thống resolve theo inline kích thước (size / 크기) của khối chứa tham chiếu (containing block / 컨테이닝 블록), không nhất thiết theo height.

---

# 11. CSS Math các hàm (functions) [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **calc()** tiếp nhận điểm tựa từ **truy vấn vùng chứa (container query) units** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **min()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `calc()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
width: calc(100% - 2rem);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **min()** tiếp nhận điểm tựa từ **calc()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **max()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `min()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
width: min(100%, 70rem);
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **max()** tiếp nhận điểm tựa từ **min()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **clamp(min, preferred, max)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `max()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
padding-inline: max(1rem, 5vw);
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **clamp(min, preferred, max)** tiếp nhận điểm tựa từ **max()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Custom các thuộc tính (properties)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `clamp(min, preferred, max)`

Responsive typography:

```css
font-size: clamp(1.5rem, 1rem + 2vw, 3rem);
```

Rất hữu ích cho:
- font-size,
- spacing,
- width,
- gap.

---

# 12. Custom các thuộc tính (properties) / CSS các biến (variables) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Custom các thuộc tính (properties)** tiếp nhận điểm tựa từ **clamp(min, preferred, max)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Custom thuộc tính (property / 속성) có cơ chế phân tầng (cascade) + inherit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Custom các thuộc tính (properties)

### CSS Idiom — phương án dự phòng (fallback) đơn vị từ (token / 토큰)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card {
  color: var(--card-color, var(--color-text));
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — đơn vị từ (token / 토큰) chuỗi xử lý (pipeline / 파이프라인)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
:root {
  --blue-600: #2563eb;
  --color-action: var(--blue-600);
}

.button {
  --button-bg: var(--color-action);
  background: var(--button-bg);
}
```

Chuỗi xử lý (pipeline / 파이프라인):

```text
Primitive token
→ Semantic token
→ Component token
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Theme by đơn vị từ (token / 토큰) override

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
:root {
  --surface: #fff;
  --text: #111;
}

[data-theme="dark"] {
  --surface: #111;
  --text: #f5f5f5;
}
```

Thành phần (component / 컴포넌트) không cần biết dark/light:

```css
.card {
  background: var(--surface);
  color: var(--text);
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Custom thuộc tính (property / 속성) mạnh nhất khi dùng như **thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약)**, không chỉ thay literal giá trị (value / 값).

```css
:root {
  --color-primary: #2563eb;
  --space-4: 1rem;
}

.button {
  background: var(--color-primary);
  padding: var(--space-4);
}
```

phương án dự phòng (fallback):

```css
color: var(--text-color, #222);
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Custom các thuộc tính (properties)** xác định đầu vào; **Custom thuộc tính (property / 속성) có cơ chế phân tầng (cascade) + inherit** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **giao diện thành phần (component API)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Custom thuộc tính (property / 속성) có cơ chế phân tầng (cascade) + inherit

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.theme-dark {
  --surface: #111;
  --text: #fff;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Custom thuộc tính (property / 속성) có cơ chế phân tầng (cascade) + inherit** xác định đầu vào; **giao diện thành phần (component API)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mẫu (pattern / 패턴) notes — mô hình hộp (box model / 박스 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## giao diện thành phần (component API)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.avatar {
  width: var(--avatar-size, 3rem);
  height: var(--avatar-size, 3rem);
}
```

Bên tiêu thụ (consumer / 소비자):

```css
.profile-avatar {
  --avatar-size: 5rem;
}
```

**cấp cao (senior / 시니어) ghi chú (note / 노트):** custom các thuộc tính (properties) nên là **đơn vị từ (token / 토큰) thiết kế (design tokens) + thành phần (component / 컴포넌트) tokens**, không chỉ là biến thay văn bản (text / 텍스트).

---

# 13. `@property` [ADV/hiện đại (modern / 현대적)]

Khai báo kiểu cho custom thuộc tính (property / 속성):

```css
@property --progress {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}
```

Sau đó có thể animate typed giá trị (value / 값):

```css
.loader {
  --progress: 0%;
  transition: --progress 300ms;
}

.loader.done {
  --progress: 100%;
}
```

Descriptors:
- `syntax`: kiểu dữ liệu, ví dụ `<length>`, `<number>`, `<color>`, `<angle>`.
- `inherits`: `true | false`.
- `initial-value`: giá trị mặc định.

---

# 14. mô hình hộp (box model / 박스 모델) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — mô hình hộp (box model / 박스 모델)** tiếp nhận điểm tựa từ **giao diện thành phần (component API)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **box-sizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — mô hình hộp (box model / 박스 모델)

### CSS Idiom — Universal border-box

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Section + inner wrapper

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.section {
  padding-block: 4rem;
}

.section__inner {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

Tách responsibility:
- outer section: vertical rhythm/background,
- inner wrapper: horizontal ràng buộc (constraint / 제약조건).

### Mẫu thiết kế (design pattern / 디자인 패턴) — Box responsibility

Một box nên có responsibility rõ:

```text
outer box → positioning/layout
middle box → spacing/border/background
inner box → content flow
```

Không phải lúc nào cũng cần nhiều wrapper; đây là mô hình tư duy (mental model / 사고 모델) để gỡ lỗi (debug / 디버그).

Một box gồm:

```text
content
padding
border
margin
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **box-sizing** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — mô hình hộp (box model / 박스 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Sizing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `box-sizing`

### `content-box`

Default truyền thống:

```css
width: 200px;
padding: 20px;
border: 2px solid;
```

Rendered width = 244px.

### `border-box`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
box-sizing: border-box;
```

`width` đã bao gồm padding + border.

Toàn cục (global / 전역) best practice:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

---

# 15. Width / Height / Sizing [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Sizing** tiếp nhận điểm tựa từ **box-sizing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) các giá trị (values)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Sizing

### CSS Idiom — Fluid + capped width

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
width: min(100%, 42rem);
```

### CSS Idiom — Prevent intrinsic overflow

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
min-width: 0;
min-height: 0;
```

Đặc biệt quan trọng trong Flex/Grid.

### Mẫu lập trình (coding pattern / 코딩 패턴) — Intrinsic card width

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.card {
  inline-size: fit-content;
  max-inline-size: 100%;
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Constraint-based bố cục (layout / 레이아웃)

Cấp cao (senior / 시니어) thường không chỉ "set kích thước (size / 크기)" mà định nghĩa các ràng buộc (constraints / 제약조건들):

```text
minimum
preferred
maximum
available space
intrinsic content size
```

Ví dụ:

```css
width: clamp(16rem, 40vw, 32rem);
```

```css
width
height
min-width
min-height
max-width
max-height
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Dùng chung (common / 공통) các giá trị (values)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Sizing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **aspect-ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) các giá trị (values)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
width: auto;
width: 100%;
width: 20rem;
width: min-content;
width: max-content;
width: fit-content;
width: fit-content(30rem);
```

### `min-content`

Kích thước nhỏ nhất content có thể co mà không overflow theo intrinsic rules.

### `max-content`

Kích thước content muốn có nếu không wrap.

### `fit-content`

Co giãn giữa min-content và max-content theo không gian khả dụng (available space).

Thực tế:

```css
.tag {
  width: fit-content;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **aspect-ratio** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) các giá trị (values)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **gộp lề (margin collapsing) [ADV]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `aspect-ratio`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.video {
  aspect-ratio: 16 / 9;
}
```

Avatar:

```css
.avatar {
  width: 4rem;
  aspect-ratio: 1;
}
```

---

# 16. Margin [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
margin-top
margin-right
margin-bottom
margin-left
margin
```

Center khối (block / 블록) có width:

```css
.container {
  width: min(100% - 2rem, 70rem);
  margin-inline: auto;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **gộp lề (margin collapsing) [ADV]** tiếp nhận điểm tựa từ **aspect-ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — ngữ cảnh định dạng (formatting context / 서식 컨텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## gộp lề (margin collapsing) [ADV]

Vertical margins của normal-flow khối (block / 블록) có thể collapse.

```css
h2 { margin-bottom: 20px; }
p  { margin-top: 30px; }
```

Khoảng cách không nhất thiết 50px; có thể collapse thành 30px.

Không collapse trong nhiều trường hợp như:
- flex/grid bố cục (layout / 레이아웃),
- padding/border tách parent-child,
- ngữ cảnh định dạng khối (block formatting context) khác.

**cấp cao (senior / 시니어) ghi chú (note / 노트):** dùng `gap` cho bố cục (layout / 레이아웃) giữa các item thường predictable hơn margin choreography.

---

# 17. Padding [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
padding
padding-top
padding-right
padding-bottom
padding-left
```

Không nhận negative giá trị (value / 값).

---

# 18. Borders [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
border
border-width
border-style
border-color
border-radius
```

Style:

```text
none
solid
dashed
dotted
double
groove
ridge
inset
outset
```

Radius:

```css
border-radius: 12px;
border-radius: 50%;
```

Pill:

```css
border-radius: 9999px;
```

Individual corners:

```css
border-top-left-radius
border-top-right-radius
border-bottom-right-radius
border-bottom-left-radius
```

---

# 19. Outline [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
outline: 2px solid currentColor;
outline-offset: 3px;
```

Khác border:
- không chiếm bố cục (layout / 레이아웃) không gian (space / 공간),
- rất phù hợp chỉ báo tiêu điểm (focus indicator).

---

# 20. Display & ngữ cảnh định dạng (formatting context / 서식 컨텍스트) [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — ngữ cảnh định dạng (formatting context / 서식 컨텍스트)** tiếp nhận điểm tựa từ **gộp lề (margin collapsing) [ADV]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **display: block** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — ngữ cảnh định dạng (formatting context / 서식 컨텍스트)

### CSS Idiom — `flow-root` để isolate khối (block / 블록) luồng (flow / 흐름)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.component {
  display: flow-root;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — bố cục (layout / 레이아웃) primitives

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--stack-gap, 1rem);
}

.cluster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--cluster-gap, .75rem);
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Formatting-context ranh giới (boundary / 경계)

Thành phần (component / 컴포넌트) phức tạp nên chủ động tạo ranh giới (boundary / 경계) khi cần:
- `display: flow-root`,
- Flex,
- Grid,
- `contain`,
- `isolation`.

Điều này giảm tác dụng phụ (side effect) từ bên ngoài.

Thuộc tính (property / 속성):

```css
display
```

Các giá trị quan trọng:

```text
none
block
inline
inline-block
flex
inline-flex
grid
inline-grid
flow-root
contents
table
list-item
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **display: block** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — ngữ cảnh định dạng (formatting context / 서식 컨텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **display: inline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `display: block`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- thường chiếm available inline width.
- bắt đầu dòng mới.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **display: inline** tiếp nhận điểm tựa từ **display: block** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **inline-block** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `display: inline`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- flow cùng text.
- width/height không hoạt động như block.
- vertical margin/padding có behavior khác block.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **inline-block** tiếp nhận điểm tựa từ **display: inline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **display: none** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `inline-block`

Inline bên ngoài, block-like sizing bên trong.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **display: none** tiếp nhận điểm tựa từ **inline-block** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **display: flow-root [ADV]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `display: none`

Loại khỏi bố cục (layout / 레이아웃) và cây khả năng tiếp cận (accessibility tree / 접근성 트리) trong hầu hết trường hợp.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **display: none** xác định đầu vào; **display: flow-root [ADV]** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **display: contents** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `display: flow-root` [ADV]

Tạo ngữ cảnh định dạng khối (block formatting context) mới.

Useful clear float / isolate luồng (flow / 흐름):

```css
.container {
  display: flow-root;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **display: flow-root [ADV]** xác định đầu vào; **display: contents** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **visibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `display: contents`

Box của element biến mất nhưng children vẫn participate bố cục (layout / 레이아웃).

⚠ Cẩn thận khả năng tiếp cận (accessibility / 접근성)/trình duyệt (browser / 브라우저) hành vi (behavior / 동작) với ngữ nghĩa (semantics / 의미론) đặc biệt.

---

# 21. Visibility & Opacity

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **visibility** tiếp nhận điểm tựa từ **display: contents** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **opacity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `visibility`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
visibility: visible;
visibility: hidden;
```

`hidden`: giữ bố cục (layout / 레이아웃) không gian (space / 공간) nhưng không paint.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **opacity** tiếp nhận điểm tựa từ **visibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Positioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `opacity`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
opacity: 0;
opacity: 0.5;
opacity: 1;
```

`opacity: 0`:
- vẫn chiếm không gian (space / 공간),
- có thể vẫn nhận pointer/focus nếu không xử lý,
- tạo ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) khi opacity < 1.

---

# 22. luồng bố cục thông thường (normal flow / 일반 흐름) [cốt lõi (core / 핵심)]

Luồng bố cục thông thường (normal flow / 일반 흐름) gồm khối (block / 블록) luồng (flow / 흐름) + inline luồng (flow / 흐름) trước khi:
- float,
- absolute positioning,
- flex,
- grid,
- multicol
thay đổi cách bố cục (layout / 레이아웃).

Cấp cao (senior / 시니어) phải hiểu "default hành vi (behavior / 동작)" trước khi override.

---

# 23. Positioning [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Positioning** tiếp nhận điểm tựa từ **opacity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **static** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Positioning

### CSS Idiom — Full inset overlay

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.overlay {
  position: absolute;
  inset: 0;
}
```

### CSS Idiom — Center absolute element

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.centered {
  position: absolute;
  inset: 50% auto auto 50%;
  translate: -50% -50%;
}
```

Nếu chỉ cần bố cục (layout / 레이아웃) center, ưu tiên:

```css
.parent {
  display: grid;
  place-items: center;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Positioning ngữ cảnh (context / 맥락)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.card {
  position: relative;
}

.card__badge {
  position: absolute;
  inset-block-start: .5rem;
  inset-inline-end: .5rem;
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Overlay quyền sở hữu (ownership / 소유권)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
local overlay → relative + absolute
viewport overlay → fixed
scroll-affixed UI → sticky
top-layer UI → dialog/popover
```

```css
position: static;
position: relative;
position: absolute;
position: fixed;
position: sticky;
```

Offsets:

```css
top
right
bottom
left
inset
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **static** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Positioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **relative** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `static`

Default. Offset không áp dụng.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **relative** tiếp nhận điểm tựa từ **static** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **absolute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `relative`

Element vẫn giữ vị trí trong luồng bố cục thông thường (normal flow / 일반 흐름), nhưng có thể offset.

Quan trọng hơn: thường tạo khối chứa tham chiếu (containing block / 컨테이닝 블록) cho absolute child.

```css
.card {
  position: relative;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **absolute** tiếp nhận điểm tựa từ **relative** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **fixed** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `absolute`

Ra khỏi luồng bố cục thông thường (normal flow / 일반 흐름).

Position dựa vào khối chứa tham chiếu (containing block / 컨테이닝 블록) phù hợp.

Hiện đại (modern / 현대적) shorthand:

```css
inset: 0;
```

tương đương:

```css
top: 0;
right: 0;
bottom: 0;
left: 0;
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **fixed** tiếp nhận điểm tựa từ **absolute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **sticky** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `fixed`

Thường cố định theo vùng nhìn (viewport).

```css
.fab {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
}
```

⚠ ancestor có `transform`, `filter`, `perspective`... có thể thay khối chứa tham chiếu (containing block / 컨테이닝 블록) hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **sticky** tiếp nhận điểm tựa từ **fixed** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Stacking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `sticky`

Hybrid relative/fixed theo vùng chứa cuộn (scroll container).

```css
.header {
  position: sticky;
  top: 0;
}
```

Dùng chung (common / 공통) thất bại (failure / 실패):
- quên `top`,
- ancestor có overflow tạo vùng chứa cuộn (scroll container) khác,
- không đủ scroll không gian (space / 공간),
- bố cục (layout / 레이아웃) các ràng buộc (constraints / 제약조건들).

---

# 24. khối chứa tham chiếu (containing block / 컨테이닝 블록) [ADV]

Nhiều `%`, absolute offsets và sizing được tính dựa vào **khối chứa tham chiếu (containing block / 컨테이닝 블록)**.

Không phải lúc nào cũng là parent trực tiếp.

Absolute element thường tìm ancestor tạo khối chứa tham chiếu (containing block / 컨테이닝 블록), ví dụ positioned ancestor.

Gỡ lỗi (debug / 디버그) absolute/fixed lỗi phải hỏi:

> "khối chứa tham chiếu (containing block / 컨테이닝 블록) thực sự của element này là element nào?"

---

# 25. z-index & ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Stacking** tiếp nhận điểm tựa từ **sticky** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **hidden** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Stacking

### CSS Idiom — cục bộ (local / 로컬) stacking cô lập (isolation)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.component {
  isolation: isolate;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — mang tính ngữ nghĩa (semantic / 의미적) z-index quy mô (scale / 규모)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
:root {
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 500;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — tầng (layer / 계층) đặc tả hợp đồng (contract / 계약)

Không cho từng thành phần (component / 컴포넌트) tự tạo số `z-index`.

Định nghĩa mang tính ngữ nghĩa (semantic / 의미적) layers:
- content,
- sticky,
- dropdown,
- overlay,
- modal,
- toast.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Khi `z-index` lỗi, gỡ lỗi (debug / 디버그) parent ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) trước khi tăng số.

`z-index` không phải toàn cục (global / 전역) number ranking đơn giản.

```css
.modal {
  position: fixed;
  z-index: 1000;
}
```

Một ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) có thể được tạo bởi nhiều điều kiện, ví dụ:
- gốc (root / 루트) element,
- positioned element với `z-index`,
- `position: fixed/sticky`,
- `opacity < 1`,
- `transform != none`,
- `filter`,
- `isolation: isolate`,
- một số flex/phần tử Grid (grid item) có z-index,
- `contain` phù hợp.

Pitfall:

```text
child z-index: 999999
```

vẫn có thể nằm dưới element khác nếu parent ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) thấp hơn.

**cấp cao (senior / 시니어) chiến lược (strategy / 전략):** define z-index tokens:

```css
:root {
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

Không dùng random `999999`.

---

# 26. Overflow [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
overflow
overflow-x
overflow-y
```

các giá trị (values):

```text
visible
hidden
clip
scroll
auto
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **hidden** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Stacking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **clip** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `hidden`

Clip overflow và thường tạo vùng chứa cuộn (scroll container) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **clip** tiếp nhận điểm tựa từ **hidden** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **auto** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `clip`

Clip mà không cung cấp scrolling như `hidden`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **auto** tiếp nhận điểm tựa từ **clip** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **contain** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `auto`

Scrollbars khi cần.

Văn bản (text / 텍스트) single-line ellipsis:

```css
.truncate {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```

Multiline line clamp:

```css
.clamp-3 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}
```

---

# 27. `contain` & `content-visibility` [ADV]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **contain** tiếp nhận điểm tựa từ **auto** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **content-visibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `contain`

Giới hạn ảnh hưởng của subtree tới bên ngoài.

```css
.widget {
  contain: layout paint;
}
```

các giá trị (values) conceptually:
- `size`
- `inline-size`
- `layout`
- `style`
- `paint`
- combinations / `strict` / `content`

Dùng cẩn thận vì có thể thay sizing/positioning hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **content-visibility** tiếp nhận điểm tựa từ **contain** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Flexbox** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `content-visibility`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.article-section {
  content-visibility: auto;
}
```

Trình duyệt (browser / 브라우저) có thể skip rendering off-screen content.

Có thể kết hợp:

```css
contain-intrinsic-size: auto 500px;
```

để giảm bố cục (layout / 레이아웃) jump.

---

# 28. Flexbox [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Flexbox** tiếp nhận điểm tựa từ **content-visibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28.1 bộ chứa (container / 컨테이너) các thuộc tính (properties)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Flexbox

### CSS Idiom — Cluster

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
}
```

Dùng cho:
- tags,
- actions,
- navbar,
- button groups.

### CSS Idiom — Push one item to edge

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.actions {
  margin-inline-start: auto;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Media đối tượng (object / 객체)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.media {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.media__body {
  min-width: 0;
  flex: 1;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Safe flexible content

Nếu flex child chứa văn bản (text / 텍스트)/ellipsis:

```css
.content {
  min-width: 0;
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — One-dimensional composition

Flexbox phù hợp khi bố cục (layout / 레이아웃) được mô tả bằng:

```text
items in a row
hoặc
items in a column
```

Nếu cần điều khiển nhiều rows + columns đồng thời, chuyển mô hình tư duy (mental model / 사고 모델) sang Grid.

Flexbox là bố cục (layout / 레이아웃) **1 chiều**: row hoặc column.

```css
.container {
  display: flex;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **28.1 bộ chứa (container / 컨테이너) các thuộc tính (properties)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Flexbox** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **flex-grow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28.1 bộ chứa (container / 컨테이너) các thuộc tính (properties)

### `flex-direction`

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
row
row-reverse
column
column-reverse
```

```css
.toolbar {
  display: flex;
  flex-direction: row;
}
```

### `flex-wrap`

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
nowrap
wrap
wrap-reverse
```

```css
.tags {
  display: flex;
  flex-wrap: wrap;
}
```

### `flex-flow`

Shorthand:

```css
flex-flow: row wrap;
```

### `justify-content`

Align theo **trục chính (main axis)**.

Dùng chung (common / 공통) các giá trị (values):

```text
flex-start
flex-end
center
space-between
space-around
space-evenly
start
end
```

```css
.nav {
  display: flex;
  justify-content: space-between;
}
```

### `align-items`

Align items trên **trục chéo (cross axis)**.

```text
stretch
flex-start
flex-end
center
baseline
```

### `align-content`

Chỉ có ý nghĩa khi có nhiều flex lines (`wrap`) và có dư cross-axis không gian (space / 공간).

```text
stretch
flex-start
flex-end
center
space-between
space-around
space-evenly
```

### `gap`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
gap: 1rem;
row-gap: 1rem;
column-gap: 2rem;
```

Ưu tiên `gap` thay vì margin giữa child.

---

# 29. phần tử Flex (flex item) các thuộc tính (properties) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **flex-grow** tiếp nhận điểm tựa từ **28.1 bộ chứa (container / 컨테이너) các thuộc tính (properties)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **flex-shrink** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `flex-grow`

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.item {
  flex-grow: 1;
}
```

Phân chia **positive không gian dư (free space)** theo tỉ lệ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **flex-shrink** tiếp nhận điểm tựa từ **flex-grow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **flex-basis** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `flex-shrink`

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.item {
  flex-shrink: 0;
}
```

Quyết định item co khi thiếu không gian (space / 공간).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **flex-basis** tiếp nhận điểm tựa từ **flex-shrink** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **flex** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `flex-basis`

Initial main-size trước grow/shrink.

```css
.item {
  flex-basis: 20rem;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **flex** tiếp nhận điểm tựa từ **flex-basis** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **align-self** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `flex`

Shorthand:

```css
flex: 1;
```

thường behave gần:

```css
flex: 1 1 0%;
```

Các mẫu (pattern / 패턴):

```css
flex: none;       /* 0 0 auto */
flex: auto;       /* 1 1 auto */
flex: 1;          /* grow */
flex: 0 0 200px;  /* fixed basis */
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **align-self** tiếp nhận điểm tựa từ **flex** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **order** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `align-self`

Override `align-items` cho một item.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **order** tiếp nhận điểm tựa từ **align-self** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Center** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `order`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
order: 2;
```

⚠ Chỉ thay visual thứ tự (order / 순서), không nhất thiết thay DOM/read/focus thứ tự (order / 순서). Tránh dùng cho mang tính ngữ nghĩa (semantic / 의미적) reordering.

---

# 30. Flexbox Pitfall: `min-width: auto` [ADV]

phần tử Flex (flex item) mặc định có minimum kích thước (size / 크기) dựa vào content.

Do đó văn bản (text / 텍스트) dài có thể làm item không co:

```css
.row {
  display: flex;
}

.content {
  min-width: 0;
}
```

Đây là fix rất thường gặp.

Tương tự vertical flex:

```css
.content {
  min-height: 0;
  overflow: auto;
}
```

---

# 31. Flex Patterns

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Center** tiếp nhận điểm tựa từ **order** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Navbar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Center

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.center {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Navbar** tiếp nhận điểm tựa từ **Center** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Equal cards** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Navbar

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.nav {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav__actions {
  margin-inline-start: auto;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Equal cards** tiếp nhận điểm tựa từ **Navbar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Grid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Equal cards

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  flex: 1 1 18rem;
}
```

---

# 32. CSS Grid [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Grid** tiếp nhận điểm tựa từ **Equal cards** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32.1 các dải lưới (grid tracks)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Grid

### CSS Idiom — Responsive auto grid

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 1rem;
}
```

### CSS Idiom — Safe fractional nhánh học (track / 트랙)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
grid-template-columns: minmax(0, 1fr);
```

Thường an toàn hơn plain `1fr` khi child có intrinsic width lớn.

### Mẫu lập trình (coding pattern / 코딩 패턴) — Sidebar bố cục (layout / 레이아웃)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.layout {
  display: grid;
  grid-template-columns:
    minmax(12rem, 18rem)
    minmax(0, 1fr);
  gap: 2rem;
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Track-first bố cục (layout / 레이아웃)

Grid phù hợp khi cấu trúc (structure / 구조) quan trọng:

```text
sidebar | main
header
content rows
card matrix
```

Bạn thiết kế tracks trước rồi đặt content vào.

Grid là bố cục (layout / 레이아웃) **2 chiều**.

```css
.grid {
  display: grid;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **32.1 các dải lưới (grid tracks)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Grid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **fr** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32.1 các dải lưới (grid tracks)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
grid-template-columns: 1fr 1fr 1fr;
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **fr** tiếp nhận điểm tựa từ **32.1 các dải lưới (grid tracks)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **repeat()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `fr`

Fraction của available không gian dư (free space).

```css
grid-template-columns: 240px 1fr;
```

Sidebar + content.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **repeat()** tiếp nhận điểm tựa từ **fr** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **minmax()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `repeat()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
grid-template-columns: repeat(3, 1fr);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **minmax()** tiếp nhận điểm tựa từ **repeat()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Responsive grid không truy vấn môi trường (media query)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `minmax()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
grid-template-columns: repeat(3, minmax(0, 1fr));
```

`minmax(0, 1fr)` thường chống intrinsic overflow tốt hơn plain `1fr`.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Responsive grid không truy vấn môi trường (media query)** tiếp nhận điểm tựa từ **minmax()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Subgrid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Responsive grid không truy vấn môi trường (media query)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
grid-template-columns:
  repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
```

### `auto-fit` vs `auto-fill`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- `auto-fill`: giữ các hypothetical empty tracks.
- `auto-fit`: collapse empty tracks để existing items stretch.

---

# 33. Grid placement

các thuộc tính (properties):

```text
grid-column-start
grid-column-end
grid-row-start
grid-row-end
grid-column
grid-row
grid-area
```

Example:

```css
.hero {
  grid-column: 1 / -1;
}
```

`-1` = last grid line.

Span:

```css
.card {
  grid-column: span 2;
}
```

---

# 34. Named Grid Areas

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.layout {
  display: grid;
  grid-template:
    "header header" auto
    "sidebar main" 1fr
    "footer footer" auto
    / 16rem 1fr;
}

header { grid-area: header; }
aside  { grid-area: sidebar; }
main   { grid-area: main; }
footer { grid-area: footer; }
```

Rất readable cho page bố cục (layout / 레이아웃).

---

# 35. Grid alignment

Bộ chứa (container / 컨테이너):

```text
justify-items
align-items
place-items
justify-content
align-content
place-content
```

Item:

```text
justify-self
align-self
place-self
```

Shorthand:

```css
place-items: center;
```

= `align-items` + `justify-items`.

---

# 36. Implicit Grid

Nếu item nằm ngoài tường minh (explicit / 명시적) grid, trình duyệt (browser / 브라우저) tạo implicit tracks.

các thuộc tính (properties):

```css
grid-auto-columns
grid-auto-rows
grid-auto-flow
```

Example:

```css
.grid {
  grid-auto-rows: minmax(6rem, auto);
}
```

`grid-auto-flow`:

```text
row
column
dense
row dense
column dense
```

⚠ `dense` có thể visually reorder items; cẩn thận khả năng tiếp cận (accessibility / 접근성).

---

# 37. Subgrid [ADV/hiện đại (modern / 현대적)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Subgrid** tiếp nhận điểm tựa từ **Responsive grid không truy vấn môi trường (media query)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Typography** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Subgrid

### CSS Idiom — Aligned card internals

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.card {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 3;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — dùng chung (shared / 공유) nhánh học (track / 트랙) đặc tả hợp đồng (contract / 계약)

Parent định nghĩa nhánh học (track / 트랙) hệ thống (system / 시스템); child reuse đúng nhánh học (track / 트랙) đó.

### Mẫu thiết kế (design pattern / 디자인 패턴) — Nested alignment without duplicated dimensions

Subgrid giảm duplicate bố cục (layout / 레이아웃) constants và giữ alignment xuyên hierarchy.

Child grid có thể kế thừa tracks từ parent.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;
}
```

Use trường hợp (case / 사례):
- card title/body/footer cần align across cards,
- nested bố cục (layout / 레이아웃) cần cùng column grid.

---

# 38. Grid vs Flexbox — chọn đúng

Dùng **Flexbox** khi:
- bố cục (layout / 레이아웃) chủ yếu 1 axis,
- content quyết định kích thước (size / 크기),
- navbar, toolbar, chips, row.

Dùng **Grid** khi:
- cần row + column,
- page bố cục (layout / 레이아웃),
- cards ma trận (matrix / 행렬),
- precise placement,
- tracks quan trọng hơn content.

Cấp cao (senior / 시니어) không hỏi "Grid hay Flex cái nào tốt hơn", mà hỏi:

> bố cục (layout / 레이아웃) này được điều khiển bởi **content luồng (flow / 흐름)** hay bởi **nhánh học (track / 트랙) cấu trúc (structure / 구조)**?

---

# 39. Float [LEGACY nhưng cần biết]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
img {
  float: left;
  margin-right: 1rem;
}
```

Float ngày nay chủ yếu hữu ích cho văn bản (text / 텍스트) wrapping quanh media.

Không nên dùng float để làm page bố cục (layout / 레이아웃) hiện đại.

Clear:

```css
clear: both;
```

---

# 40. Multi-column bố cục (layout / 레이아웃) [ADV]

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.article {
  columns: 3 18rem;
  column-gap: 2rem;
}
```

các thuộc tính (properties):

```text
column-count
column-width
columns
column-gap
column-rule
column-span
break-before
break-after
break-inside
```

Useful cho newspaper/text-heavy layouts.

---

# 41. Typography [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Typography** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Subgrid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **font-family** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Typography

### CSS Idiom — Unitless line-height

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
body {
  line-height: 1.5;
}
```

### CSS Idiom — Readable measure

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.prose {
  max-inline-size: 65ch;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Fluid kiểu (type / 타입) quy mô (scale / 규모)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
:root {
  --step--1: clamp(.875rem, .84rem + .15vw, .95rem);
  --step-0: clamp(1rem, .95rem + .25vw, 1.125rem);
  --step-1: clamp(1.25rem, 1.05rem + .9vw, 1.75rem);
  --step-2: clamp(1.75rem, 1.25rem + 2vw, 3rem);
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Typographic hierarchy

Xây một hệ kiểu (type system / 타입 시스템):
- body,
- small,
- label,
- heading,
- display.

Không chọn từng font-size ngẫu nhiên.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **font-family** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Typography** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **font-size** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `font-family`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
body {
  font-family:
    Inter,
    system-ui,
    -apple-system,
    "Segoe UI",
    sans-serif;
}
```

Luôn có generic phương án dự phòng (fallback).

Generic families:
- `serif`
- `sans-serif`
- `monospace`
- `cursive`
- `fantasy`
- `system-ui`

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **font-size** tiếp nhận điểm tựa từ **font-family** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **font-weight** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `font-size`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
font-size: 1rem;
```

Fluid:

```css
font-size: clamp(1rem, 0.95rem + 0.4vw, 1.25rem);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **font-weight** tiếp nhận điểm tựa từ **font-size** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **font-style** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `font-weight`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
normal ≈ 400
bold ≈ 700
100 ... 900
```

biến (variable) font có thể hỗ trợ phạm vi (range / 범위).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **font-style** tiếp nhận điểm tựa từ **font-weight** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **line-height** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `font-style`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
normal
italic
oblique
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **line-height** tiếp nhận điểm tựa từ **font-style** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **font shorthand** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `line-height`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
body {
  line-height: 1.5;
}
```

Unitless thường tốt vì inherit theo multiplier.

Heading:

```css
h1 {
  line-height: 1.1;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **font shorthand** tiếp nhận điểm tựa từ **line-height** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **text-align** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `font` shorthand

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
font: italic 600 1rem/1.5 Inter, sans-serif;
```

⚠ Shorthand reset nhiều font sub-properties.

---

# 42. văn bản (text / 텍스트) các thuộc tính (properties) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **text-align** tiếp nhận điểm tựa từ **font shorthand** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **text-decoration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `text-align`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
start
end
left
right
center
justify
```

Ưu tiên `start/end` cho internationalization.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **text-decoration** tiếp nhận điểm tựa từ **text-align** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **text-transform** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `text-decoration`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
a {
  text-decoration: underline;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.2em;
}
```

Sub-properties:
- `text-decoration-line`
- `text-decoration-color`
- `text-decoration-style`
- `text-decoration-thickness`

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **text-transform** tiếp nhận điểm tựa từ **text-decoration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **letter-spacing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `text-transform`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
none
uppercase
lowercase
capitalize
```

Không dùng CSS uppercase thay cho dữ liệu nếu ngữ nghĩa (semantics / 의미론)/bản sao (copy / 복사) thực sự cần uppercase.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **letter-spacing** tiếp nhận điểm tựa từ **text-transform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **word-spacing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `letter-spacing`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.title {
  letter-spacing: -0.02em;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **word-spacing** tiếp nhận điểm tựa từ **letter-spacing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **text-indent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `word-spacing`

Điều chỉnh không gian (space / 공간) giữa từ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **text-indent** tiếp nhận điểm tựa từ **word-spacing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **white-space** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `text-indent`

Indent dòng đầu.

---

# 43. Wrapping / Breaking [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **white-space** tiếp nhận điểm tựa từ **text-indent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **overflow-wrap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `white-space`

Dùng chung (common / 공통):

```text
normal
nowrap
pre
pre-wrap
pre-line
break-spaces
```

### `nowrap`

Không wrap tại normal whitespace.

### `pre`

Giữ whitespace + newline, không wrap tự nhiên.

### `pre-wrap`

Giữ whitespace/newline nhưng cho wrap.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **white-space** xác định đầu vào; **overflow-wrap** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **word-break** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `overflow-wrap`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
overflow-wrap: anywhere;
```

Cho phép break long URL/đơn vị từ (token / 토큰).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **overflow-wrap** xác định đầu vào; **word-break** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **hyphens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `word-break`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
normal
break-all
keep-all
```

Cẩn thận `break-all` vì có thể break rất xấu.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **hyphens** tiếp nhận điểm tựa từ **word-break** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **text-overflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `hyphens`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
p {
  hyphens: auto;
}
```

Cần `lang` đúng trong HTML để trình duyệt (browser / 브라우저) hyphenate tốt.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **hyphens** xác định đầu vào; **text-overflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **text-wrap [hiện đại (modern / 현대적)]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `text-overflow`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
text-overflow: ellipsis;
```

Thường đi cùng `overflow:hidden` + `white-space:nowrap`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **text-overflow** xác định đầu vào; **text-wrap [hiện đại (modern / 현대적)]** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mẫu (pattern / 패턴) notes — Color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `text-wrap` [hiện đại (modern / 현대적)]

Useful các giá trị (values):

```text
wrap
nowrap
balance
pretty
```

Heading:

```css
h1 {
  text-wrap: balance;
}
```

Body bản sao (copy / 복사):

```css
p {
  text-wrap: pretty;
}
```

---

# 44. Web Fonts `@font-face` [cốt lõi (core / 핵심)/ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@font-face {
  font-family: "MyFont";
  src: url("/fonts/myfont.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

Descriptors quan trọng:
- `font-family`
- `src`
- `font-weight`
- `font-style`
- `font-display`
- `unicode-range`

`font-display` dùng chung (common / 공통):
- `auto`
- `block`
- `swap`
- `fallback`
- `optional`

Hiệu năng (performance / 성능): ưu tiên WOFF2, subset khi cần, không tải (load / 로드) quá nhiều weights.

---

# 45. Color [cốt lõi (core / 핵심) → hiện đại (modern / 현대적)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Color** tiếp nhận điểm tựa từ **text-wrap [hiện đại (modern / 현대적)]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Keywords** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Color

### CSS Idiom — `currentColor`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.icon {
  fill: currentColor;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — mang tính ngữ nghĩa (semantic / 의미적) color tokens

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
--color-action: #2563eb;
--color-danger: #dc2626;
--color-text-muted: #6b7280;
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — thành phần nguyên thủy (primitive / 기본 요소) → mang tính ngữ nghĩa (semantic / 의미적) → thành phần (component / 컴포넌트)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
blue-600
→ action-primary
→ button-primary-bg
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Oklch phù hợp khi cần tạo palette có lightness dễ kiểm soát hơn HSL.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Keywords** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hex** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Keywords

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
color: red;
color: transparent;
color: currentColor;
```

`currentColor` = hiện tại (current / 현재) giá trị (value / 값) của `color`.

```css
.icon {
  border: 1px solid currentColor;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Hex** tiếp nhận điểm tựa từ **Keywords** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **rgb()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hex

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
#ff0000
#f00
#ff000080 /* alpha */

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **rgb()** tiếp nhận điểm tựa từ **Hex** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **hsl()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `rgb()`

Hiện đại (modern / 현대적) cú pháp (syntax / 문법):

```css
color: rgb(255 0 0 / 80%);
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **hsl()** tiếp nhận điểm tựa từ **rgb()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **oklch() [hiện đại (modern / 현대적)]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `hsl()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
color: hsl(220 90% 56%);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **oklch() [hiện đại (modern / 현대적)]** tiếp nhận điểm tựa từ **hsl()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Relative colors [hiện đại (modern / 현대적)]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `oklch()` [hiện đại (modern / 현대적)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
color: oklch(62% 0.2 250);
```

Oklch hữu ích cho hệ thống thiết kế (design system) vì lightness gần với perceived lightness hơn HSL.

```css
:root {
  --brand: oklch(62% 0.20 255);
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Relative colors [hiện đại (modern / 현대적)]** tiếp nhận điểm tựa từ **oklch() [hiện đại (modern / 현대적)]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **color-mix()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relative colors [hiện đại (modern / 현대적)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
--brand-hover:
  oklch(from var(--brand) calc(l - 0.08) c h);
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **color-mix()** tiếp nhận điểm tựa từ **Relative colors [hiện đại (modern / 현대적)]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **light-dark()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `color-mix()`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
background:
  color-mix(in oklab, var(--brand) 20%, white);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **light-dark()** tiếp nhận điểm tựa từ **color-mix()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **background-size** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `light-dark()`

Kết hợp color scheme-aware các giá trị (values) khi môi trường hỗ trợ:

```css
:root {
  color-scheme: light dark;
  --surface: light-dark(white, #111);
}
```

---

# 46. Backgrounds [cốt lõi (core / 핵심)]

các thuộc tính (properties):

```text
background-color
background-image
background-repeat
background-position
background-size
background-origin
background-clip
background-attachment
background
```

Example:

```css
.hero {
  background:
    linear-gradient(rgb(0 0 0 / .45), rgb(0 0 0 / .45)),
    url("/hero.jpg")
    center / cover
    no-repeat;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **background-size** tiếp nhận điểm tựa từ **light-dark()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tuyến tính (linear / 선형)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `background-size`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
auto
cover
contain
<length>
<percentage>
```

- `cover`: cover box, có thể crop.
- `contain`: show toàn bộ ảnh (image / 이미지), có thể dư khoảng trống.

---

# 47. Gradients [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Tuyến tính (linear / 선형)** tiếp nhận điểm tựa từ **background-size** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Radial** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tuyến tính (linear / 선형)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
background:
  linear-gradient(135deg, #2563eb, #7c3aed);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Radial** tiếp nhận điểm tựa từ **Tuyến tính (linear / 선형)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Radial

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
background:
  radial-gradient(circle at top, white, #ddd);
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Conic** tiếp nhận điểm tựa từ **Radial** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **box-shadow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conic

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
background:
  conic-gradient(red, yellow, lime, cyan, blue, magenta, red);
```

Useful:
- charts,
- color wheels,
- decorative UI.

---

# 48. Shadows [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **box-shadow** tiếp nhận điểm tựa từ **Conic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **text-shadow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `box-shadow`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
box-shadow: 0 8px 24px rgb(0 0 0 / 12%);
```

Cú pháp (syntax / 문법) concept:

```text
offset-x offset-y blur spread color inset?
```

Multiple shadows:

```css
box-shadow:
  0 1px 2px rgb(0 0 0 / .08),
  0 8px 24px rgb(0 0 0 / .10);
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **text-shadow** tiếp nhận điểm tựa từ **box-shadow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **object-fit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `text-shadow`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
text-shadow: 0 1px 2px rgb(0 0 0 / .3);
```

---

# 49. đối tượng (object / 객체) sizing: images/video [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **object-fit** tiếp nhận điểm tựa từ **text-shadow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **object-position** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `object-fit`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
fill
contain
cover
none
scale-down
```

```css
.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **object-position** tiếp nhận điểm tựa từ **object-fit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **backdrop-filter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `object-position`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
object-position: center top;
```

---

# 50. `image-rendering`

Có thể điều khiển scaling ảnh (image / 이미지) điểm ảnh (pixel / 픽셀) art.

Dùng chung (common / 공통):
```text
auto
crisp-edges
pixelated
```

---

# 51. Filters [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
filter: blur(4px);
filter: brightness(1.1);
filter: contrast(1.2);
filter: grayscale(1);
filter: drop-shadow(0 4px 8px rgb(0 0 0 / .2));
```

các hàm (functions):
- `blur()`
- `brightness()`
- `contrast()`
- `drop-shadow()`
- `grayscale()`
- `hue-rotate()`
- `invert()`
- `opacity()`
- `saturate()`
- `sepia()`

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **backdrop-filter** tiếp nhận điểm tựa từ **object-position** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — thuộc tính lô-gic (logic / 논리) (logical properties)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `backdrop-filter`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.glass {
  background: rgb(255 255 255 / 70%);
  backdrop-filter: blur(16px);
}
```

Có chi phí (cost / 비용) rendering; kiểm thử (test / 테스트) hiệu năng (performance / 성능).

---

# 52. Blend Modes [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
mix-blend-mode: multiply;
background-blend-mode: multiply;
```

Dùng chung (common / 공통) blend modes:
- `normal`
- `multiply`
- `screen`
- `overlay`
- `darken`
- `lighten`
- `difference`

---

# 53. thuộc tính lô-gic (logic / 논리) (logical properties) [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — thuộc tính lô-gic (logic / 논리) (logical properties)** tiếp nhận điểm tựa từ **backdrop-filter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — thiết kế đáp ứng (responsive design)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — thuộc tính lô-gic (logic / 논리) (logical properties)

### CSS Idiom — Inline centering

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
margin-inline: auto;
```

### CSS Idiom — Writing-mode-safe spacing

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
padding-inline: 1rem;
padding-block: .75rem;
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — International-ready thành phần (component / 컴포넌트)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
margin-inline-start: auto;
border-inline-start: 1px solid;
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Direction-agnostic UI

Thành phần (component / 컴포넌트) tránh hard-code LTR các giả định (assumptions / 가정들) để hỗ trợ RTL/localization tốt hơn.

Thay vì phụ thuộc `left/right/top/bottom`, dùng writing-mode-aware các thuộc tính (properties).

Vật lý (physical / 물리적):

```css
margin-left
padding-right
border-top
width
height
```

Logical:

```css
margin-inline-start
margin-inline-end
margin-block-start
margin-block-end

padding-inline
padding-block

border-inline-start
border-block-end

inline-size
block-size
```

Example:

```css
.card {
  padding-inline: 1rem;
  padding-block: 1.5rem;
  margin-inline: auto;
  max-inline-size: 70rem;
}
```

**cấp cao (senior / 시니어) ghi chú (note / 노트):** thuộc tính lô-gic (logic / 논리) (logical properties) giúp RTL/i18n tốt hơn.

---

# 54. Writing Modes [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
writing-mode: horizontal-tb;
writing-mode: vertical-rl;
writing-mode: vertical-lr;
```

Related:

```css
direction: rtl;
text-orientation: mixed;
```

Không nên dùng `direction` chỉ để reorder UI tùy tiện.

---

# 55. thiết kế đáp ứng (responsive design) [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — thiết kế đáp ứng (responsive design)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — thuộc tính lô-gic (logic / 논리) (logical properties)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Media features quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — thiết kế đáp ứng (responsive design)

### CSS Idiom — Content-driven điểm ngắt (breakpoint)

Không chọn điểm ngắt (breakpoint) vì tên thiết bị. Chọn tại điểm bố cục (layout / 레이아웃) cần thay đổi.

### Mẫu lập trình (coding pattern / 코딩 패턴) — Fluid first, truy vấn (query / 쿼리) second

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
1. intrinsic sizing
2. flex/grid wrapping
3. clamp/min/max
4. media/container query khi cần
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Responsive thành phần (component / 컴포넌트)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.widget-shell {
  container-type: inline-size;
}

@container (width >= 30rem) {
  .widget {
    grid-template-columns: 8rem 1fr;
  }
}
```

Thành phần (component / 컴포넌트) tự thích ứng theo không gian nó thực sự nhận được.

Responsive không chỉ là "mobile điểm ngắt (breakpoint)".

Cấp cao (senior / 시니어) approach:
1. content-first,
2. bố cục nội tại (intrinsic layout),
3. fluid sizing,
4. truy vấn môi trường (media query) khi bố cục (layout / 레이아웃) thực sự cần đổi,
5. truy vấn vùng chứa (container query) khi thành phần (component / 컴포넌트) cần thích ứng theo bộ chứa (container / 컨테이너).

---

# 56. các truy vấn môi trường (media queries) [cốt lõi (core / 핵심)]

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
@media (min-width: 768px) {
  .layout {
    grid-template-columns: 16rem 1fr;
  }
}
```

Hiện đại (modern / 현대적) phạm vi (range / 범위) cú pháp (syntax / 문법):

```css
@media (width >= 48rem) {}
```

Có thể:

```css
@media (48rem <= width < 80rem) {}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Media features quan trọng** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — thiết kế đáp ứng (responsive design)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dark chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Media features quan trọng

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
width
height
orientation
aspect-ratio
resolution
hover
any-hover
pointer
any-pointer
prefers-color-scheme
prefers-reduced-motion
prefers-contrast
forced-colors
display-mode
```

---

# 57. Mobile-first

Cơ sở (base / 기반) = mobile:

```css
.card {
  display: block;
}

@media (width >= 48rem) {
  .card {
    display: grid;
    grid-template-columns: 12rem 1fr;
  }
}
```

Không bắt buộc mọi dự án (project / 프로젝트) phải mobile-first, nhưng thường giúp cải tiến lũy tiến (progressive enhancement) và CSS đơn giản.

---

# 58. người dùng (user / 사용자) Preference các truy vấn môi trường (media queries) [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Dark chế độ (mode / 모드)** tiếp nhận điểm tựa từ **Media features quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **giảm chuyển động (reduced motion)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dark chế độ (mode / 모드)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@media (prefers-color-scheme: dark) {
  :root {
    --surface: #111;
    --text: #eee;
  }
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **giảm chuyển động (reduced motion)** tiếp nhận điểm tựa từ **Dark chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pointer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## giảm chuyển động (reduced motion)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto;
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    transition-duration: 0.01ms;
  }
}
```

Trong môi trường vận hành (production / 운영 환경) có thể viết targeted hơn thay vì kill toàn bộ motion.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Pointer** tiếp nhận điểm tựa từ **giảm chuyển động (reduced motion)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — truy vấn vùng chứa (container query)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pointer

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@media (pointer: coarse) {
  .button {
    min-height: 44px;
  }
}
```

Đừng detect "mobile" bằng width nếu điều bạn thực sự quan tâm là đầu vào (input / 입력) modality.

---

# 59. các truy vấn vùng chứa (container queries) [ADV/hiện đại (modern / 현대적)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — truy vấn vùng chứa (container query)** tiếp nhận điểm tựa từ **Pointer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Individual transform các thuộc tính (properties)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — truy vấn vùng chứa (container query)

### CSS Idiom — Named bộ chứa (container / 컨테이너) đặc tả hợp đồng (contract / 계약)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.panel {
  container: panel / inline-size;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — thành phần (component / 컴포넌트) chế độ (mode / 모드) switch

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
@container panel (width < 24rem) {
  .profile {
    display: block;
  }
}

@container panel (width >= 24rem) {
  .profile {
    display: grid;
    grid-template-columns: auto 1fr;
  }
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Contextual responsiveness

Thành phần (component / 컴포넌트) hỏi:

> "Không gian tôi thực sự nhận được rộng bao nhiêu?"

thay vì chỉ hỏi vùng nhìn (viewport).

truy vấn môi trường (media query) hỏi vùng nhìn (viewport).

truy vấn vùng chứa (container query) hỏi **bộ chứa (container / 컨테이너) của thành phần (component / 컴포넌트)**.

Setup:

```css
.card-list {
  container-type: inline-size;
}
```

Truy vấn (query / 쿼리):

```css
@container (width >= 32rem) {
  .card {
    display: grid;
    grid-template-columns: 10rem 1fr;
  }
}
```

Named bộ chứa (container / 컨테이너):

```css
.sidebar {
  container-name: sidebar;
  container-type: inline-size;
}

@container sidebar (width >= 25rem) {
  .widget {
    grid-template-columns: 1fr 1fr;
  }
}
```

Shorthand:

```css
container: sidebar / inline-size;
```

**cấp cao (senior / 시니어) use trường hợp (case / 사례):** thành phần (component / 컴포넌트) dùng trong main, sidebar, modal, dashboard card mà không phụ thuộc vùng nhìn (viewport).

---

# 60. bộ chứa (container / 컨테이너) Style Queries [hiện đại (modern / 현대적)]

Có thể truy vấn (query / 쿼리) custom thuộc tính (property / 속성)/computed style trạng thái (state / 상태) của bộ chứa (container / 컨테이너) trong mức hỗ trợ trình duyệt (browser support / 브라우저 지원) phù hợp.

Concept:

```css
.card-wrapper {
  --density: compact;
}

@container style(--density: compact) {
  .card {
    padding: .5rem;
  }
}
```

Nên xem tính tương thích (compatibility / 호환성) của trình duyệt (browser / 브라우저) targets trước khi dùng môi trường vận hành (production / 운영 환경).

---

# 61. Responsive Media [cốt lõi (core / 핵심)]

Images:

```css
img,
video {
  max-width: 100%;
  height: auto;
}
```

Bộ chứa (container / 컨테이너):

```css
.wrapper {
  width: min(100% - 2rem, 75rem);
  margin-inline: auto;
}
```

---

# 62. CSS Transforms [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
transform: translateX(10px);
transform: translate(10px, 20px);
transform: scale(1.05);
transform: rotate(5deg);
transform: skewX(10deg);
```

Multiple:

```css
transform: translateY(-2px) scale(1.02);
```

⚠ transform thứ tự (order / 순서) matters.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Individual transform các thuộc tính (properties)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — truy vấn vùng chứa (container query)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **transform-origin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Individual transform các thuộc tính (properties)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
translate: 10px 0;
rotate: 5deg;
scale: 1.05;
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **transform-origin** tiếp nhận điểm tựa từ **Individual transform các thuộc tính (properties)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3D** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `transform-origin`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
transform-origin: center;
transform-origin: top left;
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **3D** tiếp nhận điểm tựa từ **transform-origin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — chuyển tiếp (transition / 전이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3D

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
perspective: 1000px;
transform: rotateY(20deg);
transform-style: preserve-3d;
backface-visibility: hidden;
```

---

# 63. Transitions [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — chuyển tiếp (transition / 전이)** tiếp nhận điểm tựa từ **3D** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — Animation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — chuyển tiếp (transition / 전이)

### CSS Idiom — Animate tường minh (explicit / 명시적) các thuộc tính (properties)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
transition:
  opacity 150ms ease,
  transform 150ms ease;
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — chuyển tiếp trạng thái (state transition / 상태 전이)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.menu {
  opacity: 0;
  translate: 0 -.5rem;
  transition:
    opacity 150ms ease,
    translate 150ms ease;
}

.menu[data-state="open"] {
  opacity: 1;
  translate: 0;
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Motion as trạng thái (state / 상태) phản hồi (feedback / 피드백)

Motion nên giải thích trạng thái (state / 상태) thay đổi (change / 변경), không chỉ để trang "đẹp hơn".

```css
.button {
  transition:
    background-color 150ms ease,
    transform 150ms ease;
}
```

Sub-properties:

```text
transition-property
transition-duration
transition-timing-function
transition-delay
transition
```

Timing:

```text
linear
ease
ease-in
ease-out
ease-in-out
cubic-bezier(...)
steps(...)
```

### Không nên

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
transition: all .3s;
```

trong thành phần (component / 컴포넌트) lớn vì:
- animate thuộc tính (property / 속성) ngoài ý muốn,
- khó predict,
- có thể gây hiệu năng (performance / 성능) issues.

Nên chỉ định:

```css
transition: opacity 150ms ease, transform 150ms ease;
```

---

# 64. Animations [cốt lõi (core / 핵심)/ADV]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — Animation** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — chuyển tiếp (transition / 전이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **animation-iteration-count** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — Animation

### CSS Idiom — Reduced-motion override

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-motion {
    animation: none;
  }
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Enter / Open / Leave trạng thái (state / 상태)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.toast[data-state="entering"] {}
.toast[data-state="open"] {}
.toast[data-state="leaving"] {}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — Separate hành vi (behavior / 동작) from presentation

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
Application state → data/aria attribute
CSS → visual state
```

JS không nên hard-code visual details; CSS không nên tự quyết định nghiệp vụ (business / 비즈니스) trạng thái (state / 상태).

```css
@keyframes spin {
  to {
    transform: rotate(1turn);
  }
}

.spinner {
  animation: spin 1s linear infinite;
}
```

các thuộc tính (properties):

```text
animation-name
animation-duration
animation-timing-function
animation-delay
animation-iteration-count
animation-direction
animation-fill-mode
animation-play-state
animation
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **animation-iteration-count** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — Animation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **animation-direction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `animation-iteration-count`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
1
2
infinite
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **animation-direction** tiếp nhận điểm tựa từ **animation-iteration-count** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **animation-fill-mode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `animation-direction`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
normal
reverse
alternate
alternate-reverse
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **animation-fill-mode** tiếp nhận điểm tựa từ **animation-direction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **animation-play-state** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `animation-fill-mode`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
none
forwards
backwards
both
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **animation-play-state** tiếp nhận điểm tựa từ **animation-fill-mode** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **will-change** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `animation-play-state`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
running
paused
```

---

# 65. hiệu năng (performance / 성능) của animation [ADV]

Ưu tiên animate:
- `transform`
- `opacity`

Cẩn thận animation liên tục của:
- `width`
- `height`
- `top/left`
- `margin`
vì có thể trigger bố cục (layout / 레이아웃) nhiều hơn.

Nhưng đừng biến "transform always fast" thành luật tuyệt đối; profiling với DevTools khi animation phức tạp.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **will-change** tiếp nhận điểm tựa từ **animation-play-state** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — lồng cú pháp (nesting)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `will-change`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card:hover {
  will-change: transform;
}
```

⚠ Không set `will-change` cho hàng trăm elements hoặc toàn cục (global / 전역). Nó là hint có tài nguyên (resource / 자원) chi phí (cost / 비용).

---

# 66. Scroll hành vi (behavior / 동작) [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
html {
  scroll-behavior: smooth;
}
```

Tôn trọng giảm chuyển động (reduced motion).

---

# 67. Scroll Snap [ADV]

Bộ chứa (container / 컨테이너):

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}
```

Items:

```css
.carousel > * {
  scroll-snap-align: start;
}
```

Related:

```text
scroll-snap-type
scroll-snap-align
scroll-snap-stop
scroll-padding
scroll-margin
```

---

# 68. hoạt ảnh điều khiển bằng cuộn (scroll-driven animations) [hiện đại (modern / 현대적)]

Cho animation progress theo scroll thay vì thời gian (time / 시간).

Concept:

```css
.progress {
  transform-origin: left;
  animation: grow linear;
  animation-timeline: scroll();
}

@keyframes grow {
  from { scale: 0 1; }
  to   { scale: 1 1; }
}
```

View timeline cho element:

```css
.card {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}
```

Kiểm tra mức hỗ trợ trình duyệt (browser support / 브라우저 지원) trước khi dùng cho trọng yếu (critical / 중요) UX; cải tiến lũy tiến (progressive enhancement) là hướng tốt.

---

# 69. chuyển cảnh giao diện (view transitions) [hiện đại (modern / 현대적)]

Cho phép trình duyệt (browser / 브라우저) animate visual chuyển tiếp (transition / 전이) giữa UI các trạng thái (states)/pages tùy API/ngữ cảnh (context / 맥락).

CSS side thường liên quan các phần tử giả (pseudo-elements):

```css
::view-transition-old(root) {}
::view-transition-new(root) {}
```

Named chuyển tiếp (transition / 전이):

```css
.hero {
  view-transition-name: hero-image;
}
```

Use trường hợp (case / 사례):
- tuyến (route / 경로) transitions,
- dùng chung (shared / 공유) element chuyển tiếp (transition / 전이),
- SPA trạng thái (state / 상태) thay đổi (change / 변경).

Đừng làm animation cản thao tác hoặc quá dài.

---

# 70. định vị theo điểm neo (anchor positioning) [hiện đại (modern / 현대적)]

Dùng CSS để đặt popover/tooltip dựa trên anchor.

Anchor:

```css
.trigger {
  anchor-name: --trigger;
}
```

Positioned element:

```css
.tooltip {
  position: fixed;
  position-anchor: --trigger;
  left: anchor(right);
  top: anchor(bottom);
}
```

Hệ sinh thái còn gồm các concept/thuộc tính (property / 속성) như:
- `anchor-name`
- `position-anchor`
- `anchor()`
- `anchor-size()`
- phương án dự phòng (fallback)/position try features.

Use trường hợp (case / 사례):
- tooltip,
- dropdown,
- menu,
- popover.

Cấp cao (senior / 시니어) quy tắc (rule / 규칙): kiểm tra trình duyệt (browser / 브라우저) mục tiêu (target / 대상) và phương án dự phòng (fallback) cho UI trọng yếu (critical / 중요).

---

# 71. CSS lồng cú pháp (nesting) [hiện đại (modern / 현대적)]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — lồng cú pháp (nesting)** tiếp nhận điểm tựa từ **will-change** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — phạm vi (scope / 범위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — lồng cú pháp (nesting)

### CSS Idiom — Nest các trạng thái (states), not DOM độ sâu (depth / 깊이)

Tốt:

```css
.button {
  &:hover {}
  &:focus-visible {}
  &[data-variant="danger"] {}
}
```

Tránh lồng cú pháp (nesting) theo toàn bộ DOM cây (tree / 트리).

### Mẫu lập trình (coding pattern / 코딩 패턴) — Component-local grouping

lồng cú pháp (nesting) phù hợp cho:
- các trạng thái (states),
- các phần tử giả (pseudo-elements),
- truy vấn môi trường (media query),
- truy vấn vùng chứa (container query),
- direct thành phần (component / 컴포넌트) slots.

### Mẫu thiết kế (design pattern / 디자인 패턴) — Flat giao diện công khai (public API), nested hiện thực (implementation / 구현)

Công khai (public / 공개) các bộ chọn (selectors) vẫn nên đơn giản; lồng cú pháp (nesting) chỉ hỗ trợ tổ chức nguồn (source / 소스).

Bản địa (native / 네이티브) CSS lồng cú pháp (nesting):

```css
.card {
  padding: 1rem;

  & .title {
    font-weight: 700;
  }

  &:hover {
    transform: translateY(-2px);
  }

  @media (width >= 48rem) {
    padding: 1.5rem;
  }
}
```

`&` đại diện bộ chọn (selector) hiện tại.

**Không nên lồng cú pháp (nesting) quá sâu:**

```css
.page {
  .section {
    .card {
      .header {
        .title {}
      }
    }
  }
}
```

Vì tạo bộ chọn (selector) coupling và độ đặc hiệu (specificity) độ phức tạp (complexity / 복잡도).

Quy tắc (rule / 규칙) thực tế: 1–3 levels là đủ trong đa số thành phần (component / 컴포넌트).

---

# 72. `@scope` [hiện đại (modern / 현대적)/ADV]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — phạm vi (scope / 범위)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — lồng cú pháp (nesting)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **appearance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — phạm vi (scope / 범위)

### CSS Idiom — Scoped typography

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@scope (.article) {
  h2 {}
  p {}
  a {}
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Scoped defaults

Dùng cho:
- article,
- widget,
- embedded app,
- third-party content area.

### Mẫu thiết kế (design pattern / 디자인 패턴) — Controlled ranh giới style (style boundary)

`@scope` nằm giữa toàn cục (global / 전역) CSS và full đóng gói (encapsulation) như Shadow DOM (cây DOM đóng gói)/CSS Modules.

Giới hạn bộ chọn (selector) trong vùng DOM.

Concept:

```css
@scope (.article) {
  h2 {
    color: var(--heading-color);
  }
}
```

Có thể phạm vi (scope / 범위) đến ranh giới (boundary / 경계) trong cú pháp (syntax / 문법) phù hợp.

Use trường hợp (case / 사례):
- thành phần (component / 컴포넌트)/themed subtree,
- tránh các bộ chọn (selectors) leak,
- giảm nhu cầu BEM prefix trong một số kiến trúc.

---

# 73. `@supports` — các truy vấn hỗ trợ tính năng (feature queries) [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@supports (display: grid) {
  .layout {
    display: grid;
  }
}
```

Negation:

```css
@supports not (backdrop-filter: blur(1rem)) {
  .glass {
    background: #fff;
  }
}
```

Complex:

```css
@supports (display: grid) and (gap: 1rem) {}
```

cải tiến lũy tiến (progressive enhancement):

```css
.card {
  background: #fff;
}

@supports (background: color-mix(in oklab, white, black)) {
  .card {
    background:
      color-mix(in oklab, var(--surface), var(--brand) 5%);
  }
}
```

---

# 74. `@media`, `@container`, `@supports` — khác nhau

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

| At-rule | Hỏi điều gì? | Use case |
|---|---|---|
| `@media` | môi trường/vùng nhìn (viewport)/người dùng (user / 사용자) preference | responsive page, dark chế độ (mode / 모드) |
| `@container` | kích thước/trạng thái (state / 상태) bộ chứa (container / 컨테이너) | responsive thành phần (component / 컴포넌트) |
| `@supports` | trình duyệt (browser / 브라우저) có hỗ trợ (support / 지원) tính năng (feature / 기능) không | cải tiến lũy tiến (progressive enhancement) |

---

# 75. các danh sách (lists) [cốt lõi (core / 핵심)]

các thuộc tính (properties):

```text
list-style-type
list-style-position
list-style-image
list-style
```

```css
ul {
  list-style: disc outside;
}
```

Custom marker:

```css
li::marker {
  color: var(--brand);
}
```

Counter advanced:

```css
.steps {
  counter-reset: step;
}

.steps li {
  counter-increment: step;
}

.steps li::before {
  content: counter(step) ". ";
}
```

---

# 76. Tables [cốt lõi (core / 핵심)]

các thuộc tính (properties):

```text
border-collapse
border-spacing
table-layout
caption-side
empty-cells
```

```css
table {
  width: 100%;
  border-collapse: collapse;
}
```

`table-layout`:

```text
auto
fixed
```

`fixed` giúp predictable widths/hiệu năng (performance / 성능) cho bảng lớn khi width xác định.

Responsive bảng (table / 테이블) thường cần wrapper:

```css
.table-scroll {
  overflow-x: auto;
}
```

---

# 77. Forms & Controls [cốt lõi (core / 핵심)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **appearance** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — phạm vi (scope / 범위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **accent-color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `appearance`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
input,
button,
select {
  font: inherit;
}

.custom-checkbox {
  appearance: none;
}
```

⚠ Khi bỏ bản địa (native / 네이티브) appearance, bạn chịu trách nhiệm về:
- focus,
- checked trạng thái (state / 상태),
- disabled,
- độ tương phản cao (high contrast),
- khả năng tiếp cận (accessibility / 접근성) visuals.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **accent-color** tiếp nhận điểm tựa từ **appearance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **caret-color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `accent-color`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
:root {
  accent-color: var(--brand);
}
```

Style bản địa (native / 네이티브):
- checkbox,
- radio,
- phạm vi (range / 범위),
- progress (tùy browser).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **caret-color** tiếp nhận điểm tựa từ **accent-color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **resize** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `caret-color`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
input {
  caret-color: var(--brand);
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **resize** tiếp nhận điểm tựa từ **caret-color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **field-sizing [hiện đại (modern / 현대적)]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `resize`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
textarea {
  resize: vertical;
}
```

các giá trị (values):
- `none`
- `both`
- `horizontal`
- `vertical`

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **field-sizing [hiện đại (modern / 현대적)]** tiếp nhận điểm tựa từ **resize** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cursor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `field-sizing` [hiện đại (modern / 현대적)]

Trong mức hỗ trợ trình duyệt (browser support / 브라우저 지원) phù hợp, giúp form controls kích thước (size / 크기) theo content.

---

# 78. Cursor & Pointer hành vi (behavior / 동작)

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **cursor** tiếp nhận điểm tựa từ **field-sizing [hiện đại (modern / 현대적)]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **pointer-events** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `cursor`

Dùng chung (common / 공통):

```text
auto
default
pointer
text
move
not-allowed
grab
grabbing
wait
progress
crosshair
```

Đừng dùng `cursor:pointer` cho non-interactive element nếu ngữ nghĩa (semantics / 의미론) không click được.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **pointer-events** tiếp nhận điểm tựa từ **cursor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **user-select** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `pointer-events`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.overlay-decoration {
  pointer-events: none;
}
```

các giá trị (values) web UI thường:
- `auto`
- `none`

⚠ `pointer-events:none` không đồng nghĩa disabled mang tính ngữ nghĩa (semantic / 의미적).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **user-select** tiếp nhận điểm tựa từ **pointer-events** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **clip-path** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `user-select`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.user-select-none {
  user-select: none;
}
```

Chỉ dùng khi selection gây hại UX; văn bản (text / 텍스트) content thường nên select được.

---

# 79. Generated Content [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
content
quotes
counter-reset
counter-increment
counter-set
```

phần tử giả (pseudo-element):

```css
a.external::after {
  content: " ↗";
}
```

Không nhét thông tin (information / 정보) quan trọng chỉ trong CSS-generated content.

---

# 80. Shapes, Clip & Mask [ADV/hiện đại (modern / 현대적)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **user-select** xác định đầu vào; **clip-path** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **shape-outside** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `clip-path`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.avatar {
  clip-path: circle(50%);
}
```

Polygon:

```css
clip-path:
  polygon(50% 0, 100% 100%, 0 100%);
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **clip-path** xác định đầu vào; **shape-outside** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Masks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `shape-outside`

Văn bản (text / 텍스트) wrap quanh shape, thường với float.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Masks** tiếp nhận điểm tựa từ **shape-outside** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **[cốt lõi (core / 핵심)]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Masks

Concept các thuộc tính (properties):
- `mask`
- `mask-image`
- `mask-size`
- `mask-position`
- `mask-repeat`

Useful cho icons/effects.

---

# 81. `isolation`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.component {
  isolation: isolate;
}
```

Tạo ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) mới và isolate blending.

Rất hữu ích để tránh negative z-index child "rơi" ra ngoài thành phần (component / 컴포넌트).

---

# 82. `box-decoration-break`

Điều khiển decoration của fragmented inline/multiline boxes.

```css
.highlight {
  box-decoration-break: clone;
}
```

Có thể cần prefixed form trong một số mục tiêu (target / 대상).

---

# 83. `writing-mode`, `direction`, international UI [ADV]

Đừng hard-code:

```css
margin-left: 16px;
text-align: left;
```

nếu dự án (project / 프로젝트) có RTL.

Nên:

```css
margin-inline-start: 1rem;
text-align: start;
```

---

# 84. At-rules cần biết

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **[cốt lõi (core / 핵심)]** tiếp nhận điểm tựa từ **Masks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **[ADV/hiện đại (modern / 현대적)]** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## [cốt lõi (core / 핵심)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
@media
@supports
@font-face
@keyframes
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **[ADV/hiện đại (modern / 현대적)]** tiếp nhận điểm tựa từ **[cốt lõi (core / 핵심)]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## [ADV/hiện đại (modern / 현대적)]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
@layer
@container
@property
@scope
@starting-style
@view-transition
@counter-style
@page
@import
@namespace
```

---

# 85. `@import`

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@import url("./theme.css");
```

Có thể kết hợp tầng (layer / 계층)/hỗ trợ (support / 지원)/media tùy cú pháp (syntax / 문법).

Tuy nhiên môi trường vận hành (production / 운영 환경) thường ưu tiên bundler/quy trình bản dựng (build / 빌드) (build pipeline) hoặc `<link>` vì `@import` có thể tạo phụ thuộc (dependency / 의존성)/loading considerations.

---

# 86. `@starting-style` [hiện đại (modern / 현대적)]

Hỗ trợ chuyển tiếp (transition / 전이) từ trạng thái element mới xuất hiện / discrete-state scenarios trong mức hỗ trợ trình duyệt (browser support / 브라우저 지원) phù hợp.

Concept:

```css
.dialog {
  opacity: 1;
  transition: opacity .2s;
}

@starting-style {
  .dialog {
    opacity: 0;
  }
}
```

Useful cho popover/dialog entry transitions.

---

# 87. Discrete transitions & `transition-behavior` [hiện đại (modern / 현대적)]

Một số discrete thuộc tính (property / 속성) có thể tham gia transitions với:

```css
transition-behavior: allow-discrete;
```

Use trường hợp (case / 사례):
- `display`,
- overlay/dialog/popover vòng đời (lifecycle / 생명주기)
trong các mức hỗ trợ trình duyệt (browser support / 브라우저 지원) phù hợp.

---

# 88. kiến trúc (architecture / 아키텍처): tổ chức CSS như cấp cao (senior / 시니어) [ADV]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **[ADV/hiện đại (modern / 현대적)]** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BEM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — kiến trúc (architecture / 아키텍처)

### CSS Idiom — One responsibility per tầng (layer / 계층)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
tokens      → values
base        → element defaults
layout      → spatial primitives
components  → UI components
utilities   → atomic helpers
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Composition over overrides

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```html
<div class="stack card">...</div>
```

thay vì tạo nhiều thành phần (component / 컴포넌트) biến thể (variant) chỉ để đổi spacing.

### Mẫu thiết kế (design pattern / 디자인 패턴) — CUBE-like thinking

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
Composition
Utility
Block
Exception
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — ITCSS-like thứ tự (ordering / 순서)

Từ toàn cục (global / 전역)/general → cục bộ (local / 로컬)/specific:
- settings/tokens,
- tools,
- generic,
- elements,
- objects,
- components,
- các tiện ích (utilities).

Có thể kết hợp với `@layer`.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Kiến trúc (architecture / 아키텍처) tốt là kiến trúc (architecture / 아키텍처) mà dev mới có thể dự đoán:
- style nằm ở đâu,
- override thế nào,
- trạng thái (state / 상태) viết ở đâu,
- đơn vị từ (token / 토큰) nào được dùng,
- thành phần (component / 컴포넌트) nào chịu trách nhiệm bố cục (layout / 레이아웃).

CSS môi trường vận hành (production / 운영 환경) không chỉ là biết thuộc tính (property / 속성).

Bạn cần quản lý:

```text
cascade
scope
tokens
component boundaries
variants
states
responsive rules
utilities
third-party CSS
dead CSS
build output
```

---

# 89. Naming Strategies

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **BEM** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ưu tiên tiện ích (utility-first)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BEM

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.card {}
.card__title {}
.card__body {}
.card--featured {}
```

Ưu:
- tường minh (explicit / 명시적),
- ít collision,
- dễ đọc trong plain CSS.

Nhược:
- verbose.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **ưu tiên tiện ích (utility-first)** tiếp nhận điểm tựa từ **BEM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CSS Modules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ưu tiên tiện ích (utility-first)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```html
<div class="flex items-center gap-4">
```

Ưu:
- nhanh,
- constrained đơn vị từ (token / 토큰) thiết kế (design tokens),
- ít custom CSS.

Nhược:
- markup nhiều lớp (class / 클래스),
- cần convention/tooling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **CSS Modules** tiếp nhận điểm tựa từ **ưu tiên tiện ích (utility-first)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CSS-in-JS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSS Modules

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.title {}
```

Hệ thống dựng (build system / 빌드 시스템) tạo scoped lớp (class / 클래스) names.

Ưu:
- cục bộ (local / 로컬) phạm vi (scope / 범위),
- giảm collision.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **CSS-in-JS** tiếp nhận điểm tựa từ **CSS Modules** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — đơn vị từ (token / 토큰) thiết kế (design tokens)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSS-in-JS

Có nhiều thời gian chạy (runtime / 런타임)/build-time approach. Không nên coi đây là "CSS replacement"; vẫn cần hiểu cơ chế phân tầng (cascade)/bố cục (layout / 레이아웃)/trình duyệt (browser / 브라우저).

---

# 90. Recommended tầng (layer / 계층) kiến trúc (architecture / 아키텍처)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
@layer reset, tokens, base, layout, components, utilities, overrides;
```

Ví dụ responsibility:

```text
reset       → normalize browser defaults
tokens      → design tokens
base        → body, headings, links
layout      → generic page/grid primitives
components  → button/card/modal
utilities   → single-purpose helpers
overrides   → rare integration overrides
```

---

# 91. đơn vị từ (token / 토큰) thiết kế (design tokens)

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — đơn vị từ (token / 토큰) thiết kế (design tokens)** tiếp nhận điểm tựa từ **CSS-in-JS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — thành phần (component / 컴포넌트) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — đơn vị từ (token / 토큰) thiết kế (design tokens)

### CSS Idiom — mang tính ngữ nghĩa (semantic / 의미적) alias

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
--gray-700: #374151;
--color-text-default: var(--gray-700);
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — phân cấp đơn vị từ (token / 토큰) (token hierarchy)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
Foundation token
→ Semantic token
→ Component token
→ State token
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — hợp đồng chủ đề (theme contract)

Theme ưu tiên override mang tính ngữ nghĩa (semantic / 의미적) tokens. thành phần (component / 컴포넌트) tokens chỉ override khi thành phần (component / 컴포넌트) có yêu cầu (requirement / 요구사항) riêng.

```css
:root {
  --color-brand-500: oklch(62% .2 255);
  --color-text: oklch(25% .02 255);
  --color-surface: white;

  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;

  --radius-sm: .375rem;
  --radius-md: .75rem;

  --shadow-sm: 0 1px 2px rgb(0 0 0 / .08);
  --shadow-md: 0 8px 24px rgb(0 0 0 / .12);

  --duration-fast: 120ms;
  --duration-normal: 200ms;
}
```

Cấp cao (senior / 시니어) distinction:
- **toàn cục (global / 전역) đơn vị từ (token / 토큰)**: `--space-4`
- **đơn vị từ (token / 토큰) ngữ nghĩa (semantic token)**: `--color-text-muted`
- **đơn vị từ (token / 토큰) thành phần (component token)**: `--button-bg`

---

# 92. Theme kiến trúc (architecture / 아키텍처)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
:root {
  --surface: #fff;
  --text: #171717;
}

[data-theme="dark"] {
  --surface: #111;
  --text: #f5f5f5;
}

body {
  background: var(--surface);
  color: var(--text);
}
```

Đừng bản sao (copy / 복사) toàn bộ thành phần (component / 컴포넌트) rules trong dark chế độ (mode / 모드); override tokens trước.

---

# 93. thành phần (component / 컴포넌트) trạng thái (state / 상태)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — thành phần (component / 컴포넌트) trạng thái (state / 상태)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — đơn vị từ (token / 토큰) thiết kế (design tokens)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — khả năng tiếp cận (accessibility / 접근성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — thành phần (component / 컴포넌트) trạng thái (state / 상태)

### CSS Idiom — Attribute-driven trạng thái (state / 상태)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.accordion[data-state="open"] {}
.tabs [aria-selected="true"] {}
.button[aria-pressed="true"] {}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — trạng thái (state / 상태) ma trận (matrix / 행렬)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
variant: primary | secondary | danger
size: sm | md | lg
state: default | hover | focus | disabled | loading
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — biến thể (variant)/trạng thái (state / 상태) separation

biến thể (variant) = định danh (identity / 식별자)/style chế độ (mode / 모드).

Trạng thái (state / 상태) = tình trạng thời gian chạy (runtime / 런타임)/tương tác (interaction / 상호작용).

Không trộn thành lớp (class / 클래스) kiểu `.button-danger-disabled`.

Nên encode trạng thái (state / 상태) rõ:

```css
.button[data-variant="danger"] {}
.tabs [aria-selected="true"] {}
.accordion[data-state="open"] {}
```

Ưu tiên trạng thái (state / 상태) từ mang tính ngữ nghĩa (semantic / 의미적) attributes khi có:

```css
button:disabled {}
input:checked {}
[aria-current="page"] {}
```

---

# 94. độ đặc hiệu (specificity) chiến lược (strategy / 전략) [ADV]

Mục tiêu (target / 대상):
- phần lớn các bộ chọn (selectors) low độ đặc hiệu (specificity),
- tránh ID,
- tránh lồng cú pháp (nesting) sâu,
- dùng tầng (layer / 계층),
- dùng `:where()` cho defaults,
- không "đấu độ đặc hiệu (specificity)".

Cơ sở (base / 기반) API:

```css
:where(.prose) h2 {
  margin-block: 2em .75em;
}
```

Người dùng (user / 사용자) override:

```css
.article h2 {
  margin-top: 3rem;
}
```

dễ thắng vì `:where()` = zero độ đặc hiệu (specificity) cho phần đó.

---

# 95. Reset / Normalize

Minimal reset:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  hanging-punctuation: first last;
}

body {
  margin: 0;
  min-height: 100dvh;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}

input,
button,
textarea,
select {
  font: inherit;
}

p,
h1,
h2,
h3,
h4,
h5,
h6 {
  overflow-wrap: break-word;
}
```

Không blindly bản sao (copy / 복사) reset từ internet; hiểu từng line.

---

# 96. khả năng tiếp cận (accessibility / 접근성) [cốt lõi (core / 핵심)/cấp cao (senior / 시니어)]

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — khả năng tiếp cận (accessibility / 접근성)** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — thành phần (component / 컴포넌트) trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Focus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — khả năng tiếp cận (accessibility / 접근성)

### CSS Idiom — Focus-visible ring

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Accessible hidden văn bản (text / 텍스트)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.visually-hidden {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — cải tiến lũy tiến (progressive enhancement)

Cơ sở (base / 기반) experience phải dùng được trước; animation/filter/view-transition là enhancement.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Style đẹp nhưng làm mất focus, cắt văn bản (text / 텍스트) khi zoom hoặc reorder visual khác DOM là regression.

CSS có thể phá khả năng tiếp cận (accessibility / 접근성) dù HTML đúng.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Focus** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — khả năng tiếp cận (accessibility / 접근성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contrast** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Focus

Phải có visible focus:

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Focus** đã nêu tiêu chí phân biệt, còn **Contrast** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **giảm chuyển động (reduced motion)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contrast

Văn bản (text / 텍스트)/background phải có contrast phù hợp theo khả năng tiếp cận (accessibility / 접근성) requirements của dự án (project / 프로젝트).

Không chỉ dựa vào màu để truyền thông tin (information / 정보):

Sai:

```text
red = error
green = success
```

Nên có icon/văn bản (text / 텍스트)/trạng thái (state / 상태) thêm.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Contrast** đã nêu tiêu chí phân biệt, còn **giảm chuyển động (reduced motion)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Zoom** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## giảm chuyển động (reduced motion)

Hỗ trợ (support / 지원):

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-animation {
    animation: none;
  }
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Zoom** tiếp nhận điểm tựa từ **giảm chuyển động (reduced motion)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Visual thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Zoom

Tránh fixed heights làm văn bản (text / 텍스트) bị cut khi người dùng (user / 사용자) zoom/font enlarge.

Sai:

```css
.button {
  height: 30px;
}
```

Tốt hơn:

```css
.button {
  min-height: 2.75rem;
  padding-block: .5rem;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Visual thứ tự (order / 순서)** tiếp nhận điểm tựa từ **Zoom** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hidden content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Visual thứ tự (order / 순서)

Đừng dùng Flex/Grid `order` để tạo visual thứ tự (order / 순서) khác hoàn toàn DOM thứ tự (order / 순서).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Hidden content** tiếp nhận điểm tựa từ **Visual thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hidden content

Các kỹ thuật khác nhau có ngữ nghĩa (semantics / 의미론) khác:

```css
display: none;
visibility: hidden;
opacity: 0;
```

Không interchangeable.

---

# 97. Visually Hidden tiện ích (utility)

Cho content dành cho screen reader nhưng không muốn hiển thị visual:

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

Đừng dùng `display:none` nếu bạn muốn assistive technology đọc content.

---

# 98. màu cưỡng bức (forced colors) / độ tương phản cao (high contrast) [ADV]

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@media (forced-colors: active) {
  .custom-control {
    border: 1px solid CanvasText;
  }
}
```

Không assume colors/shadows luôn được kết xuất (render / 렌더링) như thiết kế (design / 설계).

---

# 99. hiệu năng (performance / 성능) [ADV/cấp cao (senior / 시니어)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **Hidden content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Không micro-optimize bộ chọn (selector) vô nghĩa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — hiệu năng (performance / 성능)

### CSS Idiom — Skip off-screen rendering khi phù hợp

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.long-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 600px;
}
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — Animate compositor-friendly các thuộc tính (properties)

Ưu tiên `opacity` và `transform` khi UX tương đương.

### Mẫu thiết kế (design pattern / 디자인 패턴) — hiệu năng (performance / 성능) ngân sách (budget / 예산)

Theo dõi:
- CSS bundle kích thước (size / 크기),
- font bytes,
- chi phí kết xuất (rendering cost),
- dịch chuyển bố cục (layout shift),
- long animation,
- large filter/backdrop regions.

CSS hiệu năng (performance / 성능) thường liên quan:
- biểu định kiểu (stylesheet / 스타일시트) kích thước (size / 크기),
- unused CSS,
- expensive rendering,
- font loading,
- ảnh (image / 이미지)/background,
- dao động bố cục do đọc/ghi xen kẽ (layout thrashing) từ JS + CSS,
- huge DOM,
- animation,
- tính lại style (style recalculation).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Không micro-optimize bộ chọn (selector) vô nghĩa** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tập trung vào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Không micro-optimize bộ chọn (selector) vô nghĩa

Hiện đại (modern / 현대적) trình duyệt (browser / 브라우저) bộ chọn (selector) engine rất tối ưu. Vấn đề maintainability thường lớn hơn việc `.a > .b` nhanh hơn hay chậm hơn vài microsecond.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Tập trung vào** tiếp nhận điểm tựa từ **Không micro-optimize bộ chọn (selector) vô nghĩa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) notes — gỡ lỗi (debugging)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tập trung vào

1. ship ít CSS hơn,
2. remove unused CSS,
3. split trọng yếu (critical / 중요)/non-critical khi phù hợp,
4. avoid massive toàn cục (global / 전역) rules,
5. optimize font/ảnh (image / 이미지),
6. avoid layout-heavy animation loops,
7. use DevTools hiệu năng (performance / 성능).

---

# 100. chuỗi xử lý kết xuất (rendering pipeline) mô hình tư duy (mental model / 사고 모델) [ADV]

Simplified:

```text
DOM + CSSOM
→ Style
→ Layout
→ Paint
→ Composite
```

Một CSS thay đổi (change / 변경) có thể ảnh hưởng các stage khác nhau.

Ví dụ conceptual:
- `width` → có thể bố cục (layout / 레이아웃) + paint + composite.
- `background` → paint + composite.
- `transform` → thường có thể composite-friendly.
- `opacity` → thường composite-friendly.

Không phải guarantee tuyệt đối; trình duyệt (browser / 브라우저) hiện thực (implementation / 구현)/ngữ cảnh (context / 맥락) matters.

---

# 101. dịch chuyển bố cục (layout shift) [ADV]

Tránh dịch chuyển bố cục (layout shift) bằng:
- `width`/`height` hoặc `aspect-ratio` cho images/media,
- reserve không gian (space / 공간) cho async content,
- font chiến lược (strategy / 전략) phù hợp,
- không inject banner bất ngờ phía trên content.

```css
.card-image {
  aspect-ratio: 16 / 9;
}
```

---

# 102. Font hiệu năng (performance / 성능)

Checklist:
- WOFF2.
- Chỉ tải (load / 로드) weights cần dùng.
- biến (variable) font nếu có lợi.
- `font-display` phù hợp.
- preload only trọng yếu (critical / 중요) font.
- subset unicode nếu large font family.
- hệ thống (system / 시스템) fonts khi thiết kế (design / 설계) cho phép.

---

# 103. CSS gỡ lỗi (debugging) Workflow [cấp cao (senior / 시니어)]

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Mẫu (pattern / 패턴) notes — gỡ lỗi (debugging)** tiếp nhận điểm tựa từ **Tập trung vào** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Step 1 — Inspect element** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) notes — gỡ lỗi (debugging)

### Mẫu lập trình (coding pattern / 코딩 패턴) — ràng buộc (constraint / 제약조건) tracing

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
computed width
→ max/min constraints
→ containing block
→ intrinsic content
→ flex/grid track
→ overflow
```

### Mẫu lập trình (coding pattern / 코딩 패턴) — cơ chế phân tầng (cascade) tracing

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
matched selector?
→ declaration valid?
→ layer?
→ specificity?
→ source order?
→ inheritance?
```

### Mẫu thiết kế (design pattern / 디자인 패턴) — gỡ lỗi (debug / 디버그) from mô hình (model / 모델), not trial-and-error

Tìm hệ thống (system / 시스템) quyết định hành vi (behavior / 동작):
- cơ chế phân tầng (cascade),
- ngữ cảnh định dạng (formatting context / 서식 컨텍스트),
- sizing thuật toán (algorithm / 알고리즘),
- positioning,
- stacking.

Khi bố cục (layout / 레이아웃) sai:

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Step 1 — Inspect element** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) notes — gỡ lỗi (debugging)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Step 2 — mô hình hộp (box model / 박스 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Step 1 — Inspect element

DevTools:
- bộ chọn (selector) matched?
- thuộc tính (property / 속성) bị strike-through?
- computed giá trị (value / 값)?
- inherited từ đâu?

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Step 2 — mô hình hộp (box model / 박스 모델)** tiếp nhận điểm tựa từ **Step 1 — Inspect element** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Step 3 — bố cục (layout / 레이아웃) ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Step 2 — mô hình hộp (box model / 박스 모델)

Check:
- content kích thước (size / 크기),
- padding,
- border,
- margin.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Step 3 — bố cục (layout / 레이아웃) ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **Step 2 — mô hình hộp (box model / 박스 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Step 4 — các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Step 3 — bố cục (layout / 레이아웃) ngữ cảnh (context / 맥락)

Element là:
- khối (block / 블록)?
- phần tử Flex (flex item)?
- phần tử Grid (grid item)?
- positioned?
- vùng chứa cuộn (scroll container)?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Step 4 — các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **Step 3 — bố cục (layout / 레이아웃) ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Step 5 — Position ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Step 4 — các ràng buộc (constraints / 제약조건들)

Check:
- min/max width/height,
- `min-width:auto`,
- định cỡ nội tại (intrinsic sizing / 내재 크기 결정),
- overflow,
- aspect ratio.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Step 5 — Position ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **Step 4 — các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Step 6 — trình duyệt (browser / 브라우저) responsive modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Step 5 — Position ngữ cảnh (context / 맥락)

Check:
- khối chứa tham chiếu (containing block / 컨테이닝 블록),
- ngữ cảnh xếp chồng (stacking context / 쌓임 맥락),
- clipping ancestor.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Step 6 — trình duyệt (browser / 브라우저) responsive modes** tiếp nhận điểm tựa từ **Step 5 — Position ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bug 1 — z-index không chạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Step 6 — trình duyệt (browser / 브라우저) responsive modes

Kiểm thử (test / 테스트):
- narrow vùng nhìn (viewport),
- zoom,
- long văn bản (text / 텍스트),
- translated văn bản (text / 텍스트),
- keyboard focus,
- giảm chuyển động (reduced motion),
- dark chế độ (mode / 모드).

---

# 104. gỡ lỗi (debug / 디버그) Helpers

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
* {
  outline: 1px solid rgb(255 0 0 / .1);
}
```

Hoặc targeted:

```css
.debug {
  outline: 2px solid magenta !important;
}
```

Grid/Flex overlays trong Chrome/Firefox DevTools cực hữu ích.

---

# 105. dùng chung (common / 공통) CSS Bugs cấp cao (senior / 시니어) phải nhận ra ngay

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 1 — z-index không chạy** tiếp nhận điểm tựa từ **Step 6 — trình duyệt (browser / 브라우저) responsive modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bug 2 — Flex child overflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 1 — `z-index` không chạy

Cause thường:
- ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) parent,
- `z-index` chưa applicable theo ngữ cảnh (context / 맥락),
- clipping.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 1 — z-index không chạy** xác định đầu vào; **Bug 2 — Flex child overflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bug 3 — Vertical flex scroll không chạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 2 — Flex child overflow

Fix thường:

```css
.child {
  min-width: 0;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 2 — Flex child overflow** xác định đầu vào; **Bug 3 — Vertical flex scroll không chạy** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bug 4 — position: sticky không stick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 3 — Vertical flex scroll không chạy

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.panel {
  display: flex;
  flex-direction: column;
  height: 100dvh;
}

.content {
  min-height: 0;
  overflow: auto;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 4 — position: sticky không stick** tiếp nhận điểm tựa từ **Bug 3 — Vertical flex scroll không chạy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bug 5 — height:100% không có tác dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 4 — `position: sticky` không stick

Check:
- có inset `top`?
- ancestor overflow?
- vùng chứa cuộn (scroll container) nào?
- parent height?

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 5 — height:100% không có tác dụng** tiếp nhận điểm tựa từ **Bug 4 — position: sticky không stick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bug 6 — Ellipsis không chạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 5 — `height:100%` không có tác dụng

Percentage height cần khối chứa tham chiếu (containing block / 컨테이닝 블록) có definite height trong nhiều bố cục (layout / 레이아웃) cases.

Dùng đúng ngữ cảnh (context / 맥락) hoặc:

```css
min-height: 100dvh;
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 6 — Ellipsis không chạy** tiếp nhận điểm tựa từ **Bug 5 — height:100% không có tác dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bug 7 — margin:auto tưởng luôn center** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 6 — Ellipsis không chạy

Cần các ràng buộc (constraints / 제약조건들):

```css
.text {
  min-width: 0;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 7 — margin:auto tưởng luôn center** tiếp nhận điểm tựa từ **Bug 6 — Ellipsis không chạy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bug 8 — absolute element "bay" sai nơi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 7 — `margin:auto` tưởng luôn center

Auto margins hoạt động khác nhau tùy ngữ cảnh định dạng (formatting context / 서식 컨텍스트)/axis/available không gian dư (free space).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bug 8 — absolute element "bay" sai nơi** tiếp nhận điểm tựa từ **Bug 7 — margin:auto tưởng luôn center** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fluid bộ chứa (container / 컨테이너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bug 8 — absolute element "bay" sai nơi

Khối chứa tham chiếu (containing block / 컨테이닝 블록) không phải ancestor bạn nghĩ.

---

# 106. Responsive bố cục (layout / 레이아웃) Recipes

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Fluid bộ chứa (container / 컨테이너)** tiếp nhận điểm tựa từ **Bug 8 — absolute element "bay" sai nơi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Auto-responsive cards** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fluid bộ chứa (container / 컨테이너)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Auto-responsive cards** tiếp nhận điểm tựa từ **Fluid bộ chứa (container / 컨테이너)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sidebar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Auto-responsive cards

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.cards {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 1rem;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Sidebar** tiếp nhận điểm tựa từ **Auto-responsive cards** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sticky sidebar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sidebar

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.layout {
  display: grid;
  grid-template-columns:
    minmax(0, 18rem)
    minmax(0, 1fr);
  gap: 2rem;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Sticky sidebar** tiếp nhận điểm tựa từ **Sidebar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bố cục (layout / 레이아웃)/math** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sticky sidebar

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.sidebar {
  align-self: start;
  position: sticky;
  top: 1rem;
}
```

---

# 107. Modal Recipe

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 1rem;
  background: rgb(0 0 0 / .5);
}

.modal {
  width: min(100%, 36rem);
  max-height: min(80dvh, 50rem);
  overflow: auto;
  border-radius: 1rem;
  background: white;
}
```

Trong môi trường vận hành (production / 운영 환경) ưu tiên bản địa (native / 네이티브) `<dialog>`/popover khi ngữ nghĩa (semantics / 의미론) phù hợp thay vì recreate mọi hành vi (behavior / 동작) bằng div.

---

# 108. Tooltip / Dropdown — cấp cao (senior / 시니어) considerations

CSS bố cục (layout / 레이아웃) chỉ là một phần.

Cần nghĩ:
- định vị theo điểm neo (anchor positioning),
- vùng nhìn (viewport) collision,
- keyboard,
- quản lý tiêu điểm (focus management),
- escape key,
- ARIA ngữ nghĩa (semantics / 의미론),
- portal/lớp trên cùng (top layer),
- scroll clipping.

Không giải quyết complex overlay chỉ bằng `position:absolute; z-index:99999`.

---

# 109. lớp trên cùng (top layer) [ADV]

Một số browser-managed UI như dialog/popover có thể được đặt vào **lớp trên cùng (top layer)**, vượt các ngữ cảnh xếp chồng (stacking contexts) bình thường.

Điều này giải thích tại sao z-index mô hình (model / 모델) của bản địa (native / 네이티브) dialog/popover khác div modal bình thường.

phần tử giả (pseudo-element) liên quan backdrop:

```css
dialog::backdrop {
  background: rgb(0 0 0 / .5);
}
```

---

# 110. CSS and Shadow DOM (cây DOM đóng gói) [ADV]

Shadow DOM (cây DOM đóng gói) tạo style đóng gói (encapsulation).

Concept cần biết:
- shadow cây (tree / 트리),
- `:host`,
- `:host(...)`,
- `::part(...)`,
- CSS custom các thuộc tính (properties) xuyên ranh giới (boundary / 경계) theo kế thừa (inheritance)/cơ chế phân tầng (cascade) rules phù hợp.

Example:

```css
:host {
  display: block;
}

button {
  color: var(--button-color, currentColor);
}
```

Bên tiêu thụ (consumer / 소비자) có thể style exposed part:

```css
my-component::part(button) {}
```

---

# 111. Print CSS [ADV]

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
@media print {
  nav,
  .ads {
    display: none;
  }

  a {
    color: black;
    text-decoration: underline;
  }
}
```

`@page` có thể điều khiển page-related styles trong print contexts.

---

# 112. CSS các hàm (functions) nên biết

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bố cục (layout / 레이아웃)/math** tiếp nhận điểm tựa từ **Sticky sidebar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **các biến (variables)/môi trường (environment / 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bố cục (layout / 레이아웃)/math

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
calc()
min()
max()
clamp()
minmax()
repeat()
fit-content()
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **các biến (variables)/môi trường (environment / 환경)** tiếp nhận điểm tựa từ **Bố cục (layout / 레이아웃)/math** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## các biến (variables)/môi trường (environment / 환경)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
var()
env()
attr()
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Color** tiếp nhận điểm tựa từ **các biến (variables)/môi trường (environment / 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Images** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Color

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
rgb()
hsl()
hwb()
lab()
lch()
oklab()
oklch()
color()
color-mix()
light-dark()
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Images** tiếp nhận điểm tựa từ **Color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transform** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Images

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
linear-gradient()
radial-gradient()
conic-gradient()
image-set()
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Transform** tiếp nhận điểm tựa từ **Images** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Filters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transform

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
translate()
scale()
rotate()
matrix()
perspective()
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Filters** tiếp nhận điểm tựa từ **Transform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Shapes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Filters

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
blur()
brightness()
contrast()
drop-shadow()
grayscale()
hue-rotate()
invert()
saturate()
sepia()
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Shapes** tiếp nhận điểm tựa từ **Filters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bố cục (layout / 레이아웃) / Box** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Shapes

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
circle()
ellipse()
inset()
polygon()
path()
```

---

# 113. CSS toàn cục (global / 전역) Keywords — phải nhớ

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
inherit
initial
unset
revert
revert-layer
```

Ngoài ra CSS-wide từ khóa (keyword / 키워드) thường có `initial`, `inherit`, `unset`, `revert`, `revert-layer`.

---

# 114. thuộc tính (property / 속성) chỉ mục (index / 인덱스) theo nhóm

Đây chỉ là appendix để tra cứu sau khi đã hiểu mô hình tư duy (mental model / 사고 모델) ở các phần trước. Không dùng section này như lộ trình học (learning path / 학습 경로) và không học thuộc thuộc tính (property / 속성) theo kiểu danh sách.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bố cục (layout / 레이아웃) / Box** tiếp nhận điểm tựa từ **Shapes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Position / stacking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bố cục (layout / 레이아웃) / Box

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
display
box-sizing
width
height
min-width
min-height
max-width
max-height
aspect-ratio
margin
margin-top/right/bottom/left
padding
padding-top/right/bottom/left
overflow
overflow-x
overflow-y
overflow-anchor
visibility
opacity
contain
content-visibility
contain-intrinsic-size
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Position / stacking** tiếp nhận điểm tựa từ **Bố cục (layout / 레이아웃) / Box** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Flexbox** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Position / stacking

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
position
top
right
bottom
left
inset
z-index
isolation
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Flexbox** tiếp nhận điểm tựa từ **Position / stacking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Grid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Flexbox

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
flex
flex-basis
flex-grow
flex-shrink
flex-direction
flex-wrap
flex-flow
justify-content
align-items
align-content
align-self
order
gap
row-gap
column-gap
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Grid** tiếp nhận điểm tựa từ **Flexbox** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Typography** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Grid

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
grid
grid-template
grid-template-columns
grid-template-rows
grid-template-areas
grid-auto-columns
grid-auto-rows
grid-auto-flow
grid-column
grid-column-start
grid-column-end
grid-row
grid-row-start
grid-row-end
grid-area
justify-items
align-items
place-items
justify-self
align-self
place-self
justify-content
align-content
place-content
gap
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Typography** tiếp nhận điểm tựa từ **Grid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Color / background** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Typography

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
font
font-family
font-size
font-style
font-weight
font-stretch
font-variant
font-feature-settings
font-variation-settings
line-height
letter-spacing
word-spacing
text-align
text-transform
text-indent
text-decoration
text-decoration-line
text-decoration-style
text-decoration-color
text-decoration-thickness
text-underline-offset
text-shadow
text-overflow
text-wrap
white-space
word-break
overflow-wrap
hyphens
vertical-align
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Color / background** tiếp nhận điểm tựa từ **Typography** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Border / visual** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Color / background

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
color
background
background-color
background-image
background-size
background-position
background-repeat
background-attachment
background-origin
background-clip
color-scheme
accent-color
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Border / visual** tiếp nhận điểm tựa từ **Color / background** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Images / replaced content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Border / visual

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
border
border-width
border-style
border-color
border-radius
border-top/right/bottom/left
outline
outline-width
outline-style
outline-color
outline-offset
box-shadow
filter
backdrop-filter
mix-blend-mode
background-blend-mode
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Images / replaced content** tiếp nhận điểm tựa từ **Border / visual** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transform / animation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Images / replaced content

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
object-fit
object-position
image-rendering
aspect-ratio
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Transform / animation** tiếp nhận điểm tựa từ **Images / replaced content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scroll** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transform / animation

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
transform
transform-origin
transform-style
translate
rotate
scale
perspective
perspective-origin
backface-visibility
transition
transition-property
transition-duration
transition-timing-function
transition-delay
transition-behavior
animation
animation-name
animation-duration
animation-timing-function
animation-delay
animation-iteration-count
animation-direction
animation-fill-mode
animation-play-state
animation-timeline
animation-range
will-change
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Scroll** tiếp nhận điểm tựa từ **Transform / animation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **UI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scroll

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
scroll-behavior
scroll-snap-type
scroll-snap-align
scroll-snap-stop
scroll-margin
scroll-padding
overscroll-behavior
scrollbar-color
scrollbar-width
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **UI** tiếp nhận điểm tựa từ **Scroll** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Danh sách (list / 목록) / counters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## UI

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
appearance
cursor
pointer-events
user-select
resize
caret-color
touch-action
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Danh sách (list / 목록) / counters** tiếp nhận điểm tựa từ **UI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảng (table / 테이블)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Danh sách (list / 목록) / counters

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
list-style
list-style-type
list-style-position
list-style-image
counter-reset
counter-increment
counter-set
content
quotes
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Bảng (table / 테이블)** tiếp nhận điểm tựa từ **Danh sách (list / 목록) / counters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Columns / fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảng (table / 테이블)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
border-collapse
border-spacing
table-layout
caption-side
empty-cells
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Columns / fragmentation** tiếp nhận điểm tựa từ **Bảng (table / 테이블)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **thuộc tính lô-gic (logic / 논리) (logical properties)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Columns / fragmentation

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
columns
column-count
column-width
column-gap
column-rule
column-span
break-before
break-after
break-inside
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **thuộc tính lô-gic (logic / 논리) (logical properties)** tiếp nhận điểm tựa từ **Columns / fragmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Writing / direction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## thuộc tính lô-gic (logic / 논리) (logical properties)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
inline-size
block-size
min-inline-size
max-inline-size
min-block-size
max-block-size
margin-inline
margin-block
padding-inline
padding-block
inset-inline
inset-block
border-inline
border-block
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Writing / direction** tiếp nhận điểm tựa từ **thuộc tính lô-gic (logic / 논리) (logical properties)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Shape / clipping / mask** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Writing / direction

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
writing-mode
direction
unicode-bidi
text-orientation
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Shape / clipping / mask** tiếp nhận điểm tựa từ **Writing / direction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiện đại (modern / 현대적) thành phần (component / 컴포넌트)/responsive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Shape / clipping / mask

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
clip-path
shape-outside
shape-margin
mask
mask-image
mask-size
mask-position
mask-repeat
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Hiện đại (modern / 현대적) thành phần (component / 컴포넌트)/responsive** tiếp nhận điểm tựa từ **Shape / clipping / mask** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiện đại (modern / 현대적) thành phần (component / 컴포넌트)/responsive

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
container
container-name
container-type
anchor-name
position-anchor
view-transition-name
```

---

# 115. bộ chọn (selector) chỉ mục (index / 인덱스) cần thành thạo

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
*
element
.class
#id
[attr]
[attr=value]
A B
A > B
A + B
A ~ B

:hover
:active
:focus
:focus-visible
:focus-within
:checked
:disabled
:enabled
:required
:optional
:valid
:invalid
:first-child
:last-child
:nth-child()
:nth-of-type()
:not()
:is()
:where()
:has()
:empty
:target
:root
:scope
:lang()

::before
::after
::marker
::selection
::placeholder
::first-letter
::first-line
::file-selector-button
::backdrop
```

---

# 116. At-rule chỉ mục (index / 인덱스) cần thành thạo

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```text
@media
@supports
@container
@layer
@scope
@property
@font-face
@keyframes
@starting-style
@view-transition
@counter-style
@page
@import
```

---

# 117. CSS cấp cao (senior / 시니어) Checklist trước khi merge PR

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **Hiện đại (modern / 현대적) thành phần (component / 컴포넌트)/responsive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Responsive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đúng đắn (correctness / 정확성)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- bộ chọn (selector) có quá rộng không?
- Có dựa vào DOM lồng cú pháp (nesting) fragile không?
- Có độ đặc hiệu (specificity) escalation không?
- Có `!important` không cần thiết không?
- Có toàn cục (global / 전역) tác dụng phụ (side effect) không?
- Long văn bản (text / 텍스트) có break bố cục (layout / 레이아웃) không?
- Loading trạng thái (state / 상태)/empty trạng thái (state / 상태)/lỗi (error / 오류) trạng thái (state / 상태) ổn không?

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Responsive** tiếp nhận điểm tựa từ **Tính đúng đắn (correctness / 정확성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng tiếp cận (accessibility / 접근성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Responsive

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

- 320px-ish narrow layout?
- Tablet?
- Wide screen?
- Content translated dài hơn?
- Zoom 200%?
- orientation thay đổi (change / 변경)?
- thành phần (component / 컴포넌트) trong bộ chứa (container / 컨테이너) khác?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Khả năng tiếp cận (accessibility / 접근성)** tiếp nhận điểm tựa từ **Responsive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tiếp cận (accessibility / 접근성)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- focus visible?
- keyboard?
- giảm chuyển động (reduced motion)?
- độ tương phản cao (high contrast)?
- trạng thái (state / 상태) không chỉ dựa vào color?
- visual thứ tự (order / 순서) = logical thứ tự (order / 순서)?

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **Khả năng tiếp cận (accessibility / 접근성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu năng (performance / 성능)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- animation thuộc tính (property) hợp lý?
- có giant shadow/filter/backdrop blur trên vùng lớn?
- unused CSS?
- font weights thừa?
- ảnh (image / 이미지) dimensions reserved?

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1. !important everywhere** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến trúc (architecture / 아키텍처)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

- dùng token thay hard-code khi mang tính ngữ nghĩa (semantic)?
- component trạng thái (state) API rõ?
- tiện ích (utility)/component responsibility rõ?
- layer đúng?
- có thể override mà không cuộc chiến độ đặc hiệu (specificity war)?

---

# 118. Những phản mẫu (anti-pattern) cần bỏ

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **1. !important everywhere** tiếp nhận điểm tựa từ **Kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. Magic z-index** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. `!important` everywhere

Sai:

```css
.btn {
  color: red !important;
}
```

Hãy sửa cơ chế phân tầng (cascade) kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **2. Magic z-index** tiếp nhận điểm tựa từ **1. !important everywhere** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Fixed điểm ảnh (pixel / 픽셀) everything** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Magic z-index

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
z-index: 999999999;
```

Không sửa được ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) cha.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **3. Fixed điểm ảnh (pixel / 픽셀) everything** tiếp nhận điểm tựa từ **2. Magic z-index** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. DOM-coupled bộ chọn (selector)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Fixed điểm ảnh (pixel / 픽셀) everything

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
width: 1200px;
height: 600px;
```

Dễ phá responsive/zoom/content.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **4. DOM-coupled bộ chọn (selector)** tiếp nhận điểm tựa từ **3. Fixed điểm ảnh (pixel / 픽셀) everything** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. transition: all** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. DOM-coupled bộ chọn (selector)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
main > div > div:nth-child(2) span {}
```

Rất fragile.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **5. transition: all** tiếp nhận điểm tựa từ **4. DOM-coupled bộ chọn (selector)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Remove focus outline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. `transition: all`

Animate unintended changes.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **6. Remove focus outline** tiếp nhận điểm tựa từ **5. transition: all** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Absolute positioning để làm toàn bộ bố cục (layout / 레이아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Remove focus outline

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
outline: none;
```

mà không replacement.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **7. Absolute positioning để làm toàn bộ bố cục (layout / 레이아웃)** tiếp nhận điểm tựa từ **6. Remove focus outline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. truy vấn môi trường (media query) theo thiết bị (device / 장치) names** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Absolute positioning để làm toàn bộ bố cục (layout / 레이아웃)

Dùng Grid/Flex trước.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **8. truy vấn môi trường (media query) theo thiết bị (device / 장치) names** tiếp nhận điểm tựa từ **7. Absolute positioning để làm toàn bộ bố cục (layout / 레이아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. JavaScript cho vấn đề CSS giải được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. truy vấn môi trường (media query) theo thiết bị (device / 장치) names

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
@media (...) /* iPhone 14 */
```

Hãy chọn điểm ngắt (breakpoint) theo content/bố cục (layout / 레이아웃), không theo tên thiết bị.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **9. JavaScript cho vấn đề CSS giải được** tiếp nhận điểm tựa từ **8. truy vấn môi trường (media query) theo thiết bị (device / 장치) names** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 1–3 — cốt lõi (core / 핵심) mechanics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. JavaScript cho vấn đề CSS giải được

Ví dụ nhiều bố cục (layout / 레이아웃) responsive/trạng thái (state / 상태) hiện có thể dùng:
- `:has()`
- truy vấn vùng chứa (container query)
- Grid
- `clamp()`
- bản địa (native / 네이티브) lồng cú pháp (nesting)
- định vị theo điểm neo (anchor positioning).

---

# 119. Học CSS như cấp cao (senior / 시니어): 20 bài tập bắt buộc

1. Recreate card từ screenshot không dùng khung phần mềm (framework / 프레임워크).
2. Navbar responsive bằng Flexbox.
3. Dashboard bố cục (layout / 레이아웃) bằng Grid.
4. sản phẩm (product / 제품) grid auto-fit không điểm ngắt (breakpoint).
5. Sticky header + sticky sidebar.
6. Modal scroll đúng khi content dài.
7. Truncate văn bản (text / 텍스트) trong flex child.
8. bảng (table / 테이블) responsive.
9. Form kiểm tra hợp lệ (validation / 검증) styles.
10. Accessible focus các trạng thái (states).
11. Dark theme bằng custom các thuộc tính (properties).
12. đơn vị từ (token / 토큰) thiết kế (design token) hệ thống (system / 시스템).
13. thành phần (component / 컴포넌트) responsive bằng truy vấn vùng chứa (container query).
14. Tooltip/dropdown với định vị theo điểm neo (anchor positioning) + phương án dự phòng (fallback).
15. Card row alignment bằng subgrid.
16. Animation respect giảm chuyển động (reduced motion).
17. Scroll snap carousel.
18. Scroll-driven reading progress.
19. bản địa (native / 네이티브) CSS lồng cú pháp (nesting) refactor.
20. `@layer` refactor dự án (project / 프로젝트) có vendor CSS.

---

# 120. Roadmap 30 ngày

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 1–3 — cốt lõi (core / 핵심) mechanics** tiếp nhận điểm tựa từ **9. JavaScript cho vấn đề CSS giải được** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 4–6 — Box/bố cục (layout / 레이아웃) fundamentals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 1–3 — cốt lõi (core / 핵심) mechanics

Học:
- cú pháp (syntax / 문법),
- các bộ chọn (selectors),
- cơ chế phân tầng (cascade),
- độ đặc hiệu (specificity),
- kế thừa (inheritance),
- các giá trị (values)/units.

Đầu ra (output / 출력):
- 20 bộ chọn (selector) examples,
- độ đặc hiệu (specificity) playground.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 4–6 — Box/bố cục (layout / 레이아웃) fundamentals** tiếp nhận điểm tựa từ **Ngày 1–3 — cốt lõi (core / 핵심) mechanics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 7–9 — Positioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 4–6 — Box/bố cục (layout / 레이아웃) fundamentals

Học:
- mô hình hộp (box model / 박스 모델),
- sizing,
- display,
- luồng bố cục thông thường (normal flow / 일반 흐름),
- overflow.

Đầu ra (output / 출력):
- article bố cục (layout / 레이아웃),
- cards,
- truncation cases.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 7–9 — Positioning** tiếp nhận điểm tựa từ **Ngày 4–6 — Box/bố cục (layout / 레이아웃) fundamentals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 10–13 — Flexbox** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 7–9 — Positioning

Học:
- relative/absolute/fixed/sticky,
- khối chứa tham chiếu (containing block / 컨테이닝 블록),
- z-index,
- ngữ cảnh xếp chồng (stacking context / 쌓임 맥락).

Đầu ra (output / 출력):
- sticky header,
- modal,
- dropdown.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 10–13 — Flexbox** tiếp nhận điểm tựa từ **Ngày 7–9 — Positioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 14–17 — Grid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 10–13 — Flexbox

Đầu ra (output / 출력):
- navbar,
- toolbar,
- media đối tượng (object / 객체),
- responsive card row.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 14–17 — Grid** tiếp nhận điểm tựa từ **Ngày 10–13 — Flexbox** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 18–19 — Typography & visual** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 14–17 — Grid

Đầu ra (output / 출력):
- dashboard,
- gallery,
- auto-fit cards,
- named areas,
- subgrid.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 18–19 — Typography & visual** tiếp nhận điểm tựa từ **Ngày 14–17 — Grid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 20–21 — Responsive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 18–19 — Typography & visual

Học:
- fonts,
- wrapping,
- colors,
- backgrounds,
- borders,
- shadows,
- gradients.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 20–21 — Responsive** tiếp nhận điểm tựa từ **Ngày 18–19 — Typography & visual** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 22–23 — Motion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 20–21 — Responsive

Học:
- fluid thiết kế (design / 설계),
- các truy vấn môi trường (media queries),
- người dùng (user / 사용자) preferences,
- các truy vấn vùng chứa (container queries).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 22–23 — Motion** tiếp nhận điểm tựa từ **Ngày 20–21 — Responsive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 24–25 — Tokens & kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 22–23 — Motion

Học:
- transforms,
- chuyển tiếp (transition / 전이),
- keyframes,
- scroll snap,
- giảm chuyển động (reduced motion).

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 24–25 — Tokens & kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Ngày 22–23 — Motion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 26–27 — hiện đại (modern / 현대적) CSS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 24–25 — Tokens & kiến trúc (architecture / 아키텍처)

Học:
- custom các thuộc tính (properties),
- `@property`,
- naming,
- layers,
- thành phần (component / 컴포넌트) trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 26–27 — hiện đại (modern / 현대적) CSS** tiếp nhận điểm tựa từ **Ngày 24–25 — Tokens & kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 28 — khả năng tiếp cận (accessibility / 접근성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 26–27 — hiện đại (modern / 현대적) CSS

Học:
- lồng cú pháp (nesting),
- `:has()`,
- `@scope`,
- định vị theo điểm neo (anchor positioning),
- chuyển cảnh giao diện (view transitions),
- hoạt ảnh điều khiển bằng cuộn (scroll-driven animations),
- hiện đại (modern / 현대적) colors.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 28 — khả năng tiếp cận (accessibility / 접근성)** tiếp nhận điểm tựa từ **Ngày 26–27 — hiện đại (modern / 현대적) CSS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 29 — hiệu năng (performance / 성능)/gỡ lỗi (debugging)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 28 — khả năng tiếp cận (accessibility / 접근성)

Kiểm thử (test / 테스트):
- keyboard,
- zoom,
- focus,
- giảm chuyển động (reduced motion),
- contrast,
- RTL/logical props.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 29 — hiệu năng (performance / 성능)/gỡ lỗi (debugging)** tiếp nhận điểm tựa từ **Ngày 28 — khả năng tiếp cận (accessibility / 접근성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngày 30 — Final dự án (project / 프로젝트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 29 — hiệu năng (performance / 성능)/gỡ lỗi (debugging)

DevTools:
- Computed styles,
- Flex/Grid overlay,
- Layers,
- hiệu năng (performance / 성능),
- Rendering.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ngày 30 — Final dự án (project / 프로젝트)** tiếp nhận điểm tựa từ **Ngày 29 — hiệu năng (performance / 성능)/gỡ lỗi (debugging)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.1 Fluid centered bộ chứa (container / 컨테이너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngày 30 — Final dự án (project / 프로젝트)

Bản dựng (build / 빌드):
- responsive dashboard,
- dark/light theme,
- modal/dialog,
- dropdown/popover,
- cards,
- forms,
- bảng (table / 테이블),
- motion,
- no CSS khung phần mềm (framework / 프레임워크).

---

# 121. CSS → SCSS: phần nào để dành cho tài liệu SCSS sau

Sau khi nắm CSS này, tài liệu SCSS không cần lặp lại Flex/Grid/mô hình hộp (box model / 박스 모델).

SCSS nên tập trung vào:

```text
Sass syntax
variables
nesting
parent selector &
partials/modules
@use
@forward
mixins
@include
functions
@if / @else
@for
@each
@while
maps
lists
interpolation
placeholder selectors
@extend
Sass module architecture
design token generation
utility generation
compile/build pipeline
migration từ @import → @use
CSS custom properties vs Sass variables
khi nào KHÔNG nên dùng Sass feature
```

**cấp cao (senior / 시니어) distinction quan trọng:**

```text
Sass variable
→ compile-time

CSS custom property
→ runtime, cascade, inheritance, themeable
```

Ví dụ:

```scss
$spacing: 16px;
```

compile xong không còn `$spacing`.

Trong khi:

```css
--spacing: 1rem;
```

vẫn tồn tại trong trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) và override được.

---

# 122. Kiến thức bạn phải giải thích được nếu muốn tự đánh giá "cấp cao (senior / 시니어) CSS"

Bạn nên trả lời rõ được các câu sau:

1. cơ chế phân tầng (cascade) chọn quy tắc (rule / 규칙) thắng như thế nào?
2. `:is()` và `:where()` khác độ đặc hiệu (specificity) ra sao?
3. Tại sao `z-index:999999` vẫn có thể nằm dưới element khác?
4. khối chứa tham chiếu (containing block / 컨테이닝 블록) của absolute/fixed được xác định thế nào?
5. Tại sao phần tử Flex (flex item) cần `min-width:0`?
6. `1fr` khác `minmax(0,1fr)` trong trường hợp biên (edge case / 경계 사례) nào?
7. `auto-fit` và `auto-fill` khác nhau thế nào?
8. Grid khác Flex theo mô hình tư duy (mental model / 사고 모델) nào?
9. Tại sao `height:100%` thường "không chạy"?
10. gộp lề (margin collapse) là gì?
11. `overflow:hidden` ảnh hưởng scroll/sticky như thế nào?
12. BFC/ngữ cảnh định dạng (formatting context / 서식 컨텍스트) giải quyết vấn đề gì?
13. ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) được tạo bởi những gì?
14. truy vấn vùng chứa (container query) tốt hơn truy vấn môi trường (media query) ở trường hợp nào?
15. `rem`, `em`, `dvh`, `cqi` dùng khi nào?
16. `min-content`, `max-content`, `fit-content` là gì?
17. `@layer` giải quyết độ đặc hiệu (specificity) kiến trúc (architecture / 아키텍처) thế nào?
18. `@scope` khác CSS Modules/Shadow DOM (cây DOM đóng gói) như thế nào về concept?
19. `@property` hơn custom thuộc tính (property / 속성) thường ở đâu?
20. `oklch()` có lợi gì cho hệ thống thiết kế (design system)?
21. CSS lồng cú pháp (nesting) bản địa (native / 네이티브) khác SCSS lồng cú pháp (nesting) về thời gian chạy (runtime / 런타임)/bản dựng (build / 빌드) tooling thế nào?
22. Animation nào dễ gây bố cục (layout / 레이아웃)/chi phí vẽ (paint cost)?
23. `opacity:0`, `visibility:hidden`, `display:none` khác nhau gì?
24. Focus khả năng tiếp cận (accessibility / 접근성) nên style thế nào?
25. thuộc tính lô-gic (logic / 논리) (logical properties) giải quyết vấn đề gì?
26. Khi nào nên dùng `contain`/`content-visibility`?
27. Cách gỡ lỗi (debug / 디버그) sticky?
28. Cách gỡ lỗi (debug / 디버그) văn bản (text / 텍스트) overflow trong flex/grid?
29. Cách thiết kế đơn vị từ (token / 토큰) thiết kế (design tokens)?
30. Cách chia tầng (layer / 계층)/components/các tiện ích (utilities) để không cuộc chiến độ đặc hiệu (specificity war)?

Nếu chưa giải thích được các câu này, hãy quay lại phần tương ứng thay vì học thêm khung phần mềm (framework / 프레임워크) CSS.

---

# 123. Tài liệu tham khảo chuẩn nên bookmark

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

- MDN CSS Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
- MDN CSS Guides: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides
- web.dev Learn CSS: https://web.dev/learn/css/
- W3C CSS specifications: https://www.w3.org/Style/CSS/
- Can I Use: https://caniuse.com/

Khi dùng tính năng (feature / 기능) hiện đại, luôn kiểm tra **trình duyệt (browser / 브라우저) targets của dự án (project / 프로젝트)**, không chỉ nhìn thấy cú pháp (syntax / 문법) mới rồi dùng ngay.

---

# 124. Appendix — cú pháp (syntax / 문법) recap cực ngắn

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
/* Reset */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Tokens */
:root {
  --brand: oklch(62% .2 255);
  --space: 1rem;
}

/* Fluid container */
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}

/* Flex */
.flex {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 1rem;
}

/* Truncate flex child */
.min-w-0 {
  min-width: 0;
}

/* Sticky */
.sticky {
  position: sticky;
  top: 0;
}

/* Aspect ratio */
.media {
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

/* Fluid type */
.title {
  font-size: clamp(1.5rem, 1rem + 2vw, 3rem);
  text-wrap: balance;
}

/* Focus */
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}

/* Component query */
.wrapper {
  container-type: inline-size;
}

@container (width >= 32rem) {
  .card {
    display: grid;
    grid-template-columns: 10rem 1fr;
  }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .motion {
    animation: none;
    transition: none;
  }
}
```

---

# 125. danh mục (catalog / 카탈로그) — CSS ngôn ngữ (language / 언어) Idioms quan trọng phải nhớ

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.1 Fluid centered bộ chứa (container / 컨테이너)** tiếp nhận điểm tựa từ **Ngày 30 — Final dự án (project / 프로젝트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.2 ngăn xếp (stack / 스택)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.1 Fluid centered bộ chứa (container / 컨테이너)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.2 ngăn xếp (stack / 스택)** tiếp nhận điểm tựa từ **125.1 Fluid centered bộ chứa (container / 컨테이너)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.3 Cluster** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.2 ngăn xếp (stack / 스택)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--stack-gap, 1rem);
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.3 Cluster** tiếp nhận điểm tựa từ **125.2 ngăn xếp (stack / 스택)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.4 Center** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.3 Cluster

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--cluster-gap, .75rem);
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.4 Center** tiếp nhận điểm tựa từ **125.3 Cluster** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.5 Cover vùng nhìn (viewport)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.4 Center

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.center {
  display: grid;
  place-items: center;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.5 Cover vùng nhìn (viewport)** tiếp nhận điểm tựa từ **125.4 Center** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.6 Sidebar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.5 Cover vùng nhìn (viewport)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.cover {
  min-height: 100dvh;
  display: grid;
  place-items: center;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.6 Sidebar** tiếp nhận điểm tựa từ **125.5 Cover vùng nhìn (viewport)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.7 Auto grid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.6 Sidebar

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.with-sidebar {
  display: grid;
  grid-template-columns:
    minmax(12rem, 18rem)
    minmax(0, 1fr);
  gap: 2rem;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.7 Auto grid** tiếp nhận điểm tựa từ **125.6 Sidebar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.8 Media đối tượng (object / 객체)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.7 Auto grid

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.auto-grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 1rem;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.8 Media đối tượng (object / 객체)** tiếp nhận điểm tựa từ **125.7 Auto grid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.9 Push hành động (action / 동작) right** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.8 Media đối tượng (object / 객체)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.media {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 1rem;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.9 Push hành động (action / 동작) right** tiếp nhận điểm tựa từ **125.8 Media đối tượng (object / 객체)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.10 Safe flex văn bản (text / 텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.9 Push hành động (action / 동작) right

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.actions {
  margin-inline-start: auto;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.10 Safe flex văn bản (text / 텍스트)** tiếp nhận điểm tựa từ **125.9 Push hành động (action / 동작) right** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.11 Safe vertical flex scroll** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.10 Safe flex văn bản (text / 텍스트)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.flex-child {
  min-width: 0;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.11 Safe vertical flex scroll** tiếp nhận điểm tựa từ **125.10 Safe flex văn bản (text / 텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.12 Single-line truncate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.11 Safe vertical flex scroll

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.panel {
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.panel__body {
  min-height: 0;
  overflow: auto;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.12 Single-line truncate** tiếp nhận điểm tựa từ **125.11 Safe vertical flex scroll** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.13 Ratio media** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.12 Single-line truncate

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.truncate {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.13 Ratio media** tiếp nhận điểm tựa từ **125.12 Single-line truncate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.14 Sticky region** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.13 Ratio media

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.media-frame {
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.media-frame > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.14 Sticky region** tiếp nhận điểm tựa từ **125.13 Ratio media** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.15 cục bộ (local / 로컬) overlay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.14 Sticky region

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.sticky {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.15 cục bộ (local / 로컬) overlay** tiếp nhận điểm tựa từ **125.14 Sticky region** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.16 Modal shell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.15 cục bộ (local / 로컬) overlay

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.wrapper {
  position: relative;
}

.wrapper__overlay {
  position: absolute;
  inset: 0;
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.16 Modal shell** tiếp nhận điểm tựa từ **125.15 cục bộ (local / 로컬) overlay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.17 Intrinsic button** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.16 Modal shell

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.modal-shell {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 1rem;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.17 Intrinsic button** tiếp nhận điểm tựa từ **125.16 Modal shell** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.18 Fluid font** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.17 Intrinsic button

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.button {
  inline-size: fit-content;
  min-block-size: 2.75rem;
  padding-inline: 1rem;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.18 Fluid font** tiếp nhận điểm tựa từ **125.17 Intrinsic button** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.19 Readable prose** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.18 Fluid font

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.title {
  font-size: clamp(1.75rem, 1rem + 3vw, 4rem);
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.19 Readable prose** tiếp nhận điểm tựa từ **125.18 Fluid font** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.20 Theme đơn vị từ (token / 토큰) consumption** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.19 Readable prose

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.prose {
  max-inline-size: 65ch;
  line-height: 1.65;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.20 Theme đơn vị từ (token / 토큰) consumption** tiếp nhận điểm tựa từ **125.19 Readable prose** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.21 trạng thái (state / 상태) via dữ liệu (data / 데이터) attribute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.20 Theme đơn vị từ (token / 토큰) consumption

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.component {
  background: var(--surface);
  color: var(--text);
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.20 Theme đơn vị từ (token / 토큰) consumption** nêu điều cần giải thích; **125.21 trạng thái (state / 상태) via dữ liệu (data / 데이터) attribute** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **125.22 mang tính ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) via ARIA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.21 trạng thái (state / 상태) via dữ liệu (data / 데이터) attribute

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.panel[data-state="open"] {}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.21 trạng thái (state / 상태) via dữ liệu (data / 데이터) attribute** nêu điều cần giải thích; **125.22 mang tính ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) via ARIA** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **125.23 Focus ring** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.22 mang tính ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) via ARIA

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
.tab[aria-selected="true"] {}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.23 Focus ring** tiếp nhận điểm tựa từ **125.22 mang tính ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) via ARIA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125.24 giảm chuyển động (reduced motion)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.23 Focus ring

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **125.24 giảm chuyển động (reduced motion)** tiếp nhận điểm tựa từ **125.23 Focus ring** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.1 thành phần nguyên thủy (primitive / 기본 요소) → thành phần (component / 컴포넌트) composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125.24 giảm chuyển động (reduced motion)

Phần này chuyển khái niệm frontend thành một rule hoặc ví dụ có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra selector, computed style và hành vi responsive.

```css
@media (prefers-reduced-motion: reduce) {
  .animated {
    animation: none;
    transition: none;
  }
}
```

---

# 126. danh mục (catalog / 카탈로그) — Coding / Programming Patterns

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.1 thành phần nguyên thủy (primitive / 기본 요소) → thành phần (component / 컴포넌트) composition** tiếp nhận điểm tựa từ **125.24 giảm chuyển động (reduced motion)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.2 trạng thái (state / 상태) Attribute mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.1 thành phần nguyên thủy (primitive / 기본 요소) → thành phần (component / 컴포넌트) composition

Thành phần nguyên thủy (primitive / 기본 요소):

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--stack-gap, 1rem);
}
```

Thành phần (component / 컴포넌트):

```html
<article class="card stack">
  ...
</article>
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.2 trạng thái (state / 상태) Attribute mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.1 thành phần nguyên thủy (primitive / 기본 요소) → thành phần (component / 컴포넌트) composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.3 Slot mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.2 trạng thái (state / 상태) Attribute mẫu (pattern / 패턴)

JS/trạng thái (state / 상태) tầng (layer / 계층):

```js
element.dataset.state = "open";
```

CSS:

```css
.dropdown[data-state="open"] {}
```

Ranh giới (boundary / 경계):

```text
JS → state
CSS → presentation
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.3 Slot mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.2 trạng thái (state / 상태) Attribute mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.4 biến thể (variant) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.3 Slot mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```html
<div class="card">
  <div data-slot="header">...</div>
  <div data-slot="body">...</div>
</div>
```

```css
.card [data-slot="header"] {}
```

Useful khi muốn expose mang tính ngữ nghĩa (semantic / 의미적) thành phần (component / 컴포넌트) slots.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.4 biến thể (variant) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.3 Slot mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.5 kích thước (size / 크기) biến thể (variant) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.4 biến thể (variant) mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.button[data-variant="primary"] {}
.button[data-variant="secondary"] {}
.button[data-variant="danger"] {}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.5 kích thước (size / 크기) biến thể (variant) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.4 biến thể (variant) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.6 đơn vị từ (token / 토큰) Override mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.5 kích thước (size / 크기) biến thể (variant) mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.button[data-size="sm"] {}
.button[data-size="md"] {}
.button[data-size="lg"] {}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.6 đơn vị từ (token / 토큰) Override mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.5 kích thước (size / 크기) biến thể (variant) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.7 bố cục (layout / 레이아웃) Wrapper mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.6 đơn vị từ (token / 토큰) Override mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.button {
  --button-bg: var(--color-action);
  background: var(--button-bg);
}

.hero .button {
  --button-bg: white;
}
```

Override đơn vị từ (token / 토큰) thường ổn hơn override nhiều internals.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.7 bố cục (layout / 레이아웃) Wrapper mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.6 đơn vị từ (token / 토큰) Override mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.8 cải tiến lũy tiến (progressive enhancement) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.7 bố cục (layout / 레이아웃) Wrapper mẫu (pattern / 패턴)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```html
<section class="section">
  <div class="container">
    ...
  </div>
</section>
```

Responsibility:
- `section`: background + vertical rhythm,
- `container`: horizontal ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.8 cải tiến lũy tiến (progressive enhancement) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.7 bố cục (layout / 레이아웃) Wrapper mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.9 Container-responsive mẫu thành phần (component pattern)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.8 cải tiến lũy tiến (progressive enhancement) mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.card {
  background: white;
}

@supports (backdrop-filter: blur(1rem)) {
  .card {
    backdrop-filter: blur(1rem);
  }
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.9 Container-responsive mẫu thành phần (component pattern)** tiếp nhận điểm tựa từ **126.8 cải tiến lũy tiến (progressive enhancement) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.10 trạng thái (state / 상태) + chuyển tiếp (transition / 전이) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.9 Container-responsive mẫu thành phần (component pattern)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```css
.component-shell {
  container-type: inline-size;
}

@container (width >= 30rem) {
  .component {
    display: grid;
  }
}
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.10 trạng thái (state / 상태) + chuyển tiếp (transition / 전이) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.9 Container-responsive mẫu thành phần (component pattern)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126.11 mang tính ngữ nghĩa (semantic / 의미적) CSS API mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.10 trạng thái (state / 상태) + chuyển tiếp (transition / 전이) mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
.popover {
  opacity: 0;
  translate: 0 -.25rem;
}

.popover[data-state="open"] {
  opacity: 1;
  translate: 0;
}
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.11 mang tính ngữ nghĩa (semantic / 의미적) CSS API mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **126.10 trạng thái (state / 상태) + chuyển tiếp (transition / 전이) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127.1 Layered cơ chế phân tầng (cascade) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126.11 mang tính ngữ nghĩa (semantic / 의미적) CSS API mẫu (pattern / 패턴)

Expose:
- `data-variant`,
- `data-size`,
- mang tính ngữ nghĩa (semantic / 의미적)/ARIA trạng thái (state / 상태),
- selected custom thuộc tính (property / 속성) hooks.

Không expose nội bộ (internal / 내부) DOM độ sâu (depth / 깊이) như API.

---

# 127. danh mục (catalog / 카탈로그) — CSS thiết kế (design / 설계) / kiến trúc (architecture / 아키텍처) Patterns

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **126.11 mang tính ngữ nghĩa (semantic / 의미적) CSS API mẫu (pattern / 패턴)** xác định đầu vào; **127.1 Layered cơ chế phân tầng (cascade) mẫu (pattern / 패턴)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **127.2 phân cấp đơn vị từ (token / 토큰) (token hierarchy) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.1 Layered cơ chế phân tầng (cascade) mẫu (pattern / 패턴)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
reset
tokens
base
objects/layout
components
utilities
overrides
```

Implement tốt bằng `@layer`.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.1 Layered cơ chế phân tầng (cascade) mẫu (pattern / 패턴)** xác định đầu vào; **127.2 phân cấp đơn vị từ (token / 토큰) (token hierarchy) mẫu (pattern / 패턴)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **127.3 Composition mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.2 phân cấp đơn vị từ (token / 토큰) (token hierarchy) mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
Foundation
→ Semantic
→ Component
→ State
```

Ví dụ:

```text
blue-600
→ color-action-primary
→ button-bg
→ button-bg-hover
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.3 Composition mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **127.2 phân cấp đơn vị từ (token / 토큰) (token hierarchy) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127.4 đóng gói (encapsulation) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.3 Composition mẫu (pattern / 패턴)

Thành phần (component / 컴포넌트) compose các primitives:

```text
Stack
Cluster
Center
Grid
Sidebar
Container
```

thay vì mỗi thành phần (component / 컴포넌트) viết lại bố cục (layout / 레이아웃).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.4 đóng gói (encapsulation) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **127.3 Composition mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127.5 Exception mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.4 đóng gói (encapsulation) mẫu (pattern / 패턴)

Mức cô lập (isolation) tăng dần:

```text
naming convention
→ @scope
→ CSS Modules
→ Shadow DOM
```

Chọn đúng mức thay vì luôn dùng mức mạnh nhất.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.5 Exception mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **127.4 đóng gói (encapsulation) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127.6 Theme-by-contract mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.5 Exception mẫu (pattern / 패턴)

Cơ sở (base / 기반):

```css
.card {}
```

Exception:

```css
.card[data-emphasis="high"] {}
```

Không duplicate thành `.special-card-special`.

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.6 Theme-by-contract mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **127.5 Exception mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127.7 quyền sở hữu hành vi đáp ứng (responsive ownership) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.6 Theme-by-contract mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```css
[data-theme="dark"] {
  --surface-default: #111;
  --text-default: #fff;
}
```

Components consume mang tính ngữ nghĩa (semantic / 의미적) tokens.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, sau nội dung của **127.6 Theme-by-contract mẫu (pattern / 패턴)**, **127.7 quyền sở hữu hành vi đáp ứng (responsive ownership) mẫu (pattern / 패턴)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **127.8 Overlay quyền sở hữu (ownership / 소유권) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.7 quyền sở hữu hành vi đáp ứng (responsive ownership) mẫu (pattern / 패턴)

Phần này giải thích rule CSS/SCSS trong quan hệ với cascade, layout và breakpoint. Hãy xác định input, thứ tự áp dụng, invariant giao diện và cách kiểm tra trên viewport thực.

```text
Page-level layout        → @media
Component-level layout   → @container
User preference          → media features
Feature availability     → @supports
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.8 Overlay quyền sở hữu (ownership / 소유권) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **127.7 quyền sở hữu hành vi đáp ứng (responsive ownership) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127.9 Accessibility-first Styling mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.8 Overlay quyền sở hữu (ownership / 소유권) mẫu (pattern / 패턴)

Mục này chốt mental model của styling thành constraint, token, composition và runtime effect. Đọc code cùng lý do chọn pattern và failure mode khi scale.

```text
local decoration → absolute
viewport UI      → fixed
scroll-affixed   → sticky
top-layer UI     → dialog/popover
anchor UI        → Anchor Positioning
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.9 Accessibility-first Styling mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **127.8 Overlay quyền sở hữu (ownership / 소유권) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127.10 bố cục theo ràng buộc (constraint-driven layout) mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.9 Accessibility-first Styling mẫu (pattern / 패턴)

Cơ sở (base / 기반) thành phần (component / 컴포넌트) phải:
- keyboard visible,
- readable khi zoom,
- không color-only trạng thái (state / 상태),
- reduced-motion compatible.

Visual enhancement đến sau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **127.10 bố cục theo ràng buộc (constraint-driven layout) mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **127.9 Accessibility-first Styling mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ellipsis** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127.10 bố cục theo ràng buộc (constraint-driven layout) mẫu (pattern / 패턴)

Không chỉ nghĩ:

```text
desktop = 1200px
tablet = 768px
mobile = 375px
```

Hãy nghĩ:

```text
content minimum
preferred size
maximum readable size
available space
wrapping threshold
```

CSS hiện đại (`min`, `max`, `clamp`, Grid, truy vấn vùng chứa (container query)) hỗ trợ cách nghĩ này tốt hơn.

---

# 128. cấp cao (senior / 시니어) mẫu (pattern / 패턴) map khóa–giá trị (map) — thuộc tính (property / 속성) nào thường đi cùng thuộc tính (property / 속성) nào

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Ellipsis** tiếp nhận điểm tựa từ **127.10 bố cục theo ràng buộc (constraint-driven layout) mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Responsive ảnh (image / 이미지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ellipsis

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
min-width: 0
+ overflow: hidden
+ white-space: nowrap
+ text-overflow: ellipsis
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Responsive ảnh (image / 이미지)** tiếp nhận điểm tựa từ **Ellipsis** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sticky** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Responsive ảnh (image / 이미지)

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
width/max-width
+ height:auto
+ object-fit
+ aspect-ratio
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Sticky** tiếp nhận điểm tựa từ **Responsive ảnh (image / 이미지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Absolute overlay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sticky

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
position: sticky
+ top/inset
+ correct scroll container
+ enough scrollable space
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Absolute overlay** tiếp nhận điểm tựa từ **Sticky** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Absolute overlay

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
parent position:relative
+ child position:absolute
+ inset
+ z-index nếu cần
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Modal** tiếp nhận điểm tựa từ **Absolute overlay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Flexible văn bản (text / 텍스트) row** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modal

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
fixed/top-layer
+ inset
+ center layout
+ max-height
+ overflow:auto
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Flexible văn bản (text / 텍스트) row** tiếp nhận điểm tựa từ **Modal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Accessible interactive điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Flexible văn bản (text / 텍스트) row

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
display:flex/grid
+ minmax(0,1fr) hoặc min-width:0
+ gap
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Accessible interactive điều khiển (control / 제어)** tiếp nhận điểm tựa từ **Flexible văn bản (text / 텍스트) row** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Theme** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Accessible interactive điều khiển (control / 제어)

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
minimum target size
+ padding
+ font:inherit
+ focus-visible
+ disabled state
+ hover as enhancement
```

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Theme** tiếp nhận điểm tựa từ **Accessible interactive điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Animation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Theme

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
custom properties
+ semantic tokens
+ data-theme/color-scheme
+ prefers-color-scheme optional
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Animation** tiếp nhận điểm tựa từ **Theme** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thành phần (component / 컴포넌트) responsive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Animation

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
state attribute
+ transform/opacity
+ transition/animation
+ prefers-reduced-motion
```

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Thành phần (component / 컴포넌트) responsive** tiếp nhận điểm tựa từ **Animation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BEM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thành phần (component / 컴포넌트) responsive

Phần này chuyển khái niệm styling thành một ví dụ hoặc rule có thể quan sát. Hãy đọc mục đích trước, sau đó kiểm tra output, edge case và tác động lên các lớp giao diện liên quan.

```text
container-type
+ @container
+ intrinsic layout
```

---

# 129. Khi nào mẫu (pattern / 패턴) trở thành phản mẫu (anti-pattern)?

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **BEM** tiếp nhận điểm tựa từ **Thành phần (component / 컴포넌트) responsive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tiện ích (utility) classes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BEM

Tốt khi:
- toàn cục (global / 전역)/plain CSS,
- cần tường minh (explicit / 명시적) naming.

Có thể dư khi:
- CSS Modules/Shadow DOM (cây DOM đóng gói) đã phạm vi (scope / 범위).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **tiện ích (utility) classes** tiếp nhận điểm tựa từ **BEM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **lồng cú pháp (nesting)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tiện ích (utility) classes

Tốt khi:
- thiết kế (design / 설계) các ràng buộc (constraints / 제약조건들) rõ,
- nhóm (team / 팀) quen composition.

Có thể xấu khi:
- tiện ích (utility) naming tùy tiện,
- không có đơn vị từ (token / 토큰) hệ thống (system / 시스템),
- dùng tiện ích (utility) để encode nghiệp vụ (business / 비즈니스) trạng thái (state / 상태).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **lồng cú pháp (nesting)** tiếp nhận điểm tựa từ **tiện ích (utility) classes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Custom các thuộc tính (properties)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## lồng cú pháp (nesting)

Tốt:
- các trạng thái (states),
- các phần tử giả (pseudo-elements),
- cục bộ (local / 로컬) media/truy vấn vùng chứa (container query).

Xấu:
- phản chiếu toàn bộ DOM cây (tree / 트리).

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Custom các thuộc tính (properties)** tiếp nhận điểm tựa từ **lồng cú pháp (nesting)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **@layer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Custom các thuộc tính (properties)

Tốt:
- thời gian chạy (runtime / 런타임) theme,
- giao diện thành phần (component API),
- mang tính ngữ nghĩa (semantic / 의미적) tokens.

Xấu:
- hàng trăm các biến (variables) không có ngữ nghĩa (semantics / 의미론),
- lớp trừu tượng (abstraction / 추상화) cho giá trị (value / 값) chỉ dùng một lần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **@layer** tiếp nhận điểm tựa từ **Custom các thuộc tính (properties)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **truy vấn vùng chứa (container query)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `@layer`

Tốt:
- codebase lớn,
- vendor CSS,
- predictable cơ chế phân tầng (cascade).

Có thể overkill:
- một thành phần (component / 컴포넌트)/tệp (file / 파일) cực nhỏ.

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **truy vấn vùng chứa (container query)** tiếp nhận điểm tựa từ **@layer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Beginner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## truy vấn vùng chứa (container query)

Tốt:
- reusable thành phần (component / 컴포넌트) ở nhiều bộ chứa (container / 컨테이너).

Không cần thiết:
- page-level điểm ngắt (breakpoint) đơn giản.

Cấp cao (senior / 시니어) không chỉ biết mẫu (pattern / 패턴); cấp cao (senior / 시니어) biết **khi nào không dùng mẫu (pattern / 패턴)**.

---

# 130. Cách đọc CSS môi trường vận hành (production / 운영 환경) như cấp cao (senior / 시니어)

Khi mở thành phần (component / 컴포넌트), đọc theo thứ tự:

```text
1. Layout context
2. Component tokens
3. Base styles
4. Slots/elements
5. Variants
6. Runtime states
7. Responsive behavior
8. Motion
9. Accessibility
10. Browser fallback
```

Ví dụ:

```css
.card {
  --card-padding: 1rem;

  display: grid;
  gap: var(--card-padding);

  border-radius: .75rem;
  background: var(--surface);
}

.card[data-variant="featured"] {
  --card-padding: 1.5rem;
}

.card:focus-within {
  outline: 2px solid var(--focus);
}

@container (width >= 30rem) {
  .card {
    grid-template-columns: auto minmax(0, 1fr);
  }
}
```

Một tệp (file / 파일) CSS dễ maintain khi dev khác đọc được luồng (flow / 흐름) này mà không phải reverse-engineer.

---

# 131. học tập (learning / 학습) Checkpoints theo cấp độ

> **Chuyển mạch:** Ở chặng này của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Beginner** tiếp nhận điểm tựa từ **truy vấn vùng chứa (container query)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Intermediate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Beginner

Phải làm được:
- bộ chọn (selector),
- cơ chế phân tầng (cascade),
- mô hình hộp (box model / 박스 모델),
- typography,
- spacing,
- Flexbox,
- Grid cơ bản,
- responsive truy vấn môi trường (media query).

Patterns cần nhớ:
- bộ chứa (container / 컨테이너),
- ngăn xếp (stack / 스택),
- cluster,
- center,
- truncate,
- responsive ảnh (image / 이미지).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Intermediate** tiếp nhận điểm tựa từ **Beginner** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cấp cao (senior / 시니어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Intermediate

Phải hiểu:
- định cỡ nội tại (intrinsic sizing / 내재 크기 결정),
- min/max các ràng buộc (constraints / 제약조건들),
- sticky,
- ngữ cảnh xếp chồng (stacking context / 쌓임 맥락),
- Grid placement,
- custom các thuộc tính (properties),
- thành phần (component / 컴포넌트) các biến thể (variants),
- các truy vấn vùng chứa (container queries).

Patterns cần biết:
- media đối tượng (object / 객체),
- sidebar,
- auto-grid,
- đơn vị từ (token / 토큰) override,
- trạng thái (state / 상태) attribute,
- responsive thành phần (component / 컴포넌트).

> **Chuyển mạch:** Trong **CSS — Beginner → cấp cao (senior / 시니어) Handbook (2026)**, **Cấp cao (senior / 시니어)** tiếp nhận điểm tựa từ **Intermediate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cấp cao (senior / 시니어)

Phải thiết kế được:
- cơ chế phân tầng (cascade) kiến trúc (architecture / 아키텍처),
- phân cấp đơn vị từ (token / 토큰) (token hierarchy),
- giao diện thành phần (component API),
- phạm vi (scope / 범위)/tầng (layer / 계층) chiến lược (strategy / 전략),
- khả năng tiếp cận (accessibility / 접근성) hành vi (behavior / 동작),
- hiệu năng (performance / 성능) chiến lược (strategy / 전략),
- trình duyệt (browser / 브라우저) phương án dự phòng (fallback),
- gỡ lỗi (debugging) methodology.

Patterns cần thành thạo:
- layered cơ chế phân tầng (cascade),
- mang tính ngữ nghĩa (semantic / 의미적) tokens,
- composition primitives,
- quyền sở hữu hành vi đáp ứng (responsive ownership),
- overlay quyền sở hữu (ownership / 소유권),
- cải tiến lũy tiến (progressive enhancement),
- bố cục theo ràng buộc (constraint-driven layout).

---

---

# 132. cơ chế phân tầng (cascade) & độ đặc hiệu (specificity) — dấu vết (trace / 추적) quyết định khai báo (declaration) thắng [cốt lõi (core / 핵심)/cấp cao (senior / 시니어)]

Một trong những sai lầm phổ biến nhất khi học CSS là coi độ đặc hiệu (specificity) như “định luật cao nhất”. Trên thực tế, trình duyệt (browser / 브라우저) chỉ so độ đặc hiệu (specificity) sau khi đã loại những khai báo (declaration) không cùng precedence. Vì vậy một bộ chọn (selector) rất mạnh vẫn có thể thua quy tắc (rule / 규칙) ở origin/tầng (layer / 계층)/importance khác. mô hình tư duy (mental model / 사고 모델) tốt hơn là coi cơ chế phân tầng (cascade) như một chuỗi bộ lọc.

Giả sử cùng một `button` nhận nhiều quy tắc (rule / 규칙) từ reset, thành phần (component / 컴포넌트) CSS, tiện ích (utility) tầng (layer / 계층) và inline style. trình duyệt (browser / 브라우저) trước tiên xét quy tắc (rule / 규칙) có relevant với element/media điều kiện (condition / 조건) hay không. Sau đó nó xét origin và `!important`, rồi lớp phân tầng (cascade layer). Chỉ những khai báo (declaration) còn cùng tầng precedence mới so độ đặc hiệu (specificity); nếu vẫn bằng nhau thì độ gần phạm vi (scope proximity) có thể tham gia với `@scope`, cuối cùng mới đến thứ tự nguồn (source order).

```text
relevance
→ origin + importance
→ cascade layer
→ specificity
→ scoping proximity
→ source order
```

Điểm thực tế quan trọng là `@layer` cho phép bạn thay đổi precedence mà không tăng bộ chọn (selector) strength. Nếu `components` đứng trước `utilities`, một tiện ích (utility) bộ chọn (selector) đơn giản có thể override thành phần (component / 컴포넌트) quy tắc (rule / 규칙) dù thành phần (component / 컴포넌트) bộ chọn (selector) nhìn “dài” hơn. Đây là lý do kiến trúc (architecture / 아키텍처) cơ chế phân tầng (cascade) tốt bền hơn việc nối thêm lớp (class / 클래스)/ID vào bộ chọn (selector).

độ đặc hiệu (specificity) của các lớp giả (pseudo-class) hiện đại cũng cần hiểu theo cơ chế chứ không học số rời rạc. `:where()` luôn đóng góp độ đặc hiệu (specificity) bằng 0, vì vậy rất phù hợp cho defaults. `:is()`, `:not()` và `:has()` lấy độ đặc hiệu (specificity) từ bộ chọn (selector) có độ đặc hiệu (specificity) cao nhất trong argument danh sách (list / 목록). Điều này có thể làm một quy tắc (rule / 규칙) mạnh hơn bạn tưởng nếu vô tình đưa ID vào argument.

```css
/* phần :where(...) không tăng specificity */
:where(.article) h2 {
  margin-block: 2rem 1rem;
}

/* specificity chịu ảnh hưởng bởi #app trong :is(...) */
:is(.page, #app) .title {
  color: var(--heading);
}
```

Khi cần override, hãy sửa đúng tầng. Nếu vấn đề là tầng (layer / 계층) thứ tự (order / 순서), sửa `@layer`; nếu bộ chọn (selector) quá mạnh, giảm độ đặc hiệu (specificity); nếu trạng thái (state / 상태) thuộc thành phần (component / 컴포넌트), dùng attribute/biến thể (variant) rõ; nếu third-party CSS dùng `!important`, isolate nó vào tầng (layer / 계층) hoặc tích hợp (integration / 통합) ranh giới (boundary / 경계). `!important` không phải công cụ đầu tiên vì nó đổi một khai báo (declaration) sang một precedence lớp (class / 클래스) khác và dễ tạo cuộc chiến mới.

Một môi trường vận hành (production / 운영 환경) gỡ lỗi (debugging) dấu vết (trace / 추적) nên bắt đầu trong DevTools: xác nhận bộ chọn (selector) match, xem khai báo (declaration) nào bị crossed-out, nhìn tầng (layer / 계층)/origin, rồi mới tính độ đặc hiệu (specificity). Nếu bạn đang tính độ đặc hiệu (specificity) trước khi biết tầng (layer / 계층) nào đang thắng, bạn đang gỡ lỗi (debug / 디버그) sai thứ tự.

---

# 133. bố cục (layout / 레이아웃) mô hình tư duy (mental model / 사고 모델) — từ không gian khả dụng (available space) tới hình học (geometry / 기하학) [cốt lõi (core / 핵심)/cấp cao (senior / 시니어)]

Bố cục (layout / 레이아웃) không phải “đặt `width`, rồi trình duyệt (browser / 브라우저) vẽ đúng con số đó”. trình duyệt (browser / 브라우저) phải giải một hệ các ràng buộc (constraints / 제약조건들). Mỗi box có intrinsic contribution từ content, min/max các ràng buộc (constraints / 제약조건들), preferred kích thước (size / 크기), không gian khả dụng (available space) từ khối chứa tham chiếu (containing block / 컨테이닝 블록) và rules của ngữ cảnh định dạng (formatting context / 서식 컨텍스트). Flexbox và Grid chỉ là hai các thuật toán bố cục (layout algorithms) khác nhau chạy trên cùng những inputs cơ bản đó.

Một cách đọc bố cục (layout / 레이아웃) hữu ích là:

```text
box được tạo bởi display nào?
→ formatting context nào đang quản lý children?
→ containing block / available size là gì?
→ intrinsic min/max-content contributions là gì?
→ min/max/width/height/aspect-ratio giới hạn ra sao?
→ algorithm phân phối free space như thế nào?
→ overflow/clipping/scroll xảy ra ở đâu?
```

Ví dụ `width: 100%` không đảm bảo element vừa màn hình. Nếu parent có padding theo `content-box`, child có min-content lớn, hoặc child là flex/phần tử Grid (grid item) với kích thước tối thiểu tự động (automatic minimum size), hình học (geometry / 기하학) cuối cùng có thể overflow. Ngược lại, một element không có tường minh (explicit / 명시적) width vẫn có thể có kích thước (size / 크기) rất cụ thể do dải lưới (grid track) hoặc Flex thuật toán (algorithm / 알고리즘) quyết định.

Luồng bố cục thông thường (normal flow / 일반 흐름) là đường cơ sở (baseline). khối (block / 블록) boxes thường xếp theo khối (block / 블록) luồng (flow / 흐름); inline content tạo các hộp dòng (line boxes). Khi `display:flex` hoặc `display:grid` xuất hiện, children trực tiếp trở thành flex/các phần tử Grid (grid items) và sizing rules thay đổi. Khi `position:absolute` xuất hiện, box rời luồng bố cục thông thường (normal flow / 일반 흐름) và hình học (geometry / 기하학) phụ thuộc khối chứa tham chiếu (containing block / 컨테이닝 블록) mới. Vì vậy “thuộc tính (property / 속성) nào đang sai?” thường là câu hỏi kém hơn “thuật toán (algorithm / 알고리즘) nào đang quyết định hình học (geometry / 기하학) này?”.

Định cỡ nội tại (intrinsic sizing / 내재 크기 결정) là chìa khóa của nhiều bug cấp cao (senior / 시니어). `min-content` mô tả kích thước nhỏ nhất content có thể co theo wrapping rules; `max-content` mô tả kích thước (size / 크기) content muốn có nếu không wrap; `fit-content` nằm giữa intrinsic desire và không gian khả dụng (available space). `minmax(0, 1fr)` trong Grid và `min-width:0` trong Flex đều là cách nói với trình duyệt (browser / 브라우저) rằng content được phép co nhỏ hơn automatic intrinsic minimum trong những ngữ cảnh (context / 맥락) cụ thể.

---

# 134. Flexbox — đọc thuật toán (algorithm / 알고리즘) thay vì thuộc thuộc tính (property / 속성) [cốt lõi (core / 핵심)/cấp cao (senior / 시니어)]

Flexbox giải bài toán một chiều. trình duyệt (browser / 브라우저) xác định trục chính (main axis) từ `flex-direction`, lấy flex cơ sở (base / 기반) kích thước (size / 크기) của từng item, so tổng hypothetical kích thước (size / 크기) với available main-axis không gian (space / 공간), rồi quyết định đang có positive không gian dư (free space) hay negative không gian dư (free space). Sau đó `flex-grow` hoặc `flex-shrink` phân phối phần dư/thiếu theo factor và các ràng buộc (constraints / 제약조건들).

Vì thế `flex: 1` không đơn giản có nghĩa “chiếm 100%”. Nó thay grow/shrink/basis để item tham gia phân phối không gian (space / 공간). Hai item `flex:1` thường chia không gian dư (free space) cân bằng, nhưng intrinsic min-size vẫn có thể chặn item co. Đây là lý do mẫu (pattern / 패턴) môi trường vận hành (production / 운영 환경) rất thường là:

```css
.row {
  display: flex;
  gap: 1rem;
}

.avatar {
  flex: none;
}

.body {
  flex: 1;
  min-width: 0;
}
```

`min-width:0` không phải mẹo Tailwind/CSS bí ẩn; nó thay mức tối thiểu tự động (automatic minimum) ràng buộc (constraint / 제약조건) để phần tử Flex (flex item) được phép co và để `overflow`, `text-overflow` hoặc child wrapping phát huy tác dụng.

Cross-axis alignment được tính sau main-axis sizing và phụ thuộc `align-items`, `align-self`, đường cơ sở (baseline) rules và available cross kích thước (size / 크기). `justify-content` chỉ phân phối remaining không gian dư (free space) trên trục chính (main axis); nếu items đã grow lấp hết không gian dư (free space) thì `justify-content:space-between` không tạo thêm “ma thuật”. Vì vậy khi alignment không như mong đợi, trước tiên xác định axis và không gian dư (free space) có thật sự tồn tại hay không.

Cấp cao (senior / 시니어) mẫu (pattern / 패턴) là dùng Flex cho composition một chiều như toolbar, cluster, media đối tượng (object / 객체), hành động (action / 동작) row. Nếu bạn bắt đầu điều khiển nhiều row/column alignment đồng thời bằng width calc, margin và thứ tự (order / 순서), hãy kiểm tra xem Grid có đúng mô hình tư duy (mental model / 사고 모델) hơn không.

---

# 135. Grid — định cỡ dải lưới (track sizing) trước, placement sau [cốt lõi (core / 핵심)/cấp cao (senior / 시니어)]

Grid mạnh vì trình duyệt (browser / 브라우저) giải tracks trước rồi đặt items vào hệ tracks đó. Bạn nên đọc Grid theo thứ tự: tường minh (explicit / 명시적) grid được định nghĩa thế nào, implicit tracks nào có thể phát sinh, intrinsic contributions của items ảnh hưởng định cỡ dải lưới (track sizing) ra sao, sau đó mới nhìn item placement.

`1fr` không đơn giản là “một phần trăm”. Fraction đơn vị (unit / 단위) phân phối **không gian dư (free space) còn lại** sau khi fixed/intrinsic các ràng buộc (constraints / 제약조건들) đã được giải. Vì phần tử Grid (grid item) có mức tối thiểu tự động (automatic minimum) contribution, `1fr` đôi khi không co nhỏ như bạn kỳ vọng. `minmax(0, 1fr)` mở minimum xuống 0 và vì thế là mẫu (pattern / 패턴) an toàn cho content area có thể chứa văn bản (text / 텍스트) dài hoặc nested bố cục (layout / 레이아웃).

```css
.shell {
  display: grid;
  grid-template-columns: 16rem minmax(0, 1fr);
}
```

`repeat(auto-fit, minmax(min(100%, 18rem), 1fr))` là ví dụ rất tốt của intrinsic thiết kế đáp ứng (responsive design). Không cần đoán “tablet điểm ngắt (breakpoint)”; trình duyệt (browser / 브라우저) tự tạo số nhánh học (track / 트랙) vừa với không gian khả dụng (available space) và collapse empty tracks. Đây là responsive bố cục (layout / 레이아웃) do các ràng buộc (constraints / 제약조건들) quyết định, không phải do thiết bị (device / 장치) categories.

Grid placement (`grid-column`, named areas, spans) nên được dùng sau khi nhánh học (track / 트랙) hệ thống (system / 시스템) đã rõ. `grid-auto-flow:dense` có thể backfill visual gaps nhưng có thể làm visual thứ tự (order / 순서) khác DOM thứ tự (order / 순서), nên không phù hợp khi thứ tự tương tác/đọc có ý nghĩa. Subgrid phù hợp khi nested thành phần (component / 컴포넌트) cần chia sẻ parent tracks thay vì duplicate width constants.

---

# 136. Responsive — quyết định bằng ràng buộc (constraint / 제약조건), không bằng tên thiết bị [cốt lõi (core / 핵심)/cấp cao (senior / 시니어)]

thiết kế đáp ứng (responsive design) tốt bắt đầu từ content và không gian khả dụng (available space). Trước khi thêm truy vấn môi trường (media query), hãy xem bố cục (layout / 레이아웃) có thể tự thích ứng bằng wrapping, định cỡ nội tại (intrinsic sizing / 내재 크기 결정), `min()`, `max()`, `clamp()`, `auto-fit` hoặc Flex/Grid hay không. truy vấn (query / 쿼리) nên xuất hiện khi **hành vi (behavior / 동작) cần đổi**, không phải vì vùng nhìn (viewport) chạm một tên thiết bị (device / 장치).

truy vấn môi trường (media query) phù hợp với page/environment-level concerns: vùng nhìn (viewport) kích thước (size / 크기), orientation, hover năng lực (capability / 역량), pointer precision, giảm chuyển động (reduced motion), color scheme hoặc print. truy vấn vùng chứa (container query) phù hợp khi một reusable thành phần (component / 컴포넌트) cần biết không gian nó thực sự nhận được trong sidebar, modal hoặc main content. Hai loại truy vấn (query / 쿼리) có thể dùng cùng nhau nhưng quyền sở hữu (ownership / 소유권) phải rõ: page shell thường theo vùng nhìn (viewport), thành phần (component / 컴포넌트) internals thường theo bộ chứa (container / 컨테이너).

```css
.dashboard {
  display: grid;
  gap: 1rem;
}

@media (width >= 64rem) {
  .dashboard {
    grid-template-columns: 18rem minmax(0, 1fr);
  }
}

.widget-host {
  container-type: inline-size;
}

@container (width >= 32rem) {
  .widget {
    grid-template-columns: auto minmax(0, 1fr);
  }
}
```

Đừng quên responsive còn gồm zoom, translated văn bản (text / 텍스트), người dùng (user / 사용자) font kích thước (size / 크기), coarse pointer, keyboard, giảm chuyển động (reduced motion) và động (dynamic / 동적) vùng nhìn (viewport). Một bố cục (layout / 레이아웃) chỉ đẹp ở ba screenshot width chưa thể gọi là robust responsive UI.

---

# 137. hiện đại (modern / 현대적) CSS — adoption chiến lược (strategy / 전략) thay vì chạy theo tính năng (feature / 기능) [ADV/hiện đại (modern / 현대적)]

Hiện đại (modern / 현대적) CSS hiện đã có nhiều công cụ từng cần preprocessor hoặc JavaScript: bản địa (native / 네이티브) lồng cú pháp (nesting), `:has()`, các lớp phân tầng (cascade layers), `@scope`, các truy vấn vùng chứa (container queries), subgrid, thuộc tính lô-gic (logic / 논리) (logical properties), `@property`, định vị theo điểm neo (anchor positioning), lớp trên cùng (top layer), popover/dialog styling, hoạt ảnh điều khiển bằng cuộn (scroll-driven animations) và chuyển cảnh giao diện (view transitions). Cách học đúng không phải ghi nhớ bản phát hành (release / 릴리스) danh sách (list / 목록) mà hiểu **vấn đề cũ nào được thay thế**.

các lớp phân tầng (cascade layers) thay độ đặc hiệu (specificity) conventions; các truy vấn vùng chứa (container queries) giảm thành phần (component / 컴포넌트) các điểm ngắt (breakpoints) phụ thuộc vùng nhìn (viewport); `:has()` giảm trạng thái (state / 상태) lớp (class / 클래스) chỉ để style DOM relationship; bản địa (native / 네이티브) lồng cú pháp (nesting) giảm một phần nhu cầu SCSS lồng cú pháp (nesting); thuộc tính lô-gic (logic / 논리) (logical properties) giảm hard-coded LTR các giả định (assumptions / 가정들); lớp trên cùng (top layer) giải nhiều stacking problems của modal/popover; định vị theo điểm neo (anchor positioning) giảm manual coordinate JS cho overlay trong mức hỗ trợ trình duyệt (browser support / 브라우저 지원) phù hợp.

Môi trường vận hành (production / 운영 환경) adoption nên chia tính năng (feature / 기능) thành ba nhóm. Nhóm critical-layout phải có trình duyệt (browser / 브라우저) đường cơ sở (baseline) phù hợp hoặc phương án dự phòng (fallback) rõ. Nhóm enhancement như balanced văn bản (text / 텍스트), visual transitions hay scroll-driven decoration có thể progressive enhance. Nhóm experimental/rapidly evolving phải được feature-query/kiểm thử (test / 테스트) trước khi trở thành foundation của hệ thống thiết kế (design system).

`@supports` không phải công cụ để bọc mọi thuộc tính (property / 속성) mới. Nếu unsupported trình duyệt (browser / 브라우저) đơn giản ignore khai báo (declaration) và phương án dự phòng (fallback) tự nhiên vẫn usable, bạn không cần truy vấn (query / 쿼리). Dùng truy vấn hỗ trợ tính năng (feature query) khi cần thay **một chiến lược (strategy / 전략) hoàn chỉnh** tùy hỗ trợ (support / 지원).

---

# 138. hiệu năng (performance / 성능) + khả năng tiếp cận (accessibility / 접근성) là bố cục (layout / 레이아웃) các ràng buộc (constraints / 제약조건들), không phải bước cuối [cấp cao (senior / 시니어)]

Hiệu năng (performance / 성능) và khả năng tiếp cận (accessibility / 접근성) thường bị đặt cuối checklist, nhưng chúng ảnh hưởng thiết kế (design / 설계) quyết định (decision / 결정) từ đầu. Một fixed-height card có thể đẹp với mẫu (sample / 표본) văn bản (text / 텍스트) nhưng cắt content khi zoom 200%. Visual reorder bằng `order`/Grid placement có thể làm keyboard/screen-reader thứ tự (order / 순서) khác visual thứ tự (order / 순서). `opacity:0` có thể giấu hình nhưng để focus mục tiêu (target / 대상) tồn tại. Heavy backdrop blur trên full vùng nhìn (viewport) có thể đẹp nhưng tốn paint/composite chi phí (cost / 비용) trên mobile.

Motion nên bắt đầu từ mang tính ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) và có reduced-motion đường dẫn (path / 경로). Interactive điều khiển (control / 제어) phải có visible focus và mục tiêu (target / 대상) kích thước (size / 크기) phù hợp. thành phần (component / 컴포넌트) phải chịu được long content, locale khác, màu cưỡng bức (forced colors)/độ tương phản cao (high contrast) và font loading. Đây là functional tính đúng đắn (correctness / 정확성), không phải optional polish.

Về hiệu năng (performance / 성능), hãy đo vô hiệu hóa (invalidation / 무효화). Thay đổi font metrics có thể gây bố cục (layout / 레이아웃); thay `width`/`height` trong animation thường kéo hình học (geometry / 기하학) recalculation; large shadows/filters tăng paint; quá nhiều promoted layers tăng bộ nhớ (memory / 메모리). `transform`/`opacity` thường compositor-friendly nhưng không phải miễn phí. `contain`, `content-visibility` và `will-change` chỉ nên dùng khi bạn hiểu tác dụng phụ (side effect) và đã đo bottleneck.

---

# 139. các mẫu dùng trong môi trường vận hành (production / 운영 환경) (production patterns) — compose hành vi (behavior / 동작) từ primitives [cấp cao (senior / 시니어)]

Môi trường vận hành (production / 운영 환경) CSS nên có một vocabulary nhỏ nhưng mạnh thay vì hàng trăm thành phần (component / 컴포넌트) rules trùng nhau. `Stack` biểu diễn vertical rhythm bằng column flex + gap. `Cluster` biểu diễn inline group có wrap. `Container` chịu horizontal ràng buộc (constraint / 제약조건). `Sidebar` dùng Grid/Flex với một fixed/intrinsic region và `minmax(0,1fr)` cho content. `Media Object` giữ media không shrink và body có `min-width:0`. App shell vertical dùng `min-height:100dvh`, fixed header region và `min-height:0; overflow:auto` cho body.

Overlay cũng cần quyền sở hữu (ownership / 소유권) rõ. Decoration cục bộ (local / 로컬) dùng positioned ancestor + absolute child. Sticky controls dùng `position:sticky` và vùng chứa cuộn (scroll container) rõ. Modal/popover trọng yếu (critical / 중요) nên ưu tiên bản địa (native / 네이티브) top-layer primitives khi ngữ nghĩa (semantics / 의미론) phù hợp thay vì đẩy `z-index` lên vô hạn. Theme nên đi qua mang tính ngữ nghĩa (semantic / 의미적) custom các thuộc tính (properties) để thành phần (component / 컴포넌트) không duplicate dark/light rules. thành phần (component / 컴포넌트) trạng thái (state / 상태) nên đi qua bản địa (native / 네이티브) lớp giả (pseudo-class), ARIA trạng thái (state / 상태) hoặc `data-*` đặc tả hợp đồng (contract / 계약) thay vì lớp (class / 클래스) tên theo từng combination.

Một mẫu (pattern / 패턴) chỉ đáng dùng khi nó làm các ràng buộc (constraints / 제약조건들) và quyền sở hữu (ownership / 소유권) dễ đọc hơn. Nếu lớp trừu tượng (abstraction / 추상화) khiến nhà phát triển (developer / 개발자) phải mở ba tệp (file / 파일) để biết `padding` cuối cùng đến từ đâu, hãy giảm lớp trừu tượng (abstraction / 추상화). cấp cao (senior / 시니어) CSS không tối đa số mẫu (pattern / 패턴); cấp cao (senior / 시니어) CSS tối đa khả năng dự đoán hành vi (behavior / 동작).

---

# Kết luận

Để lên cấp cao (senior / 시니어) CSS, mục tiêu không phải là nhớ 500 thuộc tính (property / 속성).

Bạn cần đạt 5 tầng:

```text
1. Syntax + property
2. Cascade + inheritance
3. Layout mental model
4. Component/responsive architecture
5. Accessibility + performance + browser/debugging
```

Một cấp cao (senior / 시니어) frontend gặp UI bug không random đổi `display`, `position`, `z-index`, `width` cho đến khi "chạy".

Họ xác định:

```text
formatting context
→ sizing constraint
→ containing block
→ cascade
→ stacking context
→ rendering/accessibility impact
```

rồi sửa đúng nguyên nhân.

Đó là cách nên học CSS.

> **Bàn giao:** Sau **Cấp cao (senior / 시니어)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
