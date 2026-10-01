# Ngôn ngữ Toán học tối thiểu để đọc Vật lý

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hàm số: một đại lượng phụ thuộc vào cái gì?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Đạo hàm: đo tốc độ biến thiên cục bộ** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Toán học trong Vật lý không chỉ là công cụ tính số. Nó là ngôn ngữ dùng để nói chính xác một đại lượng phụ thuộc vào đâu, thay đổi như thế nào, tích lũy ra sao và các bậc tự do tương tác với nhau theo cấu trúc nào.

## Hàm số: một đại lượng phụ thuộc vào cái gì?

Hàm số (function / 함수) là một quy tắc ánh xạ đầu vào thành đầu ra. Khi viết

```math
x(t),
```

ta nói vị trí `x` phụ thuộc vào thời gian `t`. Khi viết

```math
T(x,y,z,t),
```

nhiệt độ là một trường phụ thuộc cả vị trí lẫn thời gian.

Điểm quan trọng của ký hiệu hàm không nằm ở dấu ngoặc mà ở việc nó buộc ta khai báo sự phụ thuộc. Nếu `P=P(V,T)`, áp suất có thể thay đổi vì thể tích hoặc nhiệt độ. Do đó khi lấy đạo hàm phải nói rõ biến nào thay đổi và biến nào được giữ cố định.

> **Chuyển mạch:** Hàm số khai báo đại lượng phụ thuộc vào biến nào và biến nào được giữ cố định; **đạo hàm** đo tốc độ thay đổi cục bộ của quan hệ đó. Khi đạo hàm trở thành một phần của luật tiến hóa, **phương trình vi phân** sẽ mô tả quỹ đạo thay vì chỉ một thời điểm.

## Đạo hàm: đo tốc độ biến thiên cục bộ

Nếu một hàm chỉ phụ thuộc một biến,

```math
v=\frac{dx}{dt}
```

là đạo hàm thường (ordinary derivative). Nó cho biết `x` thay đổi nhanh thế nào theo `t` tại thời điểm đang xét.

Nếu trường phụ thuộc nhiều biến, chẳng hạn `T(x,y,z,t)`, đạo hàm riêng (partial derivative / 편미분)

```math
\frac{\partial T}{\partial x}
```

cho biết nhiệt độ thay đổi theo `x` khi `y`, `z` và `t` được giữ cố định. Đây là lý do cơ học chất lưu, điện từ học và truyền nhiệt thường dùng ký hiệu `\partial` thay cho `d`.

Đạo hàm còn mang ý nghĩa hình học. `dx/dt` là độ dốc của đồ thị `x(t)`, còn đạo hàm bậc hai mô tả cách độ dốc đó tiếp tục thay đổi.

> **Chuyển mạch:** Đạo hàm cho biết tốc độ và độ cong cục bộ, còn **phương trình vi phân** gắn chúng với lực, điều kiện ban đầu và diễn tiến theo thời gian. Với trường phụ thuộc nhiều tọa độ, **gradient** chuyển câu hỏi từ “đổi theo thời gian bao nhiêu” sang “tăng nhanh nhất theo hướng nào”.

## Phương trình vi phân: quy luật về sự tiến hóa

Phương trình vi phân (differential equation / 미분방정식) liên hệ một hàm chưa biết với các đạo hàm của nó. Phương trình Newton

```math
m\frac{d^2x}{dt^2}=F(x,v,t)
```

không trực tiếp cho ta `x(t)`. Nó đặt một quy luật lên độ cong của quỹ đạo theo thời gian. Muốn chọn được một quỹ đạo cụ thể còn cần điều kiện ban đầu (initial conditions), chẳng hạn `x(0)` và `v(0)`.

Điểm này rất quan trọng: **định luật tiến hóa không đồng nghĩa với trạng thái hiện tại**. Cùng một phương trình chuyển động có thể tạo vô số nghiệm khác nhau tùy trạng thái ban đầu.

> **Chuyển mạch:** Phương trình vi phân mô tả quy luật biến đổi; **gradient** chỉ hướng tăng nhanh nhất của một trường và nối thế năng với lực hoặc điện thế với điện trường. Khi trường là vectơ và cần hỏi dòng ròng đi ra hay đi vào một điểm, **divergence** là phép đo kế tiếp.

## Độ dốc (gradient / 기울기): hướng tăng nhanh nhất

Với trường vô hướng `f(x,y,z)`, độ dốc (gradient / 기울기) là

```math
\nabla f=
\left(
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y},
\frac{\partial f}{\partial z}
\right).
```

Độ dốc (gradient / 기울기) là một vectơ chỉ hướng mà `f` tăng nhanh nhất tại điểm đang xét; độ lớn của nó cho biết mức độ dốc cục bộ.

Trong hệ bảo toàn,

```math
\vec F=-\nabla U,
```

nên lực hướng về phía thế năng giảm nhanh nhất. Tương tự, quan hệ

```math
\vec E=-\nabla V
```

nối điện trường với độ biến thiên không gian của điện thế.

Độ dốc (gradient / 기울기) không chỉ xuất hiện trong Vật lý. Trong tối ưu hóa, hạ độ dốc (gradient / 기울기) (gradient descent) di chuyển trong không gian tham số theo hướng giảm nhanh hàm mất mát. Đây là cùng cấu trúc toán học nhưng có cách diễn giải khác.

> **Chuyển mạch:** Gradient mô tả hướng tăng của trường vô hướng; **divergence** lấy trường vectơ và đo dòng ròng như một nguồn hoặc hố cục bộ. Nếu divergence trả lời “bao nhiêu đi ra”, **curl** tiếp theo trả lời “trường có xu hướng quay quanh điểm hay không”.

## Divergence: nguồn và dòng ra cục bộ

Với trường vectơ `\vec A`, divergence (divergence / 발산)

```math
\nabla\cdot\vec A
```

đo mức dòng ròng đi ra khỏi một vùng vô cùng nhỏ quanh điểm đang xét. Giá trị dương gợi ý hành vi giống nguồn; giá trị âm gợi ý hành vi giống hố hút.

Dạng vi phân của định luật Gauss là

```math
\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0},
```

cho thấy mật độ điện tích đóng vai trò nguồn của điện trường.

Với dòng chất lưu không nén được,

```math
\nabla\cdot\vec v=0,
```

nghĩa là tại mỗi vùng nhỏ không có sự tích tụ hoặc thất thoát thể tích do mất cân bằng dòng vào–ra.

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Divergence: nguồn và dòng ra cục bộ** nêu điều cần giải thích; **Curl: xu hướng quay cục bộ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Từ cục bộ đến toàn cục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Curl: xu hướng quay cục bộ

Curl (curl / 회전) của trường vectơ

```math
\nabla\times\vec A
```

đo xu hướng tuần hoàn cục bộ của trường.

Định luật Faraday ở dạng vi phân

```math
\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}
```

cho biết từ trường biến thiên theo thời gian tạo ra một điện trường có cấu trúc tuần hoàn.

Độ dốc (gradient / 기울기), divergence và curl không phải ba phép toán rời rạc được đặt tên tùy ý. Chúng mô tả ba loại cấu trúc cục bộ khác nhau: độ dốc của trường vô hướng, nguồn của trường vectơ và xu hướng quay của trường vectơ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Từ cục bộ đến toàn cục** tiếp nhận điểm tựa từ **Curl: xu hướng quay cục bộ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tích phân: cộng dồn các phần tử vô cùng nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ cục bộ đến toàn cục

Một mẫu hình sâu của giải tích là thông tin đạo hàm cục bộ có thể được tích phân để cho quan hệ toàn cục trên biên.

Trong một chiều,

```math
\int_a^b\frac{df}{dx}\,dx=f(b)-f(a).
```

Định lý divergence cho

```math
\int_V(\nabla\cdot\vec A)dV
=\oint_{\partial V}\vec A\cdot d\vec S,
```

còn định lý Stokes cho

```math
\int_S(\nabla\times\vec A)\cdot d\vec S
=\oint_{\partial S}\vec A\cdot d\vec l.
```

Nhờ các định lý này, phương trình Maxwell có thể được viết ở dạng vi phân hoặc dạng tích phân. Một dạng nói điều gì xảy ra tại từng điểm, dạng kia nói tổng thông lượng hoặc tuần hoàn trên một vùng hữu hạn.

> **Chuyển mạch:** Trong **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Tích phân: cộng dồn các phần tử vô cùng nhỏ** tiếp nhận điểm tựa từ **Từ cục bộ đến toàn cục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Số phức và pha** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tích phân: cộng dồn các phần tử vô cùng nhỏ

Tích phân có thể được hiểu là giới hạn của phép cộng rất nhiều phần tử nhỏ. Nếu biết vận tốc theo thời gian,

```math
\Delta x=\int_{t_1}^{t_2}v(t)\,dt
```

cho độ dời. Nếu biết mật độ khối lượng,

```math
M=\int_V\rho\,dV
```

cho tổng khối lượng trong thể tích.

Ý nghĩa vật lý của tích phân phụ thuộc vào thứ đang được cộng và miền tích phân. Vì vậy luôn cần hỏi: phần tử vi phân `dt`, `dx`, `dA` hay `dV` đại diện cho cái gì?

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Số phức và pha** tiếp nhận điểm tựa từ **Tích phân: cộng dồn các phần tử vô cùng nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ma trận và phép biến đổi tuyến tính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Số phức và pha

Số phức (complex number / 복소수) có dạng

```math
z=a+ib,
```

với `i^2=-1`. Công thức Euler

```math
e^{i\theta}=\cos\theta+i\sin\theta
```

biến bài toán dao động và quay thành đại số hàm mũ rất gọn. Một dao động hình sin có thể viết

```math
A\cos(\omega t+\phi)=\Re\left(Ae^{i(\omega t+\phi)}\right).
```

Trong mạch xoay chiều, sóng, quang học và cơ học lượng tử, biểu diễn phức giúp giữ cả biên độ lẫn pha. Đại lượng quan sát cuối cùng thường là số thực hoặc được lấy từ môđun bình phương, nhưng phần phức ở bước trung gian chứa thông tin pha cần thiết để mô tả giao thoa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Ma trận và phép biến đổi tuyến tính** tiếp nhận điểm tựa từ **Số phức và pha** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vectơ riêng và trị riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận và phép biến đổi tuyến tính

Ma trận (matrix / 행렬) nên được hiểu như biểu diễn của một phép biến đổi tuyến tính sau khi đã chọn cơ sở. Phương trình

```math
\vec y=A\vec x
```

không chỉ là phép nhân một bảng số; `A` mô tả cách vectơ đầu vào được biến đổi thành vectơ đầu ra.

Phép quay, tensor ứng suất, hệ dao động ghép, phân cực ánh sáng, toán tử lượng tử và đồ họa máy tính đều dùng cấu trúc ma trận.

> **Chuyển mạch:** Trong **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Vectơ riêng và trị riêng** tiếp nhận điểm tựa từ **Ma trận và phép biến đổi tuyến tính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khai triển Taylor và tuyến tính hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vectơ riêng và trị riêng

Nếu

```math
A\vec v=\lambda\vec v,
```

thì `\vec v` là vectơ riêng (eigenvector), còn `\lambda` là trị riêng (eigenvalue). Dưới phép biến đổi `A`, hướng của `\vec v` được giữ nguyên và chỉ độ lớn thay đổi theo hệ số `\lambda`.

Trong dao động cơ học, các vectơ riêng thường biểu diễn chế độ (mode / 모드) chuẩn (normal modes), còn trị riêng liên hệ với tần số riêng. Trong cơ học lượng tử, trạng thái riêng (eigenstate) của một toán tử quan sát tương ứng với một giá trị xác định có thể thu được khi đo đại lượng đó.

Cùng một đại số tuyến tính được tái sử dụng, nhưng ý nghĩa vật lý của vectơ và trị riêng phụ thuộc vào bài toán.

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Khai triển Taylor và tuyến tính hóa** tiếp nhận điểm tựa từ **Vectơ riêng và trị riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô tả liên tục và mô tả rời rạc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khai triển Taylor và tuyến tính hóa

Với một hàm đủ trơn quanh `x_0`,

```math
f(x_0+\delta)=f(x_0)+f'(x_0)\delta+
\frac12f''(x_0)\delta^2+\cdots.
```

Nếu `\delta` đủ nhỏ, các hạng bậc cao giảm nhanh và ta có thể giữ một vài hạng đầu. Đây là cơ sở của tuyến tính hóa (linearization).

Ví dụ,

```math
\sin\theta=\theta-\frac{\theta^3}{6}+\cdots,
```

nên khi `|\theta|\ll1` rad,

```math
\sin\theta\approx\theta.
```

Ta không nên chỉ nói “góc có vẻ nhỏ”. Hạng bị bỏ đầu tiên `\theta^3/6` cho phép ước lượng định lượng sai số của xấp xỉ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Mô tả liên tục và mô tả rời rạc** tiếp nhận điểm tựa từ **Khai triển Taylor và tuyến tính hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô tả liên tục và mô tả rời rạc

Nhiều mô hình vật lý dùng biến liên tục, nhưng máy tính phải biểu diễn chúng bằng số lượng hữu hạn điểm. Ví dụ,

```math
\frac{dx}{dt}\approx\frac{x_{n+1}-x_n}{\Delta t}.
```

Khi `\Delta t` hữu hạn, sai số rời rạc hóa (discretization error) xuất hiện. Lưới quá thô có thể bỏ mất cấu trúc tần số cao, làm thuật toán mất ổn định hoặc tạo hiện tượng giả số.

Do đó trong vật lý tính toán luôn có hai câu hỏi riêng: mô hình vật lý có phù hợp với hệ thật không, và phương pháp số có giải mô hình đó đủ chính xác không. Máy tính có thể giải rất chính xác một mô hình sai, hoặc giải sai một mô hình đúng.

> **Chuyển mạch:** Trong **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Mô tả liên tục và mô tả rời rạc** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Đạo hàm mô tả biến thiên cục bộ; tích phân cộng dồn các đóng góp cục bộ; phương trình vi phân mã hóa quy luật tiến hóa; độ dốc (gradient / 기울기), divergence và curl mô tả cấu trúc không gian của trường; đại số tuyến tính tổ chức nhiều bậc tự do; khai triển Taylor cho phép xây dựng các mô hình gần đúng có kiểm soát.

Khi gặp một biểu thức toán học trong Vật lý, đừng chỉ hỏi “tính thế nào?”. Hãy hỏi thêm: biến này đại diện cho đại lượng gì, nó sống trong không gian nào, đạo hàm đang giữ biến nào cố định, tích phân đang cộng trên miền nào và phép xấp xỉ đang bỏ qua bậc nào.

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

Biết thao tác ký hiệu không đồng nghĩa với hiểu mô hình. Một đạo hàm không có ý nghĩa nếu không biết biến độc lập; một tích phân không đầy đủ nếu không biết miền; một vectơ không đầy đủ nếu không biết hệ tọa độ hoặc không gian của nó; một phương trình vi phân không chọn được nghiệm vật lý duy nhất nếu thiếu điều kiện đầu hoặc điều kiện biên.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ Toán học tối thiểu để đọc Vật lý**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Tư duy Vật lý](00_physical_thinking.md).

**Liên hệ tiếp:** [Đối xứng, bảo toàn và thang đo](04_symmetry_conservation_scale.md), [Các cấu trúc lặp lại trong Vật lý](../13_connections/00_knowledge_connections.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
