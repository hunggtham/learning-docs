# Môn 2 · Bài 08 — Hiện thực đơn vị module, IPC và tái sử dụng phần mềm

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Mở màn cho **Chương 2: Thiết kế & Hiện thực Module, Tích hợp hệ thống (통합 구현)**, bài học này chuyển dịch tư duy từ việc tổ chức dữ liệu đơn lẻ sang việc xây dựng các khối phần mềm có khả năng biên dịch độc lập (**단위 모듈 — Unit Module**). Bài học phân tích sâu các chỉ số đo lường tính độc lập của module (Coupling vs Cohesion), 5 cơ chế giao tiếp liên tiến trình (**IPC**) và 2 trường phái tái sử dụng phần mềm (**Software Reuse**).

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ 6 bài học cũ: `31, 32, 33, 34, 35, 92-bai-hoc.md` (tương ứng với các mục 34, 핵심 031, 핵심 034, 093 ~ 096 trong tài liệu chuẩn gốc). Toàn bộ thứ bậc Coupling/Cohesion và các cơ chế IPC được đối chiếu chuẩn xác theo giáo trình khảo thí HRDK.

> **Mạch kiến thức:** Trong kiến trúc phần mềm hướng module, các khối chương trình phải độc lập cao nhưng vẫn cần trao đổi thông tin với nhau an toàn. Bài học này giải quyết ba vấn đề kỹ thuật: (1) Tính độc lập của một đơn vị module được định lượng qua độ gắn kết (응집도) và độ ghép nối (결합도) theo thứ bậc nào? (2) Tại sao các tiến trình trong hệ điều hành bị cô lập bộ nhớ và 5 phương thức IPC (Shared Memory, Socket, Semaphore, Pipe, Message Queue) giải quyết bài toán giao tiếp liên tiến trình ra sao? (3) Hai phương pháp tái sử dụng phần mềm (Hướng tổng hợp linh kiện vs Hướng tạo sinh từ đặc tả) khác nhau ở cơ chế nào?

---

## 1. 단위 모듈과 모듈의 독립성 — Đơn vị Module và Tính độc lập Module

**단위 모듈은 한 가지 동작을 수행하는 최소 단위의 소프트웨어 블록으로, 독립적으로 컴파일이 가능하고 재사용될 수 있는 구조이다.**

Trong kỹ nghệ phần mềm, module hóa (모듈화 — Modularity) là việc phân rã một hệ thống phần mềm phức tạp thành các đơn vị nhỏ độc lập. Một **Đơn vị module (단위 모듈 — Unit Module)** thường tương ứng với một hàm, một lớp (Class) hoặc một phân hệ nhỏ thực hiện duy nhất một nhiệm vụ chức năng hoàn chỉnh.

### Hai chỉ số vàng đo lường tính độc lập của Module
Chất lượng của một kiến trúc module được quyết định bởi nguyên tắc: **Độ gắn kết nội bộ cao (고응집도 — High Cohesion)** và **Độ phụ thuộc ghép nối thấp (저결합도 — Low Coupling)**.

```
[ THIẾT KẾ TỐI ƯU ]  ===>  응집도 (Cohesion) CỰC ĐẠI  +  결합도 (Coupling) CỰC TIỂU
```

#### 1. 결합도 (Coupling — Độ ghép nối): Đo lường mức độ phụ thuộc giữa các module
Càng ít phụ thuộc nhau càng tốt. Đề thi Kỹ sư Xử lý Thông tin thường xuyên yêu cầu sắp xếp thứ tự từ **Tốt nhất (Yếu nhất / Tự do nhất)** đến **Tồi tệ nhất (Chặt nhất / Nguy hiểm nhất)**:

$$\mathbf{자료(Data) \lt 스탬프(Stamp) \lt 제어(Control) \lt 외부(External) \lt 공통(Common) \lt 내용(Content)}$$

- **자료 결합도 (Data Coupling — Tốt nhất):** Hai module chỉ trao đổi với nhau bằng các tham số dữ liệu đơn giản (Primitive Parameters).
- **스탬프 결합도 (Stamp Coupling):** Hai module truyền cho nhau cả một cấu trúc dữ liệu bản ghi (Record/Struct) dù chỉ dùng 1 vài trường nhỏ.
- **제어 결합도 (Control Coupling):** Module này truyền cờ điều khiển (`Flag`) để can thiệp vào logic rẽ nhánh bên trong module kia.
- **외부 결합도 (External Coupling):** Nhiều module cùng chia sẻ giao thức truyền thông hoặc định dạng tệp ngoài.
- **공통 결합도 (Common Coupling):** Nhiều module cùng đọc và ghi vào một **vùng biến toàn cục (Global Variable)**. Rất nguy hiểm vì một module sửa biến sẽ làm hỏng các module khác.
- **내용 결합도 (Content Coupling — Tồi tệ nhất):** Module này trực tiếp nhảy vào can thiệp hoặc sửa đổi dữ liệu/mã lệnh nội bộ của module kia.

#### 2. 응집도 (Cohesion — Độ gắn kết nội bộ): Đo lường mức độ tập trung chức năng của các câu lệnh bên trong một module
Càng tập trung thực hiện 1 mục đích duy nhất càng tốt. Thứ tự từ **Tồi tệ nhất (Yếu nhất)** đến **Tốt nhất (Mạnh nhất)**:

$$\mathbf{우연적(Coincidental) \lt 논리적(Logical) \lt 시간적(Temporal) \lt 절차적(Procedural) \lt 통신적(Communicational) \lt 순차적(Sequential) \lt 기능적(Functional)}$$

- **기능적 응집도 (Functional Cohesion — Tốt nhất tuyệt đối):** Tất cả các câu lệnh bên trong module chỉ cùng phục vụ **duy nhất một chức năng toán học/nghiệp vụ đơn lẻ** (ví dụ: hàm `calculateSquareRoot(x)`).
- **순차적 응집도 (Sequential Cohesion):** Đầu ra của câu lệnh này trở thành đầu vào trực tiếp cho câu lệnh kế tiếp bên trong module.
- **통신적 / 교환적 응집도 (Communicational Cohesion):** Các thao tác bên trong module cùng xử lý trên một tập dữ liệu đầu vào.
- **절차적 응집도 (Procedural Cohesion):** Các thao tác được gom lại vì phải thực thi theo một trình tự các bước xác định.
- **시간적 응집도 (Temporal Cohesion):** Các câu lệnh được gom vào cùng một hàm chỉ vì chúng được thực thi tại cùng một thời điểm (ví dụ: hàm khởi tạo `initSystem()`).
- **논리적 응집도 (Logical Cohesion):** Gom các thao tác có tính chất tương tự nhau về mặt logic nhưng không liên quan nghiệp vụ (ví dụ: gom tất cả các thao tác in ấn báo cáo vào 1 module dù xử lý dữ liệu khác nhau).
- **우연적 응집도 (Coincidental Cohesion — Tồi tệ nhất):** Các câu lệnh được nhét chung vào một module hoàn toàn ngẫu nhiên không có bất kỳ mối liên hệ logic nào.

---

## 2. 프로세스 간 통신 (IPC — Inter-Process Communication)

Trong các hệ điều hành hiện đại (Linux, Windows), mỗi tiến trình (Process) đều được cấp phát một **không gian địa chỉ bộ nhớ ảo cô lập hoàn toàn** nhằm ngăn chặn một tiến trình bị lỗi làm sập toàn bộ hệ thống. 

Tuy nhiên, trong các hệ thống phần mềm lớn, các đơn vị module chạy trên các tiến trình độc lập bắt buộc phải trao đổi thông điệp và đồng bộ hóa với nhau. Cơ chế do hệ điều hành cung cấp để làm việc này gọi là **IPC (Inter-Process Communication)**.

### Bảng 5 phương thức IPC kinh điển chuẩn đề thi

| Phương thức IPC | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Đặc điểm nhận diện cốt lõi |
| :--- | :--- | :--- | :--- |
| **Bộ nhớ chia sẻ** | **공유 메모리 (Shared Memory)** | Hệ điều hành ánh xạ một vùng nhớ RAM vật lý chung vào không gian địa chỉ của nhiều tiến trình để các bên cùng đọc/ghi trực tiếp | **Tốc độ nhanh nhất** trong tất cả các IPC vì không tốn công sao chép qua Kernel; cần cơ chế khóa đồng bộ |
| **Ổ cắm mạng** | **소켓 (Socket)** | Tạo điểm cuối kết nối mạng logic (IP Address + Port Number) theo giao thức TCP/UDP | Hỗ trợ giao tiếp **qua môi trường mạng** giữa các máy tính khác nhau (Client/Server) |
| **Cờ hiệu đồng bộ** | **세마포어 (Semaphores)** | Biến đếm nguyên thủy do Dijkstra đề xuất, dùng thao tác nguyên tử $P$ (Wait) và $V$ (Signal) để kiểm soát quyền vào miền găng (Critical Section) | Chuyên dùng để **đồng bộ hóa và kiểm soát tương tranh**, ngăn chặn xung đột tài nguyên chung |
| **Đường ống** | **파이프 (Pipes & Named Pipes)** | Kênh đệm bộ nhớ 1 chiều (Unidirectional) hoạt động theo nguyên lý FIFO: Một tiến trình ghi vào đầu ống, tiến trình kia đọc ra ở đầu kia | **Anonymous Pipe:** giữa các tiến trình cha - con; **Named Pipe:** giữa các tiến trình bất kỳ |
| **Hàng đợi thông điệp** | **메시지 큐 (Message Queue)** | Các thông điệp được đóng gói thành gói tin và đưa vào hàng đợi do hệ điều hành quản lý trong bộ nhớ | Hỗ trợ truyền thông **bất đồng bộ (Asynchronous)** giữa các tiến trình độc lập |

---

## 3. 소프트웨어 재사용 기법 (Software Reuse) — Tái sử dụng phần mềm

**소프트웨어 재사용은 이미 검증된 소프트웨어의 개발 지식이나 부품을 새로운 시스템 구축에 다시 활용하는 기법이다.**

### Lợi ích cốt lõi của Tái sử dụng:
1. **Rút ngắn thời gian và chi phí phát triển (개발 비용 및 기간 단축):** Giảm thiểu công việc viết code lặp lại.
2. **Nâng cao chất lượng và độ tin cậy (품질 및 신뢰도 향상):** Các module tái sử dụng đã chạy ổn định qua nhiều năm trong các dự án trước nên hầu như đã sạch lỗi.
3. **Chuẩn hóa kiến trúc:** Thống nhất các quy chuẩn lập trình và giao diện trong toàn doanh nghiệp.

### Hai trường phái tái sử dụng chuẩn mực:

```
[ 합성 중심 (Composition) ]                 [ 생성 중심 (Generation) ]
   +-----+   +-----+                          +----------------------+
   | Khối | + | Khối |  ===> Phần mềm mới     | Bản đặc tả trừu tượng | ===> Trình sinh mã ===> Code mới
   |  A  |   |  B  |                          +----------------------+
   +-----+   +-----+                                    
  (Lắp ráp linh kiện Component)                      (Sinh mã tự động theo mẫu Pattern)
```

1. **합성 중심 (Composition-based / Block-based — Hướng tổng hợp / Hướng linh kiện):**
   - **Cơ chế:** Lắp ghép các khối phần mềm (**블록 / 컴포넌트 — Component**) đã hoàn thiện và được kiểm thử sẵn lại với nhau thành một hệ thống mới.
   - **Hình tượng ẩn dụ:** Giống như trò chơi xếp hình Lego (ghép các mảnh có sẵn).
2. **생성 중심 (Generation-based / Pattern-based — Hướng tạo sinh):**
   - **Cơ chế:** Dựa trên một **bản mô tả đặc tả trừu tượng (Abstract Specification)** và các mẫu thiết kế cấu trúc (Pattern), một trình sinh mã tự động (Code Generator) sẽ phân tích và trực tiếp sinh ra mã nguồn mới phù hợp với bài toán cụ thể.
   - **Hình tượng ẩn dụ:** Giống như chiếc máy in 3D in ra đồ vật dựa trên bản vẽ CAD.

### Bốn hoạt động cốt lõi của Tái kỹ nghệ phần mềm (Re-engineering):
- **분석 (Analysis — Phân tích):** Khảo sát hệ thống cũ để xác định phần nào còn giá trị tái sử dụng.
- **재구성 (Restructuring — Tái cấu trúc):** Sửa đổi cấu trúc mã nguồn bên trong mà không làm thay đổi hành vi chức năng bên ngoài.
- **역공학 (Reverse Engineering — Kỹ nghệ đảo ngược):** Khôi phục lại tài liệu thiết kế kiến trúc và đặc tả từ tệp mã nguồn hoặc tệp nhị phân có sẵn.
- **이관 (Migration — Chuyển dịch):** Đưa phần mềm sang vận hành trên môi trường phần cứng, hệ điều hành hoặc cơ sở dữ liệu mới.

---

## 4. Nối mạch kiến thức sang bài tiếp theo

Từ cấp độ các module đơn lẻ chạy trong một tiến trình hoặc trên cùng một máy chủ, khi quy mô phần mềm phát triển thành hệ thống phân tán đa nền tảng (doanh nghiệp sở hữu nhiều hệ thống ERP, CRM, Core Banking độc lập viết bằng nhiều ngôn ngữ khác nhau), việc trao đổi dữ liệu không thể chỉ dùng các IPC đơn giản mà bắt buộc phải sử dụng các nền tảng tích hợp ứng dụng doanh nghiệp chuyên nghiệp: **EAI (Enterprise Application Integration)** và **ESB (Enterprise Service Bus)**.

Chúng ta sẽ chuyển sang **[Bài 09: Tích hợp hệ thống EAI/ESB và giao thức truyền thông](09-tich-hop-he-thong-eai-esb.md)** để nghiên cứu 4 mô hình kiến trúc EAI kinh điển (Point-to-Point, Hub & Spoke, Message Bus, Hybrid) và các định dạng trao đổi dữ liệu web hiện đại (JSON, XML, AJAX, REST).

---

## 5. 복습 체크리스트 (Checklist ôn tập)

- [ ] Thuộc lòng quy tắc vàng: 응집도 (Cohesion) càng cao càng tốt, 결합도 (Coupling) càng thấp càng tốt.
- [ ] Xếp đúng thứ tự 결합도 từ yếu đến mạnh: Data $\lt$ Stamp $\lt$ Control $\lt$ External $\lt$ Common $\lt$ Content.
- [ ] Xếp đúng thứ tự 응집도 từ yếu đến mạnh: Coincidental $\lt$ Logical $\lt$ Temporal $\lt$ Procedural $\lt$ Communicational $\lt$ Sequential $\lt$ Functional.
- [ ] Nhớ 기능적 응집도 (Functional) là mạnh nhất; 자료 결합도 (Data) là tốt nhất.
- [ ] Kể tên đầy đủ 5 phương thức IPC: Shared Memory, Socket, Semaphore, Pipe, Message Queue.
- [ ] Nhớ Shared Memory có tốc độ nhanh nhất và Semaphore chuyên dùng để đồng bộ khóa tương tranh.
- [ ] Phân biệt rõ 합성 중심 (lắp ráp linh kiện có sẵn) và 생성 중심 (sinh mã từ đặc tả trừu tượng).
- [ ] Nhớ 4 bước của Re-engineering: 분석 (Analysis), 재구성 (Restructuring), 역공학 (Reverse Engineering), 이관 (Migration).
