# 12. 데이터 파티셔닝과 데이터베이스 보안·암호화 (Phân Vùng Dữ Liệu và Bảo Mật, Mã Hóa CSDL)

## 1. 개요 및 학습 목표 (Tổng quan & Mục tiêu học tập)

- [한국어]: 초대용량 데이터베이스 환경에서 I/O 병목을 해소하고 가용성을 극대화하기 위해 대형 테이블을 물리적으로 분할하는 **파티셔닝(Partitioning)** 기법을 적용한다. 아울러 데이터베이스의 기밀성과 무결성을 보호하기 위해 **접근 통제 3대 모델(DAC, MAC, RBAC)**, 보안 무결성 모델(Bell-LaPadula, Biba), 그리고 **대칭키·비대칭키 암호화(Encryption)** 알고리즘을 체계적으로 구축한다.
- [Tiếng Việt]: Trong môi trường cơ sở dữ liệu siêu lớn, để giải quyết nút thắt cổ chai I/O và tối ưu hóa tính sẵn sàng, kỹ sư áp dụng kỹ thuật **Phân vùng bảng (Partitioning / 파티셔닝)**. Đồng thời, nhằm bảo vệ tính bí mật và toàn vẹn dữ liệu, hệ thống triển khai **3 mô hình kiểm soát truy cập (DAC, MAC, RBAC)**, các mô hình an ninh kinh điển (Bell-LaPadula, Biba), và hệ thống giải thuật **Mã hóa đối xứng / Bất đối xứng (Encryption / 암호화)**.

### 학습 목표 (Mục tiêu kiến thức)
1. **파티셔닝의 개념과 5대 분할 방식 (Bản chất Phân vùng & 5 Phương pháp phân chia):** Phân biệt sâu sắc Phân vùng phạm vi (`범위 분할 / Range`), Phân vùng băm (`해시 분할 / Hash`), Phân vùng danh sách (`목록 분할 / List`), Phân vùng kết hợp (`조합 분할 / Composite`), và Phân vùng xoay vòng (`라운드 로빈 / Round Robin` - không cần Primary Key).
2. **파티션 프루닝과 운영 이점 (Cắt tỉa phân vùng & Tối ưu hóa vận hành):** Hiểu rõ cơ chế Partition Pruning chỉ quét các phân vùng mục tiêu và lợi ích xóa dữ liệu lịch sử tức thì bằng lệnh `DROP PARTITION`.
3. **접근 통제 3대 기술 (3 mô hình kiểm soát truy cập dữ liệu):** So sánh toàn diện DAC (theo chủ sở hữu), MAC (theo cấp bậc bảo mật hệ thống), và RBAC (theo vai trò chức danh).
4. **보안 모델의 규칙 대조 (Đối chiếu quy tắc mô hình an ninh kinh điển):** Phân tích mô hình Bell-LaPadula (tính bí mật: No Read Up, No Write Down) đối trọng với mô hình Biba (tính toàn vẹn: No Read Down, No Write Up).
5. **대칭키 vs 비대칭키 암호화 (Mã hóa đối xứng vs Bất đối xứng):** So sánh số lượng khóa, tốc độ, độ phức tạp quản lý khóa và các thuật toán tiêu biểu (DES, AES, SEED, ARIA vs RSA, ECC).

---

## 2. 개념 연결 및 브리지 (Cầu nối kiến thức)

- **Từ đâu (Origin - Xuất phát điểm):**
  - [한국어]: 이전 [11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md](11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md)에서 우리는 분산 환경에서의 네트워크 투명성과 물리적 노드 배치, 2단계 커밋 합의 규약을 학습했습니다.
  - [Tiếng Việt]: Ở bài học trước, chúng ta đã nắm vững kiến trúc phân tán trên mạng diện rộng với 4 tính chất trong suốt và giao thức cam kết 2 pha 2PC.
- **Đang giải quyết gì (Current Problem - Vấn đề bài học giải quyết):**
  - [한국어]: 단일 노드 내부에서 수천만 건 이상의 트랜잭션 데이터가 누적될 때 발생하는 디스크 I/O 저하를 방지하기 위해 **파티셔닝(Partitioning)** 기법을 확립하고, 악의적 침입과 비인가 접근으로부터 핵심 자산을 보호하는 **다층 보안 및 암호화 메커니즘**을 규명합니다.
  - [Tiếng Việt]: Khi dữ liệu tích lũy lên hàng chục triệu bản ghi trên một nút lưu trữ, hiệu năng đọc/ghi suy giảm nghiêm trọng và nguy cơ lộ lọt thông tin tăng cao. Bài học này giải quyết việc xé nhỏ bảng dữ liệu qua **Phân vùng (Partitioning)** và thiết lập lá chắn bảo vệ thông qua **Kiểm soát truy cập và Mã hóa CSDL**.
- **Dùng đi đâu (Forward Handoff - Chuyển tiếp tương lai):**
  - [한국어]: 본 장에서 완성된 물리적 저장 파티션 및 보안 통제 체계는 다음 [13-chuyen-doi-du-lieu-etl-data-warehouse-va-big-data.md](13-chuyen-doi-du-lieu-etl-data-warehouse-va-big-data.md)에서 대규모 분석 처리를 위한 ETL 데이터 정제 파이프라인 및 데이터 웨어하우스(DW/OLAP), 빅데이터 분산 저장소로 연계됩니다.
  - [Tiếng Việt]: Các phân vùng dữ liệu và chuẩn mã hóa này sẽ là đầu vào để xây dựng các đường ống chuyển đổi ETL, kho dữ liệu lớn Data Warehouse / OLAP và hệ sinh thái Big Data ở bài học tiếp theo.

---

## 3. 핵심 이론 및 용어 대조 (Lý thuyết cốt lõi & Đối chiếu thuật ngữ)

### 3.1. 파티셔닝의 개념과 5대 분할 방식 (Bản chất Phân vùng & 5 Phương pháp)

- [한국어]: **파티셔닝(Partitioning)**은 대용량의 테이블이나 인덱스를 작은 논리적 단위인 파티션(Partition)으로 나누어 관리하는 기법이다. 물리적으로는 별도의 데이터 파일에 분산 저장되지만, 사용자 및 응용 프로그램 관점에서는 하나의 테이블로 인식된다.
- [Tiếng Việt]: **Phân vùng (Partitioning)** là kỹ thuật phân chia các bảng hoặc chỉ mục có dung lượng cực lớn thành các đơn vị quản lý nhỏ hơn gọi là Phân vùng. Về mặt vật lý chúng được lưu trên các tệp dữ liệu độc lập, nhưng đối với ứng dụng và người dùng, chúng vẫn là một bảng thống nhất.

| 파티셔닝 방식 (Phương pháp) | 영문 / 한글 명칭 | 분할 기준 및 메커니즘 (Cơ chế phân chia) | 시험 핵심 포인트 및 적용 사례 |
|---|---|---|---|
| **범위 분할** | **Range Partitioning**<br>`범위 분할` | 지정한 열의 **연속적인 값의 범위(Range)**를 기준으로 분할 | • **날짜(일별, 월별, 분기별)** 기준 분할에 가장 보편적.<br>• 최신 데이터 분할에 트랜잭션이 집중되는 편향 위험 존재. |
| **해시 분할** | **Hash Partitioning**<br>`해시 분할` | 지정한 열의 값에 **해시 함수(Hash Function)**를 적용하여 균등 분할 | • 특정 범위에 데이터가 쏠리는 현상 완화.<br>• **고객번호, 주민등록번호** 등 균일한 분포를 가진 컬럼에 최적.<br>• 특정 데이터의 저장 위치 예측 불가. |
| **목록 분할** | **List Partitioning**<br>`목록 분할` | 관리자가 사전에 명시적으로 정의한 **불연속적이고 고유한 값의 목록** 기준 | • **지역명(서울, 부산), 국가명(한국, 미국)** 등 명확히 구분되는 범주형 코드 분할에 적용. |
| **조합 분할** | **Composite Partitioning**<br>`조합 분할` | 2단계 결합 분할: **1차로 범위 분할(Range) 후, 2차로 해시 분할(Hash)** 적용 | • 단일 범위 분할만으로는 여전히 크기가 너무 큰 초대형 테이블에 적용 (예: 월별 분할 후 고객ID 해시 분할). |
| **라운드 로빈 분할** | **Round Robin Partitioning**<br>`라운드 로빈 분할` | 레코드가 입력되는 순서대로 각 파티션에 균등하게 순환 분배 | • **기본키(Primary Key)가 전혀 필요 없음**.<br>• 데이터 균등 분배에는 최상이나, 특정 키 기반 검색 최적화에는 불리. |

- **파티션 프루닝 (Partition Pruning - Cắt tỉa phân vùng):**
  - [한국어]: SQL 쿼리의 `WHERE` 절 조건에 해당하는 파티션만 선별적으로 접근하고, 관련 없는 파티션은 아예 디스크 I/O 대상에서 제외하여 검색 속도를 극대화하는 옵티마이저 최적화 기법.
  - [Tiếng Việt]: Cơ chế của Optimizer chỉ quét đúng các phân vùng thỏa mãn điều kiện `WHERE` và bỏ qua hoàn toàn các phân vùng còn lại, giúp tiết kiệm đến 90% chi phí I/O đĩa cứng.

---

### 3.2. 데이터베이스 접근 통제 3대 기술 (DAC vs MAC vs RBAC)

- [한국어]: **접근 통제(Access Control)**는 비인가된 사용자가 데이터베이스의 자원에 불법적으로 접근하거나 파괴하는 것을 통제하는 보안 메커니즘이다.

| 모델 (Mô hình) | 영문 / 한글 명칭 | 권한 부여 주체 (Tiêu chí trao quyền) | 기술적 특성 및 제어 방식 |
|---|---|---|---|
| **DAC** | **Discretionary Access Control**<br>`임의 접근통제` | **데이터 소유자 (Data Owner)** | • 데이터 객체를 생성한 소유자가 타인에게 임의로 권한 부여 및 회수.<br>• SQL 표준인 **`GRANT` / `REVOKE`** 구문이 대표적.<br>• 구현이 용이하나 트로이 목마 등 악성 코드에 취약. |
| **MAC** | **Mandatory Access Control**<br>`강제 접근통제` | **시스템 관리자 및 보안 등급(레이블)** | • 주체의 인가 등급(Clearance)과 객체의 보안 등급(Classification: 극비, 비밀, 대외비, 일반)을 비교하여 시스템이 강제 통제.<br>• 소유자라 할지라도 임의로 권한을 이전할 수 없음.<br>• 군사 및 국가 정보 기관에서 필수 적용. |
| **RBAC** | **Role-Based Access Control**<br>`역할기반 접근통제` | **사용자의 역할 (Role) 및 직책** | • 개별 사용자가 아닌 **조직의 역할(직책, 직무)**에 권한을 할당하고, 사용자를 해당 역할에 배속시키는 방식.<br>• 인사 이동 시 역할만 변경하면 되므로 관리가 극히 효율적.<br>• 일반 기업 및 금융 시스템에서 널리 활용. |

---

### 3.3. 정형 보안 모델 비교 (Bell-LaPadula vs Biba)

- [한국어]: MAC(강제 접근통제)을 수학적·논리적으로 정형화한 대표적 보안 모델이다.

```
[ Bell-LaPadula (BLP) 모델 ]                     [ Biba (비바) 모델 ]
  • 핵심 목표: 기밀성 (Confidentiality)             • 핵심 목표: 무결성 (Integrity)
  • No Read Up   (NRU: 상위 등급 읽기 금지)        • No Read Down (NRD: 하위 등급 읽기 금지)
  • No Write Down (NWD: 하위 등급 쓰기 금지)       • No Write Up   (NWU: 상위 등급 쓰기 금지)
```

| 비교 항목 (Tiêu chí) | 벨-라파듈라 모델 (Bell-LaPadula / BLP) | 비바 모델 (Biba Model) |
|---|---|---|
| **최우선 보장 목표** | **기밀성 (Confidentiality / `기밀성`)** | **무결성 (Integrity / `무결성`)** |
| **읽기 규칙 (Read)** | **단순 보안 규칙 (No Read Up - NRU)**<br>주체는 자신보다 높은 보안 등급의 문서를 읽을 수 없음. | **단순 무결성 규칙 (No Read Down - NRD)**<br>주체는 자신보다 낮은 무결성 등급의 문서를 읽을 수 없음. |
| **쓰기 규칙 (Write)** | **스타 특성 규칙 (*-Property / No Write Down - NWD)**<br>주체는 자신보다 낮은 보안 등급의 문서에 쓸 수 없음. (정보 누설 차단) | **스타 무결성 규칙 (*-Property / No Write Up - NWU)**<br>주체는 자신보다 높은 무결성 등급의 문서를 수정할 수 없음. (오염 방지) |

- **기타 주요 보안 모델:**
  - **클락-윌슨 모델 (Clark-Wilson):** 상업적 환경의 무결성 보장 모델로, 데이터 변조를 막기 위해 반드시 인증된 프로그램(잘 정의된 트랜잭션)을 통해서만 데이터에 접근하도록 강제.
  - **차이니즈 월 모델 (Chinese Wall / Brewer-Nash):** 금융 및 회계 법인 등에서 발생할 수 있는 **이해 충돌(Conflict of Interest)**을 사전에 원천 차단하기 위해 이전 접근 기록에 따라 접근을 동적으로 제한.

---

### 3.4. 데이터베이스 암호화 (대칭키 vs 비대칭키)

- [한국어]: **암호화(Encryption)**는 평문(Plaintext)을 정당한 권한이 없는 자가 판독할 수 없도록 암호문(Ciphertext)으로 변환하는 과정이며, **복호화(Decryption)**는 이를 원문으로 되돌리는 과정이다.

| 구분 (Tiêu chí) | 개인키 / 대칭키 암호 (Symmetric Key) | 공개키 / 비대칭키 암호 (Asymmetric Key) |
|---|---|---|
| **키 구조** | **암호화 키 = 복호화 키** (동일한 단일 비밀키 사용) | **암호화 키 $\neq$ 복호화 키** (한 쌍의 공개키와 개인키 사용) |
| **암호화/복호화 방식** | 공개키로 암호화 불가, 양측이 비밀키 공유 | 누구나 아는 **공개키로 암호화**, 자신만의 **비밀키로 복호화** |
| **연산 속도** | **매우 빠름** (대용량 데이터 암호화에 필수적) | **느림** (복잡한 수학적 모듈러 연산 소요) |
| **필요 키 개수** | $N$명 간 통신 시 $\mathbf{\frac{N(N-1)}{2}}$개의 키 필요 | $N$명 간 통신 시 $\mathbf{2N}$개의 키만 필요 |
| **키 관리/분배** | 키 분배 및 관리가 매우 까다로움 | 키 분배가 극히 안전하고 용이함 |
| **대표 알고리즘** | • **블록 암호:** DES, 3DES, AES, **SEED (한국)**, **ARIA (한국)**<br>• **스트림 암호:** RC4 | • **소인수분해 기반:** RSA<br>• **이산대수 기반:** DSA, Diffie-Hellman<br>• **타원곡선 기반:** ECC |

---

## 4. 실전 시험 대비 / 함정 분석 (Bẫy đề thi & Trắc nghiệm)

### 함정 포인트 (Trap Points)
1. **Bẫy 라운드 로빈 분할 (Round Robin Partitioning):**
   - Đề bài: *"Phương pháp phân vùng dữ liệu nào không đòi hỏi phải có Khóa chính (Primary Key) và phân bổ đều đặn tuần tự các bản ghi?"* $\rightarrow$ Đáp án: **라운드 로빈 분할 (Round Robin Partitioning)**.
2. **Bẫy Bell-LaPadula vs Biba:**
   - Đề hỏi: *"Mô hình bảo mật nào áp dụng nguyên tắc No Read Down (NRD) và No Write Up (NWU) nhằm bảo vệ tính toàn vẹn (무결성)?"* $\rightarrow$ Đáp án: **비바 모델 (Biba Model)**. Rất nhiều thí sinh nhầm với Bell-LaPadula.
   - Nhớ câu thần chú: **Bell-LaPadula = Bí mật (기밀성)**; **Biba = Toàn vẹn (무결성)**.
3. **Bẫy thuật toán mã hóa của Hàn Quốc:**
   - Trong các đề thi Kỹ sư xử lý thông tin, các thuật toán mã hóa đối xứng do Hàn Quốc phát triển như **SEED (KISA 개발)** và **ARIA (국가정보원 개발)** thường xuyên xuất hiện $\rightarrow$ Cả hai đều thuộc nhóm **대칭키 블록 암호 (Mã hóa khối đối xứng)**.
4. **Bẫy DAC vs MAC:**
   - Đề hỏi: *"Hệ thống kiểm soát truy cập trong đó chủ sở hữu dữ liệu có toàn quyền quyết định cấp quyền truy cập bằng lệnh GRANT là gì?"* $\rightarrow$ Đáp án: **DAC (임의 접근통제)**.

---

## 5. 복습 체크리스트 (Bảng kiểm tra ôn tập)

- [ ] Phân biệt rõ 5 loại 파티션: 범위(Range), 해시(Hash), 목록(List), 조합(Composite), 라운드 로빈(Round Robin).
- [ ] Nhớ kỹ 라운드 로빈 분할 không cần 기본키 (Primary Key).
- [ ] Trình bày được khái niệm 파티션 프루닝 (Partition Pruning).
- [ ] So sánh 3 mô hình 접근 통제: DAC (chủ sở hữu), MAC (cấp bậc bảo mật), RBAC (vai trò chức vụ).
- [ ] Thuộc lòng quy tắc No Read Up / No Write Down của 벨-라파듈라 (기밀성) và No Read Down / No Write Up của 비바 (무결성).
- [ ] So sánh 대칭키 và 비대칭키 về tốc độ, số lượng khóa và kể tên thuật toán tiêu biểu (SEED, ARIA, AES vs RSA, ECC).
