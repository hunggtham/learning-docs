# Pipeline Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ

Một mô hình ML có thể chạy đúng trong notebook nhưng sai trong production nếu đặc trưng được tính khác nhau giữa huấn luyện và phục vụ. **Sai lệch huấn luyện–phục vụ (training–serving skew / 학습-서빙 불일치)** xảy ra khi biểu diễn lúc huấn luyện không khớp biểu diễn lúc suy luận.

## Pipeline đặc trưng là gì?

Pipeline đặc trưng biến sự kiện thô hoặc bảng dữ liệu thành đầu vào của mô hình:

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

## Tính đúng theo thời điểm

Giả sử đặc trưng `avg_spend_30d` được dùng cho dự đoán tại thời điểm `t`. Dữ liệu huấn luyện chỉ được dùng giao dịch xảy ra trước `t`.

Nếu join với bảng khách hàng hiện tại có chứa thông tin từ tương lai, rò rỉ dữ liệu xảy ra.

Feature store hoặc kho dữ liệu không tự động bảo đảm tính đúng theo thời điểm (point-in-time correctness); semantics của truy vấn mới là yếu tố quyết định.

## Đặc trưng Offline và Online

Kho offline tối ưu cho phân tích theo lô và huấn luyện. Kho online tối ưu cho tra cứu độ trễ thấp.

Kiến trúc phổ biến:

```text
định nghĩa đặc trưng dùng chung
   ├─ materialization offline → huấn luyện
   └─ materialization online  → phục vụ
```

Mục tiêu là tái sử dụng logic và contract, không nhất thiết dùng cùng một nơi lưu trữ vật lý.

## Tính nhất quán của phép biến đổi

Các phép biến đổi như chuẩn hóa, ánh xạ vocabulary hoặc xử lý giá trị thiếu phải dùng tham số và phiên bản giống lúc huấn luyện.

Ví dụ chuẩn hóa:

\[
z=\frac{x-\mu_{train}}{\sigma_{train}}
\]

Không được tính lại `μ,σ` trên batch live theo một logic khác.

## Tokenizer và tiền xử lý cũng là Pipeline đặc trưng

Trong LLM hoặc Vision, tokenizer, resize ảnh và chuẩn hóa audio đều là pipeline biểu diễn. Sai phiên bản có thể phá mô hình giống như sai lệch đặc trưng ở dữ liệu bảng.

## Hợp đồng Schema

Schema đầu vào cần mô tả:

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

## Xử lý đặc trưng bị thiếu

Tra cứu production có thể timeout hoặc thiếu dữ liệu. Chính sách phải tường minh:

- dùng giá trị mặc định;
- dùng nguồn dự phòng;
- từ chối dự đoán;
- dùng mô hình giảm cấp.

Huấn luyện nên mô phỏng tình trạng thiếu dữ liệu thực tế nếu deployment có thể gặp tình huống đó.

## Độ mới

Mỗi đặc trưng có thể có TTL hoặc yêu cầu độ mới riêng. Hồ sơ người dùng cũ 24 giờ có thể chấp nhận; chỉ số tốc độ gian lận cũ 24 giờ thì không.

Theo dõi độ mới là một phần của độ tin cậy mô hình.

## Backfill

Khi logic đặc trưng được sửa, backfill dữ liệu lịch sử cần versioning. Không nên ghi đè âm thầm tập dữ liệu cũ nếu muốn tái lập mô hình đã huấn luyện trước đó.

## Rò rỉ qua dữ liệu tổng hợp

Phép tổng hợp có thể vô tình nhìn vào cửa sổ mục tiêu:

```text
dự đoán tại ngày 10
đặc trưng = tổng tháng tính tới ngày 30  ❌
```

Tác vụ theo thời gian cần join đúng theo thời điểm.

## Kiểm tra tính nhất quán Huấn luyện–Phục vụ

Có thể lấy mẫu từ request production rồi tính lại đặc trưng bằng pipeline offline để so sánh giá trị. Báo cáo chênh lệch giúp phát hiện skew.

## Feature Store chỉ là một Abstraction

Feature store giúp khám phá, tái sử dụng và materialize đặc trưng, nhưng nếu định nghĩa đặc trưng sai thì kết quả vẫn sai. Công cụ không thay thế semantics của domain.

## Pipeline Ngữ cảnh của LLM

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

Nếu huấn luyện hoặc đánh giá dùng cách lắp ráp context khác production thì đó cũng là một dạng skew.

## Mô hình tư duy

```text
Mô hình nhìn thấy biểu diễn, không nhìn trực tiếp thực tại.
Tính nhất quán của biểu diễn là một hợp đồng production.
```

## Những nhầm lẫn thường gặp

### “Cùng tên cột nghĩa là cùng một đặc trưng”

Không. Semantics, cửa sổ thời gian hoặc đơn vị có thể khác.

### “Feature store loại bỏ leakage”

Không nếu truy vấn point-in-time được viết sai.

### “LLM không có feature engineering”

Không đúng. Tokenizer, retrieval và quá trình lắp ráp prompt/context chính là kỹ thuật biểu diễn (representation engineering).

## Liên kết kiến thức

Xem [Data Leakage](../14_data_for_ai/05_data_leakage.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md), [Inference Pipeline](../15_ai_engineering/02_inference_pipeline.md), [Monitoring](./06_monitoring_and_observability.md).