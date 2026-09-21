# Glossary — Computer Science Việt / English / 한국어

Glossary này dùng để nhận diện thuật ngữ khi đọc textbook, documentation, 기사 시험 hoặc trao đổi trong công ty Hàn Quốc. Nó **không thay chapter giải thích concept**; link ở cột cuối dẫn tới context đầy đủ.

| English term | 한국어 | Tiếng Việt / ý chính | Chapter |
|---|---|---|---|
| Abstraction | 추상화 | Trừu tượng hóa: giữ contract cần thiết, che chi tiết implementation | [Foundations](./00_computation_information/03_logic_state_abstraction_and_invariants.md) |
| Algorithm | 알고리즘 | Thuật toán: procedure biến input thành output theo specification | [Algorithms](./01_algorithms_data_structures/00_algorithmic_thinking_and_correctness.md) |
| Asymptotic complexity | 점근적 복잡도 | Độ tăng chi phí khi input scale | [Complexity](./01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) |
| Big O | 빅오 표기법 | Upper-bound asymptotic notation | [Complexity](./01_algorithms_data_structures/01_complexity_and_asymptotic_analysis.md) |
| Bit | 비트 | Binary digit 0/1 | [Information](./00_computation_information/01_information_bits_and_encoding.md) |
| Byte | 바이트 | Nhóm 8 bit trong kiến trúc hiện đại phổ biến | [Information](./00_computation_information/01_information_bits_and_encoding.md) |
| Encoding | 인코딩 | Quy tắc map symbol/value ↔ representation | [Information](./00_computation_information/01_information_bits_and_encoding.md) |
| Two's complement | 2의 보수 | Representation signed integer phổ biến | [Machine representation](./00_computation_information/02_numbers_and_machine_representation.md) |
| Floating point | 부동소수점 | Biểu diễn số xấp xỉ dạng significand/exponent | [Machine representation](./00_computation_information/02_numbers_and_machine_representation.md) |
| Invariant | 불변식 | Property phải được bảo toàn qua transitions | [State & invariants](./00_computation_information/03_logic_state_abstraction_and_invariants.md) |
| Computability | 계산 가능성 | Khả năng problem/function được algorithm tính | [Computability](./00_computation_information/04_computability_and_limits.md) |
| Undecidable | 결정 불가능 | Không có algorithm tổng quát luôn halt và quyết định đúng | [Computability](./00_computation_information/04_computability_and_limits.md) |
| Array | 배열 | Mảng contiguous, random indexing | [Linear structures](./01_algorithms_data_structures/03_linear_data_structures.md) |
| Linked list | 연결 리스트 | Danh sách liên kết bằng references | [Linear structures](./01_algorithms_data_structures/03_linear_data_structures.md) |
| Stack | 스택 | LIFO abstract data type | [Linear structures](./01_algorithms_data_structures/03_linear_data_structures.md) |
| Queue | 큐 | FIFO abstract data type | [Linear structures](./01_algorithms_data_structures/03_linear_data_structures.md) |
| Hash table | 해시 테이블 | Map key→bucket/slot qua hash | [Hashing](./01_algorithms_data_structures/04_hashing_and_hash_tables.md) |
| Collision | 충돌 | Hai keys map cùng hash/bucket | [Hashing](./01_algorithms_data_structures/04_hashing_and_hash_tables.md) |
| Tree | 트리 | Graph hierarchy connected acyclic | [Trees](./01_algorithms_data_structures/05_trees_heaps_and_search_structures.md) |
| Heap | 힙 | Partial-order tree dùng priority queue | [Trees](./01_algorithms_data_structures/05_trees_heaps_and_search_structures.md) |
| B-tree / B+ tree | B-트리 / B+트리 | High-fanout search tree tối ưu page/block access | [Trees](./01_algorithms_data_structures/05_trees_heaps_and_search_structures.md) |
| Graph | 그래프 | Nodes/edges biểu diễn relationships | [Graphs](./01_algorithms_data_structures/06_graphs_and_graph_algorithms.md) |
| BFS | 너비 우선 탐색 | Tìm kiếm theo breadth/layers | [Graphs](./01_algorithms_data_structures/06_graphs_and_graph_algorithms.md) |
| DFS | 깊이 우선 탐색 | Tìm kiếm đi sâu trước | [Graphs](./01_algorithms_data_structures/06_graphs_and_graph_algorithms.md) |
| Dynamic Programming | 동적 계획법 | Tái sử dụng overlapping subproblems với state/recurrence | [Strategies](./01_algorithms_data_structures/08_algorithmic_strategies.md) |
| Greedy | 그리디, 탐욕법 | Quyết định local không quay lại khi có proof phù hợp | [Strategies](./01_algorithms_data_structures/08_algorithmic_strategies.md) |
| CPU | 중앙 처리 장치 | Bộ xử lý trung tâm | [CPU/ISA](./02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) |
| ISA | 명령어 집합 구조 | Contract instructions/registers giữa software và CPU | [CPU/ISA](./02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) |
| Cache | 캐시 | Tầng lưu nhỏ/nhanh giữ data likely reused | [Cache](./02_computer_architecture/02_memory_hierarchy_and_cache.md) |
| Cache line | 캐시 라인 | Đơn vị block CPU cache transfer/coherence | [Cache](./02_computer_architecture/02_memory_hierarchy_and_cache.md) |
| Locality | 지역성 | Tính cục bộ temporal/spatial của accesses | [Data layout](./01_algorithms_data_structures/02_memory_models_and_data_layout.md) |
| DMA | 직접 메모리 접근 | Device transfer memory không CPU copy từng word | [I/O](./02_computer_architecture/03_io_interrupts_dma_and_devices.md) |
| Interrupt | 인터럽트 | Event chuyển CPU control tới handler | [I/O](./02_computer_architecture/03_io_interrupts_dma_and_devices.md) |
| ABI | 응용 프로그램 이진 인터페이스 | Binary calling/layout/link contract | [ABI](./02_computer_architecture/04_machine_code_assembly_and_abi.md) |
| SIMD | 단일 명령 다중 데이터 | Một instruction xử lý nhiều lanes data | [Parallel architecture](./02_computer_architecture/05_parallel_computer_architecture.md) |
| Kernel | 커널 | Privileged core của OS | [Kernel](./03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) |
| System call | 시스템 호출 | Controlled entry từ user mode vào kernel | [Kernel](./03_operating_systems/00_kernel_syscalls_and_os_abstractions.md) |
| Process | 프로세스 | Isolated execution/resource context | [Processes](./03_operating_systems/01_processes_threads_and_scheduling.md) |
| Thread | 스레드 | Schedulable execution stream | [Processes](./03_operating_systems/01_processes_threads_and_scheduling.md) |
| Context switch | 문맥 교환 | Chuyển CPU execution context giữa tasks | [Processes](./03_operating_systems/01_processes_threads_and_scheduling.md) |
| Mutex | 뮤텍스 | Mutual-exclusion lock | [Concurrency](./03_operating_systems/02_concurrency_synchronization_and_deadlock.md) |
| Deadlock | 교착 상태 | Tasks chờ cycle không progress | [Concurrency](./03_operating_systems/02_concurrency_synchronization_and_deadlock.md) |
| Virtual memory | 가상 메모리 | Virtual-address mapping/isolation abstraction | [Virtual memory](./03_operating_systems/03_virtual_memory_and_address_spaces.md) |
| Page fault | 페이지 폴트 | Trap khi page mapping cần OS handling | [Virtual memory](./03_operating_systems/03_virtual_memory_and_address_spaces.md) |
| File system | 파일 시스템 | Abstraction names/files trên storage blocks | [Filesystem](./03_operating_systems/04_filesystems_storage_and_io.md) |
| Virtual machine | 가상 머신 | Virtualized hardware/runtime environment tùy context | [Virtualization](./03_operating_systems/05_privilege_isolation_and_virtualization.md) |
| Container | 컨테이너 | OS-level isolation dùng namespaces/cgroups etc. | [Virtualization](./03_operating_systems/05_privilege_isolation_and_virtualization.md) |
| Semantics | 의미론 | Quy tắc meaning của language/program | [Language semantics](./04_programming_languages/00_language_semantics_and_execution_models.md) |
| Type system | 타입 시스템 | Rules về values/operations/compatibility | [Types](./04_programming_languages/01_types_values_references_and_memory.md) |
| Garbage Collection | 가비지 컬렉션 | Reclaim memory unreachable tự động | [Types](./04_programming_languages/01_types_values_references_and_memory.md) |
| Closure | 클로저 | Function + captured lexical environment | [Scope/closures](./04_programming_languages/02_scope_closures_functions_and_control_flow.md) |
| Compiler | 컴파일러 | Transform source/IR sang representation executable hơn | [Compiler](./04_programming_languages/03_compilers_interpreters_vm_and_jit.md) |
| Interpreter | 인터프리터 | Runtime evaluator của source/AST/bytecode | [Compiler](./04_programming_languages/03_compilers_interpreters_vm_and_jit.md) |
| JIT | JIT 컴파일 | Compile hot code at runtime | [Compiler](./04_programming_languages/03_compilers_interpreters_vm_and_jit.md) |
| Transaction | 트랜잭션 | Atomic logical state transition trong DB | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| ACID | ACID | Atomicity, Consistency, Isolation, Durability | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| MVCC | 다중 버전 동시성 제어 | Giữ multiple versions để isolate concurrent transactions | [Transactions](./05_data_databases/02_transactions_acid_and_concurrency_control.md) |
| Index | 인덱스 | Auxiliary access path cho query | [Indexes](./05_data_databases/03_indexes_and_query_execution.md) |
| WAL | 선행 기록 로그 | Write-ahead logging cho atomicity/durability/recovery | [Storage](./05_data_databases/04_storage_logs_recovery_and_durability.md) |
| Packet | 패킷 | Network-layer data unit (dùng rộng tùy context) | [Network layers](./06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md) |
| Routing | 라우팅 | Chọn next path/next hop cho network destinations | [IP/Routing](./06_networks_distributed_systems/01_ethernet_ip_subnetting_and_routing.md) |
| TCP | 전송 제어 프로토콜 | Reliable ordered byte-stream transport | [TCP/UDP](./06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) |
| UDP | 사용자 데이터그램 프로토콜 | Datagram transport không built-in retransmission/order | [TCP/UDP](./06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) |
| DNS | 도메인 이름 시스템 | Distributed naming system | [Web request](./06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) |
| TLS | 전송 계층 보안 | Secure channel protocol | [Web request](./06_networks_distributed_systems/03_dns_http_tls_and_web_request.md) |
| Replication | 복제 | Giữ nhiều copies của data/state | [Replication](./06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) |
| Partitioning / Sharding | 파티셔닝 / 샤딩 | Chia dataset/workload qua nodes | [Replication](./06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) |
| Consensus | 합의 | Nodes đồng thuận authoritative decision/log | [Replication](./06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) |
| Authentication | 인증 | Xác minh identity/credential | [Identity](./07_security_reliability/02_identity_authentication_and_authorization.md) |
| Authorization | 인가 | Quyết định permission trên action/resource | [Identity](./07_security_reliability/02_identity_authentication_and_authorization.md) |
| Cryptographic hash | 암호학적 해시 | One-way fixed-length digest với security properties | [Cryptography](./07_security_reliability/01_cryptography_foundations.md) |
| MAC | 메시지 인증 코드 | Keyed integrity/authenticity tag | [Cryptography](./07_security_reliability/01_cryptography_foundations.md) |
| Digital signature | 전자 서명 | Asymmetric signature verified bằng public key | [Cryptography](./07_security_reliability/01_cryptography_foundations.md) |
| Observability | 옵저버빌리티, 관측 가능성 | Khả năng suy internal state từ telemetry | [Reliability](./07_security_reliability/05_fault_tolerance_observability_and_reliability.md) |
| SLO | 서비스 수준 목표 | Target cho measured reliability/service indicator | [Reliability](./07_security_reliability/05_fault_tolerance_observability_and_reliability.md) |
| Latency | 지연 시간 | Thời gian hoàn thành operation | [Performance](./08_software_systems/02_performance_capacity_and_scalability.md) |
| Throughput | 처리량 | Lượng work hoàn thành mỗi unit time | [Performance](./08_software_systems/02_performance_capacity_and_scalability.md) |
| Backpressure | 백프레셔 | Tín hiệu downstream capacity ngược lên producer | [Queues](./08_software_systems/03_state_queues_backpressure_and_boundaries.md) |
| Idempotency | 멱등성 | Lặp cùng logical operation không đổi effect sau lần đầu | [Time/Idempotency](./08_software_systems/04_time_serialization_and_idempotency.md) |
| Serialization | 직렬화 | Chuyển values/state thành wire/storage representation | [Time/Idempotency](./08_software_systems/04_time_serialization_and_idempotency.md) |
