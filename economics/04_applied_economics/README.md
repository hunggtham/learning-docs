# 04 — Applied Economics

> **Mạch đọc:** [README](./README.md) là owner của **04 — Applied Economics**. Route học đi từ ngành, tổ chức và chính sách → labor/health/environment/IO → dữ liệu và identification → đánh giá trade-off, để ứng dụng luôn quay về mô hình kinh tế và giới hạn bằng chứng.

Applied Economics dùng lý thuyết (theory / 이론) từ Microeconomics, Thị trường (market / 시장) Cấu trúc (structure / 구조)/Game Lý thuyết (theory / 이론) và Macroeconomics cùng identification discipline từ Econometrics để phân tích labor, taxation/công khai (public / 공개) chính sách (policy / 정책), trade, development và industries cụ thể. Mô-đun (module / 모듈) này không phải tập hợp trường hợp (case / 사례) studies. Mỗi chapter phải trả lời đồng thời: **cơ chế (mechanism / 메커니즘) nào đang hoạt động, estimand nào cần đo, variation nào identify tác động (effect / 효과), ai chịu incidence, và kết quả (result / 결과) có generalize/quy mô (scale / 규모) được không?**

## Thứ tự học chuẩn gốc (canonical / 정본)

1. [Labor Economics](./00_labor_economics.md) — labor demand/supply, human capital, signaling, tìm kiếm (search / 검색)/matching, monopsony, minimum wage, unions, discrimination, di chuyển (migration / 마이그레이션) và labor-policy identification.
2. [Public Economics](./01_public_economics.md) — taxation/incidence, redistribution, xã hội (social / 사회적) insurance, health/education provision, administrative burden, optimal-tax lô-gic (logic / 논리) và chính sách (policy / 정책) evaluation.
3. [International Trade](./02_international_trade.md) — comparative advantage, factor phân phối (distribution / 분포), gravity, firm heterogeneity, tariffs, toàn cục (global / 전역) giá trị (value / 값) chains, trade adjustment và empirical trade designs.
4. [Development Economics](./03_development_economics.md) — poverty, credit/rủi ro (risk / 위험) các ràng buộc (constraints / 제약조건들), health/education, structural transformation, hạ tầng (infrastructure / 인프라), institutions/trạng thái (state / 상태) sức chứa (capacity / 용량), industrial chính sách (policy / 정책) và scale-up.
5. [Industrial Organization](./04_industrial_organization.md) — demand estimation, substitution, markups, entry, vertical/nền tảng (platform / 플랫폼) markets, mergers, procurement, innovation và structural/reduced-form IO.

> **Chuyển mạch:** Canonical order supplies theory; applied spine adds domain institutions, measurement and policy constraints, making each dependency explicit.

## Applied spine

```text
Economic mechanism
→ treatment / exposure / institutional variation
→ outcome + population
→ estimand
→ identification problem
→ empirical design
→ incidence / distribution
→ equilibrium / dynamics / scale-up
→ policy limits
```

Nếu một chapter chỉ có lý thuyết (theory / 이론) mà không nói dữ liệu (data / 데이터)/thiết kế (design / 설계), nó chưa đủ applied. Nếu chỉ có empirical correlation mà không có cơ chế (mechanism / 메커니즘)/counterfactual, nó cũng chưa đủ applied.

> **Chuyển mạch:** Applied spine links theory to domain constraints; each dependency must be stated as evidence/contract so policy claims remain testable.

## Phụ thuộc (dependency / 의존성)

Applied Economics nên được đọc sau hoặc song song với:

- [Microeconomics](../01_microeconomics/README.md) cho incentives, welfare và thị trường (market / 시장) failures;
- [Market Structure & Game Theory](../02_market_structure_game_theory/README.md) cho strategic tương tác (interaction / 상호작용), thị trường (market / 시장) power và cơ chế (mechanism / 메커니즘) thiết kế (design / 설계);
- [Macroeconomics](../03_macroeconomics/README.md) cho aggregate các ràng buộc (constraints / 제약조건들), fiscal/monetary/open-economy regimes;
- [Econometrics](../05_econometrics/README.md) cho estimands, counterfactuals, OLS/IV/RDD/DiD/thời gian (time / 시간) series và robustness.

Folder numbering giữ `04 Applied`, `05 Econometrics`, nhưng hiện thực (implementation / 구현) thứ tự (order / 순서) cố ý xây Econometrics trước để mô-đun (module / 모듈) này có bằng chứng (evidence / 증거) discipline ngay từ đầu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Applied Economics**, **Phụ thuộc (dependency / 의존성)** nêu điều cần giải thích; **Bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phân phối (distribution / 분포) và general equilibrium** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약)

Mỗi empirical claim trong Applied Economics phải ghi rõ ít nhất một trong ba trạng thái:

```text
Descriptive evidence
Causal evidence under stated design assumptions
Structural/model-based counterfactual
```

Không trộn ba tầng này.

Một exporter productivity premium là descriptive cho đến khi xử lý selection. Một DiD estimate là nhân quả (causal / 인과적) chỉ nếu parallel trends/counterfactual credible. Một merger simulation là structural counterfactual conditional on estimated demand/conduct các giả định (assumptions / 가정들).

> **Chuyển mạch:** Trong **04 — Applied Economics**, **Bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **Phân phối (distribution / 분포) và general equilibrium** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Chính sách (policy / 정책) interpretation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) và general equilibrium

Applied chính sách (policy / 정책) gần như luôn tạo winners/losers. Vì vậy average tác động (effect / 효과) không đủ nếu incidence khác mạnh theo income, skill, geography, firm kích thước (size / 크기) hoặc thị trường (market / 시장) position.

Ngoài ra, tác động (effect / 효과) cục bộ (local / 로컬)/pilot có thể đổi khi quy mô (scale / 규모): wages, prices, rents, firm entry, di chuyển (migration / 마이그레이션), taxes và political phản hồi (response / 응답) đều có thể điều chỉnh. Mô-đun (module / 모듈) này phải luôn nêu partial-equilibrium vs general-equilibrium ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **04 — Applied Economics**, **Chính sách (policy / 정책) interpretation** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) và general equilibrium** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) interpretation

Economics có thể estimate consequences, trade-offs và welfare under tường minh (explicit / 명시적) xã hội (social / 사회적) các giả định (assumptions / 가정들). Một estimate không tự chuyển thành chính sách (policy / 정책) recommendation. Chính sách (policy / 정책) còn phụ thuộc distributional weights, legal các ràng buộc (constraints / 제약조건들), hiện thực (implementation / 구현) sức chứa (capacity / 용량), rights, political institutions và bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **04 — Applied Economics**, **Connections** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) interpretation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checklist khi đọc một applied claim** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Connections

- [Korea Business & Economy](../../korea_business_economy_knowledge_library/README.md) là trường hợp (case / 사례) tầng (layer / 계층) để áp dụng labor, trade, industrial chính sách (policy / 정책), firm cấu trúc (structure / 구조) và finance trong bối cảnh Hàn Quốc.
- [Investing](../../investing/README.md) dùng firm/industry/macro results để phân tích assets và companies; không thay thế applied economics.
- [World Geography](../../world_geography/README.md) cung cấp spatial, vận chuyển (transport / 전송), tài nguyên (resource / 자원) và market-access các ràng buộc (constraints / 제약조건들).
- [World History](../../world_history/README.md) cung cấp institutional/historical chuỗi (sequence / 시퀀스) nhưng không tự đóng vai nhân quả (causal / 인과적) thiết kế (design / 설계).
- [Psychology](../../psychology/README.md) liên quan labor supply, salience, take-up, expectations và behavioral công khai (public / 공개) economics.

> **Chuyển mạch:** Trong **04 — Applied Economics**, **Checklist khi đọc một applied claim** tiếp nhận điểm tựa từ **Connections** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Checklist khi đọc một applied claim

Hãy hỏi: cơ chế (mechanism / 메커니즘) nào; đơn vị (unit / 단위)/population nào; kết quả (outcome / 결과)/treatment là gì; estimand nào; assignment/nguồn (source / 소스) of variation nào; selection/endogeneity nào; thiết kế (design / 설계) các giả định (assumptions / 가정들) nào không kiểm thử (test / 테스트) được trực tiếp; incidence rơi vào ai; short-run/long-run khác nhau không; equilibrium/scale-up có đổi tác động (effect / 효과) không; kết quả (result / 결과) có bên ngoài (external / 외부) validity sang institution khác không.

Applied Economics hoàn tất cốt lõi (core / 핵심) khi người đọc không chỉ biết “chính sách (policy / 정책) X thường có tác động (effect / 효과) Y”, mà có thể giải thích **vì sao, tác động (effect / 효과) nào được đo, từ variation nào, cho population nào, và kết luận dừng ở đâu**.

> **Bàn giao:** Sau **Checklist khi đọc một applied claim**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
