# Tác động (effect / 효과) các hệ thống (systems / 시스템들), capabilities và controlled side effects

> **Mạch đọc:** Đặt **tác động (effect / 효과) các hệ thống (systems / 시스템들), capabilities và controlled side effects** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Side tác động (effect / 효과) là thay đổi observable ngữ cảnh (context / 맥락)** sang **Pure cốt lõi (core / 핵심) và effectful shell**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hệ kiểu (type system / 타입 시스템) thường trả lời một expression tạo ra loại giá trị (value / 값) nào. Nhưng hai functions cùng trả `String` có thể rất khác: một hàm (function / 함수) thuần chỉ format dữ liệu; hàm (function / 함수) khác đọc mạng (network / 네트워크), ghi cơ sở dữ liệu (database / 데이터베이스) hoặc throw exception. **tác động (effect / 효과) hệ thống (system / 시스템)** mở rộng static lập luận (reasoning / 추론) để mô tả computation có thể làm gì ngoài việc trả giá trị (value / 값).

## Side tác động (effect / 효과) là thay đổi observable ngữ cảnh (context / 맥락)

I/O, mutation, exception, async suspension và nondeterminism đều có thể được xem là effects. Side tác động (effect / 효과) không xấu; phần lớn chương trình hữu ích cần chúng. Vấn đề là tác động (effect / 효과) ẩn làm cục bộ (local / 로컬) lập luận (reasoning / 추론) khó hơn.

Nếu hàm (function / 함수) signature cho thấy tác động (effect / 효과), caller có thể biết phụ thuộc (dependency / 의존성) và thất bại (failure / 실패) modes mà không đọc toàn hiện thực (implementation / 구현).


> **Chuyển mạch:** Từ **Side tác động (effect / 효과) là thay đổi observable ngữ cảnh (context / 맥락)**, ta sang **Pure cốt lõi (core / 핵심) và effectful shell** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Pure cốt lõi (core / 핵심) và effectful shell

Functional thiết kế (design / 설계) thường cố giữ nghiệp vụ (business / 비즈니스) transformation thuần rồi đẩy I/O ra ranh giới (boundary / 경계). Điều này không phải để “loại bỏ tác động (effect / 효과)” mà để cô lập chúng.

Một pricing hàm (function / 함수) nhận đầu vào (input / 입력) và trả kết quả (result / 결과) dễ kiểm thử (test / 테스트) hơn hàm (function / 함수) tự đọc clock, cơ sở dữ liệu (database / 데이터베이스) và môi trường (environment / 환경). Các phụ thuộc (dependency / 의존성) effectful có thể được truyền vào rõ ràng.


> **Chuyển mạch:** Từ **Pure cốt lõi (core / 핵심) và effectful shell**, ta sang **Exceptions như tác động (effect / 효과)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Exceptions như tác động (effect / 효과)

Checked exceptions trong Java là một dạng tác động (effect / 효과) annotation hạn chế: signature nói phương thức (method / 메서드) có thể thất bại (fail / 실패) theo một số kiểu. Chúng không phải full tác động (effect / 효과) hệ thống (system / 시스템), nhưng cho thấy ý tưởng rằng control-flow hành vi (behavior / 동작) có thể trở thành part of đặc tả hợp đồng (contract / 계약).

Unchecked exceptions linh hoạt hơn nhưng tác động (effect / 효과) trở nên implicit. sự đánh đổi (trade-off / 트레이드오프) là verbosity và composability so với explicitness.


> **Chuyển mạch:** Từ **Exceptions như tác động (effect / 효과)**, ta sang **Async và suspension** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Async và suspension

Kotlin `suspend` đánh dấu hàm (function / 함수) có thể suspend mà không khối (block / 블록) luồng thực thi (thread / 스레드). Đây cũng là một effect-like distinction: caller phải chạy trong coroutine ngữ cảnh (context / 맥락) phù hợp.

Structured tính đồng thời (concurrency / 동시성) tiếp tục idea này bằng cách đưa thời gian tồn tại (lifetime / 수명)/cancellation relationship vào cấu trúc (structure / 구조) thay vì để tasks sống tự do.


> **Chuyển mạch:** Từ **Async và suspension**, ta sang **Capability-based thiết kế (design / 설계)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Capability-based thiết kế (design / 설계)

**năng lực (capability / 역량)** là tham chiếu (reference / 참조)/đơn vị từ (token / 토큰) trao quyền thực hiện hành động (action / 동작). Thay vì mã (code / 코드) có ambient authority truy cập filesystem/mạng (network / 네트워크) toàn cục, thành phần (component / 컴포넌트) chỉ nhận năng lực (capability / 역량) nó cần.

Điều này kết nối kiểu (type / 타입)/thiết kế (design / 설계) với bảo mật (security / 보안) principle of least privilege. Nếu hàm (function / 함수) không nhận cơ sở dữ liệu (database / 데이터베이스) năng lực (capability / 역량), ta có bằng chứng cấu trúc rằng nó không thể trực tiếp gọi cơ sở dữ liệu (database / 데이터베이스) qua đường dẫn (path / 경로) bình thường.


> **Chuyển mạch:** Từ **Capability-based thiết kế (design / 설계)**, ta sang **Algebraic effects** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Algebraic effects

Algebraic effects tách việc “yêu cầu một tác động (effect / 효과)” khỏi “handler thực thi tác động (effect / 효과)”. Computation có thể phát thao tác (operation / 연산) như `ReadConfig` hoặc `Log`, còn handler quyết định hiện thực (implementation / 구현).

Mô hình tư duy (mental model / 사고 모델) gần phụ thuộc (dependency / 의존성) injection nhưng được đưa vào ngữ nghĩa (semantics / 의미론) của ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) và có thể compose điều khiển (control / 제어) effects mạnh hơn.


> **Chuyển mạch:** Từ **Algebraic effects**, ta sang **tác động (effect / 효과) polymorphism** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tác động (effect / 효과) polymorphism

Nếu lớp trừu tượng (abstraction / 추상화) chỉ dùng tác động (effect / 효과) của callback được truyền vào, ta muốn signature không hard-code mọi tác động (effect / 효과). tác động (effect / 효과) polymorphism cho phép generic mã (code / 코드) preserve/propagate tác động (effect / 효과) set tương tự kiểu (type / 타입) polymorphism preserve types.

Đây là nơi thiết kế (design / 설계) trở nên phức tạp: hệ thống càng biểu đạt chính xác, suy luận (inference / 추론) và lỗi (error / 오류) messages càng khó.


> **Chuyển mạch:** Từ **tác động (effect / 효과) polymorphism**, ta sang **môi trường vận hành (production / 운영 환경) liên kết (connection / 연결)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Môi trường vận hành (production / 운영 환경) liên kết (connection / 연결)

Tác động (effect / 효과) visibility giúp rà soát (review / 검토) kiến trúc (architecture / 아키텍처). Một lĩnh vực (domain / 도메인) mô-đun (module / 모듈) thuần dễ bộ nhớ đệm (cache / 캐시), replay và property-test. Một hàm (function / 함수) có mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스)/thời gian (time / 시간) effects cần hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도)/idempotency và khả năng quan sát (observability / 관측 가능성).

Do đó tác động (effect / 효과) không chỉ là PL lý thuyết (theory / 이론); nó là cách nối static đặc tả hợp đồng (contract / 계약) với operational hành vi (behavior / 동작).


> **Chuyển mạch:** Từ **môi trường vận hành (production / 운영 환경) liên kết (connection / 연결)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> kiểu (type / 타입) nói “giá trị gì có thể đi ra”; tác động (effect / 효과) nói “trong lúc tạo giá trị đó computation có thể tác động gì lên thế giới”. Thiết kế tốt làm authority và effects đủ rõ để người đọc lập luận (reasoning / 추론) mà không phải giả định hidden hành vi (behavior / 동작).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 type systems effects and runtime contracts](./00_type_systems_effects_and_runtime_contracts.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
