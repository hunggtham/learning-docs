# 6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 회복 (Recovery)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

객체, 시스템, 개념

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**에서 만든 기준을 이어받아 **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)** và nối nó với **1. 회복 (Recovery)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)

Ở bước 43/69, **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)** xuất hiện như phần tiếp nối của **5. 관계 데이터 연산 및 정규화 (Phép toán quan hệ & Chuẩn hóa)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **SQL의 3가지 분류 (Phân loại câu lệnh SQL)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **SQL의 3가지 분류 (Phân loại câu lệnh SQL)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### SQL의 3가지 분류 (Phân loại câu lệnh SQL)

Bây giờ ta đi vào nội dung của **SQL의 3가지 분류 (Phân loại câu lệnh SQL)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “SQL의 3가지 분류 (Phân loại câu lệnh SQL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DDL (데이터 정의어):** `CREATE`, `ALTER`, `DROP`.
- **DML (데이터 조작어):** `SELECT`, `INSERT`, `DELETE`, `UPDATE`.
- **DCL (데이터 제어어):** `COMMIT` (Lưu vĩnh viễn), `ROLLBACK` (Hoàn tác), `GRANT` (Cấp quyền), `REVOKE` (Thu hồi quyền).

Các bullet của **SQL의 3가지 분류 (Phân loại câu lệnh SQL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **SQL의 3가지 분류 (Phân loại câu lệnh SQL)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **SELECT 명령어 구조 (Cấu trúc lệnh SELECT)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **SELECT 명령어 구조 (Cấu trúc lệnh SELECT)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### SELECT 명령어 구조 (Cấu trúc lệnh SELECT)

Phần nguồn của **SELECT 명령어 구조 (Cấu trúc lệnh SELECT)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “SELECT 명령어 구조 (Cấu trúc lệnh SELECT)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `SELECT` [DISTINCT] 속성명 `FROM` 테이블명 `WHERE` 조건 `GROUP BY` 속성 `HAVING` 그룹조건 `ORDER BY` 속성 [ASC|DESC]
- 그룹 함수: COUNT (Số lượng), MAX (Lớn nhất), MIN (Nhỏ nhất), SUM (Tổng), AVG (Trung bình).

Các bullet của **SELECT 명령어 구조 (Cấu trúc lệnh SELECT)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **SELECT 명령어 구조 (Cấu trúc lệnh SELECT)**, đừng bắt đầu lại từ số không. **삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)

Các ý ngay dưới **삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **INSERT:** `INSERT INTO` 테이블명(속성) `VALUES` (데이터);
- **DELETE:** `DELETE FROM` 테이블명 `WHERE` 조건; (Lưu ý: DROP là xóa bảng, DELETE là xóa dòng).
- **UPDATE:** `UPDATE` 테이블명 `SET` 속성=데이터 `WHERE` 조건;

Các bullet của **삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**삽입 / 삭제 / 갱신 문법 (Cú pháp Thêm, Xóa, Sửa)** vừa cho ta cách đặt câu hỏi. Bây giờ **뷰 (View)의 특징 (Đặc điểm của View)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **뷰 (View)의 특징 (Đặc điểm của View)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 뷰 (View)의 특징 (Đặc điểm của View)

Bây giờ ta đi vào nội dung của **뷰 (View)의 특징 (Đặc điểm của View)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “뷰 (View)의 특징 (Đặc điểm của View)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기본 테이블에서 유도된 가상 테이블 (Bảng ảo). 물리적으로 존재하지 않음.
- 필요한 데이터만 보여줘서 자동 보안 제공.
- 뷰의 정의를 `ALTER`로 변경할 수 없으며 (삭제 후 다시 생성해야 함), 인덱스를 가질 수 없음. (Không thể sửa định nghĩa, không có index).
- 생성: `CREATE VIEW`, 삭제: `DROP VIEW 뷰이름 CASCADE` (xóa tất cả liên quan) / `RESTRICT` (nếu đang bị dùng thì cấm xóa).

Các bullet của **뷰 (View)의 특징 (Đặc điểm của View)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **뷰 (View)의 특징 (Đặc điểm của View)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)

Phần nguồn của **내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **내장 SQL (Embedded SQL):** 응용 프로그램 코드 내에 삽입된 SQL. 수행 결과로 단 하나의 튜플만 반환됨. (SQL nhúng trong code như Java/C, chỉ trả về 1 dòng 1 lúc).
- **시스템 카탈로그 (System Catalog = Data Dictionary):** 스키마, 권한 등 메타 데이터(Meta-Data)를 저장하는 시스템 DB. (Từ điển dữ liệu chứa thông tin cấu trúc DB).
- 시스템이 자동으로 갱신하며, 사용자는 SELECT로 검색할 수 있지만 갱신(UPDATE/INSERT)은 불가. (Chỉ được xem, không được tự ý sửa).

Với **내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **내장 SQL과 시스템 카탈로그 (Embedded SQL & System Catalog)**, đừng bắt đầu lại từ số không. **트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)

Các ý ngay dưới **트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터베이스 상태를 변환시키는 하나의 논리적 단위 (복구 및 병행 수행의 단위). (Đơn vị công việc logic, ví dụ: 1 giao dịch chuyển tiền).
- **Atomicity (원자성):** 모두 반영되거나 아예 반영되지 않아야 함 (All or Nothing). (Thành công toàn bộ hoặc không có gì).
- **Consistency (일관성):** 트랜잭션 성공 완료 후 항상 일관성 있는 상태 유지. (Kết thúc giao dịch dữ liệu phải đúng đắn, không vi phạm ràng buộc).
- **Isolation (독립성, 격리성):** 실행 중에 다른 트랜잭션이 끼어들 수 없음. (Giao dịch đang chạy thì giao dịch khác không được can thiệp vào giữa chừng).
- **Durability (영속성, 지속성):** 완료된 결과는 영구적으로 반영되어야 함. (Giao dịch xong thì kết quả phải lưu vĩnh viễn dù cúp điện).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **ACID** (Atomicity, Consistency, Isolation, Durability) hoặc **NNĐT** (Nguyên - Nhất - Độc - Trì): **Người Ngoan Đáng Thương**.

# 정보처리기사 - Subject 1 Part 2

Các ý về **트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Như vậy, **트랜잭션(Transaction)의 정의와 4가지 특성 (Định nghĩa & 4 Đặc tính ACID)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Như vậy, **6. SQL과 객체, 시스템 개념 (SQL, View, Catalog & Transaction)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **1. 회복 (Recovery)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.