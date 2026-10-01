# Debugging xuyên lớp trừu tượng (abstraction / 추상화) layers: từ symptom đến bất biến (invariant / 불변식) và sự cố (incident / 인시던트) containment

> **Mạch đọc:** [README](./README.md) là owner của tuyến debugging nâng cao. File đi từ symptom tới invariant, boundary, evidence rồi mới xuống lower layer; các ví dụ về request, durability, concurrency và security chỉ minh họa cùng một quy tắc: sửa ở tầng sở hữu invariant.


Môi trường vận hành (production / 운영 환경) bug thường xuất hiện ở tầng (layer / 계층) A nhưng nguyên nhân nằm ở tầng (layer / 계층) B hoặc tương tác (interaction / 상호작용) giữa nhiều layers. Advanced debugging vì vậy cần tránh hai cực: nhảy ngay xuống assembly/kernel, hoặc chỉ nhìn ứng dụng (application / 애플리케이션) log và giả định lớp trừu tượng (abstraction / 추상화) luôn giữ.

Mô hình tư duy (mental model / 사고 모델) của chapter này là **contract-driven descent**: bắt đầu tại lớp trừu tượng (abstraction / 추상화) cao nhất còn giải thích được symptom, viết bất biến (invariant / 불변식) đang bị vi phạm, thu bằng chứng (evidence / 증거) ở ranh giới (boundary / 경계), rồi chỉ đi xuống tầng dưới khi cơ chế (mechanism / 메커니즘) ở tầng hiện tại không đủ giải thích hành vi (behavior / 동작).

## 1. Symptom không phải cơ chế (mechanism / 메커니즘), cơ chế (mechanism / 메커니즘) chưa chắc là gốc (root / 루트) điều kiện (condition / 조건)

CPU 100% là symptom. cơ chế (mechanism / 메커니즘) có thể là GC vòng lặp (loop / 루프), regex pathological, spin khóa (lock / 잠금), serialization hoặc legitimate compute. gốc (root / 루트) điều kiện (condition / 조건) có thể là thử lại (retry / 재시도) storm do downstream hết thời gian chờ (timeout / 타임아웃).

Tương tự, `401`, TLS handshake thất bại (failure / 실패) hoặc “KMS hết thời gian chờ (timeout / 타임아웃)” đều là symptom. gốc (root / 루트) điều kiện (condition / 조건) có thể là expired định danh (identity / 식별자), chính sách (policy / 정책) rollout sai, clock skew, certificate chuỗi (chain / 사슬) lỗi, secret rotation không đồng bộ hoặc điều khiển (control / 제어) plane unavailable.

Nếu chỉ sửa cơ chế (mechanism / 메커니즘) gần nhất—tăng CPU, restart pod, renew certificate bằng tay—sự cố (incident / 인시던트) có thể tái phát vì nhân quả (causal / 인과적) vòng lặp (loop / 루프) vẫn tồn tại.

## 2. Viết bất biến (invariant / 불변식) trước khi mở thêm dashboard

Một investigation mạnh bắt đầu bằng câu có thể bị chứng minh sai, ví dụ:

```text
mỗi committed order chỉ bị charge một lần
reader thấy object chỉ sau safe publication
request chỉ được xử lý khi principal có quyền tương ứng
after COMMIT OK, transaction survive failure model đã công bố
queue không được giữ work đã quá deadline
service B chỉ chấp nhận workload identity thuộc trust domain X
```

Bất biến (invariant / 불변식) giúp chọn bằng chứng (evidence / 증거). Nếu không biết thuộc tính (property / 속성) nào phải đúng, rất dễ mở hàng chục đồ thị (graph / 그래프) nhưng không biết đồ thị (graph / 그래프) nào có ý nghĩa.

## 3. ranh giới (boundary / 경계) là nơi biểu diễn (representation / 표현), authority hoặc quyền sở hữu (ownership / 소유권) thay đổi

Ở mỗi ranh giới (boundary / 경계), hỏi:

```text
representation có đổi không?
queue/buffer có xuất hiện không?
ownership/lifetime đổi không?
retry/timeout có tạo duplicate không?
clock/order assumption có đổi không?
security principal hoặc authority có đổi không?
cache có thể stale không?
durability/consistency guarantee có đổi không?
```

Nhiều bug nằm ở transformation giữa hai components đều “đúng” khi xét riêng.

## 4. bằng chứng (evidence / 증거) ladder: đi từ nhân quả (causal / 인과적) đường dẫn (path / 경로) tới lower-layer cơ chế (mechanism / 메커니즘)

Một investigation thường hiệu quả khi bằng chứng (evidence / 증거) được xếp theo câu hỏi:

```text
user-visible symptom là gì?
↓
request/transaction nào đại diện được symptom?
↓
timeline causal của request đó là gì?
↓
queue/wait/resource nào chiếm critical path?
↓
subsystem nào sở hữu resource đó?
↓
mechanism thấp hơn nào giải thích behavior?
```

Dấu vết (trace / 추적) cho nhân quả (causal / 인과적) cấu trúc (structure / 구조); metrics cho population/saturation; profiler/counters cho cơ chế (mechanism / 메커니즘); logs cho sự kiện (event / 이벤트)/ngữ cảnh (context / 맥락). Không công cụ (tool / 도구) nào một mình là “truth”.

> **Chuyển mạch:** Evidence type narrows ownership: metrics reveal saturation, traces reveal causal timing, logs reveal events. The first case separates a slow request from a fast query by locating queue wait before execution.

## 5. Ví dụ: yêu cầu (request / 요청) chậm nhưng truy vấn (query / 쿼리) nhanh

DB dashboard báo truy vấn (query / 쿼리) 20 ms, API mất 2 s. Có thể 1.8 s nằm ở connection-pool wait trước khi truy vấn (query / 쿼리) bắt đầu. truy vấn (query / 쿼리) tracing chỉ đo dịch vụ (service / 서비스) thời gian (time / 시간) sau acquire nên bỏ qua hàng đợi (queue / 큐) delay.

Fix chỉ mục (index / 인덱스) không giải. bằng chứng (evidence / 증거) cần pool utilization, acquire wait, giao dịch (transaction / 트랜잭션) duration và caller tính đồng thời (concurrency / 동시성). Lower lớp trừu tượng (abstraction / 추상화) quyết định hành vi (behavior / 동작) ở đây không phải truy vấn (query / 쿼리) optimizer mà là admission ranh giới (boundary / 경계) trước cơ sở dữ liệu (database / 데이터베이스).

## 6. Ví dụ: `write()` success nhưng dữ liệu (data / 데이터) mất sau crash

Ứng dụng (application / 애플리케이션) thấy syscall return thành công, nhưng bytes có thể mới ở kernel page bộ nhớ đệm (cache / 캐시). Nếu yêu cầu (requirement / 요구사항) là survive power mất mát (loss / 손실), lớp trừu tượng (abstraction / 추상화) “ghi (write / 쓰기) succeeded” yếu hơn bất biến (invariant / 불변식) nghiệp vụ (business / 비즈니스) cần.

Đi xuống cơ sở dữ liệu (database / 데이터베이스) WAL → syscall → filesystem → thiết bị (device / 장치) flush ngữ nghĩa (semantics / 의미론) để xác định tầng nào thực sự cung cấp persistence. Xem [đường durability xuyên tầng](./03_durability_path_application_commit_wal_filesystem_device.md).

## 7. Ví dụ: tính đồng thời (concurrency / 동시성) bug chỉ lộ trên môi trường vận hành (production / 운영 환경) hardware

Mã nguồn (source code / 소스 코드) nhìn ordered, kiểm thử (test / 테스트) trên một ISA pass nhưng môi trường vận hành (production / 운영 환경) thất bại (fail / 실패). Nếu program thiếu happens-before, kiểm thử (test / 테스트) chỉ đang dựa vào accidental timing hoặc stronger thứ tự (ordering / 순서) của một nền tảng (platform / 플랫폼).

Đi xuống ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) → trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) → ISA thứ tự (ordering / 순서) → bộ nhớ đệm (cache / 캐시)/coherence để giải thích hành vi (behavior / 동작), nhưng fix phải quay lại tầng sở hữu bất biến (invariant / 불변식) đồng bộ. Xem [đường correctness xuyên tầng](./02_correctness_path_language_os_cpu_memory_ordering.md).

> **Chuyển mạch:** Hai ví dụ về durability và concurrency cho thấy việc đi xuống tầng thấp chỉ có ích khi đã viết invariant. Từ đó, **8. bảo mật đường dẫn** mở rộng cùng quy tắc sang authority và trust boundary.

## 8. bảo mật (security / 보안) đường dẫn (path / 경로): định danh (identity / 식별자) → authorization → secret → TLS → dịch vụ (service / 서비스) ranh giới (boundary / 경계)

Một sự cố (incident / 인시던트) bảo mật (security / 보안)/độ tin cậy (reliability / 신뢰성) thường đi qua chuỗi authority chứ không dừng ở một credential.

Ví dụ dịch vụ (service / 서비스) A gọi dịch vụ (service / 서비스) B:

```text
workload/process A
→ chứng minh identity
→ nhận certificate/token/credential
→ TLS hoặc mTLS bảo vệ channel và bind peer identity
→ B xác thực principal
→ authorization policy quyết định action
→ B dùng secret/KMS capability để truy cập resource C
→ audit trail ghi lại authority đã dùng
```

Bất biến (invariant / 불변식) quan trọng là **định danh (identity / 식별자) không tự suy ra authorization**. “A là dịch vụ (service / 서비스) hợp lệ” không có nghĩa A được phép đọc mọi dataset hoặc dùng mọi KMS key.

## 9. Secret là năng lực (capability / 역량); nơi lưu secret không phải toàn bộ trust mô hình (model / 모델)

Một secret, đơn vị từ (token / 토큰) hoặc private key trao cho holder một năng lực (capability / 역량). Nếu attacker lấy được credential có quyền decrypt mọi customer key, blast radius do authorization phạm vi (scope / 범위) quyết định, không phải do encryption thuật toán (algorithm / 알고리즘) mạnh hay yếu.

Vì vậy khi gỡ lỗi (debug / 디버그) credential compromise, đừng chỉ hỏi secret bị leak ở đâu. Hỏi thêm:

```text
credential có scope gì?
lifetime bao lâu?
service nào chấp nhận nó?
key/resource nào nó truy cập được?
log nào ghi lại use?
revoke ở boundary nào?
```

Đây là liên kết (connection / 연결) trực tiếp từ secret management sang sự cố (incident / 인시던트) containment.

## 10. TLS bảo vệ channel nhưng ranh giới (boundary / 경계) phía sau vẫn cần chính sách (policy / 정책)

TLS/mTLS có thể chứng minh peer sở hữu credential cho định danh (identity / 식별자) đã được CA/trust lĩnh vực (domain / 도메인) cấp. Nó không tự quyết định nghiệp vụ (business / 비즈니스) authorization.

Một dịch vụ (service / 서비스) mesh bật mTLS toàn cluster nhưng chính sách (policy / 정책) `allow all authenticated workloads` vẫn có blast radius rất lớn nếu một tải công việc (workload / 워크로드) bị compromise. Encryption in transit không thay least privilege.

Đọc [PKI, mTLS và service identity](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).

## 11. sự cố (incident / 인시던트) containment là phá propagation đường dẫn (path / 경로) có chủ đích

Khi nghi compromise, phản hồi (response / 응답) không chỉ là “đổi password”. Mục tiêu là cắt khả năng attacker tiếp tục đi qua trust đồ thị (graph / 그래프).

Tùy sự cố (incident / 인시던트), containment có thể cần:

```text
revoke/expire credential
narrow authorization policy
disable key version hoặc KMS grant
isolate workload/network boundary
rotate downstream secrets
block token/session family
stop deployment artifact hoặc supply-chain path
preserve forensic evidence
```

Thứ tự matters. Revoke secret nhưng để attacker mint secret mới qua compromised tải công việc (workload / 워크로드) định danh (identity / 식별자) không giải quyết gốc (root / 루트) authority.

## 12. Rotation và revocation là phân tán (distributed / 분산) chuyển tiếp trạng thái (state transition / 상태 전이)

Credential mới và cũ có thể cùng tồn tại trong overlap cửa sổ (window / 윈도우). bộ nhớ đệm (cache / 캐시), long-lived liên kết (connection / 연결), đơn vị từ (token / 토큰) TTL và replica/cấu hình (config / 설정) propagation làm chính sách (policy / 정책) không đổi atomically toàn hệ thống.

Bất biến (invariant / 불변식) cần rõ: khi nào credential cũ không còn được chấp nhận? dịch vụ (service / 서비스) nào đã nhận trust bundle mới? quay lui (rollback / 롤백) có làm credential đã revoke sống lại không?

Bảo mật (security / 보안) thay đổi (change / 변경) vì vậy có cùng family với lược đồ (schema / 스키마)/giao thức (protocol / 프로토콜) evolution: nhiều versions coexist và tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) phải được quản lý.

## 13. bảo mật (security / 보안) điều khiển (control / 제어) cũng có dạng thất bại (failure mode / 실패 모드) độ tin cậy (reliability / 신뢰성)

Short-lived certificates giảm exposure cửa sổ (window / 윈도우) nhưng tăng phụ thuộc (dependency / 의존성) vào issuer/renewal đường dẫn (path / 경로). KMS fail-closed bảo vệ key nhưng có thể gây outage. Online revocation check có thể tạo mạng (network / 네트워크) phụ thuộc (dependency / 의존성) trên yêu cầu (request / 요청) đường găng (critical path / 임계 경로).

Không có nghĩa phải bỏ điều khiển (control / 제어). Nghĩa là thiết kế (design / 설계) phải biết **bảo mật (security / 보안) bất biến (invariant / 불변식) nào không được hy sinh** và **availability degradation nào chấp nhận được** khi điều khiển (control / 제어) plane thất bại (fail / 실패).

## 14. bằng chứng vận hành (production evidence / 운영 증거) cho định danh (identity / 식별자)/bảo mật (security / 보안) chuỗi (chain / 사슬)

Investigation cần nối ứng dụng (application / 애플리케이션) dấu vết (trace / 추적) với bảo mật (security / 보안) bằng chứng (evidence / 증거):

```text
principal/workload identity
certificate serial / token issuer-audience-subject
policy decision và policy version
KMS/key id + operation
service boundary nguồn/đích
TLS/certificate validation error
credential issuance/rotation/revocation event
```

Không log raw secret/đơn vị từ (token / 토큰). Mục tiêu là log định danh (identity / 식별자) và quyết định (decision / 결정) siêu dữ liệu (metadata / 메타데이터) đủ để reconstruct authority đường dẫn (path / 경로) mà không tạo thêm leakage.

## 15. thời gian (time / 시간) là phụ thuộc (dependency / 의존성) bảo mật (security / 보안) hay bị quên

Certificate validity, đơn vị từ (token / 토큰) expiry, nonce/replay cửa sổ (window / 윈도우) và log correlation đều phụ thuộc thời gian (time / 시간). Clock skew có thể làm một credential hợp lệ bị reject hoặc credential đã hết hạn vẫn được một thành phần (component / 컴포넌트) hiểu sai nếu kiểm tra hợp lệ (validation / 검증) không nhất quán.

Khi nhiều services đồng loạt báo auth thất bại (failure / 실패) sau rollout/NTP sự cố (incident / 인시던트), lower lớp trừu tượng (abstraction / 추상화) thực sự quyết định hành vi (behavior / 동작) có thể là clock discipline chứ không phải OAuth/TLS mã (code / 코드).

## 16. thất bại (failure / 실패) containment cần failure-domain lập luận (reasoning / 추론)

Nếu mọi services tin cùng một gốc (root / 루트) credential cực mạnh, compromise gốc (root / 루트) đó có blast radius toàn fleet. Nếu mỗi region/tenant/tải công việc (workload / 워크로드) có authority boundaries phù hợp, sự cố (incident / 인시던트) có thể được khoanh vùng.

Đây là lý do least privilege, separate trust domains, scoped KMS grants và mạng (network / 네트워크)/dịch vụ (service / 서비스) boundaries đều là **containment kiến trúc (architecture / 아키텍처)**, không chỉ compliance controls.

## 17. thử lại (retry / 재시도) có thể phá containment hoặc làm sự cố (incident / 인시던트) nặng hơn

Một dịch vụ (service / 서비스) auth/KMS/TLS thất bại (fail / 실패) có thể bị caller thử lại (retry / 재시도) hàng loạt. Nếu thất bại (failure / 실패) là chính sách (policy / 정책) deterministic, thử lại (retry / 재시도) vô ích và chỉ tăng tải (load / 로드) lên issuer/KMS/proxy đang có sự cố (incident / 인시던트).

Bảo mật (security / 보안) errors cần được phân loại retryable hay non-retryable. `401/403`, certificate mismatch hoặc signature invalid thường không nên được đối xử giống hết thời gian chờ (timeout / 타임아웃) transient.

Điều này nối bảo mật (security / 보안) trực tiếp với [retry → overload → backpressure](./01_end_to_end_latency_browser_edge_service_db_storage.md).

## 18. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

Khi symptom nằm ở tầng cao, hỏi đặc tả hợp đồng (contract / 계약) nào bên dưới bị phụ thuộc (dependency / 의존성):

```text
API timeout          -> queue/pool/network/runtime?
auth failure         -> identity, clock, trust chain hay policy?
data loss            -> WAL, filesystem, device hay replication ack rule?
concurrency bug       -> language model hay CPU ordering?
latency p99 spike     -> service time hay queue feedback loop?
```

Mục tiêu không phải luôn xuống tầng thấp nhất. Mục tiêu là xuống **đủ thấp để cơ chế (mechanism / 메커니즘) trở nên tất yếu**, rồi quay lại tầng sở hữu bất biến (invariant / 불변식) để sửa.

## 19. Mô hình tư duy

> Debugging xuyên layers là contract-driven descent. bảo mật (security / 보안) sự cố (incident / 인시던트) containment cũng vậy: định danh (identity / 식별자) tạo principal, authorization giới hạn năng lực (capability / 역량), secrets/keys mở quyền tới tài nguyên (resource / 자원), TLS bảo vệ dịch vụ (service / 서비스) ranh giới (boundary / 경계), còn containment cắt propagation đường dẫn (path / 경로) khi một ranh giới (boundary / 경계) bị compromise. **bằng chứng (evidence / 증거) phải reconstruct cả nhân quả (causal / 인과적) đường dẫn (path / 경로) của yêu cầu (request / 요청) lẫn authority đường dẫn (path / 경로) của principal.**

## Kết nối

Đọc cùng [leaky abstractions](../../basic/90_connections/04_abstraction_layers_and_leaky_abstractions.md), [PKI/mTLS](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md), [Secret/KMS lifecycle](../../07_security_reliability/advanced/06_secrets_kms_hsm_rotation_and_envelope_encryption.md), [End-to-end request/overload](./01_end_to_end_latency_browser_edge_service_db_storage.md), [Correctness path](./02_correctness_path_language_os_cpu_memory_ordering.md) và [Durability path](./03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 end to end latency browser edge service db storage](./01_end_to_end_latency_browser_edge_service_db_storage.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
