# Quan hệ, Transaction, NULL và Identifier

> **Mục tiêu:** Quan hệ trong mô hình, ACID, NULL trong SQL và natural/surrogate key.

## Từ khóa cần nhớ (Keyword)

Các thuật ngữ SQLD được giữ nguyên tiếng Hàn/English trong phần nguồn. Khi ghi chú, dùng mẫu `용어 (English) (Tiếng Việt)` để nối tên gọi trong đề với ý nghĩa thực tế.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`).

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

## 제2절 관계와 조인의 이해

## Phần 2: Quan hệ và JOIN

Ba hình này nối tiếp phần **반정규화 — Denormalization — Phi chuẩn hóa**, sau đó chuyển sang **관계 — Relationship — Quan hệ** và **조인 — JOIN — Kết nối bảng**.

---

## 1. 반정규화

## 1. Phi chuẩn hóa

### 1.1 반정규화의 khái niệm

**반정규화는 역정규화라고도 하며, 비정규화와는 다르다.**

**반정규화 còn được gọi là phi chuẩn hóa, nhưng không giống hoàn toàn với việc không chuẩn hóa.**

- `반정규화`: Denormalization, điều chỉnh có chủ đích mô hình đã chuẩn hóa.
- `비정규화`: Unnormalized, mô hình chưa được chuẩn hóa đầy đủ.

**반정규화는 데이터베이스 성능 향상을 위해 데이터 중복을 허용하고 조인을 줄이는 방법이다.**

**Phi chuẩn hóa là phương pháp cho phép trùng lặp dữ liệu và giảm JOIN nhằm cải thiện hiệu năng cơ sở dữ liệu.**

**반정규화는 정규화된 데이터 모델을 중복·통합·분리하여 시스템의 개발과 운영을 단순화하는 모델링 기법이다.**

**Phi chuẩn hóa là kỹ thuật điều chỉnh mô hình đã chuẩn hóa bằng cách thêm trùng lặp, gộp hoặc tách dữ liệu để đơn giản hóa việc phát triển và vận hành hệ thống.**

---

### 1.2 반정규화의 효과와 단점

**반정규화는 조회 속도를 향상시킬 수 있지만 데이터 모델의 유연성은 낮아질 수 있다.**

**Phi chuẩn hóa có thể tăng tốc độ truy vấn nhưng có thể làm giảm tính linh hoạt của mô hình dữ liệu.**

**반정규화를 하면 입력·수정·삭제 성능이 저하될 수 있다.**

**Khi phi chuẩn hóa, hiệu năng thêm, sửa và xóa dữ liệu có thể giảm.**

Lý do là cùng một thông tin có thể được lưu ở nhiều nơi, nên khi thay đổi phải cập nhật nhiều dòng hoặc nhiều bảng.

Ví dụ, nếu `부서명` được sao chép vào bảng `사원`, khi tên phòng ban thay đổi phải sửa nhiều dòng nhân viên.

---

### 1.3 Khi nào thực hiện 반정규화?

**정규화로 엔터티와 관계의 수가 많아져 조인으로 인한 성능 저하가 예상될 때 반정규화를 수행할 수 있다.**

**Có thể thực hiện phi chuẩn hóa khi việc chuẩn hóa làm tăng số Entity và quan hệ, khiến hiệu năng JOIN được dự đoán sẽ giảm.**

**정규화에 충실할수록 데이터의 종속성과 활용성은 향상되지만 수행 속도가 느려지는 경우 반정규화를 고려할 수 있다.**

**Nếu việc tuân thủ chuẩn hóa giúp tăng tính phụ thuộc và khả năng sử dụng dữ liệu nhưng làm tốc độ xử lý chậm, có thể cân nhắc phi chuẩn hóa.**

**대량의 범위를 자주 처리해야 하는 경우 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên phải xử lý một phạm vi dữ liệu lớn.**

**특정 범위의 데이터만 자주 처리하는 경우 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên chỉ xử lý một phạm vi dữ liệu cụ thể.**

**요약이나 집계 정보가 자주 요구되는 경우 반정규화를 고려할 수 있다.**

**Có thể cân nhắc phi chuẩn hóa khi thường xuyên cần thông tin tóm tắt hoặc tổng hợp.**

Ví dụ:

- Tổng doanh thu theo tháng.
- Số lượng nhân viên theo phòng ban.
- Số đơn hàng của từng khách hàng.
- Tổng điểm hoặc tổng số giao dịch.

**반정규화가 조회 성능 향상을 항상 보장하는 것은 아니다.**

**Phi chuẩn hóa không phải lúc nào cũng bảo đảm cải thiện hiệu năng truy vấn.**

Phải kiểm tra SQL thực tế, dữ liệu thực tế và Execution Plan trước khi quyết định.

---

## 2. Ví dụ 반정규화 trong hình

## 2. Ví dụ phi chuẩn hóa trong hình

Trong hình có hai bảng đã được chuẩn hóa:

#### 사원 테이블 — Bảng nhân viên

| 사번(PK) | 이름 | 부서번호 |
| --- | --- | --- |
| 2401 | 김지민 | 100 |
| 2402 | 이사원 | 101 |
| 2403 | 유현지 | 201 |

#### 부서 테이블 — Bảng phòng ban

| 부서번호(PK) | 부서명 | 소재지 |
| --- | --- | --- |
| 100 | 영업부 | 서울 |
| 101 | 개발부 | 서울 |
| 201 | 생산부 | 부산 |

**사원 테이블의 부서번호와 부서 테이블의 부서번호가 같은 값을 가지므로 두 테이블을 연결할 수 있다.**

**Vì `부서번호` trong bảng nhân viên và `부서번호` trong bảng phòng ban có cùng giá trị nên có thể kết nối hai bảng.**

**부서번호가 두 테이블을 연결하는 JOIN KEY가 된다.**

**`부서번호` trở thành JOIN KEY kết nối hai bảng.**

Câu SQL tương ứng:

```sql
SELECT s.사번,
       s.이름,
       s.부서번호,
       d.부서명,
       d.소재지
FROM 사원 s
JOIN 부서 d
  ON s.부서번호 = d.부서번호;
```

Khi thực hiện truy vấn này, thông tin phòng ban được lấy bằng JOIN thay vì lưu lặp lại trong bảng nhân viên.

Nếu phi chuẩn hóa, có thể thêm `부서명` và `부서 위치` vào bảng `사원`.

```
사원(사번, 이름, 부서번호, 부서명, 부서위치)
```

Khi đó truy vấn đơn giản hơn, nhưng nếu tên phòng ban thay đổi thì nhiều dòng nhân viên cần được cập nhật.

---

## 3. 관계

## 3. Quan hệ

### 3.1 관계의 정의

**관계는 엔터티의 인스턴스 사이에 존재하는 논리적인 연관성이다.**

**Quan hệ là sự liên kết logic tồn tại giữa các Instance của các Entity.**

Nói đơn giản:

- Entity là đối tượng hoặc chủ đề.
- Instance là một bản ghi cụ thể của Entity.
- Relationship là mối liên hệ giữa các bản ghi đó.

Ví dụ:

```
사원 Entity
부서 Entity
```

Một nhân viên cụ thể `김지민` thuộc một phòng ban cụ thể `영업부`.

Đây là quan hệ giữa một Instance của `사원` và một Instance của `부서`.

---

### 3.2 Quan hệ thông qua hành động

**관계는 엔터티 사이의 존재 관계와 행위 관계로 구분할 수 있다.**

**Quan hệ có thể được chia thành quan hệ tồn tại và quan hệ hành vi.**

#### 존재 관계

**존재 관계는 한 엔터티가 다른 엔터티에 소속되는 관계이다.**

**Quan hệ tồn tại là quan hệ trong đó một Entity thuộc về một Entity khác.**

Ví dụ:

```
사원은 부서에 소속된다.
Nhân viên thuộc phòng ban.
```

Trong hình:

```
사원 ── 소속 ── 부서
```

#### 행위 관계

**행위 관계는 어떤 행위를 통해 엔터티 사이에 발생하는 관계이다.**

**Quan hệ hành vi là quan hệ phát sinh giữa các Entity thông qua một hành động.**

Ví dụ:

```
고객이 주문한다.
Khách hàng đặt hàng.
```

Quan hệ `주문` phát sinh khi khách hàng thực hiện hành động đặt hàng.

---

## 4. 식별관계와 비식별관계

## 4. Quan hệ định danh và không định danh

### 4.1 식별관계

**부모의 식별자를 자식의 식별자에 포함하면 식별관계이다.**

**Nếu khóa định danh của cha được bao gồm trong khóa định danh của con thì đó là quan hệ định danh.**

Ví dụ:

```
부모 PK → 자식 PK
```

Trong quan hệ định danh, khóa của bảng cha trở thành một phần của PK bảng con.

Ví dụ:

```
주문(PK: 주문번호)
주문상세(PK: 주문번호 + 상품번호)
```

`주문번호` của bảng `주문` đồng thời tham gia vào PK của `주문상세`.

---

### 4.2 비식별관계

**부모의 식별자를 자식의 일반 속성으로 포함하면 비식별관계이다.**

**Nếu khóa định danh của cha chỉ được đưa vào bảng con với tư cách thuộc tính thường thì đó là quan hệ không định danh.**

Ví dụ:

```
부서(부서번호 PK)
사원(사번 PK, 부서번호 FK)
```

`부서번호` là PK của bảng `부서`, nhưng trong bảng `사원`, nó chỉ là FK chứ không tham gia vào PK.

---

## 5. 조인

## 5. JOIN

### 5.1 Khái niệm JOIN

**조인은 두 테이블의 공통 속성을 이용하여 데이터를 결합하는 것이다.**

**JOIN là việc kết hợp dữ liệu của hai bảng bằng thuộc tính chung.**

**조인에 사용되는 공통 속성을 조인 키 또는 JOIN KEY라고 한다.**

**Thuộc tính chung được sử dụng để JOIN gọi là Join Key hoặc JOIN KEY.**

Trong ví dụ:

```
사원.부서번호 = 부서.부서번호
```

`부서번호` là JOIN KEY.

---

### 5.2 JOIN trước và sau chuẩn hóa

Trước chuẩn hóa, bảng `사원` chứa cả:

```
사번, 이름, 부서번호, 부서명, 부서위치
```

Khi đó có thể truy vấn trực tiếp:

```sql
SELECT 사번, 이름, 부서명
FROM 사원
WHERE 사번 = '2401';
```

Sau chuẩn hóa, bảng `사원` chỉ chứa:

```
사번, 이름, 부서번호
```

Bảng `부서` chứa:

```
부서번호, 부서명, 부서위치
```

Muốn lấy thông tin đầy đủ phải JOIN:

```sql
SELECT a.사번,
       a.이름,
       b.부서명
FROM 사원 a,
     부서 b
WHERE a.부서번호 = b.부서번호
  AND a.사번 = '2401';
```

Hoặc viết theo ANSI JOIN:

```sql
SELECT a.사번,
       a.이름,
       b.부서명
FROM 사원 a
JOIN 부서 b
  ON a.부서번호 = b.부서번호
WHERE a.사번 = '2401';
```

**정규화 후에는 데이터의 독립성이 높아지지만 필요한 정보를 함께 조회하려면 조인이 필요하다.**

**Sau chuẩn hóa, tính độc lập của dữ liệu tăng lên nhưng cần JOIN khi muốn truy vấn các thông tin liên quan cùng lúc.**

---

## 6. Self JOIN

## 6. Tự JOIN

### 6.1 관계형 데이터 모델

**관계형 데이터 모델에서 자기 자신끼리의 관계를 자기 자신과의 관계라고 한다.**

**Trong mô hình dữ liệu quan hệ, quan hệ giữa các bản ghi trong cùng một Entity gọi là quan hệ với chính nó.**

Một Entity có thể chứa quan hệ phân cấp giữa các Instance của chính Entity đó.

Ví dụ:

```
직원 → 상사
Nhân viên → Cấp trên
```

Cùng một bảng `직원`, nhưng một dòng có thể là cấp trên của dòng khác.

---

### 6.2 Ví dụ bảng nhân viên

| 직원ID(PK) | 이름 | 상사ID |
| --- | --- | --- |
| 1 | 나사장 | NULL |
| 2 | 김철수 | 1 |
| 3 | 이지현 | 1 |
| 4 | 황수지 | 2 |
| 5 | 박현석 | 3 |

Ý nghĩa:

- `나사장` không có cấp trên nên `상사ID = NULL`.
- `김철수` có cấp trên là nhân viên `1`.
- `이지현` có cấp trên là nhân viên `1`.
- `황수지` có cấp trên là nhân viên `2`.
- `박현석` có cấp trên là nhân viên `3`.

**상사ID는 같은 직원 테이블의 직원ID를 참조한다.**

**`상사ID` tham chiếu đến `직원ID` trong chính bảng nhân viên.**

Đây là Self Referencing Foreign Key.

---

### 6.3 SQL Self JOIN

**어떤 직원의 상사 이름을 조회하려면 직원 테이블을 두 번 사용해야 한다.**

**Muốn truy vấn tên cấp trên của một nhân viên thì phải sử dụng bảng nhân viên hai lần.**

```sql
SELECT e.이름 AS 직원이름,
       m.이름 AS 상사이름
FROM 직원 e
LEFT JOIN 직원 m
  ON e.상사ID = m.직원ID;
```

Giải thích:

- `e`: bảng đại diện cho nhân viên.
- `m`: bảng đại diện cho cấp trên.
- `e.상사ID = m.직원ID`: cấp trên của nhân viên là nhân viên có ID tương ứng.

Kết quả:

| 직원이름 | 상사이름 |
| --- | --- |
| 나사장 | NULL |
| 김철수 | 나사장 |
| 이지현 | 나사장 |
| 황수지 | 김철수 |
| 박현석 | 이지현 |

**자기 자신을 두 개의 별칭으로 나누어 사용하는 조인을 셀프 조인이라고 한다.**

**JOIN một bảng với chính nó bằng hai bí danh khác nhau gọi là Self JOIN.**

---

## 7. 상호 배타적 관계

## 7. Quan hệ loại trừ lẫn nhau

### 7.1 Khái niệm

**상호 배타적 관계는 하나의 부모가 여러 자식 중 하나의 자식과만 관계를 가지는 것이다.**

**Quan hệ loại trừ lẫn nhau là quan hệ trong đó một bản ghi cha chỉ có quan hệ với một trong nhiều loại bản ghi con.**

Trong hình có:

```
개인고객
법인고객
주문
```

Một `주문` có thể thuộc về:

- Một `개인고객`, hoặc
- Một `법인고객`.

Nhưng không thể đồng thời thuộc về cả hai.

**주문은 개인고객 또는 법인고객 중 하나만 참조할 수 있다.**

**Một đơn hàng chỉ có thể tham chiếu đến một trong hai loại: khách hàng cá nhân hoặc khách hàng doanh nghiệp.**

---

### 7.2 Cấu trúc trong hình

Bảng `개인고객`:

```
고객번호
개인고객명
```

Bảng `법인고객`:

```
법인번호
법인명
```

Bảng `주문`:

```
주문번호
고객구분코드
개인/법인번호(FK)
```

`고객구분코드` dùng để phân biệt đơn hàng thuộc khách hàng cá nhân hay doanh nghiệp.

Ví dụ:

```
고객구분코드 = 개인
→ 개인고객번호를 참조

고객구분코드 = 법인
→ 법인번호를 참조
```

**고객구분코드에 따라 개인번호 또는 법인번호 중 하나만 유효하다.**

**Tùy vào mã loại khách hàng, chỉ số cá nhân hoặc số doanh nghiệp có hiệu lực.**

Đây chính là tính `Exclusive-OR`.

```
개인 OR 법인
Cá nhân HOẶC doanh nghiệp
```

Không phải:

```
개인 AND 법인
Cá nhân VÀ doanh nghiệp
```

---

## KẾT LUẬN GHI NHỚ CUỐI BÀI

### 1. 반정규화

**반정규화는 조회 성능을 위해 중복을 허용하고 JOIN을 줄이는 방법이다.**

**Phi chuẩn hóa là cách cho phép trùng lặp và giảm JOIN để cải thiện hiệu năng truy vấn.**

Nhưng phải nhớ:

```
조회 성능 ↑ 가능
입력/수정/삭제 성능 ↓ 가능
유연성 ↓ 가능
```

---

### 2. 관계

| 한국어 | English | Nghĩa |
| --- | --- | --- |
| 존재 관계 | Existence Relationship | Quan hệ tồn tại |
| 행위 관계 | Action Relationship | Quan hệ hành vi |
| 식별관계 | Identifying Relationship | Quan hệ định danh |
| 비식별관계 | Non-identifying Relationship | Quan hệ không định danh |
| 상호 배타적 관계 | Exclusive-OR Relationship | Quan hệ loại trừ lẫn nhau |

---

### 3. JOIN

**조인은 공통 속성인 JOIN KEY를 이용해 여러 테이블의 데이터를 결합하는 것이다.**

**JOIN là kết hợp dữ liệu của nhiều bảng bằng thuộc tính chung gọi là JOIN KEY.**

Ví dụ:

```sql
ON 사원.부서번호 = 부서.부서번호
```

---

### 4. Self JOIN

**셀프 조인은 하나의 테이블을 서로 다른 별칭으로 두 번 사용하여 자기 자신과 JOIN하는 것이다.**

**Self JOIN là JOIN một bảng với chính nó bằng hai bí danh khác nhau.**

Ví dụ thường gặp:

- Nhân viên - cấp trên.
- Danh mục cha - danh mục con.
- Bình luận cha - bình luận trả lời.
- Cấu trúc thư mục.

---

### 5. Câu ghi nhớ cuối bài

```
정규화하면 JOIN 증가
→ JOIN KEY로 테이블 연결
→ 같은 테이블끼리 연결하면 SELF JOIN
→ 여러 자식 중 하나만 연결하면 EXCLUSIVE-OR
```

**Chuẩn hóa làm tăng JOIN; các bảng được kết nối bằng JOIN KEY; cùng một bảng JOIN với chính nó là Self JOIN; chỉ được kết nối với một trong nhiều loại con là Exclusive-OR.**
---

## 제3절 모델이 표현하는 트랜잭션의 이해

## Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu

### 1. 트랜잭션(Transaction)이란?

> **트랜잭션은 업무 처리를 위한 논리적인 작업 단위이다.**
Transaction là **một đơn vị công việc logic để xử lý một nghiệp vụ**.
> 

#### Keyword: 트랜잭션 — Transaction — Giao dịch

Điểm quan trọng nhất là đừng hiểu `Transaction = một câu SQL`.

Một transaction có thể chứa:

```sql
SELECT ...
UPDATE ...
INSERT ...
DELETE ...
```

Nhiều câu SQL có thể cùng phục vụ **một nghiệp vụ duy nhất**, nên chúng được gom lại thành **một transaction**.

Ví dụ nghiệp vụ:

> A chuyển 1 triệu won cho B.
> 

Về mặt nghiệp vụ, đây là **một việc duy nhất**.

Nhưng DB phải thực hiện nhiều bước:

```
A → B chuyển 1 triệu

① Kiểm tra A có đủ tiền
② Trừ A 1 triệu
③ Cộng B 1 triệu
```

Có thể tưởng tượng SQL:

```sql
SELECT balance
FROM account
WHERE customer_id = 'A';

UPDATE account
SET balance = balance - 1000000
WHERE customer_id = 'A';

UPDATE account
SET balance = balance + 1000000
WHERE customer_id = 'B';

COMMIT;
```

Ba câu SQL khác nhau, nhưng xét về nghiệp vụ:

```
[      ONE TRANSACTION       ]

check A
   ↓
-1,000,000 A
   ↓
+1,000,000 B
   ↓
COMMIT
```

---

## 2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다

> **하나의 트랜잭션에 속한 동작들은 모두 성공하거나, 모두 취소(UNDO)되어야 한다.**
Các thao tác thuộc cùng một transaction phải **hoặc thành công toàn bộ, hoặc bị hủy toàn bộ**.
> 

Đây chính là:

### All or Nothing

Ví dụ A có:

```
A = 5,000,000
B = 2,000,000
```

Chuyển 1 triệu:

```
A: 5M → 4M
B: 2M → 3M
```

Đúng.

Nhưng giả sử:

```
① A -1M     SUCCESS
② B +1M     ERROR
```

DB không được để:

```
A = 4M
B = 2M
```

vì 1 triệu đã “biến mất”.

Ngược lại cũng không được:

```
A = 5M
B = 3M
```

vì tiền tự nhiên xuất hiện.

Vì vậy:

```
① A -1M
② B +1M
      │
      ├── tất cả SUCCESS → COMMIT
      │
      └── có lỗi         → ROLLBACK
```

#### COMMIT

> **COMMIT은 트랜잭션의 변경사항을 확정한다.**
COMMIT xác nhận và làm cho các thay đổi của transaction được hoàn tất.
> 

#### ROLLBACK

> **ROLLBACK은 트랜잭션에서 발생한 변경사항을 취소한다.**
ROLLBACK hủy các thay đổi xảy ra trong transaction.
> 

Đây là ý trong ảnh:

> **부분 COMMIT 불가, 동시 COMMIT이나 ROLLBACK으로 처리**
Không được commit từng phần; toàn bộ nghiệp vụ phải được xử lý thống nhất bằng COMMIT hoặc ROLLBACK.
> 

---

## 3. 왜 ERD에서 트랜잭션이 중요한가?

## Tại sao Transaction lại liên quan đến ERD?

Đây là đoạn rất dễ đọc qua nhưng lại quan trọng trong SQLD.

> **두 엔터티의 관계가 서로 필수적일 때 하나의 트랜잭션을 형성한다.**
Khi quan hệ giữa hai entity mang tính bắt buộc với nhau trong nghiệp vụ, chúng có xu hướng cùng tham gia một transaction.
> 

Ví dụ:

```
고객 ───── 주문
Customer    Order
```

Nếu nghiệp vụ yêu cầu một `주문` phải gắn với một `고객`, thì quan hệ đó mang tính bắt buộc ở phía tương ứng.

Ngược lại:

> **두 엔터티가 서로 독립적인 수행이 가능하다면 선택적 관계로 표현한다.**
Nếu nghiệp vụ của hai entity có thể diễn ra độc lập thì quan hệ có thể được biểu diễn dưới dạng optional.
> 

---

## 4. 필수적 관계 vs 선택적 관계

### 필수적 관계 — Mandatory Relationship

> **관계가 반드시 존재해야 한다.**
Quan hệ bắt buộc phải tồn tại.
> 

Ví dụ:

```
주문 → 고객
Order → Customer
```

Nếu quy tắc nghiệp vụ nói:

> 주문은 반드시 고객에게 속한다.
Mỗi đơn hàng bắt buộc phải thuộc về một khách hàng.
> 

thì phía đó là mandatory.

---

### 선택적 관계 — Optional Relationship

> **관계가 없어도 엔터티 인스턴스가 존재할 수 있다.**
Một instance của entity vẫn có thể tồn tại dù chưa có quan hệ đó.
> 

Ví dụ:

```
고객
Pham
```

Pham vừa đăng ký tài khoản nhưng chưa từng đặt hàng.

Vậy:

```
Customer → Order

0..N
```

Một customer có thể có:

```
0 order
1 order
N orders
```

---

## 5. IE와 Barker 표기법

Ảnh của bạn nhấn mạnh sự khác nhau về ký hiệu.

#### IE 표기법

> **필수적 관계: 원 X**
Quan hệ bắt buộc: không có vòng tròn.
> 

> **선택적 관계: 원 O**
Quan hệ optional: có vòng tròn `○`.
> 

Có thể nhớ:

```
○ = zero allowed
```

Có vòng tròn nghĩa là:

```
0개도 가능
0 cũng được
→ optional
```

#### Barker 표기법

> **필수적 관계: 실선의 관계선**
Mandatory → đường liền.
> 

> **선택적 관계: 점선의 관계선**
Optional → đường đứt.
> 

Mẹo thi:

```
IE
○ → Optional

Barker
------  solid  → Mandatory
- - - - dashed → Optional
```

---

## 6. 트랜잭션의 특징 — ACID

Ảnh tiếp theo đưa ra 4 thuộc tính cực kỳ quan trọng:

```
A → Atomicity
C → Consistency
I → Isolation
D → Durability
```

Đây chính là **ACID**.

---

### ① 원자성 Atomicity — Tính nguyên tử

> **트랜잭션은 더 이상 분해가 불가능한 업무의 최소단위이다.**
Transaction được xem là đơn vị nghiệp vụ nhỏ nhất không thể chia nhỏ thêm khi xét tính hoàn thành.
> 

> **전부 처리되거나 모두 처리되지 않아야 한다.**
Hoặc toàn bộ được thực hiện, hoặc toàn bộ không được thực hiện.
> 

Chính là:

```
ALL OR NOTHING
```

Ví dụ:

```
A - 1M
B + 1M
```

Không được:

```
A -1M ✓
B +1M ✗
```

Mà phải:

```
✓ ✓ → COMMIT

hoặc

✗ → ROLLBACK toàn bộ
```

#### Keyword nhớ nhanh

```
Atomicity
= 원자성
= All or Nothing
= COMMIT / ROLLBACK
```

---

## 7. ② 일관성 Consistency — Tính nhất quán

> **트랜잭션이 성공적으로 완료된 후에도 DB는 일관된 상태여야 한다.**
Sau khi transaction hoàn tất thành công, database vẫn phải ở trạng thái nhất quán.
> 

Điểm cốt lõi:

```
DB hợp lệ
   ↓
Transaction
   ↓
DB vẫn hợp lệ
```

Ví dụ trước chuyển tiền:

```
A = 5M
B = 2M

Total = 7M
```

Sau:

```
A = 4M
B = 3M

Total = 7M
```

Các ràng buộc nghiệp vụ vẫn đúng.

Consistency không chỉ là tiền. Nó còn liên quan tới:

```
PK
FK
UNIQUE
CHECK
NOT NULL
Business Rule
```

Ví dụ:

```sql
CHECK (balance >= 0)
```

Nếu transaction khiến:

```
balance = -1,000,000
```

trong khi hệ thống cấm số dư âm, thì trạng thái DB không còn thỏa quy tắc.

#### Nhớ:

```
Consistency
= trước hợp lệ
→ transaction
→ sau vẫn hợp lệ
```

---

## 8. ③ 격리성 Isolation — Tính cô lập

> **실행 중인 트랜잭션의 중간결과를 다른 트랜잭션이 접근할 수 없다.**
Transaction khác không được tùy ý nhìn thấy/kế thừa trạng thái trung gian chưa hoàn tất của transaction đang chạy.
> 

Giả sử:

```
Transaction A

UPDATE balance - 1M
...
chưa COMMIT
```

Transaction B không nên dựa vào trạng thái chưa hoàn tất đó như thể nó đã được xác nhận.

Có thể hình dung:

```
T1: A -1M ---------------- COMMIT
         ↑
         │ trạng thái trung gian
         │
T2: không nên nhìn nó như dữ liệu đã hoàn tất
```

Đây là lý do xuất hiện các vấn đề concurrency như:

```
Dirty Read
Non-repeatable Read
Phantom Read
```

và các mức:

```
READ UNCOMMITTED
READ COMMITTED
REPEATABLE READ
SERIALIZABLE
```

SQLD ở đoạn này chủ yếu cần nhớ bản chất:

> **Isolation = các transaction đang chạy phải được cách ly thích hợp với nhau.**
> 

---

## 9. ④ 영속성 / 지속성 Durability — Tính bền vững

> **트랜잭션이 성공적으로 완료되면 결과는 데이터베이스에 영속적으로 저장된다.**
Khi transaction đã hoàn tất thành công, kết quả phải được lưu bền vững trong database.
> 

Tức là:

```
COMMIT 완료
    ↓
결과 유지
```

Ví dụ bạn chuyển tiền thành công.

Sau đó:

```
server restart
```

thì không được quay lại:

```
A = 5M
B = 2M
```

mà phải giữ:

```
A = 4M
B = 3M
```

---

## ⭐ Tổng hợp ACID cực dễ nhớ

| Korean | English | Ý chính |
| --- | --- | --- |
| 원자성 | Atomicity | All or Nothing |
| 일관성 | Consistency | Trước/sau đều hợp lệ |
| 격리성 | Isolation | Transaction không can thiệp trạng thái trung gian của nhau |
| 영속성 | Durability | COMMIT rồi thì phải được giữ |

Nhớ chuỗi:

```
Atomicity   → Có làm hết không?
Consistency → Kết quả có hợp lệ không?
Isolation   → Transaction khác có gây/nhìn thấy ảnh hưởng trung gian không?
Durability  → Commit rồi có giữ được không?
```

---

## 제4절 NULL 속성의 이해

## Phần 4 — NULL

Đây là phần **rất dễ bị gài trong SQLD**.

### 10. NULL là gì?

> **NULL은 아직 정의되지 않은 값이다.**
NULL là giá trị **chưa được xác định / không biết / không tồn tại theo ngữ cảnh**, chứ không phải một giá trị thông thường.
> 

Trong ảnh:

> **NULL은 0 또는 공백과 다르다.**
NULL khác `0` và khác chuỗi rỗng/khoảng trắng.
> 

Đây là điểm bắt buộc phải nhớ:

```
NULL ≠ 0
NULL ≠ ' '
```

Về mặt khái niệm:

```
0
→ biết giá trị
→ giá trị chính xác là zero

NULL
→ không biết/chưa có giá trị
```

Ví dụ:

```
나이 = 0
```

nghĩa là biết tuổi bằng 0.

Nhưng:

```
나이 = NULL
```

nghĩa là:

> Không biết tuổi / chưa nhập tuổi.
> 

---

## 11. NULL trong phép toán

> **NULL 값을 포함하는 연산의 결과값도 NULL 값이다.**
Phép toán có NULL thường cho kết quả NULL.
> 

Ví dụ:

```sql
10 + NULL
```

→

```
NULL
```

Tại sao?

Bởi vì:

```
10 + một giá trị không biết
```

thì kết quả cũng:

```
không biết
```

Tương tự:

```
NULL + 100 → NULL
NULL - 10  → NULL
NULL * 2   → NULL
```

---

## 12. NVL và ISNULL

Trong Oracle:

```sql
NVL(column, replacement)
```

Ví dụ:

```sql
NVL(C, 0)
```

> **컬럼 C의 NULL 값을 0으로 치환한다.**
Thay NULL trong cột C bằng 0.
> 

Ví dụ:

```
C
----
10
NULL
20
```

```sql
SELECT NVL(C, 0)
```

→

```
10
0
20
```

Lưu ý SQLD thường xoay quanh Oracle, vì vậy hãy nhớ mạnh:

```sql
NVL()
```

`ISNULL()` phổ biến ở SQL Server.

---

## 13. NULL không được so sánh bằng =

Đây là câu cực quan trọng trong ảnh:

> **NULL과의 모든 비교(IS NULL 제외)는 알 수 없음(UNKNOWN)을 반환한다.**
Các phép so sánh thông thường với NULL trả về UNKNOWN, ngoại trừ kiểm tra `IS NULL`/`IS NOT NULL`.
> 

Sai:

```sql
WHERE column = NULL
```

Đúng:

```sql
WHERE column IS NULL
```

Và:

```sql
WHERE column IS NOT NULL
```

---

### Tại sao `NULL = NULL` không phải TRUE?

Vì NULL nghĩa là:

```
unknown
```

Ví dụ:

```
A = NULL
B = NULL
```

Bạn không biết A.

Bạn cũng không biết B.

Không có nghĩa:

```
A = B
```

Ví dụ thực tế:

```
A tuổi = không biết
B tuổi = không biết
```

Không thể kết luận:

```
A và B bằng tuổi nhau
```

Do đó:

```sql
NULL = NULL
```

không trả về `TRUE`.

Trong logic SQL:

```
TRUE
FALSE
UNKNOWN
```

được gọi là **Three-Valued Logic — 3VL**.

---

## 14. NULL trong Aggregate Function

Ảnh có bảng:

```
컬럼1    컬럼2
10       20
20       NULL
```

Hãy tính.

#### COUNT(column)

```sql
COUNT(column1)
```

→ `2`

```sql
COUNT(column2)
```

→ `1`

Vì:

> **COUNT(column)은 NULL을 제외한다.**
COUNT(column) bỏ qua NULL.
> 

---

#### SUM

```sql
SUM(column1)
= 10 + 20
= 30
```

```sql
SUM(column2)
= 20
```

NULL bị bỏ qua.

---

#### AVG

Đây là chỗ cực dễ sai.

```sql
AVG(column2)
```

không phải:

```
(20 + 0) / 2
= 10 ❌
```

Mà là:

```
20 / 1
= 20 ✓
```

Vì:

> **집계 함수에서 NULL은 0이 아니라 계산 대상에서 제외된다.**
Trong aggregate function, NULL không được xem là 0 mà bị loại khỏi tập tính toán.
> 

---

## 15. COUNT(*) khác COUNT(column)

```sql
COUNT(*)
```

> **NULL 여부와 관계없이 행 자체를 센다.**
Đếm số dòng, bất kể trong dòng có NULL hay không.
> 

Trong bảng:

```
row 1
row 2
```

→

```sql
COUNT(*) = 2
```

Nhưng:

```sql
COUNT(column2) = 1
```

Vì row thứ hai:

```
column2 = NULL
```

Do đó:

```
COUNT(*)       → đếm ROW
COUNT(column)  → đếm NON-NULL
```

#### ⭐ Đây là một công thức SQLD rất đáng nhớ

```
COUNT(*) = 모든 행
COUNT(col) = NULL 제외
```

---

## 16. Nếu column là PK?

Ảnh ghi:

> **컬럼이 PK라면 NULL값 허용 X → 항상 COUNT(*) = COUNT(컬럼)**
Nếu column là PK thì không cho phép NULL, vì vậy COUNT(*) luôn bằng COUNT(column) trên bảng đó.
> 

Vì:

```
PRIMARY KEY
= UNIQUE
+ NOT NULL
```

Cho nên:

```sql
COUNT(*)
```

và:

```sql
COUNT(pk_column)
```

sẽ bằng nhau.

---

## 17. Trung bình trên toàn bộ số dòng

Ảnh nhấn mạnh:

```
전체 행 개수에 대한 평균
= SUM(column) / COUNT(*)
```

Khác với:

```sql
AVG(column)
```

Ví dụ:

```
20
NULL
```

#### AVG(column)

```
20 / 1
= 20
```

#### SUM(column)/COUNT(*)

```
20 / 2
= 10
```

Hai kết quả hoàn toàn khác nhau.

Đây là dạng bẫy SQLD rất phổ biến.

---

## 18. NULL의 ERD 표기법

Ảnh nói:

#### IE

> **NULL 허용 여부 알 수 없음**
Không thể xác định trực tiếp việc attribute có cho phép NULL hay không từ cách biểu diễn attribute như trong hình.
> 

#### Barker

> **속성 앞 동그라미 표시**
Dùng ký hiệu trước thuộc tính để biểu diễn tính optional.
> 

Trong hình Barker:

```
## 주문번호
○ 주문금액
○ 주문취소금액
```

Trong đó `#` liên quan đến identifier/key, còn `○` biểu thị thuộc tính optional.

---

## 제5절 본질식별자 vs 인조식별자

Đây là phần tiếp nối trực tiếp kiến thức `식별자` bạn vừa học trước đó.

## 19. 본질식별자 — Natural/Original Identifier

Ảnh dùng:

> **원조(본질) 식별자**
Identifier được hình thành tự nhiên từ nghiệp vụ và cần thiết cho việc phân biệt dữ liệu.
> 

Ví dụ:

```
학번
주민등록번호
사번
```

Tức là bản thân nghiệp vụ đã có nó.

Ví dụ:

```
학생

학번
----
20260001
20260002
```

Không phải vì DB cần PK nên ta mới nghĩ ra `학번`; nó vốn có ý nghĩa trong nghiệp vụ trường học.

Có thể liên hệ với thuật ngữ phổ biến:

```
본질식별자
≈ Natural Key / Business Key
```

---

## 20. 인조식별자 — Surrogate Key

> **업무에는 존재하지 않지만 편의성을 위해 인위적으로 만든 식별자이다.**
Là identifier không tồn tại tự nhiên trong nghiệp vụ nhưng được tạo nhân tạo để thuận tiện cho hệ thống.
> 

Ví dụ:

```
ORDER_DETAIL_ID
USER_ID
SEQ
AUTO_INCREMENT
IDENTITY
```

Ví dụ:

```
주문상세번호
-------------
1
2
3
4
```

`주문상세번호` có thể chẳng có ý nghĩa gì với khách hàng.

Nó chỉ giúp DB nói:

```
đây là row #1
đây là row #2
```

Đó chính là:

```
Surrogate Key
= 인조식별자
```

---

## 21. Tại sao cần 인조식별자?

Ảnh đưa ra ví dụ rất hay.

Ban đầu `주문이력` dùng:

```
PK = 주문번호 + 상품번호
```

Tức composite PK:

```
ORDER_ID + PRODUCT_ID
```

Ví dụ:

```
101 + c03
101 + c05
101 + c06
```

Đều khác nhau → OK.

Nhưng vài giờ sau khách thêm lại `c03`:

```
101 + c03
```

Ta có:

```
101 c03 ← lần đầu
101 c05
101 c06
101 c03 ← lần sau
```

PK:

```
(101, c03)
```

bị trùng.

→ `PRIMARY KEY violation`.

---

## 22. Giải pháp: 주문상세번호

Ta thêm:

```
주문상세번호
Order Detail ID
```

Ví dụ:

```
주문상세번호 | 주문번호 | 상품번호
---------------------------------
1            101       c03
2            101       c05
3            101       c06
4            101       c03
```

Bây giờ:

```
PK = 주문상세번호
```

nên:

```
1 ≠ 4
```

Hai row được phân biệt.

Đây chính là **인조식별자**.

Có thể sinh bằng Oracle Sequence:

```sql
주문상세번호_SEQ.NEXTVAL
```

Ví dụ:

```sql
INSERT INTO 주문이력
VALUES (주문상세번호_SEQ.NEXTVAL, '101', 'c03', 3, ...);
```

Sequence tự sinh:

```
1
2
3
4
...
```

---

## 23. Nhưng 인조식별자 tạo ra một vấn đề lớn

Đây là phần ảnh muốn bạn đặc biệt chú ý.

Khi:

```
PK = 주문상세번호
```

thì DB chỉ kiểm tra:

```
주문상세번호 unique?
```

Ví dụ:

```
ID | ORDER | PRODUCT
--------------------
1  | 101   | c03
2  | 101   | c05
3  | 101   | c06
4  | 101   | c03
```

Về PK:

```
1
2
3
4
```

→ tất cả unique.

Cho nên DB chấp nhận.

Nhưng nếu nghiệp vụ **không cho phép cùng một `(주문번호, 상품번호)` xuất hiện lặp lại**, thì surrogate PK đã che mất business uniqueness đó.

Đây là ý:

> **인조식별자만이 주식별자라 시스템 오류로 인한 중복 데이터의 입력을 막을 수 없다.**
Nếu chỉ dựa vào surrogate identifier làm primary identifier thì có thể không ngăn được duplicate theo business key.
> 

---

## 24. Đây chính là nhược điểm quan trọng của 인조식별자

Ảnh liệt kê:

> **중복 데이터 발생 가능성 → 데이터 품질 저하**
Có khả năng phát sinh dữ liệu trùng → giảm chất lượng dữ liệu.
> 

Ví dụ:

```
ID | ORDER | PRODUCT
1  | 101   | C03
2  | 101   | C03
```

PK vẫn:

```
1 ≠ 2
```

→ DB nói OK.

Nhưng nghiệp vụ có thể nói:

```
101 + C03
```

không được duplicate.

Vậy cần thêm:

```sql
UNIQUE (ORDER_ID, PRODUCT_ID)
```

nếu business rule yêu cầu uniqueness.

---

## 25. 인조식별자 có thể làm tăng Index

Ảnh nói:

> **불필요한 인덱스 생성 → 저장 공간 낭비 및 DML 성능 저하**
Có thể phát sinh index bổ sung không cần thiết → tốn storage và giảm hiệu năng DML.
> 

Ví dụ:

```
PK:
ORDER_DETAIL_ID
```

DB thường cần index phục vụ PK/unique constraint.

Nhưng thực tế query thường:

```sql
WHERE ORDER_ID = ?
AND PRODUCT_ID = ?
```

thì có thể lại cần index:

```
(ORDER_ID, PRODUCT_ID)
```

Kết quả:

```
Index 1 → ORDER_DETAIL_ID
Index 2 → ORDER_ID + PRODUCT_ID
```

Trong khi nếu thiết kế phù hợp khác đi, có trường hợp có thể giảm một phần index.

Mỗi index bổ sung làm DML như:

```sql
INSERT
UPDATE
DELETE
```

tốn thêm chi phí vì DB không chỉ sửa table mà còn phải duy trì index.

---

## 26. Một vấn đề khác: Query vẫn phải dùng business columns

Ảnh nói rất đúng:

> **검색할 때 결국 주문번호와 상품번호를 기반으로 WHERE절을 작성하게 된다.**
Khi tìm kiếm dữ liệu, cuối cùng ta vẫn thường viết WHERE dựa trên 주문번호 và 상품번호.
> 

Ví dụ người dùng không biết:

```
ORDER_DETAIL_ID = 473928
```

Họ biết:

```
Order = 101
Product = C03
```

Vì vậy ứng dụng lại query:

```sql
SELECT *
FROM 주문이력
WHERE 주문번호 = '101'
AND 상품번호 = 'C03';
```

Chứ không phải lúc nào cũng:

```sql
WHERE 주문상세번호 = 473928;
```

Đây là lý do surrogate key **không tự động thay thế business key về mặt nghiệp vụ**.

---

## 27. 인조식별자의 장점 — Ưu điểm

Ảnh cũng nói rõ:

> **시퀀스나 키 제약조건 등을 통해 주식별자를 생성할 수 있어 개발의 편의성이 향상된다.**
Có thể tạo primary identifier dễ dàng bằng sequence/key mechanism, giúp việc phát triển thuận tiện hơn.
> 

Ví dụ thay vì PK:

```
customer_id
+ product_id
+ date
+ version
```

rất dài, ta dùng:

```
ID
----
10001
10002
10003
```

Foreign key cũng đơn giản.

Thay vì child table phải giữ:

```
customer_id
product_id
date
version
```

có thể chỉ giữ:

```
parent_id
```

→ code dễ hơn
→ JOIN đơn giản hơn
→ FK nhỏ hơn
→ developer dễ quản lý hơn.

Ảnh tóm lại:

```
시간 ↓
비용 ↓
```

---

## 28. Nhưng tại sao ảnh nói “꼭 필요한 경우에만”?

> **개발 편의성을 높여주나 단점도 존재하니 꼭 필요한 경우에만 사용하는 것이 바람직하다.**
Surrogate identifier giúp phát triển thuận tiện nhưng cũng có nhược điểm, vì vậy cần dùng khi phù hợp chứ không phải cứ thấy composite key là thay ngay.
> 

Điểm thi quan trọng là:

```
인조식별자 = luôn tốt ❌

본질식별자 = luôn tốt ❌
```

Phải xem **business rule + uniqueness + query pattern + integrity + performance**.

---

## 29. Nối toàn bộ phần này với kiến thức Key trước đó

Bạn có thể ghép với cây Key đã học:

```
Super Key
│
└── Candidate Key
      │
      ├── Primary Key
      │
      └── Alternate Key
```

Nhưng:

```
본질식별자 / 인조식별자
```

là **một góc phân loại khác**.

Ví dụ:

```
EMPLOYEE

EMP_ID       ← surrogate
EMAIL        ← natural/business identifier
SSN          ← natural identifier
```

Có thể thiết kế:

```
PK = EMP_ID
UNIQUE = EMAIL
```

Vậy:

```
EMP_ID
→ 인조식별자
→ Primary Key

EMAIL
→ 본질식별자
→ Candidate Key / Alternate Key
```

Điểm này rất quan trọng: **Primary Key không đồng nghĩa với Natural Key.**

---

## 30. Bức tranh tổng thể của 5 ảnh

Bây giờ hãy nối chúng thành một logic duy nhất.

```
                DATABASE MODEL
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
   Transaction       NULL       Identifier
        │             │             │
        ↓             ↓             ↓
      ACID        Unknown      본질 / 인조
        │                           │
   ┌────┼────┐                      ├─ Natural
   ↓    ↓    ↓                      │
   A C  I    D                      └─ Surrogate
```

#### Transaction trả lời:

```
Một nghiệp vụ phải được xử lý như thế nào?
```

→ All or Nothing.

#### ACID trả lời:

```
Transaction phải đảm bảo những tính chất gì?
```

→ Atomicity / Consistency / Isolation / Durability.

#### NULL trả lời:

```
DB biểu diễn giá trị chưa biết/chưa có thế nào?
```

→ NULL.

#### Identifier trả lời:

```
Làm thế nào phân biệt từng instance/row?
```

→ Identifier.

#### Natural vs Surrogate trả lời:

```
Identifier đó đến từ nghiệp vụ
hay do hệ thống tạo?
```

→ 본질식별자 vs 인조식별자.

---

## ⭐ NOTE ÔN SQLD — Phần cần thuộc

```
[TRANSACTION]

트랜잭션
= 업무 처리를 위한 논리적 작업 단위
= Logical Unit of Work

Atomicity
= All or Nothing

Consistency
= DB의 일관성 유지

Isolation
= 다른 Transaction의 중간 결과 접근 제한

Durability
= COMMIT된 결과는 지속적으로 유지
```

```
[NULL]

NULL
≠ 0
≠ blank
= unknown / undefined / absence

NULL + number → NULL

NULL = NULL → UNKNOWN
NULL IS NULL → TRUE

COUNT(*)   → 모든 행
COUNT(col) → NULL 제외

SUM/AVG/MAX/MIN
→ NULL 제외

AVG(col)
= SUM(col) / COUNT(col)

전체 행을 기준으로 나누려면
= SUM(col) / COUNT(*)
```

```
[IDENTIFIER]

본질식별자
= 업무에서 자연스럽게 존재
= Natural / Business Identifier

인조식별자
= 시스템에서 인위적으로 생성
= Surrogate Identifier
= Sequence / Auto-generated ID 등
```

Và **một câu để nhớ toàn bộ phần 인조식별자**:

> **인조식별자는 PK를 단순하게 만들어 개발은 편리하지만, 업무적으로 유일해야 하는 값의 중복까지 자동으로 막아주는 것은 아니다.**
Surrogate key làm PK đơn giản và giúp phát triển thuận tiện, nhưng **không tự động bảo vệ tính duy nhất của business key**.
> 

Ví dụ điển hình:

```
PK = ORDER_DETAIL_ID

nhưng business rule:
(ORDER_ID, PRODUCT_ID) phải unique

→ cần UNIQUE(ORDER_ID, PRODUCT_ID)
  nếu nghiệp vụ thực sự yêu cầu không trùng.
```

Đây chính là mối liên hệ quan trọng nhất giữa **PK – 본질식별자 – 인조식별자 – UNIQUE – 데이터 무결성** mà đề SQLD có thể biến thành câu hỏi đánh lừa.

Mình sẽ tiếp tục đúng format học SQLD đã thống nhất: **bám sát nội dung ảnh → 1 ý tiếng Hàn + 1 ý tiếng Việt → giải thích keyword ngay tại chỗ → sau đó mở rộng phần dễ nhầm/dễ ra thi → cuối bài có `📌 NOTE 시험` để ôn nhanh.**
