# Time, Clock, Timezone và NTP trên Linux

Thời gian trên server nghe có vẻ là chi tiết nhỏ, nhưng sai vài phút có thể làm TLS, token hết hạn, distributed tracing, log correlation, cron và database transaction trở nên khó hiểu. Trong hệ thống nhiều máy, thời gian chính xác không chỉ để hiển thị đẹp; nó là một phần của **tính đúng đắn vận hành (operational correctness)**.

## Linux có nhiều khái niệm về thời gian

Khi chạy:

```bash
date
```

bạn thấy wall-clock time theo timezone hiện tại. Nhưng kernel và application còn sử dụng nhiều loại clock khác. Có clock phản ánh thời gian lịch, có clock tăng đơn điệu dùng để đo duration, và phần cứng có **RTC (Real-Time Clock)** để giữ thời gian qua reboot.

Điểm quan trọng là “thời gian” không phải chỉ một con số duy nhất.

## UTC và local time

Server production thường lưu hoặc trao đổi timestamp theo UTC vì UTC tránh nhiều vấn đề timezone và daylight-saving time. Local timezone vẫn hữu ích cho con người khi đọc log.

```bash
date
date -u
timedatectl
```

`date -u` hiển thị UTC. `timedatectl` cho biết local time, universal time, RTC và trạng thái synchronization.

Một timestamp tốt trong log thường kèm offset:

```text
2026-09-20T20:30:15+09:00
```

hoặc UTC:

```text
2026-09-20T11:30:15Z
```

Timestamp không có timezone dễ gây nhầm khi so log giữa Seoul, UTC server và dịch vụ ở region khác.

## Timezone

Timezone thường được quản lý qua database `tzdata`. Xem timezone:

```bash
timedatectl
```

Đổi timezone, nếu thật sự cần:

```bash
sudo timedatectl set-timezone Asia/Seoul
```

Không nên đổi timezone production chỉ để log “dễ nhìn hơn” nếu hệ thống đã có convention UTC. Thay đổi timezone có thể ảnh hưởng cron hoặc cách application format timestamp.

## Wall clock và monotonic clock

Wall clock có thể được điều chỉnh bởi NTP hoặc admin. Vì vậy nó không lý tưởng để đo elapsed duration.

Application thường nên dùng **monotonic clock** cho timeout và benchmark vì clock này không đi lùi khi wall time được điều chỉnh.

Trong Java, `System.currentTimeMillis()` phục vụ timestamp kiểu wall clock, còn `System.nanoTime()` phù hợp hơn để đo duration.

Đây là ví dụ OS concept ảnh hưởng trực tiếp cách viết backend code.

## NTP giải quyết vấn đề gì?

Các oscillator phần cứng bị drift. Nếu không đồng bộ, hai server có thể lệch nhau dần. NTP (Network Time Protocol) giúp đồng bộ clock với nguồn thời gian tin cậy.

Trên systemd-based system có thể kiểm tra:

```bash
timedatectl status
```

Tùy distribution, dịch vụ thực tế có thể là `systemd-timesyncd`, `chronyd` hoặc `ntpd`.

Chrony thường gặp trên server hiện đại:

```bash
chronyc tracking
chronyc sources -v
```

Các command này giúp xem offset, reference source và trạng thái synchronization.

## Step và slew

Nếu clock lệch, hệ thống có thể **step** thời gian bằng cách nhảy trực tiếp hoặc **slew** bằng cách điều chỉnh tốc độ clock dần dần.

Step lớn có thể làm một số application nhạy cảm với time gặp hành vi bất ngờ. Vì vậy time daemon có policy về khi nào được step và khi nào slew.

Không nên tự chạy `date -s` trên production nếu time synchronization đang được quản lý mà chưa hiểu tác động.

## Tại sao clock sai làm TLS lỗi?

Certificate có khoảng hiệu lực `Not Before` và `Not After`. Nếu client nghĩ hiện tại nằm ngoài khoảng đó, TLS verification có thể thất bại dù certificate hoàn toàn hợp lệ theo thời gian thực.

Khi gặp lỗi certificate “not yet valid” hoặc “expired” bất thường, hãy kiểm tra clock:

```bash
date -u
timedatectl
```

Đây là ví dụ một symptom ở TLS nhưng root cause nằm ở system time.

## Token và authentication

JWT, OAuth access token, session expiration và signed URL thường dựa trên timestamp. Clock skew giữa issuer và verifier có thể gây token “chưa có hiệu lực” hoặc “đã hết hạn”.

Vì vậy distributed authentication thường cho phép một lượng **clock skew** nhỏ, nhưng không nên dùng skew lớn để che hệ thống đồng bộ thời gian kém.

## Log correlation

Giả sử API server log 20:00:01 và database log 11:00:03 UTC. Nếu người điều tra không biết timezone, có thể tưởng chúng là hai sự kiện cách nhau 9 giờ.

Trước incident analysis, hãy xác nhận:

```bash
date '+%F %T %Z %z'
date -u
```

Trong hệ thống nhiều host, nên chuẩn hóa timestamp format và timezone để correlation dễ hơn.

## Cron và timezone

Cron chạy theo timezone của môi trường/daemon tương ứng. Job “02:00 mỗi ngày” là một yêu cầu chưa đủ nếu hệ thống có nhiều timezone.

Nếu business logic gắn với Korea time nhưng server dùng UTC, hãy viết requirement rõ và kiểm tra scheduler hỗ trợ timezone thế nào.

Systemd timer có khả năng biểu diễn calendar event rõ hơn trong nhiều trường hợp và có thể xem lịch chạy bằng:

```bash
systemctl list-timers
```

## Daylight Saving Time

Hàn Quốc hiện không dùng DST, nhưng server phục vụ quốc gia có DST vẫn có thể bị ảnh hưởng. Một local time như 02:30 có ngày không tồn tại hoặc xuất hiện hai lần khi DST chuyển đổi.

Vì vậy event mang tính kỹ thuật nên thường lưu bằng UTC/instant, còn timezone chỉ áp dụng khi hiển thị hoặc xử lý business calendar.

## RTC và reboot

Hardware clock giữ thời gian khi máy tắt. Kiểm tra:

```bash
sudo hwclock --show
```

Nhiều Linux system cấu hình RTC theo UTC. `timedatectl` hiển thị trạng thái liên quan.

Trong VM/cloud, hypervisor và guest time synchronization có thể tương tác. Nếu clock drift liên tục, cần xem cả time daemon và nền tảng ảo hóa.

## Leap second và giả định “mỗi phút luôn 60 giây”

Timekeeping thực tế phức tạp hơn lịch đơn giản. Leap second từng được sử dụng để điều chỉnh UTC. Hệ thống có thể xử lý bằng step, smear hoặc cơ chế khác tùy provider.

Application thông thường không nên tự viết thuật toán timekeeping từ đầu. Hãy dùng thư viện date/time chuẩn của ngôn ngữ và lưu instant/timezone đúng mô hình.

## Troubleshooting time

Khi nghi clock problem, flow hợp lý là:

```bash
date '+%F %T %Z %z'
date -u
timedatectl status
```

Nếu dùng Chrony:

```bash
chronyc tracking
chronyc sources -v
```

Sau đó kiểm tra DNS/network tới time source, firewall UDP khi phù hợp, service status và logs.

Không sửa clock thủ công trước khi biết daemon nào đang sở hữu time synchronization.

## Mô hình tư duy (Mental Model)

Hãy tách ba câu hỏi:

```text
Hệ thống đang nghĩ bây giờ là lúc nào?
Timestamp đang được biểu diễn theo timezone nào?
Clock có đang được đồng bộ với nguồn tin cậy không?
```

Trong distributed system, correctness không yêu cầu mọi clock giống tuyệt đối từng nanosecond, nhưng cần sai số đủ nhỏ cho protocol và business semantics.

## Những hiểu lầm phổ biến

**“Server hiển thị đúng giờ nên time không có vấn đề.”** Có thể timezone đúng nhưng clock offset vẫn sai, hoặc ngược lại.

**“NTP chỉ cần cấu hình một lần.”** Clock tiếp tục drift; synchronization là quá trình liên tục.

**“Timeout nên dùng wall clock.”** Duration nên dùng monotonic clock khi runtime cung cấp.

**“Mọi log cùng timestamp là cùng thời điểm.”** Cần xem timezone, clock skew và timestamp precision.

## Kết nối kiến thức

Time liên kết trực tiếp với [Logging và Observability](./logging_journal_observability.md), [Scheduling và Automation](../08_operations/scheduling_automation.md), TLS trong networking, authentication token trong backend và quá trình phân tích incident trong [Production Troubleshooting](../09_production/production_troubleshooting.md).