# Xác suất → hiệu chuẩn → quyết định và rủi ro

> **Mạch đọc:** Chapter này không tạo một lĩnh vực (domain / 도메인) “decision science” mới. Nó là tuyến liên kết (connection route / 연결 경로) nối nền xác suất (probability / 확률) và thống kê (statistics / 통계) đã có trong Mathematics với đo lường bằng chứng (evidence / 증거), đánh giá mô hình (model evaluation / 모델 평가) và quyết định dưới bất định (decision under uncertainty / 불확실성하 의사결정). Nếu chưa chắc về xác suất có điều kiện (conditional probability / 조건부 확률), kỳ vọng (expectation / 기댓값) hoặc phân phối xác suất (probability distribution / 확률 분포), nên đọc [xác suất có điều kiện và Bayes](../06_probability_statistics/02_conditional_probability_and_bayes.md), [kỳ vọng và phương sai](../06_probability_statistics/04_expectation_variance_and_limit_laws.md) và [thống kê suy luận](../06_probability_statistics/05_descriptive_and_inferential_statistics.md) trước.

Câu hỏi trung tâm của chapter là: **một con số xác suất tốt trở thành một quyết định tốt bằng cách nào?** Xác suất mô tả mức độ bất định; hiệu chuẩn (calibration / 보정) kiểm tra xem các xác suất đó có khớp với tần suất quan sát hay không; hàm mất mát (loss function / 손실 함수), tiện ích (utility / 효용) và ràng buộc (constraint / 제약조건) chuyển niềm tin thành hành động. Vì vậy đường đi đúng không phải `prediction → action`, mà là:

```text
uncertain world
→ evidence
→ probability estimate
→ calibration + discrimination check
→ consequences / costs / utility
→ decision threshold or policy
→ observed outcome
→ feedback and recalibration
```

## 1. Xác suất là biểu diễn của bất định, chưa phải quyết định

Một dự báo xác suất (probabilistic forecast / 확률 예측) như “xác suất xảy ra sự kiện là 70%” không nói trực tiếp ta nên làm gì. Nó chỉ mô tả niềm tin định lượng về một biến cố. Hai người có cùng xác suất 70% vẫn có thể chọn hành động khác nhau nếu hậu quả, mức chịu rủi ro, ngân sách hoặc ràng buộc khác nhau.

Đây là ranh giới quan trọng giữa **suy luận (inference / 추론)** và **quyết định (decision / 의사결정)**. Suy luận hỏi “điều gì có khả năng đúng?”. Quyết định hỏi “với những gì ta biết và các hậu quả có thể xảy ra, hành động nào phù hợp với mục tiêu?”. Nhầm hai câu hỏi làm người học dễ biến một dự báo tốt thành một quy tắc hành động máy móc.

Ví dụ, một hệ thống dự báo 10% khả năng giao dịch là gian lận. Nếu chặn nhầm một giao dịch hợp lệ chỉ gây một ít ma sát, ngưỡng hành động có thể thấp. Nếu chặn nhầm làm mất khách hàng lớn hoặc tạo nghĩa vụ pháp lý, cùng xác suất 10% có thể chưa đủ để hành động. Ta cần một lớp bổ sung: chi phí và lợi ích của mỗi kết quả.

> **Chuyển mạch:** Trước khi tối ưu hành động, cần biết xác suất đầu vào có đáng tin không. Đó là vai trò của hiệu chuẩn (calibration / 보정).

## 2. Hiệu chuẩn trả lời “70% có thật sự giống 70% không?”

Một mô hình dự báo được **hiệu chuẩn tốt (well-calibrated / 잘 보정된)** khi trong nhóm các trường hợp được gán xác suất gần `p`, biến cố xảy ra với tần suất gần `p` trong dài hạn, với điều kiện population và cơ chế sinh dữ liệu đủ ổn định.

Nếu một mô hình đưa ra 100 dự báo quanh 0,70 và khoảng 70 trường hợp xảy ra, nhóm đó có bằng chứng hiệu chuẩn tốt hơn một mô hình mà chỉ 40 trường hợp xảy ra. Nhưng một nhóm nhỏ không đủ để kết luận mạnh; ta còn phải xem kích thước mẫu (sample size / 표본 크기), khoảng bất định (uncertainty interval / 불확실성 구간), sự dịch chuyển phân phối (distribution shift / 분포 이동) và cách chia bin.

Hiệu chuẩn (calibration / 보정) là một thuộc tính của **xác suất dự báo**, không phải chỉ của nhãn cuối cùng. Một bộ phân loại có độ chính xác (accuracy / 정확도) cao vẫn có thể dự báo xác suất quá tự tin. Ngược lại, một mô hình có hiệu chuẩn tốt vẫn có thể phân biệt trường hợp dương và âm kém nếu mọi dự báo đều gần tỷ lệ nền.

### Ví dụ tối giản

Giả sử biến cố xảy ra 20% trong population. Hai mô hình dự báo 1.000 trường hợp:

```text
Model A: hầu hết dự báo quanh 0.20
Model B: một số quanh 0.05, một số quanh 0.80
```

Nếu cả hai đều hiệu chuẩn, Model B thường hữu ích hơn cho quyết định vì nó tách được các trường hợp rủi ro thấp và cao. Điều này đưa ta tới khái niệm tiếp theo: **khả năng phân biệt (discrimination / 판별력)**.

## 3. Hiệu chuẩn và khả năng phân biệt là hai trục khác nhau

**Hiệu chuẩn (calibration / 보정)** hỏi xác suất có đúng mức hay không. **Khả năng phân biệt (discrimination / 판별력)** hỏi mô hình có xếp các trường hợp có biến cố cao hơn các trường hợp không có biến cố hay không. Một mô hình hữu ích thường cần cả hai, nhưng hai thuộc tính không thay thế nhau.

Một dự báo luôn bằng tỷ lệ nền 20% có thể được hiệu chuẩn hoàn hảo nếu dữ liệu thật đúng 20%, nhưng nó không giúp chọn trường hợp nào cần ưu tiên. Một mô hình xếp hạng rất tốt nhưng luôn đẩy 60% thành 90% và 20% thành 50% có thể có khả năng phân biệt tốt nhưng hiệu chuẩn kém; nếu ta dùng xác suất đó để tính kỳ vọng tiền tệ hoặc thiết lập ngưỡng hành động, sai số hiệu chuẩn sẽ đi thẳng vào quyết định.

Vì vậy, khi đánh giá một hệ thống dự báo, không nên hỏi một câu “mô hình chính xác bao nhiêu?”. Cần tách ít nhất ba câu:

1. xác suất có hiệu chuẩn không;
2. mô hình có phân biệt/ranking hữu ích không;
3. với chi phí và mục tiêu thực tế, quyết định tạo ra từ mô hình có tốt hơn baseline không.

Ba câu này tương ứng với ba lớp `belief → ranking → action`.

## 4. Quy tắc chấm điểm đúng đắn giúp thưởng dự báo xác suất trung thực

Để đánh giá dự báo xác suất, ta cần quy tắc chấm điểm đúng đắn (proper scoring rule / 적정 점수 규칙): về kỳ vọng, người dự báo đạt điểm tốt nhất khi báo đúng xác suất mà họ thực sự tin dựa trên thông tin đang có.

### Brier score

Với biến cố nhị phân `y ∈ {0,1}` và dự báo `p`, **điểm Brier (Brier score / 브라이어 점수)** là:

```text
Brier = (p - y)^2
```

Điểm càng nhỏ càng tốt. Dự báo 0,90 nhưng biến cố không xảy ra bị phạt mạnh hơn dự báo 0,60. Đây là một cách rất trực quan để thấy sự tự tin sai có giá.

### Log loss

**Mất mát logarit (log loss / 로그 손실)** phạt đặc biệt mạnh các dự báo cực kỳ tự tin nhưng sai:

```text
log loss = -[y log(p) + (1-y) log(1-p)]
```

Nếu `p` tiến sát 1 nhưng `y = 0`, mất mát tăng rất lớn. Điều này phù hợp với nhiều hệ thống nơi “gần như chắc chắn” là một tuyên bố mạnh và phải có bằng chứng tương xứng.

Không có một score duy nhất trả lời toàn bộ bài toán. Quy tắc chấm điểm đo chất lượng dự báo; nó chưa mã hóa toàn bộ chi phí kinh doanh, rủi ro vận hành hoặc quyền ưu tiên của người ra quyết định. Do đó score tốt là điều kiện hữu ích nhưng chưa đủ cho policy tốt.

> **Chuyển mạch:** Khi xác suất đã được đo và kiểm tra, bước tiếp theo là ánh xạ kết quả có thể xảy ra thành giá trị hoặc tổn thất.

## 5. Từ xác suất sang quyết định: tổn thất kỳ vọng và tiện ích kỳ vọng

Giả sử ta có các hành động `a` và các trạng thái thế giới `s`. Mỗi cặp `(a, s)` tạo một tổn thất (loss / 손실) `L(a,s)`. Với xác suất hiện tại `P(s|evidence)`, ta có **tổn thất kỳ vọng (expected loss / 기대 손실)**:

```text
E[L | a] = Σ_s P(s | evidence) · L(a, s)
```

Một quy tắc quyết định cơ bản là chọn hành động có tổn thất kỳ vọng thấp nhất trong số hành động hợp lệ. Viết bằng tiện ích (utility / 효용) thì tương đương với tối đa hóa **tiện ích kỳ vọng (expected utility / 기대 효용)**.

Điểm quan trọng nằm ở chỗ `P(s|evidence)` và `L(a,s)` là hai loại tri thức khác nhau. Xác suất thuộc lớp mô tả bất định; hàm mất mát thuộc lớp mục tiêu/hậu quả. Tranh luận về “xác suất đúng” không giải quyết được bất đồng về giá trị, và thay đổi cost matrix không có nghĩa mô hình xác suất thay đổi.

### Ví dụ ngưỡng hành động

Ta cân nhắc một hành động phòng ngừa có chi phí `C_action`. Nếu không hành động và biến cố xấu xảy ra, tổn thất là `C_failure`. Bỏ qua các chi tiết khác, hành động hợp lý khi:

```text
p · C_failure > C_action
```

hay:

```text
p > C_action / C_failure
```

Tỷ lệ bên phải tạo một **ngưỡng quyết định (decision threshold / 의사결정 임계값)**. Ngưỡng không phải thuộc tính cố định của mô hình; nó sinh từ hậu quả. Khi chi phí thay đổi, ngưỡng tối ưu có thể thay đổi dù mô hình và dữ liệu không đổi.

## 6. Sai dương và sai âm chỉ có nghĩa khi gắn với hậu quả

Trong phân loại nhị phân, **dương tính giả (false positive / 거짓 양성)** và **âm tính giả (false negative / 거짓 음성)** không có mức nghiêm trọng cố định. Tùy lĩnh vực, một loại có thể đắt hơn nhiều loại còn lại.

Ví dụ trong phát hiện gian lận, âm tính giả có thể gây mất tiền; dương tính giả có thể làm khách hàng hợp lệ bị từ chối. Trong hệ thống cảnh báo vận hành, dương tính giả tạo mệt mỏi cảnh báo (alert fatigue / 경보 피로), còn âm tính giả làm sự cố bị bỏ sót. Trong đầu tư, một “tín hiệu sai” có thể tạo chi phí giao dịch và rủi ro vị thế; bỏ lỡ một cơ hội lại là chi phí cơ hội khác.

Vì vậy, ma trận nhầm lẫn (confusion matrix / 혼동 행렬) chỉ là thống kê trung gian. Muốn ra quyết định phải nối nó với phân phối hậu quả, quy mô tổn thất và ràng buộc hành động.

## 7. Tỷ lệ nền quyết định cách ta đọc bằng chứng

**Tỷ lệ nền (base rate / 기저율)** là tần suất trước khi quan sát bằng chứng cụ thể. Khi một biến cố hiếm, ngay cả test có sensitivity/specificity cao vẫn có thể tạo nhiều dương tính giả nếu áp dụng trên population rất rộng. Đây là ứng dụng trực tiếp của Bayes chứ không phải một mẹo riêng.

Một sai lầm phổ biến là đọc `P(test positive | event)` như `P(event | test positive)`. Hai đại lượng khác nhau. Từ [Bayes](../06_probability_statistics/02_conditional_probability_and_bayes.md), ta biết posterior còn phụ thuộc prior/base rate.

Trong quyết định thực tế, bỏ qua tỷ lệ nền (base rate / 기저율) tạo hai lỗi liên tiếp: xác suất hậu nghiệm bị phóng đại, rồi ngưỡng hành động được áp dụng trên một xác suất sai. Vì vậy pipeline tốt phải kiểm tra population trước cả calibration lẫn policy.

## 8. Hiệu chuẩn không bất biến khi môi trường thay đổi

Một mô hình hiệu chuẩn tốt trên dữ liệu lịch sử có thể mất hiệu chuẩn sau **dịch chuyển phân phối (distribution shift / 분포 이동)**. Có nhiều cơ chế:

- tỷ lệ nền thay đổi theo thời gian;
- hành vi người dùng thay đổi;
- dữ liệu đầu vào được đo bằng công cụ mới;
- policy của chính hệ thống làm thay đổi population quan sát;
- chỉ các trường hợp được hành động mới có nhãn kết quả, tạo selection bias.

Điểm cuối đặc biệt quan trọng: nếu dự báo khiến ta can thiệp, outcome sau đó không còn là counterfactual “nếu không can thiệp”. Hệ thống quyết định tự tạo dữ liệu cho lần học tiếp theo. Đây là vòng phản hồi (feedback loop / 피드백 루프), và calibration monitoring phải hiểu chính sách sinh dữ liệu chứ không chỉ vẽ reliability diagram.

Do đó, hiệu chuẩn (calibration / 보정) cần được gắn với thời gian, cohort và phiên bản mô hình. Một giá trị tổng hợp trên toàn lịch sử có thể che drift gần đây.

## 9. Giá trị của thông tin: đo xem bằng chứng mới có đáng thu thập không

Không phải mọi bất định đều đáng loại bỏ. Nếu hai hành động có cùng kết quả tối ưu trên toàn phạm vi xác suất hợp lý, thu thêm dữ liệu có thể không đổi quyết định.

**Giá trị kỳ vọng của thông tin hoàn hảo (expected value of perfect information / 완전정보 기대가치)** hỏi: nếu biết chắc trạng thái trước khi hành động, ta kỳ vọng cải thiện kết quả bao nhiêu so với quyết định tốt nhất hiện tại. **Giá trị kỳ vọng của thông tin mẫu (expected value of sample information / 표본정보 기대가치)** hỏi câu tương tự với một phép đo/test thực tế có nhiễu.

Mental model quan trọng là:

```text
information is valuable only when it can change a consequential decision
```

Vì vậy một dashboard, test hoặc nghiên cứu mới không tự có giá trị chỉ vì “thêm dữ liệu”. Nó có giá trị khi giảm bất định đủ để thay đổi hành động hoặc giảm tổn thất kỳ vọng nhiều hơn chi phí thu thập thông tin.

Tuyến này nối trực tiếp sang [Research Methods](../../research_methods/README.md): thiết kế nghiên cứu (research design / 연구 설계), đo lường (measurement / 측정) và lấy mẫu (sampling / 표본추출) quyết định chất lượng của bằng chứng dùng để cập nhật xác suất.

## 10. Rủi ro không chỉ là phương sai

Trong toán tài chính và nhiều bài toán kỹ thuật, phương sai (variance / 분산) là thước đo tiện lợi cho độ phân tán, nhưng **rủi ro (risk / 위험)** rộng hơn độ biến động. Hai phân phối có cùng phương sai có thể có xác suất đuôi, độ lệch, downside hoặc cấu trúc phụ thuộc rất khác nhau.

Một quyết định tốt cần hỏi ít nhất:

- xác suất của các kết quả xấu là bao nhiêu;
- mức độ xấu của chúng là bao nhiêu;
- các rủi ro có đồng thời xảy ra không;
- có giới hạn sống còn, thanh khoản, vốn hoặc an toàn nào khiến một tail event không thể chấp nhận không;
- ước lượng xác suất đuôi có đủ dữ liệu hay đang quá tự tin.

Ở Investing, đây là lý do không được biến `expected return` thành quyết định đầu tư trực tiếp. Cần portfolio context, covariance/dependence, downside, liquidity và giới hạn tổn thất. Chapter [Toán trong Finance, công việc và đời sống](./04_math_for_finance_work_and_daily_life.md) giữ lớp ứng dụng toán học, còn [Investing](../../investing/README.md) là đơn vị sở hữu (canonical owner / 정본 소유자) của quyết định đầu tư và quản trị danh mục.

## 11. Một worked example: cảnh báo sự cố production

Giả sử hệ thống dự báo xác suất một service sẽ gặp sự cố nghiêm trọng trong 30 phút tới. Mục tiêu không phải tạo một ví dụ DevOps đầy đủ mà để thấy toàn bộ tuyến toán học.

Mô hình đưa ra xác suất 0,25. Trên dữ liệu validation gần đây, các dự báo quanh 0,25 dẫn đến sự cố khoảng 0,23–0,27 tùy cohort, nên calibration tạm chấp nhận được. Nếu chỉ nhìn `25%`, ta chưa biết phải làm gì.

Giả sử hành động an toàn là chuyển 20% traffic sang vùng dự phòng, gây chi phí hiệu năng tương đương 2 đơn vị. Nếu không hành động và sự cố xảy ra, tổn thất kỳ vọng tương đương 15 đơn vị. Trong mô hình tối giản:

```text
expected loss(no action) = 0.25 × 15 = 3.75
expected loss(action)    = 2
```

Hành động có tổn thất kỳ vọng thấp hơn. Nhưng nếu chuyển traffic làm tăng rủi ro cho vùng dự phòng hoặc nếu mô hình bị drift sau deploy mới, phép tính trên thiếu biến. Ta phải cập nhật loss model và kiểm tra calibration theo revision.

Sau hành động, service không xảy ra sự cố. Ta **không** thể kết luận dự báo 25% là sai từ một trường hợp. Một biến cố xác suất 25% thường không xảy ra 75% số lần. Hơn nữa, hành động có thể đã ngăn sự cố; outcome quan sát không còn là outcome không can thiệp. Muốn đánh giá causal effect của policy cần thiết kế nghiên cứu/phân tích khác.

Worked example này cho thấy một chuỗi reasoning đầy đủ:

```text
probability estimate
→ calibration evidence
→ consequence model
→ expected loss
→ action
→ intervention changes data-generating process
→ monitoring + research design
```

## 12. Năm lỗi tư duy thường gặp

**Một: biến xác suất thành khẳng định chắc chắn.** `70%` không có nghĩa “sẽ xảy ra”; nó mô tả một ensemble hoặc niềm tin có điều kiện trên thông tin hiện tại.

**Hai: dùng accuracy để thay calibration.** Accuracy phụ thuộc threshold và prevalence; nó không nói xác suất 0,80 có đáng tin như 0,80 hay không.

**Ba: chọn threshold từ metric thay vì hậu quả.** F1/AUC có thể hữu ích cho model comparison nhưng không tự định nghĩa chi phí false positive/false negative trong môi trường thật.

**Bốn: đánh đồng rủi ro với volatility.** Tail loss, correlation khi stress, giới hạn thanh khoản hoặc rủi ro ruin có thể quan trọng hơn variance trung bình.

**Năm: thu thêm dữ liệu mà không hỏi quyết định nào sẽ thay đổi.** Measurement có chi phí; thông tin chỉ đáng giá khi nó cải thiện lựa chọn hoặc giảm bất định có hậu quả.

## 13. Bản đồ owner: học tiếp ở đâu

Chapter này chỉ giữ lớp kết nối. Mỗi phần sâu có đơn vị sở hữu (canonical owner / 정본 소유자) riêng:

- nền xác suất (probability / 확률), Bayes, kỳ vọng (expectation / 기댓값), phân phối (distribution / 분포) và thống kê (statistics / 통계): [`mathematics/06_probability_statistics`](../06_probability_statistics/);
- đo lường (measurement / 측정), sampling, study design và evidence synthesis: [Research Methods](../../research_methods/README.md);
- econometrics và causal identification: [Economics](../../economics/README.md);
- đánh giá mô hình AI/ML và production evaluation: [Computer Science — Artificial Intelligence](../../computer_science/02_artificial_intelligence/README.md);
- nhận thức, bias và hành vi quyết định của con người: [Psychology](../../psychology/README.md);
- risk/portfolio/application trong tài chính: [Investing](../../investing/README.md).

Tuyến đọc ngắn nhất sau chapter này là:

```text
Bayes / probability
→ calibration + scoring
→ expected loss / utility
→ threshold / policy
→ research design + monitoring
→ domain-specific decision
```

## Kết luận: bất định chỉ trở nên hữu ích khi đi hết tới hành động và quay về bằng chứng

Bất biến (invariant / 불변식) quan trọng nhất là: **xác suất, chất lượng dự báo và chất lượng quyết định là ba lớp khác nhau**. Hiệu chuẩn (calibration / 보정) nối xác suất với thực tế quan sát; hàm mất mát (loss function / 손실 함수) và tiện ích (utility / 효용) nối thực tế bất định với hành động; vòng phản hồi (feedback loop / 피드백 루프) nối hành động trở lại dữ liệu và buộc ta kiểm tra lại calibration.

Ranh giới của chapter là không thay thế giáo trình decision theory, econometrics, AI evaluation hay portfolio management. Nó cung cấp đường đi xuyên repository để khi gặp một con số xác suất, người đọc biết hỏi tiếp: **nó được hiệu chuẩn thế nào, hậu quả của các lựa chọn là gì, dữ liệu mới có thể đổi quyết định không, và policy hiện tại có đang làm thay đổi dữ liệu dùng để đánh giá chính nó không?**