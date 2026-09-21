# Ngôn ngữ lập trình & Runtime nâng cao

Roadmap:

1. [Hệ thống kiểu, effect và runtime contract](./00_type_systems_effects_and_runtime_contracts.md)
2. [Kiểu dữ liệu đại số, variance và suy luận kiểu](./01_algebraic_data_types_variance_and_type_inference.md)
3. [Ownership, borrowing, linear/affine types và an toàn bộ nhớ](./02_ownership_borrowing_linear_types_and_memory_safety.md)
4. [Effect system, capability và kiểm soát side effect](./03_effect_systems_capabilities_and_controlled_side_effects.md)
5. [Compiler IR, SSA, phân tích data-flow và tối ưu](./04_compiler_ir_ssa_dataflow_and_optimization.md)
6. [JIT profiling, speculative optimization và deoptimization](./05_jit_profiling_speculative_optimization_and_deoptimization.md)
7. [Garbage collection: generational, concurrent, compacting và barrier](./06_garbage_collection_generational_concurrent_compacting_and_barriers.md)
8. [Coroutine, continuation, async runtime và structured concurrency](./07_coroutines_continuations_async_runtimes_and_structured_concurrency.md)
9. FFI, ABI, object layout và khả năng tương tác giữa ngôn ngữ
10. Reflection, metaprogramming và staged computation

Tám chapter hiện có tạo một đường học liền mạch từ hợp đồng tĩnh và ownership xuống compiler IR/JIT, sau đó đi vào hai subsystem runtime quan trọng nhất: quản lý bộ nhớ tự động và lập lịch công việc bất đồng bộ. Phần tiếp theo tập trung FFI/ABI, object layout và interoperability để nối runtime với native code và OS.