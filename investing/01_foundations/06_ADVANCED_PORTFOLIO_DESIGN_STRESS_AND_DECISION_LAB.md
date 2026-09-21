# Phòng thí nghiệm nâng cao: thiết kế danh mục, kiểm thử căng thẳng và quy tắc quyết định

> File này không lặp lại định nghĩa về đa dạng hóa, tái cân bằng hay độ biến động. Mục tiêu là biến các khái niệm nền tảng thành một quy trình thiết kế danh mục có thể kiểm chứng. Người đọc phải đi từ **mục tiêu → nghĩa vụ → bảng cân đối → nguồn rủi ro → ngân sách rủi ro → kiểm thử → quy tắc hành động → đánh giá sau quyết định**.

## 1. Bắt đầu từ bài toán tài chính, không bắt đầu từ sản phẩm

Một danh mục chỉ có ý nghĩa khi nó phục vụ một tập nghĩa vụ cụ thể. Trước khi chọn ETF, cổ phiếu hay trái phiếu, cần mô tả bốn lớp:

```text
Nguồn thu nhập
→ tài sản hiện có
→ nghĩa vụ chắc chắn / có xác suất
→ mục tiêu theo thời gian
```

Ví dụ, hai người đều có 100 triệu KRW nhưng một người cần 70 triệu trong 18 tháng để thuê nhà, còn người kia chưa cần dùng tiền trong 10 năm. Nếu cả hai cùng giữ 80% cổ phiếu, con số tỷ trọng giống nhau nhưng chất lượng quyết định hoàn toàn khác.

Điểm cốt lõi là **rủi ro phải được đo so với mục tiêu**, không chỉ so với độ biến động thị trường.

## 2. Xây bảng cân đối kinh tế của hộ gia đình

Bảng cân đối tài chính truyền thống chỉ liệt kê tiền, cổ phiếu, nhà và nợ. Với đầu tư dài hạn, cần thêm **vốn con người (human capital)** — giá trị hiện tại của thu nhập nghề nghiệp tương lai.

Một kỹ sư công nghệ có thu nhập phụ thuộc chu kỳ công nghệ đã có mức phơi nhiễm kinh tế với ngành này ngay cả khi chưa mua cổ phiếu công nghệ. Nếu danh mục lại tập trung mạnh vào công nghệ, tổng rủi ro thực cao hơn con số trong tài khoản chứng khoán.

Khung phân tích:

```text
Tài sản tài chính
+ Tài sản thực
+ Vốn con người
- Nợ hiện tại
- Nghĩa vụ tương lai
= Bảng cân đối kinh tế
```

## 3. Tách khả năng chịu rủi ro thành ba lớp

Không nên dùng một câu hỏi kiểu “bạn có chịu được giảm 30% không?”. Hãy tách:

**Khả năng tài chính chịu rủi ro (risk capacity):** mức lỗ mà kế hoạch vẫn sống được.

**Mức chịu đựng tâm lý (risk tolerance):** mức biến động mà người đầu tư không phá vỡ quy tắc.

**Mức rủi ro cần thiết (risk requirement):** lượng rủi ro cần chấp nhận để xác suất đạt mục tiêu đủ cao.

Một kế hoạch tốt phải thỏa cả ba. Nếu mục tiêu yêu cầu lợi suất quá cao trong khi khả năng chịu rủi ro thấp, giải pháp không phải “tìm tài sản tốt hơn” mà có thể phải tăng tiết kiệm, kéo dài thời gian hoặc giảm mục tiêu.

## 4. Chuyển tỷ trọng vốn thành ngân sách rủi ro

Tỷ trọng vốn không cho biết nguồn rủi ro. Một danh mục 50% cổ phiếu và 50% trái phiếu ngắn hạn có thể nhận phần lớn biến động từ cổ phiếu.

Với danh mục nhiều tài sản, nên phân loại rủi ro thành:

```text
Rủi ro tăng trưởng
Rủi ro lãi suất / duration
Rủi ro tín dụng
Rủi ro lạm phát
Rủi ro tiền tệ
Rủi ro hàng hóa
Rủi ro thanh khoản
Rủi ro đòn bẩy
Rủi ro vận hành
```

Sau đó hỏi: nếu một biến duy nhất gây 50–60% tổn thất tiềm năng, danh mục có thực sự đa dạng không?

## 5. Đóng góp rủi ro biên và đóng góp rủi ro thành phần

Khi tăng một vị thế nhỏ, mức biến động danh mục thay đổi bao nhiêu là **đóng góp rủi ro biên (marginal contribution to risk, MCTR)**.

Đóng góp rủi ro của vị thế gần bằng:

```text
Tỷ trọng vị thế × MCTR
```

Ý nghĩa thực tế: hai vị thế cùng 10% vốn có thể đóng góp rủi ro rất khác nếu một vị thế biến động cao và tương quan mạnh với phần còn lại.

Không cần tối ưu toán học hoàn hảo; chỉ cần dùng khái niệm này để phát hiện **tập trung rủi ro ẩn**.

## 6. Tương quan phải được xem theo trạng thái

Tương quan trung bình 5 năm có thể che mất hành vi khi khủng hoảng. Nên xem ít nhất ba ma trận:

```text
Toàn bộ giai đoạn
Giai đoạn thị trường tăng
Giai đoạn thị trường giảm mạnh
```

Nếu nhiều tài sản có tương quan thấp trong bình thường nhưng tăng đồng loạt trong căng thẳng, lợi ích đa dạng hóa có thể biến mất đúng lúc cần nhất.

Đây là lý do kiểm thử căng thẳng phải bổ sung cho covariance lịch sử.

## 7. Thiết kế tầng thanh khoản

Thanh khoản nên được tổ chức theo nghĩa vụ, không theo cảm giác an toàn.

```text
Tầng 1: tiền cần ngay
Tầng 2: tiền cho nghĩa vụ 6–24 tháng
Tầng 3: tài sản phòng thủ trung hạn
Tầng 4: tài sản tăng trưởng dài hạn
Tầng 5: ý tưởng chủ động / rủi ro cao
```

Một danh mục có lợi suất kỳ vọng cao nhưng buộc phải bán cổ phiếu trong khủng hoảng để trả nghĩa vụ ngắn hạn là một thiết kế kém.

## 8. Kiểm thử cú sốc đơn biến

Bắt đầu bằng cú sốc đơn giản để hiểu độ nhạy:

```text
Lợi suất thực +150 bp
USD/KRW +12%
Cổ phiếu toàn cầu -30%
Chênh lệch tín dụng +400 bp
Vàng -15%
Thanh khoản giảm mạnh
```

Mục tiêu không phải dự báo xác suất chính xác mà là nhìn xem danh mục gãy ở đâu.

## 9. Kiểm thử cú sốc kết hợp

Khủng hoảng thật hiếm khi chỉ có một biến thay đổi. Một kịch bản hợp lý hơn:

```text
Lạm phát quay lại
→ lợi suất dài hạn tăng
→ USD mạnh
→ cổ phiếu duration dài giảm
→ tín dụng doanh nghiệp yếu đi
→ thanh khoản giảm
```

Hoặc:

```text
Suy thoái
→ lợi nhuận doanh nghiệp giảm
→ chênh lệch tín dụng mở rộng
→ cổ phiếu giảm
→ ngân hàng trung ương cắt lãi
→ trái phiếu chính phủ tăng
```

Hai kịch bản đều có cổ phiếu giảm nhưng phần phòng vệ phù hợp rất khác nhau.

## 10. Kiểm thử ngược

**Kiểm thử ngược (reverse stress test)** không hỏi “nếu X xảy ra thì lỗ bao nhiêu?”, mà hỏi:

> Điều gì phải xảy ra để kế hoạch tài chính thất bại?

Ví dụ:

```text
Danh mục giảm bao nhiêu thì tiền đặt cọc nhà không còn đủ?
USD/KRW đi bao xa thì nghĩa vụ KRW bị thiếu?
Mất việc bao lâu thì phải bán tài sản tăng trưởng?
Mức margin nào gây bán cưỡng bức?
```

Cách nhìn này giúp tìm điểm thất bại trước khi tối ưu lợi suất.

## 11. Tái cân bằng theo dải và theo rủi ro

Tái cân bằng theo tỷ trọng là đơn giản nhất, nhưng có thể bổ sung tín hiệu rủi ro.

Ví dụ:

```text
Mục tiêu cổ phiếu: 60%
Dải cho phép: 55–65%
```

Nếu cổ phiếu tăng lên 66%, có thể tái cân bằng. Tuy nhiên nếu biến động giảm mạnh và đóng góp rủi ro vẫn nằm trong giới hạn, có thể xem xét ngưỡng theo rủi ro thay vì máy móc.

Điều quan trọng là quy tắc phải được đặt **trước** khi cảm xúc xuất hiện.

## 12. Dùng dòng tiền mới để tái cân bằng

Trong giai đoạn tích lũy, dòng tiền mới là công cụ tái cân bằng ít ma sát nhất.

Nếu cổ phiếu đang cao hơn mục tiêu và trái phiếu thấp hơn mục tiêu, khoản tiết kiệm mới có thể được chuyển vào trái phiếu trước khi bán cổ phiếu. Cách này giảm phí, thuế và sai lầm thời điểm.

## 13. Quy tắc giảm rủi ro khi mục tiêu đến gần

Khi thời hạn rút tiền giảm, rủi ro thị trường của phần tiền dành cho mục tiêu đó nên giảm nếu không có khả năng bù lỗ.

Một quy tắc có thể là:

```text
> 7 năm: ưu tiên tăng trưởng
3–7 năm: cân bằng tăng trưởng và ổn định
1–3 năm: tăng tài sản khớp nghĩa vụ
< 1 năm: ưu tiên thanh khoản / bảo toàn danh nghĩa
```

Đây không phải công thức cố định, mà là cách minh họa tư duy khớp tài sản–nghĩa vụ.

## 14. Quy tắc bán phải gắn với nguyên nhân

Không nên bán chỉ vì “đã lời nhiều” hoặc “giá giảm mạnh”. Một vị thế nên được xem xét khi:

```text
Luận điểm bị vô hiệu hóa
Rủi ro vượt ngân sách
Kỳ vọng lợi suất không còn hấp dẫn
Thanh khoản xấu đi đáng kể
Nghĩa vụ tới hạn
Danh mục bị tập trung quá mức
Có lựa chọn thay thế tốt hơn sau chi phí
```

Việc ghi lý do bán trước khi hành động giúp tránh hợp lý hóa sau sự kiện.

## 15. Nhật ký quyết định

Mỗi quyết định lớn nên ghi:

```text
Thông tin có tại thời điểm quyết định
Giả định chính
Kịch bản cơ sở / xấu / tốt
Lợi suất kỳ vọng
Rủi ro lớn nhất
Điều kiện vô hiệu hóa
Quy mô vị thế
Thời điểm đánh giá lại
```

Sau đó đánh giá **chất lượng quyết định** riêng với **kết quả**. Một quyết định tốt vẫn có thể lỗ do bất định; một quyết định xấu vẫn có thể lời do may mắn.

## 16. Hiệu chỉnh dự báo

Nếu thường xuyên viết xác suất cho kịch bản, có thể kiểm tra độ hiệu chỉnh (calibration).

Ví dụ, các sự kiện được gán xác suất 70% có xảy ra gần 70% không? Nếu chỉ xảy ra 40%, hệ thống dự báo đang quá tự tin.

Đây là bước quan trọng để cải thiện tư duy thay vì chỉ nhìn lợi nhuận.

## 17. Phân rã sai lầm danh mục

Khi kết quả xấu, tách nguyên nhân:

```text
Sai giả định vĩ mô
Sai chọn tài sản
Sai định giá
Sai quy mô vị thế
Sai phòng vệ
Sai thời điểm thực thi
Chi phí cao hơn dự kiến
Phá kỷ luật
```

Không sửa mô hình vĩ mô nếu vấn đề thực sự là quy mô vị thế; không sửa chiến lược nếu vấn đề là phá quy tắc.

## 18. Bài tập tổng hợp

Hãy xây một danh mục giả định với ba mục tiêu:

```text
Quỹ khẩn cấp 6 tháng
Tiền nhà trong 3 năm
Tài sản hưu trí trong 20 năm
```

Sau đó:

1. gán đồng tiền nghĩa vụ;
2. xác định khả năng chịu rủi ro;
3. chia tầng thanh khoản;
4. đặt phân bổ chiến lược;
5. xác định ngân sách rủi ro;
6. chạy ba kịch bản căng thẳng;
7. viết quy tắc tái cân bằng;
8. viết quy tắc bán;
9. viết điều kiện thay đổi phân bổ khi hoàn cảnh sống đổi.

Nếu hoàn thành được bài tập này, người đọc đã chuyển từ “biết sản phẩm” sang **thiết kế một hệ thống đầu tư có mục tiêu**.

## 19. Liên kết đọc tiếp

- [Đo lường rủi ro và phân tích danh mục](./04_RISK_MEASUREMENT_PORTFOLIO_ANALYTICS_AND_DECISION_RULES.md)
- [Phân rã kết quả, phí, thuế và hành vi](./05_PERFORMANCE_ATTRIBUTION_FEES_TAX_AND_BEHAVIORAL_REVIEW.md)
- [Danh mục đa tài sản và phòng vệ](../02_asset_classes/05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md)
- [Tình huống cú sốc lạm phát](../07_integrated_case_studies/01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md)

## Kết luận

Thiết kế danh mục chuyên nghiệp không bắt đầu bằng câu hỏi “mua gì?”, mà bằng:

```text
Tôi cần tiền cho việc gì?
→ nghĩa vụ nằm ở đâu và bằng đồng tiền nào?
→ nguồn rủi ro nào đang chi phối?
→ nếu sai, kế hoạch có sống được không?
→ quy tắc nào buộc tôi hành động nhất quán?
```

Một danh mục tốt không cần tối ưu hoàn hảo. Nó cần **đủ bền để người sở hữu có thể duy trì qua nhiều chế độ thị trường và nhiều giai đoạn cuộc sống**.