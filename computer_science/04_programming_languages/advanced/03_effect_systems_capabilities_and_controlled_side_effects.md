# Effect systems, capabilities và controlled side effects

Type system thường trả lời một expression tạo ra loại value nào. Nhưng hai functions cùng trả `String` có thể rất khác: một function thuần chỉ format dữ liệu; function khác đọc network, ghi database hoặc throw exception. **Effect system** mở rộng static reasoning để mô tả computation có thể làm gì ngoài việc trả value.

## Side effect là thay đổi observable context

I/O, mutation, exception, async suspension và nondeterminism đều có thể được xem là effects. Side effect không xấu; phần lớn chương trình hữu ích cần chúng. Vấn đề là effect ẩn làm local reasoning khó hơn.

Nếu function signature cho thấy effect, caller có thể biết dependency và failure modes mà không đọc toàn implementation.

## Pure core và effectful shell

Functional design thường cố giữ business transformation thuần rồi đẩy I/O ra boundary. Điều này không phải để “loại bỏ effect” mà để cô lập chúng.

Một pricing function nhận input và trả result dễ test hơn function tự đọc clock, database và environment. Các dependency effectful có thể được truyền vào rõ ràng.

## Exceptions như effect

Checked exceptions trong Java là một dạng effect annotation hạn chế: signature nói method có thể fail theo một số kiểu. Chúng không phải full effect system, nhưng cho thấy ý tưởng rằng control-flow behavior có thể trở thành part of contract.

Unchecked exceptions linh hoạt hơn nhưng effect trở nên implicit. Trade-off là verbosity và composability so với explicitness.

## Async và suspension

Kotlin `suspend` đánh dấu function có thể suspend mà không block thread. Đây cũng là một effect-like distinction: caller phải chạy trong coroutine context phù hợp.

Structured concurrency tiếp tục idea này bằng cách đưa lifetime/cancellation relationship vào structure thay vì để tasks sống tự do.

## Capability-based design

**Capability** là reference/token trao quyền thực hiện action. Thay vì code có ambient authority truy cập filesystem/network toàn cục, component chỉ nhận capability nó cần.

Điều này kết nối type/design với security principle of least privilege. Nếu function không nhận database capability, ta có bằng chứng cấu trúc rằng nó không thể trực tiếp gọi database qua path bình thường.

## Algebraic effects

Algebraic effects tách việc “yêu cầu một effect” khỏi “handler thực thi effect”. Computation có thể phát operation như `ReadConfig` hoặc `Log`, còn handler quyết định implementation.

Mental model gần dependency injection nhưng được đưa vào semantics của language/runtime và có thể compose control effects mạnh hơn.

## Effect polymorphism

Nếu abstraction chỉ dùng effect của callback được truyền vào, ta muốn signature không hard-code mọi effect. Effect polymorphism cho phép generic code preserve/propagate effect set tương tự type polymorphism preserve types.

Đây là nơi design trở nên phức tạp: hệ thống càng biểu đạt chính xác, inference và error messages càng khó.

## Production connection

Effect visibility giúp review architecture. Một domain module thuần dễ cache, replay và property-test. Một function có network/database/time effects cần timeout, retry/idempotency và observability.

Do đó effect không chỉ là PL theory; nó là cách nối static contract với operational behavior.

## Mental Model

> Type nói “giá trị gì có thể đi ra”; effect nói “trong lúc tạo giá trị đó computation có thể tác động gì lên thế giới”. Thiết kế tốt làm authority và effects đủ rõ để người đọc reasoning mà không phải giả định hidden behavior.