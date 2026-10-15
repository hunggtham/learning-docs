# 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và lợi ích của kỹ thuật tái sử dụng phần mềm (소프트웨어 재사용 - Software Reuse): sử dụng lại toàn bộ hoặc một phần các sản phẩm phát triển phần mềm đã được kiểm chứng nhằm tiết kiệm thời gian, chi phí và nâng cao độ tin cậy.
- Phân biệt hai phương pháp tái sử dụng cơ bản: Phương pháp tổng hợp (합성 중심 - Composition-based / Component-based) và Phương pháp tạo sinh (생성 중심 - Generation-based).
- Hiểu rõ các quy trình kỹ thuật liên quan: Phân tích tái sử dụng (분석 - Analysis), Tái cấu trúc (재구조 - Restructuring), và Kỹ nghệ đảo ngược (역공학 - Reverse Engineering).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 재사용 (Software Reuse)
- 합성 중심 (Composition-based / 블록 맞춤식 / 컴포넌트 재사용)
- 생성 중심 (Generation-based / 패턴 및 명세 구체화)
- 재공학 (Re-engineering / 분석, 재구성, 역공학)
- 개발 비용 및 기간 단축 (Cost & Time Reduction)
- 소프트웨어 품질 향상 (Quality Enhancement)

## 선행·연결 개념 (Kiến thức liên kết)
- [91-bai-hoc.md](91-bai-hoc.md): Kỹ thuật thiết kế thuật toán và độ phức tạp thời gian.
- [93-bai-hoc.md](93-bai-hoc.md): Đặc trưng cơ sở dữ liệu và hệ thống DBMS.
- [33-bai-hoc.md](33-bai-hoc.md): Nguyên lý thiết kế mô-đun và tính trừu tượng.

## 읽는 방법 (Cách đọc)
- Phân biệt hai trường phái tái sử dụng lớn trong đề thi:
  - **합성 중심 (Composition-based / Hướng tổng hợp):** Giống như chơi xếp hình Lego. Lấy các khối linh kiện có sẵn (**컴포넌트 - Component**) đã được kiểm thử để lắp ráp lại thành phần mềm mới.
  - **생성 중심 (Generation-based / Hướng tạo sinh):** Dựa trên tài liệu đặc tả trừu tượng hoặc các mẫu cấu trúc (Pattern) để hệ thống tự động sinh ra mã nguồn mới phù hợp với bài toán.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh hai phương pháp tái sử dụng phần mềm:**

| Tiêu chuẩn so sánh | 합성 중심 (Composition / Block) | 생성 중심 (Generation / Pattern) |
| :--- | :--- | :--- |
| **Cơ chế tái sử dụng** | Lắp ghép các khối phần mềm (**블록 / 컴포넌트**) đã hoàn thiện | Tự động sinh mã dựa trên **bản mô tả đặc tả trừu tượng** |
| **Bản chất kỹ thuật** | Tái sử dụng ở mức linh kiện nhị phân hoặc thư viện mã | Tái sử dụng ở mức tri thức thiết kế và quy tắc sinh mã |
| **Hình tượng ẩn dụ** | Xếp gạch Lego thành ngôi nhà mới | Máy in 3D in đồ vật dựa trên bản vẽ CAD |
| **Ưu điểm** | Dễ hiểu, tiết kiệm thời gian tích hợp trực tiếp | Linh hoạt thích ứng với các biến thể bài toán khác nhau |

- **Bốn hoạt động cốt lõi của Tái kỹ nghệ phần mềm (Re-engineering):**
  1. **분석 (Analysis - Phân tích):** Khảo sát hệ thống hiện tại để xác định phần nào còn giá trị tái sử dụng.
  2. **재구성 (Restructuring - Tái cấu trúc):** Thay đổi cấu trúc mã nguồn bên trong mà không làm đổi hành vi chức năng.
  3. **역공학 (Reverse Engineering - Kỹ nghệ đảo ngược):** Khôi phục lại tài liệu thiết kế và đặc tả từ mã nguồn nhị phân có sẵn.
  4. **이관 (Migration - Chuyển dịch):** Đưa phần mềm sang môi trường phần cứng hoặc hệ điều hành mới.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Lợi ích chiến lược của việc tái sử dụng:**
  - Giảm thiểu rủi ro lỗi logic: Mã nguồn đã chạy qua nhiều năm trong các dự án trước đã được kiểm thử thực tế và chịu tải tốt.
  - Tăng năng suất lao động: Giảm thiểu công việc viết code lặp lại (Boilerplate code).
  - Chuẩn hóa kiến trúc doanh nghiệp: Các dự án dùng chung một bộ Component UI/API nhất quán.

### 복습 체크리스트
- [ ] Phân biệt rõ 합성 중심 (lắp ráp linh kiện/Component) và 생성 중심 (sinh mã từ đặc tả).
- [ ] Nhớ mục đích cốt lõi của Software Reuse: Tiết kiệm chi phí, rút ngắn thời gian, tăng chất lượng.
- [ ] Nêu được 4 bước của Re-engineering: 분석 (Analysis), 재구성 (Restructuring), 역공학 (Reverse Engineering), 이관 (Migration).
