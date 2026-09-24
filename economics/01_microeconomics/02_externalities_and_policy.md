# Externalities & Policy — Khi private decision khác social outcome

Externality (`외부효과`) xuất hiện khi hành động của một actor tạo cost hoặc benefit cho người khác nhưng phần effect đó không được phản ánh đầy đủ trong market price hoặc contract giữa các bên. Đây là một trong những lý do quan trọng khiến private equilibrium có thể khác social optimum.

Externality không đồng nghĩa đơn giản với “ảnh hưởng đến người khác”. Nếu effect đã được internalize qua price, property right hoặc contract thì nó không còn là externality theo nghĩa kinh tế học. Câu hỏi cốt lõi là: **decision-maker có đối mặt với đầy đủ marginal social consequence của hành động mình hay không?**

## 1. Private marginal cost và social marginal cost

Giả sử một factory sản xuất output `q`. Firm nhìn private marginal cost (PMC), nhưng production tạo pollution damage cho cộng đồng.

Khi đó:

```text
SMC = PMC + Marginal External Damage
```

Nếu market demand phản ánh social marginal benefit và không có external benefit, competitive equilibrium xảy ra nơi:

```text
PMB = PMC
```

trong khi social optimum xảy ra nơi:

```text
SMB = SMC
```

Nếu `SMC > PMC`, market thường sản xuất quá nhiều so với social optimum. Đây là negative production externality.

## 2. Positive externality và under-provision

Externality có thể dương. Vaccination, basic research hoặc một số hoạt động giáo dục có thể tạo benefit cho người ngoài decision.

Khi consumer chỉ nhìn private marginal benefit (PMB) nhưng xã hội nhận thêm external benefit:

```text
SMB = PMB + Marginal External Benefit
```

Nếu `SMB > PMB`, private market có thể cung cấp ít hơn social optimum.

Điều quan trọng là không gắn nhãn “positive” hoặc “negative” theo cảm xúc. Phải xác định margin, beneficiary, harmed party và causal channel cụ thể.

## 3. Externality tạo wedge như thế nào

Trong welfare chapter, tax tạo wedge giữa buyer price và seller price. Externality tạo wedge giữa private signal và social consequence.

Ví dụ pollution:

```text
Private decision rule:
produce while MB ≥ PMC

Social decision rule:
produce while SMB ≥ SMC
```

Khoảng cách `SMC − PMC` tại mỗi quantity là marginal external damage. Nếu khoảng cách này không được internalize, firm không có incentive tự nhiên để giảm activity đến social optimum.

## 4. Pigouvian tax và logic internalization

Pigouvian tax đặt tax trên activity gây external cost sao cho private marginal cost sau tax gần bằng social marginal cost.

Trong idealized case:

```text
Pigouvian tax per unit = Marginal External Damage at social optimum
```

Tax không cần “trừng phạt” actor; mục tiêu của nó là thay đổi price signal để actor nhìn thấy social cost tại margin.

Nếu tax đúng mức và information hoàn hảo, firm tối ưu lợi nhuận tư nhân có thể tự chọn quantity gần social optimum.

Nhưng implementation khó vì regulator cần ước lượng damage, monitor activity, phân biệt heterogeneous sources và xử lý uncertainty.

## 5. Subsidy cho positive externality

Với positive externality, subsidy có thể làm private marginal benefit hoặc effective return tăng về phía social marginal benefit.

Trong benchmark:

```text
optimal subsidy ≈ Marginal External Benefit at social optimum
```

Tuy nhiên subsidy cũng có fiscal cost, fraud risk, targeting problem và possibility of subsidizing activity vốn đã xảy ra. Vì vậy cần phân biệt additionality: bao nhiêu behavior thật sự thay đổi vì subsidy.

## 6. Quantity regulation và standard

Thay vì dùng price, regulator có thể đặt quantity cap, emission standard hoặc technology standard.

Nếu mọi firm có marginal abatement cost giống nhau và regulator biết chính xác optimum, command-and-control có thể đạt target. Trong thực tế marginal abatement cost khác nhau rất lớn.

Một uniform technology mandate có thể buộc firm chi phí cao và thấp cùng dùng một solution, trong khi price-based instrument cho phép mỗi firm tự chọn cách giảm cost thấp nhất.

## 7. Tradable permits và cap-and-trade

Cap-and-trade đặt tổng quantity pollution rồi phân bổ hoặc auction permits. Firms có abatement cost thấp sẽ giảm nhiều và bán permit; firms có abatement cost cao sẽ mua permit.

Nếu market permit hoạt động tốt, trading làm marginal abatement cost hội tụ:

```text
MAC_1 = MAC_2 = ... = Permit Price
```

Đây là điểm mạnh của tradable permits: regulator chọn total quantity, market giúp phân bổ abatement giữa sources.

Tax và permit khác ở thứ regulator cố định:

```text
Tax  → cố định price của pollution
Permit → cố định quantity của pollution
```

Khi uncertainty lớn, lựa chọn price hay quantity phụ thuộc slope của marginal damage và marginal abatement cost, volatility, monitoring và political constraints.

## 8. Coase theorem và property rights

Coase theorem đưa ra một benchmark mạnh: nếu property rights rõ, transaction cost bằng 0 và parties có thể bargain đầy đủ, họ có thể đạt efficient allocation bất kể quyền ban đầu thuộc về ai.

Ví dụ một factory gây noise cho hotel. Nếu hotel có quyền im lặng, factory có thể trả tiền để được gây noise khi production value lớn hơn damage. Nếu factory có quyền gây noise, hotel có thể trả để factory giảm noise khi damage lớn hơn production value.

Trong frictionless model, final efficient quantity có thể giống nhau dù distribution khác nhau.

Nhưng theorem không nói bargaining luôn giải quyết externality ngoài đời. Khi có hàng nghìn affected parties, asymmetric information, bargaining cost, strategic holdout, unclear causality hoặc enforcement problem, transaction cost phá vỡ benchmark.

## 9. Property rights không chỉ là “tư hữu hóa”

Property right là tập quyền sử dụng, loại trừ, chuyển nhượng và hưởng lợi. Nhiều environmental hoặc digital resources khó define rights hoàn chỉnh.

Atmosphere, biodiversity, public space hoặc privacy data có boundaries phức tạp. Việc gán rights còn liên quan legitimacy, distribution và enforcement.

Do đó Coasean analysis hữu ích nhất khi hỏi: externality tồn tại vì missing right nào, contracting friction nào và transaction cost nào?

## 10. Network externality và platform market

Network effect xảy ra khi utility của một user phụ thuộc số hoặc composition của users khác. Direct network effect có thể xuất hiện ở communication network; indirect network effect xuất hiện khi nhiều users thu hút complementors như developers hoặc merchants.

Không phải mọi network effect đều là market failure cần policy. Một platform có thể internalize phần effect qua pricing hai phía. Ngược lại, lock-in, tipping và compatibility issue có thể tạo market power.

Vì vậy cần tách ba concept:

- technological network effect;
- externality chưa được internalize;
- strategic market power.

## 11. Congestion và common access

Road congestion là ví dụ negative externality: mỗi driver tính private travel cost của mình nhưng không tính delay gây thêm cho drivers khác.

Congestion pricing đặt charge gần marginal congestion cost vào thời gian/location gây tắc.

Nhưng effect phụ thuộc alternatives. Nếu public transport yếu hoặc commuting schedule không linh hoạt, incidence có thể rơi mạnh vào nhóm income thấp. Đây là nơi welfare và distribution phải được phân tích cùng nhau.

## 12. Double dividend và policy interaction

Environmental tax vừa có thể giảm externality vừa tạo revenue. Revenue có thể dùng để giảm distortionary tax khác hoặc transfer cho households.

Nhưng không nên tự động kết luận có “double dividend”. Tax interaction với labor supply, capital, energy input và existing regulation có thể tạo distortion mới.

Policy analysis cần nhìn full system:

```text
Gross environmental benefit
− abatement/resource cost
− administrative cost
− tax interaction effects
+ value of recycled revenue
```

## 13. Government failure và imperfect intervention

Market failure là lý do để xem xét intervention, không phải proof rằng intervention cụ thể cải thiện welfare.

Government có thể thiếu information, bị regulatory capture, tạo rent-seeking, đặt standard lỗi thời hoặc monitor kém. Policy cũng tạo behavioral adaptation và loopholes.

Vì vậy comparison đúng là:

```text
Imperfect market outcome
vs.
Imperfect feasible policy outcome
```

không phải “market thực tế” so với “government hoàn hảo”.

## 14. Behavioral externality và paternalism

Một số policy tranh luận dựa trên “internality”: decision-maker gây cost cho chính future self vì present bias, addiction hoặc limited attention.

Đây không phải externality truyền thống vì harmed party vẫn là cùng cá nhân qua thời gian. Tuy nhiên behavioral public economics có thể dùng tax, default hoặc information intervention để sửa decision bias.

Cần giữ boundary rõ: evidence về cognitive bias không tự động xác định optimal policy, vì regulator cũng có information limit và value judgment.

## 15. Empirical identification của externality

Để policy đúng, phải đo causal external damage hoặc benefit. Correlation không đủ.

Ví dụ muốn đo pollution ảnh hưởng health, cần tách pollution khỏi income, industrial composition, weather và location sorting. Research có thể dùng natural experiment, instrumental variable, regression discontinuity hoặc panel design tùy setting.

Đây là lý do Economics cần Econometrics: theoretical wedge cho biết cần đo gì, econometric design cho biết claim có causal credibility hay không.

## 16. Failure modes thường gặp

Sai lầm thứ nhất là gọi mọi side effect là externality dù đã được price hoặc contract internalize.

Sai lầm thứ hai là chọn tax bằng average damage thay vì marginal damage tại relevant quantity.

Sai lầm thứ ba là nghĩ Coase theorem nói “không cần chính phủ”. Theorem là benchmark về transaction cost bằng 0; chính transaction cost thực tế mới quyết định institutional design.

Sai lầm thứ tư là tối ưu efficiency nhưng bỏ qua incidence, enforcement và political feasibility.

## 17. Mental model khi phân tích externality

Khi gặp một case, hãy hỏi theo sequence:

1. Action nào tạo spillover?
2. Ai quyết định và ai chịu effect?
3. Effect đã được internalize qua price, contract hoặc ownership chưa?
4. PMC/PMB khác SMC/SMB ở đâu?
5. Market quantity cao hơn hay thấp hơn social optimum?
6. Instrument nào tác động đúng margin: tax, subsidy, cap, permit, bargaining hay information?
7. Regulator cần biết gì để calibrate instrument?
8. Ai chịu incidence và có behavioral response nào?
9. Monitoring, transaction cost và government failure có làm policy đổi ranking không?

Externality cho thấy vì sao market price đôi khi không mang đầy đủ social information. Public goods đẩy vấn đề đi xa hơn: đôi khi market thậm chí không thể dễ dàng charge từng beneficiary vì hàng hóa **non-rival** và **non-excludable**.
