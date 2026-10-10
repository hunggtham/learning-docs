# 정보처리기사 필기 2026 — High-Risk Confusion Atlas

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **정보처리기사 필기 2026 — High-Risk Confusion Atlas**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1.1 xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **1.2 Functional vs Non-functional yêu cầu (requirement / 요구사항)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối confusion atlas với verification, validation và requirement types, để lỗi khái niệm được tách bằng tiêu chí.

> Mục tiêu của tệp (file / 파일) này là xử lý nhóm câu hỏi khó nhất: **các đáp án đều nghe có vẻ đúng** nhưng chỉ một đáp án khớp chính xác với cơ chế, tầng (layer / 계층) hoặc từ khóa của câu hỏi. Không học tệp (file / 파일) này như flashcard. Với mỗi pair, phải trả lời được: *ranh giới nằm ở đâu, dấu hiệu đề bài là gì, và khi nào cả hai cùng xuất hiện nhưng một cái vẫn là đáp án tốt hơn?*

---

# 1. Môn 1 — 소프트웨어 설계

## 1.1 xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증)

**xác minh (verification / 확인) — 검증** hỏi: sản phẩm/thiết kế (design / 설계)/mã (code / 코드) có được xây đúng theo specification không?

**kiểm tra hợp lệ (validation / 검증) — 확인/타당성 확인** hỏi: specification/sản phẩm có thực sự giải quyết nhu cầu stakeholder không?

### Dấu hiệu đề

- “conforms to specification”, “built correctly” → xác minh (verification / 확인).
- “meets người dùng (user / 사용자) needs”, “right sản phẩm (product / 제품)” → kiểm tra hợp lệ (validation / 검증).

### Bẫy

Một hệ thống (system / 시스템) có thể xác minh (verification / 확인) tốt nhưng kiểm tra hợp lệ (validation / 검증) thất bại: mã (code / 코드) đúng spec, nhưng spec sai nhu cầu thật.

---

> **Nối mạch:** Sau khi phân biệt **1.1 xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증)** bằng câu hỏi “đúng đặc tả hay đúng nhu cầu”, chuyển sang **1.2 Functional vs Non-functional yêu cầu (requirement / 요구사항)** để xem yêu cầu được mô tả theo hành vi hay theo ràng buộc chất lượng.

## 1.2 Functional vs Non-functional yêu cầu (requirement / 요구사항)

**Functional yêu cầu (requirement / 요구사항) — 기능 요구사항** mô tả năng lực (capability / 역량)/nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작).

**Non-functional yêu cầu (requirement / 요구사항) — 비기능 요구사항** mô tả chất lượng (quality / 품질), ràng buộc (constraint / 제약조건) hoặc operating điều kiện (condition / 조건).

### Dấu hiệu đề

`User can export report` → functional.

`Report must finish within 3 seconds for 5,000 concurrent users` → non-functional.

### Bẫy

Câu có động từ chưa chắc functional. Nếu năng lực (capability / 역량) vẫn tồn tại khi bỏ ràng buộc (constraint / 제약조건) thì ràng buộc (constraint / 제약조건) nhiều khả năng non-functional.

---

> **Nối mạch:** Khi đã biết một yêu cầu nói về năng lực hay ràng buộc, hãy chuyển sang **1.3 DFD vs Flowchart** để tách luồng dữ liệu khỏi luồng điều khiển; tiêu chí đó chuẩn bị cho việc đọc các sơ đồ tương tác tiếp theo.

## 1.3 DFD vs Flowchart

**DFD** tập trung dữ liệu (data / 데이터) movement và transformation giữa tiến trình (process / 프로세스), dữ liệu (data / 데이터) store và bên ngoài (external / 외부) thực thể (entity / 엔터티).

**Flowchart** tập trung điều khiển (control / 제어) luồng (flow / 흐름) và chuỗi (sequence / 시퀀스) của step/quyết định (decision / 결정).

### Bẫy

Cả hai đều có “mũi tên” và “tiến trình (process / 프로세스)”. Hãy hỏi arrow biểu diễn **dữ liệu (data / 데이터)** hay **điều khiển (control / 제어)**.

---

> **Nối mạch:** **1.3 DFD vs Flowchart** vừa tách dữ liệu khỏi điều khiển; **1.4 chuỗi (sequence / 시퀀스) Diagram vs Activity Diagram** tiếp tục tách thông điệp theo thời gian khỏi workflow và nhánh xử lý.

## 1.4 chuỗi (sequence / 시퀀스) Diagram vs Activity Diagram

**chuỗi (sequence / 시퀀스) Diagram**: message giữa đối tượng (object / 객체)/thành phần (component / 컴포넌트) theo trục thời gian.

**Activity Diagram**: workflow, branch, merge, parallel activity.

### Dấu hiệu đề

- “message thứ tự (order / 순서) between objects” → chuỗi (sequence / 시퀀스).
- “nghiệp vụ (business / 비즈니스) workflow / parallel branch” → Activity.

---

> **Nối mạch:** Sau khi phân biệt sơ đồ mô tả thông điệp với sơ đồ mô tả workflow, chuyển sang **1.5 Aggregation vs Composition** để hỏi quan hệ whole–part có sở hữu vòng đời hay không.

## 1.5 Aggregation vs Composition

**Aggregation**: whole–part yếu; part có thể tồn tại độc lập.

**Composition**: quyền sở hữu (ownership / 소유권)/vòng đời (lifecycle / 생명주기) mạnh; part phụ thuộc whole.

### Dấu hiệu đề

Nếu xóa whole và part cũng mất về ngữ nghĩa (semantic / 의미적) → composition.

---

> **Nối mạch:** **1.5 Aggregation vs Composition** đã xác định mức gắn kết giữa whole và part; **1.6 Cohesion vs Coupling** mở rộng câu hỏi đó vào chất lượng bên trong một module và mức phụ thuộc giữa các module.

## 1.6 Cohesion vs Coupling

**Cohesion — 응집도** nhìn **bên trong một mô-đun (module / 모듈)**: các phần tử có phục vụ cùng purpose không?

**Coupling — 결합도** nhìn **giữa các mô-đun (module / 모듈)**: mức phụ thuộc lẫn nhau.

### Bẫy

“High cohesion” và “low coupling” thường cùng là mục tiêu nhưng không đồng nghĩa.

---

> **Nối mạch:** Từ phân biệt “gắn kết bên trong” và “phụ thuộc bên ngoài” ở **1.6 Cohesion vs Coupling**, chuyển sang **1.7 dữ liệu (data / 데이터) Coupling vs Stamp Coupling** để nhận diện mức dữ liệu thực sự được truyền qua lời gọi.

## 1.7 dữ liệu (data / 데이터) Coupling vs Stamp Coupling

**dữ liệu (data / 데이터) Coupling**: chỉ truyền đúng dữ liệu cần thiết.

**Stamp Coupling**: truyền cả cấu trúc (structure / 구조)/đối tượng (object / 객체) lớn hơn nhu cầu thật.

### Scenario

`send(customerId)` → dữ liệu (data / 데이터) Coupling.

`send(Customer customer)` nhưng callee chỉ dùng `customer.id` → Stamp Coupling.

---

> **Nối mạch:** **1.7 dữ liệu (data / 데이터) Coupling vs Stamp Coupling** hỏi “truyền đúng dữ liệu hay cả cấu trúc”; **1.8 điều khiển (control / 제어) Coupling vs dữ liệu (data / 데이터) Coupling** hỏi thêm liệu tham số có điều khiển nhánh nội bộ hay chỉ mang giá trị.

## 1.8 điều khiển (control / 제어) Coupling vs dữ liệu (data / 데이터) Coupling

Nếu parameter chỉ là dữ liệu nghiệp vụ → dữ liệu (data / 데이터) Coupling.

Nếu parameter/flag quyết định branch nội bộ của mô-đun (module / 모듈) khác → điều khiển (control / 제어) Coupling.

```text
process(order)             → data-oriented
process(order, mode='X')   → có thể control coupling nếu mode điều khiển path nội bộ
```

---

> **Nối mạch:** Sau khi phân biệt tham số dữ liệu với tham số điều khiển ở **1.8**, chuyển sang **1.9 SRP vs ISP** để tách hai loại áp lực thiết kế: lý do một module thay đổi và interface buộc client phụ thuộc.

## 1.9 SRP vs ISP

**SRP** hỏi một lớp (class / 클래스)/mô-đun (module / 모듈) có quá nhiều **reason to thay đổi (change / 변경)** không.

**ISP** hỏi máy khách (client / 클라이언트) có bị buộc phụ thuộc vào **giao diện (interface / 인터페이스) phương thức (method / 메서드) không dùng** không.

Lớp (class / 클래스) vừa gửi mail, lưu DB, generate PDF → SRP.

Giao diện (interface / 인터페이스) 25 methods nhưng một máy khách (client / 클라이언트) chỉ cần 2 → ISP.

---

> **Nối mạch:** **1.9 SRP vs ISP** đã tách trách nhiệm thay đổi khỏi bề rộng interface; **1.10 OCP vs DIP** chuyển sang câu hỏi về khả năng mở rộng và hướng phụ thuộc giữa chính sách với hiện thực.

## 1.10 OCP vs DIP

**OCP**: mở rộng hành vi (behavior / 동작) mà giảm sửa mã (code / 코드) ổn định.

**DIP**: high-level chính sách (policy / 정책) không phụ thuộc trực tiếp low-level hiện thực (implementation / 구현); cả hai dựa lớp trừu tượng (abstraction / 추상화).

Phụ thuộc (dependency / 의존성) Injection thường giúp DIP nhưng không tự động chứng minh OCP.

---

> **Nối mạch:** Từ mục tiêu mở rộng và đảo chiều phụ thuộc ở **1.10 OCP vs DIP**, chuyển sang **1.11 chiến lược (strategy / 전략) vs trạng thái (state / 상태)** để nhận diện hành vi đổi vì thuật toán được chọn hay vì trạng thái nội bộ.

## 1.11 chiến lược (strategy / 전략) vs trạng thái (state / 상태)

Cấu trúc lớp (class / 클래스) có thể rất giống nhau.

**chiến lược (strategy / 전략)**: thuật toán (algorithm / 알고리즘)/chính sách (policy / 정책) được chọn hoặc thay thế.

**trạng thái (state / 상태)**: hành vi (behavior / 동작) thay đổi vì đối tượng (object / 객체) đang ở trạng thái nội bộ (internal state / 내부 상태) khác.

`DiscountPolicy` → chiến lược (strategy / 전략).

`OrderState: PAID → SHIPPED → CANCELLED` → trạng thái (state / 상태).

---

> **Nối mạch:** **1.11 chiến lược (strategy / 전략) vs trạng thái (state / 상태)** vừa phân biệt nguồn của hành vi; **1.12 Adapter vs Facade** đổi trọng tâm sang mục đích của lớp trung gian: sửa lệch interface hay đơn giản hóa subsystem.

## 1.12 Adapter vs Facade

**Adapter** giải quyết **giao diện (interface / 인터페이스) mismatch**.

**Facade** giải quyết **subsystem độ phức tạp (complexity / 복잡도)** bằng một mặt tiền đơn giản.

Nếu đề nói “legacy API không tương thích” → Adapter.

Nếu nói “máy khách (client / 클라이언트) phải gọi 7 subsystem và cần API đơn giản” → Facade.

---

> **Nối mạch:** Sau khi phân biệt adapter sửa tương thích và facade giảm độ phức tạp, chuyển sang **1.13 Decorator vs Proxy** để hỏi wrapper đang thêm trách nhiệm hay kiểm soát truy cập.

## 1.13 Decorator vs Proxy

Cả hai đều thường wrap đối tượng (object / 객체).

**Decorator** thêm hành vi (behavior / 동작)/responsibility động.

**Proxy** kiểm soát/đại diện truy cập tới đối tượng (object / 객체) thật: lazy, remote, protection, caching tùy loại.

Hỏi: wrapper nhằm **thêm chức năng** hay **kiểm soát truy cập (access / 접근)**?

---

> **Nối mạch:** **1.13 Decorator vs Proxy** kết thúc nhóm wrapper bằng tiêu chí “thêm chức năng hay kiểm soát truy cập”; **1.14 Factory phương thức (method / 메서드) vs Abstract Factory** chuyển sang quy mô của việc tạo sản phẩm.

## 1.14 Factory phương thức (method / 메서드) vs Abstract Factory

**Factory phương thức (method / 메서드)** tập trung phương thức (method / 메서드) tạo một loại sản phẩm (product / 제품), thường cho subclass/hiện thực (implementation / 구현) quyết định concrete kiểu (type / 타입).

**Abstract Factory** tạo **một họ các đối tượng (object / 객체) liên quan** mà máy khách (client / 클라이언트) không cần biết concrete classes.

---

> **Nối mạch:** Sau khi tách factory tạo một sản phẩm khỏi factory tạo cả họ sản phẩm, **1.15 Wireframe vs Mockup vs Prototype** đưa cùng thói quen phân biệt theo mức độ tương tác vào artefact thiết kế; từ đó chuyển sang cấu trúc dữ liệu của Môn 2.

## 1.15 Wireframe vs Mockup vs Prototype

Wireframe → skeleton/bố cục (layout / 레이아웃).

Mockup → hình thức trực quan gần sản phẩm.

Prototype → tương tác (interaction / 상호작용)/luồng (flow / 흐름) thử nghiệm.

Câu hỏi “kiểm thử (test / 테스트) tương tác (interaction / 상호작용) trước hiện thực (implementation / 구현)” thường nghiêng Prototype hơn Mockup.

---

# 2. Môn 2 — 소프트웨어 개발

> **Nối mạch:** Từ mức độ tương tác của prototype, chuyển sang **2.1 ngăn xếp (stack / 스택) vs hàng đợi (queue / 큐)** để phân biệt hai quy tắc lấy phần tử: LIFO và FIFO; đó là nền cho cách duyệt đồ thị ở mục sau.

## 2.1 ngăn xếp (stack / 스택) vs hàng đợi (queue / 큐)

Ngăn xếp (stack / 스택) → LIFO.

Hàng đợi (queue / 큐) → FIFO.

Không chỉ nhớ acronym: hãy dấu vết (trace / 추적) push/pop hoặc enqueue/dequeue.

---

> **Nối mạch:** **2.1 ngăn xếp (stack / 스택) vs hàng đợi (queue / 큐)** cung cấp cơ chế lưu vết; **2.2 BFS vs DFS** dùng hàng đợi hoặc ngăn xếp để tạo thứ tự duyệt khác nhau, rồi bàn giao sang cấu trúc cây.

## 2.2 BFS vs DFS

BFS dùng frontier FIFO và khám phá theo tầng (layer / 계층); đồ thị (graph / 그래프) unweighted cho shortest đường dẫn (path / 경로) theo số cạnh.

DFS đi sâu trước; mạnh trong traversal, connectivity, cycle/topological lập luận (reasoning / 추론) nhưng không tự bảo đảm shortest đường dẫn (path / 경로) unweighted.

---

> **Nối mạch:** Sau khi thấy thứ tự duyệt thay đổi theo cấu trúc lưu vết, **2.3 BST vs vùng nhớ động (heap / 힙)** tách hai mục tiêu thường bị nhầm: tìm kiếm theo thứ tự khóa và giữ phần tử ưu tiên.

## 2.3 BST vs vùng nhớ động (heap / 힙)

**BST** duy trì thứ tự (ordering / 순서) quan hệ (relation / 관계) giữa left/gốc (root / 루트)/right; inorder cho sorted thứ tự (order / 순서) nếu key phù hợp.

**vùng nhớ động (heap / 힙)** chỉ bảo đảm parent-child vùng nhớ động (heap / 힙) thuộc tính (property / 속성); không tạo globally sorted traversal.

Min-heap lấy minimum hiệu quả nhưng tìm kiếm (search / 검색) arbitrary key không giống BST.

---

> **Nối mạch:** **2.3 BST vs vùng nhớ động (heap / 힙)** đã tách thứ tự khóa khỏi ưu tiên; **2.4 tìm kiếm nhị phân (binary search / 이진 탐색) vs băm (hash / 해시) Lookup** tiếp tục hỏi dữ liệu được tìm nhờ thứ tự hay nhờ hàm băm.

## 2.4 tìm kiếm nhị phân (binary search / 이진 탐색) vs băm (hash / 해시) Lookup

Tìm kiếm nhị phân (binary search / 이진 탐색) cần ordered cấu trúc (structure / 구조) và O(log n) comparison tìm kiếm (search / 검색).

Băm (hash / 해시) lookup average-case có thể gần O(1), nhưng không tự hỗ trợ ordered/phạm vi (range / 범위) ngữ nghĩa (semantics / 의미론).

---

> **Nối mạch:** Sau khi phân biệt lookup dựa trên thứ tự với lookup dựa trên hash, **2.5 Quick Sort vs Merge Sort** chuyển sang bài toán sắp xếp và cách mỗi thuật toán đánh đổi pivot, bộ nhớ và tính ổn định.

## 2.5 Quick Sort vs Merge Sort

Quick Sort thường in-place-ish với partition và average O(n log n), nhưng worst O(n²).

Merge Sort worst O(n log n), stable trong hiện thực (implementation / 구현) điển hình nhưng cần extra bộ nhớ (memory / 메모리) cho array merge.

Đề hỏi worst-case → đừng chọn theo average reputation.

---

> **Nối mạch:** **2.5 Quick Sort vs Merge Sort** kết thúc nhóm thuật toán bằng cách đọc theo điều kiện và chi phí; **2.6 Stub vs Driver** áp dụng cách hỏi đó vào thành phần giả lập: bên cung cấp lời gọi hay bên gọi thành phần.

## 2.6 Stub vs Driver

Top-down tích hợp (integration / 통합) → thiếu lower mô-đun (module / 모듈) → **Stub**.

Bottom-up tích hợp (integration / 통합) → thiếu upper caller → **Driver**.

Mô hình tư duy (mental model / 사고 모델): stub giả người **bị gọi**; driver giả người **đi gọi**.

---

> **Nối mạch:** Sau khi biết stub và driver đứng ở hai phía khác nhau của lời gọi kiểm thử, **2.7 Black-box vs White-box** chuyển trọng tâm sang nguồn quan sát: chỉ nhìn đầu vào–đầu ra hay theo dõi cấu trúc bên trong.

## 2.7 Black-box vs White-box

Black-box nhìn đầu vào (input / 입력)/đầu ra (output / 출력) theo specification, không cần nội bộ (internal / 내부) cấu trúc (structure / 구조).

White-box dùng nội bộ (internal / 내부) điều khiển (control / 제어)/cấu trúc dữ liệu (data structure / 자료구조) của mã (code / 코드).

Ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석) → black-box.

Statement/Branch/đường dẫn (path / 경로) Coverage → white-box.

---

> **Nối mạch:** **2.7 Black-box vs White-box** xác định cách quan sát; **2.8 Equivalence Partitioning vs ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석)** dùng quan sát theo đầu vào để chọn lớp tương đương và các điểm biên có nguy cơ sai.

## 2.8 Equivalence Partitioning vs ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석)

Equivalence Partitioning chia lĩnh vực (domain / 도메인) thành các lớp (class / 클래스) kỳ vọng hành vi (behavior / 동작) tương đương.

Ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석) tập trung ngay biên và gần biên, nơi bug off-by-one dễ xuất hiện.

---

> **Nối mạch:** Sau khi chọn lớp giá trị và điểm biên, chuyển sang **2.9 Retest vs Regression kiểm thử (test / 테스트)** để phân biệt chạy lại lỗi đã sửa với kiểm tra ảnh hưởng lan sang chức năng khác.

## 2.9 Retest vs Regression kiểm thử (test / 테스트)

**Retest**: kiểm lại chính defect đã sửa.

**Regression kiểm thử (test / 테스트)**: kiểm xem thay đổi có phá hành vi (behavior / 동작) cũ ở chỗ khác không.

Một bản phát hành (release / 릴리스) có thể cần cả hai.

---

> **Nối mạch:** **2.9 Retest vs Regression kiểm thử (test / 테스트)** phân biệt mục tiêu của lần chạy; **2.10 Alpha vs Beta kiểm thử (test / 테스트)** chuyển sang bối cảnh người dùng và mức hoàn thiện của sản phẩm trước phát hành.

## 2.10 Alpha vs Beta kiểm thử (test / 테스트)

Alpha thường nội bộ hoặc môi trường kiểm soát của tổ chức phát triển.

Beta thường do bên ngoài (external / 외부)/real users trong môi trường gần thực tế hơn trước bản phát hành (release / 릴리스) rộng.

---

> **Nối mạch:** Sau khi phân biệt alpha và beta theo mức độ kiểm thử, **2.11 phiên bản (version / 버전) điều khiển (control / 제어) vs cấu hình (configuration / 구성) Management** tách danh tính của artefact khỏi tập thiết lập tạo ra nó.

## 2.11 phiên bản (version / 버전) điều khiển (control / 제어) vs cấu hình (configuration / 구성) Management

Phiên bản (version / 버전) điều khiển (control / 제어) quản lý lịch sử (history / 이력)/phiên bản (version / 버전)/branch của nguồn (source / 소스)/sản phẩm tạo ra (artifact / 산출물).

Cấu hình (configuration / 구성) Management rộng hơn: identification, baseline, thay đổi (change / 변경) điều khiển (control / 제어), status accounting, kiểm tra (audit / 감사) và bản phát hành (release / 릴리스)/cấu hình (configuration / 구성) items.

Git là công cụ (tool / 도구) quan trọng nhưng không phải toàn bộ SCM/CM discipline.

---

> **Nối mạch:** **2.11 phiên bản (version / 버전) điều khiển (control / 제어) vs cấu hình (configuration / 구성) Management** đã tách mã nguồn khỏi thiết lập; **2.12 bản dựng (build / 빌드) vs gói (package / 패키지) vs bản phát hành (release / 릴리스)** theo dõi artefact từ lúc tạo đến lúc giao cho người dùng.

## 2.12 bản dựng (build / 빌드) vs gói (package / 패키지) vs bản phát hành (release / 릴리스)

**bản dựng (build / 빌드)** biến nguồn (source / 소스) thành executable/sản phẩm tạo ra (artifact / 산출물).

**gói (package / 패키지)** gom sản phẩm tạo ra (artifact / 산출물) + phụ thuộc (dependency / 의존성)/siêu dữ liệu (metadata / 메타데이터)/cấu hình (config / 설정)/manual cần cho phân phối (distribution / 분포)/install.

**bản phát hành (release / 릴리스)** là một phiên bản (version / 버전) được chuẩn bị/approve để phân phối/deploy theo tiến trình (process / 프로세스).

---

> **Nối mạch:** Sau khi phân biệt build, package và release theo vòng đời artefact, **2.13 Checksum/băm (hash / 해시) vs Digital Signature** hỏi tiếp cách kiểm tra toàn vẹn và xác thực nguồn; rồi chuyển sang khóa trong cơ sở dữ liệu.

## 2.13 Checksum/băm (hash / 해시) vs Digital Signature

Checksum/băm (hash / 해시) so sánh content giúp phát hiện thay đổi/corruption.

Digital Signature kết hợp cryptographic signing để hỗ trợ authenticity/integrity và non-repudiation các giả định (assumptions / 가정들).

Biết băm (hash / 해시) đúng không tự nói **ai** tạo gói (package / 패키지).

---

# 3. Môn 3 — 데이터베이스 구축

> **Nối mạch:** Từ kiểm tra toàn vẹn và xác thực artefact ở **2.13**, chuyển sang **3.1 Super Key vs Candidate Key** để phân biệt một tập thuộc tính đủ nhận diện với tập đủ nhận diện tối thiểu.

## 3.1 Super Key vs Candidate Key

Super Key xác định duy nhất row nhưng có thể dư attribute.

Candidate Key là **minimal superkey**.

Primary Key chỉ là candidate key được chọn làm key chính.

---

> **Nối mạch:** **3.1 Super Key vs Candidate Key** đã xác định tính tối thiểu; **3.2 Candidate Key vs Primary Key** hỏi tiếp trong các candidate key, khóa nào được chọn làm định danh chính của bảng.

## 3.2 Candidate Key vs Primary Key

Một quan hệ (relation / 관계) có thể có nhiều candidate keys nhưng chỉ chọn một primary key.

Các candidate key còn lại thường gọi alternate keys theo terminology truyền thống.

---

> **Nối mạch:** Sau khi tách candidate key khỏi primary key, **3.3 Selection vs Projection** chuyển sang đại số quan hệ: lọc hàng theo điều kiện hay chọn cột theo thuộc tính.

## 3.3 Selection vs Projection

Selection — σ — chọn **row** theo predicate.

Projection — π — chọn **column/attribute**.

Đừng bị đánh lừa bởi tiếng Anh “select” trong SQL vì `SELECT col` của SQL lại gần projection về relational algebra.

---

> **Nối mạch:** **3.3 Selection vs Projection** tách thao tác trên hàng và cột; **3.4 Partial vs Transitive phụ thuộc (dependency / 의존성)** tách cách thuộc tính phụ thuộc vào khóa để chuẩn hóa quan hệ.

## 3.4 Partial vs Transitive phụ thuộc (dependency / 의존성)

Partial phụ thuộc (dependency / 의존성): non-key attribute phụ thuộc vào **một phần** composite key.

Transitive phụ thuộc (dependency / 의존성): key → non-key A → non-key B.

2NF chủ yếu xử lý partial phụ thuộc (dependency / 의존성); 3NF xử lý transitive phụ thuộc (dependency / 의존성) theo intuition thi cơ bản.

---

> **Nối mạch:** Sau khi nhận diện partial và transitive dependency, **3.5 3NF vs BCNF** cho thấy hai mức chuẩn hóa khác nhau ở điều kiện mọi determinant có phải là super key hay không.

## 3.5 3NF vs BCNF

3NF cho phép một số FD mà determinant không là superkey nếu dependent là prime attribute theo formal definition.

BCNF chặt hơn: determinant của mọi non-trivial FD phải là superkey.

Nếu đề chỉ dùng ví dụ cơ bản, cả hai có thể cho cùng decomposition; cần nhìn formal điều kiện (condition / 조건) khi câu hỏi cố tình tạo ngoại lệ.

---

> **Nối mạch:** **3.5 3NF vs BCNF** xử lý phụ thuộc ở mức logic; **3.6 Logical vs vật lý (physical / 물리적) cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)** chuyển câu hỏi sang cách mô hình được triển khai trên hệ thống.

## 3.6 Logical vs vật lý (physical / 물리적) cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)

Logical thiết kế (design / 설계) nói quan hệ (relation / 관계)/thực thể (entity / 엔터티), key, phụ thuộc (dependency / 의존성), normalization.

Vật lý (physical / 물리적) thiết kế (design / 설계) nói lưu trữ (storage / 저장소), chỉ mục (index / 인덱스), partition, clustering, truy cập (access / 접근) đường dẫn (path / 경로), denormalization có kiểm soát.

Truy vấn (query / 쿼리) chậm vì thiếu chỉ mục (index / 인덱스) là vật lý (physical / 물리적) bài toán (problem / 문제), không tự động là normalization bài toán (problem / 문제).

---

> **Nối mạch:** Sau khi tách thiết kế logic khỏi bố trí vật lý, **3.7 B+cây (tree / 트리) vs băm (hash / 해시) chỉ mục (index / 인덱스)** so sánh hai cách lập chỉ mục theo kiểu truy vấn và mẫu phân bố khóa.

## 3.7 B+cây (tree / 트리) vs băm (hash / 해시) chỉ mục (index / 인덱스)

B+cây (tree / 트리) giữ thứ tự (ordering / 순서) → equality + phạm vi (range / 범위) + ordered traversal.

Băm (hash / 해시) tự nhiên cho equality lookup nhưng không hỗ trợ ordered phạm vi (range / 범위) theo cùng cách.

Nếu predicate `created_at BETWEEN ...` → B+cây (tree / 트리) thường tự nhiên hơn.

---

> **Nối mạch:** **3.7 B+cây (tree / 트리) vs băm (hash / 해시) chỉ mục (index / 인덱스)** cho biết cấu trúc index; **3.8 Cardinality vs Selectivity** bổ sung cách đánh giá có bao nhiêu giá trị và bộ lọc loại được bao nhiêu dòng.

## 3.8 Cardinality vs Selectivity

**Cardinality** thường nói số lượng distinct values hoặc số row tùy ngữ cảnh (context / 맥락) thống kê.

**Selectivity** nói fraction/khả năng predicate thu hẹp dữ liệu (data / 데이터).

Column gender có cardinality thấp; `user_id` thường cardinality cao.

---

> **Nối mạch:** Sau khi hiểu selectivity là sức lọc, **3.9 WHERE vs HAVING** đặt phép lọc vào đúng thời điểm: trước grouping hay sau khi nhóm đã được tạo.

## 3.9 WHERE vs HAVING

WHERE lọc row trước grouping.

HAVING lọc group sau aggregate.

`WHERE status='PAID'` và `HAVING SUM(amount)>1000` có thể xuất hiện cùng truy vấn (query / 쿼리) nhưng ở hai phase khác nhau.

---

> **Nối mạch:** **3.9 WHERE vs HAVING** đã phân biệt lọc trước và sau grouping; **3.10 COUNT() vs COUNT(column)** tiếp tục kiểm tra dữ liệu nào được tính, đặc biệt khi có `NULL`.

## 3.10 COUNT(*) vs COUNT(column)

`COUNT(*)` đếm rows.

`COUNT(column)` bỏ qua NULL ở column đó.

Trong LEFT phép nối (join / 조인) unmatched row, khác biệt này dễ xuất hiện.

---

> **Nối mạch:** Sau khi phân biệt `COUNT(*)` với `COUNT(column)`, chuyển sang **3.11 INNER phép nối (join / 조인) vs LEFT phép nối (join / 조인)** để xem việc giữ hay loại dòng không khớp thay đổi kết quả đếm ra sao.

## 3.11 INNER phép nối (join / 조인) vs LEFT phép nối (join / 조인)

INNER phép nối (join / 조인) giữ match hai bên.

LEFT phép nối (join / 조인) giữ mọi row bên trái, unmatched bên phải thành NULL.

Nếu yêu cầu (requirement / 요구사항) là “show all customers kể cả chưa có thứ tự (order / 순서)” → LEFT phép nối (join / 조인).

---

> **Nối mạch:** **3.11 INNER phép nối (join / 조인) vs LEFT phép nối (join / 조인)** làm lộ các dòng thiếu phía đối tác; **3.12 NULL vs Empty String vs 0** giúp phân biệt “không có giá trị” với chuỗi rỗng và số không.

## 3.12 NULL vs Empty String vs 0

NULL biểu diễn missing/unknown/not-applicable theo mô hình (model / 모델)/ngữ cảnh (context / 맥락).

`''` là một string giá trị (value / 값); `0` là numeric giá trị (value / 값).

Comparison với NULL dùng `IS NULL`, không dùng `= NULL` trong SQL chuẩn.

---

> **Nối mạch:** Sau khi tách ba trạng thái giá trị ở **3.12**, **3.13 Dirty Read vs Non-repeatable Read vs Phantom** chuyển sang ba kiểu bất nhất do giao dịch quan sát dữ liệu ở các thời điểm khác nhau.

## 3.13 Dirty Read vs Non-repeatable Read vs Phantom

Dirty Read: đọc dữ liệu (data / 데이터) chưa lần ghi nhận (commit / 커밋) của giao dịch (transaction / 트랜잭션) khác.

Non-repeatable Read: cùng row đọc hai lần ra giá trị (value / 값) khác do committed cập nhật (update / 업데이트)/delete.

Phantom: cùng predicate truy vấn (query / 쿼리) ra set row khác vì insert/delete phù hợp predicate.

Đơn vị (unit / 단위) thay đổi là key để phân biệt: **uncommitted giá trị (value / 값)**, **same row giá trị (value / 값)**, hay **set membership**.

---

> **Nối mạch:** **3.13 Dirty Read vs Non-repeatable Read vs Phantom** mô tả lỗi đọc; **3.14 Deadlock vs Lost cập nhật (update / 업데이트)** chuyển sang lỗi phối hợp khi giao dịch giữ khóa hoặc ghi đè cùng dữ liệu.

## 3.14 Deadlock vs Lost cập nhật (update / 업데이트)

Deadlock: transactions chờ tài nguyên (resource / 자원) vòng tròn, không tiến được.

Lost cập nhật (update / 업데이트): một cập nhật (update / 업데이트) bị ghi đè/mất vì concurrent writes không được kiểm soát.

Cả hai là tính đồng thời (concurrency / 동시성) bài toán (problem / 문제) nhưng symptom hoàn toàn khác.

---

> **Nối mạch:** Sau khi tách deadlock khỏi lost update, **3.15 Serial vs Serializable** hỏi mức cô lập cần đạt: thực thi tuần tự thật hay chỉ tương đương với một thứ tự tuần tự.

## 3.15 Serial vs Serializable

Serial schedule: giao dịch (transaction / 트랜잭션) chạy hoàn toàn từng cái một.

Serializable schedule: interleave nhưng tác động (effect / 효과) tương đương một serial thứ tự (order / 순서) theo criterion đang xét.

Conflict-serializable không đồng nghĩa schedule phải visually serial.

---

> **Nối mạch:** **3.15 Serial vs Serializable** chốt tiêu chí đúng của lịch giao dịch; **3.16 Undo vs Redo** chuyển sang cơ chế khôi phục: hoàn tác tác động chưa commit hay áp lại tác động đã commit.

## 3.16 Undo vs Redo

Undo quay lại tác động (effect / 효과) của giao dịch (transaction / 트랜잭션) chưa lần ghi nhận (commit / 커밋)/aborted theo chiến lược khôi phục (recovery strategy / 복구 전략).

Redo tái áp tác động (effect / 효과) của committed giao dịch (transaction / 트랜잭션) chưa reflected đầy đủ trên dữ liệu (data / 데이터) pages sau crash.

WAL/log chuỗi (sequence / 시퀀스) quyết định khôi phục (recovery / 복구) hành động (action / 동작) cụ thể.

---

> **Nối mạch:** Sau khi phân biệt Undo và Redo theo hướng phục hồi log, **3.17 Backup vs Checkpoint** tách bản sao dùng để khôi phục thảm họa khỏi điểm mốc giúp engine rút ngắn việc phục hồi, rồi mở sang Môn 4.

## 3.17 Backup vs Checkpoint

Backup là bản sao dữ liệu để restore sau mất mát (loss / 손실)/corruption/disaster.

Checkpoint giúp khôi phục (recovery / 복구) engine giảm phạm vi log cần xem khi crash khôi phục (recovery / 복구).

Checkpoint không thay backup.

---

# 4. Môn 4 — 프로그래밍 언어 활용

> **Nối mạch:** **3.17 Backup vs Checkpoint** khép nhóm phục hồi dữ liệu; **4.1 tiến trình (process / 프로세스) vs luồng thực thi (thread / 스레드)** chuyển sang đơn vị thực thi, tách tài nguyên riêng của process khỏi trạng thái dùng chung của thread.

## 4.1 tiến trình (process / 프로세스) vs luồng thực thi (thread / 스레드)

Tiến trình (process / 프로세스) có address không gian (space / 공간)/tài nguyên (resource / 자원) ngữ cảnh (context / 맥락) riêng hơn.

Threads trong cùng tiến trình (process / 프로세스) thường share address không gian (space / 공간)/resources.

Luồng thực thi (thread / 스레드) nhẹ hơn về communication/ngữ cảnh (context / 맥락) nhưng trạng thái dùng chung (shared state / 공유 상태) tạo synchronization rủi ro (risk / 위험).

---

> **Nối mạch:** **4.1 tiến trình (process / 프로세스) vs luồng thực thi (thread / 스레드)** tách tài nguyên riêng khỏi trạng thái dùng chung; **4.2 tính đồng thời (concurrency / 동시성) vs Parallelism** hỏi các tác vụ chỉ chồng lấn tiến độ hay thực sự chạy cùng lúc.

## 4.2 tính đồng thời (concurrency / 동시성) vs Parallelism

Tính đồng thời (concurrency / 동시성): nhiều tác vụ (task / 작업) có progress overlapping về thời gian.

Parallelism: nhiều tác vụ (task / 작업) thực sự execute đồng thời trên nhiều đơn vị thực thi (execution unit / 실행 유닛)/cốt lõi (core / 핵심).

Single-core vòng lặp sự kiện (event loop / 이벤트 루프) có tính đồng thời (concurrency / 동시성) nhưng không nhất thiết parallel CPU thực thi (execution / 실행).

---

> **Nối mạch:** Sau khi phân biệt concurrency với parallelism, **4.3 Mutex vs Semaphore** chuyển sang công cụ điều phối: khóa có ownership để loại trừ hay bộ đếm cho phép nhiều holder.

## 4.3 Mutex vs Semaphore

Mutex thường mutual exclusion với quyền sở hữu (ownership / 소유권) ngữ nghĩa (semantics / 의미론).

Semaphore là counter permits; có thể cho N concurrent holders.

Nhị phân (binary / 이진) semaphore có thể giống mutex ở vài use trường hợp (case / 사례) nhưng không đồng nhất lớp trừu tượng (abstraction / 추상화).

---

> **Nối mạch:** **4.3 Mutex vs Semaphore** cho biết cơ chế cấp quyền; **4.4 Race điều kiện (condition / 조건) vs Deadlock** kiểm tra hệ quả khi đồng bộ thiếu: kết quả sai do tranh chấp hay hệ thống mắc kẹt chờ nhau.

## 4.4 Race điều kiện (condition / 조건) vs Deadlock

Race điều kiện (condition / 조건): kết quả (result / 결과) phụ thuộc timing/interleaving.

Deadlock: các participant bị kẹt vì circular tài nguyên (resource / 자원) wait.

Race có thể cho kết quả (result / 결과) sai nhưng chương trình vẫn chạy tiếp; deadlock thường làm progress dừng.

---

> **Nối mạch:** Sau khi tách race condition khỏi deadlock, **4.5 Deadlock Prevention vs Avoidance vs Detection** phân biệt ba thời điểm can thiệp: ngăn điều kiện, tránh trạng thái không an toàn, hay phát hiện sau khi xảy ra.

## 4.5 Deadlock Prevention vs Avoidance vs Detection

Prevention: phá ít nhất một Coffman điều kiện (condition / 조건).

Avoidance: chỉ cấp tài nguyên (resource / 자원) nếu trạng thái (state / 상태) vẫn safe, ví dụ Banker’s thuật toán (algorithm / 알고리즘).

Detection: cho phép deadlock xảy ra rồi phát hiện và recover.

---

> **Nối mạch:** **4.5 Deadlock Prevention vs Avoidance vs Detection** khép nhóm an toàn đồng thời; **4.6 FCFS vs SJF vs Round Robin** chuyển sang chính sách lập lịch và cách nó ưu tiên công việc.

## 4.6 FCFS vs SJF vs Round Robin

FCFS → đơn giản, convoy tác động (effect / 효과).

SJF → ưu tiên burst ngắn, tốt cho average waiting trong mô hình (model / 모델) lý tưởng, có starvation rủi ro (risk / 위험).

Round Robin → thời gian (time / 시간) quantum, preemptive/time-sharing, sự đánh đổi (trade-off / 트레이드오프) responsiveness vs context-switch overhead.

---

> **Nối mạch:** Sau khi chọn thuật toán lịch, **4.7 Waiting vs Turnaround vs phản hồi (response / 응답) thời gian (time / 시간)** tách các thước đo kết quả: chờ đến lượt, hoàn tất toàn bộ hay phản hồi lần đầu.

## 4.7 Waiting vs Turnaround vs phản hồi (response / 응답) thời gian (time / 시간)

Turnaround = Completion − Arrival.

Waiting = Turnaround − CPU dịch vụ (service / 서비스) thời gian (time / 시간) trong bài đơn giản.

Phản hồi (response / 응답) = First Run − Arrival.

Một tiến trình (process / 프로세스) có phản hồi (response / 응답) tốt nhưng turnaround dài nếu được chạy sớm một chút rồi phải chờ lâu sau đó.

---

> **Nối mạch:** **4.7 Waiting vs Turnaround vs phản hồi (response / 응답) thời gian (time / 시간)** đo hiệu quả lịch CPU; **4.8 Paging vs Segmentation** chuyển sang cách hệ thống chia và ánh xạ không gian nhớ.

## 4.8 Paging vs Segmentation

Paging chia fixed-size page/frame.

Segmentation chia logical variable-size segment.

Paging thường gắn nội bộ (internal / 내부) fragmentation; segmentation contiguous truyền thống dễ bên ngoài (external / 외부) fragmentation.

---

> **Nối mạch:** Sau khi phân biệt page cố định với segment theo logic chương trình, **4.9 FIFO vs LRU Page Replacement** hỏi trang nào bị đẩy ra khi bộ nhớ cần chỗ: trang vào trước hay trang ít được dùng gần đây.

## 4.9 FIFO vs LRU Page Replacement

FIFO chọn page vào bộ nhớ (memory / 메모리) lâu nhất.

LRU chọn page lâu nhất chưa được sử dụng.

Tham chiếu (reference / 참조) gần đây có thể cứu page trong LRU nhưng không thay arrival thứ tự (order / 순서) của FIFO.

---

> **Nối mạch:** **4.9 FIFO vs LRU Page Replacement** mô tả chính sách thay trang; **4.10 Page Fault vs Thrashing** phân biệt một lần thiếu trang với tình trạng hệ thống dành hầu hết thời gian để thay trang.

## 4.10 Page Fault vs Thrashing

Page fault là một sự kiện (event / 이벤트): referenced page chưa resident.

Thrashing là system-level điều kiện (condition / 조건): quá nhiều paging/page faults làm useful công việc (work / 작업) giảm mạnh.

Một page fault đơn lẻ không phải thrashing.

---

> **Nối mạch:** Sau khi tách lỗi nhớ cục bộ khỏi suy giảm toàn hệ thống, **4.11 TCP vs UDP** chuyển sang mạng: truyền tin có kết nối, kiểm soát và thứ tự hay ưu tiên sự gọn nhẹ.

## 4.11 TCP vs UDP

TCP: connection-oriented, ordered reliable byte stream.

UDP: connectionless datagram, không tự bảo đảm delivery/thứ tự (order / 순서).

“UDP nhanh hơn” không phải universal truth; overhead/ngữ nghĩa (semantics / 의미론) khác nhau.

---

> **Nối mạch:** **4.11 TCP vs UDP** đã tách semantics truyền tải; **4.12 IP vs MAC Address** tách tiếp địa chỉ logic dùng để định tuyến khỏi địa chỉ phần cứng trong một segment.

## 4.12 IP vs MAC Address

IP dùng logical network-layer addressing/routing.

MAC dùng link-layer addressing trên cục bộ (local / 로컬) segment.

Router forward theo IP; cục bộ (local / 로컬) frame delivery dùng link-layer address.

---

> **Nối mạch:** Sau khi phân biệt loại địa chỉ và phạm vi của nó, **4.13 DNS vs DHCP** tách hai dịch vụ dễ nhầm: phân giải tên thành địa chỉ và cấp cấu hình mạng cho máy.

## 4.13 DNS vs DHCP

DNS giải tên/bản ghi (record / 레코드).

DHCP cấp mạng (network / 네트워크) cấu hình (configuration / 구성) động như IP, mask, gateway, DNS máy chủ (server / 서버).

---

> **Nối mạch:** **4.13 DNS vs DHCP** xác định dịch vụ gắn với tên và cấu hình; **4.14 mạng (network / 네트워크) Address vs Broadcast Address** chuyển sang phạm vi đích của gói: một mạng hay mọi host trong mạng.

## 4.14 mạng (network / 네트워크) Address vs Broadcast Address

Trong subnet truyền thống:

Mạng (network / 네트워크) address: host bits = all 0.

Broadcast address: host bits = all 1.

Usable host thường nằm giữa hai ranh giới (boundary / 경계) này, trừ special cases.

---

> **Nối mạch:** Sau khi tách network address khỏi broadcast address, **4.15 Overloading vs Overriding** quay lại ngôn ngữ hướng đối tượng để phân biệt nạp chồng theo chữ ký với ghi đè theo kế thừa.

## 4.15 Overloading vs Overriding

Overloading: cùng tên, parameter signature khác; resolution chủ yếu compile-time.

Overriding: subclass cung cấp hiện thực (implementation / 구현) mới của instance phương thức (method / 메서드); thời gian chạy (runtime / 런타임) động (dynamic / 동적) dispatch.

Chỉ khác return kiểu (type / 타입) không đủ overload trong Java.

---

> **Nối mạch:** **4.15 Overloading vs Overriding** đã tách lựa chọn compile-time khỏi hành vi runtime; **4.16 giá trị (value / 값) vs tham chiếu (reference / 참조)/Alias lập luận (reasoning / 추론)** hỏi tiếp biến được truyền như bản sao hay cùng trỏ đến một đối tượng, rồi mở sang quản lý dự án.

## 4.16 giá trị (value / 값) vs tham chiếu (reference / 참조)/Alias lập luận (reasoning / 추론)

C pointer bản sao (copy / 복사) address giá trị (value / 값) nhưng có thể mutate pointed đối tượng (object / 객체).

Java pass-by-value, kể cả khi giá trị (value / 값) đó là đối tượng (object / 객체) tham chiếu (reference / 참조).

Python assignment bind name tới đối tượng (object / 객체); hai names có thể alias một mutable đối tượng (object / 객체).

Điểm chung: **bản sao (copy / 복사) tham chiếu (reference / 참조)/address giá trị (value / 값) không đồng nghĩa bản sao (copy / 복사) đối tượng (object / 객체)**.

---

# 5. Môn 5 — 정보시스템 구축 관리

> **Nối mạch:** Từ cách truyền giá trị và alias ở **4.16**, chuyển sang **5.1 Waterfall vs Agile** để phân biệt kế hoạch tuần tự cố định với vòng lặp thích ứng theo phản hồi.

## 5.1 Waterfall vs Agile

Waterfall tổ chức phase theo chuỗi (sequence / 시퀀스) rõ và phản hồi (feedback / 피드백)/thay đổi (change / 변경) thường đắt hơn khi muộn.

Agile/iterative dùng vòng phản hồi (feedback / 피드백) ngắn và incremental delivery.

Không kết luận “Agile không cần thiết kế (design / 설계)/documentation” hoặc “Waterfall luôn sai”.

---

> **Nối mạch:** Sau khi tách Waterfall khỏi Agile theo cách lập kế hoạch và phản hồi, **5.2 rủi ro (risk / 위험) vs Issue** hỏi một bất định còn có thể xảy ra hay một vấn đề đã hiện hữu.

## 5.2 rủi ro (risk / 위험) vs Issue

Rủi ro (risk / 위험) là sự kiện **có thể xảy ra** trong tương lai với xác suất (probability / 확률)/impact.

Issue là vấn đề **đã xảy ra/đang tồn tại** cần xử lý.

---

> **Nối mạch:** **5.2 rủi ro (risk / 위험) vs Issue** đã phân biệt trạng thái tiềm ẩn và hiện hữu; **5.3 PERT vs CPM** chuyển sang kỹ thuật ước lượng thời lượng bất định và lập lịch với thời lượng xác định.

## 5.3 PERT vs CPM

PERT truyền thống dùng optimistic/most-likely/pessimistic estimate để tính expected duration.

CPM tập trung phụ thuộc (dependency / 의존성) mạng (network / 네트워크), đường dẫn (path / 경로) duration, đường găng (critical path / 임계 경로)/slack.

Một dự án (project / 프로젝트) có thể dùng cả hai ý tưởng.

---

> **Nối mạch:** Sau khi chọn PERT hay CPM theo kiểu ước lượng, **5.4 đường găng (critical path / 임계 경로) vs Longest Activity** nhắc rằng đường quyết định thời hạn dự án không nhất thiết là một hoạt động đơn lẻ dài nhất.

## 5.4 đường găng (critical path / 임계 경로) vs Longest Activity

Đường găng (critical path / 임계 경로) là **chuỗi đường dẫn (path / 경로)** quyết định dự án (project / 프로젝트) duration, không phải activity đơn lẻ dài nhất.

Một activity rất dài nhưng có float vẫn có thể không nằm đường găng (critical path / 임계 경로).

---

> **Nối mạch:** **5.4 đường găng (critical path / 임계 경로) vs Longest Activity** chốt cách đọc phụ thuộc thời gian; **5.5 RAID vs Backup** chuyển sang độ sẵn sàng và bảo vệ dữ liệu, tách dư thừa vận hành khỏi bản sao phục hồi.

## 5.5 RAID vs Backup

RAID tăng availability/tolerance với một số disk thất bại (failure / 실패).

Backup cung cấp restore điểm (point / 지점) độc lập hơn cho deletion, corruption, ransomware, disaster tùy kiến trúc (architecture / 아키텍처).

RAID không phải backup.

---

> **Nối mạch:** Sau khi phân biệt RAID giúp hệ thống tiếp tục chạy với backup dùng để restore, **5.6 Replication vs Backup** hỏi dữ liệu được đồng bộ cho vận hành hay được lưu thành điểm phục hồi.

## 5.6 Replication vs Backup

Replication giữ bản sao (copy / 복사) gần hiện tại (current / 현재) để availability/read quy mô (scale / 규모)/failover.

Backup giữ khôi phục (recovery / 복구) bản sao (copy / 복사)/phiên bản (version / 버전) theo chính sách (policy / 정책).

Sai dữ liệu/xóa nhầm có thể replicate nhanh sang replica; backup lịch sử có thể giúp quay lại trạng thái (state / 상태) cũ.

---

> **Nối mạch:** **5.6 Replication vs Backup** tách đồng bộ liên tục khỏi bản sao lưu; **5.7 HA vs DR** mở rộng thành mục tiêu giảm gián đoạn đang xảy ra hay khôi phục sau sự cố lớn.

## 5.7 HA vs DR

High Availability — 고가용성 — giảm downtime trong thất bại (failure / 실패) thường gặp, thường failover nhanh.

Disaster khôi phục (recovery / 복구) — 재해복구 — phục hồi sau sự cố lớn/miền lỗi (failure domain / 장애 도메인) rộng.

Multi-node trong cùng miền lỗi (failure domain / 장애 도메인) có thể HA nhưng vẫn DR yếu.

---

> **Nối mạch:** Sau khi chọn HA hay DR theo mục tiêu phục vụ, **5.8 RTO vs RPO** định lượng hai giới hạn: mất bao lâu để phục hồi và chấp nhận mất bao nhiêu dữ liệu.

## 5.8 RTO vs RPO

RTO hỏi: **bao lâu phải khôi phục dịch vụ (service / 서비스)?**

RPO hỏi: **chấp nhận mất bao nhiêu dữ liệu tính theo thời gian?**

30 phút downtime → RTO.

Mất tối đa 5 phút giao dịch (transaction / 트랜잭션) → RPO.

---

> **Nối mạch:** **5.8 RTO vs RPO** biến yêu cầu phục hồi thành con số; **5.9 Vertical vs Horizontal Scaling** chuyển sang cách tăng năng lực bằng máy lớn hơn hay nhiều instance hơn.

## 5.9 Vertical vs Horizontal Scaling

Vertical: tăng tài nguyên (resource / 자원) cho một nút (node / 노드).

Horizontal: thêm nhiều nút (node / 노드)/instance.

Horizontal scaling thường cần giải bài trạng thái (state / 상태) phân phối (distribution / 분포), tải (load / 로드) balancing và consistency.

---

> **Nối mạch:** Sau khi phân biệt scale dọc và ngang, **5.10 VM vs bộ chứa (container / 컨테이너)** hỏi mức cô lập và phần hệ điều hành được ảo hóa hay dùng chung.

## 5.10 VM vs bộ chứa (container / 컨테이너)

VM truyền thống có guest OS/kernel riêng trên hypervisor.

Bộ chứa (container / 컨테이너) thường share host kernel nhưng isolate tiến trình (process / 프로세스)/resources qua OS primitives.

Bộ chứa (container / 컨테이너) không tự động “an toàn hơn” hoặc “nhanh hơn” trong mọi ngữ cảnh (context / 맥락).

---

> **Nối mạch:** **5.10 VM vs bộ chứa (container / 컨테이너)** đã tách kiểu đóng gói runtime; **5.11 IaaS vs PaaS vs SaaS** chuyển sang ranh giới trách nhiệm giữa nhà cung cấp và người dùng.

## 5.11 IaaS vs PaaS vs SaaS

IaaS: provider cung cấp compute/lưu trữ (storage / 저장소)/mạng (network / 네트워크) primitives; customer quản nhiều tầng (layer / 계층) OS/thời gian chạy (runtime / 런타임)/app hơn.

PaaS: provider quản nền tảng (platform / 플랫폼)/thời gian chạy (runtime / 런타임) nhiều hơn, customer tập trung ứng dụng (application / 애플리케이션)/dữ liệu (data / 데이터).

SaaS: customer sử dụng ứng dụng hoàn chỉnh.

Hãy hỏi **ai quản tầng (layer / 계층) nào**, không học bằng tên vendor.

---

> **Nối mạch:** Sau khi xác định ai quản lý lớp nào trong IaaS, PaaS và SaaS, **5.12 Authentication vs Authorization** tách việc chứng minh danh tính khỏi việc quyết định quyền được làm gì.

## 5.12 Authentication vs Authorization

Authentication — 인증 — xác minh định danh (identity / 식별자).

Authorization — 인가/권한부여 — quyết định định danh (identity / 식별자) đó được phép làm gì.

Login đúng không có nghĩa được quyền đọc mọi invoice.

---

> **Nối mạch:** **5.12 Authentication vs Authorization** xác định ai được phép làm gì; **5.13 Hashing vs Encryption** chuyển sang cách bảo vệ dữ liệu: biến một chiều để kiểm tra hay biến đổi có khóa để giải mã.

## 5.13 Hashing vs Encryption

Hashing là one-way digest theo thiết kế (design / 설계) cryptographic; dùng integrity/password lưu trữ (storage / 저장소) với scheme phù hợp.

Encryption là reversible với key, dùng confidentiality.

Password không nên lưu bằng reversible encryption như substitute cho password hashing KDF.

---

> **Nối mạch:** Sau khi tách hashing khỏi encryption, **5.14 Symmetric vs Asymmetric Cryptography** so sánh cơ chế khóa dùng chung với cặp khóa công khai–bí mật và mục tiêu sử dụng của chúng.

## 5.14 Symmetric vs Asymmetric Cryptography

Symmetric dùng cùng secret key family cho encrypt/decrypt, hiệu quả với bulk dữ liệu (data / 데이터).

Asymmetric dùng công khai (public / 공개)/private key pair, phù hợp key exchange/signature và một số encryption use trường hợp (case / 사례).

TLS thường kết hợp nhiều thành phần nguyên thủy (primitive / 기본 요소), không phải chỉ “asymmetric encryption”.

---

> **Nối mạch:** **5.14 Symmetric vs Asymmetric Cryptography** chốt ranh giới giữa các mô hình khóa; **5.15 SQL Injection vs XSS** chuyển sang nơi đầu vào độc hại tác động: truy vấn phía máy chủ hay script trong trình duyệt.

## 5.15 SQL Injection vs XSS

SQL Injection làm untrusted đầu vào (input / 입력) thay đổi cấu trúc/ý nghĩa SQL command.

Cốt lõi (core / 핵심) defense: parameterized truy vấn (query / 쿼리)/prepared statement.

XSS đưa script/content độc hại vào trình duyệt (browser / 브라우저) ngữ cảnh (context / 맥락).

Cốt lõi (core / 핵심) defense: context-aware đầu ra (output / 출력) encoding/escaping, template an toàn (safety / 안전) và related controls.

Cả hai đều liên quan đầu vào (input / 입력), nhưng nguyên nhân gốc (root cause / 근본 원인)/sink khác nhau.

---

> **Nối mạch:** Sau khi nhận diện SQL injection và XSS theo điểm thực thi, **5.16 Firewall vs WAF** hỏi lớp phòng vệ đang lọc lưu lượng mạng chung hay hiểu ngữ nghĩa HTTP và ứng dụng web.

## 5.16 Firewall vs WAF

Mạng (network / 네트워크) firewall kiểm traffic theo mạng (network / 네트워크)/vận chuyển (transport / 전송) quy tắc (rule / 규칙) và ngữ cảnh (context / 맥락) thiết bị.

WAF hiểu HTTP/web ứng dụng (application / 애플리케이션) ngữ nghĩa (semantics / 의미론) sâu hơn để filter web attack patterns.

WAF không thay secure coding; firewall L3/L4 không tự giải SQL injection nguyên nhân gốc (root cause / 근본 원인).

---

> **Nối mạch:** **5.16 Firewall vs WAF** phân biệt lọc theo lớp và ngữ nghĩa; **5.17 IDS vs IPS** chuyển sang phản ứng của hệ thống: chỉ phát hiện và cảnh báo hay chặn lưu lượng đáng ngờ.

## 5.17 IDS vs IPS

IDS thiên detection/alert.

IPS thường inline và có khả năng khối (block / 블록)/prevent traffic.

Triển khai (deployment / 배포) thực tế đa dạng, nhưng đây là ranh giới conceptual thường dùng trong đề.

---

> **Nối mạch:** Sau khi tách IDS khỏi IPS theo hành động, **5.18 TLS vs VPN** phân biệt mã hóa một kết nối/luồng ứng dụng với đường hầm bảo vệ cả lưu lượng giữa các mạng hoặc host.

## 5.18 TLS vs VPN

TLS bảo vệ một ứng dụng (application / 애플리케이션)/session/channel cụ thể theo giao thức (protocol / 프로토콜) setup.

VPN tạo protected tunnel/mạng (network / 네트워크) overlay giữa endpoint/mạng (network / 네트워크).

Cả hai có thể dùng cryptography nhưng phạm vi (scope / 범위) khác.

---

> **Nối mạch:** **5.18 TLS vs VPN** khép nhóm bảo vệ đường truyền; **5.19 Threat vs Vulnerability vs rủi ro (risk / 위험)** chuyển sang mô hình nguyên nhân, tách tác nhân đe dọa, điểm yếu và khả năng thiệt hại.

## 5.19 Threat vs Vulnerability vs rủi ro (risk / 위험)

Threat: tác nhân/sự kiện có thể gây hại.

Vulnerability: weakness có thể bị khai thác.

Rủi ro (risk / 위험): khả năng + impact của harm trong ngữ cảnh (context / 맥락) cụ thể.

Điều khiển (control / 제어) giảm likelihood/impact/exposure nhưng không nhất thiết xóa threat.

---

# 6. Meta-confusions — khi hai đáp án đều đúng

> **Nối mạch:** Sau mô hình threat–vulnerability–risk ở **5.19**, **6.1 nguyên nhân gốc (root cause / 근본 원인) vs Defense in độ sâu (depth / 깊이)** đặt các đáp án đúng cạnh nhau và yêu cầu chọn theo phạm vi tác động trực tiếp hay lớp phòng vệ bổ sung.

## 6.1 nguyên nhân gốc (root cause / 근본 원인) vs Defense in độ sâu (depth / 깊이)

Nếu SQL injection xảy ra, cả WAF và prepared statement đều có thể giúp. Nhưng nếu đề hỏi **biện pháp trực tiếp xử lý nguyên nhân trong mã (code / 코드)**, prepared statement là đáp án mạnh hơn.

Nếu hỏi “additional perimeter điều khiển (control / 제어)”, WAF có thể đúng.

Câu hỏi thi thường không chỉ kiểm fact; nó kiểm **phạm vi (scope / 범위) của fact**.

---

> **Nối mạch:** **6.1 nguyên nhân gốc (root cause / 근본 원인) vs Defense in độ sâu (depth / 깊이)** vừa cho thấy cách chọn đáp án theo phạm vi; **6.2 cơ chế (mechanism / 메커니즘) vs Goal** áp dụng cùng nguyên tắc để tách thuộc tính mong muốn khỏi cách đạt được nó.

## 6.2 cơ chế (mechanism / 메커니즘) vs Goal

Ví dụ:

```text
Goal: Availability
Mechanisms: redundancy, replication, failover
```

Nếu hỏi “thuộc tính chất lượng” → Availability.

Nếu hỏi “cách đạt thuộc tính đó” → cơ chế (mechanism / 메커니즘) cụ thể.

---

> **Nối mạch:** Sau khi tách goal khỏi mechanism ở **6.2**, **6.3 Symptom vs Cause** nhắc người học không chọn giải pháp theo dấu hiệu bề mặt mà phải lần về nguyên nhân được bằng chứng hỗ trợ.

## 6.3 Symptom vs Cause

Slow truy vấn (query / 쿼리) là symptom.

Nguyên nhân có thể là full scan, poor cardinality estimate, missing chỉ mục (index / 인덱스), khóa (lock / 잠금) wait, I/O saturation hoặc thiết kế (design / 설계) khác.

Đừng chọn giải pháp chỉ vì nó “liên quan hiệu năng (performance / 성능)”. Chọn đáp án khớp bằng chứng (evidence / 증거) trong đề.

---

> **Nối mạch:** **6.3 Symptom vs Cause** đã tách biểu hiện khỏi nguyên nhân; **6.4 Logical tầng (layer / 계층) vs vật lý (physical / 물리적) tầng (layer / 계층)** khép atlas bằng câu hỏi phạm vi: cơ chế đúng ở một tầng có đủ để bảo đảm bất biến ở tầng khác hay không.

## 6.4 Logical tầng (layer / 계층) vs vật lý (physical / 물리적) tầng (layer / 계층)

Normalization đúng lô-gic (logic / 논리) không đảm bảo truy vấn (query / 쿼리) nhanh.

TLS đúng mạng (network / 네트워크) bảo mật (security / 보안) không đảm bảo object-level authorization.

Mutex đúng trong một tiến trình (process / 프로세스) không bảo vệ trạng thái dùng chung (shared state / 공유 상태) giữa nhiều máy chủ (server / 서버) instances.

Đây là mẫu (pattern / 패턴) chung: một cơ chế (mechanism / 메커니즘) có thể đúng **ở tầng (layer / 계층) của nó** nhưng không đủ cho bất biến (invariant / 불변식) ở tầng (layer / 계층) khác.

---

# 7. Closed-book discrimination kiểm thử (test / 테스트)

Không nhìn phần trên, tự trả lời trong một câu cho mỗi cặp:

1. xác minh (verification / 확인) / kiểm tra hợp lệ (validation / 검증)
2. DFD / Flowchart
3. chuỗi (sequence / 시퀀스) / Activity Diagram
4. Aggregation / Composition
5. Cohesion / Coupling
6. dữ liệu (data / 데이터) / Stamp Coupling
7. SRP / ISP
8. OCP / DIP
9. chiến lược (strategy / 전략) / trạng thái (state / 상태)
10. Adapter / Facade
11. Decorator / Proxy
12. Stub / Driver
13. Black-box / White-box
14. Retest / Regression
15. phiên bản (version / 버전) điều khiển (control / 제어) / cấu hình (configuration / 구성) Management
16. Super Key / Candidate Key
17. Partial / Transitive phụ thuộc (dependency / 의존성)
18. 3NF / BCNF
19. B+cây (tree / 트리) / băm (hash / 해시) chỉ mục (index / 인덱스)
20. WHERE / HAVING
21. COUNT(*) / COUNT(column)
22. Dirty / Non-repeatable / Phantom Read
23. Deadlock / Lost cập nhật (update / 업데이트)
24. Serial / Serializable
25. Backup / Checkpoint
26. tiến trình (process / 프로세스) / luồng thực thi (thread / 스레드)
27. tính đồng thời (concurrency / 동시성) / Parallelism
28. Mutex / Semaphore
29. Race / Deadlock
30. Prevention / Avoidance / Detection
31. Waiting / Turnaround / phản hồi (response / 응답) thời gian (time / 시간)
32. FIFO / LRU
33. Page Fault / Thrashing
34. TCP / UDP
35. DNS / DHCP
36. Overloading / Overriding
37. rủi ro (risk / 위험) / Issue
38. PERT / CPM
39. RAID / Backup
40. Replication / Backup
41. HA / DR
42. RTO / RPO
43. Vertical / Horizontal Scaling
44. VM / bộ chứa (container / 컨테이너)
45. Authentication / Authorization
46. Hashing / Encryption
47. SQL Injection / XSS
48. Firewall / WAF
49. IDS / IPS
50. Threat / Vulnerability / rủi ro (risk / 위험)

Nếu một cặp chỉ giải thích được sau khi nhìn ghi chú, hãy đánh dấu `CONFUSION GAP` và quay lại deep-dive tương ứng trước khi chuyển sang scenario mới.

> **Bàn giao:** Sau **6.4 Logical tầng (layer / 계층) vs vật lý (physical / 물리적) tầng (layer / 계층)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
