# 07. Testing, đặc tả hợp đồng (contract / 계약) và tích hợp (integration / 통합)

> **Mạch đọc:** Đặt **07. Testing, đặc tả hợp đồng (contract / 계약) và tích hợp (integration / 통합)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **kiểm thử (test / 테스트) theo ranh giới (boundary / 경계)** sang **Hermeticity và dữ liệu**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

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


> **Chuyển mạch:** Từ **kiểm thử (test / 테스트) theo ranh giới (boundary / 경계)**, ta sang **Hermeticity và dữ liệu** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hermeticity và dữ liệu

Mỗi kiểm thử (test / 테스트) phải biết trạng thái (state / 상태) seed, clock, randomness và bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) nào được
thay thế. Fake không được tự tạo ngữ nghĩa (semantics / 의미론) khác môi trường vận hành (production / 운영 환경); dùng kiểm thử tích hợp (integration test / 통합 테스트)
cho truy vấn (query / 쿼리)/giao dịch (transaction / 트랜잭션)/ràng buộc (constraint / 제약조건) mà mock không thể chứng minh. kiểm thử (test / 테스트) dữ liệu (data / 데이터) tối thiểu,
không dùng credential môi trường vận hành (production / 운영 환경) và không phụ thuộc thứ tự kiểm thử (test / 테스트).


> **Chuyển mạch:** Từ **Hermeticity và dữ liệu**, ta sang **đặc tả hợp đồng (contract / 계약) evolution** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đặc tả hợp đồng (contract / 계약) evolution

Consumer-driven đặc tả hợp đồng (contract / 계약) hữu ích khi nhiều nhóm (team / 팀) deploy độc lập. Kiểm tra trường dữ liệu (field / 필드)
thêm/xóa, nullability, enum và status mã (code / 코드). lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) cần kiểm thử (test / 테스트) cả phiên bản (version / 버전)
cũ và mới trong rollout nhiều phiên bản. Property-based kiểm thử (test / 테스트) phù hợp cho parser,
pagination, idempotency và bất biến (invariant / 불변식) máy trạng thái (state machine / 상태 머신).


> **Chuyển mạch:** Từ **đặc tả hợp đồng (contract / 계약) evolution**, ta sang **bằng chứng (evidence / 증거) của kiểm thử (test / 테스트)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bằng chứng (evidence / 증거) của kiểm thử (test / 테스트)

Thất bại (failure / 실패) message phải nêu đầu vào (input / 입력), expected bất biến (invariant / 불변식) và observed trạng thái (state / 상태). Flaky kiểm thử (test / 테스트)
là tín hiệu về race, clock, trạng thái dùng chung (shared state / 공유 상태) hoặc phụ thuộc (dependency / 의존성) không kiểm soát; không
nên chỉ tăng thử lại (retry / 재시도) cho kiểm thử (test / 테스트) để che nguyên nhân.

Tham khảo nền xác minh (verification / 확인) và debugging tại [Software Engineering](../../computer_science/09_software_engineering/README.md).


> **Chuyển mạch:** Từ **bằng chứng (evidence / 증거) của kiểm thử (test / 테스트)**, ta sang **Đào sâu: kiểm thử (test / 테스트) như bằng chứng của bất biến (invariant / 불변식)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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


> **Chuyển mạch:** Từ **Đào sâu: kiểm thử (test / 테스트) như bằng chứng của bất biến (invariant / 불변식)**, ta sang **Bài tập suy luận** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bài tập suy luận

Viết kiểm thử (test / 테스트) ma trận (matrix / 행렬) cho `POST /orders` gồm duplicate key, concurrent phiên bản (version / 버전) xung đột (conflict / 충돌),
payment hết thời gian chờ (timeout / 타임아웃) sau lần ghi nhận (commit / 커밋) và worker replay. Chỉ ra kiểm thử (test / 테스트) nào đơn vị (unit / 단위), tích hợp (integration / 통합),
đặc tả hợp đồng (contract / 계약) hay E2E; giải thích vì sao mock không đủ cho từng bất biến (invariant / 불변식).


> **Chuyển mạch:** Từ **Bài tập suy luận**, ta sang **hiệu năng (performance / 성능) và bảo mật (security / 보안) regression** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **hiệu năng (performance / 성능) và bảo mật (security / 보안) regression**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 backend request lifecycle](./00_backend_request_lifecycle.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
