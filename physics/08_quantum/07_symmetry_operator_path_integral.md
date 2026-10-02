# Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đối xứng, generator operators, commutators và path integral trong cơ học lượng tử**. Route đi từ continuous symmetries → generators/commutators → translation and momentum → rotations/angular momentum → path-integral formulation, để các mô tả nối cùng một động lực học.

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

> **Chuyển mạch:** Trong **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Tịnh tiến và toán tử động lượng** tiếp nhận điểm tựa từ **Đối xứng trong cơ học lượng tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Commutator và tính tương thích của đại lượng quan sát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Commutator và tính tương thích của đại lượng quan sát** tiếp nhận điểm tựa từ **Tịnh tiến và toán tử động lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phương trình Heisenberg** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Phương trình Heisenberg** tiếp nhận điểm tựa từ **Commutator và tính tương thích của đại lượng quan sát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đối xứng và suy biến mức năng lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Đối xứng và suy biến mức năng lượng** tiếp nhận điểm tựa từ **Phương trình Heisenberg** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đối xứng rời rạc và parity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đối xứng và suy biến mức năng lượng

Nếu một toán tử đối xứng `\hat U` giao hoán với Hamiltonian,

```math
[\hat H,\hat U]=0,
```

thì biến đổi một trạng thái riêng năng lượng bằng `\hat U` vẫn cho trạng thái có cùng năng lượng.

Đối xứng vì vậy có thể tạo suy biến hoặc cho phép phân loại trạng thái bằng số lượng tử.

Với thế xuyên tâm, Hamiltonian có đối xứng quay nên giao hoán với `L^2` và `L_z`. Trạng thái nguyên tử được gắn nhãn bằng các số lượng tử mômen động lượng.

Khi đặt từ trường ngoài, đối xứng quay đầy đủ bị phá và suy biến có thể tách ra thành hiệu ứng Zeeman.

> **Chuyển mạch:** Ở chặng này của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Đối xứng rời rạc và parity** tiếp nhận điểm tựa từ **Đối xứng và suy biến mức năng lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đối xứng hoán vị của hạt đồng nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Đối xứng hoán vị của hạt đồng nhất** tiếp nhận điểm tựa từ **Đối xứng rời rạc và parity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tích phân đường: một formulation khác của cơ học lượng tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đối xứng hoán vị của hạt đồng nhất

Đổi chỗ hai hạt đồng nhất cũng là một phép biến đổi rời rạc.

- trạng thái boson đối xứng dưới hoán vị;
- trạng thái fermion phản đối xứng.

Ràng buộc này dẫn tới thống kê Bose–Einstein, nguyên lý loại trừ Pauli và rất nhiều hiện tượng nhiều hạt.

> **Chuyển mạch:** Trong **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Tích phân đường: một formulation khác của cơ học lượng tử** tiếp nhận điểm tựa từ **Đối xứng hoán vị của hạt đồng nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giới hạn cổ điển từ pha dừng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tích phân đường: một formulation khác của cơ học lượng tử

Tích phân đường Feynman viết propagator từ `(x_a,t_a)` tới `(x_b,t_b)` dưới dạng hình thức

```math
K(b,a)
=\int\mathcal D[x(t)]
\exp\left(\frac{i}{\hbar}S[x(t)]\right).
```

Ở đây `S[x(t)]` là tác dụng của một lịch sử `x(t)`.

Ta không nên hiểu rằng hạt cổ điển thật sự tách thành vô số bản sao và đi qua mọi con đường. Phát biểu toán học là biên độ chuyển tiếp nhận đóng góp phức từ các lịch sử khả dĩ.

> **Chuyển mạch:** Ở chặng này của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Tích phân đường: một formulation khác của cơ học lượng tử** đã nêu tiêu chí phân biệt, còn **Giới hạn cổ điển từ pha dừng** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Ví dụ hai khe dưới góc nhìn biên độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Giới hạn cổ điển từ pha dừng** cho ta quy tắc; **Ví dụ hai khe dưới góc nhìn biên độ** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Propagator và tính chất ghép nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nếu môi trường ghi lại thông tin đường đi đủ rõ, trạng thái môi trường gắn với hai nhánh trở nên gần trực giao. Khi lấy dấu vết (trace / 추적) môi trường, giao thoa giảm: đây là mất kết hợp lượng tử (decoherence).

> **Chuyển mạch:** Trong **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Ví dụ hai khe dưới góc nhìn biên độ** cho ta quy tắc; **Propagator và tính chất ghép nối** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Gauge trường dữ liệu (field / 필드) và pha lượng tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Propagator và tính chất ghép nối** nêu điều cần giải thích; **Gauge trường dữ liệu (field / 필드) và pha lượng tử** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Gauge symmetry và pha cục bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gauge trường dữ liệu (field / 필드) và pha lượng tử

Trong điện từ trường, tác dụng của hạt tích điện chứa coupling với thế `A_\mu`.

Do đó pha lượng tử phụ thuộc tích phân của thế dọc quỹ đạo. Hiệu ứng Aharonov–Bohm là ví dụ nơi từ trường cục bộ dọc theo đường đi có thể bằng 0 nhưng chênh lệch pha toàn cục vẫn đo được.

Tích phân đường làm mối liên hệ giữa topology, gauge và pha lượng tử trở nên trực quan.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Gauge trường dữ liệu (field / 필드) và pha lượng tử** nêu điều cần giải thích; **Gauge symmetry và pha cục bộ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Đơn vị và giới hạn bán cổ điển** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gauge symmetry và pha cục bộ

Pha toàn cục của trạng thái lượng tử không quan sát được trực tiếp. Nếu cho phép quy ước pha thay đổi theo vị trí–thời gian, đạo hàm thường sinh thêm hạng.

Gauge trường dữ liệu (field / 필드) cung cấp kết nối để so sánh pha tại các điểm lân cận theo cách hiệp biến.

Đây là cầu nối từ redundancy toán học của pha tới điện từ học và lý thuyết trường lượng tử.

> **Chuyển mạch:** Trong **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Gauge symmetry và pha cục bộ** đã nêu tiêu chí phân biệt, còn **Đơn vị và giới hạn bán cổ điển** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Khi formalism tích phân đường hữu ích?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị và giới hạn bán cổ điển

Tác dụng `S` có cùng đơn vị với `\hbar`, nên

```math
\frac{S}{\hbar}
```

là đại lượng vô thứ nguyên xuất hiện trong pha.

Khi `S/\hbar` rất lớn, pha dao động nhanh và xấp xỉ pha dừng hiệu quả. Khi tác dụng cùng bậc `\hbar`, nhiều lịch sử có thể đóng góp đáng kể và trực giác cổ điển mất hiệu lực.

> **Chuyển mạch:** Ở chặng này của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Đơn vị và giới hạn bán cổ điển** đã nêu tiêu chí phân biệt, còn **Khi formalism tích phân đường hữu ích?** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi formalism tích phân đường hữu ích?

Tích phân đường đặc biệt hữu ích khi:

- nghiên cứu giới hạn bán cổ điển;
- xử lý gauge lý thuyết (theory / 이론) và QFT;
- phân tích tunneling bằng biến đổi thời gian Euclid;
- xây partition hàm (function / 함수) lượng tử;
- khai thác symmetry và topology.

Tuy nhiên, đây không phải lúc nào là cách tính đơn giản nhất. Với giếng thế một chiều cơ bản, phương trình Schrödinger và phương pháp toán tử thường trực tiếp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Khi formalism tích phân đường hữu ích?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

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

> **Chuyển mạch:** Trong **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Hạt thật sự chia thành vô hạn bản sao đi mọi đường”

Không. Tích phân đường là formulation của biên độ chuyển tiếp, không phải bộ phim cổ điển của nhiều bản sao hạt.

### “Commutator khác 0 nghĩa là không thể đo hai đại lượng liên tiếp”

Không. Ta vẫn có thể đo liên tiếp, nhưng thứ tự đo ảnh hưởng trạng thái và thống kê; hai đại lượng không có cấu trúc giá trị sắc đồng thời như khi các toán tử giao hoán.

### “Đối xứng chỉ là hình học đẹp mắt”

Không. Đối xứng vật lý có thể là tịnh tiến, quay pha nội tại, hoán vị hạt hoặc gauge redundancy, không chỉ là đối xứng hình học nhìn thấy được.

### “Tích phân đường và Schrödinger là hai lý thuyết khác nhau”

Không. Trong miền chuẩn của cơ học lượng tử không tương đối tính, chúng là các formulation tương đương.

> **Chuyển mạch:** Ở chặng này của **Đối xứng, toán tử sinh, commutator và tích phân đường trong cơ học lượng tử**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Mômen động lượng](02_angular_momentum_spin.md), [Cơ học Hamilton nâng cao](../01_mechanics/10_canonical_transformations_hamilton_jacobi.md).

**Liên hệ tiếp:** [Thế gauge](../05_electromagnetism/06_potentials_gauge.md), [Trường lượng tử](../09_atomic_nuclear_particle/05_quantum_fields_symmetry_interactions.md), [Thống kê lượng tử](05_identical_particles_quantum_statistics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
