# Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Basic Foundations

> **Mạch đọc:** [README](./README.md) là owner của **Coverage audit cho Computer Science basic foundations**. Route kiểm tra đi từ chapter inventory → README ownership/links → connection coverage → audit scripts và warnings, để số liệu coverage phản ánh đúng cấu trúc hiện hành.

Tài liệu này kiểm tra coverage và conceptual boundaries để `computer_science/basic/` không trở thành collection chapter ngẫu nhiên. Sau vòng comprehensive expansion, foundation thư viện (library / 라이브러리) có **100 topic chapters** trong **14 nhóm conceptual**, cộng `README.md`, glossary Việt–Anh–Hàn và kiểm tra (audit / 감사) này.

## 1. Computation & thông tin (information / 정보) — 5 chapters

Đã cover computation/chuyển tiếp trạng thái (state transition / 상태 전이), thông tin (information / 정보)/encoding, nhị phân (binary / 이진)/hex/integer/floating điểm (point / 지점), lô-gic (logic / 논리)/invariants/lớp trừu tượng (abstraction / 추상화) và computability/undecidability. Mathematical proof, Boolean algebra và thông tin (information / 정보) lý thuyết (theory / 이론) sâu hơn cross-reference sang `mathematics/`.

> **Chuyển mạch:** Trong **Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Basic Foundations**, **1. Computation & thông tin (information / 정보) — 5 chapters** nêu điều cần giải thích; **2. Algorithms & dữ liệu (data / 데이터) Structures — 12 chapters** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Computer kiến trúc (architecture / 아키텍처) — 8 chapters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Algorithms & dữ liệu (data / 데이터) Structures — 12 chapters

Đã cover specification/tính đúng đắn (correctness / 정확성)/termination; asymptotic, amortized, worst/average/lower bounds; bộ nhớ (memory / 메모리) locality/bố cục (layout / 레이아웃); arrays/lists/stacks/queues/deques; hashing; trees/B-tree/heaps/tries; graphs; sorting/tìm kiếm (search / 검색)/selection; recursion/divide-and-conquer/greedy/backtracking/DP; string algorithms/KMP/rolling băm (hash / 해시)/suffix structures; randomized/approximation/online/streaming algorithms; reductions, P/NP/NP-hard/NP-complete và parameterized-complexity intuition.

Các chapter này đóng vai trò **foundation DSA** cho các lĩnh vực (domain / 도메인) khác. Những cấu trúc, proofs, variants và hiện thực (implementation / 구현) chuyên sâu hơn được tách sang thư viện (library / 라이브러리) dữ liệu (data / 데이터) Structures & Algorithms advanced thay vì tiếp tục phình `basic/`.

> **Chuyển mạch:** Ở chặng này của **Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Basic Foundations**, **2. Algorithms & dữ liệu (data / 데이터) Structures — 12 chapters** nêu điều cần giải thích; **3. Computer kiến trúc (architecture / 아키텍처) — 8 chapters** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Operating các hệ thống (systems / 시스템들) — 8 chapters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Computer kiến trúc (architecture / 아키텍처) — 8 chapters

Đã cover digital lô-gic (logic / 논리)/sequential circuits; CPU/ISA/instruction cycle; chuỗi xử lý (pipeline / 파이프라인)/out-of-order; bộ nhớ đệm (cache / 캐시)/TLB/coherence; I/O/interrupt/DMA; assembly/ABI; multicore/SIMD/GPU/NUMA/Amdahl; SSD/HDD/NVMe/FTL/persistence; hiệu năng (performance / 성능) equations, power, benchmarking và roofline intuition.

> **Chuyển mạch:** **Computer Architecture** giải thích resource và execution substrate; **Operating Systems** quản lý process, memory và I/O, rồi **Programming Languages/Runtime** đặt semantics lên substrate đó.

## 4. Operating các hệ thống (systems / 시스템들) — 8 chapters

Đã cover kernel/người dùng (user / 사용자) privilege, syscalls, processes/threads/scheduling/ngữ cảnh (context / 맥락) switching, synchronization/atomics/bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)/deadlock, virtual bộ nhớ (memory / 메모리)/TLB/COW/mmap, filesystem/page bộ nhớ đệm (cache / 캐시)/journaling, containers/VM/namespaces/cgroups, IPC/signals/pipes/dùng chung (shared / 공유) bộ nhớ (memory / 메모리), boot/drivers/MMIO/DMA và blocking/non-blocking/async I/O.

> **Chuyển mạch:** **Programming Languages/Runtime** biến substrate thành type và control-flow contract; **Data/Databases** lưu, truy vấn và bảo toàn state theo contract đó.

## 5. Programming Languages & thời gian chạy (runtime / 런타임) — 9 chapters

Đã cover cú pháp (syntax / 문법)/ngữ nghĩa (semantics / 의미론)/thực thi (execution / 실행) các mô hình (models / 모델들); values/references/aliasing/bộ nhớ (memory / 메모리) management; phạm vi (scope / 범위)/closure/điều khiển (control / 제어)/async; trình biên dịch (compiler / 컴파일러)/IR/JIT/thời gian chạy (runtime / 런타임); programming paradigms; lỗi (error / 오류)/tài nguyên (resource / 자원) an toàn (safety / 안전); kiểu (type / 타입) các hệ thống (systems / 시스템들)/subtyping/generics/variance/ADTs; lexer/parser/AST/ngữ nghĩa (semantic / 의미적) phân tích (analysis / 분석)/SSA; threads/actors/CSP/structured tính đồng thời (concurrency / 동시성)/quyền sở hữu (ownership / 소유권)/bộ nhớ (memory / 메모리) an toàn (safety / 안전).

> **Chuyển mạch:** Ở chặng này của **Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Basic Foundations**, **5. Programming Languages & thời gian chạy (runtime / 런타임) — 9 chapters** nêu điều cần giải thích; **6. dữ liệu (data / 데이터) & Databases — 8 chapters** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. Networks & phân tán (distributed / 분산) các hệ thống (systems / 시스템들) — 9 chapters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. dữ liệu (data / 데이터) & Databases — 8 chapters

Đã cover dữ liệu (data / 데이터) các mô hình (models / 모델들); relational mô hình (model / 모델)/keys/FD/normalization/NULL; transactions ACID/isolation anomalies/locks/MVCC/serializability; indexes/B+ cây (tree / 트리)/băm (hash / 해시)/truy vấn (query / 쿼리) thực thi (execution / 실행); pages/buffer pool/WAL/khôi phục (recovery / 복구)/LSM; relational algebra/SQL logical ngữ nghĩa (semantics / 의미론)/cửa sổ (window / 윈도우)/grouping; cardinality estimation/phép nối (join / 조인) thứ tự (ordering / 순서)/truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화); NoSQL các mô hình (models / 모델들), shard keys, replication, OLTP/OLAP, row-vs-column stores, warehouse/lake/lakehouse.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Basic Foundations**, **6. dữ liệu (data / 데이터) & Databases — 8 chapters** nêu điều cần giải thích; **7. Networks & phân tán (distributed / 분산) các hệ thống (systems / 시스템들) — 9 chapters** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. bảo mật (security / 보안) & độ tin cậy (reliability / 신뢰성) — 9 chapters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Networks & phân tán (distributed / 분산) các hệ thống (systems / 시스템들) — 9 chapters

Đã cover layering/encapsulation/packets; Ethernet/ARP/IP/subnet/routing/NAT; TCP/UDP/luồng (flow / 흐름)/congestion/BDP; DNS/HTTP/TLS; partial thất bại (failure / 실패)/thời gian (time / 시간)/causality/consistency/CAP; replication/sharding/quorum/consensus/Raft intuition; socket APIs, IPv6, firewall/VPN/MTU; forwarding vs routing, OSPF/BGP/AS/anycast; HTTP/2 framing, HTTP/3/QUIC và hiện đại (modern / 현대적) vận chuyển (transport / 전송) trade-offs.

> **Chuyển mạch:** **Networks/Distributed Systems** đặt boundary và failure semantics; **Security/Reliability** kiểm soát authority, trust và recovery; **Software Systems** kết hợp chúng thành service.

## 8. bảo mật (security / 보안) & độ tin cậy (reliability / 신뢰성) — 9 chapters

Đã cover threat modeling/trust/least privilege; cryptographic primitives/password hashing/AEAD/PKI; định danh (identity / 식별자)/authentication/authorization/session/OAuth-OIDC intuition; bộ nhớ (memory / 메모리)/injection vulnerabilities; testing/static/formal/fuzz/debugging; thử lại (retry / 재시도)/hết thời gian chờ (timeout / 타임아웃)/circuit breaker/bulkhead/khả năng quan sát (observability / 관측 가능성)/SLI-SLO; SOP/CORS/XSS/CSRF/SSRF/session web bảo mật (security / 보안); keys/secrets/certificates/KMS/HSM/rotation; phụ thuộc (dependency / 의존성)/bản dựng (build / 빌드) provenance/SBOM/CI supply-chain bảo mật (security / 보안).

> **Chuyển mạch:** **Software Systems** cho thấy runtime và service boundary; **Software Engineering** quản lý change, testing và delivery của các boundary đó.

## 9. Software các hệ thống (systems / 시스템들) — 8 chapters

Đã cover modularity/API contracts; Git/bản dựng (build / 빌드)/link/gói (package / 패키지)/reproducibility; độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량)/queueing/sức chứa (capacity / 용량)/pools/scaling; trạng thái (state / 상태) placement/queues/backpressure; clocks/serialization/lược đồ (schema / 스키마) evolution/idempotency; caching/TTL/stampede/tải (load / 로드) balancing/CDN/consistent hashing; sự kiện (event / 이벤트)/command/log/stream delivery/thứ tự (order / 순서)/sự kiện (event / 이벤트) thời gian (time / 시간); monolith/services/dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권)/saga/gateway/mesh/Conway's Law.

> **Chuyển mạch:** **Software Engineering** cung cấp lifecycle và evidence; **AI Foundations** áp dụng chúng cho data, model, inference và evaluation.

## 10. Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) — 5 chapters

Đã cover requirements/specification/acceptance criteria/traceability/risk-driven tiến trình (process / 프로세스); kiến trúc (architecture / 아키텍처) chất lượng (quality / 품질) attributes, coupling/cohesion, ADR, thông tin (information / 정보) hiding và patterns-by-context; đơn vị (unit / 단위)/tích hợp (integration / 통합)/E2E/đặc tả hợp đồng (contract / 계약)/thuộc tính (property / 속성)/fuzz/mutation/static xác minh (verification / 확인) chiến lược (strategy / 전략); CI/CD/cấu hình (config / 설정)/tính năng (feature / 기능) flags/triển khai (deployment / 배포)/cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션)/IaC/runbooks; maintenance/refactoring/legacy/technical debt/dữ liệu (data / 데이터) evolution/kiến thức (knowledge / 지식) debt/sunsetting.

> **Chuyển mạch:** **AI Foundations** làm rõ representation và decision; **HCI/Graphics** chuyển chúng thành perception, interaction và rendering boundary.

## 11. AI Foundations — 5 chapters

Đã cover tác nhân (agent / 에이전트)/bài toán (problem / 문제) formulation/state-space tìm kiếm (search / 검색)/A*/minimax/planning; lô-gic (logic / 논리)/kiến thức (knowledge / 지식) biểu diễn (representation / 표현)/Bayesian networks/approximate suy luận (inference / 추론)/nhân quả (causal / 인과적) distinction; supervised/unsupervised/self-supervised học tập (learning / 학습), mất mát (loss / 손실)/generalization/overfit/leakage/shift; neural networks/backprop/SGD/CNN/attention/transformers/embeddings; evaluation metrics/calibration/subgroups/human-in-loop/dữ liệu (data / 데이터) provenance/robustness.

AI specialization như NLP, computer vision, reinforcement học tập (learning / 학습), robotics, foundation-model các hệ thống (systems / 시스템들) và MLOps đủ lớn để thành libraries riêng; chapter hiện tại cung cấp prerequisites và vocabulary để đi vào chúng.

> **Chuyển mạch:** **HCI/Graphics** cho biết hệ thống được cảm nhận và dùng thế nào; **Computing, Society, Ethics & Profession** đặt impact và responsibility vào context xã hội.

## 12. HCI & Computer Graphics — 5 chapters

Đã cover mô hình tư duy (mental models / 사고 모델들)/phản hồi (feedback / 피드백)/human factors/Fitts/Hick/errors; giao diện (interface / 인터페이스) thông tin (information / 정보) kiến trúc (architecture / 아키텍처)/khả năng tiếp cận (accessibility / 접근성)/keyboard/focus/color/responsive/người dùng (user / 사용자) research; graphics coordinate spaces/matrices/projection/raster chuỗi xử lý (pipeline / 파이프라인)/shaders/độ sâu (depth / 깊이); sampling/color spaces/gamma/alpha/textures/raster-vs-ray-tracing/compression; multimedia frame timing/game vòng lặp (loop / 루프)/audio/video/synchronization/real-time hành vi (behavior / 동작).

> **Chuyển mạch:** **Computing/Society/Ethics** nêu boundary của use và harm; **Cross-domain Connections** nối các invariant về đúng owner ở domain khác.

## 13. Computing, Society, Ethics & Profession — 4 chapters

Đã cover privacy/dữ liệu (data / 데이터) minimization/consent/purpose/professional responsibility/dual use; dữ liệu (data / 데이터) provenance/measurement-sampling-label độ lệch (bias / 편향)/fairness/phản hồi (feedback / 피드백) loops/quản trị (governance / 거버넌스); copyright/open-source licenses/patent/trademark/dữ liệu (data / 데이터) licenses/compliance; năng lượng (energy / 에너지)/embodied chi phí (cost / 비용)/e-waste/digital divide/khả năng tiếp cận (accessibility / 접근성)/resilience/nền tảng (platform / 플랫폼) concentration.

Legal specifics thay đổi theo jurisdiction/thời gian (time / 시간) nên chapter law chỉ cung cấp conceptual map, không thay hiện tại (current / 현재) legal research/advice.

> **Chuyển mạch:** **Cross-domain Connections** ghi đường quay lại canonical owner; **Coverage đối chiếu curriculum CS rộng** kiểm tra gap mà không biến gap thành duplicate.

## 14. Cross-domain Connections — 5 chapters

Đã có end-to-end nguồn (source / 소스)→trình biên dịch (compiler / 컴파일러)/JIT→CPU; trình duyệt (browser / 브라우저)→DNS/TLS/mạng (network / 네트워크)→máy chủ (server / 서버)→DB; dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기) register→bộ nhớ đệm (cache / 캐시)→RAM→disk→mạng (network / 네트워크); recurring trade-offs; lớp trừu tượng (abstraction / 추상화)/leaky-abstraction mô hình (model / 모델).

Các chapter mới cross-link trực tiếp vào những liên kết (connection / 연결) này thay vì duplicate toàn bộ content.

> **Chuyển mạch:** Ở chặng này của **Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Basic Foundations**, **14. Cross-domain Connections — 5 chapters** đã nêu tiêu chí phân biệt, còn **Coverage đối chiếu với một curriculum CS rộng** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Các lĩnh vực (domain / 도메인) cố ý không nhồi vào Basic thư viện (library / 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coverage đối chiếu với một curriculum CS rộng

Foundation thư viện (library / 라이브러리) hiện đã có coverage cho các kiến thức (knowledge / 지식) areas lớn thường xuất hiện trong chương trình Khoa học máy tính (computer science / 컴퓨터 과학): algorithmic foundations, kiến trúc (architecture / 아키텍처), operating các hệ thống (systems / 시스템들), programming languages, dữ liệu (data / 데이터) management, networking/phân tán (distributed / 분산) computing, bảo mật (security / 보안), software development/các hệ thống (systems / 시스템들), kỹ nghệ phần mềm (software engineering / 소프트웨어 공학), AI, HCI, graphics/interactive các hệ thống (systems / 시스템들) và xã hội (social / 사회적)/professional issues. Mathematical/statistical foundations nằm trong dedicated `mathematics/` thư viện (library / 라이브러리) và được cross-reference thay vì bản sao (copy / 복사).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Coverage kiểm tra (audit / 감사) — Khoa học máy tính (computer science / 컴퓨터 과학) Basic Foundations**, **Coverage đối chiếu với một curriculum CS rộng** đã nêu tiêu chí phân biệt, còn **Các lĩnh vực (domain / 도메인) cố ý không nhồi vào Basic thư viện (library / 라이브러리)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Chất lượng (quality / 품질) kiểm tra (audit / 감사) criteria** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các lĩnh vực (domain / 도메인) cố ý không nhồi vào Basic thư viện (library / 라이브러리)

Các lĩnh vực (domain / 도메인) sau đủ lớn để tạo thư viện kiến thức (knowledge library / 지식 라이브러리) riêng: advanced dữ liệu (data / 데이터) Structures & Algorithms; advanced trình biên dịch (compiler / 컴파일러) construction/backend tối ưu hóa (optimization / 최적화); kernel internals/device-driver programming chuyên sâu; formal methods/mô hình (model / 모델) checking/theorem proving chuyên sâu; cryptographic giao thức (protocol / 프로토콜) proofs; robotics; NLP/CV chuyên sâu; MLOps/foundation-model kỹ thuật (engineering / 엔지니어링); cloud-provider/kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링); computer graphics engine/game engine chuyên sâu; quantum computing; scientific/HPC computing; embedded/real-time hardware chuyên sâu.

Việc không tạo 20–50 files cho mỗi specialization là **conceptual ranh giới (boundary / 경계)**, không phải missing foundational topic.

> **Chuyển mạch:** **Các domain cố ý không nhồi vào Basic** giữ boundary của thư viện; **Quality criteria** kiểm tra boundary đó, rồi **Maintenance rules** bảo vệ nó qua các lần cập nhật.

## Chất lượng (quality / 품질) kiểm tra (audit / 감사) criteria

Một chapter chỉ được coi là đạt khi có bài toán (problem / 문제)/phenomenon trước definition, giải thích cơ chế (mechanism / 메커니즘) và các giả định (assumptions / 가정들), examples/counterexamples hoặc trường hợp biên (edge case / 경계 사례) phù hợp, terminology English + Korean khi hữu ích, mô hình tư duy (mental model / 사고 모델), misconceptions và cross-reference. Prose phải là phần chính; bullet chỉ dùng cho danh sách (list / 목록) tự nhiên.

Vòng comprehensive expansion tập trung xử lý ba loại gap: concept có mặt nhưng quá implicit; foundational lĩnh vực (domain / 도메인) hoàn toàn chưa có; và môi trường vận hành (production / 운영 환경) cơ chế (mechanism / 메커니즘) thường bị khung phần mềm (framework / 프레임워크)/API che khuất. Kết quả là thư viện (library / 라이브러리) tăng từ 59 lên **100 topic chapters** mà vẫn giữ ranh giới (boundary / 경계) theo mô hình tư duy (mental model / 사고 모델) thay vì chia tệp (file / 파일) theo độ khó.

> **Chuyển mạch:** **Maintenance rules** khép coverage bằng owner, link và evidence; phần chuyên sâu quay về chapter canonical thay vì mở rộng mù.

## Maintenance quy tắc (rule / 규칙)

Khi mở rộng tiếp, không thêm chapter chỉ vì technology phổ biến. Chỉ thêm khi topic có mô hình tư duy (mental model / 사고 모델) riêng, là phụ thuộc (dependency / 의존성) quan trọng cho nhiều domains, hoặc một specialization mới được tách thành thư viện (library / 라이브러리) riêng. `computer_science/basic/` phải tiếp tục trả lời câu hỏi: **“Computation và software các hệ thống (systems / 시스템들) hoạt động từ thông tin (information / 정보) tới human/societal impact như thế nào, và các ràng buộc (constraints / 제약조건들)/trade-offs nào lặp lại xuyên các layers?”**

Các nội dung advanced không nên được bản sao (copy / 복사) ngược vào `basic/`; `basic/` chỉ cung cấp prerequisite, mô hình tư duy (mental model / 사고 모델) và cầu nối (bridge / 브리지) cần thiết rồi cross-reference sang thư viện (library / 라이브러리) chuyên sâu.

> **Bàn giao:** Sau **Maintenance quy tắc (rule / 규칙)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
