# 9. 트리 (Tree) 용어

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và hệ thống thuật ngữ cấu trúc Cây (`트리 - Tree`) trong khoa học máy tính: Nút gốc (`루트`), Nút cha/con (`부모/자식`), Nút lá (`단말 노드`), và Nút anh em (`형제 노드`).
- Phân biệt rõ sự khác nhau giữa Bậc của một nút (`노드의 차수`) và Bậc của cả cây (`트리의 차수`).
- Biết cách tính toán chính xác Bậc, Số lượng nút lá, Cấp độ (`레벨 - Level`), và Chiều cao/Độ sâu (`높이/깊이 - Height/Depth`) của một cây cho trước trong đề thi.

## 핵심 키워드 (Từ khóa)
- 트리 (Cây / Tree / 비선형 계층 구조)
- 루트 노드 (Nút gốc / Root Node)
- 단말 노드 / 잎 노드 (Nút lá / Leaf Node / Terminal Node / Degree = 0)
- 형제 노드 (Nút anh em / Sibling Node)
- 노드의 차수 (Bậc của nút / Degree of Node / 자식 노드의 수)
- 트리의 차수 (Bậc của cây / Degree of Tree / 최대 차수)
- 깊이 / 높이 (Độ sâu / Chiều cao / Depth / Height)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([8. 연결 리스트, 스택, 큐, 데크](51-bai-hoc.md)):** Sau khi hoàn thành các cấu trúc tuyến tính, bài này chính thức đi sâu vào cấu trúc phi tuyến tính quan trọng nhất: Cây.
- **Tiếp nối sang bài sau ([10. 이진 트리의 운행법 (Binary Tree Traversal)](53-bai-hoc.md)):** Áp dụng cấu trúc cây nhị phân để thực hiện 3 phép duyệt cây kinh điển: Tiền thứ tự (Preorder), Trung thứ tự (Inorder), và Hậu thứ tự (Postorder).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc định nghĩa các thuật ngữ thi trắc nghiệm: Nút lá là nút có bậc bằng 0; Bậc của cây là Bậc lớn nhất trong tất cả các nút; Chiều cao là Level lớn nhất.
- Đọc TẦNG B để theo dõi bài toán mẫu tính Bậc và Nút lá của một cây thực tế.

---

## 9. 트리 (Tree) 용어

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Hệ thống thuật ngữ cốt lõi của cấu trúc Cây (Tree Terminology):**
  - `노드 (Node - Nút)`: Một phần tử dữ liệu đơn vị độc lập cấu thành nên cây.
  - `근 노드 / 루트 (Root Node - Nút gốc)`: Nút cao nhất đứng ở đỉnh của cây, **không có bất kỳ nút cha nào**. Một cây chỉ có duy nhất một Root.
  - `부모 노드 (Parent Node - Nút cha)`: Nút nằm ở cấp độ ngay phía trên và kết nối trực tiếp đến các nút con bên dưới nó.
  - `자식 노드 (Child Node - Nút con)`: Các nút nằm ở cấp độ ngay phía dưới chịu sự phân nhánh trực tiếp từ nút cha.
  - `형제 노드 (Sibling Node - Nút anh em)`: Các nút con có **cùng chung một nút cha duy nhất**.
  - `단말 노드 / 잎 노드 (Terminal Node / Leaf Node - Nút lá)`:
    - **Nút không có bất kỳ nút con nào (`자식이 하나도 없는 노드`)**.
    - Đặc trưng toán học: **Bậc của nút lá bằng 0 (`차수 = 0`)**.
  - `비단말 노드 (Non-terminal Node / Branch Node - Nút nhánh / Nút trong)`: Nút có ít nhất một nút con (Bậc $\ge 1$).
  - `조상 노드 (Ancestor - Tổ tiên)`: Tất cả các nút nằm trên đường đi từ nút gốc đến nút cha của nút hiện tại.
  - `자손 노드 (Descendant - Hậu duệ)`: Tất cả các nút con, cháu nằm trong toàn bộ cây con phân nhánh bên dưới nút hiện tại.
  - `노드의 차수 (Degree of Node - Bậc của nút)`:
    - **Tổng số lượng nút con trực tiếp** mà nút đó liên kết (`그 노드가 가지고 있는 자식 노드의 개수`).
  - `트리의 차수 (Degree of Tree - Bậc của cây)`:
    - **Giá trị bậc lớn nhất trong số tất cả các nút có trong cây (`노드들의 차수 중 가장 큰 값 / Max Degree`)**.
  - `레벨 (Level - Cấp độ)`: Tầng phân cấp của cây; quy ước Nút gốc (Root) ở Level 1, các nút con của nó ở Level 2, v.v.
  - `높이 / 깊이 (Height / Depth - Chiều cao / Độ sâu của cây)`:
    - **Cấp độ Level lớn nhất của các nút xuất hiện trong cây (`트리가 가질 수 있는 최대 레벨`)**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Nút lá (Terminal Node) có bậc bằng mấy?"* -> **Bằng 0 (차수 = 0)**.
  - **Bẫy 2:** *"Bậc của cây (Degree of Tree) là tổng số nút của cây?"* -> **Sai hoàn toàn**. Bậc của cây là **Bậc lớn nhất trong các nút (최대 차수)**.
  - **Bẫy 3:** *"Các nút nằm cùng một Level thì luôn là nút anh em (Sibling)?"* -> **Sai**. Chỉ khi chúng có **CÙNG MỘT NÚT CHA** thì mới là nút anh em.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Root là đỉnh không cha, Leaf là lá không con bậc 0, Bậc của cây là bậc lớn nhất, Chiều cao là level lớn nhất".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán mẫu trắc nghiệm phân tích cây:**
  - Cho cây có Nút gốc $A$:
    - $A$ có 3 con là $B, C, D$.
    - $B$ có 2 con là $E, F$.
    - $C$ không có con nào.
    - $D$ có 1 con là $G$. Các nút $E, F, G$ không có con.
  - Ta xác định các chỉ số:
    - Bậc của nút $A$: có 3 con $\rightarrow$ Degree($A$) = $3$.
    - Bậc của nút $B$: có 2 con $\rightarrow$ Degree($B$) = $2$.
    - Bậc của nút $C$: Degree($C$) = $0$.
    - **Bậc của cả cây (Degree of Tree)**: $\max(3, 2, 0, 1) = \mathbf{3}$.
    - **Danh sách nút lá (Leaf Nodes)**: $C, E, F, G$ (tổng cộng có **4 nút lá**).
    - **Chiều cao của cây (Height)**: Level 1 ($A$) $\rightarrow$ Level 2 ($B, C, D$) $\rightarrow$ Level 3 ($E, F, G$) $\rightarrow$ Chiều cao = $\mathbf{3}$.

### 복습 체크리스트
- [ ] Phân biệt được Root (nút gốc) và Leaf (nút lá bậc 0).
- [ ] Tính đúng Bậc của một nút (số con trực tiếp) và Bậc của cả cây (max bậc).
- [ ] Xác định đúng Sibling nodes (chung cha).
- [ ] Đếm đúng số nút lá và xác định chiều cao/độ sâu của một cây cho trước.
