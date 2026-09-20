# Kotlin + Android Master — Engineering & Governance Deep Dive

> File này bổ sung cho [`../04_kotlin_master.md`](../04_kotlin_master.md). Mục tiêu là hoàn thiện lớp kiến thức production engineering mà một codebase Android sống nhiều năm cần có: build engineering, dependency/supply-chain governance, ABI, migration, observability, performance budget, security/integrity, privacy, accessibility/adaptive UI, ADR/ownership, quality gate và Kotlin Multiplatform strategy.

# 1. Build engineering là một phần của architecture

Ở codebase lớn, build system ảnh hưởng trực tiếp developer productivity, CI cost và khả năng nâng version. Gradle có configuration phase và execution phase. **Configuration cache** giảm việc cấu hình lại task graph khi input phù hợp; **build cache** tái sử dụng output task nếu input fingerprint giống nhau. Custom task/plugin không tương thích cache có thể làm mất lợi ích toàn repo.

Convention plugin trong `build-logic` giúp gom cấu hình Android/Kotlin/Compose chung mà không copy hàng trăm dòng giữa module. Tuy nhiên convention plugin cũng là code production của toolchain: nó cần test, version awareness và API nhỏ.

# 2. Version Catalog, BOM và dependency constraint

Version Catalog giúp đặt alias/version dependency tập trung trong `libs.versions.toml`, nhưng nó không tự giải quyết compatibility. BOM/platform giúp một họ thư viện dùng tập version đã được kiểm tra cùng nhau. Dependency constraint giới hạn version có thể resolve.

Tại snapshot 2026-09-20, Compose stable BOM là `2026.09.00`. BOM giúp align Compose library versions, nhưng không có nghĩa “thêm BOM là tự có mọi Compose dependency”; từng artifact vẫn phải khai báo riêng.

# 3. Build reproducibility và dependency locking

Build production nên biết chính xác dependency graph nào đã tạo artifact. Dynamic version như `1.+` hay “latest.release” làm cùng một commit có thể build ra binary khác nhau ở hai thời điểm, gây khó reproduce incident.

Dependency locking hoặc dependency verification tăng khả năng reproducibility/supply-chain control. Reproducible build không có nghĩa byte-for-byte luôn giống trong mọi toolchain nếu ecosystem chưa bảo đảm; mục tiêu thực tế là input/version/build configuration được kiểm soát và audit được.

# 4. Supply-chain security và dependency lifecycle

Ứng dụng mobile mang theo nhiều transitive dependency. Mỗi dependency là code chạy trong process, có thể thêm permission, native library, network behavior hoặc vulnerability. Governance tốt không phải cấm library; nó yêu cầu biết owner, lý do dùng, maintenance status và plan nâng version.

Khi chọn dependency mới, ngoài API convenience còn phải nhìn license, release cadence, bus factor, security history, binary size, minSdk/compileSdk requirement, KMP/Java compatibility và migration cost nếu library bị bỏ.

# 5. SBOM

**SBOM (Software Bill of Materials)** là inventory machine-readable về component/version trong artifact. Tổ chức có compliance/security requirement có thể dùng SBOM cùng vulnerability scanning để biết một CVE ảnh hưởng artifact nào.

Scanner chỉ là signal. Một CVE có thể không reachable trong app của bạn hoặc chỉ ảnh hưởng environment khác; ngược lại một dependency không có CVE công khai vẫn có behavior/privacy risk. Vì vậy dependency security cần triage, không phải auto-upgrade mù quáng.

# 6. Kotlin public API và module boundary

Ở app multi-module, `public` tạo coupling. API surface càng lớn, thay đổi càng lan rộng và incremental build càng tệ. Ưu tiên expose contract/model nhỏ, giữ implementation `internal` khi có thể.

Nhưng không tạo interface chỉ để giảm public class count. Interface có giá trị khi boundary phản ánh ownership, volatility, platform abstraction hoặc test seam thực sự.

Một feature module tốt không cần export mọi ViewModel, DTO, DAO và mapper. Phần lớn implementation nên ở bên trong; module khác chỉ thấy contract cần thiết.

# 7. Source, binary và behavioral compatibility

Một thay đổi có thể source-compatible nhưng binary-incompatible, hoặc compile được nhưng behavior thay đổi. Public library phải phân biệt ba lớp này.

Đổi JVM name, generic signature, visibility, inheritance hierarchy, inline public function, default argument hoặc generated API có thể ảnh hưởng caller theo cách khác nhau. Với library publish cho nhiều app, API dump/binary compatibility validation nên trở thành CI gate.

Behavioral compatibility thường còn quan trọng hơn. Repository method giữ nguyên signature nhưng đổi từ cache-first sang network-only có thể phá UX dù compiler không báo lỗi.

# 8. Toolchain migration là một compatibility graph

JDK ↔ Gradle ↔ AGP ↔ Kotlin ↔ KSP/compiler plugin ↔ Compose ↔ compileSdk/targetSdk tạo compatibility graph. Một migration an toàn chia thành lát nhỏ và giữ build xanh sau mỗi lát.

Một workflow thực dụng là nâng wrapper/toolchain trước, giải warning/deprecation, nâng processor/library, test performance, sau đó nâng target SDK và xử lý behavior change. Nếu thay mọi thứ cùng lúc, root cause analysis trở nên đắt.

Snapshot hiện tại của bộ note là Kotlin 2.4.20, Android Studio Quail 4 / 2026.1.4 Patch 1 và AGP 9.4.1. Android 17 là API 37. Google Play từ 2026-08-31 yêu cầu app/update Android thông thường target API 36 trở lên; đây là minimum Play requirement chứ không phải latest platform API.

# 9. Target SDK migration khác library upgrade

Nâng `compileSdk` chủ yếu cho compiler biết API mới. Nâng `targetSdk` có thể bật behavior change platform. Vì vậy target SDK upgrade cần test behavior chứ không chỉ build thành công.

Mỗi Android release có hai nhóm thay đổi: thay đổi áp dụng cho mọi app chạy trên OS mới và thay đổi chỉ áp dụng khi app target API mới. Migration plan phải đọc cả hai nhóm.

# 10. Observability: crash chỉ là một phần

Observability mobile phải trả lời được user/session nào bị gì, ở app version/device/API nào, trước đó event nào xảy ra và backend request tương ứng là gì. Crash report chỉ là một phần. ANR, startup, jank, network failure, sync backlog và feature success rate cũng có thể cần telemetry.

Structured log nên có event name và field ổn định thay vì concat string tùy ý. Correlation/request ID giúp nối mobile log với backend trace nếu privacy policy cho phép.

Không ghi token, password, raw PII hoặc document nhạy cảm chỉ để debug dễ hơn.

# 11. Telemetry schema cũng là API

Analytics/observability event cần owner và schema ổn định. Nếu mỗi developer tự đổi tên event/property, dashboard và alert nhanh chóng mất độ tin cậy.

Sampling cần thiết vì gửi mọi event tốn pin/data và tạo chi phí. Event high-volume như frame metric có thể cần sampling mạnh; security/audit event có policy khác.

# 12. Performance budget

Performance production nên có budget: cold-start percentile, frame/jank threshold, memory peak, binary size, battery/network budget. Không có budget, “performance tốt” trở thành cảm giác.

Budget phải gắn với device class và percentile. Một app trung bình 10 ms/frame nhưng thỉnh thoảng spike 150 ms vẫn cho cảm giác giật.

# 13. Macrobenchmark, Baseline Profile và Perfetto

Macrobenchmark đo journey như startup/scroll/interaction ở app level. Baseline Profile ghi lại code path quan trọng để ART compile tối ưu sớm hơn. Perfetto giúp nhìn scheduling, binder, I/O, frame timeline và system event.

Performance workflow đúng là hypothesis → measurement → change → measurement lại. Không bắt đầu bằng “thêm `remember`”, “đổi List sang Sequence” hoặc “bật profile” nếu chưa biết bottleneck.

# 14. Regression governance

Benchmark CI cần kiểm soát device/thermal state để giảm noise. So một lần chạy duy nhất không đủ. Có thể dùng threshold/baseline theo percentile hoặc rolling median tùy pipeline.

Không phải mọi PR đều cần full macrobenchmark; affected-path hoặc nightly benchmark có thể hợp lý hơn. Nhưng release cần có performance signal đủ để phát hiện regression lớn.

# 15. Authentication, authorization và integrity

Authentication trả lời “ai”; authorization trả lời “được phép làm gì”; app/device integrity chỉ là thêm signal. Play Integrity hoặc attestation có thể giúp backend đánh giá risk, nhưng không nên dùng như bằng chứng tuyệt đối rằng client không bị sửa.

Authorization phải thực thi phía server. Client-side role check chỉ phục vụ UX. APK nằm trên thiết bị người dùng nên phải coi là môi trường không đáng tin.

# 16. Android Keystore và BiometricPrompt

Android Keystore giúp tạo/lưu key mà app không cần đọc raw key material trực tiếp trong nhiều cấu hình. Hardware-backed key nếu thiết bị hỗ trợ tăng protection nhưng vẫn phải có threat model và fallback phù hợp.

`BiometricPrompt` có thể gate user authentication cho operation nhạy cảm. Nhưng biometric UI không tự biến request backend thành authorized request. Server vẫn cần token/authorization contract riêng.

# 17. Network Security Config

Network Security Config cho phép định nghĩa cleartext policy, trust anchor và debug override có kiểm soát. Đây là cách tốt hơn tự viết trust manager tùy tiện.

Debug CA chỉ nên tồn tại trong debug-specific config. Không đưa “trust all certificate” vào production để xử lý certificate issue.

# 18. WebView là browser nhúng

WebView cần xem như security boundary. JavaScript interface, file access, navigation và origin cần được giới hạn. Không load content không tin cậy cùng native capability mạnh mà không review threat model.

Nếu dùng `addJavascriptInterface`, chỉ expose API tối thiểu và hiểu version/security implication. Deep link từ web vào native cũng phải validate input như external input.

# 19. Privacy engineering

Privacy không phải form cuối dự án. Data inventory phải biết dữ liệu nào thu thập, mục đích, nơi lưu, thời gian giữ, có gửi third party hay không và user có thể xóa/export thế nào.

Những câu trả lời này ảnh hưởng schema, logging, analytics, backup và API. Thêm một SDK analytics có thể đổi privacy inventory dù feature business không thay đổi.

# 20. Backup và device transfer

Dữ liệu có thể được restore trên thiết bị khác nếu backup config cho phép. Vì vậy assumption “file này chỉ tồn tại trên thiết bị gốc” có thể sai.

Token, key, encrypted database và credential-derived data cần backup policy rõ. Nếu key không restore nhưng ciphertext có restore, app phải xử lý recovery thay vì rơi vào trạng thái dữ liệu không đọc được.

# 21. Google Play Data Safety và permission governance

Data Safety/permission declaration phải phản ánh behavior thật của app và SDK. Một SDK có thể thu device identifier/network data mà product team không nhận ra nếu chỉ nhìn code feature.

Permission nên theo least privilege. Nếu system picker có thể cung cấp capability cần thiết, đôi khi tốt hơn xin quyền rộng như toàn bộ photo/contact storage.

# 22. Accessibility là requirement kiến trúc UI

Accessibility không nên là checklist sau cùng. Compose semantics, content description, role, state description, focus order, touch target và contrast ảnh hưởng TalkBack, switch access và test automation.

UI phải hoạt động khi font scale lớn. Nếu layout chỉ đúng ở 1.0x font, architecture/layout constraint đang quá cứng.

# 23. Adaptive UI và large screen

Adaptive UI không đồng nghĩa tạo layout riêng cho từng tablet. Thiết kế theo available space/window size và posture giúp phone, tablet, foldable và desktop-windowed mode dùng cùng information architecture nhưng phân bố pane khác nhau.

State/navigation model phải không phụ thuộc giả định “mỗi lúc chỉ có một screen full-width”. Hai-pane UI có thể cần selection state tách khỏi navigation destination.

# 24. Android 17 và large-screen adaptivity

Android 17 tiếp tục đẩy mạnh adaptive behavior. Với app target API 37 trên large screen, một số khả năng opt-out orientation/resizing trước đây bị hạn chế hơn. Điều cần học không phải thuộc một flag, mà là thiết kế UI không phụ thuộc orientation lock và kích thước cố định.

Mỗi target SDK upgrade phải review behavior change vì platform contract có thể thay đổi mà source code không đổi.

# 25. Architecture Decision Record

Ở scale tổ chức, kiến trúc thất bại nhiều khi do decision không có context chứ không do pattern sai. **ADR (Architecture Decision Record)** ghi problem, constraint, decision, alternative và consequence.

Ví dụ quyết định “Room là local source of truth” nên ghi lý do offline requirement, data volume, sync semantics và alternative đã loại. Người sau sẽ biết khi nào decision còn hợp lệ thay vì giữ pattern như giáo điều.

# 26. Ownership

Mỗi core module/platform capability cần owner. Shared code “mọi người đều sở hữu” thường thực tế là không ai sở hữu. Ownership rõ làm dependency upgrade, incident response và deprecation có nơi chịu trách nhiệm.

Ownership không có nghĩa một người duy nhất được sửa. Nó nghĩa có nhóm chịu trách nhiệm về roadmap, quality và compatibility.

# 27. Quality gate từ local đến release

Một pipeline mature có tầng feedback tăng dần: formatter/compiler → unit test/static analysis → module integration → instrumented/UI test → benchmark/security scan → release validation.

Không phải mọi PR chạy toàn bộ suite đắt tiền. Có thể shard, affected-module selection hoặc nightly pipeline. Nhưng artifact release phải đi qua gate phù hợp risk.

# 28. Flaky test là defect của test system

Flaky test không phải “chuyện bình thường của CI”. Quarantine có thể cần tạm thời để unblock pipeline, nhưng phải có owner/root-cause.

Nếu team quen bấm rerun đến xanh, CI mất vai trò signal và incident production sẽ khó phân biệt regression thật khỏi noise.

# 29. Kotlin Multiplatform: chia sẻ đúng thứ cần chia sẻ

KMP có giá trị khi business logic, data model, networking hoặc persistence abstraction thật sự chung giữa platform. Không nên ép UI/platform API khác biệt vào abstraction quá chung chỉ để tăng phần trăm shared code.

Metric tốt hơn là giảm duplicated business invariant và maintenance cost.

# 30. `expect/actual` và platform boundary

`expect/actual` hữu ích cho platform capability nhỏ nhưng lạm dụng sẽ tạo abstraction khó hiểu. Boundary cần rõ về dispatcher/threading, serialization, date/time, file/network API và error model.

Shared module nên có test riêng, public API nhỏ và release/version discipline giống mọi library khác.

# 31. Operating model cho codebase sống nhiều năm

Một hệ thống bền không chỉ có architecture diagram. Nó cần dependency update cadence, deprecation budget, database migration test, target SDK plan, performance baseline, crash/ANR SLO, security patch process và cleanup policy cho feature flag/legacy path.

Nếu project chỉ nâng version khi Play Console bắt buộc, migration debt sẽ tích tụ thành big-bang upgrade. Cadence nhỏ và thường xuyên rẻ hơn nhiều so với vài năm một lần.

# 32. Feature flag lifecycle

Feature flag hỗ trợ staged rollout/rollback nhưng cũng tạo state space. Mỗi flag nên có owner, default, telemetry, expiration date và cleanup ticket.

Flag không được cleanup sẽ khiến code path cũ/mới cùng tồn tại, test matrix tăng và developer sau không biết path nào còn được dùng.

# 33. Release artifact traceability

Mỗi artifact production nên trace được về commit, build config, dependency graph, signing identity, mapping file và feature/config state. Khi crash xảy ra, phải biết binary nào thật sự đang chạy chứ không chỉ “branch main lúc đó”.

Build number/versionCode nên monotonic theo release channel policy; versionName dành cho người dùng nhưng cũng cần convention nhất quán.

# 34. Rollback không chỉ là phát lại APK cũ

Nếu release mới đã migration database, thay server contract hoặc ghi data schema mới, rollback binary có thể không đủ. Migration phải cân nhắc backward compatibility và rollback window.

Server/mobile version skew là trạng thái bình thường vì user không update đồng thời. API contract nên chịu được nhiều app version trong một khoảng thời gian xác định.

# 35. Incident response trên mobile

Mobile incident khó hơn web vì không thể patch mọi device ngay lập tức. Cần remote config/feature flag hợp lý, backend mitigation, staged rollout và observability để giảm blast radius.

Khi incident xảy ra, ưu tiên giảm tác động trước rồi mới root-cause. Postmortem nên tạo action về test, telemetry, rollout hoặc architecture—not chỉ “developer cẩn thận hơn”.

# 36. Bản đồ mastery cuối cùng

Master Kotlin/Android không có nghĩa nhớ mọi API. Hãy giữ bốn mental model xuyên suốt: **type/contract** ở language level; **lifetime/state/failure** ở concurrency và UI; **source-of-truth/boundary** ở architecture/data; **measurement/governance** ở production engineering.

Khi gặp library mới, đặt nó vào bốn mental model này sẽ giúp hiểu nhanh hơn học syntax riêng lẻ.

# 37. Cách review một feature end-to-end

Lần theo từ user action → UI state/event → ViewModel/use case → repository/source → network/database → response/error → state mới → telemetry. Sau đó hỏi điều gì xảy ra khi rotate, process kill, offline, retry, duplicate input, app update, schema migration và rollback.

Nếu hệ thống có câu trả lời nhất quán cho chuỗi này, kiến thức đã vượt khỏi mức “biết framework” và tiến tới engineering mastery.
