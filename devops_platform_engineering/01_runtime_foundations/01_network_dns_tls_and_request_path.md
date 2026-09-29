# Từ URL đến tiến trình (process / 프로세스): DNS, TCP, TLS, proxy và đường đi của yêu cầu (request path / 요청 경로)

> **Mạch đọc:** Đọc **Từ URL đến tiến trình (process / 프로세스): DNS, TCP, TLS, proxy và đường đi của yêu cầu (request path / 요청 경로)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. mạng (network / 네트워크) troubleshooting cần một đường đi cụ thể** sang **2. DNS là ánh xạ (mapping / 매핑) có bộ nhớ đệm (cache / 캐시) và thời gian sống**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. mạng (network / 네트워크) troubleshooting cần một đường đi cụ thể

Khi người dùng (user / 사용자) nói “API không vào được”, câu đó chưa phải thất bại (failure / 실패) mô hình (model / 모델). yêu cầu (request / 요청) đi qua nhiều trạng thái (state / 상태): tên miền phải resolve, tuyến (route / 경로) phải tồn tại, TCP liên kết (connection / 연결) phải mở, TLS handshake phải thành công, proxy/bộ cân bằng tải (load balancer / 로드 밸런서) phải chọn backend, backend phải listen, ứng dụng (application / 애플리케이션) phải xử lý phụ thuộc (dependency / 의존성) rồi phản hồi (response / 응답) mới quay về.

Mô hình tư duy (mental model / 사고 모델) hiệu quả là vẽ đường đi của yêu cầu (request path / 요청 경로) thay vì đoán:

```text
client
  ↓ DNS
IP / load balancer
  ↓ TCP + TLS
edge / ingress / reverse proxy
  ↓ service routing
backend endpoint
  ↓ socket
application process
  ↓
database / cache / external service
```

Mỗi mũi tên có dạng thất bại (failure mode / 실패 모드) và bằng chứng (evidence / 증거) riêng.

## 2. DNS là ánh xạ (mapping / 매핑) có bộ nhớ đệm (cache / 캐시) và thời gian sống

DNS không phải một “danh bạ tức thời”. Resolver có thể bộ nhớ đệm (cache / 캐시) bản ghi (record / 레코드) theo TTL, nhiều tầng bộ nhớ đệm (cache / 캐시) tồn tại ở OS, thời gian chạy (runtime / 런타임), cục bộ (local / 로컬) DNS, cluster DNS và upstream resolver. Vì vậy vừa đổi bản ghi (record / 레코드) nhưng một số máy khách (client / 클라이언트) vẫn đi IP cũ không nhất thiết là DNS “sai”; có thể là expected bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작).

Khi gỡ lỗi (debug / 디버그), cần phân biệt name resolution thất bại với liên kết (connection / 연결) thất bại. `dig` hoặc `nslookup` cho thấy resolver trả gì; nhưng ứng dụng (application / 애플리케이션) thời gian chạy (runtime / 런타임) có thể có bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) khác. Trong Kubernetes còn có khám phá dịch vụ (service discovery / 서비스 디스커버리) và cluster DNS, nên cùng một hostname có thể resolve khác tùy không gian tên (namespace / 네임스페이스)/tìm kiếm (search / 검색) lĩnh vực (domain / 도메인).

## 3. TCP kiểm tra reachability ở mức liên kết (connection / 연결)

Nếu DNS đã trả đúng IP, bước sau là có mở TCP liên kết (connection / 연결) được không. `curl` tiện nhưng gộp DNS, TCP, TLS và HTTP thành một thao tác. Khi cần cô lập tầng (layer / 계층), có thể dùng `nc -vz host port`, `ss`, hoặc `curl -v` để xem chuỗi (sequence / 시퀀스).

`connection refused` thường hàm ý tuyến (route / 경로) tới host tồn tại nhưng tại endpoint đó không có listener hoặc firewall chủ động reject. `timeout` có thể là packet bị drop, tuyến (route / 경로) sai, bảo mật (security / 보안) chính sách (policy / 정책) hoặc máy chủ (server / 서버) không phản hồi. Hai lỗi (error / 오류) này không nên được giải thích giống nhau.

## 4. TLS không chỉ là encryption

TLS vừa bảo vệ kênh vừa xác thực danh tính endpoint thông qua certificate chuỗi (chain / 사슬) và hostname kiểm tra hợp lệ (validation / 검증). Một dịch vụ (service / 서비스) có thể reachable ở TCP nhưng TLS thất bại (fail / 실패) vì certificate hết hạn, SAN không khớp hostname, trust chuỗi (chain / 사슬) thiếu intermediate hoặc máy khách (client / 클라이언트)/máy chủ (server / 서버) không có cipher/giao thức (protocol / 프로토콜) chung.

Trong service-to-service, mutual TLS còn xác thực cả máy khách (client / 클라이언트). Cơ chế PKI, certificate kiểm tra hợp lệ (validation / 검증) và dịch vụ (service / 서비스) định danh (identity / 식별자) đã có chuẩn gốc (canonical / 정본) chapter tại [PKI, mTLS và service identity](../../computer_science/07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md). DevOps cần tập trung vào vòng đời (lifecycle / 생명주기): ai issue cert, ai rotate, trust bundle phân phối thế nào, expiry được alert trước bao lâu và rollout có backward tính tương thích (compatibility / 호환성) không.

## 5. bộ cân bằng tải (load balancer / 로드 밸런서) và reverse proxy tạo thêm trạng thái (state / 상태)

Bộ cân bằng tải (load balancer / 로드 밸런서) không đơn giản “chia đều yêu cầu (request / 요청)”. Nó có health trạng thái (state / 상태), liên kết (connection / 연결) pool, hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), thuật toán (algorithm / 알고리즘) và có thể terminate TLS. Nếu health check đường dẫn (path / 경로) khác hành vi (behavior / 동작) thật, backend có thể được coi healthy nhưng người dùng (user / 사용자) yêu cầu (request / 요청) vẫn thất bại (fail / 실패). Nếu proxy hết thời gian chờ (timeout / 타임아웃) 30 giây nhưng ứng dụng (application / 애플리케이션) hết thời gian chờ (timeout / 타임아웃) 60 giây, yêu cầu (request / 요청) có thể bị client-facing thất bại (failure / 실패) trong khi backend vẫn tiếp tục xử lý.

Hết thời gian chờ (timeout / 타임아웃) nên được thiết kế như ngân sách (budget / 예산) giảm dần dọc đường đi của yêu cầu (request path / 요청 경로). Upstream hết thời gian chờ (timeout / 타임아웃) phải dài hơn downstream thao tác (operation / 연산) đủ để ứng dụng (application / 애플리케이션) có thời gian xử lý thất bại (failure / 실패) và trả phản hồi (response / 응답), nhưng không dài đến mức giữ tài nguyên (resource / 자원) vô hạn.

## 6. thử lại (retry / 재시도) có thể cứu transient thất bại (failure / 실패) hoặc khuếch đại outage

Thử lại (retry / 재시도) hữu ích khi thất bại (failure / 실패) tạm thời và thao tác (operation / 연산) an toàn để lặp. Nhưng khi downstream đã quá tải, mỗi yêu cầu (request / 요청) thử lại (retry / 재시도) thêm làm traffic tăng, tạo phản hồi (feedback / 피드백) dương và có thể biến độ trễ (latency / 지연 시간) spike thành outage. thử lại (retry / 재시도) cần deadline, backoff, jitter và giới hạn attempt; ghi (write / 쓰기) thao tác (operation / 연산) còn cần idempotency ngữ nghĩa (semantics / 의미론).

Phân tán (distributed / 분산) thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) được đào sâu ở [distributed transactions, exactly-once và failure semantics](../../computer_science/06_networks_distributed_systems/advanced/00_distributed_transactions_exactly_once_and_failure_semantics.md). Ở tầng nền tảng (platform / 플랫폼), bất biến (invariant / 불변식) là thử lại (retry / 재시도) chính sách (policy / 정책) phải nhìn thấy được và không được mặc định vô hạn trong nhiều proxy tầng (layer / 계층) cùng lúc.

## 7. Kubernetes thêm virtual mạng (network / 네트워크) lớp trừu tượng (abstraction / 추상화)

Trong Kubernetes, `Service` thường cung cấp virtual endpoint ổn định trong khi `Pod` endpoint thay đổi. Ingress/Gateway nhận traffic từ ngoài và tuyến (route / 경로) vào dịch vụ (service / 서비스). chính sách mạng (network policy / 네트워크 정책) có thể giới hạn luồng (flow / 흐름). CNI hiện thực (implementation / 구현) quyết định packet đi như thế nào nhưng mô hình tư duy (mental model / 사고 모델) trước tiên vẫn là: name → virtual dịch vụ (service / 서비스) → endpoint → pod socket.

Khi một `Service` không trả traffic, kiểm tra selector/endpoints trước khi đổ lỗi cho DNS. Nếu endpoint danh sách (list / 목록) rỗng, name resolution có thể hoàn toàn đúng nhưng không có backend. Nếu endpoint có và pod listen, tiếp tục kiểm tra ánh xạ cổng (port mapping / 포트 매핑), readiness, chính sách mạng (network policy / 네트워크 정책) và proxy/data-plane trạng thái (state / 상태).

## 8. NAT và địa chỉ quan sát được

NAT thay đổi nguồn (source / 소스)/destination address ở một số ranh giới (boundary / 경계). Điều này quan trọng với allowlist, logging và tỷ lệ (rate / 비율) limit. ứng dụng (application / 애플리케이션) có thể thấy IP của proxy thay vì máy khách (client / 클라이언트) thật; proxy có thể đưa original máy khách (client / 클라이언트) IP qua header nhưng chỉ nên trust header từ proxy ranh giới (boundary / 경계) đã biết.

Khi gỡ lỗi (debug / 디버그) “IP nào đang gọi”, phải hỏi ở tầng (layer / 계층) nào. Packet capture trên nút (node / 노드), bộ cân bằng tải (load balancer / 로드 밸런서) truy cập (access / 접근) log và ứng dụng (application / 애플리케이션) truy cập (access / 접근) log có thể hiển thị ba địa chỉ khác nhau mà đều đúng theo perspective của chúng.

## 9. Một bài toán gỡ lỗi (debug / 디버그) từng bước

Giả sử `https://api.example.com/orders` trả `502`.

Đầu tiên xác nhận DNS trả endpoint mong muốn. Sau đó `curl -v` để biết TLS có hoàn thành không. Nếu TLS thành công và phản hồi (response / 응답) là HTTP 502 từ ingress, client-to-ingress đường dẫn (path / 경로) về cơ bản đã hoạt động. Tập trung sang ingress-to-backend.

Kiểm tra tuyến (route / 경로)/dịch vụ (service / 서비스) ánh xạ (mapping / 매핑). Nếu Kubernetes dịch vụ (service / 서비스) không có endpoint, xem label selector và readiness. Nếu endpoint có, kiểm tra pod có listen đúng cổng (port / 포트) bằng `ss -lntp` hoặc probe phù hợp. Nếu pod nhận yêu cầu (request / 요청) nhưng trả chậm, xem ứng dụng (application / 애플리케이션) dấu vết (trace / 추적)/log và downstream phụ thuộc (dependency / 의존성). Đây là cách giảm tìm kiếm (search / 검색) không gian (space / 공간) theo bằng chứng (evidence / 증거).

## 10. cấp cao (senior / 시니어) ghi chú (note / 노트): đường đi của yêu cầu (request path / 요청 경로) là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) có deadline

Một yêu cầu (request / 요청) synchronous là một chuỗi phụ thuộc (dependency / 의존성) về thời gian. Nếu yêu cầu (request / 요청) đi qua năm hop và mỗi hop dùng hết thời gian chờ (timeout / 타임아웃) 30 giây độc lập, worst-case hành vi (behavior / 동작) có thể vượt xa người dùng (user / 사용자) deadline. nền tảng (platform / 플랫폼) nên cung cấp convention về liên kết (connection / 연결) hết thời gian chờ (timeout / 타임아웃), yêu cầu (request / 요청) deadline, thử lại (retry / 재시도) và propagation của correlation/ngữ cảnh dấu vết (trace context / 추적 컨텍스트).

Khi topology thay đổi, mô hình tư duy (mental model / 사고 모델) vẫn giữ nguyên: xác định name resolution, liên kết (connection / 연결), định danh (identity / 식별자), routing, endpoint health, ứng dụng (application / 애플리케이션) hành vi (behavior / 동작) và downstream phụ thuộc (dependency / 의존성). công cụ (tool / 도구) chỉ giúp lấy bằng chứng (evidence / 증거) ở từng điểm.

## 11. liên kết (connection / 연결) cũng là tài nguyên hữu hạn ở phía máy khách (client / 클라이언트)

Mỗi TCP liên kết (connection / 연결) dùng socket/tệp (file / 파일) descriptor và thường chiếm một nguồn (source / 소스) cổng (port / 포트) tạm thời (ephemeral port). Khi ứng dụng (application / 애플리케이션) mở rất nhiều outbound liên kết (connection / 연결) ngắn sống, không reuse liên kết (connection / 연결) hoặc thử lại (retry / 재시도) storm, máy khách (client / 클라이언트)/NAT có thể hết cổng (port / 포트) khả dụng trước khi máy chủ (server / 서버) CPU cao.

Triệu chứng có thể là connect hết thời gian chờ (timeout / 타임아웃) hoặc lỗi mở liên kết (connection / 연결) trong khi DNS, máy chủ (server / 서버) listener và máy chủ (server / 서버) CPU đều bình thường. Vì vậy outbound thất bại (failure / 실패) cần nhìn cả client-side socket trạng thái (state / 상태), liên kết (connection / 연결) pool và NAT ranh giới (boundary / 경계), không chỉ máy chủ (server / 서버).

`TIME_WAIT` không tự động là bug; nó là phần của TCP vòng đời (lifecycle / 생명주기) giúp tránh packet cũ bị nhầm với liên kết (connection / 연결) mới. Nhưng liên kết (connection / 연결) churn cực lớn làm cổng (port / 포트)/socket trạng thái (state / 상태) tăng và trở thành sức chứa (capacity / 용량) concern. Reuse/pooling/keep-alive đúng cách thường tốt hơn chỉ tăng cổng (port / 포트) phạm vi (range / 범위).

## 12. NAT/conntrack có trạng thái (state / 상태) và có thể là bottleneck ẩn

Firewall/NAT/bộ cân bằng tải (load balancer / 로드 밸런서) thường giữ connection-tracking trạng thái (state / 상태). Một nút (node / 노드) hoặc gateway có thể hết conntrack bảng (table / 테이블)/translation sức chứa (capacity / 용량) dù ứng dụng (application / 애플리케이션) chỉ số (metric / 지표) bình thường. Khi đó packet mới bị drop hoặc liên kết (connection / 연결) setup thất bại không đồng đều.

Mẫu (pattern / 패턴) hay gặp là nhiều Pod cùng nút (node / 노드) gọi một bên ngoài (external / 외부) endpoint qua cùng NAT, hoặc thử lại (retry / 재시도) storm làm số liên kết (connection / 연결) mới tăng đột biến. bằng chứng (evidence / 증거) cần đi xuống nút (node / 노드)/gateway chỉ số (metric / 지표): active liên kết (connection / 연결), conntrack usage, SNAT cổng (port / 포트) allocation, packet drop.

Đây là ví dụ mạng (network / 네트워크) lớp trừu tượng (abstraction / 추상화) “rò”: dịch vụ (service / 서비스) chỉ thấy `connect timeout`, nhưng bottleneck nằm ở dùng chung (shared / 공유) mạng (network / 네트워크) trạng thái (state / 상태) bên dưới.

## 13. Long-lived liên kết (connection / 연결) làm DNS thay đổi (change / 변경) không có hiệu lực ngay

DNS TTL chỉ ảnh hưởng lần resolve. Nếu máy khách (client / 클라이언트) đã giữ HTTP keep-alive, HTTP/2 hoặc cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) lâu dài, nó có thể tiếp tục nói chuyện với endpoint cũ ngay cả khi DNS bộ nhớ đệm (cache / 캐시) đã hết hạn cho lookup mới.

Vì vậy di chuyển (migration / 마이그레이션) bằng DNS cần xét liên kết (connection / 연결) thời gian tồn tại (lifetime / 수명) và draining. “TTL đã xuống 30 giây nên sau 30 giây mọi traffic sang IP mới” là giả định sai nếu liên kết (connection / 연결) hiện tại sống hàng phút hoặc hàng giờ.

Khi thay bộ cân bằng tải (load balancer / 로드 밸런서)/cơ sở dữ liệu (database / 데이터베이스) endpoint, cần plan cho cả resolver bộ nhớ đệm (cache / 캐시) **và** liên kết (connection / 연결) pool vòng đời (lifecycle / 생명주기).

## 14. ngân sách thời gian chờ (timeout budget / 타임아웃 예산) phải tính cả thử lại (retry / 재시도) và hàng đợi (queue / 큐)

Giả sử người dùng (user / 사용자) deadline là 2 giây. dịch vụ (service / 서비스) A gọi B hết thời gian chờ (timeout / 타임아웃) 1,5 giây và thử lại (retry / 재시도) một lần. Nếu attempt đầu dùng hết 1,5 giây, attempt hai gần như không còn thời gian để hoàn thành trước người dùng (user / 사용자) deadline. Nếu B còn hàng đợi (queue / 큐) nội bộ, hết thời gian chờ (timeout / 타임아웃) ở A không biết công việc (work / 작업) đã bắt đầu hay chưa.

Thiết kế tốt truyền deadline hoặc tính remaining ngân sách (budget / 예산). Downstream hết thời gian chờ (timeout / 타임아웃) phải ngắn hơn remaining upstream deadline đủ để trả thất bại (failure / 실패) có kiểm soát. thử lại (retry / 재시도) chỉ được thực hiện nếu còn ngân sách (budget / 예산) và thao tác (operation / 연산) an toàn.

Hết thời gian chờ (timeout / 타임아웃) không nên được chọn độc lập từng nhóm (team / 팀). Nó là một đặc tả hợp đồng (contract / 계약) xuyên lời gọi (call / 호출) đồ thị (graph / 그래프).

## 15. thử lại (retry / 재시도) multiplication giữa nhiều tầng (layer / 계층)

Nếu máy khách (client / 클라이언트) thử lại (retry / 재시도) 3 lần, proxy thử lại (retry / 재시도) 2 lần và ứng dụng (application / 애플리케이션) SDK thử lại (retry / 재시도) 3 lần, một người dùng (user / 사용자) yêu cầu (request / 요청) có thể tạo số attempt downstream lớn hơn rất nhiều so với ý định của từng tầng (layer / 계층). Không phải lúc nào cũng đạt tích số tối đa vì hết thời gian chờ (timeout / 타임아웃)/deadline, nhưng rủi ro (risk / 위험) amplification là thật.

Vì vậy nền tảng (platform / 플랫폼) cần convention “tầng (layer / 계층) nào sở hữu thử lại (retry / 재시도)”. Proxy có thể thử lại (retry / 재시도) connect thất bại (failure / 실패) cho idempotent yêu cầu (request / 요청); ứng dụng (application / 애플리케이션) có lĩnh vực (domain / 도메인) ngữ cảnh (context / 맥락) để biết thao tác (operation / 연산) nào safe. Không nên bật thử lại (retry / 재시도) mặc định ở mọi tầng (layer / 계층) mà không nhìn toàn đường dẫn (path / 경로).

## 16. 502, 503 và 504 chỉ là clue theo vị trí phát sinh

Mã lỗi từ proxy thường gợi tầng (layer / 계층) nhưng không phải universal truth. `502` thường nghĩa proxy không nhận phản hồi (response / 응답) hợp lệ từ upstream; `503` có thể không có backend ready/overload; `504` thường là upstream hết thời gian chờ (timeout / 타임아웃). hiện thực (implementation / 구현) cụ thể có thể khác.

Do đó luôn xác định **ai phát status** bằng phản hồi (response / 응답) header/truy cập (access / 접근) log rồi mới suy luận. Một ứng dụng (application / 애플리케이션) cũng có thể tự trả 503; nhìn status mã (code / 코드) mà không biết emitter dễ đi sai tầng (layer / 계층).

## 17. cấp cao (senior / 시니어) walkthrough: chỉ một số Pod không gọi được bên ngoài (external / 외부) API

Giả sử 30% Pod hết thời gian chờ (timeout / 타임아웃) khi gọi bên ngoài (external / 외부) payment API, máy chủ (server / 서버) payment không thấy yêu cầu (request / 요청) tương ứng. DNS giống nhau, Pod CPU/bộ nhớ (memory / 메모리) bình thường. Nếu các Pod lỗi tập trung trên vài nút (node / 노드), hypothesis chuyển sang nút (node / 노드)/mạng (network / 네트워크) ranh giới (boundary / 경계).

Kiểm tra nút (node / 노드) NAT/conntrack/SNAT cổng (port / 포트), CNI/chính sách mạng (network policy / 네트워크 정책) và outbound tuyến (route / 경로). Nếu conntrack gần đầy hoặc SNAT allocation cạn đúng trên nút (node / 노드) lỗi, quy mô (scale / 규모) thêm Pod vào cùng nút (node / 노드) có thể làm tệ hơn. Mitigation có thể phân tán tải công việc (workload / 워크로드)/nút (node / 노드), giảm liên kết (connection / 연결) churn/thử lại (retry / 재시도) hoặc tăng gateway sức chứa (capacity / 용량) tùy kiến trúc (architecture / 아키텍처).

Chuỗi nhân quả (causal chain / 인과 사슬) quan trọng: partial thất bại (failure / 실패) theo nút (node / 노드) là dimension giúp giảm tìm kiếm (search / 검색) không gian (space / 공간) từ “bên ngoài (external / 외부) API không ổn” xuống “dùng chung (shared / 공유) egress trạng thái (state / 상태) trên subset nút (node / 노드)”.

## 18. Negative DNS bộ nhớ đệm (cache / 캐시) có thể kéo dài thất bại (failure / 실패) sau khi bản ghi (record / 레코드) đã được sửa

Bộ nhớ đệm (cache / 캐시) không chỉ lưu câu trả lời thành công. Resolver/thời gian chạy (runtime / 런타임) cũng có thể bộ nhớ đệm (cache / 캐시) kết quả âm như `NXDOMAIN` hoặc lookup thất bại (failure / 실패) trong một khoảng thời gian. Vì vậy một hostname vừa được tạo hoặc vừa sửa có thể vẫn thất bại (fail / 실패) trên một số máy khách (client / 클라이언트) dù authoritative DNS hiện đã đúng.

Trong sự cố (incident / 인시던트) di chuyển (migration / 마이그레이션), cần hỏi máy khách (client / 클라이언트) nào đã lookup vào thời điểm bản ghi (record / 레코드) chưa tồn tại và thời gian chạy (runtime / 런타임) đó giữ negative kết quả (result / 결과) bao lâu. Restart tiến trình (process / 프로세스) đôi khi “sửa” vì xóa bộ nhớ đệm (cache / 캐시) cục bộ, nhưng đó chỉ là observation. Long-term fix là hiểu resolver/bộ nhớ đệm (cache / 캐시) đặc tả hợp đồng (contract / 계약), chuẩn bị bản ghi (record / 레코드) trước cutover và tránh giả định mọi máy khách (client / 클라이언트) re-query ngay.

DNS debugging trưởng thành luôn xác định **resolver đường dẫn (path / 경로) + bộ nhớ đệm (cache / 캐시) thời gian tồn tại (lifetime / 수명) + liên kết (connection / 연결) thời gian tồn tại (lifetime / 수명)**, không chỉ chạy một `dig` từ laptop operator.

## 19. liên kết (connection / 연결) pool có hàng đợi (queue / 큐) riêng và có thể che mạng (network / 네트워크) khỏe

Ứng dụng (application / 애플리케이션) thường không mở socket mới cho mỗi yêu cầu (request / 요청) mà mượn liên kết (connection / 연결) từ pool. Khi pool đã dùng hết, yêu cầu (request / 요청) có thể chờ trong pool hàng đợi (queue / 큐) trước khi bất kỳ packet nào được gửi đi. Từ góc nhìn máy chủ (server / 서버) downstream, không có traffic; từ góc nhìn người dùng (user / 사용자), yêu cầu (request / 요청) vẫn hết thời gian chờ (timeout / 타임아웃).

Do đó cần tách `pool wait time`, `connect time`, TLS thời gian (time / 시간) và yêu cầu (request / 요청)/dịch vụ (service / 서비스) thời gian (time / 시간). Nếu pool wait tăng nhưng connect/yêu cầu (request / 요청) độ trễ (latency / 지연 시간) của liên kết (connection / 연결) đã mượn vẫn bình thường, bottleneck nằm ở client-side tính đồng thời (concurrency / 동시성)/pool sizing hoặc liên kết (connection / 연결) leak, không nằm ở mạng (network / 네트워크) đường dẫn (path / 경로).

Tăng pool kích thước (size / 크기) không luôn là fix. Pool lớn hơn làm tăng tính đồng thời (concurrency / 동시성) downstream và có thể đẩy cơ sở dữ liệu (database / 데이터베이스)/API vào saturation. liên kết (connection / 연결) pool là một admission-control ranh giới (boundary / 경계) nhỏ; sizing phải gắn với downstream ngân sách (budget / 예산).

## 20. MTU mismatch có thể tạo “kết nối được nhưng yêu cầu (request / 요청) lớn bị treo”

Đường mạng có giới hạn kích thước packet tối đa theo từng hop. Nếu đường dẫn (path / 경로) MTU Discovery hoạt động không đúng hoặc ICMP cần thiết bị chặn, packet lớn có thể bị drop trong khi packet nhỏ vẫn đi được. Triệu chứng điển hình là TCP connect/TLS ban đầu có vẻ ổn nhưng upload, phản hồi (response / 응답) lớn hoặc một số giao thức (protocol / 프로토콜) message lại hết thời gian chờ (timeout / 타임아웃).

Thất bại (failure / 실패) này dễ bị hiểu nhầm thành ứng dụng (application / 애플리케이션) bug vì health check nhỏ vẫn xanh. bằng chứng (evidence / 증거) cần so yêu cầu (request / 요청) nhỏ/lớn, packet retransmission và MTU trên overlay/VPN/tunnel đường dẫn (path / 경로). Trong môi trường bộ chứa (container / 컨테이너)/VXLAN/WireGuard, encapsulation làm effective MTU nhỏ hơn vật lý (physical / 물리적) mạng (network / 네트워크).

Không nên “fix” bằng hạ MTU ngẫu nhiên toàn hệ thống. Mục tiêu là tìm ranh giới (boundary / 경계) nào làm packet vượt effective đường dẫn (path / 경로) MTU và cấu hình endpoint/tunnel nhất quán.

## 21. HTTP/2 multiplexing giảm liên kết (connection / 연결) count nhưng tạo thất bại (failure / 실패) phạm vi (scope / 범위) khác

Với HTTP/1.1, nhiều máy khách (client / 클라이언트) thường dùng pool nhiều liên kết (connection / 연결) để song song yêu cầu (request / 요청). HTTP/2 cho phép nhiều stream multiplex trên một liên kết (connection / 연결). Điều này giảm liên kết (connection / 연결) churn nhưng làm một liên kết (connection / 연결) trở thành dùng chung (shared / 공유) vận chuyển (transport / 전송) cho nhiều yêu cầu (request / 요청).

Nếu liên kết (connection / 연결) HTTP/2 gặp packet mất mát (loss / 손실), GOAWAY, flow-control hoặc proxy reset, nhiều stream có thể bị ảnh hưởng cùng lúc. Vì vậy chỉ số (metric / 지표) “chỉ có vài liên kết (connection / 연결)” không có nghĩa blast radius nhỏ. Cần quan sát stream/yêu cầu (request / 요청) lỗi (error / 오류) cùng liên kết (connection / 연결) vòng đời (lifecycle / 생명주기).

Nền tảng (platform / 플랫폼) không cần buộc mọi nhóm (team / 팀) hiểu frame giao thức (protocol / 프로토콜) chi tiết, nhưng phải tránh giả định (assumption / 가정) `1 connection = 1 request`. sức chứa (capacity / 용량) và thất bại (failure / 실패) lập luận (reasoning / 추론) phải theo giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론) thực tế.

## 22. bộ cân bằng tải (load balancer / 로드 밸런서) health là một observation có độ trễ

Backend có thể vừa thất bại (fail / 실패) nhưng bộ cân bằng tải (load balancer / 로드 밸런서) chưa mark unhealthy cho tới vài lần probe; hoặc backend vừa hồi nhưng chưa được đưa lại vào pool. Trong cửa sổ đó, một phần traffic có thể vẫn đi sai nơi hoặc sức chứa (capacity / 용량) thực thấp hơn dashboard ứng dụng (application / 애플리케이션) nghĩ.

Health-check interval, unhealthy/healthy threshold, liên kết (connection / 연결) draining và endpoint propagation tạo một vòng điều khiển (control loop / 제어 루프) riêng. Nếu rollout đổi hàng loạt backend nhanh hơn health hệ thống (system / 시스템) hội tụ, transient 5xx có thể xuất hiện dù từng tiến trình (process / 프로세스) shutdown “đúng”.

Khi điều tra, overlay backend vòng đời (lifecycle / 생명주기) với health-state chuyển tiếp (transition / 전이) và routing bằng chứng (evidence / 증거). “Pod Ready” và “bộ cân bằng tải (load balancer / 로드 밸런서) đã tuyến (route / 경로) ổn định” là hai trạng thái (state / 상태) khác nhau.

## 23. cấp cao (senior / 시니어) walkthrough: health check xanh nhưng upload tệp (file / 파일) lớn hết thời gian chờ (timeout / 타임아웃)

Giả sử GET `/health` và yêu cầu (request / 요청) JSON nhỏ đều thành công, nhưng upload trên 2 MiB treo qua VPN/overlay đường dẫn (path / 경로). máy chủ (server / 서버) ứng dụng (application / 애플리케이션) không thấy yêu cầu (request / 요청) hoàn chỉnh, CPU và pool bình thường. Đây là clue rằng thất bại (failure / 실패) phụ thuộc packet kích thước (size / 크기)/đường dẫn (path / 경로) chứ không phụ thuộc lô-gic nghiệp vụ (business logic / 비즈니스 로직).

So sánh direct đường dẫn (path / 경로) với tunneled đường dẫn (path / 경로), kiểm tra retransmission và effective MTU. Nếu tunnel thêm encapsulation làm packet lớn bị black-hole trong khi ICMP phản hồi (feedback / 피드백) bị chặn, health check nhỏ sẽ không phát hiện.

Bài học là synthetic check chỉ chứng minh đúng tải công việc (workload / 워크로드) mà nó thực sự phát. môi trường vận hành (production / 운영 환경) xác minh (verification / 확인) phải đại diện đủ các thuộc tính (property / 속성) quan trọng của đường đi của yêu cầu (request path / 요청 경로): kích thước (size / 크기), giao thức (protocol / 프로토콜), định danh (identity / 식별자), tuyến (route / 경로) và deadline.

## 24. Circuit breaker là admission điều khiển (control / 제어) theo phụ thuộc (dependency / 의존성) trạng thái (state / 상태), không phải cơ chế chữa phụ thuộc (dependency / 의존성)

Khi một phụ thuộc (dependency / 의존성) đang hết thời gian chờ (timeout / 타임아웃) hàng loạt, tiếp tục cho mọi yêu cầu (request / 요청) chờ hết hết thời gian chờ (timeout / 타임아웃) vừa giữ luồng thực thi (thread / 스레드)/liên kết (connection / 연결) vừa làm downstream nhận thêm tải (load / 로드). Circuit breaker có thể tạm ngừng gửi một lớp (class / 클래스) yêu cầu (request / 요청) sau khi thất bại (failure / 실패) vượt điều kiện, trả lỗi/fallback sớm rồi cho một lượng probe nhỏ kiểm tra khả năng hồi phục.

Giá trị của breaker nằm ở việc **giới hạn công việc (work / 작업) vô ích và bảo vệ caller**, không nằm ở việc làm downstream khỏe lại. Threshold quá nhạy có thể mở breaker vì một burst ngắn; threshold quá chậm thì tài nguyên (resource / 자원) caller đã cạn trước khi breaker hành động. `half-open` cũng là một khôi phục (recovery / 복구) experiment: probe phải đủ nhỏ để không tạo khôi phục (recovery / 복구) storm nhưng đủ đại diện để quyết định đóng breaker.

Breaker cần được đặt ở ranh giới (boundary / 경계) có ngữ nghĩa (semantics / 의미론) đúng. Nếu proxy breaker theo HTTP 5xx nhưng ứng dụng (application / 애플리케이션) trả HTTP 200 cho nghiệp vụ (business / 비즈니스) thất bại (failure / 실패), tín hiệu (signal / 신호) sai. Nếu mỗi instance tự breaker nhưng phụ thuộc (dependency / 의존성) thất bại (failure / 실패) chỉ ảnh hưởng một region, aggregate dashboard có thể che trạng thái (state / 상태) phân mảnh. Vì vậy breaker trạng thái (state / 상태), rejected yêu cầu (request / 요청) và probe kết quả (outcome / 결과) nên observable theo phụ thuộc (dependency / 의존성)/cohort.

## 25. Bulkhead giới hạn blast radius của một phụ thuộc (dependency / 의존성) hoặc tải công việc (workload / 워크로드) lớp (class / 클래스)

Một dịch vụ (service / 서비스) có thể gọi payment, recommendation và email. Nếu tất cả outbound lời gọi (call / 호출) dùng chung luồng thực thi (thread / 스레드) pool/liên kết (connection / 연결) ngân sách (budget / 예산), email provider treo có thể chiếm hết tài nguyên (resource / 자원) và làm payment cũng thất bại (fail / 실패) dù payment phụ thuộc (dependency / 의존성) khỏe. **Bulkhead** tách tính đồng thời (concurrency / 동시성)/tài nguyên (resource / 자원) pool theo miền lỗi (failure domain / 장애 도메인) để một phụ thuộc (dependency / 의존성) không tiêu hết sức chứa (capacity / 용량) của caller.

Isolation không miễn phí: pool quá nhỏ làm utilization kém hoặc tạo hàng đợi (queue / 큐) cục bộ; pool quá lớn lại không còn bảo vệ. Sizing nên dựa trên criticality, expected tính đồng thời (concurrency / 동시성), hết thời gian chờ (timeout / 타임아웃) và downstream sức chứa (capacity / 용량). Với asynchronous hệ thống (system / 시스템), partition hàng đợi (queue / 큐)/bên tiêu thụ (consumer / 소비자) tính đồng thời (concurrency / 동시성) có vai trò tương tự.

Mô hình tư duy (mental model / 사고 모델) là `shared caller resource → partition theo failure class → admission riêng → graceful degradation`. Đây là liên kết (connection / 연결) trực tiếp giữa networking, SRE overload điều khiển (control / 제어) và multi-tenancy fairness.

## 26. Hedged yêu cầu (request / 요청) đổi tail độ trễ (latency / 지연 시간) lấy tải (load / 로드) và duplicate-work rủi ro (risk / 위험)

Một kỹ thuật giảm tail độ trễ (latency / 지연 시간) là gửi yêu cầu (request / 요청) thứ hai khi attempt đầu chậm bất thường, rồi dùng phản hồi (response / 응답) đến trước. Cách này có thể hữu ích với read idempotent trên replicated backend khi tail chủ yếu do straggler, nhưng nó **chủ động tăng tải (load / 로드) đúng lúc yêu cầu (request / 요청) chậm**.

Nếu threshold quá thấp hoặc backend đang saturation, hedging khuếch đại outage giống thử lại (retry / 재시도) storm. Với ghi (write / 쓰기)/side tác động (effect / 효과), duplicate thực thi (execution / 실행) còn nguy hiểm hơn nếu không có idempotency. Vì vậy hedging chỉ nên xuất hiện sau khi đã hiểu độ trễ (latency / 지연 시간) phân phối (distribution / 분포), remaining deadline, idempotency và spare sức chứa (capacity / 용량); không phải default thử lại (retry / 재시도) “thông minh hơn”.

Bằng chứng (evidence / 증거) cần tách original attempt, hedge attempt, winner, cancellation success và extra downstream công việc (work / 작업). Nếu yêu cầu (request / 요청) thứ hai thắng nhưng attempt đầu không được cancel và vẫn chạy tới cuối, người dùng (user / 사용자) độ trễ (latency / 지연 시간) giảm nhưng hệ thống (system / 시스템) chi phí (cost / 비용)/tính đồng thời (concurrency / 동시성) có thể tăng đáng kể.

## 27. Draining phải bao phủ cả routing trạng thái (state / 상태) và liên kết (connection / 연결) trạng thái (state / 상태)

Khi backend rời pool để deploy hoặc failover, ngừng gửi **liên kết (connection / 연결) mới** chưa đủ nếu máy khách (client / 클라이언트)/proxy đang giữ keep-alive hoặc HTTP/2 liên kết (connection / 연결) cũ. Ngược lại đóng liên kết (connection / 연결) ngay có thể reset in-flight yêu cầu (request / 요청). Safe draining là giao thức (protocol / 프로토콜) giữa endpoint vòng đời (lifecycle / 생명주기), load-balancer routing và liên kết (connection / 연결) thời gian tồn tại (lifetime / 수명).

Một chuỗi (sequence / 시퀀스) thường mong muốn là: endpoint ngừng nhận công việc (work / 작업) mới, routing trạng thái (state / 상태) hội tụ, existing liên kết (connection / 연결)/in-flight công việc (work / 작업) có grace period, rồi tiến trình (process / 프로세스) mới đóng listener và thoát. Với long-lived stream/WebSocket, đặc tả hợp đồng (contract / 계약) cần rõ có cho phép sống tới hết session, gửi reconnect tín hiệu (signal / 신호) hay cưỡng bức close sau deadline.

Bằng chứng vận hành (production evidence / 운영 증거) nên nối `readiness/drain state → endpoint membership → active connection/stream → process termination`. Nếu chỉ nhìn Pod termination timestamp, ta có thể bỏ lỡ việc proxy vẫn reuse liên kết (connection / 연결) cũ hoặc máy khách (client / 클라이언트) reconnect storm sau cutover.

## 28. Egress nguồn (source / 소스) định danh (identity / 식별자) vừa là bảo mật (security / 보안) đặc tả hợp đồng (contract / 계약) vừa là sức chứa (capacity / 용량) đặc tả hợp đồng (contract / 계약)

Nhiều hệ thống bên ngoài allowlist theo nguồn (source / 소스) IP, trong khi tải công việc (workload / 워크로드) nội bộ có thể đi qua nút (node / 노드) SNAT, NAT gateway hoặc egress proxy. Vì vậy “IP của dịch vụ (service / 서비스)” thường không phải thuộc tính cố định của Pod mà là kết quả của egress topology. Nếu autoscaling hoặc failover chuyển tải công việc (workload / 워크로드) sang một NAT pool khác, yêu cầu (request / 요청) có thể bị từ chối dù ứng dụng (application / 애플리케이션) và DNS đều khỏe.

Cùng một nguồn (source / 소스) IP còn có sức chứa (capacity / 용량) hữu hạn cho translation/ánh xạ cổng (port mapping / 포트 매핑). Gom hàng nghìn tải công việc (workload / 워크로드) qua một vài egress address giúp chính sách (policy / 정책) đơn giản nhưng tạo dùng chung (shared / 공유) miền lỗi (failure domain / 장애 도메인). Mở thêm nguồn (source / 소스) IP có thể tăng sức chứa (capacity / 용량), nhưng lại thay đổi allowlist/kiểm tra (audit / 감사) đặc tả hợp đồng (contract / 계약) với phụ thuộc (dependency / 의존성) bên ngoài.

Nền tảng (platform / 플랫폼) cần coi egress định danh (identity / 식별자) như năng lực (capability / 역량) được quản lý: tải công việc (workload / 워크로드) nào dùng pool nào, destination nào yêu cầu stable định danh (identity / 식별자), sức chứa (capacity / 용량)/cổng (port / 포트) utilization ra sao và failover có giữ cùng chính sách (policy / 정책) đặc tả hợp đồng (contract / 계약) không. bảo mật (security / 보안) và networking gặp nhau ở cùng một ranh giới (boundary / 경계).

## 29. DNS bộ nhớ đệm (cache / 캐시) stampede có thể biến TTL expiry thành traffic burst

Bộ nhớ đệm (cache / 캐시) giảm tải resolver, nhưng nếu rất nhiều tiến trình (process / 프로세스) nhận cùng TTL và cùng hết hạn gần một thời điểm, chúng có thể đồng loạt truy vấn (query / 쿼리) lại. Khi autoscaling tạo hàng nghìn instance hoặc bản ghi (record / 레코드) có TTL quá thấp, resolver/authoritative DNS có thể nhận burst lớn dù yêu cầu (request / 요청) tỷ lệ (rate / 비율) nghiệp vụ (business / 비즈니스) không đổi.

Thất bại (failure / 실패) chuỗi (chain / 사슬) có thể là `TTL expiry → synchronized lookup → resolver saturation → lookup latency/failure → application retry → resolver load tăng thêm`. Vì vậy giảm TTL không phải luôn làm di chuyển (migration / 마이그레이션) “an toàn hơn”; nó đổi freshness lấy truy vấn (query / 쿼리) tải (load / 로드) và làm vòng điều khiển (control loop / 제어 루프) nhạy hơn.

Bằng chứng (evidence / 증거) cần tách bộ nhớ đệm (cache / 캐시) hit/miss, truy vấn (query / 쿼리) tỷ lệ (rate / 비율), resolver độ trễ (latency / 지연 시간)/lỗi (error / 오류) và ứng dụng (application / 애플리케이션) thử lại (retry / 재시도). Cơ chế giảm burst có thể gồm bộ nhớ đệm (cache / 캐시) hierarchy, prefetch/refresh phù hợp, jitter ở refresh đường dẫn (path / 경로) hoặc sức chứa (capacity / 용량) resolver đủ cho miss storm. Mục tiêu là tránh đồng bộ hóa máy khách (client / 클라이언트) quanh cùng một expiry ranh giới (boundary / 경계).

## 30. TCP listen hàng đợi (queue / 큐) và accept hàng đợi (queue / 큐) tạo saturation trước khi nghiệp vụ (business / 비즈니스) handler chạy

Một tiến trình (process / 프로세스) có thể đang listen trên cổng (port / 포트) nhưng chưa chắc nhận liên kết (connection / 연결) mới kịp. Kernel giữ trạng thái (state / 상태) cho liên kết (connection / 연결) đang handshake và liên kết (connection / 연결) đã hoàn tất handshake nhưng chưa được ứng dụng (application / 애플리케이션) `accept()`. Khi hàng đợi (queue / 큐) tương ứng đầy, máy khách (client / 클라이언트) có thể thấy connect độ trễ (latency / 지연 시간), retransmission hoặc hết thời gian chờ (timeout / 타임아웃) trước khi yêu cầu (request / 요청) chạm ứng dụng (application / 애플리케이션) handler.

Điều này giải thích trường hợp health chỉ số (metric / 지표) nghiệp vụ (business / 비즈니스) nhìn bình thường nhưng liên kết (connection / 연결) setup xấu dưới burst. CPU trung bình thấp cũng không loại trừ accept bottleneck nếu vòng lặp sự kiện (event loop / 이벤트 루프)/luồng thực thi (thread / 스레드) accept bị khối (block / 블록) hoặc hàng đợi (queue / 큐) limit quá nhỏ so với burst shape.

Bằng chứng (evidence / 증거) nên nối SYN/retransmission, listen/accept hàng đợi (queue / 큐), socket trạng thái (state / 상태), tiến trình (process / 프로세스) scheduling và yêu cầu (request / 요청) arrival ở ứng dụng (application / 애플리케이션). Tăng backlog mù quáng chỉ dời hàng đợi (queue / 큐) sang kernel; nếu ứng dụng (application / 애플리케이션) không drain đủ nhanh, độ trễ (latency / 지연 시간) vẫn tích lũy. Fix phải nhắm vào dịch vụ (service / 서비스) tỷ lệ (rate / 비율), admission hoặc burst absorption phù hợp.

## 31. liên kết (connection / 연결) ngân sách (budget / 예산) có thể lập luận (reasoning / 추론) bằng arrival tỷ lệ (rate / 비율) và holding thời gian (time / 시간)

Số liên kết (connection / 연결) đồng thời không chỉ phụ thuộc yêu cầu (request / 요청) tỷ lệ (rate / 비율). Theo intuition của Little's Law, tính đồng thời (concurrency / 동시성) xấp xỉ arrival tỷ lệ (rate / 비율) nhân thời gian mỗi đơn vị (unit / 단위) giữ tài nguyên (resource / 자원). Nếu dịch vụ (service / 서비스) gọi phụ thuộc (dependency / 의존성) 2.000 lần/giây và mỗi lời gọi (call / 호출) giữ liên kết (connection / 연결) trung bình 100 ms, order-of-magnitude tính đồng thời (concurrency / 동시성) đã khoảng 200 trước thử lại (retry / 재시도), tail độ trễ (latency / 지연 시간) hoặc pool wait.

Khi độ trễ (latency / 지연 시간) tăng từ 100 ms lên 1 giây mà arrival tỷ lệ (rate / 비율) giữ nguyên, số công việc (work / 작업)/liên kết (connection / 연결) cần giữ có thể tăng khoảng mười lần. Đây là lý do downstream chậm có thể làm caller cạn socket/luồng thực thi (thread / 스레드)/pool dù traffic người dùng (user / 사용자) không tăng. thử lại (retry / 재시도) còn tăng effective arrival tỷ lệ (rate / 비율), tạo phản hồi (feedback / 피드백) dương.

Sức chứa (capacity / 용량) planning nên có ngân sách (budget / 예산) cho pool, tệp (file / 파일) descriptor, ephemeral/SNAT cổng (port / 포트), conntrack và downstream tính đồng thời (concurrency / 동시성) thay vì chỉ nhìn bandwidth. Một mạng (network / 네트워크) đường dẫn (path / 경로) có băng thông dư vẫn có thể chết vì stateful tài nguyên (resource / 자원) exhaustion.

## 32. Keep-alive stale liên kết (connection / 연결) tạo thất bại (failure / 실패) sau cutover dù DNS đã đúng

Liên kết (connection / 연결) reuse giảm handshake chi phí (cost / 비용) nhưng giữ trạng thái (state / 상태) lâu hơn topology. Sau failover hoặc endpoint replacement, pool có thể chứa liên kết (connection / 연결) tới backend cũ, half-closed socket hoặc đường dẫn (path / 경로) đã không còn hợp lệ. yêu cầu (request / 요청) đầu tiên reuse liên kết (connection / 연결) stale có thể thất bại (fail / 실패) rồi yêu cầu (request / 요청) sau mới reconnect thành công, tạo mẫu (pattern / 패턴) lỗi rải rác khó thấy.

Pool cần vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약): idle hết thời gian chờ (timeout / 타임아웃), max liên kết (connection / 연결) age khi cần, kiểm tra hợp lệ (validation / 검증)/thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론) và hành vi (behavior / 동작) khi nhận GOAWAY/RST. hết thời gian chờ (timeout / 타임아웃) quá ngắn làm liên kết (connection / 연결) churn/SNAT pressure; quá dài làm cutover/draining chậm và giữ stale trạng thái (state / 상태) lâu.

Vì vậy tuning keep-alive phải nối ba mục tiêu: giảm setup chi phí (cost / 비용), giới hạn tài nguyên (resource / 자원) churn và bảo đảm topology thay đổi (change / 변경) hội tụ trong thời gian chấp nhận được.

## 33. mạng (network / 네트워크) bằng chứng (evidence / 증거) phải được đọc theo tầng (layer / 계층) và theo cohort

Một dashboard aggregate có thể nói lỗi (error / 오류) 5%, nhưng 5% đó có thể tập trung ở một nút (node / 노드), một NAT gateway, một resolver, một AZ, một giao thức (protocol / 프로토콜) phiên bản (version / 버전) hoặc một destination IP. Dimension đúng thường quan trọng hơn thêm chỉ số (metric / 지표) mới.

Khi gỡ lỗi (debug / 디버그), nên xây bằng chứng (evidence / 증거) chuỗi (chain / 사슬) theo thứ tự `resolve → connect → TLS → route → pool/queue → application → dependency`, rồi chia theo cohort như nút (node / 노드)/AZ/nguồn (source / 소스) IP/destination/revision. Packet-level bằng chứng (evidence / 증거) hữu ích khi cần chứng minh handshake/retransmission; proxy/truy cập (access / 접근) log hữu ích để xác định emitter/routing; dấu vết (trace / 추적) giúp nối ứng dụng (application / 애플리케이션) phụ thuộc (dependency / 의존성). Không tầng (layer / 계층) nào một mình là “nguồn chuẩn (source of truth / 정본)” cho toàn đường đi của yêu cầu (request path / 요청 경로).

Operational implication là instrumentation phải giữ đủ định danh (identity / 식별자) để correlate các perspective. Nếu NAT log chỉ có translated tuple còn ứng dụng (application / 애플리케이션) log chỉ có yêu cầu (request / 요청) ID mà không có cách nối chúng, sự cố (incident / 인시던트) sẽ tốn thời gian ở bước chứng minh hai observation thuộc cùng luồng (flow / 흐름).

## 34. cấp cao (senior / 시니어) walkthrough: autoscale làm bên ngoài (external / 외부) API lỗi dù máy chủ (server / 서버) bên ngoài khỏe

Giả sử traffic tăng làm dịch vụ (service / 서비스) từ 50 lên 300 Pod. Ngay sau scale-out, outbound lời gọi (call / 호출) tới một partner bắt đầu hết thời gian chờ (timeout / 타임아웃)/403 theo từng nhóm Pod; partner báo backend khỏe. Nếu Pod mới nằm ở nút (node / 노드)/egress pool khác, hai hypothesis cần kiểm tra song song: nguồn (source / 소스) IP mới chưa nằm trong allowlist và dùng chung (shared / 공유) NAT/SNAT sức chứa (capacity / 용량) đã cạn do liên kết (connection / 연결) churn lúc scale-out.

Đừng chỉ tăng replica thêm vì chính scale-out có thể tăng liên kết (connection / 연결) creation và fan-out qua cùng gateway. Hãy group thất bại (failure / 실패) theo nút (node / 노드)/nguồn (source / 소스) egress IP, kiểm tra partner truy cập (access / 접근) log, SNAT/conntrack utilization, liên kết (connection / 연결) reuse và effective thử lại (retry / 재시도) tỷ lệ (rate / 비율). Nếu 403 chỉ theo nguồn (source / 소스) IP mới, đó là định danh (identity / 식별자)/chính sách (policy / 정책) mismatch; nếu connect hết thời gian chờ (timeout / 타임아웃) tăng cùng cổng (port / 포트) allocation saturation, đó là sức chứa (capacity / 용량) thất bại (failure / 실패); hai thất bại (failure / 실패) còn có thể xảy ra đồng thời.

Mô hình tư duy (mental model / 사고 모델) cuối cùng là **mạng (network / 네트워크) đường dẫn (path / 경로) có cả định danh (identity / 식별자), trạng thái (state / 상태) và hàng đợi (queue / 큐)**. Reachability nhị phân không đủ để lập luận (reasoning / 추론) môi trường vận hành (production / 운영 환경): một luồng (flow / 흐름) phải có đúng name, tuyến (route / 경로), authority, liên kết (connection / 연결) trạng thái (state / 상태), sức chứa (capacity / 용량) và deadline xuyên suốt đường đi.

> **Bàn giao:** Sau **34. cấp cao (senior / 시니어) walkthrough: autoscale làm bên ngoài (external / 외부) API lỗi dù máy chủ (server / 서버) bên ngoài khỏe**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 linux execution and service model](./00_linux_execution_and_service_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
