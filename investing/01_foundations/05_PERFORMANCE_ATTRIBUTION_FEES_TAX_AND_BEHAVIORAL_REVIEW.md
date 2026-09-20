# 05 — Performance Attribution, Fees, Tax và Behavioral Review

> Mục tiêu của chapter này là trả lời câu hỏi mà rất nhiều nhà đầu tư bỏ qua: **portfolio tăng hoặc giảm vì lý do gì?** Nếu không tách được performance thành allocation, security selection, currency, fees, tax và behavior, người đầu tư rất dễ học sai bài học từ chính kết quả của mình.

## 1. Lợi nhuận tốt chưa chắc quyết định tốt

Một quyết định đầu tư phải được đánh giá bằng chất lượng của quy trình tại thời điểm ra quyết định, không chỉ bằng outcome sau đó. Mua một cổ phiếu không phân tích gì rồi tình cờ tăng 50% vẫn có thể là một quyết định có quy trình kém. Ngược lại, một quyết định hợp lý dựa trên dữ liệu và risk control vẫn có thể thua lỗ vì tương lai luôn chứa uncertainty.

Điều này dẫn tới một nguyên tắc quan trọng: **process quality** và **outcome quality** là hai biến khác nhau. Portfolio review phải xem cả hai.

## 2. Total Return phải được phân rã

Total return của một tài sản thường đến từ nhiều nguồn. Với cổ phiếu, return có thể đến từ earnings growth, dividend, multiple expansion hoặc currency. Với bond, return có thể đến từ coupon, yield change, roll-down và credit spread change. Với ETF quốc tế, currency có thể đóng góp lớn đến mức return bằng KRW rất khác return bằng USD.

Một framework đơn giản là:

```text
Portfolio Return
= Market/Beta Effect
+ Allocation Effect
+ Security Selection Effect
+ Currency Effect
+ Income
- Fees
- Tax
- Trading Friction
```

Framework này không phải công thức kế toán tuyệt đối cho mọi portfolio, nhưng rất hữu ích để tư duy.

## 3. Benchmark và Active Return

Bạn không thể đánh giá portfolio nếu không biết đang so với cái gì. **Benchmark** phải phản ánh cơ hội đầu tư thực tế và risk profile tương đối phù hợp. Nếu portfolio 80% equity mà so với deposit rate, kết luận sẽ dễ bị méo.

Active return có thể viết đơn giản:

```text
Active Return = Portfolio Return - Benchmark Return
```

Nhưng active return chỉ có ý nghĩa khi benchmark đúng. Một portfolio Korea equity tập trung semiconductor có thể outperform KOSPI nhưng underperform một semiconductor index; hai so sánh trả lời hai câu hỏi khác nhau.

## 4. Allocation Effect và Selection Effect

**Allocation effect** đến từ việc phân bổ nhiều hay ít vào một asset class hoặc sector so với benchmark. **Selection effect** đến từ việc chọn security tốt hay xấu bên trong nhóm đó.

Ví dụ, nếu bank sector tăng mạnh và portfolio overweight bank, phần lợi nhuận đó chủ yếu đến từ allocation. Nếu portfolio giữ đúng trọng số bank như benchmark nhưng chọn được bank tốt hơn phần còn lại, đó gần với selection effect.

Tư duy này giúp tránh kết luận kiểu “tôi giỏi stock picking” trong khi thực ra phần lớn performance đến từ một sector bet.

## 5. Currency Attribution

Với investor có base currency là KRW, lợi nhuận của một tài sản USD nên được tách thành asset return và FX return.

Một approximation đơn giản là:

```text
KRW Return ≈ USD Asset Return + USD/KRW FX Return
```

Công thức chính xác hơn có interaction term:

```text
(1 + Asset Return) × (1 + FX Return) - 1
```

Nếu S&P 500 tăng 10% bằng USD nhưng USD giảm 8% so với KRW, investor Hàn Quốc không nhận trọn +10% bằng KRW.

## 6. Fee Drag và Compounding

Phí nhỏ theo năm có thể trở thành khác biệt lớn trong thời gian dài vì phí cũng bị compound theo chiều ngược lại. Không chỉ expense ratio, investor còn phải tính spread, brokerage commission, FX conversion cost, withholding tax, borrow cost, swap và slippage.

Một ETF có expense ratio thấp hơn chưa chắc rẻ hơn nếu spread rộng, tracking difference xấu hoặc FX conversion cost lớn. **Total implementation cost** mới là thứ cần so sánh.

## 7. Tax Drag và After-Tax Return

Đối với investor thật, return trước thuế không phải return cuối cùng. Tax treatment có thể khác giữa capital gain, dividend, interest, foreign income, pension wrapper và tax-advantaged account.

Do luật thay đổi theo jurisdiction và thời gian, tài liệu này không cố đóng đinh rate cụ thể. Framework cần nhớ là:

```text
Pre-tax Return
→ Realized / Unrealized split
→ Income type
→ Applicable account wrapper
→ Tax / withholding
→ After-tax Return
```

Khi so sánh hai sản phẩm, phải so after-tax và after-fee nếu mục tiêu là quyết định đầu tư thực tế.

## 8. Turnover và Tax Efficiency

Turnover cao thường làm tăng phí, spread, slippage và có thể tăng tax realization. Một strategy outperform trước phí nhưng turnover cực cao có thể underperform sau phí.

Đây là lý do **gross alpha** và **net alpha** phải được tách riêng. Trong thực tế, net alpha mới có giá trị.

## 9. Behavioral Attribution

Một phần performance đến từ hành vi của investor hơn là tài sản. Các lỗi phổ biến gồm bán winner quá sớm, giữ loser quá lâu, tăng risk sau chuỗi thắng, panic sell trong drawdown, mua theo FOMO và thay strategy đúng lúc strategy đang ở phase yếu tạm thời.

Behavioral review nên hỏi: “Quyết định này đến từ rule đã viết trước hay từ cảm xúc sau khi giá chạy?”

Nếu không có rule trước sự kiện, rất khó phân biệt adaptation hợp lý với emotional reaction.

## 10. Decision Journal

Decision journal nên lưu tối thiểu thesis, expected return driver, key risks, valuation assumption, invalidation conditions, horizon và position-size rationale.

Điểm quan trọng không phải viết thật dài mà là ghi lại **information set tại thời điểm quyết định**. Khi review sau sáu tháng, bạn có thể xem thesis sai ở đâu: revenue assumption, margin, macro regime, valuation, FX hay execution.

## 11. Outcome Bias và Hindsight Bias

**Outcome bias** là đánh giá quyết định chỉ dựa vào kết quả. **Hindsight bias** là sau khi sự kiện xảy ra, cảm giác rằng kết quả “rõ ràng từ đầu”. Hai bias này phá hỏng learning loop.

Cách giảm chúng là lưu forecast range và probability trước khi có kết quả. Khi outcome xuất hiện, so với distribution đã dự kiến chứ không viết lại lịch sử.

## 12. Base Rate và Calibration

Một investor nên dần học cách calibration. Nếu bạn đánh giá 20 sự kiện có 70% xác suất mà chỉ đúng khoảng 50%, model hoặc confidence của bạn đang có vấn đề.

Không cần xây hệ thống thống kê phức tạp ngay từ đầu. Chỉ cần bắt đầu dùng ngôn ngữ xác suất thay vì “chắc chắn tăng” hay “không thể giảm”.

## 13. Monthly Review

Monthly review nên tập trung vào portfolio-level questions: allocation có lệch IPS không, concentration có tăng không, FX exposure có thay đổi không, drawdown đến từ market beta hay thesis-specific problem, fees có bất thường không và có position nào vượt risk budget không.

Không cần thay portfolio chỉ vì monthly review. Review là để đo và hiểu, không phải để tạo thêm trading activity.

## 14. Quarterly Thesis Review

Quarterly review phù hợp để xem earnings, balance sheet, sector condition và valuation. Câu hỏi quan trọng là liệu expected return từ hôm nay có còn hấp dẫn hay không, chứ không phải giá mua ban đầu là bao nhiêu.

Purchase price là thông tin lịch sử. Opportunity cost của capital ở hiện tại mới quyết định giữ hay tái phân bổ.

## 15. Annual Portfolio Audit

Annual audit nên xem lại objective, liabilities, emergency fund, income stability, horizon, risk capacity, tax wrapper, benchmark và asset allocation. Cuộc sống thay đổi thì IPS cũng có thể cần cập nhật.

Nhưng IPS không nên thay đổi chỉ vì market vừa tăng hay giảm mạnh. Thay đổi policy vì price action ngắn hạn thường là performance chasing.

## 16. Attribution Template thực hành

Một review có thể viết theo format:

```text
1. Portfolio return: ...
2. Benchmark return: ...
3. Active return: ...
4. Allocation effect: ...
5. Security selection effect: ...
6. Currency effect: ...
7. Income/dividend/interest: ...
8. Fees/tax/friction: ...
9. Largest positive thesis contribution: ...
10. Largest negative thesis contribution: ...
11. Behavioral mistakes: ...
12. Process changes justified by data: ...
```

Điều quan trọng là không biến review thành danh sách cảm xúc. Mỗi kết luận nên gắn với một measurable driver.

## 17. Khi nào nên thay đổi strategy?

Không nên bỏ strategy chỉ vì vài tháng underperformance. Nhưng cũng không nên trung thành mù quáng. Strategy change hợp lý khi economic premise thay đổi, evidence accumulation cho thấy edge không còn, implementation cost cao hơn dự kiến, risk vượt khả năng chịu đựng hoặc objective cá nhân thay đổi.

Điểm mấu chốt là có **predefined review criteria**.

## 18. Kết nối sang các domain khác

Performance attribution sử dụng kiến thức từ Asset Classes để hiểu return driver, Company Analysis để phân biệt thesis-specific alpha, Economics để nhận diện macro beta, Trading để đo execution cost và Korea/Vietnam domain để hiểu currency/tax/market structure theo jurisdiction.

Một investor trưởng thành không chỉ hỏi “portfolio lời bao nhiêu?” mà hỏi: **lời vì đâu, risk nào đã chịu, phần nào có thể lặp lại và phần nào chỉ là may mắn?**
