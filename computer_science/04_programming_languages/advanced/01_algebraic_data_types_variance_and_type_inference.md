# Algebraic data types, variance và type inference

Type system không chỉ ngăn việc cộng string với integer. Ở mức sâu hơn, type là ngôn ngữ mô tả **shape của state**, operation nào hợp lệ và quan hệ nào compiler có thể chứng minh trước runtime. Algebraic data types, variance và type inference là ba mảnh quan trọng để hiểu vì sao generic API có thể vừa expressive vừa safe.

## Product type: nhiều giá trị cùng tồn tại

Một record như `User(name, age)` chứa đồng thời `name` **và** `age`. Trong type theory, đây là **product type (곱 타입)**. Số trạng thái khả dĩ của product gần với tích số trạng thái của từng field.

Struct, tuple, record và class data object thường mang trực giác product: một value được tạo từ nhiều component cùng hiện diện.

## Sum type: một trong nhiều khả năng

Một result có thể là `Success(value)` **hoặc** `Failure(error)`. Đây là **sum type (합 타입)**. Rust `enum`, Haskell algebraic data type, Kotlin sealed hierarchy và Java sealed types + pattern matching đều biểu diễn ý tưởng tương tự ở mức khác nhau.

Sum type mạnh hơn việc dùng `null` hoặc magic integer vì alternatives được đưa vào type. Compiler có thể kiểm tra exhaustiveness: nếu domain có ba case mà code chỉ xử lý hai, thiếu case trở thành lỗi có thể phát hiện sớm.

## Modeling state để loại bỏ invalid state

Giả sử payment có `status`, `paidAt`, `failureReason`. Một model phẳng cho phép trạng thái vô nghĩa như `status=SUCCESS` nhưng `paidAt=null` và `failureReason` lại có giá trị.

Một sum type có thể tách thành `Pending`, `Succeeded(paidAt)`, `Failed(reason)`. Khi representation phản ánh invariant, nhiều validation chuyển từ runtime convention thành compile-time structure.

Đây là nguyên tắc **make invalid states unrepresentable**.

## Generic type và variance

Giả sử `Cat` là subtype của `Animal`. Câu hỏi khó hơn là `List<Cat>` có phải subtype của `List<Animal>` không. Câu trả lời phụ thuộc operation mà container cho phép.

Nếu một `List<Cat>` được xem như mutable `List<Animal>`, caller có thể thêm `Dog`; invariant của list bị phá. Vì vậy mutable generic thường phải **invariant**.

Nếu abstraction chỉ produce `T`, covariance thường an toàn: nơi cần producer của `Animal` có thể dùng producer của `Cat`. Nếu abstraction chỉ consume `T`, contravariance có thể phù hợp: consumer xử lý mọi `Animal` cũng xử lý được `Cat`.

Java wildcard `? extends T` / `? super T`, Kotlin `out` / `in`, C# `out` / `in` là các cách language biểu đạt quan hệ này.

## PECS là hệ quả, không phải câu thần chú

Trong Java, “Producer Extends, Consumer Super” hữu ích nhưng nên hiểu từ capability. `List<? extends Animal>` cho phép đọc value như `Animal` nhưng không cho thêm arbitrary `Animal`, vì actual list có thể là `List<Cat>`. `List<? super Cat>` cho phép thêm `Cat`, nhưng khi đọc chỉ biết chắc value là `Object`.

Compiler không gây khó dễ; nó đang bảo vệ information bị mất khi type bị existentially abstracted.

## Type inference là constraint solving

Khi viết generic function mà không chỉ rõ type parameter, compiler thu thập constraints từ argument, expected return type và language rules rồi tìm substitution phù hợp.

Ví dụ conceptual:

```text
identity(x: T) -> T
name = identity("Alice")
```

Argument tạo constraint `T = String`. Với generic phức tạp, compiler phải giải subtype constraints, variance và overload resolution. Vì vậy đôi lúc một biểu thức “rõ ràng với người” vẫn cần explicit type annotation để giảm ambiguity.

## Local inference và global inference

Một số language cố suy luận phần lớn type toàn chương trình; Java/Kotlin/C# chủ yếu dùng inference cục bộ quanh expression/generic call. Local inference giữ API type contract explicit hơn và giúp compiler/tooling scale tốt, đổi lại programmer phải viết type ở boundary nhiều hơn.

Không có lựa chọn tuyệt đối tốt: đây là trade-off giữa annotation burden, error message, compile-time complexity và readability.

## Higher-kinded abstraction: type constructor như parameter

`List<T>` không phải một concrete type cho tới khi `T` được cung cấp; có thể xem `List` như type constructor. Higher-kinded types cho phép abstraction trên chính các constructor dạng `F<T>` thay vì chỉ trên `T`.

Điều này hữu ích khi muốn diễn đạt pattern chung giữa `List`, `Option`, `Future`... nhưng cũng tăng độ phức tạp của type system. Một số language hỗ trợ trực tiếp, một số dùng interface/generic encoding thay thế.

## API design consequence

Type càng precise, compiler càng có nhiều information để giúp caller. Nhưng type quá phức tạp có thể làm error message và onboarding tệ. Senior design không phải tối đa hóa type cleverness mà chọn boundary nơi compile-time guarantee đáng giá hơn complexity.

## Mental model

> Product type mô tả “A và B”; sum type mô tả “A hoặc B”; variance mô tả subtype relation biến đổi thế nào khi đi qua generic constructor; inference là quá trình giải constraints. Khi dùng chúng đúng, type system trở thành công cụ modeling domain chứ không chỉ bộ kiểm tra syntax.