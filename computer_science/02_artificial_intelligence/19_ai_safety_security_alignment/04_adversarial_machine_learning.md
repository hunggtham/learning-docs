# Học máy đối kháng (Adversarial Machine Learning)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Adversarial machine learning**. Route đi từ threat model → evasion/poisoning/extraction attacks → perturbation budget → robustness evaluation → defenses and residual exposure, để tấn công luôn được đọc trong bối cảnh tài sản và attacker.

**Học máy đối kháng (Adversarial Machine Learning / 적대적 머신러닝)** nghiên cứu cách một hệ thống học máy phản ứng khi có một đối tượng chủ động tìm cách làm mô hình sai, vượt qua bộ phát hiện hoặc làm giảm chất lượng hệ thống. Điểm khác với nhiễu ngẫu nhiên là kẻ tấn công có mục tiêu và có thể điều chỉnh chiến lược dựa trên phản hồi của hệ thống.

## Kiến thức cần có trước

Nên nắm [hàm mất mát và rủi ro](../04_machine_learning/04_loss_objective_and_risk.md), [gradient và tối ưu hóa](../05_neural_networks/05_gradient_descent_and_optimizers.md), [khả năng bền vững trước dịch chuyển phân phối](../18_evaluation_reliability_interpretability/03_robustness_and_distribution_shift.md) và [mô hình đe dọa trong bảo mật AI](./README.md).

> **Chuyển mạch:** Trong **Học máy đối kháng (Adversarial Machine Learning)**, **Mô hình đe dọa là điểm bắt đầu** tiếp nhận điểm tựa từ **Kiến thức cần có trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác toán học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Ba nhãn thường gặp là **hộp trắng (white-box)**, **hộp đen (black-box)** và **tấn công trong thế giới vật lý (physical-world attack)**. Đây chỉ là cách mô tả quyền truy cập; độ khó thực tế còn phụ thuộc giới hạn của lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Ở chặng này của **Học máy đối kháng (Adversarial Machine Learning)**, **Trực giác toán học** tiếp nhận điểm tựa từ **Mô hình đe dọa là điểm bắt đầu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tấn công né tránh tại thời điểm suy luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Học máy đối kháng (Adversarial Machine Learning)**, **Tấn công né tránh tại thời điểm suy luận** tiếp nhận điểm tựa từ **Trực giác toán học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao ví dụ đối kháng tồn tại?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tấn công né tránh tại thời điểm suy luận

**Tấn công né tránh (evasion attack)** thay đổi đầu vào (input / 입력) khi hệ thống đang suy luận để làm mô hình chọn kết quả sai hoặc vượt qua bộ phát hiện.

Ví dụ ở mức khái niệm:

```text
ảnh bị thay đổi rất nhỏ
→ mô hình phân loại sai

mẫu giao dịch được điều chỉnh
→ điểm gian lận giảm

văn bản được biến đổi cách viết
→ bộ lọc nội dung bỏ sót
```

Một perturbation nhỏ theo chuẩn toán học chưa chắc thực tế. Với ảnh, thay đổi vài điểm ảnh (pixel / 픽셀) số có thể không tương ứng với điều kiện in ấn, góc nhìn hoặc ánh sáng ngoài đời. Với giao dịch, một véc-tơ (vector / 벡터) tính năng (feature / 기능) có thể chứa tổ hợp không thể xảy ra trong nghiệp vụ (business / 비즈니스) thật.

> **Chuyển mạch:** Trong **Học máy đối kháng (Adversarial Machine Learning)**, **Tấn công né tránh tại thời điểm suy luận** cho ta quy tắc; **Vì sao ví dụ đối kháng tồn tại?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Độ dốc (gradient / 기울기) và attacker thích nghi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao ví dụ đối kháng tồn tại?

Trong không gian chiều cao, biên quyết định của mô hình có thể nằm rất gần một điểm dữ liệu theo một số hướng mà con người không chú ý. Mô hình cũng có thể sử dụng các đặc trưng có sức dự đoán cao nhưng giòn, thay vì chỉ dựa vào những đặc trưng con người cho là “ngữ nghĩa”.

Điều này liên hệ trực tiếp tới **thiên lệch quy nạp (inductive bias)** và học biểu diễn: mô hình học điều gì phụ thuộc dữ liệu, kiến trúc và hàm mục tiêu, không phụ thuộc trực tiếp vào cách con người muốn giải thích bài toán.

> **Chuyển mạch:** Ở chặng này của **Học máy đối kháng (Adversarial Machine Learning)**, **Vì sao ví dụ đối kháng tồn tại?** cho ta quy tắc; **Độ dốc (gradient / 기울기) và attacker thích nghi** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Tấn công hộp đen** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) và attacker thích nghi

Trong bối cảnh hộp trắng, độ dốc (gradient / 기울기) của mất mát (loss / 손실) theo đầu vào (input / 입력) cho biết hướng nào làm mất mát (loss / 손실) tăng nhanh. Đây là lý do nhiều phương pháp kiểm thử đối kháng dùng độ dốc (gradient / 기울기) như một tín hiệu tìm kiếm. Trong môi trường vận hành (production / 운영 환경), điều quan trọng hơn là **adaptive evaluation**: nếu defense đã biết trước, attacker cũng được giả định biết defense và điều chỉnh chiến lược theo nó.

Một defense chỉ hiệu quả với một bộ tấn công cố định nhưng thất bại ngay khi attacker thích nghi thường là dấu hiệu đánh giá chưa đủ mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Học máy đối kháng (Adversarial Machine Learning)**, **Tấn công hộp đen** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) và attacker thích nghi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính chuyển giao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tấn công hộp đen

Trong hộp đen, attacker chỉ thấy API và đầu ra (output / 출력). Họ có thể tận dụng nhiều yêu cầu (request / 요청) để ước lượng ranh giới quyết định hoặc huấn luyện một mô hình thay thế (surrogate model). Vì vậy ẩn kiến trúc hoặc trọng số có thể tăng chi phí tấn công nhưng không tạo ra một ranh giới bảo mật vững chắc.

Ở môi trường vận hành (production / 운영 환경), tỷ lệ (rate / 비율) limit, quota, xác thực và giám sát hành vi truy vấn giúp giảm ngân sách tấn công, nhưng không nên được xem là bằng chứng rằng mô hình đã bền vững.

> **Chuyển mạch:** Trong **Học máy đối kháng (Adversarial Machine Learning)**, **Tính chuyển giao** tiếp nhận điểm tựa từ **Tấn công hộp đen** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Huấn luyện đối kháng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính chuyển giao

Ví dụ đối kháng được tạo cho một mô hình đôi khi vẫn làm mô hình khác sai. Hiện tượng này gọi là **tính chuyển giao (transferability)**. Nó cho thấy nhiều mô hình có thể chia sẻ cấu trúc ranh giới quyết định tương tự, đồng thời giải thích vì sao việc giữ bí mật mô hình (model / 모델) family không phải defense chính.

> **Chuyển mạch:** Ở chặng này của **Học máy đối kháng (Adversarial Machine Learning)**, **Huấn luyện đối kháng** tiếp nhận điểm tựa từ **Tính chuyển giao** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo đảm bền vững có chứng nhận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Huấn luyện đối kháng

**Huấn luyện đối kháng (adversarial training)** bổ sung các ví dụ khó vào vòng huấn luyện và tối ưu trực tiếp bài toán min–max ở trên. Đây là một trong những phương pháp mạnh cho một threat mô hình (model / 모델) đã xác định, nhưng có sự đánh đổi (trade-off / 트레이드오프):

```text
chi phí huấn luyện cao hơn
có thể giảm accuracy trên dữ liệu sạch
robustness thường chỉ mạnh trong threat set đã huấn luyện
có thể cần model capacity lớn hơn
```

Nếu threat mô hình (model / 모델) môi trường vận hành (production / 운영 환경) khác threat mô hình (model / 모델) dùng để huấn luyện, độ bền vững có thể không chuyển sang tốt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Học máy đối kháng (Adversarial Machine Learning)**, **Bảo đảm bền vững có chứng nhận** tiếp nhận điểm tựa từ **Huấn luyện đối kháng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phát hiện đầu vào (input / 입력) đáng ngờ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo đảm bền vững có chứng nhận

Một số phương pháp cung cấp **bảo đảm có chứng nhận (certified robustness)** trong một vùng nhiễu bị chặn. Giá trị của chúng nằm ở việc đưa ra cam kết toán học rõ ràng, nhưng phạm vi bảo đảm thường hẹp hơn nhiều so với toàn bộ attack surface của hệ thống thật.

Bảo đảm kiểu “ổn định trong bán kính `r` theo chuẩn đã chọn” không nói gì trực tiếp về prompt injection, poisoning, lỗi parser, quyền công cụ (tool / 도구) hoặc tấn công chuỗi cung ứng.

> **Chuyển mạch:** Trong **Học máy đối kháng (Adversarial Machine Learning)**, **Phát hiện đầu vào (input / 입력) đáng ngờ** tiếp nhận điểm tựa từ **Bảo đảm bền vững có chứng nhận** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tấn công trong thế giới vật lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phát hiện đầu vào (input / 입력) đáng ngờ

Bộ phát hiện đối kháng hoặc ngoài phân phối (OOD detector) có thể đánh dấu đầu vào (input / 입력) khác thường trước khi mô hình (model / 모델) chính xử lý. Tuy nhiên detector cũng là một mô hình có thể bị attacker thích nghi. Vì vậy detection nên là một lớp defense-in-depth, không phải cơ chế duy nhất.

> **Chuyển mạch:** Ở chặng này của **Học máy đối kháng (Adversarial Machine Learning)**, **Tấn công trong thế giới vật lý** tiếp nhận điểm tựa từ **Phát hiện đầu vào (input / 입력) đáng ngờ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Văn bản và LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Một attack thành công trong tensor-space nhưng thất bại sau camera chuỗi xử lý (pipeline / 파이프라인) không có cùng ý nghĩa rủi ro với attack chịu được nhiều biến đổi vật lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Học máy đối kháng (Adversarial Machine Learning)**, **Văn bản và LLM** tiếp nhận điểm tựa từ **Tấn công trong thế giới vật lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Văn bản và LLM

Đầu vào ngôn ngữ là rời rạc nên không thể sao chép nguyên cách tối ưu perturbation điểm ảnh (pixel / 픽셀). Tuy vậy vẫn có các đầu vào (input / 입력) đối kháng như paraphrase, Unicode bất thường, cấu trúc định dạng lạ hoặc chuỗi gây mô hình (model / 모델) đổi hành vi.

Với ứng dụng LLM có RAG và công cụ (tool / 도구), [prompt injection](./03_prompt_injection_and_jailbreaks.md) là vấn đề nghiêm trọng hơn generic adversarial classification vì nó tác động tới **authority** và điều khiển (control / 제어) luồng (flow / 흐름) của hệ thống.

> **Chuyển mạch:** Trong **Học máy đối kháng (Adversarial Machine Learning)**, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Văn bản và LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá đúng cách** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai môi trường vận hành (production / 운영 환경)

Một hệ thống môi trường vận hành (production / 운영 환경) nên tách defense theo nhiều lớp:

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

Nếu mô hình phân loại đưa ra xác suất bất thường hoặc đầu vào (input / 입력) nằm ngoài miền được hỗ trợ, hệ thống có thể từ chối quyết định tự động và chuyển sang fallback hoặc human rà soát (review / 검토).

> **Chuyển mạch:** Ở chặng này của **Học máy đối kháng (Adversarial Machine Learning)**, **Đánh giá đúng cách** tiếp nhận điểm tựa từ **Mô hình triển khai môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프) trong thiết kế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Học máy đối kháng (Adversarial Machine Learning)**, **Sự đánh đổi (trade-off / 트레이드오프) trong thiết kế** tiếp nhận điểm tựa từ **Đánh giá đúng cách** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프) trong thiết kế

Tăng robustness thường đánh đổi ít nhất một trong các yếu tố: compute, độ trễ (latency / 지연 시간), accuracy sạch, độ phức tạp triển khai hoặc phạm vi đầu vào (input / 입력) được chấp nhận. môi trường vận hành (production / 운영 환경) thiết kế (design / 설계) cần chọn defense theo mức độ rủi ro chứ không theo một benchmark chung cho mọi use trường hợp (case / 사례).

Ví dụ dịch vụ đề xuất nội dung có thể chấp nhận fallback mềm, trong khi hệ thống xác minh danh tính hoặc kiểm soát công nghiệp có thể cần thất bại (fail / 실패) closed và human escalation.

> **Chuyển mạch:** Trong **Học máy đối kháng (Adversarial Machine Learning)**, **Dạng thất bại (failure mode / 실패 모드) thường gặp** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프) trong thiết kế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) thường gặp

**Đánh giá quá yếu.** Attack cố định không còn hiệu quả sau khi defense thay đổi, nhưng adaptive attacker vẫn vượt qua được.

**độ dốc (gradient / 기울기) masking.** Defense làm độ dốc (gradient / 기울기) khó dùng nhưng không thật sự làm biên quyết định tốt hơn; attacker có thể chuyển sang kỹ thuật khác hoặc mô hình thay thế.

**Threat mô hình (model / 모델) không thực tế.** Kết quả đẹp trong benchmark nhưng đầu vào (input / 입력) tạo ra không thể tồn tại trong lĩnh vực (domain / 도메인).

**Bảo vệ mô hình (model / 모델) nhưng quên hệ thống (system / 시스템).** Mô hình robust không ngăn được lỗi authorization, parser, retrieval hoặc supply chuỗi (chain / 사슬).

**Phản ứng quá mức.** Bộ lọc quá chặt có thể làm tăng false positive và chặn người dùng hợp lệ.

> **Chuyển mạch:** Ở chặng này của **Học máy đối kháng (Adversarial Machine Learning)**, **Mô hình tư duy** gom các mảnh từ **Dạng thất bại (failure mode / 실패 모드) thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Học máy đối kháng hỏi: nếu phía bên kia cũng đang tối ưu, ranh giới quyết định và chuỗi xử lý (pipeline / 파이프라인) của hệ thống sẽ thất bại ở đâu?**

Mục tiêu môi trường vận hành (production / 운영 환경) không phải chứng minh “không thể bị tấn công”, mà là giới hạn khả năng, chi phí và hậu quả của attacker trong một threat mô hình (model / 모델) rõ ràng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Học máy đối kháng (Adversarial Machine Learning)**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Chịu được nhiễu ngẫu nhiên nghĩa là chịu được tấn công đối kháng”

Không. Attacker chọn đầu vào (input / 입력) có chủ đích thay vì lấy nhiễu ngẫu nhiên.

### “Ẩn mô hình (model / 모델) là đủ”

Không. API vẫn rò rỉ hành vi, còn tính chuyển giao cho phép attacker dùng surrogate mô hình (model / 모델).

### “Một certified radius nghĩa là hệ thống đã secure”

Không. Chứng nhận chỉ bao phủ perturbation mô hình (model / 모델) cụ thể, không bao phủ toàn hệ thống.

### “Robust mô hình (model / 모델) thì không cần hệ thống (system / 시스템) controls”

Không. Authorization, tỷ lệ (rate / 비율) limit, kiểm tra hợp lệ (validation / 검증), sandbox và sự cố (incident / 인시던트) phản hồi (response / 응답) vẫn là các lớp riêng.

> **Chuyển mạch:** Trong **Học máy đối kháng (Adversarial Machine Learning)**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Nên đọc cùng [Robustness và Distribution Shift](../18_evaluation_reliability_interpretability/03_robustness_and_distribution_shift.md), [Red Teaming](../18_evaluation_reliability_interpretability/06_red_teaming_and_adversarial_evaluation.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Data Poisoning](./05_data_poisoning_backdoors_and_model_attacks.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
