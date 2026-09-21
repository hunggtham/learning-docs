# Hệ quy chiếu phi quán tính: gia tốc, Coriolis, ly tâm và vật lý trên Trái Đất

## Vì sao cần một chương riêng về hệ quy chiếu phi quán tính?

Định luật Newton có dạng đơn giản nhất trong **hệ quy chiếu quán tính (inertial frame / 관성계)**. Tuy nhiên, nhiều hệ mà ta trực tiếp sống và đo đạc lại không quán tính: ô tô tăng tốc, thang máy, bàn quay hay chính Trái Đất đang tự quay.

Nếu dùng trực tiếp

```math
\sum \mathbf F=m\mathbf a
```

mà không phân biệt gia tốc của vật với gia tốc của hệ tọa độ, ta có thể gán sai nguyên nhân cho chuyển động.

Cần tách hai câu hỏi:

- tương tác vật lý nào thực sự tác dụng lên vật;
- hệ tọa độ của người quan sát đang tịnh tiến hoặc quay như thế nào.

Lực quán tính không phải một tương tác cơ bản mới. Nó là hạng hiệu chỉnh giúp phương trình trong hệ phi quán tính có dạng giống Newton.

## Hệ quy chiếu tịnh tiến có gia tốc

Giả sử hệ `S'` có gốc tọa độ tại `\mathbf R(t)` so với hệ quán tính `S`. Nếu vị trí của vật trong `S'` là `\mathbf r'`, thì

```math
\mathbf r=\mathbf R(t)+\mathbf r'.
```

Lấy hai đạo hàm theo thời gian:

```math
\mathbf a=\mathbf A+\mathbf a',
```

với

```math
\mathbf A=\ddot{\mathbf R}
```

là gia tốc của chính hệ `S'`.

Trong hệ quán tính,

```math
m\mathbf a=\sum\mathbf F_{real}.
```

Thay biểu thức gia tốc vào,

```math
m\mathbf a'
=\sum\mathbf F_{real}-m\mathbf A.
```

Người quan sát trong `S'` có thể giữ dạng Newton bằng cách đưa vào lực quán tính

```math
\mathbf F_{inertial}=-m\mathbf A.
```

Khi ô tô tăng tốc về phía trước, hành khách có cảm giác bị kéo về sau. Trong hệ gắn với mặt đất, ghế phải tác dụng lực về trước để tăng tốc cơ thể. Trong hệ gắn với xe, ta thêm lực quán tính hướng về sau để mô tả cùng chuyển động tương đối.

## Thang máy và trọng lượng biểu kiến

Một người khối lượng `m` đứng trên cân trong thang máy. Cân đo phản lực pháp tuyến `N`, không trực tiếp đo lực hấp dẫn `mg`.

Nếu thang máy gia tốc lên với độ lớn `a`, trong hệ quán tính gắn với mặt đất:

```math
N-mg=ma,
```

nên

```math
N=m(g+a).
```

Nếu thang máy gia tốc xuống,

```math
N=m(g-a).
```

Trong rơi tự do với `a=g`,

```math
N=0.
```

Đây là trạng thái không trọng lượng biểu kiến, không phải trường hấp dẫn bằng không. Phân biệt này là bước chuẩn bị trực giác cho nguyên lý tương đương trong thuyết tương đối rộng.

## Vì sao hệ quay sinh thêm nhiều hạng gia tốc?

Trong một hệ quay với vận tốc góc `\boldsymbol\Omega`, các vectơ cơ sở cũng thay đổi theo thời gian. Với một vectơ `\mathbf A`, đạo hàm trong hai hệ liên hệ bởi

```math
\left(\frac{d\mathbf A}{dt}\right)_{inertial}
=
\left(\frac{d\mathbf A}{dt}\right)_{rot}
+
\boldsymbol\Omega\times\mathbf A.
```

Áp dụng hai lần cho vị trí, ta thu được

```math
\mathbf a
=
\mathbf A_O
+
\mathbf a'
+
2\boldsymbol\Omega\times\mathbf v'
+
\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r')
+
\dot{\boldsymbol\Omega}\times\mathbf r'.
```

Ngoài gia tốc tương đối `\mathbf a'`, các hạng còn lại lần lượt đến từ:

- gia tốc tịnh tiến của gốc tọa độ;
- hiệu ứng Coriolis;
- hiệu ứng ly tâm;
- hiệu ứng Euler khi tốc độ quay thay đổi.

Các hạng này sinh ra từ hình học của hệ tọa độ phụ thuộc thời gian, không phải từ một tương tác mới giữa các vật.

## Lực Coriolis

Trong hệ quay, lực Coriolis là

```math
\mathbf F_C=-2m\boldsymbol\Omega\times\mathbf v'.
```

Nó chỉ xuất hiện khi vật có vận tốc tương đối `\mathbf v'` trong hệ quay. Vì tích có hướng luôn vuông góc với `\mathbf v'`,

```math
P_C=\mathbf F_C\cdot\mathbf v'=0.
```

Do đó lực Coriolis không trực tiếp sinh công tức thời lên vật trong chính hệ quay; nó chủ yếu đổi hướng chuyển động.

Trên Trái Đất, Coriolis ảnh hưởng rõ ở các dòng khí quyển và đại dương quy mô lớn. Ở Bắc bán cầu, chuyển động ngang có xu hướng lệch sang phải so với hướng chuyển động; ở Nam bán cầu lệch sang trái.

Không nên áp dụng máy móc quy tắc này cho mọi chuyển động nhỏ. Trong bồn rửa hay các thí nghiệm ngắn, hình học bình chứa, dòng ban đầu và độ nhớt thường mạnh hơn hiệu ứng Coriolis nhiều lần.

## Lực ly tâm và thế hiệu dụng

Lực ly tâm trong hệ quay là

```math
\mathbf F_{cf}
=-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r').
```

Nếu hệ quay đều quanh trục `z`, độ lớn trong mặt phẳng vuông góc trục là

```math
F_{cf}=m\Omega^2r_\perp.
```

Hướng của nó ra xa trục quay.

Lực ly tâm có thể được biểu diễn bằng thế hiệu dụng

```math
U_{cf}=-\frac12m\Omega^2r_\perp^2.
```

Vì vậy trong hệ quay, ta có thể cộng thế ly tâm với các thế thật để tìm điểm cân bằng.

Các điểm Lagrange trong bài toán ba vật hạn chế là ví dụ quan trọng: thế hấp dẫn của hai vật lớn kết hợp với thế ly tâm trong hệ cùng quay tạo nên các điểm đứng yên tương đối.

## Lực Euler

Khi `\boldsymbol\Omega` thay đổi theo thời gian, xuất hiện lực Euler

```math
\mathbf F_E=-m\dot{\boldsymbol\Omega}\times\mathbf r'.
```

Nếu một bàn quay bắt đầu tăng tốc góc, vật trên bàn có xu hướng “tụt lại” theo phương tiếp tuyến trong hệ cùng quay. Hạng Euler mô tả chính hiệu ứng này.

## Con lắc Foucault: quan sát Trái Đất quay bằng cơ học

Với một con lắc Foucault lý tưởng, mặt phẳng dao động gần như giữ hướng trong không gian quán tính trong khi Trái Đất quay bên dưới. Người quan sát trên Trái Đất vì vậy thấy mặt phẳng dao động tiến động.

Ở vĩ độ `\lambda`, tốc độ góc tiến động xấp xỉ

```math
\Omega_F=\Omega_E\sin\lambda.
```

Tại cực, mặt phẳng dao động quay tương đối gần một vòng trong một ngày thiên văn. Tại xích đạo, hiệu ứng bậc nhất này bằng không.

Đây là một thí nghiệm đẹp vì nó biến chuyển động quay toàn cầu của Trái Đất thành một hiệu ứng cơ học đo được tại chỗ.

## Hiệu ứng Eötvös và trọng lực hiệu dụng

Một vật chuyển động về phía đông hoặc tây trên Trái Đất quay có thêm thành phần Coriolis theo phương thẳng đứng. Vì vậy trọng lượng biểu kiến thay đổi rất nhỏ tùy hướng và tốc độ chuyển động.

Trong trắc địa chính xác và dẫn đường, “trọng lực” đo được thường là tổng của trường hấp dẫn, hiệu ứng quay của Trái Đất và ảnh hưởng hình dạng không cầu hoàn hảo của Trái Đất.

Gia tốc trọng trường hiệu dụng nhỏ hơn gần xích đạo không chỉ do lực ly tâm mà còn do Trái Đất phình ra ở xích đạo, khiến khoảng cách tới tâm lớn hơn.

## Cân bằng địa chuyển

Trong khí quyển và đại dương quy mô lớn, gia tốc cục bộ có thể nhỏ hơn nhiều so với lực do gradient áp suất và Coriolis. Khi đó có thể xuất hiện cân bằng gần đúng

```math
-\frac{1}{\rho}\nabla_h p
-2\boldsymbol\Omega\times\mathbf v
\approx0.
```

Kết quả là gió hoặc dòng biển có thể chạy gần song song với các đường đẳng áp thay vì trực tiếp từ áp suất cao sang áp suất thấp.

Đây là ví dụ cho thấy lực quán tính có thể là một phần thiết yếu của mô hình rút gọn rất hữu ích khi hệ quy chiếu tự nhiên của bài toán là hệ gắn với Trái Đất.

## Ví dụ định lượng: độ lệch của vật rơi

Giả sử vật được thả từ độ cao `h`. Bỏ qua lực cản không khí và coi `g` không đổi, thời gian rơi bậc không là

```math
t_f\approx\sqrt{\frac{2h}{g}}.
```

Trong hệ gắn với Trái Đất, vận tốc rơi tạo gia tốc Coriolis ngang có bậc độ lớn

```math
a_C\sim2\Omega_Ev_z.
```

Vì `v_z` tăng trong quá trình rơi, không thể coi `a_C` là hằng số rồi dùng đơn giản `a_Ct^2/2`. Cần tích phân phương trình chuyển động hoặc dùng nhiễu loạn quanh nghiệm rơi tự do.

Tham số nhỏ tự nhiên của bài toán là

```math
\Omega_Et_f.
```

Nếu tham số này rất nhỏ, Coriolis chỉ là hiệu chỉnh bậc thấp. Đây là cách tiếp cận đúng hơn việc học thuộc một công thức độ lệch riêng lẻ.

## Navigation, IMU và kỹ thuật cảm biến

Đơn vị đo quán tính (Inertial Measurement Unit, IMU) dùng accelerometer và gyroscope để suy ra chuyển động.

Accelerometer đo gia tốc riêng (proper acceleration), không trực tiếp trả về gia tốc tọa độ do trường hấp dẫn. Thuật toán dẫn đường phải kết hợp:

- hướng của thiết bị từ gyroscope;
- mô hình trọng lực;
- tốc độ quay Trái Đất;
- hiệu chỉnh Coriolis;
- phép biến đổi giữa các hệ tọa độ.

Nếu bỏ các hiệu chỉnh này, sai số vị trí tích lũy nhanh trong hệ dẫn đường quán tính chính xác cao.

Đây là cầu nối trực tiếp giữa cơ học cổ điển, sensor fusion và kỹ nghệ phần mềm: sai quy ước trục, dấu hoặc frame có thể phá hỏng kết quả dù cảm biến rất tốt.

## Khi nào nên dùng hệ phi quán tính?

Không có quy tắc rằng hệ quán tính luôn “đúng hơn” về thực hành. Hệ quán tính thường làm định luật cơ bản đơn giản hơn; hệ quay hoặc tăng tốc có thể làm hình học, biên hoặc vật thể cần nghiên cứu đứng yên tương đối.

Ví dụ, phân tích cánh turbine thuận tiện trong hệ quay; phân tích tương tác thật có thể rõ hơn trong hệ phòng thí nghiệm gần quán tính.

Mô hình tốt chọn hệ quy chiếu sao cho phần khó của bài toán trở nên đơn giản mà vẫn ghi đầy đủ các hạng quán tính cần thiết.

## Giới hạn của mô hình

Các công thức trên thuộc cơ học cổ điển và giả sử phép cộng vận tốc Galilei phù hợp. Khi tốc độ gần `c`, cần động học tương đối tính.

Trên Trái Đất, nhiều mô hình coi `\boldsymbol\Omega_E` và `g` không đổi trong một vùng nhỏ. Với bài toán quy mô hành tinh hoặc trắc địa chính xác, phải dùng mô hình trường hấp dẫn, hình dạng Trái Đất và tọa độ địa lý chi tiết hơn.

## Mô hình tư duy (Mental Model)

Lực quán tính là **hệ quả của việc mô tả chuyển động trong một hệ tọa độ tự gia tốc hoặc tự quay**. Trong hệ quay, ngay cả vectơ cơ sở cũng thay đổi theo thời gian; chính phép đạo hàm của cơ sở động sinh ra các hạng Coriolis, ly tâm và Euler.

Có thể dùng quy trình:

```text
chọn hệ quy chiếu
→ xác định hệ có gia tốc/quay không
→ viết quan hệ giữa đạo hàm hai hệ
→ thêm các hạng quán tính cần thiết
→ kiểm tra dấu, hướng và giới hạn khi Ω → 0
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Lực ly tâm là lực giả nên có thể bỏ qua”

Sai khi đang giải bài trong hệ quay. “Giả” chỉ nói nó không đến từ tương tác cơ bản; trong phương trình của hệ quay, hạng này vẫn cần thiết.

### “Coriolis tự tạo năng lượng cho bão”

Không. Coriolis chủ yếu đổi hướng dòng. Năng lượng của khí quyển đến từ chênh lệch áp suất, bức xạ Mặt Trời, nhiệt ẩn và các quá trình khác.

### “Không trọng lượng nghĩa là không còn hấp dẫn”

Không. Không trọng lượng biểu kiến thường nghĩa phản lực đỡ gần bằng không. Vệ tinh trên quỹ đạo vẫn chịu gia tốc hấp dẫn đáng kể.

### “Nước trong mọi bồn rửa quay theo Coriolis”

Không. Ở quy mô nhỏ, điều kiện ban đầu, hình học và ma sát thường chi phối mạnh hơn nhiều.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md), [Chuyển động quay](05_rotation_rigid_body.md).

**Liên hệ tiếp:** [Hấp dẫn và quỹ đạo](06_gravitation_orbits.md), [Cơ học chất lưu](../03_continuum/00_fluids.md), [Thuyết tương đối rộng](../07_relativity/01_general_relativity.md), [Tín hiệu và cảm biến](../12_experimental_computational/01_signals_sampling_noise.md).
