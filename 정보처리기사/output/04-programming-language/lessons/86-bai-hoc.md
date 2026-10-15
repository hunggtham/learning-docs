# 인터프리터 언어 (Interpreter Languages / Ngôn ngữ thông dịch)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế vận hành và triết lý thực thi của các ngôn ngữ thông dịch (인터프리터 언어 - Interpreter Languages).
- Phân biệt chi tiết sự khác nhau mang tính bản chất giữa Trình biên dịch (컴파일러 - Compiler) và Trình thông dịch (인터프리터 - Interpreter) về: Đơn vị dịch, Tệp đầu ra, Tốc độ thực thi, và Quy trình gỡ lỗi.
- Thuộc lòng danh sách các ngôn ngữ lập trình thuộc họ thông dịch thường xuất hiện trong đề thi (Python, JavaScript, BASIC, LISP, PROLOG, APL, PHP).

## 핵심 키워드 (Từ khóa)
- 인터프리터 (Interpreter - 줄 단위 번역 및 즉시 실행)
- 컴파일러 (Compiler - 전체 번역 및 목적 파일 생성)
- 목적 코드 / 실행 파일 (Object Code / Executable `.exe` 부재)
- 대화형 실행 (Interactive Execution / REPL)
- 번역 속도 vs 실행 속도 (Translation Time vs Execution Speed)
- 대표 인터프리터 언어 (Python, JS, BASIC, LISP, PROLOG, APL)

## 선행·연결 개념 (Kiến thức liên kết)
- [85-bai-hoc.md](85-bai-hoc.md): Công nghệ kết nối cơ sở dữ liệu JDBC vs ODBC.
- [87-bai-hoc.md](87-bai-hoc.md): Nguyên lý tính cục bộ tham chiếu bộ nhớ (Locality).
- [72-bai-hoc.md](72-bai-hoc.md): Phân loại ngôn ngữ lập trình hướng thủ tục, OOP và Script.

## 읽는 방법 (Cách đọc)
- Phân biệt hai cơ chế dịch mã trong đề thi:
  - **컴파일러 (Compiler):** Đọc **toàn bộ mã nguồn một lần**, sinh ra tệp mã đối tượng/thực thi nhị phân độc lập (`.obj`, `.exe`). Thời gian dịch ban đầu lâu, nhưng khi chạy thì **tốc độ cực nhanh**. *Đại diện:* C, C++, FORTRAN, PASCAL.
  - **인터프리터 (Interpreter):** Đọc và dịch **từng dòng một (Line-by-line)** rồi thực thi ngay lập tức, **hoàn toàn không sinh ra tệp mã đối tượng trung gian**. Thời gian bắt đầu chạy nhanh, nhưng tốc độ tổng thể chậm hơn do phải dịch lại khi gặp vòng lặp. *Đại diện:* Python, JavaScript, BASIC, LISP, PROLOG, APL, PHP.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng so sánh toàn diện Compiler vs Interpreter:**

| Tiêu chuẩn so sánh | Trình biên dịch (컴파일러 - Compiler) | Trình thông dịch (인터프리터 - Interpreter) |
| :--- | :--- | :--- |
| **Đơn vị xử lý** | Đọc và phân tích **toàn bộ chương trình (Program as a whole)** cùng một lúc. | Đọc và xử lý **từng câu lệnh / từng dòng một (Line by line)**. |
| **Tệp mã đối tượng** | **Có tạo ra** tệp mã máy trung gian (Object code `.obj`, Executable `.exe`). | **Tuyệt đối không tạo ra** tệp mã đối tượng trung gian. |
| **Tốc độ biên dịch** | Tương đối chậm ở bước biên dịch ban đầu. | Không mất thời gian biên dịch trước, chạy được ngay lập tức. |
| **Tốc độ thực thi** | **Cực nhanh** (CPU thực thi trực tiếp mã máy nhị phân). | **Chậm hơn** (Vì mỗi lần thực thi lại phải dịch lại từ đầu). |
| **Sử dụng bộ nhớ** | Tốn dung lượng đĩa và RAM để lưu tệp thực thi nhị phân độc lập. | Tiết kiệm bộ nhớ lưu trữ tệp nhị phân nhưng cần trình thông dịch thường trú. |
| **Thời điểm báo lỗi** | Báo toàn bộ danh sách lỗi cú pháp sau khi quét xong toàn bộ file mã. | Dừng chương trình ngay lập tức tại **dòng đầu tiên phát hiện lỗi cú pháp/runtime**. |
| **Ngôn ngữ tiêu biểu** | **C, C++, FORTRAN, PASCAL, COBOL, Go** | **Python, JavaScript, BASIC, LISP, PROLOG, APL, PHP** |

- **2. Danh sách các ngôn ngữ thông dịch kinh điển cần nhớ khi làm bài trắc nghiệm:**
  - **Python:** Ngôn ngữ thông dịch hiện đại, dùng rộng rãi trong AI, Data Science, Web.
  - **JavaScript:** Ngôn ngữ thông dịch trên trình duyệt (thực thi bởi engine V8, SpiderMonkey).
  - **BASIC:** Ngôn ngữ giáo dục nhập môn thời kỳ đầu máy tính cá nhân.
  - **LISP & PROLOG:** Các ngôn ngữ thông dịch phục vụ nghiên cứu trí tuệ nhân tạo.
  - **APL (A Programming Language):** Ngôn ngữ xử lý mảng toán học bằng các ký hiệu đặc thù.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật Biên dịch tức thời JIT (Just-In-Time Compilation) trong ngôn ngữ hiện đại:**
  - Để khắc phục nhược điểm chạy chậm của Interpreter thuần túy, các môi trường thực thi hiện đại (như Java Virtual Machine JVM, Node.js V8 Engine, PyPy) tích hợp thêm trình biên dịch JIT.
  - Khi chương trình chạy, các đoạn mã được gọi lặp đi lặp lại nhiều lần ("Hot Spots" như thân vòng lặp lớn) sẽ được JIT biên dịch động ngay lúc đó sang mã máy CPU thực tế và lưu vào bộ nhớ đệm cache, giúp kết hợp tốc độ khởi động nhanh của Interpreter và tốc độ chạy tối đa của Compiler.

### 복습 체크리스트
- [ ] Ghi nhớ sự khác biệt cốt lõi: Compiler dịch toàn bộ có tạo file `.exe`, Interpreter dịch từng dòng không tạo file `.exe`.
- [ ] Nhớ Compiler chạy nhanh hơn Interpreter sau khi đã biên dịch xong.
- [ ] Kể tên đầy đủ các ngôn ngữ thông dịch trong đề thi: Python, JavaScript, BASIC, LISP, PROLOG, APL, PHP.
- [ ] Hiểu rõ cơ chế báo lỗi của Interpreter: Gặp dòng lỗi ở đâu thì dừng ngay tại dòng đó.
