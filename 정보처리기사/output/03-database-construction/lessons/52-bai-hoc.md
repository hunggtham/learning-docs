# 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

## 학습 목표 (Mục tiêu)
- Nắm vững bức tranh toàn cảnh về Ngôn ngữ dữ liệu quan hệ (`관계 데이터 언어`): Phân biệt rõ hai nhánh lý thuyết trụ cột là **Đại số quan hệ (`관계대수` - Thủ tục)** và **Giải tích quan hệ (`관계해석` - Phi thủ tục)**.
- Tổng hợp thành thạo 4 toán tử quan hệ thuần túy: **Select ($\sigma$ - lọc hàng)**, **Project ($\pi$ - chọn cột)**, **Join ($\bowtie$ - kết nối bảng)**, và **Division ($\div$ - phép chia quan hệ)**.
- Củng cố 4 toán tử tập hợp thông thường ($\cup, \cap, -, \times$) và công thức tính toán Bậc (Degree) cùng Lượng số (Cardinality) khi thực hiện phép tích Đề-các.

## 핵심 키워드 (Từ khóa)
- 관계 데이터 언어 (Ngôn ngữ dữ liệu quan hệ / Relational Data Language)
- 관계대수 (Đại số quan hệ / Relational Algebra: 절차적 언어)
- 관계해석 (Giải tích quan hệ / Relational Calculus: 비절차적 언어)
- 순수 관계 연산자 (Toán tử quan hệ thuần túy: $\sigma, \pi, \bowtie, \div$)
- 일반 집합 연산자 (Toán tử tập hợp: $\cup, \cap, -, \times$)
- 수평 연산 (Phép toán ngang - Select) / 수직 연산 (Phép toán dọc - Project)
- 디그리 (Degree / Bậc) / 카디널리티 (Cardinality / Lượng số)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([12-bai-hoc.md](12-bai-hoc.md), [16-bai-hoc.md](16-bai-hoc.md), [42-bai-hoc.md](42-bai-hoc.md), [51-bai-hoc.md](51-bai-hoc.md)):** Bài học này đóng vai trò đúc kết toàn diện toàn bộ các ký hiệu toán học Hy Lạp và phép toán quan hệ thành một hệ thống lý thuyết hoàn chỉnh trước khi chuyển sang phần chuyển đổi dữ liệu và ETL.
- **Tiếp nối sang các bài sau ([53-bai-hoc.md](53-bai-hoc.md), [54-bai-hoc.md](54-bai-hoc.md)):** Để di chuyển và làm sạch dữ liệu trong quy trình ETL, các thao tác lọc Select, chiếu Project và kết nối Join được hệ thống tự động sinh mã chạy ngầm.

## 읽는 방법 (Cách đọc)
- Học thuộc câu thần chú phân loại:
  - **Select ($\sigma$):** Hàng ngang $\rightarrow$ Lọc Tuple $\rightarrow$ Ký hiệu $\sigma$ (Sigma).
  - **Project ($\pi$):** Cột dọc $\rightarrow$ Chọn Attribute $\rightarrow$ Ký hiệu $\pi$ (Pi).
  - **Join ($\bowtie$):** Ghép bảng $\rightarrow$ Ký hiệu chiếc nơ $\bowtie$.
  - **Division ($\div$):** Chia tập con $\rightarrow$ Ký hiệu phép chia $\div$.
- Nhớ công thức tích Cartesian Product: Bậc cộng lại ($Degree_R + Degree_S$), Lượng số nhân lên ($Cardinality_R \times Cardinality_S$).

---

## 15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 2 nhánh Ngôn ngữ dữ liệu quan hệ:**
  | Nhánh ngôn ngữ | Thuật ngữ Hàn - Anh | Bản chất kỹ thuật | Cách tiếp cận |
  |---|---|---|---|
  | **Đại số quan hệ** | `관계대수` (Relational Algebra) | **Ngôn ngữ mang tính thủ tục (`절차적 언어`)**; cả toán hạng đầu vào và kết quả đầu ra đều là các Quan hệ (Relation). | Chỉ rõ **thực hiện phép toán nào theo trình tự nào** để tìm ra kết quả (How to find). |
  | **Giải tích quan hệ** | `관계해석` (Relational Calculus) | **Ngôn ngữ mang tính phi thủ tục (`비절차적 언어`)**; dựa trên nền tảng giải tích vị từ toán học của E. F. Codd. | Chỉ rõ **cần dữ liệu gì bằng biểu thức vị từ**, không quan tâm trình tự thực thi (What to find). |

- **2. Bảng 4 toán tử quan hệ thuần túy (순수 관계 연산자 4가지):**
  | Toán tử | Ký hiệu Hy Lạp | Chiều thao tác | Ý nghĩa kỹ thuật | Biểu thức ví dụ |
  |---|:---:|---|---|---|
  | **Select (선택)** | **$\sigma$** (Sigma) | **Ngang (`수평 연산`)** | Trích xuất các **bộ (hàng / tuple)** thỏa mãn điều kiện chọn. | $\sigma_{Luong \ge 3000}(NHAN\_VIEN)$ |
  | **Project (추출)** | **$\pi$** (Pi) | **Dọc (`수직 연산`)** | Trích xuất các **thuộc tính (cột / attribute)** được yêu cầu; **tự động loại bỏ trùng lặp**. | $\pi_{MaNV, HoTen}(NHAN\_VIEN)$ |
  | **Join (조인)** | **$\bowtie$** (Bowtie) | Kết hợp bảng | Ghép 2 bảng lại thành 1 bảng mới dựa trên thuộc tính chung (Natural Join $\bowtie_N$ tự động khử cột trùng). | $SINH\_VIEN \bowtie LOP\_HOC$ |
  | **Division (나누기)** | **$\div$** | Chia quan hệ | Lấy các giá trị thuộc tính của quan hệ $R$ xuất hiện kết hợp với **toàn bộ** các giá trị của quan hệ $S$. | $DANG\_KY \div MON\_BAT\_BUOC$ |

- **3. Bảng 4 toán tử tập hợp thông thường (일반 집합 연산자 4가지):**
  - **합집합 (UNION, $\cup$):** Tập hợp tất cả các bộ của cả 2 bảng; tự động loại bỏ trùng lặp.
  - **교집합 (INTERSECTION, $\cap$):** Tập hợp các bộ xuất hiện ở cả hai bảng.
  - **차집합 (DIFFERENCE, $-$):** Tập hợp các bộ có trong $R$ nhưng không có trong $S$.
  - **교차곱 (CARTESIAN PRODUCT, $\times$):** Tập hợp tất cả các cặp có thể giữa bộ của $R$ và bộ của $S$.
    - **Bậc kết quả (Degree):** $Degree(R \times S) = Degree(R) + Degree(S)$
    - **Lượng số kết quả (Cardinality):** $Cardinality(R \times S) = Cardinality(R) \times Cardinality(S)$
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Phép toán nào là phép toán ngang (수평 연산)?"* $\rightarrow$ Đáp án: **Select ($\sigma$)**.
  - Đề hỏi: *"Phép toán nào là phép toán dọc (수직 연산) và tự động loại bỏ trùng lặp?"* $\rightarrow$ Đáp án: **Project ($\pi$)**.
  - Cho bảng R có 3 cột 4 dòng, bảng S có 2 cột 5 dòng. Thực hiện phép tích $R \times S$:
    - Bậc mới = $3 + 2 = \mathbf{5}$.
    - Lượng số mới = $4 \times 5 = \mathbf{20}$.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tương quan giữa Đại số quan hệ và cú pháp SQL:**
  - $\sigma_{Tuoi \ge 20}(SINH\_VIEN) \iff$ `SELECT * FROM SINH_VIEN WHERE Tuoi >= 20;`
  - $\pi_{HoTen, Lop}(SINH\_VIEN) \iff$ `SELECT DISTINCT HoTen, Lop FROM SINH_VIEN;`
  - $R \bowtie_{R.A = S.A} S \iff$ `SELECT * FROM R INNER JOIN S ON R.A = S.A;`
  - Bộ máy SQL Parser của RDBMS biên dịch các câu lệnh SQL khai báo (Declarative) thành cây biểu thức đại số quan hệ (Relational Algebra Tree) để Optimizer tối ưu hóa đường đi.

### 복습 체크리스트
- [ ] Phân biệt được đặc trưng của 관계대수 (thủ tục) và 관계해석 (phi thủ tục).
- [ ] Nhớ chính xác ký hiệu và chiều thao tác: $\sigma$ (Select - ngang), $\pi$ (Project - dọc), $\bowtie$ (Join), $\div$ (Division).
- [ ] Tính thành thạo Degree (+) và Cardinality ($\times$) của phép nhân Cartesian Product.
- [ ] Nắm được cơ chế tự động khử trùng lặp của phép toán Project ($\pi$).
