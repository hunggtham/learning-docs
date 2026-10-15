# 075 & 076: 스택, 큐, 데크 (Stack, Queue, Deque)

## 학습 목표 (Mục tiêu)
- So sánh toàn diện ba cấu trúc dữ liệu tuyến tính trọng điểm: Ngăn xếp (스택 - Stack), Hàng đợi (큐 - Queue) và Hàng đợi hai đầu (데크 - Deque).
- Nắm vững sự đối lập về nguyên lý xuất nhập: Stack theo LIFO (Vào sau ra trước) vs Queue theo FIFO (Vào trước ra trước).
- Phân biệt chính xác hai biến thể đặc biệt của Deque: Scroll (스크롤 - Deque hạn chế đầu vào) và Shelf (셸프 - Deque hạn chế đầu ra).

## 핵심 키워드 (Từ khóa)
- 스택 (Stack) & LIFO (후입선출)
- 큐 (Queue) & FIFO (선입선출)
- 데크 (Deque - Double Ended Queue)
- 프런트 (Front) & 리어 (Rear)
- 스크롤 (Scroll - 입력 제한 데크)
- 셸프 (Shelf - 출력 제한 데크)
- 작업 스케줄링 (Job Scheduling) & BFS

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): Chi tiết cơ chế vận hành và ứng dụng của Stack.
- [04-bai-hoc.md](04-bai-hoc.md): Chi tiết cấu trúc Hàng đợi (Queue) và các dạng Queue vòng (Circular Queue).
- [10-bai-hoc.md](10-bai-hoc.md): Thuật toán tìm kiếm theo chiều rộng (BFS) sử dụng Queue.

## 읽는 방법 (Cách đọc)
- Nắm vững bảng so sánh đối đầu giữa Stack vs Queue (Con trỏ, Nguyên lý, Ứng dụng).
- Đi thi trắc nghiệm phần Deque cực kỳ hay hỏi về Scroll vs Shelf:
  - **Scroll (스크롤):** Hạn chế **Đầu vào (입력 제한)** $\rightarrow$ Vào 1 đầu, ra 2 đầu.
  - **Shelf (셸프):** Hạn chế **Đầu ra (출력 제한)** $\rightarrow$ Vào 2 đầu, ra 1 đầu.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh tổng hợp Stack vs Queue vs Deque:**

| Tiêu chí so sánh | 스택 (Stack) | 큐 (Queue) | 데크 (Deque) |
| :--- | :--- | :--- | :--- |
| **Nguyên lý xuất nhập** | **LIFO (Last-In, First-Out)** / 후입선출 | **FIFO (First-In, First-Out)** / 선입선출 | Vào và ra linh hoạt ở **cả hai đầu** |
| **Vị trí thao tác** | Chỉ ở **1 đầu** duy nhất (Đỉnh Top) | Thêm ở đầu cuối (`Rear`), Lấy ra ở đầu trước (`Front`) | Thêm và xóa đều được ở cả đầu trước (Left) và đầu sau (Right) |
| **Con trỏ quản lý** | Con trỏ `Top` (và `Bottom` cố định) | Hai con trỏ: `Front` (xóa) và `Rear` (chèn) | Hai con trỏ ở hai đầu biên |
| **Lĩnh vực ứng dụng** | Đệ quy, ngắt CPU, biểu thức Postfix, nút Back, thuật toán DFS | Hàng đợi in ấn (Spooling), lập lịch tiến trình OS (FCFS Scheduling), thuật toán BFS | Quản lý bộ đệm kép, hàng đợi ưu tiên 2 chiều |

- **Hai biến thể giới hạn của Deque (Rất hay thi):**
  - **1. 스크롤 (Scroll - 입력 제한 데크 / Input Restricted Deque):**
    - **Hạn chế đầu vào:** Chỉ cho phép **chèn dữ liệu ở 1 đầu duy nhất**, nhưng cho phép **xóa dữ liệu ở cả 2 đầu**.
  - **2. 셸프 (Shelf - 출력 제한 데크 / Output Restricted Deque):**
    - **Hạn chế đầu ra:** Chỉ cho phép **xóa dữ liệu ở 1 đầu duy nhất**, nhưng cho phép **chèn dữ liệu ở cả 2 đầu**.

- **Bẫy đề thi trắc nghiệm:**
  - **Bẫy 1:** *"Cấu trúc Deque chỉ cho phép thêm dữ liệu ở một đầu nhưng cho phép xóa ở hai đầu gọi là gì?"* $\rightarrow$ Đáp án: **스크롤 (Scroll)**.
  - **Bẫy 2:** *"Hàng đợi tiến trình đợi CPU trong hệ điều hành sử dụng cấu trúc nào?"* $\rightarrow$ Đáp án: **큐 (Queue / FIFO)**.
  - **Bẫy 3:** *"Thao tác lấy dữ liệu trong Queue làm thay đổi con trỏ nào?"* $\rightarrow$ Lấy ra (Delete) làm tăng con trỏ **Front**; Thêm vào (Insert) làm tăng con trỏ **Rear**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa cơ chế hoạt động Deque:**
  - **Scroll (Hạn chế Input):**
    ```
    Input duy nhất --> [   ĐẦU A   ] [ Data 1 ] [ Data 2 ] [   ĐẦU B   ]
    Output A     <--                                      --> Output B
    ```
  - **Shelf (Hạn chế Output):**
    ```
    Input A      --> [   ĐẦU A   ] [ Data 1 ] [ Data 2 ] [   ĐẦU B   ] <-- Input B
    Output duy nhất <--
    ```
- **Hiện tượng tràn ảo trong Linear Queue:**
  - Trong Queue tuyến tính dạng mảng, khi `Rear` chạm đáy mảng thì không thể chèn thêm dù vùng trước `Front` đã bị xóa trống. Giải pháp khắc phục là sử dụng **원형 큐 (Circular Queue - Hàng đợi vòng)** dùng phép chia lấy dư modulo.

### 복습 체크리스트
- [ ] So sánh được sự khác biệt giữa LIFO (Stack) và FIFO (Queue).
- [ ] Xác định chính xác vai trò của Front (lấy ra) và Rear (thêm vào) trong Queue.
- [ ] Nắm vững đặc trưng Deque: Vào/ra ở cả 2 đầu.
- [ ] Phân biệt không nhầm lẫn giữa Scroll (Hạn chế Input) và Shelf (Hạn chế Output).
