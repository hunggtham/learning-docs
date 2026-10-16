# 이상 현상, 함수적 종속성 및 정규화 (Bất thường dữ liệu, Phụ thuộc hàm và Chuẩn hóa 1NF đến 5NF)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 hiện tượng dị thường dữ liệu (`이상 현상` / Anomalies): Dị thường thêm (`삽입 이상` / Insertion Anomaly), Dị thường xóa (`삭제 이상` / Deletion Anomaly), Dị thường sửa (`갱신 이상` / Update Anomaly).
- Phân biệt sâu sắc 3 loại phụ thuộc hàm cốt lõi: Phụ thuộc hàm hoàn toàn (FFD), Phụ thuộc hàm một phần (PFD), và Phụ thuộc hàm bắc cầu (TFD).
- Thuộc nằm lòng câu khẩu quyết 6 bước chuẩn hóa dữ liệu: **"원 - 부 - 이 - 결 - 다 - 조"** (hoặc **"도 - 부 - 이 - 결 - 다 - 조"**): 1NF $\rightarrow$ 2NF $\rightarrow$ 3NF $\rightarrow$ BCNF $\rightarrow$ 4NF $\rightarrow$ 5NF.
- Nắm vững quy trình chuẩn hóa từng bước thông qua ca phân tích thực tế từ hệ thống quản lý đăng ký môn học (`수강 관리 시스템`).
- Làm chủ định nghĩa và điều kiện thỏa mãn của từng dạng chuẩn: 1NF (giá trị nguyên tử), 2NF (loại bỏ PFD), 3NF (loại bỏ TFD), BCNF (mọi Determinant là Candidate Key), 4NF (loại bỏ đa trị MVD), 5NF (loại bỏ phụ thuộc kết nối JD).

## 핵심 키워드 (Từ khóa)
- 이상 현상 (Hiện tượng dị thường / Anomaly: 삽입, 삭제, 갱신 이상)
- 함수적 종속성 (Phụ thuộc hàm / Functional Dependency: X -> Y)
- 결정자, 종속자 (Determinant X, Dependent Y)
- 완전 함수 종속, 부분 함수 종속, 이행적 함수 종속 (FFD, PFD, TFD)
- 정규화 (Chuẩn hóa / Normalization / 무손실 분해 Lossless Decomposition)
- 원·부·이·결·다·조 / 도·부·이·결·다·조 (Khẩu quyết 6 bước chuẩn hóa)
- 1NF, 2NF, 3NF, BCNF, 4NF, 5NF

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Khi thiết kế bảng sơ khai ở [02-mo-hinh-du-lieu-va-bieu-do-erd.md](02-mo-hinh-du-lieu-va-bieu-do-erd.md), việc gộp nhiều thuộc tính vào cùng một bảng lớn thường gây ra dư thừa dữ liệu (Redundancy) và khiến dữ liệu bị mâu thuẫn khi thao tác.
- **Đang giải quyết gì (Current Problem):** Phân tích 3 hiện tượng dị thường (`삽입·삭제·갱신 이상`), làm rõ bản chất Phụ thuộc hàm và thực hiện quy trình chuẩn hóa 6 bước từ 1NF đến 5NF để phân rã bảng thành các bảng nhỏ hơn mà không làm mất mát thông tin (Lossless Join Decomposition).
- **Dùng đi đâu (Forward Handoff):** Chuẩn hóa cao giúp dữ liệu sạch nhưng lại làm giảm tốc độ truy vấn do phải `JOIN` quá nhiều bảng. [07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md](07-phi-chuan-hoa-va-toi-uu-hieu-nang-truy-van.md) sẽ giải quyết bài toán cân bằng ngược lại: **Phi chuẩn hóa (반정규화)** và tối ưu hóa hiệu năng truy vấn.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng câu khẩu quyết "원-부-이-결-다-조", bảng đối chiếu 6 dạng chuẩn và các bẫy trắc nghiệm nhận diện dạng chuẩn.
- Đọc TẦNG B để theo dõi bài toán thực tế xuyên suốt về hệ thống quản lý đăng ký môn học, trực tiếp chứng kiến cách dữ liệu bị dị thường và được chuẩn hóa từng bước từ 1NF đến 5NF.

---

## 이상 현상, 함수적 종속성 및 정규화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khẩu quyết 6 bước chuẩn hóa: "원 - 부 - 이 - 결 - 다 - 조"

Mục đích của chuẩn hóa: **Tối thiểu hóa dư thừa dữ liệu, triệt tiêu 3 dị thường, phân rã bảng bảo toàn thông tin (무손실 분해 / Lossless Decomposition)**.

$$\text{비정규형} \xrightarrow{\text{원/도}} \text{1NF} \xrightarrow{\text{부}} \text{2NF} \xrightarrow{\text{이}} \text{3NF} \xrightarrow{\text{결}} \text{BCNF} \xrightarrow{\text{다}} \text{4NF} \xrightarrow{\text{조}} \text{5NF}$$

```text
  원 (hoặc 도): 원자값 (도메인이 원자값)      ──> Đạt chuẩn 1NF (Mỗi ô một giá trị nguyên tử)
  부: 부분 함수 종속 제거                      ──> Đạt chuẩn 2NF (Loại bỏ phụ thuộc một phần, đạt FFD)
  이: 이행적 함수 종속 제거                    ──> Đạt chuẩn 3NF (Loại bỏ phụ thuộc bắc cầu X -> Y -> Z)
  결: 결정자이면서 후보키 아닌 것 제거 (결정자=후보키) ──> Đạt chuẩn BCNF (Mọi Determinant phải là Candidate Key)
  다: 다치 종속 제거                          ──> Đạt chuẩn 4NF (Loại bỏ phụ thuộc đa trị MVD)
  조: 조인 종속성 이용                        ──> Đạt chuẩn 5NF (Loại bỏ phụ thuộc phép kết nối JD)
```

#### 2. Bảng đối chiếu chi tiết các cấp độ dạng chuẩn

| Dạng chuẩn (정규형) | Điều kiện tiên quyết & Thao tác cốt lõi | Vấn đề được giải quyết | Khẩu quyết |
| :--- | :--- | :--- | :--- |
| **제1정규형 (1NF)** | Mọi giá trị thuộc tính trong bảng đều là **giá trị nguyên tử (원자값 - Atomic Value)**. | Loại bỏ thuộc tính lặp, thuộc tính đa trị. | **원 (도)** |
| **제2정규형 (2NF)** | Thỏa mãn 1NF + **Loại bỏ phụ thuộc hàm một phần (부분 함수 종속 제거)**. Mọi thuộc tính không khóa phải phụ thuộc hoàn toàn vào toàn bộ khóa chính (FFD). | Tách thuộc tính phụ thuộc vào một phần của khóa ghép. | **부** |
| **제3정규형 (3NF)** | Thỏa mãn 2NF + **Loại bỏ phụ thuộc hàm bắc cầu (이행적 함수 종속 제거)**. Không còn tình trạng $X \rightarrow Y \rightarrow Z$. | Tách thuộc tính phụ thuộc gián tiếp qua thuộc tính thường. | **이** |
| **BCNF (Boyce-Codd)**| Thỏa mãn 3NF + **Mọi quyết định tử đều phải là khóa ứng viên (모든 결정자는 후보키)**. | Giải quyết trường hợp thuộc tính khóa phụ thuộc vào thuộc tính không phải candidate key. | **결** |
| **제4정규형 (4NF)** | Thỏa mãn BCNF + **Loại bỏ phụ thuộc đa trị (다치 종속 / Multivalued Dependency 제거)**. | Tách các mối quan hệ đa giá trị độc lập nhau ($X \twoheadrightarrow Y \mid Z$). | **다** |
| **제5정규형 (5NF)** | Thỏa mãn 4NF + **Áp dụng phụ thuộc phép kết nối (조인 종속 / Join Dependency 이용)**. | Phân rã bảng bảo đảm khi join lại không sinh ra bản ghi giả (Spurious Tuples). | **조** |

#### 3. Bẫy đề thi và quy tắc ghi nhớ (시험 대비 함정 & 암기 팁)

##### Các bẫy trắc nghiệm kinh điển
- **Bẫy 1: Khẩu quyết chuyển đổi dạng chuẩn:**
  - *Câu hỏi:* "Để chuyển từ dạng chuẩn 2NF sang 3NF, cần phải loại bỏ yếu tố nào?"
  - *Đáp án đúng:* **이행적 함수 종속성 (Phụ thuộc hàm bắc cầu / Transitive Dependency)**.
  - *Mẹo tra cứu:* `원 (1) -> 부 (2) -> 이 (3) -> 결 (BCNF) -> 다 (4) -> 조 (5)`. Đang ở 2NF muốn lên 3NF thì nhìn chữ `이` (이행적).
- **Bẫy 2: Bản chất của chuẩn BCNF:**
  - *Câu hỏi:* "Dạng chuẩn nào yêu cầu tất cả các Quyết định tử (Determinant / 결정자) đều bắt buộc phải là Khóa ứng viên (Candidate Key / 후보키)?"
  - *Đáp án đúng:* **BCNF (보이스-코드 정규형)**.
- **Bẫy 3: Khi nào bảng tự động đạt chuẩn 2NF:**
  - *Câu hỏi:* "Nếu một bảng đạt chuẩn 1NF và Khóa chính chỉ gồm DUY NHẤT 1 CỘT (Khóa đơn), bảng đó có cần xét 2NF không?"
  - *Đáp án đúng:* **TỰ ĐỘNG ĐẠT 2NF**. Vì khóa chính chỉ có 1 cột nên về mặt toán học không thể tồn tại "phụ thuộc vào một phần của khóa chính".
- **Bẫy 4: Vị trí của Chuẩn hóa trong thiết kế CSDL:**
  - *Đáp án đúng:* **Thiết kế Logic (논리적 설계)**, tuyệt đối không phải Thiết kế Vật lý.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Ba hiện tượng dị thường dữ liệu (이상 현상 / Anomalies)

Xét bảng quản lý đăng ký môn học khi gộp chung mọi thông tin vào một bảng duy nhất:
```text
수강기록(학번, 학생이름, 학과명, 과목코드, 과목명, 교수번호, 교수명, 성적)
PK: (학번, 과목코드)
```

| 학번 (MSSV) | 학생이름 (Tên SV) | 학과명 (Khoa) | 과목명 (Môn) | 교수명 (Giáo sư) | 성적 (Điểm) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1001 | Tham | CS | CSDL | Kim | A |
| 1001 | Tham | CS | Mạng | Lee | B |
| 1002 | Min | CS | CSDL | Kim | A |

Khi lưu chung như trên, 3 hiện tượng dị thường lập tức xuất hiện:
1. **Dị thường cập nhật (갱신 이상 / Update Anomaly):**
   - Giáo sư Kim đổi tên thành Park. Do thông tin giáo sư bị lặp lại ở nhiều dòng sinh viên học môn CSDL, người quản trị phải cập nhật ở tất cả các dòng. Nếu bỏ sót một dòng, cùng một giáo sư dạy cùng môn sẽ có 2 tên khác nhau, làm mất tính nhất quán của CSDL.
2. **Dị thường thêm (삽입 이상 / Insertion Anomaly):**
   - Nhà trường mở một môn học mới `AI (Trí tuệ nhân tạo)` do giáo sư Park phụ trách nhưng chưa có sinh viên nào đăng ký. Vì `학번` là một phần của Khóa chính, bảng không cho phép thêm môn mới này do Khóa chính không được nhận giá trị `NULL` (vi phạm Toàn vẹn thực thể `개체 무결성`).
3. **Dị thường xóa (삭제 이상 / Deletion Anomaly):**
   - Sinh viên 1002 hủy học phần môn CSDL. Nếu ta xóa dòng này và đây là sinh viên cuối cùng học môn đó, toàn bộ dữ liệu về môn học CSDL và Giáo sư Kim sẽ bị xóa mất vĩnh viễn khỏi hệ thống.

#### 2. Quy trình chuẩn hóa từng bước từ 1NF đến 5NF qua ví dụ thực tế

##### Bước 1: 비정규형 $\rightarrow$ 제1정규형 (1NF) — "원자값" (Giá trị nguyên tử)
- **Vấn đề:** Bảng chưa chuẩn hóa có ô chứa danh sách nhiều giá trị:
  - Sinh viên Tham đăng ký: `수강과목 = {CSDL, Java, Mạng}` $\rightarrow$ Vi phạm tính nguyên tử.
- **Giải pháp:** Tách mỗi môn học thành một hàng riêng biệt sao cho mỗi ô chỉ chứa đúng 1 giá trị duy nhất.

##### Bước 2: 1NF $\rightarrow$ 제2정규형 (2NF) — "부분 함수 종속 제거" (Loại bỏ phụ thuộc một phần)
- **Phân tích phụ thuộc hàm với Khóa chính phức hợp `(학번, 과목코드)`:**
  - `(학번, 과목코드) → 성적` (Phụ thuộc hoàn toàn vào cả 2 cột $\rightarrow$ FFD).
  - `학번 → 학생이름, 학과명` (Chỉ cần biết `학번` là biết tên và khoa $\rightarrow$ PFD, phụ thuộc 1 phần).
  - `과목코드 → 과목명, 교수번호` (Chỉ cần biết `과목코드` là biết tên môn $\rightarrow$ PFD, phụ thuộc 1 phần).
- **Giải pháp tách bảng:**
  - `STUDENT(학번, 학생이름, 학과명)`
  - `COURSE(과목코드, 과목명, 교수번호)`
  - `ENROLLMENT(학번, 과목코드, 성적)`

##### Bước 3: 2NF $\rightarrow$ 제3정규형 (3NF) — "이행적 함수 종속 제거" (Loại bỏ phụ thuộc bắc cầu)
- **Phân tích bảng `STUDENT(학번, 학생이름, 학과코드, 학과명)`:**
  - `학번 → 학과코드`
  - `학과코드 → 학과명`
  - Kéo theo `학번 → 학과명` qua chuỗi bắc cầu ($X \rightarrow Y \rightarrow Z$).
- **Giải pháp tách bảng:**
  - `STUDENT(학번, 학생이름, 학과코드)`
  - `DEPARTMENT(학과코드, 학과명)`

##### Bước 4: 3NF $\rightarrow$ BCNF — "결정자는 후보키" (Determinant là Candidate Key)
- **Phân tích bảng `수업(학생, 과목, 교수)`:**
  - Giả thiết: Mỗi giáo sư chỉ dạy đúng 1 môn, nhưng 1 môn có thể do nhiều giáo sư dạy. Một sinh viên có thể học nhiều môn.
  - Phụ thuộc hàm: `(학생, 과목) → 교수`, và `교수 → 과목`.
  - Khóa ứng viên là `(학생, 과목)` và `(학생, 교수)`.
  - Trong phụ thuộc `교수 → 과목`, `교수` là Determinant nhưng **không phải là Candidate Key** (vì 1 giáo sư dạy nhiều sinh viên nên không định danh được dòng).
- **Giải pháp tách bảng:**
  - `교수과목(교수, 과목)` — PK: `교수`
  - `수강(학생, 교수)` — PK: `(학생, 교수)`

##### Bước 5: BCNF $\rightarrow$ 제4정규형 (4NF) — "다치 종속 제거" (Loại bỏ phụ thuộc đa trị)
- **Vấn đề:** Khi 1 sinh viên có nhiều sở thích độc lập (`취미`) và nhiều bằng cấp độc lập (`자격증`). Sự kết hợp tổ hợp giữa sở thích và bằng cấp sinh ra rất nhiều dòng thừa lặp vô nghĩa ($X \twoheadrightarrow Y \mid Z$).
- **Giải pháp:** Tách thành 2 bảng độc lập: `학생_취미(학번, 취미)` và `학생_자격증(학번, 자격증)`.

##### Bước 6: 4NF $\rightarrow$ 제5정규형 (5NF) — "조인 종속 제거" (Loại bỏ phụ thuộc kết nối)
- **Vấn đề:** Bảng có thể phân rã thành 3 bảng nhỏ hơn, nhưng khi thực hiện Natural Join 3 bảng đó lại với nhau thì phải bảo đảm không sinh ra các bộ dữ liệu giả (Spurious Tuples) mà phản ánh chính xác dữ liệu ban đầu.

---

### 복습 체크리스트
- [ ] Phân biệt rõ 3 dị thường dữ liệu: Thêm (`삽입`), Xóa (`삭제`), Sửa (`갱신`).
- [ ] Thuộc nằm lòng khẩu quyết 6 bước chuẩn hóa: **"원 - 부 - 이 - 결 - 다 - 조"** (Nguyên tử $\rightarrow$ Một phần $\rightarrow$ Bắc cầu $\rightarrow$ Quyết định tử là khóa $\rightarrow$ Đa trị $\rightarrow$ Nối).
- [ ] Phân biệt được 3 loại phụ thuộc hàm: Hoàn toàn (FFD), Một phần (PFD), Bắc cầu (TFD).
- [ ] Hiểu rõ vì sao bảng có Khóa chính đơn (1 cột) thì tự động đạt chuẩn 2NF.
- [ ] Nắm vững điều kiện BCNF: Tất cả các Quyết định tử (Determinant) đều phải là Khóa ứng viên (Candidate Key).
