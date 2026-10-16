# 소프트웨어 프로세스 품질 및 성숙도 표준 (Tiêu chuẩn chất lượng phần mềm & Mô hình độ trưởng thành ISO/IEC, CMMI, SPICE)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc, phạm vi và cách phân loại của các bộ tiêu chuẩn quốc tế về vòng đời phần mềm: **ISO/IEC 12207**.
- Phân biệt chi tiết 3 nhóm tiến trình theo ISO/IEC 12207: Tiến trình cơ bản (기본 생명 주기), Tiến trình hỗ trợ (지원 생명 주기), và Tiến trình tổ chức (조직 생명 주기).
- Nắm vững 6 đặc tính chất lượng sản phẩm phần mềm theo **ISO/IEC 9126** và bộ tiêu chuẩn hiện đại **ISO/IEC 25010 (SQuaRE)**.
- Thuộc lòng 5 cấp độ trưởng thành của mô hình **CMMI** theo khẩu quyết **초관정정최** (Initial, Managed, Defined, Quantitatively Managed, Optimizing).
- Phân biệt 6 cấp độ năng lực quy trình của tiêu chuẩn **SPICE (ISO/IEC 15504)** từ Cấp 0 đến Cấp 5.

## 핵심 키워드 (Từ khóa song ngữ)
- ISO/IEC 12207 (Software Life Cycle Processes — Tiêu chuẩn quy trình vòng đời phần mềm)
- 기본 생명 주기 (Primary Processes — 획득, 공급, 개발, 운영, 유지보수)
- 지원 생명 주기 (Supporting Processes — 문서화, 형상 관리, 품질 보증, 검증, 확인)
- 조직 생명 주기 (Organizational Processes — 관리, 기반 구조, 훈련, 개선)
- ISO/IEC 9126 (Software Product Quality — 기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성)
- ISO/IEC 25010 (SQuaRE — Bổ sung 보안성 Security và 호환성 Compatibility)
- CMMI (Capability Maturity Model Integration — Mô hình trưởng thành năng lực)
- CMMI 5단계 (초관정정최 — 초기 Initial, 관리 Managed, 정의 Defined, 정량적 관리 Quantitatively Managed, 최적화 Optimizing)
- SPICE / ISO/IEC 15504 (Software Process Improvement and Capability dEtermination — 불완전, 수행, 관리, 확립, 예측, 최적화)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi lập kế hoạch ngân sách và tiến độ tại [03-quan-ly-du-an-chi-phi-va-tien-do.md](03-quan-ly-du-an-chi-phi-va-tien-do.md), một dự án muốn bảo đảm sản phẩm đầu ra không bị lỗi và được khách hàng quốc tế chấp nhận phải tuân thủ các quy chuẩn quy trình và tiêu chuẩn chất lượng được thừa nhận toàn cầu.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp khung đánh giá chất lượng toàn diện: chuẩn hóa vòng đời phát triển (ISO/IEC 12207), tiêu chí đánh giá chất lượng sản phẩm (ISO/IEC 9126/25010) và thang đo độ trưởng thành của tổ chức phát triển (CMMI, SPICE).
- **Dùng đi đâu (Forward Handoff):** Khi quy trình phát triển và kiểm soát chất lượng đã đạt chuẩn, hệ thống thông tin cần thiết lập hàng rào phòng thủ bảo mật ngay từ khâu thiết kế tại [05-khung-bao-mat-phan-mem-va-phap-luat.md](05-khung-bao-mat-phan-mem-va-phap-luat.md) và lập trình an toàn tại [06-lo-hong-phan-mem-va-secure-coding.md](06-lo-hong-phan-mem-va-secure-coding.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **ISO/IEC 12207 (Phân loại 3 nhóm tiến trình):**
  - **Tiến trình cơ bản (기본):** Chỉ gồm 5 tiến trình trực tiếp: **획득 (Mua sắm), 공급 (Cung cấp), 개발 (Phát triển), 운영 (Vận hành), 유지보수 (Bảo trì)**.
  - **Tiến trình hỗ trợ (지원):** Các hoạt động phụ trợ độc lập: **문서화 (Tài liệu), 형상 관리 (Quản lý cấu hình), 품질 보증 (QA), 검증 (Verification), 확인 (Validation), 감사 (Audit)**.
  - **Tiến trình tổ chức (조직):** Các hoạt động cấp công ty: **관리 (Quản lý), 기반 구조 (Hạ tầng), 훈련 (Đào tạo), 개선 (Cải tiến)**.
- **CMMI 5 cấp độ (Khẩu quyết vàng: 초-관-정-정-최):**
  - Cấp 1 (초기 - Initial): Không có quy trình, dựa vào cá nhân anh hùng.
  - Cấp 2 (관리 - Managed): Quy trình được quản lý ở **cấp dự án riêng lẻ** (특정 프로젝트 중심).
  - Cấp 3 (정의 - Defined): Quy trình được chuẩn hóa ở **cấp toàn tổ chức/công ty** (조직 차원의 표준화).
  - Cấp 4 (정량적 관리 - Quantitatively Managed): Đo lường bằng **số liệu thống kê định lượng** (통계적, 정량적 측정).
  - Cấp 5 (최적화 - Optimizing): **Liên tục cải tiến** quy trình dựa trên phản hồi và công nghệ mới.
- **SPICE (ISO/IEC 15504):** Đề hỏi tiêu chuẩn đánh giá năng lực tiến trình $\rightarrow$ Chọn **SPICE / ISO/IEC 15504**; nhớ thang đo 6 mức: **Cấp 0 (불완전) đến Cấp 5 (최적화)**.

---

## 소프트웨어 프로세스 품질 및 성숙도 표준

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tiêu chuẩn quy trình vòng đời phần mềm ISO/IEC 12207
ISO/IEC 12207 là tiêu chuẩn quốc tế quy định toàn diện các hoạt động, nhiệm vụ cần thực hiện trong suốt vòng đời của phần mềm, chia thành 3 nhóm tiến trình chính:

| Nhóm tiến trình | Tên tiếng Hàn & Anh | Các tiến trình thành phần chi tiết |
| :--- | :--- | :--- |
| **Tiến trình cơ bản** | **기본 생명 주기 (Primary Processes)** | 5 tiến trình cốt lõi tạo ra và vận hành sản phẩm:<br>1. **획득 (Acquisition):** Xác định nhu cầu, đấu thầu, mua sắm.<br>2. **공급 (Supply):** Cung cấp giải pháp, bàn giao cho khách hàng.<br>3. **개발 (Development):** Phân tích, thiết kế, viết mã, kiểm thử.<br>4. **운영 (Operation):** Cài đặt và vận hành trong môi trường thực tế.<br>5. **유지보수 (Maintenance):** Sửa lỗi, thích ứng, nâng cấp. |
| **Tiến trình hỗ trợ** | **지원 생명 주기 (Supporting Processes)** | Hỗ trợ tiến trình cơ bản nhằm đảm bảo chất lượng:<br>- **문서화 (Documentation):** Lập tài liệu vòng đời.<br>- **형상 관리 (Configuration Management):** Quản lý phiên bản.<br>- **품질 보증 (Quality Assurance - QA):** Đảm bảo chất lượng độc lập.<br>- **검증 (Verification) & 확인 (Validation):** Kiểm tra đặc tả và kiểm tra người dùng.<br>- **합동 검토 (Joint Review), 감사 (Audit), 문제 해결 (Problem Resolution)**. |
| **Tiến trình tổ chức** | **조직 생명 주기 (Organizational Processes)** | Xây dựng năng lực nền tảng cho toàn bộ doanh nghiệp:<br>- **관리 (Management):** Quản lý danh mục và điều hành dự án.<br>- **기반 구조 (Infrastructure):** Thiết lập môi trường phần cứng, mạng, công cụ.<br>- **훈련 (Training):** Đào tạo kỹ năng cho nhân sự.<br>- **개선 (Improvement):** Đánh giá và cải tiến quy trình công ty. |

#### 2. Tiêu chuẩn chất lượng sản phẩm phần mềm (ISO/IEC 9126 & ISO/IEC 25010)
- **ISO/IEC 9126 — 6 đặc tính chất lượng truyền thống:**
  1. **기능성 (Functionality - Tính chức năng):** Hệ thống có thực hiện đúng và đầy đủ các chức năng yêu cầu hay không (적합성, 정확성, 상호운용성, 보안성, 준수성).
  2. **신뢰성 (Reliability - Độ tin cậy):** Khả năng duy trì mức hiệu năng xác định trong điều kiện hoạt động ổn định (성숙성, 결함 허용성, 회복성).
  3. **사용성 (Usability - Khả năng sử dụng):** Mức độ dễ hiểu, dễ học và dễ vận hành đối với người dùng (이해성, 습득성, 운용성, 매력성).
  4. **효율성 (Efficiency - Hiệu quả):** Mối quan hệ giữa mức hiệu năng và lượng tài nguyên phần cứng tiêu tốn (시간 반응성, 자원 효율성).
  5. **유지보수성 (Maintainability - Tính bảo trì):** Mức độ dễ dàng khi sửa đổi, nâng cấp và kiểm thử (분석성, 변경성, 안정성, 시험성).
  6. **이식성 (Portability - Tính khả chuyển):** Khả năng chuyển phần mềm từ môi trường này sang môi trường khác (적응성, 설치성, 공존성, 대체성).
- **ISO/IEC 25010 (SQuaRE):** Chuẩn hiện đại thay thế ISO/IEC 9126, tách độc lập thành 8 đặc tính chất lượng bằng cách nâng cấp **보안성 (Security - Tính bảo mật)** và **호환성 (Compatibility - Tính tương thích)** thành các đặc tính lớn ngang hàng.

#### 3. Mô hình trưởng thành năng lực CMMI (Capability Maturity Model Integration)
CMMI do Viện Công nghệ Phần mềm Mỹ (SEI) phát triển, đánh giá năng lực và độ trưởng thành của quy trình phát triển phần mềm trong doanh nghiệp theo 5 cấp độ (Staged Representation):

| Cấp độ | Tên tiếng Hàn & Anh | Đặc trưng nhận diện cốt lõi trong đề thi |
| :---: | :--- | :--- |
| **Level 1** | **초기 (Initial)** | - **Quy trình hỗn loạn, tự phát**, không có chuẩn mực.<br>- Thành công hoàn toàn phụ thuộc vào năng lực của **cá nhân anh hùng (영웅적 개인)**; không thể dự báo trước về chi phí và chất lượng. |
| **Level 2** | **관리 (Managed)** | - Đã thiết lập quy trình quản lý cơ bản ở **cấp độ dự án riêng lẻ** (Project-level).<br>- Quản lý được yêu cầu, chi phí, tiến độ; **có thể lặp lại thành công** ở các dự án tương tự. |
| **Level 3** | **정의 (Defined)** | - Quy trình được chuẩn hóa và văn bản hóa ở **cấp độ toàn bộ tổ chức/công ty** (Organizational-level).<br>- Có tài liệu hướng dẫn quy chuẩn, công cụ hỗ trợ và chương trình đào tạo thống nhất. |
| **Level 4** | **정량적 관리 (Quantitatively Managed)** | - Quy trình và chất lượng sản phẩm được **đo lường bằng số liệu thống kê định lượng** (통계적, 정량적 측정).<br>- Dự báo được tỷ lệ phát sinh lỗi và kiểm soát dung sai chất lượng một cách khoa học. |
| **Level 5** | **최적화 (Optimizing)** | - Quy trình **liên tục được đổi mới và cải tiến** (지속적인 프로세스 개선) dựa trên phân tích số liệu định lượng và chủ động áp dụng các công nghệ tiên tiến. |

#### 4. Tiêu chuẩn đánh giá năng lực quy trình SPICE (ISO/IEC 15504)
SPICE là tiêu chuẩn quốc tế dùng để đánh giá và cải tiến năng lực của các tiến trình phần mềm, gồm 6 mức năng lực (Capability Levels):
- **Level 0 (불완전 - Incomplete):** Tiến trình chưa được thực hiện hoặc không đạt được mục đích của tiến trình.
- **Level 1 (수행 - Performed):** Tiến trình được thực hiện và tạo ra được các sản phẩm đầu ra xác định.
- **Level 2 (관리 - Managed):** Tiến trình được lập kế hoạch, theo dõi, điều chỉnh và các sản phẩm đầu ra được kiểm soát.
- **Level 3 (확립 - Established):** Tiến trình được triển khai dựa trên quy trình chuẩn đã được định nghĩa của tổ chức.
- **Level 4 (예측 - Predictable):** Tiến trình vận hành ổn định trong các giới hạn đo lường định lượng xác định.
- **Level 5 (최적화 - Optimizing):** Tiến trình liên tục cải tiến để đáp ứng các mục tiêu kinh doanh chiến lược của doanh nghiệp.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Phân biệt Kiểm tra đặc tả (Verification) và Kiểm tra người dùng (Validation)
Trong nhóm tiến trình hỗ trợ của ISO/IEC 12207:
- **검증 (Verification - "Xây dựng sản phẩm có đúng quy chuẩn không?"):**
  - Kiểm tra xem sản phẩm đầu ra của một giai đoạn có đáp ứng đúng tài liệu đặc tả yêu cầu đã đề ra ở giai đoạn trước đó hay không.
  - Mang tính chất kỹ thuật nội bộ (Internal technical check).
- **확인 (Validation - "Có xây dựng đúng sản phẩm khách hàng cần không?"):**
  - Kiểm tra xem sản phẩm cuối cùng sau khi hoàn thiện có đáp ứng đúng mục đích sử dụng thực tế và nhu cầu nghiệp vụ của khách hàng/người dùng cuối hay không.
  - Mang tính chất nghiệp vụ thực tế (Real-world user validation).

#### So sánh ranh giới giữa CMMI Level 2 và Level 3
- **Bẫy đề thi kinh điển:** Sự khác biệt sống còn giữa Level 2 và Level 3 nằm ở phạm vi áp dụng quy trình:
  - Nếu câu hỏi nhấn mạnh quy trình được quản lý ở **từng dự án cụ thể (프로젝트별)** $\rightarrow$ Chọn **Level 2 (관리 - Managed)**.
  - Nếu câu hỏi nhấn mạnh quy trình được chuẩn hóa ở **cấp toàn bộ tổ chức (조직 차원의 표준화)** $\rightarrow$ Chọn **Level 3 (정의 - Defined)**.

---

### 복습 체크리스트
- [ ] Phân loại chính xác 3 nhóm tiến trình ISO/IEC 12207: Cơ bản (기본: 획득, 공급, 개발, 운영, 유지보수); Hỗ trợ (지원: 문서화, 형상관리, QA, 검증, 확인); Tổ chức (조직: 관리, 기반구조, 훈련, 개선).
- [ ] Đọc tên 6 đặc tính chất lượng của ISO/IEC 9126: 기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성.
- [ ] Thuộc lòng 5 cấp độ CMMI theo khẩu quyết: **초-관-정-정-최** (초기, 관리, 정의, 정량적 관리, 최적화).
- [ ] Phân biệt được ranh giới CMMI: Level 2 là cấp dự án, Level 3 là chuẩn hóa cấp toàn công ty.
- [ ] Nhớ 6 cấp độ năng lực SPICE: Level 0 (불완전) $\rightarrow$ Level 5 (최적화).
