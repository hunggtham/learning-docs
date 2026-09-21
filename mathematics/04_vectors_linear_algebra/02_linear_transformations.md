# Phép biến đổi tuyến tính: cấu trúc, basis và information flow

Phép biến đổi tuyến tính (linear transformation / 선형변환) là một mapping giữa hai vector spaces bảo toàn cách chúng ta cộng vectors và scale bằng scalars. Formal definition thường được viết ngay:

```math
T(u+v)=T(u)+T(v),
```

```math
T(cu)=cT(u).
```

Nhưng intuition nên đến trước: **linearity nghĩa là transformation tôn trọng superposition**. Nếu một state được tạo bằng cách trộn các components theo weights nào đó, thì transform whole state tương đương transform từng component rồi trộn lại với chính weights đó.

Đây là lý do linear models rất mạnh. Ta không cần biết transformation làm gì với vô số vectors; chỉ cần biết nó làm gì với một basis.

## Từ basis đến toàn bộ transformation

Giả sử `V` có basis

```math
v_1,\ldots,v_n.
```

Mọi vector `x` viết duy nhất thành

```math
x=c_1v_1+\cdots+c_nv_n.
```

Nếu `T` linear thì

```math
T(x)=c_1T(v_1)+\cdots+c_nT(v_n).
```

Vì vậy toàn bộ behavior của `T` được quyết định bởi images của basis vectors. Đây là lý do finite-dimensional linear transformation có thể được lưu bằng một matrix.

Nếu dùng standard basis `e_1,...,e_n`, column thứ `j` của matrix `A` chính là

```math
Ae_j.
```

Nói cách khác, columns không phải những con số tùy ý: chúng cho biết từng coordinate axis bị gửi đi đâu.

## Vì sao matrix representation phụ thuộc basis?

Transformation là object abstract; matrix chỉ là representation của nó dưới một pair of bases cụ thể.

Một vector vật lý có thể giống nhau nhưng coordinates thay đổi khi đổi basis. Tương tự, cùng transformation `T` có matrix `A` trong basis này và matrix `B` trong basis khác.

Nếu `P` là change-of-basis matrix phù hợp thì thường xuất hiện relation

```math
B=P^{-1}AP.
```

Hai matrices này look khác nhau nhưng represent cùng operator.

Đây là reason eigenbasis, PCA basis hay Fourier basis quan trọng: chúng không thay đổi underlying object; chúng chọn coordinate system khiến operator hoặc data structure dễ nhìn hơn.

## Worked example — rotation như linear transformation

Rotation 2D góc `\theta` có matrix

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Tại sao columns có form đó? Vì standard basis vectors

```math
e_1=(1,0),\qquad e_2=(0,1)
```

sau rotation trở thành

```math
T(e_1)=(\cos\theta,\sin\theta),
```

```math
T(e_2)=(-\sin\theta,\cos\theta).
```

Đặt hai images đó làm columns, ta nhận matrix rotation. Đây là cách derive matrix từ action on basis, không cần học thuộc.

## Kernel: directions nào bị mất?

Kernel hoặc null space là

```math
\ker T=\{x:T(x)=0\}.
```

Nếu tồn tại nonzero `x` trong kernel, transformation đã collapse direction đó thành zero. Khi đó hai inputs khác nhau có thể tạo cùng output:

```math
T(u)=T(v)
\Rightarrow
T(u-v)=0.
```

Nếu kernel chỉ có zero vector, transformation injective.

Kernel vì vậy là **information-loss subspace**.

Ví dụ projection từ `R^3` xuống xy-plane:

```math
T(x,y,z)=(x,y,0)
```

có kernel là toàn bộ z-axis. Mọi khác biệt chỉ theo `z` bị projection xóa hoàn toàn.

## Image: outputs nào reachable?

Image là

```math
\operatorname{Im}T=\{T(x):x\in V\}.
```

Trong matrix form, image là column space. Nếu `A:R^n\to R^m`, equation

```math
Ax=b
```

có solution khi và chỉ khi `b` nằm trong image của transformation.

Rank chính là dimension của image:

```math
\operatorname{rank}(T)=\dim(\operatorname{Im}T).
```

Nó đo số independent output directions mà transformation có thể tạo.

## Rank-nullity: accounting của degrees of freedom

Với finite-dimensional `V`:

```math
\dim V
=
\operatorname{rank}T+\operatorname{nullity}T.
```

Đây không chỉ là formula. Nó nói mỗi input degree of freedom rơi vào một trong hai loại: hoặc vẫn ảnh hưởng tới output, hoặc bị collapse vào kernel.

Ví dụ map từ `R^3` xuống plane bằng projection có rank 2 và nullity 1:

```math
3=2+1.
```

Một dimension bị mất, hai dimensions sống sót.

## Injective, surjective và invertible dưới góc nhìn geometry

Nếu `T:V\to W`:

- injective nghĩa không có information direction bị mất;
- surjective nghĩa mọi target trong `W` đều reachable;
- bijective nghĩa cả hai điều trên cùng đúng.

Trong finite dimensions bằng nhau, injective và surjective trở thành equivalent. Với square matrix `A`, các conditions này tương đương với full rank và invertibility.

Nếu dimensions khác nhau, intuition thay đổi. Map từ `R^3` sang `R^2` không thể injective nếu linear, vì phải collapse ít nhất một direction. Map từ `R^2` sang `R^3` không thể surjective, vì image tối đa chỉ là 2D subspace.

## Affine transformation khác linear transformation ở đâu?

Map

```math
T(x)=Ax+b
```

với `b\neq0` không linear vì

```math
T(0)=b\neq0.
```

Nó là affine transformation. Geometry vẫn bảo toàn nhiều structures như straight lines và parallelism, nhưng origin không còn fixed.

Trong machine learning, layer thường viết

```math
z=Wx+b.
```

Framework có thể gọi đây là “linear layer”, nhưng mathematically đó là affine map. Distinction này quan trọng khi reasoning về composition, symmetries và proofs.

## Linearization: vì sao linear transformations còn quan trọng với nonlinear systems?

Ngay cả khi system nonlinear, behavior local quanh một point thường được approximate bởi linear map.

Với differentiable function

```math
f:\mathbb R^n\to\mathbb R^m,
```

Jacobian tại `x_0` cho local linear approximation:

```math
f(x_0+\Delta x)
\approx
f(x_0)+J_f(x_0)\Delta x.
```

Vì vậy linear algebra không chỉ áp dụng cho “linear world”. Nó là first-order language để hiểu nonlinear systems locally.

Đây là bridge tới multivariable calculus, optimization, control và neural-network backpropagation.

## Composition và matrix multiplication

Nếu `T:V\to W` và `S:W\to U` đều linear, composition `S\circ T` cũng linear.

Trong coordinates:

```math
[T]=A,\qquad [S]=B,
```

thì

```math
[S\circ T]=BA.
```

Order phản ánh process order. Apply `T` trước, rồi `S`; matrix product vì vậy đọc từ right sang left khi acting on vectors.

## Eigenvectors: directions transformation không đổi hướng

Nếu

```math
Av=\lambda v,
```

thì direction `v` được transformation giữ nguyên, chỉ scale bởi `\lambda`.

Eigenvectors là natural directions của operator. Trong eigenbasis phù hợp, repeated application của transformation có thể trở nên rất đơn giản:

```math
A^k=P D^k P^{-1}.
```

Đây là reason eigen-analysis xuất hiện trong dynamic systems, Markov chains, PCA, vibrations và stability.

## Physics connection — superposition

Linear differential equations và linear transformations chia sẻ superposition principle. Nếu response với input `u` là `T(u)` và response với `v` là `T(v)`, thì response với `au+bv` là

```math
T(au+bv)=aT(u)+bT(v).
```

Điều này cho phép phân rã signals thành modes, frequencies hoặc basis states, xử lý từng component rồi combine lại. Fourier analysis dựa sâu vào logic này.

## AI connection — representations và local geometry

Embeddings là vectors; weight matrices transform representations giữa feature spaces. Attention dùng projections như `W_Qx`, `W_Kx`, `W_Vx`. Backpropagation repeatedly composes local linear maps represented by Jacobians.

Nhưng whole neural network nonlinear vì có activations. Linear transformations vẫn là building blocks và local sensitivity operators.

## Failure modes và assumptions

Linearity là assumption mạnh. Nếu doubling input không roughly double output, hoặc interactions giữa features tạo nonlinear effects, linear map có thể không model system globally.

Một coordinate matrix cũng không có intrinsic meaning nếu basis không rõ. Hai teams có thể lưu cùng geometric operator bằng matrices khác nhau vì convention axis/order khác nhau.

Trong numerical work, transformation có thể mathematically invertible nhưng practically unstable nếu near-singular. Structural theory cần đi cùng conditioning.

## Mental Model

> Linear transformation là một machine tôn trọng mixtures. Vì mọi vector là mixture của basis vectors, chỉ cần biết machine làm gì với basis là đủ. Kernel nói information nào bị mất; image nói outputs nào reachable; matrix là coordinate encoding của machine; đổi basis là đổi cách mô tả chứ không đổi machine.

## Common Misconceptions

**“Matrix chính là transformation.”** Không hoàn toàn. Matrix là representation của transformation dưới chosen bases.

**“Có `b` term vẫn là linear.”** `Ax+b` với `b\neq0` là affine, vì origin không map về origin.

**“Rank chỉ là số nonzero rows sau elimination.”** Đó là cách tính. Meaning sâu hơn là dimension của reachable output space.

**“Linear model nghĩa line thẳng trong mọi context.”** Không. Linear map giữa high-dimensional vector spaces có thể represent rotations, projections, shears, filters và many operators phức tạp.