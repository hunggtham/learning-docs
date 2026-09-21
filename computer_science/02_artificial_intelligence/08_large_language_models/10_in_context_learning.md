# Học trong ngữ cảnh

**Học trong ngữ cảnh (In-Context Learning — ICL / 문맥 내 학습)** là hiện tượng mô hình thay đổi hành vi dựa trên ví dụ hoặc chỉ dẫn nằm trong context **mà không cần cập nhật trọng số**.

Ví dụ:

```text
Input: 2 + 3
Output: five

Input: 4 + 1
Output: five

Input: 7 + 2
Output:
```

Mô hình có thể suy ra pattern rằng đầu ra cần viết bằng chữ và trả `nine` dù không có bước gradient nào xảy ra.

## “Học” nhưng không cập nhật tham số

Tên gọi dễ gây nhầm. Trong ICL, trọng số mô hình giữ nguyên trong phiên inference. Thứ thay đổi là trạng thái ẩn và pattern attention được điều kiện hóa bởi context.

Do đó cần phân biệt:

```text
Học trong training → cập nhật tham số
Học trong context  → hành vi tạm thời được điều kiện hóa bởi prompt/context
```

Khi context kết thúc, sự thích ứng đó không được lưu vĩnh viễn vào trọng số.

## Zero-shot, one-shot và few-shot

**Zero-shot** chỉ cung cấp instruction mà không có ví dụ.

**One-shot** cung cấp một demonstration.

**Few-shot** cung cấp một vài demonstration để mô hình suy ra tác vụ hoặc format.

Few-shot đặc biệt hữu ích khi một tác vụ khó mô tả bằng quy tắc nhưng dễ minh họa bằng ví dụ.

## Demonstration truyền thông tin gì?

Một demonstration có thể truyền nhiều loại thông tin cùng lúc:

- ánh xạ của tác vụ;
- định dạng đầu ra;
- ngữ nghĩa của label;
- tone và style;
- cách xử lý edge case;
- pattern giải quyết vấn đề hoặc reasoning.

Vì vậy chất lượng ví dụ quan trọng hơn chỉ số lượng.

## Nhạy với thứ tự

ICL có thể nhạy với thứ tự các ví dụ. Ví dụ xuất hiện gần cuối đôi khi ảnh hưởng mạnh hơn, mất cân bằng label có thể làm output bị bias và một demonstration xấu có thể kéo mô hình theo hướng sai.

Vì vậy đánh giá prompt nên thử nhiều tập ví dụ và thứ tự khác nhau thay vì chỉ dùng một prompt được viết thủ công.

## Ngữ nghĩa của label

Nếu label là chuỗi tùy ý như `A`, `B`, `C`, few-shot example giúp mô hình ánh xạ class ngữ nghĩa sang token label.

Nếu label trong ví dụ sai, mô hình có thể làm theo demonstration thay vì prior nội bộ.

Do đó ICL vừa là năng lực vừa là bề mặt tấn công: context độc hại có thể điều hướng hành vi.

## Context như một chương trình tạm thời

Một mô hình tư duy hữu ích là xem prompt như một **chương trình tạm thời (temporary program)**:

```text
chỉ dẫn
+ ví dụ
+ fact được truy xuất
+ kết quả công cụ
→ context tính toán tạm thời
```

Trọng số mô hình đóng vai trò bộ diễn giải đã học; context định nghĩa trạng thái và tác vụ cục bộ.

So sánh này không hoàn hảo vì việc thực thi LLM có tính xác suất và không có ngữ nghĩa hình thức như ngôn ngữ lập trình, nhưng rất hữu ích trong system design.

## Vì sao ICL xuất hiện?

Trong pretraining, mô hình thấy rất nhiều văn bản nơi phần trước thiết lập quy ước cục bộ cho phần sau: hướng dẫn, ví dụ, hội thoại, code và chuỗi question–answer. Transformer học cách dùng context để dự đoán token tiếp theo theo các quy ước đó.

Quy mô và độ đa dạng tác vụ làm năng lực này mạnh hơn. Cơ chế chi tiết vẫn là chủ đề nghiên cứu, nhưng engineering không cần giả định rằng mô hình đang chạy một vòng gradient descent ẩn bên trong.

## ICL và fine-tuning

ICL phù hợp khi tác vụ thay đổi nhanh, số ví dụ ít, cần triển khai không qua training hoặc cần tùy chỉnh theo từng phiên.

Fine-tuning phù hợp khi hành vi phải nhất quán trên rất nhiều request và pattern tương đối ổn định.

Đánh đổi:

```text
ICL
→ linh hoạt, không cập nhật trọng số, tốn token context

Fine-tuning
→ hành vi bền vững, có chi phí training, giảm overhead prompt
```

## ICL và RAG

RAG đưa **tri thức hoặc bằng chứng bên ngoài** vào context. ICL đưa ví dụ và instruction để định nghĩa **hành vi tác vụ**.

Một ứng dụng RAG có thể dùng cả hai:

```text
few-shot examples
+ tài liệu được truy xuất
+ câu hỏi người dùng
→ câu trả lời
```

## Context dài không miễn phí

Few-shot example tiêu tốn context window và chi phí inference. Quá nhiều ví dụ có thể làm loãng thông tin quan trọng hoặc đẩy nội dung cần thiết ra khỏi cửa sổ.

Do đó việc chọn example trở thành một bài toán retrieval: chọn demonstration liên quan nhất thay vì nhét toàn bộ dữ liệu vào prompt.

## Chọn few-shot động

Có thể embedding query của người dùng, truy xuất các ví dụ có nhãn tương tự rồi đưa chúng vào prompt. Đây là cách kết hợp retrieval với ICL.

Tuy nhiên similarity không phải lúc nào cũng đồng nghĩa “ví dụ tốt nhất”. Trong một số tác vụ, độ đa dạng hoặc độ bao phủ quan trọng hơn nearest neighbor.

## Nhiễm chỉ dẫn trong context

Tài liệu truy xuất hoặc text do người dùng cung cấp có thể chứa instruction. Nếu ứng dụng trộn dữ liệu và chỉ dẫn mà không có ranh giới rõ, mô hình có thể làm theo nội dung không đáng tin.

Khả năng học từ context chính là một lý do **prompt injection** nguy hiểm: mô hình vốn được huấn luyện để điều chỉnh hành vi theo ngữ cảnh.

## ICL và reasoning

Few-shot example có lời giải từng bước có thể cải thiện một số tác vụ bằng cách minh họa pattern phân rã vấn đề. Tuy nhiên mô hình cũng có thể chỉ sao chép phong cách bề mặt mà không duy trì logic đúng.

Đánh giá cần kiểm tra tính đúng của câu trả lời chứ không chỉ sự xuất hiện của văn bản “trông giống reasoning”.

## Mô hình tư duy

> In-context learning là **sự thích ứng tạm thời thông qua ngữ cảnh**, không phải cập nhật tham số.

Mô hình đọc prompt vừa như dữ liệu vừa như đặc tả tác vụ, vì vậy thiết kế context là một phần của việc lập trình hệ thống AI.

## Những hiểu lầm thường gặp

### “Few-shot example huấn luyện mô hình ngay lúc inference”

Không có cập nhật trọng số tiêu chuẩn. Thay đổi hành vi đến từ context conditioning.

### “Càng nhiều ví dụ càng tốt”

Không. Chi phí context, trùng lặp và ví dụ mâu thuẫn có thể làm chất lượng giảm.

### “Long context thay thế fine-tuning”

Không. Điều kiện hóa theo phiên và hành vi bền vững giải quyết những vấn đề khác nhau.

## Liên kết kiến thức

ICL nối [Pretraining](./04_pretraining.md), [Attention/Transformer](../06_deep_learning_architectures/04_attention.md), RAG và quản lý context của Agent.

Xem tiếp: [Prompting and Context Engineering](./11_prompting_and_context_engineering.md).