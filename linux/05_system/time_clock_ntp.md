# Thời gian (time / 시간), Clock, Timezone và NTP trên Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Linux có nhiều khái niệm về thời gian** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **UTC và cục bộ (local / 로컬) thời gian (time / 시간)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối time, clock và NTP, để phân biệt giờ hệ thống, monotonic time và đồng bộ thời gian dùng cho log hoặc giao dịch.

Thời gian trên máy chủ (server / 서버) nghe có vẻ là chi tiết nhỏ, nhưng sai vài phút có thể làm TLS, đơn vị từ (token / 토큰) hết hạn, phân tán (distributed / 분산) tracing, log correlation, cron và cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) trở nên khó hiểu. Trong hệ thống nhiều máy, thời gian chính xác không chỉ để hiển thị đẹp; nó là một phần của **tính đúng đắn vận hành (operational correctness)**.

## Linux có nhiều khái niệm về thời gian

Khi chạy:

```bash
date
```

bạn thấy wall-clock thời gian (time / 시간) theo timezone hiện tại. Nhưng kernel và ứng dụng (application / 애플리케이션) còn sử dụng nhiều loại clock khác. Có clock phản ánh thời gian lịch, có clock tăng đơn điệu dùng để đo duration, và phần cứng có **RTC (Real-Time Clock)** để giữ thời gian qua reboot.

Điểm quan trọng là “thời gian” không phải chỉ một con số duy nhất.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **UTC và cục bộ (local / 로컬) thời gian (time / 시간)** tiếp nhận điểm tựa từ **Linux có nhiều khái niệm về thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Timezone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## UTC và cục bộ (local / 로컬) thời gian (time / 시간)

Máy chủ (server / 서버) môi trường vận hành (production / 운영 환경) thường lưu hoặc trao đổi timestamp theo UTC vì UTC tránh nhiều vấn đề timezone và daylight-saving thời gian (time / 시간). cục bộ (local / 로컬) timezone vẫn hữu ích cho con người khi đọc log.

```bash
date
date -u
timedatectl
```

`date -u` hiển thị UTC. `timedatectl` cho biết cục bộ (local / 로컬) thời gian (time / 시간), universal thời gian (time / 시간), RTC và trạng thái synchronization.

Một timestamp tốt trong log thường kèm offset:

```text
2026-09-20T20:30:15+09:00
```

hoặc UTC:

```text
2026-09-20T11:30:15Z
```

Timestamp không có timezone dễ gây nhầm khi so log giữa Seoul, UTC máy chủ (server / 서버) và dịch vụ ở region khác.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Timezone** tiếp nhận điểm tựa từ **UTC và cục bộ (local / 로컬) thời gian (time / 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Wall clock và monotonic clock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Timezone

Timezone thường được quản lý qua cơ sở dữ liệu (database / 데이터베이스) `tzdata`. Xem timezone:

```bash
timedatectl
```

Đổi timezone, nếu thật sự cần:

```bash
sudo timedatectl set-timezone Asia/Seoul
```

Không nên đổi timezone môi trường vận hành (production / 운영 환경) chỉ để log “dễ nhìn hơn” nếu hệ thống đã có convention UTC. Thay đổi timezone có thể ảnh hưởng cron hoặc cách ứng dụng (application / 애플리케이션) format timestamp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Wall clock và monotonic clock** tiếp nhận điểm tựa từ **Timezone** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NTP giải quyết vấn đề gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Wall clock và monotonic clock

Wall clock có thể được điều chỉnh bởi NTP hoặc admin. Vì vậy nó không lý tưởng để đo elapsed duration.

Ứng dụng (application / 애플리케이션) thường nên dùng **monotonic clock** cho hết thời gian chờ (timeout / 타임아웃) và benchmark vì clock này không đi lùi khi wall thời gian (time / 시간) được điều chỉnh.

Trong Java, `System.currentTimeMillis()` phục vụ timestamp kiểu wall clock, còn `System.nanoTime()` phù hợp hơn để đo duration.

Đây là ví dụ OS concept ảnh hưởng trực tiếp cách viết backend mã (code / 코드).

> **Chuyển mạch:** Trong **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **NTP giải quyết vấn đề gì?** tiếp nhận điểm tựa từ **Wall clock và monotonic clock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Step và slew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NTP giải quyết vấn đề gì?

Các oscillator phần cứng bị drift. Nếu không đồng bộ, hai máy chủ (server / 서버) có thể lệch nhau dần. NTP (network Time protocol) giúp đồng bộ clock với nguồn thời gian tin cậy.

Trên systemd-based hệ thống (system / 시스템) có thể kiểm tra:

```bash
timedatectl status
```

Tùy phân phối (distribution / 분포), dịch vụ thực tế có thể là `systemd-timesyncd`, `chronyd` hoặc `ntpd`.

Chrony thường gặp trên máy chủ (server / 서버) hiện đại:

```bash
chronyc tracking
chronyc sources -v
```

Các command này giúp xem offset, tham chiếu (reference / 참조) nguồn (source / 소스) và trạng thái synchronization.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Step và slew** tiếp nhận điểm tựa từ **NTP giải quyết vấn đề gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tại sao clock sai làm TLS lỗi?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Step và slew

Nếu clock lệch, hệ thống có thể **step** thời gian bằng cách nhảy trực tiếp hoặc **slew** bằng cách điều chỉnh tốc độ clock dần dần.

Step lớn có thể làm một số ứng dụng (application / 애플리케이션) nhạy cảm với thời gian (time / 시간) gặp hành vi bất ngờ. Vì vậy thời gian (time / 시간) daemon có chính sách (policy / 정책) về khi nào được step và khi nào slew.

Không nên tự chạy `date -s` trên môi trường vận hành (production / 운영 환경) nếu thời gian (time / 시간) synchronization đang được quản lý mà chưa hiểu tác động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Tại sao clock sai làm TLS lỗi?** tiếp nhận điểm tựa từ **Step và slew** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đơn vị từ (token / 토큰) và authentication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao clock sai làm TLS lỗi?

Certificate có khoảng hiệu lực `Not Before` và `Not After`. Nếu máy khách (client / 클라이언트) nghĩ hiện tại nằm ngoài khoảng đó, TLS xác minh (verification / 확인) có thể thất bại dù certificate hoàn toàn hợp lệ theo thời gian thực.

Khi gặp lỗi certificate “not yet valid” hoặc “expired” bất thường, hãy kiểm tra clock:

```bash
date -u
timedatectl
```

Đây là ví dụ một symptom ở TLS nhưng nguyên nhân gốc (root cause / 근본 원인) nằm ở hệ thống (system / 시스템) thời gian (time / 시간).

> **Chuyển mạch:** Trong **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Đơn vị từ (token / 토큰) và authentication** tiếp nhận điểm tựa từ **Tại sao clock sai làm TLS lỗi?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Log correlation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị từ (token / 토큰) và authentication

JWT, OAuth truy cập (access / 접근) đơn vị từ (token / 토큰), session expiration và signed URL thường dựa trên timestamp. Clock skew giữa issuer và verifier có thể gây đơn vị từ (token / 토큰) “chưa có hiệu lực” hoặc “đã hết hạn”.

Vì vậy phân tán (distributed / 분산) authentication thường cho phép một lượng **clock skew** nhỏ, nhưng không nên dùng skew lớn để che hệ thống đồng bộ thời gian kém.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Log correlation** tiếp nhận điểm tựa từ **Đơn vị từ (token / 토큰) và authentication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cron và timezone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log correlation

Giả sử API máy chủ (server / 서버) log 20:00:01 và cơ sở dữ liệu (database / 데이터베이스) log 11:00:03 UTC. Nếu người điều tra không biết timezone, có thể tưởng chúng là hai sự kiện cách nhau 9 giờ.

Trước sự cố (incident / 인시던트) phân tích (analysis / 분석), hãy xác nhận:

```bash
date '+%F %T %Z %z'
date -u
```

Trong hệ thống nhiều host, nên chuẩn hóa timestamp format và timezone để correlation dễ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Cron và timezone** tiếp nhận điểm tựa từ **Log correlation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Daylight Saving thời gian (time / 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cron và timezone

Cron chạy theo timezone của môi trường/daemon tương ứng. Job “02:00 mỗi ngày” là một yêu cầu chưa đủ nếu hệ thống có nhiều timezone.

Nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) gắn với Korea thời gian (time / 시간) nhưng máy chủ (server / 서버) dùng UTC, hãy viết yêu cầu (requirement / 요구사항) rõ và kiểm tra scheduler hỗ trợ timezone thế nào.

Systemd timer có khả năng biểu diễn calendar sự kiện (event / 이벤트) rõ hơn trong nhiều trường hợp và có thể xem lịch chạy bằng:

```bash
systemctl list-timers
```

> **Chuyển mạch:** Trong **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Daylight Saving thời gian (time / 시간)** tiếp nhận điểm tựa từ **Cron và timezone** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RTC và reboot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Daylight Saving thời gian (time / 시간)

Hàn Quốc hiện không dùng DST, nhưng máy chủ (server / 서버) phục vụ quốc gia có DST vẫn có thể bị ảnh hưởng. Một cục bộ (local / 로컬) thời gian (time / 시간) như 02:30 có ngày không tồn tại hoặc xuất hiện hai lần khi DST chuyển đổi.

Vì vậy sự kiện (event / 이벤트) mang tính kỹ thuật nên thường lưu bằng UTC/instant, còn timezone chỉ áp dụng khi hiển thị hoặc xử lý nghiệp vụ (business / 비즈니스) calendar.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **RTC và reboot** tiếp nhận điểm tựa từ **Daylight Saving thời gian (time / 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Leap second và giả định “mỗi phút luôn 60 giây”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RTC và reboot

Hardware clock giữ thời gian khi máy tắt. Kiểm tra:

```bash
sudo hwclock --show
```

Nhiều Linux hệ thống (system / 시스템) cấu hình RTC theo UTC. `timedatectl` hiển thị trạng thái liên quan.

Trong VM/cloud, hypervisor và guest thời gian (time / 시간) synchronization có thể tương tác. Nếu clock drift liên tục, cần xem cả thời gian (time / 시간) daemon và nền tảng ảo hóa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Leap second và giả định “mỗi phút luôn 60 giây”** tiếp nhận điểm tựa từ **RTC và reboot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Troubleshooting thời gian (time / 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Leap second và giả định “mỗi phút luôn 60 giây”

Timekeeping thực tế phức tạp hơn lịch đơn giản. Leap second từng được sử dụng để điều chỉnh UTC. Hệ thống có thể xử lý bằng step, smear hoặc cơ chế khác tùy provider.

Ứng dụng (application / 애플리케이션) thông thường không nên tự viết thuật toán timekeeping từ đầu. Hãy dùng thư viện date/thời gian (time / 시간) chuẩn của ngôn ngữ và lưu instant/timezone đúng mô hình.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Troubleshooting thời gian (time / 시간)** tiếp nhận điểm tựa từ **Leap second và giả định “mỗi phút luôn 60 giây”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Troubleshooting thời gian (time / 시간)

Khi nghi clock bài toán (problem / 문제), luồng (flow / 흐름) hợp lý là:

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

Sau đó kiểm tra DNS/mạng (network / 네트워크) tới thời gian (time / 시간) nguồn (source / 소스), firewall UDP khi phù hợp, dịch vụ (service / 서비스) status và logs.

Không sửa clock thủ công trước khi biết daemon nào đang sở hữu thời gian (time / 시간) synchronization.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Troubleshooting thời gian (time / 시간)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hãy tách ba câu hỏi:

```text
Hệ thống đang nghĩ bây giờ là lúc nào?
Timestamp đang được biểu diễn theo timezone nào?
Clock có đang được đồng bộ với nguồn tin cậy không?
```

Trong hệ thống phân tán (distributed system / 분산 시스템), tính đúng đắn (correctness / 정확성) không yêu cầu mọi clock giống tuyệt đối từng nanosecond, nhưng cần sai số đủ nhỏ cho giao thức (protocol / 프로토콜) và nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“máy chủ (server / 서버) hiển thị đúng giờ nên thời gian (time / 시간) không có vấn đề.”** Có thể timezone đúng nhưng clock offset vẫn sai, hoặc ngược lại.

**“NTP chỉ cần cấu hình một lần.”** Clock tiếp tục drift; synchronization là quá trình liên tục.

**“hết thời gian chờ (timeout / 타임아웃) nên dùng wall clock.”** Duration nên dùng monotonic clock khi thời gian chạy (runtime / 런타임) cung cấp.

**“Mọi log cùng timestamp là cùng thời điểm.”** Cần xem timezone, clock skew và timestamp precision.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), Clock, Timezone và NTP trên Linux**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Thời gian (time / 시간) liên kết trực tiếp với [Logging và Observability](./logging_journal_observability.md), [Scheduling và Automation](../08_operations/scheduling_automation.md), TLS trong networking, authentication đơn vị từ (token / 토큰) trong backend và quá trình phân tích sự cố (incident / 인시던트) trong [Production Troubleshooting](../09_production/production_troubleshooting.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
