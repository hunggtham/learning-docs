# Thời gian, đồng hồ, thứ tự và quan hệ nhân quả trong hệ thống phân tán

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thời gian, đồng hồ, thứ tự và quan hệ nhân quả trong hệ thống phân tán**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Đồng hồ vật lý không hoàn hảo** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Wall clock và monotonic clock** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối time, clocks, ordering và causality, để hệ phân tán biết sự kiện nào có thể được so sánh và suy ra.

Trong một chương trình chạy trên một máy, lập trình viên thường có trực giác rằng “A xảy ra trước B” nếu A xuất hiện trước trong luồng lệnh hoặc đồng hồ hệ thống cho số nhỏ hơn. Trong hệ thống phân tán, trực giác đó trở nên nguy hiểm. Hai máy có đồng hồ vật lý khác nhau, message có thể trễ hoặc đi đường khác nhau, và không tồn tại một quan sát viên trung tâm luôn biết chính xác thứ tự toàn cục của mọi sự kiện.

Chapter này giải thích vì sao **thời gian vật lý (physical time)**, **thứ tự lô-gic (logic / 논리) (logical ordering)** và **quan hệ nhân quả (causality / 인과성)** là ba khái niệm khác nhau, đồng thời chỉ ra chúng ảnh hưởng thế nào đến replication, consensus, lease, giải quyết xung đột (conflict resolution / 충돌 해결) và khả năng quan sát (observability / 관측 가능성).

## 1. Đồng hồ vật lý không hoàn hảo

Mỗi máy có oscillator riêng. Tốc độ của oscillator có sai số nên hai clock có thể **trôi (clock drift)** theo thời gian. Hệ thống đồng bộ thời gian như NTP hoặc PTP giúp giảm sai lệch nhưng không biến clock thành nguồn sự thật tuyệt đối.

Ta cần phân biệt:

- **clock offset**: hai clock đang lệch nhau bao nhiêu tại một thời điểm;
- **clock drift**: tốc độ clock chạy nhanh/chậm tương đối theo thời gian;
- **clock bất định (uncertainty / 불확실성)**: khoảng mà hệ thống không thể biết thời gian thật chính xác hơn.

Nếu máy chủ (server / 서버) A báo `12:00:00.100` và máy chủ (server / 서버) B báo `12:00:00.090`, không thể tự động kết luận sự kiện (event / 이벤트) ở B xảy ra trước sự kiện (event / 이벤트) ở A nếu clock offset chưa được kiểm soát đủ chặt.

> **Nối mạch:** Physical clocks drift và jump; wall clock phục vụ timestamp, monotonic clock phục vụ duration, còn happened-before biểu diễn causality khi không có global order.

## 2. Wall clock và monotonic clock

**Đồng hồ lịch (wall clock)** cố gắng biểu diễn thời gian thực như ngày/giờ. Nó có thể bị điều chỉnh khi NTP sửa clock hoặc người quản trị thay đổi thời gian.

**Đồng hồ đơn điệu (monotonic clock)** chỉ tăng theo một chiều và phù hợp để đo duration:

```text
start = monotonic_now()
...
elapsed = monotonic_now() - start
```

Hết thời gian chờ (timeout / 타임아웃), độ trễ (latency / 지연 시간) và interval nên dựa vào monotonic clock nếu thời gian chạy (runtime / 런타임) hỗ trợ. Dùng wall clock để đo hết thời gian chờ (timeout / 타임아웃) có thể gây lỗi nếu thời gian hệ thống nhảy lùi hoặc tiến.

> **Nối mạch:** **3. “Happened-before” là quan hệ lô-gic (logic / 논리)** nối từ **2. Wall clock và monotonic clock** sang **4. Lamport clock**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. “Happened-before” là quan hệ lô-gic (logic / 논리)

Lamport đưa ra quan hệ **xảy ra trước (happened-before, →)** dựa trên ba quy tắc trực giác:

1. trong cùng một tiến trình (process / 프로세스), sự kiện (event / 이벤트) trước trong thứ tự chương trình xảy ra trước sự kiện (event / 이벤트) sau;
2. gửi message xảy ra trước việc nhận chính message đó;
3. quan hệ có tính bắc cầu.

Nếu `A → B`, B có thể bị ảnh hưởng bởi A. Nếu không có `A → B` cũng không có `B → A`, hai sự kiện (event / 이벤트) được xem là **đồng thời về lô-gic (logic / 논리) (concurrent)**.

Điểm quan trọng: concurrent ở đây không có nghĩa hai sự kiện (event / 이벤트) xảy ra đúng cùng nanosecond; nó nghĩa hệ thống không có quan hệ nhân quả đủ để xếp chúng theo một chiều bắt buộc.

> **Nối mạch:** **4. Lamport clock** nối từ **3. “Happened-before” là quan hệ lô-gic (logic / 논리)** sang **5. véc-tơ (vector / 벡터) clock**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Lamport clock

**Đồng hồ Lamport (Lamport clock)** gán một số nguyên lô-gic (logic / 논리) cho sự kiện (event / 이벤트). Mỗi tiến trình (process / 프로세스) tăng counter trước sự kiện (event / 이벤트); khi gửi message, nó đính kèm counter; khi nhận, tiến trình (process / 프로세스) lấy `max(local, received)+1`.

Nó bảo đảm:

```text
A → B  =>  L(A) < L(B)
```

Nhưng chiều ngược lại không đúng. `L(A) < L(B)` không chứng minh A gây ra B. Lamport clock tạo một thứ tự tiện dụng nhưng không biểu diễn đầy đủ tính đồng thời (concurrency / 동시성).

> **Nối mạch:** **5. véc-tơ (vector / 벡터) clock** nối từ **4. Lamport clock** sang **6. nhân quả (causal / 인과적) consistency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. véc-tơ (vector / 벡터) clock

**Đồng hồ véc-tơ (vector / 벡터) (vector clock)** giữ một véc-tơ (vector / 벡터) counter, mỗi thành phần đại diện tiến độ lô-gic (logic / 논리) của một replica/tiến trình (process / 프로세스).

Ví dụ:

```text
A: [3,1,0]
B: [2,2,0]
```

Nếu mọi thành phần của véc-tơ (vector / 벡터) A nhỏ hơn hoặc bằng B và ít nhất một thành phần nhỏ hơn, A xảy ra trước B. Nếu không véc-tơ (vector / 벡터) nào trội hoàn toàn, hai trạng thái (state / 상태) có thể concurrent.

Véc-tơ (vector / 벡터) clock vì vậy hữu ích trong hệ thống multi-master hoặc xung đột (conflict / 충돌) detection. Đổi lại siêu dữ liệu (metadata / 메타데이터) tăng theo số participant, nên môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) thường cần biến thể hoặc cơ chế nén.

> **Nối mạch:** **6. nhân quả (causal / 인과적) consistency** nối từ **5. véc-tơ (vector / 벡터) clock** sang **7. Total thứ tự (order / 순서) và nhân quả (causal / 인과적) thứ tự (order / 순서) khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. nhân quả (causal / 인과적) consistency

**Nhất quán nhân quả (causal consistency)** yêu cầu nếu B phụ thuộc A thì mọi observer thấy B phải thấy A trước hoặc cùng lúc theo cách hợp lệ.

Ví dụ:

```text
user đăng bài A
user khác đọc A và viết comment B
```

Nếu replica hiển thị B trước khi A xuất hiện, trải nghiệm vi phạm nhân quả (causal / 인과적) quan hệ (relation / 관계).

Nhân quả (causal / 인과적) consistency yếu hơn linearizability nhưng mạnh hơn eventual consistency thuần túy. Nó thường là điểm cân bằng hữu ích khi muốn giảm cross-region coordination.

> **Nối mạch:** **7. Total thứ tự (order / 순서) và nhân quả (causal / 인과적) thứ tự (order / 순서) khác nhau** nối từ **6. nhân quả (causal / 인과적) consistency** sang **8. Linearizability và real-time thứ tự (order / 순서)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Total thứ tự (order / 순서) và nhân quả (causal / 인과적) thứ tự (order / 순서) khác nhau

**Thứ tự toàn phần (total order)** xếp mọi sự kiện (event / 이벤트) thành một chuỗi duy nhất. Consensus log thường cung cấp một dạng total thứ tự (order / 순서) cho command đã lần ghi nhận (commit / 커밋).

**Thứ tự nhân quả (causal order)** chỉ buộc những sự kiện (event / 이벤트) thực sự phụ thuộc nhau phải theo thứ tự; sự kiện (event / 이벤트) độc lập có thể không cần coordination.

Total thứ tự (order / 순서) đơn giản cho máy trạng thái (state machine / 상태 머신) replication nhưng phải trả chi phí coordination. nhân quả (causal / 인과적) thứ tự (order / 순서) cho tính đồng thời (concurrency / 동시성) nhiều hơn nhưng ứng dụng (application / 애플리케이션) phải xử lý xung đột (conflict / 충돌) hoặc trạng thái (state / 상태) merge phức tạp hơn.

> **Nối mạch:** **8. Linearizability và real-time thứ tự (order / 순서)** nối từ **7. Total thứ tự (order / 순서) và nhân quả (causal / 인과적) thứ tự (order / 순서) khác nhau** sang **9. Lease phụ thuộc giả định thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Linearizability và real-time thứ tự (order / 순서)

**Linearizability** yêu cầu mỗi thao tác (operation / 연산) trông như xảy ra tại một điểm duy nhất giữa lúc gọi và lúc trả kết quả. Nếu thao tác (operation / 연산) A đã hoàn tất trước khi B bắt đầu theo thời gian thực, B phải quan sát A theo thứ tự phù hợp.

Điều này mạnh hơn chỉ có một total thứ tự (order / 순서) nội bộ. Một log có thứ tự nhưng máy khách (client / 클라이언트) đọc từ replica stale có thể vẫn vi phạm linearizability.

> **Nối mạch:** **9. Lease phụ thuộc giả định thời gian** nối từ **8. Linearizability và real-time thứ tự (order / 순서)** sang **10. Timestamp-based giải quyết xung đột (conflict resolution / 충돌 해결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Lease phụ thuộc giả định thời gian

Lease trao quyền trong một khoảng thời gian. Nếu đơn vị sở hữu (owner / 오너) cũ nghĩ lease còn hiệu lực nhưng authority mới đã cấp quyền cho đơn vị sở hữu (owner / 오너) khác, hai writer có thể cùng hoạt động.

Vì vậy lease thường cần:

```text
bounded clock drift
hoặc authority trung tâm
hoặc fencing token ở resource cuối
```

Fencing đơn vị từ (token / 토큰) an toàn hơn khi tài nguyên (resource / 자원) có thể từ chối writer cũ dựa trên số thế hệ tăng đơn điệu. Thời gian một mình không đủ làm protection trong mọi dạng thất bại (failure mode / 실패 모드).

> **Nối mạch:** **10. Timestamp-based giải quyết xung đột (conflict resolution / 충돌 해결)** nối từ **9. Lease phụ thuộc giả định thời gian** sang **11. Hybrid logical clock**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Timestamp-based giải quyết xung đột (conflict resolution / 충돌 해결)

Một số hệ thống chọn “last ghi (write / 쓰기) wins” dựa trên timestamp. Nếu clock lệch, ghi (write / 쓰기) thực tế mới hơn có thể có timestamp nhỏ hơn và bị mất.

Do đó LWW dễ triển khai nhưng ngữ nghĩa (semantics / 의미론) phải được chấp nhận rõ. Nó phù hợp khi xung đột (conflict / 충돌) có thể giải bằng chính sách (policy / 정책) đơn giản; không phù hợp nếu mất một cập nhật (update / 업데이트) là không thể chấp nhận về nghiệp vụ.

> **Nối mạch:** **11. Hybrid logical clock** nối từ **10. Timestamp-based giải quyết xung đột (conflict resolution / 충돌 해결)** sang **12. Clock bất định (uncertainty / 불확실성) và bên ngoài (external / 외부) consistency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Hybrid logical clock

**Hybrid Logical Clock (HLC)** kết hợp thông tin từ vật lý (physical / 물리적) clock với logical thành phần (component / 컴포넌트). Mục tiêu là giữ timestamp gần thời gian thực nhưng vẫn bảo toàn nhân quả (causal / 인과적) thứ tự (ordering / 순서) tốt hơn raw wall clock.

HLC hữu ích cho phân tán (distributed / 분산) cơ sở dữ liệu (database / 데이터베이스) cần timestamp compact, có khả năng so sánh, nhưng không muốn siêu dữ liệu (metadata / 메타데이터) lớn như véc-tơ (vector / 벡터) clock.

Mô hình tư duy (mental model / 사고 모델): vật lý (physical / 물리적) thành phần (component / 컴포넌트) giúp timestamp gần với thời gian con người; logical thành phần (component / 컴포넌트) sửa những trường hợp message khiến nhân quả (causal / 인과적) thứ tự (order / 순서) vượt vật lý (physical / 물리적) reading cục bộ.

> **Nối mạch:** **12. Clock bất định (uncertainty / 불확실성) và bên ngoài (external / 외부) consistency** nối từ **11. Hybrid logical clock** sang **13. hết thời gian chờ (timeout / 타임아웃) không phải thất bại (failure / 실패) detector hoàn hảo**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Clock bất định (uncertainty / 불확실성) và bên ngoài (external / 외부) consistency

Một số hệ thống dùng clock dịch vụ (service / 서비스) có bound bất định (uncertainty / 불확실성) rồi chờ đủ để chắc rằng timestamp lần ghi nhận (commit / 커밋) không bị future thao tác (operation / 연산) vượt sai thứ tự. Chiến lược này đổi độ trễ (latency / 지연 시간) lấy stronger thứ tự (ordering / 순서) guarantee.

Điểm tổng quát không phải học thuộc một sản phẩm cụ thể mà là hiểu rằng nếu muốn dùng vật lý (physical / 물리적) thời gian (time / 시간) để quyết định thứ tự phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션), hệ thống phải quản lý **độ bất định của đồng hồ** như một phần tính đúng đắn (correctness / 정확성) mô hình (model / 모델).

> **Nối mạch:** **13. hết thời gian chờ (timeout / 타임아웃) không phải thất bại (failure / 실패) detector hoàn hảo** nối từ **12. Clock bất định (uncertainty / 불확실성) và bên ngoài (external / 외부) consistency** sang **14. thử lại (retry / 재시도) làm thứ tự quan sát phức tạp hơn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. hết thời gian chờ (timeout / 타임아웃) không phải thất bại (failure / 실패) detector hoàn hảo

Nếu yêu cầu (request / 요청) chưa trả sau 500 ms, có thể máy chủ (server / 서버) chết, mạng (network / 네트워크) chậm, hàng đợi (queue / 큐) dài, GC pause hoặc phản hồi (response / 응답) bị mất. hết thời gian chờ (timeout / 타임아웃) chỉ tạo **nghi ngờ (suspicion)**.

Đây là liên kết (connection / 연결) giữa thời gian (time / 시간) và thất bại (failure / 실패) detector. Trong asynchronous mạng (network / 네트워크) không có upper bound cố định cho delay, không thể phân biệt chắc chắn “nút (node / 노드) chết” với “nút (node / 노드) rất chậm” chỉ bằng thời gian chờ hữu hạn.

> **Nối mạch:** **14. thử lại (retry / 재시도) làm thứ tự quan sát phức tạp hơn** nối từ **13. hết thời gian chờ (timeout / 타임아웃) không phải thất bại (failure / 실패) detector hoàn hảo** sang **15. Tracing và clock skew**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. thử lại (retry / 재시도) làm thứ tự quan sát phức tạp hơn

Máy khách (client / 클라이언트) gửi yêu cầu (request / 요청) R1, hết thời gian chờ (timeout / 타임아웃) rồi thử lại (retry / 재시도) R2. R2 có thể tới máy chủ (server / 서버) trước R1 nếu tuyến (route / 경로) khác nhau. Nếu thao tác (operation / 연산) không idempotent, thứ tự arrival có thể tạo duplicate hoặc trạng thái ngoài dự kiến.

Phân tán (distributed / 분산) giao thức (protocol / 프로토콜) phải lập luận (reasoning / 추론) theo message định danh (identity / 식별자) và durable trạng thái (state / 상태), không giả định yêu cầu (request / 요청) đến theo thứ tự gửi.

> **Nối mạch:** **15. Tracing và clock skew** nối từ **14. thử lại (retry / 재시도) làm thứ tự quan sát phức tạp hơn** sang **16. mạng (network / 네트워크) partition và “thời gian im lặng”**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Tracing và clock skew

Phân tán (distributed / 분산) dấu vết (trace / 추적) thường ghép span từ nhiều host. Nếu dùng wall-clock timestamp tuyệt đối, clock skew có thể làm child span trông như bắt đầu trước parent.

Dấu vết (trace / 추적) hệ thống (system / 시스템) thường dùng parent-child relationship, duration monotonic và correction lô-gic (logic / 논리) thay vì tin tuyệt đối vào timestamp toàn cục.

Khả năng quan sát (observability / 관측 가능성) vì vậy cũng chịu cùng giới hạn về thời gian (time / 시간) mô hình (model / 모델) như phân tán (distributed / 분산) tính đúng đắn (correctness / 정확성).

> **Nối mạch:** **16. mạng (network / 네트워크) partition và “thời gian im lặng”** nối từ **15. Tracing và clock skew** sang **17. phụ thuộc (dependency / 의존성) với consensus**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. mạng (network / 네트워크) partition và “thời gian im lặng”

Một nút (node / 노드) không nhận heartbeat trong 10 giây không biết remote nút (node / 노드) chết hay đường mạng bị partition. Nếu cả hai phía tự promote leader mới, split-brain có thể xảy ra.

Thời gian im lặng chỉ là bằng chứng (evidence / 증거), không phải proof. Authority transfer cần quorum, fencing hoặc giao thức (protocol / 프로토콜) mạnh hơn.

> **Nối mạch:** **17. phụ thuộc (dependency / 의존성) với consensus** nối từ **16. mạng (network / 네트워크) partition và “thời gian im lặng”** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. phụ thuộc (dependency / 의존성) với consensus

Consensus không yêu cầu đồng hồ vật lý đồng bộ hoàn hảo để bảo đảm an toàn (safety / 안전). Timing chủ yếu ảnh hưởng liveness, election hết thời gian chờ (timeout / 타임아웃) và tốc độ convergence.

Đây là một insight quan trọng: giao thức (protocol / 프로토콜) tốt cố tách **an toàn (safety / 안전)** khỏi timing giả định (assumption / 가정) khi có thể. Nếu clock chậm hoặc message delay lớn, hệ thống có thể ngừng tiến triển tạm thời nhưng không nên lần ghi nhận (commit / 커밋) hai giá trị mâu thuẫn.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **17. phụ thuộc (dependency / 의존성) với consensus** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Timestamp lớn hơn nghĩa là sự kiện (event / 이벤트) xảy ra sau.”** Chỉ đúng nếu clock mô hình (model / 모델) và bất định (uncertainty / 불확실성) cho phép kết luận đó.

**“NTP làm mọi máy chủ (server / 서버) có cùng giờ.”** NTP giảm sai lệch nhưng không tạo đồng hồ tuyệt đối hoàn hảo.

**“hết thời gian chờ (timeout / 타임아웃) nghĩa là yêu cầu (request / 요청) thất bại.”** hết thời gian chờ (timeout / 타임아웃) chỉ nói caller chưa nhận kết quả trong deadline.

**“Consensus cần clock chính xác.”** an toàn (safety / 안전) của consensus thường dựa vào quorum/log rules; clock chủ yếu giúp hết thời gian chờ (timeout / 타임아웃) và liveness.

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> Trong hệ thống phân tán (distributed system / 분산 시스템), **thời gian không phải một trục toàn cục miễn phí**. Hãy tách vật lý (physical / 물리적) thời gian (time / 시간), logical thứ tự (order / 순서) và causality rồi chọn đúng công cụ cho guarantee cần thiết.

Khi thiết kế replication hoặc workflow, hãy hỏi: thao tác (operation / 연산) nào có nhân quả (causal / 인과적) phụ thuộc (dependency / 의존성), thứ tự (ordering / 순서) nào thực sự cần total, clock bất định (uncertainty / 불확실성) là bao nhiêu, hết thời gian chờ (timeout / 타임아웃) chỉ tạo suspicion hay authority, và xung đột (conflict / 충돌) được phát hiện/giải quyết ở đâu.

Xem thêm: [Consensus](./03_consensus_log_replication_reconfiguration_and_snapshots.md), [CRDT và causal consistency](./04_crdts_causal_consistency_and_conflict_resolution.md), [Leases và fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md) và [Distributed tracing](../../90_connections/advanced/README.md).

> **Bàn giao:** Giữ lại distinction giữa physical time, logical order, causality, timeout suspicion và consensus authority trước khi rời chapter. Sang [Consensus internals](./03_consensus_log_replication_reconfiguration_and_snapshots.md) khi cần durable ordering, [CRDTs](./04_crdts_causal_consistency_and_conflict_resolution.md) khi cần causal merge, hoặc [Leases/fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md) khi thời gian tham gia vào quyền ghi; quay về [README](./README.md) để xác nhận owner.
