# Môn 2 · Bài 03 — Cấu trúc phi tuyến: Cây và duyệt cây nhị phân

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Nếu như [Bài 01](01-cau-truc-du-lieu-tuyen-tinh.md) và [Bài 02](02-ky-phap-bieu-thuc-va-stack.md) tập trung vào các cấu trúc tuyến tính có quan hệ phần tử $1 - 1$, thì bài học này chính thức đưa người học sang nhóm **비선형 구조 (Cấu trúc dữ liệu phi tuyến)** với đại diện phân cấp quan trọng nhất: **Cây (트리 — Tree)** và **Cây nhị phân (이진 트리 — Binary Tree)**. Bài học trang bị toàn bộ hệ thống thuật ngữ đo lường cây, các dạng cây nhị phân đặc thù và ba thuật toán duyệt cây kinh điển luôn có mặt trong đề thi trắc nghiệm.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `05-bai-hoc.md`, `06-bai-hoc.md`, `07-bai-hoc.md`, `08-bai-hoc.md` và `09-bai-hoc.md` (tương ứng với các mục 3, 4, 30, 025, 078 & 079 trong tài liệu chuẩn gốc). Toàn bộ định lý toán học về số cạnh và quy tắc duyệt cây được đối chiếu chuẩn xác với giáo trình khảo thí HRDK.

> **Mạch kiến thức:** Cấu trúc cây giải quyết bài toán mô hình hóa các hệ thống có tính phân cấp cha - con (thư mục tệp tin, cây cú pháp AST, bảng chỉ mục CSDL). Bài học này giải quyết ba vấn đề kỹ thuật cốt lõi: (1) Các thuật ngữ đo lường cây (Degree, Leaf, Depth, Forest) được định nghĩa và tính toán như thế nào? (2) Bốn dạng cây nhị phân đặc thù (Perfect, Complete, Full, Threaded) khác nhau ở điều kiện biên nào? (3) Ba thuật toán duyệt cây (Preorder, Inorder, Postorder) vận hành ra sao và phương pháp tái dựng cây nhị phân từ kết quả duyệt thực hiện như thế nào?

---

## 1. 트리(Tree)의 개념 및 핵심 용어 체계 — Cấu trúc Cây và thuật ngữ

**트리는 정점(Node)과 선분(Branch)을 이용하여 사이클을 이루지 않도록 구성한 계층형 비선형 자료구조이다.**

Về mặt lý thuyết đồ thị toán học, **Cây (Tree)** là một **đồ thị vô hướng, liên thông và không chứa bất kỳ chu trình (Acyclic Connected Graph) nào**. Giữa hai nút bất kỳ trong cây luôn luôn chỉ tồn tại duy nhất một đường đi đơn giản.

### Định lý toán học số cạnh của cây
Nếu một cây có tổng cộng $N$ đỉnh (Nodes / Vertices) thì tổng số nhánh nối (Branches / Edges) luôn luôn bằng đúng:
$$\text{Số cạnh (Edges)} = N - 1$$
*(Ví dụ: Cây có 10 nút thì bắt buộc có đúng 9 cạnh nối).*

---

### Bảng thuật ngữ đo lường cấu trúc Cây chuẩn đề thi

| Thuật ngữ (Hàn / Anh) | Định nghĩa kỹ thuật | Dấu hiệu nhận biết trong đề thi |
| :--- | :--- | :--- |
| **루트 노드 (Root Node)** | Nút đỉnh cao nhất của cây, không có bất kỳ nút cha nào trỏ đến | Cây luôn chỉ có duy nhất 1 Root Node |
| **단말 노드 / 잎 노드 (Terminal / Leaf Node)** | Nút nằm ở đáy tận cùng của nhánh, **không có nút con nào** | **차수 (Degree) = 0** |
| **비단말 노드 (Non-terminal Node)** | Nút trung gian có ít nhất một nút con kết nối bên dưới | Degree $\ge 1$ |
| **자식 / 부모 노드 (Child / Parent Node)** | Nút ở tầng dưới trực tiếp là Child; nút ở tầng trên trực tiếp là Parent | Quan hệ trực tiếp 1 thế hệ |
| **형제 노드 (Sibling Node)** | Các nút có **cùng một nút cha trực tiếp** | Cùng xuất phát từ một nút Parent |
| **조상 / 자손 (Ancestor / Descendant)** | Ancestor là tất cả các nút trên đường đi từ Root đến nút đó; Descendant là tất cả các nút con cháu bên dưới | Quan hệ phả hệ nhiều thế hệ |
| **노드의 차수 (Degree of Node)** | **Số lượng nhánh con trực tiếp** xuất phát từ nút đó | Đếm số lượng con trực tiếp của nút |
| **트리의 차수 (Degree of Tree)** | **Giá trị 차수 lớn nhất** trong số tất cả các nút có trong cây | $\max(\text{Degree của toàn bộ các nút})$ |
| **레벨 (Level)** | Thứ tự tầng bậc của nút (Root thường quy ước ở Level 1) | Đi xuống mỗi thế hệ thì Level tăng 1 |
| **깊이 / 높이 (Depth / Height)** | Mức tầng lớn nhất mà cây đạt được | $\max(\text{Level của các nút trong cây})$ |
| **숲 (Forest)** | Tập hợp của các cây không giao nhau | **Loại bỏ Root Node của cây sẽ thu được một Forest** |

### Ví dụ tính toán minh họa thực tế
Xét một cây có cấu trúc:
- Nút `A` (Root) có 2 con là `B` và `C`.
- Nút `B` có 3 con là `D`, `E`, `F`.
- Nút `C` có 1 con là `G`.
- Các nút `D`, `E`, `F`, `G` không có con.

1. **Độ sâu / Chiều cao (Height):** 3 (Mức 1: `A`, Mức 2: `B, C`, Mức 3: `D, E, F, G`).
2. **Nút lá (Leaf Nodes):** `D`, `E`, `F`, `G` (4 nút có Degree = 0).
3. **Bậc của nút (Degree of Node):** Nút `A` có bậc 2; Nút `B` có bậc 3; Nút `C` có bậc 1.
4. **Bậc của cây (Degree of Tree):** $\max(2, 3, 1, 0) = \mathbf{3}$.
5. **Số cạnh nối:** Có 7 nút $\rightarrow$ Số cạnh = $7 - 1 = \mathbf{6}$ cạnh.

---

## 2. 이진 트리(Binary Tree)의 분류 — Các dạng cây nhị phân đặc thù

**이진 트리는 모든 노드의 차수가 2 이하인 트리로, 각 노드가 왼쪽 자식과 오른쪽 자식을 가질 수 있는 구조이다.**

Cây nhị phân là dạng cây quan trọng nhất trong lập trình thuật toán, trong đó mỗi nút có **tối đa 2 nút con** ($\text{Degree} \le 2$). Nhánh con bên trái (Left Subtree) và nhánh con bên phải (Right Subtree) được phân biệt rõ ràng về mặt vị trí.

### Các dạng cây nhị phân tiêu biểu

```
   [ 포화 이진 트리 ]            [ 완전 이진 트리 ]            [ 편향 이진 트리 ]
         (1)                          (1)                         (1)
        /   \                        /   \                         \
      (2)   (3)                    (2)   (3)                       (2)
      / \   / \                    / \   /                           \
    (4) (5)(6) (7)               (4) (5)(6)                          (3)
 (Đầy kín mọi lá ở đáy)     (Điền tuần tự từ trái sang phải)     (Lệch hẳn 1 bên)
```

1. **포화 이진 트리 (Perfect / Saturated Binary Tree — Cây nhị phân bão hòa):**
   - Tất cả các nút lá đều nằm ở mức đáy cùng (Level cuối cùng) và tất cả các nút nội bộ đều có đủ đúng 2 nút con.
   - Với cây có độ sâu $h$, tổng số nút chính xác tuyệt đối là: $\mathbf{N = 2^h - 1}$.
2. **완전 이진 트리 (Complete Binary Tree — Cây nhị phân hoàn chỉnh):**
   - Cây có độ sâu $h$, các nút từ mức 1 đến mức $h-1$ đều được lấp đầy hoàn toàn.
   - Ở mức cuối cùng $h$, các nút được **điền liên tục tuần tự từ trái sang phải không được có lỗ hổng**.
   - Số nút dao động trong khoảng: $2^{h-1} \le N \le 2^h - 1$.
   - Đây là cấu trúc dữ liệu nền tảng để xây dựng **Heap (힙)** trong thuật toán Heap Sort.
3. **전 이진 트리 (Full / Strictly Binary Tree — Cây nhị phân đầy đủ):**
   - Mọi nút trong cây chỉ có thể có **hoặc là đúng 0 nút con (nút lá), hoặc là đúng 2 nút con**, không bao giờ tồn tại nút có đúng 1 con.
4. **편향 이진 트리 (Skewed Binary Tree — Cây nhị phân lệch):**
   - Cây bị suy biến thành danh sách liên kết, các nút chỉ phát triển lệch hoàn toàn về phía bên trái (Left Skewed) hoặc bên phải (Right Skewed), làm hiệu năng tìm kiếm tụt xuống $O(n)$.
5. **스레드 이진 트리 (Threaded Binary Tree — Cây nhị phân có ren):**
   - Trong cây nhị phân thông thường, có rất nhiều con trỏ `NULL` ở các nút lá gây lãng phí bộ nhớ.
   - Cây Threaded tận dụng các con trỏ `NULL` này để lưu trữ địa chỉ của **Nút tiền nhiệm (Inorder Predecessor)** hoặc **Nút kế nhiệm (Inorder Successor)**, giúp việc duyệt cây theo thứ tự Inorder diễn ra cực nhanh mà **không cần dùng đệ quy hay ngăn xếp (Stack)**.

---

## 3. 이진 트리의 운행법 (Traversal) — Ba phương pháp duyệt cây nhị phân

Duyệt cây (Tree Traversal) là thao tác thăm tất cả các nút trong cây đúng một lần duy nhất theo một thứ tự xác định. Trong cây nhị phân, thứ tự duyệt luôn tuân theo nguyên tắc: **Cây con bên trái (Left) luôn được thăm trước Cây con bên phải (Right)**. Tên gọi của phương pháp được quyết định bởi vị trí mà **Nút gốc (Root)** được thăm:

### Bảng 3 phương pháp duyệt cây nhị phân cốt lõi

| Phương pháp duyệt | Tên tiếng Hàn & Anh | Thứ tự thăm các nút | Vị trí nút Root | Ký pháp tương ứng |
| :--- | :--- | :--- | :--- | :--- |
| **Tiền thứ tự** | **전위 순회 (Preorder)** | $\mathbf{Root} \rightarrow \text{Left} \rightarrow \text{Right}$ | Đứng **đầu tiên** | **Prefix** (Tiền tố) |
| **Trung thứ tự** | **중위 순회 (Inorder)** | $\text{Left} \rightarrow \mathbf{Root} \rightarrow \text{Right}$ | Đứng **ở giữa** | **Infix** (Trung tố) |
| **Hậu thứ tự** | **후위 순회 (Postorder)** | $\text{Left} \rightarrow \text{Right} \rightarrow \mathbf{Root}$ | Đứng **sau cùng** | **Postfix** (Hậu tố) |

### Ví dụ trace duyệt cây thực hành
Xét cây nhị phân sau:
```
          [A]
         /   \
       [B]   [C]
       / \     \
     [D] [E]   [F]
```

1. **Preorder (전위 순회):** Thăm Root trước, sau đó rẽ nhánh.
   - Thăm `A` $\rightarrow$ nhánh trái thăm `B` $\rightarrow$ thăm `D` $\rightarrow$ thăm `E` $\rightarrow$ nhánh phải thăm `C` $\rightarrow$ thăm `F`.
   - Kết quả: **`A - B - D - E - C - F`**
2. **Inorder (중위 순회):** Đi kịch sàn bên trái trước, thăm Root, rồi sang phải.
   - Nhánh trái nhất: `D` $\rightarrow$ thăm Root con `B` $\rightarrow$ thăm `E` $\rightarrow$ thăm Root chính `A` $\rightarrow$ sang nhánh phải: thăm Root con `C` $\rightarrow$ thăm `F`.
   - Kết quả: **`D - B - E - A - C - F`**
3. **Postorder (후위 순회):** Thăm hết con cái hai bên rồi mới thăm đến Root.
   - Cây con trái: `D` $\rightarrow$ `E` $\rightarrow$ `B` $\rightarrow$ Cây con phải: `F` $\rightarrow$ `C` $\rightarrow$ thăm Root chính `A` sau cùng.
   - Kết quả: **`D - E - B - F - C - A`**

---

## 4. Kỹ thuật tái dựng Cây nhị phân từ kết quả duyệt

Trong đề thi Kỹ sư Xử lý Thông tin, dạng bài tập nâng cao thường cho trước 2 chuỗi duyệt (ví dụ: Preorder và Inorder, hoặc Postorder và Inorder) và yêu cầu: *"Xác định kết quả duyệt Postorder của cây"* hoặc *"Tìm nút lá của cây"*.

### Quy tắc suy diễn giải nhanh:
1. **Tìm Nút Gốc (Root):**
   - Ký tự **đầu tiên** trong chuỗi **Preorder** chắc chắn là **Root của toàn cây**.
   - Ký tự **cuối cùng** trong chuỗi **Postorder** chắc chắn là **Root của toàn cây**.
2. **Phân chia Cây con Trái / Phải:**
   - Đem nút Root vừa tìm được soi vào chuỗi **Inorder**:
   - Tất cả các ký tự nằm **bên trái Root** trong Inorder bắt buộc thuộc về **Cây con bên trái (Left Subtree)**.
   - Tất cả các ký tự nằm **bên phải Root** trong Inorder bắt buộc thuộc về **Cây con bên phải (Right Subtree)**.
3. **Lặp lại đệ quy:** Tiếp tục áp dụng quy tắc trên cho các cây con cho đến khi vẽ lại hoàn chỉnh toàn bộ hình dạng cây.

---

## 5. Nối mạch kiến thức sang bài tiếp theo

Từ cấu trúc cây phân cấp (1 - N) không có chu trình, khi nới lỏng điều kiện và cho phép các nút có thể liên kết tự do đa chiều với nhau (N - M) và cho phép tồn tại chu trình khép kín, ta bước sang cấu trúc tổng quát hơn của thế giới đồ thị.

Chúng ta sẽ tiếp tục hành trình cấu trúc phi tuyến với **[Bài 04: Cấu trúc phi tuyến — Đồ thị và biểu diễn đồ thị](04-do-thi-va-bieu-dien-do-thi.md)** để làm chủ công thức tính số cạnh tối đa của đồ thị có hướng/vô hướng, hai phương pháp biểu diễn ma trận kề (Adjacency Matrix) vs danh sách kề (Adjacency List), và hai giải thuật duyệt đồ thị nền tảng BFS, DFS.

---

## 6. 복습 체크리스트 (Checklist ôn tập)

- [ ] Định nghĩa Cây là đồ thị liên thông không có chu trình (사이클 없는 그래프).
- [ ] Nhớ tính chất: Cây có $N$ nút thì luôn có $N - 1$ cạnh nối.
- [ ] Nhớ tính chất 단말 노드 (Leaf Node): Nút không có con, Degree = 0.
- [ ] Tính đúng Bậc của cây (트리의 차수): Lấy giá trị Degree lớn nhất trong cây.
- [ ] Nhớ định nghĩa Forest: Tập hợp các cây con thu được sau khi bỏ đi Root Node.
- [ ] Phân biệt 포화 이진 트리 (Perfect - đầy mọi mức $2^h-1$) và 완전 이진 트리 (Complete - điền tuần tự từ trái sang phải).
- [ ] Hiểu vai trò của 스레드 이진 트리 (Threaded): Dùng con trỏ NULL làm con trỏ duyệt Inorder không cần Stack.
- [ ] Thuộc lòng thứ tự 3 phép duyệt: Preorder (Root-L-R), Inorder (L-Root-R), Postorder (L-R-Root).
- [ ] Tái dựng được hình dạng cây nhị phân khi biết chuỗi Inorder kết hợp với Preorder hoặc Postorder.
