# 정보처리기사 — 하향식 설계와 데이터베이스 정규화

> **핵심 흐름 / Mạch tư duy cần nhớ**  
> **요구 분석 → 개념적 설계 → 논리적 설계 + 정규화 → 물리적 설계 → 구현**  
> Phân tích yêu cầu → thiết kế khái niệm → thiết kế logic + chuẩn hóa → thiết kế vật lý → triển khai.

---

## 1. 하나의 이야기로 이해하기 / Hiểu bằng một câu chuyện

대학교가 다음 시스템을 원한다고 생각하자.

> “학생이 과목을 신청하고, 학교는 누가 어떤 과목을 수강하는지와 성적을 관리하고 싶다.”

Nếu bắt đầu ngay bằng `CREATE TABLE` thì rất dễ tạo ra một bảng to, lặp dữ liệu và khó sửa. Vì vậy ta dùng tư duy **하향식 설계 (Top-down design, thiết kế từ trên xuống)**: trước hết nhìn mục tiêu lớn của hệ thống, sau đó chia nó thành các phần nhỏ dần; chỉ cuối cùng mới quyết định các cột, khóa và câu SQL.

```text
수강 관리 시스템 (toàn hệ thống)
        ↓
학생 관리 / 과목 관리 / 수강 관리 (các chức năng lớn)
        ↓
학생, 과목, 교수, 수강이라는 데이터 (đối tượng dữ liệu)
        ↓
ERD, 테이블, 키 (mô hình bảng và khóa)
        ↓
정규화 1NF → 2NF → 3NF → BCNF (loại lỗi dữ liệu)
        ↓
인덱스·저장 방식·DDL (tối ưu vật lý và tạo thật)
```

**정규화 (Normalization, chuẩn hóa)** không phải là bước “nghĩ hệ thống cần gì”. Nó là công việc kiểm tra các bảng sau khi đã thiết kế logic, rồi tách chúng hợp lý để một sự thật chỉ được lưu ở một chỗ.

---

## 2. 하향식 설계 / Thiết kế từ trên xuống

### 정의 / Định nghĩa

**하향식 설계**는 전체 시스템을 먼저 파악한 뒤, 큰 기능을 작은 기능으로 단계적으로 분해하는 방법이다.

Đây là phương pháp: hiểu **toàn cảnh trước**, sau đó phân rã chức năng lớn thành chức năng nhỏ, rồi mới đi đến chi tiết. Từ khóa thường gặp: **전체 → 부분**, **추상적 → 구체적**, **상위 → 하위**, **분할·정복 (divide and conquer)**.

Ví dụ:

| Level | Korean | Ví dụ |
|---|---|---|
| 1 | 수강 관리 시스템 | Hệ thống quản lý đăng ký môn |
| 2 | 학생 관리 / 과목 관리 / 수강 관리 | Quản lý sinh viên / môn học / đăng ký |
| 3 | 학생 등록, 과목 조회, 수강 신청, 성적 입력 | Các chức năng nhỏ |
| 4 | 입력값, 처리 절차, 테이블, SQL | Chi tiết thực thi |

### 하향식 설계가 DB 설계에 연결되는 방식

Ban đầu, ta nói về thế giới thực: **학생(Student)**, **과목(Course)**, **교수(Professor)**, **수강(Enrollment)**. Đây là **개념적 설계 (conceptual design)**, thường dùng **ERD**. Chưa cần quan tâm dùng Oracle hay MariaDB.

Sau đó, chuyển thành table, cột, khóa: `STUDENT`, `COURSE`, `PROFESSOR`, `ENROLLMENT`. Đây là **논리적 설계 (logical design)**. Trong chính bước này, ta kiểm tra **정규화**.

Cuối cùng mới cân nhắc cách lưu để chạy nhanh: index, partition, loại dữ liệu, dung lượng… Đây là **물리적 설계 (physical design)**; sau đó dùng DDL như `CREATE TABLE` để **구현 (implementation)**.

> **시험 포인트:** 정규화는 일반적으로 **논리적 설계 단계**에서 수행한다.  
> Điểm thi: chuẩn hóa thường thực hiện ở giai đoạn thiết kế logic.

---

## 3. 왜 정규화가 필요한가? / Vì sao cần chuẩn hóa?

Nếu làm nhanh, ta có thể tạo một bảng duy nhất:

```text
수강기록(학번, 학생이름, 학과코드, 학과명,
        과목코드, 과목명, 교수번호, 교수명, 성적)
```

| 학번 | 학생이름 | 학과명 | 과목명 | 교수명 | 성적 |
|---|---|---|---|---|---|
| 1001 | Tham | 컴퓨터공학과 | DB | Kim | A |
| 1001 | Tham | 컴퓨터공학과 | Java | Lee | B |
| 1002 | Min | 컴퓨터공학과 | DB | Kim | A |

Một sinh viên học nhiều môn, một môn có nhiều sinh viên. Vì thế tên sinh viên, tên môn, tên giáo sư bị lặp lại. Sự lặp này tạo ra **이상(Anomaly, bất thường)**:

| 이상 | Korean meaning | Giải thích |
|---|---|---|
| 갱신 이상 | update anomaly | Giáo sư Kim đổi tên phải sửa mọi dòng DB. Sót một dòng thì cùng một người có hai tên. |
| 삽입 이상 | insertion anomaly | Có môn mới nhưng chưa ai đăng ký: bảng yêu cầu 학번 nên không thêm môn được. |
| 삭제 이상 | deletion anomaly | Xóa sinh viên cuối cùng học DB có thể làm mất luôn thông tin môn DB và giáo sư. |

**정규화의 목적 (mục tiêu chuẩn hóa)**: giảm **중복성 (redundancy, trùng lặp)**, loại **이상 현상**, bảo đảm **데이터 무결성 (data integrity, toàn vẹn dữ liệu)**.

---

## 4. 함수적 종속: 2NF·3NF의 출발점

### 함수적 종속 (Functional Dependency, hàm phụ thuộc)

`A → B`라고 하면, A의 값이 정해지면 B의 값도 하나로 결정된다는 뜻이다.

Nói đơn giản: biết A thì xác định duy nhất được B. A ở bên trái gọi là **결정자 (determinant, yếu tố quyết định)**.

```text
학번 → 학생이름, 학과코드
과목코드 → 과목명, 교수번호
교수번호 → 교수명
(학번, 과목코드) → 성적
```

Ví dụ cuối rất quan trọng: chỉ biết `학번` thì chưa biết điểm môn nào; chỉ biết `과목코드` cũng chưa biết điểm của sinh viên nào. Phải biết cả hai mới có điểm. Vì vậy `(학번, 과목코드)` là **복합키 (composite key, khóa ghép)**.

### 키 용어 / Thuật ngữ khóa

| Korean | English | Nghĩa Việt |
|---|---|---|
| 슈퍼키 | superkey | Tập thuộc tính phân biệt được từng row; có thể chứa cột thừa. |
| 후보키 | candidate key | Superkey tối thiểu, không có cột thừa. |
| 기본키 | primary key | Một candidate key được chọn làm khóa chính. |
| 대체키 | alternate key | Candidate key không được chọn làm PK. |
| 외래키 | foreign key | Cột tham chiếu PK/candidate key của bảng khác. |
| 복합키 | composite key | Key gồm từ hai cột trở lên. |

---

## 5. 1NF부터 BCNF까지 / Từ 1NF đến BCNF

### 5.1 제1정규형 (1NF) — 원자값

**정의:** 모든 속성의 도메인이 원자값(atomic value)만 가져야 한다.

Mỗi ô chỉ giữ **một giá trị không thể chia nhỏ theo yêu cầu dữ liệu**, không phải list hay nhóm lặp.

Sai (chưa 1NF):

| 학번 | 이름 | 수강과목 |
|---|---|---|
| 1001 | Tham | DB, Java, Network |

Đúng 1NF:

| 학번 | 이름 | 과목코드 |
|---|---|---|
| 1001 | Tham | DB |
| 1001 | Tham | Java |
| 1001 | Tham | Network |

> **암기 / Mẹo nhớ:** **1NF = 한 칸에 한 값** (một ô, một giá trị).  
> 1NF chỉ xử lý kiểu dữ liệu trong ô; nó chưa xóa được phụ thuộc hay trùng lặp.

---

### 5.2 제2정규형 (2NF) — 부분 함수 종속 제거

**정의:** 1NF를 만족하고, 기본키의 일부에만 종속되는 일반 속성(부분 함수 종속)이 없어야 한다.

Điều kiện: đã là 1NF và không có thuộc tính không khóa chỉ phụ thuộc vào **một phần** của khóa ghép.

```text
수강기록(학번, 과목코드, 학생이름, 과목명, 성적)
PK = (학번, 과목코드)

학번 → 학생이름              ← PK의 일부에만 의존
과목코드 → 과목명            ← PK의 일부에만 의존
(학번, 과목코드) → 성적     ← 전체 PK에 의존
```

`학생이름` không cần biết `과목코드`; chỉ cần `학번`. `과목명` cũng chỉ cần `과목코드`. Đây là **부분 함수 종속 (partial dependency)**. Tách ra:

```text
STUDENT(학번, 학생이름)
COURSE(과목코드, 과목명)
ENROLLMENT(학번, 과목코드, 성적)
```

> **암기 / Mẹo nhớ:** **2NF = 복합키의 일부 의존 제거**.  
> Nếu PK chỉ gồm **một cột**, không thể có partial dependency; đạt 1NF thì tự động đạt 2NF.

---

### 5.3 제3정규형 (3NF) — 이행적 함수 종속 제거

**정의:** 2NF를 만족하고, 기본키가 아닌 속성이 다른 일반 속성에 종속되는 이행적 함수 종속이 없어야 한다.

Ví dụ:

```text
COURSE(과목코드, 과목명, 교수번호, 교수명)

과목코드 → 교수번호
교수번호 → 교수명
따라서 과목코드 → 교수명
```

`교수명` phụ thuộc gián tiếp vào `과목코드` qua `교수번호`. Nó không nên nằm ở bảng COURSE. Đây là **이행적 함수 종속 (transitive dependency)**: `A → B`, `B → C`, nên `A → C`.

```text
COURSE(과목코드, 과목명, 교수번호)
PROFESSOR(교수번호, 교수명)
```

> **암기 / Mẹo nhớ:** **3NF = 키 → 일반속성 → 일반속성 제거**.  
> Khóa → thuộc tính thường → thuộc tính thường: hãy tách thuộc tính ở cuối ra bảng khác.

---

### 5.4 BCNF (보이스-코드 정규형) — 결정자는 후보키

**정의:** 모든 함수적 종속 `X → Y`에서 결정자 X는 반드시 후보키이어야 한다.

BCNF chặt hơn 3NF. Cách kiểm tra: nhìn **mọi vế trái** của dependency. Vế trái có phải **후보키** không? Nếu không thì chưa BCNF.

```text
수업(학생, 과목, 교수)

(학생, 과목) → 교수
교수 → 과목       (한 교수는 한 과목만 담당한다고 가정)
```

`교수` quyết định `과목`, nhưng `교수` không phân biệt được từng row vì một giáo sư có nhiều sinh viên. Tức `교수` không phải candidate key → vi phạm BCNF.

```text
교수과목(교수, 과목)
수강(학생, 교수)
```

> **암기 / Mẹo nhớ:** **BCNF = 결정자는 반드시 후보키**.  
> Mẹo đề thi: thấy “결정자(candidate key가 아님)” là nghĩ đến BCNF.

---

### 5.5 4NF·5NF — 기억할 키워드

| Form | Korean | Loại bỏ | Mẹo Việt |
|---|---|---|---|
| 4NF | 제4정규형 | 다치 종속 (multivalued dependency) | Một khóa sinh ra nhiều tập giá trị độc lập. |
| 5NF | 제5정규형 | 조인 종속 (join dependency) | Tách bảng sao cho join lại không sinh thông tin sai. |

Chuỗi cần thuộc:

> **1NF 원자값 → 2NF 부분 함수 종속 → 3NF 이행 함수 종속 → BCNF 결정자 → 4NF 다치 종속 → 5NF 조인 종속**  
> **원·부·이·결·다·조**  
> Atomic → Partial → Transitive → Determinant → Multivalued → Join.

---

## 6. 정규화 판단 순서 / Cách làm câu hỏi chuẩn hóa

Khi đề cho relation và functional dependencies, hãy làm đúng thứ tự này:

1. **기본키/후보키를 찾는다.** Tìm PK/candidate key trước.
2. **반복 그룹 또는 다중값이 있는가?** Có list/repeating group → chưa 1NF.
3. **복합키의 일부 → 일반속성?** Có → partial dependency, chưa 2NF.
4. **키 → 일반속성 → 일반속성?** Có → transitive dependency, chưa 3NF.
5. **모든 결정자가 후보키인가?** Có determinant không phải candidate key → chưa BCNF.

**Cảnh báo:** Đừng chỉ nhìn bảng “có cột lặp”. Hãy luôn viết dependency bằng mũi tên. 2NF và 3NF được quyết định bởi **함수적 종속**, không phải cảm giác.

---

## 7. 하향식 통합 테스트: 같은 단어, 다른 맥락

Trong 정보처리기사, **하향식 (top-down)** còn xuất hiện ở **통합 테스트 (integration testing)**. Nó dùng cùng hướng “trên xuống”, nhưng không phải thiết kế database và không liên quan 1NF/2NF.

| Test style | Đi từ | Module chưa có thì dùng | Câu nhớ |
|---|---|---|---|
| 하향식 통합 테스트 | 상위 모듈 → 하위 모듈 | **Stub (스텁)** | Module dưới chưa có, dùng module giả dưới. |
| 상향식 통합 테스트 | 하위 모듈 → 상위 모듈 | **Driver (드라이버)** | Module trên chưa có, cần chương trình gọi module dưới. |

> **Top-down → Stub**, **Bottom-up → Driver**.  
> Phân biệt: top-down design = cách thiết kế/phân rã; top-down integration test = cách tích hợp và kiểm thử module.

---

## 8. 시험 직전 30초 암기 노트

```text
[DB 설계]
요구 분석 → 개념적 설계(ERD) → 논리적 설계(정규화) → 물리적 설계 → 구현(DDL)

[정규화 목적]
중복 최소화 + 갱신/삽입/삭제 이상 제거 + 무결성 향상

[정규형]
1NF: 원자값 / 한 칸에 한 값
2NF: 부분 함수 종속 제거 / 복합키의 일부 의존 제거
3NF: 이행 함수 종속 제거 / 키 → 일반속성 → 일반속성 제거
BCNF: 모든 결정자는 후보키
4NF: 다치 종속 제거
5NF: 조인 종속 제거

[통합 테스트]
하향식 = Stub
상향식 = Driver
```

---

## 9. 자기 점검 문제 / Tự kiểm tra

### 문제 1

`학생(학번, 이름, 전화번호1, 전화번호2)`에서 여러 전화번호를 한 속성에 `010-..., 02-...`처럼 저장한다면 어느 정규형을 위반하는가?

**정답: 1NF.** Một ô có nhiều value; cần tách thành row hoặc bảng số điện thoại riêng tùy yêu cầu.

### 문제 2

`주문상세(주문번호, 상품번호, 주문일자, 상품명, 수량)`의 PK는 `(주문번호, 상품번호)`이다. `주문번호 → 주문일자`, `상품번호 → 상품명`일 때 문제가 되는 정규형은?

**정답: 2NF.** `주문일자` và `상품명` chỉ phụ thuộc vào một phần PK ghép → 부분 함수 종속.

### 문제 3

`사원(사원번호, 부서번호, 부서명)`에서 `사원번호 → 부서번호`, `부서번호 → 부서명`이면 무엇을 제거해야 하는가?

**정답: 3NF의 이행 함수 종속.** Tách `부서(부서번호, 부서명)`.

### 문제 4

“모든 결정자는 후보키이어야 한다”는 어느 정규형인가?

**정답: BCNF (보이스-코드 정규형).**

---

## 10. 최종 연결 문장 / Câu kết nối để nhớ thật lâu

**하향식 설계**로 먼저 hệ thống lớn được chia nhỏ: “trường cần quản lý đăng ký môn” → “cần quản lý sinh viên, môn học, giáo sư, đăng ký”. Ta dùng ERD để mô tả thế giới thực rồi chuyển thành bảng. Khi bảng quá to và cùng một thông tin bị ghi nhiều lần, ta dùng **정규화** trong thiết kế logic: trước hết đảm bảo mỗi ô một giá trị (**1NF**), tiếp theo xóa thuộc tính chỉ phụ thuộc một phần khóa ghép (**2NF**), rồi xóa phụ thuộc gián tiếp qua thuộc tính thường (**3NF**), và ở mức nghiêm ngặt hơn kiểm tra mọi determinant đều là candidate key (**BCNF**). Khi model dữ liệu đã sạch, mới đến index và cách lưu vật lý.

> **요구를 크게 보고(하향식), 데이터를 올바르게 나누고(정규화), 마지막에 성능을 설계한다(물리적 설계).**  
> Nhìn yêu cầu lớn trước, tách dữ liệu đúng sau, rồi mới tối ưu hiệu năng ở cuối.
