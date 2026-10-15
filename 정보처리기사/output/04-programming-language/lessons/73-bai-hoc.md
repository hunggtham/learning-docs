# 084. 페이지 교체 알고리즘 (Page Replacement Algorithms / Thuật toán thay thế trang nhớ)

## 학습 목표 (Mục tiêu)
- Nắm vững nguyên lý hoạt động và tiêu chí lựa chọn trang nạn nhân của các thuật toán thay thế trang nhớ ảo: FIFO, OPT, LRU, LFU, và NUR.
- Phân biệt sự khác nhau giữa tính cục bộ không gian (공간 구역성 - Spatial Locality) và tính cục bộ thời gian (시간 구역성 - Temporal Locality).
- Thấu hiểu hiện tượng suy giảm hiệu năng nghiêm trọng do lỗi trang liên tục (스레싱 - Thrashing) và các giải pháp kiểm soát (Working Set, Page Fault Frequency).

## 핵심 키워드 (Từ khóa)
- 가상기억장치 (Virtual Memory)
- 페이지 부재 (Page Fault)
- 페이지 교체 알고리즘 (Page Replacement: FIFO, OPT, LRU, LFU, NUR)
- Belady의 모순 (Belady's Anomaly in FIFO)
- 시간 구역성 (Temporal Locality) & 공간 구역성 (Spatial Locality)
- 스레싱 (Thrashing - Page I/O Overhead)
- 워킹 셋 (Working Set) & PFF (Page Fault Frequency)

## 선행·연결 개념 (Kiến thức liên kết)
- [72-bai-hoc.md](72-bai-hoc.md): Phân loại ngôn ngữ lập trình và quản lý bộ nhớ.
- [74-bai-hoc.md](74-bai-hoc.md): Các điều kiện bế tắc Deadlock và giải thuật tương hỗ loại trừ (Mutual Exclusion).
- [38-bai-hoc.md](38-bai-hoc.md): Chiến lược phân bổ bộ nhớ thực (First Fit, Best Fit, Worst Fit).

## 읽는 방법 (Cách đọc)
- Phân biệt 4 thuật toán thay thế trang qua tiêu chí quyết định:
  - **FIFO:** Vào trước ra trước (Thời điểm nạp vào RAM sớm nhất). Chú ý hiện tượng nghịch lý Belady.
  - **OPT:** Nhìn về **Tương lai** (Lâu được dùng nhất trong tương lai $\rightarrow$ Tối ưu lý thuyết, không hiện thực hóa được).
  - **LRU:** Nhìn về **Quá khứ** (Lâu nhất không được ai chạm vào tính đến thời điểm hiện tại).
  - **LFU:** Đếm **Số lần** (Tần suất xuất hiện / số lượt tham chiếu ít nhất).
  - **NUR:** Dựa vào 2 bit $(R, M)$: Bit tham chiếu $R$ và bit chỉnh sửa $M$. Ưu tiên đuổi $(0,0)$ đầu tiên.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các thuật toán thay thế trang nhớ (Page Replacement):**

| Thuật toán | Tiêu chuẩn chọn trang để thay thế | Khả năng hiện thực & Đánh giá |
| :--- | :--- | :--- |
| **FIFO** (First-In, First-Out) | Trang được nạp vào bộ nhớ RAM ở **thời điểm sớm nhất** sẽ bị đẩy ra trước. | Dễ cài đặt bằng hàng đợi Queue, nhưng có thể gặp **nghịch lý Belady** (Tăng thêm số khung trang RAM nhưng số lần lỗi trang lại tăng lên). |
| **OPT** (Optimal Replacement) | Trang sẽ **lâu nhất không được sử dụng trong tương lai** sẽ bị đẩy ra. | **Đạt tỷ lệ lỗi trang thấp nhất lý thuyết**, nhưng không thể cài đặt thực tế vì hệ điều hành không thể dự đoán chính xác chuỗi tham chiếu tương lai của tiến trình. |
| **LRU** (Least Recently Used) | Trang có **khoảng thời gian dài nhất không được tham chiếu trong quá khứ** sẽ bị thay thế. | Hiệu năng rất cao, xấp xỉ thuật toán tối ưu OPT; được ứng dụng rộng rãi nhất trên thực tế (dùng Stack hoặc Timestamp). |
| **LFU** (Least Frequently Used) | Trang có **tổng số lần được tham chiếu (tần suất) ít nhất** sẽ bị thay thế. | Tốn chi phí duy trì bộ đếm tham chiếu; dễ gặp lỗi giữ lại các trang chỉ được dùng nhiều ở giai đoạn khởi động nhưng không còn dùng sau đó. |
| **NUR** (Not Used Recently) | Dựa vào 2 cờ bit: $R$ (Reference bit - Tham chiếu) và $M$ (Modified bit - Chỉnh sửa) để xếp hạng thành 4 mức ưu tiên thay thế. | Thứ tự ưu tiên đuổi từ thấp đến cao: **$(R=0, M=0) \rightarrow (R=0, M=1) \rightarrow (R=1, M=0) \rightarrow (R=1, M=1)$**. |

- **2. Tính cục bộ của tham chiếu bộ nhớ (Locality - Denning):**
  - **시간 구역성 (Temporal Locality - Cục bộ thời gian):** Nếu một ô nhớ được tham chiếu tại thời điểm hiện tại thì nó có xu hướng sẽ được tham chiếu lại nhiều lần nữa trong tương lai gần. *Ví dụ:* Các biến đếm trong vòng lặp (`for`, `while`), biến tích lũy, các hàm con được gọi liên tục.
  - **공간 구역성 (Spatial Locality - Cục bộ không gian):** Nếu một ô nhớ được tham chiếu thì các ô nhớ lân cận nằm sát cạnh nó cũng có xác suất rất cao sẽ được tham chiếu kế tiếp. *Ví dụ:* Duyệt tuần tự các phần tử của mảng một chiều (Array), thực thi khối mã lệnh tuần tự.

- **3. Hiện tượng Thrashing (스레싱):**
  - Xảy ra khi số khung trang (Page Frames) cấp cho tiến trình quá ít, dẫn đến tỷ lệ lỗi trang (Page Fault) tăng vọt.
  - Hệ điều hành phải dành phần lớn thời gian CPU chỉ để hoán chuyển trang nhớ giữa RAM và ổ đĩa (Page In / Page Out) thay vì thực thi tính toán hữu ích, khiến thông lượng của toàn hệ thống rơi xuống gần bằng 0.
  - **Giải pháp:** Sử dụng mô hình **Working Set** (Tập trang đang hoạt động) hoặc theo dõi **Tần suất lỗi trang (PFF - Page Fault Frequency)** để cấp phát động số khung trang phù hợp.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa bài toán truy vết LRU với 3 khung trang:**
  - Chuỗi tham chiếu: `1, 2, 3, 1, 4` với 3 khung RAM ban đầu rỗng.
  - Nạp `1` (Fault, RAM: `[1]`), nạp `2` (Fault, RAM: `[1, 2]`), nạp `3` (Fault, RAM: `[1, 2, 3]`).
  - Gặp `1` (Hit, cập nhật `1` là vừa dùng gần nhất, RAM: `[2, 3, 1]`).
  - Gặp `4` (Fault, trang `2` lâu nhất chưa dùng $\rightarrow$ thay `2` bằng `4`, RAM: `[4, 3, 1]`).

### 복습 체크리스트
- [ ] Phân biệt được tiêu chí cốt lõi: FIFO (vào trước), OPT (tương lai), LRU (quá khứ), LFU (tần suất).
- [ ] Ghi nhớ nghịch lý Belady chỉ xuất hiện ở thuật toán **FIFO**.
- [ ] Nhớ thứ tự ưu tiên thay thế của NUR: Cặp bit $(0, 0)$ bị thay thế đầu tiên.
- [ ] Phân biệt Temporal Locality (vòng lặp lặp lại biến) vs Spatial Locality (duyệt mảng liên tiếp kề nhau).
- [ ] Hiểu Thrashing là hiện tượng CPU bị nghẽn do bận hoán đổi trang liên tục vì thiếu RAM.
