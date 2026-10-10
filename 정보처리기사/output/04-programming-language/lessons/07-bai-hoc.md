# 237. 변수명 작성 규칙 (Variable Naming Rules)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **237. 변수명 작성 규칙 (Variable Naming Rules)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy nối phạm vi tên hợp lệ, quy ước đặt tên và khả năng đọc mã để thấy một tên biến tốt hỗ trợ kiểm soát lỗi thế nào.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **237. 변수명 작성 규칙 (Variable Naming Rules)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **237. 변수명 작성 규칙 (Variable Naming Rules)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **연산자 (Operators)** khi chuyển sang phần tiếp theo.

> **Mối nối:** Mục tiêu đã xác định tên biến phải vừa hợp lệ vừa dễ đọc; các **핵심 키워드 (Từ khóa)** tiếp theo chỉ ra những thành phần tạo nên một tên. Hãy đọc chúng như tiêu chí kiểm tra mã, không như danh sách thuật ngữ tách rời.

## 핵심 키워드 (Từ khóa)

변수명, 작성, 규칙

> **Mối nối:** Từ khóa cho biết ta cần kiểm tra ký tự, vị trí bắt đầu và từ dành riêng; phần **선행·연결 개념 (Kiến thức liên kết)** giải thích các quy tắc đó trong ngữ cảnh shell và mã chương trình. **읽는 방법 (Cách đọc)** tiếp theo sẽ giúp áp dụng chúng vào tên cụ thể.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**에서 만든 기준을 이어받아 **237. 변수명 작성 규칙 (Variable Naming Rules)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Mối nối:** Khi đã biết bối cảnh của các quy tắc, hãy dùng **읽는 방법 (Cách đọc)** để kiểm tra từng tên theo chuỗi: ký tự → điều kiện hợp lệ → khả năng đọc và bảo trì. Phần **237. 변수명 작성 규칙 (Variable Naming Rules)** bên dưới cung cấp ví dụ để đối chiếu chuỗi này.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Mối nối:** Các bước đọc vừa nêu tạo khung cho phần ví dụ và quy tắc chính. Hãy dùng chúng để phân biệt tên hợp lệ với tên chỉ “trông có vẻ rõ”, rồi giữ lại tiêu chí đó khi chuyển sang bài về toán tử.

## 237. 변수명 작성 규칙 (Variable Naming Rules)

Ở bước 7/91, **237. 변수명 작성 규칙 (Variable Naming Rules)** xuất hiện như phần tiếp nối của **087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **237. 변수명 작성 규칙 (Variable Naming Rules)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “237. 변수명 작성 규칙 (Variable Naming Rules)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 영문자, 숫자, 밑줄(`_`)의 조합만 가능.
- **첫 글자는 숫자로 시작할 수 없음** (예: `1a` 안됨).
- 공백이나 특수문자(`+`, `-`, `*`, `/`, `@` 등) 사용 금지.
- 예약어(`if`, `for`, `while` 등) 사용 금지.
- 대소문자 엄격히 구분.

**Giải thích (Vietnamese):**
Quy tắc đặt tên biến: Không được bắt đầu bằng số, không có khoảng trắng, không chứa ký tự đặc biệt (trừ dấu gạch dưới `_`), không dùng từ khoá của ngôn ngữ.

---

Như vậy, **237. 변수명 작성 규칙 (Variable Naming Rules)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **연산자 (Operators)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **237. 변수명 작성 규칙 (Variable Naming Rules)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
