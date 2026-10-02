# Hàm số: từ quan hệ đến quy tắc biến đổi

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hàm số: từ quan hệ đến quy tắc biến đổi**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ quan hệ (relation / 관계) đến hàm (function / 함수)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Codomain và phạm vi (range / 범위): vì sao phải phân biệt?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối function concept với input, output, domain và composition, để hiểu hàm như quy tắc ánh xạ có điều kiện.

Hàm số (Function / 함수) là một trong những ý tưởng trung tâm của toán học vì nó cho phép ta mô tả **một quy tắc ổn định nối đầu vào (input / 입력) với đầu ra (output / 출력)**. Khi nói “nhiệt độ phụ thuộc vào thời gian”, “giá tiền phụ thuộc vào số lượng”, “tọa độ mới phụ thuộc vào tọa độ cũ sau một phép quay”, hoặc “mô hình (model / 모델) nhận tính năng (feature / 기능) véc-tơ (vector / 벡터) và trả về prediction”, ta đang nhìn thế giới dưới dạng một ánh xạ (mapping / 매핑).

Điểm quan trọng là hàm (function / 함수) không bắt đầu từ công thức. Nó bắt đầu từ câu hỏi: **nếu biết trạng thái đầu vào, ta có xác định được trạng thái đầu ra hay không?** Công thức, bảng dữ liệu, đồ thị (graph / 그래프), lookup bảng (table / 테이블), chương trình máy tính hay neural mạng (network / 네트워크) chỉ là các cách biểu diễn khác nhau của cùng ý tưởng ánh xạ (mapping / 매핑) đó.

> Hàm số là một đặc tả hợp đồng (contract / 계약): đầu vào (input / 입력) thuộc không gian nào, đầu ra (output / 출력) thuộc không gian nào, và mỗi đầu vào (input / 입력) hợp lệ được map tới đầu ra (output / 출력) nào.

## Từ quan hệ (relation / 관계) đến hàm (function / 함수)

Một quan hệ (Relation / 관계) chỉ nói rằng một số objects có liên hệ với nhau. Nếu `A` là tập người và `B` là tập thành phố, quan hệ “đã từng sống ở” có thể nối một người với nhiều thành phố. Nó chưa phải hàm (function / 함수) từ người sang thành phố vì cùng một đầu vào (input / 입력) có thể có nhiều outputs.

Một hàm (function / 함수) `f:A→B` thêm ràng buộc (constraint / 제약조건) mạnh hơn: **mỗi phần tử của `A` phải được gán đúng một phần tử trong `B`**.

```math
f:A\to B
```

`A` là miền xác định (Domain / 정의역). `B` là đối miền (Codomain / 공역). Với mỗi `x∈A`, notation

```math
y=f(x)
```

nói rằng `f` map đầu vào (input / 입력) `x` thành đầu ra (output / 출력) `y`.

Điều kiện “đúng một đầu ra (output / 출력)” không cấm nhiều inputs cùng đi tới một đầu ra (output / 출력). Ví dụ

```math
f(x)=x^2
```

cho `f(2)=4` và `f(-2)=4`; điều này hoàn toàn hợp lệ. hàm (function / 함수) chỉ cấm một đầu vào (input / 입력) duy nhất đồng thời được gán hai outputs khác nhau trong cùng definition.

### Lĩnh vực (domain / 도메인) không phải ghi chú phụ

Xét biểu thức

```math
f(x)=\frac{1}{x}.
```

Nếu chỉ nhìn formula, ta có thể tưởng lĩnh vực (domain / 도메인) là mọi số thực. Nhưng tại `x=0`, division không được định nghĩa. Vì vậy một definition chính xác phải nói

```math
f:\mathbb R\setminus\{0\}\to\mathbb R.
```

Lĩnh vực (domain / 도메인) là một phần của hàm (function / 함수), không phải siêu dữ liệu (metadata / 메타데이터) trang trí. Cùng formula nhưng khác lĩnh vực (domain / 도메인) có thể tạo ra những hàm (function / 함수) có properties khác nhau.

Ví dụ `f(x)=x^2` trên toàn `R` không injective. Nếu restrict lĩnh vực (domain / 도메인) thành `[0,∞)`, nó trở thành injective và có inverse `√x` trên phạm vi (range / 범위) tương ứng. Việc “chọn lĩnh vực (domain / 도메인)” vì thế có thể thay đổi cả cấu trúc (structure / 구조) của bài toán (problem / 문제).

> **Chuyển mạch:** Trong **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Codomain và phạm vi (range / 범위): vì sao phải phân biệt?** tiếp nhận điểm tựa từ **Từ quan hệ (relation / 관계) đến hàm (function / 함수)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàm (function / 함수) không nhất thiết là công thức đóng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Codomain và phạm vi (range / 범위): vì sao phải phân biệt?

Phạm vi (range / 범위) hay ảnh (image / 이미지) là tập outputs thực sự đạt được. Codomain là tập mà ta tuyên bố đầu ra (output / 출력) thuộc vào.

Với

```math
f:\mathbb R\to\mathbb R,\qquad f(x)=x^2,
```

codomain là `R`, nhưng phạm vi (range / 범위) là `[0,∞)`.

Nếu thay definition bằng

```math
f:\mathbb R\to[0,\infty),\qquad f(x)=x^2,
```

formula không đổi nhưng thuộc tính (property / 속성) “surjective hay không” đã đổi. Trong definition thứ nhất, hàm (function / 함수) không surjective lên `R` vì không có đầu vào (input / 입력) nào cho đầu ra (output / 출력) âm. Trong definition thứ hai, nó surjective lên `[0,∞)`.

Đây là lý do toán học hiện đại coi hàm (function / 함수) là **ánh xạ (mapping / 매핑) kèm lĩnh vực (domain / 도메인) và codomain**, không chỉ là expression.

> **Chuyển mạch:** Ở chặng này của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Hàm (function / 함수) không nhất thiết là công thức đóng** tiếp nhận điểm tựa từ **Codomain và phạm vi (range / 범위): vì sao phải phân biệt?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đồ thị (graph / 그래프) của hàm (function / 함수) là tập các input-output pairs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm (function / 함수) không nhất thiết là công thức đóng

Khi học phổ thông, hàm (function / 함수) thường xuất hiện dưới dạng `y=2x+3`, `y=x²` hay `y=sin x`, nên dễ hình thành misconception rằng hàm (function / 함수) phải có closed-form formula.

Thực tế, một hàm (function / 함수) có thể được định nghĩa bằng bảng (table / 테이블):

| user_id | risk_score |
|---|---:|
| A | 0.13 |
| B | 0.82 |

Nó cũng có thể được định nghĩa bằng thuật toán (algorithm / 알고리즘), simulation hoặc program. Một sorting hàm (function / 함수) nhận một danh sách (list / 목록) và trả danh sách (list / 목록) đã sắp xếp; một trình biên dịch (compiler / 컴파일러) pass nhận AST và trả AST mới; một neural mạng (network / 네트워크) nhận véc-tơ (vector / 벡터) đầu vào (input / 입력) và trả logits. Nếu ánh xạ (mapping / 매핑) deterministic và đặc tả hợp đồng (contract / 계약) được xác định rõ, tất cả đều có thể được nhìn như functions.

Điều này rất quan trọng vì nó tách **mathematical đối tượng (object / 객체)** khỏi **biểu diễn (representation / 표현)**. hàm (function / 함수) là ánh xạ (mapping / 매핑); formula chỉ là một cách biểu diễn ánh xạ (mapping / 매핑).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Đồ thị (graph / 그래프) của hàm (function / 함수) là tập các input-output pairs** tiếp nhận điểm tựa từ **Hàm (function / 함수) không nhất thiết là công thức đóng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Injective, surjective và bijective** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồ thị (graph / 그래프) của hàm (function / 함수) là tập các input-output pairs

Với hàm (function / 함수) một biến thực `f:R→R`, đồ thị (graph / 그래프) là tập

```math
\{(x,f(x))\mid x\in\operatorname{domain}(f)\}.
```

Đồ thị (graph / 그래프) không phải là hàm (function / 함수); nó là một biểu diễn (representation / 표현) hình học của hàm (function / 함수).

Vertical line kiểm thử (test / 테스트) xuất phát trực tiếp từ definition. Nếu một vertical line `x=c` cắt curve ở hai points khác nhau, cùng đầu vào (input / 입력) `c` đang tương ứng hai values của `y`. quan hệ (relation / 관계) đó không thể là đồ thị (graph / 그래프) của một single-valued hàm (function / 함수) `y=f(x)`.

Nhưng quan hệ (relation / 관계) đó vẫn có thể rất hữu ích. Circle

```math
x^2+y^2=1
```

không phải toàn cục (global / 전역) hàm (function / 함수) `y=f(x)` vì với nhiều `x` có hai values `y=±√(1-x²)`. Ta có thể chia nó thành hai functions, hoặc dùng parametric biểu diễn (representation / 표현). Đây là ví dụ cho thấy “không phải hàm (function / 함수) theo biểu diễn (representation / 표현) hiện tại” không có nghĩa đối tượng (object / 객체) vô dụng; có thể biểu diễn (representation / 표현) chưa phù hợp.

> **Chuyển mạch:** Trong **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Injective, surjective và bijective** tiếp nhận điểm tựa từ **Đồ thị (graph / 그래프) của hàm (function / 함수) là tập các input-output pairs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Composition: xây hệ phức tạp từ transformations đơn giản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Injective, surjective và bijective

Ba properties này mô tả cách ánh xạ (mapping / 매핑) sử dụng đầu vào (input / 입력) và codomain.

Một hàm (function / 함수) là đơn ánh (Injective / 일대일 함수) nếu

```math
f(x_1)=f(x_2)\Rightarrow x_1=x_2.
```

Nói trực giác: hai inputs khác nhau không bị collapse thành cùng đầu ra (output / 출력). thông tin (information / 정보) về đầu vào (input / 입력) không bị mất theo kiểu đó.

Một hàm (function / 함수) là toàn ánh (Surjective / 전사 함수) nếu mọi element trong codomain đều được hit bởi ít nhất một đầu vào (input / 입력).

Một hàm (function / 함수) là song ánh (Bijective / 전단사 함수) nếu vừa injective vừa surjective. Khi đó mỗi đầu ra (output / 출력) trong codomain tương ứng đúng một đầu vào (input / 입력) và ánh xạ (mapping / 매핑) có thể đảo ngược hoàn toàn.

### Invertibility là câu hỏi về thông tin (information / 정보) preservation

Nếu `f` bijective, tồn tại inverse hàm (function / 함수)

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

Đây không chỉ là một trick đại số. Inverse tồn tại khi đầu ra (output / 출력) giữ đủ thông tin (information / 정보) để recover đầu vào (input / 입력) duy nhất.

Xét

```math
f(x)=x^2.
```

Nếu lĩnh vực (domain / 도메인) là toàn `R`, đầu ra (output / 출력) `4` không cho biết đầu vào (input / 입력) là `2` hay `-2`; thông tin (information / 정보) về sign đã mất. Vì vậy inverse toàn cục (global / 전역) không tồn tại. Restrict lĩnh vực (domain / 도메인) sang `x≥0` loại ambiguity đó và inverse trở thành `√x`.

Trong computing, hashing thường cố ý không invertible: nhiều possible inputs map vào không gian đầu ra (output / 출력) nhỏ hơn. Compression lossless phải preserve đủ thông tin (information / 정보) để decode; lossy compression chấp nhận mất một phần thông tin (information / 정보) để giảm biểu diễn (representation / 표현) kích thước (size / 크기).

> **Chuyển mạch:** Ở chặng này của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Composition: xây hệ phức tạp từ transformations đơn giản** tiếp nhận điểm tựa từ **Injective, surjective và bijective** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàm (function / 함수) như transformation của cấu trúc (structure / 구조)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Composition: xây hệ phức tạp từ transformations đơn giản

Giả sử

```math
g:A\to B
```

và

```math
f:B\to C.
```

Nếu đầu ra (output / 출력) của `g` là đầu vào (input / 입력) hợp lệ của `f`, ta có composition

```math
(f\circ g)(x)=f(g(x)).
```

Composition (Composition / 합성함수) là cách toán học mô tả chuỗi xử lý (pipeline / 파이프라인). Một complex transformation có thể được hiểu như chuỗi các transformations nhỏ.

Ví dụ, giả sử temperature Celsius được chuyển sang Fahrenheit rồi thành label:

```text
Celsius → Fahrenheit → category
```

Nếu `g` convert Celsius thành Fahrenheit và `f` convert Fahrenheit thành category, whole tiến trình (process / 프로세스) là `f∘g`.

Trong software, parse → validate → normalize → persist là chuỗi xử lý (pipeline / 파이프라인) của functions. Trong neural mạng (network / 네트워크),

```math
f(x)=f_L(f_{L-1}(\cdots f_2(f_1(x))\cdots))
```

là composition của layers. chuỗi (chain / 사슬) quy tắc (rule / 규칙) trong calculus tồn tại chính vì ta cần biết sensitivity của một composition.

### Composition thường không giao hoán

Thông thường

```math
f\circ g\ne g\circ f.
```

Rotate rồi translate một đối tượng (object / 객체) thường khác translate rồi rotate. Normalize dữ liệu (data / 데이터) rồi apply threshold có thể khác threshold rồi normalize. thứ tự (order / 순서) là một phần của tiến trình (process / 프로세스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Hàm (function / 함수) như transformation của cấu trúc (structure / 구조)** tiếp nhận điểm tựa từ **Composition: xây hệ phức tạp từ transformations đơn giản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parameters và family of functions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm (function / 함수) như transformation của cấu trúc (structure / 구조)

Một cách nhìn mạnh hơn “machine input-output” là coi hàm (function / 함수) như một transformation giữa spaces.

```math
f:A\to B
```

nói rằng ta đang chuyển description từ không gian (space / 공간) `A` sang không gian (space / 공간) `B`. Với tuyến tính (linear / 선형) algebra, ma trận (matrix / 행렬) đại diện tuyến tính (linear / 선형) hàm (function / 함수) giữa véc-tơ (vector / 벡터) spaces. Với xác suất (probability / 확률), random variable là hàm (function / 함수) từ mẫu (sample / 표본) không gian (space / 공간) sang numbers. Với tối ưu hóa (optimization / 최적화), mục tiêu (objective / 목표) hàm (function / 함수) map quyết định (decision / 결정) véc-tơ (vector / 벡터) thành scalar chi phí (cost / 비용). Với truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리), truy vấn (query / 쿼리) map cơ sở dữ liệu (database / 데이터베이스) trạng thái (state / 상태) thành kết quả (result / 결과) quan hệ (relation / 관계).

Cùng một concept hàm (function / 함수) vì thế nối nhiều mảng toán khác nhau.

> **Chuyển mạch:** Trong **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Parameters và family of functions** tiếp nhận điểm tựa từ **Hàm (function / 함수) như transformation của cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Piecewise functions và nghiệp vụ (business / 비즈니스) rules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parameters và family of functions

Xét

```math
f(x)=ax+b.
```

`x` là variable đầu vào (input / 입력). `a` và `b` là parameters (Parameters / 매개변수) chọn một hàm (function / 함수) cụ thể trong family affine functions.

Nếu `a=2,b=3`, ta có một member cụ thể `f(x)=2x+3`. Nếu đổi parameters, ánh xạ (mapping / 매핑) thay đổi.

Machine học tập (learning / 학습) có thể được nhìn như bài toán: chọn parameters `θ` để hàm (function / 함수)

```math
f_\theta(x)
```

phù hợp dữ liệu (data / 데이터) và mục tiêu (objective / 목표). huấn luyện (training / 학습) không “tạo phép thuật”; nó tìm kiếm (search / 검색) trong một family functions được kiến trúc (architecture / 아키텍처) cho phép.

> **Chuyển mạch:** Ở chặng này của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Piecewise functions và nghiệp vụ (business / 비즈니스) rules** tiếp nhận điểm tựa từ **Parameters và family of functions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monotonicity và inverse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Piecewise functions và nghiệp vụ (business / 비즈니스) rules

Không phải hệ thống (system / 시스템) nào cũng dùng cùng quy tắc (rule / 규칙) trên toàn lĩnh vực (domain / 도메인). Piecewise hàm (function / 함수) cho phép quy tắc (rule / 규칙) phụ thuộc region.

```math
f(x)=
\begin{cases}
-x,&x<0,\\
x,&x\ge0.
\end{cases}
```

định nghĩa absolute giá trị (value / 값) `|x|`.

Tax brackets, shipping fees, tiered pricing, ReLU activation, tỷ lệ (rate / 비율) limits và SLA penalties đều thường có piecewise cấu trúc (structure / 구조).

Điểm cần chú ý là piecewise hàm (function / 함수) vẫn chỉ là **một hàm (function / 함수)**, nếu tại mỗi đầu vào (input / 입력) đúng một branch xác định đầu ra (output / 출력). ranh giới (boundary / 경계) conditions cần được viết cẩn thận để tránh gap hoặc overlap gây ambiguity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Monotonicity và inverse** tiếp nhận điểm tựa từ **Piecewise functions và nghiệp vụ (business / 비즈니스) rules** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transformations của đồ thị (graph / 그래프) và tác động lên đầu vào (input / 입력)/đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monotonicity và inverse

Nếu hàm (function / 함수) strictly increasing trên một interval,

```math
x_1<x_2\Rightarrow f(x_1)<f(x_2),
```

thì nó injective trên interval đó. Tương tự với strictly decreasing.

Monotonicity (Monotonicity / 단조성) vì thế là một cách geometric để thấy invertibility cục bộ hoặc trên restricted lĩnh vực (domain / 도메인). Đây là lý do logarithm có thể là inverse của exponential: exponential strictly increasing trên `R` khi cơ sở (base / 기반) `>1`.

> **Chuyển mạch:** Trong **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Transformations của đồ thị (graph / 그래프) và tác động lên đầu vào (input / 입력)/đầu ra (output / 출력)** tiếp nhận điểm tựa từ **Monotonicity và inverse** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàm (function / 함수) equality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transformations của đồ thị (graph / 그래프) và tác động lên đầu vào (input / 입력)/đầu ra (output / 출력)

Nếu `y=f(x)`, một số transformations cơ bản là:

```math
g(x)=f(x)+c
```

shift đầu ra (output / 출력) lên `c`.

```math
g(x)=f(x-c)
```

shift đồ thị (graph / 그래프) sang phải `c`, vì muốn `g(x)` dùng cùng old đầu vào (input / 입력) `u`, ta cần `x-c=u`, tức `x=u+c`.

```math
g(x)=af(x)
```

Quy mô (scale / 규모) đầu ra (output / 출력) theo `a`.

```math
g(x)=f(ax)
```

Quy mô (scale / 규모) đầu vào (input / 입력) axis theo factor nghịch đảo. Đây là chỗ dễ nhầm vì transformation xảy ra **bên trong đầu vào (input / 입력)**.

Cách nhớ tốt hơn không phải thuộc quy tắc (rule / 규칙) “inside ngược, outside thuận”, mà hỏi: “để hàm (function / 함수) cũ nhận cùng đầu vào (input / 입력) như trước, đầu vào (input / 입력) mới phải thay đổi thế nào?”

> **Chuyển mạch:** Ở chặng này của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Hàm (function / 함수) equality** tiếp nhận điểm tựa từ **Transformations của đồ thị (graph / 그래프) và tác động lên đầu vào (input / 입력)/đầu ra (output / 출력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수), kiểu (type / 타입) và Đặc tả API (API contract / API 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm (function / 함수) equality

Hai functions bằng nhau khi chúng có cùng lĩnh vực (domain / 도메인) phù hợp và cho cùng đầu ra (output / 출력) với mọi đầu vào (input / 입력) trong lĩnh vực (domain / 도메인) đó. Hai formulas trông khác nhau vẫn có thể represent cùng hàm (function / 함수) trên một lĩnh vực (domain / 도메인).

Ví dụ

```math
\frac{x^2-1}{x-1}=x+1
```

đúng khi `x≠1`. Nhưng nếu hàm (function / 함수) bên trái có lĩnh vực (domain / 도메인) `R\{1}` còn `x+1` được định nghĩa trên toàn `R`, thì chúng không hoàn toàn là cùng hàm (function / 함수) nếu lĩnh vực (domain / 도메인) được coi là một phần của đối tượng (object / 객체).

Đây là distinction quan trọng khi simplification tạo ra removable discontinuity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm số: từ quan hệ đến quy tắc biến đổi**, sau nội dung của **Hàm (function / 함수) equality**, **Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수), kiểu (type / 타입) và Đặc tả API (API contract / API 계약)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수) trong xác suất (probability / 확률)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수), kiểu (type / 타입) và Đặc tả API (API contract / API 계약)

Trong programming, một hàm (function / 함수) signature như

```text
User → RiskScore
```

rất giống notation

```math
f:A\to B.
```

Hệ kiểu (type system / 타입 시스템) nói đầu vào (input / 입력)/đầu ra (output / 출력) spaces hợp lệ; hiện thực (implementation / 구현) nói ánh xạ (mapping / 매핑) cụ thể. Nếu hàm (function / 함수) partial vì một số inputs gây lỗi (error / 오류), ta có thể mô hình (model / 모델) đầu ra (output / 출력) không gian (space / 공간) rộng hơn, chẳng hạn

```text
UserInput → Result<User, ValidationError>
```

thay vì giả vờ mọi đầu vào (input / 입력) đều hợp lệ.

Cách nhìn này giúp thấy lĩnh vực (domain / 도메인)/codomain không phải khái niệm hàn lâm xa mã (code / 코드); chúng là mathematical phiên bản (version / 버전) của đặc tả hợp đồng (contract / 계약) thiết kế (design / 설계).

> **Chuyển mạch:** Trong **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수) trong xác suất (probability / 확률)** tiếp nhận điểm tựa từ **Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수), kiểu (type / 타입) và Đặc tả API (API contract / API 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi hàm (function / 함수) mô hình (model / 모델) không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수) trong xác suất (probability / 확률)

Một biến ngẫu nhiên (Random Variable / 확률변수) thực chất là hàm (function / 함수)

```math
X:\Omega\to\mathbb R,
```

map mỗi elementary kết quả (outcome / 결과) trong mẫu (sample / 표본) không gian (space / 공간) `Ω` thành một number. “Random” nằm ở kết quả (outcome / 결과) được chọn theo xác suất (probability / 확률) mô hình (model / 모델); ánh xạ (mapping / 매핑) `X` itself là deterministic.

Đây là một liên kết (connection / 연결) quan trọng: khi hiểu hàm (function / 함수) tốt, xác suất (probability / 확률) bớt giống một collection công thức riêng biệt.

> **Chuyển mạch:** Ở chặng này của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Khi hàm (function / 함수) mô hình (model / 모델) không đủ** tiếp nhận điểm tựa từ **Liên kết kiến thức (knowledge connection / 지식 연결) — hàm (function / 함수) trong xác suất (probability / 확률)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi hàm (function / 함수) mô hình (model / 모델) không đủ

Hàm (function / 함수) giả định cùng đầu vào (input / 입력) trong mô hình (model / 모델) xác định một đầu ra (output / 출력). Nhưng nhiều các hệ thống (systems / 시스템들) thực tế có noise, hidden trạng thái (state / 상태) hoặc randomness. Khi cùng observable đầu vào (input / 입력) có thể dẫn tới nhiều outcomes, ta có thể cần xác suất (probability / 확률) phân phối (distribution / 분포)

```math
P(Y\mid X=x)
```

thay vì deterministic `y=f(x)`.

Trong động (dynamic / 동적) các hệ thống (systems / 시스템들), đầu ra (output / 출력) còn phụ thuộc trạng thái nội bộ (internal state / 내부 상태) chứ không chỉ hiện tại (current / 현재) bên ngoài (external / 외부) đầu vào (input / 입력). Khi đó mô hình (model / 모델) state-space phù hợp hơn một stateless hàm (function / 함수) đơn giản.

Điều này không làm hàm (function / 함수) mất giá trị; nó chỉ nhắc rằng mô hình (model / 모델) phải chứa đủ variables để deterministic ánh xạ (mapping / 매핑) trở nên hợp lý, hoặc phải chuyển sang probabilistic mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Khi hàm (function / 함수) mô hình (model / 모델) không đủ** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> hàm (function / 함수) là một transformation có đặc tả hợp đồng (contract / 계약). lĩnh vực (domain / 도메인) nói những trạng thái đầu vào nào hợp lệ; quy tắc (rule / 규칙) nói chúng được biến đổi ra sao; codomain nói ta đang mô tả đầu ra (output / 출력) trong không gian (space / 공간) nào. Composition xây hệ lớn từ transformations nhỏ, còn invertibility hỏi transformation có giữ đủ thông tin (information / 정보) để quay ngược lại hay không.

> **Chuyển mạch:** Trong **Hàm số: từ quan hệ đến quy tắc biến đổi**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“hàm (function / 함수) nghĩa là mỗi đầu ra (output / 출력) chỉ có một đầu vào (input / 입력).”** Sai chiều. yêu cầu (requirement / 요구사항) là mỗi đầu vào (input / 입력) có đúng một đầu ra (output / 출력). Nhiều inputs có thể cùng map tới một đầu ra (output / 출력); chỉ khi hàm (function / 함수) injective thì đầu ra (output / 출력) mới xác định đầu vào (input / 입력) duy nhất.

**“hàm (function / 함수) phải có công thức.”** Formula chỉ là biểu diễn (representation / 표현). bảng (table / 테이블), program, lookup ánh xạ (mapping / 매핑), simulation hay learned mô hình (model / 모델) đều có thể represent a hàm (function / 함수).

**“`f^{-1}` là `1/f`.”** Inverse hàm (function / 함수) undo ánh xạ (mapping / 매핑); reciprocal chỉ lấy nghịch đảo giá trị (value / 값). Hai operations khác nhau hoàn toàn.

**“lĩnh vực (domain / 도메인) chỉ cần nhìn từ formula.”** ngữ cảnh (context / 맥락) cũng quyết định lĩnh vực (domain / 도메인). `√x` về algebra có lĩnh vực (domain / 도메인) `x≥0` trên real numbers, nhưng một mô hình vật lý (physical model / 물리 모델) có thể còn restriction chặt hơn, chẳng hạn length phải nằm trong một khoảng đo thực tế.

**“Hai expressions bằng nhau thì hai functions luôn giống nhau.”** lĩnh vực (domain / 도메인)/codomain là một phần của hàm (function / 함수). Simplification có thể che mất excluded points hoặc thay đổi structural properties.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
