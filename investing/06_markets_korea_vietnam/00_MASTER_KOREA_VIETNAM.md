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

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **2. Hàn Quốc và Việt Nam khác nhau ở đâu?** tiếp nhận điểm tựa từ **1. Không phân tích thị trường chỉ bằng chỉ số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Hạ tầng thị trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Hàn Quốc và Việt Nam khác nhau ở đâu?

Hàn Quốc có thị trường vốn lớn hơn, tính quốc tế hóa cao hơn và tỷ trọng các doanh nghiệp xuất khẩu toàn cầu rất lớn.

Việt Nam có vai trò nổi bật của nhà đầu tư nội địa, ngân hàng, bất động sản, FDI và chu kỳ tín dụng trong nước.

Do đó cùng một Fed shock có thể truyền vào hai thị trường theo kênh khác nhau.

# Phần II — Hàn Quốc

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **3. Hạ tầng thị trường** tiếp nhận điểm tựa từ **2. Hàn Quốc và Việt Nam khác nhau ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Đặc điểm kinh tế Hàn Quốc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **4. Đặc điểm kinh tế Hàn Quốc** tiếp nhận điểm tựa từ **3. Hạ tầng thị trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. KRW** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Đặc điểm kinh tế Hàn Quốc

Hàn Quốc là nền kinh tế:

- định hướng xuất khẩu;
- nhập khẩu nhiều năng lượng;
- có ngành bán dẫn rất lớn;
- nhạy với China cycle;
- nhạy với USD/KRW;
- có household debt đáng kể.

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **5. KRW** tiếp nhận điểm tựa từ **4. Đặc điểm kinh tế Hàn Quốc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. BOK** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **6. BOK** tiếp nhận điểm tựa từ **5. KRW** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Semiconductor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. BOK

Bank of Korea (BOK) điều hành chính sách (policy / 정책) tỷ lệ (rate / 비율) trong bối cảnh phải cân bằng:

- inflation;
- growth;
- financial stability;
- household debt;
- FX conditions.

Mức chính sách (policy / 정책) tỷ lệ (rate / 비율) hiện tại luôn phải kiểm tra từ BOK khi cần dữ liệu mới nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **7. Semiconductor** tiếp nhận điểm tựa từ **6. BOK** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Các ngành Hàn Quốc cần theo dõi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **8. Các ngành Hàn Quốc cần theo dõi** tiếp nhận điểm tựa từ **7. Semiconductor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Hạ tầng thị trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **9. Hạ tầng thị trường** tiếp nhận điểm tựa từ **8. Các ngành Hàn Quốc cần theo dõi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Đặc điểm kinh tế Việt Nam** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **10. Đặc điểm kinh tế Việt Nam** tiếp nhận điểm tựa từ **9. Hạ tầng thị trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. SBV và VND** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Đặc điểm kinh tế Việt Nam

Các động lực lớn gồm:

- domestic credit;
- thuộc tính (property / 속성) cycle;
- FDI;
- manufacturing exports;
- công khai (public / 공개) investment;
- household savings;
- VND stability.

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **11. SBV và VND** tiếp nhận điểm tựa từ **10. Đặc điểm kinh tế Việt Nam** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Ngân hàng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **12. Ngân hàng** tiếp nhận điểm tựa từ **11. SBV và VND** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Bất động sản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **13. Bất động sản** tiếp nhận điểm tựa từ **12. Ngân hàng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Các ngành Việt Nam quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **14. Các ngành Việt Nam quan trọng** tiếp nhận điểm tựa từ **13. Bất động sản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. toàn cục (global / 전역) sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **15. toàn cục (global / 전역) sensitivity** tiếp nhận điểm tựa từ **14. Các ngành Việt Nam quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Fed shock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **16. Fed shock** tiếp nhận điểm tựa từ **15. toàn cục (global / 전역) sensitivity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. China shock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **17. China shock** tiếp nhận điểm tựa từ **16. Fed shock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Oil shock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. China shock

China slowdown có thể ảnh hưởng Korea qua exports/semiconductors/industrials và ảnh hưởng Vietnam qua trade, manufacturing supply chuỗi (chain / 사슬), commodities và FDI dynamics.

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **18. Oil shock** tiếp nhận điểm tựa từ **17. China shock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Oil shock

Hàn Quốc là năng lượng (energy / 에너지) importer lớn nên oil shock có thể tác động terms of trade mạnh.

Việt Nam có cấu trúc năng lượng khác và tác động cần tách theo upstream/downstream, fiscal pricing và inflation.

# Phần V — Dòng vốn và breadth

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth** tiếp nhận điểm tựa từ **18. Oil shock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Foreign luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth

Chỉ số tăng nhờ vài large caps khác hoàn toàn một rally có nhiều cổ phiếu cùng tham gia.

Theo dõi:

- advance/decline;
- volume;
- sector breadth;
- equal-weight vs cap-weight nếu có dữ liệu.

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **19. chỉ mục (index / 인덱스) move không bằng thị trường (market / 시장) breadth** xác định đầu vào; **20. Foreign luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **21. Domestic liquidity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Foreign luồng (flow / 흐름)

Foreign buying/selling có thể ảnh hưởng price mạnh ở một số giai đoạn nhưng không nên được xem là “smart money” mặc định.

Dòng vốn có thể đến từ:

- passive rebalance;
- FX hedge;
- toàn cục (global / 전역) rủi ro (risk / 위험) reduction;
- country allocation;
- company view.

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **20. Foreign luồng (flow / 흐름)** xác định đầu vào; **21. Domestic liquidity** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. Wrapper không phải underlying** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Domestic liquidity

Ở Việt Nam, domestic deposit tỷ lệ (rate / 비율), margin balance và retail turnover có thể ảnh hưởng mạnh đến thị trường (market / 시장) multiple.

Ở Hàn Quốc, household flows, pension/institutional flows và ETF/futures mechanics cũng đáng chú ý.

# Phần VI — ETF, ETN và derivatives

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **22. Wrapper không phải underlying** tiếp nhận điểm tựa từ **21. Domestic liquidity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Futures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Wrapper không phải underlying

ETF/ETN niêm yết bằng KRW không đồng nghĩa exposure kinh tế là KRW.

Cần tách:

```text
Listing Currency
Underlying Currency
Economic Exposure
Hedge Policy
```

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **23. Futures** tiếp nhận điểm tựa từ **22. Wrapper không phải underlying** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Leveraged/inverse products** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Futures

Futures giúp hedge beta hoặc trade chỉ mục (index / 인덱스) nhưng phải hiểu:

- multiplier;
- margin;
- expiry;
- basis;
- roll;
- settlement.

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **24. Leveraged/inverse products** tiếp nhận điểm tựa từ **23. Futures** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Bốn lớp tiền tệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Leveraged/inverse products

Daily-reset sản phẩm (product / 제품) có đường dẫn (path / 경로) phụ thuộc (dependency / 의존성).

Không nên ngoại suy `2× daily` thành `2× long-term`.

# Phần VII — Cross-border investing

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **25. Bốn lớp tiền tệ** tiếp nhận điểm tựa từ **24. Leveraged/inverse products** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Wrapper và legal claim** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Bốn lớp tiền tệ

Khi đầu tư đa quốc gia cần phân biệt:

```text
Trading Currency
Underlying Economic Currency
Reporting / Home Currency
Liability Currency
```

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **26. Wrapper và legal claim** tiếp nhận điểm tựa từ **25. Bốn lớp tiền tệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Thuế và truy cập (access / 접근)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Wrapper và legal claim

Cùng một exposure có thể mua qua:

- cục bộ (local / 로컬) ETF;
- direct foreign bảo mật (security / 보안);
- depositary receipt;
- fund;
- derivative.

Mỗi wrapper có tax, custody, settlement, liquidity và legal claim khác nhau.

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **27. Thuế và truy cập (access / 접근)** tiếp nhận điểm tựa từ **26. Wrapper và legal claim** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Company research** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **28. Company research** tiếp nhận điểm tựa từ **27. Thuế và truy cập (access / 접근)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. thị trường (market / 시장) research** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Company research

Sau khi đặt country/sector map, company research đi từ dữ liệu vận hành, bảng cân đối và exposure tiền tệ tới định giá và liquidity-aware sizing. Sơ đồ dưới đây là trình tự kiểm tra, không phải danh sách file để đọc rời rạc.

```text
Business Model
→ Sector Driver
→ Financial Statements
→ Balance Sheet
→ Earnings Revision
→ Valuation
→ Catalyst / Invalidation
```

> **Chuyển mạch:** Trong **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **29. thị trường (market / 시장) research** tiếp nhận điểm tựa từ **28. Company research** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. nguồn (source / 소스) hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, **29. thị trường (market / 시장) research** nêu điều cần giải thích; **30. nguồn (source / 소스) hierarchy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bản đồ tổng quan thị trường Hàn Quốc và Việt Nam**, các dấu vết trong **30. nguồn (source / 소스) hierarchy** được đọc cùng nhau ở **Kết luận** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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
