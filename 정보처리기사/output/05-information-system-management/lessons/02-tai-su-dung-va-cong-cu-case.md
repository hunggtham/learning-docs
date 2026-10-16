# 소프트웨어 재사용, 재공학 & CASE 도구 (Tái sử dụng, Tái kỹ nghệ phần mềm & Công cụ CASE)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, ý nghĩa kinh tế và các lợi ích cốt lõi của Tái sử dụng phần mềm (소프트웨어 재사용 - Software Reuse).
- Phân biệt bản chất kỹ thuật của hai phương pháp tiếp cận tái sử dụng: Tiếp cận dựa trên tổng hợp (합성 중심 - Synthesis / Composition-based) và Tiếp cận dựa trên phân tích/sinh mã (생성 중심 - Analysis / Generation-based).
- Thấu hiểu mục tiêu của Tái kỹ nghệ phần mềm (소프트웨어 재공학 - Software Reengineering) và các hoạt động cốt lõi: Phân tích (분석), Tái cấu trúc (재구성), Kỹ nghệ ngược (역공학), Kỹ nghệ xuôi (순공학), và Di chuyển nền tảng (이식).
- Phân loại toàn diện các công cụ hỗ trợ công nghệ phần mềm bằng máy tính (CASE: 상위 CASE, 하위 CASE, 통합 CASE) và vai trò hạt nhân của Kho lưu trữ trung tâm (중앙 저장소 - Central Repository).

## 핵심 키워드 (Từ khóa song ngữ)
- 소프트웨어 재사용 (Software Reuse — Tái sử dụng tài sản phần mềm đã kiểm chứng)
- 합성 중심 (Synthesis / Composition-Based — Lắp ghép module, component có sẵn như khối Lego)
- 생성 중심 (Analysis / Generation-Based — Phân tích mẫu đặc tả và sinh mã nguồn tự động)
- 소프트웨어 재공학 (Software Reengineering — Nâng cao tính bảo trì của hệ thống cũ)
- 역공학 (Reverse Engineering — Khôi phục tài liệu thiết kế/đặc tả từ mã nguồn có sẵn)
- 재구성 (Restructuring — Tối ưu hóa cấu trúc bên trong mà không thay đổi chức năng ngoài)
- 순공학 (Forward Engineering — Phát triển tính năng mới từ mô hình đã tái cấu trúc)
- 이식 (Migration — Chuyển đổi hệ thống sang nền tảng phần cứng/HĐH mới)
- CASE 도구 (Computer Aided Software Engineering — Tự động hóa các pha trong vòng đời SDLC)
- 상위 CASE (Upper CASE — Hỗ trợ pha kế hoạch, phân tích yêu cầu, thiết kế kiến trúc)
- 하위 CASE (Lower CASE — Hỗ trợ pha viết mã, kiểm thử, bảo trì)
- 통합 CASE (Integrated CASE / I-CASE — Bao phủ toàn bộ vòng đời SDLC)
- 중앙 저장소 (Central Repository — Kho lưu trữ tập trung bảo đảm tính nhất quán của CASE)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi xác định phương pháp luận phát triển (CBD, Agile) từ bài học [01-phuong-phap-luan-va-framework.md](01-phuong-phap-luan-va-framework.md), doanh nghiệp không bắt đầu viết mã từ con số không mà tận dụng tài sản trí tuệ sẵn có.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết bài toán nâng cao năng suất, cắt giảm chi phí bảo trì và hiện đại hóa các hệ thống cũ (Legacy Systems) thông qua kỹ thuật tái sử dụng, quy trình tái kỹ nghệ và bộ công cụ tự động hóa CASE.
- **Dùng đi đâu (Forward Handoff):** Các chỉ số tái sử dụng và mức độ tự động hóa của công cụ CASE là tham số đầu vào trực tiếp để tính toán chi phí, công số nhân tháng (Man-Month) và tiến độ dự án trong [03-quan-ly-du-an-chi-phi-va-tien-do.md](03-quan-ly-du-an-chi-phi-va-tien-do.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Tái sử dụng (Software Reuse):**
  - Nhắc đến **"블록(부품)을 조립" (Lắp ghép khối/linh kiện có sẵn)** $\rightarrow$ Chọn **합성 중심 (Synthesis / Composition-based)**.
  - Nhắc đến **"추상화된 명세/패턴을 바탕으로 소스 코드를 생성" (Phân tích đặc tả và sinh mã tự động)** $\rightarrow$ Chọn **생성 중심 (Analysis / Generation-based)**.
- **Tái kỹ nghệ (Reengineering) vs Kỹ nghệ ngược (Reverse Engineering):**
  - Đề hỏi: *"Mục đích chính của 재공학 là gì?"* $\rightarrow$ Đáp án đúng luôn xoay quanh: **유지보수성 향상 (Nâng cao tính bảo trì)** và **유지보수 비용 절감 (Giảm chi phí bảo trì)**.
  - Đề hỏi: *"Phục hồi tài liệu thiết kế, sơ đồ hoặc đặc tả từ mã nguồn phần mềm cũ là hoạt động gì?"* $\rightarrow$ Đáp án đúng là **역공학 (Reverse Engineering / Kỹ nghệ ngược)**.
  - Nhớ các hoạt động của 재공학: **분석 (Phân tích) $\rightarrow$ 재구성 (Tái cấu trúc) $\rightarrow$ 역공학 (Kỹ nghệ ngược) $\rightarrow$ 순공학 (Kỹ nghệ xuôi) / 이식 (Di chuyển nền tảng)**.
- **Công cụ CASE:**
  - Pha đầu (Kế hoạch, Phân tích, Thiết kế kiến trúc) $\rightarrow$ **상위 CASE (Upper CASE)**.
  - Pha sau (Viết code, Kiểm thử, Tài liệu hóa, Bảo trì) $\rightarrow$ **하위 CASE (Lower CASE)**.
  - Xuyên suốt toàn bộ chu trình sống SDLC $\rightarrow$ **통합 CASE (Integrated CASE)**.
  - Trái tim duy trì tính toàn vẹn và nhất quán của CASE $\rightarrow$ **중앙 저장소 (Central Repository)**.

---

## 소프트웨어 재사용, 재공학 & CASE 도구

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Tái sử dụng phần mềm (소프트웨어 재사용 - Software Reuse)
- **개념 (Khái niệm):** Quá trình tận dụng lại các tri thức, kinh nghiệm, mã nguồn, module, tài liệu thiết kế hoặc kiến trúc phần mềm đã được phát triển và kiểm chứng trước đó vào một dự án mới.
- **Lợi ích chiến lược:**
  - `개발 시간 단축 및 개발 비용 절감` — Rút ngắn thời gian phát triển từ 30% đến 50%, giảm đáng kể chi phí nhân lực.
  - `소프트웨어 품질 및 신뢰성 향상` — Tăng độ tin cậy và chất lượng do các thành phần tái sử dụng đã được kiểm thử và chạy ổn định trong thực tế.
  - `프로젝트 위험 감소 및 표준화 촉진` — Giảm thiểu rủi ro thất bại dự án, thúc đẩy chuẩn hóa quy trình công nghệ trong doanh nghiệp.
- **Đối chiếu 2 phương pháp tiếp cận tái sử dụng:**

| Tiêu chí | Tiếp cận dựa trên tổng hợp (합성 중심) | Tiếp cận dựa trên phân tích/sinh mã (생성 중심) |
| :--- | :--- | :--- |
| **Tên tiếng Hàn & Anh** | **합성 중심 (Synthesis / Composition-Based)** | **생성 중심 (Analysis / Generation-Based)** |
| **Cơ chế kỹ thuật** | Lắp ghép và tích hợp các khối thành phần (Software Blocks / Components) có sẵn trong kho lưu trữ thành hệ thống hoàn chỉnh. | Phân tích miền ứng dụng (Domain Analysis), từ đó tự động sinh mã nguồn mới dựa trên các mô hình đặc tả trừu tượng hoặc mẫu thiết kế. |
| **Ẩn dụ trực quan** | **Trò chơi xếp hình Lego** (Block building). | **Khuôn đúc sản phẩm** (Pattern/Spec generator). |
| **Công nghệ tiêu biểu** | Kiến trúc CBD (Component-Based Development), thư viện COTS. | Trình tạo giao diện GUI Builder, Bộ sinh cú pháp Lex/Yacc, Trình tạo mã ORM, Trình sinh khung mẫu mã nguồn. |

#### 2. Kỹ nghệ tái sinh phần mềm (소프트웨어 재공학 - Software Reengineering)
- **개념 (Khái niệm):** Quá trình phân tích, tái cấu trúc và hiện đại hóa hệ thống phần mềm cũ (Legacy System) để cải thiện chất lượng, nâng cao tính bảo trì (유지보수성) và kéo dài tuổi thọ hệ thống mà không làm thay đổi các chức năng nghiệp vụ ban đầu.
- **Các hoạt động cốt lõi trong quy trình tái kỹ nghệ (핵심 시험 포인트):**
  1. **분석 (Analysis / Phân tích):** Khảo sát cấu trúc hiện tại của hệ thống cũ, đánh giá tính khả thi kinh tế kỹ thuật và xác định các module cần tái kỹ nghệ.
  2. **재구성 (Restructuring / Tái cấu trúc):** Thay đổi, tối ưu hóa cấu trúc bên trong của mã nguồn hoặc cấu trúc dữ liệu để làm mã sạch hơn, dễ đọc và dễ bảo trì hơn mà không làm thay đổi hành vi nghiệp vụ bên ngoài.
  3. **역공학 (Reverse Engineering / Kỹ nghệ ngược):** Phân tích mã nguồn hoặc tệp nhị phân hiện có để trích xuất ngược lại các tài liệu thiết kế, sơ đồ luồng dữ liệu hoặc đặc tả yêu cầu đã bị thất lạc trong quá trình vận hành lâu năm.
  4. **순공학 (Forward Engineering / Kỹ nghệ xuôi):** Quá trình phát triển phần mềm thông thường đi từ tài liệu thiết kế và đặc tả (đã được khôi phục hoặc nâng cấp) để sinh mã hoặc bổ sung thêm các tính năng nghiệp vụ mới.
  5. **이식 (Migration / Di chuyển nền tảng):** Chuyển đổi toàn bộ hệ thống phần mềm đã được tái cấu trúc sang hoạt động trên nền tảng phần cứng, hệ điều hành hoặc cơ sở dữ liệu mới.

#### 3. Công cụ CASE (Computer Aided Software Engineering)
- **개념 (Khái niệm):** Bộ các công cụ phần mềm chuyên dụng hỗ trợ tự động hóa toàn bộ hoặc từng phần các hoạt động trong chu trình sống phát triển phần mềm (SDLC), từ phân tích yêu cầu, thiết kế kiến trúc, sinh mã cho đến kiểm thử và bảo trì.
- **Phân loại công cụ CASE:**

| Nhóm CASE | Tên tiếng Hàn & Anh | Phạm vi giai đoạn SDLC hỗ trợ | Chức năng & Sản phẩm đại diện |
| :--- | :--- | :--- | :--- |
| **CASE cấp cao** | **상위 CASE (Upper CASE)** | Các giai đoạn đầu: **Lập kế hoạch, Phân tích yêu cầu, Thiết kế kiến trúc**. | Vẽ sơ đồ luồng dữ liệu (DFD), sơ đồ thực thể liên kết (ERD), mô hình hóa cấu trúc hệ thống, kiểm tra tính nhất quán của đặc tả. |
| **CASE cấp thấp** | **하위 CASE (Lower CASE)** | Các giai đoạn sau: **Cài đặt mã nguồn, Kiểm thử, Bàn giao, Bảo trì**. | Trình sinh mã nguồn tự động, công cụ kiểm thử đơn vị tự động, công cụ tài liệu hóa mã nguồn, theo dõi lỗi (Defect tracking). |
| **CASE tích hợp** | **통합 CASE (Integrated CASE)** | **Bao phủ toàn bộ chu trình sống SDLC** từ phân tích đến bảo trì. | Đồng bộ dữ liệu xuyên suốt giữa các pha; thay đổi ở mô hình thiết kế sẽ tự động cập nhật xuống mã nguồn và kịch bản kiểm thử. |

- **중앙 저장소 (Central Repository / Kho lưu trữ trung tâm của CASE):**
  - Là cơ sở dữ liệu dùng chung lưu trữ toàn bộ các sản phẩm bàn giao (산출물) của dự án: tài liệu yêu cầu, biểu đồ thiết kế, từ điển dữ liệu, mã nguồn và kết quả kiểm thử.
  - Đảm bảo tính toàn vẹn, tính nhất quán (일관성) và khả năng truy vết (추적성) giữa các giai đoạn phát triển khác nhau.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Mối quan hệ giữa Tái kỹ nghệ (Reengineering) và Tái cấu trúc (Refactoring)
- **Tái cấu trúc (Refactoring):** Là một kỹ thuật vi mô nằm trong giai đoạn phát triển hoặc bảo trì nhỏ, sửa đổi cấu trúc bên trong của mã nguồn nhằm loại bỏ mã xấu ("Code Smells"), nâng cao tính dễ đọc mà không làm thay đổi hành vi bên ngoài.
- **Tái kỹ nghệ (Reengineering):** Là một chiến lược quy mô lớn cấp hệ thống (Macro-level), bao gồm cả việc khảo sát kinh tế kỹ thuật, khôi phục kiến trúc bằng Kỹ nghệ ngược (Reverse Engineering), tái cấu trúc dữ liệu và di chuyển sang nền tảng công nghệ mới (ví dụ: chuyển đổi hệ thống ngân hàng từ COBOL trên Mainframe sang Java Spring Boot trên Cloud).

#### Rào cản kỹ thuật của việc Tái sử dụng phần mềm
- Để một module có thể tái sử dụng thành công, nó phải thỏa mãn các nguyên lý thiết kế:
  - **Độ kết dính cao (High Cohesion):** Module chỉ thực hiện một nhiệm vụ duy nhất, rõ ràng.
  - **Độ ghép nối thấp (Low Coupling):** Module không bị phụ thuộc cứng vào trạng thái hoặc các biến nội bộ của module khác.
  - **Giao diện chuẩn hóa (Standardized Interface):** Đầu vào và đầu ra được định nghĩa bằng các hợp đồng giao diện rõ ràng (Interface/API Contracts).

---

### 복습 체크리스트
- [ ] Phân biệt rõ: 합성 중심 (Synthesis/Composition) là lắp ghép linh kiện/khối có sẵn (Lego); 생성 중심 (Analysis/Generation) là phân tích mẫu và sinh mã tự động.
- [ ] Nhớ các hoạt động của quy trình tái kỹ nghệ: 분석 (Phân tích), 재구성 (Tái cấu trúc), 역공학 (Kỹ nghệ ngược), 순공학 (Kỹ nghệ xuôi), 이식 (Di chuyển nền tảng).
- [ ] Nắm được bản chất của 역공학 (Reverse Engineering): Đi ngược từ mã nguồn để khôi phục tài liệu thiết kế bị mất.
- [ ] Phân loại chính xác: 상위 CASE hỗ trợ pha đầu (Phân tích, Thiết kế); 하위 CASE hỗ trợ pha sau (Viết mã, Kiểm thử); 통합 CASE bao phủ toàn bộ SDLC.
- [ ] Nhớ vai trò của 중앙 저장소 (Central Repository): Trái tim duy trì tính nhất quán và lưu trữ toàn bộ tài sản trong môi trường CASE.
