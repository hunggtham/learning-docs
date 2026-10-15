# 핵심 111 & 112: 반도체 기억소자 및 자기 코어 (Semiconductor Memory & Magnetic Core)

## 학습 목표 (Mục tiêu)
- Nắm vững công thức và phương pháp tính toán dung lượng bộ nhớ bán dẫn dựa trên số lượng đường bus địa chỉ (Address Bus) và bus dữ liệu (Data Bus).
- Hiểu rõ mối liên hệ giữa thanh ghi địa chỉ bộ nhớ (MAR), thanh ghi đệm bộ nhớ (MBR) với cấu trúc từ nhớ (Word).
- Nắm vững đặc tính vật lý và cấu tạo của lõi từ (자기 코어 - Magnetic Core): bộ nhớ phá hủy khi đọc (DRO Memory), chu kỳ khôi phục dữ liệu (Restoration Time) và cấu trúc 4 dây truyền dẫn.

## 핵심 키워드 (Từ khóa)
- 주소 버스 (Address Bus / Đường địa chỉ / $2^n$ Words)
- 데이터 버스 (Data Bus / Đường dữ liệu / Kích thước Word)
- 기억용량 계산 (Memory Capacity Calculation)
- MAR & MBR (Memory Address Register & Memory Buffer Register)
- 자기 코어 (Magnetic Core / Lõi từ)
- 파괴 메모리 (DRO - Destructive Read Out)
- 4선식 구조 (4-wire Structure: X구동선, Y구동선, 센스선, 금지선)

## 선행·연결 개념 (Kiến thức liên kết)
- [83-bai-hoc.md](83-bai-hoc.md): Bộ nhớ RAM - So sánh toàn diện DRAM và SRAM.
- [85-bai-hoc.md](85-bai-hoc.md): Bộ nhớ phụ và thời gian truy cập đĩa từ (Disk Access Time).
- [정보처리기사/output/04-programming-language/lessons/01-bai-hoc.md](../../04-programming-language/lessons/01-bai-hoc.md): Kiến trúc máy tính và quản lý không gian nhớ.

## 읽는 방법 (Cách đọc)
- Nhớ công thức tính dung lượng bộ nhớ chuẩn thi:
  $$\text{Dung lượng (Capacity)} = (\text{Số Word}) \times (\text{Độ dài Word})$$
  - Với $n$ đường Address Bus $\rightarrow$ Tạo ra $2^n$ địa chỉ (tương ứng với $2^n$ Words, quyết định dung lượng MAR).
  - Với $m$ đường Data Bus $\rightarrow$ Mỗi Word có độ dài $m$ bits (quyết định độ rộng MBR).
  - Ví dụ: 7 Address lines, 8 Data lines $\rightarrow$ Dung lượng $= 2^7 \times 8\text{ bits} = 128 \times 8\text{ bits} = 128\text{ Bytes}$.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân tích mối quan hệ giữa Bus và Thanh ghi máy tính:**

| Thành phần | Đại lượng quyết định | Thanh ghi phần cứng tương ứng | Vai trò trong hệ thống |
| :--- | :--- | :--- | :--- |
| **Address Bus (주소선)** | Số lượng đường $n$ quyết định **tổng số Word ($2^n$)** | **MAR (Memory Address Register)** và **PC (Program Counter)** | Xác định phạm vi không gian địa chỉ tối đa CPU có thể trỏ tới |
| **Data Bus (데이터선)** | Số lượng đường $m$ quyết định **kích thước mỗi Word ($m$ bits)** | **MBR (Memory Buffer Register)** và **IR (Instruction Register)** | Xác định độ rộng của kênh truyền dữ liệu mỗi lần nạp/ghi |

- **Đặc tính kỹ thuật của bộ nhớ Lõi từ (자기 코어 - Magnetic Core):**

| Tiêu chí | Nội dung chi tiết chuẩn thi |
| :--- | :--- |
| **Nguyên lý đọc** | Là bộ nhớ **파괴 판독 메모리 (DRO - Destructive Read Out)**; thao tác đọc làm mất từ tính của lõi |
| **Chu kỳ ghi lại** | Bắt buộc phải có khoảng thời gian **재저장 시간 (Restoration Time)** để ghi phục hồi lại dữ liệu vừa đọc |
| **Cấu tạo 4 dây (4-wire)** | - **2 dây điều khiển (구동선 X, Y):** Xác định tọa độ lõi cần đọc/ghi; **1 dây cảm biến (센스 선 - Sense line):** Đọc tín hiệu trạng thái 0 hoặc 1; **1 dây cấm (금지 선 - Inhibit line):** Ngăn chặn việc thay đổi trạng thái khi ghi dữ liệu |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán thi mẫu về tính dung lượng bộ nhớ:**
  - *Đề bài:* Một hệ thống bộ nhớ có thanh ghi MAR 16 bits và thanh ghi MBR 32 bits. Hỏi dung lượng tối đa của bộ nhớ này là bao nhiêu?
  - *Lời giải:*
    - Số Word $= 2^{16} = 65,536\text{ Words} = 64\text{ KWords}$.
    - Kích thước mỗi Word $= 32\text{ bits} = 4\text{ Bytes}$.
    - Tổng dung lượng $= 2^{16} \times 4\text{ Bytes} = 64\text{ K} \times 4\text{ Bytes} = 256\text{ KBytes}$.

### 복습 체크리스트
- [ ] Tính được dung lượng bộ nhớ: $2^{\text{Address lines}} \times \text{Data lines}$.
- [ ] Nhớ Address Bus quyết định số Word (MAR), Data Bus quyết định độ dài Word (MBR).
- [ ] Nhớ Magnetic Core là bộ nhớ 파괴 메모리 (DRO) cần thời gian tái lưu trữ (Restoration Time).
- [ ] Kể tên đủ 4 loại dây trong cấu tạo lõi từ: X구동선, Y구동선, 센스선, 금지선.
