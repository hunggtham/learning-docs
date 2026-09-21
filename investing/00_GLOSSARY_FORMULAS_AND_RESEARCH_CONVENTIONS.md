# Thuật ngữ, quy ước công thức và tiêu chuẩn nghiên cứu

> File này là lớp chuẩn hóa dùng chung cho toàn bộ `investing/`. Mục tiêu là giúp người đọc dùng cùng một hệ thuật ngữ, cùng quy ước công thức và cùng cách phân biệt dữ kiện, ước tính, giả định và luận điểm đầu tư. Phần giải thích luôn ưu tiên tiếng Việt; thuật ngữ tiếng Anh chỉ được giữ như từ khóa bổ sung để tra cứu tài liệu gốc.

## 1. Quy tắc ngôn ngữ của thư viện

Phần giải thích phải được viết tự nhiên bằng tiếng Việt. Khi một thuật ngữ chuyên môn quan trọng xuất hiện lần đầu, viết tiếng Việt trước rồi đặt từ tiếng Anh trong ngoặc.

Ví dụ:

- câu hỏi (question)
- lợi suất (return)
- lợi suất đến ngày đáo hạn (yield to maturity, YTM)
- rủi ro thanh khoản (liquidity risk)
- dòng tiền tự do (free cash flow, FCF)
- vốn lưu động (working capital)
- quyền định giá (pricing power)

Không viết một câu kiểu `Portfolio risk depends on correlation and liquidity`. Hãy viết: **Rủi ro của danh mục phụ thuộc vào tương quan (correlation) và tính thanh khoản (liquidity).**

Các tên chuẩn và viết tắt đã phổ biến như ETF, ETN, CPI, GDP, ROIC, FCFF, FCFE, WACC, DV01, VaR, KOSPI hay VN30 có thể giữ nguyên, nhưng ý nghĩa phải được giải thích bằng tiếng Việt ở lần xuất hiện đầu tiên.

## 2. Dữ kiện, ước tính, giả định, kịch bản và luận điểm đầu tư

Một ghi chú nghiên cứu (research note) phải phân biệt rõ năm lớp thông tin.

**Dữ kiện (fact)** là thông tin đã xảy ra và có nguồn xác minh, ví dụ doanh thu quý vừa rồi, lãi suất chính sách hiện tại hoặc số cổ phiếu đang lưu hành.

**Ước tính (estimate)** là con số dự báo của doanh nghiệp, nhà phân tích hoặc thị trường, ví dụ EPS đồng thuận (consensus EPS) cho năm sau. Ước tính luôn phải gắn với nguồn và thời điểm.

**Giả định (assumption)** là đầu vào do người phân tích chủ động đặt vào mô hình, ví dụ biên lợi nhuận gộp (gross margin) 35% trong kịch bản cơ sở.

**Kịch bản (scenario)** là một tập hợp giả định nhất quán về đường đi của nền kinh tế hoặc doanh nghiệp.

**Luận điểm đầu tư (thesis)** là một nhận định có thể kiểm chứng về khoảng cách giữa kỳ vọng đang được thị trường phản ánh vào giá và kết quả bạn cho rằng có xác suất xảy ra cao hơn hoặc thấp hơn.

Chuỗi tối thiểu nên là:

```text
Dữ kiện → Diễn giải → Giả định → Kịch bản → Định giá / Lợi suất kỳ vọng → Vị thế → Điều kiện vô hiệu hóa
```

## 3. Giá trị danh nghĩa và giá trị thực

**Danh nghĩa (nominal)** là giá trị chưa điều chỉnh lạm phát. **Thực (real)** là giá trị đã điều chỉnh theo sức mua.

Lợi suất thực chính xác gần:

```text
Real Return = (1 + Nominal Return) / (1 + Inflation) - 1
```

Với tỷ lệ nhỏ có thể dùng xấp xỉ:

```text
Real Return ≈ Nominal Return - Inflation
```

Không nên so lương, GDP, lợi suất trái phiếu hay kết quả danh mục dài hạn chỉ bằng số danh nghĩa khi các giai đoạn lạm phát khác nhau.

## 4. Lợi suất số học và lợi suất hình học

**Lợi suất trung bình số học (arithmetic return)** là trung bình các mức lợi suất theo từng kỳ. **Lợi suất hình học (geometric return)** phản ánh tác động của lãi kép.

Nếu vốn đi từ 100 → 150 → 100, lợi suất số học trung bình hai kỳ vẫn dương, nhưng tổng tài sản quay lại đúng 100. Đây là lý do độ biến động có thể làm giảm tốc độ tăng trưởng kép.

CAGR:

```text
CAGR = (Ending Value / Beginning Value)^(1/n) - 1
```

Trong quá trình tích lũy tài sản, lợi suất hình học thường quan trọng hơn lợi suất trung bình số học.

## 5. Độ biến động, phương sai và độ lệch chuẩn

**Phương sai (variance)** đo độ lệch bình phương trung bình quanh giá trị trung bình. **Độ lệch chuẩn (standard deviation)** là căn bậc hai của phương sai và thường được dùng làm thước đo độ biến động (volatility).

Quy đổi gần đúng sang năm:

```text
Annual Volatility ≈ Period Volatility × √Periods Per Year
```

Tuy nhiên lợi suất tài chính thường có hiện tượng cụm biến động (volatility clustering) và đuôi phân phối dày (fat tails), nên công thức căn bậc hai theo thời gian chỉ là xấp xỉ.

## 6. Hiệp phương sai và tương quan

**Hiệp phương sai (covariance)** đo mức hai tài sản biến động cùng nhau. **Tương quan (correlation)** chuẩn hóa hiệp phương sai về khoảng từ `-1` đến `+1`.

```text
Correlation(A,B) = Cov(A,B) / (σA × σB)
```

Tương quan thấp trong thời kỳ bình thường không đảm bảo đa dạng hóa tốt trong khủng hoảng. Vì vậy nên kết hợp tương quan trung bình với tương quan khi thị trường giảm, mức phơi nhiễm nhân tố (factor exposure) và kiểm thử kịch bản.

## 7. Phương sai của danh mục

Với hai tài sản:

```text
σp² = w1²σ1² + w2²σ2² + 2w1w2Cov(1,2)
```

Điều quan trọng không phải học thuộc công thức, mà hiểu rủi ro danh mục phụ thuộc cả rủi ro riêng của từng tài sản và cách chúng tương tác với nhau.

Một tài sản có độ biến động cao vẫn có thể làm giảm rủi ro tổng thể nếu tương quan với phần còn lại đủ thấp.

## 8. Beta và Alpha

**Beta** đo gần đúng độ nhạy của tài sản so với chỉ số tham chiếu (benchmark).

```text
Beta = Cov(Rasset, Rbenchmark) / Var(Rbenchmark)
```

**Alpha** là phần lợi suất còn lại sau khi đã tính đến chỉ số tham chiếu hoặc mô hình nhân tố phù hợp. Không nên gọi toàn bộ phần vượt trội là alpha nếu nó chỉ đến từ việc nắm nhiều cổ phiếu giá trị, vốn hóa nhỏ hoặc một nhân tố quen thuộc khác.

## 9. Sharpe, Sortino và Information Ratio

Sharpe Ratio:

```text
Sharpe = (Portfolio Return - Risk-Free Return) / Portfolio Volatility
```

Sortino thay tổng độ biến động bằng độ lệch giảm giá (downside deviation). Information Ratio so lợi suất chủ động với sai lệch bám chỉ số (tracking error):

```text
IR = Active Return / Tracking Error
```

Các tỷ lệ này hữu ích để đánh giá quy trình nhưng không thay thế phân tích mức suy giảm, rủi ro đuôi, tính thanh khoản và đường đi của kết quả.

## 10. Mức suy giảm và toán phục hồi

**Mức suy giảm (drawdown)** đo mức giảm từ đỉnh trước đó:

```text
Drawdown = Current Value / Previous Peak - 1
```

Khả năng phục hồi là phi tuyến:

```text
Mất 10% → cần tăng 11,1%
Mất 20% → cần tăng 25%
Mất 50% → cần tăng 100%
```

Vì vậy quản trị danh mục phải chú trọng khả năng sống sót và tăng trưởng kép, không chỉ lợi suất trung bình.

## 11. VaR và Expected Shortfall

**Giá trị chịu rủi ro (Value at Risk, VaR)** ước lượng ngưỡng tổn thất tại một mức tin cậy và khoảng thời gian nhất định. **Tổn thất kỳ vọng vượt ngưỡng (Expected Shortfall)** đo mức lỗ trung bình khi đã vượt ngưỡng VaR.

Không chỉ số nào là “mức lỗ tối đa”. Chúng đều phụ thuộc mô hình, dữ liệu và giả định phân phối, đồng thời có thể đánh giá thấp các cú nhảy giá hoặc sự đứt gãy thanh khoản.

## 12. Giá trị hiện tại và chiết khấu

Nguyên tắc cơ bản của định giá:

```text
PV = Future Cash Flow / (1 + Discount Rate)^t
```

Giá trị của tài sản là giá trị hiện tại (present value, PV) của các dòng tiền hoặc lợi ích kinh tế phù hợp với quyền lợi pháp lý của người nắm giữ. Tỷ lệ chiết khấu càng cao thì các dòng tiền ở xa càng mất giá mạnh.

## 13. Giá trị doanh nghiệp và giá trị vốn chủ sở hữu

Một cầu nối đơn giản:

```text
Enterprise Value = Equity Value + Net Debt + Other Senior Claims - Non-operating Assets
```

Giá trị doanh nghiệp (Enterprise Value, EV) và giá trị vốn chủ sở hữu (Equity Value) không thể dùng thay thế cho nhau. FCFF được chiết khấu bằng WACC để đi tới EV; FCFE được chiết khấu bằng chi phí vốn chủ sở hữu (cost of equity) để đi tới Equity Value.

## 14. Dòng tiền tự do

Một công thức vận hành đơn giản cho dòng tiền tự do của doanh nghiệp (FCFF):

```text
FCFF ≈ EBIT × (1 - Tax Rate)
       + D&A
       - Capex
       - Change in Net Working Capital
```

Vốn lưu động ròng (net working capital) phải được hiểu theo mô hình kinh doanh. Ngân hàng và công ty bảo hiểm cần cách tiếp cận khác với doanh nghiệp công nghiệp.

## 15. ROIC và tái đầu tư

Một trực giác quan trọng:

```text
Growth ≈ Reinvestment Rate × Return on Incremental Capital
```

Nếu doanh nghiệp tái đầu tư nhiều nhưng lợi suất trên vốn tăng thêm thấp hơn chi phí vốn, tăng trưởng có thể phá hủy giá trị cổ đông. Tăng trưởng chất lượng cần cả dư địa phát triển và hiệu quả trên đơn vị kinh tế.

## 16. Giá trái phiếu, duration và DV01

Giá trái phiếu là giá trị hiện tại của coupon và tiền gốc. Độ nhạy gần đúng với lợi suất:

```text
%ΔPrice ≈ -Modified Duration × ΔYield
```

**Thời hạn điều chỉnh (modified duration)** đo độ nhạy theo tỷ lệ phần trăm. **DV01/PV01** đo thay đổi tiền tệ khi lợi suất thay đổi 1 điểm cơ bản (basis point).

Danh mục trái phiếu nên được nhìn qua thời hạn lãi suất, độ nhạy theo từng đoạn đường cong và độ nhạy với chênh lệch tín dụng, không chỉ qua giá trị danh nghĩa.

## 17. Các loại lợi suất của trái phiếu

Coupon, lợi suất hiện tại (current yield), lợi suất đến đáo hạn (YTM), lợi suất đến ngày được mua lại sớm (yield to call), lợi suất xấu nhất (yield to worst) và lợi suất phân phối của quỹ là các khái niệm khác nhau.

Trước khi so sánh hai mức lợi suất, cần kiểm tra cách tính dòng tiền, quy ước số ngày, cách ghép lãi, giả định đáo hạn hoặc mua lại sớm, rủi ro tín dụng, tính thanh khoản, quyền chọn và đồng tiền.

## 18. Tổn thất tín dụng kỳ vọng

Công thức đơn giản:

```text
Expected Loss ≈ PD × LGD × Exposure
```

Trong đó PD là xác suất vỡ nợ (probability of default), LGD là tỷ lệ tổn thất khi vỡ nợ (loss given default). Chênh lệch tín dụng (credit spread) còn chứa phần bù rủi ro và phần bù thanh khoản, nên không thể đọc nó như xác suất vỡ nợ thuần túy.

## 19. Phân rã lợi suất ngoại tệ

Lợi suất quy về đồng tiền cơ sở:

```text
Home Return = (1 + Local Asset Return) × (1 + FX Return) - 1
```

Cần phân biệt:

```text
Đồng tiền giao dịch (Trading Currency)
Đồng tiền kinh tế của tài sản (Underlying Economic Currency)
Đồng tiền báo cáo (Reporting Currency)
Đồng tiền nghĩa vụ tương lai (Liability Currency)
```

Một ETF niêm yết bằng KRW không có nghĩa rủi ro USD của tài sản cơ sở biến mất.

## 20. Giá trị danh nghĩa và ký quỹ của hợp đồng tương lai

```text
Futures Notional = Futures Price × Contract Multiplier
```

Ký quỹ (margin) chỉ là tài sản bảo đảm, không phải toàn bộ vốn có thể mất. Quy mô vị thế phải dựa trên giá trị danh nghĩa, độ nhạy, mức lỗ trong kịch bản bất lợi và đường đi của yêu cầu ký quỹ.

## 21. Quyền chọn và các độ nhạy Greek

Giá trị tại đáo hạn:

```text
Call = max(S - K, 0)
Put  = max(K - S, 0)
```

Trước ngày đáo hạn, quyền chọn còn chịu ảnh hưởng của thời gian, biến động ngụ ý (implied volatility), lãi suất, cổ tức và cấu trúc bề mặt biến động.

Delta, Gamma, Theta, Vega và Rho là các độ nhạy cục bộ; chúng không thay thế kiểm thử nhiều kịch bản khi thị trường có cú nhảy lớn.

## 22. Quy mô vị thế theo ngân sách rủi ro

Một khung cơ bản:

```text
Position Size ≈ Allowed Loss / Loss Per Unit Under Invalidation
```

Mức lỗ cho phép phải được xem cùng tổng rủi ro đang mở của danh mục, mức trùng lặp nhân tố, thanh khoản, rủi ro nhảy giá và đòn bẩy.

## 23. Kỳ vọng toán học

```text
Expectancy = Win Rate × Average Win - Loss Rate × Average Loss
```

Tỷ lệ thắng cao không đảm bảo kỳ vọng dương. Một chiến lược bán biến động (short-volatility strategy) có thể thắng thường xuyên nhưng chịu một số khoản lỗ rất lớn ở phần đuôi phân phối.

## 24. Chỉ số tham chiếu

Chỉ số tham chiếu (benchmark) phải được chọn trước khi đánh giá kết quả và phải phù hợp với tập cơ hội đầu tư.

Một benchmark tốt giúp phân biệt kết quả đến từ beta thị trường, nghiêng nhân tố, phân bổ tài sản, lựa chọn chứng khoán, tiền tệ hay chất lượng thực thi lệnh.

Không thay benchmark sau khi chiến lược hoạt động kém chỉ để làm thành tích trông tốt hơn.

## 25. Kỷ luật dữ liệu đúng thời điểm

Mọi nghiên cứu lịch sử phải phân biệt:

```text
Ngày quan sát (Observation Date)
Ngày công bố (Publication Date)
Ngày sửa đổi dữ liệu (Revision Date)
Thời điểm ra quyết định (Decision Time)
Thời điểm thực thi (Execution Time)
```

Không được dùng dữ liệu đã được sửa đổi về sau như thể nhà đầu tư đã biết nó tại thời điểm quyết định. Đây là nguyên tắc chống thiên lệch nhìn trước (look-ahead bias).

## 26. Thứ bậc nguồn dữ liệu

Ưu tiên chung:

```text
Cơ quan quản lý / Sở giao dịch / Ngân hàng trung ương / Cơ quan thống kê
→ Báo cáo kiểm toán / Công bố chính thức của doanh nghiệp
→ Tài liệu quan hệ nhà đầu tư (IR) / Biên bản cuộc họp
→ Nhà cung cấp dữ liệu chất lượng cao
→ Báo cáo phân tích của công ty chứng khoán
→ Tin tức
→ Thảo luận cộng đồng
```

Nguồn ở tầng cao hơn không phải luôn đúng tuyệt đối, nhưng dữ kiện quan trọng nên được neo bằng nguồn sơ cấp khi có thể.

## 27. Quy tắc thời điểm cho dữ liệu động

Lãi suất chính sách, thuế, chu kỳ thanh toán, thành phần chỉ số, giới hạn sở hữu nước ngoài, quy định tiếp cận thị trường và thông số sản phẩm có thể thay đổi.

Mọi dữ liệu động nên ghi rõ `tính đến YYYY-MM-DD` hoặc kỳ tham chiếu. Nếu không có thời điểm, người đọc rất dễ nhầm dữ liệu lịch sử thành quy định hiện hành.

## 28. Kịch bản cơ sở, tích cực và tiêu cực

Ba kịch bản không nên chỉ là cộng hoặc trừ 20% một cách tùy ý. Chúng phải khác nhau ở các động lực kinh tế chính.

Ví dụ với doanh nghiệp bán dẫn:

```text
Cơ sở: ASP phục hồi vừa phải + công suất sử dụng cải thiện
Tích cực: tỷ trọng HBM tăng nhanh + kỷ luật nguồn cung được duy trì
Tiêu cực: công suất mới tăng nhanh + nhu cầu hụt kỳ vọng → ASP giảm
```

Sau đó mới chuyển các động lực thành doanh thu, biên lợi nhuận, dòng tiền và định giá.

## 29. Chất xúc tác và điều kiện vô hiệu hóa

**Chất xúc tác (catalyst)** là sự kiện hoặc dữ liệu có thể khiến thị trường cập nhật kỳ vọng. **Điều kiện vô hiệu hóa (invalidation)** là bằng chứng cho thấy luận điểm đầu tư không còn đúng.

Luận điểm không được biến thành niềm tin không thể kiểm chứng. Nếu cơ chế cốt lõi đã sai, phải cập nhật hoặc loại bỏ luận điểm.

## 30. Trước quyết định và sau kết quả

**Trước quyết định (ex-ante)** là những gì có thể biết hoặc ước tính trước khi hành động. **Sau kết quả (ex-post)** là kết quả thực tế sau đó.

Một quyết định tốt vẫn có thể dẫn đến kết quả xấu do bất định. Một quyết định tệ vẫn có thể kiếm tiền do may mắn. Khi đánh giá, phải tách chất lượng quyết định khỏi thiên lệch theo kết quả.

## 31. Phân rã kết quả đầu tư

Một lần đánh giá nên tách ít nhất:

```text
Tác động thị trường / Beta
Phân bổ tài sản
Lựa chọn chứng khoán
Nhân tố
Tiền tệ
Thu nhập
Phí và chênh lệch mua bán
Trượt giá / Tác động thị trường
Chi phí vốn / Chi phí vay
Thuế
Sai lệch hành vi
```

Mục tiêu là biết phần nào đến từ kỹ năng, phần nào đến từ rủi ro đã nhận và phần nào chỉ là may mắn.

## 32. Quy tắc viết ghi chú nghiên cứu

Một ghi chú nghiên cứu tốt cần trả lời theo thứ tự:

```text
Tôi đang phân tích điều gì?
→ Dữ kiện nào đã biết?
→ Thị trường đang kỳ vọng điều gì?
→ Động lực nào quyết định kết quả?
→ Kịch bản nào có thể xảy ra?
→ Giá hiện tại đòi hỏi điều gì?
→ Tôi đang nhận rủi ro gì?
→ Điều gì làm luận điểm sai?
→ Tôi sẽ đánh giá lại khi nào?
```

Viết câu hoàn chỉnh bằng tiếng Việt trước. Chỉ giữ từ tiếng Anh trong ngoặc khi nó là thuật ngữ chuẩn cần tra cứu.

## 33. Nguyên tắc cuối cùng

Mục tiêu của thư viện không phải là nhét càng nhiều thuật ngữ tiếng Anh càng tốt. Mục tiêu là hiểu bản chất bằng tiếng Việt nhưng vẫn nhận ra thuật ngữ gốc khi đọc báo cáo, tài liệu học thuật hoặc dữ liệu quốc tế.

Quy tắc mặc định:

```text
Tiếng Việt để hiểu → Tiếng Anh trong ngoặc để tra cứu → Viết tắt để dùng thực tế
```
