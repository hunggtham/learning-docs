# 10. 이진 트리의 운행법 (Binary Tree Traversal)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **10. 이진 트리의 운행법 (Binary Tree Traversal)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối binary tree traversal với preorder, inorder, postorder và stack, để thứ tự duyệt gắn với câu hỏi cần trả lời.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **10. 이진 트리의 운행법 (Binary Tree Traversal)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **10. 이진 트리의 운행법 (Binary Tree Traversal)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **11. 수식의 표기법 (Expression Notation)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định preorder, inorder, postorder và stack trả lời câu hỏi nào; từ khóa khoanh vùng thứ tự duyệt trước khi nối sang kiến thức liên kết.

## 핵심 키워드 (Từ khóa)

이진, 트리의, 운행법

Kiến thức liên kết đặt traversal trên nền tree terms; cách đọc tiếp theo giúp chọn thứ tự theo dependency của bài toán.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **9. 트리 (Tree) 용어**에서 만든 기준을 이어받아 **10. 이진 트리의 운행법 (Binary Tree Traversal)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần traversal dùng khung đó để nối thứ tự xử lý với output cần tìm.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng quan hệ giữa thứ tự duyệt và câu hỏi thuật toán; khi sang expression notation, hãy giữ lại stack và dependency.

## 10. 이진 트리의 운행법 (Binary Tree Traversal)

Sau khi đã đặt nền bằng **9. 트리 (Tree) 용어**, ta chuyển sang **10. 이진 트리의 운행법 (Binary Tree Traversal)**. Đây là mắt xích 53/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **10. 이진 트리의 운행법 (Binary Tree Traversal)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **Preorder (전위)**, **Inorder (중위)**, **Postorder (후위)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “10. 이진 트리의 운행법 (Binary Tree Traversal)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **Preorder (전위)**: Root -> Left -> Right
- **Inorder (중위)**: Left -> Root -> Right
- **Postorder (후위)**: Left -> Right -> Root

Ta có thể khép mục **10. 이진 트리의 운행법 (Binary Tree Traversal)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **11. 수식의 표기법 (Expression Notation)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **10. 이진 트리의 운행법 (Binary Tree Traversal)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
