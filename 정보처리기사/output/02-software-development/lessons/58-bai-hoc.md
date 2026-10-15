# 43. 테스트 분류 방식 (Test Classification)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống phân loại kiểm thử phần mềm đa chiều dựa trên 3 tiêu chí: Theo trạng thái thực thi (실행 여부), Theo cơ sở thiết kế (기반) và Theo mục đích kiểm tra (목적).
- Phân biệt sự khác nhau giữa Kiểm thử tĩnh (정적 테스트 - Không chạy chương trình) và Kiểm thử động (동적 테스트 - Trực tiếp thực thi mã nguồn).
- Nằm lòng 6 loại hình kiểm thử theo mục đích chuyên biệt: Kiểm thử phục hồi (Recovery), Kiểm thử bảo mật (Security), Kiểm thử áp lực quá tải (Stress), Kiểm thử hiệu năng (Performance), Kiểm thử hồi quy (Regression) và Kiểm thử song song (Parallel).

## 핵심 키워드 (Từ khóa)
- 테스트 분류 (Test Classification)
- 정적 테스트 (Static Testing: 워크스루, 인스펙션)
- 동적 테스트 (Dynamic Testing: 화이트박스, 블랙박스)
- 명세 기반 (Specification) & 구조 기반 (Structure) & 경험 기반 (Experience)
- 회복 테스트 (Recovery) & 안전 테스트 (Security)
- 강도 / 스트레스 테스트 (Stress Testing / 과부하)
- 회귀 테스트 (Regression Testing / 변경 후 결함 재확인)
- 병행 테스트 (Parallel Testing)

## 선행·연결 개념 (Kiến thức liên kết)
- [52-bai-hoc.md](52-bai-hoc.md): Kiểm thử hộp trắng vs Kiểm thử hộp đen (thuộc nhóm Kiểm thử động).
- [57-bai-hoc.md](57-bai-hoc.md): Các nguyên lý kiểm thử ứng dụng nền tảng.
- [59-bai-hoc.md](59-bai-hoc.md): Các tiêu chí độ phủ trong kiểm thử cấu trúc.

## 읽는 방법 (Cách đọc)
- Phân biệt theo mục đích kiểm thử cực kỳ hay gặp trong đề thi:
  - Cố tình đánh sập hệ thống rồi đo thời gian phục hồi $\rightarrow$ **회복 테스트 (Recovery)**.
  - Đưa tải trọng vượt quá giới hạn thiết kế (quá tải CPU/RAM) $\rightarrow$ **강도 테스트 (Stress)**.
  - Đo thời gian phản hồi, thông lượng xử lý $\rightarrow$ **성능 테스트 (Performance)**.
  - **Sửa code xong kiểm tra lại xem có phát sinh lỗi MỚI ở chỗ khác không** $\rightarrow$ **회귀 테스트 (Regression)**.
  - Cho hệ thống mới và hệ thống cũ chạy song song cùng một dữ liệu để so kết quả $\rightarrow$ **병행 테스트 (Parallel)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân loại theo Trạng thái thực thi chương trình (실행 여부):**
  - **정적 테스트 (Static Testing):** **Không chạy chương trình trên máy tính**, tiến hành rà soát thủ công cấu trúc mã, tài liệu thiết kế hoặc dùng công cụ phân tích tĩnh.
    - *Hình thức:* 워크스루 (Walkthrough - trao đổi không chính thức), 인스펙션 (Inspection - kiểm tra chính thức theo checklist), 정적 코드 분석 (Static Code Analysis).
  - **동적 테스트 (Dynamic Testing):** **Trực tiếp nạp và chạy chương trình trên máy tính**, truyền dữ liệu vào để kiểm tra hành vi thực tế. Bao gồm cả White-box và Black-box Testing.
- **2. Phân loại theo Cơ sở thiết kế ca kiểm thử (Bases):**
  - **명세 기반 (Specification-based):** Dựa vào bản đặc tả yêu cầu chức năng (Black-box: Equivalence Partitioning, Boundary Value).
  - **구조 기반 (Structure-based):** Dựa vào cấu trúc luồng điều khiển mã nguồn bên trong (White-box: Statement, Branch, Condition Coverage).
  - **경험 기반 (Experience-based):** Dựa vào trực giác và kinh nghiệm tích lũy của kiểm thử viên (Error Guessing, Exploratory Testing).
- **3. Phân loại theo Mục đích kiểm tra chuyên biệt (Rất hay thi):**

| Loại kiểm thử | Tên tiếng Hàn & Anh | Mục đích và cơ chế kiểm tra (Từ khóa nhận diện) |
| :--- | :--- | :--- |
| **Kiểm thử phục hồi** | **회복 테스트 (Recovery)** | Cố tình tạo ra các sự cố phần cứng, ngắt mạng hoặc sập nguồn để kiểm tra khả năng tự động sao lưu và khôi phục dữ liệu bình thường của hệ thống |
| **Kiểm thử an toàn** | **안전 테스트 (Security)** | Kiểm tra các lỗ hổng bảo mật, cơ chế xác thực, phân quyền và khả năng chống lại các cuộc tấn công thâm nhập bất hợp pháp từ bên ngoài |
| **Kiểm thử áp lực** | **강도 테스트 (Stress)** | Đưa hệ thống vào trạng thái **quá tải cực đoan (Overload)** vượt quá năng lực thiết kế tối đa (ví dụ: lượng truy cập gấp 10 lần) để xem hệ thống sập thế nào |
| **Kiểm thử hiệu năng** | **성능 테스트 (Performance)** | Đo lường các chỉ số hiệu quả vận hành trong điều kiện bình thường: **Thời gian phản hồi (Response Time), Thông lượng (Throughput), Tỷ lệ sử dụng tài nguyên (CPU/RAM)** |
| **Kiểm thử hồi quy** | **회귀 테스트 (Regression)** | Sau khi sửa lỗi hoặc nâng cấp tính năng mới, **tiến hành kiểm tra lại toàn bộ hệ thống để bảo đảm việc sửa code không sinh ra lỗi mới (새로운 결함)** |
| **Kiểm thử song song** | **병행 테스트 (Parallel)** | Nhập cùng một tập dữ liệu đầu vào vào cả hệ thống mới và hệ thống cũ đang vận hành để so sánh đối chiếu kết quả đầu ra xem có đồng nhất không |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tự động hóa Kiểm thử hồi quy (Automated Regression Testing):**
  - Trong phương pháp phát triển Agile và quy trình CI/CD hiện đại, việc sửa code diễn ra hàng ngày, thậm chí hàng giờ.
  - Con người không thể chạy lại bằng tay hàng nghìn Test Case mỗi lần commit. Vì vậy, **Kiểm thử hồi quy luôn được tự động hóa 100%** bằng các công cụ như Selenium, Cypress, JUnit để máy chủ tự động thực thi trong đêm hoặc trong tiến trình CI/CD.

### 복습 체크리스트
- [ ] Phân biệt được Kiểm thử tĩnh (không chạy code) và Kiểm thử động (chạy code).
- [ ] Nhớ 3 cơ sở thiết kế: Đặc tả (Spec), Cấu trúc (Code), Kinh nghiệm (Experience).
- [ ] Nhận diện 강도 테스트 (Stress) qua từ khóa kiểm tra tình trạng quá tải (과부하).
- [ ] Nhận diện 회귀 테스트 (Regression) qua từ khóa kiểm tra phát sinh lỗi mới sau khi sửa mã.
- [ ] Nhận diện 병행 테스트 (Parallel) qua việc chạy song song hệ thống cũ và mới.
