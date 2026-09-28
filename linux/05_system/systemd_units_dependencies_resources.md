# Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing

> **Mạch đọc:** Đọc **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Systemd không chỉ là một công cụ restart dịch vụ (service / 서비스)** sang **đơn vị (unit / 단위) đồ thị (graph / 그래프) thay cho chuỗi script tuần tự**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Chương [Quá trình khởi động, systemd và dịch vụ](./systemd_boot_services.md) giới thiệu systemd như trình quản lý vòng đời dịch vụ. Chương này đi sâu hơn vào cách systemd thực sự xây dựng đồ thị phụ thuộc, cách các đơn vị (unit / 단위) được kích hoạt, cách tài nguyên (resource / 자원) điều khiển (control / 제어) nối với cgroup, và vì sao nhiều lỗi “dịch vụ (service / 서비스) chạy tay được nhưng systemd không chạy” xuất phát từ việc hiểu sai thực thi (execution / 실행) ngữ cảnh (context / 맥락).

## Systemd không chỉ là một công cụ restart dịch vụ (service / 서비스)

Systemd là `PID 1` trên nhiều bản phân phối Linux hiện đại. Nó quản lý:

- phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프);
- tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기);
- socket activation;
- timer activation;
- mount units;
- logging tích hợp (integration / 통합);
- tài nguyên (resource / 자원) controls qua cgroup;
- một phần sandboxing/bảo mật (security / 보안) chính sách (policy / 정책).

Do đó `systemctl restart app` chỉ là một giao diện nhỏ của toàn bộ hệ thống.

## Đơn vị (unit / 단위) đồ thị (graph / 그래프) thay cho chuỗi script tuần tự

Mô hình cũ dễ hình dung như:

```text
script A
→ script B
→ sleep 10
→ script C
```

Nhưng cách này không biểu diễn tốt phụ thuộc (dependency / 의존성) thực và làm boot chậm do tuần tự hóa không cần thiết.

Systemd dùng đồ thị:

```text
network.target ─┐
filesystem.mount ├─→ app.service
secret.mount ────┘
```

Các đơn vị (unit / 단위) độc lập có thể khởi động song song.

## Quan hệ thứ tự (ordering / 순서) khác yêu cầu (requirement / 요구사항)

Đây là điểm gây nhầm rất nhiều.

`After=A` nói rằng nếu A và đơn vị (unit / 단위) hiện tại cùng có trong giao dịch (transaction / 트랜잭션), đơn vị (unit / 단위) hiện tại được start sau A.

`Requires=A` nói A là phụ thuộc (dependency / 의존성) mạnh; khi đơn vị (unit / 단위) được start, A cũng được kéo vào.

`Wants=A` tương tự nhưng yếu hơn.

Vì vậy:

```ini
After=network.target
```

không tự động đảm bảo `network.target` được kéo vào, và càng không đảm bảo DNS hay API bên ngoài đã healthy.

## `Before=`

`Before=A` là quan hệ thứ tự (ordering / 순서) ngược với `After=A`.

Không nên khai báo cả hai chiều gây cycle.

Có thể kiểm tra cycle/phụ thuộc (dependency / 의존성) bằng:

```bash
systemctl list-dependencies app.service
systemctl list-dependencies --reverse app.service
```

## `Requires=` và thất bại (failure / 실패) propagation

Nếu A `Requires=B`, thất bại (failure / 실패) của B có thể ảnh hưởng A tùy tình huống activation/vòng đời (lifecycle / 생명주기).

Nhưng phụ thuộc (dependency / 의존성) ngữ nghĩa (semantics / 의미론) không thay thế application-level thử lại (retry / 재시도) hoặc readiness.

Một cơ sở dữ liệu (database / 데이터베이스) dịch vụ (service / 서비스) “active” chưa chắc đã sẵn sàng trả truy vấn (query / 쿼리).

## `Wants=` khi nào phù hợp?

`Wants=` phù hợp với phụ thuộc (dependency / 의존성) mong muốn nhưng không nên làm đơn vị (unit / 단위) chính thất bại (fail / 실패) nếu phụ thuộc (dependency / 의존성) phụ không lên được.

Ví dụ khả năng quan sát (observability / 관측 가능성) sidecar hoặc optional bộ nhớ đệm (cache / 캐시) có thể phù hợp tùy kiến trúc (architecture / 아키텍처).

## `BindsTo=`

`BindsTo=` tạo quan hệ vòng đời (lifecycle / 생명주기) chặt hơn, thường dùng khi đơn vị (unit / 단위) phải dừng nếu phụ thuộc (dependency / 의존성) biến mất.

Không nên dùng tràn lan; vòng đời (lifecycle / 생명주기) coupling quá mạnh có thể tạo cascading thất bại (failure / 실패).

## `PartOf=`

`PartOf=` hữu ích khi muốn restart/stop một parent-like đơn vị (unit / 단위) kéo theo đơn vị (unit / 단위) khác.

Ví dụ một nhóm dịch vụ (service / 서비스) có thể được tổ chức để restart cùng nhau.

## `Conflicts=`

Một số đơn vị (unit / 단위) không thể active đồng thời.

`Conflicts=` biểu diễn quan hệ loại trừ.

Ví dụ hai hiện thực (implementation / 구현) cạnh tranh cùng một tài nguyên (resource / 자원) có thể được cấu hình để không cùng chạy.

## Mục tiêu (target / 대상) đơn vị (unit / 단위)

Mục tiêu (target / 대상) không chạy lô-gic nghiệp vụ (business logic / 비즈니스 로직). Nó nhóm và đồng bộ các đơn vị (unit / 단위) khác.

Ví dụ:

```bash
systemctl list-dependencies multi-user.target
```

Mục tiêu (target / 대상) gần với “mốc trạng thái hệ thống” hơn là dịch vụ (service / 서비스).

## Activation giao dịch (transaction / 트랜잭션)

Khi yêu cầu:

```bash
systemctl start app.service
```

systemd không đơn giản gọi `ExecStart`. Nó xây một giao dịch (transaction / 트랜잭션) gồm các đơn vị (unit / 단위) được kéo vào bởi phụ thuộc (dependency / 의존성), kiểm tra thứ tự (ordering / 순서), job conflicts và sau đó thực thi theo đồ thị (graph / 그래프).

Đây là lý do một đơn vị (unit / 단위) tệp (file / 파일) nhỏ có thể kéo theo rất nhiều operations.

## Socket activation

Systemd có thể mở listening socket trước rồi chỉ start dịch vụ (service / 서비스) khi traffic tới.

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

- dịch vụ (service / 서비스) có thể start on demand;
- socket có thể tồn tại sớm trong boot;
- một số restart có thể giảm khoảng trống listener.

Nhưng ứng dụng (application / 애플리케이션) phải hỗ trợ socket activation ngữ nghĩa (semantics / 의미론).

## Timer activation

Timer đơn vị (unit / 단위) tách lịch khỏi nghiệp vụ (business / 비즈니스) tiến trình (process / 프로세스).

Ví dụ:

```ini
[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true
```

Timer kích hoạt dịch vụ (service / 서비스) đơn vị (unit / 단위) riêng.

Điều này giúp job có logging, định danh (identity / 식별자), tài nguyên (resource / 자원) limit và sandbox giống dịch vụ (service / 서비스) bình thường.

## Đường dẫn (path / 경로) activation

Systemd còn có `.path` đơn vị (unit / 단위) để kích hoạt dịch vụ (service / 서비스) khi đường dẫn (path / 경로)/tệp (file / 파일) thay đổi theo một số điều kiện.

Đây là event-driven alternative cho polling vòng lặp (loop / 루프) trong một số use trường hợp (case / 사례).

## Dịch vụ (service / 서비스) `Type=`

`Type=` ảnh hưởng cách systemd xác định dịch vụ (service / 서비스) đã khởi động.

Một số kiểu phổ biến:

- `simple` — tiến trình (process / 프로세스) từ `ExecStart` được coi là main tiến trình (process / 프로세스) gần như ngay lập tức;
- `exec` — giống simple nhưng systemd chờ `execve()` thành công;
- `forking` — daemon fork rồi parent exit;
- `oneshot` — command chạy xong rồi đơn vị (unit / 단위) có thể chuyển trạng thái phù hợp;
- `notify` — dịch vụ (service / 서비스) chủ động báo READY cho systemd;
- `dbus` — readiness gắn với D-Bus name.

Chọn sai `Type=` có thể làm systemd nghĩ dịch vụ (service / 서비스) healthy quá sớm hoặc theo dõi sai tiến trình (process / 프로세스).

## `Type=notify` và readiness tốt hơn

Nếu ứng dụng (application / 애플리케이션) hỗ trợ `sd_notify`, nó có thể báo:

```text
READY=1
```

chỉ sau khi đã hoàn tất initialization.

Điều này chính xác hơn `sleep 10` hoặc đoán readiness từ tiến trình (process / 프로세스) existence.

## Main PID

Systemd phải biết tiến trình (process / 프로세스) nào là main tiến trình (process / 프로세스) để theo dõi vòng đời (lifecycle / 생명주기).

```bash
systemctl show app -p MainPID
```

Nếu daemon double-fork hoặc wrapper shell không dùng `exec`, systemd có thể theo dõi tiến trình (process / 프로세스) không như mong muốn.

## Vì sao shell wrapper nên dùng `exec` trong một số tình huống?

Ví dụ script:

```bash
#!/usr/bin/env bash
java -jar app.jar
```

shell tiến trình (process / 프로세스) giữ vai trò parent.

Nếu viết:

```bash
exec java -jar app.jar
```

shell được thay bằng Java tiến trình (process / 프로세스). tín hiệu (signal / 신호)/vòng đời (lifecycle / 생명주기) thường đơn giản hơn.

Không phải mọi script đều cần `exec`, nhưng cần hiểu tiến trình (process / 프로세스) cây (tree / 트리).

## `ExecStartPre=` và `ExecStartPost=`

Có thể dùng để thực hiện bước trước/sau start:

```ini
ExecStartPre=/usr/bin/test -f /opt/app/app.jar
ExecStart=/usr/bin/java -jar /opt/app/app.jar
ExecStartPost=/usr/local/bin/register-service.sh
```

Không nên biến đơn vị (unit / 단위) tệp (file / 파일) thành một triển khai (deployment / 배포) script dài. Những bước có transactional lô-gic (logic / 논리) phức tạp thường nên nằm ngoài dịch vụ (service / 서비스) startup.

## `ExecCondition=`

`ExecCondition=` cho phép kiểm tra điều kiện trước start với ngữ nghĩa (semantics / 의미론) riêng.

Nó hữu ích để tránh start đơn vị (unit / 단위) khi precondition không đúng mà không coi mọi trường hợp là thất bại (failure / 실패).

## Môi trường (environment / 환경)

Systemd không tự đọc `.bashrc` hoặc `.profile` giống interactive login shell.

Có thể dùng:

```ini
Environment=SPRING_PROFILES_ACTIVE=prod
EnvironmentFile=/etc/app/app.env
```

Nhưng secret management cần cẩn thận: môi trường (environment / 환경) có thể lộ qua debugging, dump hoặc quyền đọc tiến trình (process / 프로세스) trạng thái (state / 상태) tùy hệ thống.

## Working directory

```ini
WorkingDirectory=/opt/app
```

Nếu ứng dụng dùng relative đường dẫn (path / 경로) mà không khai báo working directory, dịch vụ (service / 서비스) có thể tìm tệp (file / 파일) sai chỗ.

Tốt hơn nữa là ứng dụng (application / 애플리케이션) dùng absolute/configured paths cho dữ liệu quan trọng.

## `User=` và `Group=`

```ini
User=app
Group=app
```

Systemd thiết lập credentials trước khi exec tiến trình (process / 프로세스).

Đây là lý do command chạy bằng gốc (root / 루트) trong SSH có thể thành công nhưng dịch vụ (service / 서비스) người dùng (user / 사용자) lại bị permission denied.

## Supplementary groups

Có thể dùng:

```ini
SupplementaryGroups=appops
```

khi dịch vụ (service / 서비스) cần thêm group truy cập (access / 접근).

Không nên thêm tiến trình (process / 프로세스) vào quá nhiều group vì mở rộng privilege surface.

## `UMask=`

Systemd có thể đặt `UMask=` riêng cho dịch vụ (service / 서비스).

Điều này ảnh hưởng chế độ (mode / 모드) của tệp (file / 파일) mới được tạo.

```ini
UMask=0027
```

Nếu app tạo log/cấu hình (config / 설정) với permission khác khi chạy tay và khi chạy dịch vụ (service / 서비스), đây là một điểm cần kiểm tra.

## Tài nguyên (resource / 자원) limits kiểu POSIX

Systemd hỗ trợ các limit như:

```ini
LimitNOFILE=65535
LimitNPROC=4096
```

Những giá trị này tương ứng với tài nguyên (resource / 자원) limit của tiến trình (process / 프로세스).

Kiểm tra thời gian chạy (runtime / 런타임):

```bash
cat /proc/<PID>/limits
```

Đừng chỉ nhìn đơn vị (unit / 단위) tệp (file / 파일); cần verify tiến trình (process / 프로세스) thực tế nhận giá trị gì.

## Cgroup tài nguyên (resource / 자원) điều khiển (control / 제어)

Systemd tổ chức services vào cgroups.

Có thể dùng các directive như:

```ini
MemoryMax=4G
MemoryHigh=3G
CPUQuota=200%
TasksMax=4096
```

`CPUQuota=200%` thường tương đương tối đa khoảng hai logical CPUs worth of CPU thời gian (time / 시간) trong period phù hợp, không phải “được gắn riêng 2 CPU vật lý”.

## `MemoryMax=`

Nếu dịch vụ (service / 서비스) vượt `MemoryMax`, cgroup OOM có thể xảy ra dù host còn RAM.

Kiểm tra:

```bash
systemctl show app -p MemoryCurrent -p MemoryMax
```

hoặc cgroup files tương ứng.

## `MemoryHigh=`

`MemoryHigh` tạo pressure/throttling trước hard kill ở `MemoryMax`.

Nó hữu ích để tạo soft ranh giới (boundary / 경계) nhưng có thể làm độ trễ (latency / 지연 시간) tăng khi reclaim.

## `TasksMax=`

Giới hạn số tasks/threads trong cgroup.

Java app tạo quá nhiều threads có thể chạm limit dù `ulimit -u` nhìn còn cao.

## Restart chính sách (policy / 정책) sâu hơn

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

Nếu dịch vụ (service / 서비스) thất bại (fail / 실패) ngay lập tức và `Restart=always`, restart storm có thể gây log storm hoặc tải phụ thuộc (dependency / 의존성).

## Exit status nào được coi là success?

Có thể điều chỉnh:

```ini
SuccessExitStatus=143
```

nhưng chỉ nên làm khi hiểu ứng dụng (application / 애플리케이션) tín hiệu (signal / 신호)/exit ngữ nghĩa (semantics / 의미론).

Ví dụ JVM nhận SIGTERM không nhất thiết luôn trả 143 tùy wrapper/thời gian chạy (runtime / 런타임).

## Hết thời gian chờ (timeout / 타임아웃) khi start/stop

```ini
TimeoutStartSec=60
TimeoutStopSec=30
```

Nếu shutdown cần drain traffic lâu hơn hết thời gian chờ (timeout / 타임아웃), systemd có thể escalate sang kill.

Đây là lý do graceful shutdown của Spring/Kubernetes/systemd phải được thiết kế đồng bộ.

## Kill chế độ (mode / 모드)

Systemd có `KillMode=` để quyết định tín hiệu (signal / 신호) gửi cho tiến trình (process / 프로세스) nào trong cgroup.

`control-group` thường giúp dừng toàn bộ tiến trình (process / 프로세스) con còn lại.

Nếu chọn sai, child tiến trình (process / 프로세스) có thể bị orphan hoặc sống sau khi dịch vụ (service / 서비스) tưởng đã stop.

## Watchdog

Một dịch vụ (service / 서비스) hỗ trợ watchdog có thể gửi heartbeat cho systemd.

Nếu heartbeat dừng, systemd coi dịch vụ (service / 서비스) unhealthy và có thể restart.

Watchdog khác health endpoint: nó đo việc tiến trình (process / 프로세스) còn phản hồi theo giao thức (protocol / 프로토콜) với dịch vụ (service / 서비스) manager.

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

Không nên bật toàn bộ rồi hy vọng ứng dụng (application / 애플리케이션) vẫn chạy. Mỗi directive thay đổi thực thi (execution / 실행) môi trường (environment / 환경) và cần kiểm thử (test / 테스트).

## `NoNewPrivileges=`

Khi bật, tiến trình (process / 프로세스) và descendants không thể đạt thêm privilege qua `execve()` theo một số cơ chế như setuid/capabilities.

Đây là điều khiển (control / 제어) quan trọng để giảm privilege escalation.

## `ProtectSystem=`

Có thể làm nhiều phần filesystem read-only trong không gian tên (namespace / 네임스페이스) của dịch vụ (service / 서비스).

Ứng dụng cần ghi (write / 쓰기) đường dẫn (path / 경로) phải được mở riêng bằng directives như `ReadWritePaths=`.

## `PrivateTmp=`

Dịch vụ (service / 서비스) nhận `/tmp` và `/var/tmp` riêng trong mount không gian tên (namespace / 네임스페이스).

Nếu hai dịch vụ (service / 서비스) trước đây trao đổi tệp (file / 파일) qua `/tmp`, bật `PrivateTmp` có thể phá tích hợp (integration / 통합) đó.

## `PrivateDevices=`

Giảm truy cập (access / 접근) tới thiết bị (device / 장치) nodes.

Phù hợp nhiều daemon không cần hardware truy cập (access / 접근) trực tiếp.

## Năng lực (capability / 역량) bounding

Thay vì full gốc (root / 루트), có thể giới hạn capabilities:

```ini
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
AmbientCapabilities=CAP_NET_BIND_SERVICE
```

Điều này cho phép app bind low cổng (port / 포트) mà không giữ toàn bộ gốc (root / 루트) privilege trong một số mô hình.

## `DynamicUser=`

Systemd có thể tạo người dùng (user / 사용자) thời gian chạy (runtime / 런타임) tạm thời cho dịch vụ (service / 서비스).

Hữu ích với daemon không cần persistent UID, nhưng cần hiểu quyền sở hữu (ownership / 소유권) của persistent files trước khi dùng.

## `systemd-analyze security`

Có thể đánh giá một số hardening options:

```bash
systemd-analyze security app.service
```

Điểm số không phải chân lý. công cụ (tool / 도구) chỉ đánh giá theo một tập heuristic; bảo mật (security / 보안) thật còn phụ thuộc ứng dụng (application / 애플리케이션) và threat mô hình (model / 모델).

## Drop-in override

Thay vì sửa trực tiếp đơn vị (unit / 단위) do gói (package / 패키지) quản lý:

```bash
sudo systemctl edit app.service
```

systemd tạo drop-in override dưới `/etc/systemd/system/...`.

Điều này tốt hơn vì gói (package / 패키지) upgrade ít ghi đè customization.

Kiểm tra merged cấu hình (config / 설정):

```bash
systemctl cat app.service
```

## `daemon-reload` khác restart

Sau khi sửa đơn vị (unit / 단위) definition:

```bash
sudo systemctl daemon-reload
```

systemd đọc lại siêu dữ liệu (metadata / 메타데이터) đơn vị (unit / 단위).

Nhưng tiến trình (process / 프로세스) đang chạy chưa tự thay đổi.

Sau đó tùy thay đổi có thể cần restart/reload dịch vụ (service / 서비스).

## Mask

```bash
sudo systemctl mask app.service
```

mask thường tạo liên kết tới `/dev/null` để ngăn đơn vị (unit / 단위) được start kể cả gián tiếp.

`disable` chỉ bỏ enablement relationship; `mask` mạnh hơn.

## Transient đơn vị (unit / 단위)

Có thể chạy command tạm dưới systemd:

```bash
systemd-run --unit=test-job --property=MemoryMax=1G /usr/local/bin/job.sh
```

Đây là cách hay để áp tài nguyên (resource / 자원) điều khiển (control / 제어) cho tác vụ (task / 작업) không cần tạo đơn vị (unit / 단위) tệp (file / 파일) cố định.

## Phạm vi (scope / 범위) đơn vị (unit / 단위)

Interactive tiến trình (process / 프로세스) có thể được group trong `.scope` đơn vị (unit / 단위).

Desktop session/bộ chứa (container / 컨테이너) manager thường tận dụng phạm vi (scope / 범위)/dịch vụ (service / 서비스) hierarchy để tổ chức cgroups.

## Journal siêu dữ liệu (metadata / 메타데이터) theo đơn vị (unit / 단위)

Systemd-journald gắn siêu dữ liệu (metadata / 메타데이터) như `_SYSTEMD_UNIT`, PID, UID vào log.

Do đó:

```bash
journalctl -u app.service
```

lọc theo siêu dữ liệu (metadata / 메타데이터), không chỉ grep văn bản (text / 텍스트).

## Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): dịch vụ (service / 서비스) “active” nhưng chưa ready

Systemd `active` chỉ phản ánh vòng đời (lifecycle / 생명주기) theo `Type=`.

Nếu Spring Boot mất 30 giây để warm bộ nhớ đệm (cache / 캐시) nhưng đơn vị (unit / 단위) `Type=simple`, systemd có thể coi active ngay khi JVM start.

Bộ cân bằng tải (load balancer / 로드 밸런서) cần readiness riêng.

Giải pháp có thể là:

- application-level readiness endpoint;
- `Type=notify` nếu hỗ trợ;
- orchestration readiness probe;
- phụ thuộc (dependency / 의존성) bên tiêu thụ (consumer / 소비자) có thử lại (retry / 재시도)/backoff.

## Một trường hợp (case / 사례): dịch vụ (service / 서비스) restart vòng lặp (loop / 루프) làm disk đầy

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

Sau đó fix nguyên nhân gốc (root cause / 근본 원인) và restart chính sách (policy / 정책)/tỷ lệ (rate / 비율) limit phù hợp.

## Một trường hợp (case / 사례): chạy tay được nhưng dịch vụ (service / 서비스) không chạy

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

- định danh (identity / 식별자);
- đường dẫn (path / 경로)/JAVA_HOME;
- working directory;
- tệp (file / 파일) permissions;
- tài nguyên (resource / 자원) limits;
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

`systemctl` chỉ là máy khách (client / 클라이언트) điều khiển bốn lớp này.

## Những hiểu lầm phổ biến

**“After=mạng (network / 네트워크).mục tiêu (target / 대상) nghĩa mạng đã dùng được.”** Không; đó chỉ là thứ tự (ordering / 순서) tương đối với một mục tiêu (target / 대상).

**“dịch vụ (service / 서비스) active nghĩa ứng dụng healthy.”** Không; readiness/nghiệp vụ (business / 비즈니스) health là lớp khác.

**“LimitNOFILE trong shell áp cho systemd dịch vụ (service / 서비스).”** Không nhất thiết; systemd có limit riêng.

**“Restart=always tăng độ tin cậy (reliability / 신뢰성).”** Có thể tạo restart storm nếu thất bại (failure / 실패) persistent.

**“Bật mọi hardening directive luôn tốt.”** Có thể phá ứng dụng (application / 애플리케이션); cần threat mô hình (model / 모델) và kiểm thử (test / 테스트).

**“disable ngăn dịch vụ (service / 서비스) start hoàn toàn.”** `mask` mới là cơ chế mạnh hơn cho mục tiêu đó.

## Kết nối kiến thức

Đọc [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md) để hiểu tài nguyên (resource / 자원)/bảo mật (security / 보안) primitives phía dưới systemd, [Bảo mật và gia cố](../08_operations/security_hardening.md) để hiểu threat mô hình (model / 모델), và [Deployment/rollback](../08_operations/deployment_release_rollback.md) để nối vòng đời (lifecycle / 생명주기) dịch vụ (service / 서비스) với quy trình phát hành (release process / 릴리스 프로세스).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [boot kernel initramfs](./boot_kernel_initramfs.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
