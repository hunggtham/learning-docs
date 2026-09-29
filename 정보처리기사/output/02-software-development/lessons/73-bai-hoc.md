# 19. 클린 코드 작성 원칙 (Clean Code Principles)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **19. 클린 코드 작성 원칙 (Clean Code Principles)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **19. 클린 코드 작성 원칙 (Clean Code Principles)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **21. 외계인 코드 (Alien Code)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

클린, 코드, 작성, 원칙

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**에서 만든 기준을 이어받아 **19. 클린 코드 작성 원칙 (Clean Code Principles)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 19. 클린 코드 작성 원칙 (Clean Code Principles)

Ở bước 73/95, **19. 클린 코드 작성 원칙 (Clean Code Principles)** xuất hiện như phần tiếp nối của **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **19. 클린 코드 작성 원칙 (Clean Code Principles)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **가독성 (Readability)**, **단순성 (Simplicity)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **가독성 (Readability)**: 누구든지 코드를 쉽게 읽을 수 있도록 작성.
* **단순성 (Simplicity)**: 코드를 간단하게 작성.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc viết code sạch. Dễ đọc, đơn giản.
* **Example**: 변수 이름을 `a` 대신 `userCount`로 짓는 것이 가독성을 높이는 것입니다.

Như vậy, **19. 클린 코드 작성 원칙 (Clean Code Principles)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **21. 외계인 코드 (Alien Code)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.