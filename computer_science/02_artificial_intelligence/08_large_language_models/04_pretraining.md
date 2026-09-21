# Tiền huấn luyện của mô hình ngôn ngữ lớn

**Tiền huấn luyện (pretraining / 사전학습)** là giai đoạn mô hình học cấu trúc thống kê từ lượng dữ liệu rất lớn trước khi được điều chỉnh để làm theo chỉ dẫn hoặc phục vụ một ứng dụng cụ thể. Với LLM chỉ-bộ-giải-mã (decoder-only), mục tiêu phổ biến là **dự đoán token tiếp theo (next-token prediction)**: tại mỗi vị trí, mô hình nhận phần tiền tố và tối đa hóa xác suất của token tiếp theo.

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Hàm mất mát tương ứng thường là negative log-likelihood hoặc cross-entropy:

\[
\mathcal L=-\sum_t \log P_\theta(x_t\mid x_{<t})
\]

Mục tiêu nhìn có vẻ đơn giản nhưng buộc mô hình phải nén rất nhiều quy luật của ngôn ngữ và thế giới vào tham số. Muốn dự đoán token tốt, mô hình phải học cú pháp, liên hệ ngữ nghĩa, cấu trúc diễn ngôn, sự đồng xuất hiện của fact, mẫu mã nguồn và nhiều dạng cấu trúc lập luận có trong phân bố huấn luyện.

## Tiền huấn luyện không phải nạp dữ liệu vào cơ sở dữ liệu

Mô hình không biến corpus thành một key-value store hoàn hảo. Huấn luyện cập nhật hàng tỷ tham số để phân bố đầu ra phù hợp dữ liệu. Tri thức vì vậy được **phân tán (distributed)** trong trọng số và biểu diễn.

Điều này giúp mô hình khái quát hóa, diễn đạt lại và kết hợp mẫu thay vì chỉ phát lại nguyên văn chuỗi huấn luyện. Đồng thời nó cũng giải thích vì sao truy xuất từ tham số không đáng tin như truy vấn cơ sở dữ liệu: tri thức trong tham số không tự có bảo đảm về độ mới, nguồn gốc hay khả năng tra cứu chính xác.

## Pipeline dữ liệu là một phần của mô hình

Chất lượng tiền huấn luyện không chỉ phụ thuộc kiến trúc. Cách xây corpus quyết định mô hình được tiếp xúc với “thế giới” nào. Dữ liệu web thô thường cần khử trùng lặp (deduplication), lọc chất lượng, nhận diện ngôn ngữ, chia tài liệu, lọc an toàn và gán trọng số cho từng nguồn.

Nếu một domain được lấy mẫu quá nhiều, mô hình có xu hướng học domain đó mạnh hơn. Nếu corpus chứa bản sao của câu hỏi benchmark, đánh giá có thể bị nhiễm (contamination). Nếu quá trình lọc loại quá nhiều dữ liệu của một ngôn ngữ, năng lực ở ngôn ngữ đó có thể giảm.

Vì vậy có thể xem phân bố huấn luyện như một **chương trình học ngầm (implicit curriculum)**.

## Ngân sách token và mức độ tiếp xúc dữ liệu

Dataset thường được đo bằng số token chứ không chỉ số document. Tài liệu dài tạo nhiều vị trí huấn luyện hơn tài liệu ngắn.

Tokenization cũng ảnh hưởng mức độ tiếp xúc và chi phí: cùng một lượng nội dung tiếng Việt hoặc tiếng Hàn có thể cần nhiều token hơn tiếng Anh tùy vocabulary, làm tăng compute và giảm dung lượng context hiệu dụng.

Xem thêm: [LLM Tokenization](./01_llm_tokenization.md).

## Causal masking

Mô hình decoder-only dùng **mặt nạ nhân quả (causal mask)** để token ở vị trí `t` không nhìn thấy token tương lai `x_{>t}` trong lúc huấn luyện. Điều này làm tác vụ huấn luyện phù hợp với sinh tự hồi quy.

Trong một sequence huấn luyện, forward pass vẫn có thể xử lý nhiều vị trí song song vì các token đúng phía trước đã có sẵn. Khi suy luận thì khác: token mới phải sinh tuần tự vì đầu ra bước trước trở thành input bước sau.

Đây là lý do thông lượng huấn luyện và độ trễ sinh có đặc tính hệ thống rất khác nhau.

## Teacher forcing

Trong huấn luyện tự hồi quy, mô hình thường nhận **token trước đó đúng theo dữ liệu (ground-truth previous token)** thay vì token do chính nó sinh. Cơ chế này gọi là **teacher forcing**.

Teacher forcing giúp tối ưu ổn định và cho phép song song hóa, nhưng tạo khác biệt với inference: nếu mô hình sinh sai một token khi triển khai, các bước sau phải điều kiện hóa trên chính lỗi đó và lỗi có thể tích lũy.

Instruction tuning và preference training có thể thay đổi hành vi nhưng không loại bỏ hoàn toàn sự khác biệt này.

## Packing và xây sequence

Để tận dụng GPU, nhiều tài liệu ngắn có thể được **đóng gói (packing)** vào cùng một sequence. Implementation phải xử lý đúng ranh giới attention nếu không muốn token của tài liệu này vô tình nhìn sang tài liệu khác theo cách không mong muốn.

Huấn luyện context dài cũng làm chi phí attention tăng mạnh. Với self-attention chuẩn, compute và memory của attention tăng gần bậc hai theo độ dài chuỗi:

\[
O(n^2)
\]

Do đó context length không phải một cấu hình miễn phí.

## Phối trộn dữ liệu

LLM tổng quát thường được huấn luyện trên hỗn hợp văn bản tự nhiên, mã nguồn, toán học, sách, tài liệu kỹ thuật và nguồn đã tuyển chọn. Trọng số của từng nguồn quyết định mức đóng góp gradient.

Ví dụ tăng dữ liệu code có thể cải thiện lập trình và đôi khi cải thiện kiểu lập luận có cấu trúc, nhưng nếu mixture mất cân bằng, chất lượng ở các domain ngôn ngữ khác có thể giảm. Đây là bài toán tối ưu đa mục tiêu chứ không phải “càng nhiều dữ liệu càng tốt”.

## Khử trùng lặp

Dữ liệu trùng khiến mô hình gặp cùng mẫu quá nhiều lần, tăng nguy cơ ghi nhớ và làm sai lệch ước lượng chất lượng. Có thể deduplicate ở cấp document, paragraph hoặc chuỗi con xấp xỉ.

Deduplication cũng quan trọng với tính toàn vẹn benchmark. Nếu tập đánh giá hoặc bản gần trùng của nó đã xuất hiện trong corpus tiền huấn luyện, điểm số không còn phản ánh khả năng khái quát hóa sạch.

## Ghi nhớ và khái quát hóa

LLM có thể vừa khái quát hóa vừa ghi nhớ; hai hiện tượng không loại trừ nhau.

Chuỗi hiếm, thông tin nhận dạng cá nhân hoặc chuỗi lặp nhiều lần có nguy cơ bị ghi nhớ cao hơn. Tuy nhiên phần lớn năng lực hữu ích đến từ các trừu tượng hóa và quy luật thống kê đã học, chứ không phải chỉ sao chép nguyên văn.

Khi đánh giá privacy, cần phân biệt:

```text
mô hình biết mẫu tổng quát
và
mô hình có thể tái tạo chuỗi huấn luyện cụ thể
```

## Tiền huấn luyện tạo base model, không phải trợ lý hoàn chỉnh

Base model được tối ưu để tiếp tục văn bản. Với prompt dạng:

```text
User: Explain gradient descent.
Assistant:
```

mô hình có thể tiếp tục theo mẫu hội thoại nếu từng thấy cấu trúc tương tự, nhưng không có bảo đảm rằng nó sẽ tuân thủ chỉ dẫn ổn định.

Hành vi làm theo chỉ dẫn thường được cải thiện bằng **tinh chỉnh có giám sát (SFT)** và **tối ưu sở thích (preference optimization)**.

## Tiền huấn luyện thích ứng theo miền

Có thể tiếp tục tiền huấn luyện trên corpus chuyên ngành như tài chính, pháp lý hoặc y sinh. Cách này thường gọi là **continued pretraining** hoặc **domain-adaptive pretraining**.

Nó khác SFT. Continued pretraining vẫn tối ưu objective của mô hình ngôn ngữ trên raw text; SFT tối ưu phản hồi dựa trên cặp input–response được định dạng rõ.

Continued pretraining hữu ích khi muốn mô hình hấp thụ vocabulary và phân bố chuyên ngành sâu hơn, nhưng có thể gây **quên nghiêm trọng (catastrophic forgetting)** nếu dữ liệu quá hẹp hoặc learning rate quá lớn.

## Tiền huấn luyện và năng lực nổi lên

Khi tăng quy mô mô hình, dữ liệu và compute, một số năng lực trở nên rõ ràng hơn. Không nên diễn giải điều đó như một “module reasoning bí mật” đột nhiên được bật.

Năng lực quan sát được là kết quả tương tác giữa kiến trúc, phân bố dữ liệu, tối ưu, quy mô và cách đánh giá. Một benchmark có thể tạo cảm giác năng lực xuất hiện đột ngột chỉ vì điểm vượt một ngưỡng trong khi chất lượng nền đã tăng dần.

## Mô hình tư duy

> Tiền huấn luyện là quá trình **nén phân bố của corpus khổng lồ vào tham số** bằng mục tiêu dự đoán token. Mô hình không học một bách khoa toàn thư có chỉ mục; nó học một hàm tạo phân bố xác suất theo context.

## Những hiểu lầm thường gặp

### “Mô hình đã đọc Internet nên biết mọi thứ trên Internet”

Corpus luôn hữu hạn, đã được lọc và có mốc thời gian. Ngay cả văn bản từng xuất hiện trong huấn luyện cũng không bảo đảm được truy xuất chính xác.

### “Pretraining chỉ dạy fact”

Nó đồng thời dạy cú pháp, phong cách, pattern code, quan hệ ngữ nghĩa, pattern thủ tục và biểu diễn dùng lại được.

### “Thêm dữ liệu luôn tốt”

Dữ liệu chất lượng thấp, trùng lặp hoặc lệch mục tiêu có thể làm mô hình tệ hơn. Chất lượng và mixture quan trọng không kém số lượng.

## Liên kết kiến thức

Tiền huấn luyện kết nối [Language Models](../07_natural_language_processing/02_language_models.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md).

Xem tiếp: [Scaling Laws](./05_scaling_laws.md).