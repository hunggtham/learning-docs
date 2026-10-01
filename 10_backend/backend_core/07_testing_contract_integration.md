# 07. Testing, đặc tả hợp đồng (contract / 계약) và tích hợp (integration / 통합)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **07. Testing, đặc tả hợp đồng (contract / 계약) và tích hợp (integration / 통합)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiểm thử (test / 테스트) theo ranh giới (boundary / 경계)** làm rõ cặp khái niệm dễ lẫn và giới hạn của cách giải thích; sau đó sang **Hermeticity và dữ liệu** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Kiểm thử (test / 테스트) theo ranh giới (boundary / 경계)

- **đơn vị (unit / 단위)** kiểm tra quyết định (decision / 결정)/bất biến (invariant / 불변식) thuần, chạy nhanh và deterministic.
- **thành phần (component / 컴포넌트)/tích hợp (integration / 통합)** kiểm tra wiring với cơ sở dữ liệu (database / 데이터베이스), hàng đợi (queue / 큐), auth adapter và
  giao dịch (transaction / 트랜잭션) thật hoặc bộ chứa (container / 컨테이너) tương đương.
- **đặc tả hợp đồng (contract / 계약)** khóa yêu cầu (request / 요청)/phản hồi (response / 응답), lỗi (error / 오류) shape, sự kiện (event / 이벤트) lược đồ (schema / 스키마) và tính tương thích (compatibility / 호환성)
  giữa producer–bên tiêu thụ (consumer / 소비자).
- **End-to-end** kiểm tra một số đường đi quan trọng từ điểm vào (entrypoint / 진입점) đến side
  tác động (effect / 효과); không biến toàn bộ suite thành E2E chậm và khó chẩn đoán.

Kiểm thử (test / 테스트) không chỉ xác nhận happy đường dẫn (path / 경로). Bao phủ duplicate yêu cầu (request / 요청), hết thời gian chờ (timeout / 타임아웃), partial
thất bại (failure / 실패), permission ranh giới (boundary / 경계), stale phiên bản (version / 버전), quay lui (rollback / 롤백), thử lại (retry / 재시도) và shutdown.

> **Chuyển mạch:** Việc chọn unit, integration, contract hay E2E phải gắn với ranh giới cần chứng minh. **Hermeticity và dữ liệu** kiểm soát môi trường của từng lớp; khi dữ liệu và clock đã ổn định, ta mới đánh giá được contract evolution.

## Hermeticity và dữ liệu

Mỗi kiểm thử (test / 테스트) phải biết trạng thái (state / 상태) seed, clock, randomness và bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) nào được
thay thế. Fake không được tự tạo ngữ nghĩa (semantics / 의미론) khác môi trường vận hành (production / 운영 환경); dùng kiểm thử tích hợp (integration test / 통합 테스트)
cho truy vấn (query / 쿼리)/giao dịch (transaction / 트랜잭션)/ràng buộc (constraint / 제약조건) mà mock không thể chứng minh. kiểm thử (test / 테스트) dữ liệu (data / 데이터) tối thiểu,
không dùng credential môi trường vận hành (production / 운영 환경) và không phụ thuộc thứ tự kiểm thử (test / 테스트).

> **Chuyển mạch:** Test hermetic giúp phân biệt lỗi của code với lỗi của fixture, clock hoặc dependency. **Đặc tả hợp đồng (contract / 계약) evolution** dùng nền đó để kiểm tra producer/consumer qua nhiều phiên bản; kết quả cần được ghi thành evidence có thể truy nguyên.

## Đặc tả hợp đồng (contract / 계약) evolution

Consumer-driven đặc tả hợp đồng (contract / 계약) hữu ích khi nhiều nhóm (team / 팀) deploy độc lập. Kiểm tra trường dữ liệu (field / 필드)
thêm/xóa, nullability, enum và status mã (code / 코드). lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) cần kiểm thử (test / 테스트) cả phiên bản (version / 버전)
cũ và mới trong rollout nhiều phiên bản. Property-based kiểm thử (test / 테스트) phù hợp cho parser,
pagination, idempotency và bất biến (invariant / 불변식) máy trạng thái (state machine / 상태 머신).

> **Chuyển mạch:** Contract evolution chỉ đáng tin khi failure message chỉ rõ input, expected và observed. **Bằng chứng (evidence / 증거) của kiểm thử (test / 테스트)** biến từng lần chạy thành dữ liệu review; từ đó có thể đi sâu vào việc chứng minh invariant thay vì chỉ đếm coverage.

## Bằng chứng (evidence / 증거) của kiểm thử (test / 테스트)

Thất bại (failure / 실패) message phải nêu đầu vào (input / 입력), expected bất biến (invariant / 불변식) và observed trạng thái (state / 상태). Flaky kiểm thử (test / 테스트)
là tín hiệu về race, clock, trạng thái dùng chung (shared state / 공유 상태) hoặc phụ thuộc (dependency / 의존성) không kiểm soát; không
nên chỉ tăng thử lại (retry / 재시도) cho kiểm thử (test / 테스트) để che nguyên nhân.

Tham khảo nền xác minh (verification / 확인) và debugging tại [Software Engineering](../../computer_science/09_software_engineering/README.md).

> **Chuyển mạch:** Khi evidence đã nêu rõ trạng thái và invariant, **Đào sâu: kiểm thử (test / 테스트) như bằng chứng của bất biến (invariant / 불변식)** kiểm tra cả negative path, fault injection và eventual consistency. **Bài tập suy luận** sẽ đặt các invariant đó vào một API có duplicate và replay.

## Đào sâu: kiểm thử (test / 테스트) như bằng chứng của bất biến (invariant / 불변식)

Kiểm thử (test / 테스트) tốt không chỉ gọi một phương thức (method / 메서드); nó chứng minh điều không được phép xảy ra.
Mỗi kiểm thử (test / 테스트) quan trọng nên ghi precondition và actor/tenant, command hoặc yêu cầu (request / 요청)
ID, bất biến (invariant / 불변식) sau lần ghi nhận (commit / 커밋)/quay lui (rollback / 롤백), side tác động (effect / 효과) có được lặp không, và bằng chứng (evidence / 증거) dùng
để assert (row, event, response hay metric).

Đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) cần kiểm tra negative không gian (space / 공간): unknown enum, duplicate sự kiện (event / 이벤트), hết thời gian chờ (timeout / 타임아웃),
permission ranh giới (boundary / 경계) và trường dữ liệu (field / 필드) mà bên tiêu thụ (consumer / 소비자) không được hiểu sai. Với eventual
consistency, assert máy trạng thái (state machine / 상태 머신) hoặc polling có deadline; không dùng sleep cố
định làm bằng chứng.

Fault injection có thể drop publish, delay cơ sở dữ liệu (database / 데이터베이스), kill worker sau lần ghi nhận (commit / 커밋), trả
`429`, đổi clock hoặc reorder sự kiện (event / 이벤트). Chạy trong môi trường cô lập, có blast radius
và cleanup rõ. Một kiểm thử (test / 테스트) pass trong happy đường dẫn (path / 경로) không chứng minh khôi phục (recovery / 복구) đúng.

> **Chuyển mạch:** Ở chặng này của **07. Testing, đặc tả hợp đồng (contract / 계약) và tích hợp (integration / 통합)**, **Đào sâu: kiểm thử (test / 테스트) như bằng chứng của bất biến (invariant / 불변식)** nêu điều cần giải thích; **Bài tập suy luận** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hiệu năng (performance / 성능) và bảo mật (security / 보안) regression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bài tập suy luận

Viết kiểm thử (test / 테스트) ma trận (matrix / 행렬) cho `POST /orders` gồm duplicate key, concurrent phiên bản (version / 버전) xung đột (conflict / 충돌),
payment hết thời gian chờ (timeout / 타임아웃) sau lần ghi nhận (commit / 커밋) và worker replay. Chỉ ra kiểm thử (test / 테스트) nào đơn vị (unit / 단위), tích hợp (integration / 통합),
đặc tả hợp đồng (contract / 계약) hay E2E; giải thích vì sao mock không đủ cho từng bất biến (invariant / 불변식).

> **Chuyển mạch:** Ma trận `POST /orders` cho biết lớp test nào chứng minh từng invariant; **Hiệu năng (performance / 성능) và bảo mật (security / 보안) regression** mở rộng cùng ma trận đó sang p99, pool exhaustion, authorization và abuse mà happy-path không thấy.

## Hiệu năng (performance / 성능) và bảo mật (security / 보안) regression

Kiểm thử tải (load test / 부하 테스트) phải có tải công việc (workload / 워크로드) mô hình (model / 모델), warm-up, dataset kích thước (size / 크기) và acceptance threshold. P50 đẹp không
che được p99, queueing hoặc pool exhaustion; đo cả downstream và lỗi (error / 오류) ngân sách (budget / 예산).
kiểm thử sức chịu tải (stress test / 스트레스 테스트) tìm điểm gãy, soak kiểm thử (test / 테스트) tìm leak/hàng đợi (queue / 큐) drift, spike kiểm thử (test / 테스트) kiểm tra
admission điều khiển (control / 제어). Kết quả chỉ có ý nghĩa khi môi trường (environment / 환경) và dữ liệu (data / 데이터) profile được
ghi lại.

Bảo mật (security / 보안) regression nên kiểm tra authorization ma trận (matrix / 행렬), tenant isolation, CSRF/
CORS chính sách (policy / 정책), replay/idempotency abuse, rate-limit bypass, secret redaction và
lỗi (error / 오류) enumeration. Fuzz parser/body kích thước (size / 크기) và kiểm tra phụ thuộc (dependency / 의존성) hết thời gian chờ (timeout / 타임아웃) để tìm
đường DoS lô-gic (logic / 논리) mà happy-path E2E không thấy.

> **Bàn giao:** Giữ lại test boundary, contract evidence, fault injection và regression thresholds; quay về [README](./README.md) khi cần nối một failure mode cụ thể về timeout, security hoặc observability.
