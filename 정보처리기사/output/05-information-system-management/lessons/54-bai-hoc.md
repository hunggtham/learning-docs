# 프로그래밍 언어의 분류 (Classification of Programming Languages)

## 학습 목표 (Mục tiêu)
- Phân loại toàn diện các thế hệ và mô hình ngôn ngữ lập trình: Thủ tục (절차적), Hướng đối tượng (객체지향), Kịch bản (스크립트), Khai báo/Logic (선언형/함수형).
- Nắm vững đặc trưng và mục đích ra đời của các ngôn ngữ thủ tục kinh điển: C, FORTRAN, COBOL, ALGOL.
- Hiểu rõ lịch sử phát triển và thuộc tính của các ngôn ngữ hướng đối tượng: Simula, Smalltalk, C++, Java.
- Phân biệt rõ phạm vi thực thi của các ngôn ngữ kịch bản Client-side (JavaScript) và Server-side (PHP, Python).

## 핵심 키워드 (Từ khóa)
- **절차적 언어 (Procedural)**: FORTRAN (khoa học tính toán), COBOL (nghiệp vụ tài chính, 4 DIVISION), ALGOL (tổ phụ của C/Pascal), C (phát triển UNIX).
- **객체지향 언어 (Object-Oriented)**: Simula (ngôn ngữ OOP đầu tiên), Smalltalk (OOP thuần túy, GUI đầu tiên), C++ (mở rộng từ C), Java (độc lập nền tảng JVM).
- **스크립트 언어 (Scripting)**: Client-side (JavaScript), Server-side (PHP, Python, Ruby).
- **선언형/AI 언어 (Declarative/AI)**: LISP (xử lý danh sách), PROLOG (lập trình logic).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [04-programming-language/03-bai-hoc.md](../../04-programming-language/lessons/03-bai-hoc.md) (Tổng quan các ngôn ngữ lập trình thủ tục).
- Liên kết với [04-programming-language/64-bai-hoc.md](../../04-programming-language/lessons/64-bai-hoc.md) (Lịch sử Simula, Smalltalk và Java OOP).
- Liên kết với [04-programming-language/83-bai-hoc.md](../../04-programming-language/lessons/83-bai-hoc.md) (Ngôn ngữ khai báo và AI: LISP, PROLOG).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh qua từ khóa:
  - "Ngôn ngữ dùng để viết lại hệ điều hành UNIX" $\rightarrow$ **C**.
  - "Ngôn ngữ đầu tiên đưa ra khái niệm hướng đối tượng Class/Object" $\rightarrow$ **Simula**.
  - "Ngôn ngữ hướng đối tượng thuần túy đầu tiên có giao diện GUI" $\rightarrow$ **Smalltalk**.
  - "Xử lý nghiệp vụ hành chính, cấu trúc văn bản tiếng Anh gồm 4 DIVISION" $\rightarrow$ **COBOL**.
  - "Tính toán công thức khoa học kỹ thuật đầu tiên" $\rightarrow$ **FORTRAN**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Ngôn ngữ lập trình thủ tục (Procedural Languages)
| Ngôn ngữ | Xuất xứ / Tác giả | Đặc trưng kỹ thuật và Mục đích sử dụng |
| :--- | :--- | :--- |
| **FORTRAN** | John Backus (IBM, 1957) | Ngôn ngữ bậc cao đầu tiên, chuyên dùng cho **tính toán khoa học và kỹ thuật** (Formula Translation) |
| **COBOL** | Grace Hopper / CODASYL | Chuyên dùng cho **xử lý nghiệp vụ thương mại, kế toán và hành chính**; văn phong tiếng Anh tự nhiên; cấu trúc chương trình gồm **4 phân khu (4 DIVISION)**: Identification, Environment, Data, Procedure |
| **ALGOL** | Nhóm nghiên cứu quốc tế | Ngôn ngữ tính toán khoa học, là **tổ hợp và mô hình gốc (모체)** đặt nền móng cú pháp cho Pascal và C |
| **C** | Dennis Ritchie (Bell Labs, 1972) | Phát triển nhằm mục đích **viết lại nhân hệ điều hành UNIX**; hỗ trợ thao tác bộ nhớ trực tiếp qua con trỏ (Pointer); tính linh hoạt cao |

#### 2. Ngôn ngữ lập trình hướng đối tượng (Object-Oriented Languages)
- **Simula (Simula 67)**: Do Ole-Johan Dahl và Kristen Nygaard phát triển tại Na Uy. Được công nhận là **ngôn ngữ lập trình hướng đối tượng đầu tiên trên thế giới**, lần đầu tiên đưa vào các khái niệm Class, Object, Kế thừa.
- **Smalltalk**: Do Alan Kay và nhóm Xerox PARC phát triển. Là ngôn ngữ **OOP thuần túy 100% (Pure OOP)** thế hệ đầu tiên, mọi thực thể kể cả số nguyên đều là đối tượng; là ngôn ngữ đầu tiên cung cấp môi trường lập trình có giao diện đồ họa **GUI** hoàn chỉnh.
- **C++**: Do Bjarne Stroustrup phát triển tại Bell Labs (ban đầu gọi là "C with Classes"). Bổ sung các tính năng OOP (Lớp, Kế thừa, Đa hình, Nạp chồng toán tử, Template) vào nền tảng tốc độ cao của C.
- **Java**: Do James Gosling tại Sun Microsystems phát triển. Hoạt động trên môi trường máy ảo **JVM** (triết lý "Write Once, Run Anywhere"), tích hợp sẵn Garbage Collector tự động dọn dẹp bộ nhớ, hỗ trợ mạnh mẽ đa luồng (Multi-threading) và lập trình phân tán qua mạng.

#### 3. Ngôn ngữ kịch bản (Scripting Languages)
- **Client-side Scripting (Phía máy khách)**:
  - **JavaScript**: Ngôn ngữ kịch bản chạy trực tiếp trên trình duyệt web của người dùng, dùng để xử lý tương tác giao diện động và sự kiện DOM.
  - **VBScript**: Ngôn ngữ kịch bản của Microsoft dựa trên Visual Basic, chủ yếu dùng cho các ứng dụng nội bộ Windows và điều khiển ActiveX.
- **Server-side Scripting (Phía máy chủ)**:
  - **Python**: Cú pháp ngắn gọn, định kiểu động, mạnh mẽ về phân tích dữ liệu, AI và phát triển web (Django, Flask).
  - **PHP**: Ngôn ngữ kịch bản nhúng mã vào HTML chuyên dụng cho phát triển ứng dụng web động phía máy chủ.
  - **Ruby**: Ngôn ngữ hướng đối tượng thanh lịch, kết hợp cùng framework Rails để phát triển web nhanh chóng.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Ngôn ngữ khai báo và Trí tuệ nhân tạo (AI Languages)
```
          ┌────────────────────────────────────────────────────────┐
          │             NGÔN NGỮ KHAI BÁO & TRÍ TUỆ NHÂN TẠO       │
          ├──────────────────────────┬─────────────────────────────┤
          │  LISP (List Processing)  │  PROLOG (Logic Programming) │
          │  - Tác giả: John McCarthy│  - Tác giả: Alain Colmerauer│
          │  - Dạng dữ liệu: Danh sách│ - Dựa trên vị từ logic hình │
          │  - Ngôn ngữ hàm (FP)     │    thức (Horn Clauses)      │
          │  - Tiên phong nghiên cứu │  - Cơ chế suy diễn tự động  │
          │    hệ chuyên gia AI      │    (Inference Engine)       │
          └──────────────────────────┴─────────────────────────────┘
```

#### 2. Bốn phân khu (DIVISION) bắt buộc trong cấu trúc chương trình COBOL
1. **IDENTIFICATION DIVISION**: Khai báo tên chương trình, tác giả, ngày viết.
2. **ENVIRONMENT DIVISION**: Khai báo môi trường máy tính và các tệp tin liên kết phần cứng.
3. **DATA DIVISION**: Khai báo cấu trúc các biến, bản ghi và tệp dữ liệu xử lý.
4. **PROCEDURE DIVISION**: Chứa các thuật toán xử lý logic nghiệp vụ và câu lệnh thực thi.

---

### 복습 체크리스트
- [ ] Bốn ngôn ngữ lập trình thủ tục kinh điển (C, FORTRAN, COBOL, ALGOL) được thiết kế cho những mục đích chính nào?
- [ ] Ngôn ngữ nào được coi là ngôn ngữ OOP đầu tiên và ngôn ngữ nào là ngôn ngữ thuần OOP đầu tiên có GUI?
- [ ] Cấu trúc một chương trình COBOL chuẩn gồm có những phân khu (DIVISION) nào?
- [ ] Sự khác nhau cơ bản giữa ngôn ngữ kịch bản Client-side và Server-side là gì?
