# Estimation & Sanity Checks — Ước lượng trước khi tin vào con số

Một con số có thể trông rất chính xác mà vẫn sai từ gốc nếu unit, scale, denominator hoặc assumption sai. Vì vậy estimation không chỉ dùng khi “không có calculator”; nó là lớp kiểm tra trước khi ta chấp nhận output của model, spreadsheet, AI, dashboard hoặc chính phép tính của mình.

Mục tiêu của chapter này là luyện một kỹ năng có thể lặp lại: **tạo một estimate độc lập đủ thô để phát hiện sai số lớn, rồi mới đi vào precision**. Formal arithmetic, probability và modeling tiếp tục thuộc [Mathematics](../../mathematics/README.md); ở đây ta tập trung vào workflow thực dụng.

## 1. Sanity check giải quyết failure mode nào?

Có bốn lỗi thường xuyên tạo ra kết quả “có vẻ hợp lý”:

- sai bậc độ lớn (order of magnitude);
- sai đơn vị;
- denominator không đúng;
- model ngầm giả định một capacity/rate không thể xảy ra trong thực tế.

Ví dụ một API được báo xử lý `12,000,000 request/second`. Trước khi tranh luận benchmark, chỉ cần hỏi số instance, request size, network throughput và CPU budget đã có thể thấy estimate có nằm trong vùng khả thi hay không.

Điểm chốt: **sanity check không cần đúng chính xác; nó cần đủ độc lập để bắt được kết quả vô lý**.

## 2. Fermi estimation: chia câu hỏi lớn thành đại lượng nhỏ

Fermi estimation (ước lượng Fermi / 페르미 추정) biến một quantity khó biết trực tiếp thành tích hoặc tổng của các quantity dễ ước lượng hơn.

Ví dụ muốn ước lượng số cốc cà phê một khu văn phòng tiêu thụ mỗi ngày:

```text
số người
× tỷ lệ uống cà phê
× số cốc trung bình/người/ngày
```

Ta không cần biết từng người. Giá trị của decomposition nằm ở việc expose assumptions: nếu estimate sai, ta biết nên kiểm tra population, participation rate hay frequency.

Workflow:

```text
Question
→ choose decomposition
→ estimate each component
→ compute rough result
→ test bounds
→ compare with external anchor
→ update only sensitive assumptions
```

## 3. Order of magnitude — trước hết hỏi “cỡ nào?”

Trước precision, xác định bậc độ lớn:

```text
10^0     đơn vị
10^3     nghìn
10^6     triệu
10^9     tỷ
```

Nếu hai phương pháp độc lập cho kết quả `10^5` và `10^6`, có thể vẫn cùng vùng hợp lý. Nếu một bên ra `10^5`, bên kia `10^9`, không nên trung bình hai số; phải tìm assumption hoặc unit bị sai.

Một estimate tốt thường bắt đầu bằng câu:

> Kết quả hợp lý phải nằm quanh hàng chục, hàng nghìn, hàng triệu hay hàng tỷ?

Câu hỏi này đặc biệt hữu ích khi đọc market size, storage capacity, traffic, budget và population statistics.

## 4. Unit check — công cụ bắt lỗi rẻ nhất

Đơn vị là constraint logic của phép tính.

Ví dụ:

```text
requests / second
× bytes / request
= bytes / second
```

Nếu cuối cùng bạn gọi kết quả là “GB storage” mà chưa nhân với thời gian, phép tính chưa thể đúng về dimension.

Một habit hữu ích:

```text
number + unit
```

thay vì chỉ ghi `500`, `2.4`, `80%`.

Với finance cũng tương tự:

```text
KRW / month
× month
= KRW
```

Không trộn annual rate với monthly cash flow nếu chưa chuyển cùng time basis.

## 5. Lower bound và upper bound

Khi input mơ hồ, đừng giả precision. Hãy tạo range bằng bounds.

Ví dụ server có thể xử lý mỗi request trong khoảng 20–50 ms CPU-equivalent và có 16 cores. Ta chưa cần benchmark chính xác để biết một single instance không thể có throughput vô hạn.

Bound reasoning hỏi:

```text
Điều gì chắc chắn không thể thấp hơn?
Điều gì chắc chắn không thể cao hơn?
```

Bounds đặc biệt hữu ích khi estimate:

- thời gian project;
- storage;
- bandwidth;
- market size;
- cost;
- energy use;
- queue capacity.

## 6. Capacity check

Một estimate thường bị giới hạn bởi bottleneck vật lý hoặc operational.

Ví dụ một nhà hàng có:

```text
40 seats
× 3 table turns / evening
≈ 120 seat-services / evening
```

Nếu báo cáo nói phục vụ 2,000 khách dine-in trong một buổi tối, cần có explanation rất đặc biệt: nhiều tầng, turnover cực cao, standing service, event space hoặc metric đang không phải dine-in customers.

Capacity check là bridge tự nhiên sang [Systems Thinking](../systems-thinking/README.md): throughput cuối cùng bị giới hạn bởi bottleneck, queue, utilization và recovery time.

## 7. Denominator check

Phần trăm không có denominator thường khó đánh giá.

```text
“tăng 50%”
```

có thể là:

```text
2 → 3
200 → 300
2 million → 3 million
```

Khi đọc claim, hỏi:

```text
50% của cái gì?
trên population nào?
trong time window nào?
```

Đây là nơi estimation nối sang [Statistics for Life](../statistics-for-life/README.md) và [Critical Thinking](../critical-thinking/README.md).

## 8. Back-of-the-envelope trước spreadsheet lớn

Nếu một business case dùng spreadsheet 20 sheet, hãy tạo một estimate 3–5 dòng trước.

Ví dụ:

```text
annual revenue
≈ customers
× purchases/customer/year
× average order value
```

Sau đó spreadsheet chi tiết phải giải thích vì sao nó lệch rough model, chứ không được mặc nhiên “đúng hơn” chỉ vì nhiều cell hơn.

Principle:

> Complexity nên giải thích deviation, không được che mất baseline.

## 9. Triangulation — dùng ít nhất hai đường độc lập

Một estimate mạnh hơn khi có hai route gần độc lập.

Ví dụ market size:

```text
Top-down:
population × adoption × spend/user

Bottom-up:
number of sellers × sales/seller
```

Nếu hai route hội tụ cùng vùng, confidence tăng. Nếu lệch xa, chính discrepancy là information: có thể definition khác nhau, missing segment, double counting hoặc assumption sai.

## 10. Sensitivity trước precision

Không phải input nào cũng đáng research thêm.

Nếu result gần như không đổi khi assumption X dao động ±50%, đừng tốn một ngày để refine X. Hãy tìm variable mà thay đổi nhỏ làm conclusion đổi.

Handoff: [Sensitivity Analysis & Uncertainty Decomposition](./02_sensitivity_analysis_and_uncertainty_decomposition.md).

## 11. Drill A — Ước lượng không tra cứu trước

Chọn một câu hỏi có thể resolve sau:

- một tòa nhà văn phòng dùng bao nhiêu điện mỗi ngày;
- một ứng dụng lưu bao nhiêu GB log mỗi tháng;
- một ga metro xử lý bao nhiêu hành khách trong giờ cao điểm;
- một team cần bao nhiêu ngày để review 300 pull requests.

Trước khi tra dữ liệu:

```text
Question:
Decomposition:
Assumptions:
Lower bound:
Central estimate:
Upper bound:
Most sensitive variable:
Confidence:
```

Sau đó mới tìm source/reference value và ghi ratio:

```text
actual / estimate
```

Không sửa estimate ban đầu.

## 12. Drill B — Sanity-check một claim có sẵn

Lấy một chart, business report, AI answer hoặc news claim có con số.

Kiểm tra theo thứ tự:

```text
unit
→ denominator
→ order of magnitude
→ capacity constraint
→ time basis
→ independent rough estimate
```

Output:

```text
Claim:
What would make it plausible:
Rough independent estimate:
Main discrepancy:
Likely source of error:
Need deeper verification? yes/no
```

Mục tiêu không phải chứng minh claim sai; mục tiêu là quyết định **claim nào đáng bỏ thêm công sức để verify**.

## 13. Drill C — Engineering sizing

Ví dụ sizing log storage:

```text
requests/day
× logs/request
× bytes/log
× retention days
× replication factor
```

Sau estimate, kiểm tra:

- peak vs average;
- compression;
- retries/duplicates;
- retention policy;
- safety margin.

So với actual telemetry sau một tuần và update assumptions.

## 14. Score và feedback loop

Lưu estimation log:

| Question | Estimate | Range | Actual/reference | Error ratio | Main miss |
|---|---:|---:|---:|---:|---|
| A | 100 | 60–180 | 140 | 1.4× | frequency |
| B | 5 TB | 2–8 TB | 18 TB | 3.6× | duplicate logs |

Không kỳ vọng error ratio luôn gần 1. Điều cần theo dõi qua nhiều bài là:

- range có cover actual thường xuyên hơn không;
- decomposition có expose đúng variables hơn không;
- lỗi unit/denominator có giảm không;
- bạn có nhận ra uncertainty trước khi tra answer không.

## 15. Failure modes

### Precision theater

`12,483,921` không tốt hơn `~12 million` nếu inputs chỉ là estimates thô.

### Anchoring vào số đầu tiên

Nếu đã đọc answer trước, estimate độc lập mất giá trị. Hãy estimate trước khi search khi có thể.

### Double counting

Decomposition theo segment dễ cộng một entity nhiều lần. Luôn hỏi các buckets có mutually exclusive không.

### Ignoring tails

Rough average không thay stress test. Với capacity/risk, cần peak và adverse scenario.

### Treating estimate as evidence

Estimate là model, không phải observation. Khi quyết định high-stakes, phải handoff sang actual measurement hoặc domain evidence.

## Reusable template

```text
# Estimate — YYYY-MM-DD

Question:
Why this estimate matters:
Unit:
Reference class / anchors:

Decomposition:
- A:
- B:
- C:

Lower bound:
Central estimate:
Upper bound:
Most sensitive assumptions:
Capacity constraints:
Independent second route:
Confidence:

Reference / actual after estimation:
Error ratio:
What caused the miss:
Rule to update next time:
```

## Connections

- [Problem Framing](../problem-framing/README.md): xác định quantity cần estimate.
- [Statistics for Life](../statistics-for-life/README.md): denominator, sampling và noisy estimates.
- [Forecasting](../forecasting/README.md): biến estimate thành range có resolution rule.
- [Sensitivity Analysis](./02_sensitivity_analysis_and_uncertainty_decomposition.md): tìm input quyết định conclusion.
- [Systems Thinking](../systems-thinking/README.md): capacity, bottleneck và throughput.
- [Decision Making](../decision-making/README.md): xác định khi rough estimate đã đủ để hành động.

Estimation tốt không thay dữ liệu thật. Nó làm một việc khác nhưng rất quan trọng: **cho bạn một baseline độc lập để biết khi nào một con số xứng đáng được tin, nghi ngờ hoặc kiểm tra sâu hơn**.