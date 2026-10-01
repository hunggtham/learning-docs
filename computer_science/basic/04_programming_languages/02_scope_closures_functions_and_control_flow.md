# Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Lexical phạm vi (scope / 범위)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Hàm (function / 함수) lời gọi (call / 호출) và activation bản ghi (record / 레코드)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Functions giúp biến computation thành reusable units. Nhưng để hiểu hàm (function / 함수) thật sự, cần biết names được resolved ở đâu, activation trạng thái (state / 상태) sống bao lâu, hàm (function / 함수) giá trị (value / 값) mang theo môi trường (environment / 환경) gì, và điều khiển (control / 제어) quay lại caller thế nào.

## Lexical phạm vi (scope / 범위)

Phạm vi (scope / 범위) xác định region nơi binding name có thể được referenced. Lexical phạm vi (scope / 범위) dựa nguồn (source / 소스) nesting. Inner phạm vi (scope / 범위) có thể shadow outer name; shadowing không mutate outer binding, nó tạo binding khác cùng identifier.

Name resolution thường xảy ra compile/static-analysis thời gian (time / 시간) theo phạm vi (scope / 범위) chuỗi (chain / 사슬), dù giá trị (value / 값) nằm thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Trong **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Hàm (function / 함수) lời gọi (call / 호출) và activation bản ghi (record / 레코드)** tiếp nhận điểm tựa từ **Lexical phạm vi (scope / 범위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **First-class functions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm (function / 함수) lời gọi (call / 호출) và activation bản ghi (record / 레코드)

Mỗi lời gọi (call / 호출) cần trạng thái (state / 상태) riêng: arguments, locals, return điểm (point / 지점) và bookkeeping. bản địa (native / 네이티브) hiện thực (implementation / 구현) thường dùng ngăn xếp (stack / 스택) frame/registers theo ABI. Recursion hoạt động vì mỗi lời gọi (call / 호출) có activation riêng.

Tail lời gọi (call / 호출) xảy ra khi kết quả (result / 결과) của hiện tại (current / 현재) hàm (function / 함수) chính là kết quả (result / 결과) của another lời gọi (call / 호출). ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) có thể tail-call optimize để reuse frame, nhưng không phải mọi ecosystem guarantee.

> **Chuyển mạch:** Ở chặng này của **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **First-class functions** tiếp nhận điểm tựa từ **Hàm (function / 함수) lời gọi (call / 호출) và activation bản ghi (record / 레코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Closure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## First-class functions

Ngôn ngữ (language / 언어) có first-class functions nếu functions có thể gán vào variables, truyền như arguments, return như values. Higher-order hàm (function / 함수) nhận/trả hàm (function / 함수).

`map`, `filter`, callbacks, sự kiện (event / 이벤트) handlers và chiến lược (strategy / 전략) injection đều dựa idea này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Closure** tiếp nhận điểm tựa từ **First-class functions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điều khiển (control / 제어) luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Closure

Closure (클로저) là hàm (function / 함수) cùng lexical môi trường (environment / 환경) cần thiết cho free variables. Ví dụ:

```javascript
function makeCounter() {
  let n = 0;
  return () => ++n;
}
```

Sau `makeCounter` return, `n` vẫn phải sống vì returned hàm (function / 함수) captures binding. thời gian chạy (runtime / 런타임) có thể hoist captured trạng thái (state / 상태) lên heap-like môi trường (environment / 환경) thay vì ordinary ngăn xếp (stack / 스택) frame.

Capture-by-value/tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) khác ngôn ngữ (language / 언어) và construct. Mutable captures có thể tạo dùng chung (shared / 공유) hidden trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Closure** xác định đầu vào; **Điều khiển (control / 제어) luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Exception như non-local điều khiển (control / 제어) transfer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều khiển (control / 제어) luồng (flow / 흐름)

Chuỗi (sequence / 시퀀스), branch, vòng lặp (loop / 루프), lời gọi (call / 호출)/return, exception và coroutine suspension đều thay “next computation”. trình biên dịch (compiler / 컴파일러) biểu diễn điều khiển (control / 제어) luồng (flow / 흐름) bằng điều khiển (control / 제어) luồng (flow / 흐름) đồ thị (graph / 그래프) — CFG, nodes là basic blocks, edges là possible transfers.

Dataflow analyses như definite assignment, liveness và tối ưu hóa (optimization / 최적화) chạy trên CFG.

> **Chuyển mạch:** Ở chặng này của **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Điều khiển (control / 제어) luồng (flow / 흐름)** xác định đầu vào; **Exception như non-local điều khiển (control / 제어) transfer** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Coroutine, generator và async** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exception như non-local điều khiển (control / 제어) transfer

Throw exception bỏ qua normal return đường dẫn (path / 경로) và tìm kiếm (search / 검색) handler theo ngăn xếp (stack / 스택)/thời gian chạy (runtime / 런타임) rules. Nó tiện cho separating lan truyền lỗi (error propagation / 오류 전파) khỏi cục bộ (local / 로컬) happy đường dẫn (path / 경로) nhưng hidden edges làm lập luận (reasoning / 추론) tài nguyên (resource / 자원) cleanup khó nếu ngôn ngữ (language / 언어) không có finally/RAII.

Exception cho expected high-frequency điều khiển (control / 제어) luồng (flow / 흐름) có thể costly hoặc confusing tùy thời gian chạy (runtime / 런타임); use depends ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Coroutine, generator và async** tiếp nhận điểm tựa từ **Exception như non-local điều khiển (control / 제어) transfer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Continuations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coroutine, generator và async

Coroutine có thể suspend và resume, nên activation trạng thái (state / 상태) phải persist qua suspension. trình biên dịch (compiler / 컴파일러) có thể transform async hàm (function / 함수) thành máy trạng thái (state machine / 상태 머신) storing locals + continuation trạng thái (state / 상태).

`await` không magic “tạo luồng thực thi (thread / 스레드)”; nó thường register continuation rồi trả điều khiển (control / 제어) khi thao tác (operation / 연산) chưa complete. thời gian chạy (runtime / 런타임)/vòng lặp sự kiện (event loop / 이벤트 루프)/scheduler quyết định mô hình thực thi (execution model / 실행 모델).

Generator `yield` tương tự suspend trạng thái (state / 상태) giữa values.

> **Chuyển mạch:** Trong **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Continuations** tiếp nhận điểm tựa từ **Coroutine, generator và async** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuations

Continuation conceptualize “phần computation còn lại”. Callback là tường minh (explicit / 명시적) continuation; promise/future chuỗi (chain / 사슬) compose continuations; async/await viết cú pháp (syntax / 문법) tuần tự trên continuation/state-machine transformation.

Mô hình tư duy (mental model / 사고 모델) này giúp hiểu why async ngăn xếp (stack / 스택) traces và exception propagation khác sync ngăn xếp lời gọi (call stack / 호출 스택).

> **Chuyển mạch:** Ở chặng này của **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Continuations** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> hàm (function / 함수) lời gọi (call / 호출) tạo **thực thi (execution / 실행) ngữ cảnh (context / 맥락)**; lexical phạm vi (scope / 범위) quyết định names; closure giữ môi trường (environment / 환경) qua thời gian tồn tại (lifetime / 수명); control-flow construct quyết định continuation nào chạy tiếp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Closure chỉ là anonymous hàm (function / 함수).”** Anonymous hàm (function / 함수) không nhất thiết capture; named hàm (function / 함수) cũng có thể closure.

**“async = multithread.”** Async là suspension/composition mô hình (model / 모델); có thể chạy single-threaded vòng lặp sự kiện (event loop / 이벤트 루프) hoặc cùng luồng thực thi (thread / 스레드) pool.

**“phạm vi (scope / 범위) và thời gian tồn tại (lifetime / 수명) là một.”** Binding có lexical phạm vi (scope / 범위) giới hạn nơi truy cập, nhưng captured đối tượng (object / 객체)/giá trị (value / 값) có thể sống lâu hơn phạm vi (scope / 범위) nguồn (source / 소스).

> **Chuyển mạch:** Trong **Phạm vi (scope / 범위), closures, functions và điều khiển (control / 제어) luồng (flow / 흐름)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Bản địa (native / 네이티브) calls nằm ở [ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md), async/tính đồng thời (concurrency / 동시성) ở [process/thread scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md), trình biên dịch (compiler / 컴파일러) transformations ở [Compiler/VM/JIT](./03_compilers_interpreters_vm_and_jit.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
