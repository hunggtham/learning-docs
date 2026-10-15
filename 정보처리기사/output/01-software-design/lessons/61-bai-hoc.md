# 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc phân tầng máy chủ chuẩn trong môi trường doanh nghiệp: Máy chủ Web (`웹 서버`), Máy chủ ứng dụng (`WAS`), và Máy chủ cơ sở dữ liệu (`DB 서버`).
- Phân biệt bản chất kỹ thuật, ưu nhược điểm và phạm vi áp dụng của 3 công nghệ lưu trữ dữ liệu kinh điển: `DAS`, `NAS`, và `SAN`.
- Nhận diện các tiêu chuẩn kỹ thuật khi thiết lập hạ tầng mạng và cân nhắc giải pháp dự phòng chống gián đoạn dịch vụ.

## 핵심 키워드 (Từ khóa)
- 운영 환경 구축 (Xây dựng môi trường vận hành / Infrastructure)
- 웹 서버 vs WAS vs DB 서버 (Web Server vs WAS vs DB Server)
- DAS (Direct Attached Storage / 전용 케이블 직결)
- NAS (Network Attached Storage / Ethernet LAN / NFS, CIFS)
- SAN (Storage Area Network / 광채널 FC 스위치 / 블록 스토리지)
- 이중화 / 고가용성 (Redundancy / High Availability - HA)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([2. 스크럼 및 XP 추가 개념](60-bai-hoc.md)):** Sau khi hoàn tất phần quy trình phát triển Agile, bài này chuyển sang giai đoạn chuẩn bị hạ tầng môi trường vận hành thực tế cho hệ thống.
- **Tiếp nối sang bài sau ([6. 구조적 분석 도구](62-bai-hoc.md)):** Tổng hợp các công cụ phân tích cấu trúc phần mềm (DFD, DD, Mini-spec) phục vụ việc thiết kế logic.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ bảng phân biệt 3 loại Storage: DAS nối dây cáp trực tiếp vào máy chủ; NAS nối mạng LAN chia sẻ file; SAN dùng cáp quang FC tốc độ cao chuyên dụng khối block.
- Đọc TẦNG B để hiểu tại sao các hệ thống CSDL lớn của ngân hàng luôn chọn SAN thay vì NAS để đạt hiệu năng I/O tối đa.

---

## 4. 운영 환경 구축 고려사항 (Operation Environment Considerations)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân tầng kiến trúc máy chủ (서버 인프라 계층):**
  - `웹 서버 (Web Server - Máy chủ Web)`:
    - Tiếp nhận yêu cầu HTTP/HTTPS trực tiếp từ trình duyệt của người dùng; xử lý và trả về các **nội dung tĩnh (`정적 콘텐츠 - HTML, CSS, JavaScript, hình ảnh`)**; đóng vai trò Reverse Proxy và cân bằng tải (Load Balancer).
    - Tiêu biểu: **Apache HTTP Server, Nginx, Microsoft IIS**.
  - `웹 애플리케이션 서버 (WAS - Web Application Server)`:
    - Tiếp nhận các yêu cầu nghiệp vụ phức tạp từ Web Server; thực thi các mã nguồn logic nghiệp vụ, quản lý phiên làm việc (Session) và tạo ra **nội dung động (`동적 콘텐츠`)** kết nối với DBMS.
    - Tiêu biểu: **Tomcat, WebLogic, JEUS, JBoss**.
  - `데이터베이스 서버 (DB Server)`:
    - Lưu trữ, quản lý và xử lý dữ liệu giao dịch bền vững.
    - Tiêu biểu: **Oracle, MySQL, PostgreSQL, MS-SQL**.
- **2. So sánh 3 công nghệ lưu trữ dữ liệu (스토리지 시스템):**
  - **DAS (Direct Attached Storage - Lưu trữ gắn trực tiếp):**
    - Thiết bị lưu trữ (ổ đĩa cứng) được **kết nối trực tiếp vào máy chủ thông qua cáp chuyên dụng riêng biệt (`전용 케이블로 직접 연결 - SATA, SAS, SCSI`)**.
    - *Ưu điểm:* Tốc độ truyền tải nhanh, dễ cài đặt, chi phí đầu tư ban đầu thấp.
    - *Nhược điểm:* **Không thể chia sẻ dữ liệu trực tiếp cho các máy chủ khác**; khả năng mở rộng dung lượng rất hạn chế.
  - **NAS (Network Attached Storage - Lưu trữ gắn mạng):**
    - Thiết bị lưu trữ độc lập được **kết nối trực tiếp vào hạ tầng mạng máy tính LAN thông qua cáp mạng Ethernet**; các máy chủ truy cập và chia sẻ dữ liệu tệp tin qua các giao thức chia sẻ file như **NFS (cho Linux/Unix) hoặc CIFS/SMB (cho Windows)**.
    - *Ưu điểm:* Dễ dàng chia sẻ dữ liệu cho nhiều máy chủ khác nhau, cài đặt thuận tiện.
    - *Nhược điểm:* **Bị giới hạn tốc độ bởi băng thông của mạng LAN**; lưu lượng truy xuất file cạnh tranh với lưu lượng mạng thông thường, dễ gây nghẽn mạng.
  - **SAN (Storage Area Network - Mạng vùng lưu trữ chuyên dụng):**
    - Xây dựng một **mạng lưới lưu trữ chuyên dụng tốc độ cực cao độc lập với mạng LAN**, kết nối các mảng đĩa lưu trữ (Storage Array) với các máy chủ thông qua **Cáp quang và Thiết bị chuyển mạch kênh sợi quang (`광채널 - Fibre Channel / FC Switch`)** hoặc iSCSI ở cấp độ khối (**Block-level**).
    - *Ưu điểm:* Tốc độ truyền dữ liệu và thông lượng cực nhanh, độ trễ cực thấp, độ tin cậy và khả năng mở rộng dung lượng gần như vô hạn.
    - *Nhược điểm:* Chi phí thiết bị quang và bản quyền phần mềm rất đắt đỏ, đòi hỏi kỹ sư chuyên môn cao để vận hành.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Công nghệ lưu trữ nào kết nối trực tiếp vào máy chủ qua cáp chuyên dụng và không chia sẻ được cho máy khác?"* -> **DAS (Direct Attached Storage)**.
  - **Bẫy 2:** *"NAS chia sẻ dữ liệu ở cấp độ nào và qua giao thức gì?"* -> **Cấp độ tệp tin (File-level), qua giao thức NFS hoặc CIFS/SMB**.
  - **Bẫy 3:** *"SAN kết nối các máy chủ với khối đĩa lưu trữ bằng công nghệ gì?"* -> **Kênh sợi quang (Fibre Channel - 광채널) hoặc FC Switch**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Web phục vụ trang tĩnh, WAS chạy logic động, DB lưu dữ liệu; DAS cắm cáp trực tiếp, NAS cắm dây mạng LAN chia sẻ file, SAN chạy cáp quang khối đĩa chuyên dụng tốc độ cao".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ma trận lựa chọn công nghệ lưu trữ theo bài toán thực tế:**
  - Máy tính cá nhân hoặc máy chủ file nhỏ cho phòng kế toán 5 người: Dùng **DAS** hoặc **NAS**.
  - Hệ thống máy chủ chia sẻ tài liệu văn phòng cho 500 nhân viên trong công ty: Dùng **NAS** vì giao thức SMB/CIFS chia sẻ thư mục mạng rất tiện lợi.
  - Cụm máy chủ cơ sở dữ liệu Oracle RAC phục vụ hàng triệu giao dịch thẻ tín dụng mỗi ngày: Bắt buộc dùng **SAN** vì yêu cầu I/O đĩa cứng ở cấp độ khối cực lớn và không thể chịu đựng độ trễ của mạng LAN.

### 복습 체크리스트
- [ ] Phân biệt được vai trò của Web Server (tĩnh) và WAS (động).
- [ ] Định nghĩa và chỉ ra ưu nhược điểm của DAS (nối cáp trực tiếp).
- [ ] Định nghĩa NAS và nhớ 2 giao thức chia sẻ file: NFS (Linux) và CIFS/SMB (Windows).
- [ ] Nhớ SAN sử dụng cáp quang Fibre Channel (FC) và thao tác ở cấp độ khối (Block-level).
