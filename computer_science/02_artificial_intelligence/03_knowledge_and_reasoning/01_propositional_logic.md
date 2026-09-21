# Logic mệnh đề cho Trí tuệ nhân tạo

**Logic mệnh đề (Propositional Logic / 명제 논리)** là một ngôn ngữ hình thức để biểu diễn các phát biểu có giá trị đúng/sai và suy luận từ chúng bằng các quy tắc chính xác. Nó đơn giản hơn Logic vị từ bậc nhất nhưng rất quan trọng vì cung cấp bộ từ vựng nền về cú pháp, ngữ nghĩa, quan hệ kéo theo, chứng minh, tính thỏa mãn và kiểm tra mô hình.

Trong AI, Logic mệnh đề xuất hiện trong hệ thống luật, bộ giải SAT, mã hóa bài toán lập kế hoạch, kiểm chứng và suy luận ràng buộc. Mục tiêu không phải biến mọi tri thức thành `P ∧ Q`, mà là hiểu **suy luận hình thức (formal reasoning)** khác với nhận dạng mẫu thống kê ở đâu.

Xem trước: [Biểu diễn tri thức](./00_knowledge_representation.md).

## Mệnh đề

Một **mệnh đề (proposition)** là một phát biểu có thể đúng hoặc sai.

Ví dụ:

```text
P: Trời đang mưa.
Q: Mặt đường ướt.
```

Không phải mệnh đề:

```text
"Hãy đóng cửa!"      → mệnh lệnh
"Mấy giờ rồi?"       → câu hỏi (question)
x > 3                 → công thức mở cho tới khi x được gán hoặc lượng hóa
```

Logic mệnh đề xem `P` như một ký hiệu nguyên tử; nó không nhìn vào cấu trúc bên trong của khái niệm “đang mưa”.

## Các phép nối logic

| Ký hiệu | Thuật ngữ | Ý nghĩa |
|---|---|---|
| `¬P` | phủ định (NOT) | không P |
| `P ∧ Q` | hội (AND) | P và Q |
| `P ∨ Q` | tuyển (OR) | P hoặc Q theo nghĩa bao hàm |
| `P → Q` | kéo theo (implication) | nếu P thì Q |
| `P ↔ Q` | tương đương hai chiều (biconditional) | P khi và chỉ khi Q |

`∨` mặc định là “hoặc bao hàm”: đúng khi một hoặc cả hai vế đúng.

## Bảng chân trị

Phép kéo theo thường gây nhầm lẫn:

| P | Q | `P → Q` |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

Vì sao `P→Q` lại đúng khi P sai?

Bởi vì:

\[
P\rightarrow Q\equiv\neg P\lor Q
\]

Nó chỉ cấm trường hợp P đúng nhưng Q sai.

Từ “nếu” trong ngôn ngữ tự nhiên đôi khi còn mang nghĩa nhân quả hoặc thời gian, những nghĩa này không tự động được chứa trong phép kéo theo vật chất của logic.

## Cú pháp và ngữ nghĩa

**Cú pháp (syntax)** định nghĩa công thức nào được viết hợp lệ.

Ví dụ:

\[
(P\land Q)\rightarrow R
\]

**Ngữ nghĩa (semantics)** định nghĩa khi nào công thức đúng dưới một cách diễn giải hoặc mô hình gán giá trị chân trị cho các ký hiệu.

Sự phân biệt này rất quan trọng:

```text
cú pháp  = cấu trúc biểu thức
ngữ nghĩa = điều kiện làm biểu thức đúng hoặc sai
```

LLM có thể sinh ra công thức trông đúng cú pháp nhưng ánh xạ công thức đó sang miền thực tế vẫn có thể sai về ngữ nghĩa.

## Mô hình trong logic

Một **mô hình (model)** ở đây là phép gán giá trị đúng/sai cho các mệnh đề.

Nếu:

```text
P=true
Q=false
```

thì mô hình đó thỏa `P∨Q` nhưng không thỏa `P∧Q`.

Ký hiệu:

\[
M\models\alpha
\]

nghĩa là mô hình `M` thỏa công thức `α`.

## Có thể thỏa, hằng đúng và mâu thuẫn

Một công thức **có thể thỏa (satisfiable)** nếu tồn tại ít nhất một mô hình làm nó đúng.

Một công thức **hằng đúng (valid/tautology)** nếu mọi mô hình đều làm nó đúng.

Ví dụ:

\[
P\lor\neg P
\]

luôn đúng.

Một công thức **không thể thỏa (unsatisfiable/contradiction)** nếu không có mô hình nào làm nó đúng:

\[
P\land\neg P
\]

Ba khái niệm này là nền của SAT và chứng minh phản chứng.

## Quan hệ kéo theo

Cơ sở tri thức `KB` **kéo theo (entails)** `α`:

\[
KB\models\alpha
\]

nếu mọi mô hình thỏa `KB` cũng thỏa `α`.

Điểm quan trọng:

> Quan hệ kéo theo là tất yếu về ngữ nghĩa, không phải chỉ vì `α` “nghe có vẻ hợp lý”.

Ví dụ:

\[
KB=\{P\rightarrow Q, P\}
\]

thì:

\[
KB\models Q
\]

## Suy diễn

Một thủ tục suy diễn dẫn xuất công thức bằng thao tác cú pháp:

\[
KB\vdash\alpha
\]

Cần phân biệt:

```text
⊨ quan hệ kéo theo về ngữ nghĩa
⊢ khả năng dẫn xuất / chứng minh bằng cú pháp
```

Một hệ chứng minh **đúng đắn (sound)** nếu chỉ dẫn xuất những kết luận thật sự được kéo theo.

Nó **đầy đủ (complete)** nếu mọi kết luận được kéo theo về nguyên tắc đều có thể được dẫn xuất.

Các thuật ngữ này nói về hệ chứng minh, không phải độ chính xác của mô hình học máy.

## Modus Ponens

Quy tắc:

\[
P,\quad P\rightarrow Q
\]

suy ra:

\[
Q
\]

Ví dụ:

```text
ServerDown → Alert
ServerDown
∴ Alert
```

Quy tắc hợp lệ независимо với ý nghĩa miền của các ký hiệu.

## Modus Tollens

\[
P\rightarrow Q,\quad \neg Q
\]

suy ra:

\[
\neg P
\]

Nhưng **khẳng định hệ quả (affirming the consequent)** là sai:

\[
P\rightarrow Q,\quad Q
\]

không cho phép suy ra `P`, vì Q có thể có nguyên nhân khác.

## Các tương đương logic

Phủ định kép:

\[
\neg\neg P\equiv P
\]

Luật De Morgan:

\[
\neg(P\land Q)\equiv \neg P\lor\neg Q
\]

\[
\neg(P\lor Q)\equiv \neg P\land\neg Q
\]

Khử phép kéo theo:

\[
P\rightarrow Q\equiv\neg P\lor Q
\]

Tương đương hai chiều:

\[
P\leftrightarrow Q
\equiv
(P\rightarrow Q)\land(Q\rightarrow P)
\]

Các phép biến đổi này rất quan trọng khi chuyển công thức sang dạng chuẩn.

## Các dạng chuẩn

### Dạng chuẩn hội

**Dạng chuẩn hội (Conjunctive Normal Form - CNF)** là phép hội của nhiều mệnh đề, mỗi mệnh đề là phép tuyển của các literal.

\[
(A\lor\neg B)\land(C\lor D)\land(\neg A\lor E)
\]

Bộ giải SAT thường làm việc trên CNF.

### Dạng chuẩn tuyển

**Dạng chuẩn tuyển (Disjunctive Normal Form - DNF)** là phép tuyển của các nhóm hội.

\[
(A\land B)\lor(\neg A\land C)
\]

Mọi công thức mệnh đề đều có thể biểu diễn bằng CNF hoặc DNF, nhưng chuyển đổi ngây thơ có thể gây bùng nổ kích thước theo cấp số nhân. **Biến đổi Tseitin (Tseitin transformation)** thêm biến phụ để tạo CNF tương đương về tính thỏa mãn với kích thước tăng tuyến tính.

## Literal và mệnh đề tuyển

Một **literal** là mệnh đề nguyên tử hoặc phủ định của nó:

```text
P
¬Q
```

Một mệnh đề tuyển (clause):

\[
P\lor\neg Q\lor R
\]

Công thức CNF là tập hoặc phép hội của các clause.

SAT khai thác cấu trúc này rất mạnh.

## Phép phân giải

**Phép phân giải (resolution)**:

\[
(P\lor A),\quad(\neg P\lor B)
\]

suy ra:

\[
A\lor B
\]

Nếu lặp phép phân giải và dẫn tới mệnh đề rỗng `□`, ta đã tìm được mâu thuẫn.

Để chứng minh `KB⊨α`, có thể thêm `¬α` vào KB rồi chứng minh tập mới không thể thỏa.

## Chứng minh bằng phản chứng

Muốn chứng minh `Q` từ:

```text
P
P → Q
```

Chuyển phép kéo theo:

\[
\neg P\lor Q
\]

Thêm `¬Q`.

Phân giải `¬P∨Q` với `¬Q` → `¬P`.

Phân giải `¬P` với `P` → mệnh đề rỗng.

Do tập giả định cộng `¬Q` mâu thuẫn, nên Q được kéo theo.

## Mệnh đề Horn

**Mệnh đề Horn (Horn clause)** có tối đa một literal dương.

Ví dụ:

\[
\neg P\lor\neg Q\lor R
\]

 tương ứng:

\[
P\land Q\rightarrow R
\]

Logic Horn hỗ trợ suy diễn tiến/lùi hiệu quả và là nền của nhiều hệ thống luật cũng như các mảnh của lập trình logic.

## Suy diễn tiến

**Suy diễn tiến (forward chaining)** bắt đầu từ các sự kiện đã biết và liên tục kích hoạt những quy tắc có tiền đề đã thỏa.

```text
Sự kiện: A, B
Quy tắc:
A ∧ B → C
C → D
```

Suy ra C, sau đó D.

Forward chaining là cách suy luận **hướng dữ liệu (data-driven)**.

Nó hữu ích khi có nhiều kết luận có thể cần hoặc sự kiện đến theo dòng.

## Suy diễn lùi

**Suy diễn lùi (backward chaining)** bắt đầu từ truy vấn hoặc mục tiêu rồi hỏi cần những tiền đề nào để chứng minh nó.

Muốn chứng minh `D`:

```text
Cần C
Muốn có C cần A và B
Kiểm tra A,B có trong tập sự kiện
```

Đây là suy luận **hướng mục tiêu (goal-driven)**.

Suy luận kiểu Prolog dùng backward chaining kết hợp hợp nhất ở mức Logic vị từ bậc nhất.

## Bài toán SAT

SAT hỏi:

> Có tồn tại phép gán Boolean cho các biến để công thức trở thành đúng không?

SAT là NP-complete, nhưng bộ giải hiện đại vẫn xử lý hiệu quả nhiều bài toán lớn có cấu trúc.

Ứng dụng gồm:

- kiểm chứng phần cứng;
- lập kế hoạch;
- lập lịch và cấu hình;
- giải phụ thuộc;
- chứng minh định lý;
- phân tích phần mềm.

## DPLL

DPLL mở rộng quay lui SAT bằng:

- lan truyền đơn vị;
- loại literal thuần;
- phân nhánh.

Các bộ giải CDCL hiện đại phát triển từ nền tảng liên quan này bằng học mệnh đề từ xung đột và quay lui không theo thứ tự thời gian.

## Lan truyền đơn vị

Mệnh đề:

\[
A\lor B\lor C
\]

Nếu `A=false` và `B=false` thì `C=true` bị bắt buộc.

Hãy lan truyền mọi phép gán bắt buộc trước khi phân nhánh.

Đây chính là nguyên lý “suy luận trước khi tìm kiếm” đã gặp trong CSP.

## Học mệnh đề từ xung đột

Khi một phép gán gây mâu thuẫn, bộ giải phân tích đồ thị suy diễn và học mệnh đề mới để tránh lặp lại cùng nguyên nhân xung đột. Cơ chế này gọi là **Conflict-Driven Clause Learning (CDCL)**.

Vòng lặp khái niệm:

```text
lan truyền
  ↓
phân nhánh
  ↓
có xung đột?
  ├─ không → tiếp tục
  └─ có → phân tích → học mệnh đề → quay lui xa
```

Mệnh đề học được vẫn là hệ quả logic, nên bộ giải trở nên hiệu quả hơn mà không đánh đổi tính đúng.

## Tính nhất quán của cơ sở tri thức

Nếu KB chứa:

\[
P
\]

và:

\[
\neg P
\]

thì cơ sở tri thức mâu thuẫn trong logic cổ điển.

Theo nguyên lý bùng nổ, từ mâu thuẫn có thể dẫn xuất bất kỳ công thức nào trong logic cổ điển.

Cơ sở tri thức thực tế có thể chứa xung đột, từ đó cần logic cận nhất quán, suy luận có xét nguồn gốc hoặc chính sách xử lý xung đột tường minh.

## Suy luận theo thế giới đóng

Bản thân Logic mệnh đề không nói rằng sự kiện không xuất hiện thì là sai. Giả định thế giới đóng là một chính sách ngữ nghĩa bổ sung.

Bộ máy luật có thể dùng **phủ định do thất bại (negation as failure)**:

```text
nếu không chứng minh được P, tạm xem P là sai
```

Điều này khác với phủ định logic cổ điển.

Nhầm hai khái niệm có thể tạo lỗi suy luận tinh vi.

## Logic và điều kiện trong phần mềm

Logic Boolean nằm bên dưới điều kiện chương trình:

```java
if (authenticated && !locked) {
    allow();
}
```

Tuy nhiên trạng thái chương trình, thời gian và tác dụng phụ khiến ngữ nghĩa phần mềm phong phú hơn công thức mệnh đề.

Kiểm chứng hình thức thường chuyển các thuộc tính chương trình sang ràng buộc SAT/SMT.

## SAT và SMT

SAT chỉ dùng biến Boolean.

**SMT (Satisfiability Modulo Theories)** bổ sung các lý thuyết như:

- số nguyên và số thực;
- mảng;
- bit-vector;
- chuỗi;
- hàm chưa diễn giải.

Ví dụ:

\[
x>3\land y=x+2\land y<4
\]

cần lý thuyết số học, không chỉ các biến Boolean nguyên tử trừ khi được mã hóa lại.

SMT rất quan trọng trong kiểm chứng chương trình và tác nhân dựa trên bộ giải.

## Logic và xác suất

Logic cổ điển:

```text
P đúng hoặc sai
```

Xác suất:

```text
P(P)=0.7
```

Logic mô tả cấu trúc chắc chắn; xác suất mô tả bất định.

Quy tắc `Smoke→Fire` trong logic nghiêm ngặt có nghĩa mọi trường hợp có khói đều có cháy. Quan hệ ngoài đời thường chỉ mang tính xác suất, nên ép nó thành phép kéo theo tuyệt đối là mô hình hóa sai.

Biểu diễn phải phù hợp với ngữ nghĩa của miền.

## Logic và suy luận bằng LLM

LLM có thể tạo chuỗi suy luận hợp logic, nhưng cơ chế dự đoán token tiếp theo không bảo đảm chứng minh đúng đắn.

Kiến trúc lai:

```text
LLM đề xuất định lý / bước chứng minh
        ↓
bộ máy logic hình thức kiểm tra tính hợp lệ
        ↓
chấp nhận / từ chối / sửa chữa
```

Cách này kết hợp suy luận ngôn ngữ linh hoạt với xác minh ký hiệu.

## Lập kế hoạch dưới dạng SAT

Lập kế hoạch có chân trời giới hạn có thể tạo các biến Boolean:

```text
ActionA_t
AtRobotRoom1_t
AtRobotRoom2_t
```

Ràng buộc mã hóa điều kiện trước, hiệu ứng và điều kiện duy nhất.

Một phép gán thỏa SAT tương ứng với một kế hoạch.

Đây là ví dụ của **quy giản biểu diễn**: biến bài toán lập kế hoạch thành bài toán thỏa mãn.

## Mô hình tư duy (mental model)

```text
Mệnh đề         = phát biểu nguyên tử đúng/sai
Công thức       = kết hợp mệnh đề bằng phép nối logic
Mô hình         = phép gán làm công thức đúng/sai
Kéo theo        = đúng trong mọi mô hình của KB
Chứng minh      = dẫn xuất bằng cú pháp
SAT             = có tồn tại ít nhất một mô hình không?
Phân giải       = quy tắc suy diễn cơ học trên clause
Suy diễn tiến   = sự kiện → hệ quả
Suy diễn lùi    = mục tiêu → tiền đề cần thiết
```

## Các hiểu lầm thường gặp

### “P→Q nghĩa là P gây ra Q”

Phép kéo theo vật chất mã hóa điều kiện chân trị, không phải quan hệ nhân quả.

### “Nếu Q đúng và P→Q thì P phải đúng”

Đây là lỗi khẳng định hệ quả.

### “Không biết nghĩa là sai”

Chỉ đúng nếu có giả định thế giới đóng hoặc chính sách phủ định do thất bại tường minh.

### “SAT là NP-complete nên bộ giải thực tế không dùng được”

Độ khó trường hợp xấu không ngăn bộ giải xử lý hiệu quả nhiều bài toán có cấu trúc quy mô lớn.

## Liên kết kiến thức

Logic mệnh đề nối Biểu diễn tri thức với CSP/SAT, lập kế hoạch và kiểm chứng hình thức. Nó cung cấp sự phân biệt ngữ nghĩa–cú pháp cần thiết trước khi học Logic vị từ bậc nhất và tạo đường cơ sở để hiểu vì sao suy luận xác suất và suy luận nơ-ron đưa ra các đánh đổi khác.

Xem tiếp: [Logic vị từ bậc nhất](./02_first_order_logic.md) và [Suy diễn và suy luận](./03_inference_and_reasoning.md).