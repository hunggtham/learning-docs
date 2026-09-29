# Môn 2 — 소프트웨어 개발: Deep Dive 2026

> Môn 2 dễ tạo cảm giác “biết rồi” vì nhiều khái niệm quen thuộc với nhà phát triển (developer / 개발자). Tuy nhiên đề thi thường hỏi theo thuật ngữ giáo trình, thứ tự tiến trình (process / 프로세스), độ phức tạp (complexity / 복잡도), kiểm thử (test / 테스트) technique hoặc công cụ (tool / 도구) category. Vì vậy phải chuyển kiến thức nghề nghiệp thành **khả năng phân loại chính xác theo cách đề hỏi**.

## 1. 데이터 입출력 구현 — dữ liệu (data / 데이터) I/O hiện thực (implementation / 구현)

### 1.1 자료구조 — dữ liệu (data / 데이터) Structures

Cấu trúc dữ liệu (data structure / 자료구조) nên học qua ba câu hỏi: dữ liệu được bố trí thế nào, thao tác (operation / 연산) chính là gì, và sự đánh đổi (trade-off / 트레이드오프) thời gian/bộ nhớ ra sao.

**Array** lưu phần tử liên tục nên truy cập chỉ mục (index / 인덱스) O(1), nhưng chèn/xóa giữa thường tốn O(n) vì phải dịch phần tử. **Linked danh sách (list / 목록)** không cần vùng nhớ liên tục, chèn/xóa khi đã có nút (node / 노드) tham chiếu (reference / 참조) có thể O(1), nhưng truy cập phần tử thứ k cần đi tuần tự O(n).

**ngăn xếp (stack / 스택)** dùng LIFO, thao tác (operation / 연산) cơ bản push/pop. Ứng dụng: ngăn xếp lời gọi (call stack / 호출 스택), undo, expression evaluation, DFS. **hàng đợi (queue / 큐)** dùng FIFO, enqueue/dequeue. Ứng dụng: scheduling, buffering, BFS. **Deque** cho phép insert/delete hai đầu.

### 1.2 cây (tree / 트리)

Cây (tree / 트리) có gốc (root / 루트), parent, child, sibling, leaf, mức (level / 수준)/độ sâu (depth / 깊이), degree. nhị phân (binary / 이진) cây (tree / 트리) giới hạn mỗi nút (node / 노드) tối đa hai child.

Traversal phải làm được bằng tay:

- Preorder: gốc (root / 루트) → Left → Right.
- Inorder: Left → gốc (root / 루트) → Right.
- Postorder: Left → Right → gốc (root / 루트).

Trong tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리), với key phân biệt, subtree trái nhỏ hơn nút (node / 노드) và subtree phải lớn hơn nút (node / 노드). Inorder traversal của BST cho chuỗi (sequence / 시퀀스) tăng dần.

Vùng nhớ vùng nhớ động (heap / 힙) không phải BST. Max-Heap chỉ bảo đảm parent ≥ child, không bảo đảm toàn bộ subtree trái nhỏ hơn subtree phải.

### 1.3 đồ thị (graph / 그래프)

Đồ thị (graph / 그래프) gồm vertex và edge. Directed đồ thị (graph / 그래프) phân biệt hướng; undirected đồ thị (graph / 그래프) không. Weighted đồ thị (graph / 그래프) có trọng số cạnh.

BFS dùng hàng đợi (queue / 큐) và đi theo tầng (layer / 계층); DFS thường dùng recursion/ngăn xếp (stack / 스택) và đi sâu trước. Khi đề hỏi shortest đường dẫn (path / 경로) trong **unweighted đồ thị (graph / 그래프)**, BFS là lựa chọn nền tảng. Với weighted đồ thị (graph / 그래프) không âm, nghĩ tới Dijkstra. Với all-pairs shortest đường dẫn (path / 경로), Floyd–Warshall thường là thuật ngữ quen thuộc.

Minimum Spanning cây (tree / 트리) khác shortest đường dẫn (path / 경로). Prim và Kruskal nhằm nối tất cả vertex với tổng trọng số cạnh nhỏ nhất mà không tạo cycle, không phải tìm đường ngắn nhất từ một nguồn (source / 소스).

### 1.4 Expression notation

Infix: `A + B`. Prefix: `+ A B`. Postfix: `A B +`.

Khi chuyển infix sang postfix, operator precedence và parenthesis quyết định vị trí operator. Đừng chỉ học ví dụ cố định; hãy luyện ngăn xếp (stack / 스택) thuật toán (algorithm / 알고리즘).

Ví dụ:

`A + B * C` → `A B C * +`.

`(A + B) * C` → `A B + C *`.

### 1.5 Sorting

Các thuật toán thường cần biết idea và độ phức tạp (complexity / 복잡도) điển hình:

| thuật toán (algorithm / 알고리즘) | Ý tưởng | Average | Worst | Stable điển hình |
|---|---|---:|---:|---|
| Bubble | đổi cặp kề sai thứ tự | O(n²) | O(n²) | Có |
| Selection | chọn min/max mỗi lượt | O(n²) | O(n²) | Không điển hình |
| Insertion | chèn phần tử vào prefix đã sort | O(n²) | O(n²) | Có |
| Merge | chia rồi merge | O(n log n) | O(n log n) | Có |
| Quick | partition quanh pivot | O(n log n) | O(n²) | Không điển hình |
| vùng nhớ động (heap / 힙) | dùng vùng nhớ động (heap / 힙) | O(n log n) | O(n log n) | Không |

Quick Sort thường nhanh trong thực tế nhưng pivot xấu có thể dẫn tới O(n²). Merge Sort ổn định và bảo đảm O(n log n) nhưng cần thêm bộ nhớ (memory / 메모리) cho merge trong hiện thực (implementation / 구현) phổ biến.

### 1.6 Searching

Tuyến tính (linear / 선형) tìm kiếm (search / 검색) O(n) và không cần sorted dữ liệu (data / 데이터). tìm kiếm nhị phân (binary search / 이진 탐색) O(log n) nhưng yêu cầu dữ liệu có thứ tự và truy cập vị trí giữa hiệu quả.

### 1.7 Hashing

Hashing map key thành bucket/chỉ mục (index / 인덱스). Collision là hai key map vào cùng vị trí.

Collision resolution thường gồm:

- Separate Chaining: mỗi bucket chứa danh sách (list / 목록)/cấu trúc (structure / 구조) các entry.
- Open Addressing: tìm slot khác trong bảng (table / 테이블), như tuyến tính (linear / 선형) Probing, Quadratic Probing, Double Hashing.

Tuyến tính (linear / 선형) Probing dễ primary clustering. Double Hashing giảm mẫu (pattern / 패턴) clustering bằng băm (hash / 해시) thứ hai.

Tải (load / 로드) factor `α = number of entries / table size` ảnh hưởng hiệu năng (performance / 성능). Khi α quá cao trong open addressing, probe chuỗi (chain / 사슬) tăng mạnh.

## 2. 통합 구현 — tích hợp (integration / 통합) hiện thực (implementation / 구현)

### 2.1 đơn vị (unit / 단위) mô-đun (module / 모듈)

Đơn vị (unit / 단위) mô-đun (module / 모듈) là phần chức năng có ranh giới (boundary / 경계) rõ, đầu vào (input / 입력)/đầu ra (output / 출력) và responsibility cụ thể. mô-đun (module / 모듈) specification cần đủ rõ để hiện thực (implementation / 구현) và kiểm thử (test / 테스트) độc lập.

Dùng chung (common / 공통) mô-đun (module / 모듈) nên chú ý tính đúng đắn (correctness / 정확성), clarity, completeness, consistency và traceability theo cách diễn đạt của giáo trình. Ý chính là mô-đun (module / 모듈) dùng chung phải có đặc tả hợp đồng (contract / 계약) rõ và không gây interpretation khác nhau giữa nhóm (team / 팀).

### 2.2 IPC — Inter-Process Communication

IPC cho phép tiến trình (process / 프로세스) trao đổi dữ liệu (data / 데이터)/synchronization. Các cơ chế thường gặp: pipe, named pipe, message hàng đợi (queue / 큐), dùng chung (shared / 공유) bộ nhớ (memory / 메모리), socket, semaphore.

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) thường nhanh vì nhiều tiến trình (process / 프로세스) truy cập cùng vùng bộ nhớ (memory / 메모리) nhưng cần synchronization. Message hàng đợi (queue / 큐) tạo ranh giới (boundary / 경계) rõ hơn nhưng có overhead bản sao (copy / 복사)/hàng đợi (queue / 큐). Semaphore chủ yếu đồng bộ quyền truy cập tài nguyên (resource / 자원), không phải kênh truyền payload lớn.

### 2.3 tích hợp (integration / 통합)

Khi tích hợp mô-đun (module / 모듈)/dịch vụ (service / 서비스), cần kiểm soát giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약), dữ liệu (data / 데이터) ánh xạ (mapping / 매핑), lỗi (error / 오류) mã (code / 코드), giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계), thử lại (retry / 재시도) và idempotency. Một thử lại (retry / 재시도) không an toàn có thể tạo duplicate thao tác (operation / 연산); vì vậy “thử lại (retry / 재시도)” không tự động là giải pháp cho mọi giao diện (interface / 인터페이스) lỗi (error / 오류).

## 3. 제품 소프트웨어 패키징 — sản phẩm (product / 제품) Software Packaging

### 3.1 Packaging

Packaging không chỉ zip tệp (file / 파일). Nó bao gồm executable/sản phẩm tạo ra (artifact / 산출물), phụ thuộc (dependency / 의존성), môi trường (environment / 환경)/cấu hình (configuration / 구성), installation procedure, phiên bản (version / 버전) thông tin (information / 정보), bản phát hành (release / 릴리스) ghi chú (note / 노트) và manual cần thiết để deploy/use sản phẩm.

### 3.2 bản phát hành (release / 릴리스) ghi chú (note / 노트)

Bản phát hành (release / 릴리스) ghi chú (note / 노트) thường chứa phiên bản (version / 버전), bản phát hành (release / 릴리스) date, changed features, fixed defects, known issues, phụ thuộc (dependency / 의존성)/môi trường (environment / 환경) và upgrade/di chuyển (migration / 마이그레이션) notes. Đề có thể hỏi thành phần nào không thuộc bản phát hành (release / 릴리스) ghi chú (note / 노트); hãy nhớ bản phát hành (release / 릴리스) ghi chú (note / 노트) giao tiếp **thay đổi của bản phát hành (release / 릴리스)**, không phải thiết kế (design / 설계) specification chi tiết.

### 3.3 DRM

DRM — Digital Rights Management — bảo vệ quyền sử dụng nội dung số. Các khái niệm có thể xuất hiện: content provider, content distributor, clearing house, bên tiêu thụ (consumer / 소비자), packaging, license và rights expression.

DRM khác encryption thuần túy. Encryption chỉ là một cơ chế kỹ thuật; DRM còn quản lý quyền sử dụng, phân phối, license và chính sách (policy / 정책).

### 3.4 cấu hình (configuration / 구성) Management — 형상 관리

SCM kiểm soát sản phẩm tạo ra (artifact / 산출물) và thay đổi trong vòng đời software. Các hoạt động nền tảng thường xoay quanh identification, phiên bản (version / 버전) điều khiển (control / 제어), thay đổi (change / 변경) điều khiển (control / 제어), status accounting và kiểm tra (audit / 감사).

Phiên bản (version / 버전) điều khiển (control / 제어) là một phần của SCM, không phải toàn bộ SCM.

Centralized VCS như SVN dựa nhiều vào central repository. phân tán (distributed / 분산) VCS như Git cho mỗi clone một repository với lịch sử (history / 이력) đầy đủ.

### 3.5 bản dựng (build / 빌드) Automation

Bản dựng (build / 빌드) automation tự động compile, kiểm thử (test / 테스트), gói (package / 패키지) và đôi khi deploy. Jenkins là automation máy chủ (server / 서버)/orchestrator; Gradle/Maven là bản dựng (build / 빌드) tools. Đề dễ trộn category: Jenkins không phải trình biên dịch (compiler / 컴파일러) và Git không phải bản dựng (build / 빌드) công cụ (tool / 도구).

## 4. 애플리케이션 테스트 관리 — ứng dụng (application / 애플리케이션) kiểm thử (test / 테스트) Management

### 4.1 Nguyên lý kiểm thử (test / 테스트)

Một số nguyên lý kinh điển cần hiểu:

Testing cho thấy **sự hiện diện của defect**, không chứng minh tuyệt đối software không còn defect. Exhaustive testing thường bất khả thi. Defect có xu hướng tập trung ở một số mô-đun (module / 모듈) — defect clustering. trường hợp kiểm thử (test case / 테스트 케이스) cần thay đổi theo thời gian để tránh pesticide paradox. Testing phụ thuộc ngữ cảnh (context / 맥락). Sản phẩm không có bug vẫn có thể thất bại nếu không đáp ứng nhu cầu — absence-of-errors fallacy.

### 4.2 xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증)

Xác minh (verification / 확인) kiểm tra sản phẩm tạo ra (artifact / 산출물) có tuân specification/tiến trình (process / 프로세스) không. kiểm tra hợp lệ (validation / 검증) kiểm tra software có đáp ứng nhu cầu người dùng/thực tế không. Hai khái niệm này lặp lại từ Môn 1; nếu vẫn nhầm thì xem là lỗi nền tảng.

### 4.3 White-box testing

White-box dựa vào nội bộ (internal / 내부) lô-gic (logic / 논리)/mã (code / 코드) cấu trúc (structure / 구조).

Coverage thường gặp:

- Statement Coverage: mỗi statement được execute ít nhất một lần.
- quyết định (decision / 결정)/Branch Coverage: mỗi kết quả (outcome / 결과) của quyết định (decision / 결정) được thực hiện.
- điều kiện (condition / 조건) Coverage: mỗi atomic điều kiện (condition / 조건) có True và False.
- điều kiện (condition / 조건)/quyết định (decision / 결정) Coverage: kết hợp điều kiện (condition / 조건) và quyết định (decision / 결정).
- Modified điều kiện (condition / 조건)/quyết định (decision / 결정) Coverage — MC/DC: mỗi điều kiện (condition / 조건) chứng minh ảnh hưởng độc lập tới quyết định (decision / 결정) kết quả (outcome / 결과).

Nếu một `if (A && B)` chỉ kiểm thử (test / 테스트) `(T,T)` và `(F,T)`, ta có thể cover cả kết quả (outcome / 결과) quyết định (decision / 결정) T/F nhưng chưa chắc cover độc lập mọi điều kiện (condition / 조건) theo tiêu chí mạnh hơn.

### 4.4 Cyclomatic độ phức tạp (complexity / 복잡도)

McCabe Cyclomatic độ phức tạp (complexity / 복잡도) đo số đường dẫn (path / 경로) độc lập tuyến tính. Công thức phổ biến:

`V(G) = E - N + 2P`

với E edge, N nút (node / 노드), P số connected thành phần (component / 컴포넌트); điều khiển (control / 제어) luồng (flow / 흐름) đồ thị (graph / 그래프) của một routine thường P=1. Một cách khác thường dùng là số quyết định (decision / 결정) điểm (point / 지점) + 1 trong cấu trúc đơn giản.

Độ phức tạp (complexity / 복잡도) cao thường gợi ý nhiều đường dẫn (path / 경로) cần kiểm thử (test / 테스트) và mã (code / 코드) khó maintain hơn.

### 4.5 Black-box testing

Black-box dựa specification và đầu vào (input / 입력)/đầu ra (output / 출력), không cần biết mã (code / 코드) bên trong.

**Equivalence Partitioning** chia đầu vào (input / 입력) thành lớp (class / 클래스) được kỳ vọng xử lý giống nhau. **ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석)** tập trung ranh giới vì defect hay xuất hiện tại min/max và sát biên. **quyết định (decision / 결정) bảng (table / 테이블)** phù hợp khi nhiều điều kiện (condition / 조건) kết hợp quy tắc (rule / 규칙). **chuyển tiếp trạng thái (state transition / 상태 전이) Testing** phù hợp hành vi (behavior / 동작) phụ thuộc trạng thái (state / 상태). **Cause-Effect đồ thị (graph / 그래프)** biểu diễn quan hệ lô-gic (logic / 논리) giữa điều kiện (condition / 조건) và tác động (effect / 효과).

### 4.6 kiểm thử (test / 테스트) levels

Đơn vị (unit / 단위) kiểm thử (test / 테스트) kiểm tra mô-đun (module / 모듈)/lớp (class / 클래스) nhỏ. kiểm thử tích hợp (integration test / 통합 테스트) kiểm tra tương tác (interaction / 상호작용) giữa mô-đun (module / 모듈). hệ thống (system / 시스템) kiểm thử (test / 테스트) kiểm tra hệ thống hoàn chỉnh với yêu cầu (requirement / 요구사항). Acceptance kiểm thử (test / 테스트) xác nhận hệ thống (system / 시스템) chấp nhận được cho người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스).

Trong V-Model, development sản phẩm tạo ra (artifact / 산출물) ở bên trái tương ứng kiểm thử (test / 테스트) mức (level / 수준) ở bên phải. Mục tiêu là dấu vết (trace / 추적) xác minh (verification / 확인)/kiểm tra hợp lệ (validation / 검증) từ yêu cầu (requirement / 요구사항)/thiết kế (design / 설계) tới kiểm thử (test / 테스트).

### 4.7 Top-down vs Bottom-up tích hợp (integration / 통합)

Top-down bắt đầu từ mô-đun (module / 모듈) cấp cao; mô-đun (module / 모듈) thấp chưa có có thể thay bằng **Stub**. Bottom-up bắt đầu từ mô-đun (module / 모듈) cấp thấp; mô-đun (module / 모듈) gọi phía trên chưa có có thể thay bằng **Driver**.

Mẹo không học vẹt: Stub **được gọi** như một mô-đun (module / 모듈) con giả. Driver **gọi** mô-đun (module / 모듈) đang kiểm thử (test / 테스트) như mô-đun (module / 모듈) cha giả.

### 4.8 kiểm thử (test / 테스트) Oracle

Oracle là nguồn/cơ chế quyết định đầu ra (output / 출력) có đúng không. Các loại hay gặp trong giáo trình: True Oracle, Sampling Oracle, Heuristic Oracle, Consistent Oracle.

True Oracle có expected kết quả (result / 결과) chính xác. Sampling Oracle chỉ kiểm tra mẫu (sample / 표본). Heuristic Oracle dùng heuristic/approximation khi không thể biết expected hoàn hảo. Consistent Oracle so sánh tính nhất quán qua hiện thực (implementation / 구현)/kết quả (result / 결과) liên quan.

### 4.9 kiểm thử (test / 테스트) Harness

Kiểm thử (test / 테스트) Harness là môi trường hỗ trợ thực thi kiểm thử (test / 테스트), có thể gồm driver, stub, kiểm thử (test / 테스트) script, kiểm thử (test / 테스트) dữ liệu (data / 데이터), monitor và công cụ (tool / 도구). Đừng đồng nhất Harness với một kiểm thử (test / 테스트) automation công cụ (tool / 도구) riêng lẻ.

### 4.10 hiệu năng (performance / 성능)

Các chỉ số (metric / 지표) cần phân biệt:

- phản hồi (response / 응답) thời gian (time / 시간): thời gian từ yêu cầu (request / 요청) tới phản hồi (response / 응답).
- thông lượng (throughput / 처리량): lượng công việc (work / 작업)/yêu cầu (request / 요청) xử lý mỗi đơn vị thời gian.
- tài nguyên (resource / 자원) Usage: CPU, bộ nhớ (memory / 메모리), disk, mạng (network / 네트워크).
- TPS: transactions per second.

Độ trễ (latency / 지연 시간) thấp không đồng nghĩa thông lượng (throughput / 처리량) cao và ngược lại.

## 5. 인터페이스 구현 — giao diện (interface / 인터페이스) hiện thực (implementation / 구현)

### 5.1 hiện thực (implementation / 구현)

Giao diện (interface / 인터페이스) hiện thực (implementation / 구현) cần ánh xạ (mapping / 매핑) dữ liệu (data / 데이터), serialization, giao thức (protocol / 프로토콜) handling, authentication, giao dịch (transaction / 트랜잭션)/lỗi (error / 오류) chính sách (policy / 정책) và logging/monitoring. Câu hỏi có thể đưa JSON/XML/API nhưng mục tiêu là nhận ra thành phần (component / 컴포넌트) nào đang làm **dữ liệu (data / 데이터) exchange** chứ không phải lô-gic nghiệp vụ (business logic / 비즈니스 로직).

### 5.2 EAI và ESB

EAI giải bài toán tích hợp enterprise ứng dụng (application / 애플리케이션). Kiểu triển khai có thể Point-to-Point, Hub & Spoke, Message Bus, Hybrid. ESB thường cung cấp bus hạ tầng cho routing, transformation và dịch vụ (service / 서비스) mediation.

### 5.3 giao diện (interface / 인터페이스) bảo mật (security / 보안)

Mạng (network / 네트워크) zone có thể dùng encryption/giao thức (protocol / 프로토콜) bảo mật (security / 보안). ứng dụng (application / 애플리케이션) zone cần kiểm tra hợp lệ (validation / 검증), authentication/authorization, secure coding. cơ sở dữ liệu (database / 데이터베이스) zone cần kiểm soát truy cập (access control / 접근 제어), encryption, kiểm tra (audit / 감사) và integrity.

Integrity check có thể dùng băm (hash / 해시)/checksum. băm (hash / 해시) không dùng để khôi phục plaintext và không phải encryption.

### 5.4 giao diện (interface / 인터페이스) xác minh (verification / 확인) tools

Công cụ (tool / 도구) category thường gặp gồm xUnit-style đơn vị (unit / 단위) kiểm thử (test / 테스트) khung phần mềm (framework / 프레임워크), API testing tools, static/động (dynamic / 동적) phân tích (analysis / 분석), monitoring/APM. Hãy phân loại công cụ (tool / 도구) theo **mục đích**, không học tên công cụ (tool / 도구) đơn độc vì công cụ (tool / 도구) ecosystem thay đổi.

## 6. Các cặp dễ mất điểm
Phần “6. Các cặp dễ mất điểm” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


| Cặp | Phân biệt |
|---|---|
| ngăn xếp (stack / 스택) vs hàng đợi (queue / 큐) | LIFO vs FIFO |
| BFS vs DFS | hàng đợi (queue / 큐)/tầng (layer / 계층) vs ngăn xếp (stack / 스택)/độ sâu (depth / 깊이) |
| BST vs vùng nhớ động (heap / 힙) | total thứ tự (ordering / 순서) theo subtree vs parent-child vùng nhớ động (heap / 힙) thuộc tính (property / 속성) |
| Shortest đường dẫn (path / 경로) vs MST | đường giữa điểm vs cây nối toàn đồ thị (graph / 그래프) |
| tìm kiếm nhị phân (binary search / 이진 탐색) vs băm (hash / 해시) | O(log n) trên sorted thứ tự (order / 순서) vs ánh xạ (mapping / 매핑) key vào bucket |
| SCM vs phiên bản (version / 버전) điều khiển (control / 제어) | quản lý cấu hình (configuration / 구성)/thay đổi (change / 변경) toàn diện vs lịch sử phiên bản (version / 버전) |
| Jenkins vs Gradle | automation máy chủ (server / 서버) vs bản dựng (build / 빌드) công cụ (tool / 도구) |
| White-box vs Black-box | nội bộ (internal / 내부) cấu trúc (structure / 구조) vs specification hành vi (behavior / 동작) |
| Stub vs Driver | mô-đun (module / 모듈) con giả vs mô-đun (module / 모듈) cha giả |
| phản hồi (response / 응답) thời gian (time / 시간) vs thông lượng (throughput / 처리량) | độ trễ (latency / 지연 시간) từng yêu cầu (request / 요청) vs lượng công việc (work / 작업)/thời gian (time / 시간) |
| băm (hash / 해시) vs Encryption | one-way digest/integrity vs reversible confidentiality với key phù hợp |

## 7. Procedural drills

### Drill 1 — Traversal

Cho cây (tree / 트리) có gốc (root / 루트) A, left B, right C; B có D và E; C có F. Viết Preorder, Inorder và Postorder.

### Drill 2 — Postfix

Chuyển `(A + B) * (C - D) / E` sang postfix bằng ngăn xếp (stack / 스택).

### Drill 3 — độ phức tạp (complexity / 복잡도)

Vì sao tìm kiếm nhị phân (binary search / 이진 탐색) không phù hợp trực tiếp với linked danh sách (list / 목록) dù về lý thuyết vẫn có thể tìm “middle” bằng traversal?

### Drill 4 — băm (hash / 해시) collision

Bảng (table / 테이블) kích thước (size / 크기) 10, băm (hash / 해시) `h(k)=k mod 10`, insert 12, 22, 32 bằng tuyến tính (linear / 선형) Probing. Các key nằm ở chỉ mục (index / 인덱스) nào? Sau đó giải thích primary clustering.

### Drill 5 — Coverage

Với `if (A || B)`, tự tạo kiểm thử (test / 테스트) tối thiểu để đạt quyết định (decision / 결정) Coverage rồi so sánh với kiểm thử (test / 테스트) cần để chứng minh từng điều kiện (condition / 조건) ảnh hưởng độc lập.

### Drill 6 — Stub/Driver

Trong top-down tích hợp (integration / 통합), mô-đun (module / 모듈) `OrderService` gọi `PaymentClient` nhưng PaymentClient chưa hoàn thành. Ta cần Stub hay Driver? Vì sao?

### Drill 7 — hiệu năng (performance / 성능)

Một API phản hồi (response / 응답) thời gian (time / 시간) giảm từ 500ms xuống 200ms nhưng số yêu cầu (request / 요청)/second không tăng vì DB liên kết (connection / 연결) pool vẫn giới hạn. chỉ số (metric / 지표) nào cải thiện, chỉ số (metric / 지표) nào gần như không đổi?

## 8. 과락 방지 checklist — Môn 2

Phải tự làm được:

- traversal cây (tree / 트리), BFS/DFS và phân biệt shortest đường dẫn (path / 경로)/MST;
- chuyển infix/prefix/postfix cơ bản;
- nhận diện độ phức tạp (complexity / 복잡도) và đặc tính chính của sorting/searching;
- giải collision hashing cơ bản;
- phân loại IPC và vai trò synchronization;
- giải thích SCM, phiên bản (version / 버전) điều khiển (control / 제어), packaging, DRM, bản dựng (build / 빌드) automation;
- phân biệt kiểm thử (test / 테스트) principle, mức (level / 수준), technique và coverage;
- tính cyclomatic độ phức tạp (complexity / 복잡도) ở điều khiển (control / 제어) luồng (flow / 흐름) đơn giản;
- phân biệt Stub/Driver và Top-down/Bottom-up;
- phân biệt kiểm thử (test / 테스트) oracle/harness;
- nhận biết hiệu năng (performance / 성능) chỉ số (metric / 지표);
- giải thích EAI/ESB và giao diện (interface / 인터페이스) bảo mật (security / 보안).

Nếu chỉ đọc được định nghĩa nhưng không làm được drill, vẫn chưa đủ an toàn cho 필기.
