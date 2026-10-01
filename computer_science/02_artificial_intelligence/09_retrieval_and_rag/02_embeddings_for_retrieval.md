# Embeddings for Retrieval

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Embeddings for Retrieval**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **From văn bản (text / 텍스트) to véc-tơ (vector / 벡터)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **What Does the véc-tơ (vector / 벡터) Represent?** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Embeddings for Retrieval**, **What Does the véc-tơ (vector / 벡터) Represent?** tiếp nhận điểm tựa từ **From văn bản (text / 텍스트) to véc-tơ (vector / 벡터)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pooling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## What Does the véc-tơ (vector / 벡터) Represent?

Embedding có thể encode topical similarity, intent, ngữ nghĩa (semantic / 의미적) equivalence hoặc task-specific relevance tùy huấn luyện (training / 학습). Một general sentence embedding mô hình (model / 모델) không nhất thiết tối ưu cho question→answer retrieval.

Ví dụ:

```text
query: "How do I reset my password?"
positive doc: "Password recovery steps"
```

Huấn luyện (training / 학습) nên đưa query-document positive pair kiểu này để hình học (geometry / 기하학) phản ánh retrieval intent.

> **Chuyển mạch:** Ở chặng này của **Embeddings for Retrieval**, **Pooling** tiếp nhận điểm tựa từ **What Does the véc-tơ (vector / 벡터) Represent?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pooling

Transformer tạo đơn vị từ (token / 토큰) representations. Để có one véc-tơ (vector / 벡터) cho whole văn bản (text / 텍스트), encoder cần pooling:

- CLS đơn vị từ (token / 토큰);
- mean pooling;
- weighted pooling;
- learned pooling.

Pooling chiến lược (strategy / 전략) ảnh hưởng retrieval chất lượng (quality / 품질). Mean pooling simple nhưng có thể dilute key đơn vị từ (token / 토큰) trong long chunk.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Embeddings for Retrieval**, **Normalization** tiếp nhận điểm tựa từ **Pooling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dimensionality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normalization

Embedding normalization thường giúp score stable:

\[
\hat z=\frac{z}{\|z\|}
\]

Nhưng không phải mọi mô hình (model / 모델) được train với same giả định (assumption / 가정). Documentation của embedding mô hình (model / 모델) cần được follow.

> **Chuyển mạch:** Trong **Embeddings for Retrieval**, **Dimensionality** tiếp nhận điểm tựa từ **Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truy vấn (query / 쿼리)/Document Prefixes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dimensionality

Dimension lớn cho sức chứa (capacity / 용량) cao hơn nhưng tăng lưu trữ (storage / 저장소)/chỉ mục (index / 인덱스) chi phí (cost / 비용). Nếu có `N` vectors dimension `d` float32:

\[
lưu trữ (storage / 저장소)\approx N\cdot d\cdot 4\ bytes
\]

1 triệu vectors × 1536 dimensions ≈ 6.1 GB chỉ cho raw vectors, chưa tính chỉ mục (index / 인덱스)/siêu dữ liệu (metadata / 메타데이터).

Dimension reduction hoặc quantized chỉ mục (index / 인덱스) có thể giảm chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Embeddings for Retrieval**, **Truy vấn (query / 쿼리)/Document Prefixes** tiếp nhận điểm tựa từ **Dimensionality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chunk Embedding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy vấn (query / 쿼리)/Document Prefixes

Một số embedding các mô hình (models / 모델들) được train với prefixes như:

```text
query: ...
passage: ...
```

Prefix không cosmetic; nó tín hiệu (signal / 신호) role trong asymmetric huấn luyện (training / 학습). Bỏ prefix có thể giảm hiệu năng (performance / 성능).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Embeddings for Retrieval**, **Chunk Embedding** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리)/Document Prefixes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Siêu dữ liệu (metadata / 메타데이터) in Embedding vs siêu dữ liệu (metadata / 메타데이터) as Filter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chunk Embedding

RAG thường embed chunks thay whole documents. Chunk véc-tơ (vector / 벡터) phải represent enough cục bộ (local / 로컬) ngữ nghĩa (semantic / 의미적) ngữ cảnh (context / 맥락) để truy vấn (query / 쿼리) match.

Nếu chunk chỉ chứa một bảng (table / 테이블) row không header, embedding mất ngữ nghĩa (semantics / 의미론). Ingestion có thể prepend section title/document siêu dữ liệu (metadata / 메타데이터) trước embedding.

> **Chuyển mạch:** Trong **Embeddings for Retrieval**, **Chunk Embedding** nêu điều cần giải thích; **Siêu dữ liệu (metadata / 메타데이터) in Embedding vs siêu dữ liệu (metadata / 메타데이터) as Filter** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hard Negatives** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Siêu dữ liệu (metadata / 메타데이터) in Embedding vs siêu dữ liệu (metadata / 메타데이터) as Filter

Có thể concatenate siêu dữ liệu (metadata / 메타데이터) vào văn bản (text / 텍스트) trước embedding:

```text
Title: Refund Policy
Product: Card
Content: ...
```

Nhưng deterministic các ràng buộc (constraints / 제약조건들) như truy cập (access / 접근) mức (level / 수준), tenant hoặc phiên bản (version / 버전) nên vẫn dùng filters. Không nên hy vọng véc-tơ (vector / 벡터) hình học (geometry / 기하학) enforce authorization.

> **Chuyển mạch:** Ở chặng này của **Embeddings for Retrieval**, **Siêu dữ liệu (metadata / 메타데이터) in Embedding vs siêu dữ liệu (metadata / 메타데이터) as Filter** nêu điều cần giải thích; **Hard Negatives** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **In-Batch Negatives** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hard Negatives

Retriever fine-tuning cần hard negatives. Ví dụ truy vấn (query / 쿼리) hỏi chính sách (policy / 정책) cho `credit card`, negative là nearly identical chính sách (policy / 정책) cho `debit card`.

Mô hình (model / 모델) học distinction trọng yếu (critical / 중요) mà general ngữ nghĩa (semantic / 의미적) similarity dễ bỏ qua.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Embeddings for Retrieval**, **In-Batch Negatives** tiếp nhận điểm tựa từ **Hard Negatives** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Matryoshka / Truncatable Embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## In-Batch Negatives

Trong contrastive huấn luyện (training / 학습), other positives trong same batch thường dùng làm negatives. Efficient nhưng có rủi ro (risk / 위험) false negatives nếu two queries share relevant docs.

Batch composition ảnh hưởng học tập (learning / 학습) tín hiệu (signal / 신호).

> **Chuyển mạch:** Trong **Embeddings for Retrieval**, **Matryoshka / Truncatable Embeddings** tiếp nhận điểm tựa từ **In-Batch Negatives** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multilingual Embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Matryoshka / Truncatable Embeddings

Một số các mô hình (models / 모델들) train để prefix dimensions vẫn usable, cho phép truncate véc-tơ (vector / 벡터) để trade chất lượng (quality / 품질) for lưu trữ (storage / 저장소)/độ trễ (latency / 지연 시간). Đây là kiến trúc (architecture / 아키텍처)/huấn luyện (training / 학습) thuộc tính (property / 속성), không áp dụng arbitrary cho mọi embedding véc-tơ (vector / 벡터).

> **Chuyển mạch:** Ở chặng này của **Embeddings for Retrieval**, **Multilingual Embeddings** tiếp nhận điểm tựa từ **Matryoshka / Truncatable Embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mã (code / 코드) Embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multilingual Embeddings

Multilingual embedding maps semantically similar văn bản (text / 텍스트) across languages vào dùng chung (common / 공통) không gian (space / 공간):

```text
"hoàn tiền"
"refund"
"환불"
```

có thể gần nhau.

Nhưng cross-language retrieval cần eval riêng vì ngôn ngữ (language / 언어) imbalance trong huấn luyện (training / 학습) có thể tạo chất lượng (quality / 품질) gap.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Embeddings for Retrieval**, **Mã (code / 코드) Embeddings** tiếp nhận điểm tựa từ **Multilingual Embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Similarity Thresholds** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mã (code / 코드) Embeddings

Mã (code / 코드) tìm kiếm (search / 검색) có ngữ nghĩa (semantics / 의미론) khác prose. hàm (function / 함수) signature, identifiers và hành vi (behavior / 동작) matter. Domain-specific mã (code / 코드) embedding mô hình (model / 모델) thường tốt hơn generic văn bản (text / 텍스트) embedding.

> **Chuyển mạch:** Trong **Embeddings for Retrieval**, **Similarity Thresholds** tiếp nhận điểm tựa từ **Mã (code / 코드) Embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Embedding Drift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Similarity Thresholds

Một dùng chung (common / 공통) mistake là hard-code `cosine > 0.8 = relevant`. Score phân phối (distribution / 분포) depends mô hình (model / 모델), corpus và truy vấn (query / 쿼리) kiểu (type / 타입).

Threshold phải calibrate trên labeled retrieval dữ liệu (data / 데이터).

Top-k ranking thường more portable than absolute threshold, nhưng abstention/use-no-evidence decisions vẫn cần calibration.

> **Chuyển mạch:** Ở chặng này của **Embeddings for Retrieval**, **Embedding Drift** tiếp nhận điểm tựa từ **Similarity Thresholds** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Embedding Drift

Khi đổi embedding mô hình (model / 모델), old and new vectors thường không nằm trong same không gian (space / 공간). truy vấn (query / 쿼리) encoded bằng new mô hình (model / 모델) không nên tìm kiếm (search / 검색) old vectors unless mô hình (model / 모델) explicitly compatible.

Di chuyển (migration / 마이그레이션) cần re-embed corpus hoặc dual-index chuyển tiếp (transition / 전이).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Embeddings for Retrieval**, **Versioning** tiếp nhận điểm tựa từ **Embedding Drift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Versioning

Store siêu dữ liệu (metadata / 메타데이터):

```text
embedding_model_version
chunker_version
source_version
created_at
```

Nếu retrieval regression xảy ra, nhóm (team / 팀) cần biết chỉ mục (index / 인덱스) được tạo bằng chuỗi xử lý (pipeline / 파이프라인) nào.

> **Chuyển mạch:** Trong **Embeddings for Retrieval**, **Privacy** tiếp nhận điểm tựa từ **Versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Privacy

Embedding không nên được assume irreversible. véc-tơ (vector / 벡터) có thể leak ngữ nghĩa (semantic / 의미적)/content thông tin (information / 정보). kiểm soát truy cập (access control / 접근 제어) cho véc-tơ (vector / 벡터) DB cần giống nguồn (source / 소스) dữ liệu (data / 데이터) sensitivity.

> **Chuyển mạch:** Ở chặng này của **Embeddings for Retrieval**, **Evaluation** tiếp nhận điểm tựa từ **Privacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Embeddings for Retrieval**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Evaluation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Embedding là **learned coordinate hệ thống (system / 시스템) cho một retrieval mục tiêu (objective / 목표)**. Distance có meaning vì mô hình (model / 모델) được train để relevant things align, không vì véc-tơ (vector / 벡터) tự mang ngữ nghĩa (semantic / 의미적) truth.

> **Chuyển mạch:** Trong **Embeddings for Retrieval**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Embedding giống cơ sở dữ liệu (database / 데이터베이스) băm (hash / 해시) của sentence”

Không. Similar inputs can be near, and véc-tơ (vector / 벡터) is lossy biểu diễn (representation / 표현).

### “Higher dimension luôn better”

Không. chi phí (cost / 비용) tăng và useful tín hiệu (signal / 신호) phụ thuộc huấn luyện (training / 학습).

### “siêu dữ liệu (metadata / 메타데이터) filter có thể thay bằng embedding”

Không cho bảo mật (security / 보안)/phiên bản (version / 버전) các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Ở chặng này của **Embeddings for Retrieval**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [LLM Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md), và tiếp theo [Vector Search](./03_vector_search.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
