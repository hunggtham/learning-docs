# 246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **제어문 (Control Statements)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

입출력, 함수와, 포맷

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **074. 데이터 입출력 (Data Input/Output)**에서 만든 기준을 이어받아 **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** và nối nó với **제어문 (Control Statements)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)

Ở bước 16/91, **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** xuất hiện như phần tiếp nối của **074. 데이터 입출력 (Data Input/Output)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **`scanf("서식문자열", &변수)`**, **`printf("서식문자열", 변수)`**, **서식 문자열**, **제어문자 (Escape Sequence)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **`scanf("서식문자열", &변수)`**: C언어 표준 입력. 변수명 앞에 주소 연산자 **`&`**를 반드시 붙여야 함.
- **`printf("서식문자열", 변수)`**: C언어 표준 출력. `&`를 붙이지 않음.
- **서식 문자열**:
  - `%d`: 10진수 정수 / `%f`: 실수 (예: `%8.2f`는 총 8자리, 소수점 2자리) / `%c`: 문자 1개 / `%s`: 문자열.
  - `%o`: 8진수 / `%x`: 16진수.
- **제어문자 (Escape Sequence)**:
  - `\n`: 줄바꿈 (New Line) / `\t`: 탭 (Tab) / `\b`: 백스페이스 / `\0`: 널 문자(문자열의 끝 표시).

**Giải thích (Vietnamese):**
Nhớ kĩ `scanf` phải có dấu `&` (địa chỉ) để nhét dữ liệu vào đúng chỗ trong RAM. `printf` thì không cần. Dấu `\0` (Null) cực kỳ quan trọng trong C để đánh dấu kết thúc một chuỗi (string).

---

Như vậy, **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **제어문 (Control Statements)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.