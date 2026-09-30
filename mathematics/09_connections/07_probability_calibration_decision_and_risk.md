# Xác suất → hiệu chuẩn → quyết định và rủi ro

> **Mạch đọc:** Chapter này là tuyến liên kết giữa xác suất, thống kê và quyết định dưới bất định; nó không tạo thêm một domain “decision science”. Nếu chưa chắc về xác suất có điều kiện (conditional probability / 조건부 확률), kỳ vọng (expectation / 기댓값) hoặc phân phối xác suất (probability distribution / 확률분포), đọc trước [xác suất có điều kiện và Bayes](../06_probability_statistics/02_conditional_probability_and_bayes.md), [kỳ vọng và phương sai](../06_probability_statistics/04_expectation_variance_and_limit_laws.md) và [thống kê suy luận](../06_probability_statistics/05_descriptive_and_inferential_statistics.md).

Câu hỏi trung tâm là: **một xác suất tốt trở thành một quyết định tốt bằng cách nào?** Xác suất mô tả bất định; hiệu chuẩn (calibration / 보정) kiểm tra mức xác suất có phù hợp với tần suất thực tế hay không; hàm mất mát (loss function / 손실함수), tiện ích (utility / 효용) và ràng buộc (constraint / 제약조건) mới chuyển niềm tin thành hành động.

```text
thế giới bất định
→ bằng chứng
→ ước lượng xác suất
→ kiểm hiệu chuẩn + khả năng phân biệt
→ hậu quả / chi phí / tiện ích
→ ngưỡng hoặc chính sách quyết định
→ kết quả thực tế
→ phản hồi và hiệu chuẩn lại
```

## 1. Xác suất chưa phải hành động

Một dự báo 70% chỉ nói mức bất định về một biến cố. Hai người có cùng xác suất vẫn có thể chọn khác nhau nếu hậu quả, ngân sách, khả năng chịu rủi ro hoặc ràng buộc khác nhau.

Đây là ranh giới giữa **suy luận (inference / 추론)** và **quyết định (decision / 의사결정)**:

```text
suy luận: điều gì có khả năng đúng?
quyết định: với xác suất đó và hậu quả tương ứng, nên làm gì?
```

Ví dụ một giao dịch có 10% khả năng gian lận. Nếu chặn nhầm giao dịch hợp lệ chỉ gây ít chi phí, ngưỡng chặn có thể thấp. Nếu chặn nhầm làm mất khách hàng hoặc tạo trách nhiệm pháp lý lớn, cùng xác suất 10% có thể chưa đủ để hành động.

> **Chuyển mạch:** Trước khi dùng xác suất để chọn hành động, phải biết con số xác suất đó có đáng tin không.

## 2. Hiệu chuẩn trả lời “70% có thật sự giống 70% không?”

Một mô hình được **hiệu chuẩn tốt (well-calibrated / 잘 보정된)** nếu trong nhóm các trường hợp được gán xác suất gần `p`, biến cố xảy ra với tần suất gần `p` trong dài hạn, với điều kiện population và cơ chế sinh dữ liệu tương đối ổn định.

Nếu 1.000 trường hợp đều được gán khoảng 70% và khoảng 700 trường hợp thật sự xảy ra, đó là dấu hiệu hiệu chuẩn tốt hơn việc chỉ 400 trường hợp xảy ra.

Nhưng cần xem thêm kích thước mẫu, khoảng bất định và sự dịch chuyển phân phối (distribution shift / 분포 이동). Một nhóm nhỏ không đủ để kết luận mạnh.

## 3. Hiệu chuẩn và khả năng phân biệt là hai trục khác nhau

**Hiệu chuẩn (calibration / 보정)** hỏi xác suất có đúng mức hay không. **Khả năng phân biệt (discrimination / 판별력)** hỏi mô hình có xếp trường hợp nguy cơ cao lên trên trường hợp nguy cơ thấp hay không.

Một mô hình luôn dự báo 20% trong population có tỷ lệ nền 20% có thể được hiệu chuẩn tốt nhưng gần như không giúp ưu tiên ai. Ngược lại, một mô hình xếp hạng tốt nhưng luôn quá tự tin có thể hữu ích cho ranking nhưng nguy hiểm nếu output được dùng để tính expected loss.

Khi đánh giá hệ thống dự báo, nên tách ba câu hỏi:

```text
xác suất có hiệu chuẩn không?
mô hình có phân biệt tốt không?
quyết định sinh ra từ model có tạo giá trị hơn baseline không?
```

## 4. Quy tắc chấm điểm đúng đắn đánh giá xác suất, không đánh giá toàn bộ quyết định

**Quy tắc chấm điểm đúng đắn (proper scoring rule / 적정점수규칙)** khuyến khích người dự báo báo xác suất trung thực.

Với biến cố nhị phân `y ∈ {0,1}` và dự báo `p`, **điểm Brier (Brier score / 브라이어 점수)** là:

```text
Brier = (p - y)^2
```

Điểm càng nhỏ càng tốt.

**Mất mát logarit (log loss / 로그손실)** là:

```text
-[y log(p) + (1-y) log(1-p)]
```

Nó phạt mạnh dự báo cực kỳ tự tin nhưng sai.

Hai thước đo này đánh giá chất lượng dự báo xác suất. Chúng chưa biết chi phí kinh doanh, hậu quả pháp lý hay ưu tiên của người ra quyết định, nên không thể thay trực tiếp cho chính sách quyết định (decision policy / 의사결정 정책).

## 5. Từ xác suất sang hành động: tổn thất kỳ vọng

Giả sử hành động là `a`, trạng thái thế giới là `s`, và `L(a,s)` là tổn thất.

**Tổn thất kỳ vọng (expected loss / 기대손실)** là:

```text
E[L | a] = Σ P(s | evidence) · L(a,s)
```

Một nguyên tắc đơn giản là chọn hành động có tổn thất kỳ vọng thấp nhất trong tập hành động hợp lệ. Viết theo tiện ích thì ta tối đa **tiện ích kỳ vọng (expected utility / 기대효용)**.

Điểm cần giữ là:

```text
xác suất
≠
giá trị / chi phí
```

Xác suất trả lời “khả năng nào xảy ra?”. Hàm mất mát trả lời “nếu xảy ra thì hậu quả lớn tới đâu?”.

## 6. Ngưỡng quyết định sinh từ hậu quả

Giả sử hành động phòng ngừa có chi phí `C_action`; nếu không hành động và sự cố xảy ra, tổn thất là `C_failure`.

Một quy tắc tối giản:

```text
p · C_failure > C_action
```

hay:

```text
p > C_action / C_failure
```

Tỷ lệ bên phải là **ngưỡng quyết định (decision threshold / 의사결정 임계값)**.

Ngưỡng không phải thuộc tính cố định của mô hình. Khi chi phí thay đổi, ngưỡng hợp lý cũng thay đổi dù mô hình không đổi.

## 7. Dương tính giả và âm tính giả chỉ có nghĩa khi gắn với chi phí

**Dương tính giả (false positive / 거짓양성)** và **âm tính giả (false negative / 거짓음성)** không tự có mức nghiêm trọng cố định.

Trong phát hiện gian lận, âm tính giả có thể gây mất tiền; dương tính giả làm khách hàng hợp lệ bị chặn. Trong cảnh báo vận hành, dương tính giả có thể gây mệt mỏi cảnh báo; âm tính giả có thể làm sự cố trôi qua không phát hiện.

Do đó không nên tối ưu độ chính xác (accuracy / 정확도) chung nếu chi phí nghiệp vụ bất đối xứng.

## 8. Tỷ lệ nền làm thay đổi ý nghĩa của tín hiệu

Một tín hiệu có vẻ mạnh vẫn có thể tạo nhiều dương tính giả nếu biến cố nền rất hiếm.

Đây là lý do cần giữ chuỗi Bayes:

```text
xác suất trước bằng chứng
→ chất lượng bằng chứng mới
→ xác suất sau bằng chứng
```

Nếu bỏ qua **tỷ lệ nền (base rate / 기저율)**, người đọc dễ đánh giá quá cao một xét nghiệm, cảnh báo hoặc tín hiệu thị trường hiếm gặp.

## 9. Giá trị thông tin: có đáng thu thêm bằng chứng không?

**Giá trị thông tin (value of information / 정보가치)** hỏi liệu dữ liệu mới có khả năng thay đổi quyết định đủ lớn để đáng chi phí thu thập hay không.

Nếu hai hành động gần như tương đương và một phép đo rẻ có thể tách chúng rõ, giá trị thông tin cao. Nếu quyết định sẽ không đổi bất kể kết quả, thu thêm dữ liệu chỉ tạo chậm trễ hoặc chi phí.

Mô hình:

```text
không chắc chắn hiện tại
→ dữ liệu mới có thể thay xác suất sau bằng chứng bao nhiêu?
→ xác suất mới có thể đổi hành động không?
→ lợi ích của việc đổi hành động có vượt chi phí thu dữ liệu không?
```

## 10. Rủi ro không đồng nghĩa với phương sai

Trong một số bài toán tài chính, phương sai hữu ích. Nhưng **rủi ro (risk / 위험)** rộng hơn biến động.

Rủi ro còn có thể là:

- xác suất mất mát cực lớn;
- không thể phục hồi trong thời hạn cần thiết;
- mất thanh khoản;
- vi phạm constraint;
- failure có tính hệ thống;
- nhiều rủi ro cùng tương quan trong stress case.

Một quyết định có phương sai thấp vẫn có thể nguy hiểm nếu có tổn thất đuôi (tail loss / 꼬리손실) lớn nhưng hiếm.

## 11. Phân phối thay đổi làm hiệu chuẩn cũ mất giá trị

**Dịch chuyển phân phối (distribution shift / 분포이동)** xảy ra khi population, environment hoặc cơ chế sinh dữ liệu đổi.

Ví dụ mô hình được hiệu chuẩn tốt trên khách hàng cũ nhưng product policy thay đổi làm population khác đi. Calibration cũ không tự động còn đúng.

Cần theo dõi:

```text
phân phối đầu vào
tỷ lệ nền
định nghĩa nhãn
policy downstream
measurement process
```

Khi một trong các lớp này đổi, phải xem lại hiệu chuẩn.

## 12. Chất lượng quyết định khác với kết quả

Một quyết định tốt vẫn có thể cho outcome xấu vì randomness. Một quyết định kém vẫn có thể may mắn.

Do đó review nên hỏi:

```text
xác suất ban đầu có hợp lý không?
model có calibrated không?
loss/utility có phản ánh mục tiêu không?
constraint có được tôn trọng không?
threshold có sinh từ hậu quả thật không?
```

Đây là cách tránh **thiên lệch kết quả (outcome bias / 결과편향)**.

## 13. Ví dụ tích hợp: cảnh báo production

Giả sử một tín hiệu báo 30% khả năng service sẽ vi phạm SLO trong 10 phút tới.

Hai hành động:

```text
A — không scale thêm
B — scale thêm 20% capacity
```

Nếu scale tốn ít nhưng SLO violation rất đắt, ngưỡng hành động có thể thấp hơn 30%. Nếu scale có rủi ro gây cascade hoặc chi phí lớn, cùng xác suất 30% có thể chưa đủ.

Sau đó cần kiểm model có calibrated trong traffic regime hiện tại không. Nếu model được train trước khi architecture đổi, xác suất 30% có thể không còn mang nghĩa cũ.

Case này cho thấy toàn chuỗi:

```text
tín hiệu
→ xác suất
→ hiệu chuẩn
→ chi phí
→ ngưỡng
→ hành động
→ kết quả
→ phản hồi
```

## 14. Các lỗi tư duy thường gặp

**Xác suất = chắc chắn:** 90% không có nghĩa biến cố chắc chắn xảy ra.

**Độ chính xác = hiệu chuẩn:** mô hình đoán nhãn đúng nhiều chưa chắc xác suất đúng mức.

**Metric cao = policy tốt:** mô hình có điểm tốt nhưng threshold sai vẫn tạo quyết định tệ.

**Ngưỡng thuộc về mô hình:** ngưỡng thực ra phụ thuộc hậu quả và constraint.

**Rủi ro = biến động:** bỏ qua tail loss, liquidity và irreversible damage.

**Không cập nhật tỷ lệ nền:** giữ prior cũ sau khi environment đã đổi.

## 15. Mô hình tổng hợp

```text
bằng chứng
→ xác suất
→ kiểm hiệu chuẩn + phân biệt
→ hậu quả / mất mát / tiện ích
→ ràng buộc
→ chính sách hoặc ngưỡng
→ hành động
→ kết quả
→ cập nhật mô hình và hiệu chuẩn
```

Insight quan trọng là: **một dự báo tốt là đầu vào cho quyết định, không phải bản thân quyết định**.

## 16. Kết nối và bàn giao

Để hiểu bằng chứng và suy luận nhân quả sâu hơn, đọc [Research Methods](../../research_methods/README.md). Để xem xác suất được dùng trong healthcare, đọc [Hiểu thông tin y tế](../../biology/90_connections/02_health_literacy_screening_diagnosis_evidence_and_shared_decisions.md). Để xem xác suất và hiệu chuẩn đi vào portfolio decision, đọc [Kinh tế vĩ mô + hành vi + bằng chứng → quyết định danh mục](../../investing/07_integrated_case_studies/08_MACRO_BEHAVIOR_EVIDENCE_TO_PORTFOLIO_DECISION.md). Để xem model probability được vận hành trong production AI, đọc [AI data → evaluation → provenance → production evidence](../../computer_science/90_connections/07_ai_data_evaluation_provenance_and_production_evidence.md).

> **Bàn giao:** Khi gặp một con số xác suất, đừng hỏi ngay “nên làm gì?”. Hãy đi qua **xác suất có đáng tin không → hậu quả là gì → ràng buộc nào tồn tại → ngưỡng/chính sách nào phù hợp → kết quả nào sẽ dùng để hiệu chuẩn lại**.