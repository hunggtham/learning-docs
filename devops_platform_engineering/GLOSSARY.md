# DevOps / Platform Engineering Glossary

File này dùng để tra nhanh thuật ngữ, không thay thế chapter giải thích cơ chế.

| Thuật ngữ | Ý nghĩa trong library |
|---|---|
| Luồng giá trị (value stream / 가치 흐름) | Chuỗi từ nhu cầu, thay đổi source, kiểm chứng, phát hành đến kết quả production và feedback quay lại team. |
| Hiện vật (artifact / 산출물) | Output bất biến của quá trình build như image, package, binary hoặc bundle; nên được định danh để cùng một artifact đi qua các môi trường. |
| Tái lập được (reproducible) | Cùng input và toolchain đã khóa cho output tương đương theo contract đã định, giúp giảm “works on my machine”. |
| Trạng thái mong muốn (desired state) | State hệ thống mà người dùng/controller khai báo muốn đạt tới. |
| Trạng thái thực tế (actual state) | State hệ thống hiện đang có tại thời điểm quan sát. |
| Đối soát (reconciliation / 조정) | Control loop liên tục so desired state với actual state và thực hiện action để thu hẹp sai khác. |
| Sai lệch cấu hình (drift) | Actual infrastructure/config khác state được quản lý hoặc mong muốn do thay đổi ngoài luồng, lỗi hoặc dependency biến đổi. |
| Tính lặp an toàn (idempotency) | Thực hiện cùng operation nhiều lần không làm state tiếp tục lệch sau khi đã đạt kết quả mong muốn. |
| Bán kính ảnh hưởng (blast radius) | Phạm vi user, workload, region hoặc data có thể bị ảnh hưởng bởi một failure/change. |
| Promotion | Chuyển cùng một artifact/config version sang stage tiếp theo sau khi đủ evidence; khác với build lại ở từng môi trường. |
| Rollback | Quay workload/config/traffic về trạng thái tương thích trước đó; không phải lúc nào cũng đơn giản khi schema hoặc external state đã đổi. |
| Roll forward | Khắc phục bằng phiên bản mới thay vì quay lại, thường cần khi state migration không thể đảo. |
| Telemetry | Dữ liệu hệ thống phát ra để suy luận behavior, thường gồm metrics, logs, traces và events. |
| Khả năng quan sát (observability / 관측 가능성) | Khả năng suy luận trạng thái nội tại từ evidence bên ngoài; không đồng nghĩa với “có nhiều dashboard”. |
| Chỉ báo mức dịch vụ (Service Level Indicator — SLI) | Phép đo gần với trải nghiệm hoặc contract của service, ví dụ tỷ lệ request hợp lệ thành công. |
| Mục tiêu mức dịch vụ (Service Level Objective — SLO) | Mục tiêu định lượng cho SLI trong một cửa sổ thời gian. |
| Error budget | Phần không hoàn hảo được chấp nhận bởi SLO; dùng để cân bằng tốc độ thay đổi và reliability. |
| Toil | Công việc vận hành lặp lại, thủ công, có thể tự động hóa, tăng gần tuyến tính theo quy mô và ít tạo learning lâu dài. |
| Runbook | Quy trình thao tác cho tình huống vận hành đã biết, phải nêu điều kiện, evidence, action và cách kiểm chứng thay vì chỉ liệt kê lệnh. |
| Playbook | Khung phản ứng rộng hơn cho loại sự cố, có thể cần judgment và nhiều nhánh quyết định. |
| Hạ tầng dưới dạng mã (Infrastructure as Code — IaC / 코드형 인프라) | Quản lý desired infrastructure bằng file/versioned change và engine có khả năng lập kế hoạch, đối chiếu state, tạo/sửa/xóa resource. |
| Policy as Code | Biểu diễn policy dưới dạng rule có thể kiểm tra tự động trong CI hoặc admission/reconciliation path. |
| GitOps | Operating model dùng Git/version control làm interface cho desired state và agent/controller tự đối soát state thực tế. |
| Chuỗi cung ứng phần mềm (software supply chain) | Toàn bộ đường đi từ source, dependency, build environment, artifact, registry đến deployment. |
| Provenance | Bằng chứng về artifact được tạo từ source, process và builder nào. |
| SBOM | Software Bill of Materials; danh mục thành phần/dependency được dùng để tạo software artifact. |
| Golden path | Đường đi chuẩn đã được platform tối ưu cho use case phổ biến. |
| Guardrail | Cơ chế giúp hoặc ép lựa chọn nằm trong boundary an toàn mà không tạo handoff thủ công không cần thiết. |
| Internal Developer Platform — IDP | Tập capability, interface và workflow nội bộ giúp product team tự phục vụ phần hạ tầng/delivery phổ biến. |
| Control plane | Thành phần giữ desired state, policy và quyết định orchestration; thường không trực tiếp phục vụ user request của application. |
| Data plane | Thành phần thực thi traffic/workload/data path theo quyết định từ control plane. |
| Multi-tenancy | Nhiều team/workload dùng chung một platform với isolation, quota, policy và ownership boundary. |
| FinOps | Discipline phối hợp kỹ thuật, tài chính và sản phẩm để làm chi phí cloud có visibility, ownership và trade-off rõ ràng. |
| Mean Time to Restore/Recover — MTTR | Thời gian phục hồi service sau failure theo định nghĩa đo đã thống nhất; dễ bị hiểu sai nếu không xác định mốc bắt đầu/kết thúc. |
| RTO | Recovery Time Objective; thời gian tối đa mục tiêu để phục hồi capability sau thảm họa. |
| RPO | Recovery Point Objective; mức mất dữ liệu theo thời gian mà tổ chức chấp nhận trong recovery scenario. |
| Immutable infrastructure | Thay vì sửa trực tiếp server/workload đang chạy, tạo phiên bản mới từ source of truth rồi thay thế instance cũ. |
| Cattle, not pets | Mental model coi instance là thay thế được; không có nghĩa bỏ qua stateful workload hoặc forensic evidence. |
| Day 0 / Day 1 / Day 2 | Thiết kế/provision ban đầu, đưa hệ thống vào hoạt động, rồi vận hành dài hạn gồm upgrade, backup, scaling, incident, rotation và cleanup. |
| Lead time | Thời gian từ lúc một nhu cầu/thay đổi bắt đầu đến khi tạo giá trị hoặc chạm trạng thái đích; gồm cả processing time và thời gian chờ. |
| Cycle/processing time | Thời gian work item thực sự được xử lý trong một bước hoặc một flow; cần phân biệt với lead time chứa queue/handoff. |
| Công việc đang dở (Work in Progress — WIP) | Số work item đang nằm trong flow nhưng chưa hoàn tất; WIP cao thường kéo queue và thời gian hoàn thành tăng. |
| Build kín (hermetic build) | Build chỉ được thấy các input đã khai báo thay vì phụ thuộc ngầm vào host, network hoặc tool cài sẵn. |
| Attestation | Statement có subject và predicate được một identity xác nhận/ký, dùng để chứng minh provenance, verification hoặc policy fact cho artifact. |
| Trust domain | Boundary trong đó identity/output được coi có mức tin cậy tương đương; output từ trust domain thấp không nên trở thành input ngầm của domain cao. |
| Pressure Stall Information — PSI | Telemetry của Linux mô tả thời gian task bị trì hoãn do thiếu CPU, memory hoặc I/O; bổ sung cho utilization metric. |
| Capacity có thể schedule (schedulable capacity) | Capacity thật mà một workload cụ thể có thể được đặt vào sau khi xét kích thước request, constraint và fragmentation; khác tổng capacity còn trống. |
| PodDisruptionBudget — PDB | Budget giới hạn một số voluntary eviction của Pod; không phải guarantee chống node crash hoặc mọi failure. |
| Preemption | Cơ chế cho workload priority cao giành resource bằng cách loại workload priority thấp hơn; phân bổ lại scarcity chứ không tạo thêm capacity. |
| Burn rate | Tốc độ tiêu error budget tương đối, thường nhìn như observed bad-event rate chia allowed bad-event rate. |
| Backpressure | Cơ chế truyền tín hiệu ngược khi downstream không theo kịp để upstream giảm tốc hoặc giới hạn work mới. |
| Load shedding | Chủ động từ chối/bỏ bớt work theo policy khi capacity thiếu để bảo vệ core capability khỏi collapse. |
| Field ownership | Contract chỉ rõ controller/actor nào chịu trách nhiệm cho từng phần state; thiếu ownership dễ tạo reconciliation conflict/oscillation. |
| Partial apply | IaC/provisioning thay được một phần remote state rồi fail; không có guarantee transaction atomic xuyên nhiều resource. |
| Eventual consistency | State mới cần thời gian lan truyền giữa subsystem; API create success không luôn đồng nghĩa resource đã usable ở mọi dependency. |
| Schedulability fragmentation | Tổng resource còn đủ nhưng bị chia trên nhiều node/failure domain nên một workload lớn không fit vào bất kỳ placement hợp lệ nào. |
| Coordinated omission | Sai lệch benchmark khi load generator giảm gửi work đúng lúc hệ thống chậm, khiến latency/saturation nhìn tốt hơn production thật. |
| Effective configuration | Configuration mà process/workload thực sự đang sử dụng tại runtime, có thể khác object/source-of-truth vừa được cập nhật. |
| Ephemeral port | Source port tạm thời mà OS cấp cho outbound connection; có thể trở thành capacity boundary khi connection churn hoặc NAT fan-out rất lớn. |
| Connection tracking — conntrack | State kernel/firewall/NAT giữ để theo dõi flow; table hoặc translation capacity cạn có thể gây network failure dù application còn resource. |
| PID 1 | Process đầu tiên trong PID namespace; trong container thường là process chính và có trách nhiệm signal/child-reaping cần được hiểu rõ. |
| Writable layer | Layer ghi tạm phía trên image read-only khi container chạy; không phải durable storage contract. |
| Multi-architecture image | Image index/manifest có variant theo kiến trúc như `amd64`/`arm64`; runtime chọn artifact tương thích node. |
| Time-to-capacity | Thời gian từ lúc demand cần thêm resource đến khi capacity mới thực sự sẵn sàng phục vụ traffic/work. |
| Durability | Khả năng dữ liệu tồn tại lâu dài mà không bị mất/corrupt; khác availability là khả năng truy cập/phục vụ tại thời điểm cần. |
| Availability | Khả năng capability truy cập và phục vụ theo contract trong thời gian quan sát; không tự động đồng nghĩa dữ liệu durable hoặc có backup. |
| Showback | Hiển thị chi phí cho owner/team để tạo visibility và incentive mà chưa hạch toán trực tiếp vào ngân sách của họ. |
| Chargeback | Phân bổ/hạch toán chi phí shared platform/cloud về đơn vị sử dụng theo mô hình đã định. |
| Unit cost | Chi phí trên một đơn vị work/value như successful request, order, build minute hoặc GB processed; denominator phải phản ánh outcome có ý nghĩa. |
| Control-plane fairness | Bảo vệ tài nguyên điều khiển dùng chung như API server, scheduler, controller hoặc CI coordinator khỏi một tenant/workload gây starvation cho tenant khác. |
| Evidence freshness | Độ mới của evidence so với actual state; dữ liệu đúng nhưng quá cũ vẫn có thể dẫn tới quyết định production sai. |
| Compensation | Action mới nhằm phục hồi invariant sau partial side effect khi không thể rollback chính xác về state cũ. |
| Adoption | Quy trình đưa một external resource đã tồn tại vào ownership/reconciliation của platform sau khi xác minh identity, policy và state mapping. |
| Orphan resource | Resource còn tồn tại nhưng không còn ownership/state mapping đáng tin trong control plane; cần quarantine/adoption/cleanup semantics thay vì xóa mù. |
| Break-glass access | Phiên nâng quyền khẩn cấp có scope, TTL, reason, audit và lifecycle riêng; không nên là admin account cố định dùng hằng ngày. |
| Policy audit mode | Chạy policy để ghi nhận violation/impact mà chưa chặn request, thường dùng trước staged enforcement. |
| Recovery convergence | Quá trình sau mitigation đưa backlog, data invariant, capacity và degraded mode trở lại steady state có kiểm soát. |
| Causal graph | Biểu diễn quan hệ mechanism giữa trigger, amplifier và hậu quả thay vì chỉ xếp sự kiện theo timestamp. |
| Circuit breaker | Cơ chế tạm ngừng gửi work tới dependency đang fail theo policy để bảo vệ caller và giảm work vô ích; không tự chữa dependency. |
| Bulkhead | Tách concurrency/resource pool theo dependency hoặc workload class để một failure không chiếm toàn bộ resource caller. |
| Hedged request | Gửi thêm attempt khi request đầu chậm để giảm tail latency; đổi lại tăng load và cần idempotency/cancellation semantics. |
| Backfill | Workload di chuyển/bổ sung dữ liệu sau schema change; cần throttle, checkpoint, resume và invariant cho mixed state. |
| Dual-write | Tạm ghi cùng logical update sang nhiều representation/store; không atomic mặc định nên cần source-of-truth, reconciliation và discrepancy evidence. |
| Telemetry priority | Chính sách ưu tiên signal khi observability pipeline quá tải để giữ evidence critical thay vì drop ngẫu nhiên mọi dữ liệu. |
| Safe mode | Trạng thái degraded của control plane cho phép một tập operation an toàn trong khi chặn mutation rủi ro lúc dependency/state chưa đáng tin. |
| Recoverable capacity | Capacity có thể được thu hồi/sẵn sàng trong deadline recovery, khác với capacity chỉ đang được workload khác mượn trên giấy. |
