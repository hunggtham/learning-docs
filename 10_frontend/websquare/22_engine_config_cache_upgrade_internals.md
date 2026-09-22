# 22 — Engine, Configuration, Cache & Upgrade Internals

Một trong những câu khó nhất trong production WebSquare là: **browser đang chạy chính xác cái gì?**

Developer thường nhìn XML source trên Git và nghĩ đó là runtime. Nhưng WebSquare5 có Engine, W-Pack artifact, client/server configuration, resource cache, web server/proxy cache và browser cache. Cùng một commit có thể tạo behavior khác nếu engine build hoặc config khác; cùng một environment có thể phục vụ artifact khác cho hai browser nếu cache identity không được kiểm soát.

Chapter 12 đã giải thích build/deployment pipeline. Chapter này đi sâu hơn vào **runtime composition, configuration precedence, cache layers, engine build identity và upgrade reasoning**.

> Mental model chính: `runtime behavior = source + generated artifact + engine build + configuration + resource resolution + browser state`.

## 1. Runtime không phải một file

Một WebSquare screen có thể phụ thuộc:

```text
websquare.html / bootstrap
WebSquare Engine resources
client configuration
server/engine configuration
W-Pack JS artifact
common JS/component
UDC/template-derived source
language pack
CSS/image/font
business API
browser cache/state
```

Khi chỉ một layer stale, symptom có thể trông như code bug.

## 2. Browser call chain

Official SP5 guide mô tả flow ở mức khái niệm:

```text
browser calls page
→ WebSquare bootstrap/engine starts
→ page source path resolved
→ W-Pack-generated JavaScript loaded
→ Engine creates/render page
```

Điều quan trọng là XML authoring source và JS runtime artifact không phải cùng identity.

## 3. Source graph và runtime graph

Source graph:

```text
XML
JS source
CSS
config source
```

Runtime graph:

```text
engine bundle
config.js/runtime config
_wpack_ artifact
common modules
cached resources
```

Debug production phải quan sát runtime graph.

## 4. Engine build là dependency thực

Tên “WebSquare5 SP5” chưa đủ.

Release note dùng build identity chi tiết. Property, default, bug fix, security behavior và component internals có thể thay đổi giữa build.

Do đó incident report nên có:

```text
product generation
SP/build version
Studio/build tool version nếu liên quan
W-Pack build identity
browser version
```

## 5. `engineType` và dev/prod behavior

SP5 server configuration có `engineType` để điều khiển mức mapping/minification/debug/log behavior của engine. Official guide khuyến nghị configuration khác cho development và production ở các mức tương ứng.

Không học thuộc một con số mà bỏ qua build. Mental model là:

```text
development engine
→ debug visibility cao hơn

production engine
→ optimized/minified/log behavior khác
```

Nếu PROD stack trace khác DEV, có thể do engine build/type chứ không phải exception khác.

## 6. Client config vs server config

SP5 tách configuration phía client và engine/server.

**client configuration** ảnh hưởng behavior phía browser/component/Submission/resource resolution.

**server configuration** ảnh hưởng engine processing, W-Pack, upload/download, encoding và integration-related behavior.

Tên file/generated representation có thể khác theo project/tooling; hãy dựa vào Studio/official guide đúng build.

## 7. Configuration là code vận hành

Config thay đổi behavior production nên phải được review/version/control tương tự source.

Anti-pattern:

```text
DEV chỉnh bằng Studio
UAT chỉnh tay trên server
PROD có XML khác nhưng không commit
```

Khi incident xảy ra không ai biết canonical config.

## 8. Config provenance

Một release nên trace:

```text
source commit
+ config commit/version
+ W-Pack tool/build
+ engine build
→ artifact set
→ environment
```

Nếu config được inject theo environment, cần biết input nào tạo runtime config cuối cùng.

## 9. Context root là part of resource identity

Context root ảnh hưởng path resolution của page/resource/API.

Bug điển hình:

```text
DEV: /
PROD: /app
```

Hard-coded absolute/relative path có thể hoạt động ở DEV nhưng 404 ở PROD.

Không fix bằng thêm `../` ngẫu nhiên. Hãy xác định canonical path-resolution rule.

## 10. W-Pack là compiler-like boundary

W-Pack chuyển page XML thành JavaScript artifact tối ưu cho runtime.

Hãy reasoning như compiler pipeline:

```text
source
→ transform
→ generated artifact
→ runtime load
```

Bug có thể ở source, transform config, stale artifact hoặc runtime engine.

## 11. Generated artifact không nên sửa tay

Nếu `_wpack_` JS được generate, sửa trực tiếp file generated tạo divergence:

```text
source says A
generated file manually says B
next build returns A
```

Fix phải ở canonical source/config/build pipeline.

## 12. Clean build khi nào cần

Incremental build nhanh nhưng có thể che stale artifact khi dependency/config thay đổi.

Khi gặp behavior không giải thích được:

```text
capture evidence
→ clean generated output
→ rebuild deterministic
→ compare artifact hash/content
```

Không biến “clean everything” thành nghi thức cho mọi bug; dùng khi artifact provenance đáng nghi.

## 13. Cache có nhiều tầng

Ít nhất có thể có:

```text
browser memory cache
browser disk cache
service worker nếu project có
reverse proxy/CDN cache
web server cache
WebSquare engine/resource cache
W-Pack/resource postfix strategy
application cache riêng
```

“Đã Ctrl+F5” không chứng minh mọi tầng đã invalidated.

## 14. Cache key là contract

Cache chỉ đúng khi key thay đổi khi content semantic thay đổi.

Nếu `common.js` content đổi nhưng URL/cache key không đổi và TTL dài, browser có thể chạy code cũ.

Pattern phổ biến:

```text
resource URL + version/postfix/hash
```

SP5 có engine cache/postfix configuration và các build mới hỗ trợ mapping postfix theo file. Exact option phải kiểm tra release note/build.

## 15. Postfix per resource

Release note SP5 hiện đại mô tả khả năng cấu hình postfix khác nhau theo file. Mental model:

```text
artifact A hash/version → URL A?v=A1
artifact B hash/version → URL B?v=B7
```

Điều này giảm invalidation toàn bộ khi chỉ một resource đổi, nhưng tăng yêu cầu build manifest/provenance rõ.

## 16. `config.js` cũng có cache identity

Nếu runtime configuration được materialize thành JS/config resource, chính config cũng có thể bị cache.

Symptom:

```text
server config đã deploy
browser vẫn dùng config cũ
```

Do đó verify Network response/runtime value, không chỉ file trên server.

## 17. Component cache và reusable resource

Một số SP5 release thay đổi cách UDC/TTC/EXC hoặc common resource được cache trong engine runtime. Đây là lý do không dựa vào private cache internals như public contract.

Nếu behavior đổi sau engine upgrade, kiểm tra release note trước khi workaround bằng global reset/hack.

## 18. Public API vs observed internal API

DevTools có thể cho thấy nhiều property/function không có trong official API reference.

Không dùng chúng chỉ vì “chạy được”. Official performance guide cũng cảnh báo API không công khai có thể thay đổi và gây khó debug sau upgrade.

Rule:

```text
official public API
> documented configuration
> project abstraction
> observed private internals
```

Private internal chỉ nên dùng khi vendor support xác nhận và có compatibility plan.

## 19. Evergreen browser làm runtime tiếp tục thay đổi

Ngay cả khi WebSquare build không đổi, Chrome/Edge/Safari/Firefox có thể tự update.

Browser change có thể ảnh hưởng:

```text
layout
focus
clipboard
download
cookie policy
CORS/security
WebView behavior
performance scheduling
```

Vì vậy compatibility matrix phải có browser dimension.

## 20. Upgrade là dependency migration

Engine upgrade không chỉ là copy engine folder.

Phải inventory:

```text
public APIs used
version-sensitive properties
legacy `$w`/Scope behavior
private APIs/hacks
Grid event assumptions
WFrame lifecycle assumptions
upload/download config
W-Pack config
hybrid bridge
browser support
```

Sau đó map release note vào dependency thực của project.

## 21. Release note phải đọc theo impact, không theo số lượng feature

Một release note 200 item không cần test 200 item như nhau.

Classify:

```text
DIRECT — project dùng feature đó
TRANSITIVE — engine/component internal thay đổi có thể ảnh hưởng
SECURITY — phải review dù chưa thấy usage
IRRELEVANT — project không có boundary đó
```

Regression priority dựa trên impact.

## 22. Compatibility matrix

Ví dụ:

| Layer | Current | Target | Risk |
|---|---|---|---|
| WebSquare Engine | SP5 build A | SP5 build B | event/cache behavior |
| W-Pack | tool A | tool B | generated artifact |
| Browser | Chrome N | N+1 | focus/download |
| Hybrid native | app 4.2 | app 4.3 | bridge capability |
| Backend API | v3 | v3/v4 compat | schema |
| Common UDC | 7 | 8 | public contract |

Matrix buộc team nhìn upgrade như system change.

## 23. Canary/smoke trước full rollout

Nếu hạ tầng cho phép, engine/artifact upgrade nên có smoke/canary evidence trước full rollout.

Critical flow:

```text
login
shell load
Search
Grid edit
Save
popup/WFrame
Excel/file
logout
hybrid capability nếu có
```

Không chỉ mở homepage rồi kết luận pass.

## 24. Cache rollout và backward compatibility

Trong rollout, browser cũ có thể giữ artifact cũ trong khi server mới đã deploy.

Do đó API/config/resource contract phải chịu được overlap hoặc có strategy force reload/version gate rõ.

Không giả định deploy là atomic đối với mọi browser.

## 25. Build identity phải visible

Support nên có cách lấy ít nhất:

```text
application build/version
W-Pack/source commit identity
WebSquare engine build
config/environment identity
```

Có thể expose qua diagnostics screen/log header tùy security policy.

Không bắt support hỏi user “anh đã clear cache chưa?” như bước đầu tiên.

## 26. Runtime manifest

Một project mature có thể tạo runtime manifest:

```json
{
  "appBuild": "2026.09.22.3",
  "gitCommit": "abc123",
  "websquareEngine": "5.0_5.xxxx",
  "wpackBuild": "...",
  "configVersion": "prod-42"
}
```

Đây là project pattern, không phải built-in WebSquare format.

Mục tiêu là provenance.

## 27. Diagnostic page

Một internal diagnostics screen có thể hiển thị non-secret metadata:

```text
screen instance
engine/build
app artifact
config version
API base logical name
browser version
locale
hybrid capability version
```

Không hiển thị token/session secret.

## 28. Performance config và cache

Official performance guide nhấn mạnh gzip/compression, static resource caching, keep-alive và WebSquare engine/cache configuration.

Nhưng performance tuning phải đo:

```text
transfer size
cache hit/miss
TTFB
parse/execute
render
```

Bật cache không sửa formatter O(n²).

## 29. `engineCache` không phải business cache

Engine/resource cache tối ưu resource loading. Nó không thay cache cho business data.

Không dùng cùng từ “cache” rồi trộn:

```text
engine resource cache
browser HTTP cache
code-list cache
business entity cache
```

Mỗi cache có owner/invalidation khác nhau.

## 30. Config precedence

Khi một behavior có thể cấu hình ở component, project config hoặc default, phải biết precedence đúng build.

Ví dụ escape/accessibility/render setting có thể có nhiều level. Không suy luận từ một project khác.

Khi debug:

```text
inspect component explicit value
→ project/runtime config
→ engine default/build behavior
```

## 31. Environment drift

Hai environment có cùng WAR/source nhưng khác:

```text
engine build
config
proxy
headers
JVM/server setting
cache
API endpoint
```

thì chúng không phải cùng runtime system.

Diff environment phải bao gồm những layer này.

## 32. Production incident: source mới, UI cũ

Evidence chain:

```text
Git commit correct
→ artifact built?
→ artifact deployed?
→ URL resolves artifact nào?
→ response cache headers?
→ browser received content/hash nào?
→ engine loaded artifact nào?
```

Không dừng ở “GitHub đã có code”.

## 33. Production incident: chỉ một user lỗi

Khả năng:

```text
stale browser cache
old tab/runtime
browser extension
browser version
local storage/state
hybrid app version
```

So sánh runtime identity giữa user lỗi và user bình thường trước khi rollback server.

## 34. Production incident: chỉ PROD lỗi

So sánh:

```text
engine build
client config
server config
W-Pack artifact hash
context root
proxy/cache headers
API route
browser policy
```

Nếu UAT và PROD source giống nhau nhưng runtime inputs khác, source diff không giúp nhiều.

## 35. Production incident: engine upgrade làm Grid khác behavior

Flow:

```text
capture old/new event trace
→ identify exact build diff
→ search release note/API change
→ reproduce minimal screen
→ remove hidden assumption hoặc set explicit supported config
→ add regression
```

Không pin engine cũ vô thời hạn chỉ vì chưa hiểu root cause.

## 36. Rollback phải rollback đúng layer

Nếu issue nằm ở config, rollback app artifact có thể không giúp. Nếu issue nằm ở engine, rollback business code có thể che symptom nhưng không sửa dependency.

Runbook phải biết rollback unit:

```text
application artifact
config
engine build
common resource
backend API
hybrid native release
```

## 37. Security patch và compatibility

Security release có thể thay behavior tưởng như unrelated, ví dụ logging, upload, IFrame, sanitization hoặc private API.

Không bỏ security patch chỉ vì regression test fail. Cần xác định dependency sai/hack nào bị lộ và migrate sang supported contract.

## 38. Reproducible build

Cùng source/config/tool version nên tạo artifact có thể xác định được.

Nếu build phụ thuộc file local không versioned hoặc Studio manual state, provenance yếu.

W-Pack command-line/CI workflow có giá trị vì giảm hidden workstation state.

## 39. Branch/release hygiene cho Knowledge Library này

Khi ghi tài liệu WebSquare:

```text
mental model ổn định → canonical chapter
exact API/property → note build-dependent
release-specific change → cite official release note
project workaround → project runbook, không canonicalize mù
```

Library không nên trở thành bản copy release note.

## 40. Master runtime equation

Một cách reasoning hữu ích:

```text
Observed Behavior
= f(
  Source,
  Generated Artifact,
  Engine Build,
  Client Config,
  Server Config,
  Resource Version,
  Browser Runtime,
  Backend Contract,
  Persistent Client State
)
```

Nếu chỉ kiểm tra `Source`, bạn mới kiểm tra một biến.

## 41. Upgrade test matrix

Ít nhất test:

```text
cold cache
warm cache
old tab → deploy → action
new tab after deploy
nested WFrame
lazy tab/preload
Grid edit/save
file/Excel
session expiry
browser current/current-1 theo support policy
hybrid app old/new capability nếu có
```

## 42. Connection map

Runtime/page: [01 — Platform, Runtime & Page Model](01_platform_runtime_page_model.md).

Migration: [07 — Legacy, Modern Evolution & Migration](07_legacy_modern_migration.md).

Resource lifetime: [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

Regression engineering: [11 — Testing, Testability & Regression](11_testing_testability_regression.md).

Build/deploy foundation: [12 — Build, Configuration & Deployment](12_build_config_deployment.md).

Hybrid version skew: [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md).

Observability: [19 — Observability, Logging & Incident Response](19_observability_incident_response.md).

Integration/client version skew: [21 — Integration Topology, MSA, Real-Time & Resilience](21_integration_topology_msa_realtime_resilience.md).

## 43. Master synthesis: 20–22 nối vào toàn library như thế nào

Ba chapter mới bổ sung ba graph mà một WebSquare Master phải giữ cùng lúc:

```text
Security graph
principal → auth → session → permission → protected command

Integration graph
screen → Submission → gateway/BFF/service → event/result

Runtime provenance graph
source → W-Pack → engine/config → cache → browser
```

Ba graph này giao nhau trong incident thực.

Ví dụ user bấm Save sau khi laptop sleep:

```text
Security graph: session đã expire
Integration graph: request đi qua gateway, có thể timeout/retry
Runtime graph: browser tab vẫn giữ page/artifact cũ
```

Nếu chỉ nhìn một graph, fix dễ sai.

## 44. Capstone Master mở rộng

Nâng mini enterprise app của chapter 16 bằng các fault injection:

```text
session expire khi Save
permission bị revoke khi tab đang mở
logout user A → login user B không reload browser
API Gateway timeout sau downstream commit
polling overlap sau browser resume
real-time duplicate/out-of-order event
browser giữ W-Pack cũ sau deploy
engine build UAT/PROD khác nhau
config.js stale trong một browser
hybrid app version cũ gọi web build mới
```

Với mỗi case phải trả lời:

```text
invariant nào bị đe dọa?
owner ở layer nào?
identity nào cần log?
operation có thể retry không?
state nào phải invalidate?
evidence nào chứng minh root cause?
regression test nào ngăn tái diễn?
```

## 45. Kết luận

WebSquare Master không coi engine/config/cache là “phần DevOps bên ngoài code”. Chúng là input trực tiếp của runtime behavior.

Khi có incident, câu hỏi đúng không phải chỉ là “code nào chạy?”, mà là:

**source nào → được build thành artifact nào → bằng tool/config nào → chạy trên engine build nào → được resolve/cache thành resource nào → trong browser/session/security state nào → gọi contract qua topology nào**.

Đó là mức reasoning giúp phân biệt một workaround tạm thời với một root-cause fix.