# 3. 트리 (Tree)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác cấu trúc dữ liệu Cây (트리 - Tree) dưới dạng đồ thị liên thông không có chu trình (Acyclic Connected Graph).
- Nắm vững các thuật ngữ nền tảng của cấu trúc cây: Root Node (Nút gốc), Branch (Nhánh), Leaf/Terminal Node (Nút lá), Level (Mức) và Depth (Độ sâu).
- Phân biệt rõ sự khác nhau giữa Bậc của nút (노드의 차수 / Degree of Node) và Bậc của toàn bộ cây (트리의 차수 / Degree of Tree).

## 핵심 키워드 (Từ khóa)
- 트리 (Tree)
- 사이클 없는 그래프 (Acyclic Graph)
- 루트 노드 (Root Node)
- 단말 노드 (Terminal Node / Leaf Node)
- 차수 / 디그리 (Degree)
- 트리의 차수 (Degree of Tree)
- 레벨 (Level) & 깊이 / 높이 (Depth / Height)

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Phân loại cấu trúc dữ liệu phi tuyến (Non-linear Structure).
- [06-bai-hoc.md](06-bai-hoc.md): Các phương pháp duyệt cây nhị phân (Preorder, Inorder, Postorder).
- [07-bai-hoc.md](07-bai-hoc.md): Các thuật ngữ mở rộng về mối quan hệ phân cấp trong cây (Parent, Child, Sibling).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh từ khóa trong đề thi trắc nghiệm:
  - Cứ thấy **"Nút không có con" (자식이 없는 노드)** hoặc **"Degree = 0"** $\rightarrow$ Chọn ngay **단말 노드 (Leaf Node / Terminal Node)**.
  - Cứ thấy **"Bậc của cây" (트리의 차수)** $\rightarrow$ Tìm nút có số con nhiều nhất, lấy số con đó làm đáp án.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Cây (Tree):**
  - Là cấu trúc dữ liệu phi tuyến (Non-linear) biểu diễn mối quan hệ phân cấp cha - con (Hierarchical) theo cấu trúc 1 - N.
  - Về mặt toán học đồ thị: Cây là một **đồ thị vô hướng, liên thông và không chứa bất kỳ chu trình (Cycle) nào**.
- **Bảng thuật ngữ cốt lõi của cấu trúc Cây:**

| Thuật ngữ (Hàn / Anh) | Định nghĩa kỹ thuật | Đặc điểm nhận diện đề thi |
| :--- | :--- | :--- |
| **루트 노드 (Root Node)** | Nút đỉnh cao nhất của cây, không có bất kỳ nút cha nào trỏ đến | Cây luôn chỉ có duy nhất 1 Root node |
| **단말 노드 / 잎 노드 (Terminal / Leaf Node)** | Nút nằm ở đáy tận cùng của nhánh, **không có nút con nào** | **Degree (차수) = 0** |
| **비단말 노드 (Non-terminal Node)** | Nút trung gian có ít nhất một nút con kết nối bên dưới | Degree $\ge 1$ |
| **노드의 차수 (Degree of Node)** | Số lượng nhánh con trực tiếp xuất phát từ nút đó | Đếm số con trực tiếp của nút |
| **트리의 차수 (Degree of Tree)** | **Giá trị 차수 lớn nhất** trong số tất cả các nút có trong cây | $\max(\text{Degree của tất cả các nút})$ |
| **레벨 (Level)** | Thứ tự tầng bậc của nút, tính từ gốc (Root thường ở Level 1) | Đi xuống mỗi thế hệ con thì Level tăng thêm 1 |
| **깊이 / 높이 (Depth / Height)** | Mức tầng lớn nhất mà cây đạt được | $\max(\text{Level của các nút trong cây})$ |

- **Ví dụ tính toán minh họa kinh điển:**
  - Giả sử một cây có: Nút `A` (Root) đẻ ra 2 con `B` và `C`. Nút `B` đẻ ra 3 con `D`, `E`, `F`. Nút `C` đẻ ra 1 con `G`.
    - Nút `A` có Degree = 2.
    - Nút `B` có Degree = 3.
    - Nút `C` có Degree = 1.
    - Các nút `D`, `E`, `F`, `G` không có con $\rightarrow$ Degree = 0 $\rightarrow$ Là các **단말 노드 (Leaf Nodes)**.
    - **트리의 차수 (Degree của cây):** Là $\max(2, 3, 1, 0) = \mathbf{3}$.
    - **Số lượng 단말 노드 (Leaf nodes):** 4 nút (`D`, `E`, `F`, `G`).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính chất toán học của Cây tự do (Free Tree):**
  - Nếu một cây có tổng cộng $N$ đỉnh (Nodes) thì số cạnh (Branches / Edges) nối giữa các đỉnh luôn luôn bằng đúng:
    $$\text{Số cạnh (Edges)} = N - 1$$
  - Giữa 2 nút bất kỳ trong cây chỉ tồn tại duy nhất một đường đi đơn giản (Simple path).
- **Ứng dụng thực tế trong hệ thống thông tin:**
  - Quản lý hệ thống tập tin và thư mục (Directory Tree).
  - Cấu trúc chỉ mục trong cơ sở dữ liệu: B-Tree, B+ Tree.
  - Phân tích cú pháp trong trình biên dịch: Abstract Syntax Tree (AST).

### 복습 체크리스트
- [ ] Định nghĩa cây là đồ thị không có chu trình (사이클이 없는 그래프).
- [ ] Nhớ tính chất 단말 노드 (Leaf Node): Nút không có con, Degree = 0.
- [ ] Tính đúng Bậc của cây (트리의 차수): Lấy giá trị Degree lớn nhất trong cây.
- [ ] Khẳng định định lý số cạnh: Cây có $N$ nút thì luôn có $N - 1$ cạnh.
