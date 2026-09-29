# Các mô hình (models / 모델들), Explanation và Causality

> **Mạch đọc:** Đọc **các mô hình (models / 모델들), Explanation và Causality** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **mô hình (model / 모델) không phải bản sao của reality** sang **Explanation có nhiều dạng**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

## Mô hình (model / 모델) không phải bản sao của reality

Mô hình (model / 모델) chọn biến, quan hệ và quy mô (scale / 규모) để trả lời một question. Một mô hình (model / 모델) có thể hữu ích dù không “giống thật” ở mọi chi tiết; tiêu chuẩn quan trọng là lĩnh vực (domain / 도메인) of validity, predictive/explanatory use, robustness và dạng thất bại (failure mode / 실패 모드). giả định (assumption / 가정) bị bỏ qua không biến mất — nó quay lại dưới dạng limitation.


> **Chuyển mạch:** Từ **mô hình (model / 모델) không phải bản sao của reality**, ta sang **Explanation có nhiều dạng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Explanation có nhiều dạng

Mechanistic explanation chỉ ra các thành phần và tương tác. Statistical explanation mô tả mẫu (pattern / 패턴) ổn định trong dữ liệu. Unification nối nhiều hiện tượng dưới một principle. Historical/evolutionary explanation truy dấu quá trình hình thành. Không nên đòi một loại explanation làm công việc của loại khác.


> **Chuyển mạch:** Từ **Explanation có nhiều dạng**, ta sang **Correlation, intervention và causality** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Correlation, intervention và causality

Correlation nói hai biến thay đổi cùng nhau; causality cần một counterfactual: điều gì sẽ xảy ra với cùng hệ đó nếu ta can thiệp vào X? Confounder, selection, sai số đo lường (measurement error / 측정 오차) và phản hồi (feedback / 피드백) có thể tạo correlation giả hoặc che mất tác động (effect / 효과). nhân quả (causal / 인과적) diagram, natural experiment và randomized intervention là các công cụ khác nhau để làm rõ giả định (assumption / 가정), không phải bằng chứng “tự động đúng”.


> **Chuyển mạch:** Từ **Correlation, intervention và causality**, ta sang **Scientific realism và giới hạn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Scientific realism và giới hạn

Một người có thể tin rằng mô hình (model / 모델) nắm bắt cấu trúc thực của thế giới ở mức nào đó (realism), hoặc xem mô hình (model / 모델) chủ yếu là công cụ dự đoán (instrumentalism). Lựa chọn này cần được tranh luận theo success, underdetermination, approximate truth và lịch sử thay thế lý thuyết (theory / 이론) — không thể giải quyết chỉ bằng một ví dụ thành công.

Liên hệ trực tiếp với [Mathematics](../../mathematics/README.md), [Physics](../../physics/README.md), [Biology](../../biology/README.md) và [Psychology](../../psychology/README.md), nơi các mô hình có quy mô (scale / 규모), đo lường (measurement / 측정) và nhân quả (causal / 인과적) ranh giới (boundary / 경계) khác nhau.


> **Chuyển mạch:** Từ **Scientific realism và giới hạn**, ta sang **Worked nhân quả (causal / 인과적) mô hình (model / 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Worked nhân quả (causal / 인과적) mô hình (model / 모델)

Claim “ngủ ít làm giảm hiệu năng (performance / 성능)” có thể có nhiều đồ thị (graph / 그래프):

```text
stress → sleep loss → performance
stress → performance
workload → sleep loss và performance
```

Nếu chỉ quan sát sleep và hiệu năng (performance / 성능), confounding từ stress/tải công việc (workload / 워크로드) chưa được loại. Intervention có thể randomize sleep opportunity nhưng vẫn phải kiểm tra adherence, học tập (learning / 학습) tác động (effect / 효과), đo lường (measurement / 측정) và transportability. nhân quả (causal / 인과적) answer không chỉ là “có correlation”; nó là một counterfactual cụ thể: cùng người đó sẽ perform thế nào nếu sleep opportunity khác đi, trong ngữ cảnh (context / 맥락) nào và trên kết quả (outcome / 결과) nào.


> **Chuyển mạch:** Từ **Worked nhân quả (causal / 인과적) mô hình (model / 모델)**, ta sang **mô hình (model / 모델) selection có giá trị** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình (model / 모델) selection có giá trị

Mô hình (model / 모델) đơn giản hơn không mặc nhiên đúng. Simplicity hữu ích vì giảm overfitting và làm giả định (assumption / 가정) rõ; mô hình (model / 모델) phức tạp hữu ích nếu cơ chế (mechanism / 메커니즘) thêm explanatory power và generalize tốt hơn. So sánh cần out-of-sample prediction, intervention kiểm thử (test / 테스트), parameter sensitivity và thất bại (failure / 실패) trường hợp (case / 사례) — không chỉ fit trên dữ liệu (data / 데이터) đã dùng để chọn mô hình (model / 모델).


> **Chuyển mạch:** Từ **mô hình (model / 모델) selection có giá trị**, ta sang **độ sâu (depth / 깊이) pass: causality như một claim có điều kiện** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ sâu (depth / 깊이) pass: causality như một claim có điều kiện

### Question và definitions

“X gây Y” phải được đọc như một intervention claim: thay X trong population, thời gian (time / 시간) cửa sổ (window / 윈도우) và ngữ cảnh (context / 맥락) xác định sẽ đổi phân phối Y thế nào. Structural equation, potential outcomes và mechanistic explanation dùng ngôn ngữ khác nhau nhưng đều cần ranh giới (boundary / 경계). Association là mẫu (pattern / 패턴); cơ chế (mechanism / 메커니즘) là chuỗi tương tác; nhân quả (causal / 인과적) tác động (effect / 효과) là counterfactual so sánh world có và không có can thiệp.

### Strongest argument và premises

Một nhân quả (causal / 인과적) argument mạnh cần: (1) treatment được định nghĩa đủ rõ; (2) temporal thứ tự (order / 순서); (3) confounder hoặc adjustment chiến lược (strategy / 전략); (4) đo lường (measurement / 측정) không làm sai exposure/kết quả (outcome / 결과); (5) transportability được kiểm tra. DAG giúp lộ premise như exchangeability và no unmeasured confounding; randomized intervention thay một số premise bằng thiết kế (design / 설계) nhưng vẫn cần adherence, interference và kết quả (outcome / 결과) validity.

### Objection, reply và rival position

Objection từ Nancy Cartwright và các nhà cơ chế (mechanism / 메커니즘): average tác động (effect / 효과) có thể không vận chuyển giữa ngữ cảnh (context / 맥락); reply là mô hình phải ghi tác động (effect / 효과) modification và cơ chế (mechanism / 메커니즘) bất biến (invariant / 불변식). Structural realism giữ rằng mô hình (model / 모델) có thể đúng một phần về cấu trúc dù entities lý thuyết thay đổi; instrumentalism nhắc rằng predictive success chưa chứng minh ontology. Không có “gold tiêu chuẩn (standard / 표준)” tách khỏi question.

### Empirical ranh giới (boundary / 경계) và implication

Natural experiment, longitudinal dữ liệu (data / 데이터) và intervention bổ sung nhau; machine-learning prediction có thể hữu ích mà không trả lời “what if”. Khi kết luận, ghi rõ population, intervention, kết quả (outcome / 결과), horizon và dạng thất bại (failure mode / 실패 모드). Implication: chính sách (policy / 정책) nhân quả (causal / 인과적) phải kèm monitoring, pre-specified stopping/revision và phân tích ai chịu spillover, không chỉ báo cáo một tác động (effect / 효과) kích thước (size / 크기).

> **Bàn giao:** Sau **Empirical ranh giới (boundary / 경계) và implication**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 scientific realism laws and underdetermination](./01_scientific_realism_laws_and_underdetermination.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
