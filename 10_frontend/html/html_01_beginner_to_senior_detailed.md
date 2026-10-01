# HTML — Beginner → cấp cao (senior / 시니어)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **HTML — Beginner → cấp cao (senior / 시니어)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tài liệu học HTML từ số 0 đến mức có thể thiết kế và rà soát (review / 검토) markup môi trường vận hành (production / 운영 환경)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **1. HTML không phải ngôn ngữ lập trình** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Tài liệu học HTML từ số 0 đến mức có thể thiết kế và rà soát (review / 검토) markup môi trường vận hành (production / 운영 환경)

Tài liệu này được viết cho người học HTML từ đầu, không giả định bạn đã có kiến thức frontend trước đó. Mục tiêu không phải là giúp bạn nhớ thật nhiều tag, mà là xây một mô hình tư duy (mental model / 사고 모델) đủ chắc để bạn hiểu trình duyệt (browser / 브라우저) đang làm gì với HTML, vì sao ngữ nghĩa (semantic / 의미적) HTML quan trọng, khi nào nên dùng một element thay vì `div`, form thực sự submit dữ liệu như thế nào, vì sao khả năng tiếp cận (accessibility / 접근성) và SEO liên quan trực tiếp tới markup, và HTML ảnh hưởng bảo mật (security / 보안)/hiệu năng (performance / 성능) ra sao.

Nếu đọc tuần tự từ đầu đến cuối, bạn phải có thể đi từ việc viết một trang HTML cơ bản tới việc rà soát (review / 검토) markup ở mức cấp cao (senior / 시니어): hiểu document cấu trúc (structure / 구조), ngữ nghĩa (semantic / 의미적) elements, links, images, tables, forms, khả năng tiếp cận (accessibility / 접근성), script loading, siêu dữ liệu (metadata / 메타데이터), responsive images, iframe, bản địa (native / 네이티브) interactive elements và những lỗi môi trường vận hành (production / 운영 환경) phổ biến.

---

# PHẦN 1 — HTML LÀ GÌ VÀ trình duyệt (browser / 브라우저) HIỂU NÓ THẾ NÀO?

> **Chuyển mạch:** Tài liệu đặt mục tiêu ở semantics và production markup; phần HTML không phải programming language làm rõ mô hình xử lý, rồi `<!doctype html>` xác định mode parsing mà browser sẽ dùng.

## 1. HTML không phải ngôn ngữ lập trình

HTML là viết tắt của **HyperText Markup ngôn ngữ (language / 언어)**. Nó là ngôn ngữ đánh dấu dùng để mô tả cấu trúc và ý nghĩa của nội dung trên web.

Ví dụ:

```html
<h1>My Profile</h1>
<p>Hello, my name is Alice.</p>
```

HTML không chứa lô-gic (logic / 논리) theo nghĩa như Java hoặc JavaScript. Nó không có vòng lặp, lớp (class / 클래스) lô-gic nghiệp vụ (business logic / 비즈니스 로직) hay thuật toán. Vai trò chính của HTML là mô tả:

```text
đây là heading
đây là paragraph
đây là link
đây là image
đây là form
đây là button
```

Trình duyệt (browser / 브라우저) parse HTML thành DOM. CSS sử dụng DOM/element cấu trúc (structure / 구조) để presentation, còn JavaScript tương tác với DOM để thêm hành vi (behavior / 동작).

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
HTML → structure + semantics
CSS  → presentation
JS   → behavior
```

Trong dự án (project / 프로젝트) hiện đại, ba tầng (layer / 계층) có thể được viết thông qua khung phần mềm (framework / 프레임워크) như React hoặc Vue, nhưng trình duyệt (browser / 브라우저) cuối cùng vẫn phải nhận được DOM tương ứng với HTML ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** HTML không phải programming language; `<!doctype html>` khai báo parsing mode, rồi document structure tiếp theo tạo cây mà browser có thể hiểu.

## 2. `<!doctype html>`

Một HTML document hiện đại nên bắt đầu:

```html
<!doctype html>
```

DOCTYPE nói với trình duyệt (browser / 브라우저) rằng document phải được kết xuất (render / 렌더링) theo standards chế độ (mode / 모드) hiện đại.

Nó không phải một HTML element và cũng không phải closing-tag cú pháp (syntax / 문법).

Nếu thiếu doctype, trình duyệt (browser / 브라우저) có thể rơi vào **quirks chế độ (mode / 모드)**, nơi một số bố cục (layout / 레이아웃)/CSS behaviors mô phỏng web rất cũ để tương thích với legacy pages.

Vì vậy môi trường vận hành (production / 운영 환경) HTML gần như luôn có:

```html
<!doctype html>
```

ở dòng đầu.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **3. Cấu trúc tối thiểu của một HTML document** tiếp nhận điểm tựa từ **2. <!doctype html>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. <html>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Cấu trúc tối thiểu của một HTML document

Một document chuẩn thường có dạng:

```html
<!doctype html>

<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1">

  <title>My Page</title>
</head>

<body>
  <h1>Hello</h1>
</body>
</html>
```

Bạn nên hiểu từng tầng (layer / 계층) thay vì chỉ bản sao (copy / 복사) skeleton.

`html` là document element. `head` chứa siêu dữ liệu (metadata / 메타데이터) và resources liên quan document. `body` chứa nội dung chính được kết xuất (render / 렌더링)/interact.

---

# PHẦN 2 — gốc (root / 루트) DOCUMENT VÀ siêu dữ liệu (metadata / 메타데이터)

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **4. <html>** tiếp nhận điểm tựa từ **3. Cấu trúc tối thiểu của một HTML document** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. dir** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. `<html>`

`<html>` là gốc (root / 루트) element của HTML document.

```html
<html lang="vi">
```

Attribute quan trọng nhất là `lang`.

Nếu page chủ yếu bằng tiếng Việt:

```html
<html lang="vi">
```

Nếu page chủ yếu bằng tiếng Hàn:

```html
<html lang="ko">
```

Nếu tiếng Anh:

```html
<html lang="en">
```

`lang` không chỉ dành cho tìm kiếm (search / 검색) engines. Screen reader có thể dùng nó để chọn pronunciation rules. trình duyệt (browser / 브라우저) translation, spell checking và khả năng tiếp cận (accessibility / 접근성) tools cũng dựa vào ngôn ngữ (language / 언어) siêu dữ liệu (metadata / 메타데이터).

Nếu chỉ một đoạn dùng ngôn ngữ khác, khai báo ở subtree:

```html
<p>
  Trong tiếng Hàn,
  <span lang="ko">안녕하세요</span>
  nghĩa là xin chào.
</p>
```

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **5. dir** tiếp nhận điểm tựa từ **4. <html>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. <head>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. `dir`

`dir` mô tả văn bản (text / 텍스트) direction:

```html
<html dir="ltr">
```

Các giá trị quan trọng:

```text
ltr
rtl
auto
```

`rtl` thường dùng với Arabic/Hebrew contexts.

`auto` hữu ích với user-generated content khi ngôn ngữ (language / 언어) direction chưa biết trước.

Ngữ nghĩa (semantic / 의미적) direction nên được biểu diễn bằng `dir` khi nó thuộc nội dung, thay vì chỉ dựa vào CSS `direction`.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **6. <head>** tiếp nhận điểm tựa từ **5. dir** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. <meta charset="utf-8">** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. `<head>`

`head` chứa siêu dữ liệu (metadata / 메타데이터) và resources, không phải phần content chính mà người dùng (user / 사용자) đọc.

Ví dụ:

```html
<head>
  <meta charset="utf-8">
  <title>Orders</title>
  <meta
    name="description"
    content="Order management dashboard">

  <link
    rel="stylesheet"
    href="/app.css">
</head>
```

Trình duyệt (browser / 브라우저) có thể discover CSS, scripts, icons, siêu dữ liệu (metadata / 메타데이터) và preload hints trong `head`.

Nguồn (source / 소스) thứ tự (order / 순서) trong `head` cũng có thể ảnh hưởng hiệu năng (performance / 성능) vì trình duyệt (browser / 브라우저) discover resources theo thứ tự parse.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **7. <meta charset="utf-8">** tiếp nhận điểm tựa từ **6. <head>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Viewport siêu dữ liệu (metadata / 메타데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. `<meta charset="utf-8">`

Khai báo encoding:

```html
<meta charset="utf-8">
```

UTF‑8 là encoding phù hợp gần như mọi web ứng dụng (application / 애플리케이션) hiện đại.

Đặt declaration sớm trong `head` để trình duyệt (browser / 브라우저) biết cách decode bytes đúng trước khi parse content.

Nếu encoding bị hiểu sai, tiếng Việt/Hàn/Nhật có thể trở thành mojibake.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **7. <meta charset="utf-8">** nêu điều cần giải thích; **8. Viewport siêu dữ liệu (metadata / 메타데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. <title>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Viewport siêu dữ liệu (metadata / 메타데이터)

Mobile responsive page thường dùng:

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1">
```

Nếu thiếu viewport siêu dữ liệu (metadata / 메타데이터), mobile trình duyệt (browser / 브라우저) có thể giả định một desktop-like bố cục (layout / 레이아웃) viewport rồi quy mô (scale / 규모) page xuống. Khi đó CSS media queries và bố cục (layout / 레이아웃) có thể không hoạt động như bạn mong đợi.

Không nên disable người dùng (user / 사용자) zoom bừa bằng:

```text
user-scalable=no
maximum-scale=1
```

vì zoom là khả năng tiếp cận (accessibility / 접근성) năng lực (capability / 역량) quan trọng.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **8. Viewport siêu dữ liệu (metadata / 메타데이터)** nêu điều cần giải thích; **9. <title>** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Meta description** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. `<title>`

`title` định nghĩa tên document:

```html
<title>Order #1234 – Admin Portal</title>
```

Nó xuất hiện ở trình duyệt (browser / 브라우저) tab, bookmark/lịch sử (history / 이력) và có thể được tìm kiếm (search / 검색) engine dùng làm kết quả (result / 결과) title.

Một page môi trường vận hành (production / 운영 환경) nên có title cụ thể và khác nhau giữa các page quan trọng.

Ví dụ yếu:

```html
<title>Home</title>
```

Ví dụ tốt hơn:

```html
<title>Dashboard – Acme Admin</title>
```

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **10. Meta description** tiếp nhận điểm tựa từ **9. <title>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. <link>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Meta description
Phần này nối mạch bài học với “10. Meta description”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<meta
  name="description"
  content="Manage orders, refunds and payment status.">
```

Description có thể được tìm kiếm (search / 검색) engine sử dụng làm snippet.

Nó không phải “từ khóa (keyword / 키워드) hack”. Nên viết một câu mô tả thật sự hữu ích cho người đang cân nhắc click kết quả (result / 결과).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **11. <link>** tiếp nhận điểm tựa từ **10. Meta description** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. <base>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. `<link>`

`link` kết nối document với bên ngoài (external / 외부) tài nguyên (resource / 자원) hoặc mô tả relationship.

Biểu định kiểu (stylesheet / 스타일시트):

```html
<link
  rel="stylesheet"
  href="/app.css">
```

Favicon:

```html
<link
  rel="icon"
  href="/favicon.svg">
```

Chuẩn gốc (canonical / 정본) URL:

```html
<link
  rel="canonical"
  href="https://example.com/products/123">
```

Preconnect:

```html
<link
  rel="preconnect"
  href="https://cdn.example.com">
```

Preload:

```html
<link
  rel="preload"
  href="/hero.webp"
  as="image">
```

Ở mức (level / 수준) beginner, chỉ cần hiểu `rel` mô tả relationship và `href` chỉ tài nguyên (resource / 자원). Ở mức (level / 수준) cấp cao (senior / 시니어), cần biết preload/preconnect có thể giúp hoặc làm hại hiệu năng (performance / 성능) nếu sử dụng bừa.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **12. <base>** tiếp nhận điểm tựa từ **11. <link>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. <body>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. `<base>`

`base` thay đổi cách relative URLs được resolve:

```html
<base href="/app/">
```

Sau đó:

```html
<a href="users">
```

có thể resolve thành `/app/users`.

`base` ảnh hưởng rất rộng: links, images, forms, scripts và fragment điều hướng (navigation / 내비게이션) có thể bị tác động. Vì vậy môi trường vận hành (production / 운영 환경) ứng dụng (application / 애플리케이션) hiếm khi dùng nếu routing/toolchain đã quản lý URL tốt.

Khi gỡ lỗi (debug / 디버그) một page có relative URLs kỳ lạ, hãy nhớ kiểm tra `<base>`.

---

# PHẦN 3 — BODY VÀ ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조)

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **13. <body>** tiếp nhận điểm tựa từ **12. <base>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Vì sao ngữ nghĩa (semantic / 의미적) HTML quan trọng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. `<body>`

`body` chứa content của document mà người dùng (user / 사용자) chủ yếu nhìn thấy và tương tác:

```html
<body>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</body>
```

Trình duyệt (browser / 브라우저) parse body markup thành DOM. JavaScript khung phần mềm (framework / 프레임워크) có thể mutate DOM sau đó, nhưng ngữ nghĩa (semantics / 의미론) cuối vẫn dựa trên elements thực tế.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **14. Vì sao ngữ nghĩa (semantic / 의미적) HTML quan trọng?** tiếp nhận điểm tựa từ **13. <body>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. <header>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Vì sao ngữ nghĩa (semantic / 의미적) HTML quan trọng?

Bạn có thể xây gần như mọi giao diện bằng:

```html
<div>
```

và CSS.

Nhưng markup:

```html
<div class="nav">
```

không nói với trình duyệt (browser / 브라우저)/cây khả năng tiếp cận (accessibility tree / 접근성 트리) rằng đây là điều hướng (navigation / 내비게이션).

Markup:

```html
<nav>
```

có ngữ nghĩa (semantic / 의미적) rõ.

Ngữ nghĩa (semantic / 의미적) HTML giúp screen readers, keyboard users, tìm kiếm (search / 검색) engines và chính nhà phát triển (developer / 개발자) hiểu document cấu trúc (structure / 구조).

Cấp cao (senior / 시니어) HTML không có nghĩa “không bao giờ dùng div”. Nó nghĩa là dùng ngữ nghĩa (semantic / 의미적) element khi ngữ nghĩa (semantics / 의미론) phù hợp và dùng `div` khi chỉ cần generic grouping/bố cục (layout / 레이아웃).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **15. <header>** tiếp nhận điểm tựa từ **14. Vì sao ngữ nghĩa (semantic / 의미적) HTML quan trọng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. <main>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. `<header>`

`header` là phần giới thiệu/header của page hoặc một section.

Page-level:

```html
<header>
  <h1>Acme</h1>
  <nav>...</nav>
</header>
```

Article-level:

```html
<article>
  <header>
    <h2>How HTML Parsing Works</h2>
    <p>Published 12 Sep 2026</p>
  </header>
</article>
```

Một page có thể có nhiều `header` nếu chúng thuộc các sections/articles khác nhau.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **16. <main>** tiếp nhận điểm tựa từ **15. <header>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. <footer>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. `<main>`

`main` biểu diễn nội dung chính của document:

```html
<main>
  ...
</main>
```

Nó tạo landmark hữu ích cho assistive technology. người dùng (user / 사용자) dùng screen reader có thể nhảy nhanh tới main content mà không phải tab/nghe toàn điều hướng (navigation / 내비게이션).

Thông thường chỉ nên có một main đang active/visible cho document.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **17. <footer>** tiếp nhận điểm tựa từ **16. <main>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. <nav>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. `<footer>`

Footer có thể thuộc toàn page hoặc article/section.

Page footer:

```html
<footer>
  <small>© 2026 Acme</small>
</footer>
```

Article footer có thể chứa:

```text
author
tags
publication metadata
related links
```

Đừng hiểu `footer` chỉ là “phần ở dưới màn hình”. Nó là ngữ nghĩa (semantic / 의미적) footer của sectioning ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **18. <nav>** tiếp nhận điểm tựa từ **17. <footer>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. <section>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. `<nav>`

`nav` dùng cho một nhóm điều hướng (navigation / 내비게이션) links quan trọng:

```html
<nav aria-label="Main navigation">
  <a href="/">Home</a>
  <a href="/products">Products</a>
</nav>
```

Nếu có nhiều điều hướng (navigation / 내비게이션) regions, accessible label giúp phân biệt:

```html
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Footer navigation">...</nav>
```

Không phải mọi nhóm links đều cần `nav`. Một danh sách (list / 목록) links nhỏ trong article có thể chỉ là danh sách (list / 목록) bình thường.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **19. <section>** tiếp nhận điểm tựa từ **18. <nav>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. <article>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. `<section>`

`section` dùng khi một phần nội dung có chủ đề riêng và thường có heading:

```html
<section>
  <h2>Features</h2>
  ...
</section>
```

Nếu bạn chỉ cần wrapper cho CSS grid/flex mà không có ngữ nghĩa (semantic / 의미적) section, `div` thường đúng hơn.

Một dùng chung (common / 공통) beginner mistake là thay tất cả `div` bằng `section` vì nghĩ ngữ nghĩa (semantic / 의미적) luôn tốt hơn. ngữ nghĩa (semantic / 의미적) sai không tốt hơn generic element.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **20. <article>** tiếp nhận điểm tựa từ **19. <section>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. <aside>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. `<article>`

`article` phù hợp với nội dung có thể tương đối độc lập:

```html
<article>
  <h2>Understanding HTML Forms</h2>
  <p>...</p>
</article>
```

Ví dụ:

```text
blog post
news item
forum post
comment
product listing unit
independent widget
```

Mental kiểm thử (test / 테스트): nếu bản sao (copy / 복사) phần này ra khỏi page, nó vẫn có ý nghĩa độc lập không? Nếu có, `article` có thể phù hợp.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **21. <aside>** tiếp nhận điểm tựa từ **20. <article>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. <address>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. `<aside>`

`aside` biểu diễn nội dung phụ hoặc tangentially related:

```html
<aside>
  <h2>Related articles</h2>
  ...
</aside>
```

Không dùng `aside` chỉ vì CSS đặt nó bên phải. Vị trí visual không quyết định ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **22. <address>** tiếp nhận điểm tựa từ **21. <aside>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. <h1> đến <h6>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. `<address>`

`address` dùng cho contact thông tin (information / 정보) liên quan tới page/article:

```html
<address>
  Contact
  <a href="mailto:support@example.com">
    support@example.com
  </a>
</address>
```

Nó không phải generic tag cho mọi postal address.

---

# PHẦN 4 — HEADINGS VÀ văn bản (text / 텍스트) cấu trúc (structure / 구조)

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **23. <h1> đến <h6>** tiếp nhận điểm tựa từ **22. <address>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. <p>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. `<h1>` đến `<h6>`

Heading biểu diễn hierarchy.

```html
<h1>HTML Guide</h1>

<h2>Forms</h2>

<h3>Input Types</h3>
```

Đừng chọn heading theo font kích thước (size / 크기). Nếu muốn văn bản (text / 텍스트) lớn hơn, dùng CSS.

Heading hierarchy giúp người dùng (user / 사용자) scan page, screen reader điều hướng (navigation / 내비게이션) và tìm kiếm (search / 검색) engine hiểu cấu trúc (structure / 구조).

Một cấp cao (senior / 시니어) rà soát (review / 검토) sẽ kiểm tra “heading có mô tả hierarchy nội dung đúng không?” chứ không chỉ “có h1 chưa?”.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **24. <p>** tiếp nhận điểm tựa từ **23. <h1> đến <h6>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. <div>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. `<p>`

Paragraph:

```html
<p>
  HTML describes the structure and semantics of a document.
</p>
```

`p` dành cho paragraph văn bản (text / 텍스트), không phải generic bộ chứa (container / 컨테이너).

Không nên đặt khối (block / 블록) structures không phù hợp bên trong `p`; trình duyệt (browser / 브라우저) parser có thể tự đóng `p`, khiến DOM khác nguồn (source / 소스) bạn tưởng. Phần Master sẽ giải thích parser hành vi (behavior / 동작) này kỹ hơn.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **25. <div>** tiếp nhận điểm tựa từ **24. <p>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. <span>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. `<div>`

`div` là generic luồng (flow / 흐름) bộ chứa (container / 컨테이너):

```html
<div class="card">
  ...
</div>
```

Nó không mang ngữ nghĩa (semantic / 의미적) riêng.

Dùng `div` khi bạn chỉ cần grouping/bố cục (layout / 레이아웃) hoặc khi không có ngữ nghĩa (semantic / 의미적) element phù hợp.

Một cấp cao (senior / 시니어) không tránh `div`; cấp cao (senior / 시니어) tránh **div soup khi bản địa (native / 네이티브) ngữ nghĩa (semantics / 의미론) đã tồn tại**.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **26. <span>** tiếp nhận điểm tựa từ **25. <div>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. <br>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. `<span>`

`span` là generic inline/phrasing bộ chứa (container / 컨테이너):

```html
<p>
  Price:
  <span class="price">$100</span>
</p>
```

Nó không mang ngữ nghĩa (semantics / 의미론) riêng.

Dùng để style hoặc attach hành vi (behavior / 동작)/dữ liệu (data / 데이터) cho một đoạn inline khi không có ngữ nghĩa (semantic / 의미적) element thích hợp.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **27. <br>** tiếp nhận điểm tựa từ **26. <span>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. <hr>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. `<br>`

`br` tạo line break:

```html
123 Main Street<br>
Seoul
```

Phù hợp khi line break là một phần nội dung, ví dụ address hoặc poem.

Không dùng:

```html
<br><br><br>
```

để tạo spacing. Spacing thuộc CSS.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **28. <hr>** tiếp nhận điểm tựa từ **27. <br>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. <strong> và <b>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. `<hr>`

`hr` biểu diễn thematic break:

```html
<section>Topic A</section>

<hr>

<section>Topic B</section>
```

Trình duyệt (browser / 브라우저) thường kết xuất (render / 렌더링) một đường ngang, nhưng ngữ nghĩa (semantic / 의미적) chính không phải “vẽ line”.

---

# PHẦN 5 — văn bản (text / 텍스트) ngữ nghĩa (semantics / 의미론)

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **29. <strong> và <b>** tiếp nhận điểm tựa từ **28. <hr>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. <em> và <i>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. `<strong>` và `<b>`

`strong` biểu diễn strong importance:

```html
<strong>Do not share your password.</strong>
```

`b` chủ yếu thu hút attention mà không nói nội dung quan trọng hơn về ngữ nghĩa (semantics / 의미론):

```html
<b>Keyword:</b> HTML
```

Cả hai thường bold mặc định, nhưng ý nghĩa khác.

Nếu mục tiêu chỉ là font-weight, CSS mới là công cụ styling.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **30. <em> và <i>** tiếp nhận điểm tựa từ **29. <strong> và <b>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. <mark>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. `<em>` và `<i>`

`em` biểu diễn stress emphasis:

```html
I <em>really</em> need this.
```

`i` dùng cho alternate voice, technical term, taxonomy, foreign phrase hoặc convention phù hợp:

```html
<i lang="la">Homo sapiens</i>
```

Trình duyệt (browser / 브라우저) thường italic cả hai, nhưng ngữ nghĩa (semantics / 의미론) khác.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **31. <mark>** tiếp nhận điểm tựa từ **30. <em> và <i>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. <small>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. `<mark>`

`mark` highlight content relevant trong ngữ cảnh (context / 맥락):

```html
Search result:
<mark>HTML</mark>
```

Rất phù hợp với tìm kiếm (search / 검색) kết quả (result / 결과) highlighting hoặc đoạn được tham chiếu (reference / 참조).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **32. <small>** tiếp nhận điểm tựa từ **31. <mark>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. <s>, <del> và <ins>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. `<small>`

`small` dành cho side comments/small print:

```html
<small>Terms and conditions apply.</small>
```

Không nên dùng chỉ vì muốn font-size nhỏ.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **33. <s>, <del> và <ins>** tiếp nhận điểm tựa từ **32. <small>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. <code>, <pre>, <kbd>, <samp>, <var>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. `<s>`, `<del>` và `<ins>`

`s` biểu diễn content không còn accurate/relevant:

```html
<s>$100</s> $70
```

`del` và `ins` biểu diễn edit lịch sử (history / 이력):

```html
<del>$100</del>
<ins>$70</ins>
```

Có thể thêm siêu dữ liệu (metadata / 메타데이터) như `datetime`.

Nếu đang hiển thị old price, `s` thường hợp hơn `del`, vì bạn không nhất thiết đang mô tả document edit.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **34. <code>, <pre>, <kbd>, <samp>, <var>** tiếp nhận điểm tựa từ **33. <s>, <del> và <ins>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. <abbr>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. `<code>`, `<pre>`, `<kbd>`, `<samp>`, `<var>`

Inline mã (code / 코드):

```html
<code>npm install</code>
```

Mã (code / 코드) khối (block / 블록):

```html
<pre><code>const x = 1;</code></pre>
```

`pre` preserve whitespace.

`kbd` biểu diễn người dùng (user / 사용자) đầu vào (input / 입력):

```html
Press <kbd>Ctrl</kbd> + <kbd>C</kbd>.
```

`samp` biểu diễn program đầu ra (output / 출력):

```html
<samp>404 Not Found</samp>
```

`var` biểu diễn variable:

```html
<var>x</var> + <var>y</var>
```

Những tags này giúp technical documentation có ngữ nghĩa (semantics / 의미론) rõ hơn.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **35. <abbr>** tiếp nhận điểm tựa từ **34. <code>, <pre>, <kbd>, <samp>, <var>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. <blockquote> và <q>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. `<abbr>`
Phần này nối mạch bài học với “35. `<abbr>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<abbr title="HyperText Markup Language">
  HTML
</abbr>
```

Dùng cho abbreviation.

`title` chỉ nên là supplemental thông tin (information / 정보), không nên là nơi duy nhất chứa trọng yếu (critical / 중요) thông tin (information / 정보) vì touch/assistive environments không phải lúc nào expose tooltip giống desktop mouse.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **36. <blockquote> và <q>** tiếp nhận điểm tựa từ **35. <abbr>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. <cite>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. `<blockquote>` và `<q>`

Khối (block / 블록) quote:

```html
<blockquote>
  The Web is for everyone.
</blockquote>
```

Inline quote:

```html
<p>He said <q>Hello</q>.</p>
```

`blockquote[cite]` có thể chứa nguồn (source / 소스) URI siêu dữ liệu (metadata / 메타데이터), nhưng trình duyệt (browser / 브라우저) không tự hiển thị citation cho người dùng (user / 사용자).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **37. <cite>** tiếp nhận điểm tựa từ **36. <blockquote> và <q>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. <time>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. `<cite>`

`cite` biểu diễn title của creative công việc (work / 작업):

```html
<cite>Clean Code</cite>
```

Không phải generic “nguồn URL” tag.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **38. <time>** tiếp nhận điểm tựa từ **37. <cite>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. <data>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. `<time>`
Phần này nối mạch bài học với “38. `<time>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<time datetime="2026-09-12">
  12 Sep 2026
</time>
```

`datetime` cung cấp machine-readable biểu diễn (representation / 표현).

Date/thời gian (time / 시간) ngữ nghĩa (semantics / 의미론) hữu ích với structured content, parsers và machine processing.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **39. <data>** tiếp nhận điểm tựa từ **38. <time>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. <sub> và <sup>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. `<data>`
Phần này nối mạch bài học với “39. `<data>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<data value="SKU-123">
  Blue Shirt
</data>
```

Visible văn bản (text / 텍스트) có thể khác machine giá trị (value / 값).

Hữu ích trong sản phẩm (product / 제품)/danh mục (catalog / 카탈로그)/data-oriented markup.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **40. <sub> và <sup>** tiếp nhận điểm tựa từ **39. <data>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. <bdi> và <bdo>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. `<sub>` và `<sup>`
Phần này nối mạch bài học với “40. `<sub>` và `<sup>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
H<sub>2</sub>O
```

```html
x<sup>2</sup>
```

Dùng cho subscript/superscript ngữ nghĩa (semantics / 의미론), không chỉ visual positioning.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **41. <bdi> và <bdo>** tiếp nhận điểm tựa từ **40. <sub> và <sup>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Ruby annotations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. `<bdi>` và `<bdo>`

`bdi` isolate bidirectional user-generated văn bản (text / 텍스트):

```html
User: <bdi>اسم</bdi>
```

Nó hữu ích khi UI left-to-right chứa username right-to-left.

`bdo` force direction:

```html
<bdo dir="rtl">ABC</bdo>
```

`bdo` hiếm hơn và nên dùng có chủ đích.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **42. Ruby annotations** tiếp nhận điểm tựa từ **41. <bdi> và <bdo>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. <ul>, <ol>, <li>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Ruby annotations

East Asian pronunciation annotations:

```html
<ruby>
  漢
  <rt>かん</rt>
</ruby>
```

`rt` chứa annotation/pronunciation. `rp` hỗ trợ fallback presentation cho old environments.

---

# PHẦN 6 — LISTS

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **43. <ul>, <ol>, <li>** tiếp nhận điểm tựa từ **42. Ruby annotations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Description list** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. `<ul>`, `<ol>`, `<li>`

Unordered danh sách (list / 목록):

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>
```

Ordered danh sách (list / 목록):

```html
<ol>
  <li>Install</li>
  <li>Configure</li>
  <li>Run</li>
</ol>
```

Dùng `ol` khi thứ tự (order / 순서) mang meaning, `ul` khi thứ tự (order / 순서) không quan trọng.

Đừng tạo danh sách (list / 목록) visual bằng nhiều `div` nếu content thật sự là danh sách (list / 목록).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **44. Description list** tiếp nhận điểm tựa từ **43. <ul>, <ol>, <li>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. <a>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Description list
Phần này nối mạch bài học với “44. Description list”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<dl>
  <dt>HTML</dt>
  <dd>Defines structure and semantics.</dd>

  <dt>CSS</dt>
  <dd>Defines presentation.</dd>
</dl>
```

`dl` rất phù hợp với glossary, siêu dữ liệu (metadata / 메타데이터) hoặc term-description pairs.

---

# PHẦN 7 — LINKS VÀ điều hướng (navigation / 내비게이션)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **45. <a>** tiếp nhận điểm tựa từ **44. Description list** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Link và button khác nhau ở bản chất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. `<a>`

Anchor tạo hyperlink:

```html
<a href="/profile">
  Profile
</a>
```

`href` có thể là:

```text
relative URL
absolute URL
fragment
mailto:
tel:
```

Ví dụ:

```html
<a href="#pricing">Pricing</a>
<a href="mailto:support@example.com">Email</a>
<a href="tel:+821012345678">Call</a>
```

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **46. Link và button khác nhau ở bản chất** tiếp nhận điểm tựa từ **45. <a>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. target="blank"** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Link và button khác nhau ở bản chất

Nếu tương tác (interaction / 상호작용) thay đổi URL/location hoặc navigate tới tài nguyên (resource / 자원) khác, dùng link:

```html
<a href="/profile">Profile</a>
```

Nếu tương tác (interaction / 상호작용) thực hiện hành động (action / 동작) trong hiện tại (current / 현재) ứng dụng (application / 애플리케이션) trạng thái (state / 상태), dùng button:

```html
<button type="button">
  Open profile panel
</button>
```

Đây là một trong những rules quan trọng nhất của ngữ nghĩa (semantic / 의미적) HTML.

Không dùng `<a href="#">` để fake button nếu không có điều hướng (navigation / 내비게이션) ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **47. target="blank"** tiếp nhận điểm tựa từ **46. Link và button khác nhau ở bản chất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. rel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. `target="_blank"`
Phần này nối mạch bài học với “47. `target="_blank"`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<a
  href="https://example.com"
  target="_blank">
  External site
</a>
```

Mở browsing ngữ cảnh (context / 맥락) mới.

Khi dùng bên ngoài (external / 외부) links, `rel` có thể cần tùy bảo mật (security / 보안)/privacy/relationship requirements.

Hiện đại (modern / 현대적) browsers có behaviors bảo vệ opener tốt hơn trước, nhưng hiểu `noopener`/`noreferrer` vẫn quan trọng khi rà soát (review / 검토) legacy hoặc tường minh (explicit / 명시적) policies.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **48. rel** tiếp nhận điểm tựa từ **47. target="blank"** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. download** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. `rel`

`rel` mô tả relationship:

```html
<a
  href="..."
  rel="nofollow sponsored">
```

Dùng chung (common / 공통) concepts:

```text
noopener
noreferrer
nofollow
ugc
sponsored
author
license
```

SEO quan hệ (relation / 관계) tokens không phải bảo mật (security / 보안) controls.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **49. download** tiếp nhận điểm tựa từ **48. rel** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. <img>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. `download`
Phần này nối mạch bài học với “49. `download`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<a
  href="/report.pdf"
  download>
  Download report
</a>
```

Nó là trình duyệt (browser / 브라우저) hint cho download hành vi (behavior / 동작) trong applicable cases.

Đừng dùng nó như access-control/bảo mật (security / 보안) cơ chế (mechanism / 메커니즘).

---

# PHẦN 8 — IMAGES VÀ RESPONSIVE IMAGES

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **50. <img>** tiếp nhận điểm tựa từ **49. download** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Viết alt đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. `<img>`
Phần này nối mạch bài học với “50. `<img>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<img
  src="/team.jpg"
  alt="Engineering team discussing a system diagram">
```

`src` chỉ tài nguyên (resource / 자원).

`alt` cung cấp văn bản (text / 텍스트) alternative khi ảnh (image / 이미지) không thể/không nên được consumed visually.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **51. Viết alt đúng** tiếp nhận điểm tựa từ **50. <img>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. width và height** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Viết `alt` đúng

Informative ảnh (image / 이미지):

```html
<img
  src="/growth-chart.png"
  alt="Revenue increased from 20 to 35 million dollars between Q1 and Q4">
```

Decorative ảnh (image / 이미지):

```html
<img
  src="/separator.svg"
  alt="">
```

`alt=""` không có nghĩa “quên alt”; nó cố ý nói ảnh (image / 이미지) decorative và không cần screen reader announce.

Alt tốt mô tả **purpose trong ngữ cảnh (context / 맥락)**, không phải liệt kê mọi điểm ảnh (pixel / 픽셀).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **52. width và height** tiếp nhận điểm tựa từ **51. Viết alt đúng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. loading** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. `width` và `height`
Phần này nối mạch bài học với “52. `width` và `height`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<img
  src="/hero.jpg"
  width="1200"
  height="800"
  alt="...">
```

Attributes này giúp trình duyệt (browser / 브라우저) biết intrinsic aspect ratio và reserve bố cục (layout / 레이아웃) không gian (space / 공간) trước khi ảnh (image / 이미지) tải (load / 로드).

Điều đó giúp giảm bố cục (layout / 레이아웃) shift.

Bạn vẫn có thể resize responsive bằng CSS:

```css
img {
  max-width: 100%;
  height: auto;
}
```

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **53. loading** tiếp nhận điểm tựa từ **52. width và height** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. srcset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. `loading`
Phần này nối mạch bài học với “53. `loading`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<img
  loading="lazy"
  src="/below-fold.jpg"
  alt="...">
```

Lazy loading phù hợp với images ngoài viewport.

Không nên lazy-load hero/LCP ảnh (image / 이미지) một cách máy móc vì trình duyệt (browser / 브라우저) có thể discover/fetch nó muộn hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **54. srcset** tiếp nhận điểm tựa từ **53. loading** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. sizes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. `srcset`
Phần này nối mạch bài học với “54. `srcset`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<img
  src="/photo-800.jpg"
  srcset="
    /photo-400.jpg 400w,
    /photo-800.jpg 800w,
    /photo-1200.jpg 1200w"
  alt="...">
```

Bạn cung cấp ảnh (image / 이미지) candidates; trình duyệt (browser / 브라우저) chọn candidate dựa trên viewport, thiết bị (device / 장치) điểm ảnh (pixel / 픽셀) ratio và expected kết xuất (render / 렌더링) width.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **55. sizes** tiếp nhận điểm tựa từ **54. srcset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. <picture>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. `sizes`
Phần này nối mạch bài học với “55. `sizes`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<img
  srcset="
    /photo-400.jpg 400w,
    /photo-800.jpg 800w,
    /photo-1200.jpg 1200w"
  sizes="
    (max-width: 600px) 100vw,
    800px"
  src="/photo-800.jpg"
  alt="...">
```

`sizes` nói trình duyệt (browser / 브라우저) ảnh (image / 이미지) dự kiến kết xuất (render / 렌더링) rộng bao nhiêu trong các viewport conditions.

Nếu `sizes` sai, trình duyệt (browser / 브라우저) có thể chọn tài nguyên (resource / 자원) quá lớn hoặc quá nhỏ.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **56. <picture>** tiếp nhận điểm tựa từ **55. sizes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. <figure> và <figcaption>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. `<picture>`

`picture` dùng khi nguồn (source / 소스) selection cần art direction hoặc format alternatives:

```html
<picture>
  <source
    srcset="/hero.avif"
    type="image/avif">

  <source
    srcset="/hero.webp"
    type="image/webp">

  <img
    src="/hero.jpg"
    width="1200"
    height="800"
    alt="Engineering team">
</picture>
```

`srcset` trên img thường giải quyết resolution/kích thước (size / 크기) selection. `picture` giải quyết nguồn (source / 소스) choice theo media/kiểu (type / 타입)/art direction.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **57. <figure> và <figcaption>** tiếp nhận điểm tựa từ **56. <picture>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. <audio>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. `<figure>` và `<figcaption>`
Phần này nối mạch bài học với “57. `<figure>` và `<figcaption>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<figure>
  <img
    src="/architecture.png"
    alt="Three-layer system architecture">

  <figcaption>
    Figure 1. Application architecture
  </figcaption>
</figure>
```

Figure phù hợp với ảnh (image / 이미지), diagram, chart, mã (code / 코드) mẫu (sample / 표본) hoặc content có caption riêng.

---

# PHẦN 9 — AUDIO, VIDEO VÀ EMBEDDED CONTENT

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **58. <audio>** tiếp nhận điểm tựa từ **57. <figure> và <figcaption>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. <video>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. `<audio>`
Phần này nối mạch bài học với “58. `<audio>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<audio
  controls
  src="/lesson.mp3">
</audio>
```

Attributes phổ biến:

```text
controls
autoplay
loop
muted
preload
```

Autoplay có nhiều trình duyệt (browser / 브라우저) restrictions, đặc biệt nếu có audio.

`preload` là hint, không phải absolute command.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **59. <video>** tiếp nhận điểm tựa từ **58. <audio>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. <source>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. `<video>`
Phần này nối mạch bài học với “59. `<video>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<video
  controls
  width="800"
  poster="/poster.jpg"
  playsinline>

  <source
    src="/movie.mp4"
    type="video/mp4">

</video>
```

`poster` là preview ảnh (image / 이미지) trước playback.

`playsinline` giúp playback inline trong supporting mobile environments.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **59. <video>** nêu điều cần giải thích; **60. <source>** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **61. <track>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. `<source>`

Media có thể cung cấp nhiều sources:

```html
<video controls>
  <source
    src="/movie.webm"
    type="video/webm">

  <source
    src="/movie.mp4"
    type="video/mp4">
</video>
```

Trình duyệt (browser / 브라우저) dùng năng lực (capability / 역량)/kiểu (type / 타입) hints để chọn phù hợp.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **60. <source>** nêu điều cần giải thích; **61. <track>** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **62. <iframe>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 61. `<track>`
Phần này nối mạch bài học với “61. `<track>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<track
  kind="captions"
  src="/captions-en.vtt"
  srclang="en"
  label="English">
```

`captions` thường chứa cả speech và relevant sound descriptions cho khả năng tiếp cận (accessibility / 접근성). `subtitles` chủ yếu dịch/transcribe dialogue cho người vẫn nghe được audio.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **62. <iframe>** tiếp nhận điểm tựa từ **61. <track>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **63. sandbox** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 62. `<iframe>`
Phần này nối mạch bài học với “62. `<iframe>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<iframe
  src="https://example.com"
  title="Payment page">
</iframe>
```

Iframe embed một browsing ngữ cảnh (context / 맥락) khác.

`title` giúp assistive technology biết iframe dùng để làm gì.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **63. sandbox** tiếp nhận điểm tựa từ **62. <iframe>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **64. allow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 63. `sandbox`
Phần này nối mạch bài học với “63. `sandbox`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<iframe
  src="https://third-party.example"
  sandbox>
</iframe>
```

Empty sandbox áp nhiều restrictions.

Bạn mở năng lực (capability / 역량) từng phần:

```html
sandbox="allow-scripts allow-forms"
```

Cấp cao (senior / 시니어) bảo mật (security / 보안) principle là **least privilege**: chỉ allow năng lực (capability / 역량) thực sự cần.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **64. allow** tiếp nhận điểm tựa từ **63. sandbox** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **65. srcdoc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 64. `allow`
Phần này nối mạch bài học với “64. `allow`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<iframe
  src="..."
  allow="camera; microphone">
</iframe>
```

Permissions chính sách (policy / 정책) cho iframe capabilities.

Đừng cấp camera/microphone/location-like capabilities nếu embedded app không cần.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **65. srcdoc** tiếp nhận điểm tựa từ **64. allow** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **66. <table>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 65. `srcdoc`
Phần này nối mạch bài học với “65. `srcdoc`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<iframe
  srcdoc="<h1>Hello</h1>">
</iframe>
```

`srcdoc` chứa HTML document inline.

Nếu content đến từ người dùng (user / 사용자)/untrusted nguồn (source / 소스), đây là HTML thực thi (execution / 실행) ngữ cảnh (context / 맥락) và có XSS implications. Nó không phải plain văn bản (text / 텍스트) bộ chứa (container / 컨테이너).

---

# PHẦN 10 — TABLES

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **66. <table>** tiếp nhận điểm tựa từ **65. srcdoc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **67. <caption>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 66. `<table>`

Bảng (table / 테이블) dùng cho tabular dữ liệu (data / 데이터), không dùng làm page bố cục (layout / 레이아웃).

```html
<table>
  ...
</table>
```

Hiện đại (modern / 현대적) bố cục (layout / 레이아웃) dùng CSS Grid/Flexbox.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **67. <caption>** tiếp nhận điểm tựa từ **66. <table>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **68. Table structure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 67. `<caption>`
Phần này nối mạch bài học với “67. `<caption>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<table>
  <caption>Monthly Revenue</caption>
  ...
</table>
```

Caption mô tả mục đích/nội dung bảng (table / 테이블) và rất hữu ích cho khả năng tiếp cận (accessibility / 접근성).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **68. Table structure** tiếp nhận điểm tựa từ **67. <caption>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **69. scope** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 68. Table structure
Phần này nối mạch bài học với “68. Table structure”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<table>
  <thead>
    <tr>
      <th scope="col">Product</th>
      <th scope="col">Price</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Keyboard</th>
      <td>$100</td>
    </tr>
  </tbody>
</table>
```

`tr` là row, `th` là header cell, `td` là dữ liệu (data / 데이터) cell.

`thead`, `tbody`, `tfoot` tạo logical groups.

Trình duyệt (browser / 브라우저) parser có table-specific rules; nguồn (source / 소스) và resulting DOM có thể khác nếu markup thiếu/invalid. Phần Master sẽ giải thích.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **69. scope** tiếp nhận điểm tựa từ **68. Table structure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **70. rowspan và colspan** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 69. `scope`
Phần này nối mạch bài học với “69. `scope`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<th scope="col">Price</th>
```

hoặc:

```html
<th scope="row">Keyboard</th>
```

Phạm vi (scope / 범위) giúp associate header với cells trong bảng (table / 테이블) đơn giản.

Complex bảng (table / 테이블) có thể cần `headers`/`id` strategies, nhưng đừng làm bảng (table / 테이블) phức tạp hơn nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **70. rowspan và colspan** tiếp nhận điểm tựa từ **69. scope** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **71. <form>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 70. `rowspan` và `colspan`
Phần này nối mạch bài học với “70. `rowspan` và `colspan`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<td colspan="2">Total</td>
```

```html
<th rowspan="2">Region</th>
```

Dùng cho merged cells.

Merged bảng (table / 테이블) structures cần kiểm thử (test / 테스트) khả năng tiếp cận (accessibility / 접근성) cẩn thận vì association trở nên phức tạp.

---

# PHẦN 11 — FORMS: PHẦN QUAN TRỌNG NHẤT CỦA HTML ứng dụng (application / 애플리케이션)

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **71. <form>** tiếp nhận điểm tựa từ **70. rowspan và colspan** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **72. action** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 71. `<form>`
Phần này nối mạch bài học với “71. `<form>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<form
  action="/login"
  method="post">
  ...
</form>
```

Form không chỉ là visual wrapper. Nó là một cơ chế (mechanism / 메커니즘) browser-native để collect successful controls và submit dữ liệu (data / 데이터) tới URL.

Đây là lý do hiểu bản địa (native / 네이티브) form ngữ nghĩa (semantics / 의미론) cực kỳ quan trọng dù bạn dùng React.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **72. action** tiếp nhận điểm tựa từ **71. <form>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **73. method** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 72. `action`
Phần này nối mạch bài học với “72. `action`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<form action="/users">
```

`action` là URL mục tiêu (target / 대상) khi form submit.

Nếu ứng dụng (application / 애플리케이션) intercept submit bằng JavaScript, bản địa (native / 네이티브) hành động (action / 동작) vẫn có thể là progressive enhancement fallback tùy kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **73. method** tiếp nhận điểm tựa từ **72. action** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **74. enctype** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 73. `method`

Dùng chung (common / 공통):

```html
method="get"
```

và:

```html
method="post"
```

GET phù hợp với safe truy vấn (query / 쿼리)/tìm kiếm (search / 검색)/filter điều hướng (navigation / 내비게이션), nơi dữ liệu (data / 데이터) có thể nằm trong URL.

POST phù hợp với state-changing submission hoặc payload không nên encoded như truy vấn (query / 쿼리).

HTML phương thức (method / 메서드) ngữ nghĩa (semantics / 의미론) không thay HTTP authorization/bảo mật (security / 보안) rules.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **74. enctype** tiếp nhận điểm tựa từ **73. method** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **75. <label>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 74. `enctype`

Default form encoding thường là:

```text
application/x-www-form-urlencoded
```

Tệp (file / 파일) upload cần:

```html
<form
  method="post"
  enctype="multipart/form-data">
```

Nếu quên multipart, tệp (file / 파일) dữ liệu (data / 데이터) sẽ không được submit đúng như bạn mong đợi.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **74. enctype** cho ta quy tắc; **75. <label>** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **76. Placeholder không phải label** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 75. `<label>`
Phần này nối mạch bài học với “75. `<label>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<label for="email">
  Email
</label>

<input
  id="email"
  name="email"
  type="email">
```

`for` match `id`.

Label không chỉ là văn bản (text / 텍스트) cạnh đầu vào (input / 입력). Nó tạo association khả năng tiếp cận (accessibility / 접근성) và click/tap hành vi (behavior / 동작).

Bạn cũng có thể wrap điều khiển (control / 제어):

```html
<label>
  Email
  <input
    name="email"
    type="email">
</label>
```

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **75. <label>** cho ta quy tắc; **76. Placeholder không phải label** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **77. <input>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 76. Placeholder không phải label

Sai:

```html
<input
  type="email"
  placeholder="Email">
```

nếu không có label.

Placeholder biến mất khi người dùng (user / 사용자) nhập và thường có contrast/khả năng tiếp cận (accessibility / 접근성) issues.

Tốt hơn:

```html
<label for="email">Email</label>

<input
  id="email"
  name="email"
  type="email"
  placeholder="name@example.com">
```

Placeholder nên là hint/example, không phải trường dữ liệu (field / 필드) name chính.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **76. Placeholder không phải label** cho ta quy tắc; **77. <input>** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **78. text** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 77. `<input>`

Đầu vào (input / 입력) là form điều khiển (control / 제어) đa năng:

```html
<input
  type="text"
  name="username">
```

Ba attributes phải hiểu sâu là:

```text
type
name
value
```

`type` chọn hành vi (behavior / 동작)/ngữ nghĩa (semantics / 의미론).

`name` là key trong form submission.

`value` liên quan hiện tại (current / 현재)/default/submitted giá trị (value / 값) tùy đầu vào (input / 입력) kiểu (type / 타입)/trạng thái (state / 상태).

---

# PHẦN 12 — đầu vào (input / 입력) TYPES

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **78. text** tiếp nhận điểm tựa từ **77. <input>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **79. password** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 78. `text`
Phần này nối mạch bài học với “78. `text`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="text"
  name="displayName">
```

General single-line văn bản (text / 텍스트).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **79. password** tiếp nhận điểm tựa từ **78. text** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **80. email** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 79. `password`
Phần này nối mạch bài học với “79. `password`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="password"
  name="password"
  autocomplete="current-password">
```

Nó che visual characters. Nó không encrypt mạng (network / 네트워크) payload.

Bảo mật (security / 보안) vẫn phụ thuộc HTTPS, máy chủ (server / 서버) lưu trữ (storage / 저장소) và authentication kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **80. email** tiếp nhận điểm tựa từ **79. password** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **81. number** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 80. `email`
Phần này nối mạch bài học với “80. `email`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="email"
  name="email"
  autocomplete="email"
  required>
```

Trình duyệt (browser / 브라우저) cung cấp email-specific kiểm tra hợp lệ (validation / 검증) ngữ nghĩa (semantics / 의미론) và mobile keyboard hints.

Máy chủ (server / 서버) vẫn phải validate email/nghiệp vụ (business / 비즈니스) rules.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **81. number** tiếp nhận điểm tựa từ **80. email** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **82. search, tel, url** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 81. `number`
Phần này nối mạch bài học với “81. `number`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="number"
  name="quantity"
  min="1"
  max="100"
  step="1">
```

Dùng cho quantity thực sự có numerical meaning.

Không dùng cho phone number, credit card, postal mã (code / 코드) hoặc ID vì chúng không phải quantities; leading zero và formatting có thể quan trọng.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **82. search, tel, url** tiếp nhận điểm tựa từ **81. number** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **83. checkbox** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 82. `search`, `tel`, `url`

Tìm kiếm (search / 검색):

```html
<input type="search">
```

Telephone:

```html
<input type="tel">
```

URL:

```html
<input type="url">
```

`tel` không validate universal phone format vì formats quá đa dạng.

`url` có URL ràng buộc (constraint / 제약조건) ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **83. checkbox** tiếp nhận điểm tựa từ **82. search, tel, url** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **84. radio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 83. `checkbox`
Phần này nối mạch bài học với “83. `checkbox`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="checkbox"
  name="agree"
  value="yes">
```

Nếu checked, form có thể submit:

```text
agree=yes
```

Nếu unchecked, trường dữ liệu (field / 필드) thường không có entry trong submitted dữ liệu (data / 데이터).

Đây là hành vi (behavior / 동작) quan trọng khi backend phân biệt false và missing.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **84. radio** tiếp nhận điểm tựa từ **83. checkbox** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **85. Date/time types** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 84. `radio`
Phần này nối mạch bài học với “84. `radio`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<label>
  <input
    type="radio"
    name="plan"
    value="basic">
  Basic
</label>

<label>
  <input
    type="radio"
    name="plan"
    value="pro">
  Pro
</label>
```

Radio cùng `name` tạo group và thường chỉ một item được selected.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **85. Date/time types** tiếp nhận điểm tựa từ **84. radio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **86. range** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 85. Date/time types
Phần này nối mạch bài học với “85. Date/time types”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input type="date">
<input type="time">
<input type="datetime-local">
<input type="month">
<input type="week">
```

`datetime-local` không tự mang timezone.

Nếu backend cần toàn cục (global / 전역) instant, timezone phải được xác định ở tầng (layer / 계층) khác.

UI display cũng phụ thuộc locale/trình duyệt (browser / 브라우저).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **86. range** tiếp nhận điểm tựa từ **85. Date/time types** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **87. color** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 86. `range`
Phần này nối mạch bài học với “86. `range`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="range"
  min="0"
  max="100"
  value="50">
```

Slider tốt cho approximate phạm vi (range / 범위) đầu vào (input / 입력).

Nếu chính xác (exact / 정확한) giá trị (value / 값) quan trọng, nên hiển thị giá trị (value / 값) hiện tại bên cạnh.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **87. color** tiếp nhận điểm tựa từ **86. range** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **88. file** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 87. `color`
Phần này nối mạch bài học với “87. `color`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="color"
  name="themeColor">
```

Bản địa (native / 네이티브) color picker trong supporting browsers.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **88. file** tiếp nhận điểm tựa từ **87. color** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **89. hidden** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 88. `file`
Phần này nối mạch bài học với “88. `file`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="file"
  name="avatar"
  accept="image/*">
```

Multiple:

```html
<input
  type="file"
  name="attachments"
  multiple>
```

`accept` chỉ là file-picker hint. máy chủ (server / 서버) vẫn phải validate kiểu (type / 타입), kích thước (size / 크기), tệp (file / 파일) signature/content và malware chính sách (policy / 정책).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **89. hidden** tiếp nhận điểm tựa từ **88. file** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **90. name** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 89. `hidden`
Phần này nối mạch bài học với “89. `hidden`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="hidden"
  name="csrf"
  value="...">
```

Hidden fields vẫn thuộc máy khách (client / 클라이언트) DOM/yêu cầu (request / 요청).

Không bao giờ coi hidden giá trị (value / 값) là secret/trusted authorization dữ liệu (data / 데이터). người dùng (user / 사용자) có thể sửa yêu cầu (request / 요청) bằng DevTools hoặc HTTP máy khách (client / 클라이언트).

---

# PHẦN 13 — đầu vào (input / 입력) ATTRIBUTES VÀ FORM kiểm tra hợp lệ (validation / 검증)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **90. name** tiếp nhận điểm tựa từ **89. hidden** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **91. value** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 90. `name`
Phần này nối mạch bài học với “90. `name`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  name="email"
  value="a@example.com">
```

`name` tạo key cho form dữ liệu (data / 데이터).

Nếu điều khiển (control / 제어) không có `name`, nó thường không đóng góp entry vào form submission.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **91. value** tiếp nhận điểm tựa từ **90. name** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **92. required** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 91. `value`

Markup:

```html
<input value="Alice">
```

Đây là initial/default giá trị (value / 값) relationship.

Sau người dùng (user / 사용자) edit, DOM thuộc tính (property / 속성):

```js
input.value
```

có thể là `"Bob"` trong khi:

```js
input.getAttribute("value")
```

vẫn phản ánh markup attribute `"Alice"`.

Đây là bước đầu để hiểu difference giữa **content attribute** và **IDL/DOM thuộc tính (property / 속성)**.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **92. required** tiếp nhận điểm tựa từ **91. value** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **93. disabled** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 92. `required`
Phần này nối mạch bài học với “92. `required`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="email"
  required>
```

Trình duyệt (browser / 브라우저) bản địa (native / 네이티브) ràng buộc (constraint / 제약조건) kiểm tra hợp lệ (validation / 검증) có thể khối (block / 블록) submission nếu giá trị (value / 값) missing/invalid.

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) giúp UX, không phải ranh giới bảo mật (security boundary / 보안 경계). máy chủ (server / 서버) bắt buộc validate lại.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **93. disabled** tiếp nhận điểm tựa từ **92. required** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **94. readonly** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 93. `disabled`
Phần này nối mạch bài học với “93. `disabled`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input disabled>
```

Disabled điều khiển (control / 제어) thường:

```text
không focus
không edit
không submit
```

Đây là boolean attribute.

Sai:

```html
<input disabled="false">
```

Nó vẫn disabled vì boolean attribute true khi attribute tồn tại.

Muốn false, remove attribute hoặc set DOM thuộc tính (property / 속성) false.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **94. readonly** tiếp nhận điểm tựa từ **93. disabled** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **95. checked và selected** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 94. `readonly`
Phần này nối mạch bài học với “94. `readonly`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  name="accountId"
  value="A123"
  readonly>
```

Readonly điều khiển (control / 제어) không cho người dùng (user / 사용자) sửa nhưng thường vẫn focusable/submittable tùy điều khiển (control / 제어) kiểu (type / 타입).

Khác disabled, disabled điều khiển (control / 제어) thường bị loại khỏi form submission.

Đây là khác biệt backend quan trọng.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **95. checked và selected** tiếp nhận điểm tựa từ **94. readonly** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **96. min, max, step** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 95. `checked` và `selected`

Initial checkbox/radio trạng thái (state / 상태):

```html
<input
  type="checkbox"
  checked>
```

Option initial trạng thái (state / 상태):

```html
<option selected>Korea</option>
```

Sau người dùng (user / 사용자) tương tác (interaction / 상호작용), DOM properties:

```js
input.checked
option.selected
```

phản ánh trạng thái hiện tại (current state / 현재 상태), còn markup attributes liên quan default/initial trạng thái (state / 상태).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **96. min, max, step** tiếp nhận điểm tựa từ **95. checked và selected** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **97. minlength, maxlength** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 96. `min`, `max`, `step`
Phần này nối mạch bài học với “96. `min`, `max`, `step`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="number"
  min="1"
  max="100"
  step="0.01">
```

Các ràng buộc (constraints / 제약조건들) này áp dụng phù hợp theo đầu vào (input / 입력) kiểu (type / 타입).

`step` mô tả allowed stepping/granularity.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **97. minlength, maxlength** tiếp nhận điểm tựa từ **96. min, max, step** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **98. pattern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 97. `minlength`, `maxlength`
Phần này nối mạch bài học với “97. `minlength`, `maxlength`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  minlength="8"
  maxlength="30">
```

Máy khách (client / 클라이언트) ràng buộc (constraint / 제약조건)/hint.

Không thay máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **98. pattern** tiếp nhận điểm tựa từ **97. minlength, maxlength** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **99. multiple** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 98. `pattern`
Phần này nối mạch bài học với “98. `pattern`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  pattern="[A-Z]{3}">
```

Mẫu (pattern / 패턴) ràng buộc (constraint / 제약조건) có thể hỗ trợ simple format kiểm tra hợp lệ (validation / 검증).

Không biến HTML regex thành bảo mật (security / 보안) filter. máy chủ (server / 서버) phải validate lĩnh vực (domain / 도메인) giá trị (value / 값) bằng quy tắc (rule / 규칙) của mình.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **99. multiple** tiếp nhận điểm tựa từ **98. pattern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **100. autocomplete** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 99. `multiple`

Có thể dùng với tệp (file / 파일), email hoặc select:

```html
<input
  type="file"
  multiple>
```

```html
<select
  name="skills"
  multiple>
```

Form dữ liệu (data / 데이터) có thể có nhiều entries cùng name.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **100. autocomplete** tiếp nhận điểm tựa từ **99. multiple** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **101. inputmode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 100. `autocomplete`

Ví dụ:

```html
<input
  name="email"
  autocomplete="email">
```

Các tokens quan trọng:

```text
name
given-name
family-name
username
new-password
current-password
one-time-code
email
tel
street-address
postal-code
organization
cc-name
cc-number
cc-exp
cc-csc
```

Autocomplete đúng giúp password manager, mobile keyboard và checkout UX.

Không tắt autofill bừa chỉ vì “UI nhìn sạch hơn”.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **101. inputmode** tiếp nhận điểm tựa từ **100. autocomplete** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **102. enterkeyhint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 101. `inputmode`
Phần này nối mạch bài học với “101. `inputmode`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="text"
  inputmode="numeric">
```

`inputmode` chủ yếu gợi ý keyboard/đầu vào (input / 입력) UI.

`type` ảnh hưởng ngữ nghĩa (semantics / 의미론)/kiểm tra hợp lệ (validation / 검증).

Ví dụ postal mã (code / 코드) numeric-looking nhưng không phải number quantity; có thể dùng:

```html
<input
  type="text"
  inputmode="numeric">
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **102. enterkeyhint** tiếp nhận điểm tựa từ **101. inputmode** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **103. <datalist>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 102. `enterkeyhint`
Phần này nối mạch bài học với “102. `enterkeyhint`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  enterkeyhint="search">
```

Gợi ý label/hành động (action / 동작) của Enter key trên mobile keyboard.

Dùng chung (common / 공통) values gồm:

```text
enter
done
go
next
previous
search
send
```

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **103. <datalist>** tiếp nhận điểm tựa từ **102. enterkeyhint** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **104. <textarea>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 103. `<datalist>`
Phần này nối mạch bài học với “103. `<datalist>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<label for="city">City</label>

<input
  id="city"
  name="city"
  list="cities">

<datalist id="cities">
  <option value="Seoul">
  <option value="Busan">
</datalist>
```

Datalist cung cấp suggestions, không phải strict selection như `select`.

Người dùng (user / 사용자) vẫn có thể nhập giá trị (value / 값) khác nếu các ràng buộc (constraints / 제약조건들) không cấm.

---

# PHẦN 14 — TEXTAREA, SELECT, FIELDSET VÀ BUTTON

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **104. <textarea>** tiếp nhận điểm tựa từ **103. <datalist>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **105. <select> và <option>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 104. `<textarea>`
Phần này nối mạch bài học với “104. `<textarea>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<textarea
  name="description"
  rows="5"></textarea>
```

Initial giá trị (value / 값) nằm giữa start/end tags:

```html
<textarea>Hello</textarea>
```

không phải `value` attribute như đầu vào (input / 입력).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **105. <select> và <option>** tiếp nhận điểm tựa từ **104. <textarea>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **106. <optgroup>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 105. `<select>` và `<option>`
Phần này nối mạch bài học với “105. `<select>` và `<option>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<select name="country">
  <option value="KR">Korea</option>
  <option value="VN">Vietnam</option>
</select>
```

Visible label có thể khác submitted `value`.

Bản địa (native / 네이티브) select cung cấp keyboard/mobile/khả năng tiếp cận (accessibility / 접근성) behaviors mà custom `div` dropdown phải tự implement rất nhiều.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **106. <optgroup>** tiếp nhận điểm tựa từ **105. <select> và <option>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **107. <fieldset> và <legend>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 106. `<optgroup>`
Phần này nối mạch bài học với “106. `<optgroup>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<select name="country">
  <optgroup label="Asia">
    <option value="KR">Korea</option>
    <option value="VN">Vietnam</option>
  </optgroup>
</select>
```

Dùng để group options theo category.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **107. <fieldset> và <legend>** tiếp nhận điểm tựa từ **106. <optgroup>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **108. <button>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 107. `<fieldset>` và `<legend>`
Phần này nối mạch bài học với “107. `<fieldset>` và `<legend>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<fieldset>
  <legend>Payment method</legend>

  <label>
    <input
      type="radio"
      name="payment"
      value="card">
    Card
  </label>
</fieldset>
```

`fieldset` group related controls.

`legend` cung cấp accessible group label.

Đặc biệt hữu ích với radio groups và related checkbox sections.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **108. <button>** tiếp nhận điểm tựa từ **107. <fieldset> và <legend>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **109. Multi-action form** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 108. `<button>`
Phần này nối mạch bài học với “108. `<button>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<button type="button">
  Open
</button>
```

Các types:

```text
button
submit
reset
```

Trong form, nếu button không phải submit, hãy khai báo:

```html
type="button"
```

rõ ràng để tránh accidental submission.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **109. Multi-action form** tiếp nhận điểm tựa từ **108. <button>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **110. <output>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 109. Multi-action form

HTML bản địa (native / 네이티브) có thể làm:

```html
<form
  action="/article"
  method="post">

  <button
    type="submit"
    name="action"
    value="save">
    Save
  </button>

  <button
    type="submit"
    name="action"
    value="publish">
    Publish
  </button>

</form>
```

Backend nhận giá trị (value / 값) của submitter được click.

Button còn có thể override `formaction`, `formmethod`, `formenctype`, `formtarget` và `formnovalidate`.

Phần Master sẽ giải thích sâu submitter/form đơn vị sở hữu (owner / 오너) ngữ nghĩa (semantics / 의미론).

---

# PHẦN 15 — bản địa (native / 네이티브) đầu ra (output / 출력) VÀ INTERACTIVE ELEMENTS

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **110. <output>** tiếp nhận điểm tựa từ **109. Multi-action form** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **111. <progress>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 110. `<output>`
Phần này nối mạch bài học với “110. `<output>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<output for="price quantity">
  100
</output>
```

Biểu diễn kết quả (result / 결과) của calculation/người dùng (user / 사용자) hành động (action / 동작).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **111. <progress>** tiếp nhận điểm tựa từ **110. <output>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **112. <meter>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 111. `<progress>`
Phần này nối mạch bài học với “111. `<progress>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<progress
  value="70"
  max="100">
  70%
</progress>
```

Dùng cho tác vụ (task / 작업) progress.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **112. <meter>** tiếp nhận điểm tựa từ **111. <progress>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **113. <details> và <summary>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 112. `<meter>`
Phần này nối mạch bài học với “112. `<meter>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<meter
  min="0"
  max="100"
  value="80">
  80
</meter>
```

Dùng cho đo lường (measurement / 측정) trong known phạm vi (range / 범위).

`progress` là tiến độ tác vụ (task / 작업); `meter` là một đo lường (measurement / 측정)/giá trị (value / 값).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **113. <details> và <summary>** gom các mảnh từ **112. <meter>** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **114. <dialog>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 113. `<details>` và `<summary>`
Phần này nối mạch bài học với “113. `<details>` và `<summary>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<details>
  <summary>Advanced settings</summary>

  <p>...</p>
</details>
```

Đây là bản địa (native / 네이티브) disclosure widget.

Trước khi tự viết accordion bằng `div + onclick + aria-expanded`, hãy xem `details/summary` có đáp ứng yêu cầu (requirement / 요구사항) không.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **114. <dialog>** gom các mảnh từ **113. <details> và <summary>** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **115. <form method="dialog">** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 114. `<dialog>`
Phần này nối mạch bài học với “114. `<dialog>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<dialog id="confirm">
  <h2>Delete item?</h2>

  <button type="button">
    Cancel
  </button>

  <button type="button">
    Delete
  </button>
</dialog>
```

JavaScript có:

```js
dialog.show()
```

cho non-modal và:

```js
dialog.showModal()
```

cho modal.

Bản địa (native / 네이티브) dialog có top-layer/modal/focus ngữ nghĩa (semantics / 의미론) tốt hơn một `div.modal` tự chế, dù môi trường vận hành (production / 운영 환경) vẫn phải kiểm thử (test / 테스트) focus luồng (flow / 흐름) và khả năng tiếp cận (accessibility / 접근성).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **115. <form method="dialog">** tiếp nhận điểm tựa từ **114. <dialog>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **116. Popover** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 115. `<form method="dialog">`

Trong dialog:

```html
<dialog id="confirm">
  <form method="dialog">
    <button value="cancel">
      Cancel
    </button>

    <button value="ok">
      OK
    </button>
  </form>
</dialog>
```

Submit form có thể đóng dialog thay vì gửi HTTP yêu cầu (request / 요청).

Đây là ví dụ tốt về HTML bản địa (native / 네이티브) hành vi (behavior / 동작) thay thế JavaScript boilerplate.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **116. Popover** tiếp nhận điểm tựa từ **115. <form method="dialog">** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **117. id** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 116. Popover

Một element có thể trở thành popover:

```html
<div
  id="menu"
  popover>
  ...
</div>
```

Invoker:

```html
<button
  type="button"
  popovertarget="menu">
  Open menu
</button>
```

Trình duyệt (browser / 브라우저) quản lý show/hide, top tầng (layer / 계층) và light-dismiss hành vi (behavior / 동작) theo popover chế độ (mode / 모드).

Tính năng (feature / 기능) này sẽ được giải thích sâu ở Master hiện thực (implementation / 구현).

---

# PHẦN 16 — toàn cục (global / 전역) ATTRIBUTES

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **117. id** tiếp nhận điểm tựa từ **116. Popover** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **118. class** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 117. `id`
Phần này nối mạch bài học với “117. `id`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<section id="pricing">
```

`id` phải unique trong document.

Nó được dùng cho fragment điều hướng (navigation / 내비게이션), label association, ARIA relationships, CSS và JS.

Duplicate IDs có thể gây khả năng tiếp cận (accessibility / 접근성)/truy vấn (query / 쿼리) bugs khó gỡ lỗi (debug / 디버그).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **118. class** tiếp nhận điểm tựa từ **117. id** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **119. style** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 118. `class`
Phần này nối mạch bài học với “118. `class`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div class="card active">
```

Lớp (class / 클래스) là space-separated tokens thường dùng cho CSS và thành phần (component / 컴포넌트) trạng thái (state / 상태) styling.

JavaScript thường thao tác qua:

```js
element.classList
```

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **119. style** tiếp nhận điểm tựa từ **118. class** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **120. title** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 119. `style`
Phần này nối mạch bài học với “119. `style`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div style="display:none">
```

Inline style hợp lệ, nhưng large ứng dụng (application / 애플리케이션) thường tránh sử dụng rộng vì maintainability, reuse và CSP kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **120. title** tiếp nhận điểm tựa từ **119. style** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **121. hidden** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 120. `title`
Phần này nối mạch bài học với “120. `title`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<abbr title="HyperText Markup Language">
  HTML
</abbr>
```

`title` là advisory thông tin (information / 정보).

Không dùng nó làm accessible name duy nhất cho trọng yếu (critical / 중요) điều khiển (control / 제어).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **121. hidden** tiếp nhận điểm tựa từ **120. title** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **122. inert** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 121. `hidden`
Phần này nối mạch bài học với “121. `hidden`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<section hidden>
```

Đánh dấu content hiện tại không relevant/không được present.

JavaScript:

```js
element.hidden = true;
```

Phần Master sẽ phân biệt `hidden`, `hidden="until-found"`, CSS hiding và khả năng tiếp cận (accessibility / 접근성) implications.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **122. inert** tiếp nhận điểm tựa từ **121. hidden** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **123. tabindex** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 122. `inert`
Phần này nối mạch bài học với “122. `inert`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<main inert>
  ...
</main>
```

`inert` làm subtree non-interactive trong nhiều người dùng (user / 사용자) tương tác (interaction / 상호작용) paths, bao gồm focus.

Useful với custom overlay workflows, nhưng bản địa (native / 네이티브) modal dialog đã có browser-managed inertness hành vi (behavior / 동작) cho surrounding content.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **123. tabindex** tiếp nhận điểm tựa từ **122. inert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **124. data-** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 123. `tabindex`
Phần này nối mạch bài học với “123. `tabindex`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
tabindex="0"
```

đưa element vào tab thứ tự (order / 순서) theo document position.

```html
tabindex="-1"
```

cho phép programmatic focus nhưng không natural tab.

Positive tabindex như:

```html
tabindex="5"
```

thường là anti-pattern vì phá natural focus thứ tự (order / 순서) và rất khó maintain.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **124. data-** tiếp nhận điểm tựa từ **123. tabindex** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **125. contenteditable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 124. `data-*`
Phần này nối mạch bài học với “124. `data-*`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<button
  data-user-id="42">
```

JavaScript:

```js
button.dataset.userId
```

Phù hợp với lightweight ứng dụng (application / 애플리케이션) siêu dữ liệu (metadata / 메타데이터).

Không chứa secret/đơn vị từ (token / 토큰) vì DOM thuộc máy khách (client / 클라이언트).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **125. contenteditable** tiếp nhận điểm tựa từ **124. data-** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **126. draggable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 125. `contenteditable`
Phần này nối mạch bài học với “125. `contenteditable`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div contenteditable="true">
  Editable text
</div>
```

Nó biến content thành editable region, nhưng không tự trở thành rich-text editor môi trường vận hành (production / 운영 환경).

Selection, paste sanitization, undo, trình duyệt (browser / 브라우저) differences và khả năng tiếp cận (accessibility / 접근성) làm editor hiện thực (implementation / 구현) phức tạp hơn nhiều.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **126. draggable** tiếp nhận điểm tựa từ **125. contenteditable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **127. spellcheck, translate, autofocus** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 126. `draggable`
Phần này nối mạch bài học với “126. `draggable`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div draggable="true">
```

Cho bản địa (native / 네이티브) drag hành vi (behavior / 동작).

Nếu drag hành động (action / 동작) là trọng yếu (critical / 중요), hãy cung cấp alternative không phụ thuộc pointer drag cho khả năng tiếp cận (accessibility / 접근성).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **127. spellcheck, translate, autofocus** tiếp nhận điểm tựa từ **126. draggable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **128. <script>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 127. `spellcheck`, `translate`, `autofocus`

Spell checking hint:

```html
<textarea spellcheck="true">
```

Không dịch:

```html
<code translate="no">
  npm install
</code>
```

Autofocus:

```html
<input autofocus>
```

Autofocus phải dùng cẩn thận vì có thể bật mobile keyboard hoặc làm screen reader ngữ cảnh (context / 맥락) nhảy bất ngờ.

---

# PHẦN 17 — SCRIPT LOADING

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **128. <script>** tiếp nhận điểm tựa từ **127. spellcheck, translate, autofocus** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **129. defer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 128. `<script>`

Classic bên ngoài (external / 외부) script:

```html
<script src="/app.js"></script>
```

Script loading chiến lược (strategy / 전략) ảnh hưởng parser và hiệu năng (performance / 성능).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **129. defer** tiếp nhận điểm tựa từ **128. <script>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **130. async** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 129. `defer`
Phần này nối mạch bài học với “129. `defer`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<script
  defer
  src="/app.js">
</script>
```

Classic deferred script được download song song và execute sau document parsing, đồng thời giữ relative thực thi (execution / 실행) thứ tự (order / 순서) giữa deferred scripts.

Đây là good default cho nhiều classic ứng dụng (application / 애플리케이션) scripts.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **130. async** tiếp nhận điểm tựa từ **129. defer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **131. type="module"** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 130. `async`
Phần này nối mạch bài học với “130. `async`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<script
  async
  src="/analytics.js">
</script>
```

Async script download song song và execute khi ready; thực thi (execution / 실행) thứ tự (order / 순서) với scripts khác không đảm bảo.

Phù hợp với independent scripts như analytics.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **131. type="module"** tiếp nhận điểm tựa từ **130. async** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **132. nomodule** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 131. `type="module"`
Phần này nối mạch bài học với “131. `type="module"`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<script
  type="module"
  src="/main.js">
</script>
```

ES mô-đun (module / 모듈) hỗ trợ `import`/`export` và mô-đun (module / 모듈) đồ thị (graph / 그래프).

Mô-đun (module / 모듈) scripts có loading/thực thi (execution / 실행) hành vi (behavior / 동작) riêng, gần deferred by default trong nhiều respects.

Hiện đại (modern / 현대적) frontend cần hiểu mô-đun (module / 모듈) loading thay vì chỉ học `async/defer`.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **132. nomodule** tiếp nhận điểm tựa từ **131. type="module"** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **133. integrity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 132. `nomodule`
Phần này nối mạch bài học với “132. `nomodule`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<script
  nomodule
  src="/legacy.js">
</script>
```

Legacy fallback mẫu (pattern / 패턴) cho browsers không hỗ trợ (support / 지원) modules.

Ngày nay nhiều projects không cần nữa, nhưng cấp cao (senior / 시니어) nên nhận diện khi maintain old bundles.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **133. integrity** tiếp nhận điểm tựa từ **132. nomodule** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **134. nonce** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 133. `integrity`
Phần này nối mạch bài học với “133. `integrity`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-..."
  crossorigin="anonymous">
</script>
```

Subresource Integrity cho trình duyệt (browser / 브라우저) verify fetched tài nguyên (resource / 자원) khớp expected băm (hash / 해시).

Hữu ích với pinned third-party CDN resources.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **134. nonce** tiếp nhận điểm tựa từ **133. integrity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **135. <noscript>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 134. `nonce`
Phần này nối mạch bài học với “134. `nonce`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<script nonce="RANDOM_PER_RESPONSE">
```

Nonce có thể được Content bảo mật (security / 보안) chính sách (policy / 정책) dùng để allow specific inline script.

Nonce phải unpredictable và phù hợp chính sách (policy / 정책). Hardcode same nonce mãi làm mất bảo mật (security / 보안) intent.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **135. <noscript>** tiếp nhận điểm tựa từ **134. nonce** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **136. SEO bắt đầu từ nội dung và ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 135. `<noscript>`
Phần này nối mạch bài học với “135. `<noscript>`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<noscript>
  JavaScript is required for this application.
</noscript>
```

Nếu cơ sở (base / 기반) tính năng (feature / 기능) có thể hoạt động bản địa (native / 네이티브)/server-side, progressive enhancement thường tốt hơn chỉ hiển thị warning.

---

# PHẦN 18 — SEO, xã hội (social / 사회적) siêu dữ liệu (metadata / 메타데이터) VÀ STRUCTURED dữ liệu (data / 데이터)

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **136. SEO bắt đầu từ nội dung và ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **135. <noscript>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **137. Canonical** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 136. SEO bắt đầu từ nội dung và ngữ nghĩa (semantics / 의미론)

HTML SEO không chỉ là meta tags.

Các foundations gồm:

```text
title
description
semantic headings
meaningful links
crawlable content
lang
alt
canonical URL
structured data khi phù hợp
```

Tìm kiếm (search / 검색) engine phải hiểu content thật.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, sau nội dung của **136. SEO bắt đầu từ nội dung và ngữ nghĩa (semantics / 의미론)**, **137. Canonical** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **138. Robots metadata** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 137. Canonical
Phần này nối mạch bài học với “137. Canonical”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<link
  rel="canonical"
  href="https://example.com/product/123">
```

Dùng để chỉ preferred URL khi nhiều URLs đại diện cùng/similar content.

Nó không phải redirect và không phải bảo mật (security / 보안) quy tắc (rule / 규칙).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **138. Robots metadata** tiếp nhận điểm tựa từ **137. Canonical** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **139. Open Graph** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 138. Robots metadata
Phần này nối mạch bài học với “138. Robots metadata”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<meta
  name="robots"
  content="noindex,nofollow">
```

`noindex` là tìm kiếm (search / 검색) indexing instruction/hint trong applicable crawler ngữ cảnh (context / 맥락).

Nó không bảo vệ private admin page. Private page phải có authentication/authorization.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **139. Open Graph** tiếp nhận điểm tựa từ **138. Robots metadata** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **140. JSON-LD structured data** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 139. Open Graph
Phần này nối mạch bài học với “139. Open Graph”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<meta
  property="og:title"
  content="HTML Guide">

<meta
  property="og:description"
  content="Learn semantic HTML">

<meta
  property="og:image"
  content="https://example.com/preview.png">
```

Dùng để tạo xã hội (social / 사회적) sharing previews trong supporting platforms.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **140. JSON-LD structured data** tiếp nhận điểm tựa từ **139. Open Graph** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **141. bản địa (native / 네이티브) HTML trước ARIA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 140. JSON-LD structured data
Phần này nối mạch bài học với “140. JSON-LD structured data”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Acme"
}
</script>
```

Structured dữ liệu (data / 데이터) giúp machine/tìm kiếm (search / 검색) engines hiểu thực thể (entity / 엔터티)/content theo vocabulary.

Nó phải phản ánh content thật, không phải nơi khai báo thông tin giả để “hack SEO”.

---

# PHẦN 19 — khả năng tiếp cận (accessibility / 접근성)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **141. bản địa (native / 네이티브) HTML trước ARIA** tiếp nhận điểm tựa từ **140. JSON-LD structured data** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **142. Accessible name** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 141. bản địa (native / 네이티브) HTML trước ARIA

Sai nếu không có lý do:

```html
<div
  role="button"
  tabindex="0">
  Save
</div>
```

Đúng hơn:

```html
<button type="button">
  Save
</button>
```

Bản địa (native / 네이티브) button đã có keyboard/focus/role/form ngữ nghĩa (semantics / 의미론).

ARIA không tạo bản địa (native / 네이티브) hành vi (behavior / 동작). Nếu dùng `role="button"` trên div, bạn còn phải implement keyboard activation và focus hành vi (behavior / 동작).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **142. Accessible name** tiếp nhận điểm tựa từ **141. bản địa (native / 네이티브) HTML trước ARIA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **143. aria-labelledby** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 142. Accessible name

Một điều khiển (control / 제어) cần tên mà cây khả năng tiếp cận (accessibility tree / 접근성 트리) hiểu.

Văn bản (text / 텍스트) button:

```html
<button>Save</button>
```

đã có accessible name.

Icon-only:

```html
<button
  type="button"
  aria-label="Close">
  ×
</button>
```

Nếu visible văn bản (text / 텍스트) tồn tại, ưu tiên để accessible name phù hợp visible văn bản (text / 텍스트).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **142. Accessible name** cho ta quy tắc; **143. aria-labelledby** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **144. aria-describedby** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 143. `aria-labelledby`
Phần này nối mạch bài học với “143. `aria-labelledby`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<h2 id="dialog-title">
  Delete account
</h2>

<div
  role="dialog"
  aria-labelledby="dialog-title">
  ...
</div>
```

Accessible name lấy từ element khác.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **143. aria-labelledby** cho ta quy tắc; **144. aria-describedby** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **145. động (dynamic / 동적) ARIA trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 144. `aria-describedby`
Phần này nối mạch bài học với “144. `aria-describedby`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<label for="password">
  Password
</label>

<input
  id="password"
  aria-describedby="password-help">

<p id="password-help">
  At least 12 characters.
</p>
```

Label/name trả lời “điều khiển (control / 제어) này là gì?”. Description bổ sung “cần biết gì thêm?”.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **145. động (dynamic / 동적) ARIA trạng thái (state / 상태)** tiếp nhận điểm tựa từ **144. aria-describedby** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **146. aria-current** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 145. động (dynamic / 동적) ARIA trạng thái (state / 상태)

Expandable button:

```html
<button
  aria-expanded="false"
  aria-controls="menu">
  Menu
</button>
```

Khi menu mở, `aria-expanded` phải cập nhật (update / 업데이트) thành `true`.

ARIA trạng thái (state / 상태) không tự sync với visual trạng thái (state / 상태) nếu JavaScript không cập nhật.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **146. aria-current** tiếp nhận điểm tựa từ **145. động (dynamic / 동적) ARIA trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **147. Live regions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 146. `aria-current`
Phần này nối mạch bài học với “146. `aria-current`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<a
  href="/orders"
  aria-current="page">
  Orders
</a>
```

Cho assistive technology biết item hiện tại.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **147. Live regions** tiếp nhận điểm tựa từ **146. aria-current** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **148. Keyboard kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 147. Live regions
Phần này nối mạch bài học với “147. Live regions”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<div
  aria-live="polite">
  Saved successfully
</div>
```

Dùng cho động (dynamic / 동적) updates cần announce.

Không dùng `assertive` cho mọi notification vì có thể interrupt người dùng (user / 사용자) liên tục.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **148. Keyboard kiểm thử (test / 테스트)** tiếp nhận điểm tựa từ **147. Live regions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **149. Hai tầng (layer / 계층) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 148. Keyboard kiểm thử (test / 테스트)

Một cấp cao (senior / 시니어) rà soát (review / 검토) phải thử page chỉ bằng keyboard:

```text
Tab
Shift+Tab
Enter
Space
Escape
arrow keys ở controls phù hợp
```

Kiểm tra focus thứ tự (order / 순서), visible focus và khả năng activate controls.

HTML ngữ nghĩa (semantics / 의미론) tốt thường giảm rất nhiều custom keyboard mã (code / 코드).

---

# PHẦN 20 — ATTRIBUTE VS DOM thuộc tính (property / 속성)

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **149. Hai tầng (layer / 계층) khác nhau** tiếp nhận điểm tựa từ **148. Keyboard kiểm thử (test / 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **150. value** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 149. Hai tầng (layer / 계층) khác nhau

Markup:

```html
<input
  value="A"
  checked>
```

Trình duyệt (browser / 브라우저) parse thành DOM đối tượng (object / 객체) có properties:

```js
input.value
input.checked
```

Content attribute và DOM thuộc tính (property / 속성) có thể reflect lẫn nhau nhưng không phải lúc nào cũng cùng trạng thái hiện tại (current state / 현재 상태).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **150. value** tiếp nhận điểm tựa từ **149. Hai tầng (layer / 계층) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **151. checked** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 150. `value`

Markup:

```html
<input value="A">
```

Người dùng (user / 사용자) sửa thành `B`.

```js
input.value
```

→ `"B"`

Nhưng:

```js
input.getAttribute("value")
```

có thể vẫn → `"A"`.

Attribute thể hiện markup/default giá trị (value / 값) relationship; thuộc tính (property / 속성) thể hiện hiện tại (current / 현재) live trạng thái (state / 상태).

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **151. checked** tiếp nhận điểm tựa từ **150. value** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **152. href** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 151. `checked`
Phần này nối mạch bài học với “151. `checked`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<input
  type="checkbox"
  checked>
```

Người dùng (user / 사용자) uncheck.

```js
input.checked
```

→ false.

`checked` content attribute vẫn có thể tồn tại và liên quan default checked trạng thái (state / 상태).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **152. href** tiếp nhận điểm tựa từ **151. checked** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **153. Boolean attributes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 152. `href`
Phần này nối mạch bài học với “152. `href`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<a href="/users">
```

```js
a.getAttribute("href")
```

có thể trả `/users`.

```js
a.href
```

thường trả fully resolved absolute URL.

Đây là ví dụ reflection/resolution hành vi (behavior / 동작) rất phổ biến.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **153. Boolean attributes** tiếp nhận điểm tựa từ **152. href** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **154. Không phải element nào cũng chứa gì cũng được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 153. Boolean attributes

Boolean attribute true theo presence:

```html
<input disabled>
```

```html
<input disabled="">
```

```html
<input disabled="false">
```

cả ba đều disabled.

False nghĩa remove attribute hoặc set thuộc tính (property / 속성) false:

```js
input.disabled = false;
```

Dùng chung (common / 공통) boolean attrs gồm `disabled`, `checked`, `selected`, `required`, `readonly`, `multiple`, `autofocus`, `hidden`, `open`, `controls`, `loop`, `muted`.

---

# PHẦN 21 — CONTENT mô hình (model / 모델) VÀ VALID HTML

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **154. Không phải element nào cũng chứa gì cũng được** tiếp nhận điểm tựa từ **153. Boolean attributes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **155. Void elements** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 154. Không phải element nào cũng chứa gì cũng được

HTML có content các mô hình (models / 모델들).

Ví dụ `ul` có danh sách (list / 목록) items phù hợp.

Interactive element không nên nest interactive element một cách invalid/problematic.

Sai:

```html
<button>
  <a href="/profile">
    Profile
  </a>
</button>
```

Nếu điều hướng (navigation / 내비게이션), dùng link. Nếu hành động (action / 동작), dùng button.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **155. Void elements** tiếp nhận điểm tựa từ **154. Không phải element nào cũng chứa gì cũng được** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **156. HTML parser không giống XML parser** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 155. Void elements

Các HTML void elements quan trọng:

```text
area
base
br
col
embed
hr
img
input
link
meta
source
track
wbr
```

Chúng không có end tag/children trong HTML cú pháp (syntax / 문법).

```html
<img
  src="/a.png"
  alt="">
```

Không viết:

```html
<img>text</img>
```

HTML void elements khác XML self-closing mô hình (model / 모델).

---

# PHẦN 22 — trình duyệt (browser / 브라우저) PARSER CƠ BẢN

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **156. HTML parser không giống XML parser** tiếp nhận điểm tựa từ **155. Void elements** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **157. trình duyệt (browser / 브라우저) có thể thêm nodes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 156. HTML parser không giống XML parser

HTML parser được thiết kế với lỗi (error / 오류) khôi phục (recovery / 복구) mạnh.

Invalid markup có thể vẫn tạo DOM và kết xuất (render / 렌더링).

Điều đó không nghĩa markup đúng.

Trình duyệt (browser / 브라우저) có standardized algorithms để sửa/normalize nhiều cases.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **157. trình duyệt (browser / 브라우저) có thể thêm nodes** tiếp nhận điểm tựa từ **156. HTML parser không giống XML parser** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **158. View nguồn (source / 소스) vs Elements** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 157. trình duyệt (browser / 브라우저) có thể thêm nodes

Nguồn (source / 소스):

```html
<table>
  <tr>
    <td>A</td>
  </tr>
</table>
```

DOM inspector có thể thấy `tbody` được parser tạo.

Đây là ví dụ nguồn (source / 소스) văn bản (text / 텍스트) không phải luôn giống resulting DOM cây (tree / 트리).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **157. trình duyệt (browser / 브라우저) có thể thêm nodes** nêu điều cần giải thích; **158. View nguồn (source / 소스) vs Elements** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **159. máy khách (client / 클라이언트) HTML không đáng tin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 158. View nguồn (source / 소스) vs Elements

**View nguồn (source / 소스)** gần với original phản hồi (response / 응답)/nguồn (source / 소스) markup.

**Elements panel** cho hiện tại (current / 현재) parsed DOM sau trình duyệt (browser / 브라우저) normalization và JavaScript mutations.

Nếu React/Vue hydrate DOM, bạn còn có khung phần mềm (framework / 프레임워크) nội bộ (internal / 내부) cây (tree / 트리)/trạng thái (state / 상태).

Khi gỡ lỗi (debug / 디버그) hydration mismatch, phải phân biệt ba tầng (layer / 계층) này.

---

# PHẦN 23 — bảo mật (security / 보안) VÀ hiệu năng (performance / 성능) FOUNDATION

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **158. View nguồn (source / 소스) vs Elements** nêu điều cần giải thích; **159. máy khách (client / 클라이언트) HTML không đáng tin** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **160. Untrusted HTML** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 159. máy khách (client / 클라이언트) HTML không đáng tin

Hidden trường dữ liệu (field / 필드), `data-*`, disabled điều khiển (control / 제어) và máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) đều có thể bị người dùng (user / 사용자) sửa/bypass.

Máy chủ (server / 서버) phải validate và authorize independent of HTML.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **160. Untrusted HTML** tiếp nhận điểm tựa từ **159. máy khách (client / 클라이언트) HTML không đáng tin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **161. Iframe bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 160. Untrusted HTML

Concept nguy hiểm:

```js
element.innerHTML = userInput;
```

Nếu `userInput` không được sanitize/encode đúng ngữ cảnh (context / 맥락), XSS có thể xảy ra.

Bảo mật (security / 보안) phải dựa trên contextual encoding/sanitization/CSP chiến lược (strategy / 전략), không phải regex remove `<script>`.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **161. Iframe bảo mật (security / 보안)** tiếp nhận điểm tựa từ **160. Untrusted HTML** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **162. tài nguyên (resource / 자원) loading ảnh hưởng hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 161. Iframe bảo mật (security / 보안)

Use sandbox/allow/referrer policies có chủ đích.

Third-party iframe là ranh giới bảo mật (security boundary / 보안 경계), không phải chỉ bố cục (layout / 레이아웃) box.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **161. Iframe bảo mật (security / 보안)** nêu điều cần giải thích; **162. tài nguyên (resource / 자원) loading ảnh hưởng hiệu năng (performance / 성능)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **163. fetchpriority** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 162. tài nguyên (resource / 자원) loading ảnh hưởng hiệu năng (performance / 성능)

HTML quyết định trình duyệt (browser / 브라우저) discover CSS, JS, images, fonts, iframes sớm hay muộn.

Do đó hiệu năng (performance / 성능) không chỉ là JavaScript tối ưu hóa (optimization / 최적화).

Good markup có thể:

```text
discover LCP image sớm
reserve image dimensions
defer non-critical scripts
lazy-load below-fold images/iframes
preconnect đúng origin
```

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **162. tài nguyên (resource / 자원) loading ảnh hưởng hiệu năng (performance / 성능)** nêu điều cần giải thích; **163. fetchpriority** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **164. Preconnect và preload** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 163. `fetchpriority`
Phần này nối mạch bài học với “163. `fetchpriority`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<img
  src="/hero.jpg"
  fetchpriority="high"
  width="1200"
  height="800"
  alt="...">
```

Đây là priority hint cho trình duyệt (browser / 브라우저).

Không đặt mọi thứ `high`; nếu mọi tài nguyên (resource / 자원) đều high thì tín hiệu (signal / 신호) mất giá trị và scheduling có thể xấu hơn.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **164. Preconnect và preload** tiếp nhận điểm tựa từ **163. fetchpriority** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **165. Native-first thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 164. Preconnect và preload

Preconnect:

```html
<link
  rel="preconnect"
  href="https://cdn.example.com">
```

Preload:

```html
<link
  rel="preload"
  href="/critical.woff2"
  as="font"
  crossorigin>
```

Preload sai `as`, wrong URL hoặc tài nguyên (resource / 자원) không thực sự trọng yếu (critical / 중요) có thể tạo duplicate/unnecessary fetch.

Hiệu năng (performance / 성능) hints phải được đo bằng DevTools/Lighthouse/RUM chứ không dùng theo cảm giác.

---

# PHẦN 24 — PROGRESSIVE ENHANCEMENT VÀ cấp cao (senior / 시니어) MINDSET

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Beginner → cấp cao (senior / 시니어)**, **165. Native-first thiết kế (design / 설계)** tiếp nhận điểm tựa từ **164. Preconnect và preload** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **166. Progressive enhancement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 165. Native-first thiết kế (design / 설계)

Trước khi tự viết JavaScript widget, kiểm tra HTML đã có bản địa (native / 네이티브) thành phần nguyên thủy (primitive / 기본 요소) chưa:

```text
button
details/summary
dialog
popover
select
input date
form validation
progress
meter
```

Bản địa (native / 네이티브) controls thường có keyboard, focus, khả năng tiếp cận (accessibility / 접근성) và trình duyệt (browser / 브라우저) tích hợp (integration / 통합) tốt hơn custom div.

---

> **Chuyển mạch:** Trong **HTML — Beginner → cấp cao (senior / 시니어)**, **166. Progressive enhancement** tiếp nhận điểm tựa từ **165. Native-first thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **167. cấp cao (senior / 시니어) HTML rà soát (review / 검토) questions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 166. Progressive enhancement

Tìm kiếm (search / 검색) form:

```html
<form
  action="/search"
  method="get">

  <label for="q">
    Search
  </label>

  <input
    id="q"
    name="q"
    type="search">

  <button type="submit">
    Search
  </button>

</form>
```

Nếu JavaScript không chạy, form vẫn submit được.

JavaScript có thể enhance suggestions, loading trạng thái (state / 상태) và máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증).

Đây là progressive enhancement: cơ sở (base / 기반) functionality tồn tại trước, JS cải thiện trải nghiệm.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Beginner → cấp cao (senior / 시니어)**, **167. cấp cao (senior / 시니어) HTML rà soát (review / 검토) questions** tiếp nhận điểm tựa từ **166. Progressive enhancement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 167. cấp cao (senior / 시니어) HTML rà soát (review / 검토) questions

Khi rà soát (review / 검토) markup, cấp cao (senior / 시니어) nên hỏi theo luồng (flow / 흐름).

Element này có ngữ nghĩa (semantic / 의미적) đúng không? Nếu dùng `div`, có bản địa (native / 네이티브) element phù hợp hơn không? Heading hierarchy có đúng không? Links và buttons có bị dùng lẫn không? Form controls có label không? Form submission thực tế sẽ gửi những fields nào? Interactive controls có keyboard accessible không? ảnh (image / 이미지) alt có đúng purpose không? tài nguyên (resource / 자원) loading có làm chậm LCP không? Iframe có sandbox quá rộng không? máy khách (client / 클라이언트) dữ liệu (data / 데이터) có bị coi là trusted không? HTML có valid/parser-stable không?

Nếu bạn có thể trả lời những câu này, bạn đang rà soát (review / 검토) HTML ở mức (level / 수준) kỹ thuật (engineering / 엔지니어링) chứ không chỉ cú pháp (syntax / 문법).

---

# PHẦN 25 — PRODUCTION PAGE HOÀN CHỈNH
Phần này nối mạch bài học với “PHẦN 25 — PRODUCTION PAGE HOÀN CHỈNH”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<!doctype html>

<html lang="vi">
<head>
  <meta charset="utf-8">

  <meta
    name="viewport"
    content="width=device-width, initial-scale=1">

  <title>
    HTML Learning Portal
  </title>

  <meta
    name="description"
    content="Learn semantic HTML from beginner to senior.">

  <link
    rel="canonical"
    href="https://example.com/html">

  <link
    rel="stylesheet"
    href="/app.css">
</head>

<body>

  <header>

    <nav aria-label="Main navigation">
      <a href="/">Home</a>
      <a href="/courses">Courses</a>
    </nav>

  </header>

  <main>

    <article>

      <header>
        <h1>HTML Beginner → Senior</h1>

        <p>
          Updated:
          <time datetime="2026-09-12">
            12 Sep 2026
          </time>
        </p>
      </header>

      <section>
        <h2>Overview</h2>

        <p>
          HTML defines document structure and semantics.
        </p>
      </section>

      <figure>

        <img
          src="/semantic-html.webp"
          width="1200"
          height="800"
          alt="Diagram showing header, navigation, main content and footer">

        <figcaption>
          Example semantic page structure
        </figcaption>

      </figure>

      <section>

        <h2>Create account</h2>

        <form
          action="/signup"
          method="post">

          <p>

            <label for="email">
              Email
            </label>

            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required>

          </p>

          <p>

            <label for="password">
              Password
            </label>

            <input
              id="password"
              name="password"
              type="password"
              autocomplete="new-password"
              minlength="12"
              aria-describedby="password-help"
              required>

            <span id="password-help">
              Use at least 12 characters.
            </span>

          </p>

          <button type="submit">
            Create account
          </button>

        </form>

      </section>

      <details>

        <summary>
          Advanced information
        </summary>

        <p>
          Native HTML can replace a surprising amount of custom JavaScript.
        </p>

      </details>

    </article>

  </main>

  <footer>
    <small>© 2026 Example</small>
  </footer>

  <script
    type="module"
    src="/app.js">
  </script>

</body>
</html>
```

Document này cố tình dùng bản địa (native / 네이티브) ngữ nghĩa (semantics / 의미론) trước custom hành vi (behavior / 동작). Heading hierarchy rõ, điều hướng (navigation / 내비게이션) dùng links, form controls có labels, ảnh (image / 이미지) có dimensions/alt, thời gian (time / 시간) machine-readable và JS dùng mô-đun (module / 모듈) loading.

---

# PHẦN 26 — ROADMAP HỌC

Ở giai đoạn Beginner, bạn cần nắm document cấu trúc (structure / 구조), văn bản (text / 텍스트), links, images, lists, tables và form basics. Bạn nên tự viết vài trang không khung phần mềm (framework / 프레임워크) để trình duyệt (browser / 브라우저) ngữ nghĩa (semantics / 의미론) trở thành phản xạ.

Ở Intermediate, tập trung ngữ nghĩa (semantic / 의미적) bố cục (layout / 레이아웃), responsive images, form kiểm tra hợp lệ (validation / 검증), `autocomplete`, bản địa (native / 네이티브) interactive elements và khả năng tiếp cận (accessibility / 접근성) fundamentals.

Ở Advanced, học attribute/thuộc tính (property / 속성), script loading, gợi ý tài nguyên (resource hints / 리소스 힌트), SEO, iframe bảo mật (security / 보안), responsive hiệu năng (performance / 성능) và progressive enhancement.

Ở cấp cao (senior / 시니어), mục tiêu là hiểu parser, form submission ngữ nghĩa (semantics / 의미론), focus/cây khả năng tiếp cận (accessibility tree / 접근성 트리), bảo mật (security / 보안) trust boundaries và browser-native nền tảng (platform / 플랫폼) hành vi (behavior / 동작). Những phần sâu hơn như foster parenting, DOM clobbering, Declarative Shadow DOM, advanced Popover/Dialog và customizable select được tách sang tệp (file / 파일) Master hiện thực (implementation / 구현) để tệp (file / 파일) này vẫn có luồng (flow / 흐름) học rõ ràng.

---

# KẾT LUẬN

Một nhà phát triển (developer / 개발자) “biết HTML” có thể nhớ hàng chục tags. Một nhà phát triển (developer / 개발자) cấp cao (senior / 시니어) phải hiểu trình duyệt (browser / 브라우저) sẽ làm gì với markup đó.

Khi thấy:

```html
<button>
```

Cấp cao (senior / 시니어) nghĩ tới hành động (action / 동작) ngữ nghĩa (semantics / 의미론), keyboard activation, focus hành vi (behavior / 동작), form submitter hành vi (behavior / 동작) và khả năng tiếp cận (accessibility / 접근성) role.

Khi thấy:

```html
<img>
```

Cấp cao (senior / 시니어) nghĩ tới alt purpose, intrinsic dimensions, responsive nguồn (source / 소스) selection, LCP và bố cục (layout / 레이아웃) shift.

Khi thấy:

```html
<form>
```

Cấp cao (senior / 시니어) nghĩ tới successful controls, submitter, GET/POST, encoding, bản địa (native / 네이티브) kiểm tra hợp lệ (validation / 검증), autocomplete và server-side trust ranh giới (boundary / 경계).

Khi thấy:

```html
<script>
```

Cấp cao (senior / 시니어) nghĩ tới parser blocking, mô-đun (module / 모듈) loading, CSP, integrity và trọng yếu (critical / 중요) rendering đường dẫn (path / 경로).

Đó là cách chuyển từ “học tag HTML” sang **kỹ thuật (engineering / 엔지니어링) HTML**.

> **Bàn giao:** Sau **167. cấp cao (senior / 시니어) HTML rà soát (review / 검토) questions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
