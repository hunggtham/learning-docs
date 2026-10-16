# IP 주소 체계, IPv4 vs IPv6 및 서브네팅 (Địa chỉ IP, IPv4/IPv6 & Subnetting)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc không gian địa chỉ IPv4 (32-bit) và đặc trưng của 5 lớp địa chỉ (Class A, B, C, D-Multicast, E-Dự phòng) cùng các dải IP đặc biệt (Private IP, Loopback `127.0.0.1`).
- Thành thạo phương pháp tính toán kỹ thuật chia mạng con (서브네팅 - Subnetting): xác định Subnet Mask, tính số mạng con tạo được, số lượng host khả dụng ($2^H - 2$), địa chỉ mạng (Network ID) và địa chỉ quảng bá (Broadcast IP).
- Phân biệt sự khác nhau toàn diện giữa IPv4 (32-bit) và IPv6 (128-bit); nắm vững 3 phương thức truyền thông trong IPv6 (Unicast, Multicast, Anycast - không có Broadcast) và quy tắc rút gọn địa chỉ IPv6 với dấu `::`.

## 핵심 키워드 (Từ khóa)
- IPv4 클래스 (IPv4 Classes) — Class A (대규모), Class B (중규모), Class C (소규모), Class D (멀티캐스트).
- 서브넷 마스크 및 CIDR (Subnet Mask & CIDR) — Mặt nạ phân tách Network ID và Host ID; ký hiệu `/n`.
- 가용 호스트 수 계산 (Usable Hosts Calculation) — Công thức $2^{\text{Host bits}} - 2$ (trừ địa chỉ mạng và broadcast).
- IPv6 주소 체계 (IPv6 Address) — 128-bit thập lục phân, 8 nhóm, bảo mật IPSec tích hợp sẵn.
- IPv6 3대 전송 방식 (IPv6 Transmission Types) — 유니캐스트 (Unicast), 멀티캐스트 (Multicast), 애니캐스트 (Anycast).
- 브로드캐스트 부재 (No Broadcast in IPv6) — IPv6 loại bỏ hoàn toàn Broadcast, thay thế bằng Multicast.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `16-mang-may-tinh-osi-7-tang-va-giao-thuc.md` (giao thức IP ở Tầng Network) và `17-tang-giao-van-tcp-udp-va-kiem-soat-luong.md` (địa chỉ IP làm đích đến cho các kết nối TCP/UDP).
- **Đang giải quyết gì (Current Problem):** Giải quyết dạng bài toán tính toán số học bắt buộc xuất hiện trong mọi kỳ thi kỹ sư: Cho một dải địa chỉ IP kèm Subnet Mask, tính toán xem có bao nhiêu máy tính có thể kết nối được và xác định địa chỉ Broadcast của mạng con.
- **Dùng đi đâu (Forward Handoff):** Sau khi làm chủ toàn bộ hạ tầng phần cứng, mạng và hệ điều hành, chương trình sẽ bước vào Phân khu 4 về Triển khai Server, Thiết kế mô-đun hóa và Kỹ nghệ phần mềm với bài `19-thiet-ke-mo-dun-coupling-va-cohesion.md`.

## 읽는 방법 (Cách đọc)
- **Nhận diện Class IPv4 qua octet đầu tiên:**
  - $1 \sim 126$ $\rightarrow$ **Class A** (Mặc định `/8` hay `255.0.0.0`).
  - $128 \sim 191$ $\rightarrow$ **Class B** (Mặc định `/16` hay `255.255.0.0`).
  - $192 \sim 223$ $\rightarrow$ **Class C** (Mặc định `/24` hay `255.255.255.0`).
  - $224 \sim 239$ $\rightarrow$ **Class D (Multicast)**.
  - $127.0.0.1$ $\rightarrow$ **Loopback (nội bộ máy)**.
- **Tính số Host khả dụng:** Cứ nhớ phải lấy $2^{\text{số bit 0 còn lại}} - 2$. Trừ 2 là vì: 1 địa chỉ mạng (phần host toàn 0) và 1 địa chỉ broadcast (phần host toàn 1).
- **IPv6:** Nhớ ngay 3 chữ: **Unicast, Multicast, Anycast**. Nếu đề thi xuất hiện chữ **"Broadcast" trong IPv6 $\rightarrow$ Phương án đó là SAI**.

---

## IP 주소 체계, IPv4 vs IPv6 및 서브네팅

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `IPv4는 32비트 주소로 Class A/B/C/D(멀티캐스트)/E로 나뉘며, 서브네팅 시 가용 호스트 수는 (2^H - 2)개이다. IPv6는 128비트 주소로 유니캐스트, 멀티캐스트, 애니캐스트 3가지만 존재하며 브로드캐스트는 존재하지 않는다.`
  - [Tiếng Việt]: IPv4 là địa chỉ 32 bit chia làm các lớp A/B/C/D(Multicast)/E, khi chia mạng con số host dùng được là (2^H - 2). IPv6 là địa chỉ 128 bit chỉ gồm 3 phương thức truyền: Unicast, Multicast, Anycast và hoàn toàn không có Broadcast.

- **1. Bảng phân lớp địa chỉ IPv4 (IPv4 클래스 분류):**

| Lớp (Class) | Bit khởi đầu | Dải octet đầu tiên | Network ID / Host ID | Số Host tối đa mỗi mạng | Mục đích sử dụng |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Class A** | `0...` | **$1 \sim 126$** | 8 bit / 24 bit (`/8`) | $2^{24} - 2 \approx \mathbf{16,777,214}$ | Mạng cơ quan quy mô khổng lồ toàn cầu. |
| **Class B** | `10...` | **$128 \sim 191$** | 16 bit / 16 bit (`/16`)| $2^{16} - 2 = \mathbf{65,534}$ | Mạng trường đại học, tổ chức quy mô vừa. |
| **Class C** | `110...` | **$192 \sim 223$** | 24 bit / 8 bit (`/24`) | $2^8 - 2 = \mathbf{254}$ | Mạng doanh nghiệp nhỏ, hộ gia đình. |
| **Class D** | `1110...` | **$224 \sim 239$** | Không chia host | — | **Dành riêng cho truyền thông Multicast**. |
| **Class E** | `1111...` | **$240 \sim 255$** | Không chia host | — | Dành riêng cho nghiên cứu, thử nghiệm. |

- **2. Bảng đối chiếu toàn diện: IPv4 vs IPv6:**

| Tiêu chuẩn so sánh | Không gian địa chỉ IPv4 | Không gian địa chỉ IPv6 |
| :--- | :--- | :--- |
| **Độ dài địa chỉ** | **32 bit** (gồm 4 nhóm 8-bit, cách nhau bằng dấu chấm `.`). | **128 bit** (gồm 8 nhóm 16-bit, cách nhau bằng dấu hai chấm `:`). |
| **Phương thức biểu diễn**| Số thập phân: `192.168.1.1` | Số thập lục phân: `2001:0db8:85a3::8a2e:0370:7334` |
| **Không gian địa chỉ** | Khoảng $2^{32} \approx 4.3 \times 10^9$ địa chỉ (đã cạn kiệt). | Khoảng $2^{128} \approx 3.4 \times 10^{38}$ địa chỉ (gần như vô tận). |
| **3 phương thức truyền** | **Unicast, Multicast, Broadcast**. | **Unicast, Multicast, Anycast (KHÔNG CÓ Broadcast)**. |
| **Tính năng bảo mật** | Tùy chọn (Cài đặt thêm IPSec). | **Tích hợp sẵn IPSec mặc định** ở tầng mạng. |
| **Cấu trúc Header** | Biến đổi từ 20 đến 60 Bytes; xử lý phức tạp. | **Cố định 40 Bytes**; đơn giản hóa, định tuyến nhanh hơn. |

- **3. Quy tắc rút gọn địa chỉ IPv6 chuẩn RFC:**
  1. **Lược bỏ các số 0 đứng đầu mỗi nhóm:** Ví dụ nhóm `0042` rút thành `42`, nhóm `0000` rút thành `0`.
  2. **Rút gọn dãy nhóm toàn số 0 liên tiếp bằng `::`:** 
     - Địa chỉ gốc: `2001:0DB8:0000:0000:0000:0000:1428:57ab`
     - Rút gọn số 0 đầu: `2001:DB8:0:0:0:0:1428:57ab`
     - Rút gọn dãy số 0 bằng `::`: `2001:DB8::1428:57ab`
     - **Lưu ý tối cao:** Dấu `::` **chỉ được phép xuất hiện duy nhất 1 lần** trong toàn bộ địa chỉ IPv6.

- **주의/함정 (Bẫy đề thi):**
  - **Công thức tính số Host khả dụng:** Luôn luôn phải nhớ **trừ đi 2**: $2^H - 2$. Đề thi đưa ra đáp án gài là $2^H$ (quên trừ 2) để bẫy thí sinh.
  - **IPv6 Anycast:** Anycast là phương thức gửi gói tin đến **duy nhất 1 máy tính gần nhất** (về mặt khoảng cách định tuyến) trong số một nhóm các máy tính cùng chia sẻ chung địa chỉ Anycast đó.
  - **Địa chỉ Loopback:** Trong IPv4 là `127.0.0.1`, trong IPv6 là `::1`.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"IPv4 32 bit trừ 2 ra host, IPv6 128 bit có Unicast, Multicast, Anycast và cấm tiệt Broadcast."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán trắc nghiệm tính toán chia mạng con Subnetting chuẩn đề thi HRDK:
- **Đề bài:** Cho một dải địa chỉ mạng Class C: `192.168.10.0/24`. Người quản trị mạng muốn chia mạng này thành các mạng con nhỏ hơn bằng cách sử dụng Subnet Mask là `255.255.255.192`. Hỏi:
  1. Có bao nhiêu mạng con được tạo ra?
  2. Mỗi mạng con có tối đa bao nhiêu địa chỉ IP có thể gán được cho máy tính (Host khả dụng)?
  3. Xác định địa chỉ Broadcast của mạng con đầu tiên?

- **Phân tích từng bước chi tiết:**
  - **Bước 1: Phân tích Subnet Mask `255.255.255.192`:**
    - Octet cuối cùng là `192`. Đổi sang nhị phân 8-bit: $192 = \mathbf{11000000}_2$.
    - Như vậy, người quản trị đã mượn **$n = 2$ bit** của phần Host làm Subnet ID, còn lại **$H = 6$ bit** dành cho Host ID (Ký hiệu CIDR là `/26`).
  - **Bước 2: Tính số mạng con tạo được:**
    $$\text{Số mạng con} = 2^n = 2^2 = \mathbf{4\text{ mạng con}}.$$
  - **Bước 3: Tính số Host khả dụng trên mỗi mạng con:**
    $$\text{Số Host} = 2^H - 2 = 2^6 - 2 = 64 - 2 = \mathbf{62\text{ máy tính/mạng con}}.$$
  - **Bước 4: Xác định bước nhảy và dải địa chỉ mạng con:**
    - Bước nhảy giữa các mạng con là: $2^H = 2^6 = 64$.
    - Mạng con 1: Địa chỉ mạng là `192.168.10.0`
      - Dải IP gán cho máy: `192.168.10.1` đến `192.168.10.62`
      - **Địa chỉ Broadcast của mạng con 1 là: `192.168.10.63`**.
    - Mạng con 2: Bắt đầu từ `192.168.10.64`, Broadcast là `192.168.10.127`.
    - Mạng con 3: Bắt đầu từ `192.168.10.128`, Broadcast là `192.168.10.191`.
    - Mạng con 4: Bắt đầu từ `192.168.10.192`, Broadcast là `192.168.10.255`.

- **Bảng tổng hợp đáp án bài toán:**

| Câu hỏi kiểm tra | Giá trị tính toán |
| :--- | :---: |
| **Số mạng con tạo được** | **4 mạng con** |
| **Số Host khả dụng mỗi mạng** | **62 máy tính** |
| **Địa chỉ Broadcast mạng con 1** | **`192.168.10.63`** |

---

### 복습 체크리스트
- [ ] Nhớ dải octet đầu nhận diện lớp: Class A ($1-126$), Class B ($128-191$), Class C ($192-223$), Class D ($224-239$ Multicast).
- [ ] Ghi nhớ địa chỉ Loopback IPv4 là `127.0.0.1`, IPv6 là `::1`.
- [ ] Thuộc lòng công thức số host khả dụng: $2^H - 2$ (trừ mạng và broadcast).
- [ ] Phân biệt được độ dài: IPv4 có 32 bit, IPv6 có 128 bit.
- [ ] Thuộc lòng 3 phương thức truyền của IPv6: Unicast, Multicast, Anycast.
- [ ] Nhớ kỹ: IPv6 loại bỏ hoàn toàn Broadcast; dấu `::` chỉ được rút gọn 1 lần duy nhất.
