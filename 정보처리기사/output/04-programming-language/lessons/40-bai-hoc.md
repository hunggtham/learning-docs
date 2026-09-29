# 프로세스 관리 (Process Management)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **프로세스 관리 (Process Management)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **프로세스 관리 (Process Management)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **085. 프로세스 및 스레드 (Process & Thread)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

프로세스, 관리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**에서 만든 기준을 이어받아 **프로세스 관리 (Process Management)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **프로세스 관리 (Process Management)** và nối nó với **085. 프로세스 및 스레드 (Process & Thread)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 프로세스 관리 (Process Management)

Ở bước 40/78, **프로세스 관리 (Process Management)** xuất hiện như phần tiếp nối của **289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **프로세스 관리 (Process Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **Dispatch (디스패치)**, **Wake Up (깨움)**, **Spooling (스풀링)**, **스레드의 분류 (Thread Types)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **297. 프로세스 (Process / Tiến trình)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **297. 프로세스 (Process / Tiến trình)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 297. 프로세스 (Process / Tiến trình)

Bây giờ ta đi vào nội dung của **297. 프로세스 (Process / Tiến trình)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 실행 중인 프로그램, PCB를 가진 프로그램. (Chương trình đang chạy, có chứa khối PCB).

Các bullet của **297. 프로세스 (Process / Tiến trình)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **297. 프로세스 (Process / Tiến trình)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **298. PCB (Process Control Block / Khối điều khiển tiến trình)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **298. PCB (Process Control Block / Khối điều khiển tiến trình)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 298. PCB (Process Control Block / Khối điều khiển tiến trình)

Phần nguồn của **298. PCB (Process Control Block / Khối điều khiển tiến trình)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 프로세스의 상태, 포인터, 식별자(PID), CPU 레지스터 정보 등 저장. (Lưu trạng thái, PID, bộ nhớ, thanh ghi CPU của tiến trình).

Các bullet của **298. PCB (Process Control Block / Khối điều khiển tiến trình)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **298. PCB (Process Control Block / Khối điều khiển tiến trình)**, đừng bắt đầu lại từ số không. **299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)

Các ý ngay dưới **299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **Dispatch (디스패치)**: 준비(Ready) -> 실행(Run). (Cấp phát CPU cho tiến trình).
- **Wake Up (깨움)**: 대기(Wait) -> 준비(Ready). (Hoàn tất I/O, sẵn sàng chạy lại).
- **Spooling (스풀링)**: 입출력 데이터를 디스크에 한꺼번에 저장. (Lưu đệm vào đĩa để xử lý I/O mượt mà).

Các bullet của **299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**299 & 300. 프로세스 상태 전이 및 용어 (Process States & Terms)** vừa cho ta cách đặt câu hỏi. Bây giờ **301. 스레드 (Thread / Luồng)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **301. 스레드 (Thread / Luồng)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 301. 스레드 (Thread / Luồng)

Bây giờ ta đi vào nội dung của **301. 스레드 (Thread / Luồng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 프로세스 내에서의 작업 단위. (Đơn vị thực thi nhỏ nhất bên trong một tiến trình).

Các bullet của **301. 스레드 (Thread / Luồng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **301. 스레드 (Thread / Luồng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)

Phần nguồn của **스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **스레드의 분류 (Thread Types)**:
  - **사용자 수준 (User-level)**: 라이브러리 사용, 빠르지만 구현 어려움. (Dùng thư viện, nhanh nhưng khó code).
  - **커널 수준 (Kernel-level)**: OS 커널이 관리, 구현 쉽지만 속도 느림. (OS quản lý, dễ code nhưng chậm).
- **스레드 장점**: 병행성 증진, 응답 시간 단축, 기억장소 낭비 감소. (Tăng đồng thời, phản hồi nhanh, tiết kiệm RAM).
- **FCFS (First Come First Service = FIFO)**: 도착한 순서대로 처리, 공평하지만 짧은 작업이 오래 대기할 수 있음. (Đến trước phục vụ trước, công bằng nhưng dễ gây kẹt xe).

Với **스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Sau khi đọc **스레드 및 스케줄링 심화 (Threads & Scheduling - Advanced)**, đừng bắt đầu lại từ số không. **303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)

Các ý ngay dưới **303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 명령어에서 사용 시 앞에 `$`를 붙인다. (Thêm `$` phía trước để gọi biến).
- **`$HOME`**: 홈 디렉터리 (Thư mục gốc).
- **`$PATH`**: 실행 파일 경로 (Đường dẫn tìm file thực thi).
- **`$PWD`**: 현재 작업 디렉터리 (Thư mục hiện tại).
- **`$LANG`**: 기본 언어 (Ngôn ngữ mặc định).

Các bullet của **303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**303. UNIX / LINUX 주요 환경 변수 (Environment Variables / Biến môi trường)** vừa cho ta cách đặt câu hỏi. Bây giờ **304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)

Bây giờ ta đi vào nội dung của **304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **`fsck`**: 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi File System).
- **`getpid`**: 자신의 프로세스 ID (Lấy PID của bản thân).
- **`getppid`**: 부모 프로세스 ID (Lấy PID của tiến trình cha).

Các bullet của **304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **304. UNIX / LINUX 기본 명령어 (Basic Commands - Bổ sung)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **프로세스 관리 (Process Management)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **085. 프로세스 및 스레드 (Process & Thread)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.