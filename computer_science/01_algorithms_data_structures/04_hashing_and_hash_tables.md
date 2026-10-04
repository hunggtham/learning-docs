# Hashing và bảng băm (hash table / 해시 테이블)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Hashing và bảng băm (hash table / 해시 테이블)**. Route đi từ hash function và collision → chaining/open addressing → load factor và resizing → worst-case, adversarial input và correctness, để tốc độ trung bình không che khuất điều kiện thất bại.

Ta muốn map key như `userId` sang giá trị (value / 값) mà không scan toàn bộ collection. Nếu key nằm trong universe lớn, direct-address bảng (table / 테이블) quá tốn bộ nhớ (memory / 메모리). Hashing giải quyết bằng cách dùng một hàm (function / 함수) nén key thành một integer/bucket chỉ mục (index / 인덱스) nhỏ hơn.

## Băm (hash / 해시) hàm (function / 함수) đang làm gì?

Băm (hash / 해시) hàm (function / 함수) ánh xạ đầu vào (input / 입력) có kích thước tùy ý vào fixed-size giá trị (value / 값). Với bảng băm (hash table / 해시 테이블), ta thường lấy băm (hash / 해시) mã (code / 코드) rồi map vào bucket phạm vi (range / 범위).

Vì number of possible keys lớn hơn buckets, collision (충돌) là tất yếu theo pigeonhole principle. Mục tiêu không phải tránh collision hoàn toàn mà phân bố keys đủ đều và xử lý collision đúng.

Một bảng băm (hash table / 해시 테이블) đúng cần equality đặc tả hợp đồng (contract / 계약) phù hợp: nếu `a == b` thì hashes phải tương thích để lookup tìm cùng location. Trong Java, đây là lý do `equals()` và `hashCode()` phải nhất quán.

> **Nối mạch:** Hash function ánh xạ key vào bucket; chaining giữ nhiều entry trong bucket, open addressing tìm vị trí khác, còn load factor dự báo collision và chi phí lookup.

## Separate chaining và open addressing

Separate chaining mỗi bucket chứa collection entries, như linked danh sách (list / 목록) hoặc cây (tree / 트리). Lookup băm (hash / 해시) tới bucket rồi tìm kiếm (search / 검색) trong bucket.

Open addressing giữ entries ngay trong bảng (table / 테이블); collision trigger probing như tuyến tính (linear / 선형)/quadratic probing hoặc double hashing. Empty/deleted markers trở thành phần quan trọng của bất biến (invariant / 불변식).

Open addressing thường có locality tốt nhưng hiệu năng (performance / 성능) suy giảm nhanh khi bảng (table / 테이블) quá đầy. Chaining linh hoạt tải (load / 로드) hơn nhưng thêm pointer/đối tượng (object / 객체) overhead.

> **Nối mạch:** **Tải (load / 로드) factor** nối từ **Separate chaining và open addressing** sang **Expected O(1) dựa trên các giả định (assumptions / 가정들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tải (load / 로드) factor

Tải (load / 로드) factor `α = n/m`, với n entries và m buckets/slots. Khi α tăng, collision/probe length tăng. động (dynamic / 동적) bảng băm (hash table / 해시 테이블) resize khi vượt threshold, rehash entries vào bảng (table / 테이블) lớn hơn.

Resize là thao tác (operation / 연산) O(n), nhưng nếu growth geometric, insert có thể amortized O(1), tương tự động (dynamic / 동적) array.

> **Nối mạch:** **Expected O(1) dựa trên các giả định (assumptions / 가정들)** nối từ **Tải (load / 로드) factor** sang **Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Expected O(1) dựa trên các giả định (assumptions / 가정들)

Bảng băm (hash table / 해시 테이블) thường được mô tả lookup expected O(1), nhưng guarantee này phụ thuộc băm (hash / 해시) phân phối (distribution / 분포) và tải (load / 로드) factor. Nếu mọi keys collide, lookup có thể O(n). Một attacker có thể cố tạo collision patterns nếu băm (hash / 해시) hàm (function / 함수) predictable, tạo hash-flooding DoS; thời gian chạy (runtime / 런타임)/khung phần mềm (framework / 프레임워크) có thể randomize seed hoặc treeify buckets để giảm rủi ro (risk / 위험).

> **Nối mạch:** **Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)** nối từ **Expected O(1) dựa trên các giả định (assumptions / 가정들)** sang **Mutable key hazard**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)

Data-structure băm (hash / 해시) ưu tiên speed và phân phối (distribution / 분포). Cryptographic băm (hash / 해시) cần thêm properties như preimage resistance, second-preimage resistance và collision resistance. Dùng `hashCode()` để lưu password là sai category.

Xem [Cryptography foundations](../07_security_reliability/01_cryptography_foundations.md).

> **Nối mạch:** **Mutable key hazard** nối từ **Bảng băm (hash table / 해시 테이블) khác cryptographic băm (hash / 해시)** sang **Băm (hash / 해시) set như map đặc biệt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mutable key hazard

Nếu key được insert rồi fields tham gia băm (hash / 해시)/equality bị mutate, băm (hash / 해시) có thể đổi. Entry vẫn nằm bucket cũ nhưng lookup tính bucket mới, khiến “key tồn tại mà tìm không thấy”. Vì vậy keys nên immutable theo equality/băm (hash / 해시) định danh (identity / 식별자) trong thời gian nằm trong map/set.

> **Nối mạch:** **Băm (hash / 해시) set như map đặc biệt** nối từ **Mutable key hazard** sang **Consistent hashing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Băm (hash / 해시) set như map đặc biệt

Set membership có thể implement bằng bảng băm (hash table / 해시 테이블) chỉ lưu keys hoặc map keys tới dummy giá trị (value / 값). Từ lớp trừu tượng (abstraction / 추상화) perspective, HashSet và HashMap chia sẻ cơ chế phân phối (distribution / 분포)/collision nhưng expose đặc tả hợp đồng (contract / 계약) khác.

> **Nối mạch:** **Consistent hashing** nối từ **Băm (hash / 해시) set như map đặc biệt** sang **Bloom filter: probabilistic membership**, vì cơ chế trước tạo đầu vào cho bước sau.

## Consistent hashing

Trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들), simple `hash(key) mod N` remap rất nhiều keys khi N thay đổi. Consistent hashing đặt nodes và keys trên băm (hash / 해시) ring để thêm/bớt nút (node / 노드) chỉ di chuyển một phần keyspace. Đây là ví dụ cùng mô hình tư duy (mental model / 사고 모델) hashing được nâng từ in-memory cấu trúc (structure / 구조) lên partition placement.

> **Nối mạch:** **Bloom filter: probabilistic membership** nối từ **Consistent hashing** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bloom filter: probabilistic membership

Bloom filter dùng nhiều băm (hash / 해시) functions và bit array. Nó có thể nói “definitely not present” hoặc “possibly present”, chấp nhận false positives nhưng không false negatives nếu không có deletion biến thể. cơ sở dữ liệu (database / 데이터베이스)/lưu trữ (storage / 저장소) hệ thống (system / 시스템) dùng Bloom filter để tránh expensive I/O cho keys chắc chắn không tồn tại.

Đây là time-space-accuracy sự đánh đổi (trade-off / 트레이드오프): một ít bộ nhớ (memory / 메모리) giảm nhiều lookups nhưng không lưu actual values.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Bloom filter: probabilistic membership**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> bảng băm (hash table / 해시 테이블) đổi **ordered cấu trúc (structure / 구조)** lấy **direct probabilistic placement**. Nhanh vì băm (hash / 해시) đưa ta gần vị trí cần tìm; collision chính sách (policy / 정책) và tải (load / 로드) factor quyết định phần việc còn lại.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“băm (hash / 해시) không collision nếu hàm (function / 함수) tốt.”** Collision là toán học tất yếu khi lĩnh vực (domain / 도메인) lớn hơn đầu ra (output / 출력) không gian (space / 공간).

**“O(1) nghĩa guaranteed.”** Thường là expected/amortized dưới các giả định (assumptions / 가정들); worst-case có thể khác.

**“Hashing và encryption giống nhau vì đều biến dữ liệu.”** băm (hash / 해시) là one-way digest; encryption thiết kế reversible với key. Data-structure băm (hash / 해시) còn có mục tiêu khác cryptographic băm (hash / 해시).

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Hashing liên quan [database hash indexes](../05_data_databases/03_indexes_and_query_execution.md), [password/MAC hashing](../07_security_reliability/01_cryptography_foundations.md), [distributed partitioning](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) và [cache key design](../08_software_systems/02_performance_capacity_and_scalability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
