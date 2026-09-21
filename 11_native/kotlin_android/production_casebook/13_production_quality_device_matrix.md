# Case 13 — Production Quality: Device Matrix, Localization, Battery, Privacy và Release Readiness

Một Android app có thể compile, pass unit test và chạy tốt trên điện thoại developer nhưng vẫn thất bại production vì khác OS version, OEM, locale, font scale, network condition, screen size, battery policy hoặc migration path. Quality engineering mobile vì vậy không chỉ là “test nhiều hơn”; nó là xây **risk matrix** phản ánh môi trường thật.

Chapter này là lớp kiểm tra cuối của toàn bộ Kotlin + Android Master Notes. Mục tiêu là biết một feature “ready for production” nghĩa là gì ngoài happy path.

# 1. Android là một platform matrix

Production Android tồn tại trên nhiều chiều:

```text
OS version
× target SDK behavior
× OEM implementation
× RAM/CPU class
× screen/window size
× locale/font scale/RTL
× network quality
× permission state
× battery state
× account/data history
× app upgrade path
```

Bạn không thể test Cartesian product đầy đủ. Vì vậy cần chọn matrix theo **risk**.

# 2. Risk-based device matrix

Một matrix tối thiểu thường nên có:

| Nhóm | Mục đích |
|---|---|
| min/near-min API | compatibility cũ |
| latest stable API | behavior mới |
| target-SDK migration API | policy/permission mới |
| low/mid/high device | performance/memory |
| Samsung/Pixel + OEM quan trọng | vendor difference |
| small phone | compact layout |
| large/tablet/foldable nếu support | adaptive UI |

Nếu app phụ thuộc BLE/camera/NFC, thêm physical hardware representative thay vì chỉ emulator.

# 3. Test upgrade path, không chỉ fresh install

Fresh install bỏ qua một lớp bug lớn: schema cũ, SharedPreferences cũ, token cũ, cached file cũ, notification channel cũ và data migration.

Release test nên có:

```text
version N production data
→ install N+1
→ migrate
→ launch critical flow
→ background/restore
→ rollback strategy nếu có
```

Room migration phải test từ các schema version thực tế còn user ngoài production, không chỉ previous version gần nhất nếu user có thể skip nhiều release.

# 4. Downgrade và rollback compatibility

Play rollback không phải lúc nào tương đương cài APK cũ đơn giản; server/API/schema có thể đã thay đổi.

Khi staged rollout version N+1 ghi data format mà N không đọc được, rollback app binary có thể làm user crash.

Senior release design hỏi trước:

```text
N+1 thay local schema thế nào?
server contract backward compatible bao lâu?
feature flag có disable behavior mới không?
rollback binary có đọc dữ liệu mới được không?
```

# Localization

## 5. String resource, không hardcode UI text

User-facing string nên ở resource để localize, test và thay đổi theo locale.

```xml
<string name="order_count">%1$d orders</string>
```

Nhưng plural phải dùng plural resource thay vì nối số + noun thủ công.

## 6. Plural

Ngôn ngữ không có cùng plural rule. Dùng `<plurals>`/quantity string để framework chọn form.

Đừng giả định chỉ singular/plural kiểu English.

## 7. Format number/currency/date theo locale

Không tự format:

```kotlin
"$price USD"
```

nếu UI cần locale-aware display. Dùng formatter thích hợp cho currency/number/date.

Domain value giữ semantic chuẩn; formatting là presentation concern.

## 8. Time zone

Timestamp server nên có semantic rõ: instant tuyệt đối hay local business date/time.

`2026-09-20 09:00` không đủ nếu không biết timezone/context.

Phân biệt:

```text
Instant → một thời điểm tuyệt đối
LocalDate → ngày lịch không timezone
LocalDateTime → local clock chưa gắn zone
ZonedDateTime → local time + zone
```

Mobile travel qua timezone dễ làm bug calendar/reminder nếu model sai từ đầu.

## 9. Locale change runtime

Locale có thể đổi khi process/app đang tồn tại. Đừng cache formatted string global vô hạn.

UI nên derive display text từ resource/formatter theo current configuration.

# RTL

## 10. Start/end thay left/right

Layout direction phải support RTL khi app localize Arabic/Hebrew. Dùng start/end cho alignment/margin khi semantic directional.

Icon có direction như arrow/back có thể cần auto-mirror.

## 11. BiDi text

Mixed Latin/Arabic/number/URL có thể render direction khó. Không tự đảo string. Dùng platform text handling và test real locale.

# Font scaling và accessibility

## 12. Large text

User có thể tăng font scale. Fixed-height container dễ cắt text.

Đừng design button/card theo một screenshot size duy nhất. Cho text wrap hoặc layout adapt.

## 13. Screen reader

Critical flow phải test manual với TalkBack ít nhất theo release cadence phù hợp. Semantics automated test giúp nhưng không thay trải nghiệm nghe thật.

## 14. Color/contrast

Không truyền trạng thái chỉ bằng màu. Error/success/selected nên có text/icon/semantic state.

Dark mode và dynamic color có thể thay contrast; custom color cần test cả theme.

# Battery và background quality

## 15. Wakeup cost

Mỗi periodic task, location update, sensor listener, BLE scan và network poll có battery cost. Một app có nhiều team dễ tạo “death by a thousand timers”.

Background work cần inventory tập trung:

```text
job name
owner
frequency
constraints
network cost
battery reason
user-visible benefit
```

## 16. Batch thay polling khi có thể

Nếu backend hỗ trợ push/stream/event, không nhất thiết poll 5 phút. Nếu work không cần exact time, để WorkManager/system batch giúp battery.

## 17. Doze/App Standby

Background execution có thể bị delay khi device idle. Business logic không nên assume periodic worker chạy chính xác từng phút.

Nếu product yêu cầu hard realtime, cần architecture/server push/user-visible foreground behavior phù hợp hơn.

# Network quality

## 18. Test slow network

Wi-Fi văn phòng che giấu race/loading bug. Test latency cao, packet loss, offline giữa request, reconnect và server timeout.

UI cần distinguish loading initial và refreshing existing content.

## 19. Retry storm

Nếu 1 triệu device cùng retry ngay sau backend outage, exponential backoff + jitter giúp tránh thundering herd.

Retry policy là distributed-system concern.

## 20. Payload size

Mobile network đắt và không ổn định. API contract cần pagination, compression, selective fields/caching khi dataset lớn.

Đừng download full history mỗi app launch.

# Memory/CPU quality

## 21. Low-memory device

Test device RAM thấp giúp phát hiện bitmap cache, giant list, WebView/media memory và startup overhead.

Background process có thể bị kill thường xuyên hơn, làm state restoration bug lộ ra.

## 22. Thermal throttling

CPU benchmark kéo dài có thể khác khi device nóng. Heavy camera/ML/video feature nên test thermal/battery thực tế chứ không chỉ một run ngắn.

# OEM fragmentation

## 23. Không giả định mọi OEM giống Pixel

Một số OEM có aggressive battery/background management, camera/Bluetooth stack khác hoặc permission UI khác.

Không viết code “detect Samsung rồi hack” ngay từ đầu. Trước tiên dựa public API; chỉ có workaround khi có evidence, isolate workaround và document scope/version.

# Security quality

## 24. Debug feature không lọt production

Release build phải kiểm tra:

```text
no debug endpoint
no trust-all certificate
no verbose sensitive logging
no test account secret
no WebView debugging ngoài ý muốn
no backup exposure ngoài policy
```

Build variant/configuration nên khiến insecure debug behavior khó lọt release.

## 25. Log redaction

Token, password, full card/account identifier, sensitive PII không nên log. Structured logging nên redaction từ source thay vì hy vọng dashboard filter sau.

## 26. Screenshot/screen recording sensitivity

Một số screen như credential/payment/health có thể cần `FLAG_SECURE` hoặc policy tương đương tùy requirement. Nhưng đừng bật toàn app nếu làm hỏng legitimate user workflow không cần thiết.

# Privacy quality

## 27. Data inventory

Trước release, biết app thu dữ liệu gì:

```text
field/event
purpose
storage location
retention
third-party recipient
user control
```

Nếu team không biết event analytics chứa gì, rất khó đảm bảo privacy hoặc Data Safety declaration đúng.

## 28. Data minimization

Không gửi raw GPS/contacts/device identifier nếu business chỉ cần derived region/count.

Privacy tốt thường bắt đầu bằng **không thu dữ liệu không cần**.

# Analytics và observability

## 29. Analytics khác telemetry reliability

Product analytics trả lời user làm gì. Operational telemetry trả lời app có khỏe không.

Đừng dùng event analytics như crash/trace system thay thế.

## 30. Event schema versioning

Analytics event là contract với data pipeline. Rename field tùy tiện phá dashboard/experiment.

```text
checkout_started.v1
checkout_completed.v1
```

không nhất thiết phải version trong tên, nhưng cần governance/schema contract rõ.

## 31. Crash-free không đủ

App không crash vẫn có thể slow, ANR, login loop hoặc sync fail silent. Monitor thêm ANR, startup, jank, network error, sync backlog và business invariant quan trọng.

# Feature flag

## 32. Flag là migration tool, không phải rác vĩnh viễn

Feature flag giúp rollout/kill-switch. Nhưng flag cũ tạo combinatorial complexity.

Mỗi flag cần owner, default, expiry/removal plan.

## 33. Server-driven flag và offline

App offline cần default/cached flag behavior. Không để app startup block vô hạn chờ config remote.

# Release pipeline

## 34. Quality gate

Một pipeline production có thể gồm:

```text
compile
→ unit test
→ lint/static analysis
→ integration test
→ instrumentation smoke
→ assemble/sign
→ artifact scan
→ internal track
→ staged rollout
→ monitor
→ expand / pause / rollback
```

Không phải team nào cần mọi gate trên mỗi PR; phân lớp theo cost và risk.

## 35. Signed artifact là immutable output

Artifact đã QA/review nên chính là artifact được promote. Tránh rebuild khác config giữa staging và production nếu không cần, vì bạn mất traceability.

## 36. Version code

`versionCode` phải tăng để Play update. `versionName` là display version. Build metadata/commit SHA nên được trace trong observability để biết crash đến từ artifact nào.

# Play/App distribution awareness

## 37. AAB và dynamic delivery

Android App Bundle cho Play generate APK tối ưu theo device. Nếu app dùng dynamic feature/module/resource delivery, test install/update path thực tế trên distribution track chứ không chỉ local APK.

## 38. Target API deadline

Google Play thay đổi target API requirement theo thời gian. Release engineering phải có cadence upgrade trước deadline, không đợi tuần cuối mới nâng target và xử lý tất cả behavior change cùng lúc.

# Backup và restore

## 39. Auto Backup không phải luôn desirable cho mọi data

Token/secret/device-bound credential có thể không nên restore sang device mới. Database/user preference khác có thể benefit từ backup.

Review backup rule theo data sensitivity và server rehydration capability.

## 40. Restore version mismatch

Backup từ app version cũ có thể được restore vào version mới. Persistence layer phải xử lý schema/data version đúng.

# Test account và seed data

## 41. Production-like state

QA cần account/data mô phỏng:

```text
new user
heavy user
expired session
offline pending mutations
legacy schema data
restricted entitlement
large dataset
```

Happy-path empty account không phát hiện nhiều bug production.

# Incident readiness

## 42. Mobile incident khác server incident

Server fix có thể deploy phút. Mobile binary đã nằm trên hàng triệu device không update ngay.

Do đó cần:

```text
server backward compatibility
feature kill switch
config fallback
staged rollout
old-client support window
```

## 43. Diagnose theo version/device cohort

Khi crash tăng, breakdown theo app version, OS, OEM/device model, locale, feature flag cohort và rollout percentage giúp tìm regression nhanh.

# Definition of Done production

## 44. Feature complete không chỉ UI xong

Một feature quan trọng chỉ nên xem production-ready khi đã trả lời:

```text
state restore thế nào?
offline thế nào?
permission denied thế nào?
loading/error/retry thế nào?
accessibility thế nào?
locale/large font/RTL thế nào?
small/large window thế nào?
analytics/telemetry gì?
data sensitive gì?
test migration gì?
rollback thế nào?
```

Không phải mọi feature cần cùng mức rigor; payment/auth/sync cần sâu hơn tooltip đơn giản. Nhưng câu hỏi phải được cân nhắc.

# Senior Notes

## 45. Quality là architecture property

Nếu code không có clear source of truth, không thể test offline đúng. Nếu navigation truyền giant object, process restore khó. Nếu networking không typed error, UI recovery mơ hồ. QA không thể “test ra” một architecture thiếu recovery path.

## 46. Matrix phải dựa telemetry

Sau production, dùng crash/device/OS/user distribution để cập nhật test matrix. Nếu 40% user dùng một OEM cụ thể, device đó quan trọng hơn một flagship hiếm.

## 47. Backward compatibility là mobile superpower

Server/API có khả năng phục vụ nhiều app version giúp rollout an toàn, incident recovery nhanh và user không bị bắt update ngay.

## 48. Không tối ưu metric đơn lẻ

Giảm startup bằng lazy quá mức có thể làm first interaction lag. Giảm network request bằng cache quá lâu có thể stale. Giảm permission prompt bằng broad permission xin một lần có thể tệ privacy. Tối ưu luôn dựa user journey và system trade-off.

# Release-readiness checklist rút gọn

Trước release lớn, review theo nhóm: compatibility/version; persistence/migration; permission/capability; lifecycle/process death; offline/network; localization/RTL/font scale; accessibility; adaptive UI; memory/performance/battery; security/privacy; analytics/observability; CI/signing/artifact; staged rollout/rollback.

Checklist không thay reasoning. Nếu một mục “N/A”, team nên biết vì sao N/A.

# Kết thúc chapter

Sau chapter này, bạn nên có khả năng xây device/test matrix theo risk; test upgrade thay vì chỉ fresh install; phân biệt localization, timezone và RTL concern; đưa font scaling/accessibility vào correctness; đánh giá battery/background work; test slow/offline network; theo dõi OEM/low-memory behavior; quản privacy/data inventory; thiết kế feature flag/rollout; và định nghĩa production-ready feature dựa trên recovery, compatibility và observability chứ không chỉ screenshot đúng thiết kế.
