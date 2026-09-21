# Phản ứng hạt nhân — bảo toàn, giá trị Q, tiết diện và chuyển nguyên tố

> **Phản ứng hạt nhân (nuclear reaction / 핵반응)** là quá trình trong đó hạt nhân trao đổi hạt, năng lượng hoặc thay đổi bản sắc. Khác với phản ứng hóa học thông thường chỉ tái sắp xếp electron, phản ứng hạt nhân có thể biến một nguyên tố thành nguyên tố khác. Các công cụ suy luận cốt lõi là định luật bảo toàn, cân bằng khối lượng–năng lượng, xác suất phản ứng và cấu trúc hạt nhân.

Chapter này nối trực tiếp từ [hạt nhân nguyên tử và năng lượng liên kết](./00_atomic_nucleus.md) và [phóng xạ](./01_radioactivity.md). Nếu phần phương trình tốc độ hoặc mạng phản ứng bị khó, có thể quay lại [động học hóa học](../06_chemical_kinetics/00_reaction_rates.md) và [mạng phản ứng hóa lượng](../04_chemical_quantities/06_stoichiometric_matrices_and_reaction_networks.md). Cùng một tư duy “trạng thái → thông lượng → biến đổi theo thời gian” được dùng lại, chỉ khác thang năng lượng và loại hạt tham gia.

## Ký hiệu tổng quát

Một phản ứng có thể viết:

\[
a+A\rightarrow B+b
\]

hoặc viết gọn:

\[
A(a,b)B
\]

trong đó hạt tới \(a\) tương tác với hạt nhân bia \(A\), tạo hạt nhân dư \(B\) và hạt đi ra \(b\).

## Các định luật bảo toàn

Phản ứng hạt nhân phải thỏa các định luật bảo toàn tương ứng, gồm tổng năng lượng, động lượng tuyến tính, mômen động lượng, điện tích, số baryon/nucleon trong các quá trình hạt nhân năng lượng thấp thông thường và số lepton khi có lepton tham gia.

Cân bằng \(Z\) và \(A\) là bước bắt buộc nhưng chưa đủ. Năng lượng, động lượng và các quy tắc chọn lượng tử vẫn có thể làm một kênh phản ứng bị cấm hoặc có xác suất rất nhỏ.

## Giá trị Q của phản ứng

Năng lượng ròng của phản ứng được mô tả bằng **giá trị Q (Q-value)**:

\[
Q=(m_{initial}-m_{final})c^2
\]

Nếu \(Q>0\), phản ứng giải phóng năng lượng ròng.

Nếu \(Q<0\), hệ cần được cung cấp động năng từ bên ngoài.

Đây là phiên bản hạt nhân của bài toán năng lượng phản ứng, nhưng thang năng lượng thường ở mức MeV thay vì eV.

### Ví dụ định lượng: từ chênh lệch khối lượng tới năng lượng

Nếu tổng khối lượng trước phản ứng lớn hơn tổng khối lượng sau phản ứng \(0.005\,u\), thì gần đúng:

\[
Q\approx0.005\times 931.5\;\text{MeV}\approx4.66\;\text{MeV}
\]

Con số khối lượng chênh rất nhỏ nhưng năng lượng trên mỗi sự kiện lại lớn vì hệ số chuyển đổi giữa khối lượng và năng lượng là rất lớn. Đây chính là cùng logic đã gặp ở **khuyết khối và năng lượng liên kết**.

## Vì sao bảng khối lượng cũng là bảng năng lượng

Khối lượng nguyên tử và hạt nhân đã mã hóa thông tin về năng lượng liên kết.

Một chênh lệch khối lượng rất nhỏ có thể tương ứng năng lượng lớn vì:

\[
1\,u\approx931.5\,MeV/c^2
\]

Do đó chỉ cần đo khối lượng đủ chính xác, ta có thể tính năng lượng của nhiều phản ứng hạt nhân.

## Năng lượng ngưỡng

Với phản ứng thu năng lượng, động năng hạt tới thường phải lớn hơn chỉ \(|Q|\) nếu xét trong hệ quy chiếu phòng thí nghiệm, vì động lượng cũng phải được bảo toàn.

Một phần động năng phải còn lại trong chuyển động của tâm khối, nên năng lượng ngưỡng có thể lớn hơn độ lớn của \(Q\) theo cách tính đơn giản.

Điểm này là ví dụ tốt cho giới hạn của việc chỉ nhìn vào cân bằng năng lượng: **động lượng và hình học va chạm cũng đặt ràng buộc**.

## Xác suất phản ứng và tiết diện

**Tiết diện phản ứng (cross section / 단면적)** định lượng xác suất hiệu dụng của một tương tác hạt nhân.

Đơn vị thường dùng là barn:

\[
1\,barn=10^{-28}\,m^2
\]

Tiết diện lớn nghĩa kênh phản ứng có xác suất cao hơn trong điều kiện năng lượng đang xét. Nó không có nghĩa hạt nhân thật sự là một đĩa cứng có diện tích đúng bằng giá trị đó.

## Vì sao tiết diện phụ thuộc năng lượng

Tiết diện có thể thay đổi rất mạnh theo năng lượng của hạt tới do nhiều yếu tố như hàng rào Coulomb, cộng hưởng, số kênh phản ứng khả dụng và mômen động lượng lượng tử.

Vì vậy cùng một hạt tới và cùng một bia có thể tạo hành vi hoàn toàn khác khi năng lượng thay đổi. Khi dùng dữ liệu tiết diện trong tính toán, luôn phải hỏi **tiết diện ở năng lượng nào?** thay vì coi \(\sigma\) như hằng số vật liệu cố định.

## Hàng rào Coulomb

Một hạt tích điện dương tiến tới hạt nhân cũng tích điện dương phải vượt lực đẩy tĩnh điện.

Thang năng lượng hàng rào có thể ước lượng:

\[
V_C\sim\frac{1}{4\pi\varepsilon_0}\frac{Z_1Z_2e^2}{R_1+R_2}
\]

Đây là lý do phản ứng do neutron gây ra thường dễ xảy ra hơn ở năng lượng thấp: neutron không phải vượt lực đẩy Coulomb.

## Xuyên hầm lượng tử

Hạt tích điện vẫn có xác suất phản ứng ngay cả khi năng lượng thấp hơn hàng rào Coulomb nhờ **xuyên hầm lượng tử (quantum tunneling)**.

Phản ứng nhiệt hạch trong sao phụ thuộc mạnh vào cơ chế này vì năng lượng nhiệt trung bình trong sao thấp hơn chiều cao hàng rào Coulomb nếu xét hoàn toàn theo cơ học cổ điển.

## Tán xạ đàn hồi

Trong **tán xạ đàn hồi (elastic scattering)**, hạt tới và hạt nhân bia giữ nguyên bản sắc; chỉ năng lượng và hướng chuyển động được phân bố lại.

Tán xạ đàn hồi được dùng để khảo sát kích thước, cấu trúc hạt nhân và để làm chậm neutron.

## Tán xạ không đàn hồi

Trong **tán xạ không đàn hồi (inelastic scattering)**, hạt nhân bia được kích thích:

\[
a+A\rightarrow a+A^*
\]

sau đó thường khử kích thích bằng cách phát gamma.

Một phần động năng của hạt tới vì vậy được chuyển thành năng lượng kích thích bên trong hạt nhân.

## Phản ứng bắt hạt

Hạt nhân bia có thể hấp thụ hạt tới rồi phát bức xạ hoặc hạt khác.

Ví dụ bắt neutron:

\[
{}^A_ZX+n\rightarrow{}^{A+1}_ZX^*\rightarrow{}^{A+1}_ZX+\gamma
\]

Quá trình bắt có thể tạo đồng vị phóng xạ từ hạt nhân ban đầu bền.

## Kích hoạt neutron

Chiếu neutron vào vật liệu có thể biến một số hạt nhân bền thành sản phẩm phóng xạ.

Đây là nền tảng của **phân tích kích hoạt neutron (neutron activation analysis)**. Vì năng lượng gamma phát ra đặc trưng cho nuclide, kỹ thuật này có thể dùng để phân tích nguyên tố ở hàm lượng rất thấp.

Đây cũng là lý do vật liệu gần nguồn neutron có thể trở thành nguồn bức xạ thứ cấp sau khi nguồn ban đầu đã tắt: **vật liệu đã bị kích hoạt**, không chỉ đơn giản là “bị chiếu xạ rồi hết”.

## Bắt proton và hạt alpha

Phản ứng bắt hạt tích điện phải đối mặt với hàng rào Coulomb, nên xác suất phụ thuộc mạnh năng lượng và xuyên hầm lượng tử.

Các phản ứng kiểu này có vai trò lớn trong tổng hợp hạt nhân bên trong sao.

## Phản ứng chuyển nucleon

Một hạt tới có thể trao đổi một hoặc nhiều nucleon với hạt nhân bia.

Ví dụ:

- phản ứng `(d,p)` thường tương ứng chuyển một neutron vào hạt nhân bia;
- phản ứng `(p,d)` có thể được xem như lấy một neutron khỏi bia.

Các phản ứng chuyển nucleon giúp khảo sát cấu trúc trạng thái hạt đơn của hạt nhân.

## Phản ứng bật hạt và spallation

Ở năng lượng cao hơn, hạt tới có thể làm bật nhiều nucleon hoặc làm hạt nhân bia vỡ thành các mảnh nhỏ hơn.

Nguồn **spallation** dùng proton năng lượng cao bắn vào bia nặng để tạo số lượng lớn neutron. Cách này được dùng trong khoa học neutron và sản xuất đồng vị.

## Mô hình hạt nhân hợp chất

Hạt tới có thể bị hấp thụ hoàn toàn, tạo một **hạt nhân hợp chất (compound nucleus)** kích thích cao. Hệ này phân bố lại năng lượng bên trong trước khi phân rã qua các kênh khả dụng.

```text
hạt tới + hạt nhân bia
→ hạt nhân hợp chất kích thích cao
→ bay hơi hạt / phát gamma / phân hạch / phát hạt khác
```

Mô hình này giải thích nhiều phản ứng cộng hưởng và phản ứng có tính thống kê.

## Phản ứng trực tiếp

Một số phản ứng xảy ra rất nhanh gần bề mặt hạt nhân mà không tạo trạng thái cân bằng nội đầy đủ.

Các phản ứng chuyển hoặc tước hạt (**stripping**) có thể giữ lại nhiều thông tin hơn về trạng thái lượng tử đầu và cuối.

Vì vậy không tồn tại một cơ chế duy nhất cho mọi phản ứng hạt nhân.

## Cộng hưởng

Nếu năng lượng hạt tới trùng với một trạng thái gần liên kết của hệ hợp chất, tiết diện có thể tăng mạnh.

**Cộng hưởng (resonance)** trong phản ứng hạt nhân có thể xem như hiện tượng ghép đúng mức năng lượng, tương tự trực giác về chuyển mức trong phổ học nhưng xảy ra trong hệ hạt nhân.

## Các vùng năng lượng neutron

Hành vi neutron phụ thuộc rất mạnh vào năng lượng. Một số nhãn định tính thường gặp là neutron nhiệt, neutron trên nhiệt và neutron nhanh.

Ranh giới chính xác giữa các vùng thay đổi theo bối cảnh.

Cùng một đồng vị có thể có tiết diện bắt hoặc phân hạch rất khác nhau giữa các vùng năng lượng đó.

## Làm chậm neutron

Neutron nhanh mất năng lượng qua va chạm, đặc biệt hiệu quả với hạt nhân nhẹ.

Vật liệu giàu hydrogen là chất làm chậm tốt vì khối lượng hạt nhân hydrogen gần neutron, cho phép truyền một phần lớn động năng trong mỗi va chạm.

Làm chậm neutron có thể làm xác suất của các phản ứng tiếp theo thay đổi mạnh.

## Hấp thụ neutron

Một số đồng vị có tiết diện bắt neutron lớn và có thể được dùng để loại neutron khỏi hệ.

Boron và cadmium là các ví dụ quen thuộc trong nhiều ứng dụng.

Cần phân biệt **làm chậm neutron (moderation)** với **hấp thụ neutron (absorption)**: một quá trình giảm năng lượng neutron, quá trình kia loại neutron khỏi quần thể tự do.

## Tốc độ phản ứng hạt nhân

Nếu thông lượng hạt tới là \(\phi\), số hạt nhân bia là \(N\) và tiết diện là \(\sigma\):

\[
R=N\sigma\phi
\]

Đây là dạng tương tự phương trình tốc độ trong Hóa học.

Trong hệ thực, nếu thông lượng phụ thuộc năng lượng thì cần tích phân trên toàn phổ năng lượng thay vì dùng một giá trị \(\sigma\) duy nhất.

### Liên hệ với động học hóa học

Trong phản ứng hóa học, tốc độ thường phụ thuộc nồng độ và hằng số tốc độ. Trong phản ứng hạt nhân dưới chùm hạt, vai trò tương tự được thực hiện bởi **số hạt bia × thông lượng × tiết diện**. Hai mô hình không giống nhau về vật lý vi mô nhưng cùng dùng một ý tưởng hệ thống: tốc độ sự kiện bằng số “mục tiêu khả dụng” nhân xác suất tương tác trên một đơn vị thông lượng.

## Tích lũy sản phẩm kích hoạt

Nếu sản phẩm tạo ra là chất phóng xạ có hằng số phân rã \(\lambda\):

\[
\frac{dN^*}{dt}=R-\lambda N^*
\]

Hệ tiến tới trạng thái trong đó tốc độ tạo sản phẩm cân bằng tốc độ phân rã.

Đây là một hệ động học bậc nhất có nguồn cấp liên tục. Nó là ví dụ rõ cho sự khác nhau giữa **trạng thái ổn định động học** và **cân bằng nhiệt động lực học**.

## Hoạt độ bão hòa

Nếu tốc độ tạo \(R\) không đổi:

\[
A(t)=R(1-e^{-\lambda t})
\]

Khi thời gian chiếu đủ dài:

\[
A\rightarrow R
\]

Sau khi dừng chiếu, hoạt độ lại giảm theo quy luật phân rã hàm mũ.

Do đó tăng thời gian chiếu vô hạn không làm hoạt độ tăng vô hạn. Khi gần bão hòa, phần sản phẩm tạo thêm trong mỗi đơn vị thời gian gần bằng phần đang phân rã.

## Chuyển nguyên tố

Khi phản ứng hạt nhân làm \(Z\) thay đổi, một nguyên tố thật sự biến thành nguyên tố khác. Quá trình này gọi là **chuyển nguyên tố (nuclear transmutation)**.

Giả kim thuật lịch sử từng tìm cách chuyển nguyên tố bằng phản ứng hóa học, nhưng điều đó không thể xảy ra vì phản ứng hóa học bảo toàn hạt nhân. Chuyển nguyên tố chỉ có thể xảy ra khi bản thân hạt nhân thay đổi.

## Đồng vị phóng xạ nhân tạo

Các phản ứng bắn phá có thể tạo đồng vị dùng trong y học, công nghiệp và nghiên cứu.

Việc chọn con đường sản xuất phụ thuộc đồng vị bia, loại hạt tới, tiết diện phản ứng, chu kỳ bán rã sản phẩm và độ tinh khiết đồng vị phóng xạ cần đạt.

Một con đường có tiết diện lớn chưa chắc tối ưu nếu đồng thời tạo nhiều đồng vị tạp khó tách hoặc sản phẩm có chu kỳ bán rã không phù hợp với logistics sử dụng.

## Mạng phản ứng hạt nhân trong sao

### Chuỗi proton–proton

Trong các sao giống Mặt Trời, chuỗi proton–proton là một con đường chính biến hydrogen thành helium.

### Chu trình CNO

Ở các sao nóng hơn, các hạt nhân C/N/O tham gia theo vai trò gần giống chất xúc tác trong chu trình chuyển hydrogen thành helium.

Cả hai quá trình giải phóng năng lượng vì helium-4 liên kết chặt hơn tổng các proton ban đầu.

## Tổng hợp nguyên tố nặng hơn helium

Các nguyên tố nặng dần được hình thành qua nhiều giai đoạn nhiệt hạch và bắt hạt trong sao.

Sau vùng sắt, nhiệt hạch thông thường không còn giải phóng năng lượng ròng thuận lợi, nên các nguyên tố nặng hơn chủ yếu cần các quá trình bắt neutron và phân rã.

## Quá trình s và quá trình r

Trong **quá trình s (s-process)**, bắt neutron chậm hơn phân rã beta nên đường tổng hợp nằm tương đối gần các hạt nhân bền.

Trong **quá trình r (r-process)**, bắt neutron diễn ra cực nhanh, tạo các hạt nhân rất giàu neutron trước khi chúng dần phân rã beta về vùng bền.

Hai cơ chế này giải thích nguồn gốc của nhiều nguyên tố nặng trong vũ trụ.

## Mạng phản ứng

Các hệ thiên văn và lò phản ứng có thể chứa hàng trăm hoặc hàng nghìn phản ứng ghép nối:

\[
\frac{dN_i}{dt}=\sum_j \text{tạo}_{j\to i}-\sum_k \text{mất}_{i\to k}
\]

Về toán học, đây rất giống mạng động học phản ứng hóa học với nhiều phương trình vi phân ghép nhau.

Khi số phản ứng lớn, các thang thời gian rất khác nhau có thể tạo hệ phương trình cứng (**stiff system**), cùng vấn đề số học đã gặp trong động học hóa học và mô hình phản ứng.

## So sánh năng lượng phản ứng hạt nhân và hóa học

Liên kết hóa học điển hình có thang eV trên mỗi phân tử, trong khi chuyển mức hạt nhân thường ở thang keV–MeV trên mỗi hạt nhân.

Chênh lệch thang năng lượng rất lớn này giải thích vì sao phản ứng hạt nhân có thể giải phóng năng lượng trên mỗi hạt biến đổi lớn hơn nhiều phản ứng hóa học.

Điều đó không có nghĩa mọi công nghệ hạt nhân tự động cho mật độ công suất cao hoặc hiệu suất hệ thống tốt; tốc độ phản ứng, truyền nhiệt, vật liệu, che chắn và kiểm soát neutron vẫn là các ràng buộc kỹ thuật riêng.

## Phép đo hạt nhân như một bài toán nghịch đảo

Nếu đầu dò đo năng lượng và góc của các hạt đi ra, các định luật bảo toàn có thể được dùng để suy ngược trạng thái hạt nhân chưa biết.

Phổ học hạt nhân vì vậy là một **bài toán nghịch đảo (inverse problem)** tương tự phổ học phân tử, nhưng sử dụng tương tác và thang năng lượng khác.

## Những hiểu lầm thường gặp

### “Chỉ cần cân bằng A và Z là phản ứng chắc chắn xảy ra”

Không. Năng lượng, động lượng và các ràng buộc lượng tử vẫn phải thỏa mãn.

### “Tiết diện chính là kích thước hình học của hạt nhân”

Không. Nó là thước đo xác suất hiệu dụng và có thể lớn hoặc nhỏ hơn diện tích hình học trực giác.

### “Neutron lúc nào cũng dễ sử dụng vì không mang điện”

Neutron tránh hàng rào Coulomb nhưng khó tạo, điều khiển và phát hiện, đồng thời có thể kích hoạt vật liệu.

### “Chuyển nguyên tố là một dạng phản ứng hóa học”

Không. Thay đổi nguyên tố đòi hỏi thay đổi hạt nhân, không chỉ tái sắp xếp electron.

### “Q dương nghĩa phản ứng chắc chắn xảy ra nhanh”

Không. Q chỉ nói về chênh lệch năng lượng ròng. Hàng rào Coulomb, tiết diện và các quy tắc chọn quyết định khả năng và tốc độ quan sát.

## Mô hình tư duy

Phản ứng hạt nhân là **va chạm cộng với chuyển trạng thái lượng tử dưới các định luật bảo toàn**. Giá trị Q cho biết năng lượng được giải phóng hay cần cung cấp; tiết diện cho biết kênh phản ứng có xác suất lớn đến đâu; mạng phản ứng cho biết quần thể các nuclide thay đổi như thế nào theo thời gian.

Xem tiếp: [Phân hạch và nhiệt hạch](./03_fission_and_fusion.md).