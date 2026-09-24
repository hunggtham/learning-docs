# National Accounts & Macro Measurement — GDP, income, prices và stock–flow reasoning

Macroeconomics bắt đầu bằng measurement. Trước khi hỏi “nền kinh tế đang tăng trưởng hay suy thoái?”, phải biết đại lượng đang đo là flow hay stock, nominal hay real, aggregate hay per-capita, gross hay net, và số liệu đó đại diện cho production, income, expenditure hay wealth.

Một lỗi phổ biến là nhảy thẳng vào interest rate, inflation hoặc policy mà không có accounting identity rõ. National accounts cung cấp ngôn ngữ nền để các model phía sau không bị mơ hồ.

## 1. GDP đo production flow, không đo toàn bộ welfare

Gross Domestic Product (GDP) là market value của final goods và services được sản xuất trong lãnh thổ một nền kinh tế trong một khoảng thời gian.

Ba ý phải giữ cùng lúc:

- **gross**: chưa trừ depreciation của capital;
- **domestic**: dựa trên nơi production diễn ra, không phải nationality của owner;
- **product**: đo production flow, không phải wealth stock.

GDP không trực tiếp đo leisure, inequality, unpaid household work, environmental damage, security, health quality hoặc subjective well-being. Nó là production-accounting measure, không phải một welfare index hoàn chỉnh.

## 2. Ba cách tính GDP phải khớp về accounting

### Production approach

Cộng value added của các producer:

```text
Value Added = Output Value − Intermediate Input Cost
```

Không cộng raw sales của mọi stage vì sẽ double-count intermediate goods.

### Expenditure approach

```text
Y = C + I + G + NX
```

Trong đó:

- `C`: household consumption;
- `I`: investment, gồm business fixed investment, residential investment và inventory change;
- `G`: government purchases of goods/services;
- `NX = X − M`: net exports.

Transfer payment như pension hoặc unemployment benefit không trực tiếp nằm trong `G` vì chúng chuyển purchasing power, không phải current production purchase.

### Income approach

Production tạo income cho labor, capital và government qua wages, profits, rents, interest, taxes less subsidies. Sau accounting adjustments, total income phải tương ứng total production.

Nếu ba cách không khớp hoàn hảo trong data thực, statistical discrepancy phản ánh measurement error và timing differences, không phá identity lý thuyết.

## 3. Final good không đồng nghĩa consumer good

Machine được firm mua là final investment good nếu nó không được resold như intermediate input trong cùng production chain. Inventory tăng cũng được tính là investment vì output đã được sản xuất dù chưa bán cho final customer.

Used goods thường không vào current GDP vì production đã được ghi ở kỳ trước; service fee của dealer lại là current production và được tính.

## 4. Nominal GDP và Real GDP

Nominal GDP dùng current prices:

```text
Nominal GDP_t = Σ P_t Q_t
```

Real GDP cố định price base hoặc dùng chain-weighting để tách quantity change khỏi price change.

Nếu nominal GDP tăng 8% nhưng price level tăng khoảng 5%, real production không tăng 8%. Cần tách price và quantity.

## 5. GDP deflator và CPI đo khác nhau

GDP deflator:

```text
GDP Deflator = Nominal GDP / Real GDP × 100
```

Nó bao phủ domestically produced final goods/services và basket thay đổi cùng current output.

Consumer Price Index (CPI) theo dõi giá một consumer basket đại diện, có thể gồm imports nhưng không gồm mọi investment/government output.

Vì scope và weighting khác nhau, CPI inflation và GDP-deflator inflation không cần bằng nhau.

## 6. Real GDP per capita gần living standard hơn total GDP nhưng vẫn chưa đủ

Total GDP có thể tăng do population tăng. Real GDP per capita:

```text
Real GDP / Population
```

cho một measure gần hơn về average material production per person.

Nhưng average che distribution. Nếu GDP per capita tăng trong khi gains tập trung ở một nhóm nhỏ, median household experience có thể khác mạnh.

## 7. GNI, GDP và cross-border income

Gross National Income (GNI) điều chỉnh GDP bằng net primary income from abroad.

Một factory nước ngoài sản xuất tại Hàn Quốc làm tăng Korea GDP; phần profit chuyển về parent abroad ảnh hưởng difference giữa GDP và GNI.

Trong economy có large foreign-owned production hoặc citizens sở hữu nhiều assets abroad, GDP và national income có thể diverge đáng kể.

## 8. Saving và investment identity

Từ expenditure identity:

```text
Y = C + I + G + NX
```

National saving có thể viết:

```text
S = Y − C − G
```

suy ra:

```text
S = I + NX
```

Trong closed economy `NX = 0`, nên accounting identity `S = I`.

Identity không nói saving “gây ra” investment theo một chiều causal cụ thể. Causality phụ thuộc financial system, interest rates, expectations, policy và open-economy capital flows.

## 9. Private saving, public saving và fiscal balance

Nếu taxes net of transfers là `T`:

```text
Private Saving = Y − T − C
Public Saving = T − G
National Saving = Private Saving + Public Saving
```

Budget deficit nghĩa public saving âm. Nhưng deficit có crowding-out effect đến đâu phụ thuộc monetary regime, output gap, capital mobility và private behavior.

## 10. Current account và capital/financial account

Trong simplified open-economy accounting:

```text
Current Account ≈ S − I
```

Current-account surplus nghĩa national saving vượt domestic investment và economy đang net lending abroad; deficit nghĩa domestic investment/consumption cần net financing from abroad.

Đây là accounting relation, không phải moral label. Deficit có thể finance productive investment hoặc unsustainable consumption; surplus có thể phản ánh competitiveness, demographics, weak domestic demand hoặc precautionary saving.

## 11. Stock và flow

GDP, income, consumption và investment là **flows** per period. Wealth, debt và capital stock là **stocks** tại một point in time.

Investment làm capital stock tăng, depreciation làm giảm:

```text
K_{t+1} = K_t + I_t − δK_t
```

Tương tự fiscal deficit là flow; public debt là accumulated stock.

Nhầm stock với flow là một trong những lỗi macro nghiêm trọng nhất.

## 12. Gross và net

Gross investment chưa trừ depreciation. Net investment:

```text
Net Investment = Gross Investment − Depreciation
```

GDP là gross; Net Domestic Product (NDP) trừ capital consumption.

Một economy có high gross investment nhưng capital depreciates rất nhanh có thể tăng productive capacity ít hơn headline investment gợi ý.

## 13. Potential output và output gap

Potential output không phải maximum physical output. Nó là estimate về output bền vững khi labor/capital được sử dụng ở mức phù hợp với stable inflation, tùy model.

Output gap:

```text
Output Gap = Actual Output − Potential Output
```

Positive gap có thể đi kèm inflation pressure; negative gap thường đi kèm idle capacity và weak labor demand.

Nhưng potential output không quan sát trực tiếp. Nó được estimate và thường revision lớn sau shock.

## 14. Business-cycle dating khác “hai quý GDP âm”

Một recession không nên chỉ được hiểu bằng heuristic “hai quý liên tiếp real GDP giảm”. Statistical agencies hoặc research bodies thường nhìn broad indicators như production, income, employment và sales.

Heuristic hữu ích để communication nhưng không phải definition universal.

## 15. Leading, coincident và lagging indicators

Macro data có timing khác nhau.

- leading indicators cố báo hiệu future activity;
- coincident indicators di chuyển cùng current cycle;
- lagging indicators phản ứng sau cycle.

Một indicator có thể change role giữa regimes, nên classification không tuyệt đối.

## 16. Frequency, seasonality và annualization

Monthly/quarterly data cần phân biệt:

```text
month-over-month
quarter-over-quarter
quarter-over-quarter annualized
year-over-year
```

Một QoQ annualized rate không phải mức tăng thực tế trong một quarter; nó là tốc độ nếu quarter đó lặp lại cả năm.

Seasonal adjustment loại patterns lặp lại theo season, nhưng bất thường như pandemic hoặc holiday shifts có thể làm adjustment khó.

## 17. Revisions và real-time data

GDP, employment và productivity thường được revision khi source data tốt hơn xuất hiện.

Policy maker ra quyết định bằng real-time vintage, không bằng revised history mà analyst nhìn sau này. Backtest dùng final data có thể tạo hindsight bias.

Đây là lý do applied macro cần lưu data vintage khi đánh giá forecast hoặc policy reaction.

## 18. Inflation measurement

Inflation là rate of change của price index, không phải bản thân price level.

Nếu inflation giảm từ 6% xuống 2%, prices vẫn tăng, chỉ tăng chậm hơn. Deflation là negative inflation, tức price level giảm.

Core inflation thường loại một số volatile components để quan sát underlying trend, nhưng headline inflation quan trọng cho household purchasing power.

## 19. Unemployment measurement

Unemployment rate:

```text
Unemployed / Labor Force
```

Labor force gồm employed + unemployed actively seeking work.

Người không tìm việc có thể nằm ngoài labor force, nên unemployment rate giảm không luôn nghĩa labor market cải thiện. Cần xem labor-force participation, employment-population ratio, hours worked và underemployment.

## 20. Productivity measurement

Labor productivity thường là output per hour hoặc per worker. Total factor productivity (TFP) là residual sau khi account observed capital/labor inputs trong production-function framework.

TFP không đơn giản là “technology”. Nó có thể capture technology, management, reallocation, measurement error và omitted capital quality.

## 21. Distribution và aggregate paradox

Aggregate GDP tăng có thể đồng thời với real income của một subgroup giảm. Macro aggregates là weighted totals, không nói distribution tự động.

Do đó khi policy question liên quan household welfare, cần nối national accounts với distributional national accounts, wage/wealth data và demographic composition.

## 22. Mental model đo macro

Trước mọi macro claim, hãy hỏi:

1. Variable là stock hay flow?
2. Nominal hay real?
3. Total hay per-capita/per-hour?
4. Gross hay net?
5. Domestic production hay national income?
6. Rate level hay rate of change?
7. Data frequency và seasonal adjustment là gì?
8. Series có revision không?
9. Identity đang được dùng như accounting relation hay causal theory?
10. Aggregate che distribution nào?

National accounts tạo skeleton. Chapter tiếp theo hỏi câu dài hạn quan trọng nhất: vì sao real output per person giữa các nước và qua thời gian có thể tăng mạnh hoặc stagnate? Đó là growth và productivity.
