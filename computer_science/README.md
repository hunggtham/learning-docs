# Thư viện kiến thức Khoa học máy tính

> **Mạch đọc:** Đọc **Thư viện kiến thức Khoa học máy tính** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Bản đồ Nền tảng → Nâng cao** sang **Thư viện AI chuyên sâu**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


`computer_science/` được tổ chức thành hai lớp kiến thức rõ ràng:

- **Nền tảng (Basic / Foundation / 기초)** tại [`basic/`](./basic/README.md): xây dựng các mô hình tư duy cốt lõi của khoa học máy tính (computer science / 컴퓨터 과학).
- **Nâng cao và chuyên sâu (Advanced / Specialized)** tại các nhóm chủ đề cùng tên ở cấp `computer_science/`: đi sâu vào cơ chế bên trong (internals), bất biến (invariant / 불변식), hành vi khi có thất bại (failure / 실패) hoặc pressure, cách quan sát môi trường vận hành (production / 운영 환경) và các đánh đổi ở mức kỹ sư nhiều kinh nghiệm.

“Nền tảng” không có nghĩa là sơ sài. Đây là lớp kiến thức tiên quyết (prerequisite) chung. Phần nâng cao không lặp lại toàn bộ kiến thức nền mà dựa trên những giả định đã được giải thích để đào sâu hơn.

Xem [quy ước ngôn ngữ](./LANGUAGE_STYLE.md) để hiểu cách thư viện ưu tiên tiếng Việt và giữ thuật ngữ tiếng Anh trong ngoặc khi cần. Xem [Coverage Audit](./COVERAGE_AUDIT.md) để biết lĩnh vực (domain / 도메인) nào đang mạnh, gap nào còn lại và quy tắc maintenance hiện tại.

## Bản đồ Nền tảng → Nâng cao

Bảng này giải thích cách hai lớp của thư viện nối với nhau: nền tảng dựng mô hình chung, còn phần nâng cao mở rộng cơ chế, failure mode và trade-off. Hãy dùng nó để chọn đúng prerequisite thay vì coi “advanced” là một danh sách rời.

| Lĩnh vực | Nền tảng | Nâng cao |
|---|---|---|
| Tính toán & Thông tin (Computation & information) | [`basic/00_computation_information`](./basic/00_computation_information/) | [`00_computation_information/advanced`](./00_computation_information/advanced/README.md) |
| Thuật toán & Cấu trúc dữ liệu (Algorithms & data Structures) | [`basic/01_algorithms_data_structures`](./basic/01_algorithms_data_structures/) | [`01_algorithms_data_structures/advanced`](./01_algorithms_data_structures/advanced/README.md) |
| Kiến trúc máy tính (Computer architecture) | [`basic/02_computer_architecture`](./basic/02_computer_architecture/) | [`02_computer_architecture/advanced`](./02_computer_architecture/advanced/README.md) |
| Hệ điều hành (Operating Systems) | [`basic/03_operating_systems`](./basic/03_operating_systems/) | [`03_operating_systems/advanced`](./03_operating_systems/advanced/README.md) |
| Ngôn ngữ lập trình & Môi trường thực thi (Programming Languages & runtime) | [`basic/04_programming_languages`](./basic/04_programming_languages/) | [`04_programming_languages/advanced`](./04_programming_languages/advanced/README.md) |
| Dữ liệu & Cơ sở dữ liệu (data & Databases) | [`basic/05_data_databases`](./basic/05_data_databases/) | [`05_data_databases/advanced`](./05_data_databases/advanced/README.md) |
| Mạng & Hệ thống phân tán (Networks & Distributed Systems) | [`basic/06_networks_distributed_systems`](./basic/06_networks_distributed_systems/) | [`06_networks_distributed_systems/advanced`](./06_networks_distributed_systems/advanced/README.md) |
| Bảo mật & Độ tin cậy (security & reliability) | [`basic/07_security_reliability`](./basic/07_security_reliability/) | [`07_security_reliability/advanced`](./07_security_reliability/advanced/README.md) |
| Hệ thống phần mềm (Software Systems) | [`basic/08_software_systems`](./basic/08_software_systems/) | [`08_software_systems/advanced`](./08_software_systems/advanced/README.md) |
| kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) | [`basic/09_software_engineering`](./basic/09_software_engineering/) | [`09_software_engineering/advanced`](./09_software_engineering/advanced/README.md) |
| Nền tảng Trí tuệ nhân tạo (AI Foundations) | [`basic/10_ai_foundations`](./basic/10_ai_foundations/) | [`10_ai_foundations/advanced`](./10_ai_foundations/advanced/README.md) |
| Tương tác người–máy & Đồ họa (HCI & Graphics) | [`basic/11_hci_graphics`](./basic/11_hci_graphics/) | [`11_hci_graphics/advanced`](./11_hci_graphics/advanced/README.md) |
| Xã hội, Đạo đức & Nghề nghiệp | [`basic/12_society_ethics_profession`](./basic/12_society_ethics_profession/) | [`12_society_ethics_profession/advanced`](./12_society_ethics_profession/advanced/README.md) |
| Kết nối xuyên lĩnh vực | [`basic/90_connections`](./basic/90_connections/) | [`90_connections/advanced`](./90_connections/advanced/README.md) |


> **Chuyển mạch:** Từ **Bản đồ Nền tảng → Nâng cao**, ta sang **Thư viện AI chuyên sâu** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thư viện AI chuyên sâu

Ngoài tuyến `basic/10_ai_foundations → 10_ai_foundations/advanced`, repository có một thư viện chuyên sâu riêng về AI:

**[Artificial Intelligence Knowledge Library](./02_artificial_intelligence/README.md)**

Thư viện này đi theo quan hệ phụ thuộc khái niệm và mở rộng từ Transformer, LLM, Retrieval/véc-tơ (vector / 벡터) tìm kiếm (search / 검색), RAG, công cụ (tool / 도구) Calling và Agents tới Evaluation, AI kỹ thuật (engineering / 엔지니어링), LLMOps, độ tin cậy (reliability / 신뢰성) và bảo mật (security / 보안). Nó bổ sung chiều sâu theo lĩnh vực (domain / 도메인), không thay thế lớp AI Foundations dùng chung của Khoa học máy tính (computer science / 컴퓨터 과학).

> **Naming ghi chú (note / 노트):** `02_artificial_intelligence/` là thư viện AI chuyên sâu, `02_computer_architecture/` là Computer kiến trúc (architecture / 아키텍처), còn `10_ai_foundations/` là tuyến AI foundations nằm trong bản đồ CS. README giữ ranh giới (boundary / 경계) rõ ràng; numbering hiện tại vẫn có thể gây nhầm khi nhìn cây (tree / 트리) trực tiếp và chỉ nên đổi trong một di chuyển (migration / 마이그레이션) có kế hoạch.


> **Chuyển mạch:** Từ **Thư viện AI chuyên sâu**, ta sang **Cách học** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách học

Không cần học hết phần nền tảng rồi mới đọc phần nâng cao. Cách hợp lý hơn là đọc chapter nền tảng tương ứng để có vocabulary và mô hình tư duy (mental model / 사고 모델) chính, sau đó chuyển sang phần nâng cao khi cần hiểu internals, bất biến (invariant / 불변식), hành vi khi thất bại (failure behavior / 실패 동작), hiệu năng (performance / 성능) hoặc bằng chứng vận hành (production evidence / 운영 증거).

### Học tập (learning / 학습) tuyến (route / 경로) 1 — từ phần cứng đến ứng dụng (application / 애플리케이션)

Route này đi từ nguyên nhân ở tầng thấp tới biểu hiện ở application. Mỗi mũi tên là một điểm cần kiểm tra khi hiệu năng hoặc hành vi chương trình không thể giải thích chỉ bằng code bề mặt.

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

Tuyến (route / 경로) này phù hợp khi muốn hiểu vì sao cùng một đoạn mã (code / 코드) có thể chậm hoặc sai vì nguyên nhân ở tầng thấp hơn. Nên đọc lần lượt kiến trúc (architecture / 아키텍처) → OS → Programming Languages & thời gian chạy (runtime / 런타임) → Software các hệ thống (systems / 시스템들) → Networks & phân tán (distributed / 분산) các hệ thống (systems / 시스템들), rồi quay lại [`90_connections/advanced`](./90_connections/advanced/README.md) để nối các tầng bằng symptom thực tế.

### Học tập (learning / 학습) tuyến (route / 경로) 2 — durability và consistency

Route này theo dõi một thay đổi dữ liệu từ transaction tới device và replica. Nó giúp người học hiểu commit ở một tầng chưa chắc đồng nghĩa dữ liệu đã bền vững ở mọi tầng.

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

Tuyến (route / 경로) này dùng cho backend/cơ sở dữ liệu (database / 데이터베이스) kỹ thuật (engineering / 엔지니어링). Bắt đầu từ nền tảng giao dịch (transaction / 트랜잭션) rồi đọc cơ sở dữ liệu (database / 데이터베이스) Advanced, OS filesystem/I/O, phân tán (distributed / 분산) các hệ thống (systems / 시스템들) và chapter [durability xuyên tầng](./90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

### Học tập (learning / 학습) tuyến (route / 경로) 3 — tính đồng thời (concurrency / 동시성) và thứ tự (ordering / 순서)

Đường đọc này nối các nghĩa khác nhau của “thứ tự” từ memory model tới distributed system. Hãy giữ câu hỏi dữ liệu có thể quan sát ở thời điểm nào trước khi chọn cơ chế đồng bộ.

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

Tuyến (route / 경로) này giúp phân biệt dữ liệu (data / 데이터) race, logical race, luồng thực thi (thread / 스레드) scheduling, bộ nhớ (memory / 메모리) reordering và phân tán (distributed / 분산) thứ tự (ordering / 순서). Không dùng từ “concurrent” như một khái niệm duy nhất cho mọi tầng.

### Học tập (learning / 학습) tuyến (route / 경로) 4 — độ tin cậy (reliability / 신뢰성) và ranh giới bảo mật (security boundary / 보안 경계)

Route cuối đặt security và reliability trên cùng một chuỗi boundary–dependency. Một control có thể giảm rủi ro tấn công nhưng đồng thời tạo dependency availability, nên cần đọc cả hai chiều.

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

Tuyến (route / 경로) này nối bảo mật (security / 보안) với độ tin cậy (reliability / 신뢰성) thay vì coi chúng là hai môn rời rạc. Một điều khiển (control / 제어) bảo mật có thể tạo phụ thuộc (dependency / 의존성) availability; một thử lại (retry / 재시도) chính sách (policy / 정책) độ tin cậy (reliability / 신뢰성) có thể trở thành abuse amplifier nếu thiếu tỷ lệ (rate / 비율) limit hoặc idempotency.


> **Chuyển mạch:** Từ **Cách học**, ta sang **Quy tắc phụ thuộc (dependency / 의존성) trong chapter nâng cao** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quy tắc phụ thuộc (dependency / 의존성) trong chapter nâng cao

Một chapter nâng cao không được giả định người đọc đã hiểu sâu thuật ngữ hệ thống chỉ vì thuật ngữ đó phổ biến. Khi lần đầu dùng các khái niệm như `process`, `thread`, `virtual memory`, `syscall`, `cache`, `WAL`, `MVCC`, `consensus`, `idempotency`, chapter phải giải thích bản chất ngắn gọn hoặc link trực tiếp tới foundation chứa mô hình tư duy (mental model / 사고 모델) đó.

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

Không cần ép mọi chapter thành template cứng, nhưng nếu một phần advanced không tạo thêm khả năng lập luận (reasoning / 추론) theo các câu hỏi trên thì chưa đủ lý do để tồn tại như một chapter riêng.


> **Chuyển mạch:** Từ **Quy tắc phụ thuộc (dependency / 의존성) trong chapter nâng cao**, ta sang **Nguyên tắc kiểm tra (audit / 감사) coverage** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nguyên tắc kiểm tra (audit / 감사) coverage

Coverage được xem là đủ khi lĩnh vực (domain / 도메인) có đường lập luận (reasoning / 추론):

```text
foundation
→ internals
→ failure modes
→ performance / concurrency / consistency
→ production evidence
→ cross-layer connections
```

Không tăng số chapter chỉ để làm roadmap dài hơn. Khi kiểm tra (audit / 감사) một lĩnh vực (domain / 도메인), ưu tiên tìm chapter quá mỏng; phụ thuộc (dependency / 의존성) ẩn; giả định (assumption / 가정) chưa nói rõ; thất bại (failure / 실패)/trường hợp biên (edge case / 경계 사례) còn thiếu; liên kết (connection / 연결) tới lower tầng (layer / 계층) quyết định hành vi (behavior / 동작); bằng chứng (evidence / 증거) môi trường vận hành (production / 운영 환경) còn thiếu; và duplicate có thể thay bằng cross-link.

Bằng chứng vận hành (production evidence / 운영 증거) có thể là chỉ số (metric / 지표), dấu vết (trace / 추적), thực thi (execution / 실행) plan, GC log, wait sự kiện (event / 이벤트), scheduler bằng chứng (evidence / 증거), PMU counter, replication position hoặc state-transition bằng chứng (evidence / 증거) tùy lĩnh vực (domain / 도메인). Mục tiêu không phải thêm công cụ (tool / 도구) name, mà giúp người đọc biết **cần quan sát tín hiệu nào để kiểm chứng cơ chế (mechanism / 메커니즘)**.

Cấu trúc dữ liệu và thuật toán (DSA) đã có phần nâng cao riêng theo cùng mô hình và đi sâu vào hiện thực (implementation / 구현) bằng C, Java và JavaScript. Các lĩnh vực (domain / 도메인) khác tiếp tục được cải thiện trong chính `computer_science/`, không tách mạng (network / 네트워크), phân tán (distributed / 분산) các hệ thống (systems / 시스템들), bảo mật (security / 보안), độ tin cậy (reliability / 신뢰성), hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링), tính đồng thời (concurrency / 동시성) hoặc hệ thống (system / 시스템) thiết kế (design / 설계) thành gốc (root / 루트) thư viện (library / 라이브러리) mới nếu conceptual ranh giới (boundary / 경계) hiện tại đã đủ.


> **Chuyển mạch:** Từ **Nguyên tắc kiểm tra (audit / 감사) coverage**, ta sang **Nguyên tắc biên soạn phần nâng cao** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nguyên tắc biên soạn phần nâng cao

Một chương nâng cao phải đào sâu hơn phần nền tảng ở ít nhất một hướng: cơ chế bên trong; bất biến hoặc chứng minh hình thức; mô hình hiệu năng; ngữ nghĩa đồng thời và lỗi; chiến lược triển khai; khả năng quan sát và gỡ lỗi; đánh đổi trong môi trường thực tế; hoặc tương tác giữa nhiều tầng trừu tượng. Không thêm một chương chỉ vì một công nghệ đang phổ biến nếu nó không tạo ra mô hình tư duy mới.
