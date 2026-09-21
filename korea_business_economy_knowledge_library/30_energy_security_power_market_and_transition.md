# Năng lượng, an ninh điện và chuyển đổi carbon tại Hàn Quốc (Energy Security & Transition / 에너지안보·전력시장·탄소전환)

Hàn Quốc là một nền kinh tế công nghiệp có cường độ sử dụng năng lượng cao nhưng ít tài nguyên hóa thạch trong nước và lưới điện gần như không kết nối với các nước láng giềng. Vì vậy năng lượng đồng thời là **vấn đề phụ thuộc nhập khẩu, chi phí công nghiệp, an ninh quốc gia và chuyển đổi carbon**.

Một fab bán dẫn, nhà máy thép hay trung tâm dữ liệu AI không chỉ hỏi “điện bao nhiêu won/kWh?”. Doanh nghiệp còn phải hỏi khả năng đấu nối lưới, độ ổn định điện, chất lượng điện, khả năng mua điện tái tạo và mức độ ổn định của chính sách trong suốt vòng đời dự án.

## Cân bằng năng lượng bắt đầu từ nhập khẩu

Dầu, LNG và than phần lớn phải nhập khẩu. Chi phí tính bằng KRW phụ thuộc đồng thời vào giá hàng hóa thế giới và tỷ giá:

\[
Chi\ phí\ nhập\ khẩu\ bằng\ KRW \approx Giá\ hàng\ hóa\ bằng\ USD \times KRW/USD
\]

Nếu giá dầu không đổi nhưng KRW mất giá 10%, chi phí nhập khẩu nội tệ vẫn tăng gần tương ứng trước khi tính hedge và thuế.

Một cú sốc năng lượng có thể truyền theo chuỗi:

```text
Giá dầu/LNG tăng hoặc KRW yếu
          ↓
Hóa đơn nhập khẩu tăng
          ↓
Áp lực thương mại / GDI
          ↓
Chi phí điện, nhiên liệu, vận tải tăng
          ↓
Biên lợi nhuận doanh nghiệp + thu nhập thực hộ gia đình giảm
          ↓
Lạm phát / phản ứng chính sách
```

Vì vậy năng lượng, vĩ mô và tỷ giá không thể phân tích tách rời.

## An ninh năng lượng không đồng nghĩa tự cung 100%

**An ninh năng lượng (energy security / 에너지안보)** nên được hiểu là khả năng duy trì nguồn cung với chi phí chấp nhận được khi xảy ra cú sốc.

Công cụ có thể gồm đa dạng hóa nguồn nhập, hợp đồng dài hạn, dự trữ chiến lược, điện hạt nhân, năng lượng tái tạo trong nước, tăng độ bền của lưới, điều chỉnh nhu cầu, lưu trữ và tiết kiệm năng lượng.

Tự cung tuyệt đối có thể quá đắt. Cách tiếp cận hợp lý hơn là thiết kế **danh mục chống chịu (resilience portfolio)**.

## Điện khác dầu: cân bằng gần như theo thời gian thực

Dầu có thể lưu trữ tương đối dễ. Điện trên quy mô quốc gia khó và đắt hơn nhiều nếu muốn lưu trữ lượng lớn.

Hệ thống điện phải liên tục duy trì:

\[
Phát\ điện = Nhu\ cầu + Tổn\ thất
\]

Nếu cung không đủ, tần số và điện áp có thể mất ổn định. Vì vậy hệ thống cần **biên dự phòng (reserve margin / 예비율)** và nguồn điện có khả năng điều chỉnh linh hoạt.

## Độ tin cậy có giá trị kinh tế lớn hơn hóa đơn điện

Với hộ gia đình, mất điện ngắn có thể chỉ là bất tiện. Với fab bán dẫn, một lần sụt áp hoặc mất điện có thể làm hỏng nhiều wafer và gián đoạn quy trình sạch.

Vì vậy khả năng cạnh tranh điện công nghiệp không chỉ là giá:

```text
Giá điện
+ độ tin cậy
+ tốc độ đấu nối
+ chất lượng điện
```

## Kiến trúc thị trường điện Hàn Quốc

KEPCO (한국전력공사) vẫn giữ vai trò trung tâm trong truyền tải, phân phối và cấu trúc bán lẻ, trong khi phát điện đến từ các công ty phát điện công và nhà sản xuất điện độc lập.

Giá bán buôn được hình thành qua cơ chế thị trường, còn giá bán lẻ có tính hành chính cao hơn và không phản ánh ngay từng biến động chi phí nhiên liệu.

Điều này tạo khả năng chênh lệch giữa **chi phí phát điện bán buôn** và **giá bán lẻ**. Nếu giá nhiên liệu tăng nhanh hơn tốc độ điều chỉnh biểu giá, chi phí không biến mất mà chuyển sang bảng cân đối của doanh nghiệp điện lực hoặc giá tương lai.

Xem [`25_public_enterprises_and_state_owned_companies.md`](./25_public_enterprises_and_state_owned_companies.md).

## SMP và logic chi phí cận biên

Thị trường bán buôn sử dụng khái niệm **System Marginal Price (SMP / 계통한계가격)**. Mô hình tư duy đơn giản là nguồn có chi phí cận biên thấp được huy động trước, sau đó bổ sung nguồn đắt hơn khi nhu cầu tăng; nhà máy cận biên ảnh hưởng giá thanh toán.

Do đó giá gas và nhiên liệu có thể tác động giá điện bán buôn ngay cả khi điện hạt nhân hoặc tái tạo có chi phí nhiên liệu thấp hơn.

## Biểu giá bán lẻ vừa là giá vừa là công cụ chính sách

Điện ảnh hưởng hộ gia đình, lạm phát và sức cạnh tranh công nghiệp. Nếu giá bán lẻ phản ánh ngay mọi biến động nhiên liệu, người dùng phải chịu biến động lớn. Nếu điều chỉnh bị trì hoãn, doanh nghiệp điện lực hấp thụ tổn thất trong thời gian đó.

Chính sách vì vậy quyết định **ai chịu chi phí và chịu vào lúc nào**, chứ không thể làm chi phí vật lý biến mất.

## Điện hạt nhân: vốn ban đầu rất lớn, độ nhạy nhiên liệu thấp hơn

Nhà máy hạt nhân cần CAPEX rất lớn và thời gian xây dài, nhưng chi phí nhiên liệu chiếm tỷ trọng thấp hơn nhiều nguồn nhiệt điện hóa thạch.

Phân tích vòng đời cần bao gồm xây dựng, chi phí tài chính trong quá trình xây, vận hành–bảo trì, nhiên liệu, nâng cấp an toàn, tháo dỡ và xử lý chất thải.

Đây là lý do chỉ so chi phí nhiên liệu sẽ đánh giá thiếu rủi ro vốn và thời gian.

## Trễ tiến độ làm chi phí tài chính tăng mạnh

Dự án hạt nhân kéo dài nhiều năm nên **lãi trong thời gian xây dựng (interest during construction)** là biến kinh tế lớn. Mỗi năm chậm không chỉ dời doanh thu mà còn làm chi phí vốn tích lũy thêm.

Vì vậy năng lực thực hiện dự án đúng tiến độ có giá trị tài chính trực tiếp.

## LNG: linh hoạt đổi lấy rủi ro nhập khẩu

Nhà máy gas có khả năng tăng giảm công suất linh hoạt hơn nhiều nguồn nền và hữu ích khi cân bằng điện tái tạo biến động. Nhưng Hàn Quốc nhập LNG nên hệ thống chịu rủi ro giá toàn cầu, vận tải, tỷ giá và điều khoản hợp đồng.

LNG có thể có **giá trị hệ thống (system value)** lớn dù chi phí mỗi kWh không phải thấp nhất, bởi khả năng điều chỉnh giúp duy trì ổn định lưới.

## Than: tài sản cũ và áp lực chuyển đổi

Than từng cung cấp nguồn điện ổn định quy mô lớn nhưng phát thải carbon cao. Khi tỷ trọng than giảm, nhà máy cũ có thể bị sử dụng thấp hơn và trở thành **tài sản mắc kẹt (stranded asset / 좌초자산)** trước khi hết tuổi thọ vật lý.

Chuyển đổi phải vừa giảm phát thải vừa bảo đảm đủ công suất hệ thống.

## Năng lượng tái tạo: nhiên liệu bằng 0 không có nghĩa chi phí hệ thống bằng 0

Solar và wind không cần mua nhiên liệu khi vận hành, nhưng sản lượng biến động. Khi tỷ trọng tăng, hệ thống cần thêm truyền tải, lưu trữ, nguồn điện linh hoạt, dự báo, điều chỉnh nhu cầu và quản lý cắt giảm công suất.

Vì vậy **LCOE** của riêng nhà máy không mô tả toàn bộ kinh tế hệ thống điện.

Hàn Quốc còn có hạn chế riêng về mật độ dân số, đất, địa hình và lưới.

## Điện gió ngoài khơi: tiềm năng lớn nhưng thực hiện phức tạp

Điện gió ngoài khơi cần quyền sử dụng khu vực biển, giấy phép, turbine, móng, cáp ngầm, cảng, tàu chuyên dụng, đấu nối lưới và chấp thuận địa phương.

Về thực thi, nó giống một dự án hạ tầng–đóng tàu phức tạp hơn là “chỉ lắp turbine”. Năng lực công nghiệp nặng của Hàn Quốc có thể tạo cơ hội chuỗi cung ứng, nhưng hiệu quả vẫn phụ thuộc tài chính và triển khai.

## Công suất năng lượng và công suất khả dụng là hai khái niệm khác nhau

Một nhà máy solar có thể tạo nhiều MWh trong năm nhưng không chắc phát đúng lúc đỉnh nhu cầu buổi tối mùa đông.

Quy hoạch phải hỏi cả:

```text
Một năm tạo bao nhiêu điện?
Tại giờ cao điểm có bao nhiêu công suất đáng tin cậy?
```

Đây là lý do lưu trữ, hạt nhân, gas và điều chỉnh nhu cầu có giá trị ngoài tỷ trọng sản lượng năm.

## Nút thắt lưới: có nguồn phát mà không truyền được thì vẫn là công suất bị kẹt

Dự án có thể đủ giấy phép và vốn nhưng vẫn không tạo giá trị nếu đấu nối lưới chậm. Truyền tải thường mất nhiều năm vì quy hoạch tuyến, đất và chấp thuận cộng đồng.

Ở phía nhu cầu, một cụm fab hoặc trung tâm dữ liệu cũng không thể mở rộng chỉ bằng việc công bố CAPEX nếu chưa bảo đảm điện và nước.

## Bán dẫn và AI làm nhu cầu điện tập trung hơn

Fab cần điện liên tục với chất lượng cao. Trung tâm dữ liệu AI tạo tải rất lớn và mật độ công suất cao. Vì vậy chiến lược AI và bán dẫn nối trực tiếp với quy hoạch lưới điện.

Không khu vực nào có thể thu hút vô hạn data center hoặc fab chỉ bằng ưu đãi thuế nếu hạ tầng điện không theo kịp.

## Độ nhạy của ngành với giá điện rất khác nhau

Nếu điện chiếm 5% tổng chi phí sản xuất, tăng giá điện 20% có thể làm tổng chi phí tăng khoảng 1 điểm phần trăm trước khi tính tiết kiệm hoặc chuyển giá.

Với ngành biên lợi nhuận mỏng, thay đổi đó có thể tác động EBIT đáng kể.

Trung tâm dữ liệu có tải liên tục; lò điện rất thâm dụng điện; bán dẫn cần cả điện, nước và độ tin cậy; hóa chất có cấu trúc phức tạp giữa năng lượng và nguyên liệu đầu vào.

## Mua điện tái tạo và RE100

Khách hàng toàn cầu có thể yêu cầu nhà cung cấp sử dụng điện tái tạo. Doanh nghiệp xuất khẩu Hàn Quốc có thể dùng PPA, chứng chỉ hoặc các cơ chế khác theo quy định hiện hành.

Khả năng tiếp cận điện sạch vì vậy trở thành yếu tố cạnh tranh của hợp đồng xuất khẩu:

```text
Yêu cầu ESG của khách hàng
→ nhu cầu mua điện tái tạo
→ chi phí năng lượng / lựa chọn địa điểm
→ khả năng cạnh tranh hợp đồng
```

## K-ETS: biến phát thải thành chi phí tài chính

**Hệ thống giao dịch phát thải Hàn Quốc (K-ETS / 배출권거래제)** tạo giá cho carbon đối với các doanh nghiệp thuộc diện áp dụng.

\[
Chi\ phí\ carbon = Phát\ thải\ ròng\ cần\ mua\ quyền \times Giá\ quyền\ phát\ thải
\]

Thép, hóa chất, xi măng và điện đặc biệt nhạy. Phân bổ miễn phí có thể giảm gánh nặng ngắn hạn nhưng không loại bỏ áp lực khử carbon dài hạn.

## Carbon ở biên giới biến phát thải trong nước thành biến xuất khẩu

Nếu thị trường nhập khẩu yêu cầu báo cáo hoặc tính chi phí carbon trong sản phẩm, phát thải của nhà máy Hàn Quốc ảnh hưởng trực tiếp khả năng tiếp cận và giá bán ở nước ngoài.

Doanh nghiệp xuất khẩu vì vậy phải quản lý cường độ carbon, khả năng truy xuất và yêu cầu của khách hàng, không chỉ tuân thủ quy định nội địa.

## Thép và hóa chất là các ngành khó giảm phát thải

Giảm carbon trong lò cao hoặc feedstock hóa dầu khó hơn nhiều so với điện hóa xe cá nhân. Các lựa chọn có thể gồm hydro, lò điện, nguyên liệu tái chế, **thu giữ–sử dụng–lưu trữ carbon (CCUS)**, feedstock carbon thấp và điện sạch.

Các công nghệ này thường cần CAPEX lớn trong khi giá carbon và mức sẵn sàng trả thêm của khách hàng chưa chắc chắn. Vì vậy kinh tế chuyển đổi chứa đồng thời rủi ro công nghệ, chính sách và nhu cầu.

## Hydro là chất mang năng lượng, không phải nguồn năng lượng miễn phí

Hydro phải được sản xuất bằng năng lượng khác. Hiệu quả kinh tế phụ thuộc phương pháp sản xuất, giá điện/gas, cường độ carbon, lưu trữ, vận chuyển, tổn thất chuyển đổi và giá trị sử dụng cuối.

Không nên đánh giá “kinh tế hydro” chỉ từ chi phí sản xuất tại nhà máy mà phải nhìn cả chuỗi.

## Ammonia là một phương tiện vận chuyển hydro

Ammonia có thể dễ vận chuyển hơn hydro trong một số trường hợp, nhưng cần tổng hợp và có thể phải cracking trở lại thành hydro. Mỗi lần chuyển đổi làm mất năng lượng và cần thêm CAPEX.

Đây là bài toán tối ưu hệ thống, không phải câu hỏi “chất mang nào rẻ hơn” đơn giản.

## ESS: giá trị không chỉ là mua điện rẻ rồi bán điện đắt

**Hệ thống lưu trữ năng lượng (Energy Storage System / ESS)** có thể cung cấp chênh lệch giá điện, điều tần, dự phòng, làm mượt tái tạo và giảm tắc nghẽn lưới.

Giá trị kinh tế phụ thuộc thiết kế thị trường: hệ thống có được trả tiền cho các dịch vụ đó hay không.

## Điều chỉnh nhu cầu: đôi khi công suất rẻ nhất là “không dùng điện lúc này”

**Demand Response (수요반응)** trả tiền cho người dùng để dịch chuyển hoặc giảm tải khi hệ thống căng thẳng. Điều này có thể giảm nhu cầu xây nguồn đỉnh và giảm áp lực lưới.

Khả năng tham gia khác nhau theo ngành; fab liên tục có ít linh hoạt hơn một số tải thương mại hoặc data center có hệ thống dự phòng.

## Hiệu quả năng lượng là “nguồn cung ảo”

Tiết kiệm 1 MWh có thể tương đương tạo thêm 1 MWh nếu chi phí đầu tư tiết kiệm thấp hơn chi phí xây nguồn mới. Hiệu quả năng lượng đồng thời giảm phụ thuộc nhập khẩu và giảm tải lưới.

Trong nền kinh tế trưởng thành, tối ưu quy trình và tòa nhà có thể rẻ hơn việc bổ sung phát điện cho mọi mức tăng nhu cầu.

## Chuyển đổi năng lượng là bài toán phân bổ vốn

Doanh nghiệp điện lực và công nghiệp phải quyết định vừa duy trì tài sản cũ vừa đầu tư công nghệ mới trong khi nhu cầu và chính sách chưa chắc chắn.

Đầu tư quá ít tạo rủi ro thiếu công suất; đầu tư quá nhiều tạo tài sản sử dụng thấp hoặc mắc kẹt. Vì vậy cần tư duy danh mục thay vì đặt cược toàn bộ vào một công nghệ.

## Kế hoạch điện là quỹ đạo chính sách, không phải kết quả chắc chắn

Các kế hoạch cung–cầu điện dài hạn cho biết hướng mong muốn về nuclear, renewables, coal và LNG. Nhưng kế hoạch chỉ trở thành sản lượng thực khi giấy phép, xây dựng, lưới, nhu cầu và chi phí được thực hiện thành công.

Nhà phân tích nên dùng kế hoạch làm kịch bản nền rồi theo dõi tiến độ thực tế.

## Xuất khẩu hạt nhân là một ngành công nghiệp phức hợp

Năng lực hạt nhân của Hàn Quốc gồm kỹ thuật, EPC, linh kiện, vận hành và dịch vụ vòng đời. Dự án xuất khẩu còn liên quan ngoại giao, tín dụng chủ quyền và chu kỳ xây dựng dài.

Vì vậy kinh tế xuất khẩu hạt nhân gần với hạ tầng nặng và quốc phòng hơn là kinh doanh hàng hóa năng lượng thông thường.

## Cách phân tích doanh nghiệp điện lực và doanh nghiệp thâm dụng điện

Với doanh nghiệp điện lực, theo dõi giá nhiên liệu, chi phí mua điện, điều chỉnh biểu giá, cơ cấu phát điện, tỷ giá, chi phí lãi vay, nợ, CAPEX lưới và tăng trưởng nhu cầu.

Với doanh nghiệp thâm dụng điện, cần hỏi tỷ trọng điện trong chi phí, loại biểu giá, hồ sơ phụ tải, độ nhạy mất điện, nghĩa vụ điện tái tạo, khả năng chuyển giá và công suất đấu nối đã được bảo đảm hay chưa.

## Stress test

Các kịch bản hữu ích gồm LNG +30%, KRW yếu 10%, giá điện công nghiệp +15%, đấu nối lưới chậm 2 năm, giá carbon tăng gấp đôi hoặc nhu cầu AI tăng nhanh hơn hạ tầng lưới.

Quan trọng là đưa cú sốc xuống dòng tiền doanh nghiệp và bảng cân đối utility, không dừng ở tiêu đề năng lượng.

## Mental Model — mô hình tư duy

> Hàn Quốc phải tối ưu đồng thời bốn mục tiêu: **an ninh nguồn cung, khả năng chi trả, độ tin cậy và khử carbon**. Không có một công nghệ duy nhất tối đa hóa cả bốn; chiến lược năng lượng là bài toán danh mục và tích hợp hệ thống.

```text
Nhiên liệu nhập khẩu + nguồn điện trong nước
              ↓
Thị trường bán buôn / lưới
              ↓
Biểu giá bán lẻ + độ tin cậy
              ↓
Hộ gia đình / doanh nghiệp
              ↓
Lạm phát + sức cạnh tranh + đầu tư
```

## Những nhầm lẫn thường gặp

Điện tái tạo có nhiên liệu bằng 0 nhưng hệ thống vẫn cần lưới và lưu trữ. Nuclear có chi phí nhiên liệu thấp nhưng dự án vẫn có rủi ro vốn và tiến độ. Giá điện thấp không chứng minh chi phí phát điện thấp. An ninh năng lượng không có nghĩa phải tự sản xuất mọi thứ. Có thêm nguồn phát không giải được thiếu điện nếu truyền tải bị nghẽn. Hydro nên được hiểu là chất mang năng lượng được sản xuất từ nguồn khác.

## Liên kết

Đọc cùng [`01_macro_economy_and_business_cycle.md`](./01_macro_economy_and_business_cycle.md), [`14_semiconductors_electronics_display.md`](./14_semiconductors_electronics_display.md), [`16_shipbuilding_steel_chemicals_heavy_industry.md`](./16_shipbuilding_steel_chemicals_heavy_industry.md), [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md), [`25_public_enterprises_and_state_owned_companies.md`](./25_public_enterprises_and_state_owned_companies.md), [`32_defense_aerospace_and_strategic_industries.md`](./32_defense_aerospace_and_strategic_industries.md) và [`34_digital_fintech_cloud_and_it_services.md`](./34_digital_fintech_cloud_and_it_services.md).
