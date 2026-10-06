# Thông tin (information / 정보) lý thuyết (theory / 이론), coding bounds và noisy channels

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thông tin (information / 정보) lý thuyết (theory / 이론), coding bounds và noisy channels**. Route đi từ surprise/entropy → mutual information và channel capacity → source/channel coding bounds → noisy transmission và decoding, để giới hạn lý thuyết quay về thiết kế truyền tin cụ thể.

Một communication hệ thống (system / 시스템) phải trả lời hai câu hỏi khác nhau nhưng liên quan chặt chẽ: **có thể biểu diễn nguồn dữ liệu ngắn tới mức nào mà vẫn khôi phục được**, và **có thể truyền dữ liệu đáng tin cậy qua một kênh có nhiễu với tốc độ tới đâu**.

**thông tin (information / 정보) lý thuyết (theory / 이론)** của Shannon cung cấp ngôn ngữ toán học để lập luận (reasoning / 추론) về bất định (uncertainty / 불확실성), compression và communication limits mà không cần biết nội dung ngữ nghĩa (semantic / 의미적) của message là ảnh, văn bản (text / 텍스트) hay packet cơ sở dữ liệu (database / 데이터베이스).

Mô hình tư duy (mental model / 사고 모델):

```text
source distribution
→ uncertainty / entropy
→ source coding
→ bits sent or stored
→ noisy channel
→ redundancy / error-control coding
→ recovered symbols
```

Chapter này tập trung vào bất biến (invariant / 불변식) và giới hạn: khi nào có thể nén, redundancy nào là cần thiết, lỗi (error / 오류) nào có thể sửa và tại sao “nhiều bandwidth hơn” không tự động đồng nghĩa “nhiều reliable thông tin (information / 정보) hơn”.

## 1. thông tin (information / 정보) bắt đầu từ surprise

Một sự kiện (event / 이벤트) chắc chắn xảy ra không mang nhiều thông tin mới. Một sự kiện (event / 이벤트) rất hiếm khi xảy ra mang nhiều surprise hơn khi ta quan sát nó.

Self-information thường được mô tả:

```text
I(x) = -log2 P(x)
```

Nếu `P(x)=1`, thông tin (information / 정보) là 0 bit. Nếu `P(x)=1/2`, sự kiện (event / 이벤트) mang 1 bit surprise. Nếu `P(x)=1/1024`, sự kiện (event / 이벤트) mang 10 bit.

Logarithm xuất hiện vì ta muốn thông tin (information / 정보) của hai independent events cộng được:

```text
P(x,y) = P(x)P(y)
⇒ I(x,y) = I(x) + I(y)
```

Đây là thuộc tính (property / 속성) phù hợp với cách description length cộng qua các lựa chọn độc lập.

> **Nối mạch:** **2. Entropy là bất định (uncertainty / 불확실성) trung bình của phân phối (distribution / 분포)** nối từ **1. thông tin (information / 정보) bắt đầu từ surprise** sang **3. Joint, conditional entropy và mutual thông tin (information / 정보)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Entropy là bất định (uncertainty / 불확실성) trung bình của phân phối (distribution / 분포)

Với random variable `X`, Shannon entropy:

```text
H(X) = - Σ p(x) log2 p(x)
```

Entropy không phải “độ hỗn loạn” theo nghĩa mơ hồ. Nó là expected self-information nếu mẫu (sample / 표본) từ phân phối (distribution / 분포).

Một fair coin có:

```text
H(X) = 1 bit
```

Một coin có xác suất head `0.999` có entropy thấp hơn nhiều vì kết quả (outcome / 결과) gần như dự đoán được.

Nếu nguồn (source / 소스) phát symbol theo phân phối (distribution / 분포) lệch, ta có cơ hội dùng mã (code / 코드) ngắn cho symbol phổ biến và mã (code / 코드) dài cho symbol hiếm để giảm expected length.

> **Nối mạch:** **3. Joint, conditional entropy và mutual thông tin (information / 정보)** nối từ **2. Entropy là bất định (uncertainty / 불확실성) trung bình của phân phối (distribution / 분포)** sang **4. nguồn (source / 소스) coding: entropy là lower-bound trung bình, không phải tệp (file / 파일) kích thước (size / 크기) thần kỳ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Joint, conditional entropy và mutual thông tin (information / 정보)

Hệ thống thực tế có nhiều variable liên quan. Nếu biết `Y` giúp dự đoán `X`, bất định (uncertainty / 불확실성) còn lại của `X` giảm.

**Conditional entropy**:

```text
H(X|Y)
```

đo bất định (uncertainty / 불확실성) còn lại về `X` sau khi biết `Y`.

**Mutual thông tin (information / 정보)**:

```text
I(X;Y) = H(X) - H(X|Y)
```

đo lượng thông tin (information / 정보) về `X` mà `Y` cung cấp.

Mô hình tư duy (mental model / 사고 모델):

```text
H(X)      = uncertainty ban đầu
H(X|Y)    = uncertainty còn lại sau khi biết Y
I(X;Y)    = phần uncertainty đã được Y giải thích
```

Mutual thông tin (information / 정보) quan trọng trong tính năng (feature / 기능) selection, communication và biểu diễn (representation / 표현) học tập (learning / 학습), nhưng không tự động chứng minh nhân quả (causal / 인과적) quan hệ (relation / 관계). Hai variable có thể chia sẻ thông tin (information / 정보) vì cùng phụ thuộc một nguyên nhân khác.

> **Nối mạch:** **3. Joint, conditional entropy và mutual thông tin (information / 정보)** đặt vấn đề; **4. nguồn (source / 소스) coding: entropy là lower-bound trung bình, không phải tệp (file / 파일) kích thước (size / 크기) thần kỳ** kiểm tra bằng chứng, rồi **5. Prefix mã (code / 코드) và Kraft inequality** mở rộng hệ quả.

## 4. nguồn (source / 소스) coding: entropy là lower-bound trung bình, không phải tệp (file / 파일) kích thước (size / 크기) thần kỳ

Nguồn (source / 소스) coding theorem nói theo trực giác rằng với nguồn (source / 소스) có phân phối (distribution / 분포) ổn định và khối (block / 블록) đủ dài, lossless mã (code / 코드) có expected bits/symbol tiến gần entropy, nhưng không thể trung bình thấp hơn entropy một cách tùy ý mà vẫn decode chính xác.

Điều này không có nghĩa mọi message cụ thể dài đúng `H(X)`. Entropy là expectation trên phân phối (distribution / 분포).

Ví dụ alphabet:

```text
A: 1/2
B: 1/4
C: 1/8
D: 1/8
```

Một prefix mã (code / 코드) hợp lý có thể dùng độ dài gần:

```text
A → 1 bit
B → 2 bits
C → 3 bits
D → 3 bits
```

Symbol phổ biến nhận mã (code / 코드) ngắn hơn.

> **Nối mạch:** **4. nguồn (source / 소스) coding: entropy là lower-bound trung bình, không phải tệp (file / 파일) kích thước (size / 크기) thần kỳ** đặt vấn đề; **5. Prefix mã (code / 코드) và Kraft inequality** kiểm tra bằng chứng, rồi **6. Compression khai thác phụ thuộc (dependency / 의존성) chứ không chỉ frequency đơn symbol** mở rộng hệ quả.

## 5. Prefix mã (code / 코드) và Kraft inequality

Nếu codeword phải decode nối tiếp mà không cần delimiter, một codeword không được là prefix của codeword khác.

Ví dụ hợp lệ:

```text
A = 0
B = 10
C = 110
D = 111
```

Kraft inequality mô tả ràng buộc (constraint / 제약조건) giữa các mã (code / 코드) length `l_i` cho prefix mã (code / 코드):

```text
Σ 2^(-l_i) ≤ 1
```

Nó cho thấy mã (code / 코드) length không thể tùy ý ngắn cho mọi symbol. Cây nhị phân có “sức chứa (capacity / 용량)” hữu hạn cho leaf codeword.

**Huffman coding** tìm prefix mã (code / 코드) tối ưu theo expected length trong lớp (class / 클래스) mã (code / 코드) symbol-by-symbol với xác suất (probability / 확률) đã biết. **Arithmetic/phạm vi (range / 범위) coding** có thể biểu diễn cả chuỗi (sequence / 시퀀스) theo interval và tiến gần entropy hơn khi xác suất (probability / 확률) không khớp đẹp với integer bit lengths.

> **Nối mạch:** **6. Compression khai thác phụ thuộc (dependency / 의존성) chứ không chỉ frequency đơn symbol** nối từ **5. Prefix mã (code / 코드) và Kraft inequality** sang **7. Cross-entropy và coding regret**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Compression khai thác phụ thuộc (dependency / 의존성) chứ không chỉ frequency đơn symbol

Nếu nguồn (source / 소스) có correlation theo thời gian, entropy mỗi symbol riêng lẻ có thể cao nhưng conditional entropy thấp.

Ví dụ văn bản (text / 텍스트): ký tự tiếp theo phụ thuộc ngữ cảnh (context / 맥락). `q` trong tiếng Anh thường làm `u` dễ dự đoán hơn. Video frame kế tiếp tương quan mạnh với frame trước. Log line kế tiếp thường dùng lại template.

Một compressor tốt vì vậy mô hình (model / 모델):

```text
P(next_symbol | context)
```

thay vì chỉ `P(symbol)`.

Đây là cầu nối (bridge / 브리지) tới ngôn ngữ (language / 언어) modeling: predictive mô hình (model / 모델) tốt giảm bất định (uncertainty / 불확실성) của next đơn vị từ (token / 토큰). Tuy nhiên cross-entropy/perplexity của mô hình (model / 모델) và ngữ nghĩa (semantic / 의미적) understanding không phải cùng một khái niệm.

> **Nối mạch:** **7. Cross-entropy và coding regret** nối từ **6. Compression khai thác phụ thuộc (dependency / 의존성) chứ không chỉ frequency đơn symbol** sang **8. Noisy channel: transmission có thể làm bit thay đổi hoặc biến mất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Cross-entropy và coding regret

Nếu true phân phối (distribution / 분포) là `P` nhưng ta encode bằng mô hình (model / 모델) `Q`, expected mã (code / 코드) length liên quan tới **cross-entropy**:

```text
H(P,Q) = - E_P[log2 Q(x)]
```

Khoảng chênh so với entropy thật được mô tả bởi KL divergence:

```text
H(P,Q) = H(P) + D_KL(P || Q)
```

Trực giác môi trường vận hành (production / 운영 환경) rất hữu ích:

```text
true uncertainty
+ model mismatch penalty
= expected coding cost under model
```

Mô hình (model / 모델) xác suất (probability / 확률) tệ không chỉ là “dự đoán kém”; nếu dùng cho entropy coding, nó tạo thêm bit thật.

> **Nối mạch:** **8. Noisy channel: transmission có thể làm bit thay đổi hoặc biến mất** nối từ **7. Cross-entropy và coding regret** sang **9. Noisy-channel coding theorem: reliable không có nghĩa zero-noise**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Noisy channel: transmission có thể làm bit thay đổi hoặc biến mất

Trong communication, channel có thể flip bit, erase symbol, reorder packet hoặc tạo burst mất mát (loss / 손실) tùy tầng (layer / 계층).

Thông tin (information / 정보) lý thuyết (theory / 이론) lớp trừu tượng (abstraction / 추상화) tách nguồn (source / 소스) khỏi channel. Ta hỏi: với channel chuyển tiếp (transition / 전이) xác suất (probability / 확률) cụ thể, tốc độ reliable thông tin (information / 정보) tối đa là bao nhiêu?

**Channel sức chứa (capacity / 용량)** là supremum của mutual thông tin (information / 정보) giữa đầu vào (input / 입력) và đầu ra (output / 출력) trên đầu vào (input / 입력) phân phối (distribution / 분포) phù hợp:

```text
C = max I(X;Y)
```

Không cần thuộc công thức cho mọi channel; cần giữ mô hình tư duy (mental model / 사고 모델): sức chứa (capacity / 용량) phụ thuộc cả tín hiệu (signal / 신호) choices lẫn noise hành vi (behavior / 동작).

> **Nối mạch:** **9. Noisy-channel coding theorem: reliable không có nghĩa zero-noise** nối từ **8. Noisy channel: transmission có thể làm bit thay đổi hoặc biến mất** sang **10. lỗi (error / 오류) detection và lỗi (error / 오류) correction khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Noisy-channel coding theorem: reliable không có nghĩa zero-noise

Một kết quả sâu của Shannon là nếu transmission tỷ lệ (rate / 비율) nhỏ hơn channel sức chứa (capacity / 용량), tồn tại coding scheme cho phép lỗi (error / 오류) xác suất (probability / 확률) giảm rất thấp khi khối (block / 블록) length tăng đủ. Nếu tỷ lệ (rate / 비율) vượt sức chứa (capacity / 용량), không thể làm reliable arbitrarily chỉ bằng coding thông minh.

Điểm quan trọng:

```text
noise tồn tại
≠ communication đáng tin cậy là bất khả thi
```

Ta thêm structured redundancy để decoder phân biệt codeword ngay cả khi một phần tín hiệu bị corruption.

Nhưng redundancy dùng bandwidth/lưu trữ (storage / 저장소). độ tin cậy (reliability / 신뢰성) luôn có chi phí (cost / 비용).

> **Nối mạch:** **10. lỗi (error / 오류) detection và lỗi (error / 오류) correction khác nhau** nối từ **9. Noisy-channel coding theorem: reliable không có nghĩa zero-noise** sang **11. Erasure dễ hơn unknown corruption**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. lỗi (error / 오류) detection và lỗi (error / 오류) correction khác nhau

Checksum/CRC thường mạnh ở **phát hiện** corruption nhưng không nhất thiết đủ để sửa. Error-correcting mã (code / 코드) thêm redundancy có cấu trúc (structure / 구조) để xác định codeword gần nhất.

Một khái niệm nền là **Hamming distance**: số vị trí khác nhau giữa hai codeword.

Nếu minimum distance giữa codeword là `d`, trực giác:

- phát hiện được tới `d-1` bit lỗi (error / 오류) trong mô hình (model / 모델) tương ứng;
- sửa được khoảng `floor((d-1)/2)` bit lỗi (error / 오류) bằng nearest-codeword lập luận (reasoning / 추론).

Đây là geometric view: codeword phải đủ xa nhau để noise nhỏ không đẩy received word sang vùng của codeword khác.

> **Nối mạch:** **11. Erasure dễ hơn unknown corruption** nối từ **10. lỗi (error / 오류) detection và lỗi (error / 오류) correction khác nhau** sang **12. Burst lỗi (error / 오류) và interleaving**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Erasure dễ hơn unknown corruption

Nếu receiver biết vị trí symbol bị mất, đó là **erasure**. Nếu receiver nhận một symbol sai mà không biết vị trí nào sai, đó là **lỗi (error / 오류)**.

Erasure thường dễ sửa hơn vì bất định (uncertainty / 불확실성) nhỏ hơn. lưu trữ (storage / 저장소)/phân tán (distributed / 분산) các hệ thống (systems / 시스템들) tận dụng điều này: nếu biết shard/nút (node / 노드) nào mất, erasure coding có thể reconstruct từ các fragment còn lại với lưu trữ (storage / 저장소) overhead thấp hơn full replication trong một số tải công việc (workload / 워크로드).

Nhưng erasure coding thêm CPU, mạng (network / 네트워크) fan-out, repair traffic và failure-domain lập luận (reasoning / 추론). Không nên kết luận “erasure coding luôn rẻ hơn replication” chỉ từ raw lưu trữ (storage / 저장소) ratio.

> **Nối mạch:** **12. Burst lỗi (error / 오류) và interleaving** nối từ **11. Erasure dễ hơn unknown corruption** sang **13. sức chứa (capacity / 용량) không đồng nghĩa thông lượng (throughput / 처리량) ứng dụng (application / 애플리케이션)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Burst lỗi (error / 오류) và interleaving

Nhiều vật lý (physical / 물리적) channel không tạo independent random bit flip; lỗi đến theo burst. Nếu một khối (block / 블록) mã (code / 코드) chịu được vài lỗi (error / 오류) nhưng cả burst rơi vào cùng khối (block / 블록), correction có thể thất bại.

**Interleaving** phân tán các symbol liên tiếp của codeword qua thời gian/không gian để một burst vật lý (physical / 물리적) trở thành các lỗi (error / 오류) thưa hơn ở nhiều codeword.

Sự đánh đổi (trade-off / 트레이드오프) là độ trễ (latency / 지연 시간) và buffer tăng. Đây là ví dụ điển hình của việc thay đổi biểu diễn (representation / 표현) để biến thất bại (failure / 실패) mẫu (pattern / 패턴) thành dạng mã (code / 코드) xử lý tốt hơn.

> **Nối mạch:** **13. sức chứa (capacity / 용량) không đồng nghĩa thông lượng (throughput / 처리량) ứng dụng (application / 애플리케이션)** nối từ **12. Burst lỗi (error / 오류) và interleaving** sang **14. Entropy không đo ngữ nghĩa (semantic / 의미적) giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. sức chứa (capacity / 용량) không đồng nghĩa thông lượng (throughput / 처리량) ứng dụng (application / 애플리케이션)

Vật lý (physical / 물리적)/link sức chứa (capacity / 용량) chỉ là một tầng. ứng dụng (application / 애플리케이션) thông lượng (throughput / 처리량) còn bị giảm bởi framing, retransmission, congestion điều khiển (control / 제어), encryption, giao thức (protocol / 프로토콜) headers, queueing và yêu cầu (request / 요청) ngữ nghĩa (semantics / 의미론).

```text
channel capacity
→ link goodput
→ transport goodput
→ application useful throughput
```

Nếu packet mất mát (loss / 손실) tăng, vận chuyển (transport / 전송) có thể giảm sending tỷ lệ (rate / 비율) dù raw link bandwidth không đổi. Nếu dữ liệu (data / 데이터) đã compressed mạnh, thêm compression CPU có thể làm thông lượng (throughput / 처리량) ứng dụng (application / 애플리케이션) xấu hơn.

Do đó khi debugging cần xác định tầng (layer / 계층) nào sở hữu “tỷ lệ (rate / 비율)” đang nói tới.

> **Nối mạch:** **14. Entropy không đo ngữ nghĩa (semantic / 의미적) giá trị (value / 값)** nối từ **13. sức chứa (capacity / 용량) không đồng nghĩa thông lượng (throughput / 처리량) ứng dụng (application / 애플리케이션)** sang **15. Entropy tỷ lệ (rate / 비율) và nguồn (source / 소스) có bộ nhớ (memory / 메모리)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Entropy không đo ngữ nghĩa (semantic / 의미적) giá trị (value / 값)

Một encrypted backup có entropy quan sát rất cao nhưng ngữ nghĩa (semantic / 의미적) giá trị (value / 값) có thể cực lớn. Một random tệp (file / 파일) cũng có entropy cao nhưng không hữu ích. Một cấu hình (configuration / 구성) tệp (file / 파일) rất compressible nhưng có thể quyết định toàn bộ môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작).

Thông tin (information / 정보) lý thuyết (theory / 이론) cố ý bỏ qua ý nghĩa (semantic meaning / 의미적 뜻) để có theorem tổng quát về coding và communication.

Đừng dùng “entropy cao” như synonym của “thông tin quan trọng”.

> **Nối mạch:** **14. Entropy không đo ngữ nghĩa (semantic / 의미적) giá trị (value / 값)** đặt vấn đề; **15. Entropy tỷ lệ (rate / 비율) và nguồn (source / 소스) có bộ nhớ (memory / 메모리)** kiểm tra bằng chứng, rồi **16. bằng chứng vận hành (production evidence / 운영 증거) cho lưu trữ (storage / 저장소)/mạng (network / 네트워크) coding** mở rộng hệ quả.

## 15. Entropy tỷ lệ (rate / 비율) và nguồn (source / 소스) có bộ nhớ (memory / 메모리)

Với tiến trình (process / 프로세스) có phụ thuộc (dependency / 의존성) dài, ta quan tâm bất định (uncertainty / 불확실성) mới trung bình mỗi symbol khi biết quá khứ:

```text
H_rate ≈ lim H(X_n | X_1 ... X_{n-1})
```

Nếu chuỗi (sequence / 시퀀스) rất predictable từ lịch sử (history / 이력), entropy tỷ lệ (rate / 비율) thấp dù marginal phân phối (distribution / 분포) từng symbol có thể trông cân bằng.

Liên kết (connection / 연결) này giải thích tại sao dictionary/ngữ cảnh (context / 맥락) compressor có thể nén chuỗi (sequence / 시퀀스) mà frequency histogram đơn giản không cho thấy lợi ích.

> **Nối mạch:** **15. Entropy tỷ lệ (rate / 비율) và nguồn (source / 소스) có bộ nhớ (memory / 메모리)** đặt vấn đề; **16. bằng chứng vận hành (production evidence / 운영 증거) cho lưu trữ (storage / 저장소)/mạng (network / 네트워크) coding** kiểm tra bằng chứng, rồi **17. liên kết (connection / 연결) với cơ sở dữ liệu (database / 데이터베이스) và phân tán (distributed / 분산) các hệ thống (systems / 시스템들)** mở rộng hệ quả.

## 16. bằng chứng vận hành (production evidence / 운영 증거) cho lưu trữ (storage / 저장소)/mạng (network / 네트워크) coding

Khi một hệ thống (system / 시스템) dùng compression hoặc error-control coding, bằng chứng (evidence / 증거) nên phân biệt:

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

Nếu compression ratio tốt nhưng CPU saturation làm hàng đợi (queue / 큐) tăng, end-to-end hệ thống (system / 시스템) có thể tệ hơn. Nếu erasure coding tiết kiệm lưu trữ (storage / 저장소) nhưng repair storm bão hòa mạng (network / 네트워크) sau rack thất bại (failure / 실패), chi phí (cost / 비용) mô hình (model / 모델) ban đầu thiếu hành vi khi thất bại (failure behavior / 실패 동작).

> **Nối mạch:** **16. bằng chứng vận hành (production evidence / 운영 증거) cho lưu trữ (storage / 저장소)/mạng (network / 네트워크) coding** đặt vấn đề; **17. liên kết (connection / 연결) với cơ sở dữ liệu (database / 데이터베이스) và phân tán (distributed / 분산) các hệ thống (systems / 시스템들)** kiểm tra bằng chứng, rồi **18. liên kết (connection / 연결) với machine học tập (learning / 학습)** mở rộng hệ quả.

## 17. liên kết (connection / 연결) với cơ sở dữ liệu (database / 데이터베이스) và phân tán (distributed / 분산) các hệ thống (systems / 시스템들)

Cơ sở dữ liệu (database / 데이터베이스) columnar encoding dùng phân phối (distribution / 분포)/locality để giảm bytes và bộ nhớ (memory / 메모리) bandwidth. Bloom filter chấp nhận false positive để giảm I/O. Replicated log dùng checksum để phát hiện corruption. phân tán (distributed / 분산) lưu trữ (storage / 저장소) có thể dùng replication hoặc erasure coding để đổi lưu trữ (storage / 저장소) overhead lấy khôi phục (recovery / 복구)/mạng (network / 네트워크) độ phức tạp (complexity / 복잡도).

Đọc thêm:

- [Columnar storage, encoding, pruning và vectorized scans](../../05_data_databases/advanced/08_columnar_storage_encoding_pruning_and_vectorized_scans.md)
- [Multi-region replication và geo-distributed trade-offs](../../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md)
- [Durability path application → WAL → filesystem → device](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md)

> **Nối mạch:** **17. liên kết (connection / 연결) với cơ sở dữ liệu (database / 데이터베이스) và phân tán (distributed / 분산) các hệ thống (systems / 시스템들)** đặt vấn đề; **18. liên kết (connection / 연결) với machine học tập (learning / 학습)** kiểm tra bằng chứng, rồi **19. Những nhầm lẫn thường gặp** mở rộng hệ quả.

## 18. liên kết (connection / 연결) với machine học tập (learning / 학습)

Cross-entropy mất mát (loss / 손실) có interpretation coding: mô hình (model / 모델) gán xác suất (probability / 확률) cao cho observed kết quả (outcome / 결과) sẽ cần ít surprise bits hơn. Perplexity thường là exponent của average negative log xác suất (probability / 확률) theo cơ sở (base / 기반) phù hợp.

Nhưng môi trường vận hành (production / 운영 환경) mô hình (model / 모델) chất lượng (quality / 품질) không chỉ là cross-entropy. Calibration, tác vụ (task / 작업) utility, phân phối (distribution / 분포) shift, độ trễ (latency / 지연 시간) và an toàn (safety / 안전) vẫn là đặc tả hợp đồng (contract / 계약) riêng.

Information-theoretic chỉ số (metric / 지표) cho biết mô hình (model / 모델) xác suất (probability / 확률) phù hợp dữ liệu (data / 데이터) tới đâu, không tự động cho biết quyết định (decision / 결정) downstream đúng hay có giá trị.

> **Nối mạch:** **18. liên kết (connection / 연결) với machine học tập (learning / 학습)** đặt tiêu chí; **19. Những nhầm lẫn thường gặp** dùng nó để kiểm tra ranh giới, rồi **20. Checklist lập luận (reasoning / 추론)** mở rộng hệ quả.

## 19. Những nhầm lẫn thường gặp

**“Entropy là randomness của một tệp (file / 파일) cụ thể.”** Shannon entropy cần phân phối (distribution / 분포)/random variable. Với đối tượng (object / 객체) cụ thể, algorithmic độ phức tạp (complexity / 복잡도) là viewpoint khác.

**“Nén tới entropy nghĩa là mọi tệp (file / 파일) đều có kích thước (size / 크기) H.”** Không. Bound là expected/asymptotic theo nguồn (source / 소스) mô hình (model / 모델).

**“Checksum sửa được lỗi.”** Checksum chủ yếu detect; correction cần redundancy có cấu trúc (structure / 구조) phù hợp.

**“Bandwidth 1 Gbps nghĩa app gửi được 1 Gbps payload.”** Không. Phải trừ giao thức (protocol / 프로토콜) overhead và hành vi (behavior / 동작) do mất mát (loss / 손실)/congestion/CPU.

**“Thêm redundancy luôn làm độ tin cậy (reliability / 신뢰성) tốt hơn.”** Chỉ nếu mã (code / 코드)/thất bại (failure / 실패) mô hình (model / 모델) phù hợp; correlated failures có thể phá giả định (assumption / 가정).

**“Mutual thông tin (information / 정보) cao nghĩa X gây ra Y.”** Không. phụ thuộc (dependency / 의존성) không đồng nghĩa causality.

> **Nối mạch:** **19. Những nhầm lẫn thường gặp** đặt tiêu chí; **20. Checklist lập luận (reasoning / 추론)** dùng nó để kiểm tra ranh giới, rồi **Kết luận** mở rộng hệ quả.

## 20. Checklist lập luận (reasoning / 추론)

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

> **Nối mạch:** **Kết luận** tổng hợp từ **20. Checklist lập luận (reasoning / 추론)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết luận

Thông tin (information / 정보) lý thuyết (theory / 이론) cung cấp hai giới hạn nền tảng: **nguồn (source / 소스) bất định (uncertainty / 불확실성) giới hạn mức lossless compression trung bình**, và **channel sức chứa (capacity / 용량) giới hạn tốc độ reliable communication qua noise**. Coding không xóa giới hạn vật lý; nó tổ chức biểu diễn (representation / 표현) và redundancy để tiến gần giới hạn đó.

Mô hình tư duy (mental model / 사고 모델) cần giữ:

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

Từ tệp (file / 파일) compression, cơ sở dữ liệu (database / 데이터베이스) encoding, mạng (network / 네트워크) vận chuyển (transport / 전송), lưu trữ (storage / 저장소) repair tới cross-entropy trong machine học tập (learning / 학습), cùng một câu hỏi lặp lại: **bất định (uncertainty / 불확실성) nằm ở đâu, biểu diễn (representation / 표현) nào đang khai thác cấu trúc (structure / 구조), và redundancy nào đang được trả để giữ bất biến (invariant / 불변식)?**

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
