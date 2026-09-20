# 05 — Multi-Asset, Hedging, Currency và Regime Allocation

Tài liệu này nối các asset classes riêng lẻ thành một portfolio thực tế. Mục tiêu là hiểu vì sao cùng một tài sản có thể hữu ích trong regime này nhưng gây hại trong regime khác, vì sao currency exposure có thể quyết định phần lớn kết quả của một nhà đầu tư quốc tế, và hedging nên được xem như công cụ quản trị rủi ro chứ không phải cách “xóa biến động miễn phí”.

## 1. Multi-Asset khác với việc mua nhiều sản phẩm

Một multi-asset portfolio không chỉ là danh sách stocks, bonds, gold và cash. Quan trọng hơn là mỗi tài sản phản ứng với growth, inflation, rates, liquidity và risk premium như thế nào.

Equities thường hưởng lợi khi earnings growth tốt và discount rate không tăng quá mạnh. Long-duration bonds thường nhạy với inflation và policy-rate expectations. Gold phản ứng với real yields, USD, geopolitical risk và demand for stores of value. Commodities phản ứng mạnh với physical supply-demand và inventory. Cash có optionality và gần như không có duration risk nhưng chịu inflation erosion.

## 2. Growth và Inflation Regimes

Một cách đơn giản để hiểu multi-asset là dùng hai trục growth và inflation. Khi growth tăng còn inflation ổn định, equities và credit thường thuận lợi. Khi growth giảm còn inflation giảm, high-quality bonds có thể tốt hơn. Khi growth mạnh và inflation tăng, commodities hoặc value/cyclicals có thể hưởng lợi tương đối. Khi growth giảm nhưng inflation cao, cả equities lẫn long bonds có thể gặp khó, tạo môi trường stagflation khó quản lý.

Đây không phải luật tuyệt đối. Asset valuation ban đầu, positioning, policy response và shock source vẫn quyết định kết quả thực tế.

## 3. Duration như một loại exposure

Duration không chỉ là thuật ngữ của bond. Growth stocks cũng có thể được xem là “long-duration equities” vì phần lớn expected cash flow nằm xa trong tương lai. Khi discount rate tăng, present value của những cash flows xa thường giảm mạnh hơn.

Một portfolio chứa long-duration Treasuries và expensive growth stocks có thể tưởng đa dạng nhưng cùng nhạy với rising real yields. Đây là ví dụ của hidden macro concentration.

## 4. Credit và Equity có thể cùng chịu một shock

Corporate bonds và equities đều nằm trong capital structure của doanh nghiệp. Khi business deteriorates, credit spreads widening có thể đi cùng stock decline. High-yield bonds vì vậy thường mang equity-like risk nhiều hơn government bonds.

Trong stress, diversification giữa high-yield credit và equities có thể thấp hơn người mới tưởng. Nếu cần defensive ballast, quality và duration của fixed income phải được hiểu rõ.

## 5. Currency Exposure

Một Korean investor mua S&P 500 unhedged ETF chịu ít nhất hai return drivers: S&P 500 bằng USD và USD/KRW. Công thức gần đúng là:

`KRW return ≈ USD asset return + USD/KRW return + interaction term`

Nếu stock tăng 10% bằng USD nhưng USD giảm 8% so KRW, KRW investor có thể chỉ còn mức gain rất nhỏ. Ngược lại, stock đi ngang nhưng USD mạnh có thể tạo positive KRW return.

## 6. Hedged và Unhedged

Currency-hedged product cố giảm ảnh hưởng FX bằng forward hoặc derivative contracts. Hedging không miễn phí. Cost phụ thuộc interest-rate differential, transaction costs, roll và basis.

Unhedged exposure có thể là diversification nếu investor có liabilities bằng KRW nhưng muốn sở hữu foreign-currency assets. Nhưng nếu tiền sắp được dùng cho mục tiêu cố định bằng KRW, large FX risk có thể không phù hợp.

## 7. Home Currency và Liability Currency

Đồng tiền bạn nhìn trên app không nhất thiết là đồng tiền risk thực. Korean-listed ETF có thể giao dịch bằng KRW nhưng underlying assets bằng USD, JPY hoặc EUR.

Currency decision nên bắt đầu từ liabilities. Nếu tương lai cần mua nhà ở Korea, KRW là liability currency. Nếu có nghĩa vụ lớn bằng VND, VND exposure cũng cần được tính. Multi-country investor nên nhìn net currency balance thay vì chỉ từng account riêng lẻ.

## 8. Hedging bằng Futures và Options

Futures có thể hedge beta, duration hoặc FX exposure khá trực tiếp, nhưng position sizing và basis phải được hiểu. Options cung cấp convex protection: loss có thể giới hạn bằng premium với long put, nhưng insurance cost có thể cao nếu mua liên tục.

Protective put nghe đơn giản nhưng long-run drag có thể lớn. Collar giảm cost bằng cách bán upside call đổi lấy downside protection. Hedging vì vậy luôn là trade-off giữa cost, protection và participation.

## 9. Tail Hedge

Tail hedge được thiết kế để payoff mạnh trong extreme events. Vấn đề là tail protection thường tốn tiền phần lớn thời gian. Một hedge tốt không phải hedge kiếm tiền hàng năm, mà là hedge có cost chấp nhận được và giúp portfolio tránh forced selling trong shock lớn.

## 10. Inflation Hedge không phải một asset duy nhất

Gold, commodities, inflation-linked bonds, real estate và equities có pricing power đều thường được gọi là inflation hedges, nhưng chúng hoạt động khác nhau.

Commodity futures có thể phản ứng nhanh với inflation shock nhưng có roll yield. Real estate chịu financing costs. Gold nhạy với real yields. TIPS bảo vệ principal theo inflation index nhưng vẫn có duration risk. Vì vậy “hedge inflation” cần xác định inflation loại nào và horizon nào.

## 11. Deflation Hedge

Trong deflationary recession, cash và high-quality government bonds thường có vai trò lớn hơn vì nominal cash flows trở nên có giá trị tương đối hơn. Nhưng nếu deflation đi cùng sovereign stress hoặc currency crisis, framework lại thay đổi.

## 12. Risk Parity

Risk parity cố phân bổ theo risk contribution thay vì capital weight. Vì bonds thường volatility thấp hơn equities, portfolio risk parity truyền thống có thể dùng leverage để tăng bond exposure.

Điểm yếu xuất hiện khi stocks và bonds cùng giảm, đặc biệt trong inflation shock. Risk parity không loại bỏ regime risk; nó chỉ phân bổ risk theo một logic khác.

## 13. 60/40 Portfolio

60/40 thường ám chỉ 60% equities và 40% bonds. Logic là growth exposure từ equities và defensive/duration exposure từ bonds. Nó hoạt động tốt hơn khi stock-bond correlation thấp hoặc âm.

Trong inflationary tightening, cả stocks lẫn bonds có thể giảm cùng lúc. Vì vậy 60/40 không phải “always safe”; hiệu quả phụ thuộc macro regime và starting yields.

## 14. Permanent Portfolio, All-Weather và Regime Diversification

Các frameworks như permanent portfolio hay all-weather cố giữ exposures có khả năng sống được qua nhiều regimes. Điểm cốt lõi không nằm ở copy tỷ trọng cố định, mà ở ý tưởng rằng investor không biết chắc tương lai thuộc regime nào.

Một portfolio robust thường chấp nhận rằng không tài sản nào luôn dẫn đầu.

## 15. Rebalancing Premium

Khi assets không hoàn toàn correlated và mean-revert phần nào, rebalancing có thể bán bớt tài sản đã tăng và mua thêm tài sản đã giảm. Nhưng “rebalancing bonus” không bảo đảm. Nếu một asset rơi vào structural decline, liên tục mua thêm có thể làm hại portfolio.

Rebalancing nên gắn với target allocation và thesis, không phải blind averaging.

## 16. Volatility Targeting

Volatility targeting giảm gross exposure khi realized volatility tăng và tăng exposure khi volatility giảm. Mục tiêu là giữ risk tương đối ổn định.

Nhược điểm là có thể buộc giảm risk sau khi market đã rơi mạnh, và tăng risk trong calm periods ngay trước shock. Nó là control mechanism, không phải alpha source tự động.

## 17. Correlation Breakdown

Historical correlation có thể đổi nhanh trong crisis. Assets từng diversify nhau có thể cùng bị bán để tạo cash hoặc đáp ứng margin calls.

Do đó stress testing nên giả định correlations xấu đi, không chỉ dùng average historical matrix.

## 18. Liquidity Hierarchy

Cash, government bonds, large-cap equities, small caps, private assets và property có liquidity khác nhau. Portfolio allocation phải tính cả thời gian cần để convert thành cash mà không tạo price impact lớn.

Emergency liabilities không nên được tài trợ bằng illiquid assets dù expected return hấp dẫn.

## 19. Multi-Asset Decision Framework

Trước khi thêm một asset, hãy hỏi nó đang mang exposure nào: growth, inflation, duration, credit, liquidity, FX hay commodity beta. Sau đó hỏi exposure đó đã tồn tại ở nơi khác chưa.

Nếu asset mới chỉ lặp lại risk cũ dưới ticker khác, diversification thực tế không tăng.

## 20. Portfolio Construction thực tế

Một quy trình tốt bắt đầu từ liabilities và horizon, sau đó xác định strategic exposures, rồi mới chọn product. Product selection là bước cuối, không phải bước đầu.

Investor nên biết vì sao mỗi asset tồn tại trong portfolio. Nếu không thể viết một câu giải thích vai trò của nó, rất có thể position đó được mua do narrative hoặc FOMO hơn là design.