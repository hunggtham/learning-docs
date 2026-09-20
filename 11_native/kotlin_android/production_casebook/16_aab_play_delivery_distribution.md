# Case 16 — Android App Bundle, Split APK, Play Delivery và Distribution Engineering

Một Android app production không kết thúc ở bước `assembleRelease`. Artifact phải được đóng gói, ký, upload, phân phối theo device configuration, có khả năng rollout dần, rollback hoặc disable feature, và vẫn hoạt động khi code/resources được chia thành nhiều split. Đây là lớp thường bị tutorial bỏ qua vì sample app chỉ cài trực tiếp một APK từ Android Studio.

Chapter này tập trung vào mental model của **artifact và delivery**: APK khác AAB thế nào, split được tạo ra sao, dynamic feature module dùng khi nào, Play App Signing ảnh hưởng key ownership thế nào, và tại sao delivery architecture phải được nghĩ cùng modularization/build/release.

## 1. APK là installable artifact, AAB là publishing artifact

**APK** chứa code/resources/native libraries đủ để Android package manager cài một package cụ thể lên device.

**Android App Bundle — AAB** là publishing format. Khi upload AAB lên Google Play, Play dùng thông tin trong bundle để generate APK set tối ưu theo device configuration. Người dùng thường không tải toàn bộ mọi density/language/ABI nếu không cần.

Mental model:

```text
source
→ Gradle/AGP
→ app-release.aab
→ Play processing/signing
→ device-specific APK splits
→ install session trên device
```

Vì vậy test một universal/local APK không hoàn toàn giống test artifact do Play generate từ AAB. Release process nên có bước test bundle-derived APKs bằng `bundletool` hoặc track testing phù hợp.

## 2. Tại sao split APK tồn tại

Một app có thể chứa nhiều loại resource theo configuration: density, ABI, language và feature. Nếu ship tất cả trong một APK monolithic, device nhận nhiều byte không bao giờ dùng.

Play có thể chia thành:

- **base APK** chứa phần bắt buộc;
- configuration splits cho ABI/density/language;
- feature splits cho dynamic feature module;
- asset packs trong mô hình phù hợp.

Package manager nhìn cả tập split như một app logical package. Code không nên giả định “mọi resource/code đều nằm trong một physical APK file”.

## 3. `bundletool` là cách quan sát AAB thay vì coi Play như black box

`bundletool` là tool nền tảng dùng để thao tác App Bundle. Một workflow học và debug hữu ích:

```text
AAB
→ bundletool build-apks
→ .apks archive
→ inspect split set
→ install-apks lên device/emulator
```

Điều này giúp reproduce issue như missing ABI, dynamic feature không được đóng gói, resource split khác expectation hoặc universal APK khác device-specific install.

Release engineer nên biết inspect artifact thực tế thay vì chỉ nhìn Gradle configuration.

## 4. App size là product metric, không chỉ build metric

AAB giúp Play tối ưu download, nhưng không miễn trừ developer khỏi size discipline. Những nguồn tăng size thường gặp:

- image/audio/video asset lớn;
- nhiều native ABI;
- duplicate dependency/resources;
- model ML lớn;
- debug metadata vô tình ship;
- feature hiếm dùng nằm trong base module;
- R8/resource shrinking chưa hoạt động đúng;
- embedded web/assets không kiểm soát.

APK Analyzer và bundle reports giúp phân tích contribution theo DEX/resource/native library.

Senior rule: đo **download size và installed size theo cohort/device**, không chỉ file `.aab` size. AAB upload size không bằng bytes user tải.

## 5. Dynamic Feature Module giải quyết delivery, không phải mặc định modularization

Một project có thể có nhiều Gradle library modules mà tất cả vẫn được install-time trong base app. **Dynamic feature module** là module tham gia Play Feature Delivery và có delivery semantics riêng.

```kotlin
plugins {
    id("com.android.dynamic-feature")
    kotlin("android")
}

dependencies {
    implementation(project(":app"))
}
```

Base app khai báo dynamic feature modules tương ứng. Feature module phụ thuộc base; base biết danh sách feature để bundle packaging.

Không chuyển mọi feature thành dynamic chỉ để “modular hiện đại”. Dynamic delivery thêm state, install failure, navigation condition, offline behavior, testing và Play dependency.

## 6. Install-time, on-demand và conditional delivery

**Install-time**: feature có ngay khi app được cài. Đây là behavior đơn giản nhất.

**On-demand**: feature được tải khi user cần. Phù hợp feature lớn nhưng ít người dùng, ví dụ editor nâng cao hoặc region-specific workflow.

**Conditional delivery**: feature chỉ install nếu device/user thỏa điều kiện như locale, device feature hoặc API level.

Một feature on-demand tạo thêm state machine:

```text
NotInstalled
→ Requesting
→ Downloading(progress)
→ Installed
→ Ready

hoặc

→ Failed(retryable/non-retryable)
```

UI/navigation phải xử lý install pending/fail; không được `Class.forName()` hoặc navigate thẳng vào code chưa có trên device.

## 7. Base module phải giữ contract tối thiểu ổn định

Dynamic feature phụ thuộc base, nên contract giữa base và feature cần nhỏ và ổn định. Nếu feature trực tiếp chạm mọi implementation nội bộ của base, modularization chỉ tồn tại trên filesystem.

Có thể dùng interface/API module hoặc navigation contract để giảm coupling. Tuy nhiên đừng tạo abstraction chỉ để chiều dependency graph đẹp; abstraction phải đại diện contract thật sự.

## 8. Resource và navigation khi feature chưa được cài

Code/resource của dynamic module không đảm bảo tồn tại trước install. Base UI phải có fallback và loading state.

Deep link vào feature on-demand là case quan trọng: app có thể được mở từ URL/notification trong trạng thái feature chưa cài. Router cần resolve intent → xác định feature → install → validate destination → navigate.

Process có thể chết giữa download/install. Vì vậy không giữ critical state chỉ trong memory.

## 9. Play Asset Delivery và large assets

Một số app/game có asset lớn hơn nhiều so với app code. Asset delivery tách concern “binary feature code” và “large data asset”. Delivery mode có thể khác nhau tùy use case.

Không nên dùng dynamic feature chỉ để chở file dữ liệu lớn nếu platform có delivery primitive phù hợp hơn. Ngược lại, backend download riêng cũng có trade-off auth/CDN/cache/versioning mà Play-managed delivery có thể giải quyết một phần.

Chọn cơ chế dựa vào ownership, size, update cadence, offline requirement và store dependency.

## 10. ABI splits và native library consequence

Nếu app có `.so`, AAB có thể cho Play ship ABI phù hợp device. Điều này giảm download nhưng đòi hỏi native dependency phải có ABI matrix đúng.

Ví dụ project có `arm64-v8a` và `x86_64` nhưng một third-party `.so` chỉ có ARM. Emulator x86_64 có thể fail load library dù phone thật chạy tốt.

Native artifact validation phải kiểm tra ABI availability, symbol, page-size alignment và packaging cho đúng release bundle.

## 11. Language split và runtime locale

Play có thể tối ưu language resources. Nếu app có dynamic language behavior, per-app language hoặc tải locale sau install, cần hiểu resource availability/delivery model.

Không nên giả định tất cả translations luôn được cài nếu bundle configuration tách language splits. Nếu product cần mọi locale offline ngay từ đầu, configuration delivery phải phản ánh requirement đó.

## 12. Play App Signing: app signing key và upload key

Trong Play App Signing, Google Play quản lý **app signing key** dùng để ký APK tới user. Developer thường dùng **upload key** để authenticate artifact upload.

Hai key có vai trò khác nhau. Mất upload key có recovery path khác với mất control app signing identity trong mô hình tự quản lý.

Team phải document:

- ai sở hữu upload credential;
- CI ký/upload thế nào;
- rotation/recovery procedure;
- package identity nào dùng key nào;
- debug/internal distribution không được nhầm production key.

## 13. Signing lineage và update compatibility

Android update một package dựa package identity/signing relationship và version rules. Release artifact ký sai có thể không upgrade được app đang cài.

Test release không chỉ `fresh install`; phải test **upgrade từ version production đang phổ biến**. Đặc biệt khi thay signing setup, split model, native library hoặc database schema.

## 14. `versionCode` và `versionName`

`versionName` là user-facing semantic label, ví dụ `3.4.0`. `versionCode` là monotonically increasing integer Android/Play dùng để so version artifact.

Không derive critical migration logic từ `versionName` string nếu system đã có schema/API-specific version riêng. App version, DB schema version và backend API version là những axes khác nhau.

CI nên tạo version metadata reproducibly và trace về commit/release tag.

## 15. Internal, closed, open và production tracks là deployment environments

Store track không chỉ để “QA tải app”. Nó là deployment control plane. Tùy organization, có thể dùng:

```text
internal
→ closed/beta
→ staged production rollout
→ wider rollout
```

Mỗi bước cần clear promotion criteria. Artifact được promote nên là cùng artifact đã test, tránh rebuild binary khác ở mỗi environment nếu không cần.

Nếu environment backend khác nhau, cân nhắc build variant/configuration strategy cẩn thận. “Promote same artifact” và “different endpoint per environment” đôi khi xung đột; giải pháp phải phù hợp threat model và release process.

## 16. Staged rollout không thay feature flag

Staged rollout kiểm soát tỷ lệ user nhận **app binary version**. Feature flag kiểm soát behavior **bên trong binary** theo runtime policy.

Nếu crash do binary initialization trước khi remote config load, feature flag có thể không cứu được. Nếu bug chỉ nằm feature mới, flag có thể disable nhanh hơn store rollback.

Một release resilient thường dùng cả hai ở các layer khác nhau.

## 17. Rollback trên mobile khó hơn server rollback

Không thể giả định user sẽ downgrade APK ngay. Nhiều user giữ version lỗi offline trong nhiều ngày. Vì vậy “rollback” mobile thường là:

- stop rollout;
- ship hotfix với versionCode cao hơn;
- disable remote feature;
- backend giữ backward compatibility;
- DB/file format phải chịu được version skew.

Migration destructive hoặc backend contract one-way khiến rollback gần như không thể.

## 18. In-app update không phải default solution cho mọi app

In-app update APIs có thể giúp prompt/update flow trong use case phù hợp, nhưng product không nên cưỡng ép update chỉ vì developer muốn giảm support matrix.

Server protocol nên có compatibility window. Nếu bắt buộc minimum version vì security/data integrity, UI phải giải thích rõ và backend policy phải có operational plan.

Update flow bản thân cũng là failure-prone state: Play availability, download, restart, user cancel, network fail.

## 19. Review, integrity và Play-specific services là optional infrastructure

In-app review, Play Integrity, update API và delivery libraries cung cấp capability hữu ích nhưng tăng coupling với Google Play environment. Core business architecture không nên giả định mọi installation channel đều có Play services nếu product có sideload/enterprise/other-store requirement.

Bọc Play-specific integration sau boundary rõ ràng nếu app phải hỗ trợ nhiều distribution channel.

## 20. Distribution channel là security boundary

Release binary có thể đi qua Play, enterprise MDM, direct APK hoặc internal distribution. Mỗi channel khác signing/update/trust model.

Security logic không được chỉ hỏi “app được cài từ Play nên trusted”. Client vẫn nằm trên user-controlled device. Integrity signal là một input risk signal, không thay backend authorization.

## 21. Offline và dynamic delivery

On-demand feature yêu cầu network để tải lần đầu, vì vậy feature business-critical offline không nên phụ thuộc dynamic install chưa có.

Nếu user chuẩn bị đi offline, product có thể prefetch feature/asset khi online. Nhưng phải xử lý storage pressure và module uninstall behavior.

Architecture nên phân biệt:

- feature capability tồn tại trong product;
- binary module đã installed trên device;
- user có entitlement;
- backend feature enabled;
- permission/hardware available.

Năm trạng thái này không đồng nghĩa.

## 22. Test AAB/delivery đúng cách

Release test matrix nên có ít nhất:

1. build AAB production-like;
2. generate/install APK set theo representative device specs;
3. fresh install;
4. upgrade từ prior production artifact;
5. language/density/ABI representative;
6. dynamic feature install/uninstall/failure nếu dùng;
7. offline launch sau install;
8. process death trong delivery flow;
9. minified/R8 release behavior;
10. verify signing/package/version metadata.

Cài `debug.apk` từ IDE không cover phần lớn risk này.

## 23. App Bundle và native 16 KB page size

Khi app chứa native `.so`, distribution correctness còn phụ thuộc binary compatibility với page-size requirements trên Android mới. NDK mới hỗ trợ alignment phù hợp tốt hơn, nhưng **mọi prebuilt native library** cũng phải compatible.

Đây là ví dụ điển hình cho việc AAB “build thành công” chưa đủ; artifact cần được validate trên device/platform target thực tế.

Case 17 sẽ đi sâu JNI/ABI/native memory và 16 KB page-size engineering.

## 24. Dynamic feature failure modes

Các lỗi thường gặp:

### Feature code được reference trực tiếp trước install

Base code có compile-time/runtime dependency không đúng boundary. Cần route qua install state/contract.

### Deep link vào module chưa có

Router phải defer navigation và preserve intent sau install.

### R8 removes reflection entry point

Dynamic delivery + reflection cần keep rule/test release artifact.

### User offline lần đầu mở feature

UI cần graceful state, không spinner vô hạn.

### Module version mismatch

Feature/base trong một installed app bundle phải cùng release set; đừng tự thiết kế hot-swap code ngoài supported platform model.

## 25. Senior decision framework: có nên dùng dynamic delivery?

Hỏi lần lượt:

- feature size có đáng kể không;
- tỷ lệ user dùng feature thấp hay cao;
- feature có cần offline ngay không;
- install latency có chấp nhận được không;
- deep link/cold start có cần feature này không;
- team có khả năng test delivery states không;
- distribution channel có phải Google Play không;
- module boundary có thật sự rõ không.

Nếu hầu hết user cần feature và size nhỏ, install-time đơn giản thường tốt hơn.

## 26. Artifact provenance và release evidence

Mỗi production release nên có thể truy ngược:

```text
release version
→ AAB checksum
→ source commit/tag
→ dependency lock/SBOM
→ toolchain
→ signing/upload identity
→ mapping/native symbols
→ CI run
→ rollout timeline
```

Crash symbolication và R8 deobfuscation cần mapping file đúng version. Native crash cần symbols tương ứng binary. Nếu artifact metadata bị mất, incident response khó hơn nhiều.

## 27. Official references

- Android App Bundle: https://developer.android.com/guide/app-bundle
- Play Feature Delivery: https://developer.android.com/guide/playcore/feature-delivery
- Reduce app size: https://developer.android.com/topic/performance/reduce-apk-size
- `bundletool`: https://developer.android.com/tools/bundletool
- Target API requirements: https://developer.android.com/google/play/requirements/target-sdk

Store policy và delivery API thay đổi theo thời gian. Khi release thật, luôn kiểm tra documentation/policy mới nhất thay vì dùng snapshot trong note như source duy nhất.