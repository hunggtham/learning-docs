# CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tính đồng thời (concurrency / 동시성) không chỉ là “cùng timestamp”** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Happens-before và logical clocks** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Strong consensus không phải lựa chọn duy nhất. Với collaborative editing, counters, sets hoặc geo-distributed applications, hệ thống đôi khi ưu tiên cục bộ (local / 로컬) availability và chấp nhận replicas tạm thời khác nhau. Khi đó câu hỏi là làm sao merge concurrent updates mà không phụ thuộc một coordinator toàn cục.

## Tính đồng thời (concurrency / 동시성) không chỉ là “cùng timestamp”

Hai events concurrent khi không có nhân quả (causal / 인과적) thứ tự (order / 순서) biết được giữa chúng. Nếu A tạo sự kiện (event / 이벤트) rồi B quan sát A trước khi tạo B, A → B. Nếu hai clients offline cập nhật (update / 업데이트) độc lập, hai events có thể incomparable.

Wall-clock timestamps không đủ đáng tin để suy ra causality vì clock skew và mạng (network / 네트워크) delay.

> **Chuyển mạch:** Trong **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **Happens-before và logical clocks** tiếp nhận điểm tựa từ **Tính đồng thời (concurrency / 동시성) không chỉ là “cùng timestamp”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CRDT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Happens-before và logical clocks

Lamport clock tạo thứ tự (ordering / 순서) nhất quán với causality nhưng không phân biệt đầy đủ tính đồng thời (concurrency / 동시성). véc-tơ (vector / 벡터) clocks/phiên bản (version / 버전) vectors có thể biểu diễn nhân quả (causal / 인과적) histories chi tiết hơn với siêu dữ liệu (metadata / 메타데이터) lớn hơn.

Nhân quả (causal / 인과적) consistency đảm bảo tác động (effect / 효과) không xuất hiện trước cause: nếu comment trả lời một post, replica không nên hiển thị reply trước post mà người dùng (user / 사용자) đã dựa vào.

> **Chuyển mạch:** Ở chặng này của **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **CRDT** tiếp nhận điểm tựa từ **Happens-before và logical clocks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **G-Counter và PN-Counter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CRDT

**Conflict-Free Replicated dữ liệu (data / 데이터) kiểu (type / 타입)** thiết kế trạng thái (state / 상태)/operations sao cho replicas có thể merge concurrent updates theo algebraic properties đảm bảo convergence.

State-based CRDT thường cần merge thao tác (operation / 연산) có tính commutative, associative và idempotent; join-semilattice cung cấp formal cấu trúc (structure / 구조) cho monotonic merge.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **G-Counter và PN-Counter** tiếp nhận điểm tựa từ **CRDT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sets và remove ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## G-Counter và PN-Counter

Grow-only counter giữ thành phần (component / 컴포넌트) per replica và merge bằng element-wise max. Tổng các components cho giá trị (value / 값). Vì merge max idempotent, duplicate trạng thái (state / 상태) exchange không làm double count.

PN-Counter kết hợp hai grow-only counters cho increments và decrements. siêu dữ liệu (metadata / 메타데이터) tăng theo replica định danh (identity / 식별자), minh họa sự đánh đổi (trade-off / 트레이드오프) giữa coordination-free merge và trạng thái (state / 상태) overhead.

> **Chuyển mạch:** Trong **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **Sets và remove ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **G-Counter và PN-Counter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Last-write-wins không phải CRDT thần kỳ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sets và remove ngữ nghĩa (semantics / 의미론)

Set khó hơn counter vì add/remove concurrent cần ngữ nghĩa (semantics / 의미론) rõ. Add-wins set và remove-wins set đều hợp lệ nhưng trả lời nghiệp vụ (business / 비즈니스) question khác nhau.

CRDT không tự quyết định ngữ nghĩa (semantics / 의미론) đúng; designer phải chọn xung đột (conflict / 충돌) chính sách (policy / 정책) phù hợp lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Ở chặng này của **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **Last-write-wins không phải CRDT thần kỳ** tiếp nhận điểm tựa từ **Sets và remove ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tombstone và garbage collection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Last-write-wins không phải CRDT thần kỳ

LWW dùng timestamp chọn winner đơn giản nhưng có thể mất concurrent cập nhật (update / 업데이트) và phụ thuộc clock các giả định (assumptions / 가정들). Nó convergence được nhưng không bảo toàn intent như richer CRDT.

“Không xung đột (conflict / 충돌) lỗi (error / 오류)” không nghĩa “không mất thông tin”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **Tombstone và garbage collection** tiếp nhận điểm tựa từ **Last-write-wins không phải CRDT thần kỳ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi nào dùng consensus, khi nào dùng CRDT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tombstone và garbage collection

Để nhớ remove đã xảy ra và ngăn item cũ sống lại, replicated structures có thể cần tombstones/phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터). Garbage collect siêu dữ liệu (metadata / 메타데이터) đòi hỏi biết mọi replicas đã vượt nhân quả (causal / 인과적) frontier nào đó, điều khó khi nodes offline lâu.

> **Chuyển mạch:** Trong **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **Khi nào dùng consensus, khi nào dùng CRDT** tiếp nhận điểm tựa từ **Tombstone và garbage collection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi nào dùng consensus, khi nào dùng CRDT

Bank transfer với bất biến (invariant / 불변식) số dư không âm thường cần coordination mạnh hơn. Like counter hoặc presence trạng thái (state / 상태) có thể chấp nhận eventual convergence.

CAP không nói “chọn CP hoặc AP cho toàn cơ sở dữ liệu (database / 데이터베이스)”; nhiều các hệ thống (systems / 시스템들) chọn consistency mô hình (model / 모델) theo thao tác (operation / 연산)/dữ liệu (data / 데이터) kiểu (type / 타입).

> **Chuyển mạch:** Ở chặng này của **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Khi nào dùng consensus, khi nào dùng CRDT** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> CRDT chuyển giải quyết xung đột (conflict resolution / 충돌 해결) từ thời gian chạy (runtime / 런타임) coordination sang data-type thiết kế (design / 설계). Muốn bỏ coordination, ta phải mã hóa merge ngữ nghĩa (semantics / 의미론) sao cho concurrent histories hội tụ mà vẫn phù hợp nghiệp vụ (business / 비즈니스) meaning.

> **Bàn giao:** Giữ lại happens-before, merge semantics, tombstone/GC và business invariant trước khi gọi một CRDT là “eventual consistency an toàn”. Sang [Consensus internals](./03_consensus_log_replication_reconfiguration_and_snapshots.md) khi invariant cần authority mạnh; sang [Multi-region replication](./05_multi_region_replication_and_geo_distributed_tradeoffs.md) khi freshness, locality và conflict policy phải đi cùng topology; quay về [README](./README.md) để xác nhận owner.
