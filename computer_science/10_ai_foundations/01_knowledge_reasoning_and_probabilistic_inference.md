# Knowledge representation, reasoning và probabilistic inference

AI system cần representation cho facts, relations và uncertainty. Nếu representation không phù hợp, reasoning trở nên impossible hoặc quá đắt. Knowledge representation nghiên cứu cách encode world model để inference tạo ra conclusions/actions hữu ích.

## Symbols và propositions

Propositional logic biểu diễn facts dạng true/false và connectives. First-order logic thêm objects, predicates, variables và quantifiers, cho representation giàu hơn.

Ví dụ `Human(x) -> Mortal(x)` và `Human(Socrates)` cho phép infer `Mortal(Socrates)` bằng logical rules.

Logic cho guarantees mạnh nhưng world thực thường incomplete/noisy.

## Knowledge graph

Graph biểu diễn entities làm nodes và relations làm edges. Knowledge graph hữu ích cho entity linking, recommendation, search và reasoning path.

Nhưng graph lưu facts không tự tạo truth. Provenance, identity resolution và temporal validity vẫn quan trọng.

## Rules và inference engines

Forward chaining bắt đầu từ known facts và áp dụng rules để derive facts mới. Backward chaining bắt đầu từ query/goal và tìm rules có thể support nó.

Prolog-style reasoning dùng unification/backtracking. Expert systems lịch sử dựa nhiều rule-based inference.

Rule systems explainable trong domain hẹp nhưng maintenance khó khi rules tương tác phức tạp.

## Uncertainty

Nếu sensor nói “mưa” với 80% reliability, binary logic không mô tả uncertainty tốt. Probability cung cấp calculus để update beliefs.

Bayes theorem:

\[
P(H|E)=\frac{P(E|H)P(H)}{P(E)}
\]

kết hợp prior belief và evidence likelihood.

## Bayesian networks

Bayesian network là directed acyclic graph nơi nodes là random variables và edges biểu diễn conditional dependencies. Factorization giảm need lưu full joint distribution khi conditional independence hợp lý.

Structure của graph là modeling assumption, không phải fact tự động.

## Hidden variables và sequence models

Hidden Markov Model có hidden states tạo observations theo sequence. Forward/Viterbi algorithms dùng dynamic programming để infer likelihood hoặc most likely state path.

Speech, bioinformatics và tracking dùng family ideas này, dù deep learning đã thay nhiều implementations.

## Approximate inference

Exact inference có thể exponential trên graph structure. Sampling/MCMC, variational methods hoặc loopy belief propagation approximate posterior.

Đây là same pattern như approximation algorithms: exact answer có thể computationally intractable, nên ta trade accuracy/resource.

## Causal reasoning khác correlation

Probabilistic association `P(Y|X)` không tự động cho intervention effect `P(Y|do(X))`. Causal models thêm assumptions về data-generating structure.

AI/data systems ra decision cần cẩn thận không coi prediction correlation thành causal prescription.

## Common Misconceptions

**“Knowledge graph là database graph nên suy luận tự xảy ra.”** Storage structure và inference semantics là hai tầng khác.

**“Bayes theorem làm prior không quan trọng khi data nhiều.”** Tùy model/data; prior influence giảm trong một số regimes nhưng modeling assumptions vẫn quyết định.

**“Probability là degree of truth duy nhất.”** Nó thường biểu diễn uncertainty/belief frequency tùy interpretation, không thay logical semantics mọi domain.

## Mental Model

> Representation quyết định câu hỏi nào có thể hỏi hiệu quả. Logic xử lý entailment dưới rules; probability xử lý uncertainty dưới distribution assumptions.

## Kết nối

Đọc [logic/proof](../../mathematics/00_foundations/01_logic_and_proof.md), [conditional probability/Bayes](../../mathematics/06_probability_statistics/02_conditional_probability_and_bayes.md) và [AI search/agents](./00_ai_problem_formulation_search_and_agents.md).