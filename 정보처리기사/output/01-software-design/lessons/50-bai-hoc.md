# 7. 자료 구조 (Data Structures)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và sơ đồ phân loại tổng thể các Cấu trúc dữ liệu (`자료 구조 - Data Structures`) trong khoa học máy tính.
- Phân biệt tuyệt đối giữa Cấu trúc tuyến tính (`선형 구조` - quan hệ 1-1) và Cấu trúc phi tuyến tính (`비선형 구조` - quan hệ 1-N hoặc N-N).
- Nhớ chính xác danh mục các cấu trúc thuộc từng nhóm để giải quyết câu hỏi phân loại trong đề thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 자료 구조 (Cấu trúc dữ liệu / Data Structures)
- 선형 구조 (Cấu trúc tuyến tính / Linear: 배열, 연결 리스트, 스택, 큐, 데크)
- 비선형 구조 (Cấu trúc phi tuyến tính / Non-linear: 트리, 그래프)
- 1:1 관계 vs 1:N / N:N 관계 (Quan hệ tương ứng giữa các phần tử)
- 스택 (LIFO), 큐 (FIFO), 데크 (Deque)
- 트리 (Tree / 계층 구조), 그래프 (Graph / 망형 구조)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([6. 분산 데이터베이스 (Distributed Database)](49-bai-hoc.md)):** Sau khi hoàn tất phần cơ sở dữ liệu, bài này bắt đầu cụm kiến thức cấu trúc dữ liệu và giải thuật trong Môn 1.
- **Tiếp nối sang bài sau ([8. 연결 리스트, 스택, 큐, 데크](51-bai-hoc.md)):** Khảo sát chi tiết cơ chế hoạt động, con trỏ và giải thuật Push/Pop của các cấu trúc dữ liệu tuyến tính.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc làu câu thần chú phân loại: Tuyến tính gồm Mảng, Danh sách liên kết, Stack, Queue, Deque; Phi tuyến tính CHỈ CÓ Tree và Graph.
- Đọc TẦNG B để hiểu tại sao việc lựa chọn đúng cấu trúc dữ liệu quyết định trực tiếp đến độ phức tạp thời gian $O(N)$ của thuật toán.

---

## 7. 자료 구조 (Data Structures)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Sơ đồ phân loại tổng thể Cấu trúc dữ liệu:**
  $$\text{자료 구조 (Cấu trúc dữ liệu)} \begin{cases} \mathbf{선형\ 구조 (Tuyến\ tính\ -\ 1:1)} & \begin{cases} \text{배열 (Array)} \\ \text{연결 리스트 (Linked List)} \\ \text{스택 (Stack)} \\ \text{큐 (Queue)} \\ \text{데크 (Deque)} \end{cases} \\ \mathbf{비선형\ 구조 (Phi\ tuyến\ tính\ -\ 1:N,\ N:N)} & \begin{cases} \text{트리 (Tree - Phân cấp)} \\ \text{그래프 (Graph - Mạng lưới)} \end{cases} \end{cases}$$
- **1. 선형 구조 (Linear Data Structures - Cấu trúc dữ liệu tuyến tính):**
  - **Đặc trưng:** Các phần tử dữ liệu được sắp xếp tuần tự nối tiếp nhau, mỗi phần tử chỉ có duy nhất **một phần tử đứng trước và một phần tử đứng sau (quan hệ tương ứng 1-1)**.
  - Các cấu trúc cốt lõi:
    - `배열 (Array - Mảng)`: Bộ nhớ liên tục, kích thước cố định, truy xuất ngẫu nhiên nhanh qua chỉ số index $O(1)$, nhưng chèn/xóa phần tử chậm vì phải dịch chuyển mảng.
    - `연결 리스트 (Linked List - Danh sách liên kết)`: Các nút (Node) lưu rải rác trong bộ nhớ, kết nối với nhau bằng con trỏ (Pointer); chèn/xóa cực nhanh $O(1)$, kích thước động linh hoạt.
    - `스택 (Stack - Ngăn xếp)`: Hoạt động theo nguyên lý **LIFO (Last In First Out - Vào sau ra trước)**; chỉ cho phép thêm (Push) và xóa (Pop) tại một đầu duy nhất (Top).
    - `큐 (Queue - Hàng đợi)`: Hoạt động theo nguyên lý **FIFO (First In First Out - Vào trước ra trước)**; thêm phần tử ở đầu sau (Rear) và xóa phần tử ở đầu trước (Front).
    - `데크 (Deque - Double-Ended Queue)`: Hàng đợi hai đầu, cho phép chèn và xóa phần tử linh hoạt ở **cả hai đầu (cả Front lẫn Rear)**.
- **2. 비선형 구조 (Non-Linear Data Structures - Cấu trúc dữ liệu phi tuyến tính):**
  - **Đặc trưng:** Các phần tử dữ liệu không xếp thành một chuỗi thẳng mà phân nhánh đa chiều phức tạp.
  - Các cấu trúc cốt lõi:
    - `트리 (Tree - Cây)`: Cấu trúc phân cấp hình cây, mỗi nút cha liên kết với nhiều nút con (**quan hệ phân nhánh 1-N**), không có chu trình kín, có một nút gốc duy nhất (Root).
    - `그래프 (Graph - Đồ thị)`: Cấu trúc mạng lưới gồm tập hợp các đỉnh (Vertices) và các cạnh (Edges) kết nối giữa các đỉnh (**quan hệ mạng lưới N-N**), có thể có chu trình, dùng mô hình hóa mạng giao thông, mạng máy tính.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Cấu trúc dữ liệu nào sau đây là cấu trúc phi tuyến tính (비선형 구조)?"* -> Chỉ có **트리 (Tree)** hoặc **그래프 (Graph)**. Các cấu trúc còn lại (Array, Stack, Queue, Deque, Linked List) đều là Tuyến tính (선형).
  - **Bẫy 2:** *"Queue hoạt động theo nguyên lý LIFO?"* -> **Sai**. Queue là **FIFO (First In First Out)**, còn Stack mới là **LIFO (Last In First Out)**.
  - **Bẫy 3:** *"Cấu trúc nào cho phép thêm và xóa ở cả hai đầu?"* -> **데크 (Deque)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Tuyến tính 1-1 gồm Mảng, Link, Stack LIFO, Queue FIFO, Deque hai đầu; Phi tuyến tính gồm Cây phân cấp 1-N và Đồ thị mạng lưới N-N".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bảng so sánh cơ chế lưu trữ: Array vs Linked List:**
  - `배열 (Array)`: Ưu thế khi bài toán cần đọc và tra cứu dữ liệu liên tục theo chỉ số ngẫu nhiên (ví dụ bảng màu, mảng số nguyên), nhưng lãng phí bộ nhớ nếu không dùng hết và tốn chi phí khi phải chèn một phần tử vào giữa.
  - `연결 리스트 (Linked List)`: Ưu thế khi số lượng phần tử biến động liên tục không biết trước và thường xuyên phải chèn/xóa phần tử (chỉ cần đổi con trỏ trỏ sang nút mới), nhưng tốn thêm bộ nhớ để lưu địa chỉ con trỏ của từng nút.

### 복습 체크리스트
- [ ] Phân loại chính xác các cấu trúc dữ liệu thành 선형 구조 hoặc 비선형 구조.
- [ ] Nhớ Stack là LIFO (Vào sau ra trước) và Queue là FIFO (Vào trước ra trước).
- [ ] Định nghĩa Deque là hàng đợi cho phép chèn xóa ở cả hai đầu.
- [ ] Nhớ hai cấu trúc phi tuyến tính duy nhất là Tree (cây) và Graph (đồ thị).
