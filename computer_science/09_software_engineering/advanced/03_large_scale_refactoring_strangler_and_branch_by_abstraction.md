# Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu: môi trường vận hành (production / 운영 환경) không dừng để kiến trúc (architecture / 아키텍처) được thay** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. bất biến (invariant / 불변식) trước roadmap** để chuyển câu hỏi ấy thành điều kiện phải giữ. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Refactoring nhỏ có thể hoàn thành trong một lần ghi nhận (commit / 커밋). di chuyển (migration / 마이그레이션) lớn kéo dài tuần/tháng phải coexist với môi trường vận hành (production / 운영 환경) traffic, nhiều nhị phân (binary / 이진) versions, nhiều teams và trạng thái (state / 상태) đã tồn tại. Vấn đề chính chuyển từ “mã (code / 코드) mới đẹp hơn” sang **làm sao đi từ trạng thái (state / 상태) A tới trạng thái (state / 상태) B qua một chuỗi trạng thái trung gian luôn deployable, observable và recoverable**.

Mô hình tư duy (mental model / 사고 모델) trung tâm là: **di chuyển (migration / 마이그레이션) là một phân tán (distributed / 분산) máy trạng thái (state machine / 상태 머신) của mã (code / 코드) + dữ liệu (data / 데이터) + giao thức (protocol / 프로토콜) + traffic + quyền sở hữu (ownership / 소유권)**. Mỗi phase phải có bất biến (invariant / 불변식), nguồn chuẩn (source of truth / 정본), tính tương thích (compatibility / 호환성) quy tắc (rule / 규칙), bằng chứng (evidence / 증거) để chuyển phase và khôi phục (recovery / 복구) đường dẫn (path / 경로) nếu giả định (assumption / 가정) thất bại (fail / 실패).

## 1. Bài toán ban đầu: môi trường vận hành (production / 운영 환경) không dừng để kiến trúc (architecture / 아키텍처) được thay

Trong di chuyển (migration / 마이그레이션) dài, old hệ thống (system / 시스템) vẫn nhận bug fixes/tính năng (feature / 기능) changes; dữ liệu (data / 데이터) tiếp tục tăng; clients không cập nhật (update / 업데이트) atomically; deploy rollout mất thời gian.

Vì vậy “new hệ thống (system / 시스템) đúng ở final trạng thái (state / 상태)” chưa đủ. kỹ thuật (engineering / 엔지니어링) phải chứng minh:

```text
old-only state an toàn
coexist state an toàn
cutover state an toàn
new-only state an toàn
```

và transitions giữa chúng không làm mất/duplicate authority.

> **Chuyển mạch:** Production cannot pause for architecture; preserve invariants while strangler/branch-by-abstraction create small cutovers, avoiding the feedback delay and risk of a big-bang rewrite.

## 2. bất biến (invariant / 불변식) trước roadmap

Trước khi chọn strangler hay rewrite, viết invariants:

```text
mỗi order có đúng một source of truth tại mọi phase
old/new readers đều hiểu schema trong compatibility window
side effect không bị thực hiện hai lần bởi shadow/dual path
rollback không đọc state mà old binary không hiểu
traffic chỉ cutover khi correctness evidence đạt threshold
```

Nếu roadmap chỉ có tasks mà không có phase invariants, di chuyển (migration / 마이그레이션) khó biết khi nào thật sự an toàn để đi tiếp.

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **3. Big-bang rewrite tối đa hóa time-to-feedback và cutover rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **2. bất biến (invariant / 불변식) trước roadmap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Strangler di chuyển (migration / 마이그레이션) chuyển năng lực (capability / 역량) từng phần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Big-bang rewrite tối đa hóa time-to-feedback và cutover rủi ro (risk / 위험)

Rewrite toàn bộ hấp dẫn vì “thoát legacy các ràng buộc (constraints / 제약조건들)”. Nhưng trong thời gian new hệ thống (system / 시스템) chưa môi trường vận hành (production / 운영 환경), old hệ thống (system / 시스템) là moving mục tiêu (target / 대상).

Rủi ro (risk / 위험):

```text
feedback production đến muộn
semantic edge cases bị bỏ sót
migration data chỉ được test gần cuối
cutover blast radius lớn
rollback khó nếu schema/state đã đổi
```

Big-bang có thể hợp lý khi ranh giới (boundary / 경계) rất nhỏ/cô lập hoặc replacement gần như stateless. Nhưng phải chứng minh thay vì mặc định “rewrite sạch hơn”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **4. Strangler di chuyển (migration / 마이그레이션) chuyển năng lực (capability / 역량) từng phần** tiếp nhận điểm tựa từ **3. Big-bang rewrite tối đa hóa time-to-feedback và cutover rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Branch by lớp trừu tượng (abstraction / 추상화) giữ tích hợp (integration / 통합) trong mainline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Strangler di chuyển (migration / 마이그레이션) chuyển năng lực (capability / 역량) từng phần

**Strangler mẫu (pattern / 패턴)** đặt routing/facade seam rồi chuyển từng năng lực (capability / 역량) sang hiện thực (implementation / 구현) mới.

```text
client
  ↓
facade/router
  ├→ old path
  └→ new path
```

Lợi ích: môi trường vận hành (production / 운영 환경) phản hồi (feedback / 피드백) sớm, blast radius theo slice, quay lui (rollback / 롤백) traffic dễ hơn.

Điểm khó: nếu dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) vẫn dùng chung (shared / 공유) tùy ý, đường đi mã (code path / 코드 경로) tách nhưng bất biến (invariant / 불변식) vẫn coupled. Seam phải chọn theo năng lực (capability / 역량)/trạng thái (state / 상태) authority, không chỉ URL đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **5. Branch by lớp trừu tượng (abstraction / 추상화) giữ tích hợp (integration / 통합) trong mainline** tiếp nhận điểm tựa từ **4. Strangler di chuyển (migration / 마이그레이션) chuyển năng lực (capability / 역량) từng phần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Expand-contract là giao thức (protocol / 프로토콜) cho tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Branch by lớp trừu tượng (abstraction / 추상화) giữ tích hợp (integration / 통합) trong mainline

Thay vì long-lived Git branch, tạo lớp trừu tượng (abstraction / 추상화) để old/new implementations cùng tồn tại trong mainline.

Typical luồng (flow / 흐름):

```text
introduce abstraction
→ route old implementation through it
→ add new implementation
→ migrate callers/traffic gradually
→ remove old implementation
→ collapse temporary abstraction if no longer useful
```

Lợi ích là continuous tích hợp (integration / 통합) và giảm merge divergence. chi phí (cost / 비용) là temporary độ phức tạp (complexity / 복잡도) trong codebase; cần deadline/xóa di chuyển (migration / 마이그레이션) scaffolding để nó không thành permanent dual kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **6. Expand-contract là giao thức (protocol / 프로토콜) cho tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **5. Branch by lớp trừu tượng (abstraction / 추상화) giữ tích hợp (integration / 통합) trong mainline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. nguồn chuẩn (source of truth / 정본) phải duy nhất hoặc xung đột (conflict / 충돌) quy tắc (rule / 규칙) phải tường minh (explicit / 명시적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Expand-contract là giao thức (protocol / 프로토콜) cho tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)

Lược đồ (schema / 스키마)/API thay đổi (change / 변경) trong phân tán (distributed / 분산) triển khai (deployment / 배포) hiếm khi atomic. mẫu (pattern / 패턴):

```text
EXPAND:
new producer/consumer version vẫn compatible với old

MIGRATE:
rollout binaries, backfill data, change traffic/authority

CONTRACT:
remove old field/path only after no old reader/writer remains
```

Bất biến (invariant / 불변식) là **trong mỗi coexist cửa sổ (window / 윈도우), mọi live phiên bản (version / 버전) combination được phép phải hiểu trạng thái (state / 상태) đủ để giữ tính đúng đắn (correctness / 정확성)**.

Rename DB column trực tiếp có thể thất bại (fail / 실패) vì old nhị phân (binary / 이진) vẫn truy vấn (query / 쿼리) tên cũ. Add-new → dual-compatible → migrate → drop-old an toàn hơn nếu trạng thái (state / 상태) ngữ nghĩa (semantics / 의미론) được quản lý rõ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **6. Expand-contract là giao thức (protocol / 프로토콜) cho tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우)** nêu điều cần giải thích; **7. nguồn chuẩn (source of truth / 정본) phải duy nhất hoặc xung đột (conflict / 충돌) quy tắc (rule / 규칙) phải tường minh (explicit / 명시적)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Naive dual-write tạo atomicity gap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. nguồn chuẩn (source of truth / 정본) phải duy nhất hoặc xung đột (conflict / 충돌) quy tắc (rule / 규칙) phải tường minh (explicit / 명시적)

Một trong những câu nguy hiểm nhất là “tạm thời cả old và new đều authoritative”. Nếu cả hai accept writes, hệ thống (system / 시스템) cần phân tán (distributed / 분산) consistency/xung đột (conflict / 충돌) ngữ nghĩa (semantics / 의미론) thật sự.

Safer patterns thường chọn:

```text
old authoritative, new mirrors
→ compare
→ switch authority once
→ new authoritative, old fallback/read-only if possible
```

Nếu dual authority thật sự cần, xung đột (conflict / 충돌)/reconciliation phải được thiết kế như hệ thống phân tán (distributed system / 분산 시스템), không gọi nó là temporary di chuyển (migration / 마이그레이션) hack.

> **Chuyển mạch:** Trong **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **7. nguồn chuẩn (source of truth / 정본) phải duy nhất hoặc xung đột (conflict / 충돌) quy tắc (rule / 규칙) phải tường minh (explicit / 명시적)** nêu điều cần giải thích; **8. Naive dual-write tạo atomicity gap** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Dual-read có thể che divergence nếu fallback quá tiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Naive dual-write tạo atomicity gap

Ứng dụng (application / 애플리케이션) writes old DB rồi new DB:

```text
write old succeeds
write new fails
```

hoặc ngược lại. Không cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) nào cover hai stores nếu không dùng phân tán (distributed / 분산) giao thức (protocol / 프로토콜).

Outbox/CDC/log-based replication có thể chuyển bài toán (problem / 문제) thành durable sự kiện (event / 이벤트) + replay/idempotency, nhưng cũng cần lag/replay ngữ nghĩa (semantics / 의미론).

Dual-write chỉ an toàn khi thất bại (failure / 실패) trạng thái (state / 상태) và repair giao thức (protocol / 프로토콜) tường minh (explicit / 명시적).

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **9. Dual-read có thể che divergence nếu fallback quá tiện** tiếp nhận điểm tựa từ **8. Naive dual-write tạo atomicity gap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Dual-read có thể che divergence nếu fallback quá tiện

Mẫu (pattern / 패턴) “read new, nếu miss thì read old” giúp di chuyển (migration / 마이그레이션) nhưng có rủi ro (risk / 위험): new store thiếu dữ liệu (data / 데이터) lâu mà dịch vụ (service / 서비스) vẫn success nhờ fallback, khiến gap không được sửa.

Bằng chứng (evidence / 증거) nên tách:

```text
new hit
fallback-to-old rate
value mismatch rate
age of not-yet-backfilled records
```

Fallback là an toàn (safety / 안전) cơ chế (mechanism / 메커니즘), không nên biến thành permanent invisibility cloak cho di chuyển (migration / 마이그레이션) debt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **10. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) thật** tiếp nhận điểm tựa từ **9. Dual-read có thể che divergence nếu fallback quá tiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Shadow traffic cho bằng chứng (evidence / 증거) nhưng side effects phải bị cô lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) thật

Bản sao (copy / 복사) historical dữ liệu (data / 데이터) không chỉ là batch script. Backfill tranh CPU, I/O, locks, bộ nhớ đệm (cache / 캐시) và replication bandwidth với foreground traffic.

Cần:

```text
rate limit / pause-resume
checkpoint progress
idempotent writes
version/conflict rule với concurrent live updates
validation sampling/full comparison
replay after failure
```

Nếu row được cập nhật (update / 업데이트) trong lúc backfill bản sao (copy / 복사) old snapshot, last-write-wins naïve có thể overwrite fresh trạng thái (state / 상태) bằng historical trạng thái (state / 상태). thứ tự (ordering / 순서)/phiên bản (version / 버전) ranh giới (boundary / 경계) phải tường minh (explicit / 명시적).

> **Chuyển mạch:** Trong **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **10. Backfill là tải công việc (workload / 워크로드) môi trường vận hành (production / 운영 환경) thật** nêu điều cần giải thích; **11. Shadow traffic cho bằng chứng (evidence / 증거) nhưng side effects phải bị cô lập** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. Comparison phải biết ngữ nghĩa (semantics / 의미론), không chỉ byte equality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Shadow traffic cho bằng chứng (evidence / 증거) nhưng side effects phải bị cô lập

Shadowing gửi bản sao (copy / 복사) yêu cầu (request / 요청) sang new đường dẫn (path / 경로) và bỏ phản hồi (response / 응답). Nó giúp compare tính đúng đắn (correctness / 정확성)/hiệu năng (performance / 성능) với production-shaped đầu vào (input / 입력).

Nhưng shadow yêu cầu (request / 요청) không được duplicate real side tác động (effect / 효과): payment, email, bên ngoài (external / 외부) mutation, expensive downstream quota.

Có thể cần stub/sandbox side tác động (effect / 효과), read-only chế độ (mode / 모드) hoặc compare at a lower pure-computation ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **11. Shadow traffic cho bằng chứng (evidence / 증거) nhưng side effects phải bị cô lập** nêu điều cần giải thích; **12. Comparison phải biết ngữ nghĩa (semantics / 의미론), không chỉ byte equality** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. Cutover là authority chuyển tiếp (transition / 전이) có preconditions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Comparison phải biết ngữ nghĩa (semantics / 의미론), không chỉ byte equality

Old/new responses có thể khác thứ tự (ordering / 순서), generated id, timestamp hoặc formatting nhưng semantically equivalent.

Comparator nên classify:

```text
must equal exactly
set-equivalent/order-insensitive
within numeric tolerance
expected intentional difference
hard correctness mismatch
```

Nếu comparison quá strict, noise che tín hiệu (signal / 신호); quá loose, bug thật bị bỏ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **13. Cutover là authority chuyển tiếp (transition / 전이) có preconditions** tiếp nhận điểm tựa từ **12. Comparison phải biết ngữ nghĩa (semantics / 의미론), không chỉ byte equality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Reversibility phải xét mã (code / 코드) + dữ liệu (data / 데이터) + giao thức (protocol / 프로토콜)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Cutover là authority chuyển tiếp (transition / 전이) có preconditions

Một cutover gate tốt dựa bằng chứng (evidence / 증거):

```text
backfill complete to known frontier
live replication lag within bound
mismatch rate within accepted threshold
new capacity headroom tested
observability/on-call ready
rollback/roll-forward path rehearsed
old path can be fenced/read-only if needed
```

“mã (code / 코드) deployed 100%” không đồng nghĩa di chuyển (migration / 마이그레이션) complete.

> **Chuyển mạch:** Trong **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **13. Cutover là authority chuyển tiếp (transition / 전이) có preconditions** nêu điều cần giải thích; **14. Reversibility phải xét mã (code / 코드) + dữ liệu (data / 데이터) + giao thức (protocol / 프로토콜)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Irreversible step phải được nhận diện trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Reversibility phải xét mã (code / 코드) + dữ liệu (data / 데이터) + giao thức (protocol / 프로토콜)

Cờ tính năng (feature flag / 기능 플래그) tuyến (route / 경로) về old hiện thực (implementation / 구현) chỉ là quay lui (rollback / 롤백) nếu old hiện thực (implementation / 구현) vẫn hiểu hiện tại (current / 현재) dữ liệu (data / 데이터)/giao thức (protocol / 프로토콜).

Destructive di chuyển (migration / 마이그레이션) có thể làm nhị phân (binary / 이진) quay lui (rollback / 롤백) vô nghĩa:

```text
new code writes format old code cannot parse
→ toggle flag back
→ old code crashes/corrupts behavior
```

Reversibility cần backward-compatible trạng thái (state / 상태) hoặc a forward repair plan. Đôi khi **roll-forward** an toàn hơn quay lui (rollback / 롤백).

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **14. Reversibility phải xét mã (code / 코드) + dữ liệu (data / 데이터) + giao thức (protocol / 프로토콜)** nêu điều cần giải thích; **15. Irreversible step phải được nhận diện trước** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Traffic ramp phải đi cùng sức chứa (capacity / 용량) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Irreversible step phải được nhận diện trước

Examples:

```text
drop old column/data
re-encrypt/delete old key material
send external side effect
change public protocol clients cannot downgrade
reassign irreversible ownership
```

Sau irreversible ranh giới (boundary / 경계), khôi phục (recovery / 복구) plan thay đổi. Runbook phải nói rõ “quay lui (rollback / 롤백) no longer safe after step X”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **16. Traffic ramp phải đi cùng sức chứa (capacity / 용량) mô hình (model / 모델)** tiếp nhận điểm tựa từ **15. Irreversible step phải được nhận diện trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. di chuyển (migration / 마이그레이션) kéo theo khả năng quan sát (observability / 관측 가능성) versioned** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Traffic ramp phải đi cùng sức chứa (capacity / 용량) mô hình (model / 모델)

Canary 1% traffic không chứng minh new đường dẫn (path / 경로) chịu 100% nếu bottleneck xuất hiện phi tuyến: liên kết (connection / 연결) pool, bộ nhớ đệm (cache / 캐시) hit ratio, DB locks, queueing knee hoặc bên ngoài (external / 외부) quota.

Ramp cần quan sát:

```text
throughput
queue wait
p95/p99
resource saturation
error/mismatch
retry amplification
cache warm-up
```

Có thể cần staged ramp 1% → 5% → 25% → 50% → 100%, nhưng thresholds phải theo tải công việc (workload / 워크로드)/SLO chứ không học thuộc percentages.

> **Chuyển mạch:** Trong **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **17. di chuyển (migration / 마이그레이션) kéo theo khả năng quan sát (observability / 관측 가능성) versioned** tiếp nhận điểm tựa từ **16. Traffic ramp phải đi cùng sức chứa (capacity / 용량) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. thất bại (failure / 실패) modes cần được kiểm thử (test / 테스트) ở chuyển tiếp (transition / 전이), không chỉ endpoint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. di chuyển (migration / 마이그레이션) kéo theo khả năng quan sát (observability / 관측 가능성) versioned

Trong coexist phase, chỉ số (metric / 지표)/log/dấu vết (trace / 추적) phải biết yêu cầu (request / 요청) chạy old/new đường dẫn (path / 경로), lược đồ (schema / 스키마) phiên bản (version / 버전), dữ liệu (data / 데이터) nguồn (source / 소스) và di chuyển (migration / 마이그레이션) cohort.

Nếu dashboard gộp tất cả, regression 5% traffic có thể biến mất trong average.

Useful dimensions:

```text
implementation version/path
cohort/tenant/region
source-of-truth version
fallback used?
backfill generation
comparison result
```

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **18. thất bại (failure / 실패) modes cần được kiểm thử (test / 테스트) ở chuyển tiếp (transition / 전이), không chỉ endpoint** tiếp nhận điểm tựa từ **17. di chuyển (migration / 마이그레이션) kéo theo khả năng quan sát (observability / 관측 가능성) versioned** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. quyền sở hữu (ownership / 소유권) di chuyển (migration / 마이그레이션) là socio-technical chuyển tiếp trạng thái (state transition / 상태 전이)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. thất bại (failure / 실패) modes cần được kiểm thử (test / 테스트) ở chuyển tiếp (transition / 전이), không chỉ endpoint

Kiểm thử (test / 테스트) đáng giá:

```text
new write succeeds, replication fails
backfill crashes midway
old/new binaries coexist
rollback after partial rollout
queue/backlog grows during cutover
feature flag service unavailable
schema contract violation by stale client
region fails during migration
```

Di chuyển (migration / 마이그레이션) tính đúng đắn (correctness / 정확성) nằm ở transitions/failures, không chỉ final happy đường dẫn (path / 경로).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **19. quyền sở hữu (ownership / 소유권) di chuyển (migration / 마이그레이션) là socio-technical chuyển tiếp trạng thái (state transition / 상태 전이)** tiếp nhận điểm tựa từ **18. thất bại (failure / 실패) modes cần được kiểm thử (test / 테스트) ở chuyển tiếp (transition / 전이), không chỉ endpoint** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Temporary tính tương thích (compatibility / 호환성) có carrying chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. quyền sở hữu (ownership / 소유권) di chuyển (migration / 마이그레이션) là socio-technical chuyển tiếp trạng thái (state transition / 상태 전이)

Tách dịch vụ (service / 서비스) sang nhóm (team / 팀) mới nhưng on-call/lược đồ (schema / 스키마) kiến thức (knowledge / 지식)/runbook vẫn ở nhóm (team / 팀) cũ không tạo autonomy.

Quyền sở hữu (ownership / 소유권) handoff cần:

```text
code/repo ownership
data/schema authority
deploy permission
on-call/runbook
SLO and incident responsibility
consumer contracts
```

Nếu responsibility split mơ hồ, incidents sẽ tạo human coordination hàng đợi (queue / 큐).

> **Chuyển mạch:** Trong **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **20. Temporary tính tương thích (compatibility / 호환성) có carrying chi phí (cost / 비용)** tiếp nhận điểm tựa từ **19. quyền sở hữu (ownership / 소유권) di chuyển (migration / 마이그레이션) là socio-technical chuyển tiếp trạng thái (state transition / 상태 전이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Branching chiến lược (strategy / 전략) và di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) là hai concerns liên quan nhưng khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Temporary tính tương thích (compatibility / 호환성) có carrying chi phí (cost / 비용)

Dual paths, adapters, flags, duplicated schemas và fallback đều tăng cognitive tải (load / 로드). Nếu không có removal criterion, di chuyển (migration / 마이그레이션) scaffold trở thành permanent kiến trúc (architecture / 아키텍처).

Mỗi temporary cơ chế (mechanism / 메커니즘) cần:

```text
owner
delete condition
deadline hoặc trigger
metric proving old usage reached zero
```

Technical debt ở đây không phải mã (code / 코드) xấu; nó là **extra trạng thái (state / 상태) không gian (space / 공간)** mà nhóm (team / 팀) phải reason trong mỗi thay đổi (change / 변경)/sự cố (incident / 인시던트).

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **21. Branching chiến lược (strategy / 전략) và di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) là hai concerns liên quan nhưng khác** tiếp nhận điểm tựa từ **20. Temporary tính tương thích (compatibility / 호환성) có carrying chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. bằng chứng vận hành (production evidence / 운영 증거) cho di chuyển (migration / 마이그레이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Branching chiến lược (strategy / 전략) và di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) là hai concerns liên quan nhưng khác

Git short-lived branch/mainline tích hợp (integration / 통합) giảm mã (code / 코드) divergence. thời gian chạy (runtime / 런타임) branch-by-abstraction giảm môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) divergence bằng controllable tuyến (route / 경로).

Long-lived tính năng (feature / 기능) branch + big-bang thời gian chạy (runtime / 런타임) cutover thường trì hoãn tích hợp (integration / 통합) ở cả hai dimensions. Better di chuyển (migration / 마이그레이션) thường tích hợp mã (code / 코드) sớm nhưng expose hành vi (behavior / 동작) dần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **21. Branching chiến lược (strategy / 전략) và di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) là hai concerns liên quan nhưng khác** nêu điều cần giải thích; **22. bằng chứng vận hành (production evidence / 운영 증거) cho di chuyển (migration / 마이그레이션)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. quyết định (decision / 결정) gate nên dựa bất biến (invariant / 불변식) + bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. bằng chứng vận hành (production evidence / 운영 증거) cho di chuyển (migration / 마이그레이션)

Một di chuyển (migration / 마이그레이션) dashboard nên trả lời:

```text
Traffic: old/new percentage by cohort
Correctness: mismatch/repair/fallback rate
Data: backfill frontier, replication lag, missing/divergent records
Performance: latency/queue/saturation per path
Reliability: retries/errors by path
Compatibility: live client/schema versions
Ownership: active old dependencies/callers
```

Một chỉ số (metric / 지표) “di chuyển (migration / 마이그레이션) 80%” không có nghĩa gì nếu không biết 80% theo traffic, records, tenants, binaries hay features.

> **Chuyển mạch:** Trong **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **22. bằng chứng vận hành (production evidence / 운영 증거) cho di chuyển (migration / 마이그레이션)** nêu điều cần giải thích; **23. quyết định (decision / 결정) gate nên dựa bất biến (invariant / 불변식) + bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. quyết định (decision / 결정) gate nên dựa bất biến (invariant / 불변식) + bằng chứng (evidence / 증거)

Trước mỗi phase chuyển tiếp (transition / 전이), hỏi:

```text
Invariant nào phải đúng?
Evidence nào chứng minh nó?
Failure nào evidence chưa cover?
Nếu transition xong, rollback còn hợp lệ không?
Authority/source of truth thay đổi ở đâu?
Temporary mechanism nào có thể xóa?
```

Điều này biến di chuyển (migration / 마이그레이션) từ dự án (project / 프로젝트) checklist thành controlled máy trạng thái (state machine / 상태 머신).

> **Chuyển mạch:** Ở chặng này của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **23. quyết định (decision / 결정) gate nên dựa bất biến (invariant / 불변식) + bằng chứng (evidence / 증거)** nêu điều cần giải thích; **24. Mô hình tư duy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Mô hình tư duy

> Large-scale refactoring là **thiết kế chuỗi trạng thái trung gian an toàn**. Strangler và branch-by-abstraction giảm blast radius bằng coexistence; expand-contract quản tính tương thích (compatibility / 호환성); backfill/CDC quản trạng thái (state / 상태) movement; cutover chuyển authority; quay lui (rollback / 롤백) chỉ tồn tại khi mã (code / 코드) + dữ liệu (data / 데이터) + giao thức (protocol / 프로토콜) còn compatible. **Đích cuối quan trọng, nhưng kỹ thuật (engineering / 엔지니어링) difficulty nằm ở mọi chuyển tiếp (transition / 전이) phải có bất biến (invariant / 불변식), bằng chứng (evidence / 증거) và khôi phục (recovery / 복구) đường dẫn (path / 경로).**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Large-scale refactoring, strangler di chuyển (migration / 마이그레이션) và branch-by-abstraction**, **Kết nối** gom các mảnh từ **24. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [maintenance/refactoring foundation](../../basic/09_software_engineering/04_maintenance_evolution_and_technical_debt.md), đọc [architecture decisions/evolution](./00_architecture_decisions_evolution_and_socio_technical_constraints.md), [API/schema evolution](./02_api_schema_compatibility_and_evolutionary_design.md), [deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md), [schema/protocol contracts](../../08_software_systems/advanced/06_schema_protocol_evolution_and_compatibility_contracts.md), [system boundaries](../../08_software_systems/07_system_decomposition_services_and_boundaries.md) và [distributed transaction/outbox](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
