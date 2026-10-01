# Đường đi của durability: ứng dụng (application / 애플리케이션) giao dịch (transaction / 트랜잭션) → MVCC/WAL → filesystem → lưu trữ (storage / 저장소) → replication

> **Mạch đọc:** [README](./README.md) là owner của tuyến durability nâng cao trong Khoa học máy tính. File theo một câu hỏi duy nhất: acknowledgement đang hứa mức sống sót nào, và bằng chứng ở tầng dưới có đủ cho lời hứa đó không? Vì vậy mạch đi từ visibility/commit sang WAL, filesystem, thiết bị, replication rồi tới bằng chứng vận hành và crash test.


Khi ứng dụng (application / 애플리케이션) nhận `COMMIT OK`, câu hỏi đúng không phải chỉ là “cơ sở dữ liệu (database / 데이터베이스) đã ghi xuống disk chưa?”. Một giao dịch (transaction / 트랜잭션) đi qua nhiều máy trạng thái (state machine / 상태 머신) và nhiều thất bại (failure / 실패) ranh giới (boundary / 경계): ứng dụng (application / 애플리케이션) giao dịch (transaction / 트랜잭션), MVCC/khóa (lock / 잠금) trạng thái (state / 상태), WAL, buffer pool, kernel page bộ nhớ đệm (cache / 캐시) hoặc direct-I/O đường dẫn (path / 경로), filesystem/khối (block / 블록) tầng (layer / 계층), controller, non-volatile media và có thể cả replication giao thức (protocol / 프로토콜).

Muốn hiểu **độ bền dữ liệu (durability / 내구성)** phải xác định chính xác bất biến (invariant / 불변식) nào được giữ tại từng tầng và acknowledgement ở tầng trên được phép phát ra sau bằng chứng (evidence / 증거) nào ở tầng dưới.

## 1. bất biến (invariant / 불변식) cốt lõi: acknowledgement không được mạnh hơn trạng thái (state / 상태) đã đạt

Một durability đặc tả hợp đồng (contract / 계약) có thể phát biểu như sau:

> Sau khi hệ thống trả success cho một giao dịch (transaction / 트랜잭션) ở durability mức (level / 수준) X, mọi thất bại (failure / 실패) nằm trong thất bại (failure / 실패) mô hình (model / 모델) của X phải vẫn cho phép khôi phục (recovery / 복구) một lịch sử chứa giao dịch (transaction / 트랜잭션) đó đúng theo consistency đặc tả hợp đồng (contract / 계약).

Điều này quan trọng vì “thất bại (failure / 실패) mô hình (model / 모델)” khác nhau giữa các chế độ (mode / 모드). cục bộ (local / 로컬) durable lần ghi nhận (commit / 커밋) có thể chỉ bảo vệ tiến trình (process / 프로세스)/host crash với lưu trữ (storage / 저장소) còn nguyên. Synchronous replicated lần ghi nhận (commit / 커밋) có thể yêu cầu survive mất leader hoặc cả một miền lỗi (failure domain / 장애 도메인). Async lần ghi nhận (commit / 커밋) có thể chủ động chấp nhận một cửa sổ mất dữ liệu.

Không nên dùng từ `commit` mà bỏ qua phần đặc tả hợp đồng (contract / 계약) này.

## 2. giao dịch (transaction / 트랜잭션) visibility và durability là hai trục khác nhau

MVCC trả lời **phiên bản (version / 버전) nào được phép nhìn thấy**; WAL/khôi phục (recovery / 복구) trả lời **lịch sử (history / 이력) nào sống sót sau crash**. Hai subsystem gặp nhau ở giao dịch (transaction / 트랜잭션) định danh (identity / 식별자) và lần ghi nhận (commit / 커밋) trạng thái (state / 상태).

Một phiên bản (version / 버전) có thể đã tồn tại trong buffer pool nhưng chưa được giao dịch (transaction / 트랜잭션) khác phép nhìn thấy. Một dữ liệu (data / 데이터) page có thể đã được ghi ra lưu trữ (storage / 저장소) dù giao dịch (transaction / 트랜잭션) tạo thay đổi trên đó chưa lần ghi nhận (commit / 커밋); khôi phục (recovery / 복구) phải dùng WAL/undo/giao dịch (transaction / 트랜잭션) siêu dữ liệu (metadata / 메타데이터) để không biến trạng thái (state / 상태) vật lý thành trạng thái (state / 상태) lô-gic (logic / 논리) hợp lệ một cách sai lầm.

Do đó bất biến (invariant / 불변식) không phải “disk luôn chỉ chứa committed dữ liệu (data / 데이터)”. bất biến (invariant / 불변식) là khôi phục (recovery / 복구) có đủ thông tin (information / 정보) và thứ tự (ordering / 순서) để dựng lại **committed lịch sử (history / 이력) hợp lệ**.

Đọc sâu hơn tại [MVCC, visibility, WAL và recovery internals](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md).

> **Chuyển mạch:** MVCC quyết định visibility của version; WAL biến lịch sử giao dịch thành log có thể replay sau crash, nối semantics của commit với filesystem/device durability.

## 3. WAL giải bài toán gì?

**Nhật ký ghi trước (Write-Ahead Logging, WAL)** yêu cầu log chứa đủ thông tin (information / 정보) để khôi phục (recovery / 복구) một thay đổi phải đạt durability cần thiết trước khi dữ liệu (data / 데이터) page phụ thuộc vào log đó được coi là an toàn để ghi theo giao thức (protocol / 프로토콜).

Mô hình tư duy (mental model / 사고 모델):

```text
log trước
page sau
```

Cơ sở dữ liệu (database / 데이터베이스) không cần flush mọi dữ liệu (data / 데이터) page khi lần ghi nhận (commit / 커밋). Sequential log flush thường rẻ hơn buộc nhiều random data-page writes đồng bộ, vì vậy WAL vừa bảo vệ tính đúng đắn (correctness / 정확성) vừa tạo hiệu năng (performance / 성능) kiến trúc (architecture / 아키텍처) cho lưu trữ (storage / 저장소) engine.

## 4. LSN nối log với page trạng thái (state / 상태)

**Log chuỗi (sequence / 시퀀스) Number (LSN)** tạo logical thứ tự (order / 순서) của log records. dữ liệu (data / 데이터) page có thể mang `pageLSN` cho biết page đã phản ánh log tới đâu. khôi phục (recovery / 복구) so sánh log position với page trạng thái (state / 상태) để quyết định redo nào còn cần thiết.

Đây là một bất biến (invariant / 불변식) rất cụ thể:

```text
page state không được đi trước durable log state theo cách làm recovery mất khả năng giải thích page đó
```

Nếu ghi (write / 쓰기) thứ tự (ordering / 순서) bị phá ở lưu trữ (storage / 저장소) ngăn xếp (stack / 스택), WAL giao thức (protocol / 프로토콜) có thể mất ý nghĩa dù cơ sở dữ liệu (database / 데이터베이스) mã (code / 코드) nhìn đúng.

> **Chuyển mạch:** LSN cho biết log và page phải được giải thích theo thứ tự nào; **5. `write()` success không đồng nghĩa durable** kiểm tra xem thứ tự đó có thực sự đi qua kernel, filesystem và thiết bị hay mới dừng ở bộ đệm.

## 5. `write()` success không đồng nghĩa durable

`write()` thường chỉ chứng minh kernel đã nhận bytes. Với buffered I/O, bytes có thể mới nằm trong **bộ đệm trang (page cache)** và page chỉ được đánh dấu dirty.

```text
write() success
≠
non-volatile persistence
```

Thành phần nguyên thủy (primitive / 기본 요소) như `fsync`, `fdatasync`, `O_DSYNC` hoặc cơ chế (mechanism / 메커니즘) tương đương truyền durability intent xuống ngăn xếp (stack / 스택). Nhưng guarantee cuối vẫn phụ thuộc filesystem, khối (block / 블록) tầng (layer / 계층), driver và thiết bị (device / 장치) thực hiện đúng đặc tả hợp đồng (contract / 계약).

## 6. Page bộ nhớ đệm (cache / 캐시) và buffer pool tạo hai lớp trạng thái (state / 상태)

Cơ sở dữ liệu (database / 데이터베이스) thường có buffer pool riêng. OS lại có page bộ nhớ đệm (cache / 캐시). Nếu cơ sở dữ liệu (database / 데이터베이스) dùng buffered tệp (file / 파일) I/O, cùng logical dữ liệu (data / 데이터) có thể đi qua cả hai lớp bộ nhớ đệm (cache / 캐시); direct I/O có thể giảm double caching nhưng không làm crash consistency tự động đúng.

Pressure ở hai tầng cũng tương tác: cơ sở dữ liệu (database / 데이터베이스) dirty-page chính sách (policy / 정책) ảnh hưởng writeback burst; kernel reclaim có thể tạo I/O contention; thiết bị (device / 장치) hàng đợi (queue / 큐) độ sâu (depth / 깊이) và flush độ trễ (latency / 지연 시간) lại phản hồi ngược lên lần ghi nhận (commit / 커밋) độ trễ (latency / 지연 시간).

Vì vậy “DB CPU thấp nhưng lần ghi nhận (commit / 커밋) p99 tăng” vẫn có thể là storage-stack bài toán (problem / 문제).

## 7. Filesystem thứ tự (ordering / 순서) và journaling

Filesystem phải bảo vệ siêu dữ liệu (metadata / 메타데이터)/cấu trúc dữ liệu (data structure / 자료구조) của chính nó qua crash. Journaling hoặc sao chép khi ghi (copy-on-write / 쓰기 시 복사) filesystem dùng giao thức (protocol / 프로토콜) riêng để giữ filesystem-consistency bất biến (invariant / 불변식).

Cơ sở dữ liệu (database / 데이터베이스) WAL và filesystem journal không trùng ranh giới (boundary / 경계):

```text
database WAL      -> transaction/recovery semantics
filesystem journal -> filesystem metadata/data-structure consistency
```

Một lớp không tự thay thế lớp kia. cơ sở dữ liệu (database / 데이터베이스) vẫn cần biết ghi (write / 쓰기)/flush ngữ nghĩa (semantics / 의미론) mà filesystem cung cấp.

> **Chuyển mạch:** WAL và journal giữ hai loại bất biến khác nhau; **8. Controller bộ nhớ đệm, flush và power-loss protection** đi xuống điểm mà lời hứa `flush` có thể bị yếu đi nếu controller hoặc nguồn điện không bảo vệ dữ liệu.

## 8. Controller bộ nhớ đệm (cache / 캐시), flush và power-loss protection

SSD/HDD có thể có volatile ghi (write / 쓰기) bộ nhớ đệm (cache / 캐시). Nếu controller báo complete trước khi dữ liệu (data / 데이터) đến non-volatile media, power mất mát (loss / 손실) có thể làm mất ghi (write / 쓰기) trừ khi thiết bị (device / 장치) có power-loss protection hoặc firmware thực hiện flush ngữ nghĩa (semantics / 의미론) đúng.

Do đó một chuỗi durability thực tế là:

```text
DB WAL flush intent
→ syscall
→ filesystem/block ordering
→ device flush/FUA semantics
→ controller
→ non-volatile media
```

Mỗi ranh giới (boundary / 경계) là một nơi lớp trừu tượng (abstraction / 추상화) có thể leak nếu guarantee bị hiểu sai.

## 9. Torn ghi (write / 쓰기) và atomicity granularity

Cơ sở dữ liệu (database / 데이터베이스) page có thể lớn hơn atomic ghi (write / 쓰기) đơn vị (unit / 단위) của lưu trữ (storage / 저장소). Power mất mát (loss / 손실) giữa ghi (write / 쓰기) có thể tạo **ghi rách (torn write)**: một phần page mới, một phần cũ.

Checksum chỉ giúp phát hiện corruption; khôi phục (recovery / 복구) cần cơ chế (mechanism / 메커니즘) như WAL redo, page LSN, double-write buffer hoặc page-image chiến lược (strategy / 전략) tùy engine. tính đúng đắn (correctness / 정확성) yêu cầu (requirement / 요구사항) là crash không được biến partial vật lý (physical / 물리적) ghi (write / 쓰기) thành logical trạng thái (state / 상태) không thể phát hiện/phục hồi.

## 10. Group lần ghi nhận (commit / 커밋): hiệu năng (performance / 성능) pressure thay đổi timing, không đổi bất biến (invariant / 불변식)

Nếu mỗi giao dịch (transaction / 트랜잭션) flush lưu trữ (storage / 저장소) riêng, flush độ trễ (latency / 지연 시간) giới hạn thông lượng (throughput / 처리량). **lần ghi nhận (commit / 커밋) theo nhóm (group commit)** gom nhiều lần ghi nhận (commit / 커밋) records vào cùng một durable flush.

```text
T1 ─┐
T2 ─┼─> one WAL flush -> acknowledge T1,T2,T3
T3 ─┘
```

Hiệu năng (performance / 성능) hành vi (behavior / 동작) thay đổi: một giao dịch (transaction / 트랜잭션) có thể chờ thêm để amortize flush chi phí (cost / 비용), nhưng acknowledgement vẫn chỉ được phát khi durability điều kiện (condition / 조건) của group đã đạt.

Đây là mẫu lập luận (reasoning / 추론) quan trọng: tối ưu hóa (optimization / 최적화) được phép đổi batching/timing, không được âm thầm làm yếu bất biến (invariant / 불변식) nếu API không đổi đặc tả hợp đồng (contract / 계약).

## 11. Checkpoint đổi khôi phục (recovery / 복구) chi phí (cost / 비용) chứ không thay lần ghi nhận (commit / 커밋) truth

Checkpoint giới hạn lượng WAL phải scan/replay sau restart. Fuzzy checkpoint có thể chạy khi tải công việc (workload / 워크로드) vẫn hoạt động; nó không nhất thiết đồng nghĩa mọi dirty page đã sạch.

Checkpoint quá thường xuyên tăng ghi (write / 쓰기) pressure; quá thưa tăng khôi phục (recovery / 복구) thời gian (time / 시간) và WAL retention. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa thời gian chạy (runtime / 런타임) chi phí (cost / 비용) và **mục tiêu thời gian khôi phục (Recovery Time Objective, RTO)**.

## 12. Replication thêm một máy trạng thái (state machine / 상태 머신) khác

Replication không đơn giản “bản sao (copy / 복사) tệp (file / 파일) sang máy khác”. Log entry có thể đi qua các trạng thái:

```text
created locally
→ written to local log
→ sent to replicas
→ received
→ persisted remotely
→ accepted by quorum/replication rule
→ applied/visible
```

Tùy giao thức (protocol / 프로토콜), máy khách (client / 클라이언트) acknowledgement có thể gắn với một mốc khác nhau. Nếu hệ thống (system / 시스템) hứa survive leader mất mát (loss / 손실), ack chỉ sau cục bộ (local / 로컬) persistence có thể chưa đủ. Nếu hệ thống (system / 시스템) hứa synchronous quorum durability, giao thức (protocol / 프로토콜) phải chứng minh một committed entry vẫn hiện diện trong quorum có authority sau failover.

Đây là nơi giao dịch (transaction / 트랜잭션) durability nối với consensus/log replication thay vì kết thúc ở cục bộ (local / 로컬) disk.

> **Chuyển mạch:** Khi replication thêm một máy trạng thái, số bản sao không còn là câu trả lời đủ. **13. Replication không tự động đồng nghĩa durability** tách rõ persistence cục bộ, quy tắc commit và độc lập failure domain.

## 13. Replication không tự động đồng nghĩa durability

Nếu leader và replica đều chỉ giữ ghi (write / 쓰기) trong volatile bộ nhớ đệm (cache / 캐시), một power sự kiện (event / 이벤트) chung vẫn có thể làm mất trạng thái (state / 상태). Nếu các replica cùng miền lỗi (failure domain / 장애 도메인), “ba bản sao” cũng không bảo vệ khỏi mất cả lĩnh vực (domain / 도메인) đó.

Durability cần lập luận (reasoning / 추론) theo ba chiều độc lập:

```text
local persistence guarantee
×
replication/commit rule
×
failure-domain independence
```

Số replica tự nó không trả lời được ba câu hỏi trên.

## 14. Synchronous replication đổi đường găng (critical path / 임계 경로)

Khi lần ghi nhận (commit / 커밋) phải đợi remote quorum, mạng (network / 네트워크) RTT, remote hàng đợi (queue / 큐) và remote lưu trữ (storage / 저장소) flush đều nằm trên đường găng (critical path / 임계 경로). Tail độ trễ (latency / 지연 시간) có thể tăng mạnh khi một replica chậm hoặc cross-region link dao động.

Giao thức (protocol / 프로토콜) tốt phải quyết định replica nào nằm trong quorum, khi nào follower chậm bị loại khỏi đường găng (critical path / 임계 경로), và authority sau failover được xác định thế nào. Đây là nơi durability, consistency và availability gặp nhau.

Đọc thêm [Consensus internals](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md).

## 15. Async replication tạo một thất bại (failure / 실패) cửa sổ (window / 윈도우) có chủ đích

Async replication có thể giảm foreground độ trễ (latency / 지연 시간) vì leader ack trước khi remote bản sao (copy / 복사) đạt durability. Đổi lại có replication lag và **mất dữ liệu tiềm năng (Recovery Point Objective, RPO)** khi failover.

Điều quan trọng là đặc tả hợp đồng (contract / 계약) phải nói rõ cửa sổ (window / 윈도우) này, metrics phải đo được lag, và failover procedure phải hiểu replica mới có lịch sử (history / 이력) tới đâu.

## 16. Virtualization và cloud lưu trữ (storage / 저장소) kéo dài chuỗi lời hứa

Trong VM/cloud, đường dẫn (path / 경로) có thể là:

```text
guest filesystem
→ virtual block device
→ hypervisor/host
→ storage network
→ replicated storage service
→ physical media
```

Một guest `fsync` chỉ đáng tin nếu mọi tầng (layer / 계층) truyền durability intent đúng. Với managed lưu trữ (storage / 저장소), guarantee phải lấy từ dịch vụ (service / 서비스) đặc tả hợp đồng (contract / 계약), không suy luận từ intuition cục bộ (local / 로컬) disk.

## 17. hiệu năng (performance / 성능) pressure thường lộ qua tail, không qua average

Lưu trữ (storage / 저장소) GC, dirty-page writeback, checkpoint burst, hàng đợi (queue / 큐) congestion hoặc replica lag có thể làm p99 lần ghi nhận (commit / 커밋) độ trễ (latency / 지연 시간) tăng trong khi average vẫn ổn.

Khi thông lượng (throughput / 처리량) tăng gần sức chứa (capacity / 용량), group lần ghi nhận (commit / 커밋) có thể cải thiện thông lượng (throughput / 처리량) nhưng hàng đợi (queue / 큐) wait cũng tăng. Khi checkpoint/writeback trùng peak traffic, foreground flush có thể tranh bandwidth với background maintenance.

Hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) vì thế phải đo **độ trễ (latency / 지연 시간) phân phối (distribution / 분포) + hàng đợi (queue / 큐) + saturation + background activity** cùng lúc.

## 18. bằng chứng vận hành (production evidence / 운영 증거) theo từng tầng

Ứng dụng (application / 애플리케이션) tầng (layer / 계층) cần giao dịch (transaction / 트랜잭션) độ trễ (latency / 지연 시간), hết thời gian chờ (timeout / 타임아웃) và acknowledgement ngữ nghĩa (semantics / 의미론). cơ sở dữ liệu (database / 데이터베이스) tầng (layer / 계층) cần WAL bytes/flush độ trễ (latency / 지연 시간), checkpoint activity, dirty pages, khóa (lock / 잠금)/MVCC horizon và replication LSN/lag. OS tầng (layer / 계층) cần dirty/writeback pages, I/O wait, block-device độ trễ (latency / 지연 시간)/hàng đợi (queue / 큐) độ sâu (depth / 깊이) và filesystem errors. lưu trữ (storage / 저장소) tầng (layer / 계층) cần thiết bị (device / 장치) độ trễ (latency / 지연 시간), utilization, lỗi (error / 오류) counters và flush hành vi (behavior / 동작) nếu telemetry cho phép. phân tán (distributed / 분산) tầng (layer / 계층) cần quorum trạng thái (state / 상태), leader term/epoch, replica match/applied positions và failover timeline.

Một đồ thị (graph / 그래프) `DB commit latency` đơn độc không đủ để xác định cơ chế.

> **Chuyển mạch:** Chỉ số theo từng tầng giúp dựng giả thuyết, nhưng durability còn cần chứng minh khi có gián đoạn thật. **19. Crash testing** biến invariant thành một kiểm tra có thể tái hiện thay vì một lời hứa trên giấy.

## 19. Crash testing là cách kiểm tra bất biến (invariant / 불변식), không phải edge-case luxury

Happy-path kiểm thử (test / 테스트) chỉ chứng minh đường dẫn (path / 경로) không crash hoạt động. Durability cần fault injection tại interruption points:

```text
kill process trước/sau WAL flush
crash host giữa writeback
force replica lag rồi fail leader
replay recovery nhiều lần
inject partial/reordered write trong test harness nếu stack cho phép
```

Sau mỗi thất bại (failure / 실패) phải kiểm tra bất biến (invariant / 불변식): committed giao dịch (transaction / 트랜잭션) theo đặc tả hợp đồng (contract / 계약) còn tồn tại; uncommitted giao dịch (transaction / 트랜잭션) không xuất hiện sai; khôi phục (recovery / 복구) idempotent; replica mới không phát lịch sử (history / 이력) trái với lần ghi nhận (commit / 커밋) quy tắc (rule / 규칙).

## 20. Backup giải bài toán khác

WAL + replication bảo vệ một số crash/thất bại (failure / 실패) scenarios. Chúng không tự bảo vệ khỏi operator lỗi (error / 오류), logical corruption, ransomware hoặc bad ghi (write / 쓰기) đã replicate tới mọi nút (node / 노드).

Backup/PITR có retention và trust ranh giới (boundary / 경계) riêng. Một durability thiết kế (design / 설계) hoàn chỉnh phải phân biệt **survive crash**, **survive nút (node / 노드) mất mát (loss / 손실)**, **survive region mất mát (loss / 손실)** và **recover historical trạng thái (state / 상태)**.

## Dùng chung (common / 공통) Misconceptions

**“lần ghi nhận (commit / 커밋) nghĩa dữ liệu (data / 데이터) page đã nằm trên disk.”** Không nhất thiết; durable WAL có thể đủ để khôi phục (recovery / 복구) committed thay đổi (change / 변경).

**“`write()` thành công nghĩa dữ liệu (data / 데이터) an toàn.”** Không; bytes có thể chỉ ở volatile bộ nhớ đệm (cache / 캐시).

**“Ba replicas nghĩa không thể mất dữ liệu.”** Không nếu acknowledgement quy tắc (rule / 규칙), cục bộ (local / 로컬) persistence hoặc failure-domain independence không đủ mạnh.

**“Replication là backup.”** Không; lỗi lô-gic (logic / 논리) và corruption có thể được replicate.

**“SSD không seek nên mọi ghi (write / 쓰기) có cùng chi phí (cost / 비용).”** FTL, garbage collection, erase khối (block / 블록), ghi (write / 쓰기) amplification và queueing vẫn làm độ trễ (latency / 지연 시간) biến động.

## Mô hình tư duy

> Durability là một chuỗi bất biến (invariant / 불변식) và acknowledgement. MVCC quyết định lịch sử (history / 이력) nào được nhìn thấy; WAL/khôi phục (recovery / 복구) quyết định lịch sử (history / 이력) nào sống sót crash; filesystem/lưu trữ (storage / 저장소) giữ thứ tự (ordering / 순서) và persistence vật lý; replication quyết định lịch sử (history / 이력) nào còn authority sau mất nút (node / 노드). **Một tầng chỉ được hứa mạnh bằng guarantee đã được chứng minh từ tầng bên dưới.**

## Kết nối

Đọc cùng [MVCC/WAL](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md), [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md), [Storage hardware](../../basic/02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md), [Consensus internals](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md) và [End-to-end latency](./01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 debugging across abstraction layers](./00_debugging_across_abstraction_layers.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
