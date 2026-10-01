# 06. hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도) và idempotency

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **06. hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도) và idempotency**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ngân sách thời gian chờ (timeout budget / 타임아웃 예산)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Thử lại (retry / 재시도) có điều kiện** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Ngân sách thời gian chờ (timeout budget / 타임아웃 예산)

Hết thời gian chờ (timeout / 타임아웃) là một phần của đặc tả hợp đồng (contract / 계약). Nếu yêu cầu (request / 요청) có deadline 2 giây, các phụ thuộc (dependency / 의존성)
không được mỗi cái tự chờ 2 giây. Truyền deadline/cancellation xuống chuỗi (chain / 사슬) và
dành ngân sách cho serialization, queueing và phản hồi (response / 응답). hết thời gian chờ (timeout / 타임아웃) cần phân biệt
connect, TLS, pool acquire, read và total deadline khi máy khách (client / 클라이언트) hỗ trợ.

> **Chuyển mạch:** Deadline còn lại quyết định retry còn hợp lý hay không. **Thử lại (retry / 재시도) có điều kiện** lọc lỗi tạm thời, số attempt và backoff trước khi phần **Idempotency** bảo vệ mutation khỏi side effect lặp.

## Thử lại (retry / 재시도) có điều kiện

Chỉ thử lại (retry / 재시도) lỗi tạm thời, yêu cầu (request / 요청) còn deadline và thao tác (operation / 연산) an toàn để lặp. Không
thử lại (retry / 재시도) kiểm tra hợp lệ (validation / 검증), permission, nghiệp vụ (business / 비즈니스) xung đột (conflict / 충돌) hoặc mọi `5xx` một cách mù quáng.
Exponential backoff + jitter và giới hạn attempts ngăn synchronized thử lại (retry / 재시도) storm.
Mỗi tầng (layer / 계층) không nên thử lại (retry / 재시도) độc lập đến khi tổng số lần nhân lên ngoài dự kiến.

> **Chuyển mạch:** Retry chỉ an toàn khi server nhận diện cùng một mutation. **Idempotency** vì thế cố định key, fingerprint và terminal result; **Quan sát** tiếp theo sẽ phân biệt timeout trước commit với timeout sau commit.

## Idempotency

Một thao tác (operation / 연산) idempotent có thể được gửi lại mà không tạo thêm hiệu ứng lô-gic (logic / 논리).
Với mutation không tự idempotent:

1. caller gửi idempotency key ổn định;
2. máy chủ (server / 서버) lưu key, yêu cầu (request / 요청) fingerprint và terminal kết quả (result / 결과);
3. yêu cầu (request / 요청) trùng fingerprint trả lại kết quả (result / 결과) cũ;
4. key dùng với payload khác bị từ chối;
5. retention đủ dài so với cửa sổ thử lại (retry / 재시도)/replay.

Unique ràng buộc (constraint / 제약조건), chuyển tiếp trạng thái (state transition / 상태 전이) (`pending → completed`) và dedupe bản ghi (record / 레코드) bảo
vệ lớp cơ sở dữ liệu (database / 데이터베이스)/bên tiêu thụ (consumer / 소비자). Idempotency key không thay thế authorization: cùng key
nhưng subject/tenant khác phải bị từ chối.

> **Chuyển mạch:** Có idempotency key vẫn chưa cho biết request đang ở đâu trong hệ thống. **Quan sát** ghi attempt, dependency và commit outcome; dữ liệu này là đầu vào để vẽ retry topology và tìm amplification.

## Quan sát

Ghi attempt number, original yêu cầu (request / 요청) ID, phụ thuộc (dependency / 의존성), hết thời gian chờ (timeout / 타임아웃) reason và final
kết quả (outcome / 결과). Phân biệt “hết thời gian chờ (timeout / 타임아웃) nhưng máy chủ (server / 서버) đã lần ghi nhận (commit / 커밋)” với “chưa tới máy chủ (server / 서버)”; đây là
lý do caller phải truy vấn (query / 쿼리) trạng thái trước khi tạo lại side tác động (effect / 효과).

> **Chuyển mạch:** Các attempt đã đo được phải được đặt lên toàn tuyến browser → API → service → provider. **Đào sâu: thử lại (retry / 재시도) topology** làm lộ retry multiplication và unknown result; **Bài tập suy luận** kiểm tra ngân sách deadline bằng con số cụ thể.

## Đào sâu: thử lại (retry / 재시도) topology

Vẽ toàn bộ thử lại (retry / 재시도) đồ thị (graph / 그래프) trước khi thêm thử lại (retry / 재시도) vòng lặp (loop / 루프):

```text
browser → API client → service A → service B → database/provider
```

Nếu mỗi hop thử lại (retry / 재시도) 3 lần, một yêu cầu (request / 요청) có thể tạo 81 attempts ở phụ thuộc (dependency / 의존성) cuối.
Chọn một thử lại (retry / 재시도) đơn vị sở hữu (owner / 오너), truyền deadline còn lại và để hop khác thất bại (fail / 실패) fast hoặc chỉ
thử lại (retry / 재시도) lỗi vận chuyển (transport / 전송) rất hẹp. Circuit breaker/bulkhead bảo vệ pool nhưng không
thay thế hết thời gian chờ (timeout / 타임아웃) và idempotency.

Hết thời gian chờ (timeout / 타임아웃) tạo trạng thái “unknown”, không phải luôn là thất bại (failure / 실패). Với read, thử lại (retry / 재시도) có
thể an toàn; với mutation, truy vấn (query / 쿼리) status bằng idempotency key/thứ tự (order / 순서) ID trước khi
tạo thao tác (operation / 연산) mới. API nên cung cấp endpoint status nếu thao tác (operation / 연산) có thể chạy sau
khi caller mất kết nối.

> **Chuyển mạch:** Retry topology cho thấy deadline bị tiêu hao và attempt bị nhân lên ở đâu. **Bài tập suy luận** biến topology đó thành ngân sách hop cụ thể; sau đó circuit breaker, bulkhead và load shedding sẽ giới hạn blast radius khi ngân sách không còn đủ.

## Bài tập suy luận

Cho deadline 2 giây, gateway overhead 100 ms, dịch vụ (service / 서비스) A gọi B và B gọi provider.
Đề xuất ngân sách (budget / 예산) từng hop, connect/read hết thời gian chờ (timeout / 타임아웃), số thử lại (retry / 재시도) tối đa và điều kiện dừng;
giải thích vì sao tổng hết thời gian chờ (timeout / 타임아웃) không được vượt deadline dù có backoff.

> **Chuyển mạch:** Bài tập deadline cho thấy retry có thể ăn hết capacity dù từng hop “hợp lệ”. **Circuit breaker, bulkhead và tải (load / 로드) shedding** là lớp bảo vệ cuối để giới hạn blast radius khi dependency vẫn suy giảm.

## Circuit breaker, bulkhead và tải (load / 로드) shedding

Ba cơ chế này giải quyết các thất bại (failure / 실패) khác nhau:

- **Circuit breaker:** ngừng gọi phụ thuộc (dependency / 의존성) đang lỗi sau ngưỡng có bằng chứng,
  chuyển sang half-open có giới hạn để probe khôi phục (recovery / 복구).
- **Bulkhead:** tách luồng thực thi (thread / 스레드)/liên kết (connection / 연결)/tính đồng thời (concurrency / 동시성) ngân sách (budget / 예산) giữa phụ thuộc (dependency / 의존성) hoặc
  tải công việc (workload / 워크로드) để một pool cạn không kéo sập toàn tiến trình (process / 프로세스).
- **tải (load / 로드) shedding:** từ chối hoặc hạ chất lượng yêu cầu (request / 요청) khi hệ thống đã vượt
  sức chứa (capacity / 용량), ưu tiên traffic quan trọng thay vì để mọi yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃).

Breaker cần tránh một trạng thái toàn cục (global / 전역) quá thô: lỗi của một tenant hoặc một
tuyến (route / 경로) có thể không đại diện cho toàn provider. Probe khôi phục (recovery / 복구) phải có jitter và
quota. Fallback chỉ được dùng khi ngữ nghĩa (semantics / 의미론) an toàn; trả dữ liệu bộ nhớ đệm (cache / 캐시) cũ cho
permission-sensitive read có thể tạo bảo mật (security / 보안) bug.

Phụ thuộc (dependency / 의존성) ngân sách (budget / 예산) nên được mô hình hóa bằng tính đồng thời (concurrency / 동시성) × dịch vụ (service / 서비스) thời gian (time / 시간) ≈ in-flight
công việc (work / 작업). Khi queueing và saturation tăng, thử lại (retry / 재시도) thường làm tình hình xấu hơn; hãy
giảm intake trước khi tăng số worker.

> **Bàn giao:** Giữ lại deadline propagation, retry ownership, idempotency và unknown-result handling; quay về [README](./README.md) để nối sang testing hoặc observability của các failure mode này.
