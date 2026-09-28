# CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)

> **Mạch đọc:** Đặt **CRDTs, nhân quả (causal / 인과적) consistency và giải quyết xung đột (conflict resolution / 충돌 해결)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **tính đồng thời (concurrency / 동시성) không chỉ là “cùng timestamp”** sang **Happens-before và logical clocks**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Strong consensus không phải lựa chọn duy nhất. Với collaborative editing, counters, sets hoặc geo-distributed applications, hệ thống đôi khi ưu tiên cục bộ (local / 로컬) availability và chấp nhận replicas tạm thời khác nhau. Khi đó câu hỏi là làm sao merge concurrent updates mà không phụ thuộc một coordinator toàn cục.

## Tính đồng thời (concurrency / 동시성) không chỉ là “cùng timestamp”

Hai events concurrent khi không có nhân quả (causal / 인과적) thứ tự (order / 순서) biết được giữa chúng. Nếu A tạo sự kiện (event / 이벤트) rồi B quan sát A trước khi tạo B, A → B. Nếu hai clients offline cập nhật (update / 업데이트) độc lập, hai events có thể incomparable.

Wall-clock timestamps không đủ đáng tin để suy ra causality vì clock skew và mạng (network / 네트워크) delay.


> **Chuyển mạch:** Từ **tính đồng thời (concurrency / 동시성) không chỉ là “cùng timestamp”**, ta sang **Happens-before và logical clocks** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Happens-before và logical clocks

Lamport clock tạo thứ tự (ordering / 순서) nhất quán với causality nhưng không phân biệt đầy đủ tính đồng thời (concurrency / 동시성). véc-tơ (vector / 벡터) clocks/phiên bản (version / 버전) vectors có thể biểu diễn nhân quả (causal / 인과적) histories chi tiết hơn với siêu dữ liệu (metadata / 메타데이터) lớn hơn.

Nhân quả (causal / 인과적) consistency đảm bảo tác động (effect / 효과) không xuất hiện trước cause: nếu comment trả lời một post, replica không nên hiển thị reply trước post mà người dùng (user / 사용자) đã dựa vào.


> **Chuyển mạch:** Từ **Happens-before và logical clocks**, ta sang **CRDT** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## CRDT

**Conflict-Free Replicated dữ liệu (data / 데이터) kiểu (type / 타입)** thiết kế trạng thái (state / 상태)/operations sao cho replicas có thể merge concurrent updates theo algebraic properties đảm bảo convergence.

State-based CRDT thường cần merge thao tác (operation / 연산) có tính commutative, associative và idempotent; join-semilattice cung cấp formal cấu trúc (structure / 구조) cho monotonic merge.


> **Chuyển mạch:** Từ **CRDT**, ta sang **G-Counter và PN-Counter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## G-Counter và PN-Counter

Grow-only counter giữ thành phần (component / 컴포넌트) per replica và merge bằng element-wise max. Tổng các components cho giá trị (value / 값). Vì merge max idempotent, duplicate trạng thái (state / 상태) exchange không làm double count.

PN-Counter kết hợp hai grow-only counters cho increments và decrements. siêu dữ liệu (metadata / 메타데이터) tăng theo replica định danh (identity / 식별자), minh họa sự đánh đổi (trade-off / 트레이드오프) giữa coordination-free merge và trạng thái (state / 상태) overhead.


> **Chuyển mạch:** Từ **G-Counter và PN-Counter**, ta sang **Sets và remove ngữ nghĩa (semantics / 의미론)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sets và remove ngữ nghĩa (semantics / 의미론)

Set khó hơn counter vì add/remove concurrent cần ngữ nghĩa (semantics / 의미론) rõ. Add-wins set và remove-wins set đều hợp lệ nhưng trả lời nghiệp vụ (business / 비즈니스) question khác nhau.

CRDT không tự quyết định ngữ nghĩa (semantics / 의미론) đúng; designer phải chọn xung đột (conflict / 충돌) chính sách (policy / 정책) phù hợp lĩnh vực (domain / 도메인).


> **Chuyển mạch:** Từ **Sets và remove ngữ nghĩa (semantics / 의미론)**, ta sang **Last-write-wins không phải CRDT thần kỳ** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Last-write-wins không phải CRDT thần kỳ

LWW dùng timestamp chọn winner đơn giản nhưng có thể mất concurrent cập nhật (update / 업데이트) và phụ thuộc clock các giả định (assumptions / 가정들). Nó convergence được nhưng không bảo toàn intent như richer CRDT.

“Không xung đột (conflict / 충돌) lỗi (error / 오류)” không nghĩa “không mất thông tin”.


> **Chuyển mạch:** Từ **Last-write-wins không phải CRDT thần kỳ**, ta sang **Tombstone và garbage collection** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tombstone và garbage collection

Để nhớ remove đã xảy ra và ngăn item cũ sống lại, replicated structures có thể cần tombstones/phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터). Garbage collect siêu dữ liệu (metadata / 메타데이터) đòi hỏi biết mọi replicas đã vượt nhân quả (causal / 인과적) frontier nào đó, điều khó khi nodes offline lâu.


> **Chuyển mạch:** Từ **Tombstone và garbage collection**, ta sang **Khi nào dùng consensus, khi nào dùng CRDT** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Khi nào dùng consensus, khi nào dùng CRDT

Bank transfer với bất biến (invariant / 불변식) số dư không âm thường cần coordination mạnh hơn. Like counter hoặc presence trạng thái (state / 상태) có thể chấp nhận eventual convergence.

CAP không nói “chọn CP hoặc AP cho toàn cơ sở dữ liệu (database / 데이터베이스)”; nhiều các hệ thống (systems / 시스템들) chọn consistency mô hình (model / 모델) theo thao tác (operation / 연산)/dữ liệu (data / 데이터) kiểu (type / 타입).


> **Chuyển mạch:** Từ **Khi nào dùng consensus, khi nào dùng CRDT**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> CRDT chuyển giải quyết xung đột (conflict resolution / 충돌 해결) từ thời gian chạy (runtime / 런타임) coordination sang data-type thiết kế (design / 설계). Muốn bỏ coordination, ta phải mã hóa merge ngữ nghĩa (semantics / 의미론) sao cho concurrent histories hội tụ mà vẫn phù hợp nghiệp vụ (business / 비즈니스) meaning.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 distributed transactions exactly once and failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
