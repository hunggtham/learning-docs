# 210. CASE (Computer-Aided Software Engineering)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, nguồn gốc và vai trò của các công cụ kỹ nghệ phần mềm có máy tính trợ giúp (CASE - Computer-Aided Software Engineering) trong việc tự động hóa vòng đời SDLC.
- Hiểu cấu trúc và vai trò hạt nhân của kho lưu trữ thông tin tập trung (CASE Repository / 정보 저장소) trong việc đảm bảo tính toàn vẹn và nhất quán của dự án.
- Phân biệt chính xác 3 loại hình công cụ CASE theo phạm vi vòng đời: CASE thượng tầng (상위 CASE), CASE hạ tầng (하위 CASE), và CASE tích hợp toàn diện (통합 CASE).

## 핵심 키워드 (Từ khóa)
- CASE (Computer-Aided Software Engineering)
- 소프트웨어 생명주기 자동화 (SDLC Automation)
- CASE 정보 저장소 (Repository - Database 역할)
- 상위 CASE (Upper CASE - 요구분석 및 설계)
- 하위 CASE (Lower CASE - 코드 작성 및 테스트)
- 통합 CASE (Integrated CASE - 전 과정 지원)
- 개발 표준화 & 생산성 향상 (Standardization & Productivity)

## 선행·연결 개념 (Kiến thức liên kết)
- [67-bai-hoc.md](67-bai-hoc.md): Kỹ thuật tái công nghệ phần mềm (분재역이).
- [69-bai-hoc.md](69-bai-hoc.md): Framework phát triển máy chủ (Server Framework) và cơ chế IoC.
- [70-bai-hoc.md](70-bai-hoc.md): Nhận diện các lỗ hổng bảo mật phổ biến trong mã nguồn.

## 읽는 방법 (Cách đọc)
- Điểm mấu chốt khi giải các câu hỏi trắc nghiệm về công cụ CASE:
  - Khái niệm: Là phần mềm chuyên dụng **tự động hóa toàn bộ hoặc một phần các bước trong vòng đời phát triển phần mềm**.
  - Phân loại:
    - **상위 (Upper) CASE:** Giai đoạn đầu $\rightarrow$ **Yêu cầu (Requirements) và Thiết kế (Design)**.
    - **하위 (Lower) CASE:** Giai đoạn sau $\rightarrow$ **Viết mã (Coding) và Kiểm thử (Testing)**.
    - **통합 (Integrated) CASE:** Phủ khắp toàn bộ vòng đời.
  - Hạt nhân thông tin: Mọi công cụ CASE đều tương tác xung quanh một cơ sở dữ liệu chung gọi là **Repository (정보 저장소)** để bảo đảm các sơ đồ UML và code luôn đồng bộ.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Lợi ích vượt trội khi áp dụng công cụ CASE:**
  - Tự động hóa các tác vụ lặp lại (vẽ sơ đồ, kiểm tra cú pháp, sinh mã khung sườn, tạo tài liệu).
  - Rút ngắn thời gian bàn giao dự án và tiết kiệm chi phí nhân công.
  - Chuẩn hóa toàn bộ quy trình làm việc theo các tiêu chuẩn kỹ thuật thống nhất.
  - Duy trì tính nhất quán giữa tài liệu phân tích nghiệp vụ, bản vẽ thiết kế và mã nguồn thực tế.

- **2. Bảng phân loại công cụ CASE theo giai đoạn SDLC:**

| Phân loại | Giai đoạn SDLC hỗ trợ | Chức năng kỹ thuật chủ đạo | Ví dụ công cụ thực tế |
| :--- | :--- | :--- | :--- |
| **상위 CASE** (Upper CASE) | **Phân tích yêu cầu & Thiết kế** (Requirements & Design) | Hỗ trợ thu thập yêu cầu người dùng, vẽ biểu đồ luồng dữ liệu (DFD), sơ đồ UML, mô hình hóa dữ liệu E-R, kiểm tra tính logic của kiến trúc. | StarUML, Enterprise Architect, IBM Rational Rose |
| **하위 CASE** (Lower CASE) | **Cài đặt & Kiểm thử** (Implementation & Testing) | Tự động sinh mã nguồn (Code Generation), kiểm tra chuẩn cú pháp tĩnh, quản lý ca kiểm thử, đo độ bao phủ mã (Coverage). | JUnit, PMD, SonarQube, Eclipse IDE |
| **통합 CASE** (Integrated CASE) | **Toàn bộ vòng đời** (Full SDLC) | Kết nối liền mạch từ phân tích, thiết kế, sinh mã đến kiểm thử và bảo trì thông qua một kho lưu trữ chung. | IBM Engineering Lifecycle Management |

- **3. Vai trò của CASE Repository (정보 저장소):**
  - Đóng vai trò như một cơ sở dữ liệu trung tâm chứa toàn bộ thông tin sản phẩm phần mềm qua từng giai đoạn: Từ điển dữ liệu (Data Dictionary), quy tắc nghiệp vụ, định nghĩa thực thể, sơ đồ quan hệ và nhật ký thay đổi.
  - Ngăn ngừa tình trạng sai lệch thông tin khi nhiều kỹ sư cùng tham gia phát triển một phân hệ lớn.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hạn chế của công cụ CASE:**
  - Chi phí đầu tư bản quyền ban đầu và chi phí đào tạo nhân lực rất lớn.
  - Nếu kỹ sư không nắm vững nguyên lý kỹ nghệ phần mềm thì công cụ CASE không thể tự động sửa các lỗi tư duy logic nghiệp vụ sai lệch từ ban đầu.

### 복습 체크리스트
- [ ] Ghi nhớ định nghĩa CASE: Phần mềm tự động hóa các khâu trong vòng đời phần mềm.
- [ ] Phân biệt chính xác: 상위 CASE (Yêu cầu & Thiết kế) vs 하위 CASE (Viết mã & Kiểm thử).
- [ ] Nhớ tên thành phần hạt nhân lưu trữ dữ liệu chung của CASE: **Repository (정보 저장소)**.
- [ ] Nắm được lợi ích lớn nhất của CASE là chuẩn hóa chu trình và nâng cao năng suất phát triển.
