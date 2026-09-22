# 12 — Build, Configuration, Deployment & Environment Reasoning

WebSquare developer thường dành phần lớn thời gian trong XML page và JavaScript, nhưng production behavior không chỉ đến từ source code. Một page có thể đúng trong Studio và sai ở UAT vì W-Pack artifact khác; cùng artifact có thể chạy khác vì client/server config; cùng config có thể cho kết quả khác vì context root, cache, reverse proxy hoặc engine build.

Vì vậy deployment phải được hiểu như một **chuỗi biến đổi có provenance**, không phải thao tác “copy file lên server”.

> Prerequisite: [01 — Platform, Runtime & Page Model](01_platform_runtime_page_model.md), [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md) và [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

## 1. Mental model: source không phải runtime artifact

Trong WebSquare5 SP5, page thường được author bằng XML nhưng W-Pack chuyển source thành JavaScript để engine/browser sử dụng. Official guide mô tả artifact page dưới `_wpack_` và common resource được chuyển tương ứng.

Pipeline cần reasoning như sau:

```text
XML/JS/CSS source
→ WebSquare configuration
→ W-Pack/build
→ generated artifact
→ package/deploy
→ web server/WAS/reverse proxy
→ browser cache/network
→ WebSquare Engine
→ runtime page
```

Bug production có thể xuất hiện ở bất kỳ mũi tên nào. Vì vậy “Git source đúng” chưa chứng minh “browser đang chạy đúng code”.

## 2. Ba identity cần phân biệt

Một release nên có ít nhất ba identity rõ.

**Source identity** trả lời source commit nào được chọn.

**Build identity** trả lời source đó được build bằng engine/tool/config nào và tạo artifact nào.

**Deployment identity** trả lời artifact nào đang thực sự phục vụ ở environment nào.

Nếu ba identity này bị trộn, team dễ rơi vào tình huống:

```text
“commit đã merge”
≠ “artifact đã rebuild”
≠ “artifact mới đã deploy”
≠ “browser user đã nhận artifact mới”
```

Production troubleshooting phải biết mình đang đứng ở bước nào.

## 3. Studio build và CI build là hai execution environment

SP5 Studio có thể tự W-Pack khi project build/rebuild. Tài liệu chính thức cũng cung cấp stand-alone W-Pack để chạy từ command line và tích hợp CI/server batch conversion.

Điều này tạo một requirement quan trọng: **CI build phải là build có thể tái tạo**, không phụ thuộc một developer đã click menu nào trong Studio.

Nếu local Studio tạo artifact khác CI, cần so:

```text
Studio/W-Pack version
engine/build package
W-Pack options
source include/exclude
common resource configuration
minification/obfuscation mode
path/context-root assumptions
```

Đừng chữa bằng cách commit artifact được tạo thủ công từ một máy mà chưa hiểu khác biệt.

## 4. W-Pack là compiler-like boundary

W-Pack không phải JavaScript compiler theo nghĩa ECMAScript language compiler, nhưng trong delivery pipeline nó đóng vai trò tương tự một transformation boundary: source authoring được chuyển thành runtime artifact.

Điều đó có ba consequence.

Thứ nhất, build error phải fail pipeline thay vì bị bỏ qua rồi deploy artifact cũ.

Thứ hai, generated output cần trace về source/build version.

Thứ ba, test phải chạy trên artifact gần với thứ sẽ deploy, không chỉ trên XML source trong development mode.

Một release process chỉ test Studio preview nhưng production chạy minified W-Pack output đang bỏ qua một boundary quan trọng.

## 5. Build reproducibility

Một build có thể gọi là reproducible về mặt vận hành khi cùng source + cùng toolchain + cùng config input tạo ra artifact tương đương về behavior.

Không nhất thiết byte-for-byte giống nếu tool chèn timestamp/hash, nhưng behavior và dependency graph phải deterministic.

Hãy version hóa hoặc quản lý rõ:

```text
WebSquare engine/tool build
W-Pack executable/version
build arguments
client/server config source
common modules/resources
third-party JS/CSS versions
browser support target
```

“Máy anh A build được” không phải build specification.

## 6. Client configuration và server configuration là hai boundary khác nhau

SP5 Studio cung cấp `client.config.xml` và `server.config.xml` trong WebSquare Configure. Tài liệu chính thức mô tả client config là nhóm setting liên quan browser/UI/runtime phía client, còn server config là nhóm setting cho WebSquare Engine/server behavior như module processing, Excel/CSV, framework adaptor, multilingual và Hybrid.

Trong artifact/runtime, các file nền như `config.xml` và `websquare.xml` vẫn xuất hiện trong documentation/config model. Tên file cụ thể và cách Studio materialize chúng có thể khác theo project/generation, vì vậy hãy phân biệt **logical configuration role** với **một filename bạn nhớ từ project cũ**.

Mental model:

```text
client configuration
→ browser/runtime/page behavior

server configuration
→ engine/server-side behavior
```

Một property ở client không thể thay thế server security policy; một server setting cũng không tự sửa page JavaScript logic.

## 7. Configuration is code

Config thay đổi behavior production, nên cần review, version history và rollback giống code.

Một thay đổi nhỏ như context root, debug mode, Submission default, engine type, cache hoặc locale có thể ảnh hưởng hàng trăm page mà không sửa một dòng XML page nào.

Do đó config change nên trả lời:

```text
vì sao đổi
scope environment nào
default cũ/mới
backward compatibility
security/performance consequence
rollback path
regression area
```

Không nên chỉnh trực tiếp production config rồi “sau này cập nhật Git”. Khi đó source of truth đã bị đảo ngược.

## 8. Environment-specific config không nên biến source thành nhiều fork

Local, DEV, UAT và PROD cần endpoint/context/log level khác nhau. Cách nguy hiểm là copy cả project thành bốn phiên bản rồi sửa tay.

Tốt hơn là có canonical source và explicit environment input/overlay theo pipeline của tổ chức.

Mental model:

```text
canonical application source
+
environment-specific values
→ resolved deploy configuration
```

Không hard-code production URL trong page nếu environment mechanism đã tồn tại.

## 9. Secret không thuộc client config

Bất cứ thứ gì browser tải được đều có thể bị user inspect. Vì vậy API secret, private key, database password hoặc credential privileged không được đặt vào client-side WebSquare config, JavaScript hay DataCollection với hy vọng “obfuscation sẽ che”.

W-Pack obfuscation/minification làm source khó đọc hơn, không tạo security boundary.

Secret management thuộc server/deployment platform.

## 10. Context root là routing contract

Context root ảnh hưởng cách page/resource/request được resolve. Một app chạy ở `/` local nhưng production ở `/bank/app/` có thể lộ hard-coded absolute path.

Test cần bao phủ:

```text
WFrame src
Submission action
image/static resource
common JS/CSS
popup/page navigation
upload/download endpoint
```

Không phải mọi servlet/resource đều nhất thiết áp dụng cùng context-root rule trong mọi build. Release note SP5 từng thay đổi behavior `contextRoot` cho nhiều loại resource, nên exact behavior phải kiểm chứng theo engine build.

Senior note: path bug thường bị hiểu nhầm thành “WFrame không load” hoặc “Submission lỗi”, trong khi root cause là URL resolution.

## 11. Engine build là dependency production

Hai environment cùng application source nhưng khác WebSquare engine build không phải cùng runtime.

Release note SP5 cho thấy engine liên tục sửa behavior của WFrame, TabControl, config, W-Pack, cache và nhiều component. Vì vậy incident report nên ghi exact engine build, không chỉ “WebSquare5 SP5”.

Version inventory tối thiểu:

```text
application release
WebSquare engine build
Studio/W-Pack build dùng để tạo artifact
browser version
server/WAS relevant version
```

Nếu UAT và PROD khác engine build, regression result UAT không hoàn toàn đại diện PROD.

## 12. `engineType` và development/production behavior

SP5 server configuration có `engineType` với các mức remapping/debug/log khác nhau. Official guide khuyến nghị development và production dùng mode phù hợp khác nhau; production thường dùng engine đã loại bớt debug information để giảm footprint.

Đừng học con số như magic constant. Điều cần hiểu là trade-off:

```text
nhiều debug metadata/log
→ dễ diagnose hơn
→ artifact/runtime nặng hơn hoặc lộ nhiều detail hơn

production-optimized engine
→ nhỏ/gọn hơn
→ diagnosis có thể cần source map/log strategy tốt hơn
```

Trước khi đổi engine type, kiểm tra compatibility và observability requirement của site.

## 13. Debug configuration không được leak sang production vô thức

Client config có các setting liên quan debug/console/debug menu ở các build tương ứng. Chúng hữu ích ở development nhưng có thể tạo noise hoặc expose operational detail nếu bật không chủ đích ở production.

Production policy nên quyết định rõ:

```text
console logging mức nào
remote log có hay không
context debug menu có cho phép không
source map public/private
PII redaction
client exception reporting
```

Không phải “production thì tắt hết log”. Production cần observability, nhưng signal phải có chủ đích và an toàn.

## 14. Cache là một phần của deployment semantics

WebSquare app có nhiều lớp cache có thể cùng tồn tại:

```text
browser HTTP cache
reverse proxy/CDN cache
web server static cache
engine/config cache
service worker nếu application dùng
```

Deploy source mới nhưng cache cũ vẫn phục vụ artifact cũ tạo trạng thái khó hiểu: HTML shell mới + common JS cũ + page W-Pack mới, hoặc ngược lại.

Vì vậy release phải có cache invalidation/versioning strategy. “Ctrl+F5 là được” không phải production strategy.

## 15. Cache key phải gắn với artifact identity

Một cách phổ biến là version/hash trong resource URL hoặc postfix theo mechanism của platform/project. SP5 release note có các capability liên quan config/W-Pack caching ở từng build, nhưng exact setting thay đổi theo version.

Mental model quan trọng:

```text
artifact content thay đổi
→ cache identity phải thay đổi hoặc cache phải được invalidated
```

Nếu content đổi nhưng URL/cache key không đổi và TTL dài, user có thể chạy mixed release.

## 16. Static compression và network configuration

Official performance guide khuyến nghị cache header và compression cho static resource; network/server configuration có thể ảnh hưởng lớn đến initial load.

Đừng tối ưu JavaScript loop 20 ms khi production đang tải nhiều MB resource không gzip hoặc thực hiện handshake không cần thiết cho hàng chục request.

Performance diagnosis phải nhìn waterfall trước khi kết luận framework chậm.

## 17. Artifact manifest

Một deployment mature nên có manifest hoặc metadata tương đương để trả lời:

```text
source commit
build timestamp/id
WebSquare/W-Pack version
config profile
artifact checksum/version
release number
```

Không cần format cụ thể. Mục tiêu là khi user gửi screenshot lúc 14:32, team có thể biết browser có khả năng đang chạy release nào.

## 18. Generated artifact không phải nơi sửa source

Nếu bug được “hotfix” trực tiếp trong `_wpack_/*.js`, source XML/JS canonical không biết thay đổi đó. Lần rebuild sau hotfix biến mất.

Emergency patch đôi khi có operational constraint riêng, nhưng sau đó phải reconcile về canonical source ngay và trace rõ divergence.

Nguyên tắc:

```text
source là nơi author
artifact là output
production là deployment của artifact
```

Đảo ba vai trò này tạo configuration/build debt rất nhanh.

## 19. Build phải fail khi artifact không đầy đủ

Một pipeline không nên thành công nếu W-Pack báo lỗi nhưng giữ file output cũ từ build trước.

Dùng clean output hoặc artifact directory mới theo build để tránh stale file masquerade.

Kiểm tra sau build:

```text
expected page artifact tồn tại
common module artifact tồn tại
không có fatal build error
manifest trỏ đúng source/build
artifact package không chứa file dev ngoài policy
```

## 20. Common resource thay đổi có blast radius lớn

Một common JS/CSS/UDC được dùng hàng trăm screen. Build/deploy common layer vì vậy có risk khác page riêng lẻ.

Release impact analysis nên hỏi:

```text
consumer nào dùng resource này
public contract có đổi không
cache key có đổi không
load order có đổi không
Scope/global assumption có đổi không
```

Regression suite phải ưu tiên representative consumers, không chỉ test demo page của common module.

## 21. Load order là dependency contract

Legacy enterprise app thường có common global JS phụ thuộc thứ tự load. W-Pack/common module config thay đổi có thể làm hidden dependency lộ ra.

Nếu `commonB.js` chỉ chạy vì `commonA.js` tình cờ tạo global trước, architecture đang phụ thuộc implicit load order.

Hướng tốt hơn là explicit dependency/module contract. Nếu chưa thể refactor, ít nhất build/test phải lock và kiểm tra order có chủ đích.

## 22. External JavaScript và third-party dependency

Third-party widget/library cần version pinning và ownership. CDN URL “latest” làm runtime thay đổi mà application không deploy.

Nếu external script được đưa qua W-Pack mechanism ở build hỗ trợ, vẫn phải biết source version và license/security policy.

Dependency upgrade phải có regression ở screen thật, đặc biệt nếu library thao tác DOM mà WebSquare cũng quản lý.

## 23. Deploy atomically khi có thể

Mixed artifact là failure mode nguy hiểm. Nếu deploy ghi đè file từng phần trong khi user đang load app, request đầu có thể lấy common file cũ, request sau lấy page mới.

Một deployment tốt cố tạo atomic release boundary bằng versioned directory, package switch, immutable artifact hoặc mechanism tương đương của hạ tầng.

Nếu platform không hỗ trợ atomic deploy hoàn toàn, maintenance/cache strategy phải giảm cửa sổ mixed-version.

## 24. Backward compatibility trong rolling deployment

Nếu frontend mới được phục vụ trong khi backend cũ/mới cùng tồn tại, API contract phải tương thích trong rollout window.

Ví dụ frontend mới gửi field `statusReason` nhưng một số backend node cũ reject unknown field. Đây không phải WebSquare bug mà là deployment compatibility bug.

Release planning phải xem frontend/backend như distributed system nếu rollout không đồng thời.

## 25. Database/backend transaction không thuộc frontend deployment nhưng ảnh hưởng rollback

Frontend rollback dễ hơn khi API/backend vẫn backward compatible. Nếu release đi kèm DB migration destructive, chỉ rollback WebSquare artifact có thể không đủ.

Do đó release plan critical flow cần biết:

```text
frontend artifact compatibility
API compatibility
DB migration direction
feature flag nếu có
rollback/roll-forward strategy
```

WebSquare library không giải thích DB migration internals; hãy dùng backend/database canonical docs cho phần đó.

## 26. Deployment smoke test dựa trên boundary

Sau deploy, đừng chỉ mở home page. Smoke test phải chạm các boundary dễ sai vì config/artifact:

```text
engine boot
common CSS/JS load
WFrame child load
Submission action resolve đúng path
DataCollection target mapping
Grid render
popup/navigation
locale resource nếu critical
upload/download nếu release đụng config tương ứng
```

Mục tiêu là phát hiện release/config issue trong vài phút.

## 27. Canary và representative user path

Nếu hạ tầng cho phép, canary một phần traffic/user trước rollout rộng giúp phát hiện browser/config/environment issue.

Canary signal nên gồm client exception, page-load failure, Submission error rate và latency của critical screen.

Không cần một platform observability phức tạp để áp dụng mental model: release nhỏ → quan sát evidence → mở rộng.

## 28. Rollback phải được diễn tập

Một rollback plan chưa từng chạy chỉ là giả thuyết.

Cần biết:

```text
artifact trước nằm ở đâu
cache invalidation khi rollback
config có rollback cùng không
backend/API còn compatible không
session/user state có ảnh hưởng không
```

Nếu rollback mất 40 phút vì phải tìm file WAR cũ trên laptop, release process chưa mature.

## 29. Config diff là first-class incident evidence

Khi “DEV chạy, PROD lỗi”, source diff thường bằng zero. Hãy diff environment:

```text
engine build
client config
server config
context root
reverse proxy rules
security headers
cache/compression
common resource version
backend endpoint
browser policy
```

Đây là cách biến “chỉ production mới lỗi” thành một finite search space.

## 30. Security header và browser policy

CSP, cookie policy, CORS, SameSite, frame restrictions và proxy header có thể làm behavior khác local.

Ví dụ external script chạy local nhưng bị CSP block production; popup/frame integration có thể bị browser policy chặn; cookie session có thể không gửi vì SameSite/domain/path.

Đừng disable security header để “WebSquare chạy được” trước khi hiểu dependency. Fix phải giữ security invariant và điều chỉnh resource/integration contract phù hợp.

## 31. File upload/download configuration có operational risk riêng

SP5 server config chứa nhiều setting cho upload, Excel và CSV. Những flow này liên quan temp directory, size, extension/content validation, encoding và memory.

Release đụng upload/download cần test trên environment gần production vì filesystem permission, proxy limit và server memory khác local.

Client success không chứng minh file đã được lưu/validate an toàn; security boundary vẫn ở server.

## 32. Encoding và locale drift

Korean enterprise system có thể gặp UTF-8, legacy encoding hoặc byte-length validation khác nhau. Một config encoding khác giữa environment có thể tạo lỗi chỉ với Korean/Vietnamese text.

Regression data nên chứa:

```text
한글
Tiếng Việt có dấu
ASCII
emoji nếu business cho phép
boundary byte length
```

Đừng chỉ test `TEST123` rồi kết luận encoding đúng.

## 33. Browser support matrix là release input

Official WebSquare engine documentation có browser support policy theo engine generation. Application thực tế có thể đặt policy hẹp hơn hoặc còn legacy requirement.

Release phải biết browser nào là supported target. Nếu code dùng modern JavaScript syntax/library, W-Pack/engine/toolchain và browser matrix phải thống nhất.

Không giữ workaround IE vô hạn chỉ vì code cũ có nó; cũng không xóa compatibility code nếu business vẫn hỗ trợ browser đó.

## 34. Observability phải sống qua minification

Production artifact minify/obfuscate làm stack khó đọc. Vì vậy cần error correlation, build ID và source mapping strategy phù hợp.

Một client error report hữu ích:

```text
release/build id
engine build
page/scope id
operation
correlation id
sanitized stack/error code
browser
```

Không log full DataList chứa PII chỉ để debug dễ hơn.

## 35. Release checklist không thay reasoning

Checklist hữu ích để không quên bước, nhưng không được biến thành ritual.

Ví dụ “clear cache” không phải câu trả lời nếu team không biết cache layer nào và vì sao cần clear. “Rebuild W-Pack” không đủ nếu không biết tool version và output nào được deploy.

Mỗi bước release nên gắn với failure mode mà nó phòng ngừa.

## 36. Example: source đã sửa nhưng production vẫn chạy code cũ

Triệu chứng: developer thấy commit mới, server cũng có XML mới, nhưng browser behavior không đổi.

Reasoning theo pipeline:

```text
source commit đúng?
→ W-Pack có rebuild page không?
→ _wpack_ artifact timestamp/hash đúng?
→ package có artifact mới không?
→ server đang serve đúng release directory không?
→ proxy/CDN/browser cache có giữ URL cũ không?
→ Network response body/build marker là version nào?
```

Đừng tiếp tục sửa JavaScript cho đến khi xác định browser thực sự chạy artifact nào.

## 37. Example: UAT pass, PROD WFrame 404

Nếu cùng source nhưng WFrame `src` 404 ở PROD, hypothesis đầu tiên nên là routing/config chứ không phải Scope.

So:

```text
context root
reverse proxy prefix
resolved WFrame URL
case sensitivity filesystem
artifact path
cache/rewrite rule
```

Sau khi page load được mới debug Scope/lifecycle. Đây là ví dụ của layer ordering trong troubleshooting.

## 38. Example: release mới làm initial load chậm gấp đôi

Tách cost:

```text
artifact size tăng?
request count tăng?
compression mất?
cache miss toàn bộ?
common module load thêm?
eager Tab/WFrame render tăng?
engine/config đổi?
```

Một release có thể không đổi business code nhưng config `alwaysDraw`, common resource hoặc cache policy làm startup chậm mạnh.

## 39. CI/CD gate gợi ý theo evidence

Một pipeline production-oriented có thể đi theo:

```text
source checkout tại commit cố định
→ static/syntax checks
→ W-Pack clean build
→ artifact integrity check
→ logic/integration tests
→ package immutable artifact
→ deploy DEV/UAT
→ smoke/regression
→ promote cùng artifact
→ production smoke
→ observe release metrics
```

Điểm quan trọng là **promote cùng artifact** khi có thể. Nếu UAT build một lần rồi PROD rebuild lại từ source, bạn đã test artifact A nhưng deploy artifact B.

## 40. Promote artifact, không rebuild vô thức

Build-once-promote là mental model mạnh cho reproducibility:

```text
commit C
→ artifact A
→ test A ở UAT
→ deploy chính A lên PROD
```

Environment-specific secret/config có thể được inject/resolve theo platform, nhưng application artifact core không nên thay đổi không trace giữa stage.

Nếu bắt buộc rebuild mỗi environment, phải chứng minh build inputs deterministic và diff output được kiểm soát.

## 41. Production change log nên ghi behavior, không chỉ commit

Một release note nội bộ tốt cho WebSquare có thể ghi:

```text
changed pages/UDC/common modules
engine/config change
W-Pack/toolchain change
API contract dependency
cache/context-root impact
migration/rollback note
known risk
```

Điều này giúp incident responder biết nơi tìm trước khi đọc hàng trăm commit.

## 42. Senior note: deployment architecture là một phần của frontend correctness

Nếu page chỉ chạy khi developer tự clear cache, correctness chưa hoàn chỉnh.

Nếu build chỉ thành công trên một Studio cá nhân, delivery chưa reproducible.

Nếu PROD khác UAT engine build mà không ai biết, regression evidence yếu.

Nếu rollback cần sửa file tay, release boundary không rõ.

Frontend engineering production không kết thúc ở `scwin` function. Nó kết thúc khi đúng artifact, đúng config, đúng dependency được phục vụ có thể quan sát và rollback được.

## 43. Mental model cuối chapter

Hãy nhìn mỗi release theo chuỗi:

```text
canonical source
→ deterministic build inputs
→ W-Pack/runtime artifact
→ immutable release identity
→ environment configuration
→ deployment/routing/cache
→ browser execution
→ observable evidence
→ rollback or roll-forward
```

Khi có incident, đi ngược chuỗi bằng evidence. Đừng giả định layer trước đúng chỉ vì layer sau trông quen thuộc.

## Nguồn đối chiếu

Các fact WebSquare-specific trong chapter này dựa trên WebSquare5 SP5 Development Guide, đặc biệt phần Project Configuration, JS Conversion/W-Pack, client configuration, server configuration, debugging và performance guide; đồng thời release note SP5 được dùng để nhấn mạnh rằng config/W-Pack/WFrame behavior thay đổi theo engine build. Exact option/default phải luôn được kiểm tra lại với tài liệu của build project đang chạy.