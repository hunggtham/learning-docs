# 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

## 학습 목표 (Mục tiêu)
- Tổng hợp và đối chiếu mối quan hệ hữu cơ giữa 5 loại Khóa (`키`) và 4 ràng buộc Toàn vẹn dữ liệu (`무결성 제약조건`) trong CSDL quan hệ.
- Nắm vững tiêu chí lựa chọn Khóa chính (`기본키`) từ tập các Khóa ứng viên (`후보키`): không chứa giá trị NULL, ít thay đổi giá trị, số lượng thuộc tính tối thiểu.
- Phân tích chi tiết quy tắc vận hành của Khóa ngoại (`외래키`) và cơ chế đảm bảo Toàn vẹn tham chiếu (`참조 무결성`) khi thực hiện các thao tác Thêm, Sửa, Xóa.

## 핵심 키워드 (Từ khóa)
- 키 (Khóa / Key)
- 무결성 (Tính toàn vẹn / Integrity)
- 슈퍼키 (Siêu khóa / Super Key)
- 후보키 (Khóa ứng viên / Candidate Key)
- 기본키 (Khóa chính / Primary Key)
- 대체키 (Khóa thay thế / Alternate Key)
- 외래키 (Khóa ngoại / Foreign Key)
- 개체 무결성 (Toàn vẹn thực thể / Entity Integrity)
- 참조 무결성 (Toàn vẹn tham chiếu / Referential Integrity)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([11-bai-hoc.md](11-bai-hoc.md), [12-bai-hoc.md](12-bai-hoc.md), [13-bai-hoc.md](13-bai-hoc.md)):** Khóa không chỉ là công cụ tìm kiếm dữ liệu mà còn là cơ chế bảo vệ tính toàn vẹn ở tầng Lược đồ khái niệm (`개념 스키마`).
- **Tiếp nối sang các bài sau ([15-bai-hoc.md](15-bai-hoc.md), [16-bai-hoc.md](16-bai-hoc.md)):** Nền tảng về Khóa và Toàn vẹn là điều kiện tiên quyết để thực hiện các phép kết nối bảng (`Join`) trong đại số quan hệ và kỹ thuật Chuẩn hóa dữ liệu (`정규화`).

## 읽는 방법 (Cách đọc)
- Ôn lại bảng so sánh Khóa ở TẦNG A: Ghi nhớ tiêu chí phân biệt **Siêu khóa** (chỉ cần duy nhất) vs **Khóa ứng viên** (cần cả duy nhất và tối thiểu).
- Khắc sâu cặp bài trùng: **Khóa chính $\leftrightarrow$ Toàn vẹn thực thể**; **Khóa ngoại $\leftrightarrow$ Toàn vẹn tham chiếu**.

---

## 14. 키(Key)의 종류와 데이터베이스 무결성 (Các loại Khóa & Tính Toàn vẹn)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 5 loại Khóa trong mô hình quan hệ:**
  | Tên Khóa | Bản chất kỹ thuật | Tính duy nhất (유일성) | Tính tối thiểu (최소성) | Quy tắc giá trị |
  |---|---|:---:|:---:|---|
  | **슈퍼키 (Super Key)** | Bất kỳ tập thuộc tính nào giúp phân biệt duy nhất từng hàng | **O** | **X** | Chứa thuộc tính dư thừa ngoài tiêu chí nhận diện |
  | **후보키 (Candidate Key)** | Tập thuộc tính vừa đủ nhỏ nhất để phân biệt duy nhất từng hàng | **O** | **O** | Không chứa bất kỳ thuộc tính dư thừa nào |
  | **기본키 (Primary Key)** | Khóa ứng viên được quản trị viên chọn làm định danh chính | **O** | **O** | **Tuyệt đối cấm NULL và cấm trùng lặp** |
  | **대체키 (Alternate Key)** | Các Khóa ứng viên còn lại không được chọn làm Khóa chính | **O** | **O** | Giữ vai trò khóa dự phòng (Secondary Key) |
  | **외래키 (Foreign Key)** | Thuộc tính tham chiếu đến Khóa chính của quan hệ cha | - | - | **Chỉ được mang giá trị tồn tại ở bảng cha hoặc NULL** |

- **2. Bốn ràng buộc Toàn vẹn dữ liệu bắt buộc (무결성 제약조건):**
  - **개체 무결성 (Entity Integrity - Toàn vẹn thực thể):**
    - Quy định: Thuộc tính cấu thành Khóa chính (`기본키`) **không được phép nhận giá trị NULL** và **không được trùng lặp**.
    - Mục đích: Đảm bảo mọi thực thể trong bảng luôn có thể định danh rõ ràng.
  - **참조 무결성 (Referential Integrity - Toàn vẹn tham chiếu):**
    - Quy định: Giá trị của Khóa ngoại (`외래키`) trong bảng con bắt buộc phải bằng một giá trị Khóa chính (`기본키`) đang thực sự tồn tại ở bảng cha, hoặc phải mang giá trị `NULL`.
    - Mục đích: Tránh hiện tượng bản ghi con mồ côi (trỏ đến bản ghi cha không tồn tại).
  - **도메인 무결성 (Domain Integrity - Toàn vẹn miền):**
    - Quy định: Giá trị của mỗi thuộc tính phải nằm trong tập hợp các giá trị hợp lệ đã được quy định sẵn (kiểu dữ liệu, định dạng, độ dài, khoảng giá trị cho phép).
  - **사용자 정의 무결성 (User-Defined Integrity - Toàn vẹn người dùng định nghĩa):**
    - Quy định: Dữ liệu phải tuân thủ các quy tắc nghiệp vụ thực tế do người dùng / lập trình viên chỉ định (ví dụ: ngày kết thúc khóa học phải sau ngày bắt đầu).
- **주의/함정 (Điểm lưu ý thi cử):**
  - Khóa ngoại có thể tham chiếu đến chính khóa chính của cùng bảng đó (Đệ quy / Self-referencing, ví dụ: cột `MaQuanLy` tham chiếu đến `MaNV`).
  - Khi xóa một hàng ở bảng cha, nếu bảng con đang tham chiếu đến thì hệ thống sẽ: Chặn xóa (`RESTRICT`), hoặc xóa luôn con (`CASCADE`), hoặc chuyển con thành rỗng (`SET NULL`).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa Khóa và Toàn vẹn trong mô hình thực tế:**
  - Hãy xét hệ thống quản lý sinh viên:
    - Bảng `KHOA(MaKhoa [PK], TenKhoa)`
    - Bảng `SINH_VIEN(MaSV [PK], HoTen, MaKhoa [FK], Email [AK])`
  - Nếu ta thêm sinh viên mới với `MaSV = NULL` $\rightarrow$ Vi phạm **개체 무결성 (Toàn vẹn thực thể)**.
  - Nếu ta thêm sinh viên mới với `MaKhoa = 'K99'` trong khi bảng `KHOA` chưa có khoa này $\rightarrow$ Vi phạm **참조 무결성 (Toàn vẹn tham chiếu)**.
  - Nếu cột `Email` là một Khóa thay thế (`대체키`), nó vẫn đảm bảo tính duy nhất và tính tối thiểu, nhưng được dùng cho việc tra cứu phụ.

### 복습 체크리스트
- [ ] Trình bày rõ điểm giống và khác nhau giữa 슈퍼키 và 후보키.
- [ ] Nêu 2 điều kiện bất biến của 기본키 (không NULL, không trùng lặp).
- [ ] Giải thích ràng buộc của 외래키 đối với bảng tham chiếu (Toàn vẹn tham chiếu).
- [ ] Phân biệt rõ 개체 무결성 và 참조 무결성.
