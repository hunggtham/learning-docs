# 120-1: 소프트웨어의 분류 (Software Classification)

## 학습 목표 (Mục tiêu)
- Nắm vững các tiêu chuẩn phân loại phần mềm trong kỹ nghệ phần mềm dựa trên mục đích sử dụng, quyền sở hữu bản quyền và mô hình phân phối sản phẩm.
- Phân biệt rõ sự khác nhau giữa Phần mềm thương mại đóng gói (상용 소프트웨어 - Commercial Software / COTS) và Phần mềm phát triển theo đơn đặt hàng (주문형 소프트웨어 / SI - Custom/Contract Software).
- Nhận diện và phân loại chính xác các hình thức phân phối phần mềm: Phần mềm miễn phí (Freeware), Phần mềm dùng thử (Shareware), Phần mềm mã nguồn mở (Open Source Software - OSS), và Phần mềm miền công cộng (Public Domain Software).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 분류 (Software Classification)
- 상용 소프트웨어 (Commercial Software / COTS / 패키지 소프트웨어)
- 주문형 소프트웨어 (Custom / Bespoke Software / SI 개발)
- 프리웨어 (Freeware / 무료 사용 / 소스 비공개)
- 셰어웨어 (Shareware / 체험판 / 일정 기간 및 기능 제한)
- 공개 소프트웨어 (Open Source Software / OSS / 소스 공개)
- 라이선스 (License / GPL, MIT, Apache)

## 선행·연결 개념 (Kiến thức liên kết)
- [100-bai-hoc.md](100-bai-hoc.md): Các mô hình công cụ quản lý phiên bản (SCM).
- [51-bai-hoc.md](51-bai-hoc.md): Bản quyền phần mềm và công nghệ DRM.
- [정보처리기사/output/03-database-construction/lessons/01-bai-hoc.md](../../03-database-construction/lessons/01-bai-hoc.md): Cơ sở dữ liệu và hệ thống quản lý cơ sở dữ liệu.

## 읽는 방법 (Cách đọc)
- Phân biệt 4 nhóm phân phối bản quyền phần mềm:
  - **상용 소프트웨어 (Commercial):** Người dùng phải trả tiền mua bản quyền mới được phép cài đặt và sử dụng (ví dụ: Microsoft Windows, Adobe Photoshop, Oracle RDBMS).
  - **셰어웨어 (Shareware):** Cho phép dùng thử miễn phí trong một khoảng thời gian nhất định (Trial 30 ngày) hoặc bị khóa một số tính năng nâng cao, muốn dùng tiếp hoặc mở khóa đầy đủ thì phải trả phí.
  - **프리웨어 (Freeware):** Miễn phí hoàn toàn 100% cho mục đích sử dụng cá nhân, nhưng tác giả **giữ kín mã nguồn (không mở mã nguồn)**.
  - **공개 소프트웨어 (Open Source / OSS):** Mở hoàn toàn mã nguồn cho cộng đồng tự do nghiên cứu, chỉnh sửa và phân phối lại theo các giấy phép mã nguồn mở quy định (GPL, Apache, MIT).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh Phần mềm thương mại đóng gói vs Phần mềm đặt hàng riêng:**

| Tiêu chí | 상용 소프트웨어 (Commercial / COTS) | 주문형 소프트웨어 (Custom / Contract / SI) |
| :--- | :--- | :--- |
| **Đối tượng người dùng** | Thị trường đại chúng rộng lớn (General Public) | Một tổ chức hoặc doanh nghiệp đặt hàng cụ thể |
| **Hình thức sản phẩm** | Đóng gói sẵn hoàn chỉnh (**패키지 소프트웨어**); mua về cài đặt dùng ngay | Xây dựng theo hợp đồng (**SI 프로젝트**); tùy biến riêng theo quy trình nghiệp vụ |
| **Chi phí ban đầu** | Tương đối thấp do chia sẻ chi phí cho hàng triệu người mua | Rất cao do phải trả toàn bộ chi phí nhân công phát triển |
| **Khả năng tùy biến** | Khó hoặc không thể tùy biến sâu mã nguồn cốt lõi | Hoàn toàn làm chủ mã nguồn và cấu trúc hệ thống |
| **Ví dụ tiêu biểu** | Hệ điều hành Windows, MS Office, Game bán lẻ | Hệ thống Core Banking của ngân hàng, Cổng thông tin nội bộ |

- **Bảng phân loại các hình thức cấp phép và phân phối phần mềm:**

| Loại phần mềm | Phí sử dụng | Trạng thái mã nguồn | Giới hạn tính năng / thời gian |
| :--- | :--- | :--- | :--- |
| **상용 (Commercial)** | Có phí (유료) | Đóng kín (비공개) | Đầy đủ tính năng sau khi kích hoạt bản quyền |
| **셰어웨어 (Shareware)** | Miễn phí ban đầu, thu phí sau | Đóng kín (비공개) | **Giới hạn thời gian (30 ngày) hoặc tính năng (Trial)** |
| **프리웨어 (Freeware)** | Hoàn toàn miễn phí | Đóng kín (비공개) | Đầy đủ tính năng, cấm bán lại mã nguồn |
| **공개 (Open Source / OSS)** | Thường miễn phí | **Mở công khai (공개)** | Tự do sửa đổi và phân phối tuân theo điều khoản giấy phép |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Các loại giấy phép mã nguồn mở (Open Source Licenses):**
  - **GPL (General Public License):** Tính chất lan truyền mạnh (Copyleft); bất kỳ ai sử dụng mã nguồn GPL để sửa đổi hoặc phát triển tiếp đều **bắt buộc phải công khai toàn bộ mã nguồn** của sản phẩm mới đó.
  - **MIT License & Apache License:** Rất thông thoáng (Permissive); cho phép tự do sử dụng trong cả các sản phẩm thương mại đóng kín mà không ép buộc phải mở mã nguồn sản phẩm phái sinh.

### 복습 체크리스트
- [ ] Phân biệt rõ 상용 소프트웨어 (thương mại đóng gói) và 주문형 소프트웨어 (đặt hàng riêng SI).
- [ ] Nhớ Shareware là phần mềm cho dùng thử có giới hạn thời gian hoặc tính năng.
- [ ] Nhớ Freeware miễn phí nhưng KHÔNG mở mã nguồn, còn OSS mở công khai mã nguồn.
- [ ] Hiểu tính chất lan truyền mở mã nguồn của giấy phép GPL.
