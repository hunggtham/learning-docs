# 15 — Quantitative reasoning: bài toán và lời giải đủ bước

PMP không phải kỳ thi toán. Tuy nhiên một số công thức là cách nén reasoning về schedule, cost, risk, investment và communication. Mục tiêu của chapter này không phải biến project manager thành analyst tài chính hay statistician, mà là hiểu mỗi con số đang đại diện cho model nào, assumption nào nằm phía sau, và khi nào arithmetic đúng vẫn có thể dẫn tới decision sai.

Nếu một công thức được nhớ mà không hiểu quantity, hãy quay lại chapter gốc: [Schedule, estimation và flow](./05_schedule_estimation_and_flow.md), [Finance, cost và value](./06_finance_cost_and_value_measurement.md), hoặc [Risk, uncertainty và decision](./08_risk_uncertainty_issues_and_decisions.md).

## 1. Critical Path Method: forward pass, backward pass và float

Giả sử project có network:

```text
A: 3 ngày
B: 4 ngày, sau A
C: 2 ngày, sau A
D: 5 ngày, sau B
E: 3 ngày, sau C
F: 2 ngày, sau cả D và E
```

### Forward pass

Ta chọn convention activity đầu tiên bắt đầu tại thời điểm `0`. Early Start (ES) và Early Finish (EF) được tính từ trái sang phải:

```text
EF = ES + Duration
ES của activity = max(EF của mọi predecessor)
```

A có `ES=0`, `EF=3`.

B và C đều phải chờ A, nên B có `ES=3`, `EF=7`; C có `ES=3`, `EF=5`.

D chờ B nên `ES=7`, `EF=12`. E chờ C nên `ES=5`, `EF=8`.

F phải chờ cả D và E. Vì vậy `ES=max(12,8)=12`, `EF=14`.

Theo network hiện tại, duration sớm nhất của project là 14 ngày.

### Backward pass

Backward pass trả lời câu hỏi ngược lại: mỗi activity có thể kết thúc muộn nhất khi nào mà chưa đẩy project finish date ra sau? Ta bắt đầu từ project finish bằng `LF=14` cho F, rồi đi từ phải sang trái:

```text
LS = LF - Duration
LF của activity = min(LS của mọi successor)
```

F: `LF=14`, `LS=12`.

D và E đều nối vào F nên cả hai có `LF=12`. D có `LS=7`; E có `LS=9`.

B nối vào D nên `LF=7`, `LS=3`. C nối vào E nên `LF=9`, `LS=7`.

A phải hoàn tất trước cả B và C. Vì vậy `LF=min(3,7)=3`, `LS=0`.

### Total float

Total float cho biết activity có thể trượt bao lâu mà chưa làm project finish date trượt theo model hiện tại:

```text
Total Float = LS - ES = LF - EF
```

A, B, D và F đều có float bằng 0. Vì vậy đường:

```text
A → B → D → F
```

là critical path với tổng duration `3+4+5+2=14`.

C có `LS-ES = 7-3 = 4` ngày float. E có `9-5 = 4` ngày float. Đường A-C-E-F dài 10 ngày, ngắn hơn critical path 4 ngày.

Điều quan trọng là float không phải “thời gian rảnh miễn phí”. Dùng hết float của một activity có thể làm downstream flexibility biến mất. Critical path cũng không cố định; khi duration, dependency hoặc resource constraint đổi, critical path có thể đổi theo.

### Free float và total float khác nhau thế nào

Free float là khoảng activity có thể delay mà chưa làm early start của successor trực tiếp bị delay. Total float rộng hơn: delay bao nhiêu trước khi project finish date bị ảnh hưởng. Hai quantity trả lời hai câu hỏi khác nhau. Một activity có thể còn total float nhưng không còn free float, nghĩa là project date chưa trượt nhưng successor sẽ phải bắt đầu muộn hơn.

## 2. Three-point estimation: expected value không phải lời hứa

Một activity có:

```text
Optimistic O = 6 ngày
Most likely M = 9 ngày
Pessimistic P = 18 ngày
```

PERT weighted estimate thường dùng:

```text
E = (O + 4M + P) / 6
  = (6 + 36 + 18) / 6
  = 10 ngày
```

Con số `10` là expected summary theo model, không phải deadline chắc chắn. Nó phụ thuộc trực tiếp vào chất lượng ba estimate đầu vào.

Một approximation thường dùng cho độ phân tán là:

```text
Standard deviation ≈ (P - O) / 6
                   = (18 - 6) / 6
                   = 2 ngày

Variance ≈ 2² = 4
```

Interpretation quan trọng hơn arithmetic: khoảng giữa optimistic và pessimistic càng rộng thì uncertainty càng lớn. Hai activity đều có expected duration 10 ngày nhưng một activity có range 9–11 còn activity kia 3–25 không có cùng risk profile.

Khi cộng variance của nhiều activity trên một path, assumption về independence trở nên quan trọng. Trong project thật, nhiều delay có thể correlated vì cùng vendor, cùng environment hoặc cùng resource. Vì vậy Monte Carlo simulation thường hữu ích hơn một phép cộng thủ công khi schedule uncertainty tương tác phức tạp.

## 3. EVM: trước hết phải hiểu PV, EV và AC

Earned Value Management (EVM / 획득가치관리) chỉ có ý nghĩa khi baseline đủ đáng tin và progress có thể đo tương đối khách quan.

Giả sử:

```text
BAC = 1,000
PV  = 500
EV  = 400
AC  = 450
```

Budget at Completion (BAC) là budget baseline cho toàn bộ planned work. Planned Value (PV) là lượng budgeted work lẽ ra phải hoàn thành tới status date. Earned Value (EV) là budgeted value của work thực sự hoàn thành. Actual Cost (AC) là chi phí thực tế đã bỏ ra.

Điểm dễ nhầm là EV không phải revenue và không phải market value. EV là “giá trị theo baseline” của work hoàn thành.

### Variance

```text
SV = EV - PV = 400 - 500 = -100
CV = EV - AC = 400 - 450 = -50
```

Schedule Variance (SV) âm nghĩa lượng planned work đã earned thấp hơn mức dự kiến tại status date. Cost Variance (CV) âm nghĩa project đã chi nhiều hơn budgeted value của work hoàn thành.

### Performance index

```text
SPI = EV / PV = 0.80
CPI = EV / AC ≈ 0.889
```

SPI dưới 1 là schedule performance thấp hơn baseline. CPI dưới 1 là cost efficiency thấp hơn baseline.

Nếu CPI bằng 0.80, intuition là mỗi 1 đơn vị chi phí chỉ tạo được khoảng 0.80 đơn vị earned value theo baseline. Đây vẫn không phải business value; một project có CPI tốt vẫn có thể làm sai sản phẩm.

### Một giới hạn quan trọng của SPI

Khi project hoàn thành toàn bộ baseline scope, `EV` và `PV` đều tiến tới `BAC`, nên SPI tiến về 1 dù project có thể đã kết thúc muộn. Vì vậy EVM schedule metrics không thay thế schedule network, milestone forecast hoặc time-based evidence. Metric phải được dùng đúng câu hỏi.

## 4. EAC: mỗi công thức encode một assumption khác nhau

Estimate at Completion (EAC) không có một formula đúng cho mọi tình huống.

### Trường hợp 1 — variance hiện tại là bất thường

Nếu phần còn lại dự kiến thực hiện đúng budget rate ban đầu:

```text
EAC = AC + (BAC - EV)
    = 450 + 600
    = 1,050
```

Mental model: phần đã xảy ra được chấp nhận như sunk history; remaining work quay lại efficiency 1.0.

### Trường hợp 2 — cost efficiency hiện tại sẽ tiếp tục

```text
EAC = BAC / CPI
    ≈ 1,000 / 0.889
    ≈ 1,125
```

Mental model: nguyên nhân làm CPI hiện tại thấp không phải one-off và tiếp tục ảnh hưởng phần còn lại.

### Trường hợp 3 — cả cost và schedule inefficiency ảnh hưởng remaining cost

Một approximation thường dùng là:

```text
EAC = AC + (BAC - EV) / (CPI × SPI)
```

Với dữ liệu trên:

```text
CPI × SPI ≈ 0.889 × 0.80 ≈ 0.711
Remaining forecast ≈ 600 / 0.711 ≈ 844
EAC ≈ 450 + 844 ≈ 1,294
```

Formula này tạo forecast bi quan hơn vì giả định schedule inefficiency cũng tiếp tục gây cost pressure. Chỉ dùng khi assumption đó có lý trong context.

### Trường hợp 4 — bottom-up re-estimate

Khi planning basis đã thay đổi mạnh, cách tốt nhất có thể là estimate lại remaining work thay vì ép historical index lên future:

```text
EAC = AC + Bottom-up ETC
```

Đây là ví dụ quan trọng cho nguyên tắc: model đơn giản chỉ hữu ích khi causal mechanism phía sau còn hợp lệ.

## 5. ETC, VAC và TCPI: forecast khác target

Estimate to Complete:

```text
ETC = EAC - AC
```

Nếu `EAC=1,125` và `AC=450`, thì:

```text
ETC = 675
```

Variance at Completion:

```text
VAC = BAC - EAC
    = 1,000 - 1,125
    = -125
```

VAC âm nghĩa forecast hiện tại vượt BAC 125.

To-Complete Performance Index (TCPI) lại hỏi một câu khác: phần work còn lại cần đạt efficiency bao nhiêu để vẫn đạt một target?

Nếu target vẫn là BAC:

```text
TCPI(BAC) = (BAC - EV) / (BAC - AC)
          = 600 / 550
          ≈ 1.091
```

Current CPI khoảng 0.889 nhưng remaining work phải đạt 1.091 để quay về BAC. Gap lớn không tự động chứng minh “không thể”, nhưng nó là evidence rằng target đòi hỏi thay đổi thực chất về cost structure, scope, productivity hoặc execution model.

Nếu organization đã phê duyệt EAC mới, TCPI có thể tính theo target EAC:

```text
TCPI(EAC) = (BAC - EV) / (EAC - AC)
```

Với `EAC=1,125`:

```text
TCPI(EAC) = 600 / 675 ≈ 0.889
```

Điều này khớp current CPI vì chính EAC đó được tạo từ assumption rằng current cost efficiency tiếp tục.

TCPI là feasibility diagnostic, không phải mệnh lệnh rebaseline.

## 6. EMV và decision tree: expected value không thay risk appetite

Expected Monetary Value (EMV / 기대금전가치) nén uncertainty thành probability-weighted monetary effect.

Option A có 30% khả năng tạo benefit 200 triệu, 70% không tạo benefit, implementation cost cố định 30 triệu:

```text
Expected benefit = 0.3 × 200 + 0.7 × 0
                 = 60 triệu

Net EMV = 60 - 30
        = 30 triệu
```

Option B tạo guaranteed net benefit 20 triệu.

Nếu chỉ tối ưu expected money, A cao hơn B. Nhưng organization có thể vẫn chọn B nếu downside của A vượt risk appetite, nếu cash-flow timing khác, nếu compliance consequence không thể quy đổi đơn giản thành tiền, hoặc nếu estimate probability không đủ tin cậy.

Decision tree đặc biệt hữu ích khi decision tạo nhiều branch nối tiếp nhau. Ta tính từ phải sang trái: mỗi chance node lấy expected value của branches; mỗi decision node so options dựa trên objective và constraints. Nhưng probability estimate phải được xem như assumption cần evidence, không phải fact.

## 7. Value of Information: khi nào đáng trả tiền để biết thêm

Giả sử quyết định chọn vendor có thể gây loss 500 triệu nếu integration thất bại. Một prototype hai tuần giá 20 triệu có thể giảm mạnh uncertainty trước commitment lớn.

Câu hỏi hợp lý không phải chỉ “prototype có tốn 20 triệu không?” mà là “20 triệu này mua được bao nhiêu information và làm giảm expected loss bao nhiêu?”.

Nếu prototype giúp tránh một quyết định có expected loss lớn hơn nhiều, test là investment vào information. Đây là lý do spike, pilot, proof of concept và early integration test có thể tạo value dù chưa tạo deliverable cuối.

Đọc tiếp mental model này ở [Risk, uncertainty và decision](./08_risk_uncertainty_issues_and_decisions.md).

## 8. NPV: tiền cùng nominal amount nhưng khác thời điểm không tương đương

Net Present Value (NPV / 순현재가치) dùng discount rate để đưa future cash flow về present value:

```text
NPV = Σ CF_t / (1 + r)^t - Initial Investment
```

Giả sử project cần đầu tư 100 triệu hôm nay và dự kiến tạo 60 triệu cuối năm 1, 60 triệu cuối năm 2. Với discount rate 10%:

```text
PV năm 1 = 60 / 1.10 ≈ 54.55
PV năm 2 = 60 / 1.10² ≈ 49.59

NPV ≈ 54.55 + 49.59 - 100
    ≈ 4.14 triệu
```

NPV dương trong model này nghĩa discounted inflow lớn hơn investment. Nhưng discount rate, cash-flow forecast, option value, strategic fit và non-financial benefit vẫn cần governance judgment.

Không nên so project chỉ bằng nominal total benefit nếu timing và risk khác nhau.

## 9. Flow metrics: Little's Law và forecasting

Trong system đủ ổn định về average arrival/completion rate, Little's Law cho relation:

```text
WIP ≈ Throughput × Cycle Time
```

Nếu trung bình có 20 item đang in progress và throughput là 5 item/tuần:

```text
Cycle Time ≈ 20 / 5 = 4 tuần
```

Equation không nói mỗi item chắc chắn mất 4 tuần. Nó là relation giữa long-run averages dưới điều kiện system tương đối stable.

Nếu WIP tăng lên 40 mà throughput vẫn khoảng 5 item/tuần:

```text
Cycle Time ≈ 40 / 5 = 8 tuần
```

Đây là lý do “bắt đầu nhiều việc hơn” có thể làm feedback chậm hơn dù utilization nhìn cao.

Flow forecasting tốt hơn khi dùng distribution thực tế của cycle time hoặc throughput thay vì chỉ average. Ví dụ thay vì nói “task mất 5 ngày”, có thể nói “85% item tương tự hoàn thành trong 8 ngày”. Đây là probabilistic forecast, không phải guarantee.

## 10. Communication channels: complexity tăng theo cặp, nhưng formula chỉ là upper bound lý thuyết

Nếu mọi người đều có thể giao tiếp trực tiếp theo cặp, số communication channels lý thuyết là:

```text
Channels = n(n - 1) / 2
```

Với 6 người:

```text
6 × 5 / 2 = 15
```

Với 10 người:

```text
10 × 9 / 2 = 45
```

Headcount tăng khoảng 67%, còn possible pairwise channels tăng 200%.

Nhưng formula không chứng minh communication workload thực tế tăng đúng 3 lần. Team structure, interface, role clarity, modularity và communication protocol làm giảm interaction cần thiết. Ý nghĩa của công thức là cho thấy coordination có nonlinear pressure khi group phình lớn.

## 11. Contract reasoning: số tiền chỉ là một phần của risk allocation

Giả sử scope tương đối ổn định, acceptance rõ và seller có historical delivery. Fixed-price có thể chuyển nhiều cost-overrun risk sang seller, nhưng seller thường price uncertainty thành risk premium.

Nếu work là discovery prototype với unknown technical solution, ép fixed-price có thể làm vendor thêm contingency lớn, giảm flexibility hoặc tạo tranh chấp “out of scope”. Time-and-materials với cap, milestone ngắn, acceptance rõ và exit point có thể tạo alignment tốt hơn.

Commercial reasoning không dừng ở “giá thấp nhất”. Cần tính total lifecycle effect: change cost, oversight, integration, lock-in, delay exposure, knowledge transfer, warranty/support và exit cost.

Procurement mechanics sâu hơn nằm ở [Quality, resources và procurement](./07_quality_resources_and_procurement.md).

## 12. Sensitivity analysis: quantity nào thật sự lái outcome

Một forecast có thể chứa nhiều input nhưng chỉ vài input quyết định outcome. Sensitivity analysis thay đổi từng assumption trong range hợp lý để xem output phản ứng mạnh tới đâu.

Ví dụ business case phụ thuộc vào ba assumption: adoption 70%, cost saving 30%, implementation cost 1 tỷ. Nếu thay adoption từ 70% xuống 50% làm NPV chuyển từ dương sang âm, adoption là high-sensitivity variable và đáng đầu tư thêm validation.

Điều này nối quantitative reasoning với project priority: uncertainty nào vừa lớn vừa có sensitivity cao cần attention trước.

## 13. Monte Carlo reasoning: đọc percentile thay vì một deadline duy nhất

Giả sử deterministic network tạo finish date 30/11. Sau khi gán range hợp lý cho các activity và mô phỏng nhiều iteration, kết quả được tóm tắt như sau:

```text
P50 finish = 30/11
P80 finish = 12/12
P90 finish = 20/12
```

Interpretation:

P50 không có nghĩa “50% chắc chắn đúng” theo nghĩa vật lý; nó nghĩa khoảng 50% iteration trong model hoàn thành không muộn hơn 30/11. P80 dùng một confidence target thận trọng hơn và cho mốc 12/12.

Nếu contract penalty bắt đầu 05/12, việc report duy nhất “forecast 30/11” che mất tail exposure. Governance cần biết probability distribution và driver chính.

Giả sử sensitivity cho thấy hai driver lớn nhất là regulatory approval và integration testing. Khi đó response có leverage có thể là early submission, parallel evidence preparation hoặc test environment sớm hơn. Thêm buffer vào documentation task ít nhạy sẽ làm schedule dài nhưng tail gần như không giảm.

Một điểm quan trọng khác là correlation. Nếu integration test và defect-fix duration cùng phụ thuộc một vendor team, model coi chúng độc lập có thể đánh giá P80 quá lạc quan. Simulation tốt không chỉ nhiều iteration; nó cần causal assumptions tốt.

### Reserve từ confidence target

Nếu deterministic/baseline target là 30/11 nhưng governance muốn commit ở mức P80 là 12/12, khoảng 12 ngày chênh lệch có thể được xem như schedule contingency ở level phù hợp. Đây không phải padding tùy tiện; nó là buffer gắn với confidence target và uncertainty model.

Khi response làm distribution thu hẹp, P80 có thể dịch sớm hơn dù P50 gần như không đổi. Điều đó cho thấy mitigation giảm tail risk ngay cả khi expected date không thay nhiều.

## 14. Claim reasoning bằng số: entitlement không tự sinh quantum

Giả sử buyer thay interface specification sau khi seller đã hoàn thành design. Seller yêu cầu:

```text
Time extension: 10 ngày
Additional cost: 80 triệu
```

Project manager không nên bắt đầu bằng câu “80 triệu có hợp lý không?”. Trước hết phải tách ba lớp:

```text
Entitlement → contract có cho relief không?
Causation   → change có thật sự gây delay/cost đó không?
Quantum     → nếu có, mức time/cost hợp lý bao nhiêu?
```

Schedule analysis cho thấy 10 ngày rework chỉ nằm trên path có 4 ngày float, nên modeled project impact là 6 ngày nếu không có effect khác. Cost record cho thấy 50 triệu labor trực tiếp, 10 triệu test environment và 5 triệu approved subcontractor cost. Phần 15 triệu còn lại là overhead allocation chưa có basis rõ.

Khi đó evidence hiện tại không hỗ trợ đơn giản “10 ngày + 80 triệu”. Nó hỗ trợ một discussion tinh hơn: entitlement có thể tồn tại, schedule impact modeled khoảng 6 ngày, direct substantiated cost hiện khoảng 65 triệu, còn overhead cần contract basis/evidence.

Nếu cùng giai đoạn seller cũng chậm 3 ngày do staffing riêng, concurrent delay phải được specialist phân tích. Arithmetic không tự quyết legal entitlement; nó làm dispute có structure thay vì bargaining từ hai con số cực đoan.

## 15. Một worked scenario tích hợp

Project có `BAC=2,000`. Tại status date:

```text
PV = 1,000
EV = 800
AC = 1,000
```

Ta có:

```text
SPI = 800 / 1,000 = 0.80
CPI = 800 / 1,000 = 0.80
SV  = 800 - 1,000 = -200
CV  = 800 - 1,000 = -200
```

Project đang behind baseline work và cost efficiency thấp hơn plan.

Nếu CPI tiếp tục:

```text
EAC = BAC / CPI
    = 2,000 / 0.80
    = 2,500
```

Nếu cả cost và schedule inefficiency tiếp tục ảnh hưởng remaining cost:

```text
EAC = AC + (BAC - EV) / (CPI × SPI)
    = 1,000 + 1,200 / 0.64
    = 1,000 + 1,875
    = 2,875
```

Hai forecast khác nhau 375 vì assumption khác nhau. PM không nên chọn formula tạo con số “đẹp” hơn; phải hỏi causal evidence. Nếu delay đến từ một approval one-off đã resolved, SPI có thể không tiếp tục kéo cost. Nếu team đang overtime liên tục vì schedule compression, combined efficiency model có thể realistic hơn.

Nếu management vẫn yêu cầu hoàn tất với BAC 2,000:

```text
TCPI(BAC) = (2,000 - 800) / (2,000 - 1,000)
          = 1,200 / 1,000
          = 1.20
```

Remaining work phải đạt CPI 1.20 trong khi historical CPI hiện tại chỉ 0.80. Trước khi cam kết target, cần evidence về scope reduction, productivity improvement, vendor renegotiation hoặc structural change đủ lớn để giải thích jump đó.

Đây chính là quantitative reasoning: phép tính tạo signal; root cause và governance quyết định action.

## 16. Robustness check: decision có đứng vững khi input thay đổi không?

Một model không chỉ cần cho ra con số; nó phải đủ **robust** để hỗ trợ decision. Nếu decision đảo chiều chỉ vì một input thay đổi rất nhỏ trong range hợp lý, organization không nên trình bày recommendation như chắc chắn.

Giả sử Option A có NPV `+8` triệu ở adoption 70%, nhưng adoption giảm nhẹ xuống 65% đã làm NPV âm. Khi đó conclusion “NPV dương nên làm” che một boundary rất gần. Decision cần thêm evidence về adoption, option giảm exposure hoặc staged investment. Ngược lại, nếu NPV vẫn dương ở nhiều scenario hợp lý và chỉ âm trong extreme case, recommendation robust hơn.

Robustness check có thể đơn giản bằng cách thay các assumption quan trọng trong range plausible rồi hỏi:

```text
Input nào làm decision đổi?
Threshold nằm gần current estimate không?
Nếu estimate sai một mức hợp lý, consequence là gì?
Có option nào giảm downside mà giữ upside không?
```

Đây là cầu nối giữa sensitivity analysis và governance. Sensitivity nói input nào ảnh hưởng output; robustness hỏi ảnh hưởng đó có đủ để thay quyết định không.

## 17. Decision-reversal threshold: tìm boundary thay vì tranh luận một con số

Nhiều cuộc họp mắc kẹt ở việc “estimate đúng là 60 hay 65?”. Câu hỏi mạnh hơn thường là: **giá trị bao nhiêu thì decision đổi?**

Ví dụ vendor A rẻ hơn 100 triệu nhưng có expected switching/lock-in cost chưa chắc chắn. Nếu analysis cho thấy vendor A chỉ còn ưu thế khi future switching cost dưới 40 triệu, thì `40` là decision-reversal threshold quan trọng hơn việc cố đo switching cost chính xác tới từng triệu ngay lập tức.

Tương tự, nếu project chỉ đạt business case khi adoption trên 62%, measurement plan nên ưu tiên evidence quanh vùng đó. Nếu adoption estimate hiện là 85%, thêm nghiên cứu để phân biệt 84% hay 86% có thể ít value. Nếu estimate là 60–65%, cùng nghiên cứu đó có Value of Information cao hơn vì có thể đổi quyết định.

Threshold thinking giúp allocation của analysis effort dựa trên **decision sensitivity**, không dựa trên thói quen “càng nhiều data càng tốt”.

## 18. Model risk: con số có thể chính xác theo model nhưng model sai cấu trúc

Model risk xảy ra khi arithmetic đúng nhưng representation của reality không đủ đúng. Có ít nhất bốn nguồn thường gặp.

Thứ nhất là **data risk**: actual input sai, thiếu hoặc outdated. Thứ hai là **parameter risk**: probability, duration hoặc cost range được estimate quá tự tin. Thứ ba là **structural risk**: model bỏ dependency/correlation, assumption nonlinear hoặc feedback loop quan trọng. Thứ tư là **usage risk**: model vốn phù hợp cho planning nhưng bị dùng như commitment tuyệt đối hoặc performance score.

Ví dụ Monte Carlo với 100.000 iteration vẫn cho kết quả yếu nếu network bỏ một regulatory dependency. EAC tính đúng tới ba chữ số thập phân vẫn không hữu ích nếu baseline EV không phản ánh completion thật. NPV chính xác về discounting vẫn sai decision nếu cash-flow model bỏ adoption cost hoặc decommission obligation.

Vì vậy review quantitative model nên hỏi không chỉ “formula đúng không?” mà còn “model boundary có chứa driver tạo outcome không?”. Precision không bù được omission.

## 19. Forecast calibration: model phải học từ sai số lịch sử

Một forecast có thể đúng một lần do may mắn. Calibration xem confidence statement có khớp actual frequency qua nhiều lần không. Nếu team liên tục báo P80 nhưng actual miss target thường xuyên hơn nhiều, input distribution, dependency hoặc correlation đang bị underestimate.

Một practice đơn giản là giữ version của forecast theo status date thay vì overwrite:

```text
Status date | Forecast | Confidence | Actual | Main reason for miss
```

Sau nhiều milestone, organization có thể phát hiện systematic optimism, vendor-specific tail hoặc loại work nào model luôn understate. Đây là dữ liệu để sửa model, không chỉ đánh giá cá nhân estimator.

Calibration cũng giúp tránh hindsight bias. Khi actual xảy ra, con số cũ phải được giữ để xem team đã biết gì lúc ra decision, thay vì âm thầm sửa forecast history cho giống outcome.

## 20. Cross-metric consistency: các con số có kể cùng một câu chuyện không?

Một dashboard có thể chứa nhiều metric “đúng” nhưng mutually inconsistent. Ví dụ SPI gần 1 trong khi milestone forecast trượt mạnh; velocity tăng trong khi cycle time cũng tăng; percent complete 90% trong khi UAT pass rate 50%; CPI tốt nhưng committed cost chưa vào AC rất lớn.

Mâu thuẫn không tự động nghĩa một metric sai. Chúng có thể đo state khác nhau. Nhưng inconsistency là signal cần giải thích trước khi governance dùng dashboard.

Một discipline hữu ích là hỏi mỗi metric:

```text
Nó đo stock, flow, efficiency hay outcome?
Nó nhìn quá khứ, hiện tại hay forecast?
Denominator/baseline là gì?
Có lag hoặc committed-but-not-realized state nào chưa phản ánh không?
```

Cross-metric reasoning ngăn việc chọn đúng một con số thuận lợi để kể narrative mong muốn. Quantitative evidence mạnh khi nhiều independent view converge hoặc khi divergence được giải thích bằng mechanism rõ.

## 21. Unit và dimensional sanity check

Nhiều lỗi không cần công thức nâng cao để phát hiện. Chỉ cần hỏi unit có hợp lý không. CPI/SPI là ratio không có đơn vị. Cycle time có đơn vị thời gian. Throughput là item/time. NPV là tiền. Probability nằm trong range hợp lệ. Một phép cộng giữa percentage và tiền trực tiếp thường vô nghĩa nếu chưa transform về cùng quantity.

Sanity check cũng áp dụng cho magnitude. Nếu thêm một engineer được forecast rút 50% schedule trong work có nhiều external dependency, model cần giải thích causal mechanism. Nếu cost saving vượt tổng cost hiện tại, denominator hoặc time horizon có thể sai.

Trước khi tin một output phức tạp, hãy kiểm tra đơn vị, order of magnitude và boundary. Đây là cách rẻ nhất để bắt model error.

## Formula map theo meaning

```text
CPM
EF = ES + Duration
LS = LF - Duration
Total Float = LS - ES = LF - EF

PERT
Expected duration = (O + 4M + P) / 6
Std. deviation ≈ (P - O) / 6
Variance ≈ Std. deviation²

EVM state
SV  = EV - PV
CV  = EV - AC
SPI = EV / PV
CPI = EV / AC

EVM forecast
EAC atypical variance = AC + (BAC - EV)
EAC cost efficiency continues = BAC / CPI
EAC cost + schedule effect = AC + (BAC - EV) / (CPI × SPI)
ETC = EAC - AC
VAC = BAC - EAC
TCPI(BAC) = (BAC - EV) / (BAC - AC)
TCPI(EAC) = (BAC - EV) / (EAC - AC)

Risk / finance
EMV = Probability × Monetary Impact
NPV = Σ CF_t / (1 + r)^t - Initial Investment

Flow / communication
WIP ≈ Throughput × Cycle Time
Channels = n(n - 1) / 2
```

Monte Carlo percentile, claim analysis và sensitivity không có một single formula đáng học thuộc. Chúng là reasoning framework: define inputs, assumptions, dependency/correlation, run or compare scenarios, rồi interpret output theo decision threshold.

Formula map này chỉ nên dùng sau khi bạn có thể giải thích quantity bằng lời. Nếu không thể nói EV khác AC thế nào hoặc vì sao một EAC formula phù hợp hơn formula khác, hãy quay lại mental model trước arithmetic.

## Mental model

> Một phép tính PMP luôn là một model thu gọn của reality. Hãy đọc quantity, assumption, uncertainty, correlation, robustness và decision consequence trước khi bấm máy. Con số đúng không cứu được một model sai; model tốt cũng chưa đủ nếu decision không đứng vững khi input thay đổi trong range hợp lý.

Sau chapter này, đọc [End-to-end case studies](./16_end_to_end_case_studies.md) để thấy schedule, finance, risk, procurement và governance cùng tương tác trong một project thực.