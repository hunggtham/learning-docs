# Quy luật mở rộng quy mô trong mô hình ngôn ngữ lớn

Khi mô hình ngôn ngữ lớn tăng kích thước, câu hỏi không chỉ là “thêm tham số có tốt hơn không?” mà là **nên phân bổ tài nguyên tính toán giữa kích thước mô hình, dữ liệu và thời gian huấn luyện như thế nào**. **Quy luật mở rộng quy mô (scaling laws / 스케일링 법칙)** nghiên cứu quan hệ thực nghiệm giữa chất lượng mô hình và các nguồn lực đó.

Một hiện tượng thường thấy là loss giảm gần theo **hàm lũy thừa (power law)** khi tăng scale trong một khoảng rộng. Điều này không có nghĩa mọi benchmark đều tăng giống nhau, nhưng nó giúp dự đoán xu hướng và lập kế hoạch training run hợp lý hơn.

## Ba trục quy mô chính

Chi phí tiền huấn luyện có thể được nhìn gần đúng qua:

```text
N = số tham số
D = số token huấn luyện
C = ngân sách tính toán
```

Nếu mô hình rất lớn nhưng dữ liệu quá ít, mô hình bị **huấn luyện chưa đủ (under-trained)**. Nếu dữ liệu rất nhiều nhưng mô hình quá nhỏ, capacity có thể là điểm nghẽn. Huấn luyện tối ưu theo compute cố tìm sự cân bằng tốt hơn giữa `N` và `D` dưới ngân sách `C` cố định.

## Số tham số không phải thước đo năng lực duy nhất

Tăng tham số mở rộng khả năng biểu diễn và không gian hàm, nhưng năng lực còn phụ thuộc kiến trúc, chất lượng dữ liệu, optimizer, độ dài context và recipe huấn luyện. Hai mô hình có cùng số tham số vẫn có thể khác nhau đáng kể.

Trong kiến trúc **Mixture-of-Experts (MoE)**, cần phân biệt **tổng tham số (total parameters)** và **tham số hoạt động (active parameters)** vì mỗi token chỉ đi qua một tập con expert. Do đó mô hình “100B” kiểu MoE không nhất thiết có chi phí inference giống dense model 100B.

## Trực giác về tối ưu compute

Giả sử có ngân sách tính toán cố định. Nếu dùng hầu hết ngân sách để tăng `N` nhưng giữ `D` thấp, mỗi tham số nhận quá ít bằng chứng huấn luyện. Ngược lại, huấn luyện một mô hình nhỏ trên lượng dữ liệu quá lớn có thể lãng phí dữ liệu vì capacity giới hạn.

Mô hình tư duy:

> Mở rộng quy mô hiệu quả nghĩa là mô hình đủ lớn để hấp thụ cấu trúc trong dữ liệu và dữ liệu đủ nhiều để huấn luyện mô hình lớn đó tới mức phù hợp.

## Token huấn luyện và số vòng qua dữ liệu

Trong tiền huấn luyện quy mô web, corpus có thể được đi qua một hoặc vài lần tùy recipe. Lặp cùng dữ liệu quá nhiều làm tăng ghi nhớ và lợi ích giảm dần. Tuy vậy dữ liệu chất lượng cao đã tuyển chọn đôi khi được lấy mẫu nhiều hơn một cách có chủ đích.

Vì vậy số token thô không đồng nghĩa lượng thông tin độc lập duy nhất.

## Loss và năng lực không mở rộng giống nhau

Loss tiền huấn luyện có thể giảm khá trơn trong khi điểm benchmark trông như tăng đột ngột. Ví dụ một bài kiểm tra pass/fail có ngưỡng; việc tăng từ 49% lên 51% có thể khiến năng lực trông như vừa “xuất hiện”.

Một số tác vụ có thể thật sự thể hiện hành vi phi tuyến do nhiều kỹ năng kết hợp, nhưng không nên gắn nhãn **emergence** cho mọi bước nhảy mà chưa kiểm tra cách đo.

## Độ dài context là một chiều scale khác

Context dài hơn cho phép mô hình điều kiện hóa trên nhiều token hơn nhưng làm attention và KV cache tốn kém hơn. Mô hình được huấn luyện ở context 4k không tự động sử dụng tốt 128k chỉ bằng thay một cấu hình.

Năng lực context dài còn phụ thuộc cơ chế vị trí, phân bố dữ liệu huấn luyện, implementation attention và cách đánh giá.

## Compute trong lúc suy luận

Scale không chỉ nằm ở pretraining. Hệ thống có thể dùng nhiều compute hơn khi inference thông qua:

- sinh nhiều candidate;
- search và verification;
- trajectory lập luận dài hơn;
- gọi công cụ;
- retrieval;
- self-consistency hoặc reranking.

Điều này tạo một đánh đổi khác: cùng một base model, tăng **inference-time compute** có thể cải thiện độ chính xác nhưng cũng tăng độ trễ và chi phí.

## Distillation và mô hình nhỏ

Mô hình lớn có thể đóng vai teacher rồi **chưng cất (distill)** một phần năng lực sang mô hình nhỏ hơn. Small model vẫn rất quan trọng khi độ trễ, riêng tư, edge deployment hoặc chi phí là constraint.

Scaling laws không hàm ý mọi ứng dụng nên dùng mô hình lớn nhất.

## Kinh tế học của scale

Huấn luyện frontier model cần phần cứng, năng lượng, mạng và kỹ thuật hệ thống rất lớn. Nhưng khi số người dùng cao, tổng chi phí production có thể bị chi phối bởi inference.

Một kiến trúc tối ưu cho training chưa chắc tối ưu cho serving. KV cache, khả năng batching, độ dài chuỗi và tốc độ decode đều trở thành biến số kinh tế.

## Lợi ích giảm dần

Quan hệ gần power law thường đồng nghĩa mỗi mức cải thiện tiếp theo ngày càng đắt. Giảm loss từ 2.0 xuống 1.8 có thể cần một mức compute, còn giảm thêm tương đương ở vùng tốt hơn có thể tốn nhiều hơn đáng kể.

Vì vậy kỹ thuật hệ thống đôi khi mang lại giá trị lớn hơn việc tiếp tục tăng model size. Nếu vấn đề là độ mới của tri thức, grounding, quyền truy cập công cụ hoặc policy, RAG hay tool integration có thể hiệu quả hơn việc huấn luyện mô hình lớn hơn chỉ để ghi nhớ tài liệu riêng.

## Scale và chất lượng dữ liệu

Mô hình lớn có khả năng hấp thụ cả pattern hữu ích lẫn nhiễu, dữ liệu trùng, thông tin sai và phong cách không mong muốn. Vì vậy khi scale tăng, quản trị dữ liệu càng quan trọng chứ không giảm.

## Scale và alignment

Năng lực cơ sở tăng không bảo đảm instruction following, tính đúng sự thật hoặc an toàn tăng cùng tốc độ. Hậu huấn luyện và alignment phải theo kịp năng lực và bề mặt tấn công.

Mô hình mạnh hơn có thể vừa hữu ích hơn vừa tạo failure mode phức tạp hơn.

## Mô hình tư duy

```text
Scale ≠ chỉ số tham số
Scale = capacity mô hình + dữ liệu + compute + context + chiến lược inference
```

Câu hỏi quan trọng không phải chỉ “mô hình bao nhiêu tỷ tham số?” mà là **nguồn lực nào hiện đang là điểm nghẽn của tác vụ và hệ thống?**

## Những hiểu lầm thường gặp

### “Mô hình lớn hơn luôn tốt hơn cho production”

Không, nếu chi phí, độ trễ, riêng tư hoặc độ đơn giản của tác vụ là yếu tố quyết định.

### “Loss giảm nghĩa mọi năng lực đều tăng”

Loss là tín hiệu tổng hợp của language modeling; các năng lực downstream có thể tăng với tốc độ rất khác nhau.

### “Context window lớn nghĩa mô hình nhớ và reasoning tốt trên toàn context”

Dung lượng cửa sổ và khả năng sử dụng context hiệu quả là hai vấn đề khác nhau.

## Liên kết kiến thức

Scaling nối với [AI Compute](../17_ai_compute_and_infrastructure/00_computation_behind_ai.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Pretraining](./04_pretraining.md).

Xem tiếp: [Instruction Tuning](./06_instruction_tuning.md).