# 스토리지 시스템 (Các Kiến trúc Hệ thống Lưu trữ: DAS, NAS, SAN)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và phân biệt rõ 3 kiến trúc lưu trữ dữ liệu doanh nghiệp cốt lõi: DAS (Direct Attached Storage), NAS (Network Attached Storage), và SAN (Storage Area Network).
- Phân biệt cơ chế truy xuất dữ liệu cấp độ tệp (File-Level) của NAS và cấp độ khối (Block-Level) của DAS và SAN.
- Hiểu rõ các giao thức kết nối tiêu biểu: NFS, CIFS/SMB cho NAS; Fibre Channel (FC) và iSCSI cho SAN.
- Đánh giá ưu nhược điểm về hiệu năng, chi phí và khả năng mở rộng của từng kiến trúc lưu trữ.

## 핵심 키워드 (Từ khóa)
- **DAS (Direct Attached Storage)**: Cắm trực tiếp bằng cáp chuyên dụng (SCSI, SAS), tốc độ cao, khó chia sẻ giữa nhiều server.
- **NAS (Network Attached Storage)**: Kết nối qua mạng LAN Ethernet thông thường, truy xuất cấp độ tệp (File-Level), giao thức NFS, CIFS/SMB.
- **SAN (Storage Area Network)**: Mạng cáp quang chuyên dụng tốc độ cao (FC-SAN, IP-SAN/iSCSI), truy xuất cấp độ khối (Block-Level).
- **Mẹo nhớ**: **DAS** = Direct (Cắm trực tiếp), **NAS** = Network LAN (Qua mạng chung), **SAN** = Storage Area Network (Mạng quang riêng biệt).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [18-bai-hoc.md](18-bai-hoc.md) (Hạ tầng lưu trữ SDS và SDDC).
- Liên kết với [28-bai-hoc.md](28-bai-hoc.md) (Công nghệ mảng đĩa RAID).
- Liên kết với [66-bai-hoc.md](66-bai-hoc.md) (Mô hình mạng OSI 7 tầng).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh dạng câu hỏi thi:
  - "Kết nối trực tiếp ổ cứng với máy chủ bằng cáp SCSI hoặc SAS" $\rightarrow$ Chọn **DAS**.
  - "Chia sẻ tệp qua mạng LAN bằng giao thức NFS hoặc CIFS" $\rightarrow$ Chọn **NAS**.
  - "Xây dựng một mạng cáp quang riêng biệt tốc độ cao chuyên dụng để truyền tải dữ liệu cấp độ khối (Block-level)" $\rightarrow$ Chọn **SAN**.
  - "Giao thức iSCSI kết hợp giữa giao thức nào?" $\rightarrow$ Giao thức lệnh SCSI chạy trên nền mạng TCP/IP.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 3 Kiến trúc Lưu trữ Doanh nghiệp
| Tiêu chí so sánh | DAS (Direct Attached Storage) | NAS (Network Attached Storage) | SAN (Storage Area Network) |
| :--- | :--- | :--- | :--- |
| **Bản chất kết nối** | Kết nối trực tiếp giữa máy chủ và ổ cứng bằng cáp vật lý chuyên dụng | Kết nối thiết bị lưu trữ vào mạng cục bộ **LAN (Ethernet)** có sẵn | Xây dựng một **mạng chuyên dụng độc lập** hoàn toàn kết nối Server và Storage |
| **Cấp độ truy xuất** | **Cấp độ khối (Block-Level)** | **Cấp độ tệp (File-Level)** | **Cấp độ khối (Block-Level)** |
| **Giao thức kết nối** | SAS, SATA, SCSI, Fibre Channel cáp | **NFS** (Linux/UNIX), **CIFS / SMB** (Windows) | **Fibre Channel (FC)**, **iSCSI** (IP-SAN) |
| **Tốc độ & Độ trễ** | Rất nhanh, độ trễ cực thấp | Bị ảnh hưởng bởi lưu lượng mạng LAN chung | Siêu nhanh, băng thông cực lớn, độ trễ tối thiểu |
| **Khả năng chia sẻ** | Khó khăn (chỉ phục vụ máy chủ được cắm nối) | **Rất dễ dàng** cho nhiều máy tính cùng truy cập | Rất cao (nhiều máy chủ cùng truy cập vào phân vùng chung) |
| **Chi phí đầu tư** | Thấp nhất | Trung bình | **Rất cao** (cần thiết bị Switch quang và Card HBA riêng) |

#### 2. Chi tiết hai biến thể của kiến trúc SAN
- **FC-SAN (Fibre Channel SAN)**:
  - Sử dụng toàn bộ hạ tầng cáp quang (Optical Fiber Cables), thiết bị chuyển mạch quang chuyên dụng (**FC Switch**) và card giao tiếp quang (**HBA - Host Bus Adapter**) gắn trên máy chủ.
  - *Đặc điểm*: Tốc độ truyền tải dữ liệu cực cao (16Gbps, 32Gbps), độ trễ gần như bằng 0; nhược điểm là chi phí đắt đỏ và yêu cầu kỹ sư có chuyên môn cao để quản trị.
- **IP-SAN (Internet Protocol SAN / iSCSI)**:
  - Đóng gói các lệnh lưu trữ SCSI truyền thống vào bên trong các gói tin giao vận **TCP/IP** thông thường (giao thức **iSCSI**).
  - *Đặc điểm*: Tận dụng được hạ tầng cáp mạng Gigabit Ethernet và Switch mạng sẵn có, giúp tiết kiệm chi phí lớn so với FC-SAN.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ kiến trúc so sánh vị trí kết nối của DAS, NAS và SAN
```
[Mô hình DAS]       [Mô hình NAS]                    [Mô hình SAN]
  [Server]            [Server]   [Client]              [Server A]   [Server B]
     │                   │          │                      │            │
  (Cáp SCSI)             └────┬─────┘                      └───┬────┬───┘
     │                        │                                │    │
     ▼                        ▼ (Mạng LAN Ethernet)            ▼    ▼ (Mạng quang FC SAN)
 [Storage]              [Thiết bị NAS]                       [FC Switch Quang]
                                                                    │
                                                                    ▼
                                                            [Hệ thống SAN Storage]
```

#### 2. Phân biệt File-Level Access vs Block-Level Access
- **File-Level Access (NAS)**: Thiết bị lưu trữ tự quản lý hệ điều hành và hệ thống tệp (NTFS, ext4). Máy khách gửi yêu cầu đọc tệp tin (ví dụ: "Đọc file `baocao.docx`"), NAS tìm tệp và trả về luồng dữ liệu tệp tin.
- **Block-Level Access (SAN, DAS)**: Thiết bị lưu trữ chỉ xem dữ liệu là các khối bit thô (LBA - Logical Block Addressing) được đánh số thứ tự từ $0, 1, 2\dots$ Hệ điều hành trên máy chủ tự quyết định định dạng hệ thống tệp và cấu trúc thư mục, mang lại hiệu năng cao vượt trội cho các ứng dụng cơ sở dữ liệu lớn (Oracle, SQL Server).

---

### 복습 체크리스트
- [ ] Phân biệt sự khác nhau cơ bản giữa 3 hình thức lưu trữ DAS, NAS và SAN?
- [ ] Thiết bị lưu trữ NAS thực hiện việc truy xuất dữ liệu ở cấp độ tệp (File-Level) hay cấp độ khối (Block-Level)?
- [ ] Giao thức NFS và CIFS/SMB thường được sử dụng trong kiến trúc lưu trữ nào?
- [ ] Công nghệ IP-SAN sử dụng giao thức nào để truyền tải các lệnh SCSI trên nền tảng mạng TCP/IP?
