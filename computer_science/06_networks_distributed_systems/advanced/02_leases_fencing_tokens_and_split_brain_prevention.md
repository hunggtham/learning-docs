# Leases, fencing tokens và split-brain prevention

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Leases, fencing tokens và split-brain prevention**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Khóa (lock / 잠금) quyền sở hữu (ownership / 소유권) không nên dựa vào niềm tin cục bộ (local / 로컬)** chỉ đường quay lại owner và tài liệu chuẩn khi cần đào sâu; sau đó sang **Lease** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Phân tán (distributed / 분산) khóa (lock / 잠금) hoặc “primary quyền sở hữu (ownership / 소유권)” khó hơn cục bộ (local / 로컬) mutex vì máy khách (client / 클라이언트) có thể pause, mất mạng (network / 네트워크) rồi quay lại sau khi hệ thống đã trao quyền cho máy khách (client / 클라이언트) khác. Nếu old đơn vị sở hữu (owner / 오너) vẫn ghi được, ta có **stale đơn vị sở hữu (owner / 오너)** và có thể corrupt trạng thái (state / 상태). Leases và fencing giải quyết hai phần khác nhau của vấn đề.

## Khóa (lock / 잠금) quyền sở hữu (ownership / 소유권) không nên dựa vào niềm tin cục bộ (local / 로컬)

Giả sử worker A lấy khóa (lock / 잠금) xử lý tệp (file / 파일). Sau đó A pause 60 giây vì GC. khóa (lock / 잠금) dịch vụ (service / 서비스) cho rằng A hết thời gian chờ (timeout / 타임아웃) và cấp khóa (lock / 잠금) cho B. B xử lý xong. A tỉnh lại và tiếp tục ghi (write / 쓰기) vì trong bộ nhớ (memory / 메모리) nó vẫn “tin” mình giữ khóa (lock / 잠금).

Nếu lưu trữ (storage / 저장소) chấp nhận ghi (write / 쓰기) của A, khóa (lock / 잠금) hết thời gian chờ (timeout / 타임아웃) đã không bảo vệ tính đúng đắn (correctness / 정확성).

Đây là dạng thất bại (failure mode / 실패 모드) kinh điển của phân tán (distributed / 분산) khóa (lock / 잠금) không có fencing.

> **Chuyển mạch:** Trong **Leases, fencing tokens và split-brain prevention**, **Lease** tiếp nhận điểm tựa từ **Khóa (lock / 잠금) quyền sở hữu (ownership / 소유권) không nên dựa vào niềm tin cục bộ (local / 로컬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fencing đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lease

Lease là quyền có thời hạn. Holder chỉ được coi có authority trước expiry theo giao thức (protocol / 프로토콜).

Lease giúp hệ thống (system / 시스템) tự thu hồi quyền sở hữu (ownership / 소유권) khi holder mất liên lạc. Nhưng clock bất định (uncertainty / 불확실성), pause và delayed messages khiến holder không thể chỉ nhìn cục bộ (local / 로컬) clock rồi tuyệt đối tin quyền còn hiệu lực.

Lease giao thức (protocol / 프로토콜) cần các giả định (assumptions / 가정들) về clock drift/mạng (network / 네트워크) delay hoặc authority central kiểm tra validity.

> **Chuyển mạch:** Ở chặng này của **Leases, fencing tokens và split-brain prevention**, **Fencing đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **Lease** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao fencing mạnh hơn “check khóa (lock / 잠금) trước ghi (write / 쓰기)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fencing đơn vị từ (token / 토큰)

Mỗi lần quyền được cấp, coordinator phát đơn vị từ (token / 토큰) đơn điệu tăng:

```text
A gets token 41
lease expires
B gets token 42
```

Lưu trữ (storage / 저장소)/tài nguyên (resource / 자원) máy chủ (server / 서버) nhớ đơn vị từ (token / 토큰) lớn nhất đã chấp nhận. Nếu A quay lại gửi ghi (write / 쓰기) với 41 sau khi B đã dùng 42, lưu trữ (storage / 저장소) reject 41.

Fencing biến stale-owner bài toán (problem / 문제) thành monotonic thứ tự (ordering / 순서) check ở nơi side tác động (effect / 효과) xảy ra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Leases, fencing tokens và split-brain prevention**, **Vì sao fencing mạnh hơn “check khóa (lock / 잠금) trước ghi (write / 쓰기)”** tiếp nhận điểm tựa từ **Fencing đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đơn vị từ (token / 토큰) cần được enforce ở tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao fencing mạnh hơn “check khóa (lock / 잠금) trước ghi (write / 쓰기)”

A có thể check khóa (lock / 잠금) và thấy valid, rồi pause trước ghi (write / 쓰기). Trong pause, lease hết và B nhận quyền mới. Khi A tiếp tục, check cũ đã stale.

Đây là TOCTOU — time-of-check to time-of-use.

Nếu ghi (write / 쓰기) mang fencing đơn vị từ (token / 토큰) và tài nguyên (resource / 자원) máy chủ (server / 서버) validate atomically, stale máy khách (client / 클라이언트) không thể bypass chỉ vì check xảy ra trước pause.

> **Chuyển mạch:** Trong **Leases, fencing tokens và split-brain prevention**, **Vì sao fencing mạnh hơn “check khóa (lock / 잠금) trước ghi (write / 쓰기)”** nêu điều cần giải thích; **Đơn vị từ (token / 토큰) cần được enforce ở tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Leader lease** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị từ (token / 토큰) cần được enforce ở tài nguyên (resource / 자원)

Nếu khóa (lock / 잠금) dịch vụ (service / 서비스) phát đơn vị từ (token / 토큰) nhưng cơ sở dữ liệu (database / 데이터베이스)/tệp (file / 파일) dịch vụ (service / 서비스) không kiểm tra đơn vị từ (token / 토큰), fencing chỉ là siêu dữ liệu (metadata / 메타데이터) trang trí.

An toàn (safety / 안전) ranh giới (boundary / 경계) phải đặt ở hệ thống (system / 시스템) thực hiện side tác động (effect / 효과): lưu trữ (storage / 저장소), máy trạng thái (state machine / 상태 머신) hoặc API đơn vị sở hữu (owner / 오너) của dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Leases, fencing tokens và split-brain prevention**, **Đơn vị từ (token / 토큰) cần được enforce ở tài nguyên (resource / 자원)** nêu điều cần giải thích; **Leader lease** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Split-brain** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Leader lease

Consensus-based hệ thống (system / 시스템) có thể dùng lease để leader phục vụ read nhanh mà không quorum mỗi read, nếu đảm bảo không leader khác hợp lệ đồng thời trong interval.

Điều này thường cần clock bounds hoặc quorum tương tác (interaction / 상호작용) cẩn thận. Nếu các giả định (assumptions / 가정들) clock sai, stale leader có thể serve stale/unsafe kết quả (result / 결과).

Lease tối ưu hóa (optimization / 최적화) luôn phải nêu rõ timing giả định (assumption / 가정).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Leases, fencing tokens và split-brain prevention**, **Split-brain** tiếp nhận điểm tựa từ **Leader lease** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Epoch/term như fencing concept** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Split-brain

Split-brain xảy ra khi nhiều actors cùng tin mình có quyền primary/ghi (write / 쓰기).

Thất bại (failure / 실패) detector có thể gây split-brain nếu mỗi partition tự promote cục bộ (local / 로컬) nút (node / 노드). Prevention cần một authority quy tắc (rule / 규칙) mà hai sides không cùng thỏa, thường quorum majority hoặc bên ngoài (external / 외부) fencing thiết bị (device / 장치)/đơn vị từ (token / 토큰) dịch vụ (service / 서비스).

Trong cluster 3 nodes, partition 2-1 cho phép side 2 giữ majority và side 1 phải ngừng writes. Availability bị hy sinh ở minority để giữ single-writer an toàn (safety / 안전).

> **Chuyển mạch:** Trong **Leases, fencing tokens và split-brain prevention**, **Epoch/term như fencing concept** tiếp nhận điểm tựa từ **Split-brain** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cơ sở dữ liệu (database / 데이터베이스) primary failover** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Epoch/term như fencing concept

Consensus protocols dùng term/epoch tăng dần. Message từ old leader term thấp có thể bị reject.

Đây là cùng mô hình tư duy (mental model / 사고 모델) với fencing đơn vị từ (token / 토큰), nhưng integrated vào replicated máy trạng thái (state machine / 상태 머신) giao thức (protocol / 프로토콜).

Epoch giúp phân biệt “message cũ đến muộn” với hiện tại (current / 현재) authority.

> **Chuyển mạch:** Ở chặng này của **Leases, fencing tokens và split-brain prevention**, **Epoch/term như fencing concept** nêu điều cần giải thích; **Cơ sở dữ liệu (database / 데이터베이스) primary failover** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phân tán (distributed / 분산) job quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cơ sở dữ liệu (database / 데이터베이스) primary failover

Một standby được promote nhưng old primary chưa thật sự chết, chỉ mất mạng (network / 네트워크) với điều khiển (control / 제어) plane. Nếu clients hoặc lưu trữ (storage / 저장소) đường dẫn (path / 경로) vẫn gửi ghi (write / 쓰기) tới old primary, divergence xảy ra.

Môi trường vận hành (production / 운영 환경) failover cần đảm bảo old primary bị **fenced**: revoke lưu trữ (storage / 저장소) truy cập (access / 접근), thay đổi (change / 변경) epoch/quorum authority, disable mạng (network / 네트워크) đường dẫn (path / 경로) hoặc cơ chế (mechanism / 메커니즘) tương đương.

“Promote new primary” chỉ là nửa đầu của failover; “old primary cannot ghi (write / 쓰기)” mới hoàn tất an toàn (safety / 안전).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Leases, fencing tokens và split-brain prevention**, **Cơ sở dữ liệu (database / 데이터베이스) primary failover** nêu điều cần giải thích; **Phân tán (distributed / 분산) job quyền sở hữu (ownership / 소유권)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tán (distributed / 분산) job quyền sở hữu (ownership / 소유권)

Scheduler có thể phát fencing đơn vị từ (token / 토큰) per job attempt. đầu ra (output / 출력) sink chỉ accept attempt đơn vị từ (token / 토큰) mới nhất.

Nếu old worker chậm hoàn thành sau thử lại (retry / 재시도) worker mới, sink reject stale kết quả (result / 결과) thay vì overwrite new kết quả (result / 결과).

Mẫu (pattern / 패턴) này hữu ích cho batch, workflow engine và exactly-once-like processing.

> **Chuyển mạch:** Trong **Leases, fencing tokens và split-brain prevention**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Phân tán (distributed / 분산) job quyền sở hữu (ownership / 소유권)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Lease trả lời **quyền có hiệu lực trong khoảng nào**; fencing đơn vị từ (token / 토큰) trả lời **làm sao tài nguyên (resource / 자원) từ chối đơn vị sở hữu (owner / 오너) cũ dù nó quay lại**. Split-brain prevention cần authority được enforce tại side-effect ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **Leases, fencing tokens và split-brain prevention**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“phân tán (distributed / 분산) khóa (lock / 잠금) hết thời gian chờ (timeout / 타임아웃) là đủ.”** Stale holder có thể tiếp tục sau pause nếu downstream không fence.

**“Clock đồng bộ bằng NTP nên lease tuyệt đối an toàn.”** Clock vẫn có drift/step và tiến trình (process / 프로세스) pause; giao thức (protocol / 프로토콜) phải dựa giả định (assumption / 가정) rõ.

**“Failover xong khi standby thành primary.”** Old primary phải mất khả năng mutate trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Leases, fencing tokens và split-brain prevention**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc trước [Failure detectors và membership](./01_failure_detectors_membership_and_gossip.md). Chapter consensus tiếp theo sẽ cho thấy term/epoch, quorum và log authority tạo fencing ngữ nghĩa (semantics / 의미론) ở cấp giao thức (protocol / 프로토콜).

> **Bàn giao:** Giữ lại lease expiry, monotonic fencing token và downstream enforcement trước khi coi failover là hoàn tất. Sang [Failure detectors và membership](./01_failure_detectors_membership_and_gossip.md) để xem suspicion/membership cung cấp input nào, rồi đọc consensus để hiểu term/epoch/quorum tạo authority bền vững; quay về [README](./README.md) để xác nhận owner.
