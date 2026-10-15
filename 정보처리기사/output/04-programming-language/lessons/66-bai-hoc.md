# 208. 소프트웨어의 재사용 (Software Reuse / Tái sử dụng phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục đích chiến lược và các lợi ích cốt lõi của việc tái sử dụng phần mềm (소프트웨어 재사용 - Software Reuse) trong công nghiệp phần mềm.
- Hiểu khái niệm Thành phần phần mềm (컴포넌트 - Component) – đơn vị đóng gói độc lập phục vụ tái sử dụng ở quy mô lớn.
- Nhận diện các yếu tố ảnh hưởng trực tiếp đến tỷ lệ tái sử dụng của module (quy mô module, tính tổng quát) và các thách thức, rào cản khi triển khai tái sử dụng trong doanh nghiệp.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 재사용 (Software Reuse)
- 개발 시간 단축 & 비용 절감 (Time & Cost Reduction)
- 품질 및 신뢰성 향상 (Quality & Reliability Improvement)
- 컴포넌트 기반 개발 (CBD - Component-Based Development)
- 모듈의 크기와 일반성 (Module Size & Generality)
- 표준화 부재 (Lack of Standardization)
- 부품화 (Componentization)

## 선행·연결 개념 (Kiến thức liên kết)
- [65-bai-hoc.md](65-bai-hoc.md): Thiết kế và lập trình hướng đối tượng (OOD & OOP).
- [67-bai-hoc.md](67-bai-hoc.md): Kỹ thuật tái công nghệ phần mềm (Software Reengineering).
- [68-bai-hoc.md](68-bai-hoc.md): Công cụ tự động hóa kỹ nghệ phần mềm CASE.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khái niệm Component: Là **tập hợp các đối tượng kết nối với nhau, có giao tiếp rõ ràng và là đơn vị tái sử dụng quy mô lớn (대규모 재사용 단위)**.
  - Về quy mô module: Module có **kích thước nhỏ và tính tổng quát cao (모듈 크기가 작고 일반적일수록)** thì tỷ lệ tái sử dụng càng cao. Module quá to hoặc gắn liền với nghiệp vụ đặc thù riêng biệt sẽ rất khó đem sang dự án khác.
  - Nhược điểm/Khó khăn: Thường chọn các đáp án liên quan đến **thiếu chuẩn hóa (표준화 부족)** hoặc khó khăn trong việc tìm kiếm và tích hợp mã nguồn.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Lợi ích của việc tái sử dụng phần mềm:**
  - **Rút ngắn chu kỳ phát triển:** Giảm thiểu thời gian thiết kế, mã hóa và kiểm thử các tính năng lặp lại.
  - **Tiết kiệm ngân sách:** Giảm chi phí nhân sự và vận hành dự án.
  - **Nâng cao chất lượng & độ tin cậy:** Các module tái sử dụng vốn đã được kiểm thử và vận hành ổn định trong các dự án thực tế trước đó, giúp giảm tỷ lệ phát sinh lỗi mới.
  - **Chuẩn hóa quy trình:** Thúc đẩy việc tài liệu hóa và đồng bộ giao tiếp kỹ thuật giữa các nhóm phát triển.

- **2. Đơn vị tái sử dụng: Component (컴포넌트):**

| Khái niệm | Định nghĩa kỹ thuật chuẩn |
| :--- | :--- |
| **Component (Thành phần)** | Là một khối phần mềm độc lập, hoàn chỉnh về mặt chức năng, được đóng gói sẵn và chỉ tương tác với môi trường bên ngoài thông qua các **giao diện (Interfaces)** được định nghĩa rõ ràng. |
| **Vai trò** | Là đơn vị cơ sở cho phương pháp phát triển phần mềm dựa trên thành phần (**CBD - Component-Based Development**), cho phép lắp ráp phần mềm như trò chơi Lego. |

- **3. Quy luật thiết kế module để tối ưu hóa tái sử dụng:**
  - **Kích thước nhỏ gọn (작은 크기):** Module nhỏ dễ đọc hiểu, dễ kiểm thử và dễ ghép nối.
  - **Tính tổng quát (일반성 - Generality):** Module xử lý các nghiệp vụ chung (xác thực, mã hóa dữ liệu, gửi email, định dạng tiền tệ) thay vì nhúng chặt logic nghiệp vụ đặc thù của một khách hàng duy nhất.
  - **Độ gắn kết cao, kết hợp thấp:** High Cohesion và Low Coupling là tiền đề bắt buộc để tái sử dụng thành công.

- **4. Các thách thức kỹ thuật lớn nhất khi tái sử dụng:**
  - **Thiếu chuẩn hóa (표준화 부족):** Các dự án sử dụng quy chuẩn mã nguồn, framework hoặc phiên bản ngôn ngữ khác nhau.
  - **Khó khăn trong phân loại & tìm kiếm:** Thiếu kho lưu trữ tập trung (Component Repository) khiến lập trình viên thà tự viết mới còn hơn mất công tìm module cũ.
  - **Chi phí tích hợp cao:** Ghép một thành phần cũ vào kiến trúc mới đôi khi tốn nhiều công sức kiểm thử tương thích hơn là viết mới.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hai phương pháp tái sử dụng chính:**
  1. **Tái sử dụng tổng hợp (합성 중심 - Composition-based / Building Block):** Lắp ghép các khối thành phần (Component) có sẵn lại với nhau như xếp hình.
  2. **Tái sử dụng phát sinh (생성 중심 - Generation-based):** Sử dụng các mẫu thiết kế và tham số trừu tượng để công cụ tự động sinh mã nguồn mới (Pattern-based Code Generation).

### 복습 체크리스트
- [ ] Ghi nhớ lợi ích lớn nhất của tái sử dụng: Rút ngắn thời gian, giảm chi phí, tăng chất lượng.
- [ ] Nhớ Component là đơn vị tái sử dụng quy mô lớn trong kiến trúc CBD.
- [ ] Khẳng định module có kích thước nhỏ và tính tổng quát cao sẽ có tỷ lệ tái sử dụng cao nhất.
- [ ] Nắm được khó khăn lớn nhất của tái sử dụng là thiếu tiêu chuẩn hóa (표준화 부족).
