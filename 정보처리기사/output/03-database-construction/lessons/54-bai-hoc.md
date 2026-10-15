# 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò và đặc trưng của khung làm việc ánh xạ SQL **MyBatis**: Tách biệt mã lệnh SQL ra khỏi mã nguồn ứng dụng (Java), cho phép quản lý SQL bằng tệp XML hoặc Annotation, rất thân thiện với lập trình viên và dễ dàng tối ưu hóa truy vấn.
- So sánh sự khác nhau cốt lõi giữa **Trình ánh xạ SQL (SQL Mapper: MyBatis)** và **Trình ánh xạ quan hệ - đối tượng (ORM: JPA, Hibernate)**.
- Khắc sâu Thứ tự ưu tiên toán tử trong câu lệnh SQL (`연산자 우선순위`): **Toán tử số học > Toán tử so sánh quan hệ > Toán tử logic**, và trong nhóm logic: **`NOT` > `AND` > `OR`**.
- Tổng hợp và hệ thống hóa lại các khái niệm xuyên suốt môn học: Phân tích ma trận CRUD và Hệ thống ca-ta-lô (System Catalog).

## 핵심 키워드 (Từ khóa)
- MyBatis (프레임워크 / SQL Mapper Framework)
- ORM (Object-Relational Mapping / JPA, Hibernate)
- SQL 매핑 (Ánh xạ SQL qua tệp XML)
- 연산자 우선순위 (Thứ tự ưu tiên toán tử trong SQL / Operator Precedence)
- 산술 연산자 (Toán tử số học: `*`, `/`, `+`, `-`)
- 관계 연산자 (Toán tử so sánh: `=`, `<>`, `<`, `>`, `LIKE`, `IN`, `BETWEEN`)
- 논리 연산자 (Toán tử logic: `NOT` > `AND` > `OR`)
- CRUD 매트릭스 / 시스템 카탈로그

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([20-bai-hoc.md](20-bai-hoc.md), [28-bai-hoc.md](28-bai-hoc.md), [30-bai-hoc.md](30-bai-hoc.md), [44-bai-hoc.md](44-bai-hoc.md), [45-bai-hoc.md](45-bai-hoc.md), [53-bai-hoc.md](53-bai-hoc.md)):** Đây là bài học tổng kết toàn bộ Môn 3: Xây dựng Cơ sở dữ liệu (03-database-construction), kết nối từ tầng lý thuyết mô hình quan hệ, ngôn ngữ SQL đến tầng ứng dụng phần mềm thực tế.
- **Tiếp nối sang Môn 4 (04-programming-language):** Kiến thức về thứ tự ưu tiên toán tử và các framework kết nối CSDL (JDBC, MyBatis, ORM) sẽ là cầu nối trực tiếp sang các bài học về lập trình Java, Python và C.

## 읽는 방법 (Cách đọc)
- Học thuộc thứ tự ưu tiên toán tử SQL theo câu khẩu quyết:
  > **Toán - Quan - Lo (Toán học > Quan hệ so sánh > Logic)**.
- Riêng đối với các toán tử logic trong mệnh đề WHERE, thứ tự bắt buộc là:
  > **`NOT` chạy trước $\rightarrow$ đến `AND` $\rightarrow$ cuối cùng là `OR`**.
- Nhớ đặc điểm nổi bật nhất của MyBatis: **Tách biệt câu lệnh SQL ra khỏi mã Java, lưu trong tệp XML**.

---

## 22. 기타 주요 개념 (Các khái niệm quan trọng khác)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Khung làm việc MyBatis và so sánh với ORM:**
  - **MyBatis là gì?**
    - Là một Khung làm việc bền vững (Persistence Framework) thuộc thể loại **SQL Mapper**.
    - Cho phép viết các câu lệnh SQL gần như nguyên bản, tách rời mã SQL phức tạp ra khỏi mã nguồn logic nghiệp vụ của Java bằng cách lưu trữ trong các **tệp cấu hình XML** hoặc Annotation.
    - Hỗ trợ lập trình viên kiểm soát trực tiếp từng câu lệnh SQL, rất phù hợp với các hệ thống cần tối ưu hóa hiệu năng câu truy vấn chuyên sâu (SQL-friendly).
  - **So sánh SQL Mapper (MyBatis) vs ORM (JPA / Hibernate):**
    | Tiêu chí so sánh | SQL Mapper (MyBatis) | ORM (JPA, Hibernate) |
    |---|---|---|
    | **Đối tượng ánh xạ** | Ánh xạ giữa **Câu lệnh SQL** với các hàm của Java | Ánh xạ trực tiếp giữa **Bảng CSDL (Table)** với **Lớp đối tượng (Class / Entity)** |
    | **Cách xử lý truy vấn** | Lập trình viên **tự viết mã SQL thủ công** | Framework **tự động sinh mã SQL** dựa trên mô hình đối tượng |
    | **Ưu điểm nổi bật** | Tối ưu hóa truy vấn phức tạp cực kỳ linh hoạt; dễ học với người giỏi SQL | Giảm thiểu mã lặp lại; độc lập với từng loại CSDL cụ thể |

- **2. Bảng Thứ tự ưu tiên toán tử trong SQL (연산자 우선순위):**
  | Thứ tự ưu tiên | Nhóm toán tử | Danh sách các toán tử | Quy tắc xử lý |
  |:---:|---|---|---|
  | **1** | **Dấu ngoặc đơn** | `( )` | Biểu thức bên trong ngoặc luôn được tính toán trước tiên |
  | **2** | **Toán tử số học** | Nhân, Chia (`*`, `/`) $\rightarrow$ Cộng, Trừ (`+`, `-`) | Theo quy tắc toán học thông thường |
  | **3** | **Toán tử nối chuỗi** | `\|\|` (Oracle, Postgres) hoặc `+` (SQL Server) | Ghép nối các chuỗi ký tự |
  | **4** | **Toán tử quan hệ / so sánh** | `=`, `<>`, `!=`, `<`, `<=`, `>`, `>=`, `BETWEEN`, `IN`, `LIKE`, `IS NULL` | Trả về kết quả chân lý logic (TRUE, FALSE, UNKNOWN) |
  | **5** | **Toán tử Logic: NOT** | `NOT` | Phủ định giá trị logic; có độ ưu tiên cao nhất trong nhóm logic |
  | **6** | **Toán tử Logic: AND** | `AND` | Phép hội logic; được thực thi trước toán tử OR |
  | **7** | **Toán tử Logic: OR** | `OR` | Phép tuyển logic; được thực thi sau cùng trong nhóm logic |

- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Thứ tự thực hiện của các toán tử logic NOT, AND, OR là gì?"* $\rightarrow$ Đáp án: **`NOT` $\rightarrow$ `AND` $\rightarrow$ `OR`**.
  - Trong biểu thức: `WHERE A = 1 OR B = 2 AND C = 3`:
    - DBMS sẽ thực hiện `(B = 2 AND C = 3)` trước, sau đó mới xét đến `OR A = 1`.
  - Đề hỏi: *"Framework nào giúp tách mã SQL ra khỏi Java và lưu trong file XML?"* $\rightarrow$ Đáp án: **MyBatis**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa bài toán bẫy logic trong SQL:**
  - Giả sử câu lệnh:
    ```sql
    SELECT * FROM NHAN_VIEN
    WHERE PhongBan = 'IT' OR PhongBan = 'KeToan' AND Luong >= 3000;
    ```
  - Do toán tử `AND` có độ ưu tiên cao hơn `OR`, câu lệnh trên được hệ thống hiểu ngầm là:
    ```sql
    WHERE PhongBan = 'IT' OR (PhongBan = 'KeToan' AND Luong >= 3000);
    ```
    - Kết quả: Tất cả nhân viên IT (bất kể lương cao hay thấp) đều được chọn, cộng với các nhân viên Kế toán có lương $\ge 3000$.
  - Nếu muốn chọn nhân viên thuộc 1 trong 2 phòng VÀ có lương $\ge 3000$, lập trình viên bắt buộc phải thêm dấu ngoặc đơn:
    ```sql
    WHERE (PhongBan = 'IT' OR PhongBan = 'KeToan') AND Luong >= 3000;
    ```

### 복습 체크리스트
- [ ] Nhớ thứ tự ưu tiên lớn: Toán học > So sánh quan hệ > Logic.
- [ ] Khắc ghi thứ tự ưu tiên của nhóm logic: NOT > AND > OR.
- [ ] Nắm được vai trò của MyBatis là SQL Mapper giúp tách SQL ra file XML.
- [ ] Phân biệt được sự khác nhau giữa MyBatis (tự viết SQL) và JPA/Hibernate (tự sinh SQL).
