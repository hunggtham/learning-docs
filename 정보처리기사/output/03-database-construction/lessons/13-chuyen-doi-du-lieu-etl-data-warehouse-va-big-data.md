# 13. 데이터 전환(ETL), 데이터 웨어하우스와 빅데이터 (Chuyển Đổi Dữ Liệu ETL, Data Warehouse và Big Data)

## 1. 개요 및 학습 목표 (Tổng quan & Mục tiêu học tập)

- [한국어]: 기업의 다양한 레거시 시스템으로부터 대규모 데이터를 추출, 정제, 변환하여 통합 저장소로 이관하는 **데이터 전환(ETL: Extraction, Transformation, Load)** 프로세스는 현대 비즈니스 인텔리전스의 출발점이다. 축적된 데이터는 다차원 분석을 지원하는 **데이터 웨어하우스(Data Warehouse / OLAP)**로 구축되며, 나아가 대규모 비정형 데이터를 분산 처리하는 **빅데이터(Big Data) 및 NoSQL 생태계**, 애플리케이션 연동을 위한 **SQL Mapper(MyBatis)와 ORM(JPA)**으로 확장된다.
- [Tiếng Việt]: Quy trình **Chuyển đổi dữ liệu (ETL / 데이터 전환: Trích xuất, Biến đổi, Nạp)** từ các hệ thống kế thừa (Legacy) về kho lưu trữ tập trung là điểm khởi đầu cho trí tuệ doanh nghiệp (BI). Dữ liệu sau khi làm sạch được nạp vào **Kho dữ liệu (Data Warehouse / OLAP)** nhằm phục vụ phân tích đa chiều, đồng thời mở rộng sang hệ sinh thái **Dữ liệu lớn (Big Data), NoSQL**, và các khung làm việc kết nối ứng dụng như **SQL Mapper (MyBatis)** và **ORM (JPA)**.

### 학습 목표 (Mục tiêu kiến thức)
1. **파일 구조와 전통적 파일 시스템 (Cấu trúc tệp truyền thống):** Nắm vững Tệp tuần tự (`순차 파일 / SAM`), Tệp tuần tự có chỉ mục (`색인 순차 파일 / ISAM` - 3 vùng: Prime, Index, Overflow), và Tệp trực tiếp (`직접 파일 / DAM`). Phân biệt ACL (gắn vào tệp) và Capability List (gắn vào người dùng).
2. **데이터 전환 및 ETL 3단계 (Quy trình chuyển đổi ETL):** Phân tích sâu 3 bước Extraction (`추출`), Transformation (`변환` - làm sạch dữ liệu), và Loading (`적재`); nắm vững vòng đời 5 trạng thái quản lý lỗi dữ liệu (Open, Assigned, Fixed, Closed, Deferred).
3. **데이터 웨어하우스 4대 특성과 OLAP 5대 연산 (Đặc tính Data Warehouse & 5 Thao tác OLAP):** Thuộc lòng 4 đặc tính Inmon (Chủ đề, Tích hợp, Chuỗi thời gian, Phi bốc hơi); phân biệt Roll-up, Drill-down, Slicing, Dicing, Pivoting; so sánh Star Schema và Snowflake Schema.
4. **빅데이터와 NoSQL 데이터베이스 4대 모델 (Big Data & 4 Dòng NoSQL):** Nắm vững đặc trưng 3V/5V của Big Data, phân biệt Key-Value (Redis), Document (MongoDB), Column-family (HBase, Cassandra), và Graph (Neo4j).
5. **SQL Mapper vs ORM 및 연산자 우선순위 (MyBatis vs ORM & Độ ưu tiên toán tử):** Phân biệt bản chất SQL Mapper (MyBatis - tự viết SQL trong XML) và ORM (JPA - tự sinh SQL); thuộc lòng thứ tự toán tử: `( )` > Toán học > Quan hệ > Logic (`NOT > AND > OR`).

---

## 2. 개념 연결 및 브리지 (Cầu nối kiến thức)

- **Từ đâu (Origin - Xuất phát điểm):**
  - [한국어]: 이전 [12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md](12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md)에서 우리는 초대용량 테이블의 파티셔닝 기법과 다층 접근 통제, 암호화 체계를 구축했습니다.
  - [Tiếng Việt]: Ở bài học trước, chúng ta đã nắm vững các kỹ thuật phân vùng bảng lớn cùng các mô hình kiểm soát truy cập và thuật toán mã hóa dữ liệu.
- **Đang giải quyết gì (Current Problem - Vấn đề bài học giải quyết):**
  - [한국어]: 본 장에서는 운영계 트랜잭션 시스템(OLTP)에 축적된 이종(Heterogeneous)의 원시 데이터를 정제하여 정보계 분석 시스템(OLAP)으로 통합하는 **ETL 파이프라인**을 설계하고, 대규모 분산 빅데이터 및 NoSQL 환경과 애플리케이션 영속성 프레임워크를 종합 완성합니다.
  - [Tiếng Việt]: Bài học này giải quyết việc trích xuất và chuẩn hóa dữ liệu từ các hệ thống vận hành giao dịch (OLTP) phân mảnh để nạp vào hệ thống phân tích báo cáo (OLAP), đồng thời tổng kết hệ sinh thái Big Data, NoSQL và cầu nối lập trình ứng dụng (MyBatis, ORM).
- **Dùng đi đâu (Forward Handoff - Chuyển tiếp tương lai):**
  - [한국어]: 본 장을 끝으로 제3과목 [데이터베이스 구축]의 13개 핵심 마스터 단원이 완결되며, 여기서 확립된 연산자 우선순위와 데이터 조작 로직은 제4과목 [프로그래밍 언어 활용](../../04-programming-language/README.md)의 C, Java, Python 알고리즘 및 데이터 구조 구현으로 이어집니다.
  - [Tiếng Việt]: Bài học này khép lại toàn bộ 13 bài học master của Môn 3: Xây dựng Cơ sở dữ liệu. Toàn bộ logic thao tác dữ liệu và thứ tự ưu tiên toán tử này sẽ làm nền tảng trực tiếp để bước sang Môn 4: Lập trình ứng dụng (C, Java, Python).

---

## 3. 핵심 이론 및 용어 대조 (Lý thuyết cốt lõi & Đối chiếu thuật ngữ)

### 3.1. 전통적 파일 시스템 구조 (Cấu trúc Tệp & Hệ thống tệp)

- [한국어]: DBMS 도입 이전에 OS 레벨에서 데이터를 파일 단위로 저장하던 고전적 구조로서, 오늘날 스토리지 내부 엔진 설계의 기초가 된다.

| 파일 구조 (Cấu trúc Tệp) | 영문 / 한글 명칭 | 저장 및 접근 메커니즘 (Cơ chế truy cập) | 장단점 및 특징 |
|---|---|---|---|
| **순차 파일** | **Sequential File**<br>`순차 파일 (SAM)` | 레코드의 논리적 순서대로 물리적 연속 공간(자기 테이프 등)에 차례로 저장 | • 순차 처리 시 속도 우수, 공간 낭비 없음.<br>• 특정 레코드 검색(Random Access) 극히 비효율적. |
| **색인 순차 파일** | **Indexed Sequential File**<br>`색인 순차 파일 (ISAM)` | 레코드를 순차 저장하면서 별도의 **색인(Index)**을 두어 순차 및 직접 접근 모두 지원 | • **3대 구역(Prime, Index, Overflow)으로 구성**.<br>• 삽입/삭제 시 오버플로 구역 관리 부하 발생. |
| **직접 파일** | **Direct File**<br>`직접 파일 (DAM)` | **해시 함수(Hash Function)**를 사용하여 레코드의 키로부터 물리적 디스크 주소를 직접 산출 | • 임의 접근 속도 최고속.<br>• 충돌(Collision) 해결 알고리즘 필요, 범위 검색 곤란. |

#### ISAM 파일의 3대 구역 (3 Vùng cấu trúc của tệp ISAM)
1. **기본 구역 (Prime Area):** 실제 데이터 레코드가 키 순서대로 정렬되어 저장되는 메인 물리 공간.
2. **색인 구역 (Index Area):** 빠른 검색을 위한 다단계 인덱스 공간 (`Track Index` $\rightarrow$ `Cylinder Index` $\rightarrow$ `Master Index`).
3. **오버플로 구역 (Overflow Area):** 새 레코드 삽입으로 Prime Area의 트랙이 꽉 찼을 때 튕겨 나온 레코드를 임시 보관하는 공간 (`Cylinder Overflow` 및 `Independent Overflow`).

- **파일 접근 제어 (ACL vs Capability List):**
  - **접근 제어 리스트 (ACL / Access Control List):** **객체(파일) 중심**으로 어떤 사용자가 어떤 권한을 가지는지 명시 (파일에 권한 목록 부착).
  - **권한 리스트 (Capability List):** **주체(사용자) 중심**으로 해당 사용자가 어떤 객체들에 접근할 수 있는지 명시 (사용자가 출입증을 소지).

---

### 3.2. 데이터 전환 및 ETL 3단계 (Data Migration & ETL)

- [한국어]: **데이터 전환(Data Migration)**은 레거시 시스템의 원시 데이터를 추출(Extraction)하여 대상 시스템에 적합하도록 정제 및 변환(Transformation)한 후, 신규 데이터베이스에 적재(Loading)하는 전 과정이다.

```
[ 소스 레거시 시스템 ] ──(추출: Extraction)──> [ 스테이징 영역 ] ──(변환: Transformation)──> [ 적재: Loading ] ──> [ 데이터 웨어하우스 ]
(RDBMS, CSV, Log)                            (Data Cleansing, 표준화)                      (신규 대상 DB)
```

| ETL 단계 | 영문 / 한글 명칭 | 주요 기술 작업 (Công việc kỹ thuật chính) |
|:---:|---|---|
| **E** | **Extraction**<br>`추출` | 다양한 원천 시스템(이종 RDBMS, 웹 로그, ERP, Excel, XML)으로부터 필요한 데이터를 안전하게 선별 추출. |
| **T** | **Transformation**<br>`변환` | **데이터 정제(Data Cleansing)**: 결측치(NULL) 보정, 이상치 제거, 형식 통일(날짜, 전화번호 포맷), 중복 제거, 코드 매핑, 비즈니스 규칙 검증. |
| **L** | **Loading**<br>`적재` | 변환 및 검증이 완료된 정제 데이터를 대상 데이터베이스 테이블 또는 DW 팩트/디멘션 테이블에 일괄 적재(Batch Load). |

- **오류 데이터 정제 5대 상태 주기 (Vòng đời quản lý lỗi dữ liệu):**
  $$\mathbf{Open\ (오류\ 감지)} \longrightarrow \mathbf{Assigned\ (담당자\ 배정)} \longrightarrow \mathbf{Fixed\ (수정\ 완료)} \longrightarrow \mathbf{Closed\ (검증\ 종료)}$$
  - **Deferred (조치 연기):** 당장 수정하기 어렵거나 우선순위가 낮아 차기 릴리스로 보류한 상태.

---

### 3.3. 데이터 웨어하우스와 OLAP 분석 (Data Warehouse & OLAP)

- [한국어]: **데이터 웨어하우스(Data Warehouse / DW)**는 의사결정 지원을 위해 기업 내의 다양한 운영계 데이터베이스로부터 추출, 정제, 통합된 다차원 데이터베이스이다. (W.H. Inmon 정의)

| 4대 특성 (4 Đặc tính Inmon) | 영문 / 한글 명칭 | 기술적 의미 (Ý nghĩa kỹ thuật) |
|---|---|---|
| **주제 지향성** | **Subject-Oriented**<br>`주제 지향성` | 일상적 업무 프로세스가 아닌 특정 **주제(고객, 상품, 매출 등)**를 중심으로 데이터를 구조화함. |
| **통합성** | **Integrated**<br>`통합성` | 서로 다른 운영 시스템의 불일치하는 코드, 단위, 명칭을 일관된 표준 형식으로 통일하여 저장. |
| **시계열성** | **Time-Variant**<br>`시계열성` | 현재 상태뿐만 아니라 과거 수년 치의 역사적(Historical) 데이터 추세를 시점별로 누적 보관. |
| **비휘발성** | **Non-Volatile**<br>`비휘발성` | 적재가 완료된 데이터는 갱신(Update)이나 삭제(Delete)되지 않고 **오직 읽기 전용(Read-only)**으로 조회 분석됨. |

#### OLAP (Online Analytical Processing) 5대 다차원 연산

| 연산 (Thao tác) | 한글 명칭 | 기술적 동작 (Động tác phân tích) | 비유 및 예시 |
|---|---|---|---|
| **Roll-up** | `롤업` | 상세 분석 데이터로부터 상위 차원의 요약 데이터로 단계적 집계 | 일별 매출 $\rightarrow$ 월별 매출 $\rightarrow$ 연도별 매출로 올라감 |
| **Drill-down** | `드릴다운` | 요약 데이터로부터 보다 구체적이고 상세한 하위 데이터로 파고듦 | 연도별 매출 $\rightarrow$ 분기별 $\rightarrow$ 매장별 상세 내역으로 내려감 |
| **Slicing** | `슬라이싱` | 다차원 큐브에서 특정 차원의 단일 단면(2차원 조각)을 잘라내어 분석 | 전체 다차원 큐브에서 '2025년도' 단면만 잘라내어 조회 |
| **Dicing** | `다이싱` | 다차원 큐브에서 여러 차원의 작은 하위 큐브(작은 주전자 조각)를 추출 | '2025년 + 서울지역 + 전자제품'의 하위 큐브 선택 |
| **Pivoting** | `피보팅` | 보고서의 행과 열의 축을 서로 맞바꾸어 새로운 관점으로 데이터를 투영 | 가로축(시간), 세로축(지역)을 서로 맞바꿔 표시 |

---

### 3.4. 빅데이터와 NoSQL 데이터베이스 (Big Data & NoSQL)

- **빅데이터의 3V / 5V:**
  - **Volume (규모):** 테라바이트(TB), 페타바이트(PB) 이상의 방대한 데이터양.
  - **Velocity (속도):** 실시간 센서 스트리밍, 클릭스트림 등 데이터의 초고속 생성 및 처리 속도.
  - **Variety (다양성):** 정형(RDBMS)뿐만 아니라 반정형(JSON, XML), 비정형(동영상, 음성, 텍스트) 데이터의 혼재.
  - (+ **Veracity - 정확성**, **Value - 가치**).
- **NoSQL 데이터베이스의 4대 분류 체계:**
  1. **Key-Value Store (키-값):** 가장 단순한 구조, 고속 읽기/쓰기 (예: **Redis**, Memcached).
  2. **Document Store (문서형):** JSON, BSON 포맷으로 복잡한 계층형 문서 저장 (예: **MongoDB**, CouchDB).
  3. **Column-family Store (컬럼 패밀리):** 행마다 서로 다른 컬럼 구성을 지원하는 대규모 분산 저장소 (예: **HBase**, **Cassandra**).
  4. **Graph Store (그래프):** 노드(Node)와 간선(Edge)으로 관계를 직접 모델링 (예: **Neo4j**).

---

### 3.5. 영속성 프레임워크와 SQL 연산자 우선순위 (MyBatis vs ORM)

| 비교 항목 (Tiêu chí) | SQL 매퍼 (SQL Mapper: MyBatis) | ORM (Object-Relational Mapping: JPA, Hibernate) |
|---|---|---|
| **패러다임** | **SQL 중심** (SQL-centric) | **객체 중심** (Object-oriented) |
| **매핑 방식** | 자바 메서드와 **수동 작성한 SQL 문(XML)**을 매핑 | 자바 객체(Entity Class)와 **DB 테이블**을 1:1 자동 매핑 |
| **쿼리 제어력** | 개발자가 복잡한 SQL 튜닝 및 인덱스 힌트를 직접 제어 가능 | 프레임워크가 SQL을 자동 생성 (복잡한 조인은 JPQL/QueryDSL 필요) |
| **최적 적용** | 레거시 DB가 복잡하거나 성능 튜닝이 핵심인 프로젝트 | 도메인 모델이 복잡하고 CRUD 반복이 많은 신규 웹 서비스 |

#### SQL 연산자 우선순위 (Operator Precedence)
- [한국어]: SQL 엔진이 식을 평가할 때 적용되는 엄격한 우선순위 규칙이다:
  1. **괄호 `( )`**: 최우선 연산.
  2. **산술 연산자**: 곱셈·나눗셈(`*`, `/`) $\rightarrow$ 덧셈·뺄셈(`+`, `-`).
  3. **문자열 연결**: `||` (또는 `+`).
  4. **비교·관계 연산자**: `=`, `<>`, `<`, `>`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`.
  5. **논리 연산자 NOT**: 논리 부정 (논리 연산자 중 가장 높음).
  6. **논리 연산자 AND**: 논리곱 (OR보다 항상 먼저 평가됨).
  7. **논리 연산자 OR**: 논리합 (가장 마지막에 평가됨).

---

## 4. 실전 시험 대비 / 함정 분석 (Bẫy đề thi & Trắc nghiệm)

### 함정 포인트 (Trap Points)
1. **Bẫy 연산자 우선순위 (NOT > AND > OR):**
   - Đề cho biểu thức: `WHERE Status = 'A' OR Age >= 30 AND City = 'Seoul'`.
   - Nhiều thí sinh tưởng chạy từ trái qua phải, nhưng thực tế DBMS chạy: `(Age >= 30 AND City = 'Seoul')` trước, sau đó mới tính đến `Status = 'A' OR (...)`.
2. **Bẫy 4대 특성 데이터 웨어하우스 (Inmon 4대 특성):**
   - Đề bài: *"Dữ liệu trong Data Warehouse thường xuyên được cập nhật (Update) và xóa (Delete) theo thời gian thực để duy trì tính tươi mới"* $\rightarrow$ **SAI**. Đặc tính của DW là **비휘발성 (Non-Volatile)**, dữ liệu chỉ nạp vào và đọc phân tích (Read-only), không bao giờ cập nhật tùy tiện.
3. **Bẫy ISAM 3대 구역:**
   - Đề hỏi: *"Vùng lưu trữ các bản ghi bị tràn khi Prime Area bị đầy được gọi là gì?"* $\rightarrow$ Đáp án: **오버플로 구역 (Overflow Area)**.
4. **Bẫy OLAP 연산 (Roll-up vs Drill-down):**
   - Từ phân tích chi tiết chuyển lên mức tổng hợp cao hơn $\rightarrow$ **Roll-up (롤업)**.
   - Từ mức tổng hợp đi sâu xuống chi tiết cụ thể $\rightarrow$ **Drill-down (드릴다운)**.
   - Cắt một lát 2 chiều từ khối đa chiều $\rightarrow$ **Slicing (슬라이싱)**.
   - Cắt một khối lập phương con nhỏ $\rightarrow$ **Dicing (다이싱)**.

---

## 5. 복습 체크리스트 (Bảng kiểm tra ôn tập)

- [ ] Phân biệt 3 cấu trúc tệp: SAM (tuần tự), ISAM (3 vùng: Prime, Index, Overflow), DAM (hàm băm).
- [ ] Phân biệt ACL (gắn vào tệp) và Capability List (gắn vào người dùng).
- [ ] Trình bày 3 bước ETL (추출, 변환, 적재) và vòng đời lỗi (Open $\rightarrow$ Assigned $\rightarrow$ Fixed $\rightarrow$ Closed).
- [ ] Thuộc lòng 4 đặc tính Data Warehouse: 주제 지향성, 통합성, 시계열성, 비휘발성.
- [ ] Phân biệt 5 thao tác OLAP: Roll-up, Drill-down, Slicing, Dicing, Pivoting.
- [ ] Phân biệt 4 dòng NoSQL: Key-Value, Document, Column-family, Graph.
- [ ] So sánh MyBatis (SQL Mapper, XML) và JPA (ORM, Class-Table mapping).
- [ ] Thuộc lòng thứ tự ưu tiên toán tử: `( )` > Toán học > Quan hệ > NOT > AND > OR.
