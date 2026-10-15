# 네트워크 통신 (Network Communication)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc mạng truyền thông máy tính: Không gian địa chỉ IPv4 (32 bits) và IPv6 (128 bits), cùng các kiểu truyền dẫn dữ liệu (Unicast, Multicast, Broadcast, Anycast).
- Nhớ phân tầng mô hình tham chiếu OSI 7 tầng và vai trò của các thiết bị mạng phần cứng tương ứng: Bộ lặp (Repeater), Cầu nối (Bridge), Bộ chuyển mạch (Switch), và Bộ định tuyến (Router).
- Phân biệt sâu sắc hai giao thức tầng giao vận cốt lõi TCP (hướng kết nối, tin cậy) và UDP (không kết nối, tốc độ cao), cùng giao thức IoT chuyên dụng MQTT.

## 핵심 키워드 (Từ khóa)
- 네트워크 통신 (Network Communication)
- IPv4 (32비트 / 8비트씩 4부분 / 십진수 표기)
- IPv6 (128비트 / 16비트씩 8부분 / 16진수 표기 / Anycast)
- OSI 7계층 (물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용)
- 네트워크 장비 (리피터, 브리지, 스위치, 라우터)
- TCP vs UDP (연결 지향 vs 비연결 지향)
- MQTT (Message Queuing Telemetry Transport / IoT 경량 프로토콜)

## 선행·연결 개념 (Kiến thức liên kết)
- [42-bai-hoc.md](42-bai-hoc.md): Tiến trình, luồng và các giải thuật lập lịch.
- [44-bai-hoc.md](44-bai-hoc.md): Chi tiết mô hình OSI 7 tầng và đơn vị PDU.
- [45-bai-hoc.md](45-bai-hoc.md): Cơ chế điều khiển luồng và điều khiển lỗi của TCP.

## 읽는 방법 (Cách đọc)
- Phân biệt hai hệ thống địa chỉ IP:
  - **IPv4:** Gồm **32 bits** (chia làm 4 phần octet, mỗi phần 8 bits cách nhau bởi dấu chấm `.`). Có các lớp A, B, C, D, E.
  - **IPv6:** Gồm **128 bits** (chia làm 8 nhóm, mỗi nhóm 16 bits viết dưới dạng số hệ 16 cách nhau bởi dấu hai chấm `:`). Giải quyết triệt để tình trạng cạn kiệt địa chỉ của IPv4; hỗ trợ thêm kiểu truyền **Anycast** và tự động cấu hình địa chỉ.
- Phân biệt các thiết bị mạng theo tầng OSI:
  - Tầng 1 (Vật lý): **리피터 (Repeater)** - khuếch đại tín hiệu điện bị suy hao.
  - Tầng 2 (Liên kết dữ liệu): **브리지 (Bridge)** và **스위치 (Switch)** - kết nối mạng LAN, lọc gói theo địa chỉ phần cứng MAC.
  - Tầng 3 (Mạng): **라우터 (Router)** - tìm đường đi tối ưu nhất (Routing) trên mạng Internet toàn cầu qua địa chỉ IP.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh: Địa chỉ IPv4 vs IPv6:**

| Tiêu chuẩn so sánh | IPv4 (Internet Protocol v4) | IPv6 (Internet Protocol v6) |
| :--- | :--- | :--- |
| **Độ dài địa chỉ** | **32 bits** | **128 bits** (Gấp 4 lần độ dài IPv4) |
| **Định dạng biểu diễn** | 4 nhóm số thập phân cách nhau bằng **dấu chấm `.`** (ví dụ: `192.168.1.1`) | 8 nhóm số hệ 16 (Hex) cách nhau bằng **dấu hai chấm `:`** |
| **Không gian địa chỉ** | Khoảng 4.3 tỷ ($2^{32}$) địa chỉ (Đã cạn kiệt) | Khoảng $3.4 \times 10^{38}$ ($2^{128}$) địa chỉ (Gần như vô hạn) |
| **Các kiểu truyền dẫn** | **Unicast, Multicast, Broadcast** | **Unicast, Multicast, Anycast** (Đã **loại bỏ hoàn toàn Broadcast**) |
| **Tính năng bảo mật** | Tùy chọn cài đặt thêm IPSec | Tích hợp sẵn chuẩn bảo mật **IPSec** từ gốc |

- **Bảng phân loại các thiết bị phần cứng mạng (Network Devices):**

| Thiết bị | Tầng OSI đối ứng | Chức năng kỹ thuật cốt lõi chuẩn thi |
| :--- | :--- | :--- |
| **리피터 (Repeater)** | **Tầng 1 (Physical)** | Nhận tín hiệu điện bị suy giảm trên đường truyền xa, **khuếch đại và tái tạo lại tín hiệu** rồi gửi tiếp |
| **허브 (Hub)** | **Tầng 1 (Physical)** | Điểm kết nối tập trung nhiều dây mạng LAN; phát gói tin đến toàn bộ các cổng (Broadcast) |
| **브리지 (Bridge)** | **Tầng 2 (Data Link)** | Kết nối 2 phân đoạn mạng LAN cùng giao thức; **lọc khung dữ liệu dựa trên địa chỉ MAC** |
| **L2 스위치 (Switch)** | **Tầng 2 (Data Link)** | Thiết bị chuyển mạch nhiều cổng tốc độ cao; gửi khung trực tiếp đến cổng đích qua bảng MAC Table |
| **라우터 (Router)** | **Tầng 3 (Network)** | Định tuyến gói tin, **chọn đường đi tối ưu nhất** giữa các mạng khác nhau dựa trên bảng định tuyến IP |
| **게이트웨이 (Gateway)** | **Tầng 4 ~ 7 (Upper Layers)** | Cổng kết nối và chuyển đổi giao thức giữa hai mạng có kiến trúc hoàn toàn khác biệt |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Giao thức MQTT (Message Queuing Telemetry Transport):**
  - Là giao thức truyền thông điệp siêu nhẹ hoạt động trên nền TCP/IP theo mô hình **Xuất bản / Đăng ký (Publish / Subscribe)**.
  - Do tiêu tốn cực ít băng thông và năng lượng pin, MQTT trở thành chuẩn giao thức truyền thông số một trong hệ sinh thái vạn vật kết nối Internet (IoT - Internet of Things).

### 복습 체크리스트
- [ ] Nhớ độ dài địa chỉ: IPv4 là 32 bits, IPv6 là 128 bits.
- [ ] Nhớ IPv6 KHÔNG CÒN Broadcast, thay vào đó bổ sung Anycast (1:gần nhất).
- [ ] Phân biệt tầng hoạt động của thiết bị: Repeater (L1), Bridge/Switch (L2), Router (L3), Gateway (L4-L7).
- [ ] Nhớ MQTT là giao thức nhẹ chuẩn IoT theo mô hình Publish/Subscribe.
