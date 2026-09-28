# NoSQL, phân tán (distributed / 분산) và analytical databases

> **Mạch đọc:** Đọc **NoSQL, phân tán (distributed / 분산) và analytical databases** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Chọn mô hình dữ liệu (data model / 데이터 모델) từ truy cập (access / 접근) mẫu (pattern / 패턴) và bất biến (invariant / 불변식)** sang **2. Denormalization là intentional replication ở logical tầng (layer / 계층)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Relational cơ sở dữ liệu (database / 데이터베이스) không phải lựa chọn duy nhất vì workloads khác nhau đặt pressure khác nhau lên mô hình dữ liệu (data model / 데이터 모델), quy mô (scale / 규모), độ trễ (latency / 지연 시간), consistency và truy vấn (query / 쿼리) patterns. “NoSQL” không phải một kiến trúc (architecture / 아키텍처) duy nhất mà là umbrella term cho nhiều các hệ thống (systems / 시스템들) đánh đổi relational generality để tối ưu một số truy cập (access / 접근) mẫu (pattern / 패턴) hoặc phân phối (distribution / 분포) mô hình (model / 모델).

Ở mức các hệ thống (systems / 시스템들) lập luận (reasoning / 추론), cơ sở dữ liệu (database / 데이터베이스) kiến trúc (architecture / 아키텍처) xoay quanh ba câu hỏi:

```text
state được partition ở đâu?
state được replicate theo authority/order nào?
physical layout nào phù hợp query/update pattern?
```

Các lựa chọn này tạo bất biến (invariant / 불변식), dạng thất bại (failure mode / 실패 모드) và bằng chứng vận hành (production evidence / 운영 증거) khác nhau.

## 1. Chọn mô hình dữ liệu (data model / 데이터 모델) từ truy cập (access / 접근) mẫu (pattern / 패턴) và bất biến (invariant / 불변식)

Document cơ sở dữ liệu (database / 데이터베이스) lưu aggregate-like documents; key-value store tối ưu lookup theo key; wide-column store tổ chức sparse rows theo partition/clustering keys; đồ thị (graph / 그래프) cơ sở dữ liệu (database / 데이터베이스) tối ưu traversal qua relationships.

Không mô hình (model / 모델) nào “schema-less” theo nghĩa không có cấu trúc (structure / 구조). lược đồ (schema / 스키마) vẫn tồn tại trong ứng dụng (application / 애플리케이션), kiểm tra hợp lệ (validation / 검증) quy tắc (rule / 규칙), serialization format hoặc implicit convention. Chỉ là nơi enforcement và evolution khác relational lược đồ (schema / 스키마).

Câu hỏi tốt hơn “SQL hay NoSQL?” là:

```text
operation nào là critical path?
invariant nào phải atomic?
query nào cần locality?
state có thể partition theo key nào?
reader chấp nhận stale tới mức nào?
```

## 2. Denormalization là intentional replication ở logical tầng (layer / 계층)

Phân tán (distributed / 분산)/document các hệ thống (systems / 시스템들) thường duplicate dữ liệu (data / 데이터) để tránh joins xuyên partitions. Điều này giảm read độ trễ (latency / 지연 시간) nhưng tạo consistency bài toán (problem / 문제): khi nguồn (source / 소스) fact đổi, các copies phải được cập nhật.

Normalization giảm cập nhật (update / 업데이트) anomalies bằng cách giảm duplication; denormalization chấp nhận duplication để tối ưu truy cập (access / 접근) đường dẫn (path / 경로).

Bất biến (invariant / 불변식) phải nói rõ bản sao (copy / 복사) nào là nguồn chuẩn (source of truth / 정본), propagation có synchronous hay asynchronous, stale cửa sổ (window / 윈도우) chấp nhận bao lâu và xung đột (conflict / 충돌)/rebuild xử lý thế nào.

## 3. Partitioning và shard key quyết định locality lẫn thất bại (failure / 실패) surface

Phân tán (distributed / 분산) cơ sở dữ liệu (database / 데이터베이스) chia dữ liệu (data / 데이터) thành partitions/shards. Shard key quyết định placement và truy vấn (query / 쿼리) locality.

Băm (hash / 해시) partitioning thường phân bố đều hơn nhưng phạm vi (range / 범위) truy vấn (query / 쿼리) khó hơn. phạm vi (range / 범위) partitioning giúp scan theo khoảng nhưng dễ skew. Monotonic timestamp có thể dồn writes vào một partition; tenant ID có thể tạo celebrity tenant hotspot.

Một shard key tốt cần cân:

```text
load distribution
query locality
transaction locality
rebalancing cost
hot-key behavior
future growth
```

Không có shard key “đúng” nếu chưa biết tải công việc (workload / 워크로드) phân phối (distribution / 분포).

## 4. Replication cần một authority mô hình (model / 모델)

Replication tạo nhiều vật lý (physical / 물리적) copies nhưng tính đúng đắn (correctness / 정확성) cần trả lời: **bản sao (copy / 복사) nào có quyền quyết định ghi (write / 쓰기) thứ tự (order / 순서)?**

Leader/follower mô hình (model / 모델) thường serialize writes qua leader rồi gửi log/changes tới followers. Multi-leader cho phép writes tại nhiều sites nhưng phải giải xung đột (conflict / 충돌)/thứ tự (order / 순서). Leaderless/quorum mô hình (model / 모델) dùng read/ghi (write / 쓰기) quorum và phiên bản (version / 버전)/xung đột (conflict / 충돌) ngữ nghĩa (semantics / 의미론) khác.

“Số replicas = 3” chưa cho biết consistency. Phải biết lần ghi nhận (commit / 커밋)/ack quy tắc (rule / 규칙) và failover authority.

## 5. cục bộ (local / 로컬) append, replicated và committed là các trạng thái khác nhau

Một ghi (write / 쓰기) có thể đi qua:

```text
received by leader
→ appended to local memory/log
→ durable locally
→ sent to followers
→ durable on followers
→ quorum condition satisfied
→ committed/visible theo protocol
→ applied to materialized state
```

Không phải hệ thống nào cũng expose cùng stages, nhưng mô hình tư duy (mental model / 사고 모델) này giúp hỏi đúng: acknowledgement được gửi ở stage nào?

Nếu máy khách (client / 클라이언트) nhận success trước durable quorum, failover có thể mất acknowledged ghi (write / 쓰기) tùy đặc tả hợp đồng (contract / 계약). Nếu phải chờ remote durable quorum, độ trễ (latency / 지연 시간) đường dẫn (path / 경로) chứa mạng (network / 네트워크) + remote lưu trữ (storage / 저장소).

## 6. Replication lag là trạng thái (state / 상태) distance, không chỉ “milliseconds”

Follower có thể chậm theo log position/LSN/chỉ mục (index / 인덱스) dù wall-clock lag khó đo chính xác. “Replica lag 2 giây” là shorthand; quantity đáng tin hơn thường là khoảng cách applied/received position so với leader theo giao thức (protocol / 프로토콜).

Lag tăng vì mạng (network / 네트워크), lưu trữ (storage / 저장소), apply CPU, khóa (lock / 잠금)/contention, large giao dịch (transaction / 트랜잭션) hoặc maintenance.

Bằng chứng vận hành (production evidence / 운영 증거) nên đo:

```text
leader commit position
follower receive/durable/apply position
apply throughput
network/storage latency
replay/apply errors
```

## 7. Read consistency là observable đặc tả hợp đồng (contract / 계약)

“Strong” và “eventual” là quá thô nếu không nói reader quan sát gì.

Các thuộc tính (property / 속성) thực dụng gồm:

```text
read-your-writes
monotonic reads
monotonic writes
consistent prefix
causal consistency
linearizable read
bounded staleness
```

Ví dụ sau khi người dùng (user / 사용자) đổi profile trên leader rồi yêu cầu (request / 요청) tiếp bị tuyến (route / 경로) sang lagging follower, họ có thể không thấy cập nhật (update / 업데이트) của chính mình. Fix có thể là session stickiness, read from leader, wait-until replica reaches đơn vị từ (token / 토큰)/LSN, hoặc stronger read giao thức (protocol / 프로토콜).

Chọn chiến lược (strategy / 전략) theo bất biến (invariant / 불변식), không theo nhãn marketing.

## 8. Replica read không miễn phí về tính đúng đắn (correctness / 정확성)

Read replicas tăng read sức chứa (capacity / 용량) và tách analytical/report tải công việc (workload / 워크로드) khỏi leader, nhưng stale read có thể phá check-then-act lô-gic (logic / 논리).

Ví dụ:

```text
writer: mark coupon used
reader trên stale replica: coupon still unused
application: cho phép dùng lại
```

Nếu bất biến (invariant / 불변식) yêu cầu unique redemption, kiểm tra hợp lệ (validation / 검증) phải chạy tại authority/giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) có consistency đủ mạnh. bộ nhớ đệm (cache / 캐시)/replica read có thể dùng cho display nhưng không nhất thiết dùng cho authorization/nghiệp vụ (business / 비즈니스) quyết định (decision / 결정).

## 9. Failover là authority transfer, không chỉ đổi DNS

Khi leader thất bại (fail / 실패), hệ thống cần chọn nút (node / 노드) mới và ngăn old leader tiếp tục accept authoritative writes nếu nó quay lại trong trạng thái partitioned.

Cơ chế (mechanism / 메커니즘) thường cần epoch/term/fencing/quorum. bất biến (invariant / 불변식):

> Tại một thời điểm theo giao thức (protocol / 프로토콜), không được có hai authorities độc lập cùng lần ghi nhận (commit / 커밋) histories không thể reconcile nếu đặc tả hợp đồng (contract / 계약) yêu cầu single lịch sử (history / 이력).

Đây là split-brain bài toán (problem / 문제). Health check một mình không đủ vì “không reach được leader” không chứng minh leader đã chết; có thể chỉ là partition.

## 10. RPO và RTO làm failover đặc tả hợp đồng (contract / 계약) cụ thể hơn

**khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표) (RPO)** trả lời có thể mất bao nhiêu committed/accepted dữ liệu (data / 데이터) theo disaster mô hình (model / 모델). **khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표) (RTO)** trả lời mất bao lâu để khôi phục dịch vụ (service / 서비스).

Async replication thường cho độ trễ (latency / 지연 시간) tốt nhưng RPO có thể > 0 khi leader mất trước khi follower catch up. Sync/quorum replication có thể giảm RPO nhưng tăng foreground độ trễ (latency / 지연 시간) và giảm ghi (write / 쓰기) availability trong một số partition/thất bại (failure / 실패) scenario.

Failover thiết kế (design / 설계) là sự đánh đổi (trade-off / 트레이드오프) consistency/durability/availability/thời gian (time / 시간), không chỉ “có replica”.

## 11. Read-after-failover cần hiểu lần ghi nhận (commit / 커밋) horizon

Replica được promote có thể có log prefix khác trạng thái mà một số clients vừa quan sát nếu acknowledgement đặc tả hợp đồng (contract / 계약) yếu hoặc failover chọn nút (node / 노드) chưa đủ hiện tại (current / 현재).

Sau failover, ứng dụng (application / 애플리케이션) có thể thấy dữ liệu (data / 데이터) “đi lùi”. Đây là violation của monotonic/user-observed lịch sử (history / 이력) nếu sản phẩm (product / 제품) giả định (assumption / 가정) mạnh hơn cơ sở dữ liệu (database / 데이터베이스) guarantee.

Bằng chứng (evidence / 증거) cần biết:

```text
write acknowledged ở commit position nào?
new leader có position nào?
node nào tham gia quorum?
old leader có bị fenced không?
read routing sau failover đi đâu?
```

## 12. Quorum không có nghĩa mọi quorum thiết kế (design / 설계) đều linearizable

Nếu N replicas, ghi (write / 쓰기) quorum `W`, read quorum `R` và `R + W > N` cho intersection intuition, nhưng tính đúng đắn (correctness / 정확성) còn phụ thuộc versioning, thất bại (failure / 실패) handling, sloppy quorum, clock các giả định (assumptions / 가정들) và read-repair giao thức (protocol / 프로토콜).

Intersection là một building khối (block / 블록), không phải proof hoàn chỉnh.

Phân tán (distributed / 분산) cơ sở dữ liệu (database / 데이터베이스) đặc tả hợp đồng (contract / 계약) phải được đọc theo concrete giao thức (protocol / 프로토콜), không học thuộc công thức quorum rồi suy ra quá mức.

## 13. LSM cây (tree / 트리) phù hợp write-heavy nhưng chuyển chi phí (cost / 비용) sang compaction/read đường dẫn (path / 경로)

Log-Structured Merge cây (tree / 트리) buffer writes trong bộ nhớ (memory / 메모리) rồi flush immutable sorted tables; background compaction merge levels.

Ghi (write / 쓰기) đường dẫn (path / 경로) biến nhiều random writes thành sequential writes, nhưng reads có thể cần check nhiều tables nếu Bloom filter/chỉ mục (index / 인덱스) không loại được. Compaction tạo ghi (write / 쓰기) amplification và background I/O.

Thất bại (failure / 실패)/hiệu năng (performance / 성능) pressure:

```text
write burst
→ memtable flush tăng
→ compaction debt tăng
→ storage bandwidth bị background work chiếm
→ read/write tail latency tăng
```

LSM là ví dụ điển hình của defer + batch + merge: chi phí (cost / 비용) bị dời, không bị xóa.

## 14. OLTP và OLAP có vật lý (physical / 물리적) các ràng buộc (constraints / 제약조건들) khác nhau

OLTP phục vụ nhiều điểm (point / 지점) read/ghi (write / 쓰기), tính đồng thời (concurrency / 동시성) cao, low độ trễ (latency / 지연 시간) và giao dịch (transaction / 트랜잭션) invariants. OLAP scan/aggregate lượng lớn dữ liệu (data / 데이터), thường đọc ít columns trên nhiều rows.

Vì tải công việc (workload / 워크로드) khác, vật lý (physical / 물리적) bố cục (layout / 레이아웃) cũng khác. Row store tối ưu locality của một bản ghi (record / 레코드); column store tối ưu locality của một attribute qua nhiều rows.

“Column cơ sở dữ liệu (database / 데이터베이스) nhanh hơn” chỉ đúng cho truy vấn (query / 쿼리) shape phù hợp.

## 15. Columnar lưu trữ (storage / 저장소) bắt đầu từ projection pushdown

Nếu bảng (table / 테이블) có 100 columns nhưng truy vấn (query / 쿼리) chỉ cần 4, row store phải đọc bytes của nhiều fields không dùng tùy bố cục (layout / 레이아웃)/bộ nhớ đệm (cache / 캐시). Columnar bố cục (layout / 레이아웃) cho phép đọc các column chunks cần thiết.

```text
SELECT region, SUM(amount)
FROM sales
GROUP BY region
```

Engine có thể đọc chủ yếu `region` và `amount`, giảm I/O và bộ nhớ (memory / 메모리) bandwidth.

Đây là hiệu năng (performance / 성능) bất biến (invariant / 불변식): **bytes processed nên gần bytes relevant hơn là full logical row width**.

## 16. Compression hiệu quả vì values cùng column có phân phối (distribution / 분포) giống nhau

Values cùng column thường có kiểu (type / 타입)/phân phối (distribution / 분포) lặp lại nên encode tốt: dictionary encoding, run-length encoding, delta encoding, bit packing và compression codecs.

Compression không chỉ giảm lưu trữ (storage / 저장소); nó có thể giảm I/O/bộ nhớ (memory / 메모리) bandwidth đủ nhiều để CPU decompression vẫn có lợi.

Nhưng high-cardinality/random dữ liệu (data / 데이터) compress kém hơn. Encoding choice phụ thuộc phân phối (distribution / 분포).

## 17. Zone map / min-max siêu dữ liệu (metadata / 메타데이터) giúp skip dữ liệu (data / 데이터)

Columnar segments/row groups có thể giữ siêu dữ liệu (metadata / 메타데이터) như min/max/null count. truy vấn (query / 쿼리) predicate có thể bỏ qua entire chunk nếu phạm vi (range / 범위) không thể match.

```text
segment amount: min=0, max=100
predicate amount > 1000
→ skip segment
```

Đây là data-skipping chỉ mục (index / 인덱스) nhẹ. Nếu clustering/thứ tự (order / 순서) của dữ liệu (data / 데이터) phù hợp predicate, skip ratio cao; nếu values random khắp mọi segment, siêu dữ liệu (metadata / 메타데이터) ít hữu ích.

Vật lý (physical / 물리적) thứ tự (ordering / 순서) vì vậy ảnh hưởng analytical scan chi phí (cost / 비용).

## 18. Vectorized thực thi (execution / 실행) amortize trình thông dịch (interpreter / 인터프리터)/function-call overhead

Thay vì xử lý một row mỗi operator lời gọi (call / 호출), analytical engine có thể xử lý batches/vectors. Điều này tăng locality, giảm virtual/function-call overhead và tạo cơ hội SIMD.

Chuỗi xử lý (pipeline / 파이프라인) có thể:

```text
scan vector
→ filter vector
→ project/decode needed columns
→ aggregate in batches
```

Nhưng batch quá lớn tăng bộ nhớ đệm (cache / 캐시) footprint; variable-length dữ liệu (data / 데이터) và branchy expressions có thể giảm SIMD efficiency.

Đọc thêm [join algorithms, vectorized execution và late materialization](../../05_data_databases/advanced/06_join_algorithms_vectorized_execution_and_late_materialization.md).

## 19. Late materialization tránh dựng full row quá sớm

Columnar engine thường giữ column vectors/row identifiers qua filter/phép nối (join / 조인) rồi chỉ reconstruct đầu ra (output / 출력) rows khi cần. Đây là **late materialization**.

Lợi ích: tránh bản sao (copy / 복사)/decode columns bị filter bỏ. sự đánh đổi (trade-off / 트레이드오프): position ánh xạ (mapping / 매핑) và gather có thể phức tạp, random truy cập (access / 접근) có thể đắt nếu chuỗi xử lý (pipeline / 파이프라인) mất locality.

Tối ưu hóa (optimization / 최적화) phải lập luận (reasoning / 추론) cùng truy vấn (query / 쿼리) selectivity và dữ liệu (data / 데이터) bố cục (layout / 레이아웃).

## 20. Analytical truy vấn (query / 쿼리) vẫn có tính đồng thời (concurrency / 동시성) và spill thất bại (failure / 실패) modes

Băm (hash / 해시) phép nối (join / 조인)/group-by cần bộ nhớ (memory / 메모리). Nếu cardinality estimate thấp hơn thực tế, operator có thể vượt ngân sách (budget / 예산) và spill ra disk. Nhiều concurrent analytical queries có thể cùng consume bộ nhớ (memory / 메모리)/bandwidth rồi làm whole-node thông lượng (throughput / 처리량) giảm.

Bằng chứng (evidence / 증거) cần tách:

```text
bytes scanned
segments skipped
compression ratio
rows/vectors processed
operator memory
spill bytes/time
CPU utilization + memory bandwidth
storage throughput
```

Truy vấn (query / 쿼리) “chậm” không nhất thiết vì SQL lô-gic (logic / 논리); có thể vì dữ liệu (data / 데이터) skipping thất bại hoặc bộ nhớ (memory / 메모리) spill.

## 21. Warehouse, lake và lakehouse là lưu trữ (storage / 저장소)/siêu dữ liệu (metadata / 메타데이터) trade-offs

Warehouse thường quản lý curated analytical dữ liệu (data / 데이터) với engine/lưu trữ (storage / 저장소) tích hợp (integration / 통합) chặt. dữ liệu (data / 데이터) lake ưu tiên đối tượng (object / 객체) lưu trữ (storage / 저장소) rẻ/open formats. Lakehouse thêm bảng (table / 테이블) siêu dữ liệu (metadata / 메타데이터), giao dịch (transaction / 트랜잭션)/phiên bản (version / 버전) ngữ nghĩa (semantics / 의미론) và truy vấn (query / 쿼리) optimizations trên đối tượng (object / 객체) lưu trữ (storage / 저장소).

Các terms này là kiến trúc (architecture / 아키텍처) families, không phải scientific categories cứng. Điều quan trọng là bất biến (invariant / 불변식):

```text
snapshot nào reader thấy?
concurrent writer commit thế nào?
schema evolution ra sao?
metadata/catalog có authority ở đâu?
object files orphan/compact thế nào?
```

## 22. Materialized view là precomputation với freshness đặc tả hợp đồng (contract / 계약)

Nếu truy vấn (query / 쿼리) đắt nhưng nguồn (source / 소스) cập nhật (update / 업데이트) ít hơn, materialized view đổi lưu trữ (storage / 저장소)/cập nhật (update / 업데이트) công việc (work / 작업) lấy truy vấn (query / 쿼리) độ trễ (latency / 지연 시간).

Câu hỏi cần trả lời:

```text
refresh synchronous hay async?
stale window bao lâu?
refresh failure làm view dừng ở version nào?
reader biết freshness không?
```

Materialization là caching ở cơ sở dữ liệu (database / 데이터베이스) quy mô (scale / 규모); consistency ngữ nghĩa (semantics / 의미론) vẫn phải tường minh (explicit / 명시적).

## 23. bằng chứng vận hành (production evidence / 운영 증거) cho phân tán (distributed / 분산) cơ sở dữ liệu (database / 데이터베이스)

Khi điều tra replication/failover/read anomaly, cần nối:

```text
client request + consistency mode
leader/epoch/term
commit/log position
replica receive/durable/apply position
replication lag/backlog
read routing target
failover/promotion timeline
network/storage errors
```

Nếu chỉ có “replica healthy=true”, không đủ để chứng minh read freshness hoặc failover tính đúng đắn (correctness / 정확성).

## 24. bằng chứng vận hành (production evidence / 운영 증거) cho analytical engine

Khi truy vấn (query / 쿼리) scan/aggregate chậm, cần:

```text
actual execution plan
cardinality estimate vs actual
bytes/segments scanned
pruning/data-skipping effectiveness
compression/decode cost
operator memory and spill
CPU/vectorization efficiency
memory/storage bandwidth
```

Tối ưu chỉ chỉ mục (index / 인덱스)/lược đồ (schema / 스키마) theo intuition mà không nhìn vật lý (physical / 물리적) thực thi (execution / 실행) dễ sửa sai tầng (layer / 계층).

## 25. thất bại (failure / 실패) ma trận (matrix / 행렬) cho replication

Một replication thiết kế (design / 설계) nên giải thích được ít nhất:

```text
leader process crash
leader host/storage loss
network partition leader↔majority
slow follower
follower storage corruption
old leader returns after failover
cross-region latency spike
control-plane membership change
```

Với mỗi trường hợp (case / 사례), hỏi: ai còn authority, ghi (write / 쓰기) có được accept không, acknowledged ghi (write / 쓰기) nào survive, read có stale không, khôi phục (recovery / 복구) bằng chứng (evidence / 증거) nằm đâu?

## 26. Mô hình tư duy

> cơ sở dữ liệu (database / 데이터베이스) kiến trúc (architecture / 아키텍처) là tương tác (interaction / 상호작용) giữa **mô hình dữ liệu (data model / 데이터 모델), partition locality, replication authority, consistency đặc tả hợp đồng (contract / 계약) và vật lý (physical / 물리적) lưu trữ (storage / 저장소)/thực thi (execution / 실행) bố cục (layout / 레이아웃)**. Replication không chỉ là nhiều copies; nó là giao thức (protocol / 프로토콜) quyết định ghi (write / 쓰기) nào có authority sau thất bại (failure / 실패). Columnar lưu trữ (storage / 저장소) không chỉ là “lưu theo cột”; nó là cách giảm bytes processed và tận dụng compression/vectorized thực thi (execution / 실행) cho analytical tải công việc (workload / 워크로드). Cả hai phải được đánh giá bằng observable đặc tả hợp đồng (contract / 계약) và bằng chứng vận hành (production evidence / 운영 증거).

## Những hiểu nhầm thường gặp

**“NoSQL tốt hơn SQL khi dữ liệu lớn.”** quy mô (scale / 규모) phụ thuộc partitioning, tải công việc (workload / 워크로드), consistency và operations; relational các hệ thống (systems / 시스템들) cũng có phân tán (distributed / 분산) implementations.

**“Replica read luôn an toàn nếu chỉ đọc.”** Stale read vẫn có thể phá nghiệp vụ (business / 비즈니스) quyết định (decision / 결정) nếu reader dùng nó để authorize/check bất biến (invariant / 불변식).

**“Failover chỉ là promote nút (node / 노드) khác.”** Promotion là authority transfer; fencing và lần ghi nhận (commit / 커밋) horizon quyết định tính đúng đắn (correctness / 정확성).

**“Quorum intersection tự động nghĩa linearizable.”** Không; giao thức (protocol / 프로토콜)/phiên bản (version / 버전)/read ngữ nghĩa (semantics / 의미론) vẫn quyết định guarantee.

**“Column store luôn nhanh hơn row store.”** Chỉ khi tải công việc (workload / 워크로드) tận dụng column projection, compression, skipping và scan/vectorization.

## Kết nối

Xem [transactions](./02_transactions_acid_and_concurrency_control.md), [storage/WAL](./04_storage_logs_recovery_and_durability.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [replication/consensus](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md), [Consensus advanced](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md), [Distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 data models and database systems](./00_data_models_and_database_systems.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
