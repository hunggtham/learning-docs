# Tư duy toán học và nguyên lý nền tảng (first principles / 제일 원리)

> **Mạch đọc:** Đọc **Tư duy toán học và nguyên lý nền tảng (first principles / 제일 원리)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Từ hiện tượng đến mô hình** sang **Đại lượng, trạng thái và quan hệ**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Toán học (Mathematics / 수학) không bắt đầu từ công thức. Nó bắt đầu từ một câu hỏi đơn giản hơn: khi thế giới quá phức tạp để suy nghĩ trực tiếp, ta có thể giữ lại những đặc điểm nào để vẫn mô tả được vấn đề một cách chính xác? Một chiếc xe đang chạy, một khoản vay ngân hàng, một tín hiệu mạng, một ảnh kỹ thuật số và một mô hình machine học tập (learning / 학습) trông hoàn toàn khác nhau, nhưng tất cả đều có thể được mô tả bằng đại lượng, quan hệ, quy tắc biến đổi và bất định. Toán học là ngôn ngữ để xây những mô hình như vậy và suy luận bên trong chúng.

## Từ hiện tượng đến mô hình

Một mô hình toán học (Mathematical model / 수학적 모델) là một biểu diễn có chủ ý. Nó không cố giữ mọi chi tiết của thực tế; nó giữ những chi tiết cần thiết cho câu hỏi đang hỏi. Nếu ta muốn dự đoán thời gian một xe đi từ A đến B, màu sơn thường không quan trọng. Vận tốc, quãng đường, điều kiện giao thông lại quan trọng. Khi ta viết

```math
t = \frac{s}{v}
```

điều đó không có nghĩa mọi chuyến đi ngoài đời đều tuân theo công thức này. Công thức ngầm giả định vận tốc `v` là không đổi hoặc `v` đại diện cho vận tốc trung bình thích hợp. Nếu xe tăng tốc, dừng đèn đỏ hoặc thay đổi đường đi, mô hình phải được sửa.

Đây là một mental habit quan trọng: trước khi dùng công thức, hãy hỏi mô hình đang giữ cái gì, bỏ cái gì và điều kiện nào làm nó còn đúng.

## Đại lượng, trạng thái và quan hệ

Một đại lượng (Quantity / 양) là một thuộc tính có thể được mô tả bằng giá trị. Khối lượng, thời gian, số yêu cầu (request / 요청) mỗi giây, nhiệt độ và số tiền đều là đại lượng. Khi một đại lượng thay đổi, ta thường biểu diễn nó bằng biến (Variable / 변수). Ví dụ `T(t)` có thể là nhiệt độ phụ thuộc vào thời gian.

Khi hai hay nhiều đại lượng liên hệ với nhau, toán học tìm cách mô tả cấu trúc của liên hệ đó. Phương trình (Equation / 방정식) mô tả một ràng buộc; hàm số (Function / 함수) mô tả quy tắc biến đầu vào (input / 입력) thành đầu ra (output / 출력); véc-tơ (vector / 벡터) gom nhiều thành phần thành một đối tượng có cấu trúc; ma trận (Matrix / 행렬) có thể biểu diễn phép biến đổi tuyến tính; xác suất (Probability / 확률) mô tả bất định trong một mô hình.

Điểm quan trọng là các ký hiệu không phải chính hiện tượng. `x`, `f(x)` hay `A` chỉ là cách nén thông tin để suy luận dễ hơn.

## Lớp trừu tượng (abstraction / 추상화): bỏ chi tiết để thấy cấu trúc

Trừu tượng hóa (Abstraction / 추상화) là quá trình tách cấu trúc chung khỏi trường hợp cụ thể. Trong lập trình, một `List<T>` cho phép ta suy nghĩ về thao tác trên danh sách mà không cần quan tâm phần tử là `String` hay `User`. Trong toán học, khái niệm hàm cho phép ta suy nghĩ về đầu vào (input / 입력), đầu ra (output / 출력) và composition mà không cần quan tâm ngay hàm đó là `x^2`, `sin x` hay một neural mạng (network / 네트워크).

Lớp trừu tượng (abstraction / 추상화) chỉ hữu ích khi ta nhớ nó dựa trên các giả định (assumptions / 가정들) nào. Ví dụ mô hình Euclid giả định không gian phẳng. Trên bề mặt Trái Đất, đường ngắn nhất giữa hai điểm là cung của great circle chứ không phải đoạn thẳng Euclid trên bản đồ phẳng.

## Suy diễn, quy nạp và kiểm chứng

Suy diễn (Deduction / 연역) bắt đầu từ tiền đề rồi dùng luật lô-gic (logic / 논리) để đi đến kết luận bắt buộc. Nếu mọi số chẵn đều chia hết cho 2 và `n` là số chẵn, thì `n` chia hết cho 2. Khi một chứng minh toán học đúng, kết luận không chỉ “thường đúng”; nó phải đúng trong hệ các giả định (assumptions / 가정들) đã chọn.

Quy nạp theo nghĩa khoa học (Induction / 귀납) quan sát nhiều trường hợp rồi đoán quy luật. Nếu ta tính `1+3=4`, `1+3+5=9`, `1+3+5+7=16`, ta có thể đoán rằng tổng `n` số lẻ đầu tiên bằng `n^2`. Nhưng quan sát không phải chứng minh. Ta cần một argument tổng quát, chẳng hạn mathematical induction hoặc một lập luận hình học.

Trong dữ liệu (data / 데이터) science, khác biệt này rất quan trọng. Một mẫu (pattern / 패턴) xuất hiện trong dữ liệu không tự động trở thành quy luật tất định của thế giới. Nó có thể do sampling độ lệch (bias / 편향), confounding hoặc noise.

## Proof: tại sao toán cần chứng minh?

Chứng minh (Proof / 증명) là chuỗi lập luận cho thấy kết luận bắt buộc đi theo từ các giả định (assumptions / 가정들) và định nghĩa. Một proof tốt không chỉ xác nhận kết quả mà còn giải thích cơ chế.

Ví dụ, tổng hai số lẻ luôn chẵn. Viết hai số lẻ bất kỳ dưới dạng

```math
2a+1, \qquad 2b+1
```

với `a,b` là số nguyên. Tổng là

```math
(2a+1)+(2b+1)=2(a+b+1)
```

nên chia hết cho 2. Ta không cần kiểm tra từng cặp số lẻ vì biểu diễn (representation / 표현) `2k+1` đã capture toàn bộ cấu trúc “lẻ”.

## Counterexample và vai trò của một trường hợp phản chứng

Một phát biểu dạng “mọi X đều có tính chất P” chỉ cần một counterexample để bị bác bỏ. Nếu ai đó nói “mọi số nguyên tố đều lẻ”, số 2 đủ để chứng minh phát biểu sai.

Đây là tư duy cực hữu ích trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학). Khi một yêu cầu (requirement / 요구사항) nói “hàm (function / 함수) này luôn trả về giá trị hợp lệ”, ta nên cố tìm đầu vào (input / 입력) phá vỡ claim: `null`, empty danh sách (list / 목록), overflow, negative đầu vào (input / 입력), timezone ranh giới (boundary / 경계). Testing tốt thường mang tinh thần counterexample tìm kiếm (search / 검색).

## Bất biến (invariant / 불변식): thứ không đổi trong quá trình biến đổi

Bất biến (Invariant / 불변량) là tính chất vẫn giữ nguyên khi hệ thống trải qua một nhóm biến đổi. Trong hình học, khoảng cách được bảo toàn dưới phép quay và tịnh tiến. Trong thuật toán (algorithm / 알고리즘), một vòng lặp (loop / 루프) bất biến (invariant / 불변식) là mệnh đề đúng trước và sau mỗi vòng lặp; nó giúp chứng minh thuật toán đúng.

Ví dụ tìm kiếm nhị phân (binary search / 이진 탐색) duy trì bất biến (invariant / 불변식) rằng nếu mục tiêu (target / 대상) còn tồn tại trong vùng chưa loại bỏ, nó nằm trong interval `[low, high]`. Mỗi bước giảm interval nhưng bảo toàn bất biến (invariant / 불변식) đó. Khi interval rỗng, ta kết luận mục tiêu (target / 대상) không tồn tại.

## Dimensional phân tích (analysis / 분석): đơn vị là một phần của lô-gic (logic / 논리)

Phân tích thứ nguyên (Dimensional analysis / 차원 해석) giúp phát hiện công thức vô lý trước khi tính số. Nếu quãng đường có đơn vị mét và thời gian có đơn vị giây, vận tốc phải có đơn vị `m/s`.

Nếu ai đó viết

```math
s = v + t
```

thì dù các số có thể cộng được trong calculator, biểu thức không có nghĩa vật lý vì `m/s` không cộng trực tiếp với `s`.

Trong mã (code / 코드), điều này tương tự hệ kiểu (type system / 타입 시스템). Một số thư viện sử dụng type-safe units để tránh cộng `Meters` với `Seconds` giống như trình biên dịch (compiler / 컴파일러) ngăn cộng `LocalDate` với một đối tượng (object / 객체) không phù hợp.

## Approximation và lỗi (error / 오류)

Thực tế hiếm khi cho dữ liệu vô hạn độ chính xác. Vì vậy xấp xỉ (Approximation / 근사) không phải phiên bản “kém” của toán; nó là phần thiết yếu của toán ứng dụng.

Nếu `π≈3.14`, sai số tuyệt đối là

```math
|\pi-3.14|
```

còn sai số tương đối là

```math
\frac{|\pi-3.14|}{|\pi|}
```

Hai phép đo trả lời hai câu hỏi khác nhau. Sai số tuyệt đối đo chênh lệch trực tiếp; sai số tương đối đo chênh lệch so với quy mô của giá trị thật.

Trong numerical computing, floating-point arithmetic có thể tạo rounding lỗi (error / 오류). Vì vậy `0.1 + 0.2` trong nhiều ngôn ngữ không biểu diễn chính xác `0.3` theo nhị phân (binary / 이진) floating điểm (point / 지점). Đây không phải “bug của toán”; nó là hệ quả của việc biểu diễn một tập vô hạn số thực bằng hữu hạn bit.

## First-Principles Thinking

Tư duy nguyên lý đầu tiên (First-Principles Thinking / 제1원리 사고) không có nghĩa phải chứng minh mọi định lý từ axioms mỗi lần. Nó có nghĩa khi gặp một quy tắc, ta cố truy về những các giả định (assumptions / 가정들) và quan hệ cơ bản khiến quy tắc đó đúng.

Với lãi kép, thay vì học thuộc

```math
A=P(1+r)^n
```

hãy bắt đầu từ quá trình: mỗi chu kỳ, số dư mới bằng số dư cũ nhân với `1+r`. Sau một chu kỳ:

```math
A_1=P(1+r)
```

sau hai chu kỳ:

```math
A_2=P(1+r)^2
```

và lặp `n` lần cho

```math
A_n=P(1+r)^n
```

Exponential growth xuất hiện vì cùng một multiplicative transformation được lặp lại.

## Liên kết kiến thức (knowledge connection / 지식 연결): cùng một cấu trúc dưới nhiều tên

Một trong những kỹ năng toán quan trọng nhất là nhận ra cấu trúc quen thuộc trong bối cảnh mới. tỷ lệ (rate / 비율) of thay đổi (change / 변경) xuất hiện thành slope trong hình học tọa độ, derivative trong calculus, velocity trong physics, marginal chi phí (cost / 비용) trong economics và độ dốc (gradient / 기울기) trong machine học tập (learning / 학습). Accumulation xuất hiện thành tổng hữu hạn, integral, cumulative xác suất (probability / 확률) và compound growth. Distance xuất hiện thành độ dài đoạn thẳng, véc-tơ (vector / 벡터) norm, lỗi (error / 오류) chỉ số (metric / 지표) và mất mát (loss / 손실).

Khi thấy một khái niệm mới, đừng chỉ hỏi “định nghĩa là gì?”. Hãy hỏi “nó có cùng cấu trúc với thứ gì mình đã biết?”.

## Mô hình tư duy (mental model / 사고 모델)

> Toán học là quá trình nén một vấn đề thành những đối tượng và quan hệ đủ chính xác để ta có thể suy luận mà không phải mang toàn bộ thế giới thật vào đầu. Một công thức chỉ là phần cuối của quá trình; phần quan trọng hơn là các giả định (assumptions / 가정들), cấu trúc và lô-gic (logic / 논리) dẫn đến nó.

## Dùng chung (common / 공통) Misconceptions

Một hiểu lầm phổ biến là toán học đồng nghĩa với tính toán nhanh. Tính toán chỉ là một phần. Nhiều bài toán khó nhất không khó vì phép nhân hay phép chia, mà vì phải chọn biểu diễn (representation / 표현) đúng.

Một hiểu lầm khác là “công thức luôn đúng”. Công thức đúng trong mô hình (model / 모델) và các giả định (assumptions / 가정들) của nó. `s=vt` không mô tả chính xác chuyển động có vận tốc thay đổi; normal phân phối (distribution / 분포) không mô tả mọi loại dữ liệu; tuyến tính (linear / 선형) regression không biến correlation thành causation.

Cuối cùng, việc máy tính cho một con số không có nghĩa câu trả lời có ý nghĩa. Nếu mô hình (model / 모델) sai, đơn vị (unit / 단위) sai hoặc dữ liệu (data / 데이터) biased, precision của calculator không cứu được kết luận.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 logic and proof](./01_logic_and_proof.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
