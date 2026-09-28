# HTTP/2, HTTP/3, QUIC và hiện đại (modern / 현대적) vận chuyển (transport / 전송)

> **Mạch đọc:** Đọc **HTTP/2, HTTP/3, QUIC và hiện đại (modern / 현대적) vận chuyển (transport / 전송)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. HTTP/1.1 và giới hạn của connection-level parallelism** sang **2. HTTP/2: nhị phân (binary / 이진) framing và nhiều stream trên một TCP liên kết (connection / 연결)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


HTTP/1.1 over TCP/TLS vẫn là nền lịch sử quan trọng, nhưng web hiện đại phát triển để giảm liên kết (connection / 연결) overhead, multiplex requests tốt hơn và cải thiện hành vi (behavior / 동작) khi packet mất mát (loss / 손실) xảy ra. Muốn hiểu HTTP/2 và HTTP/3, cần tách ba lớp thường bị trộn lẫn: **HTTP ngữ nghĩa (semantics / 의미론)**, **stream multiplexing**, và **vận chuyển (transport / 전송) delivery/congestion hành vi (behavior / 동작)**.

Một yêu cầu (request / 요청) `GET /api/users` vẫn mang HTTP ngữ nghĩa (semantics / 의미론) dù chạy qua HTTP/1.1, HTTP/2 hay HTTP/3. Điều thay đổi mạnh là cách nhiều requests chia sẻ liên kết (connection / 연결), cách bytes được đánh số/giao lại sau mất mát (loss / 손실) và cách handshake/bảo mật (security / 보안) trạng thái (state / 상태) được thiết lập.

## 1. HTTP/1.1 và giới hạn của connection-level parallelism

HTTP/1.1 hỗ trợ persistent liên kết (connection / 연결), nhưng một liên kết (connection / 연결) vẫn là một TCP byte stream có thứ tự. Pipelining từng tồn tại trong specification nhưng khó triển khai rộng vì phản hồi (response / 응답) thứ tự (ordering / 순서) và head-of-line hành vi (behavior / 동작). Browsers vì thế thường mở nhiều TCP connections tới cùng origin để tăng parallelism.

Nhiều connections giúp tránh một số blocking giữa requests nhưng phải trả thêm handshake, congestion trạng thái (state / 상태), socket bộ nhớ (memory / 메모리) và máy chủ (server / 서버) tài nguyên (resource / 자원). Đây là ví dụ điển hình: khi một lớp trừu tượng (abstraction / 추상화) không multiplex tốt, hệ thống (system / 시스템) thường tạo parallelism bằng cách nhân số tài nguyên (resource / 자원) bên dưới.

## 2. HTTP/2: nhị phân (binary / 이진) framing và nhiều stream trên một TCP liên kết (connection / 연결)

HTTP/2 giữ HTTP methods/status/caching ngữ nghĩa (semantics / 의미론) nhưng đổi wire biểu diễn (representation / 표현) thành nhị phân (binary / 이진) frames. Mỗi yêu cầu (request / 요청)/phản hồi (response / 응답) thuộc một **luồng (stream / 스트림)** có stream ID riêng; frames của nhiều streams có thể interleave trên cùng liên kết (connection / 연결).

Headers được compress bằng HPACK để giảm repeated siêu dữ liệu (metadata / 메타데이터). ứng dụng (application / 애플리케이션) không còn phải chờ phản hồi (response / 응답) của yêu cầu (request / 요청) A hoàn tất mới gửi/nhận frames của yêu cầu (request / 요청) B theo kiểu tuần tự đơn giản.

Điều này giảm **application-level head-of-line blocking**, nhưng tất cả frames cuối cùng vẫn được đặt vào một TCP byte stream duy nhất.

## 3. Vì sao HTTP/2 vẫn có vận chuyển (transport / 전송) head-of-line blocking?

TCP hứa giao một byte stream **reliable và in-order**. Nếu segment chứa bytes ở giữa stream bị mất, TCP có thể đã nhận bytes nằm sau gap nhưng chưa được phép giao chúng lên ứng dụng (application / 애플리케이션) trước khi phần thiếu được retransmit.

Giả sử HTTP/2 stream A và B có frames interleave:

```text
TCP bytes:
A1 | B1 | A2 | B2
```

Nếu segment chứa `A2` bị mất nhưng segment chứa `B2` tới nơi, TCP vẫn phải lấp gap byte-stream trước khi giao phần sau. Từ góc nhìn HTTP/2, stream B không liên quan lô-gic (logic / 논리) tới A nhưng vẫn bị vận chuyển (transport / 전송) thứ tự (ordering / 순서) chặn.

Điểm cần giữ:

```text
HTTP/2 multiplexing
≠
independent transport delivery
```

## 4. QUIC dùng UDP làm substrate nhưng tự cung cấp vận chuyển (transport / 전송) ngữ nghĩa (semantics / 의미론)

**QUIC** chạy trên UDP datagrams để có không gian triển khai vận chuyển (transport / 전송) lô-gic (logic / 논리) ở người dùng (user / 사용자) không gian (space / 공간), nhưng QUIC không phải “UDP gửi gì mất nấy”. Nó tự cung cấp reliable streams, mất mát (loss / 손실) detection/khôi phục (recovery / 복구), luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어), cryptographic handshake và liên kết (connection / 연결) management.

HTTP/3 ánh xạ HTTP ngữ nghĩa (semantics / 의미론) lên QUIC. Mỗi QUIC stream có không gian byte/offset riêng nên mất mát (loss / 손실) của dữ liệu stream A không buộc vận chuyển (transport / 전송) giữ lại dữ liệu đã hoàn chỉnh của stream B chỉ để bảo toàn một toàn cục (global / 전역) byte stream như TCP.

Điều này giảm connection-wide head-of-line blocking do vận chuyển (transport / 전송) thứ tự (ordering / 순서), nhưng packet mất mát (loss / 손실) không miễn phí: lost bytes vẫn phải retransmit, congestion controller vẫn có thể giảm sending tỷ lệ (rate / 비율) và nhiều streams vẫn chia sẻ cùng mạng (network / 네트워크) đường dẫn (path / 경로)/sức chứa (capacity / 용량).

## 5. Packet number và stream offset là hai loại thứ tự (ordering / 순서) khác nhau

Một mô hình tư duy (mental model / 사고 모델) hữu ích là tách **packet number** khỏi **stream offset**.

QUIC packets có packet numbers phục vụ acknowledgement/mất mát (loss / 손실) khôi phục (recovery / 복구). Dữ liệu ứng dụng (application / 애플리케이션) bên trong lại thuộc các streams với offsets riêng. Một stream cần reconstruct bytes theo thứ tự của chính stream đó, nhưng stream khác không cần chờ một gap không liên quan.

Đây là cơ chế bên trong giải thích tại sao HTTP/3 cải thiện hành vi (behavior / 동작) dưới mất mát (loss / 손실) so với HTTP/2/TCP mà không từ bỏ độ tin cậy (reliability / 신뢰성).

Câu hỏi đúng là: **thứ tự (ordering / 순서) bất biến (invariant / 불변식) nằm ở connection-wide byte stream hay từng logical stream?**

## 6. ACK và mất mát (loss / 손실) khôi phục (recovery / 복구) không đồng nghĩa retransmit packet y hệt

Vận chuyển (transport / 전송) reliable cần biết dữ liệu nào peer đã nhận và dữ liệu nào cần gửi lại. QUIC có acknowledgements cho packet ranges và loss-detection lô-gic (logic / 논리) dựa trên packet thứ tự (ordering / 순서)/timing. Khi mất mát (loss / 손실) được suy ra, hiện thực (implementation / 구현) có thể retransmit **thông tin (information / 정보)/frames cần thiết** trong packet mới thay vì tái phát nguyên datagram cũ với cùng packet định danh (identity / 식별자).

Điều này quan trọng cho debugging: packet numbers phản ánh transmission attempts, còn stream offsets phản ánh logical dữ liệu (data / 데이터). Một yêu cầu (request / 요청) chậm có thể do cùng stream dữ liệu (data / 데이터) phải được gửi lại dù packet định danh (identity / 식별자) đã thay đổi.

## 7. Congestion điều khiển (control / 제어) vẫn là shared-resource bất biến (invariant / 불변식)

QUIC tránh một loại head-of-line blocking nhưng không thể bỏ **điều khiển tắc nghẽn (congestion control / 혼잡 제어)**. Nhiều connections cùng chia sẻ bottleneck link; sender phải điều chỉnh amount of in-flight dữ liệu (data / 데이터) theo bằng chứng (evidence / 증거) từ ACK/mất mát (loss / 손실)/ECN và thuật toán (algorithm / 알고리즘) đang dùng.

Các streams trên một liên kết (connection / 연결) thường vẫn chịu chung đường dẫn (path / 경로) congestion trạng thái (state / 상태). Nếu packet mất mát (loss / 손실) làm congestion cửa sổ (window / 윈도우) giảm, thông lượng (throughput / 처리량) của nhiều streams có thể cùng giảm dù delivery thứ tự (ordering / 순서) độc lập hơn.

Vì vậy câu “HTTP/3 packet mất mát (loss / 손실) chỉ ảnh hưởng một stream” là quá mạnh. Chính xác hơn: mất mát (loss / 손실) không bắt vận chuyển (transport / 전송) khối (block / 블록) delivery của stream khác chỉ vì một toàn cục (global / 전역) byte gap, nhưng **sức chứa (capacity / 용량) reaction ở liên kết (connection / 연결)/đường dẫn (path / 경로) mức (level / 수준) vẫn có thể ảnh hưởng tất cả**.

## 8. luồng (flow / 흐름) điều khiển (control / 제어) khác congestion điều khiển (control / 제어)

**Điều khiển luồng (flow control / 흐름 제어)** bảo vệ receiver khỏi sender gửi nhanh hơn khả năng nhận/buffer. **Congestion điều khiển (control / 제어)** bảo vệ mạng (network / 네트워크) đường dẫn (path / 경로) khỏi lượng in-flight traffic quá lớn.

QUIC có thể có connection-level và stream-level flow-control limits. Một stream hết receive credit có thể dừng dù mạng (network / 네트워크) không congested. Ngược lại, receive buffers còn nhiều nhưng congestion cửa sổ (window / 윈도우) nhỏ vẫn giới hạn transmission.

Khi gỡ lỗi (debug / 디버그) thông lượng (throughput / 처리량) thấp, cần phân biệt receiver flow-control limited, congestion-window/đường dẫn (path / 경로) limited, ứng dụng (application / 애플리케이션) không tạo dữ liệu đủ nhanh, packet mất mát (loss / 손실)/retransmission hay CPU/crypto/thời gian chạy (runtime / 런타임) bottleneck.

## 9. TLS tích hợp (integration / 통합) làm bảo mật (security / 보안) trở thành một phần của vận chuyển (transport / 전송) máy trạng thái (state machine / 상태 머신)

QUIC tích hợp TLS 1.3 chặt với liên kết (connection / 연결) establishment. vận chuyển (transport / 전송) parameters và cryptographic trạng thái (state / 상태) tiến triển cùng handshake, giúp dùng chung (common / 공통) đường dẫn (path / 경로) giảm round trips so với việc dựng TCP rồi mới dựng TLS như hai máy trạng thái (state machine / 상태 머신) nối tiếp.

Tuy nhiên “ít round trip hơn” không đồng nghĩa zero chi phí (cost / 비용). Certificate kiểm tra hợp lệ (validation / 검증), key derivation, máy chủ (server / 서버) processing, packet mất mát (loss / 손실) và đường dẫn (path / 경로) RTT vẫn tồn tại.

Handshake thất bại (failure / 실패) cũng không nhất thiết là “QUIC bug”. Nguyên nhân có thể nằm ở certificate, clock, trust store, chính sách mạng (network policy / 네트워크 정책), UDP filtering hoặc phiên bản (version / 버전) negotiation.

## 10. 0-RTT đổi độ trễ (latency / 지연 시간) lấy replay giả định (assumption / 가정)

Repeat máy khách (client / 클라이언트) có thể gửi **0-RTT early dữ liệu (data / 데이터)** khi có session trạng thái (state / 상태) phù hợp. Lợi ích là ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터) có thể đi trước khi full handshake mới hoàn tất.

Đổi lại, early dữ liệu (data / 데이터) có replay rủi ro (risk / 위험) theo threat mô hình (model / 모델) của giao thức (protocol / 프로토콜). ứng dụng (application / 애플리케이션) chỉ nên cho 0-RTT thực hiện thao tác (operation / 연산) có ngữ nghĩa (semantics / 의미론) chịu được replay hoặc có idempotency/deduplication bảo vệ phù hợp.

Một payment `POST` không tự trở nên an toàn chỉ vì vận chuyển (transport / 전송) cho phép gửi sớm. bảo mật (security / 보안)/hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) không được làm yếu nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식).

## 11. liên kết (connection / 연결) ID tách logical liên kết (connection / 연결) khỏi 4-tuple

TCP liên kết (connection / 연결) thường gắn chặt với nguồn (source / 소스)/destination IP+cổng (port / 포트) pair. QUIC dùng **liên kết (connection / 연결) ID** để peer có thể nhận diện logical liên kết (connection / 연결) ngay cả khi mạng (network / 네트워크) address thay đổi trong một số tình huống như NAT rebinding hoặc máy khách (client / 클라이언트) chuyển Wi-Fi sang cellular.

Di chuyển (migration / 마이그레이션) không có nghĩa “chấp nhận packet từ bất kỳ địa chỉ nào”. đường dẫn (path / 경로) mới cần được kiểm tra hợp lệ (validation / 검증) để tránh spoofing/amplification và hiện thực (implementation / 구현) vẫn phải quản lý congestion/đường dẫn (path / 경로) trạng thái (state / 상태) đúng.

Vận chuyển (transport / 전송) liên kết (connection / 연결) continuity cũng không thay ứng dụng (application / 애플리케이션) authorization/session ngữ nghĩa (semantics / 의미론). Một valid liên kết (connection / 연결) không tự chứng minh yêu cầu (request / 요청) được phép truy cập tài nguyên (resource / 자원).

## 12. Address kiểm tra hợp lệ (validation / 검증) và amplification protection

UDP cho phép sender giả mạo nguồn (source / 소스) address dễ hơn connection-oriented handshake intuition. máy chủ (server / 서버) không nên gửi lượng dữ liệu lớn tới địa chỉ chưa được chứng minh reachable, nếu không attacker có thể biến máy chủ (server / 서버) thành reflection/amplification nguồn (source / 소스).

QUIC vì vậy có cơ chế address kiểm tra hợp lệ (validation / 검증) và giới hạn amount of dữ liệu (data / 데이터) máy chủ (server / 서버) được gửi trước khi máy khách (client / 클라이언트) address được validate.

Đây là ví dụ bảo mật (security / 보안) bất biến (invariant / 불변식) ảnh hưởng trực tiếp hiệu năng (performance / 성능) đường dẫn (path / 경로): trước khi trust reachability, máy chủ (server / 서버) phải hạn chế amplification dù nó có phản hồi (response / 응답) lớn sẵn sàng.

## 13. đường dẫn (path / 경로) MTU: vận chuyển (transport / 전송) không thể gửi datagram lớn tùy ý

Mỗi mạng (network / 네트워크) đường dẫn (path / 경로) có giới hạn kích thước packet có thể đi qua mà không cần fragmentation, thường được lập luận (reasoning / 추론) bằng **đường dẫn (path / 경로) MTU (Maximum Transmission Unit / 경로 MTU)**.

QUIC chạy trên UDP nên hiện thực (implementation / 구현) phải chọn datagram kích thước (size / 크기) phù hợp và thích nghi với đường dẫn (path / 경로). Datagram quá lớn có thể bị drop trên một hop. Nếu ICMP/PTB signaling bị firewall chặn hoặc đường dẫn (path / 경로) hành vi (behavior / 동작) bất thường, hệ thống (system / 시스템) có thể gặp **PMTU black hole**: small packets/handshake có vẻ hoạt động nhưng large datagrams liên tục biến mất.

Symptom thường khó chịu: liên kết (connection / 연결) thiết lập được, yêu cầu (request / 요청) nhỏ chạy, nhưng transfer lớn stall hoặc retransmit nhiều.

Đây là lý do packet-level diagnosis phải nhìn kích thước (size / 크기) phân phối (distribution / 분포), ICMP/chính sách mạng (network policy / 네트워크 정책) và mất mát (loss / 손실) mẫu (pattern / 패턴) thay vì chỉ “ping được nên mạng (network / 네트워크) ổn”.

## 14. UDP blocking và fallback là môi trường vận hành (production / 운영 환경) reality

Một số enterprise mạng (network / 네트워크), firewall hoặc middlebox vẫn chặn/giới hạn UDP. trình duyệt (browser / 브라우저)/máy khách (client / 클라이언트) có thể thử HTTP/3 rồi fallback sang HTTP/2/TCP.

Nếu chỉ nhìn server-side HTTP/3 metrics, ta có thể bỏ qua population đang fallback. bằng chứng vận hành (production evidence / 운영 증거) nên phân biệt attempted HTTP/3, successful HTTP/3, fallback HTTP/2, handshake/phiên bản (version / 버전) lỗi (error / 오류) và UDP đường dẫn (path / 경로) thất bại (failure / 실패).

Giao thức (protocol / 프로토콜) mới phải coexist với triển khai (deployment / 배포) reality; tính tương thích (compatibility / 호환성) đường dẫn (path / 경로) là một phần của hệ thống (system / 시스템) thiết kế (design / 설계).

## 15. liên kết (connection / 연결) coalescing và origin ranh giới (boundary / 경계)

HTTP/2/3 có thể reuse liên kết (connection / 연결) cho nhiều origins trong điều kiện certificate/DNS/address và máy khách (client / 클라이언트) chính sách (policy / 정책) cho phép. Điều này tiết kiệm handshake/socket trạng thái (state / 상태), nhưng **vận chuyển (transport / 전송) reuse không hợp nhất bảo mật (security / 보안) origins**.

Trình duyệt (browser / 브라우저) vẫn phải duy trì origin isolation, credential/cookie rules và certificate định danh (identity / 식별자). “Cùng liên kết (connection / 연결)” không có nghĩa hai applications được phép đọc trạng thái (state / 상태) của nhau.

## 16. Header compression có trạng thái (state / 상태) và thất bại (failure / 실패) ranh giới (boundary / 경계) riêng

HTTP/2 dùng HPACK; HTTP/3 dùng QPACK để thích nghi với vận chuyển (transport / 전송) có streams độc lập. Header compression giảm repeated bytes nhưng tạo dynamic-table trạng thái (state / 상태) giữa peers.

Stateful compression phải tránh biến packet/stream reordering thành toàn cục (global / 전역) blocking quá mức. Đây là lý do HTTP/3 không chỉ “đổi TCP thành QUIC”; một số cơ chế (mechanism / 메커니즘) phía HTTP cũng phải thiết kế lại để phù hợp delivery mô hình (model / 모델) mới.

## 17. Worked example: packet mất mát (loss / 손실) trên một page nhiều requests

Giả sử trình duyệt (browser / 브라우저) tải HTML, CSS, JavaScript và nhiều API calls qua một liên kết (connection / 연결). Với HTTP/2/TCP, một lost TCP segment có thể tạo byte gap; frames của streams khác đã tới sau gap vẫn chưa được TCP giao lên HTTP/2.

Với HTTP/3/QUIC, lost dữ liệu (data / 데이터) của stream JavaScript vẫn phải recover, nhưng completed dữ liệu (data / 데이터) của API stream khác có thể được deliver nếu stream của nó không thiếu bytes. Tuy nhiên mất mát (loss / 손실) bằng chứng (evidence / 증거) có thể khiến congestion controller giảm sending tỷ lệ (rate / 비율) cho liên kết (connection / 연결), nên mọi stream vẫn có thể chậm hơn một phần.

Mô hình tư duy (mental model / 사고 모델) đúng là:

```text
independent stream ordering
+
shared path capacity
```

chứ không phải “mất mát (loss / 손실) chỉ ảnh hưởng đúng một yêu cầu (request / 요청)”.

## 18. khả năng quan sát (observability / 관측 가능성) khó hơn vì vận chuyển (transport / 전송) siêu dữ liệu (metadata / 메타데이터) được mã hóa nhiều hơn

QUIC mã hóa nhiều vận chuyển (transport / 전송) siêu dữ liệu (metadata / 메타데이터) hơn TCP, giúp privacy và giảm giao thức (protocol / 프로토콜) ossification do middlebox phụ thuộc vào fields nội bộ. Đổi lại packet capture ngoài endpoint không còn nhìn được mọi trạng thái (state / 상태) như TCP truyền thống.

Diagnosis cần tăng endpoint telemetry: handshake phase, negotiated phiên bản (version / 버전), RTT estimate, mất mát (loss / 손실)/khôi phục (recovery / 복구) counters, congestion trạng thái (state / 상태), flow-control blocked thời gian (time / 시간), stream độ trễ (latency / 지연 시간) và fallback reason.

Privacy/evolvability và operator visibility là sự đánh đổi (trade-off / 트레이드오프) thật, không phải hiện thực (implementation / 구현) accident.

## 19. Packet-level diagnosis: đọc symptom theo cơ chế (mechanism / 메커니즘)

Nếu time-to-first-byte tăng, trước tiên tách DNS, liên kết (connection / 연결) setup, TLS/QUIC handshake, máy chủ (server / 서버) processing và first phản hồi (response / 응답) bytes. Nếu thông lượng (throughput / 처리량) transfer lớn thấp, kiểm tra RTT, mất mát (loss / 손실), congestion cửa sổ (window / 윈도우)/pacing, flow-control blocked trạng thái (state / 상태) và đường dẫn (path / 경로) MTU. Nếu chỉ một subset mạng (network / 네트워크) thất bại (fail / 실패), so sánh UDP reachability/fallback, NAT/firewall hành vi (behavior / 동작) và MTU.

Bằng chứng (evidence / 증거) hữu ích gồm:

```text
protocol/version negotiated
connection reuse vs cold setup
handshake duration/failure reason
smoothed RTT và RTT variance
loss/retransmitted data
congestion-limited time
flow-control-limited time
stream-level latency
UDP/HTTP3 fallback rate
packet/datagram sizes và PMTU symptoms
```

Packet capture chỉ là một bằng chứng (evidence / 증거) nguồn (source / 소스). ứng dụng (application / 애플리케이션) dấu vết (trace / 추적) giải thích yêu cầu (request / 요청) ngữ nghĩa (semantics / 의미론); endpoint vận chuyển (transport / 전송) metrics giải thích trạng thái (state / 상태) mà encrypted wire capture có thể không thấy.

## 20. phiên bản (version / 버전) evolution và triển khai (deployment / 배포)

HTTP/2 và HTTP/3 là giao thức (protocol / 프로토콜) standards, nhưng môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) phụ thuộc máy khách (client / 클라이언트)/máy chủ (server / 서버) hiện thực (implementation / 구현), congestion thuật toán (algorithm / 알고리즘), TLS thư viện (library / 라이브러리), kernel/mạng (network / 네트워크) đường dẫn (path / 경로) và intermediaries. Không nên gắn một tối ưu hóa (optimization / 최적화) với một trình duyệt (browser / 브라우저)/máy chủ (server / 서버) phiên bản (version / 버전) rồi coi nó là universal law.

Khi rollout HTTP/3, nên so theo cohorts và mạng (network / 네트워크) conditions: RTT thấp/cao, mất mát (loss / 손실) thấp/cao, mobile/Wi-Fi, geographic region, cold/reused connections. Average toàn fleet có thể che nhóm thật sự được lợi hoặc bị regression.

## Dùng chung (common / 공통) Misconceptions

**“HTTP/2 bỏ TCP.”** Không; HTTP/2 thường chạy trên TCP + TLS.

**“QUIC là UDP nên không reliable.”** QUIC dùng UDP datagrams làm substrate nhưng tự cung cấp reliable streams, mất mát (loss / 손실) khôi phục (recovery / 복구), luồng (flow / 흐름) điều khiển (control / 제어) và congestion điều khiển (control / 제어).

**“HTTP/3 loại bỏ mọi head-of-line blocking.”** Nó giảm connection-wide HOL do TCP byte-stream thứ tự (ordering / 순서); một stream vẫn cần thứ tự bytes của chính nó và đường dẫn (path / 경로) congestion vẫn là dùng chung (shared / 공유) ràng buộc (constraint / 제약조건).

**“QUIC di chuyển (migration / 마이그레이션) nghĩa session/auth tự survive mọi mạng (network / 네트워크) thay đổi (change / 변경).”** vận chuyển (transport / 전송) có thể survive đường dẫn (path / 경로) thay đổi (change / 변경); nghiệp vụ (business / 비즈니스)/session authorization là đặc tả hợp đồng (contract / 계약) ở tầng khác.

**“Ping được nghĩa MTU/đường dẫn (path / 경로) ổn.”** Small packets có thể đi trong khi larger UDP datagrams bị black-hole.

**“HTTP/3 luôn nhanh hơn.”** Lợi ích phụ thuộc RTT, mất mát (loss / 손실), liên kết (connection / 연결) reuse, tải công việc (workload / 워크로드), hiện thực (implementation / 구현) và chính sách mạng (network policy / 네트워크 정책).

## Mô hình tư duy (mental model / 사고 모델)

> HTTP evolution giữ ứng dụng (application / 애플리케이션) ngữ nghĩa (semantics / 의미론) nhưng thay cách **nhiều streams chia sẻ một vận chuyển (transport / 전송) liên kết (connection / 연결)**. HTTP/2 multiplex ở ứng dụng (application / 애플리케이션) tầng (layer / 계층) nhưng vẫn chịu một TCP byte stream; HTTP/3 dùng QUIC để cho từng stream có thứ tự (ordering / 순서) riêng, trong khi congestion/đường dẫn (path / 경로) sức chứa (capacity / 용량) vẫn được chia sẻ. Khi gỡ lỗi (debug / 디버그), hãy tách handshake, stream thứ tự (ordering / 순서), luồng (flow / 흐름) điều khiển (control / 제어), congestion điều khiển (control / 제어) và đường dẫn (path / 경로) MTU thay vì gọi chung là “mạng (network / 네트워크) chậm”.

## Kết nối

Đọc [TCP/UDP và congestion](./02_transport_tcp_udp_and_congestion.md), [DNS/HTTP/TLS](./03_dns_http_tls_and_web_request.md), [socket/NAT/firewall/VPN](./06_sockets_ipv6_nat_firewalls_and_vpn.md), [web request end-to-end](../90_connections/01_browser_to_database_request.md) và [request path advanced](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 network layers packets and encapsulation](./00_network_layers_packets_and_encapsulation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
