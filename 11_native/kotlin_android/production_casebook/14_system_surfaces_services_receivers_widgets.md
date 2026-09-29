# Trường hợp (case / 사례) 14 — Android hệ thống (system / 시스템) Surfaces: dịch vụ (service / 서비스), Receiver, Provider, Notification, Widget, Shortcut và Tile

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 14 — Android hệ thống (system / 시스템) Surfaces: dịch vụ (service / 서비스), Receiver, Provider, Notification, Widget, Shortcut và Tile** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **3. dịch vụ (service / 서비스) không đồng nghĩa background luồng thực thi (thread / 스레드)** sang **4. Started dịch vụ (service / 서비스) và bound dịch vụ (service / 서비스)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một lỗi tư duy phổ biến khi học Android hiện đại là coi app = một Activity chứa Compose. Trên thực tế Android là thành phần (component / 컴포넌트) nền tảng (platform / 플랫폼). Hệ thống, app khác hoặc người dùng (user / 사용자) có thể tương tác với app qua notification, broadcast, content URI, widget, shortcut, tile, dịch vụ (service / 서비스) hoặc deep link ngay cả khi Activity chính chưa tồn tại.

Chapter này nối thành phần (component / 컴포넌트) mô hình (model / 모델) truyền thống với kiến trúc (architecture / 아키텍처) hiện đại. Mục tiêu không phải quay lại style “mọi lô-gic (logic / 논리) trong dịch vụ (service / 서비스)”, mà hiểu **entry điểm (point / 지점) nào được hệ thống (system / 시스템) tạo, thời gian tồn tại (lifetime / 수명) nào áp dụng, tiến trình (process / 프로세스) có thể ở trạng thái nào, dữ liệu nào được phép tin và công việc (work / 작업) nào phải được chuyển sang đơn vị sở hữu (owner / 오너) bền hơn**.

# 1. Mỗi Android thành phần (component / 컴포넌트) là một entry điểm (point / 지점) độc lập

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

Vì vậy đừng assume `MainActivity` hoặc luồng (flow / 흐름) initialization nào đó đã chạy trước.

Nếu phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) chỉ được setup bằng mã (code / 코드) trong Activity, receiver/dịch vụ (service / 서비스) có thể thất bại (fail / 실패) khi hệ thống (system / 시스템) tạo nó trực tiếp.

Process-wide initialization cần nằm ở tầng (layer / 계층) phù hợp như `Application`/DI initialization, nhưng vẫn phải nhẹ để không làm cold-start của mọi thành phần (component / 컴포넌트) nặng lên.

# 2. Activity là user-facing tác vụ (task / 작업) surface, không phải ứng dụng (application / 애플리케이션) singleton

Activity đại diện một UI entry/cửa sổ (window / 윈도우) trong tác vụ (task / 작업). Nhiều Activity có thể tồn tại hoặc app có thể single-activity với điều hướng (navigation / 내비게이션) Compose.

Dù kiến trúc (architecture / 아키텍처) nào, Activity không nên sở hữu durable nghiệp vụ (business / 비즈니스) trạng thái (state / 상태). Nó là vòng đời (lifecycle / 생명주기)/cửa sổ (window / 윈도우) đơn vị sở hữu (owner / 오너), wiring surface và nơi integrate hệ thống (system / 시스템) UI/activity-result/deep-link theo ranh giới (boundary / 경계) phù hợp.

# Dịch vụ (service / 서비스)

## 3. dịch vụ (service / 서비스) không đồng nghĩa background luồng thực thi (thread / 스레드)

`Service` vòng đời (lifecycle / 생명주기) callback mặc định chạy trên main luồng thực thi (thread / 스레드) của tiến trình (process / 프로세스). Nếu làm blocking công việc (work / 작업) trực tiếp trong `onStartCommand()`, app vẫn có thể ANR.

Dịch vụ (service / 서비스) là thành phần (component / 컴포넌트)/thời gian tồn tại (lifetime / 수명) lớp trừu tượng (abstraction / 추상화), không phải luồng thực thi (thread / 스레드) lớp trừu tượng (abstraction / 추상화).

Nếu dịch vụ (service / 서비스) cần asynchronous công việc (work / 작업), nó vẫn phải dùng coroutine/executor phù hợp và quản cancellation/tài nguyên (resource / 자원).

## 4. Started dịch vụ (service / 서비스) và bound dịch vụ (service / 서비스)

Started dịch vụ (service / 서비스) được start để thực hiện nhiệm vụ theo vòng đời (lifecycle / 생명주기) dịch vụ (service / 서비스). Bound dịch vụ (service / 서비스) expose giao diện (interface / 인터페이스) cho máy khách (client / 클라이언트) bind và gọi.

Bound dịch vụ (service / 서비스) hữu ích cho long-lived cục bộ (local / 로컬)/remote dịch vụ (service / 서비스) tương tác (interaction / 상호작용), nhưng phần lớn app CRUD thông thường không cần tự tạo bound dịch vụ (service / 서비스).

## 5. Foreground dịch vụ (service / 서비스)

Foreground dịch vụ (service / 서비스) dùng cho công việc user-noticeable đang diễn ra mà nền tảng (platform / 플랫폼) cho phép: điều hướng (navigation / 내비게이션), media playback, active recording/tracking theo chính sách (policy / 정책) và foreground-service kiểu (type / 타입) phù hợp.

Nó phải hiển thị notification và không phải loophole để giữ tiến trình (process / 프로세스) sống.

Nếu công việc (work / 작업) có thể trì hoãn, durable và không cần chạy ngay liên tục, WorkManager thường đúng hơn.

## 6. dịch vụ (service / 서비스) restart ngữ nghĩa (semantics / 의미론)

`onStartCommand()` trả chế độ (mode / 모드) như `START_NOT_STICKY`, `START_STICKY`, `START_REDELIVER_INTENT` theo đặc tả hợp đồng (contract / 계약). Không chọn `START_STICKY` chỉ vì muốn dịch vụ (service / 서비스) “không chết”.

Tiến trình (process / 프로세스) vẫn có thể bị kill; dịch vụ (service / 서비스) có thể được recreate tùy ngữ nghĩa (semantics / 의미론) nhưng in-memory trạng thái (state / 상태) mất. Durable tác vụ (task / 작업) phải persist progress/đầu vào (input / 입력) nếu cần khôi phục (recovery / 복구).

# BroadcastReceiver

## 7. Receiver phải làm ít và nhanh

BroadcastReceiver là entry điểm (point / 지점) ngắn. `onReceive()` không phải nơi upload cơ sở dữ liệu (database / 데이터베이스) lớn hoặc sync 5 phút.

Luồng (flow / 흐름) tốt:

```text
broadcast arrives
→ validate/filter
→ persist minimal event/input
→ enqueue WorkManager nếu cần durable work
→ return
```

## 8. `goAsync()` không biến receiver thành dịch vụ (service / 서비스) vô hạn

`goAsync()` cho phép hoàn thành một ít async công việc (work / 작업) sau `onReceive`, nhưng vẫn có thời gian (time / 시간)/thời gian tồn tại (lifetime / 수명) ràng buộc (constraint / 제약조건). Dùng cho thao tác (operation / 연산) ngắn; durable/long công việc (work / 작업) vẫn nên chuyển WorkManager.

## 9. Exported receiver

Receiver exported nhận đầu vào (input / 입력) từ ngoài app phải coi Intent là untrusted. Validate hành động (action / 동작)/extras và dùng permission protection nếu use trường hợp (case / 사례) yêu cầu.

Động (dynamic / 동적) receiver registration cũng cần thời gian tồn tại (lifetime / 수명) unregister đúng và flag exported/not-exported phù hợp API/phiên bản (version / 버전).

# ContentProvider

## 10. Provider là dữ liệu (data / 데이터) IPC ranh giới (boundary / 경계)

ContentProvider expose structured dữ liệu (data / 데이터)/URI giao diện (interface / 인터페이스) giữa tiến trình (process / 프로세스)/app. Android hệ thống (system / 시스템) sử dụng provider concept cho contacts/media/document và app có thể tạo provider riêng.

Nó không chỉ là “cơ sở dữ liệu (database / 데이터베이스) wrapper”. Provider là IPC/bảo mật (security / 보안)/versioning ranh giới (boundary / 경계).

## 11. `ContentResolver`

Máy khách (client / 클라이언트) truy cập provider qua `ContentResolver`:

```kotlin
contentResolver.query(
    uri,
    projection,
    selection,
    selectionArgs,
    sortOrder
)
```

Môi trường vận hành (production / 운영 환경) mã (code / 코드) cần close Cursor/tài nguyên (resource / 자원) bằng `use` và không truy vấn (query / 쿼리) khối lượng lớn trên main luồng thực thi (thread / 스레드).

## 12. URI permission

Provider có thể grant temporary URI permission thay vì expose toàn dữ liệu (data / 데이터) store. Đây là principle of least privilege ở data-sharing tầng (layer / 계층).

## 13. FileProvider

`FileProvider` là ContentProvider đặc biệt để share tệp (file / 파일) private bằng content URI. Nó giúp tránh `file://` exposure và cho grant read/ghi (write / 쓰기) tạm thời.

# Notification

## 14. Notification là hệ thống (system / 시스템) surface, không chỉ UI banner

Notification tồn tại ngoài Activity vòng đời (lifecycle / 생명주기), có thể được người dùng (user / 사용자) tap khi tiến trình (process / 프로세스) chết. Vì vậy `PendingIntent` phải reconstruct điều hướng (navigation / 내비게이션) từ durable/typed identifier.

Không dựa vào singleton bộ nhớ (memory / 메모리) khi handling notification tap.

## 15. Stable notification ID

Nếu cùng logical job/cập nhật (update / 업데이트) cần cập nhật (update / 업데이트) existing notification, dùng stable ID. Random ID mỗi lần tạo spam notification.

Ví dụ download progress:

```text
notificationId = hash(downloadId)
```

## 16. Channel ngữ nghĩa (semantics / 의미론)

Channel nên đại diện category người dùng (user / 사용자) hiểu. Importance/sound sau khi channel tồn tại phần lớn thuộc người dùng (user / 사용자) điều khiển (control / 제어).

Đừng phiên bản (version / 버전) channel theo mỗi bản phát hành (release / 릴리스) để reset preference người dùng (user / 사용자).

## 17. hành động (action / 동작) button

Notification hành động (action / 동작) có thể trigger receiver/dịch vụ (service / 서비스)/activity qua PendingIntent. hành động (action / 동작) handler phải idempotent nếu người dùng (user / 사용자) tap nhiều hoặc PendingIntent được redeliver trong trường hợp biên (edge case / 경계 사례).

# PendingIntent

## 18. PendingIntent là năng lực (capability / 역량) đơn vị từ (token / 토큰)

Khi app tạo PendingIntent, app cho hệ thống (system / 시스템)/other thành phần (component / 컴포넌트) quyền thực hiện một Intent với định danh (identity / 식별자) của app trong phạm vi nhất định.

Vì vậy uniqueness, mutability và payload đều là bảo mật (security / 보안)/tính đúng đắn (correctness / 정확성) concern.

## 19. Immutable mặc định

Nếu use trường hợp (case / 사례) không cần bên ngoài (external / 외부) party fill/thay đổi (change / 변경) Intent, dùng immutable.

Mutable chỉ khi nền tảng (platform / 플랫폼) API thực sự cần mutate, ví dụ một số inline reply/tương tác (interaction / 상호작용) đặc tả hợp đồng (contract / 계약).

## 20. PendingIntent định danh (identity / 식별자)

Hai PendingIntent có thể được hệ thống (system / 시스템) coi là cùng định danh (identity / 식별자) dựa trên Intent fields/yêu cầu (request / 요청) mã (code / 코드); extras không phải lúc nào tham gia equality như nhà phát triển (developer / 개발자) tưởng.

Nếu notification hành động (action / 동작) cho item khác nhau, cần đảm bảo yêu cầu (request / 요청)/dữ liệu (data / 데이터)/hành động (action / 동작) tạo định danh (identity / 식별자) đúng để không reuse nhầm extras.

# App Widget

## 21. Widget không phải mini Activity

App Widget kết xuất (render / 렌더링) qua `RemoteViews` hoặc Glance lớp trừu tượng (abstraction / 추상화) tùy hiện thực (implementation / 구현). Nó chạy dưới ràng buộc (constraint / 제약조건) hệ thống (system / 시스템) surface, cập nhật (update / 업데이트)/vòng đời (lifecycle / 생명주기) khác Compose screen.

Không cố nhúng arbitrary UI lô-gic (logic / 논리) từ screen vào widget.

## 22. Widget trạng thái (state / 상태)

Widget có thể tồn tại lâu hơn tiến trình (process / 프로세스). trạng thái (state / 상태) quan trọng phải đến từ persistent nguồn chuẩn (source of truth / 정본).

Nếu người dùng (user / 사용자) pin nhiều widget instance, mỗi `appWidgetId` có cấu hình (configuration / 구성)/trạng thái (state / 상태) riêng.

## 23. cập nhật (update / 업데이트) frequency

Periodic widget cập nhật (update / 업데이트) quá thường xuyên tốn battery và bị nền tảng (platform / 플랫폼) ràng buộc (constraint / 제약조건). Event-driven cập nhật (update / 업데이트) khi dữ liệu (data / 데이터) đổi thường tốt hơn polling ngắn.

## 24. Widget bộ nhớ (memory / 메모리)

RemoteViews payload có tài nguyên (resource / 자원)/bộ nhớ (memory / 메모리) ràng buộc (constraint / 제약조건). Android 17 tăng enforcement rõ hơn với Bitmap/Icon bộ nhớ (memory / 메모리) trong RemoteViews cho mục tiêu (target / 대상) 37+, vì vậy không gửi bitmap khổng lồ vào widget.

# App Shortcut

## 25. Static và động (dynamic / 동적) shortcut

Shortcut giúp người dùng (user / 사용자) nhảy trực tiếp vào hành động (action / 동작)/destination. Static shortcut phù hợp hành động (action / 동작) cố định; động (dynamic / 동적) shortcut phù hợp thực thể (entity / 엔터티)/hành động (action / 동작) thay đổi theo người dùng (user / 사용자) usage.

Shortcut phải mở được luồng (flow / 흐름) đúng khi tiến trình (process / 프로세스) cold-start.

## 26. Shortcut ID là đặc tả hợp đồng (contract / 계약)

Nếu shortcut đại diện conversation/thứ tự (order / 순서), ID cần ổn định để cập nhật (update / 업데이트)/remove đúng. Không encode secret trực tiếp vào shortcut ID/Intent.

# Quick Settings Tile

## 27. Tile là quick hệ thống (system / 시스템) điều khiển (control / 제어)

Tile phù hợp hành động (action / 동작) trạng thái đơn giản người dùng (user / 사용자) muốn truy cập nhanh, ví dụ toggle VPN-like tính năng (feature / 기능) hoặc start/stop dịch vụ (service / 서비스) hợp lệ.

Tile dịch vụ (service / 서비스) có vòng đời (lifecycle / 생명주기) riêng; đừng assume Activity exists.

## 28. Tile trạng thái (state / 상태) phải phản ánh truth

Nếu tile hiển thị active/inactive nhưng underlying dịch vụ (service / 서비스) thất bại (fail / 실패), UI hệ thống sai. trạng thái (state / 상태) phải derive từ nguồn chuẩn (source of truth / 정본) và cập nhật (update / 업데이트) khi actual status đổi.

# Deep link và bên ngoài (external / 외부) điều hướng (navigation / 내비게이션)

## 29. Entry từ hệ thống (system / 시스템) phải reconstruct đồ thị (graph / 그래프)

Notification, widget, shortcut, app link đều có thể mở app từ cold tiến trình (process / 프로세스). điều hướng (navigation / 내비게이션) mã (code / 코드) nên xử lý theo typed destination + lĩnh vực (domain / 도메인) identifier.

Ví dụ:

```text
notification(orderId=42)
→ launch app
→ session check
→ load order 42
→ authorization check
→ navigate detail
```

Không serialize whole `Order` đối tượng (object / 객체) vào PendingIntent.

# Multi-process awareness

## 30. `android:process`

Một số thành phần (component / 컴포넌트)/thư viện (library / 라이브러리) có thể chạy tiến trình (process / 프로세스) riêng. Khi đó singleton, DI đồ thị (graph / 그래프), static bộ nhớ đệm (cache / 캐시) và bộ nhớ (memory / 메모리) trạng thái (state / 상태) tách biệt.

Đa số app không cần custom multi-process. Chỉ dùng khi nền tảng (platform / 플랫폼)/thư viện (library / 라이브러리) yêu cầu (requirement / 요구사항) rõ vì độ phức tạp (complexity / 복잡도) tăng mạnh: IPC, initialization, dữ liệu (data / 데이터) consistency, logging và crash hành vi (behavior / 동작).

# WorkManager và hệ thống (system / 시스템) components

## 31. Receiver/dịch vụ (service / 서비스) không thay WorkManager

WorkManager quản durable deferrable công việc (work / 작업) với các ràng buộc (constraints / 제약조건들)/thử lại (retry / 재시도)/persistence. Receiver là sự kiện (event / 이벤트) entry, dịch vụ (service / 서비스) là thành phần (component / 컴포넌트) thời gian tồn tại (lifetime / 수명), foreground dịch vụ (service / 서비스) là user-visible long công việc (work / 작업).

Một kiến trúc (architecture / 아키텍처) tốt thường phối hợp:

```text
BroadcastReceiver
→ enqueue unique WorkManager work
→ repository transaction
→ database source of truth
→ notification update nếu cần
```

## 32. Unique công việc (work / 작업)

Nếu cùng sync sự kiện (event / 이벤트) tới nhiều lần, unique công việc (work / 작업) chính sách (policy / 정책) giúp deduplicate/coalesce theo nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

Nhưng đừng dùng unique công việc (work / 작업) để che underlying idempotency bug; máy chủ (server / 서버)/cục bộ (local / 로컬) mutation vẫn nên idempotent khi cần.

# Tiến trình (process / 프로세스) initialization

## 33. ContentProvider có thể khởi tạo rất sớm

Một số thư viện (library / 라이브러리) dùng provider-based initializer để chạy trước `Application.onCreate()`. Điều này tiện nhưng có startup chi phí (cost / 비용).

Khi kiểm tra (audit / 감사) cold start, nhớ initialization có thể đến từ manifest/provider chứ không chỉ mã (code / 코드) bạn thấy trong ứng dụng (application / 애플리케이션).

## 34. App Startup

Jetpack App Startup cung cấp cách quản initializer/phụ thuộc (dependency / 의존성) rõ hơn cho thư viện (library / 라이브러리)/app initialization, nhưng vẫn cần lazy/defer khi initialization không cần trước first frame.

# Bảo mật (security / 보안)

## 35. thành phần (component / 컴포넌트) attack surface

Rà soát (review / 검토) manifest:

```text
exported Activity
exported Service
exported Receiver
exported Provider
intent-filter
permission protection
URI grant
```

Mỗi exported thành phần (component / 컴포넌트) là API surface của app.

## 36. tường minh (explicit / 명시적) Intent cho nội bộ (internal / 내부) lời gọi (call / 호출)

Nếu mục tiêu (target / 대상) thành phần (component / 컴포넌트) nội bộ đã biết, tường minh (explicit / 명시적) Intent giảm ambiguity/hijacking so với implicit Intent không cần thiết.

## 37. Signature permission

Trong ecosystem nhiều app cùng tổ chức và signing điều khiển (control / 제어), signature-level permission có thể protect IPC giữa app. Nhưng certificate rotation/phân phối (distribution / 분포) kiến trúc (architecture / 아키텍처) cần tính trước.

# Testing hệ thống (system / 시스템) surfaces

## 38. Cold-start kiểm thử (test / 테스트)

Mỗi entry điểm (point / 지점) quan trọng nên kiểm thử (test / 테스트) khi tiến trình (process / 프로세스) chưa tồn tại:

```text
kill process
→ tap notification
→ expected screen/data
```

Tương tự widget/shortcut/deep link.

## 39. Duplicate delivery

Kiểm thử (test / 테스트) notification hành động (action / 동작)/broadcast/công việc (work / 작업) sự kiện (event / 이벤트) lặp. nghiệp vụ (business / 비즈니스) mutation không được double-charge/double-submit.

## 40. Permission/export bảo mật (security / 보안) kiểm thử (test / 테스트)

Thử gửi malformed Intent từ adb/kiểm thử (test / 테스트) app tới exported thành phần (component / 컴포넌트). Validate app không crash và không thực hiện privileged hành động (action / 동작) trái phép.

# Cấp cao (senior / 시니어) Notes

## 41. hệ thống (system / 시스템) surface là công khai (public / 공개) đặc tả hợp đồng (contract / 계약)

Notification hành động (action / 동작), shortcut, deep link, provider URI hoặc exported receiver đều có thể sống qua nhiều app phiên bản (version / 버전). Thay đặc tả hợp đồng (contract / 계약) cần di chuyển (migration / 마이그레이션)/versioning mindset.

## 42. Entry điểm (point / 지점) mỏng

Thành phần (component / 컴포넌트) callback nên chủ yếu parse/validate → delegate. lô-gic nghiệp vụ (business logic / 비즈니스 로직) ở repository/use trường hợp (case / 사례) giúp reuse và kiểm thử (test / 테스트).

## 43. Reconstruct thay vì vận chuyển (transport / 전송) giant trạng thái (state / 상태)

Hệ thống (system / 시스템) surface nên truyền stable ID/intention, sau đó app reconstruct trạng thái (state / 상태) từ nguồn chuẩn (source of truth / 정본). Đây là mẫu (pattern / 패턴) chung nối điều hướng (navigation / 내비게이션), Binder limit, tiến trình (process / 프로세스) death và bảo mật (security / 보안).

## 44. Không dùng thành phần (component / 컴포넌트) để chống tiến trình (process / 프로세스) death

Dịch vụ (service / 서비스)/widget/provider không phải mẹo để giữ app sống. Android kiến trúc (architecture / 아키텍처) tốt giả định tiến trình (process / 프로세스) có thể mất và trạng thái (state / 상태) có thể reconstruct.

# Checklist kết thúc chapter

Bạn nên giải thích được vì sao dịch vụ (service / 서비스) không phải background luồng thực thi (thread / 스레드); Receiver vì sao phải ngắn; ContentProvider là IPC/dữ liệu (data / 데이터) ranh giới bảo mật (security boundary / 보안 경계); notification tap phải hoạt động từ cold tiến trình (process / 프로세스); PendingIntent vì sao là năng lực (capability / 역량) đơn vị từ (token / 토큰); widget/shortcut/tile có vòng đời (lifecycle / 생명주기) khác Activity; WorkManager khác dịch vụ (service / 서비스)/Receiver; multi-process làm singleton sai thế nào; và vì sao exported thành phần (component / 컴포넌트) cần được rà soát (review / 검토) như một API công khai (public API / 공개 API)/bảo mật (security / 보안) surface.

> **Bàn giao:** Sau **44. Không dùng thành phần (component / 컴포넌트) để chống tiến trình (process / 프로세스) death**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
