# Welfare & Market Efficiency — Surplus, incidence và điều kiện để thị trường hiệu quả

Welfare economics hỏi một câu khác với consumer hoặc producer theory. Consumer theory hỏi household chọn gì; producer theory hỏi firm sản xuất bao nhiêu; welfare economics hỏi **kết quả chung có sử dụng nguồn lực theo cách tạo ra nhiều giá trị nhất trong mô hình hay không, ai nhận phần giá trị đó, và kết luận này phụ thuộc vào assumption nào**.

Điểm quan trọng là không đồng nhất ba câu hỏi khác nhau: hiệu quả (`efficiency`), phân phối (`distribution`) và công bằng (`equity`). Một allocation có thể hiệu quả theo nghĩa Pareto nhưng phân phối rất bất bình đẳng. Ngược lại, một policy có thể giảm total surplus nhưng được xã hội chấp nhận vì mục tiêu phân phối hoặc bảo hiểm rủi ro.

## 1. Willingness to pay và willingness to accept

Ở phía consumer, willingness to pay (WTP) là mức tối đa người mua sẵn sàng trả cho một đơn vị hàng hóa tại margin. Trong mô hình demand chuẩn, demand curve có thể đọc như marginal willingness to pay.

Nếu một người sẵn sàng trả 12 cho một đơn vị nhưng market price là 8, phần chênh lệch 4 là consumer surplus của đơn vị đó. Với nhiều đơn vị, consumer surplus là diện tích giữa demand curve và market price trên quantity thực sự mua.

Ở phía producer, supply curve trong cạnh tranh hoàn hảo thường phản ánh marginal cost của đơn vị biên. Nếu firm sẵn sàng bán một đơn vị khi giá ít nhất là 5 nhưng market price là 8, producer surplus của đơn vị đó là 3. Producer surplus khác accounting profit vì fixed cost và economic cost có thể được xử lý khác nhau tùy context.

## 2. Total surplus và social gains from trade

Trong baseline không có externality, market power, tax distortion hoặc information problem:

```text
Total Surplus = Consumer Surplus + Producer Surplus
```

Một trade tạo gains from trade khi willingness to pay của buyer lớn hơn opportunity cost của seller. Vì vậy social surplus của một đơn vị có thể viết trực giác là:

```text
Social value of unit = WTP − Marginal Cost
```

Nếu `WTP > MC`, xã hội theo mô hình được lợi khi đơn vị đó được sản xuất. Nếu `WTP < MC`, nguồn lực dùng để sản xuất đơn vị đó có giá trị opportunity cost lớn hơn giá trị consumer gán cho output.

Điểm quantity hiệu quả xuất hiện nơi marginal benefit bằng marginal cost. Trong competitive equilibrium đơn giản, đây cũng là nơi demand và supply cắt nhau.

## 3. Vì sao competitive equilibrium có thể hiệu quả

Kết luận “competitive market maximizes surplus” không phải định luật vô điều kiện. Nó dựa vào một tập assumptions mạnh: nhiều buyer và seller, price taking, property rights rõ, không có externality, thông tin phù hợp, hàng hóa có thể giao dịch, không có transaction cost quan trọng và preferences/technology đủ regular để equilibrium tồn tại.

Khi assumptions này giữ, giá đóng vai trò signal. Buyer có WTP cao hơn giá mua hàng; seller có marginal cost thấp hơn giá sản xuất. Giao dịch tiếp tục cho đến khi đơn vị tiếp theo không còn tạo positive gains from trade.

Nếu một assumption bị phá vỡ, equilibrium vẫn có thể tồn tại nhưng không còn đảm bảo social efficiency. Đây là cầu nối trực tiếp sang externality, public goods, asymmetric information và market power.

## 4. First Welfare Theorem và giới hạn của nó

First Welfare Theorem nói rằng, dưới assumptions chuẩn của competitive general equilibrium, một competitive equilibrium là Pareto efficient: không thể làm một người khá hơn mà không làm ít nhất một người khác tệ đi.

Pareto efficiency là tiêu chuẩn rất yếu về equity. Một allocation nơi một người sở hữu gần như mọi tài nguyên vẫn có thể Pareto efficient nếu mọi redistribution làm người đó mất utility.

Vì vậy theorem không nói rằng market outcome là “công bằng”, “mong muốn về mặt xã hội” hay “tối ưu tuyệt đối”. Nó chỉ nối competitive equilibrium với một khái niệm efficiency rất cụ thể dưới assumptions rõ ràng.

## 5. Second Welfare Theorem và separation giữa efficiency với distribution

Second Welfare Theorem cho trực giác rằng, dưới thêm các điều kiện convexity, nhiều Pareto-efficient allocations có thể được decentralize bằng competitive prices nếu xã hội điều chỉnh initial endowments phù hợp.

Ý tưởng này tạo separation logic:

```text
Redistribute endowments first
→ then let prices coordinate decentralized choices
```

Trong thực tế, lump-sum transfer hoàn hảo hiếm khi tồn tại. Chính phủ thường không biết đầy đủ ability, preferences hoặc hidden income; tax và transfer làm thay đổi incentive. Vì vậy separation giữa efficiency và redistribution thường chỉ là benchmark để tư duy, không phải policy recipe trực tiếp.

## 6. Price control và deadweight loss

Nếu price ceiling được đặt dưới equilibrium price và có hiệu lực, quantity demanded tăng nhưng quantity supplied giảm. Giao dịch thực tế bị giới hạn bởi phía ngắn hơn của market, thường tạo shortage.

Một số trades có `WTP > MC` không xảy ra nữa. Phần gains from trade bị mất gọi là deadweight loss (DWL).

Price floor phía trên equilibrium có logic đối xứng: quantity supplied vượt quantity demanded, và một phần trades hiệu quả không xảy ra.

Tuy nhiên phân tích welfare không dừng ở tam giác DWL. Cần hỏi thêm: ai được rationed, allocation mechanism là xếp hàng hay quan hệ, quality có đổi không, black market có xuất hiện không, và mục tiêu policy là affordability, income support hay stabilization.

## 7. Tax incidence không phụ thuộc đơn giản vào người “nộp thuế”

Giả sử có per-unit tax `t`. Tax tạo wedge giữa giá buyer trả và giá seller nhận:

```text
P_buyer − P_seller = t
```

Legal incidence là ai chuyển tiền cho nhà nước. Economic incidence là ai thực sự chịu giảm welfare sau khi giá và quantity điều chỉnh.

Phía market ít elastic hơn thường chịu phần burden lớn hơn vì khó thay đổi behavior. Nếu demand rất inelastic còn supply elastic, buyer thường chịu phần lớn tax qua giá cao hơn. Nếu supply inelastic còn demand elastic, seller chịu phần lớn qua net price thấp hơn.

Đây là ví dụ quan trọng cho reasoning: policy effect đi qua behavioral response, không đi thẳng từ luật sang outcome.

## 8. Tax revenue, DWL và elasticity

Government revenue là:

```text
Tax Revenue = t × Q_after_tax
```

Deadweight loss đến từ trades biến mất vì tax wedge. Với cùng tax rate, DWL thường lớn hơn khi demand hoặc supply co giãn hơn vì quantity phản ứng mạnh hơn.

Một approximation quen thuộc với linear curves là DWL tăng gần theo bình phương tax rate. Vì vậy doubling tax rate có thể làm DWL tăng hơn gấp đôi, dù exact result phụ thuộc shape của curves.

Nhưng DWL không tự động đồng nghĩa policy “xấu”. Nếu tax sửa externality, finance public good hoặc tạo insurance/social value, phải so social benefit với distortion thay vì chỉ nhìn triangle trong partial equilibrium.

## 9. Partial equilibrium và general equilibrium

Phân tích một market riêng biệt là partial equilibrium. Nó hữu ích khi spillover sang market khác nhỏ hoặc có thể tạm giữ cố định.

General equilibrium theo dõi nhiều market tương tác đồng thời. Ví dụ tax lao động có thể đổi labor supply, wage, consumption, saving và firm investment. Một subsidy housing có thể ảnh hưởng land price và construction chứ không chỉ renter expenditure.

Vì vậy kết luận từ một demand–supply diagram cần ghi rõ phạm vi: short run hay long run, một market hay nhiều market, factor mobility có hay không.

## 10. Kaldor–Hicks và cost–benefit reasoning

Pareto criterion quá chặt cho policy thực tế vì hầu hết thay đổi tạo winner và loser. Kaldor–Hicks efficiency hỏi liệu tổng gains có đủ lớn để về nguyên tắc winners có thể compensate losers hay không.

Đây là nền của nhiều cost–benefit analysis, nhưng “có thể compensate” khác “thực sự compensate”. Nếu distribution quan trọng, không thể chỉ cộng dollar gains và losses mà bỏ qua marginal value của income, rights hoặc political constraints.

## 11. Equity không thể rút ra từ efficiency theorem

Positive economics có thể phân tích ai chịu tax, quantity đổi bao nhiêu, real income của nhóm nào giảm. Normative economics cần value judgment về công bằng, quyền, capability, redistribution hoặc social welfare.

Một social welfare function đôi khi được viết:

```text
W = W(U1, U2, ..., Un)
```

Nhưng form của `W` không phải kết luận khoa học thuần túy. Nó encode cách xã hội đánh đổi welfare giữa người với người.

Vì vậy chapter welfare phải giữ hai tầng riêng biệt:

- model mô tả consequence;
- ethical/social criterion đánh giá consequence.

## 12. Failure modes thường gặp

Sai lầm đầu tiên là coi consumer surplus như utility tuyệt đối. Surplus đo bằng tiền và phụ thuộc assumptions về demand, income effect và comparability.

Sai lầm thứ hai là coi competitive equilibrium luôn efficient. Chỉ cần externality, market power, asymmetric information, public good hoặc missing market xuất hiện thì result có thể đổi.

Sai lầm thứ ba là dùng total surplus để xóa distribution. Hai policies có cùng total surplus có thể phân phối rất khác nhau.

Sai lầm thứ tư là kết luận từ statutory incidence sang economic incidence mà không xét elasticity.

## 13. Mental model để đọc welfare question

Khi gặp một policy hoặc market outcome, hãy lần lượt hỏi:

1. Marginal benefit và marginal cost nằm ở đâu?
2. Private và social benefit/cost có trùng nhau không?
3. Price hoặc policy tạo wedge nào giữa buyer và seller?
4. Quantity thay đổi bao nhiêu và trades nào biến mất hoặc xuất hiện?
5. Surplus được chuyển giữa nhóm nào, phần nào là transfer và phần nào là real resource loss?
6. Kết luận đang nói efficiency hay equity?
7. Short-run và long-run elasticity có khác nhau không?
8. Có general-equilibrium effect hoặc behavioral adaptation nào bị bỏ qua không?

Welfare economics là cầu nối từ “market hoạt động thế nào” sang “market outcome có đặc tính gì”. Chapter tiếp theo dùng cùng logic nhưng thêm một điểm quan trọng: khi private action tạo cost hoặc benefit cho người ngoài giao dịch, market price không còn chứa đầy đủ social signal. Đó là **externality (외부효과)**.
