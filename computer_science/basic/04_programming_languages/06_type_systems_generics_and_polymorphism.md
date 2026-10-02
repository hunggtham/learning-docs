# Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Type systems, generics và polymorphism**. Route đi từ type proposition/typing judgment → generics và variance → subtyping/dispatch → abstraction boundaries, để type safety được phân biệt với business correctness.

Kiểu (type / 타입) thường được học như nhãn `int`, `String`, `boolean`. Nhưng hệ kiểu (type system / 타입 시스템) sâu hơn: nó là một static hoặc động (dynamic / 동적) discipline dùng để phân loại values/expressions và giới hạn operations nhằm loại bỏ một lớp invalid programs hoặc định nghĩa hành vi thời gian chạy (runtime behavior / 런타임 동작) rõ hơn.

## Kiểu (type / 타입) là một proposition về giá trị (value / 값)

Nếu expression có kiểu (type / 타입) `int`, ngôn ngữ (language / 언어) cho phép một tập operations tương ứng và loại bỏ những operations không có ngữ nghĩa (semantics / 의미론) hợp lệ trong mô hình (model / 모델) đó.

Static typing kiểm tra nhiều properties trước thời gian chạy (runtime / 런타임); động (dynamic / 동적) typing gắn kiểu (type / 타입) thông tin (information / 정보)/checks nhiều hơn với thời gian chạy (runtime / 런타임) values. Đây là continuum thiết kế, không phải nhị phân (binary / 이진) “an toàn vs không an toàn”.

Một static hệ kiểu (type system / 타입 시스템) vẫn có thể có unsafe escape hatches; một dynamically typed ngôn ngữ (language / 언어) vẫn có bộ nhớ (memory / 메모리) an toàn (safety / 안전) và strong thời gian chạy (runtime / 런타임) checks.

> **Chuyển mạch:** Trong **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Kiểu (type / 타입) an toàn (safety / 안전) không đồng nghĩa nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **Kiểu (type / 타입) là một proposition về giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nominal và structural typing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểu (type / 타입) an toàn (safety / 안전) không đồng nghĩa nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성)

`transfer(Account from, Account to, Money amount)` có thể type-check hoàn hảo nhưng vẫn cho phép amount âm nếu kiểu (type / 타입) `Money` không encode ràng buộc (constraint / 제약조건) đó.

Hệ kiểu (type system / 타입 시스템) chỉ bảo đảm properties mà nó biểu diễn. Một thiết kế richer kiểu (type / 타입) như `PositiveMoney` có thể chuyển bất biến (invariant / 불변식) từ thời gian chạy (runtime / 런타임) check sang construction quy tắc (rule / 규칙).

Đây là principle “make invalid states unrepresentable”, nhưng quá nhiều kiểu (type / 타입) độ phức tạp (complexity / 복잡도) cũng tăng cognitive chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Nominal và structural typing** tiếp nhận điểm tựa từ **Kiểu (type / 타입) an toàn (safety / 안전) không đồng nghĩa nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Subtyping và substitutability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nominal và structural typing

Nominal typing dựa trên declared định danh (identity / 식별자)/relationship: lớp (class / 클래스) `UserId` khác `OrderId` dù nội bộ (internal / 내부) biểu diễn (representation / 표현) cùng là integer nếu ngôn ngữ (language / 언어) dùng nominal định danh (identity / 식별자).

Structural typing dựa trên shape/capabilities: nếu đối tượng (object / 객체) có các fields/methods cần thiết thì có thể satisfy kiểu (type / 타입). TypeScript interfaces thường thể hiện structural hành vi (behavior / 동작).

Hai các mô hình (models / 모델들) ảnh hưởng API evolution, tính tương thích (compatibility / 호환성) và lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Subtyping và substitutability** tiếp nhận điểm tựa từ **Nominal và structural typing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parametric polymorphism và generics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Subtyping và substitutability

Nếu `S` là subtype của `T`, giá trị (value / 값) `S` có thể dùng ở nơi `T` được yêu cầu mà không phá đặc tả hợp đồng (contract / 계약). Đây là tinh thần của Liskov Substitution Principle.

Inheritance cú pháp (syntax / 문법) không tự đảm bảo ngữ nghĩa (semantic / 의미적) substitutability. Một subclass có thể type-compatible nhưng strengthen precondition hoặc weaken postcondition theo cách phá caller các giả định (assumptions / 가정들).

> **Chuyển mạch:** Trong **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Parametric polymorphism và generics** tiếp nhận điểm tựa từ **Subtyping và substitutability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parametric polymorphism và generics

Generic hàm (function / 함수) như `identity<T>(x: T): T` làm việc đồng nhất cho mọi `T`. Đây là parametric polymorphism.

Generic containers như `List<T>` cho phép reuse cấu trúc dữ liệu (data structure / 자료구조) mà vẫn giữ kiểu (type / 타입) quan hệ (relation / 관계) giữa đầu vào (input / 입력)/đầu ra (output / 출력).

Hiện thực (implementation / 구현) có thể monomorphize thành phiên bản (version / 버전) riêng cho mỗi concrete kiểu (type / 타입) hoặc erase kiểu (type / 타입) parameters ở thời gian chạy (runtime / 런타임) (như Java type erasure cho nhiều generics). sự đánh đổi (trade-off / 트레이드오프) là mã (code / 코드) kích thước (size / 크기), specialization hiệu năng (performance / 성능) và thời gian chạy (runtime / 런타임) kiểu (type / 타입) thông tin (information / 정보).

> **Chuyển mạch:** Ở chặng này của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Variance** tiếp nhận điểm tựa từ **Parametric polymorphism và generics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sum types và sản phẩm (product / 제품) types** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variance

Nếu `Cat <: Animal`, có phải `List<Cat> <: List<Animal>`? Không phải luôn.

Nếu mutable `List<Cat>` được coi là `List<Animal>`, caller có thể insert `Dog`, phá bất biến (invariant / 불변식). Read-only producer có thể covariance an toàn hơn; bên tiêu thụ (consumer / 소비자) có thể contravariance.

Java wildcard quy tắc (rule / 규칙) “Producer Extends, bên tiêu thụ (consumer / 소비자) Super” là practical reflection của variance lý thuyết (theory / 이론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Sum types và sản phẩm (product / 제품) types** tiếp nhận điểm tựa từ **Variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nullability và option types** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sum types và sản phẩm (product / 제품) types

Sản phẩm (product / 제품) kiểu (type / 타입) kết hợp nhiều fields cùng tồn tại, như tuple/bản ghi (record / 레코드). Sum kiểu (type / 타입) biểu diễn một trong nhiều alternatives, như enum có payload hoặc algebraic dữ liệu (data / 데이터) kiểu (type / 타입).

Ví dụ kết quả (result / 결과):

```text
Result<T, E> = Ok(T) | Error(E)
```

encode success/thất bại (failure / 실패) vào kiểu (type / 타입) thay vì sentinel `null` hoặc exception-only giao thức (protocol / 프로토콜).

Mẫu (pattern / 패턴) matching có thể buộc exhaustiveness, giúp trình biên dịch (compiler / 컴파일러) phát hiện trường hợp (case / 사례) bị bỏ sót.

> **Chuyển mạch:** Trong **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Sum types và sản phẩm (product / 제품) types** cho ta quy tắc; **Nullability và option types** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Gradual typing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nullability và option types

Nếu `null` có thể xuất hiện ở hầu hết tham chiếu (reference / 참조) types, nhiều invalid states lan vào program. Nullable kiểu (type / 타입) `T?` hoặc `Option<T>` tách “có giá trị (value / 값)” và “không có giá trị (value / 값)” thành tường minh (explicit / 명시적) kiểu (type / 타입) trạng thái (state / 상태).

Static nullability không loại mọi null bug, nhưng thu hẹp nơi cần lập luận (reasoning / 추론).

> **Chuyển mạch:** Ở chặng này của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Nullability và option types** cho ta quy tắc; **Gradual typing** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gradual typing

Một số languages kết hợp static và động (dynamic / 동적) typing. TypeScript thêm static tầng (layer / 계층) trên JavaScript nhưng erase types khi emit JS. Python kiểu (type / 타입) hints chủ yếu phục vụ tools/checkers chứ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) mặc định không enforce toàn bộ annotations.

Điều này cho phép adoption từng bước nhưng ranh giới (boundary / 경계) typed/untyped cần được validate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Gradual typing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Static typing làm program đúng.”** Nó chỉ chứng minh một tập properties theo hệ kiểu (type system / 타입 시스템); lô-gic (logic / 논리), tính đồng thời (concurrency / 동시성) và nghiệp vụ (business / 비즈니스) bugs vẫn tồn tại.

**“động (dynamic / 동적) typing nghĩa là không có types.”** Values vẫn có thời gian chạy (runtime / 런타임) types; khác ở thời điểm và cơ chế checking.

**“Inheritance và subtyping là cùng một thứ.”** Inheritance là reuse/nominal cơ chế (mechanism / 메커니즘); ngữ nghĩa (semantic / 의미적) substitutability là thuộc tính (property / 속성) mạnh hơn.

> **Chuyển mạch:** Trong **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> hệ kiểu (type system / 타입 시스템) là một ngôn ngữ (language / 언어) nhỏ bên trong ngôn ngữ (language / 언어) lớn, mô tả những states/operations nào được coi là hợp lệ trước hoặc trong thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Ở chặng này của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), generics và polymorphism**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [values/references/memory](./01_types_values_references_and_memory.md), [language semantics](./00_language_semantics_and_execution_models.md), [API contracts](../08_software_systems/00_abstraction_modularity_interfaces_and_apis.md) và các ghi chú (note / 노트) Java/TypeScript trong repo để thấy cùng concepts được triển khai khác nhau.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
