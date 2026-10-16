# 프로그래밍 언어 분류 및 컴파일러 vs 인터프리터 (Phân loại ngôn ngữ & Biên dịch vs Thông dịch)

## 학습 목표 (Mục tiêu)
- Nắm vững sự khác nhau mang tính bản chất giữa hai phương thức thực thi chương trình: Trình biên dịch (컴파일러 - Compiler) và Trình thông dịch (인터프리터 - Interpreter), cũng như mô hình mã trung gian Bytecode (Java JVM).
- Phân biệt 4 mô hình lập trình (Programming Paradigms) kinh điển: Ngôn ngữ mệnh lệnh/thủ tục (명령형/절차적 언어), Ngôn ngữ hướng đối tượng (객체지향 언어), Ngôn ngữ khai báo (선언형 언어: Hàm và Logic), và Ngôn ngữ kịch bản (스크립트 언어).
- Nhận diện chính xác mục đích thiết kế của các ngôn ngữ lập trình lịch sử thường xuyên xuất hiện trong câu hỏi trắc nghiệm của HRDK: FORTRAN (khoa học kỹ thuật), COBOL (kinh doanh/kế toán), LISP (hàm), PROLOG (logic).

## 핵심 키워드 (Từ khóa)
- 컴파일러 vs 인터프리터 (Compiler vs Interpreter) — Sinh mã đối tượng chạy nhanh vs Thông dịch từng dòng chạy tương tác.
- 목적 코드 (Object Code) — Tệp mã máy trung gian (`.obj`) chỉ được tạo ra bởi Compiler.
- 명령형/절차적 언어 (Imperative / Procedural) — Hướng dẫn máy tính cách thức thực hiện ("How"), ví dụ: C, FORTRAN, COBOL.
- 선언형 언어 (Declarative) — Chỉ định kết quả mong muốn ("What"): Hàm (LISP, Haskell) & Logic (PROLOG).
- 하이브리드 바이트코드 (Hybrid Bytecode) — Trình biên dịch sinh Bytecode trung gian cho máy ảo JVM thực thi.
- 스크립트 언어 (Scripting Languages) — Ngôn ngữ thông dịch phục vụ tự động hóa và phát triển nhanh.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa các trải nghiệm cú pháp và biên dịch giữa C (ngôn ngữ biên dịch), Java (ngôn ngữ bytecode) và Python (ngôn ngữ thông dịch) đã học từ bài 01 đến bài 09.
- **Đang giải quyết gì (Current Problem):** Trả lời các câu hỏi lý thuyết phân loại của kỳ thi: Tại sao ngôn ngữ này chạy nhanh hơn ngôn ngữ kia, ngôn ngữ nào tạo tệp mã đối tượng độc lập, và ngôn ngữ nào phù hợp cho bài toán suy diễn trí tuệ nhân tạo hoặc tính toán khoa học.
- **Dùng đi đâu (Forward Handoff):** Khái niệm tệp thực thi mã máy và quá trình nạp chương trình vào RAM sẽ chuyển giao trực tiếp sang việc tìm hiểu cơ chế quản lý tiến trình và quản lý bộ nhớ của Hệ điều hành trong bài `11-tong-quan-he-dieu-hanh-unix-linux-va-shell-script.md` và `12-tien-trinh-luong-va-dieu-phoi-cpu.md`.

## 읽는 방법 (Cách đọc)
- **Compiler vs Interpreter:**
  - Cứ thấy **"tạo tệp mã đối tượng (목적 코드 생성)"** $\rightarrow$ Chọn ngay **Compiler** (C, C++, Go).
  - Cứ thấy **"không tạo mã đối tượng, dịch từng dòng (줄 단위 / 대화형 실행)"** $\rightarrow$ Chọn ngay **Interpreter** (Python, JS, BASIC).
- **Mô hình lập trình:**
  - "Làm như thế nào (How)" $\rightarrow$ **Mệnh lệnh / Thủ tục** (C, Pascal).
  - "Cái gì cần đạt được (What)" $\rightarrow$ **Khai báo** (SQL, LISP, PROLOG).
  - FORTRAN = Tính toán khoa học; COBOL = Thương mại/Kinh doanh; PROLOG = Logic/AI; LISP = Xử lý danh sách/Hàm.

---

## 프로그래밍 언어 분류 및 컴파일러 vs 인터프리터

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `컴파일러는 전체 원시 코드를 한 번에 번역하여 목적 코드(실행 파일)를 생성하므로 실행 속도가 빠르지만, 인터프리터는 한 줄씩 번역하여 바로 실행하므로 목적 코드를 생성하지 않고 실행 속도가 느리다. 절차적 언어는 'How', 선언형 언어는 'What'에 집중한다.`
  - [Tiếng Việt]: Trình biên dịch dịch toàn bộ mã nguồn cùng lúc và tạo ra tệp mã đối tượng (tệp thực thi) nên tốc độ chạy nhanh; trình thông dịch dịch từng dòng một và thực thi ngay nên không tạo tệp mã đối tượng và tốc độ chạy chậm hơn. Ngôn ngữ thủ tục tập trung vào 'How', ngôn ngữ khai báo tập trung vào 'What'.

- **1. Bảng đối chiếu toàn diện: Trình biên dịch vs Trình thông dịch:**

| Tiêu chuẩn so sánh | Trình biên dịch (컴파일러 - Compiler) | Trình thông dịch (인터프리터 - Interpreter) |
| :--- | :--- | :--- |
| **Đơn vị xử lý dịch** | **Toàn bộ chương trình (Program as a whole)** cùng một lúc. | **Từng dòng lệnh một (Line by line)** theo kiểu tương tác. |
| **Tệp mã đối tượng** | **Có tạo ra tệp mã đối tượng (`.obj`, `.exe`)** độc lập. | **Tuyệt đối KHÔNG tạo ra tệp mã đối tượng**. |
| **Tốc độ thực thi** | **Rất nhanh** (vì mã máy đã được biên dịch sẵn). | **Chậm hơn** (vì mỗi lần chạy đều phải dịch lại từ đầu). |
| **Tốc độ biên dịch ban đầu**| Chậm hơn (phải quét toàn bộ cú pháp dự án). | Tức thì (gõ lệnh nào chạy ngay lệnh đó). |
| **Phát hiện lỗi (Debug)** | Báo toàn bộ danh sách lỗi sau khi dịch xong. | Báo lỗi ngay tại chính dòng lệnh bị sai. |
| **Ngôn ngữ tiêu biểu** | **C, C++, Go, FORTRAN, COBOL**. | **Python, JavaScript, Ruby, PHP, BASIC**. |

- **2. Bảng phân loại 4 mô hình lập trình (프로그래밍 패러다임 분류):**

| Mô hình lập trình | Định hướng cốt lõi | Ngôn ngữ tiêu biểu chuẩn đề thi | Mục đích / Đặc trưng khảo thí |
| :--- | :--- | :--- | :--- |
| **1. Mệnh lệnh / Thủ tục**<br>(명령형 / 절차적) | Tập trung vào **"Làm thế nào (How)"**; tuần tự thay đổi biến trạng thái. | **C, FORTRAN, COBOL, ALGOL, Pascal** | • **FORTRAN:** Tính toán khoa học kỹ thuật.<br>• **COBOL:** Xử lý kinh doanh, ngân hàng.<br>• **C:** Hệ thống và hiệu năng cao. |
| **2. Hướng đối tượng**<br>(객체지향) | Đóng gói thực thể tự chủ gồm dữ liệu và phương thức. | **Java, C++, C#, Smalltalk, Python** | Tái sử dụng cao qua Kế thừa và Đa hình; mô phỏng thế giới thực. |
| **3. Khai báo: Hàm**<br>(선언형 - 함수형) | Tập trung vào **"Cái gì (What)"**; tính toán dựa trên hàm toán học, không side-effect. | **LISP, Haskell, Erlang, Clojure** | **LISP:** Xử lý danh sách (List Processing), ứng dụng nghiên cứu AI đời đầu. |
| **4. Khai báo: Logic**<br>(선언형 - 논리형) | Giải quyết vấn đề bằng suy diễn logic mệnh đề và quy tắc. | **PROLOG** | Hệ chuyên gia (Expert System), chứng minh định lý tự động. |

- **3. Mô hình lai Bytecode trong Java (하이브리드 바이트코드):**
  - Trình biên dịch Java (`javac`) không dịch thẳng ra mã máy vật lý mà dịch mã nguồn `.java` thành **Bytecode trung gian** lưu trong tệp `.class`.
  - Khi chạy, Máy ảo Java (**JVM - Java Virtual Machine**) sẽ nạp Bytecode và dùng kết hợp **Interpreter** cùng **JIT Compiler (Just-In-Time Compiler)** để biên dịch các đoạn mã nóng (Hotspot) thành mã máy bản địa.
  - Nhờ cơ chế này, Java đạt triết lý nổi tiếng: **"Write Once, Run Anywhere (WORA)"** (Viết một lần, chạy mọi nơi).

- **주의/함정 (Bẫy đề thi):**
  - **Khẳng định sai về Interpreter:** Đề thi khẳng định: *"Trình thông dịch tạo ra tệp mã đối tượng trước khi thực thi"* $\rightarrow$ Đây là khẳng định **SAI HOÀN TOÀN**; chỉ Compiler mới tạo ra mã đối tượng (목적 코드).
  - **Nhầm lẫn giữa FORTRAN và COBOL:** FORTRAN dành cho khoa học kỹ thuật (Formula Translation); COBOL dành cho kế toán, thương mại kinh doanh (Common Business-Oriented Language).

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Compiler sinh file chạy nhanh, Interpreter dịch từng dòng tương tác; FORTRAN khoa học, COBOL kế toán, PROLOG suy diễn logic."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ quy trình biên dịch của C (Compiler Pipeline):
$$\text{Mã nguồn (.c)} \xrightarrow{\text{Tiền xử lý (Preprocessor)}} \text{Mã mở rộng} \xrightarrow{\text{Trình biên dịch (Compiler)}} \text{Mã hợp ngữ (.s)} \xrightarrow{\text{Trình hợp dịch (Assembler)}} \mathbf{\text{Mã đối tượng (.obj)}} \xrightarrow{\text{Trình liên kết (Linker)}} \mathbf{\text{Tệp thực thi (.exe)}}$$

- Tệp `.obj` chứa mã máy nhưng chưa liên kết các hàm thư viện như `printf`.
- Trình liên kết (Linker) chịu trách nhiệm ghép nối `.obj` với các thư viện chuẩn để sinh ra tệp thực thi cuối cùng `.exe`.

#### 2. Sơ đồ quy trình thực thi mã Bytecode của Java (JVM):
$$\text{Mã nguồn Java (.java)} \xrightarrow{\text{Lệnh javac}} \mathbf{\text{Bytecode (.class)}} \xrightarrow{\text{Nạp vào JVM}} \begin{cases} \text{Interpreter: Dịch nhanh từng dòng} \\ \text{JIT Compiler: Dịch mã máy cho đoạn lặp nhiều} \end{cases}$$

#### 3. Đối chiếu tư duy "How" (Mệnh lệnh) vs "What" (Khai báo):
- **Ví dụ bài toán:** Lấy các số chẵn trong danh sách `[1, 2, 3, 4, 5, 6]`.
  - *Mô hình Mệnh lệnh (C - "How"):*
    Lập trình viên phải chỉ rõ từng bước: Khởi tạo mảng kết quả, tạo vòng lặp từ 0 đến 5, kiểm tra `arr[i] % 2 == 0`, nếu đúng thì gán vào mảng mới và tăng biến đếm.
  - *Mô hình Khai báo (SQL / Functional - "What"):*
    Chỉ cần tuyên bố điều kiện mong muốn: `SELECT num FROM numbers WHERE num % 2 = 0;` mà không cần quan tâm máy tính duyệt vòng lặp như thế nào.

---

### 복습 체크리스트
- [ ] Ghi nhớ tiêu chí quyết định: Compiler tạo ra mục đích mã đối tượng (`.obj`), Interpreter không tạo mã đối tượng.
- [ ] Nắm được ưu điểm của Compiler: Tốc độ thực thi nhanh; ưu điểm của Interpreter: Debug nhanh từng dòng.
- [ ] Nhớ triết lý: Mệnh lệnh tập trung vào "How", Khai báo tập trung vào "What".
- [ ] Thuộc tên ngôn ngữ đặc thù: FORTRAN (khoa học), COBOL (kinh doanh), PROLOG (logic), LISP (hàm/AI).
- [ ] Hiểu cơ chế Java Bytecode: `javac` dịch sang `.class`, máy ảo JVM thực thi độc lập nền tảng.
