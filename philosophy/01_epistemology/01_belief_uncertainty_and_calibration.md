# Belief, Uncertainty và Calibration

## Tin một điều không phải là nhị phân

Belief có thể biểu diễn như mức độ tin tưởng thay đổi theo evidence. Probability là một ngôn ngữ để biểu diễn uncertainty, nhưng không phải mọi uncertainty đều là random chance: có aleatory uncertainty từ quá trình và epistemic uncertainty từ thiếu knowledge.

Calibration hỏi: trong các claim được gắn 70% confidence, khoảng 70% có đúng không? Đây là chuẩn thực dụng cho forecasting, diagnosis, science communication và AI. Calibration tốt vẫn có thể sai ở từng trường hợp; nó đánh giá phân phối dự đoán qua nhiều trường hợp.

## Bayes như quy tắc cập nhật

```text
posterior ∝ likelihood × prior
```

Prior không nhất thiết là định kiến tùy tiện; nó ghi lại thông tin trước đó. Likelihood hỏi evidence này phù hợp với hypothesis nào hơn. Một test có sensitivity cao nhưng base rate thấp vẫn có thể tạo nhiều false positive — đây là lý do cần phân biệt likelihood ratio với “test positive nghĩa là chắc chắn có bệnh”.

## Ranh giới

Không nên biến mọi câu hỏi giá trị thành một con số probability. Probability giúp quản lý uncertainty về claim; nó không tự quyết định điều gì đáng mong muốn, công bằng hay đúng về mặt đạo đức.

## Ví dụ base rate

Giả sử một bệnh có prevalence 1%, test có sensitivity 90% và specificity 95%. Trong 10.000 người, khoảng 90 người bệnh test dương tính và khoảng 495 người không bệnh cũng dương tính. Positive predictive value chỉ khoảng 15% (90 / 585), không phải 90%. Người đọc thường nhầm sensitivity với xác suất bệnh khi test dương tính vì đảo chiều điều kiện trong Bayes.

Ví dụ này cũng cho thấy calibration cần context. Một con số “90% accurate” không đủ nếu không biết prevalence, threshold, cost của false positive/negative và population mà test được validate.

## Updating mà không overreact

Evidence mạnh khi likelihood ratio lớn, không chỉ vì nó gây ấn tượng. Hãy ghi prior, dự đoán trước evidence, cập nhật theo magnitude và kiểm tra posterior predictive: nếu model không dự đoán được pattern mới, vấn đề có thể nằm ở model chứ không chỉ ở confidence.
