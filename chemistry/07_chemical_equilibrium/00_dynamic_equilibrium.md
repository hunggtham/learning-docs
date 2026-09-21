# Cân bằng động — từ tốc độ thuận nghịch đến cực tiểu Gibbs

> **Cân bằng hóa học (chemical equilibrium / 화학 평형)** là trạng thái trong đó thành phần vĩ mô của hệ không còn thay đổi theo thời gian, dù các quá trình thuận và nghịch vẫn tiếp tục ở cấp phân tử. Vì vậy cân bằng là **động**, không phải trạng thái mọi chuyển động đã dừng.

Cân bằng là điểm gặp của ba cách nhìn:

```text
động học: tốc độ thuận = tốc độ nghịch
nhiệt động lực học: ΔrG = 0
thống kê: các dao động vi mô có trung bình ổn định
```

Ba mô tả này tương thích nhưng trả lời những câu hỏi khác nhau.

## Vì sao cần khái niệm cân bằng?

Nhiều phản ứng không đi hoàn toàn tới một phía. Với phản ứng thuận nghịch:

\[
N_2O_4(g)\rightleftharpoons 2NO_2(g)
\]

nếu bắt đầu chỉ với `N2O4`, phản ứng phân ly tạo `NO2`. Khi `NO2` tích lũy, xác suất các phân tử `NO2` gặp nhau và tái tạo `N2O4` tăng.

Cuối cùng tốc độ hai chiều bằng nhau:

\[
v_{thuận}=v_{nghịch}
\]

Khi đó nồng độ trung bình không còn đổi, nhưng các phân tử vẫn liên tục chuyển hóa qua lại.

Đây là lý do cân bằng không thể hiểu là “phản ứng đã dừng”.

## Tốc độ ròng bằng 0

Với một phản ứng thuận nghịch, tốc độ ròng có thể viết khái niệm:

\[
v_{net}=v_{thuận}-v_{nghịch}
\]

Tại cân bằng:

\[
v_{net}=0
\]

nhưng điều đó không có nghĩa:

\[
v_{thuận}=v_{nghịch}=0
\]

Hai tốc độ có thể đều lớn nhưng triệt tiêu ở mức ròng.

Đây là một điểm nền tảng vì nhiều người nhầm “không đổi theo thời gian” với “không còn quá trình vi mô”.

## Ví dụ động học đơn giản A ⇌ B

Xét phản ứng một bước lý tưởng:

\[
A\rightleftharpoons B
\]

với:

\[
v_f=k_f[A]
\]

\[
v_r=k_r[B]
\]

Tại cân bằng:

\[
k_f[A]_{eq}=k_r[B]_{eq}
\]

suy ra:

\[
\frac{[B]_{eq}}{[A]_{eq}}=\frac{k_f}{k_r}
\]

Trong mô hình lý tưởng đơn giản này:

\[
K_c=\frac{k_f}{k_r}
\]

Quan hệ này rất hữu ích để nối động học với cân bằng, nhưng không nên áp dụng máy móc cho mọi phản ứng tổng. Nếu cơ chế có nhiều bước, rate law phức tạp hoặc hệ không lý tưởng, mối liên hệ giữa các hằng số tốc độ vi mô và `K` cần được xây dựng từ toàn cơ chế.

## Cân bằng từ góc nhìn năng lượng tự do Gibbs

Ở nhiệt độ và áp suất không đổi:

\[
\Delta_rG=\Delta_rG^\circ+RT\ln Q
\]

Nếu:

\[
\Delta_rG<0
\]

một mức tiến triển nhỏ theo chiều thuận làm Gibbs của hệ giảm.

Nếu:

\[
\Delta_rG>0
\]

chiều nghịch làm Gibbs giảm.

Tại cân bằng:

\[
\Delta_rG=0
\]

và:

\[
Q=K
\]

Do đó cân bằng là trạng thái mà không còn dịch chuyển vi phân được phép nào theo tọa độ phản ứng có thể làm giảm Gibbs thêm trong các ràng buộc đang xét.

## Cực tiểu Gibbs và mức tiến triển phản ứng

Gọi \(\xi\) là **mức tiến triển phản ứng (extent of reaction)**:

\[
dn_i=\nu_i d\xi
\]

ở `T,P` không đổi:

\[
\frac{dG}{d\xi}=\Delta_rG
\]

Tại cân bằng:

\[
\frac{dG}{d\xi}=0
\]

Một cân bằng bền còn cần độ cong cục bộ phù hợp để một nhiễu nhỏ không làm hệ tự rời khỏi điểm cân bằng.

Mô hình này cho thấy Le Châtelier, `Q`, `K` và cân bằng pha đều có thể quy về hình dạng của bề mặt Gibbs.

## Cân bằng không có nghĩa 50/50

Tốc độ thuận và nghịch bằng nhau không có nghĩa nồng độ chất phản ứng bằng nồng độ sản phẩm.

Nếu:

\[
K\gg1
\]

cân bằng có thể nghiêng rất mạnh về sản phẩm.

Nếu:

\[
K\ll1
\]

cân bằng có thể nghiêng mạnh về chất phản ứng.

Điều bằng nhau là **động lực ròng** hoặc **tốc độ ròng**, không phải lượng của hai phía.

## Cân bằng khác trạng thái ổn định

Một hệ mở có thể có nồng độ gần không đổi nhưng vẫn có dòng vật chất ròng.

Ví dụ một bể phản ứng liên tục có thể nhận chất phản ứng với đúng tốc độ chúng bị tiêu thụ. Nồng độ trong bể ổn định theo thời gian nhưng hệ không ở cân bằng nhiệt động.

Đó là **trạng thái ổn định (steady state)**.

So sánh:

```text
cân bằng:
không có dòng ròng do driving force nhiệt động

steady state:
có thể có dòng vật chất/năng lượng liên tục
nhưng các biến vĩ mô không đổi theo thời gian
```

Tế bào sống là ví dụ quan trọng của hệ trạng thái ổn định xa cân bằng.

## Vì sao sự sống không ở cân bằng?

Tế bào liên tục:

- nhận chất dinh dưỡng;
- thải sản phẩm;
- duy trì gradient ion;
- thủy phân ATP;
- truyền electron qua chuỗi hô hấp.

Nếu tế bào đạt cân bằng nhiệt động hoàn toàn với môi trường, phần lớn gradient và dòng chuyển hóa cần cho chức năng sống sẽ biến mất.

Sinh học vì vậy hoạt động nhờ **duy trì trạng thái ngoài cân bằng** bằng dòng năng lượng tự do liên tục.

## Cân bằng chi tiết

Trong nhiều hệ ở cân bằng nhiệt động, **cân bằng chi tiết (detailed balance)** nói rằng mỗi quá trình vi mô và quá trình nghịch tương ứng có dòng trung bình cân bằng nhau.

Điều này mạnh hơn chỉ nói tổng tốc độ ròng bằng 0.

Tuy nhiên cần cẩn thận khi áp dụng cho mạng phản ứng được dẫn động bởi ánh sáng, điện trường, dòng vật chất hoặc nguồn năng lượng ngoài. Những hệ ngoài cân bằng có thể có chu trình dòng ròng dù nồng độ trung bình gần ổn định.

## Thuận nghịch vi mô và cơ chế

Nếu một bước cơ bản có thể xảy ra theo chiều thuận, nguyên lý vi mô cho phép chiều nghịch tương ứng khi trạng thái và năng lượng phù hợp.

Nhưng từ đó không được suy ra mọi phương trình phản ứng tổng đều có cơ chế nghịch đơn giản bằng cách “đảo mũi tên”. Cơ chế thực có thể gồm nhiều bước và trung gian khác nhau.

Đây là lý do cân bằng nhiệt động không tự cho cơ chế phản ứng.

## Chất xúc tác làm gì tại cân bằng?

Chất xúc tác tạo con đường phản ứng có hàng rào hoạt hóa thấp hơn.

Nó tăng tốc cả chiều thuận và nghịch theo cách phù hợp với cùng chênh lệch Gibbs đầu–cuối.

Vì vậy chất xúc tác:

```text
làm hệ tới cân bằng nhanh hơn
nhưng không đổi K tại cùng T
```

Nếu quan sát thấy “nhiều sản phẩm hơn” sau khi thêm xúc tác vào một thí nghiệm trước đó chưa đạt cân bằng, đó là vì hệ tiến gần cân bằng nhanh hơn, không phải vì xúc tác đổi vị trí cân bằng.

## Cân bằng vật lý

Cùng logic áp dụng cho chuyển pha.

Lỏng–hơi:

\[
H_2O(l)\rightleftharpoons H_2O(g)
\]

Ở cân bằng, tốc độ bay hơi bằng tốc độ ngưng tụ.

Rắn–dung dịch:

\[
NaCl(s)\rightleftharpoons Na^+(aq)+Cl^-(aq)
\]

Ở dung dịch bão hòa có tinh thể, ion vẫn liên tục rời và quay lại bề mặt tinh thể.

Do đó “bão hòa” không nghĩa các hạt ngừng chuyển động.

## Cân bằng acid–base

Trong nước:

\[
HA+H_2O\rightleftharpoons H_3O^++A^-
\]

proton liên tục được chuyển giữa các tiểu phần. Giá trị `Ka` mô tả thành phần cân bằng, không phải thời gian proton “ở yên” trên một phân tử.

Đây là cầu nối giữa cân bằng động và phần acid–base.

## Cân bằng điện hóa

Ở điện cực hở mạch, phản ứng oxy hóa và khử có thể vẫn xảy ra ở cấp vi mô nhưng dòng Faraday ròng bằng 0.

Thế điện cực cân bằng được xác định bởi Nernst và hoạt độ các tiểu phần.

Khi ta kéo dòng qua điện cực, hệ bị đẩy ra khỏi cân bằng và xuất hiện quá thế.

Vì vậy electrochemistry là một ví dụ rất rõ của sự chuyển từ equilibrium sang nonequilibrium operation.

## Dao động cân bằng

Ở hệ vĩ mô, số hạt rất lớn nên dao động tương đối nhỏ và ta thấy nồng độ gần như cố định.

Ở hệ nano hoặc thí nghiệm đơn phân tử, dao động có thể đủ lớn để quan sát.

Cân bằng nhiệt động vì vậy là trạng thái thống kê, không phải từng vi trạng thái đứng yên.

## Thời gian thư giãn về cân bằng

Sau một nhiễu nhỏ, hệ thường cần thời gian để trở lại cân bằng. Khoảng thời gian đặc trưng đó gọi chung là **thời gian thư giãn (relaxation time)**.

Đo relaxation sau một bước thay đổi nhiệt độ, áp suất hoặc điện trường có thể cung cấp thông tin động học rất nhanh.

Các kỹ thuật relaxation kinetics từng đóng vai trò quan trọng trong nghiên cứu phản ứng nhanh.

## Cân bằng cục bộ

Trong một hệ lớn có gradient nhiệt độ hoặc nồng độ, toàn hệ có thể chưa cân bằng. Tuy nhiên một vùng rất nhỏ đôi khi vẫn có thể được xấp xỉ gần cân bằng nội bộ.

Đó là ý tưởng **cân bằng cục bộ (local equilibrium)** trong nhiệt động lực học không cân bằng.

Nó cho phép dùng các đại lượng như nhiệt độ hay thế hóa học cục bộ trong mô hình truyền nhiệt và truyền khối.

## Ví dụ: bình kín có N₂O₄/NO₂

Bắt đầu với nhiều `N2O4`:

```text
t = 0:
v_thuận lớn
v_nghịch gần 0
```

Theo thời gian:

```text
[N2O4] giảm
[NO2] tăng
v_thuận giảm
v_nghịch tăng
```

Tại cân bằng:

```text
v_thuận = v_nghịch
Q = K
ΔrG = 0
```

Nếu tăng nhiệt độ hoặc thể tích, `Q`, `K` hoặc cả hai có thể thay đổi tùy loại nhiễu; hệ sau đó tiến tới một cân bằng mới.

## Khi nào dùng mô hình cân bằng?

Mô hình cân bằng phù hợp khi thời gian quan sát dài hơn đáng kể thời gian hệ cần để thư giãn về cân bằng.

Nếu phản ứng quá chậm, hệ có thể chưa đạt cân bằng dù trạng thái cân bằng nhiệt động đã xác định rõ.

Ví dụ diamond có thể tồn tại lâu ở điều kiện mà graphite bền hơn nhiệt động vì hàng rào chuyển pha lớn.

Trong hóa phân tích, nhiều phép tính acid–base giả định cân bằng proton nhanh. Với hệ tạo phức chậm hoặc kết tủa chậm, giả định này cần được kiểm tra.

## Các hiểu lầm thường gặp

### “Cân bằng nghĩa chất phản ứng bằng sản phẩm”

Sai. Thành phần cân bằng phụ thuộc `K`.

### “Cân bằng nghĩa phản ứng dừng”

Sai. Hai chiều tiếp tục nhưng tốc độ ròng bằng 0.

### “Nồng độ không đổi luôn nghĩa cân bằng”

Sai. Một hệ mở ở steady state có thể duy trì nồng độ cố định với dòng ròng liên tục.

### “Chất xúc tác làm K lớn hơn”

Sai. Chất xúc tác thay đổi động học, không đổi `K` ở cùng nhiệt độ.

### “ΔG° = 0 tại cân bằng”

Không nhất thiết. Tại cân bằng là \(\Delta_rG=0\). Đại lượng chuẩn \(\Delta_rG^\circ\) chỉ bằng 0 khi `K=1` ở nhiệt độ đó.

### “Cân bằng cho biết tốc độ phản ứng”

Không. `K` cho vị trí cân bằng; động học cho tốc độ tiến tới đó.

## Mô hình tư duy

Cân bằng hóa học nên được hình dung như **một giao điểm giữa động học và nhiệt động lực học**.

```text
phản ứng thuận + phản ứng nghịch
→ thành phần thay đổi
→ Q tiến về K
→ ΔrG tiến về 0
→ tốc độ ròng tiến về 0
```

Nhưng các chuyển đổi vi mô vẫn tiếp tục.

Xem tiếp: [Hằng số cân bằng](./01_equilibrium_constant.md), [Thương số phản ứng](./02_reaction_quotient.md) và [Nhiệt động lực học của cân bằng](./04_thermodynamics_of_equilibrium.md).