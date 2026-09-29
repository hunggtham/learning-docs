# Kiến thức (knowledge / 지식) biểu diễn (representation / 표현), lập luận (reasoning / 추론) và probabilistic suy luận (inference / 추론)

> **Mạch đọc:** Đọc **kiến thức (knowledge / 지식) biểu diễn (representation / 표현), lập luận (reasoning / 추론) và probabilistic suy luận (inference / 추론)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Symbols và propositions** sang **kiến thức (knowledge / 지식) đồ thị (graph / 그래프)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


AI hệ thống (system / 시스템) cần biểu diễn (representation / 표현) cho facts, relations và bất định (uncertainty / 불확실성). Nếu biểu diễn (representation / 표현) không phù hợp, lập luận (reasoning / 추론) trở nên impossible hoặc quá đắt. kiến thức (knowledge / 지식) biểu diễn (representation / 표현) nghiên cứu cách encode world mô hình (model / 모델) để suy luận (inference / 추론) tạo ra conclusions/actions hữu ích.

## Symbols và propositions

Propositional lô-gic (logic / 논리) biểu diễn facts dạng true/false và connectives. First-order lô-gic (logic / 논리) thêm objects, predicates, variables và quantifiers, cho biểu diễn (representation / 표현) giàu hơn.

Ví dụ `Human(x) -> Mortal(x)` và `Human(Socrates)` cho phép infer `Mortal(Socrates)` bằng logical rules.

Lô-gic (logic / 논리) cho guarantees mạnh nhưng world thực thường incomplete/noisy.


> **Chuyển mạch:** Từ **Symbols và propositions**, ta sang **kiến thức (knowledge / 지식) đồ thị (graph / 그래프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kiến thức (knowledge / 지식) đồ thị (graph / 그래프)

Đồ thị (graph / 그래프) biểu diễn entities làm nodes và relations làm edges. kiến thức (knowledge / 지식) đồ thị (graph / 그래프) hữu ích cho thực thể (entity / 엔터티) linking, recommendation, tìm kiếm (search / 검색) và lập luận (reasoning / 추론) đường dẫn (path / 경로).

Nhưng đồ thị (graph / 그래프) lưu facts không tự tạo truth. Provenance, định danh (identity / 식별자) resolution và temporal validity vẫn quan trọng.


> **Chuyển mạch:** Từ **kiến thức (knowledge / 지식) đồ thị (graph / 그래프)**, ta sang **Rules và suy luận (inference / 추론) engines** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Rules và suy luận (inference / 추론) engines

Forward chaining bắt đầu từ known facts và áp dụng rules để derive facts mới. Backward chaining bắt đầu từ truy vấn (query / 쿼리)/goal và tìm rules có thể hỗ trợ (support / 지원) nó.

Prolog-style lập luận (reasoning / 추론) dùng unification/backtracking. Expert các hệ thống (systems / 시스템들) lịch sử dựa nhiều rule-based suy luận (inference / 추론).

Quy tắc (rule / 규칙) các hệ thống (systems / 시스템들) explainable trong lĩnh vực (domain / 도메인) hẹp nhưng maintenance khó khi rules tương tác phức tạp.


> **Chuyển mạch:** Từ **Rules và suy luận (inference / 추론) engines**, ta sang **bất định (uncertainty / 불확실성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bất định (uncertainty / 불확실성)

Nếu sensor nói “mưa” với 80% độ tin cậy (reliability / 신뢰성), nhị phân (binary / 이진) lô-gic (logic / 논리) không mô tả bất định (uncertainty / 불확실성) tốt. xác suất (probability / 확률) cung cấp calculus để cập nhật (update / 업데이트) beliefs.

Bayes theorem:

\[
P(H|E)=\frac{P(E|H)P(H)}{P(E)}
\]

kết hợp prior belief và bằng chứng (evidence / 증거) likelihood.


> **Chuyển mạch:** Từ **bất định (uncertainty / 불확실성)**, ta sang **Bayesian networks** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bayesian networks

Bayesian mạng (network / 네트워크) là directed acyclic đồ thị (graph / 그래프) nơi nodes là random variables và edges biểu diễn conditional dependencies. Factorization giảm need lưu full joint phân phối (distribution / 분포) khi conditional independence hợp lý.

Cấu trúc (structure / 구조) của đồ thị (graph / 그래프) là modeling giả định (assumption / 가정), không phải fact tự động.


> **Chuyển mạch:** Từ **Bayesian networks**, ta sang **Hidden variables và chuỗi (sequence / 시퀀스) các mô hình (models / 모델들)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hidden variables và chuỗi (sequence / 시퀀스) các mô hình (models / 모델들)

Hidden Markov mô hình (model / 모델) có hidden states tạo observations theo chuỗi (sequence / 시퀀스). Forward/Viterbi algorithms dùng động (dynamic / 동적) programming để infer likelihood hoặc most likely trạng thái (state / 상태) đường dẫn (path / 경로).

Speech, bioinformatics và tracking dùng family ideas này, dù deep học tập (learning / 학습) đã thay nhiều implementations.


> **Chuyển mạch:** Từ **Hidden variables và chuỗi (sequence / 시퀀스) các mô hình (models / 모델들)**, ta sang **Approximate suy luận (inference / 추론)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Approximate suy luận (inference / 추론)

Chính xác (exact / 정확한) suy luận (inference / 추론) có thể exponential trên đồ thị (graph / 그래프) cấu trúc (structure / 구조). Sampling/MCMC, variational methods hoặc loopy belief propagation approximate posterior.

Đây là same mẫu (pattern / 패턴) như approximation algorithms: chính xác (exact / 정확한) answer có thể computationally intractable, nên ta trade accuracy/tài nguyên (resource / 자원).


> **Chuyển mạch:** Từ **Approximate suy luận (inference / 추론)**, ta sang **lập luận nhân quả (causal reasoning / 인과적 추론) khác correlation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lập luận nhân quả (causal reasoning / 인과적 추론) khác correlation

Probabilistic association `P(Y|X)` không tự động cho intervention tác động (effect / 효과) `P(Y|do(X))`. nhân quả (causal / 인과적) các mô hình (models / 모델들) thêm các giả định (assumptions / 가정들) về data-generating cấu trúc (structure / 구조).

AI/dữ liệu (data / 데이터) các hệ thống (systems / 시스템들) ra quyết định (decision / 결정) cần cẩn thận không coi prediction correlation thành nhân quả (causal / 인과적) prescription.


> **Chuyển mạch:** Từ **lập luận nhân quả (causal reasoning / 인과적 추론) khác correlation**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“kiến thức (knowledge / 지식) đồ thị (graph / 그래프) là cơ sở dữ liệu (database / 데이터베이스) đồ thị (graph / 그래프) nên suy luận tự xảy ra.”** lưu trữ (storage / 저장소) cấu trúc (structure / 구조) và suy luận (inference / 추론) ngữ nghĩa (semantics / 의미론) là hai tầng khác.

**“Bayes theorem làm prior không quan trọng khi dữ liệu (data / 데이터) nhiều.”** Tùy mô hình (model / 모델)/dữ liệu (data / 데이터); prior influence giảm trong một số regimes nhưng modeling các giả định (assumptions / 가정들) vẫn quyết định.

**“xác suất (probability / 확률) là degree of truth duy nhất.”** Nó thường biểu diễn bất định (uncertainty / 불확실성)/belief frequency tùy interpretation, không thay logical ngữ nghĩa (semantics / 의미론) mọi lĩnh vực (domain / 도메인).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> biểu diễn (representation / 표현) quyết định câu hỏi nào có thể hỏi hiệu quả. lô-gic (logic / 논리) xử lý entailment dưới rules; xác suất (probability / 확률) xử lý bất định (uncertainty / 불확실성) dưới phân phối (distribution / 분포) các giả định (assumptions / 가정들).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [logic/proof](../../../mathematics/00_foundations/01_logic_and_proof.md), [conditional probability/Bayes](../../../mathematics/06_probability_statistics/02_conditional_probability_and_bayes.md) và [AI search/agents](./00_ai_problem_formulation_search_and_agents.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 ai problem formulation search and agents](./00_ai_problem_formulation_search_and_agents.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
