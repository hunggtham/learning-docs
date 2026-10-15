# 184-185. 반정규화 (Denormalization)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và động cơ kỹ thuật của Phi chuẩn hóa (`반정규화 / Denormalization` / 역정규화): Cố tình vi phạm các quy tắc chuẩn hóa nhằm nâng cao hiệu năng truy vấn (`시스템 성능 향상`) và tạo thuận tiện trong vận hành.
- Phân tích chi tiết 4 phương pháp phi chuẩn hóa chính: Gộp bảng (`테이블 통합`), Chia bảng (`테이블 분할`), Thêm bảng trùng lặp (`중복 테이블 추가`), và Thêm thuộc tính trùng lặp (`중복 속성 추가`).
- Nhận thức rõ sự đánh đổi (Trade-off): Tăng tốc độ đọc nhưng làm tăng dung lượng lưu trữ, giảm tính nhất quán (`일관성 저하`) và tăng rủi ro dị thường khi cập nhật.

## 핵심 키워드 (Từ khóa)
- 반정규화 (Phi chuẩn hóa / Denormalization / 역정규화)
- 성능 향상 (Tăng hiệu năng hệ thống)
- 테이블 통합 (Gộp bảng / Table Integration)
- 테이블 분할 (Chia bảng / Table Partitioning: 수평 분할, 수직 분할)
- 중복 테이블 추가 (Thêm bảng trùng lặp / Redundant Table)
- 중복 속성 추가 (Thêm thuộc tính trùng lặp / Redundant Attribute)
- 집계 테이블 (Bảng tổng hợp / Aggregation Table)
- 데이터 일관성 (Tính nhất quán dữ liệu / Consistency)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([16-bai-hoc.md](16-bai-hoc.md), [17-bai-hoc.md](17-bai-hoc.md), [18-bai-hoc.md](18-bai-hoc.md)):** Chuẩn hóa triệt để giúp loại bỏ hoàn toàn dị thường nhưng lại phân mảnh dữ liệu thành nhiều bảng, khiến các câu truy vấn phức tạp phải thực hiện hàng loạt phép Join ($\bowtie$) làm chậm hệ thống.
- **Tiếp nối sang các bài sau ([20-bai-hoc.md](20-bai-hoc.md), [21-bai-hoc.md](21-bai-hoc.md)):** Phi chuẩn hóa là một kỹ thuật tối ưu hóa then chốt trong thiết kế cơ sở dữ liệu thực tế, đặc biệt đối với các hệ thống phân tích dữ liệu lớn và báo cáo tổng hợp (Data Warehouse / OLAP).

## 읽는 방법 (Cách đọc)
- Nhớ câu định nghĩa chuẩn trong đề thi: **"Cố ý vi phạm nguyên tắc chuẩn hóa để tăng hiệu năng" $\rightarrow$ 반정규화**.
- Phân biệt 2 cách chia bảng:
  - Chia theo hàng (Record) $\rightarrow$ **수평 분할 (Horizontal Partitioning)**.
  - Chia theo cột (Attribute) $\rightarrow$ **수직 분할 (Vertical Partitioning)**.

---

## 184-185. 반정규화 (Denormalization)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa và Bản chất của Phi chuẩn hóa (반정규화의 개념):**
  - Là quá trình tích hợp, nhân bản hoặc phân chia lại các mô hình dữ liệu đã được chuẩn hóa nhằm **cải thiện tốc độ truy vấn** và đơn giản hóa quá trình phát triển ứng dụng.
  - Bản chất: **Cố tình vi phạm các nguyên tắc chuẩn hóa (`의도적으로 정규화 원칙을 위배`)**.
  - Trước khi thực hiện phi chuẩn hóa, kỹ sư bắt buộc phải cân nhắc giữa: **Tính nhất quán & toàn vẹn dữ liệu** đối trọng với **Tốc độ truy xuất hệ thống**.
- **2. Bốn kỹ thuật Phi chuẩn hóa chính (반정규화 4대 방법):**
  | Phương pháp | Thuật ngữ Hàn - Anh | Kỹ thuật chi tiết | Mục đích tối ưu |
  |---|---|---|---|
  | **Gộp bảng** | `테이블 통합` (Table Integration) | - Gộp 2 bảng có quan hệ 1:1; Gộp 2 bảng 1:N nếu luôn luôn được truy vấn cùng nhau; Gộp bảng Supertype / Subtype. | Loại bỏ hoàn toàn chi phí thực hiện phép Join giữa các bảng liên quan. |
  | **Chia bảng** | `테이블 분할` (Table Partitioning) | - **수평 분할 (Chia ngang):** Phân chia bảng dựa theo số bản ghi/hàng (ví dụ: tách theo năm giao dịch, theo chi nhánh); **수직 분할 (Chia dọc):** Phân chia bảng dựa theo danh sách thuộc tính/cột khi bảng có quá nhiều cột, tách cột ít dùng hoặc cột bảo mật lớn ra riêng. | Giảm khối lượng I/O ổ đĩa khi quét bảng; tối ưu vùng đệm bộ nhớ (Buffer pool). |
  | **Thêm bảng trùng lặp** | `중복 테이블 추가` (Redundant Table) | - **집계 테이블 (Bảng tổng hợp):** Lưu sẵn kết quả SUM, AVG, COUNT; **진행 테이블 (Bảng tiến trình):** Lưu trạng thái xử lý tạm thời; **특정 부분 테이블 (Bảng trích đoạn):** Lưu trước một tập dữ liệu con thường xuyên truy vấn. | Tránh việc phải tính toán lại từ đầu trên khối lượng dữ liệu khổng lồ mỗi khi có người dùng xem báo cáo. |
  | **Thêm thuộc tính trùng lặp** | `중복 속성 추가` (Redundant Attribute) | Thêm một cột của bảng khác vào bảng hiện tại (ví dụ: lưu luôn `TenKhoa` vào bảng `SINH_VIEN`). | Rút ngắn lộ trình truy vấn, loại bỏ lệnh Join phụ khi chỉ cần lấy 1 vài trường dữ liệu. |

- **3. Nhược điểm và rủi ro của Phi chuẩn hóa:**
  - Làm tăng nguy cơ xuất hiện lại **3 loại dị thường dữ liệu (Thêm, Xóa, Sửa)**.
  - Làm **giảm tính nhất quán và tính chính xác** của dữ liệu (`일관성 및 정합성 저하`).
  - Tốn thêm dung lượng lưu trữ trên đĩa cứng.
  - **Phi chuẩn hóa quá đà (`과도한 반정규화`)** sẽ phản tác dụng, khiến chi phí cập nhật dữ liệu tăng vọt và làm giảm hiệu năng chung của hệ thống.
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Phi chuẩn hóa có luôn luôn làm tăng hiệu năng hệ thống không?"* $\rightarrow$ **KHÔNG**, phi chuẩn hóa quá đà sẽ làm chậm hệ thống do overhead ghi và bảo trì dữ liệu trùng lặp.
  - Đề hỏi: *"Chia bảng theo dòng (Record) gọi là gì?"* $\rightarrow$ Đáp án: **수평 분할 (Phân vùng ngang / Horizontal Partitioning)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ minh họa kỹ thuật Thêm cột trùng lặp:**
  - Mô hình chuẩn hóa:
    - `DON_HANG(MaDH, NgayDat, MaKH)`
    - `KHACH_HANG(MaKH, TenKH, SoDienThoai)`
  - Mỗi khi hiển thị danh sách đơn hàng cho nhân viên giao vận, hệ thống bắt buộc phải `JOIN` bảng `DON_HANG` với `KHACH_HANG` chỉ để lấy mỗi tên khách hàng.
  - Áp dụng phi chuẩn hóa: Thêm trực tiếp cột `TenKH` vào bảng `DON_HANG`.
    - Kết quả: Câu truy vấn `SELECT MaDH, NgayDat, TenKH FROM DON_HANG` chạy ngay lập tức mà không cần bất kỳ phép Join nào.
    - Đánh đổi: Nếu khách hàng đổi tên, hệ thống phải cập nhật ở cả 2 bảng; nếu quên cập nhật ở bảng đơn hàng sẽ gây mâu thuẫn dữ liệu.

### 복습 체크리스트
- [ ] Nắm vững định nghĩa 반정규화: cố tình vi phạm chuẩn hóa để tăng tốc độ hệ thống.
- [ ] Kể tên 4 kỹ thuật phi chuẩn hóa: 테이블 통합, 테이블 분할, 중복 테이블 추가, 중복 속성 추가.
- [ ] Phân biệt được 수평 분할 (chia theo hàng) và 수직 분할 (chia theo cột).
- [ ] Giải thích được tại sao quá lạm dụng phi chuẩn hóa (과도한 반정규화) lại làm chậm hệ thống.
