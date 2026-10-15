# 292. 페이지 교체 알고리즘 (Thuật toán thay thế trang / Page Replacement)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế hoạt động và tiêu chuẩn chọn trang nạn nhân của các thuật toán thay thế trang nhớ ảo: **OPT**, **FIFO**, **LRU**, **LFU**, và **NUR**.
- Phân biệt rõ sự khác nhau giữa thước đo theo dòng thời gian (Thời điểm nạp vào RAM của FIFO vs Lần tham chiếu gần nhất của LRU) và thước đo theo số lần sử dụng (Tần suất của LFU).
- Giải thích được nguyên lý vận hành của thuật toán NUR (Not Used Recently) dựa trên cặp bit cờ trạng thái Tham chiếu ($R$) và Chỉnh sửa ($M$).

## 핵심 키워드 (Từ khóa)
- 페이지 교체 (Page Replacement)
- OPT (Optimal - 이상적 최적 알고리즘)
- FIFO (First-In, First-Out - Belady의 모순)
- LRU (Least Recently Used - 시간적 최근성)
- LFU (Least Frequently Used - 참조 횟수/빈도)
- NUR (Not Used Recently - 참조 비트 R, 변형 비트 M)
- 페이지 부재율 최소화 (Minimizing Page Fault Rate)

## 선행·연결 개념 (Kiến thức liên kết)
- [89-bai-hoc.md](89-bai-hoc.md): Cấu trúc phân tầng hệ thống UNIX (Kernel, Shell, Utility).
- [91-bai-hoc.md](91-bai-hoc.md): Khối điều khiển tiến trình PCB (Process Control Block).
- [73-bai-hoc.md](73-bai-hoc.md): Đại cương về thuật toán thay thế trang và hiện tượng Thrashing.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong các câu hỏi đề thi:
  - **OPT:** Nhìn về **Tương lai** $\rightarrow$ Trang lâu nhất không dùng trong tương lai. Không cài đặt thực tế được.
  - **FIFO:** Nhìn vào **Thời điểm nạp** $\rightarrow$ Trang vào RAM sớm nhất. Cảnh giác hiện tượng Belady Anomaly.
  - **LRU:** Nhìn về **Quá khứ** $\rightarrow$ Trang có thời gian chưa dùng lâu nhất tính từ hiện tại. Rất phổ biến.
  - **LFU:** Đếm **Số lần** $\rightarrow$ Trang có số lần tham chiếu ít nhất.
  - **NUR:** Xem **Cặp bit $(R, M)$** $\rightarrow$ Ưu tiên đuổi $(0,0)$ đầu tiên, sau đó tới $(0,1)$, $(1,0)$, và cuối cùng là $(1,1)$.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 5 thuật toán thay thế trang kinh điển:**

| Thuật toán | Tiêu chuẩn chọn trang để thay thế | Tính khả thi thực tế | Đánh giá ưu nhược điểm |
| :--- | :--- | :--- | :--- |
| **OPT** (Optimal) | Trang sẽ **lâu nhất không được sử dụng trong tương lai**. | **Không khả thi** (Lý thuyết) | Đạt tỷ lệ lỗi trang thấp nhất tuyệt đối; dùng làm chuẩn đối chuẩn (Benchmark) để đánh giá các thuật toán khác. |
| **FIFO** (First-In First-Out) | Trang được nạp vào bộ nhớ RAM ở **thời điểm sớm nhất**. | Dễ cài đặt bằng hàng đợi Queue | Dễ gặp nghịch lý Belady (tăng số khung trang nhưng số lần lỗi trang lại tăng lên). |
| **LRU** (Least Recently Used) | Trang có **khoảng thời gian lâu nhất chưa được tham chiếu trong quá khứ**. | Khả thi cao (dùng Timestamp / Stack) | Hiệu năng tiệm cận tối ưu; phản ánh chính xác nguyên lý tính cục bộ thời gian (Temporal Locality). |
| **LFU** (Least Frequently Used) | Trang có **tổng số lần được tham chiếu (tần suất) ít nhất**. | Khả thi (dùng bộ đếm Counter) | Tốn chi phí quản lý bộ đếm; có thể giữ lại các trang cũ chỉ dùng nhiều lúc đầu nhưng không còn dùng sau đó. |
| **NUR** (Not Used Recently) | Dựa trên 2 bit cờ: Bit tham chiếu $R$ (0: chưa đọc, 1: đã đọc) và Bit biến đổi $M$ (0: chưa sửa, 1: đã ghi sửa). | Khả thi rất cao (hỗ trợ phần cứng) | Xấp xỉ LRU với chi phí phần cứng cực thấp; thứ tự thay thế: $(0,0) \rightarrow (0,1) \rightarrow (1,0) \rightarrow (1,1)$. |

- **2. 4 cấp độ ưu tiên thay thế trong thuật toán NUR:**
  1. Cấp 1 (Đuổi đầu tiên): $(R=0, M=0)$ – Không được tham chiếu gần đây và dữ liệu chưa bị sửa đổi (không cần ghi lại đĩa).
  2. Cấp 2: $(R=0, M=1)$ – Không được tham chiếu gần đây nhưng dữ liệu đã bị sửa đổi (phải ghi lại đĩa).
  3. Cấp 3: $(R=1, M=0)$ – Được tham chiếu gần đây nhưng dữ liệu sạch chưa sửa.
  4. Cấp 4 (Giữ lại lâu nhất): $(R=1, M=1)$ – Vừa được tham chiếu vừa bị sửa đổi.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ truy vết chuỗi tham chiếu trang minh họa sự khác nhau:**
  - Chuỗi tham chiếu: `1, 2, 3, 2, 1, 5` với 3 khung trang bộ nhớ.
  - Khi nạp trang `5` vào RAM (đang chứa `{1, 2, 3}`):
    - *FIFO:* Trang `1` vào sớm nhất $\rightarrow$ Đuổi `1` để nạp `5`.
    - *LRU:* Các trang vừa dùng gần đây theo thứ tự là `1`, rồi `2`, lâu nhất chưa dùng là `3` $\rightarrow$ Đuổi `3` để nạp `5`.

### 복습 체크리스트
- [ ] Ghi nhớ tiêu chí chọn trang: OPT (tương lai), FIFO (vào sớm nhất), LRU (quá khứ xa nhất), LFU (ít lần nhất).
- [ ] Nhớ hiện tượng Belady Anomaly chỉ xảy ra ở thuật toán **FIFO**.
- [ ] Thuộc 4 mức ưu tiên thay thế của NUR: $(0,0) \rightarrow (0,1) \rightarrow (1,0) \rightarrow (1,1)$.
- [ ] Phân biệt được sự khác nhau giữa LRU (đo thời gian) và LFU (đo số lần đếm).
