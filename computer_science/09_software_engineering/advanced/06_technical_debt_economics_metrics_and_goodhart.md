# Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Technical debt không đồng nghĩa mã (code / 코드) xấu** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Debt metaphor hữu ích nhưng không phải accounting literal** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Đọc trước [Architecture decisions, evolution và socio-technical constraints](./00_architecture_decisions_evolution_and_socio_technical_constraints.md) và [Large-scale refactoring, strangler và branch-by-abstraction](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md). Chapter này tập trung vào một câu hỏi khó hơn “mã (code / 코드) có sạch không?”: **khi nào một ràng buộc (constraint / 제약조건) kiến trúc/kỹ thuật thực sự trở thành debt, debt tạo chi phí qua mỗi thay đổi như thế nào, và làm sao dùng metrics để ra quyết định mà không biến chỉ số (metric / 지표) thành mục tiêu bị game?**

Mô hình tư duy (mental model / 사고 모델):

```text
past decision / shortcut / obsolete assumption
→ constraint on current change
→ recurring friction / risk / delay
→ economic impact
→ evidence
→ paydown / contain / accept decision
```

## 1. Technical debt không đồng nghĩa mã (code / 코드) xấu

Một đoạn mã (code / 코드) xấu nhưng không bao giờ thay đổi có thể gần như không tạo “interest”. Một phụ thuộc (dependency / 의존성) ranh giới (boundary / 경계) nhìn khá sạch nhưng buộc 12 teams coordination cho mỗi bản phát hành (release / 릴리스) có thể tạo debt rất lớn.

Debt nên được nhận diện qua **future thay đổi (change / 변경) chi phí (cost / 비용) và rủi ro (risk / 위험)**, không chỉ aesthetic.

Một definition thực dụng:

> Technical debt là một thiết kế (design / 설계)/hiện thực (implementation / 구현)/operational ràng buộc (constraint / 제약조건) làm chi phí hoặc rủi ro của các thay đổi tương lai cao hơn đáng kể so với một trạng thái thay thế hợp lý.

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **2. Debt metaphor hữu ích nhưng không phải accounting literal** tiếp nhận điểm tựa từ **1. Technical debt không đồng nghĩa mã (code / 코드) xấu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Deliberate debt và accidental debt có quản trị (governance / 거버넌스) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Debt metaphor hữu ích nhưng không phải accounting literal

Financial debt có principal, interest tỷ lệ (rate / 비율) và đặc tả hợp đồng (contract / 계약) rõ. Technical debt không có con số khách quan như vậy.

Ta vẫn có thể dùng metaphor:

```text
principal ≈ cost để thay đổi cấu trúc hiện tại
interest ≈ recurring extra cost vì chưa thay đổi
```

Nhưng estimate có bất định (uncertainty / 불확실성) lớn. Đừng giả vờ “debt = 327 engineer-hours” là fact nếu chưa có bằng chứng (evidence / 증거).

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **3. Deliberate debt và accidental debt có quản trị (governance / 거버넌스) khác nhau** tiếp nhận điểm tựa từ **2. Debt metaphor hữu ích nhưng không phải accounting literal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Obsolescence debt đến từ môi trường thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Deliberate debt và accidental debt có quản trị (governance / 거버넌스) khác nhau

Deliberate debt có thể là quyết định hợp lý: ship MVP nhanh, chấp nhận manual di chuyển (migration / 마이그레이션) vì deadline, dùng monolith khi nhóm (team / 팀) nhỏ.

Accidental debt xuất hiện từ misunderstanding, uncontrolled coupling hoặc drift.

Quan trọng hơn origin là **giả định (assumption / 가정) còn đúng không**. Một shortcut có thể hợp lý năm đầu nhưng trở thành bottleneck khi quy mô (scale / 규모)/nhóm (team / 팀)/regulation thay đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **4. Obsolescence debt đến từ môi trường thay đổi** tiếp nhận điểm tựa từ **3. Deliberate debt và accidental debt có quản trị (governance / 거버넌스) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. thay đổi (change / 변경) amplification là một tín hiệu (signal / 신호) mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Obsolescence debt đến từ môi trường thay đổi

Mã (code / 코드) có thể không đổi nhưng nền tảng (platform / 플랫폼)/thời gian chạy (runtime / 런타임)/thư viện (library / 라이브러리) hết hỗ trợ (support / 지원), bảo mật (security / 보안) baseline thay đổi hoặc nghiệp vụ (business / 비즈니스) mô hình (model / 모델) đổi.

Đây là debt do bên ngoài (external / 외부) evolution. “Không ai làm gì sai” không làm chi phí (cost / 비용) biến mất.

Phiên bản (version / 버전) evolution chapter ở ngôn ngữ (language / 언어)/khung phần mềm (framework / 프레임워크) nên được nối với maintenance economics thay vì xem upgrade là housekeeping vô nghĩa.

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **5. thay đổi (change / 변경) amplification là một tín hiệu (signal / 신호) mạnh** tiếp nhận điểm tựa từ **4. Obsolescence debt đến từ môi trường thay đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Coordination debt là technical debt ở socio-technical tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. thay đổi (change / 변경) amplification là một tín hiệu (signal / 신호) mạnh

Một yêu cầu nghiệp vụ (business / 비즈니스) nhỏ nhưng buộc sửa 20 modules, 8 repositories và 5 teams cho thấy coupling/thay đổi (change / 변경) amplification.

Có thể lập luận (reasoning / 추론):

```text
business change size
→ number of technical boundaries touched
→ coordination + test + deploy surface
→ lead time + defect risk
```

Không cần một score universal; trend và repeated examples thường đủ để chứng minh debt.

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **6. Coordination debt là technical debt ở socio-technical tầng (layer / 계층)** tiếp nhận điểm tựa từ **5. thay đổi (change / 변경) amplification là một tín hiệu (signal / 신호) mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. dữ liệu (data / 데이터)/lược đồ (schema / 스키마) debt thường có irreversibility cao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Coordination debt là technical debt ở socio-technical tầng (layer / 계층)

Nếu kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계) không khớp quyền sở hữu (ownership / 소유권), mọi thay đổi cross-service cần meetings, synchronized bản phát hành (release / 릴리스) và dùng chung (shared / 공유) sự cố (incident / 인시던트) handling.

Conway-style tác động (effect / 효과) nghĩa nhóm (team / 팀) topology và hệ thống (system / 시스템) topology tác động lẫn nhau. Refactor mã (code / 코드) không giải được nếu quyền sở hữu (ownership / 소유권) mô hình (model / 모델) vẫn giữ same coordination bottleneck.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **6. Coordination debt là technical debt ở socio-technical tầng (layer / 계층)** nêu điều cần giải thích; **7. dữ liệu (data / 데이터)/lược đồ (schema / 스키마) debt thường có irreversibility cao** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. kiểm thử (test / 테스트) debt là thiếu confidence, không chỉ thiếu coverage %** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. dữ liệu (data / 데이터)/lược đồ (schema / 스키마) debt thường có irreversibility cao

Duplicate nguồn chuẩn (source of truth / 정본), overloaded column ngữ nghĩa (semantics / 의미론), missing provenance hoặc lược đồ (schema / 스키마) không hỗ trợ evolution có thể buộc di chuyển (migration / 마이그레이션) dài.

Dữ liệu (data / 데이터) debt khác mã (code / 코드) debt vì old dữ liệu (data / 데이터) tồn tại lâu và quay lui (rollback / 롤백) khó. Paydown thường cần expand-contract, backfill, shadow read, dual-read/dual-write caution và kiểm tra hợp lệ (validation / 검증).

Đọc [API/schema compatibility](./02_api_schema_compatibility_and_evolutionary_design.md) và [large-scale migration](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md).

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **7. dữ liệu (data / 데이터)/lược đồ (schema / 스키마) debt thường có irreversibility cao** nêu điều cần giải thích; **8. kiểm thử (test / 테스트) debt là thiếu confidence, không chỉ thiếu coverage %** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Operational debt xuất hiện khi hệ thống (system / 시스템) chỉ chạy được nhờ heroics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. kiểm thử (test / 테스트) debt là thiếu confidence, không chỉ thiếu coverage %

Coverage 85% không chứng minh trọng yếu (critical / 중요) invariants được kiểm thử (test / 테스트). bộ kiểm thử (test suite / 테스트 스위트) chậm/flaky có thể làm engineers bỏ chạy tests, tăng thay đổi (change / 변경) rủi ro (risk / 위험).

Kiểm thử (test / 테스트) debt nên nhìn:

```text
khả năng phát hiện regression quan trọng
feedback latency
flakiness
production representativeness
failure-model coverage
```

Coverage line chỉ là một observation phụ.

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **9. Operational debt xuất hiện khi hệ thống (system / 시스템) chỉ chạy được nhờ heroics** tiếp nhận điểm tựa từ **8. kiểm thử (test / 테스트) debt là thiếu confidence, không chỉ thiếu coverage %** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Debt interest có thể đo qua recurring friction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Operational debt xuất hiện khi hệ thống (system / 시스템) chỉ chạy được nhờ heroics

Manual restart, tribal runbook, alert noise, undocumented failover hoặc triển khai (deployment / 배포) cần “người A nhớ bước bí mật” đều là debt.

Interest biểu hiện qua on-call tải (load / 로드), sự cố (incident / 인시던트) duration và cognitive tải (load / 로드). Automation có thể trả debt, nhưng automation không hiểu bất biến (invariant / 불변식) có thể chỉ đóng gói thất bại (failure / 실패) nhanh hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **10. Debt interest có thể đo qua recurring friction** tiếp nhận điểm tựa từ **9. Operational debt xuất hiện khi hệ thống (system / 시스템) chỉ chạy được nhờ heroics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Một debt item cần đơn vị sở hữu (owner / 오너), trigger và exit điều kiện (condition / 조건)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Debt interest có thể đo qua recurring friction

Các tín hiệu (signal / 신호) thực tế gồm repeated sự cố (incident / 인시던트) lớp (class / 클래스), lead thời gian (time / 시간) do coordination, di chuyển (migration / 마이그레이션) overhead, flaky-test retries, manual toil, phụ thuộc (dependency / 의존성) upgrade blocks, high change-failure tỷ lệ (rate / 비율) ở một subsystem và on-call pages.

Không tín hiệu (signal / 신호) nào một mình là debt score. Chúng là bằng chứng (evidence / 증거) để hỏi ràng buộc (constraint / 제약조건) nào gây friction.

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **11. Một debt item cần đơn vị sở hữu (owner / 오너), trigger và exit điều kiện (condition / 조건)** tiếp nhận điểm tựa từ **10. Debt interest có thể đo qua recurring friction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Paydown timing là option-value quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Một debt item cần đơn vị sở hữu (owner / 오너), trigger và exit điều kiện (condition / 조건)

Backlog “refactor someday” gần như không có quản trị (governance / 거버넌스). Một debt bản ghi (record / 레코드) hữu ích nên mô tả:

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

Trigger có thể là traffic threshold, number of teams, next regulation deadline hoặc repeated sự cố (incident / 인시던트) count.

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **12. Paydown timing là option-value quyết định (decision / 결정)** tiếp nhận điểm tựa từ **11. Một debt item cần đơn vị sở hữu (owner / 오너), trigger và exit điều kiện (condition / 조건)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Reversibility là tài sản kiến trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Paydown timing là option-value quyết định (decision / 결정)

Refactor quá sớm có thể lãng phí nếu sản phẩm (product / 제품) direction đổi. Quá muộn có thể làm di chuyển (migration / 마이그레이션) đắt hơn theo số consumers/dữ liệu (data / 데이터).

Có thể lập luận (reasoning / 추론) bằng expected giá trị (value / 값):

```text
cost of paydown now
vs
expected future interest + risk + migration growth
```

Bất định (uncertainty / 불확실성) khiến “wait for thông tin (information / 정보)” có option giá trị (value / 값), nhưng chỉ khi hệ thống (system / 시스템) giữ reversibility đủ lâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **13. Reversibility là tài sản kiến trúc** tiếp nhận điểm tựa từ **12. Paydown timing là option-value quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Interest có thể compound qua coupling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Reversibility là tài sản kiến trúc

Tính năng (feature / 기능) flags, lớp trừu tượng (abstraction / 추상화) seams, compatible schemas và modular boundaries làm future thay đổi (change / 변경) rẻ hơn. Chúng mua option giá trị (value / 값).

Một kiến trúc (architecture / 아키텍처) không tối ưu thông lượng (throughput / 처리량) hôm nay nhưng dễ thay đổi có thể có economic giá trị (value / 값) lớn trong lĩnh vực (domain / 도메인) bất định.

Kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) nên ghi giả định (assumption / 가정) và quay lui (rollback / 롤백)/di chuyển (migration / 마이그레이션) đường dẫn (path / 경로), không chỉ rationale hiện tại.

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **14. Interest có thể compound qua coupling** tiếp nhận điểm tựa từ **13. Reversibility là tài sản kiến trúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Không phải debt nào cũng nên trả** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Interest có thể compound qua coupling

Nếu workaround A tạo phụ thuộc (dependency / 의존성) B, rồi B buộc workaround C, chi phí (cost / 비용) tăng phi tuyến.

Ví dụ dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) ban đầu giúp ship nhanh; sau đó nhiều services truy cập trực tiếp; lược đồ (schema / 스키마) thay đổi (change / 변경) cần coordinate tất cả; nhóm (team / 팀) tạo views/flags; monitoring khó. Debt không còn là một shortcut mà thành mạng (network / 네트워크) các ràng buộc (constraints / 제약조건들).

Đây là lý do early containment ranh giới (boundary / 경계) đôi khi đáng giá hơn “đại refactor” sau này.

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **15. Không phải debt nào cũng nên trả** tiếp nhận điểm tựa từ **14. Interest có thể compound qua coupling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Metrics là sensors, không phải mục tiêu (objective / 목표) hàm (function / 함수) mặc định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Không phải debt nào cũng nên trả

Legacy hệ thống (system / 시스템) sẽ retire trong 3 tháng có thể không đáng rewrite. Debt ở low-change mô-đun (module / 모듈) có interest thấp. Một risky refactor có thể tệ hơn trạng thái hiện tại (current state / 현재 상태).

Options gồm:

```text
pay down
contain / isolate
instrument
accept explicitly
replace later
retire
```

Cấp cao (senior / 시니어) quyết định (decision / 결정) là economic sự đánh đổi (trade-off / 트레이드오프), không phải moral judgment về mã (code / 코드) chất lượng (quality / 품질).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **16. Metrics là sensors, không phải mục tiêu (objective / 목표) hàm (function / 함수) mặc định** tiếp nhận điểm tựa từ **15. Không phải debt nào cũng nên trả** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Goodhart xuất hiện vì proxy khác mục tiêu (objective / 목표)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Metrics là sensors, không phải mục tiêu (objective / 목표) hàm (function / 함수) mặc định

Lead thời gian (time / 시간), triển khai (deployment / 배포) frequency, kiểm thử (test / 테스트) coverage, incidents, CPU chi phí (cost / 비용) hay story points đều đo một projection của hệ thống (system / 시스템).

Khi chỉ số (metric / 지표) trở thành mục tiêu (target / 대상) cứng, hành vi (behavior / 동작) thích nghi để tối ưu chỉ số (metric / 지표) có thể phá mục tiêu thật. Đây là Goodhart's Law ở dạng thực dụng:

> Khi một measure trở thành mục tiêu (target / 대상), nó có xu hướng mất chất lượng như một measure.

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **17. Goodhart xuất hiện vì proxy khác mục tiêu (objective / 목표)** tiếp nhận điểm tựa từ **16. Metrics là sensors, không phải mục tiêu (objective / 목표) hàm (function / 함수) mặc định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. chỉ số (metric / 지표) quản trị (governance / 거버넌스) cần một chỉ số (metric / 지표) cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Goodhart xuất hiện vì proxy khác mục tiêu (objective / 목표)

Nếu mục tiêu (target / 대상) là “deploy 20 lần/ngày”, nhóm (team / 팀) có thể chia thay đổi (change / 변경) vô nghĩa. Nếu mục tiêu (target / 대상) là “coverage 90%”, tests có thể tăng line coverage nhưng không kiểm thử (test / 테스트) bất biến (invariant / 불변식). Nếu mục tiêu (target / 대상) là “close tickets nhanh”, tickets có thể bị split/close sớm.

Bài toán (problem / 문제) không phải chỉ số (metric / 지표) xấu; bài toán (problem / 문제) là **proxy bị dùng như mục tiêu (objective / 목표) duy nhất**.

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **18. chỉ số (metric / 지표) quản trị (governance / 거버넌스) cần một chỉ số (metric / 지표) cây (tree / 트리)** tiếp nhận điểm tựa từ **17. Goodhart xuất hiện vì proxy khác mục tiêu (objective / 목표)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Leading và lagging indicators có vai trò khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. chỉ số (metric / 지표) quản trị (governance / 거버넌스) cần một chỉ số (metric / 지표) cây (tree / 트리)

Bắt đầu từ kết quả (outcome / 결과):

```text
customer/business outcome
→ reliability/security/correctness constraint
→ delivery capability
→ system/process signals
```

Ví dụ “giảm lead thời gian (time / 시간)” phải giữ change-failure/SLO guardrail. “Giảm cloud chi phí (cost / 비용)” phải giữ độ trễ (latency / 지연 시간)/lỗi (error / 오류)/bảo mật (security / 보안) guardrail.

Chỉ số (metric / 지표) cây (tree / 트리) làm rõ sự đánh đổi (trade-off / 트레이드오프) thay vì tối ưu single number.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **19. Leading và lagging indicators có vai trò khác nhau** tiếp nhận điểm tựa từ **18. chỉ số (metric / 지표) quản trị (governance / 거버넌스) cần một chỉ số (metric / 지표) cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. DORA-style metrics là diagnostic signals, không phải nhóm (team / 팀) leaderboard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Leading và lagging indicators có vai trò khác nhau

Sự cố (incident / 인시던트) tỷ lệ (rate / 비율) là lagging indicator: biết sau khi thất bại (failure / 실패) xảy ra. kiểm thử (test / 테스트) tín hiệu (signal / 신호), rollout anomaly hoặc độ phức tạp (complexity / 복잡도) hotspot có thể leading nhưng nhiều false positives hơn.

Một quản trị (governance / 거버넌스) tốt kết hợp cả hai. Không đòi leading indicator “dự đoán hoàn hảo”.

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **20. DORA-style metrics là diagnostic signals, không phải nhóm (team / 팀) leaderboard** tiếp nhận điểm tựa từ **19. Leading và lagging indicators có vai trò khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화) có thể làm toàn cục (global / 전역) hệ thống (system / 시스템) tệ hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. DORA-style metrics là diagnostic signals, không phải nhóm (team / 팀) leaderboard

Triển khai (deployment / 배포) frequency, lead thời gian (time / 시간), thay đổi (change / 변경) thất bại (failure / 실패) và khôi phục (recovery / 복구) thời gian (time / 시간) có thể hữu ích để thấy luồng (flow / 흐름)/độ tin cậy (reliability / 신뢰성) trend.

Nhưng so trực tiếp teams có sản phẩm (product / 제품)/rủi ro (risk / 위험)/regulatory ngữ cảnh (context / 맥락) khác nhau có thể sai. nhóm (team / 팀) hạ tầng (infrastructure / 인프라) có đơn vị (unit / 단위) of triển khai (deployment / 배포) khác mobile app nhóm (team / 팀).

Dùng metrics để tìm ràng buộc (constraint / 제약조건) và trend nội bộ tốt hơn dùng để xếp hạng con người.

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **21. cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화) có thể làm toàn cục (global / 전역) hệ thống (system / 시스템) tệ hơn** tiếp nhận điểm tựa từ **20. DORA-style metrics là diagnostic signals, không phải nhóm (team / 팀) leaderboard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. kỹ thuật (engineering / 엔지니어링) productivity không thể nén thành LOC/lần ghi nhận (commit / 커밋) count** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화) có thể làm toàn cục (global / 전역) hệ thống (system / 시스템) tệ hơn

Nhóm (team / 팀) A giảm lead thời gian (time / 시간) bằng cách đẩy kiểm tra hợp lệ (validation / 검증) sang downstream nhóm (team / 팀) B. chỉ số (metric / 지표) A đẹp hơn nhưng end-to-end delivery không nhanh hơn.

Do đó ranh giới (boundary / 경계) của chỉ số (metric / 지표) phải khớp ranh giới (boundary / 경계) của kết quả (outcome / 결과). Nếu mục tiêu (objective / 목표) là customer thay đổi (change / 변경) lead thời gian (time / 시간), đo chỉ một chuỗi xử lý (pipeline / 파이프라인) stage dễ bị game.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **22. kỹ thuật (engineering / 엔지니어링) productivity không thể nén thành LOC/lần ghi nhận (commit / 커밋) count** tiếp nhận điểm tựa từ **21. cục bộ (local / 로컬) tối ưu hóa (optimization / 최적화) có thể làm toàn cục (global / 전역) hệ thống (system / 시스템) tệ hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. sự cố (incident / 인시던트) học tập (learning / 학습) là phản hồi (feedback / 피드백) cho debt portfolio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. kỹ thuật (engineering / 엔지니어링) productivity không thể nén thành LOC/lần ghi nhận (commit / 커밋) count

Lines of mã (code / 코드) có thể tăng khi thiết kế (design / 설계) tệ hơn; xóa mã (code / 코드) có thể tạo nhiều giá trị (value / 값). lần ghi nhận (commit / 커밋) count phụ thuộc style. PR count dễ split.

Productivity nên lập luận (reasoning / 추론) từ useful outcomes, chất lượng (quality / 품질), maintainability và luồng (flow / 흐름) các ràng buộc (constraints / 제약조건들); quantitative metrics cần qualitative ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **23. sự cố (incident / 인시던트) học tập (learning / 학습) là phản hồi (feedback / 피드백) cho debt portfolio** tiếp nhận điểm tựa từ **22. kỹ thuật (engineering / 엔지니어링) productivity không thể nén thành LOC/lần ghi nhận (commit / 커밋) count** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Worked example: dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) giữa nhiều services** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. sự cố (incident / 인시던트) học tập (learning / 학습) là phản hồi (feedback / 피드백) cho debt portfolio

Nếu sự cố (incident / 인시던트) postmortem lặp lại cùng phụ thuộc (dependency / 의존성) bottleneck hoặc manual failover, đó là bằng chứng (evidence / 증거) debt interest đang được trả bằng downtime/on-call effort.

Debt prioritization nên tăng khi recurrence chứng minh expected mất mát (loss / 손실) cao hơn estimate cũ.

Sự cố (incident / 인시던트) không chỉ tạo hành động (action / 동작) item “fix bug”; nó cập nhật economic mô hình (model / 모델) của kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **23. sự cố (incident / 인시던트) học tập (learning / 학습) là phản hồi (feedback / 피드백) cho debt portfolio** cho ta quy tắc; **24. Worked example: dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) giữa nhiều services** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. Worked example: kiểm thử (test / 테스트) coverage mục tiêu (target / 대상) bị game** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Worked example: dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) giữa nhiều services

Ban đầu ba services dùng chung lược đồ (schema / 스키마) để ship nhanh. Sau hai năm có 15 services. Một column rename cần months coordination; tests khó isolate; lược đồ (schema / 스키마) deploy có blast radius lớn.

Debt bằng chứng (evidence / 증거):

```text
small schema changes → many teams touched
release coordination ↑
rollback complexity ↑
incidents from hidden consumers ↑
```

Paydown không nhất thiết “microservices rewrite”. Có thể tạo quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계), API/read mô hình (model / 모델), tính tương thích (compatibility / 호환성) tầng (layer / 계층) và migrate consumers dần bằng branch-by-abstraction.

Success chỉ số (metric / 지표) là giảm thay đổi (change / 변경) amplification và blast radius, không phải số services.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **24. Worked example: dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) giữa nhiều services** cho ta quy tắc; **25. Worked example: kiểm thử (test / 테스트) coverage mục tiêu (target / 대상) bị game** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. Một quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thực dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Worked example: kiểm thử (test / 테스트) coverage mục tiêu (target / 대상) bị game

Management đặt 90% coverage làm KPI. nhóm (team / 팀) viết tests gọi getters/setters, mock mọi phụ thuộc (dependency / 의존성) và tránh refactor vì snapshot tests fragile. Coverage tăng nhưng môi trường vận hành (production / 운영 환경) regressions không giảm.

Correction không phải bỏ metrics hoàn toàn. Chuyển focus sang trọng yếu (critical / 중요) bất biến (invariant / 불변식) coverage, mutation/thuộc tính (property / 속성)/đặc tả hợp đồng (contract / 계약) tests ở rủi ro (risk / 위험) areas, kiểm thử (test / 테스트) phản hồi (feedback / 피드백) thời gian (time / 시간) và escaped defect classes.

Chỉ số (metric / 지표) trở lại vai trò sensor.

> **Chuyển mạch:** Trong **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **25. Worked example: kiểm thử (test / 테스트) coverage mục tiêu (target / 대상) bị game** cho ta quy tắc; **26. Một quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thực dụng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **27. Kết nối sang các chapter khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Một quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thực dụng

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

Không cần score giả chính xác. Mục tiêu là làm các giả định (assumptions / 가정들) tường minh (explicit / 명시적) để rà soát (review / 검토) lại theo thời gian.

> **Chuyển mạch:** Ở chặng này của **Technical debt economics, kỹ thuật (engineering / 엔지니어링) metrics và Goodhart's Law**, **27. Kết nối sang các chapter khác** tiếp nhận điểm tựa từ **26. Một quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thực dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 27. Kết nối sang các chapter khác

Technical-debt economics nối với [architecture evolution](./00_architecture_decisions_evolution_and_socio_technical_constraints.md), [boundary economics](./01_modular_monolith_vs_services_boundary_economics.md), [large-scale refactoring](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md), [test architecture](./04_test_architecture_contract_mutation_property_and_production_verification.md) và [deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md).

Mô hình tư duy (mental model / 사고 모델) cuối cùng: **technical debt là portfolio của future các ràng buộc (constraints / 제약조건들). Metrics chỉ giúp thấy interest/rủi ro (risk / 위험) khi chúng vẫn là sensors; khi biến thành mục tiêu (target / 대상) tuyệt đối, chính chỉ số (metric / 지표) có thể tạo debt mới.**

> **Bàn giao:** Sau **27. Kết nối sang các chapter khác**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
