# Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Pretraining không phải cơ sở dữ liệu (database / 데이터베이스) ingestion** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) là một phần của mô hình (model / 모델)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Pretraining (사전학습 / tiền huấn luyện)** là giai đoạn mô hình (model / 모델) học statistical cấu trúc (structure / 구조) từ một lượng dữ liệu rất lớn trước khi được điều chỉnh để làm theo instruction hoặc phục vụ một ứng dụng (application / 애플리케이션) cụ thể. Với decoder-only LLM, mục tiêu (objective / 목표) phổ biến là **next-token prediction**: tại mỗi vị trí, mô hình (model / 모델) nhận prefix và tối đa hóa xác suất của đơn vị từ (token / 토큰) tiếp theo.

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Mất mát (loss / 손실) tương ứng thường là negative log-likelihood hay cross-entropy:

\[
\mathcal L=-\sum_t \log P_\theta(x_t\mid x_{<t})
\]

Điểm quan trọng là mục tiêu (objective / 목표) này nhìn có vẻ đơn giản nhưng buộc mô hình (model / 모델) phải nén rất nhiều regularity của ngôn ngữ (language / 언어) và world vào parameters. Muốn dự đoán đơn vị từ (token / 토큰) tiếp theo tốt, mô hình (model / 모델) phải học cú pháp (syntax / 문법), ngữ nghĩa (semantic / 의미적) association, discourse cấu trúc (structure / 구조), factual co-occurrence, coding patterns và nhiều dạng lập luận (reasoning / 추론) mẫu (pattern / 패턴) xuất hiện trong huấn luyện (training / 학습) phân phối (distribution / 분포).

## Pretraining không phải cơ sở dữ liệu (database / 데이터베이스) ingestion

Mô hình (model / 모델) không biến corpus thành một key-value store hoàn hảo. huấn luyện (training / 학습) cập nhật hàng tỷ parameters sao cho phân phối (distribution / 분포) đầu ra (output / 출력) phù hợp dữ liệu (data / 데이터). kiến thức (knowledge / 지식) vì vậy được **phân tán (distributed / 분산)** trong weights. Một fact có thể được encode qua nhiều directions trong biểu diễn (representation / 표현) không gian (space / 공간) và nhiều layers cùng lúc.

Điều này giải thích vì sao mô hình (model / 모델) có thể generalize, paraphrase và combine patterns thay vì chỉ replay chính xác (exact / 정확한) huấn luyện (training / 학습) strings. Đồng thời nó cũng giải thích vì sao retrieval từ parameters không đáng tin như truy vấn cơ sở dữ liệu (database / 데이터베이스): parameterized kiến thức (knowledge / 지식) không có guarantee về freshness, provenance hay chính xác (exact / 정확한) lookup.

> **Chuyển mạch:** Trong **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Pretraining không phải cơ sở dữ liệu (database / 데이터베이스) ingestion** nêu điều cần giải thích; **Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) là một phần của mô hình (model / 모델)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Đơn vị từ (token / 토큰) ngân sách (budget / 예산) và exposure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) là một phần của mô hình (model / 모델)

Pretraining chất lượng (quality / 품질) không chỉ phụ thuộc kiến trúc (architecture / 아키텍처). Corpus construction quyết định mô hình (model / 모델) nhìn thấy thế giới nào. Raw web dữ liệu (data / 데이터) thường phải qua deduplication, chất lượng (quality / 품질) filtering, ngôn ngữ (language / 언어) detection, document segmentation, an toàn (safety / 안전) filtering và mixture weighting.

Nếu một lĩnh vực (domain / 도메인) được oversample, mô hình (model / 모델) có xu hướng học lĩnh vực (domain / 도메인) đó mạnh hơn. Nếu corpus chứa duplicated benchmark questions, evaluation có thể bị contamination. Nếu filtering loại quá mạnh một ngôn ngữ (language / 언어), năng lực (capability / 역량) của ngôn ngữ (language / 언어) đó giảm.

Vì vậy có thể coi huấn luyện (training / 학습) phân phối (distribution / 분포) là một implicit curriculum.

> **Chuyển mạch:** Ở chặng này của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) là một phần của mô hình (model / 모델)** nêu điều cần giải thích; **Đơn vị từ (token / 토큰) ngân sách (budget / 예산) và exposure** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Nhân quả (causal / 인과적) masking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị từ (token / 토큰) ngân sách (budget / 예산) và exposure

Dataset thường được đo bằng **đơn vị từ (token / 토큰) count**, không chỉ số document. Một document dài có nhiều huấn luyện (training / 학습) positions hơn document ngắn. Tokenization cũng ảnh hưởng exposure: cùng một câu tiếng Việt hoặc tiếng Hàn có thể cần nhiều đơn vị từ (token / 토큰) hơn tiếng Anh tùy vocabulary, làm tăng compute và giảm effective ngữ cảnh (context / 맥락) sức chứa (capacity / 용량).

Xem thêm: [LLM Tokenization](./01_llm_tokenization.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Nhân quả (causal / 인과적) masking** tiếp nhận điểm tựa từ **Đơn vị từ (token / 토큰) ngân sách (budget / 예산) và exposure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Teacher forcing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhân quả (causal / 인과적) masking

Decoder-only mô hình (model / 모델) dùng nhân quả (causal / 인과적) mask để đơn vị từ (token / 토큰) tại vị trí `t` không nhìn thấy future đơn vị từ (token / 토큰) `x_{>t}` trong huấn luyện (training / 학습). Điều này làm huấn luyện (training / 학습) tác vụ (task / 작업) khớp với autoregressive generation.

Trong mỗi chuỗi (sequence / 시퀀스), forward pass vẫn có thể xử lý nhiều positions song song vì ground-truth previous tokens đã biết. suy luận (inference / 추론) khác: đơn vị từ (token / 토큰) mới phải được sinh tuần tự vì đầu ra (output / 출력) của bước trước trở thành đầu vào (input / 입력) bước sau.

Sự khác nhau này là lý do huấn luyện (training / 학습) thông lượng (throughput / 처리량) và generation độ trễ (latency / 지연 시간) có characteristics rất khác.

> **Chuyển mạch:** Trong **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Teacher forcing** tiếp nhận điểm tựa từ **Nhân quả (causal / 인과적) masking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Packing và chuỗi (sequence / 시퀀스) construction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Teacher forcing

Trong huấn luyện (training / 학습) autoregressive, mô hình (model / 모델) thường nhận **ground-truth previous tokens** thay vì đơn vị từ (token / 토큰) do chính nó sinh. Cơ chế này gọi là teacher forcing.

Nó làm tối ưu hóa (optimization / 최적화) ổn định và parallelizable nhưng tạo mismatch với suy luận (inference / 추론): khi mô hình (model / 모델) sinh sai một đơn vị từ (token / 토큰) lúc triển khai (deployment / 배포), những bước tiếp theo phải điều kiện (condition / 조건) trên chính lỗi đó. lỗi (error / 오류) có thể compound.

Instruction tuning và preference huấn luyện (training / 학습) không loại bỏ hoàn toàn mismatch này.

> **Chuyển mạch:** Ở chặng này của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Teacher forcing** xác định đầu vào; **Packing và chuỗi (sequence / 시퀀스) construction** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Dữ liệu (data / 데이터) mixture** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Packing và chuỗi (sequence / 시퀀스) construction

Để tận dụng GPU, nhiều short documents có thể được **packed** vào cùng chuỗi (sequence / 시퀀스). hiện thực (implementation / 구현) phải đảm bảo attention ranh giới (boundary / 경계) đúng nếu không muốn đơn vị từ (token / 토큰) của document này vô tình nhìn sang document khác theo cách không mong muốn.

Long-context huấn luyện (training / 학습) cũng làm chi phí (cost / 비용) attention tăng mạnh. Với vanilla self-attention, compute/bộ nhớ (memory / 메모리) attention tăng gần quadratic theo chuỗi (sequence / 시퀀스) length:

\[
O(n^2)
\]

Do đó ngữ cảnh (context / 맥락) length không phải một setting miễn phí.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Packing và chuỗi (sequence / 시퀀스) construction** nêu điều cần giải thích; **Dữ liệu (data / 데이터) mixture** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Deduplication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) mixture

Một LLM tổng quát thường train trên mixture như natural ngôn ngữ (language / 언어), mã (code / 코드), mathematics, books, technical documents và curated sources. Weight của từng nguồn (source / 소스) quyết định độ dốc (gradient / 기울기) contribution.

Ví dụ tăng mã (code / 코드) dữ liệu (data / 데이터) có thể cải thiện programming và đôi khi lập luận (reasoning / 추론) có cấu trúc, nhưng nếu mixture mất cân bằng có thể làm giảm ngôn ngữ (language / 언어) chất lượng (quality / 품질) ở lĩnh vực (domain / 도메인) khác. Đây là một tối ưu hóa (optimization / 최적화) đa mục tiêu chứ không chỉ “càng nhiều dữ liệu (data / 데이터) càng tốt”.

> **Chuyển mạch:** Trong **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Dữ liệu (data / 데이터) mixture** nêu điều cần giải thích; **Deduplication** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Memorization và generalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deduplication

Duplicate dữ liệu (data / 데이터) làm mô hình (model / 모델) gặp cùng mẫu (pattern / 패턴) quá nhiều lần, tăng memorization và làm chất lượng (quality / 품질) estimate sai. Dedup có thể ở document-level, paragraph-level hoặc approximate substring mức (level / 수준).

Dedup cũng quan trọng cho benchmark integrity. Nếu evaluation set hoặc near-duplicate của nó xuất hiện trong pretraining corpus, score không còn đo pure generalization.

> **Chuyển mạch:** Ở chặng này của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Memorization và generalization** tiếp nhận điểm tựa từ **Deduplication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델), không tạo assistant hoàn chỉnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memorization và generalization

LLM có thể vừa generalize vừa memorize. Hai hiện tượng không loại trừ nhau.

Rare strings, personally identifying văn bản (text / 텍스트) hoặc repeated sequences có nguy cơ memorization cao hơn. Nhưng phần lớn năng lực (capability / 역량) hữu ích đến từ learned abstractions và statistical regularities chứ không phải chính xác (exact / 정확한) copying.

Khi đánh giá privacy, cần phân biệt:

```text
model biết pattern chung
vs
model có thể reproduce training sequence cụ thể
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델), không tạo assistant hoàn chỉnh** tiếp nhận điểm tựa từ **Memorization và generalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Domain-adaptive pretraining** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델), không tạo assistant hoàn chỉnh

Cơ sở (base / 기반) mô hình (model / 모델) được optimize để continue văn bản (text / 텍스트). Nếu prompt:

```text
User: Explain gradient descent.
Assistant:
```

Cơ sở (base / 기반) mô hình (model / 모델) có thể tiếp tục theo mẫu (pattern / 패턴) đối thoại nếu dữ liệu huấn luyện (training data / 학습 데이터) có mẫu (pattern / 패턴) đó, nhưng không có guarantee sẽ tuân instruction ổn định.

Instruction-following hành vi (behavior / 동작) thường được cải thiện qua supervised fine-tuning và preference tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Trong **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Domain-adaptive pretraining** tiếp nhận điểm tựa từ **Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델), không tạo assistant hoàn chỉnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pretraining và emergent năng lực (capability / 역량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Domain-adaptive pretraining

Có thể tiếp tục pretraining trên corpus chuyên ngành, ví dụ finance, legal hoặc biomedical dữ liệu (data / 데이터). Đây là **continued pretraining / domain-adaptive pretraining**.

Nó khác SFT. Continued pretraining vẫn tối ưu language-model mục tiêu (objective / 목표) trên raw văn bản (text / 텍스트), còn SFT tối ưu đầu ra (output / 출력) được định dạng theo đầu vào (input / 입력)–phản hồi (response / 응답) examples.

Continued pretraining hữu ích khi muốn mô hình (model / 모델) hấp thụ vocabulary và phân phối (distribution / 분포) chuyên ngành sâu hơn, nhưng có thể gây catastrophic forgetting nếu mixture quá hẹp hoặc học tập (learning / 학습) tỷ lệ (rate / 비율) quá cao.

> **Chuyển mạch:** Ở chặng này của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Pretraining và emergent năng lực (capability / 역량)** tiếp nhận điểm tựa từ **Domain-adaptive pretraining** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pretraining và emergent năng lực (capability / 역량)

Khi quy mô (scale / 규모) mô hình (model / 모델)/dữ liệu (data / 데이터)/compute tăng, một số năng lực (capability / 역량) xuất hiện rõ hơn. Không nên hiểu điều đó như “một mô-đun (module / 모듈) lập luận (reasoning / 추론) bí mật tự bật”. năng lực (capability / 역량) observable là kết quả của kiến trúc (architecture / 아키텍처), dữ liệu (data / 데이터) phân phối (distribution / 분포), tối ưu hóa (optimization / 최적화), quy mô (scale / 규모) và evaluation threshold tương tác.

Một benchmark có thể trông như năng lực (capability / 역량) xuất hiện đột ngột chỉ vì score vượt một threshold, trong khi underlying hiệu năng (performance / 성능) tăng dần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Pretraining và emergent năng lực (capability / 역량)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Pretraining là quá trình **nén phân phối (distribution / 분포) của một corpus khổng lồ vào parameters** bằng mục tiêu (objective / 목표) dự đoán đơn vị từ (token / 토큰). mô hình (model / 모델) không học một encyclopedia có chỉ mục (index / 인덱스); nó học một hàm (function / 함수) tạo xác suất (probability / 확률) phân phối (distribution / 분포) dựa trên ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “mô hình (model / 모델) đã đọc internet nên biết mọi thứ trên internet”

Huấn luyện (training / 학습) corpus luôn hữu hạn, filtered và có cutoff. Ngay cả văn bản (text / 텍스트) từng xuất hiện trong huấn luyện (training / 학습) cũng không bảo đảm mô hình (model / 모델) retrieve chính xác.

### “Pretraining chỉ dạy kiến thức factual”

Nó đồng thời dạy cú pháp (syntax / 문법), style, mã (code / 코드) patterns, ngữ nghĩa (semantic / 의미적) relations, procedural patterns và representations hữu ích.

### “Thêm dữ liệu (data / 데이터) luôn tốt”

Low-quality, duplicated hoặc mismatched dữ liệu (data / 데이터) có thể làm mô hình (model / 모델) tệ hơn. dữ liệu (data / 데이터) chất lượng (quality / 품질) và mixture quan trọng như quantity.

> **Chuyển mạch:** Ở chặng này của **Pretraining của Large ngôn ngữ (language / 언어) mô hình (model / 모델)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Pretraining kết nối [Language Models](../07_natural_language_processing/02_language_models.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md).

Xem tiếp: [Scaling Laws](./05_scaling_laws.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
