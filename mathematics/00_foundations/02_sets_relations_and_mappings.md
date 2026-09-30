# Tập hợp, quan hệ và ánh xạ: từ membership đến cấu trúc

> **Mạch đọc:** Đọc **Tập hợp, quan hệ và ánh xạ: từ membership đến cấu trúc** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Set là lớp trừu tượng (abstraction / 추상화) về membership** sang **2. Subset: universal statement dưới dạng set ngôn ngữ (language / 언어)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tập hợp (set / 집합), quan hệ (relation / 관계) và ánh xạ (mapping / 사상) là ba lớp lớp trừu tượng (abstraction / 추상화) xuất hiện gần như khắp toán học và Khoa học máy tính (computer science / 컴퓨터 과학). Set trả lời **đối tượng nào đang thuộc universe ta xét**. quan hệ (relation / 관계) trả lời **những cặp nào được xem là có liên hệ**. hàm (function / 함수)/ánh xạ (mapping / 매핑) thêm discipline: **mỗi đầu vào (input / 입력) phải đi tới đúng một đầu ra (output / 출력)**.

Điểm quan trọng là ba concept này không phải ba chapter rời nhau. Chúng tạo một phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬):

```text
membership
→ subset
→ product space
→ relation
→ equivalence / order
→ function
→ injective / surjective / bijective
→ quotient / inverse / structure preservation
```

## 1. Set là lớp trừu tượng (abstraction / 추상화) về membership

Nếu `x` thuộc set `A`:

```math
x\in A.
```

Nếu không:

```math
x\notin A.
```

Ordinary set không quan tâm thứ tự (order / 순서) hay duplicate. `{1,2,2,3}` biểu diễn cùng set với `{1,2,3}`.

Điều này khác danh sách (list / 목록)/array, nơi thứ tự (order / 순서) và multiplicity thường là part of meaning.

Set lớp trừu tượng (abstraction / 추상화) mạnh vì nó cho phép ta tách **định danh (identity / 식별자) của elements** khỏi **cách lưu trữ chúng**. Trong xác suất (probability / 확률), sự kiện (event / 이벤트) là subset của mẫu (sample / 표본) không gian (space / 공간). Trong tối ưu hóa (optimization / 최적화), feasible set chứa mọi quyết định (decision / 결정) hợp lệ. Trong databases, một truy vấn (query / 쿼리) predicate chọn một subset của rows về mặt conceptual, dù SQL thực tế có bag ngữ nghĩa (semantics / 의미론) và NULL.

## 2. Subset: universal statement dưới dạng set ngôn ngữ (language / 언어)

`A` là subset của `B` nếu

```math
A\subseteq B
```

nghĩa là

```math
\forall x\;(x\in A\Rightarrow x\in B).
```

Đây là liên kết (connection / 연결) trực tiếp giữa set lý thuyết (theory / 이론) và lô-gic (logic / 논리).

Muốn chứng minh hai sets bằng nhau, chiến lược (strategy / 전략) chuẩn gốc (canonical / 정본) là **double inclusion**:

```text
A ⊆ B
B ⊆ A
```

Vì set được xác định hoàn toàn bởi membership, nếu hai sets chứa đúng cùng elements thì chúng bằng nhau.

## 3. Empty set và vacuous truth

Tập rỗng (empty set / 공집합)

```math
\varnothing
```

là subset của mọi set.

Lý do không phải convention tùy ý. `∅⊆A` nghĩa:

```math
\forall x\;(x\in\varnothing\Rightarrow x\in A).
```

Không có `x` nào thuộc `∅`, nên không tồn tại counterexample làm implication sai.

Đây là ví dụ quan trọng của vacuous truth. Cùng mẫu (pattern / 패턴) xuất hiện trong đồ thị (graph / 그래프) lý thuyết (theory / 이론), universal quantification và proofs trên empty structures.

## 4. Union, intersection, difference và complement

Union:

```math
A\cup B
```

chứa elements thuộc `A` hoặc `B` hoặc cả hai.

Intersection:

```math
A\cap B
```

chứa elements thuộc cả hai.

Difference:

```math
A\setminus B
```

chứa elements thuộc `A` nhưng không thuộc `B`.

Nếu có universe `U`, complement:

```math
A^c=U\setminus A.
```

Membership biến các identities này thành Boolean lô-gic (logic / 논리). Ví dụ:

```math
x\in(A\cap B)
\iff
(x\in A)\land(x\in B).
```

Do đó De Morgan cho sets:

```math
(A\cup B)^c=A^c\cap B^c
```

và

```math
(A\cap B)^c=A^c\cup B^c.
```

không phải hai formula ngẫu nhiên; chúng là De Morgan lô-gic (logic / 논리) applied vào membership predicates.

## 5. Cartesian sản phẩm (product / 제품) tạo không gian của possible pairs

Tích Descartes (Cartesian product / 데카르트 곱):

```math
A\times B
=
\{(a,b):a\in A,b\in B\}.
```

Nếu

```text
A={1,2}
B={x,y}
```

thì

```text
A×B={(1,x),(1,y),(2,x),(2,y)}.
```

Cartesian sản phẩm (product / 제품) quan trọng vì nó tạo universe cho quan hệ (relation / 관계).

Ví dụ:

```text
Users × Products
```

là mọi user-product pairs có thể có. “người dùng (user / 사용자) purchased sản phẩm (product / 제품)” chỉ chọn một subset của possible pairs đó.

Trong xác suất (probability / 확률), joint mẫu (sample / 표본) không gian (space / 공간) thường là sản phẩm (product / 제품) của thành phần (component / 컴포넌트) spaces khi mô hình (model / 모델) phù hợp. Trong trạng thái (state / 상태) machines, state-action pairs cũng có sản phẩm (product / 제품) cấu trúc (structure / 구조).

## 6. quan hệ (relation / 관계) là subset của sản phẩm (product / 제품) không gian (space / 공간)

Một nhị phân (binary / 이진) quan hệ (relation / 관계) `R` từ `A` tới `B` là

```math
R\subseteq A\times B.
```

Nếu `(a,b)∈R`, ta nói `a` liên hệ với `b`.

Ví dụ quan hệ (relation / 관계) “employee works for company” là subset của

```text
Employees × Companies.
```

Quan hệ (relation / 관계) “người dùng (user / 사용자) follows người dùng (user / 사용자)” là subset của

```text
Users × Users.
```

Đồ thị (graph / 그래프) directed cũng có thể nhìn như quan hệ (relation / 관계) trên vertices: edge `(u,v)` nghĩa `uRv`.

Đây là reason đồ thị (graph / 그래프) lý thuyết (theory / 이론), cơ sở dữ liệu (database / 데이터베이스) relations và thứ tự (order / 순서) relations có family resemblance: tất cả đều bắt đầu từ **which tuples are allowed**.

## 7. Properties của quan hệ (relation / 관계) và ý nghĩa structural

### Reflexive

Reflexive hỏi mỗi phần tử có quan hệ với chính nó hay không. Tính chất này là một điều kiện cục bộ, nhưng nó giúp phân biệt các loại relation trước khi xét chúng tạo cấu trúc gì.

```math
aRa
```

cho mọi `a`.

### Symmetric

Symmetric kiểm tra chiều của quan hệ: nếu A liên hệ B thì B có liên hệ A không. Hãy dùng nó để nhận ra khi nào relation mô tả liên kết hai chiều và khi nào cần giữ hướng.

```math
aRb\Rightarrow bRa.
```

### Antisymmetric

Antisymmetric không có nghĩa là “không đối xứng” hoàn toàn; nó cấm hai phần tử khác nhau cùng liên hệ hai chiều. Đây là điều kiện nền cho thứ tự bộ phận.

```math
aRb\land bRa\Rightarrow a=b.
```

Antisymmetric không có nghĩa “không symmetric”; nó nói mutual quan hệ (relation / 관계) giữa distinct elements bị cấm.

### Transitive

Transitive hỏi liệu quan hệ có truyền qua một phần tử trung gian hay không. Nó giúp nén chuỗi quan hệ và là cầu nối tới equivalence relation và order.

```math
aRb\land bRc\Rightarrow aRc.
```

Những properties này không chỉ là checklist. Chúng quyết định quan hệ (relation / 관계) tạo ra cấu trúc (structure / 구조) gì.

## 8. Equivalence quan hệ (relation / 관계): formal hóa “khác biểu diễn (representation / 표현) nhưng cùng đối tượng (object / 객체) lớp (class / 클래스)”

Equivalence quan hệ (relation / 관계) là reflexive, symmetric và transitive.

Ví dụ modulo 3:

```math
a\sim b
\iff
3\mid(a-b).
```

Integers được partition thành ba equivalence classes:

```text
[0], [1], [2]
```

Mọi integer nằm đúng một lớp (class / 클래스).

Điểm sâu là equivalence quan hệ (relation / 관계) cho phép ta **collapse details không quan trọng**. Thay vì phân biệt mọi integer, modulo 3 chỉ giữ remainder lớp (class / 클래스).

Cùng idea xuất hiện khi:

- coi fractions `1/2` và `2/4` là cùng rational number;
- coi vectors khác nhau bởi một transformation nào đó là same orbit/lớp (class / 클래스);
- quotient spaces trong algebra/topology;
- canonicalization trong software.

## 9. Partial thứ tự (order / 순서): formal hóa phụ thuộc (dependency / 의존성) và hierarchy

Partial thứ tự (order / 순서) thường reflexive, antisymmetric và transitive.

Không phải mọi pair đều cần comparable.

Ví dụ set inclusion:

```math
A\subseteq B
```

là partial thứ tự (order / 순서) trên power set.

Phụ thuộc (dependency / 의존성) relations cũng thường partial-order-like khi không có cycles. Hai tasks độc lập có thể không đứng trước/sau nhau.

Total thứ tự (order / 순서) thêm yêu cầu (requirement / 요구사항) rằng mọi pair comparable. Number line với `≤` là total thứ tự (order / 순서); phụ thuộc (dependency / 의존성) DAG nói chung không phải total thứ tự (order / 순서).

## 10. hàm (function / 함수) là quan hệ (relation / 관계) có tính đơn trị toàn phần

Hàm (function / 함수)

```math
f:A\to B
```

có thể được xem là quan hệ (relation / 관계) `R⊆A×B` thỏa:

1. với mọi `a∈A`, tồn tại đầu ra (output / 출력);
2. đầu ra (output / 출력) đó là duy nhất.

Nói cách khác, mỗi đầu vào (input / 입력) có **exactly one** đầu ra (output / 출력).

Hàm (function / 함수) không cần formula. Lookup bảng (table / 테이블), parser, cơ sở dữ liệu (database / 데이터베이스) projection, ảnh (image / 이미지) transform hay trained mô hình (model / 모델) đều có thể là functions nếu ánh xạ (mapping / 매핑) deterministic trong mô hình (model / 모델) đang xét.

## 11. lĩnh vực (domain / 도메인), codomain và ảnh (image / 이미지) không thể bỏ qua

Trong

```math
f:A\to B,
```

`A` là lĩnh vực (domain / 도메인), `B` là codomain.

Ảnh (image / 이미지)/phạm vi (range / 범위) là subset của `B` thực sự được hit:

```math
f(A)=\{f(a):a\in A\}.
```

Cùng formula nhưng khác lĩnh vực (domain / 도메인)/codomain có thể là functions khác nhau về structural properties.

Ví dụ `f(x)=x^2`:

```math
f:\mathbb R\to\mathbb R
```

không surjective.

Nhưng

```math
f:[0,\infty)\to[0,\infty)
```

là bijective.

Vì vậy lĩnh vực (domain / 도메인)/codomain không phải siêu dữ liệu (metadata / 메타데이터) phụ.

## 12. Injective, surjective, bijective như thông tin (information / 정보) hành vi (behavior / 동작)

Injective (đơn ánh / 단사):

```math
f(a)=f(b)\Rightarrow a=b.
```

Different inputs không collapse vào cùng đầu ra (output / 출력). Theo thông tin (information / 정보) viewpoint, injective ánh xạ (mapping / 매핑) không mất distinction giữa inputs.

Surjective (toàn ánh / 전사): mọi đầu ra (output / 출력) trong codomain reachable.

Bijective (song ánh / 전단사): vừa injective vừa surjective.

Bijective ánh xạ (mapping / 매핑) có inverse:

```math
f^{-1}:B\to A.
```

Đây là lý do invertibility gắn với thông tin (information / 정보) preservation.

Lossless encoding cần khôi phục (recovery / 복구) ánh xạ (mapping / 매핑); unique IDs cần injectivity; coordinate changes dùng bijections trên suitable domains.

## 13. Composition: nối mappings thành chuỗi xử lý (pipeline / 파이프라인)

Nếu

```math
f:A\to B,
\qquad
g:B\to C,
```

thì

```math
(g\circ f)(x)=g(f(x)).
```

Composition là ngôn ngữ của pipelines.

Trong software:

```text
raw input
→ parse
→ validate
→ transform
→ serialize
```

Trong neural networks, layers compose thành mô hình (model / 모델). Trong hình học (geometry / 기하학), transformations compose. Trong category lý thuyết (theory / 이론), composition trở thành central thành phần nguyên thủy (primitive / 기본 요소).

Composition generally không commutative:

```math
g\circ f\ne f\circ g.
```

Thứ tự (order / 순서) matters vì intermediate spaces/meaning khác nhau.

## 14. Cardinality: đo kích thước (size / 크기) bằng bijection

Với finite sets, cardinality chỉ là count.

Với infinite sets, definition bằng bijection trở nên sâu hơn. Natural numbers và even numbers có cùng cardinality vì

```math
n\mapsto 2n
```

là bijection.

Điều này phá intuition hữu hạn “proper subset luôn nhỏ hơn”.

Cantor's diagonal idea còn cho thấy power set của một set có cardinality strictly lớn hơn chính set đó:

```math
|A|<|\mathcal P(A)|.
```

Với finite set `|A|=n`:

```math
|\mathcal P(A)|=2^n
```

vì mỗi element tương ứng một include/exclude bit.

## 15. Power set và state-space explosion

Power set không chỉ là concept pure math. Nếu hệ thống (system / 시스템) có `n` Boolean flags, mỗi subset các flags-on là một trạng thái (state / 상태), nên có

```math
2^n
```

possible states.

Đây là nguồn (source / 소스) của combinatorial explosion trong exhaustive tìm kiếm (search / 검색), tính năng (feature / 기능) subsets, truy cập (access / 접근) combinations và trạng thái (state / 상태) xác minh (verification / 확인).

Set lý thuyết (theory / 이론) vì vậy nối trực tiếp sang độ phức tạp (complexity / 복잡도).

## 16. cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결): quan hệ (relation / 관계) toán học và SQL quan hệ (relation / 관계) không hoàn toàn giống nhau

Relational mô hình (model / 모델) toán học gần với set of tuples. SQL tables thực tế có thể cho duplicate rows và `NULL`, nên SQL ngữ nghĩa (semantics / 의미론) không trùng set lý thuyết (theory / 이론) thuần.

Điều này là ví dụ quan trọng của mô hình (model / 모델) layering:

```text
mathematical relation
≠ implementation data structure
```

Nhưng set/quan hệ (relation / 관계) thinking vẫn giúp hiểu joins, keys, functional dependencies và normalization.

## 17. xác suất (probability / 확률) liên kết (connection / 연결)

Mẫu (sample / 표본) không gian (space / 공간) `Ω` là set outcomes; sự kiện (event / 이벤트) `A` là subset:

```math
A\subseteq\Omega.
```

Intersection là “A và B”, union là “A hoặc B”, complement là “không A”.

Xác suất (probability / 확률) measure gán number cho subsets/events. Vì vậy xác suất (probability / 확률) lý thuyết (theory / 이론) xây trực tiếp trên set lô-gic (logic / 논리).

Conditional xác suất (probability / 확률) còn có thể nhìn như việc **restrict universe sang sự kiện (event / 이벤트) B đã biết xảy ra**, rồi renormalize xác suất (probability / 확률) trong universe mới.

## 18. dùng chung (common / 공통) proof strategies với sets

Để chứng minh

```math
A=B,
```

chọn arbitrary `x`, rồi chứng minh

```math
x\in A\iff x\in B.
```

Hoặc double inclusion.

Để chứng minh two sets disjoint:

```math
A\cap B=\varnothing,
```

show rằng giả sử `x` thuộc cả hai dẫn tới contradiction.

Proof set identities thường trở thành propositional lô-gic (logic / 논리) sau khi expand membership definitions.

## Mô hình tư duy (mental model / 사고 모델)

> Set định nghĩa **universe của objects**. Cartesian sản phẩm (product / 제품) tạo **universe của possible tuples**. quan hệ (relation / 관계) chọn **tuples được phép nối**. Equivalence quan hệ (relation / 관계) gom representations thành classes; partial thứ tự (order / 순서) tạo hierarchy/phụ thuộc (dependency / 의존성); hàm (function / 함수) ép mỗi đầu vào (input / 입력) đi tới đúng một đầu ra (output / 출력). Phần lớn cấu trúc toán học cao hơn chỉ là thêm rules lên những nền này.

## Dùng chung (common / 공통) Misconceptions

Set không phải list: order và duplicates không thuộc ordinary set. `A⊂B` convention có thể khác textbook về proper subset, nên nên dùng ký hiệu rõ. Antisymmetric không phải opposite của symmetric. Codomain không nhất thiết bằng image. Injective không imply surjective. Với infinite sets, proper subset có thể có cùng cardinality với parent set.
