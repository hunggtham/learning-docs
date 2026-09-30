# Ứng phó Sự cố và Vòng đời môi trường vận hành (production / 운영 환경) AI

> **Mạch đọc:** Đặt **Ứng phó Sự cố và Vòng đời môi trường vận hành (production / 운영 환경) AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Sự cố không chỉ là dịch vụ (service / 서비스) Down** sang **Mức độ nghiêm trọng**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hệ thống AI cuối cùng vẫn là hệ thống môi trường vận hành (production / 운영 환경) và sẽ có sự cố: độ trễ tăng đột biến, sai phiên bản mô hình, dữ liệu xấu, bùng phát hallucination, retrieval outage, hành động công cụ (tool / 도구) không an toàn, rò rỉ dữ liệu hoặc chi phí tăng mất kiểm soát. **Ứng phó sự cố (incident response / 사고 대응)** biến những thất bại (failure / 실패) này thành một quy trình có containment, chẩn đoán, phục hồi và học hỏi.

## Sự cố không chỉ là dịch vụ (service / 서비스) Down

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

Một regression nhỏ ở tính năng (feature / 기능) ít rủi ro khác hoàn toàn một hành động thanh toán không được phép.

## Vòng đời Sự cố

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Khi thất bại (failure / 실패) có tác động cao, ưu tiên giảm harm trước khi hiểu đầy đủ nguyên nhân gốc.

Các hành động có thể gồm:

- vô hiệu hóa công cụ (tool / 도구) hoặc hành động (action / 동작);
- quay lui (rollback / 롤백) mô hình, prompt hoặc chỉ mục (index / 인덱스);
- tuyến (route / 경로) sang fallback xác định;
- bắt buộc human approval;
- giảm traffic;
- thu hồi credential bị compromise.

## Khả năng tái lập Sự cố

Cần dấu vết (trace / 추적) siêu dữ liệu (metadata / 메타데이터) như:

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

Không có dấu vết (trace / 추적) theo phiên bản, việc gỡ lỗi (debug / 디버그) rất dễ biến thành đoán mò.

## Kill Switch

Tác nhân (agent / 에이전트) hoặc tích hợp công cụ (tool / 도구) rủi ro cao nên có cơ chế vô hiệu hóa hành động (action / 동작) nhanh mà không cần redeploy toàn bộ ngăn xếp (stack / 스택).

Kill switch chi tiết hữu ích hơn việc shutdown cả dịch vụ.

## Quay lui (rollback / 롤백)

Mục tiêu quay lui (rollback / 롤백) phải là một **gói hành vi đã biết là tốt (known-good behavior bundle)**, không chỉ tệp (file / 파일) trọng số trước đó.

Sự cố RAG có thể cần quay lui (rollback / 롤백) chỉ mục (index / 인덱스) hoặc chunking. Sự cố do prompt LLM có thể cần quay lui (rollback / 롤백) cả cặp prompt/mô hình (model / 모델).

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

## Sự cố của tác nhân (agent / 에이전트)

Thất bại (failure / 실패) của tác nhân (agent / 에이전트) có trajectory dài. Cần tái dựng chuyển trạng thái và side tác động (effect / 효과).

Các cơ chế quan trọng gồm:

- idempotency;
- log hành động;
- checkpoint phê duyệt;
- vòng lặp (loop / 루프) có giới hạn;
- thao tác bù hoặc hoàn tác khi có thể.

## Sự cố Chi phí

Ví dụ:

- bộ nhớ đệm (cache / 캐시) bị tắt;
- tác nhân (agent / 에이전트) thử lại (retry / 재시도) vô hạn;
- độ dài ngữ cảnh (context / 맥락) tăng đột ngột;
- routing đưa mọi yêu cầu (request / 요청) sang mô hình lớn nhất.

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

Trigger có thể là “provider hết thời gian chờ (timeout / 타임아웃)”, nhưng nguyên nhân gốc có thể là “thử lại (retry / 재시도) không giới hạn + không có fallback + hàng đợi (queue / 큐) saturation”.

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

“Nhắc nhóm cẩn thận hơn” là một điều khiển (control / 제어) yếu.

## Quản lý Vòng đời

Mô hình hoặc ứng dụng môi trường vận hành (production / 운영 환경) có các giai đoạn:

```text
phát triển
kiểm định
staging
production
bảo trì
ngừng sử dụng
```

Mỗi giai đoạn nên có đơn vị sở hữu (owner / 오너) và tiêu chí kết thúc rõ.

## Deprecation

Phiên bản mô hình (model / 모델)/API/prompt cũ cần chính sách deprecation. máy khách (client / 클라이언트) tồn tại lâu có thể vẫn gọi lược đồ (schema / 스키마) cũ.

Không nên xóa sản phẩm tạo ra (artifact / 산출물) trước khi yêu cầu retention hoặc kiểm tra (audit / 감사) đã được đáp ứng.

## Quyền sở hữu (ownership / 소유권)

Mỗi năng lực (capability / 역량) AI môi trường vận hành (production / 운영 환경) nên có đơn vị sở hữu (owner / 오너) và đường on-call rõ. Nếu sự cố xảy ra mà không biết nhóm nào chịu trách nhiệm thì mức trưởng thành của nền tảng (platform / 플랫폼) còn thấp.

## Runbook

Runbook chứa hành động cụ thể cho những thất bại (failure / 실패) đã biết:

```text
retrieval index cũ → kiểm tra build → đổi alias → rebuild
model latency tăng → kiểm tra queue/GPU → scale/fallback
tool output không an toàn → disable tool → kiểm tra trace → rotate credential nếu cần
```

Runbook giúp giảm tải nhận thức khi sự cố đang diễn ra.

## Game Day và Diễn tập thất bại (failure / 실패)

Có thể mô phỏng mô hình (model / 모델) endpoint thất bại (failure / 실패), chỉ mục (index / 인덱스) outage hoặc bad triển khai (deployment / 배포) để xác nhận fallback thực sự hoạt động.

Fallback chưa từng được kiểm thử thường chỉ tồn tại trên sơ đồ.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Độ tin cậy không phải “không bao giờ fail”.
Độ tin cậy là phát hiện → giới hạn ảnh hưởng → phục hồi → học hỏi.
```

## Những nhầm lẫn thường gặp

### “quay lui (rollback / 롤백) mô hình (model / 모델) là đủ”

Không. thất bại (failure / 실패) có thể nằm ở dữ liệu, prompt, chỉ mục (index / 인덱스), công cụ (tool / 도구) hoặc hạ tầng (infrastructure / 인프라).

### “chất lượng (quality / 품질) sự cố (incident / 인시던트) không cần on-call”

Không đúng. Quyết định sai âm thầm có tác động cao có thể nghiêm trọng hơn downtime.

### “Postmortem là tìm người gây lỗi”

Không. Mục tiêu là cải thiện điều khiển (control / 제어) của hệ thống và khả năng học hỏi của tổ chức.

## Liên kết kiến thức

Xem [Monitoring](./06_monitoring_and_observability.md), [LLMOps](./08_llmops.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [Safety/Security](../19_ai_safety_security_alignment/README.md).
