# 2. Định giá cổ phiếu: lợi suất, dòng tiền và multiples

Bài 1 đã tách quyền sở hữu, dòng tiền và tỷ số hiệu quả. Bài này dùng chúng để giải quyết câu hỏi trung tâm của định giá (valuation / 가치평가): với rủi ro và thời điểm đã biết, một dòng tiền tương lai đáng giá bao nhiêu hôm nay? Các công thức trong source không phải máy tạo giá mục tiêu; chúng là cách làm lộ giả định về tăng trưởng, rủi ro, tái đầu tư và cấu trúc vốn.

## 1. Lãi kép, tỷ suất sinh lợi (rate of return / 수익률), suất sinh lợi yêu cầu (required return / 요구수익률) và CAPM

Một khoản tiền tăng theo lãi kép:

```text
FV = PV × (1 + r)^n
PV = FV / (1 + r)^n
```

Trong đó `PV` là giá trị hiện tại, `FV` là giá trị tương lai, `r` là suất sinh lợi mỗi kỳ và `n` là số kỳ. Ví dụ 100 tăng 10% một năm thành 110 sau một năm và 121 sau hai năm; cộng 10 + 10 sẽ bỏ qua việc năm thứ hai sinh lời trên 110.

CAPM (Capital Asset Pricing Model / 자본자산가격결정모형) trong source viết logic:

```text
E(Rᵢ) = Rf + βᵢ × [E(Rm) − Rf]
```

`Rf` là lãi suất phi rủi ro, `βᵢ` là độ nhạy của tài sản với thị trường, còn `E(Rm) − Rf` là phần bù rủi ro thị trường. CAPM nối rủi ro hệ thống với suất sinh lợi yêu cầu; nó không định lượng rủi ro riêng lẻ, thanh khoản, tail risk hay sai số mô hình. Vì vậy CAPM là một giả định discount rate, không phải mô tả đầy đủ thực tế.

## 2. NPV và PVGO

NPV (Net Present Value / 순현재가치) là giá trị hiện tại của dòng tiền vào trừ vốn bỏ ra. Nếu NPV dương dưới cùng bộ giả định, dự án tạo giá trị vượt suất sinh lợi yêu cầu; nếu discount rate, dòng tiền hoặc thời hạn đổi, kết luận cũng đổi. PVGO (Present Value of Growth Opportunities) tách giá trị hiện tại của tài sản đang vận hành khỏi giá trị của cơ hội tăng trưởng. Tách này giúp hỏi đúng: giá đang trả cho lợi nhuận hiện tại hay cho tái đầu tư tương lai?

Đừng nhầm NPV dương với lợi nhuận chắc chắn. NPV là kết quả của mô hình và giả định. Hãy ghi rõ tăng trưởng, biên lợi nhuận, vốn tái đầu tư và discount rate; sau đó kiểm thử kịch bản. Đây là cầu nối sang FCFE/FCFF, nơi cùng một doanh nghiệp được nhìn từ hai nhóm người cung cấp vốn.

### Mô hình chiết khấu cổ tức (Dividend Discount Model / 배당할인모형) và tăng trưởng ổn định

Raw đặt cổ tức theo chuỗi thời gian cạnh growth rate để nhấn mạnh rằng giá cổ phiếu có thể được nhìn như giá trị hiện tại của các khoản phân phối cho cổ đông:

```text
P₀ = D₁/(1+k) + D₂/(1+k)² + ... + Pₙ/(1+k)ⁿ
```

Trong đó `Dₜ` là cổ tức kỳ `t`, `k` là suất sinh lợi yêu cầu của cổ đông và `Pₙ` là giá trị còn lại ở cuối giai đoạn dự báo. Với giả định cổ tức tăng đều mãi mãi, mô hình Gordon rút gọn thành:

```text
D₁ = D₀ × (1+g)
P₀ = D₁ / (k−g),  với k > g
```

`g` không phải tốc độ tăng doanh thu tùy ý; nó phải nhất quán với tỷ lệ giữ lại lợi nhuận, ROE, nhu cầu tái đầu tư và sức cạnh tranh dài hạn. Nếu `k` tiến sát `g`, mẫu số rất nhỏ và giá mô hình trở nên cực kỳ nhạy; nếu `k ≤ g`, công thức không cho một giá trị ổn định hữu hạn. Đây là điều kiện biên quan trọng, không phải lỗi máy tính.

Ví dụ minh họa: nếu cổ tức hiện tại `D₀ = 4`, tăng trưởng dài hạn `g = 5%` và suất sinh lợi yêu cầu `k = 11%`, thì `D₁ = 4,2` và `P₀ = 4,2/(0,11−0,05) = 70`. Nếu chỉ tăng `g` lên 6% trong khi giữ nguyên `k`, giá mô hình thành `4,24/(0,11−0,06) = 84,8`; phần tăng thêm không đến từ “cổ tức hôm nay” mà từ giả định rằng tăng trưởng cao kéo dài. Vì vậy phải kiểm thử `g` cùng ROE, payout và tái đầu tư thay vì chọn một con số thuận mắt.

Mô hình này nối với các phần sau: cổ tức là dòng tiền cho equity; FCFE mở rộng cách đo tiền có thể phân phối; còn PER/PBR/PSR là các multiple cô đọng kỳ vọng về tăng trưởng và rủi ro. Không được cộng giá trị DDM với FCFE hoặc multiple như các nguồn giá trị độc lập; chúng có thể đang đếm cùng một dòng tiền hai lần.

## 3. FCFE, FCFF và WACC

FCFE (Free Cash Flow to Equity) là tiền còn lại cho cổ đông sau chi đầu tư, thay đổi vốn lưu động và tài trợ nợ cần thiết. FCFF (Free Cash Flow to Firm) là tiền cho toàn bộ nhà cung cấp vốn trước phân phối giữa nợ và vốn chủ. Source ghi quan hệ khái quát:

```text
FCFF = FCFE + chi phí lãi sau thuế + dòng tiền trả nợ ròng
```

Ở đây **dòng tiền trả nợ ròng = nợ đã trả − nợ mới vay**. Vì vậy cách viết trên tương đương với công thức chuẩn `FCFF = FCFE + Interest×(1−T) − Net Borrowing` nếu `Net Borrowing = nợ mới vay − nợ đã trả`. Phải khóa quy ước dấu trước khi thay số; nếu không, cùng một transaction có thể bị cộng hai lần.

FCFE thường chiết khấu bằng cost of equity; FCFF chiết khấu bằng WACC (Weighted Average Cost of Capital / 가중평균자본비용). Source cho cấu trúc WACC theo trọng số vốn chủ và nợ; viết rõ theo quy ước thị trường:

```text
WACC = [E/(D+E)] × Rₑ + [D/(D+E)] × R_d × (1−T)
```

Trong đó `E` và `D` là giá trị thị trường của equity/debt, `Rₑ` là cost of equity, `R_d` là cost of debt trước thuế và `T` là thuế suất dùng cho tax shield. Cơ chế là mỗi nguồn vốn đòi một required return khác nhau; WACC là blended hurdle rate cho **FCFF** khi cấu trúc vốn/thuế phù hợp với giả định. Dùng book-value weights, trộn kỳ hạn/risk regime hoặc dùng WACC cho FCFE đều làm sai ownership của discount rate.

## 4. EVA, NOPAT, invested capital và ROIC

EVA (Economic Value Added / 경제적 부가가치) đo lợi nhuận hoạt động sau thuế vượt chi phí sử dụng vốn:

```text
EVA = NOPAT − (Invested Capital × WACC)
    = Invested Capital × (ROIC − WACC)
```

`NOPAT` là Net Operating Profit After Tax; `Invested Capital` là vốn hoạt động đã đầu tư; `ROIC = NOPAT / Invested Capital`. Khi ROIC lớn hơn WACC, mỗi đồng vốn mới tạo giá trị kinh tế; khi thấp hơn, tăng trưởng có thể phá hủy giá trị dù doanh thu tăng. Đây là cơ chế giải thích vì sao “tăng trưởng” không tự động tốt.

## 5. PER/EPS: hệ số giá trên lợi nhuận (Price-Earnings Ratio / 주가수익비율)

PER (Price–Earnings Ratio / 주가수익비율) là:

```text
PER = giá thị trường mỗi cổ phiếu / EPS
```

EPS (Earnings Per Share) là lợi nhuận quy cho một cổ phiếu theo mẫu số phù hợp. Có thể diễn giải giá = EPS × PER: thị trường vừa định giá mức lợi nhuận, vừa định giá mức multiple cho tăng trưởng và rủi ro. EPS âm, lợi nhuận chu kỳ hoặc một khoản bất thường làm PER kém ổn định; hãy dùng lợi nhuận chuẩn hóa và so sánh với doanh nghiệp cùng mô hình.

## 6. PBR (Price-to-Book Ratio / 주가순자산비율) và ROE

PBR (Price-to-Book Ratio / 주가순자산비율) so giá thị trường với BPS (Book Value Per Share):

```text
PBR = giá cổ phiếu / BPS
EPS = BPS × ROE
```

Vì vậy, cùng một PBR có thể hợp lý hoặc đắt tùy ROE và chi phí vốn. PBR thấp không tự động là rẻ: tài sản ghi sổ có thể suy giảm, ROE có thể thấp hơn cost of equity, hoặc doanh nghiệp đang phá hủy giá trị. PBR–ROE là đối chiếu giữa giá trị ghi sổ và khả năng sinh lời, không phải công thức thay thế phân tích tài sản.

## 7. PSR (Price-to-Sales Ratio / 주가매출비율) và margin

PSR (Price-to-Sales Ratio / 주가매출액비율) dùng doanh thu trên mỗi cổ phiếu (SPS):

```text
PSR = giá cổ phiếu / SPS
EPS = SPS × biên lợi nhuận
```

Doanh nghiệp biên cao có thể xứng đáng PSR cao hơn doanh nghiệp doanh thu lớn nhưng biên thấp. PSR hữu ích khi lợi nhuận tạm âm, nhưng không thể bỏ qua chi phí để biến doanh thu thành tiền. Source dùng quan hệ PSR–margin như một cảnh báo: nếu biên không cải thiện, doanh thu tăng không đủ tạo EPS.

## 8. EV/EBITDA

EV (Enterprise Value) nhìn giá trị hoạt động cho cả chủ nợ và cổ đông; dạng khái quát `EV = equity value + nợ chịu lãi − tiền và tương đương tiền`. EBITDA (Earnings Before Interest, Tax, Depreciation and Amortization) gần với lợi nhuận hoạt động trước khấu hao, nhưng không phải dòng tiền tự do. `EV/EBITDA` hữu ích để so sánh cấu trúc vốn khác nhau, song dễ sai với doanh nghiệp cần capex lớn, thuê tài sản nhiều hoặc có vốn lưu động biến động.

## 9. Quy trình dùng multiple

Đọc bảng multiple theo bốn bước: (1) xác định numerator và denominator; (2) kiểm tra chất lượng và chu kỳ của denominator; (3) so với nhóm tương đồng; (4) nối multiple với tăng trưởng, biên, ROIC và rủi ro. Không dùng nhiều tỷ số để tạo ảo giác đồng thuận: PER, PBR, PSR và EV/EBITDA có thể cùng sai nếu dự báo dòng tiền sai.

## 10. Worked valuation bridge

Giả sử `Rf = 5%`, beta bằng `1,2` và phần bù rủi ro thị trường là `5%`. CAPM cho suất sinh lợi yêu cầu khoảng `5% + 1,2 × 5% = 11%`. Con số 11% chưa phải giá trị cổ phiếu; nó chỉ là tỷ lệ dùng để chiết khấu dòng tiền có rủi ro tương tự. Nếu doanh nghiệp có nợ, dòng tiền cho toàn công ty còn cần WACC; nếu định giá trực tiếp phần cổ đông, FCFE phải đi với cost of equity.

Với một dự án bỏ ra 100 hôm nay và nhận 60 rồi 70 trong hai năm, NPV ở 10% là:

```text
NPV = −100 + 60/1,10 + 70/(1,10)^2 ≈ 12,40
```

NPV dương trong ví dụ này chỉ nói rằng dòng tiền giả định vượt hurdle rate 10%; bảng độ nhạy dưới đây cho thấy biên an toàn thay đổi thế nào khi discount rate đổi.

Để thấy kết luận phụ thuộc giả định ra sao, giữ nguyên dòng tiền nhưng đổi discount rate:

| Discount rate | NPV xấp xỉ | Cách đọc |
|---:|---:|---|
| 8% | 15,57 | Biên an toàn rộng hơn vì suất chiết khấu thấp hơn |
| 10% | 12,40 | Kịch bản cơ sở của ví dụ |
| 20% | −1,39 | Giá trị hiện tại không còn bù vốn bỏ ra |

NPV dương trong ví dụ này chỉ nói rằng dòng tiền giả định vượt hurdle rate 10%. Nếu doanh thu giảm, capex tăng hoặc discount rate lên 20%, NPV có thể âm. Bảng độ nhạy không dự báo mức nào sẽ xảy ra; nó chỉ cho biết luận điểm nhạy nhất với biến nào và khi nào cần vô hiệu hóa mô hình.

## 11. Tam giác kiểm tra multiple

Giả sử một cổ phiếu có EPS chuẩn hóa 5 và giá 75, PER là 15 lần. Để biết 15 lần có hợp lý không, cần nối ba câu hỏi: lợi nhuận 5 có lặp lại không; ROE và tái đầu tư có đủ để tăng EPS không; và 15 lần đang cao hay thấp so với rủi ro, tăng trưởng và cost of equity của nhóm tương đồng. Nếu EPS tăng do bán tài sản, PER thấp là ảo; nếu EPS đang ở đáy chu kỳ, PER cao chưa chắc đắt.

Tương tự, PBR phải đọc cùng ROE và chất lượng tài sản; PSR phải đọc cùng margin; EV/EBITDA phải đọc cùng capex và nợ. Ba cặp này là các phép kiểm chéo, không phải ba phiếu bầu độc lập. Khi chúng mâu thuẫn, quay về báo cáo và dòng tiền ở bài 1 thay vì lấy trung bình các multiple.

## 12. Điều kiện vô hiệu hóa luận điểm định giá

Một luận điểm định giá cần được coi là sai nếu một trong bốn điều kiện xảy ra: denominator không còn phản ánh hoạt động bình thường; tăng trưởng đòi hỏi tái đầu tư lớn hơn mô hình; ROIC giảm dưới WACC; hoặc discount rate tăng vì rủi ro hệ thống/liquidity. Viết trước các điều kiện này giúp phân biệt “giá chưa chạy” với “mô hình đã hỏng”.

## Chốt và bàn giao

Invariant của bài là “giá trị = dòng tiền hoặc lợi nhuận tương lai được quy đổi theo rủi ro và thời gian”. Ranh giới là mọi công thức phụ thuộc giả định và đối tượng dòng tiền. Bài 3 chuyển từ giá trị nội tại sang dữ liệu giá/khối lượng: tín hiệu kỹ thuật có thể giúp mô tả hành vi thị trường, nhưng không chứng minh doanh nghiệp đáng giá hơn. Xem [Phân tích kỹ thuật](./03_TECHNICAL_ANALYSIS.md).
