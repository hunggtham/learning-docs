# Bán dẫn, điện tử và màn hình Hàn Quốc (Semiconductors & Electronics / 반도체·전자·디스플레이)

Bán dẫn là một trong những ngành quan trọng nhất để hiểu kinh tế Hàn Quốc hiện đại vì nó kết hợp hầu hết các chủ đề lớn của thư viện: **cường độ vốn cao, R&D, học qua thực hành, phụ thuộc xuất khẩu, quy mô chaebol, hệ sinh thái nhà cung cấp, tính chu kỳ và địa chính trị**.

Nhưng “ngành bán dẫn” không phải một mô hình kinh doanh duy nhất. Bộ nhớ, foundry, fabless, thiết bị, vật liệu, đóng gói và điện tử thành phẩm có cấu trúc kinh tế rất khác nhau. Nếu chỉ nhìn tiêu đề “nhu cầu chip tăng”, rất dễ áp sai logic cho từng công ty.

## Từ điện tử tiêu dùng tới năng lực bán dẫn

Ngành điện tử Hàn Quốc không bắt đầu ở biên công nghệ. Giai đoạn đầu dựa nhiều vào linh kiện nhập khẩu, cấp phép, lắp ráp và học hỏi từ công nghệ nước ngoài.

Có thể hình dung quá trình tích lũy năng lực:

```text
Lắp ráp
   ↓
Nội địa hóa linh kiện
   ↓
Kỹ thuật quy trình
   ↓
Tự thiết kế sản phẩm
   ↓
Linh kiện cốt lõi / bán dẫn
   ↓
R&D tuyến đầu + tiêu chuẩn + hệ sinh thái
```

Đây là **học qua thực hành (learning-by-doing / 생산을 통한 학습)**. Năng lực không chỉ đến từ bằng sáng chế; nó tích lũy qua lặp lại sản xuất, xử lý lỗi, phối hợp nhà cung cấp và kinh nghiệm vận hành thiết bị.

Bán dẫn là bước nhảy khó hơn lắp ráp điện tử vì fab cần lượng vốn rất lớn và thế hệ công nghệ thay đổi liên tục.

## Chuỗi giá trị bán dẫn

Một chuỗi đơn giản:

```text
EDA / IP / Kiến trúc
        ↓
Thiết kế chip (Fabless / IDM)
        ↓
Chế tạo wafer (Foundry / IDM)
        ↓
Lắp ráp / đóng gói / kiểm thử
        ↓
Hệ thống / thiết bị cuối
```

Song song là hệ sinh thái thiết bị và vật liệu: quang khắc, khắc, lắng đọng, đo kiểm; wafer, khí, photoresist, hóa chất; substrate và vật liệu đóng gói.

**IDM (Integrated Device Manufacturer / 종합반도체기업)** thực hiện nhiều công đoạn. **Fabless (팹리스)** tập trung thiết kế. **Foundry (파운드리)** sản xuất theo thiết kế của khách hàng. **OSAT** tập trung lắp ráp và kiểm thử.

Trước khi chọn chỉ số tài chính, phải xác định công ty đang đứng ở nút nào của chuỗi giá trị.

## Bộ nhớ: sản phẩm chuẩn hóa và chu kỳ cung–cầu

DRAM và NAND là hai nhóm bộ nhớ lớn. Bộ nhớ có mức chuẩn hóa cao hơn nhiều loại chip logic tùy biến, nên cân bằng cung–cầu toàn ngành ảnh hưởng mạnh tới **giá bán bình quân (Average Selling Price / ASP)**.

Một chu kỳ bộ nhớ điển hình:

```text
Nhu cầu mạnh / cung thiếu
        ↓
ASP + lợi nhuận ↑
        ↓
CAPEX ↑
        ↓
Công suất tăng theo sau
        ↓
Tồn kho ↑ / ASP ↓
        ↓
Cắt CAPEX
        ↓
Tăng cung chậm lại
        ↓
Phục hồi
```

Đây là chu kỳ điển hình của ngành thâm dụng vốn và có nét giống hàng hóa. Tuy nhiên “giống hàng hóa” không có nghĩa sản phẩm hoàn toàn đồng nhất; node công nghệ, hiệu quả điện năng, độ tin cậy và cơ cấu sản phẩm vẫn tạo khác biệt.

## HBM: kinh tế của bộ nhớ trở nên khác biệt hơn

**HBM (High Bandwidth Memory / 고대역폭메모리)** xếp chồng nhiều die DRAM để cung cấp băng thông rất cao cho bộ tăng tốc AI.

HBM đòi hỏi die chất lượng cao, quy trình xếp chồng và TSV, đóng gói tiên tiến, kiểm soát nhiệt, chứng nhận của khách hàng và tỷ lệ đạt chất lượng cao trên nhiều lớp.

Nếu một stack có nhiều die, lỗi tại một lớp có thể làm cả cụm không sử dụng được. Vì vậy bài toán **tỷ lệ đạt (yield / 수율)** phức tạp hơn DRAM đơn lẻ.

Sự bùng nổ AI không chỉ tăng lượng bit; nó còn làm tăng giá trị của **năng lực đóng gói + yield + chứng nhận khách hàng**.

## Yield: kỹ thuật chuyển thành biên lợi nhuận như thế nào?

Yield là tỷ lệ sản phẩm đạt chuẩn so với lượng đầu ra lý thuyết.

Nếu chi phí wafer gần như cố định:

\[
Chi\ phí\ trên\ die\ tốt
\approx
\frac{Chi\ phí\ wafer + Chi\ phí\ quy\ trình}{Số\ die\ đạt\ chuẩn}
\]

Yield tăng từ 70% lên 90% không chỉ làm số sản phẩm bán được tăng; nó còn phân bổ cùng chi phí fab trên nhiều chip hơn.

Với quy mô fab hiện đại, vài điểm phần trăm yield có thể tạo ảnh hưởng tài chính rất lớn. Đây là ví dụ rõ của việc kỹ thuật biến thành kế toán.

## Cường độ vốn: fab là cỗ máy chi phí cố định rất lớn

Fab cần phòng sạch, quang khắc, thiết bị khắc–lắng đọng, điện nước và đội ngũ kỹ sư. Khấu hao là một khoản chi phí lớn.

Một cách hình dung:

\[
Chi\ phí\ cố\ định\ trên\ đơn\ vị
=
\frac{Tổng\ chi\ phí\ cố\ định\ fab}{Sản\ phẩm\ đạt\ chuẩn\ giao\ bán}
\]

Khi **tỷ lệ sử dụng công suất (utilization / 가동률)** thấp, chi phí trên đơn vị tăng. Khi utilization cao, **đòn bẩy hoạt động (operating leverage)** mạnh.

Vì vậy cùng một ASP vẫn có thể tạo biên lợi nhuận rất khác tùy utilization và yield.

## Độ trễ công suất tạo ra chu kỳ

Fab không thể tăng công suất trong vài tuần. Xây fab, lắp thiết bị, chứng nhận quy trình và tăng yield cần nhiều thời gian.

Đây là **độ trễ nguồn cung (supply lag)**.

Khi nhu cầu mạnh, giá tăng trước khi công suất mới đi vào hoạt động. Doanh nghiệp nhìn thấy lợi nhuận cao và đầu tư; nhưng tới khi công suất mới xuất hiện, nhu cầu có thể đã chậm lại.

Cường độ vốn lớn + độ trễ dài là nguồn gốc cấu trúc của tính chu kỳ.

## CAPEX lớn không tự động là tín hiệu tích cực

CAPEX có thể gồm **đầu tư duy trì/chuyển thế hệ công nghệ** và **đầu tư tăng trưởng**.

CAPEX lớn có thể phản ánh niềm tin vào tương lai, nhưng cũng có thể tạo dư cung sau này. Tạo giá trị chỉ xảy ra khi:

\[
Lợi\ suất\ công\ suất\ mới > Chi\ phí\ vốn
\]

Không thể suy luận `CAPEX tăng = giá trị tăng`.

## Thời điểm khấu hao và lợi nhuận

Chi tiền xây fab xảy ra trước; khấu hao chỉ bắt đầu khi tài sản được đưa vào sử dụng. Vì vậy dòng tiền ra có thể xuất hiện trước, còn gánh nặng khấu hao tăng sau khi fab bắt đầu ramp.

Nếu nhu cầu yếu đúng lúc công suất mới bắt đầu khấu hao, doanh nghiệp chịu hai lực cùng lúc:

```text
ASP / utilization ↓
+
Khấu hao ↑
```

Đây là lý do thời điểm dòng tiền và lợi nhuận kế toán khác nhau.

## Kinh tế foundry: dịch vụ sản xuất nhưng hào cạnh tranh rất sâu

Foundry sản xuất chip theo thiết kế của khách hàng. Các biến cốt lõi gồm khả năng cạnh tranh của node công nghệ, yield, utilization, lòng tin của khách hàng, hệ sinh thái thiết kế, đóng gói và tốc độ đưa sản phẩm vào sản lượng lớn.

Khách hàng không chỉ mua mật độ transistor. Họ cần **PDK (Process Design Kit)**, thư viện IP, khả năng tương thích EDA, quy trình tăng yield đáng tin cậy và hỗ trợ đóng gói.

Chuyển foundry có chi phí lớn vì thiết kế phải được điều chỉnh và chứng nhận lại. Đây tạo **chi phí chuyển đổi (switching cost)**.

Node nhỏ hơn không tự động tốt hơn; chi phí, điện năng, hiệu năng và yield phải phù hợp use case.

## Kinh tế fabless: nhẹ tài sản hơn nhưng phụ thuộc kiểu khác

Fabless tránh CAPEX fab khổng lồ nhưng chi rất mạnh cho R&D và thiết kế.

Rủi ro chính gồm quyền tiếp cận công suất foundry, chi phí tape-out, thất bại thiết kế, tập trung khách hàng và sản phẩm nhanh lỗi thời.

Một design win lớn có thể tạo biên lợi nhuận cao; bỏ lỡ một thế hệ kiến trúc có thể làm tăng trưởng suy sụp.

Vì vậy năng lực R&D và quan hệ hệ sinh thái quan trọng hơn utilization vật lý.

## Đóng gói tiên tiến làm mờ ranh giới front-end và back-end

Trong lịch sử, đóng gói và kiểm thử thường bị coi là khâu giá trị thấp hơn. AI, HBM và chiplet làm **đóng gói tiên tiến (advanced packaging)** trở thành một nút thắt hiệu năng.

Khi nhiều die phải giao tiếp ở băng thông cao, interposer, substrate và thiết kế nhiệt ảnh hưởng trực tiếp tới hiệu năng hệ thống.

Điều này làm giá trị dịch chuyển trong chuỗi cung ứng. Một nút từng bị coi là “giá trị thấp” có thể trở thành nút chiến lược khi kiến trúc công nghệ thay đổi.

## Thiết bị bán dẫn: “bán cuốc xẻng” nhưng vẫn có chu kỳ

Doanh thu thiết bị phụ thuộc lịch CAPEX của fab nhiều hơn ASP chip trực tiếp.

Đơn hàng thiết bị có thể đi trước công suất chip thực tế. Doanh nghiệp thiết bị thường có R&D cao, rào cản chứng nhận lớn, doanh thu dịch vụ từ installed base, tập trung khách hàng và rủi ro kiểm soát xuất khẩu.

Mô hình “picks-and-shovels” không có nghĩa miễn nhiễm chu kỳ. Nếu fab cắt CAPEX, đơn hàng thiết bị mới có thể giảm mạnh.

## Vật liệu và hóa chất: nhu cầu lặp lại nhưng hào chứng nhận cao

Khí, photoresist, wafer và hóa chất đặc biệt được tiêu thụ liên tục. So với thiết bị, doanh thu có thể lặp lại hơn khi fab vận hành.

Tuy nhiên chứng nhận rất nghiêm ngặt vì một lượng tạp chất nhỏ cũng có thể làm yield giảm. Hào cạnh tranh có thể đến từ độ tinh khiết, độ ổn định, logistics và quá trình chứng nhận của khách hàng, không chỉ bằng sáng chế.

Tập trung khách hàng vẫn là rủi ro vì chỉ vài fab lớn đã chiếm phần lớn nhu cầu.

## Tồn kho: phải nhìn cả nhà sản xuất và khách hàng

Giá bộ nhớ phục hồi có thể đến từ nhu cầu cuối thật hoặc chỉ từ tái tích trữ tạm thời.

Cần tách:

```text
Nhu cầu cuối
Tồn kho khách hàng
Tồn kho nhà sản xuất
Tồn kho kênh phân phối
```

Nếu khách hàng tái tích trữ sau khi tồn kho xuống rất thấp, đơn hàng có thể tạm thời tăng nhanh hơn tiêu dùng cuối. Ngoại suy giai đoạn này thành tăng trưởng cấu trúc rất dễ gây sai lầm chu kỳ.

## Tăng bit, ASP và cơ cấu sản phẩm

Doanh thu bộ nhớ có thể phân rã gần đúng:

\[
Doanh\ thu \approx Bit\ giao\ bán \times ASP\ trên\ bit
\]

Nhưng HBM và cơ cấu sản phẩm cao cấp làm ASP bình quân phức tạp hơn.

Doanh thu có thể tăng do số bit tăng, giá thị trường tăng, tỷ trọng HBM cao hơn hoặc tỷ giá. Tác động tới biên lợi nhuận khác nhau theo từng nguyên nhân.

## Tập trung khách hàng: AI tạo tăng trưởng nhưng cũng tạo phụ thuộc mới

Khách hàng HBM cao cấp ít hơn người mua bộ nhớ phổ thông. Thắng khách hàng hyperscaler hoặc hãng accelerator lớn tạo tăng trưởng rất nhanh nhưng cũng làm mức tập trung khách hàng và yêu cầu chứng nhận cao hơn.

Quyền lực khách hàng có thể ảnh hưởng giá, lịch CAPEX và roadmap công nghệ. Tăng trưởng cấu trúc của AI không xóa rủi ro thương lượng.

## Địa chính trị chuỗi cung ứng: bán dẫn là hạ tầng chiến lược

Chip tiên tiến phụ thuộc thiết bị, EDA, IP và vật liệu phân bố toàn cầu. Không quốc gia nào nắm toàn bộ nút quan trọng.

Kiểm soát xuất khẩu và hạn chế công nghệ có thể tác động quyền tiếp cận thiết bị, thị trường khách hàng, vị trí fab, hoạt động tại Trung Quốc và hợp tác R&D.

**Tự cung tự cấp 100%** thường không thực tế và có thể không hiệu quả. Khả năng chống chịu tốt hơn là giảm điểm phụ thuộc đơn lẻ quan trọng và duy trì phương án thay thế đáng tin cậy.

Địa chính trị vì vậy đã trở thành biến dòng tiền doanh nghiệp, không chỉ là bối cảnh chính sách đối ngoại.

## Kinh tế vị trí: vì sao fab tập trung theo cụm?

Fab cần điện ổn định, nước siêu tinh khiết, nhà cung cấp, nhân lực kỹ thuật và logistics. Cụm công nghiệp giảm thời gian phối hợp và tăng mật độ nhân lực–nhà cung cấp.

Nhưng tập trung cũng tạo **rủi ro chung (common-mode risk)**: sự cố điện, nước hoặc thiên tai địa phương có thể ảnh hưởng nhiều cơ sở cùng lúc.

Địa lý công nghiệp vì vậy là đánh đổi giữa hiệu quả tập trung và khả năng chống chịu.

Xem [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md) và [`30_energy_security_power_market_and_transition.md`](./30_energy_security_power_market_and_transition.md).

## Điện tử thành phẩm có kinh tế khác chip

Smartphone, TV và thiết bị gia dụng phụ thuộc BOM, tồn kho kênh, marketing, chu kỳ sản phẩm và sức mạnh thương hiệu.

Thương hiệu cao cấp tạo quyền định giá nhưng chu kỳ thay thế sản phẩm có thể giới hạn tăng trưởng số lượng. Biên phần cứng có thể vừa phải trong khi dịch vụ và phụ kiện làm giá trị vòng đời khách hàng cao hơn.

Vì vậy Samsung Electronics không thể được phân tích như “một công ty bán dẫn” duy nhất; cơ cấu phân khúc rất quan trọng.

## Màn hình: vị trí dẫn đầu công nghệ có thể dịch chuyển

Hàn Quốc từng dẫn đầu LCD nhưng hàng hóa hóa và quy mô Trung Quốc làm kinh tế thay đổi. Doanh nghiệp Hàn Quốc chuyển trọng tâm sang OLED và công nghệ màn hình cao cấp.

Ngành màn hình có nhiều đặc điểm giống bán dẫn: CAPEX cao, học yield, chứng nhận khách hàng, thế hệ công nghệ và rủi ro dư công suất.

Một công nghệ có thể vượt trội về kỹ thuật nhưng thất bại về kinh tế nếu yield, chi phí hoặc mức chấp nhận của khách hàng thấp.

## OLED: khác biệt hóa đi cùng rủi ro công suất

OLED có thể tạo rào cản cao hơn nhờ vật liệu, quy trình và nhu cầu thiết bị cao cấp. Nhưng dây chuyền thế hệ mới vẫn cần đạt utilization đủ cao.

Nếu chu kỳ sản phẩm khách hàng yếu, dây chuyền đắt tiền có thể bị sử dụng thấp. Dẫn đầu công nghệ không xóa kinh tế công suất.

## Hệ sinh thái nhà cung cấp: năng lực lan ra ngoài Samsung/SK/LG

Các doanh nghiệp bán dẫn và điện tử lớn dựa vào nhiều nhà cung cấp thiết bị, vật liệu và linh kiện. Điều này tạo lan tỏa: nhà cung cấp học tiêu chuẩn chất lượng toàn cầu và có thể xuất khẩu sang khách hàng ngoài tập đoàn.

Nhưng phụ thuộc captive cũng có thể xuất hiện. Nhà cung cấp có công nghệ tốt nhưng chỉ một khách hàng lớn vẫn có quyền thương lượng yếu.

Vì vậy thành công bán dẫn có thể lan tỏa năng suất hoặc làm năng suất tập trung tùy khả năng scale-up của nhà cung cấp.

Xem [`06_sme_mid_sized_and_subcontracting_ecosystem.md`](./06_sme_mid_sized_and_subcontracting_ecosystem.md).

## R&D và nhân tài: tri thức quy trình mang tính tích lũy

Biên công nghệ bán dẫn di chuyển liên tục nên R&D không chỉ là chi tiêu tăng trưởng; phần lớn còn là **đầu tư để tồn tại (survival investment)**.

Nhiều kỹ năng là kiến thức ngầm. Kỹ sư quy trình lâu năm có thể hiểu những tương tác tinh tế không ghi đầy đủ trong tài liệu.

Vì vậy giữ nhân lực và chiều sâu cụm công nghiệp là tài sản chiến lược.

Xem [`29_innovation_rnd_education_and_human_capital.md`](./29_innovation_rnd_education_and_human_capital.md).

## Bảng chỉ số khi phân tích công ty

Với doanh nghiệp bộ nhớ/IDM, nên theo dõi ASP, tăng bit, cơ cấu HBM/cao cấp, tồn kho, utilization, bình luận yield, CAPEX, khấu hao, R&D và tiền ròng/nợ ròng.

Với foundry, nên theo dõi cơ cấu node, utilization, yield/ramp, tập trung khách hàng, CAPEX và hệ sinh thái đóng gói tiên tiến.

Với doanh nghiệp thiết bị/vật liệu, nên theo dõi tập trung khách hàng, backlog, installed base, tỷ trọng dịch vụ–vật tư tiêu hao, các lần đạt chứng nhận và rủi ro kiểm soát xuất khẩu.

Không chỉ số nào nên được đọc một mình.

## Chuẩn hóa chu kỳ khi định giá

Ở đỉnh giá bộ nhớ, P/E quá khứ có thể rất thấp. Ở đáy chu kỳ, P/E có thể rất cao hoặc vô nghĩa.

Vì vậy định giá bán dẫn cần giả định **chu kỳ bình thường hóa (normalized cycle)**.

Nên hỏi ASP giữa chu kỳ là bao nhiêu, utilization bền vững ở mức nào, khấu hao sau fab mới sẽ ra sao và tỷ trọng sản phẩm cao cấp nào thực sự mang tính cấu trúc.

Cách này hữu ích hơn so sánh cơ học P/E một năm.

## Stress test

Các cú sốc hữu ích gồm ASP bộ nhớ -20%, chậm chứng nhận HBM, utilization -10 điểm phần trăm, fab mới bắt đầu khấu hao trước khi nhu cầu đến, hạn chế xuất khẩu, khách hàng lớn mất thị phần, biến động KRW và giá điện tăng.

Sau đó theo dõi tác động tới biên lợi nhuận hoạt động, FCF và phản ứng CAPEX.

## Mental Model — mô hình tư duy

> Bán dẫn là cuộc chơi của **công nghệ + yield + công suất + cơ cấu sản phẩm + chu kỳ + hệ sinh thái**. Lợi thế của Hàn Quốc không nằm ở một nhà máy đơn lẻ mà ở hệ thống sản xuất–kỹ thuật tích lũy qua nhiều thập niên.

```text
R&D / Quy trình
      ↓
Yield + năng lực sản phẩm
      ↓
Chứng nhận khách hàng
      ↓
Sản lượng / ASP / cơ cấu
      ↓
Dòng tiền
      ↓
CAPEX thế hệ tiếp theo
      ↓
Vòng học lặp lại
```

## Những nhầm lẫn thường gặp

**“AI boom làm bộ nhớ hết chu kỳ.”** Sai. Nhu cầu cấu trúc tăng nhưng phản ứng cung và CAPEX vẫn tạo chu kỳ.

**“CAPEX lớn là tích cực.”** Không nếu lợi suất tương lai thấp hoặc gây dư cung.

**“Node nhỏ hơn luôn tốt hơn.”** Không; yield, chi phí, PPA và use case đều quan trọng.

**“Công ty bán dẫn nào cũng hưởng AI như nhau.”** Sai. Vị trí trong chuỗi giá trị khác nhau.

**“Tự cung tự cấp 100% là chống chịu tối ưu.”** Không nhất thiết. Đa dạng hóa và phương án thay thế đáng tin cậy thường hiệu quả hơn.

**“Doanh thu tăng nghĩa vị trí công nghệ dẫn đầu hơn.”** Không; ASP, FX và chu kỳ có thể giải thích tăng trưởng.

## Liên kết

Đọc cùng [`02_trade_export_and_global_value_chains.md`](./02_trade_export_and_global_value_chains.md), [`06_sme_mid_sized_and_subcontracting_ecosystem.md`](./06_sme_mid_sized_and_subcontracting_ecosystem.md), [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md), [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md), [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md), [`29_innovation_rnd_education_and_human_capital.md`](./29_innovation_rnd_education_and_human_capital.md) và [`30_energy_security_power_market_and_transition.md`](./30_energy_security_power_market_and_transition.md).
