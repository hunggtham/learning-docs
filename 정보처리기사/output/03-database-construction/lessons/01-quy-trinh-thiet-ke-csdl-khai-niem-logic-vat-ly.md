# 데이터베이스 설계 단계 (Quy trình thiết kế CSDL: Khái niệm, Logic và Vật lý)

## 학습 목표 (Mục tiêu)
- Nắm vững trình tự 5 giai đoạn thiết kế CSDL: Phân tích yêu cầu, Thiết kế khái niệm, Thiết kế logic, Thiết kế vật lý, Cài đặt.
- Phân biệt sản phẩm đầu ra và tính độc lập công nghệ/DBMS ở từng giai đoạn (Khái niệm độc lập DBMS; Logic phụ thuộc mô hình RDBMS; Vật lý phụ thuộc DBMS và phần cứng).
- Nắm vững 3 thành phần của mô hình dữ liệu (Cấu trúc, Thao tác, Ràng buộc) và 3 tiêu chí đánh giá thiết kế vật lý (Thời gian phản hồi, Không gian lưu trữ, Thông lượng).
- Nhận diện chính xác các bẫy trắc nghiệm kinh điển về vị trí của Chuẩn hóa (정규화 ở Thiết kế Logic) và thời điểm dùng câu lệnh DDL (Cài đặt 구현).

## 핵심 키워드 (Từ khóa)
- 데이터베이스 설계 (Thiết kế CSDL / Database Design)
- 요구 조건 분석 (Phân tích yêu cầu / Requirements Analysis / 요구 조건 명세서)
- 개념적 설계 (Thiết kế khái niệm / Conceptual Design / E-R 다이어그램 / DBMS 독립적)
- 논리적 설계 (Thiết kế logic / Logical Design / 테이블 매핑 / 정규화)
- 물리적 설계 (Thiết kế vật lý / Physical Design / 저장 레코드 / 클러스터링 / 인덱스)
- 구현 (Cài đặt / Implementation / DDL / CREATE TABLE)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Người học bắt đầu từ những yêu cầu nghiệp vụ sơ khai, phi cấu trúc của doanh nghiệp hoặc người dùng cuối (`요구 조건 명세서`).
- **Đang giải quyết gì (Current Problem):** Phân chia quá trình biến đổi dữ liệu thành các tầng độc lập để kiểm soát độ phức tạp: thiết kế khái niệm vẽ mô hình thực thể mà chưa cần biết sẽ dùng Oracle hay MySQL; thiết kế logic tạo bảng và triệt tiêu dư thừa dữ liệu (chuẩn hóa); thiết kế vật lý tối ưu hóa thời gian đáp ứng và lưu trữ trên ổ đĩa.
- **Dùng đi đâu (Forward Handoff):** Sau khi có toàn cảnh quy trình, [02-mo-hinh-du-lieu-va-bieu-do-erd.md](02-mo-hinh-du-lieu-va-bieu-do-erd.md) sẽ đi sâu vào kỹ thuật mô hình hóa dữ liệu và biểu đồ E-R chi tiết.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng câu thần chú "Yêu - Khái - Lo - Vật - Cài" và các bẫy trắc nghiệm điểm thi hay gài bẫy nhất.
- Đọc TẦNG B để nắm vững chi tiết 5 giai đoạn, các sản phẩm bàn giao, 3 thành phần mô hình dữ liệu và các tiêu chí tối ưu hóa lưu trữ đĩa.

---

## 데이터베이스 설계 단계

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Trình tự 5 giai đoạn thiết kế CSDL (데이터베이스 설계 5단계 순서)

Trong kỳ thi 정보처리기사, trình tự 5 giai đoạn thiết kế CSDL là câu hỏi cốt lõi xuất hiện liên tục trong đề thi:

$$\text{요구 조건 분석} \longrightarrow \text{개념적 설계} \longrightarrow \text{논리적 설계} \longrightarrow \text{물리적 설계} \longrightarrow \text{구현}$$

```
[1. 요구 조건 분석] ──> [2. 개념적 설계] ──> [3. 논리적 설계] ──> [4. 물리적 설계] ──> [5. 구현]
  (Phân tích yêu cầu)    (Thiết kế khái niệm)   (Thiết kế logic)     (Thiết kế vật lý)     (Cài đặt DDL)
  - Khảo sát người dùng   - Sơ đồ E-R          - Ánh xạ sang Bảng   - Định dạng Record    - Lệnh DDL
  - Bản đặc tả yêu cầu   - Transaction model  - Chuẩn hóa (정규화)  - Index / Clustering  - Tạo DB thật
```

#### 2. Bảng đối chiếu 5 giai đoạn thiết kế CSDL

| Giai đoạn (단계) | Nhiệm vụ trọng tâm (핵심 과업) | Sản phẩm đầu ra (산출물) | Tính độc lập kỹ thuật (기술 독립성) |
| :--- | :--- | :--- | :--- |
| **1. 요구 조건 분석** (Phân tích yêu cầu) | Phỏng vấn, khảo sát người dùng, phân tích quy trình nghiệp vụ | `요구 조건 명세서` (Bản đặc tả yêu cầu) | Độc lập hoàn toàn với công nghệ |
| **2. 개념적 설계** (Thiết kế khái niệm) | Trừu tượng hóa thế giới thực, mô hình hóa thực thể và giao dịch | `개념 스키마` (Biểu đồ E-R 다이어그램) | **DBMS 독립적** (Độc lập hoàn toàn với DBMS) |
| **3. 논리적 설계** (Thiết kế logic) | Ánh xạ E-R sang bảng quan hệ, thực hiện chuẩn hóa dữ liệu | `논리 스키마` (Lược đồ bảng, quan hệ) | Phụ thuộc mô hình DBMS (RDBMS), độc lập phần cứng |
| **4. 물리적 설계** (Thiết kế vật lý) | Quyết định cấu trúc lưu trữ đĩa, định dạng bản ghi, đánh Index | `물리 스키마` (Cấu trúc file, index) | **DBMS 및 HW 종속** (Phụ thuộc cả DBMS và phần cứng) |
| **5. 구현** (Cài đặt / Triển khai) | Viết câu lệnh DDL để tạo bảng, tạo index, nạp dữ liệu | Database chạy thật trên máy chủ | Hiện thực hóa mã nguồn DDL |

#### 3. Bẫy đề thi và quy tắc ghi nhớ (시험 대비 함정 & 암기 팁)

##### Các bẫy trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Vị trí của Chuẩn hóa (정규화의 단계)**
  - *Câu hỏi:* "Chuẩn hóa (정규화) được thực hiện ở giai đoạn nào trong quy trình thiết kế CSDL?"
  - *Đáp án đúng:* **Thiết kế Logic (논리적 설계)**.
  - *Bẫy sai:* Thí sinh rất dễ chọn nhầm *Thiết kế Vật lý (물리적 설계)* hoặc *Thiết kế Khái niệm (개념적 설계)*.
- **Bẫy 2: Vẽ sơ đồ E-R thuộc bước nào? (E-R 다이어그램 작성)**
  - *Câu hỏi:* "Sơ đồ E-R được xây dựng ở bước nào và chuyển đổi thành bảng ở bước nào?"
  - *Đáp án đúng:* **Xây dựng ở Thiết kế Khái niệm (개념적 설계)**; **Chuyển thành Bảng ở Thiết kế Logic (논리적 설계)**.
- **Bẫy 3: Độc lập với DBMS (DBMS 독립성)**
  - *Câu hỏi:* "Giai đoạn thiết kế nào hoàn toàn độc lập với phần mềm DBMS mục tiêu?"
  - *Đáp án đúng:* **Thiết kế Khái niệm (개념적 설계)**. Giai đoạn Thiết kế Logic đã phụ thuộc vào mô hình DBMS (ví dụ chọn RDBMS hay Graph DB).
- **Bẫy 4: Lệnh DDL nằm ở bước nào? (DDL의 단계)**
  - *Câu hỏi:* "Việc sử dụng DDL để tạo cấu trúc bảng thực tế diễn ra ở bước nào?"
  - *Đáp án đúng:* **Cài đặt (구현 / Implementation)**, không phải bước thiết kế.

##### Mẹo ghi nhớ thần chú (Mnemonic)
- **Thần chú trình tự:** `"Yêu - Khái - Lo - Vật - Cài"`
  - `Yêu`: **Yêu** cầu (`요구 조건 분석`)
  - `Khái`: **Khái** niệm (`개념적 설계` - Vẽ E-R, DBMS 독립적)
  - `Lo`: **Lo**gic (`논리적 설계` - Mapping bảng, Chuẩn hóa 정규화)
  - `Vật`: **Vật** lý (`물리적 설계` - Đĩa, Record, Index, Phụ thuộc HW)
  - `Cài`: **Cài** đặt (`구현` - Gõ lệnh DDL, chạy DB thật)

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chi tiết từng giai đoạn thiết kế (설계 단계별 핵심 내용)

##### 1.1. Phân tích yêu cầu (요구 조건 분석 / Requirements Analysis)
- **개념 (Bản chất):** Thu thập và phân tích các nhu cầu lưu trữ thông tin, quy tắc nghiệp vụ và khối lượng xử lý dự kiến từ người dùng cuối.
- **주요 활동 (Hoạt động chính):**
  - Khảo sát người dùng, phỏng vấn các phòng ban liên quan.
  - Phân tích luồng nghiệp vụ hiện hành và xác định phạm vi hệ thống mới.
  - Lập bản đặc tả yêu cầu cơ sở dữ liệu (`요구 조건 명세서`).

##### 1.2. Thiết kế khái niệm (개념적 설계 / Conceptual Design)
- **개념 (Bản chất):** Là quá trình nhận thức thế giới thực và biểu diễn thành các khái niệm trừu tượng (`현실 세계의 인식을 추상적 개념으로 표현`), hoàn toàn độc lập với hệ quản trị CSDL mục tiêu (`DBMS 독립적`).
- **2 công việc tiến hành song song (2대 병행 과업):**
  1. **개념 스키마 모델링 (Mô hình hóa lược đồ khái niệm):** Xác định các kiểu thực thể (Entity), thuộc tính (Attribute) và các mối quan hệ (Relationship) giữa chúng, tạo ra biểu đồ E-R (`E-R 다이어그램`).
  2. **트랜잭션 모델링 (Mô hình hóa giao dịch):** Xác định các thao tác nghiệp vụ, luồng xử lý dữ liệu đầu vào/đầu ra độc lập với DBMS để đảm bảo lược đồ khái niệm có đủ dữ liệu đáp ứng yêu cầu người dùng.
- **Sản phẩm đầu ra cốt lõi:** Biểu đồ thực thể - mối quan hệ (`E-R 다이어그램`).

##### 1.3. Thiết kế logic (논리적 설계 / Logical Design)
- **개념 (Bản chất):** Là quá trình chuyển đổi (ánh xạ / mapping) cấu trúc dữ liệu từ tầng khái niệm thành cấu trúc dữ liệu logic mà hệ quản trị CSDL mục tiêu hỗ trợ (`특정 DBMS가 지원하는 논리적 자료 구조로 변환`).
- **3 công việc cốt lõi (3대 핵심 과업):**
  1. **논리 스키마 설계 (Thiết kế lược đồ logic):** Ánh xạ các thực thể và quan hệ trong sơ đồ E-R thành các bảng (Relation Schema / Table) trong mô hình dữ liệu quan hệ.
  2. **정규화 수행 (Thực hiện chuẩn hóa dữ liệu):** Phân rã các bảng để loại bỏ sự dư thừa dữ liệu (Redundancy) và ngăn chặn 3 hiện tượng dị thường (Anomaly: Thêm, Xóa, Sửa).
  3. **트랜잭션 인터페이스 설계 (Thiết kế giao diện giao dịch):** Định nghĩa cụ thể các tham số đầu vào, đầu ra của từng giao dịch nghiệp vụ.
- **3 thành phần của mô hình dữ liệu (데이터 모델의 3대 요소):**
  - `구조 (Structure)`: Thể hiện tính chất tĩnh của dữ liệu và mối quan hệ giữa các đối tượng.
  - `연산 (Operation)`: Thể hiện tính chất động, các thao tác xử lý dữ liệu (SELECT, INSERT, UPDATE, DELETE).
  - `제약 조건 (Constraint)`: Các quy tắc toàn vẹn bắt buộc dữ liệu thực tế phải tuân thủ (Khóa chính, Khóa ngoại, NOT NULL, CHECK).

##### 1.4. Thiết kế vật lý (물리적 설계 / Physical Design)
- **개념 (Bản chất):** Chuyển đổi cấu trúc dữ liệu logic thành cấu trúc lưu trữ vật lý trên các thiết bị lưu trữ thứ cấp (như ổ đĩa cứng, SSD) phù hợp với DBMS cụ thể và cấu hình phần cứng máy chủ.
- **Nội dung bắt buộc phải quyết định:**
  - `저장 레코드 양식 설계`: Xác định kiểu dữ liệu, độ dài trường, phân bố giá trị và tần suất truy cập của từng bản ghi.
  - `레코드 집중 (Record Clustering)`: Gom các bản ghi thường xuyên được truy xuất cùng nhau vào cùng một khối nhớ vật lý (Block/Page) để giảm thiểu thao tác I/O đĩa.
  - `액세스 경로 및 인덱스 (Access Path & Index)`: Thiết kế các cây chỉ mục (B-Tree, Bitmap), cấu trúc bảng băm (Hashing) để tăng tốc độ tìm kiếm.
- **3 tiêu chí đánh giá hiệu năng thiết kế vật lý (물리적 설계 옵션 평가 기준):**
  1. `반응 시간 (Response Time)`: Thời gian từ lúc gửi yêu cầu truy vấn đến khi nhận kết quả.
  2. `공간 활용도 (Space Utilization)`: Dung lượng đĩa tiêu tốn bởi bảng dữ liệu và hệ thống chỉ mục phụ trợ.
  3. `트랜잭션 처리량 (Transaction Throughput)`: Số lượng giao dịch trung bình hệ thống xử lý trong 1 giây (TPS).

##### 1.5. Cài đặt (구현 / Implementation)
- **개념 (Bản chất):** Sử dụng ngôn ngữ định nghĩa dữ liệu (`DDL`) của DBMS mục tiêu để tạo ra cơ sở dữ liệu vật lý chạy thật trên hệ điều hành máy chủ.
- **Hoạt động:** Viết lệnh `CREATE TABLE`, `CREATE INDEX`, `CREATE VIEW`, cấp phát quyền truy cập và nạp dữ liệu ban đầu.

---

### 복습 체크리스트
- [ ] Thuộc lòng thứ tự 5 giai đoạn: `요구 조건 분석 → 개념적 설계 → 논리적 설계 → 물리적 설계 → 구현`.
- [ ] Phân biệt được: Khái niệm là vẽ E-R và độc lập DBMS; Logic là ánh xạ E-R sang bảng và làm Chuẩn hóa (정규화).
- [ ] Nắm vững 3 tiêu chí thiết kế vật lý: Thời gian phản hồi (`반응 시간`), Mức chiếm dụng không gian (`공간 활용도`), Thông lượng giao dịch (`트랜잭션 처리량`).
- [ ] Nhớ chính xác 3 thành phần của mô hình dữ liệu: Cấu trúc (`구조`), Thao tác (`연산`), Ràng buộc (`제약 조건`).
