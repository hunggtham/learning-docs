# 226 - 227. 데이터베이스 접속 기술 (Database Connectivity)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế hoạt động và kiến trúc của các công nghệ giao tiếp và kết nối cơ sở dữ liệu: **JDBC (Java Database Connectivity)** và **ODBC (Open Database Connectivity)**.
- Phân biệt rõ phạm vi áp dụng, tính độc lập ngôn ngữ và hệ điều hành giữa JDBC (chuyên biệt cho hệ sinh thái Java) và ODBC (tiêu chuẩn mở của Microsoft cho đa ngôn ngữ).
- Hiểu cấu trúc phân tầng kết nối thông qua trình quản lý điều khiển (Driver Manager) và các loại hình trình điều khiển kết nối cơ sở dữ liệu.

## 핵심 키워드 (Từ khóa)
- 데이터베이스 접속 기술 (Database Connectivity)
- JDBC (Java DataBase Connectivity - Sun Microsystems)
- ODBC (Open DataBase Connectivity - Microsoft)
- 드라이버 매니저 (Driver Manager)
- 플랫폼 및 DBMS 독립성 (OS & DBMS Independence)
- SQL 실행 및 결과 매핑 (Query Execution & ResultSet)
- ORM 프레임워크 (Object-Relational Mapping: JPA, MyBatis)

## 선행·연결 개념 (Kiến thức liên kết)
- [84-bai-hoc.md](84-bai-hoc.md): Kỹ thuật Mashup và kiến trúc hướng dịch vụ SOA.
- [86-bai-hoc.md](86-bai-hoc.md): Ngôn ngữ thông dịch (Interpreter) và cơ chế thực thi.
- [70-bai-hoc.md](70-bai-hoc.md): Lỗ hổng SQL Injection và giải pháp PreparedStatement trong JDBC.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh hai công nghệ kết nối then chốt:
  - **JDBC:** Nhớ ngay từ khóa **"Java"** $\rightarrow$ API chuẩn của Java do Sun Microsystems thiết kế, cho phép chương trình Java kết nối với bất kỳ cơ sở dữ liệu nào, chạy trên mọi hệ điều hành (độc lập nền tảng nhờ JVM).
  - **ODBC:** Nhớ từ khóa **"Open"** và **"Microsoft"** $\rightarrow$ Tiêu chuẩn công nghiệp mở, cho phép **bất kỳ ngôn ngữ lập trình nào** (C, C++, Visual Basic, Python, v.v.) kết nối tới các hệ quản trị DBMS khác nhau thông qua ODBC Driver.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu toàn diện JDBC vs ODBC:**

| Tiêu chuẩn so sánh | ODBC (Open Database Connectivity) | JDBC (Java Database Connectivity) |
| :--- | :--- | :--- |
| **Hãng khởi xướng** | **Microsoft** (Ra đời năm 1992) | **Sun Microsystems** (Ra đời năm 1997) |
| **Ngôn ngữ hỗ trợ** | **Đa ngôn ngữ** (C, C++, VB, Delphi, Python...) | **Chuyên biệt cho Java** (và ngôn ngữ chạy trên JVM như Kotlin, Scala) |
| **Tính độc lập HĐH** | Ban đầu gắn chặt với Windows; sau này có bản mở rộng trên Linux qua unixODBC. | **Hoàn toàn độc lập hệ điều hành** (Đúng chuẩn triết lý Java "Write Once, Run Anywhere"). |
| **Thành phần điều phối** | **ODBC Driver Manager** | **JDBC Driver Manager** (`java.sql.DriverManager`) |
| **Hiệu năng & Phức tạp** | Tốc độ C/C++ cao nhưng cấu hình DSN (Data Source Name) trên hệ điều hành khá phức tạp. | Dễ cấu hình qua chuỗi kết nối URL (`jdbc:mysql://...`); quản lý kết nối an toàn với Connection Pool. |

- **2. Quy trình 4 bước kết nối và thực thi SQL cơ bản trong JDBC:**
  1. **Nạp Driver (드라이버 로드):** `Class.forName("com.mysql.cj.jdbc.Driver");`
  2. **Tạo kết nối (연결 생성):** `Connection conn = DriverManager.getConnection(url, user, password);`
  3. **Tạo đối tượng câu lệnh và thực thi (SQL 실행):** `PreparedStatement pstmt = conn.prepareStatement(sql);`
  4. **Thu nhận kết quả và giải phóng (결과 처리 및 자원 반납):** `ResultSet rs = pstmt.executeQuery();` rồi gọi `.close()`.

- **3. Sự phát triển lên tầng cao: SQL Mapper và ORM:**
  - Viết mã JDBC thuần túy đòi hỏi nhiều thao tác lặp lại (mở kết nối, gán tham số, đọc `ResultSet`, đóng tài nguyên).
  - Để tăng năng suất, các framework hiện đại được đưa vào sử dụng:
    - **SQL Mapper (MyBatis):** Tách riêng câu lệnh SQL ra tệp XML, tự động ánh xạ tham số và kết quả vào Java Object.
    - **ORM (JPA / Hibernate):** Ánh xạ trực tiếp bảng quan hệ trong CSDL thành các lớp đối tượng Java (Entity), lập trình viên thao tác với DB hoàn toàn thông qua phương thức hướng đối tượng mà không cần viết SQL thủ công.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **4 loại JDBC Driver (JDBC Driver Types):**
  - *Type 1 (JDBC-ODBC Bridge):* Chuyển lệnh JDBC thành lệnh ODBC; phụ thuộc thư viện native của HĐH.
  - *Type 2 (Native-API Driver):* Dùng thư viện C/C++ của nhà cung cấp CSDL trên máy khách.
  - *Type 3 (Network-Protocol Driver):* Đi qua máy chủ trung gian Middleware.
  - *Type 4 (Direct-to-Database Pure Java Driver):* Trình điều khiển viết bằng 100% Java thuần khiết, kết nối trực tiếp qua Socket giao thức mạng của DBMS $\rightarrow$ **Loại phổ biến và hiệu quả nhất hiện nay**.

### 복습 체크리스트
- [ ] Nhớ ODBC là tiêu chuẩn mở của Microsoft dùng cho đa ngôn ngữ (C, C++, VB).
- [ ] Nhớ JDBC là tiêu chuẩn kết nối cơ sở dữ liệu chuyên biệt của nền tảng Java.
- [ ] Nắm được vai trò của Driver Manager: Điều phối và cấp phát kết nối thông qua driver phù hợp.
- [ ] Phân biệt được sự phát triển: JDBC thuần $\rightarrow$ SQL Mapper (MyBatis) $\rightarrow$ ORM (JPA/Hibernate).
