# 100-2 ~ 104: 저작권 및 DRM (Copyright & Digital Rights Management)

## 학습 목표 (Mục tiêu)
- Định nghĩa Quyền tác giả phần mềm (소프트웨어 저작권 - Software Copyright) với tư cách là quyền độc quyền mang tính bài trừ (배타적 독점적 권리) của người sáng tạo.
- Hiểu rõ sự kết hợp giữa khung khổ pháp lý bản quyền và các biện pháp bảo vệ kỹ thuật số bằng công nghệ DRM.
- Nắm vững các công nghệ xác thực và nhận diện quyền sở hữu trí tuệ: Thủy vân số (워터마킹 - Digital Watermarking), Giấu tin mật (스테가노그래피 - Steganography), Ngôn ngữ XrML và các mô hình tính cước tại Clearing House.

## 핵심 키워드 (Từ khóa)
- 저작권 (Copyright / 배타적 독점적 권리)
- DRM 핵심 기술 (Core DRM Technologies)
- 클리어링 하우스 (Clearing House / 종량제 청구)
- 디지털 워터마킹 (Digital Watermarking / 저작권 표시)
- 스테가노그래피 (Steganography / 기밀 은닉)
- XrML (eXtensible rights Markup Language)
- DOI (Digital Object Identifier)

## 선행·연결 개념 (Kiến thức liên kết)
- [43-bai-hoc.md](43-bai-hoc.md): Quy trình chi tiết đóng gói DRM (Real-time vs Pre-packaging).
- [50-bai-hoc.md](50-bai-hoc.md): Hệ thống 6 thành phần kiến trúc của DRM.
- [52-bai-hoc.md](52-bai-hoc.md): Chuyển sang chương Kiểm thử phần mềm (Testing: White-box vs Black-box).

## 읽는 방법 (Cách đọc)
- Phân biệt cặp công nghệ bảo vệ bản quyền hay bị hỏi bẫy trong đề thi:
  - **디지털 워터마킹 (Digital Watermarking):** Chèn thông tin bản quyền (Logo chìm, mã tác giả) vào nội dung để **khẳng định quyền sở hữu và chứng minh tác quyền khi bị đạo nhái**.
  - **스테가노그래피 (Steganography):** Giấu một bức thông điệp bí mật bên trong một bức ảnh hoặc file âm thanh bình thường để **truyền tin mật mà người ngoài không hay biết**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bản chất pháp lý của Quyền tác giả (저작권 - Copyright):**
  - Là quyền sở hữu trí tuệ mang tính chất **độc quyền và loại trừ (배타적 독점적 권리)** dành cho người sáng tạo ra tác phẩm tinh thần (phần mềm, thuật toán, cơ sở dữ liệu).
  - Do đặc tính kỹ thuật số rất dễ bị sao chép nguyên vẹn chỉ bằng một thao tác nhấn phím (`Ctrl+C / Ctrl+V`), pháp luật quốc tế thừa nhận việc áp dụng các biện pháp kỹ thuật số (DRM) để ngăn chặn hành vi xâm phạm quyền tác giả.
- **Bảng tổng hợp các kỹ thuật bảo mật bản quyền chuyên sâu trong đề thi:**

| Công nghệ kỹ thuật | Tên tiếng Hàn & Anh | Mục đích và cơ chế hoạt động |
| :--- | :--- | :--- |
| **Định danh đối tượng số** | **DOI (Digital Object Identifier)** | Hệ thống cấp mã số định danh duy nhất toàn cầu cho các tài sản số trên Internet, bảo đảm liên kết vĩnh viễn dù tệp có đổi máy chủ lưu trữ |
| **Ngôn ngữ biểu diễn quyền** | **XrML (eXtensible rights Markup Language)** | Ngôn ngữ chuẩn hóa dựa trên XML dùng để **định nghĩa cụ thể các quyền hạn sử dụng** (Xem, in, sao chép, thời hạn hết hạn) kèm chữ ký số bảo đảm toàn vẹn |
| **Thủy vân số** | **디지털 워터마킹 (Digital Watermarking)** | Nhúng thông tin bản quyền (Tên tác giả, số ID người mua) vào sâu trong tín hiệu số của hình ảnh/video/âm thanh mà mắt người không nhận thấy, dùng để **truy vết nguồn gốc phát tán lậu** |
| **Kỹ thuật giấu tin** | **스테가노그래피 (Steganography)** | Kỹ thuật giấu kín dữ liệu mật vào trong các bit trọng số thấp (LSB) của tệp đa phương tiện vô hại để truyền thông tin tuyệt mật |
| **Chống bẻ khóa** | **크랙 방지 (Tamper Resistance)** | Xáo trộn luồng điều khiển mã (Code Obfuscation), mã hóa chuỗi ký tự, ngăn chặn Reverse Engineering và Debugger |

- **Cơ chế thanh toán và cấp phép tại Clearing House:**
  - Hỗ trợ đa dạng các mô hình kinh doanh:
    - Mua đứt một lần (Perpetual License).
    - Thuê bao định kỳ theo tháng/năm (Subscription).
    - **Tính cước theo lượng sử dụng (종량제 - Pay-per-use):** Trừ tiền dựa trên số lần mở tệp, thời gian xem video, hoặc lưu lượng dữ liệu truyền tải.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phân loại Thủy vân số (Watermarking):**
  - **Visible Watermark (Hữu hình):** Logo chìm đè lên góc video/ảnh (dễ thấy, dùng để quảng bá và cảnh báo).
  - **Invisible Watermark (Vô hình):** Nhúng vào miền tần số (DCT, DWT) của ảnh. Kể cả khi kẻ gian cắt xén ảnh (Cropping), nén ảnh JPEG thì thông tin bản quyền vẫn tồn tại và phần mềm chuyên dụng vẫn trích xuất ra được.

### 복습 체크리스트
- [ ] Định nghĩa quyền tác giả là quyền độc quyền loại trừ (배타적 독점적 권리).
- [ ] Phân biệt được Digital Watermarking (chứng minh tác quyền) và Steganography (giấu tin mật).
- [ ] Nhớ tên ngôn ngữ biểu diễn quyền hạn sử dụng là XrML.
- [ ] Nhớ mã định danh số chuẩn hóa toàn cầu là DOI.
