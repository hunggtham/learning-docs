# Biểu diễn (representation / 표현) học tập (learning / 학습): học cách biểu diễn dữ liệu

> **Mạch đọc:** Đặt **biểu diễn (representation / 표현) học tập (learning / 학습): học cách biểu diễn dữ liệu** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **biểu diễn (representation / 표현) là gì?** sang **tuyến tính (linear / 선형) Probe như một kiểm thử (test / 테스트)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Biểu diễn (representation / 표현) học tập (learning / 학습) là một trong những ý tưởng trung tâm nhất của Deep học tập (learning / 학습). Thay vì chỉ học ánh xạ (mapping / 매핑) trực tiếp `input → output`, mạng (network / 네트워크) học intermediate spaces trong đó những factors relevant cho tác vụ (task / 작업) được sắp xếp theo hình học (geometry / 기하학) dễ xử lý hơn.

Một biểu diễn (representation / 표현) tốt không có nghĩa “véc-tơ (vector / 벡터) nhìn đẹp”. Nó phải làm downstream computation đơn giản, robust hoặc transferable hơn.

## Biểu diễn (representation / 표현) là gì?

Raw đối tượng (object / 객체) có thể rất phức tạp:

- ảnh (image / 이미지): pixels;
- văn bản (text / 텍스트): đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스);
- audio: waveform;
- người dùng (user / 사용자): tương tác (interaction / 상호작용) lịch sử (history / 이력);
- molecule: đồ thị (graph / 그래프).

Encoder tạo véc-tơ (vector / 벡터)/tensor:

\[
z=f_\theta(x)
\]

`z` là learned biểu diễn (representation / 표현).

Downstream head:

\[
\hat y=g_\phi(z)
\]

Nếu `z` organize task-relevant thông tin (information / 정보) tốt, `g` có thể rất simple.

## Tuyến tính (linear / 선형) Probe như một kiểm thử (test / 테스트)

Nếu frozen biểu diễn (representation / 표현) `z` cho phép tuyến tính (linear / 선형) classifier đạt hiệu năng (performance / 성능) cao, ta nói mục tiêu (target / 대상) thông tin (information / 정보) **linearly accessible**.

Tuyến tính (linear / 선형) probe không đo toàn bộ ngữ nghĩa (semantic / 의미적) richness, nhưng là useful diagnostic: tính năng (feature / 기능) extractor đã “untangle” tác vụ (task / 작업) đến mức nào?

## Phân tán (distributed / 분산) biểu diễn (representation / 표현)

One-hot symbol đặt mỗi category ở orthogonal axis; không encode similarity.

Dense learned embedding:

\[
z\in R^d
\]

có thể encode multiple factors phân tán (distributed / 분산) across dimensions/directions.

Similarity quan hệ (relation / 관계) xuất hiện từ huấn luyện (training / 학습) mục tiêu (objective / 목표), không từ véc-tơ (vector / 벡터) format tự thân.

## Embedding hình học (geometry / 기하학)

Nếu contrastive huấn luyện (training / 학습) kéo related pairs gần nhau và đẩy unrelated pairs xa:

```text
semantically related objects → nearby directions/regions
unrelated objects → farther apart
```

thì cosine/dot-product retrieval becomes meaningful.

Nhưng hình học (geometry / 기하학) objective-specific. Embedding tốt cho ngữ nghĩa (semantic / 의미적) tìm kiếm (search / 검색) chưa chắc tốt cho sentiment clustering hoặc recommendation.

## Supervised biểu diễn (representation / 표현) học tập (learning / 학습)

Classifier mạng (network / 네트워크) learn hidden biểu diễn (representation / 표현) vì final tác vụ (task / 작업) mất mát (loss / 손실) backprop through encoder.

Hidden layers retain thông tin (information / 정보) useful cho mục tiêu (target / 대상) và có thể discard nuisance factors.

Nếu mục tiêu (target / 대상) narrow, biểu diễn (representation / 표현) cũng có thể narrow và transfer kém.

## Self-Supervised biểu diễn (representation / 표현) học tập (learning / 학습)

Self-supervision tạo học tập (learning / 학습) tín hiệu (signal / 신호) từ raw dữ liệu (data / 데이터).

Examples:

- predict next đơn vị từ (token / 토큰);
- reconstruct masked đơn vị từ (token / 토큰)/patch;
- contrast views of same ảnh (image / 이미지);
- predict future segment;
- reconstruct corrupted đầu vào (input / 입력).

Mục tiêu là exploit abundant unlabeled dữ liệu (data / 데이터) để learn reusable cấu trúc (structure / 구조).

Foundation các mô hình (models / 모델들) largely rely on self-supervised pretraining rồi adapt downstream.

## Contrastive học tập (learning / 학습)

Given positive pair `(x,x⁺)` and negatives `x⁻`, mục tiêu (objective / 목표) encourage similarity positive > negatives.

InfoNCE-style mất mát (loss / 손실):

\[
L=-\log
\frac{\exp(sim(z,z^+)/\tau)}
{\sum_j\exp(sim(z,z_j)/\tau)}
\]

`τ` là temperature.

Choice positive pairs defines invariance. ảnh (image / 이미지) augmentations say two crops/color variants should represent same ngữ nghĩa (semantic / 의미적) đối tượng (object / 객체). Wrong augmentation can erase task-relevant thông tin (information / 정보).

## Chỉ số (metric / 지표) học tập (learning / 학습)

Triplet mất mát (loss / 손실):

\[
L=\max(0,d(a,p)-d(a,n)+m)
\]

push anchor-positive closer than anchor-negative by margin `m`.

Hard-negative mining is trọng yếu (critical / 중요): easy negatives produce little độ dốc (gradient / 기울기); false negatives can damage ngữ nghĩa (semantic / 의미적) hình học (geometry / 기하학).

## Autoencoder biểu diễn (representation / 표현)

Encoder-decoder:

\[
x\to z\to\hat x
\]

Reconstruction mục tiêu (objective / 목표) forces `z` to preserve đầu vào (input / 입력) thông tin (information / 정보) needed for reconstruction.

But pixel-perfect reconstruction may prioritize low-level detail not ngữ nghĩa (semantics / 의미론). Bottleneck/denoising/variational các ràng buộc (constraints / 제약조건들) alter learned factors.

Thus mục tiêu (objective / 목표) determines what “important thông tin (information / 정보)” means.

## Bottleneck và Compression

A lower-dimensional `z` forces compression. Under an thông tin (information / 정보) Bottleneck intuition, biểu diễn (representation / 표현) should keep thông tin (information / 정보) useful for mục tiêu (target / 대상) while discarding irrelevant variation.

Formal thông tin (information / 정보) Bottleneck studies sự đánh đổi (trade-off / 트레이드오프) between `I(X;Z)` and `I(Z;Y)`, but practical deep networks do not always directly optimize this formula.

Mental idea remains useful: good biểu diễn (representation / 표현) filters nuisance while preserving predictive cấu trúc (structure / 구조).

## Invariance và Equivariance

**bất biến (invariant / 불변식)** biểu diễn (representation / 표현): transformation of đầu vào (input / 입력) should not thay đổi (change / 변경) biểu diễn (representation / 표현)/đầu ra (output / 출력).

Example ảnh (image / 이미지) classification may want translation invariance.

**Equivariant** biểu diễn (representation / 표현): đầu ra (output / 출력) changes predictably with đầu vào (input / 입력) transformation.

For segmentation/pose, spatial shift should shift đầu ra (output / 출력) correspondingly, not erase location.

Kiến trúc (architecture / 아키텍처) and augmentation encode these các giả định (assumptions / 가정들).

## Transfer học tập (learning / 학습)

Pretrained encoder learns broad biểu diễn (representation / 표현), then downstream tác vụ (task / 작업) uses:

- frozen features + new head;
- partial fine-tuning;
- full fine-tuning;
- adapters/LoRA.

Transfer works when pretraining biểu diễn (representation / 표현) covers factors relevant downstream.

Negative transfer occurs when nguồn (source / 소스) biases/mục tiêu (objective / 목표) mismatch mục tiêu (target / 대상).

## Biểu diễn (representation / 표현) Collapse

Some self-supervised objectives rủi ro (risk / 위험) all inputs map to same constant véc-tơ (vector / 벡터). Then similarity trivial nhưng no thông tin (information / 정보).

Contrastive negatives, stop-gradient asymmetry, predictor kiến trúc (architecture / 아키텍처), variance/covariance regularizers or teacher-student dynamics prevent collapse in different methods.

Understanding collapse clarifies why self-supervised mất mát (loss / 손실) thiết kế (design / 설계) matters.

## Disentanglement

Idealized disentangled biểu diễn (representation / 표현) assigns distinct latent factors to independent generative causes. Example rotation, lighting, định danh (identity / 식별자) separated.

In practice disentanglement is difficult and often not identifiable without inductive độ lệch (bias / 편향)/supervision. Do not assume latent dimensions map cleanly to human concepts.

## Sparse vs Dense Representations

Sparse biểu diễn (representation / 표현) activates few components; dense uses many.

Sparse can improve interpretability/lưu trữ (storage / 저장소)/retrieval properties. Dense embeddings are compact and differentiable.

Hiện đại (modern / 현대적) retrieval increasingly combines sparse lexical and dense ngữ nghĩa (semantic / 의미적) representations because they capture complementary cấu trúc (structure / 구조).

## Biểu diễn (representation / 표현) Drift

When encoder is retrained, embedding hình học (geometry / 기하학) changes. Stored vectors in véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) generated by old encoder may become incompatible.

Môi trường vận hành (production / 운영 환경) consequence:

```text
embedding model version change
→ re-embed corpus
→ rebuild/revalidate index
```

Biểu diễn (representation / 표현) versioning is an LLMOps/data-engineering concern, not just mô hình (model / 모델) lý thuyết (theory / 이론).

## Probing và Interpretability

Probe classifiers can detect whether thông tin (information / 정보) exists in biểu diễn (representation / 표현), but high probe accuracy does not prove cơ sở (base / 기반) mô hình (model / 모델) actually uses that thông tin (information / 정보) causally.

Interventions/ablation are needed for stronger claims.

Biểu diễn (representation / 표현) interpretability must distinguish **decodability** from **nhân quả (causal / 인과적) use**.

## LLM Hidden States Preview

Transformer converts đơn vị từ (token / 토큰) embeddings through layers into contextual representations. Same đơn vị từ (token / 토큰) can have different hidden véc-tơ (vector / 벡터) depending ngữ cảnh (context / 맥락).

Final hidden trạng thái (state / 상태) feeds đầu ra (output / 출력) projection/softmax for next-token prediction. Intermediate layers may encode cú pháp (syntax / 문법), ngữ nghĩa (semantic / 의미적), factual and tác vụ (task / 작업) cấu trúc (structure / 구조) in phân tán (distributed / 분산) form.

This chapter therefore directly prepares embeddings/Transformer/LLM sections.

## Mô hình tư duy (mental model / 사고 모델)

> biểu diễn (representation / 표현) học tập (learning / 학습) = học một coordinate hệ thống (system / 시스템) nơi relationships relevant cho mục tiêu (objective / 목표) trở nên dễ tính hơn.

Raw không gian (space / 공간) không nhất thiết có useful hình học (geometry / 기하학); huấn luyện (training / 학습) bends/reorganizes không gian (space / 공간).

## Dùng chung (common / 공통) Misconceptions

### “Embedding gần nhau nghĩa objects giống nhau tuyệt đối”

Chúng gần theo hình học (geometry / 기하학)/mục tiêu (objective / 목표)/mô hình (model / 모델)/dữ liệu (data / 데이터) cụ thể.

### “Latent dimension 42 chắc chắn đại diện một concept”

Thông tin (information / 정보) thường phân tán (distributed / 분산)/subspace-based.

### “Self-supervised mô hình (model / 모델) không cần labels nên mục tiêu (objective / 목표) neutral”

Pretext tác vụ (task / 작업), augmentation và sampling chính là inductive độ lệch (bias / 편향) mạnh.

### “Nếu thông tin (information / 정보) decodable từ hidden trạng thái (state / 상태) thì mô hình (model / 모델) đang dùng nó”

Decodability không chứng minh nhân quả (causal / 인과적) reliance.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Biểu diễn (representation / 표현) học tập (learning / 학습) nối [Dimensionality Reduction](../04_machine_learning/12_dimensionality_reduction.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Regularization](./07_regularization.md) và sau này [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md), [RAG](../09_retrieval_and_rag/05_rag_fundamentals.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from linear models to neural networks](./00_from_linear_models_to_neural_networks.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
