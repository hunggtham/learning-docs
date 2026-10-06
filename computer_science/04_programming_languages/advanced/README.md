# Ngôn ngữ lập trình & thời gian chạy (runtime / 런타임) nâng cao

> **Mạch đọc:** [README](./README.md) là owner của **Ngôn ngữ lập trình & thời gian chạy (runtime / 런타임) nâng cao**. Route đi từ type/effect contracts → algebraic types và ownership → compiler IR/JIT/GC → coroutine và structured concurrency, để mỗi chapter chỉ rõ invariant, phép tối ưu và failure boundary.

Bắt đầu từ [Programming Languages foundation](../../basic/04_programming_languages/00_language_semantics_and_execution_models.md).

## Chuẩn gốc (canonical / 정본) chapters

1. [Hệ thống kiểu, effect và runtime contract](./00_type_systems_effects_and_runtime_contracts.md)
2. [Kiểu dữ liệu đại số, variance và suy luận kiểu](./01_algebraic_data_types_variance_and_type_inference.md)
3. [Ownership, borrowing, linear/affine types và an toàn bộ nhớ](./02_ownership_borrowing_linear_types_and_memory_safety.md)
4. [Effect system, capability và kiểm soát side effect](./03_effect_systems_capabilities_and_controlled_side_effects.md)
5. [Compiler IR, SSA, phân tích data-flow và tối ưu](./04_compiler_ir_ssa_dataflow_and_optimization.md)
6. [JIT profiling, speculative optimization và deoptimization](./05_jit_profiling_speculative_optimization_and_deoptimization.md)
7. [Garbage collection: generational, concurrent, compacting và barrier](./06_garbage_collection_generational_concurrent_compacting_and_barriers.md)
8. [Coroutine, continuation, async runtime và structured concurrency](./07_coroutines_continuations_async_runtimes_and_structured_concurrency.md)

Nhánh học (track / 트랙) đi từ static/thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약) xuống trình biên dịch (compiler / 컴파일러)/JIT, bộ nhớ (memory / 메모리) management và async scheduling. Mỗi chapter advanced phải nói rõ bất biến (invariant / 불변식) nào trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) giữ, tối ưu hóa (optimization / 최적화)/speculation nào được phép, deoptimization/thất bại (failure / 실패) xảy ra ra sao và OS/CPU bên dưới quyết định hành vi (behavior / 동작) nào.

> **Nối mạch:** **Chuẩn gốc chapters** giữ semantics của ngôn ngữ và runtime; **Depth priorities** chọn thứ tự đào sâu theo rủi ro quan sát được, không tạo bản sao ngoài owner.

## Độ sâu (depth / 깊이) priorities

FFI/ABI, đối tượng (object / 객체) bố cục (layout / 레이아웃), reflection và metaprogramming không mặc định cần chapter mới. FFI/đối tượng (object / 객체) bố cục (layout / 레이아웃) nên đào sâu tại quyền sở hữu (ownership / 소유권)/thời gian chạy (runtime / 런타임)/trình biên dịch (compiler / 컴파일러) boundaries; reflection/metaprogramming chỉ tách riêng nếu tạo mô hình tư duy (mental model / 사고 모델) mới vượt quá kiểu (type / 타입)/tác động (effect / 효과)/thời gian chạy (runtime / 런타임) contracts hiện có.

Cross-layer đường dẫn (path / 경로) bắt buộc: [language memory model → OS → CPU ordering](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

> **Bàn giao:** Sau **Độ sâu (depth / 깊이) priorities**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
