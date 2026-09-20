# Probabilistic Data Structures cho dữ liệu lớn
**확률적 자료구조 / Probabilistic Data Structures**

Khi dữ liệu quá lớn để giữ exact state cho mọi item, requirement thực tế đôi khi không cần exact answer. Nếu product/system chấp nhận một **error model / 오류 모델** rõ ràng, ta có thể đổi một phần exactness lấy memory nhỏ hơn nhiều, mergeability tốt hơn và throughput cao hơn.

Probabilistic data structure không phải “phiên bản thiếu chính xác” của exact structure theo nghĩa mơ hồ. Một structure tốt phải nói rõ:

```text
query nào được hỗ trợ
loại lỗi nào có thể xảy ra
loại lỗi nào không xảy ra
error probability / magnitude phụ thuộc parameter nào
structure có merge được không
update/delete semantics là gì
```

Mental model trung tâm:

> Exact structure giữ đủ information để phân biệt mọi state cần thiết. Probabilistic structure cố ý nén nhiều histories vào cùng internal state và mô tả xác suất hoặc biên độ sai do sự nén đó gây ra.

## Khi nào approximation đáng giá?

Các workloads phổ biến:

```text
membership trước expensive disk lookup
ước lượng số user unique
frequency/heavy hitters trong event stream
sampling stream không biết trước length
network telemetry
large-scale analytics
cache/filter pipelines
```

Nếu answer dùng cho accounting, authorization hoặc correctness-critical transaction, approximate structure có thể sai abstraction. Error budget phải đến từ requirement, không phải từ sự tiện lợi của implementation.

## Bloom Filter

**Bloom Filter / 블룸 필터** trả lời approximate membership cho insertion-only set theo standard model.

Nó dùng bit array length `m` và `k` hash positions cho mỗi key.

Insert:

```text
for each hash position:
    bit[position] = 1
```

Query:

```text
nếu bất kỳ required bit = 0 -> chắc chắn không có
nếu mọi required bit = 1 -> có thể có
```

Standard Bloom Filter có **false positives** nhưng không có false negatives nếu không delete và implementation/hash consistent.

## Bloom Filter error derivation

Sau `n` inserts, tổng khoảng `kn` bit-setting events.

Probability một particular bit vẫn 0:

\[
\left(1-\frac1m\right)^{kn}
\approx e^{-kn/m}
\]

nên probability bit là 1 xấp xỉ:

\[
1-e^{-kn/m}
\]

Một key chưa insert bị false positive nếu cả `k` positions của nó đều đã 1:

\[
p \approx \left(1-e^{-kn/m}\right)^k
\]

Formula này cho thấy parameter trade-off. Tăng `k` ban đầu giảm collision chance của query, nhưng set nhiều bits hơn và tăng CPU cost; quá nhiều hashes làm filter saturated nhanh hơn.

## Optimal k intuition

Với `m` và expected `n` cố định, optimal number hashes gần:

\[
k \approx \frac mn \ln 2
\]

Khi đó roughly half bits set trong idealized model.

Không cần memorize formula để dùng mọi lúc, nhưng phải biết filter cần parameterization theo **expected cardinality và target false-positive rate**, không phải chọn arbitrary bit size.

## Sizing từ error budget

Nếu target false-positive probability `p` và expected inserts `n`, required bits scale roughly:

\[
m \approx -\frac{n\ln p}{(\ln 2)^2}
\]

Điều quan trọng: filter size tuyến tính theo expected inserted count cho fixed error target, nhưng constant bits/item nhỏ hơn exact hash set rất nhiều vì filter không giữ keys.

## Bloom Filter không thể trả keys

Vì chỉ giữ bit evidence, ta không thể iterate inserted items hoặc reconstruct original set. Nó chỉ là membership filter.

Nếu application sau này cần list members, Bloom Filter không thể thay exact structure; nó chỉ đứng trước exact storage như prefilter.

## Bloom Filter trước disk/database lookup

Một classic pipeline:

```text
query key
  ↓
Bloom Filter
  ↓ nếu definitely absent: stop
  ↓ nếu maybe present:
exact index / disk / SSTable / database
```

False positive chỉ gây extra expensive lookup. Không false negative nghĩa filter không bỏ mất item thật.

Đây là use case lý tưởng vì error type chỉ ảnh hưởng performance, không correctness final.

## Counting Bloom Filter

Standard Bloom Filter khó delete vì clearing một bit có thể xóa evidence của nhiều keys.

Counting Bloom Filter dùng small counters thay bits. Insert increment, delete decrement.

Nhưng deletion chỉ safe nếu application đảm bảo key đang logically present đúng multiplicity. Decrement sai có thể tạo false negatives.

Counters tăng memory đáng kể và có overflow/saturation considerations.

## Stable/scalable Bloom variants

Nếu stream không bounded, fixed Bloom Filter eventually saturates. Variants như scalable Bloom filters add new filters as capacity grows; stable Bloom filters intentionally decay information cho streaming recency scenarios.

Mỗi variant đổi error semantics. Không nên gọi chung “Bloom Filter” rồi assume standard guarantees.

## Cuckoo Filter intuition

Cuckoo Filter lưu compact fingerprints trong buckets và hỗ trợ deletion natural hơn Bloom Filter. Lookup false positives do fingerprint collisions.

Insertion có thể relocate fingerprints như cuckoo hashing.

Trade-off khác về load factor, deletion và small-set performance. Khi requirement cần approximate membership + deletion, Cuckoo Filter là một candidate đáng biết.

## XOR Filter intuition

Static approximate membership filters như XOR filters có thể đạt lookup nhanh/memory compact sau build, nhưng dynamic insertion semantics khác Bloom Filter.

Lesson quan trọng: static vs dynamic workload mở ra different probabilistic structures.

## Count-Min Sketch

**Count-Min Sketch (CMS / 카운트-민 스케치)** ước lượng frequency của keys trong stream.

Structure có `d` rows, mỗi row width `w`; mỗi row dùng hash function riêng.

Update key `x` by `c`:

```text
counter[row][hash_row(x)] += c
```

Query estimate:

```text
min over rows of corresponding counters
```

Trong standard non-negative frequency model, collisions chỉ thêm counts của keys khác, nên estimate không nhỏ hơn true count.

## Vì sao lấy minimum?

Mỗi row estimate:

\[
trueCount(x)+collisionNoise
\]

Noise không âm. Minimum cố chọn row ít polluted nhất.

Average sẽ giữ more collision noise; minimum phù hợp one-sided error model.

## Width và depth

Typical theoretical parameterization:

```text
width controls additive error magnitude
depth controls failure probability/confidence
```

Roughly, width `O(1/ε)` và depth `O(log 1/δ)` cho guarantee dạng estimate không vượt true count + `ε * totalMass` với probability cao, dưới assumptions standard.

Không nên nhớ constants mà quên semantics: error relative to total stream mass, không necessarily relative error per rare item.

## Conservative update

Một CMS variant chỉ increment counters đang ở current minimum estimate thay vì tất cả rows, giúp giảm overestimation practical trong some workloads.

Guarantee/semantics cần đọc đúng variant; optimization không tự preserve mọi theoretical property textbook.

## Heavy hitters

Count-Min Sketch có thể combine với heap/candidate set để tìm approximate frequent items.

Sketch alone query cần key known. Nếu muốn discover heavy hitters without enumerating all keys, cần candidate-generation mechanism khác.

Đây là recurring principle: summary may answer query for given key nhưng không necessarily recover key identities.

## Signed updates caveat

Standard one-sided CMS reasoning dựa non-negative updates. Nếu stream có negative updates/deletions, counters/noise semantics đổi và cần strict-turnstile/general-turnstile variants/assumptions.

Error guarantee luôn gắn update model.

## HyperLogLog

**HyperLogLog (HLL / 하이퍼로그로그)** ước lượng cardinality — số distinct values — bằng memory gần constant theo stream size cho fixed precision.

Exact distinct count cần giữ set all unique items hoặc external exact structure. HLL chỉ giữ statistical evidence từ hashes.

## Leading-zero intuition

Uniform random bitstring bắt đầu bằng `r` zero liên tiếp với probability giảm exponentially.

Nếu thấy một hash có rất nhiều leading zeros, điều đó gợi ý đã sample nhiều distinct hashes.

Một naive estimator từ maximum leading-zero count có variance lớn. HyperLogLog chia hashes vào nhiều registers và aggregate observations để ổn định estimate.

## HLL registers

Hash được split conceptually thành:

```text
bucket/register index bits
remaining bits dùng để đo rank/leading-zero position
```

Mỗi register giữ max observed rank cho items mapped tới nó.

Final estimate dùng harmonic-style aggregation + corrections tùy algorithm/version.

Memory chỉ là số registers * bits/register, không tăng theo distinct cardinality until representational limits.

## Precision parameter

Nếu có `m` registers, relative standard error classic approximation thường scale khoảng:

\[
O(1/\sqrt m)
\]

Nhiều registers -> more memory, lower error.

Đây là clear error-memory knob.

## Small-cardinality correction

Khi cardinality nhỏ, raw HLL estimator có bias/variance behavior khác. Implementations thường dùng linear-counting-like corrections hoặc empirically tuned schemes.

Production accuracy phụ thuộc exact HLL/HLL++ variant, hash width và bias correction, nên đừng tự implement primitive estimator rồi assume library-grade guarantees.

## Mergeability của HLL

Hai HLL cùng configuration có thể merge register-wise bằng max:

```text
merged[i] = max(A[i], B[i])
```

vì each register stores maximum evidence seen in either stream.

Đây là lý do HLL rất mạnh trong distributed analytics: each worker summarizes partition, coordinator merges compact states.

## Union dễ, intersection khó hơn

HLL merge tự nhiên estimate union cardinality. Intersection có thể derive via inclusion-exclusion:

\[
|A\cap B|=|A|+|B|-|A\cup B|
\]

nhưng error có thể amplify khi subtract large noisy estimates. Specialized sketches may be better for set similarity/intersection.

Approximate algebra cần propagate error, không chỉ apply exact formula.

## Reservoir Sampling

Nếu stream length không biết trước và muốn sample `k` items uniformly without storing all items, **Reservoir Sampling / 저수지 샘플링** giữ reservoir size `k`.

Với item thứ `i` (`i` 1-based), nếu `i<=k` thì fill reservoir. Sau đó chọn item với probability `k/i`; nếu chọn, replace random reservoir slot.

Memory `O(k)` independent of stream length.

## Uniformity proof cho k=1

Item ở position `j` được chọn lúc đến với probability `1/j`. Để còn sample cuối stream length `n`, nó phải survive steps `j+1...n`:

\[
\frac1j\cdot\frac{j}{j+1}\cdot\frac{j+1}{j+2}\cdots\frac{n-1}{n}=\frac1n
\]

nên mỗi item có equal probability `1/n`.

General reservoir size `k` cho probability inclusion `k/n` mỗi item.

## Weighted reservoir sampling

Nếu items có weights và muốn probability proportional to weight, standard uniform reservoir không đủ. Có weighted reservoir algorithms dùng random keys/priorities.

Again, “sampling” semantics phải precise: uniform over items, over events, over weight hay over distinct keys?

## Sampling with replacement vs without replacement

Reservoir sampling classic size `k` là sample without replacement từ stream positions.

Nếu requirement cần independent samples with replacement, algorithm khác.

Statistics downstream phụ thuộc sampling design.

## Bottom-k / KMV sketches

Một elegant distinct-count/set-summary idea: hash every distinct key uniformly to `[0,1)`, giữ `k` smallest hash values.

Threshold of k-th smallest chứa cardinality information; union sketches dễ merge bằng taking k smallest from combined sets.

KMV/bottom-k còn hỗ trợ approximate set similarity/intersection better than HLL in some workloads.

Conceptually, this is order statistics over random hashes.

## MinHash

**MinHash** estimate Jaccard similarity:

\[
J(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

For random permutation/hash, probability two sets có same minimum hash equals Jaccard similarity under idealized assumptions.

Multiple independent hashes/signature components reduce variance.

Use cases: near-duplicate detection, document similarity, set similarity search.

## Locality-Sensitive Hashing connection

LSH uses hash families designed so similar items collide with higher probability than dissimilar items. Nó khác ordinary hash table hash, nơi goal thường uniform distribution independent of semantic similarity.

MinHash signatures can feed LSH for approximate nearest-neighbor-like set similarity search.

Same word “hash” nhưng objective khác hoàn toàn.

## Quotient/compact filters intuition

Compact approximate membership structures exploit fingerprints/remainders and packed layouts for cache efficiency. Exact details vary, but design space repeatedly trades:

```text
bits per key
false-positive rate
build/update support
delete support
lookup locality
mergeability
```

Probabilistic data structures nên được chọn bằng requirement matrix, không theo popularity.

## Morris approximate counter intuition

Ngay cả một single integer count có thể được approximated probabilistically với logarithmic-scale state. Morris counter increments stored exponent-like value probabilistically, representing counts over large range with few bits at cost of variance.

Không phải common application primitive today, nhưng nó minh họa cực đoan idea “trade exact count for tiny memory”.

## Error types cần phân biệt

Approximate structures có thể có:

```text
false positive
false negative
one-sided overestimate
one-sided underestimate
unbiased noisy estimate
relative error
additive error
probabilistic confidence failure
```

Không được nói chung “có sai số khoảng 1%” nếu không định nghĩa 1% của cái gì và confidence bao nhiêu.

## Relative vs additive error

Suppose true count is 10.

Additive error `±100` useless dù total stream huge. Relative error 1% would be `±0.1` idealized.

Count-Min Sketch typical guarantee additive relative to total mass, nên rare-key relative error có thể rất lớn.

HyperLogLog targets relative cardinality error more naturally.

Query requirement quyết định error metric.

## Confidence parameter

Một guarantee dạng:

```text
error <= ε with probability >= 1-δ
```

có hai knobs: error magnitude `ε` và failure probability `δ`.

Reducing both usually costs more memory/CPU. Product requirement nên translate thành `ε,δ` thay vì “accuracy cao”.

## Hash independence assumptions

Theoretical proofs có thể assume fully independent hashes, trong khi real implementations dùng practical hash functions/seeds.

Pairwise/k-wise independence may suffice for some bounds. Production library design balances theoretical assumptions, speed và attack resistance.

Không nên extrapolate theorem nếu hash behavior/data adversarial không match assumptions.

## Hash width và collision floor

Nếu using 64-bit hash for enormous cardinalities, raw hash collisions themselves become non-zero. Birthday bound says collision probability grows around square root of hash space.

For standard scales 64-bit may be adequate, but high-integrity/huge systems need reason about hash width.

Approximate structure error is not the only possible collision source.

## Distributed mergeability

Mergeable sketches are algebraically attractive because workers can summarize data independently.

Examples:

```text
HLL: register-wise max
CMS with same layout/seeds: counter-wise addition
Bloom filters same config: bitwise OR for union-membership approximation
bottom-k: keep k smallest combined hashes
```

But merge requires same compatible parameters/hash seeds. Combining incompatible sketches silently invalidates guarantees.

## Monoid-like aggregation

Many mergeable sketches have associative merge + identity empty sketch, making them natural distributed aggregation states.

This resembles monoid-based reasoning in segment trees, but operation semantics include probabilistic error.

Associativity enables tree reductions, parallel aggregation and streaming checkpoints.

## Serialization/versioning

Production sketch stored or sent over network needs metadata:

```text
algorithm/version
precision parameters
hash seed/function id
counter width
endianness/encoding
```

Merging states from incompatible versions/configurations can produce nonsense.

Approximate structure is still a data format with schema evolution concerns.

## Saturation

Fixed-size counters/registers may saturate.

Counting Bloom counters can overflow. CMS fixed counters can overflow on long streams. HLL rank storage has finite max. Production implementation chooses counter width, saturation behavior or epoch/windowing.

Overflow can destroy theoretical guarantees if ignored.

## Time windows

Many streams ask “last 5 minutes” rather than all-time.

Sketches that only support monotonic addition cannot simply forget old events. Solutions may use rotating windows, exponential histograms, per-bucket sketches or structures with deletion support.

Time-decay requirement fundamentally changes design.

## Sliding-window approximate counting

A simple system approach: keep one sketch per time bucket and merge buckets covering current window. Trade-off:

```text
more buckets -> finer expiration accuracy + more memory/merge work
fewer buckets -> coarser boundaries
```

Advanced streaming algorithms give stronger bounds, but bucketization already shows temporal state must be modeled explicitly.

## Cardinality under privacy constraints

Approximate aggregate sketches do not automatically provide privacy. HLL/MinHash state can leak information under some threat models. Differential privacy adds noise/analysis distinct from sketch error.

Approximation and privacy are separate concepts.

## Adversarial inputs

If attacker can infer hash seeds or exploit deterministic weak hash, Bloom/CMS guarantees may degrade or be manipulated.

Security-sensitive deployments may rotate/secret seeds or use robust hashing, with performance cost.

Error model should include threat model when untrusted inputs exist.

## Probabilistic structure vs cache

Bloom Filter answers membership approximation; cache stores actual values for subset keys. Combining:

```text
Bloom says definitely absent -> skip cache/backend lookup path
maybe present -> cache/backend check
```

But a Bloom Filter itself cannot return value.

Different structures solve different query classes even if all reduce work.

## Bloom + LSM Tree

LSM storage levels/SSTables can each have Bloom Filter. Point lookup checks filters to skip files definitely lacking key.

False positives cause extra file checks; no false negatives preserve correctness.

This is a canonical systems connection because filter error maps directly to I/O overhead.

## CMS in telemetry

Network flow IDs/cardinality too large for exact per-key map. CMS can estimate frequency with fixed memory. Heavy-hitter candidate mechanism surfaces likely elephants for further exact monitoring.

This tiered design — approximate broad scan + exact small candidate set — is a common production pattern.

## HLL in analytics databases

`APPROX_COUNT_DISTINCT`-style operations can use HLL-family sketches to reduce memory/shuffle. Partial aggregations on workers merge centrally.

Exact `COUNT(DISTINCT)` may require large hash sets/sorts and network transfer; approximate cardinality offers predictable compact state.

Again, correct choice depends business accuracy requirement.

## MinHash for duplicate detection

Documents can be represented by shingles/sets. Exact Jaccard all-pairs is expensive. MinHash signatures compress set similarity; LSH groups likely similar documents; exact comparison can verify candidates.

Pipeline:

```text
raw set
 -> MinHash signature
 -> LSH candidate generation
 -> exact/expensive verification
```

Probabilistic structure often works best as a **filtering stage**, not final authority.

## Parameter selection should be capacity planning

Do not hard-code sketch parameters without expected scale.

For Bloom Filter, need expected `n`, desired `p`.

For HLL, choose register count from target relative error/memory.

For CMS, choose width/depth from additive error/confidence.

Then monitor actual cardinality/stream mass. If reality exceeds design assumptions, error can become much worse.

## Monitoring sketch health

Production metrics may include:

```text
Bloom bit occupancy / estimated saturation
insert count vs design capacity
CMS counter saturation
HLL precision/version
merge incompatibility errors
observed false-positive sample rate
```

Approximate structures need operational observability like any subsystem.

## Validation by simulation

Because error is statistical, tests should simulate many randomized datasets and compare empirical error distribution with expected envelope.

One dataset passing does not validate probability guarantee.

For Bloom Filter:

```text
insert known set
verify zero false negatives
query large known-absent sample
measure false positive rate
```

For HLL/CMS, run across cardinalities/distributions including skew.

## Differential testing

Small exact reference structures provide ground truth:

```text
HashSet for membership/cardinality
HashMap for counts
stored stream for sample inclusion checks
```

Probabilistic result is compared statistically, not exact-value equal except properties like no false negatives where guaranteed.

## Random seed reproducibility

Tests should often fix/inject seeds để reproduce failure. Production can choose random seeds per process/table for security/distribution.

Deterministic tests and randomized deployment are compatible concerns.

## Benchmarking

Measure more than throughput:

```text
bytes per key / fixed sketch bytes
query/update latency
merge cost
cache behavior
hash computation cost
error distribution
serialization size
```

A sketch with slightly lower theoretical error may be worse if hash cost or memory layout dominates workload.

## When exact structure is better

If cardinality moderate and memory available, exact `HashSet`/`HashMap` often simpler, debuggable and supports iteration/deletion naturally.

Approximation introduces operational complexity and error reasoning. Do not use sketches just because data is “big” without quantifying benefit.

## Choosing among common structures

| Question | Candidate |
|---|---|
| “Key chắc chắn không tồn tại?” | Bloom/Cuckoo/XOR filter family |
| “Key này xuất hiện khoảng bao nhiêu lần?” | Count-Min Sketch |
| “Có khoảng bao nhiêu distinct keys?” | HyperLogLog |
| “Lấy k samples uniform từ stream?” | Reservoir Sampling |
| “Hai sets giống nhau khoảng bao nhiêu?” | MinHash / bottom-k |
| “Need exact iteration/value retrieval?” | probabilistic structure alone không đủ |

Table chỉ là orientation; exact variant phải match update/error model.

## Common misconceptions

“Bloom Filter nói present nghĩa key có thật” — sai, chỉ maybe present.

“Bloom Filter support delete bằng clear bits” — sai cho standard filter vì shared bits.

“CMS error là ±x” — standard model thường one-sided overestimate.

“HLL cho exact distinct khi cardinality nhỏ” — implementation có corrections nhưng vẫn là approximate structure unless library explicitly switches exact representation.

“Randomized structure error tự biến mất khi data lớn” — không; parameter/error model quyết định.

“Merge sketches bất kỳ” — sai; configuration/hash compatibility bắt buộc.

“Approximate = không đáng tin” — sai; properly parameterized probabilistic guarantee có thể rất strong và operationally better than exact state impossible to maintain.

## Mental Model

> Probabilistic data structures không cố giữ data; chúng giữ **evidence**. Bloom Filter giữ evidence membership trong bits, CMS giữ noisy count evidence, HLL giữ rare hash-pattern evidence về cardinality, reservoir giữ representative sample. Memory nhỏ vì many distinct histories intentionally collapse into the same summary state.

Khi chọn một probabilistic structure, hãy hỏi: **error nào được phép, error metric là additive hay relative, confidence bao nhiêu, stream/update model là gì, cần merge/delete/window không, hash assumptions có hợp threat model không, và approximation sẽ ảnh hưởng correctness hay chỉ performance?**

Xem tiếp: [Hash Tables](../01_linear_structures/04_hash_tables.md), [Amortized & Randomized Thinking](./03_amortized_randomized_and_probabilistic_thinking.md), [Bitsets](./02_bit_manipulation_and_bitsets.md), [DSA in Systems](../90_connections/01_dsa_in_databases_networks_and_systems.md) và [Mathematical Toolkit](../00_foundations/04_mathematical_toolkit_for_dsa.md).
