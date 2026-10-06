# Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ basis đến toàn bộ transformation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vì sao ma trận (matrix / 행렬) biểu diễn (representation / 표현) phụ thuộc basis?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối linear transformations với ma trận, basis và composition, để phép biến đổi được đọc qua tác động lên không gian chứ không chỉ qua công thức.

Phép biến đổi tuyến tính (linear transformation / 선형변환) là một ánh xạ (mapping / 매핑) giữa hai véc-tơ (vector / 벡터) spaces bảo toàn cách chúng ta cộng vectors và quy mô (scale / 규모) bằng scalars. Formal definition thường được viết ngay:

```math
T(u+v)=T(u)+T(v),
```

```math
T(cu)=cT(u).
```

Nhưng intuition nên đến trước: **linearity nghĩa là transformation tôn trọng superposition**. Nếu một trạng thái (state / 상태) được tạo bằng cách trộn các components theo weights nào đó, thì transform whole trạng thái (state / 상태) tương đương transform từng thành phần (component / 컴포넌트) rồi trộn lại với chính weights đó.

Đây là lý do tuyến tính (linear / 선형) các mô hình (models / 모델들) rất mạnh. Ta không cần biết transformation làm gì với vô số vectors; chỉ cần biết nó làm gì với một basis.

## Từ basis đến toàn bộ transformation

Giả sử `V` có basis

```math
v_1,\ldots,v_n.
```

Mọi véc-tơ (vector / 벡터) `x` viết duy nhất thành

```math
x=c_1v_1+\cdots+c_nv_n.
```

Nếu `T` tuyến tính (linear / 선형) thì

```math
T(x)=c_1T(v_1)+\cdots+c_nT(v_n).
```

Vì vậy toàn bộ hành vi (behavior / 동작) của `T` được quyết định bởi images của basis vectors. Đây là lý do finite-dimensional tuyến tính (linear / 선형) transformation có thể được lưu bằng một ma trận (matrix / 행렬).

Nếu dùng tiêu chuẩn (standard / 표준) basis `e_1,...,e_n`, column thứ `j` của ma trận (matrix / 행렬) `A` chính là

```math
Ae_j.
```

Nói cách khác, columns không phải những con số tùy ý: chúng cho biết từng coordinate axis bị gửi đi đâu.

> **Nối mạch:** Trong **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Vì sao ma trận (matrix / 행렬) biểu diễn (representation / 표현) phụ thuộc basis?** nối từ **Từ basis đến toàn bộ transformation** sang **Worked example — rotation như tuyến tính (linear / 선형) transformation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao ma trận (matrix / 행렬) biểu diễn (representation / 표현) phụ thuộc basis?

Transformation là đối tượng (object / 객체) abstract; ma trận (matrix / 행렬) chỉ là biểu diễn (representation / 표현) của nó dưới một pair of bases cụ thể.

Một véc-tơ (vector / 벡터) vật lý có thể giống nhau nhưng coordinates thay đổi khi đổi basis. Tương tự, cùng transformation `T` có ma trận (matrix / 행렬) `A` trong basis này và ma trận (matrix / 행렬) `B` trong basis khác.

Nếu `P` là change-of-basis ma trận (matrix / 행렬) phù hợp thì thường xuất hiện quan hệ (relation / 관계)

```math
B=P^{-1}AP.
```

Hai matrices này look khác nhau nhưng represent cùng operator.

Đây là reason eigenbasis, PCA basis hay Fourier basis quan trọng: chúng không thay đổi underlying đối tượng (object / 객체); chúng chọn coordinate hệ thống (system / 시스템) khiến operator hoặc cấu trúc dữ liệu (data structure / 자료구조) dễ nhìn hơn.

> **Nối mạch:** Ở chặng này của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Vì sao ma trận (matrix / 행렬) biểu diễn (representation / 표현) phụ thuộc basis?** nêu quy tắc; **Worked example — rotation như tuyến tính (linear / 선형) transformation** thử quy tắc trong tình huống, rồi **Kernel: directions nào bị mất?** mở rộng hệ quả.

## Worked example — rotation như tuyến tính (linear / 선형) transformation

Rotation 2D góc `\theta` có ma trận (matrix / 행렬)

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Tại sao columns có form đó? Vì tiêu chuẩn (standard / 표준) basis vectors

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

Đặt hai images đó làm columns, ta nhận ma trận (matrix / 행렬) rotation. Đây là cách derive ma trận (matrix / 행렬) từ hành động (action / 동작) on basis, không cần học thuộc.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Worked example — rotation như tuyến tính (linear / 선형) transformation** nêu quy tắc; **Kernel: directions nào bị mất?** thử quy tắc trong tình huống, rồi **Ảnh (image / 이미지): outputs nào reachable?** mở rộng hệ quả.

## Kernel: directions nào bị mất?

Kernel hoặc null không gian (space / 공간) là

```math
\ker T=\{x:T(x)=0\}.
```

Nếu tồn tại nonzero `x` trong kernel, transformation đã collapse direction đó thành zero. Khi đó hai inputs khác nhau có thể tạo cùng đầu ra (output / 출력):

```math
T(u)=T(v)
\Rightarrow
T(u-v)=0.
```

Nếu kernel chỉ có zero véc-tơ (vector / 벡터), transformation injective.

Kernel vì vậy là **information-loss subspace**.

Ví dụ projection từ `R^3` xuống xy-plane:

```math
T(x,y,z)=(x,y,0)
```

có kernel là toàn bộ z-axis. Mọi khác biệt chỉ theo `z` bị projection xóa hoàn toàn.

> **Nối mạch:** Trong **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Ảnh (image / 이미지): outputs nào reachable?** nối từ **Kernel: directions nào bị mất?** sang **Rank-nullity: accounting của degrees of freedom**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ảnh (image / 이미지): outputs nào reachable?

Ảnh (image / 이미지) là

```math
\operatorname{Im}T=\{T(x):x\in V\}.
```

Trong ma trận (matrix / 행렬) form, ảnh (image / 이미지) là column không gian (space / 공간). Nếu `A:R^n\to R^m`, equation

```math
Ax=b
```

có solution khi và chỉ khi `b` nằm trong ảnh (image / 이미지) của transformation.

Rank chính là dimension của ảnh (image / 이미지):

```math
\operatorname{rank}(T)=\dim(\operatorname{Im}T).
```

Nó đo số independent đầu ra (output / 출력) directions mà transformation có thể tạo.

> **Nối mạch:** Ở chặng này của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Rank-nullity: accounting của degrees of freedom** nối từ **Ảnh (image / 이미지): outputs nào reachable?** sang **Injective, surjective và invertible dưới góc nhìn hình học (geometry / 기하학)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Rank-nullity: accounting của degrees of freedom

Với finite-dimensional `V`:

```math
\dim V
=
\operatorname{rank}T+\operatorname{nullity}T.
```

Đây không chỉ là formula. Nó nói mỗi đầu vào (input / 입력) degree of freedom rơi vào một trong hai loại: hoặc vẫn ảnh hưởng tới đầu ra (output / 출력), hoặc bị collapse vào kernel.

Ví dụ map từ `R^3` xuống plane bằng projection có rank 2 và nullity 1:

```math
3=2+1.
```

Một dimension bị mất, hai dimensions sống sót.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Injective, surjective và invertible dưới góc nhìn hình học (geometry / 기하학)** nối từ **Rank-nullity: accounting của degrees of freedom** sang **Affine transformation khác tuyến tính (linear / 선형) transformation ở đâu?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Injective, surjective và invertible dưới góc nhìn hình học (geometry / 기하학)

Nếu `T:V\to W`:

- injective nghĩa không có thông tin (information / 정보) direction bị mất;
- surjective nghĩa mọi mục tiêu (target / 대상) trong `W` đều reachable;
- bijective nghĩa cả hai điều trên cùng đúng.

Trong finite dimensions bằng nhau, injective và surjective trở thành equivalent. Với square ma trận (matrix / 행렬) `A`, các conditions này tương đương với full rank và invertibility.

Nếu dimensions khác nhau, intuition thay đổi. Map từ `R^3` sang `R^2` không thể injective nếu tuyến tính (linear / 선형), vì phải collapse ít nhất một direction. Map từ `R^2` sang `R^3` không thể surjective, vì ảnh (image / 이미지) tối đa chỉ là 2D subspace.

> **Nối mạch:** Trong **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Affine transformation khác tuyến tính (linear / 선형) transformation ở đâu?** nối từ **Injective, surjective và invertible dưới góc nhìn hình học (geometry / 기하학)** sang **Linearization: vì sao tuyến tính (linear / 선형) transformations còn quan trọng với nonlinear các hệ thống (systems / 시스템들)?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Affine transformation khác tuyến tính (linear / 선형) transformation ở đâu?

Map

```math
T(x)=Ax+b
```

với `b\neq0` không tuyến tính (linear / 선형) vì

```math
T(0)=b\neq0.
```

Nó là affine transformation. hình học (geometry / 기하학) vẫn bảo toàn nhiều structures như straight lines và parallelism, nhưng origin không còn fixed.

Trong machine học tập (learning / 학습), tầng (layer / 계층) thường viết

```math
z=Wx+b.
```

Khung phần mềm (framework / 프레임워크) có thể gọi đây là “tuyến tính (linear / 선형) tầng (layer / 계층)”, nhưng mathematically đó là affine map. Distinction này quan trọng khi lập luận (reasoning / 추론) về composition, symmetries và proofs.

> **Nối mạch:** Ở chặng này của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Linearization: vì sao tuyến tính (linear / 선형) transformations còn quan trọng với nonlinear các hệ thống (systems / 시스템들)?** nối từ **Affine transformation khác tuyến tính (linear / 선형) transformation ở đâu?** sang **Composition và phép nhân ma trận (matrix multiplication / 행렬 곱셈)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Linearization: vì sao tuyến tính (linear / 선형) transformations còn quan trọng với nonlinear các hệ thống (systems / 시스템들)?

Ngay cả khi hệ thống (system / 시스템) nonlinear, hành vi (behavior / 동작) cục bộ (local / 로컬) quanh một điểm (point / 지점) thường được approximate bởi tuyến tính (linear / 선형) map.

Với differentiable hàm (function / 함수)

```math
f:\mathbb R^n\to\mathbb R^m,
```

Jacobian tại `x_0` cho cục bộ (local / 로컬) tuyến tính (linear / 선형) approximation:

```math
f(x_0+\Delta x)
\approx
f(x_0)+J_f(x_0)\Delta x.
```

Vì vậy tuyến tính (linear / 선형) algebra không chỉ áp dụng cho “tuyến tính (linear / 선형) world”. Nó là first-order ngôn ngữ (language / 언어) để hiểu nonlinear các hệ thống (systems / 시스템들) locally.

Đây là cầu nối (bridge / 브리지) tới multivariable calculus, tối ưu hóa (optimization / 최적화), điều khiển (control / 제어) và neural-network backpropagation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Composition và phép nhân ma trận (matrix multiplication / 행렬 곱셈)** nối từ **Linearization: vì sao tuyến tính (linear / 선형) transformations còn quan trọng với nonlinear các hệ thống (systems / 시스템들)?** sang **Eigenvectors: directions transformation không đổi hướng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Composition và phép nhân ma trận (matrix multiplication / 행렬 곱셈)

Nếu `T:V\to W` và `S:W\to U` đều tuyến tính (linear / 선형), composition `S\circ T` cũng tuyến tính (linear / 선형).

Trong coordinates:

```math
[T]=A,\qquad [S]=B,
```

thì

```math
[S\circ T]=BA.
```

Thứ tự (order / 순서) phản ánh tiến trình (process / 프로세스) thứ tự (order / 순서). Apply `T` trước, rồi `S`; ma trận (matrix / 행렬) sản phẩm (product / 제품) vì vậy đọc từ right sang left khi acting on vectors.

> **Nối mạch:** Trong **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Eigenvectors: directions transformation không đổi hướng** nối từ **Composition và phép nhân ma trận (matrix multiplication / 행렬 곱셈)** sang **Physics liên kết (connection / 연결) — superposition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Eigenvectors: directions transformation không đổi hướng

Nếu

```math
Av=\lambda v,
```

thì direction `v` được transformation giữ nguyên, chỉ quy mô (scale / 규모) bởi `\lambda`.

Eigenvectors là natural directions của operator. Trong eigenbasis phù hợp, repeated ứng dụng (application / 애플리케이션) của transformation có thể trở nên rất đơn giản:

```math
A^k=P D^k P^{-1}.
```

Đây là reason eigen-analysis xuất hiện trong động (dynamic / 동적) các hệ thống (systems / 시스템들), Markov chains, PCA, vibrations và stability.

> **Nối mạch:** Ở chặng này của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, sau nội dung của **Eigenvectors: directions transformation không đổi hướng**, **Physics liên kết (connection / 연결) — superposition** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **AI liên kết (connection / 연결) — representations và cục bộ (local / 로컬) hình học (geometry / 기하학)** mở rộng hệ quả hoặc giới hạn liên quan.

## Physics liên kết (connection / 연결) — superposition

Tuyến tính (linear / 선형) differential equations và tuyến tính (linear / 선형) transformations chia sẻ superposition principle. Nếu phản hồi (response / 응답) với đầu vào (input / 입력) `u` là `T(u)` và phản hồi (response / 응답) với `v` là `T(v)`, thì phản hồi (response / 응답) với `au+bv` là

```math
T(au+bv)=aT(u)+bT(v).
```

Điều này cho phép phân rã signals thành modes, frequencies hoặc basis states, xử lý từng thành phần (component / 컴포넌트) rồi combine lại. Fourier phân tích (analysis / 분석) dựa sâu vào lô-gic (logic / 논리) này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **AI liên kết (connection / 연결) — representations và cục bộ (local / 로컬) hình học (geometry / 기하학)** nối từ **Physics liên kết (connection / 연결) — superposition** sang **Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## AI liên kết (connection / 연결) — representations và cục bộ (local / 로컬) hình học (geometry / 기하학)

Embeddings là vectors; weight matrices transform representations giữa tính năng (feature / 기능) spaces. Attention dùng projections như `W_Qx`, `W_Kx`, `W_Vx`. Backpropagation repeatedly composes cục bộ (local / 로컬) tuyến tính (linear / 선형) maps represented by Jacobians.

Nhưng whole neural mạng (network / 네트워크) nonlinear vì có activations. tuyến tính (linear / 선형) transformations vẫn là building blocks và cục bộ (local / 로컬) sensitivity operators.

> **Nối mạch:** Trong **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)** nối từ **AI liên kết (connection / 연결) — representations và cục bộ (local / 로컬) hình học (geometry / 기하학)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)

Linearity là giả định (assumption / 가정) mạnh. Nếu doubling đầu vào (input / 입력) không roughly double đầu ra (output / 출력), hoặc interactions giữa features tạo nonlinear effects, tuyến tính (linear / 선형) map có thể không mô hình (model / 모델) hệ thống (system / 시스템) globally.

Một coordinate ma trận (matrix / 행렬) cũng không có intrinsic meaning nếu basis không rõ. Hai teams có thể lưu cùng geometric operator bằng matrices khác nhau vì convention axis/thứ tự (order / 순서) khác nhau.

Trong numerical công việc (work / 작업), transformation có thể mathematically invertible nhưng practically unstable nếu near-singular. Structural lý thuyết (theory / 이론) cần đi cùng conditioning.

> **Nối mạch:** Ở chặng này của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> tuyến tính (linear / 선형) transformation là một machine tôn trọng mixtures. Vì mọi véc-tơ (vector / 벡터) là mixture của basis vectors, chỉ cần biết machine làm gì với basis là đủ. Kernel nói thông tin (information / 정보) nào bị mất; ảnh (image / 이미지) nói outputs nào reachable; ma trận (matrix / 행렬) là coordinate encoding của machine; đổi basis là đổi cách mô tả chứ không đổi machine.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phép biến đổi tuyến tính: cấu trúc, basis và thông tin (information / 정보) luồng (flow / 흐름)**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“ma trận (matrix / 행렬) chính là transformation.”** Không hoàn toàn. ma trận (matrix / 행렬) là biểu diễn (representation / 표현) của transformation dưới chosen bases.

**“Có `b` term vẫn là tuyến tính (linear / 선형).”** `Ax+b` với `b\neq0` là affine, vì origin không map về origin.

**“Rank chỉ là số nonzero rows sau elimination.”** Đó là cách tính. Meaning sâu hơn là dimension của reachable đầu ra (output / 출력) không gian (space / 공간).

**“mô hình tuyến tính (linear model / 선형 모델) nghĩa line thẳng trong mọi ngữ cảnh (context / 맥락).”** Không. tuyến tính (linear / 선형) map giữa high-dimensional véc-tơ (vector / 벡터) spaces có thể represent rotations, projections, shears, filters và many operators phức tạp.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
