# 4. 병행 제어 (Concurrency Control)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **4. 병행 제어 (Concurrency Control)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **4. 병행 제어 (Concurrency Control)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 보안 및 암호화 (Security & Encryption)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

병행, 제어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 트랜잭션의 상태 (Transaction States)**에서 만든 기준을 이어받아 **4. 병행 제어 (Concurrency Control)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **4. 병행 제어 (Concurrency Control)** và nối nó với **5. 보안 및 암호화 (Security & Encryption)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 4. 병행 제어 (Concurrency Control)

Sau khi đã đặt nền bằng **3. 트랜잭션의 상태 (Transaction States)**, ta chuyển sang **4. 병행 제어 (Concurrency Control)**. Đây là mắt xích 47/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **4. 병행 제어 (Concurrency Control)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념 (Concept)**, **문제점 (Problems)**, **갱신 분실 (Lost Update)**, **비완료 의존성 (Uncommitted Dependency)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “4. 병행 제어 (Concurrency Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Concept)**: Điều khiển sự tương tác giữa các giao dịch chạy đồng thời để bảo vệ tính 일관성 (nhất quán).
- **문제점 (Problems)**:
  - **갱신 분실 (Lost Update)**: Mất bản cập nhật.
  - **비완료 의존성 (Uncommitted Dependency)**: Phụ thuộc vào giao dịch chưa commit (Dirty Read).
  - **모순성 (Inconsistency)**: Mâu thuẫn dữ liệu.
  - **연쇄 복귀 (Cascading Rollback)**: Phải rollback dây chuyền.
- **로킹 (Locking)**: Khóa dữ liệu để sử dụng 상호 배타적 (độc quyền - Mutual Exclusion).
  - **로킹 단위 (Locking Granularity)**: Đơn vị khóa.
    - Đơn vị 크면 (lớn) -> ít khóa, dễ quản lý, nhưng mức đồng thời thấp (낮은 병행성).
    - Đơn vị 작으면 (nhỏ) -> ngược lại.
- **Ví dụ**: Hai người cùng rút tiền từ một tài khoản, Locking giúp chỉ 1 người được rút tại 1 thời điểm.
- 💡 **Mẹo ghi nhớ**: Vấn đề đồng thời: L/U/I/C (Lost, Uncommitted, Inconsistency, Cascading) -> **Làm Út In Cười**

Ta có thể khép mục **4. 병행 제어 (Concurrency Control)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 보안 및 암호화 (Security & Encryption)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.