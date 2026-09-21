# Biohealth, dược phẩm, thiết bị y tế và K-Beauty Hàn Quốc (Biohealth / 바이오헬스·제약·의료기기·K뷰티)

Biohealth là một trong những lĩnh vực cho thấy Hàn Quốc đang chuyển từ tăng trưởng thiên về sản xuất sang mô hình kết hợp **khoa học + quy định + IP + sản xuất giá trị cao**. Nhưng “bio” là nhãn rất rộng. Phát triển thuốc mới, biosimilar, CDMO, chẩn đoán, thiết bị y tế và mỹ phẩm có mô hình kinh doanh, yêu cầu vốn và dạng thất bại hoàn toàn khác nhau.

Nếu dùng một bội số định giá hoặc một logic kiểu “già hóa → bio tốt” cho tất cả doanh nghiệp, phân tích gần như chắc chắn sai.

## Ba cổng của kinh tế biohealth

Một công nghệ y tế thường phải đi qua ba cổng:

```text
Thành công kỹ thuật
      ↓
Được cơ quan quản lý cho phép
      ↓
Được thị trường chấp nhận / được hoàn trả chi phí
```

Thất bại ở bất kỳ cổng nào đều có thể làm giá trị kỳ vọng giảm mạnh.

Đây là điểm khác lớn với sản xuất thông thường. Một nhà máy thường có thể bán sản phẩm khi sản phẩm hoạt động và đạt tiêu chuẩn; thuốc hoặc thiết bị y tế còn phải đi qua nhiều năm thử nghiệm, phê duyệt và chấp nhận của bên thanh toán.

# Phần I — Phát triển thuốc mới (Innovative Pharma / 신약개발)

## Phát triển thuốc là một chuỗi xác suất

Một pipeline đơn giản:

```text
Khám phá hoạt chất
→ Tiền lâm sàng
→ Giai đoạn 1
→ Giai đoạn 2
→ Giai đoạn 3
→ Thẩm định của cơ quan quản lý
→ Ra mắt thị trường
→ Theo dõi sau lưu hành
```

Mỗi giai đoạn có xác suất thất bại riêng.

Nếu xác suất thành công ở các bước là `p1...pn`:

\[
P(thành\ công) \approx \prod_i p_i
\]

Đây là lý do một tài sản đang ở Phase 1 không thể được định giá chỉ bằng doanh số đỉnh tương lai rồi chiết khấu theo thời gian. Nó cần **giá trị đã điều chỉnh xác suất**.

## rNPV: logic định giá đã điều chỉnh rủi ro

Một rNPV đơn giản:

\[
rNPV = \sum_t \frac{P_t \times Dòng\ tiền\ kỳ\ vọng_t}{(1+r)^t} - Chi\ phí\ R\&D\ còn\ lại
\]

`P_t` phản ánh xác suất đạt tới giai đoạn tương lai hoặc thương mại hóa.

rNPV rất nhạy với giả định. Nó là khung tư duy, không phải “sự thật định giá”.

## Tiêu chí đánh giá thử nghiệm và thiết kế nghiên cứu là biến kinh tế

Kết quả thử nghiệm không chỉ phụ thuộc “thuốc có tác dụng hay không”. Nó còn phụ thuộc **tiêu chí đánh giá (clinical endpoint)**, thuốc đối chứng, quần thể bệnh nhân và thiết kế thống kê.

Một thuốc có thể có tác dụng sinh học nhưng vẫn không đạt ngưỡng cơ quan quản lý hoặc ngưỡng thương mại cần thiết.

Vì vậy người phân tích cần hiểu “thành công” trong protocol thực sự nghĩa là gì.

## Runway tiền mặt: biotech có thể hết tiền trước khi khoa học cho câu trả lời

Biotech nhỏ thường ít doanh thu định kỳ.

\[
Runway \approx \frac{Tiền\ mặt}{Mức\ đốt\ tiền\ mỗi\ quý}
\]

Nếu runway kết thúc trước mốc dữ liệu lâm sàng quan trọng tiếp theo, rủi ro pha loãng và huy động vốn trở thành trung tâm.

Một phân tử rất tốt nhưng tài chính yếu vẫn có thể phá hủy giá trị cổ đông qua nhiều vòng phát hành cổ phiếu giá thấp.

## Hợp đồng cấp phép: giá trị headline thường không phải tiền chắc chắn

Hợp đồng licensing biotech thường gồm:

```text
Khoản trả trước (upfront)
Mốc phát triển
Mốc phê duyệt
Mốc doanh số
Tiền bản quyền (royalty)
```

Một thương vụ được quảng bá “1 tỷ USD” có thể phần lớn là các khoản mốc có điều kiện.

Luôn tách:

```text
Tiền chắc chắn nhận ngay
so với
Tiền tương lai phụ thuộc xác suất
```

## Bằng sáng chế và “vách bằng sáng chế”

Giá trị dược phẩm phụ thuộc thời gian độc quyền.

Hệ thống bằng sáng chế có thể gồm bằng sáng chế cho phân tử, công thức, quy trình và mục đích sử dụng với ngày hết hạn khác nhau.

Khi độc quyền suy yếu, thuốc generic hoặc biosimilar có thể làm giá và thị phần giảm.

Vì vậy dòng tiền thương mại phải có giả định hữu hạn về thời gian độc quyền.

# Phần II — Biosimilar (바이오시밀러)

## Biosimilar không đơn giản là “generic của thuốc sinh học”

Thuốc sinh học là phân tử phức tạp được tạo qua hệ thống sống và quy trình sản xuất. Điều kiện sản xuất có thể ảnh hưởng đặc tính sản phẩm.

Biosimilar phải chứng minh mức tương đồng cao và tính tương đương theo quy định; năng lực quy trình và chất lượng vì vậy rất quan trọng.

Rào cản gồm:

- phân tích đặc tính sản phẩm;
- bằng chứng lâm sàng và pháp quy;
- sản xuất GMP;
- quy mô sản xuất;
- đối tác thương mại toàn cầu.

## Hết bằng sáng chế tạo cơ hội, không bảo đảm thị phần

Khi độc quyền của thuốc gốc hết, thị trường mở ra nhưng thị phần còn phụ thuộc:

- niềm tin của bác sĩ;
- động lực của bên thanh toán;
- quy tắc chuyển đổi thuốc;
- mức giảm giá;
- mua sắm bệnh viện;
- năng lực thương mại và thương hiệu.

Kinh tế biosimilar vì vậy là sự kết hợp giữa khoa học, quy định và chiến lược tiếp cận thị trường.

## Giá giảm dần và chiến lược danh mục sản phẩm

Doanh nghiệp vào sớm có thể giành thị phần hấp dẫn, nhưng khi nhiều đối thủ tham gia, giá thường chịu áp lực giảm.

Vì vậy doanh nghiệp cần pipeline gồm nhiều biosimilar hoặc sản phẩm sinh học mới thay vì phụ thuộc mãi vào một phân tử.

Thời điểm ra mắt từng sản phẩm trong danh mục trở thành biến quan trọng.

# Phần III — CDMO (위탁개발생산)

## CDMO bán năng lực phát triển và sản xuất dưới dạng dịch vụ

**Tổ chức phát triển và sản xuất theo hợp đồng (Contract Development and Manufacturing Organization / CDMO)** giúp khách hàng phát triển và sản xuất thuốc sinh học hoặc dược phẩm.

Mô hình này gần với dịch vụ công nghiệp công nghệ cao hơn là “đặt cược nghiên cứu” của biotech phát triển thuốc mới.

Các biến cốt lõi:

```text
Công suất lắp đặt
Tỷ lệ sử dụng
Backlog / hợp đồng khách hàng
Tỷ lệ mẻ sản xuất đạt chuẩn
Mức tập trung khách hàng
CAPEX / khấu hao
```

## Chi phí cố định cao tạo đòn bẩy hoạt động

Bioreactor và nhà máy cần cơ sở vật chất đắt đỏ, hệ thống vô trùng và quy trình thẩm định nghiêm ngặt.

Khi tỷ lệ sử dụng thấp, khấu hao và lao động cố định trên mỗi mẻ cao. Khi tỷ lệ sử dụng tăng, chi phí đơn vị giảm.

Logic giống fab bán dẫn, nhưng quy định và yêu cầu chất lượng làm việc chuyển nhà sản xuất khó hơn.

## Chứng nhận và GMP tạo chi phí chuyển đổi

Khi khách hàng chuyển địa điểm sản xuất thuốc sinh học, họ có thể phải chuyển quy trình, thẩm định lại và nộp hồ sơ pháp quy.

Vì vậy nhà máy đã được chứng nhận thành công có thể có chi phí chuyển đổi cao.

Lịch sử chất lượng trở thành **tài sản vô hình**.

Một sự cố nhiễm bẩn hoặc sai lệch quy trình có thể dừng sản xuất, kích hoạt thanh tra và phá niềm tin nhiều hơn rất nhiều so với giá trị của một mẻ bị mất.

## Rủi ro mở rộng công suất

Nhu cầu cao có thể khiến toàn ngành đồng thời mở rộng CAPEX.

Nếu quá nhiều công suất đi vào vận hành trước nhu cầu thực, tỷ lệ sử dụng và biên lợi nhuận giảm.

Vì vậy công suất bioreactor công bố không phải bảo đảm doanh thu tương lai.

# Phần IV — Thiết bị y tế và chẩn đoán (Medical Devices & Diagnostics / 의료기기·진단)

## Thiết bị y tế nằm giữa điện tử và quy định y tế

Máy chẩn đoán hình ảnh, siêu âm, thiết bị phẫu thuật, xét nghiệm và hệ thống y tế số kết hợp phần cứng/phần mềm với bằng chứng pháp quy.

Thành công thương mại cần:

- phê duyệt;
- được bệnh viện mua;
- phù hợp quy trình lâm sàng;
- dịch vụ và đào tạo;
- cơ chế hoàn trả trong một số sản phẩm.

Ưu thế kỹ thuật một mình có thể không vượt được sự trì trệ trong mua sắm và thay đổi quy trình bệnh viện.

## Kinh tế của nền thiết bị đã lắp đặt

Nhà cung cấp có thể bán hoặc đặt thiết bị rồi tạo doanh thu định kỳ từ:

- vật tư tiêu hao;
- thuốc thử;
- hợp đồng dịch vụ;
- nâng cấp phần mềm.

Mô hình này gần với logic “máy in–mực in”: thiết bị tạo một nền khách hàng đã cài đặt, sau đó vật tư và dịch vụ tạo doanh thu lặp lại.

Nền thiết bị đã lắp đặt có thể tạo chi phí chuyển đổi vì nhân viên đã được đào tạo và workflow đã tích hợp.

## Chẩn đoán: số xét nghiệm × mức hoàn trả × biên vật tư

Kinh tế của hệ thống chẩn đoán thường phụ thuộc nhiều vào số xét nghiệm thực hiện trên nền thiết bị đã lắp hơn là số thiết bị bán mới.

Vì vậy thiết bị có thể đóng vai trò “kênh thu hút” cho doanh thu thuốc thử và vật tư tiêu hao định kỳ.

Cần tách doanh thu bán máy với doanh thu vật tư phía sau.

# Phần V — Hoàn trả chi phí và kinh tế bên thanh toán (Reimbursement & Payer Economics / 보험·약가)

## Nhu cầu bệnh nhân không bằng quy mô thị trường thương mại

\[
Thị\ trường\ thương\ mại \neq Số\ bệnh\ nhân \times Giá\ niêm\ yết
\]

Cần điều chỉnh theo:

- số bệnh nhân được chẩn đoán;
- quần thể đủ điều kiện;
- phạm vi bảo hiểm/hoàn trả;
- giá sau đàm phán;
- mức chấp nhận của bác sĩ;
- mức tuân thủ điều trị;
- cạnh tranh.

Hệ thống bảo hiểm y tế quốc gia làm bên thanh toán có quyền thương lượng đáng kể.

## Già hóa làm tăng nhu cầu nhưng không tạo quyền định giá vô hạn

Dân số già làm nhu cầu bệnh mạn tính, chẩn đoán và chăm sóc tăng.

Nhưng ngân sách bên thanh toán vẫn có giới hạn. Khối lượng có thể tăng trong khi giá hoàn trả bị gây áp lực.

Vì vậy **gió thuận nhân khẩu học không đồng nghĩa biên lợi nhuận chắc chắn mở rộng**.

# Phần VI — K-Beauty (K뷰티)

## Mỹ phẩm là kinh tế thương hiệu tiêu dùng, không phải kinh tế dược phẩm

K-Beauty thường xuất hiện trong thống kê xuất khẩu biohealth, nhưng mô hình kinh doanh gần hàng tiêu dùng hơn dược phẩm.

Rào cản gia nhập thấp hơn thuốc mới. Chu kỳ sản phẩm nhanh hơn, còn thương hiệu, mạng xã hội và phân phối quan trọng hơn.

Một thương hiệu mỹ phẩm có thể tung sản phẩm rất nhanh, nhưng đối thủ cũng vậy.

## Hệ sinh thái ODM/OEM làm giảm rào cản nhà máy

Hàn Quốc có hệ sinh thái **ODM/OEM mỹ phẩm** mạnh. Thương hiệu có thể thuê ngoài công thức và sản xuất, nhờ đó ra mắt nhanh mà không cần sở hữu nhà máy.

Chuỗi giá trị mô-đun này làm nhu cầu vốn thấp hơn nhưng chuyển trọng tâm khác biệt sang:

- thương hiệu;
- cộng đồng/influencer;
- ý tưởng sản phẩm;
- kênh bán;
- tốc độ;
- mua lặp lại.

## Tăng trưởng viral khác thương hiệu bền vững

Một SKU lan truyền mạnh có thể làm doanh thu bùng nổ.

Nhưng tính bền vững cần:

- mua lặp lại;
- pipeline sản phẩm mới;
- phân phối đa kênh;
- đa dạng địa lý;
- giá trị thương hiệu vượt khỏi một sản phẩm.

Vì vậy tăng follower hoặc độ nóng trên mạng xã hội nên được nối với dữ liệu bán thực tế nếu có thể.

## Sell-in và sell-through

**Sell-in:** thương hiệu giao hàng cho nhà phân phối hoặc nhà bán lẻ.

**Sell-through:** người tiêu dùng cuối mua hàng.

Sell-in mạnh nhưng sell-through yếu có thể tạo tồn kho trong kênh và sau đó dẫn tới hoàn trả hoặc giảm giá.

Nên kiểm tra khoản phải thu, tồn kho và dữ liệu nhà phân phối, không chỉ doanh thu.

## Kinh tế từng kênh phân phối

Kênh có thể gồm cửa hàng chuyên mỹ phẩm, trung tâm thương mại, D2C, marketplace toàn cầu và nhà phân phối địa phương.

Mỗi kênh có khác biệt về:

- biên lợi nhuận gộp;
- chi phí marketing;
- ai sở hữu tồn kho;
- khả năng tiếp cận dữ liệu khách hàng;
- chi phí thu hút khách hàng.

D2C có thể có biên gộp cao hơn nhưng CAC, logistics và đổi trả cũng cao. Marketplace giúp mở rộng quốc tế nhanh nhưng phụ thuộc phí nền tảng và thuật toán xếp hạng.

## Tồn kho và hạn sử dụng

Mỹ phẩm và dược phẩm có hạn sử dụng.

Tăng trưởng nhanh rồi nhu cầu giảm có thể tạo giảm giá hàng tồn kho hoặc bán tháo.

Doanh thu cao gần cuối quý nên được so cùng khoản phải thu và sell-through phía dưới nếu rủi ro tập trung nhà phân phối lớn.

# Đa dạng hóa xuất khẩu

Xuất khẩu biohealth và mỹ phẩm đã mở rộng từ Trung Quốc sang Mỹ, châu Âu, Nhật Bản và các thị trường khác.

Đa dạng hóa giảm rủi ro phụ thuộc một quốc gia nhưng làm tăng phức tạp pháp quy và kênh bán.

Mỗi khu vực có thể yêu cầu phê duyệt, nhãn, hồ sơ và chiến lược thương mại riêng.

Mở rộng toàn cầu vì vậy cần năng lực tổ chức pháp quy, không chỉ dịch ngôn ngữ và marketing.

## Ảnh chụp xuất khẩu năm 2025

KHIDI công bố xuất khẩu biohealth Hàn Quốc năm 2025 khoảng **27,87 tỷ USD**, gồm dược phẩm, thiết bị y tế và mỹ phẩm. Đây là ảnh chụp có mốc thời gian, được công bố năm 2026; phân tích hiện tại phải dùng dữ liệu chính thức mới nhất.

Thông điệp cấu trúc rộng hơn là biohealth và K-Beauty đang trở thành động cơ xuất khẩu đáng kể bên cạnh công nghiệp nặng truyền thống.

# Các kiểu doanh nghiệp: không so sánh những mô hình không cùng loại

## Biotech phát triển thuốc

Theo dõi:

```text
Runway tiền mặt
Giai đoạn pipeline
Mốc thử nghiệm lâm sàng
Giả định rNPV
Licensing / upfront
Rủi ro pha loãng
```

## Biosimilar

```text
Phê duyệt
Thời điểm ra mắt
Thị phần
Mức giảm giá
Chi phí sản xuất
Đối tác thương mại
```

## CDMO

```text
Công suất
Tỷ lệ sử dụng
Backlog / hợp đồng
Mức tập trung khách hàng
CAPEX / khấu hao
Lịch sử chất lượng / thanh tra
```

## Thiết bị / chẩn đoán

```text
Nền thiết bị đã lắp
Doanh thu vật tư / thuốc thử
Phê duyệt / hoàn trả
Kênh bệnh viện
Biên dịch vụ
```

## Thương hiệu mỹ phẩm

```text
Mức tập trung SKU
Tỷ lệ mua lặp lại
Cơ cấu kênh / địa lý
Hiệu quả marketing
Tồn kho / phải thu
Sell-through
```

## ODM mỹ phẩm

```text
Mức tập trung khách hàng
Khối lượng đơn hàng
Năng lực R&D / công thức
Tỷ lệ sử dụng nhà máy
Biên lợi nhuận theo cơ cấu sản phẩm
```

Dùng một “bội số bio” chung cho tất cả mô hình là vô nghĩa.

# Khác biệt về phân bổ vốn và tài trợ

Biotech chưa có doanh thu nên ưu tiên bảo toàn runway và tài trợ cho các mốc nghiên cứu.

CDMO trưởng thành có thể dùng nợ nhiều hơn vì dòng tiền sản xuất theo hợp đồng dễ dự báo hơn.

Thương hiệu mỹ phẩm có thể ít tài sản cố định nhưng vẫn cần vốn lưu động và marketing.

Công ty thiết bị có thể cần tổ chức dịch vụ sau bán hàng và tồn kho.

Cùng một tỷ lệ đòn bẩy có mức rủi ro khác nhau giữa các mô hình.

# Lợi thế pháp quy: vừa là rào cản vừa là rủi ro nhị phân

Chi phí tuân thủ làm chậm đối thủ mới, nhưng khi doanh nghiệp xây được hệ thống chất lượng và lịch sử phê duyệt, đó có thể trở thành lợi thế.

Tuy nhiên cùng sự phụ thuộc đó tạo rủi ro giảm mạnh nếu xảy ra:

- thử nghiệm thất bại;
- sự cố thanh tra;
- cảnh báo / thu hồi;
- chậm phê duyệt.

Không được giả định thành công pháp quy chỉ vì công nghệ có vẻ hứa hẹn.

# Chất lượng sản xuất là tài sản kinh tế

GMP, hồ sơ mẻ sản xuất, thẩm định và lịch sử thanh tra không được phản ánh đầy đủ trên bảng cân đối.

Nhưng khách hàng có dám giao sản xuất thuốc sinh học cho một CDMO hay không phụ thuộc rất mạnh vào chúng.

Một sự cố chất lượng có thể phá nhiều năm niềm tin.

Vì vậy hệ thống chất lượng là **vốn vô hình (intangible capital)**.

# Kiểm tra sức chịu đựng

Biotech phát triển thuốc:

- thử nghiệm chậm 1 năm;
- xác suất thành công giảm;
- thị trường vốn đóng lại.

CDMO:

- tỷ lệ sử dụng giảm 15 điểm %;
- khách hàng lớn trì hoãn;
- nhà máy mới tăng công suất chậm.

Biosimilar:

- ra mắt chậm;
- giá giảm nhanh hơn;
- đối thủ vào sớm hơn.

Beauty:

- SKU viral mất đà;
- CAC tăng gấp đôi;
- tồn kho nhà phân phối tăng;
- quy định kênh Trung Quốc/Mỹ thay đổi.

# Mô hình tư duy

> Biohealth biến **khoa học thành dòng tiền thông qua thành công kỹ thuật, quy định, chất lượng sản xuất và khả năng tiếp cận thương mại**. K-Beauty chia sẻ logic xuất khẩu/thương hiệu toàn cầu nhưng vận hành theo kinh tế hàng tiêu dùng thay vì kinh tế xác suất của dược phẩm.

```text
Tri thức / công thức / IP
          ↓
Phát triển / sản xuất
          ↓
Cổng pháp quy / chất lượng
          ↓
Kênh bán / hoàn trả
          ↓
Chấp nhận / sử dụng lặp lại
          ↓
Dòng tiền
```

# Những nhầm lẫn thường gặp

**“Dân số bệnh nhân lớn = doanh thu lớn.”** Sai. Hoàn trả và mức chấp nhận quyết định thị trường thương mại thực.

**“Biosimilar chỉ là generic của thuốc sinh học.”** Sai. Độ phức tạp quy trình và pháp quy cao hơn nhiều.

**“CDMO không phát triển thuốc nên gần như không có rủi ro.”** Sai. Công suất, khách hàng và chất lượng vẫn là rủi ro lớn.

**“Già hóa bảo đảm lợi nhuận y tế tăng.”** Sai. Bên thanh toán có thể gây áp lực giá.

**“K-Beauty xuất khẩu tăng nghĩa thương hiệu nào cũng có moat.”** Sai. ODM làm rào cản sản xuất thấp; mua lặp lại, thương hiệu và kênh mới quyết định độ bền.

**“Headline licensing deal = tiền chắc chắn.”** Sai. Phần lớn giá trị có thể là các mốc phụ thuộc điều kiện.

# Liên kết

Đọc cùng [`02_trade_export_and_global_value_chains.md`](./02_trade_export_and_global_value_chains.md), [`07_startups_venture_and_scaleups.md`](./07_startups_venture_and_scaleups.md), [`27_demographics_households_and_consumption.md`](./27_demographics_households_and_consumption.md), [`29_innovation_rnd_education_and_human_capital.md`](./29_innovation_rnd_education_and_human_capital.md) và [`33_logistics_ports_and_distribution_networks.md`](./33_logistics_ports_and_distribution_networks.md).

### Nguồn nền

- Korea Health Industry Development Institute (KHIDI), kết quả xuất khẩu Biohealth 2025 công bố năm 2026: https://www.khidi.or.kr/board/view?linkId=48940966&menuId=MENU00100
- Tài liệu triển vọng ngành/xuất khẩu của KHIDI.
- Công bố của cơ quan quản lý Hàn Quốc/quốc tế và hồ sơ doanh nghiệp cho phân tích từng sản phẩm.