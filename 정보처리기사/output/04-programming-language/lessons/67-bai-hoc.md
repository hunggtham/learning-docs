# 209. 소프트웨어 재공학 (Software Reengineering / Tái cấu trúc phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục đích chiến lược và sự cần thiết của kỹ thuật tái công nghệ phần mềm (소프트웨어 재공학 - Software Reengineering) trong việc giải quyết khủng hoảng bảo trì.
- Thuộc lòng 4 hoạt động kỹ thuật cốt lõi của quy trình Reengineering theo khẩu quyết **분재역이**: Phân tích (분석), Tái cấu trúc (재구성), Kỹ thuật dịch ngược (역공학), và Di trú hệ thống (이식).
- Phân biệt bản chất giữa Kỹ thuật dịch ngược (Reverse Engineering - khôi phục tài liệu thiết kế từ mã nguồn) và Tái cấu trúc (Restructuring - tối ưu hóa cấu trúc code giữ nguyên chức năng).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 재공학 (Software Reengineering)
- 유지보수성 향상 (Maintainability Enhancement)
- 분석 (Analysis)
- 재구성/개조 (Restructuring / Refactoring)
- 역공학 (Reverse Engineering)
- 재문서화 (Redocumentation)
- 이식 (Migration)
- 암기 공식 (분재역이)

## 선행·연결 개념 (Kiến thức liên kết)
- [62-bai-hoc.md](62-bai-hoc.md): Phân loại bảo trì phần mềm (수적완예: 예방 보수).
- [63-bai-hoc.md](63-bai-hoc.md): Hiện tượng mã ngoài hành tinh (Alien Code).
- [68-bai-hoc.md](68-bai-hoc.md): Công cụ hỗ trợ phát triển phần mềm tự động CASE.

## 읽는 방법 (Cách đọc)
- Khẩu quyết 4 hoạt động tái công nghệ bắt buộc phải nhớ khi đi thi:
  $$\mathbf{분 \rightarrow 재 \rightarrow 역 \rightarrow 이}$$
  - **분**석 (Analysis): Khảo sát hiện trạng hệ thống cũ.
  - **재**구성 (Restructuring): Viết lại cấu trúc code cho gọn sạch, không đổi chức năng.
  - **역**공학 (Reverse Engineering): Dịch ngược từ code ra tài liệu thiết kế (**Hình thức cổ điển nhất là 재문서화 - Redocumentation**).
  - **이**식 (Migration): Đưa app sang môi trường phần cứng, OS mới.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Mục đích của tái công nghệ phần mềm (Software Reengineering):**
  - Không phải vứt bỏ toàn bộ để làm lại từ số 0 mà là **cải tiến, tu sửa và nâng cấp hệ thống phần mềm cũ** nhằm kéo dài vòng đời sử dụng, nâng cấp chất lượng và cắt giảm chi phí bảo trì.
  - Được xếp vào dạng bảo trì phòng ngừa (예방 보수 - Preventive Maintenance).

- **2. Bảng phân tích 4 hoạt động chính của Reengineering (분재역이):**

| Hoạt động | Tên tiếng Hàn & Anh | Mục tiêu & Phương pháp thực hiện |
| :--- | :--- | :--- |
| **Phân tích** | **분석** (Analysis) | Đánh giá hiện trạng của phần mềm, mức độ đáp ứng nghiệp vụ, độ phức tạp của mã nguồn và dự toán chi phí tái công nghệ. |
| **Tái cấu trúc** | **재구성 / 개조** (Restructuring) | Sắp xếp, tổ chức lại cấu trúc dữ liệu và logic điều khiển bên trong mã nguồn nhằm loại bỏ code thừa, giảm độ kết hợp mà **hoàn toàn giữ nguyên hành vi chức năng bên ngoài** (tương tự khái niệm Refactoring hiện đại). |
| **Dịch ngược** | **역공학** (Reverse Engineering) | Phân tích mã nguồn hoặc tệp nhị phân hiện có để **khôi phục ngược lại tài liệu đặc tả, sơ đồ luồng dữ liệu (DFD) và kiến trúc thiết kế**. Hình thức lâu đời và phổ biến nhất của 역공학 là **재문서화 (Redocumentation - Viết lại tài liệu)**. |
| **Di trú** | **이식** (Migration) | Chuyển đổi toàn bộ cơ sở mã nguồn và dữ liệu sang vận hành trên nền tảng phần cứng mới, hệ điều hành mới hoặc ngôn ngữ lập trình hiện đại hơn. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phân biệt Thuận công nghệ (Forward Engineering) vs Nghịch công nghệ (Reverse Engineering):**
  - *Forward Engineering (순공학):* Đi theo luồng truyền thống từ Đặc tả yêu cầu $\rightarrow$ Thiết kế kiến trúc $\rightarrow$ Viết mã nguồn (Coding).
  - *Reverse Engineering (역공학):* Đi ngược lại từ Mã nguồn đã biên dịch/chương trình thực thi $\rightarrow$ Phân tích cấu trúc hàm $\rightarrow$ Khôi phục lại bản vẽ thiết kế kiến trúc và mô hình dữ liệu ban đầu.

### 복습 체크리스트
- [ ] Thuộc lòng 4 bước tái công nghệ: **분재역이** (분석, 재구성, 역공학, 이식).
- [ ] Nhớ Kỹ thuật dịch ngược (Reverse Engineering) là việc khôi phục tài liệu thiết kế từ mã nguồn có sẵn.
- [ ] Ghi nhớ hình thức lâu đời nhất của Reverse Engineering là **재문서화 (Redocumentation)**.
- [ ] Khẳng định Restructuring tối ưu hóa cấu trúc nội bộ nhưng không làm thay đổi chức năng bên ngoài.
