# 116-121. 관계대수 (Relational Algebra)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất kỹ thuật của Đại số quan hệ (`관계대수 / Relational Algebra`): Ngôn ngữ truy vấn mang tính thủ tục (`절차적 언어`), chỉ rõ quy trình và thứ tự thực hiện để lấy dữ liệu.
- Phân biệt chi tiết ký hiệu, cú pháp và cơ chế hoạt động của 4 toán tử quan hệ thuần túy (`순수 관계 연산자`): **Select ($\sigma$)**, **Project ($\pi$)**, **Join ($\bowtie$)**, và **Division ($\div$)**.
- Phân biệt toán tử quan hệ thuần túy với các toán tử tập hợp (`일반 집합 연산자`: Union, Intersection, Difference, Cartesian Product).
- So sánh Đại số quan hệ (`관계대수` - Thủ tục) với Đại số giải tích quan hệ (`관계해석` - Phi thủ tục).

## 핵심 키워드 (Từ khóa)
- 관계대수 (Đại số quan hệ / Relational Algebra)
- 절차적 언어 (Ngôn ngữ thủ tục / Procedural Language)
- Select (시그마 $\sigma$ / Phép chọn theo hàng)
- Project (파이 $\pi$ / Phép chiếu theo cột)
- Join (조인 $\bowtie$ / Phép kết nối)
- Division (디비전 $\div$ / Phép chia quan hệ)
- 관계해석 (Đại số giải tích quan hệ / Relational Calculus)
- 비절차적 언어 (Ngôn ngữ phi thủ tục / Non-procedural)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([08-bai-hoc.md](08-bai-hoc.md), [12-bai-hoc.md](12-bai-hoc.md)):** Đại số quan hệ hoạt động trực tiếp trên cấu trúc Relation (Tuple và Attribute), nhận đầu vào là các quan hệ và sinh ra kết quả là quan hệ mới.
- **Tiếp nối sang các bài sau ([17-bai-hoc.md](17-bai-hoc.md), [18-bai-hoc.md](18-bai-hoc.md)):** Các thao tác tách và nối bảng trong quá trình Chuẩn hóa dữ liệu (`정규화`) hoàn toàn dựa trên phép Project ($\pi$) để tách và Natural Join ($\bowtie_N$) để ghép lại không mất mát thông tin.

## 읽는 방법 (Cách đọc)
- Học thuộc ký hiệu toán học Hy Lạp: **$\sigma$ là Select (hàng ngang)**, **$\pi$ là Project (cột dọc)**.
- Ghi nhớ bản chất: **Đại số quan hệ = Thủ tục (nêu RÕ CÁCH LÀM)**; **Đại số giải tích quan hệ = Phi thủ tục (chỉ nêu KẾT QUẢ CẦN GÌ)**.

---

## 116-121. 관계대수 (Relational Algebra)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bản chất của Đại số quan hệ (관계대수의 본질):**
  - Là ngôn ngữ thao tác dữ liệu hình thức mang tính **thủ tục (`절차적 언어`)**.
  - Người dùng phải mô tả rõ **thao tác nào được thực hiện theo trình tự nào** để thu được kết quả mong muốn.
  - Tính đóng (Closure property): Cả toán hạng đầu vào và kết quả đầu ra đều là Quan hệ (Relation).
- **2. Bốn toán tử quan hệ thuần túy (순수 관계 연산자 4가지):**
  | Toán tử | Ký hiệu | Chiều thao tác | Ý nghĩa & Quy tắc xử lý |
  |---|:---:|---|---|
  | **Select** | $\sigma$ (Sigma) | **Ngang (수평 연산)** | Trích xuất các **bộ (hàng / tuple)** thỏa mãn vị từ điều kiện cho trước. Ví dụ: $\sigma_{Diem \ge 8}(SINH\_VIEN)$ lấy các sinh viên có điểm $\ge 8$. |
  | **Project** | $\pi$ (Pi) | **Dọc (수직 연산)** | Trích xuất các **thuộc tính (cột / attribute)** được chỉ định trong danh sách. Ví dụ: $\pi_{MaSV, HoTen}(SINH\_VIEN)$. **Tự động loại bỏ các bộ trùng lặp** trong kết quả. |
  | **Join** | $\bowtie$ (Bowtie) | Kết hợp bảng | Ghép 2 bảng lại thành 1 bảng mới dựa trên thuộc tính chung; **자연 조인 (Natural Join, $\bowtie_N$):** Ghép bằng thuộc tính chung và tự động loại bỏ cột trùng lặp; **세타 조인 (Theta Join):** Ghép theo phép so sánh ($\theta \in \{=, <, \le, >, \ge, \ne\}$). |
  | **Division** | $\div$ | Phép chia | Lấy các giá trị thuộc tính của quan hệ $R$ xuất hiện kết đôi với **TOÀN BỘ** các giá trị thuộc tính của quan hệ $S$. |

- **3. Bốn toán tử tập hợp thông thường (일반 집합 연산자):**
  - **합집합 (UNION, $\cup$):** Tập hợp tất cả các bộ của cả 2 quan hệ, tự động khử trùng lặp. Hai quan hệ phải khả hợp (cùng số lượng và miền thuộc tính).
  - **교집합 (INTERSECTION, $\cap$):** Tập hợp các bộ xuất hiện đồng thời ở cả hai quan hệ.
  - **차집합 (DIFFERENCE, $-$):** Tập hợp các bộ có trong $R$ nhưng không có trong $S$.
  - **교차곱 (CARTESIAN PRODUCT, $\times$):** Tập hợp tất cả các cặp có thể giữa bộ của $R$ và bộ của $S$.
    - $Degree(R \times S) = Degree(R) + Degree(S)$
    - $Cardinality(R \times S) = Cardinality(R) \times Cardinality(S)$
- **4. So sánh cốt lõi: 관계대수 (Đại số quan hệ) vs 관계해석 (Giải tích quan hệ):**
  | Tiêu chí | 관계대수 (Relational Algebra) | 관계해석 (Relational Calculus) |
  |---|---|---|
  | **Đặc trưng ngôn ngữ** | **절차적 언어 (Thủ tục)** | **비절차적 언어 (Phi thủ tục)** |
  | **Cách tiếp cận** | Chỉ rõ **cách tìm (How to find)** dữ liệu qua chuỗi phép toán | Chỉ rõ **cần dữ liệu gì (What to find)** bằng biểu thức toán |
  | **Nền tảng lý thuyết** | Đại số tập hợp và toán tử quan hệ | Giải tích vị từ toán học (Predicate Calculus của E.F. Codd) |
  | **Ký hiệu đặc trưng** | $\sigma, \pi, \bowtie, \div, \cup, \cap, -, \times$ | Ký hiệu lượng từ: $\forall$ (For all), $\exists$ (There exists) |
- **주의/함정 (Bẫy đề thi):**
  - Đề hỏi: *"Phép toán nào loại bỏ các hàng trùng lặp sau khi trích xuất cột?"* $\rightarrow$ Đáp án: **Project ($\pi$)**.
  - Đề hỏi: *"Phép toán nào là 수평 연산 (thao tác ngang)?"* $\rightarrow$ Đáp án: **Select ($\sigma$)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa trực quan bài toán Division ($\div$):**
  - Giả sử bảng $R(MaSV, MaMonHoc)$ ghi nhận các môn mà sinh viên đã đăng ký.
  - Bảng $S(MaMonHoc)$ gồm danh sách các môn bắt buộc: `{CS101, CS102}`.
  - Biểu thức $R \div S$:
    - Trả về danh sách `MaSV` của những sinh viên đã đăng ký **ĐỦ CẢ HAI MÔN** `CS101` và `CS102`.
    - Sinh viên nào chỉ đăng ký một môn sẽ bị loại bỏ.
- **Tương quan với ngôn ngữ SQL hiện đại:**
  - `Select` ($\sigma$) tương ứng mệnh đề `WHERE`.
  - `Project` ($\pi$) tương ứng mệnh đề `SELECT DISTINCT`.
  - `Join` ($\bowtie$) tương ứng mệnh đề `FROM R JOIN S ON ...`.

### 복습 체크리스트
- [ ] Phân biệt được ký hiệu $\sigma$ (Select - lọc hàng) và $\pi$ (Project - chọn cột).
- [ ] Nhớ rõ 관계대수 là 절차적 언어, còn 관계해석 là 비절차적 언어.
- [ ] Nắm được cơ chế của phép chia Division ($\div$): chọn bộ chứa toàn bộ tập con.
- [ ] Tính thành thạo Degree và Cardinality khi thực hiện Cartesian Product ($\times$).
