# Môn 2 · Bài 04 — Cấu trúc phi tuyến: Đồ thị và biểu diễn đồ thị

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Nếu như [Bài 03](03-cay-va-duyet-cay-nhi-phan.md) nghiên cứu Cây — một đồ thị phân cấp đặc biệt không có chu trình, thì bài học này mở rộng phạm vi ra cấu trúc mạng lưới tổng quát nhất trong khoa học máy tính: **Đồ thị (그래프 — Graph)**. Bài học trang bị công thức tính số cạnh tối đa, hai phương pháp biểu diễn trong bộ nhớ máy tính (Ma trận kề vs Danh sách kề), hai thuật toán duyệt đồ thị kinh điển (DFS và BFS) cùng khái niệm cây khung nhỏ nhất (MST).

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `10-bai-hoc.md`, `11-bai-hoc.md` và phần đồ thị trong `01-bai-hoc.md` (tương ứng với các mục 1, 026, 077 trong tài liệu chuẩn gốc). Toàn bộ công thức toán học và bảng tính toán In-degree / Out-degree được đối chiếu chuẩn xác với giáo trình khảo thí HRDK.

> **Mạch kiến thức:** Đồ thị mô hình hóa các mối quan hệ đa chiều $N - M$ trong thế giới thực (mạng máy tính, bản đồ giao thông, mạng xã hội). Bài học này giải quyết ba vấn đề kỹ thuật: (1) Công thức tính số cạnh tối đa của đồ thị vô hướng và có hướng được thiết lập từ đâu? (2) Khi nào nên dùng Ma trận kề (Adjacency Matrix) và khi nào bắt buộc phải dùng Danh sách kề (Adjacency List) để tối ưu bộ nhớ? (3) Hai giải thuật tìm kiếm DFS (dùng Stack) và BFS (dùng Queue) khác nhau ra sao về cơ chế duyệt và ứng dụng thực tiễn?

---

## 1. 그래프(Graph)의 개념 및 분류 체계 — Khái niệm và phân loại đồ thị

**그래프는 정점(Vertex)과 정점들을 연결하는 간선(Edge)의 집합으로 구성된 네트워크형 비선형 자료구조이다.**

Đồ thị được ký hiệu toán học là $G = (V, E)$, trong đó $V$ là tập hợp các đỉnh (Vertices / Nodes) và $E$ là tập hợp các cạnh nối (Edges / Branches).

### Phân loại đồ thị và công thức tính số cạnh tối đa

Giả sử một đồ thị có $n$ đỉnh ($|V| = n$):

| Tiêu chuẩn so sánh | 무방향 그래프 (Đồ thị vô hướng) | 방향 그래프 (Đồ thị có hướng / Di-Graph) |
| :--- | :--- | :--- |
| **Đặc điểm cạnh nối** | Các cạnh không có mũi tên chỉ hướng; cạnh $(u, v)$ và $(v, u)$ là một cạnh duy nhất | Các cạnh có mũi tên chỉ hướng; cung $\langle u, v \rangle$ ($u \rightarrow v$) khác hoàn toàn với cung $\langle v, u \rangle$ ($v \rightarrow u$) |
| **Công thức số cạnh tối đa** | $$\mathbf{\frac{n(n - 1)}{2}}$$ | $$\mathbf{n(n - 1)}$$ |
| **Giải thích công thức** | Mỗi đỉnh có thể nối với $n-1$ đỉnh còn lại, nhưng mỗi cạnh nối giữa 2 đỉnh được tính chung $\rightarrow$ chia đôi | Mỗi cặp đỉnh có thể có 2 cung ngược chiều nhau $\rightarrow$ giữ nguyên |
| **Khái niệm bậc của đỉnh** | Tổng số cạnh nối trực tiếp vào đỉnh đó | Chia làm hai loại: **Bậc vào (In-degree)** và **Bậc ra (Out-degree)** |

### Khái niệm Đồ thị đầy đủ (완전 그래프 — Complete Graph)
- Là đồ thị mà giữa hai đỉnh bất kỳ luôn luôn có một cạnh nối trực tiếp.
- Đồ thị vô hướng đầy đủ có đúng $\frac{n(n-1)}{2}$ cạnh; đồ thị có hướng đầy đủ có đúng $n(n-1)$ cạnh.

### Ví dụ tính toán nhanh trong đề thi
- Đồ thị vô hướng có $n = 5$ đỉnh: Số cạnh tối đa là $\frac{5 \times 4}{2} = \mathbf{10}$ cạnh.
- Đồ thị có hướng có $n = 6$ đỉnh: Số cạnh tối đa là $6 \times 5 = \mathbf{30}$ cạnh.

---

## 2. 그래프의 메모리 표현 방식 — Biểu diễn đồ thị trong máy tính

Có hai phương pháp chính để lưu trữ đồ thị vào bộ nhớ máy tính:

### 2.1. 인접 행렬 (Adjacency Matrix — Ma trận kề)
- **Cơ chế:** Dùng một ma trận vuông 2 chiều kích thước $n \times n$ (với $n$ là số đỉnh).
- Phần tử $A[i][j]$ được định nghĩa:
  $$A[i][j] = \begin{cases} 1 & \text{nếu có cạnh nối từ đỉnh } i \text{ sang đỉnh } j \\ 0 & \text{nếu không có cạnh nối} \end{cases}$$

#### Tính chất cốt lõi của Ma trận kề chuẩn đề thi:
1. **Đồ thị vô hướng (무방향 그래프):**
   - Ma trận kề **luôn luôn đối xứng qua đường chéo chính** ($A[i][j] = A[j][i]$).
   - Bậc của đỉnh $i$ bằng tổng các số 1 trên hàng $i$ (hoặc tổng trên cột $i$).
2. **Đồ thị có hướng (방향 그래프):**
   - Ma trận kề nói chung là **ma trận bất đối xứng** ($A[i][j] \ne A[j][i]$).
   - **Bậc ra (진출 차수 — Out-degree):** Bằng **tổng các số 1 trên Hàng $i$** (số cung xuất phát từ đỉnh $i$ đi ra ngoài).
   - **Bậc vào (진입 차수 — In-degree):** Bằng **tổng các số 1 trên Cột $j$** (số cung từ các đỉnh khác đi vào đỉnh $j$).
   - Tổng bậc của đỉnh $i$: $\text{Degree}(i) = \text{In-degree} + \text{Out-degree}$.

#### Đánh giá ưu nhược điểm:
- **Ưu điểm:** Kiểm tra xem hai đỉnh có cạnh nối hay không cực nhanh với thời gian tức thời $O(1)$ (`if (A[u][v] == 1)`). Rất phù hợp cho **밀집 그래프 (Dense Graph — Đồ thị dày đặc nhiều cạnh)**.
- **Nhược điểm:** Tốn kém bộ nhớ cố định $O(n^2)$ bất kể đồ thị có ít cạnh đến đâu. Rất lãng phí cho **희소 그래프 (Sparse Graph — Đồ thị thưa ít cạnh)** vì phần lớn ma trận toàn số 0.

---

### 2.2. 인접 리스트 (Adjacency List — Danh sách kề)
- **Cơ chế:** Dùng một mảng gồm $n$ con trỏ Head, mỗi phần tử của mảng trỏ đến một Danh sách liên kết (Linked List) chứa tất cả các đỉnh kề với nó.
- **Ưu điểm:** Tiết kiệm bộ nhớ tối đa, không gian lưu trữ chỉ tốn đúng $O(n + e)$ (với $n$ là số đỉnh, $e$ là số cạnh). Rất tối ưu cho đồ thị thưa (Sparse Graph).
- **Nhược điểm:** Để kiểm tra xem đỉnh $u$ có nối với đỉnh $v$ hay không, ta phải duyệt tuần tự danh sách liên kết của đỉnh $u$, tốn thời gian $O(\text{Degree}(u))$.

---

## 3. 그래프 탐색 알고리즘 — Hai giải thuật duyệt đồ thị kinh điển

Duyệt đồ thị là quá trình ghé thăm tất cả các đỉnh có thể đến được từ một đỉnh xuất phát, đảm bảo mỗi đỉnh chỉ được thăm đúng một lần duy nhất (sử dụng mảng đánh dấu `visited[]`).

### Bảng so sánh đối đầu DFS vs BFS

| Tiêu chí | 깊이 우선 탐색 (DFS - Depth-First Search) | 너비 우선 탐색 (BFS - Breadth-First Search) |
| :--- | :--- | :--- |
| **Cơ chế duyệt** | Đi sâu nhất có thể dọc theo một nhánh trước khi quay lui (**Backtracking**) | Loang dần, thăm toàn bộ các đỉnh lân cận cùng tầng trước khi chuyển xuống tầng sâu hơn |
| **Cấu trúc dữ liệu** | **스택 (Stack)** hoặc hàm đệ quy (Recursion) | **큐 (Queue)** |
| **Đường đi tìm kiếm** | Không đảm bảo tìm được đường đi ngắn nhất | **Luôn tìm được đường đi ngắn nhất** trên đồ thị không có trọng số |
| **Ứng dụng điển hình** | Phát hiện chu trình (Cycle detection), Sắp xếp tô-pô (Topological Sort), Giải mê cung, Phân tích thành phần liên thông mạnh | Tìm đường đi ngắn nhất, Bài toán lan truyền virus mạng, Phân tích mạng lưới xã hội (Bậc kết nối) |
| **Độ phức tạp** | Dùng Ma trận kề: $O(V^2)$; Dùng Danh sách kề: $O(V + E)$ | Dùng Ma trận kề: $O(V^2)$; Dùng Danh sách kề: $O(V + E)$ |

---

## 4. 최소 비용 신장 트리 (MST — Minimum Spanning Tree)

Trong các bài toán thiết kế mạng lưới cáp quang hoặc đường ống dẫn nước với chi phí tối thiểu, khái niệm Cây khung nhỏ nhất đóng vai trò quyết định:

### 4.1. 신장 트리 (Spanning Tree — Cây khung)
- Là đồ thị con chứa **toàn bộ $n$ đỉnh** của đồ thị gốc $G$, liên thông và không có chu trình.
- Cây khung của một đồ thị $n$ đỉnh **bắt buộc phải có đúng đúng $n - 1$ cạnh**.

### 4.2. 최소 비용 신장 트리 (MST — Cây khung nhỏ nhất)
- Trong đồ thị có trọng số (Weighted Graph), MST là cây khung có **tổng trọng số các cạnh là nhỏ nhất**.
- Hai thuật toán tham lam (Greedy) kinh điển để tìm MST:
  1. **크루스칼 알고리즘 (Kruskal's Algorithm):**
     - Sắp xếp tất cả các cạnh theo trọng số tăng dần.
     - Lần lượt chọn cạnh có trọng số nhỏ nhất thêm vào cây khung, với điều kiện cạnh được chọn **không được tạo thành chu trình** (kiểm tra chu trình bằng cấu trúc tập hợp rời rạc Union-Find / Disjoint Set).
     - Dừng lại khi đã chọn đủ $n - 1$ cạnh. Phù hợp cho đồ thị thưa.
  2. **프림 알고리즘 (Prim's Algorithm):**
     - Bắt đầu từ một đỉnh tùy ý.
     - Tại mỗi bước, chọn cạnh có trọng số nhỏ nhất nối một đỉnh đã có trong cây với một đỉnh chưa có trong cây.
     - Lặp lại cho đến khi toàn bộ $n$ đỉnh được kết nối. Phù hợp cho đồ thị dày.

---

## 5. Nối mạch kiến thức sang bài tiếp theo

Đến đây, chúng ta đã hoàn thành trọn vẹn việc khảo sát các cấu trúc dữ liệu nền tảng trong bộ nhớ máy tính: từ cấu trúc tuyến tính ([Bài 01](01-cau-truc-du-lieu-tuyen-tinh.md)), ký pháp ngăn xếp ([Bài 02](02-ky-phap-bieu-thuc-va-stack.md)), cấu trúc cây ([Bài 03](03-cay-va-duyet-cay-nhi-phan.md)) cho đến cấu trúc mạng lưới đồ thị ([Bài 04](04-do-thi-va-bieu-dien-do-thi.md)).

Khi dữ liệu đã được nạp vào các cấu trúc này, thao tác xử lý thường xuyên và tốn kém tài nguyên nhất chính là **sắp xếp thứ tự dữ liệu**. Chúng ta sẽ chuyển sang bài học đồ sộ bậc nhất của Chương 1: **[Bài 05: Độ phức tạp và thuật toán sắp xếp](05-thuat-toan-sap-xep-va-do-phuc-tap.md)**, nơi ta sẽ tổng hợp và so sánh toàn diện 8 thuật toán sắp xếp kinh điển (Bubble, Selection, Insertion, Shell, Quick, Heap, Merge, Radix) cùng bảng độ phức tạp Big-O.

---

## 6. 복습 체크리스트 (Checklist ôn tập)

- [ ] Tính đúng công thức số cạnh cực đại: Vô hướng là $n(n-1)/2$, Có hướng là $n(n-1)$.
- [ ] Khẳng định ma trận kề của đồ thị vô hướng luôn là ma trận đối xứng qua đường chéo chính.
- [ ] Tính chuẩn xác: Bậc ra (Out-degree) bằng tổng hàng; Bậc vào (In-degree) bằng tổng cột trong ma trận kề có hướng.
- [ ] Phân biệt khi nào dùng Ma trận kề ($O(n^2)$ - Dense Graph) và Danh sách kề ($O(n+e)$ - Sparse Graph).
- [ ] Ghi nhớ chắc chắn: DFS dùng Stack (hoặc đệ quy), BFS dùng Queue.
- [ ] Nhớ BFS luôn tìm được đường đi ngắn nhất trên đồ thị không trọng số.
- [ ] Định nghĩa Spanning Tree có $n$ đỉnh và đúng $n - 1$ cạnh.
- [ ] Phân biệt thuật toán Kruskal (chọn cạnh nhỏ nhất không tạo chu trình) và Prim (phát triển từ đỉnh).
