# 4. SQL 문법의 종류 (Các loại cú pháp SQL)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. SQL 문법의 종류 (Các loại cú pháp SQL)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **4. SQL 문법의 종류 (Các loại cú pháp SQL)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

SQL, 문법의, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**에서 만든 기준을 이어받아 **4. SQL 문법의 종류 (Các loại cú pháp SQL)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)

Sau khi đã đặt nền bằng **3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)**, ta chuyển sang **4. SQL 문법의 종류 (Các loại cú pháp SQL)**. Đây là mắt xích 29/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **4. SQL 문법의 종류 (Các loại cú pháp SQL)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

| 종류 (Loại) | 명령어 (Lệnh) | 설명 & 역할 (Mô tả & Vai trò) | Giải thích (VN) |
|---|---|---|---|
| **DDL** (Data Definition Language) | CREATE, ALTER, DROP, TRUNCATE | 데이터베이스를 **정의**하는 언어, 구조 결정. (Ngôn ngữ định nghĩa dữ liệu - Cấu trúc). | Dùng để Tạo (CREATE), Sửa (ALTER), Xóa hoàn toàn (DROP), hoặc Xóa trắng (TRUNCATE) bảng. Giống như việc xây/đập một ngôi nhà. |
| **DML** (Data Manipulation Language) | SELECT, INSERT, UPDATE, DELETE | 저장된 자료를 조회, 삽입, 수정, 삭제. (Ngôn ngữ thao tác dữ liệu - Nội dung). | Dùng để Thêm, Sửa, Xóa, Lấy dữ liệu bên trong bảng. Giống như việc sắp xếp đồ đạc trong nhà. |
| **DCL** (Data Control Language) | GRANT, REVOKE, COMMIT, ROLLBACK | 데이터 보안, 무결성, 권한, 병행 수행제어. (Ngôn ngữ điều khiển dữ liệu - Quyền & Giao dịch). | Dùng để Cấp quyền (GRANT), Thu hồi quyền (REVOKE), hoặc kiểm soát giao dịch (COMMIT/ROLLBACK). |

> 💡 **Mẹo ghi nhớ:**
> DDL: **CADT** (Create, Alter, Drop, Truncate - "Cắt" cấu trúc).
> DML: **SUDI** (Select, Update, Delete, Insert - "Sửa đi" dữ liệu).
> DCL: **GRCR** (Grant, Revoke, Commit, Rollback - "Gác cổng" bảo vệ).

---

Ta có thể khép mục **4. SQL 문법의 종류 (Các loại cú pháp SQL)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.