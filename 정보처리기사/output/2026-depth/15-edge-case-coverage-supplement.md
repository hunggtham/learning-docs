# 정보처리기사 필기 2026 — Edge-Case Coverage Supplement

> tệp (file / 파일) này dùng để bù các vùng kiến thức có **độ salience thấp**: dễ bị bỏ qua vì không nổi bật như UML, SQL hay subnetting, nhưng vẫn nằm trong các chapter đã xác nhận của 필기. Mục tiêu không phải học thêm ngoài phạm vi, mà làm cho coverage trong 21 chapter bớt phụ thuộc vào vài chủ đề quen thuộc.
>
> Cách dùng: chỉ đọc tệp (file / 파일) này sau Master Guide và 5 Deep-Dive. Với mỗi mục, phải trả lời được ba câu: **Nó dùng để làm gì? Nó khác cái gần nhất ở đâu? Một câu hỏi có thể đổi wording thế nào?**

---

# Môn 1 — 소프트웨어 설계

## 1. yêu cầu (requirement / 요구사항) feasibility không đồng nghĩa với yêu cầu (requirement / 요구사항) validity

Một yêu cầu (requirement / 요구사항) có thể phản ánh đúng mong muốn stakeholder nhưng vẫn không khả thi về kỹ thuật, ngân sách hoặc thời gian. Ngược lại, một chức năng hoàn toàn khả thi kỹ thuật vẫn có thể không giải quyết nhu cầu thực.

Hãy tách bốn câu hỏi:

- **Need:** stakeholder có thực sự cần không?
- **Feasibility:** có thể xây trong ràng buộc (constraint / 제약조건) không?
- **Priority:** có đáng làm trước không?
- **Verifiability:** có thể kiểm chứng rõ ràng không?

Nếu yêu cầu (requirement / 요구사항) nói “hệ thống phải rất nhanh”, vấn đề đầu tiên là **không verifiable** vì thiếu threshold. Nếu nói “mọi yêu cầu (request / 요청) phải trả trong 1 microsecond trên mobile mạng (network / 네트워크)”, nó measurable nhưng có thể **không feasible**.

## 2. yêu cầu (requirement / 요구사항) ambiguity vs incompleteness vs inconsistency

**Ambiguity — 모호성:** một câu có nhiều cách hiểu.
**Incompleteness — 불완전성:** thiếu trường hợp hoặc thông tin cần thiết.
**Inconsistency — 불일치성:** hai yêu cầu (requirement / 요구사항) mâu thuẫn nhau.

Ví dụ:

```text
R1: 비밀번호는 최소 8자이다.
R2: 비밀번호는 정확히 6자여야 한다.
```

Đây là inconsistency, không phải ambiguity.

## 3. DFD balancing

Khi phân rã một tiến trình (process / 프로세스) từ mức (level / 수준) cao xuống mức (level / 수준) thấp, đầu vào (input / 입력)/đầu ra (output / 출력) luồng dữ liệu (data flow / 데이터 흐름) bên ngoài của tiến trình (process / 프로세스) phải được bảo toàn về mặt lô-gic (logic / 논리). Đây là **balancing**.

Nếu ngữ cảnh (context / 맥락) diagram có đầu vào (input / 입력) `Order` và đầu ra (output / 출력) `Receipt`, nhưng mức (level / 수준) con bỗng tạo thêm bên ngoài (external / 외부) đầu ra (output / 출력) `CreditScore` chưa xuất hiện ở ranh giới (boundary / 경계) mức (level / 수준) trên, cần kiểm tra consistency của decomposition.

## 4. dữ liệu (data / 데이터) Dictionary và Mini-specification

Dữ liệu (data / 데이터) Dictionary định nghĩa **dữ liệu (data / 데이터) element/cấu trúc dữ liệu (data structure / 자료구조)**. Mini-specification định nghĩa **lô-gic (logic / 논리) xử lý** của tiến trình (process / 프로세스) thấp.

Nếu đề mô tả “định nghĩa cấu trúc của CUSTOMER = ID + NAME + ...” → dữ liệu (data / 데이터) Dictionary.
Nếu đề mô tả “nếu amount > 1,000 thì manager approval” → Mini-spec/quyết định (decision / 결정) lô-gic (logic / 논리).

## 5. quyết định (decision / 결정) bảng (table / 테이블) vs cây quyết định (decision tree / 의사결정 트리)

Quyết định (decision / 결정) bảng (table / 테이블) hữu ích khi có nhiều điều kiện (condition / 조건)/hành động (action / 동작) combinations cần kiểm tra coverage có hệ thống. cây quyết định (decision tree / 의사결정 트리) trực quan hóa chuỗi (sequence / 시퀀스)/branch quyết định (decision / 결정).

Đừng chọn theo hình thức “bảng (table / 테이블) dễ nhìn hơn”. Hỏi: có cần **liệt kê tổ hợp điều kiện (condition / 조건)** và hành động (action / 동작) tương ứng không?

## 6. UML relationship: realization

Realization — 실체화 — thường dùng khi lớp (class / 클래스)/thành phần (component / 컴포넌트) hiện thực giao diện (interface / 인터페이스)/specification.

Generalization là subtype/inheritance quan hệ (relation / 관계). Realization gần “implements đặc tả hợp đồng (contract / 계약)” hơn “is-a lớp (class / 클래스) hierarchy” thuần túy.

## 7. Include vs Extend trong Use trường hợp (case / 사례)

`<<include>>` thể hiện hành vi (behavior / 동작) chung được use trường hợp (case / 사례) gốc **luôn gọi như phần bắt buộc** trong luồng (flow / 흐름) được mô hình hóa.
`<<extend>>` thêm hành vi (behavior / 동작) **tùy điều kiện/extension điểm (point / 지점)**.

Ví dụ `Checkout` include `Authenticate Payment`; `Apply Coupon` có thể extend luồng (flow / 흐름) khi người dùng (user / 사용자) có coupon.

## 8. trạng thái (state / 상태) vs Activity Diagram

Trạng thái (state / 상태) Diagram tập trung **một đối tượng (object / 객체) thay đổi trạng thái (state / 상태) theo sự kiện (event / 이벤트)**. Activity Diagram tập trung **workflow/điều khiển (control / 제어) luồng (flow / 흐름)** giữa hành động (action / 동작).

Một thứ tự (order / 순서) đi `CREATED → PAID → SHIPPED → DELIVERED` → trạng thái (state / 상태).
Một nghiệp vụ (business / 비즈니스) tiến trình (process / 프로세스) có fork/phép nối (join / 조인) giữa “verify stock” và “fraud check” → Activity.

## 9. thành phần (component / 컴포넌트) vs triển khai (deployment / 배포) Diagram

Thành phần (component / 컴포넌트) Diagram hỏi **software pieces và phụ thuộc (dependency / 의존성)**. triển khai (deployment / 배포) Diagram hỏi **sản phẩm tạo ra (artifact / 산출물)/thành phần (component / 컴포넌트) chạy trên nút (node / 노드) nào**.

Nếu đề nói Web máy chủ (server / 서버), App máy chủ (server / 서버), DB máy chủ (server / 서버) như vật lý (physical / 물리적)/thời gian chạy (runtime / 런타임) nodes → triển khai (deployment / 배포).

## 10. kiến trúc (architecture / 아키텍처) chất lượng (quality / 품질) sự đánh đổi (trade-off / 트레이드오프)

Layering tăng separation nhưng có thể tăng độ trễ (latency / 지연 시간)/lời gọi (call / 호출) overhead. Central repository đơn giản hóa sharing nhưng tạo central phụ thuộc (dependency / 의존성). Client-server tập trung dịch vụ (service / 서비스) nhưng máy chủ (server / 서버) có thể thành bottleneck/thất bại (failure / 실패) concentration.

Không có kiến trúc (architecture / 아키텍처) style “luôn tốt hơn”; đáp án đúng thường gắn với yêu cầu (requirement / 요구사항) cụ thể.

## 11. Cohesion nuance: sequential vs communicational

**Sequential cohesion:** đầu ra (output / 출력) của một phần là đầu vào (input / 입력) cho phần tiếp theo.
**Communicational cohesion:** nhiều thao tác (operation / 연산) cùng dùng/chỉnh cùng dữ liệu (data / 데이터) set.

Nếu mô-đun (module / 모듈) `read → parse → transform` theo chuỗi xử lý (pipeline / 파이프라인) → sequential. Nếu mô-đun (module / 모듈) có `create/read/update` cùng trên Customer bản ghi (record / 레코드) → communicational có thể gần hơn.

## 12. bên ngoài (external / 외부) coupling

Bên ngoài (external / 외부) coupling xảy ra khi modules phụ thuộc vào bên ngoài (external / 외부) format/giao thức (protocol / 프로토콜)/thiết bị (device / 장치) giao diện (interface / 인터페이스) chung.

Ví dụ hai mô-đun (module / 모듈) cùng phụ thuộc một tệp (file / 파일) format hoặc communication giao thức (protocol / 프로토콜) bên ngoài. Nó khác dùng chung (common / 공통) Coupling là **share toàn cục (global / 전역) dữ liệu (data / 데이터)**.

## 13. Fan-in không tự động đồng nghĩa tốt

Fan-in cao có thể cho thấy reuse tốt, nhưng một utility “god mô-đun (module / 모듈)” được mọi nơi gọi vì chứa quá nhiều responsibility vẫn có thiết kế (design / 설계) smell.

Chỉ số (metric / 지표) là tín hiệu (signal / 신호), không phải verdict.

## 14. giao diện (interface / 인터페이스) lỗi (error / 오류) ngữ nghĩa (semantics / 의미론)

API/giao diện (interface / 인터페이스) specification không chỉ có trường dữ liệu (field / 필드). Cần xác định:

- kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류);
- authentication/authorization thất bại (failure / 실패);
- nghiệp vụ (business / 비즈니스) rejection;
- transient hạ tầng (infrastructure / 인프라) lỗi (error / 오류);
- hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) hành vi (behavior / 동작);
- duplicate yêu cầu (request / 요청) ngữ nghĩa (semantics / 의미론).

Nếu tất cả lỗi đều trả một mã chung, bên tiêu thụ (consumer / 소비자) khó quyết định có thử lại (retry / 재시도) được hay không.

## 15. dữ liệu (data / 데이터) format tính tương thích (compatibility / 호환성)

Tính tương thích (compatibility / 호환성) có thể phá vì:

- rename trường dữ liệu (field / 필드);
- thay đổi (change / 변경) kiểu (type / 타입);
- thay đổi (change / 변경) nullability;
- thay đổi (change / 변경) enum giá trị (value / 값);
- thay đổi (change / 변경) ngữ nghĩa (semantic / 의미적) nhưng giữ tên;
- thay đổi (change / 변경) thứ tự (ordering / 순서)/encoding các giả định (assumptions / 가정들).

Thay lược đồ (schema / 스키마) không chỉ là cú pháp (syntax / 문법) issue; ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성) quan trọng hơn.

---

# Môn 2 — 소프트웨어 개발

## 16. ADT vs hiện thực (implementation / 구현)

Ngăn xếp (stack / 스택) là **abstract dữ liệu (data / 데이터) kiểu (type / 타입)** với push/pop/top ngữ nghĩa (semantics / 의미론). Nó có thể được implement bằng array hoặc linked danh sách (list / 목록).

Đừng đồng nhất ADT với cấu trúc (structure / 구조) hiện thực (implementation / 구현) cụ thể.

## 17. vùng nhớ động (heap / 힙) vs BST

Vùng nhớ vùng nhớ động (heap / 힙) chỉ đảm bảo parent-child thứ tự (ordering / 순서) phù hợp vùng nhớ động (heap / 힙) thuộc tính (property / 속성); nó không duy trì full BST thứ tự (ordering / 순서) giữa left/right subtree.

Max-heap gốc (root / 루트) cho maximum nhanh. BST hỗ trợ ordered tìm kiếm (search / 검색)/phạm vi (range / 범위) tốt khi balanced phù hợp.

## 18. Complete nhị phân (binary / 이진) cây (tree / 트리)

Complete nhị phân (binary / 이진) cây (tree / 트리) điền nút (node / 노드) theo mức (level / 수준) từ trái sang phải, ngoại trừ mức (level / 수준) cuối có thể chưa đầy. vùng nhớ động (heap / 힙) thường được lưu hiệu quả bằng array nhờ tính chất này.

## 19. AVL/Balanced cây (tree / 트리) lập luận (reasoning / 추론)

Balanced cây (tree / 트리) tồn tại để tránh height suy thoái thành O(n) như BST lệch. Không cần giả định mọi BST tự cân bằng.

Nếu insert key đã sorted vào naive BST, cây (tree / 트리) có thể thành chuỗi (chain / 사슬).

## 20. đồ thị (graph / 그래프) representations

Adjacency ma trận (matrix / 행렬): bộ nhớ (memory / 메모리) O(V²), edge lookup nhanh.
Adjacency danh sách (list / 목록): bộ nhớ (memory / 메모리) O(V+E), phù hợp sparse đồ thị (graph / 그래프).

Nếu đồ thị (graph / 그래프) cực sparse, ma trận (matrix / 행렬) có thể lãng phí bộ nhớ (memory / 메모리).

## 21. MST vs shortest đường dẫn (path / 경로)

Minimum Spanning cây (tree / 트리) nối **tất cả vertices** với total edge weight nhỏ nhất, không cycle. Shortest đường dẫn (path / 경로) tối ưu đường từ nguồn (source / 소스) tới mục tiêu (target / 대상)/all targets.

Prim/Kruskal ≠ Dijkstra.

## 22. Stable sorting

Stable sort bảo toàn relative thứ tự (order / 순서) của records có key bằng nhau.

Nếu sort employee theo department sau khi đã stable-sort theo hire date, stability có thể có ý nghĩa cho multi-key thứ tự (ordering / 순서) chiến lược (strategy / 전략).

## 23. In-place vs out-of-place

In-place thuật toán (algorithm / 알고리즘) dùng auxiliary bộ nhớ (memory / 메모리) nhỏ theo đầu vào (input / 입력) kích thước (size / 크기), còn out-of-place cần buffer đáng kể. Merge Sort array hiện thực (implementation / 구현) điển hình cần auxiliary array; vùng nhớ động (heap / 힙) Sort có thể in-place.

## 24. Collision ≠ duplicate key

Băm (hash / 해시) collision là **khác key nhưng cùng băm (hash / 해시)/chỉ mục (index / 인덱스)**. Duplicate key là cùng logical key xuất hiện lại.

Collision resolution không tự giải nghiệp vụ (business / 비즈니스) duplicate ngữ nghĩa (semantics / 의미론).

## 25. Open addressing deletion

Trong open addressing, xóa một slot bằng cách biến nó thành “never occupied” có thể phá probe chuỗi (chain / 사슬). Thường cần tombstone/deleted marker hoặc rehash chiến lược (strategy / 전략).

Đây là ví dụ cho việc hiện thực (implementation / 구현) detail ảnh hưởng tính đúng đắn (correctness / 정확성).

## 26. Static testing vs động (dynamic / 동적) testing

Static testing không chạy program: rà soát (review / 검토), inspection, static phân tích (analysis / 분석). động (dynamic / 동적) testing chạy program với inputs.

Rà soát mã (code review / 코드 리뷰) có thể tìm bug mà không cần execute.

## 27. lỗi (error / 오류), Defect/Fault, thất bại (failure / 실패)

Human lỗi (error / 오류) có thể tạo defect/fault trong sản phẩm tạo ra (artifact / 산출물). Khi defect được kích hoạt thời gian chạy (runtime / 런타임), hệ thống (system / 시스템) có thể thất bại (failure / 실패) observable.

Ba tầng này không đồng nghĩa.

## 28. trường hợp kiểm thử (test case / 테스트 케이스) vs kiểm thử (test / 테스트) điều kiện (condition / 조건)

Kiểm thử (test / 테스트) điều kiện (condition / 조건) là aspect/scenario cần kiểm thử (test / 테스트). trường hợp kiểm thử (test case / 테스트 케이스) cụ thể hóa precondition, đầu vào (input / 입력), steps, expected kết quả (result / 결과).

“Nên kiểm thử (test / 테스트) password ranh giới (boundary / 경계)” là điều kiện (condition / 조건); “7-char → reject, 8-char → accept” là concrete cases.

## 29. Equivalence Partition không thay ranh giới (boundary / 경계) giá trị (value / 값)

Equivalence Partition chia đầu vào (input / 입력) thành classes được kỳ vọng behave giống nhau. ranh giới (boundary / 경계) giá trị (value / 값) tập trung cạnh của ranges vì lỗi thường nằm quanh boundaries.

Hai technique bổ sung nhau.

## 30. Statement 100% không bảo đảm Branch 100%

Một `if` có thể execute statement trong true branch mà chưa từng exercise false kết quả (outcome / 결과). Do đó statement coverage 100% vẫn có thể thiếu quyết định (decision / 결정) kết quả (outcome / 결과).

## 31. điều kiện (condition / 조건) coverage vs branch coverage

Với compound điều kiện (condition / 조건) `A && B`, branch coverage chỉ cần overall quyết định (decision / 결정) true/false. điều kiện (condition / 조건) coverage quan tâm từng atomic điều kiện (condition / 조건) nhận true/false.

Không suy rằng một chỉ số (metric / 지표) luôn subsume chỉ số (metric / 지표) kia trong mọi form nếu không xét criterion formal.

## 32. Smoke vs regression

Smoke kiểm thử (test / 테스트) là shallow check để biết bản dựng (build / 빌드) đủ ổn cho testing tiếp. Regression kiểm thử (test / 테스트) kiểm hành vi (behavior / 동작) cũ sau thay đổi (change / 변경).

Một smoke suite có thể cũng chạy lại nhiều lần, nhưng intent khác regression.

## 33. Alpha vs beta nuance

Alpha thường diễn ra trong môi trường controlled của tổ chức phát triển. Beta đưa sản phẩm cho bên ngoài (external / 외부)/representative users trong ngữ cảnh (context / 맥락) gần thực tế hơn.

## 34. cấu hình (configuration / 구성) item

Cấu hình (configuration / 구성) Item không chỉ mã nguồn (source code / 소스 코드). Có thể gồm yêu cầu (requirement / 요구사항) document, bản dựng (build / 빌드) script, lược đồ (schema / 스키마), cấu hình (config / 설정), kiểm thử (test / 테스트) sản phẩm tạo ra (artifact / 산출물), nhị phân (binary / 이진), manual.

## 35. bản dựng (build / 빌드) vs bản phát hành (release / 릴리스)

Bản dựng (build / 빌드) biến nguồn (source / 소스)/phụ thuộc (dependency / 의존성) thành sản phẩm tạo ra (artifact / 산출물). bản phát hành (release / 릴리스) là quyết định (decision / 결정)/tiến trình (process / 프로세스) đưa một phiên bản xác định tới môi trường (environment / 환경)/người dùng (user / 사용자).

Nhiều bản dựng (build / 빌드) không trở thành bản phát hành (release / 릴리스).

## 36. DRM roles ở mức khái niệm

DRM liên quan quyền sử dụng nội dung số: license, key, usage chính sách (policy / 정책), packaging/protection và enforcement. Đừng nhầm với nguồn (source / 소스) phiên bản (version / 버전) điều khiển (control / 제어) hoặc vận chuyển (transport / 전송) encryption đơn thuần.

## 37. giao diện (interface / 인터페이스) monitoring

Tích hợp (integration / 통합) môi trường vận hành (production / 운영 환경) cần quan sát độ trễ (latency / 지연 시간), lỗi (error / 오류) tỷ lệ (rate / 비율), thông lượng (throughput / 처리량), thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃), hàng đợi (queue / 큐) backlog và lược đồ (schema / 스키마)/đặc tả hợp đồng (contract / 계약) thất bại (failure / 실패). giao diện (interface / 인터페이스) “đã implement” nhưng không observable rất khó vận hành.

## 38. Idempotency vs deduplication

Idempotency là thuộc tính (property / 속성) khi repeated same thao tác (operation / 연산) không làm thay đổi kết quả (outcome / 결과) sau lần đầu theo ngữ nghĩa (semantics / 의미론). Deduplication là technique phát hiện/loại duplicate events/requests.

Deduplication có thể là một cách implement idempotency, nhưng hai từ không đồng nghĩa hoàn toàn.

---

# Môn 3 — 데이터베이스 구축

## 39. lĩnh vực (domain / 도메인) và attribute

Lĩnh vực (domain / 도메인) là tập giá trị hợp lệ về kiểu (type / 타입)/ràng buộc (constraint / 제약조건) ngữ nghĩa (semantics / 의미론). Attribute là named thuộc tính (property / 속성) trong quan hệ (relation / 관계).

`Age` là attribute; integers 0–150 có thể là conceptual lĩnh vực (domain / 도메인).

## 40. Degree vs cardinality

Degree — 차수 — số attributes/columns.
Cardinality — 카디널리티 — số tuples/rows trong quan hệ (relation / 관계) theo relational terminology cơ bản.

Trong truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화), cardinality còn được dùng cho row count/estimated row count; đừng nhầm với selectivity.

## 41. Natural key vs surrogate key

Natural key có nghiệp vụ (business / 비즈니스) meaning; surrogate key được tạo để identify row. Surrogate key không loại bỏ nhu cầu unique ràng buộc (constraint / 제약조건) trên nghiệp vụ (business / 비즈니스) candidate key nếu nghiệp vụ (business / 비즈니스) vẫn yêu cầu uniqueness.

## 42. Composite key nuance

Composite key gồm nhiều attributes. Partial phụ thuộc (dependency / 의존성) mới trở thành vấn đề 2NF khi non-prime attribute phụ thuộc một **proper subset** của candidate key composite.

## 43. Prime attribute

Prime attribute là attribute thuộc ít nhất một candidate key. Non-prime không thuộc candidate key nào.

Formal 3NF điều kiện (condition / 조건) dùng khái niệm prime attribute; không chỉ học “loại transitive phụ thuộc (dependency / 의존성)” như shortcut.

## 44. Trivial FD

FD `X → Y` là trivial nếu `Y ⊆ X`.

Ví dụ `{A,B} → A` luôn đúng theo relational phụ thuộc (dependency / 의존성) definition, không cung cấp thông tin (information / 정보) mới.

## 45. Lossless decomposition

Decomposition tốt cần tránh tạo spurious tuples khi phép nối (join / 조인) lại. Lossless phép nối (join / 조인) bảo đảm phép nối (join / 조인) các quan hệ (relation / 관계) con khôi phục đúng quan hệ (relation / 관계) gốc theo phụ thuộc (dependency / 의존성) các giả định (assumptions / 가정들).

Normalization không chỉ là “chia bảng nhỏ”.

## 46. phụ thuộc (dependency / 의존성) preservation

Dependency-preserving decomposition cho phép enforce dependencies bằng cách kiểm từng quan hệ (relation / 관계) con mà không cần phép nối (join / 조인) phức tạp.

BCNF decomposition có thể lossless nhưng không luôn preserve mọi phụ thuộc (dependency / 의존성); đây là sự đánh đổi (trade-off / 트레이드오프) lý thuyết quan trọng.

## 47. View updatability

Không phải mọi view đều dễ cập nhật (update / 업데이트). Aggregation, GROUP BY, DISTINCT hoặc phép nối (join / 조인) phức tạp có thể làm cập nhật (update / 업데이트) ambiguous/không được DBMS cho phép.

## 48. Clustered concept

Một lưu trữ (storage / 저장소) organization/chỉ mục (index / 인덱스) có thể ảnh hưởng vật lý (physical / 물리적) thứ tự (ordering / 순서)/locality, nhưng chính xác (exact / 정확한) ngữ nghĩa (semantics / 의미론) phụ thuộc DBMS. Trong thi lý thuyết, hiểu ý tưởng **dữ liệu (data / 데이터) được tổ chức gần thứ tự (order / 순서) của key** và một bảng (table / 테이블) không thể có nhiều vật lý (physical / 물리적) thứ tự (order / 순서) độc lập cùng lúc.

## 49. Covering chỉ mục (index / 인덱스)

Nếu chỉ mục (index / 인덱스) chứa đủ columns để trả truy vấn (query / 쿼리) mà không cần lookup row/bảng (table / 테이블) thêm, truy vấn (query / 쿼리) có thể được “covered”. Nhưng chỉ mục (index / 인덱스) rộng hơn tăng lưu trữ (storage / 저장소) và ghi (write / 쓰기) maintenance.

## 50. Selectivity

Selectivity cao thường nghĩa predicate giữ ít rows hơn tương đối, làm chỉ mục (index / 인덱스) có thể hữu ích hơn. Column boolean với 50/50 phân phối (distribution / 분포) thường selectivity thấp hơn unique ID.

## 51. Sargability

Predicate có form cho phép DB dùng chỉ mục (index / 인덱스) tìm kiếm (search / 검색) hiệu quả được gọi sargable trong thực hành DB. Ví dụ hàm (function / 함수) áp lên indexed column có thể làm optimizer khó dùng phạm vi (range / 범위) seek tùy DBMS.

Concept này nối SQL cú pháp (syntax / 문법) với vật lý (physical / 물리적) truy cập (access / 접근) đường dẫn (path / 경로).

## 52. NULL lô-gic (logic / 논리)

SQL dùng three-valued lô-gic (logic / 논리): TRUE/FALSE/UNKNOWN. `col = NULL` không dùng để kiểm thử (test / 테스트) nullness; dùng `IS NULL`.

`NOT IN` với NULL trong subquery có thể cho kết quả (result / 결과) bất ngờ do UNKNOWN; phải lập luận (reasoning / 추론) cẩn thận.

## 53. UNION vs UNION ALL

UNION loại duplicate, thường cần additional công việc (work / 작업). UNION ALL giữ tất cả rows.

Nếu nghiệp vụ (business / 비즈니스) không cần deduplicate, UNION ALL thường tránh chi phí (cost / 비용) loại trùng.

## 54. Correlated subquery

Correlated subquery tham chiếu row từ outer truy vấn (query / 쿼리). mô hình tư duy (mental model / 사고 모델) là inner lô-gic (logic / 논리) phụ thuộc hiện tại (current / 현재) outer row, dù optimizer có thể transform thực thi (execution / 실행).

## 55. giao dịch (transaction / 트랜잭션) savepoint

SAVEPOINT cho phép quay lui (rollback / 롤백) một phần giao dịch (transaction / 트랜잭션) tới marker, không nhất thiết quay lui (rollback / 롤백) toàn giao dịch (transaction / 트랜잭션). chính xác (exact / 정확한) cú pháp (syntax / 문법)/hành vi (behavior / 동작) DBMS-specific nhưng concept là partial quay lui (rollback / 롤백) điểm (point / 지점).

## 56. Recoverability vs serializability

Serializability liên quan tính đúng đắn (correctness / 정확성) của concurrent interleaving như serial thứ tự (order / 순서). Recoverability liên quan lần ghi nhận (commit / 커밋) phụ thuộc (dependency / 의존성) và khả năng khôi phục (recovery / 복구) khi giao dịch (transaction / 트랜잭션) abort.

Một schedule có thể xét hai properties khác nhau.

## 57. Cascading quay lui (rollback / 롤백)

Nếu T2 đọc uncommitted giá trị (value / 값) từ T1 rồi T1 abort, T2 có thể phải quay lui (rollback / 롤백) theo → cascading quay lui (rollback / 롤백).

Strict scheduling/appropriate isolation giúp tránh chuỗi (chain / 사슬) này.

## 58. Two-Phase Locking concept

2PL có growing phase acquire locks và shrinking phase bản phát hành (release / 릴리스) locks; sau khi bắt đầu bản phát hành (release / 릴리스) thì không acquire khóa (lock / 잠금) mới theo basic 2PL.

2PL hỗ trợ xung đột (conflict / 충돌) serializability nhưng variants khác nhau ảnh hưởng recoverability/deadlock.

## 59. Deadlock đồ thị (graph / 그래프)

Wait-for đồ thị (graph / 그래프) nút (node / 노드) là transactions/processes, edge `Ti → Tj` nghĩa Ti đang chờ tài nguyên (resource / 자원) do Tj giữ. Cycle có thể chỉ ra deadlock trong single-instance khóa (lock / 잠금) mô hình (model / 모델).

## 60. Checkpoint không phải backup

Checkpoint giảm lượng log/khôi phục (recovery / 복구) công việc (work / 작업) cần scan bằng cách ghi khôi phục (recovery / 복구) trạng thái (state / 상태)/coordination. Backup là bản sao (copy / 복사) dữ liệu (data / 데이터) phục vụ restore.

## 61. Logical vs vật lý (physical / 물리적) backup

Logical backup có thể xuất lược đồ (schema / 스키마)/dữ liệu (data / 데이터) dưới dạng SQL/records; vật lý (physical / 물리적) backup bản sao (copy / 복사) lưu trữ (storage / 저장소) pages/files. sự đánh đổi (trade-off / 트레이드오프) về portability, speed, restore granularity khác nhau.

## 62. di chuyển (migration / 마이그레이션) kiểm tra hợp lệ (validation / 검증) dimensions

Không chỉ row count. Cần xem:

- count;
- checksum/băm (hash / 해시) khi phù hợp;
- key uniqueness;
- referential integrity;
- aggregate reconciliation;
- nghiệp vụ (business / 비즈니스) invariants;
- encoding/timezone/precision.

---

# Môn 4 — 프로그래밍 언어 활용

## 63. Compile-time vs thời gian chạy (runtime / 런타임) lỗi (error / 오류)

Cú pháp (syntax / 문법)/kiểu (type / 타입) lỗi (error / 오류) có thể bị phát hiện compile-time tùy ngôn ngữ (language / 언어). Null dereference, divide-by-zero, bounds lỗi (error / 오류) có thể thời gian chạy (runtime / 런타임).

Không suy mọi bug đều compile lỗi (error / 오류) chỉ vì mã (code / 코드) “sai”.

## 64. Static vs động (dynamic / 동적) typing

Static typing kiểm kiểu (type / 타입) quan hệ (relation / 관계) chủ yếu trước thời gian chạy (runtime / 런타임); động (dynamic / 동적) typing gắn/check kiểu (type / 타입) ở thời gian chạy (runtime / 런타임). Cả hai vẫn có strong/weak typing nuances; đừng equate static = compiled, động (dynamic / 동적) = interpreted tuyệt đối.

## 65. phạm vi (scope / 범위) vs thời gian tồn tại (lifetime / 수명)

Variable có thể out of phạm vi (scope / 범위) nhưng đối tượng (object / 객체) vẫn sống nếu còn tham chiếu (reference / 참조). Static cục bộ (local / 로컬) có lexical cục bộ (local / 로컬) phạm vi (scope / 범위) nhưng thời gian tồn tại (lifetime / 수명) lâu.

## 66. ngăn xếp (stack / 스택) vs bộ nhớ vùng động (heap memory / 힙 메모리)

Ngăn xếp lời gọi (call stack / 호출 스택) thường giữ frame/cục bộ (local / 로컬) điều khiển (control / 제어) trạng thái (state / 상태); vùng nhớ động (heap / 힙) dùng động (dynamic / 동적) objects/allocation. chính xác (exact / 정확한) ngôn ngữ (language / 언어) thời gian chạy (runtime / 런타임) có lớp trừu tượng (abstraction / 추상화) riêng, nhưng exam concept nên tách automatic lời gọi (call / 호출) thời gian tồn tại (lifetime / 수명) và động (dynamic / 동적) allocation.

## 67. C pointer to pointer

`int **pp` chứa address của `int*`. Dereference một lần → pointer; hai lần → int giá trị (value / 값).

Câu pointer nhiều lớp phải vẽ address/giá trị (value / 값) bảng (table / 테이블), không dấu vết (trace / 추적) trong đầu.

## 68. C array parameter

Khi truyền array vào hàm (function / 함수) parameter theo cú pháp thông thường, parameter thường được điều chỉnh thành pointer kiểu (type / 타입). Vì vậy `sizeof(param)` trong hàm (function / 함수) không cho total array kích thước (size / 크기) như ở original array đối tượng (object / 객체).

## 69. C struct vs union

Struct members có lưu trữ (storage / 저장소) riêng (với padding). Union members share lưu trữ (storage / 저장소). Union kích thước (size / 크기) thường đủ chứa largest member + alignment.

## 70. Java static phương thức (method / 메서드) vs overriding

Static phương thức (method / 메서드) không dynamic-dispatch như instance overriding; phương thức (method / 메서드) hiding/resolution khác. Nếu đề trộn `static`, đừng áp dụng máy móc quy tắc (rule / 규칙) `A x = new B(); x.f()` của instance phương thức (method / 메서드).

## 71. Java equals vs tham chiếu (reference / 참조) định danh (identity / 식별자)

`==` với đối tượng (object / 객체) references kiểm tham chiếu (reference / 참조) định danh (identity / 식별자); `.equals()` có thể được override để kiểm logical equality.

String literals/interning làm đầu ra (output / 출력) puzzle dễ gây nhầm; tập trung ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약), không mẹo tình cờ.

## 72. Java checked vs unchecked exception

Checked exception thường phải catch/declare. RuntimeException hierarchy là unchecked. Nhưng “checked = recoverable” và “unchecked = unrecoverable” không phải định nghĩa formal.

## 73. Python shallow vs deep bản sao (copy / 복사)

Shallow bản sao (copy / 복사) tạo outer bộ chứa (container / 컨테이너) mới nhưng nested objects vẫn dùng chung (shared / 공유). Deep bản sao (copy / 복사) recursively bản sao (copy / 복사) đối tượng (object / 객체) đồ thị (graph / 그래프) theo khả năng/thư viện (library / 라이브러리) ngữ nghĩa (semantics / 의미론).

## 74. Python default mutable argument

Default argument được evaluate khi hàm (function / 함수) definition executed, không mỗi lời gọi (call / 호출). Mutable default có thể giữ trạng thái (state / 상태) qua calls.

Concept này kiểm tra thời gian tồn tại (lifetime / 수명)/evaluation, không chỉ cú pháp (syntax / 문법).

## 75. tiến trình (process / 프로세스) scheduling arrival thời gian (time / 시간)

Không được sort chỉ theo burst nếu tiến trình (process / 프로세스) chưa arrive. SJF/SRTF selection xét ready processes tại thời điểm scheduling.

## 76. phản hồi (response / 응답) thời gian (time / 시간) vs waiting thời gian (time / 시간)

Phản hồi (response / 응답) thời gian (time / 시간) = lần đầu được CPU − arrival. Waiting thời gian (time / 시간) = tổng thời gian ở ready hàng đợi (queue / 큐).

Một tiến trình (process / 프로세스) có thể phản hồi (response / 응답) sớm nhưng sau đó chờ nhiều lần → waiting lớn.

## 77. Starvation vs deadlock

Starvation: một tiến trình (process / 프로세스) có thể chờ vô hạn vì scheduling/tài nguyên (resource / 자원) unfairness dù hệ thống (system / 시스템) vẫn tiến. Deadlock: set processes chờ vòng nhau và không tiến.

## 78. Aging

Aging tăng priority của tiến trình (process / 프로세스) chờ lâu để giảm starvation trong priority scheduling.

## 79. nội bộ (internal / 내부) vs bên ngoài (external / 외부) fragmentation

Fixed-size allocation có thể lãng phí bên trong allocated khối (block / 블록) → nội bộ (internal / 내부). Variable-size contiguous allocation có holes bên ngoài → bên ngoài (external / 외부).

## 80. TLB

Translation Lookaside Buffer bộ nhớ đệm (cache / 캐시) recent virtual-to-physical address translations để giảm page-table lookup chi phí (cost / 비용).

TLB miss không đồng nghĩa page fault: page có thể resident nhưng translation không có trong TLB.

## 81. Demand paging

Page được tải (load / 로드) khi được referenced, thay vì tải (load / 로드) toàn bộ trước. Nó dựa locality để giảm bộ nhớ (memory / 메모리) footprint/I/O ban đầu, nhưng page fault chi phí (cost / 비용) cao khi miss.

## 82. FIFO Belady anomaly

FIFO có thể tăng page faults khi tăng số frames đối với một số tham chiếu (reference / 참조) strings. LRU/Optimal thuộc ngăn xếp (stack / 스택) algorithms nên không có anomaly này theo thuộc tính (property / 속성) classic.

## 83. IPv4 private ranges

Private IPv4 ranges thường cần nhận diện:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Đừng nhầm toàn bộ `172.x.x.x` là private.

## 84. mạng (network / 네트워크) address vs host address

Với prefix, mạng (network / 네트워크) address có host bits = 0; broadcast truyền thống host bits = 1. Host address nằm giữa, trừ special prefix/use cases.

## 85. Default gateway

Host gửi packet tới destination ngoài cục bộ (local / 로컬) subnet thông qua default gateway/router. DNS không làm nhiệm vụ forwarding packet.

## 86. MAC vs IP

MAC phục vụ local-link delivery; IP phục vụ logical addressing/routing across networks. Router thay đổi link-layer frame hop-by-hop trong khi IP destination có thể giữ end-to-end (trừ NAT và các mechanism khác).

## 87. TCP handshake purpose

Three-way handshake thiết lập liên kết (connection / 연결) trạng thái (state / 상태) và đồng bộ initial chuỗi (sequence / 시퀀스) thông tin (information / 정보). Nó không “mã hóa” liên kết (connection / 연결); TLS làm cryptographic protection ở tầng (layer / 계층) khác.

## 88. luồng (flow / 흐름) điều khiển (control / 제어) vs congestion điều khiển (control / 제어)

Luồng (flow / 흐름) điều khiển (control / 제어) bảo vệ receiver khỏi sender quá nhanh. Congestion điều khiển (control / 제어) phản ứng sức chứa (capacity / 용량)/congestion của mạng (network / 네트워크) đường dẫn (path / 경로).

## 89. DNS recursive vs iterative idea

Recursive resolver có thể thay máy khách (client / 클라이언트) thực hiện chuỗi lookup. Authoritative máy chủ (server / 서버) cung cấp records cho zone nó quản lý.

## 90. NAT

NAT translate address/cổng (port / 포트) giữa domains, thường cho phép nhiều private hosts share công khai (public / 공개) address bằng PAT/NAPT. NAT không phải firewall ngữ nghĩa (semantic / 의미적) hoàn chỉnh dù có thể ảnh hưởng reachability.

---

# Môn 5 — 정보시스템 구축 관리

## 91. dự án (project / 프로젝트) rủi ro (risk / 위험) vs issue

Rủi ro (risk / 위험) là uncertain sự kiện (event / 이벤트)/điều kiện (condition / 조건) có thể ảnh hưởng mục tiêu. Issue là vấn đề đã xảy ra/cần xử lý hiện tại.

Rủi ro (risk / 위험) register có xác suất (probability / 확률)/impact/phản hồi (response / 응답); issue log tracking khác.

## 92. Contingency reserve

Reserve dành cho known/identified risks khác với management reserve cho unknown/overall bất định (uncertainty / 불확실성) theo project-management taxonomy. Nếu đề dùng terminology cụ thể, đọc wording kỹ.

## 93. Forward pass / backward pass

CPM forward pass tính earliest start/finish. Backward pass tính latest start/finish. Slack/float = khoảng delay có thể có mà không ảnh hưởng dự án (project / 프로젝트) finish theo mạng (network / 네트워크) các giả định (assumptions / 가정들).

## 94. đường găng (critical path / 임계 경로) có thể thay đổi

Sau delay, acceleration hoặc phụ thuộc (dependency / 의존성) thay đổi (change / 변경), đường găng (critical path / 임계 경로) có thể đổi. Không coi đường găng (critical path / 임계 경로) là thuộc tính vĩnh viễn của dự án (project / 프로젝트).

## 95. Vertical vs horizontal scaling

Vertical scale-up: tăng tài nguyên (resource / 자원) của một nút (node / 노드). Horizontal scale-out: thêm nodes.

Scale-out cần phân phối (distribution / 분포), tải (load / 로드) balancing, trạng thái (state / 상태)/dữ liệu (data / 데이터) coordination; không miễn phí.

## 96. tải (load / 로드) balancing vs failover

Tải (load / 로드) balancing phân phối traffic/công việc (work / 작업). Failover chuyển dịch vụ (service / 서비스) sang standby/healthy thành phần (component / 컴포넌트) khi thất bại (failure / 실패).

Một bộ cân bằng tải (load balancer / 로드 밸런서) có health checks có thể hỗ trợ failover, nhưng intents khác nhau.

## 97. Active-active vs active-standby

Active-active nhiều instance cùng serve traffic; active-standby có primary active và standby chờ takeover.

Active-active tăng sức chứa (capacity / 용량)/availability nhưng consistency/trạng thái (state / 상태) coordination phức tạp hơn.

## 98. Replication chế độ (mode / 모드)

Synchronous replication giảm RPO vì acknowledge sau khi replica xác nhận theo thiết kế (design / 설계), nhưng tăng độ trễ (latency / 지연 시간)/availability sự đánh đổi (trade-off / 트레이드오프). Asynchronous replication giảm ghi (write / 쓰기) độ trễ (latency / 지연 시간) coupling nhưng có lag/data-loss cửa sổ (window / 윈도우).

## 99. Backup full/incremental/differential

Full: toàn bộ selected dữ liệu (data / 데이터).
Incremental: changes từ backup gần nhất theo scheme.
Differential: changes từ last full.

Restore chuỗi (chain / 사슬) và backup thời gian (time / 시간)/lưu trữ (storage / 저장소) sự đánh đổi (trade-off / 트레이드오프) khác nhau.

## 100. Cold/Warm/Hot site concept

Cold site có facility cơ bản, cần thời gian setup dài. Warm có partial equipment/dữ liệu (data / 데이터) readiness. Hot gần production-ready hơn, RTO thấp hơn nhưng chi phí (cost / 비용) cao.

## 101. RTO/RPO không phải đo lường (measurement / 측정) thực tế

RTO/RPO là **objectives**. Actual khôi phục (recovery / 복구) thời gian (time / 시간)/dữ liệu (data / 데이터) mất mát (loss / 손실) có thể tệ hơn nếu thiết kế (design / 설계)/kiểm thử (test / 테스트) không đáp ứng.

## 102. MTBF vs MTTR

MTBF — mean thời gian (time / 시간) between failures — độ tin cậy (reliability / 신뢰성) interval chỉ số (metric / 지표).
MTTR — mean thời gian (time / 시간) to repair/recover — duration restore chỉ số (metric / 지표).

Availability thường tăng khi MTBF tăng hoặc MTTR giảm.

## 103. IaaS/PaaS/SaaS responsibility

Càng lên SaaS, provider quản nhiều ngăn xếp (stack / 스택) hơn; customer tập trung cấu hình (config / 설정)/dữ liệu (data / 데이터)/use. IaaS customer vẫn quản OS/middleware/app nhiều hơn.

Không chỉ học tên; hỏi “ai chịu responsibility cho tầng (layer / 계층) nào?”.

## 104. ảnh bộ chứa (container image / 컨테이너 이미지) vs running ảnh bộ chứa (container image / 컨테이너 이미지) là immutable-ish packaged template/layers. bộ chứa (container / 컨테이너) là thời gian chạy (runtime / 런타임) instance của ảnh (image / 이미지) với writable trạng thái (state / 상태)/tiến trình (process / 프로세스) không gian tên (namespace / 네임스페이스).

## 105. Orchestration

Bộ chứa (container / 컨테이너) orchestration xử triển khai (deployment / 배포), scheduling, scaling, health, khám phá dịch vụ (service discovery / 서비스 디스커버리)/cấu hình (config / 설정)/secrets tùy nền tảng (platform / 플랫폼). Nó không tự sửa ứng dụng (application / 애플리케이션) lô-gic (logic / 논리) bug.

## 106. Confidentiality vs privacy

Confidentiality là bảo mật (security / 보안) thuộc tính (property / 속성) ngăn disclosure trái phép. Privacy rộng hơn, liên quan collection/use/retention/rights của personal dữ liệu (data / 데이터).

## 107. Threat, vulnerability, exploit, rủi ro (risk / 위험)

Threat có khả năng gây harm. Vulnerability là weakness. Exploit là cách/mã (code / 코드) tận dụng weakness. rủi ro (risk / 위험) kết hợp likelihood/impact/ngữ cảnh (context / 맥락) của harm.

## 108. Symmetric vs asymmetric crypto

Symmetric dùng dùng chung (shared / 공유) secret và hiệu quả cho bulk encryption. Asymmetric dùng công khai (public / 공개)/private key và hỗ trợ key exchange/signature scenarios nhưng computationally costlier.

Hybrid protocols thường kết hợp cả hai.

## 109. Encryption vs hashing vs encoding

Encryption reversible với key. băm (hash / 해시) one-way digest. Encoding chỉ biểu diễn (representation / 표현) transformation, không nhằm confidentiality.

Base64 không phải encryption.

## 110. Salt vs encryption key

Password salt là non-secret random giá trị (value / 값) thêm trước hashing để chống precomputed/rainbow attacks và duplicate băm (hash / 해시) patterns. Nó không cần giữ bí mật như encryption key.

## 111. MAC vs digital signature

Message Authentication mã (code / 코드) dùng dùng chung (shared / 공유) secret để integrity/authenticity giữa parties biết secret; digital signature dùng private/công khai (public / 공개) key và hỗ trợ non-repudiation thuộc tính (property / 속성) theo trust mô hình (model / 모델).

## 112. RBAC vs ACL

ACL gắn permissions theo tài nguyên (resource / 자원) và identities/groups. RBAC gán permissions cho roles rồi users nhận roles.

Hai mô hình (model / 모델) có thể coexist.

## 113. Least privilege vs separation of duties

Least privilege giảm quyền mỗi principal xuống mức cần thiết. Separation of Duties chia trọng yếu (critical / 중요) tiến trình (process / 프로세스) qua nhiều roles để một cá nhân không tự hoàn tất toàn bộ sensitive luồng (flow / 흐름).

## 114. Firewall stateful vs stateless

Stateless filter xét packet quy tắc (rule / 규칙) riêng lẻ. Stateful firewall theo dõi liên kết (connection / 연결)/session trạng thái (state / 상태) để quyết định traffic liên quan.

## 115. WAF phạm vi (scope / 범위)

WAF tập trung HTTP/application-layer patterns. Nó không thay mạng (network / 네트워크) firewall, secure coding hay DB permissions.

## 116. SIEM concept

SIEM tập trung/chuẩn hóa/correlate bảo mật (security / 보안) logs/events để detection/investigation. Nó không phải IDS sensor duy nhất và không tự khối (block / 블록) mọi attack.

## 117. Vulnerability scan vs penetration kiểm thử (test / 테스트)

Vulnerability scan tìm known weaknesses/cấu hình (config / 설정) signatures tự động hơn. Penetration kiểm thử (test / 테스트) cố exploit/chaining trong phạm vi (scope / 범위) để chứng minh impact.

## 118. Patch management

Không chỉ “cài patch”. Bao gồm inventory, assess severity/exposure, kiểm thử (test / 테스트) tính tương thích (compatibility / 호환성), deploy, verify và quay lui (rollback / 롤백) plan.

## 119. sự cố (incident / 인시던트) phản hồi (response / 응답) vòng đời (lifecycle / 생명주기)

Một luồng (flow / 흐름) khái quát:

```text
Preparation → Detection/Analysis → Containment → Eradication → Recovery → Lessons Learned
```

Wording có thể thay đổi tùy khung phần mềm (framework / 프레임워크) nhưng intent giữ: phát hiện, hạn chế harm, loại nguyên nhân, phục hồi, cải tiến.

## 120. Backup restore kiểm thử (test / 테스트)

Có backup tệp (file / 파일) không chứng minh restore được. Restore drill kiểm tính toàn vẹn, procedure, phụ thuộc (dependency / 의존성), credential/key và RTO thực tế.

---

# Closed-book edge-case check

Không nhìn tài liệu, trả lời ngắn 30 câu sau:

1. Ambiguity khác inconsistency thế nào?
2. DFD balancing bảo toàn điều gì?
3. Realization khác generalization ở đâu?
4. Include khác extend ở Use trường hợp (case / 사례) thế nào?
5. Sequential cohesion khác communicational cohesion thế nào?
6. bên ngoài (external / 외부) coupling khác dùng chung (common / 공통) coupling thế nào?
7. vùng nhớ động (heap / 힙) khác BST ở thứ tự (ordering / 순서) bất biến (invariant / 불변식) nào?
8. MST khác shortest đường dẫn (path / 경로) ở mục tiêu (objective / 목표) nào?
9. Stable sort bảo toàn thuộc tính (property / 속성) nào?
10. Collision khác duplicate key thế nào?
11. Static testing khác động (dynamic / 동적) testing thế nào?
12. Statement coverage 100% vì sao chưa đủ branch coverage?
13. Candidate key và surrogate key khác vai trò nào?
14. Prime attribute là gì?
15. Lossless decomposition bảo vệ điều gì?
16. phụ thuộc (dependency / 의존성) preservation có thể sự đánh đổi (trade-off / 트레이드오프) với BCNF thế nào?
17. `IS NULL` khác `= NULL` thế nào?
18. Serializability khác recoverability ở đâu?
19. TLB miss khác page fault thế nào?
20. phản hồi (response / 응답) thời gian (time / 시간) khác waiting thời gian (time / 시간) thế nào?
21. Starvation khác deadlock thế nào?
22. luồng (flow / 흐름) điều khiển (control / 제어) khác congestion điều khiển (control / 제어) thế nào?
23. NAT khác firewall ở intent nào?
24. rủi ro (risk / 위험) khác issue thế nào?
25. tải (load / 로드) balancing khác failover thế nào?
26. RTO/RPO là mục tiêu (objective / 목표) hay đo lường (measurement / 측정)?
27. Encryption/băm (hash / 해시)/encoding khác nhau ra sao?
28. Least privilege khác separation of duties thế nào?
29. Vulnerability scan khác penetration kiểm thử (test / 테스트) thế nào?
30. Vì sao backup phải được restore-test?

Nếu dưới 24/30 câu trả lời rõ ràng, chưa coi phần edge-case coverage là ổn.
