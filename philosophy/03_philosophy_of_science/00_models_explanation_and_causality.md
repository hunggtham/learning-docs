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
