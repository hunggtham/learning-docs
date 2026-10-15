# 023 & 024: 자료구조 (Data Structures / Cấu trúc dữ liệu)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của cấu trúc dữ liệu (자료구조 - Data Structure): cách thức tổ chức và lưu trữ dữ liệu hiệu quả trong bộ nhớ máy tính.
- Phân biệt sâu sắc hai nhóm cấu trúc dữ liệu chính: Cấu trúc tuyến tính (선형 구조 - Linear) và Cấu trúc phi tuyến tính (비선형 구조 - Non-linear).
- Nhớ đặc điểm vận hành của từng cấu trúc con: Mảng, Danh sách liên kết, Ngăn xếp (LIFO), Hàng đợi (FIFO), Hàng đợi hai đầu Deque, Cây (Tree - không chu trình) và Đồ thị (Graph).

## 핵심 키워드 (Từ khóa)
- 자료구조 (Data Structure / 선형 vs 비선형)
- 선형 구조 (Linear Structure / 배열, 선형 리스트, 스택, 큐, 데크)
- 비선형 구조 (Non-linear Structure / 트리, 그래프)
- 스택 (Stack / LIFO / 서브루틴 호출, 인터럽트)
- 큐 (Queue / FIFO / 작업 스케줄링, 스풀링)
- 데크 (Deque / Double-ended Queue / Scroll & Shelf)
- 비순환성 (Acyclic / 트리의 무사이클 특성)

## 선행·연결 개념 (Kiến thức liên kết)
- [89-bai-hoc.md](89-bai-hoc.md): Phân loại máy tính theo Flynn và các kỹ thuật xử lý song song.
- [91-bai-hoc.md](91-bai-hoc.md): Kỹ thuật thiết kế thuật toán và độ phức tạp thời gian.
- [01-bai-hoc.md](01-bai-hoc.md): Chi tiết cấu trúc dữ liệu tuyến tính và phi tuyến tính.

## 읽는 방법 (Cách đọc)
- Phân loại nhanh theo quan hệ giữa các phần tử:
  - **선형 구조 (Tuyến tính - Quan hệ 1:1):** Các phần tử sắp xếp nối tiếp nhau thành một hàng. Bao gồm: Mảng (배열), Danh sách liên kết (연결 리스트), Stack, Queue, Deque.
  - **비선형 구조 (Phi tuyến tính - Quan hệ 1:N hoặc N:M):**
    - Quan hệ 1:N phân cấp thứ bậc: **Cây (Tree)** - đặc biệt là **tuyệt đối không có chu trình (No Cycle)**.
    - Quan hệ N:M mạng lưới kết nối: **Đồ thị (Graph)** - bao gồm tập đỉnh (Vertices) và tập cạnh (Edges).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân loại tổng thể cấu trúc dữ liệu:**

| Nhóm cấu trúc | Quan hệ phần tử | Tên cấu trúc dữ liệu cụ thể | Đặc trưng vận hành và ứng dụng |
| :--- | :--- | :--- | :--- |
| **선형 구조 (Linear)** | **1 : 1** (Nối tiếp) | **배열 (Array)** | Các ô nhớ liên tục; truy xuất $O(1)$ qua chỉ số; kích thước cố định |
|  |  | **연결 리스트 (Linked List)** | Các nút nối bằng con trỏ; chèn/xóa linh hoạt; kích thước động |
|  |  | **스택 (Stack)** | Cơ chế **LIFO (Last-In-First-Out)**; gọi hàm con (Subroutine), đệ quy, ngắt |
|  |  | **큐 (Queue)** | Cơ chế **FIFO (First-In-First-Out)**; điều phối tiến trình HĐH, hàng đợi in Spool |
|  |  | **데크 (Deque)** | Chèn và xóa ở **cả hai đầu**; biến thể Scroll (hạn chế nhập) và Shelf (hạn chế xuất) |
| **비선형 구조 (Non-linear)** | **1 : N** (Phân cấp) | **트리 (Tree)** | Cấu trúc phân nhánh từ gốc (Root); **không chứa chu trình khép kín (Cycle)** |
|  | **N : M** (Mạng lưới) | **그래프 (Graph)** | Tập hợp các đỉnh $V$ nối với nhau bằng các cạnh $E$; có hướng hoặc vô hướng |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa Cây và Đồ thị:**
  - Một Cây thực chất là một Đồ thị vô hướng, liên thông và không có chu trình (Connected Acyclic Graph).
  - Với một cây có $n$ đỉnh, số lượng cạnh luôn chính xác bằng $n - 1$. Nếu thêm bất kỳ một cạnh nào vào cây, chu trình sẽ ngay lập tức xuất hiện.

### 복습 체크리스트
- [ ] Phân loại đúng: 선형 (Array, Linked List, Stack, Queue, Deque) vs 비선형 (Tree, Graph).
- [ ] Nhớ Stack là LIFO (Last In First Out), Queue là FIFO (First In First Out).
- [ ] Nhớ Deque cho phép thao tác ở cả 2 đầu.
- [ ] Nhớ tính chất cốt lõi của Tree: Cấu trúc phân cấp và hoàn toàn không có chu trình (No Cycle).
