# National Accounts & Macro Đo lường (measurement / 측정) — GDP, income, prices và stock–luồng (flow / 흐름) lập luận (reasoning / 추론)

Macroeconomics bắt đầu bằng đo lường (measurement / 측정). Trước khi hỏi “nền kinh tế đang tăng trưởng hay suy thoái?”, phải biết đại lượng đang đo là luồng (flow / 흐름) hay stock, nominal hay real, aggregate hay per-capita, gross hay net, và số liệu đó đại diện cho môi trường vận hành (production / 운영 환경), income, expenditure hay wealth.

Một lỗi phổ biến là nhảy thẳng vào interest tỷ lệ (rate / 비율), inflation hoặc chính sách (policy / 정책) mà không có accounting định danh (identity / 식별자) rõ. National accounts cung cấp ngôn ngữ nền để các mô hình (model / 모델) phía sau không bị mơ hồ.

## 1. GDP đo môi trường vận hành (production / 운영 환경) luồng (flow / 흐름), không đo toàn bộ welfare

Gross Domestic Sản phẩm (product / 제품) (GDP) là giá trị thị trường (market value / 시장 가치) của final goods và services được sản xuất trong lãnh thổ một nền kinh tế trong một khoảng thời gian.

Ba ý phải giữ cùng lúc:

- **gross**: chưa trừ depreciation của capital;
- **domestic**: dựa trên nơi môi trường vận hành (production / 운영 환경) diễn ra, không phải nationality của đơn vị sở hữu (owner / 오너);
- **sản phẩm (product / 제품)**: đo môi trường vận hành (production / 운영 환경) luồng (flow / 흐름), không phải wealth stock.

GDP không trực tiếp đo leisure, inequality, unpaid household công việc (work / 작업), environmental damage, bảo mật (security / 보안), health chất lượng (quality / 품질) hoặc subjective well-being. Nó là production-accounting measure, không phải một welfare chỉ mục (index / 인덱스) hoàn chỉnh.

## 2. Ba cách tính GDP phải khớp về accounting

### Môi trường vận hành (production / 운영 환경) approach

Cộng giá trị (value / 값) added của các producer:

```text
Value Added = Output Value − Intermediate Input Cost
```

Không cộng raw sales của mọi stage vì sẽ double-count intermediate goods.

### Expenditure approach
Phần “Expenditure approach” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Y = C + I + G + NX
```

Trong đó:

- `C`: household consumption;
- `I`: investment, gồm nghiệp vụ (business / 비즈니스) fixed investment, residential investment và inventory thay đổi (change / 변경);
- `G`: government purchases of goods/services;
- `NX = X − M`: net exports.

Transfer payment như pension hoặc unemployment benefit không trực tiếp nằm trong `G` vì chúng chuyển purchasing power, không phải hiện tại (current / 현재) môi trường vận hành (production / 운영 환경) purchase.

### Income approach

Môi trường vận hành (production / 운영 환경) tạo income cho labor, capital và government qua wages, profits, rents, interest, taxes less subsidies. Sau accounting adjustments, total income phải tương ứng total môi trường vận hành (production / 운영 환경).

Nếu ba cách không khớp hoàn hảo trong dữ liệu (data / 데이터) thực, statistical discrepancy phản ánh sai số đo lường (measurement error / 측정 오차) và timing differences, không phá định danh (identity / 식별자) lý thuyết.

## 3. Final good không đồng nghĩa bên tiêu thụ (consumer / 소비자) good

Machine được firm mua là final investment good nếu nó không được resold như intermediate đầu vào (input / 입력) trong cùng môi trường vận hành (production / 운영 환경) chuỗi (chain / 사슬). Inventory tăng cũng được tính là investment vì đầu ra (output / 출력) đã được sản xuất dù chưa bán cho final customer.

Used goods thường không vào hiện tại (current / 현재) GDP vì môi trường vận hành (production / 운영 환경) đã được ghi ở kỳ trước; dịch vụ (service / 서비스) fee của dealer lại là hiện tại (current / 현재) môi trường vận hành (production / 운영 환경) và được tính.

## 4. Nominal GDP và Real GDP

Nominal GDP dùng hiện tại (current / 현재) prices:

```text
Nominal GDP_t = Σ P_t Q_t
```

Real GDP cố định price cơ sở (base / 기반) hoặc dùng chain-weighting để tách quantity thay đổi (change / 변경) khỏi price thay đổi (change / 변경).

Nếu nominal GDP tăng 8% nhưng price mức (level / 수준) tăng khoảng 5%, real môi trường vận hành (production / 운영 환경) không tăng 8%. Cần tách price và quantity.

## 5. GDP deflator và CPI đo khác nhau

GDP deflator:

```text
GDP Deflator = Nominal GDP / Real GDP × 100
```

Nó bao phủ domestically produced final goods/services và basket thay đổi cùng hiện tại (current / 현재) đầu ra (output / 출력).

Bên tiêu thụ (consumer / 소비자) Price Chỉ mục (index / 인덱스) (CPI) theo dõi giá một bên tiêu thụ (consumer / 소비자) basket đại diện, có thể gồm imports nhưng không gồm mọi investment/government đầu ra (output / 출력).

Vì phạm vi (scope / 범위) và weighting khác nhau, CPI inflation và GDP-deflator inflation không cần bằng nhau.

## 6. Real GDP per capita gần living tiêu chuẩn (standard / 표준) hơn total GDP nhưng vẫn chưa đủ

Total GDP có thể tăng do population tăng. Real GDP per capita:

```text
Real GDP / Population
```

cho một measure gần hơn về average material môi trường vận hành (production / 운영 환경) per person.

Nhưng average che phân phối (distribution / 분포). Nếu GDP per capita tăng trong khi gains tập trung ở một nhóm nhỏ, median household experience có thể khác mạnh.

## 7. GNI, GDP và cross-border income

Gross National Income (GNI) điều chỉnh GDP bằng net primary income from abroad.

Một factory nước ngoài sản xuất tại Hàn Quốc làm tăng Korea GDP; phần profit chuyển về parent abroad ảnh hưởng difference giữa GDP và GNI.

Trong economy có large foreign-owned môi trường vận hành (production / 운영 환경) hoặc citizens sở hữu nhiều assets abroad, GDP và national income có thể diverge đáng kể.

## 8. Saving và investment định danh (identity / 식별자)

Từ expenditure định danh (identity / 식별자):

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

Trong closed economy `NX = 0`, nên accounting định danh (identity / 식별자) `S = I`.

Định danh (identity / 식별자) không nói saving “gây ra” investment theo một chiều nhân quả (causal / 인과적) cụ thể. Causality phụ thuộc financial hệ thống (system / 시스템), interest rates, expectations, chính sách (policy / 정책) và open-economy capital flows.

## 9. Private saving, công khai (public / 공개) saving và fiscal balance

Nếu taxes net of transfers là `T`:

```text
Private Saving = Y − T − C
Public Saving = T − G
National Saving = Private Saving + Public Saving
```

Ngân sách (budget / 예산) deficit nghĩa công khai (public / 공개) saving âm. Nhưng deficit có crowding-out tác động (effect / 효과) đến đâu phụ thuộc monetary regime, đầu ra (output / 출력) gap, capital mobility và private hành vi (behavior / 동작).

## 10. Hiện tại (current / 현재) account và capital/financial account

Trong simplified open-economy accounting:

```text
Current Account ≈ S − I
```

Current-account surplus nghĩa national saving vượt domestic investment và economy đang net lending abroad; deficit nghĩa domestic investment/consumption cần net financing from abroad.

Đây là accounting quan hệ (relation / 관계), không phải moral label. Deficit có thể finance productive investment hoặc unsustainable consumption; surplus có thể phản ánh competitiveness, demographics, weak domestic demand hoặc precautionary saving.

## 11. Stock và luồng (flow / 흐름)

GDP, income, consumption và investment là **flows** per period. Wealth, debt và capital stock là **stocks** tại một điểm (point / 지점) in thời gian (time / 시간).

Investment làm capital stock tăng, depreciation làm giảm:

```text
K_{t+1} = K_t + I_t − δK_t
```

Tương tự fiscal deficit là luồng (flow / 흐름); công khai (public / 공개) debt là accumulated stock.

Nhầm stock với luồng (flow / 흐름) là một trong những lỗi macro nghiêm trọng nhất.

## 12. Gross và net

Gross investment chưa trừ depreciation. Net investment:

```text
Net Investment = Gross Investment − Depreciation
```

GDP là gross; Net Domestic Sản phẩm (product / 제품) (NDP) trừ capital consumption.

Một economy có high gross investment nhưng capital depreciates rất nhanh có thể tăng productive sức chứa (capacity / 용량) ít hơn headline investment gợi ý.

## 13. Potential đầu ra (output / 출력) và đầu ra (output / 출력) gap

Potential đầu ra (output / 출력) không phải maximum vật lý (physical / 물리적) đầu ra (output / 출력). Nó là estimate về đầu ra (output / 출력) bền vững khi labor/capital được sử dụng ở mức phù hợp với stable inflation, tùy mô hình (model / 모델).

Đầu ra (output / 출력) gap:

```text
Output Gap = Actual Output − Potential Output
```

Positive gap có thể đi kèm inflation pressure; negative gap thường đi kèm idle sức chứa (capacity / 용량) và weak labor demand.

Nhưng potential đầu ra (output / 출력) không quan sát trực tiếp. Nó được estimate và thường revision lớn sau shock.

## 14. Business-cycle dating khác “hai quý GDP âm”

Một recession không nên chỉ được hiểu bằng heuristic “hai quý liên tiếp real GDP giảm”. Statistical agencies hoặc research bodies thường nhìn broad indicators như môi trường vận hành (production / 운영 환경), income, employment và sales.

Heuristic hữu ích để communication nhưng không phải definition universal.

## 15. Leading, coincident và lagging indicators

Macro dữ liệu (data / 데이터) có timing khác nhau.

- leading indicators cố báo hiệu future activity;
- coincident indicators di chuyển cùng hiện tại (current / 현재) cycle;
- lagging indicators phản ứng sau cycle.

Một indicator có thể thay đổi (change / 변경) role giữa regimes, nên classification không tuyệt đối.

## 16. Frequency, seasonality và annualization

Monthly/quarterly dữ liệu (data / 데이터) cần phân biệt:

```text
month-over-month
quarter-over-quarter
quarter-over-quarter annualized
year-over-year
```

Một QoQ annualized tỷ lệ (rate / 비율) không phải mức tăng thực tế trong một quarter; nó là tốc độ nếu quarter đó lặp lại cả năm.

Seasonal adjustment loại patterns lặp lại theo season, nhưng bất thường như pandemic hoặc holiday shifts có thể làm adjustment khó.

## 17. Revisions và real-time dữ liệu (data / 데이터)

GDP, employment và productivity thường được revision khi nguồn (source / 소스) dữ liệu (data / 데이터) tốt hơn xuất hiện.

Chính sách (policy / 정책) maker ra quyết định bằng real-time vintage, không bằng revised lịch sử (history / 이력) mà analyst nhìn sau này. Backtest dùng final dữ liệu (data / 데이터) có thể tạo hindsight độ lệch (bias / 편향).

Đây là lý do applied macro cần lưu dữ liệu (data / 데이터) vintage khi đánh giá forecast hoặc chính sách (policy / 정책) reaction.

## 18. Inflation đo lường (measurement / 측정)

Inflation là tỷ lệ (rate / 비율) of thay đổi (change / 변경) của price chỉ mục (index / 인덱스), không phải bản thân price mức (level / 수준).

Nếu inflation giảm từ 6% xuống 2%, prices vẫn tăng, chỉ tăng chậm hơn. Deflation là negative inflation, tức price mức (level / 수준) giảm.

Cốt lõi (core / 핵심) inflation thường loại một số volatile components để quan sát underlying trend, nhưng headline inflation quan trọng cho household purchasing power.

## 19. Unemployment đo lường (measurement / 측정)

Unemployment tỷ lệ (rate / 비율):

```text
Unemployed / Labor Force
```

Labor force gồm employed + unemployed actively seeking công việc (work / 작업).

Người không tìm việc có thể nằm ngoài labor force, nên unemployment tỷ lệ (rate / 비율) giảm không luôn nghĩa labor thị trường (market / 시장) cải thiện. Cần xem labor-force participation, employment-population ratio, hours worked và underemployment.

## 20. Productivity đo lường (measurement / 측정)

Labor productivity thường là đầu ra (output / 출력) per hour hoặc per worker. Total factor productivity (TFP) là residual sau khi account observed capital/labor inputs trong production-function khung phần mềm (framework / 프레임워크).

TFP không đơn giản là “technology”. Nó có thể capture technology, management, reallocation, sai số đo lường (measurement error / 측정 오차) và omitted capital chất lượng (quality / 품질).

## 21. Phân phối (distribution / 분포) và aggregate paradox

Aggregate GDP tăng có thể đồng thời với real income của một subgroup giảm. Macro aggregates là weighted totals, không nói phân phối (distribution / 분포) tự động.

Do đó khi chính sách (policy / 정책) question liên quan household welfare, cần nối national accounts với distributional national accounts, wage/wealth dữ liệu (data / 데이터) và demographic composition.

## 22. Mô hình tư duy (mental model / 사고 모델) đo macro

Trước mọi macro claim, hãy hỏi:

1. Variable là stock hay luồng (flow / 흐름)?
2. Nominal hay real?
3. Total hay per-capita/per-hour?
4. Gross hay net?
5. Domestic môi trường vận hành (production / 운영 환경) hay national income?
6. Tỷ lệ (rate / 비율) mức (level / 수준) hay tỷ lệ (rate / 비율) of thay đổi (change / 변경)?
7. Dữ liệu (data / 데이터) frequency và seasonal adjustment là gì?
8. Series có revision không?
9. Định danh (identity / 식별자) đang được dùng như accounting quan hệ (relation / 관계) hay nhân quả (causal / 인과적) lý thuyết (theory / 이론)?
10. Aggregate che phân phối (distribution / 분포) nào?

National accounts tạo skeleton. Chapter tiếp theo hỏi câu dài hạn quan trọng nhất: vì sao real đầu ra (output / 출력) per person giữa các nước và qua thời gian có thể tăng mạnh hoặc stagnate? Đó là growth và productivity.
