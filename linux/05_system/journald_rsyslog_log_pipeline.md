# Journald, rsyslog và đường đi của nhật ký trong Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Journald, rsyslog và đường đi của nhật ký trong Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Một dòng log đi đâu?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **stdout và stderr không tự có tệp (file / 파일) log** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối journald, rsyslog và log pipeline, để dữ liệu sự kiện đi từ process tới lưu trữ, lọc và cảnh báo.

Chương [Nhật ký, journal và khả năng quan sát hệ thống](./logging_journal_observability.md) giải thích vai trò của log như một nguồn bằng chứng. Chương này đi sâu vào chuỗi xử lý (pipeline / 파이프라인) log ở tầng Linux: stdout/stderr của dịch vụ (service / 서비스) đi đâu, `systemd-journald` lưu dữ liệu thế nào, `rsyslog` hoặc syslog daemon tham gia ở đâu, vì sao log có thể bị mất, và log rotation phải phối hợp với tệp (file / 파일) descriptor của tiến trình (process / 프로세스) ra sao.

## Một dòng log đi đâu?

Với dịch vụ (service / 서비스) systemd, ứng dụng (application / 애플리케이션) thường ghi ra stdout/stderr.

Systemd có thể nối các stream này vào journal.

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
application stdout/stderr
        ↓
systemd service plumbing
        ↓
systemd-journald
        ↓
journal storage
        ├─ journalctl
        ├─ forward to syslog/rsyslog
        └─ forward/export to centralized logging
```

Nhưng ứng dụng (application / 애플리케이션) cũng có thể tự ghi tệp (file / 파일) riêng, nên môi trường vận hành (production / 운영 환경) có thể tồn tại song song nhiều đường log.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **stdout và stderr không tự có tệp (file / 파일) log** tiếp nhận điểm tựa từ **Một dòng log đi đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Journald lưu siêu dữ liệu (metadata / 메타데이터), không chỉ văn bản (text / 텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## stdout và stderr không tự có tệp (file / 파일) log

Nếu Java app chạy:

```bash
java -jar app.jar
```

trong terminal, stdout/stderr đi terminal.

Nếu systemd quản lý dịch vụ (service / 서비스), descriptors có thể được nối theo `StandardOutput=` và `StandardError=`.

Mặc định trên nhiều systemd các hệ thống (systems / 시스템들), đầu ra (output / 출력) đi journal.

Kiểm tra đơn vị (unit / 단위):

```bash
systemctl cat app.service
systemctl show app -p StandardOutput -p StandardError
```

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **stdout và stderr không tự có tệp (file / 파일) log** nêu điều cần giải thích; **Journald lưu siêu dữ liệu (metadata / 메타데이터), không chỉ văn bản (text / 텍스트)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Boot ID** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journald lưu siêu dữ liệu (metadata / 메타데이터), không chỉ văn bản (text / 텍스트)

Mỗi journal entry có thể kèm siêu dữ liệu (metadata / 메타데이터) như:

- `_PID`;
- `_UID`;
- `_GID`;
- `_SYSTEMD_UNIT`;
- `_COMM`;
- `_EXE`;
- `_BOOT_ID`;
- `_HOSTNAME`;
- `PRIORITY`.

Xem chi tiết:

```bash
journalctl -u app -o verbose -n 1
```

Điều này giải thích vì sao `journalctl -u app` mạnh hơn `grep app` trên văn bản (text / 텍스트) log: nó lọc bằng structured siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Journald lưu siêu dữ liệu (metadata / 메타데이터), không chỉ văn bản (text / 텍스트)** nêu điều cần giải thích; **Boot ID** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Journal volatile và persistent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Boot ID

Mỗi lần boot có một `_BOOT_ID` khác.

Xem boots:

```bash
journalctl --list-boots
```

Log boot trước:

```bash
journalctl -b -1
```

Đây là công cụ quan trọng khi máy chủ (server / 서버) vừa reboot sau kernel panic hoặc maintenance.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Journal volatile và persistent** tiếp nhận điểm tựa từ **Boot ID** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Storage=** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journal volatile và persistent

Journald có thể lưu journal dưới:

```text
/run/log/journal
```

cho volatile lưu trữ (storage / 저장소) hoặc:

```text
/var/log/journal
```

cho persistent lưu trữ (storage / 저장소), tùy cấu hình (config / 설정)/phân phối (distribution / 분포).

Nếu journal chỉ volatile, reboot sẽ mất log cũ.

Kiểm tra:

```bash
journalctl --disk-usage
ls -ld /var/log/journal /run/log/journal 2>/dev/null
```

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Storage=** tiếp nhận điểm tựa từ **Journal volatile và persistent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Journal kích thước (size / 크기) và retention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Storage=`

Trong `journald.conf`, `Storage=` có thể có các chế độ (mode / 모드) như:

```text
auto
volatile
persistent
none
```

Ngữ nghĩa (semantics / 의미론) cụ thể phụ thuộc systemd phiên bản (version / 버전).

Môi trường vận hành (production / 운영 환경) cần quyết định retention theo operational yêu cầu (requirement / 요구사항) thay vì để mặc định mà không biết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Journal kích thước (size / 크기) và retention** tiếp nhận điểm tựa từ **Storage=** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Log burst** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journal kích thước (size / 크기) và retention

Các cấu hình có thể gồm:

```text
SystemMaxUse=
SystemKeepFree=
SystemMaxFileSize=
MaxRetentionSec=
```

Không nên đặt retention chỉ dựa trên “30 ngày nghe hợp lý”.

Cần tính:

```text
log rate × retention window × compression/overhead
```

và chừa headroom cho sự cố (incident / 인시던트) burst.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Log burst** tiếp nhận điểm tựa từ **Journal kích thước (size / 크기) và retention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Journald tỷ lệ (rate / 비율) limiting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log burst

Một lỗi thử lại (retry / 재시도) có thể làm log tỷ lệ (rate / 비율) tăng hàng chục lần.

Nếu retention chỉ được sizing theo average tỷ lệ (rate / 비율), disk có thể đầy trong sự cố (incident / 인시던트).

Sức chứa (capacity / 용량) planning log cần tính burst scenario.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Log burst** đã nêu tiêu chí phân biệt, còn **Journald tỷ lệ (rate / 비율) limiting** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Tỷ lệ (rate / 비율) limit là bảo vệ và cũng là mất mát (loss / 손실) chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journald tỷ lệ (rate / 비율) limiting

Journald có cơ chế tỷ lệ (rate / 비율) limit để tránh một dịch vụ (service / 서비스) flood toàn hệ thống.

Các cấu hình liên quan có thể gồm:

```text
RateLimitIntervalSec=
RateLimitBurst=
```

Nếu vượt giới hạn, một số messages có thể bị suppressed.

Do đó “ứng dụng (application / 애플리케이션) nói đã log” không chắc mọi message đều còn trong journal.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Journald tỷ lệ (rate / 비율) limiting** đã nêu tiêu chí phân biệt, còn **Tỷ lệ (rate / 비율) limit là bảo vệ và cũng là mất mát (loss / 손실) chế độ (mode / 모드)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Priority** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tỷ lệ (rate / 비율) limit là bảo vệ và cũng là mất mát (loss / 손실) chế độ (mode / 모드)

Tỷ lệ (rate / 비율) limiting bảo vệ disk/CPU nhưng có thể làm mất chi tiết đúng lúc sự cố (incident / 인시던트).

Thiết kế tốt cần:

- alert khi suppressed messages xuất hiện;
- log sampling hợp lý;
- không tạo thử lại (retry / 재시도) log spam;
- giữ lỗi (error / 오류) summaries quan trọng.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Tỷ lệ (rate / 비율) limit là bảo vệ và cũng là mất mát (loss / 손실) chế độ (mode / 모드)** đã nêu tiêu chí phân biệt, còn **Priority** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Structured fields** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Priority

Syslog/journal dùng priority levels như:

```text
emerg
alert
crit
err
warning
notice
info
debug
```

Filter:

```bash
journalctl -p err..alert
```

Ứng dụng (application / 애플리케이션) khung phần mềm (framework / 프레임워크) mức (level / 수준) như `ERROR`, `WARN` không phải lúc nào map hoàn hảo sang syslog priority nếu chỉ ghi plain stdout.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Structured fields** tiếp nhận điểm tựa từ **Priority** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Syslog là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Structured fields

Ứng dụng (application / 애플리케이션) có thể gửi structured fields qua journald API hoặc logger tích hợp (integration / 통합).

Điều này cho phép truy vấn (query / 쿼리) theo trường dữ liệu (field / 필드) thay vì parse message string.

Tuy nhiên nhiều Java apps vẫn gửi JSON/plain văn bản (text / 텍스트) qua stdout, sau đó centralized collector parse tiếp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Syslog là gì?** tiếp nhận điểm tựa từ **Structured fields** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Journald → rsyslog** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Syslog là gì?

Syslog là một family giao thức (protocol / 프로토콜)/convention lâu đời để chuyển log giữa applications/daemon.

Daemon như `rsyslog` có thể:

- nhận cục bộ (local / 로컬) syslog;
- đọc journal;
- ghi tệp (file / 파일);
- forward qua mạng (network / 네트워크);
- filter theo facility/priority;
- transform message.

Journald và rsyslog không nhất thiết loại trừ nhau.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Journald → rsyslog** tiếp nhận điểm tựa từ **Syslog là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **/dev/log** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journald → rsyslog

Một kiến trúc (architecture / 아키텍처) phổ biến:

```text
service
 ↓
journald
 ↓
rsyslog
 ↓
/var/log/... hoặc remote collector
```

Tùy cấu hình (config / 설정), rsyslog có thể đọc journal qua mô-đun (module / 모듈)/giao diện (interface / 인터페이스) thay vì journald forward raw socket.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **/dev/log** tiếp nhận điểm tựa từ **Journald → rsyslog** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tệp (file / 파일) logging trực tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/dev/log`

Các applications truyền thống có thể gửi syslog tới Unix socket như `/dev/log`.

Trên systemd các hệ thống (systems / 시스템들), journald có thể nhận traffic này.

Do đó dịch vụ (service / 서비스) không nhất thiết ghi stdout mới vào journal.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Tệp (file / 파일) logging trực tiếp** tiếp nhận điểm tựa từ **/dev/log** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ai nên chịu trách nhiệm rotation?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp (file / 파일) logging trực tiếp

Một Java app có thể dùng Logback/Log4j để ghi:

```text
/var/log/app/app.log
```

Khi đó chuỗi xử lý (pipeline / 파이프라인) có thể bỏ qua journald cho nghiệp vụ (business / 비즈니스) log.

Sự đánh đổi (trade-off / 트레이드오프):

- tệp (file / 파일) format/rotation do ứng dụng (application / 애플리케이션) kiểm soát;
- dễ tail;
- nhưng siêu dữ liệu (metadata / 메타데이터) systemd ít hơn;
- phải quản lý rotation và disk riêng.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Ai nên chịu trách nhiệm rotation?** tiếp nhận điểm tựa từ **Tệp (file / 파일) logging trực tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rename rotation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ai nên chịu trách nhiệm rotation?

Có ba lựa chọn thường gặp:

```text
application rotates
logrotate rotates
journal handles retention
```

Không nên để ứng dụng (application / 애플리케이션) và logrotate cùng rotate cùng một tệp (file / 파일) mà không hiểu tương tác (interaction / 상호작용).

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Rename rotation** tiếp nhận điểm tựa từ **Ai nên chịu trách nhiệm rotation?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **copytruncate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rename rotation

Một mẫu (pattern / 패턴):

```text
app.log → app.log.1
new app.log được tạo
```

Tiến trình (process / 프로세스) phải đóng/reopen tệp (file / 파일) để ghi vào tệp (file / 파일) mới.

Nếu tiến trình (process / 프로세스) vẫn giữ FD tới inode cũ, nó tiếp tục ghi vào `app.log.1` hoặc inode đã unlink.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **copytruncate** tiếp nhận điểm tựa từ **Rename rotation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tín hiệu (signal / 신호) để reopen log** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `copytruncate`

`logrotate` có option `copytruncate`:

```text
copy current file → rotated copy
truncate original file in place
```

Ưu điểm: ứng dụng (application / 애플리케이션) không cần reopen FD.

Nhược điểm: có race cửa sổ (window / 윈도우) giữa bản sao (copy / 복사) và truncate; một số log lines có thể mất hoặc duplicate.

Do đó reopen-by-signal thường tốt hơn nếu ứng dụng (application / 애플리케이션) hỗ trợ.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Tín hiệu (signal / 신호) để reopen log** tiếp nhận điểm tựa từ **copytruncate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deleted-open log** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tín hiệu (signal / 신호) để reopen log

Một số daemons nhận `SIGHUP` để reopen log files.

`logrotate` có thể có `postrotate`:

```bash
systemctl kill -s HUP service
```

Nhưng hành vi (behavior / 동작) là application-specific; không gửi HUP nếu chưa biết daemon xử lý thế nào.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Deleted-open log** tiếp nhận điểm tựa từ **Tín hiệu (signal / 신호) để reopen log** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Journal vacuum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deleted-open log

Trường hợp (case / 사례) kinh điển:

```text
admin rm app.log
process vẫn giữ FD
→ path biến mất
→ process vẫn ghi inode cũ
→ disk vẫn đầy
```

Tìm:

```bash
sudo lsof +L1
```

Fix phải làm tiến trình (process / 프로세스) close/reopen FD hoặc restart an toàn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Journal vacuum** tiếp nhận điểm tựa từ **Deleted-open log** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernel logs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Journal vacuum

Có thể giảm journal bằng:

```bash
sudo journalctl --vacuum-time=7d
sudo journalctl --vacuum-size=1G
```

Nhưng vacuum trong sự cố (incident / 인시던트) chỉ là khôi phục (recovery / 복구) hành động (action / 동작). Cần tìm tại sao log tăng và chỉnh retention/sức chứa (capacity / 용량).

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Kernel logs** tiếp nhận điểm tựa từ **Journal vacuum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhật ký kiểm tra (audit log / 감사 로그)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kernel logs

Kernel messages có thể vào journal:

```bash
journalctl -k
```

`dmesg` đọc kernel ring buffer.

Hai nguồn liên quan nhưng không hoàn toàn giống về persistence và siêu dữ liệu (metadata / 메타데이터).

Sau reboot, `dmesg` chỉ phản ánh boot hiện tại, còn persistent journal có thể giữ boot trước.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Nhật ký kiểm tra (audit log / 감사 로그)** tiếp nhận điểm tựa từ **Kernel logs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Centralized logging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhật ký kiểm tra (audit log / 감사 로그)

Linux kiểm tra (audit / 감사) subsystem có thể ghi security-relevant events qua `auditd`.

Ví dụ SELinux AVC denials thường nằm trong kiểm tra (audit / 감사) trail.

Nhật ký kiểm tra (audit log / 감사 로그) có ngữ nghĩa (semantics / 의미론) khác ứng dụng (application / 애플리케이션) log; retention và tamper resistance có thể cần nghiêm ngặt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Centralized logging** tiếp nhận điểm tựa từ **Nhật ký kiểm tra (audit log / 감사 로그)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **At-most-once và at-least-once trong log shipping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Centralized logging

Một host đơn lẻ có thể mất disk hoặc bị compromise. môi trường vận hành (production / 운영 환경) thường forward log tới hệ thống tập trung.

Mô hình tư duy (mental model / 사고 모델):

```text
application
→ local collector
→ network buffer/queue
→ centralized backend
→ index/storage
→ query/alert
```

Mỗi mũi tên là một thất bại (failure / 실패) điểm (point / 지점).

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **At-most-once và at-least-once trong log shipping** tiếp nhận điểm tựa từ **Centralized logging** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Buffer trên disk** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## At-most-once và at-least-once trong log shipping

Log forwarder có thể ưu tiên:

- low độ trễ (latency / 지연 시간) nhưng chấp nhận mất mát (loss / 손실);
- durable hàng đợi (queue / 큐) và thử lại (retry / 재시도);
- at-least-once dẫn tới duplicate.

Vì vậy centralized logs có thể thiếu hoặc duplicate entries.

Không nên giả định log chuỗi xử lý (pipeline / 파이프라인) có exactly-once ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Buffer trên disk** tiếp nhận điểm tựa từ **At-most-once và at-least-once trong log shipping** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backpressure trong logging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Buffer trên disk

Collector như Fluent Bit, véc-tơ (vector / 벡터), Filebeat hoặc rsyslog có thể buffer trên bộ nhớ (memory / 메모리)/disk.

Disk buffer giúp chịu mạng (network / 네트워크) outage nhưng cũng chiếm disk và cần sức chứa (capacity / 용량) planning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Backpressure trong logging** tiếp nhận điểm tựa từ **Buffer trên disk** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Async logging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backpressure trong logging

Nếu log sink chậm, producer/collector phải quyết định:

```text
block application?
drop logs?
buffer memory?
buffer disk?
```

Nếu synchronous logging khối (block / 블록) yêu cầu (request / 요청) luồng thực thi (thread / 스레드), outage của logging backend có thể làm nghiệp vụ (business / 비즈니스) API chậm.

Đây là coupling nguy hiểm.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Async logging** tiếp nhận điểm tựa từ **Backpressure trong logging** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Log và dữ liệu nhạy cảm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Async logging

Java logger có thể dùng async appender để tách yêu cầu (request / 요청) luồng thực thi (thread / 스레드) khỏi I/O log.

Nhưng hàng đợi (queue / 큐) hữu hạn.

Khi hàng đợi (queue / 큐) đầy, chính sách (policy / 정책) có thể khối (block / 블록) hoặc drop.

Async không xóa bottleneck; nó chỉ thêm buffer và thay hành vi khi thất bại (failure behavior / 실패 동작).

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Async logging** nêu điều cần giải thích; **Log và dữ liệu nhạy cảm** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Retention khác backup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log và dữ liệu nhạy cảm

Không log:

- password;
- truy cập (access / 접근) đơn vị từ (token / 토큰);
- full private key;
- card dữ liệu (data / 데이터);
- unnecessary personal dữ liệu (data / 데이터).

Masking phải xảy ra trước khi message đi vào chuỗi xử lý (pipeline / 파이프라인).

Xóa khỏi dashboard sau khi đã ingest không có nghĩa dữ liệu đã biến mất khỏi lưu trữ (storage / 저장소)/backup.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Log và dữ liệu nhạy cảm** nêu điều cần giải thích; **Retention khác backup** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Thời gian (time / 시간) thứ tự (ordering / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retention khác backup

Giữ log 30 ngày trong Elasticsearch không phải backup.

Retention chỉ nói dữ liệu còn truy vấn (query / 쿼리) được bao lâu.

Backup/archival cần chính sách (policy / 정책) riêng về restore và integrity.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Thời gian (time / 시간) thứ tự (ordering / 순서)** tiếp nhận điểm tựa từ **Retention khác backup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multiline dấu vết ngăn xếp (stack trace / 스택 트레이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thời gian (time / 시간) thứ tự (ordering / 순서)

Phân tán (distributed / 분산) logs không có một toàn cục (global / 전역) clock tuyệt đối hoàn hảo.

Ngay cả khi NTP đồng bộ, mạng (network / 네트워크) delay và buffering có thể làm ingestion thứ tự (order / 순서) khác sự kiện (event / 이벤트) thứ tự (order / 순서).

Nên giữ sự kiện (event / 이벤트) timestamp tại nguồn (source / 소스) và dấu vết (trace / 추적)/yêu cầu (request / 요청) ID.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Multiline dấu vết ngăn xếp (stack trace / 스택 트레이스)** tiếp nhận điểm tựa từ **Thời gian (time / 시간) thứ tự (ordering / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Log lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multiline dấu vết ngăn xếp (stack trace / 스택 트레이스)

Java exception có nhiều dòng.

Collector phải biết multiline rules, nếu không mỗi ngăn xếp (stack / 스택) frame có thể thành một log sự kiện (event / 이벤트) riêng.

Structured JSON với exception trường dữ liệu (field / 필드) có thể giúp nhưng vẫn cần chiến lược (strategy / 전략) cho dấu vết ngăn xếp (stack trace / 스택 트레이스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Log lược đồ (schema / 스키마)** tiếp nhận điểm tựa từ **Multiline dấu vết ngăn xếp (stack trace / 스택 트레이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cardinality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log lược đồ (schema / 스키마)

Một lược đồ (schema / 스키마) tốt thường có:

```text
timestamp
level
service
host / instance
request_id / trace_id
logger
message
error_type
stack_trace
```

Không phải mọi sự kiện (event / 이벤트) cần mọi trường dữ liệu (field / 필드), nhưng consistency giúp truy vấn (query / 쿼리).

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Cardinality** tiếp nhận điểm tựa từ **Log lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một trường hợp (case / 사례): API độ trễ (latency / 지연 시간) tăng cùng log volume** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cardinality

Trường dữ liệu (field / 필드) như `user_id`, `request_id` có cardinality rất cao.

Chỉ mục (index / 인덱스) mọi trường dữ liệu (field / 필드) cardinality cao có thể làm logging backend tốn bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소).

Khả năng quan sát (observability / 관측 가능성) lược đồ (schema / 스키마) cần cân bằng truy vấn (query / 쿼리) usefulness với chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Cardinality** cho ta quy tắc; **Một trường hợp (case / 사례): API độ trễ (latency / 지연 시간) tăng cùng log volume** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례): disk đầy nhưng du không thấy tệp (file / 파일) lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một trường hợp (case / 사례): API độ trễ (latency / 지연 시간) tăng cùng log volume

Chuỗi có thể là:

```text
upstream timeout
→ retry
→ mỗi retry ghi stack trace
→ log volume tăng 100×
→ async queue đầy
→ logging chuyển sang block
→ request threads chờ logger
→ API latency tăng
```

Log lúc này không chỉ là bằng chứng; nó trở thành một phần nguyên nhân.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Một trường hợp (case / 사례): API độ trễ (latency / 지연 시간) tăng cùng log volume** cho ta quy tắc; **Trường hợp (case / 사례): disk đầy nhưng du không thấy tệp (file / 파일) lớn** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례): journal không có log boot trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): disk đầy nhưng `du` không thấy tệp (file / 파일) lớn

Khả năng:

```text
logrotate/unlink
→ process giữ old FD
→ `ls` không thấy
→ `df` vẫn đầy
```

Kiểm tra:

```bash
sudo lsof +L1
```

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Trường hợp (case / 사례): disk đầy nhưng du không thấy tệp (file / 파일) lớn** cho ta quy tắc; **Trường hợp (case / 사례): journal không có log boot trước** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례): centralized logging mất vài phút dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): journal không có log boot trước

Kiểm tra:

```bash
journalctl --list-boots
ls -ld /var/log/journal
```

Nếu lưu trữ (storage / 저장소) volatile, log boot cũ có thể đã mất.

Đây là thiết kế (design / 설계) quyết định (decision / 결정) cần sửa trước sự cố (incident / 인시던트) tiếp theo.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Trường hợp (case / 사례): journal không có log boot trước** cho ta quy tắc; **Trường hợp (case / 사례): centralized logging mất vài phút dữ liệu** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례): centralized logging mất vài phút dữ liệu

Cần kiểm tra từng đoạn:

```text
application emitted?
local journal/file có entry?
collector đọc được?
collector queue/backpressure?
network tới backend?
backend ingest/index?
query filter/timezone đúng?
```

Không nên kết luận “ứng dụng (application / 애플리케이션) không log” chỉ vì dashboard không thấy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Journald, rsyslog và đường đi của nhật ký trong Linux**, các dấu vết trong **Trường hợp (case / 사례): centralized logging mất vài phút dữ liệu** được đọc cùng nhau ở **Mô hình tư duy** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Log là một chuỗi xử lý (pipeline / 파이프라인) dữ liệu:

```text
producer
→ local transport
→ local storage/buffer
→ shipper
→ network
→ central backend
→ index/query
```

Mỗi tầng (layer / 계층) có buffering, retention, tỷ lệ (rate / 비율) limit và dạng thất bại (failure mode / 실패 모드) riêng.

> **Chuyển mạch:** Trong **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“Journal có log nghĩa centralized backend chắc chắn có.”** Forwarder/mạng (network / 네트워크)/backend có thể lỗi.

**“Logrotate xóa tệp (file / 파일) là giải phóng disk.”** Không nếu tiến trình (process / 프로세스) còn giữ FD.

**“Async logging không ảnh hưởng ứng dụng (application / 애플리케이션).”** hàng đợi (queue / 큐) đầy vẫn có thể khối (block / 블록) hoặc drop.

**“Càng nhiều gỡ lỗi (debug / 디버그) càng dễ điều tra.”** Có thể tạo noise, chi phí (cost / 비용) và thậm chí I/O bottleneck.

**“Centralized log là nguồn chuẩn (source of truth / 정본) tuyệt đối.”** chuỗi xử lý (pipeline / 파이프라인) có thể drop, duplicate hoặc reorder events.

> **Chuyển mạch:** Ở chặng này của **Journald, rsyslog và đường đi của nhật ký trong Linux**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc [VFS/page cache/writeback](../01_filesystem/vfs_page_cache_writeback.md) để hiểu log I/O, [Time/clock/NTP](./time_clock_ntp.md) để hiểu timestamp correlation, và [Observability/tracing](../09_production/observability_tracing_strace_perf.md) để kết hợp log với metrics và tracing.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
