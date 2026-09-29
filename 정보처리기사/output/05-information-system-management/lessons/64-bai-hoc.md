# UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **IP 주소 및 서브네팅 (IP Address & Subnetting)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

UNIX, LINUX, 환경, 변수, 기본, 명령어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**에서 만든 기준을 이어받아 **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** và nối nó với **IP 주소 및 서브네팅 (IP Address & Subnetting)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)

Ở bước 64/86, **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** xuất hiện như phần tiếp nối của **주요 스케줄링 알고리즘 (Major Scheduling Algorithms)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 주요 환경 변수 (Environment Variables)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 주요 환경 변수 (Environment Variables)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 주요 환경 변수 (Environment Variables)

Bây giờ ta đi vào nội dung của **1. 주요 환경 변수 (Environment Variables)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

환경 변수를 사용할 때는 변수명 앞에 `$`를 붙입니다.
- `$HOME`: 사용자의 홈 디렉터리
- `$PWD`: 현재 작업하는 디렉터리
- `$PATH`: 실행 파일을 찾는 경로
- `$USER`: 사용자의 이름

Các bullet của **1. 주요 환경 변수 (Environment Variables)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 주요 환경 변수 (Environment Variables)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 기본 명령어 (Basic Commands)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 기본 명령어 (Basic Commands)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 기본 명령어 (Basic Commands)

Phần nguồn của **2. 기본 명령어 (Basic Commands)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 기본 명령어 (Basic Commands)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `cat`: 파일 내용 화면 표시
- `chmod`: 파일 보호 모드 설정 (사용 허가 지정)
- `chown`: 파일 소유자 변경
- `cp`: 파일 복사 / `rm`: 파일 삭제
- `find`: 파일 검색
- `fork`: 새로운 프로세스 생성 (프로세스 복제)
- `fsck`: 파일 시스템 검사 및 보수
- `ls`: 현재 디렉터리 내 파일 목록 확인

> **Vietnamese Explanation**:
> Biến môi trường trong UNIX/LINUX giúp hệ thống biết các cài đặt mặc định (như đường dẫn `$PATH`, thư mục chủ `$HOME`). Các lệnh cơ bản như `chmod` dùng để phân quyền file, `fork` để nhân bản tiến trình.

Các bullet của **2. 기본 명령어 (Basic Commands)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 기본 명령어 (Basic Commands)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **UNIX/LINUX 환경 변수 및 기본 명령어 (UNIX Variables & Commands)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **IP 주소 및 서브네팅 (IP Address & Subnetting)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.