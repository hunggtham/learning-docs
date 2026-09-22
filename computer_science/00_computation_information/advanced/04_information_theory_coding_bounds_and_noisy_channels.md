# Information theory, coding bounds và noisy channels

Một communication system phải trả lời hai câu hỏi khác nhau nhưng liên quan chặt chẽ: **có thể biểu diễn nguồn dữ liệu ngắn tới mức nào mà vẫn khôi phục được**, và **có thể truyền dữ liệu đáng tin cậy qua một kênh có nhiễu với tốc độ tới đâu**.

**Information theory (lý thuyết thông tin / 정보 이론)** của Shannon cung cấp ngôn ngữ toán học để reasoning về uncertainty, compression và communication limits mà không cần biết nội dung semantic của message là ảnh, text hay packet database.

Mental model:

```text
source distribution
→ uncertainty / entropy
→ source coding
→ bits sent or stored
→ noisy channel
→ redundancy / error-control coding
→ recovered symbols
```

Chapter này tập trung vào invariant và giới hạn: khi nào có thể nén, redundancy nào là cần thiết, error nào có thể sửa và tại sao “nhiều bandwidth hơn” không tự động đồng nghĩa “nhiều reliable information hơn”.

## 1. Information bắt đầu từ surprise

Một event chắc chắn xảy ra không mang nhiều thông tin mới. Một event rất hiếm khi xảy ra mang nhiều surprise hơn khi ta quan sát nó.

Self-information thường được mô tả:

```text
I(x) = -log2 P(x)
```

Nếu `P(x)=1`, information là 0 bit. Nếu `P(x)=1/2`, event mang 1 bit surprise. Nếu `P(x)=1/1024`, event mang 10 bit.

Logarithm xuất hiện vì ta muốn information của hai independent events cộng được:

```text
P(x,y) = P(x)P(y)
⇒ I(x,y) = I(x) + I(y)
```

Đây là property phù hợp với cách description length cộng qua các lựa chọn độc lập.

## 2. Entropy là uncertainty trung bình của distribution

Với random variable `X`, Shannon entropy:

```text
H(X) = - Σ p(x) log2 p(x)
```

Entropy không phải “độ hỗn loạn” theo nghĩa mơ hồ. Nó là expected self-information nếu sample từ distribution.

Một fair coin có:

```text
H(X) = 1 bit
```

Một coin có xác suất head `0.999` có entropy thấp hơn nhiều vì outcome gần như dự đoán được.

Nếu source phát symbol theo distribution lệch, ta có cơ hội dùng code ngắn cho symbol phổ biến và code dài cho symbol hiếm để giảm expected length.

## 3. Joint, conditional entropy và mutual information

Hệ thống thực tế có nhiều variable liên quan. Nếu biết `Y` giúp dự đoán `X`, uncertainty còn lại của `X` giảm.

**Conditional entropy**:

```text
H(X|Y)
```

đo uncertainty còn lại về `X` sau khi biết `Y`.

**Mutual information**:

```text
I(X;Y) = H(X) - H(X|Y)
```

đo lượng information về `X` mà `Y` cung cấp.

Mental model:

```text
H(X)      = uncertainty ban đầu
H(X|Y)    = uncertainty còn lại sau khi biết Y
I(X;Y)    = phần uncertainty đã được Y giải thích
```

Mutual information quan trọng trong feature selection, communication và representation learning, nhưng không tự động chứng minh causal relation. Hai variable có thể chia sẻ information vì cùng phụ thuộc một nguyên nhân khác.

## 4. Source coding: entropy là lower-bound trung bình, không phải file size thần kỳ

Source coding theorem nói theo trực giác rằng với source có distribution ổn định và block đủ dài, lossless code có expected bits/symbol tiến gần entropy, nhưng không thể trung bình thấp hơn entropy một cách tùy ý mà vẫn decode chính xác.

Điều này không có nghĩa mọi message cụ thể dài đúng `H(X)`. Entropy là expectation trên distribution.

Ví dụ alphabet:

```text
A: 1/2
B: 1/4
C: 1/8
D: 1/8
```

Một prefix code hợp lý có thể dùng độ dài gần:

```text
A → 1 bit
B → 2 bits
C → 3 bits
D → 3 bits
```

Symbol phổ biến nhận code ngắn hơn.

## 5. Prefix code và Kraft inequality

Nếu codeword phải decode nối tiếp mà không cần delimiter, một codeword không được là prefix của codeword khác.

Ví dụ hợp lệ:

```text
A = 0
B = 10
C = 110
D = 111
```

Kraft inequality mô tả constraint giữa các code length `l_i` cho prefix code:

```text
Σ 2^(-l_i) ≤ 1
```

Nó cho thấy code length không thể tùy ý ngắn cho mọi symbol. Cây nhị phân có “capacity” hữu hạn cho leaf codeword.

**Huffman coding** tìm prefix code tối ưu theo expected length trong class code symbol-by-symbol với probability đã biết. **Arithmetic/range coding** có thể biểu diễn cả sequence theo interval và tiến gần entropy hơn khi probability không khớp đẹp với integer bit lengths.

## 6. Compression khai thác dependency chứ không chỉ frequency đơn symbol

Nếu source có correlation theo thời gian, entropy mỗi symbol riêng lẻ có thể cao nhưng conditional entropy thấp.

Ví dụ text: ký tự tiếp theo phụ thuộc context. `q` trong tiếng Anh thường làm `u` dễ dự đoán hơn. Video frame kế tiếp tương quan mạnh với frame trước. Log line kế tiếp thường dùng lại template.

Một compressor tốt vì vậy model:

```text
P(next_symbol | context)
```

thay vì chỉ `P(symbol)`.

Đây là bridge tới language modeling: predictive model tốt giảm uncertainty của next token. Tuy nhiên cross-entropy/perplexity của model và semantic understanding không phải cùng một khái niệm.

## 7. Cross-entropy và coding regret

Nếu true distribution là `P` nhưng ta encode bằng model `Q`, expected code length liên quan tới **cross-entropy**:

```text
H(P,Q) = - E_P[log2 Q(x)]
```

Khoảng chênh so với entropy thật được mô tả bởi KL divergence:

```text
H(P,Q) = H(P) + D_KL(P || Q)
```

Trực giác production rất hữu ích:

```text
true uncertainty
+ model mismatch penalty
= expected coding cost under model
```

Model probability tệ không chỉ là “dự đoán kém”; nếu dùng cho entropy coding, nó tạo thêm bit thật.

## 8. Noisy channel: transmission có thể làm bit thay đổi hoặc biến mất

Trong communication, channel có thể flip bit, erase symbol, reorder packet hoặc tạo burst loss tùy layer.

Information theory abstraction tách source khỏi channel. Ta hỏi: với channel transition probability cụ thể, tốc độ reliable information tối đa là bao nhiêu?

**Channel capacity** là supremum của mutual information giữa input và output trên input distribution phù hợp:

```text
C = max I(X;Y)
```

Không cần thuộc công thức cho mọi channel; cần giữ mental model: capacity phụ thuộc cả signal choices lẫn noise behavior.

## 9. Noisy-channel coding theorem: reliable không có nghĩa zero-noise

Một kết quả sâu của Shannon là nếu transmission rate nhỏ hơn channel capacity, tồn tại coding scheme cho phép error probability giảm rất thấp khi block length tăng đủ. Nếu rate vượt capacity, không thể làm reliable arbitrarily chỉ bằng coding thông minh.

Điểm quan trọng:

```text
noise tồn tại
≠ communication đáng tin cậy là bất khả thi
```

Ta thêm structured redundancy để decoder phân biệt codeword ngay cả khi một phần tín hiệu bị corruption.

Nhưng redundancy dùng bandwidth/storage. Reliability luôn có cost.

## 10. Error detection và error correction khác nhau

Checksum/CRC thường mạnh ở **phát hiện** corruption nhưng không nhất thiết đủ để sửa. Error-correcting code thêm redundancy có structure để xác định codeword gần nhất.

Một khái niệm nền là **Hamming distance**: số vị trí khác nhau giữa hai codeword.

Nếu minimum distance giữa codeword là `d`, trực giác:

- phát hiện được tới `d-1` bit error trong model tương ứng;
- sửa được khoảng `floor((d-1)/2)` bit error bằng nearest-codeword reasoning.

Đây là geometric view: codeword phải đủ xa nhau để noise nhỏ không đẩy received word sang vùng của codeword khác.

## 11. Erasure dễ hơn unknown corruption

Nếu receiver biết vị trí symbol bị mất, đó là **erasure**. Nếu receiver nhận một symbol sai mà không biết vị trí nào sai, đó là **error**.

Erasure thường dễ sửa hơn vì uncertainty nhỏ hơn. Storage/distributed systems tận dụng điều này: nếu biết shard/node nào mất, erasure coding có thể reconstruct từ các fragment còn lại với storage overhead thấp hơn full replication trong một số workload.

Nhưng erasure coding thêm CPU, network fan-out, repair traffic và failure-domain reasoning. Không nên kết luận “erasure coding luôn rẻ hơn replication” chỉ từ raw storage ratio.

## 12. Burst error và interleaving

Nhiều physical channel không tạo independent random bit flip; lỗi đến theo burst. Nếu một block code chịu được vài error nhưng cả burst rơi vào cùng block, correction có thể thất bại.

**Interleaving** phân tán các symbol liên tiếp của codeword qua thời gian/không gian để một burst physical trở thành các error thưa hơn ở nhiều codeword.

Trade-off là latency và buffer tăng. Đây là ví dụ điển hình của việc thay đổi representation để biến failure pattern thành dạng code xử lý tốt hơn.

## 13. Capacity không đồng nghĩa throughput application

Physical/link capacity chỉ là một tầng. Application throughput còn bị giảm bởi framing, retransmission, congestion control, encryption, protocol headers, queueing và request semantics.

```text
channel capacity
→ link goodput
→ transport goodput
→ application useful throughput
```

Nếu packet loss tăng, transport có thể giảm sending rate dù raw link bandwidth không đổi. Nếu data đã compressed mạnh, thêm compression CPU có thể làm throughput application xấu hơn.

Do đó khi debugging cần xác định layer nào sở hữu “rate” đang nói tới.

## 14. Entropy không đo semantic value

Một encrypted backup có entropy quan sát rất cao nhưng semantic value có thể cực lớn. Một random file cũng có entropy cao nhưng không hữu ích. Một configuration file rất compressible nhưng có thể quyết định toàn bộ production behavior.

Information theory cố ý bỏ qua semantic meaning để có theorem tổng quát về coding và communication.

Đừng dùng “entropy cao” như synonym của “thông tin quan trọng”.

## 15. Entropy rate và source có memory

Với process có dependency dài, ta quan tâm uncertainty mới trung bình mỗi symbol khi biết quá khứ:

```text
H_rate ≈ lim H(X_n | X_1 ... X_{n-1})
```

Nếu sequence rất predictable từ history, entropy rate thấp dù marginal distribution từng symbol có thể trông cân bằng.

Connection này giải thích tại sao dictionary/context compressor có thể nén sequence mà frequency histogram đơn giản không cho thấy lợi ích.

## 16. Production evidence cho storage/network coding

Khi một system dùng compression hoặc error-control coding, evidence nên phân biệt:

```text
logical bytes
encoded/compressed bytes
wire/storage bytes
error/erasure rate
retry/reconstruction rate
CPU encode/decode cost
latency distribution
repair traffic
failure-domain correlation
```

Nếu compression ratio tốt nhưng CPU saturation làm queue tăng, end-to-end system có thể tệ hơn. Nếu erasure coding tiết kiệm storage nhưng repair storm bão hòa network sau rack failure, cost model ban đầu thiếu failure behavior.

## 17. Connection với database và distributed systems

Database columnar encoding dùng distribution/locality để giảm bytes và memory bandwidth. Bloom filter chấp nhận false positive để giảm I/O. Replicated log dùng checksum để phát hiện corruption. Distributed storage có thể dùng replication hoặc erasure coding để đổi storage overhead lấy recovery/network complexity.

Đọc thêm:

- [Columnar storage, encoding, pruning và vectorized scans](../../05_data_databases/advanced/08_columnar_storage_encoding_pruning_and_vectorized_scans.md)
- [Multi-region replication và geo-distributed trade-offs](../../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md)
- [Durability path application → WAL → filesystem → device](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md)

## 18. Connection với machine learning

Cross-entropy loss có interpretation coding: model gán probability cao cho observed outcome sẽ cần ít surprise bits hơn. Perplexity thường là exponent của average negative log probability theo base phù hợp.

Nhưng production model quality không chỉ là cross-entropy. Calibration, task utility, distribution shift, latency và safety vẫn là contract riêng.

Information-theoretic metric cho biết model probability phù hợp data tới đâu, không tự động cho biết decision downstream đúng hay có giá trị.

## 19. Những nhầm lẫn thường gặp

**“Entropy là randomness của một file cụ thể.”** Shannon entropy cần distribution/random variable. Với object cụ thể, algorithmic complexity là viewpoint khác.

**“Nén tới entropy nghĩa là mọi file đều có size H.”** Không. Bound là expected/asymptotic theo source model.

**“Checksum sửa được lỗi.”** Checksum chủ yếu detect; correction cần redundancy có structure phù hợp.

**“Bandwidth 1 Gbps nghĩa app gửi được 1 Gbps payload.”** Không. Phải trừ protocol overhead và behavior do loss/congestion/CPU.

**“Thêm redundancy luôn làm reliability tốt hơn.”** Chỉ nếu code/failure model phù hợp; correlated failures có thể phá assumption.

**“Mutual information cao nghĩa X gây ra Y.”** Không. Dependency không đồng nghĩa causality.

## 20. Checklist reasoning

```text
Source distribution là gì và có ổn định không?
Entropy đang nói về marginal hay conditional uncertainty?
Codec model dependency nào?
Lossless hay lossy contract?
Channel failure là random error, erasure hay burst/correlated?
Ta cần detect hay correct?
Redundancy tiêu tốn bandwidth/storage/latency bao nhiêu?
Rate đang đo ở physical, transport hay application layer?
Evidence nào cho thấy bottleneck là information limit thay vì implementation limit?
```

## Kết luận

Information theory cung cấp hai giới hạn nền tảng: **source uncertainty giới hạn mức lossless compression trung bình**, và **channel capacity giới hạn tốc độ reliable communication qua noise**. Coding không xóa giới hạn vật lý; nó tổ chức representation và redundancy để tiến gần giới hạn đó.

Mental model cần giữ:

```text
probability
→ surprise
→ entropy
→ code length

noise
→ uncertainty at receiver
→ structured redundancy
→ detection/correction
→ reliable information rate
```

Từ file compression, database encoding, network transport, storage repair tới cross-entropy trong machine learning, cùng một câu hỏi lặp lại: **uncertainty nằm ở đâu, representation nào đang khai thác structure, và redundancy nào đang được trả để giữ invariant?**