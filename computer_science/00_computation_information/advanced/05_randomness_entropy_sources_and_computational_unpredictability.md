# Randomness, entropy sources và computational unpredictability

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Randomness, entropy sources và computational unpredictability**. Route đi từ deterministic/pseudorandom → entropy source và extraction → unpredictability/conditioning → cryptographic randomness và failure modes, để API sinh số ngẫu nhiên luôn được đánh giá bằng nguồn và mô hình đe dọa.

Hệ thống cần randomness cho session đơn vị từ (token / 토큰), cryptographic key, nonce, randomized thuật toán (algorithm / 알고리즘), sampling, tải (load / 로드) balancing, simulation và testing. Nhưng từ “random” thường che giấu nhiều đặc tả hợp đồng (contract / 계약) khác nhau.

Một chuỗi (sequence / 시퀀스) có thể vượt qua statistical tests nhưng vẫn hoàn toàn predictable nếu attacker biết seed. Một hardware nguồn (source / 소스) có vật lý (physical / 물리적) noise nhưng biased. Một CSPRNG có đầu ra (output / 출력) rất tốt nhưng nếu trạng thái (state / 상태) bị clone qua VM snapshot, hai máy có thể sinh cùng stream. Một UUID có vẻ ngẫu nhiên nhưng không nhất thiết có bảo mật (security / 보안) entropy đủ cho secret.

Mô hình tư duy (mental model / 사고 모델):

```text
physical / environmental uncertainty
→ entropy estimation
→ conditioning / extraction
→ seed
→ deterministic generator state
→ random bytes
→ protocol-specific use
```

Chapter này phân biệt **entropy nguồn (source / 소스)**, **PRNG**, **CSPRNG**, **statistical randomness** và **computational unpredictability**, rồi nối chúng với thất bại (failure / 실패) modes môi trường vận hành (production / 운영 환경).

## 1. Deterministic computation không tự tạo entropy

Nếu program hoàn toàn deterministic và đầu vào (input / 입력)/trạng thái (state / 상태) ban đầu đã biết, đầu ra (output / 출력) cũng đã được xác định.

```text
state_0 + deterministic algorithm
→ state_1
→ output_1
→ state_2
→ output_2
```

Ta có thể kéo dài 256 bit seed thành hàng terabyte pseudorandom đầu ra (output / 출력), nhưng không tạo thêm 1 TB bất định (uncertainty / 불확실성) độc lập. Entropy của toàn stream bị giới hạn bởi bất định (uncertainty / 불확실성) thực của seed/trạng thái (state / 상태) theo threat mô hình (model / 모델).

Đây là distinction nền tảng:

```text
expansion of bits
≠ creation of entropy
```

PRNG mở rộng một seed ngắn thành stream dài có statistical properties tốt. Entropy nguồn (source / 소스) mới là nơi bất định (uncertainty / 불확실성) đi vào hệ thống (system / 시스템).

> **Nối mạch:** **1. Deterministic computation không tự tạo entropy** đặt vấn đề; **2. Entropy nguồn (source / 소스) là nguồn bất định (uncertainty / 불확실성), không phải API tên random** kiểm tra bằng chứng, rồi **3. Shannon entropy và min-entropy phục vụ câu hỏi khác nhau** mở rộng hệ quả.

## 2. Entropy nguồn (source / 소스) là nguồn bất định (uncertainty / 불확실성), không phải API tên random

Entropy có thể đến từ vật lý (physical / 물리적) noise, timing jitter, thiết bị (device / 장치) events hoặc hardware cơ chế (mechanism / 메커니즘) tùy nền tảng (platform / 플랫폼). Nhưng raw nguồn (source / 소스) thường không lý tưởng: có độ lệch (bias / 편향), correlation, health thất bại (failure / 실패) và phụ thuộc (dependency / 의존성) vào môi trường (environment / 환경).

Một entropy subsystem phải lập luận (reasoning / 추론) ít nhất:

```text
source behavior
→ amount of unpredictable variation
→ health/conditioning
→ accumulation
→ seed readiness
```

Không nên chỉ hỏi “đã gọi `/dev/random` hay API SecureRandom chưa?”. Cần hiểu thời gian chạy (runtime / 런타임)/OS đó seed generator như thế nào và vòng đời (lifecycle / 생명주기) trạng thái (state / 상태) ra sao.

> **Nối mạch:** **2. Entropy nguồn (source / 소스) là nguồn bất định (uncertainty / 불확실성), không phải API tên random** đặt vấn đề; **3. Shannon entropy và min-entropy phục vụ câu hỏi khác nhau** kiểm tra bằng chứng, rồi **4. Conditioning và extractor** mở rộng hệ quả.

## 3. Shannon entropy và min-entropy phục vụ câu hỏi khác nhau

Shannon entropy đo bất định (uncertainty / 불확실성) trung bình. bảo mật (security / 보안) thường quan tâm attacker đoán kết quả (outcome / 결과) tốt nhất tới đâu.

**Min-entropy** dùng xác suất (probability / 확률) lớn nhất:

```text
H_min(X) = -log2(max_x P(X=x))
```

Nếu một nguồn (source / 소스) có nhiều kết quả (outcome / 결과) nhưng một kết quả (outcome / 결과) xảy ra 50%, attacker đã có guess rất mạnh dù average bất định (uncertainty / 불확실성) nhìn có vẻ không quá thấp.

Vì vậy bảo mật (security / 보안) entropy estimation thường conservative hơn việc nhìn histogram “khá đều”.

> **Nối mạch:** **4. Conditioning và extractor** nối từ **3. Shannon entropy và min-entropy phục vụ câu hỏi khác nhau** sang **5. PRNG và CSPRNG**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Conditioning và extractor

Raw vật lý (physical / 물리적) nguồn (source / 소스) có thể biased/correlated. Một **conditioner/extractor** cố biến đầu vào (input / 입력) có đủ entropy thành đầu ra (output / 출력) gần uniform hơn.

Nhưng extractor không tạo entropy từ không khí. Nếu đầu vào (input / 입력) thực tế có gần zero bất định (uncertainty / 불확실성), băm (hash / 해시) nó không biến đầu ra (output / 출력) thành secret.

```text
predictable input
→ hash
→ deterministic digest
```

Digest có thể trông uniform nhưng attacker biết đầu vào (input / 입력) vẫn tính được digest.

Đây là lỗi tư duy phổ biến: **appearance of randomness** không đồng nghĩa **unpredictability**.

> **Nối mạch:** **5. PRNG và CSPRNG** nối từ **4. Conditioning và extractor** sang **6. Forward bảo mật (security / 보안) và backtracking resistance**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. PRNG và CSPRNG

PRNG thông thường tối ưu speed/statistical chất lượng (quality / 품질) cho simulation hoặc randomized thuật toán (algorithm / 알고리즘). Nếu attacker quan sát đủ đầu ra (output / 출력), trạng thái (state / 상태) có thể bị suy ra tùy thuật toán (algorithm / 알고리즘).

**Cryptographically Secure PRNG (CSPRNG)** cần đặc tả hợp đồng (contract / 계약) mạnh hơn: với attacker computationally bounded, đầu ra (output / 출력) tiếp theo phải khó dự đoán từ đầu ra (output / 출력) đã thấy nếu trạng thái (state / 상태)/seed chưa bị compromise.

CSPRNG thường dùng cryptographic thành phần nguyên thủy (primitive / 기본 요소) để cập nhật (update / 업데이트) trạng thái (state / 상태) và generate bytes. Ta lập luận (reasoning / 추론) bằng chuyển tiếp trạng thái (state transition / 상태 전이), không bằng tên API:

```text
secret state S_i
→ generate output O_i
→ evolve state to S_(i+1)
```

Bảo mật (security / 보안) phụ thuộc seed chất lượng (quality / 품질), trạng thái (state / 상태) secrecy, cập nhật (update / 업데이트) thiết kế (design / 설계) và vòng đời (lifecycle / 생명주기).

> **Nối mạch:** **6. Forward bảo mật (security / 보안) và backtracking resistance** nối từ **5. PRNG và CSPRNG** sang **7. Seed vòng đời (lifecycle / 생명주기) quan trọng hơn độ dài đầu ra (output / 출력)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Forward bảo mật (security / 보안) và backtracking resistance

Nếu attacker compromise generator trạng thái (state / 상태) tại thời điểm `t`, hai câu hỏi xuất hiện:

```text
Có reconstruct được output cũ không?
Có dự đoán được output tương lai không?
```

Một thiết kế (design / 설계) tốt có thể cố cung cấp **backtracking resistance**: trạng thái (state / 상태) hiện tại không đủ để recover đầu ra (output / 출력) quá khứ đã xóa khỏi trạng thái (state / 상태).

Nếu generator sau đó nhận entropy mới và reseed, nó có thể lấy lại unpredictability cho tương lai. Đây thường được gọi theo các khái niệm như prediction resistance/khôi phục (recovery / 복구) tùy construction.

Không có generator nào cứu được giao thức (protocol / 프로토콜) nếu attacker đọc trực tiếp random bytes ngay khi ứng dụng (application / 애플리케이션) sử dụng chúng.

> **Nối mạch:** **6. Forward bảo mật (security / 보안) và backtracking resistance** đặt đầu vào cho **7. Seed vòng đời (lifecycle / 생명주기) quan trọng hơn độ dài đầu ra (output / 출력)**, rồi **8. Boot-time entropy và early-start thất bại (failure / 실패)** mở rộng hệ quả.

## 7. Seed vòng đời (lifecycle / 생명주기) quan trọng hơn độ dài đầu ra (output / 출력)

Một generator có đầu ra (output / 출력) 4096-bit không mạnh nếu seed chỉ có 20 bit bất định (uncertainty / 불확실성). Attacker có thể brute-force seed không gian (space / 공간) rồi regenerate toàn stream.

Bảo mật (security / 보안) lập luận (reasoning / 추론) phải đi ngược:

```text
secret/token
← generator output
← generator state
← seed
← entropy sources
```

Đây là **entropy provenance**. Khi sự cố (incident / 인시던트) xảy ra, cần biết secret được sinh ở đâu, khi nào, trên machine trạng thái (state / 상태) nào và generator đã seed/reseed chưa.

> **Nối mạch:** **7. Seed vòng đời (lifecycle / 생명주기) quan trọng hơn độ dài đầu ra (output / 출력)** đặt đầu vào cho **8. Boot-time entropy và early-start thất bại (failure / 실패)**, rồi **9. VM snapshot, fork và cloned trạng thái (state / 상태)** mở rộng hệ quả.

## 8. Boot-time entropy và early-start thất bại (failure / 실패)

Ngay sau boot, VM/bộ chứa (container / 컨테이너)/embedded thiết bị (device / 장치) có thể chưa thu đủ environmental entropy. Nếu dịch vụ (service / 서비스) tạo host key, TLS key hoặc session secret quá sớm bằng generator chưa ready đúng đặc tả hợp đồng (contract / 계약), nhiều instance có thể tạo đầu ra (output / 출력) yếu hoặc correlated.

Hiện đại (modern / 현대적) OS cố giải quyết seed readiness trong kernel RNG, nhưng ứng dụng (application / 애플리케이션) vẫn cần hiểu nền tảng (platform / 플랫폼) guarantee thay vì tự xây entropy pool bằng timestamp/PID.

Timestamp, tiến trình (process / 프로세스) ID, MAC address hoặc username có thể khác nhau nhưng thường dễ đoán; uniqueness không đồng nghĩa entropy.

> **Nối mạch:** **9. VM snapshot, fork và cloned trạng thái (state / 상태)** nối từ **8. Boot-time entropy và early-start thất bại (failure / 실패)** sang **10. Nonce, salt, IV và secret đơn vị từ (token / 토큰) có đặc tả hợp đồng (contract / 계약) khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. VM snapshot, fork và cloned trạng thái (state / 상태)

Đây là thất bại (failure / 실패) môi trường vận hành (production / 운영 환경) quan trọng.

Giả sử VM đã có CSPRNG trạng thái (state / 상태) `S`, sau đó snapshot được clone thành hai machine:

```text
VM A: S → O1 → O2 → ...
VM B: S → O1 → O2 → ...
```

Nếu không có reseed hoặc fork/snapshot detection, hai machine có thể sinh stream giống nhau.

Tương tự, tiến trình (process / 프로세스) fork có thể bản sao (copy / 복사) userspace PRNG trạng thái (state / 상태). thời gian chạy (runtime / 런타임)/thư viện (library / 라이브러리) tốt cần reseed hoặc split stream đúng cách.

Thất bại (failure / 실패) này không được phát hiện bằng statistical kiểm thử (test / 테스트) trên từng stream riêng; mỗi stream vẫn trông random. Vấn đề nằm ở **correlation giữa replicas**.

> **Nối mạch:** **10. Nonce, salt, IV và secret đơn vị từ (token / 토큰) có đặc tả hợp đồng (contract / 계약) khác nhau** nối từ **9. VM snapshot, fork và cloned trạng thái (state / 상태)** sang **11. Birthday bound và collision**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Nonce, salt, IV và secret đơn vị từ (token / 토큰) có đặc tả hợp đồng (contract / 계약) khác nhau

Không phải mọi random-looking giá trị (value / 값) cần cùng thuộc tính (property / 속성).

**Salt** trong password hashing chủ yếu cần uniqueness để phá precomputation/rainbow-table reuse; salt thường không cần secret.

**Nonce** nghĩa “number used once”. Nhiều cryptographic chế độ (mode / 모드) cần uniqueness dưới cùng key; random nonce chỉ là một cách đạt uniqueness với collision xác suất (probability / 확률) đủ thấp.

**IV** có yêu cầu (requirement / 요구사항) tùy cipher/chế độ (mode / 모드): có chế độ (mode / 모드) cần unpredictable, có chế độ (mode / 모드) cần unique. Không được bản sao (copy / 복사) quy tắc (rule / 규칙) giữa các construction.

**Session/đơn vị từ (token / 토큰)/key** thường cần unpredictability mạnh vì attacker đoán đúng là compromise authority.

Mô hình tư duy (mental model / 사고 모델):

```text
value name
→ protocol invariant
→ required property: unique? unpredictable? secret? non-repeating?
→ generation strategy
```

> **Nối mạch:** **11. Birthday bound và collision** nối từ **10. Nonce, salt, IV và secret đơn vị từ (token / 토큰) có đặc tả hợp đồng (contract / 계약) khác nhau** sang **12. Modulo độ lệch (bias / 편향)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Birthday bound và collision

Nếu chọn ngẫu nhiên từ không gian (space / 공간) có `N` giá trị, collision trở nên đáng kể sau khoảng `sqrt(N)` samples, không phải sau `N` samples.

Với `b` random bits, collision xác suất (probability / 확률) tăng theo birthday tác động (effect / 효과) quanh `2^(b/2)` samples.

Điều này quan trọng cho random identifier ở fleet quy mô (scale / 규모). “128-bit ID rất lớn” thường đúng trong thực tế, nhưng lập luận (reasoning / 추론) phải dựa trên mẫu (sample / 표본) volume và acceptable collision rủi ro (risk / 위험), không chỉ cảm giác.

Nếu collision tuyệt đối không được phép theo nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식), random ID một mình vẫn là probabilistic guarantee; có thể cần uniqueness ràng buộc (constraint / 제약조건) hoặc coordinated không gian tên (namespace / 네임스페이스).

> **Nối mạch:** **12. Modulo độ lệch (bias / 편향)** nối từ **11. Birthday bound và collision** sang **13. Sampling và tải (load / 로드) balancing không phải lúc nào cần crypto randomness**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Modulo độ lệch (bias / 편향)

Một lỗi hiện thực (implementation / 구현) phổ biến là lấy random integer rồi `% n` để chọn uniform trong `[0,n)` khi nguồn (source / 소스) phạm vi (range / 범위) không chia hết cho `n`.

Một số kết quả (outcome / 결과) sẽ có nhiều preimage hơn kết quả (outcome / 결과) khác, tạo độ lệch (bias / 편향).

**Rejection sampling** giải quyết bằng cách bỏ vùng dư để mỗi kết quả (outcome / 결과) có số preimage bằng nhau.

Đây là ví dụ nhỏ nhưng quan trọng: high-quality random bytes có thể bị ứng dụng (application / 애플리케이션) transform làm mất phân phối (distribution / 분포) đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** **13. Sampling và tải (load / 로드) balancing không phải lúc nào cần crypto randomness** nối từ **12. Modulo độ lệch (bias / 편향)** sang **14. Deterministic randomness trong testing là tính năng (feature / 기능)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Sampling và tải (load / 로드) balancing không phải lúc nào cần crypto randomness

Randomized thuật toán (algorithm / 알고리즘) hoặc bộ cân bằng tải (load balancer / 로드 밸런서) thường chỉ cần phân phối (distribution / 분포) tốt, speed cao và independence đủ cho tải công việc (workload / 워크로드); CSPRNG có thể không cần thiết.

Ngược lại, bảo mật (security / 보안) đơn vị từ (token / 토큰) cần attacker-resistance chứ không chỉ uniform histogram.

Chọn generator theo bất biến (invariant / 불변식):

```text
simulation → reproducibility + statistical quality
load balancing → distribution + low overhead
security token → unpredictability + state safety
lottery/fairness → auditability + manipulation resistance
```

Dùng CSPRNG cho mọi thứ có thể đơn giản hóa API nhưng không thay thế việc xác định threat mô hình (model / 모델).

> **Nối mạch:** **14. Deterministic randomness trong testing là tính năng (feature / 기능)** nối từ **13. Sampling và tải (load / 로드) balancing không phải lúc nào cần crypto randomness** sang **15. Statistical tests không chứng minh cryptographic bảo mật (security / 보안)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Deterministic randomness trong testing là tính năng (feature / 기능)

Kiểm thử (test / 테스트) thường muốn random đầu vào (input / 입력) nhưng vẫn reproduce thất bại (failure / 실패). Cách tốt là ghi seed:

```text
seed
→ deterministic generator
→ generated test case
→ failure
```

Khi thất bại (fail / 실패), log seed hoặc shrink trường hợp (case / 사례) để chạy lại chính xác.

Property-based testing vì vậy thường cố ý dùng pseudorandom deterministic stream. “Không random thật” ở đây là lợi ích, không phải bảo mật (security / 보안) bug, vì bất biến (invariant / 불변식) của testing là reproducibility.

> **Nối mạch:** **15. Statistical tests không chứng minh cryptographic bảo mật (security / 보안)** nối từ **14. Deterministic randomness trong testing là tính năng (feature / 기능)** sang **16. Randomness trong hệ thống phân tán (distributed system / 분산 시스템)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Statistical tests không chứng minh cryptographic bảo mật (security / 보안)

Frequency, runs, autocorrelation và bộ kiểm thử (test suite / 테스트 스위트) khác có thể phát hiện generator tệ. Nhưng pass các kiểm thử (test / 테스트) đó không chứng minh attacker không predict được trạng thái (state / 상태).

Một tuyến tính (linear / 선형) generator có thể tạo đầu ra (output / 출력) có histogram đẹp nhưng bị reconstruct trạng thái (state / 상태) từ vài đầu ra (output / 출력).

Bảo mật (security / 보안) cần reduction/cryptanalysis/thiết kế (design / 설계) rà soát (review / 검토) phù hợp, không chỉ statistical appearance.

```text
passes randomness tests
≠ cryptographically unpredictable
```

> **Nối mạch:** **16. Randomness trong hệ thống phân tán (distributed system / 분산 시스템)** nối từ **15. Statistical tests không chứng minh cryptographic bảo mật (security / 보안)** sang **17. Randomness và cryptographic key generation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Randomness trong hệ thống phân tán (distributed system / 분산 시스템)

Hệ thống phân tán (distributed system / 분산 시스템) dùng randomness cho election hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도) jitter, sampling hoặc randomized tải (load / 로드) spreading.

Nếu nhiều nút (node / 노드) seed giống nhau, chúng có thể đồng bộ hành vi (behavior / 동작) thay vì decorrelate:

```text
same seed / same timer pattern
→ synchronized retry
→ thundering herd
```

Jitter chỉ có tác dụng nếu randomization thực sự tạo đủ diversity giữa actors.

Với giao thức (protocol / 프로토콜) fairness hoặc công khai (public / 공개) randomness, threat mô hình (model / 모델) khó hơn: participant có thể cố độ lệch (bias / 편향) đầu ra (output / 출력) bằng cách chọn khi nào reveal contribution. Các construction như commit-reveal hoặc verifiable random hàm (function / 함수) tồn tại để hạn chế manipulation, nhưng mỗi construction có liveness/trust giả định (assumption / 가정) riêng.

> **Nối mạch:** **17. Randomness và cryptographic key generation** nối từ **16. Randomness trong hệ thống phân tán (distributed system / 분산 시스템)** sang **18. khả năng quan sát (observability / 관측 가능성) mà không làm lộ secret**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Randomness và cryptographic key generation

Key generation cần entropy phù hợp key không gian (space / 공간) và thuật toán (algorithm / 알고리즘). Không được sinh key bằng password, timestamp hoặc UUID không có bảo mật (security / 보안) đặc tả hợp đồng (contract / 계약) tương đương rồi chỉ pad/băm (hash / 해시) thành đúng length.

Hashing một 32-bit random seed thành 256-bit key vẫn chỉ có khoảng 32 bit tìm kiếm (search / 검색) không gian (space / 공간) nếu attacker biết generation tiến trình (process / 프로세스).

```text
key length
≠ entropy of key
```

Đây là distinction quan trọng khi kiểm tra (audit / 감사) secret-generation mã (code / 코드).

> **Nối mạch:** **18. khả năng quan sát (observability / 관측 가능성) mà không làm lộ secret** nối từ **17. Randomness và cryptographic key generation** sang **19. thất bại (failure / 실패) investigation đường dẫn (path / 경로)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. khả năng quan sát (observability / 관측 가능성) mà không làm lộ secret

Không log random đơn vị từ (token / 토큰)/key để “gỡ lỗi (debug / 디버그) entropy”. bằng chứng (evidence / 증거) nên tập trung vào provenance và health siêu dữ liệu (metadata / 메타데이터):

- generator/provider/phiên bản (version / 버전);
- seed readiness/reseed events nếu nền tảng (platform / 플랫폼) expose an toàn;
- fork/snapshot vòng đời (lifecycle / 생명주기);
- duplicate/collision tỷ lệ (rate / 비율) của non-secret identifiers;
- entropy-source health tín hiệu (signal / 신호);
- instance/ảnh (image / 이미지) lineage;
- boot thời gian (time / 시간) và key-generation thời gian (time / 시간).

Secret bytes phải được redacted. khả năng quan sát (observability / 관측 가능성) không được phá chính bảo mật (security / 보안) bất biến (invariant / 불변식) đang kiểm tra.

> **Nối mạch:** **18. khả năng quan sát (observability / 관측 가능성) mà không làm lộ secret** đặt đầu vào cho **19. thất bại (failure / 실패) investigation đường dẫn (path / 경로)**, rồi **20. liên kết (connection / 연결) với Kolmogorov độ phức tạp (complexity / 복잡도)** mở rộng hệ quả.

## 19. thất bại (failure / 실패) investigation đường dẫn (path / 경로)

Giả sử môi trường vận hành (production / 운영 환경) phát hiện session đơn vị từ (token / 토큰) duplicate giữa hai hosts.

Lập luận (reasoning / 추론) đường dẫn (path / 경로):

```text
duplicate token
→ token generation transform
→ CSPRNG stream
→ process state lineage
→ fork/container/VM snapshot
→ OS RNG seed/reseed
→ image/bootstrap behavior
```

Hypothesis có thể gồm ứng dụng (application / 애플리케이션) truncation, modulo/encoding bug, dùng chung (shared / 공유) deterministic seed, cloned VM trạng thái (state / 상태) hoặc đơn vị từ (token / 토큰) không gian (space / 공간) quá nhỏ.

Bằng chứng (evidence / 증거) phải phân biệt collision xác suất bình thường với deterministic duplication.

> **Nối mạch:** **19. thất bại (failure / 실패) investigation đường dẫn (path / 경로)** đặt đầu vào cho **20. liên kết (connection / 연결) với Kolmogorov độ phức tạp (complexity / 복잡도)**, rồi **21. liên kết (connection / 연결) với thông tin (information / 정보) lý thuyết (theory / 이론)** mở rộng hệ quả.

## 20. liên kết (connection / 연결) với Kolmogorov độ phức tạp (complexity / 복잡도)

Một CSPRNG stream dài có thể computationally indistinguishable from random nhưng algorithmic description ngắn: generator + seed.

Đây không phải mâu thuẫn. Hai lý thuyết (theory / 이론) hỏi hai câu khác nhau:

```text
Kolmogorov:
Có description ngắn tồn tại không?

Cryptography:
Attacker giới hạn tài nguyên có phân biệt/dự đoán được không?
```

Đọc [Kolmogorov complexity, compression và incompressibility](./03_kolmogorov_complexity_compression_and_incompressibility.md).

> **Nối mạch:** **21. liên kết (connection / 연결) với thông tin (information / 정보) lý thuyết (theory / 이론)** nối từ **20. liên kết (connection / 연결) với Kolmogorov độ phức tạp (complexity / 복잡도)** sang **22. Những nhầm lẫn thường gặp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. liên kết (connection / 연결) với thông tin (information / 정보) lý thuyết (theory / 이론)

Entropy nguồn (source / 소스) cung cấp bất định (uncertainty / 불확실성). CSPRNG bảo tồn/mở rộng bất định (uncertainty / 불확실성) dưới computational giả định (assumption / 가정) cho use trường hợp (case / 사례), nhưng deterministic expansion không tăng information-theoretic entropy thật.

Đọc [Information theory, coding bounds và noisy channels](./04_information_theory_coding_bounds_and_noisy_channels.md).

> **Nối mạch:** **21. liên kết (connection / 연결) với thông tin (information / 정보) lý thuyết (theory / 이론)** đặt tiêu chí; **22. Những nhầm lẫn thường gặp** dùng nó để kiểm tra ranh giới, rồi **23. Checklist lập luận (reasoning / 추론)** mở rộng hệ quả.

## 22. Những nhầm lẫn thường gặp

**“băm (hash / 해시) timestamp là random.”** Không nếu timestamp có entropy thấp/dễ đoán.

**“UUID luôn đủ để làm secret.”** Không; phải biết phiên bản (version / 버전)/generation đặc tả hợp đồng (contract / 계약) và threat mô hình (model / 모델).

**“256-bit đầu ra (output / 출력) nghĩa 256 bit entropy.”** Không nếu seed/trạng thái (state / 상태) chỉ có ít bất định (uncertainty / 불확실성).

**“PRNG pass statistical tests nên secure.”** Không.

**“Nonce phải luôn secret.”** Không; thuộc tính (property / 속성) chính phụ thuộc giao thức (protocol / 프로토콜), thường là uniqueness.

**“Entropy nguồn (source / 소스) và CSPRNG là một thứ.”** Không. Một bên đưa bất định (uncertainty / 불확실성) vào; một bên quản lý/mở rộng trạng thái (state / 상태) để sinh đầu ra (output / 출력) hiệu quả.

> **Nối mạch:** **22. Những nhầm lẫn thường gặp** đặt tiêu chí; **23. Checklist lập luận (reasoning / 추론)** dùng nó để kiểm tra ranh giới, rồi **Kết luận** mở rộng hệ quả.

## 23. Checklist lập luận (reasoning / 추론)

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

> **Nối mạch:** **Kết luận** tổng hợp từ **23. Checklist lập luận (reasoning / 추론)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết luận

Randomness trong computer hệ thống (system / 시스템) là một **state-and-provenance bài toán (problem / 문제)**, không phải một API lời gọi (call / 호출).

```text
uncertainty source
→ entropy
→ conditioning
→ seed
→ protected generator state
→ output
→ protocol invariant
```

Nếu không biết bất định (uncertainty / 불확실성) đến từ đâu, trạng thái (state / 상태) được clone/compromise thế nào và bên tiêu thụ (consumer / 소비자) thực sự cần thuộc tính (property / 속성) gì, từ “random” gần như không đủ thông tin kỹ thuật. Phân biệt entropy, statistical chất lượng (quality / 품질) và computational unpredictability là nền tảng để lập luận (reasoning / 추론) đúng về cryptography, phân tán (distributed / 분산) jitter, simulation và randomized algorithms.

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
