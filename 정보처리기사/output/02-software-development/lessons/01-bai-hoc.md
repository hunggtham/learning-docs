# 1. 자료 구조의 분류 (Classification of Data Structures)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **1. 자료 구조의 분류 (Classification of Data Structures)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **1. 자료 구조의 분류 (Classification of Data Structures)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 스택 (Stack) 및 응용 (Applications)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

자료, 구조의, 분류

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 자료 구조의 분류 (Classification of Data Structures)**을(를) 독립된 암기 항목으로 두지 않고, 이 과목에서 다룰 문제의 출발점으로 삼는다. 먼저 무엇을 설명하는지와 어디까지 적용되는지를 확인한 뒤 세부 규칙으로 들어간다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 1. 자료 구조의 분류 (Classification of Data Structures)

Chúng ta bắt đầu mạch học bằng **1. 자료 구조의 분류 (Classification of Data Structures)**. Trước khi đi vào từng thuật ngữ, hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục 1/95 là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, không chỉ được ghi nhớ như danh sách.

Để đọc **1. 자료 구조의 분류 (Classification of Data Structures)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **선형 구조 (Linear Structure)**, **비선형 구조 (Non-linear Structure)**, **방향/무방향 그래프의 최대 간선 수 (Maximum edges in graphs)**, **Example** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

* **선형 구조 (Linear Structure)**: 배열(Array), 선형 리스트(Linear List), 스택(Stack), 큐(Queue), 데크(Deque)
* **비선형 구조 (Non-linear Structure)**: 트리(Tree), 그래프(Graph)
* **방향/무방향 그래프의 최대 간선 수 (Maximum edges in graphs)**:
  * 무방향 그래프 (Undirected Graph): n(n-1)/2
  * 방향 그래프 (Directed Graph): n(n-1)
* **VI (Vietnamese) (Tiếng Việt):**
  * Cấu trúc tuyến tính: Mảng, danh sách tuyến tính, ngăn xếp, hàng đợi, hàng đợi hai đầu.
  * Cấu trúc phi tuyến: Cây, Đồ thị.
  * Số cạnh tối đa: Đồ thị vô hướng là n(n-1)/2, có hướng là n(n-1).
* **Example**: 노드가 4개인 무방향 그래프의 최대 간선 수는 4(4-1)/2 = 6개입니다. (Với đồ thị vô hướng có 4 đỉnh, số cạnh tối đa là 6).
* 💡 **Mẹo ghi nhớ**: Tuyến tính (Linear) là một đường thẳng (Mảng, Stack, Queue). Phi tuyến là rẽ nhánh (Cây, Đồ thị).

Như vậy, **1. 자료 구조의 분류 (Classification of Data Structures)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **2. 스택 (Stack) 및 응용 (Applications)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.