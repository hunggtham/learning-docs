# 정보 보안 및 하드웨어 신기술 (Security & HW Tech)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và cơ chế hoạt động của Secure OS cùng 4 phương pháp phân ly tài nguyên bảo mật (암호적, 논리적, 시간적, 물리적 분리).
- Hiểu rõ các giải pháp tính sẵn sàng cao (High Availability - HA) và các mô hình vận hành máy chủ dự phòng.
- Phân biệt cấu trúc các cấp độ mảng đĩa độc lập dự phòng (RAID 0, 1, 5, 6) về tốc độ, chi phí và khả năng chịu lỗi.
- Nắm bắt công nghệ bảo mật phần cứng ARM TrustZone và mô hình dịch vụ đám mây BaaS (Blockchain as a Service).

## 핵심 키워드 (Từ khóa)
- **Secure OS**: 보안 커널 (Security Kernel), MAC (Mandatory Access Control), 4 phương pháp phân ly tài nguyên (암호적, 논리적, 시간적, 물리적 분리).
- **고가용성 (HA - High Availability)**: Hot Standby (chờ nóng), Mutual Takeover (tiếp quản lẫn nhau), Concurrent (đồng thời).
- **RAID**: RAID 0 (Striping - không dự phòng), RAID 1 (Mirroring - bản sao 100%), RAID 5 (Parity phân tán), RAID 6 (Dual Parity).
- **신기술 (New Tech)**: TrustZone (ARM phân tách Normal World và Secure World), BaaS (Blockchain as a Service), 허니팟 (Honeypot).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [26-bai-hoc.md](26-bai-hoc.md) (정보 보안 일반 및 시스템 보안 - Secure OS và CIA Triad).
- Liên kết với [10-bai-hoc.md](10-bai-hoc.md) (SW 품질 및 프로세스 표준 - Độ tin cậy hệ thống).
- Liên kết với [36-bai-hoc.md](36-bai-hoc.md) (접근 통제 모델 - Chi tiết mô hình DAC, MAC, RBAC).

## 읽는 방법 (Cách đọc)
- Nhớ nhanh 4 cơ chế cô lập của Secure OS: **Vật lý** (dùng máy riêng), **Thời gian** (chia lượt chạy khác thời điểm), **Logic** (OS phân quyền ảo hóa), **Mã hóa** (dữ liệu nằm chung nhưng khóa riêng).
- Đi thi chú ý số ổ đĩa tối thiểu cho RAID: RAID 1 cần ít nhất 2 ổ, RAID 5 cần ít nhất 3 ổ, RAID 6 cần ít nhất 4 ổ.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Hệ điều hành bảo mật (Secure OS)
- **Định nghĩa**: Hệ điều hành được cấy ghép thêm nhân bảo mật (Security Kernel) nhằm thực thi các chính sách bảo mật nghiêm ngặt như kiểm soát truy cập bắt buộc (MAC), nhận dạng người dùng và ngăn chặn tấn công leo thang đặc quyền.
- **4 phương pháp phân ly bảo vệ tài nguyên (보호 분리 방법)**:
  - **물리적 분리 (Phân ly vật lý)**: Các tiến trình chạy trên các thiết bị phần cứng, bộ xử lý hoặc máy chủ hoàn toàn độc lập.
  - **시간적 분리 (Phân ly thời gian)**: Các tiến trình có cấp độ an ninh khác nhau được xếp lịch thực thi tại các khung thời gian riêng biệt, không chạy đồng thời.
  - **논리적 분리 (Phân ly logic)**: Các tiến trình chia sẻ chung tài nguyên phần cứng nhưng được phân tách không gian địa chỉ ảo và phạm vi truy cập bởi hệ điều hành.
  - **암호적 분리 (Phân ly mật mã)**: Các tệp tin hoặc luồng dữ liệu được mã hóa bằng các khóa mật mã khác nhau; người không có khóa giải mã phù hợp sẽ không thể đọc được nội dung dù nằm chung trên một ổ cứng.

#### 2. Tính sẵn sàng cao (High Availability - HA)
- **Khái niệm**: Hệ thống được thiết kế với các thành phần dự phòng (Redundancy) để duy trì hoạt động liên tục không gián đoạn, ngay cả khi một máy chủ hoặc linh kiện bị sự cố (Failover tức thì).
- **3 cấu hình triển khai HA phổ biến**:
  - **Hot Standby (Active - Standby)**: Máy chủ chính (Active) xử lý toàn bộ tải công việc, máy chủ phụ (Standby) ở trạng thái chờ sẵn sàng. Khi máy chính gặp lỗi, máy phụ tiếp quản ngay lập tức.
  - **Mutual Takeover (Active - Active)**: Cả hai máy chủ đều hoạt động đồng thời và chia sẻ tải. Khi một máy bị hỏng, máy còn lại sẽ gánh toàn bộ tải của cả hai hệ thống.
  - **Concurrent Processing**: Nhiều máy chủ cùng xử lý song song một cơ sở dữ liệu dùng chung (Shared Storage / Clustered DB).

#### 3. Công nghệ lưu trữ RAID
| Cấp độ RAID | Kỹ thuật cốt lõi | Khả năng chịu lỗi | Số ổ đĩa tối thiểu / Hiệu suất lưu trữ |
| :--- | :--- | :--- | :--- |
| **RAID 0** | **Striping (Ghi xen kẽ)**: Dữ liệu được chia nhỏ và ghi đồng thời lên nhiều ổ | **Không có** (1 ổ hỏng là mất toàn bộ dữ liệu) | Tối thiểu 2 ổ / Dung lượng 100% (Tốc độ đọc/ghi cao nhất) |
| **RAID 1** | **Mirroring (Ghi nhân bản)**: Sao chép y hệt dữ liệu sang ổ đĩa thứ hai | **Có** (Chịu được hỏng 1 ổ trong cặp) | Tối thiểu 2 ổ / Dung lượng $50\%$ (Chi phí ổ đĩa cao) |
| **RAID 5** | **Distributed Parity (Parity phân tán)**: Dữ liệu và mã kiểm tra Parity ghi luân phiên trên tất cả các ổ | **Có** (Chịu được hỏng tối đa **1 ổ đĩa**) | Tối thiểu **3 ổ** / Dung lượng $(N-1)/N$ |
| **RAID 6** | **Dual Distributed Parity**: Tính toán 2 khối Parity độc lập phân tán trên các ổ | **Có** (Chịu được hỏng tối đa **2 ổ đĩa** cùng lúc) | Tối thiểu **4 ổ** / Dung lượng $(N-2)/N$ |

#### 4. Công nghệ phần cứng mới và Đám mây
- **ARM TrustZone**: Công nghệ bảo mật tích hợp sâu vào kiến trúc vi xử lý của hãng ARM. CPU được chia thành hai phân vùng tách biệt:
  - **Normal World (Non-secure World)**: Chạy hệ điều hành thông thường (Android, Linux) và các ứng dụng hàng ngày.
  - **Secure World**: Môi trường thực thi tin cậy (TEE - Trusted Execution Environment) chạy một hệ điều hành bảo mật nhỏ, lưu trữ khóa mật mã, xử lý xác thực sinh trắc học và thanh toán số.
- **BaaS (Blockchain as a Service)**: Mô hình điện toán đám mây cho phép các doanh nghiệp thuê môi trường máy chủ đã cấu hình sẵn để xây dựng, lưu trữ và vận hành các ứng dụng blockchain của riêng mình mà không cần tự đầu tư phần cứng phức tạp.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Kiến trúc phân chia thế giới của ARM TrustZone
```
┌──────────────────────────────────────┬──────────────────────────────────────┐
│       Normal World (Không an toàn)   │        Secure World (Tin cậy)        │
│  - Hệ điều hành (Android, iOS)       │  - Secure OS / TEE                   │
│  - Ứng dụng người dùng (App, Game)   │  - Quản lý khóa riêng tư (Keystore)  │
│  - Driver phần cứng thông thường     │  - Xử lý quét vân tay / Face ID      │
└──────────────────┬───────────────────┴──────────────────┬───────────────────┘
                   │                                      │
                   └──────────────► [SMC (Secure Monitor Call)] ◄─────────────┘
                                  (Cầu nối chuyển mạch an toàn phần cứng)
```

#### 2. Kỹ thuật tính dung lượng RAID thực tế
- Giả sử có 4 ổ đĩa cứng, mỗi ổ dung lượng $2\text{ TB}$ ($N = 4$):
  - **RAID 0**: $4 \times 2 = 8\text{ TB}$ (Tốc độ tối đa, không an toàn).
  - **RAID 1**: $2\text{ TB}$ (Chỉ lưu được một nửa dung lượng tổng thể nếu dùng cơ chế cặp).
  - **RAID 5**: $(4 - 1) \times 2 = 6\text{ TB}$ (Mất 1 ổ làm Parity, hỏng 1 ổ vẫn khôi phục được).
  - **RAID 6**: $(4 - 2) \times 2 = 4\text{ TB}$ (Mất 2 ổ làm Parity kép, hỏng 2 ổ bất kỳ vẫn an toàn).

---

### 복습 체크리스트
- [ ] Bốn phương pháp phân ly bảo mật trong Secure OS (Vật lý, Thời gian, Logic, Mật mã) hoạt động như thế nào?
- [ ] Số lượng ổ đĩa tối thiểu cần thiết để xây dựng mảng đĩa RAID 5 và RAID 6 lần lượt là bao nhiêu?
- [ ] Tại sao RAID 0 không có khả năng chịu lỗi (Fault Tolerance)?
- [ ] Trong kiến trúc ARM TrustZone, việc phân chia Normal World và Secure World mang lại lợi ích bảo mật gì?
