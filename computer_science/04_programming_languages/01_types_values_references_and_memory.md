# Types, values, references và bộ nhớ (memory / 메모리) management

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Types, values, references và memory management**. Route đi từ value/representation → references và aliasing → static/dynamic typing → lifetime, allocation và memory safety, để kiểu dữ liệu không bị tách khỏi layout và vòng đời.

Hệ kiểu (type system / 타입 시스템) không chỉ là danh sách `int`, `string`, `class`. kiểu (type / 타입) mô tả tập values và operations hợp lệ, giúp ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) encode các giả định (assumptions / 가정들). bộ nhớ (memory / 메모리) management quyết định values sống ở đâu, ai sở hữu, khi nào reclaim và references có ngữ nghĩa (semantics / 의미론) gì.

## Giá trị (value / 값) và biểu diễn (representation / 표현)

Giá trị (value / 값) là ngữ nghĩa (semantic / 의미적) thực thể (entity / 엔터티) như integer 42; biểu diễn (representation / 표현) là bit mẫu (pattern / 패턴)/đối tượng (object / 객체) bố cục (layout / 레이아웃) dùng để hiện thực. Hai values equal không nhất thiết same định danh (identity / 식별자). Java `Integer`, JavaScript objects, Python integers hay C structs có biểu diễn (representation / 표현)/định danh (identity / 식별자) khác nhau.

Kiểu (type / 타입) có thể influence kích thước (size / 크기)/bố cục (layout / 레이아웃) nhưng lớp trừu tượng (abstraction / 추상화) có thể che vật lý (physical / 물리적) biểu diễn (representation / 표현). `String` không phải “mảng chars” universal; Java uses compact-string hiện thực (implementation / 구현) details, UTF-16 APIs; Rust `String` is UTF-8 buffer lớp trừu tượng (abstraction / 추상화); JS string ngữ nghĩa (semantics / 의미론) use UTF-16 mã (code / 코드) units.

> **Nối mạch:** **Static và động (dynamic / 동적) typing** nối từ **Giá trị (value / 값) và biểu diễn (representation / 표현)** sang **Nominal và structural typing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Static và động (dynamic / 동적) typing

Static kiểu (type / 타입) checker xác minh các ràng buộc (constraints / 제약조건들) trước thời gian chạy (runtime / 런타임); hệ động (dynamic system / 동적 시스템) checks types/operations khi thực thi (execution / 실행). sự đánh đổi (trade-off / 트레이드오프) không đơn giản an toàn (safety / 안전) vs flexibility. Static các hệ thống (systems / 시스템들) có expressive levels khác nhau; động (dynamic / 동적) languages có tests/contracts/static analyzers optional.

Strong/weak typing là thuật ngữ mơ hồ; nên nói cụ thể implicit coercion nào được phép, bộ nhớ (memory / 메모리) an toàn (safety / 안전) ra sao, casts/checks thế nào.

> **Nối mạch:** **Nominal và structural typing** nối từ **Static và động (dynamic / 동적) typing** sang **Giá trị (value / 값) ngữ nghĩa (semantics / 의미론) và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Nominal và structural typing

Nominal typing dựa declared định danh (identity / 식별자)/relationship (`class A implements I`). Structural typing dựa shape/capabilities (“có methods này thì phù hợp”). Java chủ yếu nominal; TypeScript mạnh về structural typing.

Choice ảnh hưởng API evolution và accidental tính tương thích (compatibility / 호환성).

> **Nối mạch:** sau nội dung của **Nominal và structural typing**, **Giá trị (value / 값) ngữ nghĩa (semantics / 의미론) và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu; **Ngăn xếp (stack / 스택) và vùng nhớ động (heap / 힙) không phải kiểu (type / 타입) quy tắc (rule / 규칙) universal** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## Giá trị (value / 값) ngữ nghĩa (semantics / 의미론) và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)

Giá trị (value / 값) ngữ nghĩa (semantics / 의미론) coi variable chứa/bản sao (copy / 복사) giá trị (value / 값) conceptually; tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) coi variable giữ tham chiếu (reference / 참조) tới đối tượng (object / 객체) định danh (identity / 식별자). Nhưng languages có nhiều nuances: Java primitives vs đối tượng (object / 객체) references; C++ giá trị (value / 값)/tham chiếu (reference / 참조)/pointer; Python names bind objects; JavaScript primitives immutable values còn objects referenced.

Aliasing xuất hiện khi nhiều references trỏ cùng mutable đối tượng (object / 객체). Mutation qua một alias observable ở alias khác, làm lập luận (reasoning / 추론) phức tạp và cần synchronization trong tính đồng thời (concurrency / 동시성).

> **Nối mạch:** **Ngăn xếp (stack / 스택) và vùng nhớ động (heap / 힙) không phải kiểu (type / 타입) quy tắc (rule / 규칙) universal** nối từ **Giá trị (value / 값) ngữ nghĩa (semantics / 의미론) và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)** sang **Manual management, RAII và garbage collection**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ngăn xếp (stack / 스택) và vùng nhớ động (heap / 힙) không phải kiểu (type / 타입) quy tắc (rule / 규칙) universal

Ngăn xếp (stack / 스택) thường phục vụ lời gọi (call / 호출) frames và automatic lifetimes; vùng nhớ động (heap / 힙) phục vụ động (dynamic / 동적) lifetimes. Nhưng trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) có thể escape-analyze, scalar replace, allocate boxes hoặc move objects. Vì vậy “cục bộ (local / 로컬) variable nằm ngăn xếp (stack / 스택), đối tượng (object / 객체) nằm vùng nhớ động (heap / 힙)” chỉ là rough hiện thực (implementation / 구현) mô hình (model / 모델) ở một số environments.

Xem OS bộ nhớ (memory / 메모리) ở [Virtual Memory](../03_operating_systems/03_virtual_memory_and_address_spaces.md).

> **Nối mạch:** **Manual management, RAII và garbage collection** nối từ **Ngăn xếp (stack / 스택) và vùng nhớ động (heap / 힙) không phải kiểu (type / 타입) quy tắc (rule / 규칙) universal** sang **GC và generational hypothesis**, vì cơ chế trước tạo đầu vào cho bước sau.

## Manual management, RAII và garbage collection

C `malloc/free` đặt responsibility reclaim vào programmer. C++ RAII gắn tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) với đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명)/destructors. Rust quyền sở hữu (ownership / 소유권)/borrowing dùng static rules để kiểm soát aliases/lifetimes và deterministic drop mà không tracing GC.

Tracing GC bắt đầu từ roots, mark reachable objects, reclaim unreachable. Mark-sweep, copying, generational và concurrent collectors có trade-offs pause, thông lượng (throughput / 처리량), footprint.

Tham chiếu (reference / 참조) counting reclaim khi count về zero, deterministic hơn nhưng cycles cần xử lý; increments/decrements có overhead.

> **Nối mạch:** **GC và generational hypothesis** nối từ **Manual management, RAII và garbage collection** sang **Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명)**, vì cơ chế trước tạo đầu vào cho bước sau.

## GC và generational hypothesis

Nhiều managed heaps tận dụng observation rằng nhiều objects “die young”. Young generation collection scan vùng nhỏ thường xuyên; survivors promote. Long-lived objects ít scan hơn.

Ghi (write / 쓰기) barriers/card tables nhánh học (track / 트랙) references giữa generations để collector không phải scan toàn old vùng nhớ động (heap / 힙) mỗi young collection.

GC tuning là sự đánh đổi (trade-off / 트레이드오프) độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và bộ nhớ (memory / 메모리) headroom, không phải chỉ “increase vùng nhớ động (heap / 힙)”.

> **Nối mạch:** sau nội dung của **GC và generational hypothesis**, **Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu; **Null và optionality** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명)

Quyền sở hữu (ownership / 소유권) trả lời ai chịu trách nhiệm tài nguyên (resource / 자원). tệp (file / 파일) descriptor, socket, DB liên kết (connection / 연결) và bộ nhớ (memory / 메모리) đều có thời gian tồn tại (lifetime / 수명). Memory-safe ngôn ngữ (language / 언어) vẫn có tài nguyên (resource / 자원) leaks nếu liên kết (connection / 연결) không close; GC chỉ reclaim bộ nhớ (memory / 메모리)/đối tượng (object / 객체), không guarantee timely bản phát hành (release / 릴리스) bên ngoài (external / 외부) resources.

`try-with-resources`, `defer`, `using`, RAII hay ngữ cảnh (context / 맥락) manager encode deterministic cleanup.

> **Nối mạch:** **Null và optionality** nối từ **Quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명)** sang **Variance và generics ở intuition mức (level / 수준)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Null và optionality

Null tham chiếu (reference / 참조) đại diện absence nhưng cho phép “missing” xâm nhập mọi tham chiếu (reference / 참조) kiểu (type / 타입) nếu ngôn ngữ (language / 언어) không distinguish. Option/Maybe/nullable types đưa absence vào hệ kiểu (type system / 타입 시스템), buộc caller handle branches.

Không có biểu diễn (representation / 표현) miễn phí: tagged union có tag, nullable pointer có thể exploit invalid/null bit patterns. Nhưng ngữ nghĩa (semantic / 의미적) clarity thường quan trọng hơn byte tối ưu.

> **Nối mạch:** **Variance và generics ở intuition mức (level / 수준)** nối từ **Null và optionality** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Variance và generics ở intuition mức (level / 수준)

Nếu Dog <: Animal, `List<Dog>` có phải subtype `List<Animal>`? Nếu mutable danh sách (list / 목록) cho insert Animal, điều đó phá danh sách (list / 목록) chó. Vì vậy mutable generics thường bất biến (invariant / 불변식); read-only producers có thể covariant, consumers contravariant theo positions.

Java wildcard mnemonic PECS — Producer Extends, bên tiêu thụ (consumer / 소비자) Super — xuất phát từ lô-gic (logic / 논리) variance này, không phải quy tắc (rule / 규칙) ngẫu nhiên.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Variance và generics ở intuition mức (level / 수준)**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> hệ kiểu (type system / 타입 시스템) quản lý **sets of values + allowed operations + các giả định (assumptions / 가정들)**. bộ nhớ (memory / 메모리) mô hình (model / 모델) quản lý **định danh (identity / 식별자), aliasing, thời gian tồn tại (lifetime / 수명) và reclamation**. Bugs thường xuất hiện khi các giả định (assumptions / 가정들) về hai lớp này không khớp.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“GC nghĩa không có bộ nhớ (memory / 메모리) leak.”** Reachable-but-unused objects, caches/listeners và bản địa (native / 네이티브) resources vẫn leak.

**“tham chiếu (reference / 참조) là bộ nhớ (memory / 메모리) address.”** thời gian chạy (runtime / 런타임) có thể move objects/encode references; ngữ nghĩa (semantic / 의미적) tham chiếu (reference / 참조) không bắt buộc expose raw address.

**“Static hệ kiểu (type system / 타입 시스템) chứng minh program đúng.”** Nó loại classes lỗi trong mô hình (model / 모델) của hệ kiểu (type system / 타입 시스템), không chứng minh mọi nghiệp vụ (business / 비즈니스)/thuộc tính (property / 속성) tính đúng đắn (correctness / 정확성).

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

[Machine representation](../00_computation_information/02_numbers_and_machine_representation.md) giải thích bits; [memory layout](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) giải thích locality; [GC/runtime](./03_compilers_interpreters_vm_and_jit.md) hiện thực thời gian tồn tại (lifetime / 수명); [concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) làm aliasing mutable nguy hiểm.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
