# Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Solution set luôn phụ thuộc lĩnh vực (domain / 도메인)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Equivalence transformations: vì sao các phép biến đổi hợp lệ?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối equations với inequalities, solution set và biến đổi tương đương, để phân biệt thao tác giữ nghiệm với thao tác làm đổi miền nghiệm.

Phương trình (equation / 방정식) và bất phương trình (inequality / 부등식) đều là cách biểu diễn **ràng buộc** lên những giá trị có thể xảy ra. Khi viết

```math
2x+3=11
```

điều quan trọng không phải là ký hiệu `=` tự nó, mà là statement: ta chỉ chấp nhận những `x` làm hai biểu thức đại diện cho cùng một giá trị.

Với bất phương trình

```math
2x+3\le 11,
```

Ràng buộc (constraint / 제약조건) yếu hơn: ta chấp nhận cả một vùng giá trị thay vì chỉ các điểm làm hai vế bằng nhau.

Vì vậy, tư duy đúng không phải là “chuyển vế cho nhanh”, mà là:

> Ta đang biến đổi biểu diễn (representation / 표현) của cùng một solution set. Mỗi bước cần biết nó có bảo toàn nghiệm hai chiều hay chỉ tạo ra candidate cần kiểm tra lại.

## 1. Solution set luôn phụ thuộc lĩnh vực (domain / 도메인)

Một phương trình không có solution set hoàn toàn tách khỏi lĩnh vực (domain / 도메인).

Ví dụ

```math
x^2=2
```

không có nghiệm trong rational numbers `\mathbb Q`, nhưng có hai nghiệm trong real numbers `\mathbb R`:

```math
x=\pm\sqrt2.
```

Tương tự,

```math
x^2=-1
```

không có nghiệm thực nhưng có nghiệm phức:

```math
x=\pm i.
```

Điều này nối trực tiếp equations với number các hệ thống (systems / 시스템들): mở rộng tập số thường xuất hiện vì một lớp (class / 클래스) equations trước đó chưa “đóng” dưới phép giải.

> **Nối mạch:** Trong **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **2. Equivalence transformations: vì sao các phép biến đổi hợp lệ?** nối từ **1. Solution set luôn phụ thuộc lĩnh vực (domain / 도메인)** sang **3. tuyến tính (linear / 선형) equations: solving là undo một affine transformation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Equivalence transformations: vì sao các phép biến đổi hợp lệ?

Giả sử

```math
A(x)=B(x).
```

Nếu ta cộng cùng một expression `C(x)` vào hai vế, ta được

```math
A(x)+C(x)=B(x)+C(x).
```

Phép biến đổi này reversible: trừ lại `C(x)` sẽ quay về equation ban đầu. Vì thế hai equations có cùng solution set.

Tương tự, nhân hai vế với một nonzero constant `k` cũng reversible:

```math
A=B
\iff
kA=kB,\qquad k\ne0.
```

Đây là bản chất của những câu quen thuộc như “chuyển vế đổi dấu”: không có thao tác (operation / 연산) đặc biệt tên là chuyển vế; ta chỉ đang cộng hoặc trừ cùng quantity ở hai phía.

### Khi phép biến đổi không reversible

Nếu từ

```math
x=1
```

bình phương hai vế, ta được

```math
x^2=1,
```

nhưng equation mới có thêm nghiệm `x=-1`. Vì squaring là many-to-one trên real numbers: `1` và `-1` cùng map tới `1`.

Do đó

```math
A=B \Rightarrow A^2=B^2
```

nhưng chiều ngược lại không luôn đúng.

Đây là lý do equations có square gốc (root / 루트), absolute giá trị (value / 값), rational expressions hoặc trigonometric transformations thường cần **substitute back** vào original ràng buộc (constraint / 제약조건).

> **Nối mạch:** Ở chặng này của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **3. tuyến tính (linear / 선형) equations: solving là undo một affine transformation** nối từ **2. Equivalence transformations: vì sao các phép biến đổi hợp lệ?** sang **4. Hệ phương trình: intersection của các ràng buộc (constraints / 제약조건들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. tuyến tính (linear / 선형) equations: solving là undo một affine transformation

Phương trình

```math
ax+b=c,\qquad a\ne0
```

có thể hiểu như một hàm (function / 함수)

```math
f(x)=ax+b
```

và câu hỏi là tìm preimage của `c` dưới `f`.

Ta undo translation trước:

```math
ax=c-b,
```

rồi undo scaling:

```math
x=\frac{c-b}{a}.
```

Cách nhìn này nối equations với inverse functions. Solving tuyến tính (linear / 선형) equation là áp dụng inverse của affine map.

### Worked example

Giải

```math
3(2x-1)+4=19.
```

Khai triển không phải lúc nào cũng là bước đầu bắt buộc, nhưng ở đây giúp thấy cấu trúc (structure / 구조):

```math
6x-3+4=19
```

```math
6x+1=19
```

```math
6x=18
```

```math
x=3.
```

Mỗi bước đều equivalence-preserving.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **4. Hệ phương trình: intersection của các ràng buộc (constraints / 제약조건들)** nối từ **3. tuyến tính (linear / 선형) equations: solving là undo một affine transformation** sang **5. Quadratic equations: vì sao có nhiều representations?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Hệ phương trình: intersection của các ràng buộc (constraints / 제약조건들)

Hệ thống (system / 시스템)

```math
\begin{cases}
x+y=10\\
x-y=2
\end{cases}
```

không phải hai bài riêng. Solution phải thỏa **cả hai** các ràng buộc (constraints / 제약조건들).

Cộng equations:

```math
2x=12
```

nên

```math
x=6,
```

rồi

```math
y=4.
```

Geometrically, mỗi equation trong hai variables là một line; solution là intersection. Hai lines có thể:

- cắt nhau tại một điểm → unique solution;
- song song → no solution;
- trùng nhau → infinitely many solutions.

Tuyến tính (linear / 선형) algebra tổng quát hóa cùng idea này thành

```math
Ax=b.
```

Rank, column không gian (space / 공간) và null không gian (space / 공간) sau này chỉ là ngôn ngữ có hệ thống hơn để mô tả consistency và degrees of freedom.

> **Nối mạch:** Trong **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **5. Quadratic equations: vì sao có nhiều representations?** nối từ **4. Hệ phương trình: intersection của các ràng buộc (constraints / 제약조건들)** sang **6. Discriminant là thông tin hình học**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Quadratic equations: vì sao có nhiều representations?

Quadratic

```math
ax^2+bx+c=0,\qquad a\ne0
```

có thể được viết ở nhiều forms vì mỗi biểu diễn (representation / 표현) làm lộ một cấu trúc (structure / 구조) khác.

Expanded form:

```math
ax^2+bx+c
```

làm coefficients rõ.

Factored form:

```math
a(x-r_1)(x-r_2)
```

làm roots rõ.

Vertex form:

```math
a(x-h)^2+k
```

làm hình học (geometry / 기하학) rõ.

### Derive quadratic formula từ completing the square

Bắt đầu:

```math
ax^2+bx+c=0.
```

Chia cho `a`:

```math
x^2+\frac ba x+\frac ca=0.
```

Chuyển constant:

```math
x^2+\frac ba x=-\frac ca.
```

Thêm bình phương nửa coefficient của `x` vào hai phía:

```math
x^2+\frac ba x+\frac{b^2}{4a^2}
=
\frac{b^2-4ac}{4a^2}.
```

Vế trái trở thành perfect square:

```math
\left(x+\frac{b}{2a}\right)^2
=
\frac{b^2-4ac}{4a^2}.
```

Lấy square gốc (root / 루트):

```math
x+\frac{b}{2a}
=
\pm\frac{\sqrt{b^2-4ac}}{2a},
```

nên

```math
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
```

Quadratic formula không phải quy tắc (rule / 규칙) rơi từ trên xuống; nó là completing-the-square được đóng gói.

> **Nối mạch:** Ở chặng này của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **6. Discriminant là thông tin hình học** nối từ **5. Quadratic equations: vì sao có nhiều representations?** sang **7. Absolute giá trị (value / 값): distance trước trường hợp (case / 사례) splitting**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Discriminant là thông tin hình học

Discriminant không chỉ quyết định phương trình bậc hai có bao nhiêu nghiệm thực. Nó còn nói đường cong cắt trục như thế nào, nên nối đại số với hình học và giúp kiểm tra nghiệm trước khi tính tiếp.

```math
\Delta=b^2-4ac
```

quyết định số real intersections giữa parabola và x-axis.

- `\Delta>0`: hai real roots;
- `\Delta=0`: tangent vào trục, một gốc (root / 루트) kép;
- `\Delta<0`: không cắt x-axis trong real plane.

Trong complex numbers, vẫn có hai roots tính theo multiplicity.

Discriminant vì vậy nối algebra với hình học (geometry / 기하학) và complex number các hệ thống (systems / 시스템들).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **6. Discriminant là thông tin hình học** nêu quy tắc; **7. Absolute giá trị (value / 값): distance trước trường hợp (case / 사례) splitting** thử quy tắc trong tình huống, rồi **8. Rational equations và lĩnh vực (domain / 도메인) restrictions** mở rộng hệ quả.

## 7. Absolute giá trị (value / 값): distance trước trường hợp (case / 사례) splitting

Absolute giá trị (value / 값) nên được hiểu trước hết là distance.

```math
|x-c|=r
```

nghĩa distance từ `x` tới `c` bằng `r`. Nếu `r>0`, có hai points:

```math
x=c-r
```

và

```math
x=c+r.
```

Còn

```math
|x-c|<r
```

nghĩa `x` nằm **bên trong** interval bán kính `r` quanh `c`:

```math
c-r<x<c+r.
```

Trong khi

```math
|x-c|>r
```

nghĩa nằm bên ngoài interval đó.

Cách hiểu distance làm absolute-value inequalities trở nên tự nhiên hơn việc học thuộc cases.

> **Nối mạch:** Trong **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **7. Absolute giá trị (value / 값): distance trước trường hợp (case / 사례) splitting** nêu quy tắc; **8. Rational equations và lĩnh vực (domain / 도메인) restrictions** thử quy tắc trong tình huống, rồi **9. Inequalities: thứ tự (order / 순서) cấu trúc (structure / 구조) khác equality ở đâu?** mở rộng hệ quả.

## 8. Rational equations và lĩnh vực (domain / 도메인) restrictions

Ví dụ

```math
\frac{1}{x-1}=2.
```

Trước khi solve phải ghi nhận

```math
x\ne1.
```

Nhân hai phía bởi `x-1` chỉ hợp lệ trên lĩnh vực (domain / 도메인) nơi denominator khác zero:

```math
1=2(x-1)
```

```math
x=\frac32.
```

Candidate này hợp lệ vì không vi phạm restriction.

Trong rational equations, lĩnh vực (domain / 도메인) restriction không phải ghi chú phụ; nó là part of the bài toán (problem / 문제) definition.

> **Nối mạch:** Ở chặng này của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **9. Inequalities: thứ tự (order / 순서) cấu trúc (structure / 구조) khác equality ở đâu?** nối từ **8. Rational equations và lĩnh vực (domain / 도메인) restrictions** sang **10. Polynomial inequalities: sign chart đến từ factors**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Inequalities: thứ tự (order / 순서) cấu trúc (structure / 구조) khác equality ở đâu?

Nếu

```math
a<b,
```

thêm cùng `c` vào hai phía giữ thứ tự (order / 순서):

```math
a+c<b+c.
```

Nhân với positive `k` cũng giữ thứ tự (order / 순서). Nhưng nếu `k<0`, direction đảo:

```math
ka>kb.
```

Tại sao? Multiplication by a negative number phản chiếu number line qua 0. Reflection đổi left ↔ right, nên thứ tự đảo.

### Worked example

Giải

```math
-3x+5\le14.
```

Trừ 5:

```math
-3x\le9.
```

Chia cho `-3`, đảo inequality:

```math
x\ge-3.
```

Solution set:

```math
[-3,\infty).
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **10. Polynomial inequalities: sign chart đến từ factors** nối từ **9. Inequalities: thứ tự (order / 순서) cấu trúc (structure / 구조) khác equality ở đâu?** sang **11. các ràng buộc (constraints / 제약조건들) trong tối ưu hóa (optimization / 최적화), physics và software**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Polynomial inequalities: sign chart đến từ factors

Giải

```math
(x-1)(x+2)>0.
```

Trọng yếu (critical / 중요) points là roots `-2` và `1`. Chúng chia number line thành ba intervals:

```text
(-∞,-2), (-2,1), (1,∞)
```

Sản phẩm (product / 제품) positive khi hai factors cùng sign. Do đó solution là

```math
(-\infty,-2)\cup(1,\infty).
```

Sign chart không phải trick riêng; nó là lập luận (reasoning / 추론) từ multiplicative signs và roots.

> **Nối mạch:** Trong **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **11. các ràng buộc (constraints / 제약조건들) trong tối ưu hóa (optimization / 최적화), physics và software** nối từ **10. Polynomial inequalities: sign chart đến từ factors** sang **12. Proof idea: vì sao solution-preserving transformations quan trọng?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. các ràng buộc (constraints / 제약조건들) trong tối ưu hóa (optimization / 최적화), physics và software

Inequalities là ngôn ngữ (language / 언어) của feasible regions:

```math
x_i\ge0,
```

```math
cost(x)\le budget,
```

```math
latency\le200\text{ ms}.
```

Trong tuyến tính (linear / 선형) programming, mỗi tuyến tính (linear / 선형) inequality tạo một half-space. Intersection của các half-spaces là feasible set.

Trong physics, các ràng buộc (constraints / 제약조건들) có thể đến từ conservation laws hoặc vật lý (physical / 물리적) bounds. Trong software, kiểm tra hợp lệ (validation / 검증) rules cũng là predicates xác định allowed trạng thái (state / 상태).

Điểm chung là: equations/inequalities không chỉ là bài solve `x`; chúng là ngôn ngữ mô tả **trạng thái (state / 상태) nào được phép tồn tại**.

> **Nối mạch:** Ở chặng này của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **12. Proof idea: vì sao solution-preserving transformations quan trọng?** nối từ **11. các ràng buộc (constraints / 제약조건들) trong tối ưu hóa (optimization / 최적화), physics và software** sang **Applications và connections**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Proof idea: vì sao solution-preserving transformations quan trọng?

Khi solving, ta muốn xây chuỗi (chain / 사슬)

```math
E_0\iff E_1\iff E_2\iff\cdots\iff E_k.
```

Nếu mỗi arrow là equivalence, mọi stage có cùng solution set.

Nếu một bước chỉ có

```math
E_i\Rightarrow E_{i+1},
```

thì `E_{i+1}` có thể có extra solutions. Khi đó final answers chỉ là candidates và phải check lại original equation.

Đây là proof-theoretic viewpoint của algebraic manipulation: mỗi step cần biết logical strength của transformation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **Applications và connections** nối từ **12. Proof idea: vì sao solution-preserving transformations quan trọng?** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Applications và connections

**Khoa học máy tính (computer science / 컴퓨터 과학):** ràng buộc (constraint / 제약조건) solvers, kiểu (type / 타입) các ràng buộc (constraints / 제약조건들), SAT/SMT lập luận (reasoning / 추론) và kiểm tra hợp lệ (validation / 검증) các hệ thống (systems / 시스템들) đều mở rộng idea “tìm assignments làm predicates đúng”.

**Physics:** equations of motion và conservation equations xác định states/trajectories hợp lệ.

**AI:** tối ưu hóa (optimization / 최적화) huấn luyện (training / 학습) là solve inequalities/equalities gián tiếp qua objectives và các ràng buộc (constraints / 제약조건들).

**Finance:** ngân sách (budget / 예산), leverage, regulatory capital và no-arbitrage relationships đều được viết dưới dạng equations/inequalities.

> **Nối mạch:** Trong **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Applications và connections** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Equation và inequality là descriptions của feasible states. Solving là thay biểu diễn (representation / 표현) của ràng buộc (constraint / 제약조건) bằng representations dễ đọc hơn trong khi theo dõi chính xác solution set. Algebra tốt không phải thao tác ký hiệu nhanh; nó là logic-preserving transformation.

> **Nối mạch:** Ở chặng này của **Phương trình và bất phương trình: ràng buộc (constraint / 제약조건), equivalence và miền nghiệm**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“Chuyển vế” là một phép toán đặc biệt.** Không; đó là shorthand cho cộng/trừ cùng quantity ở hai phía.

**Bình phương hai vế luôn equivalent.** Không; squaring có thể mất sign thông tin (information / 정보) và tạo extraneous solutions.

**Một equation có nghiệm mà không cần lĩnh vực (domain / 도메인).** Không; solution set phụ thuộc number hệ thống (system / 시스템) và restrictions.

**`f'(x)=0` hay `\Delta=0` tự nó là một mẹo riêng.** Những conditions này đều encode hình học (geometry / 기하학)/cấu trúc (structure / 구조) cụ thể; hiểu cấu trúc (structure / 구조) giúp tránh học thuộc rời rạc.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
