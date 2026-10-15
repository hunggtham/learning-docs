# 078 & 079: 트리 및 운행법 (Tree & Tree Traversal)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất toán học của cấu trúc Cây dưới dạng đồ thị liên thông không chu trình (사이클이 없는 그래프).
- Thuần thục ba giải thuật duyệt cây nhị phân (Preorder, Inorder, Postorder) và phương pháp xác định thứ tự thăm nút cho các bài toán phức tạp có nhiều nhánh con.
- Luyện tập kỹ năng chuyển đổi từ sơ đồ cây sang chuỗi duyệt và ngược lại từ hai chuỗi duyệt tái tạo cây nhị phân ban đầu.

## 핵심 키워드 (Từ khóa)
- 사이클 없는 그래프 (Acyclic Connected Graph)
- 이진 트리 순회 (Binary Tree Traversal)
- 전위 운행 (Preorder: Root → Left → Right)
- 중위 운행 (Inorder: Left → Root → Right)
- 후위 운행 (Postorder: Left → Right → Root)
- 이진 탐색 트리 (Binary Search Tree - BST)

## 선행·연결 개념 (Kiến thức liên kết)
- [06-bai-hoc.md](06-bai-hoc.md): Nguyên lý cơ bản của duyệt cây nhị phân.
- [08-bai-hoc.md](08-bai-hoc.md): Tổng hợp cấu trúc cây và các chỉ số hình học.
- [10-bai-hoc.md](10-bai-hoc.md): Cấu trúc đồ thị (Graph) và các thuật toán tìm kiếm DFS / BFS.

## 읽는 방법 (Cách đọc)
- Nhớ kỹ quy tắc 3 bước duyệt đệ quy:
  - Khi duyệt nhánh con, áp dụng đúng trật tự đệ quy cho từng cây con (Subtree) nhỏ hơn trước khi quay lên nhánh cha.
  - Luôn nhớ: Nhánh trái (Left) luôn luôn được duyệt xong trước nhánh phải (Right).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Đặc điểm cấu trúc của Cây:**
  - **Đồ thị không có chu trình (사이클이 없는 그래프):** Bất kỳ chu trình khép kín nào xuất hiện cũng khiến đồ thị không còn là cây.
  - **Số cạnh cố định:** Với $N$ nút, luôn có đúng $N - 1$ cạnh.
- **Quy tắc duyệt cây nhị phân 3 phương thức:**

| Phương pháp duyệt | Ký hiệu | Trật tự đệ quy | Gốc (Root) ở vị trí nào? |
| :--- | :--- | :--- | :--- |
| **전위 순회 (Preorder)** | NLR | $\mathbf{N} \rightarrow \mathbf{L} \rightarrow \mathbf{R}$ | **Đầu tiên** trong chuỗi kết quả |
| **중위 순회 (Inorder)** | LNR | $\mathbf{L} \rightarrow \mathbf{N} \rightarrow \mathbf{R}$ | **Nằm giữa** cây con trái và phải |
| **후위 순회 (Postorder)** | LRN | $\mathbf{L} \rightarrow \mathbf{R} \rightarrow \mathbf{N}$ | **Cuối cùng** trong chuỗi kết quả |

*(Ghi chú: N = Node/Root, L = Left subtree, R = Right subtree)*

- **Bài toán mẫu thực chiến thi trắc nghiệm:**
  - Cho cây nhị phân như hình dưới:
    ```
            [+]
           /   \
         [*]   [E]
        /   \
      [A]   [B]
    ```
    - **Preorder:** `+ * A B E` (Dấu `+` đứng đầu).
    - **Inorder:** `A * B + E` (Dấu `+` nằm giữa cụm `A * B` và `E`).
    - **Postorder:** `A B * E +` (Dấu `+` đứng sau cùng).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính chất đặc biệt của Cây nhị phân tìm kiếm (Binary Search Tree - BST):**
  - Trong một cây BST (Cây con trái nhỏ hơn nút gốc, cây con phải lớn hơn nút gốc):
    - Khi áp dụng phép duyệt **Inorder (중위 순회)** trên cây BST, kết quả thu được sẽ là một **dãy số tăng dần có thứ tự hoàn hảo (Sorted Ascending Sequence)**.
    - Đây là cơ sở của giải thuật sắp xếp Tree Sort.

### 복습 체크리스트
- [ ] Khẳng định cây là đồ thị liên thông không có chu trình.
- [ ] Nhớ mã ký hiệu NLR (Preorder), LNR (Inorder), LRN (Postorder).
- [ ] Nhận diện được đặc tính: Duyệt Inorder trên BST cho kết quả tăng dần có thứ tự.
- [ ] Chuyển đổi chính xác cây toán học thành biểu thức Prefix, Infix, Postfix.
