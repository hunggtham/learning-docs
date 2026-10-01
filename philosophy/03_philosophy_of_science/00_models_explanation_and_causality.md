# Các mô hình (models / 모델들), Explanation và Causality

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Các mô hình (models / 모델들), Explanation và Causality**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình (model / 모델) không phải bản sao của reality** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Explanation có nhiều dạng** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Mô hình (model / 모델) không phải bản sao của reality

Mô hình (model / 모델) chọn biến, quan hệ và quy mô (scale / 규모) để trả lời một question. Một mô hình (model / 모델) có thể hữu ích dù không “giống thật” ở mọi chi tiết; tiêu chuẩn quan trọng là lĩnh vực (domain / 도메인) of validity, predictive/explanatory use, robustness và dạng thất bại (failure mode / 실패 모드). giả định (assumption / 가정) bị bỏ qua không biến mất — nó quay lại dưới dạng limitation.

> **Chuyển mạch:** Model chọn lọc reality để giải thích một hiện tượng; correlation chỉ mô tả cùng biến thiên, còn intervention mới kiểm tra một quan hệ nhân quả trong điều kiện đã nêu.

## Explanation có nhiều dạng

Mechanistic explanation chỉ ra các thành phần và tương tác. Statistical explanation mô tả mẫu (pattern / 패턴) ổn định trong dữ liệu. Unification nối nhiều hiện tượng dưới một principle. Historical/evolutionary explanation truy dấu quá trình hình thành. Không nên đòi một loại explanation làm công việc của loại khác.

> **Chuyển mạch:** Mechanistic, statistical, unifying và historical explanation trả lời các câu hỏi khác nhau; không loại nào tự tạo ra quan hệ nhân quả. **Correlation, intervention và causality** tiếp theo tách mô tả cùng biến thiên khỏi counterfactual cần thiết để nói “X gây Y”.

## Correlation, intervention và causality

Correlation nói hai biến thay đổi cùng nhau; causality cần một counterfactual: điều gì sẽ xảy ra với cùng hệ đó nếu ta can thiệp vào X? Confounder, selection, sai số đo lường (measurement error / 측정 오차) và phản hồi (feedback / 피드백) có thể tạo correlation giả hoặc che mất tác động (effect / 효과). nhân quả (causal / 인과적) diagram, natural experiment và randomized intervention là các công cụ khác nhau để làm rõ giả định (assumption / 가정), không phải bằng chứng “tự động đúng”.

> **Chuyển mạch:** Correlation chỉ cho biết hai biến cùng thay đổi; intervention đặt câu hỏi về thế giới phản thực và các giả định kiểm soát confounder. **Scientific realism và giới hạn** tiếp theo hỏi mô hình nhân quả đang cam kết điều gì về cấu trúc thực, và cam kết ấy dừng ở đâu.

## Scientific realism và giới hạn

Một người có thể tin rằng mô hình (model / 모델) nắm bắt cấu trúc thực của thế giới ở mức nào đó (realism), hoặc xem mô hình (model / 모델) chủ yếu là công cụ dự đoán (instrumentalism). Lựa chọn này cần được tranh luận theo success, underdetermination, approximate truth và lịch sử thay thế lý thuyết (theory / 이론) — không thể giải quyết chỉ bằng một ví dụ thành công.

Liên hệ trực tiếp với [Mathematics](../../mathematics/README.md), [Physics](../../physics/README.md), [Biology](../../biology/README.md) và [Psychology](../../psychology/README.md), nơi các mô hình có quy mô (scale / 규모), đo lường (measurement / 측정) và nhân quả (causal / 인과적) ranh giới (boundary / 경계) khác nhau.

> **Chuyển mạch:** Realism và instrumentalism đặt ra hai cách đọc thành công của mô hình, nhưng không thay thế kiểm tra causal assumptions. **Worked causal model** đưa confounder, intervention và transportability vào một trường hợp cụ thể; sau đó **model selection** so sánh độ phức tạp với khả năng khái quát.

## Worked nhân quả (causal / 인과적) mô hình (model / 모델)

Claim “ngủ ít làm giảm hiệu năng (performance / 성능)” có thể có nhiều đồ thị (graph / 그래프):

```text
stress → sleep loss → performance
stress → performance
workload → sleep loss và performance
```

Nếu chỉ quan sát sleep và hiệu năng (performance / 성능), confounding từ stress/tải công việc (workload / 워크로드) chưa được loại. Intervention có thể randomize sleep opportunity nhưng vẫn phải kiểm tra adherence, học tập (learning / 학습) tác động (effect / 효과), đo lường (measurement / 측정) và transportability. nhân quả (causal / 인과적) answer không chỉ là “có correlation”; nó là một counterfactual cụ thể: cùng người đó sẽ perform thế nào nếu sleep opportunity khác đi, trong ngữ cảnh (context / 맥락) nào và trên kết quả (outcome / 결과) nào.

> **Chuyển mạch:** Worked example cho thấy một causal claim phụ thuộc population, intervention, outcome và confounder cụ thể; **model selection** kiểm tra liệu mô hình đơn giản hay phức tạp dự đoán tốt ngoài mẫu. **Depth pass** sẽ gom các điều kiện đó thành tiêu chuẩn viết một claim nhân quả có ranh giới.

## Mô hình (model / 모델) selection có giá trị

Mô hình (model / 모델) đơn giản hơn không mặc nhiên đúng. Simplicity hữu ích vì giảm overfitting và làm giả định (assumption / 가정) rõ; mô hình (model / 모델) phức tạp hữu ích nếu cơ chế (mechanism / 메커니즘) thêm explanatory power và generalize tốt hơn. So sánh cần out-of-sample prediction, intervention kiểm thử (test / 테스트), parameter sensitivity và thất bại (failure / 실패) trường hợp (case / 사례) — không chỉ fit trên dữ liệu (data / 데이터) đã dùng để chọn mô hình (model / 모델).

> **Chuyển mạch:** Model selection không chọn “mô hình đúng tuyệt đối”; nó cân bằng fit, overfitting, cơ chế và transportability. **Depth pass** biến kết quả đó thành checklist: định nghĩa intervention, thứ tự thời gian, confounder, đo lường, population và điều kiện thất bại trước khi gọi một association là causality.

## Độ sâu (depth / 깊이) pass: causality như một claim có điều kiện

### Question và definitions

“X gây Y” phải được đọc như một intervention claim: thay X trong population, thời gian (time / 시간) cửa sổ (window / 윈도우) và ngữ cảnh (context / 맥락) xác định sẽ đổi phân phối Y thế nào. Structural equation, potential outcomes và mechanistic explanation dùng ngôn ngữ khác nhau nhưng đều cần ranh giới (boundary / 경계). Association là mẫu (pattern / 패턴); cơ chế (mechanism / 메커니즘) là chuỗi tương tác; nhân quả (causal / 인과적) tác động (effect / 효과) là counterfactual so sánh world có và không có can thiệp.

### Strongest argument và premises

Một nhân quả (causal / 인과적) argument mạnh cần: (1) treatment được định nghĩa đủ rõ; (2) temporal thứ tự (order / 순서); (3) confounder hoặc adjustment chiến lược (strategy / 전략); (4) đo lường (measurement / 측정) không làm sai exposure/kết quả (outcome / 결과); (5) transportability được kiểm tra. DAG giúp lộ premise như exchangeability và no unmeasured confounding; randomized intervention thay một số premise bằng thiết kế (design / 설계) nhưng vẫn cần adherence, interference và kết quả (outcome / 결과) validity.

### Objection, reply và rival position

Objection từ Nancy Cartwright và các nhà cơ chế (mechanism / 메커니즘): average tác động (effect / 효과) có thể không vận chuyển giữa ngữ cảnh (context / 맥락); reply là mô hình phải ghi tác động (effect / 효과) modification và cơ chế (mechanism / 메커니즘) bất biến (invariant / 불변식). Structural realism giữ rằng mô hình (model / 모델) có thể đúng một phần về cấu trúc dù entities lý thuyết thay đổi; instrumentalism nhắc rằng predictive success chưa chứng minh ontology. Không có “gold tiêu chuẩn (standard / 표준)” tách khỏi question.

### Empirical ranh giới (boundary / 경계) và implication

Natural experiment, longitudinal dữ liệu (data / 데이터) và intervention bổ sung nhau; machine-learning prediction có thể hữu ích mà không trả lời “what if”. Khi kết luận, ghi rõ population, intervention, kết quả (outcome / 결과), horizon và dạng thất bại (failure mode / 실패 모드). Implication: chính sách (policy / 정책) nhân quả (causal / 인과적) phải kèm monitoring, pre-specified stopping/revision và phân tích ai chịu spillover, không chỉ báo cáo một tác động (effect / 효과) kích thước (size / 크기).

> **Bàn giao:** Sau **Độ sâu (depth / 깊이) pass: causality như một claim có điều kiện**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
