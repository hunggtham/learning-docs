# 026: 그래프 (Graph / Đồ thị)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác cấu trúc dữ liệu Đồ thị (그래프 - Graph) gồm tập hợp các đỉnh (Vertices / 정점) và các cạnh (Edges / 간선).
- Phân biệt Đồ thị vô hướng (무방향 그래프) và Đồ thị có hướng (방향 그래프), nắm vững công thức tính số cạnh cực đại cho từng loại.
- Phân biệt hai giải thuật tìm kiếm đồ thị kinh điển: Tìm kiếm theo chiều sâu (DFS - 깊이 우선 탐색 dùng Stack) và Tìm kiếm theo chiều rộng (BFS - 너비 우선 탐색 dùng Queue).

## 핵심 키워드 (Từ khóa)
- 그래프 (Graph)
- 정점 (Vertex / Node) & 간선 (Edge)
- 방향 그래프 (Directed Graph): $n(n-1)$
- 무방향 그래프 (Undirected Graph): $n(n-1)/2$
- 깊이 우선 탐색 (DFS - Depth-First Search / 스택)
- 너비 우선 탐색 (BFS - Breadth-First Search / 큐)

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Phân loại cấu trúc dữ liệu tuyến tính và phi tuyến.
- [02-bai-hoc.md](02-bai-hoc.md): 스택 (Stack) và ứng dụng trong thuật toán DFS.
- [04-bai-hoc.md](04-bai-hoc.md): 큐 (Queue) và ứng dụng trong thuật toán BFS.
- [11-bai-hoc.md](11-bai-hoc.md): Biểu diễn đồ thị bằng Ma trận kề (Adjacency Matrix).

## 읽는 방법 (Cách đọc)
- Học thuộc công thức tính số cạnh: Có hướng thì $n(n-1)$, Vô hướng thì chia đôi $\frac{n(n-1)}{2}$.
- Nắm vững cặp đôi cấu trúc dữ liệu tương ứng của giải thuật tìm kiếm:
  - **DFS (Chiều sâu):** Đi sâu đến cùng rồi quay lui $\rightarrow$ Dùng **스택 (Stack)** hoặc đệ quy.
  - **BFS (Chiều rộng):** Loang dần theo từng tầng xung quanh $\rightarrow$ Dùng **큐 (Queue)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Đặc điểm cơ bản của Đồ thị (Graph):**
  - Là cấu trúc dữ liệu phi tuyến biểu diễn mối quan hệ đa chiều N - M giữa các đối tượng.
  - Ký hiệu: $G = (V, E)$ với $V$ là tập hợp các đỉnh (Vertices), $E$ là tập hợp các cạnh nối (Edges).
- **Phân loại đồ thị và công thức số cạnh tối đa:**

| Tiêu chí | 무방향 그래프 (Đồ thị vô hướng) | 방향 그래프 (Đồ thị có hướng) |
| :--- | :--- | :--- |
| **Đặc điểm cạnh** | Cạnh không có mũi tên định hướng; cạnh $(v_i, v_j)$ cũng chính là $(v_j, v_i)$ | Cạnh có mũi tên chỉ hướng; cung $\langle v_i, v_j \rangle$ khác với $\langle v_j, v_i \rangle$ |
| **Số cạnh tối đa** | $$\frac{n(n - 1)}{2}$$ | $$n(n - 1)$$ |
| **Bậc của đỉnh** | Tổng số cạnh nối trực tiếp vào đỉnh đó | Chia thành: Bậc vào (In-degree) và Bậc ra (Out-degree) |

- **Bảng so sánh hai giải thuật duyệt đồ thị cốt lõi:**

| Tiêu chí | 깊이 우선 탐색 (DFS - Depth-First Search) | 너비 우선 탐색 (BFS - Breadth-First Search) |
| :--- | :--- | :--- |
| **Cơ chế duyệt** | Khám phá càng sâu càng tốt dọc theo một nhánh trước khi quay lui (Backtracking) | Thăm tất cả các đỉnh lân cận ở mức hiện tại trước khi chuyển sang mức sâu hơn |
| **Cấu trúc dữ liệu** | **스택 (Stack)** hoặc hàm đệ quy (Recursion) | **큐 (Queue)** |
| **Ứng dụng điển hình** | Tìm thành phần liên thông, sắp xếp topo, giải mê cung, phát hiện chu trình | Tìm đường đi ngắn nhất trên đồ thị không trọng số, bài toán lan truyền mạng |

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Thuật toán duyệt đồ thị nào sử dụng cấu trúc dữ liệu Queue?"* $\rightarrow$ Đáp án: **BFS (너비 우선 탐색)**.
  - **Bẫy 2:** *"Đồ thị có hướng 6 đỉnh có tối đa bao nhiêu cạnh?"* $\rightarrow$ $6 \times (6 - 1) = 30$ cạnh.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Độ phức tạp thời gian của DFS và BFS:**
  - Nếu đồ thị được biểu diễn bằng **Ma trận kề (Adjacency Matrix)**: Cả DFS và BFS đều mất thời gian $O(V^2)$ do phải duyệt qua toàn bộ ma trận kích thước $V \times V$.
  - Nếu đồ thị được biểu diễn bằng **Danh sách kề (Adjacency List)**: Độ phức tạp tối ưu hơn, đạt $O(V + E)$ với $V$ là số đỉnh và $E$ là số cạnh.

### 복습 체크리스트
- [ ] Tính đúng số cạnh tối đa của đồ thị vô hướng $n(n-1)/2$ và có hướng $n(n-1)$.
- [ ] Ghi nhớ chắc chắn: DFS dùng Stack, BFS dùng Queue.
- [ ] Hiểu nguyên lý tìm kiếm: DFS đi sâu hết cỡ mới lùi lại, BFS loang theo tầng rộng.
- [ ] Nhớ độ phức tạp thời gian khi dùng danh sách kề là $O(V + E)$.
