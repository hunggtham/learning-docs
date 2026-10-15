# 4. 프로세스 품질 표준 (Tiêu chuẩn chất lượng quy trình)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc và sự phân loại của các bộ tiêu chuẩn quốc tế về quy trình chất lượng phần mềm: **ISO/IEC 12207**, mô hình trưởng thành năng lực **CMMI**, và tiêu chuẩn đánh giá năng lực quy trình **SPICE (ISO/IEC 15504)**.
- Phân biệt 3 nhóm chu kỳ vòng đời phần mềm theo ISO/IEC 12207: Chu kỳ cơ bản (기본 생명 주기), Chu kỳ hỗ trợ (지원 생명 주기), và Chu kỳ tổ chức (조직 생명 주기).
- Thuộc lòng 5 cấp độ trưởng thành của CMMI theo khẩu quyết **초관정정최** (Initial, Managed, Defined, Quantitatively Managed, Optimizing) và 6 cấp độ năng lực của SPICE (Cấp 0 đến Cấp 5).

## 핵심 키워드 (Từ khóa)
- 프로세스 품질 표준 (Process Quality Standards)
- ISO/IEC 12207 (기본, 지원, 조직 생명 주기)
- CMMI 5단계 (초기, 관리, 정의, 정량적 관리, 최적화)
- CMMI 암기 공식 (초관정정최 - IMDQO)
- SPICE / ISO/IEC 15504 (불완전, 수행, 관리, 확립, 예측, 최적화)
- 검증 (Verification) vs 확인 (Validation)
- 프로세스 지속적 개선 (Continuous Process Improvement)

## 선행·연결 개념 (Kiến thức liên kết)
- [09-bai-hoc.md](09-bai-hoc.md): Kỹ thuật ước lượng toán học COCOMO, Putnam và FP.
- [11-bai-hoc.md](11-bai-hoc.md): Quản lý cấu hình phần mềm (SCM) và các tiêu chuẩn bảo mật.
- [08-bai-hoc.md](08-bai-hoc.md): Tổng quan các phương pháp ước tính chi phí dự án.

## 읽는 방법 (Cách đọc)
- Các điểm then chốt bắt buộc phải thuộc làu khi đi thi:
  - **ISO/IEC 12207:** Phải phân biệt rõ các tiến trình thuộc:
    - *기본 (Cơ bản):* 획득 (Mua), 공급 (Bán), 개발 (Code/Dev), 운영 (Vận hành), 유지보수 (Bảo trì).
    - *지원 (Hỗ trợ):* 문서화 (Tài liệu), 형상관리 (SCM), 품질보증 (QA), 검증 (Verification), 확인 (Validation).
    - *조직 (Tổ chức):* 관리 (Management), 기반구조 (Infrastructure), 훈련 (Training), 개선 (Improvement).
  - **CMMI 5 cấp độ:** Khẩu quyết bất hủ:
    $$\mathbf{초 \rightarrow 관 \rightarrow 정 \rightarrow 정 \rightarrow 최}$$
    - Level 1: **초**기 (Initial - Hỗn loạn, cá nhân phụ thuộc).
    - Level 2: **관**리 (Managed - Quản lý ở cấp dự án).
    - Level 3: **정**의 (Defined - Chuẩn hóa toàn tổ chức).
    - Level 4: **정**량적 관리 (Quantitatively Managed - Đo bằng thống kê).
    - Level 5: **최**적화 (Optimizing - Liên tục cải tiến).
  - **SPICE (ISO/IEC 15504):** Bắt đầu từ Cấp 0 (불완전 - Incomplete) đến Cấp 5 (최적화 - Optimizing).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân loại chu kỳ vòng đời phần mềm theo chuẩn ISO/IEC 12207:**

| Nhóm chu kỳ vòng đời | Tên tiếng Hàn & Anh | Các tiến trình kỹ thuật thành phần |
| :--- | :--- | :--- |
| **Chu kỳ cơ bản** (Primary Life Cycle) | **기본 생명 주기** | **획득** (Acquisition - Mua/Thu nạp), **공급** (Supply - Cung ứng), **개발** (Development - Phát triển), **운영** (Operation - Vận hành), **유지보수** (Maintenance - Bảo trì). |
| **Chu kỳ hỗ trợ** (Supporting Life Cycle) | **지원 생명 주기** | **문서화** (Documentation), **형상 관리** (Configuration Management), **품질 보증** (Quality Assurance), **검증** (Verification), **확인** (Validation), **합동 검토** (Joint Review), **감사** (Audit), **문제 해결** (Problem Resolution). |
| **Chu kỳ tổ chức** (Organizational Life Cycle) | **조직 생명 주기** | **관리** (Management), **기반 구조** (Infrastructure), **훈련** (Training), **개선** (Improvement). |

- **2. Bảng 5 cấp độ trưởng thành của mô hình CMMI (초관정정최):**

| Cấp độ CMMI | Tên cấp độ (KR / EN) | Đặc trưng thực tế của tổ chức phần mềm |
| :---: | :--- | :--- |
| **Cấp 1** | **초기 (Initial)** | Quy trình hoàn toàn hỗn loạn (Ad-hoc), thiếu kỷ luật; thành bại của dự án phụ thuộc 100% vào sự hy sinh cá nhân của một vài lập trình viên anh hùng (Heroics). |
| **Cấp 2** | **관리 (Managed)** | Đã thiết lập được quy trình quản lý cơ bản ở cấp độ **từng dự án riêng lẻ** (ước tính chi phí, lập lịch, kiểm soát thay đổi); có thể lặp lại thành công cho các dự án tương tự. |
| **Cấp 3** | **정의 (Defined)** | Toàn bộ quy trình công nghệ và quản lý đã được văn bản hóa, chuẩn hóa và áp dụng đồng bộ ở cấp độ **toàn công ty/toàn tổ chức** (Enterprise Standard Process). |
| **Cấp 4** | **정량적 관리 (Quantitatively Managed)** | Quy trình và chất lượng sản phẩm được **đo lường, kiểm soát chặt chẽ bằng các chỉ số thống kê toán học định lượng** (Metrics / Statistical Process Control). |
| **Cấp 5** | **최적화 (Optimizing)** | Tổ chức liên tục cải tiến và đổi mới quy trình dựa trên dữ liệu định lượng và thử nghiệm các công nghệ phần mềm tiên tiến nhất. |

- **3. Bảng 6 cấp độ năng lực của tiêu chuẩn SPICE (ISO/IEC 15504):**

| Cấp độ SPICE | Tên cấp độ năng lực | Mô tả trạng thái năng lực quy trình |
| :---: | :--- | :--- |
| **0단계** | **불완전 (Incomplete)** | Quy trình chưa được thực hiện hoặc không đạt được mục tiêu cơ bản đặt ra. |
| **1단계** | **수행 (Performed)** | Quy trình được thực hiện và tạo ra sản phẩm đầu ra được công nhận. |
| **2단계** | **관리 (Managed)** | Quy trình được lập kế hoạch, giám sát và điều chỉnh theo lịch trình. |
| **3단계** | **확립 (Established)** | Quy trình được định nghĩa dựa trên tiêu chuẩn quy trình của tổ chức. |
| **4단계** | **예측 (Predictable)** | Quy trình vận hành ổn định trong các giới hạn định lượng được xác định từ trước. |
| **5단계** | **최적화 (Optimizing)** | Quy trình liên tục được hoàn thiện để đáp ứng các mục tiêu nghiệp vụ tương lai. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phân biệt rạch ròi: Kiểm chứng (Verification) vs Xác thực (Validation):**
  - **검증 (Verification - Kiểm chứng):** *"Are we building the product right?"* – Kiểm tra xem sản phẩm có được xây dựng đúng theo đúng bản vẽ thiết kế kỹ thuật hay không (Tập trung vào tính chuẩn mực của quy trình và mã nguồn, do lập trình viên/đội QA làm).
  - **확인 (Validation - Xác thực):** *"Are we building the right product?"* – Kiểm tra xem sản phẩm hoàn thiện có thực sự giải quyết đúng bài toán nghiệp vụ và đáp ứng mong đợi của người dùng hay không (Tập trung vào mục đích sử dụng cuối cùng, do khách hàng/người dùng làm).

### 복습 체크리스트
- [ ] Phân loại được các tiến trình của ISO/IEC 12207: Cơ bản (Phát triển, Vận hành), Hỗ trợ (QA, SCM, Tài liệu), Tổ chức (Đào tạo, Cải tiến).
- [ ] Đọc vanh vách 5 cấp độ CMMI theo khẩu quyết: **초관정정최** (초기, 관리, 정의, 정량적 관리, 최적화).
- [ ] Nhớ SPICE (ISO/IEC 15504) có 6 cấp độ từ 0 (불완전) đến 5 (최적화).
- [ ] Phân biệt được: Verification (Làm đúng thiết kế) vs Validation (Làm đúng nhu cầu người dùng).
