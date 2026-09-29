# 4. 이진 트리의 운행법 (Binary Tree Traversal)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. 이진 트리의 운행법 (Binary Tree Traversal)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **4. 이진 트리의 운행법 (Binary Tree Traversal)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **30. 트리 구조 추가 용어 (Tree Terminology Additional)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

이진, 트리의, 운행법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 트리 (Tree)**에서 만든 기준을 이어받아 **4. 이진 트리의 운행법 (Binary Tree Traversal)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. 이진 트리의 운행법 (Binary Tree Traversal)

Sau khi đã đặt nền bằng **3. 트리 (Tree)**, ta chuyển sang **4. 이진 트리의 운행법 (Binary Tree Traversal)**. Đây là mắt xích 5/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **4. 이진 트리의 운행법 (Binary Tree Traversal)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **Preorder (전위)**, **Inorder (중위)**, **Postorder (후위)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **Preorder (전위)**: Root → Left → Right
* **Inorder (중위)**: Left → Root → Right
* **Postorder (후위)**: Left → Right → Root
* **VI (Vietnamese) (Tiếng Việt):**
  * Preorder: Gốc -> Trái -> Phải.
  * Inorder: Trái -> Gốc -> Phải.
  * Postorder: Trái -> Phải -> Gốc.
* **Example**: 수식 `A + B`를 전위 표기하면 `+ A B`, 중위 표기하면 `A + B`, 후위 표기하면 `A B +`가 됩니다.
* 💡 **Mẹo ghi nhớ**: Tiền/Trung/Hậu tố chỉ vị trí của Root (Gốc) so với Trái/Phải.

Ta có thể khép mục **4. 이진 트리의 운행법 (Binary Tree Traversal)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **30. 트리 구조 추가 용어 (Tree Terminology Additional)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.