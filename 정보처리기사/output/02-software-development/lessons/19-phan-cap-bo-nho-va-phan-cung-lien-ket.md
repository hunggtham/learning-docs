# 19. Phân cấp bộ nhớ và Kiến trúc phần cứng liên kết (기억장치 계층 구조 및 컴퓨터 구조)

## 1. Ranh giới môn học và Tổng quan Phân cấp bộ nhớ (기억장치 계층 구조)

> [!NOTE]
> **Ranh giới liên môn (Cross-Subject Boundary):**
> Bài học này là phụ lục liên môn chuyên sâu trong Môn 2 (소프트웨어 개발). Các khái niệm tổ chức phần cứng, phân cấp bộ nhớ, Cache, bộ nhớ ảo và kiến trúc song song là kiến thức nền tảng vật lý quyết định hiệu năng thực thi của các thuật toán và module phần mềm. Nội dung này liên kết trực tiếp với **Môn 4 (프로그래밍 언어 활용 - Quản lý bộ nhớ và tiến trình của Hệ điều hành)** và **Môn 5 (정보시스템 구축관리 - Kiến trúc hạ tầng máy tính)**.

### 1.1. Kim tự tháp phân cấp bộ nhớ (Memory Hierarchy)

Để giải quyết mâu thuẫn muôn thuở giữa **Tốc độ truy cập (Speed)**, **Dung lượng lưu trữ (Capacity)** và **Giá thành phần cứng (Cost)**, các hệ thống máy tính hiện đại áp dụng cấu trúc phân cấp bộ nhớ nhiều tầng:

```
                  ┌──────────────────────┐
                  │    레지스터 (Register)│  ▲ Tốc độ nhanh nhất
                  ├──────────────────────┤  │ Dung lượng nhỏ nhất
                  │   캐시 (L1/L2/L3)    │  │ Giá thành/bit đắt nhất
                  ├──────────────────────┤  │
                  │   주기억장치 (RAM)    │  │
                  ├──────────────────────┤  │
                  │  보조기억장치 (SSD/HDD)│  │ Dung lượng lớn nhất
                  ├──────────────────────┤  │ Tốc độ chậm nhất
                  │   자기 테이프 (Tape)  │  ▼ Giá thành/bit rẻ nhất
                  └──────────────────────┘
```

- **Quy luật đánh đổi kỹ thuật:**
  - Càng tiến gần CPU (phía trên đỉnh tháp): Tốc độ truy cập càng cao, chi phí trên mỗi bit càng đắt đỏ, nhưng dung lượng lưu trữ càng bị hạn chế.
  - Càng xa CPU (phía đáy tháp): Dung lượng lưu trữ càng khổng lồ, chi phí trên mỗi bit càng rẻ, nhưng tốc độ truy xuất càng suy giảm nghiêm trọng.

---

## 2. Bộ nhớ chính bán dẫn: DRAM vs SRAM và Lõi từ

### 2.1. Bảng so sánh kinh điển 6 tiêu chí giữa DRAM và SRAM

Bộ nhớ truy cập ngẫu nhiên bán dẫn (**RAM - Random Access Memory**) được chia thành 2 nhánh công nghệ phục vụ hai mục đích hoàn toàn khác nhau:

| Tiêu chí so sánh | 동적 램 - DRAM (Dynamic RAM) | 정적 램 - SRAM (Static RAM) |
| :--- | :--- | :--- |
| **Cấu tạo phần tử nhớ** | Tụ điện (**커패시터 - Capacitor**) và 1 transistor | Mạch lật trạng thái (**플립플롭 - Flip-Flop**) |
| **Mạch làm tươi** | **Bắt buộc phải có mạch làm tươi định kỳ (재충전 회로 필요 - Refresh)** | **Không cần làm tươi** (giữ nguyên dữ liệu chừng nào còn cấp điện) |
| **Tốc độ truy cập** | Tương đối chậm | **Cực kỳ nhanh** (xấp xỉ tốc độ bus CPU) |
| **Mật độ tích hợp** | **Rất cao** (kích thước ô nhớ siêu nhỏ) | Thấp (mỗi bit cần 4-6 transistor) |
| **Giá thành sản xuất** | Rẻ trên mỗi đơn vị dung lượng | Rất đắt đỏ |
| **Phạm vi ứng dụng** | Làm **Bộ nhớ chính (주기억장치 - Main RAM)** | Làm **Bộ nhớ đệm (캐시 메모리 - Cache Memory)** |

> [!IMPORTANT]
> **Từ khóa sống còn trong đề thi:**
> Khi câu hỏi nhắc đến **재충전 (Làm tươi / Refresh)** hoặc **커패시터 (Tụ điện tích điện)** $\rightarrow$ Chọn ngay **DRAM**.
> Khi câu hỏi nhắc đến **플립플롭 (Flip-Flop)** hoặc **캐시 메모리 (Cache Memory)** $\rightarrow$ Chọn ngay **SRAM**.

### 2.2. Tính toán dung lượng bộ nhớ bán dẫn (기억용량 계산)
Dung lượng của một chip bộ nhớ được xác định bởi số lượng đường dây của Bus địa chỉ (**주소 버스 - Address Bus**) và Bus dữ liệu (**데이터 버스 - Data Bus**):

$$\text{Tổng dung lượng (Capacity)} = (\text{Số lượng từ nhớ - Words}) \times (\text{Độ dài từ nhớ - Word Length})$$

- Nếu hệ thống có $n$ đường Address Bus $\rightarrow$ Tạo ra $2^n$ địa chỉ (tương ứng $2^n$ Words, quyết định kích thước thanh ghi địa chỉ **MAR**).
- Nếu hệ thống có $m$ đường Data Bus $\rightarrow$ Mỗi Word có độ dài $m$ bits (quyết định kích thước thanh ghi đệm dữ liệu **MBR**).
- *Ví dụ tính toán chuẩn thi:* Bộ nhớ có 10 đường Address Bus và 8 đường Data Bus $\rightarrow$ Dung lượng $= 2^{10} \times 8\text{ bits} = 1024 \times 1\text{ Byte} = 1\text{ KB}$.

### 2.3. Lõi từ (자기 코어 - Magnetic Core)
- Là công nghệ bộ nhớ từ tính sơ khai trong lịch sử máy tính.
- **Đặc tính DRO (Destructive Read Out - Đọc phá hủy):** Khi thực hiện thao tác đọc dữ liệu từ lõi từ, trạng thái từ tính của lõi bị phá hủy. Do đó, hệ thống bắt buộc phải có chu kỳ phục hồi dữ liệu (**재생산 주기 - Restoration Time**) để ghi lại nội dung vừa đọc.
- **Cấu trúc 4 dây truyền dẫn:** Gồm 2 dây điều khiển dòng điện toạ độ (X 구동선, Y 구동선), 1 dây cảm ứng đọc tín hiệu (센스선 - Sense Line) và 1 dây cấm đảo từ (금지선 - Inhibit Line).

---

## 3. Bộ nhớ phụ và Thời gian truy cập đĩa từ (보조기억장치)

### 3.1. Phân loại SASD vs DASD

| Loại phương tiện | Phân loại truy cập | Cơ chế hoạt động | Thiết bị đại diện |
| :--- | :--- | :--- | :--- |
| **Băng từ (자기 테이프)** | **SASD (Sequential Access)** | Đọc/ghi tuần tự từ đầu cuộn băng đến cuối cuộn băng; muốn tìm dữ liệu ở giữa phải tua qua toàn bộ đoạn trước | Băng từ sao lưu dự phòng (Backup Tape) |
| **Đĩa từ (자기 디스크)** | **DASD (Direct Access)** | Đầu đọc có thể nhảy trực tiếp đến vị trí vật lý bất kỳ trên mặt đĩa mà không cần duyệt tuần tự | Ổ cứng cơ học (HDD), Đĩa mềm (Floppy) |

### 3.2. Cấu trúc đĩa từ và Công thức tính thời gian truy cập (Disk Access Time)

Một đĩa cứng bao gồm nhiều phiến đĩa xếp chồng quay quanh trục:
- **Track (트랙 - Rãnh):** Các vòng tròn đồng tâm chứa dữ liệu trên bề mặt phiến đĩa.
- **Sector (섹터 - Cung):** Đoạn chia nhỏ nhất trên mỗi Track (thường có dung lượng 512 Bytes hoặc 4 KB).
- **Cylinder (실린더 - Hình trụ):** Tập hợp tất cả các Track có cùng bán kính nằm trên nhiều bề mặt phiến đĩa xếp chồng.

```
                  ┌────────────────────────────────────────────────────────┐
                  │                 TỔNG THỜI GIAN TRUY CẬP ĐĨA             │
                  │                     (Disk Access Time)                 │
                  └───────────────────────────┬────────────────────────────┘
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         ▼                                    ▼                                    ▼
┌─────────────────────────┐          ┌─────────────────────────┐          ┌─────────────────────────┐
│ 탐색 시간 (Seek Time)    │          │ 회전 지연 시간 (Latency) │          │ 전송 시간 (Transmission)│
│ Đầu đọc di chuyển vào   │    +     │ Đĩa quay đưa Sector cần │    +     │ Đọc các byte dữ liệu và │
│ đúng rãnh Track         │          │ đọc nằm dưới đầu từ     │          │ truyền qua bus về RAM   │
│ (Mất nhiều thời gian    │          │ (Thời gian trung bình   │          │                         │
│  nhất trong 3 thành phần│          │  bằng quay nửa vòng đĩa)│          │                         │
└─────────────────────────┘          └─────────────────────────┘          └─────────────────────────┘
```

$$\text{Disk Access Time} = \text{Seek Time (탐색 시간)} + \text{Latency Time (회전 지연 시간)} + \text{Transmission Time (전송 시간)}$$

---

## 4. Tăng tốc truy cập bộ nhớ: CAM và Memory Interleaving

### 4.1. Bộ nhớ liên kết (연관 기억장치 - Associative Memory / CAM)

- **Nguyên lý hoạt động:** Trong bộ nhớ thông thường, CPU muốn đọc dữ liệu phải cung cấp **Địa chỉ ô nhớ (Address)**. Ngược lại, trong **CAM (Content Addressable Memory)**, CPU tìm kiếm và truy xuất dữ liệu trực tiếp bằng **Nội dung ghi nhớ (기억된 내용)**.
- **Cấu tạo phần cứng:** Mỗi ô nhớ trong CAM được tích hợp một mạch so sánh song song (**일치 회로 - Match Circuit**). Khi truyền một từ khóa tìm kiếm (Search Key) vào, tất cả các từ nhớ trong mảng sẽ so sánh đồng thời trong đúng 1 chu kỳ máy.
- **Ưu nhược điểm:** Tốc độ tìm kiếm tức thì cực nhanh nhưng giá thành sản xuất cực kỳ đắt đỏ.
- **Ứng dụng thực tế:** Được sử dụng trong các bảng ánh xạ địa chỉ của **Cache Memory** và bảng chuyển đổi trang nhanh (**TLB - Translation Lookaside Buffer**) của bộ nhớ ảo.

### 4.2. Kỹ thuật xen kẽ bộ nhớ (메모리 인터리빙 - Memory Interleaving)

- **Vấn đề đặt ra:** Tốc độ xử lý của CPU nhanh hơn nhiều lần so với tốc độ nạp dữ liệu từ một thanh RAM đơn lẻ.
- **Giải pháp:** Chia bộ nhớ thành nhiều mô-đun nhớ độc lập (Banks/Modules). Các địa chỉ ô nhớ liên tiếp nhau $0, 1, 2, 3...$ được phân bổ luân phiên vòng tròn sang các Module $0, 1, 2, 3...$
- **Cơ chế truy cập song song (Concurrent Access):** CPU có thể phát lệnh đọc đồng thời nhiều từ nhớ từ các module khác nhau trong cùng một chu kỳ bus mà không cần chờ module trước hoàn thành chu kỳ đọc, từ đó gia tăng gấp bội băng thông bộ nhớ và hỗ trợ truyền dữ liệu trực tiếp tốc độ cao (**DMA**).

---

## 5. Bộ nhớ đệm (캐시 메모리 - Cache Memory)

### 5.1. Khái niệm và Nguyên lý cục bộ (Locality of Reference)
Cache Memory là bộ nhớ đệm tốc độ cực cao làm bằng SRAM nằm kẹp giữa CPU và Main RAM, dựa trên **Nguyên lý cục bộ (국소성 / 지역성 - Locality)**:
- **Cục bộ thời gian (시간 국소성 - Temporal Locality):** Một ô nhớ vừa được truy cập sẽ có xác suất rất cao được truy cập lại trong tương lai gần (ví dụ: biến đếm vòng lặp, hàm con).
- **Cục bộ không gian (공간 국소성 - Spatial Locality):** Khi một ô nhớ được truy cập, các ô nhớ nằm liền kề nó cũng sẽ sớm được truy cập (ví dụ: mảng duyệt tuần tự, khối lệnh liên tiếp).

### 5.2. Công thức tính Tỷ lệ trúng (Hit Ratio) và Thời gian truy cập hiệu dụng
- **Tỷ lệ trúng (적중률 - Hit Ratio $H$):** Tỷ lệ phần trăm số lần CPU tìm thấy dữ liệu mong muốn ngay trong Cache.
  $$H = \frac{N_{\text{hits}}}{N_{\text{hits}} + N_{\text{misses}}}$$
- **Tỷ lệ trượt (미스율 - Miss Ratio):** $1 - H$.
- **Thời gian truy cập trung bình (Effective Access Time):**
  $$T_{\text{avg}} = H \cdot T_{\text{cache}} + (1 - H) \cdot T_{\text{main}}$$

### 5.3. Ba phương pháp ánh xạ địa chỉ Cache (Mapping Techniques)

| Phương pháp ánh xạ | Tên tiếng Hàn | Nguyên lý hoạt động | Đánh giá kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Ánh xạ trực tiếp** | **직접 매핑 (Direct Mapping)** | Mỗi khối ô nhớ trong RAM chỉ được phép nạp vào đúng một dòng Cache duy nhất theo công thức modulo cố định | Mạch phần cứng cực kỳ đơn giản, rẻ tiền; nhưng **tỷ lệ xung đột (Conflict Miss) rất cao** |
| **Ánh xạ kết hợp hoàn toàn** | **연관 매핑 (Associative Mapping)** | Khối RAM có thể được nạp vào bất kỳ dòng trống nào còn lại trong toàn bộ bộ nhớ Cache | Tỷ lệ trúng cao nhất, linh hoạt tuyệt đối; nhưng **mạch so sánh CAM cực kỳ phức tạp và đắt tiền** |
| **Ánh xạ kết hợp tập hợp** | **세트-연관 매핑 (Set-Associative Mapping)** | Dung hòa hai cách trên: Cache được chia thành các Tập hợp (Set), mỗi khối RAM map vào 1 Set cố định nhưng có thể chọn dòng tự do bên trong Set đó | Cân bằng hoàn hảo giữa chi phí phần cứng và tỷ lệ trúng; là **chuẩn thiết kế phổ biến nhất trong CPU hiện đại** |

### 5.4. Hai chính sách ghi dữ liệu (Write Policy)
- **Write-Through (동시 갱신 / 즉시 기록):** Khi CPU thực hiện lệnh ghi, dữ liệu được ghi đồng thời vào cả Cache Memory lẫn Main RAM. Đảm bảo tính nhất quán dữ liệu tuyệt đối nhưng tốc độ ghi bị chậm do phải chờ RAM.
- **Write-Back (블록 교체 시 갱신 / 지연 기록):** Khi CPU ghi, dữ liệu chỉ được cập nhật tức thì trên Cache và đánh dấu bit bẩn (**Dirty Bit**). Dữ liệu chỉ được ghi trả về Main RAM khi khối Cache đó bị giải phóng để nạp khối mới. Tốc độ ghi cực nhanh nhưng mạch điều khiển phức tạp.

---

## 6. Bộ nhớ ảo (가상 기억장치 - Virtual Memory)

### 6.1. Khái niệm và Cơ chế chuyển đổi địa chỉ (Address Mapping)
- **Định nghĩa:** Là kỹ thuật quản lý bộ nhớ của Hệ điều hành kết hợp với phần cứng **MMU (Memory Management Unit)** cho phép hệ thống thực thi các chương trình có kích thước lớn hơn dung lượng thanh RAM vật lý thực tế bằng cách tận dụng một phần ổ cứng phụ (DASD) làm không gian nhớ ảo.
- **Địa chỉ ảo (Virtual Address):** Không gian địa chỉ do trình biên dịch gán cho tiến trình, nằm trên đĩa.
- **Địa chỉ thực (Physical Address):** Vị trí thực tế của ô nhớ trên thanh RAM.
- Quá trình chuyển đổi từ Địa chỉ ảo sang Địa chỉ thực được thực hiện thông qua bảng ánh xạ trang (**Page Table**) hoặc bảng chuyển đổi nhanh (**TLB**).

### 6.2. Phân trang (Paging) vs Phân đoạn (Segmentation)

| Tiêu chí | 페이징 (Paging - Phân trang) | 세그멘테이션 (Segmentation - Phân đoạn) |
| :--- | :--- | :--- |
| **Kích thước khối** | **Cố định (고정 크기 분할)** | **Biến đổi (가변 크기 논리 분할)** |
| **Đơn vị phân chia** | Đơn vị vật lý: Page (trên đĩa) và Frame (trên RAM) | Đơn vị logic theo cấu trúc chương trình: Main, Subroutine, Array |
| **Vấn đề phân mảnh** | Xuất hiện **Phân mảnh nội vi (Internal Fragmentation)**; không có phân mảnh ngoại vi | Xuất hiện **Phân mảnh ngoại vi (External Fragmentation)**; không có phân mảnh nội vi |

### 6.3. Hiện tượng Lỗi trang (Page Fault) và Hiện tượng Trì trệ (Thrashing)
- **페이지 부재 (Page Fault - Lỗi trang):** Xảy ra khi CPU cần truy xuất một lệnh hoặc dữ liệu thuộc Page $k$, nhưng Page này chưa được nạp sẵn vào Frame trên RAM. Phần cứng MMU kích hoạt ngắt **Page Fault Trap**, CPU tạm dừng tiến trình hiện tại để Hệ điều hành thực hiện thao tác I/O đọc khối dữ liệu từ ổ cứng nạp vào RAM.
- **스레싱 (Thrashing - Hiện tượng trì trệ):** Tình trạng hệ thống dành phần lớn thời gian CPU chỉ để hoán đổi trang ra vào giữa đĩa và RAM (**Page Swapping**) thay vì thực hiện các lệnh hữu ích của tiến trình, khiến hiệu suất toàn hệ thống giảm sút nghiêm trọng về 0.

---

## 7. Phân loại máy tính song song theo Flynn (플린의 분류법)

Năm 1966, Michael J. Flynn đề xuất thang phân loại kiến trúc máy tính kinh điển dựa trên số lượng luồng lệnh (**Instruction Stream**) và luồng dữ liệu (**Data Stream**):

| Thể loại Flynn | Luồng lệnh & Luồng dữ liệu | Kiến trúc phần cứng đại diện | Đặc điểm vận hành |
| :--- | :--- | :--- | :--- |
| **SISD** | 1 Luồng lệnh $\times$ 1 Luồng dữ liệu | Máy tính Von Neumann truyền thống đơn nhân (Single-core PC) | Thực thi tuần tự từng câu lệnh trên một phần tử dữ liệu duy nhất |
| **SIMD** | 1 Luồng lệnh $\times$ Nhiều Luồng dữ liệu | **배열 프로세서 (Array Processor)**, Bộ xử lý đồ họa **GPU** | Một câu lệnh duy nhất được phát ra và áp dụng đồng loạt lên toàn bộ mảng dữ liệu song song |
| **MISD** | Nhiều Luồng lệnh $\times$ 1 Luồng dữ liệu | Về mặt lý thuyết thuần túy; rất hiếm trong thực tế | Nhiều bộ xử lý cùng thực hiện các phép toán khác nhau trên một luồng dữ liệu duy nhất |
| **MIMD** | Nhiều Luồng lệnh $\times$ Nhiều Luồng dữ liệu | **다중 처리기 (Multiprocessor)**, Máy tính đa lõi (Multi-core), Cụm máy chủ phân tán (Cluster) | Nhiều bộ xử lý thực thi độc lập các luồng lệnh khác nhau trên các luồng dữ liệu khác nhau |

### 7.1. Kỹ thuật xử lý đường ống (파이프라인 - Pipelining)
- Kỹ thuật chia chu kỳ thực thi của một lệnh thành nhiều giai đoạn con độc lập (Lấy lệnh - IF, Giải mã lệnh - ID, Lấy toán hạng - OF, Thực thi lệnh - EX).
- Các giai đoạn của nhiều lệnh liên tiếp được xếp chồng gối đầu lên nhau trong từng chu kỳ xung nhịp (Clock Cycle), giúp hoàn thành trung bình 1 lệnh trên mỗi chu kỳ máy mà không cần tăng tần số phần cứng.

---

## 8. Câu hỏi ôn tập và bẫy đề thi thực tế

1. **Phân biệt cơ chế DRAM và SRAM:**
   - *Câu hỏi:* Loại bộ nhớ RAM nào sử dụng mạch lật trạng thái Flip-Flop, không cần mạch làm tươi định kỳ và thường được dùng làm bộ nhớ đệm Cache Memory?
   - *Đáp án chuẩn thi:* **정적 램 (SRAM - Static RAM)**.
2. **Thời gian truy cập đĩa từ:**
   - *Bẫy đề thi:* "Trong 3 thành phần của thời gian truy cập đĩa cứng (Access Time), thời gian truyền dữ liệu (Transmission Time) là thành phần chiếm tỷ trọng thời gian lớn nhất." $\rightarrow$ **SAI**. Thành phần chiếm nhiều thời gian nhất là **탐색 시간 (Seek Time)** vì đầu đọc cơ học phải di chuyển vật lý đến đúng rãnh Track.
3. **Đặc trưng của bộ nhớ liên kết CAM:**
   - *Câu hỏi:* Bộ nhớ nào tìm kiếm dữ liệu dựa trên **nội dung ghi nhớ (기억된 내용)** thay vì dựa trên địa chỉ vật lý ô nhớ?
   - *Đáp án chuẩn thi:* **연관 기억장치 (Associative Memory / CAM)**.
4. **Phân loại kiến trúc Flynn:**
   - *Câu hỏi:* Kiến trúc máy tính nào thực thi đồng thời một câu lệnh duy nhất trên nhiều phần tử dữ liệu song song (thường thấy trong các bộ xử lý đồ họa GPU hoặc Array Processor)?
   - *Đáp án chuẩn thi:* **SIMD (Single Instruction, Multi Data)**.

---

## 9. Tổng kết Môn 2 và Ranh giới chuyển tiếp sang Môn 3 & Môn 4

Bài học 19 chính thức khép lại toàn bộ chương trình học tập của **Môn 2: Phát triển phần mềm (소프트웨어 개발)** thuộc kỳ thi Kỹ sư xử lý thông tin.

Quá trình phát triển phần mềm đã trang bị cho bạn hệ thống kiến thức toàn diện từ:
- Cấu trúc dữ liệu và giải thuật tối ưu (Chương 1).
- Thiết kế module, chuẩn kết nối liên hệ thống và an ninh giao diện (Chương 2).
- Quy trình đóng gói bản quyền DRM, kiểm soát phiên bản SCM và tự động hóa CI/CD (Chương 3).
- Các phương pháp và mô hình kiểm thử hộp trắng/hộp đen công nghiệp (Chương 4).
- Tiêu chuẩn mã sạch Clean Code, tái cấu trúc Refactoring và nền tảng tổ chức bộ nhớ máy tính (Chương 5 & Phụ lục).

Từ đây, bạn có thể tiếp tục hành trình sang:
- **Môn 3 (데이터베이스 구축 - Xây dựng cơ sở dữ liệu):** Đi sâu vào mô hình dữ liệu quan hệ, chuẩn hóa RDBMS, tối ưu hóa câu lệnh SQL nâng cao và quản trị giao dịch ACID.
- **Môn 4 (프로그래밍 언어 활용 - Sử dụng ngôn ngữ lập trình):** Đi sâu vào cú pháp ngôn ngữ C, Java, Python và cơ chế quản lý tiến trình, luồng, phân trang bộ nhớ ảo chuyên sâu của Hệ điều hành.
