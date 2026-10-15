# 16. 정규화(Normalization)와 이상 현상(Anomaly)

## 학습 목표 (Mục tiêu)
- Nắm vững mối quan hệ nhân quả trực tiếp giữa Hiện tượng dị thường dữ liệu (`이상 현상 / Anomaly`) và kỹ thuật Chuẩn hóa (`정규화 / Normalization`).
- Nhận diện chính xác 3 loại dị thường: Dị thường Thêm (`삽입 이상`), Dị thường Xóa (`삭제 이상`), và Dị thường Cập nhật (`갱신 이상`).
- Khắc ghi bảng điều kiện và khẩu quyết ghi nhớ 6 cấp độ chuẩn hóa: 1NF (Nguyên tử) $\rightarrow$ 2NF (Khử phụ thuộc phần) $\rightarrow$ 3NF (Khử phụ thuộc bắc cầu) $\rightarrow$ BCNF (Yếu tố quyết định là khóa ứng viên) $\rightarrow$ 4NF (Khử đa trị) $\rightarrow$ 5NF (Phụ thuộc kết nối).

## 핵심 키워드 (Từ khóa)
- 정규화 (Chuẩn hóa / Normalization)
- 이상 현상 (Dị thường / Anomaly)
- 삽입 이상 (Dị thường thêm / Insertion Anomaly)
- 삭제 이상 (Dị thường xóa / Deletion Anomaly)
- 갱신 이상 (Dị thường cập nhật / Update Anomaly)
- 완전 함수 종속 (Phụ thuộc hàm hoàn toàn / Full Functional Dependency)
- 부분 함수 종속 (Phụ thuộc hàm từng phần / Partial Functional Dependency)
- 이행적 함수 종속 (Phụ thuộc hàm bắc cầu / Transitive Functional Dependency)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([17-bai-hoc.md](17-bai-hoc.md), [18-bai-hoc.md](18-bai-hoc.md), [19-bai-hoc.md](19-bai-hoc.md)):** Chuẩn hóa là giải pháp cốt lõi để loại bỏ dị thường và bảo vệ tính toàn vẹn dữ liệu ở tầng thiết kế logic, trước khi được chuyển sang giai đoạn tối ưu hóa truy vấn vật lý.
- **Tiếp nối sang các bài sau ([21-bai-hoc.md](21-bai-hoc.md), [22-bai-hoc.md](22-bai-hoc.md)):** Sau khi chuẩn hóa đạt các dạng chuẩn cao, khi triển khai vào thực tế cần phối hợp với bộ tối ưu hóa truy vấn (Optimizer: RBO, CBO) và cân nhắc Phi chuẩn hóa (`반정규화`) để đảm bảo tốc độ phản hồi của hệ thống.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng tóm tắt 3 loại Dị thường:
  - Thêm dữ liệu không mong muốn $\rightarrow$ **삽입 이상**.
  - Xóa mất thông tin quan trọng ngoài ý muốn $\rightarrow$ **삭제 이상**.
  - Cập nhật một phần gây mâu thuẫn $\rightarrow$ **갱신 이상**.
- Thuộc làu câu thần chú ghi nhớ 6 cấp độ chuẩn hóa tiếng Hàn: **도 - 부 - 이 - 결 - 다 - 조**.

---

## 16. 정규화(Normalization)와 이상 현상(Anomaly)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Ba loại Dị thường dữ liệu bắt buộc ghi nhớ (이상 현상 3가지):**
  | Tên Dị thường | Thuật ngữ Hàn - Anh | Khái niệm & Cơ chế phát sinh | Ví dụ nhận diện trong đề thi |
  |---|---|---|---|
  | **Dị thường Thêm** | `삽입 이상` (Insertion Anomaly) | Khi thêm một bản ghi mới, người dùng buộc phải thêm cả những dữ liệu không mong muốn hoặc không có sẵn do cấu trúc bảng gộp chung. | Thêm một khoa mới nhưng chưa tuyển được sinh viên nào, do cột MãSV là khóa chính nên không được phép chèn bản ghi. |
  | **Dị thường Xóa** | `삭제 이상` (Deletion Anomaly) | Khi xóa một dữ liệu không cần thiết, kéo theo các thông tin có giá trị khác cùng nằm trên hàng đó bị xóa liên đới dây chuyền (`연쇄 삭제`). | Xóa thông tin một sinh viên thôi học dẫn đến mất luôn toàn bộ thông tin về ngành học và giảng viên hướng dẫn của ngành đó. |
  | **Dị thường Cập nhật** | `갱신 이상` (Update Anomaly) | Khi sửa đổi một thuộc tính bị trùng lặp ở nhiều hàng, nếu chỉ sửa đổi một số hàng mà sót các hàng khác sẽ sinh ra mâu thuẫn dữ liệu (`정보 불일치 / 모순`). | Đổi số điện thoại của trưởng khoa nhưng chỉ sửa ở 1 hàng sinh viên, các hàng sinh viên khác vẫn giữ số cũ. |

- **2. Bảng 6 cấp độ Chuẩn hóa theo chuẩn đề thi:**
  | Cấp độ | Điều kiện bắt buộc (Hàn - Việt) | Ý nghĩa kỹ thuật | Mẹo nhớ |
  |---|---|---|:---:|
  | **1NF** | **도메인이 원자값** (Domain là giá trị nguyên tử) | Khử các thuộc tính lặp lại hoặc đa trị, mỗi ô chỉ chứa 1 giá trị duy nhất | **도** |
  | **2NF** | **부분적 함수 종속 제거** (Khử phụ thuộc hàm từng phần) | Tất cả các thuộc tính không khóa phải phụ thuộc hoàn toàn vào toàn bộ khóa chính | **부** |
  | **3NF** | **이행적 함수 종속 제거** (Khử phụ thuộc hàm bắc cầu) | Loại bỏ mối phụ thuộc gián tiếp qua thuộc tính không khóa ($A \rightarrow B, B \rightarrow C$) | **이** |
  | **BCNF** | **결정자이면서 후보키가 아닌 것 제거** (Mọi quyết định thức là khóa ứng viên) | Chuẩn Boyce-Codd nâng cao: Mọi thuộc tính quyết định ($X \rightarrow Y$) đều phải là một Candidate Key | **결** |
  | **4NF** | **다치 종속 제거** (Khử phụ thuộc đa trị - MVD) | Khử bỏ hiện tượng một thuộc tính độc lập kéo theo một tập nhiều giá trị ($A \twoheadrightarrow B$) | **다** |
  | **5NF** | **조인 종속성 이용** (Xử lý phụ thuộc phép kết nối - JD) | Đảm bảo khi tách thành nhiều bảng con, dùng phép kết nối tự nhiên có thể tái tạo lại bảng ban đầu không tổn thất | **조** |
- **Khẩu quyết ghi nhớ kinh điển:**
  > **도 - 부 - 이 - 결 - 다 - 조** (Đồ - Bu - I - Gyeol - Da - Jo: Đô-main nguyên tử $\rightarrow$ Bỏ từng phần $\rightarrow$ Bỏ bắc cầu $\rightarrow$ Quyết định thức $\rightarrow$ Bỏ đa trị $\rightarrow$ Bỏ phụ thuộc Join).
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Điều kiện để đạt 2NF từ 1NF là gì?"* $\rightarrow$ Đáp án: **완전 함수 종속 만족 (Thỏa mãn phụ thuộc hàm hoàn toàn)** hoặc **부분적 함수 종속 제거 (Loại bỏ phụ thuộc hàm từng phần)**.
  - Đề hỏi: *"Mục đích cốt lõi của việc chuẩn hóa là gì?"* $\rightarrow$ Đáp án: **데이터 중복 배제 및 이상 현상 방지 (Loại bỏ dư thừa dữ liệu và ngăn ngừa dị thường)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế phụ thuộc hàm từng phần (부분 함수 종속) trong 2NF:**
  - Giả sử bảng có Khóa chính phức hợp gồm 2 cột: `(MãSV, MãMH)`.
  - Cột `ĐiểmThi` phụ thuộc vào cả `(MãSV, MãMH)` $\rightarrow$ Đây là **Phụ thuộc hàm hoàn toàn (`완전 함수 종속`)**.
  - Cột `TênSV` chỉ phụ thuộc vào một phần của khóa chính là `MãSV` $\rightarrow$ Đây là **Phụ thuộc hàm từng phần (`부분 함수 종속`)**.
  - Để đạt 2NF, bắt buộc phải tách `TênSV` ra một bảng độc lập `SINH_VIEN(MãSV, TênSV)`.
- **Cơ chế phụ thuộc bắc cầu (이행적 함수 종속) trong 3NF:**
  - Khóa chính: `MãSV`.
  - Ta có: `MãSV -> MãKhoa` (Mỗi sinh viên thuộc về một khoa).
  - Và: `MãKhoa -> TênKhoa` (Mỗi mã khoa có tên khoa tương ứng).
  - Suy ra: `MãSV -> TênKhoa` thông qua thuộc tính trung gian `MãKhoa`.
  - Để đạt 3NF, phải tách bảng thành: `SINH_VIEN(MãSV, MãKhoa)` và `KHOA(MãKhoa, TênKhoa)`.

### 복습 체크리스트
- [ ] Phân biệt được 3 hiện tượng dị thường: 삽입 이상, 삭제 이상, 갱신 이상.
- [ ] Nhớ chính xác khẩu quyết 6 bước: 도 - 부 - 이 - 결 - 다 - 조.
- [ ] Giải thích được khái niệm 완전 함수 종속 và 부분 함수 종속.
- [ ] Trình bày được định nghĩa của 이행적 함수 종속 ($A \rightarrow B, B \rightarrow C \implies A \rightarrow C$).
