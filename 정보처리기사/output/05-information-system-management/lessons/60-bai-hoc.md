# 페이지 교체 알고리즘과 페이지 크기 (Thuật toán Thay thế Trang & Kích thước Trang)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất của lỗi thiếu trang (Page Fault) và cơ chế hoán đổi trang trong quản lý bộ nhớ ảo.
- Phân biệt các thuật toán thay thế trang kinh điển: Tối ưu lý thuyết (OPT), Nhập trước xuất trước (FIFO) và Nghịch lý Belady, Ít sử dụng gần đây nhất (LRU), Tần suất sử dụng thấp nhất (LFU), và Chưa sử dụng gần đây (NUR).
- Phân tích chi tiết quy tắc 2 bit trạng thái (Reference bit, Modified bit) trong thuật toán NUR.
- Đánh giá sự đánh đổi hai chiều (Trade-offs) khi thiết kế kích thước trang bộ nhớ (Page Size) Lớn vs Nhỏ.

## 핵심 키워드 (Từ khóa)
- **페이지 부재 (Page Fault)**: Sự kiện CPU cần truy xuất một trang nhớ nhưng trang đó chưa được nạp vào RAM.
- **페이지 교체 알고리즘 (Page Replacement)**: OPT (Tối ưu lý thuyết), FIFO (vào trước ra trước, Belady Anomaly), LRU (thời gian xa nhất), LFU (tần suất ít nhất), NUR (xấp xỉ bằng bit $r, m$).
- **NUR 4 cấp độ**: Cấp 1 $(0, 0)$, Cấp 2 $(0, 1)$, Cấp 3 $(1, 0)$, Cấp 4 $(1, 1)$.
- **페이지 크기 영향 (Page Size Impact)**: Trang nhỏ giảm phân mảnh nhưng tăng kích thước Page Table; Trang lớn giảm I/O nhưng tăng phân mảnh nội vi.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [59-bai-hoc.md](59-bai-hoc.md) (Khái niệm Paging và phân mảnh nội vi).
- Liên kết với [61-bai-hoc.md](61-bai-hoc.md) (Hiện tượng Locality, Working Set và Thrashing).
- Liên kết với [04-programming-language/86-bai-hoc.md](../../04-programming-language/lessons/86-bai-hoc.md) (Thuật toán thay thế trang chi tiết).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh tiêu chí chọn trang thay thế:
  - Nhìn về **tương lai** (không khả thi thực tế) $\rightarrow$ **OPT (Optimal)**.
  - Nhìn về **thời điểm vào** (vào sớm nhất thì ra trước) $\rightarrow$ **FIFO**.
  - Nhìn về **thời gian sử dụng gần nhất** (lâu chưa dùng tới nhất) $\rightarrow$ **LRU**.
  - Đếm **số lần sử dụng** (số lần được gọi ít nhất) $\rightarrow$ **LFU**.
  - Dùng cặp bit kiểm tra (Tham chiếu, Biến đổi) $\rightarrow$ **NUR**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh các Thuật toán Thay thế Trang (Page Replacement)
| Thuật toán (KR / EN) | Tiêu chí chọn trang để loại bỏ | Đặc điểm kỹ thuật & Đánh giá |
| :--- | :--- | :--- |
| **OPT (Optimal Replacement)** | Chọn trang mà trong **tương lai lâu nhất sẽ không được dùng đến** | Tỷ lệ lỗi trang thấp nhất; **Không thể hiện thực hóa** trong thực tế vì không ai đoán trước được tương lai (dùng làm mốc so sánh lý thuyết) |
| **FIFO (First In First Out)** | Chọn trang đã **nằm trong bộ nhớ lâu nhất** (vào trước thì ra trước) | Cài đặt đơn giản bằng hàng đợi (Queue); Mắc phải **Nghịch lý Belady (Belady's Anomaly)**: khi tăng số khung trang, số lỗi trang đôi khi lại tăng lên |
| **LRU (Least Recently Used)** | Chọn trang có **thời gian kể từ lần truy cập cuối cùng là lâu nhất** | Nhìn về quá khứ; hiệu quả cao và được ứng dụng rộng rãi nhất; triển khai bằng Stack hoặc bộ đếm thời gian (Counter) |
| **LFU (Least Frequently Used)** | Chọn trang có **tần suất (số lần) được tham chiếu là ít nhất** | Cần bộ đếm số lần gọi; nhược điểm là trang mới nạp vào dễ bị loại bỏ vì số lần đếm còn thấp |
| **NUR (Not Used Recently)** | Thuật toán xấp xỉ LRU chi phí thấp, phân loại trang dựa trên **Bit tham chiếu ($r$) và Bit biến đổi ($m$)** | Kiểm tra 2 bit: Ưu tiên loại bỏ trang chưa đọc và chưa sửa $(r=0, m=0)$ trước tiên |
| **SCR (Second Chance)** | Cải tiến của FIFO kết hợp bit tham chiếu (Thuật toán đồng hồ Clock) | Nếu trang có bit tham chiếu $= 1$, đặt lại về $0$ và chuyển xuống cuối hàng đợi; nếu bit $= 0$ thì thay thế ngay |

#### 2. Chi tiết 4 cấp độ ưu tiên thay thế trong thuật toán NUR
- Mỗi trang được hệ điều hành gắn 2 bit trạng thái:
  - **Bit tham chiếu ($r$ - Reference Bit)**: Bằng $1$ nếu trang vừa được truy xuất (đọc/ghi), bằng $0$ nếu chưa.
  - **Bit biến đổi ($m$ - Modified/Dirty Bit)**: Bằng $1$ nếu nội dung trang đã bị chỉnh sửa (cần ghi lại đĩa), bằng $0$ nếu chưa sửa.
- Trình tự ưu tiên chọn trang bị thay thế (chọn từ cấp thấp nhất):
  1. **Cấp 1: $(r = 0, m = 0)$** $\rightarrow$ Chưa được tham chiếu gần đây, nội dung không bị sửa (Chi phí thay thế rẻ nhất, không cần ghi đĩa).
  2. **Cấp 2: $(r = 0, m = 1)$** $\rightarrow$ Chưa được tham chiếu gần đây, nhưng nội dung đã bị sửa.
  3. **Cấp 3: $(r = 1, m = 0)$** $\rightarrow$ Mới được tham chiếu gần đây, nội dung chưa bị sửa.
  4. **Cấp 4: $(r = 1, m = 1)$** $\rightarrow$ Mới được tham chiếu gần đây, nội dung đã bị sửa (Trang này có giá trị cao nhất, giữ lại sau cùng).

#### 3. Bảng so sánh Đánh đổi Kích thước Trang (Page Size Trade-offs)
| Tiêu chí xem xét | Khi Kích thước Trang NHỎ (Small Page Size) | Khi Kích thước Trang LỚN (Large Page Size) |
| :--- | :--- | :--- |
| **Phân mảnh nội vi** | **Giảm** (lãng phí ô nhớ ở trang cuối rất nhỏ) | **Tăng** (lãng phí ô nhớ ở trang cuối lớn) |
| **Kích thước Bảng trang (Page Table)** | **Tăng rất lớn** (cần nhiều dòng để quản lý vô số trang nhỏ, tốn RAM) | **Giảm nhỏ gọn** (số dòng ít, tiết kiệm RAM lưu bảng) |
| **Tốc độ dịch địa chỉ** | Chậm hơn do bảng trang quá dài | Nhanh hơn do bảng trang ngắn |
| **Số lần đọc/ghi đĩa (Disk I/O)** | Tăng lên do phải nạp nhiều trang nhỏ lẻ tẻ | Giảm xuống do mỗi lần đọc đưa được cả khối lớn vào RAM |
| **Độ khớp tính cục bộ (Locality)** | **Khớp rất tốt** (chỉ nạp đúng những lệnh thực sự cần chạy) | Kém hơn (dễ nạp thừa các đoạn mã không bao giờ dùng tới) |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán mô phỏng thay thế trang FIFO và Nghịch lý Belady
- Giả sử chuỗi tham chiếu trang: `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`
- Khi cấp 3 khung trang (Frames): Xảy ra **9** lần Page Fault.
- Khi cấp 4 khung trang (Frames): Xảy ra **10** lần Page Fault!
- Hiện tượng tăng thêm khung trang nhưng số lỗi trang lại tăng lên gọi là **Nghịch lý Belady (Belady's Anomaly)**. Thuật toán LRU và OPT không bao giờ mắc phải nghịch lý này nhờ tính chất tập hợp xếp chồng (Stack Algorithm).

---

### 복습 체크리스트
- [ ] Thuật toán OPT có thể được triển khai trực tiếp trong các hệ điều hành thương mại hiện nay không và tại sao?
- [ ] Nghịch lý Belady (Belady's Anomaly) xảy ra với thuật toán thay thế trang nào?
- [ ] Trong thuật toán NUR, trang có cặp bit $(r=0, m=0)$ và trang $(r=1, m=1)$ thì trang nào sẽ bị thay thế trước?
- [ ] Khi giảm kích thước trang (Page Size), kích thước của Bảng quản lý trang (Page Table) sẽ tăng lên hay giảm đi?
