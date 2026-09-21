# CI/CD/CT cho Hệ thống AI

Trong phần mềm truyền thống, **CI/CD** chủ yếu kiểm tra mã nguồn và triển khai ứng dụng. Hệ thống AI cần thêm kiểm tra cho dữ liệu, artifact mô hình và hành vi. Vì vậy MLOps thường nói tới **CI/CD/CT**: tích hợp liên tục (Continuous Integration), phân phối/triển khai liên tục (Continuous Delivery/Deployment) và huấn luyện liên tục (Continuous Training).

## Tích hợp liên tục

CI cho AI nên kiểm nhiều lớp:

```text
unit test cho mã nguồn
kiểm tra schema / hợp đồng dữ liệu
kiểm tra phép biến đổi đặc trưng
smoke test cho huấn luyện
kiểm tra serialization / load
kiểm tra signature của mô hình
kiểm tra hợp lý của đánh giá
kiểm tra bảo mật / static analysis
```

Một pipeline có thể thất bại dù mã nguồn biên dịch bình thường nếu schema upstream thay đổi hoặc phân phối đặc trưng bất thường.

## Kiểm tra dữ liệu

Ví dụ:

- tỷ lệ null;
- khoảng giá trị;
- vocabulary của category;
- tỷ lệ bản ghi trùng;
- độ mới;
- tính đúng theo thời điểm (point-in-time correctness);
- khả năng sẵn có của nhãn.

Kiểm tra dữ liệu không chứng minh dữ liệu “đúng hoàn toàn”, nhưng giúp chặn nhiều failure phổ biến trước khi huấn luyện.

## Smoke Test cho Huấn luyện

Không cần huấn luyện toàn bộ mô hình trong CI. Có thể chạy trên tập con nhỏ để xác nhận pipeline thực thi end-to-end, loss hữu hạn và artifact có thể được tải lại.

Huấn luyện đầy đủ thường chạy ở một job điều phối riêng.

## Phân phối liên tục và Triển khai liên tục

**Continuous Delivery** đảm bảo ứng viên luôn ở trạng thái có thể triển khai nhưng việc thăng cấp lên production vẫn cần phê duyệt.

**Continuous Deployment** tự động đưa thay đổi đã vượt qua gate vào production.

Với AI có rủi ro cao, delivery kết hợp phê duyệt có kiểm soát thường phù hợp hơn triển khai hoàn toàn tự động.

## Cổng cho Triển khai Mô hình

Ứng viên có thể cần vượt qua:

```text
cổng chất lượng offline
bộ regression test
cổng độ trễ / chi phí
cổng fairness / safety
cổng tương thích
cổng shadow / canary
```

Ngưỡng của gate nên được version hóa và có thể review.

## Huấn luyện liên tục

CT có thể tự động hoặc bán tự động kích hoạt huấn luyện lại khi:

- tới lịch;
- đã có đủ nhãn mới;
- drift vượt ngưỡng;
- mùa vụ kinh doanh thay đổi;
- nguồn dữ liệu được cập nhật.

Nhưng huấn luyện lại không đồng nghĩa tự động thăng cấp.

```text
kích hoạt huấn luyện
→ đánh giá
→ đăng ký ứng viên
→ so sánh với champion
→ phê duyệt / thăng cấp
```

## Trigger Huấn luyện lại và Trigger Triển khai lại

Có thể huấn luyện lại nhưng không triển khai nếu mô hình mới không tốt hơn. Ngược lại có thể triển khai lại cùng mô hình vì hạ tầng hoặc runtime được vá mà không cần huấn luyện lại.

Tách hai khái niệm này làm vòng đời rõ hơn.

## Rollback

Rollback cần khôi phục bộ mô hình, tokenizer/preprocessor, prompt và cấu hình tương thích. Nếu database hoặc index schema đã migrate theo cách không tương thích, chỉ rollback mô hình có thể vẫn thất bại.

## Triển khai Canary

Chỉ chuyển một tỷ lệ traffic tới ứng viên rồi theo dõi chỉ số hệ thống và chỉ số chất lượng/kinh doanh.

Canary cần chú ý thiên lệch lựa chọn (selection bias): tập traffic phải đủ đại diện hoặc kết quả phải được diễn giải đúng.

## Triển khai Shadow

Ứng viên nhận bản sao request nhưng output không ảnh hưởng người dùng. Cách này hữu ích để đo độ trễ và hành vi trên traffic thật.

Shadow có thể gần như nhân đôi chi phí suy luận và vẫn phải tuân thủ kiểm soát quyền riêng tư.

## CI/CD cho LLM

Ứng dụng LLM có thể thay đổi prompt, retrieval, tool hoặc model provider. CI nên có bộ kiểm thử hành vi (behavioral test set) cho:

```text
độ đúng của câu trả lời
mức hỗ trợ của citation
độ tuân thủ JSON / schema
lựa chọn tool
trường hợp từ chối / bảo mật
trường hợp prompt injection
chi phí / độ trễ
```

So sánh chuỗi chính xác thường quá giòn với output sinh nội dung; nên dùng kiểm tra có cấu trúc hoặc đánh giá bằng verifier khi phù hợp.

## Pipeline như Mã nguồn

Pipeline huấn luyện và triển khai nên được version hóa như mã nguồn để có thể review diff, tái lập và rollback.

Cấu hình chỉ tồn tại trong UI thủ công dễ tạo trạng thái ẩn khó truy vết.

## Secret và Môi trường

Log của training hoặc CI không được làm lộ API key, credential hoặc dữ liệu nhạy cảm. Quyền giữa dev, staging và production nên được tách rõ.

## Mô hình tư duy

```text
CI → chứng minh thay đổi nhất quán nội bộ
CT → tạo artifact đã học mới
CD → đưa artifact đã được phê duyệt qua các môi trường một cách an toàn
```

## Những nhầm lẫn thường gặp

### “Continuous Training nghĩa là luôn huấn luyện mô hình mới nhất”

Không. Tần suất huấn luyện phải dựa trên dữ liệu, giá trị và chi phí, không phải chỉ vì có thể tự động hóa.

### “Vượt benchmark offline thì nên tự động triển khai”

Không. Phân phối production và ràng buộc hệ thống có thể khác.

### “CI của LLM chỉ cần kiểm tra cú pháp prompt”

Không. Regression về hành vi, bảo mật và retrieval mới là phần khó.

## Liên kết kiến thức

Xem [Model Registry](./03_model_registry.md), [Monitoring](./06_monitoring_and_observability.md), [Drift](./07_drift_and_retraining.md), [LLMOps](./08_llmops.md).