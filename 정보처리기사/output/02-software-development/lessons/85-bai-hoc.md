# 핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)

## 학습 목표 (Mục tiêu)
- Nắm vững phân loại và đặc tính của bộ nhớ phụ (보조기억장치 - Auxiliary Memory): bộ nhớ bất biến (비휘발성), dung lượng lớn, giá thành rẻ nhưng tốc độ truy cập chậm hơn bộ nhớ chính.
- Phân biệt rõ hai cơ chế truy cập lưu trữ: Truy cập tuần tự SASD (Sequential Access Storage Device) của Băng từ và Truy cập trực tiếp ngẫu nhiên DASD (Direct Access Storage Device) của Đĩa từ.
- Nắm vững cấu trúc hình học của đĩa từ (Track, Sector, Cylinder) và công thức tính thời gian truy cập đĩa: $\text{Access Time} = \text{Seek Time} + \text{Latency Time} + \text{Transmission Time}$.

## 핵심 키워드 (Từ khóa)
- 보조기억장치 (Auxiliary / Secondary Memory)
- 자기 테이프 (Magnetic Tape / SASD / 백업용)
- 자기 디스크 (Magnetic Disk / DASD / 하드디스크)
- 트랙, 섹터, 실린더 (Track, Sector, Cylinder)
- 디스크 접근 시간 (Disk Access Time)
- 탐색 시간 (Seek Time / 헤드가 트랙으로 이동)
- 회전 지연 시간 (Latency Time / 섹터가 헤드로 회전)
- 전송 시간 (Transmission Time / 데이터 전송)

## 선행·연결 개념 (Kiến thức liên kết)
- [84-bai-hoc.md](84-bai-hoc.md): Linh kiện nhớ bán dẫn và tính toán dung lượng bộ nhớ.
- [86-bai-hoc.md](86-bai-hoc.md): Bộ nhớ liên kết (CAM) và kỹ thuật xen kẽ bộ nhớ (Memory Interleaving).
- [정보처리기사/output/04-programming-language/lessons/02-bai-hoc.md](../../04-programming-language/lessons/02-bai-hoc.md): Quản lý tệp tin và thiết bị ngoại vi của hệ điều hành.

## 읽는 방법 (Cách đọc)
- Ghi nhớ bộ 3 thành phần của công thức truy cập đĩa (SLT):
  $$\text{Access Time} = \text{Seek Time (탐색 시간)} + \text{Latency Time (회전 지연 시간)} + \text{Transmission Time (전송 시간)}$$
  1. **Seek Time (Tìm rãnh):** Đầu đọc cơ học di chuyển tịnh tiến vào đúng vòng rãnh Track (mất nhiều thời gian nhất).
  2. **Latency / Rotational Delay (Chờ xoay):** Đĩa từ quay tròn quanh trục để cung dữ liệu Sector cần đọc chạy tới nằm dưới đầu đọc (trung bình bằng thời gian quay nửa vòng đĩa).
  3. **Transmission Time (Truyền dữ liệu):** Đọc các byte dữ liệu trên Sector và đẩy qua cáp bus vào RAM.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh Băng từ (Tape) vs Đĩa từ (Disk):**

| Thiết bị | Chế độ truy cập | Cấu trúc vật lý | Ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **자기 테이프 (Magnetic Tape)** | **SASD (Sequential Access)**; chỉ có thể đọc tuần tự từ đầu tới cuối cuộn băng | Dải băng nhựa phủ oxit từ tính, chia thành các khối Block (IBG - Inter-Block Gap) | Lưu trữ sao lưu dự phòng dung lượng cực lớn (Backup/Archive), chi phí rẻ |
| **자기 디스크 (Magnetic Disk)** | **DASD (Direct Access)**; có thể nhảy cóc trực tiếp đến vị trí bất kỳ | Gồm nhiều đĩa (Platters), chia thành các đường tròn đồng tâm (**Track**), cung quạt (**Sector**), và tập hợp track cùng trục (**Cylinder**) | Thiết bị lưu trữ chính của hệ điều hành và cơ sở dữ liệu (HDD, SSD) |

- **Bảng chi tiết 3 thành phần thời gian truy cập đĩa từ:**

| Thành phần thời gian | Tên tiếng Hàn & Anh | Hành động vật lý của ổ cứng | Tỷ trọng thời gian |
| :--- | :--- | :--- | :--- |
| **1. 탐색 시간** | **Seek Time** | Cần gạt đưa đầu đọc/ghi (R/W Head) di chuyển đến đúng **트랙 (Track)** chỉ định | Chiếm thời gian **lớn nhất** trong toàn bộ chu kỳ |
| **2. 회전 지연 시간** | **Latency Time (Rotational Delay)** | Đĩa quay tròn để đưa đúng **섹터 (Sector)** cần đọc vào vị trí ngay dưới đầu đọc | Trung bình bằng $\frac{1}{2}$ chu kỳ quay của đĩa |
| **3. 전송 시간** | **Transmission Time** | Đầu đọc cảm biến từ trường chuyển đổi thành bit số và truyền dữ liệu vào bộ nhớ chính | Phụ thuộc vào tốc độ quay đĩa và dung lượng cần nạp |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Thuật toán lập lịch cần gạt đĩa (Disk Scheduling):**
  - Để giảm thiểu tối đa thành phần Seek Time (thành phần tốn thời gian nhất), hệ điều hành áp dụng các thuật toán điều phối đầu đọc:
    - **FCFS (First Come First Served):** Đến trước phục vụ trước (kém hiệu quả).
    - **SSTF (Shortest Seek Time First):** Chọn yêu cầu có khoảng cách track gần đầu đọc nhất (nguy cơ đói tài nguyên - Starvation cho các track ở xa).
    - **SCAN (Elevator):** Đầu đọc di chuyển liên tục từ đầu này sang đầu kia như thang máy, phục vụ các track trên đường đi.

### 복습 체크리스트
- [ ] Viết đúng công thức: Access Time = Seek Time + Latency Time + Transmission Time.
- [ ] Phân biệt được Seek Time (tìm Track) và Latency Time (chờ xoay đến Sector).
- [ ] Nhớ Tape là SASD (tuần tự), Disk là DASD (trực tiếp).
- [ ] Nắm được cấu trúc đĩa: Track (đường tròn), Sector (cung), Cylinder (tập hợp track cùng vị trí trên các mặt đĩa).
