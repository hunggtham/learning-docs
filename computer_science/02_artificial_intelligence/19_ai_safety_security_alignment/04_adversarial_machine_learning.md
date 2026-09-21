# Học máy đối kháng (Adversarial Machine Learning)

**Học máy đối kháng (Adversarial Machine Learning / 적대적 머신러닝)** nghiên cứu cách một hệ thống học máy phản ứng khi có một đối tượng chủ động tìm cách làm mô hình sai, vượt qua bộ phát hiện hoặc làm giảm chất lượng hệ thống. Điểm khác với nhiễu ngẫu nhiên là kẻ tấn công có mục tiêu và có thể điều chỉnh chiến lược dựa trên phản hồi của hệ thống.

## Kiến thức cần có trước

Nên nắm [hàm mất mát và rủi ro](../04_machine_learning/04_loss_objective_and_risk.md), [gradient và tối ưu hóa](../05_neural_networks/05_gradient_descent_and_optimizers.md), [khả năng bền vững trước dịch chuyển phân phối](../18_evaluation_reliability_interpretability/03_robustness_and_distribution_shift.md) và [mô hình đe dọa trong bảo mật AI](./README.md).

## Mô hình đe dọa là điểm bắt đầu

Không thể nói một mô hình “an toàn trước adversarial attack” nếu chưa nói rõ kẻ tấn công có khả năng gì. Một **mô hình đe dọa (threat model)** nên trả lời ít nhất:

```text
kẻ tấn công biết gì về mô hình?
có xem được gradient hoặc trọng số không?
chỉ được gửi request qua API hay có quyền truy cập sâu hơn?
được phép thay đổi input ở mức nào?
có giới hạn vật lý hoặc nghiệp vụ nào?
mục tiêu là gây sai, né phát hiện hay làm hệ thống tốn tài nguyên?
```

Ba nhãn thường gặp là **hộp trắng (white-box)**, **hộp đen (black-box)** và **tấn công trong thế giới vật lý (physical-world attack)**. Đây chỉ là cách mô tả quyền truy cập; độ khó thực tế còn phụ thuộc giới hạn của domain.

## Trực giác toán học

Mô hình học tham số `θ` để giảm hàm mất mát trên dữ liệu bình thường. Trong bài toán đối kháng, ta xét thêm một nhiễu có chủ đích `δ` nằm trong tập ràng buộc `S`:

\[
\max_{\delta\in S} L(f_\theta(x+\delta),y)
\]

Nếu huấn luyện theo hướng bền vững, bài toán thường có dạng cực tiểu–cực đại:

\[
\min_\theta\; \mathbb{E}_{(x,y)}
\left[
\max_{\delta\in S} L(f_\theta(x+\delta),y)
\right]
\]

Ý nghĩa quan trọng là mô hình không chỉ cần đúng ở một điểm `x`, mà còn phải ổn định trong một vùng lân cận được xác định bởi mô hình đe dọa. Tuy nhiên tập `S` chỉ là mô hình hóa. Nếu `S` không phản ánh cách attacker thật sự có thể thao tác hệ thống thì “robust accuracy” vẫn có thể gây hiểu nhầm.

## Tấn công né tránh tại thời điểm suy luận

**Tấn công né tránh (evasion attack)** thay đổi input khi hệ thống đang suy luận để làm mô hình chọn kết quả sai hoặc vượt qua bộ phát hiện.

Ví dụ ở mức khái niệm:

```text
ảnh bị thay đổi rất nhỏ
→ mô hình phân loại sai

mẫu giao dịch được điều chỉnh
→ điểm gian lận giảm

văn bản được biến đổi cách viết
→ bộ lọc nội dung bỏ sót
```

Một perturbation nhỏ theo chuẩn toán học chưa chắc thực tế. Với ảnh, thay đổi vài pixel số có thể không tương ứng với điều kiện in ấn, góc nhìn hoặc ánh sáng ngoài đời. Với giao dịch, một vector feature có thể chứa tổ hợp không thể xảy ra trong business thật.

## Vì sao ví dụ đối kháng tồn tại?

Trong không gian chiều cao, biên quyết định của mô hình có thể nằm rất gần một điểm dữ liệu theo một số hướng mà con người không chú ý. Mô hình cũng có thể sử dụng các đặc trưng có sức dự đoán cao nhưng giòn, thay vì chỉ dựa vào những đặc trưng con người cho là “ngữ nghĩa”.

Điều này liên hệ trực tiếp tới **thiên lệch quy nạp (inductive bias)** và học biểu diễn: mô hình học điều gì phụ thuộc dữ liệu, kiến trúc và hàm mục tiêu, không phụ thuộc trực tiếp vào cách con người muốn giải thích bài toán.

## Gradient và attacker thích nghi

Trong bối cảnh hộp trắng, gradient của loss theo input cho biết hướng nào làm loss tăng nhanh. Đây là lý do nhiều phương pháp kiểm thử đối kháng dùng gradient như một tín hiệu tìm kiếm. Trong production, điều quan trọng hơn là **adaptive evaluation**: nếu defense đã biết trước, attacker cũng được giả định biết defense và điều chỉnh chiến lược theo nó.

Một defense chỉ hiệu quả với một bộ tấn công cố định nhưng thất bại ngay khi attacker thích nghi thường là dấu hiệu đánh giá chưa đủ mạnh.

## Tấn công hộp đen

Trong hộp đen, attacker chỉ thấy API và output. Họ có thể tận dụng nhiều request để ước lượng ranh giới quyết định hoặc huấn luyện một mô hình thay thế (surrogate model). Vì vậy ẩn kiến trúc hoặc trọng số có thể tăng chi phí tấn công nhưng không tạo ra một ranh giới bảo mật vững chắc.

Ở production, rate limit, quota, xác thực và giám sát hành vi truy vấn giúp giảm ngân sách tấn công, nhưng không nên được xem là bằng chứng rằng mô hình đã bền vững.

## Tính chuyển giao

Ví dụ đối kháng được tạo cho một mô hình đôi khi vẫn làm mô hình khác sai. Hiện tượng này gọi là **tính chuyển giao (transferability)**. Nó cho thấy nhiều mô hình có thể chia sẻ cấu trúc ranh giới quyết định tương tự, đồng thời giải thích vì sao việc giữ bí mật model family không phải defense chính.

## Huấn luyện đối kháng

**Huấn luyện đối kháng (adversarial training)** bổ sung các ví dụ khó vào vòng huấn luyện và tối ưu trực tiếp bài toán min–max ở trên. Đây là một trong những phương pháp mạnh cho một threat model đã xác định, nhưng có trade-off:

```text
chi phí huấn luyện cao hơn
có thể giảm accuracy trên dữ liệu sạch
robustness thường chỉ mạnh trong threat set đã huấn luyện
có thể cần model capacity lớn hơn
```

Nếu threat model production khác threat model dùng để huấn luyện, độ bền vững có thể không chuyển sang tốt.

## Bảo đảm bền vững có chứng nhận

Một số phương pháp cung cấp **bảo đảm có chứng nhận (certified robustness)** trong một vùng nhiễu bị chặn. Giá trị của chúng nằm ở việc đưa ra cam kết toán học rõ ràng, nhưng phạm vi bảo đảm thường hẹp hơn nhiều so với toàn bộ attack surface của hệ thống thật.

Bảo đảm kiểu “ổn định trong bán kính `r` theo chuẩn đã chọn” không nói gì trực tiếp về prompt injection, poisoning, lỗi parser, quyền tool hoặc tấn công chuỗi cung ứng.

## Phát hiện input đáng ngờ

Bộ phát hiện đối kháng hoặc ngoài phân phối (OOD detector) có thể đánh dấu input khác thường trước khi model chính xử lý. Tuy nhiên detector cũng là một mô hình có thể bị attacker thích nghi. Vì vậy detection nên là một lớp defense-in-depth, không phải cơ chế duy nhất.

## Tấn công trong thế giới vật lý

Với robot, camera hoặc hệ thống thị giác, cần xem xét:

```text
góc nhìn
ánh sáng
chất lượng in hoặc màn hình
chuyển động
thời tiết
nhiễu cảm biến
camera pipeline
```

Một attack thành công trong tensor-space nhưng thất bại sau camera pipeline không có cùng ý nghĩa rủi ro với attack chịu được nhiều biến đổi vật lý.

## Văn bản và LLM

Đầu vào ngôn ngữ là rời rạc nên không thể sao chép nguyên cách tối ưu perturbation pixel. Tuy vậy vẫn có các input đối kháng như paraphrase, Unicode bất thường, cấu trúc định dạng lạ hoặc chuỗi gây model đổi hành vi.

Với ứng dụng LLM có RAG và tool, [prompt injection](./03_prompt_injection_and_jailbreaks.md) là vấn đề nghiêm trọng hơn generic adversarial classification vì nó tác động tới **authority** và control flow của hệ thống.

## Mô hình triển khai production

Một hệ thống production nên tách defense theo nhiều lớp:

```text
request
→ authentication / quota
→ kiểm tra định dạng và domain constraints
→ model inference
→ kiểm tra output / policy
→ business validation
→ action hoặc response
→ logging + monitoring
```

Nếu mô hình phân loại đưa ra xác suất bất thường hoặc input nằm ngoài miền được hỗ trợ, hệ thống có thể từ chối quyết định tự động và chuyển sang fallback hoặc human review.

## Đánh giá đúng cách

Một báo cáo adversarial robustness tốt nên nói rõ:

```text
threat model
quyền truy cập của attacker
ràng buộc perturbation
số lần truy vấn nếu là black-box
defense có được attacker biết không?
metric trên dữ liệu sạch
metric dưới tấn công
chi phí tính toán
```

Chỉ viết “robust accuracy = 80%” mà không có các điều kiện trên là chưa đủ thông tin.

## Trade-off trong thiết kế

Tăng robustness thường đánh đổi ít nhất một trong các yếu tố: compute, latency, accuracy sạch, độ phức tạp triển khai hoặc phạm vi input được chấp nhận. Production design cần chọn defense theo mức độ rủi ro chứ không theo một benchmark chung cho mọi use case.

Ví dụ dịch vụ đề xuất nội dung có thể chấp nhận fallback mềm, trong khi hệ thống xác minh danh tính hoặc kiểm soát công nghiệp có thể cần fail closed và human escalation.

## Failure mode thường gặp

**Đánh giá quá yếu.** Attack cố định không còn hiệu quả sau khi defense thay đổi, nhưng adaptive attacker vẫn vượt qua được.

**Gradient masking.** Defense làm gradient khó dùng nhưng không thật sự làm biên quyết định tốt hơn; attacker có thể chuyển sang kỹ thuật khác hoặc mô hình thay thế.

**Threat model không thực tế.** Kết quả đẹp trong benchmark nhưng input tạo ra không thể tồn tại trong domain.

**Bảo vệ model nhưng quên system.** Mô hình robust không ngăn được lỗi authorization, parser, retrieval hoặc supply chain.

**Phản ứng quá mức.** Bộ lọc quá chặt có thể làm tăng false positive và chặn người dùng hợp lệ.

## Mô hình tư duy

> **Học máy đối kháng hỏi: nếu phía bên kia cũng đang tối ưu, ranh giới quyết định và pipeline của hệ thống sẽ thất bại ở đâu?**

Mục tiêu production không phải chứng minh “không thể bị tấn công”, mà là giới hạn khả năng, chi phí và hậu quả của attacker trong một threat model rõ ràng.

## Những nhầm lẫn thường gặp

### “Chịu được nhiễu ngẫu nhiên nghĩa là chịu được tấn công đối kháng”

Không. Attacker chọn input có chủ đích thay vì lấy nhiễu ngẫu nhiên.

### “Ẩn model là đủ”

Không. API vẫn rò rỉ hành vi, còn tính chuyển giao cho phép attacker dùng surrogate model.

### “Một certified radius nghĩa là hệ thống đã secure”

Không. Chứng nhận chỉ bao phủ perturbation model cụ thể, không bao phủ toàn hệ thống.

### “Robust model thì không cần system controls”

Không. Authorization, rate limit, validation, sandbox và incident response vẫn là các lớp riêng.

## Liên kết kiến thức

Nên đọc cùng [Robustness và Distribution Shift](../18_evaluation_reliability_interpretability/03_robustness_and_distribution_shift.md), [Red Teaming](../18_evaluation_reliability_interpretability/06_red_teaming_and_adversarial_evaluation.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Data Poisoning](./05_data_poisoning_backdoors_and_model_attacks.md) và [Secure AI System Design](./08_secure_ai_system_design.md).