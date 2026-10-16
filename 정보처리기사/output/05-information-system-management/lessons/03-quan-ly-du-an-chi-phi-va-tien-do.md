# 소프트웨어 프로젝트 관리: 비용 산정 및 일정 계획 (Quản lý dự án phần mềm: Ước tính chi phí COCOMO/FP & Lập tiến độ PERT/CPM)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 yếu tố cốt lõi của quản lý dự án phần mềm (**3P: People - Con người, Problem - Vấn đề, Process - Quy trình**).
- Làm chủ toàn diện các phương pháp ước tính chi phí phần mềm: Tiếp cận từ trên xuống (하향식: 전문가 감정, 델파이 기법) và Tiếp cận từ dưới lên (상향식: LOC, COCOMO, Putnam, Function Point).
- Thuộc lòng và vận dụng chính xác các công thức tính toán: Công số nhân tháng (Man-Month / MM), thời gian phát triển dự án, năng suất lao động theo LOC.
- Phân biệt chi tiết 3 chế độ phát triển trong mô hình **COCOMO** (Organic $\le 50\text{ KDSI}$, Semi-Detached $\le 300\text{ KDSI}$, Embedded $> 300\text{ KDSI}$) và 5 thành phần điểm chức năng **Function Point** (EI, EO, EQ, ILF, EIF).
- Thấu hiểu cơ chế quản lý tiến độ mạng: Công thức thời gian kỳ vọng 3 điểm của **PERT** ($t_e = \frac{O + 4M + P}{6}$), Sơ đồ thanh **Gantt Chart**, và xác định **Đường găng (임계 경로 - Critical Path)** với độ dự trữ thời gian bằng 0 (Total Float = 0).

## 핵심 키워드 (Từ khóa song ngữ)
- 프로젝트 3대 요소 (3P — People 인적 자원, Problem 문제/요구사항, Process 프로세스)
- 하향식 산정 기법 (Top-Down Estimation — 전문가 감정 기법, 델파이 기법 Delphi)
- 상향식 산정 기법 (Bottom-Up Estimation — LOC 기법, 수학적 산정 모형)
- LOC 기법 (Lines of Code — Công số Man-Month, Thời gian, Chi phí, Năng suất)
- COCOMO 모형 (Boehm — 조직형 Organic, 반분리형 Semi-Detached, 내장형 Embedded)
- 푸트남 모형 (Putnam Model — Rayleigh-Norden 곡선, SLIM 도구)
- 기능 점수 (FP - Function Point — Albrecht, 언어 독립적, EI, EO, EQ, ILF, EIF)
- PERT (Program Evaluation and Review Technique — 3점 추정법, 낙관치 O, 기대치 M, 비관치 P)
- CPM (Critical Path Method — 임계 경로, 확정적 일정 관리)
- 임계 경로 (Critical Path — 프로젝트 최장 경로, 최소 완료 기간, 총 여유 시간 0)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi xác định phương pháp luận từ [01-phuong-phap-luan-va-framework.md](01-phuong-phap-luan-va-framework.md) và mức độ tái sử dụng từ [02-tai-su-dung-va-cong-cu-case.md](02-tai-su-dung-va-cong-cu-case.md), người quản trị dự án (PM) phải lượng hóa nguồn lực: cần bao nhiêu tiền, bao nhiêu lập trình viên và bao lâu thì hoàn thành.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp toàn bộ công thức tính toán tài chính, ước lượng nhân công (LOC/COCOMO/FP) và các thuật toán lập lịch mạng (PERT/CPM/Critical Path) nhằm kiểm soát tiến độ và ngăn ngừa thất thoát ngân sách.
- **Dùng đi đâu (Forward Handoff):** Quy trình quản lý chi phí và tiến độ sau khi thiết lập sẽ được đánh giá độ trưởng thành theo các tiêu chuẩn quốc tế tại [04-tieu-chuan-chat-luong-va-cmmi.md](04-tieu-chuan-chat-luong-va-cmmi.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **3P Quản lý dự án:** Đề hỏi yếu tố quan trọng nhất $\rightarrow$ Luôn là **People (Con người / 인적 자원)**.
- **Kỹ thuật Delphi:** Từ khóa nhận diện là **"익명" (Ẩn danh)**, **"여러 차례 설문" (Nhiều vòng khảo sát)**, **"간사/조정자" (Điều phối viên tổng hợp)** nhằm loại bỏ ý kiến áp đặt của chuyên gia quyền lực.
- **COCOMO Modes (Phải nhớ ranh giới KDSI):**
  - $\le 50\text{ KDSI}$ (dự án nhỏ, quen thuộc) $\rightarrow$ **조직형 (Organic)**.
  - $> 50 \sim 300\text{ KDSI}$ (trung bình, tiện ích) $\rightarrow$ **반분리형 (Semi-Detached)**.
  - $> 300\text{ KDSI}$ (quy mô lớn, hệ thống nhúng, vũ khí, y tế) $\rightarrow$ **내장형 (Embedded)**.
  - *Bẫy đề thi:* COCOMO tuyệt đối **không có** chế độ mang tên "Sequential" hay "Distributed".
- **Function Point (FP):**
  - Đo lường kích thước phần mềm **độc lập với ngôn ngữ lập trình** (ngược với LOC phụ thuộc ngôn ngữ).
  - Phân biệt: **ILF (nội bộ)** vs **EIF (ngoại vi)**; **EI (vào)** vs **EO (ra có tính toán)** vs **EQ (tra cứu không tính toán)**.
- **PERT/CPM & Đường găng:**
  - Nhớ công thức $t_e = \frac{O + 4M + P}{6}$ (hệ số của $M$ luôn là $4$, mẫu số luôn là $6$).
  - **임계 경로 (Critical Path):** Là đường đi có **tổng thời gian dài nhất**, quyết định **thời gian ngắn nhất để hoàn thành dự án**, và có **여유 시간 = 0 (Float/Slack = 0)**.

---

## 소프트웨어 프로젝트 관리: 비용 산정 및 일정 계획

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Yếu tố nền tảng quản lý dự án (Project 3P)
- **1. People (사람 / 인적 자원):** Con người là yếu tố quan trọng nhất quyết định thành bại của dự án phần mềm.
- **2. Problem (문제 / 요구사항):** Làm rõ vấn đề nghiệp vụ và phạm vi yêu cầu khách hàng cần giải quyết.
- **3. Process (프로세스 / 절차):** Khung quy trình và các giai đoạn phát triển phần mềm được áp dụng.

#### 2. Phân loại phương pháp ước tính chi phí phần mềm

| Nhóm phương pháp | Tên tiếng Hàn & Anh | Cơ chế hoạt động & Đại diện tiêu biểu |
| :--- | :--- | :--- |
| **Tiếp cận từ trên xuống** | **하향식 산정 (Top-Down)** | Ước lượng tổng ngân sách dựa trên kinh nghiệm lịch sử của các dự án tương tự trước đây, sau đó phân bổ ngược xuống từng phân hệ con.<br>- **전문가 감정 기법 (Expert Judgement):** Nhờ 2-3 chuyên gia lão luyện phán đoán; ưu điểm nhanh nhưng mang nặng tính chủ quan.<br>- **델파이 기법 (Delphi Technique):** Các chuyên gia ước tính **ẩn danh (익명)** qua nhiều vòng khảo sát, người điều phối tổng hợp kết quả để loại bỏ sự chi phối của cá nhân uy thế nhất. |
| **Tiếp cận từ dưới lên** | **상향식 산정 (Bottom-Up)** | Chia nhỏ hệ thống thành các tác vụ/module đơn vị, tính toán chi phí chi tiết từng phần rồi cộng dồn lại.<br>- **LOC 기법:** Đếm dòng mã nguồn.<br>- **Mô hình toán học:** COCOMO, Putnam, Function Point (FP). |

#### 3. Công thức tính toán định lượng theo LOC (Lines of Code)
- **Công số nỗ lực (Effort / Man-Month):**
  $$\text{노력 (Man-Month)} = \frac{\text{총 LOC}}{\text{월간 1인당 생산 LOC}}$$
- **Thời gian phát triển dự án (Development Time):**
  $$\text{개발 기간 (개월)} = \frac{\text{노력 (Man-Month)}}{\text{투입 인원 (명)}}$$
- **Năng suất lao động trung bình (Productivity):**
  $$\text{생산성} = \frac{\text{총 LOC}}{\text{노력 (Man-Month)}}$$
- **Tổng chi phí phát triển (Development Cost):**
  $$\text{개발 비용} = \text{노력 (Man-Month)} \times \text{1인당 월평균 인건비}$$

#### 4. Các mô hình ước tính toán học kinh điển

##### A. Mô hình COCOMO (Barry Boehm)
Ước lượng công số dựa trên quy mô dòng lệnh giao hàng KDSI (1 KDSI = 1,000 dòng mã nguồn).
- **조직형 (Organic Mode):**
  - Quy mô: $\le 50\text{ KDSI}$ (5 vạn dòng).
  - Đặc điểm: Ứng dụng nghiệp vụ văn phòng nội bộ, môi trường quen thuộc, yêu cầu ổn định.
- **반분리형 (Semi-Detached Mode):**
  - Quy mô: $> 50 \sim 300\text{ KDSI}$ (30 vạn dòng).
  - Đặc điểm: Hệ thống giao dịch, tiện ích quản trị mạng, hệ điều hành cơ sở dữ liệu tầm trung.
- **내장형 (Embedded Mode):**
  - Quy mô: $> 300\text{ KDSI}$ (trên 30 vạn dòng).
  - Đặc điểm: Hệ thống nhúng thời gian thực (Real-time), vũ khí quân sự, điều khiển hàng không, thiết bị y tế; ràng buộc phần cứng và tiêu chuẩn an toàn cực kỳ khắt khe.

##### B. Mô hình Putnam (SLIM Tool)
- Dựa trên đường cong phân bố nỗ lực theo thời gian **Rayleigh-Norden**.
- Công số nỗ lực đạt đỉnh ở giai đoạn thử nghiệm tích hợp và giảm dần khi bàn giao.

##### C. Mô hình Điểm chức năng Function Point (Allan Albrecht)
- **Ưu điểm lớn nhất:** Đo lường kích thước chức năng độc lập với ngôn ngữ lập trình và công nghệ phần cứng.
- **5 nhóm thành phần chức năng đo lường:**
  1. **외부 입력 (EI - External Input):** Dữ liệu/lệnh điều khiển từ bên ngoài đi vào làm thay đổi tệp logic nội bộ.
  2. **외부 출력 (EO - External Output):** Dữ liệu được xử lý, tính toán rồi gửi ra ngoài (báo cáo, hóa đơn).
  3. **외부 조회 (EQ - External Inquiry):** Truy vấn tra cứu thông tin trực tiếp, không làm thay đổi dữ liệu và không yêu cầu tính toán chuyển đổi phức tạp.
  4. **내부 논리 파일 (ILF - Internal Logical File):** Nhóm dữ liệu nghiệp vụ logic do chính ứng dụng quản lý lưu trữ bên trong.
  5. **외부 연계 파일 (EIF - External Interface File):** Nhóm dữ liệu do ứng dụng khác quản lý nhưng hệ thống này có tham chiếu/đọc dữ liệu.

#### 5. Quản lý tiến độ dự án: PERT, CPM & Đường găng (Critical Path)

| Công cụ | Tên tiếng Hàn & Anh | Cơ chế vận hành & Đặc điểm nhận diện |
| :--- | :--- | :--- |
| **Biểu đồ Gantt** | **간트 차트 (Gantt Chart)** | Biểu đồ thanh ngang biểu diễn lịch trình từng tác vụ theo thời gian; trực quan dễ xem nhưng khó thấy quan hệ ràng buộc phụ thuộc phức tạp giữa các tác vụ. |
| **Sơ đồ PERT** | **PERT (3점 추정법)** | Áp dụng cho dự án mới **chưa có tiền lệ (bất định cao)**. Ước lượng thời gian kỳ vọng trung bình $t_e$ theo 3 kịch bản:<br>$$t_e = \frac{O + 4M + P}{6}$$<br>($O$: Lạc quan - Optimistic, $M$: Khả dĩ nhất - Most Likely, $P$: Bi quan - Pessimistic). |
| **Phương pháp CPM** | **CPM (Critical Path Method)** | Áp dụng cho dự án **đã có tiền lệ**, thời gian từng tác vụ là xác định. Tập trung tìm **Đường găng (Critical Path)**. |

- **임계 경로 (Critical Path — Đường găng):**
  - **핵심 원리 (Nguyên tắc cốt lõi):**
    - [Tiếng Hàn]: `임계 경로는 네트워크 상에서 소요 시간이 가장 긴 경로이며, 프로젝트의 최소 완료 시간을 결정한다.`
    - [Tiếng Việt]: Đường găng là chuỗi các công việc có tổng thời gian dài nhất nối từ điểm bắt đầu đến điểm kết thúc, quyết định mốc thời gian hoàn thành tối thiểu của toàn bộ dự án.
    - [Tiếng Hàn]: `임계 경로 상의 작업들은 총 여유 시간(Total Float / Slack)이 0이다.`
    - [Tiếng Việt]: Các công việc trên đường găng có độ dự trữ thời gian bằng 0. Nếu bất kỳ công việc nào trên đường găng trễ $k$ ngày, ngày nghiệm thu toàn dự án sẽ bị trễ $k$ ngày tương ứng.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Bài toán ví dụ tính toán Man-Month và Thời gian dự án
- **Đề bài mẫu:** Dự án có quy mô dự kiến $30,000\text{ LOC}$. Năng suất lập trình viên là $1,000\text{ LOC/tháng}$. Nếu công ty bố trí $5$ nhân sự tham gia dự án, hãy tính:
  1. Công số nỗ lực (Effort).
  2. Thời gian phát triển dự án.
- **Lời giải:**
  1. $\text{Effort} = \frac{30,000}{1,000} = 30\text{ Man-Months}$ (cần 30 tháng công).
  2. $\text{Thời gian} = \frac{30\text{ MM}}{5\text{ người}} = 6\text{ tháng}$.

#### Bài toán ví dụ tính thời gian kỳ vọng PERT
- **Đề bài mẫu:** Một tác vụ phân tích cơ sở dữ liệu có: Thời gian lạc quan $O = 4\text{ ngày}$, Thời gian khả dĩ nhất $M = 7\text{ ngày}$, Thời gian bi quan $P = 16\text{ ngày}$. Hãy tính thời gian kỳ vọng hoàn thành tác vụ $t_e$.
- **Lời giải:**
  $$t_e = \frac{O + 4M + P}{6} = \frac{4 + (4 \times 7) + 16}{6} = \frac{4 + 28 + 16}{6} = \frac{48}{6} = 8\text{ ngày}$$

---

### 복습 체크리스트
- [ ] Nhớ 3P quản lý dự án: People, Problem, Process (People là yếu tố quan trọng nhất).
- [ ] Nắm vững đặc trưng Delphi: Khảo sát chuyên gia ẩn danh (익명) qua nhiều vòng để đạt đồng thuận.
- [ ] Thuộc công thức LOC: $\text{Effort} = \frac{\text{LOC}}{\text{Năng suất}}$, $\text{Thời gian} = \frac{\text{Effort}}{\text{Nhân sự}}$.
- [ ] Phân biệt 3 chế độ COCOMO: 조직형 (Organic $\le 50\text{K}$), 반분리형 (Semi-Detached $\le 300\text{K}$), 내장형 (Embedded $> 300\text{K}$).
- [ ] Nhớ 5 thành phần Function Point: EI, EO, EQ, ILF, EIF (FP độc lập với ngôn ngữ lập trình).
- [ ] Thuộc công thức PERT: $t_e = \frac{O + 4M + P}{6}$.
- [ ] Khắc ghi định nghĩa Đường găng (Critical Path): Đường dài nhất trong sơ đồ mạng, quyết định thời gian tối thiểu của dự án, có Total Float = 0.
