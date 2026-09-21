# Ứng phó Sự cố và Vòng đời Production AI

Hệ thống AI cuối cùng vẫn là hệ thống production và sẽ có sự cố: độ trễ tăng đột biến, sai phiên bản mô hình, dữ liệu xấu, bùng phát hallucination, retrieval outage, hành động tool không an toàn, rò rỉ dữ liệu hoặc chi phí tăng mất kiểm soát. **Ứng phó sự cố (incident response / 사고 대응)** biến những failure này thành một quy trình có containment, chẩn đoán, phục hồi và học hỏi.

## Sự cố không chỉ là Service Down

Sự cố AI có thể là:

```text
lỗi availability
suy giảm chất lượng
distribution shift âm thầm
sự kiện bảo mật / prompt injection
rò rỉ quyền riêng tư
rollout sai model / config
retrieval bị hỏng
agent loop / chi phí chạy mất kiểm soát
side effect không an toàn
```

Nhiều sự cố vẫn trả HTTP 200 nên giám sát uptime truyền thống là chưa đủ.

## Mức độ nghiêm trọng

Mức độ nghiêm trọng nên dựa trên tác động:

- số người dùng hoặc giao dịch bị ảnh hưởng;
- rủi ro tài chính/pháp lý;
- khả năng hoàn tác;
- mức độ lộ dữ liệu;
- thời lượng;
- hệ quả an toàn.

Một regression nhỏ ở feature ít rủi ro khác hoàn toàn một hành động thanh toán không được phép.

## Vòng đời Sự cố

```text
phát hiện
→ phân loại ban đầu
→ giới hạn ảnh hưởng
→ giảm thiểu / phục hồi
→ xác minh
→ truyền thông
→ phân tích nguyên nhân gốc
→ hành động khắc phục
```

## Ưu tiên Giới hạn ảnh hưởng trước

Khi failure có tác động cao, ưu tiên giảm harm trước khi hiểu đầy đủ nguyên nhân gốc.

Các hành động có thể gồm:

- vô hiệu hóa tool hoặc action;
- rollback mô hình, prompt hoặc index;
- route sang fallback xác định;
- bắt buộc human approval;
- giảm traffic;
- thu hồi credential bị compromise.

## Khả năng tái lập Sự cố

Cần trace metadata như:

```text
request ID
mô hình / phiên bản
phiên bản prompt / config
phiên bản retrieval / index
tool call
hash của input/output hoặc nội dung đã redact
độ trễ / chi phí
quyết định policy
```

Không có trace theo phiên bản, việc debug rất dễ biến thành đoán mò.

## Kill Switch

Agent hoặc tích hợp tool rủi ro cao nên có cơ chế vô hiệu hóa action nhanh mà không cần redeploy toàn bộ stack.

Kill switch chi tiết hữu ích hơn việc shutdown cả dịch vụ.

## Rollback

Mục tiêu rollback phải là một **gói hành vi đã biết là tốt (known-good behavior bundle)**, không chỉ file trọng số trước đó.

Sự cố RAG có thể cần rollback index hoặc chunking. Sự cố do prompt LLM có thể cần rollback cả cặp prompt/model.

## Sự cố từ Dữ liệu

Dữ liệu upstream xấu có thể làm hỏng huấn luyện hoặc suy luận trực tiếp. Phản ứng có thể là:

```text
đóng băng pipeline
cách ly partition
khôi phục snapshot trước
vô hiệu hóa feature
chỉ huấn luyện lại sau khi validation đạt
```

Không nên tự động huấn luyện lại trên dữ liệu bị lỗi.

## Sự cố của Agent

Failure của agent có trajectory dài. Cần tái dựng chuyển trạng thái và side effect.

Các cơ chế quan trọng gồm:

- idempotency;
- log hành động;
- checkpoint phê duyệt;
- loop có giới hạn;
- thao tác bù hoặc hoàn tác khi có thể.

## Sự cố Chi phí

Ví dụ:

- cache bị tắt;
- agent retry vô hạn;
- độ dài context tăng đột ngột;
- routing đưa mọi request sang mô hình lớn nhất.

Giám sát chi phí cần cảnh báo theo tốc độ tiêu thụ, không nên chờ tới hóa đơn cuối tháng.

## Postmortem

Postmortem tốt tập trung vào nguyên nhân hệ thống thay vì đổ lỗi cá nhân.

Cấu trúc có thể gồm:

```text
mức tác động
timeline
lỗ hổng phát hiện
nguyên nhân gốc
yếu tố góp phần
điều gì hoạt động tốt
điều gì thất bại
action item + owner + deadline
```

## Nguyên nhân gốc và Trigger

Trigger có thể là “provider timeout”, nhưng nguyên nhân gốc có thể là “retry không giới hạn + không có fallback + queue saturation”.

Chỉ sửa trigger mà không sửa điểm yếu hệ thống sẽ không cải thiện khả năng phục hồi.

## Phân cấp Hành động Khắc phục

Biện pháp mạnh thường nằm ở tầng hệ thống:

```text
thêm validation
làm trạng thái bất hợp lệ khó biểu diễn
thêm ranh giới permission
thêm regression test tự động
thêm rollback / kill switch
cải thiện monitoring
```

“Nhắc nhóm cẩn thận hơn” là một control yếu.

## Quản lý Vòng đời

Mô hình hoặc ứng dụng production có các giai đoạn:

```text
phát triển
kiểm định
staging
production
bảo trì
ngừng sử dụng
```

Mỗi giai đoạn nên có owner và tiêu chí kết thúc rõ.

## Deprecation

Phiên bản model/API/prompt cũ cần chính sách deprecation. Client tồn tại lâu có thể vẫn gọi schema cũ.

Không nên xóa artifact trước khi yêu cầu retention hoặc audit đã được đáp ứng.

## Ownership

Mỗi capability AI production nên có owner và đường on-call rõ. Nếu sự cố xảy ra mà không biết nhóm nào chịu trách nhiệm thì mức trưởng thành của platform còn thấp.

## Runbook

Runbook chứa hành động cụ thể cho những failure đã biết:

```text
retrieval index cũ → kiểm tra build → đổi alias → rebuild
model latency tăng → kiểm tra queue/GPU → scale/fallback
tool output không an toàn → disable tool → kiểm tra trace → rotate credential nếu cần
```

Runbook giúp giảm tải nhận thức khi sự cố đang diễn ra.

## Game Day và Diễn tập Failure

Có thể mô phỏng model endpoint failure, index outage hoặc bad deployment để xác nhận fallback thực sự hoạt động.

Fallback chưa từng được kiểm thử thường chỉ tồn tại trên sơ đồ.

## Mô hình tư duy

```text
Độ tin cậy không phải “không bao giờ fail”.
Độ tin cậy là phát hiện → giới hạn ảnh hưởng → phục hồi → học hỏi.
```

## Những nhầm lẫn thường gặp

### “Rollback model là đủ”

Không. Failure có thể nằm ở dữ liệu, prompt, index, tool hoặc infrastructure.

### “Quality incident không cần on-call”

Không đúng. Quyết định sai âm thầm có tác động cao có thể nghiêm trọng hơn downtime.

### “Postmortem là tìm người gây lỗi”

Không. Mục tiêu là cải thiện control của hệ thống và khả năng học hỏi của tổ chức.

## Liên kết kiến thức

Xem [Monitoring](./06_monitoring_and_observability.md), [LLMOps](./08_llmops.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [Safety/Security](../19_ai_safety_security_alignment/README.md).