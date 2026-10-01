# Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Cú pháp (syntax / 문법), ngữ nghĩa (semantics / 의미론) và pragmatics** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Static và động (dynamic / 동적) ngữ nghĩa (semantics / 의미론)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Programming ngôn ngữ (language / 언어) là một formal hệ thống (system / 시스템) để mô tả computation cho cả con người và hiện thực (implementation / 구현) tools. cú pháp (syntax / 문법) chỉ trả lời “viết thế nào”; ngữ nghĩa (semantics / 의미론) trả lời “chương trình đó có nghĩa gì”. Hai languages có cú pháp (syntax / 문법) giống nhau nhưng evaluation, kiểu (type / 타입) conversion, bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성) hoặc lỗi (error / 오류) ngữ nghĩa (semantics / 의미론) khác nhau có thể tạo hành vi (behavior / 동작) rất khác.

## Cú pháp (syntax / 문법), ngữ nghĩa (semantics / 의미론) và pragmatics

Cú pháp (syntax / 문법) định nghĩa chuỗi đơn vị từ (token / 토큰)/construct nào hợp lệ. ngữ nghĩa (semantics / 의미론) gán meaning cho constructs. Pragmatics liên quan cách ngôn ngữ (language / 언어) được dùng hiệu quả trong ecosystem.

Ví dụ `a + b` syntactically đơn giản nhưng ngữ nghĩa (semantics / 의미론) phụ thuộc types: integer addition, floating-point addition, string concatenation, overloaded operator hoặc user-defined phương thức (method / 메서드) dispatch.

Parser chỉ xác định cấu trúc (structure / 구조) không đủ để biết kết quả (result / 결과); kiểu (type / 타입) checker/thời gian chạy (runtime / 런타임) phải áp ngữ nghĩa (semantic / 의미적) rules.

> **Chuyển mạch:** Trong **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Static và động (dynamic / 동적) ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **Cú pháp (syntax / 문법), ngữ nghĩa (semantics / 의미론) và pragmatics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình thực thi (execution model / 실행 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Static và động (dynamic / 동적) ngữ nghĩa (semantics / 의미론)

Static ngữ nghĩa (semantics / 의미론) là properties có thể kiểm tra trước thực thi (execution / 실행), như name resolution hoặc kiểu (type / 타입) các ràng buộc (constraints / 제약조건들). động (dynamic / 동적) ngữ nghĩa (semantics / 의미론) mô tả evaluation khi program chạy.

“Static vs động (dynamic / 동적) ngôn ngữ (language / 언어)” thường bị dùng quá rộng. kiểu (type / 타입) checking thời gian (time / 시간), binding thời gian (time / 시간), dispatch, bộ nhớ (memory / 메모리) allocation và mã (code / 코드) generation là những dimensions riêng. Python động (dynamic / 동적) typing không nghĩa mọi quyết định đều thời gian chạy (runtime / 런타임); Java static typing vẫn có động (dynamic / 동적) dispatch và JIT compilation.

> **Chuyển mạch:** Ở chặng này của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Mô hình thực thi (execution model / 실행 모델)** tiếp nhận điểm tựa từ **Static và động (dynamic / 동적) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình thực thi (execution model / 실행 모델)

Một nguồn (source / 소스) program có thể đi qua nhiều chuỗi xử lý (pipeline / 파이프라인):

```text
source
  ↓ parse / analyze
AST / IR
  ↓ compile or interpret
bytecode / machine code / evaluator
  ↓ runtime + OS
CPU / memory / I/O
```

C, Rust thường ahead-of-time compile bản địa (native / 네이티브) mã (code / 코드). Java compile nguồn (source / 소스) → JVM bytecode rồi trình thông dịch (interpreter / 인터프리터)/JIT execute. JavaScript engines parse → nội bộ (internal / 내부) IR/bytecode → JIT optimize hot paths. Python CPython compile nguồn (source / 소스) → bytecode và evaluate trên VM, dù hiện thực (implementation / 구현) alternatives tồn tại.

“Compiled vs interpreted” vì vậy không phải nhị phân (binary / 이진) classification của ngôn ngữ (language / 언어); nó là hiện thực (implementation / 구현) chiến lược (strategy / 전략).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Evaluation thứ tự (order / 순서)** tiếp nhận điểm tựa từ **Mô hình thực thi (execution model / 실행 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Name binding và môi trường (environment / 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation thứ tự (order / 순서)

Ngôn ngữ (language / 언어) quy định hoặc để unspecified thứ tự (order / 순서) expression evaluation. Side effects khiến thứ tự (order / 순서) quan trọng. Short-circuit Boolean operators thường chỉ evaluate RHS khi cần. Lazy languages trì hoãn evaluation; eager languages evaluate arguments trước lời gọi (call / 호출) theo rules.

Nếu mã (code / 코드) phụ thuộc unspecified thứ tự (order / 순서), portability/tính đúng đắn (correctness / 정확성) dễ vỡ.

> **Chuyển mạch:** Trong **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Name binding và môi trường (environment / 환경)** tiếp nhận điểm tựa từ **Evaluation thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mutable trạng thái (state / 상태) và effects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Name binding và môi trường (environment / 환경)

Identifier như `x` phải được resolved tới binding. Lexical/static scoping dựa nguồn (source / 소스) nesting; động (dynamic / 동적) scoping dựa lời gọi (call / 호출) chuỗi (chain / 사슬) thời gian chạy (runtime / 런타임). Most mainstream languages dùng lexical phạm vi (scope / 범위).

Môi trường (environment / 환경) có thể conceptualize ánh xạ (mapping / 매핑) names → locations/values. Closure giữ môi trường (environment / 환경) cần thiết để hàm (function / 함수) tiếp tục truy cập (access / 접근) lexical variables sau outer hàm (function / 함수) return.

> **Chuyển mạch:** Ở chặng này của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Mutable trạng thái (state / 상태) và effects** tiếp nhận điểm tựa từ **Name binding và môi trường (environment / 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Determinism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mutable trạng thái (state / 상태) và effects

Expression thuần (pure) cho same đầu vào (input / 입력) cùng đầu ra (output / 출력) và không observable side effects. Imperative languages cho statements mutate trạng thái (state / 상태). I/O, exceptions, thời gian (time / 시간), randomness và dùng chung (shared / 공유) bộ nhớ (memory / 메모리) đều là effects.

Functional programming không xóa effects khỏi reality; nó cố isolate/mô hình (model / 모델) chúng để lập luận (reasoning / 추론) dễ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Determinism** tiếp nhận điểm tựa từ **Mutable trạng thái (state / 상태) và effects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngôn ngữ (language / 언어) specification vs hiện thực (implementation / 구현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Determinism

Program deterministic khi cùng relevant trạng thái (state / 상태)/đầu vào (input / 입력) tạo same observable kết quả (result / 결과). Randomness, thời gian (time / 시간), I/O, tính đồng thời (concurrency / 동시성) và undefined hành vi (behavior / 동작) làm determinism khó hơn. Reproducible builds/tests cố kiểm soát hidden inputs như timezone, locale, random seed và phụ thuộc (dependency / 의존성) versions.

> **Chuyển mạch:** Trong **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Ngôn ngữ (language / 언어) specification vs hiện thực (implementation / 구현)** tiếp nhận điểm tựa từ **Determinism** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Undefined, unspecified và implementation-defined hành vi (behavior / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngôn ngữ (language / 언어) specification vs hiện thực (implementation / 구현)

Ngôn ngữ (language / 언어) spec định nghĩa đặc tả hợp đồng (contract / 계약); trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) hiện thực (implementation / 구현) có freedom tối ưu miễn observable hành vi (behavior / 동작) phù hợp. Java bộ nhớ (memory / 메모리) mô hình (model / 모델), ECMAScript spec hay C tiêu chuẩn (standard / 표준) là ví dụ ngữ nghĩa (semantic / 의미적) contracts.

Hiện thực (implementation / 구현) bug khác ngôn ngữ (language / 언어) quy tắc (rule / 규칙). Khi debugging subtle hành vi (behavior / 동작), cần biết câu hỏi đang thuộc spec, thời gian chạy (runtime / 런타임) hiện thực (implementation / 구현) hay thư viện (library / 라이브러리).

> **Chuyển mạch:** Ở chặng này của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Undefined, unspecified và implementation-defined hành vi (behavior / 동작)** tiếp nhận điểm tựa từ **Ngôn ngữ (language / 언어) specification vs hiện thực (implementation / 구현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Undefined, unspecified và implementation-defined hành vi (behavior / 동작)

C/C++ phân biệt các categories này. Undefined hành vi (behavior / 동작) không impose requirements, cho trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) freedom nhưng khiến lập luận (reasoning / 추론) nguy hiểm nếu program vi phạm. Implementation-defined yêu cầu hiện thực (implementation / 구현) document choice. Unspecified cho phép vài choices không cần document mỗi occurrence.

Managed languages thường giảm UB ở ứng dụng (application / 애플리케이션) mức (level / 수준) bằng checks/exceptions nhưng bản địa (native / 네이티브) boundaries và dữ liệu (data / 데이터) races vẫn có nuances.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Undefined, unspecified và implementation-defined hành vi (behavior / 동작)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Programming ngôn ngữ (language / 언어) là **đặc tả hợp đồng (contract / 계약) về meaning**, còn trình biên dịch (compiler / 컴파일러)/trình thông dịch (interpreter / 인터프리터)/thời gian chạy (runtime / 런타임) là machinery thực hiện đặc tả hợp đồng (contract / 계약). Đừng đồng nhất nguồn (source / 소스) construct với một hiện thực (implementation / 구현) vật lý duy nhất.

> **Chuyển mạch:** Trong **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Compiled ngôn ngữ (language / 언어) nhanh, interpreted ngôn ngữ (language / 언어) chậm.”** hiện thực (implementation / 구현), JIT, tải công việc (workload / 워크로드), thời gian chạy (runtime / 런타임) libraries và tối ưu hóa (optimization / 최적화) quan trọng; classification quá đơn giản.

**“Static typing nghĩa mọi thứ quyết định compile thời gian (time / 시간).”** động (dynamic / 동적) dispatch, allocation, reflection và JIT vẫn thời gian chạy (runtime / 런타임).

**“ngữ nghĩa (semantics / 의미론) chỉ là lý thuyết.”** Evaluation thứ tự (order / 순서), overflow, equality, bộ nhớ (memory / 메모리) mô hình (model / 모델) và exceptions đều là ngữ nghĩa (semantics / 의미론) gây bugs thực tế.

> **Chuyển mạch:** Ở chặng này của **Programming ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론) và thực thi (execution / 실행) các mô hình (models / 모델들)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Compiler/VM/JIT](./03_compilers_interpreters_vm_and_jit.md) hiện thực chuỗi xử lý (pipeline / 파이프라인); [types/memory](./01_types_values_references_and_memory.md) làm rõ values/thời gian tồn tại (lifetime / 수명); [CPU/ABI](../02_computer_architecture/04_machine_code_assembly_and_abi.md) là mục tiêu (target / 대상) bản địa (native / 네이티브); [concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) gặp ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
