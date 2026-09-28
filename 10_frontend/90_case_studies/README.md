# Frontend Case Studies — Browser Trace & Production Evidence

Folder này không thêm một framework mới. Nó dùng các case xuyên nhiều owner để kiểm tra xem người đọc có thật sự nối được Web Platform thành một hệ thống hay chỉ biết từng chapter riêng lẻ.

Canonical theory vẫn nằm ở các track HTML, CSS, JavaScript, React, WebSquare, XML và các domain lân cận. Case study chỉ có vai trò bắt người đọc đi qua boundary:

```text
request
→ response
→ parser
→ DOM / CSSOM
→ style
→ layout
→ paint / composite
→ JavaScript scheduling
→ interaction
→ state
→ network
→ artifact / deployment evidence
```

## 00 — Request → Pixel → Interaction Trace

[00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md](./00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md)

Case này lấy một màn hình web tưởng như đơn giản — mở danh sách, tải dữ liệu, bấm lọc, mở modal — rồi trace từ URL cho tới pixel và interaction. Trọng tâm không phải thuộc pipeline, mà là biết **owner nào tạo ra state nào, work xảy ra lúc nào, evidence nào chứng minh nguyên nhân và failure có thể nằm ở boundary nào**.

## 01 — Rendering Performance Measurement Lab

[01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md](./01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md)

Lab này xử lý gap `paint/composite` trong coverage audit. Người học phải tạo baseline, record trace, phân biệt scripting/style/layout/paint/composite, xác định invalidation và thử một thay đổi duy nhất trước khi kết luận. Mục tiêu là thay câu “property này GPU-accelerated nên nhanh” bằng một quy trình đo được và reproducible.

## Cách dùng

Không đọc case như lời giải cố định. Trước mỗi phần, hãy tự viết hypothesis và expected evidence. Sau đó mới so với flow trong tài liệu.

Một case được xem là hoàn thành khi có thể tạo artifact:

```text
request / network timeline
DOM + style ownership map
main-thread / rendering trace
state + async ordering diagram
failure-mode table
before/after measurement
source → build → deployed artifact evidence
```

Nếu chỉ kết luận “React render nhiều” hoặc “CSS gây reflow” mà không chỉ ra event, invalidation, timing và trace tương ứng thì chưa đạt.
