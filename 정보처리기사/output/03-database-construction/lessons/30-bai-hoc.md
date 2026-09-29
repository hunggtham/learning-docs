# A+ Deep Dive: SQL 결과를 행 단위로 추적하기

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

Deep, Dive, SQL, 결과를, 단위로, 추적하기

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. SQL 문법의 종류 (Các loại cú pháp SQL)**에서 만든 기준을 이어받아 **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** và nối nó với **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## A+ Deep Dive: SQL 결과를 행 단위로 추적하기

Từ **4. SQL 문법의 종류 (Các loại cú pháp SQL)**, ta đã có điểm tựa để bước vào **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 30/56 trước khi đi vào chi tiết.

Để đọc **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **1. 샘플 스키마와 데이터** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 1. 샘플 스키마와 데이터

Các ý ngay dưới **1. 샘플 스키마와 데이터** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

```sql
CREATE TABLE sales (
  dept CHAR(1), amount INT
);
INSERT INTO sales VALUES ('A', 120), ('A', 80), ('B', 90), ('B', 40);
```

Phần **1. 샘플 스키마와 데이터** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **1. 샘플 스키마와 데이터** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. WHERE와 HAVING의 순서** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **2. WHERE와 HAVING의 순서**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 2. WHERE와 HAVING의 순서

Bây giờ ta đi vào nội dung của **2. WHERE와 HAVING의 순서**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

```sql
SELECT dept, SUM(amount) AS total
FROM sales
WHERE amount >= 80
GROUP BY dept
HAVING SUM(amount) >= 150
ORDER BY total DESC;
```

행 필터를 먼저 적용하면 `(A,120)`, `(A,80)`, `(B,90)`만 남는다. 그룹별 합계는
`A=200`, `B=90`이므로 `HAVING`을 통과하는 최종 결과는 `A | 200` 한 행이다.

- `WHERE`: 그룹화 **전** 개별 행을 제거.
- `GROUP BY`: 같은 키를 그룹으로 묶고 집계.
- `HAVING`: 그룹화 **후** 집계 결과를 제거.
- `ORDER BY`: 최종 결과의 표시 순서를 정함. 명시하지 않으면 순서를 가정하지 않는다.

> **시험 함정:** 집계 함수 조건을 `WHERE`에 넣지 않고 `HAVING`에 둔다. 별칭(alias)은 구현/문맥에 따라 `WHERE`에서 바로 사용할 수 없으므로 원래 표현식을 확인한다.

Các bullet của **2. WHERE와 HAVING의 순서** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. WHERE와 HAVING의 순서**, đừng bắt đầu lại từ số không. **자주 혼동하는 판별 포인트** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **자주 혼동하는 판별 포인트**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 자주 혼동하는 판별 포인트

Phần nguồn của **자주 혼동하는 판별 포인트** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- `GRANT`/`REVOKE`는 권한을 다루는 **DCL**, `COMMIT`/`ROLLBACK`/`SAVEPOINT`는 트랜잭션을 다루는 **TCL**이다.
- 로킹 단위를 작게 하면 동시성·공유도는 커지지만 잠금 관리 오버헤드도 증가한다. 작은 단위가 교착상태를 자동으로 제거하지는 않는다.
- 2NF는 부분 함수 종속, 3NF는 이행 함수 종속, BCNF는 모든 결정자가 후보키여야 한다는 조건으로 구별한다.
- 뷰는 보안·논리적 독립성에 활용할 수 있지만, 갱신 가능 여부는 정의 방식과 제약에 따라 달라지고 일반적으로 독립 인덱스를 갖지 않는다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.