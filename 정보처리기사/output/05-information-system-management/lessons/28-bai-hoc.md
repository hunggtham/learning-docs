# 정보 보안 및 하드웨어 신기술 (Security & HW Tech)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **소프트웨어 보안 (Software Security)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

정보, 보안, 하드웨어, 신기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**에서 만든 기준을 이어받아 **정보 보안 및 하드웨어 신기술 (Security & HW Tech)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** và nối nó với **소프트웨어 보안 (Software Security)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 정보 보안 및 하드웨어 신기술 (Security & HW Tech)

Ở bước 28/86, **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** xuất hiện như phần tiếp nối của **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **BaaS (Blockchain as a Service)**, **OWASP**, **허니팟 (Honeypot)**, **Secure OS** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **1. 보안 용어 및 Secure OS** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **1. 보안 용어 및 Secure OS** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 1. 보안 용어 및 Secure OS

Bây giờ ta đi vào nội dung của **1. 보안 용어 및 Secure OS**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “1. 보안 용어 및 Secure OS” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **BaaS (Blockchain as a Service)**: 클라우드 기반 블록체인 개발 환경 제공.
- **OWASP**: 웹 취약점을 연구하는 비영리 단체 (10대 취약점 발표).
- **허니팟 (Honeypot)**: 침입자를 속여 정보를 수집하기 위해 설치해 둔 시스템 (미끼).
- **Secure OS**: 기존 OS에 보안 기능 커널을 이식한 운영체제. 암호적, 논리적, 시간적, 물리적 분리 방법을 통해 보호하며 식별, 인증, 접근통제(MAC, DAC) 기능을 제공합니다.

Các bullet của **1. 보안 용어 및 Secure OS** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 보안 용어 및 Secure OS** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 하드웨어 신기술** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **2. 하드웨어 신기술**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 2. 하드웨어 신기술

Phần nguồn của **2. 하드웨어 신기술** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “2. 하드웨어 신기술” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **HA (High Availability, 고가용성)**: 장애 발생 시 즉시 다른 시스템으로 대체 가능한 이중화 환경.
- **RAID**: 여러 개의 하드디스크에 데이터를 분산 저장하여 속도와 안정성을 향상시키는 기술.
- **트러스트존 (TrustZone)**: 프로세서 내에 일반 구역과 보안 구역을 분할하는 ARM의 하드웨어 보안 기술.

Các bullet của **2. 하드웨어 신기술** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **2. 하드웨어 신기술** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **정보 보안 및 하드웨어 신기술 (Security & HW Tech)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **소프트웨어 보안 (Software Security)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.