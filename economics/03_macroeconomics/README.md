# 03 — Macroeconomics

Macroeconomics nghiên cứu nền kinh tế ở cấp aggregate nhưng không được biến aggregate thành một “actor duy nhất”. Mô-đun (module / 모듈) này bắt đầu từ đo lường (measurement / 측정), đi qua long-run productive sức chứa (capacity / 용량), labor/inflation, money/banking, fiscal–monetary stabilization và kết thúc ở open-economy các ràng buộc (constraints / 제약조건들). Mỗi chapter phải tách accounting định danh (identity / 식별자) khỏi nhân quả (causal / 인과적) mô hình (model / 모델), short run khỏi long run, và domestic cơ chế (mechanism / 메커니즘) khỏi ứng dụng (application / 애플리케이션) vào financial markets.

## Thứ tự học chuẩn gốc (canonical / 정본)

1. [National Accounts & Macro Measurement](./00_national_accounts_and_macro_measurement.md) — GDP/GNI, nominal–real, price indices, saving–investment identities, stock–luồng (flow / 흐름), potential đầu ra (output / 출력), labor/inflation/productivity đo lường (measurement / 측정) và real-time revisions.
2. [Long-Run Growth & Productivity](./01_long_run_growth_and_productivity.md) — môi trường vận hành (production / 운영 환경) hàm (function / 함수), Solow, capital deepening, technology, growth accounting, human capital, endogenous growth, convergence, institutions, structural transformation và misallocation.
3. [Labor, Unemployment & Inflation](./02_labor_unemployment_and_inflation.md) — labor-force flows, tìm kiếm (search / 검색)/matching, wage setting, Phillips curve, expectations, inflation mechanisms, hysteresis và empirical boundaries.
4. [Money, Banking & Monetary Policy](./03_money_banking_and_monetary_policy.md) — bank/central-bank balance sheets, money creation, capital vs reserves, policy-rate transmission, real rates, QE, credit/exchange-rate channels và financial stability.
5. [Fiscal Policy & Business Cycles](./04_fiscal_policy_and_business_cycles.md) — multipliers, automatic stabilizers, trạng thái (state / 상태) dependence, debt dynamics, fiscal không gian (space / 공간), inventory/financial accelerators, RBC/New Keynesian perspectives và fiscal–monetary tương tác (interaction / 상호작용).
6. [Open Economy, Exchange Rates & Crises](./05_open_economy_exchange_rates_and_crises.md) — balance of payments, `CA = S − I`, nominal/real FX, PPP, interest parity, trilemma, capital flows, currency/maturity mismatch, sudden stops và crisis mechanisms.

## Trục học (learning spine / 학습 축)
Phần “Trục học (learning spine / 학습 축)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Measurement / accounting identities
→ long-run productive capacity
→ short-run labor and price dynamics
→ money / banking / interest-rate transmission
→ fiscal and monetary stabilization
→ open-economy external constraints
→ empirical identification
```

Mô-đun (module / 모듈) cố ý bắt đầu bằng đo lường (measurement / 측정) vì macro rất dễ nhầm định danh (identity / 식별자) với lý thuyết (theory / 이론). `S = I + NX`, government ngân sách (budget / 예산) ràng buộc (constraint / 제약조건) hay balance-of-payments equality là accounting structures; chúng không tự nói direction of causality. Nhân quả (causal / 인과적) interpretation phải đi qua behavioral các giả định (assumptions / 가정들), institutional regime và bằng chứng (evidence / 증거).

## Kết quả cần đạt

Sau mô-đun (module / 모듈) này, người học phải có thể phân biệt stock/luồng (flow / 흐름), nominal/real, gross/net và aggregate/per-capita; đọc GDP/inflation/unemployment mà không bỏ revisions hoặc denominator effects; giải thích vì sao capital accumulation khác productivity growth; tách frictional/structural/cyclical unemployment; đọc inflation qua demand, supply, expectations và markups; dựng balance-sheet lô-gic (logic / 논리) của banks và central bank; đánh giá fiscal multiplier theo trạng thái (state / 상태)/regime; phân tích debt dynamics qua primary balance và `r − g`; đồng thời đọc hiện tại (current / 현재) account, exchange tỷ lệ (rate / 비율) và capital flows qua bên ngoài (external / 외부) balance-sheet exposures thay vì một headline ratio.

Người học cũng phải biết bất định (uncertainty / 불확실성) nằm ở đâu. Potential đầu ra (output / 출력), neutral tỷ lệ (rate / 비율), NAIRU và expected inflation đều không quan sát trực tiếp; chúng là model-dependent estimates. Không dùng một điểm (point / 지점) estimate như fact tuyệt đối.

## Ranh giới (boundary / 경계) với Investing Economics

[`investing/04_economics/`](../../investing/04_economics/README.md) tiếp tục giữ ứng dụng (application / 애플리케이션) tầng (layer / 계층) cho macro dữ liệu (data / 데이터) playbook, liquidity, thị trường (market / 시장) transmission, crisis cases, chính sách (policy / 정책) regimes, debt/demographics và nowcasting. `economics/03_macroeconomics/` là chuẩn gốc (canonical / 정본) general-purpose tầng (layer / 계층): giải cơ chế (mechanism / 메커니즘), các giả định (assumptions / 가정들) và accounting trước khi map sang asset prices hoặc positioning.

Quy tắc là **cross-link, không duplicate**. Khi Investing cần giải thích nguyên lý chung, link về chapter chuẩn gốc (canonical / 정본) tại đây; khi Economics cần market-specific monitoring hoặc investment interpretation, link sang Investing.

## Ranh giới (boundary / 경계) với Econometrics

Macro mô hình (model / 모델) tạo predictions nhưng nhiều biến endogenous cùng lúc. Ví dụ tỷ lệ (rate / 비율) hike thường xảy ra khi inflation/outlook đã thay đổi, nên correlation giữa tỷ lệ (rate / 비율) và inflation không đo nhân quả (causal / 인과적) tác động (effect / 효과) của chính sách (policy / 정책). Fiscal spending cũng phản ứng với recession, exchange tỷ lệ (rate / 비율) phản ứng với both domestic and toàn cục (global / 전역) shocks.

Vì vậy bước tiếp theo là [Econometrics](../README.md#learning-route-và-coverage-target): đo lường (measurement / 측정) → identification → regression → experiments/quasi-experiments → IV/DiD/panel/thời gian (time / 시간) series. Macro bằng chứng (evidence / 증거) cần đặc biệt chú ý simultaneity, expectations, regime changes và real-time dữ liệu (data / 데이터) revisions.

## Ranh giới (boundary / 경계) với Applied Economics và Lịch sử (history / 이력)

Labor, công khai (public / 공개) finance, trade, development và industrial organization sẽ dùng macro các ràng buộc (constraints / 제약조건들) nhưng cần micro foundations và nhân quả (causal / 인과적) bằng chứng (evidence / 증거) riêng. Economic Lịch sử (history / 이력) & Institutions sẽ dùng macro chuỗi (sequence / 시퀀스) để so sánh growth, crises, monetary regimes và trạng thái (state / 상태) sức chứa (capacity / 용량) qua thời gian; không duplicate chronology từ World Lịch sử (history / 이력).

## Checklist khi đọc một macro claim

Trước khi chấp nhận một kết luận, kiểm tra: đại lượng đang đo là gì; accounting định danh (identity / 식별자) nào đang dùng; behavioral cơ chế (mechanism / 메커니즘) nào biến định danh (identity / 식별자) thành prediction; horizon short/long run; regime monetary/fiscal/exchange-rate; balance-sheet exposure; expectations; distributional heterogeneity; dữ liệu (data / 데이터) vintage; và identification chiến lược (strategy / 전략) nào có thể phân biệt nhân quả (causal / 인과적) tác động (effect / 효과) với chính sách (policy / 정책) phản hồi (response / 응답)/endogeneity.
