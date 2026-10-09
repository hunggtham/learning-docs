# 19. 클린 코드 작성 원칙 (Clean Code Principles)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **19. 클린 코드 작성 원칙 (Clean Code Principles)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối clean code với naming, function, coupling và changeability, để khả năng đọc trở thành một thuộc tính vận hành.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **19. 클린 코드 작성 원칙 (Clean Code Principles)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **19. 클린 코드 작성 원칙 (Clean Code Principles)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **21. 외계인 코드 (Alien Code)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định clean code giảm chi phí hiểu, sửa và kiểm thử qua tên, cấu trúc và trách nhiệm rõ; từ khóa khoanh vùng cohesion, coupling và smell.

## 핵심 키워드 (Từ khóa)

클린, 코드, 작성, 원칙

Kiến thức liên kết đặt clean code trên nền complexity và testability; cách đọc tiếp theo giúp nối nguyên tắc viết với chi phí thay đổi.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**에서 만든 기준을 이어받아 **19. 클린 코드 작성 원칙 (Clean Code Principles)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần clean code dùng khung đó để nối lựa chọn cấu trúc với khả năng kiểm chứng.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng ranh giới clean code phụ thuộc ngữ cảnh; khi sang alien code, hãy nhận diện smell trước khi sửa.

## 19. 클린 코드 작성 원칙 (Clean Code Principles)

Sau khi đã đặt nền bằng **18. 최악의 시간 복잡도 (Worst-case Time Complexity)**, ta chuyển sang **19. 클린 코드 작성 원칙 (Clean Code Principles)**. Đây là mắt xích 74/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **19. 클린 코드 작성 원칙 (Clean Code Principles)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **가독성 (Readability)**, **단순성 (Simplicity)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “19. 클린 코드 작성 원칙 (Clean Code Principles)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

* **가독성 (Readability)**: 누구든지 코드를 쉽게 읽을 수 있도록 작성.
* **단순성 (Simplicity)**: 코드를 간단하게 작성.
* **VI (Vietnamese) (Tiếng Việt):** Nguyên tắc viết code sạch. Dễ đọc, đơn giản.
* **Example**: 변수 이름을 `a` 대신 `userCount`로 짓는 것이 가독성을 높이는 것입니다.

Ta có thể khép mục **19. 클린 코드 작성 원칙 (Clean Code Principles)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **21. 외계인 코드 (Alien Code)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **19. 클린 코드 작성 원칙 (Clean Code Principles)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
