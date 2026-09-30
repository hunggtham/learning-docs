# 핵심 262: 포인터와 포인터 변수 (Pointer)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 262: 포인터와 포인터 변수 (Pointer)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 262: 포인터와 포인터 변수 (Pointer)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **포인터와 배열 (Pointer and Array)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

핵심, 포인터와, 포인터, 변수

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **핵심 261: C언어의 문자열 배열**에서 만든 기준을 이어받아 **핵심 262: 포인터와 포인터 변수 (Pointer)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **핵심 262: 포인터와 포인터 변수 (Pointer)** và nối nó với **포인터와 배열 (Pointer and Array)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 핵심 262: 포인터와 포인터 변수 (Pointer)

Ở bước 43/86, **핵심 262: 포인터와 포인터 변수 (Pointer)** xuất hiện như phần tiếp nối của **핵심 261: C언어의 문자열 배열**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **핵심 262: 포인터와 포인터 변수 (Pointer)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **개념**, **기호**, **Example (KR/VN)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 262: 포인터와 포인터 변수 (Pointer)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념**: 변수의 **메모리 주소**를 저장하는 변수. 동적 메모리(Heap) 접근 시 활용. (Con trỏ: Biến lưu trữ địa chỉ bộ nhớ).
- **기호**:
  - `*`: 포인터 선언 시 사용 (예: `int *p;`). 또는 포인터가 가리키는 주소의 **값(Value)**을 참조할 때 사용 (`*p = 10;`). (Dùng để khai báo con trỏ, hoặc lấy giá trị tại địa chỉ đó).
  - `&`: 특정 변수의 **주소(Address)**를 가져올 때 사용. (Dùng để lấy địa chỉ của biến).
- **Example (KR/VN)**:
  - `int a = 50;` (변수 a 생성 및 50 저장 / Tạo biến a, gán 50).
  - `int *p = &a;` (포인터 p에 a의 주소 저장 / Con trỏ p lưu địa chỉ của a).
  - `*p = 70;` (p가 가리키는 곳(a)의 값을 70으로 변경 / Đổi giá trị tại địa chỉ p trỏ đến thành 70. Lúc này a = 70).
- 💡 **Mẹo ghi nhớ**: `&`(And)는 주소(Address), `*`(Star)는 값(Value)을 가리킨다고 기억하세요.

Như vậy, **핵심 262: 포인터와 포인터 변수 (Pointer)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **포인터와 배열 (Pointer and Array)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.