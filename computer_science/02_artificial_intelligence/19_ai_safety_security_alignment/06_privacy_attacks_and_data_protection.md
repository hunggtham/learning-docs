# Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI

Hệ thống AI có thể xử lý hoặc học từ dữ liệu nhạy cảm trong nhiều giai đoạn: thu thập, huấn luyện, suy luận, truy xuất, logging và lưu trữ lâu dài. Vì vậy **bảo mật quyền riêng tư (privacy engineering / 프라이버시 엔지니어링)** không chỉ là “ẩn tên trong database”, mà là kiểm soát dòng chảy thông tin xuyên suốt toàn bộ vòng đời của hệ thống.

## Kiến thức cần có trước

Nên đọc [Data Governance](../14_data_for_ai/08_data_governance.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [RAG](../09_retrieval_and_rag/README.md), [Agent Memory](../10_agents_and_ai_systems/04_agent_memory.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

## Bề mặt rủi ro quyền riêng tư

Dữ liệu nhạy cảm có thể xuất hiện ở nhiều nơi:

```text
raw dataset
feature store
training snapshot
checkpoint
embedding / vector database
prompt và conversation
retrieved documents
tool output
agent memory
logs / traces
model output
backup
```

Một hệ thống có thể mã hóa database rất tốt nhưng vẫn làm lộ dữ liệu qua debug log, semantic cache hoặc trace của agent.

## Memorization và exposure

Mô hình có capacity lớn có thể ghi nhớ các chuỗi hiếm hoặc lặp lại nhiều lần trong dữ liệu huấn luyện. **Ghi nhớ (memorization)** không đồng nghĩa dữ liệu chắc chắn sẽ được sinh lại, nhưng nó làm tăng khả năng exposure trong một số điều kiện.

Các yếu tố làm tăng rủi ro gồm:

- mẫu xuất hiện nhiều lần;
- chuỗi rất hiếm hoặc duy nhất;
- overfitting;
- model capacity cao;
- dữ liệu bí mật xuất hiện ở format dễ học.

Deduplication và data minimization giúp giảm rủi ro nhưng không tạo bảo đảm tuyệt đối.

## Membership inference

**Suy luận thành viên (membership inference)** hỏi liệu một record cụ thể có từng nằm trong training set hay không. Nếu model phản ứng khác đáng kể giữa mẫu đã thấy và chưa thấy, attacker có thể dùng sự khác biệt đó làm tín hiệu.

Overfitting, confidence quá chi tiết hoặc API trả quá nhiều thông tin có thể làm rủi ro tăng.

## Model inversion và reconstruction

Trong **model inversion**, attacker cố tái dựng thuộc tính hoặc input đại diện từ output, gradient hoặc embedding. Mức độ khả thi phụ thuộc threat model và loại dữ liệu.

Điểm production quan trọng là: embedding, gradient và intermediate representation cũng là dữ liệu có thể mang thông tin nhạy cảm, không chỉ raw record.

## Training-data extraction

Generative model đôi khi có thể tái tạo đoạn dữ liệu đã ghi nhớ. Vì vậy security evaluation nên có canary hoặc test pattern đại diện cho dữ liệu nhạy cảm và kiểm tra khả năng mô hình lặp lại chúng.

Không nên xem model weights như “database đã được anonymize”.

## Trực giác Differential Privacy

**Quyền riêng tư vi sai (Differential Privacy — DP / 차등 개인정보 보호)** đưa ra một giới hạn toán học về mức độ ảnh hưởng của một cá nhân lên output.

Một cơ chế ngẫu nhiên `M` được gọi gần đúng là `(ε,δ)`-DP nếu với hai dataset lân cận `D` và `D'` chỉ khác một record:

\[
P(M(D)\in S)
\le e^\epsilon P(M(D')\in S)+\delta
\]

`ε` nhỏ hơn thường tương ứng với privacy mạnh hơn nhưng thường làm utility giảm hoặc cần thêm dữ liệu/compute.

Điểm cốt lõi: DP không phải “ẩn danh hóa bằng noise một lần”, mà là một cơ chế có budget và composition rõ ràng.

## DP-SGD

Một dạng training riêng tư thường dùng:

```text
1. tính gradient theo từng sample hoặc microbatch
2. clip gradient để giới hạn ảnh hưởng tối đa
3. cộng noise
4. theo dõi privacy budget
```

Trade-off chính là quality, compute và privacy budget. Với model rất lớn, chi phí có thể đáng kể.

## Privacy budget và composition

Nhiều lần truy vấn hoặc huấn luyện có thể cộng dồn rủi ro. Vì vậy cần accounting thay vì chỉ nhìn một giá trị noise cố định.

## Federated Learning không tự động riêng tư

**Học liên kết (federated learning)** giữ raw data ở thiết bị hoặc site, nhưng update mô hình vẫn có thể làm lộ thông tin. Có thể cần thêm secure aggregation, DP hoặc giới hạn metadata.

Federated learning giải bài toán vị trí dữ liệu; nó không tự động giải toàn bộ privacy problem.

## Secure aggregation

**Tổng hợp an toàn (secure aggregation)** cho phép server nhận giá trị tổng hợp từ nhiều client mà không nhất thiết thấy từng update riêng lẻ. Đây là một lớp bảo vệ hữu ích nhưng không bao phủ toàn bộ metadata, endpoint compromise hoặc model-output leakage.

## Embedding không phải dữ liệu vô danh

Embedding có thể chứa thông tin về ngữ nghĩa, thuộc tính và đôi khi cho phép linking hoặc reconstruction. Vector database cần được bảo vệ như một datastore nhạy cảm:

```text
ACL / tenant filter
encryption
retention
index lifecycle
access audit
cache isolation
```

Không nên dùng lý do “vector không đọc được bằng mắt” để coi embedding là anonymous.

## Quyền riêng tư trong RAG

Authorization phải xảy ra **trước hoặc trong retrieval**:

```text
user identity
→ tenant / ACL filter
→ retrieval
→ reranking
→ context
→ LLM
```

Không được retrieve tài liệu trái quyền rồi yêu cầu LLM “đừng tiết lộ”. Khi tài liệu đã vào context, security boundary đã bị phá.

## Quyền riêng tư trong Agent Memory

Persistent memory là một datastore thật sự. Nó cần:

- user/tenant scope;
- write policy;
- correction semantics;
- TTL/retention;
- delete propagation;
- provenance;
- audit.

Memory không nên trở thành prompt log tồn tại vĩnh viễn.

## Cache và cross-tenant leakage

Semantic cache, prompt cache hoặc response cache có thể làm lộ dữ liệu nếu key không bao gồm tenant/security context. Cache hit không được phép bỏ qua authorization.

Production cache key thường cần phụ thuộc vào:

```text
user/tenant scope
model version
prompt version
retrieval/index version
policy version
```

## Logs và traces

Observability dễ trở thành “shadow data lake”. Cần áp dụng:

```text
redaction
sampling
field-level access control
encryption
retention limit
audit log
```

Không nên ghi raw secret, credential hoặc sensitive prompt theo mặc định.

## Data minimization

Ít dữ liệu hơn thường giảm cả privacy risk lẫn token/compute cost. Chỉ nên thu thập và đưa vào context phần dữ liệu thật sự cần cho task.

“Context càng nhiều càng tốt” là anti-pattern nếu context chứa thông tin không cần thiết hoặc vượt mục đích đã được chấp thuận.

## Purpose limitation

Dữ liệu được thu thập cho mục đích A không tự động hợp lệ cho việc training mục đích B. Governance cần ghi rõ purpose, source, retention và quyền sử dụng.

## Xóa dữ liệu và model unlearning

Xóa raw record khỏi database không tự động xóa ảnh hưởng đã học trong weights.

**Model unlearning** nghiên cứu cách loại bỏ ảnh hưởng đó mà không retrain toàn bộ. Tuy nhiên với hệ thống lớn, bảo đảm mạnh và kiểm chứng vẫn khó. Trong một số trường hợp, retrain từ clean snapshot vẫn là phương án chắc chắn hơn.

Delete request cũng phải lan tới:

```text
raw store
feature store
vector index
agent memory
cache
logs
training snapshot nếu policy yêu cầu
backup lifecycle
```

## Encryption và confidential computing

Encryption at rest và in transit là baseline. Trusted execution environment hoặc homomorphic techniques có thể bảo vệ computation trong một số threat model nhưng đổi lại bằng complexity và performance cost.

Các kỹ thuật này không thay thế authorization và data minimization.

## Mô hình triển khai production

Một luồng xử lý dữ liệu nhạy cảm nên có dạng:

```text
request
→ xác thực
→ phân quyền
→ data minimization
→ xử lý / retrieval
→ model
→ output validation / redaction
→ response
→ privacy-aware logging
→ retention lifecycle
```

Nếu một stage không cần raw sensitive value, không nên truyền nó qua stage đó.

## Đánh giá privacy

Evaluation nên bao gồm:

- kiểm tra extraction/canary;
- cross-tenant retrieval test;
- cache isolation;
- log/trace leakage;
- deletion propagation;
- membership/inversion risk theo threat model;
- secret scanning;
- permission regression.

Privacy test phải trở thành release gate cho những workflow có dữ liệu nhạy cảm.

## Trade-off

Privacy control thường tạo trade-off với utility, observability và tốc độ phát triển. Redaction quá mạnh có thể làm debugging khó; retention quá ngắn có thể làm incident investigation khó; DP mạnh có thể giảm model quality.

Thiết kế đúng không phải “privacy tối đa bất kể cost”, mà là xác định threat model, legal/policy constraint và mức dữ liệu tối thiểu cần thiết cho task.

## Failure mode thường gặp

**Cross-tenant vector search.** Metadata filter bị bỏ qua hoặc cache dùng chung scope.

**Log chứa secret.** Debugging tiện nhưng tạo datastore nhạy cảm mới.

**Delete không lan xuống downstream.** Raw record biến mất nhưng index/memory/cache vẫn còn.

**Embedding bị coi là anonymous.** Dẫn đến quyền truy cập lỏng hơn raw data.

**Provider boundary không rõ.** Không biết prompt được giữ bao lâu hoặc có được tái sử dụng không.

**Agent memory không có owner/TTL.** Dữ liệu cá nhân tích lũy vô hạn.

## Mô hình tư duy

> **Privacy trong AI là kiểm soát information flow xuyên suốt vòng đời, không chỉ xóa định danh khỏi dataset.**

Mỗi bản sao, embedding, cache, trace và model artifact đều có thể trở thành một phần của privacy surface.

## Những nhầm lẫn thường gặp

### “Embedding không đọc được nên anonymous”

Không. Embedding có thể giữ thông tin nhạy cảm và cần access control.

### “Federated learning nghĩa là privacy đã được giải quyết”

Không. Update và metadata vẫn có thể rò rỉ.

### “Xóa record khỏi database là xóa khỏi model”

Không. Ảnh hưởng đã học có thể còn trong weights và các artifact downstream.

### “Mã hóa dữ liệu là đủ”

Không. User có quyền hợp lệ vẫn có thể truy cập quá mức nếu authorization hoặc purpose limitation sai.

## Liên kết kiến thức

Nên đọc cùng [Data Governance](../14_data_for_ai/08_data_governance.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Secure AI System Design](./08_secure_ai_system_design.md), [RAG](../09_retrieval_and_rag/README.md) và [Agent Memory](../10_agents_and_ai_systems/04_agent_memory.md).