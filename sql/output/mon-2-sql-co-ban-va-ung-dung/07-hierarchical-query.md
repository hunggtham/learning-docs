# Hierarchical Query

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Hierarchical query**. Route đi từ parent/child relation → root/branch traversal → recursive CTE or CONNECT BY → cycle/depth handling → path aggregation, để cấu trúc cây nối với cách truy hồi.

> **Mục tiêu:** START WITH, CONNECT BY PRIOR, LEVEL, NOCYCLE và các pseudocolumn phân cấp.

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

> **Chuyển mạch:** Trong **Hierarchical Query**, **Mạch tư duy (Logic học)** tiếp nhận điểm tựa từ **Từ khóa cần nhớ (Keyword)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạch nối của bài học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **Mạch nối của bài học** tiếp nhận điểm tựa từ **Mạch tư duy (Logic học)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **🧠 Công thức nhớ 10 giây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **Hierarchical Query** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

Để học **Hierarchical Query** như một mạch suy luận, trước hết hãy giữ câu hỏi: **quan hệ cha–con được bắt đầu, mở rộng và dừng lại theo điều kiện nào?** Mục đích của bài là biến **START WITH, CONNECT BY PRIOR, LEVEL, NOCYCLE và các pseudocolumn phân cấp** thành cách đọc có thể áp dụng.

```sql
ORDER BY ...
OFFSET N ROWS
FETCH NEXT M ROWS ONLY
```

nhớ:

```text
OFFSET = bỏ N row
FETCH = lấy M row
```

---

Ta bắt đầu **⑨ Ví dụ 4~6** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ⑨ Ví dụ 4~6

Phần này nối mạch SQL với “⑨ Ví dụ 4~6”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
OFFSET 3 ROWS
FETCH NEXT 3 ROWS ONLY
```

→ row vị trí:

```text
4, 5, 6
```

---

Khi gom phần **⑨ Ví dụ 4~6** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑨ Ví dụ 4~6**. Bây giờ chuyển sang **⑩ SQL Server TOP**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑩ SQL Server TOP** bằng câu hỏi: **ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ⑩ SQL Server TOP

Phần này nối mạch SQL với “⑩ SQL Server TOP”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
SELECT TOP 2 ...
ORDER BY ...
```

---

Khi gom phần **⑩ SQL Server TOP** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑩ SQL Server TOP**. Bây giờ chuyển sang **⑪ WITH TIES**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑪ WITH TIES** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### ⑪ WITH TIES

Phần này nối mạch SQL với “⑪ WITH TIES”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
TOP 2 WITH TIES
```

Nếu vị trí thứ 2 bị đồng hạng:

```text
2 rows có thể biến thành 3+ rows
```

---

Khi gom phần **⑪ WITH TIES** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑪ WITH TIES**. Bây giờ chuyển sang **🧠 Công thức nhớ 10 giây**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **🧠 Công thức nhớ 10 giây** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **🧠 Công thức nhớ 10 giây** tiếp nhận điểm tựa từ **Mạch nối của bài học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1. 계층형 질의 — Hierarchical Query là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 🧠 Công thức nhớ 10 giây

Phần này nối mạch SQL với “🧠 Công thức nhớ 10 giây”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ROWNUM
= Oracle số row giả
= limit trước ORDER BY nếu cùng query level

Top N đúng với ROWNUM
= ORDER BY trong subquery
→ ROWNUM ở ngoài

RANK
= tie cùng hạng + skip rank

OFFSET N
= bỏ N row

FETCH M
= lấy M row

TOP N
= SQL Server

WITH TIES
= lấy thêm những row bằng boundary value
```

Và câu quan trọng nhất của cả chương:

> **TOP-N 문제에서 먼저 판단할 것: "N개의 행"을 원하는가, 아니면 "N개의 순위"를 원하는가?**
> Khi gặp bài TOP-N, trước tiên phải xác định: **muốn N row hay muốn N thứ hạng**.

Hai yêu cầu này nhìn giống nhau nhưng khi có **동점/tie**, kết quả có thể hoàn toàn khác.
Tiếp tục **제6절 계층형 질의와 셀프 조인 — Hierarchical Query & Self Join**. Phần ảnh này tập trung gần như toàn bộ vào **Hierarchical Query của Oracle**, đặc biệt là `START WITH`, `CONNECT BY PRIOR`, `LEVEL`, `NOCYCLE`, `CONNECT_BY_ROOT`, `SYS_CONNECT_BY_PATH`, `CONNECT_BY_ISLEAF`, `CONNECT_BY_ISCYCLE`.

Khi gom phần **🧠 Công thức nhớ 10 giây** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **🧠 Công thức nhớ 10 giây**. Bây giờ chuyển sang **1. 계층형 질의 — Hierarchical Query là gì?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **1. 계층형 질의 — Hierarchical Query là gì?** bằng câu hỏi: **quan hệ cha–con được bắt đầu, mở rộng và dừng lại theo điều kiện nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **1. 계층형 질의 — Hierarchical Query là gì?** tiếp nhận điểm tựa từ **🧠 Công thức nhớ 10 giây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. 순환관계 데이터 모델 — Recursive Relationship** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **1. 계층형 질의 — Hierarchical Query là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **1. 계층형 질의 — Hierarchical Query là gì?**. Bây giờ chuyển sang **2. 순환관계 데이터 모델 — Recursive Relationship**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **2. 순환관계 데이터 모델 — Recursive Relationship** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **2. 순환관계 데이터 모델 — Recursive Relationship** tiếp nhận điểm tựa từ **1. 계층형 질의 — Hierarchical Query là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **2. 순환관계 데이터 모델 — Recursive Relationship** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **2. 순환관계 데이터 모델 — Recursive Relationship**. Bây giờ chuyển sang **3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐** bằng câu hỏi: **quan hệ cha–con được bắt đầu, mở rộng và dừng lại theo điều kiện nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐** tiếp nhận điểm tựa từ **2. 순환관계 데이터 모델 — Recursive Relationship** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. START WITH** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐

Phần này nối mạch SQL với “3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐**. Bây giờ chuyển sang **4. START WITH**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **4. START WITH** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **4. START WITH** tiếp nhận điểm tựa từ **3. Cú pháp cơ bản của Hierarchical Query ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Root luôn có LEVEL = 1** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **4. START WITH** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **4. START WITH**. Bây giờ chuyển sang **5. Root luôn có LEVEL = 1**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **5. Root luôn có LEVEL = 1** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **5. Root luôn có LEVEL = 1** tiếp nhận điểm tựa từ **4. START WITH** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. CONNECT BY PRIOR ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **5. Root luôn có LEVEL = 1** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **5. Root luôn có LEVEL = 1**. Bây giờ chuyển sang **6. CONNECT BY PRIOR ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **6. CONNECT BY PRIOR ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **6. CONNECT BY PRIOR ⭐⭐⭐** tiếp nhận điểm tựa từ **5. Root luôn có LEVEL = 1** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. PRIOR nghĩa chính xác là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **6. CONNECT BY PRIOR ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **6. CONNECT BY PRIOR ⭐⭐⭐**. Bây giờ chuyển sang **7. PRIOR nghĩa chính xác là gì?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **7. PRIOR nghĩa chính xác là gì?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **7. PRIOR nghĩa chính xác là gì?** tiếp nhận điểm tựa từ **6. CONNECT BY PRIOR ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **7. PRIOR nghĩa chính xác là gì?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **7. PRIOR nghĩa chính xác là gì?**. Bây giờ chuyển sang **8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐** tiếp nhận điểm tựa từ **7. PRIOR nghĩa chính xác là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Ví dụ chuẩn trong ảnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐**. Bây giờ chuyển sang **9. Ví dụ chuẩn trong ảnh**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **9. Ví dụ chuẩn trong ảnh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **8. Cách suy luận PRIOR dễ nhất ⭐⭐⭐** cho ta quy tắc; **9. Ví dụ chuẩn trong ảnh** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Ví dụ chuẩn trong ảnh

Phần này nối mạch SQL với “9. Ví dụ chuẩn trong ảnh”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **9. Ví dụ chuẩn trong ảnh** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **9. Ví dụ chuẩn trong ảnh**. Bây giờ chuyển sang **10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **9. Ví dụ chuẩn trong ảnh** cho ta quy tắc; **10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **11. Hướng duyệt xuôi và ngược** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐**. Bây giờ chuyển sang **11. Hướng duyệt xuôi và ngược**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **11. Hướng duyệt xuôi và ngược** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **11. Hướng duyệt xuôi và ngược** tiếp nhận điểm tựa từ **10. Nếu đặt PRIOR sai vị trí thì sao? ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Hướng duyệt xuôi và ngược

Đây là phần cần hiểu thay vì thuộc máy móc.

Khi gom phần **11. Hướng duyệt xuôi và ngược** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **11. Hướng duyệt xuôi và ngược**. Bây giờ chuyển sang **Parent → Child**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Parent → Child** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Parent → Child** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Parent → Child**. Bây giờ chuyển sang **Child → Parent**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Child → Parent** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Child → Parent** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Child → Parent**. Bây giờ chuyển sang **Công thức dễ nhớ**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Công thức dễ nhớ** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **Công thức dễ nhớ** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Công thức dễ nhớ**. Bây giờ chuyển sang **12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐** tiếp nhận điểm tựa từ **11. Hướng duyệt xuôi và ngược** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Nếu AREA nằm trong WHERE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐

Ảnh đưa hai query.

Khi gom phần **12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐**. Bây giờ chuyển sang **Điều kiện nằm trong CONNECT BY**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Điều kiện nằm trong CONNECT BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

### Điều kiện nằm trong CONNECT BY

Phần này nối mạch SQL với “Điều kiện nằm trong CONNECT BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **Điều kiện nằm trong CONNECT BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Điều kiện nằm trong CONNECT BY**. Bây giờ chuyển sang **13. Nếu AREA nằm trong WHERE**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **13. Nếu AREA nằm trong WHERE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **13. Nếu AREA nằm trong WHERE** tiếp nhận điểm tựa từ **12. WHERE và CONNECT BY khác nhau thế nào? ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Thứ tự xử lý quan trọng ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Nếu AREA nằm trong WHERE

Phần này nối mạch SQL với “13. Nếu AREA nằm trong WHERE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **13. Nếu AREA nằm trong WHERE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **13. Nếu AREA nằm trong WHERE**. Bây giờ chuyển sang **14. Thứ tự xử lý quan trọng ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **14. Thứ tự xử lý quan trọng ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **14. Thứ tự xử lý quan trọng ⭐⭐⭐** tiếp nhận điểm tựa từ **13. Nếu AREA nằm trong WHERE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. NOCYCLE ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **14. Thứ tự xử lý quan trọng ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **14. Thứ tự xử lý quan trọng ⭐⭐⭐**. Bây giờ chuyển sang **15. NOCYCLE ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **15. NOCYCLE ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **15. NOCYCLE ⭐⭐⭐** tiếp nhận điểm tựa từ **14. Thứ tự xử lý quan trọng ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Ví dụ cycle trong ảnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **15. NOCYCLE ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **15. NOCYCLE ⭐⭐⭐**. Bây giờ chuyển sang **16. Ví dụ cycle trong ảnh**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **16. Ví dụ cycle trong ảnh** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **15. NOCYCLE ⭐⭐⭐** cho ta quy tắc; **16. Ví dụ cycle trong ảnh** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **17. NOCYCLE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Ví dụ cycle trong ảnh

Phần này nối mạch SQL với “16. Ví dụ cycle trong ảnh”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **16. Ví dụ cycle trong ảnh** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **16. Ví dụ cycle trong ảnh**. Bây giờ chuyển sang **17. NOCYCLE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **17. NOCYCLE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **16. Ví dụ cycle trong ảnh** cho ta quy tắc; **17. NOCYCLE** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **18. LEVEL ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **17. NOCYCLE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **17. NOCYCLE**. Bây giờ chuyển sang **18. LEVEL ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **18. LEVEL ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **18. LEVEL ⭐⭐⭐** tiếp nhận điểm tựa từ **17. NOCYCLE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. CONNECTBYISLEAF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **18. LEVEL ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **18. LEVEL ⭐⭐⭐**. Bây giờ chuyển sang **19. CONNECT_BY_ISLEAF**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **19. CONNECT_BY_ISLEAF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **19. CONNECTBYISLEAF** tiếp nhận điểm tựa từ **18. LEVEL ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. CONNECTBYROOT ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **19. CONNECT_BY_ISLEAF** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **19. CONNECT_BY_ISLEAF**. Bây giờ chuyển sang **20. CONNECT_BY_ROOT ⭐⭐⭐**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **20. CONNECT_BY_ROOT ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **20. CONNECTBYROOT ⭐⭐⭐** tiếp nhận điểm tựa từ **19. CONNECTBYISLEAF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. SYSCONNECTBYPATH ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **20. CONNECT_BY_ROOT ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **20. CONNECT_BY_ROOT ⭐⭐⭐**. Bây giờ chuyển sang **21. SYS_CONNECT_BY_PATH ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **21. SYS_CONNECT_BY_PATH ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **20. CONNECTBYROOT ⭐⭐⭐** xác định đầu vào; **21. SYSCONNECTBYPATH ⭐⭐⭐** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. Ví dụ kết hợp CONNECTBYROOT + PATH** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. SYS_CONNECT_BY_PATH ⭐⭐⭐

Phần này nối mạch SQL với “21. SYS_CONNECT_BY_PATH ⭐⭐⭐”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **21. SYS_CONNECT_BY_PATH ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **21. SYS_CONNECT_BY_PATH ⭐⭐⭐**. Bây giờ chuyển sang **22. Ví dụ kết hợp CONNECT_BY_ROOT + PATH**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **22. Ví dụ kết hợp CONNECT_BY_ROOT + PATH** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **21. SYSCONNECTBYPATH ⭐⭐⭐** cho ta quy tắc; **22. Ví dụ kết hợp CONNECTBYROOT + PATH** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **23. ORDER SIBLINGS BY** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **22. Ví dụ kết hợp CONNECT_BY_ROOT + PATH** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **22. Ví dụ kết hợp CONNECT_BY_ROOT + PATH**. Bây giờ chuyển sang **23. ORDER SIBLINGS BY**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **23. ORDER SIBLINGS BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **22. Ví dụ kết hợp CONNECTBYROOT + PATH** cho ta quy tắc; **23. ORDER SIBLINGS BY** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **24. Vì sao không dùng ORDER BY bình thường?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **23. ORDER SIBLINGS BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **23. ORDER SIBLINGS BY**. Bây giờ chuyển sang **24. Vì sao không dùng ORDER BY bình thường?**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **24. Vì sao không dùng ORDER BY bình thường?** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **24. Vì sao không dùng ORDER BY bình thường?** tiếp nhận điểm tựa từ **23. ORDER SIBLINGS BY** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. CONNECTBYISCYCLE ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **24. Vì sao không dùng ORDER BY bình thường?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **24. Vì sao không dùng ORDER BY bình thường?**. Bây giờ chuyển sang **25. CONNECT_BY_ISCYCLE ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **25. CONNECT_BY_ISCYCLE ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **25. CONNECTBYISCYCLE ⭐⭐⭐** tiếp nhận điểm tựa từ **24. Vì sao không dùng ORDER BY bình thường?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. CONNECTBYISCYCLE khác NOCYCLE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **25. CONNECT_BY_ISCYCLE ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **25. CONNECT_BY_ISCYCLE ⭐⭐⭐**. Bây giờ chuyển sang **26. CONNECT_BY_ISCYCLE khác NOCYCLE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **26. CONNECT_BY_ISCYCLE khác NOCYCLE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **26. CONNECTBYISCYCLE khác NOCYCLE** tiếp nhận điểm tựa từ **25. CONNECTBYISCYCLE ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Tổng hợp các pseudocolumn/hàm hierarchical** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **26. CONNECT_BY_ISCYCLE khác NOCYCLE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **26. CONNECT_BY_ISCYCLE khác NOCYCLE**. Bây giờ chuyển sang **27. Tổng hợp các pseudocolumn/hàm hierarchical**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **27. Tổng hợp các pseudocolumn/hàm hierarchical** bằng câu hỏi: **quan hệ cha–con được bắt đầu, mở rộng và dừng lại theo điều kiện nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **27. Tổng hợp các pseudocolumn/hàm hierarchical** gom các mảnh từ **26. CONNECTBYISCYCLE khác NOCYCLE** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **28. Cách giải bài PRIOR bằng tay ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Tổng hợp các pseudocolumn/hàm hierarchical

Phần này nối mạch SQL với “27. Tổng hợp các pseudocolumn/hàm hierarchical”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **27. Tổng hợp các pseudocolumn/hàm hierarchical** lại, ta không cần nhớ các dòng như những mảnh rời: bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **27. Tổng hợp các pseudocolumn/hàm hierarchical**. Bây giờ chuyển sang **28. Cách giải bài PRIOR bằng tay ⭐⭐⭐**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **28. Cách giải bài PRIOR bằng tay ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **28. Cách giải bài PRIOR bằng tay ⭐⭐⭐** gom các mảnh từ **27. Tổng hợp các pseudocolumn/hàm hierarchical** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **29. Ví dụ tự tính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **28. Cách giải bài PRIOR bằng tay ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **28. Cách giải bài PRIOR bằng tay ⭐⭐⭐**. Bây giờ chuyển sang **Bước 1: lấy root**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bước 1: lấy root** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Bước 1: lấy root

Phần này nối mạch SQL với “Bước 1: lấy root”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
ID = 1
```

Khi gom phần **Bước 1: lấy root** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bước 1: lấy root**. Bây giờ chuyển sang **Bước 2: nhìn phần có PRIOR**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bước 2: nhìn phần có PRIOR** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Bước 2: nhìn phần có PRIOR

Phần này nối mạch SQL với “Bước 2: nhìn phần có PRIOR”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
PRIOR ID
```

Giá trị từ current row:

```text
1
```

Khi gom phần **Bước 2: nhìn phần có PRIOR** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bước 2: nhìn phần có PRIOR**. Bây giờ chuyển sang **Bước 3: đưa sang phía còn lại**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bước 3: đưa sang phía còn lại** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Bước 3: đưa sang phía còn lại

Tìm:

```text
PARENT_ID = 1
```

Khi gom phần **Bước 3: đưa sang phía còn lại** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bước 3: đưa sang phía còn lại**. Bây giờ chuyển sang **Bước 4**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **Bước 4** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### Bước 4

Những row đó là next level.

Rồi lặp lại.

---

Khi gom phần **Bước 4** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **Bước 4**. Bây giờ chuyển sang **29. Ví dụ tự tính**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **29. Ví dụ tự tính** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **28. Cách giải bài PRIOR bằng tay ⭐⭐⭐** cho ta quy tắc; **29. Ví dụ tự tính** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **30. Đảo PRIOR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **29. Ví dụ tự tính** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **29. Ví dụ tự tính**. Bây giờ chuyển sang **30. Đảo PRIOR**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **30. Đảo PRIOR** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **29. Ví dụ tự tính** cho ta quy tắc; **30. Đảo PRIOR** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **31. Hierarchical Query và Self Join liên quan thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **30. Đảo PRIOR** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **30. Đảo PRIOR**. Bây giờ chuyển sang **31. Hierarchical Query và Self Join liên quan thế nào?**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **31. Hierarchical Query và Self Join liên quan thế nào?** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **31. Hierarchical Query và Self Join liên quan thế nào?** tiếp nhận điểm tựa từ **30. Đảo PRIOR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Self Join khác Hierarchical Query** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **31. Hierarchical Query và Self Join liên quan thế nào?** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **31. Hierarchical Query và Self Join liên quan thế nào?**. Bây giờ chuyển sang **32. Self Join khác Hierarchical Query**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **32. Self Join khác Hierarchical Query** bằng câu hỏi: **ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **32. Self Join khác Hierarchical Query** tiếp nhận điểm tựa từ **31. Hierarchical Query và Self Join liên quan thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. START WITH có thể có nhiều root** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **32. Self Join khác Hierarchical Query** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **32. Self Join khác Hierarchical Query**. Bây giờ chuyển sang **33. START WITH có thể có nhiều root**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **33. START WITH có thể có nhiều root** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **33. START WITH có thể có nhiều root** tiếp nhận điểm tựa từ **32. Self Join khác Hierarchical Query** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **33. START WITH có thể có nhiều root** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **33. START WITH có thể có nhiều root**. Bây giờ chuyển sang **34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **33. START WITH có thể có nhiều root** đã nêu tiêu chí phân biệt, còn **34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **35. START WITH vs WHERE ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table**. Bây giờ chuyển sang **35. START WITH vs WHERE ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **35. START WITH vs WHERE ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **34. Một điểm dễ nhầm: LEVEL không phải depth tuyệt đối của table** đã nêu tiêu chí phân biệt, còn **35. START WITH vs WHERE ⭐⭐⭐** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **36. CONNECT BY condition vs WHERE condition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **35. START WITH vs WHERE ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **35. START WITH vs WHERE ⭐⭐⭐**. Bây giờ chuyển sang **36. CONNECT BY condition vs WHERE condition**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **36. CONNECT BY condition vs WHERE condition** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **36. CONNECT BY condition vs WHERE condition** tiếp nhận điểm tựa từ **35. START WITH vs WHERE ⭐⭐⭐** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Cách hình dung toàn query** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **36. CONNECT BY condition vs WHERE condition** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **36. CONNECT BY condition vs WHERE condition**. Bây giờ chuyển sang **37. Cách hình dung toàn query**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **37. Cách hình dung toàn query** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **37. Cách hình dung toàn query** tiếp nhận điểm tựa từ **36. CONNECT BY condition vs WHERE condition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Bẫy SQLD về PRIOR ⭐⭐⭐** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **37. Cách hình dung toàn query** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **37. Cách hình dung toàn query**. Bây giờ chuyển sang **38. Bẫy SQLD về PRIOR ⭐⭐⭐**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **38. Bẫy SQLD về PRIOR ⭐⭐⭐** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Ở chặng này của **Hierarchical Query**, **37. Cách hình dung toàn query** đã nêu tiêu chí phân biệt, còn **38. Bẫy SQLD về PRIOR ⭐⭐⭐** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **🔥 SQLD NOTE — 반드시 암기** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi gom phần **38. Bẫy SQLD về PRIOR ⭐⭐⭐** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **38. Bẫy SQLD về PRIOR ⭐⭐⭐**. Bây giờ chuyển sang **🔥 SQLD NOTE — 반드시 암기**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **🔥 SQLD NOTE — 반드시 암기** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hierarchical Query**, **38. Bẫy SQLD về PRIOR ⭐⭐⭐** đã nêu tiêu chí phân biệt, còn **🔥 SQLD NOTE — 반드시 암기** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **🧠 Công thức nhớ 10 giây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 🔥 SQLD NOTE — 반드시 암기

Khi gom phần **🔥 SQLD NOTE — 반드시 암기** lại, ta không cần nhớ các dòng như những mảnh rời: các định nghĩa và điều kiện làm rõ phạm vi áp dụng. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **🔥 SQLD NOTE — 반드시 암기**. Bây giờ chuyển sang **① Hierarchical Query**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **① Hierarchical Query** bằng câu hỏi: **quan hệ cha–con được bắt đầu, mở rộng và dừng lại theo điều kiện nào?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ① Hierarchical Query

Phần này nối mạch SQL với “① Hierarchical Query”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
START WITH
→ chọn root

CONNECT BY PRIOR
→ định nghĩa quan hệ giữa các level
```

---

Khi gom phần **① Hierarchical Query** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **① Hierarchical Query**. Bây giờ chuyển sang **② LEVEL**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **② LEVEL** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ② LEVEL

Phần này nối mạch SQL với “② LEVEL”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
Root = 1
Child = 2
Grandchild = 3
...
```

---

Khi gom phần **② LEVEL** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **② LEVEL**. Bây giờ chuyển sang **③ PRIOR**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **③ PRIOR** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ③ PRIOR

Công thức an toàn:

```text
CONNECT BY PRIOR A = B

A của row hiện tại
→ tìm next row có B bằng A
```

---

Khi gom phần **③ PRIOR** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **③ PRIOR**. Bây giờ chuyển sang **④ Parent → Child phổ biến**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **④ Parent → Child phổ biến** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

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

Khi gom phần **④ Parent → Child phổ biến** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **④ Parent → Child phổ biến**. Bây giờ chuyển sang **⑤ Child → Parent**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑤ Child → Parent** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑤ Child → Parent

Phần này nối mạch SQL với “⑤ Child → Parent”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```sql
CONNECT BY PRIOR PARENT_ID = ID
```

---

Khi gom phần **⑤ Child → Parent** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑤ Child → Parent**. Bây giờ chuyển sang **⑥ START WITH khác WHERE**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑥ START WITH khác WHERE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑥ START WITH khác WHERE

Phần này nối mạch SQL với “⑥ START WITH khác WHERE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
START WITH
= chọn nơi bắt đầu

WHERE
= lọc kết quả hierarchy
```

---

Khi gom phần **⑥ START WITH khác WHERE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑥ START WITH khác WHERE**. Bây giờ chuyển sang **⑦ CONNECT BY condition khác WHERE**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑦ CONNECT BY condition khác WHERE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑦ CONNECT BY condition khác WHERE

Phần này nối mạch SQL với “⑦ CONNECT BY condition khác WHERE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
CONNECT BY condition
= quyết định có nối sang node tiếp theo hay không

WHERE
= filter row sau traversal
```

---

Khi gom phần **⑦ CONNECT BY condition khác WHERE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑦ CONNECT BY condition khác WHERE**. Bây giờ chuyển sang **⑧ NOCYCLE**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑧ NOCYCLE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑧ NOCYCLE

Phần này nối mạch SQL với “⑧ NOCYCLE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
NOCYCLE
→ tránh lỗi do vòng lặp
```

---

Khi gom phần **⑧ NOCYCLE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑧ NOCYCLE**. Bây giờ chuyển sang **⑨ CONNECT_BY_ISCYCLE**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑨ CONNECT_BY_ISCYCLE** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑨ CONNECT_BY_ISCYCLE

Phần này nối mạch SQL với “⑨ CONNECT_BY_ISCYCLE”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
1 → phát hiện cycle
0 → không
```

---

Khi gom phần **⑨ CONNECT_BY_ISCYCLE** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑨ CONNECT_BY_ISCYCLE**. Bây giờ chuyển sang **⑩ CONNECT_BY_ISLEAF**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑩ CONNECT_BY_ISLEAF** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑩ CONNECT_BY_ISLEAF

Phần này nối mạch SQL với “⑩ CONNECT_BY_ISLEAF”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
1 → leaf node
0 → còn child
```

---

Khi gom phần **⑩ CONNECT_BY_ISLEAF** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑩ CONNECT_BY_ISLEAF**. Bây giờ chuyển sang **⑪ CONNECT_BY_ROOT**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑪ CONNECT_BY_ROOT** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑪ CONNECT_BY_ROOT

Phần này nối mạch SQL với “⑪ CONNECT_BY_ROOT”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
current row thuộc root nào?
```

---

Khi gom phần **⑪ CONNECT_BY_ROOT** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑪ CONNECT_BY_ROOT**. Bây giờ chuyển sang **⑫ SYS_CONNECT_BY_PATH**: phần mới sẽ **đối chiếu** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑫ SYS_CONNECT_BY_PATH** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑫ SYS_CONNECT_BY_PATH

Phần này nối mạch SQL với “⑫ SYS_CONNECT_BY_PATH”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
root → ... → current
```

Ví dụ:

```text
/A/C/D
```

---

Khi gom phần **⑫ SYS_CONNECT_BY_PATH** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑫ SYS_CONNECT_BY_PATH**. Bây giờ chuyển sang **⑬ ORDER SIBLINGS BY**: phần mới sẽ **dùng lại** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **⑬ ORDER SIBLINGS BY** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

#### ⑬ ORDER SIBLINGS BY

Phần này nối mạch SQL với “⑬ ORDER SIBLINGS BY”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

```text
sort các node cùng parent
```

mà không phá cấu trúc cây.

---

Khi gom phần **⑬ ORDER SIBLINGS BY** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Vậy ta đã có tiêu chí để đọc **⑬ ORDER SIBLINGS BY**. Bây giờ chuyển sang **🧠 Công thức nhớ 10 giây**: phần mới sẽ **mở rộng** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.

Ta bắt đầu **🧠 Công thức nhớ 10 giây** bằng câu hỏi: **khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó.

> **Chuyển mạch:** Trong **Hierarchical Query**, **🧠 Công thức nhớ 10 giây** tiếp nhận điểm tựa từ **🔥 SQLD NOTE — 반드시 암기** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 🧠 Công thức nhớ 10 giây

Phần này nối mạch SQL với “🧠 Công thức nhớ 10 giây”, giải thích dữ liệu đầu vào, điều kiện xử lý và kết quả cần kiểm tra trước khi đọc ví dụ.

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

Khi gom phần **🧠 Công thức nhớ 10 giây** lại, ta không cần nhớ các dòng như những mảnh rời: cú pháp cho thấy quy tắc được thực hiện trong truy vấn và ví dụ cho thấy quy tắc biến thành kết quả cụ thể. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần.

Như vậy, **🧠 Công thức nhớ 10 giây** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.

> **Bàn giao:** Sau **🧠 Công thức nhớ 10 giây**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
