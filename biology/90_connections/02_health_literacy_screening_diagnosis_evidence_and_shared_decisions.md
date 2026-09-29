# Hiểu thông tin y tế: triệu chứng → xác suất trước xét nghiệm → kiểm tra → bằng chứng → quyết định chung

> **Mạch đọc:** Chapter này là tuyến **hiểu biết y tế (health literacy / 건강 문해력)** nối Biology, Mathematics, Research Methods và Psychology. Nó không dạy tự chẩn đoán và không thay thế bác sĩ, dược sĩ hoặc hướng dẫn y tế tại nơi người đọc đang sống. Câu hỏi trung tâm là: **khi nhận một triệu chứng, kết quả xét nghiệm, lời khuyên điều trị hoặc một headline về sức khỏe, làm thế nào hiểu đúng bằng chứng và hỏi đúng câu hỏi trước khi ra quyết định?**

Biology sở hữu mechanism của cơ thể; [Research Methods](../../research_methods/README.md) sở hữu cách thiết kế và đánh giá bằng chứng; [Probability → Calibration → Decision and Risk](../../mathematics/09_connections/07_probability_calibration_decision_and_risk.md) sở hữu xác suất và quyết định dưới bất định; Psychology giải thích risk perception, placebo/nocebo và communication. Chapter này nối các owner đó thành một workflow đời sống.

Một mental model ngắn:

```text
observation / symptom
→ context + prior probability
→ measurement / test
→ update probability
→ benefit–harm trade-off
→ values + constraints
→ decision
→ follow-up / re-evaluation
```

Điểm quan trọng nhất là: **một test result không tự nói phải làm gì**. Nó chỉ là một mảnh evidence được diễn giải trong context.

## 1. Health literacy không phải memorization tên bệnh

Một người có thể nhớ hàng trăm disease names nhưng vẫn đọc sai risk, test và treatment claim. Health literacy thực dụng cần khả năng:

```text
phân biệt symptom, sign, screening và diagnosis
đọc probability và uncertainty
kiểm tra nguồn evidence
hiểu benefit và harm theo absolute terms
nhận biết giới hạn của một test
biết câu hỏi nào phải hỏi clinician
biết khi nào thông tin online không đủ để tự xử lý
```

Mục tiêu không phải biến người đọc thành clinician. Mục tiêu là giúp người đọc không biến một con số hoặc headline thành certainty.

## 2. Symptom, sign và diagnosis là ba tầng khác nhau

**Triệu chứng (symptom / 증상)** là experience do người bệnh cảm nhận hoặc mô tả, như đau, chóng mặt hoặc mệt.

**Dấu hiệu (sign / 징후)** là finding có thể quan sát/đo được trong examination hoặc measurement.

**Chẩn đoán (diagnosis / 진단)** là một model giải thích pattern của symptoms, signs, tests và context.

Một symptom có thể có nhiều cause. Một disease có thể biểu hiện bằng nhiều symptom. Vì vậy mapping:

```text
one symptom → one diagnosis
```

thường là reasoning quá mạnh.

## 3. Differential diagnosis là quản lý hypothesis

Trong clinical reasoning, nhiều hypothesis có thể tồn tại cùng lúc. Chúng khác nhau về probability và consequence.

Một clinician không chỉ hỏi “bệnh nào giống nhất?” mà còn cân nhắc:

```text
common things
serious things that must not be missed
patient-specific risk factors
how much new evidence would change management
```

Người đọc không cần tự dựng differential đầy đủ. Nhưng hiểu concept này giúp tránh search một symptom rồi khóa vào disease đầu tiên nhìn thấy.

## 4. Base rate đứng trước test result

Giả sử một test có sensitivity và specificity khá tốt. Nếu condition rất hiếm trong population/context đang xét, positive result vẫn có thể chứa tỷ lệ false positive đáng kể.

Đây là **base-rate problem**. Cùng một test có thể mang ý nghĩa khác nhau ở:

```text
người asymptomatic low-risk
người có symptom điển hình
người có exposure cụ thể
population high-risk
```

Vì vậy câu hỏi đúng trước test là:

> Xác suất condition này hợp lý đến đâu **trước** khi biết kết quả?

Đó là **xác suất trước xét nghiệm (pre-test probability / 검사 전 확률)**.

## 5. Sensitivity và specificity không phải xác suất bạn mắc bệnh

**Độ nhạy (sensitivity / 민감도)** hỏi: trong những người thật sự có condition, test bắt được bao nhiêu?

```text
sensitivity = true positive / all condition-positive cases
```

**Độ đặc hiệu (specificity / 특이도)** hỏi: trong những người thật sự không có condition, test trả negative đúng bao nhiêu?

```text
specificity = true negative / all condition-negative cases
```

Hai metric này mô tả behavior của test dưới reference standard. Chúng không trực tiếp trả lời:

> Tôi vừa positive; xác suất tôi thật sự có condition là bao nhiêu?

Câu đó liên quan tới **positive predictive value (PPV / 양성 예측도)** và prior prevalence/context.

## 6. Predictive value phụ thuộc population

**PPV** và **NPV** thay đổi khi prevalence thay đổi.

Ví dụ giả định có 10,000 người, prevalence 1%, test sensitivity 90%, specificity 95%.

```text
condition present: 100
true positive: 90
false negative: 10

condition absent: 9,900
false positive: 495
true negative: 9,405
```

Trong 585 positive results:

```text
PPV = 90 / 585 ≈ 15.4%
```

Dù sensitivity 90% và specificity 95%, positive result trong low-prevalence population không đồng nghĩa “95% chắc chắn mắc bệnh”.

Ví dụ này không mô tả bất kỳ test cụ thể nào; nó chỉ minh họa vì sao base rate quan trọng.

## 7. Screening khác diagnostic testing

**Sàng lọc (screening / 선별검사)** thường áp dụng cho người chưa có symptom rõ để tìm disease/risk sớm hơn.

**Xét nghiệm chẩn đoán (diagnostic testing / 진단 검사)** thường được dùng khi symptom, sign hoặc risk đã làm condition trở thành hypothesis cần kiểm tra.

Screening cần tiêu chuẩn cao hơn câu “test có phát hiện disease không?”. Một screening program còn phải hỏi:

```text
phát hiện sớm có thay outcome có ý nghĩa không?
false positive tạo harm gì?
overdiagnosis bao nhiêu?
follow-up procedure có risk gì?
chi phí và burden ra sao?
```

## 8. Phát hiện sớm không luôn đồng nghĩa sống lâu hơn

Một chương trình screening có thể làm thời gian từ diagnosis tới death trông dài hơn chỉ vì diagnosis xảy ra sớm hơn, dù death không đổi. Đây là **lead-time bias**.

Ví dụ đơn giản:

```text
without screening: diagnosis year 8 → death year 10 = survival after diagnosis 2 years
with screening: diagnosis year 4 → death year 10 = survival after diagnosis 6 years
```

Survival-after-diagnosis tăng nhưng lifespan không đổi.

Vì vậy outcome quan trọng thường là mortality, morbidity hoặc quality of life phù hợp với disease/context, không chỉ “5-year survival after diagnosis”.

## 9. Length bias và overdiagnosis

Screening theo interval có xu hướng dễ bắt những disease phát triển chậm hơn vì chúng tồn tại lâu hơn trong detectable phase. Đây là **length bias**.

**Chẩn đoán quá mức (overdiagnosis / 과잉진단)** xảy ra khi phát hiện một abnormality thật nhưng nó sẽ không gây symptom hoặc harm đáng kể trong lifetime của người đó.

Overdiagnosis không phải false positive. Condition/pathology có thể “thật”, nhưng việc biết và điều trị nó có thể không tạo net benefit.

## 10. Reference range không phải ranh giới giữa khỏe và bệnh

Laboratory **reference range** thường được xây từ distribution của một reference population và method cụ thể. Một value hơi ngoài range không tự động có nghĩa disease; một value trong range cũng không đảm bảo không có disease.

Cần đọc cùng:

```text
unit
measurement method
reference interval của lab đó
age / sex / physiological context nếu relevant
fasting/time-of-day condition nếu relevant
trend theo thời gian
clinical context
```

Đặc biệt, unit mismatch có thể tạo hiểu lầm lớn. Không so hai con số từ hai lab nếu chưa xác nhận unit và method tương thích.

## 11. Một lần đo có thể chứa biological + measurement variation

Measurement quan sát được có thể viết conceptually:

```text
observed value
= underlying biological state
+ short-term biological variation
+ pre-analytic variation
+ analytic measurement error
```

Pre-analytic variation có thể đến từ timing, sample handling, hydration, meal, exercise hoặc medication context tùy test.

Vì vậy trend đôi khi informative hơn một single measurement, nhưng việc repeat test hay không vẫn phụ thuộc medical context.

## 12. Correlation không tự tạo causal treatment

Một observational study có thể thấy nhóm có biomarker X cao có outcome xấu hơn. Điều đó không tự chứng minh rằng giảm biomarker X bằng bất kỳ cách nào cũng cải thiện outcome.

Có thể tồn tại:

```text
confounding
reverse causation
selection bias
measurement bias
shared cause
```

Đây là lý do causal evidence và randomized trials quan trọng khi câu hỏi là effect của intervention.

Đọc sâu về evidence design ở [Research Questions, Theory and Design](../../research_methods/00_research_questions_theory_and_design.md) và [Systematic Reviews and Evidence Synthesis](../../research_methods/03_systematic_reviews_and_evidence_synthesis.md).

## 13. Randomized trial giải quyết câu hỏi cụ thể, không phải mọi câu hỏi

**Thử nghiệm ngẫu nhiên có đối chứng (randomized controlled trial — RCT / 무작위 대조시험)** giúp cân bằng confounder giữa treatment groups theo expectation khi thiết kế và thực hiện tốt.

Nhưng một RCT vẫn cần đọc:

```text
population là ai?
intervention chính xác là gì?
comparator là gì?
follow-up bao lâu?
primary outcome là gì?
loss to follow-up?
adherence / crossover?
absolute effect size?
harms?
```

Một RCT rất tốt ở population A không tự động externalize sang population B khác tuổi, comorbidity hoặc baseline risk.

## 14. Surrogate endpoint có thể hữu ích nhưng không đồng nghĩa patient outcome

Một **surrogate endpoint** là measurement trung gian được kỳ vọng liên quan tới outcome thực sự quan trọng, ví dụ biomarker.

Surrogate giúp trial nhanh hoặc khả thi hơn, nhưng intervention có thể cải thiện surrogate mà không cải thiện survival, symptom hoặc quality of life tương ứng.

Do đó luôn hỏi:

> Outcome này là thứ bệnh nhân trực tiếp cảm nhận/sống lâu hơn, hay là marker trung gian?

## 15. Relative risk có thể làm effect trông lớn hơn

Giả sử risk giảm từ 2% xuống 1%.

**Relative risk reduction:**

```text
(2% - 1%) / 2% = 50%
```

**Absolute risk reduction:**

```text
2% - 1% = 1 percentage point
```

Hai cách đều đúng nhưng trả lời câu khác nhau.

Một headline “giảm risk 50%” có thể rất khác về practical significance tùy baseline risk.

## 16. Number Needed to Treat phụ thuộc baseline và horizon

Từ absolute risk reduction có thể tính gần đúng:

```text
NNT = 1 / absolute risk reduction
```

Nếu ARR = 0.01 thì NNT ≈ 100 trong time horizon của study.

NNT không phải constant vĩnh viễn của một treatment. Nó phụ thuộc baseline risk, follow-up time, endpoint và population.

Tương tự, harm có thể mô tả bằng absolute increase và **Number Needed to Harm (NNH)** khi phù hợp.

## 17. Benefit và harm phải dùng cùng denominator/time horizon

Không nên so:

```text
benefit relative risk over 10 years
với
harm absolute risk over 3 months
```

mà không làm rõ denominator và horizon.

Một decision aid tốt nên trình bày benefit/harm trên cùng population scale nếu có thể, ví dụ “trên 1,000 người trong 5 năm”.

## 18. Statistical significance không bằng clinical importance

Một effect nhỏ có thể đạt statistical significance với sample rất lớn nhưng ít ý nghĩa clinical. Ngược lại study nhỏ có thể không đạt threshold dù effect estimate có thể quan trọng nhưng uncertainty rộng.

Cần nhìn:

```text
effect size
confidence interval
baseline risk
patient-relevant outcome
study quality
consistency
```

p-value không thay toàn bộ evaluation.

## 19. Confidence interval là vùng uncertainty, không phải tem chất lượng

Một interval rộng báo estimate còn không chắc. Một interval hẹp có thể precise nhưng vẫn biased nếu study design sai.

Precision và validity là hai vấn đề khác nhau.

Một measurement rất precise của wrong construct vẫn cho answer rất chắc nhưng sai câu hỏi.

## 20. Systematic review mạnh khi input studies và synthesis phù hợp

**Tổng quan hệ thống (systematic review / 체계적 문헌고찰)** không tự động là evidence hoàn hảo chỉ vì nằm trên “đỉnh evidence pyramid”. Chất lượng còn phụ thuộc:

```text
search completeness
study eligibility
risk of bias
heterogeneity
publication bias
outcome definition
meta-analysis model
certainty assessment
```

Garbage in, pooled garbage out vẫn có thể xảy ra.

## 21. Guideline là evidence + value judgment + feasibility

Clinical guideline thường không chỉ copy effect size. Recommendation còn cân nhắc:

```text
benefit
harm
evidence certainty
patient values
resource use
feasibility
equity
```

Vì vậy hai guideline có thể khác recommendation dù đọc overlapping evidence, đặc biệt khi trade-off gần nhau hoặc healthcare systems khác nhau.

Khi guideline liên quan quyết định thật, cần dùng phiên bản hiện hành của tổ chức có thẩm quyền tại jurisdiction phù hợp thay vì dựa vào một note tĩnh.

## 22. Shared decision-making bắt đầu khi có nhiều option hợp lý

**Ra quyết định chung (shared decision-making / 공유 의사결정)** không có nghĩa clinician và patient mỗi bên “50% kiến thức”. Clinician mang expertise về evidence, diagnosis và treatment; patient mang values, goals, lived experience và constraints.

Một cấu trúc hữu ích:

```text
what are my options?
what are the likely benefits?
what are the likely harms/burdens?
how certain is the evidence?
what happens if we wait/watch?
which outcome matters most to me?
what follow-up changes the plan?
```

## 23. Watchful waiting cũng là một action có monitoring

“Chưa điều trị ngay” không đồng nghĩa “không làm gì”. Một **watchful waiting / active surveillance** plan tốt phải nói:

```text
what is being monitored?
when re-check?
what threshold changes management?
what symptom/change requires earlier review?
```

Không có follow-up condition thì “đợi” dễ biến thành loss to follow-up.

## 24. Medication literacy: đọc active ingredient trước brand

Một medicine label cần ít nhất:

```text
active ingredient
dose per unit
route
frequency
maximum dose nếu có
duration
indication
contraindication / caution
major interaction
```

Brand name có thể khác giữa countries; nhiều combination products có thể chứa cùng active ingredient.

Do đó một risk đời thường là **duplicate ingredient** khi dùng nhiều OTC/cold/pain products cùng lúc mà chỉ nhìn brand.

Khi không chắc, pharmacist là nguồn phù hợp để kiểm tra active ingredient, duplication và interaction.

## 25. Dose khác concentration và amount

Ví dụ liquid medicine có thể ghi `mg/mL`. Cần phân biệt:

```text
dose = amount of active ingredient intended
concentration = active ingredient per volume
volume administered = mL actually taken
```

Sai unit hoặc nhầm mg với mL là category error, không chỉ arithmetic error.

Không tự chuyển liều từ người lớn sang trẻ em bằng phép chia đơn giản; pediatric dosing phụ thuộc product, indication, weight/age và guidance cụ thể.

## 26. “Natural” không đồng nghĩa risk-free

Supplement, herb hoặc traditional product vẫn có thể có pharmacological effect, contamination, dose variability hoặc interaction.

Risk evaluation nên hỏi cùng câu hỏi như thuốc khác:

```text
active component là gì?
evidence cho indication?
dose?
interaction?
quality control?
who should avoid it?
```

Label “natural” là source category, không phải safety proof.

## 27. Adherence failure có thể trông như treatment failure

Nếu medication không được dùng theo regimen thực tế, outcome không phản ánh đầy đủ efficacy của regimen đó.

Lý do non-adherence có thể là:

```text
side effect
cost
complex schedule
forgetfulness
belief/fear
symptom improved
instructions unclear
```

Vì vậy câu hỏi “thuốc không hiệu quả?” đôi khi phải tách khỏi “regimen có được thực hiện không và vì sao?”.

## 28. Placebo và nocebo không có nghĩa symptom là tưởng tượng

Expectation, learning và context có thể thay perception của symptom và một số physiological response. [Placebo, nocebo, expectation and context](../../psychology/06_applied/13_placebo_nocebo_expectation_and_context.md) giải thích mechanism sâu hơn.

Điểm practical là cách risk được communicated có thể thay experience và adherence. Nhưng placebo/nocebo không được dùng để phủ nhận disease mechanism hoặc thay evidence-based treatment khi treatment cần thiết.

## 29. Online symptom checker là triage aid, không phải oracle

Search engine hoặc AI có thể giúp tạo câu hỏi, giải thích terminology và chuẩn bị cho appointment. Nhưng chúng thiếu hoặc không verify đầy đủ:

```text
physical examination
complete history
vital signs
full medication list
reliable test context
local epidemiology
longitudinal record
```

Do đó confidence của generated text không nên được nhầm với clinical certainty.

## 30. Triage không nên học bằng một danh sách red flags bất biến

Urgency phụ thuộc symptom, severity, onset, age, pregnancy, comorbidity, medication và context. Một static note không thể bao phủ mọi emergency.

Mental model an toàn hơn là:

```text
rapid/severe deterioration
possible threat to breathing/circulation/neurologic function
major injury/poisoning
high-risk context
→ use local urgent/emergency pathway rather than continue self-research
```

Khi nghi ngờ tình huống khẩn cấp, dùng dịch vụ y tế khẩn cấp tại nơi đang sống. Chapter này không cung cấp protocol triage cá nhân.

## 31. Hãy chuẩn bị appointment như một data handoff

Một clinician có thể reason tốt hơn khi input rõ. Một note ngắn hữu ích thường gồm:

```text
main concern
onset + timeline
what makes it better/worse
severity/function impact
relevant measurements
medications/supplements
allergies
important past history
what you are worried about
questions you want answered
```

Không cần viết essay; timeline và medication list chính xác thường có giá trị hơn nhiều screenshot rời.

## 32. Hỏi “điều gì sẽ thay đổi quyết định?”

Một test có giá trị khi result có thể thay management.

Nếu cả positive lẫn negative result đều không thay action, cần hỏi test đang phục vụ mục đích gì: reassurance, documentation, prognosis, eligibility hay curiosity?

Đây là **giá trị thông tin (value of information / 정보 가치)** trong decision science.

## 33. Repeat testing có thể tạo false alarms

Nếu test nhiều independent measurements với reference range 95%, ngay cả người khỏe hoàn toàn cũng có xác suất ít nhất một value ngoài range tăng khi số test tăng.

Conceptually:

```text
P(at least one outside range)
= 1 - P(all inside range)
```

Điều này không có nghĩa ignore abnormal results. Nó giải thích vì sao large panels tạo incidental findings và cần interpretation thay vì panic theo từng flag.

## 34. Family history là risk information, không phải destiny

Family history có thể phản ánh genetics, shared environment hoặc cả hai. Nó thay prior probability cho một số condition nhưng không xác định chắc outcome cá nhân.

Genetic result cũng cần context về penetrance, variant classification và population evidence. Một “gene for X” headline thường oversimplify nhiều tầng uncertainty.

## 35. Health information thay đổi theo thời gian

Guideline, drug safety information và screening recommendation có thể thay khi evidence mới xuất hiện. Vì vậy repository nên lưu **mental models evergreen**, còn con số tuổi, interval, dose, contraindication hoặc jurisdiction-specific rule cần kiểm tra nguồn hiện hành trước quyết định.

Đây là boundary quan trọng giữa knowledge library và clinical reference.

## 36. Financial dimension của healthcare

Healthcare decision có thể tạo:

```text
out-of-pocket cost
lost work time
insurance claim complexity
future premium / coverage implications tùy system
travel/caregiver cost
```

Nhưng cost không nên được tách khỏi expected benefit/harm. Personal finance route tại [Tài chính cá nhân trước khi đầu tư](../../investing/01_foundations/07_PERSONAL_FINANCE_CASHFLOW_DEBT_INSURANCE_AND_INVESTING.md) giúp xem medical shock như một balance-sheet/liquidity risk mà không biến health decision thành pure financial optimization.

## 37. Communication failure là một clinical risk

Một plan tốt có thể fail nếu patient hiểu khác clinician. Trước khi rời appointment, cần rõ:

```text
working diagnosis / uncertainty là gì?
plan hiện tại là gì?
medicine/test dùng để làm gì?
expected timeline?
what changes the plan?
when/how follow up?
```

**Teach-back** là kỹ thuật người nhận nhắc lại plan bằng lời của mình để kiểm tra shared understanding, không phải test trí nhớ.

Psychology về communication/conflict nằm tại [Interpersonal Communication and Conflict](../../psychology/06_applied/03_interpersonal_communication_and_conflict.md).

## 38. Worked example: đọc một headline treatment claim

Giả sử headline nói:

> “Treatment A giảm risk của outcome X 40%.”

Không vội kết luận. Đi theo route:

```text
1. population nào?
2. baseline risk bao nhiêu?
3. 40% là relative hay absolute?
4. follow-up bao lâu?
5. outcome patient-important hay surrogate?
6. comparator là placebo, usual care hay treatment khác?
7. harm/side effect bao nhiêu?
8. confidence interval?
9. study design?
10. result đã được replicate/synthesized chưa?
```

Nếu baseline risk giảm từ 5% xuống 3%, relative reduction là 40% nhưng absolute reduction là 2 percentage points. Hai con số mô tả cùng effect nhưng practical interpretation khác.

## 39. Worked example: đọc một positive screening result

Một positive result không nên được dịch thẳng thành diagnosis. Route reasoning là:

```text
screening population risk
→ test characteristics
→ result
→ post-test probability
→ confirmatory pathway nếu guideline yêu cầu
→ benefit/harm of next action
```

Câu hỏi cần hỏi clinician có thể là:

```text
Kết quả này thay xác suất condition lên khoảng mức nào?
Có cần confirmatory test không?
False positive/common benign explanation là gì?
Nếu chờ và repeat thì trade-off gì?
```

## 40. Failure mode: dùng reference range như binary diagnosis

Flag `H` hoặc `L` là signal để interpret, không phải diagnosis label.

## 41. Failure mode: dùng anecdote thay denominator

Một người quen có side effect nặng là information thật nhưng không cho biết incidence. Ngược lại một người dùng tốt không chứng minh treatment an toàn cho mọi population.

Anecdote mạnh về salience, yếu về denominator.

## 42. Failure mode: “study says” nhưng không xác định study type

Cell study, animal study, observational association, small trial, large randomized trial và systematic review trả lời các tầng câu hỏi khác nhau. Không được collapse tất cả thành “scientists proved”.

## 43. Failure mode: search cho tới khi gặp answer mong muốn

Khi anxiety cao, repeated searching dễ biến thành confirmation loop. Một process tốt đặt stopping rule:

```text
source hierarchy đã đủ chưa?
question cần clinician/data mới không?
search thêm có thay decision không?
```

Nếu không, information acquisition có diminishing return và có thể tăng distress.

## 44. Mô hình tư duy tổng hợp

```text
symptom / observation
      ↓
context + baseline risk
      ↓
measurement quality
      ↓
Bayesian update
      ↓
evidence quality + effect size
      ↓
absolute benefit / harm
      ↓
patient values + constraints
      ↓
decision + follow-up trigger
```

Health literacy tốt không tạo certainty giả. Nó giúp biết **uncertainty đang nằm ở đâu** và evidence nào có thể giảm uncertainty đủ để thay action.

## 45. Kết nối

Để hiểu physiology và disease mechanism, quay về các chapter Biology liên quan. Để hiểu sensitivity, Bayes và decision threshold, đọc [Probability → Calibration → Decision and Risk](../../mathematics/09_connections/07_probability_calibration_decision_and_risk.md). Để đánh giá causal claim và synthesis, đọc [Research Methods](../../research_methods/README.md). Để hiểu risk perception và nocebo, đọc [Risk, Uncertainty and Science Communication](../../psychology/90_connections/03_risk_uncertainty_and_science_communication.md) cùng [Placebo/Nocebo](../../psychology/06_applied/13_placebo_nocebo_expectation_and_context.md).

Từ đây, practical-life route nối healthcare với finance, communication và career tại [Practical-life decision route](../../psychology/90_connections/07_practical_life_decisions_finance_health_communication_and_career.md).

> **Bàn giao:** Sau chapter này, người đọc nên có thể nhìn một test, screening claim hoặc treatment headline và tách được prior probability, measurement quality, effect size, uncertainty, benefit/harm và follow-up. Khi quyết định phụ thuộc medical details cá nhân, bước tiếp theo là trao đổi với professional phù hợp chứ không kéo dài suy luận từ tài liệu tĩnh.