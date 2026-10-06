# Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Không phân tích thị trường chỉ bằng chỉ số** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Hàn Quốc và Việt Nam khác nhau ở đâu?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của master Korea–Vietnam, rồi nối kinh tế, thị trường, ngành và rủi ro xuyên biên giới.

> tệp (file / 파일) này là bản đồ kiến thức cho lĩnh vực (domain / 도메인) `06_markets_korea_vietnam/`. Mục tiêu là giúp người đọc định vị **cấu trúc thị trường, biến vĩ mô, ngành trọng yếu, dòng vốn và rủi ro triển khai** trước khi đi vào các playbook chuyên sâu.

> **Lưu ý về dữ liệu động:** lãi suất chính sách, thuế, chu kỳ thanh toán, quy định short-selling, foreign room, điều kiện thị trường (market / 시장) truy cập (access / 접근), thành phần chỉ số và quy định sản phẩm có thể thay đổi. Các thông tin này phải được kiểm tra lại theo nguồn chính thức tại thời điểm sử dụng; không coi snapshot lịch sử là quy tắc vĩnh viễn.

# Phần I — mô hình tư duy (mental model / 사고 모델) chung

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

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **2. Hàn Quốc và Việt Nam khác nhau ở đâu?** nối từ **1. Không phân tích thị trường chỉ bằng chỉ số** sang **3. Hạ tầng thị trường**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Hàn Quốc và Việt Nam khác nhau ở đâu?

Hàn Quốc có thị trường vốn lớn hơn, tính quốc tế hóa cao hơn và tỷ trọng các doanh nghiệp xuất khẩu toàn cầu rất lớn.

Việt Nam có vai trò nổi bật của nhà đầu tư nội địa, ngân hàng, bất động sản, FDI và chu kỳ tín dụng trong nước.

Do đó cùng một Fed shock có thể truyền vào hai thị trường theo kênh khác nhau.

# Phần II — Hàn Quốc

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **3. Hạ tầng thị trường** nối từ **2. Hàn Quốc và Việt Nam khác nhau ở đâu?** sang **4. Đặc điểm kinh tế Hàn Quốc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Hạ tầng thị trường

Các tên quan trọng cần nhận diện gồm:

- KRX — Korea Exchange;
- KOSPI;
- KOSDAQ;
- KONEX;
- KOSPI 200;
- KSD — Korea Securities Depository;
- FSC/FSS trong hệ thống giám sát tài chính.

Mỗi thị trường và sản phẩm có quy tắc giao dịch, settlement và truy cập (access / 접근) riêng; phải kiểm tra specification hiện hành khi giao dịch thật.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **4. Đặc điểm kinh tế Hàn Quốc** nối từ **3. Hạ tầng thị trường** sang **5. KRW**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Đặc điểm kinh tế Hàn Quốc

Hàn Quốc là nền kinh tế:

- định hướng xuất khẩu;
- nhập khẩu nhiều năng lượng;
- có ngành bán dẫn rất lớn;
- nhạy với China cycle;
- nhạy với USD/KRW;
- có household debt đáng kể.

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **5. KRW** nối từ **4. Đặc điểm kinh tế Hàn Quốc** sang **6. BOK**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **6. BOK** nối từ **5. KRW** sang **7. Semiconductor**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. BOK

Bank of Korea (BOK) điều hành chính sách (policy / 정책) tỷ lệ (rate / 비율) trong bối cảnh phải cân bằng:

- inflation;
- growth;
- financial stability;
- household debt;
- FX conditions.

Mức chính sách (policy / 정책) tỷ lệ (rate / 비율) hiện tại luôn phải kiểm tra từ BOK khi cần dữ liệu mới nhất.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **7. Semiconductor** nối từ **6. BOK** sang **8. Các ngành Hàn Quốc cần theo dõi**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Semiconductor

Bán dẫn là một trong những kênh quan trọng nhất nối Korea với toàn cục (global / 전역) technology cycle.

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

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **8. Các ngành Hàn Quốc cần theo dõi** nối từ **7. Semiconductor** sang **9. Hạ tầng thị trường**, vì cơ chế trước tạo đầu vào cho bước sau.

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
- retail/bên tiêu thụ (consumer / 소비자) brands.

# Phần III — Việt Nam

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **9. Hạ tầng thị trường** nối từ **8. Các ngành Hàn Quốc cần theo dõi** sang **10. Đặc điểm kinh tế Việt Nam**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Chu kỳ thanh toán, biên độ giá, foreign truy cập (access / 접근) và sản phẩm (product / 제품) rules có thể thay đổi nên phải kiểm tra theo HOSE/HNX/VSDC/SSC hoặc nguồn chính thức tương ứng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **10. Đặc điểm kinh tế Việt Nam** nối từ **9. Hạ tầng thị trường** sang **11. SBV và VND**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Đặc điểm kinh tế Việt Nam

Các động lực lớn gồm:

- domestic credit;
- thuộc tính (property / 속성) cycle;
- FDI;
- manufacturing exports;
- công khai (public / 공개) investment;
- household savings;
- VND stability.

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **11. SBV và VND** nối từ **10. Đặc điểm kinh tế Việt Nam** sang **12. Ngân hàng**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. SBV và VND

Trạng thái (state / 상태) Bank of Vietnam (SBV) phải cân bằng:

```text
Growth
Inflation
Banking Liquidity
Credit
USD/VND Stability
```

Vì vậy room nới lỏng trong nước không hoàn toàn độc lập với toàn cục (global / 전역) USD conditions.

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **12. Ngân hàng** nối từ **11. SBV và VND** sang **13. Bất động sản**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Ngân hàng

Các KPI quan trọng:

- credit growth;
- NIM;
- CASA;
- NPL;
- Group-2;
- provision coverage;
- credit chi phí (cost / 비용);
- capital adequacy;
- thuộc tính (property / 속성) exposure.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **13. Bất động sản** nối từ **12. Ngân hàng** sang **14. Các ngành Việt Nam quan trọng**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **14. Các ngành Việt Nam quan trọng** nối từ **13. Bất động sản** sang **15. toàn cục (global / 전역) sensitivity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Các ngành Việt Nam quan trọng

Ngoài bank/thuộc tính (property / 속성):

- securities companies;
- industrial parks;
- retail/bên tiêu thụ (consumer / 소비자);
- public-investment beneficiaries;
- ports/logistics;
- aviation;
- năng lượng (energy / 에너지)/utilities;
- steel/cement;
- technology services;
- telecom;
- agriculture/chemicals.

# Phần IV — So sánh Hàn Quốc và Việt Nam

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **15. toàn cục (global / 전역) sensitivity** nối từ **14. Các ngành Việt Nam quan trọng** sang **16. Fed shock**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. toàn cục (global / 전역) sensitivity

Hàn Quốc thường phản ứng nhanh hơn với:

- toàn cục (global / 전역) tech cycle;
- foreign institutional flows;
- toàn cục (global / 전역) rates;
- KRW.

Việt Nam thường có thêm lớp rất quan trọng từ:

- domestic liquidity;
- deposit rates;
- retail margin;
- property-bank cycle;
- cục bộ (local / 로컬) regulation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **16. Fed shock** nối từ **15. toàn cục (global / 전역) sensitivity** sang **17. China shock**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Fed shock

Một chuỗi (chain / 사슬) tổng quát:

```text
US Yields ↑
→ USD ↑
→ KRW / VND Pressure
→ Local Financial Conditions
→ Foreign / Domestic Flows
→ Sector Earnings / Multiples
```

Cường độ khác nhau tùy từng thị trường.

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **17. China shock** nối từ **16. Fed shock** sang **18. Oil shock**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. China shock

China slowdown có thể ảnh hưởng Korea qua exports/semiconductors/industrials và ảnh hưởng Vietnam qua trade, manufacturing supply chuỗi (chain / 사슬), commodities và FDI dynamics.

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **18. Oil shock** nối từ **17. China shock** sang **19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Oil shock

Hàn Quốc là năng lượng (energy / 에너지) importer lớn nên oil shock có thể tác động terms of trade mạnh.

Việt Nam có cấu trúc năng lượng khác và tác động cần tách theo upstream/downstream, fiscal pricing và inflation.

# Phần V — Dòng vốn và breadth

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth** nối từ **18. Oil shock** sang **20. Foreign luồng (flow / 흐름)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth

Chỉ số tăng nhờ vài large caps khác hoàn toàn một rally có nhiều cổ phiếu cùng tham gia.

Theo dõi:

- advance/decline;
- volume;
- sector breadth;
- equal-weight vs cap-weight nếu có dữ liệu.

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth** đặt đầu vào cho **20. Foreign luồng (flow / 흐름)**, rồi **21. Domestic liquidity** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. Foreign luồng (flow / 흐름)

Foreign buying/selling có thể ảnh hưởng price mạnh ở một số giai đoạn nhưng không nên được xem là “smart money” mặc định.

Dòng vốn có thể đến từ:

- passive rebalance;
- FX hedge;
- toàn cục (global / 전역) rủi ro (risk / 위험) reduction;
- country allocation;
- company view.

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **20. Foreign luồng (flow / 흐름)** đặt đầu vào cho **21. Domestic liquidity**, rồi **22. Wrapper không phải underlying** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. Domestic liquidity

Ở Việt Nam, domestic deposit tỷ lệ (rate / 비율), margin balance và retail turnover có thể ảnh hưởng mạnh đến thị trường (market / 시장) multiple.

Ở Hàn Quốc, household flows, pension/institutional flows và ETF/futures mechanics cũng đáng chú ý.

# Phần VI — ETF, ETN và derivatives

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **22. Wrapper không phải underlying** nối từ **21. Domestic liquidity** sang **23. Futures**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Wrapper không phải underlying

ETF/ETN niêm yết bằng KRW không đồng nghĩa exposure kinh tế là KRW.

Cần tách:

```text
Listing Currency
Underlying Currency
Economic Exposure
Hedge Policy
```

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **23. Futures** nối từ **22. Wrapper không phải underlying** sang **24. Leveraged/inverse products**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Futures

Futures giúp hedge beta hoặc trade chỉ mục (index / 인덱스) nhưng phải hiểu:

- multiplier;
- margin;
- expiry;
- basis;
- roll;
- settlement.

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **24. Leveraged/inverse products** nối từ **23. Futures** sang **25. Bốn lớp tiền tệ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Leveraged/inverse products

Daily-reset sản phẩm (product / 제품) có đường dẫn (path / 경로) phụ thuộc (dependency / 의존성).

Không nên ngoại suy `2× daily` thành `2× long-term`.

# Phần VII — Cross-border investing

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **25. Bốn lớp tiền tệ** nối từ **24. Leveraged/inverse products** sang **26. Wrapper và legal claim**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Bốn lớp tiền tệ

Khi đầu tư đa quốc gia cần phân biệt:

```text
Trading Currency
Underlying Economic Currency
Reporting / Home Currency
Liability Currency
```

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **26. Wrapper và legal claim** nối từ **25. Bốn lớp tiền tệ** sang **27. Thuế và truy cập (access / 접근)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Wrapper và legal claim

Cùng một exposure có thể mua qua:

- cục bộ (local / 로컬) ETF;
- direct foreign bảo mật (security / 보안);
- depositary receipt;
- fund;
- derivative.

Mỗi wrapper có tax, custody, settlement, liquidity và legal claim khác nhau.

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **27. Thuế và truy cập (access / 접근)** nối từ **26. Wrapper và legal claim** sang **28. Company research**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Thuế và truy cập (access / 접근)

Không hard-code mức thuế, ISA limit, withholding tỷ lệ (rate / 비율) hay foreign-access quy tắc (rule / 규칙) trong kiến thức (knowledge / 지식) cơ sở (base / 기반) dài hạn.

Khi ra quyết định thật phải kiểm tra:

- tax residency;
- treaty;
- withholding;
- account wrapper;
- broker legal thực thể (entity / 엔터티);
- thị trường (market / 시장) truy cập (access / 접근) hiện hành.

# Phần VIII — Quy trình research

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **28. Company research** nối từ **27. Thuế và truy cập (access / 접근)** sang **29. thị trường (market / 시장) research**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Company research

Sau khi đặt country/sector map, company research đi từ dữ liệu vận hành, bảng cân đối và exposure tiền tệ tới định giá và liquidity-aware sizing. Sơ đồ dưới đây là trình tự đánh giá, không phải danh sách file để đọc rời rạc.

```text
Business Model
→ Sector Driver
→ Financial Statements
→ Balance Sheet
→ Earnings Revision
→ Valuation
→ Catalyst / Invalidation
```

> **Nối mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **29. thị trường (market / 시장) research** nối từ **28. Company research** sang **30. nguồn (source / 소스) hierarchy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. thị trường (market / 시장) research

Market research nối dữ liệu vĩ mô, flow, breadth, valuation và access rules thành một thesis có thể review. Hãy dùng sơ đồ để biết câu hỏi nào cần trả lời trước khi chọn cổ phiếu hoặc vị thế xuyên biên giới.

```text
Macro
→ FX
→ Rates / Credit
→ Flow / Breadth
→ Sector Leadership
→ Earnings
→ Valuation
```

> **Nối mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **29. thị trường (market / 시장) research** đặt vấn đề; **30. nguồn (source / 소스) hierarchy** đối chiếu bằng chứng, rồi **Kết luận** mở rộng hệ quả hoặc giới hạn liên quan.

## 30. nguồn (source / 소스) hierarchy

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, các dấu vết trong **30. nguồn (source / 소스) hierarchy** được đọc cùng nhau ở **Kết luận** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết luận

Không nên học Korea/Vietnam thị trường (market / 시장) như hai danh sách ticker hoặc chỉ số.

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

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
