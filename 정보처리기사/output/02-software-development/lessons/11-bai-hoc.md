# 077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)

## 학습 목표 (Mục tiêu)
- Nắm vững phương pháp biểu diễn đồ thị trong bộ nhớ máy tính bằng Ma trận kề (인접 행렬 - Adjacency Matrix).
- Phân biệt tính chất đối xứng của ma trận kề giữa Đồ thị vô hướng (ma trận đối xứng) và Đồ thị có hướng (ma trận bất đối xứng).
- Thành thạo kỹ năng tính Bậc vào (In-degree), Bậc ra (Out-degree) và Tổng bậc của các đỉnh thông qua việc cộng tổng các hàng và cột trong ma trận kề.

## 핵심 키워드 (Từ khóa)
- 인접 행렬 (Adjacency Matrix)
- 무방향 그래프 대칭 행렬 (Symmetric Matrix)
- 방향 그래프 비대칭 행렬 (Asymmetric Matrix)
- 진입 차수 (In-degree) & 진출 차수 (Out-degree)
- 희소 그래프 (Sparse Graph) & 밀집 그래프 (Dense Graph)
- 공간 복잡도 $O(V^2)$

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Phân loại cấu trúc phi tuyến (Tree, Graph).
- [10-bai-hoc.md](10-bai-hoc.md): Định nghĩa đồ thị và các giải thuật tìm kiếm DFS / BFS.
- [14-bai-hoc.md](14-bai-hoc.md): Giới thiệu các thuật toán sắp xếp (Sorting Algorithms).

## 읽는 방법 (Cách đọc)
- Nhớ quy tắc đọc ma trận kề cho Đồ thị có hướng:
  - Tính tổng các phần tử trên **Hàng $i$ (Row)** $\rightarrow$ **Bậc ra (Out-degree / 진출 차수)**: Số cung xuất phát từ đỉnh $i$ đi ra ngoài.
  - Tính tổng các phần tử trên **Cột $j$ (Column)** $\rightarrow$ **Bậc vào (In-degree / 진입 차수)**: Số cung từ bên ngoài đi vào đỉnh $j$.
- Nhớ tính chất đối xứng: Đồ thị vô hướng luôn tạo ra ma trận **đối xứng qua đường chéo chính (Symmetric)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Biểu diễn đồ thị bằng Ma trận kề (Adjacency Matrix):**
  - Giả sử đồ thị có $N$ đỉnh: Ma trận kề $A$ là ma trận vuông kích thước $N \times N$.
  - Phần tử $A[i][j]$ được định nghĩa:
    $$A[i][j] = \begin{cases} 1 & \text{nếu có cạnh nối từ đỉnh } i \text{ đến đỉnh } j \\ 0 & \text{nếu không có cạnh nối} \end{cases}$$
- **Tính chất ma trận kề giữa hai loại đồ thị:**

| Tiêu chí | 무방향 그래프 (Đồ thị vô hướng) | 방향 그래프 (Đồ thị có hướng) |
| :--- | :--- | :--- |
| **Tính đối xứng** | **Luôn đối xứng qua đường chéo chính** ($A[i][j] = A[j][i]$) | Thường **không đối xứng** ($A[i][j] \ne A[j][i]$) |
| **Bậc ra (Out-degree / 진출 차수)** | Bằng tổng các số 1 trên hàng $i$ | **Tổng các số 1 trên hàng $i$** |
| **Bậc vào (In-degree / 진입 차수)** | Bằng tổng các số 1 trên cột $j$ (bằng bậc ra) | **Tổng các số 1 trên cột $j$** |
| **Tổng bậc của đỉnh** | Tổng hàng $i$ (hoặc tổng cột $i$) | $\text{Bậc ra (Hàng)} + \text{Bậc vào (Cột)}$ |

- **Đánh giá hiệu năng và không gian lưu trữ:**
  - **Không gian bộ nhớ:** Luôn tốn cố định $O(N^2)$ ô nhớ bất kể số cạnh nhiều hay ít.
  - **Khi nào nên dùng Ma trận kề:** Rất tốt cho **밀집 그래프 (Dense Graph - Đồ thị dày đặc nhiều cạnh)** vì tra cứu cạnh $O(1)$.
  - **Hạn chế lớn:** Lãng phí bộ nhớ nghiêm trọng đối với **희소 그래프 (Sparse Graph - Đồ thị thưa ít cạnh)** vì phần lớn ma trận toàn số 0. Khi đó nên dùng **인접 리스트 (Adjacency List)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ đọc ma trận kề đồ thị có hướng:**
  - Xét đồ thị có 3 đỉnh $\{1, 2, 3\}$ với ma trận kề:
    $$A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
    - Đỉnh 1: Hàng 1 có hai số 1 ($1 \rightarrow 2, 1 \rightarrow 3$) $\rightarrow$ $\text{Out-degree} = 2$. Cột 1 không có số 1 $\rightarrow$ $\text{In-degree} = 0$.
    - Đỉnh 2: Hàng 2 có một số 1 ($2 \rightarrow 3$) $\rightarrow$ $\text{Out-degree} = 1$. Cột 2 có một số 1 (từ đỉnh 1) $\rightarrow$ $\text{In-degree} = 1$.
    - Đỉnh 3: Hàng 3 toàn số 0 $\rightarrow$ $\text{Out-degree} = 0$. Cột 3 có hai số 1 (từ đỉnh 1 và 2) $\rightarrow$ $\text{In-degree} = 2$.

### 복습 체크리스트
- [ ] Khẳng định ma trận kề đồ thị vô hướng luôn là ma trận đối xứng.
- [ ] Tính đúng Out-degree (cộng theo hàng) và In-degree (cộng theo cột) của đồ thị có hướng.
- [ ] Nhớ không gian lưu trữ của ma trận kề là $O(N^2)$.
- [ ] Phân biệt khi nào dùng ma trận kề (Dense Graph) và khi nào dùng danh sách kề (Sparse Graph).
