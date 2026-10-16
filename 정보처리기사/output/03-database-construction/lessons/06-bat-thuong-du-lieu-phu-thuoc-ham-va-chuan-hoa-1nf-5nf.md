# 이상 현상, 함수적 종속성 및 정규화 (Bất thường dữ liệu, Phụ thuộc hàm và Chuẩn hóa 1NF đến 5NF)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 hiện tượng dị thường dữ liệu (`이상 현상`): Dị thường thêm (`삽입 이상`), Dị thường xóa (`삭제 이상`), Dị thường sửa (`갱신 이상`).
- Phân biệt sâu sắc 3 loại phụ thuộc hàm cốt lõi: Phụ thuộc hàm hoàn toàn (FFD), Phụ thuộc hàm một phần (PFD), và Phụ thuộc hàm bắc cầu (TFD).
- Thuộc nằm lòng thần chú 6 bước chuẩn hóa dữ liệu: **"도 - 부 - 이 - 결 - 다 - 조"** (1NF $\rightarrow$ 2NF $\rightarrow$ 3NF $\rightarrow$ BCNF $\rightarrow$ 4NF $\rightarrow$ 5NF).
- Làm chủ định nghĩa và điều kiện thỏa mãn của từng dạng chuẩn: 1NF (giá trị nguyên tử), 2NF (loại bỏ PFD), 3NF (loại bỏ TFD), BCNF (mọi Determinant là Candidate Key), 4NF (loại bỏ đa trị), 5NF (phụ thuộc kết nối).
- Nhận diện các bẫy trắc nghiệm về thứ tự chuyển đổi dạng chuẩn và giai đoạn thực hiện chuẩn hóa.

## 핵심 키워드 (Từ khóa)
- 이상 현상 (Hiện tượng dị thường: 삽입, 삭제, 갱신 이상)
- 함수적 종속성 (Phụ thuộc hàm / Functional Dependency: X -> Y)
- 완전/부분/이행적 함수 종속 (FFD, PFD, TFD)
- 정규화 (Chuẩn hóa / Normalization / 무손실 분해)
- 도·부·이·결·다·조 (Khẩu quyết 6 bước chuẩn hóa)
- 1NF, 2NF, 3NF, BCNF, 4NF, 5NF

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Khi thiết kế bảng sơ khai ở Bài 02, việc gộp nhiều thuộc tính vào cùng một bảng lớn thường gây ra dư thừa dữ liệu (Redundancy) và khiến dữ liệu bị mâu thuẫn khi thao tác.
- **Đang giải quyết gì (Current Problem):** Phân tích 3 hiện tượng dị thường (`삽입·삭제·갱신 이상`), làm rõ cơ chế Phụ thuộc hàm đầy đủ vs một phần vs bắc cầu; sau đó thực hiện 6 bước chuẩn hóa từ 1NF đến 5NF để tách bảng an toàn (không mất mát thông tin - Lossless Join Decomposition).
- **Dùng đi đâu (Forward Handoff):** Chuẩn hóa cao giúp dữ liệu sạch nhưng lại làm chậm tốc độ truy vấn do phải `JOIN` quá nhiều bảng. [07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md](07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md) sẽ giải quyết bài toán cân bằng ngược lại: **Phi chuẩn hóa (반정규화)** và tối ưu hóa hiệu năng truy vấn.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng thần chú "도 - 부 - 이 - 결 - 다 - 조", bảng đối chiếu 6 dạng chuẩn và các bẫy trắc nghiệm hỏi nhanh dạng chuẩn.
- Đọc TẦNG B để hiểu sâu bản chất 3 hiện tượng dị thường, cơ chế phân rã không mất mát thông tin và cách vẽ chuỗi phụ thuộc hàm.

---

## 이상 현상, 함수적 종속성 및 정규화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Thần chú ghi nhớ chuỗi chuẩn hóa 6 bước: "도 - 부 - 이 - 결 - 다 - 조"

Mục đích của chuẩn hóa: **Tối thiểu hóa dư thừa dữ liệu, triệt tiêu 3 dị thường, phân rã bảng bảo toàn thông tin (무손실 분해 / Lossless Decomposition)**.

$$\text{비정규형} \xrightarrow{\text{도}} \text{1NF} \xrightarrow{\text{부}} \text{2NF} \xrightarrow{\text{이}} \text{3NF} \xrightarrow{\text{결}} \text{BCNF} \xrightarrow{\text{다}} \text{4NF} \xrightarrow{\text{조}} \text{5NF}$$

```
  도: 도메인이 원자값              ──> Đạt chuẩn 1NF (Miền giá trị nguyên tử)
  부: 부분 함수 종속 제거          ──> Đạt chuẩn 2NF (Loại bỏ phụ thuộc một phần, đạt FFD)
  이: 이행적 함수 종속 제거        ──> Đạt chuẩn 3NF (Loại bỏ phụ thuộc bắc cầu X->Y->Z)
  결: 결정자이면서 후보키 아닌 것 제거 ──> Đạt chuẩn BCNF (Mọi Determinant phải là Candidate Key)
  다: 다치 종속 제거              ──> Đạt chuẩn 4NF (Loại bỏ phụ thuộc đa trị)
  조: 조인 종속성 이용            ──> Đạt chuẩn 5NF (Áp dụng phụ thuộc phép kết nối)
```

#### 2. Bảng đối chiếu chi tiết các cấp độ dạng chuẩn

| Dạng chuẩn (정규형) | Điều kiện tiên quyết & Hành động cốt lõi (조건 및 작업) | Dị thường / Vấn đề được giải quyết |
| :--- | :--- | :--- |
| **제1정규형 (1NF)** | `테이블의 모든 속성 값이 원자값(Atomic Value)만으로 구성` | Loại bỏ các thuộc tính lặp, thuộc tính đa trị (Multivalued). |
| **제2정규형 (2NF)** | 1NF thỏa mãn + **`부분 함수 종속 제거`** (Đạt 완전 함수 종속 FFD) | Tách các thuộc tính chỉ phụ thuộc vào một phần của khóa chính phức hợp sang bảng riêng. |
| **제3정규형 (3NF)** | 2NF thỏa mãn + **`이행적 함수 종속 제거`** (Không còn $X \rightarrow Y \rightarrow Z$) | Tách các thuộc tính phụ thuộc gián tiếp qua thuộc tính không khóa sang bảng riêng. |
| **BCNF (Boyce-Codd)**| 3NF thỏa mãn + **`모든 결정자가 후보키(Candidate Key)`** | Loại bỏ trường hợp một thuộc tính khóa phụ thuộc vào một thuộc tính không phải là khóa ứng viên. |
| **제4정규형 (4NF)** | BCNF thỏa mãn + **`다치 종속(Multivalued Dependency) 제거`** | Loại bỏ việc 1 giá trị của $X$ độc lập xác định nhiều giá trị của $Y$ và $Z$. |
| **제5정규형 (5NF)** | 4NF thỏa mãn + **`조인 종속(Join Dependency) 이용`** (PJ/NF) | Phân rã bảng thành các bảng nhỏ hơn mà khi ghép lại không sinh ra dữ liệu giả (Spurious Tuples). |

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정)

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

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Ba hiện tượng dị thường dữ liệu (이상 현상 / Anomalies)

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

| Hiện tượng dị thường | Mệnh đề thi gốc (원문) | Bản chất kỹ thuật & Tình huống thực tế |
| :--- | :--- | :--- |
| **1. 삽입 이상** (Insertion Anomaly) | `원하지 않는 자료가 삽입되거나, 자료가 부족하여 삽입되지 않는 현상` | Bị ép phải nhập dữ liệu không cần thiết, hoặc không thể thêm bản ghi vì chưa có dữ liệu Khóa chính (vi phạm `개체 무결성`). |
| **2. 삭제 이상** (Deletion Anomaly) | `하나의 자료만 삭제하려 했는데, 연쇄적으로 다른 유용한 정보까지 삭제되는 현상` | Khi xóa một thông tin không cần thiết, CSDL vô tình xóa luôn cả những thông tin quan trọng khác nằm cùng dòng mà người dùng muốn giữ lại. |
| **3. 갱신 이상** (Update Anomaly) | `일부 튜플의 정보만 갱신되어 정보에 불일치성(Inconsistency)이 발생하는 현상` | Khi cập nhật dữ liệu lặp lại ở một số dòng mà bỏ sót các dòng còn lại, CSDL rơi vào trạng thái mâu thuẫn dữ liệu. |

#### 2. Phụ thuộc hàm (함수적 종속성 / Functional Dependency: $X \rightarrow Y$)

Nếu với mỗi giá trị của thuộc tính $X$, luôn chỉ xác định được duy nhất một giá trị của thuộc tính $Y$, ta nói rằng: **$Y$ phụ thuộc hàm vào $X$** (ký hiệu: $X \rightarrow Y$).
- **$X$ gọi là:** `결정자 (Determinant / Quyết định tử)` — Vế quyết định.
- **$Y$ gọi là:** `종속자 (Dependent / Phụ thuộc tử)` — Vế bị phụ thuộc.

##### Ba loại phụ thuộc hàm cốt lõi
1. **완전 함수 종속 (Full Functional Dependency - FFD):** $Y$ phụ thuộc vào TOÀN BỘ khóa chính phức hợp. *(Ví dụ: (MSSV, Mã môn) $\rightarrow$ Điểm số)*.
2. **부분 함수 종속 (Partial Functional Dependency - PFD):** $Y$ chỉ phụ thuộc vào MỘT PHẦN của khóa chính phức hợp. *(Ví dụ: (MSSV, Mã môn) $\rightarrow$ Tên sinh viên, chỉ cần MSSV là biết tên)*. $\rightarrow$ Đây là nguyên nhân khiến bảng chưa đạt chuẩn 2NF.
3. **이행적 함수 종속 (Transitive Functional Dependency - TFD):** $X \rightarrow Y$ và $Y \rightarrow Z$ kéo theo $X \rightarrow Z$. *(Ví dụ: MSSV $\rightarrow$ Mã khoa $\rightarrow$ Tên trưởng khoa)*. $\rightarrow$ Đây là nguyên nhân khiến bảng chưa đạt chuẩn 3NF.

---

### 복습 체크리스트
- [ ] Phân biệt 3 loại dị thường: Dị thường thêm (삽입), Dị thường xóa (삭제), Dị thường sửa (갱신).
- [ ] Phân biệt 3 loại phụ thuộc hàm: Hoàn toàn (완전 FFD), Một phần (부분 PFD), Bắc cầu (이행적 TFD).
- [ ] Thuộc lòng thần chú 6 bước: **도 - 부 - 이 - 결 - 다 - 조** (1NF: 원자값 $\rightarrow$ 2NF: 부분 $\rightarrow$ 3NF: 이행 $\rightarrow$ BCNF: 결정자 $\rightarrow$ 4NF: 다치 $\rightarrow$ 5NF: 조인).
- [ ] Nhớ điều kiện BCNF: Mọi quyết định tử phải là khóa ứng viên (후보키).
