# 089. IP와 서브네팅, IPv4 vs IPv6 (IP & Subnetting)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc phân lớp địa chỉ IPv4 theo tiêu chuẩn Classful: Lớp A (Mạng cực lớn), Lớp B (Mạng trung bình), Lớp C (Mạng nhỏ), Lớp D (Truyền đa hướng Multicast), và Lớp E (Nghiên cứu thử nghiệm).
- Hiểu sâu nguyên lý mặt nạ mạng con (서브넷 마스크 - Subnet Mask) và kỹ thuật chia mạng con (서브네팅 - Subnetting) nhằm tối ưu hóa việc phân phối dải địa chỉ IP và giảm thiểu miền quảng bá (Broadcast Domain).
- Rèn luyện kỹ năng giải các bài toán tính toán mạng con: Xác định địa chỉ mạng (Network ID), địa chỉ quảng bá (Broadcast Address), và số lượng máy trạm khả dụng ($2^h - 2$).
- Phân biệt 4 hình thức truyền dữ liệu mạng: Đơn hướng (Unicast), Đa hướng (Multicast), Quảng bá (Broadcast), và Bất kỳ (Anycast).

## 핵심 키워드 (Từ khóa)
- IP 주소 체계 (IPv4 vs IPv6)
- IPv4 클래스 (Class A: `0.~`, Class B: `128.~`, Class C: `192.~`)
- 서브넷 마스크 (Subnet Mask / AND 연산)
- 서브네팅 계산 (Subnetting / 네트워크 ID, 브로드캐스트 ID)
- 유효 호스트 수 ($2^h - 2$)
- 전송 방식 4가지 (유니캐스트, 멀티캐스트, 브로드캐스트, 애니캐스트)

## 선행·연결 개념 (Kiến thức liên kết)
- [48-bai-hoc.md](48-bai-hoc.md): Lập trình hướng đối tượng và các nguyên lý OOP.
- [50-bai-hoc.md](50-bai-hoc.md): Câu lệnh rẽ nhánh đa tầng `if - else if`.
- [44-bai-hoc.md](44-bai-hoc.md): Mô hình OSI 7 tầng và địa chỉ logic tầng mạng.

## 읽는 방법 (Cách đọc)
- Phân biệt các dải số lớp IPv4 qua byte đầu tiên:
  - **Class A:** Byte đầu bắt đầu bằng bit `0` $\rightarrow$ Từ **`0.0.0.0` đến `127.255.255.255`**. Subnet mask mặc định: `255.0.0.0`. Dành cho các tổ chức khổng lồ.
  - **Class B:** Byte đầu bắt đầu bằng bit `10` $\rightarrow$ Từ **`128.0.0.0` đến `191.255.255.255`**. Subnet mask mặc định: `255.255.0.0`. Dành cho các doanh nghiệp vừa.
  - **Class C:** Byte đầu bắt đầu bằng bit `110` $\rightarrow$ Từ **`192.0.0.0` đến `223.255.255.255`**. Subnet mask mặc định: `255.255.255.0`. Dành cho mạng nội bộ nhỏ.
  - **Class D:** Từ `224.0.0.0` đến `239.255.255.255` $\rightarrow$ Dùng cho **Multicast**.
  - **Class E:** Từ `240.0.0.0` trở đi $\rightarrow$ Dùng nghiên cứu thử nghiệm (Experimental).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng các lớp địa chỉ IPv4 tiêu chuẩn (IPv4 Classes):**

| Lớp mạng | Bit mở đầu | Dải địa chỉ Byte đầu | Subnet Mask mặc định | Tỷ lệ Network ID / Host ID | Số host tối đa mỗi mạng |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **Class A** | `0...` | **`1` ~ `126`** (127 là loopback) | `255.0.0.0` (`/8`) | 8 bits / 24 bits | $2^{24} - 2 \approx 16.7$ triệu hosts |
| **Class B** | `10..` | **`128` ~ `191`** | `255.255.0.0` (`/16`) | 16 bits / 16 bits | $2^{16} - 2 = 65,534$ hosts |
| **Class C** | `110.` | **`192` ~ `223`** | `255.255.255.0` (`/24`) | 24 bits / 8 bits | $2^8 - 2 = 254$ hosts |
| **Class D** | `1110` | **`224` ~ `239`** | Không có | Không phân chia Host | Dùng riêng cho **멀티캐스트 (Multicast)** |
| **Class E** | `1111` | **`240` ~ `255`** | Không có | Không phân chia Host | Dành riêng cho nghiên cứu, dự phòng |

- **Công thức tính toán chia mạng con (Subnetting):**
  - Giả sử mượn $b$ bits của phần Host làm Subnet ID, phần Host còn lại $h$ bits:
    $$\text{Số lượng mạng con sinh ra} = 2^b$$
    $$\text{Số lượng máy trạm khả dụng trên mỗi mạng con} = 2^h - 2$$
  - *(Lý do phải trừ 2: Vì trừ đi địa chỉ mạng đầu tiên `Host ID toàn 0` và địa chỉ quảng bá cuối cùng `Host ID toàn 1`).*

- **Bảng phân loại 4 phương thức truyền dữ liệu:**

| Kiểu truyền | Ký hiệu quan hệ | Bản chất kỹ thuật truyền thông | Hệ điều hành hỗ trợ |
| :--- | :---: | :--- | :--- |
| **유니캐스트 (Unicast)** | **1 : 1** | Gửi từ một máy nguồn duy nhất đến **đúng một máy đích** xác định | IPv4 và IPv6 |
| **멀티캐스트 (Multicast)** | **1 : N** | Gửi từ một máy nguồn đến **một nhóm các máy trạm cụ thể** đã đăng ký | IPv4 (Class D) và IPv6 |
| **브로드캐스트 (Broadcast)** | **1 : All** | Gửi từ một máy nguồn đến **toàn bộ tất cả các máy trong cùng mạng** | **Chỉ có trong IPv4** (IPv6 đã loại bỏ) |
| **애니캐스트 (Anycast)** | **1 : 1 (Gần nhất)** | Gửi từ máy nguồn đến **đúng một máy trạm nằm ở vị trí gần nhất** trong nhóm | **Chỉ có trong IPv6** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán thi mẫu tính toán chia mạng con:**
  - *Đề bài:* Cho dải IP mạng Class C: `192.168.1.0/26`. Hãy xác định Subnet Mask, số lượng mạng con, số host tối đa mỗi mạng, và địa chỉ mạng của dải chứa IP `192.168.1.100`.
  - *Lời giải chi tiết:*
    1. Tiền tố `/26` nghĩa là có 26 bit 1 trong Subnet Mask $\rightarrow$ Byte cuối cùng có 2 bit mượn: $11000000_2 = 128 + 64 = 192$. Subnet Mask là `255.255.255.192`.
    2. Số mạng con sinh ra: Mượn 2 bit $\rightarrow 2^2 = \mathbf{4\text{ mạng con}}$.
    3. Số bit Host còn lại: $32 - 26 = 6\text{ bits}$. Số host dùng được: $2^6 - 2 = 64 - 2 = \mathbf{62\text{ hosts/mạng}}$.
    4. Bốn dải mạng con:
       - Mạng 1: `192.168.1.0` đến `.63` (Host: `.1` đến `.62`)
       - Mạng 2: `192.168.1.64` đến `.127` (Host: `.65` đến `.126`)
       - Mạng 3: `192.168.1.128` đến `.191`
       - Mạng 4: `192.168.1.192` đến `.255`
    5. IP `192.168.1.100` rơi vào dải Mạng 2 $\rightarrow$ Địa chỉ mạng là **`192.168.1.64`**, địa chỉ Broadcast là **`192.168.1.127`**.

### 복습 체크리스트
- [ ] Nhớ số byte đầu của các lớp: Class A (1-126), Class B (128-191), Class C (192-223).
- [ ] Nhớ công thức số host dùng được: $2^h - 2$ (trừ Network ID và Broadcast ID).
- [ ] Phân biệt được Unicast (1:1), Multicast (1:nhóm), Broadcast (1:tất cả - chỉ IPv4), Anycast (1:gần nhất - chỉ IPv6).
- [ ] Tính thành thạo Subnet Mask từ ký pháp CIDR (ví dụ: `/26` ra `.192`).
