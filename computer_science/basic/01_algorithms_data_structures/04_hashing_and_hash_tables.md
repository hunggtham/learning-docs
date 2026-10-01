# Hashing và bảng băm (hash table / 해시 테이블)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hashing và bảng băm (hash table / 해시 테이블)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Băm (hash / 해시) hàm (function / 함수) đang làm gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Separate chaining và open addressing** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Ta muốn map key như `userId` sang giá trị (value / 값) mà không scan toàn bộ collection. Nếu key nằm trong universe lớn, direct-address bảng (table / 테이블) quá tốn bộ nhớ (memory / 메모리). Hashing giải quyết bằng cách dùng một hàm (function / 함수) nén key thành một integer/bucket chỉ mục (index / 인덱스) nhỏ hơn.

## Băm (hash / 해시) hàm (function / 함수) đang làm gì?

Băm (hash / 해시) hàm (function / 함수) ánh xạ đầu vào (input / 입력) có kích thước tùy ý vào fixed-size giá trị (value / 값). Với bảng băm (hash table / 해시 테이블), ta thường lấy băm (hash / 해시) mã (code / 코드) rồi map vào bucket phạm vi (range / 범위).

Vì number of possible keys lớn hơn buckets, collision (충돌) là tất yếu theo pigeonhole principle. Mục tiêu không phải tránh collision hoàn toàn mà phân bố keys đủ đều và xử lý collision đúng.

Một bảng băm (hash table / 해시 테이블) đúng cần equality đặc tả hợp đồng (contract / 계약) phù hợp: nếu `a == b` thì hashes phải tương thích để lookup tìm cùng location. Trong Java, đây là lý do `equals()` và `hashCode()` phải nhất quán.

> **Chuyển mạch:** Trong **Hashing và bảng băm (hash table / 해시 테이블)**, **Separate chaining và open addressing** tiếp nhận điểm tựa từ **Băm (hash / 해시) hàm (function / 함수) đang làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tải (load / 로드) factor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Separate chaining và open addressing

Separate chaining mỗi bucket chứa collection entries, như linked danh sách (list / 목록) hoặc cây (tree / 트리). Lookup băm (hash / 해시) tới bucket rồi tìm kiếm (search / 검색) trong bucket.

Open addressing giữ entries ngay trong bảng (table / 테이블); collision trigger probing như tuyến tính (linear / 선형)/quadratic probing hoặc double hashing. Empty/deleted markers trở thành phần quan trọng của bất biến (invariant / 불변식).

Open addressing thường có locality tốt nhưng hiệu năng (performance / 성능) suy giảm nhanh khi bảng (table / 테이블) quá đầy. Chaining linh hoạt tải (load / 로드) hơn nhưng thêm pointer/đối tượng (object / 객체) overhead.

> **Chuyển mạch:** Ở chặng này của **Hashing và bảng băm (hash table / 해시 테이블)**, **Tải (load / 로드) factor** tiếp nhận điểm tựa từ **Separate chaining và open addressing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Expected O(1) dựa trên các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tải (load / 로드) factor

Tải (load / 로드) factor `α = n/m`, với n entries và m buckets/slots. Khi α tăng, collision/probe length tăng. động (dynamic / 동적) bảng băm (hash table / 해시 테이블) resize khi vượt threshold, rehash entries vào bảng (table / 테이블) lớn hơn.

Resize là thao tác (operation / 연산) O(n), nhưng nếu growth geometric, insert có thể amortized O(1), tương tự động (dynamic / 동적) array.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hashing và bảng băm (hash table / 해시 테이블)**, **Expected O(1) dựa trên các giả định (assumptions / 가정들)** tiếp nhận điểm tựa từ **Tải (load / 로드) factor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Expected O(1) dựa trên các giả định (assumptions / 가정들)

Bảng băm (hash table / 해시 테이블) thường được mô tả lookup expected O(1), nhưng guarantee này phụ thuộc băm (hash / 해시) phân phối (distribution / 분포) và tải (load / 로드) factor. Nếu mọi keys collide, lookup có thể O(n). Một attacker có thể cố tạo collision patterns nếu băm (hash / 해시) hàm (function / 함수) predictable, tạo hash-flooding DoS; thời gian chạy (runtime / 런타임)/khung phần mềm (framework / 프레임워크) có thể randomize seed hoặc treeify buckets để giảm rủi ro (risk / 위험).

> **Chuyển mạch:** Trong **Hashing và bảng băm (hash table / 해시 테이블)**, **Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)** tiếp nhận điểm tựa từ **Expected O(1) dựa trên các giả định (assumptions / 가정들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mutable key hazard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)

Data-structure băm (hash / 해시) ưu tiên speed và phân phối (distribution / 분포). Cryptographic băm (hash / 해시) cần thêm properties như preimage resistance, second-preimage resistance và collision resistance. Dùng `hashCode()` để lưu password là sai category.

Xem [Cryptography foundations](../07_security_reliability/01_cryptography_foundations.md).

> **Chuyển mạch:** Ở chặng này của **Hashing và bảng băm (hash table / 해시 테이블)**, **Mutable key hazard** tiếp nhận điểm tựa từ **Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Băm (hash / 해시) set như map đặc biệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mutable key hazard

Nếu key được insert rồi fields tham gia băm (hash / 해시)/equality bị mutate, băm (hash / 해시) có thể đổi. Entry vẫn nằm bucket cũ nhưng lookup tính bucket mới, khiến “key tồn tại mà tìm không thấy”. Vì vậy keys nên immutable theo equality/băm (hash / 해시) định danh (identity / 식별자) trong thời gian nằm trong map/set.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hashing và bảng băm (hash table / 해시 테이블)**, **Băm (hash / 해시) set như map đặc biệt** tiếp nhận điểm tựa từ **Mutable key hazard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Consistent hashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Băm (hash / 해시) set như map đặc biệt

Set membership có thể implement bằng bảng băm (hash table / 해시 테이블) chỉ lưu keys hoặc map keys tới dummy giá trị (value / 값). Từ lớp trừu tượng (abstraction / 추상화) perspective, HashSet và HashMap chia sẻ cơ chế phân phối (distribution / 분포)/collision nhưng expose đặc tả hợp đồng (contract / 계약) khác.

> **Chuyển mạch:** Trong **Hashing và bảng băm (hash table / 해시 테이블)**, **Consistent hashing** tiếp nhận điểm tựa từ **Băm (hash / 해시) set như map đặc biệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bloom filter: probabilistic membership** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consistent hashing

Trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들), simple `hash(key) mod N` remap rất nhiều keys khi N thay đổi. Consistent hashing đặt nodes và keys trên băm (hash / 해시) ring để thêm/bớt nút (node / 노드) chỉ di chuyển một phần keyspace. Đây là ví dụ cùng mô hình tư duy (mental model / 사고 모델) hashing được nâng từ in-memory cấu trúc (structure / 구조) lên partition placement.

> **Chuyển mạch:** Ở chặng này của **Hashing và bảng băm (hash table / 해시 테이블)**, **Bloom filter: probabilistic membership** tiếp nhận điểm tựa từ **Consistent hashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bloom filter: probabilistic membership

Bloom filter dùng nhiều băm (hash / 해시) functions và bit array. Nó có thể nói “definitely not present” hoặc “possibly present”, chấp nhận false positives nhưng không false negatives nếu không có deletion biến thể. cơ sở dữ liệu (database / 데이터베이스)/lưu trữ (storage / 저장소) hệ thống (system / 시스템) dùng Bloom filter để tránh expensive I/O cho keys chắc chắn không tồn tại.

Đây là time-space-accuracy sự đánh đổi (trade-off / 트레이드오프): một ít bộ nhớ (memory / 메모리) giảm nhiều lookups nhưng không lưu actual values.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hashing và bảng băm (hash table / 해시 테이블)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Bloom filter: probabilistic membership** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> bảng băm (hash table / 해시 테이블) đổi **ordered cấu trúc (structure / 구조)** lấy **direct probabilistic placement**. Nhanh vì băm (hash / 해시) đưa ta gần vị trí cần tìm; collision chính sách (policy / 정책) và tải (load / 로드) factor quyết định phần việc còn lại.

> **Chuyển mạch:** Trong **Hashing và bảng băm (hash table / 해시 테이블)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“băm (hash / 해시) không collision nếu hàm (function / 함수) tốt.”** Collision là toán học tất yếu khi lĩnh vực (domain / 도메인) lớn hơn đầu ra (output / 출력) không gian (space / 공간).

**“O(1) nghĩa guaranteed.”** Thường là expected/amortized dưới các giả định (assumptions / 가정들); worst-case có thể khác.

**“Hashing và encryption giống nhau vì đều biến dữ liệu.”** băm (hash / 해시) là one-way digest; encryption thiết kế reversible với key. Data-structure băm (hash / 해시) còn có mục tiêu khác cryptographic băm (hash / 해시).

> **Chuyển mạch:** Ở chặng này của **Hashing và bảng băm (hash table / 해시 테이블)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Hashing liên quan [database hash indexes](../05_data_databases/03_indexes_and_query_execution.md), [password/MAC hashing](../07_security_reliability/01_cryptography_foundations.md), [distributed partitioning](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) và [cache key design](../08_software_systems/02_performance_capacity_and_scalability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
