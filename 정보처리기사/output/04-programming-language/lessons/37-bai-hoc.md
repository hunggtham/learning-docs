# 083. 메모리 관리 기법 - 배치 전략 (Memory Placement Strategies)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 chiến lược nạp tiến trình vào các phân vùng bộ nhớ chính (주기억장치 배치 전략 - Memory Placement Strategies): First Fit (최초 적합), Best Fit (최적 적합), và Worst Fit (최악 적합).
- Phân biệt hiện tượng phân mảnh nội vi (내부 단편화 - Internal Fragmentation) và phân mảnh ngoại vi (외부 단편화 - External Fragmentation).
- Rèn luyện kỹ năng giải các bài toán thực hành cấp phát bộ nhớ: Cho danh sách các phân vùng trống và kích thước tiến trình cần nạp, xác định chính xác phân vùng được chọn và dung lượng phân mảnh còn lại.

## 핵심 키워드 (Từ khóa)
- 기억장치 배치 전략 (Memory Placement Strategies)
- 최초 적합 (First Fit / 탐색 시간 최소 / 최초 가용 영역)
- 최적 적합 (Best Fit / 단편화 최소 / 가장 작은 가용 영역)
- 최악 적합 (Worst Fit / 단편화 최대 / 가장 큰 가용 영역)
- 내부 단편화 (Internal Fragmentation / 분할 내 낭비 공간)
- 외부 단편화 (External Fragmentation / 너무 작아서 못 쓰는 빈 공간)

## 선행·연결 개념 (Kiến thức liên kết)
- [36-bai-hoc.md](36-bai-hoc.md): Hệ thống UNIX và mô tả tệp tin (File Descriptor).
- [38-bai-hoc.md](38-bai-hoc.md): Quản lý bộ nhớ ảo - Phân trang và Phân đoạn.
- [33-bai-hoc.md](33-bai-hoc.md): Khái quát quản lý bộ nhớ và lập lịch tiến trình.

## 읽는 방법 (Cách đọc)
- Phân biệt 3 chiến lược qua mục tiêu tối ưu:
  - **First Fit (최초 적합):** Quét từ địa chỉ thấp đến cao, gặp ô trống đầu tiên có kích thước $\ge$ kích thước tiến trình là nạp ngay $\rightarrow$ **Nhanh nhất về thời gian tìm kiếm**.
  - **Best Fit (최적 적합):** So sánh tất cả ô trống đủ điều kiện, chọn ô trống có kích thước sát nhất (chênh lệch nhỏ nhất) $\rightarrow$ **Để lại mảnh vụn thừa nhỏ nhất**.
  - **Worst Fit (최악 적합):** So sánh tất cả ô trống đủ điều kiện, cố tình chọn ô trống có kích thước to nhất $\rightarrow$ **Để lại phần diện tích trống thừa lớn nhất** để hy vọng các tiến trình khác có thể nhét vừa vào phần còn lại đó.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 chiến lược cấp phát bộ nhớ:**

| Chiến lược nạp | Quy tắc lựa chọn ô trống | Tốc độ tìm kiếm | Đặc điểm phân mảnh (Fragmentation) |
| :--- | :--- | :--- | :--- |
| **First Fit (최초 적합)** | Chọn ô trống **đầu tiên** tìm thấy có kích thước $\ge$ kích thước tiến trình | **Cực nhanh**, dừng ngay khi thấy ô đầu tiên | Để lại các khoảng phân mảnh ngẫu nhiên rải rác |
| **Best Fit (최적 적합)** | Chọn ô trống có $(\text{Kích thước ô} - \text{Kích thước tiến trình})$ là **nhỏ nhất** ($\ge 0$) | Chậm hơn, phải duyệt toàn bộ danh sách ô trống | Tạo ra nhiều mảnh vụn rất nhỏ (**단편화 최소화**), các mảnh này khó tái sử dụng |
| **Worst Fit (최악 적합)** | Chọn ô trống có kích thước **LỚN NHẤT** trong toàn bộ bộ nhớ | Chậm hơn, phải duyệt toàn bộ danh sách ô trống | Phần dư còn lại có kích thước lớn, dễ tận dụng cho tiến trình sau |

- **Bài toán thi mẫu thực hành cấp phát bộ nhớ:**
  - *Đề bài:* Bộ nhớ có 4 phân vùng trống theo thứ tự địa chỉ: **[1] 10KB, [2] 20KB, [3] 8KB, [4] 15KB**. Cần nạp một tiến trình $P$ có kích thước **12KB**. Hỏi phân vùng nào được chọn và phân mảnh thừa là bao nhiêu theo 3 chiến lược?
  - *Lời giải chi tiết:*
    1. **Theo First Fit:**
       - Xét [1] 10KB: Nhỏ hơn 12KB $\rightarrow$ Bỏ qua.
       - Xét [2] 20KB: Đủ lớn $\ge 12\text{KB}$ $\rightarrow$ **CHỌN PHÂN VÙNG [2]**.
       - Phần mảnh thừa $= 20 - 12 = \mathbf{8KB}$.
    2. **Theo Best Fit:**
       - Các phân vùng đủ chứa 12KB là: [2] 20KB và [4] 15KB.
       - So sánh chênh lệch: Phân vùng [4] chênh $15 - 12 = 3\text{KB}$; Phân vùng [2] chênh $20 - 12 = 8\text{KB}$.
       - Chọn mức chênh lệch nhỏ nhất $\rightarrow$ **CHỌN PHÂN VÙNG [4]**.
       - Phần mảnh thừa $= 15 - 12 = \mathbf{3KB}$.
    3. **Theo Worst Fit:**
       - Phân vùng lớn nhất trong cả 4 vùng là [2] 20KB.
       - Chọn ô rộng nhất $\rightarrow$ **CHỌN PHÂN VÙNG [2]**.
       - Phần mảnh thừa $= 20 - 12 = \mathbf{8KB}$.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật gom dọn bộ nhớ (Compaction / 가비지 컬렉션):**
  - Sau nhiều đợt nạp và giải phóng tiến trình, bộ nhớ bị chia cắt thành hàng trăm mảnh vụn ngoại vi (External Fragmentation) nằm rải rác, khiến một tiến trình lớn không thể nạp vào dù tổng dung lượng trống cộng lại vẫn đủ.
  - Hệ điều hành thực hiện kỹ thuật dồn ô nhớ (Compaction / Đóng gói bộ nhớ): Di chuyển tất cả các tiến trình đang chạy dồn về một đầu bộ nhớ, gom toàn bộ các mảnh vụn rải rác lại thành một khối trống liên tục khổng lồ ở đầu kia.

### 복습 체크리스트
- [ ] Nhớ First Fit nạp vào ô trống đầu tiên tìm thấy (tốc độ nhanh nhất).
- [ ] Nhớ Best Fit nạp vào ô vừa khít nhất (để lại phần dư nhỏ nhất).
- [ ] Nhớ Worst Fit nạp vào ô lớn nhất (để lại phần dư lớn nhất).
- [ ] Giải thành thạo bài toán trắc nghiệm tính vị trí phân vùng và phần mảnh thừa.
