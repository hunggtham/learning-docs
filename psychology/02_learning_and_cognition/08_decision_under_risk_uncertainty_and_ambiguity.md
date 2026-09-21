# Ra quyết định dưới rủi ro, bất định và mơ hồ — Decision under Risk, Uncertainty & Ambiguity

Ra quyết định trong đời thực hiếm khi xảy ra khi ta biết chắc kết quả. Phần lớn lựa chọn nằm giữa ba trạng thái: **rủi ro (risk)** khi có thể ước lượng xác suất; **bất định (uncertainty)** khi xác suất chưa rõ; và **mơ hồ (ambiguity)** khi ngay cả cấu trúc của bài toán còn chưa biết đầy đủ.

## Expected value chưa đủ

Nếu chỉ nhân mỗi outcome với probability rồi cộng lại, ta có **giá trị kỳ vọng (expected value)**. Đây là công cụ quan trọng, nhưng con người không trải nghiệm mọi thay đổi tiền bạc, thời gian hay sức khỏe theo tuyến tính.

Mất 1 triệu khi chỉ còn 2 triệu có ý nghĩa khác mất 1 triệu khi có 2 tỷ. Vì vậy normative decision theory dùng **utility** để mô tả giá trị chủ quan của outcome thay vì chỉ dùng số tiền tuyệt đối.

## Expected Utility Theory

**Lý thuyết lợi ích kỳ vọng (Expected Utility Theory)** mô tả lựa chọn nhất quán khi người ra quyết định có preference ổn định và tuân theo một số tiên đề. Nó là benchmark hữu ích để đánh giá quyết định, nhưng không phải mô tả hoàn hảo hành vi thật.

Một người có thể từ chối gamble có expected value dương vì utility của mất mát lớn hơn utility của lợi ích tương ứng. Điều này không nhất thiết phi lý; nó có thể phản ánh constraint tài chính hoặc hậu quả bất đối xứng.

## Prospect Theory

**Prospect Theory** cho thấy con người thường đánh giá outcome tương đối so với **điểm tham chiếu (reference point)** thay vì chỉ theo mức cuối cùng. Hai ý nổi bật là **loss aversion** và **probability weighting**.

Loss aversion mô tả xu hướng mất mát thường có tác động tâm lý mạnh hơn lợi ích cùng độ lớn. Probability weighting mô tả việc con người không dùng xác suất theo cách tuyến tính: xác suất rất nhỏ có thể được overweight, còn một số xác suất trung bình-cao có thể bị xử lý khác với tính toán chuẩn.

## Framing

Cùng một outcome có thể dẫn tới lựa chọn khác nếu được mô tả theo gain hoặc loss. Đây là **hiệu ứng khung (framing effect)**.

Một treatment nói “90% sống sót” và “10% tử vong” có cùng arithmetic nhưng có thể tạo cảm giác khác. Trong product, “giữ được 20 phút mỗi ngày” và “đang mất 10 giờ mỗi tháng” cũng là hai framing khác nhau.

Framing không chỉ là thao túng; nó nhắc rằng representation của problem là một phần của decision process.

## Ambiguity aversion

Con người thường thích option có probability rõ hơn option có probability không rõ, ngay cả khi expected outcome có thể tương tự. Đây là **né tránh mơ hồ (ambiguity aversion)**.

Trong engineering, một solution quen thuộc nhưng mediocre đôi khi được chọn hơn architecture mới có upside lớn vì uncertainty về failure mode. Đây có thể là lựa chọn hợp lý nếu switching cost lớn, nhưng cũng có thể giữ organization trong local optimum.

## Description–experience gap

Con người phản ứng khác với risk khi đọc probability trên giấy so với khi học từ trải nghiệm lặp lại. Khi học qua experience, rare event có thể bị under-sampled vì đơn giản là chưa xảy ra trong sample cá nhân.

Một team vận hành hệ thống 2 năm không gặp outage lớn dễ conclude architecture rất an toàn, dù true tail risk chưa biến mất.

## Base rate và conditional probability

Một sai lầm thường gặp là bỏ qua **tỷ lệ nền (base rate)**. Nếu một test có false-positive nhỏ nhưng condition rất hiếm, phần lớn positive result vẫn có thể là false positive.

Dùng **tần suất tự nhiên (natural frequencies)** thường giúp reasoning tốt hơn. Thay vì nói “sensitivity 90%, specificity 95%, prevalence 1%”, có thể mô tả trên 10.000 người để thấy số true positive và false positive cụ thể.

Xem [[../00_foundations/09_replication_meta_analysis_and_bayesian_reasoning]].

## Regret và counterfactual thinking

Decision không kết thúc khi outcome xuất hiện. Con người so sánh outcome thật với alternative tưởng tượng: “giá mà mình chọn khác”. Đây là **tư duy phản thực (counterfactual thinking)**.

Regret có thể hữu ích khi nó cập nhật strategy; nó trở nên kém hữu ích khi đánh giá quyết định chỉ dựa vào outcome. Một good decision có thể cho bad outcome vì luck, và bad decision có thể may mắn cho good outcome.

## Outcome bias

**Thiên lệch kết quả (outcome bias)** là đánh giá chất lượng quyết định dựa quá nhiều vào outcome sau khi biết kết quả. Trong postmortem, điều này dễ biến một decision hợp lý dưới uncertainty thành “rõ ràng sai” chỉ vì outcome xấu.

Decision log ghi information, estimate và assumption trước outcome giúp giữ lại uncertainty thật tại thời điểm quyết định.

## Temporal discounting

Con người thường discount reward ở tương lai. **Chiết khấu theo thời gian (temporal discounting)** giúp giải thích vì sao lợi ích nhỏ ngay lập tức có thể thắng lợi ích lớn nhưng xa hơn.

Điều này xuất hiện trong saving, exercise, học tập, technical debt và maintenance. Developer biết refactor hôm nay có lợi tháng sau nhưng deadline hiện tại tạo immediate reward rõ hơn.

Xem [[12_temporal_cognition_prospective_memory_and_time]].

## Pre-mortem

**Pre-mortem** là giả định kế hoạch đã thất bại rồi hỏi “điều gì có thể đã gây ra failure?”. Kỹ thuật này giúp tạo hypothesis tiêu cực mà optimism hoặc commitment có thể đang suppress.

Pre-mortem không thay thế quantitative risk analysis, nhưng hữu ích để mở search space trước khi team quá gắn với một plan.

## Decision hygiene

Decision hygiene tập trung thiết kế process thay vì mong “con người bớt bias”. Một process tốt có thể dùng independent estimate trước discussion, checklist assumption, base-rate reference, red-team review, threshold rõ và decision log.

Mục tiêu không phải xóa bias hoàn toàn mà giảm việc cùng một case cho kết quả quá khác chỉ vì noise hoặc framing ngẫu nhiên.

## Những hiểu lầm phổ biến

**“Bias nghĩa là con người phi lý.”** Nhiều heuristic là adaptive trong một số environment.

**“Nếu biết xác suất thì quyết định đúng là option có expected value cao nhất.”** Constraint, utility và downside có thể làm lựa chọn khác vẫn hợp lý.

**“Loss aversion luôn giống nhau ở mọi người và mọi domain.”** Effect phụ thuộc task, stake, framing và reference point.

**“Good outcome chứng minh decision tốt.”** Outcome và decision quality cần tách nhau.

## Mô hình tư duy

```text
information
 + probability estimate
 + utility / constraint
 + reference point
 + time horizon
 + uncertainty about model itself
                ↓
             decision
                ↓
      outcome + learning update
```

> Chất lượng ra quyết định nên được đánh giá bằng process và information có sẵn tại thời điểm chọn, không chỉ bằng outcome xảy ra sau đó.

## Kết nối kiến thức

Xem [[02_thinking_language_and_decision]], [[04_cognitive_biases_and_metacognition]], [[12_temporal_cognition_prospective_memory_and_time]], [[../00_foundations/08_causal_inference_and_psychological_evidence]], [[../90_connections/03_risk_uncertainty_and_science_communication]] và [[../06_applied/02_hci_ai_and_human_decision_support]].
