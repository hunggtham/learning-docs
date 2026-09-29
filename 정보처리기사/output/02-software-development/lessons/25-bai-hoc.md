# 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **116 & 117: 형상 관리 도구 (SVN vs Git)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

형상, 관리

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**에서 만든 기준을 이어받아 **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 109 ~ 112: 형상 관리 (SCM - Software Configuration Management)

Ở bước 25/95, **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** xuất hiện như phần tiếp nối của **핵심 032 & 033: 형상 관리 및 IDE (Configuration Management & IDE)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **형상 관리 (SCM):** 소프트웨어 변경 사항을 체계적으로 관리. (Quản lý mọi thay đổi của phần mềm: Source code, tài liệu, thiết kế... trong suốt vòng đời).
- **목적:** 가시성 (Tính hiển thị - ai đang làm gì), 추적성 (Tính truy xuất - ai gây ra lỗi này), 무절제한 변경 방지 (Ngăn chặn việc sửa code vô tội vạ).

Trước hết, ta đặt **형상 관리 5대 기능 (5 Chức năng của SCM)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **형상 관리 5대 기능 (5 Chức năng của SCM)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 형상 관리 5대 기능 (5 Chức năng của SCM)

Bây giờ ta đi vào nội dung của **형상 관리 5대 기능 (5 Chức năng của SCM)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

1. **형상 식별 (Identification):** Đặt tên, đánh số phiên bản, phân nhánh (Tree) để dễ quản lý.
2. **버전 제어 (Version Control):** Lưu lại các version cũ/mới.
3. **형상 통제 (Configuration Control):** Yêu cầu đổi code phải được xem xét kỹ trước khi nhập vào bản chính (Baseline).
4. **형상 감사 (Audit):** Kiểm tra lại xem code đã chuẩn chưa.
5. **형상 기록 (Status Reporting):** Ghi chép lịch sử báo cáo.

Phần **형상 관리 5대 기능 (5 Chức năng của SCM)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **형상 관리 5대 기능 (5 Chức năng của SCM)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **버전 관리 용어 (Thuật ngữ Version Control)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **버전 관리 용어 (Thuật ngữ Version Control)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 버전 관리 용어 (Thuật ngữ Version Control)

Phần nguồn của **버전 관리 용어 (Thuật ngữ Version Control)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **저장소 (Repository):** Kho lưu trữ code.
- **체크아웃 (Check-out):** Lấy code từ Kho về máy mình để sửa.
- **체크인 (Check-in) / 커밋 (Commit):** Lưu code mình vừa sửa vào máy mình (Local) hoặc đưa lên Kho.
- **동기화 (Update):** Lấy code mới nhất của người khác trên Kho về máy mình để đồng bộ.

---

Các bullet của **버전 관리 용어 (Thuật ngữ Version Control)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **버전 관리 용어 (Thuật ngữ Version Control)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **109 ~ 112: 형상 관리 (SCM - Software Configuration Management)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **116 & 117: 형상 관리 도구 (SVN vs Git)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.