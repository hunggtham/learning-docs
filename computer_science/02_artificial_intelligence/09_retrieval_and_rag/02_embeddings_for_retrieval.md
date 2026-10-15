# Embeddings for Retrieval

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Embeddings for retrieval**. Route đi từ text/query encoding → embedding space → contrastive or dual-encoder training → hard negatives → recall and domain transfer, để vector chỉ có ý nghĩa khi giữ được quan hệ truy hồi.

**Embedding retrieval** biến truy vấn (query / 쿼리) và document thành vectors sao cho hình học (geometry / 기하학) của véc-tơ (vector / 벡터) không gian (space / 공간) phản ánh relevance hữu ích. Điều quan trọng là embedding không có meaning “tự nhiên”; meaning của distance đến từ huấn luyện (training / 학습) mục tiêu (objective / 목표) và dữ liệu (data / 데이터).

## From văn bản (text / 텍스트) to véc-tơ (vector / 벡터)

Một encoder tạo:

\[
z=f_\theta(text)\in\mathbb{R}^d
\]

Truy vấn (query / 쿼리) và document được encode thành `q`, `d`. Retrieval dùng similarity:

\[
s(q,d)=q^Td
\]

hoặc cosine similarity:

\[
\cos(q,d)=\frac{q^Td}{\|q\|\|d\|}
\]

Nếu vectors được L2-normalize, dot sản phẩm (product / 제품) và cosine ranking giống nhau.

Từ text, query và document được encode thành vectors; bước tiếp theo hỏi vector đang đại diện cho loại quan hệ relevance nào.

## What Does the véc-tơ (vector / 벡터) Represent?

Embedding có thể encode topical similarity, intent, ngữ nghĩa (semantic / 의미적) equivalence hoặc task-specific relevance tùy huấn luyện (training / 학습). Một general sentence embedding mô hình (model / 모델) không nhất thiết tối ưu cho question→answer retrieval.

Ví dụ:

```text
query: "How do I reset my password?"
positive doc: "Password recovery steps"
```

Huấn luyện (training / 학습) nên đưa query-document positive pair kiểu này để hình học (geometry / 기하학) phản ánh retrieval intent.

Ý nghĩa của vector đến từ objective và dữ liệu huấn luyện, không phải từ bản thân tọa độ; pooling quyết định cách gom token thành một biểu diễn duy nhất.

## Pooling

Transformer tạo đơn vị từ (token / 토큰) representations. Để có one véc-tơ (vector / 벡터) cho whole văn bản (text / 텍스트), encoder cần pooling:

- CLS đơn vị từ (token / 토큰);
- mean pooling;
- weighted pooling;
- learned pooling.

Pooling chiến lược (strategy / 전략) ảnh hưởng retrieval chất lượng (quality / 품질). Mean pooling simple nhưng có thể dilute key đơn vị từ (token / 토큰) trong long chunk.

Pooling giữ lại một vector cho chunk, còn normalization làm score giữa các vector ổn định hơn khi mô hình được huấn luyện theo giả định tương ứng.

## Normalization

Embedding normalization thường giúp score stable:

\[
\hat z=\frac{z}{\|z\|}
\]

Nhưng không phải mọi mô hình (model / 모델) được train với same giả định (assumption / 가정). Documentation của embedding mô hình (model / 모델) cần được follow.

Normalization giúp so sánh nhất quán trong một không gian, nhưng dimension vẫn quyết định capacity, bộ nhớ và chi phí index.

## Dimensionality

Dimension lớn cho sức chứa (capacity / 용량) cao hơn nhưng tăng lưu trữ (storage / 저장소)/chỉ mục (index / 인덱스) chi phí (cost / 비용). Nếu có `N` vectors dimension `d` float32:

\[
lưu trữ (storage / 저장소)\approx N\cdot d\cdot 4\ bytes
\]

1 triệu vectors × 1536 dimensions ≈ 6.1 GB chỉ cho raw vectors, chưa tính chỉ mục (index / 인덱스)/siêu dữ liệu (metadata / 메타데이터).

Dimension reduction hoặc quantized chỉ mục (index / 인덱스) có thể giảm chi phí (cost / 비용).

Dimension lớn có thể tăng sức chứa nhưng cũng tăng chi phí; sau khi chọn kích thước, pipeline còn phải tuân thủ prefix query/document của model.

## Truy vấn (query / 쿼리)/Document Prefixes

Một số embedding các mô hình (models / 모델들) được train với prefixes như:

```text
query: ...
passage: ...
```

Prefix không cosmetic; nó tín hiệu (signal / 신호) role trong asymmetric huấn luyện (training / 학습). Bỏ prefix có thể giảm hiệu năng (performance / 성능).

Prefix mang tín hiệu về vai trò của text trong huấn luyện; khi encode thực tế, chunk cũng phải giữ đủ context cục bộ để vector có ích cho retrieval.

## Chunk Embedding

RAG thường embed chunks thay whole documents. Chunk véc-tơ (vector / 벡터) phải represent enough cục bộ (local / 로컬) ngữ nghĩa (semantic / 의미적) ngữ cảnh (context / 맥락) để truy vấn (query / 쿼리) match.

Nếu chunk chỉ chứa một bảng (table / 테이블) row không header, embedding mất ngữ nghĩa (semantics / 의미론). Ingestion có thể prepend section title/document siêu dữ liệu (metadata / 메타데이터) trước embedding.

Chunk embedding cần biểu diễn nội dung đủ rõ, còn metadata authorization và version nên được giữ như filter deterministic thay vì nhồi tất cả vào vector.

## Siêu dữ liệu (metadata / 메타데이터) in Embedding vs siêu dữ liệu (metadata / 메타데이터) as Filter

Có thể concatenate siêu dữ liệu (metadata / 메타데이터) vào văn bản (text / 텍스트) trước embedding:

```text
Title: Refund Policy
Product: Card
Content: ...
```

Nhưng deterministic các ràng buộc (constraints / 제약조건들) như truy cập (access / 접근) mức (level / 수준), tenant hoặc phiên bản (version / 버전) nên vẫn dùng filters. Không nên hy vọng véc-tơ (vector / 벡터) hình học (geometry / 기하학) enforce authorization.

Metadata filter giữ các ràng buộc không thể suy ra an toàn từ similarity; hard negatives thì dạy model phân biệt các tài liệu gần nhau nhưng khác đáp án.

## Hard Negatives

Retriever fine-tuning cần hard negatives. Ví dụ truy vấn (query / 쿼리) hỏi chính sách (policy / 정책) cho `credit card`, negative là nearly identical chính sách (policy / 정책) cho `debit card`.

Mô hình (model / 모델) học distinction trọng yếu (critical / 중요) mà general ngữ nghĩa (semantic / 의미적) similarity dễ bỏ qua.

Hard negatives tạo các cặp khó có chủ đích; in-batch negatives mở rộng số negative hiệu quả nhưng phải kiểm soát false negatives.

## In-Batch Negatives

Trong contrastive huấn luyện (training / 학습), other positives trong same batch thường dùng làm negatives. Efficient nhưng có rủi ro (risk / 위험) false negatives nếu two queries share relevant docs.

Batch composition ảnh hưởng học tập (learning / 학습) tín hiệu (signal / 신호).

In-batch negatives phụ thuộc batch composition; Matryoshka embeddings đưa một trade-off khác bằng cách cho phép cắt vector theo ngân sách.

## Matryoshka / Truncatable Embeddings

Một số các mô hình (models / 모델들) train để prefix dimensions vẫn usable, cho phép truncate véc-tơ (vector / 벡터) để trade chất lượng (quality / 품질) for lưu trữ (storage / 저장소)/độ trễ (latency / 지연 시간). Đây là kiến trúc (architecture / 아키텍처)/huấn luyện (training / 학습) thuộc tính (property / 속성), không áp dụng arbitrary cho mọi embedding véc-tơ (vector / 벡터).

Truncatable embeddings chỉ hoạt động khi model được huấn luyện cho thuộc tính đó; multilingual embeddings lại tập trung vào việc căn chỉnh không gian giữa các ngôn ngữ.

## Multilingual Embeddings

Multilingual embedding maps semantically similar văn bản (text / 텍스트) across languages vào dùng chung (common / 공통) không gian (space / 공간):

```text
"hoàn tiền"
"refund"
"환불"
```

có thể gần nhau.

Nhưng cross-language retrieval cần eval riêng vì ngôn ngữ (language / 언어) imbalance trong huấn luyện (training / 학습) có thể tạo chất lượng (quality / 품질) gap.

Multilingual alignment cần được đo theo từng language pair; với mã nguồn, identifiers và cấu trúc hàm tạo ra một loại tín hiệu khác.

## Mã (code / 코드) Embeddings

Mã (code / 코드) tìm kiếm (search / 검색) có ngữ nghĩa (semantics / 의미론) khác prose. hàm (function / 함수) signature, identifiers và hành vi (behavior / 동작) matter. Domain-specific mã (code / 코드) embedding mô hình (model / 모델) thường tốt hơn generic văn bản (text / 텍스트) embedding.

Code embeddings cần giữ semantics của signature và hành vi; khi dùng similarity score cho quyết định retrieval, threshold phải được calibrate trên dữ liệu có nhãn.

## Similarity Thresholds

Một dùng chung (common / 공통) mistake là hard-code `cosine > 0.8 = relevant`. Score phân phối (distribution / 분포) depends mô hình (model / 모델), corpus và truy vấn (query / 쿼리) kiểu (type / 타입).

Threshold phải calibrate trên labeled retrieval dữ liệu (data / 데이터).

Top-k ranking thường more portable than absolute threshold, nhưng abstention/use-no-evidence decisions vẫn cần calibration.

Threshold phụ thuộc model, corpus và query distribution; embedding drift có thể làm threshold cũ và index cũ mất ý nghĩa sau khi đổi model.

## Embedding Drift

Khi đổi embedding mô hình (model / 모델), old and new vectors thường không nằm trong same không gian (space / 공간). truy vấn (query / 쿼리) encoded bằng new mô hình (model / 모델) không nên tìm kiếm (search / 검색) old vectors unless mô hình (model / 모델) explicitly compatible.

Di chuyển (migration / 마이그레이션) cần re-embed corpus hoặc dual-index chuyển tiếp (transition / 전이).

Khi không gian embedding thay đổi, cần re-embed hoặc duy trì dual index; versioning ghi lại chuỗi pipeline để truy nguyên regression.

## Versioning

Store siêu dữ liệu (metadata / 메타데이터):

```text
embedding_model_version
chunker_version
source_version
created_at
```

Nếu retrieval regression xảy ra, nhóm (team / 팀) cần biết chỉ mục (index / 인덱스) được tạo bằng chuỗi xử lý (pipeline / 파이프라인) nào.

Versioning nối model với chunker và source snapshot; privacy là ranh giới tiếp theo vì vector có thể vẫn tiết lộ thông tin nguồn.

## Privacy

Embedding không nên được assume irreversible. véc-tơ (vector / 벡터) có thể leak ngữ nghĩa (semantic / 의미적)/content thông tin (information / 정보). kiểm soát truy cập (access control / 접근 제어) cho véc-tơ (vector / 벡터) DB cần giống nguồn (source / 소스) dữ liệu (data / 데이터) sensitivity.

Embedding không nên được coi là vô hại chỉ vì đã biến thành vector; evaluation phải đo retrieval task và các slice rủi ro thực tế.

## Evaluation

Embedding chất lượng (quality / 품질) nên đo retrieval tác vụ (task / 작업):

```text
Recall@k
MRR
nDCG
hard-negative discrimination
multilingual slices
```

Visualization đẹp của vectors không đủ bằng chứng (evidence / 증거) môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질).

Evaluation cung cấp bằng chứng vận hành, còn mô hình tư duy tóm tắt vì sao distance chỉ có nghĩa trong một objective retrieval cụ thể.

## Mô hình tư duy (mental model / 사고 모델)

> Embedding là **learned coordinate hệ thống (system / 시스템) cho một retrieval mục tiêu (objective / 목표)**. Distance có meaning vì mô hình (model / 모델) được train để relevant things align, không vì véc-tơ (vector / 벡터) tự mang ngữ nghĩa (semantic / 의미적) truth.

Mô hình tư duy này đặt embedding như hệ tọa độ học được cho một mục tiêu truy hồi; các ngộ nhận sau đây kiểm tra những suy luận sai về vector.

## Dùng chung (common / 공통) Misconceptions

### “Embedding giống cơ sở dữ liệu (database / 데이터베이스) băm (hash / 해시) của sentence”

Không. Similar inputs can be near, and véc-tơ (vector / 벡터) is lossy biểu diễn (representation / 표현).

### “Higher dimension luôn better”

Không. chi phí (cost / 비용) tăng và useful tín hiệu (signal / 신호) phụ thuộc huấn luyện (training / 학습).

### “siêu dữ liệu (metadata / 메타데이터) filter có thể thay bằng embedding”

Không cho bảo mật (security / 보안)/phiên bản (version / 버전) các ràng buộc (constraints / 제약조건들).

Các ngộ nhận thường nhầm embedding với hash, coi dimension là chất lượng tuyệt đối hoặc dùng vector thay authorization; phần liên kết kiến thức nối sang đại số tuyến tính, LLM embeddings và vector search.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [LLM Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md), và tiếp theo [Vector Search](./03_vector_search.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
