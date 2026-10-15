# 핵심 110: RAM (Random Access Memory) - DRAM vs SRAM

## 학습 목표 (Mục tiêu)
- Nắm vững đặc tính vật lý và nguyên lý vận hành của bộ nhớ truy cập ngẫu nhiên RAM (Random Access Memory) - bộ nhớ khả biến (휘발성 메모리 / Volatile Memory).
- Phân biệt sâu sắc và toàn diện giữa DRAM (Dynamic RAM) và SRAM (Static RAM) trên 6 tiêu chuẩn cốt lõi: Cấu tạo linh kiện, Chu kỳ làm tươi (Refresh), Tốc độ truy cập, Mật độ tích hợp, Mức tiêu thụ điện năng và Giá thành.
- Hiểu rõ vị trí và vai trò ứng dụng của DRAM (Bộ nhớ chính / Main Memory) và SRAM (Bộ nhớ đệm / Cache Memory) trong kiến trúc phân cấp bộ nhớ máy tính.

## 핵심 키워드 (Từ khóa)
- RAM (Random Access Memory / 휘발성 메모리)
- DRAM (Dynamic RAM / 커패시터 콘덴서 / 재충전 Refresh)
- SRAM (Static RAM / 플립플롭 Flip-Flop / 고속)
- 주기억장치 (Main Memory / DRAM 사용)
- 캐시 메모리 (Cache Memory / SRAM 사용)
- 집적도 (Integration Density)

## 선행·연결 개념 (Kiến thức liên kết)
- [82-bai-hoc.md](82-bai-hoc.md): Ghi chú phát hành phần mềm (Release Note).
- [84-bai-hoc.md](84-bai-hoc.md): Linh kiện nhớ bán dẫn và dung lượng bộ nhớ.
- [87-bai-hoc.md](87-bai-hoc.md): Cấu trúc và chính sách ghi của bộ nhớ đệm Cache Memory.

## 읽는 방법 (Cách đọc)
- Ghi nhớ bản chất qua hai linh kiện nền tảng:
  - **DRAM (Dynamic):** Cấu tạo từ **Tụ điện (콘덴서 / Capacitor)**. Tụ điện bị rò rỉ điện tích theo thời gian nên **bắt buộc phải nạp lại định kỳ (재충전 / Refresh)** nếu không sẽ mất dữ liệu. Bù lại cấu tạo đơn giản, mật độ tích hợp cực cao, giá rẻ $\rightarrow$ Dùng làm thanh RAM chính trong máy tính.
  - **SRAM (Static):** Cấu tạo từ **Mạch lật Flip-Flop**. Có điện là giữ nguyên trạng thái, **không cần làm tươi (Refresh 불필요)**. Tốc độ cực nhanh, tiêu thụ ít điện năng nhưng mạch phức tạp, đắt tiền $\rightarrow$ Dùng làm bộ nhớ đệm Cache bên trong CPU.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh kinh điển 6 tiêu chí giữa DRAM và SRAM:**

| Tiêu chuẩn so sánh | DRAM (Dynamic RAM - RAM động) | SRAM (Static RAM - RAM tĩnh) |
| :--- | :--- | :--- |
| **Cấu tạo linh kiện (구성 소자)** | **커패시터 / 콘덴서 (Tụ điện Capacitor)** | **플립플롭 (Mạch lật Flip-Flop)** |
| **Làm tươi (재충전 / Refresh)** | **Cần làm tươi định kỳ (필요)** do tụ rò điện | **Không cần làm tươi (불필요)** khi có nguồn điện |
| **Tốc độ truy cập (접근 속도)** | Chậm hơn (느림) | Cực nhanh (빠름) |
| **Mật độ tích hợp (집적도)** | **Cao (높음)**; chứa được nhiều bit trên diện tích nhỏ | **Thấp (낮음)**; mạch lật tốn nhiều transistor |
| **Tiêu thụ điện (전력 소모)** | Tương đối nhiều hơn do chu kỳ nạp lại | Ít hơn ở trạng thái tĩnh |
| **Giá thành (가격)** | Rẻ (저가) | Đắt (고가) |
| **Ứng dụng chủ đạo (주요 용도)** | **주기억장치 (Bộ nhớ chính / Thanh RAM)** | **캐시 메모리 (Cache Memory L1/L2/L3)** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Đặc tính khả biến (Volatile Memory):**
  - Cả DRAM và SRAM đều là bộ nhớ khả biến (휘발성): Dữ liệu sẽ lập tức biến mất hoàn toàn khi tắt nguồn điện máy tính.
  - Ngược lại với RAM là ROM (Read Only Memory - bộ nhớ bất biến / 비휘발성) như Flash ROM, EEPROM dùng để lưu trữ BIOS/UEFI.

### 복습 체크리스트
- [ ] Nhớ linh kiện cấu tạo: DRAM dùng Tụ điện (콘덴서), SRAM dùng Mạch lật (플립플롭).
- [ ] Nhớ DRAM cần 재충전 (Refresh) định kỳ, SRAM không cần Refresh.
- [ ] Nhớ DRAM dùng làm 주기억장치 (Main Memory), SRAM dùng làm 캐시 메모리 (Cache).
- [ ] Nhớ DRAM có 집적도 (mật độ tích hợp) cao hơn và giá rẻ hơn SRAM.
