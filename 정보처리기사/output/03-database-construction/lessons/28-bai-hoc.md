# 4. SQL 문법의 종류 (Các loại cú pháp SQL)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **4. SQL 문법의 종류 (Các loại cú pháp SQL)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **4. SQL 문법의 종류 (Các loại cú pháp SQL)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

SQL, 문법의, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**에서 만든 기준을 이어받아 **4. SQL 문법의 종류 (Các loại cú pháp SQL)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **4. SQL 문법의 종류 (Các loại cú pháp SQL)** và nối nó với **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)

Ở bước 28/54, **4. SQL 문법의 종류 (Các loại cú pháp SQL)** xuất hiện như phần tiếp nối của **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **4. SQL 문법의 종류 (Các loại cú pháp SQL)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “4. SQL 문법의 종류 (Các loại cú pháp SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 명령어 (Lệnh) | 설명 & 역할 (Mô tả & Vai trò) | Giải thích (VN) |
|---|---|---|---|
| **DDL** (Data Definition Language) | CREATE, ALTER, DROP, TRUNCATE | 데이터베이스를 **정의**하는 언어, 구조 결정. (Ngôn ngữ định nghĩa dữ liệu - Cấu trúc). | Dùng để Tạo (CREATE), Sửa (ALTER), Xóa hoàn toàn (DROP), hoặc Xóa trắng (TRUNCATE) bảng. Giống như việc xây/đập một ngôi nhà. |
| **DML** (Data Manipulation Language) | SELECT, INSERT, UPDATE, DELETE | 저장된 자료를 조회, 삽입, 수정, 삭제. (Ngôn ngữ thao tác dữ liệu - Nội dung). | Dùng để Thêm, Sửa, Xóa, Lấy dữ liệu bên trong bảng. Giống như việc sắp xếp đồ đạc trong nhà. |
| **DCL** (Data Control Language) | GRANT, REVOKE | 데이터 보안과 권한 제어. (Ngôn ngữ điều khiển dữ liệu - Quyền). | Dùng để cấp quyền hoặc thu hồi quyền. |
| **TCL** (Transaction Control Language) | COMMIT, ROLLBACK, SAVEPOINT | 트랜잭션의 확정, 취소, 부분 복귀. (Ngôn ngữ điều khiển giao dịch). | Dùng để xác nhận, hoàn tác hoặc đặt điểm khôi phục giao dịch. |

> 💡 **Mẹo ghi nhớ:**
> DDL: **CADT** (Create, Alter, Drop, Truncate - "Cắt" cấu trúc).
> DML: **SUDI** (Select, Update, Delete, Insert - "Sửa đi" dữ liệu).
> DCL: **GR** (Grant, Revoke - "Gác quyền"). TCL: **CRS** (Commit, Rollback, Savepoint - "Chốt/Rút/Save").

---

Như vậy, **4. SQL 문법의 종류 (Các loại cú pháp SQL)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.