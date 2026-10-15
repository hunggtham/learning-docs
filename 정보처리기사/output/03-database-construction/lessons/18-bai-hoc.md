# 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)

## 학습 목표 (Mục tiêu)
- Hiểu sâu nguyên nhân gốc rễ sinh ra 3 hiện tượng dị thường dữ liệu (`이상 현상 / Anomaly`): Dị thường Thêm (`삽입 이상`), Dị thường Xóa (`삭제 이상`), và Dị thường Cập nhật (`갱신 이상`).
- Phân tích chi tiết 10 mục tiêu thiết kế của Chuẩn hóa dữ liệu (`정규화의 목적`) theo giáo trình thi Kỹ sư xử lý thông tin Hàn Quốc.
- Khắc sâu bản chất toán học của Phụ thuộc hàm (`함수적 종속성`) và Phụ thuộc bắc cầu (`이행적 함수 종속성: $A \rightarrow B, B \rightarrow C \implies A \rightarrow C$`).

## 핵심 키워드 (Từ khóa)
- 정규화 (Chuẩn hóa / Normalization)
- 이상 현상 (Hiện tượng dị thường / Anomaly)
- 삽입 이상 (Dị thường thêm / Insertion Anomaly)
- 삭제 이상 (Dị thường xóa / Deletion Anomaly)
- 갱신 이상 (Dị thường cập nhật / Update Anomaly)
- 연쇄 삭제 (Xóa liên đới dây chuyền / Cascading Deletion)
- 정보 모순 (Mâu thuẫn thông tin / Inconsistency)
- 함수적 종속 (Phụ thuộc hàm / Functional Dependency)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([14-bai-hoc.md](14-bai-hoc.md), [15-bai-hoc.md](15-bai-hoc.md), [17-bai-hoc.md](17-bai-hoc.md)):** Khi thiết kế bảng vi phạm quy tắc toàn vẹn hoặc gộp chung nhiều thực thể độc lập vào cùng một quan hệ, hiện tượng dị thường sẽ bùng phát ngay khi vận hành.
- **Tiếp nối sang các bài sau ([19-bai-hoc.md](19-bai-hoc.md), [20-bai-hoc.md](20-bai-hoc.md)):** Để sửa chữa dị thường mà không làm giảm tốc độ hệ thống quá mức, người kỹ sư phải cân bằng giữa Chuẩn hóa và Phi chuẩn hóa (`반정규화`).

## 읽는 방법 (Cách đọc)
- Phân biệt 3 loại Dị thường qua các tình huống điển hình:
  - Muốn thêm thông tin này nhưng **bắt buộc phải bịa ra thông tin khác** $\rightarrow$ **삽입 이상 (Dị thường thêm)**.
  - Xóa một thông tin này nhưng **bị xóa mất luôn thông tin quan trọng khác** $\rightarrow$ **삭제 이상 (Dị thường xóa)**.
  - Cập nhật một chỗ nhưng chỗ khác không đổi gây **mâu thuẫn dữ liệu** $\rightarrow$ **갱신 이상 (Dị thường cập nhật)**.

---

## 179-182. 정규화와 이상 심화 (Normalization & Anomaly - Deep Dive)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Ba loại dị thường dữ liệu kinh điển (이상 현상 3가지):**
  | Hiện tượng dị thường | Tên tiếng Hàn & Anh | Cơ chế phát sinh | Hậu quả kỹ thuật |
  |---|---|---|---|
  | **Dị thường Thêm** | `삽입 이상` (Insertion Anomaly) | Khi muốn chèn một bộ dữ liệu mới, hệ thống bắt buộc người dùng phải nhập kèm các giá trị không mong muốn hoặc chưa có (do bảng có khóa chính kết hợp bị dính dữ liệu chưa phát sinh). | Không thể ghi dữ liệu nếu thiếu thông tin phụ, hoặc phải chấp nhận chèn giá trị giả/rỗng vi phạm toàn vẹn. |
  | **Dị thường Xóa** | `삭제 이상` (Deletion Anomaly) | Khi xóa một dữ liệu không còn cần thiết, các dữ liệu có giá trị quan trọng khác cùng nằm trên hàng đó bị xóa liên đới ngoài ý muốn (`연쇄 삭제`). | Mất vĩnh viễn thông tin nền tảng mà người dùng không hề muốn xóa. |
  | **Dị thường Cập nhật** | `갱신 이상` (Update Anomaly) | Dữ liệu bị dư thừa trùng lặp trên nhiều hàng, khi chỉnh sửa chỉ cập nhật một số hàng mà bỏ sót các hàng còn lại. | Gây mâu thuẫn thông tin (`정보 모순 / Inconsistency`), cùng một đối tượng nhưng có hai thông tin khác nhau. |

- **2. Mục tiêu toàn diện của Chuẩn hóa (정규화의 목적):**
  - **Duy trì tính ổn định và toàn vẹn của cấu trúc dữ liệu** (`데이터 구조의 안정성 및 무결성 유지`).
  - **Loại bỏ sự dư thừa dữ liệu** để ngăn ngừa 3 loại dị thường (`데이터 중복 배제하여 이상 발생 방지`).
  - **Tối thiểu hóa không gian lưu trữ dữ liệu** (`자료 저장 공간의 최소화`).
  - **Giảm nhu cầu phải tái cấu trúc lược đồ quan hệ** khi phát sinh thêm dữ liệu mới.
  - **Đơn giản hóa mô hình dữ liệu** (`데이터 모형의 단순화`).
  - Cho phép biểu diễn bất kỳ quan hệ nào một cách rõ ràng trong CSDL.
- **3. Phụ thuộc hàm (함수적 종속성 / Functional Dependency):**
  - Ký hiệu: $X \rightarrow Y$ ($X$ là Yếu tố quyết định / `결정자`, $Y$ là Yếu tố phụ thuộc / `종속자`).
  - Nghĩa là: Cứ với mỗi giá trị của $X$ thì luôn xác định duy nhất một giá trị tương ứng của $Y$.
  - **Phụ thuộc hàm bắc cầu (`이행적 함수 종속`):** Nếu $X \rightarrow Y$ và $Y \rightarrow Z$ thì dẫn đến $X \rightarrow Z$. Đây là đối tượng trọng tâm cần loại bỏ khi đưa từ **2NF lên 3NF**.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Tình trạng xóa một sinh viên hủy môn học làm mất luôn toàn bộ thông tin về môn học đó là dị thường gì?"* $\rightarrow$ Đáp án: **삭제 이상 (Deletion Anomaly)**.
  - Đề hỏi: *"Chuẩn hóa có làm tăng tốc độ truy vấn SELECT không?"* $\rightarrow$ **KHÔNG**, chuẩn hóa giảm dư thừa và tránh dị thường, nhưng làm tăng phép Join nên có thể **làm chậm** tốc độ SELECT. (Muốn tăng tốc phải dùng Phi chuẩn hóa `반정규화`).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ phân tích ca bệnh dị thường:**
  - Giả sử bảng duy nhất: `DANG_KY(MaSV, TenSV, MaMH, TenMH, GiangVien)`:
    - **삽입 이상:** Thêm môn học mới `CS201 - Trí tuệ nhân tạo` nhưng chưa có sinh viên nào đăng ký $\rightarrow$ Do `MaSV` là khóa chính nên không thể để `NULL`, không thể chèn môn học mới vào CSDL!
    - **삭제 이상:** Sinh viên duy nhất học môn `Toán rời rạc` xin rút môn $\rightarrow$ Xóa hàng của sinh viên đó sẽ xóa mất luôn thông tin về môn `Toán rời rạc` và giảng viên giảng dạy!
    - **갱신 이상:** Giảng viên môn `Cơ sở dữ liệu` đổi phòng làm việc $\rightarrow$ Phải cập nhật hàng trăm dòng của hàng trăm sinh viên học môn này; nếu sót 1 dòng sẽ dẫn đến thông tin phòng làm việc bị xung đột.
  - **Giải pháp chuẩn hóa:** Phân tách thành 3 bảng độc lập: `SINH_VIEN`, `MON_HOC`, và `DANG_KY_MON`. Khi đó cả 3 dị thường đều được hóa giải triệt để.

### 복습 체크리스트
- [ ] Trình bày rõ định nghĩa và ví dụ của 3 hiện tượng dị thường: 삽입 이상, 삭제 이상, 갱신 이상.
- [ ] Phân tích được tác hại của việc xóa dây chuyền (연쇄 삭제).
- [ ] Nắm vững khái niệm 결정자 ($X$) và 종속자 ($Y$) trong quan hệ $X \rightarrow Y$.
- [ ] Hiểu được vì sao chuẩn hóa giúp loại bỏ dị thường nhưng lại tăng số lượng phép Join.
