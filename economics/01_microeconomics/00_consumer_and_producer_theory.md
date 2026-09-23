# Consumer & Producer Theory — Lựa chọn, cầu, chi phí và cung

Consumer và producer theory là hai mô hình nền tảng của microeconomics. Mục tiêu không phải gán cho con người một công thức utility “đúng tuyệt đối”, mà tạo một ngôn ngữ để hỏi: tác nhân đang tối ưu gì, constraint nào ràng buộc, và thay đổi nào làm lựa chọn ở biên đổi hướng?

## 1. Consumer bắt đầu từ budget constraint

Với hai hàng hóa `x` và `y`, thu nhập `m` và giá `p_x`, `p_y`, budget constraint là:

```text
p_x x + p_y y ≤ m
```

Đường ngân sách có intercept `m / p_x` và `m / p_y`, độ dốc `-p_x / p_y`. Giá tương đối, không chỉ giá tuyệt đối, quyết định trade-off. Thu nhập tăng làm đường ngân sách dịch song song; giá một hàng hóa đổi làm đường xoay quanh intercept của hàng hóa kia nếu thu nhập danh nghĩa giữ nguyên.

Budget constraint không nói household chắc chắn chọn điểm nào. Nó chỉ cho biết tập lựa chọn khả thi. Để chọn một điểm, cần mô hình hóa preferences hoặc quy tắc quyết định.

## 2. Preferences, utility và indifference curve

Preference biểu diễn thứ tự mà consumer gán cho các bundles. Utility là representation tiện dụng của thứ tự đó; utility cao hơn không nhất thiết là “hạnh phúc nhiều hơn” theo đơn vị cardinal có thể so sánh giữa người với người.

Các giả định thường dùng:

- **completeness**: consumer có thể xếp hạng hai bundles hoặc coi chúng indifferent;
- **transitivity**: nếu A được thích hơn B và B hơn C thì A được thích hơn C;
- **monotonicity**: nhiều hơn một hàng hóa tốt, nếu không có bads;
- **convexity**: bundles cân bằng thường được ưa thích hơn extremes.

Indifference curve nối các bundles đem lại cùng utility. Độ dốc của nó là marginal rate of substitution (MRS): consumer sẵn sàng bỏ bao nhiêu `y` để có thêm một đơn vị `x` mà vẫn giữ utility.

## 3. Optimal choice là tiếp điểm giữa objective và constraint

Trong nghiệm nội bộ, consumer chọn bundle thỏa:

```text
MRS = p_x / p_y
```

Trực giác: willingness to trade ở biên phải bằng market trade-off. Nếu MRS lớn hơn price ratio, `x` tương đối đáng giá nên consumer muốn tăng `x`; nếu nhỏ hơn, consumer muốn giảm `x`.

Điều kiện tiếp điểm không áp dụng máy móc khi có corner solution, perfect substitutes, perfect complements, discrete choice, fixed cost hoặc non-convex preferences. Khi đó phải kiểm tra toàn bộ boundary của feasible set.

## 4. Price change tạo income effect và substitution effect

Khi giá `x` giảm, consumer có hai phản ứng:

1. **Substitution effect**: `x` rẻ tương đối hơn so với `y`, nên thay thế về phía `x`.
2. **Income effect**: cùng một thu nhập danh nghĩa mua được nhiều sức mua hơn; hướng tác động phụ thuộc việc `x` là normal good hay inferior good.

Với normal good, hai hiệu ứng thường cùng làm lượng cầu tăng khi giá giảm. Với inferior good, income effect có thể ngược chiều. Chỉ trong trường hợp đặc biệt, hiệu ứng ngược chiều đủ mạnh mới tạo Giffen behavior; không nên suy ra mọi hàng hóa inferior đều là Giffen goods.

## 5. Từ lựa chọn cá nhân tới đường cầu

Đường cầu biểu diễn lượng cầu tối ưu ở mỗi mức giá, giữ các yếu tố liên quan khác theo một ceteris paribus nhất định. **Movement along demand curve** đến từ thay đổi giá của chính hàng hóa. **Shift of demand curve** đến từ thu nhập, giá hàng thay thế/bổ sung, kỳ vọng, preferences, số người mua hoặc thông tin.

Elasticity đo phản ứng tỷ lệ:

```text
price elasticity of demand = %ΔQ_d / %ΔP
```

Elasticity là local hoặc theo một khoảng giá cụ thể. Doanh thu tăng hay giảm khi giá đổi phụ thuộc độ co giãn, không thể kết luận chỉ từ hướng của giá.

## 6. Producer bắt đầu từ technology

Firm biến inputs thành output qua production function:

```text
q = f(K, L, A, ...)
```

`K` có thể là capital, `L` là labor, `A` là technology hoặc productivity shifter. Production function mô tả khả năng kỹ thuật, chưa tự nói firm nên sản xuất bao nhiêu hay ai sở hữu surplus.

Trong ngắn hạn, ít nhất một input bị cố định. Trong dài hạn, firm có thể điều chỉnh tất cả inputs, thay đổi quy mô plant và chọn technology. Vì vậy short-run cost curve không thể đọc như long-run cost curve.

## 7. Cost: fixed, variable, average và marginal

- **Fixed cost** không đổi theo output trong phạm vi ngắn hạn nhất định.
- **Variable cost** thay đổi khi output thay đổi.
- **Average total cost** là total cost chia output.
- **Marginal cost** là chi phí tăng thêm của một đơn vị output.

```text
TC(q) = FC + VC(q)
MC(q) = ΔTC / Δq
ATC(q) = TC(q) / q
```

Marginal cost có thể tăng vì diminishing marginal product của input biến đổi. Average cost có thể giảm khi fixed cost được phân bổ trên nhiều đơn vị, nhưng diseconomies of scale hoặc coordination cost có thể làm nó tăng lại.

## 8. Profit maximization và supply

Lợi nhuận kinh tế là:

```text
π(q) = TR(q) − TC(q)
```

Firm cạnh tranh hoàn hảo là price taker và chọn output nội bộ khi:

```text
P = MR = MC
```

Điều kiện này chỉ cho nghiệm tối ưu cục bộ. Firm vẫn phải kiểm tra shutdown condition trong ngắn hạn, exit condition trong dài hạn, fixed cost, capacity và khả năng có nhiều nghiệm.

Đường cung cá nhân không phải toàn bộ MC curve. Trong cạnh tranh hoàn hảo, short-run supply thường là phần MC nằm trên minimum AVC; nhưng market power, adjustment cost, inventory và strategic behavior làm mapping này thay đổi.

## 9. Từ private equilibrium tới social outcome

Nếu producer hoặc consumer không chịu toàn bộ cost/benefit do giao dịch tạo ra, private equilibrium có thể lệch khỏi social optimum.

```text
social marginal cost = private marginal cost + external damage
social marginal benefit = private marginal benefit + external benefit
```

Externality, public good và asymmetric information tạo lý do để phân tích market failure. Nhưng “có market failure” không tự động chứng minh một can thiệp cụ thể tốt hơn laissez-faire; cần tính policy implementation cost, government failure, incidence và phản ứng hành vi.

## 10. Checklist mô hình

1. Ai là decision-maker và objective của họ là gì?
2. Budget, technology hoặc institutional constraint nằm ở đâu?
3. Biến nào là price, quantity, stock, flow hoặc parameter?
4. Nghiệm có nằm ở interior hay boundary?
5. Kết luận là short-run hay long-run?
6. Có externality, market power, information asymmetry hay strategic response không?
7. Nếu giá thay đổi, đây là movement along curve hay curve shift?
8. Kết quả nói về private efficiency, social efficiency, distribution hay cả ba?

Đây là nền để đọc market structure và game theory mà không nhầm “firm tối đa hóa lợi nhuận trong mô hình” với mô tả đầy đủ về doanh nghiệp ngoài đời.
