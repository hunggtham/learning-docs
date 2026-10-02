# Chuyển động quay, mômen lực và mômen động lượng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Chuyển động quay, mômen lực và mômen động lượng**. Route đi từ translation/rotation analogy → torque/angular acceleration → moment of inertia → angular momentum → rigid-body energy and constraints, để quay nối động lực học với hình học.

Chuyển động quay không phải một tập công thức tách biệt khỏi cơ học tịnh tiến. Nó là cùng lô-gic (logic / 논리) Newton–năng lượng–bảo toàn nhưng hình học của vật mở rộng khiến phân bố khối lượng quanh trục trở nên quan trọng.

## Từ tịnh tiến sang quay

Một số cặp tương ứng hữu ích là:

| Tịnh tiến | Chuyển động quay |
|---|---|
| vị trí `x` | góc `\theta` |
| vận tốc `v` | vận tốc góc `\omega` |
| gia tốc `a` | gia tốc góc `\alpha` |
| khối lượng `m` | mômen quán tính `I` |
| lực `F` | mômen lực `\tau` |
| động lượng `p` | mômen động lượng `L` |
| `K=mv^2/2` | `K_{rot}=I\omega^2/2` |

Sự tương tự này hữu ích nhưng không hoàn hảo. Ví dụ mômen động lượng và vận tốc góc của một vật rắn tổng quát không nhất thiết cùng phương. Muốn hiểu chuyển động quay ba chiều cần tensor quán tính chứ không chỉ một số `I`.

> **Chuyển mạch:** Trong **Chuyển động quay, mômen lực và mômen động lượng**, **Radian là đơn vị tự nhiên của góc** tiếp nhận điểm tựa từ **Từ tịnh tiến sang quay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động học quay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Radian là đơn vị tự nhiên của góc

Radian được định nghĩa bởi

```math
\theta=\frac{s}{r},
```

với `s` là độ dài cung. Vì là tỉ số hai chiều dài, radian không có thứ nguyên.

Giải tích lượng giác có dạng tự nhiên khi góc đo bằng radian:

```math
\frac{d}{d\theta}\sin\theta=\cos\theta.
```

Đây là lý do các công thức `v=\omega r` hay `a_t=\alpha r` sử dụng trực tiếp `\theta` theo radian.

> **Chuyển mạch:** Ở chặng này của **Chuyển động quay, mômen lực và mômen động lượng**, **Động học quay** tiếp nhận điểm tựa từ **Radian là đơn vị tự nhiên của góc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mômen lực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động học quay

Sau khi mô tả vị trí và vận tốc tuyến tính, ta đổi sang góc, tốc độ góc và gia tốc góc. Phần này đặt các đại lượng quay cạnh đại lượng tịnh tiến để thấy phép tương tự và giới hạn của nó.

```math
\omega=\frac{d\theta}{dt},
```

```math
\alpha=\frac{d\omega}{dt}.
```

Một điểm cách trục một khoảng `r` có tốc độ tiếp tuyến

```math
v=\omega r
```

và gia tốc tiếp tuyến

```math
a_t=\alpha r.
```

Ngay cả khi `\omega` không đổi, hướng vận tốc vẫn thay đổi nên còn gia tốc hướng tâm

```math
a_c=\omega^2r=\frac{v^2}{r}.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuyển động quay, mômen lực và mômen động lượng**, **Mômen lực** tiếp nhận điểm tựa từ **Động học quay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao τ=Iα xuất hiện?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mômen lực

Mômen lực (torque / 돌림힘) được định nghĩa

```math
\vec\tau=\vec r\times\vec F.
```

Độ lớn là

```math
\tau=rF\sin\phi=F\ell,
```

trong đó `\ell` là cánh tay đòn vuông góc từ trục tới đường tác dụng của lực.

Cùng một lực có thể tạo hiệu ứng quay rất khác nhau tùy vị trí đặt lực. Đây là lý do tay nắm cửa đặt xa bản lề.

> **Chuyển mạch:** Trong **Chuyển động quay, mômen lực và mômen động lượng**, **Vì sao τ=Iα xuất hiện?** tiếp nhận điểm tựa từ **Mômen lực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mômen quán tính phụ thuộc trục quay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao `τ=Iα` xuất hiện?

Xét một vật rắn quay quanh trục cố định. Với phần tử khối lượng `m_i` ở khoảng cách `r_i`, gia tốc tiếp tuyến là

```math
a_{t,i}=\alpha r_i.
```

Thành phần lực tiếp tuyến cần thiết là

```math
F_{t,i}=m_i\alpha r_i.
```

Mômen lực của phần tử đó:

```math
\tau_i=r_iF_{t,i}=m_ir_i^2\alpha.
```

Cộng trên toàn vật:

```math
\sum_i\tau_i=\left(\sum_i m_ir_i^2\right)\alpha.
```

Do đó

```math
\tau=I\alpha,
```

với

```math
I=\sum_i m_ir_i^2.
```

`I` xuất hiện vì khối lượng ở xa trục khó tăng tốc góc hơn theo hệ số `r^2`.

> **Chuyển mạch:** Ở chặng này của **Chuyển động quay, mômen lực và mômen động lượng**, **Mômen quán tính phụ thuộc trục quay** tiếp nhận điểm tựa từ **Vì sao τ=Iα xuất hiện?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Định lý trục song song** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mômen quán tính phụ thuộc trục quay

Với phân bố liên tục,

```math
I=\int r_\perp^2\,dm.
```

`r_\perp` là khoảng cách vuông góc tới trục quay. Vì vậy `I` không chỉ là thuộc tính của vật mà còn của **vật + trục đang chọn**.

Ví dụ:

- vành mỏng: `I=MR^2`;
- đĩa đặc quanh trục trung tâm: `I=\frac12MR^2`;
- thanh mảnh quanh tâm: `I=\frac1{12}ML^2`.

Cùng `M` và `R`, vành có `I` lớn hơn đĩa vì nhiều khối lượng nằm xa trục hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuyển động quay, mômen lực và mômen động lượng**, **Định lý trục song song** tiếp nhận điểm tựa từ **Mômen quán tính phụ thuộc trục quay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động năng quay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Định lý trục song song

Nếu biết mômen quán tính quanh trục đi qua tâm khối,

```math
I=I_{cm}+Md^2,
```

với `d` là khoảng cách giữa hai trục song song.

Định lý này rất hữu ích khi vật quay quanh bản lề hoặc trục không đi qua tâm khối.

> **Chuyển mạch:** Trong **Chuyển động quay, mômen lực và mômen động lượng**, **Động năng quay** tiếp nhận điểm tựa từ **Định lý trục song song** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mômen động lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động năng quay

Mỗi phần tử có tốc độ `v_i=\omega r_i`, nên

```math
K=\sum_i\frac12m_iv_i^2
=\frac12\omega^2\sum_i m_ir_i^2.
```

Do đó

```math
K_{rot}=\frac12I\omega^2.
```

Công của mômen lực thỏa

```math
dW=\tau\,d\theta,
```

và công suất quay là

```math
P=\tau\omega.
```

Đây là phiên bản quay của `dW=Fdx` và `P=Fv`.

> **Chuyển mạch:** Ở chặng này của **Chuyển động quay, mômen lực và mômen động lượng**, **Mômen động lượng** tiếp nhận điểm tựa từ **Động năng quay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tensor quán tính và trục chính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mômen động lượng

Đối với chất điểm,

```math
\vec L=\vec r\times\vec p.
```

Định luật động lực học tổng quát là

```math
\vec\tau_{ext}=\frac{d\vec L}{dt}.
```

Nếu mômen lực ngoài bằng không,

```math
\vec L=\text{hằng số}.
```

Bảo toàn mômen động lượng là nguyên lý tổng quát hơn công thức `L=I\omega`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuyển động quay, mômen lực và mômen động lượng**, **Tensor quán tính và trục chính** tiếp nhận điểm tựa từ **Mômen động lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiện tượng “vợt tennis”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tensor quán tính và trục chính

Trong chuyển động quay ba chiều,

```math
\vec L=\mathbf I\,\vec\omega,
```

trong đó `\mathbf I` là tensor quán tính (inertia tensor). Chỉ khi quay quanh một trục chính (principal axis) thì `\vec L` song song với `\vec\omega` và có thể viết đơn giản

```math
L=I\omega.
```

Tensor quán tính giải thích vì sao một vật có hình dạng bất đối xứng có thể có chuyển động quay phức tạp dù không chịu mômen lực ngoài.

> **Chuyển mạch:** Trong **Chuyển động quay, mômen lực và mômen động lượng**, **Hiện tượng “vợt tennis”** tiếp nhận điểm tựa từ **Tensor quán tính và trục chính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo toàn mômen động lượng và người trượt băng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiện tượng “vợt tennis”

Một vật rắn tự do có ba trục chính với ba mômen quán tính `I_1<I_2<I_3`. Quay gần trục có `I_1` nhỏ nhất hoặc `I_3` lớn nhất thường ổn định, còn quay gần trục trung gian `I_2` có thể không ổn định.

Đây là định lý trục trung gian (intermediate-axis theorem), thường được thấy khi ném một quyển sách hoặc vợt tennis lên không: quay quanh một trục có thể đột ngột lật hướng.

Hiện tượng này cho thấy chuyển động quay ba chiều không thể hiểu đầy đủ chỉ bằng trực giác `τ=Iα` một chiều.

> **Chuyển mạch:** Ở chặng này của **Chuyển động quay, mômen lực và mômen động lượng**, **Bảo toàn mômen động lượng và người trượt băng** tiếp nhận điểm tựa từ **Hiện tượng “vợt tennis”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Con quay và tiến động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo toàn mômen động lượng và người trượt băng

Khi một vận động viên kéo tay vào, mômen quán tính giảm. Nếu mômen lực ngoài nhỏ,

```math
I_i\omega_i=I_f\omega_f.
```

Do `I_f<I_i`, ta có `\omega_f>\omega_i`.

Động năng không nhất thiết bảo toàn trong thao tác này. Người trượt băng thực hiện công bằng cơ bắp để kéo tay vào, nên năng lượng quay có thể tăng dù mômen động lượng bảo toàn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuyển động quay, mômen lực và mômen động lượng**, **Con quay và tiến động** tiếp nhận điểm tựa từ **Bảo toàn mômen động lượng và người trượt băng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lăn không trượt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Con quay và tiến động

Một con quay quay nhanh có mômen động lượng lớn. Nếu trọng lực tạo mômen lực gần vuông góc với `\vec L`, mômen lực chủ yếu đổi **hướng** của `\vec L` thay vì làm giảm nhanh độ lớn của nó.

Kết quả là trục quay tiến động (precession). Trong mô hình đơn giản,

```math
\Omega_p\approx\frac{\tau}{L}.
```

Hiện tượng này xuất hiện trong con quay hồi chuyển, vệ tinh, động lực học hành tinh và cảm biến quán tính.

> **Chuyển mạch:** Trong **Chuyển động quay, mômen lực và mômen động lượng**, **Lăn không trượt** tiếp nhận điểm tựa từ **Con quay và tiến động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vai trò của ma sát tĩnh khi lăn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lăn không trượt

Điều kiện lăn không trượt là

```math
v_{cm}=\omega R.
```

Tổng động năng gồm phần tịnh tiến và quay:

```math
K=\frac12Mv_{cm}^2+\frac12I_{cm}\omega^2.
```

Nếu vật lăn từ độ cao `h` xuống mà không mất năng lượng,

```math
Mgh=\frac12Mv^2+\frac12I\frac{v^2}{R^2}.
```

Suy ra

```math
v^2=\frac{2gh}{1+I/(MR^2)}.
```

Vật có `I/(MR^2)` lớn hơn sẽ có tốc độ tâm khối nhỏ hơn tại cùng độ cao vì nhiều năng lượng nằm trong chuyển động quay.

> **Chuyển mạch:** Ở chặng này của **Chuyển động quay, mômen lực và mômen động lượng**, **Vai trò của ma sát tĩnh khi lăn** tiếp nhận điểm tựa từ **Lăn không trượt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ: đĩa đặc lăn xuống dốc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vai trò của ma sát tĩnh khi lăn

Trong lăn không trượt trên bề mặt cố định, điểm tiếp xúc tức thời có vận tốc bằng không so với mặt đất. Vì vậy ma sát tại tiếp xúc có thể là ma sát tĩnh và không nhất thiết tiêu tán cơ năng.

Hướng của ma sát không thể đoán chỉ từ hướng chuyển động tâm khối; phải xét xu hướng trượt tương đối tại điểm tiếp xúc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuyển động quay, mômen lực và mômen động lượng**, **Vai trò của ma sát tĩnh khi lăn** cho ta quy tắc; **Ví dụ: đĩa đặc lăn xuống dốc** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ: đĩa đặc lăn xuống dốc

Với đĩa đặc

```math
I=\frac12MR^2.
```

Dọc mặt phẳng nghiêng:

```math
Mg\sin\theta-f=Ma.
```

Phương trình quay quanh tâm:

```math
fR=I\alpha.
```

Điều kiện không trượt:

```math
a=\alpha R.
```

Suy ra

```math
f=\frac12Ma.
```

Thế vào phương trình tịnh tiến:

```math
Mg\sin\theta-\frac12Ma=Ma,
```

nên

```math
a=\frac23g\sin\theta.
```

Gia tốc nhỏ hơn `g\sin\theta` của một vật trượt không ma sát vì một phần năng lượng đi vào quay.

> **Chuyển mạch:** Trong **Chuyển động quay, mômen lực và mômen động lượng**, **Ví dụ: đĩa đặc lăn xuống dốc** cho ta quy tắc; **Mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Chuyển động quay là cơ học của **phân bố khối lượng và hình học quanh trục**. Mômen lực đo khả năng thay đổi mômen động lượng; mômen quán tính đo cách khối lượng được phân bố; còn bảo toàn mômen động lượng là hệ quả sâu hơn của đối xứng quay.

> **Chuyển mạch:** Ở chặng này của **Chuyển động quay, mômen lực và mômen động lượng**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Mômen quán tính chỉ phụ thuộc vật”

Sai. Nó phụ thuộc cả trục quay.

### “Nếu mômen động lượng bảo toàn thì động năng cũng bảo toàn”

Không. Một hệ có thể thay đổi `I` bằng nội công, làm `K` thay đổi trong khi `L` vẫn giữ nguyên.

### “Ma sát khi lăn luôn làm mất năng lượng”

Không. Ma sát tĩnh trong lăn không trượt có thể không sinh công tại điểm tiếp xúc với mặt đất.

### “L luôn song song với ω”

Chỉ đúng đơn giản khi quay quanh trục chính hoặc trong những hình học đủ đối xứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuyển động quay, mômen lực và mômen động lượng**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Động học](00_kinematics.md), [Các lực thường gặp](02_common_forces.md), [Công và năng lượng](03_work_energy_power.md).

**Liên hệ tiếp:** [Cơ học giải tích](08_analytical_mechanics.md), [Đối xứng và bảo toàn](../00_foundations/04_symmetry_conservation_scale.md), [Dao động ghép và mode chuẩn](../02_oscillations_waves/02_coupled_oscillators_normal_modes.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
