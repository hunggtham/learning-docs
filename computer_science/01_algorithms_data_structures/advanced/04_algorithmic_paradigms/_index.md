# 04_algorithmic_paradigms

> **Mạch đọc:** Đọc **04algorithmicparadigms** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.

Nhóm này tập trung vào các cách tổ chức quá trình giải bài toán: tìm kiếm, sắp xếp, phân rã, greedy, DP, tối ưu hóa (optimization / 최적화) và tìm kiếm (search / 검색) trên không gian trạng thái.

- `00_searching.md` — tuyến tính (linear / 선형)/tìm kiếm nhị phân (binary search / 이진 탐색), monotonic predicate và tìm kiếm (search / 검색) over answer.
- `01_sorting.md` — comparison/non-comparison sort, hybrid/adaptive/bên ngoài (external / 외부) sorting và chi phí (cost / 비용) mô hình (model / 모델).
- `02_recursion_and_backtracking.md` — recursion contracts, backtracking, pruning và state-space tìm kiếm (search / 검색).
- `03_divide_and_conquer.md` — recurrence, công việc (work / 작업)/span, cache-oblivious và các decomposition patterns.
- `04_greedy_algorithms.md` — exchange argument, cut thuộc tính (property / 속성), scheduling, Huffman và greedy tính đúng đắn (correctness / 정확성).
- `05_dynamic_programming.md` — trạng thái (state / 상태) thiết kế (design / 설계), chuyển tiếp (transition / 전이), top-down/bottom-up, tối ưu hóa (optimization / 최적화) và reconstruction.
- `06_selection_and_top_k.md` — Quickselect, Median-of-Medians, vùng nhớ động (heap / 힙)/partial sorting và phân tán (distributed / 분산) Top-K.
- `07_two_pointers_sliding_window_prefix_difference.md` — monotonic cửa sổ (window / 윈도우), prefix trạng thái (state / 상태) và difference/sự kiện (event / 이벤트) techniques.
- `08_intervals_and_sweep_line.md` — interval ngữ nghĩa (semantics / 의미론), sweep-line active set, hình học (geometry / 기하학) và temporal applications.
- `09_hard_problems_reductions_and_approximation.md` — reductions, NP landscape, FPT, approximation và solver-based methods.
- `10_greedy_matroids_primal_dual_and_approximation.md` — matroid exchange, primal–dual, submodular greedy, approximation và online greedy.
- `11_constraint_search_branch_and_bound.md` — CSP, propagation, MRV/LCV, symmetry breaking, Branch-and-Bound, relaxation, alpha-beta và SAT-style tìm kiếm (search / 검색) ideas.

Hai chapter cuối mở rộng các paradigm cốt lõi: `10_...` giải thích **vì sao** greedy đúng hoặc vẫn hữu ích khi chỉ có approximation guarantee; `11_...` giải thích cách một cây backtracking thô được biến thành solver có propagation, bound và certificate.

> **Bàn giao:** Sau **04algorithmicparadigms**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 searching](./00_searching.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
