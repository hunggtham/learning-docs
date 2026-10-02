# 8. 서브쿼리와 뷰 (Truy vấn con và View)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **8. 서브쿼리와 뷰 (Truy vấn con và View)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối subquery với view, scope và query composition, để truy vấn lồng và lớp biểu diễn dữ liệu có owner rõ ràng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **8. 서브쿼리와 뷰 (Truy vấn con và View)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **8. 서브쿼리와 뷰 (Truy vấn con và View)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **191-192. 인덱스 (Index)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **8. 서브쿼리와 뷰 (Truy vấn con và View)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

서브쿼리와

> **Chuyển mạch:** Ở chặng này của **8. 서브쿼리와 뷰 (Truy vấn con và View)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **193. 뷰 (View)**에서 만든 기준을 이어받아 **8. 서브쿼리와 뷰 (Truy vấn con và View)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **8. 서브쿼리와 뷰 (Truy vấn con và View)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. 서브쿼리와 뷰 (Truy vấn con và View)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **8. 서브쿼리와 뷰 (Truy vấn con và View)**, **8. 서브쿼리와 뷰 (Truy vấn con và View)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 8. 서브쿼리와 뷰 (Truy vấn con và View)

Sau khi đã đặt nền bằng **193. 뷰 (View)**, ta chuyển sang **8. 서브쿼리와 뷰 (Truy vấn con và View)**. Đây là mắt xích 32/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 서브쿼리와 뷰 (Truy vấn con và View)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **서브쿼리 (Subquery)**. Hãy xác định **서브쿼리 (Subquery)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 서브쿼리 (Subquery)

Phần nguồn của **서브쿼리 (Subquery)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “서브쿼리 (Subquery)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **단일 행 서브쿼리 (Single-row Subquery):** Trả về 1 dòng. Dùng toán tử `=`, `>`, `<`.
- **다중 행 서브쿼리 (Multi-row Subquery):** Trả về nhiều dòng. Dùng `IN`, `ANY`, `ALL`.
- **인라인 뷰 (Inline View):** Subquery nằm trong mệnh đề `FROM`, tạo thành bảng ảo tạm thời.

Các bullet của **서브쿼리 (Subquery)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **서브쿼리 (Subquery)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **뷰 (VIEW - Bảng ảo)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **뷰 (VIEW - Bảng ảo)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 뷰 (VIEW - Bảng ảo)

Các ý ngay dưới **뷰 (VIEW - Bảng ảo)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “뷰 (VIEW - Bảng ảo)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `CREATE VIEW 뷰명 AS (SELECT문);`
- `DROP VIEW 뷰명;`
- **장점 (Ưu điểm):** Bảo mật (chỉ cho xem cột cần thiết), Đơn giản hóa truy vấn phức tạp, Đảm bảo tính toàn vẹn dữ liệu.
- **단점 (Nhược điểm):** Không thể sửa đổi cấu trúc dễ dàng, cơ bản là Read Only, **Không thể gắn Index (인덱스 불가능)**.

---

Các bullet của **뷰 (VIEW - Bảng ảo)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **뷰 (VIEW - Bảng ảo)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **8. 서브쿼리와 뷰 (Truy vấn con và View)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **191-192. 인덱스 (Index)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **8. 서브쿼리와 뷰 (Truy vấn con và View)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
