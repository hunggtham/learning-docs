# 108. 도메인 (Domain)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa chuẩn xác của Miền giá trị (`도메인 / Domain`): Tập hợp tất cả các giá trị nguyên tử (`원자값 / Atomic values`) có cùng kiểu dữ liệu mà một thuộc tính (`속성 / Attribute`) cụ thể được phép nhận.
- Hiểu rõ vai trò của Miền giá trị trong việc đảm bảo Ràng buộc toàn vẹn miền (`도메인 무결성 / Domain Integrity`).
- Nhận thức được mối liên hệ giữa kiểu dữ liệu (Data Type) trong lập trình SQL và khái niệm Miền giá trị trong lý thuyết quan hệ.

## 핵심 키워드 (Từ khóa)
- 도메인 (Miền giá trị / Domain)
- 원자값 (Giá trị nguyên tử / Atomic Value)
- 도메인 무결성 (Toàn vẹn miền giá trị / Domain Integrity)
- 속성 (Thuộc tính / Attribute)
- 데이터 타입 (Kiểu dữ liệu)
- CHECK 제약조건 (Ràng buộc CHECK trong SQL)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([12-bai-hoc.md](12-bai-hoc.md), [15-bai-hoc.md](15-bai-hoc.md), [40-bai-hoc.md](40-bai-hoc.md)):** Sau khi hiểu rằng Thuộc tính (Attribute) là đơn vị logic nhỏ nhất của bảng, Miền giá trị chính là tập hợp không gian giá trị hợp lệ quy định tính đúng đắn cho thuộc tính đó.
- **Tiếp nối sang bài sau ([42-bai-hoc.md](42-bai-hoc.md), [43-bai-hoc.md](43-bai-hoc.md)):** Khái niệm miền giá trị là cơ sở cho Giải tích quan hệ miền (`도메인 관계해석`) và dạng chuẩn 1NF (mọi miền giá trị phải là nguyên tử).

## 읽는 방법 (Cách đọc)
- Học thuộc định nghĩa cốt lõi trong đề thi: **"하나의 애트리뷰트가 취할 수 있는 같은 타입의 원자값들의 집합" $\rightarrow$ 도메인 (Domain)**.
- Ghi nhớ ví dụ kinh điển:
  - Thuộc tính `성별 (Giới tính)` $\rightarrow$ Domain là `{남, 여}`.
  - Thuộc tính `학점 (Điểm chữ)` $\rightarrow$ Domain là `{A, B, C, D, F}`.
  - Thuộc tính `월 (Tháng)` $\rightarrow$ Domain là tập số nguyên từ 1 đến 12.

---

## 108. 도메인 (Domain)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Định nghĩa kỹ thuật của Miền giá trị (도메인의 정의):**
  - Là **tập hợp các giá trị nguyên tử (`원자값들의 집합`) có cùng kiểu dữ liệu** mà một thuộc tính được phép tiếp nhận trong cơ sở dữ liệu.
  - Tính nguyên tử (`원자성`): Mỗi phần tử trong miền giá trị là một giá trị đơn nhất, không thể phân chia nhỏ hơn nữa theo quan điểm logic của hệ thống.
- **2. Mối quan hệ giữa Miền giá trị và Toàn vẹn dữ liệu:**
  - **도메인 무결성 (Domain Integrity):** Ràng buộc quy định rằng mọi giá trị được nhập vào cột dữ liệu bắt buộc phải là một phần tử thuộc Miền giá trị đã được định nghĩa.
  - Hệ quản trị DBMS bảo đảm toàn vẹn miền thông qua: Kiểu dữ liệu (`INT`, `VARCHAR`, `DATE`), độ dài tối đa, ràng buộc `CHECK`, hoặc kiểu dữ liệu do người dùng tự định nghĩa (`CREATE DOMAIN`).
- **3. Cú pháp DDL tạo Miền giá trị trong chuẩn SQL:**
  ```sql
  CREATE DOMAIN GIOI_TINH CHAR(1)
      DEFAULT 'M'
      CONSTRAINT CHK_GT CHECK (VALUE IN ('M', 'F'));
  ```
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Tập hợp các giá trị nguyên tử cùng kiểu mà một thuộc tính có thể nhận được gọi là gì?"* $\rightarrow$ Đáp án: **도메인 (Domain)**.
  - Đề hỏi: *"Nếu nhập điểm thi là 15 (trong khi thang điểm là 0-10) thì vi phạm quy tắc toàn vẹn nào?"* $\rightarrow$ Đáp án: **도메인 무결성 (Domain Integrity)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh giữa Kiểu dữ liệu và Miền giá trị:**
  - Kiểu dữ liệu (`INT`): Cho phép nhận bất kỳ số nguyên nào từ $-2^{31}$ đến $2^{31}-1$.
  - Miền giá trị `TuoiHocSinh`: Là tập số nguyên bị giới hạn chặt chẽ trong khoảng từ $6$ đến $18$.
  - Do đó, Miền giá trị mang ngữ nghĩa nghiệp vụ thực tế hẹp hơn và chính xác hơn kiểu dữ liệu phần cứng thuần túy.

### 복습 체크리스트
- [ ] Học thuộc định nghĩa 도메인: 같은 타입의 원자값들의 집합.
- [ ] Nêu được 2 ví dụ thực tế về miền giá trị (Giới tính, Điểm số).
- [ ] Giải thích được vai trò của 도메인 무결성 trong việc ngăn chặn dữ liệu rác.
- [ ] Phân biệt được sự khác nhau giữa Kiểu dữ liệu chung và Miền giá trị nghiệp vụ.
