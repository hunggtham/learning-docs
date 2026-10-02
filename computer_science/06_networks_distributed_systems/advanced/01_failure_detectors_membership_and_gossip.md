# Thất bại (failure / 실패) detectors, membership và gossip protocols

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thất bại (failure / 실패) detectors, membership và gossip protocols**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hết thời gian chờ (timeout / 타임아웃) chỉ tạo suspicion** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Perfect thất bại (failure / 실패) detector là lớp trừu tượng (abstraction / 추상화) mạnh** để kiểm tra nhận định bằng tiêu chí hoặc phép thử. Mạch này nối failure detectors với membership và gossip, để suspicion, state dissemination và false positive được phân biệt.

Trong hệ thống phân tán (distributed system / 분산 시스템), nút (node / 노드) không thể trực tiếp biết “nút (node / 노드) kia đã chết”. Nó chỉ biết **message/reply chưa đến trong một khoảng thời gian**. mạng (network / 네트워크) delay, GC pause, CPU saturation, packet mất mát (loss / 손실) và tiến trình (process / 프로세스) crash đều có thể tạo cùng observation. Vì vậy thất bại (failure / 실패) detection là bài toán suy luận dưới bất định (uncertainty / 불확실성).

## Hết thời gian chờ (timeout / 타임아웃) chỉ tạo suspicion

Nếu A ping B và sau 1 giây không có reply, A có thể suspect B. Nhưng B có thể vẫn sống, chỉ chậm hoặc mạng (network / 네트워크) partition.

Hết thời gian chờ (timeout / 타임아웃) ngắn phát hiện nhanh nhưng false positive nhiều. hết thời gian chờ (timeout / 타임아웃) dài giảm false positive nhưng failover chậm.

Không có threshold hoàn hảo nếu mạng (network / 네트워크) delay không có upper bound chắc chắn.

> **Chuyển mạch:** Trong **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Perfect thất bại (failure / 실패) detector là lớp trừu tượng (abstraction / 추상화) mạnh** tiếp nhận điểm tựa từ **Hết thời gian chờ (timeout / 타임아웃) chỉ tạo suspicion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Membership là máy trạng thái (state machine / 상태 머신) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Perfect thất bại (failure / 실패) detector là lớp trừu tượng (abstraction / 추상화) mạnh

Lý thuyết (theory / 이론) phân tán (distributed / 분산) các hệ thống (systems / 시스템들) mô tả thất bại (failure / 실패) detectors theo properties như completeness và accuracy.

Perfect detector lý tưởng cuối cùng phát hiện mọi tiến trình (process / 프로세스) crash và không nghi nhầm tiến trình (process / 프로세스) đúng. Trong asynchronous mạng (network / 네트워크) thuần, guarantee này không thực tế vì “rất chậm” không phân biệt được với “đã chết”.

Môi trường vận hành (production / 운영 환경) các hệ thống (systems / 시스템들) vì vậy dùng eventually-accurate các giả định (assumptions / 가정들), heartbeats và adaptive hết thời gian chờ (timeout / 타임아웃).

> **Chuyển mạch:** Ở chặng này của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Membership là máy trạng thái (state machine / 상태 머신) riêng** tiếp nhận điểm tựa từ **Perfect thất bại (failure / 실패) detector là lớp trừu tượng (abstraction / 추상화) mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Heartbeat** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Membership là máy trạng thái (state machine / 상태 머신) riêng

Cluster cần biết tập members: joining, alive, suspect, leaving, dead.

Membership không chỉ là một danh sách (list / 목록) IP. Nó cần phiên bản (version / 버전)/epoch/incarnation để phân biệt old thông tin (information / 정보) với nút (node / 노드) restart.

Nếu nút (node / 노드) B restart với cùng address nhưng incarnation mới, gossip cũ nói “B dead” không được phép giết membership mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Heartbeat** tiếp nhận điểm tựa từ **Membership là máy trạng thái (state machine / 상태 머신) riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gossip** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heartbeat

Nút (node / 노드) gửi heartbeat định kỳ hoặc peers chủ động probe nhau. Missing heartbeats tạo suspicion.

Central coordinator đơn giản nhưng thành bottleneck/single phụ thuộc (dependency / 의존성). All-to-all heartbeat quy mô (scale / 규모) `O(n^2)` messages. Large clusters thường dùng subset probing + gossip.

> **Chuyển mạch:** Trong **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Gossip** tiếp nhận điểm tựa từ **Heartbeat** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SWIM intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gossip

Mỗi round, nút (node / 노드) trao đổi membership/trạng thái (state / 상태) với một số peers ngẫu nhiên. thông tin (information / 정보) lan truyền epidemic-style.

Gossip có ưu điểm decentralized, robust và message chi phí (cost / 비용) per nút (node / 노드) thấp hơn broadcast toàn cluster. Đổi lại, convergence không instant và trạng thái (state / 상태) tạm thời không đồng nhất.

Một nút (node / 노드) có thể biết thất bại (failure / 실패) trước nút (node / 노드) khác; giao thức (protocol / 프로토콜) sử dụng membership phải chịu được điều đó.

> **Chuyển mạch:** Ở chặng này của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **SWIM intuition** tiếp nhận điểm tựa từ **Gossip** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **False positive nguy hiểm hơn tưởng tượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SWIM intuition

Family giao thức (protocol / 프로토콜) như SWIM tách thất bại (failure / 실패) detection và thông tin (information / 정보) dissemination. nút (node / 노드) probe mục tiêu (target / 대상); nếu direct ping thất bại (fail / 실패), có thể nhờ một số peers indirect ping để phân biệt cục bộ (local / 로컬) đường dẫn (path / 경로) issue.

Sau suspicion, status được piggyback qua gossip.

Chi tiết hiện thực (implementation / 구현) khác nhau, nhưng mô hình tư duy (mental model / 사고 모델) quan trọng là **randomized probing + suspicion + epidemic dissemination**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **False positive nguy hiểm hơn tưởng tượng** tiếp nhận điểm tựa từ **SWIM intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## False positive nguy hiểm hơn tưởng tượng

Nếu suspect lập tức trigger leader election, shard reassignment và dữ liệu (data / 데이터) replication, một mạng (network / 네트워크) hiccup nhỏ có thể tạo “khôi phục (recovery / 복구) storm”.

Membership tầng (layer / 계층) cần hysteresis/suspicion period và downstream điều khiển (control / 제어) plane cần tỷ lệ (rate / 비율) limit remediation.

Thất bại (failure / 실패) detector không nên tự động biến bất định (uncertainty / 불확실성) thành destructive hành động (action / 동작) quá sớm.

> **Chuyển mạch:** Trong **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Partition** tiếp nhận điểm tựa từ **False positive nguy hiểm hơn tưởng tượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phi accrual detector** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partition

Hai halves của cluster có thể cùng nghĩ phía kia dead. Nếu cả hai tiếp tục nhận writes như primary, split-brain xảy ra.

Membership/thất bại (failure / 실패) detector không tự giải split-brain. Cần quorum, consensus, lease/fencing hoặc bên ngoài (external / 외부) authority để quyết định ai có quyền mutate trạng thái dùng chung (shared state / 공유 상태).

Đây là lý do “health check thất bại (fail / 실패)” không tương đương “safe to promote standby”.

> **Chuyển mạch:** Ở chặng này của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Phi accrual detector** tiếp nhận điểm tựa từ **Partition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Clock và timer các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phi accrual detector

Thay vì nhị phân (binary / 이진) hết thời gian chờ (timeout / 타임아웃) cố định, detector có thể tính suspicion mức (level / 수준) dựa phân phối (distribution / 분포) heartbeat intervals. Phi accrual trả continuous score biểu diễn observation hiện tại bất thường mức nào so lịch sử (history / 이력).

Điều này thích ứng độ trễ (latency / 지연 시간) variation tốt hơn fixed hết thời gian chờ (timeout / 타임아웃) trong một số các hệ thống (systems / 시스템들), nhưng vẫn không biến bất định (uncertainty / 불확실성) thành certainty.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Clock và timer các giả định (assumptions / 가정들)** tiếp nhận điểm tựa từ **Phi accrual detector** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Membership thay đổi (change / 변경) và quyền sở hữu trạng thái (state ownership / 상태 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Clock và timer các giả định (assumptions / 가정들)

Thất bại (failure / 실패) detection dùng cục bộ (local / 로컬) timeouts nên phụ thuộc timer scheduling và tiến trình (process / 프로세스) pauses. Long GC stop-the-world có thể làm nút (node / 노드) khỏe bị peers suspect.

Môi trường vận hành (production / 운영 환경) tuning phải xem GC, CPU starvation, event-loop stalls và mạng (network / 네트워크) tail độ trễ (latency / 지연 시간) cùng nhau.

> **Chuyển mạch:** Trong **Thất bại (failure / 실패) detectors, membership và gossip protocols**, sau nội dung của **Clock và timer các giả định (assumptions / 가정들)**, **Membership thay đổi (change / 변경) và quyền sở hữu trạng thái (state ownership / 상태 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Membership thay đổi (change / 변경) và quyền sở hữu trạng thái (state ownership / 상태 소유권)

Khi member set đổi, shard quyền sở hữu (ownership / 소유권) hoặc replica placement có thể phải rebalance. Nếu membership flaps, dữ liệu (data / 데이터) movement liên tục tạo tải (load / 로드) lớn.

Do đó stable membership và controlled reconfiguration là prerequisite cho lưu trữ (storage / 저장소) cluster khỏe.

> **Chuyển mạch:** Ở chặng này của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Membership thay đổi (change / 변경) và quyền sở hữu trạng thái (state ownership / 상태 소유권)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> thất bại (failure / 실패) detector không nói “ai chết”; nó cung cấp **suspicion tín hiệu (signal / 신호) dưới timing các giả định (assumptions / 가정들)**. Membership biến signals đó thành versioned cluster view; safety-critical quyền sở hữu (ownership / 소유권) phải dựa thêm quorum/consensus/fencing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Ping hết thời gian chờ (timeout / 타임아웃) = nút (node / 노드) chết.”** Chỉ là một observation không có reply đúng hạn.

**“Gossip cho mọi nút (node / 노드) trạng thái (state / 상태) giống nhau ngay.”** Gossip converges dần và chấp nhận temporary inconsistency.

**“Detect thất bại (failure / 실패) là đủ để failover an toàn.”** Failover mutation authority cần fencing/quorum để tránh split-brain.

> **Chuyển mạch:** Trong **Thất bại (failure / 실패) detectors, membership và gossip protocols**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Tiếp theo đọc [Leases, fencing tokens và split-brain prevention](./02_leases_fencing_tokens_and_split_brain_prevention.md). Sau đó consensus internals giải thích cách cluster đồng ý durable log/trạng thái (state / 상태) transitions.

> **Bàn giao:** Giữ lại suspicion ≠ proof, membership là state machine, gossip có convergence delay và failover cần fencing/quorum. Sang [Leases và fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md) để biến suspicion thành quyền ghi an toàn; sau đó đọc consensus để theo dõi durable authority; quay về [README](./README.md) để xác nhận owner.
