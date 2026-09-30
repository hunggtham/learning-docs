# 정보처리기사 필기 2026 — Active Recall Bank 250

> 250 câu **không có lựa chọn A/B/C/D**, chia đều 50 câu/môn. Đây là lớp kiểm tra breadth sau khi đã đọc deep-dive. Mỗi câu phải trả lời bằng lời của mình trước khi xem `Answer Cues` ở cuối từng môn.
>
> Quy tắc: nếu chỉ nhận ra đáp án sau khi nhìn cue, tính là **sai**. Nếu trả lời đúng từ khóa (keyword / 키워드) nhưng không giải thích được cơ chế (mechanism / 메커니즘)/ranh giới, tính **0.5 điểm**.

---

# Môn 1 — 소프트웨어 설계 — 50 recall prompts

1. Functional yêu cầu (requirement / 요구사항) khác Non-functional yêu cầu (requirement / 요구사항) ở câu hỏi cốt lõi nào?
2. xác minh (verification / 확인) khác kiểm tra hợp lệ (validation / 검증) thế nào?
3. Ambiguity khác Inconsistency thế nào?
4. yêu cầu (requirement / 요구사항) Traceability phục vụ hai mục đích chính nào?
5. Feasibility khác Priority thế nào?
6. luồng (flow / 흐름) chính của requirements development gồm bốn bước nào?
7. DFD tập trung vào cái gì?
8. DFD balancing nghĩa là gì?
9. dữ liệu (data / 데이터) Dictionary khác Mini-specification thế nào?
10. quyết định (decision / 결정) bảng (table / 테이블) hữu ích nhất khi nào?
11. Use trường hợp (case / 사례) Diagram trả lời câu hỏi gì?
12. chuỗi (sequence / 시퀀스) Diagram trả lời câu hỏi gì?
13. Activity Diagram khác máy trạng thái (state machine / 상태 머신) Diagram thế nào?
14. thành phần (component / 컴포넌트) Diagram khác triển khai (deployment / 배포) Diagram thế nào?
15. Association, Aggregation và Composition khác nhau thế nào?
16. Generalization khác Realization thế nào?
17. `<<include>>` khác `<<extend>>` thế nào?
18. Wireframe khác Mockup thế nào?
19. Prototype khác Storyboard thế nào?
20. Intuitiveness và Learnability khác nhau ở đâu?
21. High cohesion / low coupling có ý nghĩa gì?
22. Functional Cohesion là gì?
23. Sequential Cohesion là gì?
24. Communicational Cohesion là gì?
25. Content Coupling là gì?
26. dùng chung (common / 공통) Coupling là gì?
27. bên ngoài (external / 외부) Coupling là gì?
28. điều khiển (control / 제어) Coupling là gì?
29. Stamp Coupling khác dữ liệu (data / 데이터) Coupling thế nào?
30. Fan-in và Fan-out là gì?
31. Encapsulation khác lớp trừu tượng (abstraction / 추상화) thế nào?
32. Inheritance khác Polymorphism thế nào?
33. SRP phát hiện thiết kế (design / 설계) smell nào?
34. OCP nhắm mục tiêu gì?
35. LSP hỏi điều gì về subtype?
36. ISP giải quyết vấn đề gì?
37. DIP thay đổi hướng phụ thuộc (dependency / 의존성) thế nào?
38. Factory phương thức (method / 메서드) khác Abstract Factory thế nào?
39. Builder khác Prototype thế nào?
40. Adapter khác Facade thế nào?
41. Decorator khác Proxy thế nào?
42. chiến lược (strategy / 전략) khác trạng thái (state / 상태) thế nào?
43. Observer dùng cho relationship nào?
44. Command mẫu (pattern / 패턴) đóng gói cái gì?
45. Template phương thức (method / 메서드) giữ cố định phần nào và mở rộng phần nào?
46. giao diện (interface / 인터페이스) đặc tả hợp đồng (contract / 계약) ngoài trường dữ liệu (field / 필드)/dữ liệu (data / 데이터) còn cần gì?
47. thử lại (retry / 재시도) có thể gây duplicate side tác động (effect / 효과) thế nào?
48. Idempotency giải quyết vấn đề gì?
49. Point-to-point tích hợp (integration / 통합) quy mô (scale / 규모) kém ở đâu?
50. Breaking API thay đổi (change / 변경) có thể xảy ra dù trường dữ liệu (field / 필드) name không đổi bằng cách nào?

## Answer Cues — Môn 1

1. **What vs chất lượng (quality / 품질)/ràng buộc (constraint / 제약조건):** năng lực (capability / 역량) nghiệp vụ vs chất lượng/ràng buộc.
2. **bản dựng (build / 빌드) sản phẩm (product / 제품) right vs bản dựng (build / 빌드) right sản phẩm (product / 제품).**
3. Nhiều cách hiểu vs hai yêu cầu (requirement / 요구사항) mâu thuẫn.
4. Impact phân tích (analysis / 분석) + coverage/source-to-test tracing.
5. Có làm được trong các ràng buộc (constraints / 제약조건들) không vs nên làm trước/giá trị tương đối.
6. Elicitation → phân tích (analysis / 분석) → Specification → kiểm tra hợp lệ (validation / 검증).
7. luồng dữ liệu (data flow / 데이터 흐름)/transformation giữa thực thể (entity / 엔터티), tiến trình (process / 프로세스), store.
8. Parent tiến trình (process / 프로세스) bên ngoài (external / 외부) I/O phải được bảo toàn khi decomposition.
9. Định nghĩa dữ liệu (data / 데이터) vs định nghĩa processing lô-gic (logic / 논리).
10. Nhiều combinations điều kiện (condition / 조건)/hành động (action / 동작) cần systematic coverage.
11. Actors và hệ thống (system / 시스템) functions/goals.
12. Message thứ tự (order / 순서) giữa participants theo thời gian.
13. Workflow/actions vs vòng đời (lifecycle / 생명주기) trạng thái (state / 상태) của đối tượng (object / 객체).
14. Software components/dependencies vs triển khai (deployment / 배포) nodes/artifacts.
15. General quan hệ (relation / 관계); weak whole-part; strong vòng đời (lifecycle / 생명주기) quyền sở hữu (ownership / 소유권).
16. Is-a hierarchy vs hiện thực (implementation / 구현) of giao diện (interface / 인터페이스)/specification.
17. Required reused hành vi (behavior / 동작) vs optional/conditional extension.
18. Skeleton/bố cục (layout / 레이아웃) vs visual appearance gần thành phẩm.
19. Interactive mẫu (sample / 표본) vs scenario chuỗi (sequence / 시퀀스)/story luồng (flow / 흐름).
20. Dễ hiểu ngay vs dễ học qua thời gian.
21. Nội bộ cùng mục tiêu, phụ thuộc (dependency / 의존성) ngoài thấp.
22. Mọi elements cùng phục vụ một chức năng rõ.
23. đầu ra (output / 출력) step trước thành đầu vào (input / 입력) step sau.
24. Operations cùng dùng/chỉnh same dữ liệu (data / 데이터) set.
25. mô-đun (module / 모듈) chạm trực tiếp internals của mô-đun (module / 모듈) khác.
26. Share toàn cục (global / 전역)/dùng chung (common / 공통) dữ liệu (data / 데이터).
27. Cùng phụ thuộc bên ngoài (external / 외부) format/giao thức (protocol / 프로토콜)/thiết bị (device / 장치).
28. Truyền flag/điều khiển (control / 제어) thông tin (information / 정보) điều khiển lô-gic (logic / 논리) bên nhận.
29. Truyền cấu trúc (structure / 구조) dư thừa vs chỉ dữ liệu (data / 데이터) cần thiết.
30. Số callers vào / số dependencies gọi ra.
31. Hide/điều khiển (control / 제어) trạng thái (state / 상태) biểu diễn (representation / 표현) vs giữ essence, bỏ detail.
32. kiểu (type / 타입) hierarchy/reuse vs same giao diện (interface / 인터페이스), different hành vi thời gian chạy (runtime behavior / 런타임 동작).
33. lớp (class / 클래스) có nhiều reasons to thay đổi (change / 변경)/responsibilities.
34. Mở rộng hành vi (behavior / 동작) mà hạn chế sửa stable mã (code / 코드).
35. Subtype thay cơ sở (base / 기반) mà không phá đặc tả hợp đồng (contract / 계약).
36. Fat giao diện (interface / 인터페이스) ép máy khách (client / 클라이언트) phụ thuộc methods không dùng.
37. High-level và low-level cùng phụ thuộc lớp trừu tượng (abstraction / 추상화).
38. Delegated creation phương thức (method / 메서드) vs factory tạo family related objects.
39. Step-by-step construction vs clone existing đối tượng (object / 객체).
40. Convert incompatible giao diện (interface / 인터페이스) vs simplify complex subsystem.
41. Add hành vi (behavior / 동작) by wrapper vs stand-in/điều khiển (control / 제어) truy cập (access / 접근).
42. Select thuật toán (algorithm / 알고리즘)/chính sách (policy / 정책) vs hành vi (behavior / 동작) driven by trạng thái nội bộ (internal state / 내부 상태).
43. One-to-many notification.
44. yêu cầu (request / 요청)/hành động (action / 동작) thành đối tượng (object / 객체).
45. Skeleton cố định, steps override/extend.
46. giao thức (protocol / 프로토콜), chuỗi (sequence / 시퀀스), lỗi (error / 오류), hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), auth/bảo mật (security / 보안), tính tương thích (compatibility / 호환성).
47. máy khách (client / 클라이언트) không biết kết quả (outcome / 결과) sau hết thời gian chờ (timeout / 타임아웃) rồi gửi lại same thao tác (operation / 연산).
48. Repeated same logical yêu cầu (request / 요청) không nhân side tác động (effect / 효과).
49. liên kết (connection / 연결)/phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) tăng nhanh khi số các hệ thống (systems / 시스템들) tăng.
50. thay đổi (change / 변경) kiểu (type / 타입), nullability, enum ngữ nghĩa (semantics / 의미론), meaning, các ràng buộc (constraints / 제약조건들).

---

# Môn 2 — 소프트웨어 개발 — 50 recall prompts

51. ADT khác hiện thực (implementation / 구현) thế nào?
52. ngăn xếp (stack / 스택) và hàng đợi (queue / 큐) khác nhau ở truy cập (access / 접근) thứ tự (order / 순서) nào?
53. BST bất biến (invariant / 불변식) cơ bản là gì?
54. vùng nhớ động (heap / 힙) bất biến (invariant / 불변식) cơ bản là gì?
55. Complete nhị phân (binary / 이진) cây (tree / 트리) có hình dạng thế nào?
56. BFS dùng cấu trúc dữ liệu (data structure / 자료구조) nào?
57. DFS thường dùng cấu trúc dữ liệu (data structure / 자료구조)/cơ chế nào?
58. Vì sao BFS cho shortest đường dẫn (path / 경로) theo số cạnh trong unweighted đồ thị (graph / 그래프)?
59. MST khác shortest đường dẫn (path / 경로) thế nào?
60. Adjacency ma trận (matrix / 행렬) và danh sách (list / 목록) sự đánh đổi (trade-off / 트레이드오프) gì?
61. tìm kiếm nhị phân (binary search / 이진 탐색) cần precondition nào?
62. Quick Sort worst-case điển hình là gì?
63. Merge Sort worst-case điển hình là gì?
64. Stable sort nghĩa là gì?
65. In-place nghĩa là gì?
66. băm (hash / 해시) collision là gì?
67. tuyến tính (linear / 선형) Probing gây clustering nào?
68. Vì sao open-address deletion cần tombstone/rehash lô-gic (logic / 논리)?
69. Static Testing khác động (dynamic / 동적) Testing thế nào?
70. lỗi (error / 오류) → Defect → thất bại (failure / 실패) liên hệ thế nào?
71. kiểm thử (test / 테스트) điều kiện (condition / 조건) khác trường hợp kiểm thử (test case / 테스트 케이스) thế nào?
72. Equivalence Partitioning làm gì?
73. ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석) làm gì?
74. Statement Coverage đo gì?
75. Branch Coverage đo gì?
76. Vì sao 100% statement chưa bảo đảm 100% branch?
77. điều kiện (condition / 조건) Coverage khác Branch Coverage thế nào?
78. Cyclomatic độ phức tạp (complexity / 복잡도) có thể tính bằng công thức nào?
79. Top-down tích hợp (integration / 통합) dùng Stub vì sao?
80. Bottom-up tích hợp (integration / 통합) dùng Driver vì sao?
81. đơn vị (unit / 단위), tích hợp (integration / 통합), hệ thống (system / 시스템), Acceptance khác phạm vi (scope / 범위) thế nào?
82. Alpha và Beta khác môi trường/người dùng thế nào?
83. Retest khác Regression thế nào?
84. Smoke kiểm thử (test / 테스트) có intent gì?
85. hiệu năng (performance / 성능) thông lượng (throughput / 처리량) khác phản hồi (response / 응답) thời gian (time / 시간) thế nào?
86. kiểm thử tải (load test / 부하 테스트) khác kiểm thử sức chịu tải (stress test / 스트레스 테스트) thế nào?
87. cấu hình (configuration / 구성) Item có thể gồm những gì ngoài nguồn (source / 소스)?
88. Baseline là gì?
89. phiên bản (version / 버전) điều khiển (control / 제어) khác cấu hình (configuration / 구성) Management thế nào?
90. bản dựng (build / 빌드) khác bản phát hành (release / 릴리스) thế nào?
91. Packaging gồm những gì ngoài nhị phân (binary / 이진)?
92. Checksum kiểm thuộc tính (property / 속성) gì?
93. DRM giải quyết vấn đề gì?
94. giao diện (interface / 인터페이스) kiểm tra hợp lệ (validation / 검증) khác nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증) thế nào?
95. Serialization lỗi (error / 오류) khác ngữ nghĩa (semantic / 의미적) kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) thế nào?
96. Retryable lỗi (error / 오류) thường có đặc điểm gì?
97. giao diện (interface / 인터페이스) khả năng quan sát (observability / 관측 가능성) nên theo dõi những chỉ số (metric / 지표) nào?
98. Deduplication khác Idempotency thế nào?
99. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) kiểm cái gì?
100. Regression suite tốt cần tránh overfit vào hiện thực (implementation / 구현) detail thế nào?

## Answer Cues — Môn 2

51. hành vi (behavior / 동작)/giao diện (interface / 인터페이스) lớp trừu tượng (abstraction / 추상화) vs array/danh sách (list / 목록)/cây (tree / 트리) concrete realization.
52. LIFO vs FIFO.
53. Left keys < nút (node / 노드) < right keys theo comparison bất biến (invariant / 불변식) phù hợp.
54. Parent ordered relative to children, không full BST thứ tự (order / 순서).
55. Fill mức (level / 수준) by mức (level / 수준), last mức (level / 수준) left-to-right.
56. hàng đợi (queue / 큐).
57. ngăn xếp (stack / 스택)/recursion.
58. Explore vertices theo distance layers.
59. Connect all vertices min total weight vs min đường dẫn (path / 경로) from nguồn (source / 소스).
60. O(V²) fast edge lookup vs O(V+E) sparse-friendly.
61. tìm kiếm (search / 검색) phạm vi (range / 범위) ordered/sorted theo comparator.
62. O(n²).
63. O(n log n).
64. Giữ relative thứ tự (order / 순서) của equal-key records.
65. Auxiliary bộ nhớ (memory / 메모리) nhỏ, mutate cấu trúc (structure / 구조) chính.
66. Different keys same băm (hash / 해시)/bucket.
67. Primary clustering.
68. Xóa “never used” có thể làm tìm kiếm (search / 검색) dừng sớm, phá probe chuỗi (chain / 사슬).
69. Không execute vs execute program.
70. Human mistake tạo fault; fault activated có thể gây observable thất bại (failure / 실패).
71. Aspect cần kiểm thử (test / 테스트) vs concrete inputs/steps/expected kết quả (result / 결과).
72. Chia đầu vào (input / 입력) thành classes hành vi (behavior / 동작) tương đương.
73. kiểm thử (test / 테스트) edges ngay quanh boundaries.
74. Executed statements.
75. quyết định (decision / 결정) outcomes/branches.
76. Có thể execute true branch statements mà chưa kiểm thử (test / 테스트) false kết quả (outcome / 결과).
77. Atomic conditions true/false vs overall quyết định (decision / 결정) outcomes.
78. `E - N + 2P` hoặc decisions + 1 trong simple connected luồng (flow / 흐름).
79. Mô phỏng callees phía dưới chưa có.
80. Mô phỏng callers phía trên chưa có.
81. thành phần (component / 컴포넌트) nhỏ → interactions → full hệ thống (system / 시스템) → người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스) acceptance.
82. nội bộ (internal / 내부) controlled users/môi trường (environment / 환경) vs bên ngoài (external / 외부) representative users.
83. Xác nhận bug fix vs kiểm không phá hành vi (behavior / 동작) khác.
84. bản dựng (build / 빌드) có đủ ổn để kiểm thử (test / 테스트) sâu tiếp không.
85. công việc (work / 작업)/thời gian (time / 시간) vs elapsed per yêu cầu (request / 요청)/thao tác (operation / 연산).
86. Expected/high tải công việc (workload / 워크로드) vs vượt limits để tìm breaking hành vi (behavior / 동작).
87. Requirements, cấu hình (config / 설정), lược đồ (schema / 스키마), scripts, tests, binaries, manuals.
88. Controlled established cấu hình (configuration / 구성)/phiên bản (version / 버전) trạng thái (state / 상태).
89. lịch sử (history / 이력)/branch/phiên bản (version / 버전) tooling vs broader identification/thay đổi (change / 변경)/status/kiểm tra (audit / 감사)/quy trình phát hành (release process / 릴리스 프로세스).
90. Compile/gói (package / 패키지) sản phẩm tạo ra (artifact / 산출물) vs đưa selected phiên bản (version / 버전) tới môi trường (environment / 환경)/users.
91. Dependencies, cấu hình (config / 설정), siêu dữ liệu (metadata / 메타데이터), install docs, license/manual.
92. Integrity/thay đổi (change / 변경)/corruption.
93. Rights/license/usage điều khiển (control / 제어) của digital content.
94. Shape/kiểu (type / 타입)/required fields vs lĩnh vực (domain / 도메인)/nghiệp vụ (business / 비즈니스) rules.
95. Không parse/encode được vs dữ liệu (data / 데이터) parse được nhưng không hợp đặc tả hợp đồng (contract / 계약)/nghiệp vụ (business / 비즈니스).
96. Transient hạ tầng (infrastructure / 인프라)/mạng (network / 네트워크)/máy chủ (server / 서버) điều kiện (condition / 조건), thao tác (operation / 연산) safe to thử lại (retry / 재시도).
97. độ trễ (latency / 지연 시간), lỗi (error / 오류), thông lượng (throughput / 처리량), thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃), backlog, đặc tả hợp đồng (contract / 계약) thất bại (failure / 실패).
98. Technique remove duplicates vs ngữ nghĩa (semantic / 의미적) repeated thao tác (operation / 연산) same tác động (effect / 효과).
99. Provider/bên tiêu thụ (consumer / 소비자) giao diện (interface / 인터페이스) các giả định (assumptions / 가정들) và tính tương thích (compatibility / 호환성).
100. Assert externally meaningful hành vi (behavior / 동작), không khóa kiểm thử (test / 테스트) vào private hiện thực (implementation / 구현) vô ích.

---

# Môn 3 — 데이터베이스 구축 — 50 recall prompts

101. quan hệ (relation / 관계), Tuple, Attribute, lĩnh vực (domain / 도메인) là gì?
102. Degree khác Cardinality thế nào?
103. Super Key khác Candidate Key thế nào?
104. Primary Key khác Alternate Key thế nào?
105. Foreign Key bảo vệ integrity nào?
106. Natural Key khác Surrogate Key thế nào?
107. Selection khác Projection thế nào?
108. phép nối (join / 조인) dùng để làm gì?
109. Division thao tác (operation / 연산) biểu diễn loại truy vấn (query / 쿼리) lô-gic (logic / 논리) nào?
110. Functional phụ thuộc (dependency / 의존성) `X → Y` nghĩa là gì?
111. Trivial FD là gì?
112. Attribute Closure dùng để làm gì?
113. Prime Attribute là gì?
114. Partial phụ thuộc (dependency / 의존성) là gì?
115. Transitive phụ thuộc (dependency / 의존성) là gì?
116. 1NF nhắm tới vấn đề gì?
117. 2NF loại vấn đề gì?
118. 3NF formal điều kiện (condition / 조건) khái quát là gì?
119. BCNF điều kiện (condition / 조건) là gì?
120. Lossless decomposition là gì?
121. phụ thuộc (dependency / 의존성) preservation là gì?
122. Logical thiết kế (design / 설계) khác vật lý (physical / 물리적) thiết kế (design / 설계) thế nào?
123. B+cây (tree / 트리) chỉ mục (index / 인덱스) phù hợp phạm vi (range / 범위) vì sao?
124. băm (hash / 해시) chỉ mục (index / 인덱스) tự nhiên phù hợp truy vấn (query / 쿼리) nào?
125. Selectivity là gì?
126. Covering chỉ mục (index / 인덱스) là gì?
127. Composite chỉ mục (index / 인덱스) thứ tự (order / 순서) quan trọng vì sao?
128. chỉ mục (index / 인덱스) nhiều gây ghi (write / 쓰기) chi phí (cost / 비용) thế nào?
129. View là gì?
130. Vì sao aggregate view có thể không updatable đơn giản?
131. DDL, DML, DCL, TCL cho mỗi nhóm một ví dụ.
132. WHERE khác HAVING thế nào?
133. INNER phép nối (join / 조인) khác LEFT phép nối (join / 조인) thế nào?
134. `COUNT(*)` khác `COUNT(col)` thế nào?
135. NULL dùng lô-gic (logic / 논리) mấy giá trị?
136. Vì sao `col = NULL` sai lô-gic (logic / 논리)?
137. UNION khác UNION ALL thế nào?
138. Correlated Subquery là gì?
139. ACID gồm bốn thuộc tính (property / 속성) nào?
140. Atomicity khác Consistency thế nào?
141. Isolation bảo vệ cái gì?
142. Durability bảo vệ cái gì?
143. Dirty Read là gì?
144. Non-repeatable Read là gì?
145. Phantom Read là gì?
146. xung đột (conflict / 충돌) Serializability kiểm bằng cách nào?
147. Two-Phase Locking có hai phase gì?
148. Deadlock Wait-for đồ thị (graph / 그래프) biểu diễn edge gì?
149. WAL và Checkpoint khác vai trò thế nào?
150. di chuyển (migration / 마이그레이션) Reconciliation nên kiểm những gì ngoài row count?

## Answer Cues — Môn 3

101. Table-like quan hệ (relation / 관계), row tuple, column attribute, allowed values lĩnh vực (domain / 도메인).
102. Số columns vs số rows.
103. Unique determinant vs minimal unique determinant.
104. Candidate key được chọn làm chính vs candidate keys còn lại.
105. Referential integrity.
106. Business-meaning identifier vs generated/artificial identifier.
107. Rows vs columns.
108. Combine related tuples theo điều kiện (condition / 조건).
109. “Entities liên hệ với tất cả members của một set” kiểu all-for-all.
110. Cùng X giá trị (value / 값) quyết định duy nhất Y giá trị (value / 값).
111. Y subset của X.
112. Tìm attributes suy ra từ set, kiểm thử (test / 테스트) super/candidate key.
113. Thuộc ít nhất một candidate key.
114. Non-prime depends on proper subset of composite candidate key.
115. Key → non-key → non-key.
116. Atomic attribute/lĩnh vực (domain / 도메인) biểu diễn (representation / 표현), loại repeating group theo relational form.
117. Partial phụ thuộc (dependency / 의존성).
118. Với non-trivial X→A, X superkey hoặc A prime.
119. Mọi determinant non-trivial phải superkey.
120. phép nối (join / 조인) relations con khôi phục đúng original không spurious tuples.
121. Enforce dependencies trên relations con không cần phép nối (join / 조인).
122. Relational cấu trúc (structure / 구조)/các ràng buộc (constraints / 제약조건들) vs lưu trữ (storage / 저장소)/chỉ mục (index / 인덱스)/partition/truy cập (access / 접근) đường dẫn (path / 경로).
123. Ordered keys + cây (tree / 트리) phạm vi (range / 범위) traversal.
124. Equality lookup.
125. Fraction/discrimination của predicate/chỉ mục (index / 인덱스) key; ít matches thường selective hơn.
126. chỉ mục (index / 인덱스) chứa đủ dữ liệu (data / 데이터) trả truy vấn (query / 쿼리) không cần bảng (table / 테이블) lookup thêm.
127. Leftmost/prefix thứ tự (ordering / 순서) quyết định usable tìm kiếm (search / 검색) ranges tùy DBMS.
128. Mỗi ghi (write / 쓰기) phải maintain indexes, thêm I/O/lưu trữ (storage / 저장소)/contention.
129. Virtual/query-defined quan hệ (relation / 관계).
130. One view row có thể không map uniquely về underlying row changes.
131. CREATE; SELECT/INSERT/cập nhật (update / 업데이트); GRANT; lần ghi nhận (commit / 커밋)/quay lui (rollback / 롤백).
132. Filter rows before grouping vs filter groups after aggregate.
133. Matching rows only vs preserve all left rows.
134. All rows vs non-NULL values của column.
135. TRUE/FALSE/UNKNOWN.
136. NULL không phải ordinary giá trị (value / 값); dùng IS NULL.
137. Deduplicate vs preserve duplicates.
138. Inner truy vấn (query / 쿼리) references hiện tại (current / 현재) outer row.
139. Atomicity, Consistency, Isolation, Durability.
140. All-or-nothing vs valid-state bất biến (invariant / 불변식) chuyển tiếp (transition / 전이).
141. Concurrent interference/anomalies.
142. Committed dữ liệu (data / 데이터) survives crash theo persistence/khôi phục (recovery / 복구) guarantees.
143. Read uncommitted dữ liệu (data / 데이터).
144. Same row read twice changes after another committed cập nhật (update / 업데이트).
145. Same predicate returns added/removed rows.
146. bản dựng (build / 빌드) precedence đồ thị (graph / 그래프); acyclic = conflict-serializable.
147. Growing acquire, Shrinking bản phát hành (release / 릴리스).
148. Ti waits for tài nguyên (resource / 자원) held by Tj.
149. Logging-before-data khôi phục (recovery / 복구) quy tắc (rule / 규칙) vs khôi phục (recovery / 복구) progress điểm (point / 지점)/reduce scan.
150. Key uniqueness, RI, aggregates, checksums, encoding, precision, nghiệp vụ (business / 비즈니스) invariants.

---

# Môn 4 — 프로그래밍 언어 활용 — 50 recall prompts

151. trình biên dịch (compiler / 컴파일러), trình thông dịch (interpreter / 인터프리터) và JIT khác nhau ở đâu?
152. khung phần mềm (framework / 프레임워크) khác thư viện (library / 라이브러리) ở flow-control quyền sở hữu (ownership / 소유권) thế nào?
153. phạm vi (scope / 범위) khác thời gian tồn tại (lifetime / 수명) thế nào?
154. giá trị (value / 값) ngữ nghĩa (semantics / 의미론) khác tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) thế nào?
155. Java pass-by-value với đối tượng (object / 객체) tham chiếu (reference / 참조) nghĩa là gì?
156. Trong C, `&x`, `p`, `*p` lần lượt là gì?
157. Pointer arithmetic `p+1` phụ thuộc gì?
158. Array decay thành pointer trong ngữ cảnh (context / 맥락) nào và ngoại lệ ý tưởng nào cần nhớ?
159. C string kết thúc bằng gì?
160. `strlen` có tính null terminator không?
161. Struct khác Union thế nào?
162. Pre-increment khác Post-increment thế nào?
163. Recursion cần hai thành phần lô-gic (logic / 논리) nào?
164. Java Overloading khác Overriding thế nào?
165. thời gian chạy (runtime / 런타임) polymorphism chọn overridden instance phương thức (method / 메서드) theo gì?
166. Abstract lớp (class / 클래스) khác giao diện (interface / 인터페이스) khái quát thế nào?
167. Checked Exception khác Unchecked Exception thế nào?
168. Java String khác StringBuilder về mutability thế nào?
169. `==` đối tượng (object / 객체) tham chiếu (reference / 참조) khác `.equals()` thế nào?
170. Python name binding nghĩa là gì?
171. Mutable vs Immutable cho ví dụ mỗi loại.
172. Shallow bản sao (copy / 복사) khác Deep bản sao (copy / 복사) thế nào?
173. Python slicing stop chỉ mục (index / 인덱스) có inclusive không?
174. Mutable Default Argument có bẫy gì?
175. tiến trình (process / 프로세스) khác luồng thực thi (thread / 스레드) thế nào?
176. Ready khác Blocked trạng thái (state / 상태) thế nào?
177. FCFS có vấn đề Convoy tác động (effect / 효과) là gì?
178. SJF ưu điểm và rủi ro (risk / 위험) nào?
179. SRTF khác SJF thế nào?
180. Round Robin phụ thuộc parameter gì?
181. thời gian (time / 시간) quantum quá nhỏ gây gì?
182. Priority Scheduling có rủi ro (risk / 위험) nào và Aging giúp thế nào?
183. Turnaround, Waiting, phản hồi (response / 응답) thời gian (time / 시간) formulas là gì?
184. Race điều kiện (condition / 조건) là gì?
185. trọng yếu (critical / 중요) Section là gì?
186. Mutex khác Semaphore thế nào?
187. Bốn Coffman conditions là gì?
188. Deadlock Prevention khác Avoidance khác Detection thế nào?
189. Paging khác Segmentation thế nào?
190. nội bộ (internal / 내부) khác bên ngoài (external / 외부) Fragmentation thế nào?
191. Page Fault là gì?
192. FIFO, LRU, Optimal chọn victim theo gì?
193. Belady’s Anomaly gắn với chính sách (policy / 정책) nào?
194. TLB miss khác Page Fault thế nào?
195. Thrashing là gì?
196. TCP khác UDP thế nào?
197. OSI mạng (network / 네트워크) tầng (layer / 계층) làm gì?
198. `/27` có bao nhiêu total/usable IPv4 addresses theo cách tính truyền thống?
199. Longest Prefix Match là gì?
200. luồng (flow / 흐름) điều khiển (control / 제어) khác Congestion điều khiển (control / 제어) thế nào?

## Answer Cues — Môn 4

151. Ahead-of-time translation, thời gian chạy (runtime / 런타임) interpretation, thời gian chạy (runtime / 런타임) hot-code compilation.
152. App calls thư viện (library / 라이브러리); khung phần mềm (framework / 프레임워크) owns skeleton và calls app hooks.
153. Lexical/truy cập (access / 접근) visibility vs thời gian chạy (runtime / 런타임) existence.
154. bản sao (copy / 복사) dữ liệu (data / 데이터) vs bản sao (copy / 복사) tham chiếu (reference / 참조) tới dùng chung (shared / 공유) đối tượng (object / 객체).
155. bản sao (copy / 복사) của tham chiếu (reference / 참조) giá trị (value / 값) được truyền; vẫn có thể mutate same đối tượng (object / 객체).
156. Address of x; stored address; giá trị (value / 값) at address.
157. Pointed element kiểu (type / 타입)/kích thước (size / 크기) ngữ nghĩa (semantics / 의미론).
158. Many expressions decay; `sizeof` on actual array và `&array` là key exceptions/concepts.
159. `\0`.
160. Không.
161. Separate lưu trữ (storage / 저장소) vs dùng chung (shared / 공유) lưu trữ (storage / 저장소).
162. Increment before expression giá trị (value / 값) vs giá trị (value / 값) old rồi increment side tác động (effect / 효과).
163. cơ sở (base / 기반) trường hợp (case / 사례) + recursive step tiến tới cơ sở (base / 기반).
164. Same name/different parameters compile-time vs subclass replacement thời gian chạy (runtime / 런타임).
165. Actual thời gian chạy (runtime / 런타임) đối tượng (object / 객체).
166. lớp (class / 클래스) lớp trừu tượng (abstraction / 추상화) có trạng thái (state / 상태)/constructor/concrete methods vs đặc tả hợp đồng (contract / 계약)/multiple hiện thực (implementation / 구현) mô hình (model / 모델).
167. Catch/declare compile-time quy tắc (rule / 규칙) vs RuntimeException hierarchy unchecked.
168. Immutable vs mutable builder.
169. định danh (identity / 식별자) vs logical equality đặc tả hợp đồng (contract / 계약).
170. Names bind to objects; assignment không bản sao (copy / 복사) đối tượng (object / 객체) mặc định.
171. danh sách (list / 목록)/dict mutable; int/str/tuple cấu trúc (structure / 구조) immutable.
172. Outer bản sao (copy / 복사) only vs recursive đồ thị (graph / 그래프) bản sao (copy / 복사).
173. Exclusive.
174. Default đối tượng (object / 객체) created once at definition, dùng chung (shared / 공유) across calls.
175. Separate address/tài nguyên (resource / 자원) ngữ cảnh (context / 맥락) vs thực thi (execution / 실행) units sharing tiến trình (process / 프로세스) resources.
176. Ready waits CPU; Blocked waits sự kiện (event / 이벤트)/I/O.
177. Short jobs stuck behind long job.
178. Low average waiting if burst known; starvation/unknown burst issue.
179. Preemptive shortest remaining thời gian (time / 시간).
180. thời gian (time / 시간) quantum.
181. ngữ cảnh (context / 맥락) switch overhead tăng.
182. Starvation; aging boosts long-waiting priorities.
183. Completion-arrival; turnaround-burst; first-run-arrival.
184. kết quả (result / 결과) depends on timing/interleaving trạng thái dùng chung (shared state / 공유 상태).
185. mã (code / 코드) region accessing dùng chung (shared / 공유) tài nguyên (resource / 자원) needing synchronization.
186. quyền sở hữu (ownership / 소유권) mutual exclusion vs permit counter synchronization.
187. Mutual exclusion, hold-and-wait, no preemption, circular wait.
188. Break điều kiện (condition / 조건); stay safe based max demand; allow then detect/recover.
189. Fixed-size pages/frames vs variable logical segments.
190. Waste inside allocated fixed khối (block / 블록) vs holes between variable blocks.
191. Referenced virtual page not resident, OS resolves/tải (load / 로드).
192. Oldest; least recently used; farthest future use.
193. FIFO.
194. Translation trượt bộ nhớ đệm (cache miss / 캐시 미스) vs actual page not resident.
195. Paging dominates useful công việc (work / 작업) due insufficient frames/working set.
196. Reliable ordered connection-oriented stream vs connectionless datagrams no delivery/thứ tự (order / 순서) guarantee.
197. Logical addressing/routing packets.
198. 32 total, 30 usable traditional.
199. Trong matching routes chọn prefix dài nhất/specific nhất.
200. Receiver protection vs mạng (network / 네트워크) congestion phản hồi (response / 응답).

---

# Môn 5 — 정보시스템 구축 관리 — 50 recall prompts

201. Waterfall khác Iterative/Agile ở phản hồi (feedback / 피드백)/thay đổi (change / 변경) luồng (flow / 흐름) thế nào?
202. rủi ro (risk / 위험) khác Issue thế nào?
203. xác suất (probability / 확률) và Impact cùng dùng để đánh giá gì?
204. PERT expected-time formula là gì?
205. đường găng (critical path / 임계 경로) là gì?
206. Float/Slack là gì?
207. Forward Pass tính gì?
208. Backward Pass tính gì?
209. Vertical Scaling khác Horizontal Scaling thế nào?
210. tải (load / 로드) Balancing khác Failover thế nào?
211. Active-Active khác Active-Standby thế nào?
212. Single điểm (point / 지점) of thất bại (failure / 실패) là gì?
213. RAID 0, 1, 5, 6 khác nhau ở redundancy/parity thế nào?
214. Vì sao RAID không phải Backup?
215. Replication khác Backup thế nào?
216. Synchronous khác Asynchronous Replication sự đánh đổi (trade-off / 트레이드오프) gì?
217. Full, Incremental, Differential Backup khác nhau thế nào?
218. Cold, Warm, Hot Site khác nhau thế nào?
219. RTO là gì?
220. RPO là gì?
221. MTBF và MTTR là gì?
222. Availability cải thiện bằng hai hướng chỉ số (metric / 지표) nào?
223. IaaS, PaaS, SaaS khác responsibility thế nào?
224. VM khác bộ chứa (container / 컨테이너) thế nào?
225. ảnh (image / 이미지) khác bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) thế nào?
226. Orchestration xử lý những việc gì?
227. Threat, Vulnerability, Exploit, rủi ro (risk / 위험) khác nhau thế nào?
228. Confidentiality, Integrity, Availability là gì?
229. Authentication khác Authorization thế nào?
230. Least Privilege là gì?
231. Separation of Duties là gì?
232. Symmetric khác Asymmetric Encryption thế nào?
233. băm (hash / 해시) khác Encryption thế nào?
234. Encoding khác Encryption thế nào?
235. Salt dùng trong password hashing để làm gì?
236. Digital Signature cung cấp properties gì?
237. MAC khác Digital Signature thế nào?
238. ACL khác RBAC thế nào?
239. SQL Injection nguyên nhân gốc (root cause / 근본 원인)/mitigation chính là gì?
240. XSS nguyên nhân gốc (root cause / 근본 원인)/mitigation chính là gì?
241. CSRF khai thác điều gì?
242. Firewall khác WAF thế nào?
243. IDS khác IPS thế nào?
244. TLS khác VPN thế nào?
245. Stateful khác Stateless Firewall thế nào?
246. Vulnerability Scan khác Penetration kiểm thử (test / 테스트) thế nào?
247. Patch Management gồm những bước gì ngoài install patch?
248. SIEM làm gì?
249. sự cố (incident / 인시던트) phản hồi (response / 응답) vòng đời (lifecycle / 생명주기) khái quát gồm các bước nào?
250. Vì sao phải restore-test backup?

## Answer Cues — Môn 5

201. Sequential phase handoff/thay đổi (change / 변경) late vs short phản hồi (feedback / 피드백)/iterative adaptation.
202. Uncertain future sự kiện (event / 이벤트) vs hiện tại (current / 현재) realized bài toán (problem / 문제).
203. rủi ro (risk / 위험) exposure/prioritization.
204. `(O + 4M + P) / 6`.
205. Longest-duration zero-slack đường dẫn (path / 경로) determining dự án (project / 프로젝트) finish trong mạng (network / 네트워크) mô hình (model / 모델).
206. Delay allowance không đổi final finish theo hiện tại (current / 현재) mạng (network / 네트워크).
207. Earliest start/finish.
208. Latest start/finish.
209. Bigger nút (node / 노드) vs more nodes.
210. Distribute công việc (work / 작업) vs takeover after thất bại (failure / 실패).
211. Multiple live serving vs standby waits to take over.
212. Một thành phần (component / 컴포넌트)/đường dẫn (path / 경로) thất bại (failure / 실패) có thể làm whole dịch vụ (service / 서비스) thất bại (fail / 실패).
213. No redundancy striping; mirroring; single parity; dual parity.
214. Không bảo vệ deletion/ransomware/logical corruption/off-array disaster/lịch sử (history / 이력).
215. Live/hiện tại (current / 현재) copies for availability vs point-in-time recoverable copies/lịch sử (history / 이력).
216. Lower data-loss cửa sổ (window / 윈도우) but more độ trễ (latency / 지연 시간)/coupling vs lower coupling with lag rủi ro (risk / 위험).
217. All; since last backup; since last full.
218. Readiness/chi phí (cost / 비용) tăng từ cold → hot, RTO thường giảm.
219. mục tiêu (target / 대상) max khôi phục (recovery / 복구) thời gian (time / 시간).
220. mục tiêu (target / 대상) max data-loss interval.
221. Mean thời gian (time / 시간) between failures; mean thời gian (time / 시간) to repair/recover.
222. MTBF tăng, MTTR giảm.
223. Provider quản ngày càng nhiều ngăn xếp (stack / 스택) từ IaaS → SaaS.
224. Separate guest OS/kernel virtualization vs share host kernel/bộ chứa (container / 컨테이너) isolation.
225. Packaged template/layers vs running instance/tiến trình (process / 프로세스) trạng thái (state / 상태).
226. Scheduling, deploy, scaling, health, khám phá dịch vụ (service discovery / 서비스 디스커버리)/cấu hình (config / 설정)/secrets tùy nền tảng (platform / 플랫폼).
227. Potential harm actor/sự kiện (event / 이벤트); weakness; phương thức (method / 메서드) to use weakness; likelihood-impact-context exposure.
228. No unauthorized disclosure; no unauthorized modification; dịch vụ (service / 서비스) accessible when needed.
229. Who are you vs what may you do.
230. Chỉ quyền tối thiểu cần thiết.
231. Chia trọng yếu (critical / 중요) duties giữa nhiều principals/roles.
232. dùng chung (shared / 공유) secret efficient bulk vs công khai (public / 공개)/private key key-exchange/signature uses.
233. Reversible with key vs one-way digest.
234. biểu diễn (representation / 표현) transform, không confidentiality.
235. Chống precomputation/rainbow và same-password same-hash mẫu (pattern / 패턴).
236. Integrity, authenticity, non-repudiation các giả định (assumptions / 가정들) theo scheme/trust.
237. Shared-secret authenticator vs asymmetric signature.
238. Per-resource định danh (identity / 식별자)/group permissions vs permissions through roles.
239. Untrusted đầu vào (input / 입력) changes SQL cấu trúc (structure / 구조); use parameterized/prepared queries + least privilege.
240. Untrusted dữ liệu (data / 데이터) executed as trình duyệt (browser / 브라우저) script/markup; context-aware đầu ra (output / 출력) encoding + safe APIs/CSP defense-in-depth.
241. trình duyệt (browser / 브라우저) tự gửi authenticated credentials cho forged state-changing yêu cầu (request / 요청); anti-CSRF đơn vị từ (token / 토큰)/SameSite/origin checks.
242. mạng (network / 네트워크) traffic chính sách (policy / 정책) vs HTTP application-layer filtering.
243. Detect/alert vs inline khối (block / 블록)/prevent.
244. Secure vận chuyển (transport / 전송) channel for ứng dụng (application / 애플리케이션) liên kết (connection / 연결) vs broader protected tunnel/mạng (network / 네트워크) connectivity.
245. Per-packet rules vs liên kết (connection / 연결) trạng thái (state / 상태) tracking.
246. Automated weakness discovery vs controlled exploitation/chaining to prove impact.
247. Inventory → assess → kiểm thử (test / 테스트) → deploy → verify → quay lui (rollback / 롤백)/monitor.
248. Collect/correlate/analyze bảo mật (security / 보안) events/logs.
249. Preparation → Detection/phân tích (analysis / 분석) → Containment → Eradication → khôi phục (recovery / 복구) → Lessons Learned.
250. tệp (file / 파일) tồn tại không chứng minh restore được, dependencies/keys/procedure/RTO phải được verify.

---

# Scoring

Mỗi câu:

```text
1.0 = đúng mechanism + ranh giới
0.5 = đúng keyword nhưng giải thích mơ hồ
0.0 = sai / chỉ nhận ra sau khi xem cue
```

| Môn | Điểm / 50 |
|---|---:|
| 소프트웨어 설계 | ___ |
| 소프트웨어 개발 | ___ |
| 데이터베이스 구축 | ___ |
| 프로그래밍 언어 활용 | ___ |
| 정보시스템 구축 관리 | ___ |

## Remediation thresholds
Phần “Remediation thresholds” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- **45–50:** breadth tốt; chuyển sang scenario/mock.
- **38–44.5:** có gaps nhỏ; dùng `15-edge-case-coverage-supplement.md` + `11-high-risk-confusion-atlas.md`.
- **30–37.5:** chưa đủ closed-book coverage; quay deep-dive của môn.
- **<30:** không nên tiếp tục spam mock; học lại Master Guide + deep-dive theo chapter.

## Spaced recall

Không làm 250 câu trong một ngày rồi bỏ. Một vòng hợp lý:

```text
Day 0: 50 câu một môn
Day 1: làm lại câu sai + 15 transfer questions tự tạo
Day 3: random 25 câu môn đó
Day 7: random 25 câu + 10 câu cross-subject
Day 14: closed-book full 50
```

Mục tiêu cuối không phải thuộc câu hỏi trong tệp (file / 파일), mà trả lời được **cùng cơ chế (mechanism / 메커니즘) khi wording, noun, số liệu và scenario thay đổi**.
