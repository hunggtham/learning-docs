# 275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)

## 학습 목표 (Mục tiêu)
- Nắm vững hệ thống phân loại ngôn ngữ lập trình theo mô hình hình thái (Programming Paradigms): Ngôn ngữ mệnh lệnh/thủ tục (절차적/명령형 언어), Ngôn ngữ hướng đối tượng (객체지향 언어), và Ngôn ngữ khai báo (선언형 언어: Hàm số và Logic).
- Phân biệt rõ sự khác nhau giữa cách tiếp cận mệnh lệnh ("Làm như thế nào" - *How to do*) và cách tiếp cận khai báo ("Làm cái gì" - *What to do*).
- Nhận diện các ngôn ngữ kinh điển phục vụ nghiên cứu trí tuệ nhân tạo (AI): LISP (xử lý danh sách) và PROLOG (suy luận logic toán học).

## 핵심 키워드 (Từ khóa)
- 프로그래밍 패러다임 (Programming Paradigms)
- 절차적/명령형 언어 (Procedural/Imperative: C, FORTRAN, COBOL)
- 객체지향 언어 (Object-Oriented: Java, C++, Smalltalk)
- 선언형 언어 (Declarative Languages - What 중심)
- 함수형 언어 (Functional: LISP, Haskell)
- 논리형 언어 (Logic: PROLOG - AI 추론)
- 구조화 문서 (Markup: XML, HTML)

## 선행·연결 개념 (Kiến thức liên kết)
- [82-bai-hoc.md](82-bai-hoc.md): Vòng lặp và các từ khóa điều khiển luồng `break`/`continue`.
- [84-bai-hoc.md](84-bai-hoc.md): Khái niệm kiến trúc hướng dịch vụ SOA và kỹ thuật Mashup.
- [53-bai-hoc.md](53-bai-hoc.md): Lịch sử các ngôn ngữ hướng thủ tục kinh điển (C, FORTRAN, COBOL).

## 읽는 방법 (Cách đọc)
- Phân loại ngôn ngữ thi cử:
  - Hỏi "Ngôn ngữ nào tập trung vào **What (Cái gì)** thay vì How (Như thế nào)?" $\rightarrow$ Chọn **선언형 언어 (Declarative Language)**.
  - Ngôn ngữ AI cổ điển:
    - **LISP:** Gắn liền với cấu trúc danh sách liên kết (List Processing), hàm đệ quy.
    - **PROLOG:** Gắn liền với suy luận logic vị từ (Predicate Logic), cơ sở tri thức hệ chuyên gia.
    - **Haskell:** Ngôn ngữ hàm thuần khiết (Pure Functional), không có hiệu ứng phụ (No Side Effects).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân loại tổng quát các mô hình ngôn ngữ lập trình:**

| Mô hình ngôn ngữ | Đại diện tiêu biểu | Triết lý & Cách tiếp cận | Đặc trưng kỹ thuật thi cử |
| :--- | :--- | :--- | :--- |
| **Mệnh lệnh / Thủ tục** (Procedural / Imperative) | **C, FORTRAN, COBOL, ALGOL, Pascal** | Tập trung vào **"Làm như thế nào (How)"**; tuần tự thay đổi trạng thái của bộ nhớ máy tính qua các lệnh gán. | Rất gần với kiến trúc Von Neumann; hiệu năng tính toán cao; lập trình viên tự quản lý bộ nhớ. |
| **Hướng đối tượng** (Object-Oriented) | **Java, C++, C#, Smalltalk, Python** | Xem chương trình là một xã hội các **đối tượng tự chủ** trao đổi thông điệp với nhau. | Đóng gói (Encapsulation), Kế thừa (Inheritance), Đa hình (Polymorphism); tái sử dụng mã nguồn vượt trội. |
| **Hàm số** (Functional) | **LISP, Haskell, Clojure, Scala** | Xem tính toán là việc lượng giá các **hàm toán học thuần khiết (Pure Functions)**, cấm thay đổi trạng thái biến (Immutable). | Không có hiệu ứng lề (Side-effect free); rất mạnh trong xử lý tính toán song song đa lõi và AI. |
| **Logic** (Logic Programming) | **PROLOG** | Dựa trên **Logic vị từ hình thức (First-Order Predicate Logic)**; mô tả sự thật (Facts) và quy tắc (Rules). | Máy tính tự động thực hiện suy diễn lùi (Backward Chaining) để tìm lời giải; dùng trong các hệ chuyên gia AI. |
| **Tài liệu cấu trúc** (Markup) | **HTML, XML, SGML** | Định nghĩa cấu trúc và ngữ nghĩa của dữ liệu thông qua các cặp thẻ (Tags). | Phục vụ trao đổi dữ liệu giữa các hệ thống không cùng nền tảng phần mềm. |

- **2. Điểm nhấn thi cử của các ngôn ngữ đặc thù:**
  - **LISP (List Processor - John McCarthy, 1958):** Là ngôn ngữ nền tảng của ngành trí tuệ nhân tạo (AI); toàn bộ chương trình và dữ liệu đều có cấu trúc dạng danh sách ngoặc đơn `(operator arg1 arg2)`.
  - **PROLOG (PROgramming in LOGic - Alain Colmerauer, 1972):** Khai báo các tiên đề và quy tắc logic; hệ thống tự động tìm kiếm đường suy luận để trả lời câu hỏi truy vấn.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự hội tụ của các ngôn ngữ hiện đại:**
  - Các ngôn ngữ hiện đại như Java (từ Java 8 với Lambda Expression và Stream API), Python, JavaScript, và C# đều tích hợp sâu các đặc tính của lập trình hàm (Functional Programming) vào mô hình hướng đối tượng, giúp code ngắn gọn, an toàn và dễ chạy song song.

### 복습 체크리스트
- [ ] Phân biệt được sự khác biệt giữa Imperative (How - Thủ tục) và Declarative (What - Khai báo).
- [ ] Nhớ LISP là ngôn ngữ xử lý danh sách dùng trong trí tuệ nhân tạo.
- [ ] Nhớ PROLOG là ngôn ngữ logic dựa trên luật suy diễn dùng trong hệ chuyên gia AI.
- [ ] Kể tên được các ngôn ngữ hướng đối tượng tiêu biểu: Smalltalk, Java, C++.
