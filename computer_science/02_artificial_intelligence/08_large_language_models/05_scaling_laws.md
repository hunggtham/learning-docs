# Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Scaling laws trong large language models**. Route đi từ model/data/compute axes → loss scaling → compute-optimal allocation → inference-time scaling → capability and saturation limits, để quy mô được đánh giá bằng budget và mục tiêu cụ thể.

Khi Large ngôn ngữ (language / 언어) mô hình (model / 모델) lớn hơn, câu hỏi không chỉ là “thêm parameters có tốt hơn không?” mà là **nên phân bổ compute giữa mô hình (model / 모델) kích thước (size / 크기), dữ liệu (data / 데이터) và huấn luyện (training / 학습) duration như thế nào**. **Scaling laws (스케일링 법칙)** nghiên cứu relationship thực nghiệm giữa mô hình (model / 모델) hiệu năng (performance / 성능) và những tài nguyên (resource / 자원) đó.

Một mẫu (pattern / 패턴) thường thấy là mất mát (loss / 손실) giảm theo power law khi tăng quy mô (scale / 규모) trong một khoảng rộng. Điều này không có nghĩa hiệu năng (performance / 성능) mọi benchmark tăng giống nhau, nhưng nó cho phép dự đoán trend và planning huấn luyện (training / 학습) runs tốt hơn.

## Ba trục quy mô (scale / 규모) chính

Pretraining chi phí (cost / 비용) có thể nhìn gần đúng qua ba quantities:

```text
N = số parameters
D = số training tokens
C = compute budget
```

Nếu mô hình (model / 모델) rất lớn nhưng dữ liệu (data / 데이터) quá ít, mô hình (model / 모델) bị **under-trained**. Nếu dữ liệu (data / 데이터) rất nhiều nhưng mô hình (model / 모델) quá nhỏ, sức chứa (capacity / 용량) có thể là bottleneck. Compute-optimal huấn luyện (training / 학습) tìm balance tốt hơn giữa `N` và `D` dưới ngân sách (budget / 예산) cố định.

> **Chuyển mạch:** Trong **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Parameters không phải sức chứa (capacity / 용량) hữu ích duy nhất** tiếp nhận điểm tựa từ **Ba trục quy mô (scale / 규모) chính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compute-optimal intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parameters không phải sức chứa (capacity / 용량) hữu ích duy nhất

Tăng parameters mở rộng hàm (function / 함수) lớp (class / 클래스) và biểu diễn (representation / 표현) sức chứa (capacity / 용량), nhưng năng lực (capability / 역량) còn phụ thuộc kiến trúc (architecture / 아키텍처), dữ liệu (data / 데이터) chất lượng (quality / 품질), optimizer, ngữ cảnh (context / 맥락) length và huấn luyện (training / 학습) recipe. Hai các mô hình (models / 모델들) cùng parameter count có thể khác đáng kể.

**Active parameters** cũng khác total parameters trong architectures như Mixture-of-Experts (MoE), nơi mỗi đơn vị từ (token / 토큰) chỉ đi qua một subset experts. Vì vậy “mô hình (model / 모델) 100B” không luôn có suy luận (inference / 추론) chi phí (cost / 비용) tương đương mô hình (model / 모델) dense 100B.

> **Chuyển mạch:** Ở chặng này của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Compute-optimal intuition** tiếp nhận điểm tựa từ **Parameters không phải sức chứa (capacity / 용량) hữu ích duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Huấn luyện (training / 학습) tokens và epochs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compute-optimal intuition

Giả sử có ngân sách (budget / 예산) compute cố định. Nếu dùng tất cả ngân sách (budget / 예산) để tăng `N` nhưng giữ `D` thấp, mỗi parameter nhìn thấy quá ít bằng chứng (evidence / 증거). Ngược lại, train mô hình (model / 모델) nhỏ trên quá nhiều dữ liệu (data / 데이터) có thể waste dữ liệu (data / 데이터) because sức chứa (capacity / 용량) giới hạn.

Mô hình tư duy (mental model / 사고 모델):

> quy mô (scale / 규모) hiệu quả là **mô hình (model / 모델) đủ lớn để hấp thụ cấu trúc (structure / 구조) trong dữ liệu (data / 데이터), và dữ liệu (data / 데이터) đủ nhiều để train mô hình (model / 모델) lớn đó đúng mức**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Huấn luyện (training / 학습) tokens và epochs** tiếp nhận điểm tựa từ **Compute-optimal intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mất mát (loss / 손실) scaling vs năng lực (capability / 역량) scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Huấn luyện (training / 학습) tokens và epochs

Trong web-scale pretraining, corpus có thể được traversed một hoặc vài lần tùy recipe. Repeating dữ liệu (data / 데이터) quá nhiều tăng memorization và diminishing returns. Nhưng curated high-quality dữ liệu (data / 데이터) đôi khi được intentionally upsampled.

Do đó raw đơn vị từ (token / 토큰) count không bằng unique thông tin (information / 정보) content.

> **Chuyển mạch:** Trong **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Mất mát (loss / 손실) scaling vs năng lực (capability / 역량) scaling** tiếp nhận điểm tựa từ **Huấn luyện (training / 학습) tokens và epochs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) length là một quy mô (scale / 규모) dimension khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mất mát (loss / 손실) scaling vs năng lực (capability / 역량) scaling

Pretraining mất mát (loss / 손실) có thể giảm smooth, trong khi benchmark năng lực (capability / 역량) nhìn discontinuous. Ví dụ benchmark pass/thất bại (fail / 실패) có threshold; mô hình (model / 모델) từ 49% lên 51% có thể trông như năng lực (capability / 역량) “xuất hiện”.

Một số tác vụ (task / 작업) thực sự có nonlinear hành vi (behavior / 동작) do composition of learned skills, nhưng không nên gọi mọi jump là emergence mà không kiểm tra chỉ số (metric / 지표) granularity.

> **Chuyển mạch:** Ở chặng này của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Ngữ cảnh (context / 맥락) length là một quy mô (scale / 규모) dimension khác** tiếp nhận điểm tựa từ **Mất mát (loss / 손실) scaling vs năng lực (capability / 역량) scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inference-time compute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) length là một quy mô (scale / 규모) dimension khác

Longer ngữ cảnh (context / 맥락) cho phép mô hình (model / 모델) điều kiện (condition / 조건) trên nhiều tokens hơn nhưng attention và KV bộ nhớ đệm (cache / 캐시) chi phí (cost / 비용) tăng. huấn luyện (training / 학습) mô hình (model / 모델) ở ngữ cảnh (context / 맥락) 4k không tự động bảo đảm mô hình (model / 모델) dùng hiệu quả 128k chỉ bằng thay cấu hình (config / 설정).

Long-context năng lực (capability / 역량) còn phụ thuộc positional phương thức (method / 메서드), huấn luyện (training / 학습) phân phối (distribution / 분포), attention hiện thực (implementation / 구현) và evaluation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Inference-time compute** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) length là một quy mô (scale / 규모) dimension khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distillation và small các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inference-time compute

Quy mô (scale / 규모) không chỉ nằm ở pretraining. mô hình (model / 모델) có thể dùng thêm compute lúc suy luận (inference / 추론) qua:

- sampling nhiều candidates;
- tìm kiếm (search / 검색)/xác minh (verification / 확인);
- longer lập luận (reasoning / 추론) trajectories;
- công cụ (tool / 도구) calls;
- retrieval;
- self-consistency hoặc reranking.

Điều này tạo sự đánh đổi (trade-off / 트레이드오프) mới: cùng một cơ sở (base / 기반) mô hình (model / 모델), tăng inference-time compute có thể cải thiện accuracy nhưng tăng độ trễ (latency / 지연 시간)/chi phí (cost / 비용).

> **Chuyển mạch:** Trong **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Distillation và small các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Inference-time compute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Distillation và small các mô hình (models / 모델들)

Quy mô (scale / 규모) lớn có thể dùng để tạo teacher, sau đó distill năng lực (capability / 역량) vào smaller mô hình (model / 모델). Small các mô hình (models / 모델들) vẫn quan trọng khi độ trễ (latency / 지연 시간), privacy, edge triển khai (deployment / 배포) hoặc chi phí (cost / 비용) là ràng buộc (constraint / 제약조건).

Scaling laws không hàm ý mọi ứng dụng (application / 애플리케이션) nên dùng mô hình (model / 모델) lớn nhất.

> **Chuyển mạch:** Ở chặng này của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Economics của quy mô (scale / 규모)** tiếp nhận điểm tựa từ **Distillation và small các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diminishing returns** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của quy mô (scale / 규모)

Huấn luyện (training / 학습) frontier mô hình (model / 모델) cần hardware, năng lượng (energy / 에너지), networking và kỹ thuật (engineering / 엔지니어링) rất lớn. Nhưng môi trường vận hành (production / 운영 환경) chi phí (cost / 비용) thường dominated bởi suy luận (inference / 추론) nếu người dùng (user / 사용자) volume cao.

Một kiến trúc (architecture / 아키텍처) tối ưu huấn luyện (training / 학습) chi phí (cost / 비용) chưa chắc tối ưu serving. KV bộ nhớ đệm (cache / 캐시), batchability, chuỗi (sequence / 시퀀스) length và decoding speed trở thành economic variables.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Diminishing returns** tiếp nhận điểm tựa từ **Economics của quy mô (scale / 규모)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scaling và dữ liệu (data / 데이터) chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diminishing returns

Power-law improvement nghĩa improvement tiếp theo thường đắt hơn. Nếu giảm mất mát (loss / 손실) từ 2.0 xuống 1.8 cần X compute, giảm từ 1.8 xuống 1.6 có thể cần nhiều hơn đáng kể.

Vì vậy hệ thống (system / 시스템) kỹ thuật (engineering / 엔지니어링) thường thắng raw scaling khi bài toán (problem / 문제) là freshness, grounding, công cụ (tool / 도구) truy cập (access / 접근) hoặc chính sách (policy / 정책). RAG có thể hiệu quả hơn train mô hình (model / 모델) lớn hơn chỉ để nhớ private documents.

> **Chuyển mạch:** Trong **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Diminishing returns** nêu điều cần giải thích; **Scaling và dữ liệu (data / 데이터) chất lượng (quality / 품질)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Scaling và alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scaling và dữ liệu (data / 데이터) chất lượng (quality / 품질)

Khi mô hình (model / 모델) nhỏ, sức chứa (capacity / 용량) có thể che bớt bad dữ liệu (data / 데이터) vì mô hình (model / 모델) không memorize everything. mô hình (model / 모델) lớn có khả năng hấp thụ cả useful patterns lẫn noise, duplicated misinformation và undesirable styles.

Do đó quy mô (scale / 규모) làm dữ liệu (data / 데이터) quản trị (governance / 거버넌스) quan trọng hơn, không ít hơn.

> **Chuyển mạch:** Ở chặng này của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Scaling và dữ liệu (data / 데이터) chất lượng (quality / 품질)** nêu điều cần giải thích; **Scaling và alignment** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scaling và alignment

Cơ sở (base / 기반) năng lực (capability / 역량) tăng không tự động kéo instruction following, truthfulness hay an toàn (safety / 안전) tăng đồng đều. Alignment/post-training phải quy mô (scale / 규모) theo năng lực (capability / 역량) và attack surface.

Một mô hình (model / 모델) mạnh hơn có thể vừa hữu ích hơn vừa có thất bại (failure / 실패) modes phức tạp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Scaling và alignment** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Scale ≠ chỉ parameters
Scale = model capacity + data + compute + context + inference strategy
```

Câu hỏi đúng không phải “bao nhiêu B parameters?”, mà là **tài nguyên (resource / 자원) nào hiện là bottleneck của tác vụ (task / 작업)/hệ thống (system / 시스템) này?**

> **Chuyển mạch:** Trong **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “mô hình (model / 모델) lớn hơn luôn tốt hơn cho môi trường vận hành (production / 운영 환경)”

Không nếu chi phí (cost / 비용), độ trễ (latency / 지연 시간), privacy hoặc tác vụ (task / 작업) simplicity dominate.

### “mất mát (loss / 손실) giảm nghĩa mọi năng lực (capability / 역량) đều tăng”

Mất mát (loss / 손실) là aggregate ngôn ngữ (language / 언어) modeling tín hiệu (signal / 신호); downstream năng lực (capability / 역량) có thể tăng với tỷ lệ (rate / 비율) khác nhau.

### “ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) lớn = mô hình (model / 모델) nhớ và lập luận (reasoning / 추론) tốt trên toàn ngữ cảnh (context / 맥락)”

Cửa sổ (window / 윈도우) sức chứa (capacity / 용량) và effective ngữ cảnh (context / 맥락) use là hai vấn đề khác nhau.

> **Chuyển mạch:** Ở chặng này của **Scaling Laws trong Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Scaling nối trực tiếp với [AI Compute](../17_ai_compute_and_infrastructure/00_compute_foundations.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Pretraining](./04_pretraining.md).

Xem tiếp: [Instruction Tuning](./06_instruction_tuning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
