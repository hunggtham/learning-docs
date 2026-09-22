# Technical debt economics, engineering metrics và Goodhart's Law

Đọc trước [Architecture decisions, evolution và socio-technical constraints](./00_architecture_decisions_evolution_and_socio_technical_constraints.md) và [Large-scale refactoring, strangler và branch-by-abstraction](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md). Chapter này tập trung vào một câu hỏi khó hơn “code có sạch không?”: **khi nào một constraint kiến trúc/kỹ thuật thực sự trở thành debt, debt tạo chi phí qua mỗi thay đổi như thế nào, và làm sao dùng metrics để ra quyết định mà không biến metric thành mục tiêu bị game?**

Mental model:

```text
past decision / shortcut / obsolete assumption
→ constraint on current change
→ recurring friction / risk / delay
→ economic impact
→ evidence
→ paydown / contain / accept decision
```

## 1. Technical debt không đồng nghĩa code xấu

Một đoạn code xấu nhưng không bao giờ thay đổi có thể gần như không tạo “interest”. Một dependency boundary nhìn khá sạch nhưng buộc 12 teams coordination cho mỗi release có thể tạo debt rất lớn.

Debt nên được nhận diện qua **future change cost và risk**, không chỉ aesthetic.

Một definition thực dụng:

> Technical debt là một design/implementation/operational constraint làm chi phí hoặc rủi ro của các thay đổi tương lai cao hơn đáng kể so với một trạng thái thay thế hợp lý.

## 2. Debt metaphor hữu ích nhưng không phải accounting literal

Financial debt có principal, interest rate và contract rõ. Technical debt không có con số khách quan như vậy.

Ta vẫn có thể dùng metaphor:

```text
principal ≈ cost để thay đổi cấu trúc hiện tại
interest ≈ recurring extra cost vì chưa thay đổi
```

Nhưng estimate có uncertainty lớn. Đừng giả vờ “debt = 327 engineer-hours” là fact nếu chưa có evidence.

## 3. Deliberate debt và accidental debt có governance khác nhau

Deliberate debt có thể là quyết định hợp lý: ship MVP nhanh, chấp nhận manual migration vì deadline, dùng monolith khi team nhỏ.

Accidental debt xuất hiện từ misunderstanding, uncontrolled coupling hoặc drift.

Quan trọng hơn origin là **assumption còn đúng không**. Một shortcut có thể hợp lý năm đầu nhưng trở thành bottleneck khi scale/team/regulation thay đổi.

## 4. Obsolescence debt đến từ môi trường thay đổi

Code có thể không đổi nhưng platform/runtime/library hết support, security baseline thay đổi hoặc business model đổi.

Đây là debt do external evolution. “Không ai làm gì sai” không làm cost biến mất.

Version evolution chapter ở language/framework nên được nối với maintenance economics thay vì xem upgrade là housekeeping vô nghĩa.

## 5. Change amplification là một signal mạnh

Một yêu cầu business nhỏ nhưng buộc sửa 20 modules, 8 repositories và 5 teams cho thấy coupling/change amplification.

Có thể reasoning:

```text
business change size
→ number of technical boundaries touched
→ coordination + test + deploy surface
→ lead time + defect risk
```

Không cần một score universal; trend và repeated examples thường đủ để chứng minh debt.

## 6. Coordination debt là technical debt ở socio-technical layer

Nếu architecture boundary không khớp ownership, mọi thay đổi cross-service cần meetings, synchronized release và shared incident handling.

Conway-style effect nghĩa team topology và system topology tác động lẫn nhau. Refactor code không giải được nếu ownership model vẫn giữ same coordination bottleneck.

## 7. Data/schema debt thường có irreversibility cao

Duplicate source of truth, overloaded column semantics, missing provenance hoặc schema không hỗ trợ evolution có thể buộc migration dài.

Data debt khác code debt vì old data tồn tại lâu và rollback khó. Paydown thường cần expand-contract, backfill, shadow read, dual-read/dual-write caution và validation.

Đọc [API/schema compatibility](./02_api_schema_compatibility_and_evolutionary_design.md) và [large-scale migration](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md).

## 8. Test debt là thiếu confidence, không chỉ thiếu coverage %

Coverage 85% không chứng minh critical invariants được test. Test suite chậm/flaky có thể làm engineers bỏ chạy tests, tăng change risk.

Test debt nên nhìn:

```text
khả năng phát hiện regression quan trọng
feedback latency
flakiness
production representativeness
failure-model coverage
```

Coverage line chỉ là một observation phụ.

## 9. Operational debt xuất hiện khi system chỉ chạy được nhờ heroics

Manual restart, tribal runbook, alert noise, undocumented failover hoặc deployment cần “người A nhớ bước bí mật” đều là debt.

Interest biểu hiện qua on-call load, incident duration và cognitive load. Automation có thể trả debt, nhưng automation không hiểu invariant có thể chỉ đóng gói failure nhanh hơn.

## 10. Debt interest có thể đo qua recurring friction

Các signal thực tế gồm repeated incident class, lead time do coordination, migration overhead, flaky-test retries, manual toil, dependency upgrade blocks, high change-failure rate ở một subsystem và on-call pages.

Không signal nào một mình là debt score. Chúng là evidence để hỏi constraint nào gây friction.

## 11. Một debt item cần owner, trigger và exit condition

Backlog “refactor someday” gần như không có governance. Một debt record hữu ích nên mô tả:

```text
constraint hiện tại
business/engineering impact
assumption
interest evidence
risk nếu để nguyên
option paydown
trigger khi nào phải làm
success / exit condition
```

Trigger có thể là traffic threshold, number of teams, next regulation deadline hoặc repeated incident count.

## 12. Paydown timing là option-value decision

Refactor quá sớm có thể lãng phí nếu product direction đổi. Quá muộn có thể làm migration đắt hơn theo số consumers/data.

Có thể reasoning bằng expected value:

```text
cost of paydown now
vs
expected future interest + risk + migration growth
```

Uncertainty khiến “wait for information” có option value, nhưng chỉ khi system giữ reversibility đủ lâu.

## 13. Reversibility là tài sản kiến trúc

Feature flags, abstraction seams, compatible schemas và modular boundaries làm future change rẻ hơn. Chúng mua option value.

Một architecture không tối ưu throughput hôm nay nhưng dễ thay đổi có thể có economic value lớn trong domain bất định.

Architecture decision nên ghi assumption và rollback/migration path, không chỉ rationale hiện tại.

## 14. Interest có thể compound qua coupling

Nếu workaround A tạo dependency B, rồi B buộc workaround C, cost tăng phi tuyến.

Ví dụ shared database ban đầu giúp ship nhanh; sau đó nhiều services truy cập trực tiếp; schema change cần coordinate tất cả; team tạo views/flags; monitoring khó. Debt không còn là một shortcut mà thành network constraints.

Đây là lý do early containment boundary đôi khi đáng giá hơn “đại refactor” sau này.

## 15. Không phải debt nào cũng nên trả

Legacy system sẽ retire trong 3 tháng có thể không đáng rewrite. Debt ở low-change module có interest thấp. Một risky refactor có thể tệ hơn current state.

Options gồm:

```text
pay down
contain / isolate
instrument
accept explicitly
replace later
retire
```

Senior decision là economic trade-off, không phải moral judgment về code quality.

## 16. Metrics là sensors, không phải objective function mặc định

Lead time, deployment frequency, test coverage, incidents, CPU cost hay story points đều đo một projection của system.

Khi metric trở thành target cứng, behavior thích nghi để tối ưu metric có thể phá mục tiêu thật. Đây là Goodhart's Law ở dạng thực dụng:

> Khi một measure trở thành target, nó có xu hướng mất chất lượng như một measure.

## 17. Goodhart xuất hiện vì proxy khác objective

Nếu target là “deploy 20 lần/ngày”, team có thể chia change vô nghĩa. Nếu target là “coverage 90%”, tests có thể tăng line coverage nhưng không test invariant. Nếu target là “close tickets nhanh”, tickets có thể bị split/close sớm.

Problem không phải metric xấu; problem là **proxy bị dùng như objective duy nhất**.

## 18. Metric governance cần một metric tree

Bắt đầu từ outcome:

```text
customer/business outcome
→ reliability/security/correctness constraint
→ delivery capability
→ system/process signals
```

Ví dụ “giảm lead time” phải giữ change-failure/SLO guardrail. “Giảm cloud cost” phải giữ latency/error/security guardrail.

Metric tree làm rõ trade-off thay vì tối ưu single number.

## 19. Leading và lagging indicators có vai trò khác nhau

Incident rate là lagging indicator: biết sau khi failure xảy ra. Test signal, rollout anomaly hoặc complexity hotspot có thể leading nhưng nhiều false positives hơn.

Một governance tốt kết hợp cả hai. Không đòi leading indicator “dự đoán hoàn hảo”.

## 20. DORA-style metrics là diagnostic signals, không phải team leaderboard

Deployment frequency, lead time, change failure và recovery time có thể hữu ích để thấy flow/reliability trend.

Nhưng so trực tiếp teams có product/risk/regulatory context khác nhau có thể sai. Team infrastructure có unit of deployment khác mobile app team.

Dùng metrics để tìm constraint và trend nội bộ tốt hơn dùng để xếp hạng con người.

## 21. Local optimization có thể làm global system tệ hơn

Team A giảm lead time bằng cách đẩy validation sang downstream team B. Metric A đẹp hơn nhưng end-to-end delivery không nhanh hơn.

Do đó boundary của metric phải khớp boundary của outcome. Nếu objective là customer change lead time, đo chỉ một pipeline stage dễ bị game.

## 22. Engineering productivity không thể nén thành LOC/commit count

Lines of code có thể tăng khi design tệ hơn; xóa code có thể tạo nhiều value. Commit count phụ thuộc style. PR count dễ split.

Productivity nên reasoning từ useful outcomes, quality, maintainability và flow constraints; quantitative metrics cần qualitative context.

## 23. Incident learning là feedback cho debt portfolio

Nếu incident postmortem lặp lại cùng dependency bottleneck hoặc manual failover, đó là evidence debt interest đang được trả bằng downtime/on-call effort.

Debt prioritization nên tăng khi recurrence chứng minh expected loss cao hơn estimate cũ.

Incident không chỉ tạo action item “fix bug”; nó cập nhật economic model của architecture.

## 24. Worked example: shared database giữa nhiều services

Ban đầu ba services dùng chung schema để ship nhanh. Sau hai năm có 15 services. Một column rename cần months coordination; tests khó isolate; schema deploy có blast radius lớn.

Debt evidence:

```text
small schema changes → many teams touched
release coordination ↑
rollback complexity ↑
incidents from hidden consumers ↑
```

Paydown không nhất thiết “microservices rewrite”. Có thể tạo ownership boundary, API/read model, compatibility layer và migrate consumers dần bằng branch-by-abstraction.

Success metric là giảm change amplification và blast radius, không phải số services.

## 25. Worked example: test coverage target bị game

Management đặt 90% coverage làm KPI. Team viết tests gọi getters/setters, mock mọi dependency và tránh refactor vì snapshot tests fragile. Coverage tăng nhưng production regressions không giảm.

Correction không phải bỏ metrics hoàn toàn. Chuyển focus sang critical invariant coverage, mutation/property/contract tests ở risk areas, test feedback time và escaped defect classes.

Metric trở lại vai trò sensor.

## 26. Một decision framework thực dụng

Khi cân debt item, hỏi:

```text
Interest evidence có lặp lại không?
Blast radius/risk là gì?
Constraint có chặn roadmap gần không?
Paydown cost và migration risk bao nhiêu?
Có containment rẻ hơn không?
Delay có làm migration khó hơn không?
Assumption nào có thể thay đổi?
Success đo bằng outcome nào?
```

Không cần score giả chính xác. Mục tiêu là làm assumptions explicit để review lại theo thời gian.

## 27. Kết nối sang các chapter khác

Technical-debt economics nối với [architecture evolution](./00_architecture_decisions_evolution_and_socio_technical_constraints.md), [boundary economics](./01_modular_monolith_vs_services_boundary_economics.md), [large-scale refactoring](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md), [test architecture](./04_test_architecture_contract_mutation_property_and_production_verification.md) và [deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md).

Mental model cuối cùng: **technical debt là portfolio của future constraints. Metrics chỉ giúp thấy interest/risk khi chúng vẫn là sensors; khi biến thành target tuyệt đối, chính metric có thể tạo debt mới.**