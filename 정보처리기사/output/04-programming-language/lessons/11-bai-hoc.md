# 244. 조건(삼항) 연산자 (Ternary Operator)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **244. 조건(삼항) 연산자 (Ternary Operator)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Hãy nối điều kiện, nhánh đúng–sai và giá trị trả về để biết toán tử ba ngôi rút gọn quyết định mà không làm mất logic.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **244. 조건(삼항) 연산자 (Ternary Operator)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **244. 조건(삼항) 연산자 (Ternary Operator)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **245. 연산자 우선순위 (Operator Precedence)** khi chuyển sang phần tiếp theo.

> **Mối nối:** Mục tiêu của bài đặt câu hỏi về cách **244. 조건(삼항) 연산자 (Ternary Operator)** chọn một trong hai giá trị; các **핵심 키워드 (Từ khóa)** tiếp theo giúp theo dõi điều kiện, nhánh đúng–sai và kết quả trả về. Từ đó, **선행·연결 개념 (Kiến thức liên kết)** cho biết tiêu chí nào được kế thừa từ nhóm toán tử trước.

## 핵심 키워드 (Từ khóa)

조건

> **Mối nối:** Từ khóa **조건** nhắc ta theo dõi cả điều kiện lẫn hai nhánh giá trị; **선행·연결 개념 (Kiến thức liên kết)** đặt chúng trên nền của **239 - 243. 연산자 (Operators)**. Sau đó, **읽는 방법 (Cách đọc)** giúp kiểm tra thứ tự đánh giá và hệ quả của từng nhánh trước khi rút gọn thành biểu thức một dòng.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **239 - 243. 연산자 (Operators)**에서 만든 기준을 이어받아 **244. 조건(삼항) 연산자 (Ternary Operator)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Mối nối:** Tiêu chí từ **239 - 243. 연산자 (Operators)** tạo nền để **읽는 방법 (Cách đọc)** kiểm tra điều kiện, thứ tự chọn nhánh và giá trị trả về. Khi chuyển vào phần chính **244. 조건(삼항) 연산자 (Ternary Operator)**, hãy dùng chuỗi điều kiện → nhánh được chọn → kết quả để đọc công thức và ví dụ.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Mối nối:** Khung đọc vừa chuẩn bị dẫn vào phần **244. 조건(삼항) 연산자 (Ternary Operator)**. Hãy đối chiếu điều kiện với nhánh đúng–sai và giá trị nhận được, rồi mang hiểu biết về thứ tự đánh giá sang **245. 연산자 우선순위 (Operator Precedence)**.

## 244. 조건(삼항) 연산자 (Ternary Operator)

Sau khi đã đặt nền bằng **239 - 243. 연산자 (Operators)**, ta chuyển sang **244. 조건(삼항) 연산자 (Ternary Operator)**. Đây là mắt xích 11/91 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **244. 조건(삼항) 연산자 (Ternary Operator)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “244. 조건(삼항) 연산자 (Ternary Operator)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 조건의 참/거짓에 따라 서로 다른 값을 반환.
- 형식: `조건 ? 참일때_값 : 거짓일때_값;`
- (예: `int max = (a > b) ? a : b;`)

**Giải thích (Vietnamese):**
Toán tử 3 ngôi giúp viết tắt câu lệnh if-else trên 1 dòng. Trả về giá trị 1 nếu điều kiện đúng, giá trị 2 nếu sai.

---

Ta có thể khép mục **244. 조건(삼항) 연산자 (Ternary Operator)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **245. 연산자 우선순위 (Operator Precedence)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **244. 조건(삼항) 연산자 (Ternary Operator)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
