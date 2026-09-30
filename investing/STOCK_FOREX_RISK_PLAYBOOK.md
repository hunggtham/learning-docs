# Sổ tay quản trị rủi ro — Cổ phiếu và Forex

> Đây là khung học tập và kiểm tra trước quyết định, không phải mức phân bổ cá nhân. Mọi tỷ lệ minh họa cần được thay bằng mục tiêu, nghĩa vụ và khả năng chịu lỗ thực tế của bạn.

Đây là lớp thực hành dễ dùng. Với danh mục nhiều tài sản, dùng [Portfolio Design Stress Lab](./01_foundations/06_ADVANCED_PORTFOLIO_DESIGN_STRESS_AND_DECISION_LAB.md); với hệ thống Forex/phái sinh, dùng [Trading System Design Lab](./05_trading_derivatives/06_TRADING_SYSTEM_DESIGN_RISK_AND_EXECUTION_LAB.md) làm nguồn chuyên sâu.

## 1. Chia tiền theo khả năng chịu mất

Phần đầu đặt rủi ro vào bối cảnh đời sống trước khi đặt lệnh. Câu hỏi không phải “tài sản này có thể lời bao nhiêu?” mà là “nếu mất một phần hoặc toàn bộ, mục tiêu nào bị ảnh hưởng và thời gian phục hồi còn bao nhiêu?”.

Trước khi chọn tài sản, chia nguồn tiền theo thời điểm cần dùng:

| Nhóm tiền | Câu hỏi | Cách tiếp cận học tập |
|---|---|---|
| **Tiền phải bảo toàn** | Nếu mất tiền này, đời sống bị ảnh hưởng không? | Không dùng để thử Forex đòn bẩy hoặc tài sản biến động cao |
| **Vốn đầu tư** | Có thể chịu biến động nhiều năm không? | Tập trung vào danh mục, cổ phiếu/ETF, thanh khoản và tái cân bằng |
| **Vốn thử nghiệm** | Mất toàn bộ có làm hỏng mục tiêu lớn không? | Chỉ dùng paper trade hoặc quy mô nhỏ; ghi rõ giới hạn lỗ |

Không gọi một khoản tiền là “vốn rảnh” chỉ vì chưa dùng trong tháng này. Hãy xét nghĩa vụ, thời điểm cần tiền và khả năng thu nhập bị gián đoạn.

Sau khi tách các nhóm tiền, ta mới có thể đặt risk budget cho một vị thế cụ thể mà không nhầm tiền có mục đích gần với vốn thử nghiệm.

## 2. Ba con số phải biết trước khi mở vị thế

Ba con số này tạo cầu nối từ khả năng chịu mất sang kịch bản lỗ. Hãy ghi chúng trước khi nhìn mục tiêu lợi nhuận, vì risk được quyết định bởi đường đi xấu chứ không chỉ bởi giá vào.

```text
1. Lỗ dự kiến trong kịch bản bình thường
2. Lỗ stress khi gap, spread rộng, thanh khoản giảm hoặc thesis sai nhanh
3. Tỷ lệ lỗ đó so với tổng vốn và risk budget
```

Nếu chỉ biết giá vào và mục tiêu lợi nhuận, hồ sơ rủi ro chưa hoàn chỉnh.

Từ đây, cổ phiếu và Forex cần hai cách tính stress khác nhau: một bên dựa trên mức giảm và thanh khoản, một bên dựa trên stop, pip, funding và gap.

## 3. Cổ phiếu: sizing theo stress loss

Với cổ phiếu, stop không bảo đảm fill và gap có thể xảy ra khi thị trường đóng cửa. Vì vậy, ta bắt đầu bằng stress loss của cả vị thế rồi mới xem mức giảm kỹ thuật có phù hợp hay không.

Với cổ phiếu không có stop bảo đảm, đừng chỉ dùng khoảng cách tới một mức giá kỹ thuật. Hãy ước lượng:

```text
Stress loss ≈ Tỷ trọng vị thế × Mức giảm stress
```

Ví dụ minh họa:

```text
Vị thế 8% danh mục
Mức giảm stress -40%
Đóng góp lỗ ≈ 8% × -40% = -3,2% danh mục
```

Sau đó kiểm tra:

- mã có thể giảm nhanh hơn khi tin xấu hoặc thị trường đóng cửa không;
- free float và thanh khoản có đủ để thoát vị thế không;
- vị thế có trùng ngành, beta, FX hoặc factor với các khoản khác không;
- luận điểm có còn đúng nếu giá giảm nhưng dữ kiện vận hành chưa đổi không.

Một công ty chất lượng cao vẫn có thể là vị thế quá lớn.

Kết luận là chất lượng doanh nghiệp không thay thế kỷ luật sizing. Forex tiếp theo dùng công thức chi tiết hơn vì lỗ chịu ảnh hưởng trực tiếp của pip, spread, slippage và financing.

## 4. Forex: sizing theo lỗ all-in

Forex cần tính lỗ all-in thay vì chỉ lấy khoảng stop. Mục tiêu của phần này là đưa mọi chi phí có thể xuất hiện trước khi đóng vị thế vào cùng một risk budget.

```text
Mức lỗ cho phép = Equity × % rủi ro dự kiến
Lỗ tại stop = Khoảng stop × Giá trị pip × Quy mô
Lỗ all-in ≈ Lỗ tại stop + spread + slippage + financing
```

Trước sự kiện lớn, thêm một lớp stress:

```text
Stress loss = Lỗ khi giá đi xa hơn stop + slippage/gap + margin impact
```

Nếu stress loss làm tài khoản gần margin call, quy mô đã quá lớn dù stop thông thường có vẻ nhỏ.

Khi quy mô đã được tính, cần tách rõ margin đang trả lời câu hỏi nào và vì sao nó không phải risk budget.

## 5. Margin không phải risk budget

Bảng dưới đây đặt các khái niệm cạnh nhau để loại bỏ nhầm lẫn phổ biến. Đọc từng dòng như một câu hỏi riêng: giá trị danh nghĩa, collateral, điểm thoát, kịch bản xấu và ngân sách tổng không phải cùng một đại lượng.

| Khái niệm | Nó trả lời câu hỏi nào? |
|---|---|
| Notional | Tôi đang kiểm soát giá trị danh nghĩa bao nhiêu? |
| Margin | Broker yêu cầu khóa bao nhiêu tài sản bảo đảm? |
| Stop loss | Tôi dự định thoát ở đâu nếu luận điểm sai? |
| Maximum loss | Kịch bản xấu nhất có thể mất bao nhiêu? |
| Risk budget | Tôi cho phép vị thế này tiêu tốn bao nhiêu rủi ro của toàn bộ danh mục? |

Ví dụ: notional 11.000 USD, margin 220 USD và stop 30 USD. Không con số nào trong ba số tự động là “mức rủi ro đúng”; phải xem gap, spread, financing và khả năng stop-out.

Sau khi tách được các đại lượng, ta có thể nhìn drawdown như một phép toán phục hồi vốn chứ không chỉ là một cảm giác khó chịu.

## 6. Drawdown và thời gian hồi phục

Mức giảm càng lớn thì tỷ lệ tăng cần thiết để hòa vốn càng không đối xứng. Bảng này giúp người mới nhìn thấy chi phí cơ hội của một drawdown trước khi chọn leverage hoặc size.

| Mức giảm | Mức tăng cần để hòa vốn |
|---:|---:|
| -10% | +11,1% |
| -20% | +25% |
| -30% | +42,9% |
| -50% | +100% |
| -70% | +233,3% |

Drawdown không chỉ là cảm giác khó chịu. Nó làm giảm vốn để phục hồi, tăng áp lực tâm lý và có thể khiến bạn thay rule ở thời điểm tệ nhất.

Vì vậy, stress test cần bao gồm nhiều trạng thái và câu hỏi hành động, không chỉ một mức giảm trung bình.

## 7. Ma trận stress tối thiểu

Ma trận này chuyển các rủi ro riêng lẻ thành tình huống có thể diễn tập. Hãy đọc theo hàng để thấy thị trường thay đổi ra sao, rồi đọc theo cột để kiểm tra cổ phiếu và Forex cùng phơi nhiễm factor nào.

| Trạng thái | Cổ phiếu | Forex | Câu hỏi cần trả lời |
|---|---|---|---|
| Bình thường | Spread/liquidity bình thường | Pip value và stop hoạt động như dự kiến | Kỳ vọng sau chi phí là gì? |
| Biến động cao | Gap hoặc limit/khó thoát | Spread rộng, slippage tăng | Lỗ all-in là bao nhiêu? |
| Cú sốc vĩ mô | Multiple co, earnings revision | Tỷ giá và rates cùng đảo chiều | Exposure nào bị trùng? |
| Mất thanh khoản | Bán được ít hoặc phải giảm giá | Stop không khớp đúng | Có đủ buffer để không bị cưỡng bức không? |
| Thesis sai | KPI, FCF hoặc bảng cân đối xấu | Relative rates/flow không còn đúng | Điều kiện dừng cụ thể là gì? |

Sau khi chạy qua ma trận, hãy viết sẵn quy tắc dừng học tập và thực thi. Quy tắc đó bảo vệ bạn khỏi việc mở vị thế mới để che giấu một lỗi chưa được hiểu.

## 8. Quy tắc dừng học tập và thực thi

Các điều kiện dưới đây là cổng an toàn trước khi thêm rủi ro. Một mục thất bại không có nghĩa phải bỏ học; nó có nghĩa cần quay lại sửa dữ liệu, sizing hoặc giả thuyết trước khi tiếp tục.

Tạm dừng mở vị thế mới nếu:

- không tính được lỗ bằng tiền trước khi vào;
- dữ liệu đầu vào đã cũ nhưng chưa ghi ngày tham chiếu;
- spread/slippage thực tế vượt giả định;
- tổng exposure USD, KRW/VND, beta hoặc carry vượt risk budget;
- đang tăng quy mô để gỡ lỗ;
- không phân biệt được thesis sai với giá chỉ nhiễu;
- hệ thống, broker, dữ liệu hoặc đối soát có lỗi.

Paper trade cũng cần quy tắc dừng. Nếu không, bạn đang luyện thói quen xấu trong môi trường không có hậu quả.

Sau mỗi quyết định, ghi lại điều gì thực sự tạo P/L và điều gì chỉ là may mắn. Đó là mục đích của review.

## 9. Review sau mỗi quyết định

Review nối kết quả với quy trình trước lệnh. Hãy trả lời các câu hỏi dưới đây bằng dữ kiện, không bằng câu chuyện được viết lại sau khi đã biết P/L.

```text
Lỗ/lãi đến từ thesis, beta, multiple, FX, carry hay may mắn?
Mức rủi ro thực tế có đúng như hồ sơ trước lệnh không?
Chi phí và slippage có bị đánh giá thấp không?
Kịch bản stress nào đã không được tính?
Quy mô đúng nhưng execution sai, hay thesis sai ngay từ đầu?
Quy tắc nào cần giữ nguyên, sửa hoặc loại bỏ?
```

Mục tiêu của review là cải thiện quy trình, không phải viết lại lịch sử để quyết định cũ trông hợp lý hơn.

Cuối cùng, dùng cổng an toàn để quyết định có đủ điều kiện dùng đòn bẩy hay vẫn nên paper trade.

## 10. Cổng an toàn trước khi dùng đòn bẩy

Checklist này là kết luận thực hành của sổ tay. Mỗi ô xác nhận một lớp hiểu biết: tiền, hợp đồng, chi phí, execution, dữ liệu và điều kiện vô hiệu hóa.

- [ ] Tiền này không cần cho nghĩa vụ gần.
- [ ] Đã biết notional, margin, stop-out và maximum loss.
- [ ] Đã mô phỏng spread, slippage, financing và gap.
- [ ] Đã có giới hạn lỗ ngày/tuần và kill switch.
- [ ] Đã thử paper trade đủ lâu để kiểm tra thực thi.
- [ ] Đã biết dữ kiện nào sẽ làm luận điểm sai.
- [ ] Có buffer thanh khoản sau khi mở vị thế.

Nếu thiếu một ô, lựa chọn hợp lý trong bài tập là chưa dùng đòn bẩy.
