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
| **Tiếp cận từ trên xuống** | **하향식 산정 (Top-Down)** | Ước lượng tổng ngân sách từ kinh nghiệm lịch sử, sau đó phân bổ xuống phân hệ con: Chuyên gia thẩm định (전문가 감정) và Phương pháp Delphi ẩn danh (델파이 기법). |
| **Tiếp cận từ dưới lên** | **상향식 산정 (Bottom-Up)** | Chia nhỏ hệ thống thành các tác vụ đơn vị, tính chi tiết từng phần rồi cộng dồn: Kỹ thuật LOC, Mô hình COCOMO, Mô hình Putnam, Điểm chức năng (FP). |

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
| **Sơ đồ PERT** | **PERT (3점 추정법)** | Áp dụng cho dự án mới chưa có tiền lệ (bất định cao). Ước lượng thời gian kỳ vọng trung bình: $t_e = (O + 4M + P)/6$ với $O$ là lạc quan, $M$ là khả dĩ nhất, $P$ là bi quan. |
| **Phương pháp CPM** | **CPM (Critical Path Method)** | Áp dụng cho dự án đã có tiền lệ, thời gian từng tác vụ là xác định. Tập trung tìm Đường găng (Critical Path). |

- **임계 경로 (Critical Path — Đường găng):**
  - **핵심 원리 (Nguyên tắc cốt lõi):**
    - [Tiếng Hàn]: `임계 경로는 네트워크 상에서 소요 시간이 가장 긴 경로이며, 프로젝트의 최소 완료 시간을 결정한다.`
    - [Tiếng Việt]: Đường găng là chuỗi các công việc có tổng thời gian dài nhất nối từ điểm bắt đầu đến điểm kết thúc, quyết định mốc thời gian hoàn thành tối thiểu của toàn bộ dự án.
    - [Tiếng Hàn]: `임계 경로 상의 작업들은 총 여유 시간(Total Float / Slack)이 0이다.`
    - [Tiếng Việt]: Các công việc trên đường găng có độ dự trữ thời gian bằng 0. Nếu bất kỳ công việc nào trên đường găng trễ $k$ ngày, ngày nghiệm thu toàn dự án sẽ bị trễ $k$ ngày tương ứng.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán ví dụ tính toán Man-Month và Thời gian dự án
- **Đề bài mẫu:** Dự án có quy mô dự kiến $30,000\text{ LOC}$. Năng suất lập trình viên là $1,000\text{ LOC/tháng}$. Nếu công ty bố trí $5$ nhân sự tham gia dự án, hãy tính:
  1. Công số nỗ lực (Effort).
  2. Thời gian phát triển dự án.
- **Lời giải:**
  1. $\text{Effort} = \frac{30,000}{1,000} = 30\text{ Man-Months}$ (cần 30 tháng công).
  2. $\text{Thời gian} = \frac{30\text{ MM}}{5\text{ người}} = 6\text{ tháng}$.

#### 2. Chi tiết công thức toán học mô hình COCOMO (Barry Boehm)
Mô hình COCOMO cơ bản (Basic COCOMO) ước tính công số nỗ lực (Effort) theo đơn vị $MM$ (Man-Month) và thời gian phát triển $TDEV$ (tháng) dựa trên quy mô dòng mã lệnh giao hàng $KDSI$ (Kilo Delivered Source Instructions, $1\text{ KDSI} = 1,000\text{ LOC}$):
$$\text{Effort (MM)} = a \times (\text{KDSI})^b$$
$$\text{TDEV (tháng)} = c \times (\text{Effort})^d$$

Hệ số thực nghiệm $(a, b, c, d)$ phụ thuộc vào 3 chế độ phát triển (Modes):

| Chế độ COCOMO | Tên tiếng Hàn & Ranh giới quy mô | Công thức nỗ lực (Effort) | Công thức thời gian (TDEV) | Đặc trưng môi trường phát triển |
| :--- | :--- | :--- | :--- | :--- |
| **Organic** | **조직형** ($\le 50\text{ KDSI}$) | $\text{MM} = 2.4 \times (\text{KDSI})^{1.05}$ | $\text{TDEV} = 2.5 \times (\text{MM})^{0.38}$ | Dự án nhỏ, đội ngũ giàu kinh nghiệm, môi trường quen thuộc, yêu cầu ổn định. |
| **Semi-Detached** | **반분리형** ($50 \sim 300\text{ KDSI}$) | $\text{MM} = 3.0 \times (\text{KDSI})^{1.12}$ | $\text{TDEV} = 2.5 \times (\text{MM})^{0.35}$ | Dự án trung bình, nhân lực hỗn hợp kinh nghiệm, tiện ích hệ thống, DBMS, trình thông dịch. |
| **Embedded** | **내장형** ($> 300\text{ KDSI}$) | $\text{MM} = 3.6 \times (\text{KDSI})^{1.20}$ | $\text{TDEV} = 2.5 \times (\text{MM})^{0.32}$ | Hệ thống thời gian thực, điều khiển nhúng, hàng không, quân sự, ràng buộc phần cứng khắt khe. |

- **Ý nghĩa của số mũ $b$ ($1.05 \rightarrow 1.12 \rightarrow 1.20$):**
  - Số mũ $b > 1$ phản ánh hiện tượng quy mô bất lợi (Diseconomies of Scale): khi hệ thống càng phình to và chuyển dần sang dạng Embedded, chi phí giao tiếp, quản lý phối hợp giữa các nhóm tăng theo hàm số mũ, khiến công số nỗ lực tăng vọt so với mức tăng tuyến tính của dòng code.
- **Ví dụ tính toán số liệu cụ thể:**
  - Giả sử một dự án thuộc chế độ Organic có quy mô $30\text{ KDSI}$ ($30,000$ dòng code).
  - Ước tính công số nỗ lực: $\text{Effort} = 2.4 \times (30)^{1.05} \approx 2.4 \times 35.65 \approx 85.56\text{ Man-Months}$.
  - Thời gian hoàn thành: $\text{TDEV} = 2.5 \times (85.56)^{0.38} \approx 2.5 \times 5.42 \approx 13.55\text{ tháng}$.
  - Số nhân lực trung bình cần bố trí: $\text{Staff} = \frac{\text{Effort}}{\text{TDEV}} = \frac{85.56}{13.55} \approx 6.3\text{ người}$.

#### 3. Mô hình Putnam và đường cong phân bố nhân lực Rayleigh-Norden
Mô hình Putnam dựa trên nghiên cứu thực nghiệm của Peter Norden và Lawrence Putnam về sự biến thiên của nhân lực trong toàn bộ vòng đời phát triển phần mềm:
- **Phương trình phần mềm Putnam (Putnam Software Equation):**
  $$S = C_k \times K^{1/3} \times t_d^{4/3}$$
  - $S$: Quy mô mã nguồn (số dòng lệnh giao hàng - Source Statements).
  - $C_k$: Hệ số công nghệ phản ánh môi trường phát triển (Technology Constant / State of Technology).
  - $K$: Tổng nỗ lực cho toàn bộ vòng đời dự án (tính bằng Man-Year hoặc Man-Month).
  - $t_d$: Thời gian phát triển dự án (tính bằng năm).
- **Phân bố nhân lực $y(t)$ theo đường cong Rayleigh:**
  $$y(t) = \frac{K}{t_d^2} \cdot t \cdot e^{-\frac{t^2}{2t_d^2}}$$

```text
  Nỗ lực nhân sự (Effort / Staffing)
    ^
    |                       [ĐỈNH NHÂN LỰC - PEAK EFFORT]
    |                          (Kiểm thử tích hợp & Hệ thống)
    |                                   /\
    |          (Lập trình mã hóa)      /  \
    |                  /\             /    \
    |                 /  \___________/      \
    |  (Thiết kế)    /                       \        (Vận hành & Bảo trì)
    |       /\      /                         \
    | _____/  \____/                           \________________________
    +--------------------------------------------------------------------> Thời gian (t)
    0               t_d (Bàn giao sản phẩm)           Vòng đời khai thác
```

- **Quy luật đề thi cần nhớ:**
  - Nỗ lực của dự án không bao giờ dàn đều hình chữ nhật mà khởi đầu chậm ở khâu phân tích/thiết kế, tăng mạnh và **đạt đỉnh (Peak)** tại giai đoạn kiểm thử tích hợp (Integration Testing), sau đó giảm nhanh khi bàn giao và kéo dài đuôi ở giai đoạn vận hành bảo trì.
  - Công cụ phần mềm thương mại tiêu biểu của mô hình Putnam là **SLIM (Software Life-cycle Management)**.

#### 4. Bài toán ví dụ tính thời gian kỳ vọng PERT
- **Đề bài mẫu:** Một tác vụ phân tích cơ sở dữ liệu có: Thời gian lạc quan $O = 4\text{ ngày}$, Thời gian khả dĩ nhất $M = 7\text{ ngày}$, Thời gian bi quan $P = 16\text{ ngày}$. Hãy tính thời gian kỳ vọng hoàn thành tác vụ $t_e$.
- **Lời giải:**
  $$t_e = \frac{O + 4M + P}{6} = \frac{4 + (4 \times 7) + 16}{6} = \frac{4 + 28 + 16}{6} = \frac{48}{6} = 8\text{ ngày}$$

#### 5. Sơ đồ mạng CPM/PERT và thuật toán xác định Đường găng (Critical Path)
Phương pháp CPM (Critical Path Method) sử dụng sơ đồ mạng công việc (Activity-on-Node hoặc Activity-on-Arrow) để quản lý phụ thuộc và thời gian:

- **Các đại lượng thời gian trong nút công việc:**
  - $ES$ (Earliest Start): Thời điểm bắt đầu sớm nhất có thể của công việc.
  - $EF$ (Earliest Finish): Thời điểm kết thúc sớm nhất: $EF = ES + \text{Duration}$.
  - $LS$ (Latest Start): Thời điểm bắt đầu muộn nhất để không làm trễ dự án: $LS = LF - \text{Duration}$.
  - $LF$ (Latest Finish): Thời điểm kết thúc muộn nhất có thể.
  - $\text{Total Float}$ (Độ dự trữ toàn phần / 여유 시간): $\text{Float} = LS - ES = LF - EF$.

- **Sơ đồ mạng mẫu minh họa:**

```text
                      +-------------------+            +--------------------+
                      |    Tác vụ B       |            |     Tác vụ D       |
                      |  Thiết kế CSDL    | ---------> | Lập trình Backend  |
                      | Thời lượng: 4 ngày|            | Thời lượng: 5 ngày |
                      +-------------------+            +--------------------+
                             ^                                    \
                            /                                      \
+---------------+   +-------------------+                           v   +-----------------+
|   Bắt đầu     |-->|    Tác vụ A       |                            -->|     Tác vụ F    |--> [ Kết thúc ]
|   (Node 1)    |   | Phân tích Yêu cầu |                               |Kiểm thử tích hợp|     (Node 6)
|  Ngày thứ 0   |   | Thời lượng: 3 ngày|                            -->|Thời lượng: 4 ngày|     (Ngày 16)
+---------------+   +-------------------+                           /   +-----------------+
                            \                                      /
                             v                                    /
                      +-------------------+            +--------------------+
                      |    Tác vụ C       |            |     Tác vụ E       |
                      | Thiết kế Giao diện| ---------> | Lập trình Frontend |
                      | Thời lượng: 2 ngày|            | Thời lượng: 3 ngày |
                      +-------------------+            +--------------------+
```

- **Phân tích tất cả các đường đi (Paths) từ Bắt đầu đến Kết thúc:**
  - **Đường đi 1:** $\text{Bắt đầu} \rightarrow A \rightarrow B \rightarrow D \rightarrow F \rightarrow \text{Kết thúc}$
    $$\text{Tổng thời gian} = 3 + 4 + 5 + 4 = 16\text{ ngày}$$
  - **Đường đi 2:** $\text{Bắt đầu} \rightarrow A \rightarrow C \rightarrow E \rightarrow F \rightarrow \text{Kết thúc}$
    $$\text{Tổng thời gian} = 3 + 2 + 3 + 4 = 12\text{ ngày}$$

- **Bảng tính toán chi tiết Forward Pass và Backward Pass:**

| Tác vụ | Thời lượng (D) | Bắt đầu sớm ($ES$) | Kết thúc sớm ($EF$) | Kết thúc muộn ($LF$) | Bắt đầu muộn ($LS$) | Độ dự trữ ($\text{Float}$) | Vị trí đường găng |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 3 ngày | 0 | 3 | 3 | 0 | $0 - 0 = 0$ | **Thuộc đường găng (Critical)** |
| **B** | 4 ngày | 3 | 7 | 7 | 3 | $3 - 3 = 0$ | **Thuộc đường găng (Critical)** |
| **C** | 2 ngày | 3 | 5 | 9 | 7 | $7 - 3 = 4$ | Nhánh phụ (Dự trữ 4 ngày) |
| **D** | 5 ngày | 7 | 12 | 12 | 7 | $7 - 7 = 0$ | **Thuộc đường găng (Critical)** |
| **E** | 3 ngày | 5 | 8 | 12 | 9 | $9 - 5 = 4$ | Nhánh phụ (Dự trữ 4 ngày) |
| **F** | 4 ngày | 12 | 16 | 16 | 12 | $12 - 12 = 0$ | **Thuộc đường găng (Critical)** |

- **Kết luận giải đề thi:**
  - **Đường găng (임계 경로 - Critical Path):** Là chuỗi $A \rightarrow B \rightarrow D \rightarrow F$ với tổng thời gian dài nhất là **$16\text{ ngày}$**.
  - **Thời gian hoàn thành dự án tối thiểu:** Bằng đúng độ dài đường găng là **$16\text{ ngày}$**.
  - **Đặc điểm sống còn:** Mọi công việc trên đường găng đều có $\text{Float} = 0$. Các tác vụ $C$ và $E$ có thể trễ tối đa $4\text{ ngày}$ mà không làm ảnh hưởng đến ngày nghiệm thu của toàn dự án.

---

### 복습 체크리스트
- [ ] Nhớ 3P quản lý dự án: People, Problem, Process (People là yếu tố quan trọng nhất).
- [ ] Nắm vững đặc trưng Delphi: Khảo sát chuyên gia ẩn danh (익명) qua nhiều vòng để đạt đồng thuận.
- [ ] Thuộc công thức LOC: $\text{Effort} = \frac{\text{LOC}}{\text{Năng suất}}$, $\text{Thời gian} = \frac{\text{Effort}}{\text{Nhân sự}}$.
- [ ] Phân biệt 3 chế độ COCOMO: 조직형 (Organic $\le 50\text{K}$), 반분리형 (Semi-Detached $\le 300\text{K}$), 내장형 (Embedded $> 300\text{K}$).
- [ ] Nhớ 5 thành phần Function Point: EI, EO, EQ, ILF, EIF (FP độc lập với ngôn ngữ lập trình).
- [ ] Thuộc công thức PERT: $t_e = \frac{O + 4M + P}{6}$.
- [ ] Khắc ghi định nghĩa Đường găng (Critical Path): Đường dài nhất trong sơ đồ mạng, quyết định thời gian tối thiểu của dự án, có Total Float = 0.
