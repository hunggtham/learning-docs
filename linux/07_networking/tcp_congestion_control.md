# TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어) khác nhau** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **Congestion cửa sổ (window / 윈도우)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối TCP congestion control với feedback, cửa sổ truyền và mất gói, để giải thích throughput thay đổi theo đường truyền.

TCP không chỉ thiết lập kết nối rồi chuyển byte. Nó còn phải trả lời hai câu hỏi khác nhau: **người nhận có đủ buffer để nhận thêm dữ liệu không?** và **mạng ở giữa có đủ khả năng vận chuyển thêm dữ liệu không?** Hai câu hỏi này tương ứng với **điều khiển luồng (flow control)** và **điều khiển tắc nghẽn (congestion control)**.

Nếu không hiểu hai cơ chế này, rất dễ nhìn một kết nối “không mất” nhưng thông lượng (throughput / 처리량) thấp rồi đổ lỗi sai cho ứng dụng hoặc máy chủ (server / 서버).

## Luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어) khác nhau

Luồng (flow / 흐름) điều khiển (control / 제어) bảo vệ **receiver**. Receiver quảng bá cửa sổ nhận (receive window) để sender biết lượng dữ liệu có thể gửi thêm mà chưa cần acknowledgment.

Congestion điều khiển (control / 제어) bảo vệ **mạng (network / 네트워크) đường dẫn (path / 경로)**. Sender cố ước lượng bao nhiêu dữ liệu có thể tồn tại trên đường mà không gây tắc nghẽn nghiêm trọng.

Có thể hình dung lượng dữ liệu sender được phép giữ “đang bay” là giới hạn bởi cả hai:

```text
send window ≈ min(receiver window, congestion window)
```

Receiver khỏe không có nghĩa mạng (network / 네트워크) đường dẫn (path / 경로) khỏe, và ngược lại.

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어) khác nhau** xác định đầu vào; **Congestion cửa sổ (window / 윈도우)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bandwidth-delay sản phẩm (product / 제품)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Congestion cửa sổ (window / 윈도우)

**Cửa sổ tắc nghẽn (congestion window - cwnd)** là trạng thái ở sender. TCP tăng hoặc giảm `cwnd` dựa trên tín hiệu từ mạng như acknowledgment, packet mất mát (loss / 손실) hoặc ECN tùy thuật toán.

Nếu `cwnd` nhỏ, sender không thể giữ nhiều byte in-flight dù link có bandwidth cao.

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Bandwidth-delay sản phẩm (product / 제품)** tiếp nhận điểm tựa từ **Congestion cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RTT là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bandwidth-delay sản phẩm (product / 제품)

Một khái niệm quan trọng là **tích băng thông–độ trễ (bandwidth-delay product - BDP)**:

```text
BDP = bandwidth × round-trip time
```

Ví dụ đường truyền 1 Gbit/s với RTT 100 ms:

```text
1,000,000,000 bit/s × 0.1 s
= 100,000,000 bit
≈ 12.5 MB
```

Muốn dùng gần hết bandwidth, kết nối cần có khả năng giữ khoảng 12.5 MB dữ liệu đang bay trên đường.

Đây là lý do cùng một máy chủ (server / 서버) nhưng truyền tệp (file / 파일) tới máy cùng datacenter và tới lục địa khác có thông lượng (throughput / 처리량) khác rất lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **RTT là gì?** tiếp nhận điểm tựa từ **Bandwidth-delay sản phẩm (product / 제품)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Slow start** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RTT là gì?

**Round-trip thời gian (time / 시간) (RTT)** là thời gian một tín hiệu đi tới peer và phản hồi quay lại.

Có thể quan sát sơ bộ:

```bash
ping <host>
```

Nhưng ICMP RTT không luôn bằng TCP ứng dụng (application / 애플리케이션) RTT. tuyến (route / 경로), firewall, queuing và ưu tiên traffic có thể khác.

Trong TCP socket, `ss` có thể cung cấp thông tin sâu hơn:

```bash
ss -ti dst <IP>
```

Tùy kernel, đầu ra (output / 출력) có thể cho thấy `rtt`, `cwnd`, retransmission và thuật toán congestion điều khiển (control / 제어).

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Slow start** tiếp nhận điểm tựa từ **RTT là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao yêu cầu (request / 요청) ngắn chịu ảnh hưởng lớn?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Slow start

Khi kết nối mới bắt đầu, sender chưa biết sức chứa (capacity / 용량) của đường dẫn (path / 경로). **Khởi động chậm (slow start)** tăng lượng dữ liệu in-flight theo tốc độ nhanh từ một cửa sổ ban đầu thay vì lập tức gửi hết bandwidth.

Ý tưởng:

```text
cwnd nhỏ
  ↓
ACK thành công
  ↓
cwnd tăng nhanh
  ↓
tiếp tục cho tới ngưỡng hoặc tín hiệu congestion
```

Tên “slow start” hơi gây hiểu lầm vì tốc độ tăng ban đầu thực ra khá nhanh theo cấp số nhân qua các vòng RTT.

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Vì sao yêu cầu (request / 요청) ngắn chịu ảnh hưởng lớn?** tiếp nhận điểm tựa từ **Slow start** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Congestion avoidance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao yêu cầu (request / 요청) ngắn chịu ảnh hưởng lớn?

Nếu phản hồi (response / 응답) chỉ vài KB, slow start không đáng kể. Nhưng phản hồi (response / 응답) vừa đủ lớn và kết nối tồn tại ngắn, liên kết (connection / 연결) có thể kết thúc trước khi TCP đạt thông lượng (throughput / 처리량) tối đa.

Điều này là một lý do HTTP keep-alive và liên kết (connection / 연결) pooling có giá trị: tái sử dụng liên kết (connection / 연결) không chỉ tránh handshake mà còn giữ lại một phần trạng thái vận chuyển (transport / 전송) đã “học” đường dẫn (path / 경로).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Congestion avoidance** tiếp nhận điểm tựa từ **Vì sao yêu cầu (request / 요청) ngắn chịu ảnh hưởng lớn?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Packet mất mát (loss / 손실) là một tín hiệu congestion truyền thống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Congestion avoidance

Sau giai đoạn đầu, TCP chuyển sang tăng thận trọng hơn. Khi phát hiện congestion, thuật toán giảm tốc độ gửi.

Cơ chế cụ thể phụ thuộc congestion điều khiển (control / 제어) thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Packet mất mát (loss / 손실) là một tín hiệu congestion truyền thống** tiếp nhận điểm tựa từ **Congestion avoidance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Retransmission** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Packet mất mát (loss / 손실) là một tín hiệu congestion truyền thống

Nhiều thuật toán TCP cổ điển coi packet mất mát (loss / 손실) là tín hiệu mạng đã quá tải. Khi mất packet, sender retransmit và giảm congestion cửa sổ (window / 윈도우).

Nhưng packet mất mát (loss / 손실) cũng có thể do:

- link lỗi;
- Wi-Fi nhiễu;
- firewall/policer;
- buffer overflow;
- tuyến (route / 경로) thay đổi;
- NIC/kernel drop.

Do đó retransmission cho biết có vấn đề truyền tải, không tự chứng minh nguyên nhân cuối cùng.

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Retransmission** tiếp nhận điểm tựa từ **Packet mất mát (loss / 손실) là một tín hiệu congestion truyền thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fast retransmit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retransmission

Quan sát tổng quan:

```bash
nstat -az | grep -E 'TcpRetransSegs|TcpTimeouts'
```

Hoặc:

```bash
ss -ti
```

Packet capture:

```bash
sudo tcpdump -ni any host <IP>
```

Wireshark thường đánh dấu retransmission, duplicate ACK và out-of-order packet, nhưng phải cẩn thận với capture điểm (point / 지점) và offloading.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Fast retransmit** tiếp nhận điểm tựa từ **Retransmission** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RTO và hết thời gian chờ (timeout / 타임아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fast retransmit

Sender không nhất thiết chờ hết thời gian chờ (timeout / 타임아웃) mới retransmit. Duplicate ACK có thể cho sender biết một segment bị mất trong khi segment sau vẫn tới nơi, giúp retransmit nhanh hơn.

Đây là ví dụ TCP dùng mẫu (pattern / 패턴) acknowledgment để suy luận trạng thái mạng.

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **RTO và hết thời gian chờ (timeout / 타임아웃)** tiếp nhận điểm tựa từ **Fast retransmit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CUBIC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RTO và hết thời gian chờ (timeout / 타임아웃)

**Retransmission hết thời gian chờ (timeout / 타임아웃) (RTO)** được ước lượng từ RTT và độ biến thiên RTT. Nếu acknowledgment không tới trước hết thời gian chờ (timeout / 타임아웃), sender retransmit.

Tail độ trễ (latency / 지연 시간) mạng cao hoặc jitter mạnh có thể làm hết thời gian chờ (timeout / 타임아웃) tăng và thông lượng (throughput / 처리량) giảm ngay cả khi bandwidth danh nghĩa lớn.

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **CUBIC** tiếp nhận điểm tựa từ **RTO và hết thời gian chờ (timeout / 타임아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BBR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CUBIC

Nhiều Linux phân phối (distribution / 분포) sử dụng hoặc từng sử dụng **CUBIC** làm congestion điều khiển (control / 제어) mặc định. CUBIC tăng cửa sổ dựa trên một hàm bậc ba theo thời gian sau congestion sự kiện (event / 이벤트), nhằm hoạt động tốt hơn trên mạng bandwidth-delay sản phẩm (product / 제품) lớn so với Reno truyền thống.

Kiểm tra thuật toán hiện tại:

```bash
sysctl net.ipv4.tcp_congestion_control
```

Danh sách thuật toán khả dụng:

```bash
sysctl net.ipv4.tcp_available_congestion_control
```

Không nên đổi thuật toán trên môi trường vận hành (production / 운영 환경) chỉ để “tăng tốc” nếu chưa benchmark tải công việc (workload / 워크로드)/đường dẫn (path / 경로) thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **BBR** tiếp nhận điểm tựa từ **CUBIC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pacing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BBR

**BBR (Bottleneck Bandwidth and Round-trip propagation time)** dùng mô hình ước lượng bandwidth bottleneck và RTT tối thiểu thay vì chủ yếu đợi packet mất mát (loss / 손실) mới giảm tốc.

Ý tưởng lớn:

```text
ước lượng bandwidth có thể phục vụ
+
ước lượng RTT nền
        ↓
điều khiển pacing và lượng data in-flight
```

BBR có thể cải thiện một số tải công việc (workload / 워크로드)/đường dẫn (path / 경로), nhưng hành vi fairness và tương tác với hàng đợi (queue / 큐)/mạng (network / 네트워크) khác cần được đánh giá thực tế.

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Pacing** tiếp nhận điểm tựa từ **BBR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bufferbloat** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pacing

Thay vì gửi một burst lớn rồi im lặng, sender có thể **điều tiết nhịp gửi (pacing)** để phân bố packet đều hơn theo thời gian.

Burst lớn dễ làm hàng đợi (queue / 큐) tăng đột ngột và gây drop. Pacing giúp giảm burstiness.

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Bufferbloat** tiếp nhận điểm tựa từ **Pacing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàng đợi (queue / 큐) management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bufferbloat

Hàng đợi (queue / 큐) mạng quá lớn có thể tránh packet mất mát (loss / 손실) nhưng giữ packet quá lâu, tạo **bufferbloat**.

Kết quả nghịch lý:

```text
không mất packet nhiều
nhưng RTT tăng mạnh dưới tải
```

Ví dụ đường truyền bình thường ping 20 ms nhưng khi upload lớn ping tăng 300–1000 ms. Đây là queueing độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Hàng đợi (queue / 큐) management** tiếp nhận điểm tựa từ **Bufferbloat** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Receive cửa sổ (window / 윈도우) và cửa sổ (window / 윈도우) scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) management

Các cơ chế **Active hàng đợi (queue / 큐) Management (AQM)** như fq_codel cố kiểm soát hàng đợi (queue / 큐) độ trễ (latency / 지연 시간) thay vì chỉ để buffer đầy rồi drop.

Trên Linux có thể kiểm tra qdisc:

```bash
tc qdisc show
```

Việc cấu hình qdisc cần hiểu topology và tải công việc (workload / 워크로드); đây không phải setting nên đổi mù quáng.

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Receive cửa sổ (window / 윈도우) và cửa sổ (window / 윈도우) scaling** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Zero cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Receive cửa sổ (window / 윈도우) và cửa sổ (window / 윈도우) scaling

TCP header truyền thống có giới hạn kích thước trường dữ liệu (field / 필드) cửa sổ (window / 윈도우). **cửa sổ (window / 윈도우) scaling** cho phép cửa sổ lớn hơn, cần cho high-BDP mạng (network / 네트워크).

Nếu receive/send buffer quá nhỏ, thông lượng (throughput / 처리량) có thể bị giới hạn dù congestion cửa sổ (window / 윈도우) cho phép nhiều hơn.

Kernel Linux thường auto-tune TCP buffers trong giới hạn cấu hình.

Kiểm tra:

```bash
sysctl net.ipv4.tcp_rmem
sysctl net.ipv4.tcp_wmem
sysctl net.core.rmem_max
sysctl net.core.wmem_max
```

Không nên tăng tất cả buffer lên cực lớn. Buffer lớn tiêu RAM và có thể góp phần vào queueing/bufferbloat.

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Zero cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **Receive cửa sổ (window / 윈도우) và cửa sổ (window / 윈도우) scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TCP backlog và handshake dưới tải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Zero cửa sổ (window / 윈도우)

Nếu receiver không đọc socket đủ nhanh, receive buffer có thể đầy và quảng bá **zero cửa sổ (window / 윈도우)**. Sender phải tạm dừng.

Đây là flow-control bottleneck, không phải congestion mạng (network / 네트워크).

Trong backend, nguyên nhân có thể là:

- ứng dụng (application / 애플리케이션) luồng thực thi (thread / 스레드) bị khối (block / 블록);
- GC pause dài;
- downstream processing chậm;
- vòng lặp sự kiện (event loop / 이벤트 루프) không đọc socket kịp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **TCP backlog và handshake dưới tải** tiếp nhận điểm tựa từ **Zero cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SYN flood và SYN cookies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TCP backlog và handshake dưới tải

Máy chủ (server / 서버) còn có hàng đợi (queue / 큐) cho kết nối đang handshake và kết nối đã hoàn thành handshake chờ ứng dụng (application / 애플리케이션) `accept()`.

Nếu ứng dụng (application / 애플리케이션) accept quá chậm hoặc máy chủ (server / 서버) bị overload, liên kết (connection / 연결) mới có thể hết thời gian chờ (timeout / 타임아웃)/drop dù tiến trình (process / 프로세스) vẫn sống.

Quan sát:

```bash
ss -s
nstat -az | grep -i listen
```

Các counter cụ thể phụ thuộc kernel.

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **SYN flood và SYN cookies** tiếp nhận điểm tựa từ **TCP backlog và handshake dưới tải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TIMEWAIT và congestion điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SYN flood và SYN cookies

SYN flood cố làm cạn tài nguyên theo dõi kết nối chưa hoàn tất. Linux có cơ chế SYN cookies để giảm một số ảnh hưởng khi hàng đợi (queue / 큐) bị áp lực.

Kiểm tra:

```bash
sysctl net.ipv4.tcp_syncookies
```

SYN cookies là cơ chế phòng vệ, không thay thế sức chứa (capacity / 용량) planning hoặc mạng (network / 네트워크) protection upstream.

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **TIMEWAIT và congestion điều khiển (control / 제어)** tiếp nhận điểm tựa từ **SYN flood và SYN cookies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Keepalive vận chuyển (transport / 전송) và keep-alive HTTP khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TIME_WAIT và congestion điều khiển (control / 제어)

`TIME_WAIT` thường xuất hiện ở endpoint chủ động đóng liên kết (connection / 연결). Nhiều `TIME_WAIT` không trực tiếp nghĩa congestion điều khiển (control / 제어) lỗi, nhưng liên kết (connection / 연결) churn cao làm mất lợi ích từ liên kết (connection / 연결) reuse và tăng chi phí handshake/slow start.

Vì vậy liên kết (connection / 연결) pool có tác động cả ứng dụng (application / 애플리케이션) tài nguyên (resource / 자원) lẫn vận chuyển (transport / 전송) efficiency.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Keepalive vận chuyển (transport / 전송) và keep-alive HTTP khác nhau** tiếp nhận điểm tựa từ **TIMEWAIT và congestion điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MTU, MSS và fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Keepalive vận chuyển (transport / 전송) và keep-alive HTTP khác nhau

TCP keepalive là probe để phát hiện peer đã chết sau một khoảng thời gian. HTTP keep-alive là tái sử dụng liên kết (connection / 연결) cho nhiều yêu cầu (request / 요청).

Hai khái niệm cùng tên gần giống nhưng mục tiêu khác nhau.

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **MTU, MSS và fragmentation** tiếp nhận điểm tựa từ **Keepalive vận chuyển (transport / 전송) và keep-alive HTTP khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TSO/GSO/GRO và quan sát packet** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MTU, MSS và fragmentation

TCP thường chọn **Maximum Segment kích thước (size / 크기) (MSS)** dựa trên MTU. Nếu đường dẫn (path / 경로) MTU nhỏ hơn dự đoán và ICMP cần thiết bị chặn, liên kết (connection / 연결) có thể gặp hiện tượng “handshake được nhưng truyền payload lớn bị treo”.

Đây là **PMTU black hole**.

Điều tra:

```bash
tracepath <host>
ip link show
```

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **TSO/GSO/GRO và quan sát packet** tiếp nhận điểm tựa từ **MTU, MSS và fragmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thông lượng (throughput / 처리량) của một TCP liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TSO/GSO/GRO và quan sát packet

Linux/NIC có offloading để gom hoặc tách packet nhằm giảm CPU overhead. Vì vậy packet capture trên host đôi khi hiển thị segment lớn hoặc mẫu (pattern / 패턴) khác wire thực tế.

Các khái niệm:

- TSO: TCP Segmentation Offload;
- GSO: Generic Segmentation Offload;
- GRO: Generic Receive Offload.

Kiểm tra:

```bash
ethtool -k eth0
```

Khi phân tích packet capture, cần biết offloading có thể làm cách nhìn trên host khác packet vật lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, sau nội dung của **TSO/GSO/GRO và quan sát packet**, **Thông lượng (throughput / 처리량) của một TCP liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Nhiều liên kết (connection / 연결) có thể che giới hạn một liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông lượng (throughput / 처리량) của một TCP liên kết (connection / 연결)

Thông lượng (throughput / 처리량) đơn liên kết (connection / 연결) phụ thuộc nhiều yếu tố:

```text
RTT
loss rate
congestion algorithm
receiver window
socket buffers
application read/write rate
path bandwidth
queueing
CPU/kernel processing
```

Vì vậy “link 10 Gbps” không có nghĩa một liên kết (connection / 연결) luôn đạt 10 Gbps.

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Thông lượng (throughput / 처리량) của một TCP liên kết (connection / 연결)** đã nêu tiêu chí phân biệt, còn **Nhiều liên kết (connection / 연결) có thể che giới hạn một liên kết (connection / 연결)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Cách đo thực tế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiều liên kết (connection / 연결) có thể che giới hạn một liên kết (connection / 연결)

Nếu một liên kết (connection / 연결) bị giới hạn bởi cửa sổ (window / 윈도우)/RTT, chạy nhiều liên kết (connection / 연결) song song có thể tăng aggregate thông lượng (throughput / 처리량). Đây là lý do một số transfer công cụ (tool / 도구) dùng parallel streams.

Nhưng nhiều liên kết (connection / 연결) cũng có thể cạnh tranh unfair với traffic khác và tăng tải (load / 로드) máy chủ (server / 서버).

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Nhiều liên kết (connection / 연결) có thể che giới hạn một liên kết (connection / 연결)** đã nêu tiêu chí phân biệt, còn **Cách đo thực tế** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cách đo thực tế

`iperf3` thường được dùng để tách mạng (network / 네트워크) thông lượng (throughput / 처리량) khỏi HTTP/ứng dụng (application / 애플리케이션) lô-gic (logic / 논리):

```bash
iperf3 -s
iperf3 -c <server>
```

Nếu `iperf3` đạt thông lượng (throughput / 처리량) tốt nhưng API vẫn chậm, bottleneck có khả năng ở ứng dụng (application / 애플리케이션)/proxy/phụ thuộc (dependency / 의존성) thay vì raw mạng (network / 네트워크) sức chứa (capacity / 용량).

Nếu `iperf3` cũng kém, cần tiếp tục kiểm tra đường dẫn (path / 경로), mất mát (loss / 손실), RTT, hàng đợi (queue / 큐) và host networking.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, các dấu vết trong **Cách đo thực tế** được đọc cùng nhau ở **Mô hình tư duy** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

TCP là một vòng điều khiển phản hồi (feedback control loop):

```text
sender gửi
   ↓
network phản hồi bằng ACK/loss/delay/ECN
   ↓
sender cập nhật mô hình/cửa sổ
   ↓
điều chỉnh tốc độ gửi
```

Không nên coi TCP chỉ là “socket đáng tin cậy”. Nó là hệ thống thích nghi liên tục với trạng thái đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“Bandwidth cao thì TCP phải nhanh.”** RTT, mất mát (loss / 손실) và cửa sổ quyết định lượng dữ liệu (data / 데이터) in-flight.

**“Không packet mất mát (loss / 손실) nghĩa mạng tốt.”** Bufferbloat có thể tạo độ trễ (latency / 지연 시간) rất cao mà gần như không drop.

**“Tăng socket buffer luôn cải thiện thông lượng (throughput / 처리량).”** Buffer quá lớn có thể tốn RAM và tăng hàng đợi (queue / 큐) độ trễ (latency / 지연 시간).

**“Nhiều `TIME_WAIT` nghĩa TCP bị lỗi.”** Thường đó là hệ quả bình thường của liên kết (connection / 연결) vòng đời (lifecycle / 생명주기); cần nhìn tỷ lệ (rate / 비율) và kiến trúc (architecture / 아키텍처) liên kết (connection / 연결) reuse.

**“BBR luôn tốt hơn CUBIC.”** Hiệu quả phụ thuộc tải công việc (workload / 워크로드), kernel và mạng (network / 네트워크) đường dẫn (path / 경로).

> **Chuyển mạch:** Ở chặng này của **TCP congestion điều khiển (control / 제어), luồng (flow / 흐름) điều khiển (control / 제어) và hành vi mạng dưới tải**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc cùng [TCP, HTTP và TLS](./tcp_http_tls.md), [IP routing/NAT/conntrack](./ip_routing_nat_conntrack.md) và [reverse proxy/load balancing](./reverse_proxy_load_balancing.md). Với backend Java, liên kết (connection / 연결) pool, thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃) và yêu cầu (request / 요청) độ trễ (latency / 지연 시간) đều chịu ảnh hưởng từ vận chuyển (transport / 전송) hành vi (behavior / 동작) bên dưới.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
