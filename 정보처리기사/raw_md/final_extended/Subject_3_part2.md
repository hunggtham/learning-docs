# 3과목 데이터베이스 구축 (Phần 3: Xây dựng Cơ sở dữ liệu) - Phần 1

> [!NOTE]
> Mặc dù đây là nội dung môn 3 (CSDL), có một số kiến thức hệ điều hành UNIX còn sót lại từ phần trước.

## 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

- **부트 블록 (Boot Block - Khối khởi động):**
  - 부팅 시 필요한 코드를 저장하고 있는 블록.
  - _Giải thích VN:_ Khối lưu trữ mã cần thiết khi khởi động máy.
  - _Ví dụ:_ MBR (Master Boot Record) trong Windows, nhưng ở UNIX nó nằm ở Boot Block, chứa bootloader để nạp hệ điều hành.

- **슈퍼 블록 (Super Block - Siêu khối):**
  - 전체 파일 시스템에 대한 정보를 저장. 사용 가능한 I-node, 사용 가능한 디스크 블록의 개수 등을 포함.
  - _Giải thích VN:_ Chứa thông tin về toàn bộ hệ thống tệp: số lượng I-node trống, các khối đĩa trống. Mỗi hệ thống tệp có Super Block riêng.
  - _Ví dụ:_ Giống như mục lục tổng quát của một thư viện cho biết thư viện có bao nhiêu kệ sách và bao nhiêu sách chưa được mượn.

- **I-node 블록 (I-node Block - Khối I-node):**
  - 각 파일이나 디렉터리에 대한 모든 정보를 저장. (소유자 UID/GID, 파일 크기, 타입, 생성/변경 시기, 권한, 데이터 블록 시작 주소 등).
  - _Giải thích VN:_ Lưu trữ siêu dữ liệu (metadata) của tệp (chủ sở hữu, kích thước, quyền, địa chỉ bắt đầu của dữ liệu, thời gian tạo/sửa).
  - _Ví dụ:_ I-node giống như thẻ căn cước (ID card) của tệp, mọi thông tin quản lý đều nằm ở đây trừ tên tệp và nội dung thực sự.

- **데이터 블록 (Data Block - Khối dữ liệu):**
  - 실제 파일에 대한 데이터가 저장된 블록.
  - _Giải thích VN:_ Nơi lưu trữ nội dung thực tế của tệp hoặc danh sách các thư mục con.
  - _Ví dụ:_ Các trang sách chứa nội dung chữ bên trong thư viện.

> 💡 **Mẹo ghi nhớ (Mnemonics):** 
> Thứ tự các khối: **B**oot -> **S**uper -> **I**-node -> **D**ata (**BSID** - Bác Sĩ I-node Dễ thương).

---

## 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

| 명령어 (Command) | 의미 (Ý nghĩa) | Giải thích & Ví dụ (VN) |
|---|---|---|
| `fork` | 새로운 프로세스 생성 (Tạo tiến trình con/nhân bản tiến trình). | Giống như phân thân. Ví dụ: Tiến trình cha gọi `fork` tạo ra một tiến trình con y hệt để làm việc song song. |
| `exec` | 새로운 프로세스 수행 (Thực thi tiến trình mới). | Thay thế tiến trình hiện tại bằng tiến trình mới. Ví dụ: Dùng `exec` để mở chương trình máy tính (calculator). |
| `&` | 백그라운드 처리 (Chạy nền). | Đặt ở cuối lệnh. Ví dụ: `find / -name test.txt &` (Tìm kiếm ngầm, cho phép gõ tiếp lệnh khác). |
| `wait` | 하위 프로세스 종료 대기 (Đợi tiến trình con kết thúc). | Ví dụ: Tiến trình cha đứng đợi (wait) tiến trình con hoàn thành công việc mới tiếp tục. |
| `exit` | 프로세스 수행 종료 (Kết thúc tiến trình). | Ví dụ: Gõ `exit` để đóng terminal. |
| `cat` | 파일 내용 표시 (Hiển thị nội dung tệp, giống `TYPE` trong DOS). | Ví dụ: `cat file.txt` (In nội dung file.txt ra màn hình). |
| `chmod` | 파일 권한 지정 (Thay đổi quyền truy cập tệp). | Ví dụ: `chmod 777 file.sh` (Cấp toàn quyền đọc, ghi, chạy). |
| `chown` | 소유자 변경 (Thay đổi chủ sở hữu). | Ví dụ: `chown root file.txt` (Đổi chủ tệp thành root). |
| `mount` | 파일 시스템 마운팅 (Gắn hệ thống tệp). | Ví dụ: Cắm USB vào và dùng `mount` để hệ thống nhận diện nội dung USB. |
| `mkfs` | 파일 시스템 생성 (Tạo hệ thống tệp). | Format ổ đĩa. Ví dụ: `mkfs.ext4 /dev/sda1`. |
| `chdir` / `cd` | 디렉터리 위치 변경 (Thay đổi thư mục). | Ví dụ: `cd /home`. |
| `fsck` | 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi hệ thống tệp). | Giống chkdsk trong Windows. Ví dụ: `fsck /dev/sda1`. |
| `rmdir` | 디렉터리 삭제 (Xóa thư mục rỗng). | Ví dụ: `rmdir empty_folder`. |
| `ls` | 파일 목록 확인 (Xem danh sách tệp). | Ví dụ: `ls -l` (Xem danh sách chi tiết). |
| `getpid` / `getppid` | 자신의 / 부모 프로세스 ID 획득 (Lấy PID / Parent PID). | ID tiến trình để quản lý (vd: dùng kill để tắt). |
| `cp` / `mv` / `rm`| 복사 (Copy) / 이동 및 이름 변경 (Move/Rename) / 삭제 (Remove). | `cp a.txt b.txt`, `mv old.txt new.txt`, `rm a.txt`. |
| `finger` | 사용자 정보 표시 (Hiển thị thông tin người dùng). | Xem ai đang đăng nhập vào hệ thống. |

---

# CHAPTER 01 SQL 응용 (Ứng dụng SQL)

## 3. 데이터베이스와 절차형 SQL (Cơ sở dữ liệu và SQL thủ tục)

| 종류 (Loại) | 설명 (Mô tả) | Ví dụ & Giải thích (VN) |
|---|---|---|
| **트리거 (Trigger)** | 테이블 이벤트(Insert, Update, Delete)에 반응해 **자동**으로 실행되는 작업. (Thực thi tự động khi có sự kiện). | _Ví dụ:_ Khi xóa 1 nhân viên khỏi bảng NhânViên, một trigger tự động lưu thông tin nhân viên đó vào bảng NhanVien_NghiViec (Audit log). |
| **프로시저 (Procedure)** | 어떤 행동을 수행하기 위한 일련의 작업 순서. (Một chuỗi các thao tác lưu sẵn để thực thi chung). | _Ví dụ:_ Một procedure `Tinh_Luong_Thang` chạy cuối tháng để tính lương cho toàn bộ công ty. |
| **사용자 정의 함수 (User-Defined Function)** | 단일 값으로 반환할 수 있도록 수행. (Hàm do người dùng định nghĩa, trả về một giá trị duy nhất). | _Ví dụ:_ Hàm `GET_AGE(ngay_sinh)` tự động tính và trả về tuổi. |

---

## 4. SQL 문법의 종류 (Các loại cú pháp SQL)

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

## 5. 스키마 (Schema - Lược đồ)

- **외부 스키마 (External Schema - Lược đồ ngoại):** 사용자나 개발자의 관점 (Góc nhìn người dùng). Nhiều lược đồ ngoại tồn tại cùng lúc (Mỗi người nhìn hệ thống một kiểu).
- **개념 스키마 (Conceptual Schema - Lược đồ khái niệm):** 조직 전체의 논리적 구조, 단 하나만 존재 (Cấu trúc logic của toàn bộ tổ chức, chỉ có 1). Quản lý quan hệ, quyền, bảo mật.
- **내부 스키마 (Internal Schema - Lược đồ nội):** 물리적 저장장치의 관점 (Góc nhìn lưu trữ vật lý). Tổ chức các bản ghi, chỉ mục trên ổ đĩa.

> 💡 **Mẹo ghi nhớ:** **Ngoại - Khái - Nội** (Người dùng (Ngoại) -> Thiết kế CSDL (Khái) -> Ổ cứng (Nội)).

---

## 6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)

### 6.1 DDL 문법 (Cú pháp DDL)
- `CREATE TABLE`: Tạo bảng. Các ràng buộc: `PRIMARY KEY` (Khóa chính), `FOREIGN KEY` (Khóa ngoại), `UNIQUE` (Duy nhất), `CONSTRAINT` (Điều kiện), `CHECK` (Kiểm tra), `DEFAULT` (Mặc định), `NOT NULL` (Không được rỗng).
- `ALTER TABLE`:
  - `ADD` (Thêm cột): `ALTER TABLE table_name ADD col_name datatype;`
  - `MODIFY` (Sửa kiểu/ràng buộc cột): `ALTER TABLE table_name MODIFY col_name datatype;`
  - `DROP` (Xóa cột): `ALTER TABLE table_name DROP col_name;`
  - `RENAME COLUMN`: Đổi tên cột.
- `DROP TABLE` [CASCADE | RESTRICT]: Xóa bảng. CASCADE (xóa luôn đối tượng phụ thuộc), RESTRICT (không xóa nếu đang bị tham chiếu).
- `TRUNCATE TABLE`: Xóa nhanh toàn bộ dữ liệu, giữ lại cấu trúc, **không thể ROLLBACK**.

### 6.2 DCL 문법 (Cú pháp DCL)
- `GRANT 권한 ON 테이블 TO 사용자 [WITH GRANT OPTION];` (Cấp quyền. WITH GRANT OPTION: cho phép người đó cấp quyền tiếp cho người khác).
- `REVOKE 권한 ON 테이블 FROM 사용자 [CASCADE CONSTRAINTS];` (Thu hồi quyền. CASCADE: thu hồi luôn quyền mà người này đã cấp cho người khác).
- `COMMIT`: Lưu vĩnh viễn giao dịch (Transaction) thành công.
- `ROLLBACK`: Hủy bỏ giao dịch bị lỗi, quay về trạng thái cũ.
- `SAVEPOINT`: Đặt điểm lưu để Rollback về điểm đó thay vì toàn bộ.

### 6.3 DML 문법 (Cú pháp DML)
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

## 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

### 집합 연산자 (Toán tử tập hợp)
- `UNION`: Hợp (Loại bỏ trùng lặp).
- `UNION ALL`: Hợp tất cả (Giữ nguyên trùng lặp).
- `INTERSECT`: Giao (Chỉ lấy phần chung).
- `MINUS` / `EXCEPT`: Hiệu (Lấy bảng 1 trừ đi các dòng có trong bảng 2).

### 조인 (JOIN)
- **INNER JOIN**: Lấy các dòng có dữ liệu khớp nhau (Giao). `SELECT * FROM A INNER JOIN B ON A.id = B.id;`
- **OUTER JOIN (LEFT, RIGHT, FULL)**: Lấy cả dữ liệu không khớp. Bên thiếu dữ liệu sẽ điền NULL.
  - Cú pháp Oracle (+): `WHERE A.id = B.id(+)` (Đây là LEFT OUTER JOIN vì dấu (+) nằm ở bảng B, tức là bảng B thiếu cũng không sao).
- **SELF JOIN**: Bảng tự JOIN với chính nó. (Dùng `AS` để tạo bí danh).
- **CROSS JOIN**: Tích Đề-các (Cartesian product), bắt cặp tất cả các dòng của 2 bảng.

---

## 8. 서브쿼리와 뷰 (Truy vấn con và View)

### 서브쿼리 (Subquery)
- **단일 행 서브쿼리 (Single-row Subquery):** Trả về 1 dòng. Dùng toán tử `=`, `>`, `<`.
- **다중 행 서브쿼리 (Multi-row Subquery):** Trả về nhiều dòng. Dùng `IN`, `ANY`, `ALL`.
- **인라인 뷰 (Inline View):** Subquery nằm trong mệnh đề `FROM`, tạo thành bảng ảo tạm thời.

### 뷰 (VIEW - Bảng ảo)
- `CREATE VIEW 뷰명 AS (SELECT문);`
- `DROP VIEW 뷰명;`
- **장점 (Ưu điểm):** Bảo mật (chỉ cho xem cột cần thiết), Đơn giản hóa truy vấn phức tạp, Đảm bảo tính toàn vẹn dữ liệu.
- **단점 (Nhược điểm):** Không thể sửa đổi cấu trúc dễ dàng, cơ bản là Read Only, **Không thể gắn Index (인덱스 불가능)**.

---

## 9. 인덱스와 트랜잭션 (Index và Giao dịch)

### 인덱스 (Index - Chỉ mục)
Dùng để tăng tốc độ tìm kiếm.
- **트리 기반 (Tree-based):** Thường dùng B-Tree, tốt cho tìm theo khoảng.
- **해시 (Hash):** Dùng Key-Value, truy cập nhanh và chi phí đồng đều, không tốt cho tìm khoảng.
- **비트맵 (Bitmap):** Dùng bit 0 và 1, phù hợp cho cột có ít giá trị khác biệt (Gender: M/F).
- **클러스터드 인덱스 (Clustered Index):** Dữ liệu thực sự được sắp xếp vật lý theo thứ tự Index. Rất tốt để tìm khoảng (Range search).

### 트랜잭션 (Transaction - Giao dịch) - ACID
| 특징 (Đặc tính) | 설명 (Mô tả) | Ý nghĩa (VN) |
|---|---|---|
| **원자성 (Atomicity)** | All or Nothing (모두 반영되거나 전혀 반영되지 않음). | **Tính nguyên tử:** Chuyển tiền: hoặc cả 2 người cùng cập nhật, hoặc không ai thay đổi gì. Dùng Commit/Rollback. |
| **일관성 (Consistency)** | 일관적인 DB 상태 유지 (Trạng thái DB nhất quán). | **Tính nhất quán:** Dữ liệu sau giao dịch phải hợp lệ. |
| **고립성 (Isolation)** | 서로 간섭 불가 (Không can thiệp lẫn nhau). | **Tính cô lập:** Khi giao dịch A đang chạy, giao dịch B không thể nhảy vào làm sai lệch. |
| **영속성 (Durability)** | 영구적으로 결과 저장 (Lưu kết quả vĩnh viễn). | **Tính bền vững:** Sau khi COMMIT, dù sập nguồn dữ liệu vẫn tồn tại. |

> 💡 **Mẹo ghi nhớ:** **ACID** (Nguyên tử - Nhất quán - Cô lập - Bền vững).

---

## 10. 트랜잭션 관리 기법 및 제어 (Quản lý và điều khiển giao dịch)

### 병행제어 기법 (Concurrency Control - Kiểm soát đồng thời)
- **로킹 (Locking):** Khóa tài nguyên để đảm bảo giao dịch chạy tuần tự (직렬화).
  - *Đơn vị khóa (Locking Unit):* Càng lớn (DB, Bảng) -> Ít Lock, Overhead nhỏ, Tính đồng thời giảm. Càng nhỏ (Bản ghi, Trường) -> Nhiều Lock, Overhead lớn, Tính đồng thời cao.
- **타임스탬프 (Time Stamping):** Gắn mốc thời gian để ưu tiên.
- **다중버전 동시제어 (MVCC):** Giữ nhiều phiên bản dữ liệu.
- **낙관적 병행제어 (Optimistic):** Cứ cho chạy đi, kết thúc mới kiểm tra lỗi (thích hợp môi trường ít xung đột).

### 트랜잭션 상태 (Trạng thái giao dịch)
- **활동 (Active):** Đang chạy.
- **부분 완료 (Partially Committed):** Đã chạy lệnh xong, chuẩn bị COMMIT nhưng chưa ghi lên đĩa.
- **완료 (Committed):** Thành công và lưu vĩnh viễn.
- **실패 (Failed):** Có lỗi xảy ra.
- **철회 (Aborted):** Bị hủy bỏ (Rollback).

### 데이터 사전 (Data Dictionary / System Catalog / Metadata)
- Lưu thông tin về các đối tượng (bảng, view, index...).
- DBMS tự động cập nhật, người dùng **chỉ được Read Only (조회만 가능)**.

---

## 11. 데이터베이스 설계 (Thiết kế cơ sở dữ liệu)

| 단계 (Giai đoạn) | 설명 (Mô tả & Hoạt động) | Giải thích (VN) |
|---|---|---|
| **1. 요구조건 분석** | 목적 파악, 요구조건 식별 | Phân tích yêu cầu: Tìm hiểu người dùng cần gì. |
| **2. 개념적 설계** | 개념 스키마, E-R 다이어그램, 트랜잭션 모델링 | Thiết kế Khái niệm: Độc lập với DBMS. Vẽ biểu đồ ER (Thực thể - Mối quan hệ). |
| **3. 논리적 설계** | 논리적 자료구조, **정규화(Normalization)**, 트랜잭션 인터페이스 설계 | Thiết kế Logic: Chuyển đổi ER sang bảng (Table). **Thực hiện chuẩn hóa (Normalization)**. |
| **4. 물리적 설계** | 물리적 구조, 저장 레코드 양식, **접근 경로(Access Path)** | Thiết kế Vật lý: Định dạng file trên đĩa cứng, chọn kiểu dữ liệu thực tế, thiết lập cấu trúc lưu trữ và Index (Đường truy cập). |

> 💡 **Mẹo ghi nhớ:** **Yêu - Khái - Lo - Vật** (Yêu cầu -> Khái niệm -> Logic -> Vật lý). Dễ thi: Chuẩn hóa ở bước Logic, Access Path/Lưu trữ ở bước Vật lý.

test
---

## 12. 관계형 데이터 모델과 릴레이션 (Mô hình dữ liệu quan hệ & Relation)

### 12.1 릴레이션의 구조 (Cấu trúc Relation / Bảng)
- **릴레이션 (Relation):** Bảng dữ liệu gồm hàng và cột.
- **튜플 (Tuple):** Hàng (Row / Record).
- **속성 (Attribute):** Cột (Column / Field).
- **차수 (Degree / 디그리):** Số lượng thuộc tính (Cột).
- **카디널리티 (Cardinality):** Số lượng 튜플 (Hàng).
- **도메인 (Domain):** Tập hợp các giá trị nguyên tử (Atomic) mà một thuộc tính có thể nhận.
- **인스턴스 (Instance):** Tập hợp các 튜플 tại một thời điểm (Dữ liệu thực tế).

> 💡 **Mẹo ghi nhớ:** **Car-Tu, De-At** (Cardinality = Tuple/Hàng, Degree = Attribute/Cột).

### 12.2 릴레이션의 특징 (Đặc điểm của Relation)
- **튜플의 유일성:** Không có 2 hàng nào giống hệt nhau.
- **튜플/속성의 무순서:** Thứ tự của các hàng và các cột **không quan trọng**.
- **원자값:** Mỗi ô (giao giữa hàng và cột) chỉ được chứa một giá trị duy nhất (không thể chia nhỏ).

---

## 13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)

### 데이터 모델 구성 요소 (Thành phần mô hình dữ liệu)
- **개체 (Entity):** Đối tượng thực tế (ví dụ: Sinh viên, Môn học).
- **속성 (Attribute):** Đặc điểm của đối tượng (ví dụ: Mã SV, Tên).
- **관계 (Relationship):** Sự liên kết giữa các đối tượng (ví dụ: Đăng ký).
- *Lưu ý: 3 yếu tố cơ bản của mô hình là Cấu trúc (Structure), Phép toán (Operation), và Ràng buộc (Constraint).*

### E-R 다이어그램 기호 (Ký hiệu biểu đồ E-R - Peter Chen)
| 기호 (Ký hiệu) | 의미 (Ý nghĩa) | Giải thích (VN) |
|---|---|---|
| **사각형 (Hình chữ nhật)** | 개체 (Entity) | Đối tượng thực thể. |
| **마름모 (Hình thoi)** | 관계 (Relationship) | Mối quan hệ giữa các thực thể (1:1, 1:N, N:M). |
| **타원 (Hình bầu dục)** | 속성 (Attribute) | Thuộc tính. |
| **밑줄 타원 (Bầu dục gạch dưới)** | 기본키 (Primary Key) | Thuộc tính Khóa chính. |
| **이중 타원 (Bầu dục kép)** | 다중 값 속성 (Multi-valued) | Thuộc tính đa trị (có thể chứa nhiều giá trị, vd: Số điện thoại). |
| **선 (Đường thẳng)** | 링크 (Link) | Đường nối kết. |

---

## 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

### 키(Key) 종류 (Các loại Khóa)
| 종류 (Loại) | 설명 (Mô tả) | Tính chất (VN) |
|---|---|---|
| **슈퍼키 (Super Key)** | 튜플을 구별할 수 있는 속성 집합. | **Tính duy nhất (유일성).** |
| **후보키 (Candidate Key)** | 기본키가 될 수 있는 키 (유일성 + 최소성). | **Duy nhất + Tối thiểu (최소성).** (Không dư thừa thuộc tính). |
| **기본키 (Primary Key)** | 후보키 중 선택된 주키. NULL 불가. | Khóa chính. **Không được trùng, Không được NULL.** |
| **대체키 (Alternate Key)** | 기본키로 선택되지 못한 나머지 후보키. | Khóa thay thế (Khóa phụ). |
| **외래키 (Foreign Key)** | 다른 릴레이션의 기본키를 참조하는 속성. | Khóa ngoại. Dùng để liên kết 2 bảng. |

### 무결성 (Integrity - Tính toàn vẹn / chính xác)
- **개체 무결성 (Entity):** Khóa chính (Primary Key) không được trùng lặp và **không được NULL**.
- **참조 무결성 (Referential):** Khóa ngoại (Foreign Key) phải khớp với Khóa chính của bảng tham chiếu, hoặc có thể là NULL.
- **도메인 무결성 (Domain):** Giá trị phải nằm trong phạm vi định nghĩa (ví dụ: Giới tính chỉ là Nam/Nữ).
- **사용자 정의 무결성 (User-defined):** Phải thỏa mãn các điều kiện do người dùng tự định nghĩa.

---

## 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

### 일반 집합 연산자 (Toán tử tập hợp cơ bản)
- **합집합 (UNION, ∪):** Hợp (lấy tất cả, bỏ trùng lặp).
- **교집합 (INTERSECTION, ∩):** Giao (lấy phần chung).
- **차집합 (DIFFERENCE, —):** Hiệu (R - S: có trong R nhưng không có trong S).
- **교차곱 (CARTESIAN PRODUCT, Х):** Tích Đề-các (kết hợp tất cả các dòng của 2 bảng).

### 순수 관계 연산자 (Toán tử quan hệ thuần túy)
| 연산자 (Toán tử) | 기호 (Ký hiệu) | 설명 (Mô tả) |
|---|---|---|
| **Select (선택)** | **σ (Sigma)** | Lấy các **Hàng (Tuple)** thỏa mãn điều kiện (Phép toán nằm ngang - 수평). |
| **Project (추출)** | **π (Pi)** | Lấy các **Cột (Attribute)** được chỉ định, loại bỏ trùng lặp (Phép toán dọc - 수직). |
| **Join (조인)** | **⋈ (Bowtie)** | Kết hợp 2 bảng dựa trên thuộc tính chung. |
| **Division (나누기)** | **÷ (Divide)** | Trả về các 튜플 của bảng R mà khớp với tất cả giá trị thuộc tính của bảng S. |

> 💡 **Mẹo ghi nhớ:** **Se-Hàng, Pro-Cột** (Select = Hàng/Tuple, Project = Cột/Attribute).

---

## 16. 정규화(Normalization)와 이상 현상(Anomaly)

**정규화 (Chuẩn hóa):** Quá trình chia nhỏ các bảng để giảm thiểu dư thừa dữ liệu và tránh các hiện tượng bất thường (이상 현상).

### 이상 현상 (Anomaly - Bất thường)
- **삽입 이상 (Insertion Anomaly):** Lỗi khi thêm dữ liệu (phải thêm các dữ liệu không mong muốn).
- **갱신 이상 (Update Anomaly):** Lỗi khi cập nhật (cập nhật thiếu sót dẫn đến dữ liệu không nhất quán).
- **삭제 이상 (Deletion Anomaly):** Lỗi 연쇄 삭제 (Xóa dây chuyền) (xóa một dữ liệu kéo theo mất luôn dữ liệu quan trọng khác).

### 정규화 단계 (Các chuẩn - Bắt buộc học thuộc)
| 정규형 (Chuẩn) | 조건 (Điều kiện để đạt được) | Mẹo ghi nhớ (VN) |
|---|---|---|
| **1NF** | **도**메인이 **원자값** (Mọi giá trị phải là Nguyên tử) | **도** (Do - Domain nguyên tử) |
| **2NF** | **부**분 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần) | **부** (Bu - Bỏ phụ thuộc phần) |
| **3NF** | **이**행 함수 종속 제거 (Loại bỏ phụ thuộc hàm bắc cầu: A→B, B→C => A→C) | **이** (I - Loại bắc cầu / I-haeng) |
| **BCNF** | 모든 **결**정자가 후보키 (Tất cả yếu tố quyết định phải là Khóa ứng viên) | **결** (Gyeol - BCNF) |
| **4NF** | **다**치 종속 제거 (Loại bỏ phụ thuộc đa trị) | **다** (Da - Đa trị) |
| **5NF** | **조**인 종속 제거 (Loại bỏ phụ thuộc Join) | **조** (Jo - Join) |

> 💡 **Mẹo ghi nhớ:** **Đồ-Bếp-I-Kết-Đa-Giò** (Đô-main, Bếp-Phần, I-Bắc cầu, Kết-Quyết định, Đa trị, Giò-Chung).

---

## 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

### 스토리지 (Storage - Thiết bị lưu trữ)
- **DAS (Direct Attached Storage):** Kết nối trực tiếp bằng cáp. Nhanh, an toàn nhưng khó mở rộng.
- **NAS (Network Attached Storage):** Kết nối qua mạng (Network-based, File-level). Mềm dẻo nhưng có thể nghẽn mạng.
- **SAN (Storage Area Network):** Dùng cáp quang (Fiber Channel), tốc độ cực cao, đắt tiền.
- **SDS (Software-defined Storage):** Quản lý toàn bộ tài nguyên lưu trữ bằng phần mềm (Ảo hóa lưu trữ).

### 분산 데이터베이스 (Distributed Database - CSDL Phân tán)
Dữ liệu phân bố ở nhiều nơi (máy chủ khác nhau) nhưng người dùng cảm giác như đang dùng 1 CSDL duy nhất.
- **장점 (Ưu điểm):** Đáng tin cậy, dễ mở rộng, tính tự trị khu vực cao.
- **단점 (Nhược điểm):** Thiết kế khó, chi phí cao, bảo mật phức tạp.

**4대 투명성 (4 Đặc tính Trong suốt - Transparency):**
1. **위치 투명성 (Location):** Người dùng không cần biết dữ liệu nằm ở máy chủ nào.
2. **중복(복제) 투명성 (Replication):** Không cần biết dữ liệu được nhân bản ra sao.
3. **병행 투명성 (Concurrency):** Nhiều người truy cập cùng lúc vẫn không bị lỗi kết quả.
4. **장애 투명성 (Failure):** Một Node chết, toàn hệ thống vẫn hoạt động bình thường.

---

## 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

### 파티셔닝 (Partitioning)
Chia các bảng lớn thành các phần nhỏ (Partition) để dễ quản lý và tăng hiệu suất.
- **범위 분할 (Range):** Phân chia theo khoảng (VD: Tháng 1, Tháng 2).
- **해시 분할 (Hash):** Dùng hàm băm để chia đều. Dữ liệu phân bố đều nhưng khó tìm theo khoảng.
- **목록 분할 (List):** Phân chia theo danh sách giá trị (VD: Nước: VN, KR, US).
- **조합 분할 (Composite):** Kết hợp các phương pháp trên.
- **라운드 로빈 (Round Robin):** Chia xoay vòng đều nhau tuần tự (Không cần khóa).

### 데이터베이스 암호화 (Mã hóa CSDL)
- **암호화 (Encryption):** Biến 평문 (Plaintext - Văn bản gốc) thành 암호문 (Ciphertext - Bản mã).
- **복호화 (Decryption):** Giải mã từ Ciphertext về Plaintext.
- **키 (Key):** Chìa khóa dùng để mã hóa và giải mã.
---

## 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

### 개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)
- **개념 (Khái niệm):** Dùng **CÙNG MỘT KHÓA** để mã hóa và giải mã (단일키 - Khóa đơn).
- **장점 (Ưu điểm):** Tốc độ xử lý cực kỳ nhanh.
- **단점 (Nhược điểm):** Khó phân phối và quản lý khóa khi có quá nhiều người dùng.
- **종류 (Thuật toán tiêu biểu):** DES, AES, SEED, ARIA. (Chia làm 2 dạng: Block - theo khối, Stream - theo luồng bit).

> 💡 **Mẹo ghi nhớ:** **Đối-Cá-Nhanh-Khó** (Khóa Đối xứng = Khóa Cá nhân = Nhanh = Khó quản lý khóa).

### 접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)
| 종류 (Loại) | 기준 (Tiêu chí) | 특징 (Đặc điểm VN) |
|---|---|---|
| **DAC (임의 접근통제)** | 소유자 (Chủ sở hữu) | Chủ dữ liệu tự do cấp/thu quyền (GRANT/REVOKE). |
| **MAC (강제 접근통제)** | 보안 등급 (Mức độ bảo mật) | Hệ thống ép buộc dựa trên cấp độ bảo mật (VD: Top Secret). |
| **RBAC (역할기반 접근통제)** | 역할 (Vai trò) | Quyền gắn với chức vụ (VD: Manager, Staff). Đổi chức vụ = tự đổi quyền. |

### MAC 보안 모델 (Các mô hình bảo mật của MAC)
- **벨-라파듈라 (Bell-LaPadula):** Tập trung vào **기밀성 (Tính Bảo mật / Kín đáo)** (Quân đội). Không đọc lên trên, Không ghi xuống dưới.
- **비바 (Biba):** Tập trung vào **무결성 (Tính Toàn vẹn)**. Ngăn chặn việc sửa đổi trái phép.
- **클락-윌슨 (Clark-Wilson):** Dành cho thương mại, chỉ cho phép sửa qua phần mềm được ủy quyền.
- **만리장성 (Chinese Wall):** Tránh xung đột lợi ích (người xem hồ sơ công ty A thì không được xem của đối thủ B).

---

## 20. 쿼리 성능 최적화와 반정규화 (Tối ưu hóa Truy vấn và Phi chuẩn hóa)

### 쿼리 성능 최적화 (Query Optimization)
Tối ưu hóa tốc độ chạy SQL thông qua **Optimizer (옵티마이저 - Bộ tối ưu)**.
- **RBO (Rule-Based Optimizer):** Tối ưu theo **규칙 (Quy tắc)** định sẵn. Phụ thuộc vào kinh nghiệm người lập trình.
- **CBO (Cost-Based Optimizer):** Tối ưu theo **비용 (Chi phí)** ước tính dựa trên thống kê dữ liệu. Rất thông minh và phổ biến hiện nay.
- **APM (Application Performance Management):** Công cụ giám sát hiệu suất ứng dụng.

### 반정규화 (Denormalization - Phi chuẩn hóa)
- **개념:** Cố tình phá vỡ chuẩn hóa (Gộp bảng, thêm dữ liệu trùng lặp).
- **목적:** Để **tăng hiệu suất truy vấn (조회 속도 향상)** khi thao tác JOIN quá nhiều.
- **단점:** Đánh đổi bằng sự **suy giảm tính nhất quán** (데이터 정합성 저하) và khó khăn khi cập nhật dữ liệu.

---

## 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

### 데이터 전환 (Data Migration - Di chuyển dữ liệu)
Là quá trình chuyển dữ liệu từ hệ thống cũ sang hệ thống mới.
- **ETL 3 bước:** 
  1. **E**xtraction (추출): Trích xuất từ nguồn.
  2. **T**ransformation (변환): Biến đổi cho phù hợp chuẩn mới.
  3. **L**oad (적재): Nạp vào hệ thống đích.

### 오류 데이터 정제 (Error Data Cleansing)
Quản lý trạng thái lỗi trong quá trình chuyển đổi:
- **Open (Mở):** Phát hiện lỗi, chưa phân tích.
- **Assigned (Đã giao):** Giao cho lập trình viên sửa.
- **Fixed (Đã sửa):** Đã sửa xong.
- **Closed (Đóng):** Đã test lại và xác nhận bình thường.
- **Deferred (Trì hoãn):** Quyết định chưa sửa lúc này (hoặc không phải lỗi).

---

## 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

### CRUD 분석 (Phân tích CRUD)
- Tạo ma trận (Matrix) giữa **Process (Tiến trình)** và **Table (Bảng)**.
- Đánh dấu **C**reate, **R**ead, **U**pdate, **D**elete để xem bảng nào bị thao tác nhiều/ít, phát hiện bảng bị bỏ sót (ít nhất mỗi bảng phải có 1 thao tác).

### MyBatis (프레임워크)
- Khung làm việc (Framework) giúp đơn giản hóa JDBC trong Java.
- **Đặc điểm:** Tách mã SQL ra khỏi mã Java (lưu trong file XML hoặc Annotation), thân thiện với lập trình viên SQL.

### 시스템 카탈로그 (System Catalog)
- **Định nghĩa:** CSDL đặc biệt chứa "dữ liệu về dữ liệu" (Metadata / Data Dictionary).
- **Đặc điểm:** Chỉ có hệ thống (DBMS) mới được quyền cập nhật (Tự động cập nhật). Người dùng chỉ có quyền **SELECT (Đọc)**.

### 연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL)
- 산술 연산자 (Toán học: `* / + -`) **>** 관계 연산자 (So sánh: `< > = !=`) **>** 논리 연산자 (Logic: `NOT > AND > OR`).

> 💡 **Mẹo ghi nhớ:** **Toán - Quan - Lo** (Toán học - Quan hệ - Logic). Nhân chia trước, cộng trừ sau, rồi đến so sánh, cuối cùng là AND/OR.

EOF
