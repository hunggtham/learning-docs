# TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. UDP: ít đặc tả hợp đồng (contract / 계약) hơn, không phải “TCP nhưng nhanh”** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. TCP cung cấp reliable ordered byte stream** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

IP best-effort chuyển datagrams nhưng không guarantee delivery, thứ tự (order / 순서) hay duplicate-free. tầng vận chuyển (transport layer / 전송 계층) thêm lớp trừu tượng (abstraction / 추상화) giữa ứng dụng (application / 애플리케이션) endpoints qua ports và trạng thái (state / 상태) machines. Ở mức foundation, cần hiểu TCP/UDP ngữ nghĩa (semantics / 의미론); ở mức các hệ thống (systems / 시스템들) lập luận (reasoning / 추론), cần theo được đường **packet → ACK/mất mát (loss / 손실) tín hiệu (signal / 신호) → congestion/cửa sổ (window / 윈도우) trạng thái (state / 상태) → retransmission/hàng đợi (queue / 큐) → ứng dụng (application / 애플리케이션) độ trễ (latency / 지연 시간)**.

Điểm quan trọng là phân biệt ba pressure sources:

```text
receiver pressure
network-path pressure
application/runtime pressure
```

TCP có cơ chế (mechanism / 메커니즘) cho hai loại đầu, nhưng ứng dụng (application / 애플리케이션) vẫn có thể tạo hàng đợi (queue / 큐)/backlog ở tầng trên.

## 1. UDP: ít đặc tả hợp đồng (contract / 계약) hơn, không phải “TCP nhưng nhanh”

UDP (user Datagram protocol) giữ datagram boundaries và thêm ports + checksum ngữ nghĩa (semantics / 의미론), nhưng không liên kết (connection / 연결) handshake, retransmission, thứ tự (ordering / 순서) hay congestion điều khiển (control / 제어) ở giao thức (protocol / 프로토콜) itself.

Ứng dụng (application / 애플리케이션) có thể tự xây độ tin cậy (reliability / 신뢰성), sequencing, pacing và congestion hành vi (behavior / 동작). QUIC chạy trên UDP nhưng tự triển khai vận chuyển (transport / 전송) ngữ nghĩa (semantics / 의미론) phong phú hơn ở userspace, cho thấy UDP có thể là substrate chứ không phải lời giải hoàn chỉnh.

Bất biến (invariant / 불변식) của UDP tầng (layer / 계층) đơn giản hơn; burden được chuyển lên ứng dụng (application / 애플리케이션)/giao thức (protocol / 프로토콜) phía trên.

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **2. TCP cung cấp reliable ordered byte stream** tiếp nhận điểm tựa từ **1. UDP: ít đặc tả hợp đồng (contract / 계약) hơn, không phải “TCP nhưng nhanh”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. chuỗi (sequence / 시퀀스) number và ACK tạo kiến thức (knowledge / 지식) về progress** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. TCP cung cấp reliable ordered byte stream

TCP là byte stream, không giữ ứng dụng (application / 애플리케이션) message boundaries. Sender có thể `write()` 100 bytes rồi 200 bytes nhưng receiver có thể `read()` theo chunks khác tùy buffering.

Ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜) cần framing riêng: length prefix, delimiter hoặc higher-level format.

TCP bất biến (invariant / 불변식) chính là dữ liệu được trình bày cho ứng dụng (application / 애플리케이션) theo byte thứ tự (order / 순서) hợp lệ, duplicate bytes được loại và missing dữ liệu (data / 데이터) được phục hồi hoặc liên kết (connection / 연결) thất bại thay vì âm thầm tạo byte stream sai.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **2. TCP cung cấp reliable ordered byte stream** xác định đầu vào; **3. chuỗi (sequence / 시퀀스) number và ACK tạo kiến thức (knowledge / 지식) về progress** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Retransmission là khôi phục (recovery / 복구), nhưng làm độ trễ (latency / 지연 시간) tăng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. chuỗi (sequence / 시퀀스) number và ACK tạo kiến thức (knowledge / 지식) về progress

TCP gắn chuỗi (sequence / 시퀀스) number cho bytes và receiver ACK progress. Sender dùng ACK, duplicate/selective acknowledgement và timers để suy ra dữ liệu đã tới hay có khả năng mất.

ACK không nhất thiết nghĩa ứng dụng (application / 애플리케이션) bên nhận đã xử lý bytes; nó chủ yếu phản ánh vận chuyển (transport / 전송) receive progress theo hiện thực (implementation / 구현)/giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론).

Đây là lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) quan trọng: vận chuyển (transport / 전송) delivery không phải nghiệp vụ (business / 비즈니스) acknowledgement.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **3. chuỗi (sequence / 시퀀스) number và ACK tạo kiến thức (knowledge / 지식) về progress** xác định đầu vào; **4. Retransmission là khôi phục (recovery / 복구), nhưng làm độ trễ (latency / 지연 시간) tăng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. Packet mất mát (loss / 손실) không nói nguyên nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Retransmission là khôi phục (recovery / 복구), nhưng làm độ trễ (latency / 지연 시간) tăng

Khi packet bị mất, sender gửi lại dữ liệu (data / 데이터) cần thiết. độ tin cậy (reliability / 신뢰성) được mua bằng waiting + extra traffic.

Mất mát (loss / 손실) khôi phục (recovery / 복구) có thể được kích hoạt bởi hết thời gian chờ (timeout / 타임아웃) hoặc ACK-pattern-based detection tùy hiện thực (implementation / 구현). Nếu khôi phục (recovery / 복구) phải đợi hết thời gian chờ (timeout / 타임아웃), độ trễ (latency / 지연 시간) spike có thể lớn hơn nhiều so với một RTT bình thường.

Do đó ứng dụng (application / 애플리케이션) p99 có thể tăng mạnh dù average packet mất mát (loss / 손실) rất nhỏ.

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **5. Packet mất mát (loss / 손실) không nói nguyên nhân** tiếp nhận điểm tựa từ **4. Retransmission là khôi phục (recovery / 복구), nhưng làm độ trễ (latency / 지연 시간) tăng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. luồng (flow / 흐름) điều khiển (control / 제어) bảo vệ receiver** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Packet mất mát (loss / 손실) không nói nguyên nhân

Một packet có thể mất vì:

```text
congested queue drop
device/NIC/kernel drop
wireless corruption/interference
routing/path change
MTU/fragmentation issue
firewall/policy drop
receiver/application không đọc kịp gây secondary pressure
```

“Có retransmission” là bằng chứng (evidence / 증거) của delivery bài toán (problem / 문제), không tự chứng minh ISP/mạng (network / 네트워크) congestion.

Diagnosis cần correlate đường dẫn (path / 경로), giao diện (interface / 인터페이스), hàng đợi (queue / 큐) và endpoint bằng chứng (evidence / 증거).

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **5. Packet mất mát (loss / 손실) không nói nguyên nhân** xác định đầu vào; **6. luồng (flow / 흐름) điều khiển (control / 제어) bảo vệ receiver** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **7. Congestion điều khiển (control / 제어) bảo vệ mạng (network / 네트워크) đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. luồng (flow / 흐름) điều khiển (control / 제어) bảo vệ receiver

Receiver có finite buffer. Advertised receive cửa sổ (window / 윈도우) nói sender biết bao nhiêu bytes có thể outstanding mà receiver còn khả năng nhận.

Nếu ứng dụng (application / 애플리케이션) bên nhận đọc socket chậm, receive buffer đầy và advertised cửa sổ (window / 윈도우) có thể co lại. Sender bị giới hạn dù mạng (network / 네트워크) đường dẫn (path / 경로) còn bandwidth.

Chuỗi nhân quả (causal chain / 인과 사슬) có thể là:

```text
receiver application chậm
→ socket buffer đầy
→ receive window giảm
→ sender throughput giảm
```

Đây là receiver backpressure, khác congestion điều khiển (control / 제어).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **6. luồng (flow / 흐름) điều khiển (control / 제어) bảo vệ receiver** xác định đầu vào; **7. Congestion điều khiển (control / 제어) bảo vệ mạng (network / 네트워크) đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **8. Bandwidth-delay sản phẩm (product / 제품) giải thích vì sao RTT quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Congestion điều khiển (control / 제어) bảo vệ mạng (network / 네트워크) đường dẫn (path / 경로)

Congestion điều khiển (control / 제어) giới hạn amount in flight theo tín hiệu (signal / 신호) như ACK timing, mất mát (loss / 손실) và ECN tùy thuật toán (algorithm / 알고리즘). Congestion cửa sổ (window / 윈도우) phản ánh estimate về safe đường dẫn (path / 경로) sức chứa (capacity / 용량).

Nếu sender bơm quá nhanh, router/switch queues tăng, delay tăng rồi packet bị drop/mark. Congestion điều khiển (control / 제어) cố giữ thông lượng (throughput / 처리량) tốt mà tránh congestion collapse.

Flow-control cửa sổ (window / 윈도우) và congestion cửa sổ (window / 윈도우) cùng có thể giới hạn sender:

```text
usable in-flight data
≈ min(receiver window, congestion window, protocol/implementation limits)
```

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **7. Congestion điều khiển (control / 제어) bảo vệ mạng (network / 네트워크) đường dẫn (path / 경로)** xác định đầu vào; **8. Bandwidth-delay sản phẩm (product / 제품) giải thích vì sao RTT quan trọng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **9. Queueing delay có thể tăng trước packet mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Bandwidth-delay sản phẩm (product / 제품) giải thích vì sao RTT quan trọng

Để fill một đường dẫn (path / 경로) bandwidth cao nhưng RTT lớn, cần đủ dữ liệu (data / 데이터) in flight:

\[
BDP = bandwidth \times RTT
\]

Ví dụ 1 Gbit/s × 0,1 s ≈ 12,5 MB. Nếu effective cửa sổ (window / 윈도우) thấp hơn nhiều BDP, sender không thể tận dụng link dù không có mất mát (loss / 손실).

Đây là lý do “bandwidth 1 Gbps” không đồng nghĩa một TCP luồng (flow / 흐름) đạt 1 Gbps trên high-RTT đường dẫn (path / 경로).

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **9. Queueing delay có thể tăng trước packet mất mát (loss / 손실)** tiếp nhận điểm tựa từ **8. Bandwidth-delay sản phẩm (product / 제품) giải thích vì sao RTT quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Congestion cửa sổ (window / 윈도우) thay đổi theo vòng phản hồi (feedback loop / 피드백 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Queueing delay có thể tăng trước packet mất mát (loss / 손실)

Router hàng đợi (queue / 큐) có thể dài lên khi arrival tỷ lệ (rate / 비율) gần/exceeds đầu ra (output / 출력) sức chứa (capacity / 용량). Packet vẫn chưa drop nhưng RTT tăng vì phải chờ hàng đợi (queue / 큐).

Đây là **bufferbloat-style lập luận (reasoning / 추론)**: large buffers có thể giữ thông lượng (throughput / 처리량) nhưng làm độ trễ (latency / 지연 시간) lớn. Nếu ứng dụng (application / 애플리케이션) hết thời gian chờ (timeout / 타임아웃) dựa baseline RTT thấp, queueing spike có thể tạo thử lại (retry / 재시도) trước cả khi packet mất mát (loss / 손실) nghiêm trọng.

Mạng (network / 네트워크) pressure vì vậy nên đo cả độ trễ (latency / 지연 시간)/RTT phân phối (distribution / 분포) chứ không chỉ mất mát (loss / 손실) percentage.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **10. Congestion cửa sổ (window / 윈도우) thay đổi theo vòng phản hồi (feedback loop / 피드백 루프)** tiếp nhận điểm tựa từ **9. Queueing delay có thể tăng trước packet mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. RTT đo lường (measurement / 측정) và retransmission hết thời gian chờ (timeout / 타임아웃) cần variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Congestion cửa sổ (window / 윈도우) thay đổi theo vòng phản hồi (feedback loop / 피드백 루프)

Sender tăng sending tỷ lệ (rate / 비율) dựa observed delivery, rồi giảm/điều chỉnh khi thấy congestion tín hiệu (signal / 신호). thuật toán (algorithm / 알고리즘) khác nhau chọn cách probe bandwidth và respond mất mát (loss / 손실)/ECN khác nhau.

Tên thuật toán (algorithm / 알고리즘) như CUBIC/BBR là hiện thực (implementation / 구현) family; mô hình tư duy (mental model / 사고 모델) bền hơn là:

```text
estimate path state
→ choose in-flight/pacing rate
→ observe ACK/loss/RTT
→ update estimate
```

Vòng điều khiển (control loop / 제어 루프) quá aggressive có thể tạo hàng đợi (queue / 큐)/mất mát (loss / 손실); quá conservative làm underutilization.

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **10. Congestion cửa sổ (window / 윈도우) thay đổi theo vòng phản hồi (feedback loop / 피드백 루프)** nêu điều cần giải thích; **11. RTT đo lường (measurement / 측정) và retransmission hết thời gian chờ (timeout / 타임아웃) cần variance** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. Reordering khác mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. RTT đo lường (measurement / 측정) và retransmission hết thời gian chờ (timeout / 타임아웃) cần variance

Một fixed hết thời gian chờ (timeout / 타임아웃) không phù hợp mọi đường dẫn (path / 경로). TCP ước lượng RTT và variance để chọn khôi phục (recovery / 복구) timer theo trạng thái (state / 상태) hiện tại.

Hết thời gian chờ (timeout / 타임아웃) quá ngắn tạo spurious retransmission; quá dài làm khôi phục (recovery / 복구) chậm. đường dẫn (path / 경로) có jitter cao khiến timer thiết kế (design / 설계) khó hơn.

Môi trường vận hành (production / 운영 환경) symptom “yêu cầu (request / 요청) thỉnh thoảng chậm đúng vài trăm ms/giây” có thể liên quan mất mát (loss / 손실) khôi phục (recovery / 복구)/retransmission timer chứ không phải handler compute.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **11. RTT đo lường (measurement / 측정) và retransmission hết thời gian chờ (timeout / 타임아웃) cần variance** nêu điều cần giải thích; **12. Reordering khác mất mát (loss / 손실)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. Head-of-line blocking là consequence của ordered byte-stream đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Reordering khác mất mát (loss / 손실)

Packets có thể tới khác thứ tự vì parallel paths, NIC/offload hành vi (behavior / 동작) hoặc mạng (network / 네트워크) conditions. Sender/receiver không nên kết luận mọi out-of-order arrival là mất mát (loss / 손실) ngay lập tức.

Hiện đại (modern / 현대적) mechanisms như selective acknowledgement giúp mô tả holes trong received chuỗi (sequence / 시퀀스) không gian (space / 공간) tốt hơn cumulative ACK đơn giản.

Diagnosis packet dấu vết (trace / 추적) cần phân biệt:

```text
actual loss
reordering
duplicate packet
retransmission
spurious retransmission
```

Nếu không, ta dễ đổ lỗi congestion sai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **13. Head-of-line blocking là consequence của ordered byte-stream đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **12. Reordering khác mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. liên kết (connection / 연결) setup tạo cold-path độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Head-of-line blocking là consequence của ordered byte-stream đặc tả hợp đồng (contract / 계약)

Nếu byte phạm vi (range / 범위) trước bị mất, TCP không thể deliver later bytes tới ứng dụng (application / 애플리케이션) như thể gap không tồn tại. Với HTTP/2 nhiều logical streams trên một TCP liên kết (connection / 연결), packet mất mát (loss / 손실) ở vận chuyển (transport / 전송) có thể trì hoãn dữ liệu (data / 데이터) của nhiều streams cùng liên kết (connection / 연결).

HTTP/3/QUIC dùng independent streams nên mất mát (loss / 손실) trên một stream không phải khối (block / 블록) ứng dụng (application / 애플리케이션) delivery của stream khác theo cùng cách, dù chúng vẫn chia sẻ congestion/đường dẫn (path / 경로) sức chứa (capacity / 용량).

Đây là ví dụ thiết kế (design / 설계) sự đánh đổi (trade-off / 트레이드오프): giữ thứ tự (ordering / 순서) ở granularity nào quyết định blast radius của một lost packet.

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, sau nội dung của **13. Head-of-line blocking là consequence của ordered byte-stream đặc tả hợp đồng (contract / 계약)**, **14. liên kết (connection / 연결) setup tạo cold-path độ trễ (latency / 지연 시간)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **15. SYN backlog và accept hàng đợi (queue / 큐) là server-side mạng (network / 네트워크) queues** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. liên kết (connection / 연결) setup tạo cold-path độ trễ (latency / 지연 시간)

TCP handshake thêm RTT trước khi ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터) theo classic luồng (flow / 흐름). TLS thêm định danh (identity / 식별자)/cryptographic handshake, dù resumption và hiện đại (modern / 현대적) giao thức (protocol / 프로토콜) giảm round trips.

Liên kết (connection / 연결) reuse amortize setup chi phí (cost / 비용) nhưng tạo trạng thái (state / 상태): pool kích thước (size / 크기), idle hết thời gian chờ (timeout / 타임아웃), stale connections và load-balancing locality.

Cold vs warm yêu cầu (request / 요청) phải được tách trong độ trễ (latency / 지연 시간) phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **14. liên kết (connection / 연결) setup tạo cold-path độ trễ (latency / 지연 시간)** xác định đầu vào; **15. SYN backlog và accept hàng đợi (queue / 큐) là server-side mạng (network / 네트워크) queues** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Socket buffers có thể che pressure tạm thời** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. SYN backlog và accept hàng đợi (queue / 큐) là server-side mạng (network / 네트워크) queues

Trước ứng dụng (application / 애플리케이션) handler, liên kết (connection / 연결) có thể phải đi qua handshake trạng thái (state / 상태) và accept hàng đợi (queue / 큐). Under burst/attack/saturation, backlog limits có thể tạo drops/timeouts trước khi ứng dụng (application / 애플리케이션) khung phần mềm (framework / 프레임워크) thấy yêu cầu (request / 요청).

Một dịch vụ (service / 서비스) dashboard có “0 yêu cầu (request / 요청) errors” trong lúc clients connect hết thời gian chờ (timeout / 타임아웃) có thể là khả năng quan sát (observability / 관측 가능성) blind spot: thất bại (failure / 실패) đang xảy ra trước HTTP/ứng dụng (application / 애플리케이션) tầng (layer / 계층).

Bằng chứng (evidence / 증거) cần nối kernel socket/listen trạng thái (state / 상태) với edge/máy khách (client / 클라이언트) metrics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **16. Socket buffers có thể che pressure tạm thời** tiếp nhận điểm tựa từ **15. SYN backlog và accept hàng đợi (queue / 큐) là server-side mạng (network / 네트워크) queues** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. MTU và fragmentation: packet kích thước (size / 크기) là đường dẫn (path / 경로) thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Socket buffers có thể che pressure tạm thời

`send()` return nhanh có thể chỉ nghĩa bytes đã vào cục bộ (local / 로컬) socket buffer. Nếu mạng (network / 네트워크)/downstream chậm, buffer dần đầy; sau đó sender khối (block / 블록) hoặc nhận backpressure/lỗi (error / 오류) tùy chế độ (mode / 모드).

Unbounded ứng dụng (application / 애플리케이션) buffering phía trên socket không giải pressure; nó chỉ chuyển hàng đợi (queue / 큐) vào vùng nhớ động (heap / 힙) và làm độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리) debt lớn hơn.

Giống các tầng (layer / 계층) khác, buffer hấp thụ burst ngắn chứ không tạo sustainable sức chứa (capacity / 용량).

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **16. Socket buffers có thể che pressure tạm thời** xác định đầu vào; **17. MTU và fragmentation: packet kích thước (size / 크기) là đường dẫn (path / 경로) thuộc tính (property / 속성)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **18. Tunneling/VPN làm effective MTU thấp hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. MTU và fragmentation: packet kích thước (size / 크기) là đường dẫn (path / 경로) thuộc tính (property / 속성)

Mỗi link có Maximum Transmission đơn vị (unit / 단위) (MTU). IP packet lớn hơn đường dẫn (path / 경로) hỗ trợ cần fragmentation ở một số scenarios/giao thức (protocol / 프로토콜) versions hoặc sender phải dùng packet kích thước (size / 크기) nhỏ hơn qua đường dẫn (path / 경로) MTU Discovery.

Nếu required ICMP/điều khiển (control / 제어) signals bị filter hoặc PMTU kiến thức (knowledge / 지식) sai, liên kết (connection / 연결) có thể exhibit “small yêu cầu (request / 요청) works, large transfer stalls” kiểu black-hole hành vi (behavior / 동작).

Diagnosis cần hỏi:

```text
problem phụ thuộc payload size không?
path MTU có thay đổi qua tunnel/VPN không?
ICMP/PMTU discovery có hoạt động không?
MSS negotiated là bao nhiêu?
```

Không phải mọi hết thời gian chờ (timeout / 타임아웃) đều là packet mất mát (loss / 손실) ngẫu nhiên.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **17. MTU và fragmentation: packet kích thước (size / 크기) là đường dẫn (path / 경로) thuộc tính (property / 속성)** xác định đầu vào; **18. Tunneling/VPN làm effective MTU thấp hơn** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **19. ECN tách congestion tín hiệu (signal / 신호) khỏi drop trong một số đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Tunneling/VPN làm effective MTU thấp hơn

Encapsulation thêm headers nên payload packet phải nhỏ hơn để fit outer đường dẫn (path / 경로) MTU. Nếu mạng (network / 네트워크) thiết kế (design / 설계) thêm VPN/overlay/dịch vụ (service / 서비스) mesh tunnel mà không quản MTU/MSS đúng, fragmentation/drop có thể xuất hiện chỉ ở một đường dẫn (path / 경로)/môi trường (environment / 환경).

Đây là leaky lớp trừu tượng (abstraction / 추상화): ứng dụng (application / 애플리케이션) thấy TCP hết thời gian chờ (timeout / 타임아웃) nhưng lower tầng (layer / 계층) quyết định hành vi (behavior / 동작) là encapsulation overhead.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **18. Tunneling/VPN làm effective MTU thấp hơn** xác định đầu vào; **19. ECN tách congestion tín hiệu (signal / 신호) khỏi drop trong một số đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. NIC offload làm packet capture khó diễn giải hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. ECN tách congestion tín hiệu (signal / 신호) khỏi drop trong một số đường dẫn (path / 경로)

Tường minh (explicit / 명시적) Congestion Notification cho phép mạng (network / 네트워크) mark congestion thay vì phải drop packet nếu endpoints/đường dẫn (path / 경로) hỗ trợ. mô hình tư duy (mental model / 사고 모델) quan trọng là congestion tín hiệu (signal / 신호) không bắt buộc đồng nghĩa packet mất mát (loss / 손실).

Điều này củng cố distinction:

```text
congestion = resource pressure trên path
loss       = một possible observable consequence
```

Môi trường vận hành (production / 운영 환경) tooling phải đọc đúng tín hiệu (signal / 신호) của ngăn xếp (stack / 스택) hiện tại.

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **19. ECN tách congestion tín hiệu (signal / 신호) khỏi drop trong một số đường dẫn (path / 경로)** xác định đầu vào; **20. NIC offload làm packet capture khó diễn giải hơn** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **21. phân tán (distributed / 분산) hết thời gian chờ (timeout / 타임아웃) nằm trên vận chuyển (transport / 전송) độ tin cậy (reliability / 신뢰성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. NIC offload làm packet capture khó diễn giải hơn

TSO/GSO/GRO/LRO-family optimizations cho phép kernel/NIC xử lý packets theo batches/segments lớn để giảm per-packet CPU chi phí (cost / 비용). Vì vậy packet capture tại host có thể hiển thị segment kích thước (size / 크기)/checksum hành vi (behavior / 동작) khác wire-level packets.

Một capture “checksum bad” trên outbound packet có thể là sản phẩm tạo ra (artifact / 산출물) trước NIC hoàn tất checksum offload, không nhất thiết packet thật trên wire bị hỏng.

Bằng chứng (evidence / 증거) cần biết capture điểm (point / 지점) và offload trạng thái (state / 상태) trước khi kết luận.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **21. phân tán (distributed / 분산) hết thời gian chờ (timeout / 타임아웃) nằm trên vận chuyển (transport / 전송) độ tin cậy (reliability / 신뢰성)** tiếp nhận điểm tựa từ **20. NIC offload làm packet capture khó diễn giải hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Packet-level diagnosis bắt đầu từ symptom và direction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. phân tán (distributed / 분산) hết thời gian chờ (timeout / 타임아웃) nằm trên vận chuyển (transport / 전송) độ tin cậy (reliability / 신뢰성)

TCP reliable byte stream không làm RPC reliable theo nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론). tiến trình (process / 프로세스) có thể crash sau khi nhận yêu cầu (request / 요청), phản hồi (response / 응답) có thể mất, liên kết (connection / 연결) có thể reset, caller có thể hết thời gian chờ (timeout / 타임아웃) sau khi remote side tác động (effect / 효과) đã lần ghi nhận (commit / 커밋).

Vận chuyển (transport / 전송) trả lời “bytes có đi theo stream không”; phân tán (distributed / 분산) ứng dụng (application / 애플리케이션) vẫn phải giải ambiguity:

```text
request chưa tới?
đã tới nhưng chưa xử lý?
đã xử lý nhưng response mất?
```

Do đó idempotency/thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론) nằm trên TCP.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **22. Packet-level diagnosis bắt đầu từ symptom và direction** tiếp nhận điểm tựa từ **21. phân tán (distributed / 분산) hết thời gian chờ (timeout / 타임아웃) nằm trên vận chuyển (transport / 전송) độ tin cậy (reliability / 신뢰성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. bằng chứng (evidence / 증거) ở máy khách (client / 클라이언트)/máy chủ (server / 서버)/đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Packet-level diagnosis bắt đầu từ symptom và direction

Khi thấy mạng (network / 네트워크) độ trễ (latency / 지연 시간)/lỗi (error / 오류), trước tiên xác định:

```text
connect path hay established connection?
upload hay download?
một endpoint hay nhiều endpoints?
payload-size dependent?
regional/path dependent?
loss/retransmission hay pure queueing delay?
receiver window hay congestion window limiting?
```

Sau đó mới chọn packet capture/counters.

Không bắt đầu bằng “TCP tuning” trước khi biết pressure nằm sender, receiver hay đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **22. Packet-level diagnosis bắt đầu từ symptom và direction** nêu điều cần giải thích; **23. bằng chứng (evidence / 증거) ở máy khách (client / 클라이언트)/máy chủ (server / 서버)/đường dẫn (path / 경로)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. thất bại (failure / 실패) ma trận (matrix / 행렬) cho vận chuyển (transport / 전송) đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. bằng chứng (evidence / 증거) ở máy khách (client / 클라이언트)/máy chủ (server / 서버)/đường dẫn (path / 경로)

Một diagnosis mạnh kết hợp nhiều viewpoints:

```text
Application:
- connect/TLS/request timing
- timeout/retry rate
- bytes transferred

Host transport:
- RTT estimate
- retransmissions
- send/receive queue
- window state
- connection resets

Kernel/NIC:
- drops/errors
- listen/accept backlog
- interface queue
- offload context

Packet trace:
- sequence/ACK progression
- retransmission/reordering
- RTT samples
- handshake/FIN/RST
- MSS/MTU clues

Network path:
- route/path change
- loss/latency by hop only when measurement semantics justify it
- ECN/queue telemetry where available
```

Một traceroute đơn lẻ không chứng minh hop hiển thị cao là bottleneck; control-plane phản hồi (response / 응답) hành vi (behavior / 동작) có thể khác forwarded traffic.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **23. bằng chứng (evidence / 증거) ở máy khách (client / 클라이언트)/máy chủ (server / 서버)/đường dẫn (path / 경로)** nêu điều cần giải thích; **24. thất bại (failure / 실패) ma trận (matrix / 행렬) cho vận chuyển (transport / 전송) đường dẫn (path / 경로)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. thất bại (failure / 실패) ma trận (matrix / 행렬) cho vận chuyển (transport / 전송) đường dẫn (path / 경로)

Hãy thử phân biệt:

```text
DNS resolves wrong/stale endpoint
SYN timeout
TCP established nhưng TLS fail
small packets work, large payload stalls
retransmission burst khi load tăng
receive window collapses
server accept queue saturation
RST sau idle reuse
path migration/routing change
```

Mỗi symptom chỉ tới lớp trừu tượng (abstraction / 추상화) khác nhau. “mạng (network / 네트워크) issue” quá rộng để là nguyên nhân gốc (root cause / 근본 원인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **25. Mô hình tư duy** gom các mảnh từ **24. thất bại (failure / 실패) ma trận (matrix / 행렬) cho vận chuyển (transport / 전송) đường dẫn (path / 경로)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Mô hình tư duy

> TCP là máy trạng thái (state machine / 상태 머신) biến unreliable packet delivery thành ordered byte stream bằng chuỗi (sequence / 시퀀스), ACK, retransmission, luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어). Receiver cửa sổ (window / 윈도우) bảo vệ endpoint; congestion cửa sổ (window / 윈도우)/pacing phản ứng đường dẫn (path / 경로) sức chứa (capacity / 용량); socket/backlog queues nối vận chuyển (transport / 전송) với OS/ứng dụng (application / 애플리케이션). **Packet mất mát (loss / 손실), reordering, MTU, queueing và receiver pressure có thể tạo symptom giống nhau ở ứng dụng (application / 애플리케이션), nên môi trường vận hành (production / 운영 환경) diagnosis phải theo chuỗi (sequence / 시퀀스)/ACK/cửa sổ (window / 윈도우)/hàng đợi (queue / 큐) bằng chứng (evidence / 증거) thay vì chỉ nhìn hết thời gian chờ (timeout / 타임아웃).**

> **Chuyển mạch:** Trong **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **25. Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“TCP preserve message boundaries.”** Không; ứng dụng (application / 애플리케이션) cần framing.

**“UDP nhanh hơn TCP.”** UDP có ít vận chuyển (transport / 전송) ngữ nghĩa (semantics / 의미론) hơn; ứng dụng (application / 애플리케이션) có thể phải tự trả độ phức tạp (complexity / 복잡도)/chi phí (cost / 비용).

**“Retransmission nghĩa mạng (network / 네트워크) congestion.”** Không; congestion chỉ là một possible cause.

**“0% packet mất mát (loss / 손실) nghĩa mạng (network / 네트워크) healthy.”** Queueing delay/bufferbloat có thể làm độ trễ (latency / 지연 시간) xấu trước drop.

**“Ping/traceroute đủ để chứng minh ứng dụng (application / 애플리케이션) đường dẫn (path / 경로) tốt.”** Không; giao thức (protocol / 프로토콜)/đường dẫn (path / 경로)/chính sách (policy / 정책) có thể khác và chúng không đo máy chủ (server / 서버)/thời gian chạy (runtime / 런타임) queues.

**“TCP reliable nghĩa thử lại (retry / 재시도) yêu cầu (request / 요청) luôn an toàn.”** vận chuyển (transport / 전송) độ tin cậy (reliability / 신뢰성) không tạo nghiệp vụ (business / 비즈니스) idempotency.

> **Chuyển mạch:** Ở chặng này của **TCP, UDP, luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và packet-level diagnosis**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Kết nối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) giải buffering; [Web request](./03_dns_http_tls_and_web_request.md) xây HTTP/TLS trên vận chuyển (transport / 전송); [Distributed systems](./04_distributed_systems_time_failure_and_consistency.md) giải hết thời gian chờ (timeout / 타임아웃) ambiguity; [Advanced end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) nối DNS/TCP/TLS với proxy/thời gian chạy (runtime / 런타임)/DB; [OS I/O](../../03_operating_systems/advanced/05_epoll_io_uring_zero_copy_and_dma.md) giải socket readiness/completion phía host.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
