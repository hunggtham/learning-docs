# Detection kỹ thuật (engineering / 엔지니어링), forensics và sự cố (incident / 인시던트) bằng chứng (evidence / 증거)

> **Mạch đọc:** Đặt **Detection kỹ thuật (engineering / 엔지니어링), forensics và sự cố (incident / 인시던트) bằng chứng (evidence / 증거)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Detection bắt đầu từ bất biến (invariant / 불변식), không bắt đầu từ SIEM quy tắc (rule / 규칙)** sang **2. Telemetry không phải sự thật tuyệt đối**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đọc trước [Security boundaries, attack chains và exploitability](./00_security_boundaries_attack_chains_and_exploitability.md). Chapter này bắt đầu từ một giới hạn căn bản: **preventive điều khiển (control / 제어) không thể được giả định là hoàn hảo**. Authentication có thể bị bypass, credential có thể bị lộ, chính sách (policy / 정책) có thể cấu hình sai, phụ thuộc (dependency / 의존성) có thể fail-open, và một hành vi hợp lệ riêng lẻ có thể trở nên nguy hiểm khi ghép thành attack chuỗi (chain / 사슬).

Vì vậy bảo mật (security / 보안) môi trường vận hành (production / 운영 환경) cần một đường lập luận (reasoning / 추론) khác:

```text
security invariant
→ telemetry về state/action
→ detection hypothesis
→ signal / correlation
→ triage
→ investigation
→ containment
→ recovery
→ learning / control improvement
```

Mục tiêu không phải “log thật nhiều”. Mục tiêu là giữ đủ bằng chứng (evidence / 증거) để phân biệt hypothesis và tái dựng authority đường dẫn (path / 경로) khi bất biến (invariant / 불변식) bị vi phạm.

## 1. Detection bắt đầu từ bất biến (invariant / 불변식), không bắt đầu từ SIEM quy tắc (rule / 규칙)

Một detection quy tắc (rule / 규칙) chỉ có ý nghĩa khi ta biết nó đang bảo vệ điều gì. Ví dụ bất biến (invariant / 불변식) có thể là:

```text
chỉ workload X được phép dùng key Y
một user không thể approve chính request do mình tạo
service A không được gọi admin endpoint của service B
```

Từ bất biến (invariant / 불변식) đó mới suy ra sự kiện (event / 이벤트) nào cần quan sát: principal, tài nguyên (resource / 자원), hành động (action / 동작), chính sách (policy / 정책) quyết định (decision / 결정), credential/key ID, nguồn (source / 소스) ngữ cảnh (context / 맥락), kết quả (result / 결과) và timestamp.

Nếu bắt đầu bằng “hãy collect tất cả logs”, hệ thống dễ tạo noise và chi phí (cost / 비용) nhưng không tăng khả năng lập luận (reasoning / 추론).

## 2. Telemetry không phải sự thật tuyệt đối

Log là một observation được tạo bởi thành phần (component / 컴포넌트) cụ thể. Nếu thành phần (component / 컴포넌트) bị compromise, disabled hoặc overloaded, telemetry có thể thiếu hoặc sai.

Vì vậy bằng chứng (evidence / 증거) strength phụ thuộc trust ranh giới (boundary / 경계):

```text
application self-log
< independent gateway / identity-provider evidence
< tamper-resistant audit pipeline
```

Thứ tự này không phải universal ranking, nhưng nhắc rằng nguồn bằng chứng (evidence / 증거) và threat mô hình (model / 모델) phải được xét cùng nhau.

## 3. sự kiện (event / 이벤트) lược đồ (schema / 스키마) phải giữ định danh (identity / 식별자) và causality

Một sự kiện (event / 이벤트) bảo mật (security / 보안) hữu ích thường cần ít nhất:

```text
who: principal / workload / user / service identity
what: action
which: resource / object / tenant
why: policy / grant / role / token audience-scope
when: timestamp + ordering context
where: host / region / network / process / session
result: success / deny / error
correlation: request / trace / session / transaction id
```

Thiếu định danh (identity / 식별자) hoặc đối tượng (object / 객체) phạm vi (scope / 범위) khiến sự cố (incident / 인시던트) responder chỉ biết “API admin đã được gọi” nhưng không biết ai có authority tại thời điểm đó.

## 4. Base-rate bài toán (problem / 문제) làm alert hiếm rất khó

Giả sử detector có độ chính xác tưởng như rất tốt nhưng attack thực sự cực hiếm. Số false positive vẫn có thể lớn hơn true positive rất nhiều.

Đây là base-rate bài toán (problem / 문제). Vì vậy detection kỹ thuật (engineering / 엔지니어링) phải cân precision/recall theo prior xác suất (probability / 확률) và analyst sức chứa (capacity / 용량), không chỉ nhìn một chỉ số (metric / 지표) classifier.

Alert fatigue là dạng thất bại (failure mode / 실패 모드) của hệ thống (system / 시스템) thiết kế (design / 설계), không chỉ là vấn đề con người “không tập trung”.

### Đo chất lượng detector trong môi trường vận hành (production / 운영 환경)

Một detector không thể được đánh giá chỉ bằng số alert hoặc một accuracy score. Trước hết phải xác định **đơn vị phát hiện** và nguồn label:

```text
event-level: event nào đáng nghi?
session/identity-level: principal nào cần điều tra?
incident-level: chuỗi hành vi nào thực sự tạo impact?
```

Labels có thể đến từ sự cố (incident / 인시던트) đã được adjudicate, replay dữ liệu lịch sử, controlled benign/malicious scenario hoặc analyst rà soát (review / 검토). Mỗi nguồn có độ lệch (bias / 편향) riêng: sự cố (incident / 인시던트) thật thường hiếm, replay có thể thiếu attacker adaptation, còn synthetic scenario dễ sạch hơn môi trường vận hành (production / 운영 환경).

Một đo lường (measurement / 측정) set hữu ích nên giữ ít nhất:

```text
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
alert rate / analyst-minute
false-negative exposure theo asset/identity/impact
time-to-detect và time-to-triage
```

`Recall` không có ý nghĩa nếu denominator chỉ gồm những trường hợp (case / 사례) detector đã nhìn thấy. Cần ghi rõ phạm vi (scope / 범위), observation cửa sổ (window / 윈도우) và những blind spot do telemetry thiếu. Ngược lại, precision cao nhưng mỗi alert cần một giờ điều tra vẫn có thể vượt analyst sức chứa (capacity / 용량).

Threshold nên được chọn theo chi phí (cost / 비용) asymmetry:

```text
false negative cost × exposure
vs
false positive cost × analyst capacity
```

Khi prevalence thay đổi, precision có thể đổi dù quy tắc (rule / 규칙) không đổi. Vì vậy đo lường (measurement / 측정) nên được phân tầng theo tenant/asset criticality, traffic regime, triển khai (deployment / 배포) cohort và attack scenario; không gộp mọi sự kiện (event / 이벤트) thành một con số đẹp. Calibration cũng quan trọng: score 0.8 chỉ hữu ích nếu ranking/meaning của score ổn định giữa các cohort.

Cổng chất lượng (quality gate / 품질 게이트) tối thiểu là detector có regression set, data-quality monitor, known blind-spot danh sách (list / 목록), đơn vị sở hữu (owner / 오너) chịu trách nhiệm và lịch rà soát (review / 검토) sau sự cố (incident / 인시던트). Không dùng số alert thấp làm proxy cho chất lượng nếu chưa chứng minh recall và telemetry coverage.

## 5. Correlation tạo ngữ cảnh (context / 맥락) nhưng cũng có thất bại (failure / 실패) modes

Một login lạ chưa chắc là attack. Một privilege thay đổi (change / 변경) riêng lẻ có thể hợp lệ. Nhưng chuỗi:

```text
new device login
→ privilege grant
→ secret read
→ unusual outbound transfer
```

có evidential giá trị (value / 값) mạnh hơn.

Correlation có thể theo định danh (identity / 식별자), host, tài nguyên (resource / 자원), dấu vết (trace / 추적), temporal cửa sổ (window / 윈도우) hoặc đồ thị (graph / 그래프) relationship. Tuy nhiên cửa sổ (window / 윈도우) quá rộng tăng false positives; quá hẹp bỏ sót slow attack. thực thể (entity / 엔터티) resolution sai có thể ghép nhầm hai users/services.

## 6. Detection là hypothesis kiểm thử (test / 테스트), không phải verdict

Một alert nên được đọc như:

> “bằng chứng (evidence / 증거) hiện tại làm hypothesis X đáng điều tra hơn baseline.”

Không nên biến detector score thành sự thật tuyệt đối. Triage cần tìm disconfirming bằng chứng (evidence / 증거), nghiệp vụ (business / 비즈니스) ngữ cảnh (context / 맥락) và known-change ngữ cảnh (context / 맥락).

Mô hình tư duy (mental model / 사고 모델) gần với debugging:

```text
symptom
→ competing hypotheses
→ discriminating evidence
→ containment decision
```

## 7. thời gian (time / 시간) là một phần của forensic tính đúng đắn (correctness / 정확성)

Cross-system investigation phụ thuộc clocks. Nếu hosts lệch thời gian, cùng attack chuỗi (chain / 사슬) có thể trông đảo thứ tự.

Wall-clock timestamp nên đi cùng monotonic/chuỗi (sequence / 시퀀스)/correlation bằng chứng (evidence / 증거) khi có thể. Distributed-system clock bất định (uncertainty / 불확실성) trong [time, clocks và causality](../../06_networks_distributed_systems/advanced/06_time_clocks_ordering_and_causality.md) áp dụng trực tiếp cho sự cố (incident / 인시던트) reconstruction.

Không nên suy luận nhân quả (causal / 인과적) thứ tự (order / 순서) chỉ từ hai timestamps gần nhau khi bất định (uncertainty / 불확실성) lớn hơn khoảng cách giữa chúng.

## 8. Immutable/tamper-evident nhật ký kiểm tra (audit log / 감사 로그) bảo vệ bằng chứng (evidence / 증거) đường dẫn (path / 경로)

Nếu attacker có cùng quyền sửa ứng dụng (application / 애플리케이션) trạng thái (state / 상태) và xóa kiểm tra (audit / 감사) logs, forensic confidence giảm mạnh.

Kiểm tra (audit / 감사) kiến trúc (architecture / 아키텍처) thường cố gắng tách quyền:

```text
producer can append event
producer cannot silently rewrite history
retention store has separate authority
access to evidence is itself audited
```

Cơ chế cụ thể có thể là append-only lưu trữ (storage / 저장소), WORM retention, signed batches hoặc restricted logging account. mô hình tư duy (mental model / 사고 모델) là **bằng chứng (evidence / 증거) authority phải độc lập hơn điều khiển (control / 제어) plane đang bị điều tra**.

## 9. chuỗi (chain / 사슬) of custody quan trọng khi bằng chứng (evidence / 증거) có hậu quả pháp lý hoặc compliance

Trong nhiều sự cố (incident / 인시던트) nội bộ, kỹ thuật (engineering / 엔지니어링) chỉ cần đủ bằng chứng (evidence / 증거) để fix hệ thống (system / 시스템). Nhưng khi bằng chứng (evidence / 증거) được dùng cho kiểm tra (audit / 감사)/pháp lý, cần provenance rõ: ai thu thập, công cụ (tool / 도구)/phiên bản (version / 버전) nào, băm (hash / 해시)/integrity nào, thời điểm nào và bản gốc ở đâu.

Bản sao (copy / 복사) tệp (file / 파일) log không kèm provenance có thể hữu ích kỹ thuật nhưng yếu hơn cho formal investigation.

## 10. Ephemeral hạ tầng (infrastructure / 인프라) làm forensic cửa sổ (window / 윈도우) ngắn hơn

Bộ chứa (container / 컨테이너)/pod/serverless instance có thể biến mất sau vài phút. Nếu chỉ giữ bằng chứng (evidence / 증거) trên cục bộ (local / 로컬) disk, autoscaling/restart có thể xóa ngữ cảnh (context / 맥락) trước khi responder biết sự cố (incident / 인시던트) xảy ra.

Do đó telemetry chuỗi xử lý (pipeline / 파이프라인) phải cân:

```text
ephemeral lifetime
vs
export latency
vs
retention cost
```

Trọng yếu (critical / 중요) định danh (identity / 식별자)/chính sách (policy / 정책)/kiểm tra (audit / 감사) events thường cần ship ra ngoài miền lỗi (failure domain / 장애 도메인) sớm hơn gỡ lỗi (debug / 디버그) logs thông thường.

## 11. bộ nhớ (memory / 메모리) và tiến trình (process / 프로세스) trạng thái (state / 상태) đôi khi quan trọng hơn disk logs

Credential theft, injected mã (code / 코드) hoặc in-memory malware có thể không để lại sản phẩm tạo ra (artifact / 산출물) rõ trên filesystem. tiến trình (process / 프로세스) cây (tree / 트리), open connections, loaded modules, bộ nhớ (memory / 메모리) mappings và thời gian chạy (runtime / 런타임) trạng thái (state / 상태) có thể là bằng chứng (evidence / 증거).

Tuy nhiên collection có overhead và privacy impact. Không có bất biến (invariant / 불변식) “capture everything”. Điều cần thiết là forensic readiness phù hợp threat mô hình (model / 모델).

## 12. mạng (network / 네트워크) bằng chứng (evidence / 증거) nói được đường dẫn (path / 경로), không luôn nói được intent

Luồng (flow / 흐름) logs, liên kết (connection / 연결) siêu dữ liệu (metadata / 메타데이터), DNS logs và proxy logs có thể cho biết ai nói chuyện với ai, volume, timing và tuyến (route / 경로). Payload encrypted có thể không quan sát được nội dung.

Một outbound liên kết (connection / 연결) lớn không tự chứng minh exfiltration. Nó cần ngữ cảnh (context / 맥락) về principal, dataset, destination trust và nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작).

## 13. định danh (identity / 식별자) bằng chứng (evidence / 증거) thường là trục chính của cloud/dịch vụ (service / 서비스) sự cố (incident / 인시던트)

Trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들) hiện đại, “host nào bị hack?” thường không đủ. Authority có thể đi qua tải công việc (workload / 워크로드) định danh (identity / 식별자), đơn vị từ (token / 토큰) exchange, role giả định (assumption / 가정), dịch vụ (service / 서비스) account hoặc delegated OAuth phạm vi (scope / 범위).

Investigation nên dựng đồ thị (graph / 그래프):

```text
credential source
→ principal
→ granted role/policy
→ resource access
→ downstream capability
→ impact
```

Đây là continuation của authority đồ thị (graph / 그래프) trong chapter bảo mật (security / 보안) boundaries.

## 14. Secret rotation là một forensic chuyển tiếp trạng thái (state transition / 상태 전이)

Khi credential bị nghi compromise, rotation/revocation không phải chỉ thay secret string. Cần biết đơn vị từ (token / 토큰)/session/bộ nhớ đệm (cache / 캐시) nào còn sống, dịch vụ (service / 서비스) nào chưa reload, replica nào chưa nhận chính sách (policy / 정책) mới và old credential được chấp nhận đến khi nào.

Containment timeline phải đo **effective revocation**, không chỉ thời điểm operator bấm “rotate”. Đọc thêm [KMS, HSM, rotation và envelope encryption](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md).

## 15. False negative thường đến từ missing telemetry hoặc attacker adaptation

Detector có thể bỏ sót vì sự kiện (event / 이벤트) không được emit, parser thất bại (fail / 실패), clock lệch, sampling quá mạnh, attacker dùng legitimate admin API hoặc hành vi thấp-chậm dưới threshold.

Vì vậy “không có alert” không chứng minh không có compromise.

Detection coverage nên được kiểm thử (test / 테스트) bằng simulated benign/malicious scenarios theo bất biến (invariant / 불변식), giống kiểm thử (test / 테스트) kiến trúc (architecture / 아키텍처) chứ không chỉ rà soát (review / 검토) quy tắc (rule / 규칙) cú pháp (syntax / 문법).

## 16. Adversarial pressure thay đổi economics của khả năng quan sát (observability / 관측 가능성)

Attacker có thể cố tạo log flood để che tín hiệu (signal / 신호) hoặc làm chuỗi xử lý (pipeline / 파이프라인) quá tải. Một hệ thống logging không bounded có thể tự trở thành availability rủi ro (risk / 위험).

Cần tỷ lệ (rate / 비율) limit, backpressure, priority classes và degradation chính sách (policy / 정책). Security-critical kiểm tra (audit / 감사) sự kiện (event / 이벤트) có thể cần guarantee khác gỡ lỗi (debug / 디버그) sự kiện (event / 이벤트).

Liên kết (connection / 연결) này nối trực tiếp với [queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 17. Detection chuỗi xử lý (pipeline / 파이프라인) cũng có data-quality bất biến (invariant / 불변식)

Nếu parser/lược đồ (schema / 스키마) evolution làm trường dữ liệu (field / 필드) `principal_id` biến mất ở 20% events, detector có thể silently mất coverage.

Do đó cần monitor:

```text
expected event rate
schema validity
field completeness
source freshness
pipeline lag
parse/drop rate
```

Bảo mật (security / 보안) detection không thể tin chuỗi xử lý (pipeline / 파이프라인) mà không quan sát chính chuỗi xử lý (pipeline / 파이프라인).

## 18. sự cố (incident / 인시던트) containment cần cắt năng lực (capability / 역량), không chỉ kill tiến trình (process / 프로세스)

Kill compromised tiến trình (process / 프로세스) có thể không đủ nếu đơn vị từ (token / 토큰) còn valid, role vẫn granted hoặc persistence cơ chế (mechanism / 메커니즘) còn tồn tại.

Containment phải xác định năng lực (capability / 역량) đồ thị (graph / 그래프) và cắt những edge quan trọng: revoke credential, disable principal, isolate tải công việc (workload / 워크로드), deny mạng (network / 네트워크) đường dẫn (path / 경로), freeze risky automation hoặc rotate keys.

Blast radius được giảm khi authority boundaries nhỏ từ trước.

## 19. khôi phục (recovery / 복구) cần chứng minh bất biến (invariant / 불변식) được phục hồi

“dịch vụ (service / 서비스) đã lên lại” không đồng nghĩa sự cố (incident / 인시던트) kết thúc. khôi phục (recovery / 복구) cần xác minh:

```text
unauthorized capability đã bị loại bỏ
credentials/policies đã ở state mới
compromised data/state đã được xử lý
telemetry coverage đã phục hồi
backlog/retry không tái kích hoạt hành vi cũ
```

Đây là điểm bảo mật (security / 보안) giao với độ tin cậy (reliability / 신뢰성).

## 20. sự cố (incident / 인시던트) học tập (learning / 학습) không nên dừng ở “human lỗi (error / 오류)”

Nếu một operator có thể vô tình cấp quyền quá rộng mà không guardrail, hệ thống (system / 시스템) thiết kế (design / 설계) đã cho phép thất bại (failure / 실패) đó.

Post-incident học tập (learning / 학습) nên hỏi giả định (assumption / 가정) nào sai, điều khiển (control / 제어) nào thiếu, bằng chứng (evidence / 증거) nào khó lấy, detection nào chậm và containment nào quá blast radius.

Kết quả có thể là policy-as-code, approval separation, safer default, better kiểm tra (audit / 감사) sự kiện (event / 이벤트) hoặc runbook; không phải chỉ thêm alert.

## 21. Privacy và retention là ràng buộc (constraint / 제약조건) thật

Bảo mật (security / 보안) telemetry thường chứa người dùng (user / 사용자) identifiers, IP, tài nguyên (resource / 자원) names hoặc yêu cầu (request / 요청) siêu dữ liệu (metadata / 메타데이터). Retain vô hạn để “forensic cho chắc” có privacy/compliance/chi phí (cost / 비용) rủi ro (risk / 위험).

Cần dữ liệu (data / 데이터) minimization, kiểm soát truy cập (access control / 접근 제어), retention tier và purpose limitation. bằng chứng (evidence / 증거) hữu ích không đồng nghĩa thu mọi payload nhạy cảm.

## 22. Worked example: dịch vụ (service / 서비스) account bị dùng sai phạm vi (scope / 범위)

Giả sử dịch vụ (service / 서비스) account của batch job bình thường chỉ đọc bucket A. Một misconfiguration cấp thêm quyền đọc bucket B chứa dữ liệu nhạy cảm. Sau đó tải công việc (workload / 워크로드) bắt đầu đọc B với volume bất thường.

Một detector tốt không chỉ trigger “bytes tăng”. Nó correlate:

```text
policy change
→ effective principal capability
→ first access to bucket B
→ data-read volume
→ outbound destination / downstream action
```

Investigation cần biết thay đổi (change / 변경) nào cấp authority, ai approve, đơn vị từ (token / 토큰) nào dùng, tài nguyên (resource / 자원) nào đọc và containment nào thu hồi năng lực (capability / 역량). Nếu chỉ có ứng dụng (application / 애플리케이션) truy cập (access / 접근) log không có policy-history bằng chứng (evidence / 증거), nguyên nhân gốc (root cause / 근본 원인) sẽ mơ hồ.

## 23. bằng chứng vận hành (production evidence / 운영 증거) checklist theo lập luận (reasoning / 추론) đường dẫn (path / 경로)

Khi điều tra, ưu tiên dựng timeline và đồ thị (graph / 그래프) thay vì dump tất cả logs. bằng chứng (evidence / 증거) hữu ích gồm định danh (identity / 식별자)/đơn vị từ (token / 토큰) siêu dữ liệu (metadata / 메타데이터) không chứa secret raw, chính sách (policy / 정책) phiên bản (version / 버전)/quyết định (decision / 결정), tài nguyên (resource / 자원)/đối tượng (object / 객체) ID, tiến trình (process / 프로세스)/tải công việc (workload / 워크로드) định danh (identity / 식별자), mạng (network / 네트워크) peer, yêu cầu (request / 요청)/dấu vết (trace / 추적)/session correlation, triển khai (deployment / 배포) phiên bản (version / 버전), clock bất định (uncertainty / 불확실성), audit-integrity status và containment actions.

Mục tiêu là trả lời được: **ai có authority gì, authority đó đến từ đâu, được dùng khi nào, đã tạo impact nào, và khi nào authority thực sự bị cắt**.

## 24. Kết nối sang các chapter khác

Detection/forensics nối với [security boundaries](./00_security_boundaries_attack_chains_and_exploitability.md), [OAuth/OIDC token lifecycle](./03_oauth_oidc_token_lifecycle_and_federation_threats.md), [secrets/KMS rotation](./06_secrets_kms_hsm_rotation_and_envelope_encryption.md), [test architecture và production verification](../../09_software_engineering/advanced/04_test_architecture_contract_mutation_property_and_production_verification.md) và [debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Mô hình tư duy (mental model / 사고 모델) cuối cùng: **bảo mật (security / 보안) bằng chứng (evidence / 증거) là một phân tán (distributed / 분산) trạng thái (state / 상태)/lịch sử (history / 이력) bài toán (problem / 문제). Detection chỉ mạnh khi định danh (identity / 식별자), authority, thời gian (time / 시간), provenance và chuỗi xử lý (pipeline / 파이프라인) độ tin cậy (reliability / 신뢰성) đều đủ để kiểm chứng hypothesis.**

> **Bàn giao:** Sau **24. Kết nối sang các chapter khác**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 security boundaries attack chains and exploitability](./00_security_boundaries_attack_chains_and_exploitability.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
