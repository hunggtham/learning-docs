# LG Energy Solution — kinh tế pin, tỷ lệ sử dụng công suất, hợp đồng và chu kỳ CAPEX

Case này dùng LG Energy Solution như một bài thực hành để hiểu một trong những ngành sản xuất chiến lược quan trọng của Hàn Quốc: **pin thứ cấp (secondary battery / 이차전지)**. Nhìn bề ngoài, ngành pin có vẻ đơn giản: xe điện tăng thì nhu cầu pin tăng. Nhưng thực tế phức tạp hơn nhiều vì tăng trưởng nhu cầu, hóa học pin, hợp đồng khách hàng, giá nguyên liệu, tỷ lệ sử dụng nhà máy, trợ cấp, nội địa hóa sản xuất và CAPEX tương tác với nhau.

Mục tiêu là chuyển câu chuyện “xe điện tăng trưởng” thành một mô hình nhân quả có thể nối tới doanh thu, biên lợi nhuận, dòng tiền và tỷ suất sinh lời trên vốn đầu tư (ROIC).

Xem nền tảng tại [15_automotive_battery_mobility](../15_automotive_battery_mobility.md), [02_trade_export_and_global_value_chains](../02_trade_export_and_global_value_chains.md) và [21_economy_to_company_transmission](../21_economy_to_company_transmission.md).

## 1. Công ty pin thực sự bán gì?

Nhà sản xuất pin không chỉ bán một sản phẩm chung tên là “pin”. Đơn vị kinh tế có thể là cell, module, pack hoặc hệ thống lưu trữ năng lượng tùy khách hàng và ứng dụng.

Có thể mô hình hóa gần đúng:

\[
Doanh\ thu \approx Sản\ lượng\ giao\ hàng\ (GWh) \times Doanh\ thu\ trên\ Wh
\]

Nhưng doanh thu trên Wh không chỉ là giá bán thuần. Nó còn chịu ảnh hưởng của hóa học pin, định dạng sản phẩm, cơ chế chuyển giá nguyên liệu (raw-material pass-through), hợp đồng khách hàng, khu vực và cơ cấu sản phẩm.

Khi doanh thu giảm, cần tách:

```text
Sản lượng giao hàng?
Giá / cơ chế chuyển giá nguyên liệu?
Cơ cấu sản phẩm?
Tỷ giá?
Lịch sản xuất của khách hàng?
```

## 2. Nhu cầu xe điện không truyền thẳng 1:1 vào lượng pin giao hàng

Chuỗi nhân quả thực tế dài hơn:

```text
Nhu cầu ô tô của người tiêu dùng
→ sản lượng của OEM
→ tỷ trọng EV / hybrid
→ dung lượng pin trên mỗi xe
→ tồn kho của OEM
→ đơn hàng / giao hàng pin
→ tỷ lệ sử dụng nhà máy cell
```

Nếu nhu cầu bán lẻ EV tăng 10% nhưng OEM đang giảm tồn kho, lượng pin giao trong một quý vẫn có thể yếu.

Ngược lại, lượng pin giao có thể tăng trước doanh số xe nếu OEM tích trữ hàng hoặc tăng sản lượng cho mẫu xe mới.

> **Mô hình tư duy:** nhu cầu pin là nhu cầu phái sinh (derived demand). Muốn hiểu nhà sản xuất cell, phải đi ngược tới nền tảng xe và lịch sản xuất của khách hàng.

## 3. Công suất GWh không đồng nghĩa sản lượng kinh tế GWh

Một nhà máy được công bố có `X GWh công suất` không có nghĩa ngay lập tức tạo ra X GWh cell đủ chuẩn để bán.

Giữa công suất danh nghĩa và sản lượng kinh tế có nhiều bước:

```text
Lắp thiết bị
→ chứng nhận
→ tăng công suất ban đầu (ramp)
→ ổn định tỷ lệ đạt chuẩn
→ khách hàng phê duyệt
→ tăng tỷ lệ sử dụng công suất
→ tạo sản lượng bán được
```

Cần tách rõ hai biến:

**Tỷ lệ sử dụng công suất (utilization / 가동률)** cho biết nhà máy đang dùng bao nhiêu phần công suất.

**Tỷ lệ đạt chuẩn (yield / 수율)** cho biết bao nhiêu phần sản lượng đầu ra đáp ứng tiêu chuẩn chất lượng.

Nhà máy chạy nhiều nhưng yield thấp vẫn có thể tiêu tốn nguyên liệu và lao động mà không tạo đủ sản lượng bán được.

## 4. Chi phí cố định lớn và đòn bẩy hoạt động

Sản xuất pin cần nhà máy, thiết bị phủ điện cực, thiết bị formation, phòng khô, hệ thống chất lượng và khấu hao lớn. Khi tỷ lệ sử dụng công suất thấp, chi phí cố định được phân bổ trên ít sản lượng hơn.

\[
Chi\ phí\ đơn\ vị = Chi\ phí\ biến\ đổi + \frac{Chi\ phí\ sản\ xuất\ cố\ định}{Sản\ lượng\ bán\ được}
\]

Nếu chi phí cố định là 1.000 và sản lượng là 100 đơn vị, chi phí cố định mỗi đơn vị là 10. Nếu sản lượng giảm còn 60, con số tăng lên khoảng 16,7 dù tổng chi phí cố định không đổi.

Đây là lý do tỷ lệ sử dụng công suất có thể khiến biên lợi nhuận biến động mạnh hơn cả sản lượng giao hàng.

## 5. Chuyển giá nguyên liệu: doanh thu giảm chưa chắc kinh tế xấu tương ứng

Lithium, nickel, cobalt và các nguyên liệu khác có thể ảnh hưởng trực tiếp giá cell. Nhiều hợp đồng có cơ chế điều chỉnh giá hoặc **chuyển giá nguyên liệu (pass-through)** ở các mức độ khác nhau.

Nếu giá nguyên liệu giảm và giá bán được điều chỉnh xuống theo công thức hợp đồng, doanh thu báo cáo có thể giảm dù sản lượng vật lý không giảm tương ứng.

Không nên suy luận máy móc:

> Doanh thu giảm = nhu cầu giảm.

Cần tách:

\[
Tăng\ trưởng\ doanh\ thu \approx Ảnh\ hưởng\ sản\ lượng + Ảnh\ hưởng\ giá/cơ\ cấu + Ảnh\ hưởng\ tỷ\ giá
\]

và phần giá phải tách tiếp giữa cơ chế chuyển giá hàng hóa với quyền định giá thực sự.

## 6. Hóa học pin là bài toán kinh tế, không chỉ là khoa học

Hóa học pin ảnh hưởng mật độ năng lượng, an toàn, mức phụ thuộc nguyên liệu, chi phí, hiệu suất và phân khúc xe mục tiêu.

Pin NCM/NCA hàm lượng nickel cao có đánh đổi chi phí–hiệu suất khác LFP. Không nên biến vấn đề thành khẩu hiệu “công nghệ A tốt hơn B”. Một loại có thể phù hợp xe cao cấp cần quãng đường dài, loại khác lại phù hợp xe phổ thông hoặc lưu trữ năng lượng.

Câu hỏi kinh tế nên là:

```text
Yêu cầu của khách hàng
→ lựa chọn hóa học pin
→ cơ cấu nguyên liệu
→ quy trình sản xuất
→ yield / chi phí
→ giá bán / biên lợi nhuận
```

Lợi thế công nghệ chỉ tạo giá trị khi chuyển được thành chứng nhận, sản lượng và mức sinh lời trên vốn đủ cao.

## 7. Mức tập trung khách hàng và rủi ro nền tảng xe

Nhà cung cấp pin thường phụ thuộc một số OEM và nền tảng xe lớn. Hợp đồng dài hạn có thể tăng khả năng dự báo nhưng không loại bỏ rủi ro.

Cần hỏi:

- hợp đồng có cam kết mua bắt buộc hay chỉ là khung hợp tác?
- khối lượng có linh hoạt không?
- công thức giá thế nào?
- khách hàng có thể trì hoãn nền tảng xe không?
- nhà máy có dành riêng cho một khách hàng không?
- nếu nhu cầu của khách hàng yếu, công suất có chuyển sang khách hàng khác được không?

Nhà máy chuyên biệt có giá trị chiến lược khi khách hàng mạnh, nhưng tạo **rủi ro công suất mắc kẹt (stranded-capacity risk)** nếu nền tảng xe thất bại.

## 8. Liên doanh: chia sẻ CAPEX nhưng tăng độ phức tạp quản trị

Mở rộng nhà máy ở nước ngoài thường sử dụng **liên doanh (joint venture / JV / 합작법인)** với hãng xe hoặc đối tác.

JV có thể giúp:

```text
Chia sẻ gánh nặng vốn
+ bảo đảm khách hàng đầu mối
+ đồng bộ địa điểm sản xuất
+ chia sẻ năng lực thực thi
```

Nhưng phạm vi kế toán rất quan trọng. JV có thể được hợp nhất, ghi nhận theo phương pháp vốn chủ sở hữu hoặc đi kèm các bảo lãnh/cam kết khác nhau tùy cấu trúc.

Không nên thấy thông báo “đầu tư nhà máy X nghìn tỷ won” rồi mặc định toàn bộ CAPEX và nợ nằm trên công ty mẹ niêm yết.

Hãy quay lại [09_disclosure_accounting_dart_kind](../09_disclosure_accounting_dart_kind.md) để xác định phạm vi báo cáo.

## 9. Nội địa hóa: địa chính trị trở thành kinh tế nhà máy

Ngành pin chịu tác động mạnh của chính sách công nghiệp, quy tắc hàm lượng nội địa, thuế quan, trợ cấp và yêu cầu an ninh chuỗi cung ứng.

Nhà máy ở Bắc Mỹ có thể được xây không chỉ vì chi phí vận chuyển mà còn vì yêu cầu nội địa hóa của khách hàng và kinh tế của ưu đãi chính sách.

```text
Ưu đãi chính sách / quy định nội địa
→ địa điểm nhà máy
→ CAPEX
→ chuỗi cung ứng địa phương
→ chi phí lao động / năng lượng
→ trợ cấp / lợi ích thuế
→ chứng nhận khách hàng
→ ROIC dự án
```

Trợ cấp không nên được coi là “lợi nhuận miễn phí”. Nếu trợ cấp chỉ bù cho chi phí sản xuất địa phương cao hơn về cơ cấu, năng lực cạnh tranh nền tảng vẫn phải đánh giá riêng.

## 10. Chu kỳ CAPEX: tăng trưởng có thể làm dòng tiền xấu trước khi tốt

Nhà sản xuất pin có thể báo cáo doanh thu và lợi nhuận kế toán tăng nhưng FCF âm vì mở rộng công suất mạnh.

\[
FCF \approx CFO - CAPEX
\]

Nhưng với doanh nghiệp sản xuất tăng trưởng, câu hỏi quan trọng hơn là:

\[
ROIC\ tăng\ thêm = \frac{Lợi\ nhuận\ hoạt\ động\ sau\ thuế\ tăng\ thêm}{Vốn\ đầu\ tư\ tăng\ thêm}
\]

Nếu toàn ngành xây quá nhiều công suất, tỷ lệ sử dụng tương lai thấp và ROIC tăng thêm có thể thấp dù tổng thị trường vẫn tăng.

> Ngành tăng trưởng không bảo đảm mọi khoản đầu tư tăng trưởng đều tạo giá trị.

## 11. Độ trễ khấu hao và ảo giác biên lợi nhuận

CAPEX hôm nay không đi hết vào báo cáo kết quả kinh doanh ngay hôm nay. Nó được vốn hóa rồi khấu hao theo thời gian.

Khi nhà máy mới bắt đầu vận hành:

```text
CAPEX đã chi
→ tài sản đưa vào sử dụng
→ khấu hao tăng
→ tỷ lệ sử dụng có thể vẫn thấp
→ áp lực biên lợi nhuận xuất hiện
```

Vì vậy đỉnh CAPEX có thể xuất hiện trước đỉnh khấu hao. Phải theo dõi cả thời điểm dòng tiền và thời điểm kế toán.

## 12. Vốn lưu động

Sản xuất pin cần nguyên liệu, sản phẩm dở dang, thành phẩm và khoản phải thu. Tăng trưởng có thể hút tiền qua tồn kho và phải thu.

Ví dụ:

```text
Doanh thu +25%
Lợi nhuận hoạt động +15%
Phải thu +35%
Tồn kho +40%
```

Nếu CFO không tăng theo lợi nhuận, cần hỏi đây là quá trình tăng công suất bình thường hay dấu hiệu bán hàng/thu tiền yếu.

## 13. Bảo hành, chất lượng và rủi ro đuôi dài từ thu hồi sản phẩm

Lỗi pin có thể tạo chi phí rất lớn vì cell là linh kiện liên quan trực tiếp đến an toàn. Dự phòng kế toán chỉ là ước tính của ban quản lý tại một thời điểm.

Cần phân biệt:

```text
Sự cố đã biết
→ quy mô sản phẩm bị ảnh hưởng ước tính
→ cách chia trách nhiệm với OEM
→ khoản dự phòng
→ khoản tiền thực trả
```

Nếu nguyên nhân kỹ thuật chưa chắc chắn, mức độ bất định của dự phòng cao.

Rủi ro chất lượng còn ảnh hưởng danh tiếng, chứng nhận khách hàng tương lai và chi phí bảo hiểm/pháp lý, chứ không chỉ một khoản phí kế toán một lần.

## 14. Mô hình kịch bản

### Kịch bản cơ sở

```text
Nhu cầu EV tăng vừa phải
→ sản lượng giao +15%
→ tỷ lệ sử dụng công suất tăng
→ giá nguyên liệu ổn định
→ yield dần ổn định
→ biên lợi nhuận tăng nhẹ
→ CAPEX vẫn cao
```

### Kịch bản bất lợi

```text
OEM trì hoãn nền tảng EV
→ sản lượng giao chỉ +0~5%
→ tỷ lệ sử dụng công suất giảm
→ cạnh tranh giá tăng
→ chi phí cố định trên mỗi Wh tăng
→ CAPEX đã cam kết vẫn phải chi
→ FCF xấu đi
```

### Kịch bản thuận lợi

```text
Mẫu xe mới của khách hàng thành công
→ tỷ lệ sử dụng tăng nhanh
→ cơ cấu sản phẩm giá trị cao tốt hơn
→ yield cải thiện
→ hấp thụ chi phí cố định tốt hơn
→ đòn bẩy hoạt động nâng biên lợi nhuận
```

Mục tiêu không phải dự đoán chính xác mà là biết **biến nào chi phối kinh tế doanh nghiệp**.

## 15. Định giá: tránh dùng một bội số mà không có bối cảnh

Doanh nghiệp pin tăng trưởng cao có thể được định giá bằng EV/EBITDA, P/E hoặc DCF tùy giai đoạn, nhưng mẫu số cần được chuẩn hóa.

Nếu EBITDA cao trước khi khấu hao phản ánh đầy đủ các nhà máy mới, EV/EBITDA có thể trông rẻ giả tạo. Nếu lợi nhuận hiện tại thấp vì chi phí tăng công suất nhưng có đường đi rõ tới tỷ lệ sử dụng tốt hơn, P/E hiện tại lại có thể kém ý nghĩa.

**Định giá ngược (reverse valuation)** hữu ích hơn:

> Giá trị doanh nghiệp hiện tại đang ngầm giả định tỷ lệ sử dụng công suất, biên lợi nhuận và ROIC dài hạn ở mức nào?

Sau đó kiểm tra các giả định đó có phù hợp với công suất toàn ngành và nhu cầu khách hàng hay không.

## 16. Những nhầm lẫn thường gặp

### “Doanh số EV tăng thì công ty pin chắc chắn tăng lợi nhuận”

Sai vì giá, cơ cấu sản phẩm, tỷ lệ sử dụng, yield và điều khoản hợp đồng có thể bù trừ tác động sản lượng.

### “Công suất càng lớn càng có lợi thế”

Sai nếu công suất không được sử dụng hoặc ROIC dự án thấp.

### “Hợp đồng dài hạn loại bỏ chu kỳ”

Sai vì thời điểm khối lượng, công thức giá và thành công của nền tảng xe vẫn thay đổi.

### “Trợ cấp là lợi ích thuần”

Sai nếu trợ cấp chỉ bù cho chi phí nội địa cao hơn hoặc đòi hỏi CAPEX lớn để đủ điều kiện.

## 17. Bài tập nghiên cứu

Khi cập nhật báo cáo mới, dựng bảng:

| Chỉ tiêu | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Sản lượng / chỉ báo công suất | | | | | |
| Doanh thu | | | | | |
| Biên lợi nhuận hoạt động | | | | | |
| CAPEX | | | | | |
| Khấu hao | | | | | |
| CFO | | | | | |
| FCF | | | | | |
| Tồn kho | | | | | |
| Phải thu | | | | | |
| Nợ ròng / tiền mặt | | | | | |

Sau đó ghi chú các nhà máy mới, JV, nền tảng xe lớn, sự cố thu hồi và thay đổi chính sách.

## Mô hình tư duy cuối

> Nhà sản xuất pin là một **doanh nghiệp phân bổ công suất dưới ràng buộc công nghệ và chính sách**. Nhu cầu EV tạo cơ hội, nhưng giá trị cho cổ đông chỉ xuất hiện khi doanh nghiệp biến CAPEX thành công suất được chứng nhận, biến công suất thành sản lượng đạt chuẩn, biến sản lượng thành giao hàng cho khách hàng và cuối cùng biến giao hàng thành tiền với ROIC đủ cao.

Đọc tiếp [08_hanwha_aerospace_defense_backlog_case](./08_hanwha_aerospace_defense_backlog_case.md) để so sánh ngành pin — nơi chu kỳ nhu cầu và công suất rất quan trọng — với quốc phòng, nơi backlog, mua sắm công và lịch giao hàng đóng vai trò trung tâm.