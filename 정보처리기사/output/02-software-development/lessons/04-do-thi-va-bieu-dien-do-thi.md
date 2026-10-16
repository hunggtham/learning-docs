# 그래프와 그래프 탐색 (Đồ thị và biểu diễn đồ thị)

## 학습 목표
- Nắm vững định nghĩa Đồ thị (`그래프 / Graph` - cấu trúc phi tuyến $N - M$), ký hiệu toán học $G = (V, E)$, phân biệt Đồ thị vô hướng (`무방향 그래프`) và Đồ thị có hướng (`방향 그래프 / Di-Graph`).
- Áp dụng thành thạo 2 công thức tính số cạnh tối đa: Đồ thị vô hướng $\frac{n(n-1)}{2}$ và Đồ thị có hướng $n(n-1)$, cùng khái niệm Đồ thị đầy đủ (`완전 그래프 / Complete Graph`).
- Hiểu rõ khái niệm Bậc của đỉnh: Đồ thị vô hướng (tổng số cạnh nối) vs Đồ thị có hướng (Bậc vào `진입 차수 / In-degree` và Bậc ra `진출 차수 / Out-degree`).
- So sánh đối đầu 2 phương pháp biểu diễn đồ thị trong máy tính: Ma trận kề (`인접 행렬 / Adjacency Matrix` - ma trận $n \times n$, đối xứng qua đường chéo chính) và Danh sách kề (`인접 리스트 / Adjacency List` - mảng con trỏ danh sách liên kết).
- Phân biệt 2 giải thuật duyệt đồ thị kinh điển: Tìm kiếm theo chiều sâu (`깊이 우선 탐색 / DFS` - dùng Ngăn xếp Stack) và Tìm kiếm theo chiều rộng (`너비 우선 탐색 / BFS` - dùng Hàng đợi Queue).
- Nắm vững khái niệm Cây khung nhỏ nhất (`최소 비용 신장 트리 / MST`) và hai giải thuật tham lam: Kruskal (chọn cạnh trọng số nhỏ nhất, tránh chu trình) và Prim (phát triển từ đỉnh).

## 핵심 키워드
- 비선형 구조 (Cấu trúc phi tuyến / Graph / 정점 Vertex, 간선 Edge)
- 무방향 그래프 vs 방향 그래프 (Đồ thị vô hướng vs Đồ thị có hướng)
- 완전 그래프 (Đồ thị đầy đủ / Complete Graph / n(n-1)/2 vs n(n-1))
- 진입 차수 & 진출 차수 (In-degree & Out-degree)
- 인접 행렬 vs 인접 리스트 (Adjacency Matrix $O(n^2)$ vs Adjacency List $O(n+e)$)
- 깊이 우선 탐색 (DFS / Depth-First Search / 스택 Stack / 재귀)
- 너비 우선 탐색 (BFS / Breadth-First Search / 큐 Queue)
- 신장 트리 & MST (Spanning Tree & Minimum Spanning Tree / Kruskal, Prim)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [03-cay-va-duyet-cay-nhi-phan.md](03-cay-va-duyet-cay-nhi-phan.md), chúng ta đã khảo sát Cây - một đồ thị phân cấp đặc biệt không có chu trình.
- **Đang giải quyết gì (Current Problem):** Đồ thị giải quyết bài toán mô hình hóa các mạng lưới đa chiều phức tạp trong thực tế (mạng máy tính, giao thông, mạng xã hội). Bài học này thiết lập công thức tính số cạnh, phương pháp biểu diễn tối ưu bộ nhớ và giải thuật duyệt mạng lưới.
- **Dùng đi đâu (Forward Handoff):** Các kỹ thuật duyệt DFS/BFS và tính toán độ phức tạp chuyển tiếp trực tiếp sang [05-thuat-toan-sap-xep-va-do-phuc-tap.md](05-thuat-toan-sap-xep-va-do-phuc-tap.md) để đánh giá hiệu năng thuật toán qua ký pháp Big-O.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng 2 công thức tính số cạnh tối đa, bảng so sánh Ma trận kề vs Danh sách kề, bảng đối chiếu DFS vs BFS và các bẫy trắc nghiệm.
- Đọc TẦNG B để hiểu sâu bậc vào/bậc ra của đồ thị có hướng, cấu trúc ma trận kề đối xứng và cơ chế hoạt động của thuật toán Kruskal / Prim.

---

## 그래프와 그래프 탐색

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại đồ thị và công thức tính số cạnh tối đa
| Tiêu chí | 무방향 그래프 (Đồ thị vô hướng) | 방향 그래프 (Đồ thị có hướng / Di-Graph) |
| :--- | :--- | :--- |
| **Đặc điểm cạnh nối** | Cạnh không có mũi tên; $(u, v)$ và $(v, u)$ là một cạnh duy nhất | Cạnh có mũi tên; cung $\langle u, v \rangle$ ($u \rightarrow v$) khác hoàn toàn với cung $\langle v, u \rangle$ |
| **Công thức số cạnh tối đa** | $\mathbf{\frac{n(n - 1)}{2}}$ | $\mathbf{n(n - 1)}$ |
| **Đồ thị đầy đủ (Complete)** | Đạt đúng $\frac{n(n-1)}{2}$ cạnh | Đạt đúng $n(n-1)$ cạnh |
| **Ví dụ: $n = 5$ đỉnh** | Tối đa: $\frac{5 \times 4}{2} = \mathbf{10}$ cạnh | Tối đa: $5 \times 4 = \mathbf{20}$ cạnh |
| **Ví dụ: $n = 6$ đỉnh** | Tối đa: $\frac{6 \times 5}{2} = \mathbf{15}$ cạnh | Tối đa: $6 \times 5 = \mathbf{30}$ cạnh |

#### 2. Bảng so sánh Ma trận kề vs Danh sách kề
| Tiêu chí | 인접 행렬 (Adjacency Matrix) | 인접 리스트 (Adjacency List) |
| :--- | :--- | :--- |
| **Bản chất lưu trữ** | Mảng 2 chiều kích thước $n \times n$ ($A[i][j] \in \{0, 1\}$) | Mảng các danh sách liên kết trỏ đến các đỉnh kề |
| **Dung lượng bộ nhớ** | Luôn tốn cố định **$O(n^2)$** | Tiết kiệm: **$O(n + e)$** ($e$ là số cạnh) |
| **Đặc tính ma trận vô hướng** | **Đối xứng qua đường chéo chính** ($A[i][j] = A[j][i]$) | Không có tính chất này |
| **Độ phức tạp kiểm tra kề** | Rất nhanh: **$O(1)$** kiểm tra ô $A[i][j]$ | Chậm hơn: Phải duyệt danh sách kề |
| **Trường hợp áp dụng** | **Đồ thị dày / nhiều cạnh (밀집 그래프 - Dense Graph)** | **Đồ thị thưa / ít cạnh (희소 그래프 - Sparse Graph)** |

#### 3. Bảng đối chiếu DFS vs BFS
| Tiêu chí | 깊이 우선 탐색 (DFS) | 너비 우선 탐색 (BFS) |
| :--- | :--- | :--- |
| **Chiến lược duyệt** | Đi sâu theo từng nhánh đến kịch sàn, gặp ngõ cụt thì quay lui | Thăm toàn bộ các đỉnh láng giềng kề cận trước khi sang tầng sâu hơn |
| **Cấu trúc dữ liệu bổ trợ** | **스택 (Stack)** hoặc hàm gọi đệ quy | **큐 (Queue)** |
| **Độ phức tạp ma trận kề** | $O(n^2)$ | $O(n^2)$ |
| **Độ phức tạp danh sách kề** | $O(n + e)$ | $O(n + e)$ |
| **Ứng dụng tiêu biểu** | Tìm chu trình, bài toán mê cung, sắp xếp tô-pô | **Tìm đường đi ngắn nhất** trên đồ thị không trọng số |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Quên chia đôi số cạnh đồ thị vô hướng:** Đồ thị vô hướng có $n = 5$ đỉnh $\rightarrow \frac{5 \times 4}{2} = 10$ cạnh (thí sinh hay chọn nhầm $5 \times 4 = 20$).
- **Bẫy 2: Thần chú cấu trúc dữ liệu DFS vs BFS:**
  - **DFS (깊이 우선)** $\leftrightarrow$ **Stack (스택)**
  - **BFS (너비 우선)** $\leftrightarrow$ **Queue (큐)**
- **Bẫy 3: Tính đối xứng của Ma trận kề:** Ma trận kề của đồ thị **vô hướng** luôn là ma trận đối xứng qua đường chéo chính ($A[i][j] = A[j][i]$). Ma trận kề của đồ thị có hướng không có tính đối xứng này.
- **Bẫy 4: Số cạnh của Cây khung (Spanning Tree):** Đồ thị liên thông có $n$ đỉnh thì mọi cây khung của nó luôn chứa đúng **$n - 1$ cạnh**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bậc của đỉnh trong Đồ thị có hướng (Di-Graph)
- **Bậc vào (진입 차수 / In-degree):** Số lượng cung có mũi tên trỏ thẳng VÀO đỉnh đó (đếm số số 1 trên cột tương ứng trong ma trận kề).
- **Bậc ra (진출 차수 / Out-degree):** Số lượng cung có mũi tên xuất phát TỪ đỉnh đó trỏ đi (đếm số số 1 trên hàng tương ứng trong ma trận kề).
- Tổng số bậc vào của toàn bộ các đỉnh luôn bằng tổng số bậc ra và bằng đúng tổng số cạnh của đồ thị:
  $$\sum \text{In-degree} = \sum \text{Out-degree} = |E|$$

#### 2. Cây khung nhỏ nhất (MST - Minimum Spanning Tree)
Cây khung là đồ thị con chứa toàn bộ $n$ đỉnh của đồ thị gốc nhưng chỉ có đúng $n-1$ cạnh và không chứa chu trình. Cây khung nhỏ nhất là cây khung có tổng trọng số các cạnh là nhỏ nhất:
- **Thuật toán Kruskal (크루스칼 알고리즘):**
  - Sắp xếp tất cả các cạnh theo thứ tự trọng số tăng dần.
  - Lần lượt chọn các cạnh có trọng số nhỏ nhất đưa vào cây khung, miễn là cạnh đó **không tạo thành chu trình** (kiểm tra chu trình bằng thuật toán Union-Find).
  - Lặp lại cho đến khi chọn đủ đúng $n - 1$ cạnh.
  - Phù hợp nhất với đồ thị thưa (Sparse Graph).
- **Thuật toán Prim (프림 알고리즘):**
  - Bắt đầu từ một đỉnh gốc bất kỳ.
  - Tại mỗi bước, chọn cạnh có trọng số nhỏ nhất nối một đỉnh đã nằm trong cây với một đỉnh chưa nằm trong cây.
  - Lặp lại cho đến khi toàn bộ $n$ đỉnh được kết nối.
  - Phù hợp nhất với đồ thị dày (Dense Graph).

---

### 복습 체크리스트
- [ ] Tính thành thạo số cạnh tối đa của đồ thị vô hướng: $\frac{n(n-1)}{2}$.
- [ ] Tính thành thạo số cạnh tối đa của đồ thị có hướng: $n(n-1)$.
- [ ] Phân biệt 진입 차수 (In-degree) và 진출 차수 (Out-degree) trong đồ thị có hướng.
- [ ] Nhớ ma trận kề của đồ thị vô hướng luôn đối xứng qua đường chéo chính.
- [ ] Chọn Adjacency Matrix cho đồ thị dày và Adjacency List cho đồ thị thưa.
- [ ] Nhớ thần chú: DFS dùng Stack, BFS dùng Queue.
- [ ] Nhớ Cây khung của đồ thị có $n$ đỉnh luôn có đúng $n - 1$ cạnh.
- [ ] Phân biệt giải thuật Kruskal (chọn cạnh, tránh chu trình) và Prim (phát triển từ đỉnh).
