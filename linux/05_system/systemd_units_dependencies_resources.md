# Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Systemd không chỉ là một công cụ restart dịch vụ (service / 서비스)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Đơn vị (unit / 단위) đồ thị (graph / 그래프) thay cho chuỗi script tuần tự** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối systemd units với dependencies, resources và lifecycle, để service graph được hiểu qua thứ tự khởi động cùng giới hạn tài nguyên.

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

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Systemd không chỉ là một công cụ restart dịch vụ (service / 서비스)** xác định đầu vào; **Đơn vị (unit / 단위) đồ thị (graph / 그래프) thay cho chuỗi script tuần tự** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Quan hệ thứ tự (ordering / 순서) khác yêu cầu (requirement / 요구사항)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Đơn vị (unit / 단위) đồ thị (graph / 그래프) thay cho chuỗi script tuần tự** xác định đầu vào; **Quan hệ thứ tự (ordering / 순서) khác yêu cầu (requirement / 요구사항)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Before=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Before=** tiếp nhận điểm tựa từ **Quan hệ thứ tự (ordering / 순서) khác yêu cầu (requirement / 요구사항)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Requires= và thất bại (failure / 실패) propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Before=`

`Before=A` là quan hệ thứ tự (ordering / 순서) ngược với `After=A`.

Không nên khai báo cả hai chiều gây cycle.

Có thể kiểm tra cycle/phụ thuộc (dependency / 의존성) bằng:

```bash
systemctl list-dependencies app.service
systemctl list-dependencies --reverse app.service
```

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Requires= và thất bại (failure / 실패) propagation** tiếp nhận điểm tựa từ **Before=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Wants= khi nào phù hợp?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Requires=` và thất bại (failure / 실패) propagation

Nếu A `Requires=B`, thất bại (failure / 실패) của B có thể ảnh hưởng A tùy tình huống activation/vòng đời (lifecycle / 생명주기).

Nhưng phụ thuộc (dependency / 의존성) ngữ nghĩa (semantics / 의미론) không thay thế application-level thử lại (retry / 재시도) hoặc readiness.

Một cơ sở dữ liệu (database / 데이터베이스) dịch vụ (service / 서비스) “active” chưa chắc đã sẵn sàng trả truy vấn (query / 쿼리).

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Wants= khi nào phù hợp?** tiếp nhận điểm tựa từ **Requires= và thất bại (failure / 실패) propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BindsTo=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Wants=` khi nào phù hợp?

`Wants=` phù hợp với phụ thuộc (dependency / 의존성) mong muốn nhưng không nên làm đơn vị (unit / 단위) chính thất bại (fail / 실패) nếu phụ thuộc (dependency / 의존성) phụ không lên được.

Ví dụ khả năng quan sát (observability / 관측 가능성) sidecar hoặc optional bộ nhớ đệm (cache / 캐시) có thể phù hợp tùy kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **BindsTo=** tiếp nhận điểm tựa từ **Wants= khi nào phù hợp?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PartOf=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `BindsTo=`

`BindsTo=` tạo quan hệ vòng đời (lifecycle / 생명주기) chặt hơn, thường dùng khi đơn vị (unit / 단위) phải dừng nếu phụ thuộc (dependency / 의존성) biến mất.

Không nên dùng tràn lan; vòng đời (lifecycle / 생명주기) coupling quá mạnh có thể tạo cascading thất bại (failure / 실패).

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **PartOf=** tiếp nhận điểm tựa từ **BindsTo=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conflicts=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `PartOf=`

`PartOf=` hữu ích khi muốn restart/stop một parent-like đơn vị (unit / 단위) kéo theo đơn vị (unit / 단위) khác.

Ví dụ một nhóm dịch vụ (service / 서비스) có thể được tổ chức để restart cùng nhau.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Conflicts=** tiếp nhận điểm tựa từ **PartOf=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mục tiêu (target / 대상) đơn vị (unit / 단위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Conflicts=`

Một số đơn vị (unit / 단위) không thể active đồng thời.

`Conflicts=` biểu diễn quan hệ loại trừ.

Ví dụ hai hiện thực (implementation / 구현) cạnh tranh cùng một tài nguyên (resource / 자원) có thể được cấu hình để không cùng chạy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Mục tiêu (target / 대상) đơn vị (unit / 단위)** tiếp nhận điểm tựa từ **Conflicts=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Activation giao dịch (transaction / 트랜잭션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mục tiêu (target / 대상) đơn vị (unit / 단위)

Mục tiêu (target / 대상) không chạy lô-gic nghiệp vụ (business logic / 비즈니스 로직). Nó nhóm và đồng bộ các đơn vị (unit / 단위) khác.

Ví dụ:

```bash
systemctl list-dependencies multi-user.target
```

Mục tiêu (target / 대상) gần với “mốc trạng thái hệ thống” hơn là dịch vụ (service / 서비스).

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Activation giao dịch (transaction / 트랜잭션)** tiếp nhận điểm tựa từ **Mục tiêu (target / 대상) đơn vị (unit / 단위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Socket activation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Activation giao dịch (transaction / 트랜잭션)

Khi yêu cầu:

```bash
systemctl start app.service
```

systemd không đơn giản gọi `ExecStart`. Nó xây một giao dịch (transaction / 트랜잭션) gồm các đơn vị (unit / 단위) được kéo vào bởi phụ thuộc (dependency / 의존성), kiểm tra thứ tự (ordering / 순서), job conflicts và sau đó thực thi theo đồ thị (graph / 그래프).

Đây là lý do một đơn vị (unit / 단위) tệp (file / 파일) nhỏ có thể kéo theo rất nhiều operations.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Socket activation** tiếp nhận điểm tựa từ **Activation giao dịch (transaction / 트랜잭션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Timer activation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Timer activation** tiếp nhận điểm tựa từ **Socket activation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đường dẫn (path / 경로) activation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Timer activation** xác định đầu vào; **Đường dẫn (path / 경로) activation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Dịch vụ (service / 서비스) Type=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đường dẫn (path / 경로) activation

Systemd còn có `.path` đơn vị (unit / 단위) để kích hoạt dịch vụ (service / 서비스) khi đường dẫn (path / 경로)/tệp (file / 파일) thay đổi theo một số điều kiện.

Đây là event-driven alternative cho polling vòng lặp (loop / 루프) trong một số use trường hợp (case / 사례).

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Đường dẫn (path / 경로) activation** xác định đầu vào; **Dịch vụ (service / 서비스) Type=** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Type=notify và readiness tốt hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Type=notify và readiness tốt hơn** tiếp nhận điểm tựa từ **Dịch vụ (service / 서비스) Type=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Main PID** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Type=notify` và readiness tốt hơn

Nếu ứng dụng (application / 애플리케이션) hỗ trợ `sd_notify`, nó có thể báo:

```text
READY=1
```

chỉ sau khi đã hoàn tất initialization.

Điều này chính xác hơn `sleep 10` hoặc đoán readiness từ tiến trình (process / 프로세스) existence.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Main PID** tiếp nhận điểm tựa từ **Type=notify và readiness tốt hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao shell wrapper nên dùng exec trong một số tình huống?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Main PID

Systemd phải biết tiến trình (process / 프로세스) nào là main tiến trình (process / 프로세스) để theo dõi vòng đời (lifecycle / 생명주기).

```bash
systemctl show app -p MainPID
```

Nếu daemon double-fork hoặc wrapper shell không dùng `exec`, systemd có thể theo dõi tiến trình (process / 프로세스) không như mong muốn.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Main PID** cho ta quy tắc; **Vì sao shell wrapper nên dùng exec trong một số tình huống?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **ExecStartPre= và ExecStartPost=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Vì sao shell wrapper nên dùng exec trong một số tình huống?** cho ta quy tắc; **ExecStartPre= và ExecStartPost=** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **ExecCondition=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `ExecStartPre=` và `ExecStartPost=`

Có thể dùng để thực hiện bước trước/sau start:

```ini
ExecStartPre=/usr/bin/test -f /opt/app/app.jar
ExecStart=/usr/bin/java -jar /opt/app/app.jar
ExecStartPost=/usr/local/bin/register-service.sh
```

Không nên biến đơn vị (unit / 단위) tệp (file / 파일) thành một triển khai (deployment / 배포) script dài. Những bước có transactional lô-gic (logic / 논리) phức tạp thường nên nằm ngoài dịch vụ (service / 서비스) startup.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **ExecCondition=** tiếp nhận điểm tựa từ **ExecStartPre= và ExecStartPost=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Môi trường (environment / 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `ExecCondition=`

`ExecCondition=` cho phép kiểm tra điều kiện trước start với ngữ nghĩa (semantics / 의미론) riêng.

Nó hữu ích để tránh start đơn vị (unit / 단위) khi precondition không đúng mà không coi mọi trường hợp là thất bại (failure / 실패).

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Môi trường (environment / 환경)** tiếp nhận điểm tựa từ **ExecCondition=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Working directory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môi trường (environment / 환경)

Systemd không tự đọc `.bashrc` hoặc `.profile` giống interactive login shell.

Có thể dùng:

```ini
Environment=SPRING_PROFILES_ACTIVE=prod
EnvironmentFile=/etc/app/app.env
```

Nhưng secret management cần cẩn thận: môi trường (environment / 환경) có thể lộ qua debugging, dump hoặc quyền đọc tiến trình (process / 프로세스) trạng thái (state / 상태) tùy hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Working directory** tiếp nhận điểm tựa từ **Môi trường (environment / 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **User= và Group=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Working directory

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```ini
WorkingDirectory=/opt/app
```

Nếu ứng dụng dùng relative đường dẫn (path / 경로) mà không khai báo working directory, dịch vụ (service / 서비스) có thể tìm tệp (file / 파일) sai chỗ.

Tốt hơn nữa là ứng dụng (application / 애플리케이션) dùng absolute/configured paths cho dữ liệu quan trọng.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **User= và Group=** tiếp nhận điểm tựa từ **Working directory** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Supplementary groups** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `User=` và `Group=`

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```ini
User=app
Group=app
```

Systemd thiết lập credentials trước khi exec tiến trình (process / 프로세스).

Đây là lý do command chạy bằng gốc (root / 루트) trong SSH có thể thành công nhưng dịch vụ (service / 서비스) người dùng (user / 사용자) lại bị permission denied.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Supplementary groups** tiếp nhận điểm tựa từ **User= và Group=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **UMask=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Supplementary groups

Có thể dùng:

```ini
SupplementaryGroups=appops
```

khi dịch vụ (service / 서비스) cần thêm group truy cập (access / 접근).

Không nên thêm tiến trình (process / 프로세스) vào quá nhiều group vì mở rộng privilege surface.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **UMask=** tiếp nhận điểm tựa từ **Supplementary groups** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tài nguyên (resource / 자원) limits kiểu POSIX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `UMask=`

Systemd có thể đặt `UMask=` riêng cho dịch vụ (service / 서비스).

Điều này ảnh hưởng chế độ (mode / 모드) của tệp (file / 파일) mới được tạo.

```ini
UMask=0027
```

Nếu app tạo log/cấu hình (config / 설정) với permission khác khi chạy tay và khi chạy dịch vụ (service / 서비스), đây là một điểm cần kiểm tra.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **UMask=** đã nêu tiêu chí phân biệt, còn **Tài nguyên (resource / 자원) limits kiểu POSIX** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Cgroup tài nguyên (resource / 자원) điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Tài nguyên (resource / 자원) limits kiểu POSIX** đã nêu tiêu chí phân biệt, còn **Cgroup tài nguyên (resource / 자원) điều khiển (control / 제어)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **MemoryMax=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Cgroup tài nguyên (resource / 자원) điều khiển (control / 제어)** nêu điều cần giải thích; **MemoryMax=** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **MemoryHigh=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `MemoryMax=`

Nếu dịch vụ (service / 서비스) vượt `MemoryMax`, cgroup OOM có thể xảy ra dù host còn RAM.

Kiểm tra:

```bash
systemctl show app -p MemoryCurrent -p MemoryMax
```

hoặc cgroup files tương ứng.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **MemoryHigh=** tiếp nhận điểm tựa từ **MemoryMax=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TasksMax=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `MemoryHigh=`

`MemoryHigh` tạo pressure/throttling trước hard kill ở `MemoryMax`.

Nó hữu ích để tạo soft ranh giới (boundary / 경계) nhưng có thể làm độ trễ (latency / 지연 시간) tăng khi reclaim.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **TasksMax=** tiếp nhận điểm tựa từ **MemoryHigh=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Restart chính sách (policy / 정책) sâu hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `TasksMax=`

Giới hạn số tasks/threads trong cgroup.

Java app tạo quá nhiều threads có thể chạm limit dù `ulimit -u` nhìn còn cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Restart chính sách (policy / 정책) sâu hơn** tiếp nhận điểm tựa từ **TasksMax=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exit status nào được coi là success?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Exit status nào được coi là success?** tiếp nhận điểm tựa từ **Restart chính sách (policy / 정책) sâu hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hết thời gian chờ (timeout / 타임아웃) khi start/stop** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exit status nào được coi là success?

Có thể điều chỉnh:

```ini
SuccessExitStatus=143
```

nhưng chỉ nên làm khi hiểu ứng dụng (application / 애플리케이션) tín hiệu (signal / 신호)/exit ngữ nghĩa (semantics / 의미론).

Ví dụ JVM nhận SIGTERM không nhất thiết luôn trả 143 tùy wrapper/thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Hết thời gian chờ (timeout / 타임아웃) khi start/stop** tiếp nhận điểm tựa từ **Exit status nào được coi là success?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kill chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hết thời gian chờ (timeout / 타임아웃) khi start/stop

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```ini
TimeoutStartSec=60
TimeoutStopSec=30
```

Nếu shutdown cần drain traffic lâu hơn hết thời gian chờ (timeout / 타임아웃), systemd có thể escalate sang kill.

Đây là lý do graceful shutdown của Spring/Kubernetes/systemd phải được thiết kế đồng bộ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Kill chế độ (mode / 모드)** tiếp nhận điểm tựa từ **Hết thời gian chờ (timeout / 타임아웃) khi start/stop** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Watchdog** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kill chế độ (mode / 모드)

Systemd có `KillMode=` để quyết định tín hiệu (signal / 신호) gửi cho tiến trình (process / 프로세스) nào trong cgroup.

`control-group` thường giúp dừng toàn bộ tiến trình (process / 프로세스) con còn lại.

Nếu chọn sai, child tiến trình (process / 프로세스) có thể bị orphan hoặc sống sau khi dịch vụ (service / 서비스) tưởng đã stop.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Watchdog** tiếp nhận điểm tựa từ **Kill chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sandboxing với systemd** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Watchdog

Một dịch vụ (service / 서비스) hỗ trợ watchdog có thể gửi heartbeat cho systemd.

Nếu heartbeat dừng, systemd coi dịch vụ (service / 서비스) unhealthy và có thể restart.

Watchdog khác health endpoint: nó đo việc tiến trình (process / 프로세스) còn phản hồi theo giao thức (protocol / 프로토콜) với dịch vụ (service / 서비스) manager.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Sandboxing với systemd** tiếp nhận điểm tựa từ **Watchdog** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NoNewPrivileges=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **NoNewPrivileges=** tiếp nhận điểm tựa từ **Sandboxing với systemd** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ProtectSystem=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `NoNewPrivileges=`

Khi bật, tiến trình (process / 프로세스) và descendants không thể đạt thêm privilege qua `execve()` theo một số cơ chế như setuid/capabilities.

Đây là điều khiển (control / 제어) quan trọng để giảm privilege escalation.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **ProtectSystem=** tiếp nhận điểm tựa từ **NoNewPrivileges=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PrivateTmp=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `ProtectSystem=`

Có thể làm nhiều phần filesystem read-only trong không gian tên (namespace / 네임스페이스) của dịch vụ (service / 서비스).

Ứng dụng cần ghi (write / 쓰기) đường dẫn (path / 경로) phải được mở riêng bằng directives như `ReadWritePaths=`.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **PrivateTmp=** tiếp nhận điểm tựa từ **ProtectSystem=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PrivateDevices=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `PrivateTmp=`

Dịch vụ (service / 서비스) nhận `/tmp` và `/var/tmp` riêng trong mount không gian tên (namespace / 네임스페이스).

Nếu hai dịch vụ (service / 서비스) trước đây trao đổi tệp (file / 파일) qua `/tmp`, bật `PrivateTmp` có thể phá tích hợp (integration / 통합) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **PrivateDevices=** tiếp nhận điểm tựa từ **PrivateTmp=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Năng lực (capability / 역량) bounding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `PrivateDevices=`

Giảm truy cập (access / 접근) tới thiết bị (device / 장치) nodes.

Phù hợp nhiều daemon không cần hardware truy cập (access / 접근) trực tiếp.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Năng lực (capability / 역량) bounding** tiếp nhận điểm tựa từ **PrivateDevices=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DynamicUser=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lực (capability / 역량) bounding

Thay vì full gốc (root / 루트), có thể giới hạn capabilities:

```ini
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
AmbientCapabilities=CAP_NET_BIND_SERVICE
```

Điều này cho phép app bind low cổng (port / 포트) mà không giữ toàn bộ gốc (root / 루트) privilege trong một số mô hình.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **DynamicUser=** tiếp nhận điểm tựa từ **Năng lực (capability / 역량) bounding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **systemd-analyze security** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `DynamicUser=`

Systemd có thể tạo người dùng (user / 사용자) thời gian chạy (runtime / 런타임) tạm thời cho dịch vụ (service / 서비스).

Hữu ích với daemon không cần persistent UID, nhưng cần hiểu quyền sở hữu (ownership / 소유권) của persistent files trước khi dùng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **systemd-analyze security** tiếp nhận điểm tựa từ **DynamicUser=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Drop-in override** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `systemd-analyze security`

Có thể đánh giá một số hardening options:

```bash
systemd-analyze security app.service
```

Điểm số không phải chân lý. công cụ (tool / 도구) chỉ đánh giá theo một tập heuristic; bảo mật (security / 보안) thật còn phụ thuộc ứng dụng (application / 애플리케이션) và threat mô hình (model / 모델).

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Drop-in override** tiếp nhận điểm tựa từ **systemd-analyze security** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **daemon-reload khác restart** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **daemon-reload khác restart** tiếp nhận điểm tựa từ **Drop-in override** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mask** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `daemon-reload` khác restart

Sau khi sửa đơn vị (unit / 단위) definition:

```bash
sudo systemctl daemon-reload
```

systemd đọc lại siêu dữ liệu (metadata / 메타데이터) đơn vị (unit / 단위).

Nhưng tiến trình (process / 프로세스) đang chạy chưa tự thay đổi.

Sau đó tùy thay đổi có thể cần restart/reload dịch vụ (service / 서비스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Mask** tiếp nhận điểm tựa từ **daemon-reload khác restart** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transient đơn vị (unit / 단위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mask

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
sudo systemctl mask app.service
```

mask thường tạo liên kết tới `/dev/null` để ngăn đơn vị (unit / 단위) được start kể cả gián tiếp.

`disable` chỉ bỏ enablement relationship; `mask` mạnh hơn.

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Transient đơn vị (unit / 단위)** tiếp nhận điểm tựa từ **Mask** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phạm vi (scope / 범위) đơn vị (unit / 단위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transient đơn vị (unit / 단위)

Có thể chạy command tạm dưới systemd:

```bash
systemd-run --unit=test-job --property=MemoryMax=1G /usr/local/bin/job.sh
```

Đây là cách hay để áp tài nguyên (resource / 자원) điều khiển (control / 제어) cho tác vụ (task / 작업) không cần tạo đơn vị (unit / 단위) tệp (file / 파일) cố định.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Phạm vi (scope / 범위) đơn vị (unit / 단위)** tiếp nhận điểm tựa từ **Transient đơn vị (unit / 단위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Journal siêu dữ liệu (metadata / 메타데이터) theo đơn vị (unit / 단위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phạm vi (scope / 범위) đơn vị (unit / 단위)

Interactive tiến trình (process / 프로세스) có thể được group trong `.scope` đơn vị (unit / 단위).

Desktop session/bộ chứa (container / 컨테이너) manager thường tận dụng phạm vi (scope / 범위)/dịch vụ (service / 서비스) hierarchy để tổ chức cgroups.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Phạm vi (scope / 범위) đơn vị (unit / 단위)** nêu điều cần giải thích; **Journal siêu dữ liệu (metadata / 메타데이터) theo đơn vị (unit / 단위)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): dịch vụ (service / 서비스) “active” nhưng chưa ready** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journal siêu dữ liệu (metadata / 메타데이터) theo đơn vị (unit / 단위)

Systemd-journald gắn siêu dữ liệu (metadata / 메타데이터) như `_SYSTEMD_UNIT`, PID, UID vào log.

Do đó:

```bash
journalctl -u app.service
```

lọc theo siêu dữ liệu (metadata / 메타데이터), không chỉ grep văn bản (text / 텍스트).

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Journal siêu dữ liệu (metadata / 메타데이터) theo đơn vị (unit / 단위)** cho ta quy tắc; **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): dịch vụ (service / 서비스) “active” nhưng chưa ready** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Một trường hợp (case / 사례): dịch vụ (service / 서비스) restart vòng lặp (loop / 루프) làm disk đầy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): dịch vụ (service / 서비스) “active” nhưng chưa ready

Systemd `active` chỉ phản ánh vòng đời (lifecycle / 생명주기) theo `Type=`.

Nếu Spring Boot mất 30 giây để warm bộ nhớ đệm (cache / 캐시) nhưng đơn vị (unit / 단위) `Type=simple`, systemd có thể coi active ngay khi JVM start.

Bộ cân bằng tải (load balancer / 로드 밸런서) cần readiness riêng.

Giải pháp có thể là:

- application-level readiness endpoint;
- `Type=notify` nếu hỗ trợ;
- orchestration readiness probe;
- phụ thuộc (dependency / 의존성) bên tiêu thụ (consumer / 소비자) có thử lại (retry / 재시도)/backoff.

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Một trường hợp (case / 사례) môi trường vận hành (production / 운영 환경): dịch vụ (service / 서비스) “active” nhưng chưa ready** cho ta quy tắc; **Một trường hợp (case / 사례): dịch vụ (service / 서비스) restart vòng lặp (loop / 루프) làm disk đầy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Một trường hợp (case / 사례): chạy tay được nhưng dịch vụ (service / 서비스) không chạy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Một trường hợp (case / 사례): dịch vụ (service / 서비스) restart vòng lặp (loop / 루프) làm disk đầy** cho ta quy tắc; **Một trường hợp (case / 사례): chạy tay được nhưng dịch vụ (service / 서비스) không chạy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Một trường hợp (case / 사례): chạy tay được nhưng dịch vụ (service / 서비스) không chạy** cho ta quy tắc; **Mô hình tư duy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“After=mạng (network / 네트워크).mục tiêu (target / 대상) nghĩa mạng đã dùng được.”** Không; đó chỉ là thứ tự (ordering / 순서) tương đối với một mục tiêu (target / 대상).

**“dịch vụ (service / 서비스) active nghĩa ứng dụng healthy.”** Không; readiness/nghiệp vụ (business / 비즈니스) health là lớp khác.

**“LimitNOFILE trong shell áp cho systemd dịch vụ (service / 서비스).”** Không nhất thiết; systemd có limit riêng.

**“Restart=always tăng độ tin cậy (reliability / 신뢰성).”** Có thể tạo restart storm nếu thất bại (failure / 실패) persistent.

**“Bật mọi hardening directive luôn tốt.”** Có thể phá ứng dụng (application / 애플리케이션); cần threat mô hình (model / 모델) và kiểm thử (test / 테스트).

**“disable ngăn dịch vụ (service / 서비스) start hoàn toàn.”** `mask` mới là cơ chế mạnh hơn cho mục tiêu đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Systemd sâu hơn: đơn vị (unit / 단위) đồ thị (graph / 그래프), phụ thuộc (dependency / 의존성), tài nguyên (resource / 자원) điều khiển (control / 제어) và sandboxing**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md) để hiểu resource/security primitives phía dưới systemd, [Bảo mật và gia cố](../08_operations/security_hardening.md) để hiểu threat model, và [Deployment/rollback](../08_operations/deployment_release_rollback.md) để nối lifecycle service với release process.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
