# 모듈 설계, 결합도·응집도 및 설계 도구 (Thiết kế Module, Độ phụ thuộc Coupling, Độ gắn kết Cohesion và Công cụ thiết kế)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm mô-đun hóa (`모듈화`) và nguyên lý độc lập chức năng (`기능적 독립성`): quy tắc vàng tăng tối đa Độ gắn kết nội tại (`응집도↑`) và giảm tối thiểu Độ phụ thuộc (`결합도↓`).
- Thuộc nằm lòng thứ tự 7 cấp độ của `응집도 (Cohesion)` từ mạnh nhất đến yếu nhất bằng thần chú `기 - 순 - 교 - 절 - 시 - 논 - 우`.
- Thuộc nằm lòng thứ tự 6 cấp độ của `결합도 (Coupling)` từ yếu nhất (tốt nhất) đến mạnh nhất (xấu nhất) bằng thần chú `자 - 스 - 제 - 외 - 공 - 내`.
- Phân biệt bản chất và kỳ vọng thiết kế của hai chỉ số cấu trúc: `팬인 (Fan-In)` (kỳ vọng cao) vs `팬아웃 (Fan-Out)` (kỳ vọng thấp).
- Làm chủ 5 nguyên tắc đặc tả mô-đun dùng chung (`공통 모듈`); 3 quy tắc thiết kế bất biến của biểu đồ `N-S 차트 (Nassi-Schneiderman Chart)`; 2 phương pháp tái sử dụng (`합성 중심 vs 생성 중심`); và các loại mã hệ thống (`코드 설계`).

## 핵심 키워드 (Từ khóa)
- 모듈화 및 기능적 독립성 (Modularity & Functional Independence / 결합도↓, 응집도↑)
- 응집도 7단계 (Cohesion: 기능적 > 순차적 > 교환적 > 절차적 > 시간적 > 논리적 > 우연적)
- 결합도 6단계 (Coupling: 자료 < 스탬프 < 제어 < 외부 < 공통 < 내용 결합도)
- 팬인 vs 팬아웃 (Fan-In - 나를 호출 / 높게 설계 vs Fan-Out - 내가 호출 / 낮게 설계)
- 공통 모듈 5대 명세 원칙 (정확성, 명확성, 완전성, 일관성, 추적성)
- N-S 차트 (Nassi-Schneiderman Chart / 상자 다이어그램 / 화살표 없음 / GOTO 없음)
- 재사용 (Reuse: 합성 중심 - Block building vs 생성 중심 - Pattern/Rule-based)
- 코드 설계 (Code: 순차, 블록, 10진, 그룹 분류, 표의 숫자, 연상 코드)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ [07-huong-doi-tuong-va-nguyen-ly-solid.md](07-huong-doi-tuong-va-nguyen-ly-solid.md), các nguyên tắc OOP và SOLID (đặc biệt là SRP và DIP) hướng đến việc xây dựng các lớp độc lập, có trách nhiệm rõ ràng. Để lượng hóa và đánh giá chất lượng thiết kế của các lớp và module này, kỹ sư phần mềm sử dụng hai thước đo kinh điển là Coupling và Cohesion.
- **Đang giải quyết gì (Current Problem):** Bài học này trang bị hệ thống phân loại định lượng toàn diện để đo lường mức độ phụ thuộc giữa các thành phần phần mềm, đưa ra các phương án tối ưu hóa cấu trúc gọi hàm (Fan-in/Fan-out), chuẩn hóa việc xây dựng module dùng chung và trực quan hóa logic thuật toán bằng sơ đồ khối chuẩn mực N-S Chart.
- **Dùng đi đâu (Forward Handoff):** Khi đã nắm vững cách thiết kế một module độc lập có Cohesion cao và Coupling thấp, bước tiếp theo là nâng cấp lên các giải pháp thiết kế kiến trúc mức đối tượng đã được chứng minh hiệu quả qua hàng thập kỷ: 23 Mẫu thiết kế GoF. Toàn bộ kiến thức bài này làm nền tảng trực tiếp cho [09-design-patterns-gof.md](09-design-patterns-gof.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng 2 câu thần chú thi trắc nghiệm sống còn: Thứ tự Cohesion **Kì - Sun - Kiều - Chul - Shi - Non - U** (`기 - 순 - 교 - 절 - 시 - 논 - 우`) và Thứ tự Coupling **Tử - Stamp - Chế - Ngoại - Công - Nội** (`자 - 스 - 제 - 외 - 공 - 내`); quy tắc Fan-In cao, Fan-Out thấp; và 3 điều cấm kỵ của N-S Chart.
- Đọc TẦNG B để phân tích ví dụ mã nguồn minh họa sự khác biệt nguy hiểm giữa Common Coupling (dùng biến toàn cục) và Content Coupling (can thiệp nội bộ).

---

## 모듈 설계, 결합도·응집도 및 설계 도구

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tính độc lập của Mô-đun (Functional Independence)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `모듈의 독립성은 결합도(Coupling)와 응집도(Cohesion)에 의해 측정되며, 독립성을 높이기 위해서는 결합도는 약하게(낮게), 응집도는 강하게(높게) 설계해야 한다.`
  - [Tiếng Việt]: Tính độc lập chức năng của mô-đun được đo lường bằng hai chỉ số: Độ kết hợp (Coupling) và Độ gắn kết (Cohesion). Để tối đa hóa tính độc lập, dễ bảo trì và tái sử dụng, quy tắc vàng là: **Kết hợp phải YẾU (thấp), Gắn kết phải MẠNH (cao)**.

---

#### 2. 7 Cấp độ 응집도 (Cohesion — Độ gắn kết nội tại)
- **Định nghĩa:** Là thước đo mức độ liên kết chặt chẽ và tập trung vào một mục đích chung duy nhất của các phần tử bên trong cùng một mô-đun. **응집도는 높을수록 (강할수록) 품질이 좋다**.
- **Thứ tự 7 cấp độ từ Mạnh nhất (Tốt nhất) $\rightarrow$ Yếu nhất (Kém nhất):**
  $$\text{기능적 (Functional)} > \text{순차적 (Sequential)} > \text{통신적/교환적 (Communicational)} > \text{절차적 (Procedural)} > \text{시간적 (Temporal)} > \text{논리적 (Logical)} > \text{우연적 (Coincidental)}$$
- **Biểu đồ phân cấp Cohesion (Độ gắn kết nội tại):**

```text
  ▲  [CAO / TỐT]  1. 기능적 (Functional)        - Duy nhất 1 chức năng chuyên biệt (TỐT NHẤT)
  │               2. 순차적 (Sequential)        - Output của bước này là Input của bước sau
  │               3. 통신/교환적 (Communicational) - Thao tác trên cùng cấu trúc dữ liệu I/O
  │               4. 절차적 (Procedural)        - Thực thi theo thứ tự các bước điều khiển
  │               5. 시간적 (Temporal)          - Gom việc thực hiện cùng một thời điểm (init/exit)
  │               6. 논리적 (Logical)           - Gom các việc tương tự, rẽ nhánh qua cờ (Flag)
  ▼  [THẤP / XẤU] 7. 우연적 (Coincidental)      - Gom ngẫu nhiên, không liên quan (TỆ NHẤT)
```

- **Mẹo ghi nhớ thần chú:**
  - Từ cao xuống thấp: **기 - 순 - 통 - 절 - 시 - 논 - 우** (*Kỳ - Thuận - Thông - Tiết - Thời - Luận - Ngẫu*).
  - Từ thấp lên cao: **우 - 논 - 시 - 절 - 통 - 순 - 기** (*Ngẫu - Luận - Thời - Tiết - Thông - Thuận - Kỳ*).

| Cấp độ 응집도 | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Nhận diện đề thi |
|:---|:---|:---|
| **1. 기능적 (Mạnh nhất)** | `기능적 응집도` (Functional Cohesion) | [Hàn/Anh]: `모듈 내부의 모든 기능 요소들이 단 하나의 단일 기능을 수행하는 경우.` / [Tiếng Việt]: Tất cả các phần tử bên trong module cùng phối hợp để thực hiện **DUY NHẤT MỘT CHỨC NĂNG NGHIỆP VỤ** (ví dụ: hàm tính căn bậc hai `sqrt(x)`). |
| **2. 순차적** | `순차적 응집도` (Sequential Cohesion) | [Hàn/Anh]: `모듈 내 하나의 활동으로부터 나온 출력 데이터를 그 다음 활동의 입력 데이터로 사용하는 경우.` / [Tiếng Việt]: **Đầu ra của thao tác này trở thành đầu vào trực tiếp của thao tác kế tiếp** bên trong module (ví dụ: Đọc file $\rightarrow$ Phân tích cú pháp). |
| **3. 교환적 / 통신적** | `통신적(교환적) 응집도` (Communicational Cohesion) | [Hàn/Anh]: `동일한 입력 자료나 출력 자료를 사용하여 서로 다른 기능을 수행하는 경우.` / [Tiếng Việt]: Các phần tử **thao tác trên CÙNG MỘT DỮ LIỆU ĐẦU VÀO hoặc ĐẦU RA** nhưng thực hiện các mục đích khác nhau. |
| **4. 절차적** | `절차적 응집도` (Procedural Cohesion) | [Hàn/Anh]: `모듈 내의 기능들이 순차적으로 수행되지만, 데이터가 아닌 제어 흐름에 따라 순서대로 실행되는 경우.` / [Tiếng Việt]: Các thao tác được thực hiện **theo một trình tự các bước định trước** theo luồng điều khiển của thuật toán. |
| **5. 시간적** | `시간적 응집도` (Temporal Cohesion) | [Hàn/Anh]: `특정 시간에 처리되어야 하는 활동들을 한 모듈에 모아 놓은 경우.` / [Tiếng Việt]: Các thao tác được gom chung chỉ vì chúng **cùng được thực thi tại CÙNG MỘT THỜI ĐIỂM** (ví dụ: hàm khởi tạo hệ thống `initialize()`, hàm đóng file khi tắt máy). |
| **6. 논리적** | `논리적 응집도` (Logical Cohesion) | [Hàn/Anh]: `논리적으로 유사한 기능을 수행하지만 서로 다른 작업을 하는 요소들이 모여 있는 경우.` / [Tiếng Việt]: Các thao tác có tính chất tương tự nhau được gom chung và **chọn thực thi thông qua một cờ tham số (Flag)** (ví dụ: hàm `output(type)` vừa in ra giấy vừa ghi ra file tùy vào cờ type). |
| **7. 우연적 (Yếu nhất)** | `우연적 응집도` (Coincidental Cohesion) | [Hàn/Anh]: `모듈 내부의 요소들이 서로 아무런 관련성 없이 우연히 모여 있는 경우.` / [Tiếng Việt]: Các phần tử được gom chung vào module **hoàn toàn ngẫu nhiên**, không có bất kỳ mối liên hệ logic, dữ liệu hay thời gian nào. Chất lượng tệ nhất. |

---

#### 3. 6 Cấp độ 결합도 (Coupling — Độ phụ thuộc giữa các module)
- **Định nghĩa:** Là thước đo mức độ phụ thuộc lẫn nhau giữa các mô-đun phần mềm. **결합도는 낮을수록 (약할수록) 품질이 좋다**.
- **Thứ tự 6 cấp độ từ Yếu nhất (Tốt nhất) $\rightarrow$ Mạnh nhất (Xấu nhất):**
  $$\text{자료 (Data)} < \text{스탬프 (Stamp)} < \text{제어 (Control)} < \text{외부 (External)} < \text{공통 (Common)} < \text{내용 (Content)}$$
- **Biểu đồ phân cấp Coupling (Độ phụ thuộc kết nối):**

```text
  ▲  [CAO / XẤU]  6. 내용 결합도 (Content)  - Can thiệp trực tiếp nội bộ/mã lệnh của module khác (TỆ NHẤT)
  │               5. 공통 결합도 (Common)   - Dùng chung biến toàn cục (Global Variables)
  │               4. 외부 결합도 (External) - Phụ thuộc định dạng/giao thức thiết bị bên ngoài
  │               3. 제어 결합도 (Control)  - Truyền cờ điều khiển (Flag) can thiệp luồng rẽ nhánh
  │               2. 스탬프 결합도 (Stamp)   - Truyền cả cấu trúc dữ liệu (Object/Record) dù chỉ dùng 1 phần
  ▼  [THẤP / TỐT] 1. 자료 결합도 (Data)    - Chỉ truyền tham số giá trị đơn nguyên (Primitive) (TỐT NHẤT)
```

- **Mẹo ghi nhớ thần chú:**
  - Từ thấp (tốt) lên cao (xấu): **자 - 스 - 제 - 외 - 공 - 내** (*Tư - Stamp - Chế - Ngoại - Công - Nội*).
  - Từ cao (xấu) xuống thấp (tốt): **내 - 공 - 외 - 제 - 스 - 자** (*Nội - Công - Ngoại - Chế - Stamp - Tư*).

| Cấp độ 결합도 | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Nhận diện đề thi |
|:---|:---|:---|
| **1. 자료 결합도 (Tốt nhất / Yếu nhất)** | `자료 결합도` (Data Coupling) | [Hàn/Anh]: `모듈 간의 인터페이스가 오직 파라미터(단순 자료값)를 통해서만 이루어지는 경우.` / [Tiếng Việt]: Các module chỉ trao đổi với nhau bằng **các tham số giá trị đơn giản (Primitive parameters: int, float, string)**. Không chia sẻ cấu trúc dữ liệu phức tạp. Tốt nhất. |
| **2. 스탬프 결합도** | `스탬프 결합도` (Stamp Coupling) | [Hàn/Anh]: `모듈 간의 인터페이스로 배열이나 레코드 등의 동일한 자료구조가 전달되는 경우.` / [Tiếng Việt]: Các module truyền cho nhau **CẢ MỘT CẤU TRÚC DỮ LIỆU TỔNG THỂ** (Object, Record, Struct), trong khi module nhận chỉ thực sự dùng một vài trường nhỏ bên trong cấu trúc đó. |
| **3. 제어 결합도** | `제어 결합도` (Control Coupling) | [Hàn/Anh]: `한 모듈이 다른 모듈의 내부 논리 흐름을 제어하기 위해 제어 신호(플래그)를 전달하는 경우.` / [Tiếng Việt]: Module này truyền **cờ điều khiển (Control Flag)** sang module kia để trực tiếp chi phối luồng logic rẽ nhánh bên trong module đó. |
| **4. 외부 결합도** | `외부 결합도` (External Coupling) | [Hàn/Anh]: `모듈들이 외부에서 도입된 데이터 포맷, 통신 프로토콜, 디바이스 인터페이스를 공유하는 경우.` / [Tiếng Việt]: Các module cùng chia sẻ và phụ thuộc vào một **định dạng dữ liệu hoặc giao thức bên ngoài** hệ thống. |
| **5. 공통 결합도** | `공통 결합도` (Common Coupling) | [Hàn/Anh]: `여러 모듈이 하나의 공통 데이터 영역(전역 변수)을 공유하여 사용하는 경우.` / [Tiếng Việt]: Các module cùng truy cập và chia sẻ **MỘT VÙNG DỮ LIỆU TOÀN CỤC (Global Variables)**. Một module sửa biến toàn cục có thể làm sập các module khác. |
| **6. 내용 결합도 (Tệ nhất / Mạnh nhất)** | `내용 결합도` (Content Coupling) | [Hàn/Anh]: `한 모듈이 다른 모듈의 내부 자료나 명령어를 직접 참조하거나 수정하는 경우.` / [Tiếng Việt]: Module này **can thiệp trực tiếp vào mã nguồn nội bộ hoặc địa chỉ nhớ của module khác**. Phá vỡ hoàn toàn tính đóng gói. Tệ nhất. |

---

#### 4. Chỉ số kiểm soát kiến trúc: Fan-In và Fan-Out

| Tiêu chí | 팬인 (Fan-In — Luồng gọi vào) | 팬아웃 (Fan-Out — Luồng gọi ra) |
|:---|:---|:---|
| **Bản chất** | Số lượng mô-đun cấp trên gọi đến mô-đun hiện tại (`나를 호출하는 모듈의 수`) | Số lượng mô-đun cấp dưới mà mô-đun hiện tại gọi đến (`내가 호출하는 모듈의 수`) |
| **Hình vẽ sơ đồ** | Số mũi tên trỏ **VÀO** nút mô-đun đó | Số mũi tên trỏ **RA** từ nút mô-đun đó |
| **Kỳ vọng thiết kế** | **NÊN CAO (높게 설계)** | **NÊN THẤP (낮게 설계)** |
| **Ý nghĩa kỹ thuật** | Fan-In cao thể hiện mô-đun có **tính tái sử dụng tốt (재사용성 우수)**. Tuy nhiên, nếu Fan-In quá cao thì khi module này lỗi sẽ ảnh hưởng diện rộng. | Fan-Out quá cao thể hiện mô-đun đang **ôm đồm quá nhiều việc, phụ thuộc phức tạp**; cần phân rã thành các mô-đun trung gian. |

---

#### 5. Công cụ thiết kế trực quan: N-S 차트 (Nassi-Schneiderman Chart)
- **Đặc trưng cốt lõi:** Là biểu đồ trực quan hóa logic thuật toán dưới dạng **các khối hộp chữ nhật lồng ghép (Box Diagram / Chapin Chart)**.
- **3 QUY TẮC THIẾT KẾ BẤT BIẾN TRONG ĐỀ THI:**
  1. `화살표 미사용 (Tuyệt đối KHÔNG dùng mũi tên)`: Luồng điều khiển luôn mặc định chảy từ trên xuống dưới trong từng ô hộp.
  2. `GOTO문 배제 (Tuyệt đối KHÔNG dùng lệnh GOTO)`: Ngăn chặn việc nhảy luồng tùy tiện, triệt để tuân thủ lập trình có cấu trúc (Structured Programming).
  3. `단일 입구와 단일 출구 (Single Entry - Single Exit)`: Mỗi khối cấu trúc chỉ có duy nhất một điểm vào ở đỉnh trên và một điểm ra ở đáy dưới.
- Biểu diễn đầy đủ 3 cấu trúc điều khiển cơ bản: **Tuần tự (순차), Lựa chọn (선택), Lặp lại (반복)**.

---

#### 6. Tái sử dụng (Reuse) và Hệ thống Mã (Code Design)

##### A. Tái sử dụng phần mềm (재사용 - Software Reuse)
- **2 Phương pháp tái sử dụng cốt lõi:**
  - `합성 중심 (Composition-based — Tái sử dụng hướng tổng hợp)`: Lắp ghép các khối component phần mềm đã có sẵn giống như trò chơi xếp hình Lego (Block-building approach).
  - `생성 중심 (Generation-based — Tái sử dụng hướng sinh mã)`: Tự động sinh ra mã nguồn mới dựa trên các khuôn mẫu và quy tắc đặc tả trừu tượng (Pattern/Rule-based approach).

##### B. Thiết kế hệ thống mã (코드 설계 - Code Design)
- **Các loại mã thường gặp trong đề thi:**
  - `순차 코드 (Sequential Code - Mã tuần tự)`: Gán số liên tục theo thứ tự phát sinh (1, 2, 3...).
  - `블록 코드 (Block Code - Mã khối)`: Dành riêng từng khoảng số cho từng nhóm đối tượng (ví dụ: 100~199 là phòng Hành chính, 200~299 là phòng Kỹ thuật).
  - `10진 코드 (Decimal Code - Mã thập phân)`: Phân cấp theo hệ thập phân Dewey (ví dụ: 000 $\rightarrow$ 010 $\rightarrow$ 011).
  - `그룹 분류 코드 (Group Classification Code - Mã phân nhóm)`: Chia nhỏ mã theo cấu trúc Lớn - Vừa - Nhỏ (ví dụ: 01-03-05).
  - `표의 숫자 코드 (Significant Digit Code - Mã số có ý nghĩa)`: Dùng chính thông số vật lý của đối tượng làm mã (ví dụ: Bóng đèn 220V-60W $\rightarrow$ mã 22060).
  - `연상 코드 (Mnemonic Code - Mã liên tưởng)`: Dùng chữ cái viết tắt gợi nhớ trực tiếp đến tên sản phẩm (ví dụ: TV-42, TV-55).

#### 7. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Thứ tự 응집도):** Đề thi trắc nghiệm hay đảo vị trí giữa `순차적 (Sequential)` và `교환/통신적 (Communicational)`. Nhớ chắc chắn: **기 $\rightarrow$ 순 $\rightarrow$ 통 $\rightarrow$ 절 $\rightarrow$ 시 $\rightarrow$ 논 $\rightarrow$ 우**.
- **Bẫy 2 (Thứ tự 결합도):** Đề hỏi *"Loại kết hợp nào có chất lượng tốt nhất / độ phụ thuộc yếu nhất?"* $\rightarrow$ Đáp án là **자료 결합도 (Data Coupling)**. Hỏi *"Loại nào xấu nhất / phụ thuộc mạnh nhất?"* $\rightarrow$ Đáp án là **내용 결합도 (Content Coupling)**.
- **Bẫy 3 (N-S Chart):** Đề hỏi *"Đặc điểm nào sau đây SAI về biểu đồ N-S?"* $\rightarrow$ Đáp án sai thường là: *"Sử dụng các mũi tên có điều kiện để biểu diễn luồng dữ liệu"* (N-S Chart **tuyệt đối không dùng mũi tên**).
- **Bẫy 4 (Kỳ vọng Fan-In / Fan-Out):**
  - Fan-In (luồng gọi vào) $\rightarrow$ **Nên CAO (높게 설계)**.
  - Fan-Out (luồng gọi ra) $\rightarrow$ **Nên THẤP (낮게 설계)**.

- **💡 Khẩu quyết thần chú đề thi:**
  - Quy tắc vàng thiết kế module: **고응저결 (Cao Ứng Thấp Kết)** $\rightarrow$ 응집도 높게(Cohesion High), 결합도 낮게(Coupling Low).
  - Cohesion từ thấp đến cao: **우-논-시-절-통-순-기** (`우`연 $\rightarrow$ `논`리 $\rightarrow$ `시`간 $\rightarrow$ `절`차 $\rightarrow$ `통`신 $\rightarrow$ `순`차 $\rightarrow$ `기`능).
  - Cohesion từ cao xuống thấp: **기-순-통-절-시-논-우**.
  - Coupling từ thấp (tốt) đến cao (xấu): **자-스-제-외-공-내** (`자`료 $\rightarrow$ `스`탬프 $\rightarrow$ `제`어 $\rightarrow$ `외`부 $\rightarrow$ `공`통 $\rightarrow$ `내`용).
  - Coupling từ cao (xấu) xuống thấp (tốt): **내-공-외-제-스-자**.
  - Câu chốt ghi nhớ: "Cohesion càng cao càng tốt theo Kì-Sun-Thông-Chul-Shi-Non-U; Coupling càng thấp càng tốt theo Tử-Stamp-Chế-Ngoại-Công-Nội; Fan-In cao tái sử dụng, Fan-Out thấp giảm rối ren; N-S ba không: không tên, không GOTO, một vào một ra".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Minh họa mã nguồn: Sự khác biệt giữa Common Coupling và Content Coupling
- **Common Coupling (공통 결합도 — Dùng biến toàn cục):**
  ```c
  int g_discountRate = 10; // Biến toàn cục dùng chung cho cả hệ thống
  void ModuleA() { g_discountRate = 20; } // Module A tự ý đổi giá trị
  void ModuleB() { int price = 100 * (100 - g_discountRate) / 100; } // Module B bị tính sai mà không biết lý do!
  ```
  Khi hàng chục module cùng đọc/ghi một biến toàn cục, việc lần vết lỗi (Debugging) trở thành cơn ác mộng.
- **Content Coupling (내용 결합도 — Can thiệp nội bộ):**
  Xảy ra khi Module A trực tiếp nhảy vào một nhãn địa chỉ bên trong thân hàm của Module B (sử dụng lệnh `goto`), hoặc trực tiếp thay đổi giá trị của một biến Private bên trong Module B mà không thông qua Setter/Getter. Khi Module B thay đổi tên biến hoặc cấu trúc nội bộ, Module A lập tức bị sập.

#### 2. Kỹ thuật phân rã khi Fan-Out quá cao
- Khi một module có Fan-Out lớn hơn 7 (gọi ra quá 7 module cấp dưới), nó vi phạm "Quy luật số 7 kỳ diệu" của tâm lý học nhận thức (Miller's Law). Module này sẽ trở nên cực kỳ phức tạp và khó kiểm thử.
- **Giải pháp chuẩn hóa kiến trúc:** Đưa vào một **Mô-đun điều phối trung gian (Coordinator / Facade Module)** ở giữa để gom nhóm các lời gọi hàm theo từng chức năng nghiệp vụ, từ đó đưa chỉ số Fan-Out của module gốc về mức an toàn (thường từ 2 đến 4).

---

### 복습 체크리스트
- [ ] Nhớ quy tắc vàng của tính độc lập mô-đun: 응집도 (Cohesion) phải CAO, 결합도 (Coupling) phải THẤP.
- [ ] Đọc vanh vách 7 cấp độ Cohesion từ mạnh đến yếu: 기능 $\rightarrow$ 순차 $\rightarrow$ 교환 $\rightarrow$ 절차 $\rightarrow$ 시간 $\rightarrow$ 논리 $\rightarrow$ 우연.
- [ ] Đọc vanh vách 6 cấp độ Coupling từ yếu (tốt) đến mạnh (xấu): 자료 $\rightarrow$ 스탬프 $\rightarrow$ 제어 $\rightarrow$ 외부 $\rightarrow$ 공통 $\rightarrow$ 내용.
- [ ] Phân biệt được Fan-In (luồng gọi vào, nên cao) và Fan-Out (luồng gọi ra, nên thấp).
- [ ] Nhớ 5 nguyên tắc đặc tả công thông mô-đun: chính xác (정확성), rõ ràng (명확성), đầy đủ (완전성), nhất quán (일관성), truy vết (추적성).
- [ ] Thuộc 3 quy tắc thiết kế của N-S Chart: không dùng mũi tên, không dùng GOTO, cấu trúc 1 lối vào - 1 lối ra.
- [ ] Phân biệt được tái sử dụng 합성 중심 (lắp ghép Component Lego) và 생성 중심 (sinh mã theo mẫu).
- [ ] Nhận diện được đặc trưng của các loại mã: 순차 (tuần tự), 블록 (phân khoảng số), 10진 (thập phân Dewey), 표의 숫자 (thông số vật lý), 연상 (viết tắt gợi nhớ).
