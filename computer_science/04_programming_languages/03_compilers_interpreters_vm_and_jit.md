# Trình biên dịch (compiler / 컴파일러), trình thông dịch (interpreter / 인터프리터), VM và JIT

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Compilers, interpreters, VM và JIT**. Route đi từ source/lexing/parsing → semantic analysis/IR → interpretation hoặc compilation → VM execution/JIT speculation, để mỗi tầng biến đổi vẫn truy được semantics ban đầu.

Mã nguồn (source code / 소스 코드) phải được biến thành actions ở machine mức (level / 수준). trình biên dịch (compiler / 컴파일러) thiết kế (design / 설계) cho thấy một chuỗi abstractions: văn bản (text / 텍스트) → tokens → cú pháp (syntax / 문법) cây (tree / 트리) → ngữ nghĩa (semantic / 의미적) biểu diễn (representation / 표현) → intermediate biểu diễn (representation / 표현) → optimized mã (code / 코드) → machine/thời gian chạy (runtime / 런타임) thực thi (execution / 실행).

Điểm cần giữ xuyên toàn chuỗi xử lý (pipeline / 파이프라인) là **ngữ nghĩa quan sát được (observable semantics)** theo đặc tả hợp đồng (contract / 계약) của ngôn ngữ. Mỗi stage được phép đổi biểu diễn (representation / 표현) rất mạnh, nhưng không được tùy ý đổi điều mà chương trình hợp lệ có quyền quan sát.

## Lexing và parsing

Lexer/tokenizer nhóm characters thành tokens như identifiers, numbers, operators. Parser dùng grammar để xây parse cây (tree / 트리)/AST.

Regular-language techniques phù hợp nhiều đơn vị từ (token / 토큰) patterns; context-free grammars mô tả nested cú pháp (syntax / 문법) như parentheses/blocks. Nhưng real ngôn ngữ (language / 언어) parsing còn xử lý precedence, ambiguities và context-sensitive checks.

AST bỏ bớt punctuation không cần thiết và giữ ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조). `1 + 2 * 3` phải thành cây (tree / 트리) thể hiện multiplication binding mạnh hơn addition.

> **Nối mạch:** Lexing và parsing dựng cấu trúc; semantic analysis kiểm tra ý nghĩa, rồi intermediate representation cho compiler, interpreter và JIT một điểm chung để tối ưu hoặc thực thi.

## Ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석)

Trình biên dịch (compiler / 컴파일러) resolve names, check types, validate điều khiển (control / 제어) rules, infer types/generics tùy ngôn ngữ (language / 언어). cú pháp (syntax / 문법) hợp lệ vẫn có thể semantically invalid, như use undefined variable hoặc return wrong kiểu (type / 타입).

Symbol bảng (table / 테이블) là ánh xạ (mapping / 매핑) names → declarations/siêu dữ liệu (metadata / 메타데이터) theo scopes.

> **Nối mạch:** **Intermediate biểu diễn (representation / 표현)** nối từ **Ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석)** sang **Tối ưu hóa (optimization / 최적화)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Intermediate biểu diễn (representation / 표현)

IR là biểu diễn (representation / 표현) giữa nguồn (source / 소스) và mục tiêu (target / 대상), giúp tối ưu hóa (optimization / 최적화) độc lập ngôn ngữ (language / 언어)/hardware phần nào. SSA — Static Single Assignment — cho mỗi variable phiên bản (version / 버전) một assignment, làm dataflow/use-def chains rõ.

LLVM IR, JVM bytecode và compiler-specific IRs ở lớp trừu tượng (abstraction / 추상화) levels khác nhau. Không nên đồng nhất mọi IR với “assembly trung gian”; một IR có thể giữ kiểu (type / 타입), exception, control-flow hoặc thời gian chạy (runtime / 런타임) siêu dữ liệu (metadata / 메타데이터) mà machine ISA không biểu diễn trực tiếp.

> **Nối mạch:** **Tối ưu hóa (optimization / 최적화)** nối từ **Intermediate biểu diễn (representation / 표현)** sang **Ahead-of-time compilation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tối ưu hóa (optimization / 최적화)

Constant folding tính `2*3` trước. Dead-code elimination bỏ computations không observable. Inlining thay lời gọi (call / 호출) bằng body để mở thêm tối ưu hóa (optimization / 최적화) nhưng tăng mã (code / 코드) kích thước (size / 크기). dùng chung (common / 공통) subexpression elimination reuse kết quả (result / 결과). vòng lặp (loop / 루프) optimizations/vectorization biến truy cập (access / 접근)/điều khiển (control / 제어) patterns.

Trình biên dịch (compiler / 컴파일러) chỉ được optimize nếu giữ ngữ nghĩa (semantics / 의미론) theo ngôn ngữ (language / 언어) spec. Undefined hành vi (behavior / 동작) trong C/C++ mở tối ưu hóa (optimization / 최적화) freedom vì trình biên dịch (compiler / 컴파일러) được assume UB không xảy ra trong valid program.

Dòng mã nguồn (source line / 소스 코드 줄) không map một-một tới lệnh máy (machine instruction / 기계 명령어). Debugger, profiler và disassembly đều đang quan sát một biểu diễn (representation / 표현) sau tối ưu hóa (optimization / 최적화), không phải “nguồn (source / 소스) chạy từng dòng”.

> **Nối mạch:** **Ahead-of-time compilation** nối từ **Tối ưu hóa (optimization / 최적화)** sang **Interpretation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ahead-of-time compilation

AOT compile trước thời gian chạy (runtime / 런타임) thành mã máy (machine code / 기계어). Startup predictable, không cần thời gian chạy (runtime / 런타임) trình biên dịch (compiler / 컴파일러), nhưng khó tận dụng chính xác (exact / 정확한) thời gian chạy (runtime / 런타임) profile/hardware trạng thái (state / 상태) trừ profile-guided tối ưu hóa (optimization / 최적화).

C/C++/Rust thường AOT. Native-image các hệ thống (systems / 시스템들) compile managed languages với trade-offs reflection/động (dynamic / 동적) features.

> **Nối mạch:** **Interpretation** nối từ **Ahead-of-time compilation** sang **JIT compilation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Interpretation

Trình thông dịch (interpreter / 인터프리터) có thể walk AST hoặc execute bytecode dispatch vòng lặp (loop / 루프). Nó giảm compile startup và dễ động (dynamic / 동적) hành vi (behavior / 동작) nhưng dispatch overhead mỗi thao tác (operation / 연산) có thể lớn.

Bytecode VM đưa nguồn (source / 소스) vào compact instruction set portable. JVM bytecode chạy trên JVM implementations cho platforms khác nhau.

> **Nối mạch:** **JIT compilation** nối từ **Interpretation** sang **Garbage collector và thời gian chạy (runtime / 런타임) services**, vì cơ chế trước tạo đầu vào cho bước sau.

## JIT compilation

Just-In-Time trình biên dịch (compiler / 컴파일러) quan sát running program, compile hot methods/loops thành optimized bản địa (native / 네이티브) mã (code / 코드). thời gian chạy (runtime / 런타임) profile cho biết actual receiver types, branch frequencies, hot paths. JIT có thể speculative optimize rồi deoptimize nếu các giả định (assumptions / 가정들) thất bại (fail / 실패).

Java HotSpot tiered compilation và hiện đại (modern / 현대적) JS engines dùng variants của idea này. Warm-up benchmark vì vậy quan trọng: mã (code / 코드) ban đầu và steady-state có thể khác.

Phần internals sâu hơn nằm ở [JIT profiling, speculative optimization và deoptimization](./advanced/05_jit_profiling_speculative_optimization_and_deoptimization.md).

> **Nối mạch:** **Garbage collector và thời gian chạy (runtime / 런타임) services** nối từ **JIT compilation** sang **Linker và loader**, vì cơ chế trước tạo đầu vào cho bước sau.

## Garbage collector và thời gian chạy (runtime / 런타임) services

Managed thời gian chạy (runtime / 런타임) thường cung cấp GC, nạp lớp (class loading / 클래스 로딩), exceptions, synchronization, reflection và profiling. hiệu năng (performance / 성능) không chỉ trình biên dịch (compiler / 컴파일러) generated mã (code / 코드) mà cả hành vi thời gian chạy (runtime behavior / 런타임 동작).

Safepoint là điểm thời gian chạy (runtime / 런타임) có thể dừng/coordinate threads cho GC/deoptimization. Stop-the-world pauses không phải toàn bộ GC; concurrent collectors làm nhiều phases song song với ứng dụng (application / 애플리케이션) nhưng vẫn cần coordination.

> **Nối mạch:** **Linker và loader** nối từ **Garbage collector và thời gian chạy (runtime / 런타임) services** sang **FFI tồn tại vì hai thời gian chạy (runtime / 런타임) không chia sẻ cùng một thế giới mặc định**, vì cơ chế trước tạo đầu vào cho bước sau.

## Linker và loader

Bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러) đầu ra (output / 출력) đối tượng (object / 객체) files; linker resolve symbols/relocations. Loader map executable/dùng chung (shared / 공유) libraries vào tiến trình (process / 프로세스). động (dynamic / 동적) linker có thể lazily resolve symbols. Đây là continuation của [machine code, assembly và ABI](../basic/02_computer_architecture/04_machine_code_assembly_and_abi.md).

API ở nguồn (source / 소스) mức (level / 수준) và ABI ở nhị phân (binary / 이진) mức (level / 수준) không phải một đặc tả hợp đồng (contract / 계약). Hai thư viện có thể giữ hàm (function / 함수) name giống nhau nhưng đổi bố cục (layout / 레이아웃)/calling convention và trở thành binary-incompatible.

> **Nối mạch:** **FFI tồn tại vì hai thời gian chạy (runtime / 런타임) không chia sẻ cùng một thế giới mặc định** nối từ **Linker và loader** sang **Kiểu (type / 타입) ở nguồn (source / 소스) không tự quyết định nhị phân (binary / 이진) biểu diễn (representation / 표현)**, vì cơ chế trước tạo đầu vào cho bước sau.

## FFI tồn tại vì hai thời gian chạy (runtime / 런타임) không chia sẻ cùng một thế giới mặc định

**Giao diện hàm ngoại (Foreign Function Interface, FFI / 외부 함수 인터페이스)** cho phép mã (code / 코드) trong một ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) gọi mã (code / 코드) được biên dịch theo thời gian chạy (runtime / 런타임)/ABI khác. Ví dụ Java JNI gọi bản địa (native / 네이티브) C/C++, Python extension gọi C, Rust gọi thư viện C, hoặc JavaScript thời gian chạy (runtime / 런타임) gọi bản địa (native / 네이티브) addon.

Một FFI lời gọi (call / 호출) không chỉ là “gọi hàm (function / 함수) ở ngôn ngữ (language / 언어) khác”. Nó là crossing điểm (point / 지점) giữa nhiều đặc tả hợp đồng (contract / 계약):

```text
source type system
→ runtime representation
→ FFI marshalling
→ native ABI/calling convention
→ foreign code ownership/lifetime
→ result/error quay lại runtime
```

Nếu hai phía không thống nhất biểu diễn (representation / 표현), quyền sở hữu (ownership / 소유권) hoặc thời gian tồn tại (lifetime / 수명), kiểu (type / 타입) checker ở phía caller không thể tự cứu chương trình.

> **Nối mạch:** **FFI tồn tại vì hai thời gian chạy (runtime / 런타임) không chia sẻ cùng một thế giới mặc định** đặt vấn đề; **Kiểu (type / 타입) ở nguồn (source / 소스) không tự quyết định nhị phân (binary / 이진) biểu diễn (representation / 표현)** kiểm tra bằng chứng, rồi **Đối tượng (object / 객체) bố cục (layout / 레이아웃) là hiện thực (implementation / 구현) đặc tả hợp đồng (contract / 계약), không nên đoán từ lớp (class / 클래스) definition** mở rộng hệ quả.

## Kiểu (type / 타입) ở nguồn (source / 소스) không tự quyết định nhị phân (binary / 이진) biểu diễn (representation / 표현)

Một `String`, `boolean`, đối tượng (object / 객체) tham chiếu (reference / 참조) hay generic collection ở managed ngôn ngữ (language / 언어) thường không có nhị phân (binary / 이진) bố cục (layout / 레이아웃) giống `char*`, `bool` hay C struct.

FFI tầng (layer / 계층) phải quyết định cách **chuyển đổi biểu diễn (marshalling / 마샬링)**: bản sao (copy / 복사) bytes, pin đối tượng (object / 객체), expose pointer, allocate temporary buffer hoặc tạo wrapper/handle.

Ví dụ Java `String` không nên được suy luận là một C NUL-terminated string. Encoding, length, embedded NUL, allocation và quyền sở hữu (ownership / 소유권) đều là đặc tả hợp đồng (contract / 계약) riêng.

Signature nhìn giống nhau ở nguồn (source / 소스) chưa đủ chứng minh interoperability.

> **Nối mạch:** **Kiểu (type / 타입) ở nguồn (source / 소스) không tự quyết định nhị phân (binary / 이진) biểu diễn (representation / 표현)** đặt vấn đề; **Đối tượng (object / 객체) bố cục (layout / 레이아웃) là hiện thực (implementation / 구현) đặc tả hợp đồng (contract / 계약), không nên đoán từ lớp (class / 클래스) definition** kiểm tra bằng chứng, rồi **Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명) là nơi FFI bug thường nghiêm trọng nhất** mở rộng hệ quả.

## Đối tượng (object / 객체) bố cục (layout / 레이아웃) là hiện thực (implementation / 구현) đặc tả hợp đồng (contract / 계약), không nên đoán từ lớp (class / 클래스) definition

Đối tượng (object / 객체) trong managed thời gian chạy (runtime / 런타임) có thể chứa header, mark word, lớp (class / 클래스) pointer, alignment padding hoặc compressed tham chiếu (reference / 참조) tùy thời gian chạy (runtime / 런타임)/cấu hình (configuration / 구성). GC cũng có thể di chuyển đối tượng (object / 객체).

Bản địa (native / 네이티브) mã (code / 코드) giữ raw pointer tới managed đối tượng (object / 객체) mà không đi qua approved pin/handle cơ chế (mechanism / 메커니즘) có thể trở thành dangling pointer sau GC compaction.

Ngược lại, pin quá nhiều đối tượng (object / 객체) để giữ address cố định có thể làm GC khó compact vùng nhớ động (heap / 힙) và tăng fragmentation/độ trễ (latency / 지연 시간).

Đây là sự đánh đổi (trade-off / 트레이드오프) trực tiếp giữa interop convenience và memory-management bất biến (invariant / 불변식).

> **Nối mạch:** **Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명) là nơi FFI bug thường nghiêm trọng nhất** nối từ **Đối tượng (object / 객체) bố cục (layout / 레이아웃) là hiện thực (implementation / 구현) đặc tả hợp đồng (contract / 계약), không nên đoán từ lớp (class / 클래스) definition** sang **Lỗi (error / 오류) mô hình (model / 모델) cũng phải được dịch qua ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명) là nơi FFI bug thường nghiêm trọng nhất

Khi một pointer crossing ranh giới (boundary / 경계), cần trả lời rõ:

```text
ai sở hữu allocation?
ai được free?
allocator nào phải free?
pointer sống tới khi nào?
callback có thể chạy sau khi owner đã teardown không?
foreign side có giữ reference qua async boundary không?
```

Free bộ nhớ (memory / 메모리) bằng allocator khác allocator đã allocate có thể corrupt vùng nhớ động (heap / 힙). bản địa (native / 네이티브) thư viện (library / 라이브러리) giữ callback/user-data pointer sau khi managed wrapper đã bị GC có thể gây use-after-free. Managed side quên bản phát hành (release / 릴리스) bản địa (native / 네이티브) handle lại gây leak mà GC không nhìn thấy.

Senior-level FFI mã (code / 코드) vì vậy thường dùng tường minh (explicit / 명시적) quyền sở hữu (ownership / 소유권) wrapper, `close`/`dispose`/RAII guard hoặc safe handle lớp trừu tượng (abstraction / 추상화) thay vì truyền raw pointer tự do.

> **Nối mạch:** **Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명) là nơi FFI bug thường nghiêm trọng nhất** đặt tiêu chí; **Lỗi (error / 오류) mô hình (model / 모델) cũng phải được dịch qua ranh giới (boundary / 경계)** dùng nó để kiểm tra ranh giới, rồi **Luồng thực thi (thread / 스레드) attachment và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)** mở rộng hệ quả.

## Lỗi (error / 오류) mô hình (model / 모델) cũng phải được dịch qua ranh giới (boundary / 경계)

C có thể báo lỗi bằng return mã (code / 코드) + `errno`; C++ có exception; Java/Python có managed exception; Rust dùng `Result` và panic ngữ nghĩa (semantics / 의미론) riêng.

Một exception không được giả định có thể tự xuyên qua arbitrary ABI frame. FFI wrapper thường phải bắt lỗi ở phía sở hữu thời gian chạy (runtime / 런타임), chuyển nó thành lỗi (error / 오류) biểu diễn (representation / 표현) ổn định rồi dựng lại exception/kết quả (result / 결과) ở phía caller.

Nếu C++ exception unwind xuyên qua C ABI hoặc panic crossing unsupported FFI ranh giới (boundary / 경계), hành vi (behavior / 동작) có thể undefined hoặc terminate tiến trình (process / 프로세스) tùy nền tảng (platform / 플랫폼)/thời gian chạy (runtime / 런타임).

Bất biến (invariant / 불변식) an toàn là: **mỗi thời gian chạy (runtime / 런타임) xử lý stack-unwinding theo đặc tả hợp đồng (contract / 계약) của chính nó; ranh giới (boundary / 경계) chuyển lỗi (error / 오류) bằng giao thức (protocol / 프로토콜) tường minh (explicit / 명시적)**.

> **Nối mạch:** **Lỗi (error / 오류) mô hình (model / 모델) cũng phải được dịch qua ranh giới (boundary / 경계)** đặt tiêu chí; **Luồng thực thi (thread / 스레드) attachment và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)** dùng nó để kiểm tra ranh giới, rồi **Crossing ranh giới (boundary / 경계) có fixed chi phí (cost / 비용) nên lời gọi (call / 호출) granularity quan trọng** mở rộng hệ quả.

## Luồng thực thi (thread / 스레드) attachment và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)

Một bản địa (native / 네이티브) luồng thực thi (thread / 스레드) do foreign thư viện (library / 라이브러리) tạo ra chưa chắc đã được managed thời gian chạy (runtime / 런타임) biết tới. Muốn gọi callback vào JVM/Python/VM khác, luồng thực thi (thread / 스레드) có thể phải attach/acquire thời gian chạy (runtime / 런타임) trạng thái (state / 상태) hoặc tuân thủ toàn cục (global / 전역) trình thông dịch (interpreter / 인터프리터) khóa (lock / 잠금)/safepoint rules tùy ecosystem.

Ngược lại, giữ thời gian chạy (runtime / 런타임) khóa (lock / 잠금) khi gọi một bản địa (native / 네이티브) thao tác (operation / 연산) blocking lâu có thể làm các logical tasks khác bị stall.

Hiệu năng (performance / 성능) của FFI không chỉ là nanoseconds lời gọi (call / 호출) overhead; nó còn phụ thuộc thread-state chuyển tiếp (transition / 전이), khóa (lock / 잠금), pin/bản sao (copy / 복사), allocation và callback frequency.

> **Nối mạch:** **Luồng thực thi (thread / 스레드) attachment và thời gian chạy (runtime / 런타임) trạng thái (state / 상태)** đặt tiêu chí; **Crossing ranh giới (boundary / 경계) có fixed chi phí (cost / 비용) nên lời gọi (call / 호출) granularity quan trọng** dùng nó để kiểm tra ranh giới, rồi **ABI stability và phiên bản (version / 버전) evolution** mở rộng hệ quả.

## Crossing ranh giới (boundary / 경계) có fixed chi phí (cost / 비용) nên lời gọi (call / 호출) granularity quan trọng

Nếu mỗi element trong một array gọi bản địa (native / 네이티브) hàm (function / 함수) riêng, marshalling/lời gọi (call / 호출) chuyển tiếp (transition / 전이) có thể lớn hơn computation. Batching một buffer lớn qua một lời gọi (call / 호출) thường hiệu quả hơn hàng triệu tiny FFI calls.

Nhưng batching quá lớn tăng temporary bộ nhớ (memory / 메모리) và độ trễ (latency / 지연 시간) trước first kết quả (result / 결과). Đây vẫn là latency-throughput sự đánh đổi (trade-off / 트레이드오프) quen thuộc.

Khi benchmark interop, cần tách:

```text
pure native compute
boundary transition
marshalling/copy
allocation
runtime lock/attachment
actual I/O
```

Nếu không, ta dễ kết luận sai “bản địa (native / 네이티브) mã (code / 코드) chậm” trong khi chi phí (cost / 비용) nằm ở conversion đường dẫn (path / 경로).

> **Nối mạch:** **Crossing ranh giới (boundary / 경계) có fixed chi phí (cost / 비용) nên lời gọi (call / 호출) granularity quan trọng** đặt tiêu chí; **ABI stability và phiên bản (version / 버전) evolution** dùng nó để kiểm tra ranh giới, rồi **Bảo mật (security / 보안): bản địa (native / 네이티브) ranh giới (boundary / 경계) có thể bỏ qua an toàn (safety / 안전) guarantees của ngôn ngữ (language / 언어)** mở rộng hệ quả.

## ABI stability và phiên bản (version / 버전) evolution

Nguồn (source / 소스) API có thể tương thích nhưng bản địa (native / 네이티브) nhị phân (binary / 이진) vẫn hỏng nếu struct bố cục (layout / 레이아웃), symbol name, calling convention hoặc trình biên dịch (compiler / 컴파일러) ABI thay đổi. C ABI thường được dùng làm interoperability ranh giới (boundary / 경계) vì tương đối ổn và đơn giản hơn C++ ABI, nhưng vẫn cần tường minh (explicit / 명시적) versioning/kích thước (size / 크기) fields khi cấu trúc (structure / 구조) evolve.

Một idiom bền hơn là opaque handle:

```text
create_handle() -> opaque pointer/id
operate(handle, ...)
destroy_handle(handle)
```

Caller không phụ thuộc trực tiếp nội bộ (internal / 내부) struct bố cục (layout / 레이아웃). Đây là thông tin (information / 정보) hiding ở nhị phân (binary / 이진) ranh giới (boundary / 경계).

> **Nối mạch:** **ABI stability và phiên bản (version / 버전) evolution** đặt tiêu chí; **Bảo mật (security / 보안): bản địa (native / 네이티브) ranh giới (boundary / 경계) có thể bỏ qua an toàn (safety / 안전) guarantees của ngôn ngữ (language / 언어)** dùng nó để kiểm tra ranh giới, rồi **Debugging qua mixed ngăn xếp (stack / 스택)** mở rộng hệ quả.

## Bảo mật (security / 보안): bản địa (native / 네이티브) ranh giới (boundary / 경계) có thể bỏ qua an toàn (safety / 안전) guarantees của ngôn ngữ (language / 언어)

Một memory-safe ngôn ngữ (language / 언어) gọi bản địa (native / 네이티브) thư viện (library / 라이브러리) không làm bản địa (native / 네이티브) thư viện (library / 라이브러리) trở nên memory-safe. Buffer overflow, use-after-free, integer truncation hoặc unchecked length ở FFI có thể phá tiến trình (process / 프로세스) dù phần ứng dụng (application / 애플리케이션) còn lại an toàn.

Đầu vào (input / 입력) crossing FFI vẫn phải được validate theo trust ranh giới (boundary / 경계). Với parser/codec/ảnh (image / 이미지)/bản địa (native / 네이티브) crypto thư viện (library / 라이브러리) xử lý bytes từ mạng (network / 네트워크), bản địa (native / 네이티브) bug có thể trở thành remote attack surface.

Sandbox/tiến trình (process / 프로세스) isolation đôi khi là ranh giới (boundary / 경계) tốt hơn in-process FFI nếu thành phần (component / 컴포넌트) bản địa (native / 네이티브) có rủi ro cao hoặc crash không được phép kéo theo tiến trình (process / 프로세스) chính.

> **Nối mạch:** **Bảo mật (security / 보안): bản địa (native / 네이티브) ranh giới (boundary / 경계) có thể bỏ qua an toàn (safety / 안전) guarantees của ngôn ngữ (language / 언어)** đặt tiêu chí; **Debugging qua mixed ngăn xếp (stack / 스택)** dùng nó để kiểm tra ranh giới, rồi **Reproducibility và tối ưu hóa (optimization / 최적화) traps** mở rộng hệ quả.

## Debugging qua mixed ngăn xếp (stack / 스택)

Crash ở FFI thường cần bằng chứng (evidence / 증거) ở cả hai worlds: managed ngăn xếp (stack / 스택), bản địa (native / 네이티브) ngăn xếp (stack / 스택), symbol/gỡ lỗi (debug / 디버그) info, cốt lõi (core / 핵심) dump/minidump, GC/bản địa (native / 네이티브) bộ nhớ (memory / 메모리) telemetry và ranh giới (boundary / 경계) arguments.

Optimized mã (code / 코드) có thể inline/omit frames; JIT mã (code / 코드) còn cần thời gian chạy (runtime / 런타임) siêu dữ liệu (metadata / 메타데이터) để symbolize. Nếu chỉ nhìn exception log phía managed side, segmentation fault trong bản địa (native / 네이티브) mã (code / 코드) có thể mất ngữ cảnh (context / 맥락) quan trọng.

Một debugging workflow tốt xác định ranh giới (boundary / 경계) lời gọi (call / 호출) gần nhất rồi kiểm tra quyền sở hữu (ownership / 소유권), lengths, luồng thực thi (thread / 스레드) định danh (identity / 식별자), bản địa (native / 네이티브) lỗi (error / 오류)/crash address và phiên bản (version / 버전) của dùng chung (shared / 공유) thư viện (library / 라이브러리).

> **Nối mạch:** **Reproducibility và tối ưu hóa (optimization / 최적화) traps** nối từ **Debugging qua mixed ngăn xếp (stack / 스택)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Reproducibility và tối ưu hóa (optimization / 최적화) traps

Microbenchmark dễ bị dead-code elimination, constant folding, JIT warmup, GC và CPU frequency changes. Benchmark khung phần mềm (framework / 프레임워크) như JMH tồn tại để giảm nhiều trap, nhưng vẫn cần representative tải công việc (workload / 워크로드).

Với bản địa (native / 네이티브)/FFI benchmark còn phải kiểm soát thư viện (library / 라이브러리) bản dựng (build / 빌드) flags, symbol/phiên bản (version / 버전), allocator, CPU kiến trúc (architecture / 아키텍처) và marshalling đường dẫn (path / 경로). So sánh gỡ lỗi (debug / 디버그) bản địa (native / 네이티브) bản dựng (build / 빌드) với optimized managed bản dựng (build / 빌드) thường không có ý nghĩa.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Reproducibility và tối ưu hóa (optimization / 최적화) traps**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) là **semantic-preserving transformation chuỗi xử lý (pipeline / 파이프라인)**. Khi chương trình đi qua FFI, nó rời một ngữ nghĩa (semantic / 의미적) universe duy nhất và phải dựng một đặc tả hợp đồng (contract / 계약) mới về nhị phân (binary / 이진) calling, biểu diễn (representation / 표현), quyền sở hữu (ownership / 소유권), lỗi (error / 오류), luồng thực thi (thread / 스레드) trạng thái (state / 상태) và thời gian tồn tại (lifetime / 수명). ABI nói hai nhị phân (binary / 이진) pieces “nói chuyện” thế nào; FFI quyết định cách ngữ nghĩa (semantics / 의미론) của hai thời gian chạy (runtime / 런타임) được dịch qua cuộc hội thoại đó.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“trình thông dịch (interpreter / 인터프리터) không compile gì.”** Nhiều interpreters compile nguồn (source / 소스) thành bytecode/IR trước evaluation.

**“JIT luôn nhanh hơn AOT.”** Startup, profile chất lượng (quality / 품질), mã (code / 코드) bộ nhớ đệm (cache / 캐시), tải công việc (workload / 워크로드) duration và AOT PGO có thể đổi kết quả.

**“Optimizer chỉ làm mã (code / 코드) nhanh hơn mà không đổi gì.”** Nó giữ allowed observable ngữ nghĩa (semantics / 의미론), nhưng timing/gỡ lỗi (debug / 디버그) bố cục (layout / 레이아웃)/mã (code / 코드) shape có thể đổi; UB/dữ liệu (data / 데이터) race làm các giả định (assumptions / 가정들) phức tạp.

**“kiểu (type / 타입) giống nhau ở hai ngôn ngữ (language / 언어) thì nhị phân (binary / 이진) biểu diễn (representation / 표현) giống nhau.”** Không; kiểu ở mã nguồn (source type / 소스 타입), đối tượng (object / 객체) bố cục (layout / 레이아웃), encoding và ABI là các đặc tả hợp đồng (contract / 계약) khác nhau.

**“Memory-safe ngôn ngữ (language / 언어) vẫn an toàn khi gọi bản địa (native / 네이티브) mã (code / 코드).”** an toàn (safety / 안전) guarantee có thể dừng ở FFI ranh giới (boundary / 경계) nếu bản địa (native / 네이티브) thành phần (component / 컴포넌트) vi phạm bộ nhớ (memory / 메모리)/thời gian tồn tại (lifetime / 수명) đặc tả hợp đồng (contract / 계약).

**“FFI chậm chỉ vì hàm (function / 함수) lời gọi (call / 호출).”** bản sao (copy / 복사)/marshalling, thời gian chạy (runtime / 런타임) locks, pinning, allocation và lời gọi (call / 호출) granularity thường quyết định chi phí (cost / 비용) lớn hơn instruction `call`.

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Formal ngôn ngữ (language / 언어)/computability ở [Computability](../basic/00_computation_information/04_computability_and_limits.md), machine mục tiêu (target / 대상) và calling convention ở [CPU/ISA](../basic/02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) và [machine code/ABI](../basic/02_computer_architecture/04_machine_code_assembly_and_abi.md), thời gian chạy (runtime / 런타임) bộ nhớ (memory / 메모리) ở [types/memory](./01_types_values_references_and_memory.md), quyền sở hữu (ownership / 소유권) sâu hơn ở [Ownership, borrowing và linear types](./advanced/02_ownership_borrowing_linear_types_and_memory_safety.md), bản dựng (build / 빌드)/link chuỗi xử lý (pipeline / 파이프라인) ở [build/link/packages](../08_software_systems/01_version_control_build_link_and_packages.md), và sandbox ranh giới (boundary / 경계) ở [Memory safety, mitigations và sandbox](../07_security_reliability/advanced/04_memory_safety_mitigations_and_sandbox_boundaries.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
