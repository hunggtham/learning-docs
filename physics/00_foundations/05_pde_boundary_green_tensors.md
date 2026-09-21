# Phương pháp Toán cho Vật lý: PDE, điều kiện biên, hàm Green và tensor

## Vì sao phương trình vi phân thường chưa đủ?

Một quỹ đạo chất điểm `x(t)` chỉ phụ thuộc vào thời gian nên thường dẫn tới phương trình vi phân thường (ordinary differential equation, ODE / 상미분방정식). Nhưng rất nhiều đại lượng vật lý là **trường (field)** phụ thuộc đồng thời vào vị trí và thời gian, chẳng hạn nhiệt độ `T(x,y,z,t)`, điện thế `\phi(x,y,z)` hoặc độ lệch sóng `u(x,t)`.

Khi đó, định luật vật lý thường trở thành phương trình vi phân riêng phần (partial differential equation, PDE / 편미분방정식).

Ba họ phương trình xuất hiện lặp lại là

```math
\nabla^2\phi=-\frac{\rho}{\varepsilon_0},
```

là phương trình Poisson trong điện tĩnh;

```math
\frac{\partial u}{\partial t}=D\nabla^2u,
```

là phương trình khuếch tán hoặc dẫn nhiệt;

và

```math
\frac{\partial^2u}{\partial t^2}=c^2\nabla^2u,
```

là phương trình sóng.

Chúng đều chứa toán tử Laplace nhưng có cấu trúc thời gian khác nhau. Vì vậy chúng mô tả hành vi vật lý khác nhau: khuếch tán làm các chênh lệch không gian dần được san bằng, còn phương trình sóng cho phép nhiễu động lan truyền với tốc độ hữu hạn trong mô hình lý tưởng.

## Phương trình không đủ để chọn nghiệm vật lý

Một PDE thường có vô số nghiệm toán học. Phương trình chỉ quy định quan hệ cục bộ giữa trường và các đạo hàm của nó. Nghiệm vật lý cụ thể còn phụ thuộc vào hình học miền, cách hệ được chuẩn bị và cách trường tương tác với biên.

Với phương trình nhiệt, ta có thể cần điều kiện ban đầu

```math
T(\mathbf r,0)=T_0(\mathbf r).
```

Sau đó phải chỉ rõ điều gì xảy ra trên biên của miền.

### Điều kiện Dirichlet

Điều kiện Dirichlet quy định trực tiếp giá trị trường trên biên:

```math
T|_{\partial V}=T_b.
```

Ví dụ, một bề mặt được giữ ở nhiệt độ cố định là bài toán Dirichlet điển hình.

### Điều kiện Neumann

Điều kiện Neumann quy định đạo hàm theo phương pháp tuyến hoặc thông lượng qua biên:

```math
\frac{\partial T}{\partial n}=g.
```

Nếu `g=0`, ta có thể đang mô hình hóa một biên cách nhiệt lý tưởng.

### Điều kiện Robin

Điều kiện Robin kết hợp giá trị trường và đạo hàm pháp tuyến. Trao đổi nhiệt đối lưu với môi trường thường dẫn tới dạng này.

Trong điện tĩnh, vật dẫn được giữ ở điện thế cố định gần với điều kiện Dirichlet, còn điện tích bề mặt cho thông tin về đạo hàm pháp tuyến của điện thế.

Điểm quan trọng là: **điều kiện biên không phải chi tiết phụ của bài toán**. Cùng một PDE nhưng điều kiện biên khác có thể mô tả các hệ vật lý hoàn toàn khác nhau.

## Tách biến và phổ mode tự nhiên

Khi hình học và điều kiện biên đủ đơn giản, ta có thể thử nghiệm dạng tích

```math
u(x,t)=X(x)T(t).
```

Thay vào phương trình sóng hoặc phương trình nhiệt thường tách bài toán thành các ODE với một hằng số phân tách.

Điều kiện biên chỉ cho phép một số giá trị riêng và hàm riêng nhất định. Vì vậy mode chuẩn, sóng dừng và phổ rời rạc có thể xuất hiện ngay trong vật lý cổ điển.

Ví dụ, một sợi dây dài `L` cố định ở hai đầu có

```math
X_n(x)=\sin\frac{n\pi x}{L},
```

với

```math
k_n=\frac{n\pi}{L}.
```

Các số sóng cho phép là rời rạc vì phương trình sóng phải đồng thời thỏa hai điều kiện biên. Do đó, chỉ nhìn thấy một phổ rời rạc chưa đủ để kết luận hệ có bản chất lượng tử.

## Fourier biến đạo hàm thành phép nhân

Một trong những lý do biến đổi Fourier mạnh trong vật lý là đạo hàm trở thành phép nhân trong không gian số sóng:

```math
\frac{d}{dx}
\longleftrightarrow ik,
```

và

```math
\frac{d^2}{dx^2}
\longleftrightarrow -k^2.
```

Với phương trình nhiệt,

```math
\frac{\partial T}{\partial t}=D\nabla^2T,
```

sau biến đổi Fourier theo không gian ta thu được, cho mỗi mode `k`,

```math
\frac{\partial\tilde T}{\partial t}
=-Dk^2\tilde T.
```

Nghiệm là

```math
\tilde T(k,t)=\tilde T(k,0)e^{-Dk^2t}.
```

Mode có `k` lớn tương ứng với cấu trúc không gian nhỏ và sắc. Hệ số suy giảm chứa `k^2`, nên các cấu trúc nhỏ bị làm phẳng nhanh hơn cấu trúc lớn. Đây là lý do toán học khiến khuếch tán có xu hướng làm trường trở nên trơn hơn.

Biến đổi Fourier vì vậy không chỉ là kỹ thuật xử lý tín hiệu. Nó chọn một cơ sở trong đó các toán tử vi phân bất biến tịnh tiến trở nên đặc biệt đơn giản.

## Biến đổi Laplace và bài toán quá độ

Biến đổi Laplace được định nghĩa bởi

```math
F(s)=\int_0^\infty f(t)e^{-st}dt.
```

Nó đặc biệt hữu ích cho hệ tuyến tính có điều kiện ban đầu. Đạo hàm theo thời gian biến thành biểu thức đại số kèm các hạng chứa giá trị ban đầu.

Mạch RC/RLC, hệ điều khiển và quá trình khuếch tán quá độ đều có thể được giải hiệu quả trong không gian Laplace. Cấu trúc này cũng liên hệ trực tiếp với hàm truyền (transfer function) trong kỹ thuật điều khiển.

## Hàm Green: xây nghiệm từ đáp ứng của nguồn điểm

Xét toán tử tuyến tính `L` và phương trình

```math
Lu=f.
```

Hàm Green `G(x,x')` được định nghĩa bởi

```math
LG(x,x')=\delta(x-x')
```

và phải thỏa **cùng loại điều kiện biên** với bài toán vật lý đang xét.

Nếu biết đáp ứng của hệ đối với nguồn delta tại `x'`, nghiệm cho nguồn tổng quát có thể được xây bằng chồng chập:

```math
u(x)=\int G(x,x')f(x')dx'.
```

Đây là cùng mô hình tư duy với đáp ứng xung (impulse response) của một hệ tuyến tính. Trong xử lý tín hiệu, đầu ra của hệ tuyến tính bất biến theo thời gian là tích chập với đáp ứng xung. Trong điện tĩnh, thế Coulomb trong không gian tự do có thể được hiểu như hàm Green của toán tử Laplace.

### Điều cần nhớ về hàm Green

Hàm Green không chỉ phụ thuộc toán tử `L`. Nó còn phụ thuộc miền hình học và điều kiện biên. Vì vậy “hàm Green của Laplacian” không phải duy nhất nếu ta chưa nói rõ bài toán sống trong không gian nào và biên được xử lý ra sao.

## Laplacian và hình học

Laplacian của trường vô hướng là

```math
\nabla^2f=\nabla\cdot\nabla f.
```

Nó đo cách giá trị tại một điểm khác với cấu trúc lân cận theo hình học của không gian. Laplacian xuất hiện trong khuếch tán, điện tĩnh, sóng, động năng lượng tử và đàn hồi vì nhiều định luật phụ thuộc độ cong hoặc độ không đồng đều không gian của trường.

Công thức cụ thể của Laplacian phụ thuộc hệ tọa độ. Trong tọa độ cầu, nó chứa các hạng bán kính và góc. Không thể lấy công thức Descartes rồi thay tùy ý `x,y,z` bằng `r,\theta,\phi`.

## Tensor và quy luật biến đổi

Một vô hướng không đổi khi ta quay hệ tọa độ. Thành phần của vectơ biến đổi với một ma trận quay. Với tensor hạng hai,

```math
T'_{ij}=R_{ik}R_{j\ell}T_{k\ell}.
```

Tensor ứng suất, tensor quán tính, tensor điện môi và metric không-thời gian đều là các ví dụ quan trọng.

Điểm cốt lõi là tensor là một đối tượng hình học có quy luật biến đổi xác định sao cho quan hệ vật lý không phụ thuộc việc ta chọn trục tọa độ nào. Một ma trận chỉ là bảng thành phần của tensor sau khi đã chọn cơ sở.

## Quy ước tổng Einstein

Khi một chỉ số xuất hiện lặp hai lần trong một hạng,

```math
a_ib_i
```

được hiểu là tổng theo `i`.

Ví dụ divergence có thể viết

```math
\partial_iA_i,
```

và phép biến đổi tuyến tính có thể viết

```math
v'_i=R_{ij}v_j.
```

Ký hiệu này làm các biểu thức tensor ngắn hơn và giúp đối xứng của phương trình nổi rõ, đặc biệt trong cơ học liên tục, điện từ học và thuyết tương đối.

## Jacobian và đổi tọa độ

Khi đổi biến trong tích phân, phần tử thể tích phải thay theo định thức Jacobian:

```math
d^nx=|\det J|\,d^nu.
```

Trong tọa độ cầu,

```math
dV=r^2\sin\theta\,dr\,d\theta\,d\phi.
```

Hệ số `r^2\sin\theta` không phải quy ước tùy ý. Nó đo mức độ một phần tử tọa độ nhỏ bị kéo giãn thành thể tích vật lý trong ánh xạ tọa độ cầu.

## Hàm delta Dirac

Delta Dirac `\delta(x)` không phải một hàm thông thường. Nó được xác định thông qua tác dụng dưới dấu tích phân:

```math
\int f(x)\delta(x-x_0)dx=f(x_0).
```

Mật độ điện tích của một điện tích điểm có thể viết

```math
\rho(\mathbf r)=q\delta^{(3)}(\mathbf r-\mathbf r_0).
```

Hàm delta cho phép biểu diễn nguồn định xứ bên trong một phương trình trường liên tục. Nó là công cụ nối mô hình “hạt điểm” với mô tả trường.

## Vô thứ nguyên hóa

Ta có thể đổi thang biến

```math
x=Lx',\qquad t=\tau t'
```

để viết PDE dưới dạng chỉ chứa các tham số vô thứ nguyên.

Các số như Reynolds, Mach hay Péclet cho biết tỉ lệ giữa các cơ chế vật lý cạnh tranh. Sau vô thứ nguyên hóa, một số hạng có thể đi kèm hệ số rất nhỏ hoặc rất lớn, từ đó cho biết cơ chế nào có thể bỏ qua trong một chế độ cụ thể.

Vô thứ nguyên hóa không chỉ làm con số “đẹp” hơn. Nó giúp tìm chế độ chi phối, xây mô hình tương tự và so sánh hai hệ có kích thước tuyệt đối khác nhau.

## Dạng mạnh, dạng yếu và phương pháp phần tử hữu hạn

Dạng mạnh (strong form) của PDE yêu cầu phương trình được thỏa tại từng điểm, nên nghiệm cần đủ trơn để các đạo hàm cần thiết tồn tại.

Dạng yếu (weak form) nhân phương trình với một hàm thử rồi tích phân trên miền. Tích phân từng phần chuyển bớt đạo hàm khỏi nghiệm và tạo ra các hạng biên.

Ví dụ với phương trình Poisson

```math
-\nabla^2u=f,
```

một dạng yếu điển hình có cấu trúc

```math
\int_V \nabla v\cdot\nabla u\,dV
=\int_V vf\,dV+\text{các hạng biên}.
```

Phương pháp phần tử hữu hạn (finite element method, FEM) xấp xỉ `u` bằng một không gian hàm hữu hạn chiều rồi giải dạng yếu. Đây là cầu nối trực tiếp giữa giải tích biến phân, PDE và mô phỏng kỹ thuật kết cấu, nhiệt, điện từ hay chất lưu.

## Kiểm tra đơn vị và điều kiện áp dụng

Các toán tử vi phân mang thứ nguyên. Nếu `x` có đơn vị mét thì `\partial/\partial x` có thứ nguyên `1/m`, còn `\nabla^2` có thứ nguyên `1/m^2`. Vì vậy mọi PDE vật lý phải cân bằng thứ nguyên giữa hai vế.

Khi chọn phương pháp giải, cũng cần kiểm tra giả định. Tách biến đòi hỏi hình học và điều kiện biên tương thích. Biến đổi Fourier thuận lợi nhất khi hệ có tính bất biến tịnh tiến hoặc miền đủ đơn giản. Hàm Green yêu cầu toán tử tuyến tính nếu muốn dùng nguyên lý chồng chập trực tiếp. FEM không tự động đảm bảo nghiệm đúng nếu lưới quá thô hoặc điều kiện biên sai.

## Mô hình tư duy (Mental Model)

ODE mô tả sự tiến hóa của một số hữu hạn bậc tự do; PDE mô tả trường có số bậc tự do liên tục theo không gian. Điều kiện đầu và điều kiện biên chọn nghiệm vật lý; Fourier và hàm riêng chọn cơ sở làm toán tử đơn giản; hàm Green xây đáp ứng tổng quát từ nguồn điểm; tensor giữ định luật độc lập với cách chọn trục tọa độ.

Có thể nhìn chuỗi giải bài như sau:

```text
xác định trường cần tìm
→ viết PDE chi phối
→ xác định miền hình học
→ đặt điều kiện đầu / điều kiện biên
→ chọn cơ sở hoặc phương pháp số phù hợp
→ kiểm tra đơn vị, hội tụ và giới hạn vật lý
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Có PDE là đủ để giải bài”

Không. Điều kiện đầu, điều kiện biên và hình học miền là một phần của chính bài toán vật lý.

### “Tensor chỉ là mảng số nhiều chiều”

Không. Mảng là cấu trúc dữ liệu; tensor vật lý được xác định bởi ý nghĩa hình học và quy luật biến đổi khi đổi cơ sở.

### “Biến đổi Fourier chỉ dùng cho tín hiệu tuần hoàn”

Chuỗi Fourier thích hợp với nhiều bài toán tuần hoàn hoặc miền hữu hạn. Biến đổi Fourier xử lý lớp rộng các hàm và phân bố không tuần hoàn; bài toán biên cũng có thể dùng các khai triển hàm riêng tổng quát hơn.

### “Dùng FEM thì luôn thu được nghiệm đúng”

Không. Kết quả còn phụ thuộc mô hình vật lý, điều kiện biên, loại phần tử, độ mịn lưới, độ ổn định số và kiểm tra hội tụ.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Ngôn ngữ Toán học](03_mathematical_language.md), [Đối xứng, bảo toàn và thang đo](04_symmetry_conservation_scale.md).

**Liên hệ tiếp:** [Tensor ứng suất và cơ học liên tục](../03_continuum/04_continuum_mechanics_stress_tensor.md), [Bài toán biên điện tĩnh](../05_electromagnetism/10_boundary_value_image_multipoles.md), [Maxwell](../05_electromagnetism/04_maxwell_em_waves.md), [Các hệ lượng tử](../08_quantum/01_quantum_systems.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md).
