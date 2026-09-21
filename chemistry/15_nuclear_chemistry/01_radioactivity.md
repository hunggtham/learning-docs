# Phóng xạ — biến đổi hạt nhân xác suất, động học phân rã và tương tác bức xạ

> **Phóng xạ (radioactivity / 방사능)** là sự biến đổi tự phát của các hạt nhân không bền. Mỗi sự kiện phân rã riêng lẻ có bản chất xác suất lượng tử, nhưng một quần thể lớn hạt nhân lại tuân theo thống kê hàm mũ rất chính xác. Đây là một ví dụ điển hình cho việc tính ngẫu nhiên vi mô có thể tạo ra khả năng dự đoán vĩ mô.

## Định luật phân rã

Nếu mỗi hạt nhân có xác suất phân rã không đổi trên một đơn vị thời gian, đặc trưng bởi hằng số \(\lambda\):

\[
\frac{dN}{dt}=-\lambda N
\]

Nghiệm là:

\[
N(t)=N_0e^{-\lambda t}
\]

**Hoạt độ phóng xạ (activity)** được định nghĩa:

\[
A=-\frac{dN}{dt}=\lambda N
\]

Do đó hoạt độ cũng giảm theo hàm mũ khi quần thể hạt nhân mẹ bị tiêu hao.

## Chu kỳ bán rã

**Chu kỳ bán rã (half-life)** là thời gian để số hạt chưa phân rã giảm còn một nửa giá trị ban đầu:

\[
t_{1/2}=\frac{\ln2}{\lambda}
\]

Sau mỗi chu kỳ bán rã, giá trị kỳ vọng của quần thể còn lại giảm một nửa.

Chu kỳ bán rã là tính chất của quần thể thống kê, không phải chiếc “đồng hồ đếm ngược” gắn riêng trên từng nguyên tử.

## Thời gian sống trung bình

**Thời gian sống trung bình (mean lifetime)** là:

\[
\tau=\frac{1}{\lambda}
\]

và có quan hệ:

\[
t_{1/2}=\tau\ln2
\]

Hai đại lượng mô tả cùng một quá trình nhưng hữu ích trong những cách xử lý toán học khác nhau.

## Đơn vị hoạt độ

**Becquerel (Bq)** tương ứng một phân rã mỗi giây.

Đơn vị cũ **curie (Ci)** lớn hơn rất nhiều.

Hoạt độ cao không tự động đồng nghĩa liều hấp thụ cao. Loại bức xạ, năng lượng, khoảng cách, hình học nguồn, che chắn và đường xâm nhập vào cơ thể đều ảnh hưởng mức năng lượng thực sự được hấp thụ.

## Phân rã alpha

Hạt alpha chính là hạt nhân helium-4:

\[
{}^A_ZX\rightarrow{}^{A-4}_{Z-2}Y+{}^4_2He
\]

Alpha gây ion hóa mạnh trên một đơn vị chiều dài đường đi nhưng có khả năng xuyên thấu thấp.

Nguồn alpha ở bên ngoài thường bị lớp vật liệu mỏng hoặc lớp ngoài của da chặn lại tương đối dễ, nhưng chất phát alpha khi đi vào trong cơ thể có thể nguy hiểm vì năng lượng được lắng đọng trong khoảng cách rất ngắn.

## Xuyên hầm lượng tử trong phân rã alpha

Theo cơ học cổ điển, cụm alpha có thể không đủ năng lượng để vượt qua hàng rào Coulomb của hạt nhân.

Cơ học lượng tử cho phép xác suất **xuyên hầm (quantum tunneling)** qua hàng rào hữu hạn.

Xác suất xuyên hầm phụ thuộc rất nhạy vào chiều cao và chiều rộng hàng rào, vì vậy chỉ một thay đổi nhỏ về năng lượng alpha cũng có thể làm chu kỳ bán rã thay đổi qua nhiều bậc độ lớn.

## Phân rã beta trừ

Trong phân rã \(\beta^-\), một neutron biến đổi thành proton:

\[
n\rightarrow p+e^-+\bar\nu_e
\]

Ở cấp hạt nhân:

\[
{}^A_ZX\rightarrow{}^A_{Z+1}Y+e^-+\bar\nu_e
\]

Số khối \(A\) không đổi, còn \(Z\) tăng thêm 1.

## Phân rã beta cộng

Trong phân rã \(\beta^+\):

\[
p\rightarrow n+e^++\nu_e
\]

Ở cấp hạt nhân, \(Z\) giảm 1 trong khi \(A\) không đổi.

Positron tạo ra sau đó có thể hủy cặp với electron và tạo photon gamma. Chụp cắt lớp phát xạ positron (**Positron Emission Tomography, PET**) khai thác cơ chế này để tạo tín hiệu hình ảnh.

## Bắt electron

Trong **bắt electron (electron capture)**, hạt nhân bắt một electron lớp trong:

\[
p+e^-\rightarrow n+\nu_e
\]

Khi đó \(Z\) giảm 1.

Việc mất electron lớp trong tạo lỗ trống trong vỏ electron. Khi các electron bên ngoài tái sắp xếp để lấp lỗ trống, hệ có thể phát tia X đặc trưng hoặc electron Auger.

## Phân rã gamma

Một hạt nhân kích thích có thể phát photon gamma:

\[
X^*\rightarrow X+\gamma
\]

Cả \(A\) và \(Z\) đều không đổi; chỉ trạng thái năng lượng của hạt nhân thay đổi.

Gamma có khả năng xuyên sâu hơn alpha vì xác suất tương tác trên một đơn vị đường đi thấp hơn, dù vẫn có thể lắng đọng năng lượng đáng kể trong vật chất.

## Chuyển đổi nội

Thay vì phát photon gamma, hạt nhân kích thích có thể truyền trực tiếp năng lượng cho một electron orbital và đẩy electron đó ra khỏi nguyên tử.

Cơ chế này gọi là **chuyển đổi nội (internal conversion)** và có thể cạnh tranh với phát gamma đối với một số chuyển mức hạt nhân.

## Chuỗi phân rã

Sản phẩm của một phân rã có thể vẫn không bền và tiếp tục phân rã:

```text
hạt nhân mẹ → hạt nhân con → thế hệ tiếp theo → ... → nuclide bền
```

Các chuỗi uranium và thorium chứa nhiều bước alpha và beta liên tiếp.

Hoạt độ của từng thành viên trong chuỗi phụ thuộc đồng thời tốc độ nó được tạo ra và tốc độ nó tiếp tục phân rã.

## Cân bằng thế tục

Nếu chu kỳ bán rã của hạt nhân mẹ dài hơn rất nhiều hạt nhân con, sau một thời gian hoạt độ của hạt nhân con có thể gần đi theo hoạt độ của hạt nhân mẹ.

Quan hệ này gọi là **cân bằng thế tục (secular equilibrium)**. Đây là một quan hệ trạng thái ổn định động học trong chuỗi phân rã, không phải cân bằng nhiệt động lực học.

## Phân nhánh phân rã

Một nuclide có thể phân rã theo nhiều kênh khác nhau. Khi đó:

\[
\lambda=\sum_i\lambda_i
\]

và phần nhánh của kênh \(i\) là:

\[
b_i=\frac{\lambda_i}{\lambda}
\]

Phần nhánh cho biết xác suất tương đối một phân rã đi theo từng con đường.

## Bức xạ tương tác với vật chất như thế nào

Các loại bức xạ mất năng lượng theo những cơ chế khác nhau.

### Hạt mang điện

Hạt alpha và beta mất năng lượng chủ yếu qua ion hóa và kích thích electron dọc theo đường đi.

### Gamma và tia X

Photon năng lượng cao có thể tương tác qua hiệu ứng quang điện, tán xạ Compton hoặc tạo cặp, tùy năng lượng photon và thành phần vật liệu.

### Neutron

Neutron không mang điện nên tương tác chủ yếu với hạt nhân qua tán xạ hoặc bắt neutron. Vì vậy neutron gây ion hóa gián tiếp thông qua các hạt tích điện thứ cấp sinh ra sau tương tác.

## Mật độ truyền năng lượng tuyến tính

**Mật độ truyền năng lượng tuyến tính (Linear Energy Transfer, LET)** mô tả năng lượng được lắng đọng trên một đơn vị chiều dài đường đi.

Alpha thường có LET cao; gamma có LET thấp hơn.

Bức xạ LET cao tạo dải ion hóa dày đặc hơn và vì vậy có thể tạo kiểu tổn thương sinh học khác với bức xạ LET thấp ở cùng mức năng lượng hấp thụ.

## Tầm đi và khả năng xuyên thấu

Bức xạ gây ion hóa càng mạnh trên mỗi đơn vị chiều dài thường mất năng lượng càng nhanh và có tầm đi ngắn hơn.

Do đó alpha lắng đọng năng lượng rất tập trung nhưng xuyên kém; gamma tương tác thưa hơn trên đường đi nên có thể xuyên sâu hơn trước khi mất phần lớn năng lượng.

## Nguyên lý che chắn

Vật liệu che chắn phù hợp phụ thuộc loại bức xạ.

- alpha thường chỉ cần lớp chắn mỏng khi nguồn ở bên ngoài;
- beta thường ưu tiên vật liệu số nguyên tử thấp để giảm bức xạ hãm;
- gamma thường cần vật liệu đặc và số nguyên tử cao;
- neutron thường cần vật liệu giàu hydrogen để làm chậm, kết hợp vật liệu có khả năng bắt neutron.

Không có một loại “tường chống bức xạ” tối ưu cho mọi trường hợp.

## Quan hệ nghịch đảo bình phương

Với nguồn gần điểm trong không gian mở, cường độ giảm gần theo:

\[
I\propto\frac{1}{r^2}
\]

Vì vậy khoảng cách là một biến rất hiệu quả trong kiểm soát phơi nhiễm.

Tuy nhiên nguồn thực có kích thước hữu hạn, môi trường có tán xạ và hình học phòng có thể làm hệ lệch khỏi mô hình nguồn điểm lý tưởng.

## Thời gian, khoảng cách và che chắn

Ba nguyên lý kinh điển của bảo vệ bức xạ là:

```text
giảm thời gian phơi nhiễm
→ tăng khoảng cách
→ dùng che chắn phù hợp
```

Đây là khung suy luận quản lý rủi ro, không thay thế quy trình an toàn bức xạ chuyên nghiệp trong môi trường làm việc thực tế.

## Liều hấp thụ

**Gray (Gy)** là joule năng lượng lắng đọng trên kilogram vật chất:

\[
1\,Gy=1\,J/kg
\]

Đại lượng này khác hoàn toàn hoạt độ tính bằng Bq. Một nguồn có thể có hoạt độ lớn nhưng tạo liều nhỏ tại một vị trí xa, hoặc ngược lại, tùy loại bức xạ và điều kiện hình học.

## Liều tương đương và liều hiệu dụng

**Sievert (Sv)** đưa thêm hệ số trọng số theo loại bức xạ; đối với liều hiệu dụng còn có trọng số theo mô hoặc cơ quan để phản ánh gần đúng rủi ro sinh học.

Gy và Sv vì vậy trả lời những câu hỏi khác nhau: Gy hỏi bao nhiêu năng lượng được hấp thụ; Sv cố gắng phản ánh hệ quả sinh học tương đối của sự hấp thụ đó.

## Hiệu ứng mô và rủi ro ngẫu nhiên

Ở liều đủ cao, một số tổn thương mô có ngưỡng và mức nghiêm trọng tăng theo liều.

Nguy cơ ung thư thường được xử lý như một hiệu ứng ngẫu nhiên, trong đó xác suất tăng theo liều. Ở vùng liều thấp, việc ước lượng rủi ro có độ không đảm bảo đáng kể và phụ thuộc mô hình dịch tễ.

## Bức xạ nền

Môi trường tự nhiên luôn có bức xạ từ tia vũ trụ, nuclide trong đất đá, radon và các đồng vị tự nhiên trong cơ thể.

Vì vậy “có bức xạ” không tự động đồng nghĩa “nguy hiểm”. Đánh giá rủi ro phải dựa trên liều, loại bức xạ, thời gian và đường phơi nhiễm.

## Radon

Radon là khí phóng xạ xuất hiện trong các chuỗi phân rã uranium và có thể tích tụ trong không gian kín.

Các sản phẩm phân rã sống ngắn của radon có thể phát alpha; khi hít vào, chúng làm tăng phơi nhiễm cho mô phổi.

Đây là ví dụ rõ cho việc hóa học và vận chuyển của một chất khí có thể kiểm soát rủi ro bắt nguồn từ quá trình hạt nhân.

## Định tuổi bằng đồng vị phóng xạ

Nếu hệ gần kín và điều kiện ban đầu có thể được ràng buộc, định luật phân rã cho phép suy ra tuổi.

Carbon-14 phù hợp với vật liệu hữu cơ tương đối gần thời hiện đại; các hệ đồng vị sống lâu hơn được dùng để định tuổi đá và sự kiện địa chất qua thời gian rất dài.

Độ chính xác phụ thuộc nhiễm bẩn, hiệu chuẩn và lịch sử mở/đóng của hệ mẫu.

## Carbon-14

Các quá trình do tia vũ trụ tạo \(^{14}C\) trong khí quyển. Sinh vật sống liên tục trao đổi carbon với môi trường; sau khi chết, trao đổi này dừng lại và \(^{14}C\) tiếp tục phân rã.

Tỉ lệ đồng vị đo được kết hợp đường cong hiệu chuẩn cho phép ước lượng tuổi mẫu.

Đây là một ví dụ nơi động học đồng vị trở thành công cụ đo thời gian.

## Đồng vị đánh dấu

Đồng vị phóng xạ có thể dùng làm **chất đánh dấu (tracer)** vì tín hiệu phóng xạ rất nhạy, trong khi đồng vị thường đi theo hóa học gần giống dạng bền của cùng nguyên tố.

Ứng dụng bao gồm theo dõi chuyển hóa, nước ngầm, dòng vật liệu và phát hiện rò rỉ trong công nghiệp.

## Các phương pháp phát hiện

### Ống đếm Geiger–Müller

Phát hiện các sự kiện ion hóa nhưng thường cung cấp ít thông tin chi tiết về năng lượng.

### Đầu dò nhấp nháy

Bức xạ tạo xung ánh sáng trong vật liệu nhấp nháy, sau đó ánh sáng được chuyển thành tín hiệu điện.

### Đầu dò bán dẫn

Bức xạ tạo cặp electron–lỗ trống trong chất bán dẫn. Một số hệ bán dẫn có thể đạt độ phân giải năng lượng rất cao.

### Liều kế

Liều kế theo dõi mức phơi nhiễm hoặc liều tích lũy cho cá nhân hay khu vực.

## Thống kê đếm

Khi các sự kiện phân rã gần độc lập, số đếm thường xấp xỉ phân bố Poisson.

Nếu đo được \(N\) sự kiện:

\[
\sigma\approx\sqrt{N}
\]

Độ không đảm bảo tương đối xấp xỉ:

\[
\frac{\sigma}{N}\approx\frac{1}{\sqrt N}
\]

Vì vậy tăng thời gian đếm làm độ chụm tăng theo căn bậc hai, không tăng tuyến tính.

## Trừ nền

Số đếm đo được gồm tín hiệu nguồn và tín hiệu nền.

Nền cần được đo riêng rồi trừ đi, đồng thời độ không đảm bảo của cả phép đo nguồn và phép đo nền phải được lan truyền vào kết quả cuối.

Ở hoạt độ thấp, thống kê của nền có thể trở thành nguồn độ không đảm bảo chi phối.

## Thời gian chết của đầu dò

Đầu dò cần một khoảng thời gian hồi phục hữu hạn sau mỗi sự kiện. Nếu tốc độ đếm quá cao, một số sự kiện có thể bị bỏ sót và đáp ứng trở nên phi tuyến.

Khi đó cần hiệu chỉnh **thời gian chết (dead time)** hoặc thay đổi hình học đo để đưa tốc độ đếm về vùng làm việc thích hợp.

## Những hiểu lầm thường gặp

### “Vật liệu phóng xạ luôn tự phát sáng”

Không. Phần lớn vật liệu phóng xạ không tự phát ra ánh sáng nhìn thấy rõ.

### “Sau một chu kỳ bán rã, mọi nguyên tử đều đã phân rã một nửa thời gian của mình”

Không. Chu kỳ bán rã mô tả quần thể; từng hạt nhân riêng lẻ vẫn có thời điểm phân rã ngẫu nhiên.

### “Bq càng lớn thì chất càng nguy hiểm”

Không thể kết luận chỉ từ hoạt độ. Liều còn phụ thuộc loại bức xạ, năng lượng, khoảng cách, đường xâm nhập và che chắn.

### “Bức xạ hoặc an toàn hoàn toàn hoặc nguy hiểm hoàn toàn”

Không. Rủi ro phụ thuộc liều và bối cảnh phơi nhiễm.

## Mô hình tư duy

Phóng xạ là **động học xác suất bậc nhất của một quần thể hạt nhân không bền**. Hoạt độ cho biết biến đổi xảy ra thường xuyên đến đâu; vận chuyển bức xạ cho biết năng lượng đi đâu; liều cho biết bao nhiêu năng lượng tới vật chất; sinh học quyết định hệ quả của năng lượng đó.

Xem tiếp: [Phản ứng hạt nhân](./02_nuclear_reactions.md).