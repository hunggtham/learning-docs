# 10. 뷰, 인덱스, 시스템 카탈로그와 CRUD 매트릭스 (View, Index, System Catalog và Ma Trận CRUD)

## 1. 개요 및 학습 목표 (Tổng quan & Mục tiêu học tập)

- [한국어]: 데이터베이스의 논리적 보안과 편의성을 제공하는 가상 테이블인 **뷰(View)**, 빠른 데이터 접근 경로를 제공하는 물리적 저장 구조인 **인덱스(Index)**, 시스템의 모든 객체 메타데이터를 관리하는 **시스템 카탈로그(System Catalog / 데이터 사전)**는 DBMS의 핵심 구성 요소이다. 아울러 애플리케이션 프로세스와 데이터 모델 간의 상호작용 및 트랜잭션 부하를 체계적으로 검증하기 위해 **CRUD 매트릭스(CRUD Matrix)** 분석 기법을 적용한다.
- [Tiếng Việt]: Khung nhìn **(View / 뷰)** là bảng ảo cung cấp tính bảo mật và độc lập logic; Chỉ mục **(Index / 인덱스)** là cấu trúc vật lý cung cấp lộ trình truy xuất nhanh nhất; Từ điển dữ liệu **(System Catalog / 시스템 카탈로그)** lưu trữ toàn bộ siêu dữ liệu mô tả các đối tượng của hệ thống. Đồng thời, để kiểm toán tính tương thích giữa tiến trình ứng dụng và bảng dữ liệu cũng như ước lượng tải giao dịch, kỹ sư áp dụng kỹ thuật phân tích **Ma trận CRUD (CRUD Matrix)**.

### 학습 목표 (Mục tiêu kiến thức)
1. **뷰(View)의 특성과 제약사항 (Đặc tính & Ràng buộc của View):** Nắm vững bản chất bảng ảo (`가상 테이블`), ưu điểm bảo mật và độc lập logic (`논리적 독립성`), cùng các giới hạn thi cử: không có chỉ mục độc lập (`인덱스 생성 불가`), không có lệnh `ALTER VIEW`, hạn chế thao tác DML.
2. **인덱스(Index) 5대 구조 및 설계 규칙 (5 cấu trúc Index & Quy tắc thiết kế):** Phân tích sâu B+Tree, Bitmap Index (cho cột độ phân biệt thấp), Function-Based Index, Bitmap Join Index, Domain Index; phân biệt Clustered Index vs Non-Clustered Index; hiểu quy luật giảm thiểu index trên bảng có tần suất INSERT/DELETE cao.
3. **시스템 카탈로그의 관리 원칙 (Nguyên tắc quản trị System Catalog):** Nắm chắc bản chất siêu dữ liệu (`메타데이터`), cơ chế DBMS tự động cập nhật khi chạy DDL, và quyền hạn của người dùng (chỉ được `SELECT`, cấm can thiệp DML).
4. **CRUD 매트릭스 분석과 품질 점검 (Phân tích & Kiểm định ma trận CRUD):** Ánh xạ 4 thao tác C-R-U-D với câu lệnh SQL, ứng dụng đo lường tần suất giao dịch (`트랜잭션 발생 횟수`) và ước tính dung lượng dữ liệu (`데이터 용량 산정`), quy tắc kiểm định bắt buộc (mỗi bảng phải có ít nhất 1 C và 1 R).

---

## 2. 개념 연결 및 브리지 (Cầu nối kiến thức)

- **Từ đâu (Origin - Xuất phát điểm):**
  - [한국어]: 이전 [09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md](09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md)에서 우리는 DDL, DML, DCL의 전체 구문 체계와 절차형 SQL(프로시저, 트리거)의 실행 구조를 정립했습니다.
  - [Tiếng Việt]: Ở bài học trước, chúng ta đã nắm trọn vẹn cú pháp DDL, DML, DCL, TCL và cơ chế thực thi của các khối lệnh SQL thủ tục.
- **Đang giải quyết gì (Current Problem - Vấn đề bài học giải quyết):**
  - [한국어]: 본 장에서는 DDL로 생성된 테이블을 바탕으로 사용자에게 필요한 가상 뷰(View)를 정의하고, 물리적 질의 속도를 비약적으로 높이는 인덱스(Index)를 설계하며, 시스템 내부 메타데이터 카탈로그와 프로세스-데이터 간의 상호작용(CRUD 매트릭스)을 분석하여 시스템 무결성을 검증합니다.
  - [Tiếng Việt]: Bài học này giải quyết việc xây dựng các khung nhìn logic ảo (View), thiết kế cấu trúc chỉ mục vật lý (Index) để tối ưu tốc độ đọc, đồng thời khai thác siêu dữ liệu hệ thống (Catalog) và lập ma trận CRUD để đo tải giao dịch, rà soát khiếm khuyết thiết kế.
- **Dùng đi đâu (Forward Handoff - Chuyển tiếp tương lai):**
  - [한국어]: 뷰와 인덱스 및 CRUD 부하 분석 결과는 다음 [11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md](11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md)에서 대규모 네트워크 분산 환경의 투명성(Transparency) 확보 및 물리적 노드 분할 설계로 직결됩니다.
  - [Tiếng Việt]: Các phân tích về tải CRUD và cấu trúc chỉ mục này sẽ làm cơ sở trực tiếp để thiết kế kiến trúc phân tán, tính trong suốt (Transparency) và phân mảnh dữ liệu trên mạng ở bài học tiếp theo.

---

## 3. 핵심 이론 및 용어 대조 (Lý thuyết cốt lõi & Đối chiếu thuật ngữ)

### 3.1. 뷰(View)의 특성과 제약사항 (Bản chất & Giới hạn của Khung nhìn)

- [한국어]: **뷰(View)**는 하나 이상의 기본 테이블(Base Table)로부터 유도된 이름을 가지는 **가상 테이블(Virtual Table)**이다. 물리적으로 데이터를 저장하지 않고, 뷰 정의(SELECT 문)만 시스템 카탈로그에 보관된다.
- [Tiếng Việt]: **Khung nhìn (View)** là một **bảng ảo (Virtual Table)** có tên gọi được tạo ra từ kết quả truy vấn của một hay nhiều bảng cơ sở. View không lưu dữ liệu thực tế trên đĩa cứng mà chỉ lưu câu lệnh định nghĩa trong Từ điển dữ liệu hệ thống.

```
[ Bảng cơ sở A ] ───┐
                    ├──> [ Lệnh SELECT định nghĩa View ] ──> [ View (Bảng ảo) ] ──> [ Người dùng tra cứu ]
[ Bảng cơ sở B ] ───┘
```

| 구분 (Tiêu chí) | 핵심 내용 (Nội dung chi tiết) | 시험 핵심 포인트 (Điểm lưu ý thi cử) |
|---|---|---|
| **장점 (Ưu điểm)** | • **논리적 데이터 독립성 제공:** 기본 테이블 구조가 변경되어도 뷰를 사용하는 응용 프로그램은 보호됨.<br>• **보안성 향상:** 민감한 컬럼(급여, 주민번호)을 제외하고 뷰를 구성하여 권한 제어.<br>• **질의문 단순화:** 복잡한 다중 조인 및 집계 쿼리를 뷰로 캡슐화하여 재사용. | • 논리적 독립성과 보안성이 가장 대표적인 장점. |
| **제약사항 (Hạn chế)** | • **독립적인 인덱스를 가질 수 없음:** 뷰 자체에는 물리적 인덱스 생성 불가.<br>• **구조 변경 불가:** `ALTER VIEW` 문법이 존재하지 않으며, 수정 시 `DROP VIEW` 후 재생성해야 함.<br>• **DML 연산의 엄격한 제약:** 집계 함수(SUM, AVG), `GROUP BY`, `DISTINCT`, `JOIN`이 포함된 뷰는 `INSERT`/`UPDATE`/`DELETE` 불가. | • **독립 인덱스 생성 불가**는 단골 기출 지문. |

---

### 3.2. 인덱스(Index)의 개념과 5대 물리 구조 (Chỉ mục & 5 Cấu trúc Vật lý)

- [한국어]: **인덱스(Index)**는 데이터 레코드에 빠르게 접근하기 위해 `<키 값, 포인터(ROWID)>` 쌍으로 구성된 데이터 구조이다.
- [Tiếng Việt]: **Chỉ mục (Index)** là cấu trúc dữ liệu lưu trữ các cặp `<Giá trị khóa, Con trỏ (ROWID)>` giúp định vị bản ghi trên khối đĩa ở tốc độ cao nhất mà không cần quét toàn bộ bảng (Table Full Scan).

| 인덱스 종류 (Loại Index) | 한글 / 영문 명칭 | 구조 및 특징 (Đặc trưng kỹ thuật) | 최적 적용 환경 (Trường hợp tối ưu) |
|---|---|---|---|
| **B+ 트리 인덱스** | `B+ Tree Index`<br>(트리 기반) | 루트(Root), 브랜치(Branch), 리프(Leaf) 노드로 구성. 리프 노드들은 양방향 링크드 리스트로 연결되어 순차 검색 우수. | **가장 널리 쓰이는 표준 인덱스**. 범위 검색(`BETWEEN`, `<`, `>`) 및 일치 검색에 최적. |
| **비트맵 인덱스** | `Bitmap Index`<br>(비트맵 기반) | 컬럼의 데이터를 0과 1의 비트(Bit) 벡터로 변환하여 저장. 크기가 매우 작고 비트 연산(AND, OR)으로 초고속 처리. | **카디널리티가 낮은 컬럼** (성별: 남/여, 혼인여부 등 고유값 종류가 적은 경우). Data Warehouse에 적합. |
| **함수 기반 인덱스** | `Function-Based Index`<br>(함수 기반) | 컬럼 값 자체 대신 함수나 수식을 적용한 결과값에 대해 인덱스를 생성 (예: `UPPER(이메일)`). | WHERE 절에서 가공된 컬럼을 자주 조회하는 경우. 데이터 적재 시 연산 부하 발생. |
| **비트맵 조인 인덱스** | `Bitmap Join Index`<br>(조인 인덱스) | 다수의 테이블을 미리 조인한 결과에 대해 비트맵 인덱스를 구축. | 스타 스키마(Star Schema) 기반의 DW 환경에서 팩트-디멘션 조인 성능 극대화. |
| **도메인 인덱스** | `Domain Index`<br>(확장형 인덱스) | 개발자가 특정 업무 영역(GIS 공간 정보, 비정형 텍스트 등)에 맞추어 직접 정의하고 구축하는 인덱스. | 지리정보시스템(GIS), 멀티미디어, 전문(Full-Text) 검색. |

#### 클러스터드 vs 넌클러스터드 인덱스 심층 비교

- **클러스터드 인덱스 (Clustered Index):**
  - [한국어]: 테이블의 실제 데이터 행 자체가 인덱스 키 순서대로 **물리적으로 정렬되어 저장**되는 인덱스. 리프 노드가 곧 실제 데이터 페이지이다.
  - [Tiếng Việt]: Dữ liệu thực tế của các dòng được **sắp xếp vật lý** trực tiếp theo thứ tự của khóa chỉ mục trên đĩa cứng; nút lá chính là trang dữ liệu thực. **Mỗi bảng chỉ có duy nhất 1 Clustered Index** (thường là Primary Key).
- **넌클러스터드 인덱스 (Non-Clustered Index / 보조 인덱스):**
  - [한국어]: 실제 데이터 페이지는 정렬되지 않은 채 힙(Heap) 영역에 존재하고, 인덱스 리프 노드는 실제 행을 가리키는 포인터(ROWID)만을 보관함.
  - [Tiếng Việt]: Vị trí vật lý của dữ liệu không đổi; nút lá của chỉ mục chỉ chứa con trỏ (ROWID) trỏ đến dòng dữ liệu thực. **Một bảng có thể tạo nhiều Non-Clustered Index**.
- **인덱스 설계 시 주의점 (Quy tắc thiết kế):**
  - [한국어]: 레코드의 **삽입(INSERT)과 삭제(DELETE)가 빈번하게 발생하는 테이블**에서는 인덱스 개수를 최소화해야 한다. (데이터 변경 시마다 모든 인덱스 트리 재구성으로 성능 급락).
  - [Tiếng Việt]: Đối với bảng có tần suất **INSERT/DELETE liên tục**, bắt buộc phải duy trì số lượng chỉ mục ở mức tối thiểu để tránh sụp đổ hiệu năng do việc liên tục tái cân bằng cây chỉ mục.

---

### 3.3. 시스템 카탈로그 (System Catalog / 데이터 사전)

- [한국어]: **시스템 카탈로그(System Catalog)**는 데이터베이스에 저장되어 있는 모든 데이터 개체(테이블, 뷰, 인덱스, 사용자, 권한 등)에 대한 정의나 명세 정보를 수록하고 있는 시스템 데이터베이스이다. 카탈로그에 저장된 정보를 **메타데이터(Metadata - 데이터에 관한 데이터)**라고 부른다.
- [Tiếng Việt]: **Từ điển dữ liệu (System Catalog / 데이터 사전)** là cơ sở dữ liệu hệ thống lưu trữ các định nghĩa, đặc tả mô tả về tất cả các đối tượng (bảng, khung nhìn, chỉ mục, người dùng, quyền hạn) trong CSDL. Thông tin lưu trong ca-ta-lô được gọi là **Siêu dữ liệu (Metadata - dữ liệu mô tả dữ liệu)**.

```
[ Người dùng thực thi DDL ] ───> [ DBMS 엔진 ] ──(Tự động cập nhật)──> [ 시스템 카탈로그 (데이터 사전) ]
                                      │
[ Người dùng tra cứu ] ───────────────┴──(Chỉ cho phép SELECT)────────> [ Đọc Metadata ]
```

- **시스템 카탈로그의 3대 핵심 특징:**
  1. **DBMS 자동 유지관리:** 사용자가 DDL(`CREATE`, `ALTER`, `DROP`) 문을 실행하면 DBMS가 카탈로그의 메타데이터를 **자동으로 생성, 갱신, 삭제**한다.
  2. **사용자 권한 제한:** 일반 사용자나 DBA는 `SELECT` 문을 통한 **조회(검색)만 가능**하다.
  3. **직접 갱신 금지:** 사용자가 `INSERT`, `UPDATE`, `DELETE` 문으로 카탈로그 테이블을 **직접 수정하는 것은 엄격히 금지**된다.

---

### 3.4. CRUD 분석 및 매트릭스 (CRUD Matrix Analysis)

- [한국어]: **CRUD 분석**은 응용 프로그램의 업무 **프로세스(Process)**와 데이터베이스의 **엔티티/테이블(Entity/Table)** 간의 상관관계를 분석하여, 시스템의 정합성을 검증하고 트랜잭션 발생 부하를 산정하는 기법이다.

| 약어 (Ký tự) | 명칭 (Thao tác) | 한글 명칭 | SQL 대응문 | 의미 및 역할 |
|:---:|---|---|:---:|---|
| **C** | **Create** | `생성` | `INSERT` | 새로운 데이터 레코드를 생성하여 테이블에 저장 |
| **R** | **Read** | `읽기` | `SELECT` | 기존에 저장된 데이터 내용을 검색 및 조회 |
| **U** | **Update** | `갱신` | `UPDATE` | 테이블에 이미 존재하는 데이터 속성값을 수정 |
| **D** | **Delete** | `삭제` | `DELETE` | 테이블에서 불필요한 데이터 레코드를 영구 삭제 |

#### CRUD 매트릭스의 핵심 활용 목적 (Mục đích ứng dụng)
1. **트랜잭션 주기별 발생 횟수 파악:** 각 프로세스가 테이블을 얼마나 자주 호출(C, R, U, D)하는지 측정하여 시스템 병목 구간을 사전 예측.
2. **데이터 용량 산정(유추):** 단위 기간당 발생하는 Create(INSERT) 횟수와 레코드 크기를 곱하여 향후 데이터베이스의 물리적 용량 증가 추세를 정확히 추정.

#### CRUD 매트릭스 품질 점검 3대 규칙 (Quy tắc kiểm định)
- **규칙 1 (엔티티 필수성):** 모든 엔티티(테이블)는 반드시 **최소 하나 이상의 `C`(Create)**와 **최소 하나 이상의 `R`(Read)**를 가져야 함.
  - `C`가 없는 테이블: 데이터가 어디서도 생성되지 않는 결함.
  - `R`가 없는 테이블: 데이터가 생성만 되고 시스템 어디에서도 쓰이지 않는 쓰레기(Dead Table).
- **규칙 2 (프로세스 필수성):** 모든 프로세스는 반드시 하나 이상의 엔티티에 대해 C, R, U, D 중 하나의 연산을 수행해야 함.
- **규칙 3 (복수 연산 우선순위):** 하나의 프로세스가 동일 엔티티에 대해 여러 연산을 동시에 수행할 경우, 일반적으로 `C > D > U > R`의 우선순위로 표기함.

---

## 4. 실전 시험 대비 / 함정 분석 (Bẫy đề thi & Trắc nghiệm)

### 함정 포인트 (Trap Points)
1. **Bẫy 인덱스 trên View:**
   - Đề bài: *"Một khung nhìn (View) sau khi được định nghĩa có thể tạo thêm các chỉ mục độc lập (Index) để tăng tốc độ tìm kiếm"* $\rightarrow$ **SAI**. View thông thường hoàn toàn **KHÔNG THỂ TẠO CHỈ MỤC ĐỘC LẬP (독립적인 인덱스를 가질 수 없음)**.
2. **Bẫy sửa đổi cấu trúc View:**
   - Khẳng định: *"Dùng lệnh ALTER VIEW để thêm cột mới cho View"* $\rightarrow$ **SAI**. Chuẩn SQL không hỗ trợ ALTER VIEW; muốn sửa đổi bắt buộc phải `DROP VIEW` rồi thực thi lại `CREATE VIEW`.
3. **Bẫy phân quyền trên 시스템 카탈로그:**
   - Đề hỏi: *"Người quản trị hệ thống (DBA) có thể dùng câu lệnh UPDATE để trực tiếp sửa đổi các bảng trong Hệ thống ca-ta-lô khi cần thiết?"* $\rightarrow$ **SAI**. Người dùng và cả DBA chỉ có quyền **SELECT tra cứu**, DBMS tự động bảo trì dữ liệu này.
4. **Bẫy bảng thiếu chữ C hoặc R trong CRUD 매트릭스:**
   - Đề hỏi: *"Trong ma trận CRUD, một bảng dữ liệu không có bất kỳ ký tự R nào ở tất cả các tiến trình thì mang ý nghĩa gì?"* $\rightarrow$ Đáp án: **Dữ liệu được lưu trữ nhưng không bao giờ được khai thác/sử dụng trong toàn bộ hệ thống**.

---

## 5. 복습 체크리스트 (Bảng kiểm tra ôn tập)

- [ ] Phân tích được 3 ưu điểm lớn của View (논리적 독립성, 보안성, 질의 단순화) và hạn chế không có Index riêng.
- [ ] So sánh 5 cấu trúc Index: B+ Tree, Bitmap (ít giá trị phân biệt), Function-Based, Bitmap Join, Domain Index.
- [ ] Phân biệt sự khác nhau giữa Clustered Index (1 cái, sắp xếp vật lý) và Non-Clustered Index (nhiều cái, dùng ROWID).
- [ ] Nhớ nguyên tắc thiết kế: bảng có nhiều thao tác INSERT/DELETE thì cần giảm thiểu số lượng Index.
- [ ] Trình bày đặc điểm của 시스템 카탈로그 (chỉ DBMS tự cập nhật, người dùng chỉ được SELECT).
- [ ] Phân tích 4 chữ cái CRUD và 2 mục đích lớn: đo tần suất phát sinh giao dịch và ước lượng dung lượng dữ liệu.
