# 026: 그래프 (Graph / Đồ thị)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **026: 그래프 (Graph / Đồ thị)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **026: 그래프 (Graph / Đồ thị)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

그래프

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**에서 만든 기준을 이어받아 **026: 그래프 (Graph / Đồ thị)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **026: 그래프 (Graph / Đồ thị)** và nối nó với **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 026: 그래프 (Graph / Đồ thị)

Ở bước 10/101, **026: 그래프 (Graph / Đồ thị)** xuất hiện như phần tiếp nối của **078 & 079: 트리 및 운행법 (Tree & Tree Traversal)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **026: 그래프 (Graph / Đồ thị)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “026: 그래프 (Graph / Đồ thị)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **방향 그래프 (Directed Graph):** Có hướng. Tối đa `n(n-1)` cạnh (n là số đỉnh).
- **무방향 그래프 (Undirected Graph):** Vô hướng. Tối đa `n(n-1)/2` cạnh.

Trước hết, ta đặt **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)

Bây giờ ta đi vào nội dung của **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DFS (Depth-First Search - Tìm kiếm theo chiều sâu):** Đi sâu nhất có thể, hết đường mới lui lại (Dùng Stack).
- **BFS (Breadth-First Search - Tìm kiếm theo chiều rộng):** Loang ra xung quanh, tầng nào xong mới xuống tầng sau (Dùng Queue).

- 💡 **Mẹo ghi nhớ (Mnemonics):** DFS = Sâu = Stack (D/S). BFS = Rộng = Queue (B/Q). Vô hướng chia 2 vì AB và BA là một.

---

Với **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Với **탐색 알고리즘 (Thuật toán tìm kiếm đồ thị)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **026: 그래프 (Graph / Đồ thị)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.