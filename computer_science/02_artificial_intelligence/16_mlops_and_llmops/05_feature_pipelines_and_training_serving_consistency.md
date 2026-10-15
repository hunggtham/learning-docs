# Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Feature pipelines và training–serving consistency**. Route đi từ feature definition → offline/online materialization → point-in-time correctness → freshness/latency → parity tests, để feature không đổi nghĩa giữa train và serve.

Một mô hình ML có thể chạy đúng trong notebook nhưng sai trong môi trường vận hành (production / 운영 환경) nếu đặc trưng được tính khác nhau giữa huấn luyện và phục vụ. **Sai lệch huấn luyện–phục vụ (training–serving skew / 학습-서빙 불일치)** xảy ra khi biểu diễn lúc huấn luyện không khớp biểu diễn lúc suy luận.

## Chuỗi xử lý (pipeline / 파이프라인) đặc trưng là gì?

Chuỗi xử lý (pipeline / 파이프라인) đặc trưng biến sự kiện thô hoặc bảng dữ liệu thành đầu vào của mô hình:

```text
dữ liệu thô
→ làm sạch / chuẩn hóa
→ join
→ tổng hợp
→ mã hóa
→ kiểm tra
→ vector đặc trưng / tensor
```

Cùng một đặc trưng về mặt ngữ nghĩa phải giữ định nghĩa nhất quán giữa huấn luyện offline và suy luận online.

Định nghĩa đặc trưng chỉ có ý nghĩa khi biết dữ liệu nào được phép xuất hiện tại thời điểm dự đoán. Sau khi xác định ranh giới thời gian đó, ta có thể tách cách materialize đặc trưng cho huấn luyện offline và phục vụ online.

## Tính đúng theo thời điểm

Giả sử đặc trưng `avg_spend_30d` được dùng cho dự đoán tại thời điểm `t`. Dữ liệu huấn luyện chỉ được dùng giao dịch xảy ra trước `t`.

Nếu phép nối (join / 조인) với bảng khách hàng hiện tại có chứa thông tin từ tương lai, rò rỉ dữ liệu xảy ra.

Tính năng (feature / 기능) store hoặc kho dữ liệu không tự động bảo đảm tính đúng theo thời điểm (point-in-time correctness); ngữ nghĩa (semantics / 의미론) của truy vấn mới là yếu tố quyết định.

Ranh giới thời gian giống nhau không buộc hai kho phải có cùng cách lưu trữ; điều quan trọng là chúng dùng chung nghĩa của đặc trưng. Nghĩa đó cần tiếp tục được giữ qua từng phép biến đổi.

## Đặc trưng Offline và Online

Kho offline tối ưu cho phân tích theo lô và huấn luyện. Kho online tối ưu cho tra cứu độ trễ thấp.

Kiến trúc phổ biến:

```text
định nghĩa đặc trưng dùng chung
   ├─ materialization offline → huấn luyện
   └─ materialization online  → phục vụ
```

Mục tiêu là tái sử dụng lô-gic (logic / 논리) và đặc tả hợp đồng (contract / 계약), không nhất thiết dùng cùng một nơi lưu trữ vật lý.

Offline và online chỉ nhất quán nếu các tham số biến đổi, phiên bản và cách xử lý thiếu dữ liệu không âm thầm khác nhau. Nguyên tắc này cũng áp dụng cho tokenizer và các bước tiền xử lý trong mô hình không dùng bảng.

## Tính nhất quán của phép biến đổi

Các phép biến đổi như chuẩn hóa, ánh xạ vocabulary hoặc xử lý giá trị thiếu phải dùng tham số và phiên bản giống lúc huấn luyện.

Ví dụ chuẩn hóa:

\[
z=\frac{x-\mu_{train}}{\sigma_{train}}
\]

Không được tính lại `μ,σ` trên batch live theo một lô-gic (logic / 논리) khác.

Tokenizer và tiền xử lý mở rộng cùng một vấn đề sang văn bản, ảnh và âm thanh: đầu vào chỉ có nghĩa khi phiên bản biến đổi được định danh. Hợp đồng lược đồ giúp ghi lại các giả định đó để dịch vụ gửi dữ liệu đúng.

## Tokenizer và tiền xử lý cũng là chuỗi xử lý (pipeline / 파이프라인) đặc trưng

Trong LLM hoặc Vision, tokenizer, resize ảnh và chuẩn hóa audio đều là chuỗi xử lý (pipeline / 파이프라인) biểu diễn. Sai phiên bản có thể phá mô hình giống như sai lệch đặc trưng ở dữ liệu bảng.

Schema mô tả kiểu dữ liệu nhưng cũng phải ghi rõ đơn vị, thời điểm và chính sách null. Khi một trường không sẵn có trong thời gian chạy, chính sách xử lý thiếu cần được quy định thay vì để từng dịch vụ tự quyết.

## Hợp đồng lược đồ (schema / 스키마)

Lược đồ (schema / 스키마) đầu vào cần mô tả:

```text
tên
kiểu dữ liệu
đơn vị
semantics theo thời gian
có được null không?
category / khoảng giá trị hợp lệ
độ mới
```

Chỉ biết kiểu là `float` chưa đủ nếu một dịch vụ gửi USD còn dịch vụ khác gửi KRW.

Chính sách thiếu dữ liệu cần được kiểm thử ngay trong huấn luyện; nếu không, mô hình có thể chỉ hoạt động ở điều kiện lý tưởng. Một giới hạn khác cũng cần theo dõi là dữ liệu có còn đủ mới so với yêu cầu của từng đặc trưng hay không.

## Xử lý đặc trưng bị thiếu

Tra cứu môi trường vận hành (production / 운영 환경) có thể hết thời gian chờ (timeout / 타임아웃) hoặc thiếu dữ liệu. Chính sách phải tường minh:

- dùng giá trị mặc định;
- dùng nguồn dự phòng;
- từ chối dự đoán;
- dùng mô hình giảm cấp.

Huấn luyện nên mô phỏng tình trạng thiếu dữ liệu thực tế nếu triển khai (deployment / 배포) có thể gặp tình huống đó.

Độ mới là một thuộc tính vận hành chứ không chỉ là trường metadata. Khi định nghĩa hoặc logic thay đổi, việc tạo lại dữ liệu lịch sử phải được quản lý như một phiên bản riêng.

## Độ mới

Mỗi đặc trưng có thể có TTL hoặc yêu cầu độ mới riêng. Hồ sơ người dùng cũ 24 giờ có thể chấp nhận; chỉ số tốc độ gian lận cũ 24 giờ thì không.

Theo dõi độ mới là một phần của độ tin cậy mô hình.

Backfill có thể phục hồi lịch sử nhưng cũng có thể làm lộ dữ liệu tương lai nếu cửa sổ tổng hợp sai. Vì vậy, mỗi phép tổng hợp phải được kiểm tra riêng theo thời điểm dự đoán.

## Backfill

Khi lô-gic (logic / 논리) đặc trưng được sửa, backfill dữ liệu lịch sử cần versioning. Không nên ghi đè âm thầm tập dữ liệu cũ nếu muốn tái lập mô hình đã huấn luyện trước đó.

Ví dụ trên cho thấy một phép tổng hợp đúng cú pháp vẫn có thể sai về thời gian. Sau khi chặn leakage, ta cần đối chiếu trực tiếp giá trị offline và online để phát hiện skew còn lại.

## Rò rỉ qua dữ liệu tổng hợp

Phép tổng hợp có thể vô tình nhìn vào cửa sổ mục tiêu:

```text
dự đoán tại ngày 10
đặc trưng = tổng tháng tính tới ngày 30  ❌
```

Tác vụ theo thời gian cần phép nối (join / 조인) đúng theo thời điểm.

Parity test biến khác biệt giữa train và serve thành tín hiệu có thể quan sát. Feature store hỗ trợ việc tái sử dụng và materialize, nhưng không tự quyết định đặc trưng có đúng nghĩa hay không.

## Kiểm tra tính nhất quán Huấn luyện–Phục vụ

Có thể lấy mẫu từ yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) rồi tính lại đặc trưng bằng chuỗi xử lý (pipeline / 파이프라인) offline để so sánh giá trị. Báo cáo chênh lệch giúp phát hiện skew.

Khi coi feature store là lớp trừu tượng thay vì nguồn chân lý, ta vẫn phải kiểm tra semantics, freshness và lineage ở bên dưới. Với LLM, cùng nguyên tắc đó xuất hiện trong chuỗi lắp ráp ngữ cảnh.

## Tính năng (feature / 기능) Store chỉ là một lớp trừu tượng (abstraction / 추상화)

Tính năng (feature / 기능) store giúp khám phá, tái sử dụng và materialize đặc trưng, nhưng nếu định nghĩa đặc trưng sai thì kết quả vẫn sai. Công cụ không thay thế ngữ nghĩa (semantics / 의미론) của lĩnh vực (domain / 도메인).

Chuỗi context của LLM cho thấy “feature pipeline” không chỉ dành cho dữ liệu bảng: retrieval, reranking và prompt template cũng là các phép biến đổi cần versioning. Từ đó, mô hình tư duy chung trở nên rõ hơn.

## Chuỗi xử lý (pipeline / 파이프라인) Ngữ cảnh của LLM

Ứng dụng LLM có cấu trúc tương tự:

```text
input của người dùng
→ chuẩn hóa
→ truy vấn retrieval
→ chunk được truy xuất
→ reranking
→ đóng gói ngữ cảnh
→ prompt template
```

Nếu huấn luyện hoặc đánh giá dùng cách lắp ráp ngữ cảnh (context / 맥락) khác môi trường vận hành (production / 운영 환경) thì đó cũng là một dạng skew.

Sơ đồ này tóm tắt ranh giới của bài: mô hình chỉ nhận biểu diễn, còn chất lượng biểu diễn phụ thuộc vào hợp đồng giữa các bước tạo ra nó. Các nhầm lẫn sau thường xóa mất ranh giới ấy.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Mô hình nhìn thấy biểu diễn, không nhìn trực tiếp thực tại.
Tính nhất quán của biểu diễn là một hợp đồng production.
```

Các hiểu lầm này đều có chung một nguyên nhân: nhìn vào tên công cụ hoặc tên cột thay vì nhìn vào thời điểm, đơn vị và chuỗi biến đổi. Các liên kết dưới đây đưa nguyên tắc đó sang leakage, training và inference pipeline.

## Những nhầm lẫn thường gặp

### “Cùng tên cột nghĩa là cùng một đặc trưng”

Không. ngữ nghĩa (semantics / 의미론), cửa sổ thời gian hoặc đơn vị có thể khác.

### “tính năng (feature / 기능) store loại bỏ leakage”

Không nếu truy vấn point-in-time được viết sai.

### “LLM không có tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링)”

Không đúng. Tokenizer, retrieval và quá trình lắp ráp prompt/ngữ cảnh (context / 맥락) chính là kỹ thuật biểu diễn (representation engineering).


## Liên kết kiến thức

Xem [Data Leakage](../14_data_for_ai/05_data_leakage.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md), [Inference Pipeline](../15_ai_engineering/02_inference_pipeline.md), [Monitoring](./06_monitoring_and_observability.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
