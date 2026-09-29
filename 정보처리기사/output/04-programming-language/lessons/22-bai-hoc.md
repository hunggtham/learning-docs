# 075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **258 - 261. 배열과 문자열 (Arrays & Strings)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

배열, 조건문, 반복문

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **배열과 포인터 심화 (Arrays & Pointers - Advanced)**에서 만든 기준을 이어받아 **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)

Ở bước 22/77, **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** xuất hiện như phần tiếp nối của **배열과 포인터 심화 (Arrays & Pointers - Advanced)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **배열 (Array)**, **조건문 (if/switch)**, **반복문 (for/while)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **배열 (Array)**: `자료형 변수명[개수] = {초깃값};` (C/Java). 2차원 배열은 `변수명[행][열]`.
- **조건문 (if/switch)**:
  - C/Java: `if (조건) { ... } else if (조건) { ... } else { ... }`
  - Python: `if 조건:` -> `elif 조건:` -> `else:`
  - switch문 (C/Java): 식의 값에 따라 `case`를 찾아가며, `break;`가 없으면 아래 문장들도 계속 실행됨.
- **반복문 (for/while)**:
  - for문 (C/Java): `for (초기식; 조건식; 증감식) { ... }`
  - for문 (Python): `for 변수 in range(시작, 끝+1):`
  - while문: 조건이 참일 동안 반복.
  - do~while문 (C/Java): 조건과 상관없이 무조건 **최소 1번**은 실행하고 조건을 검사함.

**Giải thích (Vietnamese):**
- Trong Python, cấu trúc điều kiện là `if`, `elif` (viết tắt của else if) và `else`. Không cần ngoặc nhọn `{}` mà dùng thụt lề (indentation).
- `do~while` khác `while` ở chỗ: `do~while` sẽ làm việc trước rồi mới kiểm tra điều kiện sau, nên chắc chắn code bên trong được chạy ít nhất 1 lần.

---

Như vậy, **075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **258 - 261. 배열과 문자열 (Arrays & Strings)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.