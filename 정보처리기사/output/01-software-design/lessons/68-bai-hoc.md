# 8. 재사용 (Reuse)

## 학습 목표 (Mục tiêu)
- Định nghĩa khái niệm 재사용 (Software Reuse - Tái sử dụng phần mềm) và các lợi ích cốt lõi: Tăng năng suất, giảm chi phí, rút ngắn thời gian phát triển và nâng cao độ tin cậy.
- Phân biệt 3 cấp độ tái sử dụng phần mềm: Hàm & Đối tượng (Function & Object), Thành phần (Component) và Ứng dụng (Application).
- Nắm vững 2 phương pháp tiếp cận tái sử dụng kinh điển: 합성 중심 (Composition-based / Lắp ghép khối) và 생성 중심 (Generation-based / Sinh mã theo mẫu quy tắc).

## 핵심 키워드 (Từ khóa)
- 재사용 (Software Reuse)
- 합성 중심 (Composition-based / Block-building)
- 생성 중심 (Generation-based / Pattern-based)
- 컴포넌트 재사용 (Component Reuse)
- 결합도 최소화 & 응집도 최대화 (Loose Coupling, High Cohesion)
- 생산성 (Productivity) & 품질 (Quality)

## 선행·연결 개념 (Kiến thức liên kết)
- [67-bai-hoc.md](67-bai-hoc.md): N-S 차트 (Nassi-Schneiderman Chart) - Biểu diễn logic cấu trúc.
- [69-bai-hoc.md](69-bai-hoc.md): 코드 (Code) 개요 & 종류 - Hệ thống mã hóa thông tin.
- [32-bai-hoc.md](32-bai-hoc.md): Thiết kế mô-đun hóa độc lập phục vụ tái sử dụng.

## 읽는 방법 (Cách đọc)
- Phân biệt 2 cách tiếp cận trong đề thi trắc nghiệm:
  - **합성 중심 (Composition):** Từ khóa là **"블록을 맞춰 조립"** (Ghép các khối block có sẵn như đồ chơi Lego).
  - **생성 중심 (Generation):** Từ khóa là **"명세나 패턴을 기반으로 코드를 만들어냄"** (Tạo code mới dựa trên quy tắc, mẫu hoặc đặc tả).
- Nhớ điều kiện tiên quyết để tái sử dụng hiệu quả: **결합도는 낮고 (Coupling thấp), 응집도는 높아야 한다 (Cohesion cao)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Định nghĩa và Lợi ích cốt lõi:**
  - **재사용 (Reuse):** Quá trình sử dụng lại các tài nguyên phần mềm đã phát triển thành công từ trước (thiết kế, mã nguồn, tài liệu, ca kiểm thử) vào việc xây dựng phần mềm mới.
  - **Lợi ích 4 tăng - 2 giảm:**
    - Tăng năng suất phát triển (개발 생산성 향상).
    - Tăng chất lượng và độ tin cậy phần mềm (품질 및 신뢰도 향상 - do mã tái sử dụng đã được kiểm chứng thực tế).
    - Giảm chi phí phát triển (개발 비용 절감).
    - Rút ngắn chu kỳ và thời gian đưa sản phẩm ra thị trường (개발 기간 단축).
- **Yêu cầu kỹ thuật kiến trúc:**
  - Để một mô-đun có thể tái sử dụng dễ dàng ở nhiều dự án khác nhau:
    - **결합도 (Coupling):** Phải **cực kỳ thấp** (không bị ràng buộc vào biến toàn cục hay cấu trúc dữ liệu lạ).
    - **응집도 (Cohesion):** Phải **rất cao** (tập trung giải quyết trọn vẹn một trách nhiệm duy nhất).

- **Phân loại 3 cấp độ tái sử dụng (Levels of Reuse):**

| Cấp độ tái sử dụng | Phạm vi áp dụng | Đặc điểm chi tiết |
| :--- | :--- | :--- |
| **함수와 객체 (Function & Object)** | Cấp độ mã nguồn (Source Code) | Sử dụng lại các hàm tiện ích chung (Math, String utils) hoặc các Class đối tượng trong thư viện chuẩn |
| **컴포넌트 (Component)** | Cấp độ thành phần đóng gói | Sử dụng lại các thành phần phần mềm độc lập thông qua giao diện chuẩn (Interface) mà không cần quan tâm hoặc sửa đổi mã nguồn bên trong |
| **애플리케이션 (Application)** | Cấp độ toàn hệ thống | Tái sử dụng nguyên cả một hệ thống hoặc phân hệ hoàn chỉnh (ví dụ: Tích hợp Cổng thanh toán, Hệ thống xác thực Single Sign-On SSO) |

- **Hai phương pháp tiếp cận kỹ thuật tái sử dụng:**

| Phương pháp | Tên tiếng Hàn & Anh | Cơ chế hoạt động (Từ khóa đề thi) |
| :--- | :--- | :--- |
| **Phương pháp ghép khối** | **합성 중심 (Composition-based / Block-building)** | Lắp ghép các khối linh kiện, mô-đun phần mềm có sẵn lại với nhau thành hệ thống mới giống như trò chơi ghép hình Lego (블록 조립) |
| **Phương pháp sinh mã** | **생성 중심 (Generation-based / Pattern-based)** | Dựa vào bản đặc tả trừu tượng, mô hình tham số hoặc các mẫu thiết kế (Design Pattern) để công cụ tự động sinh ra mã nguồn mới (추상화 명세 $\rightarrow$ 코드 생성) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Rào cản và chi phí của việc tái sử dụng:**
  - Chi phí thiết kế để một thành phần có thể tái sử dụng (Design for Reuse) thường tốn kém hơn 30% - 50% so với viết hàm dùng một lần (vì phải chuẩn hóa tham số, xử lý ngoại lệ bao quát, viết tài liệu hướng dẫn kỹ lưỡng).
  - Khái niệm **Software Component**: Một khối nhị phân độc lập, có hợp đồng giao tiếp (Interface Contract) rõ ràng, tuân thủ các chuẩn như JavaBeans, COM/DCOM, hoặc các Microservice APIs hiện đại.

### 복습 체크리스트
- [ ] Nắm vững 4 lợi ích lớn của Software Reuse: Tăng năng suất, tăng độ tin cậy, giảm chi phí, giảm thời gian.
- [ ] Nhớ điều kiện kiến trúc: 결합도는 낮고 (Coupling thấp), 응집도는 높아야 한다 (Cohesion cao).
- [ ] Phân biệt được 3 mức độ: 함수/객체 (Code), 컴포넌트 (Interface), 애플리케이션 (Hệ thống).
- [ ] Phân biệt rõ 합성 중심 (Lắp ráp khối block) và 생성 중심 (Sinh mã từ đặc tả/mẫu).
