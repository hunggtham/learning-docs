# Biểu diễn bài toán (Problem Representation) trong AI

Trước khi một hệ thống AI có thể tìm kiếm, học, suy luận hoặc tối ưu hóa, bài toán phải được chuyển thành một **biểu diễn (representation / 표현)** mà máy có thể thao tác. Đây là bước thường bị xem nhẹ vì nó xuất hiện trước thuật toán, nhưng cách biểu diễn có thể quyết định rất lớn việc bài toán dễ hay khó giải.

Máy không trực tiếp nhận “ý nghĩa”. Nó nhận bit, số, token, tensor, đồ thị hoặc cấu trúc ký hiệu. Vì vậy câu hỏi đầu tiên không nên là “mô hình nào mạnh nhất?”, mà là:

> **Ta đang biểu diễn thế giới như thế nào, và cách biểu diễn đó giữ lại hoặc làm mất thông tin gì?**

## Từ bài toán thực tế tới bài toán tính toán

Giả sử muốn xây hệ thống tìm đường trong Seoul. Thế giới thực gồm đường phố, giao thông, đường một chiều, thời gian, thời tiết, tai nạn và vô số chi tiết khác. Không thể đưa toàn bộ “thế giới thật” nguyên trạng vào thuật toán. Ta phải chọn một **mức trừu tượng (abstraction)** phù hợp.

Một biểu diễn đơn giản có thể là:

```text
Giao lộ       → nút (node)
Đường         → cạnh (edge)
Thời gian đi  → trọng số cạnh
Vị trí hiện tại → nút bắt đầu
Điểm đến        → nút đích
```

Khi đó bài toán thực được chuyển thành bài toán tìm kiếm trên đồ thị (graph search).

Nếu chỉ dùng khoảng cách làm trọng số, hệ thống có thể chọn đường ngắn nhưng đang tắc. Nếu dùng thời gian di chuyển kỳ vọng, biểu diễn phù hợp hơn với mục tiêu “đến nhanh”. Nếu cần tránh đường thu phí, biểu diễn phải thêm ràng buộc hoặc chi phí tương ứng.

Vì vậy, biểu diễn luôn gắn với **mục tiêu và giả định (assumption)** của bài toán.

## Không gian trạng thái (state space)

Trong AI cổ điển, một bài toán thường được mô hình hóa bằng:

- **trạng thái ban đầu (initial state)**;
- **không gian trạng thái (state space)**;
- **hành động hoặc phép biến đổi (actions/operators)**;
- **mô hình chuyển trạng thái (transition model)**;
- **điều kiện đích (goal test)**;
- **chi phí đường đi (path cost)** nếu cần.

Ví dụ với trò chơi 8-puzzle, mỗi cách sắp xếp các ô là một trạng thái. Di chuyển một ô tạo ra trạng thái mới. Thuật toán tìm kiếm không cần biết puzzle là “đồ chơi”; nó chỉ cần biểu diễn trạng thái và quy tắc chuyển trạng thái.

Không gian trạng thái có thể cực lớn. Chỉ với `n` biến nhị phân đã có tới:

\[
2^n
\]

trạng thái có thể xảy ra. Đây là nguồn gốc của **bùng nổ tổ hợp (combinatorial explosion / 조합 폭발)**.

Một biểu diễn tốt đôi khi giảm không gian tìm kiếm nhiều hơn việc thay một thuật toán tìm kiếm bằng thuật toán khác.

## Đặc trưng trong học máy

Trong học máy cổ điển, dữ liệu đầu vào thường được biểu diễn thành **vector đặc trưng (feature vector)**:

\[
\mathbf{x} = [x_1, x_2, \dots, x_d]
\]

Ví dụ, mô hình đánh giá rủi ro tín dụng có thể sử dụng các đặc trưng như:

```text
tuổi
thu nhập
số tiền vay
tỷ lệ nợ
độ dài lịch sử thanh toán
số lần trả chậm
```

Mô hình không nhìn thấy “khách hàng” như con người. Nó nhìn thấy một vector số.

**Kỹ thuật đặc trưng (feature engineering)** là quá trình thiết kế biểu diễn hữu ích từ dữ liệu thô. Nếu biểu diễn không chứa tín hiệu cần thiết, mô hình tốt đến đâu cũng khó học được ánh xạ mong muốn.

## Học biểu diễn (representation learning)

Học sâu thay đổi cách xây dựng biểu diễn. Thay vì kỹ sư tự chọn mọi đặc trưng, mô hình có thể học các biểu diễn trung gian trực tiếp từ dữ liệu.

Một mô hình phân loại ảnh có thể biến đổi dữ liệu theo chuỗi khái niệm:

```text
điểm ảnh
  ↓
cạnh / kết cấu cục bộ
  ↓
hình dạng / bộ phận
  ↓
đặc trưng thị giác trừu tượng hơn
  ↓
dự đoán lớp
```

Đây không phải hệ phân cấp cố định tuyệt đối, nhưng cho thấy ý tưởng chính: các tầng ẩn biến dữ liệu ban đầu thành những không gian biểu diễn thuận lợi hơn cho nhiệm vụ.

Trong xử lý ngôn ngữ tự nhiên (NLP), mã token được ánh xạ thành **vector nhúng (embedding vector / 임베딩 벡터)**. Transformer tiếp tục biến các vector này thành **biểu diễn theo ngữ cảnh (contextual representation)**, nghĩa là cùng một từ có thể có biểu diễn khác nhau tùy câu và vị trí xung quanh.

## Biểu diễn ký hiệu (symbolic representation)

Không phải mọi biểu diễn đều là vector. Tri thức có thể được biểu diễn bằng ký hiệu, vị từ, quy tắc hoặc đồ thị.

Ví dụ:

```text
works_for(Alice, CompanyA)
located_in(CompanyA, Seoul)
```

Một đồ thị tri thức (knowledge graph) có thể biểu diễn thực thể và quan hệ:

```text
Alice ──works_for──> CompanyA ──located_in──> Seoul
```

Biểu diễn ký hiệu có lợi khi cấu trúc và quan hệ cần ngữ nghĩa tường minh. Biểu diễn vector phù hợp khi cần đo độ tương đồng, học mẫu và tối ưu hóa khả vi. Hệ thống lai có thể kết hợp cả hai.

## Phân phối xác suất như một dạng biểu diễn

Khi bất định quan trọng, trạng thái không nên bị ép thành một sự thật duy nhất mà có thể được biểu diễn bằng **phân phối xác suất (probability distribution)**.

Ví dụ, hệ thống định vị chưa chắc robot đang ở đâu:

\[
P(Location = A)=0.6
\]
\[
P(Location = B)=0.3
\]
\[
P(Location = C)=0.1
\]

Biểu diễn này giữ lại sự bất định thay vì buộc hệ thống chọn một đáp án quá sớm.

Đây là nền tảng của suy luận Bayes, mô hình trạng thái ẩn và robotics xác suất.

## Biểu diễn chuỗi (sequence representation)

Ngôn ngữ, âm thanh và chuỗi thời gian đều có thứ tự. Nếu chỉ xem các phần tử như một tập hợp không thứ tự, ta làm mất thông tin quan trọng.

Ví dụ:

```text
Dog bites man
```

khác về ý nghĩa với:

```text
Man bites dog
```

mặc dù chứa cùng các từ.

Vì vậy mô hình chuỗi cần mã hóa thứ tự bằng cơ chế hồi quy, thông tin vị trí hoặc kiến trúc tương đương. Transformer không có hồi quy tự nhiên như RNN nên cần **biểu diễn vị trí (positional representation/encoding)** để biết thứ tự token.

## Biểu diễn đồ thị (graph representation)

Khi mối quan hệ quan trọng hơn vị trí trong một chuỗi, đồ thị là phép trừu tượng tự nhiên.

Mạng xã hội, phân tử, mạng đường bộ, đồ thị phụ thuộc và đồ thị tri thức đều có thể biểu diễn bằng:

\[
G=(V,E)
\]

trong đó `V` là tập đỉnh hoặc nút và `E` là tập cạnh.

Biểu diễn đồ thị cho phép suy luận về tính liên thông, lân cận, đường đi ngắn nhất, độ trung tâm và truyền thông điệp (message passing).

## Biểu diễn liên tục và không gian nhúng

Phép nhúng (embedding) đưa một đối tượng rời rạc vào không gian vector liên tục:

\[
f: Object \rightarrow \mathbb{R}^d
\]

Nếu mục tiêu huấn luyện được thiết kế phù hợp, quan hệ ngữ nghĩa có thể được phản ánh một phần bằng hình học trong không gian vector. Hai tài liệu có ý nghĩa gần nhau có thể có độ tương đồng cosine cao hơn.

Đây là nền tảng của tìm kiếm ngữ nghĩa, hệ thống gợi ý và RAG.

Tuy nhiên, không nên xem không gian nhúng là “bản đồ hoàn hảo của ý nghĩa”. Hình học của nó phụ thuộc vào mô hình, dữ liệu và mục tiêu huấn luyện. Thước đo tương đồng chỉ có ý nghĩa trong ngữ cảnh của biểu diễn đó.

## Biểu diễn mất mát và không mất mát

Một biểu diễn có thể làm mất thông tin. Đây là **biểu diễn mất mát (lossy representation)**.

Ví dụ, giảm kích thước ảnh từ `4000×3000` xuống `224×224` làm mất chi tiết. Tách token có thể chia từ hiếm thành nhiều mảnh nhỏ. Gộp nhật ký sự kiện theo ngày có thể làm mất thứ tự thời gian ở mức phút.

Mất thông tin không nhất thiết là xấu. Nén có thể loại bỏ chi tiết không cần thiết và khiến bài toán có thể xử lý được. Câu hỏi đúng là: **thông tin bị mất có quan trọng đối với nhiệm vụ hay không?**

## Tính bất biến (invariance)

Một biểu diễn tốt thường cố phản ánh những phép biến đổi không nên làm thay đổi ý nghĩa của nhiệm vụ.

Ví dụ, mô hình nhận diện vật thể lý tưởng vẫn nên nhận ra cùng một vật thể khi nó dịch chuyển nhẹ trong ảnh. Đây liên quan đến **tính bất biến hoặc hiệp biến theo phép tịnh tiến (translation invariance/equivariance)** của mạng tích chập (CNN).

Trong văn bản, ý nghĩa đôi khi nên bất biến trước thay đổi định dạng hoặc khoảng trắng, nhưng không thể bất biến hoàn toàn trước thay đổi thứ tự từ.

Vì vậy thiết kế biểu diễn luôn gắn với các giả định về tính bất biến.

## Số chiều và lời nguyền số chiều

Vector có quá nhiều chiều làm tăng chi phí tính toán và độ khó thống kê. Đây là bối cảnh của **lời nguyền số chiều (curse of dimensionality)**.

Khi số chiều tăng, dữ liệu trở nên thưa hơn trong không gian. Khoảng cách giữa các điểm cũng có thể kém phân biệt hơn. Các kỹ thuật giảm chiều như PCA cố giữ lại phần biến thiên quan trọng trong một không gian nhỏ hơn.

Học biểu diễn sâu cũng thường tạo **không gian tiềm ẩn (latent space)** có cấu trúc hữu ích hơn dữ liệu thô.

## Biểu diễn và lược đồ cơ sở dữ liệu

Trong kỹ nghệ phần mềm, **lược đồ cơ sở dữ liệu (database schema)** cũng là một dạng biểu diễn của miền nghiệp vụ. Một ứng dụng AI thường phải đi qua nhiều dạng biểu diễn:

```text
Hàng trong CSDL quan hệ
    ↓
Đối tượng ứng dụng
    ↓
Văn bản tuần tự hóa / lời nhắc có cấu trúc
    ↓
Token
    ↓
Vector nhúng / trạng thái ẩn
    ↓
Đầu ra mô hình
    ↓
Trạng thái ứng dụng có cấu trúc
```

Lỗi có thể xuất hiện ở ranh giới giữa các biểu diễn, chứ không chỉ trong mô hình. Ví dụ, nếu cơ sở dữ liệu lưu thời gian sai múi giờ, mô hình phía sau có thể suy luận sai dù bản thân mô hình hoạt động đúng.

## Biểu diễn và hàm mục tiêu cùng quyết định việc học

Mô hình không tự nhiên học “ý nghĩa”. Nó học biểu diễn giúp giảm **hàm mục tiêu (objective)** mà quá trình huấn luyện yêu cầu.

Nếu học tương phản (contrastive learning) kéo các cặp dương lại gần nhau và đẩy các cặp âm ra xa, hình học của không gian nhúng sẽ phản ánh chính mục tiêu đó.

Nếu mô hình ngôn ngữ được huấn luyện bằng dự đoán token tiếp theo, biểu diễn ẩn của nó cũng được định hình bởi nhiệm vụ dự đoán token tiếp theo.

Do đó:

```text
Dữ liệu + Kiến trúc + Hàm mục tiêu → Biểu diễn đã học
```

Không nên tách cách biểu diễn khỏi mục tiêu huấn luyện.

## Mô hình tư duy (mental model)

Hãy nghĩ biểu diễn như **API giữa thế giới và thuật toán**.

API tốt làm lộ ra đúng thông tin ở mức trừu tượng phù hợp. API tệ che mất tín hiệu cần thiết hoặc đưa vào quá nhiều chi tiết không liên quan.

Khi mô hình thất bại, đừng chỉ hỏi “cần mô hình lớn hơn không?”. Hãy hỏi liệu cách biểu diễn có đang làm bài toán khó hơn một cách không cần thiết hay không.

## Các hiểu lầm thường gặp

### “Dữ liệu thô luôn tốt nhất vì mô hình tự học được mọi thứ”

Không đúng trong mọi trường hợp. Học đầu-cuối (end-to-end learning) có thể rất mạnh nhưng cần dữ liệu, năng lực tính toán và kiến trúc phù hợp. Ràng buộc miền hoặc đặc trưng có cấu trúc đôi khi cải thiện hiệu quả sử dụng mẫu và độ tin cậy.

### “Embedding = ý nghĩa”

Phép nhúng là một biểu diễn số đã được học để phục vụ một mục tiêu. Nó có thể nắm bắt nhiều quy luật ngữ nghĩa nhưng không đồng nghĩa với “ý nghĩa tuyệt đối”.

### “Càng nhiều đặc trưng càng tốt”

Đặc trưng không liên quan có thể làm tăng nhiễu, chi phí, nguy cơ quá khớp và rò rỉ dữ liệu. Chất lượng biểu diễn quan trọng hơn số lượng đặc trưng đơn thuần.

## Liên kết kiến thức

Biểu diễn bài toán nối trực tiếp với cấu trúc dữ liệu, đại số tuyến tính, xác suất, lý thuyết thông tin, thiết kế cơ sở dữ liệu, xử lý tín hiệu và kiến trúc phần mềm. Đây là lý do AI không thể tách khỏi nền tảng khoa học máy tính.

Xem tiếp: [Kiến trúc hệ thống AI](./04_ai_system_architecture.md).