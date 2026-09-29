# 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

DDL, DML, DCL, 상세

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**에서 만든 기준을 이어받아 **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

Từ **220-230. 하위 질의, 트리거, DBMS 접속 및 데이터 전환**, ta đã có điểm tựa để bước vào **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/55 trước khi đi vào chi tiết.

Để đọc **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **6.1 DDL 문법 (Cú pháp DDL)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 6.1 DDL 문법 (Cú pháp DDL)

Các ý ngay dưới **6.1 DDL 문법 (Cú pháp DDL)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- `CREATE TABLE`: Tạo bảng. Các ràng buộc: `PRIMARY KEY` (Khóa chính), `FOREIGN KEY` (Khóa ngoại), `UNIQUE` (Duy nhất), `CONSTRAINT` (Điều kiện), `CHECK` (Kiểm tra), `DEFAULT` (Mặc định), `NOT NULL` (Không được rỗng).
- `ALTER TABLE`:
  - `ADD` (Thêm cột): `ALTER TABLE table_name ADD col_name datatype;`
  - `MODIFY` (Sửa kiểu/ràng buộc cột): `ALTER TABLE table_name MODIFY col_name datatype;`
  - `DROP` (Xóa cột): `ALTER TABLE table_name DROP col_name;`
  - `RENAME COLUMN`: Đổi tên cột.
- `DROP TABLE` [CASCADE | RESTRICT]: Xóa bảng. CASCADE (xóa luôn đối tượng phụ thuộc), RESTRICT (không xóa nếu đang bị tham chiếu).
- `TRUNCATE TABLE`: Xóa nhanh toàn bộ dữ liệu, giữ lại cấu trúc, **không thể ROLLBACK**.

Các bullet của **6.1 DDL 문법 (Cú pháp DDL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **6.1 DDL 문법 (Cú pháp DDL)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **6.2 DCL 문법 (Cú pháp DCL)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **6.2 DCL 문법 (Cú pháp DCL)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 6.2 DCL 문법 (Cú pháp DCL)

Bây giờ ta đi vào nội dung của **6.2 DCL 문법 (Cú pháp DCL)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- `GRANT 권한 ON 테이블 TO 사용자 [WITH GRANT OPTION];` (Cấp quyền. WITH GRANT OPTION: cho phép người đó cấp quyền tiếp cho người khác).
- `REVOKE 권한 ON 테이블 FROM 사용자 [CASCADE CONSTRAINTS];` (Thu hồi quyền. CASCADE: thu hồi luôn quyền mà người này đã cấp cho người khác).
- `COMMIT`: Lưu vĩnh viễn giao dịch (Transaction) thành công.
- `ROLLBACK`: Hủy bỏ giao dịch bị lỗi, quay về trạng thái cũ.
- `SAVEPOINT`: Đặt điểm lưu để Rollback về điểm đó thay vì toàn bộ.

Các bullet của **6.2 DCL 문법 (Cú pháp DCL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **6.2 DCL 문법 (Cú pháp DCL)**, đừng bắt đầu lại từ số không. **6.3 DML 문법 (Cú pháp DML)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **6.3 DML 문법 (Cú pháp DML)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 6.3 DML 문법 (Cú pháp DML)

Phần nguồn của **6.3 DML 문법 (Cú pháp DML)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- `SELECT [DISTINCT] 속성명 FROM 테이블 WHERE 조건 GROUP BY 속성명 HAVING 조건 ORDER BY 속성명 [ASC|DESC];`
  - `DISTINCT`: Loại bỏ dòng trùng lặp.
  - `GROUP BY`: Nhóm dữ liệu (ROLLUP, CUBE để tính tổng phụ).
  - `HAVING`: Điều kiện cho nhóm (GROUP BY).
- **집계 함수 (Hàm tập hợp):** `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `STDDEV` (độ lệch chuẩn), `VARIANCE` (phương sai).
- **순위 함수 (Hàm xếp hạng):** `RANK` (bỏ qua số hạng: 1, 1, 3), `DENSE_RANK` (không bỏ qua: 1, 1, 2), `ROW_NUMBER` (đánh số thứ tự: 1, 2, 3).
- **WHERE 연산자 (Toán tử điều kiện):** `LIKE '%'` (Nhiều ký tự), `LIKE '_'` (1 ký tự), `BETWEEN A AND B`, `IN()`, `IS NULL`.
- `UPDATE 테이블 SET 속성 = 데이터 WHERE 조건;` (Sửa dữ liệu).
- `DELETE FROM 테이블 WHERE 조건;` (Xóa dữ liệu, có thể ROLLBACK).
- `INSERT INTO 테이블 (속성) VALUES (데이터);` (Thêm dữ liệu).

---

Với **6.3 DML 문법 (Cú pháp DML)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Như vậy, **6.3 DML 문법 (Cú pháp DML)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.