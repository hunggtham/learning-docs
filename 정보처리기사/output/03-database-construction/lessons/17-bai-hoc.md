# 123-125. 정규화 (Normalization)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và ý nghĩa cốt lõi của Chuẩn hóa dữ liệu (`정규화 / Normalization`): Quá trình phân tách các quan hệ dựa trên lý thuyết phụ thuộc hàm (`함수적 종속성`) để giảm thiểu dư thừa dữ liệu và ngăn ngừa các hiện tượng dị thường (`이상 / Anomaly`).
- Nhớ chính xác giai đoạn thực hiện: Chuẩn hóa được tiến hành trong bước **Thiết kế logic (`논리적 설계 단계`)**.
- Học thuộc lòng chuỗi 6 bước chuẩn hóa kinh điển: **1NF $\rightarrow$ 2NF $\rightarrow$ 3NF $\rightarrow$ BCNF $\rightarrow$ 4NF $\rightarrow$ 5NF** và điều kiện biến đổi của từng bước theo khẩu quyết thi cử tiếng Hàn **"도-부-이-결-다-조"**.

## 핵심 키워드 (Từ khóa)
- 정규화 (Chuẩn hóa / Normalization)
- 함수적 종속성 (Phụ thuộc hàm / Functional Dependency)
- 1NF (제1정규형 - 도메인 원자값 / Miền giá trị nguyên tử)
- 2NF (제2정규형 - 부분 함수 종속 제거 / Khử phụ thuộc hàm từng phần)
- 3NF (제3정규형 - 이행 함수 종속 제거 / Khử phụ thuộc hàm bắc cầu)
- BCNF (보이스-코드 정규형 - 결정자 후보키 / Yếu tố quyết định là khóa ứng viên)
- 4NF (제4정규형 - 다치 종속 제거 / Khử phụ thuộc đa trị)
- 5NF (제5정규형 - 조인 종속 이용 / Dựa trên phụ thuộc kết nối)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([02-bai-hoc.md](02-bai-hoc.md), [11-bai-hoc.md](11-bai-hoc.md), [16-bai-hoc.md](16-bai-hoc.md)):** Chuẩn hóa là trọng tâm kỹ thuật của giai đoạn Thiết kế logic, sử dụng phép chiếu ($\pi$) để phân tách lược đồ lớn thành các lược đồ nhỏ hơn bảo toàn thông tin.
- **Tiếp nối sang các bài sau ([18-bai-hoc.md](18-bai-hoc.md), [19-bai-hoc.md](19-bai-hoc.md), [20-bai-hoc.md](20-bai-hoc.md)):** Hiểu rõ cơ chế từng cấp độ chuẩn hóa sẽ giúp giải quyết triệt để 3 loại dị thường (Thêm, Xóa, Sửa) và đánh giá khi nào cần tiến hành Phi chuẩn hóa (`반정규화`).

## 읽는 방법 (Cách đọc)
- Thuộc làu câu thần chú ghi nhớ tiếng Hàn: **도 - 부 - 이 - 결 - 다 - 조 (Đô - Bu - I - Gyeol - Da - Jo)**.
- Khi làm bài trắc nghiệm, đối chiếu ngay:
  - Thấy "Nguyên tử (원자값)" $\rightarrow$ **1NF**.
  - Thấy "Phụ thuộc hàm từng phần (부분 함수 종속)" $\rightarrow$ **2NF**.
  - Thấy "Bắc cầu (이행적 함수 종속: $A \rightarrow B, B \rightarrow C \implies A \rightarrow C$)" $\rightarrow$ **3NF**.
  - Thấy "Yếu tố quyết định (결정자)" $\rightarrow$ **BCNF**.

---

## 123-125. 정규화 (Normalization)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa và Bản chất của Chuẩn hóa (정규화의 개념):**
  - Là kỹ thuật phân rã lược đồ quan hệ không hợp lý thành các tập thuộc tính nhỏ hơn nhằm **loại bỏ sự dư thừa dữ liệu (`데이터 중복 배제`)** và duy trì tính toàn vẹn.
  - Được thực hiện trong **giai đoạn Thiết kế logic (`논리적 설계 단계`)**.
  - Càng lên dạng chuẩn bậc cao (차수가 높아질수록), số lượng ràng buộc cần thỏa mãn càng nhiều và dữ liệu càng ít dư thừa.
- **2. Bảng tổng hợp 6 cấp độ chuẩn hóa (정규화 과정 요약표):**
  | Cấp độ Chuẩn | Điều kiện chuyển tiếp (Hàn - Việt) | Khẩu quyết | Bản chất kỹ thuật cần nhớ |
  |---|---|:---:|---|
  | **Bảng chưa chuẩn $\rightarrow$ 1NF** | **도메인이 원자값** (Mọi giá trị thuộc tính phải là giá trị nguyên tử) | **도 (Đô)** | Không cho phép thuộc tính lặp lại hoặc chứa mảng/danh sách giá trị trong cùng một ô. |
  | **1NF $\rightarrow$ 2NF** | **부분적 함수 종속 제거** (Loại bỏ phụ thuộc hàm từng phần) | **부 (Bu)** | Mọi thuộc tính không khóa phải phụ thuộc hàm hoàn toàn (`완전 함수 종속`) vào toàn bộ khóa chính (đặc biệt khi khóa chính là khóa kết hợp gồm nhiều cột). |
  | **2NF $\rightarrow$ 3NF** | **이행적 함수 종속 제거** (Loại bỏ phụ thuộc hàm bắc cầu) | **이 (I)** | Không cho phép chuỗi phụ thuộc gián tiếp qua thuộc tính không khóa ($X \rightarrow Y$ và $Y \rightarrow Z$ kéo theo $X \rightarrow Z$). |
  | **3NF $\rightarrow$ BCNF** | **결정자이면서 후보키가 아닌 것 제거** (Mọi yếu tố quyết định phải là khóa ứng viên) | **결 (Gyeol)** | Dạng chuẩn Boyce-Codd (BCNF). Nếu thuộc tính $A$ quyết định thuộc tính $B$ ($A \rightarrow B$) thì $A$ bắt buộc phải là một Khóa ứng viên (`후보키`). |
  | **BCNF $\rightarrow$ 4NF** | **다치 종속 제거** (Loại bỏ phụ thuộc đa trị - MVD) | **다 (Da)** | Khử bỏ hiện tượng một thuộc tính xác định một tập nhiều giá trị độc lập ($A \twoheadrightarrow B$). |
  | **4NF $\rightarrow$ 5NF** | **조인 종속성 이용** (Xử lý phụ thuộc kết nối - JD) | **조 (Jo)** | Phân rã bảo toàn phép kết nối không mất mát thông tin (`무손실 분해 / Lossless Decomposition`). |

- **3. Quy tắc cốt lõi thi trắc nghiệm:**
  - Chuẩn hóa là phân rã **không mất mát thông tin (`무손실 조인 분해`)**.
  - Nhược điểm của chuẩn hóa quá mức: Do bảng bị tách nhỏ nên khi truy vấn dữ liệu cần thực hiện nhiều phép **Join ($\bowtie$)**, dẫn đến **suy giảm hiệu năng truy vấn**.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Chuẩn hóa được thực hiện ở giai đoạn nào?"* $\rightarrow$ **논리적 설계 (Thiết kế logic)** (không phải vật lý hay khái niệm).
  - Đề hỏi: *"Bỏ phụ thuộc hàm bắc cầu để đạt chuẩn nào?"* $\rightarrow$ **3NF** (제3정규형).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa trực quan từ Chưa chuẩn lên 3NF:**
  - **Chưa chuẩn $\rightarrow$ 1NF:** Bảng `SINH_VIEN(MaSV, SoDienThoai)` có 1 sinh viên ghi 2 số điện thoại trong 1 ô `0901, 0902` $\rightarrow$ Tách thành từng hàng riêng lẻ với giá trị đơn nhất (원자값).
  - **1NF $\rightarrow$ 2NF:** Bảng `DANG_KY(MaSV, MaMH, TenMH, Diem)` có Khóa chính là `(MaSV, MaMH)`. Nhưng `TenMH` chỉ phụ thuộc vào `MaMH` (phụ thuộc từng phần) $\rightarrow$ Tách thành 2 bảng: `DANG_KY(MaSV, MaMH, Diem)` và `MON_HOC(MaMH, TenMH)`.
  - **2NF $\rightarrow$ 3NF:** Bảng `NHAN_VIEN(MaNV, TenNV, MaPhong, TenPhong)` có `MaNV -> MaPhong` và `MaPhong -> TenPhong` $\rightarrow$ Tồn tại phụ thuộc bắc cầu `MaNV -> TenPhong` $\rightarrow$ Tách thành `NHAN_VIEN(MaNV, TenNV, MaPhong)` và `PHONG_BAN(MaPhong, TenPhong)`.

### 복습 체크리스트
- [ ] Học thuộc lòng khẩu quyết: 도 - 부 - 이 - 결 - 다 - 조.
- [ ] Định nghĩa được 1NF (nguyên tử), 2NF (khử phụ thuộc từng phần), 3NF (khử phụ thuộc bắc cầu).
- [ ] Giải thích được điều kiện BCNF: mọi quyết định thức đều là khóa ứng viên.
- [ ] Nhớ rõ giai đoạn thực hiện chuẩn hóa: 논리적 설계 단계.
