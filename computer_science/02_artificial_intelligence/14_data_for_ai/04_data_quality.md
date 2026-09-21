# Chất lượng Dữ liệu

**Chất lượng dữ liệu (data quality / 데이터 품질)** không phải một điểm số duy nhất. Một dataset có thể sạch về format nhưng vẫn kém vì coverage thiếu, label sai, timestamp đã stale hoặc distribution lệch xa môi trường deployment.

Một framework thực dụng nên nhìn qua nhiều chiều:

```text
độ đúng — correctness
độ đầy đủ — completeness
độ nhất quán — consistency
độ duy nhất — uniqueness
độ mới — freshness
độ phủ — coverage
mức đại diện — representativeness
chất lượng label
lineage
khả năng sẵn sàng — availability
```

## Độ đúng

Giá trị có phản ánh hiện tượng thật không? `country=KR` có thể hoàn toàn hợp schema nhưng vẫn sai với user cụ thể.

Correctness thường cần reference source, audit domain hoặc đối chiếu với nguồn authoritative.

## Độ đầy đủ

Bao nhiêu thông tin bắt buộc bị missing? Tuy nhiên completeness 100% cũng không bảo đảm usefulness; field có thể đã được điền bằng default value vô nghĩa chỉ để không còn null.

Vì vậy completeness phải được đánh giá cùng semantics của giá trị.

## Độ nhất quán

Cùng một concept có được biểu diễn nhất quán giữa các source và theo thời gian không?

```text
currency = KRW ở table A
currency = USD ở table B
nhưng field name giống nhau
```

Semantic inconsistency thường nguy hiểm hơn schema mismatch rõ ràng vì pipeline vẫn chạy nhưng ý nghĩa dữ liệu đã lệch.

## Độ duy nhất

Duplicate example làm thay đổi effective weighting của dataset.

Cần định nghĩa duplicate theo entity hoặc event chứ không chỉ exact row equality. Hai row khác ID vẫn có thể là cùng một real-world event.

## Độ mới

Feature hoặc source có được cập nhật đủ nhanh cho use case không? User profile từ sáu tháng trước có thể hợp format nhưng đã stale với decision hiện tại.

Nên định nghĩa **freshness SLA** riêng cho từng feature hoặc source thay vì một ngưỡng chung cho toàn dataset.

## Độ phủ

Dataset có chứa những case mà hệ thống thật sự sẽ gặp không? Coverage nên được phân tích theo các chiều có ý nghĩa như:

- khu vực địa lý;
- thiết bị;
- ngôn ngữ;
- class;
- thời gian;
- sensor;
- subgroup;
- edge case.

Aggregate row count lớn không chứng minh coverage tốt.

## Mức độ Đại diện

Training distribution có gần với target deployment distribution không?

Oversampling một class hiếm có thể là lựa chọn có chủ đích để giúp học tốt hơn, nhưng calibration và evaluation phải tính tới việc class prior ở production khác training.

## Chất lượng Label

Một số metric hữu ích gồm:

- mức disagreement giữa annotator;
- tỷ lệ cần adjudication;
- accuracy trên known-answer task;
- class-specific noise;
- label latency và maturity.

Chất lượng label phải được theo dõi như một thành phần của data quality, không phải giả định luôn đúng.

## Chất lượng Lineage

Nếu không biết dữ liệu đến từ đâu, qua transformation nào và version nào, việc debug gần như không thể dù các value nhìn có vẻ hợp lý.

Lineage tốt cho phép truy ngược:

```text
model prediction
→ feature version
→ dataset snapshot
→ transform job
→ source record
```

## Dashboard về Sức khỏe Dataset

Nên monitor xu hướng theo thời gian chứ không chỉ chạy check một lần:

```text
row / event count
null rate
số entity duy nhất
class prior
feature quantile
category cardinality
freshness
label delay
join failure
```

Điều quan trọng là phát hiện biến động bất thường giữa các dataset version hoặc giữa training và production.

## Kiểm tra Distribution

Có thể so sánh reference distribution với dữ liệu hiện tại bằng các metric thống kê như:

- PSI;
- KS statistic;
- Wasserstein distance;
- Jensen–Shannon divergence;
- kiểm định dạng chi-square cho category.

Không có một threshold universal. Với dataset rất lớn, khác biệt thống kê cực nhỏ cũng có thể trở nên “significant” dù không có business impact. Cần nhìn cả effect size và ảnh hưởng tới decision.

## Schema Drift và Semantic Drift

**Schema drift** xảy ra khi field name, type hoặc structure thay đổi.

**Semantic drift** xảy ra khi schema vẫn giống nhưng ý nghĩa đổi. Ví dụ `status=1` trước đây nghĩa là `active`, nhưng sau một phiên bản service lại nghĩa là `verified`.

Semantic drift khó phát hiện tự động hơn nhiều, vì vậy semantic contract và versioning rất quan trọng.

## Feature Drift

Distribution của input thay đổi:

\[
P_t(X) \neq P_{ref}(X)
\]

Không phải mọi feature drift đều làm model kém đi. Cần liên hệ drift với performance hoặc decision quality thay vì chỉ cảnh báo vì distribution khác.

## Label Drift và Concept Drift

Quan hệ giữa input và target có thể thay đổi:

\[
P_t(Y\mid X) \neq P_{ref}(Y\mid X)
\]

Đây thường là dạng drift nguy hiểm hơn, nhưng label thực tế hay đến trễ nên việc phát hiện cũng khó hơn.

## Data Slice

Metric aggregate dễ che lỗi theo subgroup. Nên định nghĩa các slice quan trọng như:

```text
user mới
ngôn ngữ hiếm
camera model cụ thể
ảnh chụp ban đêm
giao dịch giá trị cao
```

Mỗi slice cần đủ sample và có quality metric riêng.

## Quality Gate

Trước khi dùng một snapshot để train hoặc deploy, pipeline có thể enforce các gate như:

```text
schema hợp lệ
không có critical feature vượt ngưỡng missing
label maturity đầy đủ
leakage audit đạt yêu cầu
coverage tối thiểu đạt chuẩn
lineage đã được ghi lại
```

Critical gate fail nên chặn pipeline thay vì chỉ hiện màu đỏ trên dashboard.

## Golden Record

Một tập nhỏ **golden record** có expected transformation rõ ràng giúp test ETL và feature pipeline end-to-end.

Khi transform code thay đổi, golden record cho biết logic có bị regression không.

## Data Quality và Model Metric

Mô hình đôi khi vẫn tạm thời hoạt động tốt dù upstream data đã có vấn đề nhờ redundancy hoặc vì lỗi mới chưa tác động tới nhiều sample.

Data-quality monitoring giúp phát hiện incident trước khi model metric giảm rõ rệt.

## Data Quality Debt

Team có thể tích lũy **data debt** giống technical debt: field không tài liệu hóa, join mong manh, source thay đổi không version, default value không rõ semantics.

Data debt làm mọi cải tiến mô hình sau đó chậm và khó tin cậy hơn.

## Chất lượng Dữ liệu Không có cấu trúc

Với text, có thể kiểm tra:

- encoding;
- spam;
- boilerplate;
- language;
- truncation;
- reliability của source và fact.

Với image/audio, có thể kiểm tra:

- corruption;
- resolution;
- blur hoặc noise;
- clipping;
- metadata mismatch.

## Chất lượng Dữ liệu cho Foundation Model

Ở quy mô lớn, cần thêm các concern ở cấp mixture:

```text
phân bố chất lượng giữa các source
deduplication
benchmark contamination
cân bằng ngôn ngữ
repetition
tỷ lệ synthetic content
```

Dữ liệu chất lượng thấp nhưng bị lặp nhiều có thể nhận lượng gradient không tương xứng và ảnh hưởng model mạnh hơn số lượng source gợi ý.

## Ví dụ Data Quality Incident

Giả sử upstream outage làm risk score bị thiếu, nhưng pipeline mới tự điền `0`. Schema và null check đều pass vì `0` là numeric value hợp lệ.

Tuy nhiên dashboard distribution sẽ cho thấy một spike đột ngột tại `0`.

Ví dụ này cho thấy data quality không thể chỉ dựa vào type và nullability; cần hiểu statistical semantics của feature.

## Mô hình tư duy

> **Data quality đặt câu hỏi: dataset này có đủ đáng tin để hỗ trợ đúng inference hoặc decision mà ta muốn, tại đúng thời điểm và trên đúng population deployment hay không?**

## Những nhầm lẫn thường gặp

### “Không còn null nghĩa là data quality cao”

Không. Default value có thể che mất missingness thật.

### “Có data drift nghĩa là model hỏng”

Không. Một số drift không liên quan tới outcome; cần kiểm tra tác động thật.

### “Chất lượng dữ liệu là trách nhiệm riêng của preprocessing team”

Không. Producer, data engineer, ML engineer và domain owner cùng chịu trách nhiệm về semantics và reliability.

## Liên kết kiến thức

Data quality nối Observability, Data Contract, Statistics và MLOps Monitoring.

Xem tiếp: [Rò rỉ Dữ liệu](./05_data_leakage.md).