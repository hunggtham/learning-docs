# 8. 연결 리스트, 스택, 큐, 데크 (Data Structure Types)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế con trỏ của 3 loại Danh sách liên kết: Danh sách liên kết đơn (`단일 연결 리스트`), Danh sách liên kết đôi (`이중 연결 리스트`), và Danh sách liên kết vòng (`원형 연결 리스트`).
- Thuộc nằm lòng các thao tác cơ bản và ứng dụng thực tiễn của `Stack` (LIFO / Đệ quy, Undo) và `Queue` (FIFO / Hàng đợi in ấn, BFS).
- Phân biệt hai biến thể hạn chế của hàng đợi hai đầu Deque: Hạn chế đầu vào (`Scroll`) và Hạn chế đầu ra (`Shelf`).

## 핵심 키워드 (Từ khóa)
- 단일·이중·원형 연결 리스트 (Singly, Doubly, Circular Linked List)
- 스택 (Stack / LIFO / Top / Push / Pop)
- 오버플로 / 언더플로 (Overflow / Underflow)
- 큐 (Queue / FIFO / Front / Rear)
- 데크 (Deque / Scroll - 입력을 제한, Shelf - 출력을 제한)
- 스택의 응용 (Recursion, Undo, DFS)
- 큐의 응용 (Spooling, CPU Scheduling, BFS)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([7. 자료 구조 (Data Structures)](50-bai-hoc.md)):** Sau khi phân loại tổng quan cấu trúc tuyến tính, bài này phân tích sâu vào các thao tác thuật toán và con trỏ điều khiển của từng cấu trúc cụ thể.
- **Tiếp nối sang bài sau ([9. 트리 (Tree) 용어](52-bai-hoc.md)):** Chuyển từ cấu trúc tuyến tính sang cấu trúc phi tuyến tính với các thuật ngữ chuyên sâu về Cây (Tree).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ các ứng dụng kinh điển của Stack (đệ quy, hoàn tác Undo) vs Queue (hàng đợi in, lập lịch CPU) và phân biệt Scroll (cấm 1 đầu vào) vs Shelf (cấm 1 đầu ra).
- Đọc TẦNG B để theo dõi trạng thái con trỏ Front và Rear thay đổi như thế nào khi thao tác Enqueue và Dequeue trên hàng đợi vòng.

---

## 8. 연결 리스트, 스택, 큐, 데크 (Data Structure Types)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 연결 리스트 (Linked List - Danh sách liên kết):**
  - `단일 연결 리스트 (Singly Linked List)`: Mỗi nút gồm 2 trường: Dữ liệu (Data) và Con trỏ liên kết (Next Pointer) trỏ đến nút kế tiếp. Duyệt một chiều từ đầu (Head) đến cuối (Tail).
  - `이중 연결 리스트 (Doubly Linked List)`: Mỗi nút có 2 con trỏ: Con trỏ trỏ nút trước (Prev) và Con trỏ trỏ nút sau (Next). Cho phép duyệt linh hoạt theo cả hai chiều tiến và lùi.
  - `원형 연결 리스트 (Circular Linked List)`: Nút cuối cùng (Tail) thay vì trỏ NULL thì trỏ ngược lại nút đầu tiên (Head), tạo thành một vòng tròn khép kín, duyệt từ nút bất kỳ có thể đi qua toàn bộ danh sách.
- **2. 스택 (Stack - Ngăn xếp):**
  - **Nguyên lý hoạt động:** **LIFO (Last In First Out - Vào sau ra trước)**.
  - **Thao tác cốt lõi:**
    - `Push`: Đẩy một phần tử mới vào vị trí đỉnh ngăn xếp (`Top`).
    - `Pop`: Lấy ra và xóa phần tử đang nằm ở đỉnh ngăn xếp (`Top`).
    - `오버플로 (Overflow)`: Xảy ra khi ngăn xếp đã đầy kín dung lượng mà vẫn cố tình thực hiện thao tác Push.
    - `언더플로 (Underflow)`: Xảy ra khi ngăn xếp đang rỗng hoàn toàn mà vẫn cố tình thực hiện thao tác Pop.
  - **Các ứng dụng kinh điển của Stack trong đề thi:**
    - Gọi hàm đệ quy (`재귀 호출 - Recursion`) và lưu trữ ngăn xếp hàm (Call Stack).
    - Tính năng hoàn tác (`Undo / Ctrl+Z`) trong các trình soạn thảo văn bản.
    - Đảo ngược chuỗi ký tự (`문자열 역순 출력`).
    - Thuật toán tìm kiếm theo chiều sâu trên đồ thị (`DFS - Depth-First Search`).
    - Chuyển đổi và tính toán giá trị biểu thức số học dạng hậu tố (Postfix Evaluation).
- **3. 큐 (Queue - Hàng đợi):**
  - **Nguyên lý hoạt động:** **FIFO (First In First Out - Vào trước ra trước)**.
  - **Cơ chế con trỏ:**
    - `Front (Đầu trước)`: Vị trí lấy phần tử ra khỏi hàng đợi (`삭제 / Dequeue`).
    - `Rear (Đầu sau)`: Vị trí chèn phần tử mới vào hàng đợi (`삽입 / Enqueue`).
  - **Các ứng dụng kinh điển của Queue trong đề thi:**
    - Quản lý hàng đợi in ấn tài liệu trên máy in (`스풀링 - Spooling`).
    - Lập lịch điều phối tiến trình của CPU (`CPU 스케줄링 - FCFS, Round Robin`).
    - Thuật toán tìm kiếm theo chiều rộng trên đồ thị (`BFS - Breadth-First Search`).
- **4. 데크 (Deque - Double-Ended Queue):**
  - Là cấu trúc mở rộng cho phép thực hiện thao tác chèn và xóa ở **cả hai đầu (cả đầu Front lẫn đầu Rear)**.
  - **2 biến thể hạn chế (Đặc sản thi trắc nghiệm):**
    - `스크롤 (Scroll - Hạn chế đầu vào / Input Restricted Deque)`: **Chỉ cho phép chèn ở 1 đầu duy nhất**, nhưng cho phép xóa ở cả 2 đầu.
    - `셸프 (Shelf - Hạn chế đầu ra / Output Restricted Deque)`: **Chỉ cho phép xóa ở 1 đầu duy nhất**, nhưng cho phép chèn ở cả 2 đầu.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Thao tác gọi hàm đệ quy (Recursion) sử dụng cấu trúc dữ liệu nào?"* -> **스택 (Stack)**, KHÔNG PHẢI Queue.
  - **Bẫy 2:** *"Xử lý Spooling của máy in sử dụng cấu trúc dữ liệu nào?"* -> **큐 (Queue)**.
  - **Bẫy 3:** *"Biến thể Deque chỉ cho phép chèn ở 1 đầu gọi là gì?"* -> **스크롤 (Scroll)**. Biến thể chỉ cho phép xóa ở 1 đầu gọi là gì? -> **셸프 (Shelf)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Stack LIFO dùng cho Đệ quy và Undo; Queue FIFO dùng cho Máy in và CPU; Scroll cấm 1 đầu vào, Shelf cấm 1 đầu ra".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế Hàng đợi vòng (Circular Queue) giải quyết vấn đề của Queue tuyến tính:**
  - Trong Queue tuyến tính, khi Rear chạm đáy mảng thì dù các phần tử ở Front đã bị Pop ra ngoài tạo khoảng trống, ta vẫn bị báo Overflow giả (Fake Overflow).
  - Hàng đợi vòng giải quyết bằng phép toán modulo `%`:
    $$\text{Rear} = (\text{Rear} + 1) \pmod{\text{Max\_Size}}$$
    $$\text{Front} = (\text{Front} + 1) \pmod{\text{Max\_Size}}$$
  - Điều này giúp con trỏ tự động quay vòng lại đầu mảng khi còn ô trống.

### 복습 체크리스트
- [ ] Phân biệt được Singly, Doubly, và Circular Linked List.
- [ ] Nêu nguyên lý LIFO của Stack và kể tên 3 ứng dụng (Recursion, Undo, DFS).
- [ ] Nêu nguyên lý FIFO của Queue và kể tên 2 ứng dụng (Spooling, BFS).
- [ ] Phân biệt được Scroll (chèn 1 đầu) và Shelf (xóa 1 đầu) của cấu trúc Deque.
