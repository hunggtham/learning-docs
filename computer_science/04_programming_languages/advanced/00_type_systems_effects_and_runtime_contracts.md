# Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiểu (type / 타입) judgment như một statement có điều kiện** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Soundness và progress/preservation intuition** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Hệ kiểu (type system / 타입 시스템) không chỉ phân loại `int`, `string` hay `User`. Ở mức advanced, nó là một static lập luận (reasoning / 추론) khung phần mềm (framework / 프레임워크) dùng để loại bỏ một tập program states trước thời gian chạy (runtime / 런타임). Điều quan trọng là hiểu **thuộc tính (property / 속성) nào được encode**, thuộc tính (property / 속성) nào vẫn nằm ngoài hệ kiểu (type system / 타입 시스템), và chi phí (cost / 비용) ergonomics/expressiveness của mỗi lựa chọn.

## Kiểu (type / 타입) judgment như một statement có điều kiện

Notation dạng `Γ ⊢ e : T` có thể đọc: dưới môi trường (environment / 환경) `Γ`, expression `e` có kiểu (type / 타입) `T`. `Γ` chứa các giả định (assumptions / 가정들)/bindings về variables. kiểu (type / 타입) checker thực hiện các suy luận (inference / 추론) rules để xây derivation hoặc báo rằng derivation không tồn tại.

Cách nhìn này giúp tách cú pháp (syntax / 문법) khỏi ngữ nghĩa (semantics / 의미론): kiểu (type / 타입) checker không “đoán kiểu” tùy ý; nó thực hiện proof theo rules của ngôn ngữ (language / 언어).

> **Chuyển mạch:** Type judgment là statement có điều kiện; soundness nối static proof với runtime progress/preservation, còn subtyping/variance quy định khi một value hoặc function có thể được thay thế an toàn.

## Soundness và progress/preservation intuition

Một hệ kiểu (type system / 타입 시스템) thường muốn thuộc tính (property / 속성) gần với: well-typed program không rơi vào một lớp (class / 클래스) invalid thời gian chạy (runtime / 런타임) states. Formalization cổ điển dùng **progress** và **preservation**. Progress: well-typed expression hoặc đã là giá trị (value / 값) hoặc có bước evaluation tiếp. Preservation: một bước evaluation không phá kiểu (type / 타입) validity.

Điều này không có nghĩa program đúng lô-gic nghiệp vụ (business logic / 비즈니스 로직). kiểu (type / 타입) an toàn (safety / 안전) chỉ bảo vệ các invariants mà hệ kiểu (type system / 타입 시스템) encode.

> **Chuyển mạch:** Ở chặng này của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**, **Subtyping và variance** tiếp nhận điểm tựa từ **Soundness và progress/preservation intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ADT và invalid states** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Subtyping và variance

Nếu `Dog <: Animal`, điều đó không tự động suy ra `List<Dog> <: List<Animal>`. Nếu mutable danh sách (list / 목록) covariance được cho phép, caller có thể insert `Cat` vào danh sách (list / 목록) thực chất chỉ chứa Dog. Vì vậy variance phụ thuộc position đọc/ghi và ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약).

Covariance phù hợp producer/read-only; contravariance thường xuất hiện ở bên tiêu thụ (consumer / 소비자)/hàm (function / 함수) parameter; invariance là lựa chọn an toàn cho mutable containers phổ biến.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**, **ADT và invalid states** tiếp nhận điểm tựa từ **Subtyping và variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác động (effect / 효과) là phần ngữ nghĩa (semantics / 의미론) ngoài return kiểu (type / 타입)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ADT và invalid states

Algebraic dữ liệu (data / 데이터) Types cho phép mô hình (model / 모델) lĩnh vực (domain / 도메인) bằng sum/sản phẩm (product / 제품) types. Thay vì hai booleans `isLoading` và `hasError` tạo bốn combinations trong đó có trạng thái (state / 상태) vô nghĩa, ta có thể encode:

```text
State = Loading | Success(Data) | Failure(Error)
```

Mẫu (pattern / 패턴) matching exhaustiveness biến missing-case thành compile-time tín hiệu (signal / 신호). Đây là ví dụ “make invalid states unrepresentable”.

> **Chuyển mạch:** Trong **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**, **Tác động (effect / 효과) là phần ngữ nghĩa (semantics / 의미론) ngoài return kiểu (type / 타입)** tiếp nhận điểm tựa từ **ADT và invalid states** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gradual typing và trust ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác động (effect / 효과) là phần ngữ nghĩa (semantics / 의미론) ngoài return kiểu (type / 타입)

Hai functions cùng `User -> User` có thể rất khác nếu một hàm (function / 함수) đọc DB, ghi log, throw exception hoặc mutate toàn cục (global / 전역) trạng thái (state / 상태). tác động (effect / 효과) hệ thống (system / 시스템) cố đưa một phần side-effect thông tin (information / 정보) vào kiểu (type / 타입)/checking tầng (layer / 계층).

Có nhiều hình thức: checked exceptions, `async` effects, năng lực (capability / 역량) types, tác động (effect / 효과) rows, monadic encodings hoặc quyền sở hữu (ownership / 소유권)/borrow restrictions. Mục tiêu chung là làm hidden tương tác (interaction / 상호작용) trở nên tường minh (explicit / 명시적) để composition dễ lập luận (reasoning / 추론) hơn.

> **Chuyển mạch:** Ở chặng này của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**, **Tác động (effect / 효과) là phần ngữ nghĩa (semantics / 의미론) ngoài return kiểu (type / 타입)** đã nêu tiêu chí phân biệt, còn **Gradual typing và trust ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Thời gian chạy (runtime / 런타임) contracts vẫn cần tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gradual typing và trust ranh giới (boundary / 경계)

TypeScript, Python typing và nhiều ecosystem cho phép typed và untyped mã (code / 코드) cùng tồn tại. Static checker chỉ guarantee trong phạm vi các giả định (assumptions / 가정들) của nó. Khi dữ liệu (data / 데이터) đi từ JSON, cơ sở dữ liệu (database / 데이터베이스), mạng (network / 네트워크) hay động (dynamic / 동적) mô-đun (module / 모듈) vào typed lĩnh vực (domain / 도메인), thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) vẫn cần thiết.

Một `as User` cast không biến untrusted bytes thành người dùng (user / 사용자) đúng nghĩa; nó chỉ thay belief của trình biên dịch (compiler / 컴파일러). Đây là ranh giới (boundary / 경계) giữa **static claim** và **thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**, **Gradual typing và trust ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **Thời gian chạy (runtime / 런타임) contracts vẫn cần tồn tại** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thời gian chạy (runtime / 런타임) contracts vẫn cần tồn tại

Không phải thuộc tính (property / 속성) nào cũng phù hợp static types. phạm vi (range / 범위) phụ thuộc cấu hình (config / 설정), permission phụ thuộc session, uniqueness phụ thuộc cơ sở dữ liệu (database / 데이터베이스) trạng thái (state / 상태), độ trễ (latency / 지연 시간) phụ thuộc hệ thống (system / 시스템) tải (load / 로드). Assertions, schemas, DB các ràng buộc (constraints / 제약조건들), giao thức (protocol / 프로토콜) kiểm tra hợp lệ (validation / 검증) và tests bổ sung cho hệ kiểu (type system / 타입 시스템).

Thiết kế cấp cao (senior / 시니어) không hỏi “hệ kiểu (type system / 타입 시스템) hay thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) tốt hơn”; nó đặt bất biến (invariant / 불변식) ở tầng (layer / 계층) có đủ thông tin (information / 정보) để enforce.

> **Chuyển mạch:** Trong **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Thời gian chạy (runtime / 런타임) contracts vẫn cần tồn tại** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> hệ kiểu (type system / 타입 시스템) là một proof/ràng buộc (constraint / 제약조건) tầng (layer / 계층) trước thời gian chạy (runtime / 런타임); tác động (effect / 효과) hệ thống (system / 시스템) mở rộng proof đó sang tương tác (interaction / 상호작용); thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약) bảo vệ những facts chỉ biết khi chương trình đang chạy.

> **Chuyển mạch:** Ở chặng này của **Kiểu (type / 타입) các hệ thống (systems / 시스템들), effects và thời gian chạy (runtime / 런타임) contracts**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Xem [type foundation](../../basic/04_programming_languages/06_type_systems_generics_and_polymorphism.md), [errors/resources](../../basic/04_programming_languages/05_errors_resources_and_runtime_safety.md) và [API contracts](../../basic/08_software_systems/00_abstraction_modularity_interfaces_and_apis.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
