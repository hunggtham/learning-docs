# Thu thập Dữ liệu

**Thu thập dữ liệu (data collection / 데이터 수집)** là quá trình quyết định cái gì được quan sát, lấy từ đâu, với tần suất nào, theo quyền truy cập nào và bằng cơ chế instrumentation nào. Đây là nơi nhiều dạng thiên lệch bắt đầu xuất hiện từ trước khi mô hình được xây dựng.

## Mục tiêu Thu thập phải xuất phát từ Mục tiêu Quyết định

Không nên thu thập dữ liệu chỉ vì “có thể”. Quy trình hợp lý hơn là bắt đầu từ:

```text
quyết định kinh doanh / khoa học
→ outcome mục tiêu
→ thời điểm cần dự đoán
→ tín hiệu cần thiết
→ cơ chế thu thập
```

Nếu hệ thống phải quyết định gian lận trong 200 ms, một feature chỉ xuất hiện sau 1 ngày không hữu ích cho inference online dù nó có thể rất mạnh trong phân tích offline.

## Các loại Nguồn Dữ liệu

Nguồn dữ liệu có thể đến từ:

- cơ sở dữ liệu giao dịch;
- log của ứng dụng;
- sensor;
- API bên thứ ba;
- nội dung do người dùng tạo;
- khảo sát;
- web hoặc public corpus;
- human annotation;
- dữ liệu tổng hợp hoặc simulation.

Mỗi nguồn có độ tin cậy, độ trễ, phạm vi sử dụng và ràng buộc pháp lý/quyền riêng tư khác nhau.

## Instrumentation

Một event được log nên có ngữ nghĩa rõ ràng, ví dụ:

```text
event_name
entity_id
event_time
properties
producer_version
```

Schema drift hoặc đổi tên event mà không có versioning có thể âm thầm phá hỏng feature pipeline ở downstream.

Instrumentation vì vậy không chỉ là “ghi càng nhiều log càng tốt”, mà là thiết kế một giao diện quan sát ổn định giữa hệ thống production và data pipeline.

## Observation Bias

Ta chỉ thu thập được những gì hệ thống hiện tại cho phép quan sát.

Ví dụ recommendation log chỉ chứa phản ứng của user với các item đã được hiển thị. Những item không bao giờ được show sẽ không có interaction data tương ứng. Đây là một dạng **thiên lệch phơi bày (exposure bias)**.

Nếu không nhận ra điều này, mô hình có thể học rằng “item ít click là item không hấp dẫn”, trong khi nguyên nhân thật chỉ là chúng hiếm khi được hiển thị.

## Chiến lược Sampling

Nếu lưu mọi event quá đắt, sampling phải giữ được những phần distribution quan trọng.

**Lấy mẫu đồng đều (uniform sampling)** đơn giản nhưng có thể làm biến mất các trường hợp hiếm. **Lấy mẫu phân tầng (stratified sampling)** giữ representation tốt hơn cho subgroup hoặc class ít gặp.

Xác suất sampling nên được lưu lại nếu downstream cần reweight hoặc ước lượng lại distribution thật.

## Độ phủ theo Thời gian

Dữ liệu cần bao phủ seasonality và những thay đổi có tính chu kỳ, ví dụ:

- ngày thường và cuối tuần;
- ngày lễ;
- campaign;
- chu kỳ kinh tế;
- thay đổi phiên bản phần mềm.

Mô hình chỉ được train trên một tuần “bình thường” có thể thất bại mạnh trong Black Friday hoặc dịp lễ lớn.

## Hiệu chuẩn Sensor

Dữ liệu từ sensor vật lý phụ thuộc calibration. Sensor drift có thể tạo distribution shift mà mô hình hiểu nhầm là thay đổi thật của thế giới.

Metadata về calibration nên được lưu trong lineage để khi model performance thay đổi có thể phân biệt lỗi do sensor và lỗi do mô hình.

## Consent và Purpose Limitation

Việc thu thập dữ liệu phải phù hợp với consent, legal basis và mục đích sử dụng đã được xác định.

“Đã thu thập được dữ liệu” không đồng nghĩa “được phép dùng dữ liệu đó để train mọi loại model”. Quyền sử dụng phải được đánh giá độc lập với khả năng kỹ thuật.

## Data Minimization

Chỉ nên thu thập lượng dữ liệu nhạy cảm tối thiểu cần thiết cho mục tiêu đã định.

Field dư thừa làm tăng:

- rủi ro bảo mật;
- gánh nặng compliance;
- chi phí lưu trữ;
- khả năng mô hình học shortcut không mong muốn.

## Identifier

Stable identifier giúp group, split và lineage chính xác hơn, nhưng identifier cũng có thể là dữ liệu nhạy cảm.

Hash một ID không tự động biến nó thành dữ liệu ẩn danh. Nếu không gian giá trị nhỏ hoặc có thể liên kết với nguồn khác, việc tái nhận diện vẫn có thể xảy ra.

## Dữ liệu từ Web

Web crawling cần xem xét ít nhất:

- robots và chính sách truy cập;
- license và copyright;
- duplicate mirror;
- mất cân bằng ngôn ngữ;
- spam và SEO content;
- dữ liệu cá nhân;
- độ mới theo thời gian.

Trong nhiều dự án, khâu curation khó và quan trọng hơn bản thân việc crawling.

## Human-Generated Feedback

Rating, click hoặc dwell time đều là **proxy** có nhiễu cho preference thật.

Click có thể chỉ thể hiện tò mò chứ không phải hài lòng. Không click có thể chỉ vì item chưa được nhìn thấy. Trước khi dùng hành vi này làm label, cần hiểu rõ cơ chế tạo hành vi và cơ chế exposure.

## Counterfactual Blindness

System log cho biết outcome của action đã được chọn, nhưng không cho biết điều gì sẽ xảy ra nếu một action khác được thực hiện.

Ví dụ hệ thống phê duyệt một loan rồi quan sát repayment, nhưng không thể quan sát repayment của cùng người dùng nếu loan bị từ chối. Đây là lý do một số bài toán quyết định cần Bandit, Reinforcement Learning hoặc causal method thay vì chỉ supervised prediction.

## Dữ liệu từ Thí nghiệm

Randomized experiment tạo bằng chứng nhân quả mạnh hơn observational data.

Cần log rõ:

```text
đối tượng có đủ điều kiện tham gia hay không
nhánh treatment / control
thời điểm assignment
experiment version
```

Nếu các thông tin này bị mất, dataset sau này rất dễ bị dùng sai ngữ nghĩa.

## Data Contract

Giữa producer và consumer nên có một **hợp đồng dữ liệu (data contract)** mô tả:

```text
schema
định nghĩa ngữ nghĩa
freshness SLA
nullability
đơn vị
owner
quy tắc thay đổi gây breaking change
```

Data pipeline có thể xem như một API giữa các team. Thay đổi schema mà không quản lý compatibility có thể phá hệ thống downstream giống như đổi API contract.

## Dữ liệu đến Muộn

Event có thể tới trễ hoặc không đúng thứ tự. Feature dựa trên event time cần các khái niệm như watermark và window policy.

Nếu bỏ qua late-arriving data, aggregate lịch sử có thể bị bias hoặc thay đổi không nhất quán giữa offline training và online serving.

## Khả dụng của Feature Offline và Online

Một feature có thể rất dễ tính trong data warehouse nhưng không thể đáp ứng latency của online inference.

Thiết kế collection cần phản ánh serving requirement từ đầu. Nếu không, team có thể xây mô hình phụ thuộc vào feature mà production không thể cung cấp đúng lúc.

## Data Retention

Giữ raw data mãi mãi vừa tốn chi phí vừa tăng rủi ro.

Retention nên dựa trên:

- mục đích sử dụng;
- yêu cầu pháp lý;
- nhu cầu reproducibility;
- độ nhạy cảm của dữ liệu.

Trong một số trường hợp, có thể lưu aggregate hoặc derived artifact thay vì giữ raw sensitive source vô thời hạn.

## Chất lượng ngay từ Nguồn

Cách làm sạch tốt nhất thường là ngăn dữ liệu xấu được tạo ra ngay từ đầu.

Ví dụ:

- validation ở UI;
- typed API;
- database constraint;
- sensor health check;
- canonical enum;
- transaction validation.

Những biện pháp này thường hiệu quả hơn việc cố sửa dữ liệu sai ở cuối pipeline.

## Giám sát Quá trình Thu thập

Nên theo dõi ít nhất:

- volume;
- tỷ lệ missing;
- schema change;
- latency;
- duplicate rate;
- category distribution;
- source outage.

Nếu event volume giảm đột ngột 90%, hệ thống cần cảnh báo trước khi dataset đó được dùng cho lần retrain tiếp theo.

## Ví dụ: eKYC

Trong hệ thống xác minh danh tính điện tử (eKYC), dữ liệu có thể gồm ảnh giấy tờ, selfie hoặc video, metadata thiết bị và kết quả decision.

Những vấn đề quan trọng gồm:

- độ đa dạng camera và thiết bị;
- glare, blur và điều kiện ánh sáng;
- coverage theo loại giấy tờ và quốc gia;
- mẫu fraud attack;
- PII và security;
- độ tin cậy của manual-review outcome khi dùng làm label.

Trong production, coverage thực tế thường quan trọng hơn việc chỉ thêm một layer mới vào model.

## Mô hình tư duy

> **Thu thập dữ liệu quyết định cửa sổ mà mô hình dùng để nhìn thế giới. Blind spot trong instrumentation sẽ trở thành blind spot trong quá trình học.**

## Những nhầm lẫn thường gặp

### “Cứ thu thập mọi thứ trước rồi quyết định sau”

Không. Cách này làm tăng rủi ro privacy, cost và semantic ambiguity; nó không phải lựa chọn miễn phí.

### “Log là ground truth khách quan”

Không. Log phản ánh hành vi của phần mềm, policy và exposure của user.

### “Dữ liệu từ bên thứ ba có thể dùng nguyên trạng”

Không. Vẫn cần kiểm tra provenance, license, schema và quality.

## Liên kết kiến thức

Thu thập dữ liệu nối Software Instrumentation, Database, Privacy và Experimental Design.

Xem tiếp: [Làm sạch Dữ liệu](./02_data_cleaning.md).