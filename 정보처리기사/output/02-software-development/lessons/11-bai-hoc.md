# 077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)

## 077: 그래프 및 인접 행렬 (Graphs & Adjacency Matrix)

### 최대 간선 수 (Số Cạnh Tối Đa)
Phần “최대 간선 수 (Số Cạnh Tối Đa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **무방향 그래프 (Vô hướng):** `n(n-1)/2`.
- **방향 그래프 (Có hướng):** `n(n-1)`. (Gấp đôi vô hướng).
*(n là số đỉnh / Vertex)*

### 인접 행렬 (Adjacency Matrix - Ma trận kề)
Phần “인접 행렬 (Adjacency Matrix - Ma trận kề)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Biểu diễn đồ thị bằng ma trận `N x N`. (Có đường đi = 1, Không có = 0).
- **방향 그래프:** Không đối xứng. Hàng (Row) là đi Ra (Out), Cột (Column) là đi Vào (In).
- **무방향 그래프:** Đối xứng qua đường chéo (Symmetric).

- **Vietnamese Explanation:** Nếu đồ thị ít cạnh (thưa) thì dùng Ma trận kề sẽ rất tốn RAM vì toàn số 0. Số cạnh của Đồ thị vô hướng luôn bằng một nửa Đồ thị có hướng vì cạnh A-B và B-A được tính là 1.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Vô hướng / 2 (Vì không phân biệt đi/về). Ma trận vô hướng = Đối xứng.

---
