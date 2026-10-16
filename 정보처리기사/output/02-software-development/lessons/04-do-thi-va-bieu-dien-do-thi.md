# 그래프와 탐색 알고리즘 (Đồ thị và biểu diễn đồ thị)

## 학습 목표
- Nắm vững định nghĩa đồ thị $G = (V, E)$, phân biệt đồ thị vô hướng (`무방향 그래프`) và có hướng (`방향 그래프`), tính đúng số cạnh tối đa: vô hướng là $\frac{n(n-1)}{2}$, có hướng là $n(n-1)$.
- So sánh hai phương pháp biểu diễn đồ thị trong bộ nhớ: Ma trận kề (`인접 행렬` - $O(n^2)$, tối ưu cho đồ thị dày) và Danh sách kề (`인접 리스트` - $O(n+e)$, tối ưu cho đồ thị thưa).
- Tính chuẩn xác Bậc vào (`진입 차수 / In-degree` - tổng cột) và Bậc ra (`진출 차수 / Out-degree` - tổng hàng) trong ma trận kề của đồ thị có hướng.
- So sánh đối đầu giữa hai giải thuật duyệt đồ thị: DFS (`깊이 우선 탐색` - dùng Stack hoặc đệ quy) và BFS (`너비 우선 탐색` - dùng Queue, tìm đường đi ngắn nhất trên đồ thị không trọng số).
- Phân biệt định nghĩa Cây khung (`신장 트리 / Spanning Tree` - gồm $n$ đỉnh và đúng $n-1$ cạnh) và hai thuật toán tìm cây khung nhỏ nhất MST: Kruskal (theo cạnh) và Prim (theo đỉnh).

## 핵심 키워드
- 그래프 (Đồ thị / Graph / 정점 Vertex, 간선 Edge)
- 완전 그래프 (Đồ thị đầy đủ / Complete Graph / n(n-1)/2 vs n(n-1))
- 인접 행렬 (Ma trận kề / Adjacency Matrix / O(n²) / 대칭행렬 vs 비대칭행렬)
- 진입 차수 vs 진출 차수 (In-degree vs Out-degree / 열의 합 vs 행의 합)
- 인접 리스트 (Danh sách kề / Adjacency List / O(n+e))
- DFS vs BFS (깊이 우선 탐색 Stack vs 너비 우선 탐색 Queue)
- 최소 비용 신장 트리 (MST / Minimum Spanning Tree / 크루스칼 Kruskal, 프림 Prim)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [03-cay-va-duyet-cay-nhi-phan.md](03-cay-va-duyet-cay-nhi-phan.md), chúng ta đã nghiên cứu cấu trúc Cây — một dạng đồ thị phân cấp đặc biệt không chứa chu trình.
- **Đang giải quyết gì (Current Problem):** Bài học này mở rộng phạm vi ra cấu trúc mạng lưới tổng quát nhất với quan hệ $N - M$ và cho phép chu trình (đồ thị mạng máy tính, bản đồ giao thông), giải quyết bài toán biểu diễn bộ nhớ tối ưu và tìm kiếm đường đi qua DFS/BFS.
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn tất 4 bài học cấu trúc dữ liệu nền tảng, chúng ta chuyển sang khảo sát thao tác tốn tài nguyên nhất trong xử lý dữ liệu với [05-thuat-toan-sap-xep-va-do-phuc-tap.md](05-thuat-toan-sap-xep-va-do-phuc-tap.md) để làm chủ 8 thuật toán sắp xếp kinh điển.

## 읽는 방법
- Đọc TẦNG A để nắm chắc hai công thức tính số cạnh tối đa, quy tắc tính bậc vào/ra trên ma trận kề và cặp đôi DFS (Stack) vs BFS (Queue).
- Đọc TẦNG B để hiểu sâu sự đánh đổi giữa Ma trận kề (Dense Graph) và Danh sách kề (Sparse Graph) cùng hai thuật toán tham lam Kruskal và Prim.

---

## 그래프와 탐색 알고리즘

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại đồ thị và công thức số cạnh tối đa
| Tiêu chuẩn so sánh | 무방향 그래프 (Đồ thị vô hướng) | 방향 그래프 (Đồ thị có hướng) |
| :--- | :--- | :--- |
| **Đặc điểm cạnh nối** | Cạnh không có mũi tên; $(u, v)$ và $(v, u)$ là một cạnh | Cạnh có mũi tên; cung $\langle u, v \rangle$ khác cung $\langle v, u \rangle$ |
| **Công thức số cạnh tối đa** | $$\mathbf{\frac{n(n - 1)}{2}}$$ | $$\mathbf{n(n - 1)}$$ |
| **Bậc của đỉnh** | Tổng số cạnh nối trực tiếp vào đỉnh đó | Tách thành **진입 차수 (In-degree)** và **진출 차수 (Out-degree)** |
| **Ma trận kề** | **Luôn đối xứng qua đường chéo chính** | Nói chung là ma trận bất đối xứng |

#### 2. Đối chiếu Ma trận kề vs Danh sách kề
| Tiêu chí | 인접 행렬 (Adjacency Matrix) | 인접 리스트 (Adjacency List) |
| :--- | :--- | :--- |
| **Cấu trúc lưu trữ** | Mảng 2 chiều kích thước $n \times n$ | Mảng gồm $n$ con trỏ trỏ tới các Linked List |
| **Không gian bộ nhớ** | **Cố định $O(n^2)$** | **Tiết kiệm $O(n + e)$** |
| **Kiểm tra cạnh $(u, v)$**| Cực nhanh: $O(1)$ (`A[u][v] == 1`) | Chậm hơn: $O(\text{Degree}(u))$ |
| **Môi trường tối ưu** | **밀집 그래프 (Dense Graph - nhiều cạnh)** | **희소 그래프 (Sparse Graph - ít cạnh)** |

#### 3. Bảng so sánh đối đầu DFS vs BFS
| Tiêu chí | 깊이 우선 탐색 (DFS) | 너비 우선 탐색 (BFS) |
| :--- | :--- | :--- |
| **Cơ chế duyệt** | Đi sâu nhất có thể theo một nhánh rồi quay lui (**Backtracking**) | Loang dần, thăm toàn bộ các đỉnh cùng tầng trước khi xuống sâu |
| **Cấu trúc hỗ trợ** | **스택 (Stack)** hoặc Đệ quy (Recursion) | **큐 (Queue)** |
| **Đường đi tìm kiếm**| Không đảm bảo ngắn nhất | **Luôn tìm được đường đi ngắn nhất (đồ thị không trọng số)** |
| **Độ phức tạp** | $O(V^2)$ với ma trận kề; $O(V + E)$ với danh sách kề | $O(V^2)$ với ma trận kề; $O(V + E)$ với danh sách kề |

#### 4. Cây khung nhỏ nhất (MST - Kruskal vs Prim)
- **Spanning Tree (신장 트리):** Đồ thị con liên thông chứa toàn bộ $n$ đỉnh và **đúng $n - 1$ cạnh**.
- **Kruskal's Algorithm:** Sắp xếp các cạnh tăng dần; lần lượt chọn cạnh nhỏ nhất không tạo chu trình (theo cạnh, phù hợp đồ thị thưa).
- **Prim's Algorithm:** Bắt đầu từ 1 đỉnh; mỗi bước kết nối đỉnh mới vào cây bằng cạnh có trọng số nhỏ nhất (theo đỉnh, phù hợp đồ thị dày).

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Bậc vào và Bậc ra trong Ma trận kề có hướng:**
  - **진출 차수 (Out-degree):** Bằng **tổng các số 1 trên Hàng $i$** (các cung đi ra).
  - **진입 차수 (In-degree):** Bằng **tổng các số 1 trên Cột $j$** (các cung đi vào).
- **Bẫy 2: Cấu trúc dữ liệu của DFS và BFS:**
  - Cứ nhắc đến **DFS** $\rightarrow$ Chọn **Stack** (hoặc đệ quy).
  - Cứ nhắc đến **BFS** $\rightarrow$ Chọn **Queue**.
- **Bẫy 3: Đường đi ngắn nhất:** Thuật toán luôn tìm được đường đi ngắn nhất trên đồ thị không có trọng số là **BFS**, không phải DFS.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Tính toán ma trận kề thực tế
- Giả sử ma trận kề của đồ thị có hướng 4 đỉnh:
  $$A = \begin{pmatrix} 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 1 & 0 \end{pmatrix}$$
- Muốn tìm Bậc ra của đỉnh 1: Cộng các số trên Hàng 1: $0 + 1 + 1 + 0 = 2$.
- Muốn tìm Bậc vào của đỉnh 3: Cộng các số trên Cột 3: $1 + 1 + 0 + 1 = 3$.

#### 2. Kiểm tra chu trình trong thuật toán Kruskal
- Thuật toán Kruskal sử dụng cấu trúc dữ liệu **Tập hợp rời rạc (Disjoint Set / Union-Find)** với hai phép toán `Find` và `Union`. Nếu hai đỉnh đầu mút của một cạnh cùng thuộc về một tập hợp đại diện (chung Root), việc thêm cạnh đó sẽ tạo ra chu trình khép kín và bị từ chối ngay lập tức.

---

### 복습 체크리스트
- [ ] Tính đúng công thức số cạnh cực đại: Vô hướng là $\frac{n(n-1)}{2}$, Có hướng là $n(n-1)$.
- [ ] Khẳng định ma trận kề của đồ thị vô hướng luôn là ma trận đối xứng qua đường chéo chính.
- [ ] Tính chuẩn xác: Bậc ra (Out-degree) bằng tổng hàng; Bậc vào (In-degree) bằng tổng cột trong ma trận kề có hướng.
- [ ] Phân biệt khi nào dùng Ma trận kề ($O(n^2)$ - Dense Graph) và Danh sách kề ($O(n+e)$ - Sparse Graph).
- [ ] Ghi nhớ chắc chắn: DFS dùng Stack (hoặc đệ quy), BFS dùng Queue.
- [ ] Nhớ BFS luôn tìm được đường đi ngắn nhất trên đồ thị không trọng số.
- [ ] Định nghĩa Spanning Tree có $n$ đỉnh và đúng $n - 1$ cạnh.
- [ ] Phân biệt thuật toán Kruskal (chọn cạnh nhỏ nhất không tạo chu trình) và Prim (phát triển từ đỉnh).
