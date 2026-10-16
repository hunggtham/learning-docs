# Mô hình dữ liệu hướng hiệu năng và chuẩn hóa

---

## 데이터 모델과 SQL

## Mô hình dữ liệu và SQL

### 1. 성능 데이터 모델링의 개요

### 1. Khái quát về mô hình hóa dữ liệu hướng hiệu năng

**성능 데이터 모델링은 데이터베이스의 성능을 고려하여 데이터 모델을 설계하는 것이다.**

**Mô hình hóa dữ liệu hướng hiệu năng là thiết kế mô hình dữ liệu có xem xét đến hiệu năng của cơ sở dữ liệu.**

Ảnh mô tả việc thiết kế mô hình dữ liệu liên quan đến:

- 정규화 — Normalization — Chuẩn hóa.
- 반정규화 — Denormalization — Phi chuẩn hóa.
- 테이블 통합 및 분할 — Gộp và tách bảng.
- 조인 구조 — Cấu trúc JOIN.
- PK/FK 설정 — Thiết lập PK/FK.
- 인덱스 — Index — Chỉ mục.

#### Thời điểm thực hiện

**성능 데이터 모델링은 분석·설계 단계에서 수행하는 것이 가장 좋다.**

**Mô hình hóa dữ liệu hướng hiệu năng nên được thực hiện ở giai đoạn phân tích và thiết kế.**

Ảnh có biểu đồ:

```
분석/설계 → 구현 → 테스트 → 운영
Phân tích/thiết kế → Triển khai → Kiểm thử → Vận hành
```

**데이터 모델의 문제는 늦게 발견할수록 수정 비용이 증가한다.**

**Càng phát hiện vấn đề của mô hình dữ liệu muộn thì chi phí sửa càng tăng.**

Nếu sửa ở giai đoạn `분석/설계`, chỉ cần sửa mô hình và thiết kế liên quan. Nếu sửa ở giai đoạn `운영`, có thể phải sửa dữ liệu, SQL, chương trình, Index và quy trình vận hành.

---

### 2. 성능 데이터 모델링 진행 순서

### 2. Thứ tự thực hiện mô hình hóa dữ liệu hướng hiệu năng

#### 1) 정규화를 정확하게 수행한다

**정규화를 정확하게 수행하여 데이터 중복과 데이터 이상을 줄인다.**

**Thực hiện chuẩn hóa chính xác để giảm dữ liệu trùng lặp và các lỗi dữ liệu.**

#### 2) DB 용량을 산정한다

**각 엔터티에 어느 정도의 데이터와 트랜잭션이 들어오는지 파악하기 위해 DB 용량을 산정한다.**

**Cần ước tính dung lượng DB để biết mỗi Entity sẽ chứa bao nhiêu dữ liệu và tiếp nhận bao nhiêu giao dịch.**

`용량 산정` có nghĩa là dự đoán:

- Số bản ghi hiện tại.
- Số bản ghi tăng mỗi ngày.
- Dữ liệu sẽ được lưu trong bao lâu.
- Tần suất truy vấn.
- Tần suất cập nhật và xóa.

#### 3) 트랜잭션 유형을 파악한다

**DB에서 발생하는 트랜잭션 유형을 파악하기 위해 CRUD 매트릭스를 활용한다.**

**Sử dụng ma trận CRUD để xác định các loại giao dịch phát sinh trong DB.**

| Ký hiệu | English | Nghĩa |
| --- | --- | --- |
| C | Create | Tạo mới |
| R | Read | Đọc, truy vấn |
| U | Update | Cập nhật |
| D | Delete | Xóa |

Ví dụ, nghiệp vụ `수강신청` có thể:

- Đọc thông tin sinh viên.
- Tạo dữ liệu đăng ký môn học.

#### 4) 반정규화를 수행한다

**용량과 트랜잭션 유형을 분석한 후 필요한 경우 반정규화를 수행한다.**

**Sau khi phân tích dung lượng và loại giao dịch, nếu cần thì thực hiện phi chuẩn hóa.**

Chuẩn hóa làm giảm trùng lặp nhưng có thể làm tăng số bảng và số lần JOIN. Nếu việc đó làm truy vấn chậm, có thể cân nhắc phi chuẩn hóa.

#### 5) 이력 모델과 인덱스를 조정한다

**이력 모델, 인덱스, PK/FK 순서, 슈퍼타입·서브타입 구조를 성능 관점에서 조정한다.**

**Điều chỉnh mô hình lịch sử, Index, thứ tự PK/FK và cấu trúc Supertype/Subtype theo góc nhìn hiệu năng.**

- `이력 모델`: Mô hình lưu lại lịch sử thay đổi.
- `인덱스`: Cấu trúc giúp tìm kiếm nhanh.
- `슈퍼타입`: Entity cha chứa thuộc tính chung.
- `서브타입`: Entity con chứa thuộc tính riêng.

#### 6) 성능을 검증한다

**마지막으로 성능 관점에서 데이터 모델을 검증한다.**

**Cuối cùng phải kiểm tra mô hình dữ liệu từ góc nhìn hiệu năng.**

Cần kiểm tra thời gian chạy SQL, số lần JOIN, dung lượng dữ liệu và hiệu quả của Index.

---

## 3. 정규화

## 3. Chuẩn hóa

### 3.1 정규화의 정의

**정규화는 최소한의 데이터 중복과 최대한의 데이터 유연성 및 일관성을 위해 데이터를 분리하는 과정이다.**

**Chuẩn hóa là quá trình tách dữ liệu để giảm trùng lặp, tăng tính linh hoạt và bảo đảm tính nhất quán.**

Ảnh cho thấy một bảng đang chứa đồng thời:

- Thông tin môn học.
- Thông tin đăng ký môn học.
- Thông tin sinh viên.

Ví dụ:

| 과목코드 | 과목명 | 학번 | 이름 | 연락처 |
| --- | --- | --- | --- | --- |
| C01 | DB개론 | 2401 | 강감찬 | 010-1234-5678 |
| C02 | DB실무 | 2401 | 강감찬 | 010-1234-5678 |
| A01 | 마이닝 | 2402 | 홍길동 | 010-6363-8282 |
| B01 | 통계 | 2401 | 강감찬 | 010-1234-5678 |
| C01 | DB개론 | 2403 | 이춘향 | 010-9876-5432 |

Tên và số điện thoại của sinh viên `2401` bị lặp lại ở nhiều dòng.

---

### 3.2 데이터 이상

#### 삭제 이상

**삭제 이상은 원하는 정보만 삭제하려고 했는데 다른 정보까지 삭제되는 현상이다.**

**Lỗi xóa là hiện tượng muốn xóa một thông tin nhưng thông tin khác cũng bị xóa theo.**

Nếu sinh viên `2402` xóa đăng ký môn `A01`, và không còn sinh viên nào học `A01`, thông tin môn học `A01` cũng có thể bị mất.

#### 삽입 이상

**삽입 이상은 관련된 다른 정보가 없어서 원하는 정보를 입력할 수 없는 현상이다.**

**Lỗi chèn là hiện tượng không thể thêm thông tin mong muốn vì thông tin liên quan khác chưa tồn tại.**

Nếu sinh viên mới `2404` chưa học môn nào, bảng cũ có thể không cho phép thêm riêng thông tin sinh viên vì khóa cần cả thông tin môn học và đăng ký học.

#### 갱신 이상

**갱신 이상은 하나의 정보를 변경하기 위해 여러 행을 수정해야 하는 현상이다.**

**Lỗi cập nhật là hiện tượng phải sửa nhiều dòng để thay đổi một thông tin.**

Nếu Kang Gam-chan đổi số điện thoại, phải sửa tất cả dòng có tên Kang Gam-chan. Nếu bỏ sót một dòng, dữ liệu sẽ không nhất quán.

---

## 4. 함수적 종속성

## 4. Phụ thuộc hàm

### 4.1 Khái niệm

**함수적 종속성은 한 속성의 값이 다른 속성의 값을 결정하는 관계이다.**

**Phụ thuộc hàm là quan hệ trong đó giá trị của một thuộc tính quyết định giá trị của thuộc tính khác.**

Ký hiệu:

```
X → Y
```

- `X`: 결정자 — Determinant — Thuộc tính quyết định.
- `Y`: 종속자 — Dependent Attribute — Thuộc tính phụ thuộc.

**X의 값 하나에 대응되는 Y의 값은 하나만 존재해야 한다.**

**Một giá trị X phải chỉ tương ứng với một giá trị Y duy nhất.**

Ví dụ:

```
학번 → 학생명
Mã sinh viên → Tên sinh viên
```

Một mã sinh viên chỉ xác định một tên sinh viên.

---

### 4.2 Ví dụ 학번 và 혈액형

**학번이 혈액형을 결정한다고 가정하면 학번 → 혈액형이다.**

**Nếu giả định mã sinh viên quyết định nhóm máu thì có 학번 → 혈액형.**

Ví dụ:

```
2401 → A형
```

**혈액형 → 학번은 성립하지 않는다.**

**혈액형 → 학번 không tồn tại.**

Một nhóm máu có thể thuộc về nhiều sinh viên nên không thể dùng nhóm máu để xác định duy nhất mã sinh viên.

---

## 5. 정규화 절차

## 5. Quy trình chuẩn hóa

Thứ tự trong ảnh:

```
비정규형 → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF
```

Cách nhớ:

```
원 · 부 · 이 · 결 · 다 · 조
```

| Nhớ | Nội dung |
| --- | --- |
| 원 | 원자성 — Tính nguyên tử |
| 부 | 부분 함수 종속 제거 — Loại bỏ phụ thuộc bộ phận |
| 이 | 이행 함수 종속 제거 — Loại bỏ phụ thuộc bắc cầu |
| 결 | 결정자는 후보키 — Determinant phải là Candidate Key |
| 다 | 다치 종속 제거 — Loại bỏ phụ thuộc đa trị |
| 조 | 조인 종속 제거 — Loại bỏ phụ thuộc JOIN |

**이전 정규형을 만족해야 다음 정규형으로 진행할 수 있다.**

**Phải đạt dạng chuẩn trước thì mới có thể tiến hành dạng chuẩn tiếp theo.**

---

## 6. 제1정규형 — 1NF

## 6. Dạng chuẩn 1 — 1NF

**제1정규형은 모든 속성이 원자값을 가져야 한다.**

**1NF yêu cầu mọi thuộc tính phải chứa giá trị nguyên tử.**

Một ô không được chứa nhiều giá trị.

Sai:

| 학번 | 전화번호 |
| --- | --- |
| 2401 | 010-1111-1111, 010-2222-2222 |

Đúng hơn là tách thành nhiều dòng hoặc một bảng riêng.

**1NF는 반복되는 그룹과 여러 값을 한 칸에 저장하는 문제를 제거한다.**

**1NF loại bỏ nhóm lặp và việc lưu nhiều giá trị trong một ô.**

---

## 7. 제2정규형 — 2NF

## 7. Dạng chuẩn 2 — 2NF

**제2정규형은 1NF를 만족하고 부분 함수 종속을 제거한 상태이다.**

**2NF là trạng thái đạt 1NF và loại bỏ phụ thuộc hàm bộ phận.**

Bảng trong ảnh:

```
학번(PK), 과목코드(PK), 평점, 과목명, 학생명, 소속학과코드, 학과명
```

Khóa chính ghép:

```
(학번, 과목코드)
```

Các phụ thuộc:

```
(학번, 과목코드) → 평점
학번 → 학생명
과목코드 → 과목명
```

`평점` phụ thuộc vào toàn bộ khóa ghép.

`학생명` chỉ phụ thuộc vào `학번`.

`과목명` chỉ phụ thuộc vào `과목코드`.

**복합 PK의 일부만으로 일반 속성이 결정되면 부분 함수 종속이다.**

**Nếu một thuộc tính thường chỉ bị quyết định bởi một phần của khóa ghép thì đó là phụ thuộc hàm bộ phận.**

Tách thành:

```
과목(과목코드 PK, 과목명)
수강(학번 PK, 과목코드 PK, 평점)
학생(학번 PK, 학생명, 소속학과코드, 학과명)
```

---

## 8. 제3정규형 — 3NF

## 8. Dạng chuẩn 3 — 3NF

**제3정규형은 2NF를 만족하고 이행 함수 종속을 제거한 상태이다.**

**3NF là trạng thái đạt 2NF và loại bỏ phụ thuộc hàm bắc cầu.**

Ảnh biểu diễn:

```
학번 → 소속학과코드
소속학과코드 → 학과명
따라서 학번 → 학과명
```

`학번` không trực tiếp quyết định `학과명`; nó quyết định `소속학과코드`, rồi `소속학과코드` quyết định `학과명`.

**일반 속성이 다른 일반 속성을 결정하면 이행 함수 종속이다.**

**Nếu một thuộc tính thường quyết định một thuộc tính thường khác thì đó là phụ thuộc hàm bắc cầu.**

Tách thành:

```
학생(학번 PK, 학생명, 소속학과코드 FK)
학과(소속학과코드 PK, 학과명)
```

---

## 9. 정규화의 성능

## 9. Hiệu năng của chuẩn hóa

**정규화는 데이터 중복을 줄이고 저장 용량을 줄일 수 있다.**

**Chuẩn hóa có thể giảm dữ liệu trùng lặp và dung lượng lưu trữ.**

**정규화는 데이터 입력·수정·삭제 시 변경 범위를 줄여 성능을 향상시킬 수 있다.**

**Chuẩn hóa có thể cải thiện hiệu năng bằng cách giảm phạm vi thay đổi khi thêm, sửa và xóa dữ liệu.**

Tuy nhiên:

**조회에서는 여러 테이블을 JOIN해야 하므로 성능이 저하될 수 있다.**

**Khi truy vấn, hiệu năng có thể giảm vì phải JOIN nhiều bảng.**

Ảnh đưa ra ví dụ:

- Trước chuẩn hóa: một bảng, khoảng 1천만 건.
- Sau chuẩn hóa: bảng học sinh khoảng 4천 건, bảng đăng ký khoảng 1천만 건.

Khi đổi năm học của một sinh viên:

- Trước chuẩn hóa: phải sửa nhiều dòng đăng ký.
- Sau chuẩn hóa: chỉ sửa một dòng trong bảng sinh viên.

Khi truy vấn `학번, 학생명, 과목명, 평점`:

- Trước chuẩn hóa: truy vấn trong một bảng.
- Sau chuẩn hóa: cần JOIN, có thể giảm hiệu năng một phần.

---

## 10. BCNF

## 10. Dạng chuẩn BCNF

**BCNF는 3NF의 강화 버전이며 모든 결정자가 후보키여야 한다.**

**BCNF là phiên bản mạnh hơn của 3NF và yêu cầu mọi Determinant phải là Candidate Key.**

Cách nhớ:

```
BCNF = 결정자는 반드시 후보키
BCNF = Determinant bắt buộc phải là Candidate Key
```

Ảnh có bảng:

```
학생번호(PK), 과목명(PK), 지도교수
```

Giả định:

```
(학생번호, 과목명) → 지도교수
지도교수 → 과목명
```

`지도교수` quyết định `과목명`, nhưng `지도교수` không phải Candidate Key trong bảng ban đầu.

**후보키가 아닌 속성이 다른 속성을 결정하면 BCNF를 만족하지 못할 수 있다.**

**Nếu một thuộc tính không phải Candidate Key quyết định thuộc tính khác thì bảng có thể không đạt BCNF.**

Tách thành:

```
학생-지도교수(학생번호, 지도교수)
지도교수-과목(지도교수, 과목명)
```

---

## 11. 제4정규형 — 4NF

## 11. Dạng chuẩn 4 — 4NF

**제4정규형은 BCNF를 만족하면서 다치 종속을 제거한 상태이다.**

**4NF là trạng thái đạt BCNF và loại bỏ phụ thuộc đa trị.**

Ảnh có bảng:

```
학생번호(PK), 과목명(PK), 취미
```

Một sinh viên có:

- Nhiều môn học.
- Nhiều sở thích.
- Môn học và sở thích độc lập với nhau.

Ví dụ:

| 학생번호 | 과목명 | 취미 |
| --- | --- | --- |
| 2401 | DB개론 | 그림 |
| 2401 | DB개론 | 게임 |
| 2401 | DB실무 | 그림 |
| 2401 | DB실무 | 게임 |

**학생번호에 대해 과목명과 취미가 서로 독립적으로 여러 개 존재하면 다치 종속이다.**

**Nếu với một mã sinh viên có nhiều môn học và nhiều sở thích độc lập với nhau thì đó là phụ thuộc đa trị.**

Ký hiệu:

```
학생번호 →→ 과목명
학생번호 →→ 취미
```

Tách thành:

```
학생-과목(학생번호, 과목명)
학생-취미(학생번호, 취미)
```

---

## 12. 제5정규형 — 5NF

## 12. Dạng chuẩn 5 — 5NF

**제5정규형은 4NF를 만족하고 조인 종속을 제거한 상태이다.**

**5NF là trạng thái đạt 4NF và loại bỏ phụ thuộc JOIN.**

**5NF는 Project Join Normal Form 또는 PJ/NF라고 한다.**

**5NF còn được gọi là Project Join Normal Form hoặc PJ/NF.**

Ảnh mô tả:

```
A를 B와 C로 분해
B와 C를 JOIN
다시 A가 됨
```

Nghĩa là:

```
A tách thành B và C
B JOIN với C
Khôi phục lại A
```

**분해한 테이블을 다시 JOIN했을 때 원래 관계가 정확하게 복원되어야 한다.**

**Khi JOIN lại các bảng đã tách, quan hệ ban đầu phải được khôi phục chính xác.**

5NF hiếm khi được áp dụng trong thiết kế DB thông thường.

---

## 13. 반정규화 — Phi chuẩn hóa (Denormalization)

### 13.1. Bản chất và Nguyên tắc áp dụng
**반정규화는 정규화된 데이터 모델에서 시스템의 성능 향상, 개발 및 운영의 단순화를 위해 의도적으로 중복, 통합, 분리를 수행하는 모델링 기법이다.**

Phi chuẩn hóa là kỹ thuật mô hình hóa có chủ đích chấp nhận trùng lặp dữ liệu, gộp hoặc tách bảng trên mô hình đã chuẩn hóa nhằm cải thiện hiệu năng truy vấn và đơn giản hóa việc phát triển, vận hành hệ thống.

- **Khác biệt quan trọng trong đề thi:**
  - `정규화 (Normalization)`: Giảm thiểu trùng lặp, triệt tiêu bất thường (Anomaly) khi INSERT/UPDATE/DELETE.
  - `반정규화 (Denormalization)`: Chấp nhận đánh đổi hiệu năng ghi để tăng tốc độ đọc (SELECT), giảm chi phí JOIN nhiều bảng.
  - `비정규화 (Unnormalized)`: Mô hình thô ban đầu chưa từng được chuẩn hóa (khác hoàn toàn với 반정규화).

- **Quy trình 3 bước trước khi quyết định Phi chuẩn hóa:**
  1. **정규화 수행 (Chuẩn hóa chuẩn mực):** Luôn hoàn thành chuẩn hóa mô hình dữ liệu trước tiên.
  2. **대체 방안 검토 (Khảo sát các giải pháp thay thế):** Khi phát sinh vấn đề hiệu năng, trước hết phải xem xét: tạo thêm chỉ mục (Index), tạo khung nhìn (View), gom cụm dữ liệu (Clustering), hoặc tối ưu lại câu lệnh SQL.
  3. **반정규화 적용 (Chỉ áp dụng khi cần thiết):** Nếu các giải pháp kỹ thuật trên không giải quyết được bài toán hiệu năng thì mới tiến hành phi chuẩn hóa.

---

### 13.2. Ba nhóm kỹ thuật Phi chuẩn hóa chính

#### 1) Phi chuẩn hóa Bảng (테이블 반정규화)
- **테이블 병합 (Gộp bảng):**
  - **Gộp bảng 1:1 (1:1 관계 병합):** Hai bảng có quan hệ 1:1 thường xuyên được truy vấn cùng nhau thì gộp làm một bảng duy nhất để triệt tiêu chi phí JOIN.
  - **Gộp bảng 1:N (1:N 관계 병합):** Gộp bảng con vào bảng cha; nhược điểm lớn là làm lặp lại nhiều lần dữ liệu của bảng cha, tốn dung lượng lưu trữ.
  - **Gộp mô hình Super/Sub-type (슈퍼·서브타입 병합):**
    - *Single Table (One Table / Roll-up):* Gộp toàn bộ Super-type và Sub-types vào 1 bảng duy nhất; truy vấn nhanh nhất nhưng nhiều ô nhận giá trị NULL.
    - *All Table per Sub-type:* Chỉ tạo các bảng Sub-type riêng biệt, chứa luôn thuộc tính của Super-type.
    - *One Table per Type:* Giữ nguyên mỗi Sub-type một bảng và 1 bảng Super-type độc lập (kết nối qua PK/FK).
- **테이블 분할 (Tách bảng):**
  - **수직 분할 (Tách dọc / Vertical Split):** Tách một bảng có quá nhiều cột thành 2 bảng có cùng khóa chính PK. Đưa các cột có dung lượng lớn (TEXT, BLOB) hoặc các cột ít khi truy xuất sang bảng phụ để giảm kích thước bản ghi, tăng số bản ghi nạp được vào một khối I/O bộ nhớ đệm (Buffer Cache).
  - **수평 분할 (Tách ngang / Horizontal Split):** Tách bảng thành nhiều bảng con có cấu trúc cột giống hệt nhau dựa trên điều kiện giá trị (ví dụ: tách theo năm `ORDER_2025`, `ORDER_2026`).
- **테이블 추가 (Thêm bảng bổ trợ):**
  - **집계 테이블 추가 (Thêm bảng tổng hợp):** Tạo bảng lưu sẵn các kết quả tổng hợp tính toán (`총매출`, `월별통계`) để tránh phải tính lại `SUM/AVG` trên hàng chục triệu dòng.
  - **진행/이력 테이블 추가 (Thêm bảng tiến trình / lịch sử):** Lưu riêng trạng thái hiện tại hoặc vết lịch sử giao dịch để phục vụ tra cứu nhanh.

#### 2) Phi chuẩn hóa Cột (컬럼 반정규화)
- **중복 컬럼 추가 (Thêm cột trùng lặp):** Sao chép trực tiếp một cột thường xuyên dùng từ bảng này sang bảng khác (ví dụ: sao chép `부서명` sang bảng `사원`) để câu lệnh `SELECT` không cần phải thực hiện phép `JOIN`.
- **파생 컬럼 추가 (Thêm cột phái sinh):** Lưu trực tiếp giá trị đã tính toán sẵn vào cột mới (ví dụ: cột `결제총액` trong bảng Đơn hàng = Đơn giá $\times$ Số lượng) thay vì tính toán động khi truy vấn.
- **PK에 의한 컬럼 추가 (Thêm cột theo PK):** Khi PK là khóa phức hợp gồm nhiều cột, thêm cột đại diện để tạo điều kiện tìm kiếm đơn giản hơn.

#### 3) Phi chuẩn hóa Quan hệ (관계 반정규화)
- **중복 관계 추가 (Thêm quan hệ trùng lặp):** Khi để truy vấn từ bảng A sang bảng C phải đi qua bảng B ($A \rightarrow B \rightarrow C$), ta tạo thêm một quan hệ trực tiếp từ $A \rightarrow C$ (thêm khóa ngoại FK trực tiếp từ C vào A) để giảm độ sâu của phép JOIN từ 2 lần xuống còn 1 lần.

---

## 14. 테이블 파티셔닝 — Phân vùng bảng (Table Partitioning)

### 14.1. Bản chất và Kỹ thuật Partition Pruning
- **Khái niệm:** Phân vùng bảng là kỹ thuật chia một bảng logic lớn có dung lượng hàng chục đến hàng trăm Gigabyte thành nhiều phân vùng vật lý độc lập (Physical Partitions) được lưu trữ trên các tablespace khác nhau.
- **Tính trong suốt phân vùng (Partition Transparency):** Người dùng và lập trình viên vẫn nhìn bảng như một bảng logic duy nhất; câu lệnh SQL không cần thay đổi tên bảng.
- **Partition Pruning (Tối ưu hóa loại trừ phân vùng):** Khi câu lệnh SQL có mệnh đề `WHERE` chứa điều kiện khớp với khóa phân vùng (Partition Key), bộ tối ưu hóa của DBMS sẽ **chỉ quét riêng phân vùng chứa dữ liệu cần tìm và bỏ qua hoàn toàn các phân vùng còn lại**, giúp giảm thiểu tối đa số khối đĩa I/O phải đọc.

### 14.2. Bốn phương pháp phân vùng bảng trong SQLD

| Phương pháp phân vùng | Tên tiếng Hàn & Anh | Cơ chế phân chia dữ liệu | Trường hợp áp dụng điển hình |
| :--- | :--- | :--- | :--- |
| **Phân vùng theo dải** | **Range Partitioning (범위 분할)** | Phân chia dữ liệu dựa trên **khoảng giá trị liên tục** của khóa phân vùng (ví dụ: `< 2025-01-01`, `< 2026-01-01`). | Phổ biến nhất trong thực tế; dữ liệu có tính chất chuỗi thời gian như ngày đặt hàng, ngày phát sinh giao dịch. |
| **Phân vùng theo danh sách** | **List Partitioning (목록 분할)** | Phân chia dữ liệu dựa trên **danh sách các giá trị rời rạc xác định** (ví dụ: `AREA_CODE IN ('02', '031')`). | Khi cột phân vùng có số lượng giá trị phân loại hữu hạn, không liên tục như mã khu vực, quốc gia, loại tiền tệ. |
| **Phân vùng theo băm** | **Hash Partitioning (해시 분할)** | DBMS áp dụng một hàm băm nội bộ lên khóa phân vùng để **phân tán ngẫu nhiên và đồng đều** dữ liệu vào các phân vùng. | Khi dữ liệu không có dải ngày tháng rõ ràng; giúp triệt tiêu hiện tượng thắt cổ chai điểm nóng I/O (Hotspot). |
| **Phân vùng kết hợp** | **Composite Partitioning (복합 분할)** | Kết hợp hai tầng phân vùng: Tầng 1 chia theo **Range Partitioning**, mỗi phân vùng con ở Tầng 2 lại chia tiếp theo **List hoặc Hash**. | Bảng giao dịch khổng lồ: Tầng 1 chia theo Năm/Tháng, Tầng 2 chia theo Mã vùng hoặc băm mã khách hàng. |

---

## 15. Hiệu năng của Chuẩn hóa: Tác động hai chiều đối với truy vấn SELECT

Một trong những sai lầm phổ biến nhất của người học SQLD là mặc định rằng: *"Chuẩn hóa luôn luôn làm suy giảm tốc độ của câu lệnh truy vấn SELECT do phải thực hiện nhiều phép JOIN"*.

Thực tế theo giáo trình K-Data SQLD, **Chuẩn hóa tác động hai chiều lên hiệu năng truy vấn SELECT**:

```
                       HIỆU NĂNG CỦA CHUẨN HÓA (정규화의 성능)
                                  │
         ┌────────────────────────┴────────────────────────┐
         ↓                                                 ↓
Ghi dữ liệu (DML)                                Đọc dữ liệu (SELECT)
- INSERT / UPDATE / DELETE nhanh hơn              - Hai mặt tùy thuộc vào điều kiện truy vấn:
- Triệt tiêu dữ liệu trùng lặp                   + GIẢM HIỆU NĂNG: Khi cần JOIN nhiều bảng
- Triệt tiêu bất thường Anomaly                  + TĂNG HIỆU NĂNG: Khi truy vấn trên bảng hẹp
```

### 15.1. Trường hợp Chuẩn hóa làm GIẢM hiệu năng SELECT
- Khi một báo cáo nghiệp vụ đòi hỏi hiển thị đồng thời thông tin của nhiều thực thể (ví dụ: Mã sinh viên, Tên sinh viên, Tên môn học, Điểm số, Tên khoa, Tên giảng viên).
- Trước khi chuẩn hóa: Mọi dữ liệu nằm chung trong 1 bảng rộng duy nhất $\rightarrow$ Truy vấn trực tiếp không cần JOIN.
- Sau khi chuẩn hóa: Bảng bị phân tách thành `SINH_VIEN`, `MON_HOC`, `DANG_KY`, `KHOA`, `GIANG_VIEN` $\rightarrow$ Câu lệnh SELECT buộc phải thực hiện 4-5 phép JOIN liên tiếp, tiêu tốn tài nguyên CPU và bộ nhớ đệm.

### 15.2. Trường hợp Chuẩn hóa làm TĂNG hiệu năng SELECT (Bẫy thi cốt lõi!)
Xét tình huống nghiệp vụ: Hệ thống trường đại học cần tra cứu danh sách *"Sinh viên năm thứ 3"*.

- **Trước khi chuẩn hóa (Bảng gộp chung `DANG_KY_HOC`):**
  - Giả sử trường có 10,000 sinh viên, mỗi sinh viên đăng ký trung bình 50 môn học trong toàn khóa $\rightarrow$ Bảng gộp chứa tới **500,000 bản ghi**.
  - Khi chạy câu lệnh `SELECT DISTINCT HOC_VIEN_ID, HO_TEN FROM DANG_KY_HOC WHERE NAM_HOC = 3;`, DBMS buộc phải thực hiện Full Table Scan quét qua toàn bộ 500,000 dòng dữ liệu kèm chi phí lọc `DISTINCT` trên bộ nhớ.
- **Sau khi chuẩn hóa (Tách thành `SINH_VIEN` và `KET_QUA_HOC`):**
  - Bảng `SINH_VIEN` chỉ lưu trữ đúng thông tin cá nhân của 10,000 sinh viên (dung lượng nhỏ gọn, kích thước bản ghi hẹp).
  - Câu lệnh `SELECT HOC_VIEN_ID, HO_TEN FROM SINH_VIEN WHERE NAM_HOC = 3;` **chỉ quét qua bảng 10,000 dòng**, nạp được nhiều bản ghi hơn vào mỗi khối đĩa I/O (Buffer Block), tốc độ thực thi nhanh hơn gấp hàng chục lần mà không cần thao tác lọc trùng lặp!

---

## 16. Cạm bẫy thi cử trọng điểm (출제 함정 & 오답 노트)

### Cạm bẫy 1: Khẳng định "Chuẩn hóa chỉ làm giảm hiệu năng của câu lệnh SELECT"
- **Bẫy đề thi:** Đề bài đưa ra nhận định: *"Chuẩn hóa dữ liệu chỉ mang lại lợi ích cho các thao tác INSERT, UPDATE, DELETE và luôn làm giảm tốc độ của tất cả các câu lệnh SELECT"*.
- **Cách phá bẫy:** SAI. Như đã phân tích ở mục 15, khi câu lệnh SELECT có điều kiện lọc trên một tập con thuộc tính đã được tách thành bảng độc lập, kích thước bảng nhỏ hơn rất nhiều so với bảng gộp ban đầu, giúp giảm số khối I/O đọc từ đĩa và tăng tốc độ truy vấn đáng kể.

### Cạm bẫy 2: Đánh đồng "Phi chuẩn hóa (반정규화)" với "Chưa chuẩn hóa (비정규화)"
- **Bẫy đề thi:** Coi việc không áp dụng chuẩn hóa ngay từ đầu và phi chuẩn hóa là cùng một bản chất.
- **Cách phá bẫy:**
  - **비정규화 (Unnormalized / Chưa chuẩn hóa):** Mô hình dữ liệu thô ban đầu, chưa từng được xử lý để triệt tiêu các phụ thuộc hàm và trùng lặp.
  - **반정규화 (Denormalization / Phi chuẩn hóa):** Là kỹ thuật có chủ đích điều chỉnh một mô hình đã hoàn thành chuẩn hóa một cách bài bản, nhằm đánh đổi một phần tính toàn vẹn dữ liệu để tối ưu tốc độ đọc và giảm tải số lần JOIN khi hệ thống chịu tải nặng.

### Cạm bẫy 3: Nhảy cóc thực hiện Phi chuẩn hóa ngay khi gặp nghẽn hiệu năng
- **Bẫy đề thi:** Câu hỏi tình huống: *"Khi hệ thống gặp vấn đề chậm trễ do truy vấn JOIN nhiều bảng, hành động đầu tiên cần làm là gộp bảng hoặc thêm cột trùng lặp"*.
- **Cách phá bẫy:** SAI. Quy trình chuẩn giải quyết bài toán hiệu năng theo giáo trình K-Data:
  1. Tối ưu lại câu lệnh SQL (SQL Tuning).
  2. Tạo hoặc cấu trúc lại chỉ mục Index (Index Tuning).
  3. Cân nhắc gom cụm dữ liệu (Clustering) hoặc sử dụng View / Materialized View.
  4. Chỉ khi tất cả các giải pháp kỹ thuật trên không đáp ứng được SLA hiệu năng thì mới tiến hành Phi chuẩn hóa (반정규화).

### Cạm bẫy 4: Nhầm lẫn điều kiện xảy ra vi phạm 2NF và 3NF
- **Bẫy đề thi:** Đưa ra một bảng có Khóa chính đơn (Single Column Primary Key) và hỏi xem bảng đó có thể vi phạm Dạng chuẩn 2 (2NF) hay không.
- **Cách phá bẫy:**
  - Vi phạm 2NF là vi phạm **Phụ thuộc hàm bộ phận (부분함수종속)**, tức là một thuộc tính thường chỉ phụ thuộc vào một phần của khóa chính.
  - Điều này **CHỈ CÓ THỂ XẢY RA KHI KHÓA CHÍNH LÀ KHÓA PHỨC HỢP (Composite PK gồm từ 2 cột trở lên)**!
  - Nếu một bảng có Khóa chính gồm 1 cột duy nhất, bảng đó **tự động thỏa mãn Dạng chuẩn 2 (2NF)** và chỉ cần kiểm tra xem có vi phạm 3NF (phụ thuộc bắc cầu) hay không.

### Cạm bẫy 5: Nhận diện chuẩn BCNF (Boyce-Codd Normal Form)
- **Bẫy đề thi:** Khẳng định một bảng đã đạt 3NF thì chắc chắn đã đạt BCNF.
- **Cách phá bẫy:** SAI. BCNF là phiên bản thắt chặt của 3NF. BCNF đòi hỏi **mọi thuộc tính quyết định (Determinant - vế trái của phụ thuộc hàm $X \rightarrow Y$) đều phải là Khóa ứng viên (Candidate Key)**. Nếu một thuộc tính thường hoặc một phần của khóa phụ lại đóng vai trò quyết định một thuộc tính khác nằm trong khóa chính thì bảng đó đạt 3NF nhưng vi phạm BCNF.

---

## 17. Câu hỏi trắc nghiệm thi thử mô phỏng (실전 기출 변형 문제 & 정답 해설)

### Câu 1 (Ba dị thường dữ liệu do chưa chuẩn hóa)
**Đề bài:** Bảng `COURSE_ENROLLMENT (과목코드, 과목명, 학번, 학생명, 연락처)` có Khóa chính phức hợp là `(과목코드, 학번)`. Nhận định nào sau đây là **ĐÚNG** khi phân tích các hiện tượng dị thường dữ liệu (데이터 이상) của bảng trên?

A. Khi xóa thông tin đăng ký môn học của một sinh viên duy nhất học môn đó, toàn bộ thông tin về tên môn học cũng bị xóa mất — Đây là Dị thường cập nhật (갱신 이상).
B. Muốn thêm một sinh viên mới vừa nhập học vào cơ sở dữ liệu nhưng sinh viên đó chưa đăng ký môn học nào thì không thể thêm được do `과목코드` thuộc Khóa chính không thể nhận giá trị NULL — Đây là Dị thường chèn (삽입 이상).
C. Khi sinh viên thay đổi số điện thoại, việc chỉ cập nhật ở một số dòng mà bỏ sót các dòng khác dẫn đến mâu thuẫn dữ liệu — Đây là Dị thường xóa (삭제 이상).
D. Quá trình chuẩn hóa dữ liệu chỉ nhằm mục đích tiết kiệm tối đa dung lượng ổ cứng chứ không có tác dụng loại bỏ các hiện tượng dị thường trên.

**Đáp án đúng:** **B**

**Giải thích chi tiết:**
- **Phương án B đúng:** Đây là định nghĩa chuẩn xác về Dị thường chèn (`삽입 이상` - Insertion Anomaly). Vì khóa chính là `(과목코드, 학번)` nên theo quy tắc toàn vẹn thực thể (Entity Integrity), không một cột nào trong PK được phép nhận NULL. Do đó, một sinh viên mới chưa học môn nào sẽ không thể được lưu trữ độc lập vào bảng này.
- **Phương án A sai:** Hiện tượng vô tình làm mất thông tin môn học khi xóa bản ghi đăng ký là Dị thường xóa (`삭제 이상` - Deletion Anomaly), không phải 갱신 이상.
- **Phương án C sai:** Hiện tượng mâu thuẫn dữ liệu khi sửa đổi không đồng bộ là Dị thường cập nhật (`갱신 이상` - Update Anomaly), không phải 삭제 이상.
- **Phương án D sai:** Mục tiêu cốt lõi của chuẩn hóa là triệt tiêu dị thường (Anomalies) và đảm bảo tính nhất quán dữ liệu, tiết kiệm bộ nhớ chỉ là hệ quả phụ.

---

### Câu 2 (Quy trình xác định các dạng chuẩn 1NF $\sim$ BCNF)
**Đề bài:** Cho bảng `STUDENT_ACADEMIC (학번, 과목코드, 성적, 지도교수, 지도교수연구실)` với các phụ thuộc hàm sau:
1. `(학번, 과목코드) → 성적`
2. `학번 → 지도교수`
3. `지도교수 → 지도교수연구실`

Biết rằng Khóa chính của bảng là `(학번, 과목코드)`. Bảng trên đang dừng lại ở dạng chuẩn nào và vi phạm dạng chuẩn nào tiếp theo?

A. Thỏa mãn 1NF, vi phạm 2NF
B. Thỏa mãn 2NF, vi phạm 3NF
C. Thỏa mãn 3NF, vi phạm BCNF
D. Đã đạt dạng chuẩn BCNF

**Đáp án đúng:** **A**

**Giải thích chi tiết:**
- **Phương án A đúng:**
  - Bảng đã có các giá trị nguyên tử đơn nhất nên thỏa mãn 1NF.
  - Tuy nhiên, Khóa chính là `(학번, 과목코드)`, mà thuộc tính `지도교수` chỉ phụ thuộc vào một phần của khóa chính là `학번` (Phụ thuộc hàm: `학번 → 지도교수`).
  - Đây chính là hiện tượng **Phụ thuộc hàm bộ phận (부분함수종속)**. Do đó, bảng vi phạm Dạng chuẩn 2 (2NF). Để đạt 2NF, ta phải tách thuộc tính `지도교수` ra khỏi bảng này.

---

### Câu 3 (Mối quan hệ giữa Chuẩn hóa và Hiệu năng truy vấn)
**Đề bài:** Xét các phát biểu sau đây về mối tương quan giữa Chuẩn hóa dữ liệu (정규화) và Hiệu năng hệ thống (성능), phát biểu nào sau đây là **CHÍNH XÁC NHẤT**?

A. Chuẩn hóa dữ liệu luôn luôn làm giảm tốc độ thực thi của mọi câu lệnh SQL trong cơ sở dữ liệu do phát sinh chi phí phân rã bảng.
B. Chuẩn hóa giúp tăng tốc độ của các thao tác INSERT, UPDATE, DELETE nhưng chắc chắn làm chậm toàn bộ các câu lệnh SELECT trong mọi hoàn cảnh.
C. Chuẩn hóa có thể giúp câu lệnh SELECT thực thi nhanh hơn trong trường hợp truy vấn lọc dữ liệu trên một bảng con có kích thước nhỏ gọn sau khi đã được phân tách.
D. Chuẩn hóa dữ liệu chỉ mang ý nghĩa lý thuyết trong thiết kế học thuật và không cần áp dụng trong các hệ thống cơ sở dữ liệu doanh nghiệp lớn.

**Đáp án đúng:** **C**

**Giải thích chi tiết:**
- **Phương án C đúng:** Đây là phát biểu chuẩn xác theo giáo trình K-Data SQLD. Sau khi chuẩn hóa, bảng dữ liệu lớn ban đầu được tách thành các bảng chuyên biệt nhỏ hơn. Khi người dùng thực hiện câu lệnh SELECT với điều kiện lọc trên một thực thể cụ thể, DBMS chỉ cần quét trên bảng con nhỏ gọn đó thay vì quét toàn bộ bảng khổng lồ chưa chuẩn hóa, giúp giảm số khối I/O đĩa và tăng tốc độ xử lý rõ rệt.
- **Phương án A và B sai:** Vì khẳng định mang tính tuyệt đối ("luôn luôn làm giảm", "chắc chắn làm chậm trong mọi hoàn cảnh").
- **Phương án D sai:** Chuẩn hóa là nền tảng sống còn của mô hình hóa dữ liệu quan hệ chuyên nghiệp.

---

### Câu 4 (Chiến lược Phi chuẩn hóa & Thứ tự ưu tiên xử lý)
**Đề bài:** Khi một hệ thống cơ sở dữ liệu gặp vấn đề suy giảm hiệu năng do phải thực hiện nhiều phép JOIN phức tạp giữa các bảng đã chuẩn hóa, quy trình xử lý nào sau đây là **ĐÚNG ĐẮN NHẤT** trước khi quyết định thực hiện Phi chuẩn hóa (반정규화)?

A. Lập tức hợp nhất toàn bộ các bảng con vào bảng cha để giảm thiểu số lượng bảng trong hệ thống.
B. Chuyển đổi toàn bộ quan hệ xác định (식별자 관계) thành quan hệ không xác định (비식별자 관계).
C. Tiến hành rà soát tối ưu hóa câu lệnh SQL, bổ sung chỉ mục Index hoặc cân nhắc sử dụng View trước khi quyết định sửa đổi cấu trúc bảng bằng phi chuẩn hóa.
D. Xóa bỏ toàn bộ các ràng buộc khóa ngoại (Foreign Key) và khóa chính (Primary Key) để tăng tốc độ ghi dữ liệu.

**Đáp án đúng:** **C**

**Giải thích chi tiết:**
- **Phương án C đúng:** Theo quy tắc chuẩn hóa hiệu năng của K-Data: Phi chuẩn hóa là giải pháp kỹ thuật can thiệp vào cấu trúc bảng và chấp nhận đánh đổi tính toàn vẹn dữ liệu. Vì vậy, trước khi thực hiện phi chuẩn hóa, nhà thiết kế bắt buộc phải rà soát các giải pháp thay thế ít rủi ro hơn: Tối ưu lại câu lệnh SQL, bổ sung chỉ mục Index thích hợp, hoặc ứng dụng Clustering / Materialized View.
- **Phương án A sai:** Hợp nhất vội vã làm gia tăng dữ liệu trùng lặp và gây lỗi dị thường.
- **Phương án B và D sai:** Xóa bỏ khóa hoặc đổi quan hệ tùy tiện phá hủy tính toàn vẹn dữ liệu và không phải là giải pháp chuẩn tắc.

---

## 18. KẾT LUẬN GHI NHỚ CUỐI BÀI

### 1. Chuỗi khẩu quyết Chuẩn hóa kinh điển
```
도 → 부 → 이 → 결 → 다 → 조
(Do → Bu → I → Gyeol → Da → Jo)
```
- **도 (Domain / 1NF):** Tất cả các thuộc tính phải mang giá trị nguyên tử đơn nhất (원자값).
- **부 (Partial / 2NF):** Loại bỏ phụ thuộc hàm bộ phận (부분 함수 종속 제거); toàn bộ thuộc tính không khóa phải phụ thuộc vào toàn bộ PK.
- **이 (Transitive / 3NF):** Loại bỏ phụ thuộc hàm bắc cầu (이행 함수 종속 제거); $X \rightarrow Y$ và $Y \rightarrow Z$ thì tách $Z$ thành bảng riêng.
- **결 (Determinant / BCNF):** Mọi thuộc tính quyết định (Determinant) đều phải là Khóa ứng viên (후보키).
- **다 (Multivalued / 4NF):** Loại bỏ phụ thuộc đa trị (다치 종속 제거).
- **조 (Join / 5NF):** Loại bỏ phụ thuộc kết nối JOIN (조인 종속 제거).

### 2. Bảng so sánh Chuẩn hóa vs Phi chuẩn hóa

| Tiêu chí | Chuẩn hóa (정규화) | Phi chuẩn hóa (반정규화) |
| :--- | :--- | :--- |
| **Mục tiêu chính** | Loại bỏ trùng lặp, triệt tiêu bất thường (Anomaly), bảo đảm tính toàn vẹn. | Tăng tốc độ truy vấn đọc (SELECT), giảm số lần JOIN khi chịu tải lớn. |
| **Hiệu năng SELECT** | Tăng tốc khi quét bảng hẹp; giảm tốc khi phải JOIN qua quá nhiều bảng. | Tăng tốc rõ rệt do dữ liệu đã được gộp hoặc tính sẵn giá trị. |
| **Hiệu năng DML (Ghi)** | Nhanh và nhất quán do mỗi dữ liệu chỉ lưu một nơi duy nhất. | Chậm hơn do phải cập nhật đồng thời nhiều cột/bảng trùng lặp. |
| **Thời điểm thực hiện** | Bắt buộc thực hiện ở giai đoạn thiết kế logic (논리적 모델링). | Chỉ thực hiện có chọn lọc sau khi các giải pháp SQL/Index không đáp ứng. |

---

## 19. Nối mạch sang Bài 04: Quan hệ, Transaction, NULL và Identifier

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 03 đã hoàn thiện bức tranh tối ưu hóa mô hình dữ liệu: từ các bước chuẩn hóa triệt tiêu bất thường (1NF $\sim$ 5NF), phân tích hiệu năng hai chiều đến kỹ thuật phi chuẩn hóa có kiểm soát và phân vùng bảng Partitioning.
> - **Đang giải quyết gì:** Trong quá trình vận hành cơ sở dữ liệu thực tế, các thao tác nghiệp vụ được nhóm thành các đơn vị giao dịch (Transaction) như thế nào? Giá trị NULL được đối xử ra sao trong các phép toán SQL và cách lựa chọn giữa Khóa tự nhiên (Natural Key) vs Khóa nhân tạo (Surrogate Key)?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 04 — Quan hệ, Transaction, NULL và Identifier](./04-quan-he-transaction-null-va-identifier.md) để nắm vững 4 đặc tính ACID của Transaction, bản chất 3 giá trị logic của NULL trong các hàm tổng hợp và chiến lược thiết kế bản chất định danh.
