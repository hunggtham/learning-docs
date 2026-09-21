# Algebraic data types, variance và type inference

Type system không chỉ gắn nhãn `int`, `String` hay `User`. Ở mức advanced, type trở thành một ngôn ngữ mô tả **shape của state hợp lệ**, cách các shape kết hợp và quan hệ substitutability giữa chúng. Algebraic Data Types, variance và inference là ba mảnh giúp xây API vừa biểu đạt mạnh vừa giảm invalid states.

## Product type: nhiều phần cùng tồn tại

Một record/object đơn giản có thể được nhìn như product type:

```text
User = Name × Email × Age
```

Một value `User` chứa đồng thời một value của mỗi component. Nếu `Name` có `a` khả năng và `Age` có `b` khả năng hữu hạn, product có khoảng `a*b` combinations.

Struct, tuple, record và class data-holder thường mang intuition này.

## Sum type: một trong nhiều case

Sum type biểu diễn value thuộc **một trong các alternatives**:

```text
PaymentResult = Success(Receipt)
              | Declined(Reason)
              | Retryable(Error)
```

Thay vì object có nhiều nullable fields và flag khó đồng bộ, sum type encode trực tiếp state machine hợp lệ.

Trong Rust có `enum`, Kotlin có sealed hierarchy, TypeScript có discriminated union, functional languages có ADT native. Java sealed types + records giúp gần hơn mô hình này.

## Invalid state explosion

Giả sử API dùng:

```text
status: string
receipt: Receipt?
error: Error?
```

Ta có thể tạo trạng thái vô nghĩa như `status=SUCCESS` nhưng `receipt=null`, hoặc vừa có receipt vừa error.

ADT chuyển nhiều rule runtime thành rule construction/type checking. Đây là ví dụ principle: **make invalid states unrepresentable** khi chi phí phù hợp.

## Pattern matching và exhaustiveness

Nếu sum type có tập cases đóng, compiler có thể kiểm tra pattern matching đã xử lý đủ case chưa.

Khi thêm case mới, compile error ở các match site trở thành một dạng impact analysis tự động.

Điều này mạnh hơn chuỗi `if(status == "...")` phân tán vì relationship giữa variants và consumers được type system theo dõi.

## Parametric polymorphism

Generic type như `List<T>` cho phép viết algorithm độc lập type cụ thể. Nhưng câu hỏi khó xuất hiện khi có subtype relation.

Nếu `Dog <: Animal`, liệu `List<Dog> <: List<Animal>`? Không tự động. Nếu cho phép và `List<Animal>` có method add, ta có thể add `Cat` vào list thực chất là `List<Dog>`, phá type safety.

## Variance

**Covariance** cho phép quan hệ đi cùng chiều: `Producer<Dog>` có thể dùng nơi cần `Producer<Animal>` nếu interface chỉ produce `T`.

**Contravariance** đi ngược chiều: consumer có thể nhận broader type. Một `Consumer<Animal>` dùng được nơi cần consumer của `Dog` vì nó biết xử lý mọi Animal.

**Invariance** không cho subtype relation giữa parameterized types.

Mental model hữu ích:

```text
output position  -> covariance thường hợp lý
input position   -> contravariance thường hợp lý
both directions  -> invariance thường cần thiết
```

Đây là intuition, không thay formal rules của từng language.

## Java/Kotlin examples

Java dùng wildcard-site variance như `? extends T` và `? super T`.

PECS mnemonic — Producer Extends, Consumer Super — hữu ích nhưng nên hiểu qua direction dữ liệu chứ không học thuộc khẩu hiệu.

Kotlin hỗ trợ declaration-site variance `out`/`in`, giúp contract variance nằm ở type declaration khi phù hợp.

## Type inference là constraint solving

Khi compiler suy ra type, nó không “đoán” bằng AI. Nó thu thập constraints từ literals, function applications, assignments và generic parameters rồi tìm substitution thỏa rules.

Ví dụ conceptual:

```text
identity(x) = x
```

Nếu không có operation nào yêu cầu type cụ thể, compiler có thể suy ra polymorphic form tương tự `T -> T` trong hệ thống phù hợp.

Type inference phức tạp hơn khi có subtyping, overload, higher-rank polymorphism hoặc effects. Language thường giới hạn inference để compile time/diagnostics còn kiểm soát được.

## Local inference vs global inference

Một số language suy type mạnh trong function body nhưng yêu cầu public API annotation. Đây là design trade-off tốt cho maintainability: implementation có ergonomics, boundary vẫn explicit.

Nếu inference lan quá xa, error message có thể xuất hiện cách xa nguyên nhân và refactor thay type ngoài ý muốn.

## Higher-kinded abstraction intuition

Type parameter thường đại diện một concrete type `T`. Higher-kinded abstraction cho phép parameter hóa trên **type constructor** như `F<_>` — ví dụ “một context/container bất kỳ”.

Nó hữu ích để biểu đạt patterns như mapping/traversal chung, nhưng tăng complexity type system đáng kể. Java không có higher-kinded types trực tiếp; ecosystems mô phỏng bằng interface patterns với ergonomic cost.

## Mental Model

> Product type mô tả “A và B”; sum type mô tả “A hoặc B”; generics mô tả structure độc lập element type; variance kiểm soát direction substitutability; inference giải constraints để giảm annotation mà vẫn giữ static guarantees.

## Common Misconceptions

**“Generic collection của subtype luôn là subtype collection.”** Mutable collection làm điều này unsafe nếu vừa đọc vừa ghi.

**“Type inference nghĩa compiler biết business meaning.”** Nó chỉ giải constraints trong type rules.

**“ADT chỉ dành cho functional programming.”** Sealed classes, enums có payload và discriminated unions mang cùng mental model trong OOP/TypeScript ecosystems.

## Kết nối

Chapter tiếp theo về ownership cho thấy type system còn có thể encode resource lifetime. Với Java backend, variance xuất hiện trực tiếp trong generic APIs; với TypeScript/React, discriminated unions rất hữu ích cho UI/request state machines.