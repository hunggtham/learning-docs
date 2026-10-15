# OSI 7계층 참조 모델 (Mô hình Tham chiếu OSI 7 Tầng)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc phân tầng, chức năng cốt lõi và đơn vị dữ liệu (PDU) của từng tầng trong mô hình tham chiếu OSI 7 tầng của tổ chức ISO.
- Phân biệt vai trò của 3 tầng cấp thấp (하위 계층: Physical, Data Link, Network) và 4 tầng cấp cao (상위 계층: Transport, Session, Presentation, Application).
- Làm chủ chức năng phân định luồng, kiểm soát lỗi, mã hóa và định tuyến giữa các hệ thống mạng mở dị thể.

## 핵심 키워드 (Từ khóa)
- **OSI 7계층 (7 Layers)**: 물-데-네-전-세-표-응 (Physical, Data Link, Network, Transport, Session, Presentation, Application).
- **데이터 단위 (PDU)**: Bit (물리), Frame (데이터링크), Packet (네트워크), Segment (전송), Data/Message (세션~응용).
- **핵심 기능**: 흐름 제어/오류 제어 (Data Link, Transport), 라우팅 경로 설정 (Network), 종단 간 신뢰 전송 (Transport), 암호화/압축 (Presentation).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [19-bai-hoc.md](19-bai-hoc.md) (Thiết bị mạng theo tầng OSI: Repeater, Switch, Router, Gateway).
- Liên kết với [23-bai-hoc.md](23-bai-hoc.md) (Các giao thức mạng tiêu biểu TCP, UDP, IP).
- Liên kết với [65-bai-hoc.md](65-bai-hoc.md) (Địa chỉ IP tầng mạng).

## 읽는 방법 (Cách đọc)
- Nhớ câu thần chú thứ tự từ tầng 1 đến tầng 7: **물 - 데 - 네 - 전 - 세 - 표 - 응** (Physical $\rightarrow$ Data Link $\rightarrow$ Network $\rightarrow$ Transport $\rightarrow$ Session $\rightarrow$ Presentation $\rightarrow$ Application).
- Phân biệt chức năng hay hỏi trong đề thi:
  - "Định tuyến đường đi (Routing), cấp phát địa chỉ IP logic" $\rightarrow$ **Network Layer (Tầng 3)**.
  - "Truyền thông tin cậy giữa hai đầu cuối (End-to-End), đánh số cổng Port" $\rightarrow$ **Transport Layer (Tầng 4)**.
  - "Mã hóa dữ liệu (Encryption), giải mã, nén dữ liệu, chuyển đổi mã ký tự ASCII/EBCDIC" $\rightarrow$ **Presentation Layer (Tầng 6)**.
  - "Đồng bộ hóa phiên hội thoại (Checkpoints, Dialog)" $\rightarrow$ **Session Layer (Tầng 5)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng tổng hợp Mô hình OSI 7 Tầng
| Tầng (Layer) | Tên tiếng Hàn & Anh | Đơn vị dữ liệu (PDU) | Thiết bị phần cứng | Chức năng kỹ thuật cốt lõi |
| :--- | :--- | :--- | :--- | :--- |
| **Tầng 7** | **응용 계층 / (Application)** | Data (Message) | L7 Switch, Gateway | Cung cấp giao diện dịch vụ mạng trực tiếp cho người dùng cuối (HTTP, FTP, SMTP, DNS) |
| **Tầng 6** | **표현 계층 / (Presentation)** | Data | Gateway | Định dạng dữ liệu, chuyển đổi mã hóa (Code conversion), **mã hóa bảo mật (Encryption)** và nén dữ liệu |
| **Tầng 5** | **세션 계층 / (Session)** | Data | Gateway | Thiết lập, duy trì, kết thúc phiên hội thoại giữa 2 ứng dụng; chèn các điểm kiểm tra đồng bộ (Synchronization Checkpoints) |
| **Tầng 4** | **전송 계층 / (Transport)** | **Segment** (TCP) / Datagram (UDP) | L4 Switch, Gateway | Truyền tải dữ liệu tin cậy giữa hai điểm đầu cuối (**End-to-End**); kiểm soát luồng (Flow Control), kiểm soát lỗi, ghép kênh |
| **Tầng 3** | **네트워크 계층 / (Network)** | **Packet** (Gói tin) | **Router**, L3 Switch | Định tuyến đường đi tối ưu (**Routing**), chuyển tiếp gói tin, đánh địa chỉ logic (IP Address), kiểm soát tắc nghẽn |
| **Tầng 2** | **데이터 링크 계층 / (Data Link)** | **Frame** (Khung tin) | **Switch (L2)**, Bridge, NIC | Truyền dữ liệu tin cậy giữa hai nút lân cận trên cùng một liên kết vật lý (Node-to-Node); đánh địa chỉ vật lý MAC, kiểm soát lỗi (CRC) |
| **Tầng 1** | **물리 계층 / (Physical)** | **Bit** (0 và 1) | **Repeater**, Dummy Hub | Chuyển đổi dữ liệu nhị phân thành tín hiệu điện, quang hoặc sóng vô tuyến; đặc tả cơ học, điện học và thủ tục cáp kết nối |

#### 2. Phân nhóm 3 tầng dưới vs 4 tầng trên
- **3 tầng dưới (하위 계층 / Media Layers - Tầng 1, 2, 3)**:
  - Tập trung vào việc **truyền dẫn dữ liệu vật lý và định tuyến mạng** qua các trạm trung gian (Point-to-Point, Hop-by-Hop).
  - Hoạt động chủ yếu bởi phần cứng mạng chuyên dụng (Cáp, Card mạng NIC, Switch, Router).
- **4 tầng trên (상위 계층 / Host Layers - Tầng 4, 5, 6, 7)**:
  - Tập trung vào việc **xử lý dữ liệu đầu cuối giữa hai máy chủ ứng dụng** (End-to-End).
  - Được cài đặt và thực thi chủ yếu thông qua phần mềm trong hệ điều hành máy trạm (TCP/IP Stack, Socket, Thư viện ứng dụng).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Quá trình đóng gói (Encapsulation) và Mở gói (Decapsulation)
```
[Bên gửi: Encapsulation - Đi từ trên xuống]
  [Data] ───────────────► Tầng 7, 6, 5 (Application, Presentation, Session)
  [Header4 | Data] ─────► Tầng 4 (Transport) -> Tạo Segment
  [Header3 | H4 | Data] ► Tầng 3 (Network)   -> Tạo Packet
  [H2 | H3 | H4 | Data | Trailer2] ──► Tầng 2 (Data Link) -> Tạo Frame (chứa FCS kiểm lỗi)
  01101001011010101... ─► Tầng 1 (Physical)  -> Tín hiệu Bit trên đường truyền cáp
                               │
                               ▼
[Bên nhận: Decapsulation - Đi từ dưới lên]
  Bóc tách ngược lại từ Tầng 1 lên Tầng 7, trả về bản rõ Data ban đầu cho ứng dụng.
```

#### 2. Điểm kiểm tra đồng bộ trong Tầng Session (Synchronization Points)
- **Điểm đồng bộ chính (Major Synchronization Point)**: Đánh dấu hoàn tất một giai đoạn truyền tải dữ liệu lớn, bắt buộc hai bên phải gửi thông điệp xác nhận rõ ràng (ACK) trước khi tiếp tục. Khi có sự cố, hệ thống phục hồi từ điểm này.
- **Điểm đồng bộ phụ (Minor Synchronization Point)**: Đánh dấu các mốc dữ liệu nhỏ trong quá trình truyền, không bắt buộc phải phản hồi xác nhận ngay lập tức.

---

### 복습 체크리스트
- [ ] Kể tên đầy đủ 7 tầng của mô hình OSI theo đúng thứ tự từ tầng 1 đến tầng 7?
- [ ] Đơn vị dữ liệu (PDU) tại Tầng 2, Tầng 3 và Tầng 4 lần lượt có tên gọi là gì?
- [ ] Chức năng nén dữ liệu và mã hóa bảo mật (Encryption) được thực hiện tại tầng nào trong mô hình OSI?
- [ ] Thiết bị Router và Switch L2 hoạt động tại các tầng nào tương ứng trong mô hình OSI?
