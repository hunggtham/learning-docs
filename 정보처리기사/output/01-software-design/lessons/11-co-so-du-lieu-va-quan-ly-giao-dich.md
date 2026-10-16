# 관계형 데이터베이스 및 트랜잭션 관리 (Cơ sở dữ liệu quan hệ và Quản lý Giao dịch)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc của Mô hình dữ liệu quan hệ (`관계형 데이터베이스 - RDBMS`): Bảng quan hệ (`릴레이션`), Bộ (`튜플`), Thuộc tính (`속성`), Lực lượng (`카디널리티`), Bậc (`디그리`), và các loại khóa (`기본키, 외래키, 후보키`).
- Thuộc nằm lòng 2 quy tắc ràng buộc toàn vẹn cốt lõi: Toàn vẹn thực thể (`개체 무결성`) và Toàn vẹn tham chiếu (`참조 무결성`).
- Làm chủ 4 phép toán quan hệ thuần túy trong Đại số quan hệ (`순수 관계 연산자: Select, Project, Join, Division`) và công thức tính Bậc/Lực lượng khi tích Descartes.
- Giải mã 3 hiện tượng dị thường dữ liệu (`이상 현상 - Anomaly: 삽입, 삭제, 갱신`) và quy trình 6 cấp độ chuẩn hóa cơ sở dữ liệu (`정규화: 1NF → 2NF → 3NF → BCNF → 4NF → 5NF`) bằng câu thần chú thần tốc **Do - Bu - I - Kyeo - Da - Jo** (`도 - 부 - 이 - 결 - 다 - 조`).
- Làm chủ 4 đặc tính sinh tử `ACID` của Giao dịch (`트랜잭션`), sơ đồ 5 trạng thái giao dịch (`트랜잭션의 상태`), và cơ chế phục hồi dữ liệu (`회복: REDO vs UNDO`).
- Phân tích sâu sắc kỹ thuật Kiểm soát đồng thời (`병행 제어`), giao thức khóa hai pha (`2PL`), an toàn mật mã (`대칭키 vs 비대칭키`), và 4 tính trong suốt của CSDL phân tán (`분산 투명성 4대 요소`).

## 핵심 키워드 (Từ khóa)
- 릴레이션 (Relation / Table / 튜플 - Row / 속성 - Column / 카디널리티 / 디그리 - Degree)
- 무결성 제약조건 (개체 무결성 - PK not null & unique / 참조 무결성 - FK = PK or null)
- 순수 관계 연산자 (Select $\sigma$, Project $\pi$, Join $\bowtie$, Division $\div$)
- 이상 현상 (Anomaly: 삽입 이상 - Insert, 삭제 이상 - Delete, 갱신 이상 - Update)
- 정규화 6단계 (Normalization: 1NF 원자값, 2NF 부분함수 제거, 3NF 이행함수 제거, BCNF 결정자, 4NF 다치종속, 5NF 조인종속)
- 트랜잭션 ACID (원자성 - Atomicity, 일관성 - Consistency, 격리성 - Isolation, 지속성 - Durability)
- 회복 기법 (Recovery: REDO - 재실행, UNDO - 취소 원상복구, 연기 갱신 vs 즉시 갱신)
- 병행 제어 (Concurrency Control: 갱신 분실, 모순성, 연쇄 복귀 / 2단계 로킹 규약 - 2PL)
- 암호화 기법 (대칭키 - DES, AES, 고속 vs 비대칭키 - RSA, 공개키/개인키, 키 관리 용이)
- 분산 투명성 4대 요소 (위치 투명성, 분할 투명성, 복제 투명성, 병행 투명성)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ [10-giao-dien-va-middleware.md](10-giao-dien-va-middleware.md), khi các hệ thống trao đổi dữ liệu với nhau qua Middleware và API, toàn bộ dữ liệu nghiệp vụ cốt lõi đều phải được lưu trữ lâu dài và bảo vệ tính toàn vẹn bên trong các Hệ quản trị cơ sở dữ liệu (DBMS).
- **Đang giải quyết gì (Current Problem):** Bài học chuyên đề này hợp nhất toàn diện 9 bài học nền tảng CSDL từ nguồn tài liệu gốc, giải quyết bài toán thiết kế cấu trúc dữ liệu tối ưu không bị dư thừa (Chuẩn hóa), truy vấn bằng phép toán quan hệ, và bảo đảm an toàn dữ liệu tuyệt đối trước các sự cố sập nguồn hoặc xung đột đa luồng thông qua cơ chế Quản lý giao dịch (ACID, Concurrency Control, Recovery).
- **Dùng đi đâu (Forward Handoff):** Kiến thức này cung cấp nền tảng lý thuyết vững chắc cho Môn 3: 데이터베이스 구축 (Xây dựng CSDL), đồng thời liên kết trực tiếp sang chuyên đề cấu trúc bộ nhớ trong [12-cau-truc-du-lieu-va-thuat-toan.md](12-cau-truc-du-lieu-va-thuat-toan.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng thần chú chuẩn hóa CSDL **Đô - Phụ - Di - Quyết - Đa - Nối** (`도 - 부 - 이 - 결 - 다 - 조`); phân biệt REDO vs UNDO; thuộc 4 đặc tính ACID; và nhận diện 4 tính trong suốt phân tán.
- Đọc TẦNG B để phân tích bài toán mẫu tính số bộ của phép tích Descartes và cơ chế phòng chống dị thường dữ liệu bằng khóa ngoại.

---

## 관계형 데이터베이스 및 트랜잭션 관리

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cấu trúc Mô hình Dữ liệu Quan hệ (Relational Model)
- **Các thành phần cốt lõi của một Bảng quan hệ (`릴레이션 - Relation`):**
  - `릴레이션 (Relation)`: Bảng dữ liệu 2 chiều gồm các hàng và các cột.
  - `튜플 (Tuple)`: Một hàng trong bảng (`행 - Row / Record`), đại diện cho một thực thể dữ liệu cụ thể.
  - `속성 (Attribute)`: Một cột trong bảng (`열 - Column / Field`), đại diện cho một đặc trưng thuộc tính của thực thể.
  - `도메인 (Domain)`: Tập hợp tất cả các giá trị hợp lệ mà một thuộc tính có thể nhận (ví dụ: Miền giá trị của Giới tính là `{Nam, Nữ}`).
  - **카디널리티 (Cardinality — Lực lượng):** **Tổng số hàng (số Tuple)** hiện có trong bảng quan hệ. Thay đổi liên tục khi thêm/xóa dữ liệu.
  - **디그리 / 차수 (Degree — Bậc):** **Tổng số cột (số Attribute)** cấu thành nên bảng quan hệ. Thường cố định sau khi thiết kế bảng.

- **Các loại khóa trong Cơ sở dữ liệu:**
  1. `슈퍼키 (Super Key)`: Tập hợp các thuộc tính có tính **Duy nhất (유일성 - Uniqueness)**, đủ để phân biệt từng tuple, nhưng chưa đạt tính tối thiểu.
  2. `후보키 (Candidate Key)`: Tập hợp các thuộc tính vừa có tính **Duy nhất (유일성)**, vừa có tính **Tối thiểu (최소성 - Minimality)** (không thể bỏ bớt bất kỳ thuộc tính nào mà vẫn định danh được).
  3. `기본키 (Primary Key - PK)`: Khóa ứng viên được người thiết kế CSDL chọn làm định danh chính cho bảng; **bắt buộc không được mang giá trị NULL và không được trùng lặp**.
  4. `대체키 (Alternate Key)`: Các khóa ứng viên còn lại không được chọn làm khóa chính.
  5. `외래키 (Foreign Key - FK)`: Thuộc tính trong một bảng tham chiếu trực tiếp đến Khóa chính của một bảng khác; dùng để thiết lập mối liên kết giữa các bảng.

- **2 Ràng buộc Toàn vẹn cốt lõi (무결성 제약조건):**
  - **개체 무결성 (Entity Integrity — Toàn vẹn thực thể):**
    - [Hàn/Anh]: `기본키(PK)는 고유한 값을 가져야 하며, 절대 NULL 값을 가질 수 없다.`
    - [Tiếng Việt]: Khóa chính phải định danh duy nhất từng bản ghi và tuyệt đối không bao giờ được phép mang giá trị NULL.
  - **참조 무결성 (Referential Integrity — Toàn vẹn tham chiếu):**
    - [Hàn/Anh]: `외래키(FK) 값은 참조하는 릴레이션의 기본키 값과 일치하거나 NULL이어야 한다.`
    - [Tiếng Việt]: Khóa ngoại không bao giờ được phép trỏ tới một bản ghi không tồn tại ở bảng cha; giá trị khóa ngoại phải bằng với giá trị khóa chính của bảng cha hoặc mang giá trị NULL.

---

#### 2. Đại số quan hệ và Quy trình Chuẩn hóa dữ liệu

##### A. 4 Phép toán quan hệ thuần túy (순수 관계 연산자)
1. `Select (셀렉트 / 기호: σ)`: Trích xuất các **Hàng (Tuple)** thỏa mãn điều kiện chỉ định (Cắt bảng theo chiều ngang).
2. `Project (프로젝트 / 기호: π)`: Trích xuất các **Cột (Attribute)** mong muốn (Cắt bảng theo chiều dọc, tự động loại bỏ các hàng trùng lặp).
3. `Join (조인 / 기호: ⋈)`: Kết hợp các bộ từ hai bảng quan hệ lại với nhau dựa trên giá trị của các thuộc tính chung (Natural Join, Equi Join).
4. `Division (디비전 / 기호: ÷)`: Phép chia bảng; tìm các bộ ở bảng A chứa toàn bộ các giá trị thuộc tính xuất hiện ở bảng B.

- **Quy tắc toán học khi thực hiện Tích Descartes (Cartesian Product / 기호: $\times$):**
  $$\text{Degree}(A \times B) = \text{Degree}(A) + \text{Degree}(B) \quad (\text{Bậc cộng})$$
  $$\text{Cardinality}(A \times B) = \text{Cardinality}(A) \times \text{Cardinality}(B) \quad (\text{Lực lượng nhân})$$

##### B. Hiện tượng Dị thường dữ liệu (이상 현상 - Anomalies)
Xảy ra khi thiết kế bảng dữ liệu tồi, chứa nhiều phụ thuộc hàm dư thừa:
1. `삽입 이상 (Insertion Anomaly — Dị thường chèn)`: Muốn chèn một thông tin mới nhưng buộc phải chèn thêm các dữ liệu không mong muốn khác do ràng buộc khóa chính.
2. `삭제 이상 (Deletion Anomaly — Dị thường xóa)`: Khi xóa một mẩu thông tin phụ thì vô tình làm **mất luôn toàn bộ thông tin quan trọng khác** của thực thể.
3. `갱신 이상 (Update Anomaly — Dị thường cập nhật)`: Khi sửa đổi một thông tin bị trùng lặp ở nhiều hàng, nếu không sửa đồng bộ tất cả các hàng sẽ dẫn đến hiện tượng **dữ liệu mâu thuẫn bất nhất**.

##### C. Quy trình Chuẩn hóa 6 Cấp độ (Normalization)
Chuẩn hóa là quy trình phân rã một bảng quan hệ lớn có dị thường thành các bảng quan hệ nhỏ hơn, an toàn và không làm mất thông tin.
- **Thần chú ghi nhớ 6 bước chuẩn hóa:** **도 - 부 - 이 - 결 - 다 - 조** (*Đô - Phụ - Di - Quyết - Đa - Nối*).

| Cấp độ chuẩn | Điều kiện thỏa mãn kỹ thuật | Mục tiêu loại bỏ |
|:---:|:---|:---|
| **1NF (제1정규형)** | Tất cả các giá trị thuộc tính phải là **giá trị nguyên tử (`원자값`)** | Loại bỏ thuộc tính đa trị, mảng lặp |
| **2NF (제2정규형)** | 1NF + Loại bỏ **phụ thuộc hàm một phần (`부분 함수 종속성 제거`)** | Mọi thuộc tính không khóa phải phụ thuộc hoàn toàn vào toàn bộ khóa chính |
| **3NF (제3정규형)** | 2NF + Loại bỏ **phụ thuộc hàm bắc cầu (`이행적 함수 종속성 제거`: $A \rightarrow B$ và $B \rightarrow C$)** | Thuộc tính không khóa không được phụ thuộc gián tiếp qua một thuộc tính không khóa khác |
| **BCNF (보이스-코드)**| 3NF + Mọi **hàm xác định (`결정자 - Determinant`) đều phải là khóa ứng viên** | Loại bỏ phụ thuộc hàm trong đó vế trái không phải là Candidate Key |
| **4NF (제4정규형)** | BCNF + Loại bỏ **phụ thuộc đa trị (`다치 종속성 제거` / Multi-valued Dependency)** | Không cho phép 1 giá trị khóa tương ứng với 1 tập hợp nhiều giá trị độc lập |
| **5NF (제5정규형)** | 4NF + Loại bỏ **phụ thuộc nối (`조인 종속성 이용` / Join Dependency)** | Đảm bảo bảng có thể phân rã và nối lại không suy hao (Lossless Join) |

---

#### 3. Quản lý Giao dịch (Transaction) và 4 Đặc tính ACID
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `트랜잭션(Transaction)은 데이터베이스에서 하나의 논리적 기능을 수행하기 위한 작업의 기본 단위이며, ACID(원자성, 일관성, 격리성, 지속성) 특성을 만족해야 한다.`
  - [Tiếng Việt]: Giao dịch là một đơn vị xử lý logic logic duy nhất bao gồm một hoặc nhiều thao tác SQL (ví dụ: chuyển tiền từ tài khoản A sang B). Toàn bộ chuỗi thao tác phải được thực thi trọn vẹn hoặc không có thao tác nào được thực thi.

- **4 Đặc tính sống còn ACID:**
  1. `원자성 (Atomicity — Tính nguyên tử / All or Nothing)`: Toàn bộ các thao tác trong giao dịch phải **hoàn tất 100% hoặc bị hủy bỏ hoàn toàn 0%**, không bao giờ tồn tại trạng thái dở dang ở giữa. Được bảo đảm bởi thao tác `COMMIT` và `ROLLBACK`.
  2. `일관성 (Consistency — Tính nhất quán)`: Sau khi giao dịch hoàn tất thành công, cơ sở dữ liệu phải luôn ở trạng thái nhất quán, thỏa mãn toàn bộ các ràng buộc toàn vẹn (ví dụ: tổng tiền trong hệ thống không đổi sau khi chuyển tiền).
  3. `격리성 / 고립성 (Isolation — Tính cô lập)`: Các giao dịch đang chạy đồng thời không được phép can thiệp hay nhìn thấy dữ liệu trung gian chưa commit của nhau.
  4. `지속성 / 영속성 (Durability — Tính bền vững)`: Một khi giao dịch đã `COMMIT` thành công, các thay đổi dữ liệu phải được **ghi nhận vĩnh viễn vào đĩa cứng**, ngay cả khi hệ thống bị mất điện đột ngột ngay sau đó.

- **5 Trạng thái của Giao dịch (Transaction States):**
  $$\text{활동 (Active)} \rightarrow \text{부분 완료 (Partially Committed)} \rightarrow \text{완료 (Committed)}$$
  $$\text{활동 (Active)} \rightarrow \text{실패 (Failed)} \rightarrow \text{철회 (Aborted)}$$
  - `활동 (Active)`: Giao dịch đang thực thi các câu lệnh.
  - `부분 완료 (Partially Committed)`: Câu lệnh SQL cuối cùng đã chạy xong trong bộ nhớ đệm (RAM) nhưng dữ liệu **chưa được ghi an toàn xuống đĩa cứng**.
  - `완료 (Committed)`: Dữ liệu đã được ghi vĩnh viễn xuống đĩa cứng, kết thúc giao dịch thành công.
  - `실패 (Failed)`: Phát hiện lỗi logic hoặc sự cố phần cứng trong quá trình thực thi.
  - `철회 (Aborted)`: Đã thực hiện thao tác `ROLLBACK` khôi phục cơ sở dữ liệu về nguyên trạng ban đầu.

---

#### 4. Kỹ thuật Phục hồi dữ liệu (Recovery) và Kiểm soát đồng thời (Concurrency Control)

##### A. Phục hồi dữ liệu: REDO vs UNDO
- **REDO (Tái thực thi / Làm lại):** Áp dụng cho các giao dịch đã thực hiện `COMMIT` trước khi hệ thống sập nhưng dữ liệu mới chỉ nằm ở bộ đệm RAM chưa kịp ghi xuống đĩa $\rightarrow$ Dựa vào file Log để ghi lại dữ liệu vào đĩa.
- **UNDO (Hủy bỏ / Khôi phục ban đầu):** Áp dụng cho các giao dịch đang ở trạng thái dở dang chưa `COMMIT` khi hệ thống sập $\rightarrow$ Dựa vào file Log để hủy bỏ toàn bộ thao tác, trả dữ liệu về trạng thái ban đầu.
- **Các phương pháp phục hồi tiêu biểu:**
  - `연기 갱신 기법 (Deferred Update — Cập nhật trì hoãn)`: Chỉ ghi log, đợi giao dịch commit mới ghi đĩa $\rightarrow$ **Chỉ cần REDO, tuyệt đối không cần UNDO**.
  - `즉시 갱신 기법 (Immediate Update — Cập nhật ngay)`: Dữ liệu được ghi ngay xuống đĩa trong khi giao dịch đang chạy $\rightarrow$ **Cần cả REDO và UNDO**.
  - `체크포인트 기법 (Checkpoint — Điểm kiểm tra)`: Định kỳ ghi toàn bộ bộ đệm xuống đĩa và đánh dấu mốc kiểm tra, giúp rút ngắn thời gian quét log khi phục hồi.

##### B. Kiểm soát đồng thời (Concurrency Control)
- **4 Lỗi phát sinh nếu không kiểm soát đồng thời:**
  1. `갱신 분실 (Lost Update)`: Hai giao dịch cùng ghi đè lên một bản ghi, làm mất kết quả cập nhật của giao dịch trước.
  2. `모순성 (Inconsistency)`: Dữ liệu bị đọc trong trạng thái không nhất quán giữa hai lần truy vấn.
  3. `연쇄 복귀 (Cascading Rollback)`: Một giao dịch bị hủy kéo theo việc phải hủy hàng loạt giao dịch khác đã đọc dữ liệu của nó.
  4. `비인가 변화 (Dirty Read)`: Đọc phải dữ liệu tạm thời của một giao dịch chưa commit và sau đó giao dịch đó lại bị rollback.
- **Giao thức khóa 2 pha (2-Phase Locking Protocol — 2PL):**
  - Đảm bảo tính tuần tự hóa (Serializability) cho các giao dịch đồng thời.
  - Gồm 2 giai đoạn:
    1. `확장 단계 (Growing Phase - Giai đoạn mở rộng)`: Chỉ được phép yêu cầu xin cấp thêm khóa mới (Lock), không được phép giải phóng khóa.
    2. `축소 단계 (Shrinking Phase - Giai đoạn thu hẹp)`: Chỉ được phép giải phóng các khóa hiện có (Unlock), không được phép xin thêm khóa mới.
  - **Lưu ý:** Giao thức 2PL bảo đảm tính tuần tự nhưng **vẫn có thể phát sinh Khóa chết (Deadlock)**.

---

#### 5. An toàn Mật mã và CSDL Phân tán

##### A. So sánh mã hóa: Đối xứng vs Bất đối xứng

| Tiêu chí | 대칭키 암호화 (Symmetric / Khóa đối xứng) | 비대칭키 암호화 (Asymmetric / Khóa công khai) |
|:---|:---|:---|
| **Cơ chế khóa** | Mã hóa và giải mã bằng **CÙNG MỘT KHÓA BÍ MẬT** | Dùng cặp khóa: **Khóa công khai (Public Key) để mã hóa**, **Khóa riêng tư (Private Key) để giải mã** |
| **Tốc độ mã hóa** | **Rất nhanh (고속)**, phù hợp mã hóa khối dữ liệu lớn | **Chậm hơn (저속)**, tiêu tốn nhiều năng lực tính toán CPU |
| **Quản lý khóa** | Khó khăn khi số lượng người dùng $N$ tăng: $\frac{N(N-1)}{2}$ khóa | Rất dễ dàng, mỗi người chỉ cần 1 cặp khóa ($2N$ khóa) |
| **Thuật toán tiêu biểu** | **DES, 3-DES, AES, SEED, ARIA** | **RSA, ECC (Elliptic Curve), Diffie-Hellman** |

##### B. 4 Tính trong suốt của CSDL Phân tán (Distributed Transparency)
1. `위치 투명성 (Location Transparency — Trong suốt vị trí)`: Người dùng truy vấn dữ liệu mà không cần biết dữ liệu đang nằm vật lý ở máy chủ nào.
2. `분할 투명성 (Fragmentation Transparency — Trong suốt phân mảnh)`: Bảng dữ liệu có thể bị chia nhỏ theo chiều ngang hoặc dọc ở nhiều nơi, người dùng chỉ nhìn thấy một bảng duy nhất.
3. `복제 투명성 (Replication Transparency — Trong suốt sao chép)`: Dữ liệu được nhân bản ở nhiều server dự phòng, nhưng người dùng thao tác như thể chỉ có 1 bản duy nhất.
4. `병행 투명성 (Concurrency Transparency — Trong suốt đồng thời)`: Nhiều giao dịch chạy đồng thời trên hệ thống phân tán mà không gây xung đột dữ liệu.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán mẫu tính toán Tích Descartes trong đề thi
- Cho Bảng $A$ có 3 thuộc tính (Degree = 3) và 4 bản ghi (Cardinality = 4).
- Cho Bảng $B$ có 4 thuộc tính (Degree = 4) và 5 bản ghi (Cardinality = 5).
- **Câu hỏi:** Bảng kết quả sau khi thực hiện phép toán $A \times B$ có Bậc và Lực lượng là bao nhiêu?
  - **Bậc (Degree) kết quả:** $\text{Degree}(A) + \text{Degree}(B) = 3 + 4 = \mathbf{7}$.
  - **Lực lượng (Cardinality) kết quả:** $\text{Cardinality}(A) \times \text{Cardinality}(B) = 4 \times 5 = \mathbf{20}$.
- Đề thi trắc nghiệm rất hay đổi ngược giữa Bậc và Lực lượng; luôn nhớ: **Bậc là số Cột $\rightarrow$ Cộng; Lực lượng là số Hàng $\rightarrow$ Nhân**.

---

### 복습 체크리스트
- [ ] Phân biệt được Bậc (Degree - số cột) và Lực lượng (Cardinality - số hàng) của bảng quan hệ.
- [ ] Nhớ điều kiện của 개체 무결성 (Khóa chính không được NULL và trùng lặp) và 참조 무결성 (Khóa ngoại phải bằng khóa chính hoặc NULL).
- [ ] Thuộc 4 phép toán quan hệ thuần túy: Select ($\sigma$), Project ($\pi$), Join ($\bowtie$), Division ($\div$).
- [ ] Đọc vanh vách thần chú 6 bước chuẩn hóa: 도 (nguyên tử) $\rightarrow$ 부 (phụ thuộc một phần) $\rightarrow$ 이 (phụ thuộc bắc cầu) $\rightarrow$ 결 (quyết định không là khóa) $\rightarrow$ 다 (phụ thuộc đa trị) $\rightarrow$ 조 (phụ thuộc nối).
- [ ] Thuộc 4 đặc tính ACID của giao dịch: Nguyên tử (Atomicity), Nhất quán (Consistency), Cô lập (Isolation), Bền vững (Durability).
- [ ] Phân biệt được trạng thái 부분 완료 (chạy xong trong RAM) và 완료 (đã ghi đĩa vĩnh viễn).
- [ ] Phân biệt được REDO (làm lại giao dịch đã commit) và UNDO (hủy bỏ giao dịch chưa commit về ban đầu).
- [ ] Nhớ tên các thuật toán khóa đối xứng (DES, AES, SEED, ARIA) và bất đối xứng (RSA, ECC).
- [ ] Kể tên 4 tính trong suốt phân tán: vị trí, phân mảnh, sao chép, đồng thời.
