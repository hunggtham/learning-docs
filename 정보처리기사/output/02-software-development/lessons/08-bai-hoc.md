# 026: 그래프 (Graph / Đồ thị)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **026: 그래프 (Graph / Đồ thị)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **026: 그래프 (Graph / Đồ thị)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 수식의 표기법 변환 (Expression Notation Conversion)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

그래프

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **025: 트리 (Tree / Cây)**에서 만든 기준을 이어받아 **026: 그래프 (Graph / Đồ thị)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 026: 그래프 (Graph / Đồ thị)

Sau khi đã đặt nền bằng **025: 트리 (Tree / Cây)**, ta chuyển sang **026: 그래프 (Graph / Đồ thị)**. Đây là mắt xích 8/95 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **026: 그래프 (Graph / Đồ thị)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **방향 그래프 (Directed Graph):** Có hướng. Tối đa `n(n-1)` cạnh (n là số đỉnh).
- **무방향 그래프 (Undirected Graph):** Vô hướng. Tối đa `n(n-1)/2` cạnh.

Ta bắt đầu phần nội dung bằng **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**. Hãy xác định **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)

Phần nguồn của **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **DFS (Depth-First Search - Tìm kiếm theo chiều sâu):** Đi sâu nhất có thể, hết đường mới lui lại (Dùng Stack).
- **BFS (Breadth-First Search - Tìm kiếm theo chiều rộng):** Loang ra xung quanh, tầng nào xong mới xuống tầng sau (Dùng Queue).

- 💡 **Mẹo ghi nhớ (Mnemonics):** DFS = Sâu = Stack (D/S). BFS = Rộng = Queue (B/Q). Vô hướng chia 2 vì AB và BA là một.

---

Với **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Ta có thể khép mục **026: 그래프 (Graph / Đồ thị)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. 수식의 표기법 변환 (Expression Notation Conversion)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.