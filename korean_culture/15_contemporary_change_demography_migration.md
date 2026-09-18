# Biến đổi đương đại: dân số, thế hệ, di cư và tái cấu trúc chuẩn mực

## Văn hoá thay đổi khi constraint thay đổi

Nếu chỉ học “truyền thống Hàn Quốc”, ta dễ nhận diện những symbol nhưng dự đoán sai xã hội đang sống. Culture không đứng ngoài demography và economy. Khi household nhỏ hơn, tuổi thọ dài hơn, phụ nữ tham gia labour market nhiều hơn, immigration tăng và smartphone trở thành infrastructure, incentive của hành vi thay đổi.

Một rule hữu ích là:

> Khi cost, benefit và available option của một practice thay đổi đủ mạnh, symbolic value có thể còn nhưng implementation sẽ bị thương lượng lại.

## 초고령사회: xã hội siêu già và đảo chiều quan hệ thế hệ

Statistics Korea công bố rằng năm 2025, người từ 65 tuổi trở lên chiếm khoảng **20,3%** dân số Hàn Quốc. Mốc trên 20% thường được gọi là **super-aged society / 초고령사회** theo convention quốc tế được dùng rộng rãi.

Già hoá không chỉ nghĩa nhiều người già hơn. Nó thay dependency ratio, health-care demand, pension finance, housing và labour supply. Nếu số worker trên mỗi retiree giảm, một welfare system pay-as-you-go chịu constraint mạnh hơn.

Cultural consequence là nghĩa vụ `효` không thể chỉ dựa vào family care như trước. Household ít con và geographic separation làm elder care phải chuyển một phần sang market, insurance và public service.

## 저출산: birthrate thấp là system output

Theo `2024 한국의 사회지표`, total fertility rate năm 2024 là khoảng **0,75**, tăng so với năm trước nhưng vẫn rất thấp. Dữ liệu này mô tả một period, không phải “tính cách dân tộc”.

Fertility là outcome của nhiều decision dưới uncertainty. Housing, job security, childcare, career cost, marriage timing, gender division và education expectation tương tác. Nếu mỗi factor tăng cost một chút, product effect có thể lớn.

Ta có thể hình dung probability of choosing childbirth như logistic response với nhiều variables, không cần coi đây là model official:

```math
P(\text{birth decision}) = \sigma(\beta_0 + \beta_1H + \beta_2J + \beta_3C + \beta_4G + \cdots)
```

`H` có thể đại diện housing constraint, `J` job security, `C` childcare support, `G` gender-workload balance. Mental model nhắc rằng không có “một nguyên nhân duy nhất”.

## 1인가구: hộ một người và sự tái thiết kế của đời sống

Household projection công bố năm 2024 dự báo one-person households tăng từ **7,39 triệu (34,1% household) năm 2022** lên khoảng **9,62 triệu (41,3%) năm 2052**. Đây là projection, không phải số chắc chắn tương lai; assumption có thể đổi.

Hộ một người tăng vì nhiều path: người trẻ sống độc lập, không kết hôn, ly hôn, separation do work, widowhood ở người cao tuổi. Vì vậy `혼자 산다` không đồng nghĩa một lifestyle category duy nhất.

Market response gồm `혼밥` — ăn một mình, `혼술` — uống một mình, portion nhỏ, studio, single-person appliance và subscription. Một hành vi từng dễ bị xem là “cô đơn” có thể bình thường hoá khi base rate tăng.

## 혼밥 và stigma decay

Khi practice hiếm, observer có thể infer social isolation. Khi practice phổ biến, cùng signal mất meaning cũ. Đây là Bayesian update: prior thay đổi theo base rate.

Nếu 5% người ăn một mình, seeing solo diner có thể signal unusual circumstance; nếu 40% household là solo, inference yếu đi. Culture thay đổi một phần vì statistics thay đổi.

## 비혼, 만혼 và marriage như lựa chọn chứ không checkpoint bắt buộc

**Non-marriage / 비혼** khác `미혼` — chưa kết hôn. `비혼` thường mang sắc thái lựa chọn hoặc identity rằng không đặt marriage như mục tiêu bắt buộc. **Late marriage / 만혼** phản ánh education dài hơn, career entry, housing và changed norms.

Khi marriage không còn universal transition, nhiều institution từng gắn quyền lợi với married household phải adapt: housing, taxation, inheritance, caregiving và workplace benefit.

## 세대 담론: X세대, MZ세대, 586 và nguy cơ overfit

Korean media dùng nhiều generational labels. Chúng hữu ích để nói về cohort shared experience, nhưng dễ biến thành horoscope.

Một cohort lớn lên trước broadband khác cohort smartphone-first; một cohort vào labour market trong high-growth era khác cohort gặp housing inflation và precarious work. Những historical exposure thật sự có explanatory value. Nhưng within-generation variance theo income, gender, region và education vẫn lớn.

Trong machine learning, nếu model dùng `generation` để explain mọi behavior, nó overfits narrative và underfits individuals.

## 외국인 주민 và Korea đa văn hoá hơn

Số foreign residents và long-term foreign nationals ở Hàn Quốc tăng trong nhiều năm. `2024 한국의 사회지표` ghi số foreign long-term residents năm 2023 khoảng **1,882 triệu**, tăng đáng kể so với năm trước.

Migration đến từ work, study, marriage, professional career và diaspora return. Điều này làm classroom, factory, farm, university và corporate team multilingual hơn.

**Multicultural family / 다문화가정** là category policy thường dùng, nhưng label cũng có thể othering nếu mọi family có foreign member bị coi “ngoài Korean norm” vĩnh viễn. Second generation đặt câu hỏi mới: Koreanness dựa vào bloodline, citizenship, language hay lived participation?

## 노동이주 và invisible infrastructure

Nhiều sector như manufacturing, agriculture, construction và care phụ thuộc migrant labour. Người tiêu dùng có thể không nhìn thấy labour chain đằng sau low-cost service hoặc food.

Culture of hospitality với foreign professional ở Seoul không đại diện experience của migrant worker ở factory/rural area. Class và visa status là variables quan trọng.

## 여성과 남성 역할: từ role mặc định sang negotiation

Gender role thay nhanh khi female education và employment tăng, family size giảm và expectation về individual career mạnh hơn. Nhưng domestic care không tự động phân phối lại cùng tốc độ.

Khi workplace vẫn giả định “ideal worker” có người khác lo home, dual-income household gặp time conflict. Đây là mismatch giữa two subsystems: labour institution update chậm hơn household reality.

Tranh luận gender ở Korea có thể rất polarized; culture book nên giải thích structural issue mà không gán một worldview duy nhất cho nam/nữ hay thế hệ.

## 고령층과 디지털: digital divide không chỉ là access

Statistics Korea cho biết năm 2024 khoảng **76,9%** người từ 65 tuổi trở lên sử dụng Internet, và messenger usage ở nhóm này rất cao. Điều này phá stereotype “người già = offline”.

Digital divide chuyển từ access sang skill, security và service design. Có smartphone không đồng nghĩa dễ dùng banking app, government certificate hay anti-phishing protection.

Universal design cần giảm cognitive load thay vì blame user.

## 지방소멸: dân số và feedback loop địa phương

Population decline ngoài capital region dẫn đến school closure, medical access giảm và local commerce suy yếu. Khi service giảm, người trẻ càng có incentive rời đi. Đây là feedback loop khó break.

`지방소멸` — “local extinction” — là term policy mạnh, nhưng không nên hiểu literal rằng region biến mất ngay; nó chỉ risk demographic sustainability.

## 환경과 기후: season truyền thống trong khí hậu thay đổi

Kimjang timing, crop, fishery và seasonal festival đều dựa climate regime. Climate change làm nhiệt độ và ecosystem shift, vì vậy “traditional seasonal knowledge” cũng phải adapt.

Culture không đứng ngoài climate science. Nếu average temperature đổi, fermentation speed, agriculture zone và disaster risk đổi theo. Heritage preservation tương lai có thể cần environmental adaptation.

## Hallyu ngược trở lại domestic identity

Khi Korean content được global audience yêu thích, domestic creators và consumers cũng nhìn culture mình qua international mirror. Food name, hanbok, traditional motif được rebranded và remix.

Đây là feedback globalization: local → global → local. Culture không chỉ export một chiều.

## Mental Model

> Văn hoá đương đại là equilibrium tạm thời giữa population structure, market, technology, law và memory. Khi một trong các biến nền đổi nhanh — như household size hay smartphone adoption — norm có thể đổi trong một thế hệ dù symbol cũ vẫn còn.

## Common Misconceptions

“Birthrate thấp vì giới trẻ ích kỷ” là causal claim đơn giản hoá một systems problem.

“One-person household = young single” sai vì elderly one-person household là component lớn và tăng.

“Korea là homogeneous society” ngày càng kém chính xác về lived population, dù national identity lịch sử vẫn mạnh.

“MZ generation có một personality chung” là category error.

## Dữ liệu cập nhật dùng trong chương

- 국가데이터처, `2025 고령자 통계`: tỷ lệ 65+ năm 2025 là 20,3%.
- 국가데이터처, `2024 한국의 사회지표`, công bố 25/3/2025: tổng dân số 2024 khoảng 51,75 triệu; TFR 2024 khoảng 0,75; long-term foreign residents 2023 khoảng 1,882 triệu.
- Statistics Korea, `Household Projections for Korea (2022–2052)`, công bố 12/9/2024: one-person households 7,39 triệu năm 2022, projection 9,62 triệu năm 2052.
- 국가데이터처, `한국의 사회동향 2025`: các biến đổi về labour, housing, private education, ageing và social conditions.
