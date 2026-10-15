# 4. 이진 트리의 운행법 (Binary Tree Traversal)

## 학습 목표 (Mục tiêu)
- Định nghĩa ba phương pháp duyệt cây nhị phân kinh điển: Duyệt tiền thứ tự (Preorder / 전위 순회), Duyệt trung thứ tự (Inorder / 중위 순회) và Duyệt hậu thứ tự (Postorder / 후위 순회).
- Nắm vững quy tắc vị trí của nút gốc (Root) trong từng phương pháp duyệt: Preorder (Gốc ở đầu), Inorder (Gốc ở giữa) và Postorder (Gốc ở cuối).
- Rèn luyện kỹ năng truy vết (Trace) và suy diễn tái dựng cây nhị phân khi biết trước chuỗi kết quả duyệt trong các bài thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 이진 트리 운행법 (Binary Tree Traversal)
- 전위 순회 (Preorder Traversal: Root → Left → Right)
- 중위 순회 (Inorder Traversal: Left → Root → Right)
- 후위 순회 (Postorder Traversal: Left → Right → Root)
- 이진 트리 (Binary Tree - Cây nhị phân)
- 수식 트리 (Expression Tree)

## 선행·연결 개념 (Kiến thức liên kết)
- [05-bai-hoc.md](05-bai-hoc.md): Định nghĩa và các thuật ngữ cơ bản của cấu trúc Cây (Tree).
- [07-bai-hoc.md](07-bai-hoc.md): Các thuật ngữ mở rộng của cấu trúc cây (Parent, Sibling, Tree Degree).
- [12-bai-hoc.md](12-bai-hoc.md): Chuyển đổi biểu thức toán học tương ứng với các phép duyệt cây.

## 읽는 방법 (Cách đọc)
- Nhớ thần chú định vị nút **Gốc (Root)**:
  - **Tiền (Pre):** Gốc đứng **Trước** $\rightarrow$ **Root** $\rightarrow$ Left $\rightarrow$ Right.
  - **Trung (In):** Gốc đứng **Giữa** $\rightarrow$ Left $\rightarrow$ **Root** $\rightarrow$ Right.
  - **Hậu (Post):** Gốc đứng **Sau cùng** $\rightarrow$ Left $\rightarrow$ Right $\rightarrow$ **Root**.
- Hai nhánh con luôn giữ nguyên thứ tự bất biến: **Nhánh Trái (Left) luôn đi trước Nhánh Phải (Right)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Đặc trưng của Cây nhị phân (Binary Tree):**
  - Là cây mà mỗi nút có **tối đa 2 nút con** (차수 $\le 2$), phân biệt rõ thành cây con bên trái (Left Subtree) và cây con bên phải (Right Subtree).
- **Ba phương pháp duyệt cây nhị phân cốt lõi:**

| Phương pháp duyệt | Tên tiếng Hàn & Anh | Thứ tự thăm các nút | Vị trí nút Root |
| :--- | :--- | :--- | :--- |
| **Duyệt tiền thứ tự** | **전위 순회 (Preorder)** | $\mathbf{Root} \rightarrow \text{Left} \rightarrow \text{Right}$ | Đứng đầu tiên |
| **Duyệt trung thứ tự** | **중위 순회 (Inorder)** | $\text{Left} \rightarrow \mathbf{Root} \rightarrow \text{Right}$ | Đứng ở giữa |
| **Duyệt hậu thứ tự** | **후위 순회 (Postorder)** | $\text{Left} \rightarrow \text{Right} \rightarrow \mathbf{Root}$ | Đứng cuối cùng |

- **Ví dụ minh họa tính toán chi tiết:**
  - Xét cây nhị phân mẫu:
    ```
          [A]
         /   \
       [B]   [C]
       / \
     [D] [E]
    ```
    - **Preorder (전위):** Bắt đầu từ Root `A` $\rightarrow$ duyệt cây con trái (`B`, `D`, `E`) $\rightarrow$ duyệt cây con phải (`C`).
      - Kết quả: **A - B - D - E - C**.
    - **Inorder (중위):** Duyệt cây con trái trước (`D`, `B`, `E`) $\rightarrow$ thăm Root `A` $\rightarrow$ duyệt cây con phải (`C`).
      - Kết quả: **D - B - E - A - C**.
    - **Postorder (후위):** Duyệt cây con trái (`D`, `E`, `B`) $\rightarrow$ duyệt cây con phải (`C`) $\rightarrow$ thăm Root `A` sau cùng.
      - Kết quả: **D - E - B - C - A**.

- **Kỹ thuật giải đề thi "Tìm nút Root và tái dựng cây":**
  - Nhìn vào chuỗi **Preorder**: Ký tự đầu tiên luôn là **Root của toàn cây**.
  - Nhìn vào chuỗi **Postorder**: Ký tự cuối cùng luôn là **Root của toàn cây**.
  - Đối chiếu vào chuỗi **Inorder**: Vị trí của Root sẽ chia chuỗi thành 2 nửa: Tất cả các phần tử bên trái Root thuộc về Cây con bên trái; tất cả các phần tử bên phải Root thuộc về Cây con bên phải.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ánh xạ sang biểu thức số học (Expression Tree):**
  - Giả sử cây nhị phân biểu diễn phép toán `+` cho hai toán hạng `A` và `B`:
    - Root là dấu `+`, Left là `A`, Right là `B`.
    - **Preorder:** `+ A B` $\rightarrow$ Biểu thức tiền tố (**Prefix**).
    - **Inorder:** `A + B` $\rightarrow$ Biểu thức trung tố (**Infix** - dạng con người hay đọc).
    - **Postorder:** `A B +` $\rightarrow$ Biểu thức hậu tố (**Postfix** - máy tính dùng Stack để tính).

### 복습 체크리스트
- [ ] Nhớ thứ tự Preorder: Root $\rightarrow$ Left $\rightarrow$ Right (Gốc trước).
- [ ] Nhớ thứ tự Inorder: Left $\rightarrow$ Root $\rightarrow$ Right (Gốc giữa).
- [ ] Nhớ thứ tự Postorder: Left $\rightarrow$ Right $\rightarrow$ Root (Gốc sau cùng).
- [ ] Tìm được ngay nút Root khi nhìn vào kết quả duyệt Preorder (đầu tiên) và Postorder (cuối cùng).
