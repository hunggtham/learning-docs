# Từ mô hình ngôn ngữ tới mô hình ngôn ngữ lớn

**Mô hình ngôn ngữ lớn (Large Language Model — LLM / 대규모 언어 모델)** không phải một loại mô hình xác suất hoàn toàn mới. Cốt lõi vẫn là **mô hình hóa ngôn ngữ (language modeling)**: ước lượng phân bố của token dựa trên ngữ cảnh. Điều thay đổi chủ yếu là **quy mô (scale)** của mô hình, dữ liệu, năng lực tính toán và quá trình hậu huấn luyện (post-training), nhờ đó mô hình học được các biểu diễn có thể tái sử dụng và năng lực rộng hơn nhiều tác vụ đơn lẻ.

Một LLM dạng chỉ-bộ-giải-mã (decoder-only) thường vẫn tối ưu:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

bằng kiến trúc Transformer. Tuy nhiên khi được mở rộng đủ lớn, mô hình tiền huấn luyện (pretrained model) có thể trở thành **mô hình nền tảng (foundation model)** và thích ứng qua prompt, ví dụ trong ngữ cảnh, tinh chỉnh (fine-tuning), tối ưu sở thích (preference optimization) và công cụ (tools).

## “Large” không có một ngưỡng cố định

Không có một số lượng tham số chính thức mà tại đó mô hình ngôn ngữ đột nhiên trở thành LLM. Thuật ngữ này mô tả một chế độ thực tế: mô hình đủ lớn và được huấn luyện trên phạm vi đủ rộng để hỗ trợ nhiều tác vụ và năng lực phía sau.

Chỉ số lượng tham số là chưa đủ. Chất lượng dữ liệu, tổng số token đã huấn luyện, kiến trúc, độ dài ngữ cảnh và hậu huấn luyện đều ảnh hưởng mạnh tới năng lực.

Một mô hình nhỏ hơn nhưng được huấn luyện tốt có thể vượt một mô hình lớn hơn nhưng được huấn luyện kém trên miền mục tiêu cụ thể.

## Tiền huấn luyện tạo mô hình cơ sở

Kho dữ liệu tiền huấn luyện (pretraining corpus) có thể rất lớn, chẳng hạn:

```text
web
sách
mã nguồn
bài báo khoa học
diễn đàn
văn bản đa ngôn ngữ
dữ liệu tổng hợp hoặc đã tuyển chọn
```

Mô hình thường học bằng mục tiêu tự giám sát (self-supervised objective), chẳng hạn dự đoán token tiếp theo.

Kết quả là **mô hình cơ sở (base model)** có khả năng tiếp tục chuỗi văn bản tốt nhưng chưa chắc tuân theo chỉ dẫn của người dùng một cách ổn định.

Trong dữ liệu tiền huấn luyện đã tồn tại nhiều phong cách và dạng tác vụ, vì vậy mô hình có thể hình thành các năng lực tiềm ẩn. Tuy nhiên hành vi mặc định của mô hình cơ sở vẫn gần với việc “tiếp tục chuỗi có xác suất hợp lý”.

## Mô hình nền tảng

**Mô hình nền tảng (foundation model)** là mô hình được tiền huấn luyện trên phạm vi rộng và có thể thích ứng cho nhiều tác vụ phía sau.

LLM thường là mô hình nền tảng tập trung vào văn bản và mã nguồn. Mô hình nền tảng đa phương thức (multimodal foundation model) bổ sung hình ảnh, âm thanh hoặc các dạng dữ liệu khác.

Tính “nền tảng” đến từ khả năng tái sử dụng biểu diễn và năng lực trên nhiều tác vụ, chứ không chỉ từ kích thước.

## Hậu huấn luyện

Hành vi của trợ lý hiện đại thường được hình thành qua **hậu huấn luyện (post-training)**:

```text
Mô hình cơ sở đã tiền huấn luyện
→ tinh chỉnh có giám sát / theo chỉ dẫn
→ tối ưu sở thích như RLHF, DPO...
→ tinh chỉnh an toàn hoặc theo miền
→ huấn luyện sử dụng công cụ
```

Hậu huấn luyện thay đổi phân bố hành vi của mô hình mà không nhất thiết bổ sung lượng tri thức thế giới rộng ngang với giai đoạn tiền huấn luyện.

## Năng lực và hành vi

Một mô hình cơ sở có thể đã có năng lực trả lời một loại câu hỏi nhưng chưa mặc định chọn cách phản hồi hữu ích. **Tinh chỉnh theo chỉ dẫn (instruction tuning)** dạy mô hình thể hiện và sử dụng năng lực theo hành vi mong muốn hơn.

Ngược lại, một tập hậu huấn luyện nhỏ khó tạo ra tri thức sâu hoàn toàn mới nếu biểu diễn và dữ liệu tiền huấn luyện không cung cấp nền tảng cần thiết.

Một mô hình tư duy hữu ích là:

```text
tiền huấn luyện
→ biểu diễn, tri thức và năng lực tổng quát

hậu huấn luyện
→ cách, thời điểm và mức ưu tiên khi thể hiện các hành vi
```

Đây không phải ranh giới tuyệt đối, nhưng giúp phân tích hệ thống rõ hơn.

## Học trong ngữ cảnh

Trong lúc suy luận, prompt có thể chứa mô tả tác vụ và các ví dụ. Trọng số không thay đổi, nhưng hành vi của mô hình thay đổi dựa trên ngữ cảnh. Cơ chế này gọi là **học trong ngữ cảnh (in-context learning)**.

```text
Ví dụ trong prompt
→ Transformer xử lý mẫu quan hệ
→ phần tiếp tục tuân theo tác vụ được suy ra
```

Điều này khác tinh chỉnh:

- học trong ngữ cảnh: tạm thời, chỉ tồn tại trong context hiện tại, không cập nhật trọng số;
- tinh chỉnh: thay đổi tham số và ảnh hưởng được lưu lại trong mô hình.

## Năng lực xuất hiện theo quy mô

Một số năng lực có vẻ xuất hiện đột ngột khi quy mô tăng nếu ta đo bằng metric rời rạc. Tuy nhiên một phần hiện tượng **năng lực nổi lên (emergent capabilities)** có thể đến từ cách đo theo ngưỡng; năng lực tiềm ẩn hoặc loss bên dưới có thể cải thiện liên tục hơn.

Do đó không nên diễn giải hiện tượng này theo hướng huyền bí. Cải thiện liên tục về mô hình có thể tạo thay đổi định tính trong thực tế khi vượt qua ngưỡng để một tác vụ trở nên khả thi.

## Tri thức của LLM trong tham số

Tiền huấn luyện nén cấu trúc thống kê của dữ liệu vào trọng số. Các fact không được lưu như những bản ghi cơ sở dữ liệu có nguồn gốc rõ ràng, mà được phân tán trong tham số và biểu diễn.

Hệ quả là:

- việc nhớ lại có tính xác suất;
- nguồn của một fact không tự động được lưu dưới dạng có thể truy xuất;
- cập nhật tri thức thường cần huấn luyện lại, chỉnh sửa mô hình hoặc truy xuất ngoài;
- các fact hiếm hoặc mâu thuẫn kém ổn định hơn;
- tri thức có thể lỗi thời theo mốc dữ liệu huấn luyện.

RAG giải quyết một phần vấn đề này bằng cách đưa tri thức bên ngoài, có thể cập nhật, vào ngữ cảnh.

## Ngữ cảnh là thông tin làm việc tạm thời

**Cửa sổ ngữ cảnh (context window)** chứa prompt, tài liệu, lịch sử hội thoại và kết quả công cụ. Nó đóng vai trò thông tin làm việc tạm thời mà attention có thể truy cập, khác với trạng thái dài hạn đã được học trong tham số.

Có thể tách bốn loại trạng thái như sau:

```text
Trọng số
→ tri thức và hành vi thống kê đã học, tồn tại lâu dài

Ngữ cảnh
→ thông tin làm việc dành riêng cho request hiện tại

Truy xuất / công cụ
→ tri thức hoặc trạng thái bên ngoài, có thể thay đổi

Hệ thống bộ nhớ
→ trạng thái người dùng / tác vụ được ứng dụng lưu bền vững
```

## LLM không tự động là tác nhân

LLM ánh xạ ngữ cảnh thành token hoặc biểu diễn cho lời gọi công cụ. **Tác nhân (agent)** cần thêm vòng lặp tương tác:

```text
mục tiêu
→ mô hình quyết định
→ công cụ / hành động
→ kết quả từ môi trường
→ cập nhật trạng thái
→ lặp lại
```

LLM có thể là thành phần lập luận hoặc lập kế hoạch, nhưng tác nhân cần lớp điều phối hệ thống (orchestration) bao quanh.

## LLM không tự động là RAG

**RAG (Retrieval-Augmented Generation)** bổ sung bước truy xuất tri thức bên ngoài trước hoặc trong quá trình sinh. Một LLM chỉ trả lời từ tham số của nó không phải là RAG.

Chất lượng RAG phụ thuộc retriever, cách chia đoạn (chunking), xếp hạng lại (reranking), cách xây context và khả năng sử dụng tài liệu của mô hình, chứ không chỉ phụ thuộc LLM.

## Vì sao kiến trúc decoder-only phổ biến?

Kiến trúc chỉ-bộ-giải-mã (decoder-only) trở thành lựa chọn phổ biến cho trợ lý tổng quát vì cùng một giao diện sinh nhân quả có thể xử lý:

```text
hoàn thành văn bản
hội thoại
phân loại dưới dạng sinh
mã nguồn
đầu ra có cấu trúc
lời gọi công cụ
few-shot task
```

Tuy vậy mô hình encoder hoặc encoder–decoder vẫn có thể hiệu quả hơn cho nhiều tác vụ chuyên biệt.

## Mô hình chat là một giao thức trên chuỗi token

Hội thoại thường được tuần tự hóa bằng token hoặc template đặc biệt:

```text
<system> ...
<user> ...
<assistant> ...
```

Mô hình cuối cùng vẫn nhận một chuỗi token. Các vai trò có ý nghĩa vì hậu huấn luyện dạy mô hình phản ứng khác nhau tùy marker và cấu trúc hội thoại.

Thay đổi **chat template** có thể ảnh hưởng đáng kể tới chất lượng và độ an toàn.

## LLM dưới góc nhìn hệ thống

```text
Người dùng / Ứng dụng
↓
Bộ xây prompt và context
↓
Tokenizer
↓
Suy luận Transformer
↓
Logit / sampling / structured decoding
↓
Công cụ / truy xuất / validation nếu có
↓
Đầu ra
```

Trong production, điểm nghẽn chất lượng thường nằm ở xây context, lỗi công cụ, quyền truy cập, độ trễ và đánh giá chứ không chỉ ở mô hình.

## Mô hình tư duy

> LLM là bộ dự đoán chuỗi được tiền huấn luyện ở quy mô lớn, có biểu diễn đủ rộng để tái sử dụng và thích ứng cho nhiều tác vụ ngôn ngữ và mã nguồn; hành vi trợ lý là kết quả của hậu huấn luyện và kiến trúc hệ thống xây trên mô hình đó.

## Những hiểu lầm thường gặp

### “LLM khác mô hình ngôn ngữ vì nó suy luận thay vì dự đoán token”

Suy luận vẫn được thực hiện thông qua việc dự đoán token. Tuy nhiên phép tính bên trong Transformer có thể hỗ trợ những hành vi giống lập luận phức tạp.

### “Nhiều tham số hơn nghĩa là tri thức tăng tuyến tính”

Năng lực phụ thuộc dữ liệu, cách huấn luyện và kiến trúc; số tham số không phải số lượng tri thức.

### “Một mô hình kiểu ChatGPT chỉ là mô hình ngôn ngữ đã tiền huấn luyện”

Hành vi hội thoại hữu ích còn cần hậu huấn luyện, giao thức prompt, lớp an toàn và tích hợp hệ thống.

### “Bộ nhớ của LLM chính là cửa sổ ngữ cảnh”

Ngữ cảnh là đầu vào tạm thời; bộ nhớ bền vững của ứng dụng là một hệ thống khác.

## Liên kết kiến thức

Nên đọc trước: [Language Models](../07_natural_language_processing/02_language_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) và [NLP tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md).

Xem tiếp: [LLM Tokenization](./01_llm_tokenization.md), sau đó là embedding, nội bộ Transformer, tiền huấn luyện và hậu huấn luyện.