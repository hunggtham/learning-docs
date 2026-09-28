# 04 — Applied Economics

> **Mạch đọc:** Đọc **04 — Applied Economics** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Thứ tự học chuẩn gốc (canonical / 정본)** sang **Applied spine**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Applied Economics dùng lý thuyết (theory / 이론) từ Microeconomics, thị trường (market / 시장) cấu trúc (structure / 구조)/Game lý thuyết (theory / 이론) và Macroeconomics cùng identification discipline từ Econometrics để phân tích labor, taxation/công khai (public / 공개) chính sách (policy / 정책), trade, development và industries cụ thể. mô-đun (module / 모듈) này không phải tập hợp trường hợp (case / 사례) studies. Mỗi chapter phải trả lời đồng thời: **cơ chế (mechanism / 메커니즘) nào đang hoạt động, estimand nào cần đo, variation nào identify tác động (effect / 효과), ai chịu incidence, và kết quả (result / 결과) có generalize/quy mô (scale / 규모) được không?**

Nói đơn giản, Applied Economics lấy một câu hỏi đời thực như “tăng lương tối thiểu có làm mất việc không?” hoặc “thuế này rơi vào ai?” rồi tách nó thành các phần nhỏ: cơ chế lý thuyết là gì, dữ liệu đo biến nào, nhóm so sánh nào tạo counterfactual, và kết quả có còn đúng khi chính sách được mở rộng không. Vì thế một ví dụ thực tế chỉ là điểm bắt đầu; nó chưa phải bằng chứng.

## Thứ tự học chuẩn gốc (canonical / 정본)

1. [Labor Economics](./00_labor_economics.md) — labor demand/supply, human capital, signaling, tìm kiếm (search / 검색)/matching, monopsony, minimum wage, unions, discrimination, di chuyển (migration / 마이그레이션) và labor-policy identification.
2. [Public Economics](./01_public_economics.md) — taxation/incidence, redistribution, xã hội (social / 사회적) insurance, health/education provision, administrative burden, optimal-tax lô-gic (logic / 논리) và chính sách (policy / 정책) evaluation.
3. [International Trade](./02_international_trade.md) — comparative advantage, factor phân phối (distribution / 분포), gravity, firm heterogeneity, tariffs, toàn cục (global / 전역) giá trị (value / 값) chains, trade adjustment và empirical trade designs.
4. [Development Economics](./03_development_economics.md) — poverty, credit/rủi ro (risk / 위험) các ràng buộc (constraints / 제약조건들), health/education, structural transformation, hạ tầng (infrastructure / 인프라), institutions/trạng thái (state / 상태) sức chứa (capacity / 용량), industrial chính sách (policy / 정책) và scale-up.
5. [Industrial Organization](./04_industrial_organization.md) — demand estimation, substitution, markups, entry, vertical/nền tảng (platform / 플랫폼) markets, mergers, procurement, innovation và structural/reduced-form IO.


> **Chuyển mạch:** Từ **Thứ tự học chuẩn gốc (canonical / 정본)**, ta sang **Applied spine** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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

Đọc theo thứ tự: **câu hỏi → cơ chế → đại lượng cần đo → thiết kế nhận diện → phân phối lợi ích/chi phí → giới hạn khi áp dụng**. Cách này giúp tránh hai lỗi phổ biến: dùng một mô hình đẹp để trả lời sai câu hỏi, hoặc dùng một con số thực nghiệm mà không biết nó đo tác động (effect / 효과) nào.


> **Chuyển mạch:** Từ **Applied spine**, ta sang **phụ thuộc (dependency / 의존성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Phụ thuộc (dependency / 의존성)

Applied Economics nên được đọc sau hoặc song song với:

- [Microeconomics](../01_microeconomics/README.md) cho incentives, welfare và thị trường (market / 시장) failures;
- [Market Structure & Game Theory](../02_market_structure_game_theory/README.md) cho strategic tương tác (interaction / 상호작용), thị trường (market / 시장) power và cơ chế (mechanism / 메커니즘) thiết kế (design / 설계);
- [Macroeconomics](../03_macroeconomics/README.md) cho aggregate các ràng buộc (constraints / 제약조건들), fiscal/monetary/open-economy regimes;
- [Econometrics](../05_econometrics/README.md) cho estimands, counterfactuals, OLS/IV/RDD/DiD/thời gian (time / 시간) series và robustness.

Folder numbering giữ `04 Applied`, `05 Econometrics`, nhưng hiện thực (implementation / 구현) thứ tự (order / 순서) cố ý xây Econometrics trước để mô-đun (module / 모듈) này có bằng chứng (evidence / 증거) discipline ngay từ đầu.


> **Chuyển mạch:** Từ **phụ thuộc (dependency / 의존성)**, ta sang **bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약)

Mỗi empirical claim trong Applied Economics phải ghi rõ ít nhất một trong ba trạng thái:

```text
Descriptive evidence
Causal evidence under stated design assumptions
Structural/model-based counterfactual
```

Không trộn ba tầng này.

Một exporter productivity premium là descriptive cho đến khi xử lý selection. Một DiD estimate là nhân quả (causal / 인과적) chỉ nếu parallel trends/counterfactual credible. Một merger simulation là structural counterfactual conditional on estimated demand/conduct các giả định (assumptions / 가정들).


> **Chuyển mạch:** Từ **bằng chứng (evidence / 증거) đặc tả hợp đồng (contract / 계약)**, ta sang **phân phối (distribution / 분포) và general equilibrium** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Phân phối (distribution / 분포) và general equilibrium

Applied chính sách (policy / 정책) gần như luôn tạo winners/losers. Vì vậy average tác động (effect / 효과) không đủ nếu incidence khác mạnh theo income, skill, geography, firm kích thước (size / 크기) hoặc thị trường (market / 시장) position.

Ngoài ra, tác động (effect / 효과) cục bộ (local / 로컬)/pilot có thể đổi khi quy mô (scale / 규모): wages, prices, rents, firm entry, di chuyển (migration / 마이그레이션), taxes và political phản hồi (response / 응답) đều có thể điều chỉnh. mô-đun (module / 모듈) này phải luôn nêu partial-equilibrium vs general-equilibrium ranh giới (boundary / 경계).


> **Chuyển mạch:** Từ **phân phối (distribution / 분포) và general equilibrium**, ta sang **chính sách (policy / 정책) interpretation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chính sách (policy / 정책) interpretation

Economics có thể estimate consequences, trade-offs và welfare under tường minh (explicit / 명시적) xã hội (social / 사회적) các giả định (assumptions / 가정들). Một estimate không tự chuyển thành chính sách (policy / 정책) recommendation. chính sách (policy / 정책) còn phụ thuộc distributional weights, legal các ràng buộc (constraints / 제약조건들), hiện thực (implementation / 구현) sức chứa (capacity / 용량), rights, political institutions và bất định (uncertainty / 불확실성).


> **Chuyển mạch:** Từ **chính sách (policy / 정책) interpretation**, ta sang **Connections** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Connections

- [Korea Business & Economy](../../korea_business_economy_knowledge_library/README.md) là trường hợp (case / 사례) tầng (layer / 계층) để áp dụng labor, trade, industrial chính sách (policy / 정책), firm cấu trúc (structure / 구조) và finance trong bối cảnh Hàn Quốc.
- [Investing](../../investing/README.md) dùng firm/industry/macro results để phân tích assets và companies; không thay thế applied economics.
- [World Geography](../../world_geography/README.md) cung cấp spatial, vận chuyển (transport / 전송), tài nguyên (resource / 자원) và market-access các ràng buộc (constraints / 제약조건들).
- [World History](../../world_history/README.md) cung cấp institutional/historical chuỗi (sequence / 시퀀스) nhưng không tự đóng vai nhân quả (causal / 인과적) thiết kế (design / 설계).
- [Psychology](../../psychology/README.md) liên quan labor supply, salience, take-up, expectations và behavioral công khai (public / 공개) economics.


> **Chuyển mạch:** Từ **Connections**, ta sang **Checklist khi đọc một applied claim** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Checklist khi đọc một applied claim

Hãy hỏi: cơ chế (mechanism / 메커니즘) nào; đơn vị (unit / 단위)/population nào; kết quả (outcome / 결과)/treatment là gì; estimand nào; assignment/nguồn (source / 소스) of variation nào; selection/endogeneity nào; thiết kế (design / 설계) các giả định (assumptions / 가정들) nào không kiểm thử (test / 테스트) được trực tiếp; incidence rơi vào ai; short-run/long-run khác nhau không; equilibrium/scale-up có đổi tác động (effect / 효과) không; kết quả (result / 결과) có bên ngoài (external / 외부) validity sang institution khác không.

Applied Economics hoàn tất cốt lõi (core / 핵심) khi người đọc không chỉ biết “chính sách (policy / 정책) X thường có tác động (effect / 효과) Y”, mà có thể giải thích **vì sao, tác động (effect / 효과) nào được đo, từ variation nào, cho population nào, và kết luận dừng ở đâu**.

> **Bàn giao:** Sau **Checklist khi đọc một applied claim**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 labor economics](./00_labor_economics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
