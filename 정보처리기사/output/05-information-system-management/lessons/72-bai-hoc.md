# 침입 탐지 시스템 (IDS; Intrusion Detection System)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và nguyên lý giám sát an ninh thời gian thực của Hệ thống phát hiện xâm nhập (IDS - Intrusion Detection System).
- Phân biệt toàn diện hai cơ chế phát hiện xâm nhập cốt lõi: Phát hiện lạm dụng / Chữ ký mẫu (오용 탐지 - Misuse Detection) và Phát hiện bất thường / Hành vi (이상 탐지 - Anomaly Detection).
- Phân biệt phạm vi triển khai của HIDS (trên máy chủ đơn lẻ) và NIDS (trên toàn mạng qua cổng Mirroring).
- Phân biệt sự khác nhau giữa Hệ thống phát hiện xâm nhập (IDS) và Hệ thống ngăn ngừa xâm nhập (IPS).

## 핵심 키워드 (Từ khóa)
- **IDS (침입 탐지 시스템)**: Giám sát và phát hiện xâm nhập trái phép thời gian thực.
- **오용 탐지 (Misuse/Signature-based)**: So khớp mẫu đã biết, tỷ lệ báo động giả thấp, không phát hiện được Zero-Day.
- **이상 탐지 (Anomaly/Behavior-based)**: Phát hiện độ lệch hành vi so với mức chuẩn, phát hiện được Zero-Day, tỷ lệ báo động giả cao.
- **HIDS vs NIDS**: HIDS (Host-based - theo dõi file log máy trạm) vs NIDS (Network-based - phân tích gói tin mạng qua Snort).
- **IDS vs IPS**: IDS (Passive - chỉ cảnh báo) vs IPS (Inline / Active - chủ động chặn gói tin).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [22-bai-hoc.md](22-bai-hoc.md) (Tường lửa Firewall và thiết bị bảo mật mạng).
- Liên kết với [26-bai-hoc.md](26-bai-hoc.md) (Hệ thống bảo vệ hệ điều hành Secure OS).
- Liên kết với [73-bai-hoc.md](73-bai-hoc.md) (Hệ thống tệp log trong Linux phục vụ HIDS).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh hai cơ chế trong đề thi:
  - "Dựa trên mẫu tấn công đã biết (Signature), độ chính xác cao nhưng không bắt được tấn công mới" $\rightarrow$ Chọn **오용 탐지 (Misuse Detection)**.
  - "Dựa trên hành vi trung bình của người dùng, bắt được tấn công Zero-day nhưng dễ báo động nhầm" $\rightarrow$ Chọn **이상 탐지 (Anomaly Detection)**.
  - "Công cụ Snort là đại diện tiêu biểu của loại nào?" $\rightarrow$ **NIDS (Network-based IDS)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 2 cơ chế phát hiện xâm nhập: Misuse vs Anomaly
| Tiêu chí kỹ thuật | 오용 탐지 (Misuse / Signature-based) | 이상 탐지 (Anomaly / Behavior-based) |
| :--- | :--- | :--- |
| **Nguyên lý phát hiện** | So khớp lưu lượng với **cơ sở dữ liệu mẫu chữ ký tấn công (Signature)** đã được định nghĩa sẵn | Thiết lập hồ sơ hành vi bình thường chuẩn (Baseline), phát hiện **độ lệch thống kê bất thường** |
| **Khả năng bắt tấn công mới** | **Không thể phát hiện** các cuộc tấn công chưa từng biết (Zero-Day Attacks) hoặc mã độc biến thể mới | **Có khả năng phát hiện** các mối đe dọa mới và tấn công chưa biết (Zero-Day) |
| **Tỷ lệ báo động giả (False Positive)** | **Rất thấp** (khi đã khớp mẫu chữ ký thì độ tin cậy gần như tuyệt đối) | **Khá cao** (khi người dùng hợp lệ có hành vi đột biến ngoài thói quen thông thường) |
| **Cơ sở dữ liệu hỗ trợ** | Cần cập nhật liên tục các tập luật chữ ký mẫu mới từ các tổ chức bảo mật | Cần thời gian học (Training phase) để xây dựng mô hình hồ sơ chuẩn xác thực |

#### 2. Phân loại theo vị trí triển khai: HIDS vs NIDS
- **HIDS (Host-Based IDS - Phát hiện xâm nhập dựa trên máy chủ)**:
  - Cài đặt trực tiếp dưới dạng phần mềm (Agent) trên từng máy chủ hoặc máy trạm quan trọng.
  - Giám sát các tệp nhật ký hệ thống (System logs), kiểm tra tính toàn vẹn của các tệp thực thi cốt lõi (File Integrity Monitoring), theo dõi các tiến trình đang chạy và các lời gọi hệ thống (System Calls).
  - *Công cụ tiêu biểu*: OSSEC, Tripwire, AIDE.
- **NIDS (Network-Based IDS - Phát hiện xâm nhập dựa trên mạng)**:
  - Lắp đặt tại các điểm nút giao thông huyết mạch của mạng (thường nhận dữ liệu từ cổng Port Mirroring / SPAN của Switch).
  - Hoạt động ở chế độ Promiscuous Mode để bắt và phân tích nội dung gói tin (Packet Payload) của toàn bộ lưu lượng chạy trên đường truyền mạng.
  - *Công cụ tiêu biểu*: **Snort**, Suricata, Bro/Zeek.

#### 3. Bảng đối chiếu IDS và IPS
| Đặc tính | IDS (Intrusion Detection System) | IPS (Intrusion Prevention System) |
| :--- | :--- | :--- |
| **Phương thức đấu nối** | **Nối song song (Out-of-path / Sniffer Mode)** thông qua cổng TAP hoặc Port Mirroring | **Nối tiếp trực tiếp (Inline Mode)**, gói tin bắt buộc phải đi xuyên qua thiết bị IPS |
| **Ảnh hưởng mạng** | Không làm chậm trễ đường truyền khi thiết bị gặp sự cố (Fail-Open) | Có thể tạo độ trễ gói tin (Latency); thiết bị lỗi có thể làm gián đoạn đường truyền |
| **Hành động phản ứng** | **Bị động (Passive)**: Chỉ ghi nhật ký sự kiện (Logging) và gửi cảnh báo (Alert) cho quản trị viên | **Chủ động (Active)**: Ngắt kết nối mạng ngay tức thì, thả bỏ gói tin độc hại (Drop packet) |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ mô hình kiến trúc kết nối IDS và IPS
```
                [Internet]
                    │
                    ▼
               [Firewall]
                    │
                    ▼ (Chế độ Inline: Đi xuyên qua)
             ┌─────────────┐
             │     IPS     │ ──► [Chặn & Drop gói tin độc hại ngay lập tức]
             └──────┬──────┘
                    │
                    ▼
           [Switch phân phối] ──(Port Mirroring / Sao chép luồng)──► [IDS (Chỉ phân tích & Cảnh báo)]
                    │
     ┌──────────────┴──────────────┐
     ▼                             ▼
[Web Server]                  [DB Server]
 (Cài HIDS)                    (Cài HIDS)
```

---

### 복습 체크리스트
- [ ] Sự khác biệt cốt lõi giữa hai phương pháp 오용 탐지 (Signature) và 이상 탐지 (Anomaly) là gì?
- [ ] Tại sao phương pháp 이상 탐지 lại có khả năng phát hiện được các cuộc tấn công Zero-day?
- [ ] Phân biệt vị trí lắp đặt và đối tượng giám sát của HIDS và NIDS?
- [ ] Điểm khác biệt then chốt trong cách kết nối và hành động giữa IDS và IPS là gì?
