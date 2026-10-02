# Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Algebraic data types, variance và type inference**. Route đi từ product/sum types → pattern matching và exhaustiveness → variance/subtyping → constraint solving/inference, để cấu trúc dữ liệu và tính đúng của type checker đi cùng nhau.

Hệ kiểu (type system / 타입 시스템) không chỉ gắn nhãn `int`, `String` hay `User`. Ở mức advanced, kiểu (type / 타입) trở thành một ngôn ngữ mô tả **shape của trạng thái (state / 상태) hợp lệ**, cách các shape kết hợp và quan hệ substitutability giữa chúng. Algebraic dữ liệu (data / 데이터) Types, variance và suy luận (inference / 추론) là ba mảnh giúp xây API vừa biểu đạt mạnh vừa giảm invalid states.

## Sản phẩm (product / 제품) kiểu (type / 타입): nhiều phần cùng tồn tại

Một bản ghi (record / 레코드)/đối tượng (object / 객체) đơn giản có thể được nhìn như sản phẩm (product / 제품) kiểu (type / 타입):

```text
User = Name × Email × Age
```

Một giá trị (value / 값) `User` chứa đồng thời một giá trị (value / 값) của mỗi thành phần (component / 컴포넌트). Nếu `Name` có `a` khả năng và `Age` có `b` khả năng hữu hạn, sản phẩm (product / 제품) có khoảng `a*b` combinations.

Struct, tuple, bản ghi (record / 레코드) và lớp (class / 클래스) data-holder thường mang intuition này.

> **Chuyển mạch:** Trong **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Sản phẩm (product / 제품) kiểu (type / 타입): nhiều phần cùng tồn tại** cho ta quy tắc; **Sum kiểu (type / 타입): một trong nhiều trường hợp (case / 사례)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Invalid trạng thái (state / 상태) explosion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sum kiểu (type / 타입): một trong nhiều trường hợp (case / 사례)

Sum kiểu (type / 타입) biểu diễn giá trị (value / 값) thuộc **một trong các alternatives**:

```text
PaymentResult = Success(Receipt)
              | Declined(Reason)
              | Retryable(Error)
```

Thay vì đối tượng (object / 객체) có nhiều nullable fields và flag khó đồng bộ, sum kiểu (type / 타입) encode trực tiếp máy trạng thái (state machine / 상태 머신) hợp lệ.

Trong Rust có `enum`, Kotlin có sealed hierarchy, TypeScript có discriminated union, functional languages có ADT bản địa (native / 네이티브). Java sealed types + records giúp gần hơn mô hình này.

> **Chuyển mạch:** Ở chặng này của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Sum kiểu (type / 타입): một trong nhiều trường hợp (case / 사례)** cho ta quy tắc; **Invalid trạng thái (state / 상태) explosion** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mẫu (pattern / 패턴) matching và exhaustiveness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Invalid trạng thái (state / 상태) explosion

Giả sử API dùng:

```text
status: string
receipt: Receipt?
error: Error?
```

Ta có thể tạo trạng thái vô nghĩa như `status=SUCCESS` nhưng `receipt=null`, hoặc vừa có receipt vừa lỗi (error / 오류).

ADT chuyển nhiều quy tắc (rule / 규칙) thời gian chạy (runtime / 런타임) thành quy tắc (rule / 규칙) construction/kiểu (type / 타입) checking. Đây là ví dụ principle: **make invalid states unrepresentable** khi chi phí phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Mẫu (pattern / 패턴) matching và exhaustiveness** tiếp nhận điểm tựa từ **Invalid trạng thái (state / 상태) explosion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parametric polymorphism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) matching và exhaustiveness

Nếu sum kiểu (type / 타입) có tập cases đóng, trình biên dịch (compiler / 컴파일러) có thể kiểm tra mẫu (pattern / 패턴) matching đã xử lý đủ trường hợp (case / 사례) chưa.

Khi thêm trường hợp (case / 사례) mới, compile lỗi (error / 오류) ở các match site trở thành một dạng impact phân tích (analysis / 분석) tự động.

Điều này mạnh hơn chuỗi `if(status == "...")` phân tán vì relationship giữa variants và consumers được hệ kiểu (type system / 타입 시스템) theo dõi.

> **Chuyển mạch:** Trong **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Parametric polymorphism** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) matching và exhaustiveness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parametric polymorphism

Generic kiểu (type / 타입) như `List<T>` cho phép viết thuật toán (algorithm / 알고리즘) độc lập kiểu (type / 타입) cụ thể. Nhưng câu hỏi khó xuất hiện khi có subtype quan hệ (relation / 관계).

Nếu `Dog <: Animal`, liệu `List<Dog> <: List<Animal>`? Không tự động. Nếu cho phép và `List<Animal>` có phương thức (method / 메서드) add, ta có thể add `Cat` vào danh sách (list / 목록) thực chất là `List<Dog>`, phá kiểu (type / 타입) an toàn (safety / 안전).

> **Chuyển mạch:** Ở chặng này của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Variance** tiếp nhận điểm tựa từ **Parametric polymorphism** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java/Kotlin examples** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variance

**Covariance** cho phép quan hệ đi cùng chiều: `Producer<Dog>` có thể dùng nơi cần `Producer<Animal>` nếu giao diện (interface / 인터페이스) chỉ produce `T`.

**Contravariance** đi ngược chiều: bên tiêu thụ (consumer / 소비자) có thể nhận broader kiểu (type / 타입). Một `Consumer<Animal>` dùng được nơi cần bên tiêu thụ (consumer / 소비자) của `Dog` vì nó biết xử lý mọi Animal.

**Invariance** không cho subtype quan hệ (relation / 관계) giữa parameterized types.

Mô hình tư duy (mental model / 사고 모델) hữu ích:

```text
output position  -> covariance thường hợp lý
input position   -> contravariance thường hợp lý
both directions  -> invariance thường cần thiết
```

Đây là intuition, không thay formal rules của từng ngôn ngữ (language / 언어).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Variance** cho ta quy tắc; **Java/Kotlin examples** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Kiểu (type / 타입) suy luận (inference / 추론) là ràng buộc (constraint / 제약조건) solving** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java/Kotlin examples

Java dùng wildcard-site variance như `? extends T` và `? super T`.

PECS mnemonic — Producer Extends, bên tiêu thụ (consumer / 소비자) Super — hữu ích nhưng nên hiểu qua direction dữ liệu chứ không học thuộc khẩu hiệu.

Kotlin hỗ trợ declaration-site variance `out`/`in`, giúp đặc tả hợp đồng (contract / 계약) variance nằm ở kiểu (type / 타입) declaration khi phù hợp.

> **Chuyển mạch:** Trong **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Java/Kotlin examples** cho ta quy tắc; **Kiểu (type / 타입) suy luận (inference / 추론) là ràng buộc (constraint / 제약조건) solving** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cục bộ (local / 로컬) suy luận (inference / 추론) vs toàn cục (global / 전역) suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiểu (type / 타입) suy luận (inference / 추론) là ràng buộc (constraint / 제약조건) solving

Khi trình biên dịch (compiler / 컴파일러) suy ra kiểu (type / 타입), nó không “đoán” bằng AI. Nó thu thập các ràng buộc (constraints / 제약조건들) từ literals, hàm (function / 함수) applications, assignments và generic parameters rồi tìm substitution thỏa rules.

Ví dụ conceptual:

```text
identity(x) = x
```

Nếu không có thao tác (operation / 연산) nào yêu cầu kiểu (type / 타입) cụ thể, trình biên dịch (compiler / 컴파일러) có thể suy ra polymorphic form tương tự `T -> T` trong hệ thống phù hợp.

Kiểu (type / 타입) suy luận (inference / 추론) phức tạp hơn khi có subtyping, overload, higher-rank polymorphism hoặc effects. ngôn ngữ (language / 언어) thường giới hạn suy luận (inference / 추론) để compile thời gian (time / 시간)/diagnostics còn kiểm soát được.

> **Chuyển mạch:** Ở chặng này của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Cục bộ (local / 로컬) suy luận (inference / 추론) vs toàn cục (global / 전역) suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Kiểu (type / 타입) suy luận (inference / 추론) là ràng buộc (constraint / 제약조건) solving** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Higher-kinded lớp trừu tượng (abstraction / 추상화) intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cục bộ (local / 로컬) suy luận (inference / 추론) vs toàn cục (global / 전역) suy luận (inference / 추론)

Một số ngôn ngữ (language / 언어) suy kiểu (type / 타입) mạnh trong hàm (function / 함수) body nhưng yêu cầu API công khai (public API / 공개 API) annotation. Đây là thiết kế (design / 설계) sự đánh đổi (trade-off / 트레이드오프) tốt cho maintainability: hiện thực (implementation / 구현) có ergonomics, ranh giới (boundary / 경계) vẫn tường minh (explicit / 명시적).

Nếu suy luận (inference / 추론) lan quá xa, lỗi (error / 오류) message có thể xuất hiện cách xa nguyên nhân và refactor thay kiểu (type / 타입) ngoài ý muốn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Higher-kinded lớp trừu tượng (abstraction / 추상화) intuition** tiếp nhận điểm tựa từ **Cục bộ (local / 로컬) suy luận (inference / 추론) vs toàn cục (global / 전역) suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Higher-kinded lớp trừu tượng (abstraction / 추상화) intuition

Kiểu (type / 타입) parameter thường đại diện một concrete kiểu (type / 타입) `T`. Higher-kinded lớp trừu tượng (abstraction / 추상화) cho phép parameter hóa trên **kiểu (type / 타입) constructor** như `F<_>` — ví dụ “một ngữ cảnh (context / 맥락)/bộ chứa (container / 컨테이너) bất kỳ”.

Nó hữu ích để biểu đạt patterns như ánh xạ (mapping / 매핑)/traversal chung, nhưng tăng độ phức tạp (complexity / 복잡도) hệ kiểu (type system / 타입 시스템) đáng kể. Java không có higher-kinded types trực tiếp; ecosystems mô phỏng bằng giao diện (interface / 인터페이스) patterns với ergonomic chi phí (cost / 비용).

> **Chuyển mạch:** Trong **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Higher-kinded lớp trừu tượng (abstraction / 추상화) intuition** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> sản phẩm (product / 제품) kiểu (type / 타입) mô tả “A và B”; sum kiểu (type / 타입) mô tả “A hoặc B”; generics mô tả cấu trúc (structure / 구조) độc lập element kiểu (type / 타입); variance kiểm soát direction substitutability; suy luận (inference / 추론) giải các ràng buộc (constraints / 제약조건들) để giảm annotation mà vẫn giữ static guarantees.

> **Chuyển mạch:** Ở chặng này của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Generic collection của subtype luôn là subtype collection.”** Mutable collection làm điều này unsafe nếu vừa đọc vừa ghi.

**“kiểu (type / 타입) suy luận (inference / 추론) nghĩa trình biên dịch (compiler / 컴파일러) biết nghiệp vụ (business / 비즈니스) meaning.”** Nó chỉ giải các ràng buộc (constraints / 제약조건들) trong kiểu (type / 타입) rules.

**“ADT chỉ dành cho functional programming.”** Sealed classes, enums có payload và discriminated unions mang cùng mô hình tư duy (mental model / 사고 모델) trong OOP/TypeScript ecosystems.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Algebraic dữ liệu (data / 데이터) types, variance và kiểu (type / 타입) suy luận (inference / 추론)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Chapter tiếp theo về quyền sở hữu (ownership / 소유권) cho thấy hệ kiểu (type system / 타입 시스템) còn có thể encode tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명). Với Java backend, variance xuất hiện trực tiếp trong generic APIs; với TypeScript/React, discriminated unions rất hữu ích cho UI/yêu cầu (request / 요청) trạng thái (state / 상태) machines.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
