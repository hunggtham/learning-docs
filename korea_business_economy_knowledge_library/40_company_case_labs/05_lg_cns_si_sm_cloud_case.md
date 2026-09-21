# LG CNS Case Lab — SI/SM, cloud, AX và kinh tế dự án

LG CNS là một trường hợp phù hợp để học cách đọc một công ty CNTT doanh nghiệp trong bối cảnh Hàn Quốc. Mô hình kinh doanh không giống SaaS thuần túy: một phần doanh thu đến từ SI theo dự án, một phần từ SM hoặc dịch vụ quản lý định kỳ, cloud–hạ tầng, nhà máy/logistics thông minh và các dịch vụ số–AI. Vì vậy chất lượng tăng trưởng doanh thu thay đổi rất nhiều tùy cơ cấu mảng kinh doanh.

LG CNS mô tả danh mục gồm Cloud & AI, Smart Engineering và Digital Business Service; trong đó SI & SM truyền thống vẫn là nền tảng quan trọng. Năm tài chính 2025 công ty công bố doanh thu năm vượt 6 nghìn tỷ KRW, nhưng case này không dùng quy mô để kết luận chất lượng. Mục tiêu là hiểu **mức sử dụng nhân lực + rủi ro dự án + doanh thu dịch vụ lặp lại + cơ cấu IP/cloud** cùng tạo ra lợi nhuận như thế nào.

## 1. SI và SM là hai cỗ máy kinh tế khác nhau

**Tích hợp hệ thống (System Integration / SI / 시스템 통합)** thường là dự án xây mới, thay thế hoặc hiện đại hóa hệ thống. Doanh thu có thể được ghi theo mốc nghiệm thu, tiến độ hoặc số nguồn lực tính phí tùy hợp đồng.

**Quản lý và vận hành hệ thống (System Management / SM / 시스템 운영·유지보수)** thường có tính lặp lại cao hơn vì khách hàng vẫn cần vận hành hệ thống sau khi đưa vào sử dụng.

Một mô hình SI theo nhân lực:

\[
Revenue_{SI} \approx Billable\ Resources \times Utilization \times Billing\ Rate
\]

Ngoài ra còn có hợp đồng giá cố định.

Một mô hình SM đơn giản:

\[
Revenue_{SM} \approx Managed\ Scope \times Contract\ Rate \times Contract\ Duration
\]

SI có cơ hội lợi nhuận từ dự án chuyển đổi lớn nhưng rủi ro phạm vi và chi phí cao. SM thường ổn định hơn nhưng tốc độ tăng trưởng và biên lợi nhuận có thể thấp nếu phụ thuộc nhiều vào lao động.

## 2. Kinh tế của nhân lực

Công ty dịch vụ CNTT biến thời gian của lập trình viên, kiến trúc sư và tư vấn thành sản phẩm bàn giao cho khách hàng. Vì vậy số lượng nhân sự không chỉ là chi phí quản lý; nó còn là **công suất sản xuất (productive capacity)**.

Một mô hình nguồn lực:

```text
giờ kỹ sư có thể cung cấp
× tỷ lệ giờ có thể tính phí
× đơn giá tính phí
= công suất doanh thu dịch vụ
```

Nếu tỷ lệ sử dụng thấp, lương vẫn phải trả. Nếu tỷ lệ sử dụng quá cao kéo dài, rủi ro làm thêm giờ, chất lượng và nghỉ việc tăng.

Vì vậy tỷ lệ sử dụng tối ưu không phải 100%.

## 3. Đơn giá tính phí và chi phí lao động

Giả sử một kỹ sư có **tổng chi phí sử dụng lao động (fully loaded cost)** mỗi năm bằng 80. Công ty có 1.800 giờ có thể tính phí nhưng tỷ lệ sử dụng thực tế chỉ 75%, tức khoảng 1.350 giờ.

Đơn giá hòa vốn trước chi phí chung:

\[
80 / 1,350 \approx 0.0593
\]

Nếu đơn giá tính phí chỉ cao hơn mức hòa vốn rất ít, lạm phát tiền lương có thể ăn hết biên lợi nhuận nhanh chóng.

Đó là lý do tự động hóa hoặc AI chỉ tạo giá trị tài chính khi công ty có thể phục vụ phạm vi công việc lớn hơn với cùng số người, giảm số giờ giao hàng nhưng vẫn giữ giá trị hợp đồng, hoặc chuyển nhân lực sang công việc có giá trị cao hơn.

Nếu hợp đồng là giá cố định, công ty có thể giữ lại phần lớn lợi ích năng suất. Nếu hợp đồng tính theo thời gian và vật tư (time-and-material / T&M), số giờ ít hơn có thể đồng thời làm doanh thu tính phí giảm. **Cấu trúc hợp đồng quyết định kinh tế của năng suất AI.**

## 4. Rủi ro của dự án giá cố định

Giả sử giá trị hợp đồng bằng 100 và tổng chi phí ước tính ban đầu bằng 85. Lợi nhuận dự kiến là 15.

Sau sáu tháng, phạm vi công việc tăng và vấn đề tích hợp làm tổng chi phí dự kiến tăng lên 110.

Kinh tế dự án thay đổi từ +15 thành -10. Nếu ước tính kế toán được cập nhật đúng, khoản lỗ dự kiến phải được phản ánh theo nguyên tắc ghi nhận doanh thu và kế toán áp dụng thay vì chờ tới khi dự án kết thúc.

Chuỗi nguyên nhân:

```text
yêu cầu không rõ
→ làm lại
→ tăng giờ lao động / nhà thầu phụ
→ chậm tiến độ
→ chi phí ước tính ↑
→ biên lợi nhuận dự án ↓ / ghi nhận dự phòng hoặc lỗ
```

Vì vậy **tài sản hợp đồng (contract asset)**, khoản phải thu chưa lập hóa đơn và ước tính chi phí dự án là các trường dữ liệu kế toán rất quan trọng.

## 5. Nhiều tầng thầu phụ

Dự án SI lớn tại Hàn Quốc thường có nhà thầu chính và nhiều đối tác hoặc nhà thầu phụ. Thuê ngoài giúp tăng công suất linh hoạt và tiếp cận kỹ năng chuyên môn, nhưng tạo đánh đổi về phối hợp, chất lượng và biên lợi nhuận.

Nếu nhà thầu chính tính khách hàng 100 và thuê ngoài 70, giá trị kinh tế giữ lại chỉ còn 30 trước chi phí quản lý dự án, kiến trúc và chi phí chung nội bộ.

Doanh thu cao với tỷ lệ thuê ngoài cao có thể tạo giá trị gia tăng thấp hơn một doanh nghiệp có doanh thu nhỏ hơn nhưng đóng góp phần mềm hoặc IP nhiều hơn.

Khi đọc công ty cần hỏi: năng lực kỹ thuật nội bộ mạnh đến đâu, tỷ lệ thầu phụ bao nhiêu, công ty là nhà thầu chính hay vendor cấp dưới, ai sở hữu quyền thiết kế–kiến trúc và ai gánh rủi ro của hợp đồng giá cố định.

## 6. Nhu cầu nội bộ tập đoàn và nhu cầu bên ngoài

Thuộc một tập đoàn lớn có thể tạo nguồn cầu nội bộ ổn định và kiến thức ngành sâu. Tuy nhiên **nhu cầu nội bộ (captive demand)** cũng đặt ra câu hỏi phân tích: giá giao dịch có theo nguyên tắc thị trường hay không, sức cạnh tranh bên ngoài mạnh đến đâu, doanh thu có tập trung vào công ty cùng tập đoàn không và nguồn cầu nội bộ có mang mục tiêu hỗ trợ chiến lược nào hay không.

Nhu cầu nội bộ có thể là lợi thế nếu chi phí chuyển đổi và mức tích hợp nghiệp vụ cao, nhưng cũng có thể che giấu năng lực bán hàng bên ngoài yếu. Cần kiểm tra bằng chứng từ khách hàng ngoài tập đoàn và biên lợi nhuận.

## 7. Cloud: từ doanh thu dự án sang dịch vụ định kỳ

Một dự án chuyển lên cloud có thể tạo nhiều lớp doanh thu:

```text
tư vấn
→ SI chuyển đổi hệ thống
→ hạ tầng / bán lại dịch vụ cloud
→ dịch vụ quản lý
→ bảo mật / tối ưu
→ dữ liệu / khối lượng công việc AI
```

Dự án chuyển đổi ban đầu có thể mang tính một lần, nhưng sau đó tạo luồng doanh thu dịch vụ quản lý kéo dài nhiều năm.

Tuy nhiên doanh thu cloud không tự động có biên cao nếu công ty chủ yếu bán lại năng lực của hyperscaler với phần chênh lệch nhỏ. Cần tách:

```text
chi phí cloud chuyển thẳng qua khách hàng
giá trị gia tăng từ dịch vụ quản lý
nền tảng / phần mềm sở hữu riêng
tư vấn / tích hợp
hạ tầng / trung tâm dữ liệu tự sở hữu
```

Biên lợi nhuận và mức độ cần vốn của từng lớp rất khác nhau.

## 8. Nhà máy thông minh và logistics thông minh

Dự án kỹ thuật thông minh kết hợp phần mềm với thiết bị hoặc quy trình vật lý. Doanh thu có thể lớn nhưng phần thiết bị mua hộ hoặc chuyển tiếp có thể làm doanh thu báo cáo cao hơn giá trị gia tăng thực.

Ví dụ:

```text
Doanh thu dự án = 1.000
Thiết bị / phần cứng chuyển tiếp = 650
Phần mềm / tích hợp / dịch vụ = 350
```

Nếu chỉ nhìn doanh thu, người phân tích có thể đánh giá quá cao tính kinh tế của phần mềm. Lợi nhuận gộp và tỷ trọng dịch vụ/IP quan trọng hơn.

## 9. AX/AI: tăng năng suất hay tạo doanh thu mới?

AI doanh nghiệp có thể tạo giá trị theo ba đường:

```text
AI dùng nội bộ
→ tăng năng suất giao dự án

AI nhúng trong SI/SM
→ tăng giá trị dự án / tự động hóa

nền tảng hoặc sản phẩm AI
→ doanh thu giấy phép / mức sử dụng lặp lại
```

Mỗi đường có biên lợi nhuận và khả năng mở rộng khác nhau.

Nếu AI sinh mã làm giảm 20% số giờ dự án nhưng hợp đồng tính theo giờ, số giờ có thể tính phí cũng có thể giảm. Nếu hợp đồng giá cố định, công ty giữ lại nhiều hơn phần lợi ích năng suất. Vì vậy cấu trúc hợp đồng quyết định kinh tế của AI.

## 10. Backlog không đồng nghĩa lợi nhuận

**Khối lượng hợp đồng còn lại (backlog / 수주잔고)** cho biết độ nhìn thấy doanh thu tương lai nhưng không bảo đảm biên lợi nhuận. Một backlog giá cố định lớn có thể chứa các dự án biên thấp hoặc thua lỗ.

Phân tích backlog cần xem giá trị hợp đồng, thời gian còn lại, cơ cấu khách hàng/ngành, tỷ lệ hợp đồng giá cố định so với T&M, phần phần cứng chuyển tiếp, biên lợi nhuận kỳ vọng và điều khoản hủy–thay đổi.

Vì vậy tiêu đề “đơn hàng tăng” mới chỉ là điểm bắt đầu.

## 11. Vốn lưu động trong kinh doanh dự án

Độ lệch thời gian thường xuất hiện giữa lúc trả lương hoặc trả vendor và lúc khách hàng được lập hóa đơn.

```text
công việc đã thực hiện
→ tài sản hợp đồng / doanh thu chưa lập hóa đơn
→ khách hàng nghiệm thu mốc
→ khoản phải thu
→ thu tiền mặt
```

Nếu tài sản hợp đồng tăng nhanh hơn doanh thu, có thể chỉ do giai đoạn của dự án; nhưng cũng có thể báo hiệu nghiệm thu bị chậm hoặc ghi nhận doanh thu quá sớm. Cần đọc cùng dòng tiền và điều khoản hợp đồng.

## 12. Ví dụ dự án

Dự án A:

```text
Giá trị hợp đồng = 500
Thời gian = 12 tháng
Lao động nội bộ = 120
Nhà thầu phụ = 220
Cloud / phần cứng = 80
Chi phí khác = 30
Lợi nhuận dự kiến = 50
```

Sau tháng thứ 8:

```text
thay đổi phạm vi chưa được khách hàng phê duyệt
chi phí thầu phụ +40
chậm lịch làm lao động tăng +25
```

Nếu công ty không thu hồi được chi phí thay đổi, lợi nhuận dự kiến chuyển từ +50 thành -15.

Bài học: ước tính của quản lý dự án là một đầu vào kế toán. Quản trị vận hành và báo cáo tài chính nối trực tiếp với nhau.

## 13. Kinh tế nghề nghiệp và kinh tế công ty

Công ty SI/SM có thể có lợi nhuận tốt nhưng một lập trình viên vẫn có kết quả nghề nghiệp rất khác tùy dự án.

Có thể lập bản đồ:

```text
sản phẩm / nền tảng nội bộ
so với dự án khách hàng

kiến trúc / phát triển lõi
so với điều phối / bảo trì

cloud / AI hiện đại
so với bảo trì hệ thống cũ

nhà thầu chính
so với tầng thầu phụ
```

Không nên dùng tăng trưởng doanh thu toàn công ty để suy ra một vị trí cụ thể chắc chắn có tốc độ học hỏi cao. Khi phân tích nhà tuyển dụng, phải thêm lớp đội nhóm và dự án bên cạnh phân tích doanh nghiệp.

## 14. Kịch bản căng thẳng: lương tăng + dự án giá cố định

Giả định:

```text
chi phí lao động bình quân +8%
đơn giá nhà thầu phụ +10%
50% backlog là hợp đồng giá cố định
khách hàng phê duyệt change request chậm
tỷ lệ sử dụng giảm từ 82% xuống 74%
```

Chuỗi tác động:

```text
chi phí/giờ ↑
+ số giờ tính phí ↓
+ giá trị hợp đồng cố định
→ biên lợi nhuận dự án co lại
→ nguy cơ lỗ hợp đồng
→ áp lực CFO nếu nghiệm thu / lập hóa đơn chậm
```

### Kịch bản cơ cấu tích cực

```text
nền SM định kỳ ổn định
tỷ trọng cloud managed service ↑
AI giảm số giờ giao dự án
tỷ trọng khách hàng bên ngoài ↑
tỷ trọng nền tảng / phần mềm sở hữu riêng ↑
```

Trong kịch bản này, doanh thu có thể chỉ tăng vừa phải nhưng chất lượng biên lợi nhuận và FCF cải thiện mạnh hơn.

## 15. Nhiệm vụ đọc DART/IR

Hãy tìm doanh thu theo nhóm kinh doanh, doanh thu với bên liên quan và công ty cùng tập đoàn, tài sản hợp đồng–khoản phải thu, backlog nếu được công bố, số nhân viên và chi phí lao động, dấu hiệu về tỷ lệ thuê ngoài, CAPEX cloud/trung tâm dữ liệu, tài sản vô hình–phần mềm, dự phòng hoặc hợp đồng thua lỗ và dòng tiền.

Nếu công ty chỉ công bố phân khúc rộng, có thể dùng thuyết minh và tài liệu IR để dựng lại cơ cấu kinh doanh nhưng phải phân biệt rõ **nhận định của ban lãnh đạo** với **sự kiện đã được kiểm toán**.

## 16. Logic định giá

Công ty dịch vụ CNTT không nên được định giá như SaaS thuần túy chỉ vì có AI hoặc cloud. Cơ cấu doanh thu quyết định khả năng mở rộng.

Có thể phân tách:

```text
sức tạo lợi nhuận định kỳ từ SM / dịch vụ quản lý
+ sức tạo lợi nhuận SI đã chuẩn hóa theo chu kỳ dự án
+ premium cho cloud / nền tảng / phần mềm nếu thật sự lặp lại và mở rộng được
+ giá trị của smart engineering
- rủi ro thực thi dự án
- tập trung khách hàng
- áp lực lao động / thầu phụ
```

Việc tăng hệ số định giá chỉ hợp lý nếu cơ cấu kinh tế thật sự chuyển sang doanh thu có chất lượng cao hơn, lặp lại hơn và mở rộng tốt hơn; không phải chỉ vì đổi nhãn từ DX sang AX.

## 17. Những yếu tố có thể phá vỡ luận điểm

Luận điểm tích cực có thể thất bại nếu doanh thu AI/cloud chủ yếu là phần chi phí chuyển tiếp biên thấp, tỷ lệ sử dụng nhân lực giảm, chi phí lương và thầu phụ tăng nhanh hơn đơn giá tính phí, xuất hiện dự án giá cố định thua lỗ lớn hoặc năng lực cạnh tranh bên ngoài yếu. Luận điểm tiêu cực có thể thất bại nếu nền doanh thu SM/dịch vụ quản lý rất ổn định, nền tảng sở hữu riêng mở rộng tốt, năng suất AI được giữ lại trong biên lợi nhuận và cơ cấu khách hàng bên ngoài tăng.

## 18. Bài tập cuối case

Tạo ma trận danh mục dự án:

| Loại dự án | Mô hình doanh thu | Rủi ro chính | Thời điểm tiền mặt | Khả năng mở rộng |
|---|---|---|---|---|
| SI giá cố định | mốc / tiến độ | vượt phạm vi / vượt chi phí | biến động | thấp–trung bình |
| SI T&M | giờ × đơn giá | tỷ lệ sử dụng / đơn giá | tương đối trực tiếp | thấp |
| SM | hợp đồng định kỳ | gia hạn / chi phí lao động | ổn định | trung bình |
| Cloud managed service | mức sử dụng / hợp đồng | chi phí vendor / cạnh tranh | định kỳ | trung bình–cao |
| Phần mềm / AI sở hữu riêng | giấy phép / mức sử dụng | khả năng chấp nhận sản phẩm | định kỳ | cao nếu có IP thật |

Sau đó ánh xạ doanh thu của công ty vào ma trận. Nếu thông tin công bố không đủ, hãy ghi rõ mức không chắc chắn thay vì đoán.

## Liên kết

Đọc cùng [34_digital_fintech_cloud_and_it_services](../34_digital_fintech_cloud_and_it_services.md), [12_labor_titles_compensation_and_workplace](../12_labor_titles_compensation_and_workplace.md), [13_business_culture_decision_making_and_communication](../13_business_culture_decision_making_and_communication.md), [09_disclosure_accounting_dart_kind](../09_disclosure_accounting_dart_kind.md) và [38_forensic_accounting_red_flags_and_earnings_quality](../38_forensic_accounting_red_flags_and_earnings_quality.md).