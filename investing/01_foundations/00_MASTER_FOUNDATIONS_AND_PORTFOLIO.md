# Bản đồ nền tảng đầu tư và quản trị danh mục

> File này là **bản đồ tổng quan**, không thay thế các chương chuyên sâu trong `01_foundations/`. Mục tiêu là giúp người đọc thấy toàn bộ hệ thống trước khi đi sâu. Phần giải thích dùng tiếng Việt; thuật ngữ tiếng Anh chỉ giữ trong ngoặc ở những điểm cần tra cứu.

## 1. Đầu tư thực chất là phân bổ sức mua theo thời gian

Tiền hôm nay và tiền trong tương lai không có cùng giá trị vì lạm phát, chi phí cơ hội và rủi ro.

```text
PV = Future Cash Flow / (1 + Discount Rate)^t
```

Đầu tư là quyết định hy sinh một phần sức mua hiện tại để nhận một phân phối sức mua trong tương lai. Vì vậy mọi quyết định phải hỏi cả lợi suất kỳ vọng lẫn xác suất không đáp ứng được mục tiêu.

Đọc sâu: [Tiền, hệ thống tài chính và cơ chế thị trường](./01_MONEY_FINANCIAL_SYSTEM_AND_MARKET_MECHANICS.md).

## 2. Lợi suất danh nghĩa và lợi suất thực

```text
Real Return = (1 + Nominal Return) / (1 + Inflation) - 1
```

Lợi suất danh nghĩa cao không đảm bảo sức mua tăng. Đây là lý do tiền mặt, trái phiếu, cổ phiếu và tài sản thực phải được đánh giá trong bối cảnh lạm phát.

## 3. Hệ thống tài chính là mạng lưới quyền lợi và nghĩa vụ

Hệ thống tài chính chuyển vốn từ người tiết kiệm sang người cần vốn qua ngân hàng, thị trường trái phiếu, cổ phiếu, quỹ và công cụ phái sinh.

Mỗi sản phẩm phải được bắt đầu bằng câu hỏi:

```text
Tôi đang sở hữu quyền lợi pháp lý nào?
Ai nợ tiền tôi?
Dòng tiền đến từ đâu?
Tôi đứng ở đâu trong cấu trúc vốn?
```

Cổ đông là người hưởng phần còn lại; trái chủ có quyền đòi theo hợp đồng; công cụ phái sinh tạo quyền/nghĩa vụ theo điều khoản hợp đồng.

## 4. Cổ phiếu

Cổ phiếu phổ thông đại diện cho quyền sở hữu phần còn lại của doanh nghiệp. Lợi suất dài hạn liên quan tới:

```text
Tăng trưởng lợi nhuận trên mỗi cổ phiếu
+ Cổ tức / Mua lại ròng
+ Thay đổi hệ số định giá
```

Tăng doanh thu không đủ; phải kiểm tra pha loãng, ROIC, nhu cầu tái đầu tư và chất lượng dòng tiền.

## 5. Cổ tức và mua lại cổ phiếu

Cổ tức chuyển tiền mặt từ doanh nghiệp sang cổ đông. Mua lại cổ phiếu tạo giá trị khi cổ phiếu được mua ở mức hợp lý và số cổ phiếu thực sự giảm.

Mua lại chỉ để bù SBC không tương đương hoàn vốn thật sự cho cổ đông.

## 6. Chia tách, phát hành thêm và pha loãng

Chia tách cổ phiếu thay đổi số đơn vị và giá trên mỗi đơn vị nhưng không tự tạo giá trị doanh nghiệp.

Phát hành thêm, quyền mua, trái phiếu chuyển đổi và chứng quyền có thể làm tăng số cổ phiếu trong tương lai. Vì vậy cần theo dõi số cổ phiếu pha loãng (diluted shares), không chỉ số cổ phiếu cơ bản.

## 7. Chỉ số và quỹ đầu tư

Chỉ số không phải “thị trường” theo nghĩa tuyệt đối. Nó là một tập hợp quy tắc lựa chọn và gán trọng số.

Hai chỉ số cùng theo một chủ đề có thể khác đáng kể về:

```text
Vũ trụ chứng khoán
Trọng số
Giới hạn tập trung
Lịch tái cân bằng
Quy tắc thêm / loại cổ phiếu
```

ETF chỉ là cấu trúc triển khai; kinh tế của khoản đầu tư nằm ở tài sản cơ sở và phương pháp chỉ số.

## 8. ETF

Khi đánh giá ETF, cần kiểm tra:

```text
Chỉ số cơ sở
Phương pháp sao chép
AUM
Spread
Tracking difference
Phí
Thuế
Securities lending
FX hedge
Thanh khoản tài sản cơ sở
```

ETF giao dịch bằng KRW không có nghĩa tài sản cơ sở không còn rủi ro USD.

Đọc sâu: [Cổ phiếu, ETF và quỹ](../02_asset_classes/01_STOCKS_ETF_AND_FUNDS.md).

## 9. Trái phiếu

Trái phiếu là hợp đồng dòng tiền. Giá bằng giá trị hiện tại của coupon và tiền gốc.

```text
%ΔPrice ≈ -Modified Duration × ΔYield
```

Rủi ro trái phiếu gồm lãi suất, đường cong, lạm phát, tín dụng, thanh khoản, quyền chọn và FX.

Một trái phiếu chính phủ dài hạn có thể biến động mạnh dù gần như không có rủi ro vỡ nợ bằng đồng tiền đó.

Đọc sâu: [Trái phiếu, lãi suất và tín dụng](../02_asset_classes/02_BONDS_RATES_AND_CREDIT.md).

## 10. Duration

Duration đo độ nhạy của giá trái phiếu với thay đổi lợi suất. DV01 đo mức thay đổi giá trị khi lợi suất dịch chuyển 1 điểm cơ bản.

Duration cũng là một trực giác hữu ích cho cổ phiếu: doanh nghiệp có phần lớn dòng tiền ở xa thường nhạy hơn với thay đổi tỷ lệ chiết khấu.

## 11. REIT và bất động sản

Bất động sản tạo lợi suất từ thu nhập thuê, tăng trưởng NOI, thay đổi cap rate và đòn bẩy.

REIT là cổ phiếu của một cấu trúc sở hữu bất động sản; nó vẫn chịu rủi ro thị trường, lãi suất, tái cấp vốn và thanh khoản.

Cap rate không nên được đọc tách khỏi tăng trưởng NOI và chi phí vốn.

## 12. Vàng

Vàng không tạo dòng tiền hợp đồng. Giá chịu ảnh hưởng của lãi suất thực, USD, nhu cầu dự trữ, địa chính trị và vị thế thị trường.

Vàng có thể giúp đa dạng hóa nhưng không phải công cụ phòng vệ hoàn hảo trong mọi giai đoạn.

## 13. Hàng hóa

Lợi suất từ hàng hóa qua futures khác biến động giá giao ngay vì còn có cấu trúc đường cong và lợi suất roll.

Contango có thể tạo lực kéo âm; backwardation có thể hỗ trợ carry dương. Do đó không thể nhìn biểu đồ spot rồi suy ra lợi suất ETF hàng hóa.

## 14. Forex

Ngoại hối là giá tương đối giữa hai đồng tiền. Tỷ giá chịu tác động của chênh lệch lãi suất, tăng trưởng, lạm phát, điều kiện thương mại, dòng vốn và tâm lý rủi ro.

Một vị thế FX luôn có hai phía. “USD mạnh” phải nói rõ mạnh so với đồng nào.

## 15. Futures

Hợp đồng tương lai tạo mức phơi nhiễm lớn hơn số tiền ký quỹ.

```text
Notional = Futures Price × Contract Multiplier
```

Ký quỹ là tài sản bảo đảm, không phải quy mô rủi ro. Cần hiểu multiplier, tick, đáo hạn, thanh toán và roll.

## 16. Quyền chọn

Quyền chọn tạo cấu trúc chi trả phi tuyến. Người mua quyền chọn thường giới hạn tổn thất ở premium, nhưng người bán quyền chọn có thể chịu đuôi lỗ lớn.

Giá quyền chọn trước đáo hạn phụ thuộc giá cơ sở, thời gian, biến động ngụ ý, lãi suất và các yếu tố khác.

Delta, Gamma, Theta và Vega là các độ nhạy, không phải dự báo.

## 17. CFD và sản phẩm OTC

CFD là hợp đồng song phương với môi giới dựa trên thay đổi giá tài sản cơ sở; nhà đầu tư thường không sở hữu tài sản đó.

Cần hiểu pháp nhân đối tác, spread, phí tài trợ qua đêm, margin, stop-out, chính sách thực thi và cơ chế bảo vệ tiền khách hàng.

## 18. ETN, sản phẩm đòn bẩy và nghịch đảo

ETN là khoản nợ không bảo đảm của tổ chức phát hành gắn với một chỉ số hoặc chiến lược, nên có thêm rủi ro tín dụng của nhà phát hành.

ETF đòn bẩy/nghịch đảo thường đặt mục tiêu theo ngày, vì vậy lợi suất nhiều ngày phụ thuộc đường đi của giá. Không thể lấy mức tăng của chỉ số rồi nhân cố định theo số ngày.

## 19. Crypto

Crypto có thể mang rủi ro thị trường, công nghệ, lưu ký, thanh khoản, quy định và đối tác. Stablecoin còn có rủi ro tài sản dự trữ và cơ chế quy đổi.

Nếu không giải thích được quyền lợi pháp lý, nguồn cầu và cơ chế lưu ký, không nên xem biến động giá đơn thuần là bằng chứng về giá trị.

## 20. Lệnh giao dịch

Lệnh thị trường ưu tiên khớp; lệnh giới hạn ưu tiên giá; stop là cơ chế kích hoạt chứ không phải bảo đảm giá thoát.

Spread, slippage và market impact là các chi phí thực tế quan trọng, đặc biệt khi quy mô vị thế lớn so thanh khoản.

## 21. Bán khống

Bán khống yêu cầu vay chứng khoán hoặc cơ chế tương đương. Chi phí vay có thể thay đổi và vị thế có thể bị thu hồi.

Tổn thất lý thuyết của bán khống không bị giới hạn khi giá tăng, vì vậy quản trị quy mô và thanh khoản rất quan trọng.

## 22. Margin và đòn bẩy

Đòn bẩy làm phóng đại cả lợi nhuận và thua lỗ. Margin call có thể buộc bán ở thời điểm xấu.

Luận điểm đúng nhưng dùng đòn bẩy quá lớn vẫn có thể thất bại vì không sống được tới khi luận điểm xảy ra.

## 23. Đa dạng hóa

Đa dạng hóa là sở hữu các nguồn lợi suất khác nhau, không phải chỉ nhiều mã.

Cần nhìn tập trung theo:

```text
Mã
Ngành
Quốc gia
Tiền tệ
Nhân tố
Thanh khoản
Nguồn thu nhập cá nhân
```

Đọc sâu: [Rủi ro danh mục, phân bổ và hành vi](./02_PORTFOLIO_RISK_ALLOCATION_AND_BEHAVIOR.md).

## 24. DCA và đầu tư một lần

Đầu tư định kỳ (Dollar-Cost Averaging, DCA) phù hợp với dòng thu nhập định kỳ và giúp giảm áp lực tâm lý về thời điểm.

Đầu tư một lần (lump sum) đưa tiền vào thị trường sớm hơn và do đó có kỳ vọng cao hơn nếu tài sản rủi ro có phần bù dương dài hạn, nhưng có rủi ro thời điểm lớn hơn ngay sau quyết định.

Không có phương pháp nào loại bỏ rủi ro thị trường.

## 25. Tái cân bằng

Tái cân bằng giữ danh mục gần cấu trúc rủi ro mục tiêu. Có thể dùng lịch hoặc dải tỷ trọng.

Dòng tiền mới thường là công cụ tái cân bằng rẻ hơn bán/mua lại vì giảm phí và thuế.

## 26. Phong cách đầu tư

Đầu tư giá trị, tăng trưởng, chất lượng, động lượng hay thu nhập chỉ là các cách nhấn mạnh những nguồn lợi suất khác nhau.

Không nên biến phong cách thành bản sắc cá nhân. Một phương pháp phải được đánh giá bằng cơ chế, bằng chứng, chi phí và khả năng thực thi.

## 27. Nhân tố

Các nhân tố như value, size, quality, momentum và low volatility có thể giải thích một phần chênh lệch lợi suất giữa các danh mục.

Một ETF có nhãn “smart beta” chỉ hữu ích nếu phương pháp thật sự tạo exposure mong muốn sau turnover và chi phí.

## 28. Tâm lý và hành vi

Những lỗi phổ biến gồm quá tự tin, thiên lệch xác nhận, FOMO, ác cảm thua lỗ, hiệu ứng sở hữu, gần đây hóa và nhìn lại.

Kỷ luật tốt cần quy tắc trước quyết định, nhật ký và điều kiện vô hiệu hóa.

## 29. Thời hạn và nghĩa vụ

Thời hạn đầu tư phải gắn với thời điểm cần tiền. Một tài sản “tốt dài hạn” có thể không phù hợp với nghĩa vụ trong 12 tháng.

Đồng tiền của nghĩa vụ cũng quan trọng. Mục tiêu bằng KRW và tài sản bằng USD tạo thêm rủi ro tỷ giá.

## 30. Thanh khoản

Tiền mặt và T-bill có vai trò khác cổ phiếu nhỏ, private credit hoặc bất động sản. Danh mục cần đủ thanh khoản để đáp ứng chi tiêu, margin và sự cố mà không phải bán tháo.

## 31. Custody và operational risk

Rủi ro đầu tư không kết thúc ở giá. Còn có môi giới, pháp nhân, lưu ký, thanh toán, quyền sở hữu thụ hưởng, lỗi vận hành và tài liệu thuế.

Nhà đầu tư phải hiểu ai thực sự giữ tài sản và quy trình xử lý nếu một trung gian thất bại.

## 32. TWR, MWR và đánh giá hiệu quả

TWR dùng để đánh giá chiến lược độc lập với thời điểm dòng tiền. MWR phản ánh trải nghiệm thực của nhà đầu tư.

Không nên đánh giá chỉ bằng tổng lợi suất. Cần nhìn mức suy giảm, rủi ro, phí, thuế và benchmark.

## 33. Lợi suất thực và sức mua

Mục tiêu tài chính cuối cùng là sức mua chứ không phải con số tài khoản. Vì vậy mọi kế hoạch dài hạn cần kiểm tra lợi suất sau lạm phát.

## 34. IPS

Tuyên bố chính sách đầu tư (Investment Policy Statement, IPS) là bản mô tả mục tiêu, nghĩa vụ, thanh khoản, phạm vi phân bổ, giới hạn tập trung, quy tắc tái cân bằng và những công cụ được phép sử dụng.

IPS giúp giảm thay đổi theo cảm xúc.

## 35. Hệ thống cuối cùng

```text
Mục tiêu
→ Nghĩa vụ
→ Thanh khoản
→ Khả năng chịu rủi ro
→ Nhóm tài sản
→ Cấu trúc sản phẩm
→ Phân bổ
→ Thực thi
→ Đo kết quả
→ Phân rã kết quả
→ Cập nhật kế hoạch
```

Nếu cần chiều sâu, không tiếp tục mở rộng file tổng quan này. Hãy chuyển sang các chapter chuyên sâu trong `01_foundations/` và `02_asset_classes/`.