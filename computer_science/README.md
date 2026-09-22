# Thư viện kiến thức Khoa học máy tính

`computer_science/` được tổ chức thành hai lớp kiến thức rõ ràng:

- **Nền tảng (Basic / Foundation / 기초)** tại [`basic/`](./basic/README.md): xây dựng các mô hình tư duy cốt lõi của Khoa học máy tính (Computer Science).
- **Nâng cao và chuyên sâu (Advanced / Specialized)** tại các nhóm chủ đề cùng tên ở cấp `computer_science/`: đi sâu vào cơ chế bên trong (internals), invariant, hành vi khi có failure hoặc pressure, cách quan sát production và các đánh đổi ở mức kỹ sư nhiều kinh nghiệm.

“Nền tảng” không có nghĩa là sơ sài. Đây là lớp kiến thức tiên quyết (prerequisite) chung. Phần nâng cao không lặp lại toàn bộ kiến thức nền mà dựa trên những giả định đã được giải thích để đào sâu hơn.

Xem [quy ước ngôn ngữ](./LANGUAGE_STYLE.md) để hiểu cách thư viện ưu tiên tiếng Việt và giữ thuật ngữ tiếng Anh trong ngoặc khi cần. Xem [Coverage Audit](./COVERAGE_AUDIT.md) để biết domain nào đang mạnh, gap nào còn lại và quy tắc maintenance hiện tại.

## Bản đồ Nền tảng → Nâng cao

| Lĩnh vực | Nền tảng | Nâng cao |
|---|---|---|
| Tính toán & Thông tin (Computation & Information) | [`basic/00_computation_information`](./basic/00_computation_information/) | [`00_computation_information/advanced`](./00_computation_information/advanced/README.md) |
| Thuật toán & Cấu trúc dữ liệu (Algorithms & Data Structures) | [`basic/01_algorithms_data_structures`](./basic/01_algorithms_data_structures/) | [`01_algorithms_data_structures/advanced`](./01_algorithms_data_structures/advanced/README.md) |
| Kiến trúc máy tính (Computer Architecture) | [`basic/02_computer_architecture`](./basic/02_computer_architecture/) | [`02_computer_architecture/advanced`](./02_computer_architecture/advanced/README.md) |
| Hệ điều hành (Operating Systems) | [`basic/03_operating_systems`](./basic/03_operating_systems/) | [`03_operating_systems/advanced`](./03_operating_systems/advanced/README.md) |
| Ngôn ngữ lập trình & Môi trường thực thi (Programming Languages & Runtime) | [`basic/04_programming_languages`](./basic/04_programming_languages/) | [`04_programming_languages/advanced`](./04_programming_languages/advanced/README.md) |
| Dữ liệu & Cơ sở dữ liệu (Data & Databases) | [`basic/05_data_databases`](./basic/05_data_databases/) | [`05_data_databases/advanced`](./05_data_databases/advanced/README.md) |
| Mạng & Hệ thống phân tán (Networks & Distributed Systems) | [`basic/06_networks_distributed_systems`](./basic/06_networks_distributed_systems/) | [`06_networks_distributed_systems/advanced`](./06_networks_distributed_systems/advanced/README.md) |
| Bảo mật & Độ tin cậy (Security & Reliability) | [`basic/07_security_reliability`](./basic/07_security_reliability/) | [`07_security_reliability/advanced`](./07_security_reliability/advanced/README.md) |
| Hệ thống phần mềm (Software Systems) | [`basic/08_software_systems`](./basic/08_software_systems/) | [`08_software_systems/advanced`](./08_software_systems/advanced/README.md) |
| Kỹ nghệ phần mềm (Software Engineering) | [`basic/09_software_engineering`](./basic/09_software_engineering/) | [`09_software_engineering/advanced`](./09_software_engineering/advanced/README.md) |
| Nền tảng Trí tuệ nhân tạo (AI Foundations) | [`basic/10_ai_foundations`](./basic/10_ai_foundations/) | [`10_ai_foundations/advanced`](./10_ai_foundations/advanced/README.md) |
| Tương tác người–máy & Đồ họa (HCI & Graphics) | [`basic/11_hci_graphics`](./basic/11_hci_graphics/) | [`11_hci_graphics/advanced`](./11_hci_graphics/advanced/README.md) |
| Xã hội, Đạo đức & Nghề nghiệp | [`basic/12_society_ethics_profession`](./basic/12_society_ethics_profession/) | [`12_society_ethics_profession/advanced`](./12_society_ethics_profession/advanced/README.md) |
| Kết nối xuyên lĩnh vực | [`basic/90_connections`](./basic/90_connections/) | [`90_connections/advanced`](./90_connections/advanced/README.md) |

## Thư viện AI chuyên sâu

Ngoài tuyến `basic/10_ai_foundations → 10_ai_foundations/advanced`, repository có một thư viện chuyên sâu riêng về AI:

**[Artificial Intelligence Knowledge Library](./02_artificial_intelligence/README.md)**

Thư viện này đi theo quan hệ phụ thuộc khái niệm và mở rộng từ Transformer, LLM, Retrieval/Vector Search, RAG, Tool Calling và Agents tới Evaluation, AI Engineering, LLMOps, Reliability và Security. Nó bổ sung chiều sâu theo domain, không thay thế lớp AI Foundations dùng chung của Computer Science.

## Cách học

Không cần học hết phần nền tảng rồi mới đọc phần nâng cao. Cách hợp lý hơn là đọc chapter nền tảng tương ứng để có vocabulary và mental model chính, sau đó chuyển sang phần nâng cao khi cần hiểu internals, invariant, failure behavior, performance hoặc production evidence.

### Learning route 1 — từ phần cứng đến application

```text
CPU / cache / memory hierarchy
↓
virtual memory / scheduler / syscall / I/O
↓
runtime: GC / JIT / coroutine
↓
application concurrency / queues / database client
↓
network / remote service
↓
distributed coordination / replication / consistency
```

Route này phù hợp khi muốn hiểu vì sao cùng một đoạn code có thể chậm hoặc sai vì nguyên nhân ở tầng thấp hơn. Nên đọc lần lượt Architecture → OS → Programming Languages & Runtime → Software Systems → Networks & Distributed Systems, rồi quay lại [`90_connections/advanced`](./90_connections/advanced/README.md) để nối các tầng bằng symptom thực tế.

### Learning route 2 — durability và consistency

```text
application transaction
↓
MVCC / WAL / lock
↓
filesystem / page cache / device
↓
replication / consensus
↓
cache / event / replica visibility
```

Route này dùng cho backend/database engineering. Bắt đầu từ nền tảng transaction rồi đọc Database Advanced, OS filesystem/I/O, Distributed Systems và chapter [durability xuyên tầng](./90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

### Learning route 3 — concurrency và ordering

```text
language memory model
↓
runtime scheduler / coroutine
↓
OS thread / synchronization
↓
CPU memory ordering / cache coherence
↓
network ordering / timeout
↓
distributed causality / consensus
```

Route này giúp phân biệt data race, logical race, thread scheduling, memory reordering và distributed ordering. Không dùng từ “concurrent” như một khái niệm duy nhất cho mọi tầng.

### Learning route 4 — reliability và security boundary

```text
identity / authorization
↓
process/container boundary
↓
service identity / TLS
↓
secret / KMS / key lifecycle
↓
distributed failure / retry / overload
↓
incident containment / recovery
```

Route này nối Security với Reliability thay vì coi chúng là hai môn rời rạc. Một control bảo mật có thể tạo dependency availability; một retry policy reliability có thể trở thành abuse amplifier nếu thiếu rate limit hoặc idempotency.

## Quy tắc dependency trong chapter nâng cao

Một chapter nâng cao không được giả định người đọc đã hiểu sâu thuật ngữ hệ thống chỉ vì thuật ngữ đó phổ biến. Khi lần đầu dùng các khái niệm như `process`, `thread`, `virtual memory`, `syscall`, `cache`, `WAL`, `MVCC`, `consensus`, `idempotency`, chapter phải giải thích bản chất ngắn gọn hoặc link trực tiếp tới foundation chứa mental model đó.

Một concept advanced nên cố gắng trả lời tự nhiên chuỗi câu hỏi sau:

```text
1. Vấn đề ban đầu là gì?
2. Invariant nào cần được duy trì?
3. Internals giữ invariant bằng mechanism nào?
4. Failure xảy ra khi assumption nào mất hiệu lực?
5. Performance / concurrency / consistency pressure làm behavior thay đổi ra sao?
6. Evidence nào giúp quan sát và phân biệt các hypothesis?
7. Abstraction layer nào bên dưới thực sự quyết định behavior?
8. Fix nên đặt ở layer nào sở hữu invariant?
```

Không cần ép mọi chapter thành template cứng, nhưng nếu một phần advanced không tạo thêm khả năng reasoning theo các câu hỏi trên thì chưa đủ lý do để tồn tại như một chapter riêng.

## Nguyên tắc audit coverage

Coverage được xem là đủ khi domain có đường reasoning:

```text
foundation
→ internals
→ failure modes
→ performance / concurrency / consistency
→ production evidence
→ cross-layer connections
```

Không tăng số chapter chỉ để làm roadmap dài hơn. Khi audit một domain, ưu tiên tìm chapter quá mỏng; dependency ẩn; assumption chưa nói rõ; failure/edge case còn thiếu; connection tới lower layer quyết định behavior; evidence production còn thiếu; và duplicate có thể thay bằng cross-link.

Production evidence có thể là metric, trace, execution plan, GC log, wait event, scheduler evidence, PMU counter, replication position hoặc state-transition evidence tùy domain. Mục tiêu không phải thêm tool name, mà giúp người đọc biết **cần quan sát tín hiệu nào để kiểm chứng mechanism**.

Cấu trúc dữ liệu và thuật toán (DSA) đã có phần nâng cao riêng theo cùng mô hình và đi sâu vào implementation bằng C, Java và JavaScript. Các domain khác tiếp tục được cải thiện trong chính `computer_science/`, không tách Network, Distributed Systems, Security, Reliability, Performance Engineering, Concurrency hoặc System Design thành root library mới nếu conceptual boundary hiện tại đã đủ.

## Nguyên tắc biên soạn phần nâng cao

Một chương nâng cao phải đào sâu hơn foundation ở ít nhất một hướng: cơ chế bên trong; invariant hoặc chứng minh; mô hình performance; concurrency/consistency semantics; failure behavior; khả năng quan sát và gỡ lỗi; deployment/evolution trade-off; hoặc interaction giữa nhiều abstraction layers.

Ưu tiên giữ cấu trúc canonical hiện có. Nếu gap có cùng invariant và failure model với chapter đang tồn tại, rewrite sâu chapter đó trước. Chỉ tạo file mới khi topic có mental model riêng, là dependency quan trọng cho nhiều phần khác và việc đặt vào chapter cũ thực sự làm mất conceptual boundary.

Không thêm chapter chỉ vì một technology đang phổ biến.