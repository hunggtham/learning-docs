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
| **Cục bộ thời gian** (시간 구역성 - Temporal) | Một ô nhớ vừa được truy xuất có xu hướng cao **sẽ được truy xuất lặp lại nhiều lần** trong tương lai gần. | Vòng lặp `for`, `while`; biến đếm tích lũy (`count++`, `sum`); ngăn xếp cuộc gọi hàm (Call Stack). |
| **Cục bộ không gian** (공간 구역성 - Spatial) | Các ô nhớ **nằm liền kề sát cạnh ô nhớ vừa truy xuất** có xu hướng cao sẽ được truy xuất kế tiếp. | Duyệt tuần tự mảng 1 chiều, 2 chiều; các câu lệnh thực thi tuần tự trong chương trình. |

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

#### 1. Minh chứng Nghịch lý Belady (Belady's Anomaly) trên giải thuật FIFO:

Nghịch lý Belady là hiện tượng xảy ra trên một số thuật toán thay thế trang (điển hình là FIFO): Khi **tăng số khung trang (Frame) được cấp phát**, số lần phát sinh lỗi trang (Page Fault) **lại tăng lên thay vì giảm đi**.

Cho chuỗi tham chiếu chuẩn của László Bélady (1969): `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5` (12 lượt truy xuất).

##### Trường hợp A: Cấp phát 3 Khung trang (FIFO với 3 Frames)

| Chuỗi | 1 | 2 | 3 | 4 | 1 | 2 | 5 | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Frame 1** | **1** | 1 | 1 | **4** | 4 | 4 | **5** | 5 | 5 | 5 | 5 | 5 |
| **Frame 2** | — | **2** | 2 | 2 | **1** | 1 | 1 | 1 | 1 | **3** | 3 | 3 |
| **Frame 3** | — | — | **3** | 3 | 3 | **2** | 2 | 2 | 2 | 2 | **4** | 4 |
| **Kết quả** | **F** | **F** | **F** | **F** | **F** | **F** | **F** | H | H | **F** | **F** | H |

- Tổng số lần Lỗi trang (Page Fault - F): **9 lần** (Số lần trúng - H: 3 lần).

##### Trường hợp B: Cấp phát 4 Khung trang (FIFO với 4 Frames)

| Chuỗi | 1 | 2 | 3 | 4 | 1 | 2 | 5 | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Frame 1** | **1** | 1 | 1 | 1 | 1 | 1 | **5** | 5 | 5 | 5 | **4** | 4 |
| **Frame 2** | — | **2** | 2 | 2 | 2 | 2 | 2 | **1** | 1 | 1 | 1 | **5** |
| **Frame 3** | — | — | **3** | 3 | 3 | 3 | 3 | 3 | **2** | 2 | 2 | 2 |
| **Frame 4** | — | — | — | **4** | 4 | 4 | 4 | 4 | 4 | **3** | 3 | 3 |
| **Kết quả** | **F** | **F** | **F** | **F** | H | H | **F** | **F** | **F** | **F** | **F** | **F** |

- Tổng số lần Lỗi trang (Page Fault - F): **10 lần** (Số lần trúng - H: 2 lần).
- **Kết luận:** Tăng khung trang từ 3 lên 4 khiến Page Fault tăng từ 9 lên 10. Nguyên nhân vì FIFO không phải là **Thuật toán ngăn xếp (Stack Algorithm)**: tập hợp trang trong $m$ khung không chứa tập con của $m-1$ khung.

#### 2. Bảng lần vết giải thuật LRU (Least Recently Used) và tính miễn nhiễm Belady:

Cùng chuỗi tham chiếu `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5` với **3 Khung trang** áp dụng LRU:

| Chuỗi | 1 | 2 | 3 | 4 | 1 | 2 | 5 | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Frame 1** | **1** | 1 | 1 | **4** | **1** | 1 | **5** | 5 | 5 | **3** | **4** | 4 |
| **Frame 2** | — | **2** | 2 | 2 | 2 | **2** | 2 | 2 | 2 | 2 | 2 | **5** |
| **Frame 3** | — | — | **3** | 3 | 3 | 3 | **1** | 1 | 1 | 1 | 1 | 1 |
| **Kết quả** | **F** | **F** | **F** | **F** | **F** | H | **F** | H | H | **F** | **F** | **F** |

- Với 3 frames, LRU sinh ra **10 lỗi trang**. Nhưng khi tăng lên 4 frames, LRU chỉ sinh ra **8 lỗi trang** (giảm đều đặn).
- **Quy tắc thi cử:** LRU và OPT là các **Thuật toán ngăn xếp (스택 알고리즘 - Stack Algorithms)** nên **tuyệt đối không bao giờ mắc nghịch lý Belady**.

#### 3. Bảng lần vết giải thuật LFU (Least Frequently Used):

LFU dựa trên số lần (tần suất) một trang được gọi trong quá khứ. Trang có bộ đếm tần số nhỏ nhất sẽ bị loại. Nếu tần số bằng nhau, áp dụng luật hòa FIFO (trang nạp trước bị thay trước).

Cho chuỗi tham chiếu: `1, 2, 3, 4, 2, 1, 5` với **3 Khung trang**:
- Bước 1: Nạp 1 $\rightarrow$ Frame: {1:1}, Lỗi trang F.
- Bước 2: Nạp 2 $\rightarrow$ Frame: {1:1, 2:1}, Lỗi trang F.
- Bước 3: Nạp 3 $\rightarrow$ Frame: {1:1, 2:1, 3:1}, Lỗi trang F.
- Bước 4: Yêu cầu 4 $\rightarrow$ Cả 1, 2, 3 đều có tần số = 1. Xét FIFO: 1 nạp sớm nhất $\rightarrow$ **Thay trang 1 bằng 4** (Frame: {4:1, 2:1, 3:1}), Lỗi trang F.
- Bước 5: Yêu cầu 2 $\rightarrow$ Trang 2 đã có sẵn (Hit H) $\rightarrow$ Tần số trang 2 tăng lên 2 (Frame: {4:1, 2:2, 3:1}).
- Bước 6: Yêu cầu 1 $\rightarrow$ Cần thay trang. Tần số: 4 có 1, 3 có 1, 2 có 2. Trong hai trang có tần số nhỏ nhất {4, 3}, trang 3 vào trước trang 4 $\rightarrow$ **Thay trang 3 bằng 1** (Frame: {4:1, 2:2, 1:1}), Lỗi trang F.
- Bước 7: Yêu cầu 5 $\rightarrow$ Cần thay trang. Tần số: 4 có 1, 1 có 1, 2 có 2. Giữa {4, 1}, trang 4 vào trước $\rightarrow$ **Thay trang 4 bằng 5** (Frame: {5:1, 2:2, 1:1}), Lỗi trang F.

#### 4. Bảng phân loại 4 lớp ưu tiên trong giải thuật NUR (Not Used Recently):

NUR sử dụng 2 bit phần cứng kết hợp cho mỗi trang:
- **Bit tham chiếu ($r$ - Reference bit):** Đặt bằng 1 khi trang được đọc hoặc ghi; đặt bằng 0 định kỳ bởi đồng hồ hệ thống.
- **Bit sửa đổi ($m$ - Modified/Dirty bit):** Đặt bằng 1 khi nội dung trang bị thay đổi (cần ghi lại đĩa khi tráo ra); đặt bằng 0 khi nạp vào.

| Lớp ưu tiên | Cặp bit $(r, m)$ | Trạng thái kỹ thuật | Đánh giá thay thế |
| :---: | :---: | :--- | :--- |
| **Cấp độ 1** | **$(0, 0)$** | Gần đây không tham chiếu, không bị sửa đổi. | **Ưu tiên thay thế số 1** (Tốt nhất vì không tốn I/O ghi đĩa). |
| **Cấp độ 2** | **$(0, 1)$** | Gần đây không tham chiếu, nhưng đã bị sửa đổi. | Ưu tiên thay thế số 2 (Phải ghi đĩa trước khi thay). |
| **Cấp độ 3** | **$(1, 0)$** | Gần đây có tham chiếu, không bị sửa đổi. | Ưu tiên thay thế số 3 (Trang đang tích cực đọc). |
| **Cấp độ 4** | **$(1, 1)$** | Gần đây có tham chiếu, và đã bị sửa đổi. | **Ưu tiên thay thế cuối cùng** (Trang đang hoạt động rất mạnh). |

#### 5. Đồ thị mối quan hệ giữa Mức độ đa nhiệm và Hiệu suất CPU (Thrashing Point):
$$\text{Hiệu suất CPU} \uparrow \text{ Tăng dần đến điểm tới hạn } \longrightarrow \mathbf{\text{Điểm gãy gục (Thrashing Point)}} \longrightarrow \downarrow \text{ Rơi thẳng đứng}$$

- Khi tăng số tiến trình đa nhiệm, ban đầu hiệu suất CPU tăng tuyến tính vì tận dụng tốt thời gian rảnh rỗi.
- Khi vượt quá ngưỡng dung lượng RAM chịu tải, hệ điều hành rơi vào điểm Thrashing $\rightarrow$ CPU chỉ bận rộn chờ I/O nạp trang, hiệu suất rơi tự do về 0.

---

### 복습 체크리스트
- [ ] Phân biệt được: Phân trang (Paging) sinh phân mảnh trong, Phân đoạn (Segmentation) sinh phân mảnh ngoài.
- [ ] Thuộc lòng đặc điểm các thuật toán: OPT (tối ưu tương lai), FIFO (nghịch lý Belady), LRU (lâu nhất quá khứ), LFU (ít lần nhất).
- [ ] Nhớ thứ tự ưu tiên thay trang của NUR: $(0,0) \rightarrow (0,1) \rightarrow (1,0) \rightarrow (1,1)$.
- [ ] Nắm vững định nghĩa Thrashing: Thời gian tráo trang lớn hơn thời gian chạy lệnh.
- [ ] Phân biệt được: Cục bộ thời gian (vòng lặp, biến đếm) vs Cục bộ không gian (duyệt mảng, tuần tự).
- [ ] Kể tên 2 giải pháp chống Thrashing: Working Set (tập làm việc) và PFF (tần số lỗi trang).
