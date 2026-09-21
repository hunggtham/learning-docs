# Thời gian, đồng hồ, thứ tự và quan hệ nhân quả trong hệ thống phân tán

Trong một chương trình chạy trên một máy, lập trình viên thường có trực giác rằng “A xảy ra trước B” nếu A xuất hiện trước trong luồng lệnh hoặc đồng hồ hệ thống cho số nhỏ hơn. Trong hệ thống phân tán, trực giác đó trở nên nguy hiểm. Hai máy có đồng hồ vật lý khác nhau, message có thể trễ hoặc đi đường khác nhau, và không tồn tại một quan sát viên trung tâm luôn biết chính xác thứ tự toàn cục của mọi sự kiện.

Chapter này giải thích vì sao **thời gian vật lý (physical time)**, **thứ tự logic (logical ordering)** và **quan hệ nhân quả (causality / 인과성)** là ba khái niệm khác nhau, đồng thời chỉ ra chúng ảnh hưởng thế nào đến replication, consensus, lease, conflict resolution và observability.

## 1. Đồng hồ vật lý không hoàn hảo

Mỗi máy có oscillator riêng. Tốc độ của oscillator có sai số nên hai clock có thể **trôi (clock drift)** theo thời gian. Hệ thống đồng bộ thời gian như NTP hoặc PTP giúp giảm sai lệch nhưng không biến clock thành nguồn sự thật tuyệt đối.

Ta cần phân biệt:

- **clock offset**: hai clock đang lệch nhau bao nhiêu tại một thời điểm;
- **clock drift**: tốc độ clock chạy nhanh/chậm tương đối theo thời gian;
- **clock uncertainty**: khoảng mà hệ thống không thể biết thời gian thật chính xác hơn.

Nếu server A báo `12:00:00.100` và server B báo `12:00:00.090`, không thể tự động kết luận event ở B xảy ra trước event ở A nếu clock offset chưa được kiểm soát đủ chặt.

## 2. Wall clock và monotonic clock

**Đồng hồ lịch (wall clock)** cố gắng biểu diễn thời gian thực như ngày/giờ. Nó có thể bị điều chỉnh khi NTP sửa clock hoặc người quản trị thay đổi thời gian.

**Đồng hồ đơn điệu (monotonic clock)** chỉ tăng theo một chiều và phù hợp để đo duration:

```text
start = monotonic_now()
...
elapsed = monotonic_now() - start
```

Timeout, latency và interval nên dựa vào monotonic clock nếu runtime hỗ trợ. Dùng wall clock để đo timeout có thể gây lỗi nếu thời gian hệ thống nhảy lùi hoặc tiến.

## 3. “Happened-before” là quan hệ logic

Lamport đưa ra quan hệ **xảy ra trước (happened-before, →)** dựa trên ba quy tắc trực giác:

1. trong cùng một process, event trước trong thứ tự chương trình xảy ra trước event sau;
2. gửi message xảy ra trước việc nhận chính message đó;
3. quan hệ có tính bắc cầu.

Nếu `A → B`, B có thể bị ảnh hưởng bởi A. Nếu không có `A → B` cũng không có `B → A`, hai event được xem là **đồng thời về logic (concurrent)**.

Điểm quan trọng: concurrent ở đây không có nghĩa hai event xảy ra đúng cùng nanosecond; nó nghĩa hệ thống không có quan hệ nhân quả đủ để xếp chúng theo một chiều bắt buộc.

## 4. Lamport clock

**Đồng hồ Lamport (Lamport clock)** gán một số nguyên logic cho event. Mỗi process tăng counter trước event; khi gửi message, nó đính kèm counter; khi nhận, process lấy `max(local, received)+1`.

Nó bảo đảm:

```text
A → B  =>  L(A) < L(B)
```

Nhưng chiều ngược lại không đúng. `L(A) < L(B)` không chứng minh A gây ra B. Lamport clock tạo một thứ tự tiện dụng nhưng không biểu diễn đầy đủ concurrency.

## 5. Vector clock

**Đồng hồ vector (vector clock)** giữ một vector counter, mỗi thành phần đại diện tiến độ logic của một replica/process.

Ví dụ:

```text
A: [3,1,0]
B: [2,2,0]
```

Nếu mọi thành phần của vector A nhỏ hơn hoặc bằng B và ít nhất một thành phần nhỏ hơn, A xảy ra trước B. Nếu không vector nào trội hoàn toàn, hai state có thể concurrent.

Vector clock vì vậy hữu ích trong hệ thống multi-master hoặc conflict detection. Đổi lại metadata tăng theo số participant, nên production system thường cần biến thể hoặc cơ chế nén.

## 6. Causal consistency

**Nhất quán nhân quả (causal consistency)** yêu cầu nếu B phụ thuộc A thì mọi observer thấy B phải thấy A trước hoặc cùng lúc theo cách hợp lệ.

Ví dụ:

```text
user đăng bài A
user khác đọc A và viết comment B
```

Nếu replica hiển thị B trước khi A xuất hiện, trải nghiệm vi phạm causal relation.

Causal consistency yếu hơn linearizability nhưng mạnh hơn eventual consistency thuần túy. Nó thường là điểm cân bằng hữu ích khi muốn giảm cross-region coordination.

## 7. Total order và causal order khác nhau

**Thứ tự toàn phần (total order)** xếp mọi event thành một chuỗi duy nhất. Consensus log thường cung cấp một dạng total order cho command đã commit.

**Thứ tự nhân quả (causal order)** chỉ buộc những event thực sự phụ thuộc nhau phải theo thứ tự; event độc lập có thể không cần coordination.

Total order đơn giản cho state machine replication nhưng phải trả chi phí coordination. Causal order cho concurrency nhiều hơn nhưng application phải xử lý conflict hoặc state merge phức tạp hơn.

## 8. Linearizability và real-time order

**Linearizability** yêu cầu mỗi operation trông như xảy ra tại một điểm duy nhất giữa lúc gọi và lúc trả kết quả. Nếu operation A đã hoàn tất trước khi B bắt đầu theo thời gian thực, B phải quan sát A theo thứ tự phù hợp.

Điều này mạnh hơn chỉ có một total order nội bộ. Một log có thứ tự nhưng client đọc từ replica stale có thể vẫn vi phạm linearizability.

## 9. Lease phụ thuộc giả định thời gian

Lease trao quyền trong một khoảng thời gian. Nếu owner cũ nghĩ lease còn hiệu lực nhưng authority mới đã cấp quyền cho owner khác, hai writer có thể cùng hoạt động.

Vì vậy lease thường cần:

```text
bounded clock drift
hoặc authority trung tâm
hoặc fencing token ở resource cuối
```

Fencing token an toàn hơn khi resource có thể từ chối writer cũ dựa trên số thế hệ tăng đơn điệu. Thời gian một mình không đủ làm protection trong mọi failure mode.

## 10. Timestamp-based conflict resolution

Một số hệ thống chọn “last write wins” dựa trên timestamp. Nếu clock lệch, write thực tế mới hơn có thể có timestamp nhỏ hơn và bị mất.

Do đó LWW dễ triển khai nhưng semantics phải được chấp nhận rõ. Nó phù hợp khi conflict có thể giải bằng policy đơn giản; không phù hợp nếu mất một update là không thể chấp nhận về nghiệp vụ.

## 11. Hybrid logical clock

**Hybrid Logical Clock (HLC)** kết hợp thông tin từ physical clock với logical component. Mục tiêu là giữ timestamp gần thời gian thực nhưng vẫn bảo toàn causal ordering tốt hơn raw wall clock.

HLC hữu ích cho distributed database cần timestamp compact, có khả năng so sánh, nhưng không muốn metadata lớn như vector clock.

Mental model: physical component giúp timestamp gần với thời gian con người; logical component sửa những trường hợp message khiến causal order vượt physical reading cục bộ.

## 12. Clock uncertainty và external consistency

Một số hệ thống dùng clock service có bound uncertainty rồi chờ đủ để chắc rằng timestamp commit không bị future operation vượt sai thứ tự. Chiến lược này đổi latency lấy stronger ordering guarantee.

Điểm tổng quát không phải học thuộc một sản phẩm cụ thể mà là hiểu rằng nếu muốn dùng physical time để quyết định thứ tự distributed transaction, hệ thống phải quản lý **độ bất định của đồng hồ** như một phần correctness model.

## 13. Timeout không phải failure detector hoàn hảo

Nếu request chưa trả sau 500 ms, có thể server chết, network chậm, queue dài, GC pause hoặc response bị mất. Timeout chỉ tạo **nghi ngờ (suspicion)**.

Đây là connection giữa time và failure detector. Trong asynchronous network không có upper bound cố định cho delay, không thể phân biệt chắc chắn “node chết” với “node rất chậm” chỉ bằng thời gian chờ hữu hạn.

## 14. Retry làm thứ tự quan sát phức tạp hơn

Client gửi request R1, timeout rồi retry R2. R2 có thể tới server trước R1 nếu route khác nhau. Nếu operation không idempotent, thứ tự arrival có thể tạo duplicate hoặc trạng thái ngoài dự kiến.

Distributed protocol phải reasoning theo message identity và durable state, không giả định request đến theo thứ tự gửi.

## 15. Tracing và clock skew

Distributed trace thường ghép span từ nhiều host. Nếu dùng wall-clock timestamp tuyệt đối, clock skew có thể làm child span trông như bắt đầu trước parent.

Trace system thường dùng parent-child relationship, duration monotonic và correction logic thay vì tin tuyệt đối vào timestamp toàn cục.

Observability vì vậy cũng chịu cùng giới hạn về time model như distributed correctness.

## 16. Network partition và “thời gian im lặng”

Một node không nhận heartbeat trong 10 giây không biết remote node chết hay đường mạng bị partition. Nếu cả hai phía tự promote leader mới, split-brain có thể xảy ra.

Thời gian im lặng chỉ là evidence, không phải proof. Authority transfer cần quorum, fencing hoặc protocol mạnh hơn.

## 17. Dependency với consensus

Consensus không yêu cầu đồng hồ vật lý đồng bộ hoàn hảo để bảo đảm safety. Timing chủ yếu ảnh hưởng liveness, election timeout và tốc độ convergence.

Đây là một insight quan trọng: protocol tốt cố tách **safety** khỏi timing assumption khi có thể. Nếu clock chậm hoặc message delay lớn, hệ thống có thể ngừng tiến triển tạm thời nhưng không nên commit hai giá trị mâu thuẫn.

## Common Misconceptions

**“Timestamp lớn hơn nghĩa là event xảy ra sau.”** Chỉ đúng nếu clock model và uncertainty cho phép kết luận đó.

**“NTP làm mọi server có cùng giờ.”** NTP giảm sai lệch nhưng không tạo đồng hồ tuyệt đối hoàn hảo.

**“Timeout nghĩa là request thất bại.”** Timeout chỉ nói caller chưa nhận kết quả trong deadline.

**“Consensus cần clock chính xác.”** Safety của consensus thường dựa vào quorum/log rules; clock chủ yếu giúp timeout và liveness.

## Mô hình tư duy

> Trong distributed system, **thời gian không phải một trục toàn cục miễn phí**. Hãy tách physical time, logical order và causality rồi chọn đúng công cụ cho guarantee cần thiết.

Khi thiết kế replication hoặc workflow, hãy hỏi: operation nào có causal dependency, ordering nào thực sự cần total, clock uncertainty là bao nhiêu, timeout chỉ tạo suspicion hay authority, và conflict được phát hiện/giải quyết ở đâu.

Xem thêm: [Consensus](./03_consensus_log_replication_reconfiguration_and_snapshots.md), [CRDT và causal consistency](./04_crdts_causal_consistency_and_conflict_resolution.md), [Leases và fencing](./02_leases_fencing_tokens_and_split_brain_prevention.md) và [Distributed tracing](../../90_connections/advanced/README.md).
