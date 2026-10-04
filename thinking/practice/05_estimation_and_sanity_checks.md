# Estimation & Sanity Checks — Ước lượng đủ tốt để phát hiện điều vô lý

Ước lượng Fermi không nhằm tạo một con số đẹp khi dữ liệu thiếu. Nó giúp trả lời nhanh ba câu hỏi: quy mô có hợp lý không, assumption nào đang chi phối, và cần đo thêm điều gì trước khi quyết định. Phần formal về xác suất, sai số và mô hình thuộc [Mathematics](../../mathematics/README.md); drill này luyện cách biến câu hỏi mơ hồ thành estimate có thể kiểm tra.

## 1. Chốt đại lượng, đơn vị và quyết định

Viết câu hỏi sao cho biết rõ object, unit, population, time horizon và decision mà estimate phục vụ. “Thị trường lớn không?” phải đổi thành “Trong 12 tháng, có bao nhiêu khách hàng thuộc segment X có thể trả mức Y tại thị trường Z?”.

Nếu không nói estimate dùng để làm gì, ta dễ đo một đại lượng thú vị nhưng không thay đổi action. Output tối thiểu là `central range → decision threshold → uncertainty that matters`.

## 2. Dựng upper/lower bounds trước khi tính giữa

Bounds ngăn kết quả rơi ra ngoài thế giới có thể xảy ra. Hỏi:

```text
minimum plausible
maximum plausible
hard physical / contractual limit
```

Ví dụ số chuyến giao hàng không thể vượt số đơn, số giờ người có thể làm hoặc năng lực kho. Nếu estimate vượt bound, lỗi thường nằm ở unit, denominator hoặc double-counting chứ chưa cần model phức tạp hơn.

## 3. Decompose thành các yếu tố nhân hoặc cộng

Một estimate dễ review hơn khi viết thành các phần có nghĩa:

```text
annual demand
= reachable users
× adoption rate
× purchase frequency
```

hoặc:

```text
monthly cost
= fixed cost
+ variable units × unit cost
+ failure / support cost
```

Mỗi factor cần range và rationale riêng. Không nhân probability máy móc khi các factor phụ thuộc nhau; decomposition ở đây để lộ assumption, không giả rằng các factor độc lập.

## 4. Kiểm tra đơn vị và bậc độ lớn

Đọc lại phép tính từ dimension: `people × events/person × cost/event` phải ra tiền, không ra “tiền mỗi người”. Sau đó làm order-of-magnitude check: kết quả là hàng chục, hàng nghìn hay hàng triệu? Một sai số 10× thường đáng nghi hơn một sai số 10%.

Sanity check cũng có thể dùng một cách tính thứ hai, dữ liệu lịch sử hoặc một reference class. Hai phương pháp độc lập cùng cho một bậc độ lớn giúp tăng confidence; chúng cùng dựa một assumption thì không phải hai bằng chứng độc lập.

## 5. Base rate và bounds không thay thế nhau

Bounds nói cái gì có thể; base rate nói cái gì thường xảy ra. Một startup có thể đạt tăng trưởng 100× về mặt logic nhưng reference class cho thấy outcome đó hiếm. Ghi riêng `hard bound`, `typical range` và `case-specific evidence` để không lấy một success story làm forecast.

## 6. Drill A — Ba context, một template

Làm cùng template trong ít nhất ba bối cảnh:

1. **Đời sống:** ước lượng chi phí điện/nước hoặc thời gian đi lại trong một tháng.
2. **Công việc:** ước lượng effort và capacity cho một thay đổi hệ thống.
3. **Thông tin:** ước lượng quy mô claim hoặc population trước khi tin một con số trên mạng.

Với mỗi context, ghi bounds trước, sau đó decomposition, range và threshold hành động. Nếu cùng một assumption làm cả ba estimate nhạy, ghi nó như một recurring failure mode cần đo thêm.

## 7. Output và cách chấm

Lưu một artifact có các ô:

```text
Question / decision:
Unit / population / time horizon:
Lower bound:
Upper bound:
Decomposition:
Base rate:
Central range:
Most sensitive assumption:
Sanity check:
Decision threshold:
What to measure next:
```

Chấm sau khi có dữ liệu bằng ba câu hỏi: estimate có đúng bậc độ lớn không, assumption nào sai, và estimate có đủ để chọn action không. Không chấm chỉ bằng sai số tuyệt đối nếu range ban đầu đã nói rõ uncertainty.

## 8. Failure modes

- **Point estimate giả precision:** một con số có nhiều chữ số không đồng nghĩa evidence tốt.
- **Bounds tùy tiện:** không nói nguồn, vật lý hoặc hợp đồng tạo ra giới hạn.
- **Double-counting:** cùng một population xuất hiện ở hai factor.
- **Đổi denominator giữa các bước:** tử số và mẫu số không còn cùng quần thể.
- **Estimate không nối decision:** tính xong nhưng không biết threshold nào sẽ đổi hành động.

Khi estimate trở thành input của decision material, nối sang [Sensitivity Analysis](./02_sensitivity_analysis_and_uncertainty_decomposition.md), [Forecasting](../forecasting/README.md) và [Risk](../risk/README.md) thay vì ép nó thành fact.

## Template tái sử dụng

```text
Estimate question:
Decision it informs:
Unit / denominator / horizon:
Hard lower and upper bounds:
Factors and ranges:
Base rate / reference class:
Central estimate:
Order-of-magnitude check:
Most sensitive factor:
Threshold for action:
Observed result:
Update rule:
```

Ước lượng tốt không phải estimate luôn đúng; nó làm lộ điều đang được giả định và cho biết phép đo tiếp theo đáng giá đến đâu.

## Connections

- [Problem Framing](../problem-framing/README.md): viết câu hỏi và outcome trước khi tính.
- [Model Selection](../model-selection/README.md): chọn decomposition hoặc model đủ dùng.
- [Sensitivity Analysis](./02_sensitivity_analysis_and_uncertainty_decomposition.md): tìm factor làm conclusion đổi.
- [Mathematics](../../mathematics/README.md): formal probability, statistics và uncertainty.
