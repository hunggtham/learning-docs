# Container: image, runtime, isolation và production behavior

## 1. Container không phải máy ảo nhỏ

Container trước hết là process được kernel cô lập và giới hạn bằng các primitive của hệ điều hành. Nó dùng kernel của host thay vì mang kernel riêng như VM truyền thống. Namespaces quyết định process nhìn thấy gì; cgroups quyết định resource account/control; capabilities và seccomp thu hẹp quyền kernel.

Cơ chế sâu đã có tại [containers, namespaces, cgroups, capabilities và seccomp](../../computer_science/03_operating_systems/advanced/06_containers_namespaces_cgroups_capabilities_and_seccomp.md). Chapter này tập trung cách các primitive đó biến thành image/runtime workflow.

## 2. Image là filesystem + metadata bất biến theo layer

Container image thường gồm nhiều layer content-addressed và metadata như command, environment, user. Image không phải “snapshot của một server đang chạy” theo nghĩa truyền thống; nó là package để runtime tạo root filesystem và process environment.

Layering giúp cache và distribution, nhưng cũng tạo hiểu nhầm. Xóa secret ở layer sau không có nghĩa secret biến mất khỏi layer cũ. Vì vậy credential không nên `COPY` vào build context/image rồi xóa. Multi-stage build giúp chỉ đưa output cần thiết sang final image.

## 3. Container lifecycle gắn với process chính

Container sống khi process chính còn sống. Nếu process chính thoát, container hoàn thành dù child process khác có thể từng được tạo. Vì vậy pattern daemonize bên trong container thường không cần thiết.

Signal handling đặc biệt quan trọng. Runtime/orchestrator gửi signal cho process chính khi stop. Application phải nhận và shutdown theo deadline. Nếu dùng shell wrapper không `exec` process thật, signal có thể dừng ở shell. Entrypoint cần được hiểu như lifecycle adapter chứ không chỉ script tiện lợi.

## 4. Image nhỏ không phải mục tiêu duy nhất

Giảm image size cải thiện pull time và attack surface, nhưng image tối thiểu đến mức không còn certificate CA, timezone data hoặc diagnostic capability cần thiết có thể gây lỗi production khó hiểu. Chọn base image dựa trên runtime requirement, vulnerability surface, update policy và operability.

Distroless phù hợp nhiều workload nhưng debugging thường cần ephemeral/debug container hoặc tool ở node; không nên vì thiếu `curl` mà cài một loạt package trực tiếp vào production container lúc incident.

## 5. Dockerfile là build graph

Đọc Dockerfile như một graph cache. Instruction nào phụ thuộc input thường thay đổi nên đặt sau instruction ổn định nếu muốn reuse cache. Ví dụ với Node/Java, dependency descriptor/lockfile có thể copy trước, resolve dependency, rồi mới copy source.

Tuy nhiên cache correctness ưu tiên speed. Build argument, secret mount và platform target phải được dùng theo semantics đúng. Secret cho package registry nên dùng build secret mechanism thay vì `ARG` hoặc `ENV` có nguy cơ lưu vào history/layer.

## 6. Root inside container vẫn là quyền đáng chú ý

“Root trong container” không tự động bằng root host, nhưng nếu container escape vulnerability, mount nhạy cảm hoặc capability quá rộng thì impact tăng. Production default nên chạy non-root khi application không cần đặc quyền, drop capability không dùng, dùng read-only filesystem khi phù hợp và tránh mount host socket kiểu `/var/run/docker.sock` trừ khi hiểu rõ quyền tương đương control-plane mà nó trao.

Container security là defense in depth, không dựa vào một namespace boundary duy nhất.

## 7. Resource request/limit bắt đầu từ cgroup

Khi orchestrator đặt memory limit, kernel/cgroup cuối cùng là nơi enforce. Memory vượt boundary có thể dẫn tới OOM kill. CPU limit thường dẫn tới throttling thay vì kill. Vì vậy failure pattern khác nhau: memory issue có process chết; CPU issue thường là latency tăng.

Đừng đặt resource limit bằng cách copy con số giữa service. Cần đo working set, concurrency, runtime behavior và peak. Với JVM/managed runtime, heap sizing phải tính cả native memory và container awareness.

## 8. Writable layer là ephemeral state

Container writable layer thường không phải nơi lưu state cần tồn tại sau reschedule. Log file, upload và database data nếu chỉ ở writable layer có thể mất khi container bị thay. Stateful data phải đi qua volume/storage contract phù hợp.

“Stateless service” không có nghĩa process không có state; nó có cache, connection và in-flight request. Nó nghĩa state cần durable/authoritative không phụ thuộc identity của instance cụ thể.

## 9. Health check phải đo đúng semantics

Liveness trả lời “process này còn có khả năng tự phục hồi hay cần restart?”. Readiness trả lời “instance này có nên nhận traffic lúc này không?”. Trộn hai semantics có thể tạo restart loop khi dependency tạm lỗi.

Ví dụ database chậm không nhất thiết là lý do kill process. Nếu liveness phụ thuộc DB, outage DB có thể khiến hàng trăm pod restart cùng lúc, tăng load khi DB vừa hồi phục. Readiness có thể tạm đưa instance khỏi traffic; liveness nên tập trung deadlock/hang không tự hồi được.

## 10. Tag, digest và promotion

Image tag là alias; digest là identity content. Production release nên có khả năng truy vết digest. Nếu manifest chỉ ghi tag mutable, rollout/restart ở hai thời điểm có thể lấy image khác nhau.

Build một lần, ký/scanning metadata một lần, rồi promote digest là pattern giúp giảm uncertainty.

## 11. Debug container theo layer

Khi container fail start, xem image/entrypoint/config trước network. Khi chạy nhưng unhealthy, xem process, ports, probe và dependency. Khi bị kill, xem exit code, OOM/event và resource pressure. Khi latency tăng, xem CPU throttling, memory/GC, I/O và network.

Container không nên trở thành abstraction khiến operator quên Linux. Nó chỉ thêm một layer packaging và isolation vào cùng execution model.

## 12. Layer bất biến không có nghĩa filesystem runtime bất biến

Image layer là content-addressed và read-only khi runtime ghép filesystem, nhưng container thường có thêm writable layer phía trên. Khi process sửa một file vốn nằm trong lower layer, storage driver có thể phải thực hiện copy-up trước khi ghi. Vì vậy một workload ghi nhiều dữ liệu vào writable layer có behavior I/O khác hẳn đọc image bất biến.

Điều này giải thích hai production pattern. Thứ nhất, ghi log dung lượng lớn vào filesystem container có thể làm ephemeral storage đầy dù application không lưu “business data”. Thứ hai, workload write-heavy không nên mặc định dùng overlay writable layer như durable storage chỉ vì path nhìn giống filesystem bình thường.

Container packaging và storage durability là hai contract khác nhau.

## 13. UID/GID và quyền file phải được reasoning xuyên image–runtime–volume

`USER 10001` trong image chỉ chọn identity process bên trong user namespace/runtime context. Khi mount volume, file trên volume có owner/mode riêng. Một image chạy tốt trên laptop có thể fail production với `Permission denied` nếu volume được provision với UID/GID khác.

Không nên chữa bằng `chmod 777` hoặc quay lại root theo phản xạ. Hãy xác định process effective UID/GID, ownership của mount, cơ chế `fsGroup`/runtime policy nếu có và ai chịu trách nhiệm initialize permission. Shared volume còn cần xét nhiều process có cùng mapping identity hay không.

Đây là ví dụ abstraction leak giữa image metadata và filesystem authorization thực tế.

## 14. PID 1 có semantics khác process bình thường

Trong Linux, PID 1 có vai trò đặc biệt đối với signal mặc định và reaping orphaned child. Nếu application hoặc shell wrapper trở thành PID 1 nhưng không xử lý child lifecycle, zombie process có thể tích tụ trong workload tạo nhiều subprocess.

Một init nhỏ có thể hữu ích khi application không làm tốt vai trò này, nhưng không nên thêm theo nghi thức. Trước hết cần biết process tree thật, ai spawn child và ai phải `wait()` chúng.

Khi shutdown không hoạt động, kiểm tra signal thực sự tới PID nào và wrapper có dùng `exec` hay không. “Orchestrator đã gửi SIGTERM” chưa chứng minh business process nhận được SIGTERM.

## 15. Memory trong container là tổng footprint theo accounting boundary

Heap chỉ là một phần. Native allocation, thread stack, JIT/code cache, mmap, shared memory và page cache accounting có thể góp vào cgroup memory tùy workload/kernel/runtime. Vì vậy đặt JVM `-Xmx` bằng đúng memory limit gần như không để headroom cho phần còn lại.

Một cách reasoning thực dụng là bắt đầu từ total cgroup usage rồi phân rã xuống runtime heap/native và kernel/file-backed behavior. Nếu container bị OOMKilled nhưng heap chưa đầy, đó không phải mâu thuẫn; hai metric đang đo boundary khác nhau.

CPU cũng tương tự. Application có thể báo CPU utilization vừa phải nhưng cgroup có throttled time cao vì demand vượt quota theo từng period. Tail latency thường nhạy với throttling hơn average CPU chart.

## 16. Image architecture và runtime architecture phải tương thích

Một image có thể được build cho `amd64`, `arm64` hoặc nhiều architecture bằng manifest list/index. Tag giống nhau không có nghĩa bytes executable giống nhau ở mọi node; runtime chọn variant phù hợp architecture.

Điều này quan trọng khi build trên Apple Silicon nhưng production dùng x86, hoặc cluster có node hỗn hợp. Emulation có thể làm build/test “chạy được” nhưng khác performance hoặc native dependency behavior so với execution thật.

Release metadata nên giữ platform/architecture identity khi nó ảnh hưởng artifact. Native library, JNI, Python wheel hoặc binary downloaded trong build là các điểm dễ tạo mismatch.

## 17. Registry availability là dependency của scaling và recovery

Workload đang chạy có thể khỏe khi registry lỗi vì image đã nằm trên node. Nhưng scale-out, node replacement hoặc disaster recovery cần pull image mới. Vì vậy registry là dependency control-plane của capacity/recovery dù không nằm trên request data path bình thường.

Runbook cần phân biệt “application đang phục vụ” với “cluster có khả năng tạo replica mới”. Image pull failure trong lúc node autoscale có thể biến traffic spike thành capacity incident.

Artifact retention cũng là recovery contract. Nếu manifest rollback trỏ digest đã bị garbage-collect khỏi registry, rollback logic đúng trên Git nhưng không thể materialize workload.

## 18. Senior walkthrough: Pod khởi động chậm chỉ sau khi node mới được thêm

Giả sử Pod trên node cũ start trong 5 giây, nhưng Pod trên node mới mất 90 giây. Application init log chỉ mất 4 giây. Phần còn lại nằm trước process startup.

Causal chain nên kiểm tra image pull size/layer cache, registry latency, node egress và volume/network setup. Nếu node cũ đã cache base layer còn node mới phải kéo image 1,5 GiB qua constrained registry/NAT, application không phải bottleneck.

Mitigation có thể là giảm artifact size hợp lý, pre-pull cho workload critical, tăng registry/egress capacity hoặc giữ warm capacity. Bài học không phải “image càng nhỏ càng tốt”, mà là startup SLO phải tính cả distribution path, không chỉ process boot time.

## 19. Image config và runtime override tạo một precedence chain

Image có thể khai báo `ENTRYPOINT`, `CMD`, `ENV`, user và working directory, nhưng orchestrator/runtime có thể override một phần. Khi container chạy khác local, cần xác định **effective runtime config**, không chỉ đọc Dockerfile.

Ví dụ image có `ENTRYPOINT ["java", "-jar", "app.jar"]` nhưng deployment override command sai; hoặc image `USER 10001` nhưng platform security context ép UID khác. Cả hai đều là legitimate composition nhưng source of behavior nằm ở nhiều layer.

Release metadata nên cho operator thấy image digest cùng effective command/env/security context quan trọng. “Image đúng” chưa chứng minh process được khởi động theo contract mong muốn.

## 20. Init container giải sequencing cục bộ, không biến dependency thành healthy

Init container có thể chuẩn bị file, permissions hoặc chờ một prerequisite trước khi main container start. Nhưng dùng loop `until curl database` để “đảm bảo DB sẵn sàng” có thể tạo coupling và startup storm khi dependency outage.

Dependency availability thường là runtime concern cần retry/backoff/degradation, không phải điều kiện phải đúng một lần ở startup. Nếu 500 Pod cùng init-poll dependency mỗi giây khi dependency hồi, chính init logic có thể tạo thundering herd.

Dùng init container khi có finite setup work với completion semantics rõ; không biến nó thành supervisor của mọi external service.

## 21. Startup resource spike khác steady-state usage

Một service có thể cần CPU/memory cao lúc JIT, load model, decompress data hoặc warm cache rồi giảm đáng kể khi steady state. Nếu resource policy chỉ dựa average production, container có thể bị throttled/OOM đúng lúc startup và không bao giờ Ready.

Ngược lại cấp limit theo startup peak cho toàn thời gian có thể lãng phí capacity. Platform cần hiểu workload class: có thể precompute artifact, lazy-load, dùng startup probe, giữ headroom hoặc tách initialization khỏi serving path.

Startup SLO là composition của image distribution + runtime setup + application initialization + readiness, không chỉ “main process đã spawn”.

## 22. Read-only root filesystem cần explicit writable paths

Chạy root filesystem read-only giảm một lớp mutation/attack surface nhưng application vẫn có thể cần `/tmp`, cache hoặc generated file. Nếu không model writable path, workload chỉ fail khi code chạm filesystem ở production.

Pattern tốt là xác định path nào thật sự cần ghi, mount `tmpfs`/ephemeral volume hoặc durable volume theo semantics, rồi giữ phần còn lại read-only. Điều này biến filesystem mutation thành contract có thể review.

Không nên bỏ read-only chỉ vì một library viết temp file mặc định; trước hết xác định data đó cần lifetime/size/security nào và cung cấp đúng storage boundary.

## 23. Container restart che state cục bộ nhưng không sửa external side effect

Restart tạo process/root writable state mới, nên có thể chữa deadlock, memory leak tạm thời hoặc corrupted local cache. Nhưng transaction đã gửi tới database/payment, message đã publish hoặc lock external vẫn tồn tại.

Vì vậy “restart sạch” chỉ đúng cho state nằm trong instance. Runbook phải biết operation nào có side effect ngoài container và idempotency/recovery của chúng. Nếu retry request sau restart mà không có business idempotency, recovery có thể tạo duplicate effect.

Container replaceability là infrastructure property; business statelessness là property khác.

## 24. Image pull policy và cache tạo consistency trade-off

Node cache giúp startup nhanh và giảm registry load. Nhưng nếu deployment dùng mutable tag, behavior có thể phụ thuộc node đã cache bytes nào và pull policy ra sao. Hai Pod cùng tag có khả năng chạy digest khác nếu workflow cho phép tag bị overwrite.

Pin digest loại bỏ ambiguity này: cache chỉ là optimization cho cùng content identity. Với immutable digest, node cache cũ không làm version stale; runtime biết chính xác content cần có.

Đây là lý do artifact immutability làm nhiều operational problem đơn giản hơn, không chỉ supply-chain security.

## 25. Senior walkthrough: chỉ Pod mới restart bị lỗi sau secret/config change

Giả sử fleet cũ vẫn khỏe, nhưng mọi Pod reschedule mới đều fail startup. Image digest giống nhau. Investigation cho thấy runtime inject environment variable/secret revision mới; process cũ chưa restart nên vẫn giữ effective config cũ.

Causal dimension là **instance birth time/config revision**, không phải image version. Nếu operator chỉ rollback image, failure vẫn tiếp tục vì config source không đổi.

Platform nên expose artifact digest + config/secret revision + startup timestamp để cohort mới/cũ dễ phân biệt. Production identity của một instance là composition của artifact và runtime inputs, không chỉ container image.