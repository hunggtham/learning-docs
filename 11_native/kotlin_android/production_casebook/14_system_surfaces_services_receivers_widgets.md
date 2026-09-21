# Case 14 — Android System Surfaces: Service, Receiver, Provider, Notification, Widget, Shortcut và Tile

Một lỗi tư duy phổ biến khi học Android hiện đại là coi app = một Activity chứa Compose. Trên thực tế Android là component platform. Hệ thống, app khác hoặc user có thể tương tác với app qua notification, broadcast, content URI, widget, shortcut, tile, service hoặc deep link ngay cả khi Activity chính chưa tồn tại.

Chapter này nối component model truyền thống với architecture hiện đại. Mục tiêu không phải quay lại style “mọi logic trong Service”, mà hiểu **entry point nào được system tạo, lifetime nào áp dụng, process có thể ở trạng thái nào, dữ liệu nào được phép tin và work nào phải được chuyển sang owner bền hơn**.

# 1. Mỗi Android component là một entry point độc lập

App có thể được process-start bởi:

```text
Activity launch
BroadcastReceiver
Service
ContentProvider access
Job/WorkManager infrastructure
Notification PendingIntent
App Widget interaction
Shortcut/deep link
```

Vì vậy đừng assume `MainActivity` hoặc flow initialization nào đó đã chạy trước.

Nếu dependency graph chỉ được setup bằng code trong Activity, receiver/service có thể fail khi system tạo nó trực tiếp.

Process-wide initialization cần nằm ở layer phù hợp như `Application`/DI initialization, nhưng vẫn phải nhẹ để không làm cold-start của mọi component nặng lên.

# 2. Activity là user-facing task surface, không phải application singleton

Activity đại diện một UI entry/window trong task. Nhiều Activity có thể tồn tại hoặc app có thể single-activity với Navigation Compose.

Dù architecture nào, Activity không nên sở hữu durable business state. Nó là lifecycle/window owner, wiring surface và nơi integrate system UI/activity-result/deep-link theo boundary phù hợp.

# Service

## 3. Service không đồng nghĩa background thread

`Service` lifecycle callback mặc định chạy trên main thread của process. Nếu làm blocking work trực tiếp trong `onStartCommand()`, app vẫn có thể ANR.

Service là component/lifetime abstraction, không phải thread abstraction.

Nếu service cần asynchronous work, nó vẫn phải dùng coroutine/executor phù hợp và quản cancellation/resource.

## 4. Started service và bound service

Started service được start để thực hiện nhiệm vụ theo lifecycle service. Bound service expose interface cho client bind và gọi.

Bound service hữu ích cho long-lived local/remote service interaction, nhưng phần lớn app CRUD thông thường không cần tự tạo bound service.

## 5. Foreground service

Foreground service dùng cho công việc user-noticeable đang diễn ra mà platform cho phép: navigation, media playback, active recording/tracking theo policy và foreground-service type phù hợp.

Nó phải hiển thị notification và không phải loophole để giữ process sống.

Nếu work có thể trì hoãn, durable và không cần chạy ngay liên tục, WorkManager thường đúng hơn.

## 6. Service restart semantics

`onStartCommand()` trả mode như `START_NOT_STICKY`, `START_STICKY`, `START_REDELIVER_INTENT` theo contract. Không chọn `START_STICKY` chỉ vì muốn service “không chết”.

Process vẫn có thể bị kill; service có thể được recreate tùy semantics nhưng in-memory state mất. Durable task phải persist progress/input nếu cần recovery.

# BroadcastReceiver

## 7. Receiver phải làm ít và nhanh

BroadcastReceiver là entry point ngắn. `onReceive()` không phải nơi upload database lớn hoặc sync 5 phút.

Flow tốt:

```text
broadcast arrives
→ validate/filter
→ persist minimal event/input
→ enqueue WorkManager nếu cần durable work
→ return
```

## 8. `goAsync()` không biến receiver thành service vô hạn

`goAsync()` cho phép hoàn thành một ít async work sau `onReceive`, nhưng vẫn có time/lifetime constraint. Dùng cho operation ngắn; durable/long work vẫn nên chuyển WorkManager.

## 9. Exported receiver

Receiver exported nhận input từ ngoài app phải coi Intent là untrusted. Validate action/extras và dùng permission protection nếu use case yêu cầu.

Dynamic receiver registration cũng cần lifetime unregister đúng và flag exported/not-exported phù hợp API/version.

# ContentProvider

## 10. Provider là data IPC boundary

ContentProvider expose structured data/URI interface giữa process/app. Android system sử dụng provider concept cho contacts/media/document và app có thể tạo provider riêng.

Nó không chỉ là “database wrapper”. Provider là IPC/security/versioning boundary.

## 11. `ContentResolver`

Client truy cập provider qua `ContentResolver`:

```kotlin
contentResolver.query(
    uri,
    projection,
    selection,
    selectionArgs,
    sortOrder
)
```

Production code cần close Cursor/resource bằng `use` và không query khối lượng lớn trên main thread.

## 12. URI permission

Provider có thể grant temporary URI permission thay vì expose toàn data store. Đây là principle of least privilege ở data-sharing layer.

## 13. FileProvider

`FileProvider` là ContentProvider đặc biệt để share file private bằng content URI. Nó giúp tránh `file://` exposure và cho grant read/write tạm thời.

# Notification

## 14. Notification là system surface, không chỉ UI banner

Notification tồn tại ngoài Activity lifecycle, có thể được user tap khi process chết. Vì vậy `PendingIntent` phải reconstruct navigation từ durable/typed identifier.

Không dựa vào singleton memory khi handling notification tap.

## 15. Stable notification ID

Nếu cùng logical job/update cần update existing notification, dùng stable ID. Random ID mỗi lần tạo spam notification.

Ví dụ download progress:

```text
notificationId = hash(downloadId)
```

## 16. Channel semantics

Channel nên đại diện category user hiểu. Importance/sound sau khi channel tồn tại phần lớn thuộc user control.

Đừng version channel theo mỗi release để reset preference user.

## 17. Action button

Notification action có thể trigger receiver/service/activity qua PendingIntent. Action handler phải idempotent nếu user tap nhiều hoặc PendingIntent được redeliver trong edge case.

# PendingIntent

## 18. PendingIntent là capability token

Khi app tạo PendingIntent, app cho system/other component quyền thực hiện một Intent với identity của app trong phạm vi nhất định.

Vì vậy uniqueness, mutability và payload đều là security/correctness concern.

## 19. Immutable mặc định

Nếu use case không cần external party fill/change Intent, dùng immutable.

Mutable chỉ khi platform API thực sự cần mutate, ví dụ một số inline reply/interaction contract.

## 20. PendingIntent identity

Hai PendingIntent có thể được system coi là cùng identity dựa trên Intent fields/request code; extras không phải lúc nào tham gia equality như developer tưởng.

Nếu notification action cho item khác nhau, cần đảm bảo request/data/action tạo identity đúng để không reuse nhầm extras.

# App Widget

## 21. Widget không phải mini Activity

App Widget render qua `RemoteViews` hoặc Glance abstraction tùy implementation. Nó chạy dưới constraint system surface, update/lifecycle khác Compose screen.

Không cố nhúng arbitrary UI logic từ screen vào widget.

## 22. Widget state

Widget có thể tồn tại lâu hơn process. State quan trọng phải đến từ persistent source of truth.

Nếu user pin nhiều widget instance, mỗi `appWidgetId` có configuration/state riêng.

## 23. Update frequency

Periodic widget update quá thường xuyên tốn battery và bị platform constraint. Event-driven update khi data đổi thường tốt hơn polling ngắn.

## 24. Widget memory

RemoteViews payload có resource/memory constraint. Android 17 tăng enforcement rõ hơn với Bitmap/Icon memory trong RemoteViews cho target 37+, vì vậy không gửi bitmap khổng lồ vào widget.

# App Shortcut

## 25. Static và dynamic shortcut

Shortcut giúp user nhảy trực tiếp vào action/destination. Static shortcut phù hợp action cố định; dynamic shortcut phù hợp entity/action thay đổi theo user usage.

Shortcut phải mở được flow đúng khi process cold-start.

## 26. Shortcut ID là contract

Nếu shortcut đại diện conversation/order, ID cần ổn định để update/remove đúng. Không encode secret trực tiếp vào shortcut ID/Intent.

# Quick Settings Tile

## 27. Tile là quick system control

Tile phù hợp action trạng thái đơn giản user muốn truy cập nhanh, ví dụ toggle VPN-like feature hoặc start/stop service hợp lệ.

Tile service có lifecycle riêng; đừng assume Activity exists.

## 28. Tile state phải phản ánh truth

Nếu tile hiển thị active/inactive nhưng underlying service fail, UI hệ thống sai. State phải derive từ source of truth và update khi actual status đổi.

# Deep link và external navigation

## 29. Entry từ system phải reconstruct graph

Notification, widget, shortcut, app link đều có thể mở app từ cold process. Navigation code nên xử lý theo typed destination + domain identifier.

Ví dụ:

```text
notification(orderId=42)
→ launch app
→ session check
→ load order 42
→ authorization check
→ navigate detail
```

Không serialize whole `Order` object vào PendingIntent.

# Multi-process awareness

## 30. `android:process`

Một số component/library có thể chạy process riêng. Khi đó singleton, DI graph, static cache và memory state tách biệt.

Đa số app không cần custom multi-process. Chỉ dùng khi platform/library requirement rõ vì complexity tăng mạnh: IPC, initialization, data consistency, logging và crash behavior.

# WorkManager và system components

## 31. Receiver/Service không thay WorkManager

WorkManager quản durable deferrable work với constraints/retry/persistence. Receiver là event entry, service là component lifetime, foreground service là user-visible long work.

Một architecture tốt thường phối hợp:

```text
BroadcastReceiver
→ enqueue unique WorkManager work
→ repository transaction
→ database source of truth
→ notification update nếu cần
```

## 32. Unique work

Nếu cùng sync event tới nhiều lần, unique work policy giúp deduplicate/coalesce theo business semantics.

Nhưng đừng dùng unique work để che underlying idempotency bug; server/local mutation vẫn nên idempotent khi cần.

# Process initialization

## 33. ContentProvider có thể khởi tạo rất sớm

Một số library dùng provider-based initializer để chạy trước `Application.onCreate()`. Điều này tiện nhưng có startup cost.

Khi audit cold start, nhớ initialization có thể đến từ manifest/provider chứ không chỉ code bạn thấy trong Application.

## 34. App Startup

Jetpack App Startup cung cấp cách quản initializer/dependency rõ hơn cho library/app initialization, nhưng vẫn cần lazy/defer khi initialization không cần trước first frame.

# Security

## 35. Component attack surface

Review manifest:

```text
exported Activity
exported Service
exported Receiver
exported Provider
intent-filter
permission protection
URI grant
```

Mỗi exported component là API surface của app.

## 36. Explicit Intent cho internal call

Nếu target component nội bộ đã biết, explicit Intent giảm ambiguity/hijacking so với implicit Intent không cần thiết.

## 37. Signature permission

Trong ecosystem nhiều app cùng tổ chức và signing control, signature-level permission có thể protect IPC giữa app. Nhưng certificate rotation/distribution architecture cần tính trước.

# Testing system surfaces

## 38. Cold-start test

Mỗi entry point quan trọng nên test khi process chưa tồn tại:

```text
kill process
→ tap notification
→ expected screen/data
```

Tương tự widget/shortcut/deep link.

## 39. Duplicate delivery

Test notification action/broadcast/work event lặp. Business mutation không được double-charge/double-submit.

## 40. Permission/export security test

Thử gửi malformed Intent từ adb/test app tới exported component. Validate app không crash và không thực hiện privileged action trái phép.

# Senior Notes

## 41. System surface là public contract

Notification action, shortcut, deep link, provider URI hoặc exported receiver đều có thể sống qua nhiều app version. Thay contract cần migration/versioning mindset.

## 42. Entry point mỏng

Component callback nên chủ yếu parse/validate → delegate. Business logic ở repository/use case giúp reuse và test.

## 43. Reconstruct thay vì transport giant state

System surface nên truyền stable ID/intention, sau đó app reconstruct state từ source of truth. Đây là pattern chung nối navigation, Binder limit, process death và security.

## 44. Không dùng component để chống process death

Service/widget/provider không phải mẹo để giữ app sống. Android architecture tốt giả định process có thể mất và state có thể reconstruct.

# Checklist kết thúc chapter

Bạn nên giải thích được vì sao Service không phải background thread; Receiver vì sao phải ngắn; ContentProvider là IPC/data security boundary; notification tap phải hoạt động từ cold process; PendingIntent vì sao là capability token; widget/shortcut/tile có lifecycle khác Activity; WorkManager khác Service/Receiver; multi-process làm singleton sai thế nào; và vì sao exported component cần được review như một public API/security surface.
