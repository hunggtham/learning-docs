# Hợp hàm, hàm ngược và phép biến đổi hàm

> **Mạch đọc:** Đọc **Hợp hàm, hàm ngược và phép biến đổi hàm** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Composition là phép nối các transformations** sang **Composition thường không giao hoán**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một hàm số (Function / 함수) mô tả một ánh xạ (mapping / 매핑) từ đầu vào (input / 입력) sang đầu ra (output / 출력). Khi các hệ thống thực tế gồm nhiều bước, ta hiếm khi chỉ có một ánh xạ (mapping / 매핑) đơn lẻ. Ta có chuỗi xử lý (pipeline / 파이프라인): đầu vào (input / 입력) đi qua bước A, đầu ra (output / 출력) của A trở thành đầu vào (input / 입력) của B. Toán học của chuỗi xử lý (pipeline / 파이프라인) đó là hợp hàm (Function Composition / 함수의 합성).

## Composition là phép nối các transformations

Nếu

```math
g:X\to Y
```

và

```math
f:Y\to Z,
```

thì hợp hàm

```math
f\circ g:X\to Z
```

được định nghĩa bởi

```math
(f\circ g)(x)=f(g(x)).
```

Ví dụ

```math
g(x)=2x+1,
```

```math
f(u)=u^2.
```

Khi đó

```math
(f\circ g)(x)=(2x+1)^2.
```

Ta không nên coi `f(g(x))` là cú pháp (syntax / 문법) trang trí. Nó diễn tả thứ tự xử lý. `g` chạy trước, `f` chạy sau.

Trong software, đây là hàm (function / 함수) composition hoặc chuỗi xử lý (pipeline / 파이프라인). Trong neural mạng (network / 네트워크), mỗi tầng (layer / 계층) là một transformation và toàn mạng (network / 네트워크) là composition của nhiều layers. Trong calculus, chuỗi (chain / 사슬) quy tắc (rule / 규칙) tồn tại chính vì thay đổi (change / 변경) phải đi xuyên qua một composition.


> **Chuyển mạch:** Từ **Composition là phép nối các transformations**, ta sang **Composition thường không giao hoán** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Composition thường không giao hoán

Thông thường

```math
f\circ g\neq g\circ f.
```

Với `f(x)=x^2` và `g(x)=x+1`:

```math
(f\circ g)(x)=(x+1)^2,
```

trong khi

```math
(g\circ f)(x)=x^2+1.
```

Kết quả khác nhau vì thứ tự transformation khác nhau. Cùng ý tưởng xuất hiện trong phép nhân ma trận (matrix multiplication / 행렬 곱셈), rotations 3D, cơ sở dữ liệu (database / 데이터베이스) transformations và stateful workflows.


> **Chuyển mạch:** Từ **Composition thường không giao hoán**, ta sang **Hàm ngược là undo một ánh xạ (mapping / 매핑)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hàm ngược là undo một ánh xạ (mapping / 매핑)

Hàm ngược (Inverse Function / 역함수) của `f` là hàm (function / 함수) `f^{-1}` sao cho

```math
f^{-1}(f(x))=x
```

và, trên miền thích hợp,

```math
f(f^{-1}(y))=y.
```

Ví dụ

```math
f(x)=3x+5.
```

Đặt

```math
y=3x+5.
```

Giải `x` theo `y`:

```math
x=\frac{y-5}{3}.
```

Do đó

```math
f^{-1}(x)=\frac{x-5}{3}.
```

Hàm ngược không phải reciprocal. `f^{-1}(x)` không có nghĩa `1/f(x)`.


> **Chuyển mạch:** Từ **Hàm ngược là undo một ánh xạ (mapping / 매핑)**, ta sang **Vì sao cần one-to-one?** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Vì sao cần one-to-one?

Xét

```math
f(x)=x^2
```

trên toàn bộ real numbers. Cả `2` và `-2` đều map tới `4`. Nếu chỉ biết đầu ra (output / 출력) là `4`, ta không thể biết đầu vào (input / 입력) ban đầu là `2` hay `-2`. ánh xạ (mapping / 매핑) đã làm mất thông tin.

Để có inverse là một hàm (function / 함수), `f` phải injective, tức one-to-one trên lĩnh vực (domain / 도메인) đang xét. Ta có thể restrict lĩnh vực (domain / 도메인) của `x^2` thành `[0,\infty)`; khi đó inverse là

```math
f^{-1}(x)=\sqrt{x}.
```

Điều này liên hệ trực tiếp với dữ liệu (data / 데이터) processing: thao tác (operation / 연산) mất thông tin thường không thể đảo ngược duy nhất. Hashing, rounding và compression mất dữ liệu là các ví dụ thực tế.


> **Chuyển mạch:** Từ **Vì sao cần one-to-one?**, ta sang **đồ thị (graph / 그래프) của inverse** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đồ thị (graph / 그래프) của inverse

Nếu `(a,b)` nằm trên đồ thị (graph / 그래프) của `y=f(x)`, thì `(b,a)` nằm trên đồ thị (graph / 그래프) của `y=f^{-1}(x)`. Vì vậy hai graphs đối xứng qua đường

```math
y=x.
```

Đây là hệ quả trực tiếp của việc hoán đổi role đầu vào (input / 입력) và đầu ra (output / 출력).


> **Chuyển mạch:** Từ **đồ thị (graph / 그래프) của inverse**, ta sang **Biến đổi đồ thị (graph / 그래프) từ một hàm (function / 함수) gốc** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Biến đổi đồ thị (graph / 그래프) từ một hàm (function / 함수) gốc

Nếu biết đồ thị (graph / 그래프) của `y=f(x)`, ta có thể hiểu nhiều đồ thị (graph / 그래프) mới mà không cần vẽ lại từ đầu.

Với

```math
y=f(x)+k,
```

toàn đồ thị (graph / 그래프) dịch lên `k` units. Với

```math
y=f(x-h),
```

Đồ thị (graph / 그래프) dịch sang phải `h` units.

Điểm dễ nhầm là horizontal shift có dấu “ngược trực giác”. Muốn điểm cũ tại đầu vào (input / 입력) `a` xuất hiện tại đầu vào (input / 입력) mới `a+h`, ta cần argument bên trong thỏa

```math
x-h=a,
```

nên `x=a+h`.

Scaling cũng có hai loại. Với

```math
y=af(x),
```

Đầu ra (output / 출력) được quy mô (scale / 규모) theo vertical direction. Với

```math
y=f(bx),
```

Đầu vào (input / 입력) cần nhỏ đi `1/b` để argument bên trong đạt cùng giá trị (value / 값), nên đồ thị (graph / 그래프) bị horizontal compression khi `|b|>1`.

Nếu `a<0` hoặc `b<0`, ta có reflection qua trục `x` hoặc trục `y`.


> **Chuyển mạch:** Từ **Biến đổi đồ thị (graph / 그래프) từ một hàm (function / 함수) gốc**, ta sang **Symmetry của functions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Symmetry của functions

Hàm chẵn (Even Function / 짝함수) thỏa

```math
f(-x)=f(x),
```

nên đồ thị (graph / 그래프) đối xứng qua trục `y`.

Hàm lẻ (Odd Function / 홀함수) thỏa

```math
f(-x)=-f(x),
```

nên đồ thị (graph / 그래프) đối xứng qua origin.

Symmetry giúp giảm computation. Trong tích hợp (integration / 통합), nếu integrand odd trên `[-a,a]`, integral bằng 0; nếu even, integral bằng hai lần integral trên `[0,a]`.


> **Chuyển mạch:** Từ **Symmetry của functions**, ta sang **Composition và phụ thuộc (dependency / 의존성) trong software** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Composition và phụ thuộc (dependency / 의존성) trong software

Một API chuỗi xử lý (pipeline / 파이프라인) có thể được mô hình (model / 모델) là

```text
raw input -> parser -> validator -> transformer -> serializer
```

Mỗi stage là một function-like transformation. Nếu một stage không injective, thông tin có thể mất và bước sau không thể reconstruct đầu vào (input / 입력). Nếu stage có side effects, mô hình (model / 모델) hàm (function / 함수) thuần túy không còn đủ, nhưng composition vẫn là mô hình tư duy (mental model / 사고 모델) hữu ích để phân tích luồng dữ liệu (data flow / 데이터 흐름).


> **Chuyển mạch:** Từ **Composition và phụ thuộc (dependency / 의존성) trong software**, ta sang **liên kết kiến thức (knowledge connection / 지식 연결)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Composition tạo nền cho chuỗi (chain / 사슬) quy tắc (rule / 규칙), ma trận (matrix / 행렬) products, coordinate transformations và neural networks. Inverse nối với solving equations, inverse matrices và reversible computing. hàm (function / 함수) transformations nối algebra với tín hiệu (signal / 신호) processing: shift theo thời gian, quy mô (scale / 규모) amplitude và frequency đều có dạng biến đổi argument/đầu ra (output / 출력).


> **Chuyển mạch:** Từ **liên kết kiến thức (knowledge connection / 지식 연결)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Hãy nghĩ hàm (function / 함수) như một transformation box. Composition là nối nhiều boxes thành chuỗi xử lý (pipeline / 파이프라인); inverse là một box có khả năng undo box trước; đồ thị (graph / 그래프) transformation là thay đổi coordinate frame hoặc quy mô (scale / 규모) của đầu vào (input / 입력)/đầu ra (output / 출력) mà không cần quên cấu trúc (structure / 구조) gốc.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

`f^{-1}` không phải `1/f`. Không phải hàm (function / 함수) nào cũng có inverse trên lĩnh vực (domain / 도메인) hiện tại. Composition không thường giao hoán. `f(x-h)` dịch phải chứ không phải trái vì transformation xảy ra bên trong đầu vào (input / 입력) coordinate.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Liên kết kiến thức** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết kiến thức

Chapter này giả định bạn đã nắm [Function Concept](./00_function_concept.md) và [Sets, Relations and Mappings](../00_foundations/02_sets_relations_and_mappings.md). Composition được dùng tiếp trong [Linear Transformations](../04_vectors_linear_algebra/02_linear_transformations.md) và [Derivatives](../05_calculus/01_derivatives.md), nơi chuỗi (chain / 사슬) quy tắc (rule / 규칙) chính là sensitivity của một composition.

Trong AI/Software, xem [Matrix Calculus, Jacobian, Hessian và Autodiff](../04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md) và [Math for AI, Data and Software](../09_connections/03_math_for_ai_data_and_software.md) để thấy computational đồ thị (graph / 그래프), chuỗi xử lý (pipeline / 파이프라인) và thông tin (information / 정보) mất mát (loss / 손실) dưới cùng mô hình tư duy (mental model / 사고 모델).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 function concept](./00_function_concept.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
