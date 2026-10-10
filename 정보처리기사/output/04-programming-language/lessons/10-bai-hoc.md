# 239 - 243. 연산자 (Operators)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **239 - 243. 연산자 (Operators)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối operators với precedence, type coercion và side effect, để biểu thức được hiểu theo ngữ nghĩa.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **239 - 243. 연산자 (Operators)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **239 - 243. 연산자 (Operators)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **244. 조건(삼항) 연산자 (Ternary Operator)** khi chuyển sang phần tiếp theo.

> **Mối nối:** Mục tiêu của bài đặt câu hỏi về vai trò và giới hạn của **239 - 243. 연산자 (Operators)**; các **핵심 키워드 (Từ khóa)** tiếp theo thu hẹp câu hỏi đó vào những nhóm toán tử cần so sánh. Khi đã nhận diện từ khóa, hãy quay về **선행·연결 개념 (Kiến thức liên kết)** để biết tiêu chí nào được kế thừa trước khi đọc phần quy tắc.

## 핵심 키워드 (Từ khóa)

연산자

> **Mối nối:** Từ khóa **연산자** giúp nhận diện các phép biến đổi; **선행·연결 개념 (Kiến thức liên kết)** bổ sung nền từ **연산자 심화 (Operators - Advanced)** để biết vì sao từng nhóm cần được đặt trong cùng một khung so sánh. Sau đó, **읽는 방법 (Cách đọc)** hướng dẫn kiểm tra toán hạng, điều kiện và kết quả thay vì học tên rời rạc.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **연산자 심화 (Operators - Advanced)**에서 만든 기준을 이어받아 **239 - 243. 연산자 (Operators)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Mối nối:** Tiêu chí kế thừa từ **연산자 심화 (Operators - Advanced)** tạo khung để **읽는 방법 (Cách đọc)** lần lượt kiểm tra toán tử số học, quan hệ, bit, logic và gán. Khi chuyển vào phần chính **239 - 243. 연산자 (Operators)**, hãy dùng cùng chuỗi đối tượng → điều kiện → hệ quả để đối chiếu các nhóm này.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Mối nối:** Khung đọc vừa chuẩn bị dẫn vào phần **239 - 243. 연산자 (Operators)**. Hãy đọc mỗi nhóm theo toán hạng, điều kiện áp dụng và giá trị tạo ra; sau đó giữ tiêu chí so sánh này khi chuyển sang **244. 조건(삼항) 연산자 (Ternary Operator)**.

## 239 - 243. 연산자 (Operators)

Ở bước 10/91, **239 - 243. 연산자 (Operators)** xuất hiện như phần tiếp nối của **연산자 심화 (Operators - Advanced)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **239 - 243. 연산자 (Operators)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận. Trong khối này, **산술 연산자**, **관계 연산자**, **비트 연산자**, **논리 연산자** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “239 - 243. 연산자 (Operators)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **산술 연산자**: 사칙연산, `%`(나머지), `++`/`--`(증감).
  - 전치(`++a`): 먼저 증가시키고 연산. 후치(`a++`): 연산 후 증가시킴.
- **관계 연산자**: `==`(같다), `!=`(다르다), `>`, `<`. C언어에서는 0 이외의 값을 참(True)으로 간주.
- **비트 연산자**: 비트 단위 연산. `&`(AND), `|`(OR), `^`(XOR: 서로 다를 때만 1), `~`(NOT). `<<`, `>>`(비트 이동).
- **논리 연산자**: `&&`(AND), `||`(OR), `!`(NOT).
- **대입 연산자**: `=`, `+=`, `-=` 등. `a += 1`은 `a = a + 1`과 동일.

---

Như vậy, **239 - 243. 연산자 (Operators)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **244. 조건(삼항) 연산자 (Ternary Operator)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **239 - 243. 연산자 (Operators)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
