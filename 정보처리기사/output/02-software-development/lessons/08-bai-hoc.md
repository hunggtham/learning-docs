# 025: 트리 (Tree / Cây)

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện các chỉ số cấu trúc định lượng của Cây: Nút gốc, Nút lá, Bậc của nút, Bậc của cây, Cấp độ và Độ sâu.
- Nắm vững quy trình duyệt cây nhị phân (Preorder, Inorder, Postorder) và giải quyết chính xác các câu hỏi tính toán giải thuật trong kỳ thi Kỹ sư xử lý thông tin.
- Rèn luyện kỹ năng phân tích cây biểu thức toán học và chuyển đổi qua lại giữa các dạng biểu thức tiền tố, trung tố và hậu tố.

## 핵심 키워드 (Từ khóa)
- 루트 노드 (Root Node)
- 단말 노드 (Leaf Node)
- 차수 (Degree of Node & Tree)
- 레벨 (Level) & 깊이 (Depth)
- 전위 순회 (Preorder)
- 중위 순회 (Inorder)
- 후위 순회 (Postorder)

## 선행·연결 개념 (Kiến thức liên kết)
- [06-bai-hoc.md](06-bai-hoc.md): Quy tắc duyệt cây nhị phân (Preorder, Inorder, Postorder).
- [07-bai-hoc.md](07-bai-hoc.md): Thuật ngữ quan hệ trong cây (Parent, Sibling, Forest).
- [09-bai-hoc.md](09-bai-hoc.md): Luyện tập giải đề thi thực chiến về duyệt cây và tính bậc.

## 읽는 방법 (Cách đọc)
- Ôn tập bảng tra cứu nhanh các chỉ số hình học của cây (Level, Depth, Degree).
- Đọc kỹ phần ví dụ tính toán mẫu ở TẦNG A để nắm chắc phương pháp đếm nút lá (Leaf) và xác định bậc tối đa của cây (Max Degree).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp chỉ số cấu trúc cây:**

| Chỉ số / Khái niệm | Định nghĩa kỹ thuật | Cách tính nhanh khi làm bài thi |
| :--- | :--- | :--- |
| **루트 노드 (Root)** | Đỉnh cao nhất của cây | Nút không có mũi tên đâm vào (Cha = null) |
| **단말 노드 (Leaf)** | Nút ở đáy, không có con | Đếm các nút có số nhánh con $= 0$ |
| **차수 (Degree of Node)** | Số lượng con trực tiếp của nút | Đếm số nhánh rẽ ngay dưới nút đó |
| **트리의 차수 (Degree of Tree)** | Bậc lớn nhất trong tất cả các nút | Tìm $\max(\text{Số con của từng nút})$ |
| **깊이 (Depth / Height)** | Tầng sâu nhất của cây | Đếm số tầng từ Root (Level 1) xuống nút sâu nhất |

- **Quy tắc duyệt cây nhị phân theo vị trí Root:**
  - **Preorder (전위):** $\mathbf{Root} \rightarrow \text{Left} \rightarrow \text{Right}$ (Root đứng trước).
  - **Inorder (중위):** $\text{Left} \rightarrow \mathbf{Root} \rightarrow \text{Right}$ (Root đứng giữa).
  - **Postorder (후위):** $\text{Left} \rightarrow \text{Right} \rightarrow \mathbf{Root}$ (Root đứng sau cùng).

- **Ví dụ phân tích cây toàn diện:**
  - Cho cây có cấu trúc:
    - Root `A` có 2 con: `B` và `C`.
    - `B` có 2 con: `D` và `E`.
    - `C` có 1 con: `F`.
    - `E` có 2 con: `G` và `H`.
  - **Phân tích chỉ số:**
    - Nút `A`: Degree = 2.
    - Nút `B`: Degree = 2.
    - Nút `C`: Degree = 1.
    - Nút `E`: Degree = 2.
    - Các nút `D`, `F`, `G`, `H`: Không có con $\rightarrow$ Degree = 0 $\rightarrow$ Có **4 단말 노드 (Leaf Nodes)**.
    - **트리의 차수 (Degree của cây):** $\max(2, 2, 1, 2, 0) = \mathbf{2}$ (Đây là cây nhị phân).
    - **깊이 (Độ sâu / Height):** Root `A` (Level 1) $\rightarrow$ `B`, `C` (Level 2) $\rightarrow$ `D`, `E`, `F` (Level 3) $\rightarrow$ `G`, `H` (Level 4) $\rightarrow$ **Depth = 4**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Công thức tính số nút tối đa của cây nhị phân:**
  - Tại một mức $\text{Level } i$: Số nút tối đa là $2^{i - 1}$ (với Root ở Level 1).
  - Cây nhị phân có độ sâu $h$:
    $$\text{Số nút tối đa} = 2^h - 1$$
    *(Ví dụ cây nhị phân đầy đủ có độ sâu $h = 4$ sẽ có tối đa $2^4 - 1 = 15$ nút).*
- **Mối quan hệ giữa Nút lá ($n_0$) và Nút có 2 con ($n_2$):**
  - Trong bất kỳ cây nhị phân nào:
    $$n_0 = n_2 + 1$$
    *(Số lượng nút lá luôn nhiều hơn số lượng nút có 2 con đúng 1 nút).*

### 복습 체크리스트
- [ ] Xác định chính xác Root, Leaf, Degree of Node và Degree of Tree trên một cây bất kỳ.
- [ ] Tính đúng độ sâu Depth bằng cách đếm số tầng từ Root xuống nút sâu nhất.
- [ ] Áp dụng công thức $n_0 = n_2 + 1$ để tính nhanh số nút lá trong cây nhị phân.
- [ ] Thực hiện thuần thục 3 phép duyệt Preorder, Inorder và Postorder.
