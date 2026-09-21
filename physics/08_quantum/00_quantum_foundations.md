# Nền tảng lượng tử: trạng thái, hàm sóng, toán tử và độ bất định

## Vì sao vật lý cổ điển không đủ?

Cơ học Newton, điện từ học Maxwell và nhiệt động lực học mô tả rất nhiều hiện tượng vĩ mô với độ chính xác cao. Tuy nhiên, cuối thế kỷ XIX và đầu thế kỷ XX xuất hiện một loạt dữ liệu mà khung cổ điển không thể giải thích nhất quán: phổ bức xạ vật đen, hiệu ứng quang điện, phổ vạch nguyên tử, độ bền của nguyên tử và hành vi của vật chất ở thang vi mô.

Vấn đề không chỉ là “thiếu một lực mới”. Những thí nghiệm này cho thấy chính cách ta mô tả **trạng thái (state)**, **phép đo (measurement)**, **xác suất (probability)** và **quỹ đạo hạt (particle trajectory)** cần được thay đổi.

Cơ học lượng tử (Quantum Mechanics / 양자역학) cung cấp một khung toán học khác để mô tả trạng thái và dự đoán phân bố xác suất của kết quả đo. Nó không nói thế giới vi mô “ngẫu nhiên hơn” một cách mơ hồ; nó đặt xác suất vào cấu trúc của lý thuyết theo một cách chính xác.

## Lượng tử hóa: vì sao một số đại lượng nhận giá trị rời rạc?

Từ “lượng tử” ban đầu gắn với ý tưởng một số trao đổi năng lượng xảy ra theo các gói rời rạc. Trong mô hình Planck ban đầu cho bộ dao động điện từ,

```math
E_n=nhf,
```

với `n=0,1,2,...`.

Về sau, ta hiểu hiện tượng rời rạc sâu hơn. Trong nhiều bài toán lượng tử, các giá trị cho phép xuất hiện do trạng thái phải thỏa đồng thời phương trình động lực học và điều kiện biên. Về mặt toán học, đây thường là một bài toán trị riêng (eigenvalue problem), tương tự việc một sợi dây cố định hai đầu chỉ cho phép một số mode sóng dừng nhất định.

Điểm quan trọng là không phải mọi đại lượng lượng tử đều rời rạc. Hạt tự do có thể có phổ động lượng liên tục. Vì vậy “lượng tử” không đồng nghĩa với “mọi thứ đều chia thành các bậc rời rạc”.

## Photon và tính lưỡng tính sóng–hạt

Einstein dùng quan hệ

```math
E=hf
```

để giải thích hiệu ứng quang điện. Ánh sáng thể hiện giao thoa và nhiễu xạ như sóng, nhưng trao đổi năng lượng với vật chất theo các lượng tử photon.

Vật chất cũng có tính chất sóng. Quan hệ de Broglie là

```math
\lambda=\frac{h}{p}.
```

Nhiễu xạ electron xác nhận rằng electron không thể được mô tả đầy đủ như một hạt cổ điển có quỹ đạo xác định trong mọi tình huống.

Cụm từ “lưỡng tính sóng–hạt” hữu ích về lịch sử nhưng dễ gây hiểu nhầm. Một hệ lượng tử không phải lúc thì “biến thành sóng”, lúc thì “biến thành hạt”. Chính xác hơn, hệ được mô tả bằng một trạng thái lượng tử; mô hình sóng và mô hình hạt chỉ là hai trực giác cổ điển nắm bắt được những khía cạnh khác nhau của cùng hệ.

## Trạng thái lượng tử và hàm sóng

Trong biểu diễn vị trí của một hạt, trạng thái thuần có thể được biểu diễn bằng hàm sóng (wavefunction / 파동함수):

```math
\psi(x,t).
```

Hàm sóng nói chung là một hàm phức. Bản thân `\psi` không phải xác suất. Quy tắc Born liên hệ hàm sóng với mật độ xác suất:

```math
P(x,t)=|\psi(x,t)|^2.
```

Để tổng xác suất tìm thấy hạt ở đâu đó bằng 1, trạng thái phải được chuẩn hóa:

```math
\int_{-\infty}^{\infty}|\psi(x,t)|^2dx=1.
```

Nếu xét một khoảng từ `a` đến `b`, xác suất tìm thấy hạt trong khoảng đó là

```math
P(a\le x\le b)=\int_a^b|\psi(x,t)|^2dx.
```

Do đó hàm sóng không chỉ là một “đường cong dao động”; nó là đối tượng từ đó lý thuyết sinh ra xác suất cho phép đo vị trí.

## Vì sao số phức xuất hiện?

Số phức cho phép pha được mã hóa trực tiếp trong biên độ lượng tử. Khi hai khả năng kết hợp,

```math
\psi=\psi_1+\psi_2,
```

xác suất không phải chỉ là tổng hai xác suất riêng lẻ:

```math
|\psi_1+\psi_2|^2
=|\psi_1|^2+|\psi_2|^2
+\psi_1^*\psi_2+\psi_2^*\psi_1.
```

Hai hạng chéo cuối phụ thuộc pha tương đối và tạo ra giao thoa. Nếu chỉ cộng xác suất cổ điển `|\psi_1|^2+|\psi_2|^2`, thông tin pha bị mất và hình giao thoa không thể xuất hiện.

Vì vậy phần phức của trạng thái không phải một thủ thuật tính toán tùy ý; nó mang thông tin vật lý về pha và sự chồng chập.

## Chồng chập lượng tử

Nếu `|a\rangle` và `|b\rangle` là hai trạng thái cơ sở, một trạng thái lượng tử có thể là

```math
|\psi\rangle=\alpha|a\rangle+\beta|b\rangle,
```

với

```math
|\alpha|^2+|\beta|^2=1.
```

Chồng chập (superposition / 중첩) là tổ hợp tuyến tính trong không gian trạng thái. Nếu đo trong chính cơ sở `|a\rangle, |b\rangle`, các xác suất tương ứng là `|\alpha|^2` và `|\beta|^2`.

Điểm quan trọng là hệ số `\alpha,\beta` còn mang pha tương đối. Vì vậy một chồng chập kết hợp (coherent superposition) chứa nhiều thông tin hơn một hỗn hợp thống kê cổ điển chỉ cho biết xác suất xuất hiện của từng trạng thái.

Không nên hình dung chồng chập như một vật thể cổ điển bị “chẻ đôi” thành hai phần vật chất. Nó là cấu trúc của trạng thái lượng tử trong không gian Hilbert.

## Phương trình Schrödinger

Phương trình Schrödinger phụ thuộc thời gian là

```math
i\hbar\frac{\partial}{\partial t}\psi(\mathbf r,t)
=\hat H\psi(\mathbf r,t),
```

trong đó

```math
\hbar=\frac{h}{2\pi}
```

và `\hat H` là toán tử Hamiltonian. Hamiltonian vừa đại diện cho năng lượng của hệ, vừa là toán tử sinh tiến hóa theo thời gian của hệ kín không tương đối tính.

Với một hạt không tương đối tính chuyển động trong thế `V(\mathbf r,t)`, Hamiltonian thường có dạng

```math
\hat H=-\frac{\hbar^2}{2m}\nabla^2+V(\mathbf r,t).
```

Do đó

```math
i\hbar\frac{\partial\psi}{\partial t}
=\left[-\frac{\hbar^2}{2m}\nabla^2+V\right]\psi.
```

Phương trình này không phải Newton II được viết bằng ký hiệu khác. Newton mô tả quỹ đạo `x(t)` của chất điểm cổ điển; Schrödinger mô tả sự tiến hóa của biên độ trạng thái lượng tử.

## Vì sao toán tử động năng chứa Laplacian?

Trong biểu diễn vị trí, toán tử động lượng là

```math
\hat{\mathbf p}=-i\hbar\nabla.
```

Từ quan hệ động năng cổ điển

```math
K=\frac{p^2}{2m},
```

ta thu được toán tử động năng

```math
\hat K=\frac{\hat p^2}{2m}
=-\frac{\hbar^2}{2m}\nabla^2.
```

Laplacian `\nabla^2\psi` đo độ cong không gian của hàm sóng. Một trạng thái biến thiên rất nhanh theo không gian thường chứa thành phần động lượng lớn hơn, vì biến thiên không gian mạnh tương ứng với phổ số sóng rộng hoặc số sóng lớn.

Đây là một cầu nối quan trọng giữa Fourier, động lượng và động năng lượng tử.

## Đại lượng quan sát và toán tử

Một đại lượng có thể đo được, hay đại lượng quan sát (observable / 관측가능량), được biểu diễn bằng một toán tử Hermitian `\hat A`.

Bài toán trị riêng có dạng

```math
\hat A|a_n\rangle=a_n|a_n\rangle.
```

Các trị riêng `a_n` là những giá trị có thể xuất hiện khi đo `A` trong trường hợp phổ rời rạc.

Nếu trạng thái được khai triển theo cơ sở riêng của `\hat A`:

```math
|\psi\rangle=\sum_n c_n|a_n\rangle,
```

thì xác suất thu được kết quả `a_n` là

```math
P(a_n)=|c_n|^2.
```

Giá trị kỳ vọng là

```math
\langle A\rangle=\langle\psi|\hat A|\psi\rangle.
```

Giá trị kỳ vọng không nhất thiết là kết quả của một phép đo riêng lẻ. Nó là trung bình dự đoán nếu ta chuẩn bị cùng một trạng thái nhiều lần và lặp phép đo dưới cùng điều kiện.

## Commutator và nguyên lý bất định

Với hai toán tử `\hat A` và `\hat B`, commutator được định nghĩa là

```math
[\hat A,\hat B]=\hat A\hat B-\hat B\hat A.
```

Vị trí và động lượng thỏa

```math
[\hat x,\hat p]=i\hbar.
```

Từ cấu trúc này suy ra quan hệ bất định Heisenberg:

```math
\Delta x\,\Delta p\ge\frac{\hbar}{2}.
```

`\Delta x` và `\Delta p` là độ lệch chuẩn của phân bố kết quả đo vị trí và động lượng trong cùng một trạng thái, không phải “sai số của dụng cụ” theo nghĩa thông thường.

## Liên hệ Fourier của độ bất định

Một gói sóng hẹp trong không gian cần nhiều thành phần số sóng `k` để tổng hợp. Vì

```math
p=\hbar k,
```

phân bố động lượng sẽ rộng hơn. Ngược lại, một trạng thái gần đơn sắc về `k` phải lan rộng trong không gian.

Điều này không phải toàn bộ nội dung của nguyên lý bất định, nhưng nó cung cấp trực giác toán học rất mạnh cho cặp vị trí–động lượng.

## Miền áp dụng và giới hạn của phương trình Schrödinger

Phương trình Schrödinger dạng trên là lý thuyết **không tương đối tính**. Nó phù hợp khi vận tốc đặc trưng nhỏ so với tốc độ ánh sáng và khi quá trình không đòi hỏi tạo–hủy hạt.

Khi hiệu ứng tương đối tính trở nên quan trọng, cần các phương trình như Klein–Gordon hoặc Dirac; khi số hạt không còn cố định và tạo–hủy hạt trở thành một phần cơ bản của hiện tượng, mô tả tự nhiên hơn là lý thuyết trường lượng tử (quantum field theory).

Ngoài ra, mô tả bằng một hàm sóng đơn phù hợp nhất cho trạng thái thuần. Hệ mở tương tác mạnh với môi trường thường cần ma trận mật độ (density matrix) và động lực học hệ mở.

## Điều kiện biên có ý nghĩa vật lý

Trong nhiều bài toán lượng tử, điều kiện biên quyết định phổ năng lượng. Ví dụ trong giếng thế vô hạn một chiều dài `L`, yêu cầu

```math
\psi(0)=\psi(L)=0
```

chỉ cho phép các mode có số sóng rời rạc. Vì thế năng lượng cũng rời rạc.

Điều này minh họa một nguyên tắc chung: **lượng tử hóa nhiều khi xuất hiện từ sự kết hợp giữa phương trình động lực học và điều kiện biên**, chứ không phải vì ta “ép” các con số thành số nguyên một cách tùy ý.

## Mô hình tư duy (Mental Model)

Trạng thái lượng tử không phải một danh sách các đại lượng cổ điển bị che giấu. Nó là đối tượng toán học từ đó ta suy ra biên độ xác suất cho các kết quả đo. Chồng chập, pha và tính không giao hoán của các toán tử là cấu trúc bên trong của lý thuyết, không phải lỗi do dụng cụ thiếu chính xác.

Có thể hình dung chuỗi mô tả như sau:

```text
chuẩn bị trạng thái
→ tiến hóa theo Hamiltonian
→ chọn đại lượng quan sát
→ phân bố xác suất kết quả đo
→ so sánh thống kê với thí nghiệm
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nguyên lý bất định chỉ do phép đo làm hạt bị nhiễu”

Không. Nhiễu do thiết bị có thể tồn tại, nhưng quan hệ bất định còn đúng ở mức cấu trúc trạng thái, ngay cả trước khi ta mô hình hóa chi tiết thiết bị đo.

### “Hàm sóng là một đám vật chất thật bị trải ra trong không gian”

Không nên diễn giải như vậy một cách trực tiếp. `\psi` là biên độ trạng thái phức; đại lượng trực tiếp nối với xác suất vị trí là `|\psi|^2`.

### “Mọi đại lượng lượng tử đều rời rạc”

Sai. Một số phổ là rời rạc, một số liên tục và một số có cả phần rời rạc lẫn liên tục. Hình dạng phổ phụ thuộc Hamiltonian và điều kiện biên.

### “Giá trị kỳ vọng là giá trị chắc chắn sẽ đo được”

Không. Giá trị kỳ vọng là trung bình thống kê qua nhiều phép chuẩn bị và đo lặp lại. Một phép đo đơn có thể cho một trị riêng khác xa giá trị kỳ vọng.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md), [Sóng và Fourier](../02_oscillations_waves/01_waves_fourier_sound.md).

**Liên hệ tiếp:** [Các hệ lượng tử mẫu](01_quantum_systems.md), [Phép đo, rối và mất kết hợp](03_measurement_entanglement_decoherence.md), [Đối xứng, toán tử và tích phân đường](07_symmetry_operator_path_integral.md).
