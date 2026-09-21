# Hóa học khí quyển — khí phản ứng, gốc tự do và tác động bức xạ

> Khí quyển có thể được xem như **một lò phản ứng hóa học được ánh sáng Mặt Trời dẫn động và đồng thời bị vận chuyển bởi chất lưu**. Nitrogen và oxygen chiếm phần lớn không khí, nhưng các chất vết ở mức ppm–ppt vẫn có thể chi phối ozone, khói quang hóa, aerosol và cân bằng bức xạ vì ảnh hưởng hóa học phụ thuộc độ phản ứng, thời gian sống và khả năng hấp thụ bức xạ chứ không chỉ phụ thuộc nồng độ.

Hóa học khí quyển ghép nhiều nền tảng đã học trước:

- [chất khí](../03_matter_and_phases/00_gases.md) để hiểu áp suất riêng phần, vận chuyển và va chạm;
- [bức xạ điện từ và lượng tử hóa](../01_atomic_structure/01_electromagnetic_radiation_and_quantization.md) cùng [phổ học](../12_analytical_chemistry/03_spectroscopy.md) để hiểu quang phân và hấp thụ bức xạ;
- [động học phản ứng](../06_chemical_kinetics/00_reaction_rates.md) và [cơ chế phản ứng](../06_chemical_kinetics/02_reaction_mechanisms.md) để hiểu chuỗi gốc tự do;
- [cân bằng động](../07_chemical_equilibrium/00_dynamic_equilibrium.md) để phân biệt cân bằng với trạng thái ổn định;
- [hóa học bề mặt và mặt phân cách](../14_materials_and_polymer_chemistry/05_surface_and_interface_chemistry.md) để hiểu phản ứng dị thể trên hạt và giọt.

## Cấu trúc khí quyển quyết định môi trường phản ứng

**Tầng đối lưu (troposphere)** chứa phần lớn khối lượng khí quyển, là nơi diễn ra thời tiết và phần lớn tiếp xúc của con người với ô nhiễm không khí. Nhiệt độ nhìn chung giảm theo độ cao vì bề mặt Trái Đất là nguồn nung nóng chính của tầng này.

**Tầng bình lưu (stratosphere)** nằm phía trên và chứa lớp ozone. Trong một phần lớn tầng bình lưu, nhiệt độ tăng theo độ cao vì ozone hấp thụ tia tử ngoại và chuyển năng lượng photon thành nhiệt.

Sự khác biệt nhiệt này ảnh hưởng trộn thẳng đứng, thời gian lưu và cơ chế phản ứng. Cao hơn nữa, mật độ khí giảm mạnh và hóa học ion cùng bức xạ năng lượng cao trở nên quan trọng hơn.

## Quang phân — ánh sáng là một tác nhân hóa học

Một phân tử có thể hấp thụ photon rồi bị phá vỡ hoặc tái sắp xếp:

\[
A+h\nu\rightarrow\text{sản phẩm}
\]

Tốc độ **quang phân (photolysis)** phụ thuộc phổ ánh sáng, tiết diện hấp thụ, hiệu suất lượng tử, độ cao, mây và góc chiếu sáng.

Một hệ số quang phân có thể viết về mặt khái niệm:

\[
J=\int\sigma(\lambda)\Phi(\lambda)I(\lambda)\,d\lambda
\]

trong đó:

- `σ(λ)` là tiết diện hấp thụ;
- `Φ(λ)` là hiệu suất lượng tử;
- `I(λ)` là thông lượng photon.

Điều này nối trực tiếp hóa học khí quyển với phổ học: không phải mọi photon đều có khả năng kích hoạt cùng một phân tử, và không phải mọi photon đã hấp thụ đều cho cùng sản phẩm.

## Gốc tự do — nồng độ nhỏ nhưng thông lượng phản ứng lớn

Gốc tự do chứa electron độc thân nên thường phản ứng nhanh.

Gốc hydroxyl `OH·` thường được gọi là “chất tẩy rửa của khí quyển” vì nó khởi động oxy hóa CO, methane và nhiều **hợp chất hữu cơ dễ bay hơi (volatile organic compounds, VOCs)**.

Nồng độ `OH·` rất thấp nhưng nó có thể được tái sinh qua nhiều bước lan truyền chuỗi. Vì vậy mức độ quan trọng của một chất không thể suy chỉ từ nồng độ tức thời.

Đây là cùng logic với chất xúc tác: một tiểu phân có thể có nồng độ nhỏ nhưng thông lượng qua nó rất lớn.

## Một nguồn OH quan trọng

Ozone hấp thụ UV:

\[
O_3+h\nu\rightarrow O_2+O(^1D)
\]

Oxygen kích thích sau đó phản ứng với hơi nước:

\[
O(^1D)+H_2O\rightarrow2OH
\]

Chuỗi này nối cường độ ánh sáng, ozone, độ ẩm và khả năng oxy hóa của khí quyển.

## Ozone tầng đối lưu — chất ô nhiễm thứ cấp

Ozone gần mặt đất phần lớn không được phát thải trực tiếp. Nó được tạo qua mạng `NOx–VOC–ánh sáng`.

Chu trình cơ bản:

\[
NO_2+h\nu\rightarrow NO+O
\]

\[
O+O_2+M\rightarrow O_3+M
\]

\[
O_3+NO\rightarrow NO_2+O_2
\]

Nếu chỉ có chu trình này, ozone khó tích lũy mạnh vì phản ứng cuối tiêu thụ ozone gần như bù cho quá trình tạo.

## Vì sao VOC làm ozone tích lũy?

`OH·` oxy hóa VOC và tạo các gốc peroxy như `RO2·` và `HO2·`.

Các gốc này có thể chuyển NO thành `NO2` mà không tiêu thụ ozone:

\[
RO_2+NO\rightarrow RO+NO_2
\]

`NO2` mới lại quang phân và tạo ozone.

Vì vậy VOC mở một con đường chuyển `NO → NO2` không cần dùng `O3`, cho phép ozone tích lũy.

## Hóa học NOx–VOC là phi tuyến

Lượng ozone không thay đổi tuyến tính đơn giản theo lượng tiền chất.

Ở vùng `NOx` thấp, thêm `NOx` có thể làm tốc độ tạo ozone tăng. Ở vùng `NOx` rất cao, phản ứng kết thúc gốc tự do và phản ứng `NO + O3` có thể làm ozone cục bộ giảm.

Do đó có thể phân biệt các chế độ:

- **giới hạn NOx (NOx-limited)**;
- **giới hạn VOC (VOC-limited)**.

Đây là ví dụ quan trọng cho thấy một mạng phản ứng không thể được điều khiển tốt bằng quy tắc tuyến tính kiểu “giảm tiền chất 20% thì sản phẩm giảm 20%”.

## Lan truyền và kết thúc chuỗi gốc tự do

Một chuỗi gốc tự do có ba vai trò khái niệm:

```text
khởi tạo
→ lan truyền
→ kết thúc
```

Trong bước lan truyền, gốc được tái sinh và chuỗi tiếp tục.

Trong bước kết thúc, gốc bị loại khỏi mạng, ví dụ:

\[
OH+NO_2+M\rightarrow HNO_3+M
\]

Tốc độ tạo ozone và sản phẩm oxy hóa phụ thuộc cạnh tranh giữa **lan truyền chuỗi (chain propagation)** và **kết thúc chuỗi (chain termination)**.

Đây chính là ứng dụng thực của tư duy cơ chế đã học trong động học hóa học.

## Oxy hóa VOC và aerosol hữu cơ thứ cấp

`OH·` có thể chuyển VOC thành carbonyl, nitrate hữu cơ và các sản phẩm oxy hóa có độ bay hơi thấp hơn.

Một phần sản phẩm sau đó ngưng tụ vào pha hạt và tạo **aerosol hữu cơ thứ cấp (secondary organic aerosol, SOA)**.

Chuỗi biến đổi là:

```text
VOC pha khí
→ oxy hóa nhiều bước
→ độ bay hơi giảm
→ phân bố khí–hạt
→ aerosol hữu cơ thứ cấp
```

Do đó hóa học pha khí và nhiệt động phân bố pha phải được xét cùng nhau.

## Aerosol — pha hạt trong khí quyển

**Aerosol** là tập hợp hạt rắn hoặc lỏng lơ lửng trong không khí.

Nguồn có thể là:

- sơ cấp: bụi, muội than, muối biển;
- thứ cấp: sulfate, nitrate, ammonium và hữu cơ tạo từ khí tiền chất.

`SO2` có thể bị oxy hóa thành sulfuric acid/sulfate; `NOx` tạo nitric acid/nitrate; `NH3` trung hòa acid để tạo muối ammonium.

Thành phần hạt phụ thuộc nhiệt độ, độ ẩm, hoạt độ nước và cân bằng khí–hạt.

## Kích thước hạt quyết định hành vi

Kích thước ảnh hưởng:

- nơi lắng đọng trong hệ hô hấp;
- thời gian tồn tại trong khí quyển;
- tán xạ và hấp thụ ánh sáng;
- khả năng tạo mầm mây;
- diện tích bề mặt cho phản ứng dị thể.

Hạt siêu mịn có diện tích bề mặt rất lớn trên mỗi đơn vị khối lượng nhưng cũng có thể kết tụ hoặc lớn dần nhanh.

## Hóa học dị thể và đa pha

Phản ứng khí quyển không chỉ xảy ra trong pha khí. Chúng còn diễn ra:

- trên bề mặt hạt;
- trong giọt mây;
- trong nước aerosol;
- tại vùng khí–lỏng hoặc khí–rắn.

Một chất khí đi vào giọt nước có thể proton hóa, ion hóa hoặc tham gia phản ứng hoàn toàn khác pha khí khô.

Trong tầng bình lưu, mây tầng bình lưu cực cung cấp bề mặt cho các phản ứng chuyển chlorine dự trữ thành dạng dễ quang phân.

Khí quyển vì vậy là **hệ phản ứng đa pha**, không phải chỉ một hỗn hợp khí.

## Ozone tầng bình lưu — bộ lọc UV

Chu trình Chapman đơn giản gồm:

\[
O_2+h\nu\rightarrow2O
\]

\[
O+O_2+M\rightarrow O_3+M
\]

\[
O_3+h\nu\rightarrow O_2+O
\]

\[
O+O_3\rightarrow2O_2
\]

Chu trình này hấp thụ một phần UV năng lượng cao và giảm lượng bức xạ tới bề mặt Trái Đất.

## Phá hủy ozone theo cơ chế xúc tác

Một gốc tự do có thể phá nhiều phân tử ozone nếu được tái sinh.

Ví dụ chlorine:

\[
Cl+O_3\rightarrow ClO+O_2
\]

\[
ClO+O\rightarrow Cl+O_2
\]

Phản ứng ròng:

\[
O_3+O\rightarrow2O_2
\]

`Cl` được tái sinh nên một lượng nhỏ chlorine hoạt tính vẫn có thể có tác động lớn.

Đây là ví dụ môi trường điển hình của xúc tác: chất xúc tác thay đổi tốc độ/con đường nhưng không bị tiêu thụ theo hệ số phản ứng tổng.

## Chất dự trữ và hoạt hóa chlorine

Chlorine có thể tồn tại trong dạng ít phản ứng hơn như `HCl` hoặc `ClONO2`.

Phản ứng trên mây tầng bình lưu cực có thể chuyển chúng thành dạng như `Cl2` dễ quang phân hơn.

Khi ánh sáng trở lại sau mùa đông vùng cực, quang phân giải phóng `Cl·` và làm chu trình phá ozone tăng nhanh.

Nhiệt độ, pha vật chất và chu kỳ chiếu sáng vì vậy ghép trực tiếp vào mạng phản ứng.

## Hiệu ứng nhà kính — phổ học ở quy mô hành tinh

Trái Đất hấp thụ phần lớn bức xạ Mặt Trời bước sóng ngắn và phát bức xạ hồng ngoại theo nhiệt độ của mình.

Các phân tử như `H2O`, `CO2`, `CH4`, `N2O` và `O3` hấp thụ hồng ngoại ở các vùng dao động–quay nhất định.

Sự hấp thụ/phát xạ làm thay đổi độ cao hiệu dụng mà từ đó bức xạ thoát ra không gian, qua đó ảnh hưởng cân bằng năng lượng hành tinh.

Hiệu ứng nhà kính không phải “nhiệt bị nhốt dưới mái kính”; cơ chế là **truyền bức xạ phụ thuộc bước sóng, độ cao và cấu trúc nhiệt khí quyển**.

### Vì sao N2 và O2 là khí nhà kính yếu?

`N2` và `O2` là phân tử hai nguyên tử đồng hạt nhân, nên các dao động cơ bản không tạo thay đổi mômen lưỡng cực mạnh theo cách cần cho hấp thụ IR thông thường.

`CO2` và `H2O` có các dao động IR hoạt tính mạnh hơn.

Đây là liên hệ trực tiếp giữa **quy tắc chọn phổ học** và khí hậu.

## Tác động bức xạ và thời gian sống

Ảnh hưởng khí hậu của một chất phụ thuộc:

- cường độ và vị trí dải hấp thụ;
- nồng độ;
- thời gian sống;
- phân bố theo độ cao;
- phản ứng hóa học gián tiếp;
- tương tác với mây/aerosol.

Methane có nồng độ thấp hơn `CO2` nhưng có dải hấp thụ mạnh và còn tham gia hóa học ảnh hưởng ozone và hơi nước.

## Thời gian lưu và mô hình hộp

Một mô hình đơn giản:

\[
\tau\approx\frac{\text{lượng tồn trữ}}{\text{tốc độ mất}}
\]

Nếu nguồn là `E` và mất mát bậc nhất có hằng số `k`:

\[
\frac{dC}{dt}=E-kC
\]

Ở **trạng thái ổn định (steady state)**:

\[
C_{ss}=\frac{E}{k}
\]

Điểm quan trọng: đây không phải cân bằng nhiệt động. Nguồn và mất mát vẫn tiếp tục, chỉ có tốc độ gần bằng nhau nên `C` gần ổn định.

Xem lại [cân bằng động và steady state](../07_chemical_equilibrium/00_dynamic_equilibrium.md).

## Lắng đọng acid

`SO2` có thể bị oxy hóa thành sulfuric acid/sulfate, còn `NOx` thành nitric acid/nitrate.

Các acid hòa vào mây/mưa hoặc lắng đọng trực tiếp dưới dạng khí/hạt, góp phần acid hóa đất, nước và ăn mòn vật liệu.

`NH3`, bụi khoáng và độ kiềm có thể trung hòa một phần acid. Vì vậy pH mưa không chỉ phụ thuộc lượng acid tạo ra mà còn phụ thuộc khả năng đệm/base của hệ.

## Aerosol và khí hậu

Hạt có thể tán xạ hoặc hấp thụ bức xạ.

Aerosol sulfate thường tán xạ mạnh; carbon đen hấp thụ mạnh.

Hạt còn có thể làm nhân ngưng tụ mây, thay đổi số giọt, kích thước giọt và thời gian sống của mây.

Ảnh hưởng ròng vì vậy phụ thuộc kích thước, thành phần, trạng thái trộn, độ cao và độ ẩm.

## Hóa học cạnh tranh với vận chuyển

Nếu thời gian sống hóa học ngắn hơn nhiều thời gian vận chuyển, chất chủ yếu tác động cục bộ. Nếu sống lâu, nó có thể được vận chuyển khu vực hoặc toàn cầu.

**Số Damköhler (Damköhler number)** là một cách so sánh thang thời gian phản ứng với thang vận chuyển.

```text
phản ứng nhanh hơn vận chuyển
→ hóa học cục bộ chi phối

vận chuyển nhanh hơn phản ứng
→ chất có thể đi xa trước khi biến đổi
```

Đây là bridge giữa kinetics và fluid transport.

## Hóa học không khí trong nhà

Không khí trong nhà thường có UV thấp hơn, tỷ lệ diện tích bề mặt/thể tích cao hơn và chịu ảnh hưởng mạnh của vật liệu xây dựng, chất tẩy rửa, con người và thông gió.

Ozone đi vào nhà có thể phản ứng với hợp chất không no trên bề mặt hoặc dầu trên da, tạo sản phẩm oxy hóa thứ cấp.

Hình học không gian vì vậy làm hóa học bề mặt trở nên quan trọng hơn so với nhiều môi trường ngoài trời.

## Đo thành phần khí quyển

Thành phần không khí được đo bằng:

- máy phân tích khí;
- sắc ký;
- phổ khối;
- hấp thụ quang học;
- viễn thám.

Vì nhiều chất ở mức ppb hoặc ppt, hiệu chuẩn, nhiễu, hấp phụ lên đường ống và biến đổi trong hệ lấy mẫu có thể chi phối sai số.

Đối với chất rất phản ứng, **hệ lấy mẫu có thể thay đổi chính mẫu cần đo**.

## Ví dụ suy luận: vì sao giảm NOx đôi khi chưa làm ozone giảm ngay theo cùng tỉ lệ?

Trong chế độ VOC-limited, lượng NOx cao có thể vừa hỗ trợ tạo ozone vừa làm tăng các đường kết thúc gốc hoặc tiêu thụ ozone trực tiếp.

Giảm NOx làm mạng phản ứng chuyển sang chế độ mới; đáp ứng vì vậy phi tuyến.

Cần biết **chế độ hóa học**, không chỉ biết tổng phát thải.

## Ví dụ suy luận: vì sao một chất nồng độ rất thấp vẫn có thể chi phối mạng phản ứng?

Nếu chất đó được tái sinh sau mỗi chu kỳ, một phân tử có thể tham gia nhiều sự kiện phản ứng trước khi bị loại.

Gốc `OH·` và chlorine hoạt tính là ví dụ. Nồng độ tức thời thấp nhưng **turnover** cao làm thông lượng hóa học lớn.

Đây là cùng nguyên lý với chất xúc tác trong hóa học thông thường.

## Những hiểu lầm thường gặp

### “Ozone hoặc tốt hoặc xấu”

Vai trò phụ thuộc vị trí. Ozone tầng bình lưu bảo vệ khỏi UV; ozone tầng đối lưu gây hại sức khỏe/thực vật và cũng góp phần hiệu ứng nhà kính.

### “Ozone mặt đất được xe cộ thải trực tiếp”

Không. Phần lớn là chất ô nhiễm thứ cấp tạo từ NOx, VOC và ánh sáng.

### “Khí có nồng độ cao nhất mới kiểm soát hóa học khí quyển”

Không. Gốc tự do hoặc chất xúc tác ở nồng độ rất thấp vẫn có thể chi phối đường phản ứng.

### “Khí nhà kính giữ nhiệt giống mái kính”

Không. Cơ chế liên quan hấp thụ/phát xạ phụ thuộc bước sóng và truyền bức xạ qua khí quyển.

### “Giảm phát thải luôn cho đáp ứng tuyến tính”

Không. `NOx–VOC`, phân bố khí–hạt và phản hồi hóa học có thể phi tuyến mạnh.

### “Steady state nghĩa là cân bằng”

Không. Trạng thái ổn định vẫn có nguồn và mất mát liên tục; cân bằng nhiệt động không có dòng ròng.

## Mô hình tư duy

Hãy xem khí quyển như **mạng phản ứng quang hóa đang chuyển động trong không gian**:

```text
ánh sáng
→ tạo trạng thái phản ứng / gốc
→ mạng phản ứng pha khí
↔ aerosol / giọt / bề mặt
→ vận chuyển + lắng đọng
→ tác động hóa học và bức xạ
```

Ánh sáng quyết định kênh quang hóa; gốc tự do truyền chuỗi; bề mặt tạo kênh đa pha; vận chuyển cạnh tranh với thời gian sống; phổ học quyết định tương tác với bức xạ.

Xem tiếp: [Hóa học nước](./01_water_chemistry.md).