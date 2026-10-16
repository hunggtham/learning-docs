# 모듈 구현과 프로세스 간 통신 (Hiện thực module và IPC)

## 학습 목표
- Nắm vững định nghĩa Đơn vị Module (`단위 모듈 / Unit Module`), nguyên tắc thiết kế độc lập module: Độ gắn kết nội bộ cao (`고응집도 / High Cohesion`) và Độ ghép nối phụ thuộc thấp (`저결합도 / Low Coupling`).
- Thuộc lòng thứ bậc 6 cấp độ Coupling từ tốt nhất đến tồi tệ nhất: Data $\rightarrow$ Stamp $\rightarrow$ Control $\rightarrow$ External $\rightarrow$ Common $\rightarrow$ Content.
- Thuộc lòng thứ bậc 7 cấp độ Cohesion từ tồi tệ nhất đến tốt nhất: Coincidental $\rightarrow$ Logical $\rightarrow$ Temporal $\rightarrow$ Procedural $\rightarrow$ Communicational $\rightarrow$ Sequential $\rightarrow$ Functional.
- Phân tích cơ chế và nhận diện 5 phương thức giao tiếp liên tiến trình (`IPC / Inter-Process Communication`): Shared Memory, Socket, Semaphore, Pipe, Message Queue.
- Phân biệt 2 hướng tiếp cận trong Tái sử dụng phần mềm (`소프트웨어 재사용`): Hướng tổng hợp linh kiện (`합성 중심`) và Hướng tạo sinh từ đặc tả (`생성 중심`).

## 핵심 키워드
- 단위 모듈 (Đơn vị Module / Unit Module / Modularity)
- 결합도 (Coupling / Data < Stamp < Control < External < Common < Content)
- 응집도 (Cohesion / Coincidental < Logical < Temporal < Procedural < Communicational < Sequential < Functional)
- IPC (Inter-Process Communication / 프로세스 간 통신)
- IPC 5대 기법 (공유 메모리 Shared Memory, 소켓 Socket, 세마포어 Semaphore, 파이프 Pipe, 메시지 큐 Message Queue)
- 재사용 기법 (Tái sử dụng phần mềm / 합성 중심 Synthesis vs 생성 중심 Generation)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở Môn 1 [08-thiet-ke-module-coupling-cohesion.md](../../01-software-design/lessons/08-thiet-ke-module-coupling-cohesion.md), chúng ta đã khảo sát các nguyên lý thiết kế module ở tầng kiến trúc.
- **Đang giải quyết gì (Current Problem):** Bài học này đi sâu vào việc hiện thực hóa mã nguồn của từng đơn vị module, đo lường định lượng tính độc lập và giải quyết bài toán giao tiếp giữa các module chạy trên các tiến trình độc lập trong hệ điều hành qua IPC.
- **Dùng đi đâu (Forward Handoff):** Khi các module mở rộng từ cấp độ tiến trình đơn lẻ lên quy mô doanh nghiệp và hệ thống phân tán, bài học tiếp theo [09-tich-hop-he-thong-eai-esb.md](09-tich-hop-he-thong-eai-esb.md) sẽ khảo sát các kiến trúc tích hợp EAI và trục dịch vụ doanh nghiệp ESB.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng hai chuỗi thứ bậc Coupling và Cohesion, bảng phân biệt 5 phương pháp IPC và các bẫy đề thi trắc nghiệm kinh điển.
- Đọc TẦNG B để hiểu sâu bản chất kỹ thuật của từng loại Coupling/Cohesion, cơ chế đồng bộ hóa Semaphore/Mutex và hai phương pháp tái sử dụng phần mềm.

---

## 모듈 구현과 프로세스 간 통신

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Nguyên tắc vàng trong thiết kế Module
```
[ THIẾT KẾ TỐI ƯU ]  ===>  응집도 (Cohesion) CỰC ĐẠI  +  결합도 (Coupling) CỰC TIỂU
```

#### 2. Chuỗi thứ bậc 6 cấp độ 결합도 (Coupling)
Từ **Tốt nhất (Yếu nhất / Tự do nhất)** đến **Tồi tệ nhất (Chặt nhất / Nguy hiểm nhất)**:
$$\mathbf{자료(Data) \lt 스탬프(Stamp) \lt 제어(Control) \lt 외부(External) \lt 공통(Common) \lt 내용(Content)}$$

| Cấp độ Coupling | Tên tiếng Hàn & Anh | Cơ chế liên kết | Đánh giá |
| :--- | :--- | :--- | :--- |
| **Data** | **자료 결합도** | Chỉ trao đổi tham số dữ liệu đơn giản (Primitive) | **Tốt nhất tuyệt đối** |
| **Stamp** | **스탬프 결합도** | Truyền cả cấu trúc dữ liệu bản ghi (Record/Struct) dù chỉ dùng 1 vài trường | Tốt vừa |
| **Control** | **제어 결합도** | Module này truyền cờ điều khiển (`Flag`) can thiệp logic module kia | Kém |
| **External** | **외부 결합도** | Nhiều module cùng chia sẻ định dạng tệp ngoài hoặc giao thức mạng | Kém |
| **Common** | **공통 결합도** | Nhiều module cùng chia sẻ và sửa đổi **biến toàn cục (Global Variable)** | Rất nguy hiểm |
| **Content** | **내용 결합도** | Module này can thiệp trực tiếp vào mã lệnh hoặc dữ liệu nội bộ của module kia | **Tồi tệ nhất** |

#### 3. Chuỗi thứ bậc 7 cấp độ 응집도 (Cohesion)
Từ **Tồi tệ nhất (Yếu nhất)** đến **Tốt nhất (Mạnh nhất)**:
$$\mathbf{우연적(Coincidental) \lt 논리적(Logical) \lt 시간적(Temporal) \lt 절차적(Procedural) \lt 통신적(Communicational) \lt 순차적(Sequential) \lt 기능적(Functional)}$$

| Cấp độ Cohesion | Tên tiếng Hàn & Anh | Cơ chế gắn kết nội bộ | Đánh giá |
| :--- | :--- | :--- | :--- |
| **Functional** | **기능적 응집도** | Mọi câu lệnh chỉ phục vụ **duy nhất 1 chức năng toán học/nghiệp vụ đơn lẻ** | **Tốt nhất tuyệt đối** |
| **Sequential** | **순차적 응집도** | Đầu ra của lệnh này trở thành đầu vào trực tiếp cho lệnh kế tiếp | Rất tốt |
| **Communicational** | **통신적 / 교환적** | Các thao tác cùng thực hiện trên một tập dữ liệu đầu vào | Khá tốt |
| **Procedural** | **절차적 응집도** | Các thao tác được gom lại vì phải chạy theo một trình tự các bước | Trung bình |
| **Temporal** | **시간적 응집도** | Các câu lệnh gom chung chỉ vì chạy tại cùng một thời điểm (hàm `init`) | Kém |
| **Logical** | **논리적 응집도** | Gom các thao tác có tính chất tương tự nhau (như các hàm in ấn) | Kém |
| **Coincidental** | **우연적 응집도** | Các câu lệnh nhét chung hoàn toàn ngẫu nhiên, không liên hệ | **Tồi tệ nhất** |

#### 4. Bảng 5 phương thức IPC (Inter-Process Communication)

| Phương thức IPC | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Đặc điểm nhận diện cốt lõi |
|:---|:---|:---|:---|
| **Shared Memory** | **공유 메모리** | Nhiều tiến trình cùng ánh xạ và truy cập chung vào một vùng nhớ RAM vật lý | **Tốc độ nhanh nhất** (không qua kernel sau khi tạo); cần cơ chế đồng bộ tránh xung đột ghi |
| **Socket** | **소켓** | Giao tiếp hai chiều thông qua cổng mạng mạng TCP/IP giữa client và server | Giao tiếp được giữa **các máy tính khác nhau qua mạng** hoặc nội bộ qua Unix Domain Socket |
| **Semaphore** | **세마포어** | Biến cờ đồng bộ hóa để kiểm soát quyền truy cập tài nguyên găng (Critical Section) | Không dùng truyền dữ liệu lớn; chỉ dùng **đồng bộ hóa và chống Race Condition / Deadlock** |
| **Pipes** | **파이프 (익명 vs 네임드)** | Kênh truyền dữ liệu một chiều (Half-duplex). Anonymous Pipe dùng cho cha-con; Named Pipe (FIFO) có tên trên filesystem | Đơn giản, dùng trong dòng lệnh (`ls \| grep`) hoặc giữa các tiến trình độc lập qua file FIFO |
| **Message Queue** | **메시지 큐** | Hàng đợi lưu trữ thông điệp bất đồng bộ trong nhân hệ điều hành (Kernel) | **Bất đồng bộ (Asynchronous)**, tiến trình gửi không cần chờ tiến trình nhận, hỗ trợ lọc theo Message Type |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Thần chú Coupling & Cohesion:**
  - Quy tắc thiết kế: **고응저결 (Cao Ứng Thấp Kết)** $\rightarrow$ Cohesion High, Coupling Low.
  - Coupling tốt nhất: **자료 결합도 (Data)**; tồi tệ nhất: **내용 결합도 (Content)** (Khẩu quyết: **자-스-제-외-공-내**).
  - Cohesion tốt nhất: **기능적 응집도 (Functional)**; tồi tệ nhất: **우연적 응집도 (Coincidental)** (Khẩu quyết: **우-논-시-절-통-순-기**).
- **Bẫy 2: Biến toàn cục thuộc loại nào:** Nhiều module cùng dùng biến toàn cục $\rightarrow$ **공통 결합도 (Common Coupling)**.
- **Bẫy 3: Phương thức IPC tốc độ cao nhất:** IPC nào có tốc độ truyền nhanh nhất do không cần sao chép dữ liệu qua kernel? $\rightarrow$ **공유 메모리 (Shared Memory)**.
- **Bẫy 4: Phân biệt Anonymous Pipe vs Named Pipe:** Anonymous Pipe chỉ dùng cho các tiến trình có quan hệ cha-con (`부모-자식 프로세스`); muốn hai tiến trình hoàn toàn độc lập giao tiếp bằng Pipe thì phải dùng **Named Pipe (FIFO)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. So sánh kiến trúc: Shared Memory vs Message Passing

```text
  [MÔ HÌNH 1: BỘ NHỚ CHIA SẺ (SHARED MEMORY)]
  Tiến trình A (Process A)                    Tiến trình B (Process B)
  ┌───────────────────────┐                   ┌───────────────────────┐
  │ Không gian địa chỉ A  │                   │ Không gian địa chỉ B  │
  └───────────┬───────────┘                   └───────────┬───────────┘
              │ Ánh xạ (Map)                              │ Ánh xạ (Map)
              ▼                                           ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │               Vùng nhớ chia sẻ vật lý (Shared Memory RAM)          │
  │   - Đọc/Ghi trực tiếp với tốc độ bus phần cứng (Không qua Kernel) │
  │   - Bắt buộc phối hợp cùng Semaphore/Mutex để chống Race Condition│
  └───────────────────────────────────────────────────────────────────┘

  [MÔ HÌNH 2: TRUYỀN THÔNG ĐIỆP (MESSAGE PASSING: PIPE / QUEUE / SOCKET)]
  Tiến trình gửi (Sender)                     Tiến trình nhận (Receiver)
  ┌───────────────────────┐                   ┌───────────────────────┐
  │  Buffer người dùng A  │                   │  Buffer người dùng B  │
  └───────────┬───────────┘                   └───────────▲───────────┘
              │ 1. write() / send()                       │ 3. read() / recv()
              ▼    (System Call vào Kernel)               │    (System Call từ Kernel)
  ┌───────────────────────────────────────────────────────┴───────────┐
  │                     Nhân Hệ Điều Hành (Kernel)                    │
  │    [ 2. Buffer dữ liệu trung gian: Pipe Buffer / Message Queue ]   │
  │    - Tốn chi phí chuyển đổi ngữ cảnh (Context Switching Overhead) │
  │    - An toàn hơn vì không chia sẻ không gian bộ nhớ trực tiếp      │
  └───────────────────────────────────────────────────────────────────┘
```

- **Phân tích bản chất:**
  - **Shared Memory (Bộ nhớ chia sẻ):** Sau khi được hệ điều hành thiết lập vùng nhớ chung ban đầu, các thao tác đọc ghi dữ liệu diễn ra như đọc ghi biến thông thường trên RAM mà **hoàn toàn không cần gọi System Call vào Kernel**. Do đó, nó đạt tốc độ cao nhất và thích hợp cho việc truyền dữ liệu dung lượng lớn (video streaming, hình ảnh đồ họa). Tuy nhiên, lập trình viên phải tự quản lý đồng bộ hóa bằng Semaphore để tránh xung đột dữ liệu.
  - **Message Passing (Truyền thông điệp):** Mỗi lần gửi nhận dữ liệu, tiến trình phải thực hiện System Call (`send`/`recv` hoặc `write`/`read`). Dữ liệu được sao chép 2 lần: từ bộ nhớ người dùng vào bộ đệm của Kernel, rồi từ Kernel sang bộ nhớ tiến trình đích. Tuy tốc độ chậm hơn và tốn tài nguyên chuyển ngữ cảnh (`Context Switching`), nhưng phương thức này an toàn tuyệt đối và có thể mở rộng chạy phân tán qua mạng (Socket).

#### 2. Chi tiết 2 phương pháp Tái sử dụng phần mềm (소프트웨어 재사용)

```text
  [ 합성 중심 (Composition-based) ]             [ 생성 중심 (Generation-based) ]
     ┌─────┐   ┌─────┐                              ┌────────────────────────┐
     │Khối │ + │Khối │  ===> Phần mềm mới           │ Bản đặc tả trừu tượng  │ ===> Trình sinh mã ===> Code mới
     │  A  │   │  B  │                              └────────────────────────┘      (Compiler/CASE)
     └─────┘   └─────┘
    (Lắp ráp linh kiện Component)                          (Sinh mã tự động theo mẫu Pattern)
```

- **합성 중심 (Synthesis-oriented / Hướng tổng hợp):**
  - Còn gọi là tái sử dụng hướng khối ghép (Block-oriented / Lego approach).
  - Lắp ráp phần mềm mới bằng cách kết hợp các khối linh kiện phần mềm (Software Components) đã được kiểm thử và lưu trữ sẵn trong thư viện.
- **생성 중심 (Generation-oriented / Hướng tạo sinh):**
  - Người dùng cung cấp bản đặc tả trừu tượng ở mức cao.
  - Công cụ phần mềm tự động hóa (CASE Tool / Code Generator) sẽ tự động sinh ra mã nguồn hoàn chỉnh dựa trên các mẫu và quy tắc tạo sinh định sẵn.

---

### 복습 체크리스트
- [ ] Thuộc lòng chuỗi 6 cấp độ Coupling: Data < Stamp < Control < External < Common < Content (`자-스-제-외-공-내`).
- [ ] Thuộc lòng chuỗi 7 cấp độ Cohesion: Coincidental < Logical < Temporal < Procedural < Communicational < Sequential < Functional (`우-논-시-절-통-순-기`).
- [ ] Nhớ biến toàn cục tương ứng với Common Coupling.
- [ ] Phân biệt 5 phương thức IPC: Shared Memory (nhanh nhất), Socket (qua mạng), Semaphore (đồng bộ), Pipe (1 chiều), Message Queue (bất đồng bộ).
- [ ] Phân biệt Anonymous Pipe (quan hệ cha-con) và Named Pipe (giao tiếp tiến trình độc lập qua tên FIFO).
- [ ] So sánh được cơ chế hoạt động của Shared Memory (không qua kernel) và Message Passing (qua kernel buffer).
- [ ] Phân biệt Tái sử dụng 합성 중심 (ghép linh kiện) và 생성 중심 (tạo sinh từ đặc tả).
