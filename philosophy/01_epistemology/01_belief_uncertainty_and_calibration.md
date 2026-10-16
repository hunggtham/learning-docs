# Belief, bất định (uncertainty / 불확실성) và Calibration

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Belief, bất định (uncertainty / 불확실성) và Calibration**. Route đi từ mức độ tin và uncertainty → xác suất/Bayes → dự báo và calibration → cập nhật khi dữ liệu mới xuất hiện, để độ tự tin phản ánh đúng khả năng sai.

## Tin một điều không phải là nhị phân

Belief có thể biểu diễn như mức độ tin tưởng thay đổi theo bằng chứng (evidence / 증거). xác suất (probability / 확률) là một ngôn ngữ để biểu diễn bất định (uncertainty / 불확실성), nhưng không phải mọi bất định (uncertainty / 불확실성) đều là random chance: có aleatory bất định (uncertainty / 불확실성) từ quá trình và epistemic bất định (uncertainty / 불확실성) từ thiếu kiến thức (knowledge / 지식).

Calibration hỏi: trong các claim được gắn 70% confidence, khoảng 70% có đúng không? Đây là chuẩn thực dụng cho forecasting, diagnosis, science communication và AI. Calibration tốt vẫn có thể sai ở từng trường hợp; nó đánh giá phân phối dự đoán qua nhiều trường hợp.

## Bayes như quy tắc cập nhật

```text
posterior ∝ likelihood × prior
```

Prior không nhất thiết là định kiến tùy tiện; nó ghi lại thông tin trước đó. Likelihood hỏi bằng chứng (evidence / 증거) này phù hợp với hypothesis nào hơn. Một kiểm thử (test / 테스트) có sensitivity cao nhưng cơ sở (base / 기반) tỷ lệ (rate / 비율) thấp vẫn có thể tạo nhiều false positive — đây là lý do cần phân biệt likelihood ratio với “kiểm thử (test / 테스트) positive nghĩa là chắc chắn có bệnh”.

## Ranh giới

Không nên biến mọi câu hỏi giá trị thành một con số xác suất (probability / 확률). xác suất (probability / 확률) giúp quản lý bất định (uncertainty / 불확실성) về claim; nó không tự quyết định điều gì đáng mong muốn, công bằng hay đúng về mặt đạo đức.

## Ví dụ cơ sở (base / 기반) tỷ lệ (rate / 비율)

Giả sử một bệnh có prevalence 1%, kiểm thử (test / 테스트) có sensitivity 90% và specificity 95%. Trong 10.000 người, khoảng 90 người bệnh kiểm thử (test / 테스트) dương tính và khoảng 495 người không bệnh cũng dương tính. Positive predictive giá trị (value / 값) chỉ khoảng 15% (90 / 585), không phải 90%. Người đọc thường nhầm sensitivity với xác suất bệnh khi kiểm thử (test / 테스트) dương tính vì đảo chiều điều kiện trong Bayes.

Ví dụ này cũng cho thấy calibration cần ngữ cảnh (context / 맥락). Một con số “90% accurate” không đủ nếu không biết prevalence, threshold, chi phí (cost / 비용) của false positive/negative và population mà kiểm thử (test / 테스트) được validate.

## Updating mà không overreact

Bằng chứng (evidence / 증거) mạnh khi likelihood ratio lớn, không chỉ vì nó gây ấn tượng. Hãy ghi prior, dự đoán trước bằng chứng (evidence / 증거), cập nhật theo magnitude và kiểm tra posterior predictive: nếu mô hình (model / 모델) không dự đoán được mẫu (pattern / 패턴) mới, vấn đề có thể nằm ở mô hình (model / 모델) chứ không chỉ ở confidence.

> **Bàn giao:** Sau **Updating mà không overreact**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
