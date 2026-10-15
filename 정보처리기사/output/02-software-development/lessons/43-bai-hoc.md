# 39. DRM 패키징 과정 상세 (DRM Packaging Process)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình kỹ thuật đóng gói nội dung số tích hợp Quản lý bản quyền số (DRM 패키징 과정).
- Phân biệt hai chiến lược đóng gói DRM dựa trên dung lượng tệp tin: Đóng gói thời gian thực (실시간 패키징 - Real-time Packaging cho tệp nhỏ) và Đóng gói trước (사전 패키징 - Pre-packaging cho tệp lớn).
- Hiểu rõ vai trò của Chữ ký số mã hóa của tác giả và cơ chế đăng ký giấy phép (License) tại Trung tâm thanh toán bản quyền (Clearing House).

## 핵심 키워드 (Từ khóa)
- DRM 패키징 (DRM Packaging Process)
- 실시간 패키징 (Real-time Packaging / 소용량)
- 사전 패키징 (Pre-packaging / 대용량)
- 암호화된 전자서명 (Encrypted Digital Signature)
- 클리어링 하우스 (Clearing House)
- 라이선스 발급 (License Issuance)
- 보안 컨테이너 (Security Container)

## 선행·연결 개념 (Kiến thức liên kết)
- [41-bai-hoc.md](41-bai-hoc.md): Khái niệm chung về đóng gói phần mềm và tài liệu hướng dẫn.
- [42-bai-hoc.md](42-bai-hoc.md): Các lưu ý bảo mật và tích hợp DRM khi đóng gói.
- [50-bai-hoc.md](50-bai-hoc.md): Hệ thống các thành phần và kỹ thuật nền tảng của DRM.

## 읽는 방법 (Cách đọc)
- Phân biệt 2 chiến lược đóng gói qua bài toán dung lượng tệp:
  - Tệp dung lượng nhỏ (Âm thanh ngắn, ảnh, văn bản e-book) $\rightarrow$ **실시간 패키징 (Real-time Packaging)**: Khách bấm mua mới lập tức đóng gói và cấp phép.
  - Tệp dung lượng lớn (Phim 4K, video dài nhiều GB) $\rightarrow$ **사전 패키징 (Pre-packaging)**: Bắt buộc phải đóng gói mã hóa sẵn từ trước để tránh máy chủ bị quá tải.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Quy trình 5 bước đóng gói DRM chuẩn:**
  1. **Số hóa nội dung (Digitization):** Chuyển đổi nội dung tương tự (Analog) sang định dạng kỹ thuật số (Digital) nếu cần thiết.
  2. **Tạo siêu dữ liệu (Metadata Creation):** Gắn thông tin tác giả, mã định danh nội dung (DOI, URI) và các chính sách điều kiện sử dụng (Usage Rules).
  3. **Đóng gói mã hóa (Packager Packaging):**
     - Bộ đóng gói (Packager) sử dụng thuật toán mã hóa đối xứng mạnh (như AES) để mã hóa toàn bộ tệp nội dung.
     - Nhúng chữ ký số đã được mã hóa của chủ sở hữu bản quyền vào tệp.
     - Đặt nội dung vào bên trong một **Thùng chứa bảo mật (보안 컨테이너 - Security Container)**.
  4. **Đăng ký bản quyền tại Clearing House:**
     - Tạo khóa giải mã và bản đặc tả giấy phép (License Policy: số lần xem, hạn sử dụng, cấm sao chép/in ấn).
     - Đăng ký và lưu trữ giấy phép chính thức tại **클리어링 하우스 (Clearing House)**.
  5. **Phân phối nội dung:** Đưa tệp đã đóng gói lên máy chủ phân phối (Distributor/CDN) để người dùng tải về.

- **So sánh hai chiến lược đóng gói DRM:**

| Chiến lược đóng gói | 실시간 패키징 (Real-time Packaging) | 사전 패키징 (Pre-packaging) |
| :--- | :--- | :--- |
| **Dung lượng nội dung** | **Dung lượng nhỏ (소용량)**: Ảnh, bài nhạc MP3 đơn lẻ, tài liệu PDF ngắn | **Dung lượng lớn (대용량)**: Phim ảnh chất lượng cao (HD/4K), trò chơi game |
| **Thời điểm đóng gói** | Đóng gói tức thời theo yêu cầu khi người dùng bấm mua hoặc tải | Đóng gói hoàn tất từ trước và lưu sẵn trên kho nội dung |
| **Tải trọng máy chủ** | Tải CPU tăng tức thời theo số lượng giao dịch đồng thời | Phân bổ tải đều, không làm thắt cổ chai máy chủ lúc cao điểm |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình giải mã và thực thi quyền hạn trên thiết bị người dùng:**
  - Khi người dùng tải về một tệp phim đã được đóng gói DRM:
    - Tệp phim bị khóa chặt không thể mở bằng các phần mềm phát video thông thường.
    - Thiết bị phải kích hoạt **DRM Controller**:
      - Gửi yêu cầu xác thực thanh toán đến **Clearing House**.
      - Clearing House cấp phát **License** chứa khóa giải mã và chính sách bản quyền (ví dụ: chỉ cho xem trong 48 giờ).
      - DRM Controller giải mã luồng video trực tiếp trong bộ nhớ an toàn (Secure Memory) và ngăn chặn việc chụp ảnh màn hình hoặc ghi video quay trộm.

### 복습 체크리스트
- [ ] Phân biệt được 실시간 패키징 (Tệp nhỏ) và 사전 패키징 (Tệp lớn).
- [ ] Nhớ Packager có nhiệm vụ mã hóa nội dung và nhúng chữ ký số của tác giả.
- [ ] Xác định vai trò của Clearing House là nơi lưu trữ và cấp phát License bản quyền.
- [ ] Nêu được chức năng của Thùng chứa bảo mật (보안 컨테이너) trong DRM.
