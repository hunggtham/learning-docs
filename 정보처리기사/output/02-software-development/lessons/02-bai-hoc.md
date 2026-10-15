# 2. 스택 (Stack) 및 응용 (Applications)

## 학습 목표 (Mục tiêu)
- Định nghĩa chính xác cấu trúc dữ liệu Ngăn xếp (스택 - Stack) và cơ chế vận hành theo nguyên lý Vào sau ra trước (LIFO - Last-In, First-Out / 후입선출).
- Nắm vững các thao tác cốt lõi trên Stack (PUSH, POP), các điều kiện biên gây lỗi tràn bộ nhớ (Overflow) và rỗng bộ nhớ (Underflow).
- Liệt kê đầy đủ và nhận diện chính xác các ứng dụng kinh điển của Stack trong hệ điều hành, trình biên dịch và giải thuật (xử lý ngắt, gọi hàm đệ quy, tính toán biểu thức hậu tố, duyệt đồ thị DFS).

## 핵심 키워드 (Từ khóa)
- 스택 (Stack)
- LIFO (Last-In, First-Out / 후입선출)
- Top 포인터 & Bottom 포인터
- PUSH (데이터 삽입) & POP (데이터 삭제)
- 오버플로 (Overflow) & 언더플로 (Underflow)
- 인터럽트 처리 (Interrupt Handling)
- 서브루틴 호출 및 복귀 주소 (Return Address)
- 후위 표기법 (Postfix Evaluation)
- 깊이 우선 탐색 (DFS)

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Phân loại cấu trúc dữ liệu tuyến tính (Linear Structure).
- [03-bai-hoc.md](03-bai-hoc.md): So sánh tổng hợp Stack, Queue (FIFO) và Deque (Double Ended Queue).
- [12-bai-hoc.md](12-bai-hoc.md): Chuyển đổi và tính toán biểu thức bằng Stack (Infix $\rightarrow$ Postfix).

## 읽는 방법 (Cách đọc)
- Nhớ hình ảnh thực tế: Chồng đĩa hoặc hộp cầu lông (đĩa đặt vào sau cùng sẽ được lấy ra đầu tiên).
- Ghi nhớ các từ khóa ứng dụng thực tế hay hỏi thi: Hễ thấy **"Hàm đệ quy (재귀 호출)"**, **"Lưu địa chỉ quay về khi gọi hàm (복귀 주소)"**, **"Xử lý ngắt (인터럽트)"**, **"Nút Back trình duyệt (뒤로 가기)"** $\rightarrow$ Đáp án chắc chắn là **스택 (Stack)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Đặc trưng bản chất của Stack:**
  - Là cấu trúc dữ liệu tuyến tính mà thao tác thêm (chèn) và xóa phần tử đều chỉ diễn ra tại **duy nhất một đầu**, gọi là đỉnh **Top**.
  - Cơ chế hoạt động: **LIFO (Last-In, First-Out)** hoặc **FILO (First-In, Last-Out)** - Phần tử vào sau cùng sẽ là phần tử đầu tiên được lấy ra.
- **Các thao tác và biến trạng thái cơ bản:**
  - `Top`: Con trỏ luôn chỉ vào phần tử nằm ở vị trí cao nhất hiện tại của Stack.
    - Khi Stack rỗng: $\text{Top} = 0$ (hoặc $-1$ tùy quy ước lập trình).
    - Khi chèn thêm (`PUSH`): Tăng con trỏ $\text{Top} = \text{Top} + 1$, sau đó ghi dữ liệu vào vị trí Top.
    - Khi lấy ra (`POP`): Đọc dữ liệu tại Top, sau đó giảm con trỏ $\text{Top} = \text{Top} - 1$.
  - `Bottom`: Đáy của Stack (cố định).
  - **Lỗi tràn bộ nhớ (Overflow - 오버플로):** Xảy ra khi cố tình thực hiện lệnh `PUSH` vào một Stack đã đầy dung lượng tối đa ($m$).
  - **Lỗi cạn bộ nhớ (Underflow - 언더플로):** Xảy ra khi cố tình thực hiện lệnh `POP` từ một Stack đang hoàn toàn rỗng.

- **Bảng ứng dụng kinh điển của Stack trong đề thi:**

| Lĩnh vực ứng dụng | Tên tiếng Hàn & Anh | Cơ chế hoạt động cụ thể |
| :--- | :--- | :--- |
| **Xử lý ngắt** | **인터럽트 처리 (Interrupt Handling)** | Khi có ngắt CPU, trạng thái thanh ghi và địa chỉ lệnh hiện tại được đẩy vào Stack để sau khi phục vụ ngắt xong sẽ POP ra tiếp tục chạy |
| **Gọi hàm / Thủ tục con** | **서브루틴 호출 및 복귀 주소 저장** | Lưu trữ địa chỉ hoàn trả (Return Address) của hàm cha khi nhảy sang thực thi hàm con (Subroutine / Function Call) |
| **Hàm đệ quy** | **재귀 호출 (Recursive Call)** | Quản lý khung ngăn xếp (Call Stack Frame) qua các tầng đệ quy lồng nhau |
| **Biểu thức toán học** | **수식 표기법 변환 및 연산 (Postfix)** | Chuyển đổi biểu thức trung tố (Infix) sang hậu tố (Postfix) và thực thi tính toán giá trị biểu thức |
| **Kiểm tra cú pháp** | **괄호 검사 (Parenthesis Matching)** | Kiểm tra tính cân xứng đóng/mở của dấu ngoặc `()`, `{}`, `[]` trong trình biên dịch |
| **Trình duyệt & Ứng dụng** | **뒤로 가기 (Undo / Redo / Back)** | Lưu lịch sử thao tác để hoàn tác văn bản hoặc lùi lại trang web trước |
| **Thuật toán đồ thị** | **깊이 우선 탐색 (DFS)** | Dùng Stack (hoặc đệ quy) để đi sâu nhất có thể dọc theo từng nhánh đồ thị trước khi quay lui |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế Call Stack trong bộ nhớ tiến trình (Process Memory Layout):**
  - Trong kiến trúc máy tính, vùng nhớ Stack phát triển từ địa chỉ cao xuống địa chỉ thấp (High Memory $\rightarrow$ Low Memory).
  - Mỗi lời gọi hàm sẽ tạo một **Stack Frame** chứa: Tham số hàm (Parameters), Biến cục bộ (Local variables), Địa chỉ quay về (Return address).
  - Nếu đệ quy vô hạn không có điểm dừng, vùng nhớ Stack sẽ vượt quá giới hạn và gây lỗi kinh điển: **Stack Overflow**.

### 복습 체크리스트
- [ ] Định nghĩa chính xác nguyên lý LIFO (후입선출) của Stack.
- [ ] Nhớ thao tác PUSH (Thêm), POP (Xóa) và vai trò của con trỏ Top.
- [ ] Phân biệt rõ lỗi Overflow (Tràn khi đầy) và Underflow (Cạn khi rỗng).
- [ ] Kể tên ít nhất 5 ứng dụng kinh điển của Stack hay xuất hiện trong đề thi Kỹ sư xử lý thông tin.
