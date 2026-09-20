# Editorial Standard — Mathematics Knowledge Library

Tài liệu trong `mathematics/` được viết như một **knowledge book để học lâu dài**, không phải cheat sheet, collection công thức hay note ôn thi. File này là chuẩn biên soạn cho các lần update tiếp theo, để những chapter được viết ở các thời điểm khác nhau vẫn có cùng chất lượng và cùng cách tư duy.

## 1. Mục tiêu của một chapter

Một chapter tốt phải giúp người đọc xây được một mental model đủ mạnh để tự suy luận khi gặp tình huống mới. Sau khi đọc, người học không chỉ trả lời được “công thức là gì?” mà còn phải hiểu:

- object hoặc concept đang nói tới là gì;
- vấn đề nào khiến concept đó cần tồn tại;
- concept được xây từ những assumption hoặc idea nào;
- formula xuất hiện từ đâu và từng thành phần có ý nghĩa gì;
- khi nào model đúng, khi nào bắt đầu sai hoặc thiếu;
- concept liên kết thế nào với các chapter trước và sau;
- cùng structure đó xuất hiện ở đâu trong science, engineering, software, data, AI hoặc đời sống.

Một chapter không được coi là hoàn thiện chỉ vì đã liệt kê đủ definitions và formulas.

## 2. Luồng giải thích mặc định

Không ép mọi chapter vào một template cứng, nhưng một luồng tốt thường là:

```text
problem / phenomenon
    ↓
what must be represented or measured?
    ↓
minimal definitions
    ↓
relationship between quantities
    ↓
model / theorem / formula
    ↓
derivation or reasoning
    ↓
worked examples
    ↓
limits and failure modes
    ↓
connections to other knowledge
    ↓
mental model
```

Nếu người đọc cần một prerequisite để hiểu bước hiện tại, hoặc giải thích prerequisite ngay tại chỗ ở mức đủ dùng, hoặc link rõ đến chapter đã giải thích nó. Không dùng câu kiểu “phần này sẽ rõ hơn ở chương nâng cao” để né giải thích bản chất cần thiết.

## 3. Viết thành discourse, không viết thành flashcard

Phần giải thích chính ưu tiên paragraph có logical flow. Bullet chỉ nên dùng khi bản chất nội dung thực sự là list, ví dụ assumptions, classification, algorithm steps hoặc concise comparison.

Không viết liên tiếp các câu như:

```text
A là ...
B là ...
C dùng để ...
```

nếu giữa A, B và C có causal relationship. Hãy nói vì sao B xuất hiện từ A và vì sao C cần B.

Mỗi section nên có một câu hỏi hoặc idea trung tâm. Heading không nên chia vụn nội dung thành quá nhiều section chỉ có một paragraph ngắn.

## 4. Definition phải đi cùng intuition

Definition chính xác là cần thiết nhưng không đủ. Khi giới thiệu một term mới, dùng format:

```text
Tên tiếng Việt (English term / 한국어 용어)
```

ở lần xuất hiện quan trọng đầu tiên nếu Korean term hữu ích.

Sau definition, giải thích object đó nên được “nhìn” như thế nào. Ví dụ, basis không chỉ là “linearly independent spanning set”; nó là một hệ tọa độ tối thiểu cho một vector space. Derivative không chỉ là limit của difference quotient; nó là local linear model của một function.

## 5. Công thức phải có provenance

Không để formula đứng một mình. Với formula quan trọng, chapter phải giải thích ít nhất bốn lớp:

1. formula đang model điều gì;
2. mỗi symbol đại diện cho gì và unit nếu có;
3. vì sao các đại lượng liên hệ theo dạng đó;
4. assumptions hoặc domain validity.

Khi derivation hợp lý trong scope, derive từng bước. Không dùng “ta dễ dàng suy ra” ở chỗ mà người học mới có thể không thấy dễ.

Ví dụ, thay vì chỉ ghi

```math
A(t)=A_0e^{kt},
```

cần nối nó với local law

```math
\frac{dA}{dt}=kA
```

và giải thích rằng exponential xuất hiện vì tốc độ thay đổi tại mỗi thời điểm tỷ lệ với chính lượng hiện có.

## 6. Ví dụ phải tạo reasoning transfer

Một chapter quan trọng nên cố gắng có nhiều lớp ví dụ khi phù hợp:

**Intuitive example** giúp người đọc hình dung structure trước khi tính toán.

**Numeric example** bắt người đọc đi qua formula với con số cụ thể và kiểm tra unit/order of magnitude.

**Real-system example** cho thấy model được sử dụng trong software, physics, finance, statistics hoặc engineering như thế nào.

**Counterexample hoặc failure example** cho biết assumption nào thật sự quan trọng.

Ví dụ không nên chỉ chứng minh rằng formula “chạy được”; nó phải làm rõ một idea.

## 7. Liên kết giữa các lĩnh vực phải dựa trên cùng structure

Không thêm section “Ứng dụng IT” chỉ để kể tên công nghệ. Chỉ tạo connection khi có cùng mathematical structure.

Ví dụ:

- composition của functions ↔ software pipeline ↔ neural network layers;
- projection ↔ least squares ↔ attention similarity ↔ graphics camera coordinates;
- exponential decay ↔ radioactive decay ↔ cache TTL probabilistic models ↔ discounting;
- graph reachability ↔ dependency resolution ↔ network routing ↔ state transition;
- condition number ↔ sensitivity of a computational problem.

Khi connection chỉ là analogy bề mặt, không dùng nó như explanation.

## 8. Phân biệt model, theorem và computation

Ba câu hỏi này phải được tách rõ:

**Model:** Ta đã chọn representation nào cho reality/problem?

**Mathematics:** Trong model đó, điều gì đúng một cách logical?

**Computation:** Máy tính thực sự tính approximation đó thế nào và error ở đâu?

Ví dụ `Ax=b` có thể có exact mathematical solution, nhưng measured `A,b` có noise và numerical algorithm lại dùng floating point. Đây là ba nguồn uncertainty khác nhau.

## 9. Luôn nói về assumptions và failure modes

Một formula hữu ích hơn khi người đọc biết lúc nào không nên dùng nó.

Các câu hỏi cần xem xét:

- domain có restriction gì?
- theorem cần continuity/differentiability/independence/nonnegative weight... không?
- model giả định linearity, stationarity, infinite resource, Gaussian noise hay independence không?
- nếu assumption hỏng thì kết luận sai theo kiểu nào?
- numerical method có stability hoặc conditioning issue không?

Đây là phần giúp knowledge chuyển từ “school math” thành engineering judgment.

## 10. Dùng notation nhất quán

Ưu tiên notation phổ biến trong textbook và documentation quốc tế. Nếu một symbol có nhiều conventions, nói rõ convention đang dùng.

Không đổi notation vô lý giữa các section. Vector nên được viết nhất quán, matrix dimension phải hợp lệ, summation index cần có range rõ khi cần. Probability phân biệt `P(A)`, density `p(x)` và likelihood `L(θ;x)`.

Formula display dùng fenced `math` block theo convention hiện tại của repository.

## 11. Mental Model không phải summary

`## Mental Model` phải nén chapter thành một cách nhìn có khả năng tái sử dụng, chứ không lặp lại definition.

Ví dụ tốt:

> Basis là một vocabulary tối thiểu cho vector space: đổi basis giống đổi ngôn ngữ tọa độ, object không đổi nhưng description có thể đơn giản hơn rất nhiều.

Mental model phải giúp người đọc dự đoán hoặc suy luận, không chỉ ghi nhớ.

## 12. Common Misconceptions phải giải thích vì sao sai

Không chỉ liệt kê lỗi. Với misconception quan trọng, nói nguyên nhân nó có vẻ hợp lý và điểm logic nào bị nhầm.

Ví dụ: “logarithm làm dữ liệu thành tuyến tính” chỉ đúng với một số functional relationships; log-transform không tự động biến arbitrary nonlinear relation thành linear relation và còn thay đổi interpretation/error structure.

## 13. Chất lượng chapter quan trọng hơn độ dài

Không đặt word-count target cứng. Tuy nhiên, chapter nền tảng chỉ vài trăm từ thường là dấu hiệu cần audit nếu concept có nhiều dependency và consequences.

Một file dài cũng có thể kém nếu lặp ý. Mục tiêu là **conceptual completeness**, không phải volume.

## 14. Checklist trước khi merge

Trước khi coi một chapter là hoàn thiện trong scope, kiểm tra:

- Có giải thích problem/need trước definition không?
- Có giải thích bản chất, không chỉ syntax/formula không?
- Formula chính có reasoning hoặc derivation phù hợp không?
- Có example đủ để transfer reasoning không?
- Có assumptions, boundary cases và failure modes không?
- Có liên kết với prerequisites và downstream concepts không?
- English/Korean terminology có nhất quán không?
- Có `Mental Model` thật sự hữu ích không?
- `Common Misconceptions` có giải thích lỗi tư duy không?
- Paragraph có flow hay vẫn giống bullet notes được kéo dài?

## Mental Model cho toàn bộ library

> Mỗi chapter không phải một hộp kiến thức riêng. Nó là một node trong graph của các representations, constraints, transformations, rates, accumulations, symmetries, uncertainties và optimization problems. Viết tốt nghĩa là làm cho các edge giữa những node đó trở nên nhìn thấy được.