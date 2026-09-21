# Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam

> File này là bản đồ kiến thức cho domain `06_markets_korea_vietnam/`. Mục tiêu là giúp người đọc định vị **cấu trúc thị trường, biến vĩ mô, ngành trọng yếu, dòng vốn và rủi ro triển khai** trước khi đi vào các playbook chuyên sâu.

> **Lưu ý về dữ liệu động:** lãi suất chính sách, thuế, chu kỳ thanh toán, quy định short-selling, foreign room, điều kiện market access, thành phần chỉ số và quy định sản phẩm có thể thay đổi. Các thông tin này phải được kiểm tra lại theo nguồn chính thức tại thời điểm sử dụng; không coi snapshot lịch sử là quy tắc vĩnh viễn.

# Phần I — Mental model chung

## 1. Không phân tích thị trường chỉ bằng chỉ số

KOSPI, KOSDAQ hay VN-Index chỉ là một lớp.

Một nghiên cứu đầy đủ nên đi theo:

```text
Global Macro
→ Country Macro
→ Currency
→ Credit / Liquidity
→ Sector
→ Company
→ Valuation
→ Market Access / Wrapper
→ Position
→ Monitoring
```

## 2. Hàn Quốc và Việt Nam khác nhau ở đâu?

Hàn Quốc có thị trường vốn lớn hơn, tính quốc tế hóa cao hơn và tỷ trọng các doanh nghiệp xuất khẩu toàn cầu rất lớn.

Việt Nam có vai trò nổi bật của nhà đầu tư nội địa, ngân hàng, bất động sản, FDI và chu kỳ tín dụng trong nước.

Do đó cùng một Fed shock có thể truyền vào hai thị trường theo kênh khác nhau.

# Phần II — Hàn Quốc

## 3. Hạ tầng thị trường

Các tên quan trọng cần nhận diện gồm:

- KRX — Korea Exchange;
- KOSPI;
- KOSDAQ;
- KONEX;
- KOSPI 200;
- KSD — Korea Securities Depository;
- FSC/FSS trong hệ thống giám sát tài chính.

Mỗi thị trường và sản phẩm có quy tắc giao dịch, settlement và access riêng; phải kiểm tra specification hiện hành khi giao dịch thật.

## 4. Đặc điểm kinh tế Hàn Quốc

Hàn Quốc là nền kinh tế:

- định hướng xuất khẩu;
- nhập khẩu nhiều năng lượng;
- có ngành bán dẫn rất lớn;
- nhạy với China cycle;
- nhạy với USD/KRW;
- có household debt đáng kể.

## 5. KRW

KRW có thể chịu ảnh hưởng bởi:

```text
Fed / US Yields
Korea–US Rate Differential
Exports
Semiconductor Cycle
Oil
China
Foreign Flows
Risk Sentiment
```

Không nên dùng một biến đơn lẻ để dự đoán USD/KRW.

## 6. BOK

Bank of Korea (BOK) điều hành policy rate trong bối cảnh phải cân bằng:

- inflation;
- growth;
- financial stability;
- household debt;
- FX conditions.

Mức policy rate hiện tại luôn phải kiểm tra từ BOK khi cần dữ liệu mới nhất.

## 7. Semiconductor

Bán dẫn là một trong những kênh quan trọng nhất nối Korea với global technology cycle.

Chuỗi cơ bản:

```text
Global IT / AI Demand
→ Inventory
→ ASP
→ Utilization
→ HBM / Product Mix
→ Capex
→ Earnings Revisions
→ KOSPI / KRW / Suppliers
```

## 8. Các ngành Hàn Quốc cần theo dõi

Ngoài semiconductor:

- autos/EV;
- batteries;
- shipbuilding;
- defense/industrials;
- banks/insurance/brokers;
- internet platforms;
- gaming;
- biotech;
- construction;
- refining/petrochemicals;
- utilities;
- retail/consumer brands.

# Phần III — Việt Nam

## 9. Hạ tầng thị trường

Các tên chính:

- HOSE;
- HNX;
- UPCoM;
- VNX;
- VSDC;
- VN-Index;
- VN30;
- VN30 futures.

Chu kỳ thanh toán, biên độ giá, foreign access và product rules có thể thay đổi nên phải kiểm tra theo HOSE/HNX/VSDC/SSC hoặc nguồn chính thức tương ứng.

## 10. Đặc điểm kinh tế Việt Nam

Các động lực lớn gồm:

- domestic credit;
- property cycle;
- FDI;
- manufacturing exports;
- public investment;
- household savings;
- VND stability.

## 11. SBV và VND

State Bank of Vietnam (SBV) phải cân bằng:

```text
Growth
Inflation
Banking Liquidity
Credit
USD/VND Stability
```

Vì vậy room nới lỏng trong nước không hoàn toàn độc lập với global USD conditions.

## 12. Ngân hàng

Các KPI quan trọng:

- credit growth;
- NIM;
- CASA;
- NPL;
- Group-2;
- provision coverage;
- credit cost;
- capital adequacy;
- property exposure.

## 13. Bất động sản

Cần đọc theo chuỗi:

```text
Legal Status
→ Presales
→ Cash Collection
→ Debt / Bond Maturity
→ Refinancing
→ Construction
→ Handover
→ Revenue / Cash Flow
```

Land bank lớn không tự động nghĩa giá trị có thể hiện thực hóa ngay.

## 14. Các ngành Việt Nam quan trọng

Ngoài bank/property:

- securities companies;
- industrial parks;
- retail/consumer;
- public-investment beneficiaries;
- ports/logistics;
- aviation;
- energy/utilities;
- steel/cement;
- technology services;
- telecom;
- agriculture/chemicals.

# Phần IV — So sánh Hàn Quốc và Việt Nam

## 15. Global sensitivity

Hàn Quốc thường phản ứng nhanh hơn với:

- global tech cycle;
- foreign institutional flows;
- global rates;
- KRW.

Việt Nam thường có thêm lớp rất quan trọng từ:

- domestic liquidity;
- deposit rates;
- retail margin;
- property-bank cycle;
- local regulation.

## 16. Fed shock

Một chain tổng quát:

```text
US Yields ↑
→ USD ↑
→ KRW / VND Pressure
→ Local Financial Conditions
→ Foreign / Domestic Flows
→ Sector Earnings / Multiples
```

Cường độ khác nhau tùy từng thị trường.

## 17. China shock

China slowdown có thể ảnh hưởng Korea qua exports/semiconductors/industrials và ảnh hưởng Vietnam qua trade, manufacturing supply chain, commodities và FDI dynamics.

## 18. Oil shock

Hàn Quốc là energy importer lớn nên oil shock có thể tác động terms of trade mạnh.

Việt Nam có cấu trúc năng lượng khác và tác động cần tách theo upstream/downstream, fiscal pricing và inflation.

# Phần V — Dòng vốn và breadth

## 19. Index move không bằng market breadth

Chỉ số tăng nhờ vài large caps khác hoàn toàn một rally có nhiều cổ phiếu cùng tham gia.

Theo dõi:

- advance/decline;
- volume;
- sector breadth;
- equal-weight vs cap-weight nếu có dữ liệu.

## 20. Foreign flow

Foreign buying/selling có thể ảnh hưởng price mạnh ở một số giai đoạn nhưng không nên được xem là “smart money” mặc định.

Dòng vốn có thể đến từ:

- passive rebalance;
- FX hedge;
- global risk reduction;
- country allocation;
- company view.

## 21. Domestic liquidity

Ở Việt Nam, domestic deposit rate, margin balance và retail turnover có thể ảnh hưởng mạnh đến market multiple.

Ở Hàn Quốc, household flows, pension/institutional flows và ETF/futures mechanics cũng đáng chú ý.

# Phần VI — ETF, ETN và derivatives

## 22. Wrapper không phải underlying

ETF/ETN niêm yết bằng KRW không đồng nghĩa exposure kinh tế là KRW.

Cần tách:

```text
Listing Currency
Underlying Currency
Economic Exposure
Hedge Policy
```

## 23. Futures

Futures giúp hedge beta hoặc trade index nhưng phải hiểu:

- multiplier;
- margin;
- expiry;
- basis;
- roll;
- settlement.

## 24. Leveraged/inverse products

Daily-reset product có path dependency.

Không nên ngoại suy `2× daily` thành `2× long-term`.

# Phần VII — Cross-border investing

## 25. Bốn lớp tiền tệ

Khi đầu tư đa quốc gia cần phân biệt:

```text
Trading Currency
Underlying Economic Currency
Reporting / Home Currency
Liability Currency
```

## 26. Wrapper và legal claim

Cùng một exposure có thể mua qua:

- local ETF;
- direct foreign security;
- depositary receipt;
- fund;
- derivative.

Mỗi wrapper có tax, custody, settlement, liquidity và legal claim khác nhau.

## 27. Thuế và access

Không hard-code mức thuế, ISA limit, withholding rate hay foreign-access rule trong knowledge base dài hạn.

Khi ra quyết định thật phải kiểm tra:

- tax residency;
- treaty;
- withholding;
- account wrapper;
- broker legal entity;
- market access hiện hành.

# Phần VIII — Quy trình research

## 28. Company research

```text
Business Model
→ Sector Driver
→ Financial Statements
→ Balance Sheet
→ Earnings Revision
→ Valuation
→ Catalyst / Invalidation
```

## 29. Market research

```text
Macro
→ FX
→ Rates / Credit
→ Flow / Breadth
→ Sector Leadership
→ Earnings
→ Valuation
```

## 30. Source hierarchy

Ưu tiên:

```text
Official Regulator / Exchange / Central Bank
→ Filing / Company Disclosure
→ IR / Transcript
→ High-Quality Data Provider
→ Broker Research
→ News
→ Social Media
```

# Phần IX — Các chapter chuyên sâu

Đọc tiếp:

- [01_KOREA_MARKET_PLAYBOOK.md](./01_KOREA_MARKET_PLAYBOOK.md)
- [02_VIETNAM_MARKET_PLAYBOOK.md](./02_VIETNAM_MARKET_PLAYBOOK.md)
- [03_CROSS_MARKET_GLOBAL_SHOCKS.md](./03_CROSS_MARKET_GLOBAL_SHOCKS.md)
- [04_MARKET_RESEARCH_WORKFLOW_DATA_SOURCES_AND_SECTOR_MAPS.md](./04_MARKET_RESEARCH_WORKFLOW_DATA_SOURCES_AND_SECTOR_MAPS.md)
- [05_CROSS_BORDER_INVESTING_CURRENCY_TAX_WRAPPERS_AND_MARKET_ACCESS.md](./05_CROSS_BORDER_INVESTING_CURRENCY_TAX_WRAPPERS_AND_MARKET_ACCESS.md)
- [06_SECTOR_DEEP_DIVES_KOREA_VIETNAM.md](./06_SECTOR_DEEP_DIVES_KOREA_VIETNAM.md)

## Kết luận

Không nên học Korea/Vietnam market như hai danh sách ticker hoặc chỉ số.

Mục tiêu là có thể nối:

```text
Global Shock
→ Country Macro
→ Currency / Credit / Liquidity
→ Sector
→ Company Earnings
→ Valuation
→ Market Access / Wrapper
→ Position Risk
```

và luôn phân biệt **kiến thức cơ chế lâu dài** với **quy định/dữ liệu động cần kiểm tra lại tại thời điểm sử dụng**.
