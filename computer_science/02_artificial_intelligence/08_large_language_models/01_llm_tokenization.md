# Tokenization cho LLM: độ dài chuỗi, từ vựng và chi phí mô hình

Tokenization cho LLM sử dụng các nguyên lý subword và byte giống NLP truyền thống, nhưng khi mô hình được mở rộng quy mô lớn, nó trở thành vấn đề về **chi phí tính toán, ngân sách ngữ cảnh, công bằng đa ngôn ngữ và khả năng tương thích giao thức**. Tokenizer không chỉ chia văn bản; nó quyết định mô hình phải thực hiện bao nhiêu bước tự hồi quy (autoregressive steps) để biểu diễn hoặc sinh cùng một lượng nội dung.

Xem nền: [Chuẩn hóa văn bản và Tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md). Chapter này tập trung vào các hệ quả dành riêng cho LLM.

## Token là đơn vị tính toán của LLM

Chi phí huấn luyện và suy luận thường tăng theo số token. Nếu cùng một câu được tách thành 20 token thay vì 10, nhiều phép toán theo chiều chuỗi phải xử lý gần gấp đôi số vị trí.

Độ trễ khi sinh tự hồi quy cũng tăng theo số token đầu ra vì các token được sinh tuần tự.

Do đó hiệu quả tokenizer ảnh hưởng trực tiếp tới:

```text
FLOPs khi huấn luyện
mức sử dụng cửa sổ ngữ cảnh
KV cache
độ trễ suy luận
chi phí API theo token
trải nghiệm đa ngôn ngữ
```

## Đánh đổi kích thước từ vựng

Từ vựng lớn có xu hướng:

- tạo chuỗi ngắn hơn;
- làm ma trận embedding và ma trận đầu ra lớn hơn;
- tạo nhiều tham số dành cho token hiếm;
- tăng bộ nhớ và phép tính ở lớp đầu ra/softmax.

Từ vựng nhỏ có xu hướng:

- tái sử dụng subword nhiều hơn;
- tạo chuỗi dài hơn;
- làm ma trận token nhỏ hơn.

Không có một kích thước tối ưu chung. Nó phụ thuộc quy mô mô hình, dữ liệu và tập ngôn ngữ cần hỗ trợ.

## Byte-Level BPE

Nhiều tokenizer kiểu GPT bắt đầu từ byte rồi hợp nhất các chuỗi thường gặp. Cách làm này có thể biểu diễn mọi chuỗi Unicode mà không cần token `<UNK>`.

Tuy nhiên các hệ chữ sử dụng nhiều byte trong UTF-8 có thể cần nhiều đơn vị cơ sở hơn trước khi merge. Nếu một ngôn ngữ xuất hiện ít trong corpus huấn luyện tokenizer, nó cũng có thể nhận ít merge hiệu quả hơn.

## Mật độ token

**Mật độ token (token fertility)** là số token trung bình cần để biểu diễn một từ, ký tự hoặc đơn vị nội dung.

Ngôn ngữ có fertility cao hơn sẽ tiêu tốn nhiều context và compute hơn cho cùng một lượng nội dung ngữ nghĩa.

Trong hệ thống đa ngôn ngữ, nên đo fertility riêng cho tiếng Hàn, tiếng Việt, tiếng Anh và dữ liệu chuyên ngành như code hay tài liệu nội bộ.

## Ảnh hưởng thực tế với tiếng Hàn và tiếng Việt

Tiếng Hàn có nhiều đuôi biến hình; tokenizer tốt có thể tái sử dụng các mẫu stem hoặc morpheme, nhưng hiệu quả phụ thuộc cân bằng corpus.

Tiếng Việt có nhiều từ đa âm tiết được viết bằng các âm tiết tách bởi khoảng trắng. Tokenizer có thể hoặc không merge tốt những biểu thức đa âm tiết phổ biến.

Vì vậy không nên áp dụng máy móc quy tắc kinh nghiệm như “khoảng bốn ký tự trên một token” vốn thường được ước lượng cho tiếng Anh.

## Chat template

Mô hình instruction/chat được hậu huấn luyện với một cách tuần tự hóa hội thoại cụ thể. Ví dụ ở mức trừu tượng:

```text
<|system|>...
<|user|>...
<|assistant|>...
```

Các token đặc biệt phân tách vai trò và lượt hội thoại.

Nếu ứng dụng tự ghép prompt bằng template sai, mô hình sẽ nhận một phân bố đầu vào khác với hậu huấn luyện và có thể hiểu sai vai trò hoặc phản hồi kém ổn định.

Khi có thể, nên dùng đúng tokenizer và chat template chính thức đi cùng checkpoint.

## BOS, EOS và điều kiện dừng

Token bắt đầu/kết thúc chuỗi như **BOS/EOS** ảnh hưởng biên sinh. Một lượt chat có thể dùng token kết thúc lượt khác với token kết thúc tài liệu.

Logic dừng của inference server phải khớp với token hoặc chuỗi dừng của mô hình. Chỉ dừng theo substring có thể cắt nhầm văn bản hợp lệ hoặc bỏ lỡ điểm dừng do khác ranh giới token.

## Token healing và hiệu ứng ranh giới

Nếu prompt kết thúc giữa một từ hoặc tại một mẫu khoảng trắng bất thường, cách token hóa phần cuối có thể khác phân bố mô hình thường thấy khi huấn luyện. Một số hệ thống dùng **token healing** hoặc token hóa lại quanh ranh giới để giảm vấn đề này.

Hiệu ứng này thường quan trọng hơn trong autocomplete và hoàn thành mã nguồn so với chat thông thường.

## Tokenization và số

Số có thể bị tách thành những nhóm chữ số không trực quan. Đây là một phần nguyên nhân khiến LLM yếu ở số học hoặc đếm chính xác: mô hình thao tác trên mẫu token thống kê chứ không làm việc với kiểu dữ liệu số nguyên bản.

Khi cần độ tin cậy cao, phép tính chính xác nên được chuyển cho code, máy tính hoặc công cụ chuyên dụng.

## Dữ liệu có cấu trúc

JSON, XML và mã nguồn có nhiều dấu câu nên có thể tiêu tốn nhiều token. Dạng minified giảm token nhưng đôi khi làm đầu ra khó đọc và khó debug; dạng định dạng đẹp dùng nhiều context hơn.

Thiết kế schema có thể tối ưu cả tính hợp lệ lẫn chi phí token. Tên field dài và lặp lại nhiều lần làm tăng token đầu ra.

## Tokenizer và khả năng tương thích với ma trận embedding

Checkpoint của mô hình phụ thuộc ánh xạ chính xác:

\[
\text{chuỗi token}\leftrightarrow \text{token id}\leftrightarrow \text{hàng embedding}
\]

Đổi tokenizer sẽ phá ngữ nghĩa của embedding dù kích thước vocabulary có giống nhau.

Khi thêm token mới, cần mở rộng ma trận embedding/đầu ra và huấn luyện các hàng mới. Việc cấp một ID mới không tự động dạy mô hình ý nghĩa của token đó.

## Token đặc biệt như một bề mặt tấn công

Nếu văn bản không tin cậy có thể chèn marker vai trò hoặc chuỗi điều khiển đặc biệt và ứng dụng tuần tự hóa kém, thứ bậc chỉ dẫn có thể bị nhiễu.

API chat an toàn hơn nên tách vai trò bằng cấu trúc giao thức và escape/encode dữ liệu người dùng đúng cách thay vì nối thô các chuỗi giả dạng `<system>` hay `<assistant>`.

Vấn đề này nối tokenization với prompt injection và bảo mật ứng dụng LLM.

## Lập ngân sách ngữ cảnh

Với cửa sổ ngữ cảnh `C`:

```text
chỉ dẫn hệ thống
+ lịch sử hội thoại
+ tài liệu truy xuất
+ kết quả công cụ
+ đầu vào người dùng
+ phần dành riêng cho đầu ra
≤ C token
```

Nếu vượt ngân sách, hệ thống cần cắt bớt, tóm tắt hoặc truy xuất chọn lọc. Cắt âm thầm có thể loại bỏ chỉ dẫn hệ thống hoặc bằng chứng quan trọng tùy implementation.

## Prompt caching

Phần prefix được lặp lại có thể được cache bởi inference server hoặc provider để giảm chi phí **prefill**. Cache thường phụ thuộc chính xác chuỗi token, nên chỉ một thay đổi nhỏ trong template cũng có thể làm mất cache hit.

Việc tổ chức system prompt và schema ổn định có thể cải thiện chi phí vận hành.

## Token đầu vào và đầu ra có đặc tính chi phí khác nhau

Giai đoạn **prefill** xử lý token đầu vào với mức song song hóa cao hơn, còn giai đoạn **decode** sinh từng token đầu ra tuần tự.

Do đó cùng số token nhưng đặc tính độ trễ khác nhau. Input dài làm tăng prefill và KV cache; output dài đặc biệt làm tăng độ trễ decode tuần tự.

Tối ưu hệ thống cần phân biệt hai pha này.

## Mô hình tư duy

> Tokenizer là giao diện nhị phân ứng dụng (ABI) giữa chuỗi ký tự của con người và tính toán tensor của LLM. Nó xác định độ mịn của chuỗi, chi phí và các ranh giới giao thức; thay tokenizer gần với thay giao diện mô hình hơn là thay một tùy chọn tiền xử lý văn bản.

## Những hiểu lầm thường gặp

### “Số token gần bằng số từ”

Tỷ lệ thay đổi mạnh theo ngôn ngữ, nội dung và tokenizer.

### “Chất lượng tokenizer chỉ ảnh hưởng chi phí”

Nó còn ảnh hưởng độ dài chuỗi, khả năng chia sẻ hình thái và độ khó khi mô hình học hoặc sinh.

### “Vai trò trong chat chỉ là nhãn văn bản”

Chúng được tuần tự hóa bằng token/template đặc thù mà mô hình đã học trong hậu huấn luyện.

### “Chỉ cần thêm token là mô hình hiểu ngay”

Embedding mới phải được huấn luyện; token ID tự nó không mang ngữ nghĩa.

## Liên kết kiến thức

Xem [NLP Tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) và [Prompting & Context Engineering](./11_prompting_and_context_engineering.md).