# 메모리 관리 기법 및 스토리지 시스템 (Quản lý bộ nhớ ảo, Thuật toán thay thế trang & Hệ thống lưu trữ RAID, DAS/NAS/SAN)

## 학습 목표 (Mục tiêu)
- Phân biệt 3 chiến lược nạp bộ nhớ: **First Fit** (nhanh nhất), **Best Fit** (khít nhất, để lại mảnh vụn nhỏ), và **Worst Fit** (vào vùng trống lớn nhất).
- Phân biệt bản chất của hai mô hình quản lý bộ nhớ ảo: **Phân trang (Paging)** với kích thước khối cố định (chỉ sinh phân mảnh nội vi) và **Phân đoạn (Segmentation)** với kích thước khối logic biến đổi (chỉ sinh phân mảnh ngoại vi).
- Làm chủ các thuật toán thay thế trang: Tối ưu lý thuyết (**OPT**), Nhập trước xuất trước (**FIFO**) và Nghịch lý Belady, Ít sử dụng gần đây nhất (**LRU**), và Tần suất sử dụng thấp nhất (**LFU**).
- Thấu hiểu bản chất của Tính cục bộ tham chiếu (**Locality**: Thời gian vs Không gian), Mô hình tập làm việc (**Working Set**), và Hiện tượng đập trang (**스래싱 - Thrashing**).
- Phân biệt 3 kiến trúc lưu trữ dữ liệu doanh nghiệp: **DAS** (gắn trực tiếp), **NAS** (truy xuất cấp tệp qua NFS/CIFS), và **SAN** (truy xuất cấp khối quang qua FC-SAN/iSCSI).
- Phân tích chi tiết khả năng chịu lỗi, hiệu năng và dung lượng sử dụng của các cấp độ mảng đĩa **RAID 0, 1, 5, 6, 10**.

## 핵심 키워드 (Từ khóa song ngữ)
- 배치 전략 (Placement Strategies — 최초 적합 First Fit, 최적 적합 Best Fit, 최악 적합 Worst Fit)
- 페이징 (Paging — 고정 크기 블록, 내부 단편화 발생, 외부 단편화 없음)
- 세그멘테이션 (Segmentation — 가변 크기 논리 블록, 외부 단편화 발생, 내부 단편화 없음)
- 페이지 교체 알고리즘 (Page Replacement — OPT 최적, FIFO 벨레이디 모순, LRU 최근최소사용, LFU 사용빈도)
- 국부성 (Locality — 시간 구역성 Temporal: Loop/Stack vs 공간 구역성 Spatial: Array/순차코드)
- 워킹 셋 (Working Set — Peter Denning, 프로세스가 자주 참조하는 페이지 집합)
- 스래싱 (Thrashing — Paging 과다로 CPU 이용률이 급감하는 현상, 다중 프로그래밍 과도)
- 스토리지 아키텍처 (Storage — DAS 직접연결, NAS 파일레벨 NFS/CIFS, SAN 블록레벨 광채널)
- RAID 레벨 (RAID 0 스트라이핑, RAID 1 미러링 50%, RAID 5 패리티 분산 1디스크 복구, RAID 6 2디스크 복구)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi các tiến trình được lập lịch CPU tại [13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md](13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md), hệ điều hành phải cấp phát không gian địa chỉ bộ nhớ RAM cho tiến trình đó và tổ chức lưu trữ bền vững các tệp tin trên hệ thống đĩa.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết toàn bộ bài toán tối ưu hóa bộ nhớ: giải quyết hiện tượng phân mảnh, thuật toán hoán đổi trang khi RAM bị đầy, chống hiện tượng sập hiệu năng Thrashing, và kiến trúc các mảng đĩa lưu trữ dự phòng RAID trong trung tâm dữ liệu.
- **Dùng đi đâu (Forward Handoff):** Hệ thống lưu trữ và bộ nhớ vật lý này là nơi đặt nền móng vận hành các hệ quản trị cơ sở dữ liệu và xử lý phân tán Big Data tại [15-quan-tri-co-so-du-lieu-va-big-data.md](15-quan-tri-co-so-du-lieu-va-big-data.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Paging vs Segmentation (Bẫy đề thi kinh điển):**
  - **Paging (Phân trang):** Kích thước **CỐ ĐỊNH (고정 크기)** $\rightarrow$ **CHỈ sinh phân mảnh nội vi (내부 단편화)**, không có phân mảnh ngoại vi.
  - **Segmentation (Phân đoạn):** Kích thước **THAY ĐỔI (가변 크기)** $\rightarrow$ **CHỈ sinh phân mảnh ngoại vi (외부 단편화)**, không có phân mảnh nội vi.
- **Thuật toán thay thế trang:**
  - Nhắc đến **"Tăng số khung trang nhưng lỗi thiếu trang lại TĂNG lên"** $\rightarrow$ Chọn **FIFO (Belady's Anomaly)**.
  - Nhắc đến **"Thay thế trang có thời gian từ lần truy cập gần nhất lâu nhất"** $\rightarrow$ Chọn **LRU**.
  - Nhắc đến **"Thay thế trang có số lần/tần suất truy cập ít nhất"** $\rightarrow$ Chọn **LFU**.
- **Hiện tượng Thrashing (스래싱):**
  - Dấu hiệu nhận diện: **CPU 이용률이 급격히 저하 (Hiệu năng CPU giảm đột ngột)** do hệ thống bận **hoán đổi trang liên tục (Paging/Swapping)**.
  - Nguyên nhân: **다중 프로그래밍 정도(Degree of Multiprogramming)가 지나치게 높음** (nạp quá nhiều tiến trình làm cạn kiệt RAM).
- **Kiến trúc Lưu trữ (Storage):**
  - Truy xuất cấp độ **Tệp tin (File-Level)** qua mạng LAN, dùng giao thức **NFS / CIFS** $\rightarrow$ Chọn **NAS**.
  - Truy xuất cấp độ **Khối dữ liệu (Block-Level)** qua mạng cáp quang riêng biệt **Fibre Channel** $\rightarrow$ Chọn **SAN**.
- **Cấp độ RAID:**
  - RAID 0: Không có dự phòng, tốc độ nhanh nhất.
  - RAID 1: Dung lượng 50%, an toàn cao.
  - RAID 5: Phân tán Parity, chịu được hỏng **1 đĩa**, dung lượng $(N-1) \times \text{Size}$.
  - RAID 6: Hai Parity độc lập, chịu được hỏng **2 đĩa đồng thời**, dung lượng $(N-2) \times \text{Size}$.

---

## 메모리 관리 기법 및 스토리지 시스템

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Chiến lược bố trí bộ nhớ chính (Placement Strategies)
Khi một tiến trình mới cần nạp vào RAM, hệ điều hành chọn vùng nhớ trống (Hole) theo 3 chiến lược:
- **1. 최초 적합 (First Fit - Khớp đầu tiên):** Nạp tiến trình vào vùng nhớ trống đầu tiên đủ lớn tìm thấy từ đầu danh sách; **tốc độ tìm kiếm nhanh nhất**.
- **2. 최적 적합 (Best Fit - Khớp khít nhất):** Quét toàn bộ danh sách để tìm vùng nhớ trống có dung lượng nhỏ nhất nhưng vẫn đủ nạp tiến trình; để lại các mảnh phân mảnh nội/ngoại vi có kích thước rất nhỏ.
- **3. 최악 적합 (Worst Fit - Khớp tệ nhất):** Quét toàn bộ để nạp tiến trình vào vùng nhớ trống có dung lượng lớn nhất còn dư; để lại phần thừa lớn có khả năng tái sử dụng cho tiến trình khác.

#### 2. Đối chiếu hai kỹ thuật quản lý bộ nhớ ảo: Phân trang vs Phân đoạn

| Tiêu chí kỹ thuật | Phân trang (페이징 - Paging) | Phân đoạn (세그멘테이션 - Segmentation) |
| :--- | :--- | :--- |
| **Đơn vị phân chia** | Chia không gian logic thành các khối có kích thước **CỐ ĐỊNH (고정 크기)** bằng nhau gọi là **Trang (Page)**; RAM chia thành các **Khung trang (Page Frame)**. | Chia không gian logic thành các khối có kích thước **THAY ĐỔI (가변 크기)** theo đơn vị logic chức năng (Hàm `main`, Mảng dữ liệu, Ngăn xếp Stack). |
| **Hiện tượng phân mảnh** | **CHỈ XẢY RA Phân mảnh nội vi (내부 단편화)** ở trang cuối cùng của tiến trình; hoàn toàn không có phân mảnh ngoại vi. | **CHỈ XẢY RA Phân mảnh ngoại vi (외부 단편화)** khi khoảng trống giữa các segment không đủ nạp segment mới; không có phân mảnh nội vi. |
| **Địa chỉ logic** | Địa chỉ gồm: Số hiệu trang ($p$) và Độ lệch ($d$). | Địa chỉ gồm: Số hiệu đoạn ($s$) và Độ lệch ($d$). |
| **Bảo vệ và Chia sẻ** | Khó thực hiện vì ranh giới trang là cơ học, không trùng với ranh giới logic của hàm/dữ liệu. | Rất dễ thực hiện bảo vệ và chia sẻ mã nguồn dùng chung giữa các tiến trình. |

#### 3. Các thuật toán thay thế trang (Page Replacement Algorithms)
Khi xảy ra lỗi thiếu trang (**페이지 부재 - Page Fault**) mà bộ nhớ RAM đã đầy, hệ điều hành phải chọn một trang nạn nhân (Victim Page) để đẩy về đĩa cứng:

| Thuật toán | Tên tiếng Hàn & Anh | Cơ chế vận hành & Điểm thi trọng tâm |
| :--- | :--- | :--- |
| **Tối ưu lý thuyết** | **OPT (Optimal)** | Thay thế trang mà **trong tương lai xa nhất sẽ không được tham chiếu tới**. Cho tỷ lệ Page Fault thấp nhất nhưng **không thể hiện thực hóa trong thực tế** vì không thể đoán trước tương lai (dùng làm chuẩn đối sánh). |
| **Nhập trước xuất trước** | **FIFO (First-In First-Out)** | Trang nào được nạp vào RAM trước thì bị đẩy ra trước.<br>$\implies$ Gặp hiện tượng **Nghịch lý Belady (Belady's Anomaly)**: Đôi khi tăng thêm số khung trang RAM cấp phát cho tiến trình lại làm tăng số lỗi thiếu trang. |
| **Ít sử dụng gần đây** | **LRU (Least Recently Used)** | Thay thế trang có **thời gian từ lần truy cập gần nhất lâu nhất** (dựa trên nguyên lý quá khứ gần). Là thuật toán phổ biến và hiệu quả nhất trong thực tế. |
| **Tần suất thấp nhất** | **LFU (Least Frequently Used)** | Thay thế trang có **tổng số lần (tần suất) được tham chiếu ít nhất** kể từ khi nạp vào RAM. |
| **Chưa dùng gần đây** | **NUR (Not Used Recently)** | Sử dụng 2 bit trạng thái: Bit tham chiếu ($r$) và Bit sửa đổi ($m$) để phân thành 4 nhóm ưu tiên thay thế: $(0,0) \rightarrow (0,1) \rightarrow (1,0) \rightarrow (1,1)$. |

#### 4. Tính cục bộ (Locality), Tập làm việc (Working Set) & Hiện tượng đập trang (Thrashing)
- **Tính cục bộ tham chiếu (Locality / 구역성):**
  - **시간 구역성 (Temporal Locality - Cục bộ thời gian):** Một ô nhớ vừa được truy cập thì có xu hướng sẽ được truy cập lại nhiều lần trong tương lai gần (các biến đếm trong vòng lặp Loop, ngăn xếp Stack, chương trình con thường gọi).
  - **공간 구역성 (Spatial Locality - Cục bộ không gian):** Một ô nhớ vừa được truy cập thì các ô nhớ có địa chỉ liền kề nó có xu hướng sẽ được truy cập tiếp theo (duyệt tuần tự các phần tử mảng Array, thực thi khối lệnh tuần tự).
- **Mô hình tập làm việc (Working Set Model - Peter Denning):**
  - Tập hợp tất cả các trang bộ nhớ mà một tiến trình tham chiếu thường xuyên trong một khoảng thời gian trượt xác định $\Delta$.
  - Nếu hệ điều hành cấp phát đủ số khung trang để giữ toàn bộ Working Set của tiến trình trong RAM, tỷ lệ lỗi thiếu trang sẽ giảm xuống mức tối thiểu.
- **Hiện tượng đập trang (스래싱 - Thrashing):**
  - **핵심 원리 (Nguyên tắc cốt lõi):**
    - [Tiếng Hàn]: `스래싱(Thrashing)은 프로세스 실행 시간보다 페이지 교체에 소요되는 시간이 더 많아져 CPU 이용률이 급격히 떨어지는 현상이다.`
    - [Tiếng Việt]: Thrashing là hiện tượng hệ thống dành phần lớn thời gian CPU chỉ để hoán đổi trang qua lại giữa RAM và đĩa cứng thay vì xử lý lệnh thực tế, khiến hiệu suất sử dụng CPU tụt dốc thê thảm về gần 0.
    - *Nguyên nhân chính:* Nạp quá nhiều tiến trình vào RAM cùng lúc (Đa chương trình hóa quá mức - Degree of Multiprogramming quá cao) làm cho mỗi tiến trình không đủ khung trang tối thiểu để chứa Working Set.
    - *Giải pháp:* Giảm bớt số lượng tiến trình đa nhiệm, trang bị thêm RAM, hoặc áp dụng cơ chế giám sát Tần suất lỗi trang (**PFF - Page Fault Frequency**).

#### 5. Kiến trúc hệ thống lưu trữ (Storage) và Mảng đĩa RAID

| Kiến trúc lưu trữ | Tên tiếng Hàn & Anh | Cơ chế kết nối & Giao thức truyền thông | Ưu nhược điểm đề thi |
| :--- | :--- | :--- | :--- |
| **DAS** | **Direct Attached Storage** | Ổ đĩa gắn trực tiếp vào máy chủ thông qua cáp chuyên dụng chuyên biệt (SATA, SAS, SCSI). | Tốc độ truyền tải rất cao, dễ lắp đặt; nhược điểm khó chia sẻ dữ liệu giữa nhiều máy chủ, giới hạn khoảng cách cáp. |
| **NAS** | **Network Attached Storage** | Thiết bị lưu trữ độc lập kết nối vào mạng LAN nội bộ qua Switch; phục vụ truy xuất ở cấp độ **Tệp tin (File-Level Access)** qua các giao thức **NFS** (Linux/UNIX) và **CIFS / SMB** (Windows). | Dễ dàng chia sẻ tệp qua mạng văn phòng; nhược điểm lưu lượng lưu trữ cạnh tranh băng thông với mạng LAN. |
| **SAN** | **Storage Area Network** | Mạng lưu trữ chuyên dụng tốc độ cao tách biệt hoàn toàn với mạng LAN; phục vụ truy xuất ở cấp độ **Khối dữ liệu (Block-Level Access)** qua mạng cáp quang **Fibre Channel (FC-SAN)** hoặc **iSCSI (IP-SAN)**. | Tốc độ cực cao, không làm nghẽn mạng LAN, khả năng mở rộng không giới hạn; chi phí đầu tư thiết bị rất đắt đỏ. |

- **Bảng đối chiếu các cấp độ mảng đĩa RAID (Redundant Array of Independent Disks):**

| Cấp độ RAID | Kỹ thuật cốt lõi | Khả năng chịu lỗi đĩa | Dung lượng lưu trữ khả dụng |
| :---: | :--- | :---: | :---: |
| **RAID 0** | **Striping (Ghi xen kẽ)**: Chia nhỏ dữ liệu ghi đồng thời lên nhiều đĩa để tăng tốc độ. | **Không có dự phòng** (1 đĩa hỏng là mất sạch dữ liệu). | **$100\%$** ($N \times \text{Size}$) |
| **RAID 1** | **Mirroring (Ghi bản sao)**: Ghi bản sao giống hệt sang đĩa thứ hai để dự phòng an toàn. | Hỏng được **1 đĩa**. | **$50\%$** |
| **RAID 5** | **Striping + Distributed Parity**: Phân tán các khối chẵn lẻ Parity trên tất cả các đĩa cứng. | Hỏng tối đa **1 đĩa cứng** (Tối thiểu cần 3 đĩa). | **$(N - 1) \times \text{Size}$** |
| **RAID 6** | **Dual Parity**: Sử dụng 2 khối Parity độc lập bằng 2 thuật toán khác nhau. | Hỏng đồng thời tối đa **2 đĩa cứng** (Tối thiểu cần 4 đĩa). | **$(N - 2) \times \text{Size}$** |
| **RAID 10** | **Mirroring rồi Striping (RAID 1 + 0)**: Kết hợp tốc độ của RAID 0 và an toàn của RAID 1. | Chịu hỏng đĩa ở các cặp mirror khác nhau (Tối thiểu cần 4 đĩa). | **$50\%$** |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Cơ chế khôi phục dữ liệu bằng phép toán XOR trong RAID 5
Trong RAID 5, bit chẵn lẻ Parity $P$ được tính bằng phép toán XOR giữa các bit dữ liệu:
$$P = D_1 \oplus D_2 \oplus D_3$$
- Nếu một đĩa (ví dụ đĩa chứa $D_2$) bị hỏng vật lý hoàn toàn:
- Hệ thống khôi phục lại dữ liệu $D_2$ bằng cách thực hiện phép XOR giữa các đĩa còn lại:
  $$D_2 = D_1 \oplus D_3 \oplus P$$
- Nhờ đặc tính toán học của phép XOR ($A \oplus A = 0$), mảng đĩa có thể phục hồi dữ liệu thời gian thực mà không làm gián đoạn dịch vụ của người dùng!

---

### 복습 체크리스트
- [ ] Phân biệt 3 chiến lược nạp bộ nhớ: First Fit (nhanh nhất), Best Fit (vừa vặn nhất), Worst Fit (vào ô trống lớn nhất).
- [ ] Nhớ hiện tượng phân mảnh: Paging chỉ sinh Phân mảnh nội vi; Segmentation chỉ sinh Phân mảnh ngoại vi.
- [ ] Nhận diện Nghịch lý Belady: Xảy ra trong thuật toán FIFO (tăng khung trang nhưng lỗi thiếu trang lại tăng).
- [ ] Phân biệt tính cục bộ: Temporal Locality (thời gian - vòng lặp Loop) vs Spatial Locality (không gian - mảng Array).
- [ ] Khắc ghi định nghĩa Thrashing: Hiệu suất CPU tụt dốc do hệ thống bận hoán đổi trang liên tục (do nạp quá nhiều tiến trình).
- [ ] Phân biệt NAS (truy xuất cấp Tệp qua NFS/CIFS) vs SAN (truy xuất cấp Khối qua cáp quang Fibre Channel).
- [ ] Thuộc khả năng chịu lỗi RAID: RAID 0 (hỏng 1 đĩa là mất hết); RAID 1 & RAID 5 (chịu hỏng tối đa 1 đĩa); RAID 6 (chịu hỏng tối đa 2 đĩa đồng thời).
