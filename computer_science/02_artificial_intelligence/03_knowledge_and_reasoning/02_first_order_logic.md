# Logic vị từ bậc nhất cho Trí tuệ nhân tạo

Logic mệnh đề (Propositional Logic) có thể biểu diễn các mệnh đề như `Rain` hay `WetRoad`, nhưng không biểu diễn tự nhiên những câu như “mọi người”, “một người nào đó”, “Alice là cha/mẹ của Bob” hay “mọi bác sĩ đều là người làm chuyên môn”. **Logic vị từ bậc nhất (First-Order Logic - FOL / 일차 논리)** mở rộng logic mệnh đề bằng đối tượng, vị từ, hàm, biến và lượng từ.

FOL quan trọng trong biểu diễn tri thức (Knowledge Representation) vì nó mô tả được **cấu trúc quan hệ bên trong một mệnh đề** thay vì xem cả câu như một ký hiệu nguyên tử. Nó là nền tảng của lập trình logic (logic programming), chứng minh định lý (theorem proving), ontology và các đặc tả hình thức (formal specifications).

Xem trước: [Logic mệnh đề](./01_propositional_logic.md).

## Vì sao Logic mệnh đề chưa đủ?

Giả sử miền bài toán có 10.000 người và ta có quy tắc:

> Mọi con người đều phải chết.

Nếu dùng Logic mệnh đề, ta có thể phải viết hàng nghìn luật riêng:

```text
Human_Alice → Mortal_Alice
Human_Bob → Mortal_Bob
...
```

FOL chỉ cần một mệnh đề:

\[
\forall x\; Human(x)\rightarrow Mortal(x)
\]

Cấu trúc `Human(x)` và biến `x` cho phép khái quát hóa (generalization) trên toàn bộ các đối tượng trong miền.

## Từ vựng của FOL

Một ngôn ngữ FOL thường gồm các thành phần sau:

- **hằng (constant)**: `Alice`, `Seoul`, `42`;
- **biến (variable)**: `x`, `y`;
- **vị từ (predicate)**: `Human(x)`, `LivesIn(x,y)`;
- **hàm (function)**: `MotherOf(x)`;
- **toán tử logic (logical connective)**: `¬, ∧, ∨, →, ↔`;
- **lượng từ (quantifier)**: `∀, ∃`.

## Term và công thức

Một **term** là biểu thức dùng để chỉ một đối tượng:

```text
Alice
x
MotherOf(Alice)
```

Một **công thức nguyên tử (atomic formula)** áp dụng một vị từ lên các term:

\[
LivesIn(Alice,Seoul)
\]

Các công thức phức tạp được tạo bằng cách kết hợp nhiều công thức nguyên tử với toán tử logic và lượng từ.

## Lượng từ toàn thể

\[
\forall x\; Human(x)\rightarrow Mortal(x)
\]

có nghĩa là với mọi đối tượng `x`, nếu `x` là con người thì `x` phải chết.

Điểm quan trọng là dạng biểu diễn này sử dụng phép kéo theo (implication), không phải phép hội đơn thuần. Ví dụ:

\[
\forall x\; Human(x)\land Mortal(x)
\]

không có nghĩa “mọi người đều phải chết”; nó khẳng định rằng **mọi đối tượng trong miền đều vừa là người vừa phải chết**, đây là một phát biểu mạnh hơn rất nhiều và thường sai với ý định ban đầu.

## Lượng từ tồn tại

\[
\exists x\; Human(x)\land LivesIn(x,Seoul)
\]

có nghĩa là tồn tại ít nhất một đối tượng vừa là con người vừa sống ở Seoul.

Với lượng từ tồn tại, phép hội thường được dùng để mô tả các thuộc tính mà đối tượng làm chứng (witness) phải thỏa mãn.

## Phạm vi của lượng từ

So sánh hai công thức:

\[
\forall x\exists y\; Loves(x,y)
\]

Công thức này có nghĩa: mỗi người đều yêu một người nào đó, nhưng người được yêu có thể khác nhau với từng `x`.

Trong khi đó:

\[
\exists y\forall x\; Loves(x,y)
\]

có nghĩa: tồn tại một người duy nhất theo nghĩa lượng từ, và tất cả mọi người đều yêu người đó.

Thứ tự lượng từ thay đổi hoàn toàn ý nghĩa của phát biểu.

## Biến tự do và biến bị ràng buộc

Trong:

\[
\forall x\; Parent(x,y)
\]

`x` là **biến bị ràng buộc (bound variable)** bởi `∀`, còn `y` là **biến tự do (free variable)**.

Một **câu đóng (closed formula)** không còn biến tự do và có thể nhận giá trị đúng/sai dưới một diễn giải cụ thể. Công thức còn biến tự do thường hoạt động giống một truy vấn hoặc một thuộc tính cần kiểm tra hơn.

## Số lượng đối số của vị từ

Vị từ một ngôi:

\[
Doctor(x)
\]

Vị từ hai ngôi:

\[
WorksAt(x,c)
\]

Vị từ ba ngôi:

\[
Transferred(x,amount,account)
\]

Ý nghĩa của vị từ phụ thuộc vào vị trí các đối số. Trong hệ thống thực tế, schema hoặc kiểu dữ liệu rõ ràng giúp tránh những tổ hợp vô nghĩa.

## Hàm và quan hệ

Hàm ánh xạ đầu vào tới một đối tượng duy nhất:

\[
MotherOf(x)
\]

Trong khi quan hệ chỉ mô tả mối liên hệ giữa các đối tượng:

\[
Mother(m,x)
\]

Dùng hàm ngầm giả định tính duy nhất hoặc tính tồn tại của kết quả. Nếu tri thức miền không đảm bảo một giá trị xác định duy nhất, biểu diễn bằng quan hệ thường an toàn hơn.

## Phép bằng

FOL có phép bằng cho phép viết:

\[
x=y
\]

và suy luận về tính đồng nhất của đối tượng.

Một giả định thường gặp trong một số hệ thống là **giả định tên duy nhất (unique-name assumption)**: các tên khác nhau đại diện cho các đối tượng khác nhau. Tuy nhiên giả định này không tự động là một phần của ngữ nghĩa FOL chuẩn.

Trong Knowledge Graph, nhận diện hai tên có thật sự cùng chỉ một thực thể hay không là một vấn đề rất quan trọng.

## Diễn giải

Một mô hình FOL bao gồm:

- miền đối tượng `D`;
- ánh xạ từ hằng sang đối tượng;
- ánh xạ từ vị từ sang quan hệ trên `D`;
- ánh xạ từ hàm sang phép biến đổi trên `D`.

Giá trị đúng/sai của công thức phụ thuộc vào diễn giải này.

Ví dụ cú pháp `CapitalOf(Seoul,Korea)` tự nó không buộc hệ thống phải hiểu “thủ đô” theo nghĩa con người; chính diễn giải mới gán ý nghĩa cho quan hệ đó.

## Ví dụ chuyển ngôn ngữ tự nhiên sang FOL

“Every engineer uses some tool” có thể biểu diễn:

\[
\forall x\;(Engineer(x)\rightarrow \exists y\;(Tool(y)\land Uses(x,y)))
\]

Nghĩa là mỗi kỹ sư có thể dùng một công cụ khác nhau.

“There is a tool every engineer uses” có thể biểu diễn:

\[
\exists y\;(Tool(y)\land\forall x\;(Engineer(x)\rightarrow Uses(x,y)))
\]

Nghĩa là tồn tại một công cụ mà tất cả kỹ sư đều dùng.

Hai câu nhìn giống nhau về từ vựng nhưng khác hoàn toàn về cấu trúc lượng từ.

## Phủ định lượng từ

Các quy tắc tương tự De Morgan áp dụng cho lượng từ:

\[
\neg\forall x\;P(x)\equiv\exists x\;\neg P(x)
\]

“Không phải ai cũng vượt qua” tương đương “có ít nhất một người không vượt qua”.

\[
\neg\exists x\;P(x)\equiv\forall x\;\neg P(x)
\]

“Không có ai vượt qua” tương đương “mọi người đều không vượt qua”.

Ngôn ngữ tự nhiên thường mơ hồ về phạm vi của lượng từ và phủ định, vì vậy việc hình thức hóa đúng không phải lúc nào cũng đơn giản.

## Thế biến toàn thể

Từ:

\[
\forall x\; Human(x)\rightarrow Mortal(x)
\]

thế `x=Socrates` ta được:

\[
Human(Socrates)\rightarrow Mortal(Socrates)
\]

Kết hợp với `Human(Socrates)`, quy tắc Modus Ponens cho phép suy ra `Mortal(Socrates)`.

## Thế biến tồn tại

Từ:

\[
\exists x\; Human(x)
\]

có thể giới thiệu một ký hiệu mới `k` đại diện cho một đối tượng làm chứng nào đó:

\[
Human(k)
\]

Không được tự ý giả định `k=Alice` nếu không có bằng chứng. Việc dùng một ký hiệu mới là điều quan trọng để giữ tính đúng đắn của phép suy luận.

## Phép thế

Một phép thế có thể viết:

\[
\theta=\{x/Alice, y/Bob\}
\]

Áp dụng lên:

\[
Parent(x,y)
\]

ta nhận được:

\[
Parent(Alice,Bob)
\]

Phép thế là cơ chế cốt lõi của hợp nhất (unification) và áp dụng quy tắc.

## Hợp nhất

**Hợp nhất (unification)** tìm một phép thế làm cho hai biểu thức trở nên giống nhau.

Ví dụ:

```text
Knows(x, Seoul)
Knows(Alice, y)
```

Bộ hợp nhất tổng quát nhất (most general unifier) là:

\[
\{x/Alice, y/Seoul\}
\]

Cơ chế này cho phép các quy tắc tổng quát khớp với các sự kiện cụ thể trong lập trình logic.

## Kiểm tra xuất hiện

Nếu cố hợp nhất:

```text
x = f(x)
```

thì trong FOL với term hữu hạn, phép hợp nhất phải thất bại vì nếu chấp nhận sẽ dẫn tới một cấu trúc đệ quy vô hạn.

**Kiểm tra xuất hiện (occurs check)** ngăn kiểu phép thế vòng lặp này.

## Modus Ponens tổng quát

Một quy tắc có dạng:

\[
P_1\land\cdots\land P_n\rightarrow Q
\]

Nếu các sự kiện hiện có khớp với các tiền đề thông qua phép thế `θ`, ta có thể suy ra `Qθ`.

Ví dụ:

```text
Parent(x,y) ∧ Parent(y,z) → Grandparent(x,z)
Parent(Alice,Bob)
Parent(Bob,Carol)
```

suy ra:

```text
Grandparent(Alice,Carol)
```

## Suy diễn tiến trong FOL

Suy diễn tiến (forward chaining) liên tục tìm những quy tắc có tiền đề khớp với tập sự kiện hiện tại, sau đó bổ sung kết luận mới.

Nếu ngôn ngữ cho phép hàm sinh vô hạn term mới, quá trình này có thể không dừng. Các ngôn ngữ như Datalog hạn chế tính biểu đạt để nhiều bài toán có không gian suy luận hữu hạn và dễ xử lý hơn.

## Suy diễn lùi

Với mục tiêu:

```text
Grandparent(Alice,Carol)?
```

hệ thống có thể khớp với kết luận của quy tắc:

```text
Grandparent(x,z)
```

rồi thay `x=Alice`, `z=Carol` và sinh ra hai mục tiêu con:

```text
Parent(Alice,y)
Parent(y,Carol)
```

Sau đó hệ thống tìm một `y` phù hợp trong tập sự kiện hoặc thông qua các quy tắc khác. Đây là nền tảng của truy vấn kiểu Prolog.

## Lập trình logic

Một chương trình Prolog có thể gồm các sự kiện và quy tắc:

```prolog
parent(alice, bob).
parent(bob, carol).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).
```

Truy vấn:

```prolog
?- grandparent(alice, carol).
```

Các mệnh đề mang tính khai báo (declarative), nhưng hành vi chạy thực tế còn phụ thuộc thứ tự quy tắc, thứ tự mục tiêu và chiến lược tìm kiếm. Vì vậy cần phân biệt ngữ nghĩa khai báo và ngữ nghĩa thực thi (operational semantics).

## Resolution trong FOL

Để áp dụng phép phân giải (resolution), công thức thường được chuyển dần về dạng mệnh đề thông qua các bước như:

1. loại bỏ phép kéo theo;
2. đẩy phủ định vào trong;
3. chuẩn hóa tên biến;
4. Skolem hóa lượng từ tồn tại;
5. bỏ lượng từ toàn thể trong ngữ cảnh mệnh đề;
6. chuyển sang CNF;
7. dùng resolution kết hợp với unification.

Skolem hóa bảo toàn tính khả thỏa (satisfiability), nhưng không phải lúc nào cũng giữ tương đương logic theo nghĩa đơn giản giữa hai công thức.

## Skolem hóa

Ví dụ:

\[
\forall x\exists y\; Loves(x,y)
\]

có thể thay đối tượng tồn tại bằng hàm Skolem:

\[
\forall x\; Loves(x,f(x))
\]

`f(x)` đại diện cho một đối tượng nào đó được yêu và có thể phụ thuộc vào `x`.

Nếu lượng từ tồn tại không nằm trong phạm vi của lượng từ toàn thể, một hằng Skolem mới có thể đủ.

## Tính quyết định được

SAT trong Logic mệnh đề là bài toán quyết định được vì số phép gán chân trị là hữu hạn.

Với FOL tổng quát, bài toán tính hợp lệ không có một thuật toán luôn dừng và trả lời đúng cho mọi công thức tùy ý. Vì vậy trong thực tế, các hệ biểu diễn tri thức thường giới hạn tính biểu đạt để đổi lấy khả năng suy luận khả thi.

## Description Logic

**Logic mô tả (Description Logic)** là họ logic bị giới hạn có chủ đích để hỗ trợ suy luận về khái niệm và quan hệ với các tính chất tốt hơn về tính quyết định được và độ phức tạp.

Ví dụ:

```text
Person
Doctor ⊑ MedicalProfessional
Doctor ⊓ Researcher
∃worksAt.Hospital
```

Logic mô tả là nền tảng của nhiều ngôn ngữ ontology như OWL.

Trong kỹ thuật biểu diễn tri thức, một hình thức đủ dùng và suy luận được đáng tin cậy thường có giá trị hơn một ngôn ngữ cực kỳ biểu đạt nhưng khó kiểm soát.

## Datalog

Datalog là một ngôn ngữ lập trình logic không cho phép tùy ý các hàm sinh cấu trúc vô hạn, thường làm việc với các sự kiện và quy tắc quan hệ hữu hạn.

Ví dụ:

```text
parent(x,y) ∧ parent(y,z) → grandparent(x,z)
```

Datalog tạo cầu nối giữa suy luận logic, cơ sở dữ liệu đệ quy và hệ quy tắc. SQL recursive CTE và một số ngôn ngữ truy vấn đồ thị có những điểm tương đồng về mặt tư duy.

## Quy tắc và cơ sở dữ liệu

Giả sử cơ sở dữ liệu có:

```text
Employee(Alice)
ManagerOf(Alice,Team1)
```

và một quy tắc:

```text
ManagerOf(x,t) → CanApprove(x,t)
```

lớp suy luận có thể sinh ra tri thức mới về quyền phê duyệt.

Tuy nhiên, khi các quy tắc liên quan tới bảo mật hoặc phân quyền, ngữ nghĩa phải được kiểm soát rất chặt vì một luật sai có thể gây leo thang đặc quyền.

## Hạn chế về thời gian

FOL cơ bản không có khái niệm thời gian tích hợp sẵn. Có thể thêm thời gian thành đối số:

\[
WorksAt(Alice,Company,t)
\]

hoặc ghi rõ một năm cụ thể:

\[
WorksAt(Alice,Company,2026)
\]

Logic thời gian (Temporal Logic) cung cấp thêm các toán tử như “luôn luôn”, “cuối cùng sẽ xảy ra”, “cho tới khi”. Trong lập kế hoạch, thời gian thường được mô hình hóa thông qua trạng thái và các bước chuyển.

## Situation Calculus và Event Calculus

AI cổ điển phát triển nhiều hình thức để mô tả hành động và sự thay đổi.

**Situation Calculus** biểu diễn một tình huống như lịch sử của các hành động và dùng các fluent để mô tả thuộc tính thay đổi theo tình huống.

**Event Calculus** tập trung vào sự kiện và khoảng thời gian mà một thuộc tính có hiệu lực.

Các hình thức này giải quyết một vấn đề kinh điển gọi là **frame problem**.

## Frame problem

Nếu robot chuyển một chiếc cốc từ A sang B, hệ thống cần suy ra rằng vị trí của cốc đã thay đổi, nhưng màu tường, số sê-ri của robot và hàng nghìn sự kiện không liên quan vẫn giữ nguyên.

Viết lại toàn bộ những điều “không thay đổi” sau mỗi hành động là bất khả thi. STRIPS giải quyết vấn đề theo hướng thực dụng bằng danh sách hiệu ứng thêm/xóa (add/delete lists).

## Ngoại lệ trong tri thức đời thường

Quy tắc:

\[
Bird(x)\rightarrow Flies(x)
\]

không đúng tuyệt đối vì chim cánh cụt là ngoại lệ.

Nếu dùng FOL cổ điển, mọi ngoại lệ phải được mô hình hóa rõ. Các hệ suy luận mặc định (default logic) hoặc suy luận phi đơn điệu (non-monotonic reasoning) cho phép diễn đạt dạng “chim thường biết bay trừ khi có bằng chứng ngoại lệ”.

Điều này cho thấy logic toán học nghiêm ngặt và suy luận đời thường không hoàn toàn giống nhau.

## Tri thức không đầy đủ

Nếu cơ sở tri thức không chứa:

```text
Owns(Alice,Car)
```

FOL không tự động suy ra:

```text
¬Owns(Alice,Car)
```

trừ khi hệ thống bổ sung giả định thế giới đóng (closed-world assumption) hoặc quy tắc tương đương.

Đây là điểm cần đặc biệt chú ý khi kết nối hệ suy luận logic với cơ sở dữ liệu.

## FOL và Knowledge Graph

Bộ ba:

```text
(Alice, worksAt, CompanyX)
```

có thể ánh xạ tự nhiên thành vị từ hai ngôi:

\[
WorksAt(Alice,CompanyX)
\]

Các tiên đề ontology có thể bổ sung thêm ngữ nghĩa hình thức.

Tuy nhiên, duyệt đồ thị (graph traversal) đơn thuần không đồng nghĩa với suy luận FOL đầy đủ. Khả năng suy luận phụ thuộc vào ngôn ngữ truy vấn và engine được sử dụng.

## FOL và Ngôn ngữ tự nhiên

Ngôn ngữ tự nhiên chứa lượng từ, phủ định, quan hệ và phạm vi nên FOL thường được dùng làm một dạng biểu diễn ngữ nghĩa.

Ví dụ câu:

> Every student read a book.

có thể được hiểu là mỗi sinh viên đọc ít nhất một cuốn sách, và mỗi người có thể đọc một cuốn khác nhau:

\[
\forall x(Student(x)\rightarrow\exists y(Book(y)\land Read(x,y)))
\]

Phân tích ngữ nghĩa (semantic parsing) cố chuyển ngôn ngữ tự nhiên thành biểu diễn logic hoặc cấu trúc, nhưng sự mơ hồ và ngữ cảnh khiến bài toán này rất khó.

## LLM kết hợp với logic

LLM có thể chuyển yêu cầu bằng ngôn ngữ tự nhiên thành ràng buộc logic, sau đó để một bộ chứng minh hoặc solver kiểm tra:

```text
Ngôn ngữ tự nhiên
     ↓ LLM phân tích ngữ nghĩa
FOL / Datalog / ràng buộc kiểu SMT
     ↓ bộ máy hình thức
kết quả đã kiểm chứng / phản ví dụ
```

Rủi ro lớn nhất nằm ở bước chuyển đổi. Một solver có thể chứng minh chính xác công thức mà nó nhận được nhưng không đảm bảo công thức đó phản ánh đúng ý định ban đầu của người dùng.

## Mô hình tư duy

```text
Hằng          = đối tượng có tên
Biến          = chỗ giữ chỗ cho đối tượng
Vị từ         = thuộc tính hoặc quan hệ
Hàm           = ánh xạ tạo ra một đối tượng
∀             = với mọi đối tượng
∃             = tồn tại ít nhất một đối tượng
Hợp nhất      = tìm phép thế làm các cấu trúc khớp nhau
Suy luận      = dẫn xuất mệnh đề mới bằng quy tắc hình thức
```

## Các hiểu lầm thường gặp

### “∀x P(x) nghĩa là P thường đúng”

Không. Lượng từ toàn thể khẳng định mọi đối tượng trong miền đều thỏa `P` dưới diễn giải đang dùng.

### “∃x nghĩa là ta biết x cụ thể là ai”

Không nhất thiết. Nó chỉ khẳng định tồn tại ít nhất một đối tượng làm chứng.

### “FOL có thể biểu diễn mọi thứ cần thiết trong AI”

FOL rất mạnh nhưng không tự nhiên với xác suất, ngoại lệ mặc định, thời gian và một số yêu cầu về hiệu năng suy luận. Vì vậy nó thường được kết hợp với các hình thức khác.

### “Chứng minh hình thức đảm bảo kết luận đúng ngoài đời thực”

Chứng minh chỉ đảm bảo kết luận đi theo logic từ các tiền đề hình thức. Nếu tiền đề hoặc cách mô hình hóa sai, kết luận ngoài đời vẫn có thể sai.

## Liên kết kiến thức

Logic vị từ bậc nhất nâng Logic mệnh đề từ các ký hiệu Boolean phẳng thành cấu trúc quan hệ, tạo cầu nối tới ontology, rule engine và Knowledge Graph. Những hạn chế của nó là lý do ta cần [Suy luận xác suất](./04_probabilistic_reasoning.md) và các phương pháp phi đơn điệu hoặc lai.

Xem tiếp: [Suy luận và lập luận](./03_inference_and_reasoning.md).