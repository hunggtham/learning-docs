Tôi sẽ tiếp tục đúng format học SQLD trong project: **bám sát nội dung ảnh trước → mỗi ý tiếng Hàn đi kèm ngay một ý tiếng Việt → giải thích keyword → sau đó mới mở rộng và nối các khái niệm với nhau**. Phần ảnh này thực ra tạo thành một chuỗi kiến thức rất liền mạch:

**Transaction → ACID → NULL → 식별자 → 본질식별자/인조식별자.**

---

# 제3절 모델이 표현하는 트랜잭션의 이해

# Phần 3 — Hiểu Transaction được biểu diễn trong mô hình dữ liệu

## 1. 트랜잭션(Transaction)이란?

> **트랜잭션은 업무 처리를 위한 논리적인 작업 단위이다.**
> Transaction là **một đơn vị công việc logic để xử lý một nghiệp vụ**.

### Keyword: 트랜잭션 — Transaction — Giao dịch

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

Về mặt nghiệp vụ, đây là **một việc duy nhất**.

Nhưng DB phải thực hiện nhiều bước:

```text
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

```text
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

# 2. 트랜잭션은 모두 성공하거나 모두 취소되어야 한다

> **하나의 트랜잭션에 속한 동작들은 모두 성공하거나, 모두 취소(UNDO)되어야 한다.**
> Các thao tác thuộc cùng một transaction phải **hoặc thành công toàn bộ, hoặc bị hủy toàn bộ**.

Đây chính là:

## All or Nothing

Ví dụ A có:

```text
A = 5,000,000
B = 2,000,000
```

Chuyển 1 triệu:

```text
A: 5M → 4M
B: 2M → 3M
```

Đúng.

Nhưng giả sử:

```text
① A -1M     SUCCESS
② B +1M     ERROR
```

DB không được để:

```text
A = 4M
B = 2M
```

vì 1 triệu đã "biến mất".

Ngược lại cũng không được:

```text
A = 5M
B = 3M
```

vì tiền tự nhiên xuất hiện.

Vì vậy:

```text
① A -1M
② B +1M
      │
      ├── tất cả SUCCESS → COMMIT
      │
      └── có lỗi         → ROLLBACK
```

### COMMIT

> **COMMIT은 트랜잭션의 변경사항을 확정한다.**
> COMMIT xác nhận và làm cho các thay đổi của transaction được hoàn tất.

### ROLLBACK

> **ROLLBACK은 트랜잭션에서 발생한 변경사항을 취소한다.**
> ROLLBACK hủy các thay đổi xảy ra trong transaction.

Đây là ý trong ảnh:

> **부분 COMMIT 불가, 동시 COMMIT이나 ROLLBACK으로 처리**
> Không được commit từng phần; toàn bộ nghiệp vụ phải được xử lý thống nhất bằng COMMIT hoặc ROLLBACK.

---

# 3. 왜 ERD에서 트랜잭션이 중요한가?

# Tại sao Transaction lại liên quan đến ERD?

Đây là đoạn rất dễ đọc qua nhưng lại quan trọng trong SQLD.

> **두 엔터티의 관계가 서로 필수적일 때 하나의 트랜잭션을 형성한다.**
> Khi quan hệ giữa hai entity mang tính bắt buộc với nhau trong nghiệp vụ, chúng có xu hướng cùng tham gia một transaction.

Ví dụ:

```text
고객 ───── 주문
Customer    Order
```

Nếu nghiệp vụ yêu cầu một `주문` phải gắn với một `고객`, thì quan hệ đó mang tính bắt buộc ở phía tương ứng.

Ngược lại:

> **두 엔터티가 서로 독립적인 수행이 가능하다면 선택적 관계로 표현한다.**
> Nếu nghiệp vụ của hai entity có thể diễn ra độc lập thì quan hệ có thể được biểu diễn dưới dạng optional.

---

# 4. 필수적 관계 vs 선택적 관계

## 필수적 관계 — Mandatory Relationship

> **관계가 반드시 존재해야 한다.**
> Quan hệ bắt buộc phải tồn tại.

Ví dụ:

```text
주문 → 고객
Order → Customer
```

Nếu quy tắc nghiệp vụ nói:

> 주문은 반드시 고객에게 속한다.
> Mỗi đơn hàng bắt buộc phải thuộc về một khách hàng.

thì phía đó là mandatory.

---

## 선택적 관계 — Optional Relationship

> **관계가 없어도 엔터티 인스턴스가 존재할 수 있다.**
> Một instance của entity vẫn có thể tồn tại dù chưa có quan hệ đó.

Ví dụ:

```text
고객
Pham
```

Pham vừa đăng ký tài khoản nhưng chưa từng đặt hàng.

Vậy:

```text
Customer → Order

0..N
```

Một customer có thể có:

```text
0 order
1 order
N orders
```

---

# 5. IE와 Barker 표기법

Ảnh của bạn nhấn mạnh sự khác nhau về ký hiệu.

### IE 표기법

> **필수적 관계: 원 X**
> Quan hệ bắt buộc: không có vòng tròn.

> **선택적 관계: 원 O**
> Quan hệ optional: có vòng tròn `○`.

Có thể nhớ:

```text
○ = zero allowed
```

Có vòng tròn nghĩa là:

```text
0개도 가능
0 cũng được
→ optional
```

### Barker 표기법

> **필수적 관계: 실선의 관계선**
> Mandatory → đường liền.

> **선택적 관계: 점선의 관계선**
> Optional → đường đứt.

Mẹo thi:

```text
IE
○ → Optional

Barker
------  solid  → Mandatory
- - - - dashed → Optional
```

---

# 6. 트랜잭션의 특징 — ACID

Ảnh tiếp theo đưa ra 4 thuộc tính cực kỳ quan trọng:

```text
A → Atomicity
C → Consistency
I → Isolation
D → Durability
```

Đây chính là **ACID**.

---

## ① 원자성 Atomicity — Tính nguyên tử

> **트랜잭션은 더 이상 분해가 불가능한 업무의 최소단위이다.**
> Transaction được xem là đơn vị nghiệp vụ nhỏ nhất không thể chia nhỏ thêm khi xét tính hoàn thành.

> **전부 처리되거나 모두 처리되지 않아야 한다.**
> Hoặc toàn bộ được thực hiện, hoặc toàn bộ không được thực hiện.

Chính là:

```text
ALL OR NOTHING
```

Ví dụ:

```text
A - 1M
B + 1M
```

Không được:

```text
A -1M ✓
B +1M ✗
```

Mà phải:

```text
✓ ✓ → COMMIT

hoặc

✗ → ROLLBACK toàn bộ
```

### Keyword nhớ nhanh

```text
Atomicity
= 원자성
= All or Nothing
= COMMIT / ROLLBACK
```

---

# 7. ② 일관성 Consistency — Tính nhất quán

> **트랜잭션이 성공적으로 완료된 후에도 DB는 일관된 상태여야 한다.**
> Sau khi transaction hoàn tất thành công, database vẫn phải ở trạng thái nhất quán.

Điểm cốt lõi:

```text
DB hợp lệ
   ↓
Transaction
   ↓
DB vẫn hợp lệ
```

Ví dụ trước chuyển tiền:

```text
A = 5M
B = 2M

Total = 7M
```

Sau:

```text
A = 4M
B = 3M

Total = 7M
```

Các ràng buộc nghiệp vụ vẫn đúng.

Consistency không chỉ là tiền. Nó còn liên quan tới:

```text
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

```text
balance = -1,000,000
```

trong khi hệ thống cấm số dư âm, thì trạng thái DB không còn thỏa quy tắc.

### Nhớ:

```text
Consistency
= trước hợp lệ
→ transaction
→ sau vẫn hợp lệ
```

---

# 8. ③ 격리성 Isolation — Tính cô lập

> **실행 중인 트랜잭션의 중간결과를 다른 트랜잭션이 접근할 수 없다.**
> Transaction khác không được tùy ý nhìn thấy/kế thừa trạng thái trung gian chưa hoàn tất của transaction đang chạy.

Giả sử:

```text
Transaction A

UPDATE balance - 1M
...
chưa COMMIT
```

Transaction B không nên dựa vào trạng thái chưa hoàn tất đó như thể nó đã được xác nhận.

Có thể hình dung:

```text
T1: A -1M ---------------- COMMIT
         ↑
         │ trạng thái trung gian
         │
T2: không nên nhìn nó như dữ liệu đã hoàn tất
```

Đây là lý do xuất hiện các vấn đề concurrency như:

```text
Dirty Read
Non-repeatable Read
Phantom Read
```

và các mức:

```text
READ UNCOMMITTED
READ COMMITTED
REPEATABLE READ
SERIALIZABLE
```

SQLD ở đoạn này chủ yếu cần nhớ bản chất:

> **Isolation = các transaction đang chạy phải được cách ly thích hợp với nhau.**

---

# 9. ④ 영속성 / 지속성 Durability — Tính bền vững

> **트랜잭션이 성공적으로 완료되면 결과는 데이터베이스에 영속적으로 저장된다.**
> Khi transaction đã hoàn tất thành công, kết quả phải được lưu bền vững trong database.

Tức là:

```text
COMMIT 완료
    ↓
결과 유지
```

Ví dụ bạn chuyển tiền thành công.

Sau đó:

```text
server restart
```

thì không được quay lại:

```text
A = 5M
B = 2M
```

mà phải giữ:

```text
A = 4M
B = 3M
```

---

# ⭐ Tổng hợp ACID cực dễ nhớ

| Korean | English     | Ý chính                                                    |
| ------ | ----------- | ---------------------------------------------------------- |
| 원자성    | Atomicity   | All or Nothing                                             |
| 일관성    | Consistency | Trước/sau đều hợp lệ                                       |
| 격리성    | Isolation   | Transaction không can thiệp trạng thái trung gian của nhau |
| 영속성    | Durability  | COMMIT rồi thì phải được giữ                               |

Nhớ chuỗi:

```text
Atomicity   → Có làm hết không?
Consistency → Kết quả có hợp lệ không?
Isolation   → Transaction khác có gây/nhìn thấy ảnh hưởng trung gian không?
Durability  → Commit rồi có giữ được không?
```

---

# 제4절 NULL 속성의 이해

# Phần 4 — NULL

Đây là phần **rất dễ bị gài trong SQLD**.

## 10. NULL là gì?

> **NULL은 아직 정의되지 않은 값이다.**
> NULL là giá trị **chưa được xác định / không biết / không tồn tại theo ngữ cảnh**, chứ không phải một giá trị thông thường.

Trong ảnh:

> **NULL은 0 또는 공백과 다르다.**
> NULL khác `0` và khác chuỗi rỗng/khoảng trắng.

Đây là điểm bắt buộc phải nhớ:

```text
NULL ≠ 0
NULL ≠ ' '
```

Về mặt khái niệm:

```text
0
→ biết giá trị
→ giá trị chính xác là zero

NULL
→ không biết/chưa có giá trị
```

Ví dụ:

```text
나이 = 0
```

nghĩa là biết tuổi bằng 0.

Nhưng:

```text
나이 = NULL
```

nghĩa là:

> Không biết tuổi / chưa nhập tuổi.

---

# 11. NULL trong phép toán

> **NULL 값을 포함하는 연산의 결과값도 NULL 값이다.**
> Phép toán có NULL thường cho kết quả NULL.

Ví dụ:

```sql
10 + NULL
```

→

```text
NULL
```

Tại sao?

Bởi vì:

```text
10 + một giá trị không biết
```

thì kết quả cũng:

```text
không biết
```

Tương tự:

```text
NULL + 100 → NULL
NULL - 10  → NULL
NULL * 2   → NULL
```

---

# 12. NVL và ISNULL

Trong Oracle:

```sql
NVL(column, replacement)
```

Ví dụ:

```sql
NVL(C, 0)
```

> **컬럼 C의 NULL 값을 0으로 치환한다.**
> Thay NULL trong cột C bằng 0.

Ví dụ:

```text
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

```text
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

# 13. NULL không được so sánh bằng =

Đây là câu cực quan trọng trong ảnh:

> **NULL과의 모든 비교(IS NULL 제외)는 알 수 없음(UNKNOWN)을 반환한다.**
> Các phép so sánh thông thường với NULL trả về UNKNOWN, ngoại trừ kiểm tra `IS NULL`/`IS NOT NULL`.

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

## Tại sao `NULL = NULL` không phải TRUE?

Vì NULL nghĩa là:

```text
unknown
```

Ví dụ:

```text
A = NULL
B = NULL
```

Bạn không biết A.

Bạn cũng không biết B.

Không có nghĩa:

```text
A = B
```

Ví dụ thực tế:

```text
A tuổi = không biết
B tuổi = không biết
```

Không thể kết luận:

```text
A và B bằng tuổi nhau
```

Do đó:

```sql
NULL = NULL
```

không trả về `TRUE`.

Trong logic SQL:

```text
TRUE
FALSE
UNKNOWN
```

được gọi là **Three-Valued Logic — 3VL**.

---

# 14. NULL trong Aggregate Function

Ảnh có bảng:

```text
컬럼1    컬럼2
10       20
20       NULL
```

Hãy tính.

### COUNT(column)

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
> COUNT(column) bỏ qua NULL.

---

### SUM

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

### AVG

Đây là chỗ cực dễ sai.

```sql
AVG(column2)
```

không phải:

```text
(20 + 0) / 2
= 10 ❌
```

Mà là:

```text
20 / 1
= 20 ✓
```

Vì:

> **집계 함수에서 NULL은 0이 아니라 계산 대상에서 제외된다.**
> Trong aggregate function, NULL không được xem là 0 mà bị loại khỏi tập tính toán.

---

# 15. COUNT(*) khác COUNT(column)

```sql
COUNT(*)
```

> **NULL 여부와 관계없이 행 자체를 센다.**
> Đếm số dòng, bất kể trong dòng có NULL hay không.

Trong bảng:

```text
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

```text
column2 = NULL
```

Do đó:

```text
COUNT(*)       → đếm ROW
COUNT(column)  → đếm NON-NULL
```

### ⭐ Đây là một công thức SQLD rất đáng nhớ

```text
COUNT(*) = 모든 행
COUNT(col) = NULL 제외
```

---

# 16. Nếu column là PK?

Ảnh ghi:

> **컬럼이 PK라면 NULL값 허용 X → 항상 COUNT(*) = COUNT(컬럼)**
> Nếu column là PK thì không cho phép NULL, vì vậy COUNT(*) luôn bằng COUNT(column) trên bảng đó.

Vì:

```text
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

# 17. Trung bình trên toàn bộ số dòng

Ảnh nhấn mạnh:

```text
전체 행 개수에 대한 평균
= SUM(column) / COUNT(*)
```

Khác với:

```sql
AVG(column)
```

Ví dụ:

```text
20
NULL
```

### AVG(column)

```text
20 / 1
= 20
```

### SUM(column)/COUNT(*)

```text
20 / 2
= 10
```

Hai kết quả hoàn toàn khác nhau.

Đây là dạng bẫy SQLD rất phổ biến.

---

# 18. NULL의 ERD 표기법

Ảnh nói:

### IE

> **NULL 허용 여부 알 수 없음**
> Không thể xác định trực tiếp việc attribute có cho phép NULL hay không từ cách biểu diễn attribute như trong hình.

### Barker

> **속성 앞 동그라미 표시**
> Dùng ký hiệu trước thuộc tính để biểu diễn tính optional.

Trong hình Barker:

```text
# 주문번호
○ 주문금액
○ 주문취소금액
```

Trong đó `#` liên quan đến identifier/key, còn `○` biểu thị thuộc tính optional.

---

# 제5절 본질식별자 vs 인조식별자

Đây là phần tiếp nối trực tiếp kiến thức `식별자` bạn vừa học trước đó.

# 19. 본질식별자 — Natural/Original Identifier

Ảnh dùng:

> **원조(본질) 식별자**
> Identifier được hình thành tự nhiên từ nghiệp vụ và cần thiết cho việc phân biệt dữ liệu.

Ví dụ:

```text
학번
주민등록번호
사번
```

Tức là bản thân nghiệp vụ đã có nó.

Ví dụ:

```text
학생

학번
----
20260001
20260002
```

Không phải vì DB cần PK nên ta mới nghĩ ra `학번`; nó vốn có ý nghĩa trong nghiệp vụ trường học.

Có thể liên hệ với thuật ngữ phổ biến:

```text
본질식별자
≈ Natural Key / Business Key
```

---

# 20. 인조식별자 — Surrogate Key

> **업무에는 존재하지 않지만 편의성을 위해 인위적으로 만든 식별자이다.**
> Là identifier không tồn tại tự nhiên trong nghiệp vụ nhưng được tạo nhân tạo để thuận tiện cho hệ thống.

Ví dụ:

```text
ORDER_DETAIL_ID
USER_ID
SEQ
AUTO_INCREMENT
IDENTITY
```

Ví dụ:

```text
주문상세번호
-------------
1
2
3
4
```

`주문상세번호` có thể chẳng có ý nghĩa gì với khách hàng.

Nó chỉ giúp DB nói:

```text
đây là row #1
đây là row #2
```

Đó chính là:

```text
Surrogate Key
= 인조식별자
```

---

# 21. Tại sao cần 인조식별자?

Ảnh đưa ra ví dụ rất hay.

Ban đầu `주문이력` dùng:

```text
PK = 주문번호 + 상품번호
```

Tức composite PK:

```text
ORDER_ID + PRODUCT_ID
```

Ví dụ:

```text
101 + c03
101 + c05
101 + c06
```

Đều khác nhau → OK.

Nhưng vài giờ sau khách thêm lại `c03`:

```text
101 + c03
```

Ta có:

```text
101 c03 ← lần đầu
101 c05
101 c06
101 c03 ← lần sau
```

PK:

```text
(101, c03)
```

bị trùng.

→ `PRIMARY KEY violation`.

---

# 22. Giải pháp: 주문상세번호

Ta thêm:

```text
주문상세번호
Order Detail ID
```

Ví dụ:

```text
주문상세번호 | 주문번호 | 상품번호
---------------------------------
1            101       c03
2            101       c05
3            101       c06
4            101       c03
```

Bây giờ:

```text
PK = 주문상세번호
```

nên:

```text
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

```text
1
2
3
4
...
```

---

# 23. Nhưng 인조식별자 tạo ra một vấn đề lớn

Đây là phần ảnh muốn bạn đặc biệt chú ý.

Khi:

```text
PK = 주문상세번호
```

thì DB chỉ kiểm tra:

```text
주문상세번호 unique?
```

Ví dụ:

```text
ID | ORDER | PRODUCT
--------------------
1  | 101   | c03
2  | 101   | c05
3  | 101   | c06
4  | 101   | c03
```

Về PK:

```text
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
> Nếu chỉ dựa vào surrogate identifier làm primary identifier thì có thể không ngăn được duplicate theo business key.

---

# 24. Đây chính là nhược điểm quan trọng của 인조식별자

Ảnh liệt kê:

> **중복 데이터 발생 가능성 → 데이터 품질 저하**
> Có khả năng phát sinh dữ liệu trùng → giảm chất lượng dữ liệu.

Ví dụ:

```text
ID | ORDER | PRODUCT
1  | 101   | C03
2  | 101   | C03
```

PK vẫn:

```text
1 ≠ 2
```

→ DB nói OK.

Nhưng nghiệp vụ có thể nói:

```text
101 + C03
```

không được duplicate.

Vậy cần thêm:

```sql
UNIQUE (ORDER_ID, PRODUCT_ID)
```

nếu business rule yêu cầu uniqueness.

---

# 25. 인조식별자 có thể làm tăng Index

Ảnh nói:

> **불필요한 인덱스 생성 → 저장 공간 낭비 및 DML 성능 저하**
> Có thể phát sinh index bổ sung không cần thiết → tốn storage và giảm hiệu năng DML.

Ví dụ:

```text
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

```text
(ORDER_ID, PRODUCT_ID)
```

Kết quả:

```text
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

# 26. Một vấn đề khác: Query vẫn phải dùng business columns

Ảnh nói rất đúng:

> **검색할 때 결국 주문번호와 상품번호를 기반으로 WHERE절을 작성하게 된다.**
> Khi tìm kiếm dữ liệu, cuối cùng ta vẫn thường viết WHERE dựa trên 주문번호 và 상품번호.

Ví dụ người dùng không biết:

```text
ORDER_DETAIL_ID = 473928
```

Họ biết:

```text
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

# 27. 인조식별자의 장점 — Ưu điểm

Ảnh cũng nói rõ:

> **시퀀스나 키 제약조건 등을 통해 주식별자를 생성할 수 있어 개발의 편의성이 향상된다.**
> Có thể tạo primary identifier dễ dàng bằng sequence/key mechanism, giúp việc phát triển thuận tiện hơn.

Ví dụ thay vì PK:

```text
customer_id
+ product_id
+ date
+ version
```

rất dài, ta dùng:

```text
ID
----
10001
10002
10003
```

Foreign key cũng đơn giản.

Thay vì child table phải giữ:

```text
customer_id
product_id
date
version
```

có thể chỉ giữ:

```text
parent_id
```

→ code dễ hơn
→ JOIN đơn giản hơn
→ FK nhỏ hơn
→ developer dễ quản lý hơn.

Ảnh tóm lại:

```text
시간 ↓
비용 ↓
```

---

# 28. Nhưng tại sao ảnh nói "꼭 필요한 경우에만"?

> **개발 편의성을 높여주나 단점도 존재하니 꼭 필요한 경우에만 사용하는 것이 바람직하다.**
> Surrogate identifier giúp phát triển thuận tiện nhưng cũng có nhược điểm, vì vậy cần dùng khi phù hợp chứ không phải cứ thấy composite key là thay ngay.

Điểm thi quan trọng là:

```text
인조식별자 = luôn tốt ❌

본질식별자 = luôn tốt ❌
```

Phải xem **business rule + uniqueness + query pattern + integrity + performance**.

---

# 29. Nối toàn bộ phần này với kiến thức Key trước đó

Bạn có thể ghép với cây Key đã học:

```text
Super Key
│
└── Candidate Key
      │
      ├── Primary Key
      │
      └── Alternate Key
```

Nhưng:

```text
본질식별자 / 인조식별자
```

là **một góc phân loại khác**.

Ví dụ:

```text
EMPLOYEE

EMP_ID       ← surrogate
EMAIL        ← natural/business identifier
SSN          ← natural identifier
```

Có thể thiết kế:

```text
PK = EMP_ID
UNIQUE = EMAIL
```

Vậy:

```text
EMP_ID
→ 인조식별자
→ Primary Key

EMAIL
→ 본질식별자
→ Candidate Key / Alternate Key
```

Điểm này rất quan trọng: **Primary Key không đồng nghĩa với Natural Key.**

---

# 30. Bức tranh tổng thể của 5 ảnh

Bây giờ hãy nối chúng thành một logic duy nhất.

```text
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

### Transaction trả lời:

```text
Một nghiệp vụ phải được xử lý như thế nào?
```

→ All or Nothing.

### ACID trả lời:

```text
Transaction phải đảm bảo những tính chất gì?
```

→ Atomicity / Consistency / Isolation / Durability.

### NULL trả lời:

```text
DB biểu diễn giá trị chưa biết/chưa có thế nào?
```

→ NULL.

### Identifier trả lời:

```text
Làm thế nào phân biệt từng instance/row?
```

→ Identifier.

### Natural vs Surrogate trả lời:

```text
Identifier đó đến từ nghiệp vụ
hay do hệ thống tạo?
```

→ 본질식별자 vs 인조식별자.

---

# ⭐ NOTE ÔN SQLD — Phần cần thuộc

```text
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

```text
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

```text
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
> Surrogate key làm PK đơn giản và giúp phát triển thuận tiện, nhưng **không tự động bảo vệ tính duy nhất của business key**.

Ví dụ điển hình:

```text
PK = ORDER_DETAIL_ID

nhưng business rule:
(ORDER_ID, PRODUCT_ID) phải unique

→ cần UNIQUE(ORDER_ID, PRODUCT_ID)
  nếu nghiệp vụ thực sự yêu cầu không trùng.
```

Đây chính là mối liên hệ quan trọng nhất giữa **PK – 본질식별자 – 인조식별자 – UNIQUE – 데이터 무결성** mà đề SQLD có thể biến thành câu hỏi đánh lừa.
