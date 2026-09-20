# Computer Science Knowledge Library

Thư mục `computer_science/` là namespace cấp cao cho các bộ kiến thức Computer Science trong repository. Nội dung được tách theo **vai trò kiến thức**, để nền tảng không bị trộn với các library chuyên sâu.

## Basic — kiến thức nền tảng

Toàn bộ Knowledge Library Computer Science nền tảng hiện nằm tại:

**[Computer Science Basic Knowledge Library](./basic/README.md)**

`basic/` chứa 100 topic chapters theo conceptual dependency, đi từ computation và information tới algorithms/data structures nền tảng, computer architecture, operating systems, programming languages/runtime, databases, networking/distributed systems, security/reliability, software systems, software engineering, AI foundations, HCI/graphics và computing in society.

```text
computer_science/
├── README.md              # trang điều hướng cấp cao
└── basic/                 # kiến thức Computer Science nền tảng
    ├── 00_computation_information/
    ├── 01_algorithms_data_structures/
    ├── 02_computer_architecture/
    ├── 03_operating_systems/
    ├── 04_programming_languages/
    ├── 05_data_databases/
    ├── 06_networks_distributed_systems/
    ├── 07_security_reliability/
    ├── 08_software_systems/
    ├── 09_software_engineering/
    ├── 10_ai_foundations/
    ├── 11_hci_graphics/
    ├── 12_society_ethics_profession/
    ├── 90_connections/
    ├── 99_glossary.md
    └── COVERAGE_AUDIT.md
```

## Advanced / Specialized

Các library chuyên sâu nên được giữ tách khỏi `basic/`. Ví dụ bộ **Data Structures & Algorithms chuyên sâu** đang được phát triển riêng ở branch `feat/dsa-knowledge-library` trong folder `data_structures_algorithms/`. Khi hợp nhất vào `main`, library đó vẫn nên giữ vai trò advanced/specialized thay vì thay thế các chapter DSA nền tảng trong `basic/`.

Nguyên tắc phân chia là: `basic/` trả lời *một computer system và các nguyên lý CS cốt lõi hoạt động như thế nào*; các library advanced đi sâu vào một domain cụ thể với nhiều algorithms, implementation, proof, optimization và edge cases hơn.
