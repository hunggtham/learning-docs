# 1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

포인터, 역참조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)**에서 만든 기준을 이어받아 **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** và nối nó với **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)

Ở bước 79/86, **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** xuất hiện như phần tiếp nối của **3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo yêu cầu liên trang)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **개념**, **Tiếng Việt**, **예시 (Example)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 널 포인터(값이 없는 메모리 주소)가 가리키는 메모리에 값을 저장하거나 읽을 때 발생하는 오류.
- **Tiếng Việt**: Lỗi xảy ra khi cố gắng đọc/ghi dữ liệu thông qua con trỏ đang có giá trị Null.
- **예시 (Example)**:
  - (KR) 객체가 생성되지 않았는데 그 객체의 메서드를 호출하여 시스템이 다운됨.
  - (VN) Gọi hàm của một đối tượng chưa được khởi tạo (bằng Null), làm app bị crash.

Như vậy, **1. 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược con trỏ Null)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **3. 취약한 API 사용 (Vulnerable API / API dễ bị tổn thương)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.