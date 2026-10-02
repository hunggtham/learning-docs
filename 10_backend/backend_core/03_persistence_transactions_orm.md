# 03. Persistence, giao dịch (transaction / 트랜잭션) và ORM

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **03. Persistence, giao dịch (transaction / 트랜잭션) và ORM**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ use trường hợp (case / 사례) đến chuyển tiếp trạng thái (state transition / 상태 전이)** đưa mô hình vào một trường hợp đủ cụ thể để quan sát; sau đó sang **ORM ranh giới (boundary / 경계)** để soi ranh giới và điểm dễ nhầm. Mạch này nối persistence với transaction và ORM, để phân biệt identity map, isolation, locking và hành vi SQL thực tế.

## Từ use trường hợp (case / 사례) đến chuyển tiếp trạng thái (state transition / 상태 전이)

Persistence không bắt đầu từ thực thể (entity / 엔터티) annotation. Bắt đầu bằng bất biến (invariant / 불변식): trạng thái (state / 상태)
nào phải cùng thay đổi, uniqueness nào phải được bảo vệ, và lúc nào dữ liệu được
coi là committed. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) nên bao quanh một use trường hợp (case / 사례) có tính nguyên
tử, không mặc định bao quanh toàn bộ yêu cầu (request / 요청) nếu yêu cầu (request / 요청) còn gọi remote dịch vụ (service / 서비스).

```text
input → validate command → load state → decide transition
      → write state + audit/outbox → commit
```

Cơ sở dữ liệu (database / 데이터베이스) ràng buộc (constraint / 제약조건) là lớp bảo vệ cuối cùng cho uniqueness, foreign key và check
bất biến (invariant / 불변식); ứng dụng (application / 애플리케이션) kiểm tra hợp lệ (validation / 검증) chỉ cải thiện thông báo lỗi. Chọn isolation
theo anomaly cần ngăn, không theo khẩu hiệu “strongest luôn tốt nhất”.

> **Chuyển mạch:** Trong **03. Persistence, giao dịch (transaction / 트랜잭션) và ORM**, trường hợp ở **Từ use trường hợp (case / 사례) đến chuyển tiếp trạng thái (state transition / 상태 전이)** cho thấy quy tắc hoạt động; **ORM ranh giới (boundary / 경계)** kiểm tra nơi quy tắc ấy không còn áp dụng hoặc dễ bị hiểu nhầm. Từ đây, **Remote side tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ORM ranh giới (boundary / 경계)

ORM giúp ánh xạ (mapping / 매핑) đối tượng (object / 객체)/bản ghi (record / 레코드) và quản lý đơn vị (unit / 단위) of công việc (work / 작업), nhưng không che được
kế hoạch truy vấn (query plan / 쿼리 계획), khóa (lock / 잠금), giao dịch (transaction / 트랜잭션) hay cardinality. rà soát (review / 검토) generated SQL. Tránh:

- N+1 truy vấn (query / 쿼리) do lazy relationship trong vòng lặp;
- trả thực thể (entity / 엔터티) trực tiếp làm lộ trường dữ liệu (field / 필드) và kéo cả đồ thị (graph / 그래프);
- giao dịch (transaction / 트랜잭션) đã đóng nhưng proxy còn lazy-load;
- bulk cập nhật (update / 업데이트) bỏ qua lĩnh vực (domain / 도메인) sự kiện (event / 이벤트)/kiểm tra (audit / 감사);
- di chuyển (migration / 마이그레이션) lược đồ (schema / 스키마) không tương thích với mã (code / 코드) đang chạy.

Đọc mô hình (model / 모델) bằng DTO/projection khi cần API ổn định. Dùng di chuyển (migration / 마이그레이션) versioned,
backward-compatible (expand → migrate → contract) cho deploy rolling.

> **Chuyển mạch:** Ở chặng này của **03. Persistence, giao dịch (transaction / 트랜잭션) và ORM**, **ORM ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **Remote side tác động (effect / 효과)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Đào sâu: giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và thất bại (failure / 실패) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Remote side tác động (effect / 효과)

Không giữ cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) mở trong lúc chờ payment/API khác. Dùng outbox,
saga hoặc trạng thái pending tùy bất biến (invariant / 불변식). Nếu lần ghi nhận (commit / 커밋) thành công nhưng gửi sự kiện (event / 이벤트)
thất bại, phải có cơ chế thử lại (retry / 재시도) và quan sát được; nếu gửi trước lần ghi nhận (commit / 커밋), bên tiêu thụ (consumer / 소비자)
có thể nhìn thấy trạng thái (state / 상태) chưa tồn tại.

Chi tiết ACID, MVCC, WAL và truy vấn (query / 쿼리) thực thi (execution / 실행) thuộc [Data & Databases](../../computer_science/05_data_databases/README.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03. Persistence, giao dịch (transaction / 트랜잭션) và ORM**, **Remote side tác động (effect / 효과)** đã nêu tiêu chí phân biệt, còn **Đào sâu: giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và thất bại (failure / 실패) ma trận (matrix / 행렬)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Bài tập suy luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đào sâu: giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và thất bại (failure / 실패) ma trận (matrix / 행렬)

Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) nên được kiểm tra bằng ma trận thay vì annotation. Với mỗi
thao tác (operation / 연산), ghi bước nào nằm trong giao dịch (transaction / 트랜잭션) và trạng thái (state / 상태) nào còn tồn tại nếu tiến trình (process / 프로세스)
chết sau bước đó:

| Bước | ranh giới (boundary / 경계) | Nếu tiến trình (process / 프로세스) chết |
|---|---|---|
| validate command | ngoài | không có trạng thái (state / 상태) |
| ghi aggregate | trong | lần ghi nhận (commit / 커밋) hoặc quay lui (rollback / 롤백) |
| ghi outbox | trong | sự kiện (event / 이벤트) còn để dispatcher đọc |
| gọi payment API | ngoài | cần idempotency/truy vấn (query / 쿼리) status |
| cập nhật projection | thường ngoài | replay từ sự kiện (event / 이벤트) |

Nếu bất biến (invariant / 불변식) yêu cầu hai row cùng đúng, ràng buộc (constraint / 제약조건)/giao dịch (transaction / 트랜잭션) phải bảo vệ chúng.
Nếu bất biến (invariant / 불변식) kéo dài qua dịch vụ (service / 서비스) hoặc thời gian, dùng máy trạng thái (state machine / 상태 머신) và
reconciliation thay vì cố kéo một giao dịch (transaction / 트랜잭션) phân tán.

Đọc rồi ghi trong hai giao dịch (transaction / 트랜잭션) riêng có thể mất cập nhật (update / 업데이트) dù mỗi giao dịch (transaction / 트랜잭션) đều
thành công. Chọn optimistic phiên bản (version / 버전) check khi xung đột (conflict / 충돌) hiếm; chọn locking khi
trọng yếu (critical / 중요) section ngắn và xung đột (conflict / 충돌) thường xuyên. Đo khóa (lock / 잠금) wait, deadlock và
giao dịch (transaction / 트랜잭션) duration thay vì chỉ nhìn thông lượng (throughput / 처리량).

> **Chuyển mạch:** Trong **03. Persistence, giao dịch (transaction / 트랜잭션) và ORM**, **Đào sâu: giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và thất bại (failure / 실패) ma trận (matrix / 행렬)** đã nêu tiêu chí phân biệt, còn **Bài tập suy luận** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết (connection / 연결) pool và read consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bài tập suy luận

Thiết kế di chuyển (migration / 마이그레이션) thêm `status=ARCHIVED` trong rolling deploy: lược đồ (schema / 스키마) expand,
mã (code / 코드) tương thích, backfill, chỉ mục (index / 인덱스) rollout, đặc tả hợp đồng (contract / 계약) và quay lui (rollback / 롤백) nếu backfill mới
chạy 30%.

> **Chuyển mạch:** Bài tập rolling deploy đã đặt migration và rollback vào một tình huống có rủi ro thật. **Liên kết (connection / 연결) pool và read consistency** tiếp tục ở lớp vận hành: pool chia sẻ ngân sách concurrency, còn replica tạo ra một consistency contract riêng.

## Liên kết (connection / 연결) pool và read consistency

Liên kết (connection / 연결) pool là dùng chung (shared / 공유) tính đồng thời (concurrency / 동시성) ngân sách (budget / 예산), không phải cách làm cho cơ sở dữ liệu (database / 데이터베이스)
nhanh hơn. Pool quá lớn gây contention và làm cơ sở dữ liệu (database / 데이터베이스) chết nhanh hơn; quá nhỏ
tạo queueing trong ứng dụng (application / 애플리케이션). Theo dõi active/idle/awaiting connections,
acquire độ trễ (latency / 지연 시간), giao dịch (transaction / 트랜잭션) duration và hết thời gian chờ (timeout / 타임아웃) theo pool.

Read replica tạo thêm consistency đặc tả hợp đồng (contract / 계약). Sau một ghi (write / 쓰기), read-your-write có
thể cần primary tuyến (route / 경로), session stickiness hoặc phiên bản (version / 버전) đơn vị từ (token / 토큰); không nên giấu
replica lag bằng thử lại (retry / 재시도) vô hạn. Nếu endpoint chấp nhận eventual consistency, trả
phiên bản (version / 버전)/updated-at để máy khách (client / 클라이언트) biết dữ liệu có thể chưa phản ánh mutation mới.

Dữ liệu (data / 데이터) retention là một phần của lược đồ (schema / 스키마) vòng đời (lifecycle / 생명주기): partition/archival, delete
cascade, kiểm tra (audit / 감사) retention và backup expiry phải được thiết kế cùng di chuyển (migration / 마이그레이션).
Không dùng ORM cascade như bằng chứng rằng mọi bản sao, bộ nhớ đệm (cache / 캐시) hay sự kiện (event / 이벤트) đã được
xóa.

> **Bàn giao:** Sau **Liên kết (connection / 연결) pool và read consistency**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
