# Instruction Tuning

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Instruction tuning**. Route đi từ language-model continuation → instruction/response format → task mixture and supervision → generalization to unseen prompts → alignment trade-offs, để dữ liệu hướng dẫn được nối với hành vi mong muốn.

Cơ sở (base / 기반) LLM được pretrain để **tiếp tục văn bản (text / 텍스트)**, nhưng người dùng (user / 사용자) muốn một assistant có thể hiểu yêu cầu (request / 요청) và tạo phản hồi (response / 응답) phù hợp. **Instruction tuning (지시 튜닝 / tinh chỉnh theo chỉ dẫn)** là quá trình điều chỉnh mô hình (model / 모델) để map từ instruction + ngữ cảnh (context / 맥락) sang desired phản hồi (response / 응답) format và hành vi (behavior / 동작).

Điểm quan trọng là instruction tuning không “dạy toàn bộ kiến thức mới”. Phần lớn broad kiến thức (knowledge / 지식) và ngôn ngữ (language / 언어) năng lực (capability / 역량) đã được hình thành trong pretraining. Post-training thay đổi cách mô hình (model / 모델) **sử dụng** năng lực (capability / 역량) đó theo tương tác (interaction / 상호작용) mẫu (pattern / 패턴) mong muốn.

## Từ continuation tới instruction following

Pretraining mục tiêu (objective / 목표):

\[
P(x_t\mid x_{<t})
\]

không phân biệt ngữ nghĩa (semantic / 의미적) role như hệ thống (system / 시스템), người dùng (user / 사용자) hay assistant trừ khi những mẫu (pattern / 패턴) đó xuất hiện trong dữ liệu (data / 데이터).

Instruction dataset đưa cấu trúc (structure / 구조) rõ hơn:

```text
Instruction: Explain recursion simply.
Response: ...
```

hoặc chat format:

```text
system → policy/context
user   → request
assistant → desired answer
```

Mô hình (model / 모델) học rằng một số đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스) đóng vai trò instruction và đầu ra (output / 출력) nên theo các ràng buộc (constraints / 제약조건들) đó.

Từ cách mô hình nhận diện instruction, ta chuyển sang câu hỏi về dữ liệu: những ví dụ nào giúp nó học được hành vi đó một cách nhất quán?

## Instruction dữ liệu (data / 데이터)

Instruction dữ liệu (data / 데이터) có thể đến từ human-written examples, synthetic generation, transformed datasets hoặc mixtures của nhiều tasks. chất lượng (quality / 품질) quan trọng hơn việc chỉ tăng số lượng.

Một example tốt không chỉ có “đáp án đúng”; nó thể hiện format, độ sâu (depth / 깊이), tone, refusal ranh giới (boundary / 경계), tool-use lược đồ (schema / 스키마) hoặc lập luận (reasoning / 추론) style cần thiết.

Nếu dataset inconsistent, mô hình (model / 모델) học phân phối (distribution / 분포) inconsistent.

Vì dữ liệu đặt ra khuôn mẫu đầu vào–đầu ra, độ đa dạng của tác vụ quyết định mô hình có học được nguyên tắc hay chỉ ghi nhớ cách diễn đạt.

## Tác vụ (task / 작업) diversity và generalization

Instruction tuning hữu ích vì mô hình (model / 모델) có thể generalize từ many tác vụ (task / 작업) templates sang instruction mới. Nếu huấn luyện (training / 학습) chỉ có narrow templates, mô hình (model / 모델) có thể overfit phrasing.

Diversity giúp mô hình (model / 모델) học meta-pattern:

> văn bản (text / 텍스트) trước mô tả intent/các ràng buộc (constraints / 제약조건들); văn bản (text / 텍스트) sau phải satisfy intent/các ràng buộc (constraints / 제약조건들).

Đây là một dạng learned giao diện (interface / 인터페이스) giữa human ngôn ngữ (language / 언어) và mô hình (model / 모델) năng lực (capability / 역량).

Khi instruction đã được hiểu như một giao diện giữa người dùng và năng lực của mô hình, cần phân biệt rõ vai trò của từng bên trong cuộc hội thoại.

## Hệ thống (system / 시스템)/người dùng (user / 사용자)/Assistant roles

Hiện đại (modern / 현대적) chat các hệ thống (systems / 시스템들) thường encode role tokens hoặc special formatting. Role hierarchy không phải thuộc tính (property / 속성) tự nhiên của ngôn ngữ (language / 언어) mô hình (model / 모델); nó là hành vi (behavior / 동작) được tạo bởi huấn luyện (training / 학습), serving giao thức (protocol / 프로토콜) và thời gian chạy (runtime / 런타임) chính sách (policy / 정책).

Vì vậy prompt injection là system-level bài toán (problem / 문제): mô hình (model / 모델) đang đọc nhiều văn bản (text / 텍스트) streams nhưng ứng dụng (application / 애플리케이션) muốn một số streams có authority cao hơn streams khác.

Phân biệt hành vi với kiến thức cũng dẫn tới một rủi ro khác: thay đổi mô hình quá mạnh có thể làm suy giảm năng lực đã có.

## Instruction tuning và kiến thức (knowledge / 지식)

Fine-tuning có thể inject some lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식), nhưng đây không phải always best công cụ (tool / 도구). Nếu kiến thức (knowledge / 지식) thay đổi thường xuyên hoặc cần provenance, retrieval thường phù hợp hơn.

Use instruction tuning khi muốn thay đổi **hành vi (behavior / 동작) ánh xạ (mapping / 매핑)**, ví dụ:

```text
input schema → structured JSON
support ticket → classification + explanation
question → answer theo policy/domain style
```

Use RAG khi muốn cung cấp facts/document ngữ cảnh (context / 맥락) fresh và traceable.

Để giảm rủi ro mất năng lực khi fine-tune, ta thường phối hợp nhiều nhiệm vụ thay vì chỉ tối ưu một tập hẹp.

## Catastrophic forgetting

Nếu fine-tune quá mạnh trên narrow dữ liệu (data / 데이터), mô hình (model / 모델) có thể mất năng lực (capability / 역량) hoặc style rộng trước đó. Mitigation gồm lower học tập (learning / 학습) tỷ lệ (rate / 비율), dữ liệu (data / 데이터) mixture, regularization và parameter-efficient tuning.

Multi-task training mở rộng độ phủ, nhưng thường cần thêm dữ liệu để đạt quy mô mong muốn; đó là lý do synthetic instruction data trở thành một lựa chọn cần đánh giá thận trọng.

## Multi-task instruction tuning

Một mô hình (model / 모델) có thể train trên translation, summarization, QA, extraction, coding và dialogue cùng lúc. dùng chung (shared / 공유) biểu diễn (representation / 표현) cho phép transfer giữa tasks.

Nhưng tác vụ (task / 작업) mixture cần weighting. Dataset lớn nhưng easy có thể dominate độ dốc (gradient / 기울기) và làm hard/rare tác vụ (task / 작업) bị underrepresented.

Synthetic data giúp mở rộng tập huấn luyện, còn phần tiếp theo đặt nó vào đúng quan hệ với SFT để tránh đồng nhất hai khái niệm.

## Synthetic instruction dữ liệu (data / 데이터)

Stronger mô hình (model / 모델) có thể generate instruction-response pairs cho weaker/open mô hình (model / 모델). Điều này quy mô (scale / 규모) nhanh nhưng có nguy cơ propagate errors, stylistic artifacts và blind spots của teacher.

Synthetic dữ liệu (data / 데이터) cần filtering/evaluation thay vì assume teacher đầu ra (output / 출력) là ground truth.

SFT là phương pháp huấn luyện thường dùng cho instruction tuning, nhưng việc làm theo instruction vẫn chưa đồng nghĩa với alignment đầy đủ.

## Instruction tuning vs SFT

Hai thuật ngữ overlap nhiều. **Supervised Fine-Tuning (SFT)** mô tả học tập (learning / 학습) procedure dùng labeled input-output pairs. **Instruction tuning** mô tả loại hành vi (behavior / 동작)/dữ liệu (data / 데이터): examples có instruction ngữ nghĩa (semantics / 의미론).

Instruction tuning thường được thực hiện bằng SFT, nhưng SFT cũng có thể dùng cho tác vụ (task / 작업) không phải natural-language instruction.

Xem tiếp: [Supervised Fine-Tuning](./07_supervised_fine_tuning.md).

Những giới hạn đó biểu hiện rõ trong các quyết định từ chối: hệ thống có thể từ chối quá nhiều hoặc bỏ sót yêu cầu không an toàn.

## Instruction following không bằng alignment hoàn chỉnh

Mô hình (model / 모델) có thể follow instruction rất tốt nhưng vẫn:

- hallucinate;
- follow malicious instruction;
- violate an toàn (safety / 안전) chính sách (policy / 정책);
- optimize wording thay vì intent;
- thất bại (fail / 실패) under conflicting instructions.

Preference huấn luyện (training / 학습) và thời gian chạy (runtime / 런타임) an toàn (safety / 안전) layers thường được thêm sau.

Đánh giá refusal cần đi cùng đánh giá đầu ra hợp lệ nói chung, vì định dạng cũng là một phần của hành vi mà instruction tuning có thể dạy.

## Over-refusal và under-refusal

Post-training an toàn (safety / 안전) có sự đánh đổi (trade-off / 트레이드오프). Nếu refusal examples quá rộng, mô hình (model / 모델) có thể từ chối benign requests. Nếu quá hẹp, harmful transformations có thể bypass.

Evaluation phải đo cả helpfulness lẫn appropriate refusal, không chỉ một phía.

Khi đã tách hành vi sinh ra từ mô hình khỏi lớp kiểm tra định dạng bên ngoài, ta có thể chốt lại toàn bộ cơ chế bằng một mô hình tư duy ngắn gọn.

## Formatting as hành vi (behavior / 동작)

Instruction tuning có thể dạy structured đầu ra (output / 출력) như JSON/XML/công cụ (tool / 도구) lời gọi (call / 호출). Tuy nhiên generation vẫn probabilistic. Nếu đầu ra (output / 출력) phải syntactically valid tuyệt đối, constrained decoding hoặc lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) nên bổ sung.

Mô hình (model / 모델) hành vi (behavior / 동작) và deterministic kiểm tra hợp lệ (validation / 검증) là hai layers khác nhau.

Mô hình tư duy này giúp kiểm tra những diễn giải dễ nhầm trước khi nối instruction tuning với các bước hậu huấn luyện tiếp theo.

## Mô hình tư duy (mental model / 사고 모델)

> Pretraining tạo **general năng lực (capability / 역량)**; instruction tuning tạo **tương tác (interaction / 상호작용) giao thức (protocol / 프로토콜)** để năng lực (capability / 역량) đó phục vụ yêu cầu (request / 요청) theo cách hữu ích hơn.

Các ngộ nhận trên đều quy instruction tuning thành thứ nó không làm được; phần liên kết kiến thức dưới đây đặt nó cạnh SFT, RLHF và DPO theo đúng ranh giới.

## Dùng chung (common / 공통) Misconceptions

### “Fine-tune là cách tốt nhất để cập nhật facts mới”

Không nhất thiết. Retrieval có freshness/provenance tốt hơn cho kiến thức (knowledge / 지식) động (dynamic / 동적).

### “Instruction tuning làm mô hình (model / 모델) hiểu mọi instruction”

Nó cải thiện generalization nhưng vẫn phụ thuộc phân phối (distribution / 분포), ngữ cảnh (context / 맥락) độ phức tạp (complexity / 복잡도) và conflicting các ràng buộc (constraints / 제약조건들).

### “Role hierarchy là hard-coded truth trong Transformer”

Role ngữ nghĩa (semantics / 의미론) đến từ huấn luyện (training / 학습) format và thời gian chạy (runtime / 런타임) hệ thống (system / 시스템), không phải attention tự nhiên biết hệ thống (system / 시스템) message có authority cao hơn.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Instruction tuning nối pretraining với assistant hành vi (behavior / 동작). Sau SFT, preference tối ưu hóa (optimization / 최적화) như RLHF/DPO tiếp tục điều chỉnh đầu ra (output / 출력) theo human preferences và chính sách (policy / 정책).

Xem tiếp: [Supervised Fine-Tuning](./07_supervised_fine_tuning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
