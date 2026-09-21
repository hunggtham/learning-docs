# Pin, ăn mòn và lưu trữ năng lượng — điện hóa học như một hệ kỹ thuật

> **Pin điện hóa (battery / 전지)** biến năng lượng tự do hóa học thành công điện bằng cách tách quá trình oxy hóa và khử về các điện cực khác nhau. Tuy nhiên một pin thực tế không chỉ gồm hai bán phản ứng. Hiệu năng phụ thuộc đồng thời vào nhiệt động lực học, động học điện cực, vận chuyển ion, chuyển pha, bề mặt phân cách, nhiệt và quá trình suy giảm vật liệu.

## Cell, battery và lưu trữ điện hóa

Một **cell điện hóa (electrochemical cell)** là một đơn vị gồm anode, chất điện ly và cathode. Một **battery** có thể gồm một hoặc nhiều cell được ghép nối tiếp hoặc song song.

Ghép nối tiếp làm tăng điện áp; ghép song song làm tăng dung lượng hoặc khả năng cấp dòng.

Lưu trữ điện hóa khác tụ điện ở chỗ năng lượng chủ yếu được lưu trong trạng thái hóa học và điện tử của vật liệu, thay vì chỉ trong sự phân tách điện tích tĩnh điện. Siêu tụ điện (supercapacitor) nằm ở vùng trung gian giữa các cơ chế này.

## Năng lượng và công suất là hai đại lượng khác nhau

Dung lượng năng lượng mô tả tổng công mà pin có thể cung cấp:

\[
E\approx \int V\,dQ
\]

Công suất mô tả tốc độ cung cấp năng lượng:

\[
P=VI
\]

Một pin có mật độ năng lượng cao chưa chắc có mật độ công suất cao. Điện cực dày có thể chứa nhiều vật liệu hoạt tính hơn nhưng làm đường vận chuyển ion dài hơn, khiến khả năng phóng hoặc sạc ở dòng lớn giảm.

Đây là một đánh đổi trung tâm trong thiết kế cell.

## Dung lượng và trạng thái sạc

Dung lượng lý thuyết xuất phát từ số electron có thể trao đổi trên mỗi mol vật liệu hoạt tính:

\[
Q_{theoretical}=\frac{nF}{M}
\]

Khi biểu diễn dưới dạng điện lượng trên khối lượng cần đổi đơn vị phù hợp.

**Trạng thái sạc (state of charge, SOC / 충전 상태)** là tỉ lệ dung lượng khả dụng còn lại. SOC không được đo trực tiếp bằng một cảm biến duy nhất; hệ thống quản lý pin (battery management system, BMS) thường ước lượng từ điện áp, tích phân dòng điện, nhiệt độ và mô hình của pin.

## Pin lithium-ion như một ví dụ điển hình

Trong pin lithium-ion, \(Li^+\) di chuyển qua lại giữa các cấu trúc vật chủ, còn electron đi qua mạch ngoài.

Một mô hình đơn giản của cell graphite/NMC khi phóng điện:

```text
điện cực âm: Li_xC6 → C6 + xLi+ + xe−
điện cực dương: Li_{1-x}MO2 + xLi+ + xe− → LiMO2
```

Hóa học thực tế phụ thuộc vật liệu cathode, thành phần và trạng thái sạc.

Điểm quan trọng là lithium kim loại không nhất thiết được tạo và hòa tan liên tục trong chế độ lithium-ion xen cài thông thường. Lithium được lưu trong mạng tinh thể của vật liệu vật chủ.

## Xen cài ion

**Xen cài (intercalation / 삽입 반응)** là quá trình ion khách đi vào cấu trúc vật chủ một cách thuận nghịch mà không phá hủy hoàn toàn khung tinh thể.

Graphite có cấu trúc lớp phù hợp cho lithium xen cài. Oxide kim loại chuyển tiếp dạng lớp, spinel và olivine cung cấp các đường khuếch tán và tâm oxy hóa-khử khác nhau.

Điện thế điện cực phụ thuộc thay đổi năng lượng tự do khi thế hóa học của lithium trong vật chủ thay đổi.

## Hóa học cathode và điện áp

Các cặp oxy hóa-khử như \(Co^{3+}/Co^{4+}\), \(Ni^{2+}/Ni^{4+}\) hoặc \(Fe^{2+}/Fe^{3+}\) tạo các vùng điện áp khác nhau.

Điện áp cao hơn có thể tăng mật độ năng lượng:

\[
Energy\approx Voltage\times Capacity
\]

nhưng vận hành ở điện áp cao cũng làm quá trình oxy hóa chất điện ly và suy giảm bề mặt phân cách nghiêm trọng hơn.

## Chất điện ly không phải chất lỏng thụ động

Chất điện ly phải dẫn ion nhưng cản electron. Nó cũng phải đủ bền về điện hóa trong khoảng điện áp làm việc.

Trong pin lithium-ion, chất điện ly carbonate hữu cơ thường không hoàn toàn bền về nhiệt động với graphite. Một phần chất điện ly phân hủy và tạo **lớp liên pha điện ly rắn (solid electrolyte interphase, SEI / 고체전해질계면)**.

SEI là một sản phẩm phân hủy nhưng có thể hữu ích: nếu đủ bền, dẫn ion tốt và chặn electron, nó bảo vệ điện cực khỏi tiếp tục phân hủy chất điện ly.

## Bề mặt phân cách quyết định tuổi thọ

Nhiều cơ chế suy giảm bắt đầu tại vùng tiếp xúc giữa điện cực và chất điện ly. SEI tiếp tục phát triển có thể tiêu thụ lithium khả dụng; lớp liên pha phía cathode hình thành ở điện thế cao; kim loại chuyển tiếp hòa tan có thể nhiễm sang anode; khí có thể sinh ra làm tăng áp suất; hạt vật liệu nứt tạo bề mặt mới; bộ góp dòng có thể bị ăn mòn.

Vì vậy lão hóa pin là bài toán ghép nối giữa hóa học bề mặt, cơ học vật liệu và vận chuyển khối.

## Khả năng làm việc ở dòng cao và khuếch tán

Thang thời gian khuếch tán xấp xỉ:

\[
t\sim \frac{L^2}{D}
\]

với \(L\) là chiều dài khuếch tán và \(D\) là hệ số khuếch tán.

Giảm kích thước hạt giúp rút ngắn đường khuếch tán nhưng lại làm tăng diện tích bề mặt và có thể làm phản ứng phụ mạnh hơn. Một cải tiến về vận chuyển có thể tạo bất lợi về độ bền bề mặt.

## C-rate

**C-rate** chuẩn hóa dòng điện theo dung lượng danh định. 1C về lý thuyết tương ứng phóng hết dung lượng trong khoảng 1 giờ; 2C khoảng 0,5 giờ; C/2 khoảng 2 giờ, nếu pin thực sự cung cấp được dung lượng đó.

Ở C-rate cao, dung lượng sử dụng thường giảm do phân cực và giới hạn vận chuyển.

## Hiệu suất Coulomb và hiệu suất năng lượng

**Hiệu suất Coulomb (Coulombic efficiency)**:

\[
\eta_Q=\frac{Q_{discharge}}{Q_{charge}}
\]

Pin sạc lại cần hiệu suất Coulomb rất cao ở mỗi chu kỳ để duy trì tuổi thọ dài.

Hiệu suất năng lượng thường thấp hơn vì điện áp khi sạc cao hơn điện áp khi phóng do hiện tượng trễ và các tổn thất điện hóa.

## Mạ lithium và sạc nhanh

Nếu \(Li^+\) không thể xen cài vào graphite đủ nhanh khi sạc mạnh, điện thế anode có thể giảm tới mức lithium kim loại bắt đầu bám trên bề mặt. Hiện tượng này gọi là **mạ lithium (lithium plating)**.

Mạ lithium làm mất lithium có thể tuần hoàn và có thể tạo cấu trúc dạng nhánh, làm tăng nguy cơ an toàn. Nhiệt độ thấp, dòng lớn, SOC cao và vận chuyển ion kém đều làm nguy cơ tăng.

Vì vậy sạc nhanh là bài toán động học và vận chuyển, không đơn giản chỉ là dùng bộ sạc có công suất cao hơn.

## Mất kiểm soát nhiệt

Pin chứa năng lượng hóa học và nhiều bề mặt phản ứng. Khi nhiệt độ tăng, phản ứng phụ có thể tăng tốc theo quan hệ Arrhenius, sinh thêm nhiệt rồi tiếp tục làm phản ứng tăng nhanh. Đây là vòng phản hồi dương.

**Mất kiểm soát nhiệt (thermal runaway / 열폭주)** không phải một phản ứng duy nhất mà là chuỗi sự kiện có thể gồm phá hủy SEI, phân hủy chất điện ly, phản ứng điện cực và trong một số hệ là giải phóng oxygen từ cathode.

Thiết kế an toàn sử dụng cơ chế ngắt màng ngăn, ngắt dòng, quản lý nhiệt, khoảng cách giữa cell và thuật toán điều khiển để phá vòng phản hồi này.

## Sodium-ion và các hệ hóa học khác

Pin sodium-ion sử dụng nguyên lý xen cài tương tự nhưng \(Na^+\) lớn hơn \(Li^+\) và hệ vật liệu phù hợp khác nhau. Ưu điểm có thể nằm ở nguồn nguyên liệu và chi phí; hạn chế thường là mật độ năng lượng thấp hơn.

LFP, NMC, LCO, sodium-ion, sulfur, pin trạng thái rắn và pin dòng đều tối ưu cho các ràng buộc khác nhau. Không có một hệ hóa học “tốt nhất” độc lập với ứng dụng.

Lưu trữ lưới điện ưu tiên chi phí, tuổi thọ và an toàn khác với điện thoại hoặc xe điện.

## Pin dòng

Trong **pin dòng oxy hóa-khử (redox-flow battery)**, chất hoạt tính chủ yếu được chứa trong các bồn ngoài và bơm qua bộ điện hóa.

Công suất chủ yếu tăng theo diện tích bộ cell; năng lượng chủ yếu tăng theo thể tích bồn và nồng độ chất hoạt tính. Kiến trúc này tách việc mở rộng năng lượng và công suất rõ hơn pin kín truyền thống.

## Siêu tụ điện và điện dung giả

Tụ điện lớp điện kép lưu điện tích tại bề mặt mà không cần phản ứng oxy hóa-khử trong toàn khối vật liệu. **Điện dung giả (pseudocapacitance)** bổ sung các phản ứng oxy hóa-khử nhanh ở bề mặt hoặc vùng gần bề mặt.

Siêu tụ điện thường có mật độ công suất cao nhưng mật độ năng lượng thấp hơn pin.

## Ăn mòn — một pin ngoài ý muốn

**Ăn mòn (corrosion / 부식)** có thể được xem như một pin điện hóa tự phát hình thành trên vật liệu.

Ví dụ gỉ sắt cần quá trình hòa tan kim loại ở vùng anode:

\[
Fe\rightarrow Fe^{2+}+2e^-
\]

và một phản ứng khử ở vùng cathode, thường là khử oxygen trong nước trung tính có oxygen hòa tan:

\[
O_2+2H_2O+4e^-\rightarrow4OH^-
\]

Các vùng khác nhau trên cùng bề mặt có thể đóng vai trò anode và cathode cục bộ. Nước hoặc chất điện ly tạo đường dẫn ion giữa các vùng đó.

## Ăn mòn Galvani

Khi hai kim loại khác nhau tiếp xúc điện với nhau trong môi trường điện ly, kim loại có điện thế hoạt động hơn có thể bị ăn mòn nhanh hơn.

Mức độ phụ thuộc chênh lệch điện thế, môi trường và đặc biệt là tỉ lệ diện tích. Anode nhỏ ghép với cathode lớn có thể chịu mật độ dòng ăn mòn rất cao và hỏng nhanh.

## Ăn mòn do chênh lệch oxygen

Ngay cả một kim loại duy nhất cũng có thể tạo vi pin nếu nồng độ oxygen khác nhau giữa các vùng. Vùng dưới cặn hoặc trong khe hẹp thường trở thành anode so với bề mặt giàu oxygen.

Đây là lý do ăn mòn cục bộ thường nguy hiểm hơn việc toàn bộ bề mặt mỏng dần đồng đều.

## Thụ động hóa

Một số kim loại tạo màng oxide bảo vệ. Nhôm và thép không gỉ có khả năng chống ăn mòn nhờ **lớp thụ động (passive layer)**.

Tuy nhiên chloride có thể phá màng thụ động tại chỗ và gây **ăn mòn rỗ (pitting corrosion)**. Hình học của hố ăn mòn có thể làm môi trường bên trong acid hơn và tập trung chloride, khiến quá trình tự tăng tốc.

## Bảo vệ chống ăn mòn

Các chiến lược bảo vệ xuất phát trực tiếp từ cơ chế điện hóa: lớp phủ ngăn chất điện ly hoặc oxygen; hợp kim hóa tạo màng thụ động bền hơn; bảo vệ cathode cung cấp electron để cấu trúc cần bảo vệ trở thành cathode; anode hi sinh bị oxy hóa thay cho kim loại chính; chất ức chế làm chậm phản ứng anode hoặc cathode; thiết kế cơ khí tránh khe hẹp và cặp kim loại bất lợi.

## Pin và ăn mòn dùng cùng một khung lý thuyết

Kỹ sư pin muốn phản ứng oxy hóa-khử xảy ra thuận nghịch, có kiểm soát và tạo công hữu ích. Kỹ sư chống ăn mòn muốn ngăn chính những con đường oxy hóa-khử tự phát tương tự xảy ra ở vị trí không mong muốn.

Cả hai lĩnh vực cùng sử dụng phương trình Nernst, động học điện cực, vận chuyển khối, thụ động hóa, khoa học bề mặt và lựa chọn vật liệu.

## Những hiểu lầm thường gặp

### “Điện áp pin là một hằng số cố định”

Không. Điện áp phụ thuộc SOC, dòng điện, nhiệt độ, thành phần và mức phân cực.

### “Sạc nhanh chỉ cần cấp nhiều dòng hơn”

Không. Điện cực phải vận chuyển ion và electron đủ nhanh đồng thời tránh mạ lithium và hư hỏng nhiệt.

### “Ăn mòn chỉ là kim loại gặp oxygen”

Không. Cần có con đường điện hóa và môi trường phù hợp; pH, chloride, ghép Galvani và vi pin cục bộ quyết định tốc độ và hình thái ăn mòn.

### “Pin trạng thái rắn tự động an toàn tuyệt đối”

Không. Chất điện ly rắn có thể giảm một số rủi ro nhưng bề mặt phân cách, xuyên nhánh kim loại, khuyết tật cơ học và điện cực năng lượng cao vẫn cần kiểm soát.

## Mô hình tư duy

Pin là **mạng phản ứng oxy hóa-khử được thiết kế để hoạt động thuận nghịch và hữu ích**; ăn mòn là **mạng oxy hóa-khử tự phát xảy ra ở nơi ta không mong muốn**. Trong cả hai trường hợp, hiệu năng được quyết định bởi nhiệt động lực học, động học, vận chuyển, bề mặt phân cách và cơ học vật liệu.

Xem thêm: [Vật liệu từ liên kết hóa học](../14_materials_and_polymer_chemistry/00_materials_from_chemical_bonding.md).