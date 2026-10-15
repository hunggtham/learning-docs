# 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục tiêu của kỹ thuật Phân vùng CSDL (`파티셔닝 / Partitioning`): Chia tách các bảng và chỉ mục dung lượng khổng lồ thành các đơn vị logic nhỏ hơn nhằm ngăn ngừa suy giảm hiệu năng và tối ưu hóa quản trị dữ liệu.
- Phân biệt chi tiết 5 phương pháp phân vùng bảng chính: **Phân vùng theo phạm vi (`범위 분할 / Range`)**, **Phân vùng theo băm (`해시 분할 / Hash`)**, **Phân vùng theo danh sách (`목록 분할 / List`)**, **Phân vùng kết hợp (`조합 분할 / Composite`)**, và **Phân vùng vòng tròn (`라운드 로빈 / Round Robin`)**.
- Nắm vững các khái niệm cơ bản của Mã hóa cơ sở dữ liệu (`데이터베이스 암호화`): Văn bản gốc (`평문 / Plaintext`), Bản mã (`암호문 / Ciphertext`), Mã hóa (`암호화 / Encryption`), và Giải mã (`복호화 / Decryption`).

## 핵심 키워드 (Từ khóa)
- 파티셔닝 (Phân vùng / Partitioning)
- 범위 분할 (Phân vùng theo khoảng / Range Partitioning)
- 해시 분할 (Phân vùng theo hàm băm / Hash Partitioning)
- 목록 분할 (Phân vùng theo danh sách / List Partitioning)
- 조합 분할 (Phân vùng kết hợp / Composite Partitioning)
- 라운드 로빈 분할 (Phân vùng xoay vòng / Round Robin Partitioning)
- 암호화 (Mã hóa / Encryption)
- 복호화 (Giải mã / Decryption)
- 평문 (Văn bản gốc / Plaintext) / 암호문 (Bản mã / Ciphertext)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([36-bai-hoc.md](36-bai-hoc.md), [37-bai-hoc.md](37-bai-hoc.md)):** Để quản lý các bảng giao dịch khổng lồ trên hệ thống lưu trữ SAN/NAS mà không bị nghẽn I/O, kỹ sư bắt buộc phải áp dụng kỹ thuật phân vùng bảng.
- **Tiếp nối sang bài sau ([39-bai-hoc.md](39-bai-hoc.md)):** Sau khi hiểu khái niệm mã hóa cơ bản, bài học tiếp theo sẽ đi sâu vào các thuật toán mã hóa đối xứng (DES, AES), bất đối xứng (RSA) và các mô hình kiểm soát truy cập (DAC, MAC, RBAC).

## 읽는 방법 (Cách đọc)
- Học thuộc bảng 5 phương pháp phân vùng ở TẦNG A:
  - Chia theo ngày, tháng, năm $\rightarrow$ **범위 분할 (Range Partitioning)**.
  - Dùng hàm băm để dàn đều dữ liệu, không đoán trước được vị trí $\rightarrow$ **해시 분할 (Hash Partitioning)**.
  - Chia theo nhóm cụ thể (Quốc gia, Khu vực) $\rightarrow$ **목록 분할 (List Partitioning)**.
  - Chia Range trước rồi chia Hash sau $\rightarrow$ **조합 분할 (Composite Partitioning)**.
  - Chia đều tuần tự lần lượt, **không cần khóa chính** $\rightarrow$ **라운드 로빈 (Round Robin Partitioning)**.

---

## 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Khái niệm và Lợi ích của Phân vùng (파티셔닝의 개요):**
  - Là kỹ thuật chia nhỏ một bảng hoặc một chỉ mục có dung lượng cực lớn (hàng chục triệu dòng) thành các khối logic nhỏ hơn gọi là các **Phân vùng (`파티션 / Partition`)**.
  - **Lợi ích kỹ thuật:** Tránh hiện tượng suy giảm hiệu năng do kích thước bảng quá lớn, tăng tốc độ quét dữ liệu nhờ kỹ thuật Partition Pruning (chỉ quét các phân vùng cần thiết), và thuận tiện trong việc sao lưu / xóa dữ liệu định kỳ.
- **2. Bảng phân loại 5 phương pháp Phân vùng trong đề thi (파티션 5대 종류):**
  | Phương pháp | Thuật ngữ tiếng Hàn & Anh | Cơ chế phân chia dữ liệu | Dấu hiệu nhận diện trong đề thi |
  |---|---|---|---|
  | **Phân vùng phạm vi** | `범위 분할` (Range Partitioning) | Dựa theo **khoảng giá trị liên tục** của một hoặc nhiều cột chỉ định (như ngày tháng, số thứ tự). | Đề thi nhắc đến phân chia theo: ngày, tháng, quý, năm (`일별, 월별, 분기별`). |
  | **Phân vùng băm** | `해시 분할` (Hash Partitioning) | Áp dụng **hàm băm (Hash function)** lên giá trị của cột để tính toán vị trí phân vùng; dữ liệu được phân bố đồng đều ngẫu nhiên. | Khắc phục hiện tượng dữ liệu bị dồn cục bộ của Range; dùng cho các cột có dữ liệu đồng đều như **Mã khách hàng, Số CCCD (`고객번호, 주민번호`)**. Không thể dự đoán dữ liệu nằm ở đâu. |
  | **Phân vùng danh sách** | `목록 분할` (List Partitioning) | Phân chia dựa trên **danh sách các giá trị rời rạc cụ thể** được người quản trị định nghĩa trước. | Đề thi nhắc đến việc gom nhóm theo danh sách: Tên Quốc gia (`한국, 미국, 일본`), Khu vực địa lý (`Châu Á, Châu Âu`). |
  | **Phân vùng kết hợp** | `조합 분할` (Composite Partitioning) | Kết hợp hai cấp phân vùng: **Phân vùng theo phạm vi (Range) trước, sau đó áp dụng hàm băm (Hash) để chia nhỏ tiếp**. | Dùng khi một phân vùng theo Range có kích thước vẫn quá lớn khiến việc quản lý gặp khó khăn. |
  | **Phân vùng xoay vòng** | `라운드 로빈 분할` (Round Robin Partitioning) | Phân bổ các bản ghi dữ liệu lần lượt xoay vòng đều nhau vào các phân vùng theo thứ tự xuất hiện. | **Tuyệt đối không cần Khóa chính (`기본키가 필요 없음`)**, các bản ghi được chia đều đồng nhất. |

- **3. Khái niệm nền tảng về Mã hóa dữ liệu (데이터베이스 암호화):**
  - **평문 (Plaintext - Văn bản gốc):** Dữ liệu rõ ràng ban đầu chưa qua xử lý bảo mật.
  - **암호문 (Ciphertext - Bản mã):** Dữ liệu sau khi bị biến đổi để người không có thẩm quyền không thể đọc hiểu được.
  - **암호화 (Encryption - Quá trình mã hóa):** Quá trình chuyển đổi từ Plaintext sang Ciphertext bằng thuật toán và khóa bí mật.
  - **복호화 (Decryption - Quá trình giải mã):** Quá trình chuyển đổi ngược lại từ Ciphertext về Plaintext.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Phương pháp phân vùng nào không cần đến khóa chính (Primary Key)?"* $\rightarrow$ Đáp án: **라운드 로빈 분할 (Round Robin Partitioning)**.
  - Đề hỏi: *"Phương pháp phân vùng nào thích hợp nhất để chia đều dữ liệu theo cột Số CCCD?"* $\rightarrow$ Đáp án: **해시 분할 (Hash Partitioning)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật Partition Pruning (Cắt tỉa phân vùng):**
  - Giả sử bảng `HOA_DON` được phân vùng theo Range cột `NgayTao` (mỗi tháng một phân vùng: `P_202501`, `P_202502`, ...).
  - Khi người dùng chạy câu lệnh `SELECT * FROM HOA_DON WHERE NgayTao BETWEEN '2025-01-01' AND '2025-01-31'`:
    - Bộ tối ưu hóa truy vấn (Optimizer) chỉ quét duy nhất phân vùng `P_202501` và bỏ qua hoàn toàn các phân vùng còn lại.
    - Giúp giảm 90% khối lượng I/O ổ đĩa so với việc phải quét toàn bộ bảng khổng lồ.

### 복습 체크리스트
- [ ] Phân biệt rõ 5 loại phân vùng: 범위, 해시, 목록, 조합, 라운드 로빈 분할.
- [ ] Nhớ kỹ 라운드 로빈 분할 không cần 기본키 (Primary Key).
- [ ] Nêu ví dụ điển hình của 해시 분할 (고객번호, 주민번호).
- [ ] Định nghĩa chính xác 4 thuật ngữ: 평문, 암호문, 암호화, 복호화.
