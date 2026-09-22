# Test architecture: contract, mutation, property-based và production verification

Test suite tốt không phải suite có nhiều test nhất. Nó là một **hệ thống bằng chứng** giúp team phát hiện regression với feedback đủ nhanh và confidence phù hợp risk. Khi software lớn lên, test architecture cần phân bổ evidence theo boundary: logic cục bộ, protocol giữa components, concurrency/timing, failure behavior và assumptions chỉ xuất hiện dưới production workload.

Điểm cốt lõi là test không chứng minh “system đúng trong mọi trường hợp”. Test lấy mẫu execution space. Vì vậy thiết kế test tốt bắt đầu từ **invariant, failure model và oracle** chứ không bắt đầu từ số lượng test case.

## 1. Test case chỉ có giá trị khi có oracle đủ mạnh

Một test gồm input/action và cách quyết định kết quả có đúng hay không. Phần quyết định đó là **oracle kiểm thử (test oracle / 테스트 오라클)**.

Oracle có thể đơn giản như `expected == actual`, nhưng ở hệ thống phức tạp nó có thể là invariant:

```text
balance không âm
committed transaction survive crash model đã hứa
consumer xử lý duplicate mà không tạo side effect thứ hai
schema mới vẫn đọc được message cũ
principal không truy cập resource ngoài policy
```

Nếu oracle yếu, test có thể chạy đúng path nhưng không phát hiện bug. Đây là lý do code coverage cao không tự tạo confidence cao.

## 2. Unit test và implementation coupling

Unit test nhanh và local nhưng dễ brittle nếu assert private implementation details. Test nên ưu tiên observable behavior/invariant thay vì mirror từng method call nội bộ.

Mock mọi dependency có thể tạo “green tests” cho một thế giới giả mà production components không thực sự tương thích.

Mock hữu ích khi cần kiểm soát rare error hoặc tách pure logic khỏi expensive dependency. Nhưng nếu test bắt đầu mô phỏng protocol, transaction hoặc network behavior bằng hàng chục expectations thủ công, fake world có thể khác production world nhiều hơn team tưởng.

## 3. Contract testing kiểm tra agreement tại boundary

Service/API integration thường hỏng ở assumptions về request/response/schema. **Kiểm thử hợp đồng (contract testing / 계약 테스트)** kiểm tra provider/consumer có cùng hiểu interface mà không cần dựng toàn system mỗi lần.

Consumer-driven contract hữu ích khi provider cần biết behavior nào consumers thật sự phụ thuộc. Tuy nhiên contract test không thay end-to-end test cho network, auth, deployment, routing hoặc shared infrastructure.

Contract cũng không chỉ là JSON shape. Behavioral contract có thể gồm status semantics, idempotency, ordering, timeout expectation, pagination, error mapping và backward compatibility.

Nếu schema vẫn parse nhưng semantics đổi từ “missing means zero” thành “missing means unknown”, structural contract có thể xanh trong khi business contract đã vỡ.

## 4. Property-based testing biến requirement thành invariant tổng quát

Thay vì viết vài examples, **kiểm thử dựa trên thuộc tính (property-based testing / 속성 기반 테스트)** sinh nhiều inputs để kiểm tra invariant như round-trip encode/decode, sorting preserves multiset hoặc parser không crash với arbitrary valid input.

Giá trị lớn nhất là buộc ta phát biểu property tổng quát. Shrinking giúp rút failing case lớn về counterexample nhỏ dễ hiểu.

Ví dụ serializer có thể được kiểm tra bằng:

```text
decode(encode(x)) ≈ x
```

Dấu `≈` quan trọng: floating point, unordered maps hoặc canonicalization có thể làm exact byte equality không phải invariant đúng. Test tốt phải phát biểu semantic equivalence đúng với domain.

## 5. Metamorphic testing hữu ích khi không biết exact expected output

Có bài toán khó có oracle tuyệt đối cho từng input, ví dụ optimizer, search ranking hoặc numerical solver. Khi đó có thể kiểm tra **quan hệ biến hình (metamorphic relation)**.

Nếu scale toàn bộ đơn vị đo theo cùng factor, hoặc biến đổi input theo một symmetry mà problem giữ nguyên, output cần biến đổi theo relation dự kiến.

Metamorphic testing không thay domain oracle, nhưng giúp kiểm tra consistency khi expected answer quá đắt hoặc khó tính trước.

## 6. Mutation testing đo sức mạnh của assertion

Code coverage chỉ nói line đã chạy, không nói assertion có khả năng bắt lỗi. **Kiểm thử đột biến (mutation testing / 변이 테스트)** cố thay operator/condition nhỏ rồi xem tests có fail không.

Mutation sống sót có thể chỉ ra assertion yếu, unreachable behavior hoặc code không quan trọng. Cost chạy cao nên thường dùng có chọn lọc ở logic critical thay vì toàn monorepo mỗi commit.

Mutation score cũng không nên thành KPI tuyệt đối. Nếu team viết assertions vô nghĩa chỉ để “kill mutant”, metric bắt đầu bị Goodhart hóa thay vì tăng correctness evidence.

## 7. Integration test cần real semantics ở nơi mock nguy hiểm

Database, broker, filesystem, TLS và transaction semantics khó mock chính xác. Containerized/ephemeral dependencies giúp integration test gần production hơn nhưng tăng startup/flakiness cost.

Điểm chọn boundary dựa vào risk. Nếu bug nguy hiểm nhất là transaction isolation, cần test với database engine thật. Nếu bug nằm ở pure calculation, dựng cả cluster chỉ làm feedback chậm hơn.

Test pyramid vì vậy không nên được hiểu là luật hình học cố định; distribution phụ thuộc system boundaries, cost of failure và tốc độ feedback.

## 8. Concurrency testing không thể thay proof bằng “chạy nhiều lần”

Race condition phụ thuộc interleaving. Loop một test 10,000 lần có thể tăng xác suất lộ bug nhưng không chứng minh protocol đúng.

Test concurrency nên làm rõ invariant và chủ động tạo pressure lên scheduling boundary: barriers/latches để đồng bộ start, deterministic scheduler khi framework hỗ trợ, randomized scheduling, stress workload và sanitizer/race detector.

Nếu bug biến mất khi thêm logging/sleep, đó có thể là Heisenbug vì instrumentation đổi timing. `sleep(100)` không phải synchronization proof.

Correctness reasoning vẫn phải quay về happens-before/ownership. Xem [đường correctness CPU → language memory model](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

## 9. Failure injection kiểm tra contract khi lower layer không còn happy path

Nhiều production invariant chỉ có ý nghĩa khi component fail giữa chừng. **Tiêm lỗi (fault injection / 장애 주입)** chủ động tạo failure ở boundary để kiểm tra recovery behavior.

Ví dụ có thể ngắt network giữa request và response, kill process trước/sau WAL flush, làm dependency timeout, trả disk-full, làm replica lag hoặc làm certificate hết hạn trong environment kiểm soát.

Mỗi injection cần gắn với hypothesis:

```text
failure xảy ra ở đâu?
invariant nào vẫn phải giữ?
caller thấy outcome nào?
retry có an toàn không?
state nào cần recover?
evidence nào chứng minh recovery thành công?
```

Nếu test chỉ kiểm tra service “không crash” mà không kiểm tra state sau recovery, oracle vẫn quá yếu.

## 10. Crash consistency cần test interruption points, không chỉ restart

Durability bug thường nằm giữa hai persistent transitions. Test hữu ích cần inject crash tại các điểm khác nhau:

```text
trước log flush
sau log flush nhưng trước data flush
sau output file nhưng trước metadata publication
sau local persist nhưng trước replica acknowledgement
```

Sau restart phải kiểm tra committed state, uncommitted state, idempotent recovery và metadata consistency.

Đây là lý do database/filesystem testing cần state-machine reasoning thay vì chỉ “restart xong app lên được”. Đọc [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

## 11. Network fault không chỉ là disconnect

Distributed systems có asymmetric failure, delay, duplication, reordering và partition. Inject `connection refused` chỉ cover một phần nhỏ.

Client có thể gửi request thành công nhưng mất response; từ caller perspective outcome trở thành ambiguous. Retry chỉ an toàn nếu operation idempotent hoặc deduplication key đủ mạnh.

Latency injection cũng cần cẩn thận. Fixed 500 ms cho mọi request tạo workload khác production burst/tail distribution. Delay distribution, packet loss và partial dependency slowdown thường cho evidence thực tế hơn.

## 12. Chaos engineering là experiment trên invariant

**Kỹ nghệ hỗn loạn (chaos engineering / 카오스 엔지니어링)** thường bị hiểu thành tắt ngẫu nhiên server. Cách tiếp cận nghiêm túc hơn là controlled experiment:

```text
steady-state hypothesis
→ bounded fault
→ observe invariant/SLO
→ abort condition
→ recovery verification
```

Blast radius phải phù hợp maturity. Early-stage system nên bắt đầu ở local/staging hoặc production cohort nhỏ với guardrails. Không cần gây outage toàn fleet nếu cùng hypothesis có thể kiểm chứng ở phạm vi nhỏ.

Chaos test có giá trị khi nó tìm assumption ẩn: failover chậm hơn timeout budget, retry storm, certificate issuer là single point of failure, hoặc autoscaler không kịp phản ứng.

## 13. Security testing cần kiểm tra authorization decision

Security test thường dừng ở “login đúng/sai”. Nhưng production incident hay nằm ở object-level authorization, delegation, parser differential và credential lifecycle.

Một test suite tốt kiểm tra principal A không đọc resource B, stale/revoked credential bị reject, policy rollout không mở rộng privilege ngoài ý muốn và malformed request không được proxy/backend diễn giải khác nhau.

Fuzzing parser/protocol đặc biệt có giá trị với input untrusted. Tuy nhiên fuzz “không crash” vẫn chưa đủ nếu parser có thể accept semantically dangerous state.

Đọc [Security boundaries và attack chains](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md).

## 14. Differential testing dùng implementation khác làm evidence so sánh

Nếu có hai independent implementations của cùng spec, cùng input có thể được chạy qua cả hai để tìm divergence. Compiler, parser, database compatibility layer và crypto implementation thường dùng kiểu reasoning này.

Divergence không tự chứng minh bên nào sai; specification có thể cho phép nhiều outputs. Nhưng nó tạo counterexample để investigation.

Shadow traffic trong migration là một biến thể production của differential testing: old/new path nhận cùng logical request rồi semantic outputs được so sánh có chọn lọc.

## 15. Production verification kiểm tra assumptions chỉ production mới có

Một số property chỉ quan sát được với real traffic/data distribution. Canary metrics, synthetic probes, shadow comparison và runtime invariants bổ sung pre-production tests.

Testing không kết thúc khi deploy; deployment là một experiment có guardrails.

Production verification cần phân biệt release health, business correctness, performance regression, security policy regression và data/schema divergence. Một canary CPU ổn không chứng minh monetary calculation đúng.

## 16. Runtime invariant biến silent corruption thành observable failure

Có invariant quá đắt để chứng minh statically nhưng rẻ để kiểm tra runtime ở sample hoặc boundary quan trọng: sequence number không lùi, account balance nằm trong range hợp lệ, replicated state hash khớp, message version được hỗ trợ.

Runtime assertion có thể fail-fast trong internal system hoặc chỉ emit telemetry tùy blast radius. Cần tránh log sensitive data và tránh assertion quá nặng trở thành performance incident.

Ý tưởng cốt lõi là chuyển “hy vọng assumption đúng” thành observable evidence.

## 17. Flaky tests là reliability failure của chính test system

Flakiness phá trust. Retry test vô hạn che race/timing bug. Cần classify nguồn nondeterminism: clock, async wait, shared state, random seed, external dependency, port collision hoặc resource exhaustion.

Deterministic time/fake clock và explicit synchronization tốt hơn sleep cố định.

Nếu test randomize input/schedule, seed phải được lưu để reproduce. Nếu test phụ thuộc eventual consistency, poll theo condition + deadline thường đúng hơn sleep “đủ lâu”.

## 18. Test data phải giữ semantics mà không tạo privacy debt

Production snapshot có distribution thực nhưng có thể chứa personal data, secret hoặc identifiers. Copy thẳng production DB vào test làm tăng breach surface và retention complexity.

Synthetic/anonymized data hữu ích nhưng có thể mất skew/rare edge cases. Test-data strategy cần cân privacy với representativeness và ghi rõ distribution nào đã bị mất.

## 19. Performance test phải đo saturation và recovery

Load test tốt tăng load qua utilization knee, đo queue wait/service time và xem system phục hồi thế nào sau burst. Nếu chỉ báo “max 20k RPS”, ta chưa biết p99 SLO, retry amplification hay backlog drain time.

Workload mix, payload sizes, cache warm/cold, downstream condition và background tasks phải gần enough production để result có ý nghĩa.

Capacity chapter đi sâu hơn tại [Capacity planning và whole-system profiling](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

## 20. Test environment có thể pass vì failure domain khác production

Staging một node không tái hiện multi-zone failover. Local filesystem không đại diện remote managed storage. In-memory queue không đại diện broker delivery semantics. Fake clock không tái hiện cross-host clock skew.

Điều này không làm lower-level test vô dụng. Nó chỉ yêu cầu test architecture ghi rõ **assumption nào mỗi environment cover và không cover**.

Một useful matrix là:

```text
invariant
→ failure model
→ test level/environment
→ oracle/evidence
```

Nhờ vậy team biết gap nào cần production canary hoặc fault-injection environment thay vì vô thức tin một green CI suite.

## 21. Incident phải quay lại test architecture dưới dạng invariant

Sau incident, cách đơn giản là thêm test cho exact input gây lỗi. Cách tốt hơn là hỏi bug reveal invariant nào chưa được encode.

Outage do retry storm không chỉ cần test “endpoint X timeout”. Cần test retry budget/backoff/admission behavior khi dependency service rate giảm. Data loss do crash không chỉ cần replay exact sequence; cần crash-point tests quanh durability protocol.

Incident learning hiệu quả biến một production surprise thành **family of properties/failure tests**, giảm xác suất cùng mechanism xuất hiện ở hình thức khác.

## 22. Test metrics cũng chịu Goodhart's Law

Coverage %, test count, pass rate, mutation score và mean CI duration đều hữu ích nhưng trở nên nguy hiểm khi biến thành target độc lập.

100% coverage có thể đạt bằng assertions yếu. Zero flaky tests có thể đạt bằng xóa test khó. CI rất nhanh có thể vì bỏ integration checks quan trọng.

Metric nên là evidence hỗ trợ câu hỏi “risk nào đang được kiểm soát?”, không phải proxy thay correctness.

## 23. Worked example: payment timeout với ambiguous outcome

Giả sử client gửi payment request, server commit transaction nhưng response bị mất. Client timeout rồi retry.

Một happy-path E2E test không cover tình huống này. Test architecture cần inject failure sau commit trước response, rồi kiểm tra:

```text
retry cùng idempotency key
→ không tạo charge thứ hai
→ client nhận outcome consistent
→ audit trail reconstruct được attempts
```

Oracle không phải “HTTP 200”. Oracle là **một logical payment tạo tối đa một irreversible charge theo contract**.

Ví dụ này nối fault injection, idempotency, transaction durability và production tracing trong một invariant duy nhất.

## 24. Worked example: schema migration old/new coexist

Trong rolling deploy, old producer và new consumer có thể coexist. Test chỉ chạy new→new bỏ sót compatibility window.

Contract matrix nên cover supported pairs:

```text
old producer → old consumer
old producer → new consumer
new producer → old consumer   nếu rollout contract yêu cầu
new producer → new consumer
```

Sau khi old version retire, contract matrix có thể thu hẹp. Testing phải phản ánh deployment state machine, không giả định fleet upgrade atomically.

## 25. Production evidence và forensic usefulness

Khi test fail hoặc incident xảy ra, evidence nên đủ để reconstruct boundary state: request/trace ID, version/build, input class, principal/policy version, dependency outcome, retry attempt, transaction/event ID và relevant timing.

Không cần log toàn payload hoặc secret. **Khả năng điều tra (forensic usefulness / 포렌식 유용성)** đến từ causal identity và decision metadata, không phải lưu mọi byte.

Test harness cũng nên export artifacts hữu ích: minimized property counterexample, random seed, fault timeline, node/replica state và relevant logs/metrics. Một flaky CI failure không reproduce được là evidence rất yếu.

## Common Misconceptions

**“Nhiều test hơn nghĩa confidence cao hơn.”** Test trùng nhau với oracle yếu có thể tăng maintenance mà không tăng evidence đáng kể.

**“100% coverage nghĩa code đúng.”** Coverage chỉ nói code đã chạy dưới test, không chứng minh assertions đủ mạnh hay failure space đã được cover.

**“Chaos engineering là tắt server ngẫu nhiên.”** Nó phải là controlled experiment gắn với steady-state hypothesis, bounded blast radius và recovery oracle.

**“Mock càng nhiều thì unit test càng tốt.”** Mocking protocol semantics có thể tạo fake world khác production.

**“Retry flaky test là fix.”** Retry có thể che race, clock hoặc resource bug và làm test system mất trust.

## Mental Model

> Test architecture là **portfolio bằng chứng về invariant dưới nhiều execution và failure models**. Unit tests kiểm tra local logic; contracts kiểm tra boundary agreement; properties/mutation kiểm tra độ rộng và sức mạnh oracle; integration/fault injection kiểm tra semantics của dependency thật; production verification kiểm tra assumptions chỉ workload thật mới làm lộ. Một test suite mạnh biết risk nào được chứng minh ở đâu và gap nào vẫn còn.

## Kết nối

Đọc cùng [Deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md), [Large-scale migration](./03_large_scale_refactoring_strangler_and_branch_by_abstraction.md), [Security boundaries](../../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md), [Capacity/whole-system profiling](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [Correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md), [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).