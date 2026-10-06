# 15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations

> **Mạch đọc:** [README](./README.md) là owner của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**; dùng README để định vị chapter trong track FX theo quốc gia. Từ **Part I — Korea** qua USD/KRW, market structure, participants, regulation và corporate hedging, rồi nối sang Vietnam và phần so sánh; các quy định nhạy thời gian phải được gắn với ngày kiểm chứng và phạm vi áp dụng.

> **Time-sensitive chapter.** Phần regulatory phải được kiểm tra lại trước khi dùng cho quyết định thực tế. Nội dung dưới đây được research theo nguồn chính thức đang truy cập ngày **2026-09-25** và phục vụ học cấu trúc thị trường, không thay thế tư vấn pháp lý/thuế/compliance.

Forex không vận hành giống nhau ở mọi quốc gia. Cùng từ “FX” có thể chỉ:

- interbank spot thị trường (market / 시장);
- corporate hedging;
- exchange-traded futures;
- regulated retail FX-margin sản phẩm (product / 제품);
- OTC derivative;
- simple currency conversion.

Vì vậy trước khi mở tài khoản hoặc backtest một instrument, phải hỏi:

```text
Jurisdiction
→ legal product category
→ permitted intermediary
→ account / remittance rules
→ margin / investor-protection rules
→ tax / reporting
→ actual executable instrument
```

## Part I — Korea

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **1. USD/KRW quote** nối từ **Part I — Korea** sang **2. Korea FX thị trường (market / 시장) không chỉ là retail app**, vì cơ chế trước tạo đầu vào cho bước sau.

## 1. USD/KRW quote

```text
USD/KRW = KRW per 1 USD
```

Nếu USD/KRW tăng:

```text
USD strengthens vs KRW
KRW weakens vs USD
```

Tiếng Hàn:

- tỷ giá: **환율**;
- ngoại hối: **외환**;
- won mạnh: **원화 강세**;
- won yếu: **원화 약세**;
- rủi ro tỷ giá: **환위험**;
- phòng vệ tỷ giá: **환헤지**.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **2. Korea FX thị trường (market / 시장) không chỉ là retail app** nối từ **1. USD/KRW quote** sang **3. Seoul FX thị trường (market / 시장) structural reform**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Korea FX thị trường (market / 시장) không chỉ là retail app

Các tầng (layer / 계층) cần phân biệt:

```text
Seoul wholesale FX market
Bank/customer FX transactions
NDF/offshore KRW markets
Currency futures/derivatives
Retail FX-margin trading
Simple bank currency exchange
```

Rules và participant set khác nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **3. Seoul FX thị trường (market / 시장) structural reform** nối từ **2. Korea FX thị trường (market / 시장) không chỉ là retail app** sang **4. Trading hours**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Seoul FX thị trường (market / 시장) structural reform

Bank of Korea và government triển khai **외환시장 구조 개선방안 — improvement measures for FX thị trường (market / 시장) cấu trúc (structure / 구조)** để tăng toàn cục (global / 전역) thị trường (market / 시장) truy cập (access / 접근).

Key changes gồm:

- foreign financial institutions đủ điều kiện có thể đăng ký thành **Registered Foreign Institution (RFI)** và tham gia thị trường;
- thị trường (market / 시장) hạ tầng (infrastructure / 인프라)/practices được điều chỉnh cho broader truy cập (access / 접근);
- trading hours của Seoul FX thị trường (market / 시장) được kéo dài.

BOK duy trì portal và danh sách RFI chính thức; danh sách (list / 목록) được cập nhật (update / 업데이트) theo thời điểm nên không bản sao (copy / 복사) một danh sách cố định vào tài liệu.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **4. Trading hours** nối từ **3. Seoul FX thị trường (market / 시장) structural reform** sang **5. RFI**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Trading hours

Theo BOK market-structure thông tin (information / 정보), từ **July 2024** Seoul FX thị trường (market / 시장) operating hours được mở rộng từ session cũ tới:

```text
09:00 Korea time
→ 02:00 next day
```

Mục tiêu là overlap tốt hơn với London và New York hours.

Điều này quan trọng cho dữ liệu (data / 데이터) research: backtest USD/KRW trước và sau reform có khác biệt về session/liquidity cấu trúc (structure / 구조).

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **5. RFI** nối từ **4. Trading hours** sang **6. Seoul Mã (code / 코드) of Conduct / FX Toàn cục (global / 전역) Mã (code / 코드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. RFI

**Registered Foreign Institution (RFI)** là foreign financial institution đáp ứng requirements và đăng ký với Korean FX authorities để tham gia theo khung phần mềm (framework / 프레임워크) mới.

RFI reform làm:

- direct truy cập (access / 접근) của toàn cục (global / 전역) institutions tăng;
- participant mix thay đổi;
- price discovery/liquidity dynamics có thể thay đổi theo giờ.

Do đó historical microstructure trước 2024 không nên assumed identical với hiện tại (current / 현재) thị trường (market / 시장).

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **6. Seoul Mã (code / 코드) of Conduct / FX Toàn cục (global / 전역) Mã (code / 코드)** nối từ **5. RFI** sang **7. BOK và monetary-policy channel**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Seoul Mã (code / 코드) of Conduct / FX Toàn cục (global / 전역) Mã (code / 코드)

Seoul Foreign Exchange Thị trường (market / 시장) Committee có mã (code / 코드) về:

- responsibilities;
- ethics/confidentiality;
- dealing principles;
- documentation;
- thứ tự (order / 순서) handling;
- operational practices.

BOK cũng có Seoul Register cho thị trường (market / 시장) participants công bố Statement of Commitment với FX Toàn cục (global / 전역) Mã (code / 코드).

Đây là institutional-market conduct khung phần mềm (framework / 프레임워크), không phải trading chiến lược (strategy / 전략).

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **7. BOK và monetary-policy channel** nối từ **6. Seoul Mã (code / 코드) of Conduct / FX Toàn cục (global / 전역) Mã (code / 코드)** sang **8. Export/semiconductor channel**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. BOK và monetary-policy channel

USD/KRW research thường cần theo dõi:

```text
BOK expected policy path
vs Fed expected policy path
```

Nhưng tỷ lệ (rate / 비율) differential chỉ là một channel.

KRW còn nhạy với:

- Korean export cycle;
- semiconductor demand;
- năng lượng (energy / 에너지) import prices;
- foreign equity/bond flows;
- broad USD;
- China/toàn cục (global / 전역) growth;
- rủi ro (risk / 위험) sentiment;
- intervention/chính sách (policy / 정책) expectations.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **8. Export/semiconductor channel** nối từ **7. BOK và monetary-policy channel** sang **9. Năng lượng (energy / 에너지) import channel**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Export/semiconductor channel

Korea có export-heavy industrial cấu trúc (structure / 구조); semiconductor cycle có thể ảnh hưởng:

```text
export receipts
corporate FX conversion
growth expectations
foreign equity flows
```

Không nên dùng quy tắc (rule / 규칙) đơn giản “semiconductor up → KRW up”, nhưng đây là nhân quả (causal / 인과적) channel cần nghiên cứu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **9. Năng lượng (energy / 에너지) import channel** nối từ **8. Export/semiconductor channel** sang **10. Foreign portfolio flows**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Năng lượng (energy / 에너지) import channel

Korea phụ thuộc nhiều vào imported năng lượng (energy / 에너지).

Năng lượng (energy / 에너지) shock có thể:

```text
import bill ↑
→ terms of trade deteriorate
→ inflation pressure ↑
→ corporate/household real income pressure
```

FX phản hồi (response / 응답) còn phụ thuộc chính sách (policy / 정책) and toàn cục (global / 전역) USD regime.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **9. Năng lượng (energy / 에너지) import channel** đặt đầu vào cho **10. Foreign portfolio flows**, rồi **11. Onshore vs offshore KRW** mở rộng hệ quả hoặc giới hạn liên quan.

## 10. Foreign portfolio flows

Foreign buying/selling Korean equities/bonds có thể tạo FX hedging/conversion demand.

Need distinguish:

```text
asset flow
currency hedge ratio
actual FX conversion
```

Foreign investor buying Korean stock không có nghĩa toàn notional immediately buys KRW unhedged.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **10. Foreign portfolio flows** đặt đầu vào cho **11. Onshore vs offshore KRW**, rồi **12. Retail FX-margin trading in Korea** mở rộng hệ quả hoặc giới hạn liên quan.

## 11. Onshore vs offshore KRW

KRW price discovery có thể liên quan:

- onshore USD/KRW thị trường (market / 시장);
- offshore NDF;
- toàn cục (global / 전역) derivatives.

Different sessions/truy cập (access / 접근) rules create lead-lag and basis relationships.

Thị trường (market / 시장) reform is intended partly to improve onshore khả năng tiếp cận (accessibility / 접근성), so relationships may evolve.

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **12. Retail FX-margin trading in Korea** nối từ **11. Onshore vs offshore KRW** sang **13. Korean retail intermediary yêu cầu (requirement / 요구사항)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Retail FX-margin trading in Korea

**FX마진거래** là một specific regulated sản phẩm (product / 제품) category in Korean investor guidance, không đồng nghĩa toàn bộ spot FX thị trường (market / 시장).

Korea Financial Investment Association (KOFIA) describes FX-margin trading as leveraged foreign-currency derivative-style trading with standardized đặc tả hợp đồng (contract / 계약) conventions and margin.

Important: sản phẩm (product / 제품) terms must be checked at the licensed Korean financial investment company; old/general web examples are not substitute for hiện tại (current / 현재) đặc tả hợp đồng (contract / 계약) specification.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **13. Korean retail intermediary yêu cầu (requirement / 요구사항)** nối từ **12. Retail FX-margin trading in Korea** sang **14. Korea FX-margin rủi ro (risk / 위험) disclosures**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Korean retail intermediary yêu cầu (requirement / 요구사항)

KOFIA's hiện tại (current / 현재) investor-warning material states that an individual participating in FX-margin trading must use a **domestic investment intermediary (국내 투자중개업자)** under the Korean capital-markets khung phần mềm (framework / 프레임워크).

KOFIA specifically warns that direct trading with an overseas financial investment nghiệp vụ (business / 비즈니스) without going through the permitted domestic derivatives/investment intermediary is illegal under the khung phần mềm (framework / 프레임워크) it describes, and related remittance may also violate foreign-exchange rules.

Practical học tập (learning / 학습) quy tắc (rule / 규칙):

```text
Do not assume:
“Broker accepts Korean residents”
=
“Trading route is lawful in Korea.”
```

Verify chính xác (exact / 정확한) legal thực thể (entity / 엔터티) and Korean intermediary tuyến (route / 경로).

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **14. Korea FX-margin rủi ro (risk / 위험) disclosures** nối từ **13. Korean retail intermediary yêu cầu (requirement / 요구사항)** sang **15. Domestic license check**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Korea FX-margin rủi ro (risk / 위험) disclosures

KOFIA highlights risks including:

- leverage magnifying mất mát (loss / 손실);
- spread/rollover chi phí (cost / 비용);
- counterparty rủi ro (risk / 위험);
- hệ thống (system / 시스템)/electronic-trading thất bại (failure / 실패);
- unauthorized intermediaries;
- exaggerated return marketing.

This aligns with the mechanics studied in chapters 03 and 05.

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **15. Domestic license check** nối từ **14. Korea FX-margin rủi ro (risk / 위험) disclosures** sang **16. FX margin vs bank currency exchange**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Domestic license check

Before any real sản phẩm (product / 제품) use, verify:

```text
Exact Korean financial investment company
Permitted derivatives brokerage activity
Account agreement
Margin requirement
FDM / overseas counterparty structure
Remittance route
Investor-protection disclosures
```

Do not verify only brand/lĩnh vực (domain / 도메인).

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **16. FX margin vs bank currency exchange** nối từ **15. Domestic license check** sang **17. Korea research timeline break**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. FX margin vs bank currency exchange

Buying USD at a Korean bank for travel/savings is not the same sản phẩm (product / 제품) as leveraged FX-margin trading.

Different:

```text
purpose
settlement
leverage
legal category
intermediary
risk
```

Do not import FX-margin rules blindly into ordinary bank FX transactions.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **17. Korea research timeline break** nối từ **16. FX margin vs bank currency exchange** sang **18. USD/VND quote**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Korea research timeline break

For dữ liệu (data / 데이터) studies, mark structural dates such as:

```text
pre-RFI / old hours
→ RFI opening phase
→ July 2024 extended-hours regime
→ later rule/infrastructure changes
```

A chiến lược (strategy / 전략)'s session tác động (effect / 효과) may shift after thị trường (market / 시장) reform.

---

# Part II — Vietnam

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **18. USD/VND quote** nối từ **17. Korea research timeline break** sang **19. Official regulatory center**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. USD/VND quote

```text
USD/VND = VND per 1 USD
```

If USD/VND rises:

```text
VND weakens relative to USD
```

Vietnam FX khung phần mềm (framework / 프레임워크) has stronger administrative/regulatory cấu trúc (structure / 구조) than free-floating major pairs, so chính sách (policy / 정책) regime matters heavily.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **19. Official regulatory center** nối từ **18. USD/VND quote** sang **20. Authorized credit institutions**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Official regulatory center

The **Trạng thái (state / 상태) Bank of Vietnam (Ngân hàng Nhà nước Việt Nam, SBV)** is the central authority for foreign-exchange management.

Research should begin from:

- Ordinance on Foreign Exchange and amendments;
- implementing decrees;
- SBV circulars;
- hiện tại (current / 현재) official legal cơ sở dữ liệu (database / 데이터베이스).

Do not infer Vietnam rules from US/EU/Korean broker practices.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **20. Authorized credit institutions** nối từ **19. Official regulatory center** sang **21. Products in the domestic khung phần mềm (framework / 프레임워크)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Authorized credit institutions

Vietnam rules distinguish **tổ chức tín dụng được phép hoạt động ngoại hối — credit institutions authorized for FX activities**.

SBV Circular 02/2021/TT-NHNN khung phần mềm (framework / 프레임워크) governs foreign-currency transactions in the domestic FX thị trường (market / 시장) between authorized credit institutions and customers.

The circular defines customers to include resident/non-resident organizations and individuals, while giao dịch (transaction / 트랜잭션) permissions vary by customer kiểu (type / 타입) and purpose.

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **21. Products in the domestic khung phần mềm (framework / 프레임워크)** nối từ **20. Authorized credit institutions** sang **22. Resident individual transactions**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Products in the domestic khung phần mềm (framework / 프레임워크)

The regulatory definitions include categories such as:

- spot;
- forward;
- swap;
- options;

but permitted use depends on institution, customer category and regulatory conditions.

Do not assume that because a sản phẩm (product / 제품) kiểu (type / 타입) exists in banking regulation, a resident individual may freely use a foreign retail leveraged broker for speculative trading.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **22. Resident individual transactions** nối từ **21. Products in the domestic khung phần mềm (framework / 프레임워크)** sang **23. USD/VND pricing khung phần mềm (framework / 프레임워크)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Resident individual transactions

Under the SBV khung phần mềm (framework / 프레임워크) retrieved for this chapter, authorized credit institutions may conduct specified FX transactions with resident individuals, including spot and certain forward transactions according to applicable rules.

The legal/economic ngữ cảnh (context / 맥락) is generally tied to the regulated domestic FX hệ thống (system / 시스템) and lawful FX needs; it is not equivalent to an unrestricted toàn cục (global / 전역) retail CFD/FX account.

Before practical use, check the hiện tại (current / 현재) consolidated văn bản (text / 텍스트) and the bank's permitted services.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **23. USD/VND pricing khung phần mềm (framework / 프레임워크)** nối từ **22. Resident individual transactions** sang **24. Exchange-rate regime matters**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. USD/VND pricing khung phần mềm (framework / 프레임워크)

For domestic USD/VND transactions, SBV regulations link spot pricing to the official **central exchange tỷ lệ (rate / 비율) (tỷ giá trung tâm)** and the permitted trading band/regime in force.

Because the band/rules can thay đổi (change / 변경), this chapter intentionally does not freeze a hiện tại (current / 현재) percentage.

Research chuỗi xử lý (pipeline / 파이프라인) should phiên bản (version / 버전):

```text
central rate
band/regime
policy change dates
actual bank/interbank quotes
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **24. Exchange-rate regime matters** nối từ **23. USD/VND pricing khung phần mềm (framework / 프레임워크)** sang **25. Official vs free-market prices**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Exchange-rate regime matters

USD/VND should not be modeled exactly like EUR/USD.

Possible drivers include:

- SBV chính sách (policy / 정책) khung phần mềm (framework / 프레임워크);
- inflation/growth;
- trade balance;
- FDI;
- remittances;
- USD cycle;
- reserves/intervention;
- domestic liquidity/rates;
- capital-flow management.

Administrative rules can create nonlinear hành vi (behavior / 동작) near chính sách (policy / 정책) boundaries.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **25. Official vs free-market prices** nối từ **24. Exchange-rate regime matters** sang **26. Foreign-currency use onshore**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Official vs free-market prices

Vietnam historically has formal regulated FX channels and restrictions on unauthorized currency exchange.

For research, distinguish:

```text
official/interbank/bank quotes
licensed exchange channels
informal/free-market observations
```

Do not merge them into one clean price series without labeling nguồn (source / 소스)/legal ngữ cảnh (context / 맥락).

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **26. Foreign-currency use onshore** nối từ **25. Official vs free-market prices** sang **27. Unauthorized exchange rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Foreign-currency use onshore

Vietnam's foreign-exchange legal khung phần mềm (framework / 프레임워크) restricts use of foreign currency within Vietnamese territory except permitted cases.

This affects:

- payments;
- quoting;
- settlement;
- account use.

It is a monetary/legal khung phần mềm (framework / 프레임워크), not just a broker quy tắc (rule / 규칙).

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **27. Unauthorized exchange rủi ro (risk / 위험)** nối từ **26. Foreign-currency use onshore** sang **28. Overseas retail Forex/CFD caution for Vietnam residents**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Unauthorized exchange rủi ro (risk / 위험)

Hiện tại (current / 현재) Vietnamese administrative-sanction rules include penalties for certain unauthorized foreign-currency buying/selling and transactions outside permitted entities/channels.

Therefore “I can find someone/app to exchange/trade” is not equivalent to a legally permitted channel.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **28. Overseas retail Forex/CFD caution for Vietnam residents** nối từ **27. Unauthorized exchange rủi ro (risk / 위험)** sang **29. International Financial Center developments**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Overseas retail Forex/CFD caution for Vietnam residents

For this thư viện (library / 라이브러리), do **not** trạng thái (state / 상태) a blanket simple quy tắc (rule / 규칙) such as “all Forex is legal” or “all Forex is illegal”. The legal kết quả (result / 결과) depends on:

```text
resident status
product
counterparty
remittance route
purpose
licensed activity
foreign-exchange controls
```

What is clear from the domestic khung phần mềm (framework / 프레임워크) is that Vietnam tightly regulates foreign-exchange activities and designates authorized institutions/channels.

Before sending funds to an overseas FX/CFD nền tảng (platform / 플랫폼), a Vietnam resident should verify hiện tại (current / 현재) SBV/foreign-exchange rules and legal remittance purpose rather than rely on broker marketing.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **29. International Financial Center developments** nối từ **28. Overseas retail Forex/CFD caution for Vietnam residents** sang **30. VND is not just a high-yield/low-yield currency tín hiệu (signal / 신호)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. International Financial Center developments

Vietnam introduced specific 2025 rules for the **International Financial Center (IFC)**, including Decree 329/2025/NĐ-CP and SBV Circular 72/2025/TT-NHNN concerning foreign-exchange/account matters inside that special khung phần mềm (framework / 프레임워크).

Important:

```text
IFC-specific rule
≠ automatic nationwide retail rule
```

Always check phạm vi (scope / 범위), eligible thực thể (entity / 엔터티) and effective provisions.

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **30. VND is not just a high-yield/low-yield currency tín hiệu (signal / 신호)** nối từ **29. International Financial Center developments** sang **31. Vietnam corporate hedging**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. VND is not just a high-yield/low-yield currency tín hiệu (signal / 신호)

Because of chính sách (policy / 정책) regime and capital-flow khung phần mềm (framework / 프레임워크), simple carry các mô hình (models / 모델들) from freely traded G10 FX can thất bại (fail / 실패).

Need mô hình (model / 모델):

```text
policy band / intervention
onshore liquidity
capital controls / convertibility constraints
forward market access
hedging instruments
```

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **31. Vietnam corporate hedging** nối từ **30. VND is not just a high-yield/low-yield currency tín hiệu (signal / 신호)** sang **32. Korea–Vietnam nghiệp vụ (business / 비즈니스) exposure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Vietnam corporate hedging

Import/export businesses may have genuine FX exposures:

```text
USD receivables
USD payables
foreign-currency debt
```

Authorized banks can provide permitted FX products under regulation.

Corporate hedge mục tiêu (objective / 목표) should be cash-flow rủi ro (risk / 위험) management, not evaluated as standalone speculative P/L.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **32. Korea–Vietnam nghiệp vụ (business / 비즈니스) exposure** nối từ **31. Vietnam corporate hedging** sang **33. Triangular exposure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Korea–Vietnam nghiệp vụ (business / 비즈니스) exposure

For a Korea-linked company operating in Vietnam, economic exposures may include:

```text
KRW
USD
VND
```

Even if invoice currency is USD, costs/revenue may be VND and reporting currency KRW.

Need map all three layers.

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **33. Triangular exposure** nối từ **32. Korea–Vietnam nghiệp vụ (business / 비즈니스) exposure** sang **34. Giao dịch (transaction / 트랜잭션) exposure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Triangular exposure

Example:

```text
Vietnam subsidiary earns VND
purchases imported inputs in USD
parent reports in KRW
```

Rủi ro (risk / 위험) cannot be summarized by one USD/VND chart.

Need analyze:

```text
transaction exposure
translation exposure
economic exposure
```

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **34. Giao dịch (transaction / 트랜잭션) exposure** nối từ **33. Triangular exposure** sang **35. Translation exposure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Giao dịch (transaction / 트랜잭션) exposure

Contractual cash luồng (flow / 흐름) in foreign currency.

Example: USD payable in 90 days.

Can be hedged with permitted forward/other instrument where legally/operationally available.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **35. Translation exposure** nối từ **34. Giao dịch (transaction / 트랜잭션) exposure** sang **36. Economic exposure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Translation exposure

Financial statements of foreign subsidiary converted into parent reporting currency.

This accounting exposure differs from cash giao dịch (transaction / 트랜잭션) rủi ro (risk / 위험).

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **36. Economic exposure** nối từ **35. Translation exposure** sang **37. Research nguồn (source / 소스) hierarchy for Korea**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Economic exposure

Long-run nghiệp vụ (business / 비즈니스) competitiveness changes when FX changes.

Example: KRW/VND/USD shifts thay đổi (change / 변경) relative labor/đầu vào (input / 입력)/export economics even without tường minh (explicit / 명시적) FX payable.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **36. Economic exposure** đặt vấn đề; **37. Research nguồn (source / 소스) hierarchy for Korea** đối chiếu bằng chứng, rồi **38. Research nguồn (source / 소스) hierarchy for Vietnam** mở rộng hệ quả hoặc giới hạn liên quan.

## 37. Research nguồn (source / 소스) hierarchy for Korea

Prefer:

```text
Bank of Korea
Ministry of Economy and Finance
Financial Services Commission / Financial Supervisory Service
KOFIA
KRX / licensed intermediaries
```

Then high-quality secondary phân tích (analysis / 분석).

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **37. Research nguồn (source / 소스) hierarchy for Korea** đặt vấn đề; **38. Research nguồn (source / 소스) hierarchy for Vietnam** đối chiếu bằng chứng, rồi **39. Regulatory versioning** mở rộng hệ quả hoặc giới hạn liên quan.

## 38. Research nguồn (source / 소스) hierarchy for Vietnam

Prefer:

```text
State Bank of Vietnam
National legal database / official government legal texts
Ministry/Government decrees
Authorized bank official product terms
```

Do not use affiliate broker websites as legal nguồn (source / 소스).

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **38. Research nguồn (source / 소스) hierarchy for Vietnam** đặt vấn đề; **39. Regulatory versioning** đối chiếu bằng chứng, rồi **40. Broker/sản phẩm (product / 제품) checklist for a Korea resident** mở rộng hệ quả hoặc giới hạn liên quan.

## 39. Regulatory versioning

For every regulatory ghi chú (note / 노트), store:

```text
source URL
publication date
effective date
retrieval date
scope
whether amended/repealed/consolidated
```

This is especially important because FX controls evolve.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **40. Broker/sản phẩm (product / 제품) checklist for a Korea resident** nối từ **39. Regulatory versioning** sang **41. Sản phẩm (product / 제품) checklist for a Vietnam resident**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Broker/sản phẩm (product / 제품) checklist for a Korea resident

```text
Is this FX-margin, futures, CFD, or currency conversion?
Which Korean legal category?
Which domestic licensed intermediary?
Is direct overseas dealing permitted for this route?
How are funds remitted?
What margin/protection applies?
What is the exact foreign counterparty?
```

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **41. Sản phẩm (product / 제품) checklist for a Vietnam resident** nối từ **40. Broker/sản phẩm (product / 제품) checklist for a Korea resident** sang **42. Do not treat regulation as static chiến lược (strategy / 전략) edge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. Sản phẩm (product / 제품) checklist for a Vietnam resident

```text
What is the lawful FX purpose?
Which authorized institution?
Which product is permitted for this customer type?
What account/remittance rule applies?
Is an overseas account/platform legally fundable for this activity?
What reporting/document requirements exist?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **42. Do not treat regulation as static chiến lược (strategy / 전략) edge** nối từ **41. Sản phẩm (product / 제품) checklist for a Vietnam resident** sang **43. Korea/Vietnam chapter is ngữ cảnh (context / 맥락), not recommendation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Do not treat regulation as static chiến lược (strategy / 전략) edge

A pricing anomaly caused by truy cập (access / 접근) restriction can disappear after reform.

Examples:

- Korea RFI truy cập (access / 접근);
- extended trading hours;
- new special financial-center khung phần mềm (framework / 프레임워크) in Vietnam.

Structural thay đổi (change / 변경) should be a breakpoint in backtest.

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **43. Korea/Vietnam chapter is ngữ cảnh (context / 맥락), not recommendation** nối từ **42. Do not treat regulation as static chiến lược (strategy / 전략) edge** sang **44. Final học tập (learning / 학습) checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. Korea/Vietnam chapter is ngữ cảnh (context / 맥락), not recommendation

This chapter should answer:

```text
What market am I observing?
Who can participate?
Which instrument is legal/available?
Which policy framework shapes the price?
Which data discontinuities matter?
```

It should not rank brokers or tell the reader to open a leveraged account.

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **44. Final học tập (learning / 학습) checklist** nối từ **43. Korea/Vietnam chapter is ngữ cảnh (context / 맥락), not recommendation** sang **Sources — Korea**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. Final học tập (learning / 학습) checklist

After the full Forex đường dẫn (path / 경로), you should be able to explain:

1. Why FX is a relative price.
2. OTC vs exchange thị trường (market / 시장) cấu trúc (structure / 구조).
3. Spot/forward/swap/futures/options differences.
4. Pips/lots/notional/P&L.
5. Margin/leverage/position sizing.
6. Relative macro and carry.
7. Price hành động (action / 동작)/indicator limitations.
8. Event-study and point-in-time research.
9. Chiến lược (strategy / 전략) families and robustness.
10. Currency/factor portfolio rủi ro (risk / 위험).
11. Journal and attribution.
12. Microstructure/thứ tự (order / 순서) luồng (flow / 흐름).
13. FX options/volatility.
14. Why Korea and Vietnam require jurisdiction-specific thị trường (market / 시장)/regulatory các mô hình (models / 모델들).

> **Nối mạch:** Đặt trong câu hỏi lớn của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **44. Final học tập (learning / 학습) checklist** đặt vấn đề; **Sources — Korea** đối chiếu bằng chứng, rồi **Sources — Vietnam** mở rộng hệ quả hoặc giới hạn liên quan.

## Sources — Korea

- Bank of Korea — FX Thị trường (market / 시장) Cấu trúc (structure / 구조) Improvement Portal: https://www.bok.or.kr/portal/main/contents.do?menuNo=201250
- Bank of Korea — Improvement Measure of FX Thị trường (market / 시장) Cấu trúc (structure / 구조): https://www.bok.or.kr/eng/main/contents.do?menuNo=400416
- Bank of Korea — Registered Foreign Institutions danh sách (list / 목록): https://www.bok.or.kr/eng/bbs/B0000367/view.do?menuNo=400489&nttId=10082323
- Bank of Korea — Seoul FX Thị trường (market / 시장) / FX Toàn cục (global / 전역) Mã (code / 코드) materials: https://www.bok.or.kr/eng/main/contents.do?menuNo=400365
- Korea Financial Investment Association — FX Margin definition/cấu trúc (structure / 구조): https://www.kofia.or.kr/wpge/m_73/sub03040401.do
- Korea Financial Investment Association — FX Margin investor precautions: https://www.kofia.or.kr/wpge/m_74/sub03040402.do
- Korea Financial Investment Association — Illegal FX Margin giao dịch (transaction / 트랜잭션) types: https://www.kofia.or.kr/wpge/m_75/sub03040403.do
- Bank of Korea — Foreign Exchange Giao dịch (transaction / 트랜잭션) Regulations / hiện tại (current / 현재) rules portal: https://www.bok.or.kr/portal/bbs/P0002014/view.do?menuNo=200402

> **Nối mạch:** Trong **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **Sources — Korea** đặt vấn đề; **Sources — Vietnam** đối chiếu bằng chứng, rồi **Nội bộ (internal / 내부) links** mở rộng hệ quả hoặc giới hạn liên quan.

## Sources — Vietnam

- Trạng thái (state / 상태) Bank of Vietnam / National Legal Cơ sở dữ liệu (database / 데이터베이스) — Circular 02/2021/TT-NHNN and hiện tại (current / 현재) related legal texts: https://vbpl.moj.gov.vn/nganhangnhanuoc/Pages/vbpq-toanvan.aspx?ItemID=147142
- Ordinance / legal khung phần mềm (framework / 프레임워크) on foreign exchange and implementing regulations via official national legal cơ sở dữ liệu (database / 데이터베이스): https://vbpl.moj.gov.vn/
- Government Decree 329/2025/NĐ-CP — International Financial Center FX/banking khung phần mềm (framework / 프레임워크): https://vbpl.vn/TW/Pages/vbpq-print.aspx?ItemID=185119
- SBV Circular 72/2025/TT-NHNN — accounts for FX activities in Vietnam International Financial Center: https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=185798

> **Nối mạch:** Ở chặng này của **15 — Korea / Vietnam FX thị trường (market / 시장) ngữ cảnh (context / 맥락) và regulations**, **Sources — Vietnam** đặt vấn đề; **Nội bộ (internal / 내부) links** đối chiếu bằng chứng. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [06 — Markets Korea/Vietnam](../../06_markets_korea_vietnam/README.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
