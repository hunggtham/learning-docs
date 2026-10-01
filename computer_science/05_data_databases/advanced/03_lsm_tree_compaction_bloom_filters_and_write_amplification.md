# LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu và bất biến (invariant / 불변식) của LSM** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **2. ghi (write / 쓰기) đường dẫn (path / 경로): foreground nhanh vì chưa tổ chức xong dữ liệu** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **1. Bài toán ban đầu và bất biến (invariant / 불변식) của LSM** nêu điều cần giải thích; **2. ghi (write / 쓰기) đường dẫn (path / 경로): foreground nhanh vì chưa tổ chức xong dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. ghi (write / 쓰기) đường dẫn (path / 경로): foreground nhanh vì chưa tổ chức xong dữ liệu

Ghi (write / 쓰기) thường được append vào **nhật ký ghi trước (Write-Ahead Log, WAL / 선행 기록 로그)** rồi cập nhật **memtable** trong RAM. Khi memtable đạt ngưỡng, engine đóng băng nó thành immutable memtable và flush thành **Sorted String bảng (table / 테이블) (SSTable)** hoặc sorted run tương tự.

Flush tuần tự thường thân thiện với khối (block / 블록) lưu trữ (storage / 저장소) hơn việc sửa ngẫu nhiên nhiều page. Nhưng cùng một logical key có thể tồn tại ở memtable, tệp (file / 파일) mới và nhiều tệp (file / 파일) cũ. Vì vậy ghi (write / 쓰기) độ trễ (latency / 지연 시간) thấp tại `PUT` không phải toàn bộ chi phí (cost / 비용) của ghi (write / 쓰기).

Một benchmark chỉ đo “bao nhiêu PUT/s trước khi compaction chạy nặng” dễ đo burst sức chứa (capacity / 용량) thay vì **sustainable ghi (write / 쓰기) thông lượng (throughput / 처리량)**.

> **Chuyển mạch:** Ở chặng này của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **2. ghi (write / 쓰기) đường dẫn (path / 경로): foreground nhanh vì chưa tổ chức xong dữ liệu** nêu điều cần giải thích; **3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Read đường dẫn (path / 경로) là phép tìm kiếm qua nhiều lớp lịch sử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn

SSTable thường immutable sau khi hoàn tất. Reader có thể đọc tệp (file / 파일) mà không phải phối hợp với writer sửa nội dung ngay trong tệp (file / 파일) đó. Compaction tạo tệp (file / 파일) mới rồi cập nhật siêu dữ liệu (metadata / 메타데이터) để publish một tập tệp (file / 파일) mới.

Engine vì thế thường có siêu dữ liệu (metadata / 메타데이터) kiểu **phiên bản (version / 버전) set / manifest** mô tả SSTable nào thuộc logical trạng thái (state / 상태) hiện tại. bất biến (invariant / 불변식) không chỉ là “tệp (file / 파일) mới đã được ghi”; siêu dữ liệu (metadata / 메타데이터) phải chuyển sang phiên bản (version / 버전) mới theo crash-safe giao thức (protocol / 프로토콜).

Nếu tiến trình (process / 프로세스) crash sau khi tạo đầu ra (output / 출력) tệp (file / 파일) nhưng trước khi publish manifest, tệp (file / 파일) có thể thành orphan và được cleanup sau. Nếu siêu dữ liệu (metadata / 메타데이터) publish trước khi tệp (file / 파일) cần thiết thực sự durable, khôi phục (recovery / 복구) có thể trỏ tới trạng thái (state / 상태) không đầy đủ. Đây là cùng family với filesystem crash consistency: **đối tượng (object / 객체) phải tồn tại đủ chắc trước khi pointer/siêu dữ liệu (metadata / 메타데이터) tuyên bố nó là live trạng thái (state / 상태)**.

Đọc thêm [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [MVCC/WAL/recovery](./00_mvcc_visibility_wal_and_recovery_internals.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **3. Immutable tệp (file / 파일) tạo tính đồng thời (concurrency / 동시성) đơn giản hơn nhưng cần publication an toàn** xác định đầu vào; **4. Read đường dẫn (path / 경로) là phép tìm kiếm qua nhiều lớp lịch sử** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. Bloom filter giải bài toán negative lookup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **4. Read đường dẫn (path / 경로) là phép tìm kiếm qua nhiều lớp lịch sử** xác định đầu vào; **5. Bloom filter giải bài toán negative lookup** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. Compaction là cơ chế trả nợ, không phải housekeeping phụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Bloom filter giải bài toán negative lookup

**Bộ lọc Bloom (Bloom filter / 블룸 필터)** là cấu trúc xác suất cho membership kiểm thử (test / 테스트). Với cấu hình đúng, nó có thể trả lời chắc chắn “key không ở đây”, hoặc “key có thể ở đây”. False positive làm engine đọc thêm tệp (file / 파일) vô ích; false negative không được phép xảy ra theo đặc tả hợp đồng (contract / 계약) thông thường của filter.

Bloom filter đặc biệt có giá trị khi lookup hỏi key không tồn tại hoặc key chỉ nằm trong một trong nhiều runs. Nhưng filter không miễn phí: nó chiếm bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소) và cần băm (hash / 해시) công việc (work / 작업).

Bits-per-key quá thấp làm false-positive tỷ lệ (rate / 비율) tăng và read amplification quay lại dưới dạng I/O. Dành quá nhiều bộ nhớ (memory / 메모리) cho filters lại có thể làm bộ nhớ đệm (cache / 캐시) dữ liệu (data / 데이터)/chỉ mục (index / 인덱스) blocks thiếu. Đây là sự đánh đổi (trade-off / 트레이드오프) trong cùng một bộ nhớ (memory / 메모리) ngân sách (budget / 예산).

> **Chuyển mạch:** Ở chặng này của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **5. Bloom filter giải bài toán negative lookup** xác định đầu vào; **6. Compaction là cơ chế trả nợ, không phải housekeeping phụ** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **7. Leveled và size-tiered tối ưu các amplification khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Compaction là cơ chế trả nợ, không phải housekeeping phụ

**Hợp nhất nền (compaction / 컴팩션)** đọc nhiều sorted runs, merge chúng theo key/phiên bản (version / 버전) thứ tự (order / 순서), ghi đầu ra (output / 출력) mới rồi chuyển siêu dữ liệu (metadata / 메타데이터) sang tập tệp (file / 파일) mới. Trong quá trình này engine có thể loại phiên bản (version / 버전) bị supersede, reclaim tombstone đã an toàn và giảm overlap giữa files.

Compaction tiêu CPU, bộ nhớ (memory / 메모리) buffer, read bandwidth và ghi (write / 쓰기) bandwidth. Nếu ingest tạo debt nhanh hơn compaction trả được, số runs/mức (level / 수준) overlap tăng. Read amplification, không gian (space / 공간) amplification và background I/O cùng tăng.

Đến một điểm engine phải throttle hoặc stall foreground writes để không tích debt vô hạn. Vì vậy `write stall time`, pending compaction bytes và mức (level / 수준) kích thước (size / 크기) thường quan trọng hơn một con số ghi (write / 쓰기) độ trễ (latency / 지연 시간) trung bình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **6. Compaction là cơ chế trả nợ, không phải housekeeping phụ** xác định đầu vào; **7. Leveled và size-tiered tối ưu các amplification khác nhau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **8. Ba amplification tạo một tam giác chi phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Leveled và size-tiered tối ưu các amplification khác nhau

**Leveled compaction** cố giảm overlap giữa files trong một mức (level / 수준). điểm (point / 지점) read có thể cần kiểm tra ít candidate hơn, nhưng một byte có thể bị rewrite nhiều lần khi được đẩy qua các mức (level / 수준).

**Size-tiered compaction** hoặc các chiến lược tiered giữ nhiều runs cùng cỡ rồi merge theo batch. Cách này thường giảm ghi (write / 쓰기) amplification nhưng có thể tăng số runs mà read phải xét và giữ duplicate versions lâu hơn.

Không có chiến lược (strategy / 전략) tốt tuyệt đối. tải công việc (workload / 워크로드) read-heavy với strict p99 lookup khác ingest-heavy; phạm vi (range / 범위) scan khác điểm (point / 지점) lookup. Quyết định compaction là quyết định về **read amplification × ghi (write / 쓰기) amplification × không gian (space / 공간) amplification**.

> **Chuyển mạch:** Trong **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **8. Ba amplification tạo một tam giác chi phí** tiếp nhận điểm tựa từ **7. Leveled và size-tiered tối ưu các amplification khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Ba amplification tạo một tam giác chi phí

Một logical byte có thể được ghi nhiều lần qua WAL, flush và compaction: đó là **khuếch đại ghi (write amplification / 쓰기 증폭)**. Một logical read có thể kiểm tra nhiều runs/blocks: **read amplification**. Dữ liệu cũ, tombstone và overlapping runs làm vật lý (physical / 물리적) bytes lớn hơn live logical dataset: **không gian (space / 공간) amplification**.

Giảm một trục thường đẩy chi phí sang trục khác. Compaction aggressive làm read/không gian (space / 공간) tốt hơn nhưng tăng background writes. Compaction lười giảm rewrite ngắn hạn nhưng giữ nhiều tệp (file / 파일)/phiên bản (version / 버전) hơn.

Trên SSD còn có amplification bên dưới: Flash Translation tầng (layer / 계층) có thể tự garbage-collect và rewrite erase blocks. Storage-engine ghi (write / 쓰기) amplification nhân với device-level amplification có thể làm bandwidth và endurance xấu hơn trực giác “SSD rất nhanh”.

> **Chuyển mạch:** Ở chặng này của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **8. Ba amplification tạo một tam giác chi phí** xác định đầu vào; **9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. Worked example: một key đi qua nhiều versions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)

Delete trong LSM thường không đi tìm và xóa ngay mọi bản sao cũ. Engine ghi **tombstone** để nói từ chuỗi (sequence / 시퀀스)/phiên bản (version / 버전) này trở đi key được coi là deleted.

Tombstone chỉ được loại khi engine biết không còn nơi nào old giá trị (value / 값) có thể tái xuất hiện sau khi tombstone biến mất. Nếu compaction drop tombstone ở mức (level / 수준) trên nhưng old giá trị (value / 값) còn ở mức (level / 수준) dưới, lookup sau đó có thể “hồi sinh” dữ liệu đã xóa.

Snapshot cũ, long-running read, replica lag, backup/PITR retention hoặc phạm vi (range / 범위) tombstone có thể kéo dài reclamation horizon. “Xóa logical” và “reclaim vật lý (physical / 물리적) bytes” là hai sự kiện khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **9. Tombstone tồn tại để delete đi cùng append-only ghi (write / 쓰기) đường dẫn (path / 경로)** cho ta quy tắc; **10. Worked example: một key đi qua nhiều versions** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **10. Worked example: một key đi qua nhiều versions** cho ta quy tắc; **11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **12. Hot key, skew và compaction locality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)

Điểm (point / 지점) lookup có Bloom filter để skip nhiều files. phạm vi (range / 범위) scan lại thường phải merge iterators từ nhiều runs vì filter membership không giải quyết thứ tự (ordering / 순서) của cả khoảng.

Nếu tải công việc (workload / 워크로드) scan lớn, nhiều overlapping runs có thể làm CPU merge, decompression và khối (block / 블록) reads tăng đáng kể dù point-read benchmark đẹp. Compaction chiến lược (strategy / 전략) phải phản ánh tải công việc (workload / 워크로드) thật thay vì tối ưu duy nhất `GET(key)`.

> **Chuyển mạch:** Ở chặng này của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **12. Hot key, skew và compaction locality** tiếp nhận điểm tựa từ **11. phạm vi (range / 범위) scan làm lộ merge chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Foreground và background I/O tranh cùng tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Hot key, skew và compaction locality

Traffic hiếm khi uniform. Một key phạm vi (range / 범위) nóng có thể nhận phần lớn writes, khiến một số SSTable/mức (level / 수준) bị rewrite liên tục trong khi dữ liệu khác gần như lạnh.

Partitioning có thể chia compaction công việc (work / 작업), nhưng skew vẫn có thể tạo hotspot trên một shard, lưu trữ (storage / 저장소) thiết bị (device / 장치) hoặc CPU group. “Cluster còn 50% sức chứa (capacity / 용량)” không giúp nếu partition chứa hot phạm vi (range / 범위) đã saturate compaction bandwidth.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **12. Hot key, skew và compaction locality** nêu điều cần giải thích; **13. Foreground và background I/O tranh cùng tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **13. Foreground và background I/O tranh cùng tài nguyên (resource / 자원)** nêu điều cần giải thích; **14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. bằng chứng vận hành (production evidence / 운영 증거): đo cả foreground lẫn debt phía sau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)

Immutable tệp (file / 파일) giúp khôi phục (recovery / 복구) lập luận (reasoning / 추론) dễ hơn nhưng không làm lưu trữ (storage / 저장소) corruption biến mất. SSTable thường có checksum hoặc block-level integrity siêu dữ liệu (metadata / 메타데이터) để phát hiện bit corruption/truncated khối (block / 블록).

Checksum phát hiện không đồng nghĩa tự sửa. Repair có thể cần replica, backup hoặc rebuild từ nguồn (source / 소스) khác. Nếu compaction đọc corrupted đầu vào (input / 입력) rồi phát đầu ra (output / 출력) mới mà không detect đúng, corruption có thể lan sang trạng thái (state / 상태) mới.

> **Chuyển mạch:** Ở chặng này của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **14. Corruption và checksums thay đổi dạng thất bại (failure mode / 실패 모드)** nêu điều cần giải thích; **15. bằng chứng vận hành (production evidence / 운영 증거): đo cả foreground lẫn debt phía sau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **15. bằng chứng vận hành (production evidence / 운영 증거): đo cả foreground lẫn debt phía sau** nêu điều cần giải thích; **16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)

Nếu điểm (point / 지점) lookup chậm nhưng lưu trữ (storage / 저장소) I/O thấp, chi phí (cost / 비용) có thể nằm ở CPU merge/filter/decompression hoặc bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작). Nếu compaction backlog tăng khi thiết bị (device / 장치) thông lượng (throughput / 처리량) đã đầy, lưu trữ (storage / 저장소) bandwidth là lower ràng buộc (constraint / 제약조건). Nếu ghi (write / 쓰기) amplification tăng sau tải công việc (workload / 워크로드) skew, compaction selection/bố cục (layout / 레이아웃) mới là đơn vị sở hữu (owner / 오너) của hành vi (behavior / 동작). Nếu tombstone không reclaim, hãy tìm snapshot/replica/retention horizon trước khi kết luận “compaction bị lỗi”.

> **Chuyển mạch:** Trong **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **16. Debugging theo lower lớp trừu tượng (abstraction / 추상화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“LSM ghi (write / 쓰기) chỉ là append nên ghi (write / 쓰기) amplification thấp.”** Foreground đường dẫn (path / 경로) append-friendly, nhưng compaction có thể rewrite cùng byte nhiều lần.

**“Bloom filter làm read O(1).”** Filter chỉ loại candidate files; lookup vẫn cần chỉ mục (index / 인덱스)/dữ liệu (data / 데이터) khối (block / 블록) và phiên bản (version / 버전) ngữ nghĩa (semantics / 의미론).

**“Delete xong là disk không gian (space / 공간) giảm ngay.”** Tombstone phải sống tới khi old versions có thể bị loại an toàn.

**“Compaction là background nên không ảnh hưởng yêu cầu (request / 요청).”** Nó tranh CPU, bộ nhớ (memory / 메모리) và I/O với foreground và có thể quyết định p99 độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Ở chặng này của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> LSM cây (tree / 트리) biến random mutation thành **append + immutable runs + background merge**. bất biến (invariant / 불변식) khó nhất không phải sort tệp (file / 파일), mà là giữ đúng lịch sử (history / 이력) khi một key tồn tại ở nhiều nơi và chỉ reclaim dữ liệu khi safe. hiệu năng (performance / 성능) phải được lập luận (reasoning / 추론) bằng ba amplification — read, ghi (write / 쓰기), không gian (space / 공간) — cùng compaction debt và lưu trữ (storage / 저장소) bandwidth. Fast foreground ghi (write / 쓰기) chỉ bền vững khi background maintenance theo kịp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LSM cây (tree / 트리), compaction, Bloom filters và ghi (write / 쓰기) amplification**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [MVCC, WAL và recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md), [Buffer pool và dirty-page management](./04_buffer_pool_replacement_and_dirty_page_management.md), [B+Tree internals](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md), [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [Queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
