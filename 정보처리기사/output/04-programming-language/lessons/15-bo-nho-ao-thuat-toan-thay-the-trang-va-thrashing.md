# 가상기억장치, 페이지 교체 알고리즘 및 스래싱 (Bộ nhớ ảo, Thay thế trang & Thrashing)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Bộ nhớ ảo (가상기억장치 - Virtual Memory) và phân biệt sự khác nhau giữa Phân trang (페이징 - Paging, kích thước cố định, phân mảnh trong) và Phân đoạn (세그멘테이션 - Segmentation, kích thước biến đổi, phân mảnh ngoài).
- Hiểu và lần vết thành thạo các thuật toán thay thế trang kinh điển: OPT (lý thuyết tối ưu), FIFO (nghịch lý Belady), LRU (lâu nhất chưa dùng), LFU (ít dùng nhất), NUR (2 bit tham chiếu/sửa đổi).
- Thấu hiểu hiện tượng trì trệ tráo trang Thrashing (스래싱), Nguyên lý cục bộ (구역성 - Locality: Thời gian vs Không gian) và các cơ chế phòng chống Thrashing: Tập làm việc (워킹 셋 - Working Set) và Tần số lỗi trang (PFF).

## 핵심 키워드 (Từ khóa)
- 가상기억장치 (Virtual Memory) — Cho phép chạy chương trình lớn hơn bộ nhớ RAM vật lý.
- 페이징 vs 세그멘테이션 (Paging vs Segmentation) — Trang cố định (phân mảnh trong) vs Đoạn biến đổi (phân mảnh ngoài).
- 페이지 교체 알고리즘 (Page Replacement Algorithms) — OPT, FIFO (Belady 모순), LRU, LFU, NUR.
- 스래싱 (Thrashing) — Tiến trình tốn thời gian tráo trang (Paging) nhiều hơn thời gian thực thi CPU.
- 구역성 (Locality / 국부성) — Cục bộ thời gian (시간 구역성) vs Cục bộ không gian (공간 구역성).
- 워킹 셋 & PFF (Working Set & Page Fault Frequency) — Các biện pháp kiểm soát phân bổ khung trang chống Thrashing.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `14-quan-ly-bo-nho-thuc-va-chien-luoc-cap-phat.md`, khi bộ nhớ vật lý RAM bị giới hạn dung lượng hoặc phân mảnh ngoài nghiêm trọng, Hệ điều hành bắt buộc phải ứng dụng kỹ thuật bộ nhớ ảo.
- **Đang giải quyết gì (Current Problem):** Giải quyết hai câu hỏi tính toán lớn nhất của phần Quản lý bộ nhớ: Cho một chuỗi tham chiếu trang và số khung trang, thuật toán nào sinh ra bao nhiêu lỗi trang (Page Fault); và vì sao máy tính bị đơ giật khi mở quá nhiều ứng dụng nặng cùng lúc.
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn tất toàn bộ kiến thức về Hệ điều hành và quản lý tài nguyên nội tại máy tính, chương trình sẽ bước sang phân khu mạng máy tính để kết nối các máy tính với nhau qua mô hình OSI 7 tầng ở bài `16-mang-may-tinh-osi-7-tang-va-giao-thuc.md`.

## 읽는 방법 (Cách đọc)
- **Paging vs Segmentation:**
  - Paging = Khối **cố định** $\rightarrow$ Dính lỗi **Phân mảnh trong (내부)**.
  - Segmentation = Khối **thay đổi theo logic** $\rightarrow$ Dính lỗi **Phân mảnh ngoài (외부)**.
- **Thuật toán thay thế trang:**
  - **OPT:** Nhìn về **TƯƠNG LAI**, chọn trang lâu nhất sau này mới dùng $\rightarrow$ Tỷ lệ lỗi trang thấp nhất.
  - **FIFO:** Vào trước ra trước $\rightarrow$ Dính hiện tượng **Belady의 모순 (tăng khung trang mà lỗi trang lại tăng)**.
  - **LRU:** Nhìn về **QUÁ KHỨ**, trang nào lâu nhất chưa được đụng tới thì đuổi đi.
  - **LFU:** Đếm **SỐ LẦN**, trang nào ít được gọi nhất thì đuổi đi.
- **Locality:** Vòng lặp `for`, biến đếm `sum` $\rightarrow$ Cục bộ **thời gian**; duyệt mảng tuần tự $\rightarrow$ Cục bộ **không gian**.

---

## 가상기억장치, 페이지 교체 알고리즘 및 스래싱

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `페이징은 내부 단편화, 세그멘테이션은 외부 단편화가 발생한다. FIFO는 프레임 수가 증가해도 페이지 부재가 증가하는 Belady의 모순이 발생하고, LRU는 최근에 가장 오랫동안 사용되지 않은 페이지를 교체한다. 스래싱은 페이지 교체 시간이 프로세스 실행 시간보다 커지는 현상이며 구역성(Locality)과 워킹 셋으로 방지한다.`
  - [Tiếng Việt]: Phân trang phát sinh phân mảnh trong, phân đoạn phát sinh phân mảnh ngoài. FIFO có thể gặp nghịch lý Belady khi tăng khung trang nhưng lỗi trang lại tăng, còn LRU thay thế trang lâu nhất chưa được sử dụng gần đây. Thrashing là hiện tượng thời gian tráo trang lớn hơn thời gian chạy lệnh CPU, được phòng chống nhờ tính cục bộ và Working Set.

- **1. Bảng đối chiếu Phân trang (Paging) vs Phân đoạn (Segmentation):**

| Tiêu chuẩn so sánh | Phân trang (페이징 - Paging) | Phân đoạn (세그멘테이션 - Segmentation) |
| :--- | :--- | :--- |
| **Kích thước khối chia** | **Kích thước cố định (Fixed Size)** bằng nhau. | **Kích thước biến đổi (Variable Size)** theo logic. |
| **Đơn vị phân chia** | Đơn vị vật lý độc lập với mã nguồn (Page). | Đơn vị logic có ý nghĩa: Hàm, Mảng, Lớp. |
| **Loại phân mảnh phát sinh**| **Chỉ phát sinh Phân mảnh trong (내부 단편화)** ở trang cuối cùng. | **Chỉ phát sinh Phân mảnh ngoài (외부 단편화)** giữa các đoạn. |
| **Bảo vệ & Chia sẻ mã** | Khó chia sẻ vì trang bị cắt ngang logic. | **Rất dễ chia sẻ và bảo vệ** theo từng hàm/module. |

- **2. Bảng các thuật toán thay thế trang (페이지 교체 알고리즘):**

| Thuật toán | Tiêu chuẩn chọn trang thay thế | Đặc điểm thi cử trọng tâm HRDK |
| :--- | :--- | :--- |
| **OPT (Tối ưu)** | Trang có thời gian tham chiếu **xa nhất trong tương lai**. | Đạt tỷ lệ lỗi trang thấp nhất; chỉ mang tính lý thuyết đối chuẩn. |
| **FIFO** | Trang được nạp vào bộ nhớ **sớm nhất trong quá khứ**. | Dễ cài đặt; xuất hiện **Nghịch lý Belady (Belady의 모순)**. |
| **LRU** | Trang **lâu nhất chưa được truy xuất** trong quá khứ. | Dựa trên thời gian/timestamp; giải thuật thực tế hiệu quả nhất. |
| **LFU** | Trang có **tần suất (số lần) tham chiếu ít nhất**. | Dựa trên bộ đếm số lần sử dụng trong quá khứ. |
| **NUR** | Dựa trên 2 bit: **Bit tham chiếu $r$** và **Bit sửa đổi $m$**. | Thứ tự ưu tiên thay: $(0,0) \rightarrow (0,1) \rightarrow (1,0) \rightarrow (1,1)$. |
| **SCR (Clock)** | Dùng biến thể FIFO kết hợp bit tham chiếu cho cơ hội 2. | Nếu bit tham chiếu bằng 1 thì xóa về 0 và bỏ qua, tìm trang khác. |

- **3. Bảng phân loại Nguyên lý cục bộ (구역성 / 국부성 - Locality của Denning):**

| Loại hình cục bộ | Bản chất nguyên lý | Hiện tượng mã nguồn đại diện trong đề thi |
| :--- | :--- | :--- |
| **Cục bộ thời gian**<br>(시간 구역성 - Temporal) | Một ô nhớ vừa được truy xuất có xu hướng cao **sẽ được truy xuất lặp lại nhiều lần** trong tương lai gần. | • Vòng lặp `for`, `while`.<br>• Biến đếm tích lũy (`count++`, `sum`).<br>• Ngăn xếp cuộc gọi hàm (Call Stack). |
| **Cục bộ không gian**<br>(공간 구역성 - Spatial) | Các ô nhớ **nằm liền kề sát cạnh ô nhớ vừa truy xuất** có xu hướng cao sẽ được truy xuất kế tiếp. | • Duyệt tuần tự mảng 1 chiều, 2 chiều.<br>• Các câu lệnh thực thi tuần tự trong chương trình. |

- **4. Hiện tượng Thrashing (스래싱) và giải pháp phòng ngừa:**
  - **Khái niệm:** Trạng thái hệ thống tốn phần lớn thời gian cho việc đọc/ghi tráo đổi trang giữa RAM và đĩa cứng (Paging I/O) thay vì thực thi chỉ thị của CPU, khiến hiệu suất CPU giảm đột ngột về gần bằng 0.
  - **Nguyên nhân chính:** Mức độ đa nhiệm (**다중 프로그래밍 정도 - Degree of Multiprogramming**) quá cao khiến số khung trang phân bổ cho mỗi tiến trình quá ít, liên tục phát sinh lỗi trang (Page Fault).
  - **Biện pháp phòng ngừa:**
    - **Tập làm việc (워킹 셋 - Working Set):** Giữ toàn bộ tập hợp các trang thường xuyên được tham chiếu trong cửa sổ thời gian $\Delta$ thường trú trong RAM.
    - **Tần số lỗi trang (PFF - Page Fault Frequency):** Thiết lập ngưỡng trên và ngưỡng dưới cho tỷ lệ lỗi trang; nếu vượt ngưỡng trên thì cấp thêm khung trang, dưới ngưỡng dưới thì thu hồi bớt khung trang.

- **주의/함정 (Bẫy đề thi):**
  - **Nghịch lý Belady (Belady의 모순):** Là hiện tượng đặc thù của **FIFO**; thông thường tăng khung trang thì lỗi trang phải giảm, nhưng với FIFO có những trường hợp tăng từ 3 lên 4 khung trang thì số lỗi trang lại **TĂNG LÊN** (ví dụ từ 9 lên 10 lỗi).
  - **NUR cấp độ (0,0):** Trang có $r=0$ (chưa đọc) và $m=0$ (chưa sửa) là trang được ưu tiên thay thế đầu tiên vì không cần ghi lại đĩa (tiết kiệm I/O).

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Paging phân mảnh trong, Segmentation phân mảnh ngoài; Belady nghịch lý của FIFO, LRU lâu nhất chưa dùng; Thrashing nghẽn tráo trang, chặn bằng Working Set."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán trắc nghiệm lần vết lỗi trang (Page Fault Trace) chuẩn đề thi:
- **Đề bài:** Cho chuỗi tham chiếu trang: `1, 2, 3, 1, 2, 4, 1, 2, 5`. Hệ thống có **3 khung trang (Page Frames)** ban đầu đều trống. Hỏi có bao nhiêu lần xảy ra lỗi trang (Page Fault) khi áp dụng thuật toán **LRU (Least Recently Used)**?

*Bảng lần vết trạng thái 3 khung trang qua từng bước:*

| Chuỗi tham chiếu | $1$ | $2$ | $3$ | $1$ | $2$ | $4$ | $1$ | $2$ | $5$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Khung trang 1** | **1** | 1 | 1 | 1 | 1 | **4** | 4 | 4 | **5** |
| **Khung trang 2** | — | **2** | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| **Khung trang 3** | — | — | **3** | 3 | 3 | 3 | **1** | 1 | 1 |
| **Xảy ra Lỗi trang?**| **Có (F)**| **Có (F)**| **Có (F)**| Không | Không | **Có (F)**| **Có (F)**| Không | **Có (F)**|

- **Chi tiết các bước thay thế:**
  - Bước 1, 2, 3: Nạp 1, 2, 3 vào khung trống $\rightarrow$ 3 lần lỗi trang ban đầu (Cold Fault).
  - Bước 4, 5: Trang 1 và 2 đã có sẵn $\rightarrow$ Không lỗi trang; cập nhật 1 và 2 là vừa dùng gần nhất (trang 3 trở thành lâu nhất chưa dùng).
  - Bước 6: Cần trang 4. Trong {1, 2, 3}, trang 3 là lâu nhất chưa dùng $\rightarrow$ **Thay trang 3 bằng 4** (Lỗi trang lần 4).
  - Bước 7: Cần trang 1. Trong {1, 2, 4}, trang 1 vừa dùng ở bước 4, trang 2 ở bước 5, trang 4 ở bước 6. Khung 1 chứa 4, khung 2 chứa 2, khung 3 chứa 3 cũ $\rightarrow$ **Thay trang 4/1 theo timestamp** $\rightarrow$ Lỗi trang lần 5.
  - Bước 9: Cần trang 5 $\rightarrow$ Lỗi trang lần 6.
- **Tổng số lần lỗi trang:** **6 lần**.

#### 2. Đồ thị mối quan hệ giữa Mức độ đa nhiệm và Hiệu suất CPU:
$$\text{Hiệu suất CPU} \uparrow \text{ Tăng dần đến điểm tới hạn } \longrightarrow \mathbf{\text{Điểm gãy gục (Thrashing Point)}} \longrightarrow \downarrow \text{ Rơi thẳng đứng}$$

- Khi tăng số tiến trình đa nhiệm, ban đầu hiệu suất CPU tăng tuyến tính.
- Nhưng khi vượt quá ngưỡng dung lượng RAM chịu tải, hệ điều hành rơi vào điểm Thrashing $\rightarrow$ CPU chỉ bận rộn chờ I/O nạp trang, hiệu suất rơi tự do về 0.

---

### 복습 체크리스트
- [ ] Phân biệt được: Phân trang (Paging) sinh phân mảnh trong, Phân đoạn (Segmentation) sinh phân mảnh ngoài.
- [ ] Thuộc lòng đặc điểm các thuật toán: OPT (tối ưu tương lai), FIFO (nghịch lý Belady), LRU (lâu nhất quá khứ), LFU (ít lần nhất).
- [ ] Nhớ thứ tự ưu tiên thay trang của NUR: $(0,0) \rightarrow (0,1) \rightarrow (1,0) \rightarrow (1,1)$.
- [ ] Nắm vững định nghĩa Thrashing: Thời gian tráo trang lớn hơn thời gian chạy lệnh.
- [ ] Phân biệt được: Cục bộ thời gian (vòng lặp, biến đếm) vs Cục bộ không gian (duyệt mảng, tuần tự).
- [ ] Kể tên 2 giải pháp chống Thrashing: Working Set (tập làm việc) và PFF (tần số lỗi trang).
