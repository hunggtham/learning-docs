# 10. 이진 트리의 운행법 (Binary Tree Traversal)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và đặc trưng của Cây nhị phân (`이진 트리 - Binary Tree`): mỗi nút có tối đa không quá 2 nút con (Cây con trái và Cây con phải).
- Thuộc nằm lòng quy tắc và thứ tự duyệt của 3 phép duyệt cây nhị phân kinh điển: Tiền thứ tự (`전위 순회 - Preorder`), Trung thứ tự (`중위 순회 - Inorder`), và Hậu thứ tự (`후위 순회 - Postorder`).
- Thành thạo kỹ năng giải bài tập truy vết thứ tự duyệt cây nhị phân và khôi phục cây từ các chuỗi duyệt trong đề thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 이진 트리 (Cây nhị phân / Binary Tree / 최대 차수 2)
- 트리 운행법 / 순회 (Duyệt cây / Tree Traversal)
- 전위 순회 (Preorder Traversal: Root $\rightarrow$ Left $\rightarrow$ Right)
- 중위 순회 (Inorder Traversal: Left $\rightarrow$ Root $\rightarrow$ Right)
- 후위 순회 (Postorder Traversal: Left $\rightarrow$ Right $\rightarrow$ Root)
- 서브트리 재귀 탐색 (Duyệt đệ quy cây con)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([9. 트리 (Tree) 용어](52-bai-hoc.md)):** Sau khi nắm các thuật ngữ cây (Root, Leaf, Degree), bài này ứng dụng cấu trúc cây nhị phân để thực hiện các giải thuật duyệt dữ liệu có hệ thống.
- **Tiếp nối sang bài sau ([11. 수식의 표기법 (Expression Notation)](54-bai-hoc.md)):** Áp dụng 3 phép duyệt Preorder, Inorder, Postorder này để biểu diễn và tính toán biểu thức tiền tố (Prefix), trung tố (Infix) và hậu tố (Postfix).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ quy tắc vàng: Tên phép duyệt chính là vị trí của Nút gốc Root (Gốc đứng đầu là Pre, Gốc đứng giữa là In, Gốc đứng cuối là Post); nhánh Trái (Left) LUÔN ĐƯỢC DUYỆT TRƯỚC nhánh Phải (Right).
- Đọc TẦNG B để theo dõi bài tập giải chi tiết từng bước trên một cây nhị phân cụ thể.

---

## 10. 이진 트리의 운행법 (Binary Tree Traversal)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Cây nhị phân):**
  - Là cây có cấu trúc đặc biệt mà trong đó **mỗi nút chỉ có tối đa 2 nút con (`모든 노드의 차수가 2 이하`)**, được phân biệt rõ ràng thành Cây con trái (`Left Subtree`) và Cây con phải (`Right Subtree`).
- **3 phép duyệt cây nhị phân kinh điển (이진 트리 3대 순회):**
  - **Quy tắc bất biến:** Nhánh Trái ($L$) luôn được duyệt trước nhánh Phải ($R$). **Vị trí của Nút gốc ($R_0$ / Root) quyết định tên gọi của phép duyệt**:
    1. **전위 순회 (Preorder Traversal - Tiền thứ tự):**
       - Thứ tự: **Root $\rightarrow$ Left $\rightarrow$ Right ($R_0 \rightarrow L \rightarrow R$)**
       - Cơ chế: Ghé thăm Nút gốc trước tiên, sau đó đệ quy duyệt toàn bộ cây con Trái, cuối cùng đệ quy duyệt toàn bộ cây con Phải.
    2. **중위 순회 (Inorder Traversal - Trung thứ tự):**
       - Thứ tự: **Left $\rightarrow$ Root $\rightarrow$ Right ($L \rightarrow R_0 \rightarrow R$)**
       - Cơ chế: Đệ quy duyệt toàn bộ cây con Trái trước, sau đó ghé thăm Nút gốc ở giữa, cuối cùng đệ quy duyệt toàn bộ cây con Phải.
    3. **후위 순회 (Postorder Traversal - Hậu thứ tự):**
       - Thứ tự: **Left $\rightarrow$ Right $\rightarrow$ Root ($L \rightarrow R \rightarrow R_0$)**
       - Cơ chế: Đệ quy duyệt toàn bộ cây con Trái, sau đó đệ quy duyệt toàn bộ cây con Phải, cuối cùng mới ghé thăm Nút gốc ở vị trí sau cùng.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Trong Preorder, nút nào luôn xuất hiện đầu tiên trong chuỗi kết quả?"* -> **Nút gốc của toàn cây (Root Node)**.
  - **Bẫy 2:** *"Trong Postorder, nút nào luôn xuất hiện cuối cùng trong chuỗi kết quả?"* -> **Nút gốc của toàn cây (Root Node)**.
  - **Bẫy 3:** *"Nhánh Phải có bao giờ được duyệt trước nhánh Trái không?"* -> **Không bao giờ**. Luôn luôn là Left trước Right ($L \rightarrow R$).
- **한 문장 설명 (Câu chốt ghi nhớ):** "Preorder Gốc đầu (G-T-P), Inorder Gốc giữa (T-G-P), Postorder Gốc cuối (T-P-G); Trái luôn đi trước Phải".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán mẫu giải chi tiết duyệt cây:**
  - Cho cây nhị phân:
    - Gốc là $A$.
    - Con trái của $A$ là $B$. $B$ có con trái là $D$, con phải là $E$.
    - Con phải của $A$ là $C$. $C$ có con trái là $F$, con phải là $G$.
  - **Thực hiện 3 phép duyệt:**
    - **1. Preorder ($R_0 \rightarrow L \rightarrow R$):**
      - Thăm gốc: $A$
      - Duyệt nhánh trái của $A$ (gốc $B$): $B \rightarrow D \rightarrow E$
      - Duyệt nhánh phải của $A$ (gốc $C$): $C \rightarrow F \rightarrow G$
      - $\Longrightarrow$ Kết quả Preorder: **$\mathbf{A - B - D - E - C - F - G}$**.
    - **2. Inorder ($L \rightarrow R_0 \rightarrow R$):**
      - Nhánh trái của $A$: $D \rightarrow B \rightarrow E$
      - Thăm gốc: $A$
      - Nhánh phải của $A$: $F \rightarrow C \rightarrow G$
      - $\Longrightarrow$ Kết quả Inorder: **$\mathbf{D - B - E - A - F - C - G}$**.
    - **3. Postorder ($L \rightarrow R \rightarrow R_0$):**
      - Nhánh trái của $A$: $D \rightarrow E \rightarrow B$
      - Nhánh phải của $A$: $F \rightarrow G \rightarrow C$
      - Thăm gốc: $A$
      - $\Longrightarrow$ Kết quả Postorder: **$\mathbf{D - E - B - F - G - C - A}$**.

### 복습 체크리스트
- [ ] Định nghĩa cây nhị phân có bậc tối đa bằng 2.
- [ ] Nhớ công thức của 전위 순회 (Preorder): Root -> Left -> Right.
- [ ] Nhớ công thức của 중위 순회 (Inorder): Left -> Root -> Right.
- [ ] Nhớ công thức của 후위 순회 (Postorder): Left -> Right -> Root.
- [ ] Tự tay vẽ cây và giải đúng 3 phép duyệt trong bài toán mẫu.
