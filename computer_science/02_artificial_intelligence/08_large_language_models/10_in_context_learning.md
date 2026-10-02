# In-Context học tập (learning / 학습)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **In-Context học tập (learning / 학습)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **“học tập (learning / 학습)” nhưng không cập nhật (update / 업데이트) parameters** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Zero-shot, one-shot, few-shot** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối in-context learning với examples, context window, adaptation và evaluation, để prompt được kiểm tra trên nhiệm vụ thật.

**In-Context học tập (learning / 학습)** là hiện tượng mô hình (model / 모델) thay đổi hành vi (behavior / 동작) dựa trên examples hoặc instructions nằm trong ngữ cảnh (context / 맥락) **mà không cần cập nhật (update / 업데이트) weights**.

Ví dụ:

```text
Input: 2 + 3
Output: five

Input: 4 + 1
Output: five

Input: 7 + 2
Output:
```

Mô hình (model / 모델) có thể infer mẫu (pattern / 패턴) đầu ra (output / 출력) bằng chữ và trả `nine` dù không có độ dốc (gradient / 기울기) step nào xảy ra.

## “học tập (learning / 학습)” nhưng không cập nhật (update / 업데이트) parameters

Tên gọi dễ gây nhầm. Trong ICL, mô hình (model / 모델) weights giữ nguyên trong suy luận (inference / 추론) session. Điều thay đổi là hidden states và attention patterns được điều kiện (condition / 조건) bởi ngữ cảnh (context / 맥락).

Vì vậy cần phân biệt:

```text
Training-time learning → update parameters
In-context learning     → temporary behavior conditioned on prompt/context
```

Ngữ cảnh (context / 맥락) hết thì adaptation đó không được lưu vĩnh viễn vào weights.

> **Chuyển mạch:** Trong **In-Context học tập (learning / 학습)**, **Zero-shot, one-shot, few-shot** tiếp nhận điểm tựa từ **“học tập (learning / 학습)” nhưng không cập nhật (update / 업데이트) parameters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Demonstrations làm gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Zero-shot, one-shot, few-shot

**Zero-shot** chỉ cung cấp instruction, không examples.

**One-shot** cung cấp một demonstration.

**Few-shot** cung cấp vài demonstrations để mô hình (model / 모델) infer tác vụ (task / 작업)/format.

Few-shot hữu ích khi tác vụ (task / 작업) khó mô tả bằng quy tắc (rule / 규칙) nhưng dễ minh họa bằng examples.

> **Chuyển mạch:** Ở chặng này của **In-Context học tập (learning / 학습)**, **Demonstrations làm gì?** tiếp nhận điểm tựa từ **Zero-shot, one-shot, few-shot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thứ tự (order / 순서) sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Demonstrations làm gì?

Demonstrations có thể truyền nhiều loại thông tin (information / 정보) cùng lúc:

- tác vụ (task / 작업) ánh xạ (mapping / 매핑);
- đầu ra (output / 출력) format;
- labels ngữ nghĩa (semantics / 의미론);
- tone/style;
- edge-case handling;
- lập luận (reasoning / 추론) mẫu (pattern / 패턴).

Vì vậy example chất lượng (quality / 품질) quan trọng hơn chỉ số lượng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **In-Context học tập (learning / 학습)**, **Thứ tự (order / 순서) sensitivity** tiếp nhận điểm tựa từ **Demonstrations làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Label ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ tự (order / 순서) sensitivity

ICL có thể sensitive với thứ tự examples. Recent examples đôi khi ảnh hưởng mạnh hơn, label imbalance có thể độ lệch (bias / 편향) đầu ra (output / 출력), và một bad demonstration có thể kéo mô hình (model / 모델) sai hướng.

Đây là lý do prompt eval cần kiểm thử (test / 테스트) multiple example sets, không chỉ một handcrafted prompt.

> **Chuyển mạch:** Trong **In-Context học tập (learning / 학습)**, **Thứ tự (order / 순서) sensitivity** cho ta quy tắc; **Label ngữ nghĩa (semantics / 의미론)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ngữ cảnh (context / 맥락) as temporary program** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Label ngữ nghĩa (semantics / 의미론)

Nếu labels là arbitrary strings như `A`, `B`, `C`, few-shot examples giúp mô hình (model / 모델) map ngữ nghĩa (semantic / 의미적) lớp (class / 클래스) sang label đơn vị từ (token / 토큰).

Nếu example labels sai, mô hình (model / 모델) có thể follow demonstration thay vì nội bộ (internal / 내부) prior.

ICL vì vậy vừa là năng lực (capability / 역량) vừa là attack surface: malicious ngữ cảnh (context / 맥락) có thể steer hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **In-Context học tập (learning / 학습)**, **Label ngữ nghĩa (semantics / 의미론)** cho ta quy tắc; **Ngữ cảnh (context / 맥락) as temporary program** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Why ICL emerges** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) as temporary program

Một mô hình tư duy (mental model / 사고 모델) hữu ích là xem prompt như một **temporary program**:

```text
instructions
+ examples
+ retrieved facts
+ tool outputs
→ temporary computation context
```

Mô hình (model / 모델) weights là trình thông dịch (interpreter / 인터프리터) learned; ngữ cảnh (context / 맥락) định nghĩa cục bộ (local / 로컬) tác vụ (task / 작업) trạng thái (state / 상태).

Analogy này không hoàn hảo vì LLM thực thi (execution / 실행) probabilistic và không có formal ngữ nghĩa (semantics / 의미론) như programming ngôn ngữ (language / 언어), nhưng hữu ích cho hệ thống (system / 시스템) thiết kế (design / 설계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **In-Context học tập (learning / 학습)**, **Why ICL emerges** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) as temporary program** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ICL vs Fine-Tuning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why ICL emerges

Trong pretraining, mô hình (model / 모델) quan sát rất nhiều văn bản (text / 텍스트) patterns nơi previous văn bản (text / 텍스트) defines cục bộ (local / 로컬) conventions: tutorials, examples, dialogues, mã (code / 코드), question-answer sequences. Transformer học dùng ngữ cảnh (context / 맥락) để predict next tokens under those cục bộ (local / 로컬) patterns.

Quy mô (scale / 규모) và tác vụ (task / 작업) diversity làm năng lực (capability / 역량) này mạnh hơn, nhưng chính xác (exact / 정확한) cơ chế (mechanism / 메커니즘) vẫn là active research topic. Không cần giả định mô hình (model / 모델) chạy hidden độ dốc (gradient / 기울기) descent để sử dụng ICL hiệu quả trong kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Trong **In-Context học tập (learning / 학습)**, **ICL vs Fine-Tuning** tiếp nhận điểm tựa từ **Why ICL emerges** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ICL vs RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ICL vs Fine-Tuning

ICL thích hợp khi tác vụ (task / 작업) thay đổi nhanh, examples ít, cần no-training triển khai (deployment / 배포) hoặc user-specific customization theo session.

Fine-tuning thích hợp khi hành vi (behavior / 동작) phải consistent trên rất nhiều requests và mẫu (pattern / 패턴) stable.

Sự đánh đổi (trade-off / 트레이드오프):

```text
ICL          → flexible, no weight update, consumes context tokens
Fine-tuning  → persistent behavior, training cost, less prompt overhead
```

> **Chuyển mạch:** Ở chặng này của **In-Context học tập (learning / 학습)**, **ICL vs RAG** tiếp nhận điểm tựa từ **ICL vs Fine-Tuning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) length is not free** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ICL vs RAG

RAG đưa bên ngoài (external / 외부) **kiến thức (knowledge / 지식)/bằng chứng (evidence / 증거)** vào ngữ cảnh (context / 맥락). ICL đưa examples/instructions để định nghĩa **tác vụ (task / 작업) hành vi (behavior / 동작)**.

Một RAG ứng dụng (application / 애플리케이션) có thể dùng cả hai:

```text
few-shot examples
+ retrieved documents
+ user query
→ answer
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **In-Context học tập (learning / 학습)**, **Ngữ cảnh (context / 맥락) length is not free** tiếp nhận điểm tựa từ **ICL vs RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động (dynamic / 동적) few-shot selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) length is not free

Few-shot examples consume ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) và suy luận (inference / 추론) chi phí (cost / 비용). Too many examples có thể dilute relevant thông tin (information / 정보) hoặc push important content ra khỏi cửa sổ (window / 윈도우).

Selection therefore becomes retrieval bài toán (problem / 문제): chọn demonstrations relevant nhất thay vì nhét toàn bộ examples.

> **Chuyển mạch:** Trong **In-Context học tập (learning / 학습)**, **Động (dynamic / 동적) few-shot selection** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) length is not free** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prompt contamination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động (dynamic / 동적) few-shot selection

Có thể embed người dùng (user / 사용자) truy vấn (query / 쿼리), retrieve similar labeled examples và insert chúng vào prompt. Đây là hybrid giữa retrieval và ICL.

Nhưng similarity không luôn đồng nghĩa examples tốt nhất. Sometimes diversity hoặc coverage quan trọng hơn nearest neighbor.

> **Chuyển mạch:** Ở chặng này của **In-Context học tập (learning / 학습)**, **Prompt contamination** tiếp nhận điểm tựa từ **Động (dynamic / 동적) few-shot selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ICL và lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prompt contamination

Retrieved/user-provided văn bản (text / 텍스트) có thể chứa instructions. Nếu ứng dụng (application / 애플리케이션) blindly mixes dữ liệu (data / 데이터) và instructions, mô hình (model / 모델) có thể follow untrusted content.

ICL năng lực (capability / 역량) chính là lý do **prompt injection** nguy hiểm: mô hình (model / 모델) naturally learns hành vi (behavior / 동작) from ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **In-Context học tập (learning / 학습)**, **ICL và lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Prompt contamination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ICL và lập luận (reasoning / 추론)

Few-shot lập luận (reasoning / 추론) examples có thể improve hiệu năng (performance / 성능) bằng cách demonstrate decomposition mẫu (pattern / 패턴). Nhưng mô hình (model / 모델) cũng có thể bản sao (copy / 복사) superficial style mà không internalize correct lô-gic (logic / 논리).

Evaluation cần check answer tính đúng đắn (correctness / 정확성), not presence of reasoning-like prose.

> **Chuyển mạch:** Trong **In-Context học tập (learning / 학습)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **ICL và lập luận (reasoning / 추론)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> In-context học tập (learning / 학습) là **temporary adaptation through ngữ cảnh (context / 맥락)**, không phải parameter cập nhật (update / 업데이트).

Mô hình (model / 모델) đọc prompt vừa như dữ liệu (data / 데이터) vừa như tác vụ (task / 작업) specification, vì vậy ngữ cảnh (context / 맥락) thiết kế (design / 설계) là một phần của programming AI hệ thống (system / 시스템).

> **Chuyển mạch:** Ở chặng này của **In-Context học tập (learning / 학습)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Few-shot examples train mô hình (model / 모델) ngay lúc suy luận (inference / 추론)”

Không có tiêu chuẩn (standard / 표준) weight cập nhật (update / 업데이트). hành vi (behavior / 동작) thay đổi (change / 변경) là ngữ cảnh (context / 맥락) conditioning.

### “Càng nhiều examples càng tốt”

Không. ngữ cảnh (context / 맥락) chi phí (cost / 비용), redundancy và conflicting examples có thể làm hiệu năng (performance / 성능) giảm.

### “Long ngữ cảnh (context / 맥락) thay thế fine-tuning”

Không. Persistent hành vi (behavior / 동작) và session-specific conditioning giải quyết different problems.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **In-Context học tập (learning / 학습)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

ICL nối [Pretraining](./04_pretraining.md), [Attention/Transformer](../06_deep_learning_architectures/04_attention.md), RAG và tác nhân (agent / 에이전트) ngữ cảnh (context / 맥락) management.

Xem tiếp: [Prompting and Context Engineering](./11_prompting_and_context_engineering.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
