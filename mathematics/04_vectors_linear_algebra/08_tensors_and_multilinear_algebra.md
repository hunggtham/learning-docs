# Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ scalar đến véc-tơ (vector / 벡터), ma trận (matrix / 행렬) rồi tensor** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Multilinearity là ý tưởng trung tâm** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối tensors với multilinear algebra, để mở rộng vector và ma trận sang nhiều chiều mà vẫn giữ quy tắc biến đổi.

Véc-tơ (vector / 벡터) và ma trận (matrix / 행렬) thường được học như hai loại đối tượng (object / 객체) tách biệt: véc-tơ (vector / 벡터) là một dãy số, ma trận (matrix / 행렬) là một bảng số. Cách nhìn này đủ để tính toán, nhưng chưa cho thấy bản chất sâu hơn. véc-tơ (vector / 벡터) mô tả một đại lượng tuyến tính theo một hướng, ma trận (matrix / 행렬) mô tả một phép biến đổi tuyến tính giữa hai không gian, còn **tensor (텐서)** là cách tổng quát hóa để mô tả quan hệ multilinear giữa nhiều không gian cùng lúc.

Tensor xuất hiện tự nhiên trong cơ học, relativity, computer graphics, tín hiệu (signal / 신호) processing và machine học tập (learning / 학습). Một ảnh RGB có thể được lưu dưới dạng tensor ba chiều `height × width × channel`; một batch ảnh thêm một chiều nữa; trọng số của neural mạng (network / 네트워크) cũng thường được lưu dưới dạng tensor. Tuy nhiên, tensor không chỉ đơn giản là “mảng nhiều chiều”. Mảng là biểu diễn (representation / 표현) trong một hệ tọa độ cụ thể; tensor là đối tượng (object / 객체) toán học tồn tại độc lập với biểu diễn (representation / 표현) đó.

## Từ scalar đến véc-tơ (vector / 벡터), ma trận (matrix / 행렬) rồi tensor

Một **scalar (스칼라)** là số không phụ thuộc hướng. Có thể xem scalar là tensor bậc 0.

Một véc-tơ (vector / 벡터) có các thành phần

```math
v=(v_1,v_2,\dots,v_n)
```

và có thể xem như tensor bậc 1.

Ma trận (matrix / 행렬)

```math
A=(a_{ij})
```

có hai chỉ số và thường được xem như tensor bậc 2 trong một basis đã chọn. Tensor bậc 3 cần ba chỉ số `T_{ijk}`, bậc 4 cần bốn chỉ số và tương tự.

Điều quan trọng là **rank/thứ tự (order / 순서) của tensor không đồng nghĩa với ma trận (matrix / 행렬) rank**. Tensor thứ tự (order / 순서) nói số lượng indices cần để xác định một thành phần (component / 컴포넌트). ma trận (matrix / 행렬) rank nói số chiều của ảnh (image / 이미지) hoặc số lượng direction độc lập mà ma trận (matrix / 행렬) giữ lại.

> **Nối mạch:** Trong **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Multilinearity là ý tưởng trung tâm** nối từ **Từ scalar đến véc-tơ (vector / 벡터), ma trận (matrix / 행렬) rồi tensor** sang **Tensor sản phẩm (product / 제품)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Multilinearity là ý tưởng trung tâm

Một hàm (function / 함수) tuyến tính theo một biến thỏa

```math
f(ax+by)=af(x)+bf(y).
```

Một hàm (function / 함수) **multilinear (다중선형)** nhận nhiều đầu vào (input / 입력) và tuyến tính theo từng đầu vào (input / 입력) khi giữ các đầu vào (input / 입력) còn lại cố định.

Ví dụ inner sản phẩm (product / 제품)

```math
\langle u,v\rangle
```

là bilinear trên không gian thực: cố định `v` thì nó tuyến tính theo `u`, và cố định `u` thì nó tuyến tính theo `v`.

Một bilinear form có thể viết trong tọa độ là

```math
B(u,v)=u^TAv.
```

Ma trận (matrix / 행렬) `A` ở đây không chỉ là bảng số. Nó là biểu diễn (representation / 표현) của một bilinear đối tượng (object / 객체) sau khi ta chọn basis.

> **Nối mạch:** Ở chặng này của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Tensor sản phẩm (product / 제품)** nối từ **Multilinearity là ý tưởng trung tâm** sang **Basis và components**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tensor sản phẩm (product / 제품)

Cho hai véc-tơ (vector / 벡터) không gian (space / 공간) `V` và `W`. **Tensor sản phẩm (product / 제품)**, ký hiệu

```math
V\otimes W,
```

là một không gian mới cho phép biểu diễn các kết hợp bilinear của hai không gian dưới dạng đối tượng (object / 객체) tuyến tính.

Với `u∈V` và `v∈W`, tensor đơn giản

```math
u\otimes v
```

được gọi là simple tensor hoặc rank-one tensor. Nếu

```math
u=(u_1,u_2),\qquad v=(v_1,v_2,v_3),
```

thì biểu diễn (representation / 표현) của `u⊗v` có các thành phần (component / 컴포넌트)

```math
T_{ij}=u_i v_j.
```

Trong ma trận (matrix / 행렬) form đây chính là outer sản phẩm (product / 제품).

```math
u v^T=
\begin{bmatrix}
u_1v_1&u_1v_2&u_1v_3\\
u_2v_1&u_2v_2&u_2v_3
\end{bmatrix}.
```

Không phải tensor nào cũng biểu diễn được bằng đúng một outer sản phẩm (product / 제품). Nhiều tensor phải là tổng của nhiều simple tensors.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Basis và components** nối từ **Tensor sản phẩm (product / 제품)** sang **Covariant và contravariant**, vì cơ chế trước tạo đầu vào cho bước sau.

## Basis và components

Giả sử `e_1,...,e_n` là basis của `V`. véc-tơ (vector / 벡터) được viết

```math
v=\sum_i v^i e_i.
```

Một tensor bậc 2 có thể viết

```math
T=\sum_{i,j} T^{ij} e_i\otimes e_j.
```

Các số `T^{ij}` là components phụ thuộc basis. Nếu đổi basis, components đổi theo một quy luật xác định sao cho tensor vật lý hoặc hình học vẫn là cùng đối tượng (object / 객체).

Đây là lý do phát biểu “tensor là multidimensional array” chưa đủ. Array chỉ là tập components sau khi basis đã được chọn.

> **Nối mạch:** Trong **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Covariant và contravariant** nối từ **Basis và components** sang **Contraction**, vì cơ chế trước tạo đầu vào cho bước sau.

## Covariant và contravariant

Trong hình học (geometry / 기하학) và physics ta thường gặp indices trên và dưới, ví dụ

```math
v^i,\qquad \omega_i,\qquad T^i_{\ jk}.
```

Véc-tơ (vector / 벡터) thuộc không gian (space / 공간) `V`. tuyến tính (linear / 선형) functional nhận véc-tơ (vector / 벡터) và trả về scalar thuộc **dual không gian (space / 공간)** `V*`. Một element của dual không gian (space / 공간) thường được gọi là covector.

Nếu `ω∈V*`, thì

```math
\omega(v)
```

là scalar. Tensor tổng quát có thể nhận cả véc-tơ (vector / 벡터) lẫn covector. Tensor kiểu (type / 타입) `(p,q)` có thể hiểu như đối tượng (object / 객체) có `p` contravariant slots và `q` covariant slots.

Trong Euclidean không gian (space / 공간) với orthonormal basis, distinction này thường bị che khuất vì inner sản phẩm (product / 제품) cho phép chuyển đổi giữa véc-tơ (vector / 벡터) và covector. Trong curved coordinates hoặc differential hình học (geometry / 기하학), distinction trở nên quan trọng.

> **Nối mạch:** Ở chặng này của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Contraction** nối từ **Covariant và contravariant** sang **Einstein summation convention**, vì cơ chế trước tạo đầu vào cho bước sau.

## Contraction

**Tensor contraction (텐서 축약)** là phép tổng theo một cặp indices, làm giảm tensor thứ tự (order / 순서).

Phép nhân ma trận (matrix multiplication / 행렬 곱셈) là một ví dụ quen thuộc:

```math
C_{ik}=\sum_j A_{ij}B_{jk}.
```

Chỉ mục (index / 인덱스) `j` bị đặc tả hợp đồng (contract / 계약). Vì vậy phép nhân ma trận (matrix multiplication / 행렬 곱셈) có thể được nhìn như một trường hợp của tensor contraction.

Dấu vết (trace / 추적) cũng là contraction:

```math
\operatorname{tr}(A)=\sum_i A_{ii}.
```

Trong deep học tập (learning / 학습), các operations như `einsum` trong NumPy/PyTorch cho phép mô tả trực tiếp contraction bằng notation kiểu Einstein.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Einstein summation convention** nối từ **Contraction** sang **Shape trong machine học tập (learning / 학습)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Einstein summation convention

Trong nhiều tài liệu physics và hình học (geometry / 기하학), một chỉ mục (index / 인덱스) xuất hiện hai lần trong một term được hiểu là tự động sum.

Thay vì viết

```math
y_i=\sum_j A_{ij}x_j,
```

có thể viết

```math
y_i=A_{ij}x_j.
```

Convention này làm các biểu thức tensor gọn hơn và làm rõ indices nào còn lại sau thao tác (operation / 연산).

> **Nối mạch:** Trong **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Shape trong machine học tập (learning / 학습)** nối từ **Einstein summation convention** sang **Broadcasting không phải tensor algebra thuần túy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Shape trong machine học tập (learning / 학습)

Một tensor trong software thường có một `shape`. Ví dụ embedding batch có shape

```text
(batch, sequence, feature)
```

và attention score có thể có shape

```text
(batch, head, query_position, key_position).
```

Shape giúp biết số components trên từng axis, nhưng không tự cho biết meaning toán học. Hai tensors có cùng shape có thể biểu diễn hoàn toàn khác nhau: ảnh, covariance, activation hay xác suất (probability / 확률) bảng (table / 테이블).

Một kỹ năng quan trọng khi đọc mô hình (model / 모델) mã (code / 코드) là luôn gắn mỗi axis với một ý nghĩa (semantic meaning / 의미적 뜻) thay vì chỉ nhìn kích thước.

> **Nối mạch:** Ở chặng này của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Broadcasting không phải tensor algebra thuần túy** nối từ **Shape trong machine học tập (learning / 학습)** sang **Symmetric và antisymmetric tensors**, vì cơ chế trước tạo đầu vào cho bước sau.

## Broadcasting không phải tensor algebra thuần túy

Khung phần mềm (framework / 프레임워크) numerical thường hỗ trợ broadcasting. Ví dụ tensor shape `(32,128,768)` có thể cộng véc-tơ (vector / 벡터) `(768,)`; véc-tơ (vector / 벡터) được conceptual repeat trên batch và chuỗi (sequence / 시퀀스) axes.

Broadcasting là convention của array programming, không phải một phép tensor basis-independent. Nó rất hữu ích trong mã (code / 코드) nhưng cần phân biệt với tensor contraction, outer sản phẩm (product / 제품) hay coordinate transformation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Symmetric và antisymmetric tensors** nối từ **Broadcasting không phải tensor algebra thuần túy** sang **Tensor decomposition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Symmetric và antisymmetric tensors

Tensor bậc 2 symmetric thỏa

```math
T_{ij}=T_{ji}.
```

Covariance ma trận (matrix / 행렬), Hessian của hàm (function / 함수) đủ smooth và stress tensor trong nhiều setting là các ví dụ symmetric.

Antisymmetric tensor thỏa

```math
T_{ij}=-T_{ji}.
```

Điều này kéo theo `T_{ii}=0`. Các antisymmetric forms liên quan chặt với orientation, cross sản phẩm (product / 제품) và differential forms.

> **Nối mạch:** Trong **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Tensor decomposition** nối từ **Symmetric và antisymmetric tensors** sang **Tensors và neural networks**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tensor decomposition

Tương tự ma trận (matrix / 행렬) có SVD, tensor cũng có các decomposition nhằm tách cấu trúc (structure / 구조) thành components đơn giản hơn. Hai ý tưởng thường gặp là CP decomposition và Tucker decomposition.

Mục tiêu có thể là compression, denoising, latent factor discovery hoặc giảm computational chi phí (cost / 비용). Khác ma trận (matrix / 행렬) SVD, tensor decomposition thường phức tạp hơn và nhiều bài toán không còn closed-form đẹp.

> **Nối mạch:** Ở chặng này của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Tensors và neural networks** nối từ **Tensor decomposition** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tensors và neural networks

Trong neural mạng (network / 네트워크), một dense tầng (layer / 계층) cơ bản thực hiện

```math
y=Wx+b.
```

Khi batch nhiều samples được xử lý cùng lúc, `x` trở thành ma trận (matrix / 행렬) hoặc tensor. Convolution nhận đầu vào (input / 입력) tensor có spatial dimensions và channels. Transformer vận hành trên tensors có axes cho batch, đơn vị từ (token / 토큰), head và tính năng (feature / 기능).

Tuy nhiên cốt lõi (core / 핵심) math vẫn quay về các thao tác (operation / 연산) tuyến tính, contraction, element-wise nonlinearities và differentiation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Tensors và neural networks** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Hãy hình dung véc-tơ (vector / 벡터) là một đối tượng (object / 객체) có một “slot tuyến tính”, ma trận (matrix / 행렬)/bilinear form có hai slots, tensor có nhiều slots. Components là cách đối tượng (object / 객체) đó trông như thế nào khi đặt nó vào một coordinate hệ thống (system / 시스템) cụ thể. Tensor algebra nghiên cứu cách kết hợp, đặc tả hợp đồng (contract / 계약) và transform các slots này mà không đánh mất cấu trúc (structure / 구조).

> **Nối mạch:** Trong **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

“Tensor chỉ là array nhiều chiều” là simplification hữu ích khi lập trình nhưng không phải định nghĩa đầy đủ. “Tensor rank” cũng không nên nhầm với ma trận (matrix / 행렬) rank. Một tensor bậc 3 không có nghĩa rank bằng 3 theo khái niệm ma trận (matrix / 행렬) rank.

Một nhầm lẫn khác là xem mọi dimension trong tensor software như một spatial dimension toán học. Trong ML, một axis có thể là batch chỉ mục (index / 인덱스), đơn vị từ (token / 토큰) chỉ mục (index / 인덱스) hoặc category chỉ mục (index / 인덱스); meaning đến từ mô hình (model / 모델), không đến từ array shape.

> **Nối mạch:** Ở chặng này của **Tensor và multilinear algebra: mở rộng véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và cách biểu diễn quan hệ nhiều chiều**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức

Chapter này nối trực tiếp với [Vector spaces, basis và dimension](./03_vector_spaces_basis_dimension.md), [Linear transformations](./02_linear_transformations.md), [Inner product và projection](./06_inner_product_orthogonality_and_projection.md), và là prerequisite tự nhiên cho [Matrix calculus, Jacobian, Hessian và automatic differentiation](./09_matrix_calculus_jacobian_hessian_and_autodiff.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
