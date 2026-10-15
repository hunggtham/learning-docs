# Value of Information — Khi nào nên tìm hiểu thêm trước khi quyết định

Value of Information (giá trị của thông tin / 정보의 가치) hỏi một câu thực dụng: **thông tin bổ sung có khả năng làm thay đổi quyết định đủ nhiều để đáng với chi phí thu thập không?**

Concept này nối [Probability](../probability/README.md), [Expected Value](../expected-value/README.md), [Decision Making](../decision-making/README.md) và research design.

## 1. Information chỉ có giá trị nếu có thể thay đổi action

Nếu dù kết quả test là A hay B ta vẫn chọn cùng một action, test có thể mang lại curiosity nhưng decision value thấp.

Workflow:

```text
current decision
→ key uncertainty
→ possible information
→ how each result changes belief
→ whether action changes
→ expected improvement
→ cost / delay / risk of obtaining information
```

## 2. Perfect information là upper bound

Expected Value of Perfect Information (EVPI) là giá trị tối đa nếu uncertainty được biết hoàn toàn trước decision.

Trực giác:

```text
EVPI
= expected payoff when state is known before action
- best expected payoff with current information
```

Nếu EVPI rất nhỏ, không có research thực tế nào về uncertainty đó đáng chi nhiều hơn mức này chỉ vì decision quality.

## 3. Sample information thực tế luôn kém hoàn hảo

Survey, test, prototype, interview hoặc experiment đều noisy.

Vì vậy cần hỏi:

- sensitivity/specificity hoặc error rate là bao nhiêu?
- sample đại diện đến đâu?
- result có đến trước deadline không?
- collection cost là gì?
- information có tạo privacy, safety hoặc operational risk không?

## 4. High-value uncertainty

Không phải uncertainty nào cũng đáng research như nhau.

Ưu tiên uncertainty có ba đặc điểm:

```text
large effect on outcome
× high current uncertainty
× plausible ability to learn
```

Một biến có uncertainty lớn nhưng payoff gần như không đổi thì value thấp. Một biến rất quan trọng nhưng không thể học thêm trước deadline cũng không phải research target tốt.

## 5. Prototype như information purchase

Prototype không chỉ là sản phẩm nhỏ. Nó có thể là cách mua information rẻ hơn full commitment.

Ví dụ:

```text
pilot feature
→ observe usage / failure modes
→ update assumptions
→ expand, revise hoặc stop
```

Điều này nối trực tiếp với reversibility và option value trong [Decision Making](../decision-making/README.md).

## 6. Medical test intuition

Một test không tự hữu ích chỉ vì chính xác cao. Value phụ thuộc vào:

```text
pre-test probability
→ test result
→ post-test probability
→ treatment threshold
→ benefit / harm of acting
```

Clinical detail phải handoff về medical evidence/domain chuyên môn; thinking toolkit chỉ cung cấp cấu trúc decision.

## 7. Research stopping rule

Research có diminishing returns. Stop khi:

- information mới ít khả năng đổi action;
- deadline cost bắt đầu lớn;
- uncertainty còn lại không material;
- cost tìm hiểu vượt expected benefit;
- reversible action cho phép học bằng làm thật với risk chấp nhận được.

“Cần thêm dữ liệu” không nên trở thành cách trì hoãn decision vô hạn.

## 8. Checklist

Trước khi mở thêm 20 tab hoặc yêu cầu thêm report, hỏi:

1. Decision nào đang chờ?
2. Uncertainty nào thật sự quyết định giữa options?
3. Kết quả nào sẽ khiến tôi đổi action?
4. Có cách rẻ hơn để học không?
5. Delay có cost gì?
6. Decision reversible đến mức nào?
7. Khi nào tôi sẽ stop researching?

## Connections

- [Probability](../probability/README.md): belief trước và sau evidence.
- [Expected Value](../expected-value/README.md): payoff của information.
- [Decision Making](../decision-making/README.md): action threshold và reversibility.
- [Forecasting](../forecasting/README.md): information làm update prediction.
- [Research Methods](../../research_methods/README.md): measurement và study design.
- [Computer Science](../../computer_science/README.md): prototypes, experiments và observability.
- [PMP](../../pmp/README.md): discovery, risk reduction và staged commitment.