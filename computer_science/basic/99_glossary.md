# Glossary — Computer Science Việt / English / 한국어

Glossary này giúp nhận diện thuật ngữ khi đọc textbook, documentation, 기사 시험 hoặc trao đổi trong công ty Hàn Quốc. Nó không thay chapter giải thích concept; cột cuối dẫn tới context đầy đủ.

| English term | 한국어 | Tiếng Việt / ý chính | Chapter |
|---|---|---|---|
| Abstraction | 추상화 | Trừu tượng hóa: giữ contract cần thiết, che implementation | [Foundations](./00_computation_information/03_logic_state_abstraction_and_invariants.md) |
| Algorithm | 알고리즘 | Procedure biến input thành output theo specification | [Algorithms](./01_algorithms_data_structures/00_algorithmic_thinking_and_correctness.md) |
| Invariant | 불변식 | Property phải được bảo toàn qua state transitions | [State](./00_computation_information/03_logic_state_abstraction_and_invariants.md) |
| Computability | 계산 가능성 | Khả năng problem/function được algorithm tính | [Computability](./00_computation_information/04_computability_and_limits.md) |
| Undecidable | 결정 불가능 | Không có algorithm tổng quát luôn halt và quyết định đúng | [Computability](./00_computation_information/04_computability_and_limits.md) |
| Encoding | 인코딩 | Quy tắc map meaning/symbol ↔ representation | [Information](./00_computation_information/01_information_bits_and_encoding.md) |
| Floating point | 부동소수점 | Biểu diễn số gần đúng bằng significand/exponent | [Representation](./00_computation_information/02_numbers_and_machine_representation.md) |
| Asymptotic complexity | 점근적 복잡도 | Cách resource cost tăng khi input scale | [Complexity](./01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) |
| Amortized analysis | 분할 상환 분석 | Average cost trên chuỗi operations dù một số operation đắt | [Complexity](./01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) |
| Hash table | 해시 테이블 | Key-value structure dùng hash→bucket/slot | [Hashing](./01_algorithms_data_structures/04_hashing_and_hash_tables.md) |
| B+ tree | B+ 트리 | High-fanout ordered index tối ưu page/block access | [Trees](./01_algorithms_data_structures/05_trees_heaps_and_search_structures.md) |
| Dynamic Programming | 동적 계획법 | State + recurrence + reuse overlapping subproblems | [Strategies](./01_algorithms_data_structures/08_algorithmic_strategies.md) |
| KMP | KMP 문자열 검색 | String search tái dùng prefix/suffix information | [Strings](./01_algorithms_data_structures/09_string_algorithms_and_text_indexing.md) |
| Rolling hash | 롤링 해시 | Hash cập nhật nhanh cho sliding window | [Strings](./01_algorithms_data_structures/09_string_algorithms_and_text_indexing.md) |
| Randomized algorithm | 무작위 알고리즘 | Algorithm dùng randomness như computational resource | [Randomized](./01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md) |
| Online algorithm | 온라인 알고리즘 | Quyết định khi chưa biết future input | [Online](./01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md) |
| Approximation algorithm | 근사 알고리즘 | Nghiệm gần optimum với quality guarantee | [Approximation](./01_algorithms_data_structures/10_randomized_approximation_and_online_algorithms.md) |
| Reduction | 환원 | Biến problem A thành B để dùng solution/độ khó của B | [Complexity Theory](./01_algorithms_data_structures/11_complexity_reductions_and_np.md) |
| NP-complete | NP-완전 | Thuộc NP và NP-hard | [Complexity Theory](./01_algorithms_data_structures/11_complexity_reductions_and_np.md) |
| CPU | 중앙 처리 장치 | Bộ xử lý trung tâm | [CPU](./02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) |
| ISA | 명령어 집합 구조 | Contract instructions/registers giữa software và CPU | [CPU](./02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) |
| Cache line | 캐시 라인 | Đơn vị transfer/coherence trong CPU cache | [Cache](./02_computer_architecture/02_memory_hierarchy_and_cache.md) |
| Locality | 지역성 | Tính cục bộ temporal/spatial của accesses | [Layout](./01_algorithms_data_structures/02_memory_models_and_data_layout.md) |
| DMA | 직접 메모리 접근 | Device transfer data với RAM không CPU copy từng word | [I/O](./02_computer_architecture/03_io_interrupts_dma_and_devices.md) |
| Interrupt | 인터럽트 | Event chuyển CPU control tới handler | [I/O](./02_computer_architecture/03_io_interrupts_dma_and_devices.md) |
| ABI | 응용 프로그램 이진 인터페이스 | Binary calling/layout/link contract | [ABI](./02_computer_architecture/04_machine_code_assembly_and_abi.md) |
| SIMD | 단일 명령 다중 데이터 | Một instruction xử lý nhiều lanes data | [Parallel](./02_computer_architecture/05_parallel_computer_architecture.md) |
| NUMA | 비균일 메모리 접근 | Memory access cost phụ thuộc location/node | [Parallel](./02_computer_architecture/05_parallel_computer_architecture.md) |
| SSD | 솔리드 스테이트 드라이브 | Persistent storage dùng flash | [Storage Hardware](./02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) |
| NVMe | NVMe | Storage protocol/interface tối ưu PCIe parallel queues | [Storage Hardware](./02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) |
| CPI / IPC | 명령어당 사이클 / 사이클당 명령어 | Metrics execution efficiency của CPU | [Performance](./02_computer_architecture/07_performance_power_and_hardware_measurement.md) |
| Kernel | 커널 | Privileged core của OS | [Kernel](./03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) |
| System call | 시스템 호출 | Controlled entry từ user mode vào kernel | [Kernel](./03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) |
| Process | 프로세스 | Isolated execution/resource context | [Processes](./03_operating_systems/01_processes_threads_and_scheduling.md) |
| Thread | 스레드 | Schedulable execution stream | [Processes](./03_operating_systems/01_processes_threads_and_scheduling.md) |
| Mutex | 뮤텍스 | Mutual-exclusion lock | [Concurrency](./03_operating_systems/02_concurrency_synchronization_and_deadlock.md) |
| Deadlock | 교착 상태 | Tasks chờ cycle không progress | [Concurrency](./03_operating_systems/02_concurrency_synchronization_and_deadlock.md) |
| Virtual memory | 가상 메모리 | Virtual-address mapping/isolation abstraction | [Virtual Memory](./03_operating_systems/03_virtual_memory_and_address_spaces.md) |
| Page fault | 페이지 폴트 | Trap khi page mapping cần kernel xử lý | [Virtual Memory](./03_operating_systems/03_virtual_memory_and_address_spaces.md) |
| Container | 컨테이너 | OS-level isolation dùng namespaces/cgroups | [Isolation](./03_operating_systems/05_privilege_isolation_and_virtualization.md) |
| IPC | 프로세스 간 통신 | Communication giữa processes | [IPC](./03_operating_systems/06_ipc_signals_pipes_and_shared_memory.md) |
| Shared memory | 공유 메모리 | Memory pages map vào nhiều processes | [IPC](./03_operating_systems/06_ipc_signals_pipes_and_shared_memory.md) |
| Async I/O | 비동기 입출력 | I/O cho phép execution tiếp tục và nhận completion sau | [Async I/O](./03_operating_systems/07_boot_device_drivers_and_async_io.md) |
| Semantics | 의미론 | Quy tắc meaning của language/program | [Semantics](./04_programming_languages/00_language_semantics_and_execution_models.md) |
| Garbage Collection | 가비지 컬렉션 | Reclaim unreachable memory tự động | [Memory](./04_programming_languages/01_types_values_references_and_memory.md) |
| Closure | 클로저 | Function + captured lexical environment | [Scope](./04_programming_languages/02_scope_closures_functions_and_control_flow.md) |
| Compiler | 컴파일러 | Transform source/IR sang executable representation | [Compiler](./04_programming_languages/03_compilers_interpreters_vm_and_jit.md) |
| JIT | JIT 컴파일 | Compile code trong runtime, thường dựa profiling | [Compiler](./04_programming_languages/03_compilers_interpreters_vm_and_jit.md) |
| Type system | 타입 시스템 | Rules phân loại values/operations để loại invalid programs | [Type Systems](./04_programming_languages/06_type_systems_generics_and_polymorphism.md) |
| Polymorphism | 다형성 | Một interface/operation áp dụng nhiều types/forms | [Type Systems](./04_programming_languages/06_type_systems_generics_and_polymorphism.md) |
| AST | 추상 구문 트리 | Structured representation của syntax | [Parsing](./04_programming_languages/07_parsing_ast_and_language_frontends.md) |
| SSA | 정적 단일 할당 | IR nơi mỗi variable version assign một lần | [Parsing/IR](./04_programming_languages/07_parsing_ast_and_language_frontends.md) |
| Actor model | 액터 모델 | Private state + asynchronous message communication | [Concurrency Models](./04_programming_languages/08_concurrency_models_and_memory_safety.md) |
| Ownership | 소유권 | Static/resource model quản lý lifetime và aliasing | [Concurrency Models](./04_programming_languages/08_concurrency_models_and_memory_safety.md) |
| Transaction | 트랜잭션 | Atomic logical state transition trong DB | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| ACID | ACID | Atomicity, Consistency, Isolation, Durability | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| MVCC | 다중 버전 동시성 제어 | Multiple versions để isolate concurrent transactions | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| WAL | 선행 기록 로그 | Log-before-data cho recovery/durability | [Storage](./05_data_databases/04_storage_logs_recovery_and_durability.md) |
| Relational algebra | 관계 대수 | Algebra của selection/projection/join trên relations | [SQL Semantics](./05_data_databases/05_relational_algebra_and_sql_semantics.md) |
| Cardinality estimation | 카디널리티 추정 | Ước lượng row count qua operators/predicates | [Optimizer](./05_data_databases/06_query_optimization_and_execution_plans.md) |
| OLTP | 온라인 트랜잭션 처리 | Workload nhiều transactions nhỏ, low latency | [Database Models](./05_data_databases/07_nosql_distributed_and_analytical_databases.md) |
| OLAP | 온라인 분석 처리 | Analytical scan/aggregate workload | [Database Models](./05_data_databases/07_nosql_distributed_and_analytical_databases.md) |
| Packet | 패킷 | Network-layer data unit theo context | [Network](./06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md) |
| TCP | 전송 제어 프로토콜 | Reliable ordered byte-stream transport | [Transport](./06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) |
| UDP | 사용자 데이터그램 프로토콜 | Datagram transport không built-in reliability/order | [Transport](./06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) |
| DNS | 도메인 이름 시스템 | Distributed naming system | [Web](./06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) |
| TLS | 전송 계층 보안 | Authenticated encrypted channel protocol | [Web](./06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) |
| Consensus | 합의 | Nodes đồng thuận authoritative value/log | [Distributed](./06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) |
| Socket | 소켓 | Application endpoint handle cho communication | [Sockets](./06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) |
| NAT | 네트워크 주소 변환 | Rewrite network address/port mappings | [Sockets/Network Boundary](./06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) |
| VPN | 가상 사설망 | Secure/tunneled overlay network | [Sockets/Network Boundary](./06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) |
| Autonomous System | 자율 시스템 | Network domain có routing policy riêng trên Internet | [Routing](./06_networks_distributed_systems/07_routing_protocols_and_the_internet.md) |
| BGP | 경계 경로 프로토콜 | Inter-AS path-vector routing protocol | [Routing](./06_networks_distributed_systems/07_routing_protocols_and_the_internet.md) |
| QUIC | QUIC | Encrypted multiplexed transport chạy trên UDP substrate | [Modern Transport](./06_networks_distributed_systems/08_http2_http3_quic_and_modern_transport.md) |
| Authentication | 인증 | Xác minh identity/credential | [Identity](./07_security_reliability/02_identity_authentication_and_authorization.md) |
| Authorization | 인가 | Quyết định permission trên action/resource | [Identity](./07_security_reliability/02_identity_authentication_and_authorization.md) |
| Threat model | 위협 모델 | Structured model về assets, attackers và attack paths | [Security](./07_security_reliability/00_threat_models_and_security_principles.md) |
| AEAD | 인증된 암호화 | Encryption + integrity/authentication | [Cryptography](./07_security_reliability/01_cryptography_foundations.md) |
| XSS | 크로스 사이트 스크립팅 | Untrusted data bị browser diễn giải thành executable content | [Web Security](./07_security_reliability/06_web_application_security.md) |
| CSRF | 사이트 간 요청 위조 | Lợi dụng browser gửi credentials ngoài intent user | [Web Security](./07_security_reliability/06_web_application_security.md) |
| KMS | 키 관리 시스템 | Managed system cho cryptographic key lifecycle | [Keys/Secrets](./07_security_reliability/07_keys_secrets_certificates_and_secure_operations.md) |
| HSM | 하드웨어 보안 모듈 | Hardware boundary bảo vệ/thực thi crypto keys | [Keys/Secrets](./07_security_reliability/07_keys_secrets_certificates_and_secure_operations.md) |
| SBOM | 소프트웨어 자재 명세서 | Inventory components trong software artifact | [Supply Chain](./07_security_reliability/08_supply_chain_and_secure_software_lifecycle.md) |
| Observability | 관측 가능성 | Suy internal state từ telemetry | [Reliability](./07_security_reliability/05_fault_tolerance_observability_and_reliability.md) |
| SLO | 서비스 수준 목표 | Reliability target trên service indicator | [Reliability](./07_security_reliability/05_fault_tolerance_observability_and_reliability.md) |
| Backpressure | 백프레셔 | Downstream capacity signal ngược producer | [Queues](./08_software_systems/03_state_queues_backpressure_and_boundaries.md) |
| Idempotency | 멱등성 | Lặp logical operation không thay final effect sau lần đầu | [Time/State](./08_software_systems/04_time_serialization_and_idempotency.md) |
| Cache stampede | 캐시 스탬피드 | Nhiều requests cùng miss/refresh hot cache entry | [Caching](./08_software_systems/05_caching_load_balancing_and_cdns.md) |
| CDN | 콘텐츠 전송 네트워크 | Distributed edge delivery/cache network | [Caching/CDN](./08_software_systems/05_caching_load_balancing_and_cdns.md) |
| Event sourcing | 이벤트 소싱 | Lưu state changes dưới dạng ordered events | [Event Systems](./08_software_systems/06_event_driven_and_stream_processing.md) |
| Saga | 사가 패턴 | Distributed workflow bằng local transactions + compensation | [System Boundaries](./08_software_systems/07_system_decomposition_services_and_boundaries.md) |
| Requirement | 요구사항 | Observable need/constraint system phải đáp ứng | [Requirements](./09_software_engineering/00_requirements_specification_and_engineering_process.md) |
| ADR | 아키텍처 결정 기록 | Record context/options/decision/consequences | [Architecture](./09_software_engineering/01_software_architecture_and_design_reasoning.md) |
| Contract testing | 계약 테스트 | Verify producer-consumer interface compatibility | [Testing](./09_software_engineering/02_testing_quality_and_verification_strategy.md) |
| Continuous Integration | 지속적 통합 | Integrate frequently với automated build/test feedback | [Delivery](./09_software_engineering/03_delivery_configuration_and_operations.md) |
| Technical debt | 기술 부채 | Future change cost do intentional/accidental shortcuts/structure | [Maintenance](./09_software_engineering/04_maintenance_evolution_and_technical_debt.md) |
| Agent | 에이전트 | System nhận percepts và chọn actions theo objective | [AI](./10_ai_foundations/00_ai_problem_formulation_search_and_agents.md) |
| Heuristic | 휴리스틱 | Estimate/rule hướng search hoặc solution | [AI Search](./10_ai_foundations/00_ai_problem_formulation_search_and_agents.md) |
| Bayesian network | 베이지안 네트워크 | DAG biểu diễn probabilistic conditional dependencies | [AI Reasoning](./10_ai_foundations/01_knowledge_reasoning_and_probabilistic_inference.md) |
| Generalization | 일반화 | Model performance trên unseen target-distribution data | [ML](./10_ai_foundations/02_machine_learning_foundations.md) |
| Overfitting | 과적합 | Fit training idiosyncrasies nhưng generalize kém | [ML](./10_ai_foundations/02_machine_learning_foundations.md) |
| Backpropagation | 역전파 | Chain-rule gradient computation trên computation graph | [Neural Networks](./10_ai_foundations/03_neural_networks_and_representation_learning.md) |
| Embedding | 임베딩 | Learned vector representation của discrete/entity data | [Neural Networks](./10_ai_foundations/03_neural_networks_and_representation_learning.md) |
| Calibration | 캘리브레이션, 보정 | Mức predicted probability khớp observed frequency | [AI Evaluation](./10_ai_foundations/04_ai_evaluation_data_and_responsibility.md) |
| HCI | 인간-컴퓨터 상호작용 | Nghiên cứu interaction giữa human và computer systems | [HCI](./11_hci_graphics/00_hci_human_factors_and_interaction_models.md) |
| Accessibility | 접근성 | Khả năng sử dụng bởi diverse abilities/devices/contexts | [Accessibility](./11_hci_graphics/01_interface_design_accessibility_and_usability.md) |
| Rasterization | 래스터화 | Chuyển geometric primitives thành screen fragments/samples | [Graphics](./11_hci_graphics/02_computer_graphics_pipeline_and_geometry.md) |
| Shader | 셰이더 | GPU program xử lý vertices/fragments/graphics stages | [Graphics](./11_hci_graphics/02_computer_graphics_pipeline_and_geometry.md) |
| Aliasing | 에일리어싱 | Sampling artifact khi signal frequency vượt representable rate | [Imaging](./11_hci_graphics/03_images_color_rasterization_and_rendering.md) |
| Frame time | 프레임 시간 | Thời gian cần tạo một frame | [Interactive Systems](./11_hci_graphics/04_multimedia_animation_and_interactive_systems.md) |
| Privacy | 개인정보 보호, 프라이버시 | Control/context của personal information lifecycle | [Ethics](./12_society_ethics_profession/00_computing_ethics_privacy_and_professional_responsibility.md) |
| Data provenance | 데이터 출처/계보 | Nguồn và transformation history của data | [Governance](./12_society_ethics_profession/01_data_governance_bias_and_algorithmic_impact.md) |
| Open-source license | 오픈소스 라이선스 | Rights/obligations cho use/modify/distribute source | [Law/Licensing](./12_society_ethics_profession/02_software_law_licenses_and_intellectual_property.md) |
| Digital divide | 디지털 격차 | Chênh lệch access/capability với computing infrastructure | [Society](./12_society_ethics_profession/03_sustainability_accessibility_and_social_infrastructure.md) |
