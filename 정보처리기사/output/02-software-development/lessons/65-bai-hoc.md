# 130 & 131: 블랙박스 테스트 (Black Box Test)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất và nguyên lý của Kiểm thử hộp đen (블랙박스 테스트 - Black-box Testing) trong việc xác minh các chức năng nghiệp vụ dựa trên bản đặc tả yêu cầu mà không cần nhìn vào mã nguồn bên trong.
- Thành thạo 5 kỹ thuật thiết kế ca kiểm thử hộp đen kinh điển: Phân vùng tương đương (동치 분할), Phân tích giá trị biên (경계값 분석), Đồ thị nguyên nhân - kết quả (원인-효과 그래프), Đoán lỗi (오류 예측) và Kiểm tra so sánh (비교 검사).
- Áp dụng thành thạo kỹ thuật Phân vùng tương đương và Phân tích giá trị biên để giải các bài toán chọn bộ dữ liệu kiểm thử tối ưu trong đề thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- 블랙박스 테스트 (Black-box Testing / 기능 테스트)
- 요구사항 명세서 기반 (Specification-based)
- 동치(동등) 분할 (Equivalence Partitioning / 유효·무효 동치 클래스)
- 경계값 분석 (Boundary Value Analysis: $min, min+1, max-1, max$)
- 원인-효과 그래프 (Cause-Effect Graphing / 의사결정표)
- 오류 예측 (Error Guessing) & 비교 검사 (Comparison Testing)

## 선행·연결 개념 (Kiến thức liên kết)
- [52-bai-hoc.md](52-bai-hoc.md): So sánh tổng quan Kiểm thử hộp trắng vs Kiểm thử hộp đen.
- [56-bai-hoc.md](56-bai-hoc.md): Xây dựng bộ ca kiểm thử (Test Case) dựa trên kỹ thuật Black-box.
- [64-bai-hoc.md](64-bai-hoc.md): Đối chiếu với phương pháp Kiểm thử hộp trắng (White-box Test).

## 읽는 방법 (Cách đọc)
- Phân biệt 2 kỹ thuật hay xuất hiện nhất trong bài tập trắc nghiệm:
  - **동치 분할 (Equivalence Partitioning):** Chia dải dữ liệu thành các khoảng (Lớp hợp lệ và Lớp không hợp lệ), mỗi khoảng chỉ cần bốc **1 giá trị đại diện bất kỳ** để test.
  - **경계값 분석 (Boundary Value Analysis):** Kinh nghiệm cho thấy lỗi luôn tập trung ở đường ranh giới mép $\rightarrow$ Chọn các giá trị **ngay tại biên, sát dưới biên và sát trên biên** ($min - 1, min, min + 1$ và $max - 1, max, max + 1$).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất của Black-box Testing:**
  - Là phương pháp kiểm thử phần mềm ở cấp độ giao diện và chức năng bên ngoài, coi hệ thống như một "chiếc hộp đen bí ẩn" mà kiểm thử viên không thể (hoặc không cần) nhìn thấy cấu trúc mã nguồn bên trong.
  - Mục tiêu: Kiểm tra xem khi truyền dữ liệu hợp lệ và bất hợp lệ vào thì hệ thống có phản hồi đúng các kết quả mong đợi theo bản đặc tả yêu cầu hay không.
- **Bảng chi tiết 5 kỹ thuật thiết kế ca kiểm thử hộp đen:**

| Kỹ thuật kiểm thử | Tên tiếng Hàn & Anh | Cơ chế hoạt động chi tiết | Ví dụ thực tế đề thi |
| :--- | :--- | :--- | :--- |
| **Phân vùng tương đương** | **동치(동등) 분할 (Equivalence Partitioning)** | Chia toàn bộ miền dữ liệu đầu vào thành các phân vùng (lớp tương đương): Lớp hợp lệ (Valid) và Lớp không hợp lệ (Invalid). Chọn 1 giá trị đại diện từ mỗi phân vùng để lập Test Case | Điểm thi từ 0 đến 100: Chia thành 3 vùng: $< 0$ (Không hợp lệ), $0 \sim 100$ (Hợp lệ), $> 100$ (Không hợp lệ). Lấy 3 giá trị test: `-5`, `75`, `120` |
| **Phân tích giá trị biên** | **경계값 분석 (Boundary Value Analysis)** | Phần lớn lỗi lập trình xảy ra ở ranh giới điều kiện (dùng nhầm dấu $>$ thành $\ge$ hoặc $<$ thành $\le$). Kỹ thuật này chọn các giá trị nằm ngay sát hai đầu biên để test | Với điều kiện $0 \le \text{Điểm} \le 100$: Chọn các giá trị kiểm thử là: `-1`, `0`, `1` và `99`, `100`, `101` |
| **Đồ thị nguyên nhân - kết quả** | **원인-효과 그래프 (Cause-Effect Graphing)** | Sử dụng các cổng logic Boolean (AND, OR, NOT) để mô hình hóa mối quan hệ nhân quả phức tạp giữa các điều kiện đầu vào (Nguyên nhân) và hành vi hệ thống (Kết quả), sau đó chuyển thành **Bảng quyết định (Decision Table)** | Đăng nhập hệ thống: Tài khoản đúng VÀ Mật khẩu đúng THÌ Thành công; ngược lại Khóa tài khoản |
| **Đoán lỗi** | **오류 예측 (Error Guessing)** | Dựa trên trực giác, kinh nghiệm thực chiến và dữ liệu lỗi trong quá khứ của kiểm thử viên để "bắt thóp" các lỗi tiềm ẩn mà các kỹ thuật khác bỏ sót | Nhập chuỗi rỗng `""`, nhập số chia là số 0, nhập ký tự SQL Injection `' OR 1=1 --` |
| **Kiểm tra so sánh** | **비교 검사 (Comparison Testing)** | Nạp cùng một tập dữ liệu đầu vào vào nhiều phiên bản phần mềm khác nhau hoặc phần mềm của đối thủ cạnh tranh để so sánh và đối chiếu độ chính xác của kết quả | Kiểm thử phần mềm tính toán thuế mới đối chiếu với phần mềm tính thuế của năm trước |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc 2 điểm biên vs 3 điểm biên trong Boundary Value Analysis:**
  - **Phương pháp 2 điểm biên (Robustness Testing cơ bản):** Cho mỗi biên, chọn giá trị biên hợp lệ ($min$) và giá trị sát biên ngoài không hợp lệ ($min - 1$).
  - **Phương pháp 3 điểm biên (Standard BVA):** Cho mỗi biên, chọn: Giá trị sát bên trong ($min + 1$), Giá trị ngay tại biên ($min$), và Giá trị sát bên ngoài ($min - 1$). Kỹ thuật này phát hiện được hầu hết các lỗi sai sót toán tử so sánh của lập trình viên.

### 복습 체크리스트
- [ ] Định nghĩa Black-box Testing là kiểm thử chức năng không nhìn mã nguồn.
- [ ] Phân biệt được 동치 분할 (chọn 1 giá trị đại diện) và 경계값 분석 (chọn các giá trị quanh mép biên).
- [ ] Nhớ đồ thị nguyên nhân - kết quả (Cause-Effect) chuyển đổi thành Bảng quyết định (Decision Table).
- [ ] Nhớ kỹ thuật 오류 예측 (Error Guessing) dựa hoàn toàn vào kinh nghiệm của kiểm thử viên.
