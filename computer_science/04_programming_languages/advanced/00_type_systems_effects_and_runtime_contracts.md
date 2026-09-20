# Type systems, effects và runtime contracts

Type system không chỉ phân loại `int`, `string` hay `User`. Ở mức advanced, nó là một static reasoning framework dùng để loại bỏ một tập program states trước runtime. Điều quan trọng là hiểu **property nào được encode**, property nào vẫn nằm ngoài type system, và cost ergonomics/expressiveness của mỗi lựa chọn.

## Type judgment như một statement có điều kiện

Notation dạng `Γ ⊢ e : T` có thể đọc: dưới environment `Γ`, expression `e` có type `T`. `Γ` chứa assumptions/bindings về variables. Type checker thực hiện các inference rules để xây derivation hoặc báo rằng derivation không tồn tại.

Cách nhìn này giúp tách syntax khỏi semantics: type checker không “đoán kiểu” tùy ý; nó thực hiện proof theo rules của language.

## Soundness và progress/preservation intuition

Một type system thường muốn property gần với: well-typed program không rơi vào một class invalid runtime states. Formalization cổ điển dùng **progress** và **preservation**. Progress: well-typed expression hoặc đã là value hoặc có bước evaluation tiếp. Preservation: một bước evaluation không phá type validity.

Điều này không có nghĩa program đúng business logic. Type safety chỉ bảo vệ các invariants mà type system encode.

## Subtyping và variance

Nếu `Dog <: Animal`, điều đó không tự động suy ra `List<Dog> <: List<Animal>`. Nếu mutable list covariance được cho phép, caller có thể insert `Cat` vào list thực chất chỉ chứa Dog. Vì vậy variance phụ thuộc position đọc/ghi và semantic contract.

Covariance phù hợp producer/read-only; contravariance thường xuất hiện ở consumer/function parameter; invariance là lựa chọn an toàn cho mutable containers phổ biến.

## ADT và invalid states

Algebraic Data Types cho phép model domain bằng sum/product types. Thay vì hai booleans `isLoading` và `hasError` tạo bốn combinations trong đó có state vô nghĩa, ta có thể encode:

```text
State = Loading | Success(Data) | Failure(Error)
```

Pattern matching exhaustiveness biến missing-case thành compile-time signal. Đây là ví dụ “make invalid states unrepresentable”.

## Effect là phần semantics ngoài return type

Hai functions cùng `User -> User` có thể rất khác nếu một function đọc DB, ghi log, throw exception hoặc mutate global state. Effect system cố đưa một phần side-effect information vào type/checking layer.

Có nhiều hình thức: checked exceptions, `async` effects, capability types, effect rows, monadic encodings hoặc ownership/borrow restrictions. Mục tiêu chung là làm hidden interaction trở nên explicit để composition dễ reasoning hơn.

## Gradual typing và trust boundary

TypeScript, Python typing và nhiều ecosystem cho phép typed và untyped code cùng tồn tại. Static checker chỉ guarantee trong phạm vi assumptions của nó. Khi data đi từ JSON, database, network hay dynamic module vào typed domain, runtime validation vẫn cần thiết.

Một `as User` cast không biến untrusted bytes thành User đúng nghĩa; nó chỉ thay belief của compiler. Đây là boundary giữa **static claim** và **runtime evidence**.

## Runtime contracts vẫn cần tồn tại

Không phải property nào cũng phù hợp static types. Range phụ thuộc config, permission phụ thuộc session, uniqueness phụ thuộc database state, latency phụ thuộc system load. Assertions, schemas, DB constraints, protocol validation và tests bổ sung cho type system.

Thiết kế senior không hỏi “type system hay runtime validation tốt hơn”; nó đặt invariant ở layer có đủ information để enforce.

## Mental Model

> Type system là một proof/constraint layer trước runtime; effect system mở rộng proof đó sang interaction; runtime contract bảo vệ những facts chỉ biết khi chương trình đang chạy.

## Kết nối

Xem [type foundation](../../basic/04_programming_languages/06_type_systems_generics_and_polymorphism.md), [errors/resources](../../basic/04_programming_languages/05_errors_resources_and_runtime_safety.md) và [API contracts](../../basic/08_software_systems/00_abstraction_modularity_interfaces_and_apis.md).