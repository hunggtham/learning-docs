# Computer Science Knowledge Library

`computer_science/` được tổ chức thành hai lớp kiến thức rõ ràng:

- **Basic / Foundation** tại [`basic/`](./basic/README.md): xây mental model cốt lõi của toàn bộ Computer Science.
- **Advanced / Specialized** tại các domain hub cùng tên ở cấp `computer_science/`: đi sâu vào internals, proofs, implementation, production behavior, failure modes và senior-level trade-offs.

`Basic` không có nghĩa sơ sài. Nó là prerequisite chung. `Advanced` không lặp lại phần nền mà bắt đầu từ những assumptions đã có để đào sâu.

## Bản đồ Basic → Advanced

| Domain | Basic | Advanced |
|---|---|---|
| Computation & Information | [`basic/00_computation_information`](./basic/00_computation_information/) | [`00_computation_information/advanced`](./00_computation_information/advanced/README.md) |
| Algorithms & Data Structures | [`basic/01_algorithms_data_structures`](./basic/01_algorithms_data_structures/) | [`01_algorithms_data_structures/advanced`](./01_algorithms_data_structures/advanced/README.md) |
| Computer Architecture | [`basic/02_computer_architecture`](./basic/02_computer_architecture/) | [`02_computer_architecture/advanced`](./02_computer_architecture/advanced/README.md) |
| Operating Systems | [`basic/03_operating_systems`](./basic/03_operating_systems/) | [`03_operating_systems/advanced`](./03_operating_systems/advanced/README.md) |
| Programming Languages & Runtime | [`basic/04_programming_languages`](./basic/04_programming_languages/) | [`04_programming_languages/advanced`](./04_programming_languages/advanced/README.md) |
| Data & Databases | [`basic/05_data_databases`](./basic/05_data_databases/) | [`05_data_databases/advanced`](./05_data_databases/advanced/README.md) |
| Networks & Distributed Systems | [`basic/06_networks_distributed_systems`](./basic/06_networks_distributed_systems/) | [`06_networks_distributed_systems/advanced`](./06_networks_distributed_systems/advanced/README.md) |
| Security & Reliability | [`basic/07_security_reliability`](./basic/07_security_reliability/) | [`07_security_reliability/advanced`](./07_security_reliability/advanced/README.md) |
| Software Systems | [`basic/08_software_systems`](./basic/08_software_systems/) | [`08_software_systems/advanced`](./08_software_systems/advanced/README.md) |
| Software Engineering | [`basic/09_software_engineering`](./basic/09_software_engineering/) | [`09_software_engineering/advanced`](./09_software_engineering/advanced/README.md) |
| AI Foundations | [`basic/10_ai_foundations`](./basic/10_ai_foundations/) | [`10_ai_foundations/advanced`](./10_ai_foundations/advanced/README.md) |
| HCI & Graphics | [`basic/11_hci_graphics`](./basic/11_hci_graphics/) | [`11_hci_graphics/advanced`](./11_hci_graphics/advanced/README.md) |
| Society, Ethics & Profession | [`basic/12_society_ethics_profession`](./basic/12_society_ethics_profession/) | [`12_society_ethics_profession/advanced`](./12_society_ethics_profession/advanced/README.md) |
| Cross-domain Connections | [`basic/90_connections`](./basic/90_connections/) | [`90_connections/advanced`](./90_connections/advanced/README.md) |

## Cách học

Không cần học hết Basic rồi mới được đọc Advanced. Quy tắc tốt hơn là: đọc foundation chapter tương ứng để có vocabulary + mechanism chính, sau đó chuyển sang advanced khi cần hiểu internals, proof, performance, failure mode hoặc production design.

Ví dụ:

```text
basic/02_computer_architecture/02_memory_hierarchy_and_cache.md
        ↓
02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md
        ↓
basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md
        ↓
advanced OS / runtime concurrency
```

DSA đã có library advanced riêng theo cùng pattern và tiếp tục giữ implementation sâu bằng C, Java và JavaScript. Các domain advanced còn lại sẽ được mở rộng từng chapter theo roadmap trong mỗi `advanced/README.md`.

## Nguyên tắc biên soạn Advanced

Advanced chapter phải trả lời sâu hơn foundation ở ít nhất một trong các hướng: internal mechanism; formal invariant/proof; performance model; concurrency/failure semantics; implementation strategy; observability/debugging; production trade-offs; hoặc cross-layer interaction. Không thêm chapter chỉ vì một technology phổ biến nếu nó không tạo mental model mới.