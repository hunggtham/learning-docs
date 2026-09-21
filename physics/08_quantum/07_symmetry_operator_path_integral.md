# Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử

## Đối xứng trong cơ học lượng tử

Trong vật lý cổ điển, đối xứng thường là một phép biến đổi không làm thay đổi định luật vật lý. Trong cơ học lượng tử, phép biến đổi trạng thái được biểu diễn bằng toán tử unitary `U`; một số đối xứng như đảo thời gian có thể cần toán tử antiunitary.

Với một biến đổi liên tục rất nhỏ,

```math
U(\epsilon)
\approx1-\frac{i}{\hbar}\epsilon\hat G,
```

trong đó `\hat G` là toán tử sinh (generator / 생성자).

Các ví dụ nền tảng:

- tịnh tiến không gian được sinh bởi động lượng;
- quay được sinh bởi mômen động lượng;
- tịnh tiến thời gian được sinh bởi Hamiltonian.

Đây là phiên bản lượng tử của mối liên hệ giữa đối xứng và đại lượng bảo toàn.

## Tịnh tiến và toán tử động lượng

Phép tịnh tiến một khoảng `a` có thể viết

```math
\hat U(a)=e^{-ia\hat P/\hbar}.
```

Trong biểu diễn vị trí,

```math
\hat P=-i\hbar\frac{d}{dx}.
```

Lý do đạo hàm xuất hiện có thể thấy từ khai triển

```math
\psi(x-a)
\approx\psi(x)-a\frac{d\psi}{dx}.
```

So sánh với khai triển của `\hat U(a)` cho thấy động lượng chính là toán tử sinh của tịnh tiến.

Điều này làm rõ một ý quan trọng: một đại lượng bảo toàn không chỉ là “con số không đổi”; nó còn có thể sinh ra một đối xứng liên tục của không gian trạng thái.

## Commutator và tính tương thích của đại lượng quan sát

Commutator được định nghĩa bởi

```math
[\hat A,\hat B]
=\hat A\hat B-\hat B\hat A.
```

Nếu hai toán tử giao hoán và thỏa các điều kiện toán học phù hợp, chúng có thể có một cơ sở trị riêng chung. Khi đó các đại lượng tương ứng có thể đồng thời có giá trị xác định trong cùng trạng thái.

Quan hệ chính tắc

```math
[\hat x,\hat p]=i\hbar
```

là nguồn gốc của quan hệ bất định

```math
\Delta x\,\Delta p\ge\frac{\hbar}{2}.
```

Độ bất định này không chỉ đến từ thiết bị đo kém; nó phản ánh cấu trúc đại số của không gian trạng thái.

## Phương trình Heisenberg

Trong bức tranh Heisenberg, trạng thái được giữ cố định hơn còn toán tử tiến hóa theo thời gian:

```math
\frac{d\hat A}{dt}
=\frac{i}{\hbar}[\hat H,\hat A]
+\frac{\partial\hat A}{\partial t}.
```

So sánh với phương trình Hamilton cổ điển

```math
\frac{dA}{dt}
=\{A,H\}
+\frac{\partial A}{\partial t},
```

ta thấy ngoặc Poisson và commutator có cấu trúc tương ứng sâu sắc.

Cơ học lượng tử vì vậy không xuất hiện như một lý thuyết hoàn toàn tách rời; nó thay đổi cách biểu diễn và đại số của các đại lượng động lực học.

## Đối xứng và suy biến mức năng lượng

Nếu một toán tử đối xứng `\hat U` giao hoán với Hamiltonian,

```math
[\hat H,\hat U]=0,
```

thì biến đổi một trạng thái riêng năng lượng bằng `\hat U` vẫn cho trạng thái có cùng năng lượng.

Đối xứng vì vậy có thể tạo suy biến hoặc cho phép phân loại trạng thái bằng số lượng tử.

Với thế xuyên tâm, Hamiltonian có đối xứng quay nên giao hoán với `L^2` và `L_z`. Trạng thái nguyên tử được gắn nhãn bằng các số lượng tử mômen động lượng.

Khi đặt từ trường ngoài, đối xứng quay đầy đủ bị phá và suy biến có thể tách ra thành hiệu ứng Zeeman.

## Đối xứng rời rạc và parity

Phép parity biến đổi

```math
\mathbf r\to-\mathbf r.
```

Nếu thế thỏa

```math
V(\mathbf r)=V(-\mathbf r),
```

Hamiltonian giao hoán với toán tử parity. Các trạng thái riêng có thể được chọn với parity chẵn hoặc lẻ.

Nhiều quy tắc chọn trong quang phổ học xuất phát từ đối xứng. Một phần tử ma trận

```math
\langle f|\hat O|i\rangle
```

có thể bằng 0 nếu tính biến đổi parity hoặc symmetry làm các đóng góp triệt tiêu.

## Đối xứng hoán vị của hạt đồng nhất

Đổi chỗ hai hạt đồng nhất cũng là một phép biến đổi rời rạc.

- trạng thái boson đối xứng dưới hoán vị;
- trạng thái fermion phản đối xứng.

Ràng buộc này dẫn tới thống kê Bose–Einstein, nguyên lý loại trừ Pauli và rất nhiều hiện tượng nhiều hạt.

## Tích phân đường: một formulation khác của cơ học lượng tử

Tích phân đường Feynman viết propagator từ `(x_a,t_a)` tới `(x_b,t_b)` dưới dạng hình thức

```math
K(b,a)
=\int\mathcal D[x(t)]
\exp\left(\frac{i}{\hbar}S[x(t)]\right).
```

Ở đây `S[x(t)]` là tác dụng của một lịch sử `x(t)`.

Ta không nên hiểu rằng hạt cổ điển thật sự tách thành vô số bản sao và đi qua mọi con đường. Phát biểu toán học là biên độ chuyển tiếp nhận đóng góp phức từ các lịch sử khả dĩ.

## Giới hạn cổ điển từ pha dừng

Khi tác dụng đặc trưng lớn hơn nhiều `\hbar`, pha

```math
e^{iS/\hbar}
```

thay đổi rất nhanh giữa các lịch sử lân cận.

Phần lớn đóng góp triệt tiêu do giao thoa, trừ vùng quanh các lịch sử thỏa

```math
\delta S=0.
```

Đây chính là nguyên lý tác dụng dừng của cơ học cổ điển.

Do đó quỹ đạo cổ điển xuất hiện như giới hạn pha dừng của tích phân đường, thay vì cần giả thuyết rằng “tự nhiên thử mọi đường rồi chọn đường tốt nhất”.

## Ví dụ hai khe dưới góc nhìn biên độ

Nếu hai khe là hai lớp lịch sử chính, biên độ tại detector là

```math
\mathcal A=\mathcal A_1+\mathcal A_2.
```

Xác suất là

```math
P=|\mathcal A_1+\mathcal A_2|^2.
```

Hạng chéo tạo giao thoa.

Nếu môi trường ghi lại thông tin đường đi đủ rõ, trạng thái môi trường gắn với hai nhánh trở nên gần trực giao. Khi lấy trace môi trường, giao thoa giảm: đây là mất kết hợp lượng tử (decoherence).

## Propagator và tính chất ghép nối

Propagator thỏa quan hệ composition

```math
K(x_f,t_f;x_i,t_i)
=\int dx\,
K(x_f,t_f;x,t)
K(x,t;x_i,t_i).
```

Cấu trúc này tương ứng với việc toán tử tiến hóa có thể được chia thành nhiều bước thời gian liên tiếp.

Tích phân đường và phương trình Schrödinger không phải hai lý thuyết cạnh tranh. Chúng là hai formulation tương đương trong miền áp dụng phù hợp, mỗi cách thuận lợi cho loại bài toán khác nhau.

## Gauge field và pha lượng tử

Trong điện từ trường, tác dụng của hạt tích điện chứa coupling với thế `A_\mu`.

Do đó pha lượng tử phụ thuộc tích phân của thế dọc quỹ đạo. Hiệu ứng Aharonov–Bohm là ví dụ nơi từ trường cục bộ dọc theo đường đi có thể bằng 0 nhưng chênh lệch pha toàn cục vẫn đo được.

Tích phân đường làm mối liên hệ giữa topology, gauge và pha lượng tử trở nên trực quan.

## Gauge symmetry và pha cục bộ

Pha toàn cục của trạng thái lượng tử không quan sát được trực tiếp. Nếu cho phép quy ước pha thay đổi theo vị trí–thời gian, đạo hàm thường sinh thêm hạng.

Gauge field cung cấp kết nối để so sánh pha tại các điểm lân cận theo cách hiệp biến.

Đây là cầu nối từ redundancy toán học của pha tới điện từ học và lý thuyết trường lượng tử.

## Đơn vị và giới hạn bán cổ điển

Tác dụng `S` có cùng đơn vị với `\hbar`, nên

```math
\frac{S}{\hbar}
```

là đại lượng vô thứ nguyên xuất hiện trong pha.

Khi `S/\hbar` rất lớn, pha dao động nhanh và xấp xỉ pha dừng hiệu quả. Khi tác dụng cùng bậc `\hbar`, nhiều lịch sử có thể đóng góp đáng kể và trực giác cổ điển mất hiệu lực.

## Khi formalism tích phân đường hữu ích?

Tích phân đường đặc biệt hữu ích khi:

- nghiên cứu giới hạn bán cổ điển;
- xử lý gauge theory và QFT;
- phân tích tunneling bằng biến đổi thời gian Euclid;
- xây partition function lượng tử;
- khai thác symmetry và topology.

Tuy nhiên, đây không phải lúc nào là cách tính đơn giản nhất. Với giếng thế một chiều cơ bản, phương trình Schrödinger và phương pháp toán tử thường trực tiếp hơn.

## Mô hình tư duy (Mental Model)

Trong cơ học lượng tử, đối xứng tổ chức không gian Hilbert, xác định generator, định luật bảo toàn và quy tắc chọn.

Tích phân đường bổ sung một góc nhìn khác: động lực lượng tử là giao thoa giữa biên độ gắn với nhiều lịch sử, còn cơ học cổ điển xuất hiện khi các pha ngoài vùng tác dụng dừng tự triệt tiêu.

Có thể nối các ý tưởng:

```text
symmetry
→ generator
→ commutator
→ conservation / quantum number
→ action
→ path integral
→ stationary phase
→ classical limit
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Hạt thật sự chia thành vô hạn bản sao đi mọi đường”

Không. Tích phân đường là formulation của biên độ chuyển tiếp, không phải bộ phim cổ điển của nhiều bản sao hạt.

### “Commutator khác 0 nghĩa là không thể đo hai đại lượng liên tiếp”

Không. Ta vẫn có thể đo liên tiếp, nhưng thứ tự đo ảnh hưởng trạng thái và thống kê; hai đại lượng không có cấu trúc giá trị sắc đồng thời như khi các toán tử giao hoán.

### “Đối xứng chỉ là hình học đẹp mắt”

Không. Đối xứng vật lý có thể là tịnh tiến, quay pha nội tại, hoán vị hạt hoặc gauge redundancy, không chỉ là đối xứng hình học nhìn thấy được.

### “Tích phân đường và Schrödinger là hai lý thuyết khác nhau”

Không. Trong miền chuẩn của cơ học lượng tử không tương đối tính, chúng là các formulation tương đương.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Mômen động lượng](02_angular_momentum_spin.md), [Cơ học Hamilton nâng cao](../01_mechanics/10_canonical_transformations_hamilton_jacobi.md).

**Liên hệ tiếp:** [Thế gauge](../05_electromagnetism/06_potentials_gauge.md), [Trường lượng tử](../09_atomic_nuclear_particle/05_quantum_fields_symmetry_interactions.md), [Thống kê lượng tử](05_identical_particles_quantum_statistics.md).
