# Ma trận hóa lượng và mạng phản ứng — từ một phương trình hóa học tới hệ phản ứng phức tạp

> Hóa lượng (stoichiometry / 화학량론) thường được học qua từng phương trình riêng lẻ. Nhưng trong hệ thực tế — chuyển hóa sinh học, cháy, khí quyển, pin, reactor công nghiệp — hàng chục tới hàng nghìn phản ứng xảy ra đồng thời. Khi đó cách nhìn từng phương trình một trở nên khó kiểm soát. **Ma trận hóa lượng (stoichiometric matrix)** cung cấp một ngôn ngữ toán học thống nhất để biểu diễn bảo toàn vật chất và cấu trúc của cả mạng phản ứng.

Chương này nối trực tiếp [phương trình hóa học](./02_chemical_equations.md), [hóa lượng](./03_stoichiometry.md), [động học](../06_chemical_kinetics/00_reaction_rates.md), [cân bằng](../07_chemical_equilibrium/00_dynamic_equilibrium.md) và [chuyển hóa sinh học](../13_biochemistry/06_metabolism_and_bioenergetics.md).

# Từ một phản ứng tới vector hóa lượng

Xét phản ứng:

\[
2H_2+O_2\rightarrow2H_2O
\]

Nếu sắp thứ tự các chất là:

```text
H2, O2, H2O
```

ta có thể biểu diễn phản ứng bằng vector hệ số:

\[
\boldsymbol\nu=
\begin{bmatrix}
-2\\
-1\\
+2
\end{bmatrix}
\]

Quy ước:

- hệ số âm cho chất phản ứng;
- hệ số dương cho sản phẩm.

Vector này không mô tả tốc độ hay cơ chế; nó chỉ mô tả **mối quan hệ bảo toàn về lượng** khi phản ứng tiến thêm một mức xác định.

# Mức tiến triển phản ứng

**Mức tiến triển phản ứng (extent of reaction, \(\xi\))** là biến đo phản ứng đã tiến được bao xa.

Với chất \(i\):

\[
dn_i=\nu_i\,d\xi
\]

Nếu tích phân từ trạng thái đầu:

\[
n_i=n_{i,0}+\nu_i\xi
\]

Đây là cách viết rất mạnh vì chỉ cần một biến \(\xi\) là có thể cập nhật toàn bộ lượng chất của một phản ứng đơn lẻ.

Ví dụ với:

\[
N_2+3H_2\rightarrow2NH_3
\]

nếu phản ứng tiến \(0.50\) mol theo mức tiến triển:

\[
\Delta n_{N_2}=-0.50
\]

\[
\Delta n_{H_2}=-1.50
\]

\[
\Delta n_{NH_3}=+1.00
\]

Hóa lượng vì vậy có thể được xem như phép biến đổi tuyến tính theo biến tiến triển.

# Nhiều phản ứng — ma trận hóa lượng

Giả sử có hai phản ứng:

\[
A+B\rightarrow C
\]

\[
C\rightarrow D+E
\]

Sắp các chất theo hàng:

```text
A, B, C, D, E
```

và phản ứng theo cột, ma trận hóa lượng là:

\[
S=
\begin{bmatrix}
-1 & 0\\
-1 & 0\\
+1 & -1\\
0 & +1\\
0 & +1
\end{bmatrix}
\]

Nếu vector mức tiến triển là:

\[
\boldsymbol\xi=
\begin{bmatrix}
\xi_1\\
\xi_2
\end{bmatrix}
\]

thì lượng chất thay đổi:

\[
\Delta\mathbf n=S\boldsymbol\xi
\]

Đây là bước chuyển từ hóa lượng thủ công sang đại số tuyến tính.

# Vì sao ma trận này quan trọng?

Nó cho phép ta trả lời có hệ thống:

- chất nào được tạo hoặc tiêu thụ bởi phản ứng nào;
- có bao nhiêu phản ứng độc lập;
- đại lượng nào được bảo toàn;
- mạng có chu trình kín không;
- phản ứng nào phụ thuộc tuyến tính vào phản ứng khác;
- tốc độ tạo chất liên hệ thế nào với tốc độ phản ứng.

Trong hệ lớn, các câu hỏi này rất khó xử lý bằng quan sát trực tiếp danh sách phương trình.

# Bảo toàn nguyên tố dưới dạng ma trận

Gọi \(E\) là ma trận thành phần nguyên tố, trong đó mỗi hàng là một nguyên tố và mỗi cột là một chất.

Nếu phản ứng bảo toàn nguyên tử, phải có:

\[
ES=0
\]

Ý nghĩa: khi ma trận hóa lượng tác động lên vector phản ứng, tổng số nguyên tử của mỗi nguyên tố không thay đổi.

Đây là cách đại số tuyến tính diễn đạt định luật bảo toàn khối lượng.

Ví dụ nếu có C, H, O trong mạng phản ứng hữu cơ, mỗi phản ứng hợp lệ phải nằm trong **không gian null (null space)** của ràng buộc nguyên tố.

# Cân bằng phương trình bằng đại số tuyến tính

Xét phản ứng chưa cân bằng:

\[
C_3H_8+O_2\rightarrow CO_2+H_2O
\]

Gọi hệ số là:

\[
x_1C_3H_8+x_2O_2\rightarrow x_3CO_2+x_4H_2O
\]

Bảo toàn từng nguyên tố tạo hệ:

\[
3x_1-x_3=0
\]

\[
8x_1-2x_4=0
\]

\[
2x_2-2x_3-x_4=0
\]

Đây là hệ phương trình tuyến tính đồng nhất. Một nghiệm tỉ lệ là:

\[
(x_1,x_2,x_3,x_4)=(1,5,3,4)
\]

Vì vậy cân bằng phản ứng thực chất là bài toán tìm một vector trong không gian nghiệm của ma trận bảo toàn.

# Tốc độ phản ứng và tốc độ tạo chất

Nếu mỗi phản ứng có tốc độ \(v_j\), tập hợp thành vector:

\[
\mathbf v=
\begin{bmatrix}
v_1\\
v_2\\
\vdots\\
v_r
\end{bmatrix}
\]

thì tốc độ thay đổi nồng độ của các chất:

\[
\frac{d\mathbf c}{dt}=S\mathbf v
\]

Đây là một trong những phương trình trung tâm của động học mạng phản ứng.

Ma trận \(S\) chứa **cấu trúc hóa lượng**, còn \(\mathbf v\) chứa **động học**.

Hai phần nên được tách rõ:

```text
S = ai biến thành ai theo tỉ lệ nào
v = mỗi phản ứng đang chạy nhanh bao nhiêu
```

# Ví dụ hai phản ứng nối tiếp

\[
A\xrightarrow{k_1}B\xrightarrow{k_2}C
\]

Ma trận:

\[
S=
\begin{bmatrix}
-1&0\\
+1&-1\\
0&+1
\end{bmatrix}
\]

Nếu:

\[
v_1=k_1[A],\qquad v_2=k_2[B]
\]

thì:

\[
\frac{d}{dt}
\begin{bmatrix}
[A]\\
[B]\\
[C]
\end{bmatrix}
=
\begin{bmatrix}
-1&0\\
+1&-1\\
0&+1
\end{bmatrix}
\begin{bmatrix}
k_1[A]\\
k_2[B]
\end{bmatrix}
\]

Suy ra:

\[
\frac{d[A]}{dt}=-k_1[A]
\]

\[
\frac{d[B]}{dt}=k_1[A]-k_2[B]
\]

\[
\frac{d[C]}{dt}=k_2[B]
\]

Một ma trận nhỏ đã tự động sinh ra toàn bộ hệ phương trình vi phân.

# Phản ứng độc lập và hạng của ma trận

Nếu một phản ứng có thể được tạo bằng tổ hợp tuyến tính của các phản ứng khác, nó không thêm một hướng hóa lượng độc lập mới.

**Hạng (rank)** của ma trận \(S\) cho biết số hướng phản ứng độc lập theo nghĩa tuyến tính.

Điều này quan trọng khi:

- giảm mô hình;
- phát hiện phản ứng dư thừa;
- chọn biến trạng thái độc lập;
- kiểm tra tính nhất quán của mạng.

# Đại lượng bảo toàn từ null space bên trái

Nếu tồn tại vector \(\mathbf l\) sao cho:

\[
\mathbf l^TS=0
\]

thì:

\[
\mathbf l^T\mathbf n=\text{hằng số}
\]

Đây là một **đại lượng bảo toàn (conserved quantity)**.

Ví dụ đơn giản, tổng số nguyên tử carbon trong hệ kín là một đại lượng bảo toàn.

Trong mạng sinh hóa, các “moiety” như tổng NAD + NADH hoặc tổng adenylate trong mô hình kín có thể tạo các ràng buộc bảo toàn gần tương tự.

# Chu trình phản ứng

Nếu tồn tại vector dòng phản ứng \(\mathbf v\neq0\) sao cho:

\[
S\mathbf v=0
\]

thì hệ có thể có một **chu trình nội tại**: phản ứng vẫn xảy ra nhưng nồng độ tổng thể không đổi.

Điều này rất quan trọng trong chuyển hóa và phân tích trạng thái ổn định.

Tuy nhiên một chu trình toán học không nhất thiết khả thi về nhiệt động. Cần thêm ràng buộc năng lượng tự do và chiều phản ứng.

# Trạng thái ổn định không phải cân bằng

Tại **trạng thái ổn định (steady state)**:

\[
\frac{d\mathbf c}{dt}=0
\]

nên:

\[
S\mathbf v=0
\]

Nhưng \(\mathbf v\) không nhất thiết bằng 0.

Nghĩa là các phản ứng có thể chạy liên tục, chỉ là lượng tạo và tiêu thụ của mỗi chất trung gian cân bằng nhau.

Đây là khác biệt cốt lõi với **cân bằng nhiệt động**, nơi các dòng thuận và nghịch không tạo dòng ròng duy trì bởi nguồn năng lượng ngoài.

Tế bào sống là ví dụ điển hình của hệ trạng thái ổn định xa cân bằng.

# Flux Balance Analysis

Trong sinh hóa hệ thống, **phân tích cân bằng dòng (flux balance analysis, FBA)** dùng:

\[
S\mathbf v=0
\]

cùng các giới hạn:

\[
v_{min}\le v\le v_{max}
\]

rồi tối ưu một hàm mục tiêu, ví dụ tốc độ tạo sinh khối:

\[
\max\;\mathbf c^T\mathbf v
\]

Đây là một bài toán quy hoạch tuyến tính.

FBA không cần biết đầy đủ hằng số động học của từng enzyme, nhưng đổi lại nó mô tả một không gian dòng khả thi chứ không tự cho cơ chế động học theo thời gian.

# Vì sao FBA hữu ích nhưng có giới hạn

Ưu điểm:

- xử lý mạng hàng nghìn phản ứng;
- dùng trực tiếp bảo toàn hóa lượng;
- không cần mọi hằng số động học;
- phù hợp phân tích trạng thái ổn định.

Giới hạn:

- phụ thuộc cấu trúc mạng;
- phụ thuộc giới hạn dòng;
- hàm mục tiêu có thể không phản ánh sinh học thật;
- không mô tả tự nhiên động lực học quá độ;
- không tự đảm bảo tính khả thi nhiệt động nếu thiếu ràng buộc bổ sung.

# Ma trận hóa lượng trong kỹ thuật phản ứng

Trong reactor hóa học, có thể viết cân bằng vật chất tổng quát:

\[
\frac{d\mathbf n}{dt}
=\mathbf F_{in}-\mathbf F_{out}+S\mathbf rV
\]

Trong đó:

- \(\mathbf F_{in}\): dòng vào;
- \(\mathbf F_{out}\): dòng ra;
- \(\mathbf r\): tốc độ phản ứng trên thể tích;
- \(V\): thể tích reactor.

Một phương trình này bao quát batch, CSTR và nhiều mô hình reactor khi thêm điều kiện phù hợp.

# Liên hệ với combustion và khí quyển

Cơ chế cháy có thể có hàng trăm species và hàng nghìn elementary reactions.

Mỗi bước thêm một cột vào \(S\); toàn hệ động học vẫn có dạng:

\[
\frac{d\mathbf c}{dt}=S\mathbf v(\mathbf c,T)
\]

Điều khó không còn là “cân bằng một phản ứng” mà là:

- tính tốc độ hàng nghìn phản ứng;
- xử lý hệ ODE cứng;
- bảo toàn nguyên tố;
- giải nhiệt độ đồng thời;
- giảm cơ chế mà vẫn giữ hành vi quan trọng.

# Hệ phương trình cứng

Nếu một số phản ứng xảy ra trong microsecond còn phản ứng khác mất giây hoặc phút, hệ có nhiều thang thời gian.

Khi đó hệ ODE có thể **cứng (stiff)** và phương pháp tích phân số đơn giản cần bước thời gian cực nhỏ để ổn định.

Đây là lý do chemistry simulation thường dùng các solver chuyên cho stiff systems.

# Ma trận Jacobian

Với:

\[
\frac{d\mathbf c}{dt}=\mathbf f(\mathbf c)
\]

Jacobian:

\[
J_{ij}=\frac{\partial f_i}{\partial c_j}
\]

mô tả mức một thay đổi nhỏ của species \(j\) ảnh hưởng tốc độ của species \(i\).

Jacobian quan trọng trong:

- ổn định số;
- phân tích sensitivity;
- tìm trạng thái ổn định;
- tối ưu mô hình động học.

# Sensitivity — phản ứng nào thực sự quan trọng?

Trong mạng lớn, không phải mọi hằng số tốc độ đều ảnh hưởng đầu ra như nhau.

Phân tích độ nhạy hỏi:

\[
\frac{\partial y}{\partial k_j}
\]

với \(y\) là đại lượng quan tâm và \(k_j\) là tham số phản ứng.

Nếu một phản ứng có độ nhạy rất nhỏ, nó có thể ít quan trọng trong điều kiện đó dù vẫn tồn tại trong cơ chế.

Đây là nền tảng của **giảm cơ chế (mechanism reduction)**.

# Định danh tham số và vấn đề nghịch đảo

Trong thực nghiệm, ta thường đo nồng độ theo thời gian rồi suy ngược hằng số tốc độ.

Đây là bài toán nghịch đảo:

```text
tham số động học
→ mô hình ODE
→ dữ liệu dự đoán
```

và ta muốn đi ngược từ dữ liệu về tham số.

Hai bộ tham số khác nhau có thể tạo đường cong gần giống nhau. Khi đó tham số **không nhận dạng tốt (poorly identifiable)**.

Tăng số phép đo không phải lúc nào cũng giải quyết được; cần đo đúng species và điều kiện làm các tham số tạo hiệu ứng khác nhau.

# Bảo toàn là công cụ kiểm tra mô hình

Sau khi mô phỏng, nên kiểm tra:

- tổng nguyên tố có được bảo toàn không;
- điện tích có hợp lý không;
- nồng độ có âm không;
- phản ứng thuận/nghịch có chiều hợp lý không;
- tổng lượng trong hệ kín có trôi số học không.

Một solver cho ra đường cong “đẹp” nhưng vi phạm bảo toàn là dấu hiệu lỗi mô hình hoặc lỗi số.

# Biểu diễn phản ứng như graph và hypergraph

Có thể xem mạng phản ứng dưới dạng graph, nhưng phản ứng thường có nhiều chất đầu vào và đầu ra nên **hypergraph** là biểu diễn tự nhiên hơn.

- species là nút;
- reaction là hyperedge nối nhiều reactant với nhiều product.

Cách nhìn này kết nối chemistry với:

- graph algorithms;
- dependency analysis;
- shortest-path synthesis;
- pathway enumeration;
- network centrality.

# Từ hóa lượng tới reaction informatics

Trong cơ sở dữ liệu phản ứng, máy tính cần biết:

- atom mapping;
- reactant/product identity;
- stoichiometric coefficients;
- charge;
- stereochemistry;
- reagents/catalysts;
- conditions.

Nếu phương trình không được cân bằng hoặc atom mapping sai, mô hình reaction prediction có thể học tín hiệu không hóa học.

Do đó hóa lượng là lớp kiểm tra chất lượng dữ liệu trước cả machine learning.

# Một ví dụ tích hợp: lên men glucose

Một mô hình tổng thể rất thô:

\[
C_6H_{12}O_6\rightarrow2C_2H_5OH+2CO_2
\]

Ở cấp hóa lượng, phương trình chỉ nói quan hệ mol.

Ở cấp mạng thực:

```text
glucose
→ glycolysis
→ pyruvate
→ acetaldehyde
→ ethanol
```

cùng hàng chục chất trung gian, ATP, NADH/NAD⁺ và enzyme.

Ma trận hóa lượng cho phép mở rộng từ phản ứng tổng thể sang mạng chi tiết mà vẫn giữ ràng buộc nguyên tố và cofactor.

# Những hiểu lầm thường gặp

### “Ma trận hóa lượng là một cách cân bằng phản ứng phức tạp hơn”

Không chỉ vậy. Nó là biểu diễn cấu trúc của toàn mạng phản ứng.

### “Nếu \(S\mathbf v=0\) thì hệ ở cân bằng”

Không. Đây có thể chỉ là trạng thái ổn định với dòng phản ứng khác 0.

### “Biết ma trận \(S\) là biết động học”

Không. \(S\) chỉ cho cấu trúc hóa lượng; cần hàm tốc độ \(\mathbf v\).

### “Một mô hình có nhiều phản ứng hơn luôn chính xác hơn”

Không. Mạng lớn nhưng tham số kém, phản ứng dư thừa hoặc dữ liệu không đủ có thể khó dự đoán hơn.

### “FBA dự đoán tốc độ enzyme trực tiếp”

Không. Nó tìm dòng phản ứng thỏa bảo toàn và ràng buộc dưới giả định trạng thái ổn định.

# Mô hình tư duy

Hãy hình dung ma trận hóa lượng như **bộ khung bảo toàn của một mạng phản ứng**. Nó không quyết định mạng chạy nhanh bao nhiêu, nhưng xác định những hướng biến đổi nào được phép. Động học đặt tốc độ lên các hướng đó; nhiệt động lực học giới hạn chiều và mức thuận lợi; dữ liệu thực nghiệm xác định tham số; toán học và lập trình giúp giải hệ khi số phản ứng vượt quá khả năng xử lý thủ công.

Xem tiếp: [Động học phản ứng](../06_chemical_kinetics/00_reaction_rates.md), [Cơ chế phản ứng](../06_chemical_kinetics/02_reaction_mechanisms.md), [Chuyển hóa và năng lượng sinh học](../13_biochemistry/06_metabolism_and_bioenergetics.md), [Hóa học và khoa học máy tính](../90_connections/chemistry_and_computer_science.md).
