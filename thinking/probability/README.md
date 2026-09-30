# Probability — Suy nghĩ bằng mức độ bất định

Xác suất (probability / 확률) trong `thinking/` không dạy lại probability theory. Phần formal nằm ở [Mathematics — Probability & Statistics](../../mathematics/06_probability_statistics/01_probability_foundations.md). Ở đây ta học cách **đặt bất định vào quyết định đời thực**.

## 1. Probability là ngôn ngữ của uncertainty

Nhiều câu hỏi không có câu trả lời chắc chắn:

- khoản đầu tư có tăng không;
- bệnh nhân có thật sự mắc bệnh sau một test dương tính không;
- project có trễ deadline không;
- một policy có tạo outcome mong muốn không.

Thay vì ép thành yes/no, hãy hỏi:

```text
What can happen?
How likely is each state?
What evidence changes those probabilities?
What happens if I am wrong?
```

## 2. Base rate trước case-specific evidence

**Base rate** là tần suất nền của một outcome trước khi nhìn evidence riêng của case. Bỏ qua base rate dễ khiến evidence “ấn tượng” được đánh giá quá mạnh.

Ví dụ, một diagnostic test có accuracy cao vẫn có thể tạo nhiều false positives nếu condition rất hiếm. Formal mechanism nằm ở [Conditional Probability & Bayes](../../mathematics/06_probability_statistics/02_conditional_probability_and_bayes.md).

Trong đầu tư, base rate có thể là tỷ lệ doanh nghiệp cùng loại sống sót hoặc tỷ lệ active strategies beat benchmark sau phí. Trong project management, base rate có thể là historical delay của project tương tự.

## 3. Conditional probability

`P(A | B)` không giống `P(B | A)`. Đây là một trong những lỗi đời thường quan trọng nhất.

```text
P(test positive | disease)
≠
P(disease | test positive)
```

Tương tự, “công ty tốt thường có tăng trưởng doanh thu” không đồng nghĩa “mọi công ty có tăng trưởng doanh thu đều là khoản đầu tư tốt”.

## 4. Bayesian updating như một mental model

Không cần luôn tính công thức. Ý tưởng thực hành là:

```text
prior belief
+ new evidence weighted by reliability
→ updated belief
```

Evidence mạnh phải làm belief thay đổi nhiều hơn evidence yếu. Nếu không có evidence nào có thể làm ta đổi ý, đó không còn là calibrated reasoning.

## 5. Independence và correlated failure

Hai rủi ro riêng lẻ không nhất thiết độc lập. Diversification chỉ hiệu quả nếu failures không cùng bị một driver chi phối.

Ví dụ, giữ cổ phiếu của năm công ty cùng ngành có vẻ là năm positions nhưng có thể cùng phụ thuộc lãi suất, regulation hoặc commodity price. Tương tự, nhiều backup đặt cùng một physical location không độc lập trước fire/flood.

## 6. Distribution quan trọng hơn average

Average outcome có thể giống nhau nhưng shape của distribution rất khác. Khi downside bất đối xứng, cần xem variance, tails và probability of ruin. Đi sâu tại [Expectation & Variance](../../mathematics/06_probability_statistics/04_expectation_variance_and_limit_laws.md) và [Risk](../risk/README.md).

## Practical protocol

Trước một quyết định bất định:

1. liệt kê 3–5 trạng thái tương lai chính;
2. gán probability range thay vì giả precision nếu evidence yếu;
3. ghi base rate;
4. ghi evidence riêng của case;
5. kiểm tra các event có correlated không;
6. hỏi evidence nào sẽ làm probability đổi;
7. đưa probabilities sang [Expected Value](../expected-value/README.md) và [Decision Making](../decision-making/README.md).

## Connections

- [Investing](../../investing/README.md): return distributions, scenario analysis, default, drawdown.
- [Research Methods](../../research_methods/README.md): sampling uncertainty, inference và evidence.
- [Psychology](../../psychology/README.md): human calibration, ambiguity và decision under risk.
- [Statistics for Life](../statistics-for-life/README.md): chuyển từ uncertain model sang interpretation of data.
- [Risk](../risk/README.md): probability không đủ; còn phải xét consequence và survivability.