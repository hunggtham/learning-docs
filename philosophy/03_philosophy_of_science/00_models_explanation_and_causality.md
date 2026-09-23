# Models, Explanation và Causality

## Model không phải bản sao của reality

Model chọn biến, quan hệ và scale để trả lời một question. Một model có thể hữu ích dù không “giống thật” ở mọi chi tiết; tiêu chuẩn quan trọng là domain of validity, predictive/explanatory use, robustness và failure mode. Assumption bị bỏ qua không biến mất — nó quay lại dưới dạng limitation.

## Explanation có nhiều dạng

Mechanistic explanation chỉ ra các thành phần và tương tác. Statistical explanation mô tả pattern ổn định trong dữ liệu. Unification nối nhiều hiện tượng dưới một principle. Historical/evolutionary explanation truy dấu quá trình hình thành. Không nên đòi một loại explanation làm công việc của loại khác.

## Correlation, intervention và causality

Correlation nói hai biến thay đổi cùng nhau; causality cần một counterfactual: điều gì sẽ xảy ra với cùng hệ đó nếu ta can thiệp vào X? Confounder, selection, measurement error và feedback có thể tạo correlation giả hoặc che mất effect. Causal diagram, natural experiment và randomized intervention là các công cụ khác nhau để làm rõ assumption, không phải bằng chứng “tự động đúng”.

## Scientific realism và giới hạn

Một người có thể tin rằng model nắm bắt cấu trúc thực của thế giới ở mức nào đó (realism), hoặc xem model chủ yếu là công cụ dự đoán (instrumentalism). Lựa chọn này cần được tranh luận theo success, underdetermination, approximate truth và lịch sử thay thế theory — không thể giải quyết chỉ bằng một ví dụ thành công.

Liên hệ trực tiếp với [Mathematics](../../mathematics/README.md), [Physics](../../physics/README.md), [Biology](../../biology/README.md) và [Psychology](../../psychology/README.md), nơi các mô hình có scale, measurement và causal boundary khác nhau.

## Worked causal model

Claim “ngủ ít làm giảm performance” có thể có nhiều graph:

```text
stress → sleep loss → performance
stress → performance
workload → sleep loss và performance
```

Nếu chỉ quan sát sleep và performance, confounding từ stress/workload chưa được loại. Intervention có thể randomize sleep opportunity nhưng vẫn phải kiểm tra adherence, learning effect, measurement và transportability. Causal answer không chỉ là “có correlation”; nó là một counterfactual cụ thể: cùng người đó sẽ perform thế nào nếu sleep opportunity khác đi, trong context nào và trên outcome nào.

## Model selection có giá trị

Model đơn giản hơn không mặc nhiên đúng. Simplicity hữu ích vì giảm overfitting và làm assumption rõ; model phức tạp hữu ích nếu mechanism thêm explanatory power và generalize tốt hơn. So sánh cần out-of-sample prediction, intervention test, parameter sensitivity và failure case — không chỉ fit trên data đã dùng để chọn model.

## Depth pass: causality như một claim có điều kiện

### Question và definitions

“X gây Y” phải được đọc như một intervention claim: thay X trong population, time window và context xác định sẽ đổi phân phối Y thế nào. Structural equation, potential outcomes và mechanistic explanation dùng ngôn ngữ khác nhau nhưng đều cần boundary. Association là pattern; mechanism là chuỗi tương tác; causal effect là counterfactual so sánh world có và không có can thiệp.

### Strongest argument và premises

Một causal argument mạnh cần: (1) treatment được định nghĩa đủ rõ; (2) temporal order; (3) confounder hoặc adjustment strategy; (4) measurement không làm sai exposure/outcome; (5) transportability được kiểm tra. DAG giúp lộ premise như exchangeability và no unmeasured confounding; randomized intervention thay một số premise bằng design nhưng vẫn cần adherence, interference và outcome validity.

### Objection, reply và rival position

Objection từ Nancy Cartwright và các nhà mechanism: average effect có thể không vận chuyển giữa context; reply là mô hình phải ghi effect modification và mechanism invariant. Structural realism giữ rằng model có thể đúng một phần về cấu trúc dù entities lý thuyết thay đổi; instrumentalism nhắc rằng predictive success chưa chứng minh ontology. Không có “gold standard” tách khỏi question.

### Empirical boundary và implication

Natural experiment, longitudinal data và intervention bổ sung nhau; machine-learning prediction có thể hữu ích mà không trả lời “what if”. Khi kết luận, ghi rõ population, intervention, outcome, horizon và failure mode. Implication: policy causal phải kèm monitoring, pre-specified stopping/revision và phân tích ai chịu spillover, không chỉ báo cáo một effect size.
