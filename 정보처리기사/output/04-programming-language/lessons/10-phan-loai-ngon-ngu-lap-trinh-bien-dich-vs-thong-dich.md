# 프로그래밍 언어 분류 및 컴파일러 vs 인터프리터 (Phân loại ngôn ngữ & Biên dịch vs Thông dịch)

## 학습 목표 (Mục tiêu)
- Nắm vững sự khác nhau mang tính bản chất giữa hai phương thức thực thi chương trình: Trình biên dịch (컴파일러 - Compiler) và Trình thông dịch (인터프리터 - Interpreter).
- Thuộc lòng 6 giai đoạn biên dịch mã nguồn của Compiler: Phân tích từ vựng (Lexical), Phân tích cú pháp (Syntax - Parse Tree), Phân tích ngữ nghĩa (Semantic), Sinh mã trung gian, Tối ưu hóa mã, và Sinh mã đích (Target Code).
- Thấu hiểu cơ chế hoạt động của trình biên dịch động Just-In-Time (JIT Compiler) và mô hình mã trung gian Bytecode trong máy ảo JVM.
- Phân biệt 4 mô hình lập trình (Programming Paradigms) kinh điển: Ngôn ngữ mệnh lệnh/thủ tục (명령형/절차적 언어), Ngôn ngữ hướng đối tượng (객체지향 언어), Ngôn ngữ khai báo (선언형 언어: Hàm và Logic), và Ngôn ngữ kịch bản (스크립트 언어).

## 핵심 키워드 (Từ khóa)
- 컴파일러 vs 인터프리터 (Compiler vs Interpreter) — Sinh mã đối tượng chạy nhanh vs Thông dịch từng dòng chạy tương tác.
- 컴파일 6단계 (6 Compilation Phases) — 어휘 분석(토큰), 구문 분석(파스 트리), 의미 분석(타입 검사), 중간 코드 생성, 코드 최적화, 목적 코드 생성.
- 파스 트리 (Parse Tree / AST) — Cây phân tích cú pháp biểu diễn cấu trúc ngữ pháp chương trình.
- 목적 코드 (Object Code) — Tệp mã máy trung gian (`.obj`) chỉ được tạo ra bởi Compiler.
- JIT 컴파일러 (Just-In-Time Compiler) — Biên dịch mã Bytecode thành mã máy bản địa tại runtime cho các đoạn mã lặp nóng (Hotspots).
- 명령형 vs 선언형 (Imperative vs Declarative) — Tập trung vào cách làm ("How") vs Tập trung vào kết quả ("What").

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa các trải nghiệm cú pháp và biên dịch giữa C (ngôn ngữ biên dịch), Java (ngôn ngữ bytecode) và Python (ngôn ngữ thông dịch) đã học từ bài 01 đến bài 09.
- **Đang giải quyết gì (Current Problem):** Trả lời các câu hỏi lý thuyết phân loại của kỳ thi: Tại sao ngôn ngữ này chạy nhanh hơn ngôn ngữ kia, ngôn ngữ nào tạo tệp mã đối tượng độc lập, quá trình dịch mã diễn ra qua các bước nào và giải quyết các lỗi cú pháp/ngữ nghĩa ở đâu.
- **Dùng đi đâu (Forward Handoff):** Khái niệm tệp thực thi mã máy và quá trình nạp chương trình vào RAM sẽ chuyển giao trực tiếp sang việc tìm hiểu cơ chế quản lý tiến trình và quản lý bộ nhớ của Hệ điều hành trong bài `11-tong-quan-he-dieu-hanh-unix-linux-va-shell-script.md` và `12-tien-trinh-luong-va-dieu-phoi-cpu.md`.

## 읽는 방법 (Cách đọc)
- **Compiler vs Interpreter:**
  - Cứ thấy **"tạo tệp mã đối tượng (목적 코드 생성)"** -> Chọn ngay **Compiler** (C, C++, Go).
  - Cứ thấy **"không tạo mã đối tượng, dịch từng dòng (줄 단위 / 대화형 실행)"** -> Chọn ngay **Interpreter** (Python, JS, BASIC).
- **6 Giai đoạn biên dịch:**
  - Từ vựng (Lexical) -> Tạo **Token**.
  - Cú pháp (Syntax) -> Tạo **Parse Tree** (Cây cú pháp).
  - Ngữ nghĩa (Semantic) -> **Kiểm tra kiểu dữ liệu (Type Checking)**.
  - Mã trung gian -> Độc lập phần cứng (3-address code).
  - Tối ưu hóa -> Bỏ code thừa, tối ưu vòng lặp.
  - Mã đích -> Sinh mã máy CPU cụ thể.
- **JIT Compiler:** Không dịch trước toàn bộ, mà dịch tức thời các đoạn mã chạy lặp đi lặp lại nhiều lần (Hotspot) thành mã máy thật để tăng tốc.

---

## 프로그래밍 언어 분류 및 컴파일러 vs 인터프리터

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `컴파일러는 전체 원시 코드를 한 번에 번역하여 목적 코드(.obj)를 생성하고 6단계(어휘-토큰, 구문-파스트리, 의미-타입검사, 중간코드, 최적화, 목적코드)를 거친다. 인터프리터는 한 줄씩 번역하여 실행하므로 목적 코드가 없다. JIT 컴파일러는 바이트코드를 런타임에 기계어로 직접 변환한다.`
  - [Tiếng Việt]: Trình biên dịch dịch toàn bộ mã nguồn cùng lúc để sinh mã đối tượng (.obj) qua 6 giai đoạn (từ vựng-token, cú pháp-parse tree, ngữ nghĩa-kiểm tra kiểu, mã trung gian, tối ưu hóa, mã đích). Trình thông dịch dịch từng dòng thực thi ngay nên không có mã đối tượng. Trình biên dịch JIT chuyển bytecode thành mã máy bản địa tại runtime.

- **1. Bảng đối chiếu toàn diện: Trình biên dịch vs Trình thông dịch:**

| Tiêu chuẩn so sánh | Trình biên dịch (컴파일러 - Compiler) | Trình thông dịch (인터프리터 - Interpreter) |
| :--- | :--- | :--- |
| **Đơn vị xử lý dịch** | **Toàn bộ chương trình (Program as a whole)** cùng một lúc. | **Từng dòng lệnh một (Line by line)** theo kiểu tương tác. |
| **Tệp mã đối tượng** | **Có tạo ra tệp mã đối tượng (`.obj`, `.exe`)** độc lập. | **Tuyệt đối KHÔNG tạo ra tệp mã đối tượng**. |
| **Tốc độ thực thi** | **Rất nhanh** (vì mã máy đã được biên dịch sẵn). | **Chậm hơn** (vì mỗi lần chạy đều phải dịch lại từ đầu). |
| **Tốc độ biên dịch ban đầu**| Chậm hơn (phải quét toàn bộ cú pháp dự án). | Tức thì (gõ lệnh nào chạy ngay lệnh đó). |
| **Phát hiện lỗi (Debug)** | Báo toàn bộ danh sách lỗi sau khi dịch xong. | Báo lỗi ngay tại chính dòng lệnh bị sai. |
| **Ngôn ngữ tiêu biểu** | **C, C++, Go, FORTRAN, COBOL**. | **Python, JavaScript, Ruby, PHP, BASIC**. |

- **2. Bảng 6 giai đoạn dịch mã của Trình biên dịch (컴파일러 번역 6단계):**

| Giai đoạn | Tên tiếng Hàn & Anh | Nhiệm vụ kỹ thuật cốt lõi | Đầu ra sinh ra (Artifact) |
| :---: | :--- | :--- | :--- |
| **1** | **어휘 분석** (Lexical Analysis) | Đọc chuỗi ký tự thô, gom nhóm thành các từ tố có nghĩa (**Token**), lọc bỏ khoảng trắng và chú thích. | Danh sách Token & Bảng ký hiệu (Symbol Table) |
| **2** | **구문 분석** (Syntax Analysis) | Kiểm tra ngữ pháp theo văn phạm phi ngữ cảnh, phát hiện lỗi cú pháp dấu câu. | **Cây phân tích cú pháp (Parse Tree / AST)** |
| **3** | **의미 분석** (Semantic Analysis) | Kiểm tra tính tương thích kiểu dữ liệu (**Type Checking**), phạm vi biến, số lượng đối số hàm. | Cây cú pháp có gán nhãn kiểu (Annotated AST) |
| **4** | **중간 코드 생성** (Intermediate Code) | Sinh biểu diễn trung gian độc lập với phần cứng máy tính (dạng mã 3 địa chỉ, Quadruple, Bytecode). | Intermediate Representation (IR) |
| **5** | **코드 최적화** (Code Optimization) | Loại bỏ mã chết (Dead code), rút gọn hằng số (Constant folding), tối ưu vòng lặp để tăng tốc độ. | Mã trung gian tối ưu |
| **6** | **목적 코드 생성** (Target Code) | Chuyển đổi mã trung gian thành mã máy bản địa hoặc mã hợp ngữ (Assembly) của kiến trúc CPU cụ thể. | **Mã đối tượng (Object Code `.obj`)** |

- **3. Bảng phân loại 4 mô hình lập trình (프로그래밍 패러다임 분류):**

| Mô hình lập trình | Định hướng cốt lõi | Ngôn ngữ tiêu biểu chuẩn đề thi | Mục đích / Đặc trưng khảo thí |
| :--- | :--- | :--- | :--- |
| **Mệnh lệnh / Thủ tục (명령형 / 절차적)** | Tập trung vào "Làm thế nào (How)"; tuần tự thay đổi biến trạng thái. | C, FORTRAN, COBOL, ALGOL, Pascal | FORTRAN cho khoa học kỹ thuật; COBOL cho kinh doanh ngân hàng; C cho hệ thống. |
| **Hướng đối tượng (객체지향)** | Đóng gói thực thể tự chủ gồm dữ liệu và phương thức. | Java, C++, C#, Smalltalk, Python | Tái sử dụng cao qua Kế thừa và Đa hình; mô phỏng thế giới thực. |
| **Khai báo: Hàm (선언형 - 함수형)** | Tập trung vào "Cái gì (What)"; tính toán dựa trên hàm toán học, không side-effect. | LISP, Haskell, Erlang, Clojure | LISP xử lý danh sách (List Processing), nghiên cứu AI đời đầu. |
| **Khai báo: Logic (선언형 - 논리형)** | Giải quyết vấn đề bằng suy diễn logic mệnh đề và quy tắc. | PROLOG | Hệ chuyên gia (Expert System), chứng minh định lý tự động. |

- **주의/함정 (Bẫy đề thi):**
  - **Khẳng định sai về Interpreter:** Đề thi khẳng định: *"Trình thông dịch tạo ra tệp mã đối tượng trước khi thực thi"* -> Đây là khẳng định **SAI HOÀN TOÀN**; chỉ Compiler mới tạo ra mã đối tượng (목적 코드).
  - **Nhiệm vụ của Syntax vs Semantic:** Kiểm tra dấu ngoặc, thiếu dấu chấm phẩy thuộc về **Syntax Analysis**; kiểm tra lỗi cộng số nguyên với chuỗi (sai kiểu) hoặc dùng biến chưa khai báo thuộc về **Semantic Analysis**.
  - **JIT Compiler:** JIT là thành phần của máy ảo (như JVM, V8), biên dịch Bytecode thành mã máy ngay tại runtime cho các đoạn mã chạy nhiều lần (Hotspot), kết hợp ưu điểm khởi động nhanh của Interpreter và tốc độ cao của Compiler.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Compiler sinh file chạy nhanh qua 6 bước (từ vựng token, cú pháp parse tree, ngữ nghĩa type check, mã trung gian, tối ưu, mã máy); Interpreter dịch từng dòng; JIT nung mã nóng thành mã máy."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ luồng 6 giai đoạn biên dịch chi tiết (Compiler Pipeline):
```text
[ Mã nguồn C: "int a = b + 10;" ]
               |
               v
1. Phân tích từ vựng (Lexer)     --> [ Token: <INT>, <ID, "a">, <ASSIGN>, <ID, "b">, <PLUS>, <NUM, 10>, <SEMI> ]
               |
               v
2. Phân tích cú pháp (Parser)    --> [ Parse Tree / AST: Nút gốc '=' có con trái 'a', con phải '+'(b, 10) ]
               |
               v
3. Phân tích ngữ nghĩa (Semantic) --> [ Kiểm tra: Biến b đã khai báo chưa? Kiểu của b có cộng được với 10 không? ]
               |
               v
4. Sinh mã trung gian (IR Gen)   --> [ Mã 3 địa chỉ: t1 = b + 10; a = t1 ]
               |
               v
5. Tối ưu hóa mã (Optimizer)     --> [ Loại bỏ biến phụ t1, tối ưu thanh ghi ]
               |
               v
6. Sinh mã đích (Code Gen)       --> [ Mã máy / Hợp ngữ: MOV EAX, [b]; ADD EAX, 10; MOV [a], EAX ]
```

#### 2. Sơ đồ cơ chế hoạt động của JIT Compiler trong Java Virtual Machine (JVM):
```text
+---------------------+
| Mã nguồn Java (.java)|
+---------------------+
           | javac (Biên dịch tĩnh ban đầu)
           v
+---------------------+
| Bytecode (.class)   | (Độc lập nền tảng, mã giả lập cho JVM)
+---------------------+
           |
           v Nạp vào JVM Runtime
+-------------------------------------------------------------+
| JVM Execution Engine                                        |
|  - Interpreter: Dịch và chạy từng dòng Bytecode ngay lập tức|
|  - Profiler: Theo dõi các đoạn mã chạy lặp lại nhiều lần    |
|              (Hotspot Code)                                 |
|  - JIT Compiler: Biên dịch trực tiếp Hotspot Bytecode thành  |
|                  Mã máy CPU bản địa (Native Machine Code)   |
|                  -> Lưu vào Code Cache để chạy siêu tốc     |
+-------------------------------------------------------------+
```

#### 3. So sánh các mô hình lập trình qua bài toán tính tổng mảng:
- *Mô hình Mệnh lệnh (C - Imperative "How"):*
```c
int sum = 0;
for (int i = 0; i < n; i++) {
    sum += arr[i]; // Lập trình viên tự quản lý biến chỉ số và trạng thái cộng dồn
}
```
- *Mô hình Hàm (Python/LISP - Declarative "What"):*
```python
total = sum(arr) # Chỉ định kết quả mong muốn, không bận tâm đến cơ chế lặp bên dưới
```

---

### 복습 체크리스트
- [ ] Ghi nhớ tiêu chí quyết định: Compiler tạo ra tệp mã đối tượng (`.obj`), Interpreter không tạo mã đối tượng.
- [ ] Thuộc lòng thứ tự 6 giai đoạn của Compiler: Từ vựng -> Cú pháp -> Ngữ nghĩa -> Mã trung gian -> Tối ưu -> Mã đích.
- [ ] Phân biệt được: Syntax Analysis sinh Parse Tree, Semantic Analysis thực hiện kiểm tra kiểu (Type Checking).
- [ ] Hiểu rõ cơ chế JIT Compiler: Dịch Bytecode thành Native Code tại runtime cho các đoạn mã Hotspot.
- [ ] Nhớ triết lý: Mệnh lệnh (C) tập trung vào "How", Khai báo (SQL, Hàm) tập trung vào "What".
- [ ] Thuộc tên các ngôn ngữ lịch sử: FORTRAN (khoa học), COBOL (kinh doanh), PROLOG (logic), LISP (hàm/AI).
