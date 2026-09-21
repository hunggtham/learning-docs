# Làm sạch Dữ liệu

**Làm sạch dữ liệu (data cleaning / 데이터 정제)** không phải thao tác máy móc kiểu “xóa những hàng xấu”. Đây là quá trình phát hiện và xử lý inconsistency, corruption, missingness, duplicate và lỗi ngữ nghĩa trong khi vẫn cố giữ lại những tín hiệu thật sự có giá trị cho mô hình.

## Làm sạch bắt đầu từ Schema và Ngữ nghĩa

Một giá trị chỉ có thể được gọi là không hợp lệ khi ta hiểu ý nghĩa của field.

```text
age = 250      → không hợp lệ nếu age tính theo năm
amount = -10   → có thể là lỗi, nhưng cũng có thể là refund hợp lệ
lat = 91       → không hợp lệ với geographic latitude
```

Vì vậy data cleaning cần domain contract, không chỉ một tập generic function.

## Giá trị Thiếu

Missing data có thể xuất hiện vì nhiều nguyên nhân:

- field là optional;
- sensor bị lỗi;
- user từ chối cung cấp;
- feature không áp dụng cho trường hợp đó;
- nguồn dữ liệu tạm thời không khả dụng;
- join không khớp;
- logging bug.

Nếu gộp tất cả về `null` rồi tự động điền mean, ta có thể xóa mất thông tin về chính cơ chế missing.

Một pattern hữu ích là lưu:

```text
giá trị
+ cờ missing
+ lý do missing nếu biết
```

## Imputation

Một số cách điền giá trị thiếu phổ biến gồm:

- hằng số hoặc sentinel;
- mean, median hoặc mode;
- giá trị theo group;
- model-based imputation;
- forward fill cho time series khi ngữ nghĩa cho phép.

Các thống kê dùng cho imputation phải được fit trên training data. Nếu tính mean bằng cả test data, distribution information của test đã bị rò rỉ vào training pipeline.

## Outlier

Một outlier có thể là:

- lỗi dữ liệu;
- trường hợp hiếm nhưng hợp lệ;
- chính fraud hoặc anomaly mà mô hình cần phát hiện.

Xóa hoặc clip outlier một cách máy móc có thể phá đúng những case quan trọng nhất.

Cần kết hợp domain bound, phân tích distribution và kiểm tra source trước khi quyết định.

## Dữ liệu Trùng lặp

Exact duplicate row tương đối dễ phát hiện, nhưng duplicate theo entity hoặc event khó hơn.

Ví dụ:

```text
cùng giao dịch được retry với event id khác
cùng tài liệu được mirror trên nhiều website
cùng ảnh được resize hoặc crop
cùng patient study được export hai lần
```

Phải định nghĩa rõ duplicate nghĩa là gì trong domain cụ thể.

## Entity Resolution

Nhiều record có thể cùng đại diện cho một entity nhưng dùng ID hoặc tên khác nhau. **Entity resolution** có thể dựa trên deterministic key, fuzzy matching hoặc probabilistic linkage.

False merge rất nguy hiểm vì nó tạo ra một lịch sử kết hợp giả giữa những entity thực ra khác nhau.

## Chuẩn hóa Kiểu dữ liệu và Đơn vị

Ví dụ điển hình:

```text
height: cm so với m
currency: KRW so với USD
timezone: local time so với UTC
date: DD/MM so với MM/DD
```

Một numeric field không có unit rõ ràng là một bug tiềm ẩn.

Nên chuẩn hóa unit nhưng vẫn giữ provenance của giá trị raw khi cần audit hoặc debug.

## Chuẩn hóa Categorical Data

`Seoul`, `SEOUL`, `서울`, `Seoul-si` có thể là cùng một thực thể hoặc không, tùy task.

Canonicalization cần ontology và context, không thể chỉ lowercase string rồi coi như đã giải quyết.

## Làm sạch Văn bản

NLP truyền thống thường loại mạnh punctuation, stopword hoặc casing. Nhưng modern NLP/LLM có thể cần chính những tín hiệu định dạng đó.

Cleaning phải giữ lại thông tin mà downstream model thực sự cần.

Một số thao tác thường gặp:

- Unicode normalization;
- loại control character;
- lọc boilerplate;
- sửa encoding;
- language detection;
- loại duplicate paragraph.

## Unicode

Các ký tự nhìn giống nhau có thể dùng code point khác nhau. Lựa chọn giữa NFC và NFKC có thể thay đổi semantics.

NFKC thực hiện compatibility normalization mạnh hơn và có thể biến đổi một số ký hiệu đặc biệt, vì vậy cần quyết định theo task chứ không áp dụng mặc định trong mọi trường hợp.

## HTML và Dữ liệu Web

Khi trích xuất nội dung chính từ web, thường cần loại navigation, quảng cáo và script.

Tuy nhiên bộ lọc boilerplate có thể vô tình xóa code block, table hoặc citation. Nếu dữ liệu sẽ dùng cho RAG hoặc layout understanding, cấu trúc tài liệu nên được giữ càng nhiều càng tốt.

## Làm sạch Ảnh

Cần kiểm tra các lỗi như:

- file decode thất bại;
- file bị corrupt;
- aspect ratio bất thường;
- duplicate;
- ảnh trống;
- label không khớp ảnh;
- orientation metadata.

Nếu auto-rotate ảnh theo EXIF nhưng không transform annotation coordinate tương ứng, bounding box hoặc mask sẽ bị lệch.

## Làm sạch Audio

Có thể kiểm tra clipping, tỷ lệ silence, duration, sampling rate, số channel, alignment với transcript và noise level.

Resampling nên được chuẩn hóa trước khi feature extraction để tránh train-serving mismatch.

## Làm sạch Time Series

Không nên sort hoặc forward-fill mù giữa nhiều entity khác nhau. Khoảng trống sensor có thể mang ý nghĩa nghiệp vụ.

Cần dùng event-time ordering và phân biệt rõ “không có phép đo” với “giá trị thật bằng 0”.

## Referential Integrity

Join có thể âm thầm làm rơi hoặc nhân đôi row. Cần kiểm tra cardinality:

```text
kỳ vọng one-to-one
nhưng thực tế one-to-many
→ số row tăng bất thường
```

Đây là một trong những lỗi data engineering phổ biến nhất trong feature pipeline.

## Cô lập Train và Test

Những transformation học thống kê từ dữ liệu phải chỉ fit trên train:

```text
scaler
imputer
vocabulary
PCA
feature selector
```

Sau đó áp dụng transformation đã cố định cho validation và test.

## Automated Data Test

Nên xem dataset như code và có assertion rõ ràng:

```text
range của row count
tỷ lệ null
unique key
miền giá trị category
numeric bound
timestamp phải đơn điệu khi cần
join cardinality
schema version
```

Framework có thể tự động hóa, nhưng nguyên lý cốt lõi vẫn là data contract + test.

## Sửa hay Loại bỏ?

Nếu lỗi có thể được sửa một cách chắc chắn, có thể repair nhưng nên lưu audit trail.

Nếu không đủ chắc chắn, drop hoặc đưa vào quarantine thường an toàn hơn. Không nên âm thầm “bịa” một giá trị chỉ để record hợp schema.

## Quarantine Dataset

Record xấu hoặc đáng ngờ có thể được chuyển sang một quarantine dataset để review thay vì xóa vĩnh viễn.

Cách này giữ lại evidence phục vụ debugging lỗi nguồn và cải thiện pipeline trong tương lai.

## Cleaning Log

Nên theo dõi số lượng record qua từng bước:

```text
số row ban đầu
số duplicate bị loại
số record sai schema
số giá trị được impute
số sample bị lọc theo ngôn ngữ
số row cuối cùng
```

Nếu dataset version mới thay đổi lớn, team phải giải thích được vì sao.

## Khả năng Tái tạo

Cleaning nên deterministic và versioned khi có thể. Sửa thủ công trực tiếp trong CSV mà không ghi lại script hoặc transformation phá hỏng lineage và reproducibility.

## Over-Cleaning

Làm sạch quá mức có thể khiến training data trở nên “đẹp” hơn production một cách không thực tế.

Nếu deployment luôn có typo, noise, blur hoặc missing value, việc loại toàn bộ những trường hợp đó khỏi train có thể làm model kém robust hơn.

## Mô hình tư duy

> **Làm sạch dữ liệu không nhằm làm dataset trông đẹp; mục tiêu là làm representation phản ánh trung thực hơn hiện tượng và contract mà mô hình sẽ gặp.**

## Những nhầm lẫn thường gặp

### “Outlier nên bị xóa”

Không. Rare valid case có thể chính là trường hợp quan trọng nhất.

### “Null nghĩa là zero”

Không. Missingness có semantics riêng.

### “Cleaning luôn có thể làm trước khi chia train/test”

Chỉ đúng với transformation hoàn toàn stateless và deterministic. Bất kỳ thống kê học từ dữ liệu nào cũng có thể gây leakage nếu fit trước khi split.

## Liên kết kiến thức

Data cleaning nối ETL, validation, thống kê về missingness và phòng chống leakage.

Xem tiếp: [Gán nhãn Dữ liệu](./03_data_labeling.md).