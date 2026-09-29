# 101. 개념적 설계 (Conceptual Design)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **101. 개념적 설계 (Conceptual Design)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **101. 개념적 설계 (Conceptual Design)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **102. 논리적 설계 (Logical Design / Data Modeling)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

개념적, 설계

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **101. 개념적 설계 (Conceptual Design)**을(를) 독립된 암기 항목으로 두지 않고, 이 과목에서 다룰 문제의 출발점으로 삼는다. 먼저 무엇을 설명하는지와 어디까지 적용되는지를 확인한 뒤 세부 규칙으로 들어간다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 101. 개념적 설계 (Conceptual Design)

Chúng ta bắt đầu mạch học bằng **101. 개념적 설계 (Conceptual Design)**. Trước khi đi vào từng thuật ngữ, hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục 1/55 là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, không chỉ được ghi nhớ như danh sách.

Để đọc **101. 개념적 설계 (Conceptual Design)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- 정보의 구조를 얻기 위하여 현실 세계에 대한 인식을 추상적 개념으로 표현하는 과정이다.
- 개념 스키마 모델링과 트랜잭션 모델링을 병행 수행한다.
- **VI (Vietnamese) (Tiếng Việt):** Thiết kế khái niệm. Quá trình biểu diễn nhận thức về thế giới thực thành các khái niệm trừu tượng để có được cấu trúc thông tin. Thực hiện song song mô hình hóa lược đồ khái niệm và mô hình hóa giao dịch.
- **Example (Korean/Vietnamese):** 현실 세계의 '학생'과 '수업'을 E-R 다이어그램으로 그리는 것. / Vẽ sơ đồ E-R cho 'học sinh' và 'lớp học' trong thế giới thực.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Khái-Trừu (Khái niệm = Trừu tượng).

Như vậy, **101. 개념적 설계 (Conceptual Design)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **102. 논리적 설계 (Logical Design / Data Modeling)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.