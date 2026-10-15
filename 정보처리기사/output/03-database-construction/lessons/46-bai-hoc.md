# 194. 파티션 (Partition)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và ý nghĩa của việc phân chia phân vùng (`파티션 / Partition`): Phân tách các bảng hoặc chỉ mục có dung lượng khổng lồ thành các đơn vị logic nhỏ hơn nhằm nâng cao hiệu năng truy vấn và đơn giản hóa công tác quản trị dữ liệu.
- Phân biệt chi tiết 5 loại hình phân vùng dữ liệu: **Phân vùng phạm vi (`범위 분할 / Range`)**, **Phân vùng băm (`해시 분할 / Hash`)**, **Phân vùng danh sách (`목록 분할 / List`)**, **Phân vùng kết hợp (`조합 분할 / Composite`)**, và **Phân vùng xoay vòng (`라운드 로빈 / Round Robin`)**.
- Nhận thức rõ các lợi ích thực tế: Nâng cao hiệu suất I/O đĩa nhờ cơ chế lọc bỏ phân vùng (Partition Pruning), và Tối ưu hóa thời gian sao lưu (Backup) và phục hồi (Recovery).

## 핵심 키워드 (Từ khóa)
- 파티션 (Phân vùng / Partition)
- 대용량 데이터베이스 (Cơ sở dữ liệu dung lượng lớn)
- 범위 분할 (Phân vùng theo khoảng / Range Partitioning)
- 해시 분할 (Phân vùng theo băm / Hash Partitioning)
- 목록 분할 (Phân vùng theo danh sách / List Partitioning)
- 조합 분할 (Phân vùng kết hợp / Composite Partitioning)
- 라운드 로빈 분할 (Phân vùng xoay vòng / Round Robin Partitioning)
- 파티션 프루닝 (Cắt tỉa phân vùng / Partition Pruning)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([38-bai-hoc.md](38-bai-hoc.md), [45-bai-hoc.md](45-bai-hoc.md)):** Sau khi phân tích ma trận CRUD và xác định các bảng có tần suất ghi nhận dữ liệu hàng triệu dòng mỗi tháng, phân vùng là giải pháp vật lý bắt buộc để duy trì tốc độ cho hệ thống.
- **Tiếp nối sang bài sau ([47-bai-hoc.md](47-bai-hoc.md), [48-bai-hoc.md](48-bai-hoc.md)):** Ở cấp độ dưới của hệ quản trị CSDL, các phân vùng này được ánh xạ trực tiếp lên các tệp dữ liệu và khối đĩa (Data Block) của hệ thống tệp hệ điều hành.

## 읽는 방법 (Cách đọc)
- Học thuộc các dấu hiệu nhận diện trong đề thi trắc nghiệm ở TẦNG A:
  - Chia theo ngày/tháng/quý/năm $\rightarrow$ **범위 분할 (Range)**.
  - Phân bổ đều ngẫu nhiên bằng hàm băm cho cột Số CCCD $\rightarrow$ **해시 분할 (Hash)**.
  - Chia theo danh sách giá trị cố định (Tên vùng, Tên quốc gia) $\rightarrow$ **목록 분할 (List)**.
  - Range trước, Hash sau $\rightarrow$ **조합 분할 (Composite)**.
  - Phân bổ xoay vòng đều nhau, **không cần khóa chính** $\rightarrow$ **라운드 로빈 (Round Robin)**.

---

## 194. 파티션 (Partition)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa và Mục tiêu của Phân vùng (파티션의 정의):**
  - Là kỹ thuật chia tách một bảng dữ liệu hoặc một chỉ mục có dung lượng cực lớn thành nhiều đơn vị vật lý/logic độc lập nhỏ hơn gọi là **Phân vùng (`파티션`)**.
  - **Mục tiêu chính:**
    - Ngăn chặn suy giảm hiệu năng do dung lượng bảng tăng trưởng đột biến.
    - Cho phép quản lý độc lập từng phân vùng (sao lưu, bảo trì, xóa dữ liệu cũ mà không khóa toàn bộ bảng).
    - Cải thiện tốc độ truy vấn nhờ kỹ thuật **Partition Pruning (Cắt tỉa phân vùng)**.
- **2. Bảng phân loại 5 phương pháp Phân vùng theo chuẩn đề thi:**
  | Phương pháp | Thuật ngữ tiếng Hàn & Anh | Tiêu chí phân chia | Đặc điểm thi trắc nghiệm |
  |---|---|---|---|
  | **Phân vùng phạm vi** | `범위 분할` (Range Partitioning) | Dựa trên **khoảng giá trị liên tục** của một cột chỉ định (như ngày tháng tạo bản ghi). | Thường áp dụng chia theo: **ngày, tháng, quý, năm (`일별, 월별, 분기별`)**. Cần chú ý nguy cơ dữ liệu dồn quá nhiều vào phân vùng tháng gần nhất. |
  | **Phân vùng băm** | `해시 분할` (Hash Partitioning) | Áp dụng **hàm băm (Hash function)** lên cột khóa để phân bố dữ liệu vào các phân vùng. | Khắc phục nhược điểm lệch dữ liệu của Range; dữ liệu được dàn đều ngẫu nhiên; **dùng cho cột có độ phân bố đều như Mã khách hàng, Số CCCD**. Không đoán được bản ghi nằm ở phân vùng nào. |
  | **Phân vùng danh sách** | `목록 분할` (List Partitioning) | Dựa trên **danh sách các giá trị rời rạc** được người quản trị chỉ định tường minh. | Dùng khi giá trị cột mang tính phân loại rõ ràng (ví dụ: cột `QuocGia` có các giá trị chia vào danh sách `ChauA`, `ChauAu`). |
  | **Phân vùng kết hợp** | `조합 분할` (Composite Partitioning) | Phân vùng đa cấp: **Áp dụng Range trước để chia theo mốc thời gian, sau đó áp dụng Hash để chia nhỏ tiếp**. | Dùng khi một phân vùng theo tháng vẫn quá lớn (hàng triệu bản ghi), cần băm nhỏ tiếp để tăng tốc song song. |
  | **Phân vùng xoay vòng** | `라운드 로빈 분할` (Round Robin Partitioning) | Phân bổ các bản ghi dữ liệu lần lượt xoay vòng vào các phân vùng theo thứ tự xuất hiện. | **Tuyệt đối không cần Khóa chính (`기본키가 필요 없음`)**, phân phối dữ liệu cân bằng nhất nhưng không hỗ trợ tìm kiếm theo khóa. |

- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Phương pháp phân vùng nào không yêu cầu phải có khóa chính?"* $\rightarrow$ Đáp án: **라운드 로빈 분할 (Round Robin Partitioning)**.
  - Đề hỏi: *"Phân vùng kết hợp (조합 분할) thường là sự kết hợp giữa hai phương pháp nào?"* $\rightarrow$ Đáp án: **범위 분할 (Range) kết hợp với 해시 분할 (Hash)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa cú pháp SQL tạo Range Partition:**
  ```sql
  CREATE TABLE GIAO_DICH (
      MaGD INT,
      NgayGD DATE,
      SoTien DECIMAL(10,2)
  )
  PARTITION BY RANGE (NgayGD) (
      PARTITION p_2025_q1 VALUES LESS THAN ('2025-04-01'),
      PARTITION p_2025_q2 VALUES LESS THAN ('2025-07-01'),
      PARTITION p_max VALUES LESS THAN (MAXVALUE)
  );
  ```
- **Lợi ích khi bảo trì dữ liệu (Data Archiving):**
  - Khi cần xóa dữ liệu giao dịch của 5 năm trước, thay vì chạy lệnh `DELETE FROM GIAO_DICH WHERE NgayGD < '2020-01-01'` (tốn hàng giờ và nghẽn Redo log), DBA chỉ cần chạy lệnh `ALTER TABLE GIAO_DICH DROP PARTITION p_2019` diễn ra trong 0.1 giây.

### 복습 체크리스트
- [ ] Trình bày được mục đích của 파티션 đối với cơ sở dữ liệu lớn.
- [ ] Phân biệt được 5 loại phân vùng: 범위, 해시, 목록, 조합, 라운드 로빈.
- [ ] Nhớ rõ 라운드 로빈 분할 không cần 기본키.
- [ ] Hiểu được khái niệm 조합 분할 (Range + Hash).
