# Hàm số: từ quan hệ đến quy tắc biến đổi

Hàm số (Function / 함수) là một trong những ý tưởng trung tâm của toán học vì nó cho phép ta mô tả **một quy tắc ổn định nối input với output**. Khi nói “nhiệt độ phụ thuộc vào thời gian”, “giá tiền phụ thuộc vào số lượng”, “tọa độ mới phụ thuộc vào tọa độ cũ sau một phép quay”, hoặc “model nhận feature vector và trả về prediction”, ta đang nhìn thế giới dưới dạng một mapping.

Điểm quan trọng là function không bắt đầu từ công thức. Nó bắt đầu từ câu hỏi: **nếu biết trạng thái đầu vào, ta có xác định được trạng thái đầu ra hay không?** Công thức, bảng dữ liệu, graph, lookup table, chương trình máy tính hay neural network chỉ là các cách biểu diễn khác nhau của cùng ý tưởng mapping đó.

> Hàm số là một contract: input thuộc không gian nào, output thuộc không gian nào, và mỗi input hợp lệ được map tới output nào.

## Từ relation đến function

Một quan hệ (Relation / 관계) chỉ nói rằng một số objects có liên hệ với nhau. Nếu `A` là tập người và `B` là tập thành phố, quan hệ “đã từng sống ở” có thể nối một người với nhiều thành phố. Nó chưa phải function từ người sang thành phố vì cùng một input có thể có nhiều outputs.

Một function `f:A→B` thêm constraint mạnh hơn: **mỗi phần tử của `A` phải được gán đúng một phần tử trong `B`**.

```math
f:A\to B
```

`A` là miền xác định (Domain / 정의역). `B` là đối miền (Codomain / 공역). Với mỗi `x∈A`, notation

```math
y=f(x)
```

nói rằng `f` map input `x` thành output `y`.

Điều kiện “đúng một output” không cấm nhiều inputs cùng đi tới một output. Ví dụ

```math
f(x)=x^2
```

cho `f(2)=4` và `f(-2)=4`; điều này hoàn toàn hợp lệ. Function chỉ cấm một input duy nhất đồng thời được gán hai outputs khác nhau trong cùng definition.

### Domain không phải ghi chú phụ

Xét biểu thức

```math
f(x)=\frac{1}{x}.
```

Nếu chỉ nhìn formula, ta có thể tưởng domain là mọi số thực. Nhưng tại `x=0`, division không được định nghĩa. Vì vậy một definition chính xác phải nói

```math
f:\mathbb R\setminus\{0\}\to\mathbb R.
```

Domain là một phần của function, không phải metadata trang trí. Cùng formula nhưng khác domain có thể tạo ra những function có properties khác nhau.

Ví dụ `f(x)=x^2` trên toàn `R` không injective. Nếu restrict domain thành `[0,∞)`, nó trở thành injective và có inverse `√x` trên range tương ứng. Việc “chọn domain” vì thế có thể thay đổi cả structure của problem.

## Codomain và range: vì sao phải phân biệt?

Range hay image (Image / 치역) là tập outputs thực sự đạt được. Codomain là tập mà ta tuyên bố output thuộc vào.

Với

```math
f:\mathbb R\to\mathbb R,\qquad f(x)=x^2,
```

codomain là `R`, nhưng range là `[0,∞)`.

Nếu thay definition bằng

```math
f:\mathbb R\to[0,\infty),\qquad f(x)=x^2,
```

formula không đổi nhưng property “surjective hay không” đã đổi. Trong definition thứ nhất, function không surjective lên `R` vì không có input nào cho output âm. Trong definition thứ hai, nó surjective lên `[0,∞)`.

Đây là lý do toán học hiện đại coi function là **mapping kèm domain và codomain**, không chỉ là expression.

## Function không nhất thiết là công thức đóng

Khi học phổ thông, function thường xuất hiện dưới dạng `y=2x+3`, `y=x²` hay `y=sin x`, nên dễ hình thành misconception rằng function phải có closed-form formula.

Thực tế, một function có thể được định nghĩa bằng table:

| user_id | risk_score |
|---|---:|
| A | 0.13 |
| B | 0.82 |

Nó cũng có thể được định nghĩa bằng algorithm, simulation hoặc program. Một sorting function nhận một list và trả list đã sắp xếp; một compiler pass nhận AST và trả AST mới; một neural network nhận vector input và trả logits. Nếu mapping deterministic và contract được xác định rõ, tất cả đều có thể được nhìn như functions.

Điều này rất quan trọng vì nó tách **mathematical object** khỏi **representation**. Function là mapping; formula chỉ là một cách biểu diễn mapping.

## Graph của function là tập các input-output pairs

Với function một biến thực `f:R→R`, graph là tập

```math
\{(x,f(x))\mid x\in\operatorname{domain}(f)\}.
```

Graph không phải là function; nó là một representation hình học của function.

Vertical line test xuất phát trực tiếp từ definition. Nếu một vertical line `x=c` cắt curve ở hai points khác nhau, cùng input `c` đang tương ứng hai values của `y`. Relation đó không thể là graph của một single-valued function `y=f(x)`.

Nhưng relation đó vẫn có thể rất hữu ích. Circle

```math
x^2+y^2=1
```

không phải global function `y=f(x)` vì với nhiều `x` có hai values `y=±√(1-x²)`. Ta có thể chia nó thành hai functions, hoặc dùng parametric representation. Đây là ví dụ cho thấy “không phải function theo representation hiện tại” không có nghĩa object vô dụng; có thể representation chưa phù hợp.

## Injective, surjective và bijective

Ba properties này mô tả cách mapping sử dụng input và codomain.

Một function là đơn ánh (Injective / 일대일 함수) nếu

```math
f(x_1)=f(x_2)\Rightarrow x_1=x_2.
```

Nói trực giác: hai inputs khác nhau không bị collapse thành cùng output. Information về input không bị mất theo kiểu đó.

Một function là toàn ánh (Surjective / 전사 함수) nếu mọi element trong codomain đều được hit bởi ít nhất một input.

Một function là song ánh (Bijective / 전단사 함수) nếu vừa injective vừa surjective. Khi đó mỗi output trong codomain tương ứng đúng một input và mapping có thể đảo ngược hoàn toàn.

### Invertibility là câu hỏi về information preservation

Nếu `f` bijective, tồn tại inverse function

```math
f^{-1}:B\to A
```

sao cho

```math
f^{-1}(f(x))=x
```

và

```math
f(f^{-1}(y))=y.
```

Đây không chỉ là một trick đại số. Inverse tồn tại khi output giữ đủ information để recover input duy nhất.

Xét

```math
f(x)=x^2.
```

Nếu domain là toàn `R`, output `4` không cho biết input là `2` hay `-2`; information về sign đã mất. Vì vậy inverse global không tồn tại. Restrict domain sang `x≥0` loại ambiguity đó và inverse trở thành `√x`.

Trong computing, hashing thường cố ý không invertible: nhiều possible inputs map vào không gian output nhỏ hơn. Compression lossless phải preserve đủ information để decode; lossy compression chấp nhận mất một phần information để giảm representation size.

## Composition: xây hệ phức tạp từ transformations đơn giản

Giả sử

```math
g:A\to B
```

và

```math
f:B\to C.
```

Nếu output của `g` là input hợp lệ của `f`, ta có composition

```math
(f\circ g)(x)=f(g(x)).
```

Composition (Composition / 합성함수) là cách toán học mô tả pipeline. Một complex transformation có thể được hiểu như chuỗi các transformations nhỏ.

Ví dụ, giả sử temperature Celsius được chuyển sang Fahrenheit rồi thành label:

```text
Celsius → Fahrenheit → category
```

Nếu `g` convert Celsius thành Fahrenheit và `f` convert Fahrenheit thành category, whole process là `f∘g`.

Trong software, parse → validate → normalize → persist là pipeline của functions. Trong neural network,

```math
f(x)=f_L(f_{L-1}(\cdots f_2(f_1(x))\cdots))
```

là composition của layers. Chain rule trong calculus tồn tại chính vì ta cần biết sensitivity của một composition.

### Composition thường không giao hoán

Thông thường

```math
f\circ g\ne g\circ f.
```

Rotate rồi translate một object thường khác translate rồi rotate. Normalize data rồi apply threshold có thể khác threshold rồi normalize. Order là một phần của process.

## Function như transformation của structure

Một cách nhìn mạnh hơn “machine input-output” là coi function như một transformation giữa spaces.

```math
f:A\to B
```

nói rằng ta đang chuyển description từ space `A` sang space `B`. Với linear algebra, matrix đại diện linear function giữa vector spaces. Với probability, random variable là function từ sample space sang numbers. Với optimization, objective function map decision vector thành scalar cost. Với database query, query map database state thành result relation.

Cùng một concept function vì thế nối nhiều mảng toán khác nhau.

## Parameters và family of functions

Xét

```math
f(x)=ax+b.
```

`x` là variable input. `a` và `b` là parameters (Parameters / 매개변수) chọn một function cụ thể trong family affine functions.

Nếu `a=2,b=3`, ta có một member cụ thể `f(x)=2x+3`. Nếu đổi parameters, mapping thay đổi.

Machine learning có thể được nhìn như bài toán: chọn parameters `θ` để function

```math
f_\theta(x)
```

phù hợp data và objective. Training không “tạo phép thuật”; nó search trong một family functions được architecture cho phép.

## Piecewise functions và business rules

Không phải system nào cũng dùng cùng rule trên toàn domain. Piecewise function cho phép rule phụ thuộc region.

```math
f(x)=
\begin{cases}
-x,&x<0,\\
x,&x\ge0.
\end{cases}
```

định nghĩa absolute value `|x|`.

Tax brackets, shipping fees, tiered pricing, ReLU activation, rate limits và SLA penalties đều thường có piecewise structure.

Điểm cần chú ý là piecewise function vẫn chỉ là **một function**, nếu tại mỗi input đúng một branch xác định output. Boundary conditions cần được viết cẩn thận để tránh gap hoặc overlap gây ambiguity.

## Monotonicity và inverse

Nếu function strictly increasing trên một interval,

```math
x_1<x_2\Rightarrow f(x_1)<f(x_2),
```

thì nó injective trên interval đó. Tương tự với strictly decreasing.

Monotonicity (Monotonicity / 단조성) vì thế là một cách geometric để thấy invertibility cục bộ hoặc trên restricted domain. Đây là lý do logarithm có thể là inverse của exponential: exponential strictly increasing trên `R` khi base `>1`.

## Transformations của graph và tác động lên input/output

Nếu `y=f(x)`, một số transformations cơ bản là:

```math
g(x)=f(x)+c
```

shift output lên `c`.

```math
g(x)=f(x-c)
```

shift graph sang phải `c`, vì muốn `g(x)` dùng cùng old input `u`, ta cần `x-c=u`, tức `x=u+c`.

```math
g(x)=af(x)
```

scale output theo `a`.

```math
g(x)=f(ax)
```

scale input axis theo factor nghịch đảo. Đây là chỗ dễ nhầm vì transformation xảy ra **bên trong input**.

Cách nhớ tốt hơn không phải thuộc rule “inside ngược, outside thuận”, mà hỏi: “để function cũ nhận cùng input như trước, input mới phải thay đổi thế nào?”

## Function equality

Hai functions bằng nhau khi chúng có cùng domain phù hợp và cho cùng output với mọi input trong domain đó. Hai formulas trông khác nhau vẫn có thể represent cùng function trên một domain.

Ví dụ

```math
\frac{x^2-1}{x-1}=x+1
```

đúng khi `x≠1`. Nhưng nếu function bên trái có domain `R\{1}` còn `x+1` được định nghĩa trên toàn `R`, thì chúng không hoàn toàn là cùng function nếu domain được coi là một phần của object.

Đây là distinction quan trọng khi simplification tạo ra removable discontinuity.

## Knowledge Connection — function, type và API contract

Trong programming, một function signature như

```text
User → RiskScore
```

rất giống notation

```math
f:A\to B.
```

Type system nói input/output spaces hợp lệ; implementation nói mapping cụ thể. Nếu function partial vì một số inputs gây error, ta có thể model output space rộng hơn, chẳng hạn

```text
UserInput → Result<User, ValidationError>
```

thay vì giả vờ mọi input đều hợp lệ.

Cách nhìn này giúp thấy domain/codomain không phải khái niệm hàn lâm xa code; chúng là mathematical version của contract design.

## Knowledge Connection — function trong probability

Một biến ngẫu nhiên (Random Variable / 확률변수) thực chất là function

```math
X:\Omega\to\mathbb R,
```

map mỗi elementary outcome trong sample space `Ω` thành một number. “Random” nằm ở outcome được chọn theo probability model; mapping `X` itself là deterministic.

Đây là một connection quan trọng: khi hiểu function tốt, probability bớt giống một collection công thức riêng biệt.

## Khi function model không đủ

Function giả định cùng input trong model xác định một output. Nhưng nhiều systems thực tế có noise, hidden state hoặc randomness. Khi cùng observable input có thể dẫn tới nhiều outcomes, ta có thể cần probability distribution

```math
P(Y\mid X=x)
```

thay vì deterministic `y=f(x)`.

Trong dynamic systems, output còn phụ thuộc internal state chứ không chỉ current external input. Khi đó model state-space phù hợp hơn một stateless function đơn giản.

Điều này không làm function mất giá trị; nó chỉ nhắc rằng model phải chứa đủ variables để deterministic mapping trở nên hợp lý, hoặc phải chuyển sang probabilistic model.

## Mental Model

> Function là một transformation có contract. Domain nói những trạng thái đầu vào nào hợp lệ; rule nói chúng được biến đổi ra sao; codomain nói ta đang mô tả output trong space nào. Composition xây hệ lớn từ transformations nhỏ, còn invertibility hỏi transformation có giữ đủ information để quay ngược lại hay không.

## Common Misconceptions

**“Function nghĩa là mỗi output chỉ có một input.”** Sai chiều. Requirement là mỗi input có đúng một output. Nhiều inputs có thể cùng map tới một output; chỉ khi function injective thì output mới xác định input duy nhất.

**“Function phải có công thức.”** Formula chỉ là representation. Table, program, lookup mapping, simulation hay learned model đều có thể represent a function.

**“`f^{-1}` là `1/f`.”** Inverse function undo mapping; reciprocal chỉ lấy nghịch đảo value. Hai operations khác nhau hoàn toàn.

**“Domain chỉ cần nhìn từ formula.”** Context cũng quyết định domain. `√x` về algebra có domain `x≥0` trên real numbers, nhưng một physical model có thể còn restriction chặt hơn, chẳng hạn length phải nằm trong một khoảng đo thực tế.

**“Hai expressions bằng nhau thì hai functions luôn giống nhau.”** Domain/codomain là một phần của function. Simplification có thể che mất excluded points hoặc thay đổi structural properties.