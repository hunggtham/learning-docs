# Kolmogorov complexity, compression và trực giác incompressibility

Có những chuỗi dữ liệu nhìn rất dài nhưng thực ra chứa rất ít thông tin mới. Chuỗi `010101...` lặp lại một triệu lần có thể được mô tả bằng một chương trình rất ngắn: “in `01` năm trăm nghìn lần”. Ngược lại, một chuỗi bit được chọn ngẫu nhiên đủ dài thường không có mô tả nào ngắn hơn đáng kể so với chính nó.

Ý tưởng này dẫn tới **Kolmogorov complexity (độ phức tạp Kolmogorov / 콜모고로프 복잡도)**: đo lượng thông tin của một đối tượng bằng độ dài của mô tả thuật toán ngắn nhất có thể sinh ra đối tượng đó.

Mental model của chapter:

```text
object x
→ candidate descriptions/programs
→ shortest program that outputs x
→ description length
→ compressibility / regularity / incompressibility
```

Điểm quan trọng không phải tính được một con số chính xác cho file thực tế. Giá trị của khái niệm nằm ở việc nối **computation**, **information**, **compression**, **randomness** và giới hạn của những gì một thuật toán có thể phát hiện.

## 1. Từ “dữ liệu dài” tới “mô tả ngắn”

Giả sử có hai chuỗi cùng dài 64 bit:

```text
A = 0101010101010101010101010101010101010101010101010101010101010101
B = 1011010010011110001011010111000010100011110101001100100101110010
```

`A` có pattern rất rõ. Một description ngắn có thể nói “lặp `01` 32 lần”. `B` có thể cũng được sinh bởi một quy luật ngắn nào đó, nhưng nếu không tồn tại quy luật ngắn hơn chính chuỗi, cách mô tả tốt nhất gần như là ghi nguyên 64 bit.

Kolmogorov complexity formalize trực giác này. Với một universal machine cố định `U`, ký hiệu gần đúng:

```text
K_U(x) = min |p|
         sao cho U(p) = x
```

`p` là program, `|p|` là độ dài description của program, còn `U(p)` là output.

Một object có `K(x)` nhỏ là **compressible**: có structure cho phép mô tả ngắn. Object có `K(x)` gần độ dài của chính nó là **incompressible**.

## 2. Tại sao phải cố định universal machine

Nếu ta được phép phát minh một machine mới cho từng object, khái niệm trở nên vô nghĩa. Ta có thể tạo machine đặc biệt với instruction một bit mang nghĩa “in toàn bộ cuốn sách này”.

Vì vậy Kolmogorov complexity luôn được định nghĩa tương đối với một universal description language hoặc universal Turing machine.

Điều đáng chú ý là **invariance theorem** cho biết khi đổi giữa hai universal machines hợp lý, complexity chỉ khác nhau tối đa bởi một hằng số phụ thuộc vào compiler/interpreter giữa hai machine:

```text
K_U(x) ≤ K_V(x) + c_VU
```

Với object rất lớn, constant này thường không làm thay đổi trực giác về việc object có structure mạnh hay gần incompressible.

Nó cũng giải thích tại sao không nên hiểu `K(x)` như kích thước file chính xác theo byte. Đây là một đại lượng lý thuyết về **minimal effective description**.

## 3. Compression là tìm model, không chỉ xóa byte thừa

Một compressor tốt đang cố tìm regularity: repetition, local correlation, dictionary reuse, predictable symbol distribution hoặc structure khác có thể mã hóa ngắn hơn.

Ta có thể nhìn compression theo hai phần:

```text
compressed representation
≈ model/description of regularity
+ residual information not explained by model
```

Ví dụ một ảnh bầu trời xanh lớn có nhiều pixel tương quan; một codec không cần mô tả từng pixel độc lập. Một source-code repository có nhiều token và đoạn text lặp lại. Một log có timestamp tăng đều và template lặp lại.

Nếu residual vẫn có structure, model chưa khai thác hết redundancy. Nếu residual gần incompressible đối với class model đang dùng, compressor đã đi gần giới hạn của chính model đó.

## 4. Kolmogorov complexity không tính được trong trường hợp tổng quát

Một câu hỏi tự nhiên là: tại sao không viết chương trình thử mọi program rồi lấy program ngắn nhất sinh ra `x`?

Vấn đề là một candidate program có thể chạy mãi không kết thúc. Muốn biết chắc “không còn program ngắn hơn nào sẽ output `x` trong tương lai”, ta phải giải quyết một dạng của **halting problem**.

Có thể chứng minh rằng `K(x)` không computable trong trường hợp tổng quát. Đây không phải hạn chế vì máy tính hiện tại quá chậm; nó là giới hạn lý thuyết.

Connection trực tiếp:

- [Formal models, reductions và computability](./00_formal_models_reductions_and_computability.md)
- [Rice's theorem và giới hạn static analysis](./02_rices_theorem_semantic_properties_and_static_analysis_limits.md)

Điều này tạo một pattern quan trọng: một đại lượng có thể được định nghĩa rất rõ nhưng không có thuật toán tổng quát luôn tính chính xác nó.

## 5. Không thể có compressor lossless làm mọi chuỗi ngắn hơn

Giả sử mọi chuỗi `n` bit đều có thể nén thành ít hơn `n` bit. Số chuỗi đầu vào là `2^n`, nhưng tổng số chuỗi ngắn hơn `n` bit chỉ là:

```text
1 + 2 + 4 + ... + 2^(n-1) = 2^n - 1
```

Không đủ codeword ngắn để ánh xạ injective cho toàn bộ `2^n` input nếu cần giải nén lossless.

Vì vậy bất kỳ lossless compressor nào cũng phải làm một số input dài hơn hoặc ít nhất không ngắn đi. Đây là pigeonhole principle ở dạng information/compression.

Kết luận thực tế: “file không nén thêm được” không chứng minh file thật sự ngẫu nhiên, nhưng không thể kỳ vọng một compressor universal luôn giảm kích thước mọi input.

## 6. Incompressibility method: chứng minh bằng cách đếm

Một insight mạnh của Kolmogorov complexity là phần lớn chuỗi dài phải incompressible.

Với chuỗi dài `n`, số description ngắn hơn `n-c` bit bị giới hạn. Do đó chỉ một phần nhỏ trong `2^n` chuỗi có thể có description ngắn hơn nhiều.

Từ đó có **incompressibility method**: thay vì xây trực tiếp một object “ngẫu nhiên”, ta reasoning rằng đa số object không thể có description ngắn; chọn một object incompressible rồi suy ra nó không thể sở hữu quá nhiều regularity đặc biệt, vì regularity đó sẽ tạo description ngắn.

Đây là proof technique, không phải compression algorithm.

## 7. Randomness như thiếu description ngắn

Một cách nhìn algorithmic randomness là: chuỗi ngẫu nhiên tốt không có program ngắn đáng kể sinh chính xác chuỗi đó.

Nhưng phải phân biệt ba ý:

```text
statistical randomness
algorithmic incompressibility
computational unpredictability
```

Một PRNG có seed 256 bit có thể sinh stream dài hàng gigabyte trông thống kê rất ngẫu nhiên. Tuy nhiên toàn bộ stream có description ngắn: “chạy PRNG X với seed S”. Vì vậy nó không algorithmically random theo độ dài output.

Dù vậy nếu PRNG là cryptographically secure, một attacker bị giới hạn tài nguyên tính toán vẫn không dự đoán được output tiếp theo. Đó là **computational unpredictability**, sẽ được đào sâu ở [Randomness, entropy sources và computational unpredictability](./05_randomness_entropy_sources_and_computational_unpredictability.md).

## 8. Kolmogorov complexity và Shannon entropy không phải cùng một đại lượng

**Shannon entropy** mô tả uncertainty trung bình của một random variable/distribution. Kolmogorov complexity nói về minimal description của một object cụ thể.

Ví dụ một fair coin source có entropy 1 bit mỗi symbol. Một sequence cụ thể sinh từ source đó vẫn có thể tình cờ là `000000...`, chuỗi có description rất ngắn.

Ngược lại, nếu chỉ có một file duy nhất mà không có distribution model, Kolmogorov viewpoint vẫn hỏi được “mô tả thuật toán ngắn nhất của file này là gì?”, trong khi Shannon entropy cần random variable/probability model.

Hai lý thuyết gặp nhau khi xét typical sequences và coding, nhưng không được dùng hai từ `entropy` và `complexity` như đồng nghĩa.

Đọc tiếp: [Information theory, coding bounds và noisy channels](./04_information_theory_coding_bounds_and_noisy_channels.md).

## 9. Minimum Description Length: model tốt phải trả cả giá model

Một application quan trọng về trực giác là **Minimum Description Length (MDL)**. Khi chọn model cho data, không chỉ đo data fit tốt tới đâu. Model quá phức tạp có thể “nhớ” data.

Ta reasoning bằng:

```text
Total description length
= description length of model
+ description length of data given model
```

Model quá đơn giản làm residual dài. Model quá phức tạp làm phần mô tả model dài. Điểm cân bằng tạo connection với Occam's razor, regularization và model selection.

Không nên biến MDL thành câu “model nhỏ luôn tốt hơn”. Một model lớn vẫn hợp lý nếu nó giảm residual đủ nhiều và generalize tốt cho mục tiêu đang xét.

## 10. Compression ratio là evidence có điều kiện

Trong production, ta không đo `K(x)` chính xác. Ta dùng compressor cụ thể như một upper bound thực dụng:

```text
K(x) ≤ length(compressor_program) + length(compressed_x) + decoding overhead
```

Nếu một dataset nén rất tốt bằng codec phù hợp, đó là evidence rằng codec tìm được regularity. Nếu không nén được, có nhiều hypothesis:

- data thật sự gần random;
- data đã được nén/encrypt trước;
- regularity tồn tại nhưng codec không model được;
- block size/dictionary/window không phù hợp;
- metadata/container overhead chiếm ưu thế ở input nhỏ.

Do đó compression ratio là evidence về **data + model**, không phải chứng minh tuyệt đối về intrinsic information.

## 11. Encryption thường phá compressibility quan sát được

Ciphertext của encryption hiện đại được thiết kế để khó phân biệt với random đối với attacker hiệu quả. Vì vậy ciphertext thường không còn pattern dễ nén.

Pipeline thường hợp lý là:

```text
plaintext
→ compress
→ encrypt
```

thay vì encrypt rồi mới compress.

Tuy nhiên compression trước encryption có thể tạo side channel khi attacker điều khiển một phần input và quan sát compressed length. Khi secret và attacker-controlled data chia sẻ compression context, length có thể leak thông tin về prefix match.

Connection này cho thấy “compression tốt” và “security tốt” không thể reasoning tách rời khỏi threat model.

## 12. Dữ liệu có structure nhưng vẫn khó học

Một object có description ngắn không đồng nghĩa một learner cụ thể sẽ tìm được description đó. Shortest program có thể tồn tại nhưng computationally rất khó khám phá.

Đây là khác biệt giữa:

```text
existence of a short description
vs
ability to discover it efficiently
```

Trong machine learning, một dataset có generative rule ngắn nhưng optimization procedure có thể không tìm được model tương ứng. Trong program synthesis, solution ngắn có thể nằm trong search space quá lớn.

Kolmogorov complexity vì vậy là thước đo description-theoretic, không phải runtime complexity của quá trình tìm description.

## 13. Ví dụ reasoning: log production tăng kích thước bất thường

Giả sử cùng số request nhưng log tăng từ 20 GB/ngày lên 80 GB/ngày và compression ratio xấu đi.

Không nên kết luận ngay “traffic random hơn”. Hãy đi theo path:

```text
logical events
→ template/cardinality
→ serialization
→ compression blocks/dictionary
→ compressed bytes
```

Có thể một release mới đưa request ID hoặc high-cardinality payload vào giữa template, phá dictionary locality. Có thể stack trace tăng. Có thể log đã chứa compressed/base64/encrypted payload. Có thể block rotation quá nhỏ làm dictionary không reuse được.

Evidence cần gồm raw bytes/event, field cardinality, template distribution, block size, codec ratio và CPU cost. Đây là cách đưa theory về regularity vào system diagnosis.

## 14. Những nhầm lẫn thường gặp

**“Kolmogorov complexity là file size sau gzip.”** Không đúng. gzip chỉ là một compressor cụ thể và cho một upper bound thực dụng.

**“Random data không có pattern nào.”** Cần cẩn thận. Một sequence hữu hạn có thể chứa local pattern tình cờ; randomness nói về description/statistical/computational property theo model cụ thể.

**“Nếu output PRNG dài thì nó có nhiều entropy tương ứng.”** Không đúng. Entropy không thể tự sinh từ deterministic computation; output uncertainty bị giới hạn bởi uncertainty của seed/state.

**“Nén được nghĩa là dữ liệu vô nghĩa.”** Không đúng. Semantic meaning và description length là hai trục khác nhau.

**“Không tính được K(x) nên khái niệm vô dụng.”** Không đúng. Nó cung cấp lower-bound intuition, proof technique và ngôn ngữ thống nhất cho compression/randomness/model complexity.

## 15. Connection map

```text
Computability
→ K(x) không computable chính xác

Counting
→ phần lớn chuỗi dài incompressible

Compression
→ tìm regularity để rút ngắn description

Information theory
→ expected code length dưới distribution

Randomness
→ incompressibility / unpredictability / entropy source

Security
→ ciphertext, PRNG, side-channel qua compressed length

Machine learning
→ model complexity + residual / MDL intuition
```

## 16. Checklist reasoning

Khi gặp một vấn đề liên quan “thông tin”, “random”, “compression” hoặc “model complexity”, hãy hỏi:

```text
Object cụ thể hay distribution đang được nói tới?
Description language/model nào được giả định?
Regularity nào compressor/model đang khai thác?
Ta cần exact information hay computationally feasible approximation?
Uncertainty đến từ source nào?
Deterministic transform có đang bị nhầm là tạo entropy mới không?
Compression ratio phản ánh intrinsic structure hay limitation của codec?
Security threat model có biến length/pattern thành side channel không?
```

## Kết luận

Kolmogorov complexity đưa ra một định nghĩa sâu về thông tin của một object: **độ dài mô tả thuật toán ngắn nhất sinh ra object đó**. Nó giải thích tại sao compression là tìm structure, tại sao phần lớn chuỗi dài không thể nén mạnh, tại sao randomness có thể nhìn qua incompressibility và tại sao có những đại lượng được định nghĩa rõ nhưng không thể tính chính xác bằng thuật toán tổng quát.

Điểm cần giữ lại không phải công thức `K(x)`, mà là distinction:

```text
length of data
≠ amount of new algorithmic information

compressibility
≠ semantic meaning

algorithmic randomness
≠ statistical appearance
≠ computational unpredictability
```

Các distinction này là prerequisite tự nhiên cho information theory, cryptographic randomness, model selection và reasoning về dữ liệu ở quy mô hệ thống.