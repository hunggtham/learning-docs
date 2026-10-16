# Môn 2 · Bài 01 — Cấu trúc dữ liệu tuyến tính (선형 자료구조)

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Để xây dựng các module xử lý dữ liệu và thuật toán tối ưu, người học cần nắm vững nền tảng tổ chức dữ liệu trong bộ nhớ máy tính. Bài học này mở màn cho **Chương 1: Cấu trúc dữ liệu, Thuật toán & Tối ưu I/O (데이터 입출력 구현)**, thiết lập bảng phân loại tổng quan giữa cấu trúc tuyến tính và phi tuyến, sau đó phân tích sâu 4 cấu trúc tuyến tính nền tảng: Mảng & Danh sách liên kết, Ngăn xếp (Stack), Hàng đợi (Queue) và Hàng đợi hai đầu (Deque).

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `01-bai-hoc.md`, `02-bai-hoc.md`, `03-bai-hoc.md`, `04-bai-hoc.md`, `80-bai-hoc.md` và `90-bai-hoc.md` (tương ứng với các mục 1, 2, 28, 29, 023 & 024, 075 & 076 trong tài liệu chuẩn gốc). Toàn bộ thuật ngữ và hành vi con trỏ được đối chiếu chính xác theo chuẩn khảo thí HRDK.

> **Mạch kiến thức:** Bài học giải quyết ba bài toán cơ bản trong quản trị bộ nhớ: (1) Mảng liên tục và Danh sách liên kết khác nhau ra sao về mật độ lưu trữ và chi phí chèn/xóa? (2) Tại sao Ngăn xếp (LIFO) là cấu trúc sống còn của đệ quy và ngắt CPU, trong khi Hàng đợi (FIFO) lại điều hành lập lịch tiến trình và bộ đệm? (3) Hai biến thể Scroll và Shelf của Deque khống chế đầu vào/đầu ra như thế nào để phục vụ các bài toán hàng đợi hai chiều?

---

## 1. 자료 구조의 분류 체계 — Phân loại cấu trúc dữ liệu tổng quan

**자료 구조는 데이터 간의 관계를 컴퓨터의 메모리에 표현하는 방식으로, 선형 구조와 비선형 구조로 구분된다.**

Cấu trúc dữ liệu (Data Structure) là cách thức tổ chức, quản lý và lưu trữ dữ liệu trong bộ nhớ máy tính sao cho các thao tác truy xuất và xử lý đạt hiệu quả tối ưu nhất.

### Bảng phân loại cấu trúc dữ liệu toàn diện

| Phân loại | Tên tiếng Hàn & Anh | Các cấu trúc tiêu biểu | Mối quan hệ giữa các phần tử |
| :--- | :--- | :--- | :--- |
| **선형 구조 (Linear)** | Tuyến tính | **배열 (Array)**, **선형 리스트 (Linear List)** (연속 vs 연결), **스택 (Stack)**, **큐 (Queue)**, **데크 (Deque)** | Quan hệ 1 - 1 (Mỗi phần tử chỉ có tối đa một phần tử đứng trước và một phần tử đứng sau) |
| **비선형 구조 (Non-linear)** | Phi tuyến | **트리 (Tree)**, **그래프 (Graph)** | Quan hệ 1 - N (Phân nhánh phân cấp cây) hoặc N - M (Mạng lưới liên kết đồ thị) |

### Dấu hiệu đề thi trắc nghiệm
- Đề thi thường hỏi: *"Cấu trúc dữ liệu nào sau đây là cấu trúc phi tuyến (비선형 구조)?"* $\rightarrow$ Đáp án đúng chỉ có thể là **트리 (Tree)** hoặc **그래프 (Graph)**. Các cấu trúc còn lại (Array, List, Stack, Queue, Deque) đều là cấu trúc tuyến tính.

---

## 2. 선형 리스트: 연속 리스트 vs 연결 리스트 — Mảng liên tục vs Danh sách liên kết

Danh sách tuyến tính (Linear List) lưu trữ một chuỗi các phần tử có thứ tự. Có hai cách hiện thực vật lý chính trên bộ nhớ:

### 2.1. 연속 리스트 (Contiguous / Sequential List — Mảng liên tục)
- **Cơ chế:** Các phần tử được lưu trữ tại các ô nhớ vật lý **nằm liên tiếp kề nhau**.
- **Ưu điểm lớn nhất:** **Truy cập ngẫu nhiên tức thời ($O(1)$)** thông qua chỉ số Index (`array[i]`). Mật độ sử dụng bộ nhớ đạt mức tối đa tuyệt đối (**기억장소 이용 효율 밀도 = 1**), không tốn thêm byte nào cho việc quản lý liên kết.
- **Nhược điểm:** Thao tác chèn hoặc xóa một phần tử ở giữa tốn nhiều chi phí ($O(n)$) do bắt buộc phải dịch chuyển hàng loạt phần tử phía sau để tạo khoảng trống hoặc dồn mảng lại. Kích thước mảng cố định, dễ dẫn đến lãng phí bộ nhớ hoặc tràn mảng.

### 2.2. 연결 리스트 (Linked List — Danh sách liên kết)
- **Cơ chế:** Các phần tử (**Node**) được lưu trữ tại các ô nhớ nằm **rải rác bất kỳ**, mỗi Node gồm 2 thành phần:
  - **데이터 필드 (Data Field):** Lưu trữ giá trị thực tế của dữ liệu.
  - **링크 / 포인터 필드 (Link / Pointer Field):** Lưu trữ địa chỉ ô nhớ của Node kế tiếp.
- **Ưu điểm lớn nhất:** Thao tác **Chèn và Xóa cực kỳ linh hoạt và nhanh chóng ($O(1)$)** khi đã ở đúng vị trí, chỉ cần cập nhật lại địa chỉ con trỏ mà không phải dịch chuyển bất kỳ dữ liệu nào khác. Kích thước bộ nhớ co giãn động theo nhu cầu.
- **Nhược điểm:** Truy cập phần tử chậm ($O(n)$) do bắt buộc phải duyệt tuần tự từ đầu Head Node theo từng con trỏ; mật độ sử dụng bộ nhớ nhỏ hơn 1 (**밀도 < 1**) vì tốn thêm vùng nhớ lưu con trỏ; nếu đứt một con trỏ trung gian thì toàn bộ các Node phía sau sẽ bị mất dấu rò rỉ bộ nhớ.

### Bảng so sánh đối đầu Mảng vs Danh sách liên kết

| Tiêu chuẩn so sánh | 연속 리스트 (Contiguous / Array) | 연결 리스트 (Linked List) |
| :--- | :--- | :--- |
| **Vị trí ô nhớ vật lý** | **Liên tiếp nhau kề sát** | **Nằm rải rác bất kỳ trong RAM** |
| **Mật độ lưu trữ (이용 효율 밀도)** | **밀도 = 1 (Tối đa)** | **밀도 < 1** (Tốn thêm bộ nhớ lưu Pointer) |
| **Truy cập phần tử** | **Random Access tức thì ($O(1)$)** | **Sequential Access tuần tự ($O(n)$)** |
| **Thao tác Chèn / Xóa** | **Chậm ($O(n)$)** do dịch chuyển dữ liệu | **Nhanh ($O(1)$)** chỉ cần đổi con trỏ |
| **Biến thể nâng cao** | Mảng đa chiều, Circular Buffer | Đơn (Singly), Đôi (Doubly), Vòng (Circular) |

### Hai trạng thái lỗi biên bộ nhớ
- **오버플로 (Overflow — Tràn bộ nhớ):** Phát sinh khi cấu trúc dữ liệu đã **đầy 100% (Full)** nhưng chương trình vẫn cố tình thực hiện thao tác chèn thêm phần tử mới.
- **언더플로 (Underflow — Thiếu hụt bộ nhớ):** Phát sinh khi cấu trúc dữ liệu đang **trống rỗng (Empty)** nhưng chương trình lại gọi thao tác lấy ra hoặc xóa phần tử.

---

## 3. 스택 (Stack) — Ngăn xếp vào sau ra trước

**스택은 한쪽 끝으로만 자료의 삽입과 삭제가 이루어지는 후입선출(LIFO, Last-In First-Out) 구조이다.**

Ngăn xếp (Stack) là cấu trúc tuyến tính bị giới hạn thao tác: mọi hoạt động chèn dữ liệu (**`PUSH`**) và lấy dữ liệu (**`POP`**) chỉ được phép diễn ra tại duy nhất một đầu gọi là đỉnh **Top**. Đáy ngăn xếp được cố định gọi là **Bottom**.

```
          |           |
PUSH ---> |  Item C   | ---> POP (Đỉnh Top)
          |  Item B   |
          |  Item A   | (Đáy Bottom)
          +-----------+
```

### Các ứng dụng kinh điển của Stack trong đề thi
Đề thi trắc nghiệm Kỹ sư Xử lý Thông tin thường xuyên yêu cầu nhận diện bài toán nào bắt buộc phải dùng Stack (LIFO):
1. **재귀 호출 (Recursive Call — Gọi hàm đệ quy):** Lưu trạng thái các tầng hàm đang gọi dở để quay ngược lại khi chạm điều kiện dừng.
2. **인터럽트 처리 (Interrupt Handling — Xử lý ngắt CPU):** Khi có ngắt, CPU đẩy địa chỉ trở về (**복귀 주소 — Return Address**) và trạng thái thanh ghi vào Stack trước khi nhảy sang thực thi hàm ngắt.
3. **서브루틴 호출 (Subroutine Call — Gọi hàm con):** Lưu địa chỉ lệnh kế tiếp để quay về sau khi thực thi xong hàm con.
4. **수식 계산 및 표기법 변환 (Expression Evaluation):** Chuyển đổi và tính toán giá trị biểu thức Hậu tố (Postfix).
5. **Đảo ngược chuỗi (String Reversal) & Nút Quay lại (Back Button) của trình duyệt web.**
6. **Thuật toán tìm kiếm theo chiều sâu (DFS — Depth-First Search) trên đồ thị.**

---

## 4. 큐 (Queue) — Hàng đợi vào trước ra trước

**큐는 한쪽 끝에서는 삽입만, 반대쪽 끝에서는 삭제만 이루어지는 선입선출(FIFO, First-In First-Out) 구조이다.**

Hàng đợi (Queue) là cấu trúc tuyến tính mở ở cả hai đầu:
- Đầu vào (**리어 / Rear**): Chỉ dùng để chèn thêm phần tử mới vào cuối hàng (**Enqueue / Insert**).
- Đầu ra (**프런트 / Front**): Chỉ dùng để lấy phần tử ra khỏi đầu hàng (**Dequeue / Delete**).

```
   (Lấy ra: Delete)                              (Thêm vào: Insert)
<--- [ Front ] [ Data 1 ] [ Data 2 ] [ Data 3 ] [ Rear ] <---
```

### Ứng dụng kinh điển của Queue trong đề thi
Cứ gặp bài toán yêu cầu phục vụ theo nguyên tắc "đến trước phục vụ trước" (First-Come, First-Served):
1. **작업 스케줄링 (Job / Process Scheduling):** Hàng đợi các tiến trình sẵn sàng chờ được cấp phát CPU trong hệ điều hành (Ready Queue).
2. **프린터 인쇄 대기열 (Printer Spooling):** Quản lý danh sách các lệnh in văn bản xếp hàng chờ máy in xử lý.
3. **Bộ đệm truyền thông (Data Communication Buffering):** Hàng đợi gói tin mạng truyền nhận không đồng bộ giữa thiết bị nhanh và thiết bị chậm.
4. **Thuật toán tìm kiếm theo chiều rộng (BFS — Breadth-First Search) trên đồ thị.**

### Hiện tượng tràn ảo và Giải pháp Hàng đợi vòng (Circular Queue)
Trong Queue tuyến tính dùng mảng, khi con trỏ `Rear` chạm đáy mảng thì không thể chèn thêm dữ liệu dù các ô phía trước `Front` đã bị xóa trống (gọi là hiện tượng tràn ảo).
- **Giải pháp:** Sử dụng **원형 큐 (Circular Queue — Hàng đợi vòng)**. Khi con trỏ chạm cuối mảng, nó sẽ tự động quay vòng lại chỉ số đầu tiên bằng phép toán chia lấy dư modulo:
  $$\text{Next Rear} = (\text{Rear} + 1) \pmod{\text{Max Size}}$$

---

## 5. 데크 (Deque) — Hàng đợi hai đầu và các biến thể

**데크(Deque, Double-Ended Queue)는 양쪽 끝에서 삽입과 삭제가 모두 가능한 선형 자료구조이다.**

Deque là sự tổng hợp linh hoạt giữa Stack và Queue: cho phép chèn và xóa dữ liệu ở cả hai đầu (Left và Right). Trong đề thi Kỹ sư Xử lý Thông tin, hai biến thể hạn chế của Deque xuất hiện với tần suất cực cao:

### Bảng phân biệt Scroll vs Shelf trong Deque

| Biến thể | Tên tiếng Hàn & Anh | Cơ chế hạn chế (Bẫy đề thi cốt lõi) | Mô hình trực quan |
| :--- | :--- | :--- | :--- |
| **Scroll** | **스크롤 (입력 제한 데크 / Input Restricted Deque)** | **Hạn chế Đầu vào:** Chỉ cho phép **chèn ở 1 đầu duy nhất**, nhưng cho phép **xóa ở cả 2 đầu** | `Vào 1 đầu (Left)` $\rightarrow$ `Ra cả 2 đầu (Left & Right)` |
| **Shelf** | **셸프 (출력 제한 데크 / Output Restricted Deque)** | **Hạn chế Đầu ra:** Chỉ cho phép **xóa ở 1 đầu duy nhất**, nhưng cho phép **chèn ở cả 2 đầu** | `Vào cả 2 đầu (Left & Right)` $\rightarrow$ `Ra 1 đầu (Left)` |

### Mẹo ghi nhớ không bao giờ nhầm
- **Scroll (Cuộn giấy):** Khi cuộn một văn bản, ta chỉ có thể cuộn vào theo 1 hướng duy nhất (**Hạn chế Input**), nhưng khi đọc có thể lật mở xem từ cả 2 mép đầu.
- **Shelf (Giá sách / Kệ đựng đồ):** Ta có thể nhét sách vào kệ từ cả bên trái lẫn bên phải (**Vào 2 đầu**), nhưng giá sách áp sát tường chỉ cho phép lấy sách ra từ 1 mặt trước duy nhất (**Hạn chế Output**).

---

## 6. Nối mạch kiến thức sang bài tiếp theo

Từ việc nắm vững 4 cấu trúc dữ liệu tuyến tính nền tảng (Mảng liên tục, Danh sách liên kết, Stack, Queue, Deque), người học đã có được các khối xây dựng cơ bản của bộ nhớ máy tính.

Ứng dụng trực tiếp và sâu sắc nhất của cấu trúc Ngăn xếp (Stack) trong trình biên dịch và hệ điều hành chính là bài toán chuyển đổi và tính toán giá trị biểu thức toán học. Chúng ta sẽ chuyển sang **[Bài 02: Ký pháp biểu thức và ứng dụng ngăn xếp](02-ky-phap-bieu-thuc-va-stack.md)** để làm chủ các giải thuật chuyển đổi Trung tố (Infix), Tiền tố (Prefix), Hậu tố (Postfix) và xây dựng cây biểu thức.

---

## 7. 복습 체크리스트 (Checklist ôn tập)

- [ ] Phân loại chính xác các cấu trúc tuyến tính (Mảng, Danh sách liên kết, Stack, Queue, Deque) và phi tuyến (Cây, Đồ thị).
- [ ] Nhớ 연속 리스트 có mật độ lưu trữ bằng 1 và truy cập nhanh $O(1)$, nhưng chèn/xóa chậm $O(n)$.
- [ ] Nhớ 연결 리스트 chèn/xóa nhanh $O(1)$ bằng con trỏ nhưng truy cập ngẫu nhiên chậm $O(n)$.
- [ ] Phân biệt rõ Overflow (chèn vào cấu trúc đầy) và Underflow (xóa khỏi cấu trúc rỗng).
- [ ] Định nghĩa Stack theo nguyên lý LIFO (후입선출) và liệt kê 5 bài toán ứng dụng (đệ quy, ngắt, subroutine, postfix, DFS).
- [ ] Định nghĩa Queue theo nguyên lý FIFO (선입선출) và liệt kê các ứng dụng (lập lịch tiến trình, spooling, buffer, BFS).
- [ ] Phân biệt chính xác: 스크롤 (Scroll) là Deque hạn chế Input; 셸프 (Shelf) là Deque hạn chế Output.
- [ ] Giải thích nguyên lý Circular Queue dùng phép toán modulo để giải quyết hiện tượng tràn ảo.
