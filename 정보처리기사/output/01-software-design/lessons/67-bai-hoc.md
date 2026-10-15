# 6. N-S 차트 (Nassi-Schneiderman Chart)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, nguồn gốc và các tên gọi khác của biểu đồ N-S (Nassi-Schneiderman Chart, Box Diagram, Chapin Chart).
- Nhớ tuyệt đối 2 đặc điểm nhận diện cốt lõi phân biệt N-S Chart với Flowchart truyền thống: **Không dùng mũi tên (화살표 미사용)** và **Không cho phép lệnh nhảy tùy tiện GOTO (GOTO 미사용)**.
- Hiểu cách biểu diễn 3 cấu trúc lập trình căn bản (Tuần tự, Lựa chọn, Lặp) trong các khối hộp chữ nhật và đánh giá ưu/nhược điểm thực tế.

## 핵심 키워드 (Từ khóa)
- N-S 차트 (Nassi-Schneiderman Chart)
- 박스 다이어그램 (Box Diagram)
- 샤핀 차트 (Chapin Chart)
- 화살표 미사용 (No Arrows)
- GOTO 미사용 (No GOTO)
- 단일 입구 / 단일 출구 (Single Entry / Single Exit)
- 순차 / 선택 / 반복 (Sequence / Selection / Iteration)

## 선행·연결 개념 (Kiến thức liên kết)
- [66-bai-hoc.md](66-bai-hoc.md): Fan-In / Fan-Out - Chỉ số cấu trúc gọi mô-đun.
- [68-bai-hoc.md](68-bai-hoc.md): 재사용 (Reuse) - Kỹ thuật tái sử dụng phần mềm.
- [29-bai-hoc.md](29-bai-hoc.md): N-S Chart và tính mô-đun hóa trong thiết kế cấu trúc chi tiết.

## 읽는 방법 (Cách đọc)
- Đi thi trắc nghiệm phần mềm: Cứ hễ thấy câu hỏi có từ khóa **"화살표를 사용하지 않음" (Không dùng mũi tên)** hoặc **"GOTO 문을 사용할 수 없음" (Không dùng GOTO)** $\rightarrow$ Khoanh ngay **N-S 차트 (Nassi-Schneiderman Chart)**.
- Phân biệt với lưu đồ thuật toán truyền thống (Flowchart): Flowchart dùng mũi tên chỉ hướng rẽ tự do, dễ tạo mã spaghetti; N-S Chart đóng khung thành từng hộp chữ nhật lồng nhau.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Đặc trưng cốt lõi của N-S 차트:**
  - **Bản chất:** Là một dạng biểu đồ trực quan hóa logic thuật toán dưới dạng **các khối hộp chữ nhật lồng nhau (Box Diagram)**, do Nassi và Schneiderman đề xuất năm 1973 để hỗ trợ phương pháp Lập trình có cấu trúc (Structured Programming).
  - **Tên gọi tương đương:** 박스 다이어그램 (Box Diagram), 샤핀 차트 (Chapin Chart).
- **Các quy tắc thiết kế bất di bất dịch:**
  1. **화살표 미사용 (Không dùng mũi tên):** Luồng điều khiển luôn mặc định chảy từ trên xuống dưới trong từng khối hộp.
  2. **GOTO 사용 불가 (Tuyệt đối không dùng GOTO):** Ngăn chặn hoàn toàn việc nhảy luồng vô tội vạ, triệt tiêu mã nguồn rối rắm (Spaghetti Code).
  3. **단일 입구와 단일 출구 (Single Entry - Single Exit):** Mỗi khối cấu trúc chỉ có duy nhất một điểm vào ở đỉnh trên và một điểm ra ở đáy dưới.
  4. **3 Cấu trúc điều khiển cơ bản:**
     - **순차 (Sequence - Tuần tự):** Các hộp chữ nhật xếp chồng liên tiếp từ trên xuống.
     - **선택 (Selection - Lựa chọn if/else, switch):** Hộp chia đôi bằng đường chéo tam giác điều kiện (True/False hoặc Case 1/2/3).
     - **반복 (Iteration - Lặp while/for):** Khung viền hình chữ L hoặc hộp bao quanh thân vòng lặp.

- **So sánh N-S Chart và Flowchart truyền thống:**

| Đặc tính so sánh | N-S 차트 (Nassi-Schneiderman Chart) | Flowchart (Lưu đồ thuật toán truyền thống) |
| :--- | :--- | :--- |
| **Ký hiệu mũi tên** | **Tuyệt đối không dùng mũi tên** | Dùng mũi tên dày đặc để nối các bước |
| **Lệnh nhảy GOTO** | **Nghiêm cấm hoàn toàn** | Cho phép rẽ nhánh nhảy tự do khắp nơi |
| **Độ khớp mã cấu trúc** | Rất cao, ánh xạ 1-1 trực tiếp sang code Java/C/C++ | Trung bình, dễ phát sinh logic nhảy lộn xộn |
| **Tính trực quan logic** | Rõ ràng phân tầng, dễ nhìn thấy cấu trúc lồng nhau (Nesting) | Dễ theo dõi luồng tổng quan nhưng khó nhìn khối lồng |
| **Độ khó khi sửa đổi** | Khá khó sửa vẽ lại bằng tay khi logic hộp trở nên phức tạp | Dễ vẽ thêm nhánh hoặc nối thêm dây mũi tên |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cấu trúc hình hộp trực quan:**
  - **Khối 순차 (Tuần tự):**
    ```
    +-----------------------------+
    | Khởi tạo biến A = 0         |
    +-----------------------------+
    | Nhập dữ liệu X              |
    +-----------------------------+
    ```
  - **Khối 선택 (Lựa chọn If-Else):**
    ```
    +--------------+--------------+
    | \        X > 0           / |
    |   \  True    |   False  /   |
    |     \        |        /     |
    +--------------+--------------+
    | In "Dương"   | In "Âm/Không"|
    +--------------+--------------+
    ```
  - **Khối 반복 (Vòng lặp While):**
    ```
    +---+-------------------------+
    | L | Điều kiện: X < 10       |
    | ặ +-------------------------+
    | p | X = X + 1; In X         |
    +---+-------------------------+
    ```
- **Ý nghĩa trong kiểm thử phần mềm:**
  - Nhờ tính chất 단일 입구 / 단일 출구 và cấu trúc phân tầng rõ ràng, N-S Chart giúp người kiểm thử (Tester) dễ dàng xác định số lượng đường đi độc lập (Cyclomatic Complexity - McCabe Complexity) để thiết kế bộ ca kiểm thử White-box Testing.

### 복습 체크리스트
- [ ] Ghi nhớ 2 đặc điểm nhận diện tối thượng của N-S Chart: Không dùng mũi tên và Không dùng GOTO.
- [ ] Nhớ tên gọi khác: Box Diagram và Chapin Chart.
- [ ] Nắm vững 3 cấu trúc căn bản: 순차 (Tuần tự), 선택 (Lựa chọn), 반복 (Lặp).
- [ ] Khẳng định được nguyên tắc dòng chảy: 단일 입구 (Một lối vào) và 단일 출구 (Một lối ra).
