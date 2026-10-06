# Mômen động lượng lượng tử, spin và phép cộng mômen động lượng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**. Route đi từ rotation generators → commutators/eigenvalues → orbital angular momentum → spin-1/2 → angular-momentum addition, để đối xứng quay nối toán tử với quan sát.

Mômen động lượng trong cơ học lượng tử không chỉ là phiên bản lượng tử của đại lượng cổ điển `\mathbf L=\mathbf r\times\mathbf p`. Nó là một ví dụ điển hình cho cách **đối xứng quay (rotational symmetry)** được mã hóa thành cấu trúc toán tử, trị riêng và quy tắc ghép trạng thái.

Spin còn đi xa hơn: nó là mômen động lượng nội tại, không có mô hình cổ điển đơn giản tương đương.

## Từ mômen động lượng cổ điển đến toán tử lượng tử

Trong cơ học cổ điển,

```math
\mathbf L=\mathbf r\times\mathbf p.
```

Trong cơ học lượng tử, các thành phần trở thành toán tử và thỏa các quan hệ giao hoán

```math
[L_x,L_y]=i\hbar L_z,
```

cùng các hoán vị vòng:

```math
[L_y,L_z]=i\hbar L_x,
```

```math
[L_z,L_x]=i\hbar L_y.
```

Do các thành phần không giao hoán, ta không thể có một trạng thái có đồng thời `L_x`, `L_y`, `L_z` đều xác định chính xác.

Tuy nhiên,

```math
[L^2,L_z]=0,
```

nên ta có thể chọn trạng thái riêng chung của `L^2` và `L_z`.

> **Nối mạch:** Trong **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Trị riêng của L^2 và Lz** nối từ **Từ mômen động lượng cổ điển đến toán tử lượng tử** sang **Vì sao chỉ đo được một thành phần cùng với L^2?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Trị riêng của `L^2` và `L_z`

Ta viết

```math
L^2|\ell,m\rangle
=\hbar^2\ell(\ell+1)|\ell,m\rangle,
```

và

```math
L_z|\ell,m\rangle
=\hbar m|\ell,m\rangle.
```

Với mômen động lượng quỹ đạo,

```math
\ell=0,1,2,\ldots
```

và

```math
m=-\ell,-\ell+1,\ldots,+\ell.
```

Do đó độ lớn của mômen động lượng không phải

```math
L=\hbar\ell,
```

mà là

```math
|\mathbf L|=\hbar\sqrt{\ell(\ell+1)}.
```

Đây là khác biệt quan trọng giữa trực giác cổ điển và cấu trúc lượng tử.

> **Nối mạch:** Ở chặng này của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Vì sao chỉ đo được một thành phần cùng với L^2?** nối từ **Trị riêng của L^2 và Lz** sang **Toán tử nâng và hạ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao chỉ đo được một thành phần cùng với `L^2`?

Nếu `L_x`, `L_y`, `L_z` cùng xác định chính xác, commutator giữa chúng phải không gây bất định (uncertainty / 불확실성) bắt buộc. Nhưng quan hệ giao hoán cho thấy các thành phần ngang không thể đồng thời có phân bố tùy ý hẹp.

Ta thường chọn trục `z` chỉ vì một hệ tọa độ cần một trục tham chiếu. Nếu hệ không có trường ngoài phá đối xứng, không có hướng `z` nào “cơ bản hơn” các hướng khác.

Khi đặt từ trường ngoài, trục của từ trường trở thành hướng vật lý đặc biệt và `m` có thể liên hệ trực tiếp với năng lượng (energy / 에너지) splitting.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Toán tử nâng và hạ** nối từ **Vì sao chỉ đo được một thành phần cùng với L^2?** sang **Mômen động lượng quỹ đạo và spherical harmonics**, vì cơ chế trước tạo đầu vào cho bước sau.

## Toán tử nâng và hạ

Định nghĩa

```math
L_\pm=L_x\pm iL_y.
```

Ta có

```math
[L_z,L_\pm]=\pm\hbar L_\pm.
```

Nếu `|\ell,m\rangle` là trạng thái riêng của `L_z`, thì

```math
L_+|\ell,m\rangle
\propto |\ell,m+1\rangle,
```

và

```math
L_-|\ell,m\rangle
\propto |\ell,m-1\rangle.
```

Hệ số chính xác là

```math
L_\pm|\ell,m\rangle
=
\hbar\sqrt{\ell(\ell+1)-m(m\pm1)}
|\ell,m\pm1\rangle.
```

Ladder không thể tăng hoặc giảm vô hạn vì norm của trạng thái phải không âm. Chuỗi phải dừng tại

```math
m=+\ell
```

và

```math
m=-\ell.
```

Từ algebra này xuất hiện cấu trúc lượng tử hóa của `m` và trị riêng `\ell(\ell+1)\hbar^2`.

Điểm quan trọng là lượng tử hóa không được gắn bằng tay; nó xuất hiện từ symmetry algebra và điều kiện trạng thái vật lý.

> **Nối mạch:** Trong **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Mômen động lượng quỹ đạo và spherical harmonics** nối từ **Toán tử nâng và hạ** sang **Spin là gì?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mômen động lượng quỹ đạo và spherical harmonics

Trong bài toán có đối xứng cầu, phần góc của hàm sóng được mô tả bằng spherical harmonics

```math
Y_\ell^m(\theta,\phi).
```

Chúng là trạng thái riêng của `L^2` và `L_z`:

```math
L^2Y_\ell^m
=\hbar^2\ell(\ell+1)Y_\ell^m,
```

```math
L_zY_\ell^m
=\hbar mY_\ell^m.
```

Đây là lý do các số lượng tử `\ell,m` xuất hiện tự nhiên trong nguyên tử hydro.

Spherical harmonics không phải “hình dạng orbital” theo nghĩa vật chất đặc. Chúng mô tả cấu trúc góc của biên độ xác suất.

> **Nối mạch:** Ở chặng này của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Spin là gì?** nối từ **Mômen động lượng quỹ đạo và spherical harmonics** sang **Spin-1/2**, vì cơ chế trước tạo đầu vào cho bước sau.

## Spin là gì?

Spin (spin / 스핀) là **mômen động lượng nội tại (intrinsic angular momentum)**.

Electron có

```math
s=\frac12.
```

Nhưng không nên hình dung electron như một quả cầu nhỏ quay quanh trục. Nếu cố ép mô hình đó thành vật thể cổ điển, ta gặp nhiều mâu thuẫn và không tái tạo được cấu trúc spinor.

Spin là một degree of freedom lượng tử được xác định bởi cách trạng thái biến đổi dưới phép quay.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Spin-1/2** nối từ **Spin là gì?** sang **Ma trận Pauli**, vì cơ chế trước tạo đầu vào cho bước sau.

## Spin-1/2

Với spin `1/2`, phép đo thành phần theo một trục chỉ cho hai giá trị:

```math
S_z=\pm\frac{\hbar}{2}.
```

Ta thường ký hiệu

```math
|\uparrow\rangle,
\qquad
|\downarrow\rangle.
```

Một trạng thái spin thuần tổng quát là

```math
|\psi\rangle
=\alpha|\uparrow\rangle
+\beta|\downarrow\rangle,
```

với

```math
|\alpha|^2+|\beta|^2=1.
```

Đây là hệ lượng tử hai mức đơn giản nhất và là prototype của qubit.

> **Nối mạch:** Trong **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Ma trận Pauli** nối từ **Spin-1/2** sang **Bloch sphere**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ma trận Pauli

Các toán tử spin có thể viết

```math
S_i=\frac{\hbar}{2}\sigma_i,
```

với

```math
\sigma_x=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
```

```math
\sigma_y=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix},
```

```math
\sigma_z=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
```

Các ma trận này thỏa

```math
[\sigma_i,\sigma_j]
=2i\epsilon_{ijk}\sigma_k.
```

Chúng là biểu diễn `2×2` cơ bản của algebra spin-1/2.

> **Nối mạch:** Ở chặng này của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Bloch sphere** nối từ **Ma trận Pauli** sang **Phép quay và nhóm SU(2)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bloch sphere

Một trạng thái spin-1/2 thuần có thể viết, bỏ qua toàn cục (global / 전역) phase,

```math
|\psi\rangle
=
\cos\frac{\theta}{2}|\uparrow\rangle
+e^{i\phi}
\sin\frac{\theta}{2}|\downarrow\rangle.
```

Cặp góc `\theta,\phi` biểu diễn một điểm trên Bloch sphere.

Bloch sphere không có nghĩa spin là một véc-tơ (vector / 벡터) cổ điển thực sự nằm trên mặt cầu. Nó là hình học của không gian trạng thái hai mức sau khi bỏ toàn cục (global / 전역) phase.

Đây là cầu nối trực tiếp giữa quantum mechanics, NMR/MRI và quantum computing.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Phép quay và nhóm SU(2)** nối từ **Bloch sphere** sang **Thí nghiệm Stern–Gerlach**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phép quay và nhóm `SU(2)`

Phép quay spin quanh trục `\hat n` một góc `\theta` được mô tả bởi

```math
U(\hat n,\theta)
=
\exp\left(
-\frac{i\theta}{\hbar}
\hat n\cdot\mathbf S
\right).
```

Với spin-1/2,

```math
U(2\pi)=-I.
```

Sau phép quay `2\pi`, spinor đổi dấu. Phải quay `4\pi` mới trở về cùng véc-tơ (vector / 벡터) trạng thái chính xác.

Toàn cục (global / 전역) phase `-1` không quan sát được đối với một trạng thái cô lập đơn lẻ, nhưng sự khác biệt pha có thể xuất hiện trong interferometry khi so sánh các nhánh khác nhau.

Đây là dấu hiệu sâu của quan hệ giữa nhóm quay không gian `SO(3)` và nhóm phủ đôi `SU(2)`.

> **Nối mạch:** Trong **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Thí nghiệm Stern–Gerlach** nối từ **Phép quay và nhóm SU(2)** sang **Mômen từ và hiệu ứng Zeeman**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thí nghiệm Stern–Gerlach

Trong Stern–Gerlach, chùm nguyên tử đi qua từ trường không đồng đều và tách thành các nhánh rời rạc theo projection của magnetic moment.

Đối với hệ hiệu dụng spin-1/2, ta quan sát hai kết quả thay vì một phân phối (distribution / 분포) liên tục như véc-tơ (vector / 벡터) cổ điển định hướng ngẫu nhiên.

Thí nghiệm này cho thấy projection của mômen động lượng lượng tử có phổ rời rạc.

Nó cũng minh họa một điểm quan trọng: đo spin theo trục `z`, rồi theo `x`, rồi lại theo `z` không tương đương việc chỉ đọc một thuộc tính cổ điển đã tồn tại cố định. Các phép đo theo các trục khác nhau liên quan các toán tử không giao hoán.

> **Nối mạch:** Ở chặng này của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Mômen từ và hiệu ứng Zeeman** nối từ **Thí nghiệm Stern–Gerlach** sang **Larmor precession**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mômen từ và hiệu ứng Zeeman

Spin của electron liên hệ với mômen từ gần đúng

```math
\boldsymbol\mu_s
=-g\frac{e}{2m_e}\mathbf S,
```

trong đó `g` của electron gần

```math
g\approx2.0023.
```

Trong từ trường,

```math
H_Z=-\boldsymbol\mu\cdot\mathbf B.
```

Nếu chọn `B` theo trục `z`, các giá trị projection khác nhau tạo các mức năng lượng khác nhau.

Đây là hiệu ứng Zeeman (Zeeman effect / 제만 효과).

Cùng cấu trúc spin–trường dữ liệu (field / 필드) coupling xuất hiện trong:

```text
NMR
MRI
ESR/EPR
atomic clocks
quantum sensing
```

Chi tiết hệ số và moment khác nhau giữa electron, nucleus và atom, nhưng lô-gic (logic / 논리) coupling với trường ngoài là chung.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Larmor precession** nối từ **Mômen từ và hiệu ứng Zeeman** sang **Phép cộng hai mômen động lượng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Larmor precession

Một spin hoặc magnetic moment trong từ trường có thể precess quanh hướng trường.

Tần số góc có dạng

```math
\omega_L=\gamma B,
```

với `\gamma` là gyromagnetic ratio.

Đây là cầu nối giữa phương trình lượng tử của spin và tín hiệu precession đo được trong NMR/MRI.

> **Nối mạch:** Trong **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Phép cộng hai mômen động lượng** nối từ **Larmor precession** sang **Triplet và singlet của hai spin-1/2**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phép cộng hai mômen động lượng

Nếu hệ có

```math
\mathbf J_1,
\qquad
\mathbf J_2,
```

thì tổng toán tử là

```math
\mathbf J=\mathbf J_1+\mathbf J_2.
```

Các số lượng tử tổng cho phép là

```math
j=|j_1-j_2|,
|j_1-j_2|+1,
\ldots,
j_1+j_2.
```

Ví dụ, hai spin `1/2` cho

```math
\frac12\otimes\frac12
=1\oplus0.
```

Tức là một sector triplet `j=1` và một sector singlet `j=0`.

> **Nối mạch:** Ở chặng này của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Triplet và singlet của hai spin-1/2** nối từ **Phép cộng hai mômen động lượng** sang **Clebsch–Gordan coefficients**, vì cơ chế trước tạo đầu vào cho bước sau.

## Triplet và singlet của hai spin-1/2

Các trạng thái triplet là

```math
|1,1\rangle
=|\uparrow\uparrow\rangle,
```

```math
|1,0\rangle
=\frac{1}{\sqrt2}
\left(
|\uparrow\downarrow\rangle
+|\downarrow\uparrow\rangle
\right),
```

```math
|1,-1\rangle
=|\downarrow\downarrow\rangle.
```

Trạng thái singlet là

```math
|0,0\rangle
=\frac{1}{\sqrt2}
\left(
|\uparrow\downarrow\rangle
-|\downarrow\uparrow\rangle
\right).
```

Singlet là trạng thái rối lượng tử. Tổng mômen động lượng bằng zero, nhưng điều đó không có nghĩa mỗi spin riêng lẻ có một véc-tơ (vector / 벡터) cổ điển xác định và đối nhau trước phép đo.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Clebsch–Gordan coefficients** nối từ **Triplet và singlet của hai spin-1/2** sang **Spin–orbit coupling**, vì cơ chế trước tạo đầu vào cho bước sau.

## Clebsch–Gordan coefficients

Có hai basis tự nhiên:

```text
uncoupled basis:
|j_1m_1\rangle|j_2m_2\rangle
```

và

```text
coupled basis:
|jm\rangle.
```

Các hệ số Clebsch–Gordan thực hiện phép đổi cơ sở giữa hai cách mô tả.

Chúng xuất hiện trong:

```text
atomic fine structure
addition of orbital + spin angular momentum
spectroscopic term symbols
nuclear spin coupling
particle decay channels
```

Vì vậy chúng không chỉ là bảng hệ số đại số; chúng mã hóa cách các biểu diễn (representation / 표현) của rotational symmetry kết hợp.

> **Nối mạch:** Trong **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Spin–orbit coupling** nối từ **Clebsch–Gordan coefficients** sang **Selection rules và symmetry**, vì cơ chế trước tạo đầu vào cho bước sau.

## Spin–orbit coupling

Trong nguyên tử, mômen động lượng quỹ đạo `\mathbf L` và spin `\mathbf S` có thể tương tác.

Một mô hình hiệu dụng thường chứa hạng

```math
H_{SO}\propto\mathbf L\cdot\mathbf S.
```

Ta định nghĩa

```math
\mathbf J=\mathbf L+\mathbf S.
```

Dùng

```math
J^2=L^2+S^2+2\mathbf L\cdot\mathbf S,
```

suy ra

```math
\mathbf L\cdot\mathbf S
=\frac12
\left(
J^2-L^2-S^2
\right).
```

Nhờ đó năng lượng spin–orbit có thể được biểu diễn bằng các số lượng tử `j,\ell,s`.

Đây là ví dụ rõ về việc symmetry algebra biến một tương tác véc-tơ (vector / 벡터) phức tạp thành bài toán trị riêng gọn hơn.

> **Nối mạch:** Ở chặng này của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Selection rules và symmetry** nối từ **Spin–orbit coupling** sang **Các giả định (assumptions / 가정들) và giới hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## Selection rules và symmetry

Mômen động lượng còn quyết định những chuyển tiếp (transition / 전이) nào được phép hoặc bị suppressed.

Trong electric-dipole chuyển tiếp (transition / 전이), các quy tắc điển hình gồm

```math
\Delta\ell=\pm1
```

và

```math
\Delta m=0,\pm1,
```

với các điều kiện khác tùy hệ.

Các selection rules không phải quy ước ghi nhớ tùy ý. Chúng phản ánh symmetry, parity và ma trận (matrix / 행렬) element của tương tác (interaction / 상호작용) operator.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Selection rules và symmetry** đặt tiêu chí; **Các giả định (assumptions / 가정들) và giới hạn** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Các giả định (assumptions / 가정들) và giới hạn

### Spin không phải rotation của vật thể có kích thước

Không nên gán electron một radius cổ điển rồi tính tốc độ bề mặt để “giải thích” spin.

### `m` phụ thuộc trục lượng tử hóa

Giá trị `m` luôn được định nghĩa so với một trục chọn trước, thường do bên ngoài (external / 외부) trường dữ liệu (field / 필드) hoặc hình học (geometry / 기하학) xác định.

### Addition rules phụ thuộc biểu diễn (representation / 표현)

Quy tắc cộng `j` áp dụng cho angular-momentum representations. Nó không có nghĩa mọi véc-tơ (vector / 벡터) lượng tử đều cộng như véc-tơ (vector / 벡터) cổ điển với góc xác định trước.

> **Nối mạch:** Trong **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Các giả định (assumptions / 가정들) và giới hạn** đặt tiêu chí; **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Những ngộ nhận thường gặp (Common Misconceptions)** mở rộng hệ quả.

## Mô hình tư duy (mental model / 사고 모델)

Mômen động lượng lượng tử nên được hiểu như **generator của phép quay**.

```text
rotational symmetry
→ angular-momentum algebra
→ quantum numbers
→ degeneracy/coupling
→ selection rules
```

Spin là biểu diễn (representation / 표현) nội tại của cùng symmetry, không phải miniature mechanical rotation.

> **Nối mạch:** Ở chặng này của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, **Những ngộ nhận thường gặp (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Spin nghĩa là electron tự quay như quả cầu”

Sai. Spin là degree of freedom lượng tử nội tại.

### “véc-tơ (vector / 벡터) spin luôn chỉ theo một hướng xác định trước phép đo”

Không nói chung. Trạng thái có thể là superposition theo basis của trục đang đo.

### “Sau phép quay `2π`, vật lý thay đổi hoàn toàn vì spinor đổi dấu”

Không. toàn cục (global / 전역) phase không quan sát trực tiếp cho trạng thái đơn lẻ; điều quan trọng là relative phase trong phép so sánh/interference.

### “Hai spin singlet chỉ là hai véc-tơ (vector / 벡터) ngược hướng”

Không. Singlet là trạng thái rối có correlation lượng tử không thể mô tả đầy đủ bằng cặp véc-tơ (vector / 벡터) cổ điển cố định.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mômen động lượng lượng tử, spin và phép cộng mômen động lượng**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Chuyển động quay cổ điển](../01_mechanics/05_rotation_rigid_body.md), [Đối xứng và bảo toàn](../00_foundations/04_symmetry_conservation_scale.md).

**Liên hệ tiếp:** [Phép đo và rối lượng tử](03_measurement_entanglement_decoherence.md), [Vật lý nguyên tử](../09_atomic_nuclear_particle/00_atomic_physics.md), [Mô hình Chuẩn](../09_atomic_nuclear_particle/03_particle_standard_model.md), [Đối xứng và path integral](07_symmetry_operator_path_integral.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
