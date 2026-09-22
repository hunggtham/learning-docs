# JIT profiling, speculative optimization và deoptimization

Ahead-of-time compiler phải tối ưu khi chưa biết workload runtime cụ thể. **JIT — Just-In-Time compilation (적시 컴파일)** có lợi thế quan sát chương trình đang chạy: type nào xuất hiện, branch nào thường đi, call site nào monomorphic, allocation nào escape và method/loop nào thật sự hot.

Nhưng adaptive optimization tạo một invariant khó hơn compiler tĩnh: **optimized machine code chỉ được chạy khi mọi assumption dùng để tạo code đó vẫn hợp lệ, và runtime phải có đường phục hồi semantic state nếu assumption bị phá.** Deoptimization không phải failure phụ; nó là phần của correctness contract cho speculative optimization.

## 1. Bài toán ban đầu: tối ưu mạnh cần biết behavior thật

Compiler có hai giới hạn trái chiều:

```text
compile sớm
→ startup nhanh hơn, chưa có runtime profile

compile rất tối ưu
→ cần nhiều analysis/CPU/memory và có thể tối ưu code không bao giờ hot
```

Runtime vì vậy thường dùng nhiều tiers: interpreter hoặc baseline compiler khởi động nhanh, thu profile, rồi optimizing compiler đầu tư mạnh cho hot regions.

Mục tiêu không phải compile toàn bộ chương trình “tốt nhất”; mục tiêu là đặt compilation budget vào code có return-on-investment cao.

## 2. Tiered compilation là resource scheduler cho compiler

Một method có thể đi qua state gần như:

```text
cold/interpreted
→ counters/profile accumulate
→ baseline compiled
→ hotter profile
→ optimizing compile
→ optimized machine code
→ invalidation/deopt nếu assumption fail
→ reprofile/recompile
```

Threshold không chỉ ảnh hưởng throughput. Threshold quá thấp làm compile storm và code-cache pressure; quá cao kéo dài warm-up.

Runtime do đó vừa là execution engine vừa là scheduler phân bổ CPU cho compilation.

## 3. Profile không phải truth vĩnh viễn

Profile ghi lại history của execution đã thấy, không chứng minh future input sẽ giống vậy. Ví dụ một call site trong warm-up chỉ thấy class `A`, nên JIT có thể inline `A.m()` và bỏ virtual dispatch generic khỏi hot path.

Assumption:

```text
receiver class tại call site hiện thuộc tập đã profile
```

Optimization chỉ đúng nếu code có guard hoặc dependency invalidation đủ để phát hiện khi assumption không còn đúng.

Đây là distinction quan trọng:

```text
proof-based optimization       -> đúng cho mọi execution thỏa semantics đã chứng minh
profile/speculative optimization -> nhanh nếu observed assumption tiếp tục đúng, cần guard/deopt
```

## 4. Inline cache và devirtualization là ví dụ về specialization

Call site có thể là:

- **monomorphic**: chủ yếu một target;
- **polymorphic**: vài targets;
- **megamorphic**: nhiều targets thay đổi.

Monomorphic site dễ inline và optimize xuyên boundary. Khi diversity tăng, code có thể cần polymorphic guard chain hoặc quay về generic dispatch.

Performance vì thế có thể đổi sau deployment mà source code không đổi: data mix mới làm call site chuyển từ monomorphic sang megamorphic và optimization landscape thay đổi.

## 5. Inlining mở khóa optimization khác nhưng làm code size tăng

Inlining không chỉ bỏ call overhead. Nó đưa callee IR vào caller để constant propagation, escape analysis, bounds-check elimination và dead-code elimination thấy nhiều context hơn.

Nhưng inlining quá mức tạo:

```text
machine-code size ↑
→ instruction-cache pressure ↑
→ compile time ↑
→ code cache pressure ↑
```

JIT dùng heuristic vì “inline mọi thứ” không tối ưu toàn hệ thống.

## 6. Guards biến assumption thành executable contract

Optimized path thường có guard:

```text
if receiver.class == A:
    run specialized inlined code
else:
    uncommon path / deopt / generic dispatch
```

Guard là boundary giữa observed profile và semantic correctness. Nếu guard fail, runtime không được tiếp tục dùng state representation đã specialized dưới assumption cũ.

Đây là lý do deoptimization metadata quan trọng như optimized instructions.

## 7. Deoptimization phải reconstruct source/runtime state

Optimizing compiler có thể:

- scalar-replace object nên object không tồn tại trên heap;
- giữ variable chỉ trong register;
- reorder/eliminate intermediate computation;
- inline nhiều frames vào một machine frame.

Khi deopt, runtime cần map optimized program point về logical frames/locals/operand state tương ứng. Một object đã scalar-replaced có thể phải **materialize** lại để generic/interpreted execution tiếp tục đúng semantics.

Invariant là:

> Sau deoptimization, chương trình phải tiếp tục như một execution hợp lệ của language semantics, dù representation vật lý trước đó khác hoàn toàn source model.

## 8. Safepoint và state metadata là hidden runtime machinery

GC, stack walking, deoptimization hoặc runtime operations khác cần biết references/live state tại những program points phù hợp. Optimized code vì vậy thường mang metadata như stack maps, deopt maps và safepoint information.

Performance pressure xuất hiện khi long-running generated code hiếm safepoint hoặc khi global runtime operation cần chờ threads đạt safe state. “Code đang chạy user logic” và “runtime có thể inspect/relocate state” là hai concerns phải được phối hợp.

## 9. On-Stack Replacement cho phép đổi tier giữa active loop

Một loop dài có thể trở thành hot trước khi method return. **On-Stack Replacement (OSR)** cho phép chuyển execution giữa representations ngay giữa active frame/loop.

OSR cần mapping:

```text
logical locals + stack state + program point
↔
optimized representation
```

Nếu benchmark có loop dài, thời gian đầu và cuối có thể chạy ở tier khác nhau; measurement cần hiểu phase thay vì giả định executable code cố định.

## 10. Escape analysis: source `new` không đồng nghĩa heap allocation

Nếu compiler chứng minh object không escape theo model của runtime, fields có thể được scalar-replace hoặc allocation có thể bị loại bỏ.

Do đó:

```text
source allocations
≠
actual heap allocations
```

Một refactor tưởng như “giảm object” chưa chắc giảm allocation thật; ngược lại một thay đổi khiến object bắt đầu escape có thể làm allocation/GC pressure tăng đáng kể dù syntax chỉ đổi nhỏ.

Production evidence phải nhìn allocation rate và compiler decision, không đếm `new` trong source.

## 11. Bounds-check elimination và loop optimization dựa vào invariants

Runtime có thể hoist/eliminate repeated checks khi chứng minh index range an toàn trong loop. Vectorization/unrolling cũng phụ thuộc aliasing, trip count và memory layout.

Một small code change có thể phá proof và làm machine code chậm hơn mà big-O không đổi. Đây là performance cliff do optimizer, không nhất thiết “JIT ngẫu nhiên”.

## 12. Speculation failure có thể tạo deoptimization storm

Nếu workload liên tục làm assumption đổi:

```text
profile A
→ optimize for A
→ input B invalidates
→ deopt
→ reprofile/recompile
→ behavior đổi lại
```

runtime có thể tiêu nhiều CPU cho compilation/deoptimization thay vì business work. Tail latency cũng có thể tăng khi compilation threads, code cache, safepoints hoặc deopt activity trùng traffic peak.

Optimization feedback loop là production phenomenon cần quan sát, không chỉ compiler theory.

## 13. Code cache là một tài nguyên hữu hạn

Generated machine code phải sống đâu đó. Code cache pressure có thể khiến runtime sweep/evict compiled code hoặc hạn chế optimization mới tùy implementation.

Do đó memory planning của managed runtime không chỉ gồm heap. Cần nghĩ tới metadata, native memory, thread stacks, direct buffers và compiled-code storage.

## 14. Warm-up, steady state và phase change là ba workload khác nhau

Startup có interpreter/baseline work và class/module initialization. Warm-up có compilation/profile collection. Steady state có optimized code. Sau đó workload vẫn có thể phase-change do data mix, plugin/module load hoặc code paths mới.

Một service autoscale nhanh nhưng instances chết trước khi warm-up xong có thể liên tục phục vụ ở inefficient tier. Đây là connection giữa JIT và system capacity/autoscaling.

## 15. Microbenchmark dễ đo optimizer hơn là đo code mình tưởng

Failure modes phổ biến:

```text
benchmark quá ngắn -> đo startup/warm-up
result không được dùng -> dead-code elimination
constant input -> constant folding/specialization phi thực tế
allocation không escape -> allocation bị loại
environment noisy -> CPU frequency/scheduler/GC che signal
```

Benchmark đúng cần harness chống optimizer artifacts, warm-up/measurement phases, nhiều forks/processes khi cần và kiểm soát workload distribution.

Quan trọng hơn: microbenchmark chỉ trả lời local mechanism; production throughput/p99 còn phụ thuộc queueing, GC, locks, I/O và downstream.

## 16. AOT và JIT tối ưu cho assumption khác nhau

AOT có thể giảm warm-up, giảm runtime compiler cost và làm startup/predictability tốt hơn. JIT có adaptive profile giúp specialize theo workload thật.

Không có winner universal. Nếu service short-lived/serverless, startup có trọng lượng lớn; nếu service sống lâu với hot loops ổn định, adaptive optimization có thể đáng giá.

Câu hỏi đúng là **workload lifetime + latency SLO + code dynamism + memory budget**.

## 17. Production evidence

Evidence nên nối source → compiler decision → runtime phase:

```text
- compilation count/time và compiler-thread CPU
- method/loop hotness khi runtime expose
- deoptimization/invalidation events
- code cache occupancy/pressure
- allocation rate và escape-related behavior
- safepoint/runtime pause data
- startup/warm-up/steady-state latency distribution
- CPU profiles có symbolized compiled frames
```

Một flame graph chỉ cho hot machine code hiện tại; nó không nói code đã deopt 50 lần trước đó. Compiler logs một mình lại không nói request p99. Cần correlate compiler/runtime evidence với workload timeline.

## 18. Failure reasoning theo abstraction layer

Nếu latency regression xuất hiện sau thay đổi type mix, kiểm tra devirtualization/profile trước khi chỉ nhìn GC. Nếu allocation tăng sau refactor nhỏ, kiểm tra escape behavior. Nếu startup chậm nhưng steady-state nhanh, tách compilation/warm-up khỏi service execution. Nếu only production chậm, kiểm tra workload phase/profile khác benchmark local.

Lower layer quyết định behavior có thể là instruction cache, branch behavior hoặc memory bandwidth, nhưng fix thường nằm ở source shape/runtime config/workload lifecycle—tầng sở hữu assumption.

## 19. Mô hình tư duy

> JIT là optimizer thích nghi có quyền **đặt cược** vào behavior runtime. Profile cung cấp evidence, guard biến assumption thành executable contract, metadata giữ khả năng reconstruct state, deoptimization là rollback path, còn runtime scheduler quyết định khi nào compilation đáng cost. **Performance cao đến từ specialization có thể kiểm chứng và phục hồi, không phải từ assumption vĩnh viễn về workload.**

## Kết nối

Ôn [compiler/runtime foundation](../../basic/04_programming_languages/03_compilers_interpreters_vms_and_runtime.md), đọc [compiler IR/SSA](./04_compiler_ir_ssa_dataflow_and_optimization.md), [GC internals](./06_garbage_collection_generational_concurrent_compacting_and_barriers.md), [CPU OoO](../../02_computer_architecture/advanced/01_out_of_order_execution_register_renaming_and_rob.md) và [Performance/capacity](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).