# LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **LSM Tree, compaction, Bloom filters và write amplification**. Route đi từ memtable/immutable files → read path/Bloom filter → compaction policy → read/write/space amplification và tombstone, để tốc độ ghi được cân với debt I/O phía sau.

B+cây (tree / 트리) tối ưu cho cập nhật theo page và truy vấn có thứ tự, nhưng tải công việc (workload / 워크로드) ghi ngẫu nhiên với tốc độ cao có thể buộc lưu trữ (storage / 저장소) engine sửa nhiều page nhỏ ở nhiều vị trí. **Cây hợp nhất có cấu trúc log (Log-Structured Merge Tree, LSM Tree / 로그 구조 병합 트리)** đổi bài toán: ghi mới trước vào cấu trúc dễ append, sau đó dùng công việc nền để hợp nhất dữ liệu thành các run đã sắp thứ tự.

LSM không làm chi phí biến mất. Nó **dời thời điểm và hình dạng của chi phí**: foreground ghi (write / 쓰기) nhẹ hơn, nhưng read đường dẫn (path / 경로), không gian (space / 공간) usage và compaction phải trả món nợ tổ chức dữ liệu về sau.

## 1. Bài toán ban đầu và bất biến (invariant / 불변식) của LSM

Một lưu trữ (storage / 저장소) engine cần đồng thời giữ vài bất biến (invariant / 불변식). ghi (write / 쓰기) đã được acknowledge theo durability đặc tả hợp đồng (contract / 계약) phải có đường khôi phục (recovery / 복구). Khi cùng một key xuất hiện ở nhiều nơi, read phải chọn đúng phiên bản (version / 버전) theo thứ tự (ordering / 순서)/visibility quy tắc (rule / 규칙) của engine. tệp (file / 파일) immutable đã được publish không được bị sửa tùy ý. Compaction chỉ được xóa phiên bản (version / 버전) hoặc tombstone khi chắc chắn việc xóa đó không làm old giá trị (value / 값) sống lại hoặc phá snapshot còn hợp lệ.

Có thể hình dung vòng đời (lifecycle / 생명주기):

```text
mutation
→ WAL
→ memtable
→ immutable memtable
→ SSTable
→ compaction qua các level/run
→ version cũ được reclaim khi safe
```

WAL trả lời durability khi dữ liệu còn ở bộ nhớ (memory / 메모리). Memtable tối ưu foreground mutation. SSTable biến trạng thái (state / 상태) thành tệp (file / 파일) immutable có thứ tự. Compaction duy trì hình dạng lâu dài của tập tệp (file / 파일).

> **Nối mạch:** **1. Bài toán ban đầu và bất biến (invariant / 불변식) của LSM** đặt vấn đề; **2. ghi (write / 쓰기) đường dẫn (path / 경로): foreground nhanh vì chưa tổ chức xong dữ liệu** kiểm tra bằng chứng, rồi **3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn** mở rộng hệ quả.

## 2. ghi (write / 쓰기) đường dẫn (path / 경로): foreground nhanh vì chưa tổ chức xong dữ liệu

Ghi (write / 쓰기) thường được append vào **nhật ký ghi trước (Write-Ahead Log, WAL / 선행 기록 로그)** rồi cập nhật **memtable** trong RAM. Khi memtable đạt ngưỡng, engine đóng băng nó thành immutable memtable và flush thành **Sorted String bảng (table / 테이블) (SSTable)** hoặc sorted run tương tự.

Flush tuần tự thường thân thiện với khối (block / 블록) lưu trữ (storage / 저장소) hơn việc sửa ngẫu nhiên nhiều page. Nhưng cùng một logical key có thể tồn tại ở memtable, tệp (file / 파일) mới và nhiều tệp (file / 파일) cũ. Vì vậy ghi (write / 쓰기) độ trễ (latency / 지연 시간) thấp tại `PUT` không phải toàn bộ chi phí (cost / 비용) của ghi (write / 쓰기).

Một benchmark chỉ đo “bao nhiêu PUT/s trước khi compaction chạy nặng” dễ đo burst sức chứa (capacity / 용량) thay vì **sustainable ghi (write / 쓰기) thông lượng (throughput / 처리량)**.

> **Nối mạch:** **2. ghi (write / 쓰기) đường dẫn (path / 경로): foreground nhanh vì chưa tổ chức xong dữ liệu** đặt vấn đề; **3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn** kiểm tra bằng chứng, rồi **4. Read đường dẫn (path / 경로) là phép tìm kiếm qua nhiều lớp lịch sử** mở rộng hệ quả.

## 3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn

SSTable thường immutable sau khi hoàn tất. Reader có thể đọc tệp (file / 파일) mà không phải phối hợp với writer sửa nội dung ngay trong tệp (file / 파일) đó. Compaction tạo tệp (file / 파일) mới rồi cập nhật siêu dữ liệu (metadata / 메타데이터) để publish một tập tệp (file / 파일) mới.

Engine vì thế thường có siêu dữ liệu (metadata / 메타데이터) kiểu **phiên bản (version / 버전) set / manifest** mô tả SSTable nào thuộc logical trạng thái (state / 상태) hiện tại. bất biến (invariant / 불변식) không chỉ là “tệp (file / 파일) mới đã được ghi”; siêu dữ liệu (metadata / 메타데이터) phải chuyển sang phiên bản (version / 버전) mới theo crash-safe giao thức (protocol / 프로토콜).

Nếu tiến trình (process / 프로세스) crash sau khi tạo đầu ra (output / 출력) tệp (file / 파일) nhưng trước khi publish manifest, tệp (file / 파일) có thể thành orphan và được cleanup sau. Nếu siêu dữ liệu (metadata / 메타데이터) publish trước khi tệp (file / 파일) cần thiết thực sự durable, khôi phục (recovery / 복구) có thể trỏ tới trạng thái (state / 상태) không đầy đủ. Đây là cùng family với filesystem crash consistency: **đối tượng (object / 객체) phải tồn tại đủ chắc trước khi pointer/siêu dữ liệu (metadata / 메타데이터) tuyên bố nó là live trạng thái (state / 상태)**.

Đọc thêm [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [MVCC/WAL/recovery](./00_mvcc_visibility_wal_and_recovery_internals.md).

> **Nối mạch:** **3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn** đặt đầu vào cho **4. Read đường dẫn (path / 경로) là phép tìm kiếm qua nhiều lớp lịch sử**, rồi **5. Bloom filter giải bài toán negative lookup** mở rộng hệ quả.

## 4. Read đường dẫn (path / 경로) là phép tìm kiếm qua nhiều lớp lịch sử

Một điểm (point / 지점) lookup thường kiểm tra memtable trước, rồi immutable memtable và các SSTable có khả năng chứa key. Nếu nhiều phiên bản (version / 버전) tồn tại, engine cần chọn phiên bản (version / 버전) mới nhất hợp lệ theo chuỗi (sequence / 시퀀스)/giao dịch (transaction / 트랜잭션) siêu dữ liệu (metadata / 메타데이터) của chính nó.

```text
memtable
→ immutable memtable
→ file metadata / key range
→ Bloom filter
→ index block
→ data block
```

Mỗi bước cố loại I/O không cần thiết. **Read amplification** vì vậy không chỉ là “số tệp (file / 파일) đã mở”, mà còn là siêu dữ liệu (metadata / 메타데이터) lookup, trượt bộ nhớ đệm (cache miss / 캐시 미스), khối (block / 블록) read và phiên bản (version / 버전) filtering cần cho một logical read.

> **Nối mạch:** **4. Read đường dẫn (path / 경로) là phép tìm kiếm qua nhiều lớp lịch sử** đặt đầu vào cho **5. Bloom filter giải bài toán negative lookup**, rồi **6. Compaction là cơ chế trả nợ, không phải housekeeping phụ** mở rộng hệ quả.

## 5. Bloom filter giải bài toán negative lookup

**Bộ lọc Bloom (Bloom filter / 블룸 필터)** là cấu trúc xác suất cho membership kiểm thử (test / 테스트). Với cấu hình đúng, nó có thể trả lời chắc chắn “key không ở đây”, hoặc “key có thể ở đây”. False positive làm engine đọc thêm tệp (file / 파일) vô ích; false negative không được phép xảy ra theo đặc tả hợp đồng (contract / 계약) thông thường của filter.

Bloom filter đặc biệt có giá trị khi lookup hỏi key không tồn tại hoặc key chỉ nằm trong một trong nhiều runs. Nhưng filter không miễn phí: nó chiếm bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소) và cần băm (hash / 해시) công việc (work / 작업).

Bits-per-key quá thấp làm false-positive tỷ lệ (rate / 비율) tăng và read amplification quay lại dưới dạng I/O. Dành quá nhiều bộ nhớ (memory / 메모리) cho filters lại có thể làm bộ nhớ đệm (cache / 캐시) dữ liệu (data / 데이터)/chỉ mục (index / 인덱스) blocks thiếu. Đây là sự đánh đổi (trade-off / 트레이드오프) trong cùng một bộ nhớ (memory / 메모리) ngân sách (budget / 예산).

> **Nối mạch:** **5. Bloom filter giải bài toán negative lookup** đặt đầu vào cho **6. Compaction là cơ chế trả nợ, không phải housekeeping phụ**, rồi **7. Leveled và size-tiered tối ưu các amplification khác nhau** mở rộng hệ quả.

## 6. Compaction là cơ chế trả nợ, không phải housekeeping phụ

**Hợp nhất nền (compaction / 컴팩션)** đọc nhiều sorted runs, merge chúng theo key/phiên bản (version / 버전) thứ tự (order / 순서), ghi đầu ra (output / 출력) mới rồi chuyển siêu dữ liệu (metadata / 메타데이터) sang tập tệp (file / 파일) mới. Trong quá trình này engine có thể loại phiên bản (version / 버전) bị supersede, reclaim tombstone đã an toàn và giảm overlap giữa files.

Compaction tiêu CPU, bộ nhớ (memory / 메모리) buffer, read bandwidth và ghi (write / 쓰기) bandwidth. Nếu ingest tạo debt nhanh hơn compaction trả được, số runs/mức (level / 수준) overlap tăng. Read amplification, không gian (space / 공간) amplification và background I/O cùng tăng.

Đến một điểm engine phải throttle hoặc stall foreground writes để không tích debt vô hạn. Vì vậy `write stall time`, pending compaction bytes và mức (level / 수준) kích thước (size / 크기) thường quan trọng hơn một con số ghi (write / 쓰기) độ trễ (latency / 지연 시간) trung bình.

> **Nối mạch:** **6. Compaction là cơ chế trả nợ, không phải housekeeping phụ** đặt đầu vào cho **7. Leveled và size-tiered tối ưu các amplification khác nhau**, rồi **8. Ba amplification tạo một tam giác chi phí** mở rộng hệ quả.

## 7. Leveled và size-tiered tối ưu các amplification khác nhau

**Leveled compaction** cố giảm overlap giữa files trong một mức (level / 수준). điểm (point / 지점) read có thể cần kiểm tra ít candidate hơn, nhưng một byte có thể bị rewrite nhiều lần khi được đẩy qua các mức (level / 수준).

**Size-tiered compaction** hoặc các chiến lược tiered giữ nhiều runs cùng cỡ rồi merge theo batch. Cách này thường giảm ghi (write / 쓰기) amplification nhưng có thể tăng số runs mà read phải xét và giữ duplicate versions lâu hơn.

Không có chiến lược (strategy / 전략) tốt tuyệt đối. tải công việc (workload / 워크로드) read-heavy với strict p99 lookup khác ingest-heavy; phạm vi (range / 범위) scan khác điểm (point / 지점) lookup. Quyết định compaction là quyết định về **read amplification × ghi (write / 쓰기) amplification × không gian (space / 공간) amplification**.

> **Nối mạch:** **8. Ba amplification tạo một tam giác chi phí** nối từ **7. Leveled và size-tiered tối ưu các amplification khác nhau** sang **9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Ba amplification tạo một tam giác chi phí

Một logical byte có thể được ghi nhiều lần qua WAL, flush và compaction: đó là **khuếch đại ghi (write amplification / 쓰기 증폭)**. Một logical read có thể kiểm tra nhiều runs/blocks: **read amplification**. Dữ liệu cũ, tombstone và overlapping runs làm vật lý (physical / 물리적) bytes lớn hơn live logical dataset: **không gian (space / 공간) amplification**.

Giảm một trục thường đẩy chi phí sang trục khác. Compaction aggressive làm read/không gian (space / 공간) tốt hơn nhưng tăng background writes. Compaction lười giảm rewrite ngắn hạn nhưng giữ nhiều tệp (file / 파일)/phiên bản (version / 버전) hơn.

Trên SSD còn có amplification bên dưới: Flash Translation tầng (layer / 계층) có thể tự garbage-collect và rewrite erase blocks. Storage-engine ghi (write / 쓰기) amplification nhân với device-level amplification có thể làm bandwidth và endurance xấu hơn trực giác “SSD rất nhanh”.

> **Nối mạch:** **8. Ba amplification tạo một tam giác chi phí** đặt đầu vào cho **9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)**, rồi **10. Worked example: một key đi qua nhiều versions** mở rộng hệ quả.

## 9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)

Delete trong LSM thường không đi tìm và xóa ngay mọi bản sao cũ. Engine ghi **tombstone** để nói từ chuỗi (sequence / 시퀀스)/phiên bản (version / 버전) này trở đi key được coi là deleted.

Tombstone chỉ được loại khi engine biết không còn nơi nào old giá trị (value / 값) có thể tái xuất hiện sau khi tombstone biến mất. Nếu compaction drop tombstone ở mức (level / 수준) trên nhưng old giá trị (value / 값) còn ở mức (level / 수준) dưới, lookup sau đó có thể “hồi sinh” dữ liệu đã xóa.

Snapshot cũ, long-running read, replica lag, backup/PITR retention hoặc phạm vi (range / 범위) tombstone có thể kéo dài reclamation horizon. “Xóa logical” và “reclaim vật lý (physical / 물리적) bytes” là hai sự kiện khác nhau.

> **Nối mạch:** **9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)** nêu quy tắc; **10. Worked example: một key đi qua nhiều versions** thử quy tắc trong tình huống, rồi **11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)** mở rộng hệ quả.

## 10. Worked example: một key đi qua nhiều versions

Giả sử:

```text
SSTable cũ:       user:42 = "A"   seq=10
SSTable mới:      user:42 = "B"   seq=20
memtable:         tombstone        seq=30
```

Reader ở snapshot sau `seq=30` phải thấy key đã bị xóa. Reader ở snapshot hợp lệ tại `seq=25` vẫn có thể cần thấy `"B"`. Vì vậy compaction không thể đơn giản “giữ bản ghi (record / 레코드) mới nhất theo wall clock”. Nó phải tôn trọng visibility/reclamation rules của engine.

Khi không còn snapshot nào cần `seq<30`, và compaction đã bao phủ mọi nơi có thể chứa phiên bản (version / 버전) cũ, tombstone mới có thể được reclaim an toàn.

Ví dụ này nối trực tiếp LSM với MVCC: immutable sorted files chỉ là vật lý (physical / 물리적) biểu diễn (representation / 표현); tính đúng đắn (correctness / 정확성) vẫn do giao dịch (transaction / 트랜잭션)/phiên bản (version / 버전) ngữ nghĩa (semantics / 의미론) quyết định.

> **Nối mạch:** **10. Worked example: một key đi qua nhiều versions** nêu quy tắc; **11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)** thử quy tắc trong tình huống, rồi **12. Hot key, skew và compaction locality** mở rộng hệ quả.

## 11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)

Điểm (point / 지점) lookup có Bloom filter để skip nhiều files. phạm vi (range / 범위) scan lại thường phải merge iterators từ nhiều runs vì filter membership không giải quyết thứ tự (ordering / 순서) của cả khoảng.

Nếu tải công việc (workload / 워크로드) scan lớn, nhiều overlapping runs có thể làm CPU merge, decompression và khối (block / 블록) reads tăng đáng kể dù point-read benchmark đẹp. Compaction chiến lược (strategy / 전략) phải phản ánh tải công việc (workload / 워크로드) thật thay vì tối ưu duy nhất `GET(key)`.

> **Nối mạch:** **12. Hot key, skew và compaction locality** nối từ **11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)** sang **13. Foreground và background I/O tranh cùng tài nguyên (resource / 자원)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Hot key, skew và compaction locality

Traffic hiếm khi uniform. Một key phạm vi (range / 범위) nóng có thể nhận phần lớn writes, khiến một số SSTable/mức (level / 수준) bị rewrite liên tục trong khi dữ liệu khác gần như lạnh.

Partitioning có thể chia compaction công việc (work / 작업), nhưng skew vẫn có thể tạo hotspot trên một shard, lưu trữ (storage / 저장소) thiết bị (device / 장치) hoặc CPU group. “Cluster còn 50% sức chứa (capacity / 용량)” không giúp nếu partition chứa hot phạm vi (range / 범위) đã saturate compaction bandwidth.

> **Nối mạch:** **12. Hot key, skew và compaction locality** đặt vấn đề; **13. Foreground và background I/O tranh cùng tài nguyên (resource / 자원)** kiểm tra bằng chứng, rồi **14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)** mở rộng hệ quả.

## 13. Foreground và background I/O tranh cùng tài nguyên (resource / 자원)

Compaction gọi là background tác vụ (task / 작업) nhưng dùng thật CPU và lưu trữ (storage / 저장소) bandwidth. Nếu nó chiếm toàn thiết bị (device / 장치) hàng đợi (queue / 큐), foreground reads/commits tăng tail độ trễ (latency / 지연 시간). Nếu throttle quá mạnh, debt tăng và cuối cùng dẫn tới ghi (write / 쓰기) stall.

Controller phải cân bằng:

```text
ingest rate
compaction debt
foreground latency
available I/O bandwidth
space headroom
```

Đây là feedback-control bài toán (problem / 문제) tương tự hàng đợi (queue / 큐)/backpressure: trì hoãn maintenance quá lâu chỉ biến maintenance thành burst lớn hơn. Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

> **Nối mạch:** **13. Foreground và background I/O tranh cùng tài nguyên (resource / 자원)** đặt vấn đề; **14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)** kiểm tra bằng chứng, rồi **15. bằng chứng vận hành (production evidence / 운영 증거): đo cả foreground lẫn debt phía sau** mở rộng hệ quả.

## 14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)

Immutable tệp (file / 파일) giúp khôi phục (recovery / 복구) lập luận (reasoning / 추론) dễ hơn nhưng không làm lưu trữ (storage / 저장소) corruption biến mất. SSTable thường có checksum hoặc block-level integrity siêu dữ liệu (metadata / 메타데이터) để phát hiện bit corruption/truncated khối (block / 블록).

Checksum phát hiện không đồng nghĩa tự sửa. Repair có thể cần replica, backup hoặc rebuild từ nguồn (source / 소스) khác. Nếu compaction đọc corrupted đầu vào (input / 입력) rồi phát đầu ra (output / 출력) mới mà không detect đúng, corruption có thể lan sang trạng thái (state / 상태) mới.

> **Nối mạch:** **14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)** đặt vấn đề; **15. bằng chứng vận hành (production evidence / 운영 증거): đo cả foreground lẫn debt phía sau** kiểm tra bằng chứng, rồi **16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)** mở rộng hệ quả.

## 15. bằng chứng vận hành (production evidence / 운영 증거): đo cả foreground lẫn debt phía sau

Một LSM engine khỏe không thể được đánh giá chỉ bằng yêu cầu (request / 요청) thông lượng (throughput / 처리량). bằng chứng (evidence / 증거) hữu ích gồm compaction backlog/pending bytes, số run/tệp (file / 파일) theo mức (level / 수준), bytes read/ghi (write / 쓰기) bởi compaction, logical-vs-physical ghi (write / 쓰기) amplification, disk utilization/hàng đợi (queue / 큐) độ trễ (latency / 지연 시간), không gian (space / 공간) amplification, tombstone/phiên bản (version / 버전) retention, Bloom-filter hành vi (behavior / 동작), block-cache hit tỷ lệ (rate / 비율), ghi (write / 쓰기) stall/throttle thời gian (time / 시간) và độ trễ (latency / 지연 시간) phân phối (distribution / 분포) của điểm (point / 지점) read/phạm vi (range / 범위) scan/ghi (write / 쓰기).

Cần đọc các chỉ số (metric / 지표) như chuỗi nhân quả (causal chain / 인과 사슬):

```text
ingest tăng
→ L0 files tăng
→ compaction debt tăng
→ background I/O saturate
→ read latency tăng
→ write throttle/stall
```

Nếu chỉ thấy “disk 100%” rồi tăng hardware mà không biết bytes đến từ foreground hay compaction, ta chưa xác định cơ chế (mechanism / 메커니즘).

> **Nối mạch:** **15. bằng chứng vận hành (production evidence / 운영 증거): đo cả foreground lẫn debt phía sau** đặt vấn đề; **16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)** kiểm tra bằng chứng, rồi **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả.

## 16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)

Nếu điểm (point / 지점) lookup chậm nhưng lưu trữ (storage / 저장소) I/O thấp, chi phí (cost / 비용) có thể nằm ở CPU merge/filter/decompression hoặc bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작). Nếu compaction backlog tăng khi thiết bị (device / 장치) thông lượng (throughput / 처리량) đã đầy, lưu trữ (storage / 저장소) bandwidth là lower ràng buộc (constraint / 제약조건). Nếu ghi (write / 쓰기) amplification tăng sau tải công việc (workload / 워크로드) skew, compaction selection/bố cục (layout / 레이아웃) mới là đơn vị sở hữu (owner / 오너) của hành vi (behavior / 동작). Nếu tombstone không reclaim, hãy tìm snapshot/replica/retention horizon trước khi kết luận “compaction bị lỗi”.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“LSM ghi (write / 쓰기) chỉ là append nên ghi (write / 쓰기) amplification thấp.”** Foreground đường dẫn (path / 경로) append-friendly, nhưng compaction có thể rewrite cùng byte nhiều lần.

**“Bloom filter làm read O(1).”** Filter chỉ loại candidate files; lookup vẫn cần chỉ mục (index / 인덱스)/dữ liệu (data / 데이터) khối (block / 블록) và phiên bản (version / 버전) ngữ nghĩa (semantics / 의미론).

**“Delete xong là disk không gian (space / 공간) giảm ngay.”** Tombstone phải sống tới khi old versions có thể bị loại an toàn.

**“Compaction là background nên không ảnh hưởng yêu cầu (request / 요청).”** Nó tranh CPU, bộ nhớ (memory / 메모리) và I/O với foreground và có thể quyết định p99 độ trễ (latency / 지연 시간).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> LSM cây (tree / 트리) biến random mutation thành **append + immutable runs + background merge**. bất biến (invariant / 불변식) khó nhất không phải sort tệp (file / 파일), mà là giữ đúng lịch sử (history / 이력) khi một key tồn tại ở nhiều nơi và chỉ reclaim dữ liệu khi safe. hiệu năng (performance / 성능) phải được lập luận (reasoning / 추론) bằng ba amplification — read, ghi (write / 쓰기), không gian (space / 공간) — cùng compaction debt và lưu trữ (storage / 저장소) bandwidth. Fast foreground ghi (write / 쓰기) chỉ bền vững khi background maintenance theo kịp.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc cùng [MVCC, WAL và recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md), [Buffer pool và dirty-page management](./04_buffer_pool_replacement_and_dirty_page_management.md), [B+Tree internals](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md), [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [Queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
