# Môn 3 · Bài 06 — Bất thường dữ liệu, Phụ thuộc hàm và Chuẩn hóa 1NF đến 5NF
# 제3과목: 데이터베이스 구축 — 이상 현상, 함수적 종속성 및 정규화(1NF~5NF, BCNF)

> **Mạch đọc:** Tiếp nối từ [Bài 05](05-dai-so-quan-he-va-giai-tich-quan-he.md) về các phép toán đại số quan hệ, bài học này xử lý trọng tâm cốt lõi nhất của giai đoạn Thiết kế logic (`논리적 설계`): **Chuẩn hóa dữ liệu (정규화 / Normalization)**. Đây là kỹ thuật phân rã bảng có hệ thống nhằm triệt tiêu 3 hiện tượng dị thường (Thêm, Xóa, Sửa) và loại bỏ dần các loại phụ thuộc hàm bất lợi theo công thức vàng **"도 - 부 - 이 - 결 - 다 - 조"**.

> **Mạch kết nối 3 bước (3-part Bridge):**
> - **Từ đâu (Khởi đầu):** Khi thiết kế bảng sơ khai ở Bài 02, việc gộp nhiều thuộc tính vào cùng một bảng lớn thường gây ra dư thừa dữ liệu (Redundancy) và khiến dữ liệu bị mâu thuẫn khi thao tác.
> - **Đang giải quyết gì (Bản chất hiện tại):** Phân tích 3 hiện tượng dị thường (`삽입·삭제·갱신 이상`), làm rõ cơ chế Phụ thuộc hàm đầy đủ vs một phần vs bắc cầu; sau đó thực hiện 6 bước chuẩn hóa từ 1NF đến 5NF để tách bảng an toàn (không mất mát thông tin - Lossless Join Decomposition).
> - **Dùng đi đâu (Đích đến tiếp theo):** Chuẩn hóa cao giúp dữ liệu sạch nhưng lại làm chậm tốc độ truy vấn do phải `JOIN` quá nhiều bảng. [Bài 07](07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md) sẽ giải quyết bài toán cân bằng ngược lại: **Phi chuẩn hóa (반정규화)** và tối ưu hóa hiệu năng truy vấn.

---

## 1. Ba hiện tượng dị thường dữ liệu (이상 현상 / Anomalies)

Dị thường (이상 / Anomaly) là hiện tượng dữ liệu bị mâu thuẫn, biến dạng hoặc không thể thao tác bình thường do bảng chứa nhiều mối quan hệ phụ thuộc hàm không hợp lý:

```
                  ┌────────────────────────────────────────┐
                  │          데이터베이스 3대 이상 현상    │
                  │   (3 Hiện tượng Dị thường Dữ liệu)     │
                  └──────────────────┬─────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
  1. 삽입 이상 (Insertion)    2. 삭제 이상 (Deletion)     3. 갱신 이상 (Update)
  - Muốn thêm đối tượng A      - Xóa đối tượng A           - Sửa giá trị ở dòng này
  - Bị ép thêm cả đối tượng B  - Vô tình xóa mất dữ liệu B - Quên sửa ở dòng khác
  - Hoặc thiếu PK không thêm   - Mất mát thông tin quý giá - Dữ liệu không nhất quán
```

### 1.1. Bảng phân tích chi tiết 3 loại dị thường

| Hiện tượng dị thường (이상 현상) | Mệnh đề thi gốc (원문) | Bản chất kỹ thuật & Tình huống thực tế |
| :--- | :--- | :--- |
| **1. 삽입 이상**<br>(Insertion Anomaly / Dị thường thêm) | `원하지 않는 자료가 삽입되거나, 자료가 부족하여 삽입되지 않는 현상` | Khi muốn thêm một bản ghi mới, người dùng bị ép phải nhập thêm những dữ liệu không cần thiết, hoặc không thể thêm bản ghi vì chưa có dữ liệu Khóa chính (vi phạm `개체 무결성`).<br>*(Ví dụ: Chưa thể nhập môn học mới vào hệ thống nếu môn đó chưa có sinh viên nào đăng ký học).* |
| **2. 삭제 이상**<br>(Deletion Anomaly / Dị thường xóa) | `하나의 자료만 삭제하려 했는데, 연쇄적으로 다른 유용한 정보까지 삭제되는 현상` | Khi người dùng thực hiện xóa một thông tin không còn cần thiết, CSDL vô tình xóa luôn cả những thông tin quan trọng khác nằm cùng dòng mà người dùng hoàn toàn muốn giữ lại.<br>*(Ví dụ: Khi sinh viên cuối cùng hủy môn học, toàn bộ thông tin về tên môn học, số tín chỉ và giáo viên phụ trách môn đó bị xóa sạch khỏi CSDL).* |
| **3. 갱신 이상**<br>(Update Anomaly / Dị thường sửa) | `일부 튜플의 정보만 갱신되어 정보에 불일치성(Inconsistency)이 발생하는 현상` | Khi một thông tin lặp lại ở nhiều dòng cần thay đổi, nếu người dùng chỉ cập nhật ở một số dòng mà bỏ sót các dòng còn lại, CSDL sẽ rơi vào trạng thái mâu thuẫn dữ liệu (cùng 1 sinh viên nhưng ở dòng này ghi quê Hà Nội, dòng kia ghi quê Đà Nẵng). |

---

## 2. Phụ thuộc hàm (함수적 종속성 / Functional Dependency: $X \rightarrow Y$)

Nếu với mỗi giá trị của thuộc tính $X$, luôn chỉ xác định được duy nhất một giá trị của thuộc tính $Y$, ta nói rằng: **$Y$ phụ thuộc hàm vào $X$** (ký hiệu: $X \rightarrow Y$).
- **$X$ gọi là:** `결정자 (Determinant / Quyết định tử)` — Vế quyết định.
- **$Y$ gọi là:** `종속자 (Dependent / Phụ thuộc tử)` — Vế bị phụ thuộc.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        3 LOẠI PHỤ THUỘC HÀM CỐT LÕI                    │
├────────────────────────────────────────────────────────────────────────┤
│ 1. 완전 함수 종속 (Full Functional Dependency - FFD):                  │
│    - $Y$ phụ thuộc vào TOÀN BỘ khóa chính phức hợp.                    │
│    - (MSSV, Mã môn) ──> Điểm số (Điểm phải có cả 2 mới xác định).      │
├────────────────────────────────────────────────────────────────────────┤
│ 2. 부분 함수 종속 (Partial Functional Dependency - PFD):                │
│    - $Y$ chỉ phụ thuộc vào MỘT PHẦN của khóa chính phức hợp.           │
│    - (MSSV, Mã môn) ──> Tên sinh viên (Chỉ cần MSSV là biết tên).      │
│    ──> Đây là nguyên nhân gây ra bảng chưa đạt chuẩn 2NF!              │
├────────────────────────────────────────────────────────────────────────┤
│ 3. 이행적 함수 종속 (Transitive Functional Dependency - TFD):           │
│    - $X \rightarrow Y$ và $Y \rightarrow Z$ kéo theo $X \rightarrow Z$  │
│    - MSSV ──> Mã khoa ──> Tên trưởng khoa (Bắc cầu qua Mã khoa).        │
│    ──> Đây là nguyên nhân gây ra bảng chưa đạt chuẩn 3NF!              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Sáu bước chuẩn hóa dữ liệu (정규화 6단계: 1NF $\rightarrow$ 5NF)

Mục đích của chuẩn hóa: **Tối thiểu hóa dư thừa dữ liệu, triệt tiêu 3 dị thường, phân rã bảng bảo toàn thông tin (무손실 분해 / Lossless Decomposition)**.

### 3.1. Thần chú ghi nhớ chuỗi chuẩn hóa: "도 - 부 - 이 - 결 - 다 - 조"

$$\text{비정규형} \xrightarrow{\text{도}} \text{1NF} \xrightarrow{\text{부}} \text{2NF} \xrightarrow{\text{이}} \text{3NF} \xrightarrow{\text{결}} \text{BCNF} \xrightarrow{\text{다}} \text{4NF} \xrightarrow{\text{조}} \text{5NF}$$

```
  도: 도메인이 원자값              ──> Đạt chuẩn 1NF (Miền giá trị nguyên tử)
  부: 부분 함수 종속 제거          ──> Đạt chuẩn 2NF (Loại bỏ phụ thuộc một phần, đạt FFD)
  이: 이행적 함수 종속 제거        ──> Đạt chuẩn 3NF (Loại bỏ phụ thuộc bắc cầu X->Y->Z)
  결: 결정자이면서 후보키 아닌 것 제거 ──> Đạt chuẩn BCNF (Mọi Determinant phải là Candidate Key)
  다: 다치 종속 제거              ──> Đạt chuẩn 4NF (Loại bỏ phụ thuộc đa trị)
  조: 조인 종속성 이용            ──> Đạt chuẩn 5NF (Áp dụng phụ thuộc phép kết nối)
```

### 3.2. Bảng đối chiếu chi tiết các cấp độ dạng chuẩn

| Dạng chuẩn (정규형) | Điều kiện tiên quyết & Hành động cốt lõi (조건 및 작업) | Dị thường / Vấn đề được giải quyết |
| :--- | :--- | :--- |
| **제1정규형 (1NF)** | `테이블의 모든 속성 값이 원자값(Atomic Value)만으로 구성` | Loại bỏ các thuộc tính lặp, thuộc tính đa trị (Multivalued). |
| **제2정규형 (2NF)** | 1NF thỏa mãn + **`부분 함수 종속 제거`** (Đạt 완전 함수 종속 FFD) | Tách các thuộc tính chỉ phụ thuộc vào một phần của khóa chính phức hợp sang bảng riêng. |
| **제3정규형 (3NF)** | 2NF thỏa mãn + **`이행적 함수 종속 제거`** (Không còn $X \rightarrow Y \rightarrow Z$) | Tách các thuộc tính phụ thuộc gián tiếp qua thuộc tính không khóa sang bảng riêng. |
| **BCNF (Boyce-Codd)**| 3NF thỏa mãn + **`모든 결정자가 후보키(Candidate Key)`** | Loại bỏ trường hợp một thuộc tính khóa phụ thuộc vào một thuộc tính không phải là khóa ứng viên. |
| **제4정규형 (4NF)** | BCNF thỏa mãn + **`다치 종속(Multivalued Dependency: $X \twoheadrightarrow Y$) 제거`** | Loại bỏ việc 1 giá trị của $X$ độc lập xác định nhiều giá trị của $Y$ và $Z$. |
| **제5정규형 (5NF)** | 4NF thỏa mãn + **`조인 종속(Join Dependency) 이용`** (PJ/NF) | Phân rã bảng thành các bảng nhỏ hơn mà khi ghép lại không sinh ra dữ liệu giả (Spurious Tuples). |

---

## 4. Bẫy đề thi và bài tập nhận diện (시험 대비 함정 & 실전 포인트)

### 4.1. Bẫy đề thi trắc nghiệm (기출 함정)
- **Bẫy 1: Khẩu quyết thứ tự chuẩn hóa:**
  - *Câu hỏi:* "Để chuyển từ dạng chuẩn 2NF sang 3NF, cần phải loại bỏ yếu tố nào?"
  - *Đáp án đúng:* **이행적 함수 종속성 (Phụ thuộc hàm bắc cầu / Transitive Dependency)**.
  - *Mẹo dò thần chú:* `도 (1) -> 부 (2) -> 이 (3) -> 결 (BCNF) -> 다 (4) -> 조 (5)`. Đang ở 2NF muốn lên 3NF thì nhìn chữ `이` (이행적).
- **Bẫy 2: Định nghĩa chuẩn BCNF:**
  - *Câu hỏi:* "Dạng chuẩn nào yêu cầu tất cả các Quyết định tử (Determinant) đều bắt buộc phải là Khóa ứng viên (Candidate Key)?"
  - *Đáp án đúng:* **BCNF (Boyce-Codd Normal Form)**.
- **Bẫy 3: Giai đoạn thực hiện Chuẩn hóa:**
  - *Câu hỏi:* "Chuẩn hóa dữ liệu được thực hiện ở bước nào trong quy trình thiết kế CSDL?"
  - *Đáp án đúng:* **Thiết kế Logic (논리적 설계)**, không phải Thiết kế Vật lý.

---

## 5. Checklist ôn thi (복습 체크리스트)

- [ ] Phân biệt 3 loại dị thường: Dị thường thêm (삽입), Dị thường xóa (삭제), Dị thường sửa (갱신).
- [ ] Phân biệt 3 loại phụ thuộc hàm: Hoàn toàn (완전 FFD), Một phần (부분 PFD), Bắc cầu (이행적 TFD).
- [ ] Thuộc lòng thần chú 6 bước: **도 - 부 - 이 - 결 - 다 - 조** (1NF: 원자값 $\rightarrow$ 2NF: 부분 $\rightarrow$ 3NF: 이행 $\rightarrow$ BCNF: 결정자 $\rightarrow$ 4NF: 다치 $\rightarrow$ 5NF: 조인).
- [ ] Nhớ điều kiện BCNF: Mọi quyết định tử phải là khóa ứng viên (후보키).
