# Thư viện kiến thức Khoa học máy tính

`computer_science/` được tổ chức thành hai lớp kiến thức rõ ràng:

- **Nền tảng (Basic / Foundation / 기초)** tại [`basic/`](./basic/README.md): xây dựng các mô hình tư duy cốt lõi của Khoa học máy tính (Computer Science).
- **Nâng cao và chuyên sâu (Advanced / Specialized)** tại các nhóm chủ đề cùng tên ở cấp `computer_science/`: đi sâu vào cơ chế bên trong (internals), chứng minh, cách triển khai, hành vi trong hệ thống thực tế, kiểu lỗi và các đánh đổi ở mức kỹ sư nhiều kinh nghiệm.

“Nền tảng” không có nghĩa là sơ sài. Đây là lớp kiến thức tiên quyết (prerequisite) chung. Phần nâng cao không lặp lại toàn bộ kiến thức nền mà dựa trên những giả định đã được giải thích để đào sâu hơn.

Xem [quy ước ngôn ngữ](./LANGUAGE_STYLE.md) để hiểu cách thư viện ưu tiên tiếng Việt và giữ thuật ngữ tiếng Anh trong ngoặc khi cần.

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

## Cách học

Không cần học hết phần nền tảng rồi mới đọc phần nâng cao. Cách hợp lý hơn là đọc chương nền tảng tương ứng để có vốn thuật ngữ và hiểu cơ chế chính, sau đó chuyển sang phần nâng cao khi cần hiểu cơ chế bên trong, chứng minh, hiệu năng, kiểu lỗi hoặc thiết kế cho hệ thống thực tế.

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

Route này phù hợp khi muốn hiểu vì sao cùng một đoạn code có thể chậm hoặc sai vì nguyên nhân ở tầng thấp hơn. Nên đọc lần lượt các phần Architecture → OS → Programming Languages & Runtime → Software Systems → Networks & Distributed Systems, rồi quay lại [`90_connections/advanced`](./90_connections/advanced/README.md) để nối các tầng bằng symptom thực tế.

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

Route này giúp phân biệt data race, logical race, thread scheduling, memory reordering và distributed ordering. Không nên dùng từ “concurrent” như một khái niệm duy nhất cho mọi tầng.

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

Một chapter nâng cao không được giả định người đọc đã hiểu sâu thuật ngữ hệ thống chỉ vì thuật ngữ đó phổ biến. Khi lần đầu dùng các khái niệm như `process`, `thread`, `virtual memory`, `syscall`, `cache`, `WAL`, `MVCC`, `consensus`, `idempotency`, chapter phải hoặc giải thích bản chất ngắn gọn trước, hoặc link trực tiếp đến chapter nền tảng chứa định nghĩa và mental model.

Mỗi chapter nâng cao nên trả lời được bốn lớp câu hỏi:

```text
1. Concept tồn tại để giải bài toán gì?
2. Internals duy trì invariant bằng cơ chế nào?
3. Khi failure/performance pressure xuất hiện thì nó hỏng hoặc chậm ra sao?
4. Nó phụ thuộc và tác động các tầng khác thế nào?
```

Nếu một nội dung chỉ liệt kê API hoặc công nghệ mà không tạo thêm mental model, nó không nên trở thành chapter riêng trong Computer Science Library.

## Nguyên tắc audit coverage

Coverage được xem là đủ khi domain đã có đường reasoning từ foundation → internals → failure modes → performance/concurrency/consistency → production evidence. Không tăng số chapter chỉ để làm roadmap dài hơn.

Khi audit một domain, ưu tiên tìm:

- chapter quá mỏng, chỉ định nghĩa mà chưa giải thích mechanism;
- dependency ẩn khiến người mới không hiểu thuật ngữ đang được dùng;
- thiếu failure matrix hoặc edge cases;
- thiếu connection tới hardware/OS/runtime/network khi connection đó quyết định behavior;
- thiếu cách quan sát thực tế như metric, trace, execution plan, GC log, wait event hoặc kernel evidence;
- duplicate giữa các domain có thể thay bằng cross-link.

Cấu trúc dữ liệu và thuật toán (DSA) đã có phần nâng cao riêng theo cùng mô hình và đi sâu vào implementation bằng C, Java và JavaScript. Các domain khác tiếp tục được cải thiện trong chính `computer_science/`, không tách thêm root library nếu conceptual boundary đã được bao phủ ở đây.

## Nguyên tắc biên soạn phần nâng cao

Một chương nâng cao phải đào sâu hơn phần nền tảng ở ít nhất một hướng: cơ chế bên trong; bất biến hoặc chứng minh hình thức; mô hình hiệu năng; ngữ nghĩa đồng thời và lỗi; chiến lược triển khai; khả năng quan sát và gỡ lỗi; đánh đổi trong môi trường thực tế; hoặc tương tác giữa nhiều tầng trừu tượng. Không thêm một chương chỉ vì một công nghệ đang phổ biến nếu nó không tạo ra mô hình tư duy mới.