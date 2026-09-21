# Các lực thường gặp: trọng lực, pháp tuyến, ma sát, dây, lò xo và lực cản

Một trong những lỗi lớn nhất khi học cơ học là xem mỗi bài như một bộ công thức riêng. Cách tốt hơn là xem mọi bài Newton như một bài **mô hình hóa tương tác**: chọn hệ, xác định những vật nào đang tương tác với hệ, biểu diễn mỗi tương tác bằng một lực, rồi chiếu tổng lực lên các trục thích hợp.

## Bắt đầu từ sơ đồ lực

Sơ đồ lực hay sơ đồ vật tự do (free-body diagram) là bước tách vật đang xét khỏi môi trường và chỉ vẽ các lực **tác dụng lên chính vật đó**.

Quy trình thực tế là:

1. Chọn vật hoặc hệ cần phân tích.
2. Liệt kê từng vật khác đang tương tác với hệ.
3. Mỗi tương tác được biểu diễn bằng một lực.
4. Chọn hệ trục phù hợp với ràng buộc hoặc hình học.
5. Viết

```math
\sum \vec F = m\vec a.
```

Điều quan trọng là không vẽ “chuyển động” như một lực. Một vật đang đi sang phải không có nghĩa phải có lực sang phải. Lực quyết định **sự thay đổi của vận tốc**, không quyết định sự tồn tại của vận tốc.

## Trọng lực gần mặt đất

Trong vùng gần bề mặt Trái Đất, nếu độ cao thay đổi nhỏ so với bán kính Trái Đất, trọng lực có thể xem gần như đều:

```math
\vec F_g=m\vec g.
```

Áp dụng Newton II cho vật chỉ chịu trọng lực:

```math
m\vec a=m\vec g
```

nên

```math
\vec a=\vec g.
```

Khối lượng triệt tiêu. Đây là lý do trong mô hình không lực cản, mọi vật rơi với cùng gia tốc dù khối lượng khác nhau.

Kết quả này không nói rằng lực hấp dẫn trên mọi vật bằng nhau. Vật nặng hơn chịu lực `mg` lớn hơn, nhưng quán tính `m` của nó cũng lớn hơn đúng cùng tỉ lệ.

## Trọng lượng biểu kiến

Cảm giác “nặng” trong thang máy liên quan tới lực pháp tuyến chứ không phải trọng lực thay đổi đáng kể.

Nếu thang máy tăng tốc lên:

```math
N-mg=ma,
```

suy ra

```math
N=m(g+a).
```

Nếu tăng tốc xuống với độ lớn `a`,

```math
N=m(g-a).
```

Trong rơi tự do lý tưởng, `a=g` nên `N=0`. Đây là trạng thái không trọng lượng biểu kiến (apparent weightlessness), dù trọng lực vẫn tồn tại.

## Lực pháp tuyến là phản ứng ràng buộc

Lực pháp tuyến (normal force / 수직항력) là lực tiếp xúc vuông góc bề mặt. Nó không có một công thức cố định như `N=mg`.

Giá trị của `N` được xác định bởi điều kiện ràng buộc. Nếu một vật nằm trên mặt phẳng nghiêng góc `\theta` và không gia tốc vuông góc mặt phẳng,

```math
N=mg\cos\theta.
```

Nếu có thêm lực kéo xiên lên trên với thành phần vuông góc bề mặt, `N` sẽ nhỏ hơn. Nếu ấn xuống, `N` tăng.

Về vi mô, lực pháp tuyến xuất hiện từ tương tác điện từ giữa các nguyên tử khi các đám mây electron bị ép lại gần. Mô hình cơ học cổ điển nén toàn bộ chi tiết đó thành một lực ràng buộc hiệu dụng.

## Ma sát tĩnh không mặc định bằng `μ_sN`

Ma sát tĩnh (static friction / 정지 마찰력) điều chỉnh để ngăn trượt tương đối đến một giới hạn:

```math
|f_s|\le \mu_sN.
```

Dấu bằng chỉ xảy ra ở ngưỡng sắp trượt. Ví dụ nếu một hộp nằm yên trên sàn ngang và ta đẩy nhẹ `5 N`, ma sát tĩnh có thể chỉ là `5 N`, không phải tự động bằng `\mu_sN`.

Đây là một nguồn sai rất phổ biến: `\mu_sN` là **giá trị cực đại** mà mô hình ma sát tĩnh cho phép, không phải giá trị bắt buộc.

## Ma sát trượt

Trong mô hình Coulomb đơn giản,

```math
f_k=\mu_kN.
```

Hướng của ma sát trượt ngược với vận tốc tương đối giữa hai bề mặt tại vùng tiếp xúc.

Mô hình này có ích nhưng không phải định luật vi mô cơ bản. Ma sát thực tế có thể phụ thuộc vào tốc độ, nhiệt độ, độ nhám, độ sạch bề mặt, bôi trơn, biến dạng dẻo và lịch sử tiếp xúc.

## Vì sao đi bộ cần ma sát tĩnh?

Khi chân đạp mặt đất về phía sau mà không trượt, mặt đất tác dụng ma sát tĩnh lên chân theo hướng về phía trước. Lực này giúp gia tốc tâm khối của cơ thể.

Trên bề mặt trơn, `\mu_s` nhỏ nên lực ngang cực đại

```math
f_{s,max}=\mu_sN
```

nhỏ hơn. Cơ thể khó tạo đủ lực ngang mà không trượt.

## Mặt phẳng nghiêng: bài toán chiếu vectơ

Trọng lực luôn hướng thẳng đứng xuống. Nếu trục `x` chọn dọc mặt phẳng nghiêng góc `\theta`, ta phân tích

```math
mg\sin\theta
```

song song mặt phẳng và

```math
mg\cos\theta
```

vuông góc mặt phẳng.

Không có “lực `mg\sin\theta`” mới xuất hiện. Đây chỉ là một thành phần của cùng vectơ `m\vec g` trên cơ sở tọa độ thuận tiện hơn.

### Điều kiện để vật bắt đầu trượt

Với vật đứng yên trên dốc, xu hướng trượt xuống có độ lớn

```math
mg\sin\theta.
```

Ma sát tĩnh tối đa là

```math
f_{s,max}=\mu_smg\cos\theta.
```

Ngưỡng bắt đầu trượt thỏa

```math
mg\sin\theta=\mu_smg\cos\theta,
```

nên

```math
\tan\theta_c=\mu_s.
```

Đây là một ví dụ cho thấy hệ số ma sát có thể được đo từ một thí nghiệm hình học đơn giản.

## Lực căng dây và ràng buộc

Lực căng (tension / 장력) là lực kéo dọc theo dây hoặc cáp. Với dây lý tưởng không khối lượng, không giãn và ròng rọc không ma sát, lực căng có thể xem như bằng nhau trên toàn dây.

Nhưng nếu ròng rọc có mômen quán tính `I`, hai lực căng ở hai phía có thể khác nhau vì cần mômen lực để làm ròng rọc quay:

```math
(T_1-T_2)R=I\alpha.
```

Vì vậy câu “lực căng luôn bằng nhau” chỉ đúng trong một mô hình lý tưởng cụ thể.

### Ví dụ Atwood

Hai vật `m_1` và `m_2` nối qua ròng rọc lý tưởng. Giả sử `m_2>m_1`.

```math
T-m_1g=m_1a,
```

```math
m_2g-T=m_2a.
```

Cộng hai phương trình:

```math
a=\frac{m_2-m_1}{m_1+m_2}g.
```

Sau đó mới thế lại để tìm `T`. Cách giải này cho thấy lực căng là đại lượng được xác định bởi toàn hệ, không phải một số biết sẵn.

## Lực đàn hồi và định luật Hooke

Gần cân bằng, nhiều hệ đàn hồi có thể tuyến tính hóa:

```math
F=-kx.
```

Dấu âm biểu diễn xu hướng phục hồi. Năng lượng thế đàn hồi tương ứng là

```math
U(x)=\frac12kx^2.
```

Lực Hooke không chỉ dành cho lò xo kim loại. Gần một cực tiểu trơn của thế năng, nhiều hệ có thể được xấp xỉ bởi thế bậc hai và từ đó dẫn đến lực gần tuyến tính.

Khi biến dạng lớn, vật liệu có thể phi tuyến, chảy dẻo, có hysteresis hoặc hỏng. Khi đó `F=-kx` không còn đủ.

## Lực cản trong chất lưu

Lực cản không có một công thức phổ quát duy nhất. Hai mô hình điển hình là:

### Chế độ Reynolds nhỏ

Với một quả cầu nhỏ chuyển động chậm trong chất lưu nhớt,

```math
F_d=6\pi\eta Rv,
```

là định luật Stokes. Lực cản tỉ lệ tuyến tính với `v`.

### Chế độ quán tính chi phối

Ở nhiều tình huống khí động học đời thường,

```math
F_d\approx\frac12\rho C_dAv^2.
```

`C_d` phụ thuộc hình dạng và chế độ dòng chảy. Việc mô hình lực cản tuyến tính hay bậc hai không phải tùy ý; nó liên quan tới số Reynolds và cấu trúc dòng.

## Vận tốc giới hạn

Một vật rơi trong không khí đạt vận tốc giới hạn (terminal velocity) khi tổng lực bằng không.

Với lực cản bậc hai:

```math
mg=\frac12\rho C_dAv_t^2,
```

nên

```math
v_t=\sqrt{\frac{2mg}{\rho C_dA}}.
```

Kết quả giải thích vì sao vật nặng và đặc có thể có vận tốc giới hạn lớn hơn, còn diện tích cản lớn làm vận tốc giới hạn giảm.

Trong nhảy dù, mở dù làm tăng mạnh `A` và thay đổi `C_d`, từ đó giảm `v_t`.

## Lực hướng tâm không phải một loại lực mới

Trong chuyển động tròn, gia tốc hướng tâm có độ lớn

```math
a_c=\frac{v^2}{r}.
```

Do đó tổng thành phần lực theo phương bán kính phải thỏa

```math
\sum F_r=m\frac{v^2}{r}.
```

“Lực hướng tâm” không phải một tương tác mới như trọng lực hay ma sát. Đó là tên gọi cho **hợp lực theo phương bán kính** cần để tạo gia tốc hướng tâm.

Ví dụ xe rẽ trên đường phẳng có thể nhận lực hướng tâm chủ yếu từ ma sát tĩnh. Vệ tinh quay quanh Trái Đất nhận lực hướng tâm từ hấp dẫn.

## Hệ quy chiếu phi quán tính và lực quán tính

Trong hệ quy chiếu đang gia tốc hoặc quay, ta có thể thêm các lực quán tính (inertial forces) để tiếp tục dùng dạng Newton quen thuộc.

Trong hệ quay với vận tốc góc `\vec\Omega`, lực Coriolis có dạng

```math
\vec F_C=-2m\vec\Omega\times\vec v'.
```

Lực ly tâm có dạng

```math
\vec F_{cf}=-m\vec\Omega\times(\vec\Omega\times\vec r).
```

Các lực này không biểu diễn tương tác mới giữa hai vật; chúng xuất hiện vì ta đang dùng một hệ quy chiếu phi quán tính.

## Bài toán mẫu: kéo hộp bằng lực xiên

Một hộp khối lượng `10 kg` được kéo bằng lực `40 N` hợp với phương ngang góc `30°`. Hệ số ma sát trượt `\mu_k=0.20`, lấy `g=9.8 m/s^2`.

Thành phần đứng của lực kéo làm giảm pháp tuyến:

```math
N=mg-F\sin30^\circ
=98-20=78\,N.
```

Ma sát trượt:

```math
f_k=\mu_kN=15.6\,N.
```

Thành phần ngang của lực kéo:

```math
F_x=40\cos30^\circ\approx34.6\,N.
```

Hợp lực ngang:

```math
F_{net,x}=34.6-15.6=19.0\,N.
```

Gia tốc:

```math
a\approx1.90\,m/s^2.
```

Điểm quan trọng là lực kéo xiên không chỉ có thành phần ngang; nó còn thay đổi `N`, từ đó thay đổi cả ma sát.

## Cách kiểm tra một sơ đồ lực

Sau khi vẽ sơ đồ, hãy hỏi:

- Mỗi lực có một vật hoặc trường cụ thể gây ra không?
- Có vô tình vẽ cả lực tác dụng lên vật khác không?
- Có vẽ vận tốc hoặc “lực chuyển động” như một lực không?
- Có dùng `N=mg` mà không kiểm tra phương vuông góc bề mặt không?
- Có đặt `f_s=\mu_sN` trước khi biết vật ở ngưỡng trượt không?

Nếu trả lời được các câu này, phần lớn lỗi cơ học cơ bản sẽ giảm đáng kể.

## Mô hình tư duy (Mental Model)

Tên lực cho biết **cơ chế tương tác hoặc ràng buộc**, còn phương trình Newton cho biết tổng tác dụng của các tương tác đó lên chuyển động. Đừng tìm một công thức cho “tình huống”; hãy xác định hệ, tương tác, ràng buộc và trục tọa độ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Vật đang chuyển động thì phải có lực theo hướng chuyển động”

Sai. Chuyển động thẳng đều có thể xảy ra khi hợp lực bằng không.

### “Pháp tuyến luôn bằng trọng lượng”

Sai. `N` phụ thuộc ràng buộc và gia tốc vuông góc bề mặt.

### “Ma sát luôn ngược chiều chuyển động của vật”

Chính xác hơn, ma sát chống chuyển động tương đối hoặc xu hướng trượt tại bề mặt tiếp xúc. Trong một số hệ như bánh xe chủ động, ma sát tĩnh có thể cùng chiều chuyển động của tâm khối.

### “Lực hướng tâm là một lực riêng”

Không. Đó là hợp lực theo phương bán kính.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md), [Vectơ và hệ quy chiếu](../00_foundations/02_space_time_vectors_frames.md).

**Liên hệ tiếp:** [Chuyển động quay](05_rotation_rigid_body.md), [Đàn hồi và cơ học vật liệu](07_statics_elasticity_materials.md), [Cơ học chất lưu](../03_continuum/00_fluids.md).
