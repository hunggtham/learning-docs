# A+ Deep Dive: 알고리즘 trace와 테스트 판정

## 학습 목표 (Mục tiêu)
- Tổng hợp và rèn luyện kỹ năng giải quyết các câu hỏi phân loại độ khó cao (A+ Deep Dive) trong môn Phát triển phần mềm: Truy vết thuật toán (Algorithm Trace) và Phán đoán thuật ngữ kiểm thử (Test Terminology Mapping).
- Thực hành thành thạo bảng truy vết từng bước (Step-by-Step Trace) của thuật toán Tìm kiếm nhị phân (Binary Search) và Sắp xếp chọn (Selection Sort).
- Nằm lòng các điểm phân biệt "bẫy đề thi" then chốt giữa Test Case vs Test Oracle, Static Analysis vs Dynamic Analysis, và Ngăn xếp (Stack) vs Hàng đợi (Queue).

## 핵심 키워드 (Từ khóa)
- 알고리즘 트레이스 (Algorithm Trace)
- 이분 검색 트레이스 (Binary Search Trace: $O(\log n)$)
- 테스트 케이스 vs 테스트 오라클 (Test Case vs Test Oracle)
- 정적 분석 (Static Analysis) vs 동적 분석 (Dynamic Analysis)
- 회귀 테스트 (Regression Testing)
- 스텁 (Stub) vs 드라이버 (Driver)
- 스택 (LIFO) vs 큐 (FIFO) 응용 판별

## 선행·연결 개념 (Kiến thức liên kết)
- [25-bai-hoc.md](25-bai-hoc.md): Nguyên lý hoạt động và công thức của Tìm kiếm nhị phân.
- [54-bai-hoc.md](54-bai-hoc.md): Định nghĩa và 4 loại hình Test Oracle.
- [55-bai-hoc.md](55-bai-hoc.md): Kiểm thử tích hợp với Test Stub và Test Driver.
- [68-bai-hoc.md](68-bai-hoc.md): Chuyển sang chương Tối ưu hóa hiệu năng truy vấn CSDL và bảo mật giao diện.

## 읽는 방법 (Cách đọc)
- Đọc kỹ TẦNG A để thuộc làu các cặp khái niệm đối ứng thường xuyên bị đề thi gài bẫy đánh lừa.
- Rèn luyện kỹ năng vẽ bảng truy vết nhanh ra nháp: Không bao giờ nhẩm vo trong đầu khi gặp câu hỏi truy vết từng vòng (Pass) của thuật toán sắp xếp hoặc tìm kiếm.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Truy vết thực chiến Thuật toán Tìm kiếm nhị phân (Binary Search Trace):**
  - Cho mảng đã sắp xếp: $A = [2, 5, 8, 12, 16]$ (kích thước $n = 5$, index từ $0$ đến $4$).
  - Bài toán: Tìm kiếm giá trị $\text{target} = 12$.

| Bước | Khoảng tìm kiếm ($F \dots L$) | Giá trị ở giữa ($M$) | So sánh và Phán đoán bước tiếp |
| :---: | :---: | :---: | :--- |
| **Bước 1** | $0 \dots 4$ | $M = \lfloor (0 + 4) / 2 \rfloor = 2 \rightarrow A[2] = 8$ | Do `8 < 12` $\rightarrow$ Thu hẹp tìm kiếm sang nửa bên phải: $F = M + 1 = 3$ |
| **Bước 2** | $3 \dots 4$ | $M = \lfloor (3 + 4) / 2 \rfloor = 3 \rightarrow A[3] = 12$ | **Khớp chính xác ($12 == 12$)!** Kết thúc tìm kiếm sau đúng 2 bước |

- **2. Bảng phân định bẫy thuật ngữ kiểm thử (Test Terminology Mapping):**

| Cặp thuật ngữ hay nhầm | Bản chất phân biệt cốt lõi | Dấu hiệu nhận biết trong đề thi |
| :--- | :--- | :--- |
| **Test Case vs Test Oracle** | **Test Case:** Kịch bản chứa dữ liệu nhập và điều kiện; **Test Oracle:** **Cơ chế / Tiêu chuẩn để phán đoán kết quả chạy là Đúng hay Sai** | Test Case là *đề bài*, Test Oracle là *đáp án mẫu* để chấm điểm |
| **Static vs Dynamic Analysis** | **정적 분석 (Static):** **Tuyệt đối không chạy chương trình**, rà soát cú pháp, độ phức tạp; **동적 분석 (Dynamic):** **Trực tiếp chạy chương trình trên máy**, theo dõi rò rỉ bộ nhớ, biến số | Thấy có thao tác "thực thi mã trên máy" $\rightarrow$ Dynamic |
| **Test Stub vs Test Driver** | **Test Stub:** Giả lập **mô-đun con cấp dưới** (dùng trong Top-down); **Test Driver:** Giả lập **chương trình chính cấp trên** (dùng trong Bottom-up) | Top-down đi với Stub; Bottom-up đi với Driver |
| **Regression Testing** | Sau khi sửa lỗi hoặc đổi code, **kiểm tra lại để bảo đảm không sinh ra lỗi mới (새로운 결함)** | Luôn gắn liền với từ khóa "sau khi sửa đổi mã nguồn" |

- **3. Phân biệt lựa chọn Cấu trúc dữ liệu theo bài toán:**
  - Cứ gặp bài toán yêu cầu **Vào sau ra trước (LIFO)** như: Gọi hàm đệ quy (Recursion), Địa chỉ quay về hàm (Return address), Tính toán biểu thức Postfix, Kiểm tra dấu ngoặc $\rightarrow$ **Chọn ngay 스택 (Stack)**.
  - Cứ gặp bài toán yêu cầu **Vào trước ra trước (FIFO)** như: Lập lịch tiến trình CPU (Job Scheduling), Hàng đợi in ấn (Spooling), Bộ đệm truyền thông (Buffer) $\rightarrow$ **Chọn ngay 큐 (Queue)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Lưu ý trong truy vết thuật toán Sắp xếp chọn (Selection Sort Trace):**
  - Trong đề thi Kỹ sư xử lý thông tin, khi đề bài yêu cầu "Ghi lại trạng thái mảng sau vòng 1 (1회전) của Selection Sort":
    - Phải ghi nhận kết quả **sau khi đã hoàn tất việc hoán đổi phần tử nhỏ nhất về vị trí đầu tiên**, chứ không phải trạng thái trung gian của từng phép so sánh riêng lẻ.
    - Một vòng lặp hoàn chỉnh (Pass) bao gồm việc quét hết mảng và thực hiện tối đa 1 lần hoán đổi (Swap).

### 복습 체크리스트
- [ ] Truy vết thành thạo từng bước của thuật toán tìm kiếm nhị phân $O(\log n)$.
- [ ] Phân biệt dứt khoát Test Case (kịch bản thử nghiệm) và Test Oracle (chuẩn chân lý để chấm đúng/sai).
- [ ] Nhớ Static Analysis không chạy mã, Dynamic Analysis trực tiếp chạy mã trên máy tính.
- [ ] Nhớ các bài toán kinh điển của Stack (đệ quy, biểu thức, ngắt) và Queue (lập lịch, in ấn, buffer).
