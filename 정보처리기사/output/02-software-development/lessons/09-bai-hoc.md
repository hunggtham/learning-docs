# 078 & 079: 트리 및 운행법 (Tree & Tree Traversal)

## 078 & 079: 트리 및 운행법 (Tree & Tree Traversal)

### 트리 (Tree - Cây)
Phần “트리 (Tree - Cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **사이클(Cycle)이 없는 그래프.** (Đồ thị không có vòng lặp / chu trình).
- **단말 노드 (Leaf Node):** Nút lá (Không có con / Degree = 0).
- **차수 (Degree):** Số nút con của một nút.
- **트리의 차수 (Tree's Degree):** Degree lớn nhất trong toàn bộ cây.
- **깊이 (Depth):** Số tầng (Level) tối đa của cây.

### 트리의 운행법 (Tree Traversal - Duyệt cây)
Phần “트리의 운행법 (Tree Traversal - Duyệt cây)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Theo vị trí của **Root (Gốc)**:
  - **Preorder (전위):** **Root** -> Left -> Right.
  - **Inorder (중위):** Left -> **Root** -> Right.
  - **Postorder (후위):** Left -> Right -> **Root**.

- **Ví dụ (Example):** Cây có Gốc A, Trái B, Phải C. Pre = ABC, In = BAC, Post = BCA.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Pre (Trước) = Root đi đầu. In (Giữa) = Root ở giữa. Post (Sau) = Root đi chót.

---
