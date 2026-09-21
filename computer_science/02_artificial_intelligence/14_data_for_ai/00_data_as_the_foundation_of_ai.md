# Dữ liệu là Nền tảng của AI

Một mô hình AI chỉ học được từ những thông tin mà pipeline dữ liệu quan sát và giữ lại. Vì vậy **dữ liệu (data / 데이터)** không phải nguyên liệu trung tính; nó là kết quả của đo lường (measurement), lựa chọn (selection), gán nhãn (labeling), ghi log và chính sách thu thập.

Mô hình tư duy:

```text
Thế giới thực
→ đo lường / ghi nhận sự kiện
→ dữ liệu thô
→ lọc / gán nhãn / biến đổi
→ tập dữ liệu huấn luyện
→ mô hình
→ quyết định
→ hành vi và dữ liệu mới trong thế giới thực
```

Vòng lặp cuối cùng đặc biệt quan trọng: một hệ thống AI sau khi triển khai có thể thay đổi chính dữ liệu mà nó sẽ nhìn thấy trong tương lai.

## Dataset không phải là Thực tế

Tập dữ liệu (dataset) chỉ là một mẫu lấy ra từ quá trình sinh dữ liệu (data-generating process). Nếu quá trình đó có thiên lệch, mô hình cũng có xu hướng học lại thiên lệch của quá trình.

Ví dụ, một dataset cho vay thường chỉ có kết quả trả nợ của những người đã được phê duyệt. Ta không quan sát được điều gì sẽ xảy ra nếu những người từng bị từ chối cũng được cho vay. Đây là vấn đề phản thực tế (counterfactual) điển hình.

## Quá trình Sinh dữ liệu

Một câu hỏi rất quan trọng là:

> Dữ liệu này xuất hiện bằng cơ chế nào?

Cần hiểu ít nhất:

- ai hoặc hệ thống nào tạo ra sự kiện;
- sensor hoặc log nào ghi nhận nó;
- trường hợp nào có thể bị thiếu;
- chính sách nào quyết định dữ liệu nào được đưa vào;
- label được xác định ở thời điểm nào;
- môi trường triển khai khác môi trường thu thập dữ liệu ra sao.

Nếu không hiểu quá trình sinh dữ liệu, rất dễ coi các pattern ngẫu nhiên hoặc thiên lệch của hệ thống ghi nhận là “quy luật của thế giới”.

## Dữ liệu Quan sát

Phần lớn dữ liệu machine learning trong production là **dữ liệu quan sát (observational data)** chứ không phải kết quả của thí nghiệm ngẫu nhiên có kiểm soát.

Tương quan trong dữ liệu có thể đến từ biến nhiễu (confounding), quy tắc lựa chọn mẫu hoặc hành vi của hệ thống hiện tại. Một mô hình dự đoán vẫn có thể hoạt động tốt nếu distribution triển khai tương tự, nhưng không nên tự động diễn giải correlation thành quan hệ nhân quả.

## Schema của Dữ liệu

Schema không chỉ là kiểu dữ liệu. Nó còn phải là một **hợp đồng ngữ nghĩa (semantic contract)** mô tả rõ:

```text
ý nghĩa của field
đơn vị
ngữ nghĩa thời gian
quy tắc nullable
nguồn dữ liệu
version
miền giá trị hợp lệ
mức độ nhạy cảm / privacy class
```

Giá trị `amount = 100` gần như vô nghĩa nếu không biết currency, unit và thời điểm mà con số đó đại diện.

## Event Time và Processing Time

Trong hệ thống streaming hoặc transaction cần phân biệt:

```text
event_time      → thời điểm sự kiện thật sự xảy ra
processing_time → thời điểm pipeline nhận hoặc xử lý sự kiện
```

Nhiều lỗi data leakage trong ML xuất hiện khi feature được tính bằng thông tin chỉ xuất hiện **sau** thời điểm cần dự đoán.

## Tính đúng theo Thời điểm

Một training example tại thời điểm `t` chỉ được phép dùng những thông tin mà production thật sự có thể biết tại `t`.

```text
thời điểm dự đoán = 10:00
feature sử dụng chargeback chỉ được phát hiện lúc 14:00
→ rò rỉ dữ liệu (data leakage)
```

Feature store hoặc truy vấn dữ liệu lịch sử vì vậy cần hỗ trợ **as-of semantics** hoặc point-in-time correctness.

## Đơn vị Quan sát

Một row trong dataset có thể đại diện cho:

- người dùng;
- giao dịch;
- phiên làm việc;
- ảnh;
- tài liệu;
- cửa sổ thời gian.

Chọn sai đơn vị quan sát có thể tạo duplicate weighting hoặc leakage. Ví dụ nhiều ảnh của cùng một bệnh nhân bị chia ngẫu nhiên sang cả train và test có thể làm metric cao giả tạo vì hai tập không thật sự độc lập.

## Lấy mẫu

Training distribution đôi khi cố ý lấy nhiều mẫu từ class hiếm để mô hình học tốt hơn. Điều này hữu ích cho optimization nhưng làm thay đổi tỷ lệ class so với môi trường production.

Nếu class prior ở deployment khác training, xác suất dự đoán, calibration và threshold có thể cần được điều chỉnh lại.

## Độ phủ của Dữ liệu

Dataset nên bao phủ không gian vận hành mà hệ thống sẽ gặp, ví dụ:

```text
ngôn ngữ
thiết bị
khu vực
điều kiện ánh sáng / tiếng ồn
nhóm khách hàng
các trường hợp hiếm nhưng quan trọng
```

Không thể kỳ vọng một mô hình generalize ổn định sang vùng mà training data chưa từng đại diện, trừ khi có assumption hoặc transfer learning phù hợp.

## Long Tail

Dữ liệu thực tế thường có phân bố đuôi dài (long-tail distribution). Các trường hợp phổ biến chiếm phần lớn dataset, trong khi những lỗi hiếm nhưng có tác động lớn lại có rất ít supervision.

Chiến lược xử lý có thể gồm thu thập có mục tiêu, reweighting, synthetic data hoặc rule riêng cho nhóm rủi ro cao.

## Dữ liệu Trùng lặp

Duplicate làm tăng giả số lượng sample hiệu quả và có thể bị phân tán qua train/test split.

Near-duplicate còn khó hơn exact duplicate: ảnh đã crop hoặc resize, tài liệu được copy, câu bị paraphrase hoặc dữ liệu được xuất lại từ cùng một nguồn có thể vẫn gần như cùng một observation.

## Versioning cho Dataset

Dataset là một artifact cần được version hóa. Một experiment có thể tái tạo được khi ta biết:

```text
snapshot nguồn
version của code biến đổi
các filter đã áp dụng
version của label
cách chia train / validation / test
hash hoặc manifest của dữ liệu
```

Không có versioning, kết quả “model A tốt hơn model B” rất khó kiểm chứng vì hai lần train có thể đã dùng dataset khác nhau.

## Data Lineage

**Dòng dõi dữ liệu (data lineage)** theo dõi nguồn gốc của feature và dataset:

```text
bảng trong database nguồn
→ ETL job
→ phép biến đổi feature
→ training dataset
→ model version
```

Lineage đặc biệt quan trọng cho debugging, compliance và phân tích ảnh hưởng khi một nguồn dữ liệu thay đổi.

## Feedback Loop

Một recommender hiển thị một số item → người dùng tương tác với những item được hiển thị → các interaction này lại trở thành training data mới.

Mô hình vì vậy có thể thay đổi distribution của dữ liệu tương lai. Điều này có thể khuếch đại popularity bias hoặc khiến hệ thống ngày càng ít quan sát các lựa chọn đã không được đề xuất.

## Selective Labels

Đôi khi outcome chỉ được quan sát sau một quyết định cụ thể. Ví dụ:

- default chỉ được quan sát ở khoản vay đã phê duyệt;
- kết quả y tế chỉ có ở bệnh nhân đã được xét nghiệm;
- fraud chỉ được xác nhận ở giao dịch đã bị điều tra.

Đây là **selective labels** và làm cho assumption i.i.d. đơn giản trở nên không đầy đủ. Một số bài toán có thể cần exploration, causal inference hoặc policy-aware evaluation.

## Dữ liệu Thiếu

Cơ chế missing rất quan trọng:

- **MCAR**: missing không liên quan tới các biến;
- **MAR**: missing phụ thuộc vào dữ liệu đã quan sát;
- **MNAR**: missing phụ thuộc vào giá trị hoặc quá trình chưa quan sát được.

Imputation không thể tự khôi phục chính xác thông tin MNAR tùy ý. Trước khi chọn kỹ thuật điền giá trị thiếu, cần hiểu vì sao dữ liệu bị thiếu.

## Dữ liệu Có cấu trúc và Không có cấu trúc

Structured data có schema rõ. Văn bản, ảnh và audio thường được gọi là unstructured data, nhưng chúng vẫn có metadata, provenance và cấu trúc tiềm ẩn.

“Unstructured” không có nghĩa pipeline không cần schema, versioning hoặc validation.

## Dữ liệu cho Foundation Model

Ở quy mô web, quá trình curation có thể bao gồm:

- loại dữ liệu trùng lặp (deduplication);
- nhận diện ngôn ngữ;
- lọc chất lượng;
- lọc an toàn;
- theo dõi license và provenance;
- loại contamination;
- điều chỉnh tỷ trọng giữa các nguồn dữ liệu.

Tỷ lệ các nguồn trong data mixture thực chất là một phần của training objective: domain nhận nhiều token hơn cũng nhận nhiều gradient update hơn.

## Benchmark Contamination

Nếu dữ liệu evaluation hoặc near-duplicate của nó xuất hiện trong training/pretraining, benchmark không còn đo generalization một cách sạch sẽ.

Exact string matching thường không đủ để phát hiện contamination vì dữ liệu có thể đã được paraphrase hoặc dẫn xuất qua nhiều nguồn trung gian.

## Số lượng và Chất lượng Dữ liệu

Nhiều dữ liệu thường có ích, nhưng dữ liệu chất lượng thấp, trùng lặp hoặc nhiều nhiễu có thể làm lãng phí compute hoặc dạy mô hình các pattern không mong muốn.

Giá trị thực tế của dữ liệu phụ thuộc vào diversity, relevance, correctness và coverage, không chỉ số row hoặc số token.

## Active Learning

Thay vì gán nhãn ngẫu nhiên, **học chủ động (active learning)** cho mô hình chọn những sample bất định hoặc giàu thông tin để con người annotate.

Cách này có thể giảm chi phí labeling, nhưng heuristic về uncertainty vẫn có thể bỏ sót những blind spot mà model đang quá tự tin một cách sai lầm.

## Data-Centric AI

Khi pipeline và model baseline đã tương đối ổn định, cải thiện label, coverage và definition của dữ liệu thường mang lại lợi ích lớn hơn việc liên tục đổi architecture.

**Data-centric AI** không có nghĩa model không quan trọng; nó coi chất lượng dữ liệu là một đối tượng engineering cần được đo, version và cải tiến có hệ thống.

## Quyền riêng tư

Training data có thể chứa dữ liệu cá nhân hoặc nhạy cảm. Quy trình thu thập cần xem xét purpose limitation, data minimization, retention và access control.

Anonymization đặc biệt khó với dữ liệu high-dimensional; text hoặc image có thể cho phép tái nhận diện gián tiếp dù identifier trực tiếp đã bị loại bỏ.

## Mô hình tư duy

> **Dataset là một góc nhìn đã được đo lường và ghi nhận về thực tế, được tạo ra bởi một quá trình. Muốn hiểu mô hình, trước hết phải hiểu quá trình tạo dataset.**

## Những nhầm lẫn thường gặp

### “Dữ liệu tự nói lên tất cả”

Không. Ý nghĩa của dữ liệu phụ thuộc measurement, schema, sampling và selection process.

### “Càng nhiều row càng tốt”

Không. Duplicate, noise và mất cân bằng coverage có thể làm giá trị biên của dữ liệu giảm mạnh.

### “Random train/test split luôn đúng”

Không. Quan hệ theo time, group hoặc entity thường yêu cầu cách chia khác để tránh leakage.

## Liên kết kiến thức

Data layer nối Thống kê, Database, Distributed Systems, Privacy và đánh giá Machine Learning.

Xem tiếp: [Thu thập Dữ liệu](./01_data_collection.md).