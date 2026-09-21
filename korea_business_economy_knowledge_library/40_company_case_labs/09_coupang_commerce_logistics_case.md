# Coupang — thương mại điện tử, mật độ hoàn tất đơn hàng, hội viên và kinh tế logistics

Case này dùng Coupang như một bài thực hành để hiểu một loại doanh nghiệp Hàn Quốc rất khác chaebol truyền thống. Công ty hình thành trong thời kỳ số và vốn mạo hiểm, nhưng mô hình kinh doanh cuối cùng lại **thâm dụng hạ tầng vật lý (physical-infrastructure intensive)**: trung tâm hoàn tất đơn hàng, tồn kho, mạng lưới giao hàng, công nghệ, chăm sóc khách hàng và vận hành chặng cuối cùng cùng hoạt động như một hệ thống.

Điểm quan trọng là: gọi một doanh nghiệp là “công nghệ” không cho biết kinh tế thực sự của nó. Cần tìm đúng **hàm sản xuất (production function)**.

Xem [17_platform_telecom_content_retail_services](../17_platform_telecom_content_retail_services.md), [33_logistics_ports_and_distribution_networks](../33_logistics_ports_and_distribution_networks.md) và [07_startups_venture_and_scaleups](../07_startups_venture_and_scaleups.md).

## 1. Doanh thu thương mại điện tử không đến từ một động cơ duy nhất

Một hệ sinh thái thương mại có thể gồm bán lẻ trực tiếp, sàn cho người bán bên thứ ba, dịch vụ logistics/hoàn tất đơn hàng, hội viên, quảng cáo và các dịch vụ liền kề.

Mỗi mảng có cách ghi nhận kế toán khác nhau.

Trong **bán lẻ trực tiếp (first-party / 1P)**, công ty mua tồn kho rồi bán lại. Tổng giá trị hàng hóa giao dịch và doanh thu báo cáo có thể gần nhau hơn vì công ty là bên bán chính.

Trong **sàn bên thứ ba (third-party marketplace / 3P)**, người bán bán trực tiếp cho khách hàng và nền tảng thu hoa hồng hoặc phí dịch vụ. Tổng giá trị giao dịch có thể rất lớn nhưng doanh thu báo cáo chỉ phản ánh phần hoa hồng/phí mà nền tảng được hưởng.

Vì vậy:

\[
GMV \neq Doanh\ thu \neq Lợi\ nhuận\ gộp \neq Dòng\ tiền
\]

Đây là phân biệt đầu tiên phải giữ.

## 2. Giá trị cho khách hàng và vòng quay tăng trưởng

Nền tảng thương mại có thể tạo một vòng quay tích cực:

```text
Nhiều lựa chọn hơn + giao nhanh hơn
→ trải nghiệm khách hàng tốt hơn
→ số đơn hàng tăng
→ mật độ tuyến giao / kho tăng
→ chi phí trên mỗi đơn giảm
→ giá và dịch vụ tốt hơn
→ nhiều khách hàng hơn
```

Nhưng vòng quay này chỉ thực sự tồn tại nếu chi phí trên mỗi đơn giảm khi mật độ tăng. Nếu tăng trưởng chủ yếu đến từ trợ giá và khuyến mãi, mạng lưới có thể lớn nhưng lợi thế kinh tế yếu.

> **Mô hình tư duy:** mật độ logistics là một dạng hiệu ứng mạng vật lý. Nhiều đơn hàng trong cùng một khu vực giúp chi phí hạ tầng và tuyến giao được phân bổ hiệu quả hơn.

## 3. Kinh tế mật độ

Giả sử một tuyến giao hàng có chi phí cố định mỗi ngày là 300.000 won.

Nếu giao 100 kiện:

\[
Chi\ phí\ cố\ định/kiện = 3.000\ won
\]

Nếu mật độ tăng lên 200 kiện trong khi chi phí tuyến chỉ tăng nhẹ lên 360.000 won:

\[
Chi\ phí/kiện = 1.800\ won
\]

Đây chỉ là ví dụ minh họa, không phải số liệu của công ty. Nó cho thấy vì sao mật độ đơn hàng có thể tạo **đòn bẩy hoạt động (operating leverage)**.

Khi mở rộng vào khu vực mật độ thấp, kinh tế có thể đảo chiều.

## 4. Trung tâm hoàn tất đơn hàng là cỗ máy tồn kho, không chỉ là nhà kho

Kinh tế của trung tâm hoàn tất đơn hàng phụ thuộc:

```text
Lưu lượng xử lý
× năng suất lấy/đóng gói
× tự động hóa
× tỷ lệ sử dụng công suất
× độ chính xác bố trí tồn kho
```

Nếu tồn kho được đặt gần nhu cầu, giao hàng nhanh hơn và chi phí vận chuyển giảm. Nhưng nếu dự báo sai, hàng có thể nằm sai địa điểm và phải chuyển kho hoặc giảm giá.

Lợi thế logistics vì vậy cần kết hợp dữ liệu/dự báo với tài sản vật lý.

## 5. Vòng quay tồn kho và vốn lưu động âm

Bán lẻ có thể có vốn lưu động thuận lợi nếu thu tiền khách hàng nhanh nhưng trả tiền nhà cung cấp chậm hơn.

\[
CCC = DIO + DSO - DPO
\]

Thương mại điện tử B2C thường có số ngày phải thu thấp; nếu thời hạn thanh toán cho nhà cung cấp dài, doanh nghiệp có thể được tài trợ một phần bởi khoản phải trả.

Tuy nhiên tồn kho tăng quá nhanh sẽ hút tiền và làm tăng rủi ro giảm giá hàng hóa. Vì vậy phải đọc tăng trưởng doanh thu cùng với tăng trưởng tồn kho.

## 6. Biên lợi nhuận gộp chưa đủ — cần biết chi phí hoàn tất đơn hàng nằm ở đâu

Hai nhà bán lẻ có cùng biên lợi nhuận gộp nhưng kinh tế hoàn tất đơn hàng có thể rất khác.

Cần hiểu cách phân loại:

```text
Giá vốn hàng hóa
Chi phí lao động hoàn tất đơn hàng
Chi phí giao hàng
Chi phí thanh toán
Chăm sóc khách hàng
Marketing
Công nghệ
```

Nếu một công ty ghi nhiều chi phí logistics bên dưới lợi nhuận gộp còn công ty khác ghi chúng trong giá vốn, biên gộp không thể so trực tiếp.

Nên đi xuống mức **lợi nhuận đóng góp (contribution margin)**:

\[
Lợi\ nhuận\ đóng\ góp/đơn = Doanh\ thu/đơn - Chi\ phí\ biến\ đổi\ sản\ phẩm/logistics/giao\ hàng
\]

sau đó mới xét chi phí cố định ở cấp công ty và công nghệ.

## 7. Hội viên: doanh thu phí có thể nhỏ nhưng ảnh hưởng kinh tế lớn

Phí hội viên có thể không phải dòng doanh thu lớn nhất nhưng làm thay đổi hành vi:

```text
Hội viên
→ khách hàng cảm nhận chi phí giao thêm gần bằng 0
→ tần suất đặt hàng tăng
→ tỷ lệ giữ chân tăng
→ mật độ đơn hàng tăng
→ hiệu quả logistics tăng
```

Tuy nhiên giao nhanh/miễn phí làm công ty gánh chi phí dịch vụ. Hội viên chỉ tạo giá trị nếu tần suất, mức giữ chân và kiếm tiền trong hệ sinh thái bù được chi phí phục vụ.

Không nên định giá hội viên chỉ bằng `số thành viên × phí hàng năm`.

## 8. Giữ chân khách hàng và kinh tế theo nhóm người dùng

Tăng trưởng khách hàng hoạt động tổng thể có thể che việc khách hàng cũ rời đi.

**Phân tích cohort** nên hỏi:

```text
Khách hàng có được ở kỳ T
→ còn bao nhiêu sau 3/6/12/24 tháng?
→ chi tiêu trên mỗi khách giữ lại thay đổi ra sao?
→ lợi nhuận đóng góp sau logistics thế nào?
```

Nếu cohort cũ chi tiêu nhiều hơn theo thời gian trong khi chi phí thu hút khách hàng không tăng quá nhanh, kinh tế đơn vị mạnh hơn con số người dùng đơn thuần.

Nếu tăng trưởng phụ thuộc liên tục vào chi phí thu hút đắt đỏ, quy mô có thể không tự củng cố.

## 9. Kinh tế sàn và động lực của người bán

Sàn 3P có tính ít thâm dụng tài sản hơn bán lẻ 1P, nhưng chất lượng người bán, tỷ lệ thu phí (take rate), quảng cáo, dịch vụ logistics và cạnh tranh quyết định giá trị.

Tăng take rate giúp doanh thu trên GMV tăng nhưng có thể khiến người bán đa nền tảng hoặc tăng giá bán.

Có thể hình dung thặng dư của người bán:

```text
Giá trị nền tảng mang lại cho người bán
- phí nền tảng
- chi phí logistics
- hiệu quả của kênh thay thế
= phần lợi ích còn lại của người bán
```

Nếu phần lợi ích này quá thấp, hệ sinh thái sẽ phản ứng.

## 10. Lao động giao chặng cuối và lời hứa dịch vụ

Giao nhanh tạo giá trị cho khách hàng nhưng làm vận hành khó hơn.

Giờ chốt đơn, phân loại ban đêm, khung giờ giao và hàng hoàn đều cần **công suất dự phòng (capacity buffer)**. Hệ thống tối ưu không phải lúc nào cũng chạy ở 100% công suất; cần khoảng trống để hấp thụ giờ cao điểm và duy trì chất lượng dịch vụ.

> Tỷ lệ sử dụng tối đa không đồng nghĩa hiệu quả kinh tế tối đa khi chi phí thất bại dịch vụ rất cao.

## 11. CAPEX: doanh nghiệp công nghệ nhưng vẫn cần vốn vật lý lớn

Trung tâm hoàn tất đơn hàng, tự động hóa, xe/thiết bị và hạ tầng CNTT tạo CAPEX và khấu hao.

```text
CAPEX hôm nay
→ công suất tương lai
→ tăng tỷ lệ sử dụng sau đó
→ khấu hao bắt đầu
→ hoàn vốn tiền mặt muộn hơn nữa
```

Vì vậy FCF có thể cải thiện chậm hơn lợi nhuận hoạt động kế toán.

Cần hỏi công suất mới có đường đi đủ rõ để đạt mật độ cần thiết và tạo mức sinh lời chấp nhận được hay không.

## 12. Mở rộng địa lý và khả năng mang lợi thế sang thị trường khác

Mạng lưới mạnh ở Hàn Quốc không tự động sao chép được sang nước khác.

Khả năng chuyển lợi thế phụ thuộc:

```text
Mật độ dân số
Cấu trúc đô thị
Chi phí lao động
Kỳ vọng giao hàng của khách hàng
Đối thủ hiện tại
Hạ tầng thanh toán
Quy định
Chi phí bất động sản / logistics
```

Chiến lược hiệu quả ở mật độ đô thị Seoul có thể không hiệu quả tại khu vực mật độ thấp.

Mỗi thị trường quốc tế phải được mô hình hóa như một thị trường mới, không chỉ nhân quy mô thành công trong nước.

## 13. Cạnh tranh: giá, tiện lợi và độ phong phú sản phẩm

Khách hàng lựa chọn một gói giá trị:

```text
Giá
+ độ phong phú sản phẩm
+ tốc độ / độ tin cậy giao hàng
+ đổi trả
+ niềm tin
+ quyền lợi hội viên
```

Doanh nghiệp có thể duy trì giá cao hơn đôi chút nếu lợi thế tiện lợi đủ lớn, nhưng chi phí chuyển đổi trong thương mại thường thấp hơn phần mềm doanh nghiệp. Lợi thế phải được duy trì liên tục bằng dịch vụ.

## 14. Truyền dẫn vĩ mô

Suy giảm tiêu dùng ảnh hưởng thương mại qua giá trị giỏ hàng, cơ cấu hàng tùy ý và tần suất đặt hàng. Lạm phát có tác động hai chiều: GMV danh nghĩa có thể tăng vì giá, nhưng sản lượng thực và cơ cấu sản phẩm có thể xấu đi.

Chi phí lao động ảnh hưởng logistics. Nhiên liệu và vận tải ảnh hưởng giao hàng. Lãi suất ảnh hưởng nhu cầu tiêu dùng và chi phí vốn khi mở rộng mạng lưới.

```text
Thu nhập thực hộ gia đình giảm
→ chi tiêu tùy ý giảm
→ cơ cấu chuyển sang hàng thiết yếu
→ GMV / doanh thu thay đổi
→ nhu cầu quảng cáo của người bán thay đổi
→ khối lượng hoàn tất đơn hàng và mật độ thay đổi
```

## 15. Mô hình kịch bản

### Kịch bản cải thiện mật độ

```text
Khách hàng hoạt động +8%
Số đơn mỗi khách +10%
Mật độ trong cùng khu vực tăng
Chi phí/đơn -7%
Biên lợi nhuận đóng góp tăng
CAPEX tăng chậm hơn số đơn
FCF cải thiện
```

### Kịch bản tăng trưởng nhưng kinh tế không cải thiện

```text
GMV +20%
Khuyến mãi mạnh
Mở rộng sang vùng mật độ thấp
Chi phí hoàn tất đơn/đơn không giảm hoặc tăng
CAPEX +30%
FCF vẫn yếu
```

Hai kịch bản đều có tăng trưởng doanh thu hấp dẫn nhưng kinh tế cho cổ đông rất khác.

## 16. Định giá

Mô hình kết hợp thương mại và nền tảng không nên được định giá chỉ bằng bội số doanh thu.

Có thể tách:

```text
Lợi nhuận đóng góp của bán lẻ cốt lõi
+ kinh tế marketplace / quảng cáo
+ giá trị hệ sinh thái hội viên
+ hoạt động mới / quyền chọn tăng trưởng
- chi phí chung
- nhu cầu tái đầu tư logistics
```

**Định giá ngược (reverse valuation)** hỏi giá trị doanh nghiệp hiện tại đang ngầm giả định biên lợi nhuận đóng góp dài hạn và tỷ lệ tái đầu tư ở mức nào.

Tăng trưởng chỉ tạo giá trị khi phần tăng thêm tạo mức sinh lời cao hơn chi phí vốn.

## 17. Những nhầm lẫn thường gặp

### “Thương mại điện tử là công nghệ ít tài sản”

Không nhất thiết. Mô hình tự vận hành fulfillment có thể rất thâm dụng vốn.

### “GMV tăng = doanh thu tăng = lợi nhuận tăng”

Sai vì còn phụ thuộc cách ghi nhận chính/bên đại lý, take rate, cơ cấu và chi phí logistics.

### “Giao càng nhanh càng tốt”

Chỉ đúng nếu lợi ích về sẵn sàng chi trả hoặc giữ chân khách hàng lớn hơn chi phí dịch vụ tăng thêm.

### “Phí hội viên gần như là lợi nhuận 100%”

Sai vì hội viên tạo nghĩa vụ dịch vụ và làm thay đổi chi phí phục vụ khách hàng.

## 18. Bài tập nghiên cứu

| Chỉ tiêu | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Khách hàng hoạt động | | | | | |
| Doanh thu/khách hàng | | | | | |
| Doanh thu | | | | | |
| Biên gộp / biên đóng góp | | | | | |
| Tồn kho | | | | | |
| CFO | | | | | |
| CAPEX | | | | | |
| FCF | | | | | |

Nếu doanh nghiệp không công bố chính xác số đơn hoặc mật độ, có thể dùng chỉ báo thay thế nhưng phải ghi rõ đâu là suy luận.

## Mô hình tư duy cuối

> Thương mại điện tử tự vận hành fulfillment là một **mạng vật lý được điều phối bằng phần mềm**. Công nghệ giúp dự báo và điều phối; lợi thế kinh tế chỉ xuất hiện khi mật độ khách hàng, bố trí tồn kho và chất lượng vận hành làm đường chi phí–dịch vụ tốt hơn đối thủ một cách bền vững.

Đọc tiếp [10_korean_construction_pf_case](./10_korean_construction_pf_case.md) để thấy mô hình thâm dụng dự án/tài sản, nơi thời điểm dòng tiền và bảo lãnh còn quan trọng hơn doanh thu báo cáo.