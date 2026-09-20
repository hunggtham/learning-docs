# Type systems, generics và polymorphism

Type (kiểu / 타입) thường được học như nhãn `int`, `String`, `boolean`. Nhưng type system (타입 시스템) sâu hơn: nó là một static hoặc dynamic discipline dùng để phân loại values/expressions và giới hạn operations nhằm loại bỏ một lớp invalid programs hoặc định nghĩa runtime behavior rõ hơn.

## Type là một proposition về value

Nếu expression có type `int`, language cho phép một tập operations tương ứng và loại bỏ những operations không có semantics hợp lệ trong model đó.

Static typing kiểm tra nhiều properties trước runtime; dynamic typing gắn type information/checks nhiều hơn với runtime values. Đây là continuum thiết kế, không phải binary “an toàn vs không an toàn”.

Một static type system vẫn có thể có unsafe escape hatches; một dynamically typed language vẫn có memory safety và strong runtime checks.

## Type safety không đồng nghĩa business correctness

`transfer(Account from, Account to, Money amount)` có thể type-check hoàn hảo nhưng vẫn cho phép amount âm nếu type `Money` không encode constraint đó.

Type system chỉ bảo đảm properties mà nó biểu diễn. Một thiết kế richer type như `PositiveMoney` có thể chuyển invariant từ runtime check sang construction rule.

Đây là principle “make invalid states unrepresentable”, nhưng quá nhiều type complexity cũng tăng cognitive cost.

## Nominal và structural typing

Nominal typing dựa trên declared identity/relationship: class `UserId` khác `OrderId` dù internal representation cùng là integer nếu language dùng nominal identity.

Structural typing dựa trên shape/capabilities: nếu object có các fields/methods cần thiết thì có thể satisfy type. TypeScript interfaces thường thể hiện structural behavior.

Hai models ảnh hưởng API evolution, compatibility và abstraction boundary.

## Subtyping và substitutability

Nếu `S` là subtype của `T`, value `S` có thể dùng ở nơi `T` được yêu cầu mà không phá contract. Đây là tinh thần của Liskov Substitution Principle.

Inheritance syntax không tự đảm bảo semantic substitutability. Một subclass có thể type-compatible nhưng strengthen precondition hoặc weaken postcondition theo cách phá caller assumptions.

## Parametric polymorphism và generics

Generic function như `identity<T>(x: T): T` làm việc đồng nhất cho mọi `T`. Đây là parametric polymorphism.

Generic containers như `List<T>` cho phép reuse data structure mà vẫn giữ type relation giữa input/output.

Implementation có thể monomorphize thành version riêng cho mỗi concrete type (như nhiều trường hợp C++ templates/Rust generics) hoặc erase type parameters ở runtime (như Java type erasure cho nhiều generics). Trade-off là code size, specialization performance và runtime type information.

## Variance

Nếu `Cat <: Animal`, có phải `List<Cat> <: List<Animal>`? Không phải luôn.

Nếu mutable `List<Cat>` được coi là `List<Animal>`, caller có thể insert `Dog`, phá invariant. Read-only producer có thể covariance an toàn hơn; consumer có thể contravariance.

Java wildcard rule “Producer Extends, Consumer Super” là practical reflection của variance theory.

## Sum types và product types

Product type kết hợp nhiều fields cùng tồn tại, như tuple/record. Sum type biểu diễn một trong nhiều alternatives, như enum có payload hoặc algebraic data type.

Ví dụ result:

```text
Result<T, E> = Ok(T) | Error(E)
```

encode success/failure vào type thay vì sentinel `null` hoặc exception-only protocol.

Pattern matching có thể buộc exhaustiveness, giúp compiler phát hiện case bị bỏ sót.

## Nullability và option types

Nếu `null` có thể xuất hiện ở hầu hết reference types, nhiều invalid states lan vào program. Nullable type `T?` hoặc `Option<T>` tách “có value” và “không có value” thành explicit type state.

Static nullability không loại mọi null bug, nhưng thu hẹp nơi cần reasoning.

## Gradual typing

Một số languages kết hợp static và dynamic typing. TypeScript thêm static layer trên JavaScript nhưng erase types khi emit JS. Python type hints chủ yếu phục vụ tools/checkers chứ runtime semantics mặc định không enforce toàn bộ annotations.

Điều này cho phép adoption từng bước nhưng boundary typed/untyped cần được validate.

## Common Misconceptions

**“Static typing làm program đúng.”** Nó chỉ chứng minh một tập properties theo type system; logic, concurrency và business bugs vẫn tồn tại.

**“Dynamic typing nghĩa là không có types.”** Values vẫn có runtime types; khác ở thời điểm và cơ chế checking.

**“Inheritance và subtyping là cùng một thứ.”** Inheritance là reuse/nominal mechanism; semantic substitutability là property mạnh hơn.

## Mental Model

> Type system là một language nhỏ bên trong language lớn, mô tả những states/operations nào được coi là hợp lệ trước hoặc trong runtime.

## Kết nối

Đọc cùng [values/references/memory](./01_types_values_references_and_memory.md), [language semantics](./00_language_semantics_and_execution_models.md), [API contracts](../08_software_systems/00_abstraction_modularity_interfaces_and_apis.md) và các note Java/TypeScript trong repo để thấy cùng concepts được triển khai khác nhau.