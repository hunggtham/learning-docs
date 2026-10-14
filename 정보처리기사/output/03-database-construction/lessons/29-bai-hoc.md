# A+ Deep Dive: SQL 결과를 행 단위로 추적하기

## A+ Deep Dive: SQL 결과를 행 단위로 추적하기

### 1. 샘플 스키마와 데이터
Phần “1. 샘플 스키마와 데이터” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

```sql
CREATE TABLE sales (
  dept CHAR(1), amount INT
);
INSERT INTO sales VALUES ('A', 120), ('A', 80), ('B', 90), ('B', 40);
```

### 2. WHERE와 HAVING의 순서
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

### 자주 혼동하는 판별 포인트
Phần “자주 혼동하는 판별 포인트” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `GRANT`/`REVOKE`는 권한을 다루는 **DCL**, `COMMIT`/`ROLLBACK`/`SAVEPOINT`는 트랜잭션을 다루는 **TCL**이다.
- 로킹 단위를 작게 하면 동시성·공유도는 커지지만 잠금 관리 오버헤드도 증가한다. 작은 단위가 교착상태를 자동으로 제거하지는 않는다.
- 2NF는 부분 함수 종속, 3NF는 이행 함수 종속, BCNF는 모든 결정자가 후보키여야 한다는 조건으로 구별한다.
- 뷰는 보안·논리적 독립성에 활용할 수 있지만, 갱신 가능 여부는 정의 방식과 제약에 따라 달라지고 일반적으로 독립 인덱스를 갖지 않는다.
