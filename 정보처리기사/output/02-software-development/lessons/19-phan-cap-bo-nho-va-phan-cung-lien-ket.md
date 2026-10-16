# 기억장치 계층 구조 및 컴퓨터 구조 (Phân cấp bộ nhớ và Kiến trúc phần cứng liên kết)

## 학습 목표
- Nắm vững kim tự tháp phân cấp bộ nhớ (`기억장치 계층 구조 / Memory Hierarchy`): Register $\rightarrow$ Cache (SRAM) $\rightarrow$ Main RAM (DRAM) $\rightarrow$ Secondary (SSD/HDD) $\rightarrow$ Tape; quy luật đánh đổi giữa tốc độ, dung lượng và giá thành.
- Phân biệt toàn diện 6 tiêu chí giữa DRAM (tụ điện Capacitor, mạch làm tươi Refresh, dung lượng lớn dùng làm RAM chính) và SRAM (mạch lật Flip-Flop, không cần làm tươi, tốc độ cực nhanh dùng làm Cache).
- Nắm vững công thức tính dung lượng bộ nhớ ($2^n \times m$), đặc tính đọc phá hủy (DRO) của Lõi từ (Magnetic Core), và phân loại SASD vs DASD.
- Tính toán thời gian truy cập đĩa từ: $\text{Disk Access Time} = \text{Seek Time} + \text{Latency Time} + \text{Transmission Time}$, nhận diện Seek Time chiếm nhiều thời gian nhất.
- Hiểu rõ cơ chế tăng tốc bộ nhớ: Bộ nhớ liên kết (`연관 기억장치 / CAM` - tìm kiếm bằng nội dung, dùng trong Cache & TLB) và Kỹ thuật xen kẽ bộ nhớ (`메모리 인터리빙 / Memory Interleaving`).
- Nắm vững nguyên lý cục bộ của Cache (Thời gian Temporal vs Không gian Spatial), công thức tỷ lệ trúng Hit Ratio, 3 phương pháp ánh xạ Cache (Direct, Associative, Set-Associative), và 2 chính sách ghi (Write-Through vs Write-Back).
- Nắm vững khái niệm Bộ nhớ ảo (`가상 기억장치`), phân biệt Phân trang (`페이징` - phân mảnh nội vi) vs Phân đoạn (`세그멘테이션` - phân mảnh ngoại vi), lỗi trang (`페이지 부재 / Page Fault`) và hiện tượng trì trệ (`스레싱 / Thrashing`).
- Nắm vững phân loại kiến trúc song song theo Flynn: SISD, SIMD (GPU, Array Processor), MISD, MIMD (Multi-core, Cluster) và kỹ thuật Pipelining.

## 핵심 키워드
- 기억장치 계층 구조 (Kim tự tháp phân cấp bộ nhớ / Register, Cache, RAM, SSD/HDD, Tape)
- DRAM vs SRAM (커패시터 재충전 주기억장치 vs 플립플롭 캐시 메모리)
- 연관 기억장치 (CAM / Associative Memory / 주소가 아닌 내용으로 검색)
- 메모리 인터리빙 (Memory Interleaving / 병렬 접근 동시 판독 / DMA 지원)
- 캐시 국소성 (Locality of Reference / 시간 국소성 Temporal vs 공간 국소성 Spatial)
- 캐시 매핑 & 쓰기 정책 (Direct, Associative, Set-Associative / Write-Through vs Write-Back)
- 가상 기억장치 (Virtual Memory / 페이징 Paging - 내부 단편화 vs 세그멘테이션 - 외부 단편화)
- 플린의 분류법 (Flynn's Taxonomy / SISD, SIMD GPU, MISD, MIMD Multi-core)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [18-clean-code-refactoring-va-kiem-tra-tinh.md](18-clean-code-refactoring-va-kiem-tra-tinh.md), chúng ta đã khảo sát các nguyên lý mã sạch Clean Code, kỹ thuật Refactoring và phân tích tĩnh/động.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp kiến thức nền tảng vật lý phần cứng của hệ thống máy tính, giải quyết mâu thuẫn tốc độ - dung lượng qua phân cấp bộ nhớ, cơ chế Cache, bộ nhớ ảo và kiến trúc song song.
- **Dùng đi đâu (Forward Handoff):** Bài học này chính thức khép lại trọn vẹn 19 bài học của Môn 2 (소프트웨어 개발), bàn giao kiến thức nền tảng sang Môn 3 (Xây dựng CSDL - cấu trúc lưu trữ bảng, index và buffer pool) và Môn 4 (Ứng dụng ngôn ngữ lập trình - quản lý bộ nhớ tiến trình, luồng, paging của Hệ điều hành).

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng so sánh DRAM vs SRAM, công thức tính Access Time đĩa từ, bảng 3 kỹ thuật ánh xạ Cache, bảng Paging vs Segmentation, và phân loại kiến trúc theo Flynn.
- Đọc TẦNG B để hiểu sâu công thức tính dung lượng bus MAR/MBR, cấu trúc lõi từ DRO, cơ chế CAM và Memory Interleaving, cùng hiện tượng Thrashing.

---

## 기억장치 계층 구조 및 컴퓨터 구조

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Kim tự tháp phân cấp bộ nhớ (Memory Hierarchy)
- **Quy luật đánh đổi kỹ thuật:**
  - Càng tiến gần CPU (đỉnh tháp): Tốc độ truy cập càng cao, chi phí trên mỗi bit càng đắt đỏ, dung lượng càng nhỏ.
  - Càng xa CPU (đáy tháp): Dung lượng càng lớn, chi phí trên mỗi bit càng rẻ, tốc độ truy xuất càng chậm.

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

#### 2. Bảng so sánh 6 tiêu chí kinh điển: DRAM vs SRAM
| Tiêu chí so sánh | 동적 램 - DRAM (Dynamic RAM) | 정적 램 - SRAM (Static RAM) |
| :--- | :--- | :--- |
| **Cấu tạo phần tử nhớ** | Tụ điện (**커패시터 - Capacitor**) và 1 transistor | Mạch lật trạng thái (**플립플롭 - Flip-Flop**) |
| **Mạch làm tươi** | **Bắt buộc phải có mạch làm tươi định kỳ (재충전 회로 필요 - Refresh)** | **Không cần làm tươi** (giữ nguyên dữ liệu chừng nào còn cấp điện) |
| **Tốc độ truy cập** | Tương đối chậm | **Cực kỳ nhanh** (xấp xỉ tốc độ bus CPU) |
| **Mật độ tích hợp** | **Rất cao** (kích thước ô nhớ siêu nhỏ) | Thấp (mỗi bit cần 4-6 transistor) |
| **Giá thành sản xuất** | Rẻ trên mỗi đơn vị dung lượng | Rất đắt đỏ |
| **Phạm vi ứng dụng** | Làm **Bộ nhớ chính (주기억장치 - Main RAM)** | Làm **Bộ nhớ đệm (캐시 메모리 - Cache Memory)** |

#### 3. Phương tiện lưu trữ phụ và Thời gian truy cập đĩa từ (Disk Access Time)
- **Phân loại truy cập:**
  - **Băng từ (자기 테이프):** **SASD (Sequential Access Storage Device)** - truy cập tuần tự từ đầu đến cuối cuộn băng.
  - **Đĩa từ (자기 디스크 / HDD):** **DASD (Direct Access Storage Device)** - đầu đọc nhảy trực tiếp đến vị trí vật lý bất kỳ.
- **Công thức tính thời gian truy cập đĩa:**
  $$\mathbf{\text{Disk Access Time} = \text{Seek Time (탐색 시간)} + \text{Latency Time (회전 지연 시간)} + \text{Transmission Time (전송 시간)}}$$
  - **Seek Time (탐색 시간):** Đầu đọc cơ học di chuyển vào đúng rãnh Track (**Mất nhiều thời gian nhất**).
  - **Latency Time (회전 지연 시간):** Đĩa quay đưa Sector cần đọc nằm dưới đầu từ (trung bình quay nửa vòng).
  - **Transmission Time (전송 시간):** Đọc các byte dữ liệu và truyền qua bus về RAM.

#### 4. Bảng 3 phương pháp ánh xạ địa chỉ Cache (Mapping Techniques)
| Phương pháp ánh xạ | Tên tiếng Hàn | Nguyên lý hoạt động | Đánh giá kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Ánh xạ trực tiếp** | **직접 매핑 (Direct Mapping)** | Mỗi khối RAM chỉ được map vào đúng một dòng Cache duy nhất theo công thức modulo | Mạch đơn giản, rẻ; nhưng tỷ lệ xung đột (**Conflict Miss**) rất cao |
| **Ánh xạ kết hợp hoàn toàn** | **연관 매핑 (Associative Mapping)** | Khối RAM có thể được nạp vào bất kỳ dòng trống nào còn lại trong Cache | Tỷ lệ trúng cao nhất; nhưng mạch so sánh CAM cực kỳ đắt đỏ |
| **Ánh xạ kết hợp tập hợp** | **세트-연관 매핑 (Set-Associative)** | Cache chia thành các Set, khối RAM map vào 1 Set cố định nhưng tự do chọn dòng trong Set | Cân bằng hoàn hảo; là **chuẩn thiết kế phổ biến nhất trong CPU hiện đại** |

- **Hai chính sách ghi (Write Policy):**
  - **Write-Through (동시 갱신):** Ghi đồng thời vào cả Cache và RAM. Nhất quán tuyệt đối nhưng tốc độ chậm.
  - **Write-Back (지연 기록):** Ghi trên Cache trước, đánh dấu **Dirty Bit**, chỉ ghi trả về RAM khi khối bị thay thế. Tốc độ rất nhanh.

#### 5. Phân trang (Paging) vs Phân đoạn (Segmentation) trong Bộ nhớ ảo
| Tiêu chí | 페이징 (Paging - Phân trang) | 세그멘테이션 (Segmentation - Phân đoạn) |
| :--- | :--- | :--- |
| **Kích thước khối** | **Cố định (고정 크기 분할)** | **Biến đổi (가변 크기 논리 분할)** |
| **Đơn vị phân chia** | Đơn vị vật lý: Page (trên đĩa) và Frame (trên RAM) | Đơn vị logic: Hàm main, Module, Mảng |
| **Vấn đề phân mảnh** | Xuất hiện **Phân mảnh nội vi (Internal Fragmentation)**; không có ngoại vi | Xuất hiện **Phân mảnh ngoại vi (External Fragmentation)**; không có nội vi |

- **페이지 부재 (Page Fault - Lỗi trang):** Xảy ra khi lệnh hoặc dữ liệu cần truy cập chưa được nạp sẵn vào Frame trên RAM, kích hoạt ngắt trap để OS đọc từ đĩa vào RAM.
- **스레싱 (Thrashing - Hiện tượng trì trệ):** Tình trạng hệ thống dành phần lớn thời gian CPU chỉ để hoán đổi trang (Page Swapping) thay vì thực thi lệnh hữu ích, khiến hiệu suất sụt giảm về 0.

#### 6. Phân loại máy tính theo Flynn (플린의 분류법)
| Thể loại | Luồng lệnh & Dữ liệu | Phần cứng đại diện | Đặc điểm vận hành |
| :--- | :--- | :--- | :--- |
| **SISD** | 1 Lệnh $\times$ 1 Dữ liệu | Máy tính Von Neumann truyền thống đơn nhân | Thực thi tuần tự từng câu lệnh trên một phần tử dữ liệu |
| **SIMD** | 1 Lệnh $\times$ Nhiều Dữ liệu | **배열 프로세서 (Array Processor)**, Bộ xử lý đồ họa **GPU** | Một lệnh duy nhất áp dụng đồng loạt lên toàn bộ mảng dữ liệu song song |
| **MISD** | Nhiều Lệnh $\times$ 1 Dữ liệu | Lý thuyết thuần túy; rất hiếm trong thực tế | Nhiều bộ xử lý cùng tính toán trên một luồng dữ liệu duy nhất |
| **MIMD** | Nhiều Lệnh $\times$ Nhiều Dữ liệu | **다중 처리기 (Multiprocessor)**, Đa lõi (Multi-core), Cụm máy chủ (Cluster) | Nhiều bộ xử lý thực thi độc lập các luồng lệnh khác nhau trên các dữ liệu khác nhau |

#### 7. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Từ khóa DRAM vs SRAM:**
  - Nhắc đến **재충전 (Làm tươi / Refresh)** hoặc **커패시터 (Tụ điện tích điện)** $\rightarrow$ Chọn ngay **동적 램 (DRAM)**.
  - Nhắc đến **플립플롭 (Flip-Flop)** hoặc **캐시 메모리 (Cache)** $\rightarrow$ Chọn ngay **정적 램 (SRAM)**.
- **Bẫy 2: Thời gian truy cập đĩa từ:** Thành phần chiếm nhiều thời gian nhất là **탐색 시간 (Seek Time)** vì đầu đọc cơ học phải di chuyển vật lý đến đúng rãnh Track.
- **Bẫy 3: Bộ nhớ liên kết CAM:** Bộ nhớ tìm kiếm dữ liệu dựa trên **nội dung ghi nhớ (기억된 내용)** thay vì địa chỉ ô nhớ $\rightarrow$ **연관 기억장치 (Associative Memory / CAM)**.
- **Bẫy 4: Nhận diện kiến trúc Flynn:** Bộ xử lý GPU hoặc Array Processor thực thi 1 lệnh trên nhiều dữ liệu $\rightarrow$ **SIMD**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Tính toán dung lượng bộ nhớ bán dẫn
$$\text{Tổng dung lượng (Capacity)} = (\text{Số lượng từ nhớ - Words}) \times (\text{Độ dài từ nhớ - Word Length})$$
- Hệ thống có $n$ đường Address Bus $\rightarrow 2^n$ địa chỉ (tương ứng kích thước thanh ghi địa chỉ MAR).
- Hệ thống có $m$ đường Data Bus $\rightarrow$ Mỗi Word có độ dài $m$ bits (tương ứng kích thước thanh ghi đệm MBR).
- *Ví dụ đề thi:* Bộ nhớ có 10 đường Address Bus và 8 đường Data Bus $\rightarrow$ Dung lượng $= 2^{10} \times 8\text{ bits} = 1024 \times 1\text{ Byte} = 1\text{ KB}$.

#### 2. Lõi từ (자기 코어 - Magnetic Core) và Đặc tính DRO
- Là công nghệ bộ nhớ từ tính sơ khai.
- **Đặc tính DRO (Destructive Read Out - Đọc phá hủy):** Đọc dữ liệu làm phá hủy trạng thái từ tính của lõi, hệ thống bắt buộc phải có chu kỳ phục hồi (**재생산 주기 - Restoration Time**) để ghi lại nội dung vừa đọc.
- Gồm 4 dây dẫn: 2 dây toạ độ (X, Y), 1 dây cảm ứng đọc tín hiệu (센스선 - Sense Line) và 1 dây cấm đảo từ (금지선 - Inhibit Line).

#### 3. Bộ nhớ liên kết CAM và Xen kẽ bộ nhớ Interleaving
- **CAM (Content Addressable Memory):** Tích hợp mạch so sánh song song (**일치 회로**), so sánh toàn bộ mảng dữ liệu trong 1 chu kỳ máy. Ứng dụng trong Cache tag directory và bảng chuyển đổi trang nhanh TLB.
- **메모리 인터리빙 (Memory Interleaving):** Chia RAM thành nhiều module độc lập, đánh địa chỉ luân phiên để CPU có thể truy cập song song đồng thời nhiều module trong 1 chu kỳ bus, hỗ trợ đắc lực cho DMA và kiến trúc Pipeline.

---

### 복습 체크리스트
- [ ] Vẽ đúng thứ tự Kim tự tháp phân cấp bộ nhớ: Register $\rightarrow$ Cache $\rightarrow$ RAM $\rightarrow$ SSD/HDD $\rightarrow$ Tape.
- [ ] So sánh đúng 6 tiêu chí giữa DRAM (tụ điện, cần làm tươi, RAM chính) và SRAM (flip-flop, không làm tươi, Cache).
- [ ] Tính thành thạo dung lượng bộ nhớ từ số đường Address Bus ($n$) và Data Bus ($m$): $2^n \times m$ bits.
- [ ] Nhớ công thức thời gian truy cập đĩa và Seek Time (탐색 시간) là thành phần tốn thời gian nhất.
- [ ] Định nghĩa bộ nhớ liên kết CAM là tìm kiếm bằng nội dung (기억된 내용) thay vì địa chỉ.
- [ ] Phân biệt 3 kỹ thuật ánh xạ Cache: Direct Mapping, Associative Mapping, Set-Associative Mapping.
- [ ] Phân biệt Write-Through (ghi đồng thời cả 2 nơi) và Write-Back (ghi vào Cache, dùng dirty bit).
- [ ] Phân biệt Paging (kích thước cố định, phân mảnh nội vi) và Segmentation (kích thước biến đổi, phân mảnh ngoại vi).
- [ ] Định nghĩa hiện tượng Page Fault và Thrashing (chỉ lo tráo trang khiến CPU đứng im).
- [ ] Phân loại chuẩn 4 nhóm máy tính theo Flynn: SISD, SIMD (GPU), MISD, MIMD (đa lõi, cụm máy chủ).
