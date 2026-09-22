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