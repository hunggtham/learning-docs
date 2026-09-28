# JIT profiling, speculative tối ưu hóa (optimization / 최적화) và deoptimization

> **Mạch đọc:** Đặt **JIT profiling, speculative tối ưu hóa (optimization / 최적화) và deoptimization** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Bài toán ban đầu: tối ưu mạnh cần biết hành vi (behavior / 동작) thật** sang **2. Tiered compilation là tài nguyên (resource / 자원) scheduler cho trình biên dịch (compiler / 컴파일러)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Ahead-of-time trình biên dịch (compiler / 컴파일러) phải tối ưu khi chưa biết tải công việc (workload / 워크로드) thời gian chạy (runtime / 런타임) cụ thể. **JIT — Just-In-Time compilation (적시 컴파일)** có lợi thế quan sát chương trình đang chạy: kiểu (type / 타입) nào xuất hiện, branch nào thường đi, lời gọi (call / 호출) site nào monomorphic, allocation nào escape và phương thức (method / 메서드)/vòng lặp (loop / 루프) nào thật sự hot.

Nhưng adaptive tối ưu hóa (optimization / 최적화) tạo một bất biến (invariant / 불변식) khó hơn trình biên dịch (compiler / 컴파일러) tĩnh: **optimized mã máy (machine code / 기계어) chỉ được chạy khi mọi giả định (assumption / 가정) dùng để tạo mã (code / 코드) đó vẫn hợp lệ, và thời gian chạy (runtime / 런타임) phải có đường phục hồi ngữ nghĩa (semantic / 의미적) trạng thái (state / 상태) nếu giả định (assumption / 가정) bị phá.** Deoptimization không phải thất bại (failure / 실패) phụ; nó là phần của tính đúng đắn (correctness / 정확성) đặc tả hợp đồng (contract / 계약) cho speculative tối ưu hóa (optimization / 최적화).

## 1. Bài toán ban đầu: tối ưu mạnh cần biết hành vi (behavior / 동작) thật

Trình biên dịch (compiler / 컴파일러) có hai giới hạn trái chiều:

```text
compile sớm
→ startup nhanh hơn, chưa có runtime profile

compile rất tối ưu
→ cần nhiều analysis/CPU/memory và có thể tối ưu code không bao giờ hot
```

Thời gian chạy (runtime / 런타임) vì vậy thường dùng nhiều tiers: trình thông dịch (interpreter / 인터프리터) hoặc baseline trình biên dịch (compiler / 컴파일러) khởi động nhanh, thu profile, rồi optimizing trình biên dịch (compiler / 컴파일러) đầu tư mạnh cho hot regions.

Mục tiêu không phải compile toàn bộ chương trình “tốt nhất”; mục tiêu là đặt compilation ngân sách (budget / 예산) vào mã (code / 코드) có return-on-investment cao.

## 2. Tiered compilation là tài nguyên (resource / 자원) scheduler cho trình biên dịch (compiler / 컴파일러)

Một phương thức (method / 메서드) có thể đi qua trạng thái (state / 상태) gần như:

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

Threshold không chỉ ảnh hưởng thông lượng (throughput / 처리량). Threshold quá thấp làm compile storm và code-cache pressure; quá cao kéo dài warm-up.

Thời gian chạy (runtime / 런타임) do đó vừa là thực thi (execution / 실행) engine vừa là scheduler phân bổ CPU cho compilation.

## 3. Profile không phải truth vĩnh viễn

Profile ghi lại lịch sử (history / 이력) của thực thi (execution / 실행) đã thấy, không chứng minh future đầu vào (input / 입력) sẽ giống vậy. Ví dụ một lời gọi (call / 호출) site trong warm-up chỉ thấy lớp (class / 클래스) `A`, nên JIT có thể inline `A.m()` và bỏ virtual dispatch generic khỏi đường xử lý nóng (hot path / 핫 패스).

Giả định (assumption / 가정):

```text
receiver class tại call site hiện thuộc tập đã profile
```

Tối ưu hóa (optimization / 최적화) chỉ đúng nếu mã (code / 코드) có guard hoặc phụ thuộc (dependency / 의존성) vô hiệu hóa (invalidation / 무효화) đủ để phát hiện khi giả định (assumption / 가정) không còn đúng.

Đây là distinction quan trọng:

```text
proof-based optimization       -> đúng cho mọi execution thỏa semantics đã chứng minh
profile/speculative optimization -> nhanh nếu observed assumption tiếp tục đúng, cần guard/deopt
```

## 4. Inline bộ nhớ đệm (cache / 캐시) và devirtualization là ví dụ về specialization

Lời gọi (call / 호출) site có thể là:

- **monomorphic**: chủ yếu một mục tiêu (target / 대상);
- **polymorphic**: vài targets;
- **megamorphic**: nhiều targets thay đổi.

Monomorphic site dễ inline và optimize xuyên ranh giới (boundary / 경계). Khi diversity tăng, mã (code / 코드) có thể cần polymorphic guard chuỗi (chain / 사슬) hoặc quay về generic dispatch.

Hiệu năng (performance / 성능) vì thế có thể đổi sau triển khai (deployment / 배포) mà mã nguồn (source code / 소스 코드) không đổi: dữ liệu (data / 데이터) mix mới làm lời gọi (call / 호출) site chuyển từ monomorphic sang megamorphic và tối ưu hóa (optimization / 최적화) landscape thay đổi.

## 5. Inlining mở khóa tối ưu hóa (optimization / 최적화) khác nhưng làm mã (code / 코드) kích thước (size / 크기) tăng

Inlining không chỉ bỏ lời gọi (call / 호출) overhead. Nó đưa callee IR vào caller để constant propagation, escape phân tích (analysis / 분석), bounds-check elimination và dead-code elimination thấy nhiều ngữ cảnh (context / 맥락) hơn.

Nhưng inlining quá mức tạo:

```text
machine-code size ↑
→ instruction-cache pressure ↑
→ compile time ↑
→ code cache pressure ↑
```

JIT dùng heuristic vì “inline mọi thứ” không tối ưu toàn hệ thống.

## 6. Guards biến giả định (assumption / 가정) thành executable đặc tả hợp đồng (contract / 계약)

Optimized đường dẫn (path / 경로) thường có guard:

```text
if receiver.class == A:
    run specialized inlined code
else:
    uncommon path / deopt / generic dispatch
```

Guard là ranh giới (boundary / 경계) giữa observed profile và ngữ nghĩa (semantic / 의미적) tính đúng đắn (correctness / 정확성). Nếu guard thất bại (fail / 실패), thời gian chạy (runtime / 런타임) không được tiếp tục dùng trạng thái (state / 상태) biểu diễn (representation / 표현) đã specialized dưới giả định (assumption / 가정) cũ.

Đây là lý do deoptimization siêu dữ liệu (metadata / 메타데이터) quan trọng như optimized instructions.

## 7. Deoptimization phải reconstruct nguồn (source / 소스)/thời gian chạy (runtime / 런타임) trạng thái (state / 상태)

Optimizing trình biên dịch (compiler / 컴파일러) có thể:

- scalar-replace đối tượng (object / 객체) nên đối tượng (object / 객체) không tồn tại trên vùng nhớ động (heap / 힙);
- giữ variable chỉ trong register;
- reorder/eliminate intermediate computation;
- inline nhiều frames vào một machine frame.

Khi deopt, thời gian chạy (runtime / 런타임) cần map optimized program điểm (point / 지점) về logical frames/locals/operand trạng thái (state / 상태) tương ứng. Một đối tượng (object / 객체) đã scalar-replaced có thể phải **materialize** lại để generic/interpreted thực thi (execution / 실행) tiếp tục đúng ngữ nghĩa (semantics / 의미론).

Bất biến (invariant / 불변식) là:

> Sau deoptimization, chương trình phải tiếp tục như một thực thi (execution / 실행) hợp lệ của ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론), dù biểu diễn (representation / 표현) vật lý trước đó khác hoàn toàn nguồn (source / 소스) mô hình (model / 모델).

## 8. Safepoint và trạng thái (state / 상태) siêu dữ liệu (metadata / 메타데이터) là hidden thời gian chạy (runtime / 런타임) machinery

GC, ngăn xếp (stack / 스택) walking, deoptimization hoặc thời gian chạy (runtime / 런타임) operations khác cần biết references/live trạng thái (state / 상태) tại những program points phù hợp. Optimized mã (code / 코드) vì vậy thường mang siêu dữ liệu (metadata / 메타데이터) như ngăn xếp (stack / 스택) maps, deopt maps và safepoint thông tin (information / 정보).

Hiệu năng (performance / 성능) pressure xuất hiện khi long-running generated mã (code / 코드) hiếm safepoint hoặc khi toàn cục (global / 전역) thời gian chạy (runtime / 런타임) thao tác (operation / 연산) cần chờ threads đạt safe trạng thái (state / 상태). “mã (code / 코드) đang chạy người dùng (user / 사용자) lô-gic (logic / 논리)” và “thời gian chạy (runtime / 런타임) có thể inspect/relocate trạng thái (state / 상태)” là hai concerns phải được phối hợp.

## 9. On-Stack Replacement cho phép đổi tier giữa active vòng lặp (loop / 루프)

Một vòng lặp (loop / 루프) dài có thể trở thành hot trước khi phương thức (method / 메서드) return. **On-Stack Replacement (OSR)** cho phép chuyển thực thi (execution / 실행) giữa representations ngay giữa active frame/vòng lặp (loop / 루프).

OSR cần ánh xạ (mapping / 매핑):

```text
logical locals + stack state + program point
↔
optimized representation
```

Nếu benchmark có vòng lặp (loop / 루프) dài, thời gian đầu và cuối có thể chạy ở tier khác nhau; đo lường (measurement / 측정) cần hiểu phase thay vì giả định executable mã (code / 코드) cố định.

## 10. Escape phân tích (analysis / 분석): nguồn (source / 소스) `new` không đồng nghĩa vùng nhớ động (heap / 힙) allocation

Nếu trình biên dịch (compiler / 컴파일러) chứng minh đối tượng (object / 객체) không escape theo mô hình (model / 모델) của thời gian chạy (runtime / 런타임), fields có thể được scalar-replace hoặc allocation có thể bị loại bỏ.

Do đó:

```text
source allocations
≠
actual heap allocations
```

Một refactor tưởng như “giảm đối tượng (object / 객체)” chưa chắc giảm allocation thật; ngược lại một thay đổi khiến đối tượng (object / 객체) bắt đầu escape có thể làm allocation/GC pressure tăng đáng kể dù cú pháp (syntax / 문법) chỉ đổi nhỏ.

Bằng chứng vận hành (production evidence / 운영 증거) phải nhìn allocation tỷ lệ (rate / 비율) và trình biên dịch (compiler / 컴파일러) quyết định (decision / 결정), không đếm `new` trong nguồn (source / 소스).

## 11. Bounds-check elimination và vòng lặp (loop / 루프) tối ưu hóa (optimization / 최적화) dựa vào invariants

Thời gian chạy (runtime / 런타임) có thể hoist/eliminate repeated checks khi chứng minh chỉ mục (index / 인덱스) phạm vi (range / 범위) an toàn trong vòng lặp (loop / 루프). Vectorization/unrolling cũng phụ thuộc aliasing, trip count và bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃).

Một small mã (code / 코드) thay đổi (change / 변경) có thể phá proof và làm mã máy (machine code / 기계어) chậm hơn mà big-O không đổi. Đây là hiệu năng (performance / 성능) cliff do optimizer, không nhất thiết “JIT ngẫu nhiên”.

## 12. Speculation thất bại (failure / 실패) có thể tạo deoptimization storm

Nếu tải công việc (workload / 워크로드) liên tục làm giả định (assumption / 가정) đổi:

```text
profile A
→ optimize for A
→ input B invalidates
→ deopt
→ reprofile/recompile
→ behavior đổi lại
```

Thời gian chạy (runtime / 런타임) có thể tiêu nhiều CPU cho compilation/deoptimization thay vì nghiệp vụ (business / 비즈니스) công việc (work / 작업). Tail độ trễ (latency / 지연 시간) cũng có thể tăng khi compilation threads, mã (code / 코드) bộ nhớ đệm (cache / 캐시), safepoints hoặc deopt activity trùng traffic peak.

Tối ưu hóa (optimization / 최적화) vòng phản hồi (feedback loop / 피드백 루프) là môi trường vận hành (production / 운영 환경) phenomenon cần quan sát, không chỉ trình biên dịch (compiler / 컴파일러) lý thuyết (theory / 이론).

## 13. mã (code / 코드) bộ nhớ đệm (cache / 캐시) là một tài nguyên hữu hạn

Generated mã máy (machine code / 기계어) phải sống đâu đó. mã (code / 코드) bộ nhớ đệm (cache / 캐시) pressure có thể khiến thời gian chạy (runtime / 런타임) sweep/evict compiled mã (code / 코드) hoặc hạn chế tối ưu hóa (optimization / 최적화) mới tùy hiện thực (implementation / 구현).

Do đó bộ nhớ (memory / 메모리) planning của managed thời gian chạy (runtime / 런타임) không chỉ gồm vùng nhớ động (heap / 힙). Cần nghĩ tới siêu dữ liệu (metadata / 메타데이터), bản địa (native / 네이티브) bộ nhớ (memory / 메모리), luồng thực thi (thread / 스레드) stacks, direct buffers và compiled-code lưu trữ (storage / 저장소).

## 14. Warm-up, steady trạng thái (state / 상태) và phase thay đổi (change / 변경) là ba tải công việc (workload / 워크로드) khác nhau

Startup có trình thông dịch (interpreter / 인터프리터)/baseline công việc (work / 작업) và lớp (class / 클래스)/mô-đun (module / 모듈) initialization. Warm-up có compilation/profile collection. Steady trạng thái (state / 상태) có optimized mã (code / 코드). Sau đó tải công việc (workload / 워크로드) vẫn có thể phase-change do dữ liệu (data / 데이터) mix, plugin/mô-đun (module / 모듈) tải (load / 로드) hoặc mã (code / 코드) paths mới.

Một dịch vụ (service / 서비스) autoscale nhanh nhưng instances chết trước khi warm-up xong có thể liên tục phục vụ ở inefficient tier. Đây là liên kết (connection / 연결) giữa JIT và hệ thống (system / 시스템) sức chứa (capacity / 용량)/autoscaling.

## 15. Microbenchmark dễ đo optimizer hơn là đo mã (code / 코드) mình tưởng

Thất bại (failure / 실패) modes phổ biến:

```text
benchmark quá ngắn -> đo startup/warm-up
result không được dùng -> dead-code elimination
constant input -> constant folding/specialization phi thực tế
allocation không escape -> allocation bị loại
environment noisy -> CPU frequency/scheduler/GC che signal
```

Benchmark đúng cần harness chống optimizer artifacts, warm-up/đo lường (measurement / 측정) phases, nhiều forks/processes khi cần và kiểm soát tải công việc (workload / 워크로드) phân phối (distribution / 분포).

Quan trọng hơn: microbenchmark chỉ trả lời cục bộ (local / 로컬) cơ chế (mechanism / 메커니즘); môi trường vận hành (production / 운영 환경) thông lượng (throughput / 처리량)/p99 còn phụ thuộc queueing, GC, locks, I/O và downstream.

## 16. AOT và JIT tối ưu cho giả định (assumption / 가정) khác nhau

AOT có thể giảm warm-up, giảm thời gian chạy (runtime / 런타임) trình biên dịch (compiler / 컴파일러) chi phí (cost / 비용) và làm startup/predictability tốt hơn. JIT có adaptive profile giúp specialize theo tải công việc (workload / 워크로드) thật.

Không có winner universal. Nếu dịch vụ (service / 서비스) short-lived/serverless, startup có trọng lượng lớn; nếu dịch vụ (service / 서비스) sống lâu với hot loops ổn định, adaptive tối ưu hóa (optimization / 최적화) có thể đáng giá.

Câu hỏi đúng là **tải công việc (workload / 워크로드) thời gian tồn tại (lifetime / 수명) + độ trễ (latency / 지연 시간) SLO + mã (code / 코드) dynamism + bộ nhớ (memory / 메모리) ngân sách (budget / 예산)**.

## 17. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) nên nối nguồn (source / 소스) → trình biên dịch (compiler / 컴파일러) quyết định (decision / 결정) → thời gian chạy (runtime / 런타임) phase:

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

Một flame đồ thị (graph / 그래프) chỉ cho hot mã máy (machine code / 기계어) hiện tại; nó không nói mã (code / 코드) đã deopt 50 lần trước đó. trình biên dịch (compiler / 컴파일러) logs một mình lại không nói yêu cầu (request / 요청) p99. Cần correlate trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거) với tải công việc (workload / 워크로드) timeline.

## 18. thất bại (failure / 실패) lập luận (reasoning / 추론) theo lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)

Nếu độ trễ (latency / 지연 시간) regression xuất hiện sau thay đổi kiểu (type / 타입) mix, kiểm tra devirtualization/profile trước khi chỉ nhìn GC. Nếu allocation tăng sau refactor nhỏ, kiểm tra escape hành vi (behavior / 동작). Nếu startup chậm nhưng steady-state nhanh, tách compilation/warm-up khỏi dịch vụ (service / 서비스) thực thi (execution / 실행). Nếu only môi trường vận hành (production / 운영 환경) chậm, kiểm tra tải công việc (workload / 워크로드) phase/profile khác benchmark cục bộ (local / 로컬).

Lower tầng (layer / 계층) quyết định hành vi (behavior / 동작) có thể là instruction bộ nhớ đệm (cache / 캐시), branch hành vi (behavior / 동작) hoặc bộ nhớ (memory / 메모리) bandwidth, nhưng fix thường nằm ở nguồn (source / 소스) shape/thời gian chạy (runtime / 런타임) cấu hình (config / 설정)/tải công việc (workload / 워크로드) vòng đời (lifecycle / 생명주기)—tầng sở hữu giả định (assumption / 가정).

## 19. Mô hình tư duy

> JIT là optimizer thích nghi có quyền **đặt cược** vào hành vi (behavior / 동작) thời gian chạy (runtime / 런타임). Profile cung cấp bằng chứng (evidence / 증거), guard biến giả định (assumption / 가정) thành executable đặc tả hợp đồng (contract / 계약), siêu dữ liệu (metadata / 메타데이터) giữ khả năng reconstruct trạng thái (state / 상태), deoptimization là quay lui (rollback / 롤백) đường dẫn (path / 경로), còn thời gian chạy (runtime / 런타임) scheduler quyết định khi nào compilation đáng chi phí (cost / 비용). **hiệu năng (performance / 성능) cao đến từ specialization có thể kiểm chứng và phục hồi, không phải từ giả định (assumption / 가정) vĩnh viễn về tải công việc (workload / 워크로드).**

## Kết nối

Ôn [compiler/runtime foundation](../../basic/04_programming_languages/03_compilers_interpreters_vm_and_jit.md), đọc [compiler IR/SSA](./04_compiler_ir_ssa_dataflow_and_optimization.md), [GC internals](./06_garbage_collection_generational_concurrent_compacting_and_barriers.md), [CPU OoO](../../02_computer_architecture/advanced/01_out_of_order_execution_register_renaming_and_rob.md) và [Performance/capacity](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 type systems effects and runtime contracts](./00_type_systems_effects_and_runtime_contracts.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
