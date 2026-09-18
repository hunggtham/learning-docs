# Ngôn ngữ đại số: biến, biểu thức và phép biến đổi

Đại số (Algebra / 대수학) ra đời khi ta không muốn giải từng bài toán bằng con số cụ thể mà muốn mô tả một pattern chung. Thay vì nói “3 hộp, mỗi hộp 5 món”, ta viết `3x` để giữ `x` như một quantity chưa biết hoặc có thể thay đổi. Từ đó, ta có thể suy luận trên cấu trúc mà không cần chốt giá trị ngay.

## Variable không chỉ là “ẩn số”

Biến (Variable / 변수) có nhiều vai trò. Trong equation `x+3=10`, `x` là unknown cần tìm. Trong function `y=2x+1`, `x` là input có thể nhận nhiều giá trị. Trong statistics, `X` có thể là random variable. Trong programming, variable là vùng tham chiếu đến value thay đổi theo execution. Các nghĩa liên quan nhưng không hoàn toàn đồng nhất.

Một variable về bản chất là một placeholder có domain. Nếu `x` đại diện số người, domain hợp lý thường là non-negative integers; nếu `x` là thời gian liên tục, real numbers có thể hợp lý hơn. Domain không phải chi tiết phụ: nó quyết định nghiệm nào có nghĩa.

## Expression và evaluation

Biểu thức (Expression / 식) là tổ hợp của constants, variables và operations tạo ra một value khi inputs được gán. `3x+2` là expression; nó chưa khẳng định điều gì đúng hay sai.

Nếu `x=4`, evaluation cho

```math
3(4)+2=14
```

Expression khác equation. Equation `3x+2=14` là một proposition phụ thuộc `x`; ta tìm values làm equality đúng.

## Equality là quan hệ cân bằng

Dấu bằng `=` không có nghĩa “hãy tính ra”. Nó khẳng định hai expression biểu diễn cùng value. Vì vậy khi biến đổi equation, mục tiêu là bảo toàn tập nghiệm.

Từ

```math
x+5=12
```

trừ 5 ở cả hai vế:

```math
x+5-5=12-5
```

cho

```math
x=7
```

Ta được phép làm vậy vì nếu `a=b`, áp dụng cùng một function vào hai vế vẫn cho equality, ở đây là function `f(t)=t-5`.

Mental model “cân hai vế” hữu ích, nhưng sâu hơn là ta đang áp dụng transformation bảo toàn equivalence.

## Distributive law

Tính phân phối (Distributive law / 분배법칙)

```math
a(b+c)=ab+ac
```

không phải mẹo mở ngoặc. Nó nói scaling một tổng bằng `a` tương đương scaling từng thành phần rồi cộng.

Hình học cho trực giác: rectangle chiều cao `a`, chiều rộng `b+c` có area `a(b+c)`. Chia rectangle thành hai phần width `b` và `c`, total area là `ab+ac`. Hai expression mô tả cùng object theo hai decomposition.

Factorization là chiều ngược lại:

```math
ab+ac=a(b+c)
```

Trong computing, đây giống refactoring một common factor ra ngoài để lộ structure chung.

## Exponents như repeated multiplication

Lũy thừa (Exponentiation / 거듭제곱) với integer exponent positive:

```math
a^n=\underbrace{a\cdot a\cdots a}_{n\text{ lần}}
```

Từ definition này suy ra

```math
a^m a^n=a^{m+n}
```

vì tổng số factors là `m+n`.

Muốn luật vẫn nhất quán khi exponent bằng 0, từ

```math
\frac{a^m}{a^m}=a^{m-m}=a^0
```

mà vế trái bằng 1 với `a≠0`, nên

```math
a^0=1
```

Negative exponent cũng đến từ consistency:

```math
a^{-n}=\frac{1}{a^n}
```

Không nên học các rule này như bảng ký hiệu rời rạc; chúng là extension để laws của exponents tiếp tục đúng.

## Roots và fractional exponents

Căn bậc `n` hỏi số nào khi lũy thừa `n` cho value đã biết:

```math
x^n=a\quad\Longrightarrow\quad x=\sqrt[n]{a}
```

Fractional exponent được định nghĩa để

```math
(a^{1/n})^n=a
```

nên

```math
a^{1/n}=\sqrt[n]{a}
```

và

```math
a^{m/n}=\sqrt[n]{a^m}
```

trong domain thích hợp.

## Algebraic identities là structure, không phải formula list

Ví dụ

```math
(a+b)^2=a^2+2ab+b^2
```

đến trực tiếp từ distributive law:

```math
(a+b)(a+b)=a^2+ab+ba+b^2
```

và commutativity `ab=ba` cho middle term `2ab`.

Khi hiểu source, ta không cần nhớ một danh sách dài identities độc lập.

## Symbolic manipulation và điều kiện hợp lệ

Một transformation algebraic có thể mất hoặc sinh nghiệm nếu không để ý domain. Ví dụ từ

```math
x^2=x
```

chia hai vế cho `x` cho `x=1`, nhưng thao tác này loại mất nghiệm `x=0` vì division by zero không hợp lệ. Cách an toàn hơn:

```math
x^2-x=0
```

```math
x(x-1)=0
```

nên

```math
x=0\quad\text{hoặc}\quad x=1
```

Mọi phép biến đổi cần hỏi: operation có reversible trên toàn domain đang xét không?

## Algebra trong programming và modeling

Khi rearrange formula để solve một parameter, ta đang làm symbolic algebra. Ví dụ latency total:

```math
T=T_{network}+T_{server}+T_{db}
```

nếu biết budget `T` và hai component, allowable DB latency là

```math
T_{db}=T-T_{network}-T_{server}
```

Trong performance engineering, finance và unit conversion, cùng tư duy isolation xuất hiện liên tục.

## Mental Model

> Algebra là nghệ thuật thay representation mà không thay meaning. Ta dùng symbols để giữ cấu trúc chung, rồi áp dụng transformations bảo toàn quan hệ cho đến khi structure cần tìm trở nên lộ rõ.

## Common Misconceptions

`=` không phải nút “ra kết quả”. Variable không luôn là unknown. “Chuyển vế đổi dấu” chỉ là shortcut ngôn ngữ cho việc cộng/trừ cùng lượng ở hai vế. Chia, bình phương hoặc lấy căn hai vế có thể thay đổi solution set nếu không kiểm tra điều kiện.
