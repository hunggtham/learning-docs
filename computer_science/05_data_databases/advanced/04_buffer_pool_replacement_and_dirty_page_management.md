# Buffer pool, replacement và dirty-page management

> **Mạch đọc:** Đặt **Buffer pool, replacement và dirty-page management** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Bài toán ban đầu: RAM nhỏ hơn cơ sở dữ liệu (database / 데이터베이스), nhưng độ trễ (latency / 지연 시간) lưu trữ (storage / 저장소) đắt** sang **2. Bảng trang (page table / 페이지 테이블) nối logical page id với vật lý (physical / 물리적) frame**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Cơ sở dữ liệu (database / 데이터베이스) không thể giả định toàn bộ dữ liệu (data / 데이터) nằm trong RAM. **Buffer pool** là page bộ nhớ đệm (cache / 캐시) do cơ sở dữ liệu (database / 데이터베이스) quản lý để giữ working set gần CPU, bảo vệ page thời gian tồn tại (lifetime / 수명) khi operators đang dùng, phối hợp dirty dữ liệu (data / 데이터) với WAL, và kiểm soát khi foreground tải công việc (workload / 워크로드) phải trả I/O chi phí (cost / 비용).

Mô hình tư duy (mental model / 사고 모델) quan trọng hơn “buffer pool là bộ nhớ đệm (cache / 캐시)”: **mỗi page có một vòng đời (lifecycle / 생명주기) và một durability frontier**. Replacement quyết định page nào mất residency; pin/latch bảo vệ quyền sở hữu (ownership / 소유권); dirty trạng thái (state / 상태) nối page với WAL; checkpoint/writeback quyết định khôi phục (recovery / 복구) debt; bộ nhớ (memory / 메모리) pressure quyết định khi nào độ trễ (latency / 지연 시간) chuyển từ hit-dominated sang I/O-dominated.

## 1. Bài toán ban đầu: RAM nhỏ hơn cơ sở dữ liệu (database / 데이터베이스), nhưng độ trễ (latency / 지연 시간) lưu trữ (storage / 저장소) đắt

Nếu mỗi logical read phải đọc lưu trữ (storage / 저장소), độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량) sẽ rất tệ. Buffer pool giữ hot pages resident và dùng locality của tải công việc (workload / 워크로드).

Nhưng bộ nhớ đệm (cache / 캐시) của DB khác generic key-value bộ nhớ đệm (cache / 캐시) vì page có thể:

```text
đang được operator dùng
đang bị update
chứa uncommitted bytes
phụ thuộc vào WAL chưa durable
đang được flush
được nhiều sessions cùng reference
```

Replacement vì vậy phải tôn trọng giao dịch (transaction / 트랜잭션)/khôi phục (recovery / 복구) invariants, không chỉ “evict key ít dùng”.

## 2. Bảng trang (page table / 페이지 테이블) nối logical page id với vật lý (physical / 물리적) frame

Engine thường cần ánh xạ (mapping / 매핑):

```text
(database/file id, page id)
→ buffer frame in RAM
```

Khi lookup hit, truy vấn (query / 쿼리) dùng frame hiện có. Khi miss, engine phải chọn victim hoặc free frame, thực hiện I/O và install ánh xạ (mapping / 매핑) mới.

Tính đồng thời (concurrency / 동시성) làm chuyển tiếp (transition / 전이) này khó hơn: hai threads cùng miss một page không nên đọc hai copies độc lập rồi cùng publish như authoritative frame. Bảng trang (page table / 페이지 테이블)/latch/load-state cần bảo đảm một logical page có biểu diễn (representation / 표현) resident nhất quán theo thiết kế (design / 설계).

## 3. Pinning giữ residency; latch/khóa (lock / 잠금) giải vấn đề khác

**Pin/tham chiếu (reference / 참조) count** thường ngăn replacement lấy frame đang được thao tác (operation / 연산) sử dụng.

**Latch** bảo vệ in-memory cấu trúc dữ liệu (data structure / 자료구조)/page cấu trúc (structure / 구조) trong thời gian rất ngắn.

**giao dịch (transaction / 트랜잭션) khóa (lock / 잠금)/MVCC** bảo vệ logical tính đồng thời (concurrency / 동시성) ngữ nghĩa (semantics / 의미론) lâu hơn.

Ba cơ chế (mechanism / 메커니즘) dễ bị trộn:

```text
pin    -> page có được evict không?
latch  -> threads có được mutate in-memory structure cùng lúc không?
lock/MVCC -> transaction nào được đọc/ghi logical state nào?
```

Pin leak có thể làm effective pool sức chứa (capacity / 용량) giảm dần dù configured buffer kích thước (size / 크기) không đổi.

## 4. Page vòng đời (lifecycle / 생명주기) là một máy trạng thái (state machine / 상태 머신)

Một simplified vòng đời (lifecycle / 생명주기):

```text
not resident
→ read requested
→ I/O in flight
→ clean resident
→ pinned/used
→ dirty resident
→ flush eligible when WAL rule satisfied
→ write in flight
→ clean resident
→ victim/evicted
```

Transitions có thể overlap/concurrent tùy hiện thực (implementation / 구현). lập luận (reasoning / 추론) theo máy trạng thái (state machine / 상태 머신) giúp gỡ lỗi (debug / 디버그) “page vẫn dirty”, “victim không chọn được”, “flush backlog tăng” tốt hơn việc chỉ nhìn hit ratio.

## 5. Replacement chính sách (policy / 정책) đang dự đoán future reuse

Pure LRU dễ bị sequential scan lớn pollute working set: hàng triệu pages chỉ đọc một lần đẩy hot OLTP chỉ mục (index / 인덱스)/gốc (root / 루트)/leaf pages ra ngoài.

Cơ sở dữ liệu (database / 데이터베이스) thường dùng clock, LRU-K, 2Q-like, scan-resistant hoặc engine-specific chính sách (policy / 정책) để ước lượng reuse bằng recency/frequency/lịch sử (history / 이력).

Không có replacement “best” universal. tải công việc (workload / 워크로드) quyết định:

```text
OLTP random hot set
sequential analytical scan
mixed read/write
index-heavy vs heap-heavy
multi-tenant working sets
```

Chính sách (policy / 정책) tốt phải tránh một tải công việc (workload / 워크로드) one-shot phá bộ nhớ đệm (cache / 캐시) của tải công việc (workload / 워크로드) latency-sensitive.

## 6. Dirty page là deferred ghi (write / 쓰기) debt

Khi page bị cập nhật (update / 업데이트), frame trở thành dirty. Engine trì hoãn flush để batch/merge writes và tránh random synchronous I/O mỗi giao dịch (transaction / 트랜잭션).

Đổi lại, dirty page là **ghi (write / 쓰기) debt**: trước khi frame bị evict/reused hoặc trước khôi phục (recovery / 복구) mục tiêu (target / 대상) nào đó, bytes phải được xử lý theo durability giao thức (protocol / 프로토콜).

Bất biến (invariant / 불변식) WAL:

> WAL records giải thích page trạng thái (state / 상태) phải durable đủ trước khi dirty page tương ứng được phép persistent theo write-ahead quy tắc (rule / 규칙).

Buffer manager vì vậy không thể tách khỏi log manager.

## 7. Dirty-page frontier và WAL frontier phải có thứ tự (ordering / 순서)

Giả sử page có `pageLSN = 500`. Nếu durable WAL mới tới LSN 450, flush page 500 ra stable lưu trữ (storage / 저장소) có thể phá khôi phục (recovery / 복구) bất biến (invariant / 불변식).

Conceptually:

```text
durableWAL >= pageLSN
→ page eligible for safe flush
```

Chính xác (exact / 정확한) siêu dữ liệu (metadata / 메타데이터) khác engine, nhưng mô hình tư duy (mental model / 사고 모델) này rất mạnh: page trạng thái (state / 상태) có một phụ thuộc (dependency / 의존성) lên log trạng thái (state / 상태).

Đọc [MVCC, WAL và recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md).

## 8. Flush không đồng nghĩa lần ghi nhận (commit / 커밋) và lần ghi nhận (commit / 커밋) không đồng nghĩa page flush

Dữ liệu (data / 데이터) page có thể flush trước giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋) nếu khôi phục (recovery / 복구) có undo/visibility siêu dữ liệu (metadata / 메타데이터) phù hợp (steal). Ngược lại committed giao dịch (transaction / 트랜잭션) không cần dữ liệu (data / 데이터) pages flush ngay nếu WAL đủ để redo (no-force).

Do đó hai đồ thị (graph / 그래프):

```text
commit latency
page writeback latency
```

có liên hệ nhưng không phải một chỉ số (metric / 지표). lần ghi nhận (commit / 커밋) thường nhạy WAL flush; checkpoint/eviction lại nhạy dirty-page writeback.

## 9. Checkpoint là cơ chế (mechanism / 메커니즘) trả khôi phục (recovery / 복구) debt có kiểm soát

Checkpoint giới hạn WAL/lịch sử (history / 이력) khôi phục (recovery / 복구) cần scan và thường phối hợp dirty-page flushing.

Nếu checkpoint flush quá aggressive:

```text
background writes burst
→ storage queue sâu
→ foreground WAL/data I/O chậm
→ transaction latency spike
```

Nếu quá lazy:

```text
dirty backlog + WAL retention ↑
→ recovery time/RTO ↑
→ disk space pressure ↑
```

Thiết kế tốt cố smooth writes theo thời gian thay vì tạo cliff định kỳ.

## 10. Background writer và foreground eviction có mục tiêu khác nhau

Background flushing cố biến dirty pages thành clean trước khi foreground luồng thực thi (thread / 스레드) cần frame. Nếu pool hết clean victims, yêu cầu (request / 요청) miss có thể phải tự chờ flush rồi mới reuse frame.

Đây là chuyển tiếp (transition / 전이) quan trọng:

```text
healthy: miss → choose clean victim → read page
pressure: miss → all victims dirty/pinned → wait for writeback → read page
```

Tail độ trễ (latency / 지연 시간) thường tăng mạnh khi hệ thống (system / 시스템) đi vào phase thứ hai dù hit ratio thay đổi ít.

## 11. Sequential scan và admission vào bộ nhớ đệm (cache / 캐시)

Không phải mọi page đọc vào đều nên có cùng bộ nhớ đệm (cache / 캐시) priority. Một scan 500 GB có thể có reuse gần zero trong OLTP timeframe.

Scan-resistant chính sách (policy / 정책), separate pools hoặc bypass/admission lô-gic (logic / 논리) có thể bảo vệ hot set. Câu hỏi thiết kế (design / 설계) là:

> Page này có xác suất reuse trước khi eviction pressure quay lại đủ cao để đáng chiếm frame không?

Đây là cùng family với bộ nhớ đệm (cache / 캐시) admission trong software các hệ thống (systems / 시스템들).

## 12. Buffer pool và kế hoạch truy vấn (query plan / 쿼리 계획) tạo phản hồi (feedback / 피드백) lẫn nhau

Optimizer ước lượng I/O/chi phí (cost / 비용) dựa statistics/mô hình (model / 모델), nhưng actual residency làm thời gian chạy (runtime / 런타임) khác nhau. chỉ mục (index / 인덱스) nested-loop có thể tuyệt vời với hot inner pages và tệ với random lưu trữ (storage / 저장소) misses.

Ngược lại plan chosen cũng thay bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태): full scan có thể pollute bộ nhớ đệm (cache / 캐시); băm (hash / 해시) phép nối (join / 조인) có thể dùng nhiều bộ nhớ (memory / 메모리) và spill; large sort có thể cạnh tranh buffer bộ nhớ (memory / 메모리)/I/O.

Do đó benchmark warm bộ nhớ đệm (cache / 캐시) và cold bộ nhớ đệm (cache / 캐시) trả lời hai tải công việc (workload / 워크로드) khác nhau. môi trường vận hành (production / 운영 환경) cần biết working-set evolution chứ không chỉ plan văn bản (text / 텍스트).

## 13. Double buffering: DB bộ nhớ đệm (cache / 캐시) và OS page bộ nhớ đệm (cache / 캐시) có thể cùng giữ dữ liệu (data / 데이터)

Với buffered I/O:

```text
DB buffer pool
↔ OS page cache
↔ filesystem/storage
```

cùng khối (block / 블록) có thể tồn tại ở hai bộ nhớ đệm (cache / 캐시) layers. Điều này đơn giản hóa một số I/O hành vi (behavior / 동작) nhưng duplicate bộ nhớ (memory / 메모리) và làm engine ít kiểm soát chính xác (exact / 정확한) ghi (write / 쓰기)/readahead đường dẫn (path / 경로) hơn.

Direct I/O có thể tránh double caching nhưng engine phải tự lo alignment, async scheduling, readahead và thời gian tồn tại (lifetime / 수명). Đây là thiết kế (design / 설계) sự đánh đổi (trade-off / 트레이드오프), không phải “direct luôn nhanh hơn”.

## 14. bộ nhớ (memory / 메모리) pressure phải tính toàn tiến trình (process / 프로세스) + OS, không riêng pool

Configured buffer pool quá lớn có thể làm OS thiếu bộ nhớ (memory / 메모리) cho page tables, stacks, filesystem siêu dữ liệu (metadata / 메타데이터), mạng (network / 네트워크) buffers, thời gian chạy (runtime / 런타임) vùng nhớ động (heap / 힙)/off-heap hoặc background tools.

Khi kernel reclaim/swapping bắt đầu, độ trễ (latency / 지연 시간) có thể tăng phi tuyến. cơ sở dữ liệu (database / 데이터베이스) nhìn “buffer pool hit cao” nhưng host vẫn thrash do tổng working set vượt RAM.

Lower-layer bằng chứng (evidence / 증거) cần gồm host bộ nhớ (memory / 메모리)/reclaim, không chỉ DB bộ nhớ đệm (cache / 캐시) metrics.

## 15. NUMA và locality ảnh hưởng in-memory DB hành vi (behavior / 동작)

Trên multi-socket host, buffer frames có vật lý (physical / 물리적) NUMA placement. Threads trên socket khác truy cập remote bộ nhớ (memory / 메모리) tốn độ trễ (latency / 지연 시간)/bandwidth interconnect.

Một dùng chung (shared / 공유)/toàn cục (global / 전역) buffer siêu dữ liệu (metadata / 메타데이터) khóa (lock / 잠금) hoặc hot page cũng có thể tạo cache-line contention dù lưu trữ (storage / 저장소) không tham gia.

Khi dữ liệu (data / 데이터) đã hot trong RAM, lower lớp trừu tượng (abstraction / 추상화) quyết định p99 có thể là NUMA/coherence chứ không phải SSD.

## 16. Multi-tenant noisy neighbor trong buffer pool

Hai tenants cùng pool có thể cạnh tranh working set. Một tenant scan lớn hoặc burst ghi (write / 쓰기) có thể:

```text
evict tenant khác
consume dirty-page budget
consume I/O queue
increase checkpoint pressure
```

Fairness cần gắn với tài nguyên (resource / 자원) thật: bộ nhớ đệm (cache / 캐시) admission/quota, I/O scheduling, tải công việc (workload / 워크로드) classes hoặc separate pools khi cần. “Tenant priority” trong yêu cầu (request / 요청) siêu dữ liệu (metadata / 메타데이터) không đủ nếu buffer/I/O tầng (layer / 계층) không enforce.

Đây là liên kết (connection / 연결) từ buffer manager sang system-level isolation.

## 17. hiệu năng (performance / 성능) pressure làm hành vi (behavior / 동작) đổi phase

Một useful phase mô hình (model / 모델):

```text
Phase A: working set fits → hits dominate
Phase B: misses increase → storage reads visible
Phase C: dirty/victim pressure → foreground waits for flush
Phase D: memory/I/O saturation → queue + checkpoint/reclaim feedback
```

Average độ trễ (latency / 지연 시간) ở phase A không dự đoán phase C/D. sức chứa (capacity / 용량) kiểm thử (test / 테스트) phải tăng tải (load / 로드)/working set đủ để tìm knee.

## 18. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) nên đo máy trạng thái (state machine / 상태 머신) thay vì một hit ratio:

```text
Residency:
- buffer hit/miss by object/workload
- resident pages / free frames
- pinned/busy frames
- eviction/victim scan cost

Dirty/writeback:
- dirty-page count/ratio
- flush rate and latency
- checkpoint age/duration
- foreground flush/wait events

WAL/storage:
- durable WAL frontier / flush latency
- storage read/write latency distribution
- queue depth/utilization

Host:
- memory pressure/reclaim/swap
- NUMA local/remote memory khi relevant
```

Một hit ratio 99% vẫn có thể che 1% misses cực đắt nằm trên đường găng (critical path / 임계 경로) của p99 requests.

## 19. thất bại (failure / 실패) lập luận (reasoning / 추론) theo lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)

Nếu truy vấn (query / 쿼리) cold chậm, kiểm tra miss/lưu trữ (storage / 저장소) đường dẫn (path / 경로). Nếu độ trễ (latency / 지연 시간) spike theo chu kỳ, correlate checkpoint/writeback. Nếu buffer pool lớn hơn mà thông lượng (throughput / 처리량) giảm, kiểm tra host reclaim/double caching/NUMA. Nếu lần ghi nhận (commit / 커밋) p99 tăng, đừng mặc định buffer pool; tách WAL flush khỏi data-page writeback. Nếu one tenant gây sự cố (incident / 인시던트), tìm bộ nhớ đệm (cache / 캐시)/I/O quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계).

## 20. Mô hình tư duy

> Buffer pool là **working-memory và write-debt manager** của lưu trữ (storage / 저장소) engine. Replacement dự đoán reuse; pin/latch giữ page thời gian tồn tại (lifetime / 수명) và in-memory tính đúng đắn (correctness / 정확성); dirty trạng thái (state / 상태) nối page với WAL; checkpoint/background writer trả khôi phục (recovery / 복구) debt; bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소) pressure quyết định khi foreground bắt đầu chờ. **Hit ratio chỉ là một symptom-level chỉ số (metric / 지표); page vòng đời (lifecycle / 생명주기) và tài nguyên (resource / 자원) frontier mới giải thích hành vi (behavior / 동작).**

## Kết nối

Ôn [database storage foundation](../../basic/05_data_databases/04_storage_logs_recovery_and_durability.md), đọc [MVCC/WAL](./00_mvcc_visibility_wal_and_recovery_internals.md), [B+Tree pages](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md), [OS memory pressure](../../03_operating_systems/advanced/02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mvcc visibility wal and recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
