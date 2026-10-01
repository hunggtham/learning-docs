# Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao SFT chưa đủ?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chuỗi xử lý (pipeline / 파이프라인) cổ điển** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**RLHF (Reinforcement Learning from Human Feedback / 인간 피드백 기반 강화학습)** là một family of post-training methods dùng human preference tín hiệu (signal / 신호) để làm mô hình (model / 모델) outputs phù hợp hơn với desired hành vi (behavior / 동작). Mục tiêu không phải “human cho biết fact nào đúng rồi mô hình (model / 모델) học thuộc”. RLHF thường học **preference thứ tự (ordering / 순서) giữa candidate responses** và dùng tín hiệu (signal / 신호) đó để cập nhật (update / 업데이트) chính sách (policy / 정책).

## Vì sao SFT chưa đủ?

SFT cần một mục tiêu (target / 대상) phản hồi (response / 응답) cụ thể. Nhưng nhiều prompts có nhiều answers đều acceptable ở mức khác nhau. Ta thường quan tâm preference mềm:

```text
response A hữu ích hơn B
A chính xác hơn B
A ít harmful hơn B
A concise hơn B
```

Human ranking chứa thông tin (information / 정보) mà single-target imitation không thể biểu diễn đầy đủ.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Vì sao SFT chưa đủ?** xác định đầu vào; **Chuỗi xử lý (pipeline / 파이프라인) cổ điển** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chính sách (policy / 정책) tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi xử lý (pipeline / 파이프라인) cổ điển

Một RLHF chuỗi xử lý (pipeline / 파이프라인) phổ biến gồm ba giai đoạn:

```text
1. SFT policy
2. collect preference pairs → train reward model
3. optimize policy against reward model with RL
```

### Preference dữ liệu (data / 데이터)

Với prompt `x`, mô hình (model / 모델) tạo candidates `y_a`, `y_b`. Human label chọn phản hồi (response / 응답) preferred:

\[
y_w \succ y_l
\]

trong đó `w` là winner và `l` là loser.

### Reward mô hình (model / 모델)

Reward mô hình (model / 모델) `r_\phi(x,y)` học score sao cho preferred answer có reward cao hơn. Một mục tiêu (objective / 목표) điển hình:

\[
\mathcal L_{RM}=-\log\sigma(r_\phi(x,y_w)-r_\phi(x,y_l))
\]

Reward mô hình (model / 모델) không phải oracle truth. Nó approximates preference phân phối (distribution / 분포) trong annotation dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Chuỗi xử lý (pipeline / 파이프라인) cổ điển** xác định đầu vào; **Chính sách (policy / 정책) tối ưu hóa (optimization / 최적화)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **PPO intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) tối ưu hóa (optimization / 최적화)

Chính sách (policy / 정책) LLM sau đó được optimized để maximize learned reward, nhưng nếu chỉ maximize reward mô hình (model / 모델) trực tiếp, mô hình (model / 모델) có thể exploit its imperfections. Vì vậy mục tiêu (objective / 목표) thường thêm penalty giữ chính sách (policy / 정책) gần tham chiếu (reference / 참조) mô hình (model / 모델):

\[
\max_\theta \; \mathbb E[r_\phi(x,y)] - \beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

KL term hạn chế chính sách (policy / 정책) drift quá xa khỏi mô hình (model / 모델) đã có ngôn ngữ (language / 언어) chất lượng (quality / 품질) tốt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **PPO intuition** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reward hacking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PPO intuition

**Proximal chính sách (policy / 정책) tối ưu hóa (optimization / 최적화) (PPO)** từng là thuật toán (algorithm / 알고리즘) phổ biến cho RLHF. PPO giới hạn cập nhật (update / 업데이트) quá lớn giữa chính sách (policy / 정책) mới và cũ để huấn luyện (training / 학습) ổn định hơn.

Trong LLM setting, “hành động (action / 동작)” là generated đơn vị từ (token / 토큰) và trajectory là phản hồi (response / 응답) chuỗi (sequence / 시퀀스). Reward thường đến ở cuối chuỗi (sequence / 시퀀스) hoặc qua learned tín hiệu (signal / 신호).

Điều này làm credit assignment khó: reward tổng cho cả phản hồi (response / 응답) không nói rõ đơn vị từ (token / 토큰) nào đóng góp bao nhiêu.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Reward hacking** tiếp nhận điểm tựa từ **PPO intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Preference không bằng truth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reward hacking

Nếu reward mô hình (model / 모델) có blind spot, chính sách (policy / 정책) có thể tìm đầu ra (output / 출력) score cao nhưng human không thực sự thích. Đây là **reward hacking / specification gaming**.

Ví dụ nếu reward mô hình (model / 모델) correlate verbosity với helpfulness, chính sách (policy / 정책) có thể tạo answer dài không cần thiết chỉ để tăng reward.

Đây là general lesson của tối ưu hóa (optimization / 최적화):

> Optimizer sẽ tối ưu **chỉ số (metric / 지표) được cho**, không phải mục tiêu trong đầu designer.

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, sau nội dung của **Reward hacking**, **Preference không bằng truth** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Annotation thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Preference không bằng truth

Human annotators có thể disagree, thiếu lĩnh vực (domain / 도메인) expertise hoặc bị ảnh hưởng wording. Reward mô hình (model / 모델) phản ánh annotation tiến trình (process / 프로세스).

Vì vậy RLHF có thể cải thiện helpfulness/style nhưng không guarantee factual tính đúng đắn (correctness / 정확성).

Grounding, retrieval và xác minh (verification / 확인) vẫn cần thiết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Annotation thiết kế (design / 설계)** tiếp nhận điểm tựa từ **Preference không bằng truth** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Helpful, Honest, Harmless là multi-objective** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Annotation thiết kế (design / 설계)

Preference guideline ảnh hưởng mô hình (model / 모델) hành vi (behavior / 동작) rất mạnh. Nếu labelers được yêu cầu ưu tiên concise answers, mô hình (model / 모델) sẽ học concise preference. Nếu an toàn (safety / 안전) chính sách (policy / 정책) mơ hồ, labels inconsistent.

Inter-annotator disagreement là tín hiệu (signal / 신호) quan trọng: bài toán (problem / 문제) có thể subjective hoặc guideline chưa đủ rõ.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Helpful, Honest, Harmless là multi-objective** tiếp nhận điểm tựa từ **Annotation thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Online vs offline preference tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Helpful, Honest, Harmless là multi-objective

Một assistant thường phải balance nhiều objectives. Helpfulness và harmlessness đôi khi xung đột (conflict / 충돌); honesty có thể yêu cầu mô hình (model / 모델) thừa nhận bất định (uncertainty / 불확실성) thay vì đưa answer decisive.

Không có một scalar reward hoàn hảo biểu diễn mọi giá trị (value / 값). Practical các hệ thống (systems / 시스템들) dùng mixtures, policies và separate evaluations.

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, sau nội dung của **Helpful, Honest, Harmless là multi-objective**, **Online vs offline preference tối ưu hóa (optimization / 최적화)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **RLHF và an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Online vs offline preference tối ưu hóa (optimization / 최적화)

Classical RLHF có mô hình (model / 모델) generate new trajectories trong vòng lặp (loop / 루프), nên phân phối (distribution / 분포) thay đổi khi chính sách (policy / 정책) cập nhật (update / 업데이트). Đây là online/on-policy flavor.

Các methods như DPO có thể optimize trực tiếp trên offline preference pairs mà không cần tường minh (explicit / 명시적) reward-model + PPO vòng lặp (loop / 루프).

Xem tiếp: [Preference Optimization and DPO](./09_preference_optimization_and_dpo.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **RLHF và an toàn (safety / 안전)** tiếp nhận điểm tựa từ **Online vs offline preference tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KL penalty như stability ràng buộc (constraint / 제약조건)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RLHF và an toàn (safety / 안전)

An toàn (safety / 안전) preference dữ liệu (data / 데이터) có thể dạy refusal, safe completion và chính sách (policy / 정책) adherence. Nhưng mô hình (model / 모델) vẫn có thể bị jailbreak vì huấn luyện (training / 학습) phân phối (distribution / 분포) không cover mọi adversarial prompt.

Thời gian chạy (runtime / 런타임) defenses, đầu vào (input / 입력)/đầu ra (output / 출력) filters, công cụ (tool / 도구) permission boundaries và red teaming là system-level layers bổ sung.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **KL penalty như stability ràng buộc (constraint / 제약조건)** tiếp nhận điểm tựa từ **RLHF và an toàn (safety / 안전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reward mô hình (model / 모델) overoptimization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KL penalty như stability ràng buộc (constraint / 제약조건)

Nếu reward tối ưu hóa (optimization / 최적화) quá mạnh, mô hình (model / 모델) có thể mất fluency hoặc collapse vào weird high-reward outputs. KL penalty giữ phân phối (distribution / 분포) gần tham chiếu (reference / 참조).

`β` lớn → chính sách (policy / 정책) conservative.

`β` nhỏ → chính sách (policy / 정책) có thể move aggressively theo reward.

Đây là một trust-region-like sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Reward mô hình (model / 모델) overoptimization** tiếp nhận điểm tựa từ **KL penalty như stability ràng buộc (constraint / 제약조건)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reward mô hình (model / 모델) overoptimization

Khi optimize chính sách (policy / 정책) ngày càng mạnh against fixed reward mô hình (model / 모델), actual human preference có thể tăng lúc đầu rồi giảm khi chính sách (policy / 정책) exploit imperfections.

Do đó reward-model score không nên là only evaluation after huấn luyện (training / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Reward mô hình (model / 모델) overoptimization** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Human preferences
      ↓
learned preference signal
      ↓
optimize policy
      ↓
assistant behavior shifts
```

RLHF là **hành vi (behavior / 동작) alignment under imperfect preference đo lường (measurement / 측정)**, không phải “upload human values vào mô hình (model / 모델)”.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “RLHF làm mô hình (model / 모델) biết facts đúng hơn”

Có thể gián tiếp cải thiện honesty, nhưng factual kiến thức (knowledge / 지식) chủ yếu đến từ pretraining/retrieval; reward tối ưu hóa (optimization / 최적화) không biến preference labels thành complete world mô hình (model / 모델).

### “Reward mô hình (model / 모델) chính là human judgment”

Không. Nó là learned approximation có độ lệch (bias / 편향)/lỗi (error / 오류).

### “RLHF = PPO”

PPO là một tối ưu hóa (optimization / 최적화) choice. RLHF rộng hơn và preference tối ưu hóa (optimization / 최적화) có nhiều alternatives.

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) from Human phản hồi (feedback / 피드백) (RLHF)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

RLHF là ứng dụng của [Reinforcement Learning](../11_reinforcement_learning/00_reinforcement_learning_foundations.md) và [Optimization](../01_mathematical_foundations/06_optimization.md), nhưng practical LLM post-training có cấu trúc (structure / 구조) riêng vì hành động (action / 동작) không gian (space / 공간) là đơn vị từ (token / 토큰) sequences và reward learned from preferences.

Xem tiếp: [DPO](./09_preference_optimization_and_dpo.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
