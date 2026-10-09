# Thư viện kiến thức phát triển phía máy chủ (backend development knowledge library / 백엔드 개발 지식 라이브러리)

Nguồn chuẩn, version boundary và các claim cần kiểm tra lại nằm trong [source ledger](./SOURCES.md).

> **Mạch đọc:** README này là owner cấp domain của **Thư viện kiến thức phát triển phía máy chủ**. **Cách đọc** xác định prerequisite và câu hỏi trung tâm; **Bản đồ nội dung** chỉ rõ chapter nào sở hữu cơ chế, còn các nhánh Java, Spring và Python chỉ là những hiện thực khác nhau của cùng contract backend.

Đây là không gian tên (namespace / 네임스페이스) chuẩn gốc (canonical / 정본) cho Phát triển phía máy chủ (backend development / 백엔드 개발). `backend_core/` giữ các
concept và bất biến (invariant / 불변식) dùng chung cho mọi backend; `java/`, `spring_java/` và
`python/` là các nhánh học (track / 트랙) hiện thực (implementation / 구현) cụ thể. Nhờ vậy Spring không còn bị
đồng nhất với toàn bộ backend kỹ thuật (engineering / 엔지니어링): khung phần mềm (framework / 프레임워크) chỉ là một cách hiện thực
yêu cầu (request / 요청) handling, persistence, bảo mật (security / 보안), testing và vận hành.

## Cách đọc

Lộ trình chính đi theo đường đi của một yêu cầu (request / 요청) và các side tác động (effect / 효과) của nó:

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

Sau `backend_core`, chọn nhánh học (track / 트랙) ngôn ngữ/khung phần mềm (framework / 프레임워크) phù hợp. Java và Python giải
thích ngữ nghĩa (semantics / 의미론) của thời gian chạy (runtime / 런타임)/ngôn ngữ (language / 언어); Spring giải thích cách khung phần mềm (framework / 프레임워크) ánh xạ
các backend concept vào ứng dụng (application / 애플리케이션). Không đọc các nhánh học (track / 트랙) như ba bản sao của
một giáo trình backend.

> **Chuyển mạch:** Sau khi hiểu cách đọc, Bản đồ nội dung cho biết đường đi từ backend core tới các nhánh ngôn ngữ/framework. Phần kế tiếp đặt ranh giới với Computer Science để tránh trùng owner của database, network và distributed systems.

## Bản đồ nội dung

| Phần | Mục tiêu |
|---|---|
| [`backend_core/`](./backend_core/README.md) | Backend concepts, contracts, thất bại (failure / 실패) modes và môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) độc lập khung phần mềm (framework / 프레임워크) |
| [`java/`](./java/) | Java ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) và kỹ thuật (engineering / 엔지니어링) practice |
| [`spring_java/`](./spring_java/) | Spring ecosystem và cách triển khai backend bằng Java |
| [`python/`](./python/README.md) | Python ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임), packaging, tính đồng thời (concurrency / 동시성) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링) |

> **Chuyển mạch:** Ranh giới owner xác định phần backend chỉ cần giải thích ở mức application contract. **Nguyên tắc học** dùng ranh giới đó để nối quyết định thiết kế với test và telemetry.

## Ranh giới với các lĩnh vực (domain / 도메인) khác

Backend cốt lõi (core / 핵심) không chép lại cơ sở dữ liệu (database / 데이터베이스) internals, mạng (network / 네트워크) internals, operating
các hệ thống (systems / 시스템들) hay phân tán (distributed / 분산) consensus. Các nền đó có đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) trong
[Computer Science](../computer_science/README.md):

- [HTTP/network và distributed systems](../computer_science/06_networks_distributed_systems/README.md)
- [database systems](../computer_science/05_data_databases/README.md)
- [security, reliability và observability](../computer_science/07_security_reliability/README.md)
- [software architecture và testing](../computer_science/09_software_engineering/README.md)

Backend cốt lõi (core / 핵심) chỉ giữ mô hình tư duy (mental model / 사고 모델) đủ để đưa ra quyết định application-level,
ghi rõ bất biến (invariant / 불변식) cần bảo vệ và dẫn sang đơn vị sở hữu (owner / 오너) khi cần đào sâu. Các ví dụ có thể
dùng HTTP, SQL, hàng đợi (queue / 큐) hoặc tracing nhưng không biến sản phẩm (product / 제품)/công cụ (tool / 도구) cụ thể thành
kiến thức chuẩn gốc (canonical / 정본).

> **Chuyển mạch:** Nguyên tắc học gom các trục correctness, latency, durability, safe change và scale thành cách đọc có thể kiểm chứng; đây là điểm bàn giao để chọn chapter cụ thể.

## Nguyên tắc học

Mỗi chapter nên được đọc bằng chuỗi câu hỏi: đặc tả hợp đồng (contract / 계약) nào đang được cung cấp;
trạng thái (state / 상태) nào thay đổi; bất biến (invariant / 불변식) nào phải giữ; thất bại (failure / 실패) có thể xuất hiện ở đâu;
bằng chứng (evidence / 증거) nào giúp phân biệt các giả thuyết; và thử lại (retry / 재시도)/khôi phục (recovery / 복구) có làm side tác động (effect / 효과)
bị lặp không. Khi chuyển sang Java, Spring hoặc Python, hãy tìm cách khung phần mềm (framework / 프레임워크)
hiện thực cùng bất biến (invariant / 불변식) đó thay vì học API như kiến thức tách rời.

Đường học nâng cao đi theo các vòng: **tính đúng đắn (correctness / 정확성)** (identity, transaction,
idempotency), **độ trễ (latency / 지연 시간)** (budget, cache, queue, dependency), **durability**
(commit, outbox, replay), rồi **thay đổi (change / 변경) an toàn (safety / 안전)** (compatibility, migration,
rollout). Mỗi vòng phải nối được thiết kế (design / 설계) quyết định (decision / 결정) với kiểm thử (test / 테스트) và telemetry, không chỉ
với một mẫu (pattern / 패턴) có sẵn.

> **Bàn giao:** Sau **Nguyên tắc học**, hãy chọn chapter trong [backend_core](./backend_core/README.md) hoặc nhánh ngôn ngữ tương ứng; README này vẫn là owner cấp domain.
