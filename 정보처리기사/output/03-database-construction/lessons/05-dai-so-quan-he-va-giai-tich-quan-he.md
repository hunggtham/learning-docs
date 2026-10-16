# 관계대수 및 관계해석 (Đại số quan hệ và Giải tích quan hệ)

## 학습 목표 (Mục tiêu)
- Phân biệt sâu sắc giữa Đại số quan hệ (`관계대수` - ngôn ngữ thủ tục, How to retrieve) và Giải tích quan hệ (`관계해석` - ngôn ngữ phi thủ tục, What to retrieve).
- Nắm vững 4 toán tử quan hệ thuần túy: Select ($\sigma$ - chọn hàng, cắt ngang), Project ($\pi$ - chọn cột, cắt dọc, tự triệt tiêu dòng trùng), Join ($\bowtie$ - kết hợp bảng theo điều kiện), Division ($\div$ - phép chia bao hàm).
- Làm chủ 4 toán tử tập hợp thông thường: Hợp ($\cup$), Giao ($\cap$), Hiệu ($-$), và Tích Descartes ($\times$).
- Hiểu rõ điều kiện Khả hợp (`합병 가능 / Union Compatible`: cùng Degree và cùng Domain tương ứng) áp dụng cho $\cup, \cap, -$.
- Nhận diện các bẫy trắc nghiệm về số lượng cột sau phép Natural Join và công thức Degree/Cardinality của phép tích Descartes.

## 핵심 키워드 (Từ khóa)
- 관계대수, 절차적 언어 (Đại số quan hệ, Ngôn ngữ thủ tục / Relational Algebra)
- 관계해석, 비절차적 언어 (Giải tích quan hệ, Ngôn ngữ phi thủ tục / Relational Calculus)
- 순수 관계 연산자 (Toán tử quan hệ thuần túy: Select, Project, Join, Division)
- 일반 집합 연산자 (Toán tử tập hợp: Union, Intersection, Difference, Cartesian Product)
- 합병 가능 (Khả hợp / Union Compatible)
- 자연 조인 (Natural Join / Ghép tự nhiên loại bỏ cột trùng)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Các bảng và khóa ở Bài 03, Bài 04 đóng vai trò là cấu trúc tĩnh (Structure) và luật lệ (Constraints). Để biến dữ liệu thành thông tin hữu ích, ta cần các thao tác (Operation).
- **Đang giải quyết gì (Current Problem):** Phân định ranh giới giữa ngôn ngữ thủ tục (Đại số quan hệ - hướng dẫn cách làm / How) và ngôn ngữ phi thủ tục (Giải tích quan hệ - tuyên bố cái cần lấy / What); đồng thời làm chủ 4 toán tử quan hệ thuần túy ($\sigma, \pi, \bowtie, \div$) và 4 toán tử tập hợp kèm điều kiện khả hợp (Union Compatible).
- **Dùng đi đâu (Forward Handoff):** Nắm vững các phép toán đại số này là điều kiện tiên quyết để hiểu cơ chế phân rã bảng ở [06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md](06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md) nhằm triệt tiêu các dị thường dữ liệu qua các dạng chuẩn 1NF $\rightarrow$ 5NF.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng 4 ký hiệu toán tử thuần túy, điều kiện khả hợp và các bẫy trắc nghiệm hay gài nhất.
- Đọc TẦNG B để hiểu sâu bản chất toán học của phép Natural Join, phép chia Division và đối chiếu TRC/DRC trong giải tích quan hệ.

---

## 관계대수 및 관계해석

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn toán tử quan hệ thuần túy (순수 관계 연산자)

```
            ┌──────────────────────────────────────────────┐
            │          순수 관계 연산자 (4대 연산)         │
            └──────────────────────┬───────────────────────┘
                                   │
      ┌────────────────┬───────────┴───────────┬────────────────┐
      ▼                ▼                       ▼                ▼
 1. Select        2. Project               3. Join          4. Division
  ($\sigma$)       ($\pi$)                 ($\bowtie$)       ($\div$)
  - Chọn HÀNG      - Chọn CỘT              - Gộp BẢNG        - Phép CHIA
  - Cắt ngang      - Cắt dọc               - Ghép theo PK/FK - Lấy giá trị bao hàm
```

| Toán tử thuần túy | Ký hiệu & Cú pháp | Bản chất thao tác | Quy tắc hình học & Lưu ý |
| :--- | :--- | :--- | :--- |
| **Select** (Chọn hàng) | $\sigma_{\text{điều\_kiện}}(R)$ | Chọn ra các dòng (Tuple / 행) thỏa mãn điều kiện logic. | Thao tác **cắt ngang** (수평 연산 / Horizontal). |
| **Project** (Chọn cột) | $\pi_{\text{cột}}(R)$ | Trích xuất các cột (Attribute / 열) mong muốn. | Thao tác **cắt dọc** (수직 연산), **tự triệt tiêu dòng trùng**. |
| **Join** (Kết hợp) | $R \bowtie S$ | Ghép nối 2 bảng dựa trên các thuộc tính chung. | **Natural Join**: Ghép cột trùng tên và chỉ giữ lại 1 cột duy nhất. |
| **Division** (Phép chia) | $R \div S$ | Tìm thuộc tính của $R$ kết hợp với toàn bộ thuộc tính của $S$. | Trả lời câu hỏi chứa từ khóa *"Tất cả (All)"*. |

#### 2. Bốn toán tử tập hợp thông thường (일반 집합 연산자)

```
[Khả hợp (합병 가능 / Union Compatible)] ──> Điều kiện bắt buộc cho: ∪, ∩, -
  1. Cùng số lượng cột (Degree của R = Degree của S)
  2. Các cột tương ứng ở cùng vị trí phải có cùng Domain (kiểu dữ liệu)
```

| Toán tử (연산자) | Ký hiệu | Điều kiện khả hợp | Quy tắc tính Degree và Cardinality |
| :--- | :---: | :---: | :--- |
| **1. 합집합 (Union)** - Hợp | $R \cup S$ | **Bắt buộc** | $\text{Degree} = D_1 = D_2$; $\text{Cardinality} \le C_1 + C_2$ (loại bỏ dòng trùng) |
| **2. 교집합 (Intersection)** - Giao | $R \cap S$ | **Bắt buộc** | $\text{Degree} = D_1 = D_2$; $\text{Cardinality} \le \min(C_1, C_2)$ |
| **3. 차집합 (Difference)** - Hiệu | $R - S$ | **Bắt buộc** | $\text{Degree} = D_1 = D_2$; $\text{Cardinality} \le C_1$ |
| **4. 카티션 프로덕트 (Cartesian Product)** | $R \times S$ | **KHÔNG CẦN** | **$\text{Degree} = D_1 + D_2$** (Cộng); **$\text{Cardinality} = C_1 \times C_2$** (Nhân) |

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정)

- **Bẫy 1: Ngôn ngữ Thủ tục vs Phi thủ tục:**
  - *Câu hỏi:* "Đại số quan hệ (관계대수) là ngôn ngữ thủ tục hay phi thủ tục?"
  - *Đáp án đúng:* **절차적 언어 (Thủ tục)**. Giải tích quan hệ (관계해석) mới là **비절차적 언어 (Phi thủ tục)**.
- **Bẫy 2: Ký hiệu toán tử thuần túy:**
  - **Select (Chọn hàng):** Dùng chữ **$\sigma$ (Sigma)**.
  - **Project (Chọn cột):** Dùng chữ **$\pi$ (Pi)**.
- **Bẫy 3: Điều kiện Khả hợp (합병 가능성 / Union Compatibility):**
  - *Câu hỏi:* "Phép toán nào trong số các phép sau KHÔNG ĐÒI HỎI 2 bảng phải khả hợp?"
  - *Đáp án đúng:* **카티션 프로덕트 (Cartesian Product: $\times$)**. Ba phép $\cup, \cap, -$ bắt buộc phải khả hợp.
- **Bẫy 4: Số cột sau phép Natural Join:**
  - Nếu $R(A, B, C)$ và $S(B, C, D)$ thực hiện Natural Join, số cột kết quả là bao nhiêu?
  - Bảng $R$ và $S$ có 2 cột trùng tên là $B$ và $C$. Khi Natural Join, 2 cột trùng này chỉ được lấy 1 lần.
  - Kết quả có 4 cột: $(A, B, C, D)$, **KHÔNG PHẢI** $3 + 3 = 6$ cột.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Đại số quan hệ vs Giải tích quan hệ (관계대수 vs 관계해석)

```
┌──────────────────────────────────────┐      ┌──────────────────────────────────────┐
│        관계대수 (Relational Algebra)  │      │       관계해석 (Relational Calculus) │
├──────────────────────────────────────┤      ├──────────────────────────────────────┤
│ - 절차적 언어 (Ngôn ngữ THỦ TỤC)     │  vs  │ - 비절차적 언어 (Ngôn ngữ PHI THỦ TỤC)│
│ - "Làm THẾ NÀO để lấy dữ liệu?"      │      │ - "Cần lấy DỮ LIỆU GÌ?" (What)       │
│   (How to retrieve data)             │      │ - E.F. Codd đề xuất dựa trên vị từ   │
│ - Sử dụng các toán tử: σ, π, ⋈, ÷    │      │ - Gồm: Tuple Calculus, Domain Calc   │
└──────────────────────────────────────┘      └──────────────────────────────────────┘
```

| Tiêu chuẩn so sánh (비교 기준) | 관계대수 (Relational Algebra) | 관계해석 (Relational Calculus) |
| :--- | :--- | :--- |
| **Bản chất ngôn ngữ** (언어의 성격) | **절차적 언어 (Ngôn ngữ Thủ tục)**: Chỉ rõ thứ tự các thao tác cần thực hiện. | **비절차적 언어 (Ngôn ngữ Phi thủ tục)**: Chỉ khai báo điều kiện kết quả mong muốn. |
| **Câu hỏi trọng tâm** (핵심 관점) | *"How to retrieve"* (Làm thế nào để lấy ra kết quả). | *"What to retrieve"* (Cái gì cần được lấy ra). |
| **Thành phần biểu diễn** (주요 구성) | Các toán tử quan hệ ($\sigma, \pi, \bowtie, \div$) và toán tử tập hợp ($\cup, \cap, -, \times$). | Vị từ toán học (Predicate Calculus: $\forall$ với mọi, $\exists$ tồn tại). |
| **Phân loại nhánh** (세부 분류) | Thuần túy (Pure) & Tập hợp (General Set). | `튜플 관계해석 (TRC)` & `도메인 관계해석 (DRC)`. |
| **Mức độ hoàn thiện** (관계적 완전성) | **Hoàn thiện quan hệ (Relationally Complete):** Cả hai ngôn ngữ có năng lực biểu đạt tương đương nhau. |

#### 2. Ví dụ thực tế minh họa toán tử thuần túy

1. **Select ($\sigma$):** $\sigma_{\text{Điểm} \ge 80}(\text{SINH\_VIEN})$ $\rightarrow$ Lọc ra các sinh viên có điểm $\ge 80$.
2. **Project ($\pi$):** $\pi_{\text{HọTên, ChuyênNgành}}(\text{SINH\_VIEN})$ $\rightarrow$ Cắt lấy 2 cột Họ tên và Chuyên ngành, loại bỏ trùng.
3. **Natural Join ($\bowtie$):** $\text{SINH\_VIEN} \bowtie \text{DANG\_KY}$ $\rightarrow$ Ghép tự động theo cột chung `MSSV`.
4. **Division ($\div$):** $R \div S$ $\rightarrow$ Trích xuất danh sách sinh viên đăng ký toàn bộ các môn học của $S$.

---

### 복습 체크리스트
- [ ] Phân biệt bản chất: Đại số quan hệ là thủ tục (How), Giải tích quan hệ là phi thủ tục (What).
- [ ] Nhận diện 4 toán tử thuần túy: Select ($\sigma$ - hàng/ngang), Project ($\pi$ - cột/dọc), Join ($\bowtie$ - gộp bảng), Division ($\div$ - chia bao hàm).
- [ ] Nắm vững điều kiện Khả hợp: Cùng Degree và cùng Domain tương ứng (áp dụng cho $\cup, \cap, -$).
- [ ] Thuộc công thức tính kết quả Cartesian Product: $\text{Degree} = D_1 + D_2$, $\text{Cardinality} = C_1 \times C_2$.
- [ ] Nhớ tính chất của Project: Tự động loại bỏ các dòng trùng lặp.
