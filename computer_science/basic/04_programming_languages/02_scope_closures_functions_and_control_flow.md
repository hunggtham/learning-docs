# Scope, closures, functions và control flow

Functions giúp biến computation thành reusable units. Nhưng để hiểu function thật sự, cần biết names được resolved ở đâu, activation state sống bao lâu, function value mang theo environment gì, và control quay lại caller thế nào.

## Lexical scope

Scope (스코프 / phạm vi) xác định region nơi binding name có thể được referenced. Lexical scope dựa source nesting. Inner scope có thể shadow outer name; shadowing không mutate outer binding, nó tạo binding khác cùng identifier.

Name resolution thường xảy ra compile/static-analysis time theo scope chain, dù value nằm runtime.

## Function call và activation record

Mỗi call cần state riêng: arguments, locals, return point và bookkeeping. Native implementation thường dùng stack frame/registers theo ABI. Recursion hoạt động vì mỗi call có activation riêng.

Tail call xảy ra khi result của current function chính là result của another call. Language/runtime có thể tail-call optimize để reuse frame, nhưng không phải mọi ecosystem guarantee.

## First-class functions

Language có first-class functions nếu functions có thể gán vào variables, truyền như arguments, return như values. Higher-order function nhận/trả function.

`map`, `filter`, callbacks, event handlers và strategy injection đều dựa idea này.

## Closure

Closure (클로저) là function cùng lexical environment cần thiết cho free variables. Ví dụ:

```javascript
function makeCounter() {
  let n = 0;
  return () => ++n;
}
```

Sau `makeCounter` return, `n` vẫn phải sống vì returned function captures binding. Runtime có thể hoist captured state lên heap-like environment thay vì ordinary stack frame.

Capture-by-value/reference semantics khác language và construct. Mutable captures có thể tạo shared hidden state.

## Control flow

Sequence, branch, loop, call/return, exception và coroutine suspension đều thay “next computation”. Compiler biểu diễn control flow bằng Control Flow Graph — CFG, nodes là basic blocks, edges là possible transfers.

Dataflow analyses như definite assignment, liveness và optimization chạy trên CFG.

## Exception như non-local control transfer

Throw exception bỏ qua normal return path và search handler theo stack/runtime rules. Nó tiện cho separating error propagation khỏi local happy path nhưng hidden edges làm reasoning resource cleanup khó nếu language không có finally/RAII.

Exception cho expected high-frequency control flow có thể costly hoặc confusing tùy runtime; use depends semantic contract.

## Coroutine, generator và async

Coroutine có thể suspend và resume, nên activation state phải persist qua suspension. Compiler có thể transform async function thành state machine storing locals + continuation state.

`await` không magic “tạo thread”; nó thường register continuation rồi trả control khi operation chưa complete. Runtime/event loop/scheduler quyết định execution model.

Generator `yield` tương tự suspend state giữa values.

## Continuations

Continuation conceptualize “phần computation còn lại”. Callback là explicit continuation; promise/future chain compose continuations; async/await viết syntax tuần tự trên continuation/state-machine transformation.

Mental model này giúp hiểu why async stack traces và exception propagation khác sync call stack.

## Mental Model

> Function call tạo **execution context**; lexical scope quyết định names; closure giữ environment qua lifetime; control-flow construct quyết định continuation nào chạy tiếp.

## Common Misconceptions

**“Closure chỉ là anonymous function.”** Anonymous function không nhất thiết capture; named function cũng có thể closure.

**“async = multithread.”** Async là suspension/composition model; có thể chạy single-threaded event loop hoặc cùng thread pool.

**“Scope và lifetime là một.”** Binding có lexical scope giới hạn nơi truy cập, nhưng captured object/value có thể sống lâu hơn scope source.

## Kết nối

Native calls nằm ở [ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md), async/concurrency ở [process/thread scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md), compiler transformations ở [Compiler/VM/JIT](./03_compilers_interpreters_vm_and_jit.md).
