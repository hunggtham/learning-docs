# 285 & 295. 워킹 셋 (Working Set / Tập làm việc)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ sở lý thuyết và công thức mô hình hóa Tập làm việc (워킹 셋 - Working Set Model do Peter Denning đề xuất) trong quản trị bộ nhớ ảo.
- Thấu hiểu mối quan hệ biện chứng giữa nguyên lý tính cục bộ (Locality), kích thước cửa sổ thời gian trượt ($\Delta$ - Working Set Window), và việc cấp phát động khung trang nhớ (Page Frames).
- Giải thích được vai trò hạt nhân của Working Set trong việc duy trì độ ổn định của hệ thống và ngăn ngừa triệt để hiện tượng suy sụp hiệu năng do nghẽn trang (스레싱 - Thrashing).

## 핵심 키워드 (Từ khóa)
- 워킹 셋 (Working Set Model - Peter Denning)
- 워킹 셋 윈도우 크기 ($\Delta$ - Working Set Window)
- 국부성 / 구역성 기반 (Locality-based Memory Management)
- 동적 페이지 할당 (Dynamic Page Allocation)
- 스레싱 방지 (Thrashing Prevention)
- 상주 집합 (Resident Set) vs 워킹 셋 (Working Set)

## 선행·연결 개념 (Kiến thức liên kết)
- [87-bai-hoc.md](87-bai-hoc.md): Nguyên lý tính cục bộ (Locality) thời gian và không gian.
- [89-bai-hoc.md](89-bai-hoc.md): Cấu trúc phân tầng hệ thống UNIX (Kernel, Shell, Utility).
- [73-bai-hoc.md](73-bai-hoc.md): Thuật toán thay thế trang và hiện tượng Thrashing.

## 읽는 방법 (Cách đọc)
- Điểm mấu chốt trong đề thi kỹ sư CNTT:
  - Khái niệm: Working Set là **"Tập hợp các trang nhớ mà tiến trình tham chiếu thường xuyên trong một khoảng thời gian nhất định ($\Delta$)"**.
  - Tác dụng lớn nhất: Bằng cách **luôn đảm bảo cấp đủ số khung trang nhớ RAM để giữ toàn bộ Working Set của tiến trình thường trú trong bộ nhớ chính**, hệ điều hành sẽ triệt tiêu lỗi trang liên tục, từ đó **ngăn chặn hiện tượng Thrashing**.
  - Đặc tính: Working Set **không cố định mà thay đổi động (Dynamic)** theo thời gian chạy của chương trình.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Mô hình toán học của Working Set (Denning):**
  - Ký hiệu: $W(t, \Delta)$ là tập hợp các trang nhớ được tiến trình tham chiếu trong khoảng thời gian từ $t - \Delta$ đến thời điểm hiện tại $t$.
  - Trong đó:
    - $t$: Thời điểm khảo sát hiện tại.
    - $\Delta$ (Delta): Kích thước **cửa sổ Working Set (Working Set Window)** – số lượng tham chiếu trang gần nhất được đưa vào xét duyệt.
  - *Ví dụ minh họa:*
    - Chuỗi tham chiếu trang: `... 2, 6, 1, 5, 7, 7, 7, 5, 1` tại thời điểm $t$.
    - Nếu chọn kích thước cửa sổ $\Delta = 5$ tham chiếu gần nhất: Tập các trang tham chiếu gần nhất là $\{7, 7, 5, 1\}$ (lấy 5 vị trí cuối: `7, 7, 7, 5, 1`).
    - Khi đó Tập làm việc Working Set là: $W(t, 5) = \{1, 5, 7\}$ (gồm 3 trang khác nhau).

- **2. Cơ chế phòng chống Thrashing bằng Working Set:**

| Tình huống tài nguyên bộ nhớ | Trạng thái hệ thống | Hành động xử lý của Hệ điều hành |
| :--- | :--- | :--- |
| $\sum \text{Kích thước Working Set} \le \text{Tổng dung lượng RAM}$ | Hệ thống vận hành trơn tru, tỷ lệ lỗi trang (Page Fault) cực thấp. | Tiến trình được cấp phát đủ khung trang theo nhu cầu thực tế; CPU duy trì thông lượng cao. |
| $\sum \text{Kích thước Working Set} > \text{Tổng dung lượng RAM}$ | Nguy cơ bùng nổ hiện tượng **Thrashing** (Máy bị đơ, giật lag do liên tục Swap trang). | Hệ điều hành chủ động **chọn một số tiến trình để tạm dừng (Suspend / Swap Out)** đưa ra bộ nhớ phụ, nhường toàn bộ khung trang RAM cho các tiến trình còn lại chạy mượt mà. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hình tượng hóa thực tế đời sống:**
  - Hãy tưởng tượng bạn đang ngồi học thi tại bàn học:
    - Mặt bàn học của bạn chính là **Bộ nhớ thực (RAM)**.
    - Kệ sách đằng xa chính là **Ổ cứng (Secondary Storage)**.
    - Cuốn sách giáo khoa, vở ghi và chiếc bút bạn đang mở ra dùng ngay lúc này chính là **Working Set**.
    - Nếu mặt bàn đủ chỗ để đặt những thứ đang dùng (Working Set), bạn học rất nhanh. Nếu mặt bàn quá chật không để vừa, bạn phải liên tục đứng lên cất sách này lấy sách kia ra kệ (Page Fault) $\rightarrow$ Hết sạch thời gian học (Thrashing).

### 복습 체크리스트
- [ ] Ghi nhớ định nghĩa Working Set: Tập hợp các trang nhớ được tham chiếu trong cửa sổ thời gian $\Delta$.
- [ ] Nắm vững mục đích cốt lõi: Giữ Working Set trong RAM để ngăn ngừa hiện tượng Thrashing.
- [ ] Khẳng định Working Set mang tính biến đổi động theo thời gian thực tế.
- [ ] Biết cách tính tập phần tử Working Set từ chuỗi tham chiếu và độ dài cửa sổ $\Delta$.
