# Tình huống 01 — Từ cú sốc CPI tới quyết định danh mục

> Đây là một tình huống tích hợp nhiều lĩnh vực. Mục tiêu không phải học khẩu quyết `CPI tăng → cổ phiếu giảm`, mà hiểu một mức CPI gây bất ngờ so với kỳ vọng (CPI surprise) truyền qua lãi suất, tỷ giá, tín dụng, lợi nhuận doanh nghiệp, định giá, danh mục và thực thi lệnh như thế nào. Toàn bộ ví dụ đều là giả định để giữ tính dùng lại lâu dài.

## 1. Bối cảnh giả định

Giả sử trước ngày công bố CPI, thị trường đang kỳ vọng lạm phát tiếp tục giảm. Mức đồng thuận (consensus) của CPI toàn phần là 2,8% so với cùng kỳ và CPI lõi là 2,9%. Thị trường cũng đang phản ánh khả năng khá cao rằng ngân hàng trung ương sẽ bắt đầu hạ lãi suất trong vài cuộc họp tới.

Số liệu thực tế:

```text
CPI toàn phần: 3,2%
CPI lõi: 3,3%
Nhà ở: vẫn dai dẳng
Dịch vụ lõi ngoài nhà ở: còn mạnh
Lạm phát hàng hóa: gần như đi ngang
```

Điểm đầu tiên không phải hỏi “3,2% có cao không?”, mà hỏi **mức chênh so với điều thị trường đã phản ánh vào giá là bao nhiêu**. Cùng mức 3,2%, phản ứng sẽ khác nếu thị trường đã kỳ vọng 3,1% thay vì 2,8%.

## 2. Tách cấu phần lạm phát

Lạm phát không phải một con số duy nhất. Nên tách ít nhất:

```text
Hàng hóa
Nhà ở
Dịch vụ
Năng lượng
Thực phẩm
Tiền lương / Chi phí lao động trên một đơn vị sản lượng
```

Lạm phát hàng hóa có thể thay đổi do chuỗi cung ứng. Giá nhà ở thường phản ánh thị trường thuê nhà với độ trễ. Lạm phát dịch vụ thường gắn chặt hơn với tiền lương và nhu cầu nội địa.

Nếu bất ngờ chủ yếu đến từ cú tăng năng lượng tạm thời, hàm phản ứng của ngân hàng trung ương có thể khác với trường hợp dịch vụ lõi vẫn dai dẳng. Vì vậy cấu phần quan trọng hơn chỉ số tiêu đề.

Đọc thêm: [Macro Data Playbook](../04_economics/03_MACRO_DATA_PLAYBOOK.md).

## 3. Cập nhật hàm phản ứng của ngân hàng trung ương

Ngân hàng trung ương không phản ứng với CPI một cách máy móc. Thị trường sẽ hỏi:

```text
Lạm phát có dai dẳng không?
Thị trường lao động còn quá chặt không?
Tăng trưởng còn đủ mạnh không?
Điều kiện tài chính đang nới hay siết?
Kỳ vọng lạm phát còn được neo giữ không?
```

Nếu dịch vụ lõi còn mạnh và việc làm chưa hạ nhiệt, thị trường có thể đẩy đường đi kỳ vọng của lãi suất chính sách lên cao hơn. Nếu tăng trưởng đã suy yếu mạnh, cùng một mức CPI bất ngờ có thể tạo phản ứng nhỏ hơn.

Chuỗi tư duy:

```text
CPI gây bất ngờ
→ Đánh giá độ dai dẳng
→ Hàm phản ứng (reaction function)
→ Đường đi kỳ vọng của lãi suất chính sách
```

## 4. Lợi suất đầu ngắn của đường cong

Lợi suất 2 năm thường nhạy với kỳ vọng về lãi suất chính sách. Nếu thị trường trì hoãn kỳ vọng hạ lãi suất, lợi suất 2 năm có thể tăng nhanh.

Nếu CPI cao hơn dự kiến nhưng lợi suất 2 năm gần như không phản ứng, có thể cú sốc đã được phản ánh trước hoặc cấu phần được xem là tạm thời.

## 5. Lợi suất đầu dài và phần bù kỳ hạn

Lợi suất 10 năm hoặc 30 năm phản ứng phức tạp hơn. Chúng có thể tăng do:

```text
Kỳ vọng lãi suất ngắn hạn cao hơn
Bất định lạm phát cao hơn
Phần bù kỳ hạn (term premium) cao hơn
```

Nếu thị trường cho rằng chính sách chặt hơn sẽ làm tăng trưởng tương lai giảm mạnh, đầu dài có thể tăng ít hơn đầu ngắn, tạo đường cong phẳng hơn. Nếu đồng thời có áp lực phát hành trái phiếu và phần bù kỳ hạn tăng, đầu dài có thể tăng mạnh hơn.

Đọc thêm: [Trái phiếu, lãi suất và tín dụng](../02_asset_classes/02_BONDS_RATES_AND_CREDIT.md).

## 6. Lợi suất thực và duration của cổ phiếu

Giá trị cổ phiếu có thể được hiểu như giá trị hiện tại của dòng tiền tương lai. Những doanh nghiệp có phần lớn dòng tiền nằm xa trong tương lai thường có duration cổ phiếu dài hơn.

```text
Lợi suất thực tăng
→ Tỷ lệ chiết khấu tăng
→ Giá trị hiện tại của dòng tiền xa giảm
→ Hệ số định giá của cổ phiếu duration dài chịu áp lực
```

Điều này không có nghĩa cổ phiếu công nghệ luôn giảm khi lợi suất tăng. Nếu kỳ vọng lợi nhuận tăng nhanh hơn tác động của tỷ lệ chiết khấu, giá cổ phiếu vẫn có thể tăng. Luôn tách **tác động lợi nhuận** và **tác động hệ số định giá**.

## 7. Kênh USD và tỷ giá địa phương

Nếu lãi suất Mỹ kỳ vọng tăng tương đối so với các nền kinh tế khác, USD thường nhận hỗ trợ. Nhưng tỷ giá còn chịu dòng vốn tránh rủi ro, điều kiện thương mại, can thiệp và chính sách nội địa.

Với Hàn Quốc:

```text
Lợi suất Mỹ tăng
→ USD mạnh hơn
→ USD/KRW tăng
→ Áp lực lạm phát nhập khẩu và điều kiện tài chính tăng
```

Doanh nghiệp xuất khẩu có thể hưởng lợi khi quy đổi doanh thu USD sang KRW, nhưng dòng vốn nước ngoài và hệ số định giá có thể đi ngược lại.

Với Việt Nam, USD mạnh có thể làm thu hẹp dư địa nới lỏng nếu VND chịu áp lực.

Đọc thêm: [Cú sốc liên thị trường](../06_markets_korea_vietnam/03_CROSS_MARKET_GLOBAL_SHOCKS.md).

## 8. Điều kiện tín dụng

Nếu CPI cao hơn dự kiến khiến kỳ vọng lãi suất duy trì cao lâu hơn, chi phí tái cấp vốn tăng. Tác động lớn hơn với:

```text
Người vay lãi suất thả nổi
Doanh nghiệp có nợ đáo hạn gần
Khả năng trả lãi thấp
Bất động sản dùng đòn bẩy cao
Doanh nghiệp nhỏ phụ thuộc vốn vay
```

Nếu lợi suất trái phiếu chính phủ tăng nhưng chênh lệch tín dụng chưa mở rộng, cú sốc có thể chủ yếu là rủi ro lãi suất. Nếu cả hai cùng tăng, điều kiện tài chính đang siết rộng hơn.

## 9. Lập bản đồ theo ngành

### Ngân hàng

Lãi suất cao hơn có thể hỗ trợ biên lãi ròng (NIM) lúc đầu, nhưng chi phí vốn và tổn thất tín dụng có thể tăng về sau. Tác động có độ trễ.

### REIT và bất động sản

Tỷ lệ chiết khấu và cap rate cao hơn gây áp lực định giá; chi phí tái cấp vốn cũng tăng. Nếu tiền thuê và NOI tăng tốt, một phần tác động có thể được bù lại.

### Bán dẫn và cổ phiếu tăng trưởng

Hệ số định giá có thể nhạy với lợi suất thực, nhưng nếu điều chỉnh dự báo lợi nhuận do AI/HBM vẫn rất mạnh, kênh lợi nhuận có thể lấn át kênh chiết khấu.

### Tiện ích và nhóm phòng thủ

Dòng tiền ổn định nhưng thường có tính duration cao. Lợi suất dài hạn tăng có thể làm hệ số định giá chịu áp lực.

### Doanh nghiệp hàng hóa

Nếu CPI cao do nhu cầu mạnh, doanh nghiệp hàng hóa có thể hưởng lợi. Nếu do cú sốc nguồn cung, các ngành sử dụng đầu vào lại chịu thiệt nhiều hơn.

## 10. Chuyển cú sốc vĩ mô vào mô hình doanh nghiệp

Một cú sốc vĩ mô chỉ có ý nghĩa đầu tư khi có thể chuyển thành biến trong mô hình doanh nghiệp.

Ví dụ với doanh nghiệp xuất khẩu Hàn Quốc:

```text
KRW yếu
→ Hỗ trợ quy đổi doanh thu USD
NHƯNG
→ Chi phí đầu vào nhập khẩu tăng
+ Chi phí vốn tăng
+ Nhu cầu toàn cầu có thể giảm
```

Cần lập bản đồ tiền tệ của doanh thu, chi phí, nợ và chính sách phòng vệ thay vì dùng khẩu quyết `KRW yếu = doanh nghiệp xuất khẩu tốt`.

## 11. Phân rã biến động định giá

Nếu cổ phiếu giảm 8% sau CPI, hãy hỏi:

```text
Bao nhiêu do dự báo EPS giảm?
Bao nhiêu do P/E co lại?
Bao nhiêu do tỷ giá, dòng vốn và thanh khoản?
```

Nếu EPS gần như không đổi nhưng P/E giảm từ 30x xuống 27x, biến động chủ yếu đến từ tỷ lệ chiết khấu. Nếu dự báo EPS cũng giảm, cú sốc đã bắt đầu đi vào kênh lợi nhuận.

Đọc thêm: [Định giá doanh nghiệp](../03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md).

## 12. Mức phơi nhiễm ở cấp danh mục

Một danh mục có thể gồm ETF tăng trưởng Mỹ, ETF trái phiếu dài hạn, ETF bán dẫn Hàn Quốc, REIT và vàng. Nhìn theo mã thì có vẻ đa dạng, nhưng bốn vị thế đầu có thể cùng chịu áp lực khi lợi suất thực tăng.

Hãy lập bản đồ các nhân tố:

```text
Duration
USD
Tăng trưởng
Tín dụng
Lạm phát
Hàng hóa
Thanh khoản
```

Đọc thêm: [Phân bổ đa tài sản](../02_asset_classes/05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md).

## 13. Thiết kế phòng vệ

Công cụ phòng vệ phải khớp đúng loại rủi ro cần giảm:

```text
Rủi ro lãi suất → DV01 / Futures lãi suất / Swap
Beta cổ phiếu → Futures chỉ số
Rủi ro đuôi → Quyền chọn
Rủi ro FX → Forward FX / Tỷ lệ phòng vệ
```

Dùng sai công cụ sẽ tạo rủi ro cơ sở (basis risk).

## 14. Quy mô vị thế theo kịch bản

Không nên quyết định quy mô chỉ vì “CPI sẽ xấu”. Hãy định nghĩa mức lỗ theo kịch bản.

Ví dụ:

```text
Cơ sở: 2Y +15bp, 10Y +10bp, USD +1%, cổ phiếu -2%
Tiêu cực: 2Y +40bp, 10Y +35bp, USD +3%, credit spread +30bp
Đuôi: kỳ vọng lạm phát mất neo, đầu dài +70bp, cổ phiếu -8%, thanh khoản xấu đi
```

Kiểm thử toàn danh mục theo các trạng thái này rồi mới quyết định quy mô.

## 15. Thực thi quanh sự kiện

Sự kiện vĩ mô thường làm chênh lệch mua bán và trượt giá tăng. Nếu giao dịch quanh CPI, lệnh thị trường có thể khớp xa giá mong muốn, stop có thể bị trượt, limit có thể không khớp hoặc bị lựa chọn bất lợi. Biến động ngụ ý của quyền chọn cũng thường cao trước sự kiện.

Kế hoạch thực thi phải được xác định **trước** thời điểm công bố.

Đọc thêm: [Thực thi và vi cấu trúc](../05_trading_derivatives/03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md).

## 16. Mua quyền chọn không chỉ cần đoán đúng hướng

Nếu mua put trước CPI, lãi/lỗ phụ thuộc đồng thời vào:

```text
Biến động giá cơ sở
Thay đổi biến động ngụ ý (IV)
Theta
Skew
Chi phí thực thi
```

Thị trường có thể giảm đúng hướng nhưng ít hơn mức biến động đã được định giá, khiến lợi nhuận quyền chọn thấp hơn kỳ vọng. Sau sự kiện, IV thường giảm nhanh.

## 17. Truyền dẫn riêng tới Hàn Quốc

Một chuỗi có thể là:

```text
CPI Mỹ cao hơn dự kiến
→ Lợi suất Mỹ tăng
→ USD mạnh
→ USD/KRW tăng
→ Dòng vốn nước ngoài chịu áp lực
→ Cổ phiếu KOSDAQ duration dài chịu áp lực
```

Nhưng nhóm bán dẫn vẫn có thể chống chịu nếu điều chỉnh dự báo lợi nhuận toàn cầu tiếp tục tăng.

## 18. Truyền dẫn riêng tới Việt Nam

Một chuỗi có thể là:

```text
Lợi suất Mỹ / USD tăng
→ VND chịu áp lực
→ Dư địa nới lỏng của SBV giảm
→ Kỳ vọng thanh khoản nội địa yếu đi
→ Bất động sản / môi giới / nhóm dùng đòn bẩy nhạy hơn
```

Tuy nhiên chính sách tín dụng, lãi suất huy động, đầu tư công và lợi nhuận nội địa có thể chi phối về trung hạn.

## 19. Thị trường đã phản ánh điều gì vào giá?

Một CPI cao hơn dự kiến chỉ tạo lợi thế nếu phản ứng thực tế khác kỳ vọng đã nằm trong giá trước sự kiện.

Trước sự kiện nên kiểm tra:

```text
Đồng thuận
Ước tính không chính thức (whisper estimate)
Định giá đường đi của Fed
Lợi suất 2 năm
Định giá cổ phiếu
Vị thế thị trường
Mức biến động hàm ý của quyền chọn
Vị thế USD
```

## 20. Xác nhận liên thị trường

Sau khi công bố, kiểm tra đồng thời lợi suất 2Y/10Y, lợi suất thực, kỳ vọng lạm phát hòa vốn, USD, chênh lệch tín dụng, vàng, dầu, độ rộng cổ phiếu và tương quan tăng trưởng–giá trị.

Nếu các tín hiệu không khớp với câu chuyện ban đầu, cần hạ mức tin cậy thay vì ép dữ liệu vào một câu chuyện duy nhất.

## 21. Phân rã sau sự kiện

Đánh giá tốt không phải chỉ ghi “tôi đoán đúng CPI”. Hãy tách:

```text
Luận điểm vĩ mô có đúng không?
Phản ứng lãi suất có đúng không?
Phản ứng FX có đúng không?
Lập bản đồ ngành có đúng không?
Quy mô vị thế có phù hợp không?
Chi phí thực thi có chấp nhận được không?
Phòng vệ có hoạt động đúng mục tiêu không?
```

## 22. Điều kiện vô hiệu hóa luận điểm

Ví dụ luận điểm ban đầu: lạm phát dai dẳng sẽ trì hoãn nới lỏng và gây áp lực lên tài sản duration dài.

Luận điểm có thể bị vô hiệu nếu thị trường lao động suy yếu nhanh, cấu phần lạm phát lõi giảm rõ, ngân hàng trung ương chấp nhận lạm phát tạm thời hoặc căng thẳng tài chính buộc chính sách phải đảo chiều.

Giá đi ngược vài phiên không tự động làm luận điểm sai; cơ chế cốt lõi thay đổi mới là điều quan trọng.

## 23. Mẫu dùng lại

```text
1. Số thực tế so với đồng thuận
2. Cấu phần
3. Độ dai dẳng
4. Hàm phản ứng
5. Lợi suất đầu ngắn
6. Lợi suất đầu dài / Phần bù kỳ hạn
7. Lợi suất thực / Kỳ vọng lạm phát
8. USD / Tỷ giá địa phương
9. Tín dụng
10. Lợi nhuận ngành
11. Định giá
12. Vị thế thị trường
13. Mức phơi nhiễm danh mục
14. Phòng vệ
15. Thực thi
16. Phân rã kết quả
```

## Kết luận

Một con số CPI không phải tín hiệu giao dịch tự động. Nó là một **cú sốc thông tin** làm thị trường cập nhật phân phối xác suất của tăng trưởng, lạm phát và chính sách. Nhà đầu tư cần theo dõi từng kênh truyền dẫn, kiểm tra điều gì đã nằm trong giá, nối nó tới dòng tiền doanh nghiệp và chỉ sau đó mới quyết định mức phơi nhiễm, công cụ phòng vệ và quy mô vị thế.