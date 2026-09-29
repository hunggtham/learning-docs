# Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ

> **Mạch đọc:** Đặt **chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **chuỗi xử lý (pipeline / 파이프라인) đặc trưng là gì?** sang **Tính đúng theo thời điểm**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Tính đúng theo thời điểm

Giả sử đặc trưng `avg_spend_30d` được dùng cho dự đoán tại thời điểm `t`. Dữ liệu huấn luyện chỉ được dùng giao dịch xảy ra trước `t`.

Nếu phép nối (join / 조인) với bảng khách hàng hiện tại có chứa thông tin từ tương lai, rò rỉ dữ liệu xảy ra.

Tính năng (feature / 기능) store hoặc kho dữ liệu không tự động bảo đảm tính đúng theo thời điểm (point-in-time correctness); ngữ nghĩa (semantics / 의미론) của truy vấn mới là yếu tố quyết định.

## Đặc trưng Offline và Online

Kho offline tối ưu cho phân tích theo lô và huấn luyện. Kho online tối ưu cho tra cứu độ trễ thấp.

Kiến trúc phổ biến:

```text
định nghĩa đặc trưng dùng chung
   ├─ materialization offline → huấn luyện
   └─ materialization online  → phục vụ
```

Mục tiêu là tái sử dụng lô-gic (logic / 논리) và đặc tả hợp đồng (contract / 계약), không nhất thiết dùng cùng một nơi lưu trữ vật lý.

## Tính nhất quán của phép biến đổi

Các phép biến đổi như chuẩn hóa, ánh xạ vocabulary hoặc xử lý giá trị thiếu phải dùng tham số và phiên bản giống lúc huấn luyện.

Ví dụ chuẩn hóa:

\[
z=\frac{x-\mu_{train}}{\sigma_{train}}
\]

Không được tính lại `μ,σ` trên batch live theo một lô-gic (logic / 논리) khác.

## Tokenizer và tiền xử lý cũng là chuỗi xử lý (pipeline / 파이프라인) đặc trưng

Trong LLM hoặc Vision, tokenizer, resize ảnh và chuẩn hóa audio đều là chuỗi xử lý (pipeline / 파이프라인) biểu diễn. Sai phiên bản có thể phá mô hình giống như sai lệch đặc trưng ở dữ liệu bảng.

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

## Xử lý đặc trưng bị thiếu

Tra cứu môi trường vận hành (production / 운영 환경) có thể hết thời gian chờ (timeout / 타임아웃) hoặc thiếu dữ liệu. Chính sách phải tường minh:

- dùng giá trị mặc định;
- dùng nguồn dự phòng;
- từ chối dự đoán;
- dùng mô hình giảm cấp.

Huấn luyện nên mô phỏng tình trạng thiếu dữ liệu thực tế nếu triển khai (deployment / 배포) có thể gặp tình huống đó.

## Độ mới

Mỗi đặc trưng có thể có TTL hoặc yêu cầu độ mới riêng. Hồ sơ người dùng cũ 24 giờ có thể chấp nhận; chỉ số tốc độ gian lận cũ 24 giờ thì không.

Theo dõi độ mới là một phần của độ tin cậy mô hình.

## Backfill

Khi lô-gic (logic / 논리) đặc trưng được sửa, backfill dữ liệu lịch sử cần versioning. Không nên ghi đè âm thầm tập dữ liệu cũ nếu muốn tái lập mô hình đã huấn luyện trước đó.

## Rò rỉ qua dữ liệu tổng hợp

Phép tổng hợp có thể vô tình nhìn vào cửa sổ mục tiêu:

```text
dự đoán tại ngày 10
đặc trưng = tổng tháng tính tới ngày 30  ❌
```

Tác vụ theo thời gian cần phép nối (join / 조인) đúng theo thời điểm.

## Kiểm tra tính nhất quán Huấn luyện–Phục vụ

Có thể lấy mẫu từ yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) rồi tính lại đặc trưng bằng chuỗi xử lý (pipeline / 파이프라인) offline để so sánh giá trị. Báo cáo chênh lệch giúp phát hiện skew.

## Tính năng (feature / 기능) Store chỉ là một lớp trừu tượng (abstraction / 추상화)

Tính năng (feature / 기능) store giúp khám phá, tái sử dụng và materialize đặc trưng, nhưng nếu định nghĩa đặc trưng sai thì kết quả vẫn sai. Công cụ không thay thế ngữ nghĩa (semantics / 의미론) của lĩnh vực (domain / 도메인).

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

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Mô hình nhìn thấy biểu diễn, không nhìn trực tiếp thực tại.
Tính nhất quán của biểu diễn là một hợp đồng production.
```

## Những nhầm lẫn thường gặp

### “Cùng tên cột nghĩa là cùng một đặc trưng”

Không. ngữ nghĩa (semantics / 의미론), cửa sổ thời gian hoặc đơn vị có thể khác.

### “tính năng (feature / 기능) store loại bỏ leakage”

Không nếu truy vấn point-in-time được viết sai.

### “LLM không có tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링)”

Không đúng. Tokenizer, retrieval và quá trình lắp ráp prompt/ngữ cảnh (context / 맥락) chính là kỹ thuật biểu diễn (representation engineering).

## Liên kết kiến thức

Xem [Data Leakage](../14_data_for_ai/05_data_leakage.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md), [Inference Pipeline](../15_ai_engineering/02_inference_pipeline.md), [Monitoring](./06_monitoring_and_observability.md).
