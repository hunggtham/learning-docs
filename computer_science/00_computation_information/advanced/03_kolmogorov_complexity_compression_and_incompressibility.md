# Kolmogorov độ phức tạp (complexity / 복잡도), compression và trực giác incompressibility

> **Mạch đọc:** Đặt **Kolmogorov độ phức tạp (complexity / 복잡도), compression và trực giác incompressibility** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Từ “dữ liệu dài” tới “mô tả ngắn”** sang **2. Tại sao phải cố định universal machine**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Có những chuỗi dữ liệu nhìn rất dài nhưng thực ra chứa rất ít thông tin mới. Chuỗi `010101...` lặp lại một triệu lần có thể được mô tả bằng một chương trình rất ngắn: “in `01` năm trăm nghìn lần”. Ngược lại, một chuỗi bit được chọn ngẫu nhiên đủ dài thường không có mô tả nào ngắn hơn đáng kể so với chính nó.

Ý tưởng này dẫn tới **Kolmogorov độ phức tạp (complexity / 복잡도)**: đo lượng thông tin của một đối tượng bằng độ dài của mô tả thuật toán ngắn nhất có thể sinh ra đối tượng đó.

Mô hình tư duy (mental model / 사고 모델) của chapter:

```text
object x
→ candidate descriptions/programs
→ shortest program that outputs x
→ description length
→ compressibility / regularity / incompressibility
```

Điểm quan trọng không phải tính được một con số chính xác cho tệp (file / 파일) thực tế. Giá trị của khái niệm nằm ở việc nối **computation**, **thông tin (information / 정보)**, **compression**, **randomness** và giới hạn của những gì một thuật toán có thể phát hiện.

## 1. Từ “dữ liệu dài” tới “mô tả ngắn”

Giả sử có hai chuỗi cùng dài 64 bit:

```text
A = 0101010101010101010101010101010101010101010101010101010101010101
B = 1011010010011110001011010111000010100011110101001100100101110010
```

`A` có mẫu (pattern / 패턴) rất rõ. Một description ngắn có thể nói “lặp `01` 32 lần”. `B` có thể cũng được sinh bởi một quy luật ngắn nào đó, nhưng nếu không tồn tại quy luật ngắn hơn chính chuỗi, cách mô tả tốt nhất gần như là ghi nguyên 64 bit.

Kolmogorov độ phức tạp (complexity / 복잡도) formalize trực giác này. Với một universal machine cố định `U`, ký hiệu gần đúng:

```text
K_U(x) = min |p|
         sao cho U(p) = x
```

`p` là program, `|p|` là độ dài description của program, còn `U(p)` là đầu ra (output / 출력).

Một đối tượng (object / 객체) có `K(x)` nhỏ là **compressible**: có cấu trúc (structure / 구조) cho phép mô tả ngắn. đối tượng (object / 객체) có `K(x)` gần độ dài của chính nó là **incompressible**.

## 2. Tại sao phải cố định universal machine

Nếu ta được phép phát minh một machine mới cho từng đối tượng (object / 객체), khái niệm trở nên vô nghĩa. Ta có thể tạo machine đặc biệt với instruction một bit mang nghĩa “in toàn bộ cuốn sách này”.

Vì vậy Kolmogorov độ phức tạp (complexity / 복잡도) luôn được định nghĩa tương đối với một universal description ngôn ngữ (language / 언어) hoặc universal Turing machine.

Điều đáng chú ý là **invariance theorem** cho biết khi đổi giữa hai universal machines hợp lý, độ phức tạp (complexity / 복잡도) chỉ khác nhau tối đa bởi một hằng số phụ thuộc vào trình biên dịch (compiler / 컴파일러)/trình thông dịch (interpreter / 인터프리터) giữa hai machine:

```text
K_U(x) ≤ K_V(x) + c_VU
```

Với đối tượng (object / 객체) rất lớn, constant này thường không làm thay đổi trực giác về việc đối tượng (object / 객체) có cấu trúc (structure / 구조) mạnh hay gần incompressible.

Nó cũng giải thích tại sao không nên hiểu `K(x)` như kích thước tệp (file / 파일) chính xác theo byte. Đây là một đại lượng lý thuyết về **minimal effective description**.

## 3. Compression là tìm mô hình (model / 모델), không chỉ xóa byte thừa

Một compressor tốt đang cố tìm regularity: repetition, cục bộ (local / 로컬) correlation, dictionary reuse, predictable symbol phân phối (distribution / 분포) hoặc cấu trúc (structure / 구조) khác có thể mã hóa ngắn hơn.

Ta có thể nhìn compression theo hai phần:

```text
compressed representation
≈ model/description of regularity
+ residual information not explained by model
```

Ví dụ một ảnh bầu trời xanh lớn có nhiều điểm ảnh (pixel / 픽셀) tương quan; một codec không cần mô tả từng điểm ảnh (pixel / 픽셀) độc lập. Một source-code repository có nhiều đơn vị từ (token / 토큰) và đoạn văn bản (text / 텍스트) lặp lại. Một log có timestamp tăng đều và template lặp lại.

Nếu residual vẫn có cấu trúc (structure / 구조), mô hình (model / 모델) chưa khai thác hết redundancy. Nếu residual gần incompressible đối với lớp (class / 클래스) mô hình (model / 모델) đang dùng, compressor đã đi gần giới hạn của chính mô hình (model / 모델) đó.

## 4. Kolmogorov độ phức tạp (complexity / 복잡도) không tính được trong trường hợp tổng quát

Một câu hỏi tự nhiên là: tại sao không viết chương trình thử mọi program rồi lấy program ngắn nhất sinh ra `x`?

Vấn đề là một candidate program có thể chạy mãi không kết thúc. Muốn biết chắc “không còn program ngắn hơn nào sẽ đầu ra (output / 출력) `x` trong tương lai”, ta phải giải quyết một dạng của **halting bài toán (problem / 문제)**.

Có thể chứng minh rằng `K(x)` không computable trong trường hợp tổng quát. Đây không phải hạn chế vì máy tính hiện tại quá chậm; nó là giới hạn lý thuyết.

Liên kết (connection / 연결) trực tiếp:

- [Formal models, reductions và computability](./00_formal_models_reductions_and_computability.md)
- [Rice's theorem và giới hạn static analysis](./02_rices_theorem_semantic_properties_and_static_analysis_limits.md)

Điều này tạo một mẫu (pattern / 패턴) quan trọng: một đại lượng có thể được định nghĩa rất rõ nhưng không có thuật toán tổng quát luôn tính chính xác nó.

## 5. Không thể có compressor lossless làm mọi chuỗi ngắn hơn

Giả sử mọi chuỗi `n` bit đều có thể nén thành ít hơn `n` bit. Số chuỗi đầu vào là `2^n`, nhưng tổng số chuỗi ngắn hơn `n` bit chỉ là:

```text
1 + 2 + 4 + ... + 2^(n-1) = 2^n - 1
```

Không đủ codeword ngắn để ánh xạ injective cho toàn bộ `2^n` đầu vào (input / 입력) nếu cần giải nén lossless.

Vì vậy bất kỳ lossless compressor nào cũng phải làm một số đầu vào (input / 입력) dài hơn hoặc ít nhất không ngắn đi. Đây là pigeonhole principle ở dạng thông tin (information / 정보)/compression.

Kết luận thực tế: “tệp (file / 파일) không nén thêm được” không chứng minh tệp (file / 파일) thật sự ngẫu nhiên, nhưng không thể kỳ vọng một compressor universal luôn giảm kích thước mọi đầu vào (input / 입력).

## 6. Incompressibility phương thức (method / 메서드): chứng minh bằng cách đếm

Một insight mạnh của Kolmogorov độ phức tạp (complexity / 복잡도) là phần lớn chuỗi dài phải incompressible.

Với chuỗi dài `n`, số description ngắn hơn `n-c` bit bị giới hạn. Do đó chỉ một phần nhỏ trong `2^n` chuỗi có thể có description ngắn hơn nhiều.

Từ đó có **incompressibility phương thức (method / 메서드)**: thay vì xây trực tiếp một đối tượng (object / 객체) “ngẫu nhiên”, ta lập luận (reasoning / 추론) rằng đa số đối tượng (object / 객체) không thể có description ngắn; chọn một đối tượng (object / 객체) incompressible rồi suy ra nó không thể sở hữu quá nhiều regularity đặc biệt, vì regularity đó sẽ tạo description ngắn.

Đây là proof technique, không phải compression thuật toán (algorithm / 알고리즘).

## 7. Randomness như thiếu description ngắn

Một cách nhìn algorithmic randomness là: chuỗi ngẫu nhiên tốt không có program ngắn đáng kể sinh chính xác chuỗi đó.

Nhưng phải phân biệt ba ý:

```text
statistical randomness
algorithmic incompressibility
computational unpredictability
```

Một PRNG có seed 256 bit có thể sinh stream dài hàng gigabyte trông thống kê rất ngẫu nhiên. Tuy nhiên toàn bộ stream có description ngắn: “chạy PRNG X với seed S”. Vì vậy nó không algorithmically random theo độ dài đầu ra (output / 출력).

Dù vậy nếu PRNG là cryptographically secure, một attacker bị giới hạn tài nguyên tính toán vẫn không dự đoán được đầu ra (output / 출력) tiếp theo. Đó là **computational unpredictability**, sẽ được đào sâu ở [Randomness, entropy sources và computational unpredictability](./05_randomness_entropy_sources_and_computational_unpredictability.md).

## 8. Kolmogorov độ phức tạp (complexity / 복잡도) và Shannon entropy không phải cùng một đại lượng

**Shannon entropy** mô tả bất định (uncertainty / 불확실성) trung bình của một random variable/phân phối (distribution / 분포). Kolmogorov độ phức tạp (complexity / 복잡도) nói về minimal description của một đối tượng (object / 객체) cụ thể.

Ví dụ một fair coin nguồn (source / 소스) có entropy 1 bit mỗi symbol. Một chuỗi (sequence / 시퀀스) cụ thể sinh từ nguồn (source / 소스) đó vẫn có thể tình cờ là `000000...`, chuỗi có description rất ngắn.

Ngược lại, nếu chỉ có một tệp (file / 파일) duy nhất mà không có phân phối (distribution / 분포) mô hình (model / 모델), Kolmogorov viewpoint vẫn hỏi được “mô tả thuật toán ngắn nhất của tệp (file / 파일) này là gì?”, trong khi Shannon entropy cần random variable/xác suất (probability / 확률) mô hình (model / 모델).

Hai lý thuyết gặp nhau khi xét typical sequences và coding, nhưng không được dùng hai từ `entropy` và `complexity` như đồng nghĩa.

Đọc tiếp: [Information theory, coding bounds và noisy channels](./04_information_theory_coding_bounds_and_noisy_channels.md).

## 9. Minimum Description Length: mô hình (model / 모델) tốt phải trả cả giá mô hình (model / 모델)

Một ứng dụng (application / 애플리케이션) quan trọng về trực giác là **Minimum Description Length (MDL)**. Khi chọn mô hình (model / 모델) cho dữ liệu (data / 데이터), không chỉ đo dữ liệu (data / 데이터) fit tốt tới đâu. mô hình (model / 모델) quá phức tạp có thể “nhớ” dữ liệu (data / 데이터).

Ta lập luận (reasoning / 추론) bằng:

```text
Total description length
= description length of model
+ description length of data given model
```

Mô hình (model / 모델) quá đơn giản làm residual dài. mô hình (model / 모델) quá phức tạp làm phần mô tả mô hình (model / 모델) dài. Điểm cân bằng tạo liên kết (connection / 연결) với Occam's razor, regularization và mô hình (model / 모델) selection.

Không nên biến MDL thành câu “mô hình (model / 모델) nhỏ luôn tốt hơn”. Một mô hình (model / 모델) lớn vẫn hợp lý nếu nó giảm residual đủ nhiều và generalize tốt cho mục tiêu đang xét.

## 10. Compression ratio là bằng chứng (evidence / 증거) có điều kiện

Trong môi trường vận hành (production / 운영 환경), ta không đo `K(x)` chính xác. Ta dùng compressor cụ thể như một upper bound thực dụng:

```text
K(x) ≤ length(compressor_program) + length(compressed_x) + decoding overhead
```

Nếu một dataset nén rất tốt bằng codec phù hợp, đó là bằng chứng (evidence / 증거) rằng codec tìm được regularity. Nếu không nén được, có nhiều hypothesis:

- dữ liệu (data / 데이터) thật sự gần random;
- dữ liệu (data / 데이터) đã được nén/encrypt trước;
- regularity tồn tại nhưng codec không mô hình (model / 모델) được;
- khối (block / 블록) kích thước (size / 크기)/dictionary/cửa sổ (window / 윈도우) không phù hợp;
- siêu dữ liệu (metadata / 메타데이터)/bộ chứa (container / 컨테이너) overhead chiếm ưu thế ở đầu vào (input / 입력) nhỏ.

Do đó compression ratio là bằng chứng (evidence / 증거) về **dữ liệu (data / 데이터) + mô hình (model / 모델)**, không phải chứng minh tuyệt đối về intrinsic thông tin (information / 정보).

## 11. Encryption thường phá compressibility quan sát được

Ciphertext của encryption hiện đại được thiết kế để khó phân biệt với random đối với attacker hiệu quả. Vì vậy ciphertext thường không còn mẫu (pattern / 패턴) dễ nén.

Chuỗi xử lý (pipeline / 파이프라인) thường hợp lý là:

```text
plaintext
→ compress
→ encrypt
```

thay vì encrypt rồi mới compress.

Tuy nhiên compression trước encryption có thể tạo side channel khi attacker điều khiển một phần đầu vào (input / 입력) và quan sát compressed length. Khi secret và attacker-controlled dữ liệu (data / 데이터) chia sẻ compression ngữ cảnh (context / 맥락), length có thể leak thông tin về prefix match.

Liên kết (connection / 연결) này cho thấy “compression tốt” và “bảo mật (security / 보안) tốt” không thể lập luận (reasoning / 추론) tách rời khỏi threat mô hình (model / 모델).

## 12. Dữ liệu có cấu trúc (structure / 구조) nhưng vẫn khó học

Một đối tượng (object / 객체) có description ngắn không đồng nghĩa một learner cụ thể sẽ tìm được description đó. Shortest program có thể tồn tại nhưng computationally rất khó khám phá.

Đây là khác biệt giữa:

```text
existence of a short description
vs
ability to discover it efficiently
```

Trong machine học tập (learning / 학습), một dataset có generative quy tắc (rule / 규칙) ngắn nhưng tối ưu hóa (optimization / 최적화) procedure có thể không tìm được mô hình (model / 모델) tương ứng. Trong program synthesis, solution ngắn có thể nằm trong tìm kiếm (search / 검색) không gian (space / 공간) quá lớn.

Kolmogorov độ phức tạp (complexity / 복잡도) vì vậy là thước đo description-theoretic, không phải thời gian chạy (runtime / 런타임) độ phức tạp (complexity / 복잡도) của quá trình tìm description.

## 13. Ví dụ lập luận (reasoning / 추론): log môi trường vận hành (production / 운영 환경) tăng kích thước bất thường

Giả sử cùng số yêu cầu (request / 요청) nhưng log tăng từ 20 GB/ngày lên 80 GB/ngày và compression ratio xấu đi.

Không nên kết luận ngay “traffic random hơn”. Hãy đi theo đường dẫn (path / 경로):

```text
logical events
→ template/cardinality
→ serialization
→ compression blocks/dictionary
→ compressed bytes
```

Có thể một bản phát hành (release / 릴리스) mới đưa yêu cầu (request / 요청) ID hoặc high-cardinality payload vào giữa template, phá dictionary locality. Có thể dấu vết ngăn xếp (stack trace / 스택 트레이스) tăng. Có thể log đã chứa compressed/base64/encrypted payload. Có thể khối (block / 블록) rotation quá nhỏ làm dictionary không reuse được.

Bằng chứng (evidence / 증거) cần gồm raw bytes/sự kiện (event / 이벤트), trường dữ liệu (field / 필드) cardinality, template phân phối (distribution / 분포), khối (block / 블록) kích thước (size / 크기), codec ratio và CPU chi phí (cost / 비용). Đây là cách đưa lý thuyết (theory / 이론) về regularity vào hệ thống (system / 시스템) diagnosis.

## 14. Những nhầm lẫn thường gặp

**“Kolmogorov độ phức tạp (complexity / 복잡도) là tệp (file / 파일) kích thước (size / 크기) sau gzip.”** Không đúng. gzip chỉ là một compressor cụ thể và cho một upper bound thực dụng.

**“Random dữ liệu (data / 데이터) không có mẫu (pattern / 패턴) nào.”** Cần cẩn thận. Một chuỗi (sequence / 시퀀스) hữu hạn có thể chứa cục bộ (local / 로컬) mẫu (pattern / 패턴) tình cờ; randomness nói về description/statistical/computational thuộc tính (property / 속성) theo mô hình (model / 모델) cụ thể.

**“Nếu đầu ra (output / 출력) PRNG dài thì nó có nhiều entropy tương ứng.”** Không đúng. Entropy không thể tự sinh từ deterministic computation; đầu ra (output / 출력) bất định (uncertainty / 불확실성) bị giới hạn bởi bất định (uncertainty / 불확실성) của seed/trạng thái (state / 상태).

**“Nén được nghĩa là dữ liệu vô nghĩa.”** Không đúng. ý nghĩa (semantic meaning / 의미적 뜻) và description length là hai trục khác nhau.

**“Không tính được K(x) nên khái niệm vô dụng.”** Không đúng. Nó cung cấp lower-bound intuition, proof technique và ngôn ngữ thống nhất cho compression/randomness/mô hình (model / 모델) độ phức tạp (complexity / 복잡도).

## 15. liên kết (connection / 연결) map

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

## 16. Checklist lập luận (reasoning / 추론)

Khi gặp một vấn đề liên quan “thông tin”, “random”, “compression” hoặc “mô hình (model / 모델) độ phức tạp (complexity / 복잡도)”, hãy hỏi:

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

Kolmogorov độ phức tạp (complexity / 복잡도) đưa ra một định nghĩa sâu về thông tin của một đối tượng (object / 객체): **độ dài mô tả thuật toán ngắn nhất sinh ra đối tượng (object / 객체) đó**. Nó giải thích tại sao compression là tìm cấu trúc (structure / 구조), tại sao phần lớn chuỗi dài không thể nén mạnh, tại sao randomness có thể nhìn qua incompressibility và tại sao có những đại lượng được định nghĩa rõ nhưng không thể tính chính xác bằng thuật toán tổng quát.

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

Các distinction này là prerequisite tự nhiên cho thông tin (information / 정보) lý thuyết (theory / 이론), cryptographic randomness, mô hình (model / 모델) selection và lập luận (reasoning / 추론) về dữ liệu ở quy mô hệ thống.

> **Bàn giao:** Sau **Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 formal models reductions and computability](./00_formal_models_reductions_and_computability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
