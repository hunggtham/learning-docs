# A+ Deep Dive: SQL 결과를 행 단위로 추적하기

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối SQL result với row-level tracing, filter, join và aggregation, để biết mỗi dòng đầu ra đến từ dữ liệu và phép biến đổi nào.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

Deep, Dive, SQL, 결과를, 단위로, 추적하기

> **Chuyển mạch:** Ở chặng này của **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. SQL 문법의 종류 (Các loại cú pháp SQL)**에서 만든 기준을 이어받아 **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## A+ Deep Dive: SQL 결과를 행 단위로 추적하기

Sau khi đã đặt nền bằng **4. SQL 문법의 종류 (Các loại cú pháp SQL)**, ta chuyển sang **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**. Đây là mắt xích 29/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 샘플 스키마와 데이터**. Hãy xác định **1. 샘플 스키마와 데이터** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 샘플 스키마와 데이터

Phần nguồn của **1. 샘플 스키마와 데이터** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 샘플 스키마와 데이터” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```sql
CREATE TABLE sales (
  dept CHAR(1), amount INT
);
INSERT INTO sales VALUES ('A', 120), ('A', 80), ('B', 90), ('B', 40);
```

Phần **1. 샘플 스키마와 데이터** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **1. 샘플 스키마와 데이터** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. WHERE와 HAVING의 순서** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. WHERE와 HAVING의 순서** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. WHERE와 HAVING의 순서

Các ý ngay dưới **2. WHERE와 HAVING의 순서** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. WHERE와 HAVING의 순서” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

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
Ở đoạn **자주 혼동하는 판별 포인트**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 자주 혼동하는 판별 포인트

Bây giờ ta đi vào nội dung của **자주 혼동하는 판별 포인트**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “자주 혼동하는 판별 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `GRANT`/`REVOKE`는 권한을 다루는 **DCL**, `COMMIT`/`ROLLBACK`/`SAVEPOINT`는 트랜잭션을 다루는 **TCL**이다.
- 로킹 단위를 작게 하면 동시성·공유도는 커지지만 잠금 관리 오버헤드도 증가한다. 작은 단위가 교착상태를 자동으로 제거하지는 않는다.
- 2NF는 부분 함수 종속, 3NF는 이행 함수 종속, BCNF는 모든 결정자가 후보키여야 한다는 조건으로 구별한다.
- 뷰는 보안·논리적 독립성에 활용할 수 있지만, 갱신 가능 여부는 정의 방식과 제약에 따라 달라지고 일반적으로 독립 인덱스를 갖지 않는다.

Các bullet của **자주 혼동하는 판별 포인트** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **자주 혼동하는 판별 포인트** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **A+ Deep Dive: SQL 결과를 행 단위로 추적하기** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **150-155. 데이터 조작어 (DML) 확장 및 조건 연산자**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **A+ Deep Dive: SQL 결과를 행 단위로 추적하기**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
