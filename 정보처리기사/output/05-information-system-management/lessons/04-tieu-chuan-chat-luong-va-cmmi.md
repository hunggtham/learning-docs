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
| **Tiến trình cơ bản** | **기본 생명 주기 (Primary Processes)** | 5 tiến trình cốt lõi tạo ra và vận hành sản phẩm: Mua sắm (획득), Cung cấp (공급), Phát triển (개발), Vận hành (운영), Bảo trì (유지보수). |
| **Tiến trình hỗ trợ** | **지원 생명 주기 (Supporting Processes)** | Các hoạt động phụ trợ độc lập: Lập tài liệu (문서화), Quản lý cấu hình (형상 관리), Đảm bảo chất lượng (품질 보증), Kiểm tra đặc tả (검증), Kiểm tra người dùng (확인), Đánh giá liên tịch (합동 검토), Kiểm toán (감사), Xử lý sự cố (문제 해결). |
| **Tiến trình tổ chức** | **조직 생명 주기 (Organizational Processes)** | Hoạt động xây dựng năng lực cấp doanh nghiệp: Quản lý (관리), Hạ tầng cơ sở (기반 구조), Đào tạo kỹ năng (훈련), Cải tiến quy trình (개선). |

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
| **Level 1** | **초기 (Initial)** | Quy trình hỗn loạn, tự phát, không chuẩn mực; thành công phụ thuộc hoàn toàn vào nỗ lực của cá nhân anh hùng (영웅적 개인). Không thể dự báo chi phí và chất lượng. |
| **Level 2** | **관리 (Managed)** | Thiết lập quy trình quản lý cơ bản ở cấp độ từng dự án riêng lẻ (Project-level); kiểm soát được yêu cầu, chi phí, tiến độ; có khả năng lặp lại thành công cho các dự án tương tự. |
| **Level 3** | **정의 (Defined)** | Quy trình được chuẩn hóa và văn bản hóa ở cấp toàn bộ tổ chức/công ty (Organizational-level); có tài liệu quy chuẩn, công cụ hỗ trợ và chương trình đào tạo thống nhất. |
| **Level 4** | **정량적 관리 (Quantitatively Managed)** | Quy trình và chất lượng sản phẩm được đo lường bằng số liệu thống kê định lượng (통계적, 정량적 측정); dự báo được tỷ lệ phát sinh lỗi và kiểm soát dung sai chất lượng. |
| **Level 5** | **최적화 (Optimizing)** | Quy trình liên tục được đổi mới và cải tiến (지속적인 프로세스 개선) dựa trên phân tích số liệu định lượng và chủ động áp dụng công nghệ mới. |

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

#### 1. Biểu đồ hình tháp 5 cấp độ trưởng thành CMMI (초-관-정-정-최)
Mô hình CMMI biểu diễn theo giai đoạn (Staged Representation) phân cấp độ trưởng thành năng lực của toàn bộ doanh nghiệp theo cấu trúc hình tháp bậc thang từ thấp lên cao:

```text
                       /=========================================\
                      /           Level 5: 최적화 (Optimizing)    \
                     /    Liên tục cải tiến quy trình & công nghệ  \
                    /===============================================\
                   /       Level 4: 정량적 관리 (Quantitatively)     \
                  /      Kiểm soát quy trình bằng số liệu thống kê   \
                 /=====================================================\
                /                 Level 3: 정의 (Defined)                \
               /         Quy trình chuẩn hóa cấp toàn bộ tổ chức/công ty   \
              /=============================================================\
             /                   Level 2: 관리 (Managed)                      \
            /          Quản lý quy trình ở cấp độ từng dự án riêng lẻ           \
           /===================================================================\
          /                     Level 1: 초기 (Initial)                          \
         /      Hỗn loạn, không quy trình chuẩn, dựa vào cá nhân anh hùng         \
        /=========================================================================\
```

- **Phân tích kỹ thuật và bẫy đề thi theo từng tầng tháp:**
  - **Level 1 (초기 - Initial):** Không có chuẩn mực. Nếu lập trình viên giỏi rời đi, dự án lập tức thất bại. Chi phí và thời gian luôn bị vượt trần.
  - **Level 2 (관리 - Managed):** Trọng tâm là quản trị dự án (Project Management). Đã kiểm soát được phạm vi yêu cầu (REQM), lập kế hoạch (PP), theo dõi tiến độ (PMC), quản lý cấu hình (CM). Có thể lặp lại thành công ở dự án tương tự, nhưng mỗi dự án vẫn có thể làm việc theo cách riêng.
  - **Level 3 (정의 - Defined):** Toàn công ty thống nhất dùng chung một bộ quy trình chuẩn (Standard Process). Có bộ phận đảm bảo chất lượng độc lập, tài liệu hướng dẫn kỹ thuật chi tiết và chương trình đào tạo nội bộ bài bản.
  - **Level 4 (정량적 관리 - Quantitatively Managed):** Áp dụng kỹ thuật kiểm soát quy trình bằng thống kê (SPC - Statistical Process Control). Đo lường năng suất, mật độ lỗi trên từng KLOC và dự báo được chất lượng sản phẩm bằng con số cụ thể.
  - **Level 5 (최적화 - Optimizing):** Doanh nghiệp chủ động phân tích nguyên nhân gốc rễ của sai lỗi (Causal Analysis) và đầu tư thử nghiệm các công nghệ, công cụ mới để liên tục tối ưu hóa quy trình.

#### 2. Hai cách tiếp cận biểu diễn trong CMMI (Staged vs Continuous)
- **Mô hình theo giai đoạn (Staged Representation):**
  - Đánh giá toàn diện tổ chức theo **5 mức độ trưởng thành (Maturity Levels 1 ~ 5)**.
  - Doanh nghiệp phải đạt tất cả các mục tiêu của mức hiện tại mới được công nhận lên mức kế tiếp.
- **Mô hình liên tục (Continuous Representation):**
  - Đánh giá năng lực của **từng lĩnh vực quy trình riêng lẻ (Capability Levels 0 ~ 3)**:
    - Level 0 (Incomplete): Chưa hoàn thành.
    - Level 1 (Performed): Đã thực hiện.
    - Level 2 (Managed): Đã quản lý.
    - Level 3 (Defined): Đã định nghĩa chuẩn hóa.
  - Giúp doanh nghiệp linh hoạt tập trung cải thiện trước các quy trình đang là điểm nghẽn mà không cần nâng cấp đồng loạt.

#### 3. Bộ tiêu chuẩn SPICE (ISO/IEC 15504) và Kiến trúc 2 chiều
SPICE (Software Process Improvement and Capability dEtermination) là khung đánh giá năng lực tiến trình quốc tế do ISO/IEC ban hành:

- **Sơ đồ kiến trúc 2 chiều của SPICE:**

```text
+---------------------------------------------------------------------------------------+
|                 MÔ HÌNH 2 CHIỀU CỦA TIÊU CHUẨN SPICE (ISO/IEC 15504)                  |
+---------------------------------------------------------------------------------------+
| [ CHIỀU NĂNG LỰC - Capability Dimension ]                                             |
| Level 5: 최적화 (Optimizing)    -> PA 5.1 (Cải tiến liên tục), PA 5.2 (Tối ưu hóa)     |
| Level 4: 예측 (Predictable)     -> PA 4.1 (Đo lường định lượng), PA 4.2 (Kiểm soát)    |
| Level 3: 확립 (Established)     -> PA 3.1 (Định nghĩa quy trình), PA 3.2 (Triển khai)  |
| Level 2: 관리 (Managed)         -> PA 2.1 (Quản lý thực thi), PA 2.2 (Sản phẩm đầu ra)|
| Level 1: 수행 (Performed)       -> PA 1.1 (Thực thi tiến trình tạo ra kết quả)        |
| Level 0: 불완전 (Incomplete)    -> Không thực hiện hoặc không đạt được mục tiêu cơ bản|
+---------------------------------------------------------------------------------------+
                                           ^
                                           |  Đánh giá chéo từng tiến trình
                                           v
+---------------------------------------------------------------------------------------+
| [ CHIỀU TIẾN TRÌNH - Process Dimension ] (Kế thừa từ chuẩn ISO/IEC 12207)             |
| 1. CUS: Nhóm khách hàng - Nhà cung cấp (Customer - Supplier Process Category)         |
| 2. ENG: Nhóm kỹ thuật công nghệ phần mềm (Engineering Process Category)               |
| 3. SUP: Nhóm hỗ trợ đảm bảo chất lượng (Support Process Category)                     |
| 4. MAN: Nhóm quản lý dự án và nhân lực (Management Process Category)                  |
| 5. ORG: Nhóm tổ chức và hạ tầng doanh nghiệp (Organization Process Category)          |
+---------------------------------------------------------------------------------------+
```

- **Bảng đối chiếu tương đương giữa cấp độ CMMI và SPICE:**

| Cấp độ | CMMI (Staged Maturity Level) | SPICE / ISO 15504 (Capability Level) | Đặc trưng cốt lõi |
| :---: | :--- | :--- | :--- |
| **0** | *(Không có)* | **Level 0: 불완전 (Incomplete)** | Tiến trình thất bại, không tạo ra sản phẩm. |
| **1** | **Level 1: 초기 (Initial)** | **Level 1: 수행 (Performed)** | Đạt mục tiêu cơ bản, dựa vào nỗ lực cá nhân. |
| **2** | **Level 2: 관리 (Managed)** | **Level 2: 관리 (Managed)** | Quản lý tốt ở cấp dự án đơn lẻ, có thể lặp lại. |
| **3** | **Level 3: 정의 (Defined)** | **Level 3: 확립 (Established)** | Quy trình chuẩn hóa thành văn bản cấp toàn công ty. |
| **4** | **Level 4: 정량적 관리 (Quantitatively)** | **Level 4: 예측 (Predictable)** | Kiểm soát và dự báo bằng số liệu thống kê định lượng. |
| **5** | **Level 5: 최적화 (Optimizing)** | **Level 5: 최적화 (Optimizing)** | Liên tục cải tiến và tối ưu hóa công nghệ quy trình. |

#### 4. Phân biệt Kiểm tra đặc tả (Verification) và Kiểm tra người dùng (Validation)
Trong nhóm tiến trình hỗ trợ của ISO/IEC 12207:
- **검증 (Verification - "Xây dựng sản phẩm có đúng quy chuẩn không?"):**
  - Kiểm tra xem sản phẩm đầu ra của một giai đoạn có đáp ứng đúng tài liệu đặc tả yêu cầu đã đề ra ở giai đoạn trước đó hay không.
  - Mang tính chất kỹ thuật nội bộ (Internal technical check).
- **확인 (Validation - "Có xây dựng đúng sản phẩm khách hàng cần không?"):**
  - Kiểm tra xem sản phẩm cuối cùng sau khi hoàn thiện có đáp ứng đúng mục đích sử dụng thực tế và nhu cầu nghiệp vụ của khách hàng/người dùng cuối hay không.
  - Mang tính chất nghiệp vụ thực tế (Real-world user validation).

#### 5. So sánh ranh giới giữa CMMI Level 2 và Level 3
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
- [ ] Nắm vững kiến trúc 2 chiều của SPICE: Chiều quy trình (CUS, ENG, SUP, MAN, ORG) và Chiều năng lực (Level 0-5).
