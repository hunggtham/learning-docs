# Test architecture: contract, mutation, property-based và production verification

Test suite tốt không phải suite có nhiều test nhất. Nó là hệ thống bằng chứng giúp team phát hiện regression với feedback đủ nhanh và confidence phù hợp risk. Khi software lớn lên, test architecture cần phân bổ loại evidence theo boundary.

## Unit test và implementation coupling

Unit test nhanh và local nhưng dễ trở nên brittle nếu assert private implementation details. Test nên ưu tiên observable behavior/invariant thay vì mirror từng method call nội bộ.

Mock mọi dependency có thể tạo “green tests” cho một thế giới giả mà production components không thực sự tương thích.

## Contract testing

Service/API integration thường hỏng ở assumptions về request/response/schema. **Contract test** kiểm tra provider/consumer có cùng hiểu interface mà không cần dựng toàn system mỗi lần.

Consumer-driven contract hữu ích khi provider cần biết behavior nào consumers thật sự phụ thuộc. Tuy nhiên contract test không thay thế end-to-end test cho network, auth, deployment và shared infrastructure.

## Property-based testing

Thay vì viết vài examples, property-based testing sinh nhiều inputs để kiểm tra invariant như round-trip encode/decode, sorting preserves multiset hoặc parser không crash với arbitrary valid input.

Giá trị lớn nhất là buộc ta phát biểu property tổng quát. Shrinking giúp rút failing case lớn về counterexample nhỏ dễ hiểu.

## Mutation testing

Code coverage chỉ nói line đã chạy, không nói assertion có khả năng bắt lỗi. Mutation testing cố thay operator/condition nhỏ rồi xem tests có fail không.

Mutation sống sót có thể chỉ ra assertion yếu hoặc code không quan trọng. Cost chạy cao nên thường dùng có chọn lọc.

## Integration và ephemeral environment

Database, broker và filesystem semantics khó mock chính xác. Containerized/ephemeral dependencies giúp integration test gần production hơn nhưng tăng startup/flakiness cost.

Test pyramid không nên được hiểu là luật hình học cố định; distribution phụ thuộc system boundaries và cost of failure.

## Production verification

Một số property chỉ quan sát được với real traffic/data distribution. Canary metrics, synthetic probes, shadow comparison và runtime invariants bổ sung pre-production tests.

Testing không kết thúc khi deploy; deployment là một experiment có guardrails.

## Flaky tests

Flakiness phá trust. Retry test vô hạn che race/timing bug. Cần classify nguồn nondeterminism: clock, async wait, shared state, random seed, external dependency.

Deterministic time/fake clock và explicit synchronization tốt hơn sleep cố định.

## Mental Model

> Test architecture là portfolio bằng chứng. Unit tests cho local logic, contracts cho boundary, properties cho invariant rộng, mutation đo sức mạnh assertions, production verification kiểm tra assumptions chỉ xuất hiện ngoài đời. Không một tầng nào đủ một mình.