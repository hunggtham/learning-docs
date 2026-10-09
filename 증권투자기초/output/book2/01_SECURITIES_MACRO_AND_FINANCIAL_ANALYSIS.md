# 1. Nền tảng đầu tư, chứng khoán và phân tích kinh tế–tài chính

Sách mở bằng một phân biệt nền tảng: đầu tư là từ bỏ tiêu dùng hiện tại để nhận dòng lợi ích tương lai, còn phân tích chứng khoán (securities analysis / 증권분석) là tìm xem quyền lợi đó được tạo ra và định giá qua cơ chế nào. Bài này nối khái niệm đầu tư với chu kỳ kinh doanh, chỉ báo kinh tế, báo cáo tài chính và các tỷ số hiệu quả. Khi nắm được chuỗi đó, người học có thể đọc các công thức định giá ở bài 2 mà không nhầm giá thị trường với giá trị kinh tế.

## 1. Đầu tư, tài sản và chứng khoán

Đầu tư thực (real investment / 실물투자) tạo ra hoặc mở rộng năng lực sản xuất, như máy móc, nhà xưởng hay hàng tồn kho. Đầu tư tài chính (financial investment / 금융투자) mua một quyền đòi hỏi đối với dòng tiền hoặc tài sản của tổ chức khác. Chứng khoán (securities / 증권) là quyền tài chính được phát hành theo một cấu trúc pháp lý; trong source, hai dạng nền tảng là cổ phiếu và trái phiếu. Cổ phiếu (stock / 주식) đại diện cho quyền sở hữu residual: cổ đông nhận phần còn lại sau khi doanh nghiệp thanh toán nghĩa vụ. Trái phiếu (bond / 채권) là quyền đòi hỏi theo hợp đồng: coupon và gốc được ưu tiên hơn cổ tức nhưng bị giới hạn theo điều khoản.

Vì hai loại quyền lợi có cơ chế khác nhau, cùng một “lợi suất” không có nghĩa cùng một rủi ro. Cổ phiếu phụ thuộc vào lợi nhuận tương lai, pha loãng và định giá kỳ vọng; trái phiếu phụ thuộc vào khả năng trả nợ, lãi suất và thời hạn. Chứng chỉ, quỹ và chỉ số gom các quyền lợi đó thành sản phẩm hoặc thước đo. Đọc phần sau theo câu hỏi “dòng tiền nào trả cho ai, trong điều kiện nào?”; đó là invariant cần mang sang định giá.

## 2. Từ nền kinh tế đến giá chứng khoán

### Ba chân trời của chu kỳ

Các khoảng thời gian dưới đây là cách source textbook phân biệt chân trời, không phải quy luật cố định:

| Chu kỳ | Khoảng xấp xỉ đọc được từ source | Cơ chế cần đặt cạnh dữ liệu |
|---|---:|---|
| Kitchin | khoảng 3–5 năm | tồn kho, đơn hàng và điều chỉnh sản xuất |
| Juglar | khoảng 7–11 năm | đầu tư máy móc, tín dụng và năng lực sản xuất |
| Kondratiev | khoảng 50–60 năm | đổi mới công nghệ, cấu trúc vốn và thay đổi dài hạn |

Một nền kinh tế có thể đồng thời ở pha tồn kho giảm của Kitchin nhưng vẫn trong chu kỳ đầu tư dài hơn. Vì vậy không nên dùng một con số chu kỳ để dự báo ngày đảo chiều; hãy hỏi dữ liệu nào đang vận động ở đúng chân trời đó.

Giá không chỉ phản ứng với một tin đơn lẻ. Chu kỳ kinh doanh (business cycle / 경기순환) nối sản lượng, doanh thu, lợi nhuận, lãi suất và khẩu vị rủi ro. Hãy dùng bảng trên để chọn đúng chân trời trước khi gắn một thay đổi dữ liệu vào câu chuyện tăng trưởng hoặc suy thoái.

GDP (Gross Domestic Product / 국내총생산) đo giá trị sản lượng cuối cùng trong nền kinh tế. Với nhà đầu tư, GDP hữu ích khi đặt cạnh lợi nhuận doanh nghiệp, cơ cấu ngành và chính sách, chứ không phải khi dùng nó như đại diện trực tiếp cho giá cổ phiếu. Tăng trưởng có thể đi cùng lạm phát, thắt chặt tiền tệ hoặc biên lợi nhuận giảm. Vì vậy, từ GDP phải đi tiếp qua kênh doanh thu → chi phí → dòng tiền → discount rate.

### Tỷ giá trong block chỉ báo vĩ mô của source

Source dành một tiểu mục riêng cho cách yết tỷ giá (exchange-rate quotation / 환율표시) và minh họa hai cách viết nghịch đảo. Với ví dụ OCR còn đọc được:

```text
1 USD = 1.300 KRW
1 KRW ≈ 1 / 1.300 USD ≈ 0,00077 USD
```

Hai cách yết là hai biểu diễn của cùng một quan hệ giá; đổi chiều quote phải lấy nghịch đảo, không được chỉ đổi ký hiệu tiền tệ. Source dùng nhãn `European term` và `American term`; khi áp dụng thực tế phải khóa rõ “đồng tiền nào là base, đồng nào là quote”, vì direct/indirect quotation phụ thuộc góc nhìn đồng nội tệ.

Cross rate được suy ra từ hai cặp có đồng tiền chung. Nếu biết `KRW/USD` và `JPY/USD`, thì một cross rate KRW/JPY có thể suy ra bằng cách chia hai quote sau khi đưa chúng về cùng orientation. Boundary quan trọng là bid/ask, spread, thời điểm giá và convention của từng thị trường; phép nghịch đảo số giữa không tự tái tạo spread giao dịch thật.

Tỷ giá đi vào phân tích chứng khoán qua doanh thu, chi phí nhập khẩu, nợ ngoại tệ và discount rate. Đồng nội tệ yếu có thể hỗ trợ doanh thu quy đổi của exporter nhưng đồng thời làm nguyên liệu nhập khẩu và nợ ngoại tệ đắt hơn; vì vậy không dùng một chiều “KRW yếu = cổ phiếu xuất khẩu tăng” như quy tắc máy móc.

## 3. Chỉ báo tâm lý và khảo sát

Trong nhóm chỉ báo kinh tế (economic indicators / 경제지표), source có công thức cho CSI (Consumer Sentiment Index / 소비자심리지수) và BSI (Business Survey Index / 기업경기실사지수). BSI được xây từ số câu trả lời tích cực và tiêu cực; một dạng chuẩn hóa đọc được là:

```text
BSI = [(số tích cực − số tiêu cực) / tổng số trả lời] × 100 + 100
```

### CSI: đọc công thức cùng giới hạn của OCR

Ví dụ CSI trong source có bốn nhóm trả lời hiện tại/kỳ vọng, tích cực/tiêu cực. Dạng reconstruct từ các số còn đọc được là:

```text
CSI ≈ [(tích cực hiện tại + tích cực kỳ vọng − tiêu cực hiện tại − tiêu cực kỳ vọng) / tổng số trả lời] × 100 + 100
```

Với các số 10, 20, 50 và 50 trên tổng 200 câu trả lời, kết quả là `[(10 + 20 − 50 − 50) / 200] × 100 + 100 = 65`. Vì OCR không bảo đảm toàn bộ tên biến và trọng số gốc, công thức này được dùng để giải thích ví dụ source chứ không được xem là đặc tả hiện hành của một khảo sát cụ thể.

Ví dụ source dùng 300 tích cực, 200 tiêu cực trên 500 câu trả lời: BSI = 120. Chỉ số trên 100 cho thấy số dư kỳ vọng tích cực trong mẫu khảo sát, không nói rằng GDP hay giá cổ phiếu chắc chắn tăng. CSI cũng cần được đọc như cán cân kỳ vọng trong mẫu, với ví dụ source cho giá trị 65; không biến một ngưỡng đơn lẻ thành tín hiệu mua bán.

Composite Index (CI / 경기종합지수) gộp nhiều chỉ báo; Diffusion Index (DI / 경기확산지수) quan sát độ rộng số thành phần đang cải thiện. CI trả lời mức độ tổng hợp, DI trả lời mức độ lan tỏa. Hai chỉ số có thể lệch nhau: một vài thành phần lớn kéo CI lên trong khi phần lớn thành phần vẫn yếu. Đây là lý do cần đặt khảo sát cạnh dữ liệu thực tế và chu kỳ, thay vì thay thế chúng.

### Worked CI–DI: mức tăng lớn nhưng độ rộng yếu

Giả sử một composite index có hai thành phần lớn, trọng số lần lượt 40% và 30%, cùng tăng 10%; ba thành phần còn lại, mỗi thành phần trọng số 10%, cùng giảm 2%. Thay đổi tổng hợp minh họa là `0,4×10% + 0,3×10% − 3×0,1×2% = 6,4%`, nên CI tăng khá mạnh. Nhưng chỉ 2/5 thành phần cải thiện, DI theo breadth chỉ là 40%. Tín hiệu lúc này là “mức tổng hợp được kéo bởi nhóm lớn, độ lan tỏa yếu”, không phải một đợt tăng đồng đều.

Ngược lại, nếu 4/5 thành phần cùng tăng 2% nhưng thành phần lớn nhất giảm 5%, DI có thể cao trong khi CI vẫn giảm. Khi hai chỉ số lệch nhau, hãy kiểm tra trọng số, ngành dẫn dắt, số thành phần thực sự cải thiện và thời điểm khảo sát. Không dùng CI để che độ rộng yếu, cũng không dùng DI để bỏ qua cú sốc ở một thành phần có trọng số hệ thống.

### Độ trễ của chỉ báo và bài kiểm tra lệch pha

Không phải chỉ báo nào cũng đo cùng một thời điểm. Hãy phân loại trước khi suy luận:

| Loại chỉ báo | Quan hệ với chu kỳ | Cách dùng thận trọng |
|---|---|---|
| Dẫn dắt (leading) | thường đổi trước hoạt động thực | dùng để tạo giả thuyết, không xác nhận kết quả |
| Đồng thời (coincident) | vận động gần cùng thời điểm với hoạt động | dùng để kiểm tra trạng thái hiện tại |
| Trễ (lagging) | phản ứng sau khi chu kỳ đã đổi | dùng để xác nhận hậu nghiệm, không timing sớm |

Nếu BSI tăng lên 120 trong khi GDP hoặc doanh số hiện tại còn giảm, có ít nhất hai cách đọc: kỳ vọng doanh nghiệp đang quay đầu trước dữ liệu cứng, hoặc mẫu khảo sát chưa đại diện cho ngành chịu suy yếu. Cách phân biệt là kiểm tra độ rộng theo ngành, thời điểm khảo sát, đơn hàng, sản lượng, vốn lưu động và dòng tiền; không chọn cách giải thích thuận lợi chỉ vì chỉ số vượt 100.

Mental model là `kỳ vọng → dữ liệu hoạt động → báo cáo tài chính → định giá`. Chỉ báo dẫn dắt mở ra câu hỏi, chỉ báo đồng thời kiểm tra hiện trạng, còn chỉ báo trễ giúp biết giả thuyết trước đó có đúng không. Nhờ vậy CSI/BSI được dùng như một mắt xích trong chuỗi, không phải tín hiệu mua bán độc lập.

## 4. Phân tích doanh nghiệp và báo cáo tài chính

Phân tích cơ bản (fundamental analysis / 기본적 분석) đi từ ngành và môi trường kinh tế đến doanh nghiệp, rồi từ doanh thu đến lợi nhuận và dòng tiền. Báo cáo tài chính (financial statements / 재무제표) là ngôn ngữ đo lường của quá trình đó: bảng cân đối cho biết nguồn lực và nghĩa vụ tại một thời điểm; báo cáo kết quả kinh doanh cho biết doanh thu, chi phí và lợi nhuận trong kỳ; báo cáo lưu chuyển tiền tệ kiểm tra lợi nhuận có chuyển thành tiền hay không. Source nhấn mạnh IFRS (International Financial Reporting Standards), IASC/IAS và K-IFRS; đây là khuôn khổ ghi nhận và trình bày, không phải bảo đảm chất lượng kinh tế của doanh nghiệp.

Khi đọc một khoản mục, cần giữ ba lớp: định nghĩa kế toán, cơ chế kinh tế và giới hạn so sánh. Doanh thu có thể tăng nhưng vốn lưu động hút tiền; lợi nhuận có thể tăng nhưng do đánh giá lại; tài sản ghi sổ có thể khác xa giá trị thay thế. Vì vậy, hãy đi từ báo cáo sang KPI ngành, chất lượng lợi nhuận và dòng tiền trước khi dùng multiple ở bài 2. Phần chuyên sâu thuộc owner [Financial Statements and Accounting](../../../investing/03_company_analysis/01_FINANCIAL_STATEMENTS_AND_ACCOUNTING.md).

Source còn đặt báo cáo vào một quy trình phân tích thay vì xem từng bảng riêng lẻ: bắt đầu ở ngành và vị thế cạnh tranh, đọc bảng cân đối để biết nguồn lực–nghĩa vụ, đọc kết quả kinh doanh để theo dõi doanh thu–chi phí–lợi nhuận, rồi đối chiếu lưu chuyển tiền tệ và thuyết minh. IFRS/IASC và K-IFRS định nghĩa cách ghi nhận, đo lường và trình bày; chúng giúp so sánh có kỷ luật nhưng không xóa khác biệt mô hình kinh doanh. Vì thế cùng một chỉ tiêu phải được hỏi thêm “được tạo ra bởi hoạt động nào, có lặp lại không, và chuyển thành tiền khi nào?”.

### Industry lifecycle: tăng trưởng không đồng nghĩa chất lượng đầu tư

Khối industry analysis của source dùng life cycle để tách bốn pha thường gặp: **introduction → growth → maturity → decline**. Cơ chế cần đọc là sự thay đổi của cầu, số đối thủ, nhu cầu vốn và khả năng tạo tiền:

| Pha | Cơ chế thường thấy | Câu hỏi đầu tư |
|---|---|---|
| Introduction | cầu còn nhỏ, chi phí xây thị trường cao, mô hình chưa ổn định | ai tài trợ burn rate và khi nào unit economics có thể đứng vững? |
| Growth | cầu tăng nhanh, nhiều đối thủ vào, capex/vốn lưu động tăng | tăng trưởng có tạo ROIC vượt cost of capital không? |
| Maturity | tăng trưởng chậm lại, cạnh tranh chuyển sang giá/hiệu suất | ai có moat, pricing power và dòng tiền bền? |
| Decline | cầu cấu trúc suy giảm hoặc bị công nghệ/thay thế lấn át | cash harvest còn hợp lý hay tài sản trở thành stranded asset? |

Đây là framework để đặt câu hỏi, không phải đồng hồ xác định giá cổ phiếu. Một ngành “growth” vẫn có thể là khoản đầu tư xấu nếu định giá quá cao hoặc cạnh tranh làm ROIC sụt; một ngành “mature” vẫn có thể tạo total return tốt nếu cash flow và capital allocation đủ mạnh.

### Từ industry analysis sang company analysis

Source tiếp tục từ ngành sang doanh nghiệp: định lượng quy mô/tăng trưởng và đặt cạnh các yếu tố định tính như vị thế cạnh tranh, cấu trúc chi phí, năng lực quản lý và chiến lược phân bổ vốn. Learning route dùng nguyên tắc `ngành → vị thế doanh nghiệp → báo cáo → tỷ số → định giá`; cross-link canonical sâu hơn nằm ở [Company Analysis](../../../investing/03_company_analysis/README.md).

### Ma trận BCG: vị thế cạnh tranh không đồng nghĩa chất lượng đầu tư

Source dùng ma trận BCG (BCG matrix / BCG 매트릭스) để đặt từng đơn vị kinh doanh trên hai trục: tốc độ tăng trưởng của thị trường và thị phần tương đối. Bốn nhãn cần đọc như các câu hỏi về phân bổ vốn:

| Ô của ma trận | Tình huống khái quát | Câu hỏi phân tích tiếp theo |
|---|---|---|
| Question Mark | thị trường tăng nhanh nhưng thị phần tương đối thấp | Có lợi thế đủ bền để tiếp tục đầu tư, hay nên rút vốn? |
| Star | thị trường tăng nhanh và thị phần tương đối cao | Tăng trưởng cần bao nhiêu vốn lưu động/capex trước khi tạo tiền? |
| Cash Cow | thị trường tăng chậm nhưng thị phần tương đối cao | Dòng tiền dư có thể tài trợ đơn vị khác hay đang bị hút bởi nợ/capex? |
| Barking Dog | thị trường tăng chậm và thị phần thấp | Có lý do chiến lược để giữ lại, hay chi phí cơ hội đã quá lớn? |

Ma trận này không tự đo profitability, ROIC, chất lượng tài sản hay định giá cổ phiếu. Một `Star` có thể tăng doanh thu nhưng tiêu nhiều tiền; một `Cash Cow` có thể tạo tiền ổn định nhưng đang suy giảm cấu trúc; một `Question Mark` chỉ đáng tài trợ nếu giả thuyết về thị phần, biên lợi nhuận và economics của khách hàng có thể kiểm chứng. Vì vậy hãy nối từng ô với chuỗi `tăng trưởng thị trường → thị phần → tái đầu tư → dòng tiền → ROIC`, thay vì dùng nhãn BCG như kết luận.

Ví dụ, nếu một mảng có tăng trưởng thị trường 15% nhưng thị phần tương đối 0,6, nó nằm gần `Question Mark`: bước tiếp theo không phải mua vì “tăng trưởng cao”, mà là kiểm tra chi phí giành khách hàng, khả năng nâng thị phần và vốn cần bỏ ra. Nếu một mảng khác tăng trưởng 3% nhưng thị phần tương đối 1,4, nó gần `Cash Cow`; hãy kiểm tra liệu dòng tiền thực sự dương sau capex và vốn lưu động. Các ngưỡng cụ thể phụ thuộc cách doanh nghiệp định nghĩa thị trường, nên đây là ví dụ mental model, không phải chuẩn phân loại phổ quát.

### Các họ tỷ số tài chính (financial ratios / 재무비율) trong source

Source có một block tỷ số lớn trước ROI/ROE. OCR của một số nhãn và mẫu số bị hỏng, nên learning route không gán tên công thức khi evidence không đủ; nhưng mục đích kinh tế của bốn họ tỷ số vẫn đọc được:

| Họ tỷ số | What | Why / mechanism | Boundary |
|---|---|---|---|
| Liquidity | so nguồn lực ngắn hạn với nghĩa vụ ngắn hạn | kiểm tra khả năng đáp ứng cash need gần hạn | tài sản ngắn hạn kém thanh khoản có thể làm ratio đẹp giả |
| Leverage / solvency | so nợ với vốn hoặc khả năng trả lãi | đòn bẩy khuếch đại ROE nhưng cũng khuếch đại default/refinancing risk | phải đọc maturity, fixed/floating rate và covenant |
| Activity / turnover | đo doanh thu hoặc chi phí trên tài sản, tồn kho, khoản phải thu | cho biết vốn bị khóa nhanh hay chậm | vòng quay cao có thể do tồn kho quá thấp hoặc credit policy quá chặt |
| Profitability | nối lợi nhuận với sales, assets hoặc equity | tách margin, asset efficiency và leverage | lợi nhuận bất thường và denominator cuối kỳ có thể bóp méo kết luận |

Các công thức OCR xác nhận chắc nhất trong block này là ROI và ROE ở phần kế tiếp. Những công thức trước đó có ký hiệu/mẫu số bị hỏng được giữ trong coverage dưới `SOURCE_AMBIGUITY`, thay vì “khôi phục” bằng công thức chuẩn từ trí nhớ.

## 5. ROI và ROE

Tỷ suất sinh lợi trên đầu tư (Return on Investment, ROI / 투자수익률) đo lợi nhuận so với khoản đầu tư; tỷ suất sinh lợi trên vốn chủ sở hữu (Return on Equity, ROE / 자기자본이익률) đo lợi nhuận quy cho vốn chủ sở hữu. Dạng khái quát:

```text
ROI = lợi nhuận / vốn đầu tư × 100%
ROE = lợi nhuận sau thuế / vốn chủ sở hữu bình quân × 100%
```

ROE cao có thể đến từ biên lợi nhuận tốt, sử dụng tài sản hiệu quả hoặc đòn bẩy cao. Vì mẫu số khác nhau, không được xếp hạng doanh nghiệp chỉ bằng một tỷ số. ROE là đầu vào trực tiếp cho quan hệ PBR–ROE ở bài 2; nếu bỏ qua đòn bẩy và chất lượng lợi nhuận, multiple sẽ bị đọc sai.

### Tách ROE thành ba cơ chế

Để không dừng ở kết luận “ROE cao”, hãy phân rã nó thành khả năng giữ lại lợi nhuận, sử dụng tài sản và mức dùng vốn vay. Dạng DuPont khái quát là:

```
ROE = biên lợi nhuận ròng × vòng quay tài sản × hệ số nhân vốn chủ
```

Trong tính toán thực tế, lợi nhuận, tài sản và vốn chủ nên dùng cùng kỳ và nhất quán giữa số đầu kỳ–cuối kỳ; nếu dùng số cuối kỳ cho một thành phần và số bình quân cho thành phần khác, DuPont sẽ tạo ra tín hiệu giả.

Ví dụ, biên ròng 8%, vòng quay tài sản 1,2 lần và hệ số nhân vốn chủ 1,5 lần cho ROE khoảng 8% × 1,2 × 1,5 = 14,4%. Nếu ROE tăng lên 19,2% chỉ vì hệ số nhân tăng từ 1,5 lên 2,0, chất lượng cải thiện khác hoàn toàn trường hợp biên lợi nhuận tăng. Trường hợp thứ nhất dựa nhiều hơn vào đòn bẩy, nên phải kiểm tra chi phí lãi, đáo hạn nợ và khả năng chịu suy giảm doanh thu.

Phân rã này không thay thế báo cáo tài chính: nó chỉ nói **ROE tăng bằng kênh nào**. Khi chuyển sang PBR ở bài 2, hãy ghép ROE với cost of equity và độ bền của từng kênh; một multiple thấp không hấp dẫn nếu ROE cao chỉ do đòn bẩy tạm thời.

## 6. Worked chain: từ chỉ báo đến luận điểm doanh nghiệp

Hãy coi một chỉ báo là điểm bắt đầu của chuỗi, không phải kết luận. Nếu BSI tăng trên 100, giả thuyết đầu tiên là kỳ vọng doanh nghiệp cải thiện. Bước kế tiếp là hỏi ngành nào trả lời tích cực, doanh thu nào có thể tăng, chi phí đầu vào và lãi vay có tăng nhanh hơn không, rồi kiểm tra xem lợi nhuận có chuyển thành CFO hay bị vốn lưu động hút mất. Chỉ khi chuỗi `kỳ vọng → hoạt động → lợi nhuận → tiền` nhất quán, chỉ báo mới có thể trở thành một phần của luận điểm.

Ví dụ, một nhà sản xuất có thể hưởng lợi từ cầu tăng nhưng đồng thời phải dự trữ hàng tồn kho và vay ngắn hạn. Doanh thu tăng làm GDP/BSI narrative đẹp hơn, nhưng dòng tiền hoạt động âm và lãi vay tăng có thể làm ROE giảm. Cùng một tín hiệu vĩ mô vì thế có thể tốt cho doanh thu nhưng xấu cho khả năng thanh toán. Đây là lý do source đặt chu kỳ, báo cáo và tỷ số cạnh nhau.

## 7. Checklist đọc báo cáo không nhầm số liệu với cơ chế

Trước khi chuyển sang định giá, hãy ghi bốn dòng: (1) doanh nghiệp bán gì và ở thị trường nào; (2) lợi nhuận đến từ giá, sản lượng, biên hay khoản bất thường; (3) tài sản và nợ nào tài trợ hoạt động; (4) chênh lệch giữa lợi nhuận và dòng tiền đến từ vốn lưu động, capex hay ghi nhận kế toán nào. Nếu không trả lời được dòng thứ tư, chưa nên dùng PER/PBR/EV/EBITDA. Bài 2 sẽ dùng chính các câu trả lời này để chọn denominator phù hợp.

## Chốt và bàn giao

Mental model của bài này là “điều kiện kinh tế → hoạt động doanh nghiệp → dòng tiền/quyền lợi → thước đo”. Ranh giới quan trọng là chỉ báo vĩ mô và tỷ số kế toán đều là phép đo có định nghĩa, không phải lời tiên tri. Bài 2 dùng dòng tiền, suất sinh lợi yêu cầu và tỷ số đó để trả lời doanh nghiệp đáng giá bao nhiêu; hãy đọc tiếp [Định giá cổ phiếu](./02_EQUITY_VALUATION_AND_MULTIPLES.md).
