# 04 — Lạm phát và sức mua (Inflation / 인플레이션)

## Định vị

[03 — Interest](./03-interest.md) cho thấy tiền có giá trị theo thời gian. Nhưng một lãi suất 4% chỉ có ý nghĩa khi biết giá hàng hóa và dịch vụ thay đổi thế nào. Chapter này giải thích lạm phát (inflation / 인플레이션) ở góc nhìn cá nhân: sức mua, thu nhập danh nghĩa/thực, “lạm phát của riêng mình” và cách tránh những so sánh sai giữa các năm.

Cơ chế hình thành lạm phát, kỳ vọng, chính sách tiền tệ và các mô hình vĩ mô thuộc [Economics — Macroeconomics](../economics/03_macroeconomics/README.md). Ở đây tập trung vào việc biến các con số đó thành quyết định tài chính hộ gia đình.

## Lạm phát không có nghĩa mọi giá đều tăng như nhau

Lạm phát (inflation / 인플레이션) là sự tăng của mức giá chung theo thời gian, không phải khẳng định rằng từng món hàng đều tăng cùng tỷ lệ. Một chỉ số giá tiêu dùng (consumer price index / 소비자물가지수) theo dõi một rổ hàng hóa và dịch vụ đại diện theo phương pháp cụ thể. Giá nhà, học phí, thực phẩm, năng lượng hay thiết bị điện tử có thể đi theo quỹ đạo rất khác.

Vì vậy, nếu CPI tăng 3%, không thể kết luận mọi hộ gia đình đều có chi phí sinh hoạt tăng đúng 3%. Một hộ chi phần lớn cho thuê nhà và năng lượng có thể trải nghiệm mức tăng khác hộ đã sở hữu nhà không vay và chi nhiều cho sản phẩm đang giảm giá.

## Sức mua và giá trị thực

Sức mua (purchasing power / 구매력) cho biết một đơn vị tiền mua được bao nhiêu hàng hóa và dịch vụ. Khi mức giá tăng, cùng số tiền danh nghĩa thường mua được ít hơn.

Nếu mức giá tăng với tỷ lệ `π`, sức mua tương đối của một số tiền cố định sau một kỳ giảm xấp xỉ theo:

```text
Purchasing power factor = 1 / (1 + π)
```

Ví dụ lạm phát 5% không có nghĩa sức mua giảm chính xác 5%; hệ số là `1 / 1.05 ≈ 0.9524`, tức giảm khoảng 4.76% so với trước.

Điều này nối trực tiếp với lãi suất thực (real interest rate / 실질금리): tiền gửi tăng danh nghĩa nhưng nếu giá cả tăng nhanh hơn, giá trị thực vẫn có thể giảm.

## Thu nhập danh nghĩa và thu nhập thực

Thu nhập danh nghĩa (nominal income / 명목소득) là số tiền nhận được theo đơn vị tiền hiện tại. Thu nhập thực (real income / 실질소득) điều chỉnh cho biến động mức giá.

Nếu lương tăng 4% nhưng mức giá liên quan đến đời sống tăng 6%, người lao động có thể “được tăng lương” trên bảng lương nhưng khả năng tiêu dùng thực giảm. Vì thế khi so sánh mức sống giữa các năm, hãy hỏi:

```text
Thu nhập tăng bao nhiêu?
→ giá của giỏ chi tiêu thực tế tăng bao nhiêu?
→ thuế và nghĩa vụ cố định thay đổi ra sao?
→ phần dư sau chi phí thiết yếu tăng hay giảm?
```

Câu cuối thường quan trọng hơn headline CPI trong quản lý dòng tiền cá nhân.

## Lạm phát cá nhân

Có thể ước lượng lạm phát cá nhân (personal inflation rate / 개인 체감물가상승률) bằng cách theo dõi chi phí của chính giỏ chi tiêu tương đối ổn định theo thời gian. Không cần tạo chỉ số kinh tế hoàn hảo; mục tiêu là phát hiện nhóm chi phí nào đang ăn vào phần dư.

Một cách thô:

```text
Personal inflation ≈ Σ(weight_i × price_change_i)
```

Trong đó `weight_i` là tỷ trọng nhóm chi tiêu trong ngân sách. Nếu tiền thuê chiếm 35% ngân sách và tăng 10%, tác động lên hộ có thể lớn hơn nhiều so với một nhóm hàng chỉ chiếm 2% dù nhóm đó tăng 20%.

Đừng biến công thức thành ảo tưởng chính xác. Thay đổi chất lượng, thay thế sản phẩm và thay đổi hành vi tiêu dùng làm phép đo khó hơn; mục tiêu là quản trị, không phải tái tạo CPI quốc gia.

## Lạm phát tác động khác nhau lên tiền mặt và nợ

Tiền mặt không sinh lãi thường mất sức mua khi lạm phát dương. Tuy nhiên điều đó không làm tiền mặt vô dụng: thanh khoản (liquidity / 유동성) vẫn có giá trị cho hóa đơn và cú sốc. Giữ quỹ dự phòng không phải “đầu tư kém”; nó mua khả năng không phải bán tài sản hoặc vay khẩn cấp.

Với nợ lãi suất cố định (fixed-rate debt / 고정금리부채), lạm phát cao hơn kỳ vọng có thể làm giá trị thực của các khoản trả cố định giảm nếu thu nhập cũng tăng. Nhưng điều này không tự động có lợi cho người vay: chi phí sinh hoạt có thể tăng nhanh hơn thu nhập, làm khả năng trả nợ thực tế xấu đi.

Với nợ lãi suất biến đổi (variable-rate debt / 변동금리부채), phản ứng của chính sách tiền tệ và lãi thị trường có thể làm khoản trả tăng, nên lạm phát cao có thể đồng thời tăng chi phí sinh hoạt và chi phí vay.

## Không dùng lạm phát để hợp thức hóa mọi đầu tư

Một lỗi phổ biến là: “tiền mất giá nên phải đầu tư ngay”. Đúng là lạm phát tạo chi phí cơ hội cho tiền nhàn rỗi dài hạn, nhưng từ đó không suy ra rằng bất kỳ tài sản rủi ro nào cũng phù hợp. Thời hạn, quỹ dự phòng, nợ, khả năng chịu drawdown và mục tiêu vẫn phải được xử lý trước.

`personal-finance/` xác định phần vốn có thể chịu rủi ro; [Investing](../investing/README.md) mới là owner của asset allocation, định giá và quản trị danh mục.

## Dự báo lạm phát và quyết định cá nhân

Không cần dự báo chính xác CPI để quản lý tài chính tốt. Thay vào đó nên làm stress test:

```text
Nếu chi phí thiết yếu tăng 10% thì dòng tiền còn dương không?
Nếu tiền thuê tái ký tăng mạnh thì quỹ dự phòng đủ bao lâu?
Nếu lãi khoản vay biến đổi tăng 2–3 điểm phần trăm thì khoản trả mới là bao nhiêu?
Nếu tăng lương thấp hơn giá cả trong hai năm thì phải điều chỉnh phần nào?
```

Stress test biến một biến số vĩ mô khó dự báo thành các điều kiện mà hộ gia đình có thể chuẩn bị.

## Kết luận và hướng đọc tiếp

Lạm phát (inflation / 인플레이션) làm phân biệt giữa **con số tiền** và **sức mua của tiền**. CPI là thước đo mức giá chung, còn ngân sách của một cá nhân có cấu trúc riêng. Khi đã hiểu lãi suất và lạm phát, ta có nền để đọc đúng “giá của tín dụng”. [05 — Credit](./05-credit.md) sẽ giải thích vì sao khả năng vay không đồng nghĩa khả năng chi trả, và vì sao credit report/score chỉ là một lớp trong quyết định nợ.
