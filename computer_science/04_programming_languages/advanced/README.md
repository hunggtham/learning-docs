# Advanced Programming Languages & Runtime

Roadmap:

1. [Type systems, effects và runtime contracts](./00_type_systems_effects_and_runtime_contracts.md)
2. [Algebraic data types, variance và type inference](./01_algebraic_data_types_variance_and_type_inference.md)
3. [Ownership, borrowing, linear/affine types và memory safety](./02_ownership_borrowing_linear_types_and_memory_safety.md)
4. [Effect systems, capabilities và controlled side effects](./03_effect_systems_capabilities_and_controlled_side_effects.md)
5. [Compiler IR, SSA, data-flow analysis và optimization](./04_compiler_ir_ssa_dataflow_and_optimization.md)
6. [JIT profiling, speculative optimization và deoptimization](./05_jit_profiling_speculative_optimization_and_deoptimization.md)
7. Garbage collectors: generational, concurrent, compacting và barriers
8. Coroutines, continuations, async runtimes và structured concurrency
9. FFI, ABI, object layout và language interoperability
10. Reflection, metaprogramming và staged computation

Các chapter hiện tại đi từ static contracts và ownership sang effect/authority, rồi hạ dần xuống compiler IR và adaptive JIT runtime. Phần tiếp theo tập trung memory management, concurrency runtime và interoperability.