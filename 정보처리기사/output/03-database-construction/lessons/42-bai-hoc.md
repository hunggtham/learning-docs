# 178. 관계해석 (Relational Calculus)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và nguồn gốc lịch sử của Giải tích quan hệ (`관계해석 / Relational Calculus`): Do nhà khoa học E. F. Codd đề xuất dựa trên nền tảng Giải tích vị từ toán học (`술어 해석 / Predicate Calculus`).
- Hiểu sâu đặc trưng cốt lõi của Giải tích quan hệ: Là ngôn ngữ mang tính **phi thủ tục (`비절차적 언어`)**, chỉ mô tả *cần dữ liệu gì (What)* thay vì *làm như thế nào (How)*.
- Khẳng định tính tương đương về năng lực toán học: **Giải tích quan hệ có sức mạnh biểu diễn tương đương hoàn toàn với Đại số quan hệ (`관계대수와 동등함`)**.
- Nhận diện chính xác hai lượng từ logic toán học quan trọng trong đề thi: Lượng từ phổ dụng $\forall$ (`전칭 정량자 / For All`) và Lượng từ tồn tại $\exists$ (`존재 정량자 / There Exists`).

## 핵심 키워드 (Từ khóa)
- 관계해석 (Giải tích quan hệ / Relational Calculus)
- 비절차적 언어 (Ngôn ngữ phi thủ tục / Non-Procedural Language)
- E. F. Codd (E.F. Codd)
- 술어 해석 (Giải tích vị từ / Predicate Calculus)
- 튜플 관계해석 (Giải tích quan hệ bộ / Tuple Relational Calculus)
- 도메인 관계해석 (Giải tích quan hệ miền / Domain Relational Calculus)
- 전칭 정량자 (Lượng từ phổ dụng: $\forall$ / For All)
- 존재 정량자 (Lượng từ tồn tại: $\exists$ / There Exists)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([12-bai-hoc.md](12-bai-hoc.md), [16-bai-hoc.md](16-bai-hoc.md), [41-bai-hoc.md](41-bai-hoc.md)):** Nếu như Đại số quan hệ (Relational Algebra) là ngôn ngữ thủ tục bắt buộc chỉ ra thứ tự thực thi của các toán tử ($\sigma, \pi, \bowtie$), thì Giải tích quan hệ là ngôn ngữ khai báo toán học nền tảng tạo cảm hứng cho sự ra đời của ngôn ngữ SQL hiện đại.
- **Tiếp nối sang bài sau ([43-bai-hoc.md](43-bai-hoc.md)):** Các vị từ trong giải tích quan hệ là công cụ hình thức để chứng minh các định lý về Phụ thuộc hàm (`함수적 종속성`) trong quá trình chuẩn hóa.

## 읽는 방법 (Cách đọc)
- Khắc sâu cặp so sánh kinh điển ở TẦNG A:
  - **관계대수 (Đại số quan hệ):** **절차적 언어 (Thủ tục)** $\rightarrow$ Nêu rõ trình tự các bước thực hiện.
  - **관계해석 (Giải tích quan hệ):** **비절차적 언어 (Phi thủ tục)** $\rightarrow$ Chỉ nêu điều kiện dữ liệu mong muốn.
- Nhớ 2 ký hiệu logic toán học:
  - $\forall$: Đọc là "For All" $\rightarrow$ **전칭 정량자** (cho mọi phần tử).
  - $\exists$: Đọc là "There Exists" $\rightarrow$ **존재 정량자** (tồn tại ít nhất một).

---

## 178. 관계해석 (Relational Calculus)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bản chất kỹ thuật của Giải tích quan hệ (관계해석의 본질):**
  - Được nhà khoa học máy tính E. F. Codd đề xuất dựa trên **Lý thuyết giải tích vị từ toán học (`술어 해석 / Predicate Calculus`)**.
  - **Đặc trưng phi thủ tục (`비절차적 언어`):** Người dùng chỉ cần mô tả biểu thức vị từ để chỉ rõ **thông tin mong muốn là gì (`원하는 정보가 무엇이라는 것만 정의`)**, hoàn toàn không cần mô tả chuỗi thứ tự thao tác để tìm ra thông tin đó.
  - **Tính tương đương năng lực (동등성):** Về mặt chức năng và năng lực xử lý CSDL quan hệ, **Giải tích quan hệ và Đại số quan hệ là tương đương nhau 100%**. Mọi câu truy vấn biểu diễn bằng đại số quan hệ đều có thể chuyển đổi tương đương sang giải tích quan hệ và ngược lại.
- **2. Phân loại 2 nhánh Giải tích quan hệ:**
  - **튜플 관계해석 (Tuple Relational Calculus):** Sử dụng các biến đại diện cho từng hàng (Tuple) trong bảng. Là nền tảng trực tiếp của ngôn ngữ truy vấn SQL.
  - **도메인 관계해석 (Domain Relational Calculus):** Sử dụng các biến đại diện cho từng miền giá trị / thuộc tính (Domain). Là nền tảng của ngôn ngữ QBE (Query-by-Example).
- **3. Bảng các ký hiệu logic toán học trong đề thi:**
  | Ký hiệu | Tên gọi tiếng Hàn | Tên tiếng Anh | Ý nghĩa logic |
  |:---:|---|---|---|
  | **$\forall$** | `전칭 정량자` | Universal Quantifier (For All) | Áp dụng cho **tất cả mọi bộ dữ liệu có thể có** trong quan hệ |
  | **$\exists$** | `존재 정량자` | Existential Quantifier (There Exists) | Chỉ cần **tồn tại ít nhất một bộ dữ liệu** thỏa mãn điều kiện vị từ |
  | **$\wedge$** | `논리곱` | AND | Cả hai điều kiện đều phải đồng thời đúng |
  | **$\vee$** | `논리합` | OR | Ít nhất một trong hai điều kiện đúng |
  | **$\neg$** | `부정` | NOT | Phủ định giá trị logic của điều kiện |

- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Ngôn ngữ truy vấn quan hệ mang đặc trưng phi thủ tục (비절차적 언어) là gì?"* $\rightarrow$ Đáp án: **관계해석 (Relational Calculus)**.
  - Đề hỏi: *"Năng lực xử lý của 관계해석 so với 관계대수 như thế nào?"* $\rightarrow$ Đáp án: **Hoàn toàn tương đương nhau (동등함)**.
  - Đề hỏi: *"Ký hiệu $\forall$ trong giải tích quan hệ là gì?"* $\rightarrow$ Đáp án: **전칭 정량자 (For All)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa biểu thức Giải tích quan hệ bộ:**
  - Biểu thức tìm tên các sinh viên học khoa CNTT:
    $$\{ t.HoTen \mid t \in SINH\_VIEN \wedge t.Khoa = 'CNTT' \}$$
  - Đọc biểu thức: "Tập hợp các giá trị $t.HoTen$ sao cho tồn tại bộ $t$ thuộc bảng $SINH\_VIEN$ và thuộc tính $Khoa$ của bộ $t$ bằng 'CNTT'".
  - Biểu thức này không hề chỉ rõ máy tính phải quét bảng hay duyệt chỉ mục thế nào; DBMS tự biên dịch thành Kế hoạch thực thi tối ưu. Đây chính là gốc rễ của câu lệnh `SELECT HoTen FROM SINH_VIEN WHERE Khoa = 'CNTT'`.

### 복습 체크리스트
- [ ] Phân biệt được 관계대수 (절차적) và 관계해석 (비절차적).
- [ ] Khẳng định được 관계해석 dựa trên 술어 해석 (Predicate Calculus) và có năng lực 동등 với 관계대수.
- [ ] Nhớ tên hai nhánh: 튜플 관계해석 vs 도메인 관계해석.
- [ ] Phân biệt được 전칭 정량자 ($\forall$) và 존재 정량자 ($\exists$).
