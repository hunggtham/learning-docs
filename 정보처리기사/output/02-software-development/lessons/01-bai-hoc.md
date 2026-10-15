# 1. 자료 구조의 분류 (Classification of Data Structures)

## 학습 목표 (Mục tiêu)
- Phân biệt rành mạch hai nhóm cấu trúc dữ liệu căn bản trong khoa học máy tính: Cấu trúc tuyến tính (선형 구조 - Linear Structure) và Cấu trúc phi tuyến (비선형 구조 - Non-linear Structure).
- Nắm vững công thức tính số cạnh tối đa (최대 간선 수) cho Đồ thị vô hướng (무방향 그래프) và Đồ thị có hướng (방향 그래프) với số đỉnh $n$.
- Nằm lòng các thuật toán và cấu trúc thuộc từng phân nhóm để giải quyết nhanh các câu hỏi phân loại trong kỳ thi Kỹ sư xử lý thông tin.

## 핵심 키워드 (Từ khóa)
- 자료 구조 (Data Structure)
- 선형 구조 (Linear Structure)
- 비선형 구조 (Non-linear Structure)
- 배열 (Array) & 선형 리스트 (Linear List)
- 스택 (Stack) & 큐 (Queue) & 데크 (Deque)
- 트리 (Tree) & 그래프 (Graph)
- 무방향 그래프 최대 간선 수: $n(n-1)/2$
- 방향 그래프 최대 간선 수: $n(n-1)$

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): 스택 (Stack) và các ứng dụng điển hình (LIFO).
- [03-bai-hoc.md](03-bai-hoc.md): So sánh tổng hợp Stack, Queue, Deque.
- [05-bai-hoc.md](05-bai-hoc.md): Cấu trúc cây phi tuyến (Tree) và duyệt cây nhị phân.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng phân loại 2 cột Tuyến tính vs Phi tuyến. Đi thi trắc nghiệm cứ hỏi "Cấu trúc nào sau đây là phi tuyến?" thì chỉ có 2 ứng viên: **트리 (Tree)** hoặc **그래프 (Graph)**.
- Ghi nhớ ngay công thức tính số cạnh đồ thị: Vô hướng thì chia 2 ($\frac{n(n-1)}{2}$), có hướng thì giữ nguyên ($n(n-1)$).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân loại cấu trúc dữ liệu toàn diện:**

| Phân loại | Tên tiếng Hàn & Anh | Các cấu trúc tiêu biểu | Mối quan hệ giữa các phần tử |
| :--- | :--- | :--- | :--- |
| **선형 구조 (Linear)** | Tuyến tính | **배열 (Array)**, **선형 리스트 (Linear List)** (Gồm 연속 리스트 & 연결 리스트), **스택 (Stack)**, **큐 (Queue)**, **데크 (Deque)** | Quan hệ 1 - 1 (Mỗi phần tử chỉ có tối đa 1 phần tử đứng trước và 1 phần tử đứng sau) |
| **비선형 구조 (Non-linear)** | Phi tuyến | **트리 (Tree)**, **그래프 (Graph)** | Quan hệ 1 - N (Phân nhánh cây) hoặc N - M (Mạng lưới đồ thị) |

- **Công thức tính số cạnh cực đại của Đồ thị (Graph Edges Calculation):**
  - Giả sử đồ thị có $n$ đỉnh (Nodes / Vertices):
    - **무방향 그래프 (Đồ thị vô hướng):**
      $$\text{Số cạnh tối đa} = \frac{n(n - 1)}{2}$$
      *(Vì mỗi cạnh nối 2 đỉnh bất kỳ không phân biệt thứ tự chiều)*
    - **방향 그래프 (Đồ thị có hướng):**
      $$\text{Số cạnh tối đa} = n(n - 1)$$
      *(Vì giữa 2 đỉnh bất kỳ có thể tồn tại 2 cung có hướng ngược nhau: $u \rightarrow v$ và $v \rightarrow u$)*
  - **Ví dụ tính toán nhanh đi thi:**
    - Cho đồ thị có $n = 5$ đỉnh:
      - Nếu là vô hướng: $\frac{5 \times 4}{2} = 10$ cạnh.
      - Nếu là có hướng: $5 \times 4 = 20$ cạnh.

- **Dạng câu hỏi bẫy trắc nghiệm:**
  - **Bẫy 1:** *"Cấu trúc nào sau đây KHÔNG PHẢI là cấu trúc phi tuyến?"* $\rightarrow$ Các đáp án đưa ra Tree, Graph, Stack $\rightarrow$ Chọn **스택 (Stack)** (vì Stack là tuyến tính).
  - **Bẫy 2:** *"Đồ thị vô hướng có 4 đỉnh thì số cạnh tối đa là bao nhiêu?"* $\rightarrow$ Áp dụng $\frac{4 \times 3}{2} = 6$ cạnh.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Khái niệm mở rộng về Danh sách tuyến tính:**
  - **연속 리스트 (Contiguous List / Array List):** Các phần tử được lưu trữ tại các ô nhớ vật lý liên tiếp nhau. Truy cập ngẫu nhiên qua chỉ số cực nhanh $O(1)$, nhưng chèn/xóa tốn kém $O(n)$ do phải dịch chuyển dữ liệu.
  - **연결 리스트 (Linked List):** Các phần tử (Node) liên kết với nhau bằng con trỏ địa chỉ (Pointer / Link). Chèn/xóa linh hoạt $O(1)$ khi đã có con trỏ, nhưng truy cập ngẫu nhiên chậm $O(n)$ và tốn thêm bộ nhớ lưu con trỏ.
- **Biểu diễn đồ thị:**
  - Đồ thị thường được lưu trữ bằng **인접 행렬 (Adjacency Matrix)** hoặc **인접 리스트 (Adjacency List)** trong lập trình giải thuật.

### 복습 체크리스트
- [ ] Phân loại chính xác 5 cấu trúc tuyến tính: Mảng, Danh sách liên kết, Stack, Queue, Deque.
- [ ] Nhớ 2 cấu trúc phi tuyến duy nhất: Cây (Tree) và Đồ thị (Graph).
- [ ] Viết đúng công thức số cạnh cực đại: Vô hướng là $n(n-1)/2$, Có hướng là $n(n-1)$.
- [ ] Tính nhẩm chuẩn xác số cạnh khi đề bài cho số đỉnh $n = 4, 5, 6$.
