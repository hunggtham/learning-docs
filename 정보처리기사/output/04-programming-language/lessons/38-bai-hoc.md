# 289 - 296. 메모리 관리 및 가상 기억장치 (Memory Management)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc và hai phương pháp quản lý bộ nhớ ảo kinh điển: Kỹ thuật phân trang (페이징 - Paging) chia khối kích thước cố định và Kỹ thuật phân đoạn (세그멘테이션 - Segmentation) chia khối theo logic biến đổi.
- Phân tích sâu sắc sự đánh đổi kích thước trang (Page Size Tradeoffs): hệ quả của việc chọn trang kích thước nhỏ (Small Page) so với chọn trang kích thước lớn (Large Page).
- Hiểu rõ bản chất hiện tượng Thrashing (스래싱), các nguyên nhân kỹ thuật gây ra và hai giải pháp phòng chống: Mô hình tập làm việc (Working Set Model) và Mô hình tần số lỗi trang (PFF - Page Fault Frequency).

## 핵심 키워드 (Từ khóa)
- 가상 기억장치 (Virtual Memory)
- 페이징 기법 (Paging / 고정 크기 / 내부 단편화)
- 세그멘테이션 기법 (Segmentation / 가변 크기 / 외부 단편화)
- 페이지 크기 결정 (Page Size Tradeoffs)
- 페이지 맵 테이블 (Page Map Table / PMT)
- 스래싱 (Thrashing / 페이지 부재 빈발)
- 워킹 셋 (Working Set / Locality 기반 참조 페이지 집합)
- PFF (Page Fault Frequency / 페이지 부재 빈도 조절)

## 선행·연결 개념 (Kiến thức liên kết)
- [37-bai-hoc.md](37-bai-hoc.md): Chiến lược cấp phát bộ nhớ First Fit, Best Fit, Worst Fit.
- [39-bai-hoc.md](39-bai-hoc.md): Quản lý tiến trình, luồng (Thread) và khối PCB.
- [정보처리기사/output/02-software-development/lessons/88-bai-hoc.md](../../02-software-development/lessons/88-bai-hoc.md): Khái niệm bộ nhớ ảo và lỗi trang (Page Fault).

## 읽는 방법 (Cách đọc)
- Phân biệt hai phương pháp tổ chức bộ nhớ ảo:
  - **페이징 (Paging):** Cắt bộ nhớ thành các phần **bằng nhau 100% (고정 크기)**. Giống như chia bánh thành các lát 100g. Ưu điểm là không có khe hở thừa giữa các khối $\rightarrow$ **Không bị phân mảnh ngoại vi**, nhưng phần đuôi của trang cuối cùng thường không dùng hết $\rightarrow$ **Gây phân mảnh nội vi (Internal Fragmentation)**.
  - **세그멘테이션 (Segmentation):** Cắt chương trình theo **đơn vị logic ý nghĩa (가변 크기)** như hàm `main()`, mảng `arr`, cấu trúc `struct`. Các khối to nhỏ khác nhau nên **không bị phân mảnh nội vi**, nhưng khi chèn vào RAM sẽ để lại các khoảng trống lắt nhắt giữa các khối $\rightarrow$ **Gây phân mảnh ngoại vi (External Fragmentation)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh: Paging vs Segmentation:**

| Tiêu chuẩn so sánh | 페이징 기법 (Paging) | 세그멘테이션 기법 (Segmentation) |
| :--- | :--- | :--- |
| **Kích thước khối** | **Cố định (고정 크기)**; do hệ thống quy định (4KB) | **Biến đổi (가변 크기)**; theo kích thước logic của module |
| **Bản chất phân chia** | Phân chia thuần túy theo vật lý; không quan tâm nội dung | Phân chia theo ý nghĩa logic (hàm, dữ liệu, stack) |
| **Hiện tượng phân mảnh** | **내부 단편화 발생 (Phân mảnh nội vi)**; External = 0 | **외부 단편화 발생 (Phân mảnh ngoại vi)**; Internal = 0 |
| **Cấu trúc địa chỉ** | Địa chỉ 2 thành phần: `(Page Number, Offset)` | Địa chỉ 2 thành phần: `(Segment Number, Offset/Limit)` |
| **Chia sẻ và bảo vệ** | Khó thiết lập quyền riêng biệt cho từng hàm logic | Rất dễ dàng chia sẻ và bảo vệ phân quyền (Read/Write/Exec) |

- **Bảng phân tích sự đánh đổi khi chọn Kích thước Trang (Page Size):**

| Hệ quả kỹ thuật | Khi chọn Trang Kích thước Nhỏ (Small Page) | Khi chọn Trang Kích thước Lớn (Large Page) |
| :--- | :--- | :--- |
| **Phân mảnh nội vi** | **Giảm thiểu (감소)**; ít lãng phí không gian trang cuối | **Tăng lên (증가)**; lãng phí nhiều bộ nhớ ở trang cuối |
| **Kích thước bảng trang** | **Rất lớn (증가)**; vì số lượng trang nhiều lên | **Nhỏ gọn (감소)**; bảng trang ít phần tử hơn |
| **Tốc độ nạp I/O từ đĩa** | Tốn nhiều lần tìm kiếm đĩa (Nhiều Seek Time) | **Nhanh hơn**, đọc được một khối lớn trong 1 lần xoay đĩa |
| **Tính cục bộ (Locality)** | Rất chính xác; chỉ nạp đúng các lệnh thực sự cần | Nạp cả những đoạn mã thừa không dùng vào RAM |

- **Bảng giải pháp phòng chống hiện tượng Thrashing:**

| Giải pháp kỹ thuật | Tên tiếng Hàn & Anh | Cơ chế hoạt động cốt lõi |
| :--- | :--- | :--- |
| **Working Set Model** | **워킹 셋 모델 (Denning)** | Tập hợp các trang được tiến trình tham chiếu thường xuyên trong một khoảng thời gian $\Delta$ (Locality). Chỉ cấp CPU khi RAM đủ chỗ nạp **toàn bộ Working Set** |
| **Page Fault Frequency** | **PFF (페이지 부재 빈도)** | Đo tần số phát sinh lỗi trang. Nếu tần số vượt ngưỡng trên (Upper Bound) $\rightarrow$ Cấp thêm khung trang; nếu tụt dưới ngưỡng dưới (Lower Bound) $\rightarrow$ Thu hồi bớt khung trang |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Định nghĩa toán học của Thrashing:**
  - Thrashing là trạng thái suy sụp của hệ điều hành khi:
    $$\text{Thời gian hoán đổi trang (Page Swapping Time)} \gg \text{Thời gian thực thi CPU (Execution Time)}$$
  - Hệ quả: Mặc dù CPU hầu như không bận xử lý công việc thực tế, nhưng hàng đợi I/O đĩa cứng luôn bị nghẽn 100%, hiệu suất toàn hệ thống rơi tự do về 0.

### 복습 체크리스트
- [ ] Nhớ Paging gây 내부 단편화 (phân mảnh nội vi), Segmentation gây 외부 단편화 (phân mảnh ngoại vi).
- [ ] Nhớ khi Page nhỏ: Bảng trang lớn, phân mảnh nội vi giảm. Khi Page lớn: Bảng trang nhỏ, phân mảnh nội vi tăng.
- [ ] Nêu được định nghĩa Thrashing: Thời gian đổi trang nhiều hơn thời gian CPU chạy.
- [ ] Kể tên 2 giải pháp chống Thrashing: Working Set (tập làm việc) và PFF (tần số lỗi trang).
