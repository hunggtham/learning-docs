# 소프트웨어 프로세스 품질 및 성숙도 표준 (Quality & Maturity Standards)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống các tiêu chuẩn quốc tế về chất lượng quy trình phần mềm và mô hình trưởng thành năng lực: **ISO/IEC 12207**, **CMMI**, và **SPICE (ISO/IEC 15504)**.
- Phân biệt chi tiết 3 nhóm tiến trình vòng đời theo ISO/IEC 12207: Tiến trình cơ bản (기본 프로세스), Tiến trình hỗ trợ (지원 프로세스), và Tiến trình tổ chức (조직 프로세스).
- Thuộc lòng 5 cấp độ trưởng thành của mô hình CMMI theo khẩu quyết **초관정정최** (Initial, Managed, Defined, Quantitatively Managed, Optimizing) và 6 cấp độ năng lực của SPICE (Level 0 đến Level 5).

## 핵심 키워드 (Từ khóa)
- 프로세스 품질 표준 (Process Quality Standards)
- ISO/IEC 12207 (기본, 지원, 조직 프로세스)
- CMMI 성숙도 5단계 (초기, 관리, 정의, 정량적 관리, 최적화)
- CMMI 암기 공식 (초관정정최)
- SPICE / ISO/IEC 15504 (수행 능력 6단계)
- 형상 관리 & 품질 보증 (SCM & QA in Supporting Lifecycle)

## 선행·연결 개념 (Kiến thức liên kết)
- [10-bai-hoc.md](10-bai-hoc.md): Nền tảng các tiêu chuẩn chất lượng quy trình phát triển phần mềm.
- [12-bai-hoc.md](12-bai-hoc.md): Đại cương truyền thông dữ liệu và các hệ thống viễn thông lịch sử.
- [09-bai-hoc.md](09-bai-hoc.md): Kỹ thuật ước lượng toán học COCOMO, Putnam và Function Point.

## 읽는 방법 (Cách đọc)
- Điểm mấu chốt khi giải bài thi phần tiêu chuẩn chất lượng:
  - **ISO/IEC 12207:** Phân biệt đúng nhóm tiến trình:
    - *Tiến trình cơ bản (기본):* 획득 (Mua), 공급 (Cung cấp), 개발 (Phát triển), 운영 (Vận hành), 유지보수 (Bảo trì).
    - *Tiến trình hỗ trợ (지원):* 문서화 (Tài liệu), 형상 관리 (Quản lý cấu hình), 품질 보증 (QA), 검증 (Verification), 확인 (Validation).
    - *Tiến trình tổ chức (조직):* 관리 (Management), 기반 구조 (Cơ sở hạ tầng), 훈련 (Đào tạo), 개선 (Cải tiến).
  - **CMMI:** Khẩu quyết 5 cấp độ:
    $$\mathbf{초 \rightarrow 관 \rightarrow 정 \rightarrow 정 \rightarrow 최}$$
    - Level 1: 초기 (Initial) $\rightarrow$ Level 2: 관리 (Managed) $\rightarrow$ Level 3: 정의 (Defined) $\rightarrow$ Level 4: 정량적 관리 (Quantitatively Managed) $\rightarrow$ Level 5: 최적화 (Optimizing).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân loại 3 nhóm tiến trình vòng đời phần mềm theo ISO/IEC 12207:**

| Nhóm tiến trình | Tên tiếng Hàn & Anh | Các tiến trình thành phần cụ thể |
| :--- | :--- | :--- |
| **Tiến trình cơ bản** (Primary Process) | **기본 프로세스** | **획득** (Acquisition), **공급** (Supply), **개발** (Development), **운영** (Operation), **유지보수** (Maintenance). |
| **Tiến trình hỗ trợ** (Supporting Process) | **지원 프로세스** | **문서화** (Documentation), **형상 관리** (Configuration Management), **품질 보증** (Quality Assurance), **검증** (Verification), **확인** (Validation), **합동 검토** (Joint Review), **감사** (Audit), **문제 해결** (Problem Resolution). |
| **Tiến trình tổ chức** (Organizational Process) | **조직 프로세스** | **관리** (Management), **기반 구조** (Infrastructure), **훈련** (Training), **개선** (Improvement). |

- **2. Bảng đối chiếu 5 cấp độ trưởng thành CMMI vs 6 cấp độ năng lực SPICE:**

| Cấp độ | CMMI (Capability Maturity Model Integration) | SPICE (ISO/IEC 15504 Capability Levels) |
| :---: | :--- | :--- |
| **0** | *(Không có cấp 0 trong mô hình bậc CMMI Staged)* | **불완전 (Incomplete):** Quy trình chưa thực hiện hoặc thất bại. |
| **1** | **초기 (Initial):** Quy trình hỗn loạn, vô kỷ luật, thành công phụ thuộc vào nỗ lực cá nhân anh hùng. | **수행 (Performed):** Quy trình được thực hiện và tạo ra sản phẩm. |
| **2** | **관리 (Managed):** Quy trình được thiết lập và quản lý ở cấp độ **từng dự án cụ thể**. | **관리 (Managed):** Quy trình được lập kế hoạch và giám sát theo dõi. |
| **3** | **정의 (Defined):** Quy trình được chuẩn hóa và văn bản hóa ở cấp độ **toàn bộ tổ chức/doanh nghiệp**. | **확립 (Established):** Quy trình được định nghĩa dựa trên tiêu chuẩn tổ chức. |
| **4** | **정량적 관리 (Quantitatively Managed):** Đo lường và kiểm soát quy trình bằng **số liệu thống kê định lượng**. | **예측 (Predictable):** Quy trình vận hành ổn định trong giới hạn định lượng. |
| **5** | **최적화 (Optimizing):** Quy trình được **liên tục cải tiến và tối ưu hóa** thông qua đổi mới công nghệ. | **최적화 (Optimizing):** Quy trình liên tục cải tiến để đáp ứng mục tiêu tương lai. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự khác biệt giữa CMMI Staged Representation và Continuous Representation:**
  - *Mô hình theo giai đoạn (Staged):* Đánh giá mức độ trưởng thành (Maturity Level) của toàn bộ doanh nghiệp từ Cấp 1 đến Cấp 5 (được dùng phổ biến nhất trong các bài thi và đấu thầu dự án).
  - *Mô hình liên tục (Continuous):* Đánh giá mức độ năng lực (Capability Level) của từng vùng quy trình nghiệp vụ riêng lẻ (Process Area) từ Cấp 0 đến Cấp 3.

### 복습 체크리스트
- [ ] Phân biệt chính xác 3 nhóm tiến trình của ISO/IEC 12207: Cơ bản, Hỗ trợ, Tổ chức.
- [ ] Thuộc lòng 5 cấp độ CMMI theo khẩu quyết: **초관정정최** (초기, 관리, 정의, 정량적 관리, 최적화).
- [ ] Ghi nhớ tiêu chuẩn SPICE có 6 cấp độ từ 0 (불완전) đến 5 (최적화).
- [ ] Nhớ CMMI cấp 3 là chuẩn hóa toàn tổ chức, cấp 4 là đo lường định lượng bằng thống kê.
