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

## Thư viện AI chuyên sâu

Ngoài tuyến `basic/10_ai_foundations → 10_ai_foundations/advanced`, repository có một thư viện chuyên sâu riêng về AI:

**[Artificial Intelligence Knowledge Library](./02_artificial_intelligence/README.md)**

Thư viện này đi theo quan hệ phụ thuộc khái niệm và mở rộng từ Transformer, LLM, Retrieval/Vector Search, RAG, Tool Calling và Agents tới Evaluation, AI Engineering, LLMOps, Reliability và Security. Nó bổ sung chiều sâu theo domain, không thay thế lớp AI Foundations dùng chung của Computer Science.

## Cách học

Không cần học hết phần nền tảng rồi mới đọc phần nâng cao. Cách hợp lý hơn là đọc chương nền tảng tương ứng để có vốn thuật ngữ và hiểu cơ chế chính, sau đó chuyển sang phần nâng cao khi cần hiểu cơ chế bên trong, chứng minh, hiệu năng, kiểu lỗi hoặc thiết kế cho hệ thống thực tế.

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

Cấu trúc dữ liệu và thuật toán (DSA) đã có thư viện nâng cao riêng theo cùng mô hình và tiếp tục đi sâu vào cách triển khai bằng C, Java và JavaScript. Các lĩnh vực nâng cao còn lại được mở rộng theo lộ trình trong từng `advanced/README.md`.

## Nguyên tắc biên soạn phần nâng cao

Một chương nâng cao phải đào sâu hơn phần nền tảng ở ít nhất một hướng: cơ chế bên trong; bất biến hoặc chứng minh hình thức; mô hình hiệu năng; ngữ nghĩa đồng thời và lỗi; chiến lược triển khai; khả năng quan sát và gỡ lỗi; đánh đổi trong môi trường thực tế; hoặc tương tác giữa nhiều tầng trừu tượng. Không thêm một chương chỉ vì một công nghệ đang phổ biến nếu nó không tạo ra mô hình tư duy mới.