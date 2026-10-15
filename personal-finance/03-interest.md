# 03 — Lãi suất và giá trị theo thời gian của tiền (Interest / 이자)

## Định vị

Sau [02 — Banking](./02-banking.md), tiền đã có nơi để giữ và di chuyển. Câu hỏi tiếp theo là: tại sao gửi tiền có thể nhận lãi, còn vay tiền phải trả lãi? Lãi suất (interest rate / 이자율) là giá của việc chuyển sức mua giữa hiện tại và tương lai, đồng thời phản ánh thời gian, rủi ro tín dụng, lạm phát kỳ vọng, thanh khoản và điều kiện thị trường.

Đây là chapter nền bắt buộc trước [05 — Credit](./05-credit.md), [06 — Loans & Debt](./06-loans-debt.md), [09 — Housing](./09-housing.md) và [11 — Retirement](./11-retirement.md).

## Giá trị thời gian của tiền

Một khoản tiền hôm nay thường có giá trị kinh tế cao hơn cùng một số tiền nhận trong tương lai vì tiền hôm nay có thể được dùng ngay, giữ làm thanh khoản hoặc sinh lợi. Khái niệm đó gọi là giá trị thời gian của tiền (time value of money / 화폐의 시간가치).

Nếu số tiền ban đầu là `P`, lãi suất mỗi kỳ là `r`, sau `n` kỳ với lãi kép (compound interest / 복리), giá trị tương lai là:

```text
FV = P × (1 + r)^n
```

Ngược lại, giá trị hiện tại (present value / 현재가치) của một khoản tiền tương lai là:

```text
PV = FV / (1 + r)^n
```

Hai công thức không chỉ dùng cho đầu tư. Chúng giải thích vì sao một khoản nợ dài hạn có tổng tiền trả lớn hơn giá mua ban đầu, vì sao tiết kiệm sớm cho nghỉ hưu có lợi thế thời gian, và vì sao cần so sánh các đề nghị thanh toán ở cùng một mốc thời gian.

## Lãi đơn và lãi kép

Với lãi đơn (simple interest / 단리), lãi chỉ tính trên tiền gốc:

```text
Interest = P × r × n
```

Với lãi kép (compound interest / 복리), lãi của kỳ trước trở thành một phần cơ sở tính lãi kỳ sau. Sự khác biệt ban đầu nhỏ nhưng tăng mạnh khi thời gian dài hoặc lãi suất cao.

Ví dụ, 10 triệu với 5%/năm trong 10 năm nếu ghép lãi hàng năm sẽ thành khoảng:

```text
10,000,000 × 1.05^10 ≈ 16,288,946
```

Điểm quan trọng không phải con số cụ thể mà là tính phi tuyến theo thời gian: thêm vài năm có thể tạo tác động lớn hơn trực giác tuyến tính.

## APR, APY và lãi suất hiệu dụng

Tỷ lệ phần trăm năm (APR, annual percentage rate / 연이율) và lợi suất phần trăm năm (APY, annual percentage yield / 연간수익률) thường không thể hoán đổi trực tiếp. Cách định nghĩa pháp lý cụ thể phụ thuộc jurisdiction và loại sản phẩm, nhưng về mặt toán học cần phân biệt **lãi suất được công bố** với **lãi suất hiệu dụng (effective annual rate / 실효연이율)** sau tần suất ghép lãi và phí.

Nếu một lãi suất danh nghĩa `r_nominal` được ghép `m` lần mỗi năm, một dạng tính lãi suất hiệu dụng là:

```text
EAR = (1 + r_nominal / m)^m − 1
```

Khi so sánh khoản vay hoặc tiền gửi, không nên chỉ nhìn con số lớn in trên quảng cáo. Cần xác định:

```text
lãi tính trên dư nợ nào?
→ ghép lãi bao lâu một lần?
→ phí bắt buộc nào đi kèm?
→ có lãi suất ưu đãi tạm thời không?
→ lãi cố định hay biến đổi?
```

## Lãi cố định và lãi biến đổi

Lãi suất cố định (fixed rate / 고정금리) giữ một mức theo điều kiện hợp đồng trong giai đoạn xác định. Lãi suất biến đổi (variable rate / 변동금리) thay đổi theo chỉ số tham chiếu hoặc quy tắc của hợp đồng.

Khoản vay lãi biến đổi có thể rẻ hơn lúc đầu nhưng chuyển một phần rủi ro lãi suất (interest-rate risk / 금리위험) sang người vay. Nếu thu nhập gần như cố định nhưng khoản trả nợ có thể tăng mạnh, rủi ro dòng tiền lớn hơn chỉ nhìn vào lãi suất hiện tại.

Ngược lại, lãi cố định tạo tính dự đoán nhưng có thể phản ánh kỳ vọng thị trường và premium cho việc khóa mức lãi. Không có loại nào luôn tốt hơn độc lập với thời hạn, biên độ thay đổi và khả năng chịu cú sốc của người vay.

## Lãi danh nghĩa và lãi thực

Lãi suất danh nghĩa (nominal interest rate / 명목금리) chưa điều chỉnh cho lạm phát. Lãi suất thực (real interest rate / 실질금리) đo thay đổi sức mua. Gần đúng khi tỷ lệ không quá lớn:

```text
real rate ≈ nominal rate − inflation rate
```

Chính xác hơn theo quan hệ Fisher:

```text
1 + real = (1 + nominal) / (1 + inflation)
```

Nếu tiền gửi trả 4% nhưng giá cả tăng 5%, số dư danh nghĩa tăng trong khi sức mua có thể giảm. [04 — Inflation](./04-inflation.md) sẽ mở rộng phần này.

## Lãi suất trên nợ: đừng nhìn tổng số tiền vay

Hai khoản vay cùng tiền gốc nhưng khác thời hạn có thể tạo nghĩa vụ rất khác. Kéo dài kỳ hạn thường giảm khoản trả hàng tháng nhưng tăng tổng lãi nếu các điều kiện khác giống nhau.

Ví dụ, khi mua xe hoặc nhà, câu hỏi “mỗi tháng trả bao nhiêu?” chưa đủ. Cần xem ít nhất:

```text
principal
interest rate / effective cost
term
fees
prepayment rules
variable-rate conditions
```

Một khoản trả tháng thấp có thể chỉ là kết quả của việc trải nợ lâu hơn.

## Lãi kép có hai mặt

Lãi kép (compound interest / 복리) thường được quảng bá như sức mạnh tích lũy tài sản. Nhưng cơ chế toán học là trung tính. Với khoản nợ quay vòng lãi cao, cùng hiệu ứng đó khiến nghĩa vụ tăng nhanh nếu lãi chưa trả tiếp tục được tính vào số dư.

Do đó “thời gian” có lợi cho người sở hữu tài sản sinh lợi nhưng có thể chống lại người mang nợ có chi phí cao. Đây là cầu nối sang [05 — Credit](./05-credit.md) và [06 — Loans & Debt](./06-loans-debt.md).

## Kết luận và hướng đọc tiếp

Mô hình cần giữ lại là:

```text
Lãi suất = giá của thời gian + rủi ro + điều kiện thị trường/hợp đồng
Lãi kép = tăng trưởng trên cả gốc lẫn phần đã tích lũy
Khoản trả thấp ≠ khoản vay rẻ
Lãi danh nghĩa ≠ tăng sức mua thực
```

Trước khi đi vào tín dụng, cần hiểu yếu tố làm lãi danh nghĩa khác lãi thực: [04 — Inflation](./04-inflation.md) giải thích sức mua, lạm phát cá nhân và vì sao cùng một mức lạm phát chung có thể tác động rất khác lên các hộ gia đình.

### Nguồn tham khảo

- Investor.gov Compound Interest Calculator: https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator
