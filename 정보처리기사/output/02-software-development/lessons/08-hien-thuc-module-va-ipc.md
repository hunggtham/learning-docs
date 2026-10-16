# 모듈 구현과 프로세스 간 통신 (Hiện thực đơn vị module, IPC và tái sử dụng)

## 학습 목표
- Nắm vững định nghĩa đơn vị module (`단위 모듈 / Unit Module`) và nguyên tắc thiết kế tối ưu: Độ gắn kết nội bộ cao (`고응집도 / High Cohesion`) và Độ phụ thuộc ghép nối thấp (`저결합도 / Low Coupling`).
- Thuộc lòng thứ bậc sắp xếp 6 cấp độ ghép nối (Coupling từ tốt nhất đến tồi tệ nhất): Data $\lt$ Stamp $\lt$ Control $\lt$ External $\lt$ Common $\lt$ Content.
- Thuộc lòng thứ bậc sắp xếp 7 cấp độ gắn kết (Cohesion từ yếu nhất đến mạnh nhất): Coincidental $\lt$ Logical $\lt$ Temporal $\lt$ Procedural $\lt$ Communicational $\lt$ Sequential $\lt$ Functional.
- Phân tích cơ chế và nhận diện qua đề thi 5 phương thức giao tiếp liên tiến trình IPC: Bộ nhớ chia sẻ (`공유 메모리`), Ổ cắm mạng (`소켓`), Cờ hiệu đồng bộ (`세마포어`), Đường ống (`파이프`), và Hàng đợi thông điệp (`메시지 큐`).
- So sánh hai trường phái tái sử dụng phần mềm: Hướng tổng hợp linh kiện (`합성 중심`) vs Hướng tạo sinh từ đặc tả (`생성 중심`), cùng 4 hoạt động tái kỹ nghệ phần mềm.

## 핵심 키워드
- 단위 모듈 (Đơn vị Module / Unit Module / 독립 컴파일)
- 결합도 (Độ ghép nối / Coupling / 자료 Data, 스탬프 Stamp, 제어 Control, 외부 External, 공통 Common, 내용 Content)
- 응집도 (Độ gắn kết / Cohesion / 우연적, 논리적, 시간적, 절차적, 통신적, 순차적, 기능적 Functional)
- IPC (프로세스 간 통신 / 공유 메모리 Shared Memory, 소켓 Socket, 세마포어 Semaphore, 파이프 Pipe, 메시지 큐)
- 소프트웨어 재사용 (Tái sử dụng / 합성 중심 Composition, 생성 중심 Generation)
- 재공학 (Tái kỹ nghệ / 분석 Analysis, 재구성 Restructuring, 역공학 Reverse Engineering, 이관 Migration)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [07-co-so-du-lieu-va-toi-uu-truy-van.md](07-co-so-du-lieu-va-toi-uu-truy-van.md), chúng ta đã hoàn tất Chương 1 về cấu trúc dữ liệu và tối ưu truy vấn CSDL.
- **Đang giải quyết gì (Current Problem):** Bài học này mở màn Chương 2 về tích hợp hệ thống, giải quyết bài toán phân rã phần mềm thành các đơn vị module độc lập, đo lường chất lượng thiết kế qua Coupling/Cohesion và thiết lập các kênh truyền thông liên tiến trình IPC an toàn.
- **Dùng đi đâu (Forward Handoff):** Khi các module phát triển thành các hệ thống phân tán đa nền tảng quy mô doanh nghiệp, bài học chuyển tiếp sang [09-tich-hop-he-thong-eai-esb.md](09-tich-hop-he-thong-eai-esb.md) để khảo sát kiến trúc tích hợp EAI/ESB và Web Service.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng hai chuỗi thứ bậc Coupling và Cohesion (câu hỏi trắc nghiệm thi cử chắc chắn 100% xuất hiện), bảng nén 5 phương thức IPC và cặp đối xứng Lego vs In 3D của Tái sử dụng phần mềm.
- Đọc TẦNG B để hiểu sâu bản chất kỹ thuật của từng loại Coupling/Cohesion và cơ chế cô lập bộ nhớ tiến trình của hệ điều hành.

---

## 모듈 구현과 프로세스 간 통신

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Nguyên tắc vàng thiết kế Module
$$\mathbf{\text{Chất lượng tối ưu}} \Longleftrightarrow \mathbf{\text{응집도 (Cohesion) CỰC ĐẠI}} + \mathbf{\text{결합도 (Coupling) CỰC TIỂU}}$$

#### 2. Chuỗi thứ bậc Coupling (Độ ghép nối phụ thuộc giữa các module)
Càng ít phụ thuộc nhau càng tốt (Sắp xếp từ **Tốt nhất $\rightarrow$ Tồi tệ nhất**):
$$\mathbf{자료(Data) \lt 스탬프(Stamp) \lt 제어(Control) \lt 외부(External) \lt 공통(Common) \lt 내용(Content)}$$
- **자료 결합도 (Data - Tốt nhất):** Chỉ trao đổi tham số dữ liệu đơn giản.
- **스탬프 결합도 (Stamp):** Truyền cả cấu trúc dữ liệu Record/Struct dù chỉ dùng vài trường.
- **제어 결합도 (Control):** Truyền cờ hiệu (Flag) can thiệp logic rẽ nhánh module khác.
- **외부 결합도 (External):** Chia sẻ định dạng giao thức hoặc file ngoài.
- **공통 결합도 (Common):** Nhiều module cùng đọc/ghi vào **vùng biến toàn cục (Global Variable)**.
- **내용 결합도 (Content - Tồi tệ nhất):** Can thiệp hoặc sửa đổi trực tiếp mã lệnh/dữ liệu nội bộ của module khác.

#### 3. Chuỗi thứ bậc Cohesion (Độ gắn kết nội bộ bên trong module)
Càng tập trung thực hiện 1 mục đích duy nhất càng tốt (Sắp xếp từ **Yếu nhất $\rightarrow$ Mạnh nhất**):
$$\mathbf{우연적 \lt 논리적 \lt 시간적 \lt 절차적 \lt 통신적 \lt 순차적 \lt 기능적}$$
- **기능적 응집도 (Functional - Tốt nhất):** Tất cả các câu lệnh chỉ cùng phục vụ **duy nhất 1 chức năng đơn lẻ**.
- **순차적 응집도 (Sequential):** Đầu ra câu lệnh này là đầu vào trực tiếp cho câu lệnh kế tiếp.
- **통신적 / 교환적 (Communicational):** Các thao tác cùng xử lý trên 1 tập dữ liệu đầu vào.
- **절차적 (Procedural):** Các thao tác thực thi theo một trình tự các bước.
- **시간적 (Temporal):** Các câu lệnh gom lại chỉ vì chạy cùng một thời điểm (như hàm khởi tạo `init`).
- **논리적 (Logical):** Gom các thao tác có tính chất tương tự nhau về mặt logic.
- **우연적 (Coincidental - Tồi tệ nhất):** Các câu lệnh nhét chung ngẫu nhiên không có liên hệ logic nào.

#### 4. Bảng 5 phương thức IPC (Inter-Process Communication)
| Phương thức IPC | Tên tiếng Hàn & Anh | Cơ chế hoạt động | Đặc điểm nhận diện cốt lõi |
| :--- | :--- | :--- | :--- |
| **Bộ nhớ chia sẻ** | **공유 메모리 (Shared Memory)** | Ánh xạ vùng RAM vật lý chung vào không gian địa chỉ các tiến trình | **Tốc độ nhanh nhất** (không qua sao chép Kernel); cần khóa đồng bộ |
| **Ổ cắm mạng** | **소켓 (Socket)** | Điểm cuối kết nối mạng (IP + Port) theo giao thức TCP/UDP | Giao tiếp **qua môi trường mạng** giữa các máy tính (Client/Server) |
| **Cờ hiệu đồng bộ**| **세마포어 (Semaphores)** | Biến đếm nguyên thủy với thao tác nguyên tử $P$ (Wait) và $V$ (Signal) | Chuyên dùng để **đồng bộ hóa và kiểm soát khóa miền găng** |
| **Đường ống** | **파이프 (Pipes)** | Kênh đệm bộ nhớ 1 chiều (FIFO): 1 bên ghi, 1 bên đọc | **Anonymous Pipe** (cha-con); **Named Pipe** (tiến trình bất kỳ) |
| **Hàng đợi tin** | **메시지 큐 (Message Queue)**| Gói tin được đưa vào hàng đợi do OS quản lý trong bộ nhớ | Hỗ trợ truyền thông **bất đồng bộ (Asynchronous)** |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Sắp xếp thứ tự Coupling:** Bắt buộc nhớ câu thần chú: **Data < Stamp < Control < External < Common < Content**. Tốt nhất là Data, tồi tệ nhất là Content.
- **Bẫy 2: Sắp xếp thứ tự Cohesion:** Mạnh nhất tuyệt đối là **Functional (기능적)**; yếu nhất là **Coincidental (우연적)**.
- **Bẫy 3: Phương thức IPC nhanh nhất:** IPC có tốc độ cao nhất là **공유 메모리 (Shared Memory)** do đọc ghi trực tiếp trên RAM không tốn overhead sao chép dữ liệu qua nhân OS.
- **Bẫy 4: Tái sử dụng 합성 중심 vs 생성 중심:**
  - Lắp ráp linh kiện có sẵn (giống Lego) $\rightarrow$ **합성 중심 (Composition-based)**.
  - Sinh mã tự động từ đặc tả trừu tượng (giống in 3D) $\rightarrow$ **생성 중심 (Generation-based)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chi tiết 4 hoạt động của Tái kỹ nghệ phần mềm (Re-engineering)
- `분석 (Analysis)`: Đánh giá và khảo sát toàn diện hệ thống hiện hành để bóc tách các thành phần còn giá trị tái sử dụng.
- `재구성 (Restructuring)`: Cải tiến cấu trúc mã nguồn bên trong để nâng cao tính bảo trì mà không làm thay đổi hành vi chức năng bên ngoài.
- `역공학 (Reverse Engineering)`: Phân tích mã nguồn hoặc file nhị phân để trích xuất ngược lại lược đồ thiết kế kiến trúc và bản đặc tả yêu cầu ban đầu.
- `이관 (Migration)`: Chuyển dịch phần mềm sang môi trường phần cứng, hệ điều hành hoặc cơ sở dữ liệu công nghệ mới.

#### 2. Cơ chế Semaphore trong kiểm soát miền găng (Critical Section)
- Thao tác $P$ (Wait): Kiểm tra nếu giá trị cờ hiệu $> 0$ thì giảm đi 1 và cho tiến trình đi vào miền găng; nếu $\le 0$ thì bắt tiến trình chờ.
- Thao tác $V$ (Signal): Sau khi tiến trình thoát khỏi miền găng, tăng giá trị cờ hiệu lên 1 để đánh thức tiến trình đang xếp hàng chờ.

---

### 복습 체크리스트
- [ ] Thuộc lòng quy tắc vàng: 응집도 (Cohesion) càng cao càng tốt, 결합도 (Coupling) càng thấp càng tốt.
- [ ] Xếp đúng thứ tự 결합도 từ yếu đến mạnh: Data $\lt$ Stamp $\lt$ Control $\lt$ External $\lt$ Common $\lt$ Content.
- [ ] Xếp đúng thứ tự 응집도 từ yếu đến mạnh: Coincidental $\lt$ Logical $\lt$ Temporal $\lt$ Procedural $\lt$ Communicational $\lt$ Sequential $\lt$ Functional.
- [ ] Nhớ 기능적 응집도 (Functional) là mạnh nhất; 자료 결합도 (Data) là tốt nhất.
- [ ] Kể tên đầy đủ 5 phương thức IPC: Shared Memory, Socket, Semaphore, Pipe, Message Queue.
- [ ] Nhớ Shared Memory có tốc độ nhanh nhất và Semaphore chuyên dùng để đồng bộ khóa tương tranh.
- [ ] Phân biệt rõ 합성 중심 (lắp ráp linh kiện có sẵn) và 생성 중심 (sinh mã từ đặc tả trừu tượng).
- [ ] Nhớ 4 bước của Re-engineering: 분석 (Analysis), 재구성 (Restructuring), 역공학 (Reverse Engineering), 이관 (Migration).
