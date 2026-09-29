# 8. 서브쿼리와 뷰 (Truy vấn con và View)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **8. 서브쿼리와 뷰 (Truy vấn con và View)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **8. 서브쿼리와 뷰 (Truy vấn con và View)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **191-192. 인덱스 (Index)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

서브쿼리와

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **193. 뷰 (View)**에서 만든 기준을 이어받아 **8. 서브쿼리와 뷰 (Truy vấn con và View)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 8. 서브쿼리와 뷰 (Truy vấn con và View)

Sau khi đã đặt nền bằng **193. 뷰 (View)**, ta chuyển sang **8. 서브쿼리와 뷰 (Truy vấn con và View)**. Đây là mắt xích 32/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **8. 서브쿼리와 뷰 (Truy vấn con và View)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **서브쿼리 (Subquery)**. Hãy xác định **서브쿼리 (Subquery)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 서브쿼리 (Subquery)

Phần nguồn của **서브쿼리 (Subquery)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **단일 행 서브쿼리 (Single-row Subquery):** Trả về 1 dòng. Dùng toán tử `=`, `>`, `<`.
- **다중 행 서브쿼리 (Multi-row Subquery):** Trả về nhiều dòng. Dùng `IN`, `ANY`, `ALL`.
- **인라인 뷰 (Inline View):** Subquery nằm trong mệnh đề `FROM`, tạo thành bảng ảo tạm thời.

Các bullet của **서브쿼리 (Subquery)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **서브쿼리 (Subquery)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **뷰 (VIEW - Bảng ảo)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **뷰 (VIEW - Bảng ảo)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 뷰 (VIEW - Bảng ảo)

Các ý ngay dưới **뷰 (VIEW - Bảng ảo)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- `CREATE VIEW 뷰명 AS (SELECT문);`
- `DROP VIEW 뷰명;`
- **장점 (Ưu điểm):** Bảo mật (chỉ cho xem cột cần thiết), Đơn giản hóa truy vấn phức tạp, Đảm bảo tính toàn vẹn dữ liệu.
- **단점 (Nhược điểm):** Không thể sửa đổi cấu trúc dễ dàng, cơ bản là Read Only, **Không thể gắn Index (인덱스 불가능)**.

---

Các bullet của **뷰 (VIEW - Bảng ảo)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **뷰 (VIEW - Bảng ảo)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **8. 서브쿼리와 뷰 (Truy vấn con và View)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **191-192. 인덱스 (Index)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.