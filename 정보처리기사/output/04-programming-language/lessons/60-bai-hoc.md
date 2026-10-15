# 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, triết lý và thời điểm áp dụng của kiểm thử hộp đen (블랙 박스 테스트 - Black Box / Functional Testing) trong quy trình bảo đảm chất lượng phần mềm.
- Phân biệt bản chất và trường hợp áp dụng của các kỹ thuật thiết kế test case hộp đen kinh điển: Phân vùng tương đương (동치 분할 검사), Phân tích giá trị biên (경계값 분석), Đồ thị nguyên nhân - kết quả (원인-효과 그래프), và Dự đoán lỗi theo kinh nghiệm (오류 예측 검사).
- So sánh sự khác biệt cốt lõi giữa kiểm thử hộp trắng (White Box) và kiểm thử hộp đen (Black Box).

## 핵심 키워드 (Từ khóa)
- 블랙 박스 테스트 (Black Box / Functional Testing)
- 요구사항 명세서 기반 (Specification-based Testing)
- 동치 분할 검사 (Equivalence Partitioning)
- 경계값 분석 (Boundary Value Analysis)
- 원인-효과 그래프 (Cause-Effect Graphing)
- 오류 예측 검사 (Error Guessing)
- 비교 검사 (Comparison Testing)
- 의사결정 테이블 (Decision Table Testing)
- 테스트 후반부 적용 (Late-stage Testing)

## 선행·연결 개념 (Kiến thức liên kết)
- [59-bai-hoc.md](59-bai-hoc.md): Kiểm thử hộp trắng (White Box Test) và độ bao phủ mã nguồn.
- [61-bai-hoc.md](61-bai-hoc.md): Chiến lược kiểm thử phần mềm tích hợp và hệ thống.
- [58-bai-hoc.md](58-bai-hoc.md): Lập trình cấu trúc và độ phức tạp McCabe.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khái niệm: Kiểm thử hộp đen là kiểm thử **chỉ dựa trên tài liệu đặc tả yêu cầu (Specification), không nhìn mã nguồn nội bộ**, thẩm định hệ thống thông qua giao tiếp đầu vào và đầu ra. Được áp dụng chủ yếu ở **giai đoạn sau (후반부)**.
  - Phân loại: Nhớ nhóm từ khóa đại diện cho Black Box gồm: **동치 분할 (Equivalence Partitioning), 경계값 분석 (Boundary Value), 원인-효과 (Cause-Effect), 오류 예측 (Error Guessing), 비교 (Comparison)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các kỹ thuật kiểm thử hộp đen chuẩn mực:**

| Tên kỹ thuật kiểm thử | Bản chất kỹ thuật & Phương pháp chọn Test Case |
| :--- | :--- |
| **동치 분할 검사 (Equivalence Partitioning)** | Chia toàn bộ miền giá trị đầu vào thành các lớp tương đương: **Lớp hợp lệ (Valid)** và **Lớp không hợp lệ (Invalid)**. Chọn một giá trị đại diện từ mỗi lớp để kiểm thử nhằm giảm số lượng test case mà vẫn đảm bảo độ bao quát. |
| **경계값 분석 (Boundary Value Analysis)** | Dựa trên thực tế lỗi phần mềm tập trung nhiều nhất ở ranh giới của các điều kiện. Thiết kế test case tại **ngay giá trị biên, ngay dưới biên, và ngay trên biên** (ví dụ: Miền hợp lệ $[1, 100]$ thì test case gồm: $0, 1, 2$ và $99, 100, 101$). |
| **원인-효과 그래프 (Cause-Effect Graphing)** | Biểu diễn mối quan hệ phụ thuộc giữa các điều kiện đầu vào (Nguyên nhân - Cause) và kết quả đầu ra (Hiệu quả - Effect) dưới dạng đồ thị cổng logic Boole (AND, OR, NOT), sau đó chuyển đổi thành Bảng quyết định (Decision Table). |
| **오류 예측 검사 (Error Guessing)** | Không dựa trên quy tắc toán học hình thức mà dựa vào **kinh nghiệm thực chiến, trực giác và danh sách lỗi thường gặp trong quá khứ** của chuyên gia kiểm thử để đưa ra các ca thử nghiệm đặc biệt. |
| **비교 검사 (Comparison Testing)** | Phát triển độc lập nhiều phiên bản phần mềm theo cùng một tài liệu đặc tả, cấp cùng một bộ dữ liệu đầu vào và **so sánh đối chiếu kết quả đầu ra** giữa các phiên bản để phát hiện sai lệch. |

- **2. So sánh tổng kết Kiểm thử Hộp trắng vs Kiểm thử Hộp đen:**

| Tiêu chí | Kiểm thử Hộp trắng (White Box) | Kiểm thử Hộp đen (Black Box) |
| :--- | :--- | :--- |
| **Tên gọi khác** | Structural Test, Glass-box Test | Functional Test, Behavioral Test |
| **Góc nhìn mã nguồn** | **Nhìn thấy toàn bộ mã nguồn bên trong** | **Không nhìn thấy mã nguồn (Mã đóng)** |
| **Cơ sở thiết kế** | Dựa trên cấu trúc logic mã và luồng điều khiển | Dựa trên tài liệu đặc tả yêu cầu (Requirements) |
| **Thời điểm áp dụng** | **Giai đoạn đầu (초기)** – Unit Test | **Giai đoạn sau (후반부)** – System, Acceptance Test |
| **Người thực hiện** | Thường là lập trình viên (Developer) | Kiểm thử viên chuyên trách (QA / Tester), Người dùng |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ phân tích giá trị biên trong đề thi:**
  - *Yêu cầu hệ thống:* "Điểm thi hợp lệ là số nguyên từ 0 đến 100 điểm".
  - *Bộ dữ liệu biên cần thử nghiệm:*
    - Cận dưới: `-1` (Không hợp lệ), `0` (Biên hợp lệ), `1` (Hợp lệ).
    - Cận trên: `99` (Hợp lệ), `100` (Biên hợp lệ), `101` (Không hợp lệ).
  - Kỹ thuật này phát hiện cực kỳ hiệu quả các lỗi dùng nhầm toán tử so sánh của lập trình viên (ví dụ viết `>` thay vì `>=`).

### 복습 체크리스트
- [ ] Ghi nhớ kiểm thử hộp đen là kiểm thử chức năng dựa trên đặc tả, không nhìn mã nguồn, áp dụng ở giai đoạn sau.
- [ ] Kể tên đầy đủ các phương pháp hộp đen: Equivalence Partitioning, Boundary Value, Cause-Effect, Error Guessing, Comparison.
- [ ] Biết cách chọn bộ dữ liệu phân tích giá trị biên ($min-1, min, min+1, max-1, max, max+1$).
- [ ] Phân biệt được sự khác nhau giữa kiểm thử hộp trắng (nội bộ, cấu trúc) và hộp đen (giao diện, chức năng).
