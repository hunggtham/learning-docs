# Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**. Route đi từ dao động tử → mode của trường → lượng tử hóa và hạt → gauge symmetry → tương tác/biên độ, để QFT nối số hạt thay đổi với trường nền.

## Vì sao cơ học lượng tử với số hạt cố định chưa đủ?

Cơ học lượng tử không tương đối tính thường bắt đầu bằng hàm sóng của một hoặc vài hạt. Cách mô tả này hoạt động rất tốt khi số hạt gần như cố định.

Nhưng trong vật lý tương đối tính và năng lượng cao, năng lượng có thể chuyển thành hạt mới và hạt có thể bị hủy:

- photon được phát hoặc hấp thụ;
- cặp electron–positron có thể được tạo khi đủ năng lượng;
- hạt không bền có thể phân rã thành các hạt khác.

Một lý thuyết với số hạt cố định không mô tả những quá trình này một cách tự nhiên.

Lý thuyết trường lượng tử (Quantum Field Theory, QFT / 양자장론) đổi điểm xuất phát:

> trường là đối tượng cơ bản; hạt là kích thích lượng tử của trường.

Electron là excitation của trường electron; photon là excitation của trường điện từ.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Từ dao động tử điều hòa tới chế độ (mode / 모드) của trường** tiếp nhận điểm tựa từ **Vì sao cơ học lượng tử với số hạt cố định chưa đủ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trường cổ điển trước khi lượng tử hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ dao động tử điều hòa tới chế độ (mode / 모드) của trường

Một trường tự do cổ điển có thể được khai triển thành các chế độ (mode / 모드) chuẩn. Mỗi chế độ (mode / 모드) về mặt toán học gần giống một dao động tử điều hòa.

Dao động tử lượng tử có mức năng lượng

```math
E_n=\hbar\omega\left(n+\frac12\right).
```

Ta định nghĩa toán tử tạo và hủy

```math
\hat a^\dagger,\qquad \hat a,
```

làm tăng hoặc giảm số lượng tử của một chế độ (mode / 모드).

Trong QFT, mỗi chế độ (mode / 모드) theo số sóng, phân cực hoặc số lượng tử khác có các toán tử tương tự. “Tạo một photon” nghĩa là tăng occupation number của một chế độ (mode / 모드) trường điện từ.

Đây là cầu nối tự nhiên từ dao động tử lượng tử sang trạng thái nhiều hạt.

> **Chuyển mạch:** Ở chặng này của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Trường cổ điển trước khi lượng tử hóa** tiếp nhận điểm tựa từ **Từ dao động tử điều hòa tới chế độ (mode / 모드) của trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lượng tử hóa các chế độ (mode / 모드) trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường cổ điển trước khi lượng tử hóa

Xét một trường vô hướng `\phi(x)` với mật độ Lagrangian minh họa

```math
\mathcal L
=\frac12\partial_\mu\phi\partial^\mu\phi
-\frac12m^2\phi^2.
```

Tác dụng là

```math
S=\int d^4x\,\mathcal L.
```

Phương trình Euler–Lagrange cho trường

```math
\partial_\mu
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}
-
\frac{\partial\mathcal L}{\partial\phi}=0
```

cho phương trình Klein–Gordon.

Điểm quan trọng là trước khi nói về “hạt”, QFT bắt đầu bằng trường như biến động lực học phân bố trên không-thời gian.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Lượng tử hóa các chế độ (mode / 모드) trường** tiếp nhận điểm tựa từ **Trường cổ điển trước khi lượng tử hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fock không gian (space / 공간) và số hạt biến đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lượng tử hóa các chế độ (mode / 모드) trường

Trong một hộp hữu hạn, trường tự do có thể khai triển Fourier thành nhiều chế độ (mode / 모드). Sau lượng tử hóa, Hamiltonian có cấu trúc

```math
H=\sum_{\mathbf k}
\hbar\omega_{\mathbf k}
\left(
 a^\dagger_{\mathbf k}a_{\mathbf k}
 +\frac12
\right).
```

Toán tử `a^\dagger_{\mathbf k}` tạo một lượng tử trong chế độ (mode / 모드) `\mathbf k`; `a_{\mathbf k}` hủy một lượng tử.

Khái niệm hạt vì vậy nổi lên từ chế độ (mode / 모드) lượng tử hóa của trường.

Với trường boson, một chế độ (mode / 모드) có thể có nhiều lượng tử. Với trường fermion, quan hệ phản giao hoán dẫn đến nguyên lý Pauli và giới hạn occupation phù hợp.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Fock không gian (space / 공간) và số hạt biến đổi** tiếp nhận điểm tựa từ **Lượng tử hóa các chế độ (mode / 모드) trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chân không lượng tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fock không gian (space / 공간) và số hạt biến đổi

Không gian Hilbert với số hạt cố định không đủ cho quá trình tạo–hủy hạt.

Fock không gian (space / 공간) được xây như tổng trực tiếp

```math
\mathcal F
=
\mathcal H_0
\oplus\mathcal H_1
\oplus\mathcal H_2
\oplus\cdots.
```

Mỗi `\mathcal H_N` là sector có `N` hạt.

Toán tử tạo ánh xạ `N\to N+1`; toán tử hủy ánh xạ `N\to N-1`.

Với một chế độ (mode / 모드) boson đơn giản,

```math
\hat N=\hat a^\dagger\hat a
```

là toán tử số hạt.

Cấu trúc này cho phép mô tả phát xạ photon, hấp thụ, phân rã và tạo cặp trong cùng một formalism.

> **Chuyển mạch:** Ở chặng này của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Chân không lượng tử** tiếp nhận điểm tựa từ **Fock không gian (space / 공간) và số hạt biến đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Propagator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chân không lượng tử

Trạng thái chân không `|0\rangle` là trạng thái không có lượng tử hạt tự do được phát hiện trong cơ sở đang xét, nhưng nó không phải “hư vô cổ điển”.

Các hàm tương quan của trường trong chân không vẫn có cấu trúc lượng tử.

Tuy nhiên, câu phổ biến “hạt ảo liên tục bật ra rồi biến mất khỏi chân không” dễ gây hiểu nhầm. Hạt ảo thường là thành phần của khai triển nhiễu loạn và Feynman diagram, không phải hạt on-shell có thể quan sát trực tiếp bằng detector.

Các hiệu ứng chân không như Lamb shift hay Casimir cần được mô tả qua trường, tương quan, điều kiện biên và tương tác cụ thể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Propagator** tiếp nhận điểm tựa từ **Chân không lượng tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tương tác (interaction / 상호작용) picture và khai triển nhiễu loạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Propagator

Một hàm tương quan hai điểm điển hình là

```math
G(x-y)
=\langle0|T\{\phi(x)\phi(y)\}|0\rangle.
```

Trong lý thuyết nhiễu loạn, propagator có thể được xem như nghịch đảo của toán tử động học tự do cùng prescription nhân quả thích hợp.

Với trường vô hướng, trong không gian động lượng ta gặp cấu trúc

```math
\frac{i}{p^2-m^2+i\epsilon}.
```

Đường bên trong Feynman diagram biểu diễn factor propagator trong một biểu thức tích phân. Nó không phải quỹ đạo camera ghi lại một hạt thật bay giữa hai vertex.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Tương tác (interaction / 상호작용) picture và khai triển nhiễu loạn** tiếp nhận điểm tựa từ **Propagator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ Lagrangian đến đại lượng đo được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tương tác (interaction / 상호작용) picture và khai triển nhiễu loạn

Nếu

```math
H=H_0+H_I,
```

thì S-matrix có dạng

```math
S
=T\exp\left[
-\frac{i}{\hbar}
\int H_I(t)dt
\right].
```

Khai triển hàm mũ tạo chuỗi theo lũy thừa của coupling.

Wick theorem tổ chức các tích toán tử thành contraction; Feynman diagram là cách ghi hình học cho các hạng trong chuỗi đó.

- cây (tree / 트리) mức (level / 수준) thường là bậc thấp nhất;
- vòng lặp (loop / 루프) chứa hiệu chỉnh lượng tử và tích phân trên động lượng nội bộ.

Diagram là công cụ bookkeeping của biên độ, không phải ảnh chụp literal của quá trình vi mô.

> **Chuyển mạch:** Ở chặng này của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Từ Lagrangian đến đại lượng đo được** tiếp nhận điểm tựa từ **Tương tác (interaction / 상호작용) picture và khai triển nhiễu loạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao vòng lặp (loop / 루프) có thể phân kỳ?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ Lagrangian đến đại lượng đo được

Chuỗi suy luận điển hình là

```text
Lagrangian
→ interaction terms
→ Feynman rules
→ amplitude M
→ |M|²
→ phase space
→ cross section / decay rate
```

Các định luật bảo toàn giới hạn phase không gian (space / 공간) cuối cùng.

Trong giới hạn không tương đối tính, cấu trúc này nối trở lại định luật vàng Fermi và lý thuyết tán xạ lượng tử.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Vì sao vòng lặp (loop / 루프) có thể phân kỳ?** tiếp nhận điểm tựa từ **Từ Lagrangian đến đại lượng đo được** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Running coupling và hàm beta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao vòng lặp (loop / 루프) có thể phân kỳ?

Lý thuyết trường liên tục cho phép tích phân qua động lượng nội bộ tùy lớn. Một số vòng lặp (loop / 루프) integral vì vậy phân kỳ nếu tính trực tiếp.

Regularization tạm thời đưa vào một cách kiểm soát miền tích phân, chẳng hạn cutoff hoặc dimensional regularization.

Renormalization sau đó biểu diễn kết quả bằng các tham số được xác định từ phép đo tại một thang năng lượng.

Cách nhìn hiện đại không phải “trừ vô cực tùy ý”. Tham số bare không phải đại lượng đo trực tiếp; coupling hiệu dụng phụ thuộc độ phân giải hoặc thang năng lượng.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Running coupling và hàm beta** tiếp nhận điểm tựa từ **Vì sao vòng lặp (loop / 루프) có thể phân kỳ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đối xứng gauge và tương tác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Running coupling và hàm beta

Với coupling vô thứ nguyên `g`, ta định nghĩa

```math
\beta(g)
=\mu\frac{dg}{d\mu}.
```

Hàm beta cho biết coupling thay đổi theo thang `\mu`.

Trong QED, coupling điện từ tăng chậm ở năng lượng cao do vacuum polarization.

Trong QCD, coupling mạnh giảm ở năng lượng cao: đây là tự do tiệm cận (asymptotic freedom).

Ý tưởng RG này có họ hàng sâu với nhóm tái chuẩn hóa trong hiện tượng tới hạn của cơ học thống kê.

> **Chuyển mạch:** Ở chặng này của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Đối xứng gauge và tương tác** tiếp nhận điểm tựa từ **Running coupling và hàm beta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gauge symmetry là redundancy hay symmetry vật lý?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đối xứng gauge và tương tác

Với trường vật chất biến đổi pha cục bộ

```math
\psi(x)
\to e^{iq\alpha(x)}\psi(x),
```

đạo hàm thường sinh thêm hạng chứa `\partial_\mu\alpha`.

Ta đưa vào trường gauge `A_\mu` và đạo hàm hiệp biến

```math
D_\mu
=\partial_\mu+iqA_\mu
```

bỏ qua các hệ số quy ước như `\hbar` hoặc `c` tùy hệ đơn vị.

Trường gauge biến đổi sao cho `D_\mu\psi` có quy luật biến đổi nhất quán.

Điểm sâu là yêu cầu đối xứng gauge cục bộ ràng buộc mạnh cấu trúc tương tác.

Trong Mô hình Chuẩn:

- điện từ liên hệ với `U(1)`;
- tương tác yếu với `SU(2)`;
- tương tác mạnh với `SU(3)`.

Các nhóm không Abel như `SU(2)` và `SU(3)` cho phép gauge boson tự mang charge tương ứng và tự tương tác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Gauge symmetry là redundancy hay symmetry vật lý?** tiếp nhận điểm tựa từ **Đối xứng gauge và tương tác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phá vỡ đối xứng tự phát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gauge symmetry là redundancy hay symmetry vật lý?

Gauge transformation thường nên được hiểu như sự dư thừa trong cách biểu diễn, không phải thao tác vật lý tạo một trạng thái quan sát được mới.

Đại lượng đo được phải gauge-invariant hoặc được xây sao cho dự đoán không phụ thuộc lựa chọn gauge.

Tuy nhiên, chính cấu trúc gauge lại quyết định tương tác, số bậc tự do và các định luật bảo toàn quan trọng.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Phá vỡ đối xứng tự phát** tiếp nhận điểm tựa từ **Gauge symmetry là redundancy hay symmetry vật lý?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **QCD, color và confinement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phá vỡ đối xứng tự phát

Nếu thế của trường có nhiều minimum suy biến, phương trình có thể đối xứng trong khi trạng thái chân không cụ thể không giữ toàn bộ đối xứng đó.

Với đối xứng toàn cục liên tục, phá vỡ tự phát dẫn tới chế độ (mode / 모드) Goldstone.

Trong gauge lý thuyết (theory / 이론), cơ chế Higgs tổ chức lại các bậc tự do và làm gauge boson có khối lượng theo cách phù hợp với đối xứng của lý thuyết.

Không nên nói đơn giản “Higgs cho mọi vật khối lượng”. Phần lớn khối lượng proton và neutron đến từ năng lượng động lực học QCD và liên kết, không phải chỉ từ tổng khối lượng bare của quark.

> **Chuyển mạch:** Ở chặng này của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **QCD, color và confinement** tiếp nhận điểm tựa từ **Phá vỡ đối xứng tự phát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Effective trường dữ liệu (field / 필드) lý thuyết (theory / 이론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## QCD, color và confinement

QCD mô tả quark và gluon với color charge.

Ở năng lượng cao hoặc khoảng cách ngắn, asymptotic freedom làm coupling yếu hơn và mô tả parton trở nên hữu ích.

Ở năng lượng thấp hoặc khoảng cách lớn, confinement khiến quark cô lập không xuất hiện như hạt tự do.

Khi kéo hai quark xa nhau, năng lượng trong trường màu tăng và cuối cùng thuận lợi hơn để tạo hadron mới thay vì giải phóng một quark đơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **QCD, color và confinement** nêu điều cần giải thích; **Effective trường dữ liệu (field / 필드) lý thuyết (theory / 이론)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Vì sao hạt truyền nặng tạo tương tác tiếp xúc?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Effective trường dữ liệu (field / 필드) lý thuyết (theory / 이론)

Không cần biết vật lý ở mọi thang để dự đoán hiện tượng năng lượng thấp.

Lý thuyết trường hiệu dụng (Effective Field Theory, EFT / 유효장이론) viết các toán tử được phép bởi symmetry rồi sắp xếp chúng theo lũy thừa của một thang năng lượng lớn `\Lambda`:

```math
\mathcal L_{eff}
=
\mathcal L_{low}
+\frac{c_5}{\Lambda}\mathcal O_5
+\frac{c_6}{\Lambda^2}\mathcal O_6
+\cdots.
```

Khi

```math
E\ll\Lambda,
```

các toán tử bậc cao bị suy giảm bởi lũy thừa `E/\Lambda`.

Do đó độ chính xác của mô hình được tổ chức có hệ thống mà không cần biết đầy đủ lý thuyết ở thang rất cao.

Lý thuyết Fermi của phân rã beta là ví dụ lịch sử của EFT năng lượng thấp trước mô tả boson `W` của điện yếu.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Effective trường dữ liệu (field / 필드) lý thuyết (theory / 이론)** nêu điều cần giải thích; **Vì sao hạt truyền nặng tạo tương tác tiếp xúc?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **QFT trong vật chất ngưng tụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao hạt truyền nặng tạo tương tác tiếp xúc?

Propagator của mediator khối lượng `M` có cấu trúc

```math
\frac{1}{q^2-M^2}.
```

Nếu

```math
|q^2|\ll M^2,
```

thì

```math
\frac{1}{q^2-M^2}
\approx
-\frac{1}{M^2}
\left(
1+\frac{q^2}{M^2}+\cdots
\right).
```

Hạng dẫn đầu gần như không phụ thuộc động lượng và trông như tương tác tiếp xúc cục bộ với hệ số bị suy giảm bởi `1/M^2`.

Đây là nguồn gốc toán học trực tiếp của nhiều tương tác hiệu dụng.

> **Chuyển mạch:** Ở chặng này của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **QFT trong vật chất ngưng tụ** tiếp nhận điểm tựa từ **Vì sao hạt truyền nặng tạo tương tác tiếp xúc?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Năng lượng chân không và vấn đề hằng số vũ trụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## QFT trong vật chất ngưng tụ

Ngôn ngữ trường không chỉ dành cho máy gia tốc.

Trong vật chất ngưng tụ, ta gặp:

- phonon;
- magnon;
- quasiparticle;
- tham số trật tự siêu dẫn;
- chế độ (mode / 모드) Goldstone;
- lý thuyết tới hạn.

Các excitation nổi lên có thể thỏa phương trình giống hạt tương đối tính dù mạng tinh thể vi mô không có đối xứng Lorentz chính xác.

Điều này minh họa sức mạnh của lý thuyết hiệu dụng: cùng cấu trúc toán học có thể xuất hiện ở nhiều hệ khác bản chất vi mô.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Năng lượng chân không và vấn đề hằng số vũ trụ** tiếp nhận điểm tựa từ **QFT trong vật chất ngưng tụ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Miền áp dụng và giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lượng chân không và vấn đề hằng số vũ trụ

Mỗi chế độ (mode / 모드) boson có hạng zero-point

```math
\frac12\hbar\omega.
```

Cộng hình thức qua vô hạn chế độ (mode / 모드) tạo tổng phân kỳ.

Trong QFT không có hấp dẫn, thường chỉ chênh lệch năng lượng hoặc đại lượng đã tái chuẩn hóa là trực tiếp quan trọng.

Khi có hấp dẫn, mật độ năng lượng tuyệt đối ghép với không-thời gian, làm vấn đề hằng số vũ trụ trở nên sâu sắc.

Do đó câu “chân không có năng lượng vô hạn” là quá đơn giản; phải phân biệt regularization, đại lượng tái chuẩn hóa và coupling với hấp dẫn.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Năng lượng chân không và vấn đề hằng số vũ trụ** đã nêu tiêu chí phân biệt, còn **Miền áp dụng và giới hạn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Miền áp dụng và giới hạn

QFT chuẩn giả sử nền không-thời gian và cấu trúc nhân quả thích hợp. Trong trường hấp dẫn lượng tử mạnh, formalism trường trên không-thời gian cổ điển có thể không còn đủ.

Khai triển nhiễu loạn chỉ hiệu quả khi coupling hoặc tham số khai triển đủ nhỏ. QCD năng lượng thấp thường cần lattice QCD hoặc kỹ thuật phi nhiễu loạn.

EFT luôn đi kèm miền hiệu lực. Khi năng lượng tiến gần `\Lambda`, các toán tử bị bỏ qua không còn nhỏ và cần mô hình sâu hơn.

> **Chuyển mạch:** Ở chặng này của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Miền áp dụng và giới hạn** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

QFT thay cách nhìn “các hạt nhỏ tương tác với nhau” bằng

```text
local fields
→ normal modes
→ quantization
→ particle excitations
→ symmetry + gauge structure
→ interactions
→ amplitudes
→ measurable cross sections / decay rates
```

Renormalization tổ chức sự phụ thuộc theo thang; EFT nói rõ ta cần giữ bậc tự do nào ở độ phân giải đang xét.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Hạt ảo là hạt thật tạm thời vi phạm bảo toàn năng lượng”

Không. nội bộ (internal / 내부) line là thành phần toán học của khai triển nhiễu loạn. Bảo toàn năng lượng–động lượng được áp dụng nhất quán tại vertex; hạt ảo không cần thỏa quan hệ on-shell của hạt được phát hiện.

### “Higgs tạo toàn bộ khối lượng vật chất”

Không. Higgs cung cấp khối lượng cho fermion cơ bản và boson điện yếu theo cơ chế của Mô hình Chuẩn; phần lớn khối lượng vật chất baryon thông thường đến từ năng lượng QCD bên trong nucleon.

### “Renormalization chỉ là che vô cực”

Không. Một phần cốt lõi là coupling và tham số hiệu dụng phụ thuộc thang; running coupling là dự đoán đo được.

### “QFT chỉ là cơ học lượng tử cộng thuyết tương đối”

Đó là động lực quan trọng nhưng chưa đủ. QFT thêm trường cục bộ, số hạt biến đổi, Fock không gian (space / 공간), chân không, renormalization và cấu trúc nhiều hạt.

### “Gauge symmetry tạo một trạng thái vật lý khác khi ta đổi gauge”

Không. Gauge choice thường là redundancy biểu diễn; dự đoán vật lý phải độc lập lựa chọn đó.

> **Chuyển mạch:** Trong **Trường lượng tử, đối xứng gauge và tương tác: nền tảng khái niệm của QFT**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Mô hình Chuẩn](03_particle_standard_model.md), [Thế gauge](../05_electromagnetism/06_potentials_gauge.md), [Đối xứng và tích phân đường](../08_quantum/07_symmetry_operator_path_integral.md).

**Liên hệ tiếp:** [Hiện tượng tới hạn và RG](../04_thermal_statistical/05_critical_phenomena_renormalization.md), [Vật chất tô pô](../10_condensed_matter_devices/04_phonons_defects_topological_matter.md), [Vũ trụ sơ khai](../11_astrophysics_cosmology/03_early_universe_dark_components.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
