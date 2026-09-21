# Thiên lệch Dataset

**Thiên lệch dữ liệu (dataset bias / 데이터 편향)** là sự lệch có hệ thống giữa dữ liệu được quan sát và phenomenon hoặc population mà mô hình thực sự cần phục vụ. Bias không chỉ là “class imbalance”; nó có thể đến từ sampling, measurement, label, quyết định lịch sử và feedback loop sau deployment.

## Selection Bias

Các example được đưa vào dataset không được chọn ngẫu nhiên so với target population.

Ví dụ một hospital dataset chỉ chứa những người đã tới khám. Nếu dùng dataset đó để ước lượng disease prevalence cho toàn population, model có thể overestimate vì nhóm đi viện khác population chung.

## Sampling Bias

Một số subgroup bị đại diện quá ít, ví dụ:

```text
camera device
ngôn ngữ
khu vực
nhóm tuổi
class hiếm
```

Mô hình vẫn có thể đạt aggregate performance cao nhưng reliability rất kém trên các subgroup nhỏ.

## Measurement Bias

Chất lượng đo feature hoặc label khác nhau giữa các group.

Ví dụ image quality thấp hơn trên một số thiết bị, hoặc sensitivity của diagnostic test khác nhau giữa population. Khi đó một phần “bias của model” thực ra bắt nguồn từ measurement system.

## Historical Bias

Dữ liệu phản ánh quyết định của con người và hệ thống trong quá khứ.

Ví dụ hiring record ghi lại ai từng được tuyển theo policy cũ, không phải một thước đo khách quan về “true talent”. Nếu học trực tiếp từ historical outcome, mô hình có thể tái tạo bất công cũ.

## Label Bias

Human label có thể khác nhau có hệ thống giữa các subgroup. Ví dụ đánh giá toxicity hoặc moderation có thể chịu ảnh hưởng dialect và bối cảnh văn hóa.

Nên audit agreement và error rate theo subgroup, không chỉ global average.

## Representation Bias

Group phổ biến chiếm phần lớn dữ liệu nên representation được học tốt hơn. Ngôn ngữ, accent hoặc domain hiếm có thể nhận embedding hoặc ASR quality kém dù label ban đầu không sai.

## Aggregation Bias

Một global model giả định cùng một mapping áp dụng cho population không đồng nhất.

Nếu mechanism thực sự khác giữa các subgroup, pooled model có thể làm một số nhóm bị thiệt. Separate model hoặc group-aware feature đôi khi hữu ích, nhưng phải xem xét thêm fairness, privacy và legal constraint.

## Evaluation Bias

Benchmark bản thân có thể không đại diện cho deployment population.

Nếu team tối ưu quá mạnh theo một benchmark hẹp, model sẽ giỏi trên phần được đo nhưng chưa chắc giỏi trong thế giới thật mà hệ thống cần phục vụ.

## Survivorship Bias

Dataset chỉ giữ lại entity còn tồn tại hoặc thành công, trong khi churned hoặc failed case biến mất khỏi dữ liệu sau đó.

Điều này dễ tạo kết luận quá lạc quan về behavior hoặc outcome.

## Feedback Loop

Model decision ảnh hưởng dữ liệu tương lai:

```text
xếp item phổ biến lên cao
→ item nhận thêm click
→ dữ liệu mới cho thấy item càng phổ biến
→ model tiếp tục ưu tiên item đó
```

Vòng lặp này có thể khuếch đại popularity bias và giảm exposure diversity.

## Proxy Variable

Ngay cả khi loại protected attribute trực tiếp, các feature khác như postcode, school hoặc language có thể là proxy mạnh.

Vì vậy **fairness through unawareness** — chỉ bỏ field nhạy cảm — thường không đủ.

## Simpson’s Paradox

Quan hệ nhìn ở aggregate có thể đảo chiều khi phân tích theo subgroup.

Trước khi đưa ra kết luận causal hoặc fairness, cần kiểm tra các conditional slice có ý nghĩa thay vì chỉ nhìn average toàn dataset.

## Trade-off giữa các Fairness Metric

Nhiều định nghĩa fairness có thể xung đột khi base rate khác nhau, ví dụ:

- demographic parity;
- equal opportunity hoặc TPR parity;
- equalized odds;
- calibration.

Không có metric nào đúng cho mọi bài toán. Lựa chọn phụ thuộc bối cảnh xã hội, pháp lý và loại decision đang được tự động hóa.

## Dataset Bias và Bias–Variance

“Bias” trong dataset bias là khái niệm về sampling, measurement và social process, khác với **bias–variance trade-off** trong Machine Learning.

Cùng một từ nhưng mô tả hai hiện tượng khác nhau.

## Reweighting

Nếu biết target distribution, có thể dùng importance weight:

\[
w(x)=\frac{P_{target}(x)}{P_{train}(x)}
\]

để điều chỉnh training hoặc evaluation trong một số assumption về covariate shift.

Tuy nhiên weight quá lớn làm variance tăng và không thể sửa vùng hoàn toàn không có support, tức `P_train(x)=0`.

## Resampling

Oversampling group hoặc class hiếm làm tăng exposure trong training. Undersampling majority giảm imbalance nhưng làm mất dữ liệu.

Synthetic oversampling có thể giúp trong một số trường hợp nhưng cũng có thể khuếch đại artifact nếu generator không phản ánh đúng subgroup thật.

## Thu thập Dữ liệu có Mục tiêu

Nhiều khi cách sửa tốt nhất là thu thêm dữ liệu thực từ slice yếu thay vì xây weighting scheme ngày càng phức tạp.

Error analysis nên trực tiếp dẫn hướng ưu tiên data collection.

## Slice-Based Evaluation

Nên đo metric riêng theo những slice có ý nghĩa operational, ví dụ:

```text
ngôn ngữ
khu vực
skin tone khi phù hợp về đạo đức/pháp lý
device
điều kiện ánh sáng
band giá trị giao dịch
user mới so với user cũ
```

Không cần tạo vô hạn combination; slice nên gắn với risk thực tế.

## Intersectionality

Bias đôi khi chỉ xuất hiện ở giao của nhiều thuộc tính, ví dụ language + age + device.

Phân tích intersection khó hơn vì sample nhanh chóng trở nên nhỏ, nên cần confidence interval và minimum-sample rule.

## Trực giác về Counterfactual Fairness

Một câu hỏi hữu ích là: decision có thay đổi nếu protected characteristic thay đổi trong khi các yếu tố nền liên quan được giữ nhất quán hay không?

Formal counterfactual fairness cần causal model và assumption mạnh, nên không thể chỉ kiểm bằng correlation đơn giản.

## Bias trong Foundation Model

Web-scale text và image data phản ánh stereotype xã hội và mất cân bằng mạnh về language, geography và topic.

Filtering có thể giảm harmful content nhưng cũng có thể vô tình loại dialect hoặc topic thiểu số nếu classifier dùng cho filtering bản thân đã bias.

## Synthetic Data và Bias

Nếu generator ban đầu đã bias, synthetic data có thể lặp lại hoặc khuếch đại cùng bias.

Việc “cân bằng số lượng” bằng synthetic sample chỉ hữu ích khi generator thực sự mô hình hóa đúng target subgroup.

## Label Policy cũng là một Value Choice

Các label như moderation, helpfulness hoặc safety không chỉ là technical category; chúng encode lựa chọn chuẩn tắc.

Dataset documentation nên làm rõ policy nào đã được dùng để tạo label.

## Tài liệu hóa Dataset

Một datasheet hoặc model-card-style documentation có thể mô tả:

- mục tiêu;
- composition;
- collection process;
- preprocessing;
- use case và limitation;
- coverage theo geography/demographic;
- license;
- known bias.

Documentation không loại bỏ bias nhưng giúp assumption trở nên có thể kiểm tra.

## Các Layer giảm Bias

Mitigation có thể xảy ra ở nhiều tầng:

```text
pre-processing  → thu thập thêm / reweight dữ liệu
in-processing   → constraint hoặc loss riêng
post-processing → threshold / calibration / policy
```

Sửa vấn đề từ data-generating process thường bền vững hơn chỉ patch threshold ở cuối pipeline.

## Mô hình tư duy

> **Dataset bias đặt câu hỏi: dữ liệu này đang đại diện cho thực tế của ai, bỏ sót ai, và cơ chế selection hoặc measurement nào đã tạo ra sự lệch đó?**

## Những nhầm lẫn thường gặp

### “Class count cân bằng nghĩa là dataset không bias”

Không. Bias vẫn có thể nằm ở subgroup coverage, measurement hoặc label.

### “Bỏ protected attribute là model sẽ fair”

Không. Proxy feature và historical outcome vẫn có thể encode cùng thông tin.

### “Fairness có một metric toán học đúng duy nhất”

Không. Các metric encode những tiêu chí chuẩn tắc khác nhau và đôi khi không thể đồng thời thỏa mãn.

## Liên kết kiến thức

Dataset bias nối Sampling Theory, Causal Inference, Fairness, Social Systems và feedback sau deployment.

Xem tiếp: [Dữ liệu Tổng hợp](./07_synthetic_data.md).