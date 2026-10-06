# Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản

> **Mạch đọc:** [README](./README.md) là owner của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**; dùng README để biết cẩm nang đứng sau phần lý thuyết và trước các case/asset lab nào. Từ **1. Không đọc headline một cách cơ học** chuyển sang baseline–consensus–pricing, surprise, cấu phần và hàm phản ứng chính sách, rồi kết thúc ở yields/FX/credit/equities; mỗi bước biến một mốc dữ liệu thành giả thuyết truyền dẫn có thể kiểm chứng.

> Dữ liệu vĩ mô chỉ hữu ích khi nó làm thay đổi xác suất về tăng trưởng, lạm phát, chính sách, thanh khoản hoặc tín dụng. Mục tiêu của chương này là biến lịch kinh tế từ một danh sách headline thành một quy trình đọc dữ liệu có hệ thống.

Khung tổng quát:

```text
Mốc nền
→ Dự báo đồng thuận
→ Kỳ vọng đã phản ánh trong giá
→ Số liệu thực tế
→ Mức bất ngờ
→ Cấu phần
→ Hàm phản ứng chính sách
→ Yields / FX / Credit
→ Equities / Commodities
```

# Phần I — Cách đọc một bản phát hành (release / 릴리스)

## 1. Không đọc headline một cách cơ học

Thị trường không phản ứng đơn giản với “CPI cao”, “NFP tốt” hay “GDP mạnh”. Giá phản ứng với:

- số thực tế so với dự báo;
- revisions;
- cấu phần;
- positioning;
- ý nghĩa đối với chính sách tương lai.

Một dữ liệu tốt có thể khiến thị trường giảm nếu nó vẫn thấp hơn điều đã được price trước.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **2. Baseline, consensus và thị trường (market / 시장) pricing** nối từ **1. Không đọc headline một cách cơ học** sang **3. Surprise không chỉ là Actual - Forecast**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Baseline, consensus và thị trường (market / 시장) pricing

Ba khái niệm này khác nhau.

**Baseline:** nhận định riêng của bạn trước sự kiện.

**Consensus:** dự báo đồng thuận của economist hoặc analyst.

**thị trường (market / 시장) pricing:** kỳ vọng được phản ánh trong futures, yield curve, options hoặc giá tài sản.

Ví dụ consensus dự báo cut 25bp nhưng futures đã phản ánh xác suất đáng kể của 50bp. Nếu ngân hàng trung ương chỉ cut 25bp, quyết định “đúng consensus” vẫn có thể bị xem là hawkish so với giá thị trường.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **3. Surprise không chỉ là Actual - Forecast** nối từ **2. Baseline, consensus và thị trường (market / 시장) pricing** sang **4. CPI**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Surprise không chỉ là Actual - Forecast

Bất ngờ thống kê cần đọc cùng revisions và xu hướng.

```text
Headline Payroll +200k
nhưng
2 tháng trước bị revise -120k
```

khác hoàn toàn một bản +200k không có revision xấu.

Một bản phát hành (release / 릴리스) nên được đọc như chuỗi thời gian, không phải một điểm đơn lẻ.

# Phần II — Lạm phát

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **4. CPI** nối từ **3. Surprise không chỉ là Actual - Forecast** sang **5. MoM, YoY và cơ sở (base / 기반) tác động (effect / 효과)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. CPI

CPI đo thay đổi giá của một giỏ hàng tiêu dùng theo phương pháp thống kê cụ thể.

Cần tách:

```text
Headline
Core
Goods
Shelter
Services
Food
Energy
```

Cốt lõi (core / 핵심) loại food và năng lượng (energy / 에너지) vì biến động cao nhưng không đồng nghĩa “lạm phát thật”.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **5. MoM, YoY và cơ sở (base / 기반) tác động (effect / 효과)** nối từ **4. CPI** sang **6. Shelter lag**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. MoM, YoY và cơ sở (base / 기반) tác động (effect / 효과)

YoY dễ bị ảnh hưởng bởi mức so sánh năm trước.

Do đó cần nhìn thêm MoM và xu hướng ngắn hạn.

Ví dụ annualized gần đúng:

```text
3-month annualized
≈ (1 + cumulative 3m change)^4 - 1
```

Tốc độ ngắn hạn nhiễu hơn nhưng có thể phát hiện điểm ngoặt sớm hơn YoY.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **6. Shelter lag** nối từ **5. MoM, YoY và cơ sở (base / 기반) tác động (effect / 효과)** sang **7. Services ex housing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Shelter lag

Chỉ số nhà ở chính thức thường phản ứng chậm hơn giá thuê mới ngoài thị trường.

Do đó shelter CPI có thể còn cao ngay cả khi new-market rent đã giảm.

Khi đọc cần hiểu độ trễ của phương pháp đo.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **7. Services ex housing** nối từ **6. Shelter lag** sang **8. PCE**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Services ex housing

Một số analyst dùng dịch vụ ngoài nhà ở, đôi khi gọi không chính thức là “supercore”, để đánh giá áp lực dịch vụ.

Không có chỉ số thần kỳ. Điều quan trọng là biết ngân hàng trung ương đang chú ý chỉ số nào và vì sao.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **8. PCE** nối từ **7. Services ex housing** sang **9. PPI và giá nhập khẩu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. PCE

PCE có trọng số và phương pháp khác CPI và thường là thước đo quan trọng trong phân tích Fed.

PCE không nên được đọc tách khỏi cấu phần. Một phần thông tin PCE còn có thể được suy ra trước từ CPI/PPI nên mức bất ngờ thị trường không phải lúc nào cũng lớn.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **9. PPI và giá nhập khẩu** nối từ **8. PCE** sang **10. Kỳ vọng lạm phát**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. PPI và giá nhập khẩu

PPI và import prices giúp theo dõi áp lực giá ở upstream.

Nhưng pass-through tới CPI không 1:1 vì doanh nghiệp có thể:

- hấp thụ chi phí;
- tăng giá bán;
- cải thiện năng suất;
- đổi nhà cung cấp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **10. Kỳ vọng lạm phát** nối từ **9. PPI và giá nhập khẩu** sang **11. Payrolls**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Kỳ vọng lạm phát

Kỳ vọng có thể đến từ survey hoặc thị trường (market / 시장) breakeven.

Breakeven gần đúng:

```text
Nominal Yield - Real Yield
```

nhưng nó chứa cả inflation rủi ro (risk / 위험) premium và liquidity premium, nên không phải “dự báo lạm phát thuần”.

# Phần III — Thị trường lao động

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **11. Payrolls** nối từ **10. Kỳ vọng lạm phát** sang **12. Unemployment tỷ lệ (rate / 비율)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Payrolls

Báo cáo việc làm Mỹ thường có establishment survey và household survey.

Nonfarm payrolls đến từ establishment side; unemployment tỷ lệ (rate / 비율) chủ yếu từ household side.

Hai survey có thể phân kỳ trong một thời gian vì phương pháp khác nhau.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **12. Unemployment tỷ lệ (rate / 비율)** nối từ **11. Payrolls** sang **13. Participation và underemployment**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Unemployment tỷ lệ (rate / 비율)

Tỷ lệ thất nghiệp tăng có thể do:

- việc làm giảm;
- hoặc nhiều người quay lại labor force nhanh hơn tốc độ tạo việc làm.

Hai trường hợp có ý nghĩa khác nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **13. Participation và underemployment** nối từ **12. Unemployment tỷ lệ (rate / 비율)** sang **14. Wage và productivity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Participation và underemployment

Nên xem thêm:

- participation tỷ lệ (rate / 비율);
- employment-population ratio;
- underemployment;
- hours worked.

Một tỷ lệ unemployment duy nhất không mô tả đầy đủ labor thị trường (market / 시장).

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **14. Wage và productivity** nối từ **13. Participation và underemployment** sang **15. Jobless claims**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Wage và productivity

Tăng lương không tự động tạo lạm phát nếu năng suất tăng tương ứng.

Một trực giác:

```text
Unit Labor Cost
≈ Wage Growth - Productivity Growth
```

Đây là cầu nối tốt hơn giữa dữ liệu lương và áp lực giá dịch vụ.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **15. Jobless claims** nối từ **14. Wage và productivity** sang **16. JOLTS**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Jobless claims

Initial claims là chỉ báo tần suất cao về người mới xin trợ cấp thất nghiệp. Continuing claims cho biết tình trạng kéo dài.

Dữ liệu tuần rất nhiễu nên nên nhìn xu hướng nhiều tuần.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **16. JOLTS** nối từ **15. Jobless claims** sang **17. PMI/ISM là diffusion chỉ mục (index / 인덱스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. JOLTS

JOLTS gồm:

- job openings;
- hires;
- quits;
- layoffs.

Openings-to-unemployed cho biết nhu cầu lao động so với nguồn cung. Quits có thể phản ánh tự tin của người lao động.

# Phần IV — PMI và chu kỳ sản xuất

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **17. PMI/ISM là diffusion chỉ mục (index / 인덱스)** nối từ **16. JOLTS** sang **18. New orders và inventories**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. PMI/ISM là diffusion chỉ mục (index / 인덱스)

PMI trên 50 thường nghĩa hoạt động tăng so với kỳ trước; dưới 50 thường nghĩa giảm.

Nhưng cần đọc components:

- new orders;
- môi trường vận hành (production / 운영 환경);
- employment;
- prices paid;
- inventories;
- supplier deliveries.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **18. New orders và inventories** nối từ **17. PMI/ISM là diffusion chỉ mục (index / 인덱스)** sang **19. Retail sales**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. New orders và inventories

Một quan hệ hữu ích:

```text
New Orders ↑ + Inventories thấp
→ Production có thể phục hồi
```

Ngược lại:

```text
New Orders ↓ + Inventories cao
→ Destocking Risk ↑
```

Điều này đặc biệt hữu ích với manufacturing, semiconductor và shipping.

# Phần V — Tiêu dùng và hộ gia đình

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **19. Retail sales** nối từ **18. New orders và inventories** sang **20. Income, savings và credit**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Retail sales

Retail sales là số danh nghĩa, vì vậy doanh thu tăng có thể chỉ do giá tăng chứ không phải volume.

Cần đọc cùng:

- inflation;
- real disposable income;
- savings;
- credit-card growth;
- delinquency.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **20. Income, savings và credit** nối từ **19. Retail sales** sang **21. Housing là sector nhạy lãi suất**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Income, savings và credit

Chi tiêu có thể được tài trợ bằng:

- wage income;
- fiscal transfer;
- asset wealth;
- borrowing.

Tăng chi tiêu nhờ real income thường bền hơn tăng chi tiêu nhờ nợ tăng nhanh.

# Phần VI — Housing

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **21. Housing là sector nhạy lãi suất** nối từ **20. Income, savings và credit** sang **22. Housing truyền chính sách (policy / 정책) sang nền kinh tế**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Housing là sector nhạy lãi suất

Các dữ liệu quan trọng:

- mortgage rates;
- permits;
- starts;
- completions;
- new-home sales;
- existing-home sales;
- inventory;
- affordability.

Permits thường đi trước hoạt động xây dựng; starts cho biết activity hiện tại; completions ảnh hưởng nguồn cung.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **22. Housing truyền chính sách (policy / 정책) sang nền kinh tế** nối từ **21. Housing là sector nhạy lãi suất** sang **23. GDP theo chi tiêu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Housing truyền chính sách (policy / 정책) sang nền kinh tế

Lãi suất mortgage ảnh hưởng:

```text
Affordability
→ Home Sales
→ Construction
→ Furnishing / Broker Activity
→ Household Wealth
```

# Phần VII — GDP

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **23. GDP theo chi tiêu** nối từ **22. Housing truyền chính sách (policy / 정책) sang nền kinh tế** sang **24. Inventory có thể làm GDP nhiễu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. GDP theo chi tiêu

Sau khi đọc tiêu dùng, đầu tư và tồn kho riêng lẻ, ta cần ghép chúng thành cấu trúc GDP để biết headline tăng trưởng đến từ đâu. Công thức dưới đây là bản đồ phân rã, không phải kết luận rằng mọi thành phần đều có chất lượng như nhau.

```text
GDP = C + I + G + (X - M)
```

Cần phân rã headline tăng trưởng thành:

- consumption;
- fixed investment;
- inventories;
- government;
- net exports.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **24. Inventory có thể làm GDP nhiễu** nối từ **23. GDP theo chi tiêu** sang **25. GDP và GDI**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Inventory có thể làm GDP nhiễu

Inventory bản dựng (build / 빌드) có thể đẩy GDP lên dù final demand yếu.

Imports trừ trong công thức GDP nhưng nhập khẩu mạnh đôi khi phản ánh domestic demand mạnh, nên không thể kết luận “imports cao là xấu”.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **25. GDP và GDI** nối từ **24. Inventory có thể làm GDP nhiễu** sang **26. Một cuộc họp có nhiều lớp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. GDP và GDI

GDP đo từ phía sản lượng; GDI đo từ phía thu nhập. Về lý thuyết chúng phản ánh cùng nền kinh tế nhưng thực tế có sai số đo lường (measurement error / 측정 오차).

Cần nhìn xu hướng và revisions.

# Phần VIII — Central bank meeting

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **26. Một cuộc họp có nhiều lớp** nối từ **25. GDP và GDI** sang **27. Hawkish cut và dovish hike**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Một cuộc họp có nhiều lớp

Cần đọc:

```text
Decision
Statement
Economic Projections
Rate Path / Dots
Vote Split
Press Conference
```

Không nên chỉ nhìn “hike/cut/hold”.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **27. Hawkish cut và dovish hike** nối từ **26. Một cuộc họp có nhiều lớp** sang **28. hiện tại (current / 현재) tỷ lệ (rate / 비율) và expected đường dẫn (path / 경로)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Hawkish cut và dovish hike

Một lần cut có thể hawkish nếu guidance cho thấy ít cut hơn về sau.

Một lần hike có thể dovish nếu ngân hàng trung ương ám chỉ chu kỳ tăng đã gần kết thúc.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **27. Hawkish cut và dovish hike** đặt đầu vào cho **28. hiện tại (current / 현재) tỷ lệ (rate / 비율) và expected đường dẫn (path / 경로)**, rồi **29. Nominal yield, real yield và breakeven** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. hiện tại (current / 현재) tỷ lệ (rate / 비율) và expected đường dẫn (path / 경로)

Tài sản chiết khấu lãi suất tương lai, không chỉ chính sách (policy / 정책) tỷ lệ (rate / 비율) hôm nay.

2Y yield và OIS/futures thường giúp đọc repricing ở đầu đường cong.

# Phần IX — Bond thị trường (market / 시장)

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **28. hiện tại (current / 현재) tỷ lệ (rate / 비율) và expected đường dẫn (path / 경로)** đặt đầu vào cho **29. Nominal yield, real yield và breakeven**, rồi **30. 2Y và 10Y** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. Nominal yield, real yield và breakeven

Nominal yield có thể thay đổi do:

- expected chính sách (policy / 정책);
- expected inflation;
- real growth;
- term premium.

Real yield đặc biệt quan trọng với định giá tài sản duration dài.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **30. 2Y và 10Y** nối từ **29. Nominal yield, real yield và breakeven** sang **31. Yield curve**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. 2Y và 10Y

2Y nhạy với expected chính sách (policy / 정책) gần hạn.

10Y phản ánh nhiều hơn:

- long-run growth;
- inflation;
- term premium;
- Treasury supply.

Một CPI nóng làm 2Y +15bp, 10Y +5bp khác hẳn một fiscal shock làm 10Y +20bp nhưng 2Y gần như không đổi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **31. Yield curve** nối từ **30. 2Y và 10Y** sang **32. Term premium**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Yield curve

Đường cong không chỉ được đọc qua độ dốc mà còn cần biết toàn bộ yield đang tăng hay giảm.

```text
Bull Steepening
Bull Flattening
Bear Steepening
Bear Flattening
```

Tên gọi chỉ hữu ích khi hiểu nguyên nhân kinh tế phía sau.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **32. Term premium** nối từ **31. Yield curve** sang **33. Credit spread**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Term premium

Phần bù kỳ hạn (term premium) là phần bù cho việc nắm duration dài trong bất định.

Nó có thể tăng do:

- fiscal issuance;
- inflation bất định (uncertainty / 불확실성);
- QT;
- giảm nhu cầu từ người mua lớn.

Long-end yield tăng vì term premium có thể thắt financial conditions dù Fed không hawkish hơn.

# Phần X — Credit

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **33. Credit spread** nối từ **32. Term premium** sang **34. Refinancing calendar**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Credit spread

Spread tăng có thể phản ánh:

- default rủi ro (risk / 위험);
- liquidity rủi ro (risk / 위험);
- rủi ro (risk / 위험) aversion;
- technical selling.

Government yield giảm nhưng high-yield spread tăng mạnh thường là tín hiệu tăng trưởng/tín dụng xấu đi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **34. Refinancing calendar** nối từ **33. Credit spread** sang **35. Bank lending standards**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Refinancing calendar

Tác động lãi suất thường có độ trễ vì nợ cố định chỉ repricing khi đáo hạn.

Cần xem maturity wall chứ không chỉ chính sách (policy / 정책) tỷ lệ (rate / 비율).

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **35. Bank lending standards** nối từ **34. Refinancing calendar** sang **36. Financial conditions rộng hơn chính sách (policy / 정책) tỷ lệ (rate / 비율)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Bank lending standards

Khảo sát lending standards giúp nối chính sách (policy / 정책) tới real economy.

Nếu bank tightening và loan demand cùng giảm, credit impulse có thể yếu ngay cả khi central bank đã dừng hike.

# Phần XI — Financial conditions

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **36. Financial conditions rộng hơn chính sách (policy / 정책) tỷ lệ (rate / 비율)** nối từ **35. Bank lending standards** sang **37. FX luôn là tương đối**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Financial conditions rộng hơn chính sách (policy / 정책) tỷ lệ (rate / 비율)

Điều kiện tài chính gồm:

- rates;
- credit spreads;
- equity prices;
- FX;
- lending standards;
- thuộc tính (property / 속성) prices.

Hai nền kinh tế cùng chính sách (policy / 정책) tỷ lệ (rate / 비율) vẫn có thể có financial conditions rất khác.

# Phần XII — FX

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **37. FX luôn là tương đối** nối từ **36. Financial conditions rộng hơn chính sách (policy / 정책) tỷ lệ (rate / 비율)** sang **38. Carry và funding currency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. FX luôn là tương đối

Một đồng tiền mạnh hay yếu phải so với đồng còn lại.

Khung cơ bản:

```text
Relative Rates
+ Relative Growth
+ External Balance
+ Carry
+ Risk Flow
+ Positioning
```

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **38. Carry và funding currency** nối từ **37. FX luôn là tương đối** sang **39. Oil: demand shock và supply shock**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Carry và funding currency

Carry tốt khi volatility thấp nhưng có thể đảo chiều mạnh trong risk-off.

Funding currency đôi khi tăng trong deleveraging dù lãi suất thấp.

# Phần XIII — Commodities

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **39. Oil: demand shock và supply shock** nối từ **38. Carry và funding currency** sang **40. Industrial metals**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Oil: demand shock và supply shock

Dầu tăng vì demand mạnh có thể đi cùng growth tốt.

Dầu tăng vì geopolitics hoặc supply disruption có thể tạo:

```text
Inflation ↑
Growth ↓
```

và mang tính stagflationary.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **40. Industrial metals** nối từ **39. Oil: demand shock và supply shock** sang **41. Gold**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Industrial metals

Copper và metals chịu ảnh hưởng của:

- China;
- manufacturing;
- inventories;
- mine supply;
- positioning.

Giá hàng hóa vừa là chỉ báo kinh tế vừa là đầu vào (input / 입력) chi phí (cost / 비용).

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **41. Gold** nối từ **40. Industrial metals** sang **42. Revision**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. Gold

Các biến chính:

- real yields;
- USD;
- central-bank demand;
- geopolitics;
- confidence in chính sách (policy / 정책) regime.

Không dùng quy tắc cơ học “inflation ↑ → gold ↑”.

# Phần XIV — Lỗi đọc dữ liệu phổ biến

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **42. Revision** nối từ **41. Gold** sang **43. Seasonality**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Revision

Dữ liệu kinh tế thường được sửa đổi.

Không nên xây thesis lớn trên một print đầu tiên nếu series vốn có revision lớn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **43. Seasonality** nối từ **42. Revision** sang **44. cơ sở (base / 기반) tác động (effect / 효과)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. Seasonality

Seasonal adjustment không hoàn hảo. Các kỳ nghỉ, thời tiết hoặc lịch Tết có thể làm dữ liệu méo.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **44. cơ sở (base / 기반) tác động (effect / 효과)** nối từ **43. Seasonality** sang **45. sai số đo lường (measurement error / 측정 오차)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. cơ sở (base / 기반) tác động (effect / 효과)

Khi YoY thay đổi mạnh, luôn kiểm tra mốc so sánh năm trước và momentum gần đây.

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **44. cơ sở (base / 기반) tác động (effect / 효과)** đặt vấn đề; **45. sai số đo lường (measurement error / 측정 오차)** đối chiếu bằng chứng, rồi **46. Positioning** mở rộng hệ quả hoặc giới hạn liên quan.

## 45. sai số đo lường (measurement error / 측정 오차)

Dữ liệu survey là ước tính, không phải đo toàn bộ nền kinh tế với độ chính xác tuyệt đối.

Nên tìm xác nhận từ nhiều series độc lập.

# Phần XV — Positioning và phản hồi giá

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **45. sai số đo lường (measurement error / 측정 오차)** đặt vấn đề; **46. Positioning** đối chiếu bằng chứng, rồi **47. Reflexivity** mở rộng hệ quả hoặc giới hạn liên quan.

## 46. Positioning

Tin xấu có thể làm thị trường tăng nếu nhà đầu tư đã còn bi quan hơn trước bản phát hành (release / 릴리스).

Tin tốt có thể làm thị trường giảm nếu positioning quá crowded long.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **47. Reflexivity** nối từ **46. Positioning** sang **48. Growth và inflation surprise**, vì cơ chế trước tạo đầu vào cho bước sau.

## 47. Reflexivity

Giá tài sản có thể quay lại ảnh hưởng economy:

```text
Equity / Property ↑
→ Wealth / Collateral ↑
→ Spending / Credit ↑
```

và chiều ngược lại.

# Phần XVI — Regime ma trận (matrix / 행렬)

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **48. Growth và inflation surprise** nối từ **47. Reflexivity** sang **49. Trước bản phát hành (release / 릴리스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 48. Growth và inflation surprise

Một ma trận đơn giản:

```text
Growth ↑ / Inflation ↓
→ Goldilocks-like

Growth ↑ / Inflation ↑
→ Overheating risk

Growth ↓ / Inflation ↓
→ Easing / Deflationary risk

Growth ↓ / Inflation ↑
→ Stagflationary risk
```

Credit và liquidity có thể làm ma trận này mất tác dụng nếu hệ thống tài chính đang stress.

# Phần XVII — Quy trình đọc một sự kiện

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **49. Trước bản phát hành (release / 릴리스)** nối từ **48. Growth và inflation surprise** sang **50. Ngay sau bản phát hành (release / 릴리스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 49. Trước bản phát hành (release / 릴리스)

Ghi lại:

```text
Consensus
Prior / Revision Risk
Market Pricing
Yield Curve
FX
Positioning
Option Implied Move
Your Baseline
```

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **50. Ngay sau bản phát hành (release / 릴리스)** nối từ **49. Trước bản phát hành (release / 릴리스)** sang **51. Sau vài giờ / cuối ngày**, vì cơ chế trước tạo đầu vào cho bước sau.

## 50. Ngay sau bản phát hành (release / 릴리스)

Đừng chỉ nhìn headline. Kiểm tra:

```text
Actual vs Consensus
Composition
Revisions
2Y
10Y
Real Yield
USD
Credit Spread
Equity Breadth
```

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **51. Sau vài giờ / cuối ngày** nối từ **50. Ngay sau bản phát hành (release / 릴리스)** sang **52. Sau vài ngày**, vì cơ chế trước tạo đầu vào cho bước sau.

## 51. Sau vài giờ / cuối ngày

Hỏi:

```text
Market đang diễn giải release thành growth shock,
inflation shock hay policy shock?
```

Theo dõi xem phản ứng ban đầu có được xác nhận bởi nhiều tài sản hay không.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **52. Sau vài ngày** nối từ **51. Sau vài giờ / cuối ngày** sang **53. sự kiện (event / 이벤트) ghi chú (note / 노트) chuẩn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 52. Sau vài ngày

Kiểm tra:

- analyst revisions;
- chính sách (policy / 정책) communication;
- credit conditions;
- sector hiệu năng (performance / 성능);
- whether positioning reversed.

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **53. sự kiện (event / 이벤트) ghi chú (note / 노트) chuẩn** nối từ **52. Sau vài ngày** sang **54. Inflation sự kiện (event / 이벤트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 53. sự kiện (event / 이벤트) ghi chú (note / 노트) chuẩn

Event note là mẫu ghi chép biến một release thành quy trình có thể review: kỳ vọng trước sự kiện, số thực tế, mức bất ngờ, cấu phần, phản ứng chính sách và phản ứng tài sản. Hãy điền nó trước khi câu chuyện sau sự kiện làm lệch trí nhớ.

```text
Event:
Consensus:
Actual:
Revision:
Composition:
What was priced:
Reaction function change:
2Y / 10Y / Real Yield:
FX:
Credit:
Equities:
Commodities:
My interpretation:
What would invalidate it:
```

# Phần XVIII — Chuỗi nhân quả cốt lõi

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **54. Inflation sự kiện (event / 이벤트)** nối từ **53. sự kiện (event / 이벤트) ghi chú (note / 노트) chuẩn** sang **55. Growth sự kiện (event / 이벤트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 54. Inflation sự kiện (event / 이벤트)

Với một sự kiện lạm phát, mục tiêu không phải chỉ ghi CPI tăng/giảm mà là xác định thành phần nào tạo surprise và điều đó thay đổi đường đi chính sách ra sao. Mẫu dưới đây giúp nối dữ liệu với yield, FX, credit và equities.

```text
CPI Surprise
→ Persistence Assessment
→ Reaction Function
→ Expected Policy Path
→ 2Y / Real Yield
→ USD
→ Equity Multiple / Credit
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **55. Growth sự kiện (event / 이벤트)** nối từ **54. Inflation sự kiện (event / 이벤트)** sang **56. Credit sự kiện (event / 이벤트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 55. Growth sự kiện (event / 이벤트)

Với dữ liệu tăng trưởng, cần tách tốc độ headline khỏi chất lượng cầu cuối, tồn kho và đóng góp chính phủ. Câu hỏi dẫn đường là nền kinh tế đang mở rộng bền vững hay chỉ được nâng bởi một thành phần tạm thời.

```text
Growth Surprise
→ Earnings Expectation
→ Policy Expectation
→ Yields / FX
→ Cyclicals vs Defensives
```

> **Nối mạch:** Trong **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **56. Credit sự kiện (event / 이벤트)** nối từ **55. Growth sự kiện (event / 이벤트)** sang **Kết luận**, vì cơ chế trước tạo đầu vào cho bước sau.

## 56. Credit sự kiện (event / 이벤트)

Credit event cần được đọc qua spread, điều kiện tái cấp vốn, tài sản thế chấp và khả năng truyền dẫn sang doanh nghiệp/ngân hàng. Đừng dừng ở việc ghi spread mở rộng; hãy xác định lớp thanh khoản hoặc solvency nào đang thay đổi.

```text
Funding Stress
→ Spread Widening
→ Lending Tightening
→ Growth Revision
→ Policy Response
```

> **Nối mạch:** Ở chặng này của **Cẩm nang đọc dữ liệu vĩ mô: từ số liệu tới phản ứng tài sản**, **Kết luận** tổng hợp từ **56. Credit sự kiện (event / 이벤트)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết luận

Đọc macro dữ liệu (data / 데이터) tốt không phải đoán headline. Mục tiêu là hiểu **thông tin mới đã thay đổi phân phối xác suất như thế nào** và thị trường đang phản ánh sự thay đổi đó qua bond, FX, credit và equity ra sao.

Chuỗi quan trọng nhất cần ghi nhớ là:

```text
Actual
→ Surprise
→ Composition
→ Reaction Function
→ Yields / FX / Credit
→ Earnings / Valuation
→ Asset Reaction
```

> **Bàn giao:** Sau **Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
