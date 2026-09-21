# Hóa lượng — định lượng phản ứng từ các định luật bảo toàn

> **Hóa lượng (stoichiometry / 화학량론)** là ngôn ngữ định lượng của phản ứng hóa học. Nó dùng phương trình cân bằng để liên hệ lượng các chất thông qua bảo toàn nguyên tử, điện tích và khối lượng. Bản chất của hóa lượng không phải một tập công thức đổi gram–mol, mà là **một hệ ràng buộc tuyến tính giữa các lượng chất**.

Ở mức cơ bản, ta dùng tỉ lệ mol. Ở mức sâu hơn, cùng tư duy được mở rộng thành **mức tiến triển phản ứng (extent of reaction)**, vector hệ số hóa lượng và ma trận stoichiometric cho cả mạng phản ứng.

# Chuỗi chuyển đổi nền tảng

Hầu hết bài toán đơn phản ứng có dạng:

```text
đại lượng đo của A
→ mol A
→ tỉ lệ hóa lượng
→ mol B
→ đại lượng cần tìm của B
```

Khối lượng, thể tích khí, nồng độ, số hạt hoặc điện lượng chỉ là những cách khác nhau để ánh xạ về lượng chất.

Mol đóng vai trò **đơn vị trung gian chung** vì phương trình hóa học đếm các thực thể theo tỉ lệ.

# Tỉ lệ mol xuất phát từ hệ số phương trình

Với:

\[
N_2+3H_2\rightarrow2NH_3
\]

hệ số cho:

\[
1\ mol\ N_2:3\ mol\ H_2:2\ mol\ NH_3
\]

Nếu có \(4.0\;mol\;N_2\) và \(H_2\) dư:

\[
4.0\,mol\,N_2\times\frac{2\,mol\,NH_3}{1\,mol\,N_2}
=8.0\,mol\,NH_3
\]

Phân số chuyển đổi này không phải công thức cần học thuộc; nó chỉ là cách viết lại tỉ lệ của phương trình.

# Hệ số hóa lượng có dấu

Một cách mô tả mạnh hơn là dùng **hệ số hóa lượng có dấu \(\nu_i\)**:

- chất phản ứng: \(\nu_i<0\);
- sản phẩm: \(\nu_i>0\).

Với phản ứng Haber:

\[
\nu_{N_2}=-1,\qquad\nu_{H_2}=-3,\qquad\nu_{NH_3}=+2
\]

Cách ký hiệu này cho phép viết toàn bộ thay đổi lượng chất bằng một công thức duy nhất.

# Mức tiến triển phản ứng

**Mức tiến triển phản ứng (extent of reaction, \(\xi\))** định nghĩa:

\[
dn_i=\nu_i\,d\xi
\]

Nếu hệ số không đổi và xét từ trạng thái đầu:

\[
n_i=n_{i,0}+\nu_i\xi
\]

Đây là một biểu thức rất quan trọng vì nó tách hai thứ:

- hóa lượng nằm trong \(\nu_i\);
- mức phản ứng thực sự đã tiến bao xa nằm trong \(\xi\).

Ví dụ với:

\[
N_2+3H_2\rightarrow2NH_3
\]

nếu \(\xi=2\;mol\):

\[
\Delta n_{N_2}=-2,
\quad
\Delta n_{H_2}=-6,
\quad
\Delta n_{NH_3}=+4\;mol
\]

# Vì sao extent tốt hơn “mẹo tỉ lệ”?

Tỉ lệ mol rất tiện cho một bài toán đơn giản. Nhưng \(\xi\) giúp xử lý:

- chất phản ứng giới hạn;
- cân bằng hóa học;
- nhiều phản ứng đồng thời;
- reactor liên tục;
- dữ liệu động học;
- tối ưu quá trình.

Nó là cầu nối giữa hóa lượng phổ thông và kỹ thuật phản ứng.

# Ví dụ khối lượng → khối lượng

Đốt methane:

\[
CH_4+2O_2\rightarrow CO_2+2H_2O
\]

Với \(16.0\;g\;CH_4\), \(O_2\) dư:

\[
16.0\,g\,CH_4
\times\frac{1\,mol\,CH_4}{16.04\,g\,CH_4}
\times\frac{1\,mol\,CO_2}{1\,mol\,CH_4}
\times\frac{44.01\,g\,CO_2}{1\,mol\,CO_2}
\]

cho khoảng:

\[
43.9\;g\;CO_2
\]

Chuỗi đơn vị:

```text
g CH4 → mol CH4 → mol CO2 → g CO2
```

là một phép kiểm logic rất mạnh. Nếu đơn vị không triệt tiêu như mong đợi, cấu trúc suy luận có vấn đề.

# Hóa lượng khí

Với khí lý tưởng:

\[
PV=nRT
\]

nên ở cùng \(T\) và \(P\), thể tích tỉ lệ với mol.

Với:

\[
2H_2+O_2\rightarrow2H_2O(g)
\]

ở cùng điều kiện khí, tỉ lệ thể tích là:

\[
2:1:2
\]

Nhưng nếu nước ngưng tụ thành lỏng, không thể dùng trực tiếp tỉ lệ thể tích khí sau phản ứng.

Khi điều kiện nhiệt độ/áp suất khác nhau, phải chuyển về mol qua phương trình trạng thái.

# Hóa lượng dung dịch

Với molarity:

\[
C=\frac{n}{V}
\]

nên:

\[
n=CV
\]

Ví dụ \(25.00\;mL\) HCl \(0.1000\;mol/L\):

\[
n=0.1000\times0.02500
=2.500\times10^{-3}\;mol
\]

Nếu trung hòa NaOH theo tỉ lệ 1:1 thì cần cùng số mol \(OH^-\).

Điểm cần nhớ là molarity dùng **thể tích dung dịch**, không phải thể tích dung môi.

# Hóa lượng và điện lượng

Trong điện hóa:

\[
Q=n_eF
\]

Nếu phản ứng điện cực cần \(z\) electron cho mỗi mol sản phẩm:

\[
n_{product}=\frac{Q}{zF}
\]

Như vậy điện lượng cũng chỉ là một “cổng vào” khác để đi tới mol.

Điều này nối hóa lượng với điện phân, pin và coulometry.

# Chất phản ứng giới hạn qua extent

Với mỗi chất phản ứng:

\[
\xi_{max,i}=\frac{n_{i,0}}{|\nu_i|}
\]

Giá trị nhỏ nhất đặt trần cho phản ứng nếu giả định một phản ứng duy nhất tiến hoàn toàn theo chiều thuận.

Đây chính là ý nghĩa sâu của mẹo “chia số mol cho hệ số rồi chọn nhỏ nhất”.

# Hóa lượng không quyết định phản ứng có đi tới hoàn toàn hay không

Với:

\[
A\rightleftharpoons B
\]

hóa lượng chỉ nói:

\[
n_A=n_{A,0}-\xi
\]

\[
n_B=n_{B,0}+\xi
\]

Giá trị cân bằng của \(\xi\) lại do:

\[
Q(\xi)=K
\]

quyết định.

Do đó:

- hóa lượng = ràng buộc bảo toàn;
- cân bằng = trạng thái dừng nhiệt động;
- động học = tốc độ tiến tới trạng thái đó.

Ba tầng này phải được phân biệt.

# Conversion, yield và selectivity

Trong hệ có phản ứng phụ, “phần trăm hiệu suất” một con số có thể không đủ.

## Độ chuyển hóa

Với chất A:

\[
X_A=\frac{n_{A,0}-n_A}{n_{A,0}}
\]

cho biết phần A đã phản ứng.

## Độ chọn lọc

Nếu A tạo sản phẩm mong muốn P và phụ phẩm U, có thể định nghĩa chọn lọc theo mol hoặc carbon tùy bài toán.

Một dạng đơn giản:

\[
S_{P/U}=\frac{n_P}{n_U}
\]

sau khi hiệu chỉnh theo hóa lượng nếu cần.

## Hiệu suất tạo sản phẩm

Một định nghĩa thường dùng:

\[
Y_P\sim X_A\times\text{phần A đã phản ứng đi tới P}
\]

Các ngành khác nhau có thể dùng quy ước yield/selectivity khác, vì vậy luôn phải đọc định nghĩa trước khi so số liệu.

# Vì sao conversion cao chưa chắc tốt?

Giả sử:

```text
A → P   mong muốn
A → U   phụ phẩm
```

Nếu catalyst làm A phản ứng hết nhưng chủ yếu tạo U, conversion gần 100% nhưng hiệu quả quy trình vẫn thấp.

Trong công nghiệp, tăng **selectivity** đôi khi quan trọng hơn tăng conversion vì phụ phẩm làm mất nguyên liệu và tăng gánh nặng tinh chế.

# Cân bằng nguyên tố — phép kiểm mạnh nhất

Nếu một hệ chỉ chứa C, H, O, ta có thể kiểm tra độc lập:

\[
n_C^{in}=n_C^{out}
\]

\[
n_H^{in}=n_H^{out}
\]

\[
n_O^{in}=n_O^{out}
\]

Nếu dữ liệu sản phẩm chứa nhiều carbon hơn tổng carbon đầu vào, chắc chắn có:

- sai số đo;
- thiếu dòng đầu vào;
- sai công thức;
- hoặc sai mô hình phản ứng.

Bảo toàn nguyên tố không cần biết cơ chế phản ứng. Vì thế nó là phép kiểm dữ liệu rất mạnh.

# Ma trận thành phần và cân bằng phương trình

Có thể biểu diễn thành phần nguyên tố bằng ma trận \(A\), còn vector hệ số hóa lượng là \(\boldsymbol{\nu}\).

Điều kiện bảo toàn nguyên tố:

\[
A\boldsymbol{\nu}=0
\]

Nói cách khác, vector phản ứng nằm trong **không gian null (null space)** của ma trận thành phần.

Đây là lý do cân bằng phương trình hóa học có thể được giải bằng đại số tuyến tính.

# Ma trận stoichiometric của mạng phản ứng

Nếu có nhiều phản ứng, ta gom hệ số thành ma trận \(S\):

\[
\mathbf n=\mathbf n_0+S\boldsymbol\xi
\]

trong đó mỗi cột của \(S\) là một phản ứng và \(\boldsymbol\xi\) chứa mức tiến triển của các phản ứng.

Trong động học:

\[
\frac{d\mathbf n}{dt}=S\mathbf r
\]

với \(\mathbf r\) là vector tốc độ phản ứng.

Đây là một trong những cấu trúc toán học quan trọng nhất nối hóa lượng với:

- mô hình reactor;
- chuyển hóa sinh học;
- combustion;
- atmospheric chemistry;
- flux balance analysis.

# Ví dụ mạng phản ứng

Giả sử:

\[
A\rightarrow B
\]

\[
B\rightarrow C
\]

Ma trận cho thứ tự species \([A,B,C]\):

\[
S=
\begin{bmatrix}
-1 & 0\\
1 & -1\\
0 & 1
\end{bmatrix}
\]

Nếu \(\xi_1\) và \(\xi_2\) lần lượt là mức tiến triển:

\[
\begin{bmatrix}
n_A\\n_B\\n_C
\end{bmatrix}
=
\begin{bmatrix}
n_{A,0}\\n_{B,0}\\n_{C,0}
\end{bmatrix}
+
S
\begin{bmatrix}
\xi_1\\\xi_2
\end{bmatrix}
\]

Cấu trúc này vẫn đúng dù động học phức tạp; chỉ giá trị \(\xi\) thay đổi theo thời gian.

# Cân bằng vật chất trong hệ dòng liên tục

Với một thiết bị quá trình:

\[
\text{tích lũy}
=
\text{vào}
-
\text{ra}
+
\text{sinh do phản ứng}
-
\text{tiêu thụ do phản ứng}
\]

Ở trạng thái ổn định:

\[
\text{tích lũy}=0
\]

Hóa lượng phản ứng cung cấp hạng sinh/tiêu thụ.

Đây là cách tư duy stoichiometric mở rộng từ cốc thí nghiệm sang dây chuyền công nghiệp.

# Recycle, purge và bypass

Trong quá trình có tuần hoàn, chất chưa phản ứng có thể được tách và đưa trở lại reactor.

Nhưng tạp trơ có thể tích lũy trong vòng recycle, nên cần một dòng **purge** để tránh nồng độ tăng vô hạn.

Bài toán khi đó không còn chỉ “mol A tạo mol B”, mà là cân bằng toàn hệ nhiều dòng.

Tuy nhiên nền tảng vẫn là bảo toàn và ma trận hóa lượng.

# Độ không đảm bảo trong bài toán hóa lượng

Giá trị đầu vào có thể gồm:

- khối lượng;
- độ tinh khiết;
- nồng độ;
- thể tích;
- nhiệt độ/áp suất;
- hiệu suất thu hồi.

Nếu kết quả:

\[
y=f(x_1,x_2,\ldots)
\]

thì độ không đảm bảo phải được truyền từ các đầu vào.

Ví dụ:

\[
n=\frac{mP}{M}
\]

với \(P\) là độ tinh khiết. Nếu cân cực chính xác nhưng assay \(P\) chỉ biết tới 1%, độ tinh khiết sẽ chi phối độ không đảm bảo mol.

# Chữ số có nghĩa không đủ cho hóa lượng định lượng nghiêm ngặt

Quy tắc chữ số có nghĩa là công cụ giáo dục hữu ích, nhưng không thay thế propagation of uncertainty.

Trong công việc phân tích, cần giữ thêm chữ số trong tính toán trung gian rồi làm tròn kết quả theo độ không đảm bảo cuối.

# Kiểm tra bằng giới hạn vật lý

Ngoài cân bằng nguyên tố, nên hỏi:

- sản phẩm có vượt lượng tối đa theo chất giới hạn không?
- conversion có >100% không?
- tổng mol carbon có được bảo toàn không?
- khối lượng đầu ra có phù hợp khối lượng đầu vào?

Các kiểm tra giới hạn đơn giản thường bắt lỗi tốt hơn việc chỉ nhìn phép tính chi tiết.

# Liên hệ với lập trình

Một hệ stoichiometric có thể được mô hình hóa bằng:

```text
species
+ composition matrix
+ reaction matrix
+ unit conversions
+ constraints
```

Phần mềm có thể:

- cân bằng phương trình;
- tìm chất giới hạn;
- kiểm tra bảo toàn;
- giải mức tiến triển;
- mô phỏng mạng phản ứng;
- cảnh báo dữ liệu không khả thi.

Đây là ví dụ rõ ràng nơi hóa học trở thành bài toán dữ liệu có cấu trúc.

# Những hiểu lầm thường gặp

### “Hệ số stoichiometric là số gram”

Không. Nó là tỉ lệ thực thể/mol; khối lượng xuất hiện sau khi nhân khối lượng mol.

### “Phương trình cân bằng nghĩa các chất đều phản ứng hết”

Không. Cân bằng chỉ bảo toàn; extent thực tế còn do giới hạn nguồn lực, cân bằng và động học.

### “Yield thấp nghĩa hóa lượng sai”

Không. Yield phản ánh quá trình thật, còn hệ số hóa lượng là ràng buộc phương trình.

### “Một phản ứng phức tạp luôn xử lý bằng một tỉ lệ mol duy nhất”

Không. Mạng nhiều phản ứng cần nhiều extent hoặc ma trận stoichiometric.

### “Conversion cao nghĩa quy trình tốt”

Không nếu selectivity thấp hoặc chi phí tách quá lớn.

# Mô hình tư duy

Hóa lượng là **hình học tuyến tính của bảo toàn vật chất**. Với một phản ứng, nó xuất hiện như tỉ lệ mol; với nhiều phản ứng, nó trở thành vector và ma trận. Mol là ngôn ngữ trung gian, còn extent cho biết hệ đã di chuyển bao xa dọc theo các hướng phản ứng được phép.

Xem tiếp: [Chất phản ứng giới hạn và hiệu suất](./04_limiting_reagent_and_yield.md).