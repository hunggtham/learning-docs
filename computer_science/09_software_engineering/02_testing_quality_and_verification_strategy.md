# Testing, quality và verification strategy

Testing không thể chứng minh program không có bug chỉ bằng chạy vài cases. Nó là sampling/experimentation trên behavior space. Strategy tốt chọn test levels và verification techniques theo risk, contracts và failure modes.

## Quality không chỉ là không crash

Software quality gồm correctness, reliability, usability, security, performance, maintainability và compatibility. Một system chạy đúng output nhưng latency 30 giây vẫn có thể fail requirement.

Do đó test strategy phải derive từ quality attributes, không chỉ code coverage.

## Unit tests

Unit test cô lập một small unit theo behavior contract. Nó feedback nhanh và giúp localize regression.

Nhưng unit boundary không nhất thiết là một function/class. Nếu over-mock internal interactions, tests become coupled to implementation và refactoring khó.

Test behavior có giá trị hơn test call choreography trừ khi interaction chính là contract.

## Integration tests

Integration test xác minh boundaries thật: database queries, serialization, external API adapters, filesystem, message broker.

Nhiều bugs nằm ở mismatched assumptions giữa components nên chỉ unit tests không đủ.

Testcontainers/ephemeral environments giúp chạy dependency thật nhưng tăng runtime/operational cost.

## End-to-end tests

E2E đi qua user-relevant flow và bắt wiring/deployment issues. Nhưng chậm, flaky và khó debug hơn.

Test pyramid không phải luật cứng về số lượng; principle là nhiều tests nhanh ở dưới, ít tests đắt ở trên, tùy architecture/risk.

## Contract testing

Producer-consumer contract test xác minh API/message compatibility mà không cần full E2E environment. Nó đặc biệt hữu ích cho independently deployed services.

Schema compatibility không đủ nếu semantics đổi. `status: ACTIVE` có thể giữ type nhưng meaning thay đổi vẫn phá consumer.

## Property-based testing

Thay vì viết vài examples, property-based testing generate nhiều inputs và kiểm invariants như sorting output ordered + permutation input.

Nó phù hợp algorithms, parsers, serialization và data structures nơi invariants rõ.

## Fuzzing

Fuzzer tạo/mutate inputs để khám phá crashes, hangs hoặc sanitizer violations. Coverage-guided fuzzing dùng execution feedback để tìm paths mới.

Fuzzing rất mạnh cho parsers/protocols nhưng không tự biết business correctness nếu không có oracle/property.

## Mutation testing

Mutation testing cố tình đổi code nhỏ (đảo condition, thay operator) rồi xem tests có fail không. Nếu mutant sống, test suite có thể không nhạy với behavior đó.

Coverage đo code đã chạy; mutation score đo một phần khả năng tests phát hiện semantic changes.

## Static analysis và formal verification

Static analyzers tìm patterns/data-flow issues mà không execute program. Formal methods có thể prove properties theo model/specification nhưng cost cao và scope phải rõ.

Không technique nào thay tất cả techniques khác; chúng cover failure spaces khác nhau.

## Flaky tests

Flakiness thường do time, race, shared state, random seed, external service hoặc environment dependency. Retry flaky test che signal và làm pipeline unreliable.

Treat test reliability như production reliability: ownership, metrics và root-cause fixes.

## Testability như design property

Code có explicit dependencies, deterministic core logic và clear boundaries dễ test hơn. Nếu test phải boot toàn app cho một business rule, architecture có thể quá coupled.

Design for testability không có nghĩa expose internals; nó nghĩa contracts/dependencies observable và controllable hợp lý.

## Common Misconceptions

**“100% coverage = không bug.”** Coverage chỉ nói lines/branches được execute, không chứng minh assertions đủ.

**“Mock càng nhiều test càng unit.”** Over-mocking dễ test implementation chứ không behavior.

**“E2E gần user nhất nên quan trọng nhất.”** Nó quan trọng nhưng không scalable cho mọi case; cần portfolio tests.

## Mental Model

> Verification là xây nhiều lưới bắt lỗi ở các abstraction levels khác nhau. Không một lưới nào đủ; strategy theo risk quan trọng hơn metric đơn lẻ.

## Kết nối

Xem [testing/debugging foundations](../07_security_reliability/04_testing_verification_and_debugging.md), [requirements](./00_requirements_specification_and_engineering_process.md) và [delivery/operations](./03_delivery_configuration_and_operations.md).