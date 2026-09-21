# Drift, Thay đổi Phân phối và Huấn luyện lại

Một mô hình được huấn luyện trên phân phối lịch sử nhưng thế giới production luôn thay đổi. **Độ trôi (drift / 드리프트)** mô tả sự thay đổi của quá trình tạo dữ liệu hoặc mối quan hệ giữa đầu vào và mục tiêu theo thời gian. Drift quan trọng vì chất lượng mô hình phụ thuộc vào các giả định về phân phối.

## Data Drift

Nếu:

\[
P_{train}(X)\neq P_{prod}(X)
\]

thì phân phối đầu vào đã thay đổi.

Ví dụ: tỷ lệ thiết bị, ngôn ngữ hoặc phân phối số tiền giao dịch của khách hàng thay đổi.

Data drift không tự động nghĩa dự đoán đã sai. Mô hình có thể vẫn khái quát hóa tốt.

## Label Shift hoặc Prior Shift

Tỷ lệ nền của lớp thay đổi:

\[
P_{train}(Y)\neq P_{prod}(Y)
\]

Ví dụ tỷ lệ gian lận tăng sau một chiến dịch tấn công.

Ngưỡng hoặc calibration có thể cần điều chỉnh ngay cả khi cấu trúc `P(Y|X)` vẫn tương đối ổn định.

## Concept Drift

Mối quan hệ giữa đầu vào và mục tiêu thay đổi:

\[
P_{train}(Y|X)\neq P_{prod}(Y|X)
\]

Đây thường là dạng nguy hiểm nhất: pattern từng có tính dự đoán không còn đúng.

Ví dụ kẻ gian thay đổi hành vi sau khi biết rule hoặc model.

## Covariate Shift

Thuật ngữ này thường dùng khi `P(X)` thay đổi nhưng giả định `P(Y|X)` vẫn ổn định. Trong một số điều kiện, reweighting có thể giúp.

Tuy nhiên cần kiểm chứng giả định thay vì chỉ gắn nhãn theo taxonomy.

## Thay đổi theo Mùa và Drift gây hại

Tính mùa vụ có thể dự đoán được và không nhất thiết là bất thường. Traffic bán lẻ cuối tuần khác ngày thường là bình thường.

Giám sát cần mốc tham chiếu phù hợp, ví dụ so sánh cùng thứ trong tuần hoặc cùng mùa thay vì một baseline tĩnh duy nhất.

## Phát hiện Drift

Có thể dùng:

- Population Stability Index;
- KS test;
- Jensen–Shannon divergence;
- histogram theo đặc trưng;
- giám sát phân phối embedding;
- kiểm định hai mẫu bằng classifier.

Nhưng ý nghĩa thống kê không đồng nghĩa ý nghĩa kinh doanh, đặc biệt khi cỡ mẫu rất lớn.

## Prediction Drift

Theo dõi phân phối của score hoặc output. Nếu xác suất dự đoán đột ngột thay đổi, nguyên nhân có thể là input shift, thay đổi model/config hoặc lỗi downstream.

Prediction drift là triệu chứng, không phải nguyên nhân gốc.

## Performance Drift

Khi ground truth đến sau, có thể theo dõi trực tiếp:

```text
accuracy / F1 / AUC
calibration
hàm mất mát có tính tới chi phí
kết quả kinh doanh
```

Đây là bằng chứng mạnh hơn chỉ nhìn input drift.

## Nhãn đến trễ

Kết quả gian lận có thể chỉ biết sau nhiều tuần hoặc tháng. Vì vậy hệ thống cần join dự đoán với nhãn đến trễ bằng prediction ID và timestamp bất biến.

Nếu không lưu context và phiên bản tại thời điểm dự đoán, đánh giá hồi cứu sẽ rất khó.

## Trigger cho Huấn luyện lại

Huấn luyện lại có thể được kích hoạt bởi:

- lịch định kỳ;
- đủ dữ liệu có nhãn mới;
- suy giảm hiệu năng;
- nguồn dữ liệu thay đổi lớn;
- policy hoặc business rule thay đổi.

Một ngưỡng drift đơn lẻ hiếm khi nên kích hoạt tự động việc thăng cấp mô hình mới.

## Cửa sổ Huấn luyện lại

Nên huấn luyện trên toàn bộ lịch sử hay chỉ cửa sổ gần đây? Toàn bộ lịch sử ổn định hơn nhưng chứa pattern cũ; cửa sổ gần đây thích nghi nhanh hơn nhưng phương sai cao và dễ quên trường hợp hiếm.

Có thể dùng lịch sử có trọng số hoặc phát lại dữ liệu phân tầng (stratified replay).

## Catastrophic Forgetting trong Continual Setting

Cập nhật mô hình theo phân phối mới có thể làm giảm khả năng cũ. Đánh giá phải giữ bộ dữ liệu lịch sử ổn định và bộ regression cho long-tail.

## Vòng phản hồi

Quyết định của mô hình ảnh hưởng nhãn tương lai. Ví dụ mô hình tín dụng chỉ phê duyệt một nhóm người dùng, nên nhãn hoàn trả chỉ được quan sát trên nhóm đã được phê duyệt.

Huấn luyện lại trực tiếp trên dữ liệu quan sát được có thể tạo thiên lệch lựa chọn.

## Drift trong LLM và RAG

Hệ thống LLM có thể drift do:

```text
provider cập nhật mô hình
prompt thay đổi
retrieval corpus thay đổi
mô hình embedding được cập nhật
index được rebuild
phân phối truy vấn người dùng thay đổi
hành vi API của tool thay đổi
```

Không phải trường hợp nào cũng cần huấn luyện lại mô hình; nhiều khi rollback cấu hình hoặc index mới là phản ứng đúng.

## Recalibration và Huấn luyện lại

Nếu khả năng xếp hạng hoặc phân biệt vẫn tốt nhưng xác suất bị lệch, recalibration hoặc điều chỉnh threshold có thể rẻ hơn huấn luyện lại toàn bộ.

## Champion–Challenger sau Huấn luyện lại

Mô hình được huấn luyện lại trở thành challenger. Nên so với champion trên bộ đánh giá cố định, bộ đánh giá gần đây và production shadow trước khi thăng cấp.

## Ngừng sử dụng Mô hình

Vòng đời không chỉ có huấn luyện lại. Một mô hình có thể được retire khi use case không còn, nguồn dữ liệu bị ngừng hoặc có giải pháp thay thế tốt hơn.

Artifact đã lưu trữ vẫn cần chính sách retention phù hợp với governance.

## Mô hình tư duy

```text
Drift là bằng chứng rằng thế giới hoặc pipeline đã thay đổi.
Huấn luyện lại chỉ là một trong nhiều phản ứng có thể có.
```

## Những nhầm lẫn thường gặp

### “Phân phối đặc trưng thay đổi thì mô hình chắc chắn hỏng”

Không. Cần nối shift với hiệu năng tác vụ thực tế.

### “Huấn luyện lại thường xuyên luôn tốt”

Không. Dữ liệu mới có thể nhiễu hoặc thiên lệch, và huấn luyện cũng có chi phí/rủi ro.

### “Drift chỉ là vấn đề của tabular ML”

Không. LLM, RAG và Agent cũng drift qua người dùng, corpus, tool và phiên bản mô hình.

## Liên kết kiến thức

Xem [Monitoring](./06_monitoring_and_observability.md), [Continuous Training](./04_ci_cd_ct_for_ai.md), [Dataset Bias](../14_data_for_ai/06_dataset_bias.md) và [Evaluation](../18_evaluation_reliability_interpretability/README.md).