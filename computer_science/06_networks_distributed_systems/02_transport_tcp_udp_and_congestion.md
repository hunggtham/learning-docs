# TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **UDP** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **TCP lớp trừu tượng (abstraction / 추상화)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

IP best-effort chuyển datagrams nhưng không guarantee delivery, thứ tự (order / 순서) hay duplicate-free. tầng vận chuyển (transport layer / 전송 계층) thêm communication lớp trừu tượng (abstraction / 추상화) giữa ứng dụng (application / 애플리케이션) endpoints qua ports.

## UDP

UDP (user Datagram protocol) giữ message boundaries và thêm ports + checksum, nhưng không liên kết (connection / 연결) handshake, retransmission, thứ tự (ordering / 순서) hay congestion điều khiển (control / 제어) ở giao thức (protocol / 프로토콜) itself. ứng dụng (application / 애플리케이션) có thể bản dựng (build / 빌드) những properties riêng.

DNS historically often UDP for small queries; real-time media/games có thể prefer timeliness hơn retransmitting stale packet. QUIC chạy độ tin cậy (reliability / 신뢰성)/congestion/encryption ở userspace trên UDP, cho thấy UDP có thể là substrate cho richer vận chuyển (transport / 전송).

“UDP nhanh hơn TCP” quá đơn giản; UDP có less built-in machinery, nhưng ứng dụng (application / 애플리케이션) yêu cầu (requirement / 요구사항) có thể phải reimplement độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** UDP exposes datagrams without delivery contract; TCP adds ordered reliable byte-stream semantics, implemented through sequence numbers and acknowledgements.

## TCP lớp trừu tượng (abstraction / 추상화)

TCP (Transmission control protocol) cung cấp reliable ordered **byte stream**, không message stream. Nếu sender writes 100 bytes rồi 200 bytes, receiver có thể read 50/250 hoặc 300 tùy buffering; ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜) cần framing.

Liên kết (connection / 연결) identified conceptually bởi endpoint tuple (source/destination IP/port plus protocol context). Handshake establishes initial chuỗi (sequence / 시퀀스) trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **TCP lớp trừu tượng (abstraction / 추상화)** xác định đầu vào; **Chuỗi (sequence / 시퀀스) numbers và acknowledgements** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Luồng (flow / 흐름) điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) numbers và acknowledgements

TCP labels bytes with chuỗi (sequence / 시퀀스) numbers. Receiver ACKs progress; sender retransmits dữ liệu (data / 데이터) inferred lost by hết thời gian chờ (timeout / 타임아웃)/duplicate ACK/SACK-related mechanisms depending hiện thực (implementation / 구현).

Retransmission không nghĩa mạng (network / 네트워크) “sửa packet”; sender sends another bản sao (copy / 복사). Receiver reorders/duplicates handling to present ordered stream.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Chuỗi (sequence / 시퀀스) numbers và acknowledgements** xác định đầu vào; **Luồng (flow / 흐름) điều khiển (control / 제어)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Congestion điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng (flow / 흐름) điều khiển (control / 제어)

Receiver has finite buffer. Advertised receive cửa sổ (window / 윈도우) tells sender how much dữ liệu (data / 데이터) can be in flight without overwhelming receiver. Đây là end-to-end **receiver sức chứa (capacity / 용량)** điều khiển (control / 제어).

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Luồng (flow / 흐름) điều khiển (control / 제어)** xác định đầu vào; **Congestion điều khiển (control / 제어)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bandwidth-delay sản phẩm (product / 제품)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Congestion điều khiển (control / 제어)

Congestion điều khiển (control / 제어) protects mạng (network / 네트워크) đường dẫn (path / 경로). Sender estimates safe congestion cửa sổ (window / 윈도우) based on ACK/mất mát (loss / 손실)/ECN and thuật toán (algorithm / 알고리즘). Goal avoid collapse while utilize sức chứa (capacity / 용량) fairly/efficiently.

Luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어) khác: một bảo vệ receiver, một phản ứng mạng (network / 네트워크) sức chứa (capacity / 용량)/queues.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Bandwidth-delay sản phẩm (product / 제품)** tiếp nhận điểm tựa từ **Congestion điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RTT và retransmission hết thời gian chờ (timeout / 타임아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bandwidth-delay sản phẩm (product / 제품)

Để fully utilize high-bandwidth high-RTT đường dẫn (path / 경로), amount in flight cần khoảng:

\[
BDP = bandwidth \times RTT
\]

Ví dụ 1 Gbit/s × 0.1 s = 100 Mbit ≈12.5 MB in flight. cửa sổ (window / 윈도우) quá nhỏ không fill pipe dù link bandwidth cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **RTT và retransmission hết thời gian chờ (timeout / 타임아웃)** tiếp nhận điểm tựa từ **Bandwidth-delay sản phẩm (product / 제품)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Head-of-line blocking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RTT và retransmission hết thời gian chờ (timeout / 타임아웃)

TCP measures RTT và variance để set hết thời gian chờ (timeout / 타임아웃) adaptively. hết thời gian chờ (timeout / 타임아웃) quá ngắn gây spurious retransmits; quá dài chậm khôi phục (recovery / 복구). hiện đại (modern / 현대적) mất mát (loss / 손실) detection uses more signals than one fixed timer.

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Head-of-line blocking** tiếp nhận điểm tựa từ **RTT và retransmission hết thời gian chờ (timeout / 타임아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) setup và TLS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Head-of-line blocking

TCP ordered stream giữ later bytes tới khi missing earlier bytes recovered. Với multiplexed ứng dụng (application / 애플리케이션) streams trên one TCP liên kết (connection / 연결), mất mát (loss / 손실) in one segment can stall all dữ liệu (data / 데이터) at vận chuyển (transport / 전송) stream mức (level / 수준). HTTP/2 solves ứng dụng (application / 애플리케이션) yêu cầu (request / 요청) multiplexing but not TCP-level HOL. HTTP/3 over QUIC uses independent streams so mất mát (loss / 손실) can khối (block / 블록) affected stream rather than all streams in same way.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, sau nội dung của **Head-of-line blocking**, **Liên kết (connection / 연결) setup và TLS** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) setup và TLS

TCP handshake adds RTT before dữ liệu (data / 데이터) unless liên kết (connection / 연결) reused; TLS adds cryptographic handshake, though hiện đại (modern / 현대적) TLS/QUIC optimize round trips/resumption. High độ trễ (latency / 지연 시간) amplifies handshake costs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Backpressure** tiếp nhận điểm tựa từ **Liên kết (connection / 연결) setup và TLS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backpressure

Socket send buffer full eventually blocks/returns unavailable; receiver/cửa sổ (window / 윈도우)/congestion propagate pressure. ứng dụng (application / 애플리케이션) that ignores backpressure by buffering unbounded dữ liệu (data / 데이터) simply moves overload into bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Backpressure** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> TCP is a **máy trạng thái (state machine / 상태 머신) that turns unreliable packets into an ordered byte stream** while controlling receiver and mạng (network / 네트워크) pressure. độ tin cậy (reliability / 신뢰성) has độ trễ (latency / 지연 시간) chi phí (cost / 비용) because missing earlier dữ liệu (data / 데이터) must be recovered.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“TCP preserves ghi (write / 쓰기) message boundaries.”** Không; it is byte-stream ngữ nghĩa (semantics / 의미론).

**“UDP has no checksum/độ tin cậy (reliability / 신뢰성) at all.”** UDP includes checksum ngữ nghĩa (semantics / 의미론), but no retransmission/thứ tự (order / 순서)/liên kết (connection / 연결) độ tin cậy (reliability / 신뢰성).

**“Packet mất mát (loss / 손실) always means vật lý (physical / 물리적) corruption.”** Congested queues deliberately drop packets; wireless/link issues are only one cause.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Queues](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) explain buffering. [Web request](./03_dns_http_tls_and_web_request.md) builds ứng dụng (application / 애플리케이션)/bảo mật (security / 보안) protocols on vận chuyển (transport / 전송). [Distributed systems](./04_distributed_systems_time_failure_and_consistency.md) must handle hết thời gian chờ (timeout / 타임아웃) even when TCP itself is reliable, because endpoint/tiến trình (process / 프로세스) can thất bại (fail / 실패).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
