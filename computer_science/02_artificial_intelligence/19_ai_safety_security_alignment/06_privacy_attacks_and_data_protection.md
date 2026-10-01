# Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến thức cần có trước** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bề mặt rủi ro quyền riêng tư** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Hệ thống AI có thể xử lý hoặc học từ dữ liệu nhạy cảm trong nhiều giai đoạn: thu thập, huấn luyện, suy luận, truy xuất, logging và lưu trữ lâu dài. Vì vậy **bảo mật quyền riêng tư (privacy engineering / 프라이버시 엔지니어링)** không chỉ là “ẩn tên trong cơ sở dữ liệu (database / 데이터베이스)”, mà là kiểm soát dòng chảy thông tin xuyên suốt toàn bộ vòng đời của hệ thống.

## Kiến thức cần có trước

Nên đọc [Data Governance](../14_data_for_ai/08_data_governance.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [RAG](../09_retrieval_and_rag/README.md), [Agent Memory](../10_agents_and_ai_systems/04_agent_memory.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Bề mặt rủi ro quyền riêng tư** tiếp nhận điểm tựa từ **Kiến thức cần có trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memorization và exposure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Một hệ thống có thể mã hóa cơ sở dữ liệu (database / 데이터베이스) rất tốt nhưng vẫn làm lộ dữ liệu qua gỡ lỗi (debug / 디버그) log, ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시) hoặc dấu vết (trace / 추적) của tác nhân (agent / 에이전트).

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Memorization và exposure** tiếp nhận điểm tựa từ **Bề mặt rủi ro quyền riêng tư** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Membership suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memorization và exposure

Mô hình có sức chứa (capacity / 용량) lớn có thể ghi nhớ các chuỗi hiếm hoặc lặp lại nhiều lần trong dữ liệu huấn luyện. **Ghi nhớ (memorization)** không đồng nghĩa dữ liệu chắc chắn sẽ được sinh lại, nhưng nó làm tăng khả năng exposure trong một số điều kiện.

Các yếu tố làm tăng rủi ro gồm:

- mẫu xuất hiện nhiều lần;
- chuỗi rất hiếm hoặc duy nhất;
- overfitting;
- mô hình (model / 모델) sức chứa (capacity / 용량) cao;
- dữ liệu bí mật xuất hiện ở format dễ học.

Deduplication và dữ liệu (data / 데이터) minimization giúp giảm rủi ro nhưng không tạo bảo đảm tuyệt đối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Membership suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Memorization và exposure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) inversion và reconstruction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Membership suy luận (inference / 추론)

**Suy luận thành viên (membership inference)** hỏi liệu một bản ghi (record / 레코드) cụ thể có từng nằm trong huấn luyện (training / 학습) set hay không. Nếu mô hình (model / 모델) phản ứng khác đáng kể giữa mẫu đã thấy và chưa thấy, attacker có thể dùng sự khác biệt đó làm tín hiệu.

Overfitting, confidence quá chi tiết hoặc API trả quá nhiều thông tin có thể làm rủi ro tăng.

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Mô hình (model / 모델) inversion và reconstruction** tiếp nhận điểm tựa từ **Membership suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Training-data extraction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) inversion và reconstruction

Trong **mô hình (model / 모델) inversion**, attacker cố tái dựng thuộc tính hoặc đầu vào (input / 입력) đại diện từ đầu ra (output / 출력), độ dốc (gradient / 기울기) hoặc embedding. Mức độ khả thi phụ thuộc threat mô hình (model / 모델) và loại dữ liệu.

Điểm môi trường vận hành (production / 운영 환경) quan trọng là: embedding, độ dốc (gradient / 기울기) và intermediate biểu diễn (representation / 표현) cũng là dữ liệu có thể mang thông tin nhạy cảm, không chỉ raw bản ghi (record / 레코드).

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Training-data extraction** tiếp nhận điểm tựa từ **Mô hình (model / 모델) inversion và reconstruction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác Differential Privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Training-data extraction

Generative mô hình (model / 모델) đôi khi có thể tái tạo đoạn dữ liệu đã ghi nhớ. Vì vậy bảo mật (security / 보안) evaluation nên có canary hoặc kiểm thử (test / 테스트) mẫu (pattern / 패턴) đại diện cho dữ liệu nhạy cảm và kiểm tra khả năng mô hình lặp lại chúng.

Không nên xem mô hình (model / 모델) weights như “cơ sở dữ liệu (database / 데이터베이스) đã được anonymize”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Trực giác Differential Privacy** tiếp nhận điểm tựa từ **Training-data extraction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DP-SGD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác Differential Privacy

**Quyền riêng tư vi sai (Differential Privacy — DP / 차등 개인정보 보호)** đưa ra một giới hạn toán học về mức độ ảnh hưởng của một cá nhân lên đầu ra (output / 출력).

Một cơ chế ngẫu nhiên `M` được gọi gần đúng là `(ε,δ)`-DP nếu với hai dataset lân cận `D` và `D'` chỉ khác một bản ghi (record / 레코드):

\[
P(M(D)\in S)
\le e^\epsilon P(M(D')\in S)+\delta
\]

`ε` nhỏ hơn thường tương ứng với privacy mạnh hơn nhưng thường làm utility giảm hoặc cần thêm dữ liệu/compute.

Điểm cốt lõi: DP không phải “ẩn danh hóa bằng noise một lần”, mà là một cơ chế có ngân sách (budget / 예산) và composition rõ ràng.

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **DP-SGD** tiếp nhận điểm tựa từ **Trực giác Differential Privacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Privacy ngân sách (budget / 예산) và composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP-SGD

Một dạng huấn luyện (training / 학습) riêng tư thường dùng:

```text
1. tính gradient theo từng sample hoặc microbatch
2. clip gradient để giới hạn ảnh hưởng tối đa
3. cộng noise
4. theo dõi privacy budget
```

Sự đánh đổi (trade-off / 트레이드오프) chính là chất lượng (quality / 품질), compute và privacy ngân sách (budget / 예산). Với mô hình (model / 모델) rất lớn, chi phí có thể đáng kể.

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Privacy ngân sách (budget / 예산) và composition** tiếp nhận điểm tựa từ **DP-SGD** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Federated học tập (learning / 학습) không tự động riêng tư** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Privacy ngân sách (budget / 예산) và composition

Nhiều lần truy vấn hoặc huấn luyện có thể cộng dồn rủi ro. Vì vậy cần accounting thay vì chỉ nhìn một giá trị noise cố định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Federated học tập (learning / 학습) không tự động riêng tư** tiếp nhận điểm tựa từ **Privacy ngân sách (budget / 예산) và composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Secure aggregation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Federated học tập (learning / 학습) không tự động riêng tư

**Học liên kết (federated learning)** giữ raw dữ liệu (data / 데이터) ở thiết bị hoặc site, nhưng cập nhật (update / 업데이트) mô hình vẫn có thể làm lộ thông tin. Có thể cần thêm secure aggregation, DP hoặc giới hạn siêu dữ liệu (metadata / 메타데이터).

Federated học tập (learning / 학습) giải bài toán vị trí dữ liệu; nó không tự động giải toàn bộ privacy bài toán (problem / 문제).

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Secure aggregation** tiếp nhận điểm tựa từ **Federated học tập (learning / 학습) không tự động riêng tư** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Embedding không phải dữ liệu vô danh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Secure aggregation

**Tổng hợp an toàn (secure aggregation)** cho phép máy chủ (server / 서버) nhận giá trị tổng hợp từ nhiều máy khách (client / 클라이언트) mà không nhất thiết thấy từng cập nhật (update / 업데이트) riêng lẻ. Đây là một lớp bảo vệ hữu ích nhưng không bao phủ toàn bộ siêu dữ liệu (metadata / 메타데이터), endpoint compromise hoặc model-output leakage.

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Secure aggregation** nêu điều cần giải thích; **Embedding không phải dữ liệu vô danh** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quyền riêng tư trong RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Embedding không phải dữ liệu vô danh

Embedding có thể chứa thông tin về ngữ nghĩa, thuộc tính và đôi khi cho phép linking hoặc reconstruction. véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) cần được bảo vệ như một datastore nhạy cảm:

```text
ACL / tenant filter
encryption
retention
index lifecycle
access audit
cache isolation
```

Không nên dùng lý do “véc-tơ (vector / 벡터) không đọc được bằng mắt” để coi embedding là anonymous.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Embedding không phải dữ liệu vô danh** nêu điều cần giải thích; **Quyền riêng tư trong RAG** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quyền riêng tư trong tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Không được retrieve tài liệu trái quyền rồi yêu cầu LLM “đừng tiết lộ”. Khi tài liệu đã vào ngữ cảnh (context / 맥락), ranh giới bảo mật (security boundary / 보안 경계) đã bị phá.

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Quyền riêng tư trong tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Quyền riêng tư trong RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ đệm (cache / 캐시) và cross-tenant leakage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyền riêng tư trong tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)

Persistent bộ nhớ (memory / 메모리) là một datastore thật sự. Nó cần:

- người dùng (user / 사용자)/tenant phạm vi (scope / 범위);
- ghi (write / 쓰기) chính sách (policy / 정책);
- correction ngữ nghĩa (semantics / 의미론);
- TTL/retention;
- delete propagation;
- provenance;
- kiểm tra (audit / 감사).

Bộ nhớ (memory / 메모리) không nên trở thành prompt log tồn tại vĩnh viễn.

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Bộ nhớ đệm (cache / 캐시) và cross-tenant leakage** tiếp nhận điểm tựa từ **Quyền riêng tư trong tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logs và traces** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm (cache / 캐시) và cross-tenant leakage

Ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시), prompt bộ nhớ đệm (cache / 캐시) hoặc phản hồi (response / 응답) bộ nhớ đệm (cache / 캐시) có thể làm lộ dữ liệu nếu key không bao gồm tenant/bảo mật (security / 보안) ngữ cảnh (context / 맥락). bộ nhớ đệm (cache / 캐시) hit không được phép bỏ qua authorization.

Môi trường vận hành (production / 운영 환경) bộ nhớ đệm (cache / 캐시) key thường cần phụ thuộc vào:

```text
user/tenant scope
model version
prompt version
retrieval/index version
policy version
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Logs và traces** tiếp nhận điểm tựa từ **Bộ nhớ đệm (cache / 캐시) và cross-tenant leakage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) minimization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logs và traces

Khả năng quan sát (observability / 관측 가능성) dễ trở thành “shadow dữ liệu (data / 데이터) lake”. Cần áp dụng:

```text
redaction
sampling
field-level access control
encryption
retention limit
audit log
```

Không nên ghi raw secret, credential hoặc sensitive prompt theo mặc định.

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Logs và traces** nêu điều cần giải thích; **Dữ liệu (data / 데이터) minimization** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Purpose limitation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) minimization

Ít dữ liệu hơn thường giảm cả privacy rủi ro (risk / 위험) lẫn đơn vị từ (token / 토큰)/compute chi phí (cost / 비용). Chỉ nên thu thập và đưa vào ngữ cảnh (context / 맥락) phần dữ liệu thật sự cần cho tác vụ (task / 작업).

“ngữ cảnh (context / 맥락) càng nhiều càng tốt” là anti-pattern nếu ngữ cảnh (context / 맥락) chứa thông tin không cần thiết hoặc vượt mục đích đã được chấp thuận.

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Dữ liệu (data / 데이터) minimization** đã nêu tiêu chí phân biệt, còn **Purpose limitation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Xóa dữ liệu và mô hình (model / 모델) unlearning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Purpose limitation

Dữ liệu được thu thập cho mục đích A không tự động hợp lệ cho việc huấn luyện (training / 학습) mục đích B. quản trị (governance / 거버넌스) cần ghi rõ purpose, nguồn (source / 소스), retention và quyền sử dụng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Purpose limitation** đã nêu tiêu chí phân biệt, còn **Xóa dữ liệu và mô hình (model / 모델) unlearning** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Encryption và confidential computing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xóa dữ liệu và mô hình (model / 모델) unlearning

Xóa raw bản ghi (record / 레코드) khỏi cơ sở dữ liệu (database / 데이터베이스) không tự động xóa ảnh hưởng đã học trong weights.

**mô hình (model / 모델) unlearning** nghiên cứu cách loại bỏ ảnh hưởng đó mà không retrain toàn bộ. Tuy nhiên với hệ thống lớn, bảo đảm mạnh và kiểm chứng vẫn khó. Trong một số trường hợp, retrain từ clean snapshot vẫn là phương án chắc chắn hơn.

Delete yêu cầu (request / 요청) cũng phải lan tới:

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

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Xóa dữ liệu và mô hình (model / 모델) unlearning** nêu điều cần giải thích; **Encryption và confidential computing** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encryption và confidential computing

Encryption at rest và in transit là baseline. Trusted thực thi (execution / 실행) môi trường (environment / 환경) hoặc homomorphic techniques có thể bảo vệ computation trong một số threat mô hình (model / 모델) nhưng đổi lại bằng độ phức tạp (complexity / 복잡도) và hiệu năng (performance / 성능) chi phí (cost / 비용).

Các kỹ thuật này không thay thế authorization và dữ liệu (data / 데이터) minimization.

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Encryption và confidential computing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai môi trường vận hành (production / 운영 환경)

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

Nếu một stage không cần raw sensitive giá trị (value / 값), không nên truyền nó qua stage đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Đánh giá privacy** tiếp nhận điểm tựa từ **Mô hình triển khai môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đánh giá privacy

Evaluation nên bao gồm:

- kiểm tra extraction/canary;
- cross-tenant retrieval kiểm thử (test / 테스트);
- bộ nhớ đệm (cache / 캐시) isolation;
- log/dấu vết (trace / 추적) leakage;
- deletion propagation;
- membership/inversion rủi ro (risk / 위험) theo threat mô hình (model / 모델);
- secret scanning;
- permission regression.

Privacy kiểm thử (test / 테스트) phải trở thành bản phát hành (release / 릴리스) gate cho những workflow có dữ liệu nhạy cảm.

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Đánh giá privacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프)

Privacy điều khiển (control / 제어) thường tạo sự đánh đổi (trade-off / 트레이드오프) với utility, khả năng quan sát (observability / 관측 가능성) và tốc độ phát triển. Redaction quá mạnh có thể làm debugging khó; retention quá ngắn có thể làm sự cố (incident / 인시던트) investigation khó; DP mạnh có thể giảm mô hình (model / 모델) chất lượng (quality / 품질).

Thiết kế đúng không phải “privacy tối đa bất kể chi phí (cost / 비용)”, mà là xác định threat mô hình (model / 모델), legal/chính sách (policy / 정책) ràng buộc (constraint / 제약조건) và mức dữ liệu tối thiểu cần thiết cho tác vụ (task / 작업).

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Dạng thất bại (failure mode / 실패 모드) thường gặp** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) thường gặp

**Cross-tenant véc-tơ (vector / 벡터) tìm kiếm (search / 검색).** siêu dữ liệu (metadata / 메타데이터) filter bị bỏ qua hoặc bộ nhớ đệm (cache / 캐시) dùng chung phạm vi (scope / 범위).

**Log chứa secret.** Debugging tiện nhưng tạo datastore nhạy cảm mới.

**Delete không lan xuống downstream.** Raw bản ghi (record / 레코드) biến mất nhưng chỉ mục (index / 인덱스)/bộ nhớ (memory / 메모리)/bộ nhớ đệm (cache / 캐시) vẫn còn.

**Embedding bị coi là anonymous.** Dẫn đến quyền truy cập lỏng hơn raw dữ liệu (data / 데이터).

**Provider ranh giới (boundary / 경계) không rõ.** Không biết prompt được giữ bao lâu hoặc có được tái sử dụng không.

**tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리) không có đơn vị sở hữu (owner / 오너)/TTL.** Dữ liệu cá nhân tích lũy vô hạn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Mô hình tư duy** gom các mảnh từ **Dạng thất bại (failure mode / 실패 모드) thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Privacy trong AI là kiểm soát thông tin (information / 정보) luồng (flow / 흐름) xuyên suốt vòng đời, không chỉ xóa định danh khỏi dataset.**

Mỗi bản sao, embedding, bộ nhớ đệm (cache / 캐시), dấu vết (trace / 추적) và mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물) đều có thể trở thành một phần của privacy surface.

> **Chuyển mạch:** Trong **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Embedding không đọc được nên anonymous”

Không. Embedding có thể giữ thông tin nhạy cảm và cần kiểm soát truy cập (access control / 접근 제어).

### “Federated học tập (learning / 학습) nghĩa là privacy đã được giải quyết”

Không. cập nhật (update / 업데이트) và siêu dữ liệu (metadata / 메타데이터) vẫn có thể rò rỉ.

### “Xóa bản ghi (record / 레코드) khỏi cơ sở dữ liệu (database / 데이터베이스) là xóa khỏi mô hình (model / 모델)”

Không. Ảnh hưởng đã học có thể còn trong weights và các sản phẩm tạo ra (artifact / 산출물) downstream.

### “Mã hóa dữ liệu là đủ”

Không. người dùng (user / 사용자) có quyền hợp lệ vẫn có thể truy cập quá mức nếu authorization hoặc purpose limitation sai.

> **Chuyển mạch:** Ở chặng này của **Bảo mật quyền riêng tư và bảo vệ dữ liệu trong AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Nên đọc cùng [Data Governance](../14_data_for_ai/08_data_governance.md), [LLMOps](../16_mlops_and_llmops/08_llmops.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Secure AI System Design](./08_secure_ai_system_design.md), [RAG](../09_retrieval_and_rag/README.md) và [Agent Memory](../10_agents_and_ai_systems/04_agent_memory.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
