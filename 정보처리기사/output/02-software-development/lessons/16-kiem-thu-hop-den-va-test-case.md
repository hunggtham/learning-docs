# 블랙박스 테스트와 테스트 케이스 설계 (Kiểm thử hộp đen và thiết kế Test Case)

## 학습 목표
- Nắm vững định nghĩa và đặc trưng của Kiểm thử hộp đen (`블랙박스 테스트 / Black-Box Testing` / `명세 기반 테스트`): kiểm thử dựa trên đặc tả yêu cầu, không nhìn mã nguồn, chủ yếu áp dụng ở cấp độ tích hợp (`통합`), hệ thống (`시스템`) và nghiệm thu (`인수`).
- Phân biệt và áp dụng thành thạo các kỹ thuật thiết kế ca kiểm thử hộp đen chuẩn thi: Phân vùng tương đương (`동치 분할`), Phân tích giá trị biên (`경계값 분석`), Đồ thị nguyên nhân - kết quả (`원인-효과 그래프`), Bảng quyết định (`의사결정 테이블`), Kiểm thử chuyển trạng thái (`상태 전이`), Đoán lỗi (`오류 예측`), Pairwise (`페어와이즈`) và Kiểm tra so sánh (`비교 검사`).
- Nắm vững quy chuẩn tài liệu kiểm thử theo tiêu chuẩn quốc tế ISO/IEC/IEEE 29119-3: các thành phần của một Test Case (`테스트 케이스`) và phân biệt với Test Scenario (`테스트 시나리오`).
- Hiểu rõ vai trò của Ma trận truy xuất nguồn gốc yêu cầu (`RTM - Requirements Traceability Matrix`) nhằm bảo đảm 100% yêu cầu được bao phủ bởi ca kiểm thử.

## 핵심 키워드
- 블랙박스 테스트 (Kiểm thử hộp đen / Black-Box / 명세 기반 / Opaque-box)
- 동치 분할 (Phân vùng tương đương / Equivalence Partitioning / 유효·무효 동치 클래스)
- 경계값 분석 (Phân tích giá trị biên / Boundary Value Analysis / min-1, min, min+1, max-1, max, max+1)
- 원인-효과 그래프 (Đồ thị nguyên nhân - kết quả / Cause-Effect Graphing / 의사결정 테이블)
- 오류 예측 (Đoán lỗi / Error Guessing / kinh nghiệm và trực giác kiểm thử viên)
- 테스트 케이스 & 테스트 시나리오 (Test Case & Test Scenario / ISO/IEC/IEEE 29119-3)
- RTM (Requirements Traceability Matrix / 추적 매트릭스 / 100% 요구사항 검증)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [15-kiem-thu-hop-trang-va-coverage.md](15-kiem-thu-hop-trang-va-coverage.md), chúng ta đã khảo sát các kỹ thuật kiểm thử hộp trắng dựa trên cấu trúc logic và mã nguồn nội bộ.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc thiết kế ca kiểm thử khi không đọc mã nguồn, tối ưu hóa không gian dữ liệu kiểm thử qua phân vùng tương đương và giá trị biên, mô hình hóa quy tắc nghiệp vụ phức tạp và chuẩn hóa tài liệu ca kiểm thử theo ISO/IEC/IEEE 29119-3.
- **Dùng đi đâu (Forward Handoff):** Sau khi có bộ ca kiểm thử chức năng, bàn giao trực tiếp sang [17-v-model-kiem-thu-tich-hop-va-oracle.md](17-v-model-kiem-thu-tich-hop-va-oracle.md) để phân bổ vào các giai đoạn phát triển theo mô hình chữ V và thiết lập cơ chế thẩm định kết quả bằng Test Oracle.

## 읽는 방법
- Đọc TẦNG A để nắm vững định nghĩa cốt lõi, bảng tổng hợp 8 kỹ thuật thiết kế ca kiểm thử hộp đen, bảng cấu trúc chuẩn của Test Case theo ISO 29119-3, và bảng phân biệt Test Case vs Test Scenario.
- Đọc TẦNG B để hiểu sâu cơ chế chọn điểm biên 2 điểm vs 3 điểm, quy trình chuyển đổi từ Cause-Effect Graph sang Decision Table, và cơ chế truy xuất nguồn gốc RTM.

---

## 블랙박스 테스트와 테스트 케이스 설계

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khái niệm và đặc điểm kiểm thử hộp đen (블랙박스 테스트)
- **Định nghĩa:**
  - [한국어]: **블랙박스 테스트는 소프트웨어의 내부 구조나 작동 원리를 모르는 상태에서 요구사항 명세서를 기반으로 기능이 정상적으로 동작하는지 검증하는 방법이다.**
  - [Tiếng Việt]: Kiểm thử hộp đen là phương pháp kiểm thử mà kiểm thử viên hoàn toàn không nhìn thấy mã nguồn bên trong, tập trung kiểm tra chức năng dựa trên tài liệu đặc tả yêu cầu bằng cách đưa dữ liệu đầu vào (Input) và đối chiếu kết quả đầu ra (Output).
- **Đối tượng kiểm tra:** Giao diện bên ngoài (UI/API), các tính năng nghiệp vụ, định dạng nhập/xuất và khả năng xử lý ngoại lệ.
- **Cấp độ áp dụng:** Áp dụng chủ yếu ở các tầng cao như **통합 테스트 (Integration Test)**, **시스템 테스트 (System Test)** và **인수 테스트 (Acceptance Test)**.
- **Mục tiêu chính:** Phát hiện các tính năng bị lập trình viên bỏ sót (omission faults), lỗi giao diện, sai lệch đặc tả nghiệp vụ.

#### 2. Bảng tổng hợp các kỹ thuật thiết kế ca kiểm thử hộp đen chuẩn thi
| Kỹ thuật kiểm thử | Tên tiếng Hàn & Anh | Cơ chế cốt lõi | Dấu hiệu nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **Phân vùng tương đương** | **동치 분할 (Equivalence Partitioning)** | Chia miền đầu vào thành các lớp hợp lệ (유효) và không hợp lệ (무효), chọn **1 giá trị đại diện** cho mỗi lớp | *동치 클래스, 대표값, 유효/무효* |
| **Phân tích giá trị biên** | **경계값 분석 (Boundary Value Analysis)** | Tập trung chọn các giá trị tại biên và sát mép biên ($min-1, min, min+1, max-1, max, max+1$) | *경계값, 경계 부근 오류 집중, 1 단위 차이* |
| **Đồ thị nguyên nhân - kết quả** | **원인-효과 그래프 (Cause-Effect Graphing)** | Dùng logic Boolean (AND, OR, NOT) liên kết nguyên nhân (Input) và kết quả (Output), chuyển thành Bảng quyết định | *입력 조건(원인), 출력 반응(효과), 불리언 로직* |
| **Bảng quyết định** | **의사결정 테이블 (Decision Table)** | Lập bảng điều kiện và hành động, mỗi cột biểu diễn một quy tắc nghiệp vụ (Rule) độc lập | *조건과 동작의 조합, 복잡한 논리 규칙* |
| **Kiểm thử chuyển trạng thái** | **상태 전이 테스팅 (State Transition)** | Dựa trên máy trạng thái hữu hạn (FSM) kiểm tra việc chuyển trạng thái khi có sự kiện tác động | *이벤트, 상태 전이, FSM, ATM/주문 프로세스* |
| **Đoán lỗi** | **오류 예측 (Error Guessing)** | Không dựa trên quy tắc toán học; dựa hoàn toàn vào **kinh nghiệm và trực giác của kiểm thử viên** | *테스터의 경험과 감각, 직관적 추측* |
| **Kiểm thử cặp** | **페어와이즈 (Pairwise Testing)** | Bảo đảm mọi cặp 2 yếu tố bất kỳ đều được kết hợp kiểm tra cùng nhau ít nhất 1 lần | *2개 요소 조합, 테스트 케이스 수 대폭 감축* |
| **Kiểm tra so sánh** | **비교 검사 (Comparison Testing)** | Nạp cùng dữ liệu đầu vào vào nhiều phiên bản phần mềm độc lập để đối chiếu tính đồng nhất | *동일한 입력, 여러 버전 출력 비교* |

#### 3. Bảng cấu trúc chuẩn của Test Case (ISO/IEC/IEEE 29119-3)
| Thành phần cấu tạo | Tên tiếng Hàn & Anh | Ý nghĩa và Quy chuẩn nội dung |
| :--- | :--- | :--- |
| **Mã định danh** | **테스트 식별자 (Test ID)** | Mã duy nhất để phân loại và truy vết (ví dụ: `TC_AUTH_LOGIN_001`) |
| **Hạng mục kiểm tra** | **테스트 항목 (Test Item)** | Tên chức năng hoặc module được kiểm tra (ví dụ: Đăng nhập hệ thống) |
| **Điều kiện tiên quyết** | **환경 설정 / 전제 조건 (Pre-conditions)** | Trạng thái bắt buộc của hệ thống trước khi bắt đầu test (ví dụ: Đã có tài khoản kích hoạt) |
| **Dữ liệu đầu vào** | **입력 명세 (Input Specification)** | Các tham số cụ thể truyền vào (ví dụ: `Username = "admin"`, `Password = "1234"`) |
| **Kết quả kỳ vọng** | **출력 명세 / 기대 결과 (Expected Result)** | Hành vi và giá trị hệ thống phải trả về (ví dụ: Hiển thị thông báo "Mật khẩu sai") |
| **Thủ tục thực hiện** | **특수 절차 요구 (Special Procedures)** | Các thao tác môi trường đặc thù (ví dụ: Rút dây mạng trong lúc bấm Đăng nhập) |
| **Quan hệ phụ thuộc** | **의존성 기술 (Inter-case Dependencies)** | Chỉ rõ Test Case này có bắt buộc phải chạy sau Test Case nào khác không |

#### 4. Phân biệt Test Case vs Test Scenario
| Tiêu chí | 테스트 케이스 (Test Case) | 테스트 시나리오 (Test Scenario) |
| :--- | :--- | :--- |
| **Bản chất** | **Phép thử đơn lẻ cho một trường hợp cụ thể** | **Kịch bản chuỗi hành vi liên hoàn của người dùng** |
| **Độ chi tiết** | Cực kỳ chi tiết: từng tham số đầu vào, từng kết quả mong đợi | Mô tả luồng nghiệp vụ ở mức tổng quan |
| **Mối quan hệ** | **Nhiều Test Case kết hợp lại tạo thành một Test Scenario** | Là tài liệu khung định hướng để suy ra tập hợp các Test Case |
| **Ví dụ minh họa** | Kiểm tra trường Mật khẩu để trống có hiện cảnh báo lỗi hay không | Kịch bản mua hàng: Đăng nhập $\rightarrow$ Tìm kiếm sản phẩm $\rightarrow$ Thêm giỏ hàng $\rightarrow$ Thanh toán |

#### 5. Bảng phân loại mức độ lỗi phần mềm (Defect Severity & Priority)

| Cấp độ 심각도 (Severity — Mức độ nghiêm trọng) | Ý nghĩa kỹ thuật | Cấp độ 우선순위 (Priority — Độ ưu tiên sửa) | Ý nghĩa kinh doanh |
|:---|:---|:---|:---|
| **치명적 (Critical)** | Hệ thống sập hoàn toàn (Crash), mất mát dữ liệu, tê liệt chức năng sống còn, không có giải pháp thay thế | **High (상 - Khẩn cấp)** | Phải sửa ngay lập tức trong vòng vài giờ (Hotfix), chặn đứng việc phát hành |
| **주요 (Major)** | Tính năng nghiệp vụ chính bị lỗi, ảnh hưởng diện rộng nhưng hệ sinh thái chung vẫn hoạt động | **Medium (중 - Bình thường)** | Bắt buộc sửa trong đợt phát hành hoặc Sprint hiện tại |
| **보통 (Normal)** | Tính năng phụ hoặc tình huống đặc thù bị lỗi, có giải pháp thay thế tạm thời (Workaround) | **Low (하 - Thấp)** | Có thể lùi lại để sửa trong các đợt cập nhật sau |
| **경미 (Minor / Trivial)** | Sai chính tả (UI typo), lệch font chữ, màu nút bấm không chuẩn, không ảnh hưởng chức năng | **Low (하 - Thấp)** | Tích lũy sửa khi có thời gian bảo trì định kỳ |

#### 6. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Số lượng mẫu trong Phân vùng tương đương (동치 분할):** Trong mỗi lớp tương đương, **chỉ cần chọn đúng 1 giá trị đại diện**. Nếu đề bài bảo phải chọn tất cả các giá trị là SAI.
- **Bẫy 2: Điểm biên trong Boundary Value Analysis (경계값 분석):** Phần lớn lỗi xảy ra ở ranh giới điều kiện do lỗi lệch 1 đơn vị (Off-by-one, nhầm `<` và `<=`). Khi điều kiện là $0 \le x \le 100$, bộ giá trị biên chuẩn 3 điểm là $\{-1, 0, 1, 99, 100, 101\}$.
- **Bẫy 3: Đặc trưng của Error Guessing (오류 예측):** Khi đề hỏi "Kỹ thuật kiểm thử nào dựa vào kinh nghiệm, trực giác và sự nhạy cảm của kiểm thử viên thay vì công thức toán học?" $\rightarrow$ Chọn ngay **오류 예측 (Error Guessing)**.
- **Bẫy 4: Vai trò của RTM:** Ma trận truy xuất nguồn gốc (Requirements Traceability Matrix) liên kết mỗi Test Case về tài liệu SRS để bảo đảm **100% yêu cầu nghiệp vụ đều được kiểm thử**, không bỏ sót tính năng.
- **Bẫy 5: Severity vs Priority:** Severity là mức độ tác động kỹ thuật (do Tester xác định); Priority là mức độ khẩn cấp xử lý theo góc độ kinh doanh (do PM/PO xác định). Hai chỉ số này không nhất thiết phải tương đương (ví dụ: Logo công ty bị sai màu $\rightarrow$ Severity là Minor nhưng Priority là High vì ảnh hưởng thương hiệu).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Phân tích giá trị biên: 2-Point Boundary vs 3-Point Boundary

```text
  [KỸ THUẬT PHÂN TÍCH GIÁ TRỊ BIÊN (BOUNDARY VALUE ANALYSIS)]
  Miền không hợp lệ           MIỀN HỢP LỆ (VALID RANGE: [a, b])          Miền không hợp lệ
  (Invalid Low)               a                               b          (Invalid High)
  ────────────────)┌──────────────────────────────────────────────┐(────────────────
                   │                                              │
         a-1       │    a         a+1                    b-1      b   │      b+1
          ▲        │    ▲          ▲                      ▲       ▲   │       ▲
   (Ngoài biên dưới) (Biên dưới) (Trong biên dưới) (Trong biên trên) (Biên trên) (Ngoài biên trên)
```

- **Kỹ thuật biên 2 điểm (2-point boundary - Chuẩn cổ điển):**
  - Với mỗi ranh giới, chọn 2 giá trị: Giá trị ngay tại biên và giá trị nằm ngay sát ngoài biên.
  - Cho miền $[a, b]$, chọn 4 giá trị: $\{a-1, a, b, b+1\}$.
- **Kỹ thuật biên 3 điểm (3-point boundary - Chuẩn ISTQB hiện đại):**
  - Với mỗi ranh giới, chọn 3 giá trị: Giá trị ngay tại biên, giá trị sát trong biên, và giá trị sát ngoài biên.
  - Cho miền $[a, b]$, chọn 6 giá trị: $\{a-1, a, a+1, b-1, b, b+1\}$.
  - Bổ sung thêm 1 giá trị danh định nằm ở giữa miền (Nominal Value) để kiểm tra luồng thông thường $\rightarrow$ Tổng cộng 7 ca kiểm thử.

#### 2. Kiểm thử chuyển trạng thái (State Transition Testing)

```text
  [MÔ HÌNH MÁY TRẠNG THÁI HỮU HẠN (FSM) - HỆ THỐNG XÁC THỰC]
         ┌───────────────────┐
         │ 1. CHƯA ĐĂNG NHẬP │
         └─────────┬─────────┘
                   │
                   │ [Sự kiện]: Nhập đúng Username & Password
                   ▼
         ┌───────────────────┐
         │   2. ĐÃ XÁC THỰC  │ ─────── [Sự kiện]: Bấm Đặt hàng ───────► ┌───────────────────┐
         └─────────┬─────────┘                                          │ 4. CHỜ THANH TOÁN │
                   │                                                    └─────────┬─────────┘
                   │ [Sự kiện]: Hết phiên chờ (Timeout 15 phút)                   │
                   ▼                                                              │ [Sự kiện]: Hủy đơn
         ┌───────────────────┐                                                    │
         │ 3. KHÓA TẠM THỜI  │ ◄──────────────────────────────────────────────────┘
         └───────────────────┘
```

- **Bản chất kỹ thuật:** Hệ thống phần mềm được mô hình hóa thành một Máy trạng thái hữu hạn (`FSM - Finite State Machine`).
- Ca kiểm thử được thiết kế dựa trên:
  1. Trạng thái hiện tại (`Current State`).
  2. Sự kiện kích hoạt (`Event / Trigger`).
  3. Điều kiện bảo vệ (`Guard Condition`).
  4. Hành động thực thi (`Action`).
  5. Trạng thái đích kế tiếp (`Next State`).
- Giúp phát hiện các lỗi chuyển trạng thái bất hợp lệ (ví dụ: Chuyển từ "Chưa đăng nhập" thẳng sang "Đã thanh toán" mà bỏ qua bước xác thực).

#### 3. Đồ thị nguyên nhân - kết quả (Cause-Effect Graphing) sang Bảng quyết định
- **Cơ chế:** Khi hành vi của hệ thống phụ thuộc vào sự kết hợp phức tạp của nhiều điều kiện đầu vào đồng thời, đồ thị nguyên nhân - kết quả sử dụng các ký hiệu logic:
  - **원인 (Causes — Nguyên nhân):** Đại diện cho các điều kiện dữ liệu đầu vào.
  - **효과 (Effects — Kết quả):** Đại diện cho các hành vi hoặc trạng thái đầu ra của hệ thống.
  - Các toán tử logic liên kết: `AND (^)`, `OR (v)`, `NOT (~)`.
  - Các ràng buộc loại trừ giữa các nguyên nhân:
    * `E` (Exclusive): Tối đa chỉ 1 nguyên nhân mang giá trị True (loại trừ lẫn nhau).
    * `I` (Inclusive): Ít nhất 1 nguyên nhân phải mang giá trị True.
    * `O` (One and only one): Đúng duy nhất 1 nguyên nhân mang giá trị True.
    * `R` (Requires): Nếu nguyên nhân A là True thì nguyên nhân B bắt buộc phải là True.
- Đồ thị sau khi vẽ sẽ được chuyển đổi trực tiếp thành **의사결정 테이블 (Decision Table)** để sinh ra các Test Case hoàn chỉnh.

#### 4. Ma trận truy xuất nguồn gốc kiểm thử (RTM - Requirements Traceability Matrix)
- Trong các dự án phần mềm chuyên nghiệp, mỗi Test Case bắt buộc phải được liên kết ngược về tài liệu Yêu cầu (Software Requirements Specification - SRS).
- **Mục đích:** Bảo đảm **100% yêu cầu nghiệp vụ của khách hàng đều có ít nhất một Test Case bao phủ**, không để lọt bất kỳ tính năng nào chưa được kiểm tra trước khi bàn giao sản phẩm.

---

### 복습 체크리스트
- [ ] Định nghĩa Black-Box Testing là kiểm thử chức năng dựa trên đặc tả yêu cầu, không nhìn mã nguồn.
- [ ] Phân biệt 유효 동치 클래스 (Lớp hợp lệ) và 무효 동치 클래스 (Lớp không hợp lệ) trong kỹ thuật 동치 분할 (Equivalence Partitioning).
- [ ] Áp dụng đúng kỹ thuật 경계값 분석 (Boundary Value Analysis): Chọn các giá trị ngay tại biên, sát dưới biên và sát trên biên ($min-1, min, min+1, max-1, max, max+1$).
- [ ] Nhớ đồ thị nguyên nhân - kết quả (Cause-Effect Graphing) sử dụng logic Boolean để chuyển thành Bảng quyết định (Decision Table).
- [ ] Nhận diện kỹ thuật 오류 예측 (Error Guessing) dựa hoàn toàn vào kinh nghiệm và trực giác của kiểm thử viên.
- [ ] Kể tên tiêu chuẩn quốc tế về tài liệu kiểm thử: ISO/IEC/IEEE 29119-3.
- [ ] Liệt kê đủ các trường cấu tạo chuẩn của Test Case: ID, Item, Pre-conditions, Input, Expected Output.
- [ ] Phân biệt Test Case (phép thử cụ thể) và Test Scenario (kịch bản chuỗi nghiệp vụ liên hoàn).
- [ ] Nêu vai trò của Ma trận truy xuất nguồn gốc RTM (bảo đảm 100% yêu cầu được kiểm thử).
