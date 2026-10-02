# 09. Modular monolith và services

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **09. Modular monolith và services**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ranh giới (boundary / 경계) trước topology** làm rõ cặp khái niệm dễ lẫn và giới hạn của cách giải thích; sau đó sang **Khi nào tách dịch vụ (service / 서비스)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối modular monolith với module boundary, dependency và migration, để tách service theo ownership thay vì theo cảm giác.

## Ranh giới (boundary / 경계) trước topology

Modular monolith và microservices đều cần ranh giới mô-đun (module boundary / 모듈 경계) rõ: quyền sở hữu (ownership / 소유권) của
trạng thái (state / 상태), công khai (public / 공개) command/truy vấn (query / 쿼리), bất biến (invariant / 불변식) và phụ thuộc (dependency / 의존성) direction. Tách tiến trình (process / 프로세스)
không tự tạo modularity; nó chỉ thêm mạng (network / 네트워크), triển khai (deployment / 배포), versioning, tracing,
thất bại (failure / 실패) và dữ liệu (data / 데이터) consistency chi phí (cost / 비용).

Một mô-đun (module / 모듈) tốt có API nhỏ, dữ liệu được sở hữu rõ, bất biến (invariant / 불변식) không cần truy cập
trực tiếp bảng của mô-đun (module / 모듈) khác, và phụ thuộc (dependency / 의존성) đi theo hướng có chủ ý. dùng chung (shared / 공유)
utility chỉ chứa thành phần nguyên thủy (primitive / 기본 요소) ổn định; đừng biến nó thành dùng chung (shared / 공유) lĩnh vực (domain / 도메인) mô hình (model / 모델) làm
mọi mô-đun (module / 모듈) coupling.

> **Chuyển mạch:** Ranh giới module phải được chứng minh bằng ownership, invariant và dependency direction trước khi bàn topology. **Khi nào tách dịch vụ (service / 서비스)** dùng các tiêu chí đó để quyết định việc tách có giải quyết một nhu cầu vận hành thật hay chỉ thêm network hop.

## Khi nào tách dịch vụ (service / 서비스)

Tách khi có ranh giới (boundary / 경계) nghiệp vụ (business / 비즈니스)/quyền sở hữu (ownership / 소유권) thật, scaling hoặc availability profile
khác, cadence/triển khai (deployment / 배포) độc lập, hoặc bảo mật (security / 보안)/isolation bắt buộc. Không tách
chỉ vì gói (package / 패키지) dài hay vì muốn “microservice-ready”. Trước khi tách, đo coupling,
giao dịch (transaction / 트랜잭션) crossing, dữ liệu (data / 데이터) truy cập (access / 접근) và operational readiness.

> **Chuyển mạch:** Một quyết định tách chỉ có giá trị khi có đường di chuyển kiểm soát được dữ liệu, contract và rollback. **Di chuyển (migration / 마이그레이션) đường dẫn (path / 경로)** biến quyết định đó thành các bước đo được; **Đào sâu: phụ thuộc (dependency / 의존성) fitness** sẽ kiểm tra boundary sau mỗi bước.

## Di chuyển (migration / 마이그레이션) đường dẫn (path / 경로)

1. Đặt mô-đun (module / 모듈) API và cấm truy cập chéo trực tiếp.
2. Thêm đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트), kiểm tra (audit / 감사) phụ thuộc (dependency / 의존성) và quyền sở hữu (ownership / 소유권).
3. Tách read mô hình (model / 모델)/sự kiện (event / 이벤트) hoặc strangler luồng (flow / 흐름) nếu cần.
4. Chuyển persistence quyền sở hữu (ownership / 소유권), rồi mới chuyển tiến trình (process / 프로세스).
5. Đo độ trễ (latency / 지연 시간), thử lại (retry / 재시도), consistency và chi phí vận hành sau mỗi bước.

Remote lời gọi (call / 호출) không thể giả định như hàm (function / 함수) lời gọi (call / 호출): phải có hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도) chính sách (policy / 정책),
idempotency, versioned đặc tả hợp đồng (contract / 계약) và fallback. phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) nên được
thay bằng cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) + sự kiện (event / 이벤트)/máy trạng thái (state machine / 상태 머신) khi bất biến (invariant / 불변식) cho phép.

Kiến trúc (architecture / 아키텍처) fundamentals và phân tán (distributed / 분산) sự đánh đổi (trade-off / 트레이드오프) thuộc [Computer Science](../../computer_science/README.md); chapter này giữ quyết định topology ở ứng dụng (application / 애플리케이션) mức (level / 수준).

> **Chuyển mạch:** Migration làm lộ coupling thật qua cross-transaction, direct table read và đồng bộ release. **Đào sâu: phụ thuộc (dependency / 의존성) fitness** đo các dấu hiệu đó; **Bài tập suy luận** áp dụng chúng vào việc tách Billing và yêu cầu điều kiện dừng.

## Đào sâu: phụ thuộc (dependency / 의존성) fitness

Ranh giới (boundary / 경계) cần được kiểm tra liên tục bằng các chỉ số: phụ thuộc (dependency / 의존성) đi ngược hướng,
giao dịch (transaction / 트랜잭션) đọc bảng mô-đun (module / 모듈) khác, bên tiêu thụ (consumer / 소비자) ngoài đơn vị sở hữu (owner / 오너), deploy cần bản phát hành (release / 릴리스) đồng
thời, và độ trễ (latency / 지연 시간)/thất bại (failure / 실패) tỷ lệ (rate / 비율) của cross-module lời gọi (call / 호출). kiến trúc (architecture / 아키텍처) kiểm thử (test / 테스트) giúp cấm
import sai, nhưng rà soát (review / 검토) quyền sở hữu (ownership / 소유권) của lược đồ (schema / 스키마), sự kiện (event / 이벤트) và on-call mới phát hiện
ranh giới (boundary / 경계) giả.

Khi dịch vụ (service / 서비스) B cần dữ liệu của A, chọn rõ: synchronous truy vấn (query / 쿼리) (coupling latency),
replicated read mô hình (model / 모델) (eventual consistency), hoặc API composition (coupling
contract). Không cho B đọc thẳng cơ sở dữ liệu (database / 데이터베이스) A “tạm thời” mà không có expiry plan;
đường tắt này thường trở thành giao dịch (transaction / 트랜잭션) xuyên dịch vụ (service / 서비스) không thể tách.

> **Chuyển mạch:** Bài tập Billing buộc nêu invariant cục bộ, outbox, dual-read/dual-write và rollback signal; đây là phép kiểm tra cuối cho việc boundary có đủ thật để tách hay chưa.

## Bài tập suy luận

Lập di chuyển (migration / 마이그레이션) plan tách `Billing` khỏi monolith: bất biến (invariant / 불변식) cục bộ (local / 로컬), giao dịch (transaction / 트랜잭션)
crossing, sự kiện (event / 이벤트)/outbox, dual-read/dual-write rủi ro (risk / 위험), quay lui (rollback / 롤백) tín hiệu (signal / 신호) và điều kiện
dừng. Nếu không thể mô tả quay lui (rollback / 롤백), ranh giới (boundary / 경계) chưa sẵn sàng.

> **Bàn giao:** Giữ lại tiêu chí boundary, migration steps, dependency fitness và rollback signal; quay về [README](./README.md) khi cần nối sang HTTP contract, persistence hoặc reliability.
