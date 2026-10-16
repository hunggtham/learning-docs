# 09. SQL 언어 체계와 절차형 SQL (Hệ Thống Ngôn Ngữ SQL và SQL Thủ Tục)

## 1. 개요 및 학습 목표 (Tổng quan & Mục tiêu học tập)

- [한국어]: **관계형 데이터베이스 언어인 SQL(Structured Query Language)**은 데이터 정의(DDL), 조작(DML), 제어(DCL), 트랜잭션 제어(TCL)의 4대 영역으로 구성된다. 나아가 단발성 쿼리의 한계를 극복하고 제어 흐름(조건문, 반복문)과 비즈니스 로직을 DBMS 내부에 캡슐화하기 위해 **절차형 SQL(Procedural SQL: 프로시저, 트리거, 사용자 정의 함수)**을 활용한다.
- [Tiếng Việt]: **Ngôn ngữ cơ sở dữ liệu quan hệ SQL (Structured Query Language)** bao gồm 4 phân nhóm chính: Định nghĩa dữ liệu (DDL), Thao tác dữ liệu (DML), Điều khiển dữ liệu (DCL), và Điều khiển giao dịch (TCL). Hơn thế nữa, để khắc phục giới hạn của các câu lệnh đơn lẻ và đóng gói luồng điều khiển (rẽ nhánh, vòng lặp) cùng logic nghiệp vụ ngay trong DBMS, lập trình viên sử dụng **SQL thủ tục (Procedural SQL: Thủ tục lưu trữ, Trigger, Hàm do người dùng định nghĩa)**.

### 학습 목표 (Mục tiêu kiến thức)
1. **SQL 4대 분류 체계 (4 phân nhóm ngôn ngữ SQL):** Nắm vững vai trò, đối tượng thao tác và cú pháp chuẩn của DDL (`데이터 정의어`), DML (`데이터 조작어`), DCL (`데이터 제어어`), và TCL (`트랜잭션 제어어`).
2. **DDL 핵심 구문과 제약조건 (Cú pháp DDL & Ràng buộc):** Sử dụng thành thạo `CREATE`, `ALTER`, `DROP` (kèm tùy chọn `CASCADE` vs `RESTRICT`), phân biệt triệt để `DROP TABLE` vs `TRUNCATE TABLE` vs `DELETE FROM TABLE`.
3. **DML 고급 질의와 연산자 (Truy vấn DML nâng cao & Toán tử):** Nắm vững thứ tự thực thi câu lệnh `SELECT`, các hàm xếp hạng (`RANK`, `DENSE_RANK`, `ROW_NUMBER`), hàm mở rộng nhóm (`ROLLUP`, `CUBE`), toán tử tập hợp (`UNION`, `UNION ALL`, `INTERSECT`, `MINUS`), và các phép `JOIN` (kèm ký hiệu `(+)` của Oracle).
4. **DCL과 TCL 문법 (Cú pháp phân quyền & Giao dịch):** Phân tích lệnh `GRANT`, `REVOKE` (với `WITH GRANT OPTION`), `COMMIT`, `ROLLBACK`, `SAVEPOINT`.
5. **절차형 SQL 3대 객체 (3 đối tượng SQL thủ tục):** Phân biệt bản chất và cú pháp của **저장 프로시저(Stored Procedure)**, **트리거(Trigger)**, và **사용자 정의 함수(User-Defined Function)**.

---

## 2. 개념 연결 및 브리지 (Cầu nối kiến thức)

- **Từ đâu (Origin - Xuất phát điểm):**
  - [한국어]: 이전 [08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md](08-giao-dich-trang-thai-acid-va-dieu-khien-dong-thoi.md)에서 우리는 데이터 일관성을 유지하기 위한 트랜잭션의 ACID 특성과 병행 제어 원리를 확립했습니다.
  - [Tiếng Việt]: Ở bài học trước, chúng ta đã nắm vững nền tảng lý thuyết về giao dịch ACID và các cơ chế kiểm soát đồng thời để bảo vệ tính nhất quán dữ liệu.
- **Đang giải quyết gì (Current Problem - Vấn đề bài học giải quyết):**
  - [한국어]: 본 장에서는 이론적으로 설계된 스키마와 제약조건을 실제 RDBMS에 구축하고 데이터를 조회·수정·제어하기 위한 표준 프로그래밍 언어인 **SQL의 전체 문법 체계**와 복잡한 비즈니스 로직을 일괄 처리하는 **절차형 SQL**을 완성합니다.
  - [Tiếng Việt]: Bài học này giải quyết việc hiện thực hóa các lược đồ thiết kế vào hệ RDBMS thực tế, cung cấp toàn bộ cú pháp chuẩn mực của **Hệ thống ngôn ngữ SQL** và đóng gói logic xử lý hàng loạt bằng **SQL thủ tục**.
- **Dùng đi đâu (Forward Handoff - Chuyển tiếp tương lai):**
  - [한국어]: 여기서 완성된 DDL과 DML 쿼리는 다음 [10-view-index-system-catalog-va-ma-tran-crud.md](10-view-index-system-catalog-va-ma-tran-crud.md)에서 가상 테이블인 뷰(View) 생성, 빠른 검색을 위한 인덱스(Index) 튜닝, 시스템 카탈로그 메타데이터 분석의 핵심 도구로 확장됩니다.
  - [Tiếng Việt]: Các câu lệnh DDL và DML được xây dựng ở đây sẽ là công cụ trực tiếp để tạo Khung nhìn (View), xây dựng Chỉ mục (Index) và phân tích Từ điển dữ liệu hệ thống (System Catalog) ở bài học tiếp theo.

---

## 3. 핵심 이론 및 용어 대조 (Lý thuyết cốt lõi & Đối chiếu thuật ngữ)

### 3.1. SQL 분류 체계 (4 Phân nhóm Ngôn ngữ SQL)

| 그룹 (Nhóm) | 영문 / 한글 명칭 | 대표 명령어 (Lệnh tiêu biểu) | 대상 및 역할 (Đối tượng & Mục đích) |
|---|---|---|---|
| **DDL** | **Data Definition Language**<br>`데이터 정의어` | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | 데이터베이스 구조, 스키마, 테이블, 뷰, 인덱스 생성 및 변경. **실행 시 자동 Commit(Auto-commit)**. |
| **DML** | **Data Manipulation Language**<br>`데이터 조작어` | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | 테이블 내부의 실질적 데이터(레코드) 조회 및 변환. **Commit/Rollback 제어 가능**. |
| **DCL** | **Data Control Language**<br>`데이터 제어어` | `GRANT`, `REVOKE` | 보안, 권한 부여 및 회수, 데이터 무결성 제어. |
| **TCL** | **Transaction Control Language**<br>`트랜잭션 제어어` | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | 트랜잭션 작업 결과의 영구 반영, 취소 및 중간 복원점 설정. |

---

### 3.2. DDL 구문과 테이블 삭제 명령 비교 (Chi tiết DDL & Xóa bảng)

#### 1. DDL 주요 문법
- **CREATE TABLE:**
  ```sql
  CREATE TABLE NHAN_VIEN (
      MaNV VARCHAR2(10) PRIMARY KEY,
      HoTen VARCHAR2(50) NOT NULL,
      Tuoi NUMBER(3) CHECK (Tuoi >= 18),
      MaPhong VARCHAR2(10),
      CONSTRAINT fk_phong FOREIGN KEY (MaPhong) REFERENCES PHONG_BAN(MaPhong)
      ON DELETE CASCADE
  );
  ```
- **ALTER TABLE:**
  - 속성 추가: `ALTER TABLE NHAN_VIEN ADD (Email VARCHAR2(100));`
  - 속성 수정: `ALTER TABLE NHAN_VIEN MODIFY (Email VARCHAR2(150) NOT NULL);`
  - 속성 삭제: `ALTER TABLE NHAN_VIEN DROP COLUMN Email;`
- **DROP TABLE 옵션 (CASCADE vs RESTRICT):**
  - **`CASCADE`**: 삭제할 테이블을 참조하고 있는 외래키 제약조건이나 뷰(View) 등 연관 객체를 **함께 연쇄적으로 강제 삭제**.
  - **`RESTRICT`**: 다른 테이블이나 뷰가 해당 테이블을 참조하고 있는 경우 **삭제 연산을 즉각 거부/취소**.

#### 2. DROP vs TRUNCATE vs DELETE 3대 명령 비교

| 명령어 | 구분 | 대상 | Rollback 가능 여부 | 속도 및 공간 반환 |
|---|:---:|---|:---:|---|
| **`DROP TABLE`** | DDL | 테이블 구조 + 데이터 전체 | **불가능 (Auto-commit)** | 최고속 / 저장 공간 즉시 반환 |
| **`TRUNCATE TABLE`** | DDL | 데이터 전체 (구조는 유지) | **불가능 (Auto-commit)** | 초고속 (Log 최소 기록) / 공간 반환 |
| **`DELETE FROM`** | DML | 특정 레코드 또는 전체 행 | **가능 (Rollback 지원)** | 느림 (Row 단위 Log 기록) / 공간 유지 |

---

### 3.3. DML 문법 및 고급 질의 (DML nâng cao & Thứ tự thực thi)

#### 1. SELECT 문의 논리적 실행 순서 (Thứ tự thực thi câu lệnh SELECT)
- [한국어]: 작성 순서와 달리 DBMS 내부 엔진이 쿼리를 평가하는 논리적 실행 순서는 다음과 같다:
  $$\mathbf{FROM \rightarrow WHERE \rightarrow GROUP\ BY \rightarrow HAVING \rightarrow SELECT \rightarrow ORDER\ BY}$$
- [Tiếng Việt]: Trật tự thực thi logic của câu truy vấn `SELECT` trong động cơ DBMS:
  1. `FROM` (Xác định nguồn bảng) $\rightarrow$ 2. `WHERE` (Lọc từng dòng đơn lẻ) $\rightarrow$ 3. `GROUP BY` (Gom nhóm) $\rightarrow$ 4. `HAVING` (Lọc điều kiện trên nhóm) $\rightarrow$ 5. `SELECT` (Chiếu các cột) $\rightarrow$ 6. `ORDER BY` (Sắp xếp kết quả cuối cùng).

#### 2. 순위 함수 비교 (Hàm xếp hạng: RANK vs DENSE_RANK vs ROW_NUMBER)

| 함수 (Hàm) | 동점 처리 방식 (Trùng điểm) | 예시 점수 [100, 90, 90, 80] 결과 |
|---|---|:---:|
| **`RANK()`** | 동점자에게 동일 등수 부여, 다음 등수는 동점자 수만큼 **건너뜀 (Skip)** | **1, 2, 2, 4** |
| **`DENSE_RANK()`** | 동점자에게 동일 등수 부여, 다음 등수는 **건너뛰지 않고 연속 부여** | **1, 2, 2, 3** |
| **`ROW_NUMBER()`** | 동점 여부와 무관하게 고유한 **연속 행 번호** 강제 부여 | **1, 2, 3, 4** |

#### 3. 집합 연산자와 JOIN
- **집합 연산자 (Set Operators):**
  - `UNION`: 합집합 후 **중복 행 제거** (정렬 비용 발생).
  - `UNION ALL`: 단순 병합, **중복 행 유지** (정렬 없음, 속도 가장 빠름).
  - `INTERSECT`: 교집합 추출.
  - `MINUS / EXCEPT`: 차집합 추출 (Oracle은 `MINUS`, ANSI는 `EXCEPT`).
- **JOIN의 종류와 Oracle `(+)` 연산자:**
  - `LEFT OUTER JOIN`: 왼쪽 테이블의 모든 행 보존. Oracle 문법: `WHERE A.id = B.id(+)` (부족한 오른쪽에 `(+)` 표기).
  - `RIGHT OUTER JOIN`: 오른쪽 테이블의 모든 행 보존. Oracle 문법: `WHERE A.id(+) = B.id`.

#### 4. 그룹 집계 확장 함수 (ROLLUP vs CUBE)
- **`ROLLUP(A, B)`**: 계층적 소계 산출 (오른쪽 컬럼부터 차례로 롤업: `(A, B)` $\rightarrow$ `(A)` $\rightarrow$ `전체 합계`).
- **`CUBE(A, B)`**: 가능한 모든 차원의 결합에 대한 소계 및 총계 산출 ($2^2 = 4$가지 조합: `(A, B)`, `(A)`, `(B)`, `전체 합계`).

---

### 3.4. DCL과 TCL (Phân Quyền & Quản Trị Giao Dịch)

- **DCL 문법 (GRANT / REVOKE):**
  ```sql
  -- Quyền kèm điều kiện cho phép người nhận ủy quyền tiếp cho người thứ ba
  GRANT SELECT, INSERT ON NHAN_VIEN TO USER_A WITH GRANT OPTION;

  -- Thu hồi quyền kèm theo thu hồi dây chuyền mọi quyền mà USER_A đã từng cấp
  REVOKE SELECT, INSERT ON NHAN_VIEN FROM USER_A CASCADE;
  ```
- **TCL 문법 (COMMIT, ROLLBACK, SAVEPOINT):**
  ```sql
  SAVEPOINT sp1;
  UPDATE TAI_KHOAN SET SoDu = SoDu - 100 WHERE ID = 'A';
  ROLLBACK TO sp1; -- Hoàn tác về điểm sp1 mà không hủy toàn bộ giao dịch
  COMMIT;          -- Chốt lưu vĩnh viễn
  ```

---

### 3.5. 절차형 SQL (Procedural SQL) 3대 객체

- [한국어]: 일반 SQL의 비절차적 특성에 조건문(`IF`), 반복문(`LOOP`)을 결합하여 DBMS 엔진 내에서 직접 실행되도록 구현한 모듈이다.

| 구분 (Đối tượng) | 핵심 개념 및 특징 (Bản chất kỹ thuật) | 반환값 (Giá trị trả về) | 호출 방식 (Cách gọi) |
|---|---|:---:|---|
| **저장 프로시저**<br>(Stored Procedure) | 일련의 쿼리를 하나의 이름으로 묶어 DB 서버에 미리 컴파일하여 저장해둔 SQL 집합. 네트워크 트래픽 감소 및 처리 속도 향상. | 반환값 필수 아님<br>(IN, OUT, INOUT 매개변수 활용) | `EXECUTE 프로시저명;`<br>독립 실행문으로 호출 |
| **트리거**<br>(Trigger) | 특정 테이블에 INSERT, UPDATE, DELETE 등 DML 이벤트가 발생할 때 **DBMS에 의해 자동(암묵적)으로 실행**되는 특별한 프로시저. | **반환값 없음**<br>(RETURN 구문 사용 불가) | DBMS 엔진에 의해<br>이벤트 발생 시 자동 발화 |
| **사용자 정의 함수**<br>(User-Defined Function) | 복잡한 수식 연산이나 비즈니스 로직을 처리하여 **단일 값(Scalar) 또는 테이블**을 반환하는 모듈. | **반드시 단일 반환값 존재**<br>(`RETURN 반환값;` 필수) | `SELECT` 절이나 `WHERE` 절 내의 수식으로 호출 |

- **절차형 SQL 기본 구조 블록:**
  ```sql
  DECLARE     -- 선언부: 변수, 상수, 커서(Cursor) 선언
  BEGIN       -- 실행부: 제어문, DML, 비즈니스 로직 수행
  EXCEPTION   -- 예외처리부: 에러 발생 시 처리 루틴
  END;        -- 종료
  ```

---

## 4. 실전 시험 대비 / 함정 분석 (Bẫy đề thi & Trắc nghiệm)

### 함정 포인트 (Trap Points)
1. **Bẫy 순위 함수 (Ranking Function):**
   - Đề bài: Cho điểm thi `[100, 95, 95, 90]`.
     - `RANK()` cho kết quả: **1, 2, 2, 4** (Nhảy cóc số 3).
     - `DENSE_RANK()` cho kết quả: **1, 2, 2, 3** (Liên tục, không nhảy cóc).
     - `ROW_NUMBER()` cho kết quả: **1, 2, 3, 4** (Đánh số độc lập).
2. **Bẫy DROP vs TRUNCATE vs DELETE:**
   - Đề hỏi: *"Lệnh nào xóa toàn bộ bản ghi nhưng giữ lại khung bảng, giải phóng bộ nhớ ngay lập tức và KHÔNG thể phục hồi bằng Rollback?"* $\rightarrow$ Đáp án: **`TRUNCATE TABLE`**.
   - Khẳng định: *"Lệnh DELETE xóa dữ liệu thì không thể Rollback"* $\rightarrow$ **SAI**. DELETE là DML, hoàn toàn Rollback được trước khi COMMIT.
3. **Bẫy Oracle (+) trong phép JOIN:**
   - Đề cho: `WHERE E.dept_no = D.dept_no(+)`.
   - Vị trí `(+)` nằm ở bên phải (`D.dept_no`), nghĩa là bên phải thiếu dữ liệu $\rightarrow$ Bảng chính là bên trái (`E`) $\rightarrow$ Đáp án là **LEFT OUTER JOIN**.
4. **Bẫy 트리거 (Trigger) vs 사용자 정의 함수 (User Function):**
   - Đề hỏi: *"Khối SQL thủ tục nào bắt buộc phải có câu lệnh `RETURN` để trả về giá trị?"* $\rightarrow$ Đáp án: **사용자 정의 함수 (User-Defined Function)**.
   - Khẳng định: *"Trigger có thể được gọi độc lập bằng lệnh EXECUTE"* $\rightarrow$ **SAI**. Trigger chỉ được kích hoạt tự động bởi sự kiện DML.

---

## 5. 복습 체크리스트 (Bảng kiểm tra ôn tập)

- [ ] Phân loại 4 nhóm SQL (DDL, DML, DCL, TCL) và các lệnh tiêu biểu.
- [ ] Phân biệt sự khác nhau giữa CASCADE và RESTRICT trong lệnh DROP.
- [ ] Phân biệt DROP TABLE, TRUNCATE TABLE, DELETE FROM TABLE về tính chất Rollback và giải phóng bộ nhớ.
- [ ] Thuộc lòng thứ tự thực thi của câu lệnh SELECT: FROM $\rightarrow$ WHERE $\rightarrow$ GROUP BY $\rightarrow$ HAVING $\rightarrow$ SELECT $\rightarrow$ ORDER BY.
- [ ] Phân biệt kết quả của RANK(), DENSE_RANK(), ROW_NUMBER().
- [ ] Nhận diện phép JOIN qua ký hiệu (+) trong Oracle.
- [ ] Phân biệt 3 đối tượng 절차형 SQL: Stored Procedure, Trigger, User-Defined Function (về tính chất gọi và giá trị trả về).
