# TCP, UDP, flow control và congestion control

IP best-effort chuyển datagrams nhưng không guarantee delivery, order hay duplicate-free. Transport layer thêm communication abstraction giữa application endpoints qua ports.

## UDP

UDP (User Datagram Protocol) giữ message boundaries và thêm ports + checksum, nhưng không connection handshake, retransmission, ordering hay congestion control ở protocol itself. Application có thể build những properties riêng.

DNS historically often UDP for small queries; real-time media/games có thể prefer timeliness hơn retransmitting stale packet. QUIC chạy reliability/congestion/encryption ở userspace trên UDP, cho thấy UDP có thể là substrate cho richer transport.

“UDP nhanh hơn TCP” quá đơn giản; UDP có less built-in machinery, nhưng application requirement có thể phải reimplement complexity.

## TCP abstraction

TCP (Transmission Control Protocol) cung cấp reliable ordered **byte stream**, không message stream. Nếu sender writes 100 bytes rồi 200 bytes, receiver có thể read 50/250 hoặc 300 tùy buffering; application protocol cần framing.

Connection identified conceptually bởi endpoint tuple (source/destination IP/port plus protocol context). Handshake establishes initial sequence state.

## Sequence numbers và acknowledgements

TCP labels bytes with sequence numbers. Receiver ACKs progress; sender retransmits data inferred lost by timeout/duplicate ACK/SACK-related mechanisms depending implementation.

Retransmission không nghĩa network “sửa packet”; sender sends another copy. Receiver reorders/duplicates handling to present ordered stream.

## Flow control

Receiver has finite buffer. Advertised receive window tells sender how much data can be in flight without overwhelming receiver. Đây là end-to-end **receiver capacity** control.

## Congestion control

Congestion control protects network path. Sender estimates safe congestion window based on ACK/loss/ECN and algorithm (CUBIC, BBR-family etc depending OS/config). Goal avoid collapse while utilize capacity fairly/efficiently.

Flow control và congestion control khác: một bảo vệ receiver, một phản ứng network capacity/queues.

## Bandwidth-delay product

Để fully utilize high-bandwidth high-RTT path, amount in flight cần khoảng:

\[
BDP = bandwidth \times RTT
\]

Ví dụ 1 Gbit/s × 0.1 s = 100 Mbit ≈12.5 MB in flight. Window quá nhỏ không fill pipe dù link bandwidth cao.

## RTT và retransmission timeout

TCP measures RTT và variance để set timeout adaptively. Timeout quá ngắn gây spurious retransmits; quá dài chậm recovery. Modern loss detection uses more signals than one fixed timer.

## Head-of-line blocking

TCP ordered stream giữ later bytes tới khi missing earlier bytes recovered. Với multiplexed application streams trên one TCP connection, loss in one segment can stall all data at transport stream level. HTTP/2 solves application request multiplexing but not TCP-level HOL. HTTP/3 over QUIC uses independent streams so loss can block affected stream rather than all streams in same way.

## Connection setup và TLS

TCP handshake adds RTT before data unless connection reused; TLS adds cryptographic handshake, though modern TLS/QUIC optimize round trips/resumption. High latency amplifies handshake costs.

## Backpressure

Socket send buffer full eventually blocks/returns unavailable; receiver/window/congestion propagate pressure. Application that ignores backpressure by buffering unbounded data simply moves overload into memory.

## Mental Model

> TCP is a **state machine that turns unreliable packets into an ordered byte stream** while controlling receiver and network pressure. Reliability has latency cost because missing earlier data must be recovered.

## Common Misconceptions

**“TCP preserves write message boundaries.”** Không; it is byte-stream semantics.

**“UDP has no checksum/reliability at all.”** UDP includes checksum semantics, but no retransmission/order/connection reliability.

**“Packet loss always means physical corruption.”** Congested queues deliberately drop packets; wireless/link issues are only one cause.

## Kết nối

[Queues](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) explain buffering. [Web request](./03_dns_http_tls_and_web_request.md) builds application/security protocols on transport. [Distributed systems](./04_distributed_systems_time_failure_and_consistency.md) must handle timeout even when TCP itself is reliable, because endpoint/process can fail.
