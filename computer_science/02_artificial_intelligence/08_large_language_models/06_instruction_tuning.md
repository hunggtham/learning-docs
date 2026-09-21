# Tinh chỉnh theo chỉ dẫn

LLM cơ sở được tiền huấn luyện để **tiếp tục văn bản**, nhưng người dùng muốn một trợ lý có thể hiểu yêu cầu và tạo phản hồi phù hợp. **Tinh chỉnh theo chỉ dẫn (instruction tuning / 지시 튜닝)** là quá trình điều chỉnh mô hình để ánh xạ từ chỉ dẫn + ngữ cảnh sang định dạng phản hồi và hành vi mong muốn.

Điểm quan trọng là instruction tuning không “dạy toàn bộ tri thức mới”. Phần lớn kiến thức rộng và năng lực ngôn ngữ đã hình thành trong tiền huấn luyện. Hậu huấn luyện chủ yếu thay đổi cách mô hình **sử dụng** các năng lực đó theo kiểu tương tác mong muốn.

## Từ tiếp tục văn bản tới làm theo chỉ dẫn

Mục tiêu tiền huấn luyện:

\[
P(x_t\mid x_{<t})
\]

không tự phân biệt vai trò ngữ nghĩa như system, user hay assistant trừ khi các mẫu đó xuất hiện trong dữ liệu.

Dataset chỉ dẫn cung cấp cấu trúc rõ hơn:

```text
Chỉ dẫn: Giải thích recursion đơn giản.
Phản hồi: ...
```

hoặc định dạng chat:

```text
system    → policy / context
user      → yêu cầu
assistant → phản hồi mong muốn
```

Mô hình học rằng một số chuỗi token đóng vai trò chỉ dẫn và đầu ra nên tuân theo các ràng buộc tương ứng.

## Dữ liệu instruction

Dữ liệu instruction có thể đến từ ví dụ do con người viết, dữ liệu tổng hợp, dataset được chuyển đổi hoặc mixture của nhiều tác vụ. Chất lượng quan trọng hơn việc chỉ tăng số lượng.

Một ví dụ tốt không chỉ có “đáp án đúng”; nó còn thể hiện định dạng, độ sâu, giọng điệu, ranh giới từ chối, schema gọi công cụ hoặc phong cách lập luận cần thiết.

Nếu dataset không nhất quán, mô hình cũng học một phân bố hành vi không nhất quán.

## Đa dạng tác vụ và khả năng khái quát hóa

Instruction tuning hữu ích vì mô hình có thể khái quát từ nhiều mẫu tác vụ sang chỉ dẫn chưa thấy. Nếu dữ liệu huấn luyện chỉ chứa một số template hẹp, mô hình có thể overfit vào cách diễn đạt.

Sự đa dạng giúp mô hình học một pattern cấp cao hơn:

> Phần văn bản trước mô tả ý định và ràng buộc; phần phản hồi phải thỏa mãn ý định và ràng buộc đó.

Đây có thể được xem như một giao diện học được giữa ngôn ngữ tự nhiên và năng lực của mô hình.

## Vai trò System, User và Assistant

Hệ thống chat hiện đại thường mã hóa vai trò bằng token đặc biệt hoặc định dạng riêng. Thứ bậc vai trò không phải thuộc tính tự nhiên của mô hình ngôn ngữ; nó là hành vi được hình thành bởi dữ liệu huấn luyện, giao thức serving và policy ở runtime.

Vì vậy **prompt injection** là vấn đề cấp hệ thống: mô hình đọc nhiều luồng văn bản, trong khi ứng dụng muốn một số luồng có quyền cao hơn các luồng khác.

## Instruction tuning và tri thức

Fine-tuning có thể bổ sung một phần tri thức theo miền, nhưng không phải lúc nào cũng là công cụ tốt nhất. Nếu tri thức thay đổi thường xuyên hoặc cần provenance, retrieval thường phù hợp hơn.

Nên dùng instruction tuning khi muốn thay đổi **ánh xạ hành vi**, ví dụ:

```text
input schema → JSON có cấu trúc
support ticket → phân loại + giải thích
câu hỏi → phản hồi theo policy hoặc phong cách domain
```

Nên dùng RAG khi cần đưa fact và document context mới, có thể truy nguồn, vào quá trình trả lời.

## Quên nghiêm trọng

Nếu fine-tune quá mạnh trên dữ liệu hẹp, mô hình có thể mất một phần năng lực hoặc phong cách tổng quát đã học. Hiện tượng này gọi là **quên nghiêm trọng (catastrophic forgetting)**.

Các cách giảm gồm learning rate thấp hơn, trộn dữ liệu tổng quát, regularization và tinh chỉnh tiết kiệm tham số (parameter-efficient fine-tuning).

## Instruction tuning đa tác vụ

Một mô hình có thể được huấn luyện đồng thời trên dịch, tóm tắt, QA, extraction, coding và dialogue. Biểu diễn dùng chung cho phép chuyển giao giữa các tác vụ.

Tuy nhiên mixture cần được gán trọng số. Dataset lớn nhưng dễ có thể chi phối gradient và khiến tác vụ khó hoặc hiếm bị đại diện quá ít.

## Dữ liệu instruction tổng hợp

Một mô hình mạnh hơn có thể sinh cặp instruction–response để huấn luyện mô hình khác. Cách này mở rộng dữ liệu nhanh nhưng có nguy cơ lan truyền lỗi, phong cách nhân tạo và blind spot của teacher.

Dữ liệu tổng hợp cần lọc và đánh giá, không nên mặc định coi đầu ra teacher là ground truth.

## Instruction tuning và SFT

Hai thuật ngữ này giao nhau nhiều nhưng nhấn mạnh hai khía cạnh khác nhau.

**Tinh chỉnh có giám sát (Supervised Fine-Tuning — SFT)** mô tả thủ tục học từ cặp input–output có nhãn. **Instruction tuning** mô tả loại dữ liệu và hành vi: ví dụ mang ý nghĩa chỉ dẫn.

Instruction tuning thường được thực hiện bằng SFT, nhưng SFT cũng có thể dùng cho tác vụ không phải natural-language instruction.

Xem tiếp: [Supervised Fine-Tuning](./07_supervised_fine_tuning.md).

## Làm theo chỉ dẫn chưa phải alignment hoàn chỉnh

Mô hình có thể làm theo instruction tốt nhưng vẫn:

- hallucinate;
- làm theo chỉ dẫn độc hại;
- vi phạm policy an toàn;
- tối ưu cách diễn đạt thay vì ý định;
- thất bại khi nhiều instruction xung đột.

Do đó hệ thống thường bổ sung preference training và các lớp an toàn ở runtime.

## Từ chối quá mức và từ chối thiếu

Hậu huấn luyện an toàn có sự đánh đổi. Nếu ví dụ từ chối quá rộng, mô hình có thể từ chối cả yêu cầu vô hại. Nếu quá hẹp, biến thể nguy hiểm có thể vượt qua ranh giới.

Đánh giá phải đo cả tính hữu ích và khả năng từ chối đúng lúc, thay vì chỉ tối ưu một phía.

## Định dạng cũng là một dạng hành vi

Instruction tuning có thể dạy mô hình tạo JSON, XML hoặc lời gọi công cụ. Tuy nhiên generation vẫn có tính xác suất. Nếu đầu ra phải hợp lệ cú pháp tuyệt đối, nên bổ sung **giải mã có ràng buộc (constrained decoding)** hoặc validation theo schema.

Hành vi mô hình và kiểm tra xác định là hai lớp khác nhau.

## Mô hình tư duy

> Tiền huấn luyện tạo **năng lực tổng quát**; instruction tuning tạo **giao thức tương tác** để năng lực đó phục vụ yêu cầu theo cách hữu ích hơn.

## Những hiểu lầm thường gặp

### “Fine-tune là cách tốt nhất để cập nhật fact mới”

Không nhất thiết. Retrieval thường tốt hơn về độ mới và provenance đối với tri thức động.

### “Instruction tuning làm mô hình hiểu mọi instruction”

Nó cải thiện khái quát hóa nhưng vẫn phụ thuộc phân bố dữ liệu, độ phức tạp của context và xung đột giữa các ràng buộc.

### “Thứ bậc vai trò được hard-code trong Transformer”

Ngữ nghĩa vai trò đến từ định dạng huấn luyện và hệ thống runtime; attention không tự biết system message có quyền cao hơn.

## Liên kết kiến thức

Instruction tuning nối pretraining với hành vi trợ lý. Sau SFT, các kỹ thuật như RLHF hoặc DPO tiếp tục điều chỉnh đầu ra theo sở thích con người và policy.

Xem tiếp: [Supervised Fine-Tuning](./07_supervised_fine_tuning.md).