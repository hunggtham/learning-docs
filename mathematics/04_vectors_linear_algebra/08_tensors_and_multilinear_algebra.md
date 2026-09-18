# Tensor và multilinear algebra: mở rộng vector, matrix và cách biểu diễn quan hệ nhiều chiều

Vector và matrix thường được học như hai loại object tách biệt: vector là một dãy số, matrix là một bảng số. Cách nhìn này đủ để tính toán, nhưng chưa cho thấy bản chất sâu hơn. Vector mô tả một đại lượng tuyến tính theo một hướng, matrix mô tả một phép biến đổi tuyến tính giữa hai không gian, còn **tensor (텐서)** là cách tổng quát hóa để mô tả quan hệ multilinear giữa nhiều không gian cùng lúc.

Tensor xuất hiện tự nhiên trong cơ học, relativity, computer graphics, signal processing và machine learning. Một ảnh RGB có thể được lưu dưới dạng tensor ba chiều `height × width × channel`; một batch ảnh thêm một chiều nữa; trọng số của neural network cũng thường được lưu dưới dạng tensor. Tuy nhiên, tensor không chỉ đơn giản là “mảng nhiều chiều”. Mảng là representation trong một hệ tọa độ cụ thể; tensor là object toán học tồn tại độc lập với representation đó.

## Từ scalar đến vector, matrix rồi tensor

Một **scalar (스칼라)** là số không phụ thuộc hướng. Có thể xem scalar là tensor bậc 0.

Một vector có các thành phần

```math
v=(v_1,v_2,\dots,v_n)
```

và có thể xem như tensor bậc 1.

Matrix

```math
A=(a_{ij})
```

có hai chỉ số và thường được xem như tensor bậc 2 trong một basis đã chọn. Tensor bậc 3 cần ba chỉ số `T_{ijk}`, bậc 4 cần bốn chỉ số và tương tự.

Điều quan trọng là **rank/order của tensor không đồng nghĩa với matrix rank**. Tensor order nói số lượng indices cần để xác định một component. Matrix rank nói số chiều của image hoặc số lượng direction độc lập mà matrix giữ lại.

## Multilinearity là ý tưởng trung tâm

Một function tuyến tính theo một biến thỏa

```math
f(ax+by)=af(x)+bf(y).
```

Một function **multilinear (다중선형)** nhận nhiều input và tuyến tính theo từng input khi giữ các input còn lại cố định.

Ví dụ inner product

```math
\langle u,v\rangle
```

là bilinear trên không gian thực: cố định `v` thì nó tuyến tính theo `u`, và cố định `u` thì nó tuyến tính theo `v`.

Một bilinear form có thể viết trong tọa độ là

```math
B(u,v)=u^TAv.
```

Matrix `A` ở đây không chỉ là bảng số. Nó là representation của một bilinear object sau khi ta chọn basis.

## Tensor product

Cho hai vector space `V` và `W`. **Tensor product (텐서곱)**, ký hiệu

```math
V\otimes W,
```

là một không gian mới cho phép biểu diễn các kết hợp bilinear của hai không gian dưới dạng object tuyến tính.

Với `u∈V` và `v∈W`, tensor đơn giản

```math
u\otimes v
```

được gọi là simple tensor hoặc rank-one tensor. Nếu

```math
u=(u_1,u_2),\qquad v=(v_1,v_2,v_3),
```

thì representation của `u⊗v` có các component

```math
T_{ij}=u_i v_j.
```

Trong matrix form đây chính là outer product.

```math
u v^T=
\begin{bmatrix}
u_1v_1&u_1v_2&u_1v_3\\
u_2v_1&u_2v_2&u_2v_3
\end{bmatrix}.
```

Không phải tensor nào cũng biểu diễn được bằng đúng một outer product. Nhiều tensor phải là tổng của nhiều simple tensors.

## Basis và components

Giả sử `e_1,...,e_n` là basis của `V`. Vector được viết

```math
v=\sum_i v^i e_i.
```

Một tensor bậc 2 có thể viết

```math
T=\sum_{i,j} T^{ij} e_i\otimes e_j.
```

Các số `T^{ij}` là components phụ thuộc basis. Nếu đổi basis, components đổi theo một quy luật xác định sao cho tensor vật lý hoặc hình học vẫn là cùng object.

Đây là lý do phát biểu “tensor là multidimensional array” chưa đủ. Array chỉ là tập components sau khi basis đã được chọn.

## Covariant và contravariant

Trong geometry và physics ta thường gặp indices trên và dưới, ví dụ

```math
v^i,\qquad \omega_i,\qquad T^i_{\ jk}.
```

Vector thuộc space `V`. Linear functional nhận vector và trả về scalar thuộc **dual space** `V*`. Một element của dual space thường được gọi là covector.

Nếu `ω∈V*`, thì

```math
\omega(v)
```

là scalar. Tensor tổng quát có thể nhận cả vector lẫn covector. Tensor type `(p,q)` có thể hiểu như object có `p` contravariant slots và `q` covariant slots.

Trong Euclidean space với orthonormal basis, distinction này thường bị che khuất vì inner product cho phép chuyển đổi giữa vector và covector. Trong curved coordinates hoặc differential geometry, distinction trở nên quan trọng.

## Contraction

**Tensor contraction (텐서 축약)** là phép tổng theo một cặp indices, làm giảm tensor order.

Matrix multiplication là một ví dụ quen thuộc:

```math
C_{ik}=\sum_j A_{ij}B_{jk}.
```

Index `j` bị contract. Vì vậy matrix multiplication có thể được nhìn như một trường hợp của tensor contraction.

Trace cũng là contraction:

```math
\operatorname{tr}(A)=\sum_i A_{ii}.
```

Trong deep learning, các operations như `einsum` trong NumPy/PyTorch cho phép mô tả trực tiếp contraction bằng notation kiểu Einstein.

## Einstein summation convention

Trong nhiều tài liệu physics và geometry, một index xuất hiện hai lần trong một term được hiểu là tự động sum.

Thay vì viết

```math
y_i=\sum_j A_{ij}x_j,
```

có thể viết

```math
y_i=A_{ij}x_j.
```

Convention này làm các biểu thức tensor gọn hơn và làm rõ indices nào còn lại sau operation.

## Shape trong machine learning

Một tensor trong software thường có một `shape`. Ví dụ embedding batch có shape

```text
(batch, sequence, feature)
```

và attention score có thể có shape

```text
(batch, head, query_position, key_position).
```

Shape giúp biết số components trên từng axis, nhưng không tự cho biết meaning toán học. Hai tensors có cùng shape có thể biểu diễn hoàn toàn khác nhau: ảnh, covariance, activation hay probability table.

Một kỹ năng quan trọng khi đọc model code là luôn gắn mỗi axis với một semantic meaning thay vì chỉ nhìn kích thước.

## Broadcasting không phải tensor algebra thuần túy

Framework numerical thường hỗ trợ broadcasting. Ví dụ tensor shape `(32,128,768)` có thể cộng vector `(768,)`; vector được conceptual repeat trên batch và sequence axes.

Broadcasting là convention của array programming, không phải một phép tensor basis-independent. Nó rất hữu ích trong code nhưng cần phân biệt với tensor contraction, outer product hay coordinate transformation.

## Symmetric và antisymmetric tensors

Tensor bậc 2 symmetric thỏa

```math
T_{ij}=T_{ji}.
```

Covariance matrix, Hessian của function đủ smooth và stress tensor trong nhiều setting là các ví dụ symmetric.

Antisymmetric tensor thỏa

```math
T_{ij}=-T_{ji}.
```

Điều này kéo theo `T_{ii}=0`. Các antisymmetric forms liên quan chặt với orientation, cross product và differential forms.

## Tensor decomposition

Tương tự matrix có SVD, tensor cũng có các decomposition nhằm tách structure thành components đơn giản hơn. Hai ý tưởng thường gặp là CP decomposition và Tucker decomposition.

Mục tiêu có thể là compression, denoising, latent factor discovery hoặc giảm computational cost. Khác matrix SVD, tensor decomposition thường phức tạp hơn và nhiều bài toán không còn closed-form đẹp.

## Tensors và neural networks

Trong neural network, một dense layer cơ bản thực hiện

```math
y=Wx+b.
```

Khi batch nhiều samples được xử lý cùng lúc, `x` trở thành matrix hoặc tensor. Convolution nhận input tensor có spatial dimensions và channels. Transformer vận hành trên tensors có axes cho batch, token, head và feature.

Tuy nhiên core math vẫn quay về các operation tuyến tính, contraction, element-wise nonlinearities và differentiation.

## Mental Model

Hãy hình dung vector là một object có một “slot tuyến tính”, matrix/bilinear form có hai slots, tensor có nhiều slots. Components là cách object đó trông như thế nào khi đặt nó vào một coordinate system cụ thể. Tensor algebra nghiên cứu cách kết hợp, contract và transform các slots này mà không đánh mất structure.

## Common Misconceptions

“Tensor chỉ là array nhiều chiều” là simplification hữu ích khi lập trình nhưng không phải định nghĩa đầy đủ. “Tensor rank” cũng không nên nhầm với matrix rank. Một tensor bậc 3 không có nghĩa rank bằng 3 theo khái niệm matrix rank.

Một nhầm lẫn khác là xem mọi dimension trong tensor software như một spatial dimension toán học. Trong ML, một axis có thể là batch index, token index hoặc category index; meaning đến từ model, không đến từ array shape.

## Liên kết kiến thức

Chapter này nối trực tiếp với [Vector spaces, basis và dimension](./03_vector_spaces_basis_dimension.md), [Linear transformations](./02_linear_transformations.md), [Inner product và projection](./06_inner_product_orthogonality_and_projection.md), và là prerequisite tự nhiên cho [Matrix calculus, Jacobian, Hessian và automatic differentiation](./09_matrix_calculus_jacobian_hessian_and_autodiff.md).