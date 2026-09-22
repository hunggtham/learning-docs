# Ngôn ngữ lập trình & Runtime nâng cao

Bắt đầu từ [Programming Languages foundation](../../basic/04_programming_languages/00_language_semantics_and_execution_models.md).

## Canonical chapters

1. [Hệ thống kiểu, effect và runtime contract](./00_type_systems_effects_and_runtime_contracts.md)
2. [Kiểu dữ liệu đại số, variance và suy luận kiểu](./01_algebraic_data_types_variance_and_type_inference.md)
3. [Ownership, borrowing, linear/affine types và an toàn bộ nhớ](./02_ownership_borrowing_linear_types_and_memory_safety.md)
4. [Effect system, capability và kiểm soát side effect](./03_effect_systems_capabilities_and_controlled_side_effects.md)
5. [Compiler IR, SSA, phân tích data-flow và tối ưu](./04_compiler_ir_ssa_dataflow_and_optimization.md)
6. [JIT profiling, speculative optimization và deoptimization](./05_jit_profiling_speculative_optimization_and_deoptimization.md)
7. [Garbage collection: generational, concurrent, compacting và barrier](./06_garbage_collection_generational_concurrent_compacting_and_barriers.md)
8. [Coroutine, continuation, async runtime và structured concurrency](./07_coroutines_continuations_async_runtimes_and_structured_concurrency.md)

Track đi từ static/runtime contract xuống compiler/JIT, memory management và async scheduling. Mỗi chapter advanced phải nói rõ invariant nào compiler/runtime giữ, optimization/speculation nào được phép, deoptimization/failure xảy ra ra sao và OS/CPU bên dưới quyết định behavior nào.

## Depth priorities

FFI/ABI, object layout, reflection và metaprogramming không mặc định cần chapter mới. FFI/object layout nên đào sâu tại ownership/runtime/compiler boundaries; reflection/metaprogramming chỉ tách riêng nếu tạo mental model mới vượt quá type/effect/runtime contracts hiện có.

Cross-layer path bắt buộc: [language memory model → OS → CPU ordering](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).