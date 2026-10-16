# 주기억장치 관리 기법 및 배치 전략 (Quản lý bộ nhớ thực & Chiến lược cấp phát)

## 학습 목표 (Mục tiêu)
- Nắm vững các phương pháp quản lý bộ nhớ chính (주기억장치 관리): Phân vùng cố định (고정 분할) và Phân vùng biến đổi (가변 분할).
- Phân biệt bản chất kỹ thuật giữa hai loại phân mảnh bộ nhớ: Phân mảnh trong (내부 단편화 - Internal Fragmentation) và Phân mảnh ngoài (외부 단편화 - External Fragmentation), cùng 2 kỹ thuật dọn dẹp: Hợp nhất (통합) và Nén bộ nhớ (압축).
- Áp dụng thành thạo 3 chiến lược cấp phát khối nhớ trống (배치 전략 - Placement Strategies): First-Fit (최초 적합), Best-Fit (최적 적합), và Worst-Fit (최악 적합) để giải quyết chính xác các bài toán tính toán trắc nghiệm của HRDK.

## 핵심 키워드 (Từ khóa)
- 내부 단편화 (Internal Fragmentation) — Bộ nhớ được cấp phát lớn hơn nhu cầu tiến trình (dư thừa bên trong).
- 외부 단편화 (External Fragmentation) — Tổng bộ nhớ trống đủ nhưng bị chia cắt thành nhiều mảnh nhỏ rời rạc.
- 최초 적합 (First-Fit) — Chọn ngay khối trống đầu tiên đủ lớn từ đầu bộ nhớ (Tốc độ tìm kiếm nhanh nhất).
- 최적 적합 (Best-Fit) — Chọn khối trống nhỏ nhất trong số các khối đủ chứa (để lại mảnh thừa nhỏ nhất).
- 최악 적합 (Worst-Fit) — Chọn khối trống lớn nhất có sẵn (để lại mảnh thừa đủ lớn để tái sử dụng).
- 메모리 압축 (Compaction) — Dồn các tiến trình về một phía để gom toàn bộ khoảng trống về phía đối diện.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `12-tien-trinh-luong-va-dieu-phoi-cpu.md`, trước khi tiến trình được CPU cấp phát thời gian chạy, nó bắt buộc phải được nạp vào một phân vùng của bộ nhớ chính (RAM).
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Khi bộ nhớ RAM có nhiều khoảng trống kích thước khác nhau nằm xen kẽ do các tiến trình nạp vào rồi giải phóng, Hệ điều hành dùng thuật toán nào để chọn vị trí xếp tiến trình mới vào vừa nhanh vừa ít lãng phí bộ nhớ nhất.
- **Dùng đi đâu (Forward Handoff):** Khi kích thước chương trình vượt quá dung lượng vật lý của RAM hoặc phân mảnh ngoài quá lớn, hệ thống buộc phải chuyển sang mô hình Bộ nhớ ảo (Virtual Memory) với các giải thuật phân trang và thay thế trang trong bài `15-bo-nho-ao-thuat-toan-thay-the-trang-va-thrashing.md`.

## 읽는 방법 (Cách đọc)
- **Chiến lược cấp phát:**
  - **First-Fit (최초 적합):** Quét từ trên xuống dưới, gặp lỗ trống đầu tiên vừa vặn là đưa vào ngay $\rightarrow$ **Nhanh nhất**.
  - **Best-Fit (최적 적합):** Tìm lỗ trống có độ lệch nhỏ nhất (vừa khít nhất với tiến trình) $\rightarrow$ **Mảnh thừa nhỏ nhất**.
  - **Worst-Fit (최악 적합):** Tìm lỗ trống to nhất trong toàn bộ danh sách để đưa vào $\rightarrow$ **Mảnh thừa to nhất**.
- **Phân mảnh:**
  - Trong (Internal): Cấp 100KB cho tiến trình cần 80KB $\rightarrow$ Dư 20KB bên trong.
  - Ngoài (External): Có 2 lỗ trống 30KB và 40KB (tổng 70KB), nhưng tiến trình cần 50KB liên tục không thể xếp vừa.

---

## 주기억장치 관리 기법 및 배치 전략

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `주기억장치 배치 전략에서 최초 적합(First-Fit)은 탐색 속도가 가장 빠르고, 최적 적합(Best-Fit)은 단편화 잔여 공간이 가장 작으며, 최악 적합(Worst-Fit)은 가장 큰 빈 공간에 배치한다. 내부 단편화는 할당 공간이 필요량보다 클 때 발생하고, 외부 단편화는 총 여유 공간은 충분하나 연속되지 않아 발생한다.`
  - [Tiếng Việt]: Trong chiến lược cấp phát bộ nhớ, First-Fit có tốc độ tìm kiếm nhanh nhất, Best-Fit để lại mảnh thừa nhỏ nhất, và Worst-Fit cấp phát vào khối trống lớn nhất. Phân mảnh trong xảy ra khi ô cấp phát lớn hơn nhu cầu; phân mảnh ngoài xảy ra khi tổng khoảng trống đủ nhưng không liên tục.

- **1. Bảng đối chiếu Phân mảnh trong vs Phân mảnh ngoài:**

| Tiêu chuẩn so sánh | Phân mảnh trong (내부 단편화 - Internal) | Phân mảnh ngoài (외부 단편화 - External) |
| :--- | :--- | :--- |
| **Bản chất nguyên nhân**| Vùng nhớ được cấp phát **lớn hơn nhu cầu thực tế** của tiến trình. | Tổng dung lượng trống đủ lớn nhưng bị **chia cắt manh mún, rời rạc**. |
| **Vị trí lãng phí** | Nằm **bên trong** phân vùng đã được giao cho tiến trình quản lý. | Nằm **bên ngoài** các phân vùng, rải rác giữa các tiến trình. |
| **Mô hình xuất hiện** | Thường gặp trong **Phân vùng cố định (Fixed Partition)** và **Phân trang (Paging)**.| Thường gặp trong **Phân vùng biến đổi (Dynamic Partition)** và **Phân đoạn (Segmentation)**. |
| **Biện pháp khắc phục**| Giảm kích thước phân vùng / khung trang; dùng phân vùng động. | Dùng kỹ thuật **Hợp nhất (통합)** hoặc **Nén bộ nhớ (압축 / Compaction)**. |

- **2. Bảng 3 chiến lược cấp phát bộ nhớ trống (기억장치 배치 전략):**

| Chiến lược cấp phát | Thuật ngữ Hàn / Anh | Tiêu chí lựa chọn khối nhớ | Ưu điểm & Nhược điểm chuẩn khảo thí |
| :--- | :--- | :--- | :--- |
| **First-Fit** | **최초 적합** | Chọn **khối trống đầu tiên** đủ lớn khi duyệt từ đầu bộ nhớ. | **Ưu điểm:** Tốc độ tìm kiếm nhanh nhất, chi phí thuật toán thấp nhất.<br>**Nhược điểm:** Dễ tập trung phân mảnh ở đầu bộ nhớ. |
| **Best-Fit** | **최적 적합** | Chọn khối trống có kích thước **nhỏ nhất** trong số các khối đủ chứa. | **Ưu điểm:** Tận dụng tối đa các khối nhớ nhỏ.<br>**Nhược điểm:** Để lại các mảnh phân mảnh ngoài siêu nhỏ không thể tái sử dụng. |
| **Worst-Fit** | **최악 적합** | Chọn khối trống có kích thước **lớn nhất** có sẵn trong bộ nhớ. | **Ưu điểm:** Mảnh thừa còn lại sau khi cắt vẫn đủ lớn để cấp cho tiến trình khác.<br>**Nhược điểm:** Phá vỡ các khối trống lớn có giá trị. |

- **3. Phân biệt kỹ thuật dọn dẹp: Hợp nhất (통합) vs Nén (압축):**
  - **Hợp nhất (통합 - Coalescing):** Khi một tiến trình kết thúc và giải phóng ô nhớ, hệ điều hành kiểm tra xem các ô nhớ nằm liền kề phía trước hoặc phía sau có trống không; nếu có thì **gộp ngay thành một khối trống lớn hơn**.
  - **Nén bộ nhớ (압축 - Compaction / Dồn bộ nhớ):** Hệ điều hành di chuyển cơ học tất cả các phân vùng đang hoạt động dồn về một đầu của RAM, giải phóng một vùng trống liên tục khổng lồ ở đầu còn lại. Thao tác này tiêu tốn nhiều thời gian xử lý và làm gián đoạn hệ thống.

- **주의/함정 (Bẫy đề thi):**
  - **Nhầm lẫn Best-Fit là tối ưu nhất:** Tên gọi là "Best-Fit (최적)" nhưng trên thực tế nó lại là giải thuật sinh ra nhiều mảnh vụn bộ nhớ vô dụng nhất (vì các mảnh thừa quá bé).
  - **First-Fit duyệt từ đâu:** First-Fit tiêu chuẩn luôn bắt đầu tìm kiếm từ khối nhớ trống đầu tiên của danh sách; biến thể **Next-Fit** sẽ tiếp tục tìm kiếm từ vị trí vừa cấp phát lần trước.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"First-Fit nhanh nhất chọn ngay khối đầu; Best-Fit khít nhất để mảnh thừa con; Worst-Fit chọn khối to đùng tái sinh mảnh lớn."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán trắc nghiệm cấp phát bộ nhớ chuẩn đề thi HRDK:
- **Đề bài:** Bộ nhớ chính hiện tại có 4 khối nhớ trống theo thứ tự địa chỉ:
  - Khối 1: `150 KB`
  - Khối 2: `300 KB`
  - Khối 3: `200 KB`
  - Khối 4: `450 KB`
  Một chương trình mới có kích thước `180 KB` yêu cầu nạp vào bộ nhớ. Hỏi theo từng chiến lược First-Fit, Best-Fit, Worst-Fit, chương trình sẽ được nạp vào khối nào và mảnh phân mảnh thừa lại là bao nhiêu?

- **Phân tích chi tiết từng chiến lược:**
  1. **First-Fit (최초 적합):**
     - Quét từ đầu: Khối 1 (150 KB) < 180 KB $\rightarrow$ Bỏ qua.
     - Đến Khối 2 (300 KB) $\ge$ 180 KB $\rightarrow$ **Chọn Khối 2 (300 KB)**.
     - Mảnh phân mảnh ngoài còn lại: $300 - 180 = \mathbf{120\text{ KB}}$.
  2. **Best-Fit (최적 적합):**
     - Các khối đủ chứa ($\ge 180$ KB): Khối 2 (300 KB), Khối 3 (200 KB), Khối 4 (450 KB).
     - Khối nhỏ nhất trong số đó là: **Khối 3 (200 KB)**.
     - Mảnh phân mảnh ngoài còn lại: $200 - 180 = \mathbf{20\text{ KB}}$ (vừa khít nhất).
  3. **Worst-Fit (최악 적합):**
     - Khối có dung lượng lớn nhất trong toàn bộ bộ nhớ là: **Khối 4 (450 KB)**.
     - Mảnh phân mảnh ngoài còn lại: $450 - 180 = \mathbf{270\text{ KB}}$ (mảnh thừa lớn nhất).

- **Bảng tổng hợp kết quả bài toán:**

| Chiến lược áp dụng | Khối nhớ được chọn | Dung lượng khối | Dung lượng mảnh thừa còn lại |
| :--- | :---: | :---: | :---: |
| **First-Fit (최초 적합)** | **Khối 2** | 300 KB | **120 KB** |
| **Best-Fit (최적 적합)** | **Khối 3** | 200 KB | **20 KB** |
| **Worst-Fit (최악 적합)** | **Khối 4** | 450 KB | **270 KB** |

---

### 복습 체크리스트
- [ ] Phân biệt rõ: Phân mảnh trong xảy ra bên trong phân vùng cấp phát, Phân mảnh ngoài xảy ra rải rác giữa các khối trống.
- [ ] Nhớ First-Fit (최초 적합) có tốc độ tìm kiếm nhanh nhất.
- [ ] Nhớ Best-Fit (최적 적합) chọn khối vừa khít nhất và sinh ra mảnh vụn nhỏ nhất.
- [ ] Nhớ Worst-Fit (최악 적합) chọn khối trống lớn nhất có sẵn.
- [ ] Giải thành thạo bài toán trắc nghiệm tính vị trí cấp phát và dung lượng mảnh thừa.
- [ ] Phân biệt được: Hợp nhất (통합) gộp các khối kề nhau, Nén (압축) di chuyển toàn bộ tiến trình về một phía.
