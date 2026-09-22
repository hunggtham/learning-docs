# Randomness, entropy sources và computational unpredictability

Hệ thống cần randomness cho session token, cryptographic key, nonce, randomized algorithm, sampling, load balancing, simulation và testing. Nhưng từ “random” thường che giấu nhiều contract khác nhau.

Một sequence có thể vượt qua statistical tests nhưng vẫn hoàn toàn predictable nếu attacker biết seed. Một hardware source có physical noise nhưng biased. Một CSPRNG có output rất tốt nhưng nếu state bị clone qua VM snapshot, hai máy có thể sinh cùng stream. Một UUID có vẻ ngẫu nhiên nhưng không nhất thiết có security entropy đủ cho secret.

Mental model:

```text
physical / environmental uncertainty
→ entropy estimation
→ conditioning / extraction
→ seed
→ deterministic generator state
→ random bytes
→ protocol-specific use
```

Chapter này phân biệt **entropy source**, **PRNG**, **CSPRNG**, **statistical randomness** và **computational unpredictability**, rồi nối chúng với failure modes production.

## 1. Deterministic computation không tự tạo entropy

Nếu program hoàn toàn deterministic và input/state ban đầu đã biết, output cũng đã được xác định.

```text
state_0 + deterministic algorithm
→ state_1
→ output_1
→ state_2
→ output_2
```

Ta có thể kéo dài 256 bit seed thành hàng terabyte pseudorandom output, nhưng không tạo thêm 1 TB uncertainty độc lập. Entropy của toàn stream bị giới hạn bởi uncertainty thực của seed/state theo threat model.

Đây là distinction nền tảng:

```text
expansion of bits
≠ creation of entropy
```

PRNG mở rộng một seed ngắn thành stream dài có statistical properties tốt. Entropy source mới là nơi uncertainty đi vào system.

## 2. Entropy source là nguồn uncertainty, không phải API tên random

Entropy có thể đến từ physical noise, timing jitter, device events hoặc hardware mechanism tùy platform. Nhưng raw source thường không lý tưởng: có bias, correlation, health failure và dependency vào environment.

Một entropy subsystem phải reasoning ít nhất:

```text
source behavior
→ amount of unpredictable variation
→ health/conditioning
→ accumulation
→ seed readiness
```

Không nên chỉ hỏi “đã gọi `/dev/random` hay API SecureRandom chưa?”. Cần hiểu runtime/OS đó seed generator như thế nào và lifecycle state ra sao.

## 3. Shannon entropy và min-entropy phục vụ câu hỏi khác nhau

Shannon entropy đo uncertainty trung bình. Security thường quan tâm attacker đoán outcome tốt nhất tới đâu.

**Min-entropy** dùng probability lớn nhất:

```text
H_min(X) = -log2(max_x P(X=x))
```

Nếu một source có nhiều outcome nhưng một outcome xảy ra 50%, attacker đã có guess rất mạnh dù average uncertainty nhìn có vẻ không quá thấp.

Vì vậy security entropy estimation thường conservative hơn việc nhìn histogram “khá đều”.

## 4. Conditioning và extractor

Raw physical source có thể biased/correlated. Một **conditioner/extractor** cố biến input có đủ entropy thành output gần uniform hơn.

Nhưng extractor không tạo entropy từ không khí. Nếu input thực tế có gần zero uncertainty, hash nó không biến output thành secret.

```text
predictable input
→ hash
→ deterministic digest
```

Digest có thể trông uniform nhưng attacker biết input vẫn tính được digest.

Đây là lỗi tư duy phổ biến: **appearance of randomness** không đồng nghĩa **unpredictability**.

## 5. PRNG và CSPRNG

PRNG thông thường tối ưu speed/statistical quality cho simulation hoặc randomized algorithm. Nếu attacker quan sát đủ output, state có thể bị suy ra tùy algorithm.

**Cryptographically Secure PRNG (CSPRNG)** cần contract mạnh hơn: với attacker computationally bounded, output tiếp theo phải khó dự đoán từ output đã thấy nếu state/seed chưa bị compromise.

CSPRNG thường dùng cryptographic primitive để update state và generate bytes. Ta reasoning bằng state transition, không bằng tên API:

```text
secret state S_i
→ generate output O_i
→ evolve state to S_(i+1)
```

Security phụ thuộc seed quality, state secrecy, update design và lifecycle.

## 6. Forward security và backtracking resistance

Nếu attacker compromise generator state tại thời điểm `t`, hai câu hỏi xuất hiện:

```text
Có reconstruct được output cũ không?
Có dự đoán được output tương lai không?
```

Một design tốt có thể cố cung cấp **backtracking resistance**: state hiện tại không đủ để recover output quá khứ đã xóa khỏi state.

Nếu generator sau đó nhận entropy mới và reseed, nó có thể lấy lại unpredictability cho tương lai. Đây thường được gọi theo các khái niệm như prediction resistance/recovery tùy construction.

Không có generator nào cứu được protocol nếu attacker đọc trực tiếp random bytes ngay khi application sử dụng chúng.

## 7. Seed lifecycle quan trọng hơn độ dài output

Một generator có output 4096-bit không mạnh nếu seed chỉ có 20 bit uncertainty. Attacker có thể brute-force seed space rồi regenerate toàn stream.

Security reasoning phải đi ngược:

```text
secret/token
← generator output
← generator state
← seed
← entropy sources
```

Đây là **entropy provenance**. Khi incident xảy ra, cần biết secret được sinh ở đâu, khi nào, trên machine state nào và generator đã seed/reseed chưa.

## 8. Boot-time entropy và early-start failure

Ngay sau boot, VM/container/embedded device có thể chưa thu đủ environmental entropy. Nếu service tạo host key, TLS key hoặc session secret quá sớm bằng generator chưa ready đúng contract, nhiều instance có thể tạo output yếu hoặc correlated.

Modern OS cố giải quyết seed readiness trong kernel RNG, nhưng application vẫn cần hiểu platform guarantee thay vì tự xây entropy pool bằng timestamp/PID.

Timestamp, process ID, MAC address hoặc username có thể khác nhau nhưng thường dễ đoán; uniqueness không đồng nghĩa entropy.

## 9. VM snapshot, fork và cloned state

Đây là failure production quan trọng.

Giả sử VM đã có CSPRNG state `S`, sau đó snapshot được clone thành hai machine:

```text
VM A: S → O1 → O2 → ...
VM B: S → O1 → O2 → ...
```

Nếu không có reseed hoặc fork/snapshot detection, hai machine có thể sinh stream giống nhau.

Tương tự, process fork có thể copy userspace PRNG state. Runtime/library tốt cần reseed hoặc split stream đúng cách.

Failure này không được phát hiện bằng statistical test trên từng stream riêng; mỗi stream vẫn trông random. Vấn đề nằm ở **correlation giữa replicas**.

## 10. Nonce, salt, IV và secret token có contract khác nhau

Không phải mọi random-looking value cần cùng property.

**Salt** trong password hashing chủ yếu cần uniqueness để phá precomputation/rainbow-table reuse; salt thường không cần secret.

**Nonce** nghĩa “number used once”. Nhiều cryptographic mode cần uniqueness dưới cùng key; random nonce chỉ là một cách đạt uniqueness với collision probability đủ thấp.

**IV** có requirement tùy cipher/mode: có mode cần unpredictable, có mode cần unique. Không được copy rule giữa các construction.

**Session/token/key** thường cần unpredictability mạnh vì attacker đoán đúng là compromise authority.

Mental model:

```text
value name
→ protocol invariant
→ required property: unique? unpredictable? secret? non-repeating?
→ generation strategy
```

## 11. Birthday bound và collision

Nếu chọn ngẫu nhiên từ space có `N` giá trị, collision trở nên đáng kể sau khoảng `sqrt(N)` samples, không phải sau `N` samples.

Với `b` random bits, collision probability tăng theo birthday effect quanh `2^(b/2)` samples.

Điều này quan trọng cho random identifier ở fleet scale. “128-bit ID rất lớn” thường đúng trong thực tế, nhưng reasoning phải dựa trên sample volume và acceptable collision risk, không chỉ cảm giác.

Nếu collision tuyệt đối không được phép theo business invariant, random ID một mình vẫn là probabilistic guarantee; có thể cần uniqueness constraint hoặc coordinated namespace.

## 12. Modulo bias

Một lỗi implementation phổ biến là lấy random integer rồi `% n` để chọn uniform trong `[0,n)` khi source range không chia hết cho `n`.

Một số outcome sẽ có nhiều preimage hơn outcome khác, tạo bias.

**Rejection sampling** giải quyết bằng cách bỏ vùng dư để mỗi outcome có số preimage bằng nhau.

Đây là ví dụ nhỏ nhưng quan trọng: high-quality random bytes có thể bị application transform làm mất distribution contract.

## 13. Sampling và load balancing không phải lúc nào cần crypto randomness

Randomized algorithm hoặc load balancer thường chỉ cần distribution tốt, speed cao và independence đủ cho workload; CSPRNG có thể không cần thiết.

Ngược lại, security token cần attacker-resistance chứ không chỉ uniform histogram.

Chọn generator theo invariant:

```text
simulation → reproducibility + statistical quality
load balancing → distribution + low overhead
security token → unpredictability + state safety
lottery/fairness → auditability + manipulation resistance
```

Dùng CSPRNG cho mọi thứ có thể đơn giản hóa API nhưng không thay thế việc xác định threat model.

## 14. Deterministic randomness trong testing là feature

Test thường muốn random input nhưng vẫn reproduce failure. Cách tốt là ghi seed:

```text
seed
→ deterministic generator
→ generated test case
→ failure
```

Khi fail, log seed hoặc shrink case để chạy lại chính xác.

Property-based testing vì vậy thường cố ý dùng pseudorandom deterministic stream. “Không random thật” ở đây là lợi ích, không phải security bug, vì invariant của testing là reproducibility.

## 15. Statistical tests không chứng minh cryptographic security

Frequency, runs, autocorrelation và test suite khác có thể phát hiện generator tệ. Nhưng pass các test đó không chứng minh attacker không predict được state.

Một linear generator có thể tạo output có histogram đẹp nhưng bị reconstruct state từ vài output.

Security cần reduction/cryptanalysis/design review phù hợp, không chỉ statistical appearance.

```text
passes randomness tests
≠ cryptographically unpredictable
```

## 16. Randomness trong distributed system

Distributed system dùng randomness cho election timeout, retry jitter, sampling hoặc randomized load spreading.

Nếu nhiều node seed giống nhau, chúng có thể đồng bộ behavior thay vì decorrelate:

```text
same seed / same timer pattern
→ synchronized retry
→ thundering herd
```

Jitter chỉ có tác dụng nếu randomization thực sự tạo đủ diversity giữa actors.

Với protocol fairness hoặc public randomness, threat model khó hơn: participant có thể cố bias output bằng cách chọn khi nào reveal contribution. Các construction như commit-reveal hoặc verifiable random function tồn tại để hạn chế manipulation, nhưng mỗi construction có liveness/trust assumption riêng.

## 17. Randomness và cryptographic key generation

Key generation cần entropy phù hợp key space và algorithm. Không được sinh key bằng password, timestamp hoặc UUID không có security contract tương đương rồi chỉ pad/hash thành đúng length.

Hashing một 32-bit random seed thành 256-bit key vẫn chỉ có khoảng 32 bit search space nếu attacker biết generation process.

```text
key length
≠ entropy of key
```

Đây là distinction quan trọng khi audit secret-generation code.

## 18. Observability mà không làm lộ secret

Không log random token/key để “debug entropy”. Evidence nên tập trung vào provenance và health metadata:

- generator/provider/version;
- seed readiness/reseed events nếu platform expose an toàn;
- fork/snapshot lifecycle;
- duplicate/collision rate của non-secret identifiers;
- entropy-source health signal;
- instance/image lineage;
- boot time và key-generation time.

Secret bytes phải được redacted. Observability không được phá chính security invariant đang kiểm tra.

## 19. Failure investigation path

Giả sử production phát hiện session token duplicate giữa hai hosts.

Reasoning path:

```text
duplicate token
→ token generation transform
→ CSPRNG stream
→ process state lineage
→ fork/container/VM snapshot
→ OS RNG seed/reseed
→ image/bootstrap behavior
```

Hypothesis có thể gồm application truncation, modulo/encoding bug, shared deterministic seed, cloned VM state hoặc token space quá nhỏ.

Evidence phải phân biệt collision xác suất bình thường với deterministic duplication.

## 20. Connection với Kolmogorov complexity

Một CSPRNG stream dài có thể computationally indistinguishable from random nhưng algorithmic description ngắn: generator + seed.

Đây không phải mâu thuẫn. Hai theory hỏi hai câu khác nhau:

```text
Kolmogorov:
Có description ngắn tồn tại không?

Cryptography:
Attacker giới hạn tài nguyên có phân biệt/dự đoán được không?
```

Đọc [Kolmogorov complexity, compression và incompressibility](./03_kolmogorov_complexity_compression_and_incompressibility.md).

## 21. Connection với information theory

Entropy source cung cấp uncertainty. CSPRNG bảo tồn/mở rộng uncertainty dưới computational assumption cho use case, nhưng deterministic expansion không tăng information-theoretic entropy thật.

Đọc [Information theory, coding bounds và noisy channels](./04_information_theory_coding_bounds_and_noisy_channels.md).

## 22. Những nhầm lẫn thường gặp

**“Hash timestamp là random.”** Không nếu timestamp có entropy thấp/dễ đoán.

**“UUID luôn đủ để làm secret.”** Không; phải biết version/generation contract và threat model.

**“256-bit output nghĩa 256 bit entropy.”** Không nếu seed/state chỉ có ít uncertainty.

**“PRNG pass statistical tests nên secure.”** Không.

**“Nonce phải luôn secret.”** Không; property chính phụ thuộc protocol, thường là uniqueness.

**“Entropy source và CSPRNG là một thứ.”** Không. Một bên đưa uncertainty vào; một bên quản lý/mở rộng state để sinh output hiệu quả.

## 23. Checklist reasoning

```text
Random value này bảo vệ invariant gì?
Cần uniqueness, unpredictability, secrecy hay reproducibility?
Entropy thực đến từ đâu?
Seed có bao nhiêu uncertainty theo attacker model?
Generator state có thể bị fork/snapshot/clone không?
Có reseed/recovery sau compromise không?
Transform sau RNG có tạo bias hoặc truncate entropy không?
Sample volume có làm collision risk đáng kể không?
Evidence nào kiểm tra provenance mà không log secret?
```

## Kết luận

Randomness trong computer system là một **state-and-provenance problem**, không phải một API call.

```text
uncertainty source
→ entropy
→ conditioning
→ seed
→ protected generator state
→ output
→ protocol invariant
```

Nếu không biết uncertainty đến từ đâu, state được clone/compromise thế nào và consumer thực sự cần property gì, từ “random” gần như không đủ thông tin kỹ thuật. Phân biệt entropy, statistical quality và computational unpredictability là nền tảng để reasoning đúng về cryptography, distributed jitter, simulation và randomized algorithms.