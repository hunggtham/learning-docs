# CRDTs, causal consistency và conflict resolution

Strong consensus không phải lựa chọn duy nhất. Với collaborative editing, counters, sets hoặc geo-distributed applications, hệ thống đôi khi ưu tiên local availability và chấp nhận replicas tạm thời khác nhau. Khi đó câu hỏi là làm sao merge concurrent updates mà không phụ thuộc một coordinator toàn cục.

## Concurrency không chỉ là “cùng timestamp”

Hai events concurrent khi không có causal order biết được giữa chúng. Nếu A tạo event rồi B quan sát A trước khi tạo B, A → B. Nếu hai clients offline update độc lập, hai events có thể incomparable.

Wall-clock timestamps không đủ đáng tin để suy ra causality vì clock skew và network delay.

## Happens-before và logical clocks

Lamport clock tạo ordering nhất quán với causality nhưng không phân biệt đầy đủ concurrency. Vector clocks/version vectors có thể biểu diễn causal histories chi tiết hơn với metadata lớn hơn.

Causal consistency đảm bảo effect không xuất hiện trước cause: nếu comment trả lời một post, replica không nên hiển thị reply trước post mà user đã dựa vào.

## CRDT

**Conflict-Free Replicated Data Type** thiết kế state/operations sao cho replicas có thể merge concurrent updates theo algebraic properties đảm bảo convergence.

State-based CRDT thường cần merge operation có tính commutative, associative và idempotent; join-semilattice cung cấp formal structure cho monotonic merge.

## G-Counter và PN-Counter

Grow-only counter giữ component per replica và merge bằng element-wise max. Tổng các components cho value. Vì merge max idempotent, duplicate state exchange không làm double count.

PN-Counter kết hợp hai grow-only counters cho increments và decrements. Metadata tăng theo replica identity, minh họa trade-off giữa coordination-free merge và state overhead.

## Sets và remove semantics

Set khó hơn counter vì add/remove concurrent cần semantics rõ. Add-wins set và remove-wins set đều hợp lệ nhưng trả lời business question khác nhau.

CRDT không tự quyết định semantics đúng; designer phải chọn conflict policy phù hợp domain.

## Last-write-wins không phải CRDT thần kỳ

LWW dùng timestamp chọn winner đơn giản nhưng có thể mất concurrent update và phụ thuộc clock assumptions. Nó convergence được nhưng không bảo toàn intent như richer CRDT.

“Không conflict error” không nghĩa “không mất thông tin”.

## Tombstone và garbage collection

Để nhớ remove đã xảy ra và ngăn item cũ sống lại, replicated structures có thể cần tombstones/version metadata. Garbage collect metadata đòi hỏi biết mọi replicas đã vượt causal frontier nào đó, điều khó khi nodes offline lâu.

## Khi nào dùng consensus, khi nào dùng CRDT

Bank transfer với invariant số dư không âm thường cần coordination mạnh hơn. Like counter hoặc presence state có thể chấp nhận eventual convergence.

CAP không nói “chọn CP hoặc AP cho toàn database”; nhiều systems chọn consistency model theo operation/data type.

## Mental Model

> CRDT chuyển conflict resolution từ runtime coordination sang data-type design. Muốn bỏ coordination, ta phải mã hóa merge semantics sao cho concurrent histories hội tụ mà vẫn phù hợp business meaning.