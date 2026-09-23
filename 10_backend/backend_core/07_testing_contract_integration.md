# 07. Testing, contract và integration

## Test theo boundary

- **Unit** kiểm tra decision/invariant thuần, chạy nhanh và deterministic.
- **Component/integration** kiểm tra wiring với database, queue, auth adapter và
  transaction thật hoặc container tương đương.
- **Contract** khóa request/response, error shape, event schema và compatibility
  giữa producer–consumer.
- **End-to-end** kiểm tra một số đường đi quan trọng từ entrypoint đến side
  effect; không biến toàn bộ suite thành E2E chậm và khó chẩn đoán.

Test không chỉ xác nhận happy path. Bao phủ duplicate request, timeout, partial
failure, permission boundary, stale version, rollback, retry và shutdown.

## Hermeticity và dữ liệu

Mỗi test phải biết state seed, clock, randomness và external dependency nào được
thay thế. Fake không được tự tạo semantics khác production; dùng integration test
cho query/transaction/constraint mà mock không thể chứng minh. Test data tối thiểu,
không dùng credential production và không phụ thuộc thứ tự test.

## Contract evolution

Consumer-driven contract hữu ích khi nhiều team deploy độc lập. Kiểm tra field
thêm/xóa, nullability, enum và status code. Schema migration cần test cả version
cũ và mới trong rollout nhiều phiên bản. Property-based test phù hợp cho parser,
pagination, idempotency và invariant state machine.

## Evidence của test

Failure message phải nêu input, expected invariant và observed state. Flaky test
là tín hiệu về race, clock, shared state hoặc dependency không kiểm soát; không
nên chỉ tăng retry cho test để che nguyên nhân.

Tham khảo nền verification và debugging tại [Software Engineering](../../computer_science/09_software_engineering/README.md).

## Đào sâu: test như bằng chứng của invariant

Test tốt không chỉ gọi một method; nó chứng minh điều không được phép xảy ra.
Mỗi test quan trọng nên ghi precondition và actor/tenant, command hoặc request
ID, invariant sau commit/rollback, side effect có được lặp không, và evidence dùng
để assert (row, event, response hay metric).

Contract test cần kiểm tra negative space: unknown enum, duplicate event, timeout,
permission boundary và field mà consumer không được hiểu sai. Với eventual
consistency, assert state machine hoặc polling có deadline; không dùng sleep cố
định làm bằng chứng.

Fault injection có thể drop publish, delay database, kill worker sau commit, trả
`429`, đổi clock hoặc reorder event. Chạy trong môi trường cô lập, có blast radius
và cleanup rõ. Một test pass trong happy path không chứng minh recovery đúng.

## Bài tập suy luận

Viết test matrix cho `POST /orders` gồm duplicate key, concurrent version conflict,
payment timeout sau commit và worker replay. Chỉ ra test nào unit, integration,
contract hay E2E; giải thích vì sao mock không đủ cho từng invariant.

## Performance và security regression

Load test phải có workload model (read/write mix, payload size, concurrency,
arrival pattern), warm-up, dataset size và acceptance threshold. P50 đẹp không
che được p99, queueing hoặc pool exhaustion; đo cả downstream và error budget.
Stress test tìm điểm gãy, soak test tìm leak/queue drift, spike test kiểm tra
admission control. Kết quả chỉ có ý nghĩa khi environment và data profile được
ghi lại.

Security regression nên kiểm tra authorization matrix, tenant isolation, CSRF/
CORS policy, replay/idempotency abuse, rate-limit bypass, secret redaction và
error enumeration. Fuzz parser/body size và kiểm tra dependency timeout để tìm
đường DoS logic mà happy-path E2E không thấy.
