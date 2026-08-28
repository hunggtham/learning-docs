# 정보처리기사 (Information Processing Engineer) - Subject 2 Part 2

## BSA (Branch and Save Return Address) 
명령어 실행 중 서브루틴(부프로그램) 호출 시, 현재의 복귀 주소(Return Address)를 저장하고 서브루틴으로 분기하는 과정입니다.

| Micro Operation (Vi 동작) | 의 미 (Ý nghĩa / Meaning) |
|---|---|
| `MAR ← MBR[AD]` | • MBR에 있는 명령어의 번지 부분을 MAR에 전송함<br>(Chuyển phần địa chỉ lệnh từ MBR sang MAR)<br>※ MBR[AD]는 복귀 주소가 저장될 위치이면서 부프로그램이 시작되기 바로 전 번지임 (Là vị trí lưu địa chỉ trở về, ngay trước địa chỉ bắt đầu chương trình con) |
| `MBR[AD] ← PC` | • PC의 값(복귀 주소)을 MBR의 주소 부분으로 전송함<br>(Chuyển giá trị PC (địa chỉ trở về) vào phần địa chỉ của MBR) |
| | ※ 복귀 주소를 저장하기 위한 준비 단계임 (Bước chuẩn bị lưu địa chỉ trở về) |
| `PC ← MBR[AD]` | • MBR의 주소 부분을 PC로 전송함<br>(Chuyển phần địa chỉ của MBR sang PC)<br>※ 부프로그램이 시작되기 바로 전 주소를 PC에 전송함 (Gửi địa chỉ ngay trước chương trình con vào PC) |
| `M[MAR] ← MBR[AD]` | • MBR에 있는 명령어의 번지 부분을 메모리의 MAR이 가리키는 위치에 전송함<br>(Lưu địa chỉ trở về vào bộ nhớ tại vị trí MAR trỏ tới) |
| `PC ← PC + 1` | • PC의 값을 1 증가시킴<br>(Tăng PC lên 1)<br>※ 부프로그램의 시작임 (Bắt đầu chương trình con) |

- **Vietnamese Explanation:** BSA là quá trình nhảy đến một chương trình con và lưu lại địa chỉ để có thể quay về chương trình chính sau khi thực thi xong. CPU lưu giá trị PC hiện tại vào bộ nhớ, sau đó gán địa chỉ của chương trình con vào PC.
- **Ví dụ (Example):** Khi bạn đang đọc một cuốn sách (chương trình chính) ở trang 10 và có một chú thích yêu cầu bạn xem phụ lục ở trang 100 (chương trình con). Bạn dùng một cái kẹp sách kẹp vào trang 10 (lưu PC), mở trang 100 đọc, đọc xong lại quay về trang kẹp sách.
- 💡 **Mẹo ghi nhớ (Mnemonics):** BSA = "Bắt (Branch) Sang (Save) Anh (Address)". Hãy nhớ trình tự: Chuyển địa chỉ (MAR) -> Lưu PC cũ (MBR) -> Cập nhật PC mới -> Lưu vào bộ nhớ -> Tăng PC lên 1 để chạy.

---

## 핵심 096: 제어 데이터 (Control Data / Dữ liệu điều khiển)

- 제어장치가 제어 신호를 발생하기 위한 자료로서, CPU가 특정한 메이저 상태와 타이밍 상태에 있을 때 제어 자료에 따른 제어 규칙에 의해 제어 신호가 발생한다. 
  (Dữ liệu để bộ điều khiển tạo ra tín hiệu điều khiển. Dựa trên trạng thái chính và trạng thái thời gian của CPU.)
- **제어 데이터의 종류 (Các loại dữ liệu điều khiển):**
  - 메이저 스테이트 사이의 변천을 제어하는 데이터 (Dữ liệu điều khiển chuyển đổi giữa các trạng thái chính - Major States)
  - 중앙처리장치의 제어점을 제어하는 데이터 (Dữ liệu điều khiển các điểm điều khiển của CPU)
  - 인스트럭션의 수행 순서를 결정하는 데 필요한 제어 데이터 (Dữ liệu điều khiển thứ tự thực thi lệnh)

| 구 분 (Phân loại) | Fetch (Lấy lệnh) | Indirect (Gián tiếp) | Execute (Thực thi) | Interrupt (Ngắt) |
|---|---|---|---|---|
| State간 변이용 (Chuyển trạng thái) | 명령어 종류, 주소지정방식 (Loại lệnh, cách định địa chỉ) | 주소지정방식 (Cách định địa chỉ) | 인터럽트 요청 신청 (Yêu cầu ngắt) | 없음 (Không) |
| 제어점 제어용 (Điều khiển điểm) | 명령어 (Lệnh) | 유효주소 (Địa chỉ hiệu dụng) | 명령어의 연산자 (Toán tử của lệnh) | Interrupt 체제에 따라 달라짐 (Tùy hệ thống ngắt) |
| 수행순서 제어용 (Thứ tự thực thi) | PC (Program Counter) | 없음 (Không) | PC | Interrupt 체제에 따라 달라짐 (Tùy hệ thống ngắt) |

- **Vietnamese Explanation:** Dữ liệu điều khiển đóng vai trò như các biển báo giao thông bên trong CPU, hướng dẫn CPU lúc nào cần lấy dữ liệu, lúc nào thực thi, lúc nào tạm dừng để xử lý ngắt.
- **Ví dụ (Example):** CPU giống như một đầu bếp. "Dữ liệu chuyển trạng thái" là đồng hồ hẹn giờ chuyển từ bước "sơ chế" sang "nấu". "Dữ liệu điều khiển điểm" là thông tin bếp nào cần bật/tắt. "Dữ liệu thứ tự" là danh sách các món ăn cần làm tiếp theo.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 3 loại 제어 데이터: "Trạng thái (State) - Điểm (Point) - Thứ tự (Order)".

---

## 핵심 097: 제어장치의 비교 (Comparison of Control Units / So sánh bộ điều khiển)

제어장치는 필요한 마이크로 연산들이 연속적으로 수행될 수 있도록 제어 신호를 보내는 역할을 한다.
(Bộ điều khiển gửi tín hiệu để các vi phép toán được thực hiện liên tục.)

| 구 분 (Phân loại) | 고정배선 제어장치 (Hardwired Control / Nối dây cứng) | 마이크로 프로그래밍 기법 (Micro-programming / Vi lập trình) |
|---|---|---|
| 반응속도 (Tốc độ phản hồi) | 고속 (Nhanh) | 저속 (Chậm) |
| 회로복잡도 (Độ phức tạp mạch) | 복잡 (Phức tạp) | 간단 (Đơn giản) |
| 경제성 (Tính kinh tế) | 비경제적 (Kém kinh tế) | 경제적 (Kinh tế) |
| 융통성 (Tính linh hoạt) | 없음 (Không) | 있음 (Có) |
| 구성 (Cấu tạo) | 하드웨어 (Phần cứng) | 소프트웨어 (Phần mềm) |

### 마이크로 프로그램 (Micro-program)
- 내부 제어신호를 발생하는 여러 가지 마이크로 인스트럭션으로 작성된 것으로, 보통 **ROM**에 저장되어 있습니다.
  (Gồm các vi lệnh tạo tín hiệu điều khiển, thường lưu trong ROM.)
- 제어 기억장치의 용량을 줄일 수 있다. (Giảm dung lượng bộ nhớ điều khiển.)
- 마이크로 명령어의 코드화된 비트들을 해독하기 위한 지연이 발생한다. (Có độ trễ do phải giải mã các bit của vi lệnh.)

### 나노 명령 (Nano Instruction)
- 나노 메모리(Nano Memory)라는 낮은 레벨의 메모리에 저장된 마이크로 명령. (Vi lệnh lưu ở bộ nhớ cấp thấp gọi là Nano Memory.)
- 수직 마이크로 명령을 수행하는 제어기에서 디코더를 ROM(나노 메모리)으로 대치하여 두 메모리 레벨로 구성한다.
  (Thay thế bộ giải mã bằng ROM 2 cấp để xử lý vi lệnh dọc.)

- **Vietnamese Explanation:** Có hai cách chế tạo bộ điều khiển: Hardwired (phần cứng 100%) chạy cực nhanh nhưng khó sửa chữa; Micro-programmed (phần mềm lưu trong ROM) thì chậm hơn một chút nhưng linh hoạt, dễ sửa đổi, nâng cấp.
- **Ví dụ (Example):** Hardwired giống như cái điều khiển quạt trần cơ học (bấm nút là quay nhanh/chậm), rất nhanh nhưng không thể thêm chức năng "hẹn giờ" được. Micro-programming giống như điều khiển TV thông minh (có phần mềm bên trong), có thể cập nhật để có giao diện mới, nhưng thao tác đôi khi bị trễ (lag) 1 giây.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Hardwired = Nhanh - Khó - Cứng (Hardware). Micro = Chậm - Dễ - Mềm (Software).

---

## 핵심 098: 마이크로 명령의 형식 (Format of Micro Instructions / Định dạng vi lệnh)

- **수평 마이크로 명령 (Horizontal Micro Instruction / Vi lệnh ngang):**
  - 마이크로 명령의 한 비트가 한 개의 마이크로 동작을 관할하는 명령이다. (Mỗi bit quản lý một vi thao tác.)
  - Micro Operation부가 m Bit일 때 m개의 마이크로 동작을 표현할 수 있다. (m bits = m thao tác.)
  - Address부의 주소에 의해 다음 마이크로 명령의 주소를 결정한다. (Phần địa chỉ quyết định vi lệnh tiếp theo.)
- **수직 마이크로 명령 (Vertical Micro Instruction / Vi lệnh dọc):**
  - 제어 메모리 외부에서 디코딩 회로를 필요로 하는 마이크로 명령이다. (Cần mạch giải mã (decoder) bên ngoài.)
  - 한 개의 마이크로 명령으로 한 개의 마이크로 동작만 제어할 수 있다. (Một vi lệnh chỉ điều khiển một thao tác.)
  - 마이크로 명령어의 비트 수가 감소된다. (Giảm số lượng bit của vi lệnh.)

- **Vietnamese Explanation:** Vi lệnh ngang thì dài, mỗi bit trực tiếp điều khiển một thành phần (tốn bộ nhớ nhưng nhanh). Vi lệnh dọc thì ngắn, mã hóa các lệnh (tiết kiệm bộ nhớ nhưng cần bộ giải mã để hiểu mã đó, làm chậm tốc độ).
- **Ví dụ (Example):** Cần bật đèn 3 phòng. 
  - Ngang: Bảng công tắc có 3 nút riêng biệt cho 3 phòng. Nhanh nhưng chiếm diện tích lớn.
  - Dọc: Một nút vặn (1,2,3). Xoay đến số 2 thì hệ thống giải mã và bật đèn phòng 2. Tiết kiệm chỗ nhưng phải tốn thời gian vặn đúng số.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Ngang (Horizontal) = Nhiều bit, Không cần dịch (Dài như dải lụa). Dọc (Vertical) = Ít bit, Phải dịch mã (Decoder).

---

## 핵심 099: 입·출력장치의 구성 (Structure of I/O Devices / Cấu trúc thiết bị Vào/Ra)

- **입·출력 제어장치 (I/O Control Unit / Bộ điều khiển Vào/Ra):**
  - 입·출력장치와 컴퓨터 사이의 자료 전송을 제어하는 장치이다. (Điều khiển truyền dữ liệu giữa I/O và máy tính.)
  - 데이터 버퍼 레지스터를 이용하여 두 장치 간의 속도 차를 조절한다. (Dùng bộ đệm (Buffer) để điều hòa chênh lệch tốc độ.)
  - 종류 (Các loại): DMA, 채널 (Channel), 입·출력 프로세서 (IOP), 입·출력 컴퓨터 등.
- **입·출력 인터페이스 (I/O Interface / Giao diện Vào/Ra):**
  - 해결 목적 (Mục đích giải quyết):
    - 전자기/기계적 장치와 전자적 CPU 간 동작 방식의 차이 (Khác biệt nguyên lý hoạt động cơ/điện và điện tử)
    - 데이터 전송 속도의 차이 (Khác biệt tốc độ)
    - 데이터 코드와 CPU 워드 형식의 차이 (Khác biệt định dạng dữ liệu)
    - 전압 레벨의 차이 (Khác biệt mức điện áp)
- **입·출력 버스 (I/O Bus):**
  - 주기억장치와 입·출력장치 사이의 데이터 전송을 위해 공통으로 연결된 버스. (Bus chung để truyền dữ liệu.)
  - 구성 (Thành phần): 데이터 버스 (Data Bus), 주소 버스 (Address Bus), 제어 버스 (Control Bus).

- **Vietnamese Explanation:** CPU chạy bằng điện tử cực nhanh, trong khi máy in, bàn phím (thiết bị I/O) chạy cơ học nên rất chậm. I/O Interface và I/O Controller đứng ở giữa làm "người phiên dịch" và "bộ đệm" để hai bên hiểu nhau và không làm CPU phải chờ đợi quá lâu.
- **Ví dụ (Example):** Bạn (CPU) nói tiếng Việt cực nhanh. Một người nước ngoài (I/O) nghe tiếng Anh cực chậm. I/O Interface chính là một anh phiên dịch viên kiêm ghi chép lại, để bạn cứ nói một lèo xong đi làm việc khác, anh ta sẽ từ từ dịch và truyền đạt lại cho người nước ngoài.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Bus Vào/Ra có 3 làn đường: Dữ liệu (chở hàng) - Địa chỉ (chỉ đường) - Điều khiển (cảnh sát giao thông).

---

## 핵심 100: 기억장치와 입·출력장치의 동작 (Memory vs I/O Devices Operation / Hoạt động của bộ nhớ và I/O)

기억장치는 처리 속도가 nano(10^-9) 단위인 전자적인 장치이고, 입·출력장치는 milli(10^-3) 단위인 기계적인 장치이므로 동작 방식에는 많은 차이가 있다.

| 비교 항목 (So sánh) | 입·출력장치 (Thiết bị I/O) | 기억장치 (Bộ nhớ) |
|---|---|---|
| 동작의 속도 (Tốc độ) | 느리다 (Chậm) | 빠르다 (Nhanh) |
| 동작의 자율성 (Tính tự chủ) | 타율/자율 (Phụ thuộc/Tự chủ) | 타율 (Phụ thuộc) |
| 정보의 단위 (Đơn vị thông tin) | Byte(문자) | Word |
| 착오 발생률 (Tỷ lệ lỗi) | 많다 (Nhiều) | 적다 (Ít) |

- **Vietnamese Explanation:** Bộ nhớ lưu trữ dưới dạng Word, tốc độ ánh sáng (Nano giây), lỗi ít. I/O lưu dạng Byte (ký tự), tốc độ rùa bò (Milli giây) do dùng cơ học, lỗi nhiều hơn (kẹt giấy, nhiễu phím).
- 💡 **Mẹo ghi nhớ (Mnemonics):** I/O = Chậm, Nhiều lỗi, Ký tự (Byte). Nhớ đến cái máy in rùa bò hay kẹt giấy.

---

## 핵심 101: 스풀링(SPOOLING)과 버퍼링(Buffering) (Spooling vs Buffering)

### 스풀링 (SPOOLING: Simultaneous Peripheral Operation On-Line)
- 디스크를 이용하여 입·출력할 데이터를 디스크에 모았다가 나중에 한꺼번에 입·출력하는 기법이다. (Dùng đĩa từ (HDD) làm bộ đệm khổng lồ chứa dữ liệu I/O, sau đó xử lý hàng loạt.)
- 고속의 CPU와 저속의 입·출력장치가 동시에 독립적으로 동작하게 하여 효율을 높인다. (Giúp CPU tốc độ cao và thiết bị I/O tốc độ thấp hoạt động song song độc lập, không phải đợi nhau.)

| 구 분 (Phân별) | 버퍼링 (Buffering) | 스풀링 (Spooling) |
|---|---|---|
| 저장위치 (Vị trí lưu) | 주기억장치 (RAM) | 보조기억장치 (Disk) |
| 운영방식 (Hoạt động) | 단일작업 (Đơn nhiệm) | 다중작업 (Đa nhiệm) |
| 구현방식 (Thực hiện) | 하드웨어 (Hardware) | 소프트웨어 (Software) |
| 입·출력방식 (I/O) | 큐 (Queue) | 큐 (Queue) |

- **Vietnamese Explanation:** Buffering dùng RAM để đệm tạm thời cho một công việc. Spooling dùng Đĩa cứng (Disk) làm bộ đệm cho nhiều công việc cùng lúc. Cả hai đều dùng hàng đợi (Queue - FIFO) để giải quyết chênh lệch tốc độ.
- **Ví dụ (Example):** In tài liệu. Nếu dùng Buffering, bạn chỉ in được 1 file, máy tính phải giữ RAM cho nó. Dùng Spooling (như hệ thống máy in hiện đại), bạn ấn in 10 file liên tục, nó lưu tạm ra ổ cứng (Spool), rồi tự động in dần, bạn có thể đi làm việc khác.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Buffer = RAM, Đơn nhiệm, Phần cứng. Spool = Disk, Đa nhiệm, Phần mềm.

---

## 핵심 102: 입·출력(Input-Output) 제어 방식 (I/O Control Methods / Các phương pháp điều khiển I/O)

- **Programmed I/O (Bằng chương trình):**
  - CPU가 상태 Flag를 계속 조사하여 자료 전송을 CPU가 직접 처리. (CPU liên tục kiểm tra cờ trạng thái để tự truyền dữ liệu - Polling).
  - CPU는 계속 I/O 작업에 관여해야 하기 때문에 다른 작업을 할 수 없다는 단점. (CPU bị kẹt, không làm được việc khác).
- **Interrupt I/O (Bằng ngắt):**
  - 인터럽트 인터페이스가 컴퓨터에게 알려 입·출력이 이루어지는 방식. (Khi I/O sẵn sàng sẽ gửi ngắt báo cho CPU).
  - CPU가 계속 Flag를 검사하지 않아도 되기 때문에 Programmed I/O보다 효율적임. (CPU rảnh rỗi hơn).
- **DMA (Direct Memory Access - Truy cập bộ nhớ trực tiếp):**
  - 입·출력장치가 직접 주기억장치를 접근하여 입·출력 전송이 CPU의 레지스터를 경유하지 않고 수행됨. (I/O giao tiếp trực tiếp với RAM, bỏ qua CPU).
  - CPU는 I/O 동작을 개시시킨 후 더 이상 간섭하지 않음. (CPU chỉ ra lệnh bắt đầu, sau đó phó mặc cho bộ điều khiển DMA).
  - **Cycle Steal (Trộm chu kỳ):** DMA 제어기와 CPU가 주기억장치를 동시에 Access 할 때 우선순위를 데이터 채널에게 주는 방식. (DMA mượn một chu kỳ bộ nhớ của CPU để truyền 1 Word).
- **Channel (Kênh):**
  - 주기억장치와 입·출력장치 사이에서 입·출력을 제어하는 입·출력 전용 프로세서(IOP). (Một bộ vi xử lý riêng biệt chỉ dành cho I/O - đỉnh cao của DMA).
  - 종류 (Các loại kênh): Selector Channel (Kênh chọn lọc - cho 1 thiết bị nhanh), Multiplexer Channel (Kênh ghép kênh - cho nhiều thiết bị chậm), Block Multiplexer (Ghép khối - nhiều thiết bị nhanh).

| Interrupt vs Cycle Steal | Interrupt (Ngắt) | Cycle Steal (Trộm chu kỳ) |
|---|---|---|
| Chạy chương trình | CPU dừng chương trình hiện tại để chạy dịch vụ ngắt. | CPU vẫn chạy ngầm các lệnh không cần RAM, nhưng bị mất 1 chu kỳ RAM. |
| Lưu trạng thái | CPU의 상태 보존이 필요하다 (Phải lưu trạng thái CPU). | CPU의 상태 보존이 필요 없다 (Không cần lưu trạng thái CPU). |

- **Vietnamese Explanation:** Có 4 cấp độ I/O: 
  1. Programmed: CPU hỏi liên tục "Xong chưa?". Rất mệt mỏi.
  2. Interrupt: I/O tự báo "Xong rồi!" bằng ngắt. CPU rảnh hơn.
  3. DMA: CPU cấp quyền, I/O tự bưng dữ liệu vào RAM, thỉnh thoảng trộm 1 nhịp của CPU (Cycle steal).
  4. Channel: Thuê hẳn một quản lý riêng (IOP) chuyên làm I/O, CPU không cần quan tâm nữa.
- **Ví dụ (Example):** Chuyển nhà.
  - Programmed: Bạn tự khuân từng thùng và liên tục chạy ra xe xem xe tải đến chưa.
  - Interrupt: Bạn đóng thùng trong nhà, khi nào xe tải đến bấm còi (Ngắt) bạn mới chạy ra.
  - DMA: Bạn thuê thợ bốc vác (DMA), họ tự khuân thùng lên xe, thỉnh thoảng cản đường bạn 1 giây (Cycle Steal).
  - Channel: Bạn thuê cty chuyển nhà trọn gói, bạn xách vali đi du lịch, họ tự làm hết.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự xịn dần: Program (Gà mờ) -> Interrupt (Biết việc) -> DMA (Độc lập) -> Channel (Chuyên nghiệp). Cycle Steal KHÔNG lưu trạng thái CPU.

---

## 핵심 103: 인터럽트의 종류 및 발생 원인 (Types and Causes of Interrupts / Các loại ngắt)

- **외부 인터럽트 (External Interrupt - Ngắt bên ngoài):** Do tín hiệu phần cứng.
  - 전원 이상 (Power Fail): Mất điện, nguồn lỗi.
  - 기계 착오 (Machine Check): Lỗi phần cứng CPU.
  - 외부 신호 (External Signal): Hết thời gian Timer, bấm bàn phím (Ctrl+C), thiết bị ngoài gọi.
  - 입·출력 (I/O): I/O xong việc, hoặc I/O lỗi.
- **내부 인터럽트 (Internal Interrupt - Ngắt bên trong / Trap):** Do CPU thực thi lệnh lỗi.
  - 프로그램 검사 (Program Check): Chia cho 0 (Divide by zero), Tràn bộ nhớ (Overflow/Underflow), Lệnh sai, Truy cập bộ nhớ trái phép.
- **소프트웨어 인터럽트 (Software Interrupt - Ngắt phần mềm):** Do người lập trình cố ý gọi.
  - SVC (SuperVisor Call): Gọi hệ điều hành để xử lý I/O phức tạp hoặc cấp quyền.

- **Vietnamese Explanation:** Ngắt (Interrupt) là hành động chen ngang khiến CPU phải dừng việc hiện tại để xử lý việc khẩn cấp. Có 3 loại: Ngắt ngoài (do môi trường, thiết bị phần cứng), Ngắt trong/Trap (do phần mềm chạy ngu như chia cho 0), Ngắt phần mềm (do lập trình viên cố ý xin HĐH giúp đỡ bằng lệnh SVC).
- **Ví dụ (Example):** Bạn đang làm bài tập (CPU).
  - Ngắt ngoài: Mất điện (Power), Điện thoại reo (External), Bút hết mực (Machine).
  - Ngắt trong: Bài toán quá khó vô lý như 5 chia 0, bộ não bạn bị khựng lại (Trap).
  - Ngắt phần mềm: Bạn chủ động giơ tay gọi thầy giáo (HĐH) lại hỏi bài (SVC).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trap (Bẫy) = Lỗi phần mềm (Chia 0, Tràn số). SVC = Chủ động gọi Giám sát (Supervisor).

---

## 핵심 104 & 105: 인터럽트 처리 (Interrupt Handling / Xử lý ngắt)

### CPU가 확인할 사항 (Những gì CPU cần xác nhận / lưu lại)
- 프로그램 카운터의 내용 (Nội dung Program Counter - Địa chỉ lệnh tiếp theo).
- 사용한 모든 레지스터의 내용 (Nội dung tất cả thanh ghi đang dùng).
- 상태 조건의 내용(PSW - Program Status Word).
*Việc lưu lại (Context Saving) thường được cất ở vùng nhớ stack hoặc vị trí 0.*

### 동작 순서 (Thứ tự hoạt động)
1. 요청 (Yêu cầu): 인터럽트 요청 신호 발생.
2. 중단 (Dừng): 현재 실행중이던 명령어(Micro Instruction)는 끝까지 실행함 (Hoàn thành vi lệnh đang chạy).
3. 보존 (Lưu trạng thái): 현재의 프로그램 상태(PC, PSW)를 보존.
4. 식별 (Xác định): 인터럽트를 요청한 장치를 식별.
5. 처리 (Xử lý): 인터럽트 서비스(취급) 루틴을 실행. (Chạy Service Routine).
6. 복구 (Phục hồi): 상태 복구 (Lấy lại PC cũ).
7. 재개 (Tiếp tục): 중단된 프로그램 실행 재개.

- **Vietnamese Explanation:** Khi có ngắt, CPU không được bỏ ngang lệnh đang làm dở (mức vi lệnh), phải hoàn thành nó. Sau đó lưu ngay địa chỉ PC và các cờ trạng thái để lát sau còn biết đường quay lại. Xác định xem ai gọi, chạy đoạn code xử lý ngắt, xong xuôi thì nạp lại PC và tiếp tục công việc cũ.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự: Gọi -> Chờ nốt -> Cất đồ -> Xem ai -> Giải quyết -> Lấy lại đồ -> Làm tiếp. (Lưu PC là quan trọng nhất).

---

## 핵심 106 & 107: 인터럽트 우선순위 (Interrupt Priorities / Mức độ ưu tiên của Ngắt)

- **우선순위 (Cao -> Thấp):** 
  전원 이상 (Power Fail) > 기계 착오 (Machine) > 외부 신호 (External) > 입·출력 (I/O) > 명령어 잘못 (Program Check) > SVC
- **판별 방법 (Cách phân định ai được ưu tiên):**
  - **Polling (소프트웨어적 방법 - Phần mềm):** CPU dùng code để hỏi vòng tròn từng thiết bị xem ai ngắt. Đổi ưu tiên dễ, nhưng **chậm**.
  - **Daisy-Chain (직렬 하드웨어 - Phần cứng nối tiếp):** Nối dây thành chuỗi. Ai ở đầu dây (gần CPU) thì ưu tiên cao.
  - **병렬 우선순위 / Vectored Interrupt (병렬 하드웨어 - Phần cứng song song):** Dùng Mask Register để ngắt theo bit. Nhanh nhất vì thiết bị tự cung cấp **Interrupt Vector** (địa chỉ xử lý ngắt) cho CPU, nhưng tốn kém phần cứng.

- **Vietnamese Explanation:** Ngắt cũng có cấp bách. Mất điện là kinh khủng nhất (số 1), rồi đến cháy máy. Các ngắt phần mềm (SVC) thì ưu tiên thấp nhất. Để biết ai ngắt, có thể dùng code để quét (Polling - chậm), hoặc nối dây cứng (Daisy Chain/Vector - nhanh). Vector Interrupt là "ngắt có định hướng", thiết bị tự chỉ cho CPU biết phải chạy đoạn code nào.
- **Ví dụ (Example):** Có 3 người giơ tay. 
  - Polling: Cô giáo đi hỏi từng người "Em hỏi gì?". Rất chậm.
  - Daisy Chain: Xếp thành hàng dọc, ai đứng trước nói trước.
  - Vector: Học sinh giơ sẵn tờ giấy ghi số trang cần hỏi, giáo viên nhìn là biết luôn (Vector chỉ hướng).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Thứ tự: Điện (Power) - Máy (Machine) - Ngoài (External) - Vào/Ra (I/O) - Lỗi (Program) - Gọi (SVC). Polling = Phần mềm (Chậm). Daisy = Nối tiếp. Vector = Phần cứng (Nhanh nhất).

---

## 핵심 108 & 109: 기억장치의 특성 및 ROM (Memory Characteristics & ROM)

### 특성을 결정하는 요소 (Yếu tố quyết định đặc tính bộ nhớ)
- **Access Time (Thời gian truy cập):** Thời gian từ lúc yêu cầu đến lúc lấy được dữ liệu.
  `Access Time = Seek Time + Latency Time (Search Time) + Transmission Time`
- **Cycle Time (Thời gian chu kỳ):** Thời gian từ lúc đọc xong tín hiệu này đến lúc có thể đọc tín hiệu tiếp theo.
  `Cycle Time ≥ Access Time` (Cycle time luôn lớn hơn hoặc bằng Access Time).
- **Bandwidth (대역폭/전송률 - Băng thông):** Tốc độ truyền dữ liệu tối đa trong 1 giây (đơn vị bit/s hoặc byte/s). Băng thông càng lớn máy càng nhanh.
- **접근 속도 (Tốc độ tiếp cận Nhanh -> Chậm):** CPU 레지스터 -> Cache -> RAM(Main Memory) -> ROM -> 자기 코어 -> 자기 디스크 (HDD) -> 자기 테이프 (Tape).

### ROM (Read Only Memory - Bộ nhớ chỉ đọc)
- 전원이 꺼져도 내용이 지워지지 않는 비휘발성 (Không bay hơi khi mất điện).
- 주로 기본 입·출력 시스템(BIOS), 자가 진단 프로그램(POST) 저장 (Thường chứa BIOS, POST).
- **ROM 종류 (Các loại ROM):**
  - Mask ROM: Nhà máy làm sẵn, không đổi được.
  - PROM: Ghi được **1번** (1 lần).
  - EPROM: 자외선 (Tia cực tím - UV) để xóa, ghi lại nhiều lần.
  - EEPROM (EAROM): 전기적인 방법 (Phương pháp điện - Electrical) để xóa và ghi. (Ví dụ: USB Flash Drive, SSD).

- **Vietnamese Explanation:** Cycle Time luôn dài hơn Access Time vì bộ nhớ cần thời gian phục hồi lại năng lượng sau khi đọc. ROM giữ lại dữ liệu khi mất điện, có nhiều loại từ cứng nhắc (Mask) đến linh hoạt (EEPROM - dùng điện để xóa). 
- **Ví dụ (Example):** EEPROM chính là công nghệ đằng sau cái USB nhỏ xinh bạn hay dùng. EPROM thì giống cái bảng viết phấn, bôi đi bằng tia UV (giẻ lau) rồi viết lại. Mask ROM là bia đá khắc chữ sẵn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** "E" đầu tiên = Erasable (Xóa được). Nhớ: EPROM = UV (Tia cực tím), EEPROM = Điện (Electonic). Cycle Time ≥ Access Time.

## 핵심 110: RAM (Random Access Memory)

- 자유롭게 읽고 쓸 수 있는 기억장치로, RWM(Read Write Memory)이라고도 한다. (Bộ nhớ có thể đọc và ghi tự do.)
- RAM에는 현재 사용중인 프로그램이나 데이터가 저장되어 있다. (Lưu trữ chương trình và dữ liệu đang được sử dụng hiện tại.)
- 전원이 꺼지면 기억된 내용이 모두 사라지는 휘발성 메모리이다. (Bộ nhớ dễ bay hơi, mất dữ liệu khi tắt nguồn.)
- 일반적으로 ‘주기억장치’ 또는 ‘메모리’라고 하면 램을 의미한다. (Thường được gọi là bộ nhớ chính hoặc đơn giản là 'bộ nhớ'.)

| 구분 (Phân loại) | DRAM (Dynamic RAM - RAM động) | SRAM (Static RAM - RAM tĩnh) |
|---|---|---|
| 구성소자 (Thành phần) | 콘덴서 (Tụ điện) | 플립플롭 (Flip-Flop) |
| 특징 (Đặc điểm) | 전하가 방전되므로 주기적인 재충전(Refresh)이 필요함 (Cần làm mới định kỳ do tụ điện bị phóng điện) | 전원이 공급되는 동안에는 기억 내용이 유지 (Giữ nội dung miễn là có nguồn) |
| 전력소모 (Tiêu thụ điện) | 적음 (Ít) | 많음 (Nhiều) |
| 접근속도 (Tốc độ) | 느림 (Chậm) | 빠름 (Nhanh) |
| 집적도 (Mật độ) | 높음 (Cao - dung lượng lớn) | 낮음 (Thấp - dung lượng nhỏ) |
| 가격 (Giá) | 저가 (Rẻ) | 고가 (Đắt) |
| 용도 (Sử dụng cho) | 일반적인 주기억장치 (Bộ nhớ chính thông thường) | 캐시 메모리 (Bộ nhớ đệm / Cache) |

- **Vietnamese Explanation:** RAM là bộ nhớ làm việc của máy tính. DRAM rẻ, dung lượng cao nhưng chậm và hay quên (phải refresh liên tục), thường dùng làm thanh RAM máy tính. SRAM đắt, dung lượng nhỏ nhưng cực nhanh, không cần refresh, dùng làm Cache trong CPU.
- **Ví dụ (Example):** SRAM giống như bộ nhớ ngắn hạn của bạn khi tính nhẩm (nhanh nhưng nhớ được ít số). DRAM giống như cuốn sổ nháp (nhớ được nhiều nhưng phải tra cứu chậm hơn, và chốc chốc phải tô lại chữ mờ - refresh).
- 💡 **Mẹo ghi nhớ (Mnemonics):** **S**RAM = **S**iêu tốc (Flip-Flop, Cache). **D**RAM = **D**ump (Đổ liên tục - Refresh, Tụ điện, RAM thường).

---

## 핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)

### RAM/ROM의 용량 계산 (Tính dung lượng RAM/ROM)
- 주소선 (Address Bus) số lượng quyết định số Word: Nếu có n đường thì có 2^n Word. (Liên quan đến MAR và PC).
- 데이터 버스 (Data Bus) số lượng quyết định kích thước mỗi Word. (Liên quan đến MBR và IR).
- `Dung lượng = Số Word × Kích thước Word`. Ví dụ: 7 Address lines, 8 Data lines => 2^7 × 8 Bit = 128 × 8 Bit.

### 자기 코어 (Magnetic Core - Lõi từ)
- 부피에 비해 용량이 작고 가격이 비싸 현재는 거의 사용하지 않는다. (Dung lượng nhỏ, giá đắt, ít dùng hiện nay.)
- 데이터를 읽으면 읽은 내용이 지워지는 파괴 메모리(DRO Memory)이므로, 재저장(Restoration Time) 시간이 필요하다. (Đọc xong là mất dữ liệu (Phá hủy), nên cần thời gian ghi lại.)
- Cấu tạo: 구동선(X, Y) 2개 (2 dây chọn địa chỉ), 센스 선 1개 (1 dây cảm biến trạng thái), 금지선 1개 (1 dây cấm).

- **Vietnamese Explanation:** Kích thước bộ nhớ phụ thuộc vào Address Bus (chiều dài) và Data Bus (chiều rộng). Lõi từ là công nghệ cổ, đọc xong bị mất dữ liệu nên phải tốn thời gian khôi phục, hiện không còn dùng.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 자기 코어 (Magnetic Core) = Đọc là Mất (DRO), Cần ghi lại. 4 dây = 2 X/Y + 1 Sense + 1 Inhibit.

---

## 핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)

### 보조기억장치 (Bộ nhớ phụ)
- 주기억장치에 비해 속도는 느리지만 저장 용량이 크다. 전원이 차단되어도 내용이 그대로 유지된다. (Chậm hơn RAM nhưng dung lượng lớn, lưu trữ vĩnh viễn.)
- **자기 테이프 (Magnetic Tape - Băng từ):**
  - 순차처리(SASD)만 할 수 있는 대용량 저장매체. (Chỉ truy cập tuần tự, không nhảy cóc được.)
  - 자료의 백업용으로 많이 사용함. (Thường dùng để Backup.)
- **자기 디스크 (Magnetic Disk - Đĩa từ / HDD):**
  - 순차, 비순차(직접) 처리가 모두 가능한 DASD 방식. (Có thể truy cập trực tiếp ngẫu nhiên.)
  - **Track (Rãnh):** Vòng tròn đồng tâm.
  - **Sector (Cung):** Track chia nhỏ, là đơn vị lưu trữ cơ bản.
  - **Cylinder (Trụ):** Tập hợp các track cùng vị trí trên các mặt đĩa.

### 디스크의 Access Time (Thời gian truy cập đĩa)
- `Access Time = Seek Time + Latency Time (Rotational Delay) + Transmission Time`
- **Seek Time (Thời gian tìm rãnh):** Đầu đọc di chuyển đến đúng Track.
- **Latency Time (Thời gian chờ xoay):** Đợi đĩa xoay đúng đến Sector cần đọc.
- **Transmission Time (Thời gian truyền):** Đọc Sector và truyền vào RAM.

- **Vietnamese Explanation:** Tape giống như băng cassette (muốn nghe bài 5 phải tua qua bài 1,2,3,4). Disk giống như đĩa CD hoặc đĩa than, bạn có thể đặt kim đọc vào bất kỳ bài nào (DASD).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Công thức tìm ổ cứng: SLT. **S**eek (Tìm Track) -> **L**atency (Đợi Sector xoay tới) -> **T**ransmission (Truyền đi).

---

## 핵심 115 & 116: 연관 기억장치 및 메모리 인터리빙 (Associative Memory & Memory Interleaving)

### 연관 기억장치 (Associative Memory / CAM)
- 주소에 의해 접근하지 않고, 기억된 내용의 일부를 이용하여 접근할 수 있는 기억장치. (Không tìm bằng Địa chỉ, mà tìm bằng Nội dung - Content Addressable Memory.)
- 정보 검색이 신속하다. (Tìm kiếm thông tin cực nhanh.)
- 캐시 메모리나 가상 메모리 매핑 테이블에 사용된다. (Dùng trong Cache hoặc Bảng ánh xạ bộ nhớ ảo.)
- 하드웨어 비용이 증가한다. (Tốn kém phần cứng vì cần mạch so sánh song song.)

### 메모리 인터리빙 (Memory Interleaving)
- CPU가 각 모듈로 전송할 주소를 교대로 분산 배치한 후 차례대로 전송하여 여러 모듈을 병행 접근하는 기법. (Kỹ thuật phân tán địa chỉ bộ nhớ thành nhiều module độc lập để CPU truy cập song song cùng lúc.)
- 캐시 기억장치, 고속 DMA 전송 등에서 많이 사용된다. (Dùng trong Cache và DMA tốc độ cao.)

- **Vietnamese Explanation:** Associative Memory giống như việc bạn gọi "Ai tên Nam đứng lên!" thay vì hỏi "Học sinh số báo danh 10 tên gì?". Nhanh nhưng tốn kém (ai cũng phải tự vểnh tai nghe). Interleaving giống như có 4 làn thu phí thay vì 1 làn, xe cộ (dữ liệu) sẽ phân tán đi qua 4 làn cùng lúc, giảm tắc nghẽn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** CAM (Content) = Tìm bằng Nội dung. Interleaving (Xen kẽ) = Đa Module, Truy cập song song.

---

## 핵심 117: 캐시 메모리 (Cache Memory)

- CPU의 속도와 메모리의 속도 차이를 줄이기 위해 사용하는 고속 Buffer Memory. (Bộ đệm tốc độ cao giảm chênh lệch tốc độ giữa CPU và RAM.)
- 캐시 메모리는 메모리 계층 구조에서 가장 빠른 소자 (Nhanh nhất trong hệ thống phân cấp bên ngoài register, dùng SRAM.)
- `적중률 (Hit Ratio) = 적중 횟수(Hits) / 총 접근 횟수 (Total Accesses)`

### 매핑 프로세스 (Mapping Process)
- 주기억장치로부터 캐시 메모리로 데이터를 전송하는 방법 (Cách ánh xạ RAM vào Cache.)
- 종류: 직접(Direct) 매핑, 어소시에이티브(Associative) 매핑, 세트-어소시에이티브(Set-Associative) 매핑.

### 쓰기 정책 (Write Policy)
- 캐시에 저장되어 있는 데이터에 수정이 발생했을 때 주기억장치에 갱신하는 시기와 방법. (Khi Cache bị thay đổi, khi nào thì ghi lại vào RAM?)
- **Write-Through:** 쓰기 동작이 이루어질 때마다 캐시와 주기억장치를 동시에 갱신. (Ghi đồng thời cả 2, an toàn nhưng chậm.)
- **Write-Back:** 캐시로부터 제거될 때 주기억장치에 복사. (Chỉ ghi vào RAM khi bị đuổi khỏi Cache, nhanh nhưng rủi ro nếu mất điện.)

- **Vietnamese Explanation:** Cache giống như cái ví tiền lẻ (SRAM) bạn để túi quần. RAM là két sắt (DRAM) ở nhà. Lấy tiền lẻ nhanh hơn về nhà mở két. 
- 💡 **Mẹo ghi nhớ (Mnemonics):** Write-Through (Xuyên qua) = Ghi luôn vào RAM (Chậm, Chắc). Write-Back (Ghi lại sau) = Khi nào dọn Cache mới ghi (Nhanh, Nguy hiểm).

---

## 핵심 118: 가상 기억장치 (Virtual Memory)

- 기억 용량이 작은 주기억장치를 마치 큰 용량을 가진 것처럼 사용할 수 있도록 하는 운영체제의 메모리 운영 기법. (Lấy một phần ổ cứng ảo hóa thành RAM, giúp máy tính chạy được các chương trình nặng hơn dung lượng RAM thực tế.)
- 보조기억장치는 디스크 같은 DASD 장치이어야 한다. (Bắt buộc dùng đĩa từ / HDD / SSD - DASD, không dùng băng từ được.)
- **주소의 사용 (Địa chỉ):**
  - **가상 주소 (Virtual Address):** Địa chỉ ảo trên ổ cứng. Đơn vị thay thế là Page (Trang).
  - **실기억 주소 (Physical Address):** Địa chỉ thực trên RAM. Đơn vị thay thế là Block / Frame.
- **페이지 부재 (Page Fault):** 가상 페이지가 주기억장치에 없는 경우. 프로그램 수행이 중단된다. (Khi dữ liệu cần tìm không có trong RAM mà nằm trên đĩa, CPU phải tạm dừng để lấy vào.)
- **주소 매핑 (Address Mapping):** 가상주소를 실기억주소로 변환하는 작업이다. 사상함수가 사용된다. (Đổi địa chỉ Ảo thành địa chỉ Thực qua hàm ánh xạ.)

- **Vietnamese Explanation:** Khi RAM 4GB nhưng game nặng 10GB, HĐH dùng ổ cứng làm RAM ảo. RAM ảo chia thành các "Trang" (Page). Khi CPU cần 1 trang mà nó chưa nằm trong RAM thực, nó bị "Page Fault", máy sẽ hơi khựng lại để tải từ ổ cứng lên.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Virtual = Đĩa cứng đóng giả làm RAM. Page Fault (Lỗi trang) = Trang chưa nạp, phải đợi.

---

## 핵심 119 & 120: 병렬 컴퓨터 분류 및 병렬처리기법 (Flynn's Taxonomy & Parallel Processing)

### 플린(Flynn)의 분류 (Phân loại Flynn)
- **SISD (Single Instruction, Single Data):** 1 Lệnh xử lý 1 Dữ liệu. (Máy tính truyền thống Von Neumann).
- **SIMD (Single Instruction, Multi Data):** 1 Lệnh xử lý Nhiều Dữ liệu. (Array Processor, xử lý đồng bộ).
- **MISD (Multi Instruction, Single Data):** Nhiều Lệnh, 1 Dữ liệu. (Không dùng trong thực tế).
- **MIMD (Multi Instruction, Multi Data):** Nhiều Lệnh xử lý Nhiều Dữ liệu. (Máy đa nhân hiện đại - Đa xử lý bất đồng bộ). Tightly Coupled (Multiprocessor), Loosely Coupled (Distributed).

### 병렬처리기법 (Kỹ thuật xử lý song song)
- **파이프라인 프로세서 (Pipeline):** Chia lệnh thành các Sub-task (như dây chuyền nhà máy). Các bước: Fetch, Decode, Operand, Execute.
- **벡터 프로세서 (Vector Processor):** Xử lý mảng dữ liệu cực nhanh (Systolic algorithm).
- **배열 프로세서 (Array Processor):** Có nhiều bộ ALU (Processing Elements), điều khiển tập trung, tính toán song song theo không gian (SIMD).
- **데이터 흐름 컴퓨터 (Data Flow Computer):** Ngược với Von Neumann (Control-flow). Lệnh không chạy theo thứ tự PC, mà cứ hễ **đủ Dữ liệu là chạy** (Không cần Program Counter).

- **Vietnamese Explanation:** SISD là làm việc một mình. SIMD là 1 ông chủ ra lệnh cho 10 người cùng làm. MIMD là 10 người tự làm 10 việc khác nhau. Data Flow là cách làm việc "không cần quản lý", ai có đủ nguyên liệu thì tự động nấu, không cần chờ sếp hô hào.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Flynn: S = Single (Đơn), M = Multi (Đa), I = Instruction (Lệnh), D = Data (Dữ liệu). Data Flow = Data dẫn dắt, Không cần PC.

---

# [과목 2] 소프트웨어 개발 (Subject 2: Software Development)
# Chapter 1. 데이터 입출력 구현 (Data I/O Implementation)

## 023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)

자료구조: 컴퓨터상 자료를 효율적으로 저장하기 위해 만들어진 논리적인 구조 (Cấu trúc logic để lưu trữ dữ liệu hiệu quả).

### 선형 구조 (Linear - Nối tiếp nhau)
- **리스트 (List):** 순서에 의해 나열된 구조. (Cấu trúc tuyến tính).
  - **선형 리스트 (Linear List / Array):** Kích thước cố định (고정), lưu liên tục (연속). Tìm kiếm cực nhanh (검색 빠름), nhưng chèn/xóa cực chậm (삽입, 삭제 느림).
  - **연결 리스트 (Linked List):** Kích thước linh hoạt (가변), liên kết bằng Pointer. Chèn/xóa cực nhanh, nhưng tìm kiếm chậm (phải dò từng cái) và tốn không gian lưu Pointer.
- **스택 (Stack):** LIFO (Last-In-First-Out). Vào/Ra ở một đầu. Dùng cho: Gọi hàm (Subroutine), Lưu địa chỉ trở về, Đệ quy (Recursion), Tính biểu thức toán học, DFS (Duyệt sâu).
- **큐 (Queue):** FIFO (First-In-First-Out). Vào một đầu, ra một đầu. Dùng cho: Lập lịch hệ điều hành (Job Scheduling), Hàng đợi in.
- **데크 (Deque):** Kết hợp Stack và Queue, có thể Vào/Ra ở CẢ HAI đầu.

### 비선형 구조 (Non-linear - Không nối tiếp)
- **트리 (Tree):** Cây. Có Node (Đỉnh) và Branch (Nhánh). **Không có chu trình (Cycle).**
- **그래프 (Graph):** Đồ thị. Có Đỉnh (Vertex) và Cạnh (Edge). Có thể có hướng hoặc vô hướng. (Cây là một dạng Đồ thị không có chu trình).

- **Vietnamese Explanation:** Cấu trúc dữ liệu là cách sắp xếp thông tin. 
  - Linear List như dãy ghế đá (tìm số ghế thì nhanh, nhưng muốn chen vào giữa phải bắt mọi người xích ra). 
  - Linked List như trò chơi nắm tay nhau (muốn chen vào giữa chỉ cần thả tay và nắm người mới, rất dễ, nhưng tìm người thứ 10 thì phải đếm từ đầu).
  - Stack như hộp bóng bàn (LIFO - vứt vào sau thì lấy ra trước). Queue như xếp hàng mua vé (FIFO - ai đến trước mua trước).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Stack = LIFO (Gọi Hàm, Đệ quy). Queue = FIFO (Lập lịch). Liên kết (Linked) = Nhanh chèn/xóa, Chậm tìm kiếm.

---

## 025: 트리 (Tree / Cây)

| 용어 (Thuật ngữ) | 설명 (Giải thích) | 예시 (Ví dụ) |
|---|---|---|
| 루트 노드 (Root Node) | Nút gốc, không có cha. Chỉ có 1 gốc. | A |
| 단말 노드 (Leaf/Terminal Node) | Nút lá, ở cuối cùng, không có con. | D, E, H, I, G |
| 레벨 (Level) | Độ sâu từ gốc tới nút. | E có Level là 3. |
| 깊이 (Depth) | Độ sâu lớn nhất của cây (Max Level - 1 hoặc tùy cách tính). | Depth = 3. |
| 차수 (Degree of Node) | Bậc của một nút: Số lượng con của nút đó. | B có 3 con => Degree = 3. |
| 트리의 차수 (Degree of Tree) | Bậc của cây: Bậc lớn nhất trong tất cả các nút. | Cả cây có nút max là 3 => Degree của cây = 3. |

### 트리 순회 (Tree Traversal - Duyệt cây)
- **전위 순회 (Preorder):** Root -> Left -> Right.
- **중위 순회 (Inorder):** Left -> Root -> Right.
- **후위 순회 (Postorder):** Left -> Right -> Root.

- **Vietnamese Explanation:** Cách tính Bậc của cây rất hay thi: Tìm cái nút nào đẻ nhiều con nhất, số con đó chính là Bậc của toàn bộ cây. Khi duyệt cây, chữ "Pre/In/Post" (Trước/Giữa/Sau) dùng để chỉ vị trí của Root. Root đứng trước là Pre, ở giữa là In, ở cuối là Post.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 단말 (Đoạn mạt = Cuối) = Leaf (Lá). Degree = Bậc = Số con. Pre/In/Post = Vị trí của Gốc (Root).

---

## 026: 그래프 (Graph / Đồ thị)

- **방향 그래프 (Directed Graph):** Có hướng. Tối đa `n(n-1)` cạnh (n là số đỉnh).
- **무방향 그래프 (Undirected Graph):** Vô hướng. Tối đa `n(n-1)/2` cạnh.

### 탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)
- **DFS (Depth-First Search - Tìm kiếm theo chiều sâu):** Đi sâu nhất có thể, hết đường mới lui lại (Dùng Stack).
- **BFS (Breadth-First Search - Tìm kiếm theo chiều rộng):** Loang ra xung quanh, tầng nào xong mới xuống tầng sau (Dùng Queue).

- 💡 **Mẹo ghi nhớ (Mnemonics):** DFS = Sâu = Stack (D/S). BFS = Rộng = Queue (B/Q). Vô hướng chia 2 vì AB và BA là một.

---

## 027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)

### 알고리즘 설계 기법 (Kỹ thuật thiết kế thuật toán)
- **분할과 정복 (Divide & Conquer):** Chia để trị. Chia nhỏ vấn đề đến khi không chia được nữa rồi gộp lại. (VD: Merge Sort, Quick Sort).
- **동적계획법 (Dynamic Programming - Quy hoạch động):** Chia bài toán, nhưng CÓ lưu lại kết quả (bộ nhớ) để tận dụng cho lần sau. (VD: Fibonacci).
- **탐욕법 (Greedy):** Tham lam. Chọn cái tốt nhất ở *ngay thời điểm hiện tại*, không cần biết tương lai.
- **백트래킹 (Backtracking):** Quay lui. Đi thử, nếu thấy bế tắc (không triển vọng - promising) thì quay lại nút cha.

### 시간 복잡도 (Time Complexity - Độ phức tạp thời gian)
- Đếm số lần thực thi các phép toán (không phải tính thời gian bằng giây).
- Biểu diễn: Big-O (최악 - Tệ nhất), Theta (평균 - Trung bình), Omega (최상 - Tốt nhất).
- **Thứ tự (Nhanh -> Chậm):** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- O(1) nghĩa là: Dữ liệu lớn đến đâu thời gian vẫn không đổi.

- **Vietnamese Explanation:** Greedy giống như đi nhặt tiền: cứ thấy tờ to nhất trước mặt là nhặt, bất chấp sau đó dẫn vào ngõ cụt. Dynamic Programming giống như làm toán: kết quả bài 1 lưu ra nháp để dùng cho bài 2.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Divide = Cắt nhỏ. Dynamic = Nhớ bài cũ. Greedy = Tham bát bỏ mâm. Backtrack = Đi lùi. O(1) là nhanh nhất.

---

## 028: 정렬 (Sorting / Thuật toán sắp xếp)

| 알고리즘 (Thuật toán) | 설명 (Giải thích) | 평균 복잡도 (Average) | 최악 (Worst) |
|---|---|---|---|
| 삽입 정렬 (Insertion Sort) | Lấy phần tử thứ i chèn vào đúng vị trí trong mảng con từ 1 tới i-1 đã sắp xếp. | O(n²) | O(n²) |
| 거품 정렬 (Bubble Sort) | So sánh 2 phần tử kề nhau, sai thì đổi chỗ. Phần tử to nhất sẽ "nổi bọt" về cuối. Cần N-1 Pass (Vòng lặp). | O(n²) | O(n²) |
| 선택 정렬 (Selection Sort) | Tìm phần tử nhỏ nhất rồi đổi chỗ nó về vị trí đầu tiên chưa sắp xếp. | O(n²) | O(n²) |
| 퀵 정렬 (Quick Sort) | Chọn Pivot (Chốt), chia làm 2 nửa: Trái nhỏ hơn, Phải to hơn. Lặp lại (Divide & Conquer). | O(n log n) | **O(n²)** |
| 합병 정렬 (Merge Sort) | Chia đôi mảng cho đến khi còn 1 phần tử, sau đó gộp (Merge) lại theo thứ tự. | O(n log n) | O(n log n) |
| 힙 정렬 (Heap Sort) | Dùng cây Complete Binary Tree (Heap) để tìm min/max rồi đưa ra ngoài, cấu trúc lại Heap. | O(n log n) | O(n log n) |

- **Vietnamese Explanation:** Bubble, Selection, Insertion là 3 thuật toán cơ bản, chạy chậm O(n²). Quick, Merge, Heap là thuật toán xịn, chạy nhanh O(n log n). Nhưng Quick Sort xui xẻo (Worst case) vẫn có thể dính O(n²).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Quick Sort (Nhanh) nhưng Worst là N². Bọt (Bubble), Chọn (Selection), Chèn (Insertion) đều là N².

---

## 029 & 030: 검색 알고리즘 및 해싱 (Search Algorithms & Hashing)

### 검색 (Search - Tìm kiếm)
- **순차 검색 (Sequential/Linear Search):** Tìm tuần tự từ đầu đến cuối. Dùng cho mảng *chưa sắp xếp*. O(n).
- **이진 검색 (Binary Search):** Tìm nhị phân. Chia đôi mảng liên tục. **Bắt buộc mảng phải ĐÃ SẮP XẾP.** O(log n). Rất nhanh.

### 해싱 (Hashing - Băm dữ liệu)
- Dùng hàm băm (Hash Function) tính ra trực tiếp địa chỉ bộ nhớ để lưu hoặc tìm kiếm dữ liệu. Nhanh nhất (O(1)).

- **Vietnamese Explanation:** Tìm tuần tự là lật từng trang sách. Tìm nhị phân là mở giữa cuốn từ điển, xem vần nào rồi gập nửa bỏ đi, tìm tiếp ở nửa kia. Băm (Hashing) là nhìn Mục lục rồi lật thẳng trang đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Binary Search = Phải Sắp Xếp (Sắp xếp), Chia đôi (절반). Hashing = O(1) Siêu Tốc.

### 해시 충돌 해결 방법 (Hash Collision Resolution / Các phương pháp giải quyết đụng độ Hash)

| 방법 (Phương pháp) | 설명 (Giải thích) |
|---|---|
| **체이닝 (Chaining - Móc xích)** | 버킷 내에 연결리스트(Linked List)를 할당하여 데이터들을 연결하는 방식. (Dùng danh sách liên kết để nối các phần tử bị đụng độ lại với nhau trong cùng 1 bucket.) |
| **개방 주소법 (Open Addressing - Địa chỉ mở)** | 충돌이 일어났을 때 다른 버킷에 데이터를 삽입해 해결하는 방식. (Khi đụng độ, tìm một ô trống khác để nhét vào. Địa chỉ dữ liệu bị thay đổi so với ban đầu.) |
| 선형 탐색 (Linear Probing) | 해시충돌 시 다음 버킷, 혹은 몇 개를 건너뛰어 삽입. (Thử tuyến tính: Tìm ô trống kế tiếp.) |
| 제곱 탐색 (Quadratic Probing) | 해시충돌 시 제곱만큼 건너뛴 버킷에 삽입 (1, 4, 9, 16...). (Thử bậc hai: Nhảy xa dần theo bình phương để tránh tụ tập.) |
| 이중 해시 (Double Hashing) | 해시충돌 시 다른 해싱함수를 한 번 더 적용. (Băm kép: Dùng thêm một hàm băm phụ để tìm khoảng nhảy.) |

- **Vietnamese Explanation:** Khi hai dữ liệu băm ra cùng một địa chỉ (Collision), ta phải giải quyết. Chaining là cho chúng ở chung một nhà nhưng nối đuôi nhau (như xâu chuỗi). Open Addressing là "nhà này có người rồi, mời anh đi tìm nhà khác". 
- 💡 **Mẹo ghi nhớ (Mnemonics):** Chaining = Dây xích (Linked List). Open Addressing = Mở cửa đi tìm nhà khác (Linear, Quadratic, Double).

---

# Chapter 2. 통합 구현 (Integration Implementation)

## 핵심 031: 모듈 구현 (Module Implementation)

- **구현 (Implementation):** 설계 명세서가 컴퓨터가 알 수 있는 모습으로 변환되는 과정. 프로그래밍 또는 코딩. (Quá trình chuyển thiết kế thành code.)
- **작업 절차 (Trình tự):** 코딩 계획 (Lập kế hoạch) → 코딩 (Code) → 컴파일 (Compile) → 테스트 (Test).
- **모듈 (Module):** 독립적인 기능을 갖는 단위. 모듈이 모이면 프로그램이 됨. (Một đơn vị độc lập thực hiện một chức năng cụ thể.)
- **컴포넌트 (Component):** 독립적으로 존재할 수 있는 부분, 재사용되는 단위, 인터페이스를 통해서만 접근. (Thành phần có thể tái sử dụng, giao tiếp qua Interface.)

- **Vietnamese Explanation:** Module là một khối code (như một hàm hoặc một class). Component là một khối lớn hơn, đóng gói sẵn và có thể lắp ráp vào nhiều phần mềm khác nhau (như một nút bấm UI, một bộ lịch).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự: Kế hoạch -> Code -> Dịch (Compile) -> Thử (Test). Module = Ghép lại thành chương trình. Component = Tái sử dụng qua Interface.

---

## 핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)

### 형상 관리 (Configuration Management)
- 소프트웨어 개발 과정의 **변경 사항을 관리**하는 것. (Quản lý mọi thay đổi trong vòng đời phần mềm - Version Control).
- 대상 (Đối tượng): 계획, 요구 분석서, 설계서, 소스 코드, 테스트 케이스, 지침서 등. (**개발 비용 - Chi phí phát triển KHÔNG nằm trong này**).
- 절차 (Trình tự): 형상 식별 (Nhận dạng) → 형상 통제 (Kiểm soát bởi CCB) → 형상 감사 (Kiểm toán) → 형상 기록 (Ghi lại).

### 형상 관리 방식 (Các phương pháp quản lý phiên bản)
- **공유 폴더 방식 (Shared Folder):** Lưu vào chung một thư mục trên mạng nội bộ. (Ví dụ: RCS).
- **클라이언트/서버 방식 (Client/Server):** Quản lý tập trung trên một máy chủ. (Ví dụ: CVS, SVN).
- **분산 저장소 방식 (Distributed Repository):** Mỗi máy cá nhân đều chứa một bản copy của kho chứa, commit lên máy cá nhân trước rồi mới push lên server. Rất an toàn. (Ví dụ: **Git**).

### 형상 관리 도구 기능 (Chức năng công cụ)
- **Check-In:** Đẩy code lên kho (Upload).
- **Check-Out:** Lấy code mới nhất về (Download).
- **Commit:** Xác nhận lưu sự thay đổi.

### IDE (Integrated Development Environment - Môi trường phát triển tích hợp)
- 코딩, 컴파일, 디버깅, 배포 (Coding, Compile, Debug, Deployment) 기능을 하나로 통합. (Tích hợp tất cả công cụ lập trình vào một phần mềm).
- Ví dụ: Eclipse (Java), Visual Studio (C#, C++), Xcode (iOS), Android Studio, IntelliJ IDEA.

- **Vietnamese Explanation:** Quản lý hình thái (Configuration/Version) giống như việc lưu file "Bao_cao_lan1", "Bao_cao_lan2", "Bao_cao_FINAL". Git (Phân tán) là công cụ phổ biến nhất hiện nay. IDE là bộ công cụ tất cả-trong-một của lập trình viên (vừa gõ code, vừa dịch, vừa tìm lỗi).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Trình tự 형상 quản lý: Nhận Kiểm Đánh Ghi (Nhận diện - Kiểm soát - Đánh giá - Ghi chép). Git = Phân tán (분산). IDE 4 bước: CoCoDeDe (Coding - Compile - Debugging - Deployment).

---

## 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

- **재사용 (Reuse):** 이미 개발되어 인정받았던 소프트웨어의 전체 또는 일부분을 다시 사용하는 기법. (Sử dụng lại code/phần mềm cũ đã được kiểm chứng để tiết kiệm thời gian, chi phí và giảm lỗi.)
- **Phân loại theo kỹ thuật:**
  - **분석 (Analysis):** Hiểu code cũ để chọn cái cần tái sử dụng.
  - **재구조 (Restructuring):** Đổi cấu trúc, không đổi chức năng.
  - **역공학 (Reverse Engineering):** Dịch ngược từ code ra bản thiết kế.
  - **이식 (Migration):** Chuyển sang môi trường / phần cứng mới.
  - **재개발 (Re-Development):** Đập đi xây lại có tham khảo cái cũ.
- **Phân loại theo phạm vi:**
  - Hàm & Đối tượng (Function/Class), Component, Ứng dụng (Application).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Reverse Engineering (Dịch ngược) = Từ Code -> Bản thiết kế. Migration = Chuyển nhà (môi trường).

---

# Chapter 3. 제품 소프트웨어 패키징 (Product Software Packaging)

## 핵심 035 & 036: 소프트웨어 패키징 및 DRM (Software Packaging & DRM)

### 패키징 고려사항 (Lưu ý khi đóng gói)
- **사용자를 중심**으로 진행. (Phải hướng tới người dùng, không phải lập trình viên).
- 보안, 이기종 연동, 복잡성 및 비효율성 문제 고려, 적합한 암호화 알고리즘 적용. (Bảo mật, liên kết đa nền tảng, dễ dùng, mã hóa).

### DRM (Digital Rights Management - Quản lý bản quyền kỹ thuật số)
- 허가된 권한 범위 내에서 콘텐츠의 이용이 가능하도록 통제하는 기술. (Kỹ thuật mã hóa, chống copy lậu, giới hạn số lần mở/in/sao chép nội dung kỹ thuật số).
- **Thành phần (Cấu trúc DRM):**
  - **Contents Provider (Người cung cấp):** Tác giả, người tạo nội dung.
  - **Contents Distributor (Người phân phối):** Nơi bán/phân phối (App Store, Melon...).
  - **Clearing House (Trung tâm thanh toán / Quản lý):** Quản lý Key (khóa), cấp phép License và tính tiền.
  - **Packager (Bộ đóng gói):** Đóng gói nội dung + Meta data + Mã hóa.
  - **DRM Controller (Bộ điều khiển):** Kiểm soát quyền sử dụng trên máy người dùng.

- **Vietnamese Explanation:** DRM là công nghệ chống vi phạm bản quyền (ví dụ: nhạc tải trên Spotify không thể copy ra máy MP3 thường nghe được). Clearing House là trọng tài ở giữa giữ chìa khóa và thu tiền.
- 💡 **Mẹo ghi nhớ (Mnemonics):** DRM = Chống copy lậu. **Clearing House** = Trạm kiểm soát và cấp phép (Rất hay thi). Firewall (Tường lửa) KHÔNG phải là công nghệ của DRM.

---

## 핵심 037 & 038: 매뉴얼 및 빌드/배포 도구 (Manuals & Build/Deploy Tools)

### 제품 소프트웨어 매뉴얼 (Tài liệu hướng dẫn)
- **설치 매뉴얼 (Installation Manual):** Hướng dẫn cài đặt. (Lưu ý cách cài, cấu hình hệ thống, cách xóa cài đặt - Uninstall).
- **사용자 매뉴얼 (User Manual):** Hướng dẫn sử dụng. (Giao diện UI, cấu hình tối thiểu, cách dùng tính năng).
- Cả hai đều phải viết theo góc nhìn của **사용자 (Người dùng)**.

### 빌드 및 모니터링 도구 (Công cụ Build & Monitoring)
- **빌드 자동화 도구 (Build Automation):** Biến source code thành file chạy một cách tự động. Ví dụ: Ant, Maven, Gradle, **Jenkins**.
- **버전 관리 도구 (Version Control):** Git, SVN.
- **정적 분석 도구 (Static Analysis):** Phân tích code tìm lỗi mà **KHÔNG CHẠY** chương trình. Ví dụ: PMD, Cppcheck, SonarQube.
- **동적 분석 도구 (Dynamic Analysis):** Vừa **CHẠY** chương trình vừa tìm lỗi (tràn bộ nhớ, v.v.). Ví dụ: Avalanche, Valgrind.

- **Vietnamese Explanation:** "Tĩnh" (Static) nghĩa là code nằm im trên giấy, dùng tool soi từng dòng xem có viết sai cú pháp hay không. "Động" (Dynamic) là bấm nút chạy phần mềm rồi xem nó có bị sập hay tốn RAM không.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Tĩnh (Static) = PMD, SonarQube (Soi code). Động (Dynamic) = Valgrind (Chạy thử). Build = Jenkins (Ông quản gia tự động).

---

## 핵심 039: 소프트웨어 품질 관련 국제 표준 (Software Quality Standards)

- **ISO/IEC 9126:** Đánh giá chất lượng phần mềm gồm 6 đặc tính: **기신사효유이**
  - **기**능성 (Functionality): Đáp ứng đúng yêu cầu.
  - **신**뢰성 (Reliability): Chạy ổn định, không lỗi, chịu lỗi tốt.
  - **사**용성 (Usability): Dễ hiểu, dễ học, dễ dùng.
  - **효**율성 (Efficiency): Tốn ít tài nguyên, chạy nhanh.
  - **유**지 보수성 (Maintainability): Dễ sửa chữa, bảo trì, phân tích.
  - **이**식성 (Portability): Dễ cài đặt, dễ chuyển sang môi trường/máy khác.
- **ISO/IEC 14598:** Tiêu chuẩn đánh giá quá trình mua/phát triển.
- **ISO/IEC 12119:** Tiêu chuẩn cho gói phần mềm thương mại.
- **ISO/IEC 25000 (SQuaRE):** Tích hợp tất cả các tiêu chuẩn 9126, 14598, 12119.

- **Vietnamese Explanation:** ISO 9126 là kinh điển nhất, bạn phải nhớ 6 chữ cái đầu của 6 đặc tính. Nếu phần mềm khó dùng => Kém "Sử dụng tính". Nếu đổi máy tính mà không chạy được => Kém "Di thực tính" (Portability).
- 💡 **Mẹo ghi nhớ (Mnemonics):** 6 Đặc tính của 9126: "Chức Tín Dùng Hiệu Bảo Di" (Chức năng - Đáng tin - Dễ dùng - Hiệu quả - Bảo trì - Di động). ISO 25000 = Chuẩn xịn nhất tổng hợp tất cả.

---

# Chapter 4. 애플리케이션 테스트 관리 (Application Test Management)

## 핵심 040: 애플리케이션 테스트 원리 및 종류 (Test Principles & Types)

### 테스트의 기본 원리 (Các nguyên lý cơ bản)
- **완벽한 테스팅은 불가능:** Không bao giờ test ra 100% không còn lỗi.
- **결함 집중 (Defect Clustering):** Lỗi thường tập trung ở 20% các module cốt lõi (Quy tắc Pareto 80/20).
- **살충제 패러독스 (Pesticide Paradox):** Nghịch lý thuốc trừ sâu. Dùng mãi một bài test thì không tìm ra lỗi mới. Cần liên tục thay đổi bộ test.
- **정황 의존성 (Context Dependency):** Tùy bối cảnh (web, app, game) mà cách test phải khác nhau.
- **오류-부재의 궤변 (Absence of Errors Fallacy):** App không có lỗi nhưng không đúng ý khách hàng thì vẫn là rác.

### 정적 테스트 vs 동적 테스트 (Static vs Dynamic Test)
- **정적 테스트 (Static):** Không chạy code. Đọc và review code/tài liệu. (Walkthrough, Inspection, Review). Phát hiện lỗi sớm, tiết kiệm tiền.
- **동적 테스트 (Dynamic):** Phải chạy chương trình. Gồm Black Box và White Box testing.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Thuốc trừ sâu (Pesticide) = Cần thay mới bộ Test. Đám mây lỗi (Clustering) = 20% code gây ra 80% lỗi.

---

## 핵심 041: 테스트 케이스 / 시나리오 / 오라클 (Test Case/Scenario/Oracle)

- **테스트 케이스 (Test Case):** Một bộ gồm: Dữ liệu đầu vào, Điều kiện chạy, Kết quả mong đợi.
- **테스트 시나리오 (Test Scenario):** Kịch bản gồm nhiều Test Case nối tiếp nhau.
- **테스트 오라클 (Test Oracle):** Tiêu chuẩn/Cơ chế để tự động đánh giá kết quả test là Đúng hay Sai (True/False).
  - **참 (True):** Kiểm tra 100% mọi trường hợp (Dùng cho máy bay, y tế).
  - **샘플링 (Sampling):** Lấy mẫu ngẫu nhiên vài test case.
  - **추정 (Heuristic):** Lấy mẫu vài cái chắc chắn, còn lại thì dùng logic ước lượng (Heuristic).
  - **일관성 검사 (Consistent):** Kiểm tra xem code cũ và mới có cho kết quả giống nhau không khi bị thay đổi (Hồi quy).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Oracle (Nhà tiên tri) = Cái để phán xét đúng/sai. True = 100%. Heuristic = Đoán.

---

## 핵심 042: 블랙박스 테스트 / 화이트박스 테스트 (Black-Box vs White-Box)

Cả hai đều là **Dynamic Test** (Phải chạy code).

### 블랙박스 테스트 (Black-box / Hộp đen / Dựa trên Chức năng)
- Không quan tâm bên trong code viết gì, chỉ quan tâm Đầu vào -> Đầu ra. (Dựa trên 명세 - Đặc tả).
- **Kỹ thuật (Các loại):**
  - **동등 분할 (Equivalence Partitioning):** Chia vùng tương đương (Vd: Nhập từ 1-100, thì test số 50 là đủ diện cho vùng đúng).
  - **경곗값 분석 (Boundary Value):** Phân tích giá trị biên (Lỗi hay xảy ra ở ranh giới, vd test số 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graph):** Bảng đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm của tester để đoán lỗi.

### 화이트박스 테스트 (White-box / Hộp trắng / Dựa trên Cấu trúc Code)
- Soi thấu bên trong code. Đảm bảo mọi dòng lệnh (Statement), mọi nhánh (Branch/Decision) đều được chạy ít nhất 1 lần.
- **Kỹ thuật (Các loại):**
  - **기본 경로 검사 (Base Path):** Đi qua tất cả các con đường code.
  - **구문 커버리지 (Statement Coverage):** Bao phủ dòng lệnh (Dễ nhất).
  - **결정 커버리지 (Decision/Branch):** Bao phủ nhánh (If True / If False).
  - **조건 커버리지 (Condition):** Bao phủ mọi điều kiện con trong If.
  - **루프 검사 (Loop Testing):** Test các vòng lặp for, while.

- **Vietnamese Explanation:** Black-box giống như lái xe ô tô: đạp ga là chạy, không cần biết động cơ nổ ra sao. White-box giống như thợ máy: tháo tung động cơ ra kiểm tra từng con ốc, từng pít-tông.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 
  - Black-box (Chức năng): Vùng (Partition), Biên (Boundary), Nhờ kinh nghiệm (Guessing).
  - White-box (Cấu trúc code): Dòng lệnh (Statement), Nhánh (Branch), Điều kiện (Condition), Vòng lặp (Loop).

---

## 핵심 043: 단위 / 통합 / 시스템 / 인수 테스트 (Test Levels)

Thứ tự Test từ nhỏ đến lớn: **단위 (Unit) → 통합 (Integration) → 시스템 (System) → 인수 (Acceptance)**.

| 단계 (Giai đoạn) | 설명 (Giải thích) | 방식 / 기법 (Cách thức) |
|---|---|---|
| **단위 (Unit Test)** | Test từng Module, hàm độc lập. | White-box, Black-box, Test cấu trúc dữ liệu. |
| **통합 (Integration)** | Nối các module lại và test sự giao tiếp giữa chúng. | - **빅뱅 (Big Bang):** Gom tất cả test 1 lần (dễ bị rối).<br>- **상향식 (Bottom-Up):** Dưới lên. Cần **Driver** (Trình điều khiển giả).<br>- **하향식 (Top-Down):** Trên xuống. Cần **Stub** (Mô đun con giả mạo). |
| **시스템 (System)** | Test toàn bộ hệ thống xem có đúng yêu cầu (Chức năng + Hiệu năng). | Yêu cầu chức năng và phi chức năng. |
| **인수 (Acceptance)** | Khách hàng/Người dùng cuối tự test để nghiệm thu. | - **알파 (Alpha):** Khách hàng test tại cty lập trình viên, có dev đứng ngó.<br>- **베타 (Beta):** Tung ra cho nhiều người dùng tự test ở nhà (Field Test), tự do. |

- **Vietnamese Explanation:** Tích hợp (Integration) rất hay ra thi. Nếu ráp từ dưới lên (Bottom-up) thì module con xong rồi, nhưng thiếu thằng gọi nó => Cần viết cục **Driver** giả để gọi. Nếu ráp từ trên xuống (Top-down), module chính có rồi nhưng chưa viết xong module con => Cần viết cục **Stub** (Cục gạch giả) để thế chỗ. Alpha test là test "nội bộ" có kiểm soát, Beta test là "open beta" như game.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Từ trên xuống (Top-Down) = Stub (Top-Stub / T-S). 상향식 (Bottom-Up) = Driver (Bottom-Driver / B-D). Alpha = Ở cty Dev. Beta = Ở nhà.

---

## 핵심 044: 테스트 자동화 도구 (Test Automation Tools)

- **정적 분석 도구 (Static Analysis):** Phân tích không cần chạy code.
- **성능 테스트 도구 (Performance Test):** Tạo ra người dùng ảo (Virtual Users) để ép tải, đo đạc băng thông, thời gian phản hồi (Load/Stress testing).
- **테스트 드라이버 (Test Driver):** Dùng trong Bottom-up. Gọi module con, truyền tham số.
- **테스트 스텁 (Test Stub):** Dùng trong Top-down. Module giả mạo, làm hình nộm trả về kết quả ảo cho module trên.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Driver (Tài xế) = Kẻ điều khiển từ trên. Stub (Gốc cây/Khúc gỗ) = Đứng ở dưới chịu đòn giả.

## 핵심 클린 코드 작성 원칙 (Clean Code Principles)

- **클린 코드 (Clean Code):** 누구나 쉽게 이해하고 수정 및 추가할 수 있는 단순 명료한 코드. (Code sạch: Dễ hiểu, dễ sửa, dễ thêm tính năng.)
- **배드 코드 (Bad code):** 프로그램의 로직이 복잡하고 이해하기 어려운 코드. (Code rác: Lộn xộn, logic phức tạp.)
- **외계인 코드 (Alien Code):** 매우 오래되거나 참고 문서 또는 개발자가 없어 유지보수 작업이 매우 어려운 코드. (Code "người ngoài hành tinh": Code cổ đại, người viết đã nghỉ việc, không có tài liệu, đụng vào là hỏng.)

| 작성 원칙 (Nguyên tắc) | 설명 (Giải thích) |
|---|---|
| **가독성 (Readability)** | 누구든지 코드를 쉽게 읽을 수 있도록 작성. 이해하기 쉬운 용어, 들여쓰기. (Dễ đọc: Tên biến rõ ràng, thụt lề chuẩn.) |
| **단순성 (Simplicity)** | 한 번에 한 가지를 처리하도록 작성, 최소 단위로 분리. (Đơn giản: Mỗi hàm chỉ làm 1 việc duy nhất.) |
| **의존성 배제 (Independence)** | 다른 모듈에 미치는 영향을 최소화. (Độc lập: Đổi chỗ này không làm sập chỗ khác.) |
| **중복성 최소화 (Minimizing Duplication)** | 코드의 중복을 최소화, 공통된 코드 사용. (DRY - Don't Repeat Yourself: Không copy-paste code.) |
| **추상화 (Abstraction)** | 상위 수준에선 간략하게, 상세 내용은 하위에서 구현. (Trừu tượng hóa: Cái chung ở trên, cái chi tiết ở dưới.) |

- **Vietnamese Explanation:** Clean Code là "đạo đức" của lập trình viên. Đừng viết Alien Code (code không ai hiểu nổi trừ người viết ban đầu). 
- 💡 **Mẹo ghi nhớ (Mnemonics):** 5 nguyên tắc: Đọc - Đơn - Độc - Lặp - Trừu. (Đọc Đơn Độc Lặp Trừu (Đọc hiểu - Đơn giản - Độc lập - Không lặp - Trừu tượng)).

---

# Chapter 5. 인터페이스 구현 (Interface Implementation)

## 핵심 046: 인터페이스 설계 확인 (EAI 구축 유형 - EAI Integration Types)

- **EAI (Enterprise Application Integration):** Doanh nghiệp có nhiều phần mềm (Kế toán, Nhân sự, Kho...), EAI giúp chúng nói chuyện được với nhau.

| 유형 (Kiểu) | 기능 (Chức năng) |
|---|---|
| **Point-to-Point** | 1:1로 연결 (Nối trực tiếp 1-1). Không có Middleware ở giữa. Khó thay đổi. |
| **Hub & Spoke** | 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형. (Nối kiểu nan hoa xe đạp. Tập trung vào cái Hub ở giữa. Hub sập là chết hết.) |
| **Message Bus** | 미들웨어(버스)를 두어 처리하는 방식. 확장성이 뛰어나며 대용량 처리가 가능. (Dùng một trục xe bus (Middleware) ở giữa. Rất dễ mở rộng và xử lý lượng lớn.) |
| **Hybrid** | 그룹 내에서는 Hub & Spoke, 그룹 간에는 Message Bus. (Lai tạp: Trong nhóm thì dùng Hub, giữa các nhóm thì dùng Bus.) |

- 💡 **Mẹo ghi nhớ (Mnemonics):** Hub & Spoke = Nan hoa (Có tâm Hub, sập tâm là chết). Message Bus = Xe buýt (Chở được nhiều, dễ mở rộng).

---

## 핵심 047: 인터페이스 보안, 기능 구현 및 검증 (Interface Security, Implementation, Verification)

### 네트워크 보안 기술 (Kỹ thuật bảo mật mạng)
- **IPSec (IP Security):** 네트워크 계층 (Network Layer). Chống giả mạo, ẩn giấu gói tin IP.
- **SSL (Secure Socket Layer):** TCP/IP ~ 애플리케이션 계층 사이. Chứng thực, mã hóa (thường dùng cho HTTPS).
- **S-HTTP:** 애플리케이션 계층 (Application Layer). Mã hóa mọi tin nhắn giữa Client và Server.

### 인터페이스 데이터 포맷 (Định dạng dữ liệu giao tiếp)
- **AJAX:** Bất đồng bộ (Asynchronous), dùng JS và XML để cập nhật một phần trang web mà không cần tải lại toàn bộ trang.
- **JSON:** Cặp "Key-Value", định dạng nhẹ, dễ đọc (Thay thế cho XML rất nhiều).
- **XML:** Thẻ Markup đa mục đích (như HTML nhưng tự tạo thẻ được).
- **YAML:** "YAML Ain't Markup Language". Định dạng dữ liệu tuần tự hóa, rất dễ đọc cho con người (hay dùng làm file config).

### 인터페이스 구현 검증 도구 (Công cụ kiểm chứng Test Interface)
- **xUnit:** Test từng "Đơn vị" (Unit) - jUnit, cppUnit.
- **STAF:** Test trong "Môi trường phân tán" (Distributed environment).
- **FitNesse:** Framework test nền web (Điền bảng là tự chạy test).
- **NTAF:** Kết hợp FitNesse + STAF (Do Naver làm).

- **Vietnamese Explanation:** Khi gửi dữ liệu giữa các máy, JSON đang là vua vì nhẹ và dễ nhìn. YAML thì thường dùng để cấu hình server. Khi test xem các máy tính nói chuyện với nhau ổn không, người ta dùng xUnit (Test từng hàm) hoặc STAF (Test qua nhiều máy).
- 💡 **Mẹo ghi nhớ (Mnemonics):** IPSec = Tầng Mạng (IP). SSL = Tầng giữa (Socket). JSON = Key-Value. STAF = Phân tán (Phân tán (Distributed)).

---

# [복습 / 심화 노트 - Revision & Deep Dive Notes]

## 073 & 074: 자료 구조의 정의 및 선형 리스트 (Data Structures & Linear List)

### 자료 구조의 분류 (Phân loại)
- **선형 구조 (Linear - Tuyến tính):** 배열 (Array), 리스트 (List), 스택 (Stack), 큐 (Queue), 데크 (Deque).
- **비선형 구조 (Non-Linear - Phi tuyến):** 트리 (Tree), 그래프 (Graph).

### 배열 (Array - Mảng)
- 동일한 자료형 (Cùng kiểu dữ liệu). 첨자(Index)를 이용 (Dùng Index để truy cập cực nhanh).
- 데이터 삭제 시 빈 공간으로 남아있어 메모리 낭비. (Xóa xong để lại lỗ hổng, lãng phí bộ nhớ).

### 연속 리스트 vs 연결 리스트 (Contiguous vs Linked List)
- **연속 리스트 (배열 / Array):** Mật độ = 1 (Kín bưng). Tìm nhanh, nhưng Thêm/Xóa chậm vì phải xô đẩy các phần tử khác.
- **연결 리스트 (포인터 / Linked List):** Mật độ < 1 (Tốn chỗ cho Con trỏ Pointer). Tìm chậm, nhưng Thêm/Xóa cực nhanh (Chỉ việc trỏ lại hướng).

- **Ví dụ (Example):** Array là ngồi ghế đá, muốn người mới ngồi giữa phải bảo mọi người xích ra. Linked List là nắm tay vòng tròn, muốn ai vào giữa chỉ việc buông tay và nắm tay người đó.

---

## 075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)

### 스택 (Stack)
- **LIFO (Last-In-First-Out / 후입선출):** Vào sau ra trước.
- **Con trỏ:** `Top` (Điểm vào/ra), `Bottom` (Đáy).
- **Lỗi:** Overflow (Đầy mà cố nhét), Underflow (Rỗng mà cố lấy).
- **Ứng dụng:** 재귀 호출 (Đệ quy), 후위 표기법 (Postfix).

### 큐 (Queue)
- **FIFO (First-In-First-Out / 선입선출):** Vào trước ra trước.
- **Con trỏ:** `Rear` (Chỗ đưa vào), `Front` (Chỗ lấy ra).
- **Ứng dụng:** 작업 스케줄링 (Lập lịch OS - Xếp hàng chờ xử lý).

### 데크 (Deque - Double Ended Queue)
- 양쪽 끝에서 모두 입출력 가능. (Vào/Ra ở cả 2 đầu).
- **Scroll (스크롤):** 입력 제한 (Hạn chế Đầu vào - Vào 1 bên, Ra 2 bên).
- **Shelf (셸프):** 출력 제한 (Hạn chế Đầu ra - Vào 2 bên, Ra 1 bên).

- 💡 **Mẹo ghi nhớ (Mnemonics):** 
  - Stack = LIFO = Đệ quy. 
  - Queue = FIFO = Lập lịch. 
  - Scroll (Cuộn) = Chỉ cuộn vào 1 hướng (Hạn chế Input). 
  - Shelf (Cái giá đỡ) = Đẩy đồ vào từ 2 bên nhưng chỉ lấy ra được 1 mặt (Hạn chế Output).

---

## 077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)

### 최대 간선 수 (Số Cạnh Tối Đa)
- **무방향 그래프 (Vô hướng):** `n(n-1)/2`.
- **방향 그래프 (Có hướng):** `n(n-1)`. (Gấp đôi vô hướng).
*(n là số đỉnh / Vertex)*

### 인접 행렬 (Adjacency Matrix - Ma trận kề)
- Biểu diễn đồ thị bằng ma trận `N x N`. (Có đường đi = 1, Không có = 0).
- **방향 그래프:** Không đối xứng. Hàng (Row) là đi Ra (Out), Cột (Column) là đi Vào (In).
- **무방향 그래프:** Đối xứng qua đường chéo (Symmetric).

- **Vietnamese Explanation:** Nếu đồ thị ít cạnh (thưa) thì dùng Ma trận kề sẽ rất tốn RAM vì toàn số 0. Số cạnh của Đồ thị vô hướng luôn bằng một nửa Đồ thị có hướng vì cạnh A-B và B-A được tính là 1.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Vô hướng / 2 (Vì không phân biệt đi/về). Ma trận vô hướng = Đối xứng.

---

## 078 & 079: 트리 및 운행법 (Tree & Tree Traversal)

### 트리 (Tree - Cây)
- **사이클(Cycle)이 없는 그래프.** (Đồ thị không có vòng lặp / chu trình).
- **단말 노드 (Leaf Node):** Nút lá (Không có con / Degree = 0).
- **차수 (Degree):** Số nút con của một nút.
- **트리의 차수 (Tree's Degree):** Degree lớn nhất trong toàn bộ cây.
- **깊이 (Depth):** Số tầng (Level) tối đa của cây.

### 트리의 운행법 (Tree Traversal - Duyệt cây)
- Theo vị trí của **Root (Gốc)**:
  - **Preorder (전위):** **Root** -> Left -> Right.
  - **Inorder (중위):** Left -> **Root** -> Right.
  - **Postorder (후위):** Left -> Right -> **Root**.

- **Ví dụ (Example):** Cây có Gốc A, Trái B, Phải C. Pre = ABC, In = BAC, Post = BCA.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Pre (Trước) = Root đi đầu. In (Giữa) = Root ở giữa. Post (Sau) = Root đi chót.

---

## 080: 수식의 표기법 (Expression Notation)

Chuyển đổi biểu thức toán học tương ứng với duyệt cây.
- **Infix (Trung tố):** `A + B` (Giống Inorder).
- **Prefix (Tiền tố):** `+ A B` (Giống Preorder).
- **Postfix (Hậu tố):** `A B +` (Giống Postorder - Máy tính rất thích kiểu này vì dùng Stack tính cực dễ).

### Cách chuyển đổi Infix sang Postfix
1. Đóng ngoặc toàn bộ theo thứ tự ưu tiên: `A / B * (C + D)` -> `((A / B) * (C + D))`
2. Kéo Dấu toán tử ra phía **SAU** dấu ngoặc của nó: `((A B /) (C D +) *)`
3. Xóa ngoặc: `A B / C D + *`

- **Vietnamese Explanation:** Máy tính không hiểu `A+B*C` vì nó không biết cái nào ưu tiên trước. Nó dùng Postfix `A B C * +` ném vào Stack để tính một lèo không cần ngoặc.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Postfix = Dấu nằm ở cuối cụm. Prefix = Dấu nằm ở đầu cụm.

---

## 081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)

- **이미 순서화된 파일(앞부분)**에 새로운 레코드를 **순서에 맞게 삽입**시켜 정렬. (Lấy phần tử hiện tại chèn vào đúng vị trí trong phần mảng đã sắp xếp phía trước nó).
- **Thời gian (Time Complexity):** O(n²) cho cả Trung bình và Tệ nhất.
- **Số vòng lặp (Pass):** Mảng có n phần tử thì chạy (n-1) vòng. Bắt đầu xét từ phần tử thứ 2.

- **Ví dụ (Example):** Xếp bài tá lả. Bạn rút một lá bài mới lên, xem trên tay bài đã xếp sẵn, thấy chỗ nào vừa thì "chèn" nó vào đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 삽입 (Chèn) = Từ khóa "Đã được sắp xếp sẵn" (Đã sắp xếp sẵn). Luôn O(n²).

## 081-2: 셸 정렬 (Shell Sort)

- **삽입 정렬(Insertion Sort)을 보완/확장**한 알고리즘. (Phiên bản nâng cấp của Insertion Sort).
- 입력 파일을 매개변수 **h(간격)** 만큼 떨어진 레코드들끼리 묶어 서브파일을 구성하고, 각 서브파일을 삽입 정렬. (Chia mảng thành các nhóm con cách nhau một khoảng $h$, sắp xếp chèn từng nhóm. Sau đó giảm $h$ dần dần về 1).
- **시간 복잡도:** 평균 O(n^1.5), 최악 O(n²). 부분적으로 정렬되어 있는 경우에 매우 유리. (Nhanh hơn O(n²) thông thường. Rất hiệu quả nếu mảng đã "hơi hơi" có thứ tự).

- **Vietnamese Explanation:** Insertion Sort thường yếu khi số nhỏ nằm tuốt ở cuối mảng (phải nhích từng bước lên đầu). Shell Sort dùng khoảng cách $h$ (ví dụ nhảy 5 bước 1 lần) để đưa số nhỏ về đầu nhanh hơn. 
- 💡 **Mẹo ghi nhớ (Mnemonics):** Shell = Vỏ ốc (Xoáy từ rộng vào hẹp). Từ khóa: **h (Khoảng cách nhảy)**, **O(n^1.5)**.

---

## 082: 선택 정렬 (Selection Sort)

- **최소값(Minimum)**을 찾아 첫 번째 위치에 놓고, 남은 것 중 또 최소값을 찾아 두 번째 위치에 놓는 방식. (Tìm phần tử nhỏ nhất đổi chỗ lên đầu, tiếp tục tìm số nhỏ nhì đổi chỗ lên thứ hai...).
- **시간 복잡도:** O(n²) (Luôn luôn).
- **Từ khóa:** "최소값을 찾아..." (Tìm giá trị nhỏ nhất...).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Selection = Đi "chọn" thằng nhỏ nhất mang lên đầu.

---

## 083: 버블 정렬 (Bubble Sort)

- **인접한 두 개의 레코드** 키 값을 비교하여 크기에 따라 위치 교환(Swap). (So sánh 2 phần tử cạnh nhau, số to đẩy lùi về sau. Số to nhất sẽ "nổi bọt" chìm xuống cuối mảng sau vòng đầu tiên).
- **종료 조건:** 더 이상 교환이 일어나지 않으면 정렬 끝. 플래그 비트(Flag Bit) 사용. (Dùng cờ Flag, nếu chạy hết 1 vòng mà không có ai đổi chỗ nghĩa là đã sắp xếp xong).
- **시간 복잡도:** O(n²).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Bubble (Nổi bọt) = Từ khóa **Hai phần tử kề nhau** (Hai cái kề nhau), **플래그 비트** (Flag bit).

---

## 084: 퀵 정렬 (Quick Sort)

- **분할과 정복 (Divide and Conquer):** 파일 나누어 정렬.
- **피벗 (Pivot):** 기준값. Nhỏ hơn Pivot sang trái, lớn hơn Pivot sang phải.
- **스택 (Stack) 필요:** 재귀 (Recursion) 호출을 위해. (Dùng đệ quy nên cần Stack nhớ vị trí).
- **가장 빠른 방식:** Trung bình nhanh nhất.
- **시간 복잡도:** 평균 **O(n log n)**, 최악 **O(n²)** (Khi mảng đã sắp xếp sẵn mà chọn Pivot ngu).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Quick = Pivot, Đệ quy, Stack. Tốt: n log n. Xấu: n².

---

## 085: 힙 정렬 (Heap Sort)

- **전이진 트리 (Complete Binary Tree)**를 힙 트리로 변환하여 정렬. (Xếp mảng thành Cây nhị phân hoàn chỉnh, tạo Heap max/min, lấy dần gốc ra ngoài).
- **시간 복잡도:** Mọi trường hợp (Tốt, trung bình, xấu) đều là **O(n log n)**. Rất ổn định, ít tốn RAM.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Heap = Cây (Cây (Tree)). Ổn định ở mức O(n log n).

---

## 086: 2-Way 합병 정렬 (Merge Sort)

- 이미 정렬된 두 개의 파일을 하나의 파일로 **합치며 (Merge)** 정렬. (Cưa đôi mảng liên tục đến khi còn 1 phần tử, rồi gộp từ từ lại thành 2, 4, 8...).
- **시간 복잡도:** Mọi trường hợp đều **O(n log n)**. 안정 정렬 (Stable Sort).

---

## 086-1: 기수 정렬 (Radix Sort / Bucket Sort)

- 데이터를 비교하지 않음! **큐(Queue)**를 이용하여 데이터의 **자릿수(Digit)**별로 나누어 담았다가 꺼냄. (Không dùng dấu < hay > để so sánh. Nhìn vào chữ số hàng Đơn vị, phân vào 10 cái Queue (0-9). Xong ráp lại, làm tiếp hàng Chục, Trăm...).
- **시간 복잡도:** **O(d*n)** (Trong đó d là số chữ số dài nhất). Cực kỳ nhanh, vượt qua giới hạn n log n của các thuật toán so sánh thông thường.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Radix (Cơ số) = Chữ số (Hàng đơn vị, chục...) (Chữ số), Queue/Bucket. Siêu tốc O(dn).

---

## 087: 이분 검색 (Binary Search - Tìm kiếm nhị phân)

- **전제조건 (Bắt buộc):** 파일이 **반드시 순서화(정렬, Ordered)** 되어 있어야 함. (Mảng bắt buộc phải được sắp xếp từ trước).
- **원리:** 찾고자 하는 값을 중간 레코드(Middle, `M = (F+L)/2`)와 비교하여 탐색 범위를 절반씩 줄임.
- **시간 복잡도:** **O(log n)**. (Gấp ngàn lần tìm tuần tự. 1000 phần tử chỉ cần tìm 10 lần).

---

## 088: 해싱 (Hashing) & 088-1: 데이터저장소 (Data Storage)

### 해싱 함수 (Hash Function)
- Chuyển `Key` thành `Home Address` trong Hash Table. 
- Từ khóa: Bucket (Xô), Slot (Khe), Collision (Đụng độ - 2 Key ra chung 1 Address), Overflow (Tràn - Bucket hết chỗ trống).
- **제산법 (Division):** Phổ biến nhất. Lấy Key chia cho số nguyên tố $Q$ lấy phần dư (Modulus).

### 데이터저장소 (Data Storage)
- **논리 (Logical):** 연관성, 구조 (Cấu trúc, liên kết, bản thiết kế trên giấy).
- **물리 (Physical):** 하드웨어, 저장장치 (Phần cứng thực tế ổ cứng HDD/SSD).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Logic = Bản vẽ. Physical = Tòa nhà thực tế.

---

## 088-2: 데이터베이스 (Database) & 089: DBMS

### 데이터베이스의 4가지 특징 (ISOS - 4 Đặc trưng của DB)
- **통합된 데이터 (Integrated Data):** 중복 배제 (Không trùng lặp).
- **저장된 데이터 (Stored Data):** 저장 매체에 저장 (Lưu trên máy tính).
- **운영 데이터 (Operational Data):** 반드시 필요한 고유 업무 자료 (Dữ liệu bắt buộc phải có để tổ chức hoạt động, không phải rác).
- **공용 데이터 (Shared Data):** 공동으로 소유 (Nhiều người/app dùng chung).

### DBMS (Database Management System)
- 소프트웨어 (Là phần mềm quản lý DB, ví dụ: MySQL, Oracle).
- **3대 기능 (3 Chức năng chính):** 
  - **정의 (Definition / DDL):** Tạo cấu trúc, bảng (Table).
  - **조작 (Manipulation / DML):** Thêm, sửa, xóa, tìm kiếm (CRUD).
  - **제어 (Control / DCL):** Bảo mật, phân quyền, tính toàn vẹn.

- 💡 **Mẹo ghi nhớ (Mnemonics):** ISOS (Integrated, Stored, Operational, Shared) - Nhớ chữ O = Operational (Vận hành/Thiết yếu). DBMS có 3 chữ D-M-C (Định nghĩa, Thao tác, Điều khiển).

---

## 090-1: 데이터의 독립성 (Data Independence)

- **논리적 독립성 (Logical):** Đổi cấu trúc logic (Thêm/xóa cột) nhưng App đang chạy không bị sập.
- **물리적 독립성 (Physical):** Đổi ổ cứng (Sang SSD, đổi server) nhưng App vẫn chạy bình thường.

---

## 091: 스키마 (Schema)

스키마 là bộ khung (Cấu trúc, ràng buộc) của Database. Có 3 góc nhìn:
- **외부 스키마 (External Schema):** User view. (User nhìn thấy gì, vd: Màn hình nhân viên chỉ thấy Lương của mình).
- **개념 스키마 (Conceptual Schema):** DB Admin view. (Toàn bộ logic, cấu trúc của doanh nghiệp. Thường gọi tắt là "Schema").
- **내부 스키마 (Internal Schema):** System view. (Cấu trúc vật lý, lưu trên đĩa như thế nào).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Ngoại (User/App) - Khái niệm (Toàn cục/Admin) - Nội (Máy móc/Ổ cứng).

---

## 091-1: 절차형 SQL (Procedural SQL)

C, JAVA처럼 분기/반복 (If/For)이 가능한 SQL (SQL có thêm logic lập trình - PL/SQL). Bọc trong khối `BEGIN ~ END`.

| 종류 (Loại) | 특징 (Đặc điểm) | ví dụ (Ví dụ sử dụng) |
|---|---|---|
| **프로시저 (Procedure)** | Gọi thủ công (`CALL`). Thực thi một chuỗi nghiệp vụ (Insert/Update nhiều bảng). KHÔNG có `RETURN`. | Chuyển tiền (Trừ A, Cộng B). |
| **트리거 (Trigger)** | Tự động chạy khi có sự kiện (Insert/Update/Delete). KHÔNG thể gọi thủ công. | Tự động ghi log khi có người xóa dữ liệu, tự trừ số lượng kho khi có đơn hàng. |
| **사용자 정의 함수 (User Defined Function)** | Dùng trong câu `SELECT`. BẮT BUỘC có `RETURN` 1 giá trị. | Hàm tính thuế VAT 10% từ giá gốc. |

- **Vietnamese Explanation:** SQL bình thường rất phèn, chỉ biết lấy dữ liệu ra. Procedural SQL thông minh hơn. Procedure như một cuốn kịch bản bạn bắt nó diễn. Trigger như cái bẫy chuột, có chuột (sự kiện) là tự sập. Function giống hệt hàm trong Toán học, đưa X trả về Y.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Procedure = Gọi mới chạy. Trigger = Tự động (Event). Function = Trả về giá trị (Return).

### 절차형 SQL의 테스트와 디버깅 (Testing & Debugging Procedural SQL)
- 절차형 SQL은 DBMS 내부에서 직접 실행되므로, 애플리케이션과 DB 사이의 데이터 전송량을 줄일 수 있어 효율적임. (Chạy trực tiếp trong DBMS nên giảm nghẽn mạng).
- **Quy trình Test & Debug:** `CREATE` (Biên dịch) -> Sửa lỗi cú pháp -> Comment các lệnh `INSERT/UPDATE/DELETE` (Tránh làm hỏng DB thật) -> Dùng `DBMS_OUTPUT` in giá trị ra màn hình để kiểm tra -> `EXEC / CALL` -> Xác nhận kết quả.

---

## 092-1: 쿼리 성능 최적화 (Query Performance Optimization)

- 데이터 입·출력 애플리케이션의 성능 향상을 위해 **SQL 코드를 최적화**하는 작업. (Tối ưu hóa mã SQL để tăng tốc độ truy xuất).
- **최적화 절차 (Trình tự tối ưu hóa):**
  1. **대상 선정:** **APM (Application Performance Monitoring)** 등 성능 측정 도구를 사용하여 느린 쿼리를 찾아냄. (Dùng APM tìm câu SQL chạy chậm).
  2. **계획 검토:** **옵티마이저 (Optimizer)**가 수립한 **실행 계획 (Execution Plan)**을 분석. (Xem bản đồ đường đi do bộ Tối ưu hóa lập ra xem có bị đi lòng vòng không).
  3. **재구성 (튜닝):** SQL 코드를 수정하거나 **인덱스 (Index)**를 재구성. (Sửa lại code hoặc tạo Index để tăng tốc).

- 💡 **Mẹo ghi nhớ (Mnemonics):** APM (Tìm bệnh) -> Optimizer/Execution Plan (Khám bệnh / Xem phim X-quang) -> Tuning (Chữa bệnh / Tạo Index).

---

## 093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)

### 단위 모듈 (Unit Module)
- 프로그램의 단위 기능을 구현하는 독립적인 최소 소프트웨어 단위. (Đơn vị phần mềm nhỏ nhất, độc lập, thực hiện 1 chức năng duy nhất).

### 단위 기능 명세서 작성 원칙 (Nguyên tắc viết Đặc tả chức năng)
- **추상화 (Abstraction):** 복잡한 시스템을 단순하게 구현. (Trừu tượng hóa - ẩn đi sự phức tạp).
- **구조화 (Structuring):** 대형 시스템을 분해하여 단위 기능별로 구분, 계층적으로 구성. (Cấu trúc hóa - chia nhỏ thành sơ đồ hình cây).
- **정보 은닉 (Information Hiding):** 한 모듈 내의 정보가 다른 모듈에 영향을 주지 않도록 숨김. (Che giấu thông tin - dùng biến private để tránh đụng độ).

### 입·출력 기능 및 알고리즘 구현 (I/O & Algorithm Implementation)
- **입·출력 구현:** Nhận Input, trả Output. Chú ý liên kết giao diện (CLI/GUI) hoặc dùng Open Source API để kết nối mạng.
- **알고리즘 구현:** Viết code xử lý logic bên trong (Process) sau khi đã có I/O.

---

## 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

### IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)
- 모듈 간 또는 복수의 프로세스 간 통신을 위한 인터페이스. (Cách các chương trình đang chạy nói chuyện với nhau).
- **Các phương pháp IPC:**
  - **Shared Memory (Bộ nhớ chia sẻ):** Nhanh nhất. Các process dùng chung 1 vùng RAM.
  - **Socket (Ổ cắm):** Giao tiếp qua mạng.
  - **Semaphores (Cờ hiệu):** Đồng bộ hóa, khóa (Locking) tài nguyên dùng chung.
  - **Pipes (Ống dẫn):** Dùng RAM theo kiểu FIFO, tại 1 thời điểm chỉ 1 process được dùng.
  - **Message Queueing (Hàng đợi tin nhắn):** Truyền tin bất đồng bộ.

### 알고리즘 구현 모듈 (Các loại Module khi lập trình)
- **디바이스 드라이버 모듈 (Device Driver):** Điều khiển phần cứng ngoại vi (vd: Máy in).
- **네트워크 모듈 (Network):** Truyền thông dữ liệu mạng.
- **파일 모듈 (File):** Truy xuất cấu trúc file trên đĩa cứng.
- **메모리 모듈 (Memory):** Quản lý RAM, cấp phát bộ nhớ ảo, hoặc làm IPC.
- **프로세스 모듈 (Process):** Tạo và quản lý các tiến trình khác.

- 💡 **Mẹo ghi nhớ (Mnemonics):** IPC là gửi thư cho nhau. Shared Memory = Bảng tin chung (Nhanh nhất). Semaphore = Cái khóa cửa nhà vệ sinh (Ai đang dùng thì khóa lại).

---

## 095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)

### 단위 모듈 테스트 (Unit Module Test)
- 코딩 직후 최소 단위인 모듈이나 컴포넌트에 초점을 맞춤. (Test ngay sau khi code xong 1 hàm/module).
- Chủ yếu dùng **화이트박스 (White-box test)** để tìm lỗi thuật toán, vòng lặp vô hạn, lỗi công thức toán học.

### 테스트 케이스 (Test Case)
- 입력 값, 실행 조건, 기대 결과의 명세서. (Tài liệu ghi rõ: Nhập gì, Điều kiện gì, Kết quả mong đợi là gì).
- 테스트 케이스를 미리 작성(사전에 정의)해야 인력과 시간 낭비를 방지. (Phải viết Test Case **trước** khi code hoặc test, để tránh test lung tung tốn thời gian).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Test Case = Input + Condition + Expected Output. Bắt buộc viết trước khi test.

---

## 097 & 120: 통합 개발 환경 (IDE - Integrated Development Environment)

- 코딩, 디버그, 컴파일, 배포 등 모든 작업을 하나의 프로그램에서 처리. (Phần mềm tất-cả-trong-một).
- **4대 기능 (4 Chức năng chính):** 
  - 코딩 (Coding): Gõ code.
  - 컴파일 (Compile): Dịch ra mã máy.
  - 디버깅 (Debugging): Tìm và sửa lỗi (Bug).
  - 배포 (Deployment): Đóng gói và giao cho người dùng.
- **대표 도구 (Các IDE tiêu biểu):**
  - **이클립스 (Eclipse):** Của IBM, Đa nền tảng (Cross-platform), chuyên Java.
  - **IntelliJ (IDEA):** Của JetBrains, Đa nền tảng, chuyên Java/Kotlin.
  - **비주얼 스튜디오 (Visual Studio):** Của Microsoft, chuyên Windows, C#/.NET.
  - **엑스 코드 (Xcode):** Của Apple, chuyên MacOS/iOS.
  - **안드로이드 스튜디오 (Android Studio):** Của Google, chuyên Android.

---

## 097-2: 테스트 프로세스 (Test Process - Quy trình kiểm thử)

**Quy trình 5 bước (5 단계):**
1. **계획 및 제어 (Planning & Control):** Lập kế hoạch, mục tiêu, chi phí.
2. **분석 및 설계 (Analysis & Design):** Viết Kịch bản (Test Scenario) và Ca kiểm thử (**Test Case**).
3. **구현 및 실현 (Implementation & Execution):** Viết Thủ tục test (**Test Procedure** - Trình tự chạy các case) và Thực thi test.
4. **평가 (Evaluation):** Đánh giá kết quả xem đạt chưa.
5. **완료 (Completion):** Lưu trữ hồ sơ, bàn giao.

- **Vietnamese Explanation:** Test Case là danh sách các món ăn cần nấu (Ví dụ: Trứng rán). Test Procedure là công thức nấu (Bước 1 bật bếp, bước 2 đập trứng). Phải có món (Case) rồi mới ghi công thức (Procedure) được.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Kế hoạch -> Phân tích (Ra Test Case) -> Thực hiện (Ra Test Procedure) -> Đánh giá -> Hoàn thành. (Kế Phân Thực Đánh Hoàn (Kế hoạch - Phân tích - Thực hiện - Đánh giá - Hoàn thành)).

---

## 098 & 기타 협업 도구 (Build Tools & Collaboration Tools)

### 빌드 도구 (Build Tool)
- 소스 코드를 실행할 수 있는 제품으로 변환(빌드)하는 과정을 자동화. (Công cụ tự động biên dịch và gom file code lại thành file chạy `.exe`, `.apk`...).
- **Ant:** Cổ điển, dùng cho Java, của Apache.
- **Maven:** Nâng cấp của Ant, quản lý thư viện (Dependencies) tự động.
- **Gradle:** Hiện đại nhất, lai giữa Ant và Maven, dùng nhiều cho Android.

### 기타 협업 도구 (Groupware / Collaboration Tools)
- **프로젝트 및 일정 관리 (Quản lý dự án):** Jira (지라), Trello, Google Calendar.
- **메신저 (Giao tiếp):** Slack, Jandi.
- **디자인 (Thiết kế UI -> Code):** Zeplin, Sketch.
- **기타:** Evernote (Ghi chú), Swagger (Tài liệu API tự động), GitHub (Lưu source code).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jira = Quản lý công việc (Ticket). Slack = Chat. Zeplin = Thiết kế. Swagger = Viết Document cho API. Gradle = Build Android.

---

## 099: 소프트웨어 패키징 (Software Packaging)

- 실행 파일들을 묶어 배포용 설치 파일을 만드는 과정. (Gom tất cả file thực thi, file hình, file cấu hình thành 1 file cài đặt (Setup.exe) để tung ra thị trường).
- **Nguyên tắc:** 
  - **사용자 중심 (Hướng tới người dùng):** Người dùng cài đặt dễ dàng, không cần biết code.
  - Cần phải 모듈화 (Module hóa) để dễ bảo trì, và tích hợp 보안 (Bảo mật / DRM).

## 100 & 100-1: 패키징 시 고려사항 및 순서 (Packaging Considerations & Sequence)

### 패키징 시 고려사항
- 최소 환경 정의 (OS/CPU/RAM). (Phải ghi rõ cấu hình tối thiểu để chạy app).
- UI와 매뉴얼 일치. (Hình ảnh UI trong thực tế và trong tài liệu phải giống nhau).
- 보안 및 암호화, DRM 연동 고려. (Bảo mật, mã hóa, tích hợp chống copy).

### 소프트웨어 패키징 순서 (Trình tự đóng gói)
1. **기능 식별 (Xác định chức năng)**
2. **모듈화 (Module hóa)**
3. **빌드 진행 (Build - Dịch ra file chạy)**
4. **사용자 환경 분석 (Phân tích môi trường người dùng - OS/CPU)**
5. **패키징 및 적용 시험 (Đóng gói & Test thử)**
6. **패키징 변경 개선 (Sửa lỗi nếu có)**
7. **배포 (Deployment - Phát hành)**

- 💡 **Mẹo ghi nhớ (Mnemonics):** Nhận-Mô-Build-Môi-Gói-Cải-Phân (Nhận diện - Module - Build - Môi trường - Đóng gói - Cải tiến - Phân phối).

---

## 100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)

### 저작권 (Copyright)
- 창작자가 가지는 **배타적 독점적 권리**. (Quyền độc quyền của tác giả). Phần mềm rất dễ bị copy (`Ctrl+C / Ctrl+V`) nên phải có DRM để bảo vệ.

### DRM의 핵심 구성 요소 (Thành phần chính của DRM)
- **패키저 (Packager):** 콘텐츠 암호화. (Người/Máy đóng gói và khóa file lại).
  - *실시간 패키징:* File nhỏ (Nhạc, ảnh) -> Khách bấm mua mới đóng gói.
  - *사전 패키징:* File to (Phim) -> Đóng gói sẵn trước khi bán.
- **클리어링 하우스 (Clearing House):** 권한, 라이선스, 결제 관리. (Trạm thu phí: Xác thực bạn đã trả tiền chưa, cấp License cho bạn mở file. Quản lý cả tính tiền theo dung lượng/thời gian - 종량제).
- **콘텐츠 분배자 (Distributor):** Nơi bán/phân phối (App Store).
- **DRM 컨트롤러 (Controller):** Phần mềm trên máy khách hàng kiểm soát việc mở file.
- **보안 컨테이너 (Security Container):** Hộp an toàn chứa file gốc để vận chuyển.

### DRM 기술 요소 (Kỹ thuật dùng trong DRM)
- **암호화 (Encryption):** Mã hóa file.
- **키 관리 (Key Management):** Quản lý khóa để mở mã hóa.
- **식별 기술 (Identification):** Gắn mã định danh (DOI, URI) để biết file nào là file nào.
- **저작권 표현 (Right Expression):** Ghi rõ quyền lợi (Vd: XrML - Chỉ cho xem, cấm in).
- **크랙 방지 (Tamper Resistance):** Chống bẻ khóa, chống hack.
- **인증 (Authentication):** Xác minh danh tính người mua.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Packager (Gói hàng + Khóa), Clearing House (Thu tiền + Đưa chìa).

---

## 104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)

### 설치 매뉴얼 (Installation Manual - Hướng dẫn cài đặt)
- **사용자 기준 (Góc nhìn người dùng):** Viết cho khách hàng, không phải cho Dev.
- **순서대로 (Theo trình tự):** Từ lúc bấm Next đến lúc Finish.
- **예외 상황 / 오류 메시지:** Phải có cách xử lý khi cài đặt bị lỗi.
- **Uninstall (Xóa cài đặt):** Bắt buộc phải hướng dẫn cách gỡ cài đặt sạch sẽ.
- **서문 (Lời nói đầu) bao gồm:** 
  - 문서 이력 (Lịch sử chỉnh sửa v1.0, v1.1).
  - 주석 (Chú ý/Tham khảo).
  - 설치 환경 체크 (Kiểm tra OS, tắt app khác trước khi cài).

### 사용자 매뉴얼 (User Manual - Hướng dẫn sử dụng)
- **컴포넌트 단위 (Theo từng Component):** Chia nhỏ theo từng tính năng (Ví dụ: Hướng dẫn riêng cho Word, Excel).
- **버전 관리 (Quản lý phiên bản):** App update tính năng thì Manual cũng phải update theo.
- **시각 자료 (Hình ảnh):** Bắt buộc phải có hình chụp màn hình UI để dễ hiểu.

---

## 105: 시각에 따른 테스트 (Verification vs Validation)

- **검증 (Verification - Xác minh):** 개발자 시각 (Góc nhìn Dev). "Làm đúng thiết kế/mã code không?". (Are we building the product right?).
- **확인 (Validation - Thẩm định):** 사용자 시각 (Góc nhìn User). "Phần mềm này có đúng cái khách hàng cần không?". (Are we building the right product?).

- 💡 **Mẹo ghi nhớ (Mnemonics):** 검증 (Verification) = Code chuẩn chưa? (Dev). 확인 (Validation) = Khách ưng không? (User).

---

## 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

- **형상 관리 (SCM):** 소프트웨어 변경 사항을 체계적으로 관리. (Quản lý mọi thay đổi của phần mềm: Source code, tài liệu, thiết kế... trong suốt vòng đời).
- **목적:** 가시성 (Tính hiển thị - ai đang làm gì), 추적성 (Tính truy xuất - ai gây ra lỗi này), 무절제한 변경 방지 (Ngăn chặn việc sửa code vô tội vạ).

### 형상 관리 5대 기능 (5 Chức năng của SCM)
1. **형상 식별 (Identification):** Đặt tên, đánh số phiên bản, phân nhánh (Tree) để dễ quản lý.
2. **버전 제어 (Version Control):** Lưu lại các version cũ/mới.
3. **형상 통제 (Configuration Control):** Yêu cầu đổi code phải được xem xét kỹ trước khi nhập vào bản chính (Baseline).
4. **형상 감사 (Audit):** Kiểm tra lại xem code đã chuẩn chưa.
5. **형상 기록 (Status Reporting):** Ghi chép lịch sử báo cáo.

### 버전 관리 용어 (Thuật ngữ Version Control)
- **저장소 (Repository):** Kho lưu trữ code.
- **체크아웃 (Check-out):** Lấy code từ Kho về máy mình để sửa.
- **체크인 (Check-in) / 커밋 (Commit):** Lưu code mình vừa sửa vào máy mình (Local) hoặc đưa lên Kho.
- **동기화 (Update):** Lấy code mới nhất của người khác trên Kho về máy mình để đồng bộ.

---

## 113 ~ 115: 버전 관리 도구 방식 (Version Control Tool Types)

| 방식 (Cách thức) | 특징 (Đặc điểm) | 대표 도구 (Công cụ) |
|---|---|---|
| **공유 폴더 (Shared Folder)** | Copy đè file vào 1 folder dùng chung trên mạng Lan. Dễ mất dữ liệu. | SCCS, RCS, PVCS |
| **클라이언트/서버 (Client/Server)** | Có 1 máy Server trung tâm giữ code. Máy cá nhân (Client) lấy về sửa rồi đẩy lên. Server chết là nghỉ làm. | **CVS, SVN** (Subversion), ClearCase |
| **분산 저장소 (Distributed Repo)** | Mỗi máy cá nhân đều là 1 cái Kho thu nhỏ (Local Repo). Copy (Clone) từ Server (Remote Repo) về. Server chết vẫn làm việc bình thường ở máy cá nhân, lúc nào Server sống lại đẩy lên sau (Push). Rất an toàn. | **Git**, Mercurial, Bitkeeper |

- **Vietnamese Explanation:** SVN là kiểu "Đi mượn sách thư viện", mất thư viện là khỏi đọc. Git là kiểu "Photo cuốn sách về nhà", thư viện cháy mình vẫn còn sách đọc, sửa sách thoải mái.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 
  - 공유 폴더 (Share folder) = RCS, PVCS. 
  - 클라이언트/서버 = CVS, SVN (Server tập trung). 
  - 분산 (Phân tán) = Git.

## 116 & 117: 형상 관리 도구 (SVN vs Git)

### Subversion (SVN)
- 클라이언트/서버 구조 (Cấu trúc Client/Server tập trung).
- **Trunk:** Thư mục chính (Main).
- **Branches:** Th nhánh để làm tính năng riêng.
- **Revision:** Mỗi lần Commit thành công, số Revision tăng lên 1.

### Git (깃)
- 분산 저장소 방식 (Lưu trữ phân tán). Phát minh bởi Linus Torvalds.
- **Snapshot (스냅샷):** Lưu lại toàn bộ trạng thái file tại một thời điểm rất nhanh chóng.
- **로컬 저장소 (Local Repo) vs 원격 저장소 (Remote Repo):** Internet đứt vẫn làm việc bình thường ở Local.

- 💡 **Mẹo ghi nhớ (Mnemonics):** SVN = Trunk (Thân cây), Revision tăng dần. Git = Snapshot, Phân tán (Phân tán (Distributed)).

---

## 118 ~ 120: 빌드 자동화 도구 (Build Automation Tools)

- 소스 코드를 실행 파일로 만드는 과정과 배포를 자동화. (Tự động hóa việc dịch code, test và đóng gói phát hành - CI/CD).
- **Jenkins:** Viết bằng Java, chạy trên web (Web GUI). Điểm mạnh là test phân tán trên nhiều máy.
- **Gradle:** Viết bằng Groovy (Ngôn ngữ kịch bản), dùng **DSL**. Điểm mạnh là có **빌드 캐시 (Build Cache)** giúp build lại cực nhanh, thường dùng làm chuẩn cho Android.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Jenkins = Java, Web GUI, Phân tán. Gradle = Groovy, DSL, Cache, Android.

---

## 120-1: 소프트웨어의 분류 (Software Classification)

- **상용 소프트웨어 (Commercial):** Bán lấy tiền (Product). VD: Windows, Office, Game.
- **서비스 제공 소프트웨어 (Service Provision / SI):** Làm theo đơn đặt hàng của 1 tổ chức (Dự án nội bộ). VD: Hệ thống ngân hàng.

---

## 120-2 ~ 126: 애플리케이션 테스트 이론 (Application Test Theory)

### 테스트의 기본 원리 (Nguyên lý cơ bản)
- **완벽한 테스트 불가능:** Không thể khẳng định 100% hết bug.
- **파레토 법칙 (Pareto):** 80% bug nằm ở 20% code cốt lõi. (Đám mây lỗi).
- **살충제 패러독스 (Pesticide Paradox):** Test hoài 1 kịch bản sẽ bị "nhờn", phải liên tục thay đổi bộ test.
- **정황 의존 (Context):** Tùy thuộc ngữ cảnh (Web, Game) mà test khác nhau.

### 테스트 분류 (Phân loại Test)
1. **실행 여부 (Theo việc có chạy code không):**
   - **정적 테스트 (Static):** Không chạy code. Đọc, review tài liệu (Walkthrough, Inspection).
   - **동적 테스트 (Dynamic):** Chạy code. (White box, Black box).
2. **테스트 기반 (Theo căn cứ Test):**
   - **명세 기반 (Specification):** Dựa vào tài liệu yêu cầu.
   - **구조 기반 (Structure):** Dựa vào luồng logic của code.
   - **경험 기반 (Experience):** Dựa vào kinh nghiệm tester (Đoán lỗi).
3. **목적 (Theo mục đích):**
   - **강도 (Stress):** Ép tải (Dồn dập bắt nó sập).
   - **회귀 (Regression):** Sửa code xong test lại xem có hỏng chỗ cũ không.
   - **회복 (Recovery):** Giả vờ ngắt điện xem app phục hồi data được không.
   - **병행 (Parallel):** Chạy app cũ và app mới cùng lúc để so kết quả.

- 💡 **Mẹo ghi nhớ (Mnemonics):** Inspection (Khám nghiệm) = Tĩnh (Static). Regression (Hồi quy) = Sửa xong test lại.

---

## 127 ~ 129: 화이트박스 테스트 (White Box Test)

- 내부 로직과 제어 구조를 직접 관찰. (Test dựa trên mã nguồn (Source Code). Nhìn thấu bên trong).
- **종류 (Các kỹ thuật):** 기초 경로 (Đường dẫn cơ bản), 조건 (Điều kiện), 루프 (Vòng lặp), 데이터 흐름 (Luồng dữ liệu).
- **검증 기준 (Coverage - Mức độ bao phủ):**
  - **문장 검증 (Statement):** Mọi dòng code phải chạy qua 1 lần.
  - **분기/결정 검증 (Branch/Decision):** Mọi nhánh lệnh (If True / False) phải chạy qua 1 lần.
  - **조건 검증 (Condition):** Mọi biểu thức điều kiện con bên trong If phải kiểm tra T/F.

- 💡 **Mẹo ghi nhớ (Mnemonics):** White Box = Code (Câu lệnh, Rẽ nhánh, Vòng lặp). Do Dev tự làm.

---

## 130 & 131: 블랙박스 테스트 (Black Box Test)

- 명세를 기초로 기능 테스트. 내부 구조 무시. (Dựa vào chức năng UI, không thèm nhìn code).
- **종류 (Các kỹ thuật):**
  - **동치 분할 (Equivalence Partitioning):** Chia vùng tương đương (Nhập đại 1 số đại diện).
  - **경계값 분석 (Boundary Value):** Test quanh cái mép (Max, Min, +1, -1). Lỗi hay nằm ở đây.
  - **원인-효과 그래프 (Cause-Effect):** Vẽ biểu đồ nhân quả.
  - **오류 예측 (Error Guessing):** Dựa vào kinh nghiệm (Kinh nghiệm Tester).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Black Box = UI, Chức năng. Các kỹ thuật thường chia theo vùng (Partition) và ranh giới (Boundary).

---

## 132 ~ 136: 개발 단계에 따른 애플리케이션 테스트 (V-Model Test Levels)

Thực hiện theo mô hình V (V-Model), từ nhỏ đến lớn:

1. **단위 테스트 (Unit Test):** Test từng Module con. Thường dùng White Box.
2. **통합 테스트 (Integration Test):** Ghép các module lại. (Có thể test kiểu Big Bang - Gom 1 cục, hoặc dần dần từ trên xuống, từ dưới lên). Tìm lỗi giao tiếp (Interface).
3. **시스템 테스트 (System Test):** Test toàn bộ hệ thống trong môi trường giống thực tế nhất. Đánh giá tính năng + hiệu năng (Bảo mật, tốc độ).
4. **인수 테스트 (Acceptance Test):** Khách hàng test để nghiệm thu.
   - **알파 (Alpha):** Khách hàng test tại văn phòng dev (có dev đứng xem).
   - **베타 (Beta):** Khách hàng tự test ở nhà (Giống Game Open Beta).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Đơn vị (Unit) -> Tích hợp (Integration) -> Hệ thống (System) -> Nghiệm thu (Acceptance). Alpha = Nội bộ, Beta = Ở nhà.
