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

## Specialized Knowledge Libraries

Các library chuyên sâu được giữ tách khỏi `basic/`. `basic/` cung cấp conceptual foundation cần thiết để hiểu Computer Science như một whole system; các library specialized mở rộng một domain thành nhiều textbook-like chapters với nhiều mechanism, implementation, mathematical reasoning, optimization và edge cases hơn.

### Data Structures & Algorithms

Bộ **Data Structures & Algorithms** chuyên sâu nằm tại:

**[Data Structures & Algorithms Knowledge Library](./01_algorithms_data_structures/README.md)**

Library này đi sâu vào data structures, algorithmic reasoning, implementation và complexity thay vì thay thế các chapter DSA nền tảng trong `basic/`.

### Artificial Intelligence

Bộ **Artificial Intelligence Knowledge Library** đang được phát triển tại:

**[Artificial Intelligence Knowledge Library](./02_artificial_intelligence/README.md)**

Library AI được tổ chức theo conceptual dependency thay vì Beginner → Advanced. Nội dung bắt đầu từ bản chất của intelligence, agents, problem representation và AI system architecture; sau đó nối tới mathematical foundations, search/planning, knowledge reasoning, Machine Learning, Deep Learning, Transformer, LLM, RAG, Agents, Reinforcement Learning, Computer Vision, multimodal AI, AI Engineering, MLOps/LLMOps, infrastructure, evaluation, safety và governance.

Nguyên tắc phân chia là: `basic/` trả lời *một computer system và các nguyên lý CS cốt lõi hoạt động như thế nào*; các library chuyên sâu trả lời *một domain cụ thể vận hành từ first principles tới production system như thế nào*.