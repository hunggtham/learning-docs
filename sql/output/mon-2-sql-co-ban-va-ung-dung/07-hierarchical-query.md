# Hierarchical Query

> **Mục tiêu:** START WITH, CONNECT BY PRIOR, LEVEL, NOCYCLE và các pseudocolumn phân cấp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

## 1. 계층형 질의 — Hierarchical Query là gì?

**KR:** 계층형 질의는 상위-하위 관계를 가진 데이터를 계층 구조로 조회하기 위한 질의이다.
**VI:** Hierarchical Query là truy vấn dùng để lấy dữ liệu có quan hệ **cha–con / trên–dưới** theo dạng cây.

Ví dụ trong ảnh:

```text
        A
       / \
      B   C
         / \
        D   E
```

Bảng dữ liệu có thể lưu như sau:

| 사원 | 관리자  |
| -- | ---- |
| A  | NULL |
| B  | A    |
| C  | A    |
| D  | C    |
| E  | C    |

Ý nghĩa:

```text
A là quản lý của B
A là quản lý của C
C là quản lý của D
C là quản lý của E
```

Dù dữ liệu nằm trong **một table**, giữa các row lại có quan hệ với nhau.

---

## 2. 순환관계 데이터 모델 — Recursive Relationship

**KR:** 하나의 엔터티 안에서 자기 자신과 관계를 맺는 것을 순환 관계라고 한다.
**VI:** Khi một entity/table có quan hệ với chính các row khác trong cùng entity đó, ta gọi là **recursive relationship / self-referencing relationship**.

Ví dụ:

```text
EMPLOYEE
- EMP_ID
- NAME
- MGR_ID
```

`MGR_ID` tham chiếu lại:

```text
EMPLOYEE.EMP_ID
```

Nên:

```text
EMP_ID 100 = nhân viên
MGR_ID 200 = quản lý của nhân viên đó
```

Các ví dụ điển hình:

```text
조직 → tổ chức
사원 → nhân viên
메뉴 → menu cha/con
부서 → phòng ban
카테고리 → category
```

---

## 3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐

```sql
SELECT ...
FROM ...
START WITH 시작조건
CONNECT BY [NOCYCLE] PRIOR 연결조건;
```

Hai phần quan trọng nhất:

```text
START WITH
CONNECT BY PRIOR
```

---

## 4. START WITH

**KR:** `START WITH`는 계층 탐색을 시작할 루트 노드를 지정한다.
**VI:** `START WITH` xác định **node bắt đầu / root node**.

Ví dụ:

```sql
START WITH PDEPT IS NULL
```

Nghĩa là:

> bắt đầu từ row không có phòng ban cha.

Nếu:

```text
DCODE  DNAME      PDEPT
0001   사장실       NULL
1000   경영지원부    0001
1001   재무관리      1000
```

thì:

```text
PDEPT IS NULL
```

chọn:

```text
0001 사장실
```

làm root.

---

## 5. Root luôn có LEVEL = 1

**KR:** 루트 노드는 LEVEL 값으로 1을 가진다.
**VI:** Root node luôn có:

```text
LEVEL = 1
```

Con trực tiếp:

```text
LEVEL = 2
```

cháu:

```text
LEVEL = 3
```

Ví dụ:

```text
사장실        LEVEL 1
├─ 경영지원부 LEVEL 2
│  ├─ 재무관리 LEVEL 3
│  └─ 총무     LEVEL 3
└─ 기술부     LEVEL 2
   ├─ H/W지원 LEVEL 3
   └─ S/W지원 LEVEL 3
```

---

## 6. CONNECT BY PRIOR ⭐⭐⭐

Đây là phần khó nhất.

**KR:** `CONNECT BY PRIOR`는 현재 행과 다음 계층 행을 어떻게 연결할지를 정의한다.
**VI:** `CONNECT BY PRIOR` xác định cách **nối row hiện tại với row ở level kế tiếp**.

Ví dụ trong ảnh:

```sql
CONNECT BY PRIOR DCODE = PDEPT
```

Ta có:

```text
DCODE = mã phòng hiện tại
PDEPT = mã phòng cha
```

Đọc:

> DCODE của row trước/cha = PDEPT của row tiếp theo/con.

---

## 7. PRIOR nghĩa chính xác là gì?

`PRIOR` không đơn giản là "cha".

Nó có nghĩa:

> **giá trị của row ở level trước trong quá trình hierarchical traversal**.

Ví dụ:

```sql
CONNECT BY PRIOR DCODE = PDEPT
```

Nếu current parent là:

```text
DCODE = 0001
```

Oracle tìm row sao cho:

```text
PDEPT = 0001
```

Ta có:

```text
1000 경영지원부
1003 기술부
```

Sau đó với:

```text
DCODE = 1000
```

Oracle tìm:

```text
PDEPT = 1000
```

→

```text
1001 재무관리
1002 총무
```

---

## 8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐

Với:

```sql
CONNECT BY PRIOR A = B
```

hãy đọc:

```text
A của row trước
=
B của row tiếp theo
```

Hay:

```text
PRIOR A
→ giữ A của current/parent
→ tìm row mới có B bằng nó
```

Đây là cách an toàn hơn việc học thuộc "PRIOR cha" hoặc "PRIOR con".

---

## 9. Ví dụ chuẩn trong ảnh

```sql
SELECT *, LEVEL
FROM DEPT
START WITH PDEPT IS NULL
CONNECT BY PRIOR DCODE = PDEPT;
```

Dữ liệu:

```text
DCODE  DNAME      PDEPT
0001   사장실       NULL
1000   경영지원부    0001
1001   재무관리      1000
1002   총무          1000
1003   기술부        0001
1004   H/W지원       1003
1005   S/W지원       1003
```

Quá trình:

```text
START:
0001

0001.DCODE
↓
find PDEPT=0001
↓
1000, 1003

1000.DCODE
↓
find PDEPT=1000
↓
1001,1002

1003.DCODE
↓
find PDEPT=1003
↓
1004,1005
```

Kết quả:

```text
0001 LEVEL 1
1000 LEVEL 2
1001 LEVEL 3
1002 LEVEL 3
1003 LEVEL 2
1004 LEVEL 3
1005 LEVEL 3
```

---

## 10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐

Ảnh đưa ví dụ sai:

```sql
CONNECT BY DCODE = PRIOR PDEPT;
```

Bắt đầu:

```text
사장실
DCODE = 0001
PDEPT = NULL
```

Vì `PRIOR PDEPT` là:

```text
NULL
```

Oracle cần tìm row có:

```text
DCODE = NULL
```

không tồn tại.

Vì vậy traversal dừng ngay.

Chỉ còn root:

```text
0001 사장실 LEVEL 1
```

---

## 11. Hướng duyệt xuôi và ngược

Đây là phần cần hiểu thay vì thuộc máy móc.

### Parent → Child

Ví dụ:

```sql
CONNECT BY PRIOR DCODE = PDEPT
```

Nếu:

```text
DCODE = key của node
PDEPT = parent key
```

thì đây là:

```text
parent → child
```

vì lấy `DCODE` của parent để tìm `PDEPT` của child.

---

### Child → Parent

Nếu muốn đi ngược:

```sql
CONNECT BY PRIOR PDEPT = DCODE
```

ta lấy parent-code đang lưu trong row hiện tại rồi tìm row có `DCODE` đó.

→ đi:

```text
child → parent
```

#### Công thức dễ nhớ

Với dữ liệu:

```text
ID
PARENT_ID
```

Xuôi:

```sql
PRIOR ID = PARENT_ID
```

Ngược:

```sql
PRIOR PARENT_ID = ID
```

---

## 12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐

Ảnh đưa hai query.

### Điều kiện nằm trong CONNECT BY

```sql
SELECT *
FROM DEPT
START WITH PDEPT IS NULL
CONNECT BY PRIOR DCODE = PDEPT
       AND AREA = '서울지사';
```

Ở đây:

```text
AREA='서울지사'
```

là **điều kiện dùng trong quá trình tìm node tiếp theo**.

Root:

```text
사장실
AREA = 포항본사
```

vẫn có thể được chọn bởi:

```sql
START WITH PDEPT IS NULL
```

sau đó CONNECT BY chỉ tìm các child thỏa:

```text
AREA = 서울지사
```

Nên root vẫn xuất hiện.

---

## 13. Nếu AREA nằm trong WHERE

```sql
SELECT *, LEVEL
FROM DEPT
WHERE AREA = '서울지사'
START WITH PDEPT IS NULL
CONNECT BY PRIOR DCODE = PDEPT;
```

Oracle trước hết tạo cây hierarchical theo:

```text
START WITH
CONNECT BY
```

sau đó `WHERE` lọc kết quả row.

Do root:

```text
사장실
AREA = 포항본사
```

không thỏa:

```text
AREA='서울지사'
```

→ bị loại khỏi kết quả.

---

## 14. Thứ tự xử lý quan trọng ⭐⭐⭐

Trong ngữ cảnh Hierarchical Query, cần nhớ:

```text
START WITH
+
CONNECT BY
→ tạo hierarchy

sau đó
WHERE
→ filter các row đã tạo
```

Nên:

> **Điều kiện ở CONNECT BY ảnh hưởng việc cây được mở rộng như thế nào.**

> **Điều kiện ở WHERE chủ yếu lọc kết quả sau khi hierarchy đã được triển khai.**

Đây là bẫy rất hay xuất hiện.

---

## 15. NOCYCLE ⭐⭐⭐

Nếu dữ liệu có cycle:

```text
A → B
B → A
```

thì có thể:

```text
A
↓
B
↓
A
↓
B
↓
...
```

Nếu không xử lý, Oracle phát hiện loop và báo lỗi.

---

## 16. Ví dụ cycle trong ảnh

```text
EMP_ID   MGR_ID

1000     2000
2000     1000
```

Nghĩa là:

```text
1000 → manager 2000
2000 → manager 1000
```

Cycle:

```text
1000
↓
2000
↓
1000
↓
2000
...
```

Query:

```sql
CONNECT BY PRIOR EMP_ID = MGR_ID
```

không có `NOCYCLE`

→ lỗi.

---

## 17. NOCYCLE

Dùng:

```sql
CONNECT BY NOCYCLE PRIOR EMP_ID = MGR_ID
```

**KR:** `NOCYCLE`은 순환 구조가 존재하더라도 오류 없이 탐색을 종료하도록 한다.
**VI:** `NOCYCLE` cho phép Oracle xử lý dữ liệu có cycle mà không tiếp tục loop vô hạn.

Nó không có nghĩa:

> sửa dữ liệu cycle.

Nó chỉ có nghĩa:

> khi phát hiện cycle, không tiếp tục traversal theo vòng đó.

---

## 18. LEVEL ⭐⭐⭐

`LEVEL` là pseudocolumn của hierarchical query.

```sql
SELECT LEVEL, ...
```

Ý nghĩa:

```text
root        → 1
child       → 2
grandchild  → 3
...
```

Ví dụ:

```text
A  1
B  2
C  2
D  3
E  3
```

---

## 19. CONNECT_BY_ISLEAF

**KR:** `CONNECT_BY_ISLEAF`는 현재 행이 리프 노드이면 1, 아니면 0을 반환한다.
**VI:** `CONNECT_BY_ISLEAF` trả:

```text
1 → leaf node
0 → không phải leaf
```

**Leaf node** = node không còn child.

Ví dụ:

```text
        A
       / \
      B   C
         / \
        D   E
```

Kết quả:

```text
A → 0
B → 1
C → 0
D → 1
E → 1
```

---

## 20. CONNECT_BY_ROOT ⭐⭐⭐

**KR:** `CONNECT_BY_ROOT`는 현재 행이 속한 계층의 루트 값을 반환한다.
**VI:** `CONNECT_BY_ROOT` trả giá trị của **root node** ứng với row hiện tại.

Ví dụ:

```sql
SELECT CONNECT_BY_ROOT 사원 AS 루트사원,
       사원
FROM 사원
START WITH 관리자 IS NULL
CONNECT BY PRIOR 사원 = 관리자;
```

Tree:

```text
A
├─ B
└─ C
   └─ D
```

thì:

```text
현재행  ROOT
A       A
B       A
C       A
D       A
```

---

## 21. SYS_CONNECT_BY_PATH ⭐⭐⭐

```sql
SYS_CONNECT_BY_PATH(column, delimiter)
```

**KR:** 루트부터 현재 행까지의 경로를 문자열로 표시한다.
**VI:** Hàm này tạo **đường dẫn từ root tới current row** thành string.

Ví dụ:

```sql
SYS_CONNECT_BY_PATH(사원, '/')
```

Tree:

```text
A
├─ B
└─ C
   └─ D
```

kết quả:

```text
A → /A
B → /A/B
C → /A/C
D → /A/C/D
```

Rất dễ nhớ:

> giống path thư mục.

```text
/root/folder/file
```

---

## 22. Ví dụ kết hợp CONNECT_BY_ROOT + PATH

Ảnh:

```sql
SELECT CONNECT_BY_ROOT 사원 AS 루트사원,
       SYS_CONNECT_BY_PATH(사원, '/') AS 경로,
       사원,
       관리자
FROM 사원
START WITH 관리자 IS NULL
CONNECT BY PRIOR 사원 = 관리자;
```

Kết quả:

| Root | Path     | Employee | Manager |
| ---- | -------- | -------- | ------- |
| A    | `/A`     | A        | NULL    |
| A    | `/A/B`   | B        | A       |
| A    | `/A/C`   | C        | A       |
| A    | `/A/C/D` | D        | C       |

Hai hàm trả lời hai câu khác nhau:

```text
CONNECT_BY_ROOT
→ root là ai?

SYS_CONNECT_BY_PATH
→ đi qua đường nào từ root đến đây?
```

---

## 23. ORDER SIBLINGS BY

**KR:** `ORDER SIBLINGS BY`는 같은 부모를 가진 형제 노드들 사이의 순서를 정렬한다.
**VI:** `ORDER SIBLINGS BY` dùng để sort **các node cùng cha**, nhưng vẫn giữ cấu trúc hierarchy.

Ví dụ:

```text
A
├─ C
├─ B
└─ D
```

Nếu:

```sql
ORDER SIBLINGS BY NAME
```

có thể thành:

```text
A
├─ B
├─ C
└─ D
```

Nhưng không phá cấu trúc:

```text
parent
→ child
```

---

## 24. Vì sao không dùng ORDER BY bình thường?

`ORDER BY` thông thường có thể sort toàn bộ result set và làm hierarchy khó nhìn.

Trong hierarchical query, nếu mục tiêu là:

> sort các anh em cùng level/cùng parent

thì:

```sql
ORDER SIBLINGS BY ...
```

phù hợp hơn.

Keyword:

```text
SIBLING = 형제 = anh em
```

---

## 25. CONNECT_BY_ISCYCLE ⭐⭐⭐

**KR:** `CONNECT_BY_ISCYCLE`은 현재 행에서 순환이 발생하는지 표시한다.
**VI:** `CONNECT_BY_ISCYCLE` dùng để đánh dấu nơi hierarchy phát hiện cycle.

Thường phải dùng cùng:

```sql
NOCYCLE
```

Ví dụ:

```sql
SELECT EMP_ID,
       NAME,
       LEVEL,
       CONNECT_BY_ISCYCLE AS IS_CYCLE
FROM EMP1
START WITH EMP_ID = 1000
CONNECT BY NOCYCLE PRIOR EMP_ID = MGR_ID;
```

Kết quả trong ảnh:

```text
EMP_ID  LEVEL  IS_CYCLE

1000      1       0
2000      2       1
```

Nghĩa là khi từ row `2000` cố đi tiếp, traversal sẽ quay về ancestor đã nằm trên path.

---

## 26. CONNECT_BY_ISCYCLE khác NOCYCLE

Hai cái không giống nhau.

```text
NOCYCLE
→ cho phép query chạy khi có cycle
```

```text
CONNECT_BY_ISCYCLE
→ cho biết row/path nào liên quan tới cycle
```

Có thể nhớ:

> `NOCYCLE` = xử lý.

> `ISCYCLE` = đánh dấu.

---

## 27. Tổng hợp các pseudocolumn/hàm hierarchical

| Thành phần            | Ý nghĩa                  |
| --------------------- | ------------------------ |
| `LEVEL`               | độ sâu hiện tại          |
| `CONNECT_BY_ISLEAF`   | có phải node lá không    |
| `CONNECT_BY_ISCYCLE`  | có phát hiện cycle không |
| `CONNECT_BY_ROOT col` | giá trị root             |
| `SYS_CONNECT_BY_PATH` | path root → current      |
| `ORDER SIBLINGS BY`   | sort node cùng cha       |
| `NOCYCLE`             | tránh lỗi cycle          |

---

## 28. Cách giải bài PRIOR bằng tay ⭐⭐⭐

Đừng cố nhớ:

> "PRIOR ở trái là xuôi, PRIOR ở phải là ngược"

một cách máy móc.

Hãy sử dụng quy trình này.

Giả sử:

```sql
START WITH ID = 1
CONNECT BY PRIOR ID = PARENT_ID;
```

#### Bước 1: lấy root

```text
ID = 1
```

#### Bước 2: nhìn phần có PRIOR

```text
PRIOR ID
```

Giá trị từ current row:

```text
1
```

#### Bước 3: đưa sang phía còn lại

Tìm:

```text
PARENT_ID = 1
```

#### Bước 4

Những row đó là next level.

Rồi lặp lại.

---

## 29. Ví dụ tự tính

Dữ liệu:

```text
ID   PARENT_ID
1    NULL
2    1
3    1
4    2
5    2
```

Query:

```sql
START WITH ID = 1
CONNECT BY PRIOR ID = PARENT_ID
```

Root:

```text
1
```

`PRIOR ID = 1`

→ tìm:

```text
PARENT_ID = 1
```

→ `2`, `3`.

Từ `2`:

```text
PRIOR ID = 2
```

→ tìm:

```text
PARENT_ID = 2
```

→ `4`, `5`.

Tree:

```text
1
├─ 2
│  ├─ 4
│  └─ 5
└─ 3
```

Levels:

```text
1 → 1
2 → 2
4 → 3
5 → 3
3 → 2
```

---

## 30. Đảo PRIOR

Cùng dữ liệu, giả sử:

```sql
START WITH ID = 5
CONNECT BY PRIOR PARENT_ID = ID
```

Root:

```text
ID=5
PARENT_ID=2
```

Lấy:

```text
PRIOR PARENT_ID = 2
```

tìm row:

```text
ID=2
```

sau đó:

```text
2.PARENT_ID = 1
```

tìm:

```text
ID=1
```

Kết quả:

```text
5
↓
2
↓
1
```

→ từ con đi lên ancestor.

Đây chính là lý do **vị trí PRIOR quyết định hướng traversal**.

---

## 31. Hierarchical Query và Self Join liên quan thế nào?

Tên chương là:

```text
계층형 질의와 셀프 조인
Hierarchical Query & Self Join
```

Vì cùng một bài toán cha-con cũng có thể nhìn bằng self join.

Ví dụ bảng EMP:

```text
EMP_ID
NAME
MGR_ID
```

Muốn lấy:

```text
employee + manager
```

có thể:

```sql
SELECT E.NAME AS EMPLOYEE,
       M.NAME AS MANAGER
FROM EMP E
LEFT JOIN EMP M
  ON E.MGR_ID = M.EMP_ID;
```

Đây là **self join** vì:

```text
EMP E
JOIN
EMP M
```

đều là cùng một table `EMP`.

---

## 32. Self Join khác Hierarchical Query

Self Join phù hợp khi ta cần quan hệ cố định:

```text
employee → manager trực tiếp
```

Ví dụ một level.

Hierarchical Query phù hợp khi cần:

```text
employee
→ manager
→ manager của manager
→ ...
→ root
```

tức là số level không cố định.

Có thể nhớ:

```text
SELF JOIN
→ nối vài level cụ thể

HIERARCHICAL QUERY
→ đi recursive không biết trước depth
```

---

## 33. START WITH có thể có nhiều root

Không nhất thiết chỉ một root.

Ví dụ:

```sql
START WITH PARENT_ID IS NULL
```

nếu có:

```text
ID 1 parent NULL
ID 10 parent NULL
```

thì có hai tree:

```text
1
├─ ...
└─ ...

10
├─ ...
└─ ...
```

Mỗi tree có:

```text
LEVEL=1
```

ở root của chính nó.

`CONNECT_BY_ROOT` giúp biết row thuộc tree nào.

---

## 34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table

`LEVEL` tính từ **START WITH hiện tại**.

Giả sử tree thật:

```text
A
└─ B
   └─ C
      └─ D
```

Nếu:

```sql
START WITH A
```

thì:

```text
A 1
B 2
C 3
D 4
```

Nhưng nếu:

```sql
START WITH C
```

thì:

```text
C 1
D 2
```

Nên:

> `LEVEL` là depth từ root được chọn bởi query, không phải depth cố định được lưu trong DB.

---

## 35. START WITH vs WHERE ⭐⭐⭐

Hai cái nhìn giống filter nhưng vai trò khác hẳn.

```sql
START WITH condition
```

trả lời:

> Tôi bắt đầu cây từ đâu?

```sql
WHERE condition
```

trả lời:

> Sau khi hierarchy được xử lý, row nào tôi muốn giữ trong result?

Đừng nhầm.

---

## 36. CONNECT BY condition vs WHERE condition

Cũng cần tách rõ:

```sql
CONNECT BY ... AND condition
```

→ condition ảnh hưởng:

```text
node nào được phép nối tiếp
```

Trong khi:

```sql
WHERE condition
```

→ condition ảnh hưởng:

```text
node nào được hiển thị trong final result
```

Đây chính là ví dụ `AREA='서울지사'` trong ảnh.

---

## 37. Cách hình dung toàn query

Ví dụ:

```sql
SELECT NAME,
       LEVEL
FROM EMP
WHERE ACTIVE = 'Y'
START WITH MGR_ID IS NULL
CONNECT BY NOCYCLE PRIOR EMP_ID = MGR_ID
ORDER SIBLINGS BY NAME;
```

Hãy đọc thành 5 bước logic:

```text
1. START WITH
   chọn root

2. CONNECT BY
   tìm child

3. NOCYCLE
   chặn cycle

4. WHERE
   lọc result

5. ORDER SIBLINGS BY
   sort siblings
```

---

## 38. Bẫy SQLD về PRIOR ⭐⭐⭐

Nếu đề cho:

```sql
CONNECT BY PRIOR 사원번호 = 관리자번호
```

đừng hỏi ngay:

> PRIOR là cha hay con?

Hãy hỏi:

```text
giá trị nào của current row được giữ?
```

`PRIOR 사원번호`.

Sau đó:

```text
tìm next row có 관리자번호 bằng giá trị đó.
```

Do manager ID của child bằng employee ID của parent:

→ đi từ parent xuống child.

---

Nếu:

```sql
CONNECT BY 사원번호 = PRIOR 관리자번호
```

thì:

```text
giữ 관리자번호 của current row
↓
tìm row có 사원번호 bằng nó
```

→ đi từ child lên parent.

## 🔥 SQLD NOTE — 반드시 암기

#### ① Hierarchical Query

```text
START WITH
→ chọn root

CONNECT BY PRIOR
→ định nghĩa quan hệ giữa các level
```

---

#### ② LEVEL

```text
Root = 1
Child = 2
Grandchild = 3
...
```

---

#### ③ PRIOR

Công thức an toàn:

```text
CONNECT BY PRIOR A = B

A của row hiện tại
→ tìm next row có B bằng A
```

---

#### ④ Parent → Child phổ biến

Với:

```text
ID
PARENT_ID
```

dùng:

```sql
CONNECT BY PRIOR ID = PARENT_ID
```

---

#### ⑤ Child → Parent

```sql
CONNECT BY PRIOR PARENT_ID = ID
```

---

#### ⑥ START WITH khác WHERE

```text
START WITH
= chọn nơi bắt đầu

WHERE
= lọc kết quả hierarchy
```

---

#### ⑦ CONNECT BY condition khác WHERE

```text
CONNECT BY condition
= quyết định có nối sang node tiếp theo hay không

WHERE
= filter row sau traversal
```

---

#### ⑧ NOCYCLE

```text
NOCYCLE
→ tránh lỗi do vòng lặp
```

---

#### ⑨ CONNECT_BY_ISCYCLE

```text
1 → phát hiện cycle
0 → không
```

---

#### ⑩ CONNECT_BY_ISLEAF

```text
1 → leaf node
0 → còn child
```

---

#### ⑪ CONNECT_BY_ROOT

```text
current row thuộc root nào?
```

---

#### ⑫ SYS_CONNECT_BY_PATH

```text
root → ... → current
```

Ví dụ:

```text
/A/C/D
```

---

#### ⑬ ORDER SIBLINGS BY

```text
sort các node cùng parent
```

mà không phá cấu trúc cây.

---

## 🧠 Công thức nhớ 10 giây

```text
START WITH
= bắt đầu ở đâu?

CONNECT BY PRIOR
= đi sang row nào tiếp?

LEVEL
= sâu bao nhiêu?

ISLEAF
= có phải lá?

ROOT
= gốc là ai?

PATH
= đi bằng đường nào?

NOCYCLE
= đừng loop

ISCYCLE
= loop ở đâu?
```

Và với `PRIOR`, chỉ cần nhớ một nguyên tắc:

> **Đừng học thuộc PRIOR = cha hay PRIOR = con. Hãy lấy giá trị của biểu thức có PRIOR ở current row, rồi dùng giá trị đó tìm row tiếp theo ở phía còn lại của dấu `=`.**

Nếu áp dụng cách này, kể cả đề SQLD đảo vị trí `PRIOR` hoặc đổi tên column, bạn vẫn tự suy ra được hướng đi đúng.
