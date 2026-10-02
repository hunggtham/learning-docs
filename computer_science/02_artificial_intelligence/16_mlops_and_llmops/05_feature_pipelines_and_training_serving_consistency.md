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

> **Chuyển mạch:** Trong **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Chuỗi xử lý (pipeline / 파이프라인) đặc trưng là gì?** xác định đầu vào; **Tính đúng theo thời điểm** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Đặc trưng Offline và Online** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đúng theo thời điểm

Giả sử đặc trưng `avg_spend_30d` được dùng cho dự đoán tại thời điểm `t`. Dữ liệu huấn luyện chỉ được dùng giao dịch xảy ra trước `t`.

Nếu phép nối (join / 조인) với bảng khách hàng hiện tại có chứa thông tin từ tương lai, rò rỉ dữ liệu xảy ra.

Tính năng (feature / 기능) store hoặc kho dữ liệu không tự động bảo đảm tính đúng theo thời điểm (point-in-time correctness); ngữ nghĩa (semantics / 의미론) của truy vấn mới là yếu tố quyết định.

> **Chuyển mạch:** Ở chặng này của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Đặc trưng Offline và Online** tiếp nhận điểm tựa từ **Tính đúng theo thời điểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính nhất quán của phép biến đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đặc trưng Offline và Online

Kho offline tối ưu cho phân tích theo lô và huấn luyện. Kho online tối ưu cho tra cứu độ trễ thấp.

Kiến trúc phổ biến:

```text
định nghĩa đặc trưng dùng chung
   ├─ materialization offline → huấn luyện
   └─ materialization online  → phục vụ
```

Mục tiêu là tái sử dụng lô-gic (logic / 논리) và đặc tả hợp đồng (contract / 계약), không nhất thiết dùng cùng một nơi lưu trữ vật lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Tính nhất quán của phép biến đổi** tiếp nhận điểm tựa từ **Đặc trưng Offline và Online** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tokenizer và tiền xử lý cũng là chuỗi xử lý (pipeline / 파이프라인) đặc trưng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính nhất quán của phép biến đổi

Các phép biến đổi như chuẩn hóa, ánh xạ vocabulary hoặc xử lý giá trị thiếu phải dùng tham số và phiên bản giống lúc huấn luyện.

Ví dụ chuẩn hóa:

\[
z=\frac{x-\mu_{train}}{\sigma_{train}}
\]

Không được tính lại `μ,σ` trên batch live theo một lô-gic (logic / 논리) khác.

> **Chuyển mạch:** Trong **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Tính nhất quán của phép biến đổi** xác định đầu vào; **Tokenizer và tiền xử lý cũng là chuỗi xử lý (pipeline / 파이프라인) đặc trưng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Hợp đồng lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tokenizer và tiền xử lý cũng là chuỗi xử lý (pipeline / 파이프라인) đặc trưng

Trong LLM hoặc Vision, tokenizer, resize ảnh và chuẩn hóa audio đều là chuỗi xử lý (pipeline / 파이프라인) biểu diễn. Sai phiên bản có thể phá mô hình giống như sai lệch đặc trưng ở dữ liệu bảng.

> **Chuyển mạch:** Ở chặng này của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Tokenizer và tiền xử lý cũng là chuỗi xử lý (pipeline / 파이프라인) đặc trưng** xác định đầu vào; **Hợp đồng lược đồ (schema / 스키마)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Xử lý đặc trưng bị thiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Xử lý đặc trưng bị thiếu** tiếp nhận điểm tựa từ **Hợp đồng lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xử lý đặc trưng bị thiếu

Tra cứu môi trường vận hành (production / 운영 환경) có thể hết thời gian chờ (timeout / 타임아웃) hoặc thiếu dữ liệu. Chính sách phải tường minh:

- dùng giá trị mặc định;
- dùng nguồn dự phòng;
- từ chối dự đoán;
- dùng mô hình giảm cấp.

Huấn luyện nên mô phỏng tình trạng thiếu dữ liệu thực tế nếu triển khai (deployment / 배포) có thể gặp tình huống đó.

> **Chuyển mạch:** Trong **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Độ mới** tiếp nhận điểm tựa từ **Xử lý đặc trưng bị thiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backfill** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ mới

Mỗi đặc trưng có thể có TTL hoặc yêu cầu độ mới riêng. Hồ sơ người dùng cũ 24 giờ có thể chấp nhận; chỉ số tốc độ gian lận cũ 24 giờ thì không.

Theo dõi độ mới là một phần của độ tin cậy mô hình.

> **Chuyển mạch:** Ở chặng này của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Backfill** tiếp nhận điểm tựa từ **Độ mới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rò rỉ qua dữ liệu tổng hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backfill

Khi lô-gic (logic / 논리) đặc trưng được sửa, backfill dữ liệu lịch sử cần versioning. Không nên ghi đè âm thầm tập dữ liệu cũ nếu muốn tái lập mô hình đã huấn luyện trước đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Backfill** nêu điều cần giải thích; **Rò rỉ qua dữ liệu tổng hợp** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kiểm tra tính nhất quán Huấn luyện–Phục vụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rò rỉ qua dữ liệu tổng hợp

Phép tổng hợp có thể vô tình nhìn vào cửa sổ mục tiêu:

```text
dự đoán tại ngày 10
đặc trưng = tổng tháng tính tới ngày 30  ❌
```

Tác vụ theo thời gian cần phép nối (join / 조인) đúng theo thời điểm.

> **Chuyển mạch:** Trong **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Rò rỉ qua dữ liệu tổng hợp** nêu điều cần giải thích; **Kiểm tra tính nhất quán Huấn luyện–Phục vụ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tính năng (feature / 기능) Store chỉ là một lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểm tra tính nhất quán Huấn luyện–Phục vụ

Có thể lấy mẫu từ yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) rồi tính lại đặc trưng bằng chuỗi xử lý (pipeline / 파이프라인) offline để so sánh giá trị. Báo cáo chênh lệch giúp phát hiện skew.

> **Chuyển mạch:** Ở chặng này của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Tính năng (feature / 기능) Store chỉ là một lớp trừu tượng (abstraction / 추상화)** tiếp nhận điểm tựa từ **Kiểm tra tính nhất quán Huấn luyện–Phục vụ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi xử lý (pipeline / 파이프라인) Ngữ cảnh của LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) Store chỉ là một lớp trừu tượng (abstraction / 추상화)

Tính năng (feature / 기능) store giúp khám phá, tái sử dụng và materialize đặc trưng, nhưng nếu định nghĩa đặc trưng sai thì kết quả vẫn sai. Công cụ không thay thế ngữ nghĩa (semantics / 의미론) của lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Tính năng (feature / 기능) Store chỉ là một lớp trừu tượng (abstraction / 추상화)** xác định đầu vào; **Chuỗi xử lý (pipeline / 파이프라인) Ngữ cảnh của LLM** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Mô hình tư duy** gom các mảnh từ **Chuỗi xử lý (pipeline / 파이프라인) Ngữ cảnh của LLM** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Mô hình nhìn thấy biểu diễn, không nhìn trực tiếp thực tại.
Tính nhất quán của biểu diễn là một hợp đồng production.
```

> **Chuyển mạch:** Ở chặng này của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Cùng tên cột nghĩa là cùng một đặc trưng”

Không. ngữ nghĩa (semantics / 의미론), cửa sổ thời gian hoặc đơn vị có thể khác.

### “tính năng (feature / 기능) store loại bỏ leakage”

Không nếu truy vấn point-in-time được viết sai.

### “LLM không có tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링)”

Không đúng. Tokenizer, retrieval và quá trình lắp ráp prompt/ngữ cảnh (context / 맥락) chính là kỹ thuật biểu diễn (representation engineering).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chuỗi xử lý (pipeline / 파이프라인) Đặc trưng và Tính nhất quán giữa Huấn luyện–Phục vụ**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Data Leakage](../14_data_for_ai/05_data_leakage.md), [Training Pipeline](../15_ai_engineering/01_training_pipeline.md), [Inference Pipeline](../15_ai_engineering/02_inference_pipeline.md), [Monitoring](./06_monitoring_and_observability.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
