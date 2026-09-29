# 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

운영체제, 구성, UNIX, 시스템

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)**에서 만든 기준을 이어받아 **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)

Ở bước 37/77, **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)** xuất hiện như phần tiếp nối của **282. 운영체제의 정의 및 목적 (Definition & Purpose of OS)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **운영체제 구성**, **제어 프로그램**, **처리 프로그램**, **UNIX의 특징** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **운영체제 구성**:
  - **제어 프로그램**: 감시(Supervisor, 핵심), 작업 제어, 데이터 관리.
  - **처리 프로그램**: 언어 번역(컴파일러), 서비스(유틸리티).
- **UNIX의 특징**: 대화식 운영체제, **C언어로 작성**되어 이식성이 높음. 트리(Tree) 구조의 파일 시스템.
  - **커널(Kernel)**: UNIX의 핵심. 하드웨어/메모리/프로세스 관리.
  - **쉘(Shell)**: 사용자의 명령어를 해석하여 커널에 전달하는 인터페이스.
- **파일 디스크립터 (File Descriptor)**: 시스템이 파일을 관리하기 위해 이름, 위치, 크기 등의 속성을 담아두는 제어 블록 (사용자가 직접 볼 수 없음).
- **UNIX 환경 변수**: `$HOME`(홈 디렉터리), `$PATH`(명령어 검색 경로), `$PWD`(현재 작업 폴더).
- **UNIX 명령어**: `chmod`(권한 변경), `fork`(프로세스 복제).

**Giải thích (Vietnamese):**
- Kernel là não bộ, Shell là lớp vỏ giao tiếp với người dùng.
- Lệnh `fork` trong Unix dùng để nhân bản một Process đang chạy thành một Process con mới.

---

Như vậy, **283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.