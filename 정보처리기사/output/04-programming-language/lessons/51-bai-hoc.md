# 305 - 308. IP 주소 체계 (IPv4 vs IPv6)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc không gian địa chỉ, cấu trúc phân đoạn và định dạng biểu diễn của giao thức IPv4 (32-bit) và IPv6 (128-bit).
- Phân biệt rõ các cơ chế truyền thông (Transmission Modes) giữa hai thế hệ: Unicast, Multicast, Broadcast (chỉ có ở IPv4) và Anycast (IPv6 thay thế Broadcast).
- Hiểu các tính năng cải tiến vượt bậc của IPv6 về mặt an ninh bảo mật tích hợp (IPSec), khả năng tự cấu hình thiết bị (Plug & Play / SLAAC) và xử lý phần đầu gói tin (Header Optimization).

## 핵심 키워드 (Từ khóa)
- IPv4 (32비트, 8비트씩 4옥텟, 10진수)
- IPv6 (128비트, 16비트씩 8필드, 16진수)
- 유니캐스트 (Unicast / 1:1)
- 멀티캐스트 (Multicast / 1:N)
- 애니캐스트 (Anycast / 1:Closest 1)
- 브로드캐스트 부재 (IPv6 Broadcast Elimination)
- IPSec 기본 탑재 (Native IPSec Support)
- PnP / 자동 주소 설정 (SLAAC / Auto-configuration)

## 선행·연결 개념 (Kiến thức liên kết)
- [49-bai-hoc.md](49-bai-hoc.md): Phân lớp mạng IPv4 (Class A/B/C) và bài toán chia mạng con Subnetting.
- [50-bai-hoc.md](50-bai-hoc.md): Câu lệnh điều khiển logic rẽ nhánh `if - else if`.
- [52-bai-hoc.md](52-bai-hoc.md): Vòng đời trạng thái dữ liệu lỗi và các yếu tố kỹ thuật phần mềm.

## 읽는 방법 (Cách đọc)
- Trọng tâm câu hỏi thi trắc nghiệm và thực hành thường tập trung vào:
  - So sánh độ dài bit: IPv4 là **32 bit**, IPv6 là **128 bit** (gấp 4 lần số bit, không gian địa chỉ $2^{128}$).
  - Ký hiệu phân cách: IPv4 dùng dấu chấm `.`, IPv6 dùng dấu hai chấm `:`.
  - Phương thức truyền: Ghi nhớ khẩu quyết **유멀애** (Unicast, Multicast, Anycast). Đặc biệt chú ý: **IPv6 hoàn toàn không có Broadcast**; cơ chế gửi quảng bá được thay thế tối ưu bằng Multicast nhóm hoặc Anycast.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng đối chiếu tổng hợp toàn diện IPv4 vs IPv6:**

| Tiêu chí so sánh | IPv4 (Internet Protocol v4) | IPv6 (Internet Protocol v6) |
| :--- | :--- | :--- |
| **Độ dài địa chỉ** | **32 bit** (4 Byte) | **128 bit** (16 Byte) |
| **Cấu trúc phân đoạn** | 4 phần (mỗi phần 8 bit = 1 Octet) | 8 nhóm (mỗi nhóm 16 bit) |
| **Hệ số biểu diễn** | Thập phân (Decimal, 0~255) | Thập lục phân (Hexadecimal, 0~FFFF) |
| **Dấu phân cách** | Dấu chấm (`.`) | Dấu hai chấm (`:`) |
| **Không gian địa chỉ** | Khoảng $2^{32} \approx 4.3 \times 10^9$ địa chỉ (đã cạn kiệt) | $2^{128} \approx 3.4 \times 10^{38}$ (gần như vô hạn) |
| **Phương thức truyền** | **Unicast, Multicast, Broadcast** | **Unicast, Multicast, Anycast** (Không có Broadcast) |
| **Bảo mật (Security)** | Tùy chọn mở rộng (Optional IPSec) | **Bắt buộc / Tích hợp sẵn (Native IPSec)** |
| **Cấu hình địa chỉ** | Gán tĩnh hoặc qua máy chủ DHCP | **Plug & Play tự động (SLAAC / Auto-configuration)** |
| **Độ dài Header** | Biến thiên (20 ~ 60 Byte) | **Cố định chuẩn (40 Byte)** giúp định tuyến cực nhanh |

- **3 phương thức truyền gói tin của IPv6 (유멀애):**
  1. **Unicast (유니캐스트 / 1:1):** Gửi gói tin từ một nguồn duy nhất đến đúng một đích duy nhất trên mạng.
  2. **Multicast (멀티캐스트 / 1:N):** Gửi gói tin từ một nguồn đến một nhóm các thiết bị đích đã đăng ký lắng nghe (Multicast Group).
  3. **Anycast (애니캐스트 / 1:가장 가까운 1):** Gửi gói tin đến nút mạng **gần nhất theo cấu trúc liên kết định tuyến (Topology)** trong số các nút chia sẻ cùng một địa chỉ Anycast.

- **Quy tắc rút gọn chuỗi địa chỉ IPv6:**
  - Có thể bỏ qua các số `0` ở đầu mỗi nhóm 16-bit (ví dụ: `:0042:` rút gọn thành `:42:`).
  - Một chuỗi liên tiếp chứa toàn bộ các nhóm `0` (`0000:0000:...`) có thể được thay thế bằng cặp dấu hai chấm kép `::`. Lưu ý: **Cặp dấu `::` chỉ được xuất hiện duy nhất 1 lần** trong toàn bộ một chuỗi địa chỉ IPv6 để tránh gây nhập nhằng khi khôi phục.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế chuyển đổi và cùng tồn tại giữa IPv4 và IPv6:**
  - Trong giai đoạn chuyển tiếp mạng Internet toàn cầu, các giải pháp kỹ thuật kết hợp gồm:
    1. **Dual Stack (스택 이중화):** Thiết bị mạng hoặc máy chủ chạy đồng thời cả hai ngăn xếp giao thức IPv4 và IPv6 trên cùng một giao tiếp mạng.
    2. **Tunneling (터널링):** Đóng gói gói tin IPv6 vào bên trong gói tin IPv4 để truyền xuyên qua mạng đường trục IPv4 trung gian (ví dụ: 6to4, Teredo, ISATAP).
    3. **Translation (주소 변환):** Bộ chuyển đổi dịch địa chỉ ở tầng mạng hoặc tầng giao vận (như NAT-PT) chuyển đổi trực tiếp giữa tiêu đề gói tin IPv4 và IPv6.

### 복습 체크리스트
- [ ] Nhớ độ dài chính xác của IPv4 (32 bit, 4 octet) và IPv6 (128 bit, 8 nhóm hex).
- [ ] Nhớ khẩu quyết 3 phương thức truyền dữ liệu của IPv6: **유멀애** (Unicast, Multicast, Anycast).
- [ ] Khẳng định được IPv6 **không hỗ trợ Broadcast**, chức năng quảng bá được giải quyết bằng Multicast/Anycast.
- [ ] Nắm được nguyên tắc rút gọn địa chỉ IPv6 (bỏ số 0 ở đầu nhóm và chỉ dùng `::` duy nhất 1 lần).
- [ ] Phân biệt được 3 kỹ thuật chuyển tiếp IPv4 $\rightarrow$ IPv6: Dual Stack, Tunneling và Translation.
