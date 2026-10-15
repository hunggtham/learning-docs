# 프로그래밍 언어 종류 및 특징 (Programming Languages Types & Features)

## 학습 목표 (Mục tiêu)
- Nắm vững lịch sử phát triển, mục đích ra đời và đặc trưng cú pháp của các ngôn ngữ lập trình hướng thủ tục (절차적 프로그래밍 언어 - Procedural Programming Languages).
- Phân biệt chi tiết thế mạnh chuyên biệt của từng ngôn ngữ kinh điển: C (Hệ điều hành/Phần cứng), FORTRAN (Tính toán khoa học), COBOL (Nghiệp vụ tài chính ngân hàng), ALGOL (Cội nguồn thuật toán cấu trúc), và PASCAL (Giảng dạy cấu trúc).
- Hiểu cấu trúc phân vùng 4 DIVISION đặc trưng trong chương trình nguồn COBOL.

## 핵심 키워드 (Từ khóa)
- 절차적 언어 (Procedural Programming Language)
- C 언어 (Dennis Ritchie, UNIX 구현, 하드웨어 제어, 포인터)
- FORTRAN (수치 계산, 과학 기술 계산의 효시)
- COBOL (사무 처리, 4대 DIVISION 구조)
- ALGOL (알고리즘 표현, C/Pascal의 모체)
- PASCAL (Niklaus Wirth, 구조적 프로그래밍 교육용)
- 순차적 실행 (Sequential Instruction Flow)

## 선행·연결 개념 (Kiến thức liên kết)
- [52-bai-hoc.md](52-bai-hoc.md): Trạng thái dữ liệu lỗi và đặc tính chương trình Batch.
- [54-bai-hoc.md](54-bai-hoc.md): Tiêu chuẩn thiết kế phần mềm tốt (Low Coupling, High Cohesion).
- [01-bai-hoc.md](01-bai-hoc.md): Căn bản về ngôn ngữ lập trình và phân loại môi trường thực thi.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - C: Thường gắn liền với từ khóa "Dennis Ritchie, 1972, Bell Labs, phát triển cùng UNIX, hỗ trợ con trỏ, vừa là ngôn ngữ bậc cao vừa có tính năng bậc thấp".
  - FORTRAN: Gắn với "Formula Translation, tính toán khoa học, ma trận, công thức toán".
  - COBOL: Gắn với "Common Business-Oriented Language, xử lý kế toán ngân hàng, có 4 DIVISION".
  - ALGOL: Gắn với "mẹ đẻ của Pascal và C, ngôn ngữ mô tả thuật toán chuẩn quốc tế".

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân loại các ngôn ngữ lập trình hướng thủ tục kinh điển:**

| Tên ngôn ngữ | Năm ra đời & Tác giả | Mục đích chính | Đặc trưng kỹ thuật nổi bật |
| :--- | :--- | :--- | :--- |
| **FORTRAN** | 1957 (John Backus - IBM) | Tính toán khoa học, công thức toán học | Ngôn ngữ bậc cao đầu tiên; xử lý số thực, mảng và ma trận cực mạnh. |
| **ALGOL** | 1958 (Hội đồng quốc tế) | Chuẩn hóa thuật toán khoa học | Tiền thân trực tiếp của C và Pascal; đưa ra cấu trúc khối (`begin-end`) và đệ quy. |
| **COBOL** | 1959 (Grace Hopper) | Xử lý dữ liệu thương mại, ngân hàng | Cú pháp tự nhiên giống câu tiếng Anh; cấu trúc chương trình bắt buộc chia làm **4 DIVISION**. |
| **BASIC** | 1964 (Kemeny & Kurtz) | Giáo dục nhập môn tin học | Cú pháp đơn giản, thông dịch, dễ học cho người mới bắt đầu. |
| **PASCAL** | 1970 (Niklaus Wirth) | Giảng dạy lập trình có cấu trúc | Kiểm tra kiểu dữ liệu tĩnh nghiêm ngặt; cấu trúc dữ liệu rõ ràng, cấm lối tắt nguy hiểm. |
| **C** | 1972 (Dennis Ritchie) | Lập trình hệ thống và hệ điều hành UNIX | Hỗ trợ con trỏ (Pointer) can thiệp trực tiếp bộ nhớ RAM; kết hợp độ trừu tượng bậc cao và hiệu năng bậc thấp. |

- **4 phân vùng (DIVISION) bắt buộc của chương trình COBOL:**
  1. **IDENTIFICATION DIVISION (Định danh):** Khai báo tên chương trình, tác giả, ngày tạo, ghi chú bản quyền.
  2. **ENVIRONMENT DIVISION (Môi trường):** Định nghĩa cấu hình phần cứng máy tính và liên kết tệp tin ngoại vi.
  3. **DATA DIVISION (Dữ liệu):** Khai báo toàn bộ cấu trúc biến, bản ghi và tệp dữ liệu được sử dụng.
  4. **PROCEDURE DIVISION (Thủ tục / Xử lý):** Chứa các câu lệnh logic thuật toán thực thi chương trình.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tại sao C được gọi là "Ngôn ngữ bậc trung" (Middle-level Language)?**
  - Mặc dù được xếp vào loại ngôn ngữ bậc cao vì có cấu trúc điều khiển rẽ nhánh, vòng lặp, kiểu dữ liệu phức hợp, C lại cho phép thao tác bit (`&, |, ^, ~`), dịch chuyển bit (`<<, >>`), và truy xuất địa chỉ bộ nhớ vật lý thông qua con trỏ (`*p`). Điều này giúp viết code chạy với tốc độ gần như Assembly nhưng vẫn đảm bảo tính di động (Portability) giữa các kiến trúc CPU khác nhau.

### 복습 체크리스트
- [ ] Ghi nhớ Dennis Ritchie phát triển ngôn ngữ C vào năm 1972 tại Bell Labs để xây dựng hệ điều hành UNIX.
- [ ] Nắm vững FORTRAN phục vụ tính toán khoa học công nghệ, COBOL phục vụ kế toán văn phòng thương mại.
- [ ] Kể tên đầy đủ 4 DIVISION của COBOL: Identification, Environment, Data, Procedure.
- [ ] Nhớ ALGOL là ngôn ngữ nền tảng tạo tiền đề phát triển cho Pascal và C.
- [ ] Hiểu lý do C được mệnh danh là ngôn ngữ cầu nối giữa bậc cao và bậc thấp nhờ cơ chế con trỏ.
