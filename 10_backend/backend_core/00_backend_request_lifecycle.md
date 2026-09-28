# 00. Backend vòng đời yêu cầu (request lifecycle / 요청 생명주기)

> **Mạch đọc:** Đặt **00. Backend vòng đời yêu cầu (request lifecycle / 요청 생명주기)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Mục tiêu** sang **bất biến (invariant / 불변식) cần giữ**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## Mục tiêu

Một backend yêu cầu (request / 요청) không chỉ là lời gọi đến controller. Nó là một đường đi qua
nhiều ranh giới (boundary / 경계), trong đó mỗi ranh giới (boundary / 경계) có đặc tả hợp đồng (contract / 계약), hết thời gian chờ (timeout / 타임아웃), trạng thái (state / 상태) và bằng chứng (evidence / 증거)
riêng.

```text
client
  → DNS/TLS/proxy/load balancer
  → server process / framework adapter
  → middleware (request id, auth, limits)
  → handler/use case
  → repository/cache/remote dependency
  → commit hoặc rollback
  → response + logs/metrics/traces
```


> **Chuyển mạch:** Từ **Mục tiêu**, ta sang **bất biến (invariant / 불변식) cần giữ** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bất biến (invariant / 불변식) cần giữ

- Mỗi yêu cầu (request / 요청) có một correlation/yêu cầu (request / 요청) ID; log ở các tầng (layer / 계층) có thể nối lại.
- Authentication được hoàn tất trước khi dùng định danh (identity / 식별자) để authorize.
- kiểm tra hợp lệ (validation / 검증) ở ranh giới (boundary / 경계) không thay thế bất biến (invariant / 불변식) trong lĩnh vực (domain / 도메인) và cơ sở dữ liệu (database / 데이터베이스).
- Side tác động (effect / 효과) chỉ được báo thành công khi trạng thái tương ứng đã lần ghi nhận (commit / 커밋), hoặc
  đặc tả hợp đồng (contract / 계약) nói rõ nó được xử lý bất đồng bộ.
- Mọi phụ thuộc (dependency / 의존성) bên ngoài có hết thời gian chờ (timeout / 타임아웃) hữu hạn; không để yêu cầu (request / 요청) chờ vô hạn.


> **Chuyển mạch:** Từ **bất biến (invariant / 불변식) cần giữ**, ta sang **Sync và async** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sync và async

Synchronous luồng (flow / 흐름) phù hợp khi caller cần kết quả ngay và ngân sách độ trễ (latency / 지연 시간) đủ.
Async luồng (flow / 흐름) phù hợp cho email, export, webhook, indexing hoặc công việc dài.
Đừng trả `200 OK` cho một side tác động (effect / 효과) chưa có đơn vị sở hữu (owner / 오너); dùng `202 Accepted` với job
ID và trạng thái có thể truy vấn khi processing còn tiếp diễn.


> **Chuyển mạch:** Từ **Sync và async**, ta sang **Cách gỡ lỗi (debug / 디버그)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách gỡ lỗi (debug / 디버그)

Bắt đầu từ yêu cầu (request / 요청) ID, timestamp và tuyến (route / 경로). Xác định yêu cầu (request / 요청) đã chết ở proxy,
hàng đợi (queue / 큐), ứng dụng (application / 애플리케이션), cơ sở dữ liệu (database / 데이터베이스) hay remote phụ thuộc (dependency / 의존성); sau đó so sánh độ trễ (latency / 지연 시간) theo
từng span thay vì đoán từ tổng thời gian. Một phản hồi (response / 응답) lỗi (error / 오류) không chứng minh
giao dịch (transaction / 트랜잭션) đã quay lui (rollback / 롤백) nếu side tác động (effect / 효과) ngoài cơ sở dữ liệu (database / 데이터베이스) đã xảy ra.


> **Chuyển mạch:** Từ **Cách gỡ lỗi (debug / 디버그)**, ta sang **Liên kết chuẩn gốc (canonical / 정본)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết chuẩn gốc (canonical / 정본)

Chi tiết tiến trình (process / 프로세스), mạng (network / 네트워크) đường dẫn (path / 경로) và lưu trữ (storage / 저장소) thuộc [Computer Science](../../computer_science/README.md).
Chapter này giữ application-level vòng đời (lifecycle / 생명주기) và cách đặt ranh giới (boundary / 경계), không mô tả
lại TCP, scheduler hay WAL internals.


> **Chuyển mạch:** Từ **Liên kết chuẩn gốc (canonical / 정본)**, ta sang **Đào sâu: yêu cầu (request / 요청) như một máy trạng thái (state machine / 상태 머신)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đào sâu: yêu cầu (request / 요청) như một máy trạng thái (state machine / 상태 머신)

Đừng coi yêu cầu (request / 요청) là một hàm `input → output` đơn giản. Trong môi trường vận hành (production / 운영 환경), nó có
thể đi qua các trạng thái:

```text
received → admitted → authenticated → authorized → executing
    → committed → response_sent
                 ↘ failed/retryable
```

`response_sent` không đồng nghĩa side tác động (effect / 효과) đã được caller quan sát hoặc
bên tiêu thụ (consumer / 소비자) đã xử lý. Với async luồng (flow / 흐름), phản hồi (response / 응답) chỉ xác nhận `accepted`; trạng thái
hoàn tất phải nằm trong job máy trạng thái (state machine / 상태 머신) có đơn vị sở hữu (owner / 오너) và retention.

### Ranh giới (boundary / 경계) và thất bại (failure / 실패) quyền sở hữu (ownership / 소유권)

Mỗi ranh giới (boundary / 경계) cần trả lời ba câu hỏi: ai sở hữu hết thời gian chờ (timeout / 타임아웃) và cancellation; trạng thái (state / 상태) nào
đã lần ghi nhận (commit / 커밋) nếu ranh giới (boundary / 경계) chết giữa chừng; caller có thể truy vấn (query / 쿼리) hoặc thử lại (retry / 재시도) thế nào.
Nếu cơ sở dữ liệu (database / 데이터베이스) lần ghi nhận (commit / 커밋) thành công nhưng publish sự kiện (event / 이벤트) thất bại, lỗi thuộc
transactional handoff và cần outbox/replay, không phải HTTP tầng (layer / 계층). Nếu proxy
hết thời gian chờ (timeout / 타임아웃) nhưng handler vẫn chạy, máy khách (client / 클라이언트) không được tự suy ra giao dịch (transaction / 트랜잭션) đã quay lui (rollback / 롤백).

### Admission điều khiển (control / 제어)

Trước lô-gic nghiệp vụ (business logic / 비즈니스 로직), máy chủ (server / 서버) có thể từ chối sớm vì body quá lớn, tỷ lệ (rate / 비율) limit,
liên kết (connection / 연결) pool cạn hoặc shutdown đang drain. Theo dõi `rejected_total`, queueing
thời gian (time / 시간) và active yêu cầu (request / 요청) count để phân biệt overload với lỗi lô-gic (logic / 논리).

### Cấu hình (configuration / 구성) và secrets

Cấu hình (configuration / 구성) có vòng đời (lifecycle / 생명주기) riêng: nguồn chuẩn (source of truth / 정본), precedence, kiểm tra hợp lệ (validation / 검증), rollout
và quay lui (rollback / 롤백). Tách immutable startup cấu hình (config / 설정) (port, schema compatibility) khỏi
động (dynamic / 동적) cấu hình (config / 설정) (feature flag, quota) và secret (credential, signing key). tiến trình (process / 프로세스)
nên thất bại (fail / 실패) fast với cấu hình (config / 설정) bắt buộc sai, nhưng không in giá trị secret vào exception,
startup log hay dấu vết (trace / 추적). Rotation cần overlap cửa sổ (window / 윈도우), phiên bản (version / 버전)/key ID và khả năng
revoke; không giả định restart mọi instance là một giao dịch (transaction / 트랜잭션) nguyên tử.

Môi trường (environment / 환경) variable là delivery cơ chế (mechanism / 메커니즘), không tự động là secret manager.
Ghi rõ ai được đọc cấu hình (config / 설정), cấu hình (config / 설정) thay đổi có kiểm tra (audit / 감사) nào, và instance đang chạy
phiên bản (version / 버전) nào. cấu hình (config / 설정) drift giữa cục bộ (local / 로컬)/staging/môi trường vận hành (production / 운영 환경) phải quan sát được như
một loại triển khai (deployment / 배포) thay đổi (change / 변경), không để gỡ lỗi (debug / 디버그) bằng cách sửa thủ công trong tiến trình (process / 프로세스).

### Bài tập suy luận

Vẽ timeline cho một `POST /orders` khi máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) ở 1.5 giây, cơ sở dữ liệu (database / 데이터베이스) lần ghi nhận (commit / 커밋)
ở giây 1.2 và sự kiện (event / 이벤트) publish thất bại ở giây 1.3. Đánh dấu phản hồi (response / 응답) caller thấy,
trạng thái (state / 상태) authoritative, thử lại (retry / 재시도) an toàn và chỉ số (metric / 지표) chứng minh từng kết luận.

> **Bàn giao:** Sau **Bài tập suy luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 http api semantics](./01_http_api_semantics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
