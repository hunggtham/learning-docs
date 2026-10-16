# 선형 자료구조 (Cấu trúc dữ liệu tuyến tính)

## 학습 목표
- Nắm vững bảng phân loại cấu trúc dữ liệu: phân biệt cấu trúc tuyến tính (`선형 구조` - quan hệ 1-1: Mảng, Danh sách liên kết, Stack, Queue, Deque) và phi tuyến (`비선형 구조` - quan hệ 1-N, N-M: Cây, Đồ thị).
- So sánh đối đầu giữa Mảng liên tục (`연속 리스트`) và Danh sách liên kết (`연결 리스트`) về mật độ lưu trữ, tốc độ truy cập ngẫu nhiên và chi phí thao tác chèn/xóa.
- Phân tích nguyên lý LIFO của Ngăn xếp (`스택 / Stack`) và FIFO của Hàng đợi (`큐 / Queue`), nhận diện chính xác các bài toán ứng dụng kinh điển trong đề thi.
- Làm chủ cơ chế giải quyết tràn ảo bằng Hàng đợi vòng (`원형 큐 / Circular Queue`) và phân biệt hai biến thể của Deque: Scroll (`스크롤` - hạn chế Input) và Shelf (`셸프` - hạn chế Output).

## 핵심 키워드
- 선형 자료구조 (Cấu trúc dữ liệu tuyến tính / Linear Data Structure)
- 비선형 구조 (Cấu trúc phi tuyến / Non-linear: 트리 Tree, 그래프 Graph)
- 연속 리스트 vs 연결 리스트 (Contiguous List vs Linked List / 밀도 = 1 vs 밀도 < 1)
- 스택 (Ngăn xếp / Stack / LIFO 후입선출 / Top / Push / Pop)
- 큐 (Hàng đợi / Queue / FIFO 선입선출 / Front / Rear / 원형 큐 Circular Queue)
- 데크 (Hàng đợi 2 đầu / Deque / 스크롤 Scroll - 입력 제한, 셸프 Shelf - 출력 제한)
- 오버플로 vs 언더플로 (Overflow vs Underflow)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Đây là bài học nền tảng mở đầu cho Môn 2 (소프트웨어 개발). Mọi thuật toán tối ưu và chương trình phần mềm đều được xây dựng dựa trên cách tổ chức dữ liệu trong bộ nhớ máy tính.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc tổ chức dữ liệu dạng tuyến tính (1-1), so sánh sự đánh đổi giữa mảng tĩnh và danh sách liên kết động, đồng thời làm rõ cơ chế điều hành luồng lệnh qua Ngăn xếp (Stack) và Hàng đợi (Queue).
- **Dùng đi đâu (Forward Handoff):** Ứng dụng trực tiếp và quan trọng nhất của cấu trúc Ngăn xếp (Stack) trong trình biên dịch chính là bài toán chuyển đổi và tính toán giá trị biểu thức số học, bàn giao trực tiếp sang [02-ky-phap-bieu-thuc-va-stack.md](02-ky-phap-bieu-thuc-va-stack.md).

## 읽는 방법
- Đọc TẦNG A để ghi nhớ chuẩn xác các bẫy đề thi trắc nghiệm: nhận diện cấu trúc phi tuyến duy nhất chỉ có Cây và Đồ thị; Scroll hạn chế Input còn Shelf hạn chế Output; danh sách các ứng dụng bắt buộc dùng Stack vs Queue.
- Đọc TẦNG B để hiểu sâu công thức modulo của Hàng đợi vòng, phân tích mật độ bộ nhớ (밀도) và cơ chế con trỏ trong Danh sách liên kết.

---

## 선형 자료구조

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại cấu trúc dữ liệu tổng quan
| Phân loại | Tên tiếng Hàn & Anh | Các cấu trúc tiêu biểu | Mối quan hệ giữa các phần tử |
| :--- | :--- | :--- | :--- |
| **선형 구조 (Tuyến tính)** | **Linear Structure** | **배열 (Array), 선형 리스트 (Linear List), 스택 (Stack), 큐 (Queue), 데크 (Deque)** | Quan hệ 1 - 1 (mỗi phần tử có tối đa 1 phần tử đứng trước và 1 phần tử đứng sau) |
| **비선형 구조 (Phi tuyến)** | **Non-linear Structure** | **트리 (Tree), 그래프 (Graph)** | Quan hệ 1 - N (phân nhánh phân cấp) hoặc N - M (mạng lưới liên kết đa chiều) |

#### 2. Đối chiếu Mảng liên tục vs Danh sách liên kết
| Tiêu chuẩn so sánh | 연속 리스트 (Contiguous / Array) | 연결 리스트 (Linked List) |
| :--- | :--- | :--- |
| **Vị trí ô nhớ vật lý** | **Liên tiếp nhau kề sát trong RAM** | **Nằm rải rác bất kỳ trong bộ nhớ** |
| **Mật độ lưu trữ (이용 효율 밀도)** | **밀도 = 1 (Tối đa, không tốn con trỏ)** | **밀도 < 1 (Tốn thêm vùng nhớ lưu con trỏ Pointer)** |
| **Truy cập phần tử** | **Truy cập ngẫu nhiên tức thì ($O(1)$ qua Index)** | **Truy cập tuần tự ($O(n)$ phải duyệt từ Head)** |
| **Thao tác Chèn / Xóa** | **Chậm ($O(n)$ do phải dịch chuyển dữ liệu)** | **Nhanh ($O(1)$ chỉ cần đổi hướng con trỏ)** |

#### 3. Bảng đối chiếu Stack vs Queue
| Cấu trúc | Nguyên lý hoạt động | Vị trí thao tác | Ứng dụng thi cử bắt buộc nhớ |
| :--- | :--- | :--- | :--- |
| **스택 (Stack)** | **LIFO (후입선출)** Vào sau ra trước | Chèn và Xóa cùng diễn ra ở đỉnh **Top** | • Gọi đệ quy (Recursive Call)<br>• Xử lý ngắt CPU (Interrupt / Return Address)<br>• Gọi hàm con (Subroutine)<br>• Tính biểu thức Hậu tố (Postfix)<br>• Duyệt đồ thị theo chiều sâu (DFS) |
| **큐 (Queue)** | **FIFO (선입선출)** Vào trước ra trước | Chèn ở cuối **Rear**, Xóa ở đầu **Front** | • Lập lịch tiến trình CPU (Process Scheduling)<br>• Hàng đợi in ấn (Printer Spooling)<br>• Bộ đệm truyền thông (Network Buffer)<br>• Duyệt đồ thị theo chiều rộng (BFS) |

#### 4. Phân biệt Scroll vs Shelf trong Deque (데크)
| Biến thể | Tên tiếng Hàn & Anh | Cơ chế hạn chế | Dấu hiệu nhận diện |
| :--- | :--- | :--- | :--- |
| **Scroll** | **스크롤 (입력 제한 데크)** | **Hạn chế Đầu vào** (Chèn ở 1 đầu, Xóa ở cả 2 đầu) | Cuộn giấy: cuộn vào theo 1 chiều, đọc mở từ 2 mép |
| **Shelf** | **셸프 (출력 제한 데크)** | **Hạn chế Đầu ra** (Xóa ở 1 đầu, Chèn ở cả 2 đầu) | Kệ sách: nhét sách vào từ 2 bên, rút sách ra từ 1 mặt trước |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Cấu trúc phi tuyến:** Đề thi hỏi: "Cấu trúc nào là phi tuyến (`비선형 구조`)?" $\rightarrow$ Đáp án chỉ có thể là **트리 (Tree)** hoặc **그래프 (Graph)**. Các cấu trúc còn lại (Array, List, Stack, Queue, Deque) đều là cấu trúc tuyến tính.
- **Bẫy 2: Lỗi biên bộ nhớ:**
  - Chèn vào khi cấu trúc đã đầy (Full) $\rightarrow$ **오버플로 (Overflow)**.
  - Lấy ra/xóa khi cấu trúc đang rỗng (Empty) $\rightarrow$ **언더플로 (Underflow)**.
- **Bẫy 3: Deque Scroll vs Shelf:** Nhớ từ khóa tiếng Hàn: `스크롤` = **입력 제한** (Hạn chế Input); `셸프` = **출력 제한** (Hạn chế Output).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cấu trúc Node trong Danh sách liên kết
- Mỗi nút (Node) trong Linked List gồm hai thành phần vật lý:
  - `데이터 필드 (Data Field)`: Chứa giá trị thực tế của dữ liệu.
  - `링크/포인터 필드 (Link / Pointer Field)`: Chứa địa chỉ ô nhớ trỏ đến nút kế tiếp.
- Nếu đứt gãy một con trỏ trung gian mà không lưu lại địa chỉ, toàn bộ các nút phía sau sẽ bị mất dấu, dẫn đến rò rỉ bộ nhớ (Memory Leak).

#### 2. Ngăn xếp và cơ chế gọi hàm con (Stack & Subroutine Call)
- Khi hàm $A$ gọi hàm $B$, hệ thống tự động đẩy địa chỉ lệnh kế tiếp của hàm $A$ (`복귀 주소 / Return Address`) cùng các biến cục bộ vào Call Stack.
- Khi hàm $B$ hoàn tất, địa chỉ này được `POP` ra khỏi đỉnh Top để CPU nhảy ngược về tiếp tục thực thi phần còn lại của hàm $A$.

#### 3. Hiện tượng tràn ảo và Hàng đợi vòng (Circular Queue)
- Trong hàng đợi tuyến tính đơn giản, khi chỉ số `Rear` chạm đáy mảng, việc chèn tiếp sẽ báo tràn (`Overflow`) dù các ô phía trước `Front` đã bị lấy ra và đang bỏ trống (gọi là Tràn ảo).
- **Hàng đợi vòng (Circular Queue):** Giải quyết triệt để bằng phép chia lấy dư:
  $$\text{Next Rear} = (\text{Rear} + 1) \pmod{\text{Max Size}}$$
- Khi `(Rear + 1) % Max Size == Front`, hàng đợi được xác định là đầy 100%.

---

### 복습 체크리스트
- [ ] Phân loại chính xác các cấu trúc tuyến tính (Mảng, Danh sách liên kết, Stack, Queue, Deque) và phi tuyến (Cây, Đồ thị).
- [ ] Nhớ rõ Mảng liên tục có mật độ lưu trữ bằng 1 và truy cập $O(1)$, nhưng chèn/xóa chậm $O(n)$.
- [ ] Nhớ rõ Danh sách liên kết chèn/xóa nhanh $O(1)$ nhưng mật độ lưu trữ nhỏ hơn 1 do tốn con trỏ.
- [ ] Phân biệt rõ Overflow (chèn khi đầy) và Underflow (xóa khi rỗng).
- [ ] Định nghĩa Stack theo nguyên lý LIFO và liệt kê 5 bài toán ứng dụng (đệ quy, ngắt CPU, hàm con, postfix, DFS).
- [ ] Định nghĩa Queue theo nguyên lý FIFO và liệt kê các ứng dụng (lập lịch tiến trình, spooling, buffer, BFS).
- [ ] Phân biệt chính xác: Scroll là Deque hạn chế Input; Shelf là Deque hạn chế Output.
- [ ] Nắm vững công thức modulo trong Hàng đợi vòng để khắc phục hiện tượng tràn ảo.
