# IP 주소 및 서브네팅 (Địa chỉ IP & Kỹ thuật Chia mạng con Subnetting)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc và phân lớp địa chỉ IPv4 (32-bit, Classes A, B, C, D, E) cùng dải địa chỉ nhận diện ban đầu.
- Làm chủ kỹ thuật chia mạng con (Subnetting), tính toán Mặt nạ mạng con (Subnet Mask), Địa chỉ mạng (Network Address), Địa chỉ quảng bá (Broadcast Address) và Số lượng máy trạm khả dụng ($2^h - 2$).
- Phân tích cấu trúc địa chỉ IPv6 (128-bit, 8 nhóm Hexadecimal) và các ưu thế vượt trội về bảo mật tích hợp (IPSec).
- Phân biệt 3 kiểu truyền thông của IPv6 (Unicast, Anycast, Multicast) và ghi nhớ việc IPv6 đã loại bỏ hoàn toàn chế độ Broadcast.

## 핵심 키워드 (Từ khóa)
- **IPv4 (32-bit)**: 4 Octet thập phân, Class A ($0 \sim 127$), Class B ($128 \sim 191$), Class C ($192 \sim 223$), Class D (Multicast), Class E (Dự phòng).
- **서브네팅 (Subnetting)**: Mượn bit của Host ID làm Subnet ID, số host khả dụng $= 2^h - 2$.
- **IPv6 (128-bit)**: 8 nhóm Hexadecimal phân tách bởi dấu hai chấm `:`, tích hợp sẵn IPSec, loại bỏ hoàn toàn Broadcast.
- **IPv6 3대 주소**: Unicast (1:1), Anycast (1:Gần nhất), Multicast (1:Nhiều).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [23-bai-hoc.md](23-bai-hoc.md) (Giao thức mạng IP, ICMP, ARP).
- Liên kết với [22-bai-hoc.md](22-bai-hoc.md) (Giao thức bảo mật VPN IPSec).
- Liên kết với [04-programming-language/51-bai-hoc.md](../../04-programming-language/lessons/51-bai-hoc.md) (So sánh chi tiết IPv4 và IPv6).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh Class của IPv4 qua Octet đầu tiên:
  - Bắt đầu từ $1 \sim 126$ $\rightarrow$ **Class A** (ví dụ: `10.x.x.x`).
  - Bắt đầu từ $128 \sim 191$ $\rightarrow$ **Class B** (ví dụ: `172.16.x.x`).
  - Bắt đầu từ $192 \sim 223$ $\rightarrow$ **Class C** (ví dụ: `192.168.1.x`).
  - Địa chỉ Multicast: **Class D** ($224 \sim 239$).
- Trong IPv6: **KHÔNG CÓ BROADCAST**! Nếu câu hỏi trắc nghiệm nói "IPv6 hỗ trợ Unicast, Multicast, Broadcast" $\rightarrow$ Câu đó là **SAI**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cấu trúc và Phân lớp địa chỉ IPv4
- **Độ dài**: 32 bits, chia thành 4 nhóm (Octet), mỗi nhóm 8 bits biểu diễn bằng số thập phân từ $0 \sim 255$ phân cách bởi dấu chấm `.` (ví dụ: `192.168.1.1`).
- **Phân loại 5 lớp địa chỉ (Classful Addressing)**:
  | Lớp mạng | Bit mở đầu | Dải Octet đầu tiên | Subnet Mask mặc định | Mục đích sử dụng |
  | :--- | :--- | :--- | :--- | :--- |
  | **Class A** | `0` | $0 \sim 127$ (Thực tế $1 \sim 126$) | `255.0.0.0` (/8) | Mạng quy mô quốc gia, tập đoàn viễn thông khổng lồ ($2^{24}$ hosts) |
  | **Class B** | `10` | $128 \sim 191$ | `255.255.0.0` (/16) | Doanh nghiệp và trường đại học quy mô vừa và lớn ($2^{16}$ hosts) |
  | **Class C** | `110` | $192 \sim 223$ | `255.255.255.0` (/24) | Mạng cục bộ quy mô nhỏ, công ty nhỏ ($2^8 - 2 = 254$ hosts) |
  | **Class D** | `1110` | $224 \sim 239$ | Không có Subnet Mask | Dành riêng cho truyền thông đa hướng (**Multicast**) |
  | **Class E** | `1111` | $240 \sim 255$ | Không có Subnet Mask | Dành riêng cho nghiên cứu khoa học và thử nghiệm tương lai |

*Lưu ý*: Địa chỉ `127.x.x.x` (đặc biệt `127.0.0.1`) là địa chỉ lặp nội bộ (**Loopback / Localhost**), không cấp cho máy trạm.

#### 2. Kỹ thuật chia mạng con (Subnetting)
- **Mục đích**: Chia một mạng IP vật lý lớn thành nhiều mạng con (Subnets) độc lập logic nhằm tiết kiệm địa chỉ IP, thu hẹp miền quảng bá (Broadcast Domain) và tăng cường bảo mật.
- **Công thức tính số máy trạm khả dụng**:
  - Giả sử sau khi mượn bit cho subnet, phần Host ID còn lại $h$ bits.
  - Số máy trạm (Host) thực tế có thể gán cho máy tính là:
    $$\text{Số Host khả dụng} = 2^h - 2$$
  - *Tại sao phải trừ đi 2?*
    1. Trừ **Địa chỉ mạng (Network Address)**: Khi tất cả các bit của Host ID đều bằng `0`.
    2. Trừ **Địa chỉ quảng bá (Broadcast Address)**: Khi tất cả các bit của Host ID đều bằng `1`.

#### 3. Địa chỉ thế hệ mới IPv6
- **Độ dài**: **128 bits**, chia làm **8 nhóm**, mỗi nhóm gồm 16 bits biểu diễn dưới dạng số thập lục phân (Hexadecimal $0 \sim F$) phân tách bằng dấu hai chấm `:` (ví dụ: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
- **Ưu thế vượt trội**:
  - Không gian địa chỉ vô tận ($2^{128}$ địa chỉ).
  - Tích hợp sẵn giao thức an ninh mạng **IPSec** ở tầng mạng (hỗ trợ xác thực Authentication và mã hóa mã hóa Encryption).
  - Hỗ trợ cơ chế tự động cấu hình không trạng thái (SLAAC - Plug and Play mạng).
  - Tiêu đề gói tin (Header) cố định 40 bytes, đơn giản hóa cấu trúc giúp Router định tuyến nhanh hơn.
- **3 hình thức truyền thông của IPv6**:
  - **Unicast**: Truyền tin từ một nguồn tới đúng **một đích duy nhất** (1:1).
  - **Anycast**: Truyền tin từ một nguồn tới **một máy chủ gần nhất** về mặt định tuyến mạng trong nhóm cùng địa chỉ (1:Nearest).
  - **Multicast**: Truyền tin từ một nguồn tới **tất cả các thành viên trong một nhóm** (1:Many).
  - *Đặc biệt lưu ý*: IPv6 **hoàn toàn không có hình thức Broadcast**; các tác vụ quảng bá được thay thế thông qua Multicast nhóm.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán tính Subnetting thực tế trong đề thi
- *Đề bài*: Cho địa chỉ mạng Class C: `192.168.1.0/24`. Hãy chia mạng này thành các mạng con sao cho mỗi mạng con có thể cấp phát được ít nhất 25 máy trạm. Xác định Subnet Mask và số máy trạm tối đa mỗi mạng con?
- *Lời giải chi tiết*:
  - Cần ít nhất 25 host khả dụng $\rightarrow 2^h - 2 \ge 25 \rightarrow 2^h \ge 27 \rightarrow$ Chọn $h = 5$ bits làm Host ID ($2^5 - 2 = 30$ hosts).
  - Mạng Class C gốc có 8 bits Host ($/24$). Để dành 5 bits cho Host ID, số bit mượn làm Subnet ID là: $8 - 5 = 3$ bits.
  - Mặt nạ mạng mới: $/24 + 3 = /27$.
  - Biểu diễn nhị phân của Octet cuối: `11100000` $= 128 + 64 + 32 = 224$.
  - Subnet Mask hoàn chỉnh: `255.255.255.224`.
  - Số mạng con tạo ra: $2^3 = 8$ mạng con.
  - Số host sử dụng được trong mỗi mạng con: $2^5 - 2 = 30$ máy trạm.

---

### 복습 체크리스트
- [ ] Dải địa chỉ IP của mạng Class B trong IPv4 bắt đầu từ số nào đến số nào?
- [ ] Tại sao khi tính số lượng Host khả dụng trong một mạng con luôn phải lấy $2^h - 2$?
- [ ] Địa chỉ IPv6 có độ dài bao nhiêu bits và được chia thành bao nhiêu nhóm?
- [ ] Kể tên 3 kiểu truyền thông địa chỉ của IPv6 và hình thức truyền thông nào của IPv4 đã bị loại bỏ hoàn toàn?
