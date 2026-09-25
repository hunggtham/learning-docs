# 정보처리기사 필기 2026 — Active Recall Bank 250

> 250 câu **không có lựa chọn A/B/C/D**, chia đều 50 câu/môn. Đây là lớp kiểm tra breadth sau khi đã đọc deep-dive. Mỗi câu phải trả lời bằng lời của mình trước khi xem `Answer Cues` ở cuối từng môn.
>
> Quy tắc: nếu chỉ nhận ra đáp án sau khi nhìn cue, tính là **sai**. Nếu trả lời đúng keyword nhưng không giải thích được mechanism/ranh giới, tính **0.5 điểm**.

---

# Môn 1 — 소프트웨어 설계 — 50 recall prompts

1. Functional Requirement khác Non-functional Requirement ở câu hỏi cốt lõi nào?  
2. Verification khác Validation thế nào?  
3. Ambiguity khác Inconsistency thế nào?  
4. Requirement Traceability phục vụ hai mục đích chính nào?  
5. Feasibility khác Priority thế nào?  
6. Flow chính của requirements development gồm bốn bước nào?  
7. DFD tập trung vào cái gì?  
8. DFD balancing nghĩa là gì?  
9. Data Dictionary khác Mini-specification thế nào?  
10. Decision Table hữu ích nhất khi nào?  
11. Use Case Diagram trả lời câu hỏi gì?  
12. Sequence Diagram trả lời câu hỏi gì?  
13. Activity Diagram khác State Machine Diagram thế nào?  
14. Component Diagram khác Deployment Diagram thế nào?  
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
26. Common Coupling là gì?  
27. External Coupling là gì?  
28. Control Coupling là gì?  
29. Stamp Coupling khác Data Coupling thế nào?  
30. Fan-in và Fan-out là gì?  
31. Encapsulation khác Abstraction thế nào?  
32. Inheritance khác Polymorphism thế nào?  
33. SRP phát hiện design smell nào?  
34. OCP nhắm mục tiêu gì?  
35. LSP hỏi điều gì về subtype?  
36. ISP giải quyết vấn đề gì?  
37. DIP thay đổi hướng dependency thế nào?  
38. Factory Method khác Abstract Factory thế nào?  
39. Builder khác Prototype thế nào?  
40. Adapter khác Facade thế nào?  
41. Decorator khác Proxy thế nào?  
42. Strategy khác State thế nào?  
43. Observer dùng cho relationship nào?  
44. Command pattern đóng gói cái gì?  
45. Template Method giữ cố định phần nào và mở rộng phần nào?  
46. Interface contract ngoài field/data còn cần gì?  
47. Retry có thể gây duplicate side effect thế nào?  
48. Idempotency giải quyết vấn đề gì?  
49. Point-to-point integration scale kém ở đâu?  
50. Breaking API change có thể xảy ra dù field name không đổi bằng cách nào?

## Answer Cues — Môn 1

1. **What vs quality/constraint:** capability nghiệp vụ vs chất lượng/ràng buộc.  
2. **Build product right vs build right product.**  
3. Nhiều cách hiểu vs hai requirement mâu thuẫn.  
4. Impact analysis + coverage/source-to-test tracing.  
5. Có làm được trong constraints không vs nên làm trước/giá trị tương đối.  
6. Elicitation → Analysis → Specification → Validation.  
7. Data flow/transformation giữa entity, process, store.  
8. Parent process external I/O phải được bảo toàn khi decomposition.  
9. Định nghĩa data vs định nghĩa processing logic.  
10. Nhiều combinations condition/action cần systematic coverage.  
11. Actors và system functions/goals.  
12. Message order giữa participants theo thời gian.  
13. Workflow/actions vs lifecycle state của object.  
14. Software components/dependencies vs deployment nodes/artifacts.  
15. General relation; weak whole-part; strong lifecycle ownership.  
16. Is-a hierarchy vs implementation of interface/specification.  
17. Required reused behavior vs optional/conditional extension.  
18. Skeleton/layout vs visual appearance gần thành phẩm.  
19. Interactive sample vs scenario sequence/story flow.  
20. Dễ hiểu ngay vs dễ học qua thời gian.  
21. Nội bộ cùng mục tiêu, dependency ngoài thấp.  
22. Mọi elements cùng phục vụ một chức năng rõ.  
23. Output step trước thành input step sau.  
24. Operations cùng dùng/chỉnh same data set.  
25. Module chạm trực tiếp internals của module khác.  
26. Share global/common data.  
27. Cùng phụ thuộc external format/protocol/device.  
28. Truyền flag/control information điều khiển logic bên nhận.  
29. Truyền structure dư thừa vs chỉ data cần thiết.  
30. Số callers vào / số dependencies gọi ra.  
31. Hide/control state representation vs giữ essence, bỏ detail.  
32. Type hierarchy/reuse vs same interface, different runtime behavior.  
33. Class có nhiều reasons to change/responsibilities.  
34. Mở rộng behavior mà hạn chế sửa stable code.  
35. Subtype thay base mà không phá contract.  
36. Fat interface ép client phụ thuộc methods không dùng.  
37. High-level và low-level cùng phụ thuộc abstraction.  
38. Delegated creation method vs factory tạo family related objects.  
39. Step-by-step construction vs clone existing object.  
40. Convert incompatible interface vs simplify complex subsystem.  
41. Add behavior by wrapper vs stand-in/control access.  
42. Select algorithm/policy vs behavior driven by internal state.  
43. One-to-many notification.  
44. Request/action thành object.  
45. Skeleton cố định, steps override/extend.  
46. Protocol, sequence, error, timeout, retry, auth/security, compatibility.  
47. Client không biết outcome sau timeout rồi gửi lại same operation.  
48. Repeated same logical request không nhân side effect.  
49. Connection/dependency graph tăng nhanh khi số systems tăng.  
50. Change type, nullability, enum semantics, meaning, constraints.

---

# Môn 2 — 소프트웨어 개발 — 50 recall prompts

51. ADT khác implementation thế nào?  
52. Stack và Queue khác nhau ở access order nào?  
53. BST invariant cơ bản là gì?  
54. Heap invariant cơ bản là gì?  
55. Complete Binary Tree có hình dạng thế nào?  
56. BFS dùng data structure nào?  
57. DFS thường dùng data structure/cơ chế nào?  
58. Vì sao BFS cho shortest path theo số cạnh trong unweighted graph?  
59. MST khác shortest path thế nào?  
60. Adjacency Matrix và List trade-off gì?  
61. Binary Search cần precondition nào?  
62. Quick Sort worst-case điển hình là gì?  
63. Merge Sort worst-case điển hình là gì?  
64. Stable sort nghĩa là gì?  
65. In-place nghĩa là gì?  
66. Hash collision là gì?  
67. Linear Probing gây clustering nào?  
68. Vì sao open-address deletion cần tombstone/rehash logic?  
69. Static Testing khác Dynamic Testing thế nào?  
70. Error → Defect → Failure liên hệ thế nào?  
71. Test Condition khác Test Case thế nào?  
72. Equivalence Partitioning làm gì?  
73. Boundary Value Analysis làm gì?  
74. Statement Coverage đo gì?  
75. Branch Coverage đo gì?  
76. Vì sao 100% statement chưa bảo đảm 100% branch?  
77. Condition Coverage khác Branch Coverage thế nào?  
78. Cyclomatic Complexity có thể tính bằng công thức nào?  
79. Top-down Integration dùng Stub vì sao?  
80. Bottom-up Integration dùng Driver vì sao?  
81. Unit, Integration, System, Acceptance khác scope thế nào?  
82. Alpha và Beta khác môi trường/người dùng thế nào?  
83. Retest khác Regression thế nào?  
84. Smoke test có intent gì?  
85. Performance Throughput khác Response Time thế nào?  
86. Load test khác Stress test thế nào?  
87. Configuration Item có thể gồm những gì ngoài source?  
88. Baseline là gì?  
89. Version Control khác Configuration Management thế nào?  
90. Build khác Release thế nào?  
91. Packaging gồm những gì ngoài binary?  
92. Checksum kiểm property gì?  
93. DRM giải quyết vấn đề gì?  
94. Interface validation khác business validation thế nào?  
95. Serialization error khác semantic validation error thế nào?  
96. Retryable error thường có đặc điểm gì?  
97. Interface observability nên theo dõi những metric nào?  
98. Deduplication khác Idempotency thế nào?  
99. Contract test kiểm cái gì?  
100. Regression suite tốt cần tránh overfit vào implementation detail thế nào?

## Answer Cues — Môn 2

51. Behavior/interface abstraction vs array/list/tree concrete realization.  
52. LIFO vs FIFO.  
53. Left keys < node < right keys theo comparison invariant phù hợp.  
54. Parent ordered relative to children, không full BST order.  
55. Fill level by level, last level left-to-right.  
56. Queue.  
57. Stack/recursion.  
58. Explore vertices theo distance layers.  
59. Connect all vertices min total weight vs min path from source.  
60. O(V²) fast edge lookup vs O(V+E) sparse-friendly.  
61. Search range ordered/sorted theo comparator.  
62. O(n²).  
63. O(n log n).  
64. Giữ relative order của equal-key records.  
65. Auxiliary memory nhỏ, mutate structure chính.  
66. Different keys same hash/bucket.  
67. Primary clustering.  
68. Xóa “never used” có thể làm search dừng sớm, phá probe chain.  
69. Không execute vs execute program.  
70. Human mistake tạo fault; fault activated có thể gây observable failure.  
71. Aspect cần test vs concrete inputs/steps/expected result.  
72. Chia input thành classes behavior tương đương.  
73. Test edges ngay quanh boundaries.  
74. Executed statements.  
75. Decision outcomes/branches.  
76. Có thể execute true branch statements mà chưa test false outcome.  
77. Atomic conditions true/false vs overall decision outcomes.  
78. `E - N + 2P` hoặc decisions + 1 trong simple connected flow.  
79. Mô phỏng callees phía dưới chưa có.  
80. Mô phỏng callers phía trên chưa có.  
81. Component nhỏ → interactions → full system → user/business acceptance.  
82. Internal controlled users/environment vs external representative users.  
83. Xác nhận bug fix vs kiểm không phá behavior khác.  
84. Build có đủ ổn để test sâu tiếp không.  
85. Work/time vs elapsed per request/operation.  
86. Expected/high workload vs vượt limits để tìm breaking behavior.  
87. Requirements, config, schema, scripts, tests, binaries, manuals.  
88. Controlled established configuration/version state.  
89. History/branch/version tooling vs broader identification/change/status/audit/release process.  
90. Compile/package artifact vs đưa selected version tới environment/users.  
91. Dependencies, config, metadata, install docs, license/manual.  
92. Integrity/change/corruption.  
93. Rights/license/usage control của digital content.  
94. Shape/type/required fields vs domain/business rules.  
95. Không parse/encode được vs data parse được nhưng không hợp contract/business.  
96. Transient infrastructure/network/server condition, operation safe to retry.  
97. Latency, error, throughput, retry, timeout, backlog, contract failure.  
98. Technique remove duplicates vs semantic repeated operation same effect.  
99. Provider/consumer interface assumptions và compatibility.  
100. Assert externally meaningful behavior, không khóa test vào private implementation vô ích.

---

# Môn 3 — 데이터베이스 구축 — 50 recall prompts

101. Relation, Tuple, Attribute, Domain là gì?  
102. Degree khác Cardinality thế nào?  
103. Super Key khác Candidate Key thế nào?  
104. Primary Key khác Alternate Key thế nào?  
105. Foreign Key bảo vệ integrity nào?  
106. Natural Key khác Surrogate Key thế nào?  
107. Selection khác Projection thế nào?  
108. Join dùng để làm gì?  
109. Division operation biểu diễn loại query logic nào?  
110. Functional Dependency `X → Y` nghĩa là gì?  
111. Trivial FD là gì?  
112. Attribute Closure dùng để làm gì?  
113. Prime Attribute là gì?  
114. Partial Dependency là gì?  
115. Transitive Dependency là gì?  
116. 1NF nhắm tới vấn đề gì?  
117. 2NF loại vấn đề gì?  
118. 3NF formal condition khái quát là gì?  
119. BCNF condition là gì?  
120. Lossless decomposition là gì?  
121. Dependency preservation là gì?  
122. Logical Design khác Physical Design thế nào?  
123. B+Tree index phù hợp range vì sao?  
124. Hash index tự nhiên phù hợp query nào?  
125. Selectivity là gì?  
126. Covering Index là gì?  
127. Composite index order quan trọng vì sao?  
128. Index nhiều gây write cost thế nào?  
129. View là gì?  
130. Vì sao aggregate view có thể không updatable đơn giản?  
131. DDL, DML, DCL, TCL cho mỗi nhóm một ví dụ.  
132. WHERE khác HAVING thế nào?  
133. INNER JOIN khác LEFT JOIN thế nào?  
134. `COUNT(*)` khác `COUNT(col)` thế nào?  
135. NULL dùng logic mấy giá trị?  
136. Vì sao `col = NULL` sai logic?  
137. UNION khác UNION ALL thế nào?  
138. Correlated Subquery là gì?  
139. ACID gồm bốn property nào?  
140. Atomicity khác Consistency thế nào?  
141. Isolation bảo vệ cái gì?  
142. Durability bảo vệ cái gì?  
143. Dirty Read là gì?  
144. Non-repeatable Read là gì?  
145. Phantom Read là gì?  
146. Conflict Serializability kiểm bằng cách nào?  
147. Two-Phase Locking có hai phase gì?  
148. Deadlock Wait-for Graph biểu diễn edge gì?  
149. WAL và Checkpoint khác vai trò thế nào?  
150. Migration Reconciliation nên kiểm những gì ngoài row count?

## Answer Cues — Môn 3

101. Table-like relation, row tuple, column attribute, allowed values domain.  
102. Số columns vs số rows.  
103. Unique determinant vs minimal unique determinant.  
104. Candidate key được chọn làm chính vs candidate keys còn lại.  
105. Referential integrity.  
106. Business-meaning identifier vs generated/artificial identifier.  
107. Rows vs columns.  
108. Combine related tuples theo condition.  
109. “Entities liên hệ với tất cả members của một set” kiểu all-for-all.  
110. Cùng X value quyết định duy nhất Y value.  
111. Y subset của X.  
112. Tìm attributes suy ra từ set, test super/candidate key.  
113. Thuộc ít nhất một candidate key.  
114. Non-prime depends on proper subset of composite candidate key.  
115. Key → non-key → non-key.  
116. Atomic attribute/domain representation, loại repeating group theo relational form.  
117. Partial dependency.  
118. Với non-trivial X→A, X superkey hoặc A prime.  
119. Mọi determinant non-trivial phải superkey.  
120. Join relations con khôi phục đúng original không spurious tuples.  
121. Enforce dependencies trên relations con không cần join.  
122. Relational structure/constraints vs storage/index/partition/access path.  
123. Ordered keys + tree range traversal.  
124. Equality lookup.  
125. Fraction/discrimination của predicate/index key; ít matches thường selective hơn.  
126. Index chứa đủ data trả query không cần table lookup thêm.  
127. Leftmost/prefix ordering quyết định usable search ranges tùy DBMS.  
128. Mỗi write phải maintain indexes, thêm I/O/storage/contention.  
129. Virtual/query-defined relation.  
130. One view row có thể không map uniquely về underlying row changes.  
131. CREATE; SELECT/INSERT/UPDATE; GRANT; COMMIT/ROLLBACK.  
132. Filter rows before grouping vs filter groups after aggregate.  
133. Matching rows only vs preserve all left rows.  
134. All rows vs non-NULL values của column.  
135. TRUE/FALSE/UNKNOWN.  
136. NULL không phải ordinary value; dùng IS NULL.  
137. Deduplicate vs preserve duplicates.  
138. Inner query references current outer row.  
139. Atomicity, Consistency, Isolation, Durability.  
140. All-or-nothing vs valid-state invariant transition.  
141. Concurrent interference/anomalies.  
142. Committed data survives crash theo persistence/recovery guarantees.  
143. Read uncommitted data.  
144. Same row read twice changes after another committed update.  
145. Same predicate returns added/removed rows.  
146. Build precedence graph; acyclic = conflict-serializable.  
147. Growing acquire, Shrinking release.  
148. Ti waits for resource held by Tj.  
149. Logging-before-data recovery rule vs recovery progress point/reduce scan.  
150. Key uniqueness, RI, aggregates, checksums, encoding, precision, business invariants.

---

# Môn 4 — 프로그래밍 언어 활용 — 50 recall prompts

151. Compiler, Interpreter và JIT khác nhau ở đâu?  
152. Framework khác Library ở flow-control ownership thế nào?  
153. Scope khác Lifetime thế nào?  
154. Value semantics khác Reference semantics thế nào?  
155. Java pass-by-value với object reference nghĩa là gì?  
156. Trong C, `&x`, `p`, `*p` lần lượt là gì?  
157. Pointer arithmetic `p+1` phụ thuộc gì?  
158. Array decay thành pointer trong context nào và ngoại lệ ý tưởng nào cần nhớ?  
159. C string kết thúc bằng gì?  
160. `strlen` có tính null terminator không?  
161. Struct khác Union thế nào?  
162. Pre-increment khác Post-increment thế nào?  
163. Recursion cần hai thành phần logic nào?  
164. Java Overloading khác Overriding thế nào?  
165. Runtime polymorphism chọn overridden instance method theo gì?  
166. Abstract Class khác Interface khái quát thế nào?  
167. Checked Exception khác Unchecked Exception thế nào?  
168. Java String khác StringBuilder về mutability thế nào?  
169. `==` object reference khác `.equals()` thế nào?  
170. Python name binding nghĩa là gì?  
171. Mutable vs Immutable cho ví dụ mỗi loại.  
172. Shallow Copy khác Deep Copy thế nào?  
173. Python slicing stop index có inclusive không?  
174. Mutable Default Argument có bẫy gì?  
175. Process khác Thread thế nào?  
176. Ready khác Blocked state thế nào?  
177. FCFS có vấn đề Convoy Effect là gì?  
178. SJF ưu điểm và risk nào?  
179. SRTF khác SJF thế nào?  
180. Round Robin phụ thuộc parameter gì?  
181. Time quantum quá nhỏ gây gì?  
182. Priority Scheduling có risk nào và Aging giúp thế nào?  
183. Turnaround, Waiting, Response time formulas là gì?  
184. Race Condition là gì?  
185. Critical Section là gì?  
186. Mutex khác Semaphore thế nào?  
187. Bốn Coffman conditions là gì?  
188. Deadlock Prevention khác Avoidance khác Detection thế nào?  
189. Paging khác Segmentation thế nào?  
190. Internal khác External Fragmentation thế nào?  
191. Page Fault là gì?  
192. FIFO, LRU, Optimal chọn victim theo gì?  
193. Belady’s Anomaly gắn với policy nào?  
194. TLB miss khác Page Fault thế nào?  
195. Thrashing là gì?  
196. TCP khác UDP thế nào?  
197. OSI Network Layer làm gì?  
198. `/27` có bao nhiêu total/usable IPv4 addresses theo cách tính truyền thống?  
199. Longest Prefix Match là gì?  
200. Flow Control khác Congestion Control thế nào?

## Answer Cues — Môn 4

151. Ahead-of-time translation, runtime interpretation, runtime hot-code compilation.  
152. App calls library; framework owns skeleton và calls app hooks.  
153. Lexical/access visibility vs runtime existence.  
154. Copy data vs copy reference tới shared object.  
155. Copy của reference value được truyền; vẫn có thể mutate same object.  
156. Address of x; stored address; value at address.  
157. Pointed element type/size semantics.  
158. Many expressions decay; `sizeof` on actual array và `&array` là key exceptions/concepts.  
159. `\0`.  
160. Không.  
161. Separate storage vs shared storage.  
162. Increment before expression value vs value old rồi increment side effect.  
163. Base case + recursive step tiến tới base.  
164. Same name/different parameters compile-time vs subclass replacement runtime.  
165. Actual runtime object.  
166. Class abstraction có state/constructor/concrete methods vs contract/multiple implementation model.  
167. Catch/declare compile-time rule vs RuntimeException hierarchy unchecked.  
168. Immutable vs mutable builder.  
169. Identity vs logical equality contract.  
170. Names bind to objects; assignment không copy object mặc định.  
171. list/dict mutable; int/str/tuple structure immutable.  
172. Outer copy only vs recursive graph copy.  
173. Exclusive.  
174. Default object created once at definition, shared across calls.  
175. Separate address/resource context vs execution units sharing process resources.  
176. Ready waits CPU; Blocked waits event/I/O.  
177. Short jobs stuck behind long job.  
178. Low average waiting if burst known; starvation/unknown burst issue.  
179. Preemptive shortest remaining time.  
180. Time quantum.  
181. Context switch overhead tăng.  
182. Starvation; aging boosts long-waiting priorities.  
183. Completion-arrival; turnaround-burst; first-run-arrival.  
184. Result depends on timing/interleaving shared state.  
185. Code region accessing shared resource needing synchronization.  
186. Ownership mutual exclusion vs permit counter synchronization.  
187. Mutual exclusion, hold-and-wait, no preemption, circular wait.  
188. Break condition; stay safe based max demand; allow then detect/recover.  
189. Fixed-size pages/frames vs variable logical segments.  
190. Waste inside allocated fixed block vs holes between variable blocks.  
191. Referenced virtual page not resident, OS resolves/load.  
192. Oldest; least recently used; farthest future use.  
193. FIFO.  
194. Translation cache miss vs actual page not resident.  
195. Paging dominates useful work due insufficient frames/working set.  
196. Reliable ordered connection-oriented stream vs connectionless datagrams no delivery/order guarantee.  
197. Logical addressing/routing packets.  
198. 32 total, 30 usable traditional.  
199. Trong matching routes chọn prefix dài nhất/specific nhất.  
200. Receiver protection vs network congestion response.

---

# Môn 5 — 정보시스템 구축 관리 — 50 recall prompts

201. Waterfall khác Iterative/Agile ở feedback/change flow thế nào?  
202. Risk khác Issue thế nào?  
203. Probability và Impact cùng dùng để đánh giá gì?  
204. PERT expected-time formula là gì?  
205. Critical Path là gì?  
206. Float/Slack là gì?  
207. Forward Pass tính gì?  
208. Backward Pass tính gì?  
209. Vertical Scaling khác Horizontal Scaling thế nào?  
210. Load Balancing khác Failover thế nào?  
211. Active-Active khác Active-Standby thế nào?  
212. Single Point of Failure là gì?  
213. RAID 0, 1, 5, 6 khác nhau ở redundancy/parity thế nào?  
214. Vì sao RAID không phải Backup?  
215. Replication khác Backup thế nào?  
216. Synchronous khác Asynchronous Replication trade-off gì?  
217. Full, Incremental, Differential Backup khác nhau thế nào?  
218. Cold, Warm, Hot Site khác nhau thế nào?  
219. RTO là gì?  
220. RPO là gì?  
221. MTBF và MTTR là gì?  
222. Availability cải thiện bằng hai hướng metric nào?  
223. IaaS, PaaS, SaaS khác responsibility thế nào?  
224. VM khác Container thế nào?  
225. Image khác Container runtime thế nào?  
226. Orchestration xử lý những việc gì?  
227. Threat, Vulnerability, Exploit, Risk khác nhau thế nào?  
228. Confidentiality, Integrity, Availability là gì?  
229. Authentication khác Authorization thế nào?  
230. Least Privilege là gì?  
231. Separation of Duties là gì?  
232. Symmetric khác Asymmetric Encryption thế nào?  
233. Hash khác Encryption thế nào?  
234. Encoding khác Encryption thế nào?  
235. Salt dùng trong password hashing để làm gì?  
236. Digital Signature cung cấp properties gì?  
237. MAC khác Digital Signature thế nào?  
238. ACL khác RBAC thế nào?  
239. SQL Injection root cause/mitigation chính là gì?  
240. XSS root cause/mitigation chính là gì?  
241. CSRF khai thác điều gì?  
242. Firewall khác WAF thế nào?  
243. IDS khác IPS thế nào?  
244. TLS khác VPN thế nào?  
245. Stateful khác Stateless Firewall thế nào?  
246. Vulnerability Scan khác Penetration Test thế nào?  
247. Patch Management gồm những bước gì ngoài install patch?  
248. SIEM làm gì?  
249. Incident Response lifecycle khái quát gồm các bước nào?  
250. Vì sao phải restore-test backup?

## Answer Cues — Môn 5

201. Sequential phase handoff/change late vs short feedback/iterative adaptation.  
202. Uncertain future event vs current realized problem.  
203. Risk exposure/prioritization.  
204. `(O + 4M + P) / 6`.  
205. Longest-duration zero-slack path determining project finish trong network model.  
206. Delay allowance không đổi final finish theo current network.  
207. Earliest start/finish.  
208. Latest start/finish.  
209. Bigger node vs more nodes.  
210. Distribute work vs takeover after failure.  
211. Multiple live serving vs standby waits to take over.  
212. Một component/path failure có thể làm whole service fail.  
213. No redundancy striping; mirroring; single parity; dual parity.  
214. Không bảo vệ deletion/ransomware/logical corruption/off-array disaster/history.  
215. Live/current copies for availability vs point-in-time recoverable copies/history.  
216. Lower data-loss window but more latency/coupling vs lower coupling with lag risk.  
217. All; since last backup; since last full.  
218. Readiness/cost tăng từ cold → hot, RTO thường giảm.  
219. Target max recovery time.  
220. Target max data-loss interval.  
221. Mean time between failures; mean time to repair/recover.  
222. MTBF tăng, MTTR giảm.  
223. Provider quản ngày càng nhiều stack từ IaaS → SaaS.  
224. Separate guest OS/kernel virtualization vs share host kernel/container isolation.  
225. Packaged template/layers vs running instance/process state.  
226. Scheduling, deploy, scaling, health, service discovery/config/secrets tùy platform.  
227. Potential harm actor/event; weakness; method to use weakness; likelihood-impact-context exposure.  
228. No unauthorized disclosure; no unauthorized modification; service accessible when needed.  
229. Who are you vs what may you do.  
230. Chỉ quyền tối thiểu cần thiết.  
231. Chia critical duties giữa nhiều principals/roles.  
232. Shared secret efficient bulk vs public/private key key-exchange/signature uses.  
233. Reversible with key vs one-way digest.  
234. Representation transform, không confidentiality.  
235. Chống precomputation/rainbow và same-password same-hash pattern.  
236. Integrity, authenticity, non-repudiation assumptions theo scheme/trust.  
237. Shared-secret authenticator vs asymmetric signature.  
238. Per-resource identity/group permissions vs permissions through roles.  
239. Untrusted input changes SQL structure; use parameterized/prepared queries + least privilege.  
240. Untrusted data executed as browser script/markup; context-aware output encoding + safe APIs/CSP defense-in-depth.  
241. Browser tự gửi authenticated credentials cho forged state-changing request; anti-CSRF token/SameSite/origin checks.  
242. Network traffic policy vs HTTP application-layer filtering.  
243. Detect/alert vs inline block/prevent.  
244. Secure transport channel for application connection vs broader protected tunnel/network connectivity.  
245. Per-packet rules vs connection state tracking.  
246. Automated weakness discovery vs controlled exploitation/chaining to prove impact.  
247. Inventory → assess → test → deploy → verify → rollback/monitor.  
248. Collect/correlate/analyze security events/logs.  
249. Preparation → Detection/Analysis → Containment → Eradication → Recovery → Lessons Learned.  
250. File tồn tại không chứng minh restore được, dependencies/keys/procedure/RTO phải được verify.

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

Mục tiêu cuối không phải thuộc câu hỏi trong file, mà trả lời được **cùng mechanism khi wording, noun, số liệu và scenario thay đổi**.
