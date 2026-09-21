# Chất lỏng — cấu trúc động, dòng chảy và bề mặt

> **Chất lỏng (liquid / 액체)** là trạng thái vật chất có mật độ cao và thể tích gần cố định nhưng không giữ hình dạng riêng. Các tiểu phần nằm gần nhau như trong chất rắn, song có đủ tự do để liên tục đổi hàng xóm, khuếch tán và chảy. Vì vậy chất lỏng phải được hiểu như một **mạng tương tác linh động**, không phải một chất rắn mất trật tự hoàn toàn hay một chất khí bị nén mạnh.

## Chất lỏng nằm giữa khí và rắn như thế nào?

Trong khí loãng, khoảng cách trung bình giữa các hạt lớn và chuyển động tịnh tiến tương đối tự do. Trong chất rắn tinh thể, hạt dao động quanh cấu hình có trật tự dài hạn. Chất lỏng nằm giữa hai giới hạn này: khoảng cách giữa các hạt ngắn, tương tác liên phân tử quan trọng, nhưng trật tự dài hạn liên tục bị chuyển động nhiệt phá vỡ.

Có thể hình dung sự cạnh tranh:

```text
lực hút + đóng gói phân tử
↔
chuyển động nhiệt + entropy
```

Nếu tương tác chi phối mạnh hơn, pha rắn có thể ổn định. Nếu entropy và xu hướng tách xa thắng đủ mạnh, pha khí được ưu tiên. Pha lỏng ổn định trong vùng trung gian của năng lượng tự do.

## Chất lỏng có cấu trúc hay không?

Chất lỏng không có mạng tuần hoàn dài hạn như tinh thể, nhưng cũng không hoàn toàn ngẫu nhiên. Các phân tử gần nhau thường có **trật tự cục bộ (short-range order)**.

Ví dụ, nước có xu hướng tạo cấu trúc gần tetrahedral cục bộ do liên kết hydro. Trong chất lỏng ion, cation và anion có tương quan mạnh về khoảng cách.

Một đại lượng dùng trong vật lý chất lỏng và mô phỏng là **hàm phân bố xuyên tâm (radial distribution function, \(g(r)\))**. Nó cho biết xác suất tìm thấy một hạt ở khoảng cách \(r\) quanh một hạt tham chiếu so với phân bố hoàn toàn ngẫu nhiên.

Trong tinh thể, `g(r)` có các đỉnh kéo dài rất xa. Trong chất lỏng, một vài đỉnh đầu rõ ràng nhưng trật tự suy giảm khi khoảng cách tăng.

## Vì sao chất lỏng khó nén?

Các phân tử trong chất lỏng đã ở gần khoảng cách cân bằng. Muốn giảm thể tích đáng kể phải ép các đám mây electron vào vùng lực đẩy tăng rất nhanh.

Do đó **hệ số nén (compressibility)** của chất lỏng nhỏ hơn khí rất nhiều.

Tuy nhiên “chất lỏng không nén được” chỉ là xấp xỉ kỹ thuật. Trong thủy lực thông thường xấp xỉ này rất hữu ích, nhưng ở áp suất rất cao hoặc khi nghiên cứu sóng âm cần xét độ nén hữu hạn.

## Khuếch tán trong chất lỏng

Các phân tử liên tục chuyển động nhiệt và đổi vị trí, nên một chất tan có thể tự lan từ vùng nồng độ cao sang thấp.

Định luật Fick ở dạng một chiều đơn giản:

\[
J=-D\frac{dc}{dx}
\]

trong đó `J` là thông lượng và `D` là hệ số khuếch tán.

Dấu âm nói rằng dòng vật chất đi theo chiều giảm nồng độ khi chỉ xét cơ chế khuếch tán đơn giản.

Hệ số khuếch tán phụ thuộc kích thước tiểu phần, độ nhớt, nhiệt độ và tương tác với dung môi. Trong mô hình hạt cầu loãng, quan hệ Stokes–Einstein gần đúng là:

\[
D=\frac{k_BT}{6\pi\eta r}
\]

Nhưng công thức này có thể sai với phân tử nhỏ, chất lỏng rất nhớt hoặc môi trường có cấu trúc phức tạp.

## Độ nhớt là gì?

**Độ nhớt (viscosity / 점도)** mô tả mức cản của chất lưu đối với biến dạng trượt.

Với chất lỏng Newton đơn giản:

\[
\tau=\eta\frac{dv}{dy}
\]

trong đó:

- \(\tau\) là ứng suất trượt;
- \(\eta\) là độ nhớt động lực;
- \(dv/dy\) là gradient vận tốc.

Ở mức phân tử, dòng chảy đòi hỏi các tiểu phần liên tục vượt qua hàng rào tái sắp xếp cục bộ. Tương tác mạnh, phân tử dài hoặc mạng liên kết rộng có thể làm quá trình đó chậm hơn.

## Vì sao tăng nhiệt độ thường làm chất lỏng ít nhớt hơn?

Khi nhiệt độ tăng, phân bố năng lượng rộng hơn và các phân tử vượt các rào cản tái sắp xếp dễ hơn. Vì vậy độ nhớt của nhiều chất lỏng giảm mạnh khi nhiệt độ tăng.

Đây là lý do dầu động cơ đặc hơn khi lạnh.

Khí có xu hướng ngược lại trong nhiều điều kiện: độ nhớt của khí thường tăng theo nhiệt độ vì vận chuyển động lượng giữa các lớp khí tăng.

## Chất lỏng phi Newton

Không phải mọi chất lỏng đều có \(\tau\propto dv/dy\). Dung dịch polymer, sơn, máu, hồ tinh bột và nhiều huyền phù có thể là **chất lưu phi Newton (non-Newtonian fluid)**.

Độ nhớt hiệu dụng có thể giảm khi tốc độ cắt tăng (**shear thinning**) hoặc tăng (**shear thickening**).

Đây là ví dụ cho thấy tính chất dòng chảy không chỉ đến từ “độ mạnh lực liên phân tử” mà còn từ cấu trúc tập thể và thời gian tái tổ chức của hệ.

## Sức căng bề mặt từ đâu ra?

Một phân tử trong lòng chất lỏng có hàng xóm ở nhiều hướng. Ở bề mặt, số hàng xóm giảm và môi trường tương tác không đối xứng.

Tạo thêm diện tích bề mặt thường làm tăng năng lượng tự do:

\[
dG=\gamma\,dA
\]

với \(\gamma\) là **sức căng bề mặt (surface tension / 표면 장력)**.

Chính vì hệ muốn giảm diện tích bề mặt nên giọt nhỏ có xu hướng gần hình cầu nếu trọng lực không chi phối mạnh.

## Áp suất Laplace và kích thước giọt

Đối với một giọt cầu lý tưởng, chênh lệch áp suất giữa trong và ngoài gần:

\[
\Delta P=\frac{2\gamma}{R}
\]

Giọt càng nhỏ thì áp suất bên trong càng lớn.

Quan hệ này quan trọng với bọt, aerosol, phổi, nhũ tương và công nghệ vi lỏng.

Trong phế nang, chất hoạt động bề mặt sinh học làm giảm sức căng bề mặt và giúp ngăn các túi khí nhỏ bị xẹp quá dễ.

## Làm ướt và góc tiếp xúc

Khi một giọt nằm trên bề mặt rắn, hình dạng của nó phản ánh cân bằng năng lượng giữa ba giao diện: rắn–khí, rắn–lỏng và lỏng–khí.

**Góc tiếp xúc (contact angle)** nhỏ thường tương ứng với bề mặt được làm ướt tốt; góc lớn tương ứng với làm ướt kém.

Khái niệm này quan trọng trong:

- sơn và phủ bề mặt;
- in mực;
- chất kết dính;
- xử lý chống nước;
- pin và điện cực xốp.

Một bề mặt “kỵ nước” không chỉ do thành phần hóa học; độ nhám vi mô cũng có thể làm hành vi thấm ướt thay đổi mạnh.

## Mao dẫn

Trong ống nhỏ, chất lỏng có thể dâng hoặc hạ do cạnh tranh giữa sức căng bề mặt, thấm ướt và trọng lực.

Với ống tròn lý tưởng:

\[
h=\frac{2\gamma\cos\theta}{\rho gr}
\]

trong đó \(\theta\) là góc tiếp xúc.

Ống càng nhỏ thì hiệu ứng mao dẫn càng lớn.

Mao dẫn là cơ chế quan trọng trong giấy, đất, gỗ, vật liệu xốp và nhiều hệ vi lưu.

## Bay hơi xảy ra dưới nhiệt độ sôi

Trong một chất lỏng, các phân tử có phân bố năng lượng. Một số phân tử ở bề mặt có đủ năng lượng và hướng chuyển động thuận lợi để thoát sang pha khí.

Đó là **bay hơi (evaporation)**.

Bay hơi làm các phân tử năng lượng cao rời hệ ưu tiên, nên phần chất lỏng còn lại có thể nguội đi. Đây là cơ chế cơ bản của mồ hôi làm mát cơ thể.

## Áp suất hơi cân bằng

Trong bình kín, phân tử liên tục bay hơi và ngưng tụ. Khi tốc độ hai chiều bằng nhau, hệ đạt cân bằng động.

Áp suất do hơi tạo ra khi đó là **áp suất hơi cân bằng (equilibrium vapor pressure)**.

Áp suất hơi phụ thuộc nhiệt độ và bản chất chất lỏng, không phụ thuộc trực tiếp lượng chất lỏng còn lại miễn là vẫn còn cả pha lỏng và pha hơi ở cân bằng.

## Liên hệ nhiệt độ – áp suất hơi

Gần đúng Clausius–Clapeyron:

\[
\ln\frac{P_2}{P_1}
=-\frac{\Delta H_{vap}}{R}
\left(\frac1{T_2}-\frac1{T_1}\right)
\]

cho thấy áp suất hơi tăng rất nhanh với nhiệt độ.

Đây là cầu nối giữa nhiệt động lực học và hiện tượng đời sống như phơi khô, chưng cất hoặc nấu ăn ở vùng cao.

## Sự sôi

Sôi xảy ra khi áp suất hơi của chất lỏng bằng áp suất bên ngoài, cho phép bọt hơi tồn tại trong lòng chất lỏng.

Do đó nhiệt độ sôi không phải một hằng số tuyệt đối của chất. Nó phụ thuộc áp suất ngoài.

Ở vùng cao, áp suất khí quyển thấp hơn nên nước sôi dưới `100 °C`. Trong nồi áp suất, áp suất tăng nên nước có thể đạt nhiệt độ lớn hơn trước khi sôi mạnh.

## Tạo mầm khi sôi

Để hình thành một bọt hơi mới, hệ phải tạo bề mặt lỏng–khí, có chi phí năng lượng. Vì vậy chất lỏng rất sạch trong bình nhẵn có thể bị **quá nhiệt (superheating)** mà chưa sôi mạnh.

Khi bọt bất ngờ hình thành, chất lỏng có thể sôi bùng. Đây là một nguy cơ thực tế khi đun nước trong lò vi sóng.

Các điểm nhám, hạt bụi hoặc đá bọt giúp tạo mầm và làm sôi ổn định hơn.

## Nước là chất lỏng đặc biệt nhưng không “vi phạm quy luật”

Nước có mạng liên kết hydro động. Mạng này làm nhiều tính chất lệch mạnh khỏi xu hướng đơn giản theo khối lượng mol.

Khối lượng riêng của nước đạt cực đại gần `4 °C`; khi tiến tới đóng băng, cấu trúc cục bộ trở nên mở hơn và thể tích tăng.

Nhiệt dung cao giúp đại dương và cơ thể sống đệm nhiệt. Sức căng bề mặt lớn ảnh hưởng giọt, mao dẫn và sinh học bề mặt.

Các tính chất này vẫn là hệ quả của nhiệt động lực học và cấu trúc phân tử, không phải ngoại lệ khỏi vật lý.

## Chất lỏng trong sinh học

Tế bào hoạt động trong môi trường nước cô đặc với protein, ion, lipid và polymer. Nước trong tế bào không hoàn toàn giống nước tinh khiết vì tương tác với các bề mặt và chất tan làm thay đổi cấu trúc cục bộ và động lực.

Vận chuyển qua màng, khuếch tán thuốc, phản ứng enzyme và sự gấp cuộn protein đều phụ thuộc tính chất của pha lỏng.

## Chất lỏng trong pin và vật liệu năng lượng

Chất điện ly lỏng trong pin phải đồng thời:

- hòa tan đủ muối;
- dẫn ion tốt;
- có độ nhớt không quá cao;
- ổn định điện hóa;
- làm ướt điện cực và separator;
- an toàn về cháy và nhiệt.

Một dung môi rất phân cực có thể hòa tan muối tốt nhưng tạo solvation quá mạnh, làm desolvation ở giao diện chậm hơn. Đây là ví dụ rõ của trade-off trong thiết kế chất lỏng kỹ thuật.

## Các hiểu lầm thường gặp

### “Phân tử chất lỏng đứng gần như cố định”

Không. Chúng liên tục dao động, quay, khuếch tán và thay đổi hàng xóm.

### “Nhiệt độ sôi là nhiệt độ phá vỡ phân tử”

Không. Chủ yếu phải thắng tương tác giữa các phân tử để tạo pha khí; liên kết cộng hóa trị bên trong phân tử thường vẫn còn.

### “Áp suất hơi chỉ xuất hiện khi sôi”

Không. Mọi chất lỏng có độ bay hơi hữu hạn đều tạo hơi ở nhiệt độ thấp hơn điểm sôi.

### “Chất lỏng không thể nén”

Đây chỉ là xấp xỉ tốt trong nhiều bài kỹ thuật, không phải sự thật tuyệt đối.

### “Độ nhớt chỉ đo độ mạnh lực liên phân tử”

Không. Hình dạng, rối chuỗi, cấu trúc tập thể và tốc độ tái sắp xếp cũng quan trọng.

## Mô hình tư duy

Chất lỏng là một **mạng tương tác luôn tái cấu trúc**. Khoảng cách ngắn làm lực liên phân tử quan trọng, còn chuyển động nhiệt ngăn hệ bị khóa thành một cấu trúc cố định. Từ cạnh tranh đó xuất hiện khuếch tán, dòng chảy, sức căng bề mặt, áp suất hơi và sự sôi.

```text
cấu trúc phân tử
→ tương tác liên phân tử
→ trật tự cục bộ + động lực
→ vận chuyển + bề mặt + cân bằng pha
→ tính chất vĩ mô
```

Xem tiếp: [Chất rắn](./02_solids.md) và [Chuyển pha – giản đồ pha](./03_phase_changes_and_phase_diagrams.md).