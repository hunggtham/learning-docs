# 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối IPC với module boundary, message và algorithm implementation, để phối hợp tiến trình có hợp đồng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định IPC và thuật toán theo loại module phối hợp qua dữ liệu, thông điệp và contract ra sao; từ khóa khoanh vùng boundary và trạng thái.

## 핵심 키워드 (Từ khóa)

IPC, 모듈별, 알고리즘, 구현

Kiến thức liên kết đặt IPC và module algorithm trên nền đặc tả interface; cách đọc tiếp theo giúp theo dõi luồng gọi và phản hồi.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**에서 만든 기준을 이어받아 **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần này dùng khung đó để nối loại module với cách truyền và xử lý dữ liệu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng boundary và lỗi khi gọi qua IPC; khi sang unit test, hãy chuyển các luồng đó thành case có thể quan sát.

## 094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)

Ở bước 34/101, **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** xuất hiện như phần tiếp nối của **093 & 093-1 & 093-2: 단위 모듈 및 명세서 (Unit Module & Specifications)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)

Bây giờ ta đi vào nội dung của **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 모듈 간 또는 복수의 프로세스 간 통신을 위한 인터페이스. (Cách các chương trình đang chạy nói chuyện với nhau).
- **Các phương pháp IPC:**
  - **Shared Memory (Bộ nhớ chia sẻ):** Nhanh nhất. Các process dùng chung 1 vùng RAM.
  - **Socket (Ổ cắm):** Giao tiếp qua mạng.
  - **Semaphores (Cờ hiệu):** Đồng bộ hóa, khóa (Locking) tài nguyên dùng chung.
  - **Pipes (Ống dẫn):** Dùng RAM theo kiểu FIFO, tại 1 thời điểm chỉ 1 process được dùng.
  - **Message Queueing (Hàng đợi tin nhắn):** Truyền tin bất đồng bộ.

Các bullet của **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **IPC (Inter-Process Communication - Giao tiếp giữa các tiến trình)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **알고리즘 구현 모듈 (Các loại Module khi lập trình)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **알고리즘 구현 모듈 (Các loại Module khi lập trình)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 알고리즘 구현 모듈 (Các loại Module khi lập trình)

Phần nguồn của **알고리즘 구현 모듈 (Các loại Module khi lập trình)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “알고리즘 구현 모듈 (Các loại Module khi lập trình)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **디바이스 드라이버 모듈 (Device Driver):** Điều khiển phần cứng ngoại vi (vd: Máy in).
- **네트워크 모듈 (Network):** Truyền thông dữ liệu mạng.
- **파일 모듈 (File):** Truy xuất cấu trúc file trên đĩa cứng.
- **메모리 모듈 (Memory):** Quản lý RAM, cấp phát bộ nhớ ảo, hoặc làm IPC.
- **프로세스 모듈 (Process):** Tạo và quản lý các tiến trình khác.

- 💡 **Mẹo ghi nhớ (Mnemonics):** IPC là gửi thư cho nhau. Shared Memory = Bảng tin chung (Nhanh nhất). Semaphore = Cái khóa cửa nhà vệ sinh (Ai đang dùng thì khóa lại).

---

Với **알고리즘 구현 모듈 (Các loại Module khi lập trình)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **알고리즘 구현 모듈 (Các loại Module khi lập trình)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **095 & 096: 단위 모듈 테스트 및 테스트 케이스 (Unit Test & Test Case)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **094 & 094-1: IPC 및 모듈별 알고리즘 구현 (IPC & Algorithm by Module Type)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
