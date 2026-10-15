# 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và phân loại 4 kiến trúc thiết bị lưu trữ dữ liệu trong hệ thống doanh nghiệp: **DAS (`Direct Attached Storage`)**, **NAS (`Network Attached Storage`)**, **SAN (`Storage Area Network`)**, và **SDS (`Software-Defined Storage`)**.
- Phân biệt rõ phương thức truy cập và môi trường truyền dẫn: DAS (cáp chuyên dụng trực tiếp), NAS (mạng Ethernet, truy cập cấp độ tệp File-level), SAN (mạng cáp quang FC, truy cập cấp độ khối Block-level).
- Nhớ rõ bảng so sánh ưu nhược điểm giữa DAS, NAS, SAN trong các câu hỏi trắc nghiệm Kỹ sư xử lý thông tin Hàn Quốc.
- Tổng hợp mối liên kết giữa kiến trúc lưu trữ phần cứng với Cơ sở dữ liệu phân tán (`분산 데이터베이스`).

## 핵심 키워드 (Từ khóa)
- 스토리지 (Lưu trữ / Storage)
- DAS (Direct Attached Storage / 전용 케이블 직접 연결)
- NAS (Network Attached Storage / 이더넷 파일 공유)
- SAN (Storage Area Network / 광 채널 전용 네트워크)
- SDS (Software-Defined Storage / 스토리지 가상화)
- 광 채널 스위치 (Fibre Channel Switch / FC 스위치)
- 파일 레벨 접근 (Truy cập cấp độ tệp) / 블록 레벨 접근 (Truy cập cấp độ khối)
- 분산 데이터베이스 (Cơ sở dữ liệu phân tán)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([03-bai-hoc.md](03-bai-hoc.md), [34-bai-hoc.md](34-bai-hoc.md), [36-bai-hoc.md](36-bai-hoc.md)):** Lựa chọn kiến trúc lưu trữ vật lý (DAS, NAS, SAN) là quyết định nền tảng trong bước Thiết kế vật lý nhằm đảm bảo thông lượng I/O cho các nút CSDL phân tán.
- **Tiếp nối sang các bài sau ([38-bai-hoc.md](38-bai-hoc.md), [39-bai-hoc.md](39-bai-hoc.md)):** Trên nền tảng hệ thống lưu trữ lớn, kỹ sư áp dụng kỹ thuật Phân vùng bảng (`파티셔닝`) và Mã hóa dữ liệu (`암호화`) để tối ưu hóa hiệu năng và bảo vệ bí mật thông tin.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng tam giác so sánh **DAS - NAS - SAN** ở TẦNG A:
  - **DAS:** Cắm dây trực tiếp như ổ cứng ngoài $\rightarrow$ Nhanh, rẻ, nhưng **không chia sẻ được cho máy chủ khác**.
  - **NAS:** Cắm vào mạng LAN thông thường $\rightarrow$ **Chia sẻ tệp dễ dàng (File-level)**, nhưng dễ nghẽn băng thông mạng.
  - **SAN:** Dựng mạng cáp quang riêng biệt (`광 채널 / FC`) $\rightarrow$ **Tốc độ cực nhanh (Block-level)**, xử lý lượng giao dịch khổng lồ, nhưng **chi phí rất đắt**.

---

## 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 3 kiến trúc Lưu trữ kinh điển (스토리지 3대 방식 비교):**
  | Kiến trúc | Thuật ngữ tiếng Hàn & Anh | Phương thức kết nối & Đặc trưng | Ưu điểm nổi bật | Nhược điểm & Hạn chế |
  |---|---|---|---|---|
  | **DAS** | `Direct Attached Storage` (Lưu trữ gắn trực tiếp) | Máy chủ kết nối trực tiếp với thiết bị lưu trữ thông qua **cáp chuyên dụng riêng biệt** (SCSI, SATA, SAS) giống như cắm ổ cứng ngoài. | - Tốc độ truy xuất nhanh. ; - Dễ dàng cài đặt và quản trị. ; - Chi phí đầu tư ban đầu thấp nhất. | - **Không thể chia sẻ tệp cho máy chủ khác** truy cập trực tiếp. ; - Khả năng mở rộng và độ linh hoạt rất kém. |
  | **NAS** | `Network Attached Storage` (Lưu trữ gắn qua mạng) | Máy chủ kết nối với hệ thống lưu trữ thông qua **mạng truyền thông cục bộ (Ethernet)**; thiết bị NAS có sẵn hệ điều hành riêng để quản lý tệp (**File-level** qua NFS, CIFS/SMB). | - Dễ dàng chia sẻ tệp tin giữa nhiều máy chủ khác nhau. ; - Khả năng mở rộng và linh hoạt cao hơn nhiều so với DAS. | - Tốc độ truy xuất phụ thuộc vào băng thông mạng. ; - **Khi lượng truy cập tăng vọt sẽ xảy ra hiện tượng nghẽn mạng (성능 저하)**. |
  | **SAN** | `Storage Area Network` (Mạng vùng lưu trữ) | Kết hợp ưu điểm tốc độ của DAS và khả năng chia sẻ của NAS; tạo một **mạng chuyên dụng độc lập** kết nối máy chủ và ổ đĩa bằng **Switch quang (FC - Fibre Channel)** và cáp quang (**Block-level**). | - Tốc độ truyền tải dữ liệu cực nhanh. ; - Rất tối ưu cho các hệ thống xử lý giao dịch cao (High Transaction). ; - Tính sẵn sàng và mở rộng tuyệt vời. | - Chi phí đầu tư thiết bị và triển khai ban đầu **rất đắt đỏ**. ; - Đòi hỏi chuyên gia quản trị mạng quang phức tạp. |

- **2. Khái niệm SDS (Software-Defined Storage - Lưu trữ định nghĩa bằng phần mềm):**
  - Là công nghệ ảo hóa toàn bộ tài nguyên lưu trữ phần cứng vật lý thành một cụm tài nguyên logic thống nhất do phần mềm tự động điều phối và quản lý.
  - Tách rời lớp phần mềm điều khiển (Control Plane) khỏi phần cứng lưu trữ vật lý (Data Plane).
- **3. Tích hợp trong Cơ sở dữ liệu phân tán (분산 데이터베이스 연계):**
  - Trong các hệ thống CSDL phân tán quy mô lớn, các máy chủ tại từng Site thường kết nối với hệ thống **SAN** để bảo đảm tốc độ ghi nhật ký giao dịch và truy xuất các bảng phân vùng lớn.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Kiến trúc lưu trữ nào sử dụng cáp quang và Switch quang (FC) để kết nối mạng chuyên dụng?"* $\rightarrow$ Đáp án: **SAN (Storage Area Network)**.
  - Đề hỏi: *"Kiến trúc nào kết nối trực tiếp bằng cáp riêng và không thể chia sẻ dữ liệu cho máy chủ khác?"* $\rightarrow$ Đáp án: **DAS (Direct Attached Storage)**.
  - Đề hỏi: *"Kiến trúc nào dùng mạng Ethernet và dễ bị giảm hiệu năng khi tải mạng tăng?"* $\rightarrow$ Đáp án: **NAS (Network Attached Storage)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh cấp độ truy xuất: File-level (NAS) vs Block-level (SAN):**
  - **File-level (NAS):** Máy khách gửi yêu cầu dạng "Hãy cho tôi đọc tệp `tailieu.pdf`". Thiết bị NAS tự định vị các block trên ổ đĩa và trả về nguyên vẹn tệp tin. Thích hợp chia sẻ tài liệu văn phòng, ảnh, video.
  - **Block-level (SAN):** Máy chủ CSDL tự quản lý hệ thống tệp và chỉ gửi lệnh dạng "Hãy đọc khối dữ liệu số 4096 đến 8192 trên ổ đĩa LUN 1". Máy chủ DBMS trực tiếp điều khiển từng block dữ liệu, đạt hiệu năng tối đa cho hệ quản trị CSDL quan hệ như Oracle, SQL Server.

### 복습 체크리스트
- [ ] Phân biệt được đặc điểm vật lý của DAS (cáp riêng), NAS (mạng Ethernet), SAN (mạng cáp quang FC).
- [ ] Nêu được ưu và nhược điểm lớn nhất của từng loại kiến trúc lưu trữ.
- [ ] Phân biệt được File-level access (NAS) và Block-level access (SAN).
- [ ] Hiểu rõ khái niệm SDS (Software-Defined Storage).
