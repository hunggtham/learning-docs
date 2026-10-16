# 관계대수 및 관계해석 (Đại số quan hệ và Giải tích quan hệ)

## 학습 목표 (Mục tiêu)
- Phân biệt sâu sắc giữa Đại số quan hệ (`관계대수` / Relational Algebra - ngôn ngữ thủ tục, How to retrieve) và Giải tích quan hệ (`관계해석` / Relational Calculus - ngôn ngữ phi thủ tục, What to retrieve).
- Nắm vững và thực hành trực quan 4 toán tử quan hệ thuần túy: Select ($\sigma$ - chọn hàng, cắt ngang), Project ($\pi$ - chọn cột, cắt dọc, tự triệt tiêu dòng trùng), Natural Join ($\bowtie$ - ghép bảng theo cột chung và loại bỏ cột trùng lặp), Division ($\div$ - phép chia bao hàm toàn bộ).
- Làm chủ 4 toán tử tập hợp thông thường: Hợp ($\cup$), Giao ($\cap$), Hiệu ($-$), và Tích Descartes ($\times$).
- Nắm vững điều kiện Khả hợp (`합병 가능` / Union Compatible: cùng số lượng cột Degree và cùng miền giá trị Domain tương ứng) áp dụng cho ba phép $\cup, \cap, -$.
- Hiểu rõ sự biến đổi cấu trúc bảng qua ví dụ bảng ASCII trực quan trước và sau thực thi từng phép toán.

## 핵심 키워드 (Từ khóa)
- 관계대수 (Đại số quan hệ / Relational Algebra / 절차적 언어)
- 관계해석 (Giải tích quan hệ / Relational Calculus / 비절차적 언어)
- 순수 관계 연산자 (Toán tử quan hệ thuần túy: Select, Project, Join, Division)
- 일반 집합 연산자 (Toán tử tập hợp: Union, Intersection, Difference, Cartesian Product)
- 셀렉트, 프로젝트 (Select $\sigma$, Project $\pi$ / 셀-행, 프-열)
- 조인, 디비전 (Join $\bowtie$, Division $\div$)
- 합병 가능 (Khả hợp / Union Compatible)
- 자연 조인 (Ghép tự nhiên / Natural Join)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Các bảng và khóa ở [03-cau-truc-quan-he-schema-tuple-attribute-domain.md](03-cau-truc-quan-he-schema-tuple-attribute-domain.md) và [04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md](04-cac-loai-khoa-va-rang-buoc-toan-ven-du-lieu.md) đóng vai trò là cấu trúc tĩnh (Structure) và luật lệ (Constraints). Để biến dữ liệu thành thông tin hữu ích, ta cần các phép toán (Operation).
- **Đang giải quyết gì (Current Problem):** Phân định ranh giới giữa ngôn ngữ thủ tục (Đại số quan hệ - hướng dẫn cách làm / How) và ngôn ngữ phi thủ tục (Giải tích quan hệ - tuyên bố cái cần lấy / What); giải thích cặn kẽ cơ chế thao tác dữ liệu qua bảng ASCII trước và sau thực thi.
- **Dùng đi đâu (Forward Handoff):** Nắm vững các phép toán đại số này là điều kiện tiên quyết để hiểu cơ chế phân rã bảng không mất mát thông tin (Lossless Join) ở [06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md](06-bat-thuong-du-lieu-phu-thuoc-ham-va-chuan-hoa-1nf-5nf.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng 4 ký hiệu toán tử thuần túy, điều kiện khả hợp, câu thần chú `셀-행, 프-열` và các bẫy trắc nghiệm hay gặp.
- Đọc TẦNG B để theo dõi chi tiết từng ví dụ bảng ASCII trước và sau khi thực thi 4 phép toán quan hệ thuần túy và 4 phép toán tập hợp.

---

## 관계대수 및 관계해석

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn toán tử quan hệ thuần túy (순수 관계 연산자)

```text
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
| **Project** (Chọn cột) | $\pi_{\text{danh\_sách\_cột}}(R)$ | Trích xuất các cột (Attribute / 열) mong muốn. | Thao tác **cắt dọc** (수직 연산), **tự động triệt tiêu dòng trùng**. |
| **Join** (Kết hợp) | $R \bowtie S$ | Ghép nối 2 bảng dựa trên các thuộc tính chung. | **Natural Join**: Ghép cột trùng tên và chỉ giữ lại 1 cột duy nhất. |
| **Division** (Phép chia) | $R \div S$ | Tìm thuộc tính của $R$ kết hợp với toàn bộ thuộc tính của $S$. | Trả lời câu hỏi chứa từ khóa *"Tất cả (All)"*. |

#### 2. Bốn toán tử tập hợp thông thường (일반 집합 연산자)

```text
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

#### 3. Bẫy đề thi và khẩu quyết ghi nhớ (시험 대비 함정 & 암기 팁)

##### Các bẫy trắc nghiệm kinh điển
- **Bẫy 1: Ngôn ngữ Thủ tục vs Phi thủ tục:**
  - *Câu hỏi:* "Đại số quan hệ (관계대수) là ngôn ngữ thủ tục hay phi thủ tục?"
  - *Đáp án đúng:* **절차적 언어 (Thủ tục - Procedural)** vì chỉ rõ các bước thực hiện. Giải tích quan hệ (관계해석) mới là **비절차적 언어 (Phi thủ tục - Non-procedural)**.
- **Bẫy 2: Ký hiệu toán tử thuần túy:**
  - Select (chọn dòng): Dùng **$\sigma$ (Sigma)**.
  - Project (chọn cột): Dùng **$\pi$ (Pi)**.
- **Bẫy 3: Điều kiện Khả hợp (합병 가능성 / Union Compatibility):**
  - *Câu hỏi:* "Phép toán nào trong số các phép sau KHÔNG ĐÒI HỎI 2 bảng phải khả hợp?"
  - *Đáp án đúng:* **카티션 프로덕트 (Cartesian Product: $\times$)**. Ba phép $\cup, \cap, -$ bắt buộc phải khả hợp.
- **Bẫy 4: Số cột sau phép Natural Join:**
  - Bảng $R(A, B, C)$ và $S(B, C, D)$ thực hiện Natural Join ($R \bowtie S$).
  - Thuộc tính chung là $B$ và $C$. Kết quả chỉ giữ 1 lần mỗi thuộc tính chung: $(A, B, C, D) \rightarrow$ **4 cột**, KHÔNG PHẢI $3 + 3 = 6$ cột.

##### Mẹo ghi nhớ thần chú (Mnemonic)
- **Thần chú thuần túy:** `"셀-행, 프-열"`
  - `셀 - 행`: **셀**렉트 ($\sigma$ Select) = **행** (chọn Hàng / Tuple, cắt ngang).
  - `프 - 열`: **프**로젝트 ($\pi$ Project) = **열** (chọn Cột / Attribute, cắt dọc).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Đại số quan hệ vs Giải tích quan hệ (관계대수 vs 관계해석)

| Tiêu chuẩn so sánh (비교 기준) | 관계대수 (Relational Algebra) | 관계해석 (Relational Calculus) |
| :--- | :--- | :--- |
| **Bản chất ngôn ngữ** | **절차적 언어 (Thủ tục)**: Chỉ rõ thứ tự từng thao tác. | **비절차적 언어 (Phi thủ tục)**: Chỉ khai báo điều kiện kết quả. |
| **Câu hỏi trọng tâm** | *"How to retrieve"* (Lấy dữ liệu như thế nào). | *"What to retrieve"* (Cần lấy ra dữ liệu gì). |
| **Công cụ diễn đạt** | Các toán tử quan hệ ($\sigma, \pi, \bowtie, \div, \cup, \cap, -, \times$). | Vị từ logic toán học (Predicate Calculus: $\forall, \exists$). |
| **Phân loại nhánh** | Toán tử thuần túy & Toán tử tập hợp. | `튜플 관계해석 (TRC)` & `도메인 관계해석 (DRC)`. |
| **Năng lực biểu đạt** | **Cả hai tương đương nhau** (Đều đạt chuẩn Relationally Complete). |

#### 2. Minh họa trực quan 4 toán tử quan hệ thuần túy bằng bảng ASCII

##### 2.1. Phép chọn Select ($\sigma$): Cắt ngang theo điều kiện
Xét bảng `SINH_VIEN`:
```text
[Bảng ban đầu: SINH_VIEN]
┌──────────┬──────────┬──────────┬──────────┐
│ MaSV     │ HoTen    │ Khoa     │ DiemTB   │
├──────────┼──────────┼──────────┼──────────┤
│ 202601   │ An       │ CS       │ 8.5      │
│ 202602   │ Binh     │ EE       │ 6.0      │
│ 202603   │ Cuong    │ CS       │ 7.0      │
│ 202604   │ Dung     │ ME       │ 9.0      │
└──────────┴──────────┴──────────┴──────────┘

Thực thi phép toán: σ_(Khoa = 'CS' AND DiemTB >= 8.0)(SINH_VIEN)

[Bảng kết quả sau khi Select]
┌──────────┬──────────┬──────────┬──────────┐
│ MaSV     │ HoTen    │ Khoa     │ DiemTB   │
├──────────┼──────────┼──────────┼──────────┤
│ 202601   │ An       │ CS       │ 8.5      │
└──────────┴──────────┴──────────┴──────────┘
```

##### 2.2. Phép chiếu Project ($\pi$): Cắt dọc và tự động loại trùng
Thực thi phép chiếu chọn cột `Khoa` trên bảng `SINH_VIEN`:
```text
Thực thi phép toán: π_(Khoa)(SINH_VIEN)

[Bảng kết quả sau khi Project - Các giá trị 'CS' trùng lặp tự động bị triệt tiêu]
┌──────────┐
│ Khoa     │
├──────────┤
│ CS       │
│ EE       │
│ ME       │
└──────────┘
```

##### 2.3. Phép kết hợp tự nhiên Natural Join ($\bowtie$): Ghép theo cột chung
Xét hai bảng `NV (NhanVien)` và `PB (PhongBan)` có chung cột `MaPhong`:
```text
[Bảng NV]                     [Bảng PB]
┌──────┬────────┬─────────┐   ┌─────────┬──────────┐
│ MaNV │ TenNV  │ MaPhong │   │ MaPhong │ TenPhong │
├──────┼────────┼─────────┤   ├─────────┼──────────┤
│ E01  │ Kim    │ D10     │   │ D10     │ NhanSu   │
│ E02  │ Lee    │ D20     │   │ D20     │ KyThuat  │
│ E03  │ Park   │ D30     │   │ D40     │ KeToan   │
└──────┴────────┴─────────┘   └─────────┴──────────┘

Thực thi phép toán: NV ⋈ PB

[Bảng kết quả Natural Join - Chỉ giữ 1 cột MaPhong duy nhất]
┌──────┬────────┬─────────┬──────────┐
│ MaNV │ TenNV  │ MaPhong │ TenPhong │
├──────┼────────┼─────────┼──────────┤
│ E01  │ Kim    │ D10     │ NhanSu   │
│ E02  │ Lee    │ D20     │ KyThuat  │
└──────┴────────┴─────────┴──────────┘
```

##### 2.4. Phép chia Division ($\div$): Phép chia bao hàm toàn bộ
Tìm các sinh viên đã đăng ký **tất cả** các môn học có trong bảng $S$:
```text
[Bảng R: DANG_KY]             [Bảng S: MON_BAT_BUOC]
┌──────────┬──────────┐       ┌──────────┐
│ MaSV     │ MaMH     │       │ MaMH     │
├──────────┼──────────┤       ├──────────┤
│ S01      │ C101     │       │ C101     │
│ S01      │ C102     │       │ C102     │
│ S02      │ C101     │       └──────────┘
│ S03      │ C102     │
│ S04      │ C101     │
│ S04      │ C102     │
│ S04      │ C103     │
└──────────┴──────────┘

Thực thi phép toán: R ÷ S

[Bảng kết quả sau Division: Chỉ lấy MaSV học CẢ C101 VÀ C102]
┌──────────┐
│ MaSV     │
├──────────┤
│ S01      │
│ S04      │
└──────────┘
```

#### 3. Minh họa trực quan 4 toán tử tập hợp

Xét hai bảng có điều kiện khả hợp (cùng 1 cột `MaSV`):
- Bảng $A = \{S01, S02, S03\}$
- Bảng $B = \{S02, S03, S04\}$

```text
[Bảng A]        [Bảng B]
┌──────┐        ┌──────┐
│ MaSV │        │ MaSV │
├──────┤        ├──────┤
│ S01  │        │ S02  │
│ S02  │        │ S03  │
│ S03  │        │ S04  │
└──────┘        └──────┘

1. Hợp A ∪ B:        2. Giao A ∩ B:      3. Hiệu A - B:      4. Hiệu B - A:
┌──────┐            ┌──────┐            ┌──────┐            ┌──────┐
│ MaSV │            │ MaSV │            │ MaSV │            │ MaSV │
├──────┤            ├──────┤            ├──────┤            ├──────┤
│ S01  │            │ S02  │            │ S01  │            │ S04  │
│ S02  │            │ S03  │            └──────┘            └──────┘
│ S03  │            └──────┘
│ S04  │
└──────┘
```

##### 4. Phép tích Descartes ($A \times C$)
Xét $A = \{S01, S02\}$ (Degree=1, Card=2) và $C = \{X, Y\}$ (Degree=1, Card=2):
```text
[Bảng kết quả A × C (Degree = 1+1=2, Cardinality = 2×2=4)]
┌────────┬────────┐
│ A.MaSV │ C.Loai │
├────────┼────────┤
│ S01    │ X      │
│ S01    │ Y      │
│ S02    │ X      │
│ S02    │ Y      │
└────────┴────────┘
```

---

### 복습 체크리스트
- [ ] Phân biệt bản chất: Đại số quan hệ là thủ tục (How), Giải tích quan hệ là phi thủ tục (What).
- [ ] Nhận diện 4 toán tử thuần túy: Select ($\sigma$ - hàng/ngang), Project ($\pi$ - cột/dọc), Join ($\bowtie$ - gộp bảng), Division ($\div$ - chia bao hàm).
- [ ] Nhớ thần chú: `"셀-행, 프-열"` (Select = Hàng, Project = Cột).
- [ ] Nắm vững điều kiện Khả hợp: Cùng Degree và cùng Domain tương ứng (bắt buộc với $\cup, \cap, -$, không áp dụng cho $\times$).
- [ ] Thuộc công thức tính kết quả Cartesian Product: $\text{Degree} = D_1 + D_2$, $\text{Cardinality} = C_1 \times C_2$.
- [ ] Hiểu rõ cơ chế tự triệt tiêu dòng trùng lặp trong phép Project ($\pi$).
