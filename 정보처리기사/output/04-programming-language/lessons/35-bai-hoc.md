# 082. 운영체제 기능 및 종류 (Operating System OS)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **082. 운영체제 기능 및 종류 (Operating System OS)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **082. 운영체제 기능 및 종류 (Operating System OS)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

운영체제, 기능, 종류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **운영체제 (Operating Systems)**에서 만든 기준을 이어받아 **082. 운영체제 기능 및 종류 (Operating System OS)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 082. 운영체제 기능 및 종류 (Operating System OS)

Sau khi đã đặt nền bằng **운영체제 (Operating Systems)**, ta chuyển sang **082. 운영체제 기능 및 종류 (Operating System OS)**. Đây là mắt xích 35/77 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **082. 운영체제 기능 및 종류 (Operating System OS)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **운영체제의 주요 프로그램**, **제어 프로그램 (Control Program)**, **처리 프로그램 (Processing Program)**, **쉘(Shell)과 커널(Kernel)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **운영체제의 주요 프로그램**:
  - **제어 프로그램 (Control Program)**: 감시(Kernel), 작업 제어, 데이터 관리.
  - **처리 프로그램 (Processing Program)**: 언어 번역(컴파일러), 서비스, 문제 프로그램.
- **쉘(Shell)과 커널(Kernel)**:
  - **쉘 (Shell)**: 사용자의 명령어를 해석하여 커널로 전달 (사용자 인터페이스).
  - **커널 (Kernel)**: 핵심 모듈. 하드웨어/메모리/프로세스를 직접 제어 및 관리.
- **운영체제 종류**:
  - **Windows**: GUI, 선점형 멀티태스킹, PnP(자동 감지) 기능.
  - **Linux / Unix**: 오픈소스 (Linux), 트리 구조 파일 시스템. 시분할 시스템.
  - **Unix 파일 시스템 구조**: 부트 블록 -> 슈퍼 블록 (전체 정보) -> 아이노드(i-node) 블록 (파일 메타데이터) -> 데이터 블록 (실제 파일 내용).

**Giải thích (Vietnamese):**
OS giống như quản gia của máy tính.
- Kernel (Hạt nhân) là bộ não xử lý phần cứng. Shell (Vỏ) là cái dòng lệnh hoặc giao diện để con người nói chuyện với bộ não đó.
- Hệ thống tệp của UNIX chia làm 4 phần: Boot (chứa code khởi động) -> Super (Thông tin tổng quan) -> i-node (Lưu tên file, quyền truy cập...) -> Data (Nội dung file thực tế).

**💡 Mẹo ghi nhớ (Mnemonics):**
**제어 프로그램**: 감작데 (감시, 작업, 데이터). / **처리 프로그램**: 언서문 (언어, 서비스, 문제).

---

Ta có thể khép mục **082. 운영체제 기능 및 종류 (Operating System OS)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.