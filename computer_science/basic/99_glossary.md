# Glossary — Khoa học máy tính (computer science / 컴퓨터 과학) Việt / English / 한국어

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Computer Science glossary Việt/English/한국어**. Route tra cứu đi từ thuật ngữ → domain/chapter owner → connection layer → ví dụ và giới hạn, để glossary hỗ trợ đọc chứ không thay thế nội dung gốc.

Glossary này giúp nhận diện thuật ngữ khi đọc textbook, documentation, 기사 시험 hoặc trao đổi trong công ty Hàn Quốc. Nó không thay chapter giải thích concept; cột cuối dẫn tới ngữ cảnh (context / 맥락) đầy đủ.

| English term | 한국어 | Tiếng Việt / ý chính | Chapter |
|---|---|---|---|
| lớp trừu tượng (abstraction / 추상화) | 추상화 | Trừu tượng hóa: giữ đặc tả hợp đồng (contract / 계약) cần thiết, che hiện thực (implementation / 구현) | [Foundations](./00_computation_information/03_logic_state_abstraction_and_invariants.md) |
| thuật toán (algorithm / 알고리즘) | 알고리즘 | Procedure biến đầu vào (input / 입력) thành đầu ra (output / 출력) theo specification | [Algorithms](./01_algorithms_data_structures/00_algorithmic_thinking_and_correctness.md) |
| bất biến (invariant / 불변식) | 불변식 | thuộc tính (property / 속성) phải được bảo toàn qua trạng thái (state / 상태) transitions | [State](./00_computation_information/03_logic_state_abstraction_and_invariants.md) |
| Computability | 계산 가능성 | Khả năng bài toán (problem / 문제)/hàm (function / 함수) được thuật toán (algorithm / 알고리즘) tính | [Computability](./00_computation_information/04_computability_and_limits.md) |
| Undecidable | 결정 불가능 | Không có thuật toán (algorithm / 알고리즘) tổng quát luôn halt và quyết định đúng | [Computability](./00_computation_information/04_computability_and_limits.md) |
| Encoding | 인코딩 | Quy tắc map meaning/symbol ↔ biểu diễn (representation / 표현) | [Information](./00_computation_information/01_information_bits_and_encoding.md) |
| Floating điểm (point / 지점) | 부동소수점 | Biểu diễn số gần đúng bằng significand/exponent | [Representation](./00_computation_information/02_numbers_and_machine_representation.md) |
| Asymptotic độ phức tạp (complexity / 복잡도) | 점근적 복잡도 | Cách tài nguyên (resource / 자원) chi phí (cost / 비용) tăng khi đầu vào (input / 입력) quy mô (scale / 규모) | [Complexity](./01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) |
| Amortized phân tích (analysis / 분석) | 분할 상환 분석 | Average chi phí (cost / 비용) trên chuỗi operations dù một số thao tác (operation / 연산) đắt | [Complexity](./01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) |
| bảng băm (hash table / 해시 테이블) | 해시 테이블 | Key-value cấu trúc (structure / 구조) dùng băm (hash / 해시)→bucket/slot | [Hashing](./01_algorithms_data_structures/04_hashing_and_hash_tables.md) |
| B+ cây (tree / 트리) | B+ 트리 | High-fanout ordered chỉ mục (index / 인덱스) tối ưu page/khối (block / 블록) truy cập (access / 접근) | [Trees](./01_algorithms_data_structures/05_trees_heaps_and_search_structures.md) |
| động (dynamic / 동적) Programming | 동적 계획법 | trạng thái (state / 상태) + recurrence + reuse overlapping subproblems | [Strategies](./01_algorithms_data_structures/08_algorithmic_strategies.md) |
| KMP | KMP 문자열 검색 | String tìm kiếm (search / 검색) tái dùng prefix/suffix thông tin (information / 정보) | [Strings](./01_algorithms_data_structures/09_string_algorithms_and_text_indexing.md) |
| Rolling băm (hash / 해시) | 롤링 해시 | băm (hash / 해시) cập nhật nhanh cho sliding cửa sổ (window / 윈도우) | [Strings](./01_algorithms_data_structures/09_string_algorithms_and_text_indexing.md) |
| Randomized thuật toán (algorithm / 알고리즘) | 무작위 알고리즘 | thuật toán (algorithm / 알고리즘) dùng randomness như computational tài nguyên (resource / 자원) | [Randomized](./01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md) |
| Online thuật toán (algorithm / 알고리즘) | 온라인 알고리즘 | Quyết định khi chưa biết future đầu vào (input / 입력) | [Online](./01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md) |
| Approximation thuật toán (algorithm / 알고리즘) | 근사 알고리즘 | Nghiệm gần optimum với chất lượng (quality / 품질) guarantee | [Approximation](./01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md) |
| Reduction | 환원 | Biến bài toán (problem / 문제) A thành B để dùng solution/độ khó của B | [Complexity Theory](./01_algorithms_data_structures/11_complexity_reductions_and_np.md) |
| NP-complete | NP-완전 | Thuộc NP và NP-hard | [Complexity Theory](./01_algorithms_data_structures/11_complexity_reductions_and_np.md) |
| CPU | 중앙 처리 장치 | Bộ xử lý trung tâm | [CPU](./02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) |
| ISA | 명령어 집합 구조 | đặc tả hợp đồng (contract / 계약) instructions/registers giữa software và CPU | [CPU](./02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) |
| bộ nhớ đệm (cache / 캐시) line | 캐시 라인 | Đơn vị transfer/coherence trong CPU bộ nhớ đệm (cache / 캐시) | [Cache](./02_computer_architecture/02_memory_hierarchy_and_cache.md) |
| Locality | 지역성 | Tính cục bộ temporal/spatial của accesses | [Layout](./01_algorithms_data_structures/02_memory_models_and_data_layout.md) |
| DMA | 직접 메모리 접근 | thiết bị (device / 장치) transfer dữ liệu (data / 데이터) với RAM không CPU bản sao (copy / 복사) từng word | [I/O](./02_computer_architecture/03_io_interrupts_dma_and_devices.md) |
| Interrupt | 인터럽트 | sự kiện (event / 이벤트) chuyển CPU điều khiển (control / 제어) tới handler | [I/O](./02_computer_architecture/03_io_interrupts_dma_and_devices.md) |
| ABI | 응용 프로그램 이진 인터페이스 | nhị phân (binary / 이진) calling/bố cục (layout / 레이아웃)/link đặc tả hợp đồng (contract / 계약) | [ABI](./02_computer_architecture/04_machine_code_assembly_and_abi.md) |
| SIMD | 단일 명령 다중 데이터 | Một instruction xử lý nhiều lanes dữ liệu (data / 데이터) | [Parallel](./02_computer_architecture/05_parallel_computer_architecture.md) |
| NUMA | 비균일 메모리 접근 | bộ nhớ (memory / 메모리) truy cập (access / 접근) chi phí (cost / 비용) phụ thuộc location/nút (node / 노드) | [Parallel](./02_computer_architecture/05_parallel_computer_architecture.md) |
| SSD | 솔리드 스테이트 드라이브 | Persistent lưu trữ (storage / 저장소) dùng flash | [Storage Hardware](./02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) |
| NVMe | NVMe | lưu trữ (storage / 저장소) giao thức (protocol / 프로토콜)/giao diện (interface / 인터페이스) tối ưu PCIe parallel queues | [Storage Hardware](./02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) |
| CPI / IPC | 명령어당 사이클 / 사이클당 명령어 | Metrics thực thi (execution / 실행) efficiency của CPU | [Performance](./02_computer_architecture/07_performance_power_and_hardware_measurement.md) |
| Kernel | 커널 | Privileged cốt lõi (core / 핵심) của OS | [Kernel](./03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) |
| lời gọi hệ thống (system call / 시스템 호출) | 시스템 호출 | Controlled entry từ chế độ người dùng (user mode / 사용자 모드) vào kernel | [Kernel](./03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) |
| tiến trình (process / 프로세스) | 프로세스 | Isolated thực thi (execution / 실행)/tài nguyên (resource / 자원) ngữ cảnh (context / 맥락) | [Processes](./03_operating_systems/01_processes_threads_and_scheduling.md) |
| luồng thực thi (thread / 스레드) | 스레드 | Schedulable thực thi (execution / 실행) stream | [Processes](./03_operating_systems/01_processes_threads_and_scheduling.md) |
| Mutex | 뮤텍스 | Mutual-exclusion khóa (lock / 잠금) | [Concurrency](./03_operating_systems/02_concurrency_synchronization_and_deadlock.md) |
| Deadlock | 교착 상태 | Tasks chờ cycle không progress | [Concurrency](./03_operating_systems/02_concurrency_synchronization_and_deadlock.md) |
| Virtual bộ nhớ (memory / 메모리) | 가상 메모리 | Virtual-address ánh xạ (mapping / 매핑)/isolation lớp trừu tượng (abstraction / 추상화) | [Virtual Memory](./03_operating_systems/03_virtual_memory_and_address_spaces.md) |
| Page fault | 페이지 폴트 | Trap khi page ánh xạ (mapping / 매핑) cần kernel xử lý | [Virtual Memory](./03_operating_systems/03_virtual_memory_and_address_spaces.md) |
| bộ chứa (container / 컨테이너) | 컨테이너 | OS-level isolation dùng namespaces/cgroups | [Isolation](./03_operating_systems/05_privilege_isolation_and_virtualization.md) |
| IPC | 프로세스 간 통신 | Communication giữa processes | [IPC](./03_operating_systems/06_ipc_signals_pipes_and_shared_memory.md) |
| dùng chung (shared / 공유) bộ nhớ (memory / 메모리) | 공유 메모리 | bộ nhớ (memory / 메모리) pages map vào nhiều processes | [IPC](./03_operating_systems/06_ipc_signals_pipes_and_shared_memory.md) |
| Async I/O | 비동기 입출력 | I/O cho phép thực thi (execution / 실행) tiếp tục và nhận completion sau | [Async I/O](./03_operating_systems/07_boot_device_drivers_and_async_io.md) |
| ngữ nghĩa (semantics / 의미론) | 의미론 | Quy tắc meaning của ngôn ngữ (language / 언어)/program | [Semantics](./04_programming_languages/00_language_semantics_and_execution_models.md) |
| Garbage Collection | 가비지 컬렉션 | Reclaim unreachable bộ nhớ (memory / 메모리) tự động | [Memory](./04_programming_languages/01_types_values_references_and_memory.md) |
| Closure | 클로저 | hàm (function / 함수) + captured lexical môi trường (environment / 환경) | [Scope](./04_programming_languages/02_scope_closures_functions_and_control_flow.md) |
| trình biên dịch (compiler / 컴파일러) | 컴파일러 | Transform nguồn (source / 소스)/IR sang executable biểu diễn (representation / 표현) | [Compiler](./04_programming_languages/03_compilers_interpreters_vm_and_jit.md) |
| JIT | JIT 컴파일 | Compile mã (code / 코드) trong thời gian chạy (runtime / 런타임), thường dựa profiling | [Compiler](./04_programming_languages/03_compilers_interpreters_vm_and_jit.md) |
| hệ kiểu (type system / 타입 시스템) | 타입 시스템 | Rules phân loại values/operations để loại invalid programs | [Type Systems](./04_programming_languages/06_type_systems_generics_and_polymorphism.md) |
| Polymorphism | 다형성 | Một giao diện (interface / 인터페이스)/thao tác (operation / 연산) áp dụng nhiều types/forms | [Type Systems](./04_programming_languages/06_type_systems_generics_and_polymorphism.md) |
| AST | 추상 구문 트리 | Structured biểu diễn (representation / 표현) của cú pháp (syntax / 문법) | [Parsing](./04_programming_languages/07_parsing_ast_and_language_frontends.md) |
| SSA | 정적 단일 할당 | IR nơi mỗi variable phiên bản (version / 버전) assign một lần | [Parsing/IR](./04_programming_languages/07_parsing_ast_and_language_frontends.md) |
| Actor mô hình (model / 모델) | 액터 모델 | Private trạng thái (state / 상태) + asynchronous message communication | [Concurrency Models](./04_programming_languages/08_concurrency_models_and_memory_safety.md) |
| quyền sở hữu (ownership / 소유권) | 소유권 | Static/tài nguyên (resource / 자원) mô hình (model / 모델) quản lý thời gian tồn tại (lifetime / 수명) và aliasing | [Concurrency Models](./04_programming_languages/08_concurrency_models_and_memory_safety.md) |
| giao dịch (transaction / 트랜잭션) | 트랜잭션 | Atomic logical chuyển tiếp trạng thái (state transition / 상태 전이) trong DB | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| ACID | ACID | Atomicity, Consistency, Isolation, Durability | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| MVCC | 다중 버전 동시성 제어 | Multiple versions để isolate concurrent transactions | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| WAL | 선행 기록 로그 | Log-before-data cho khôi phục (recovery / 복구)/durability | [Storage](./05_data_databases/04_storage_logs_recovery_and_durability.md) |
| Relational algebra | 관계 대수 | Algebra của selection/projection/phép nối (join / 조인) trên relations | [SQL Semantics](./05_data_databases/05_relational_algebra_and_sql_semantics.md) |
| Cardinality estimation | 카디널리티 추정 | Ước lượng row count qua operators/predicates | [Optimizer](./05_data_databases/06_query_optimization_and_execution_plans.md) |
| OLTP | 온라인 트랜잭션 처리 | tải công việc (workload / 워크로드) nhiều transactions nhỏ, low độ trễ (latency / 지연 시간) | [Database Models](./05_data_databases/07_nosql_distributed_and_analytical_databases.md) |
| OLAP | 온라인 분석 처리 | Analytical scan/aggregate tải công việc (workload / 워크로드) | [Database Models](./05_data_databases/07_nosql_distributed_and_analytical_databases.md) |
| Packet | 패킷 | Network-layer dữ liệu (data / 데이터) đơn vị (unit / 단위) theo ngữ cảnh (context / 맥락) | [Network](./06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md) |
| TCP | 전송 제어 프로토콜 | Reliable ordered byte-stream vận chuyển (transport / 전송) | [Transport](./06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) |
| UDP | 사용자 데이터그램 프로토콜 | Datagram vận chuyển (transport / 전송) không built-in độ tin cậy (reliability / 신뢰성)/thứ tự (order / 순서) | [Transport](./06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) |
| DNS | 도메인 이름 시스템 | phân tán (distributed / 분산) naming hệ thống (system / 시스템) | [Web](./06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) |
| TLS | 전송 계층 보안 | Authenticated encrypted channel giao thức (protocol / 프로토콜) | [Web](./06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) |
| Consensus | 합의 | Nodes đồng thuận authoritative giá trị (value / 값)/log | [Distributed](./06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) |
| Socket | 소켓 | ứng dụng (application / 애플리케이션) endpoint handle cho communication | [Sockets](./06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) |
| NAT | 네트워크 주소 변환 | Rewrite mạng (network / 네트워크) address/cổng (port / 포트) mappings | [Sockets/Network Boundary](./06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) |
| VPN | 가상 사설망 | Secure/tunneled overlay mạng (network / 네트워크) | [Sockets/Network Boundary](./06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) |
| Autonomous hệ thống (system / 시스템) | 자율 시스템 | mạng (network / 네트워크) lĩnh vực (domain / 도메인) có routing chính sách (policy / 정책) riêng trên Internet | [Routing](./06_networks_distributed_systems/07_routing_protocols_and_the_internet.md) |
| BGP | 경계 경로 프로토콜 | Inter-AS path-vector routing giao thức (protocol / 프로토콜) | [Routing](./06_networks_distributed_systems/07_routing_protocols_and_the_internet.md) |
| QUIC | QUIC | Encrypted multiplexed vận chuyển (transport / 전송) chạy trên UDP substrate | [Modern Transport](./06_networks_distributed_systems/08_http2_http3_quic_and_modern_transport.md) |
| Authentication | 인증 | Xác minh định danh (identity / 식별자)/credential | [Identity](./07_security_reliability/02_identity_authentication_and_authorization.md) |
| Authorization | 인가 | Quyết định permission trên hành động (action / 동작)/tài nguyên (resource / 자원) | [Identity](./07_security_reliability/02_identity_authentication_and_authorization.md) |
| Threat mô hình (model / 모델) | 위협 모델 | Structured mô hình (model / 모델) về assets, attackers và attack paths | [Security](./07_security_reliability/00_threat_models_and_security_principles.md) |
| AEAD | 인증된 암호화 | Encryption + integrity/authentication | [Cryptography](./07_security_reliability/01_cryptography_foundations.md) |
| XSS | 크로스 사이트 스크립팅 | Untrusted dữ liệu (data / 데이터) bị trình duyệt (browser / 브라우저) diễn giải thành executable content | [Web Security](./07_security_reliability/06_web_application_security.md) |
| CSRF | 사이트 간 요청 위조 | Lợi dụng trình duyệt (browser / 브라우저) gửi credentials ngoài intent người dùng (user / 사용자) | [Web Security](./07_security_reliability/06_web_application_security.md) |
| KMS | 키 관리 시스템 | Managed hệ thống (system / 시스템) cho cryptographic key vòng đời (lifecycle / 생명주기) | [Keys/Secrets](./07_security_reliability/07_keys_secrets_certificates_and_secure_operations.md) |
| HSM | 하드웨어 보안 모듈 | Hardware ranh giới (boundary / 경계) bảo vệ/thực thi crypto keys | [Keys/Secrets](./07_security_reliability/07_keys_secrets_certificates_and_secure_operations.md) |
| SBOM | 소프트웨어 자재 명세서 | Inventory components trong software sản phẩm tạo ra (artifact / 산출물) | [Supply Chain](./07_security_reliability/08_supply_chain_and_secure_software_lifecycle.md) |
| khả năng quan sát (observability / 관측 가능성) | 관측 가능성 | Suy trạng thái nội bộ (internal state / 내부 상태) từ telemetry | [Reliability](./07_security_reliability/05_fault_tolerance_observability_and_reliability.md) |
| SLO | 서비스 수준 목표 | độ tin cậy (reliability / 신뢰성) mục tiêu (target / 대상) trên dịch vụ (service / 서비스) indicator | [Reliability](./07_security_reliability/05_fault_tolerance_observability_and_reliability.md) |
| Backpressure | 백프레셔 | Downstream sức chứa (capacity / 용량) tín hiệu (signal / 신호) ngược producer | [Queues](./08_software_systems/03_state_queues_backpressure_and_boundaries.md) |
| Idempotency | 멱등성 | Lặp logical thao tác (operation / 연산) không thay final tác động (effect / 효과) sau lần đầu | [Time/State](./08_software_systems/04_time_serialization_and_idempotency.md) |
| bộ nhớ đệm (cache / 캐시) stampede | 캐시 스탬피드 | Nhiều requests cùng miss/refresh hot bộ nhớ đệm (cache / 캐시) entry | [Caching](./08_software_systems/05_caching_load_balancing_and_cdns.md) |
| CDN | 콘텐츠 전송 네트워크 | phân tán (distributed / 분산) edge delivery/bộ nhớ đệm (cache / 캐시) mạng (network / 네트워크) | [Caching/CDN](./08_software_systems/05_caching_load_balancing_and_cdns.md) |
| sự kiện (event / 이벤트) sourcing | 이벤트 소싱 | Lưu trạng thái (state / 상태) changes dưới dạng ordered events | [Event Systems](./08_software_systems/06_event_driven_and_stream_processing.md) |
| Saga | 사가 패턴 | phân tán (distributed / 분산) workflow bằng cục bộ (local / 로컬) transactions + compensation | [System Boundaries](./08_software_systems/07_system_decomposition_services_and_boundaries.md) |
| yêu cầu (requirement / 요구사항) | 요구사항 | Observable need/ràng buộc (constraint / 제약조건) hệ thống (system / 시스템) phải đáp ứng | [Requirements](./09_software_engineering/00_requirements_specification_and_engineering_process.md) |
| ADR | 아키텍처 결정 기록 | bản ghi (record / 레코드) ngữ cảnh (context / 맥락)/options/quyết định (decision / 결정)/consequences | [Architecture](./09_software_engineering/01_software_architecture_and_design_reasoning.md) |
| đặc tả hợp đồng (contract / 계약) testing | 계약 테스트 | Verify producer-consumer giao diện (interface / 인터페이스) tính tương thích (compatibility / 호환성) | [Testing](./09_software_engineering/02_testing_quality_and_verification_strategy.md) |
| Continuous tích hợp (integration / 통합) | 지속적 통합 | Integrate frequently với automated bản dựng (build / 빌드)/kiểm thử (test / 테스트) phản hồi (feedback / 피드백) | [Delivery](./09_software_engineering/03_delivery_configuration_and_operations.md) |
| Technical debt | 기술 부채 | Future thay đổi (change / 변경) chi phí (cost / 비용) do intentional/accidental shortcuts/cấu trúc (structure / 구조) | [Maintenance](./09_software_engineering/04_maintenance_evolution_and_technical_debt.md) |
| tác nhân (agent / 에이전트) | 에이전트 | hệ thống (system / 시스템) nhận percepts và chọn actions theo mục tiêu (objective / 목표) | [AI](./10_ai_foundations/00_ai_problem_formulation_search_and_agents.md) |
| Heuristic | 휴리스틱 | Estimate/quy tắc (rule / 규칙) hướng tìm kiếm (search / 검색) hoặc solution | [AI Search](./10_ai_foundations/00_ai_problem_formulation_search_and_agents.md) |
| Bayesian mạng (network / 네트워크) | 베이지안 네트워크 | DAG biểu diễn probabilistic conditional dependencies | [AI Reasoning](./10_ai_foundations/01_knowledge_reasoning_and_probabilistic_inference.md) |
| Generalization | 일반화 | mô hình (model / 모델) hiệu năng (performance / 성능) trên unseen target-distribution dữ liệu (data / 데이터) | [ML](./10_ai_foundations/02_machine_learning_foundations.md) |
| Overfitting | 과적합 | Fit huấn luyện (training / 학습) idiosyncrasies nhưng generalize kém | [ML](./10_ai_foundations/02_machine_learning_foundations.md) |
| Backpropagation | 역전파 | Chain-rule độ dốc (gradient / 기울기) computation trên computation đồ thị (graph / 그래프) | [Neural Networks](./10_ai_foundations/03_neural_networks_and_representation_learning.md) |
| Embedding | 임베딩 | Learned véc-tơ (vector / 벡터) biểu diễn (representation / 표현) của discrete/thực thể (entity / 엔터티) dữ liệu (data / 데이터) | [Neural Networks](./10_ai_foundations/03_neural_networks_and_representation_learning.md) |
| Calibration | 캘리브레이션, 보정 | Mức predicted xác suất (probability / 확률) khớp observed frequency | [AI Evaluation](./10_ai_foundations/04_ai_evaluation_data_and_responsibility.md) |
| HCI | 인간-컴퓨터 상호작용 | Nghiên cứu tương tác (interaction / 상호작용) giữa human và computer các hệ thống (systems / 시스템들) | [HCI](./11_hci_graphics/00_hci_human_factors_and_interaction_models.md) |
| khả năng tiếp cận (accessibility / 접근성) | 접근성 | Khả năng sử dụng bởi diverse abilities/devices/contexts | [Accessibility](./11_hci_graphics/01_interface_design_accessibility_and_usability.md) |
| Rasterization | 래스터화 | Chuyển geometric primitives thành screen fragments/samples | [Graphics](./11_hci_graphics/02_computer_graphics_pipeline_and_geometry.md) |
| Shader | 셰이더 | GPU program xử lý vertices/fragments/graphics stages | [Graphics](./11_hci_graphics/02_computer_graphics_pipeline_and_geometry.md) |
| Aliasing | 에일리어싱 | Sampling sản phẩm tạo ra (artifact / 산출물) khi tín hiệu (signal / 신호) frequency vượt representable tỷ lệ (rate / 비율) | [Imaging](./11_hci_graphics/03_images_color_rasterization_and_rendering.md) |
| Frame thời gian (time / 시간) | 프레임 시간 | Thời gian cần tạo một frame | [Interactive Systems](./11_hci_graphics/04_multimedia_animation_and_interactive_systems.md) |
| Privacy | 개인정보 보호, 프라이버시 | điều khiển (control / 제어)/ngữ cảnh (context / 맥락) của personal thông tin (information / 정보) vòng đời (lifecycle / 생명주기) | [Ethics](./12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md) |
| dữ liệu (data / 데이터) provenance | 데이터 출처/계보 | Nguồn và transformation lịch sử (history / 이력) của dữ liệu (data / 데이터) | [Governance](./12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md) |
| Open-source license | 오픈소스 라이선스 | Rights/obligations cho use/modify/distribute nguồn (source / 소스) | [Law/Licensing](./12_society_ethics_profession/02_software_law_licenses_and_intellectual_property.md) |
| Digital divide | 디지털 격차 | Chênh lệch truy cập (access / 접근)/năng lực (capability / 역량) với computing hạ tầng (infrastructure / 인프라) | [Society](./12_society_ethics_profession/03_sustainability_accessibility_and_social_infrastructure.md) |

> **Bàn giao:** Sau **Glossary — Khoa học máy tính (computer science / 컴퓨터 과학) Việt / English / 한국어**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
