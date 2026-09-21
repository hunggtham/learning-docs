# 04_algorithmic_paradigms

Nhóm này tập trung vào các cách tổ chức quá trình giải bài toán: tìm kiếm, sắp xếp, phân rã, greedy, DP, optimization và search trên không gian trạng thái.

- `00_searching.md` — linear/binary search, monotonic predicate và search over answer.
- `01_sorting.md` — comparison/non-comparison sort, hybrid/adaptive/external sorting và cost model.
- `02_recursion_and_backtracking.md` — recursion contracts, backtracking, pruning và state-space search.
- `03_divide_and_conquer.md` — recurrence, work/span, cache-oblivious và các decomposition patterns.
- `04_greedy_algorithms.md` — exchange argument, cut property, scheduling, Huffman và greedy correctness.
- `05_dynamic_programming.md` — state design, transition, top-down/bottom-up, optimization và reconstruction.
- `06_selection_and_top_k.md` — Quickselect, Median-of-Medians, heap/partial sorting và distributed Top-K.
- `07_two_pointers_sliding_window_prefix_difference.md` — monotonic window, prefix state và difference/event techniques.
- `08_intervals_and_sweep_line.md` — interval semantics, sweep-line active set, geometry và temporal applications.
- `09_hard_problems_reductions_and_approximation.md` — reductions, NP landscape, FPT, approximation và solver-based methods.
- `10_greedy_matroids_primal_dual_and_approximation.md` — matroid exchange, primal–dual, submodular greedy, approximation và online greedy.
- `11_constraint_search_branch_and_bound.md` — CSP, propagation, MRV/LCV, symmetry breaking, Branch-and-Bound, relaxation, alpha-beta và SAT-style search ideas.

Hai chapter cuối mở rộng các paradigm cốt lõi: `10_...` giải thích **vì sao** greedy đúng hoặc vẫn hữu ích khi chỉ có approximation guarantee; `11_...` giải thích cách một cây backtracking thô được biến thành solver có propagation, bound và certificate.