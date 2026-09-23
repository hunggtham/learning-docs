# Backend Development Knowledge Library

Đây là namespace canonical cho Backend Development. `backend_core/` giữ các
concept và invariant dùng chung cho mọi backend; `java/`, `spring_java/` và
`python/` là các track implementation cụ thể. Nhờ vậy Spring không còn bị
đồng nhất với toàn bộ backend engineering: framework chỉ là một cách hiện thực
request handling, persistence, security, testing và vận hành.

## Cách đọc

Lộ trình chính đi theo đường đi của một request và các side effect của nó:

```text
request lifecycle
    ↓
HTTP/API contract → identity/session → persistence/transaction
    ↓
cache → async job/message → timeout/retry/idempotency
    ↓
testing/contract → observability/debugging
    ↓
module boundary → service boundary → production case studies
```

Sau `backend_core`, chọn track ngôn ngữ/framework phù hợp. Java và Python giải
thích semantics của runtime/language; Spring giải thích cách framework ánh xạ
các backend concept vào application. Không đọc các track như ba bản sao của
một giáo trình backend.

## Bản đồ nội dung

| Phần | Mục tiêu |
|---|---|
| [`backend_core/`](./backend_core/README.md) | Backend concepts, contracts, failure modes và production reasoning độc lập framework |
| [`java/`](./java/) | Java language/runtime và engineering practice |
| [`spring_java/`](./spring_java/) | Spring ecosystem và cách triển khai backend bằng Java |
| [`python/`](./python/README.md) | Python language/runtime, packaging, concurrency và production engineering |

## Ranh giới với các domain khác

Backend Core không chép lại database internals, network internals, operating
systems hay distributed consensus. Các nền đó có canonical owner trong
[Computer Science](../computer_science/README.md):

- [HTTP/network và distributed systems](../computer_science/06_networks_distributed_systems/README.md)
- [database systems](../computer_science/05_data_databases/README.md)
- [security, reliability và observability](../computer_science/07_security_reliability/README.md)
- [software architecture và testing](../computer_science/09_software_engineering/README.md)

Backend Core chỉ giữ mental model đủ để đưa ra quyết định application-level,
ghi rõ invariant cần bảo vệ và dẫn sang owner khi cần đào sâu. Các ví dụ có thể
dùng HTTP, SQL, queue hoặc tracing nhưng không biến product/tool cụ thể thành
kiến thức canonical.

## Nguyên tắc học

Mỗi chapter nên được đọc bằng chuỗi câu hỏi: contract nào đang được cung cấp;
state nào thay đổi; invariant nào phải giữ; failure có thể xuất hiện ở đâu;
evidence nào giúp phân biệt các giả thuyết; và retry/recovery có làm side effect
bị lặp không. Khi chuyển sang Java, Spring hoặc Python, hãy tìm cách framework
hiện thực cùng invariant đó thay vì học API như kiến thức tách rời.

Đường học nâng cao đi theo các vòng: **correctness** (identity, transaction,
idempotency), **latency** (budget, cache, queue, dependency), **durability**
(commit, outbox, replay), rồi **change safety** (compatibility, migration,
rollout). Mỗi vòng phải nối được design decision với test và telemetry, không chỉ
với một pattern có sẵn.
