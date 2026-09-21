# Systemd sâu hơn: unit graph, dependency, resource control và sandboxing

Chương [Quá trình khởi động, systemd và dịch vụ](./systemd_boot_services.md) giới thiệu systemd như trình quản lý vòng đời dịch vụ. Chương này đi sâu hơn vào cách systemd thực sự xây dựng đồ thị phụ thuộc, cách các unit được kích hoạt, cách resource control nối với cgroup, và vì sao nhiều lỗi “service chạy tay được nhưng systemd không chạy” xuất phát từ việc hiểu sai execution context.

## Systemd không chỉ là một công cụ restart service

Systemd là `PID 1` trên nhiều bản phân phối Linux hiện đại. Nó quản lý:

- dependency graph;
- process lifecycle;
- socket activation;
- timer activation;
- mount units;
- logging integration;
- resource controls qua cgroup;
- một phần sandboxing/security policy.

Do đó `systemctl restart app` chỉ là một giao diện nhỏ của toàn bộ hệ thống.

## Unit graph thay cho chuỗi script tuần tự

Mô hình cũ dễ hình dung như:

```text
script A
→ script B
→ sleep 10
→ script C
```

Nhưng cách này không biểu diễn tốt dependency thực và làm boot chậm do tuần tự hóa không cần thiết.

Systemd dùng đồ thị:

```text
network.target ─┐
filesystem.mount ├─→ app.service
secret.mount ────┘
```

Các unit độc lập có thể khởi động song song.

## Quan hệ ordering khác requirement

Đây là điểm gây nhầm rất nhiều.

`After=A` nói rằng nếu A và unit hiện tại cùng có trong transaction, unit hiện tại được start sau A.

`Requires=A` nói A là dependency mạnh; khi unit được start, A cũng được kéo vào.

`Wants=A` tương tự nhưng yếu hơn.

Vì vậy:

```ini
After=network.target
```

không tự động đảm bảo `network.target` được kéo vào, và càng không đảm bảo DNS hay API bên ngoài đã healthy.

## `Before=`

`Before=A` là quan hệ ordering ngược với `After=A`.

Không nên khai báo cả hai chiều gây cycle.

Có thể kiểm tra cycle/dependency bằng:

```bash
systemctl list-dependencies app.service
systemctl list-dependencies --reverse app.service
```

## `Requires=` và failure propagation

Nếu A `Requires=B`, failure của B có thể ảnh hưởng A tùy tình huống activation/lifecycle.

Nhưng dependency semantics không thay thế application-level retry hoặc readiness.

Một database service “active” chưa chắc đã sẵn sàng trả query.

## `Wants=` khi nào phù hợp?

`Wants=` phù hợp với dependency mong muốn nhưng không nên làm unit chính fail nếu dependency phụ không lên được.

Ví dụ observability sidecar hoặc optional cache có thể phù hợp tùy architecture.

## `BindsTo=`

`BindsTo=` tạo quan hệ lifecycle chặt hơn, thường dùng khi unit phải dừng nếu dependency biến mất.

Không nên dùng tràn lan; lifecycle coupling quá mạnh có thể tạo cascading failure.

## `PartOf=`

`PartOf=` hữu ích khi muốn restart/stop một parent-like unit kéo theo unit khác.

Ví dụ một nhóm service có thể được tổ chức để restart cùng nhau.

## `Conflicts=`

Một số unit không thể active đồng thời.

`Conflicts=` biểu diễn quan hệ loại trừ.

Ví dụ hai implementation cạnh tranh cùng một resource có thể được cấu hình để không cùng chạy.

## Target unit

Target không chạy business logic. Nó nhóm và đồng bộ các unit khác.

Ví dụ:

```bash
systemctl list-dependencies multi-user.target
```

Target gần với “mốc trạng thái hệ thống” hơn là service.

## Activation transaction

Khi yêu cầu:

```bash
systemctl start app.service
```

systemd không đơn giản gọi `ExecStart`. Nó xây một transaction gồm các unit được kéo vào bởi dependency, kiểm tra ordering, job conflicts và sau đó thực thi theo graph.

Đây là lý do một unit file nhỏ có thể kéo theo rất nhiều operations.

## Socket activation

Systemd có thể mở listening socket trước rồi chỉ start service khi traffic tới.

Ví dụ conceptual:

```text
client
  ↓
app.socket (socket do systemd giữ)
  ↓
app.service được kích hoạt
  ↓
socket FD được truyền cho service
```

Lợi ích:

- service có thể start on demand;
- socket có thể tồn tại sớm trong boot;
- một số restart có thể giảm khoảng trống listener.

Nhưng application phải hỗ trợ socket activation semantics.

## Timer activation

Timer unit tách lịch khỏi business process.

Ví dụ:

```ini
[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true
```

Timer kích hoạt service unit riêng.

Điều này giúp job có logging, identity, resource limit và sandbox giống service bình thường.

## Path activation

Systemd còn có `.path` unit để kích hoạt service khi path/file thay đổi theo một số điều kiện.

Đây là event-driven alternative cho polling loop trong một số use case.

## Service `Type=`

`Type=` ảnh hưởng cách systemd xác định service đã khởi động.

Một số kiểu phổ biến:

- `simple` — process từ `ExecStart` được coi là main process gần như ngay lập tức;
- `exec` — giống simple nhưng systemd chờ `execve()` thành công;
- `forking` — daemon fork rồi parent exit;
- `oneshot` — command chạy xong rồi unit có thể chuyển trạng thái phù hợp;
- `notify` — service chủ động báo READY cho systemd;
- `dbus` — readiness gắn với D-Bus name.

Chọn sai `Type=` có thể làm systemd nghĩ service healthy quá sớm hoặc theo dõi sai process.

## `Type=notify` và readiness tốt hơn

Nếu application hỗ trợ `sd_notify`, nó có thể báo:

```text
READY=1
```

chỉ sau khi đã hoàn tất initialization.

Điều này chính xác hơn `sleep 10` hoặc đoán readiness từ process existence.

## Main PID

Systemd phải biết process nào là main process để theo dõi lifecycle.

```bash
systemctl show app -p MainPID
```

Nếu daemon double-fork hoặc wrapper shell không dùng `exec`, systemd có thể theo dõi process không như mong muốn.

## Vì sao shell wrapper nên dùng `exec` trong một số tình huống?

Ví dụ script:

```bash
#!/usr/bin/env bash
java -jar app.jar
```

shell process giữ vai trò parent.

Nếu viết:

```bash
exec java -jar app.jar
```

shell được thay bằng Java process. Signal/lifecycle thường đơn giản hơn.

Không phải mọi script đều cần `exec`, nhưng cần hiểu process tree.

## `ExecStartPre=` và `ExecStartPost=`

Có thể dùng để thực hiện bước trước/sau start:

```ini
ExecStartPre=/usr/bin/test -f /opt/app/app.jar
ExecStart=/usr/bin/java -jar /opt/app/app.jar
ExecStartPost=/usr/local/bin/register-service.sh
```

Không nên biến unit file thành một deployment script dài. Những bước có transactional logic phức tạp thường nên nằm ngoài service startup.

## `ExecCondition=`

`ExecCondition=` cho phép kiểm tra điều kiện trước start với semantics riêng.

Nó hữu ích để tránh start unit khi precondition không đúng mà không coi mọi trường hợp là failure.

## Environment

Systemd không tự đọc `.bashrc` hoặc `.profile` giống interactive login shell.

Có thể dùng:

```ini
Environment=SPRING_PROFILES_ACTIVE=prod
EnvironmentFile=/etc/app/app.env
```

Nhưng secret management cần cẩn thận: environment có thể lộ qua debugging, dump hoặc quyền đọc process state tùy hệ thống.

## Working directory

```ini
WorkingDirectory=/opt/app
```

Nếu ứng dụng dùng relative path mà không khai báo working directory, service có thể tìm file sai chỗ.

Tốt hơn nữa là application dùng absolute/configured paths cho dữ liệu quan trọng.

## `User=` và `Group=`

```ini
User=app
Group=app
```

Systemd thiết lập credentials trước khi exec process.

Đây là lý do command chạy bằng root trong SSH có thể thành công nhưng service user lại bị permission denied.

## Supplementary groups

Có thể dùng:

```ini
SupplementaryGroups=appops
```

khi service cần thêm group access.

Không nên thêm process vào quá nhiều group vì mở rộng privilege surface.

## `UMask=`

Systemd có thể đặt `UMask=` riêng cho service.

Điều này ảnh hưởng mode của file mới được tạo.

```ini
UMask=0027
```

Nếu app tạo log/config với permission khác khi chạy tay và khi chạy service, đây là một điểm cần kiểm tra.

## Resource limits kiểu POSIX

Systemd hỗ trợ các limit như:

```ini
LimitNOFILE=65535
LimitNPROC=4096
```

Những giá trị này tương ứng với resource limit của process.

Kiểm tra runtime:

```bash
cat /proc/<PID>/limits
```

Đừng chỉ nhìn unit file; cần verify process thực tế nhận giá trị gì.

## Cgroup resource control

Systemd tổ chức services vào cgroups.

Có thể dùng các directive như:

```ini
MemoryMax=4G
MemoryHigh=3G
CPUQuota=200%
TasksMax=4096
```

`CPUQuota=200%` thường tương đương tối đa khoảng hai logical CPUs worth of CPU time trong period phù hợp, không phải “được gắn riêng 2 CPU vật lý”.

## `MemoryMax=`

Nếu service vượt `MemoryMax`, cgroup OOM có thể xảy ra dù host còn RAM.

Kiểm tra:

```bash
systemctl show app -p MemoryCurrent -p MemoryMax
```

hoặc cgroup files tương ứng.

## `MemoryHigh=`

`MemoryHigh` tạo pressure/throttling trước hard kill ở `MemoryMax`.

Nó hữu ích để tạo soft boundary nhưng có thể làm latency tăng khi reclaim.

## `TasksMax=`

Giới hạn số tasks/threads trong cgroup.

Java app tạo quá nhiều threads có thể chạm limit dù `ulimit -u` nhìn còn cao.

## Restart policy sâu hơn

Các giá trị thường gặp:

```ini
Restart=no
Restart=on-failure
Restart=always
Restart=on-abnormal
```

Cần kết hợp với:

```ini
RestartSec=5s
StartLimitIntervalSec=60
StartLimitBurst=5
```

Nếu service fail ngay lập tức và `Restart=always`, restart storm có thể gây log storm hoặc tải dependency.

## Exit status nào được coi là success?

Có thể điều chỉnh:

```ini
SuccessExitStatus=143
```

nhưng chỉ nên làm khi hiểu application signal/exit semantics.

Ví dụ JVM nhận SIGTERM không nhất thiết luôn trả 143 tùy wrapper/runtime.

## Timeout khi start/stop

```ini
TimeoutStartSec=60
TimeoutStopSec=30
```

Nếu shutdown cần drain traffic lâu hơn timeout, systemd có thể escalate sang kill.

Đây là lý do graceful shutdown của Spring/Kubernetes/systemd phải được thiết kế đồng bộ.

## Kill mode

Systemd có `KillMode=` để quyết định signal gửi cho process nào trong cgroup.

`control-group` thường giúp dừng toàn bộ process con còn lại.

Nếu chọn sai, child process có thể bị orphan hoặc sống sau khi service tưởng đã stop.

## Watchdog

Một service hỗ trợ watchdog có thể gửi heartbeat cho systemd.

Nếu heartbeat dừng, systemd coi service unhealthy và có thể restart.

Watchdog khác health endpoint: nó đo việc process còn phản hồi theo protocol với service manager.

## Sandboxing với systemd

Systemd cung cấp nhiều directive để giảm privilege:

```ini
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
PrivateDevices=true
RestrictSUIDSGID=true
CapabilityBoundingSet=
```

Không nên bật toàn bộ rồi hy vọng application vẫn chạy. Mỗi directive thay đổi execution environment và cần test.

## `NoNewPrivileges=`

Khi bật, process và descendants không thể đạt thêm privilege qua `execve()` theo một số cơ chế như setuid/capabilities.

Đây là control quan trọng để giảm privilege escalation.

## `ProtectSystem=`

Có thể làm nhiều phần filesystem read-only trong namespace của service.

Ứng dụng cần write path phải được mở riêng bằng directives như `ReadWritePaths=`.

## `PrivateTmp=`

Service nhận `/tmp` và `/var/tmp` riêng trong mount namespace.

Nếu hai service trước đây trao đổi file qua `/tmp`, bật `PrivateTmp` có thể phá integration đó.

## `PrivateDevices=`

Giảm access tới device nodes.

Phù hợp nhiều daemon không cần hardware access trực tiếp.

## Capability bounding

Thay vì full root, có thể giới hạn capabilities:

```ini
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
AmbientCapabilities=CAP_NET_BIND_SERVICE
```

Điều này cho phép app bind low port mà không giữ toàn bộ root privilege trong một số mô hình.

## `DynamicUser=`

Systemd có thể tạo user runtime tạm thời cho service.

Hữu ích với daemon không cần persistent UID, nhưng cần hiểu ownership của persistent files trước khi dùng.

## `systemd-analyze security`

Có thể đánh giá một số hardening options:

```bash
systemd-analyze security app.service
```

Điểm số không phải chân lý. Tool chỉ đánh giá theo một tập heuristic; security thật còn phụ thuộc application và threat model.

## Drop-in override

Thay vì sửa trực tiếp unit do package quản lý:

```bash
sudo systemctl edit app.service
```

systemd tạo drop-in override dưới `/etc/systemd/system/...`.

Điều này tốt hơn vì package upgrade ít ghi đè customization.

Kiểm tra merged config:

```bash
systemctl cat app.service
```

## `daemon-reload` khác restart

Sau khi sửa unit definition:

```bash
sudo systemctl daemon-reload
```

systemd đọc lại metadata unit.

Nhưng process đang chạy chưa tự thay đổi.

Sau đó tùy thay đổi có thể cần restart/reload service.

## Mask

```bash
sudo systemctl mask app.service
```

mask thường tạo liên kết tới `/dev/null` để ngăn unit được start kể cả gián tiếp.

`disable` chỉ bỏ enablement relationship; `mask` mạnh hơn.

## Transient unit

Có thể chạy command tạm dưới systemd:

```bash
systemd-run --unit=test-job --property=MemoryMax=1G /usr/local/bin/job.sh
```

Đây là cách hay để áp resource control cho task không cần tạo unit file cố định.

## Scope unit

Interactive process có thể được group trong `.scope` unit.

Desktop session/container manager thường tận dụng scope/service hierarchy để tổ chức cgroups.

## Journal metadata theo unit

Systemd-journald gắn metadata như `_SYSTEMD_UNIT`, PID, UID vào log.

Do đó:

```bash
journalctl -u app.service
```

lọc theo metadata, không chỉ grep text.

## Một case production: service “active” nhưng chưa ready

Systemd `active` chỉ phản ánh lifecycle theo `Type=`.

Nếu Spring Boot mất 30 giây để warm cache nhưng unit `Type=simple`, systemd có thể coi active ngay khi JVM start.

Load balancer cần readiness riêng.

Giải pháp có thể là:

- application-level readiness endpoint;
- `Type=notify` nếu hỗ trợ;
- orchestration readiness probe;
- dependency consumer có retry/backoff.

## Một case: service restart loop làm disk đầy

Chuỗi:

```text
config sai
→ service exit ngay
→ Restart=always
→ start lại liên tục
→ log tăng nhanh
→ journal/file log đầy disk
```

Điều tra:

```bash
systemctl status app
journalctl -u app --since '-10 min'
systemctl show app -p NRestarts
```

Sau đó fix root cause và restart policy/rate limit phù hợp.

## Một case: chạy tay được nhưng service không chạy

So sánh:

```bash
# interactive shell
env
pwd
ulimit -a
id

# systemd view
systemctl show app -p User -p Group -p Environment -p WorkingDirectory -p LimitNOFILE
```

Các khác biệt thường nằm ở:

- identity;
- PATH/JAVA_HOME;
- working directory;
- file permissions;
- resource limits;
- sandboxing directives.

## Mô hình tư duy

Hãy nhìn systemd theo bốn lớp:

```text
unit graph
   ↓
execution context
   ↓
process/cgroup lifecycle
   ↓
resource + security policy
```

`systemctl` chỉ là client điều khiển bốn lớp này.

## Những hiểu lầm phổ biến

**“After=network.target nghĩa mạng đã dùng được.”** Không; đó chỉ là ordering tương đối với một target.

**“Service active nghĩa ứng dụng healthy.”** Không; readiness/business health là lớp khác.

**“LimitNOFILE trong shell áp cho systemd service.”** Không nhất thiết; systemd có limit riêng.

**“Restart=always tăng reliability.”** Có thể tạo restart storm nếu failure persistent.

**“Bật mọi hardening directive luôn tốt.”** Có thể phá application; cần threat model và test.

**“disable ngăn service start hoàn toàn.”** `mask` mới là cơ chế mạnh hơn cho mục tiêu đó.

## Kết nối kiến thức

Đọc [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md) để hiểu resource/security primitives phía dưới systemd, [Bảo mật và gia cố](../08_operations/security_hardening.md) để hiểu threat model, và [Deployment/rollback](../08_operations/deployment_release_rollback.md) để nối lifecycle service với release process.