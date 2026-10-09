# SQL / SQLD — source ledger và engine/exam-version boundary

> **Owner:** `sql/` (canonical SQL and SQLD learning output). Ledger này tách relational concepts/SQL semantics, engine-specific behavior và exam syllabus.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| SQL-PG-01 | PostgreSQL Global Development Group | SQL, type, transaction, planner và implementation behavior của PostgreSQL | https://www.postgresql.org/docs/current/ | current manual; major version phải ghi | Không suy PostgreSQL behavior thành SQL standard hoặc Oracle/MySQL behavior; ghi release/config | SQL lessons and examples |
| SQL-ORACLE-01 | Oracle — Database SQL Language Reference | Oracle SQL syntax, functions, transaction/DDL behavior | https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/ | Oracle Database 23c reference; kiểm tra 2026-10-09 | Ghi DB release; không dùng làm generic SQL semantics nếu feature/vendor-specific | SQLD vendor comparison |
| SQL-SQLITE-01 | SQLite project | compact engine SQL grammar, type affinity, locking và limitations | https://www.sqlite.org/lang.html | docs live; release phải ghi khi claim behavior | SQLite compatibility/affinity khác server RDBMS; không suy portability từ syntax alone | engine comparison |
| SQL-DATAQ-01 | 한국데이터산업진흥원 — DataQ | exam route, registration và official SQLD notices | https://www.dataq.or.kr/ | portal; notice/exam cycle phải ghi | Portal không đủ để xác nhận syllabus/version; phải lưu notice/guide cụ thể và kỳ thi | SQLD exam boundary |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| SQL-STANDARD-01 | `REVIEW_REQUIRED` | Một câu SQL có thể hợp lệ ở engine này nhưng không portable; phải ghi standard/engine/version và expected result. | Owner lesson + engine reviewer |
| SQL-PLAN-01 | `NEEDS_SOURCE` | Plan, index, isolation, lock, cost và performance claim cần engine/version/schema/data distribution/plan output. | Owner advanced SQL |
| SQL-EXAM-01 | `NEEDS_SOURCE` | Exam scope, weighting, pass rule và terminology phải lấy từ notice/guide chính thức của đúng kỳ; không dùng summary/old PDF như current. | Owner SQLD output |
| SQL-SECURITY-01 | `REVIEW_REQUIRED` | SQL injection/privilege/PII claim phải gắn DB/app boundary, threat model và tested mitigation; syntax lesson không đủ. | Owner security boundary |

## Quy trình refresh

1. Gắn engine/version và expected result cho example; tách relational concept khỏi vendor syntax.
2. Khi engine release hoặc exam notice đổi, chạy regression examples và cập nhật lesson/ledger.
3. Lưu exam cycle, notice URL và ngày hiệu lực; thiếu official notice thì giữ `NEEDS_SOURCE`.
4. Không dùng structural/output audit thay cho execution test và manual explanation review.
