# Rò rỉ Dữ liệu

**Rò rỉ dữ liệu (data leakage / 데이터 누수)** xảy ra khi training hoặc evaluation pipeline cho mô hình tiếp cận thông tin mà production inference thực tế sẽ không có, hoặc khi thông tin từ validation/test ảnh hưởng ngược trở lại training. Leakage tạo metric đẹp giả tạo và là một trong những failure nghiêm trọng nhất của hệ thống Machine Learning.

## Target Leakage

Feature chứa trực tiếp hoặc gián tiếp thông tin về target sau thời điểm cần prediction.

Ví dụ cần dự đoán fraud ngay tại thời điểm giao dịch nhưng feature lại chứa:

```text
chargeback_status
manual_investigation_result
post-transaction dispute count
```

Mô hình không hề “thông minh” hơn; nó chỉ đang nhìn thấy tương lai.

## Temporal Leakage

Feature aggregate vô tình sử dụng các event xảy ra sau prediction time.

Ví dụ cần dự đoán churn vào ngày 1/9 nhưng feature “số support ticket trong tháng 9” lại được tính bằng toàn bộ bảng của cả tháng.

Feature hợp lệ phải dùng truy vấn theo thời điểm:

```text
chỉ dùng event có event_time <= prediction_time
```

## Nhiễm chéo giữa Train và Test

Cùng một entity hoặc near-duplicate xuất hiện ở cả hai phía, ví dụ:

- frame từ cùng một video;
- record của cùng bệnh nhân;
- tài liệu web được copy;
- nhiều transaction của cùng customer;
- phiên bản augmented của cùng một ảnh.

Random row split không đủ nếu các observation có correlation theo group.

## Preprocessing Leakage

Nếu fit scaler, PCA, imputer hoặc vocabulary trên toàn dataset trước khi split:

\[
\mu = mean(train+test)
\]

thì distribution của test đã ảnh hưởng transformation dùng cho train.

Pattern đúng là:

```text
fit transformation trên train
→ đóng băng tham số
→ áp dụng lên validation và test
```

## Feature Selection Leakage

Nếu chọn feature dựa trên correlation với target được tính bằng cả test set, test đã tham gia vào model design.

Feature selection và hyperparameter tuning phải nằm trong training/validation process, không được dùng final test làm tín hiệu cải tiến.

## Cross-Validation Leakage

Nếu preprocessing được fit bên ngoài các cross-validation fold, thông tin giữa các fold có thể bị rò rỉ.

Mỗi fold phải fit transformation trên phần training của chính fold đó rồi mới apply sang phần validation tương ứng.

## Leakage qua Quy trình Human Labeling

Field do con người tạo có thể encode outcome một cách gián tiếp.

Ví dụ analyst viết note sau khi case đã được giải quyết và note chứa câu “confirmed fraud”. Nếu model phải triage **trước** khi analyst xử lý, note này là một feature bất hợp lệ dù nó tồn tại trong database.

## Proxy Leakage

Một feature có thể technically tồn tại tại prediction time nhưng chỉ xuất hiện vì quy trình production hiện tại đã ngầm biết target.

Ví dụ `queue=fraud_team` cho biết upstream rule đã đánh dấu case là đáng ngờ. Mô hình có thể đạt metric rất cao nhưng thực chất chỉ học lại routing logic cũ và sẽ dễ hỏng nếu quy trình routing thay đổi.

## Identifier Leakage

ID đôi khi encode time, source hoặc category ngoài ý muốn. Model có thể memorize entity hoặc batch thay vì học signal tổng quát.

Những high-cardinality ID cần được audit cẩn thận ngay cả khi nhìn bề ngoài chúng không liên quan target.

## Duplicate Leakage trong Foundation Model

Text trong benchmark evaluation có thể đã xuất hiện nguyên văn hoặc dưới dạng paraphrase trong pretraining corpus. Khi đó benchmark score trộn lẫn generalization và memorization.

Contamination detection có thể dùng exact hash, n-gram similarity, semantic matching và source provenance, nhưng rất khó phát hiện hoàn hảo ở quy mô lớn.

## Leakage trong Đánh giá RAG

Nếu gold answer được đưa thẳng vào indexed corpus theo cách không giống production, hệ thống RAG có thể retrieve đáp án quá trực tiếp và tạo score không thực tế.

Evaluation corpus phải được xây sao cho phản ánh đúng dữ liệu mà deployment thật sự có.

## Time-Based Split

Với hệ thống dự đoán tương lai, cách chia **train quá khứ → validation/test tương lai** thường mô phỏng deployment tốt hơn:

```text
train: Jan–Jun
validation: Jul
test: Aug
```

Tuy nhiên một time split duy nhất có thể chịu seasonality hoặc regime shift mạnh; rolling backtest giúp đánh giá ổn định hơn.

## Group Split

Toàn bộ observation của cùng một entity nên nằm trong cùng một split, ví dụ theo:

```text
patient_id
user_id
company_id
device_id
video_id
```

Điều này giảm nguy cơ model memorize entity rồi “nhận lại” nó ở test.

## Spatial Leakage

Trong dữ liệu địa lý, các điểm gần nhau thường correlation mạnh. Random point split có thể làm test quá dễ vì train đã chứa các vị trí lân cận.

Nếu mục tiêu là generalize sang vùng mới, có thể cần **spatial block split**.

## Câu hỏi Audit Leakage

Với mỗi feature, nên hỏi:

1. feature này được tạo ở thời điểm nào?
2. source event có xảy ra trước prediction time không?
3. production có thể compute cùng logic vào đúng thời điểm không?
4. target hoặc downstream decision có ảnh hưởng ngược lên feature không?
5. cùng entity hoặc derivative của dữ liệu có xuất hiện ở test không?

## Point-in-Time Join trong Feature Store

Khi tạo historical training set, join đúng phải chọn feature value mới nhất **có sẵn trước event time**, không phải record mới nhất ở hiện tại.

Đây là một chức năng cốt lõi của temporal feature store.

## Hidden Leakage qua Aggregate

Một monthly aggregate có thể mang timestamp là ngày đầu tháng nhưng thực tế chỉ được tính sau khi tháng kết thúc.

Vì vậy timestamp field không đủ chứng minh feature đã available; lineage cần ghi cả **availability time**.

## Hyperparameter Overfitting

Nếu team liên tục xem test score rồi chỉnh model, test set dần trở thành một validation set không chính thức. Final metric khi đó sẽ optimistic.

Cần final holdout ẩn hoặc quy trình evaluation nghiêm ngặt hơn như nested validation khi tuning nhiều vòng.

## Early Stopping

Dùng validation để early stopping là hợp lệ vì validation thuộc quá trình model selection.

Nhưng final test phải được giữ nguyên và chỉ dùng sau khi model selection hoàn tất.

## Dấu hiệu Gợi ý Leakage

Một số tín hiệu đáng nghi:

- metric cao bất thường;
- một feature áp đảo toàn bộ feature importance;
- performance sụp mạnh khi dùng future split;
- model rất tốt offline nhưng kém online;
- feature correlation chỉ xuất hiện sau outcome timestamp.

Metric cao không chứng minh có leakage, nhưng là lý do chính đáng để audit kỹ.

## Ví dụ: Credit Risk

Feature `days_past_due_current` có thể hợp lệ khi dự đoán default trong 12 tháng tiếp theo ở thời điểm hiện tại, nhưng lại bất hợp lệ nếu mục tiêu là dự đoán default ngay tại thời điểm loan origination.

Một feature có “hợp pháp” hay không phụ thuộc định nghĩa task và prediction timestamp.

## Mô hình tư duy

> **Leakage nghĩa là mô hình nhận thông tin nằm ngoài ranh giới thông tin thực sự tồn tại tại thời điểm ra quyết định.**

Hãy suy nghĩ như một auditor kiểm tra timeline, không chỉ như người thao tác dataframe.

## Những nhầm lẫn thường gặp

### “Leakage chỉ là vô tình đưa target column vào feature”

Không. Temporal aggregate, duplicate, human workflow và preprocessing leakage còn phổ biến và tinh vi hơn.

### “Random split ngăn được leakage”

Không nếu dữ liệu có correlation theo time, group hoặc không gian.

### “Feature có trong database thì dùng được”

Không. Nó có thể chỉ xuất hiện sau prediction time hoặc chỉ được biết nhờ một downstream process.

## Liên kết kiến thức

Leakage nối Temporal Database, Causal Process Understanding và Evaluation Design.

Xem tiếp: [Thiên lệch Dataset](./06_dataset_bias.md).