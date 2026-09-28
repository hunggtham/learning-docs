# 15 — Quantitative lập luận (reasoning / 추론): bài toán và lời giải đủ bước

> **Mạch đọc:** Đặt **15 — Quantitative lập luận (reasoning / 추론): bài toán và lời giải đủ bước** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. đường găng (critical path / 임계 경로) phương thức (method / 메서드): forward pass, backward pass và float** sang **Forward pass**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


PMP không phải kỳ thi toán. Tuy nhiên một số công thức là cách nén lập luận (reasoning / 추론) về schedule, chi phí (cost / 비용), rủi ro (risk / 위험), investment và communication. Mục tiêu của chapter này không phải biến dự án (project / 프로젝트) manager thành analyst tài chính hay statistician, mà là hiểu mỗi con số đang đại diện cho mô hình (model / 모델) nào, giả định (assumption / 가정) nào nằm phía sau, và khi nào arithmetic đúng vẫn có thể dẫn tới quyết định (decision / 결정) sai.

Nếu một công thức được nhớ mà không hiểu quantity, hãy quay lại chapter gốc: [Schedule, estimation và flow](./05_schedule_estimation_and_flow.md), [Finance, cost và value](./06_finance_cost_and_value_measurement.md), hoặc [Risk, uncertainty và decision](./08_risk_uncertainty_issues_and_decisions.md).

## 1. đường găng (critical path / 임계 경로) phương thức (method / 메서드): forward pass, backward pass và float

Giả sử dự án (project / 프로젝트) có mạng (network / 네트워크):

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

Theo mạng (network / 네트워크) hiện tại, duration sớm nhất của dự án (project / 프로젝트) là 14 ngày.

### Backward pass

Backward pass trả lời câu hỏi ngược lại: mỗi activity có thể kết thúc muộn nhất khi nào mà chưa đẩy dự án (project / 프로젝트) finish date ra sau? Ta bắt đầu từ dự án (project / 프로젝트) finish bằng `LF=14` cho F, rồi đi từ phải sang trái:

```text
LS = LF - Duration
LF của activity = min(LS của mọi successor)
```

F: `LF=14`, `LS=12`.

D và E đều nối vào F nên cả hai có `LF=12`. D có `LS=7`; E có `LS=9`.

B nối vào D nên `LF=7`, `LS=3`. C nối vào E nên `LF=9`, `LS=7`.

A phải hoàn tất trước cả B và C. Vì vậy `LF=min(3,7)=3`, `LS=0`.

### Total float

Total float cho biết activity có thể trượt bao lâu mà chưa làm dự án (project / 프로젝트) finish date trượt theo mô hình (model / 모델) hiện tại:

```text
Total Float = LS - ES = LF - EF
```

A, B, D và F đều có float bằng 0. Vì vậy đường:

```text
A → B → D → F
```

là đường găng (critical path / 임계 경로) với tổng duration `3+4+5+2=14`.

C có `LS-ES = 7-3 = 4` ngày float. E có `9-5 = 4` ngày float. Đường A-C-E-F dài 10 ngày, ngắn hơn đường găng (critical path / 임계 경로) 4 ngày.

Điều quan trọng là float không phải “thời gian rảnh miễn phí”. Dùng hết float của một activity có thể làm downstream flexibility biến mất. đường găng (critical path / 임계 경로) cũng không cố định; khi duration, phụ thuộc (dependency / 의존성) hoặc tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건) đổi, đường găng (critical path / 임계 경로) có thể đổi theo.

### Free float và total float khác nhau thế nào

Free float là khoảng activity có thể delay mà chưa làm early start của successor trực tiếp bị delay. Total float rộng hơn: delay bao nhiêu trước khi dự án (project / 프로젝트) finish date bị ảnh hưởng. Hai quantity trả lời hai câu hỏi khác nhau. Một activity có thể còn total float nhưng không còn free float, nghĩa là dự án (project / 프로젝트) date chưa trượt nhưng successor sẽ phải bắt đầu muộn hơn.

## 2. Three-point estimation: expected giá trị (value / 값) không phải lời hứa

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

Con số `10` là expected summary theo mô hình (model / 모델), không phải deadline chắc chắn. Nó phụ thuộc trực tiếp vào chất lượng ba estimate đầu vào.

Một approximation thường dùng cho độ phân tán là:

```text
Standard deviation ≈ (P - O) / 6
                   = (18 - 6) / 6
                   = 2 ngày

Variance ≈ 2² = 4
```

Interpretation quan trọng hơn arithmetic: khoảng giữa optimistic và pessimistic càng rộng thì bất định (uncertainty / 불확실성) càng lớn. Hai activity đều có expected duration 10 ngày nhưng một activity có phạm vi (range / 범위) 9–11 còn activity kia 3–25 không có cùng rủi ro (risk / 위험) profile.

Khi cộng variance của nhiều activity trên một đường dẫn (path / 경로), giả định (assumption / 가정) về independence trở nên quan trọng. Trong dự án (project / 프로젝트) thật, nhiều delay có thể correlated vì cùng vendor, cùng môi trường (environment / 환경) hoặc cùng tài nguyên (resource / 자원). Vì vậy Monte Carlo simulation thường hữu ích hơn một phép cộng thủ công khi schedule bất định (uncertainty / 불확실성) tương tác phức tạp.

## 3. EVM: trước hết phải hiểu PV, EV và AC

Earned giá trị (value / 값) Management (EVM / 획득가치관리) chỉ có ý nghĩa khi baseline đủ đáng tin và progress có thể đo tương đối khách quan.

Giả sử:

```text
BAC = 1,000
PV  = 500
EV  = 400
AC  = 450
```

Ngân sách (budget / 예산) at Completion (BAC) là ngân sách (budget / 예산) baseline cho toàn bộ planned công việc (work / 작업). Planned giá trị (value / 값) (PV) là lượng budgeted công việc (work / 작업) lẽ ra phải hoàn thành tới status date. Earned giá trị (value / 값) (EV) là budgeted giá trị (value / 값) của công việc (work / 작업) thực sự hoàn thành. Actual chi phí (cost / 비용) (AC) là chi phí thực tế đã bỏ ra.

Điểm dễ nhầm là EV không phải revenue và không phải giá trị thị trường (market value / 시장 가치). EV là “giá trị theo baseline” của công việc (work / 작업) hoàn thành.

### Variance

```text
SV = EV - PV = 400 - 500 = -100
CV = EV - AC = 400 - 450 = -50
```

Schedule Variance (SV) âm nghĩa lượng planned công việc (work / 작업) đã earned thấp hơn mức dự kiến tại status date. chi phí (cost / 비용) Variance (CV) âm nghĩa dự án (project / 프로젝트) đã chi nhiều hơn budgeted giá trị (value / 값) của công việc (work / 작업) hoàn thành.

### Hiệu năng (performance / 성능) chỉ mục (index / 인덱스)

```text
SPI = EV / PV = 0.80
CPI = EV / AC ≈ 0.889
```

SPI dưới 1 là schedule hiệu năng (performance / 성능) thấp hơn baseline. CPI dưới 1 là chi phí (cost / 비용) efficiency thấp hơn baseline.

Nếu CPI bằng 0.80, intuition là mỗi 1 đơn vị chi phí chỉ tạo được khoảng 0.80 đơn vị earned giá trị (value / 값) theo baseline. Đây vẫn không phải nghiệp vụ (business / 비즈니스) giá trị (value / 값); một dự án (project / 프로젝트) có CPI tốt vẫn có thể làm sai sản phẩm.

### Một giới hạn quan trọng của SPI

Khi dự án (project / 프로젝트) hoàn thành toàn bộ baseline phạm vi (scope / 범위), `EV` và `PV` đều tiến tới `BAC`, nên SPI tiến về 1 dù dự án (project / 프로젝트) có thể đã kết thúc muộn. Vì vậy EVM schedule metrics không thay thế schedule mạng (network / 네트워크), milestone forecast hoặc time-based bằng chứng (evidence / 증거). chỉ số (metric / 지표) phải được dùng đúng câu hỏi.

## 4. EAC: mỗi công thức encode một giả định (assumption / 가정) khác nhau

Estimate at Completion (EAC) không có một formula đúng cho mọi tình huống.

### Trường hợp 1 — variance hiện tại là bất thường

Nếu phần còn lại dự kiến thực hiện đúng ngân sách (budget / 예산) tỷ lệ (rate / 비율) ban đầu:

```text
EAC = AC + (BAC - EV)
    = 450 + 600
    = 1,050
```

Mô hình tư duy (mental model / 사고 모델): phần đã xảy ra được chấp nhận như sunk lịch sử (history / 이력); remaining công việc (work / 작업) quay lại efficiency 1.0.

### Trường hợp 2 — chi phí (cost / 비용) efficiency hiện tại sẽ tiếp tục

```text
EAC = BAC / CPI
    ≈ 1,000 / 0.889
    ≈ 1,125
```

Mô hình tư duy (mental model / 사고 모델): nguyên nhân làm CPI hiện tại thấp không phải one-off và tiếp tục ảnh hưởng phần còn lại.

### Trường hợp 3 — cả chi phí (cost / 비용) và schedule inefficiency ảnh hưởng remaining chi phí (cost / 비용)

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

Formula này tạo forecast bi quan hơn vì giả định schedule inefficiency cũng tiếp tục gây chi phí (cost / 비용) pressure. Chỉ dùng khi giả định (assumption / 가정) đó có lý trong ngữ cảnh (context / 맥락).

### Trường hợp 4 — bottom-up re-estimate

Khi planning basis đã thay đổi mạnh, cách tốt nhất có thể là estimate lại remaining công việc (work / 작업) thay vì ép historical chỉ mục (index / 인덱스) lên future:

```text
EAC = AC + Bottom-up ETC
```

Đây là ví dụ quan trọng cho nguyên tắc: mô hình (model / 모델) đơn giản chỉ hữu ích khi nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘) phía sau còn hợp lệ.

## 5. ETC, VAC và TCPI: forecast khác mục tiêu (target / 대상)

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

To-Complete hiệu năng (performance / 성능) chỉ mục (index / 인덱스) (TCPI) lại hỏi một câu khác: phần công việc (work / 작업) còn lại cần đạt efficiency bao nhiêu để vẫn đạt một mục tiêu (target / 대상)?

Nếu mục tiêu (target / 대상) vẫn là BAC:

```text
TCPI(BAC) = (BAC - EV) / (BAC - AC)
          = 600 / 550
          ≈ 1.091
```

Hiện tại (current / 현재) CPI khoảng 0.889 nhưng remaining công việc (work / 작업) phải đạt 1.091 để quay về BAC. Gap lớn không tự động chứng minh “không thể”, nhưng nó là bằng chứng (evidence / 증거) rằng mục tiêu (target / 대상) đòi hỏi thay đổi thực chất về chi phí (cost / 비용) cấu trúc (structure / 구조), phạm vi (scope / 범위), productivity hoặc mô hình thực thi (execution model / 실행 모델).

Nếu organization đã phê duyệt EAC mới, TCPI có thể tính theo mục tiêu (target / 대상) EAC:

```text
TCPI(EAC) = (BAC - EV) / (EAC - AC)
```

Với `EAC=1,125`:

```text
TCPI(EAC) = 600 / 675 ≈ 0.889
```

Điều này khớp hiện tại (current / 현재) CPI vì chính EAC đó được tạo từ giả định (assumption / 가정) rằng hiện tại (current / 현재) chi phí (cost / 비용) efficiency tiếp tục.

TCPI là feasibility diagnostic, không phải mệnh lệnh rebaseline.

## 6. EMV và cây quyết định (decision tree / 의사결정 트리): expected giá trị (value / 값) không thay rủi ro (risk / 위험) appetite

Expected Monetary giá trị (value / 값) nén bất định (uncertainty / 불확실성) thành probability-weighted monetary tác động (effect / 효과).

Option A có 30% khả năng tạo benefit 200 triệu, 70% không tạo benefit, hiện thực (implementation / 구현) chi phí (cost / 비용) cố định 30 triệu:

```text
Expected benefit = 0.3 × 200 + 0.7 × 0
                 = 60 triệu

Net EMV = 60 - 30
        = 30 triệu
```

Option B tạo guaranteed net benefit 20 triệu.

Nếu chỉ tối ưu expected money, A cao hơn B. Nhưng organization có thể vẫn chọn B nếu downside của A vượt rủi ro (risk / 위험) appetite, nếu cash-flow timing khác, nếu compliance consequence không thể quy đổi đơn giản thành tiền, hoặc nếu estimate xác suất (probability / 확률) không đủ tin cậy.

Cây quyết định (decision tree / 의사결정 트리) đặc biệt hữu ích khi quyết định (decision / 결정) tạo nhiều branch nối tiếp nhau. Ta tính từ phải sang trái: mỗi chance nút (node / 노드) lấy expected giá trị (value / 값) của branches; mỗi quyết định (decision / 결정) nút (node / 노드) so options dựa trên mục tiêu (objective / 목표) và các ràng buộc (constraints / 제약조건들). Nhưng xác suất (probability / 확률) estimate phải được xem như giả định (assumption / 가정) cần bằng chứng (evidence / 증거), không phải fact.

## 7. giá trị (value / 값) of thông tin (information / 정보): khi nào đáng trả tiền để biết thêm

Giả sử quyết định chọn vendor có thể gây mất mát (loss / 손실) 500 triệu nếu tích hợp (integration / 통합) thất bại. Một prototype hai tuần giá 20 triệu có thể giảm mạnh bất định (uncertainty / 불확실성) trước commitment lớn.

Câu hỏi hợp lý không phải chỉ “prototype có tốn 20 triệu không?” mà là “20 triệu này mua được bao nhiêu thông tin (information / 정보) và làm giảm expected mất mát (loss / 손실) bao nhiêu?”.

Nếu prototype giúp tránh một quyết định có expected mất mát (loss / 손실) lớn hơn nhiều, kiểm thử (test / 테스트) là investment vào thông tin (information / 정보). Đây là lý do spike, pilot, proof of concept và early kiểm thử tích hợp (integration test / 통합 테스트) có thể tạo giá trị (value / 값) dù chưa tạo deliverable cuối.

Đọc tiếp mô hình tư duy (mental model / 사고 모델) này ở [Risk, uncertainty và decision](./08_risk_uncertainty_issues_and_decisions.md).

## 8. NPV: tiền cùng nominal amount nhưng khác thời điểm không tương đương

Net Present giá trị (value / 값) dùng discount tỷ lệ (rate / 비율) để đưa future cash luồng (flow / 흐름) về present giá trị (value / 값):

```text
NPV = Σ CF_t / (1 + r)^t - Initial Investment
```

Giả sử dự án (project / 프로젝트) cần đầu tư 100 triệu hôm nay và dự kiến tạo 60 triệu cuối năm 1, 60 triệu cuối năm 2. Với discount tỷ lệ (rate / 비율) 10%:

```text
PV năm 1 = 60 / 1.10 ≈ 54.55
PV năm 2 = 60 / 1.10² ≈ 49.59

NPV ≈ 54.55 + 49.59 - 100
    ≈ 4.14 triệu
```

NPV dương trong mô hình (model / 모델) này nghĩa discounted inflow lớn hơn investment. Nhưng discount tỷ lệ (rate / 비율), cash-flow forecast, option giá trị (value / 값), strategic fit và non-financial benefit vẫn cần quản trị (governance / 거버넌스) judgment.

Không nên so dự án (project / 프로젝트) chỉ bằng nominal total benefit nếu timing và rủi ro (risk / 위험) khác nhau.

## 9. luồng (flow / 흐름) metrics: Little's Law và forecasting

Trong hệ thống (system / 시스템) đủ ổn định về average arrival/completion tỷ lệ (rate / 비율), Little's Law cho quan hệ (relation / 관계):

```text
WIP ≈ Throughput × Cycle Time
```

Nếu trung bình có 20 item đang in progress và thông lượng (throughput / 처리량) là 5 item/tuần:

```text
Cycle Time ≈ 20 / 5 = 4 tuần
```

Equation không nói mỗi item chắc chắn mất 4 tuần. Nó là quan hệ (relation / 관계) giữa long-run averages dưới điều kiện hệ thống (system / 시스템) tương đối stable.

Nếu WIP tăng lên 40 mà thông lượng (throughput / 처리량) vẫn khoảng 5 item/tuần:

```text
Cycle Time ≈ 40 / 5 = 8 tuần
```

Đây là lý do “bắt đầu nhiều việc hơn” có thể làm phản hồi (feedback / 피드백) chậm hơn dù utilization nhìn cao.

Luồng (flow / 흐름) forecasting tốt hơn khi dùng phân phối (distribution / 분포) thực tế của cycle thời gian (time / 시간) hoặc thông lượng (throughput / 처리량) thay vì chỉ average. Ví dụ thay vì nói “tác vụ (task / 작업) mất 5 ngày”, có thể nói “85% item tương tự hoàn thành trong 8 ngày”. Đây là probabilistic forecast, không phải guarantee.

## 10. Communication channels: độ phức tạp (complexity / 복잡도) tăng theo cặp, nhưng formula chỉ là upper bound lý thuyết

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

Nhưng formula không chứng minh communication tải công việc (workload / 워크로드) thực tế tăng đúng 3 lần. nhóm (team / 팀) cấu trúc (structure / 구조), giao diện (interface / 인터페이스), role clarity, modularity và communication giao thức (protocol / 프로토콜) làm giảm tương tác (interaction / 상호작용) cần thiết. Ý nghĩa của công thức là cho thấy coordination có nonlinear pressure khi group phình lớn.

## 11. đặc tả hợp đồng (contract / 계약) lập luận (reasoning / 추론): số tiền chỉ là một phần của rủi ro (risk / 위험) allocation

Giả sử phạm vi (scope / 범위) tương đối ổn định, acceptance rõ và seller có historical delivery. Fixed-price có thể chuyển nhiều cost-overrun rủi ro (risk / 위험) sang seller, nhưng seller thường price bất định (uncertainty / 불확실성) thành rủi ro (risk / 위험) premium.

Nếu công việc (work / 작업) là discovery prototype với unknown technical solution, ép fixed-price có thể làm vendor thêm contingency lớn, giảm flexibility hoặc tạo tranh chấp “out of phạm vi (scope / 범위)”. Time-and-materials với cap, milestone ngắn, acceptance rõ và exit điểm (point / 지점) có thể tạo alignment tốt hơn.

Commercial lập luận (reasoning / 추론) không dừng ở “giá thấp nhất”. Cần tính total vòng đời (lifecycle / 생명주기) tác động (effect / 효과): thay đổi (change / 변경) chi phí (cost / 비용), oversight, tích hợp (integration / 통합), lock-in, delay exposure, kiến thức (knowledge / 지식) transfer, warranty/hỗ trợ (support / 지원) và exit chi phí (cost / 비용).

Procurement mechanics sâu hơn nằm ở [Quality, resources và procurement](./07_quality_resources_and_procurement.md).

## 12. Sensitivity phân tích (analysis / 분석): quantity nào thật sự lái kết quả (outcome / 결과)

Một forecast có thể chứa nhiều đầu vào (input / 입력) nhưng chỉ vài đầu vào (input / 입력) quyết định kết quả (outcome / 결과). Sensitivity phân tích (analysis / 분석) thay đổi từng giả định (assumption / 가정) trong phạm vi (range / 범위) hợp lý để xem đầu ra (output / 출력) phản ứng mạnh tới đâu.

Ví dụ nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) phụ thuộc vào ba giả định (assumption / 가정): adoption 70%, chi phí (cost / 비용) saving 30%, hiện thực (implementation / 구현) chi phí (cost / 비용) 1 tỷ. Nếu thay adoption từ 70% xuống 50% làm NPV chuyển từ dương sang âm, adoption là high-sensitivity variable và đáng đầu tư thêm kiểm tra hợp lệ (validation / 검증).

Điều này nối quantitative lập luận (reasoning / 추론) với dự án (project / 프로젝트) priority: bất định (uncertainty / 불확실성) nào vừa lớn vừa có sensitivity cao cần attention trước.

## 13. Monte Carlo lập luận (reasoning / 추론): đọc percentile thay vì một deadline duy nhất

Giả sử deterministic mạng (network / 네트워크) tạo finish date 30/11. Sau khi gán phạm vi (range / 범위) hợp lý cho các activity và mô phỏng nhiều iteration, kết quả được tóm tắt như sau:

```text
P50 finish = 30/11
P80 finish = 12/12
P90 finish = 20/12
```

Interpretation:

P50 không có nghĩa “50% chắc chắn đúng” theo nghĩa vật lý; nó nghĩa khoảng 50% iteration trong mô hình (model / 모델) hoàn thành không muộn hơn 30/11. P80 dùng một confidence mục tiêu (target / 대상) thận trọng hơn và cho mốc 12/12.

Nếu đặc tả hợp đồng (contract / 계약) penalty bắt đầu 05/12, việc report duy nhất “forecast 30/11” che mất tail exposure. quản trị (governance / 거버넌스) cần biết xác suất (probability / 확률) phân phối (distribution / 분포) và driver chính.

Giả sử sensitivity cho thấy hai driver lớn nhất là regulatory approval và tích hợp (integration / 통합) testing. Khi đó phản hồi (response / 응답) có leverage có thể là early submission, parallel bằng chứng (evidence / 증거) preparation hoặc kiểm thử (test / 테스트) môi trường (environment / 환경) sớm hơn. Thêm buffer vào documentation tác vụ (task / 작업) ít nhạy sẽ làm schedule dài nhưng tail gần như không giảm.

Một điểm quan trọng khác là correlation. Nếu kiểm thử tích hợp (integration test / 통합 테스트) và defect-fix duration cùng phụ thuộc một vendor nhóm (team / 팀), mô hình (model / 모델) coi chúng độc lập có thể đánh giá P80 quá lạc quan. Simulation tốt không chỉ nhiều iteration; nó cần nhân quả (causal / 인과적) các giả định (assumptions / 가정들) tốt.

### Reserve từ confidence mục tiêu (target / 대상)

Nếu deterministic/baseline mục tiêu (target / 대상) là 30/11 nhưng quản trị (governance / 거버넌스) muốn lần ghi nhận (commit / 커밋) ở mức P80 là 12/12, khoảng 12 ngày chênh lệch có thể được xem như schedule contingency ở mức (level / 수준) phù hợp. Đây không phải padding tùy tiện; nó là buffer gắn với confidence mục tiêu (target / 대상) và bất định (uncertainty / 불확실성) mô hình (model / 모델).

Khi phản hồi (response / 응답) làm phân phối (distribution / 분포) thu hẹp, P80 có thể dịch sớm hơn dù P50 gần như không đổi. Điều đó cho thấy mitigation giảm tail rủi ro (risk / 위험) ngay cả khi expected date không thay nhiều.

## 14. Claim lập luận (reasoning / 추론) bằng số: entitlement không tự sinh quantum

Giả sử buyer thay giao diện (interface / 인터페이스) specification sau khi seller đã hoàn thành thiết kế (design / 설계). Seller yêu cầu:

```text
Time extension: 10 ngày
Additional cost: 80 triệu
```

Dự án (project / 프로젝트) manager không nên bắt đầu bằng câu “80 triệu có hợp lý không?”. Trước hết phải tách ba lớp:

```text
Entitlement → contract có cho relief không?
Causation   → change có thật sự gây delay/cost đó không?
Quantum     → nếu có, mức time/cost hợp lý bao nhiêu?
```

Schedule phân tích (analysis / 분석) cho thấy 10 ngày rework chỉ nằm trên đường dẫn (path / 경로) có 4 ngày float, nên modeled dự án (project / 프로젝트) impact là 6 ngày nếu không có tác động (effect / 효과) khác. chi phí (cost / 비용) bản ghi (record / 레코드) cho thấy 50 triệu labor trực tiếp, 10 triệu kiểm thử (test / 테스트) môi trường (environment / 환경) và 5 triệu approved subcontractor chi phí (cost / 비용). Phần 15 triệu còn lại là overhead allocation chưa có basis rõ.

Khi đó bằng chứng (evidence / 증거) hiện tại không hỗ trợ đơn giản “10 ngày + 80 triệu”. Nó hỗ trợ một discussion tinh hơn: entitlement có thể tồn tại, schedule impact modeled khoảng 6 ngày, direct substantiated chi phí (cost / 비용) hiện khoảng 65 triệu, còn overhead cần đặc tả hợp đồng (contract / 계약) basis/bằng chứng (evidence / 증거).

Nếu cùng giai đoạn seller cũng chậm 3 ngày do staffing riêng, concurrent delay phải được specialist phân tích. Arithmetic không tự quyết legal entitlement; nó làm dispute có cấu trúc (structure / 구조) thay vì bargaining từ hai con số cực đoan.

## 15. Một worked scenario tích hợp

Dự án (project / 프로젝트) có `BAC=2,000`. Tại status date:

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

Dự án (project / 프로젝트) đang behind baseline công việc (work / 작업) và chi phí (cost / 비용) efficiency thấp hơn plan.

Nếu CPI tiếp tục:

```text
EAC = BAC / CPI
    = 2,000 / 0.80
    = 2,500
```

Nếu cả chi phí (cost / 비용) và schedule inefficiency tiếp tục ảnh hưởng remaining chi phí (cost / 비용):

```text
EAC = AC + (BAC - EV) / (CPI × SPI)
    = 1,000 + 1,200 / 0.64
    = 1,000 + 1,875
    = 2,875
```

Hai forecast khác nhau 375 vì giả định (assumption / 가정) khác nhau. PM không nên chọn formula tạo con số “đẹp” hơn; phải hỏi nhân quả (causal / 인과적) bằng chứng (evidence / 증거). Nếu delay đến từ một approval one-off đã resolved, SPI có thể không tiếp tục kéo chi phí (cost / 비용). Nếu nhóm (team / 팀) đang overtime liên tục vì schedule compression, combined efficiency mô hình (model / 모델) có thể realistic hơn.

Nếu management vẫn yêu cầu hoàn tất với BAC 2,000:

```text
TCPI(BAC) = (2,000 - 800) / (2,000 - 1,000)
          = 1,200 / 1,000
          = 1.20
```

Remaining công việc (work / 작업) phải đạt CPI 1.20 trong khi historical CPI hiện tại chỉ 0.80. Trước khi cam kết mục tiêu (target / 대상), cần bằng chứng (evidence / 증거) về phạm vi (scope / 범위) reduction, productivity improvement, vendor renegotiation hoặc structural thay đổi (change / 변경) đủ lớn để giải thích jump đó.

Đây chính là quantitative lập luận (reasoning / 추론): phép tính tạo tín hiệu (signal / 신호); nguyên nhân gốc (root cause / 근본 원인) và quản trị (governance / 거버넌스) quyết định hành động (action / 동작).

## 16. Robustness check: quyết định (decision / 결정) có đứng vững khi đầu vào (input / 입력) thay đổi không?

Một mô hình (model / 모델) không chỉ cần cho ra con số; nó phải đủ **robust** để hỗ trợ quyết định (decision / 결정). Nếu quyết định (decision / 결정) đảo chiều chỉ vì một đầu vào (input / 입력) thay đổi rất nhỏ trong phạm vi (range / 범위) hợp lý, organization không nên trình bày recommendation như chắc chắn.

Giả sử Option A có NPV `+8` triệu ở adoption 70%, nhưng adoption giảm nhẹ xuống 65% đã làm NPV âm. Khi đó conclusion “NPV dương nên làm” che một ranh giới (boundary / 경계) rất gần. quyết định (decision / 결정) cần thêm bằng chứng (evidence / 증거) về adoption, option giảm exposure hoặc staged investment. Ngược lại, nếu NPV vẫn dương ở nhiều scenario hợp lý và chỉ âm trong extreme trường hợp (case / 사례), recommendation robust hơn.

Robustness check có thể đơn giản bằng cách thay các giả định (assumption / 가정) quan trọng trong phạm vi (range / 범위) plausible rồi hỏi:

```text
Input nào làm decision đổi?
Threshold nằm gần current estimate không?
Nếu estimate sai một mức hợp lý, consequence là gì?
Có option nào giảm downside mà giữ upside không?
```

Đây là cầu nối giữa sensitivity phân tích (analysis / 분석) và quản trị (governance / 거버넌스). Sensitivity nói đầu vào (input / 입력) nào ảnh hưởng đầu ra (output / 출력); robustness hỏi ảnh hưởng đó có đủ để thay quyết định không.

## 17. Decision-reversal threshold: tìm ranh giới (boundary / 경계) thay vì tranh luận một con số

Nhiều cuộc họp mắc kẹt ở việc “estimate đúng là 60 hay 65?”. Câu hỏi mạnh hơn thường là: **giá trị bao nhiêu thì quyết định (decision / 결정) đổi?**

Ví dụ vendor A rẻ hơn 100 triệu nhưng có expected switching/lock-in chi phí (cost / 비용) chưa chắc chắn. Nếu phân tích (analysis / 분석) cho thấy vendor A chỉ còn ưu thế khi future switching chi phí (cost / 비용) dưới 40 triệu, thì `40` là decision-reversal threshold quan trọng hơn việc cố đo switching chi phí (cost / 비용) chính xác tới từng triệu ngay lập tức.

Tương tự, nếu dự án (project / 프로젝트) chỉ đạt nghiệp vụ (business / 비즈니스) trường hợp (case / 사례) khi adoption trên 62%, đo lường (measurement / 측정) plan nên ưu tiên bằng chứng (evidence / 증거) quanh vùng đó. Nếu adoption estimate hiện là 85%, thêm nghiên cứu để phân biệt 84% hay 86% có thể ít giá trị (value / 값). Nếu estimate là 60–65%, cùng nghiên cứu đó có giá trị (value / 값) of thông tin (information / 정보) cao hơn vì có thể đổi quyết định.

Threshold thinking giúp allocation của phân tích (analysis / 분석) effort dựa trên **quyết định (decision / 결정) sensitivity**, không dựa trên thói quen “càng nhiều dữ liệu (data / 데이터) càng tốt”.

## 18. mô hình (model / 모델) rủi ro (risk / 위험): con số có thể chính xác theo mô hình (model / 모델) nhưng mô hình (model / 모델) sai cấu trúc

Mô hình (model / 모델) rủi ro (risk / 위험) xảy ra khi arithmetic đúng nhưng biểu diễn (representation / 표현) của reality không đủ đúng. Có ít nhất bốn nguồn thường gặp.

Thứ nhất là **dữ liệu (data / 데이터) rủi ro (risk / 위험)**: actual đầu vào (input / 입력) sai, thiếu hoặc outdated. Thứ hai là **parameter rủi ro (risk / 위험)**: xác suất (probability / 확률), duration hoặc chi phí (cost / 비용) phạm vi (range / 범위) được estimate quá tự tin. Thứ ba là **structural rủi ro (risk / 위험)**: mô hình (model / 모델) bỏ phụ thuộc (dependency / 의존성)/correlation, giả định (assumption / 가정) nonlinear hoặc vòng phản hồi (feedback loop / 피드백 루프) quan trọng. Thứ tư là **usage rủi ro (risk / 위험)**: mô hình (model / 모델) vốn phù hợp cho planning nhưng bị dùng như commitment tuyệt đối hoặc hiệu năng (performance / 성능) score.

Ví dụ Monte Carlo với 100.000 iteration vẫn cho kết quả yếu nếu mạng (network / 네트워크) bỏ một regulatory phụ thuộc (dependency / 의존성). EAC tính đúng tới ba chữ số thập phân vẫn không hữu ích nếu baseline EV không phản ánh completion thật. NPV chính xác về discounting vẫn sai quyết định (decision / 결정) nếu cash-flow mô hình (model / 모델) bỏ adoption chi phí (cost / 비용) hoặc decommission obligation.

Vì vậy rà soát (review / 검토) quantitative mô hình (model / 모델) nên hỏi không chỉ “formula đúng không?” mà còn “mô hình (model / 모델) ranh giới (boundary / 경계) có chứa driver tạo kết quả (outcome / 결과) không?”. Precision không bù được omission.

## 19. Forecast calibration: mô hình (model / 모델) phải học từ sai số lịch sử

Một forecast có thể đúng một lần do may mắn. Calibration xem confidence statement có khớp actual frequency qua nhiều lần không. Nếu nhóm (team / 팀) liên tục báo P80 nhưng actual miss mục tiêu (target / 대상) thường xuyên hơn nhiều, đầu vào (input / 입력) phân phối (distribution / 분포), phụ thuộc (dependency / 의존성) hoặc correlation đang bị underestimate.

Một practice đơn giản là giữ phiên bản (version / 버전) của forecast theo status date thay vì overwrite:

```text
Status date | Forecast | Confidence | Actual | Main reason for miss
```

Sau nhiều milestone, organization có thể phát hiện systematic optimism, vendor-specific tail hoặc loại công việc (work / 작업) nào mô hình (model / 모델) luôn understate. Đây là dữ liệu để sửa mô hình (model / 모델), không chỉ đánh giá cá nhân estimator.

Calibration cũng giúp tránh hindsight độ lệch (bias / 편향). Khi actual xảy ra, con số cũ phải được giữ để xem nhóm (team / 팀) đã biết gì lúc ra quyết định (decision / 결정), thay vì âm thầm sửa forecast lịch sử (history / 이력) cho giống kết quả (outcome / 결과).

## 20. Cross-metric consistency: các con số có kể cùng một câu chuyện không?

Một dashboard có thể chứa nhiều chỉ số (metric / 지표) “đúng” nhưng mutually inconsistent. Ví dụ SPI gần 1 trong khi milestone forecast trượt mạnh; velocity tăng trong khi cycle thời gian (time / 시간) cũng tăng; percent complete 90% trong khi UAT pass tỷ lệ (rate / 비율) 50%; CPI tốt nhưng committed chi phí (cost / 비용) chưa vào AC rất lớn.

Mâu thuẫn không tự động nghĩa một chỉ số (metric / 지표) sai. Chúng có thể đo trạng thái (state / 상태) khác nhau. Nhưng inconsistency là tín hiệu (signal / 신호) cần giải thích trước khi quản trị (governance / 거버넌스) dùng dashboard.

Một discipline hữu ích là hỏi mỗi chỉ số (metric / 지표):

```text
Nó đo stock, flow, efficiency hay outcome?
Nó nhìn quá khứ, hiện tại hay forecast?
Denominator/baseline là gì?
Có lag hoặc committed-but-not-realized state nào chưa phản ánh không?
```

Cross-metric lập luận (reasoning / 추론) ngăn việc chọn đúng một con số thuận lợi để kể narrative mong muốn. Quantitative bằng chứng (evidence / 증거) mạnh khi nhiều independent view converge hoặc khi divergence được giải thích bằng cơ chế (mechanism / 메커니즘) rõ.

## 21. đơn vị (unit / 단위) và dimensional sanity check

Nhiều lỗi không cần công thức nâng cao để phát hiện. Chỉ cần hỏi đơn vị (unit / 단위) có hợp lý không. CPI/SPI là ratio không có đơn vị. Cycle thời gian (time / 시간) có đơn vị thời gian. thông lượng (throughput / 처리량) là item/thời gian (time / 시간). NPV là tiền. xác suất (probability / 확률) nằm trong phạm vi (range / 범위) hợp lệ. Một phép cộng giữa percentage và tiền trực tiếp thường vô nghĩa nếu chưa transform về cùng quantity.

Sanity check cũng áp dụng cho magnitude. Nếu thêm một engineer được forecast rút 50% schedule trong công việc (work / 작업) có nhiều bên ngoài (external / 외부) phụ thuộc (dependency / 의존성), mô hình (model / 모델) cần giải thích nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘). Nếu chi phí (cost / 비용) saving vượt tổng chi phí (cost / 비용) hiện tại, denominator hoặc thời gian (time / 시간) horizon có thể sai.

Trước khi tin một đầu ra (output / 출력) phức tạp, hãy kiểm tra đơn vị, thứ tự (order / 순서) of magnitude và ranh giới (boundary / 경계). Đây là cách rẻ nhất để bắt mô hình (model / 모델) lỗi (error / 오류).

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

Monte Carlo percentile, claim phân tích (analysis / 분석) và sensitivity không có một single formula đáng học thuộc. Chúng là lập luận (reasoning / 추론) khung phần mềm (framework / 프레임워크): define inputs, các giả định (assumptions / 가정들), phụ thuộc (dependency / 의존성)/correlation, run or compare scenarios, rồi interpret đầu ra (output / 출력) theo quyết định (decision / 결정) threshold.

Formula map này chỉ nên dùng sau khi bạn có thể giải thích quantity bằng lời. Nếu không thể nói EV khác AC thế nào hoặc vì sao một EAC formula phù hợp hơn formula khác, hãy quay lại mô hình tư duy (mental model / 사고 모델) trước arithmetic.

## Mô hình tư duy (mental model / 사고 모델)

> Một phép tính PMP luôn là một mô hình (model / 모델) thu gọn của reality. Hãy đọc quantity, giả định (assumption / 가정), bất định (uncertainty / 불확실성), correlation, robustness và quyết định (decision / 결정) consequence trước khi bấm máy. Con số đúng không cứu được một mô hình (model / 모델) sai; mô hình (model / 모델) tốt cũng chưa đủ nếu quyết định (decision / 결정) không đứng vững khi đầu vào (input / 입력) thay đổi trong phạm vi (range / 범위) hợp lý.

Sau chapter này, đọc [End-to-end case studies](./16_end_to_end_case_studies.md) để thấy schedule, finance, rủi ro (risk / 위험), procurement và quản trị (governance / 거버넌스) cùng tương tác trong một dự án (project / 프로젝트) thực.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 foundations value and project system](./00_foundations_value_and_project_system.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
