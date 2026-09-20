# Amortized, Randomized và Probabilistic Thinking
**Amortized Analysis, Randomization & Probabilistic Reasoning / 상환 분석, 무작위화, 확률적 사고**

Không phải mọi guarantee trong DSA đều có dạng “mỗi operation chắc chắn mất `O(f(n))`”. Có những structure thỉnh thoảng làm một operation rất đắt nhưng cả chuỗi operations vẫn rẻ; có algorithm dùng randomness để tránh input xấu; và có structure cố ý chấp nhận xác suất error để đổi lấy memory nhỏ hơn nhiều.

Ba nhóm ý tưởng này dễ bị trộn lẫn, nhưng chúng trả lời ba câu hỏi khác nhau:

**Amortized analysis** phân bổ cost trên một sequence operations.

**Randomized analysis** lấy expectation trên random choices của algorithm hoặc random model.

**Probabilistic data structure** cho phép answer có uncertainty được kiểm soát để đạt trade-off space/time tốt hơn.

## 1. Amortized không phải Average-case

Đây là distinction rất quan trọng.

Average-case analysis thường cần distribution assumptions về inputs. Amortized analysis không cần giả sử input random. Nó nói rằng dù adversary chọn sequence operations thế nào trong model cho phép, tổng cost trên sequence vẫn bị bounded.

Dynamic array append là ví dụ kinh điển. Một append bình thường `O(1)`, nhưng lúc capacity đầy phải allocate array mới và copy `O(n)` elements. Một operation riêng lẻ có thể đắt, nhưng nếu capacity tăng theo factor như 2, tổng copy cost qua `m` appends vẫn `O(m)`, nên amortized append là `O(1)`.

## 2. Aggregate Method

**Aggregate analysis** tính tổng cost của `m` operations rồi chia cho `m`.

Giả sử dynamic array bắt đầu capacity 1 và double mỗi lần full. Copy counts qua resizes:

```text
1 + 2 + 4 + 8 + ... < 2m
```

ngoài `m` writes của appends. Tổng vẫn `O(m)`, nên amortized cost mỗi append `O(1)`.

Điểm quan trọng là expensive resizes hiếm dần theo geometric growth.

## 3. Accounting Method

Accounting method tưởng tượng mỗi cheap operation trả một “credit” lớn hơn actual cost. Credit dư được cất lại để trả cho future expensive operation.

Ví dụ mỗi append có thể được charge 3 units dù actual normal append chỉ cost 1. Hai units dư tích lũy trên elements/structure; khi resize xảy ra, credits trả cho copies.

Nếu thiết kế accounting scheme sao cho balance không bao giờ âm, tổng actual cost không thể vượt tổng charges.

Phương pháp này giúp biến proof thành intuition “operation rẻ trả trước cho operation đắt”.

## 4. Potential Method

Potential method tổng quát hơn. Gán cho data structure state `D` một potential:

\[
\Phi(D) \ge 0
\]

Amortized cost của operation `i`:

\[
\hat c_i = c_i + \Phi(D_i)-\Phi(D_{i-1})
\]

Nếu operation làm structure tích lũy “khả năng gây work tương lai”, potential tăng và amortized charge lớn hơn actual. Nếu operation đắt tiêu thụ phần potential đó, potential giảm và bù lại actual cost.

Khi cộng telescoping qua sequence:

\[
\sum \hat c_i = \sum c_i + \Phi(D_m)-\Phi(D_0)
\]

Nếu initial potential nhỏ/0 và potential luôn nonnegative, amortized total upper-bound actual total theo cách có kiểm soát.

## 5. Stack với multipop

Giả sử stack hỗ trợ `push`, `pop` và `multipop(k)` pop tối đa k items. Một `multipop` riêng có thể `O(n)`.

Nhưng mỗi item chỉ được pushed một lần và popped tối đa một lần. Qua `m` operations, tổng number of pops không vượt total pushes. Vì vậy total work `O(m)` và amortized mỗi operation `O(1)`.

Đây là ví dụ rất sạch: expensive operation không thể xảy ra liên tục vì nó tiêu thụ resource đã tích lũy trước đó.

## 6. Monotonic Stack cũng dùng amortized reasoning

Trong algorithms như Next Greater Element, mỗi element được push một lần và pop tối đa một lần khỏi monotonic stack.

Dù inner `while` có vẻ nested và một iteration có thể pop nhiều elements, tổng pops trên toàn algorithm chỉ `O(n)`.

Vì vậy whole algorithm `O(n)`, không phải `O(n^2)`.

Đây là một pattern phân tích rất quan trọng: nested loop chưa chắc quadratic nếu inner work tiêu thụ objects không quay lại.

## 7. Union-Find và inverse Ackermann

DSU với union-by-rank/size và path compression có amortized complexity gần constant:

\[
O(\alpha(n))
\]

với inverse Ackermann function tăng cực chậm.

Một `find` riêng có thể traverse nhiều nodes trước compression, nhưng sequence operations làm forest ngày càng phẳng. Phân tích chính xác phức tạp, nhưng mental model là expensive traversals đồng thời cải thiện structure cho future operations.

Amortized analysis giải thích tại sao performance thực tế tốt hơn worst-case của một single uncompressed path traversal.

## 8. Splay Tree và amortized guarantee

Splay Tree không giữ strict AVL/Red-Black balance sau mỗi operation. Sau access, node được splay lên root bằng rotations.

Một operation có thể `O(n)`, nhưng sequence operations có amortized `O(log n)` dưới analysis chuẩn.

Đổi lại, recently accessed elements gần root hơn, tạo locality property tự thích nghi.

Đây là ví dụ structure deliberately không bảo đảm worst-case mỗi operation để có amortized guarantee và adaptive behavior.

## 9. Amortized guarantee và latency-sensitive systems

Amortized `O(1)` không có nghĩa mọi request latency `O(1)`. Dynamic-array resize hoặc hash-table rehash vẫn có thể tạo spike.

Trong real-time hoặc low-tail-latency system, worst-case individual operation có thể quan trọng hơn average throughput. Có thể cần incremental rehashing, preallocation hoặc structure có deterministic bounds.

Vì vậy khi nói “O(1) amortized”, phải giữ nguyên từ **amortized**; bỏ nó đi làm guarantee mạnh hơn thực tế.

## 10. Randomized Algorithm là gì?

Randomized algorithm dùng random choices như một phần logic. Với cùng input, hai runs có thể đi theo path khác nhau.

Mục tiêu thường là tránh deterministic worst-case patterns hoặc đơn giản hóa algorithm.

Randomized Quicksort chọn pivot ngẫu nhiên. Input có thể đã sorted, nhưng pivot positions không bị fixed vào boundary theo một deterministic bad strategy như “luôn chọn phần tử đầu”.

Expected runtime:

\[
O(n\log n)
\]

trên randomness của pivot choices.

## 11. Expected time không phải deterministic bound

Nói randomized quicksort expected `O(n log n)` không có nghĩa mỗi run chắc chắn dưới `cn log n`.

Một run xấu vẫn có thể gần `O(n^2)`, nhưng xác suất của chuỗi partitions cực xấu nhỏ dưới random model chuẩn.

Expected complexity phải luôn nói expectation đang lấy trên cái gì: random choices của algorithm, random input distribution hay hash function family.

## 12. Las Vegas vs Monte Carlo

Hai flavor quan trọng:

**Las Vegas algorithm** luôn trả answer đúng; randomness ảnh hưởng runtime hoặc path execution. Randomized Quicksort là ví dụ: output vẫn sorted đúng, chỉ runtime thay đổi.

**Monte Carlo algorithm** chạy trong time bound tốt hơn nhưng có xác suất answer sai. Repeated randomized primality tests hoặc fingerprint-based equality checks có thể thuộc dạng này tùy construction.

Distinction giúp nói rõ guarantee: random runtime hay random correctness.

## 13. Randomized Hashing và adversarial inputs

Hash table expected `O(1)` thường dựa trên hash distribution tốt. Nếu attacker có thể chọn keys tạo collisions, worst-case chain/probe sequence có thể xấu.

Randomized/universal hashing chọn hash function từ một family sao cho fixed adversarial key set khó predict collisions trước khi random seed được biết.

Trong systems nhận untrusted input, security/adversarial model quan trọng hơn textbook average-case assumption.

Một số runtime còn chuyển bucket collision-heavy sang tree-like structure hoặc randomize hash seeds để giảm denial-of-service risks.

## 14. Treap: random priorities tạo expected balance

Treap kết hợp BST ordering theo key với heap ordering theo random priority.

Nếu priorities random độc lập, tree shape có distribution tương tự randomized BST và expected height `O(log n)`.

Treap cho thấy randomization có thể được encode vào structure, không chỉ algorithm control flow.

Split/merge operations của treap còn làm nó hữu ích trong implicit sequence structures và randomized balanced-tree implementations.

## 15. Skip List

Skip List cũng dùng randomness để tạo multiple levels. Mỗi node được promote lên level cao hơn với probability nhất định, tạo các “express lanes”.

Expected search/insert/delete `O(log n)` với implementation tương đối đơn giản và concurrency-friendly variants.

Không có deterministic AVL-style rotation invariant; balance xuất hiện từ probabilistic distribution của heights.

## 16. Probabilistic Data Structures: đổi exactness lấy resource

Có workload mà answer exact quá đắt hoặc không cần thiết. Ví dụ muốn biết một URL “có thể đã thấy chưa” trên billions of items. Một HashSet exact có thể quá lớn.

Probabilistic structure dùng ít memory hơn bằng cách chấp nhận controlled error như false positive hoặc approximate count.

Điều bắt buộc là phải hiểu **error semantics**; “xác suất sai” không phải một con số chung mà có direction và parameter dependence cụ thể.

## 17. Bloom Filter

Bloom Filter có bit array size `m` và `k` hash functions.

Insert item set `k` bit positions thành 1. Query item tính cùng positions.

Nếu có ít nhất một bit 0, item **definitely not present**.

Nếu mọi bit 1, item **possibly present**.

Trong standard insert/query Bloom Filter không deletion, không có false negatives nếu implementation/hash model đúng. False positives có thể xảy ra vì bits được set bởi other items.

## 18. False Positive Probability của Bloom Filter

Sau insert `n` items với `k` hashes vào `m` bits, probability một bit vẫn 0 xấp xỉ:

\[
(1-1/m)^{kn} \approx e^{-kn/m}
\]

False positive probability xấp xỉ:

\[
p \approx (1-e^{-kn/m})^k
\]

Với `m` và `n` cố định, optimal `k` gần:

\[
k \approx \frac{m}{n}\ln 2
\]

Công thức này cho thấy error rate không magic; nó phụ thuộc bits-per-item và số hashes.

## 19. Bloom Filter trong hệ thống

LSM-tree database có thể dùng Bloom Filter cho mỗi SSTable. Nếu filter nói “definitely not present”, database tránh đọc table/disk block không cần thiết. Nếu “possibly present”, nó vẫn phải check storage thật.

Vì false positive chỉ gây extra work chứ không làm mất dữ liệu, Bloom Filter rất phù hợp như một **negative cache/filter**.

Đây là cách chọn probabilistic structure từ error direction phù hợp với system semantics.

## 20. Counting Bloom Filter và deletion

Standard Bloom Filter không thể clear một bit khi delete item vì bit đó có thể được item khác share.

Counting Bloom Filter thay bit bằng small counter. Insert increment counters; delete decrement. Query kiểm tra counters > 0.

Đổi lại memory lớn hơn và có risks như counter overflow nếu width quá nhỏ.

## 21. Count-Min Sketch

Count-Min Sketch dùng nhiều rows của counters với independent hash functions. Update item increment một counter mỗi row. Estimate frequency lấy minimum các counters tương ứng.

Collision chỉ làm estimate tăng, nên estimate là upper-biased trong standard model.

Memory phụ thuộc desired error/confidence, không phụ thuộc trực tiếp số distinct keys như exact HashMap.

Nó phù hợp streaming frequency, telemetry và heavy-hitter candidate generation.

## 22. HyperLogLog

HyperLogLog estimate cardinality — số distinct items — bằng việc quan sát patterns của hash values, đặc biệt vị trí leading zeros, rồi aggregate qua registers.

Nó cho estimate với small relative error dùng memory rất nhỏ so với exact set.

HLL rất phổ biến trong analytics vì distinct count exact trên billions keys có thể quá đắt.

## 23. Reservoir Sampling

Nếu stream length không biết trước và muốn giữ uniform random sample size `k`, reservoir sampling xử lý online với `O(k)` memory.

Sau khi giữ first k items, item thứ `i` được chọn vào reservoir với probability `k/i`; nếu chọn, nó thay một slot random.

Proof cho thấy sau mỗi step, mỗi item đã thấy có probability `k/i` nằm trong sample.

Đây là một randomized streaming algorithm nhưng output sample distribution, không phải approximate counter.

## 24. Approximation Algorithm khác Randomized Algorithm

**Approximation algorithm** chấp nhận solution không optimal nhưng có guarantee về quality, ví dụ within factor `α` của optimum. Nó có thể hoàn toàn deterministic.

**Randomized algorithm** dùng randomness nhưng có thể vẫn luôn trả exact answer.

Hai concepts độc lập. Một algorithm có thể deterministic approximation, randomized exact, randomized approximation hoặc deterministic exact.

Không nên gom tất cả dưới nhãn “probabilistic”.

## 25. Expected, High-probability và Worst-case Guarantees

Một expected bound nói giá trị trung bình theo randomness.

Một **with high probability** bound mạnh hơn theo hướng xác suất tail nhỏ, thường dạng failure probability giảm polynomial/exponential theo `n`.

Worst-case deterministic bound không phụ thuộc random outcomes.

Khi đọc paper/docs, phải nhìn loại guarantee. Hai algorithms cùng “O(n log n)” nhưng một cái expected, một cái worst-case có ý nghĩa khác trong adversarial/latency-sensitive context.

## 26. Chernoff/Concentration intuition

Probabilistic analysis thường không chỉ hỏi expectation mà còn hỏi probability lệch xa expectation.

Concentration bounds như Chernoff/Hoeffding cho biết tổng các random variables độc lập hoặc gần độc lập có probability tail giảm nhanh.

Không nhất thiết phải thuộc mọi công thức để dùng DSA, nhưng cần hiểu tại sao “expected tốt” chưa đủ; ta muốn biết distribution có tập trung quanh expected value hay có tail lớn.

## 27. Random seed và reproducibility

Randomized tests/algorithms trong engineering cần log seed khi debugging. Nếu bug chỉ xuất hiện ở một sequence random, không có seed thì rất khó reproduce.

Trong security contexts, seed còn có yêu cầu unpredictability khác với test reproducibility. Không nên dùng pseudo-random generator không phù hợp để bảo vệ adversarial hashing nếu threat model yêu cầu cryptographic unpredictability.

## 28. Monte Carlo error amplification

Nếu một Monte Carlo algorithm có independent failure probability `p < 1/2`, chạy nhiều lần và aggregate theo appropriate rule có thể giảm error exponentially.

Ví dụ repeated independent tests có thể đưa failure từ `p` xuống roughly `p^r` trong one-sided cases hoặc dùng majority voting trong two-sided settings.

Randomness cho phép trade runtime để mua confidence.

## 29. Khi nào nên dùng probabilistic structure?

Probabilistic structure phù hợp khi false positives/approximation không phá correctness cốt lõi, memory hoặc throughput là constraint lớn, và downstream system có cách verify khi cần.

Bloom Filter trước database lookup là safe vì “possibly present” vẫn được xác minh. Nhưng dùng Bloom Filter làm source-of-truth cho authorization là không phù hợp vì false positive có thể trở thành security bug.

Error semantics phải match product semantics.

## 30. Một mental checklist cho guarantee

Khi đọc một complexity statement, hãy hỏi:

Nó là worst-case, expected hay amortized? Expectation lấy trên input hay random choices? Có adversarial input không? Error là false positive, false negative hay additive/multiplicative approximation? Probability bound là per-query hay whole-run? Structure có rebuild/reset effects không?

Chỉ khi những qualifiers này rõ, guarantee mới có ý nghĩa engineering.

## Mental Model

> **Amortized** phân bổ cost trên một sequence. **Randomized** phân bổ behavior trên random choices. **Probabilistic structures** chủ động đổi exactness lấy space/time. Đây là ba kiểu trade-off khác nhau, không phải ba tên cho cùng một ý tưởng.

Học sâu các concept này giúp đọc complexity statements chính xác hơn và hiểu tại sao nhiều system thực tế chọn “expected”, “amortized” hoặc “approximately correct” thay vì deterministic exactness ở mọi operation.

Xem thêm: [Probabilistic Data Structures](./06_probabilistic_data_structures.md), [Skip Lists](../02_trees/07_skip_lists.md), [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [Testing & Benchmarking](../80_language_implementations/03_cross_language_testing_and_benchmarking.md).