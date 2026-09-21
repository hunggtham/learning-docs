# Inference Pipeline

**Pipeline suy luận (inference pipeline / 추론 파이프라인)** biến một yêu cầu production thành input phù hợp với mô hình, thực thi mô hình, sau đó biến raw output thành quyết định hoặc phản hồi có thể sử dụng. Độ đúng phụ thuộc toàn bộ đường đi, không chỉ forward pass.

```text
request
→ kiểm tra
→ lấy feature / context
→ tiền xử lý / tokenize
→ model inference
→ decode / hậu xử lý
→ policy / validation
→ response
```

## Tính nhất quán giữa Training và Serving

Cùng một phép biến đổi về mặt semantics nên được dùng online giống như khi training. Các dạng skew phổ biến gồm:

- normalization constant khác nhau;
- category mapping không khớp;
- tokenizer version khác;
- timezone hoặc window khác;
- quy tắc resize/crop ảnh khác.

Nên dùng chung library/artifact hoặc sinh transform từ một specification duy nhất.

## Kiểm tra Request

Trước khi đưa dữ liệu vào mô hình cần kiểm tra:

- schema và type;
- field bắt buộc;
- giới hạn kích thước;
- enum hợp lệ;
- authentication;
- các ràng buộc nội dung.

Nên reject request sai càng sớm càng tốt thay vì để tensor/runtime phát sinh lỗi khó hiểu ở phía sau.

## Truy xuất Feature

Feature online cần đúng theo thời điểm, đủ mới và có độ trễ thấp. Feature service có thể lấy dữ liệu từ cache, KV store hoặc database.

Khi timeout, hệ thống phải định nghĩa rõ sẽ:

- fail;
- dùng giá trị mặc định;
- dùng stale cache;
- route sang fallback model.

Giá trị mặc định có thể làm chất lượng giảm âm thầm, vì vậy cần log rõ khi fallback xảy ra.

## Tiền xử lý

Các tác vụ thường gồm:

```text
chuẩn hóa giá trị số
mã hóa category
tokenize text
resize / normalize image
resample audio
tạo tensor đầu vào cho model
```

Với mô hình nhẹ, preprocessing latency đôi khi còn lớn hơn thời gian chạy model.

## Dynamic Shape

Sequence hoặc image có kích thước khác nhau làm batching và memory khó tối ưu. Padding tất cả về item lớn nhất gây lãng phí compute.

Có thể nhóm request theo length/shape để tăng hiệu quả.

## Suy luận sinh nội dung

LLM inference thường có hai giai đoạn:

1. **prefill**: xử lý input/context và tạo KV cache;
2. **decode**: sinh token theo kiểu autoregressive, từng bước một.

Prompt dài làm prefill đắt hơn; output dài làm decode đắt hơn.

## Decoding

Các tham số thường gặp:

- greedy;
- temperature;
- top-k;
- top-p;
- beam search;
- stop sequence;
- max token.

Chúng là một phần của hành vi sản phẩm, vì vậy cần được version hóa và theo dõi.

## Structured Output

Nếu downstream cần JSON hoặc function call, output phải được kiểm theo schema. Constrained decoding có thể giảm lỗi cú pháp nhưng không thay thế semantic validation.

## Hậu xử lý

Ví dụ:

- classification threshold;
- NMS cho object detection;
- detokenization;
- confidence calibration;
- business rule;
- redaction;
- unit conversion.

Hậu xử lý là một phần của hợp đồng giữa mô hình và hệ thống, không phải bước trang trí.

## Ngân sách Timeout

Có thể chia deadline end-to-end như:

```text
feature 30 ms
model 100 ms
postprocess 10 ms
network margin 20 ms
```

Nếu model dùng hết toàn bộ deadline, downstream không còn khoảng trống để phục hồi hoặc fallback.

## Retry

Retry inference thường an toàn khi chỉ đọc, nhưng request lặp lại vẫn tiêu tốn capacity và có thể khuếch đại outage. Chỉ nên retry lỗi transient, kèm deadline và backoff.

Với Agent hoặc tool có side effect, retry cần idempotency.

## Admission Control

Khi hệ thống quá tải, nên từ chối hoặc trì hoãn request ưu tiên thấp thay vì cho queue dài vô hạn. Tail latency thường quan trọng hơn average latency.

## Streaming Output

LLM hoặc TTS có thể stream output từng phần. Streaming cải thiện cảm nhận **time-to-first-output**, nhưng làm moderation và rollback khó hơn vì người dùng đã thấy token trước khi toàn bộ phản hồi được validate.

Guardrail cần được thiết kế phù hợp với đặc điểm này.

## Cancellation

Nếu người dùng ngắt kết nối, nên dừng generation để giải phóng GPU nếu runtime hỗ trợ. Nếu không, hệ thống vẫn tiếp tục sinh token không ai sử dụng.

## Pipeline nhiều mô hình

Ví dụ RAG:

```text
embed query
→ retrieve
→ rerank
→ generate
→ cite / validate
```

Latency end-to-end là tổng hoặc kết quả kết hợp của nhiều stage. Cần tối ưu toàn bộ graph thay vì chỉ một mô hình.

## Cascade

Có thể dùng mô hình rẻ trước, chỉ gọi mô hình đắt cho case khó:

```text
small classifier
→ nếu confidence cao: kết thúc
→ nếu không: route sang large model
```

Cascade có thể giảm cost trung bình nếu routing đủ đáng tin.

## Batching

Scheduler online có thể gom nhiều request thành batch GPU để tăng throughput. Nhưng chờ đủ batch lại làm latency tăng. Dynamic hoặc continuous batching giúp cân bằng hai mục tiêu này.

## KV Cache

Autoregressive Transformer lưu key/value tensor của token trước đó để không phải tính lại toàn bộ history ở mỗi token output.

Memory xấp xỉ tăng theo:

```text
batch × sequence length × layers × hidden/head dimensions
```

Trong LLM serving, KV cache thường giới hạn concurrency mạnh hơn bản thân weights.

## Prefix Caching

Nếu nhiều request dùng chung system prefix hoặc document dài giống nhau, có thể cache kết quả prefill/KV để giảm compute, với điều kiện prefix và model config phải khớp chính xác và dữ liệu được cô lập đúng theo privacy scope.

## Kiểm tra Output

Với ứng dụng rủi ro cao:

```text
model output
→ deterministic rule
→ external verification
→ human review khi cần
```

Không nên cho generative output trực tiếp thay đổi critical system mà không qua validation.

## Logging

Nên ghi lại một cách an toàn:

- model/config version;
- latency theo từng thành phần;
- input shape hoặc token count;
- output length;
- error và fallback;
- quality feedback.

Không nên log raw secret hoặc PII theo mặc định.

## Mô hình tư duy

> **Inference pipeline là một graph biến đổi có deadline latency, trong đó semantics phải khớp với training và mọi failure mode quan trọng phải được định nghĩa rõ.**

## Những nhầm lẫn thường gặp

### “Inference latency chính là thời gian forward của model”

Không. Feature fetch, tokenization, queue, network và postprocess đều đóng góp latency.

### “Streaming làm model chạy nhanh hơn”

Không nhất thiết. Streaming chủ yếu làm người dùng thấy output sớm hơn; tổng compute có thể không đổi.

### “Retry luôn làm reliability tốt hơn”

Không. Khi hệ thống quá tải, retry storm có thể khiến outage nặng hơn.

## Liên kết kiến thức

Inference pipeline dẫn trực tiếp tới kiến trúc serving và trade-off giữa batch với online inference.

Xem tiếp: [Model Serving](./03_model_serving.md).