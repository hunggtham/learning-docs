# Amortized, Randomized và Probabilistic Thinking
**상환 분석, 무작위화, 확률적 사고**

Không phải mọi guarantee đều “mỗi operation chắc chắn mất X”. Có guarantee theo cả sequence operations hoặc expectation trên randomness.

## Amortized analysis

Dynamic array resize là ví dụ điển hình. Một append đôi khi `O(n)` nhưng sequence dài có average amortized `O(1)`.

Ba kiểu reasoning phổ biến là aggregate, accounting và potential method. Potential method tưởng tượng structure tích lũy “potential” ở những operation rẻ để trả cho operation đắt tương lai.

## Randomized algorithms

Randomized quicksort chọn pivot ngẫu nhiên để input cố định khó liên tục tạo partition xấu. Expected runtime `O(n log n)` không nói mọi run đều đúng bằng mức đó; nó là kỳ vọng theo randomness.

## Probabilistic structures

Bloom filter dùng bit array và nhiều hashes để membership test với false positive probability nhưng không false negative trong model insert/query chuẩn. Nó đánh đổi memory để chấp nhận câu trả lời “có thể có” đôi khi sai dương.

## Hashing và adversarial behavior

Randomized/universal hashing có thể giúp chống input được thiết kế để gây collisions. Khi xử lý dữ liệu không tin cậy, worst-case/adversarial model có thể quan trọng hơn average-case thông thường.

## Mental Model

> Amortized guarantee phân bổ cost trên sequence. Randomized/expected guarantee phân bổ trên randomness. Probabilistic structures chủ động đổi exactness lấy space/time.

## Potential method trực giác

Ta gán một potential `Phi(state) >= 0`. Amortized cost của operation:

\[
\hat c_i = c_i + \Phi(D_i)-\Phi(D_{i-1})
\]

Nếu operation làm structure “tích năng lượng” cho future work, potential tăng và amortized charge cao hơn actual. Khi expensive operation tiêu năng lượng, potential giảm và bù actual cost.

Dynamic table, splay tree và many incremental structures có thể được phân tích theo cách này.

## Las Vegas và Monte Carlo

Randomized algorithms có hai flavor quan trọng.

**Las Vegas**: luôn trả answer đúng; randomness ảnh hưởng runtime. Randomized quicksort là ví dụ điển hình nếu implementation sorting luôn đúng.

**Monte Carlo**: runtime bounded hơn nhưng có xác suất error. Probabilistic primality tests hoặc hashing-based equality checks có thể thuộc dạng này tùy design.

Distinction giúp nói rõ guarantee thay vì chỉ gọi “randomized”.

## Bloom filter mechanics

Bit array `m` bits, `k` hash functions. Insert set `k` positions. Query “definitely not present” nếu có ít nhất một bit 0; nếu mọi bit 1 thì “possibly present”. False positives xảy ra do keys khác cùng set bits.

Standard Bloom filter không hỗ trợ deletion an toàn vì clear một bit có thể phá membership của item khác; counting Bloom filter dùng counters để support deletion với memory cost cao hơn.

## Approximation vs randomness

Approximation algorithm có thể deterministic nhưng cố ý trả solution gần optimal để đổi lấy polynomial runtime. Randomized algorithm có thể trả exact solution nhưng dùng random choices. Hai concepts độc lập dù đôi khi xuất hiện cùng nhau.
