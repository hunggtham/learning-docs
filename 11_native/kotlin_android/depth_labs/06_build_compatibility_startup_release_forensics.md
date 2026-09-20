# Depth Lab 06 — Build, Compatibility, Startup và Release Forensics

Một Android app production không chỉ là source code Kotlin chạy đúng trong IDE. Code phải đi qua Gradle/AGP/Kotlin compiler, resource/manifest merge, D8/R8, packaging, signing, distribution và platform compatibility trước khi user thực sự chạy nó. Nhiều bug chỉ xuất hiện ở release build, một variant cụ thể, một API level mới hoặc sau khi target SDK tăng.

Depth Lab này đào sâu cách reasoning từ **source -> build graph -> artifact -> install -> startup -> runtime compatibility -> release**.

---

## 1. Build failure và runtime failure có thể cùng nguồn gốc nhưng khác phase

Ví dụ annotation processor generated code sai có thể fail compile.

R8 remove class dùng reflection có thể compile/build thành công nhưng crash runtime release.

Manifest merge có thể khiến app install được nhưng component exported sai.

Hãy luôn hỏi bug xuất hiện ở phase nào:

```text
configuration
compilation
code generation
resource processing
DEX/shrinking
packaging
signing
installation
class loading
startup
runtime behavior
```

Phase xác định loại evidence cần thu thập.

---

## 2. Gradle configuration graph khác task execution graph

Gradle phải đọc build logic và tạo model task trước khi execute task cần thiết.

Build chậm có thể đến từ:

```text
configuration quá nặng
plugin làm I/O trong configuration
nhiều project/module
non-cacheable task
poor incremental inputs
```

Không phải mọi build-slow issue đều do compiler.

---

## 3. Convention plugin giúp tập trung policy, không chỉ giảm copy-paste

Nếu 30 module đều copy:

```kotlin
android {
    compileSdk = ...
    kotlinOptions ...
}
```

config dễ drift.

Convention plugin có thể encode policy:

```text
Android library baseline
Compose module baseline
feature module baseline
testing baseline
lint baseline
```

Lợi ích lớn nhất là **governance**: upgrade toolchain có một số boundary rõ thay vì sửa từng module tùy ý.

---

## 4. Version catalog quản lý coordinates, không thay dependency policy

`libs.versions.toml` giúp centralize version/alias.

Nhưng nó không tự trả lời:

```text
module nào được phép phụ thuộc library nào?
version nào approved?
transitive dependency nào rủi ro?
```

Catalog là syntax/management tool. Dependency governance vẫn cần rule và ownership.

---

## 5. `api` vs `implementation` ảnh hưởng compile graph

Nếu library module expose dependency type trong public API, consumer cần dependency đó trên compile classpath.

Dùng `api` mở rộng public dependency surface.

Dùng `implementation` giữ dependency private hơn và có thể giảm recompilation downstream.

Rule:

> dependency visibility nên phản ánh public ABI, không chỉ “dùng cái nào build được”.

---

## 6. Build variant là product state space

Nếu có:

```text
buildType: debug/release
flavor: free/paid
region: kr/global
```

variant có thể tăng theo tích Descartes:

```text
2 x 2 x 2 = 8 variants
```

Mỗi dimension làm tăng:

```text
CI matrix
manifest/resource override
signing config
test coverage
release complexity
```

Đừng dùng flavor để encode mọi runtime feature flag.

---

## 7. Source set precedence cần được hiểu như override graph

Ví dụ:

```text
src/main
src/free
src/release
src/freeRelease
```

Một resource/class/config có thể được override ở source set cụ thể.

Bug “debug đúng, release sai” thường đến từ source-set divergence.

Khi debug variant-specific issue, inspect merged source/resource/manifest output thay vì chỉ đọc `main`.

---

## 8. Manifest merger là hidden architecture boundary

Library có thể đóng góp:

```text
provider
receiver
service
permission
metadata
```

App final manifest là merge result.

Một SDK thêm auto-init ContentProvider có thể ảnh hưởng startup mà app code không gọi trực tiếp.

Do đó final merged manifest là artifact cần review trong release forensic.

---

## 9. Resource merge cũng có collision và override semantics

Tên resource global trong application package có thể collision giữa app/library.

Library author nên prefix resource khi phù hợp.

Consumer cần hiểu resource override có thể thay library behavior nếu library dùng public resource hook.

---

## 10. Generated code là part của build contract

KSP/compiler plugin/codegen tạo source app không viết tay.

Khi generated code fail:

```text
input annotation/API changed?
processor/plugin version compatible với Kotlin/AGP?
incremental processing invalidation đúng?
generated source ở đâu?
```

Debug generated code bằng cách inspect output, không coi plugin là “magic”.

---

## 11. KSP migration không chỉ là đổi plugin name

Processor phải support KSP.

Generated API/behavior có thể khác.

Build performance có thể tốt hơn, nhưng correctness và compatibility cần test.

Migration toolchain luôn cần release note + sample build + full CI.

---

## 12. D8 và R8 giải quyết hai vấn đề khác nhau

Mental model đơn giản:

```text
JVM bytecode -> D8 -> DEX
release shrink/optimize/obfuscate -> R8
```

R8 có thể:

```text
remove unused code
inline
rename
rewrite/optimize
```

Vì vậy release-only crash phải nghĩ tới shrinker/reflection/generated metadata.

---

## 13. Reflection phá static reachability assumption

Code:

```kotlin
Class.forName("com.example.PluginImpl")
```

R8 không luôn suy ra class cần giữ nếu reference chỉ là string/dynamic metadata.

Keep rule phải càng hẹp càng tốt.

Bad:

```proguard
-keep class ** { *; }
```

sẽ phá shrink benefit.

---

## 14. Serialization và reflection cần consumer rules đúng

SDK/library có thể cần ship consumer ProGuard rule để consumer app không phải tự biết internals.

Library author phải test:

```text
sample consumer release + minifyEnabled true
```

Không chỉ test library module compile.

---

## 15. Mapping file là production debugging artifact

Sau obfuscation, stack trace cần mapping để deobfuscate.

Release pipeline phải lưu/upload mapping theo build id/version.

Nếu artifact đã rollout nhưng mapping thất lạc, crash forensic khó hơn nhiều.

---

## 16. Signing key là long-term identity

Update app cần compatible signing identity.

Signing key loss/rotation là release-engineering incident, không phải build detail nhỏ.

Production key không nên nằm plain trong repo.

Quyền truy cập signing material cần least privilege/audit.

---

## 17. Build reproducibility giúp forensic

Khi incident xảy ra, cần trả lời:

```text
source commit nào tạo artifact này?
dependency version chính xác?
toolchain version?
feature config?
signing lineage?
```

Artifact metadata nên nối về source commit và CI run.

---

## 18. Dependency lock giúp giảm “same source, different binary”

Nếu dynamic/transitive resolution thay đổi theo thời gian, rebuild commit cũ có thể ra dependency graph khác.

Dependency locking/version pinning giúp forensic và supply-chain control.

---

## 19. `minSdk`, `compileSdk`, `targetSdk` là ba contract khác nhau

```text
minSdk -> device cũ nhất app hỗ trợ
compileSdk -> API surface compiler biết
 targetSdk -> behavior contract app opt-in với platform mới
```

Tăng compileSdk có thể không đổi runtime behavior ngay.

Tăng targetSdk có thể activate behavior changes dù source code gần như không đổi.

---

## 20. Platform migration nên tách compile migration và behavior migration

Một chiến lược:

```text
Step 1: upgrade toolchain/compileSdk
Step 2: fix compile/deprecation
Step 3: giữ targetSdk cũ, regression test
Step 4: enable target behavior changes có kiểm soát
Step 5: bump targetSdk
Step 6: device/API matrix test
```

Tách dimension giúp giảm số biến thay đổi cùng lúc.

---

## 21. Behavior change có thể apply cho mọi app hoặc target-gated

Khi đọc Android release notes, phân biệt:

```text
changes affecting all apps running on version X
changes only if targetSdk >= X
```

Nếu không phân biệt, team có thể bỏ lỡ regression trên device mới dù chưa bump target.

---

## 22. Compatibility framework là migration tool

Android có compatibility framework cho phép một số behavior change được toggle trong dev/test.

Điều này giúp isolate:

```text
bug do OS mới?
hay do target behavior cụ thể?
```

Dùng toggle như diagnostic/migration aid, không phải production long-term bypass.

---

## 23. API guard bảo vệ class loading/runtime access

```kotlin
if (Build.VERSION.SDK_INT >= 33) {
    useNewApi()
}
```

Nhưng cần cẩn thận với static initialization/class verification ở một số pattern cũ.

Tách API-specific code vào method/class rõ có thể giúp compatibility và readability.

---

## 24. Desugaring mang một số language/library feature xuống API cũ

Developer có thể dùng modern Java API trên minSdk thấp nếu desugaring hỗ trợ.

Nhưng không phải mọi Android framework API đều được “backport”.

Phải phân biệt:

```text
Java language/library desugaring
vs
Android framework API availability
```

---

## 25. SDK Extensions làm API availability không còn chỉ là API level

Một API có thể available theo extension version trên cùng Android API level.

Check cần dựa contract của API, không luôn chỉ `SDK_INT`.

Mental model compatibility ngày càng là capability check hơn integer check đơn giản.

---

## 26. Non-SDK interface là compatibility risk

Reflection/internal platform API có thể bị restrict theo Android version.

Nếu library phụ thuộc hidden API, app có thể vỡ khi OS mới dù source không đổi.

Production code nên ưu tiên public SDK contract.

---

## 27. OEM behavior là dimension ngoài API level

Hai device cùng API level có thể khác:

```text
battery manager
camera implementation
background restriction
Bluetooth stack
WebView version
```

Compatibility test matrix cần OEM risk-based, không chỉ emulator API matrix.

---

## 28. WebView là independently updated runtime

WebView behavior có thể đổi qua update component mà không đổi Android OS version.

Hybrid app cần log WebView version khi debug issue rendering/JS bridge/network.

---

## 29. Startup phải được xem như dependency critical path

Cold start path:

```text
process fork
-> Application
-> providers/initializers
-> DI graph
-> Activity creation
-> first composition/layout/draw
-> first frame
-> usable content
```

Mọi eager initializer nằm trên critical path đều cộng latency.

---

## 30. TTID và TTFD trả lời hai câu khác nhau

TTID:

```text
khi nào frame đầu xuất hiện?
```

TTFD:

```text
khi nào UI thực sự usable/full content?
```

Một app có TTID rất nhanh nhờ splash/placeholder nhưng data usable sau 5 giây vẫn có UX tệ.

Track cả hai khi phù hợp.

---

## 31. Eager initialization phải có lý do

Một SDK analytics không nhất thiết cần fully initialize trước first frame.

Một security/session dependency có thể cần sớm hơn.

Classify initializer:

```text
required before first frame
required before first interaction
can defer background
demand-driven lazy
```

Đây là dependency scheduling problem.

---

## 32. ContentProvider auto-init có thể ẩn startup work

Một library có thể auto-init qua manifest provider.

App team không thấy call trong Application nhưng startup vẫn chậm.

Forensic cần inspect merged manifest + startup trace.

---

## 33. App Startup giúp declare initializer dependencies

Initializer có thể phụ thuộc initializer khác.

Nhưng dùng framework không tự làm initialization rẻ hơn.

Cần vẫn phân loại eager/lazy và đo cost.

---

## 34. DI container creation có thể nằm critical path

Large dependency graph, reflection hoặc eager singleton construction có thể làm startup chậm.

Review object nào thực sự cần instantiate trước first screen.

Lazy provider không phải lúc nào xấu; nó có thể chuyển cost tới đúng feature usage.

---

## 35. Startup I/O trên main thread là red flag

Examples:

```text
large SharedPreferences read
DB query
file scan
network wait
JSON parse lớn
```

Main thread cần tạo first frame nhanh.

StrictMode và Perfetto giúp phát hiện blocking work.

---

## 36. Nhưng “move everything background” cũng không đủ

Nếu first screen bắt buộc data A trước khi meaningful render, data A vẫn nằm critical user path dù chạy background.

Optimization cần:

```text
less work
cache
precompute
progressive rendering
parallelism phù hợp
```

không chỉ đổi thread.

---

## 37. Baseline Profile tối ưu code compilation path

Profile giúp runtime compile/precompile critical methods/classes.

Nó không loại bỏ I/O/business work.

Benchmark effect thay vì assume.

---

## 38. Macrobenchmark startup cần control compilation mode

Đo cold startup nhiều lần với profile/compilation state phù hợp giúp phân biệt compiler benefit và application work.

Benchmark phải stable enough để regression meaningful.

---

## 39. Release-only issue forensic checklist

Khi debug “debug OK, release crash”:

```text
R8/minification?
resource shrink?
reflection?
consumer rules?
signing/config?
BuildConfig/flavor value?
manifest merge?
network security config?
proguard mapping?
```

Đừng debug business code trước khi loại trừ build-mode difference.

---

## 40. Variant-only bug checklist

```text
sourceSet override?
manifest placeholder?
resource override?
different dependency?
different endpoint?
signing certificate-dependent API?
feature flag default?
```

Always reproduce exact variant.

---

## 41. Upgrade forensic nên change one axis at a time

Nếu cùng lúc nâng:

```text
Kotlin
AGP
Gradle
Compose
compileSdk
targetSdk
Room
```

và build/runtime hỏng, search space rất lớn.

Upgrade theo compatible slices khi có thể, commit nhỏ và CI sau mỗi slice.

---

## 42. Dependency graph diff là artifact review hữu ích

Trước/after toolchain upgrade, compare:

```text
resolved versions
new transitive deps
removed deps
native libraries
license/security metadata
```

Một indirect update có thể đổi runtime behavior.

---

## 43. AAB khiến installed APK phụ thuộc device configuration

Upload artifact không nhất thiết giống byte-for-byte package user cài.

Delivery có thể split theo:

```text
ABI
density
language
feature module
```

Release test nên dùng bundletool/Play track để test actual delivery path khi relevant.

---

## 44. Artifact provenance nên xuyên từ commit tới installed build

Useful fields:

```text
versionName
versionCode
git SHA
CI build id
build time/toolchain hash
feature config version
```

Không expose secret; mục tiêu là forensic traceability.

---

## 45. Release gate nên verify artifact, không chỉ source

Gate:

```text
assemble/bundle release
run lint/tests
R8 success
mapping captured
signing verified
bundle/APK inspected
smoke install
critical journey
```

Source test pass chưa chứng minh final artifact đúng.

---

## 46. Build/compatibility checklist

| Câu hỏi | Evidence |
|---|---|
| Variant graph có cần thiết không? | product matrix |
| Source set override rõ không? | merged output |
| Dependency API surface tối thiểu chưa? | api vs implementation |
| Release minify đã test chưa? | R8 sample run |
| Mapping/artifact lưu chưa? | CI artifact |
| Target migration tách behavior chưa? | compatibility plan |
| API availability check đúng contract chưa? | SDK/extension guard |
| OEM/WebView risk có test không? | device matrix |
| Startup critical path đã trace chưa? | Perfetto/Macrobenchmark |
| Rollback artifact/data compatible không? | release drill |

---

## 47. Kết luận

Android build và platform compatibility nên được xem như một continuous compiler/distribution/runtime contract.

Mental model:

```text
source
-> dependency graph
-> variant
-> generated/merged inputs
-> compiler/DEX/R8
-> signed artifact
-> delivery
-> platform behavior
-> startup critical path
-> production evidence
```

Khi debug theo phase và artifact thay vì chỉ đọc source code, nhiều bug “chỉ xảy ra trên release/device X” trở nên có cấu trúc để điều tra.