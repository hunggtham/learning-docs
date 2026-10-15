# 핵심 117: 캐시 메모리 (Cache Memory)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò của bộ nhớ đệm Cache Memory như một bộ đệm tốc độ cao (고속 Buffer Memory) giải quyết sự chênh lệch tốc độ giữa CPU và bộ nhớ chính (RAM).
- Nắm chắc công thức tính tỷ lệ trúng bộ nhớ đệm (적중률 - Hit Ratio) và thời gian truy cập hiệu dụng (Effective Access Time).
- Phân biệt 3 phương pháp ánh xạ địa chỉ từ RAM vào Cache: Ánh xạ trực tiếp (Direct Mapping), Ánh xạ kết hợp hoàn toàn (Associative Mapping), và Ánh xạ kết hợp tập hợp (Set-Associative Mapping).
- So sánh hai chính sách ghi dữ liệu lên bộ nhớ đệm: Ghi xuyên suốt (Write-Through) và Ghi trả sau (Write-Back).

## 핵심 키워드 (Từ khóa)
- 캐시 메모리 (Cache Memory / 고속 완충 기억장치)
- 적중률 (Hit Ratio / $H = \frac{\text{Hits}}{\text{Total Accesses}}$)
- 미스율 (Miss Ratio / $1 - H$)
- 직접 매핑 (Direct Mapping)
- 연관 매핑 (Associative Mapping)
- 세트-연관 매핑 (Set-Associative Mapping)
- Write-Through (동시 갱신 / 즉시 기록)
- Write-Back (블록 교체 시 갱신 / 지연 기록)

## 선행·연결 개념 (Kiến thức liên kết)
- [86-bai-hoc.md](86-bai-hoc.md): Bộ nhớ liên kết (CAM) và xen kẽ bộ nhớ (Memory Interleaving).
- [88-bai-hoc.md](88-bai-hoc.md): Bộ nhớ ảo (Virtual Memory) và hiện tượng lỗi trang.
- [83-bai-hoc.md](83-bai-hoc.md): So sánh DRAM bộ nhớ chính và SRAM làm Cache.

## 읽는 방법 (Cách đọc)
- Phân biệt rõ hai cặp khái niệm trọng tâm:
  - **3 phương pháp ánh xạ (Mapping):**
    - **직접 매핑 (Direct):** Mỗi khối RAM chỉ được map vào đúng 1 dòng Cache cố định theo công thức modulo $\rightarrow$ Phần cứng cực kỳ đơn giản, giá rẻ nhưng tỷ lệ xung đột (Conflict Miss) rất cao.
    - **연관 매핑 (Associative):** Khối RAM có thể nhảy vào bất kỳ dòng trống nào trong Cache $\rightarrow$ Tỷ lệ trúng cao nhất, linh hoạt nhưng mạch so sánh đắt đỏ.
    - **세트-연관 매핑 (Set-Associative):** Dung hòa 2 cách trên: Cache chia thành các Set, mỗi khối RAM map vào 1 Set cố định, nhưng bên trong Set có thể chọn dòng tự do.
  - **2 chính sách ghi (Write Policy):**
    - **Write-Through:** CPU ghi đồng thời cả vào Cache LẪN RAM $\rightarrow$ Nhất quán dữ liệu tuyệt đối nhưng làm chậm tốc độ CPU vì phải đợi RAM.
    - **Write-Back:** CPU chỉ ghi vào Cache; chỉ khi khối đó bị đẩy ra ngoài (Evicted) thì mới chép ngược về RAM $\rightarrow$ Tốc độ tối đa nhưng cấu trúc phức tạp (cần Dirty Bit).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Công thức tính toán hiệu năng Cache:**
  $$\text{적중률 (Hit Ratio)} = H = \frac{\text{Số lần trúng (Hits)}}{\text{Tổng số lần truy cập (Total Accesses)}}$$
  $$\text{Effective Access Time} = H \cdot T_c + (1 - H) \cdot T_m$$
  *(Trong đó $T_c$ là thời gian truy cập Cache, $T_m$ là thời gian truy cập RAM).*

- **Bảng so sánh 3 kỹ thuật ánh xạ (Mapping Process):**

| Phương pháp ánh xạ | Cơ chế phân phối khối | Ưu điểm cốt lõi | Nhược điểm (Bẫy đề thi) |
| :--- | :--- | :--- | :--- |
| **직접 매핑 (Direct)** | Khối $i$ của RAM chỉ được map vào dòng $i \pmod m$ của Cache | Mạch phần cứng rất đơn giản, chi phí rẻ, tốc độ tra cứu nhanh | Xung đột vị trí cao (Conflict Miss); nếu 2 khối tranh chấp 1 dòng sẽ bị hoán đổi liên tục |
| **연관 매핑 (Associative)** | Bất kỳ khối nào của RAM cũng có thể đặt vào bất kỳ dòng nào còn trống của Cache | Tỷ lệ trúng cao nhất; không bị xung đột vị trí cố định | Đòi hỏi mạch so sánh song song phức tạp (CAM), giá thành đắt |
| **세트-연관 매핑 (Set-Associative)** | Chia Cache thành các Tập hợp (Sets); RAM map vào Set cố định, nhưng tự do chọn Way trong Set | Kết hợp ưu điểm của cả hai: chi phí phần cứng vừa phải và tỷ lệ xung đột thấp | Phổ biến nhất trong kiến trúc CPU hiện đại (2-Way, 4-Way, 8-Way) |

- **Bảng so sánh 2 chính sách ghi (Write Policy):**

| Chính sách ghi | Cơ chế cập nhật | Ưu điểm | Nhược điểm |
| :--- | :--- | :--- | :--- |
| **Write-Through (Ghi xuyên suốt)** | Khi ghi dữ liệu, cập nhật **đồng thời cả vào Cache và RAM** | Tính nhất quán dữ liệu cao; không bao giờ bị lệch dữ liệu giữa Cache và RAM | Ghi chậm do tốc độ bị nghẽn ở phía RAM; tiêu tốn băng thông bus |
| **Write-Back (Ghi trả sau)** | Chỉ cập nhật trên Cache; chỉ khi khối bị thay thế mới chép lại về RAM | Tốc độ xử lý của CPU đạt mức cao nhất; giảm tối đa số lần ghi vào RAM | Cần thêm cờ kiểm tra (Dirty bit / Modified bit); nguy cơ mất dữ liệu nếu sập nguồn đột ngột |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính cục bộ của tham chiếu (Locality of Reference):**
  - Cache hoạt động hiệu quả nhờ 2 nguyên lý cục bộ của chương trình máy tính:
    - **시간 구역성 (Temporal Locality):** Một biến hay chỉ mục vừa được truy cập thì rất có khả năng sẽ được truy cập lại trong tương lai gần (ví dụ: biến đếm vòng lặp `for`).
    - **공간 구역성 (Spatial Locality):** Một ô nhớ vừa được truy cập thì các ô nhớ nằm liền kề nó cũng sẽ được truy cập tiếp theo (ví dụ: duyệt tuần tự các phần tử mảng `A[i]`, `A[i+1]`).

### 복습 체크리스트
- [ ] Tính được Hit Ratio = Hits / Total Accesses.
- [ ] Phân biệt được Direct Mapping (cố định), Associative Mapping (bất kỳ), và Set-Associative (dung hòa).
- [ ] Nhớ Write-Through ghi đồng thời vào RAM, Write-Back chỉ ghi khi khối bị đẩy ra ngoài.
- [ ] Giải thích được nguyên lý Temporal Locality (thời gian) và Spatial Locality (không gian).
