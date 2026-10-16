# 선형 자료구조 (Cấu trúc dữ liệu tuyến tính)

## 학습 목표
- Nắm vững định nghĩa và hệ thống phân loại cấu trúc dữ liệu: phân biệt cấu trúc tuyến tính (`선형 구조` - quan hệ $1 - 1$) và phi tuyến (`비선형 구조` - quan hệ $1 - N, N - M$).
- So sánh đối đầu giữa Mảng liên tục (`연속 리스트` - mật độ lưu trữ bằng 1, truy cập $O(1)$, chèn/xóa $O(n)$) và Danh sách liên kết (`연결 리스트` - mật độ $< 1$, chèn/xóa $O(1)$, truy cập $O(n)$).
- Phân biệt hai trạng thái lỗi biên bộ nhớ: Tràn bộ nhớ (`오버플로 / Overflow`) và Thiếu hụt bộ nhớ (`언더플로 / Underflow`).
- Nắm vững nguyên lý hoạt động của Ngăn xếp (`스택 / Stack` - LIFO) và 6 ứng dụng kinh điển: đệ quy (`재귀 호출`), ngắt CPU (`인터럽트`), hàm con (`서브루틴`), biểu thức hậu tố (`수식 계산 / 후위 표기법`), đảo ngược chuỗi và tìm kiếm DFS.
- Nắm vững nguyên lý hoạt động của Hàng đợi (`큐 / Queue` - FIFO), hiện tượng tràn ảo và công thức hàng đợi vòng (`원형 큐 / Circular Queue`).
- Phân biệt hai biến thể hạn chế của Hàng đợi hai đầu (`데크 / Deque`): Scroll (`스크롤` - hạn chế đầu vào) và Shelf (`셸프` - hạn chế đầu ra).

## 핵심 키워드
- 선형 자료구조 (Cấu trúc dữ liệu tuyến tính / Linear Data Structures)
- 연속 리스트 vs 연결 리스트 (Mảng liên tục vs Danh sách liên kết / Contiguous vs Linked List)
- 오버플로 & 언더플로 (Overflow - đầy chèn thêm vs Underflow - rỗng lấy ra)
- 스택 (Ngăn xếp / Stack / LIFO / PUSH & POP / 재귀 호출 / 서브루틴 / 인터럽트)
- 큐 (Hàng đợi / Queue / FIFO / Front & Rear / Enqueue & Dequeue / 작업 스케줄링)
- 원형 큐 (Hàng đợi vòng / Circular Queue / Tràn ảo / Modulo)
- 데크 (Hàng đợi hai đầu / Deque / 스크롤 Scroll - 입력 제한 vs 셸프 Shelf - 출력 제한)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở Môn 1 [12-cau-truc-du-lieu-va-thuat-toan.md](../../01-software-design/lessons/12-cau-truc-du-lieu-va-thuat-toan.md), chúng ta đã khảo sát tổng quan vai trò của dữ liệu và giải thuật trong thiết kế phần mềm.
- **Đang giải quyết gì (Current Problem):** Bài học này đi sâu vào tầng vật lý bộ nhớ, phân tích cơ chế con trỏ, mật độ lưu trữ và các thao tác chèn/xóa trên 4 cấu trúc tuyến tính nền tảng (Mảng, Danh sách liên kết, Stack, Queue, Deque).
- **Dùng đi đâu (Forward Handoff):** Ứng dụng trực tiếp của Ngăn xếp (Stack) trong tính toán biểu thức được chuyển giao sang [02-ky-phap-bieu-thuc-va-stack.md](02-ky-phap-bieu-thuc-va-stack.md) để khảo sát ký pháp Infix, Prefix, Postfix.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng phân loại Tuyến tính vs Phi tuyến, bảng so sánh Mảng vs Danh sách liên kết, bảng phân biệt Deque Scroll vs Shelf và các bẫy trắc nghiệm.
- Đọc TẦNG B để hiểu sâu biểu đồ ASCII của Stack, Queue, công thức modulo của Hàng đợi vòng và 6 ứng dụng kinh điển của Stack trong hệ điều hành/trình biên dịch.

---

## 선형 자료구조

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại cấu trúc dữ liệu tổng quan
| Phân loại | Tên tiếng Hàn & Anh | Các cấu trúc tiêu biểu | Mối quan hệ giữa các phần tử |
| :--- | :--- | :--- | :--- |
| **선형 구조 (Linear)** | Tuyến tính | **배열 (Array)**, **선형 리스트 (Linear List)** (연속 vs 연결), **스택 (Stack)**, **큐 (Queue)**, **데크 (Deque)** | Quan hệ 1 - 1 (Mỗi phần tử chỉ có tối đa 1 phần tử trước và 1 phần tử sau) |
| **비선형 구조 (Non-linear)** | Phi tuyến | **트리 (Tree)**, **그래프 (Graph)** | Quan hệ 1 - N (Cây phân cấp) hoặc N - M (Mạng lưới đồ thị) |

#### 2. Bảng so sánh đối đầu Mảng liên tục vs Danh sách liên kết
| Tiêu chí | 연속 리스트 (Contiguous List / Array) | 연결 리스트 (Linked List) |
| :--- | :--- | :--- |
| **Vị trí ô nhớ vật lý** | Nằm **liên tiếp kề nhau** trong bộ nhớ RAM | Nằm **rải rác bất kỳ**, kết nối qua con trỏ |
| **Truy cập ngẫu nhiên** | **Rất nhanh: $O(1)$** qua chỉ số index `array[i]` | **Chậm: $O(n)$**, phải duyệt tuần tự từ đầu Head |
| **Thao tác Chèn / Xóa** | **Chậm: $O(n)$**, phải dịch chuyển các phần tử sau | **Rất nhanh: $O(1)$**, chỉ cập nhật lại con trỏ |
| **Mật độ lưu trữ** | **Tối đa: Bằng 1** (toàn bộ ô nhớ chứa dữ liệu thật) | **Nhỏ hơn 1** (tốn thêm vùng nhớ lưu con trỏ trỏ tiếp) |
| **Kích thước bộ nhớ** | Cố định, khó thay đổi linh hoạt | Co giãn động theo nhu cầu |

#### 3. Bảng phân biệt Scroll vs Shelf trong Deque (Hàng đợi hai đầu)
| Biến thể | Tên tiếng Hàn & Anh | Cơ chế hạn chế (Bẫy đề thi cốt lõi) | Mô hình trực quan |
| :--- | :--- | :--- | :--- |
| **Scroll** | **스크롤 (입력 제한 데크 / Input Restricted)** | **Hạn chế Đầu vào:** Chỉ cho phép **chèn ở 1 đầu**, cho phép **xóa ở cả 2 đầu** | Vào 1 đầu $\rightarrow$ Ra cả 2 đầu |
| **Shelf** | **셸프 (출력 제한 데크 / Output Restricted)** | **Hạn chế Đầu ra:** Chỉ cho phép **xóa ở 1 đầu**, cho phép **chèn ở cả 2 đầu** | Vào cả 2 đầu $\rightarrow$ Ra 1 đầu |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Cấu trúc phi tuyến:** Đề hỏi *"Cấu trúc dữ liệu nào sau đây là cấu trúc phi tuyến (비선형 구조)?"* $\rightarrow$ Đáp án đúng chỉ có thể là **트리 (Tree)** hoặc **그래프 (Graph)**. Các cấu trúc còn lại (Array, List, Stack, Queue, Deque) đều là cấu trúc tuyến tính.
- **Bẫy 2: Phân biệt Overflow vs Underflow:**
  - `오버플로 (Overflow)`: Phát sinh khi cấu trúc dữ liệu đã **đầy 100% (Full)** nhưng vẫn cố tình chèn thêm phần tử mới.
  - `언더플로 (Underflow)`: Phát sinh khi cấu trúc dữ liệu đang **trống rỗng (Empty)** nhưng lại gọi thao tác lấy ra hoặc xóa phần tử.
- **Bẫy 3: Phân biệt nguyên lý Stack vs Queue:**
  - `스택 (Stack)`: **LIFO (Last-In First-Out / 후입선출)** - Vào sau ra trước. Thao tác tại đỉnh Top duy nhất.
  - `큐 (Queue)`: **FIFO (First-In First-Out / 선입선출)** - Vào trước ra trước. Chèn ở Rear, lấy ra ở Front.
- **Bẫy 4: Mẹo nhớ Deque Scroll vs Shelf:**
  - **Scroll (Cuộn giấy):** Cuộn văn bản vào theo 1 hướng duy nhất (**Hạn chế Input**), đọc từ cả 2 mép đầu.
  - **Shelf (Giá sách):** Nhét sách vào kệ từ cả 2 bên (**Vào 2 đầu**), lấy sách ra từ 1 mặt trước duy nhất (**Hạn chế Output**).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Khái niệm và phân loại cấu trúc dữ liệu
- [한국어]: **자료 구조는 데이터 간의 관계를 컴퓨터의 메모리에 표현하는 방식으로, 선형 구조와 비선형 구조로 구분된다.**
- [Tiếng Việt]: Cấu trúc dữ liệu là cách thức tổ chức, quản lý và lưu trữ dữ liệu trong bộ nhớ máy tính sao cho các thao tác truy xuất và xử lý đạt hiệu quả tối ưu nhất.
- Mỗi phần tử trong cấu trúc tuyến tính chỉ có tối đa một phần tử đứng trước (tiền nhiệm) và một phần tử đứng sau (kế nhiệm).

#### 2. Cấu trúc vật lý của Danh sách liên kết (Linked List)
- Mỗi nút (Node) trong Danh sách liên kết gồm 2 thành phần vật lý:
  - `데이터 필드 (Data Field)`: Chứa giá trị thực tế của dữ liệu.
  - `링크 / 포인터 필드 (Link / Pointer Field)`: Chứa địa chỉ ô nhớ trỏ đến nút kế tiếp.
- Nếu đứt gãy một con trỏ trung gian mà không lưu lại địa chỉ, toàn bộ các nút phía sau sẽ bị mất dấu, dẫn đến rò rỉ bộ nhớ (Memory Leak).

#### 3. Ngăn xếp (Stack) và Sơ đồ hoạt động
- [한국어]: **스택은 한쪽 끝으로만 자료의 삽입과 삭제가 이루어지는 후입선출(LIFO, Last-In First-Out) 구조이다.**
- [Tiếng Việt]: Ngăn xếp là cấu trúc tuyến tính bị giới hạn thao tác: mọi hoạt động chèn dữ liệu (`PUSH`) và lấy dữ liệu (`POP`) chỉ được phép diễn ra tại duy nhất một đầu gọi là đỉnh **Top**. Đáy ngăn xếp được cố định gọi là **Bottom**.

```
          |           |
PUSH ---> |  Item C   | ---> POP (Đỉnh Top)
          |  Item B   |
          |  Item A   | (Đáy Bottom)
          +-----------+
```

##### 6 ứng dụng kinh điển của Stack trong đề thi
1. **재귀 호출 (Recursive Call — Gọi hàm đệ quy):** Lưu trạng thái các tầng hàm đang gọi dở để quay ngược lại khi chạm điều kiện dừng.
2. **인터럽트 처리 (Interrupt Handling — Xử lý ngắt CPU):** Khi có ngắt, CPU đẩy địa chỉ trở về (**복귀 주소 — Return Address**) và trạng thái thanh ghi vào Stack trước khi nhảy sang thực thi hàm ngắt.
3. **서브루틴 호출 (Subroutine Call — Gọi hàm con):** Lưu địa chỉ lệnh kế tiếp để quay về sau khi thực thi xong hàm con.
4. **수식 계산 및 표기법 변환 (Expression Evaluation):** Chuyển đổi và tính toán giá trị biểu thức Hậu tố (Postfix).
5. **Đảo ngược chuỗi (String Reversal) & Nút Quay lại (Back Button) của trình duyệt web.**
6. **Thuật toán tìm kiếm theo chiều sâu (DFS — Depth-First Search) trên đồ thị.**

#### 4. Hàng đợi (Queue) và Hiện tượng tràn ảo
- [한국어]: **큐는 한쪽 끝에서는 삽입만, 반대쪽 끝에서는 삭제만 이루어지는 선입선출(FIFO, First-In First-Out) 구조이다.**
- [Tiếng Việt]: Hàng đợi là cấu trúc tuyến tính mở ở cả hai đầu:
  - Đầu vào (**리어 / Rear**): Chỉ dùng để chèn thêm phần tử mới vào cuối hàng (**Enqueue / Insert**).
  - Đầu ra (**프런트 / Front**): Chỉ dùng để lấy phần tử ra khỏi đầu hàng (**Dequeue / Delete**).

```
   (Lấy ra: Delete)                              (Thêm vào: Insert)
<--- [ Front ] [ Data 1 ] [ Data 2 ] [ Data 3 ] [ Rear ] <---
```

##### 4 ứng dụng kinh điển của Queue trong đề thi
1. **작업 스케줄링 (Job / Process Scheduling):** Hàng đợi các tiến trình sẵn sàng chờ được cấp phát CPU trong hệ điều hành (Ready Queue).
2. **프린터 인쇄 대기열 (Printer Spooling):** Quản lý danh sách các lệnh in văn bản xếp hàng chờ máy in xử lý.
3. **Bộ đệm truyền thông (Data Communication Buffering):** Hàng đợi gói tin mạng truyền nhận không đồng bộ giữa thiết bị nhanh và thiết bị chậm.
4. **Thuật toán tìm kiếm theo chiều rộng (BFS — Breadth-First Search) trên đồ thị.**

##### Hiện tượng tràn ảo và Giải pháp Hàng đợi vòng (Circular Queue)
- Trong Queue tuyến tính dùng mảng, khi con trỏ `Rear` chạm đáy mảng thì không thể chèn thêm dữ liệu dù các ô phía trước `Front` đã bị xóa trống (gọi là hiện tượng tràn ảo).
- **Giải pháp:** Sử dụng **원형 큐 (Circular Queue — Hàng đợi vòng)**. Khi con trỏ chạm cuối mảng, nó sẽ tự động quay vòng lại chỉ số đầu tiên bằng phép toán chia lấy dư modulo:
  $$\text{Next Rear} = (\text{Rear} + 1) \pmod{\text{Max Size}}$$
- Khi `(Rear + 1) % Max Size == Front`, hàng đợi được xác định là đầy 100%.

#### 5. Hàng đợi hai đầu (데크 / Deque)
- [한국어]: **데크(Deque, Double-Ended Queue)는 양쪽 끝에서 삽입과 삭제가 모두 가능한 선형 자료구조이다.**
- [Tiếng Việt]: Deque là sự tổng hợp linh hoạt giữa Stack và Queue: cho phép chèn và xóa dữ liệu ở cả hai đầu (Left và Right).
- **Scroll (입력 제한 데크):** Hạn chế đầu vào (chèn 1 đầu, lấy ra 2 đầu).
- **Shelf (출력 제한 데크):** Hạn chế đầu ra (chèn 2 đầu, lấy ra 1 đầu).

---

### 복습 체크리스트
- [ ] Phân loại chính xác các cấu trúc tuyến tính (Mảng, Danh sách liên kết, Stack, Queue, Deque) và phi tuyến (Cây, Đồ thị).
- [ ] Nhớ 연속 리스트 có mật độ lưu trữ bằng 1 và truy cập nhanh $O(1)$, nhưng chèn/xóa chậm $O(n)$.
- [ ] Nhớ 연결 리스트 chèn/xóa nhanh $O(1)$ bằng con trỏ nhưng truy cập ngẫu nhiên chậm $O(n)$.
- [ ] Phân biệt rõ Overflow (chèn vào cấu trúc đầy) và Underflow (xóa khỏi cấu trúc rỗng).
- [ ] Định nghĩa Stack theo nguyên lý LIFO (후입선출) và liệt kê 6 bài toán ứng dụng (đệ quy, ngắt CPU, subroutine, postfix, đảo ngược chuỗi, DFS).
- [ ] Định nghĩa Queue theo nguyên lý FIFO (선입선출) và liệt kê 4 ứng dụng (lập lịch tiến trình, spooling, buffer, BFS).
- [ ] Phân biệt chính xác: 스크롤 (Scroll) là Deque hạn chế Input; 셸프 (Shelf) là Deque hạn chế Output.
- [ ] Giải thích nguyên lý Circular Queue dùng phép toán modulo để giải quyết hiện tượng tràn ảo.
