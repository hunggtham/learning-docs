# 30. 트리 구조 추가 용어 (Tree Terminology Additional)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống thuật ngữ quan hệ gia phả trong cấu trúc Cây: Nút cha (부모 노드), Nút con (자식 노드), Nút anh em (형제 노드), Nút tổ tiên (조상 노드) và Nút hậu duệ (후손 노드).
- Định nghĩa chính xác khái niệm Rừng (포레스트 - Forest) và mối quan hệ biến đổi giữa Cây và Rừng khi loại bỏ nút gốc.
- Hiểu sâu các chỉ số đo lường hình học của cây: Bậc của cây (Degree of Tree), Bán kính, Đường kính và Cấp bậc phân tầng để phân tích cấu trúc dữ liệu tối ưu.

## 핵심 키워드 (Từ khóa)
- 부모 노드 (Parent Node)
- 자식 노드 (Child / Son Node)
- 형제 노드 (Sibling Node)
- 조상 노드 (Ancestor Node) & 후손 노드 (Descendant Node)
- 트리의 차수 (Degree of Tree)
- 포레스트 (Forest - Rừng)
- 서브트리 (Subtree - Cây con)

## 선행·연결 개념 (Kiến thức liên kết)
- [05-bai-hoc.md](05-bai-hoc.md): Định nghĩa nền tảng của Cây và nút lá (Leaf node).
- [06-bai-hoc.md](06-bai-hoc.md): Duyệt cây nhị phân (Preorder, Inorder, Postorder).
- [08-bai-hoc.md](08-bai-hoc.md): Tổng hợp toàn diện thuật ngữ và các bài toán tính bậc của cây.

## 읽는 방법 (Cách đọc)
- Liên tưởng trực quan đến quan hệ gia đình trong cây gia phả:
  - Cùng cha $\rightarrow$ **형제 노드 (Sibling)**.
  - Nút nằm ở tầng trên trực tiếp $\rightarrow$ **부모 노드 (Parent)**.
  - Bỏ nút Root của cây $\rightarrow$ Tạo ra **Forest (숲 - Tập hợp các cây con độc lập)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng thuật ngữ quan hệ gia phả trong Cây:**

| Thuật ngữ (Hàn / Anh) | Định nghĩa kỹ thuật | Mẹo nhận biết đề thi |
| :--- | :--- | :--- |
| **부모 노드 (Parent Node)** | Nút ở cấp bậc ngay phía trên ($Level - 1$) có cạnh trực tiếp nối xuống nút hiện tại | Mỗi nút (trừ Root) đều có **duy nhất 1 nút cha** |
| **자식 노드 (Child / Son Node)** | Các nút ở cấp bậc ngay phía dưới ($Level + 1$) được nối từ nút hiện tại | Một nút có thể có 0, 1 hoặc nhiều nút con |
| **형제 노드 (Sibling Node)** | **Các nút có chung một nút cha duy nhất (동일한 부모 노드)** | Nằm cùng cấp bậc và cùng xuất phát từ một nút cha |
| **조상 노드 (Ancestor Node)** | Tập hợp tất cả các nút nằm trên đường đi từ nút gốc (Root) đến nút cha của nút hiện tại | Bao gồm cha, ông, cố... ngược lên tận Root |
| **후손 노드 (Descendant Node)** | Tập hợp tất cả các nút nằm trong các cây con bên dưới nút hiện tại | Bao gồm con, cháu, chắt... đi xuống tận nút lá |
| **포레스트 (Forest / 숲)** | Tập hợp của **hai hay nhiều cây độc lập rời rạc** | Nếu cắt bỏ nút Root của một cây, các cây con bên dưới sẽ tạo thành một Forest |

- **Các công thức và quy tắc nhận diện:**
  - **트리의 차수 (Degree of Tree):**
    $$\text{Degree của cây} = \max(\text{Degree của tất cả các nút})$$
    *(Nếu tất cả các nút trong cây chỉ có tối đa 2 con, thì Degree của cây là 2 - tức cây nhị phân).*
  - **Mối quan hệ Cây $\leftrightarrow$ Rừng:**
    $$\text{Cây (Tree)} - \text{Root} = \text{Rừng (Forest)}$$

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Thuật toán chuyển đổi Rừng thành Cây nhị phân (Forest to Binary Tree):**
  - Trong cấu trúc dữ liệu kinh điển, một Forest có thể chuyển đổi thành một cây nhị phân duy nhất bằng quy tắc **Left-Child Right-Sibling (LCRS)**:
    - Nhánh con bên trái (Left branch): Trỏ đến đứa con đầu tiên (First child).
    - Nhánh con bên phải (Right branch): Trỏ đến người anh em ruột kế tiếp (Next sibling).
  - Kỹ thuật này giúp lưu trữ cây đa phân (Multi-way Tree) bằng cấu trúc dữ liệu con trỏ nhị phân cố định 2 nhánh, tiết kiệm bộ nhớ.

### 복습 체크리스트
- [ ] Định nghĩa chính xác 형제 노드 (Sibling Node): Các nút có chung một cha.
- [ ] Phân biệt 조상 노드 (Ngược lên Root) và 후손 노드 (Xuống tận lá).
- [ ] Nhớ nguyên lý tạo Forest: Cắt bỏ nút Root sẽ biến các cây con thành một Forest.
- [ ] Tính nhẩm Degree của cây bằng cách tìm bậc lớn nhất của các nút thành phần.
