# Môn 3 · Bài 05 — Đại số quan hệ và Giải tích quan hệ
# 제3과목: 데이터베이스 구축 — 관계대수(순수 관계 연산자·일반 집합 연산자) 및 관계해석

> **Mạch đọc:** Tiếp nối từ [Bài 04](04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md) về các loại khóa và ràng buộc toàn vẹn, bài học này bước vào thế giới toán học nền tảng làm nên sức mạnh của ngôn ngữ truy vấn SQL: **Đại số quan hệ (관계대수)** và **Giải tích quan hệ (관계해석)**. Đây là chủ đề xuất hiện với tần suất dày đặc trong đề thi trắc nghiệm và câu hỏi tính toán của kỳ thi Kỹ sư Xử lý Thông tin.

> **Mạch kết nối 3 bước (3-part Bridge):**
> - **Từ đâu (Khởi đầu):** Các bảng và khóa ở Bài 03, Bài 04 đóng vai trò là cấu trúc tĩnh (Structure) và luật lệ (Constraints). Để biến dữ liệu thành thông tin hữu ích, ta cần các thao tác (Operation).
> - **Đang giải quyết gì (Bản chất hiện tại):** Phân định ranh giới giữa ngôn ngữ thủ tục (Đại số quan hệ - hướng dẫn *cách làm / How*) và ngôn ngữ phi thủ tục (Giải tích quan hệ - tuyên bố *cái cần lấy / What*); đồng thời làm chủ 4 toán tử quan hệ thuần túy ($\sigma, \pi, \bowtie, \div$) và 4 toán tử tập hợp kèm điều kiện khả hợp (Union Compatible).
> - **Dùng đi đâu (Đích đến tiếp theo):** Nắm vững các phép toán đại số này là điều kiện tiên quyết để hiểu cơ chế phân rã bảng ở [Bài 06](06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md) nhằm triệt tiêu các dị thường dữ liệu qua các dạng chuẩn 1NF $\rightarrow$ 5NF.

---

## 1. Đại số quan hệ vs Giải tích quan hệ (관계대수 vs 관계해석)

Đây là câu hỏi phân loại kinh điển xuất hiện trong hầu hết các kỳ thi:

```
┌──────────────────────────────────────┐      ┌──────────────────────────────────────┐
│        관계대수 (Relational Algebra)  │      │       관계해석 (Relational Calculus) │
├──────────────────────────────────────┤      ├──────────────────────────────────────┤
│ - 절차적 언어 (Ngôn ngữ THỦ TỤC)     │  vs  │ - 비절차적 언어 (Ngôn ngữ PHI THỦ TỤC)│
│ - "Làm THẾ NÀO để lấy dữ liệu?"      │      │ - "Cần lấy DỮ LIỆU GÌ?" (What)       │
│   (How to retrieve data)             │      │ - E.F. Codd đề xuất dựa trên vị từ   │
│ - Sử dụng các toán tử: $\sigma, \pi$ │      │ - Gồm: Tuple Calculus, Domain Calc   │
└──────────────────────────────────────┘      └──────────────────────────────────────┘
```

### 1.1. Bảng so sánh bản chất kỹ thuật

| Tiêu chuẩn so sánh (비교 기준) | 관계대수 (Relational Algebra) | 관계해석 (Relational Calculus) |
| :--- | :--- | :--- |
| **Bản chất ngôn ngữ**<br>(언어의 성격) | **절차적 언어 (Ngôn ngữ Thủ tục)**<br>Chỉ rõ thứ tự các thao tác cần thực hiện. | **비절차적 언어 (Ngôn ngữ Phi thủ tục)**<br>Chỉ khai báo điều kiện kết quả mong muốn. |
| **Câu hỏi trọng tâm**<br>(핵심 관점) | *"How to retrieve"* (Làm thế nào để lấy ra kết quả). | *"What to retrieve"* (Cái gì cần được lấy ra). |
| **Thành phần biểu diễn**<br>(주요 구성) | Các toán tử quan hệ ($\sigma, \pi, \bowtie, \div$) và toán tử tập hợp ($\cup, \cap, -, \times$). | Vị từ toán học (Predicate Calculus: $\forall$ với mọi, $\exists$ tồn tại). |
| **Phân loại nhánh**<br>(세부 분류) | Thuần túy (Pure) & Tập hợp (General Set). | `튜플 관계해석 (TRC)` & `도메인 관계해석 (DRC)`. |
| **Mức độ hoàn thiện**<br>(관계적 완전성) | **Hoàn thiện quan hệ (Relationally Complete):** Cả hai ngôn ngữ có năng lực biểu đạt tương đương nhau. Mọi câu truy vấn viết được bằng Giải tích quan hệ đều chuyển đổi được sang Đại số quan hệ. |

---

## 2. Bốn toán tử quan hệ thuần túy (순수 관계 연산자)

Bốn toán tử này được thiết kế chuyên biệt cho mô hình dữ liệu quan hệ:

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

### 2.1. Chi tiết 4 toán tử quan hệ thuần túy

#### 1. Select ($\sigma$ - Sigma)
- **Ký hiệu & Cú pháp:** $\sigma_{\text{điều\_kiện}}(R)$
- **Bản chất:** Chọn ra các **dòng (Tuple / 행)** thỏa mãn điều kiện logic nhất định.
- **Tính chất hình học:** Là thao tác **cắt ngang (수평 연산 / Horizontal operator)** trên bảng.
- **Ví dụ:** $\sigma_{\text{Điểm} \ge 80}(\text{SINH\_VIEN})$ $\rightarrow$ Trích xuất tất cả sinh viên có điểm từ 80 trở lên.

#### 2. Project ($\pi$ - Pi)
- **Ký hiệu & Cú pháp:** $\pi_{\text{danh\_sách\_cột}}(R)$
- **Bản chất:** Trích xuất ra các **cột (Attribute / 열)** mong muốn từ bảng nguồn.
- **Tính chất hình học:** Là thao tác **cắt dọc (수직 연산 / Vertical operator)** trên bảng.
- **Quy tắc quan trọng:** Phép Project **tự động triệt tiêu các dòng trùng lặp (Duplicate Elimination)** trong kết quả vì một Relation không cho phép các tuple giống hệt nhau.
- **Ví dụ:** $\pi_{\text{HọTên, ChuyênNgành}}(\text{SINH\_VIEN})$ $\rightarrow$ Chỉ lấy ra 2 cột Họ tên và Chuyên ngành.

#### 3. Join ($\bowtie$ - Bowtie)
- **Ký hiệu & Cú pháp:** $R \bowtie_{\text{điều\_kiện\_join}} S$
- **Bản chất:** Kết hợp các tuple của 2 relation $R$ và $S$ lại với nhau dựa trên thuộc tính chung.
- **자연 조인 (Natural Join):** Phép Join tự nhiên là trường hợp đặc biệt và phổ biến nhất, trong đó điều kiện kết hợp là **bằng nhau trên tất cả các cột trùng tên**, và trong bảng kết quả **chỉ giữ lại 1 cột duy nhất** đại diện cho các cột trùng tên đó (loại bỏ cột trùng lặp).
- **Ví dụ:** $\text{SINH\_VIEN} \bowtie \text{DANG\_KY}$ (tự động ghép theo cột chung `MSSV`).

#### 4. Division ($\div$ - Phép chia)
- **Ký hiệu & Cú pháp:** $R \div S$
- **Bản chất:** Tìm tất cả các giá trị thuộc tính của $R$ mà được kết hợp với **TOÀN BỘ** các giá trị thuộc tính có trong $S$.
- **Ứng dụng thực tế:** Trả lời các câu hỏi chứa từ khóa *"tất cả"* (All): *"Tìm những sinh viên đã đăng ký TẤT CẢ các môn học do Giáo sư X giảng dạy"*.

---

## 3. Bốn toán tử tập hợp thông thường (일반 집합 연산자)

Áp dụng lý thuyết tập hợp toán học cho các Relation:

```
[Khả hợp (합병 가능 / Union Compatible)] ──> Điều kiện bắt buộc cho: $\cup, \cap, -$
  1. Cùng số lượng cột (Degree của R = Degree của S)
  2. Các cột tương ứng ở cùng vị trí phải có cùng Domain (kiểu dữ liệu)
```

| Toán tử (연산자) | Ký hiệu | Điều kiện khả hợp | Quy tắc tính Degree và Cardinality |
| :--- | :---: | :---: | :--- |
| **1. 합집합 (Union)**<br>Hợp | $R \cup S$ | **Bắt buộc** | - $\text{Degree} = D_1 = D_2$<br>- $\text{Cardinality} \le C_1 + C_2$ *(do loại trừ dòng trùng)* |
| **2. 교집합 (Intersection)**<br>Giao | $R \cap S$ | **Bắt buộc** | - $\text{Degree} = D_1 = D_2$<br>- $\text{Cardinality} \le \min(C_1, C_2)$ |
| **3. 차집합 (Difference)**<br>Hiệu | $R - S$ | **Bắt buộc** | - $\text{Degree} = D_1 = D_2$<br>- $\text{Cardinality} \le C_1$ |
| **4. 카티션 프로덕트 (Cartesian Product)**<br>Tích Đề-các | $R \times S$ | **KHÔNG CẦN**<br>(Không bắt buộc) | - **$\text{Degree} = D_1 + D_2$** *(Cộng các cột)*<br>- **$\text{Cardinality} = C_1 \times C_2$** *(Nhân các dòng)* |

---

## 4. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

### 4.1. Bẫy đề thi trắc nghiệm (기출 함정)
- **Bẫy 1: Ngôn ngữ Thủ tục vs Phi thủ tục:**
  - *Câu hỏi:* "Đại số quan hệ (관계대수) là ngôn ngữ thủ tục hay phi thủ tục?"
  - *Đáp án đúng:* **절차적 언어 (Thủ tục)**. Giải tích quan hệ (관계해석) mới là **비절차적 언어 (Phi thủ tục)**.
- **Bẫy 2: Ký hiệu toán tử thuần túy:**
  - Thí sinh hay nhầm ký hiệu giữa Select và Project:
    - **Select (Chọn hàng)** $\rightarrow$ Dùng chữ **$\sigma$ (Sigma)**.
    - **Project (Chọn cột)** $\rightarrow$ Dùng chữ **$\pi$ (Pi)**.
- **Bẫy 3: Điều kiện Khả hợp (합병 가능성 / Union Compatibility):**
  - *Câu hỏi:* "Phép toán nào trong số các phép sau KHÔNG ĐÒI HỎI 2 bảng phải khả hợp?"
  - *Đáp án đúng:* **카티션 프로덕트 (Cartesian Product: $\times$)**. Ba phép $\cup, \cap, -$ bắt buộc phải khả hợp.
- **Bẫy 4: Số cột sau phép Natural Join:**
  - Nếu $R(A, B, C)$ và $S(B, C, D)$ thực hiện Natural Join, số cột kết quả là bao nhiêu?
  - Bảng $R$ và $S$ có 2 cột trùng tên là $B$ và $C$. Khi Natural Join, 2 cột trùng này chỉ được lấy 1 lần.
  - Kết quả có 4 cột: $(A, B, C, D)$, **KHÔNG PHẢI** $3 + 3 = 6$ cột.

---

## 5. Checklist ôn thi (복습 체크리스트)

- [ ] Phân biệt bản chất: Đại số quan hệ là thủ tục (How), Giải tích quan hệ là phi thủ tục (What).
- [ ] Nhận diện 4 toán tử thuần túy: Select ($\sigma$ - hàng/ngang), Project ($\pi$ - cột/dọc), Join ($\bowtie$ - gộp bảng), Division ($\div$ - chia bao hàm).
- [ ] Nắm vững điều kiện Khả hợp: Cùng Degree và cùng Domain tương ứng (áp dụng cho $\cup, \cap, -$).
- [ ] Thuộc công thức tính kết quả Cartesian Product: $\text{Degree} = D_1 + D_2$, $\text{Cardinality} = C_1 \times C_2$.
- [ ] Nhớ tính chất của Project: Tự động loại bỏ các dòng trùng lặp.
