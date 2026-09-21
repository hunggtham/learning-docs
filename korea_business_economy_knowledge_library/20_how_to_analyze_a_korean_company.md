# Cách phân tích một công ty Hàn Quốc từ đầu đến cuối (Company Analysis Framework / 한국 기업 분석 프레임워크)

Đây là chương thực hành trung tâm của toàn bộ thư viện. Khi gặp một doanh nghiệp mới—dù là nơi định ứng tuyển, nhà cung cấp, đối tác dự án hay một công ty niêm yết—không nên bắt đầu từ biểu đồ giá cổ phiếu hoặc danh tiếng thương hiệu. Hãy đi theo chuỗi **pháp nhân → mô hình kinh doanh → ngành và chuỗi giá trị → bộ máy tài chính → quản trị → phân bổ vốn → rủi ro và định giá**.

Mục tiêu không phải tạo một danh sách kiểm tra máy móc. Mục tiêu là xây dựng một **mô hình nhân quả (causal model)** đủ rõ để trả lời ba câu hỏi: doanh nghiệp kiếm tiền bằng cách nào, điều gì làm cơ chế kinh tế của nó tốt hoặc xấu đi, và bằng chứng nào sẽ khiến giả thuyết ban đầu không còn đúng.

## Bước 0 — Đặt doanh nghiệp vào lịch sử và hệ sinh thái

Trước hết hãy hỏi doanh nghiệp hình thành trong giai đoạn nào của kinh tế Hàn Quốc. Một tập đoàn xây dựng hoặc công nghiệp hình thành trong thời kỳ tái thiết và phát triển công nghiệp nặng thường có nền tài sản, thói quen sử dụng nợ và mạng lưới nhà cung cấp rất khác một nền tảng số sinh ra trong thời kỳ Internet băng rộng. Một công ty dịch vụ CNTT thuộc chaebol có nhu cầu nội bộ ổn định (captive demand) khác một startup SaaS phải tự tìm từng khách hàng.

Nguồn gốc lịch sử không quyết định tương lai, nhưng thường giải thích được “DNA tổ chức” của doanh nghiệp. Nếu công ty thuộc một tập đoàn lớn, nên đọc [phả hệ doanh nghiệp](./00_history/08_company_genealogies.md) và [chaebol](./04_chaebol_and_large_business_groups.md).

## Bước 1 — Xác định đúng pháp nhân

Thương hiệu không đồng nghĩa với **pháp nhân (legal entity / 법인)**. Một thương hiệu có thể được vận hành bởi nhiều công ty con, trong khi một công ty niêm yết có thể sở hữu nhiều thương hiệu hoàn toàn khác nhau.

Cần xác định tên pháp nhân tiếng Hàn, trạng thái niêm yết, mã chứng khoán nếu có, tập đoàn mẹ, công ty con quan trọng, mã doanh nghiệp trên DART và phạm vi báo cáo hợp nhất. Nếu thuộc tập đoàn, tối thiểu hãy vẽ một tầng phía trên và một tầng phía dưới:

```text
Người kiểm soát / công ty mẹ
        ↓
Doanh nghiệp đang phân tích
        ↓
Các công ty con quan trọng
```

Câu hỏi cốt lõi là: **pháp nhân nào thực sự ký hợp đồng, vay nợ, sở hữu tài sản và tạo lợi nhuận?**

## Bước 2 — Xác định động cơ doanh thu

Doanh thu (revenue / 매출액) nên được tách theo phân khúc, khu vực, nhóm khách hàng và sản phẩm nếu doanh nghiệp công bố đủ dữ liệu.

Một quan hệ cơ bản là:

\[
Doanh\ thu = Sản\ lượng \times Giá
\]

Nhưng “sản lượng” có nghĩa khác nhau giữa các ngành. Với nền tảng số, đó có thể là người dùng hoặc giao dịch. Với ngân hàng, đơn vị kinh tế có thể là dư nợ, tài sản sinh lãi, tiền gửi hoặc phí. Với xây dựng, doanh thu liên quan đến tiến độ dự án và đơn hàng tồn đọng. Với SaaS, có thể nhìn số thuê bao và doanh thu định kỳ hằng năm (ARR).

Sau đó cần hỏi: sản lượng tăng do thị trường tăng hay doanh nghiệp giành thêm thị phần? Giá tăng do quyền định giá hay chỉ do lạm phát? Cơ cấu sản phẩm (mix) có làm biên lợi nhuận thay đổi không? Doanh thu có tính lặp lại hay chỉ xuất hiện một lần? Mức độ tập trung khách hàng có cao không?

## Bước 3 — Vẽ chuỗi giá trị và quyền thương lượng

Một sơ đồ tối thiểu:

```text
Đầu vào quan trọng
→ Quy trình của doanh nghiệp
→ Khách hàng trực tiếp
→ Nhu cầu cuối cùng
```

Trên sơ đồ đó, đánh dấu mức độ tập trung của nhà cung cấp, mức độ tập trung khách hàng, chi phí chuyển đổi (switching cost), sản phẩm thay thế, quy định, logistics, địa lý và quyền định giá (pricing power).

Biên lợi nhuận gộp thường chỉ có ý nghĩa khi biết doanh nghiệp đang đứng ở đâu trong chuỗi. Một nhà cung cấp linh kiện có công nghệ tốt nhưng phụ thuộc một khách hàng duy nhất vẫn có thể có quyền thương lượng yếu nếu người mua dễ thay nhà cung cấp.

## Bước 4 — Tìm đơn vị kinh tế tự nhiên

Doanh thu và lợi nhuận toàn công ty có thể che mất cơ chế kinh tế của từng đơn vị. Hãy tìm **đơn vị kinh tế (economic unit)** phù hợp với ngành.

Bán dẫn có thể nhìn wafer, bit, yield và ASP. Hàng không có thể nhìn hành khách-km, hệ số tải và doanh thu trên đơn vị vận chuyển. Nền tảng số có thể nhìn người dùng, giao dịch và tỷ lệ thu phí (take rate). SaaS có thể nhìn khách hàng, ARR và tỷ lệ rời bỏ (churn). Ngân hàng cần nhìn khoản vay, NIM và chi phí tín dụng. Xây dựng cần nhìn biên lợi nhuận dự án và mức phơi nhiễm PF.

Nếu chưa xác định được đơn vị kinh tế, phân tích thường vẫn đang ở mức quá tổng hợp.

## Bước 5 — Lợi thế cạnh tranh phải có cơ chế

**Hào kinh tế (economic moat / 경제적 해자)** có thể đến từ lợi thế chi phí, quy mô, công nghệ, yield, hiệu ứng mạng lưới, chi phí chuyển đổi, thương hiệu, giấy phép, phân phối, dữ liệu hoặc bí quyết quy trình.

Không nên dừng ở câu “công nghệ tốt”. Hãy nối thành chuỗi:

```text
Công nghệ tạo giá trị gì cho khách hàng?
↓
Khách hàng có sẵn sàng trả tiền cho giá trị đó không?
↓
Tại sao đối thủ khó sao chép?
↓
Lợi thế có xuất hiện trong biên lợi nhuận, thị phần hoặc tỷ lệ giữ chân không?
```

Một năng lực kỹ thuật không chuyển thành giá trị kinh tế có thể chỉ là sự xuất sắc về kỹ thuật, chưa chắc là lợi thế cạnh tranh có thể kiếm tiền.

## Bước 6 — Đọc ba báo cáo tài chính cùng nhau

Báo cáo kết quả kinh doanh cho biết khả năng tạo lợi nhuận. Bảng cân đối kế toán cho biết doanh nghiệp sở hữu nguồn lực gì và ai có quyền đòi hỏi trên các nguồn lực đó. Báo cáo lưu chuyển tiền tệ cho biết tiền thật sự di chuyển như thế nào.

Tối thiểu cần theo dõi tăng trưởng doanh thu, biên lợi nhuận gộp và hoạt động, khoản phải thu, tồn kho, dòng tiền hoạt động so với lợi nhuận ròng, CAPEX, nợ và lịch đáo hạn, chi phí lãi vay, số lượng cổ phiếu, cổ tức và mua lại cổ phiếu.

Ba báo cáo phải giải thích được lẫn nhau. Lợi nhuận tăng liên tục nhưng tiền mặt giảm liên tục là tín hiệu cần tìm nguyên nhân.

## Bước 7 — Đối chiếu lợi nhuận với tiền mặt

Kế toán dồn tích (accrual accounting / 발생주의 회계) có thể ghi nhận doanh thu trước khi thu tiền. Nếu lợi nhuận ròng tăng nhưng dòng tiền từ hoạt động kinh doanh (CFO) yếu, hãy kiểm tra khoản phải thu, tồn kho, tài sản hợp đồng, lợi nhuận một lần, dự phòng và việc vốn hóa chi phí.

Một xấp xỉ thường dùng cho doanh nghiệp công nghiệp là:

\[
Dòng\ tiền\ tự\ do\ (FCF) \approx CFO - CAPEX
\]

Tuy nhiên không nên áp dụng máy móc cho ngân hàng hoặc bảo hiểm vì cấu trúc bảng cân đối và khái niệm vốn hoạt động của các ngành tài chính khác doanh nghiệp công nghiệp.

## Bước 8 — Xây cầu nối tài chính nhiều năm

Một năm có thể nằm đúng đỉnh hoặc đáy chu kỳ. Nên nhìn ít nhất 5–10 năm khi dữ liệu cho phép:

```text
Doanh thu
→ Lợi nhuận hoạt động
→ Biên lợi nhuận
→ CFO
→ CAPEX
→ FCF
→ Nợ
→ Số lượng cổ phiếu
→ ROIC / ROE
```

Đánh dấu các sự kiện lớn như mua lại doanh nghiệp, chia tách, mở nhà máy, đỉnh/đáy chu kỳ, thay đổi chuẩn kế toán hoặc thay đổi quy định. Mục tiêu là phân biệt **thay đổi cấu trúc (structural change)** với **nhiễu tạm thời (temporary noise)**.

## Bước 9 — Phân biệt chu kỳ và thay đổi cấu trúc

Nhiều ngành lớn của Hàn Quốc có tính chu kỳ mạnh: bán dẫn, hóa chất, thép, đóng tàu, xây dựng và pin. Lợi nhuận ở đỉnh chu kỳ có thể làm P/E trông rất thấp ngay trước khi lợi nhuận giảm.

Thay vì kéo dài lợi nhuận một năm sang tương lai, hãy ước lượng **lợi nhuận chuẩn hóa (normalized earnings / 정상화 이익)** và hỏi lợi nhuận tăng do chu kỳ, tỷ giá, chi phí đầu vào, thị phần, công nghệ, công suất hay quyền định giá. Mỗi động lực có độ bền khác nhau.

## Bước 10 — Đọc bảng cân đối và đòn bẩy ẩn

Nợ vay trên trang đầu báo cáo chưa chắc bằng tổng đòn bẩy kinh tế. Phần thuyết minh có thể chứa hợp đồng thuê, bảo lãnh, cam kết PF, factoring, phái sinh, công ty liên kết chưa hợp nhất, nghĩa vụ hưu trí và khoản phải thu với bên liên quan.

Một doanh nghiệp có nợ vay thấp nhưng bảo lãnh lớn vẫn có rủi ro đuôi (tail risk) đáng kể. Xem thêm [ngân hàng và tài trợ doanh nghiệp](./11_banks_finance_and_corporate_funding.md).

## Bước 11 — Phân tích quản trị doanh nghiệp

Cần xem cổ đông kiểm soát, bên liên quan, thành phần hội đồng quản trị, cổ phiếu quỹ, sáp nhập/chia tách, giao dịch nội bộ và vấn đề kế nhiệm.

Với công ty thuộc chaebol, câu hỏi quan trọng là:

> Quyết định này tối ưu lợi ích của chính pháp nhân đang phân tích hay chủ yếu phục vụ kiến trúc kiểm soát của toàn tập đoàn?

Không nên mặc định có xung đột. Mục tiêu là tách rõ hai cấp độ lợi ích.

## Bước 12 — Theo dõi phân bổ vốn

Dòng tiền hoạt động có thể được dùng cho CAPEX duy trì, CAPEX tăng trưởng, R&D, M&A, trả nợ, cổ tức, mua lại cổ phiếu hoặc tích lũy tiền mặt.

Chất lượng quản lý thường thể hiện rõ hơn qua mô hình phân bổ vốn nhiều năm hơn là qua một bài phát biểu của ban lãnh đạo. Tăng trưởng chỉ tạo giá trị nếu lợi nhuận trên phần vốn đầu tư mới cao hơn chi phí vốn.

Một xấp xỉ hữu ích là:

\[
ROIIC \approx \frac{\Delta NOPAT}{\Delta Vốn\ đầu\ tư}
\]

Nếu doanh nghiệp tái đầu tư rất lớn nhưng NOPAT tăng thêm thấp, doanh thu tăng vẫn có thể phá hủy giá trị.

## Bước 13 — Chuyển câu chuyện của ban lãnh đạo thành biến đo được

Các cụm từ như “AI”, “EV”, “xanh” hay “toàn cầu” trong tài liệu IR mới chỉ là câu chuyện. Hãy chuyển chúng thành các biến cụ thể: CAPEX bao nhiêu, công suất bao nhiêu, khi nào tăng sản lượng, khách hàng là ai, giả định tỷ lệ sử dụng công suất thế nào, ASP và biên lợi nhuận bao nhiêu, ROIC cần đạt mức nào.

Nếu một câu chuyện không thể nối với doanh thu, chi phí, tài sản hoặc dòng tiền, hãy coi nó là **giả thuyết (hypothesis)** chứ chưa phải sự thật.

## Bước 14 — Tách sự thật, tuyên bố của quản lý và suy luận

Một ghi chú nghiên cứu nên phân biệt rõ:

**Sự thật (fact):** báo cáo công bố CAPEX 5 nghìn tỷ KRW.

**Tuyên bố của quản lý (management claim):** CAPEX này sẽ tạo vị thế dẫn đầu.

**Suy luận (inference):** tỷ lệ sử dụng công suất phải đạt một mức nhất định để lợi nhuận dự án vượt tỷ suất yêu cầu.

Trộn ba tầng này là một nguồn lớn của thiên kiến xác nhận (confirmation bias).

## Bước 15 — Chọn doanh nghiệp so sánh đúng tầng chuỗi giá trị

Không nên so sánh toàn bộ Samsung Electronics với TSMC chỉ vì cả hai đều liên quan đến bán dẫn. Hãy so bộ nhớ với bộ nhớ, foundry với foundry, nhà sản xuất cathode với nhà sản xuất cathode, nhà sản xuất cell pin với nhà sản xuất cell, công ty SI với công ty SI và ngân hàng Internet với nhóm ngân hàng/fintech có cơ chế kinh tế tương đồng.

So sánh ngang hàng (peer comparison) chỉ có ý nghĩa khi các doanh nghiệp kiếm tiền theo cơ chế đủ giống nhau.

## Bước 16 — Lập ma trận phơi nhiễm kinh tế vĩ mô

Xác định những biến thực sự có liên hệ nhân quả với doanh nghiệp: KRW/USD, lãi suất BOK, dầu hoặc hàng hóa, nhu cầu Trung Quốc/Mỹ, nợ hộ gia đình, nhà ở, chu kỳ bán dẫn và quy định. Không cần đưa mọi biến vào mô hình. Chỉ giữ những biến có đường truyền tác động rõ.

Xem [cơ chế truyền dẫn từ nền kinh tế đến doanh nghiệp](./21_economy_to_company_transmission.md).

## Bước 17 — Chỉ định giá sau khi hiểu cơ chế kinh tế

Không có một chỉ số định giá phù hợp mọi ngành. P/E hữu ích hơn khi lợi nhuận tương đối ổn định hoặc đã được chuẩn hóa. P/B kết hợp ROE thường phù hợp hơn với tổ chức tài chính. EV/EBITDA hữu ích khi so sánh tài sản hoạt động giữa các cấu trúc vốn khác nhau. DCF phù hợp khi có thể mô hình hóa dòng tiền với các giả định minh bạch.

\[
EV = \sum_{t=1}^{n}\frac{FCF_t}{(1+WACC)^t} + \frac{Giá\ trị\ cuối\ kỳ}{(1+WACC)^n}
\]

DCF không tạo ra sự chắc chắn. Giá trị lớn nhất của nó là buộc các giả định phải lộ ra. Bảng độ nhạy thường hữu ích hơn một giá mục tiêu duy nhất.

## Bước 18 — Định giá ngược

Thay vì chỉ hỏi “giá hợp lý là bao nhiêu?”, có thể hỏi:

> Giá thị trường hiện tại đang ngầm yêu cầu mức tăng trưởng, biên lợi nhuận hoặc ROIC bao nhiêu?

Đây là **DCF ngược (reverse DCF / 역산 DCF)**. Nếu giá hiện tại chỉ hợp lý khi biên lợi nhuận tăng lên mức doanh nghiệp chưa từng đạt, giả thuyết cần bằng chứng rất mạnh.

## Bước 19 — Kiểm tra sức chịu đựng

Tạo các cú sốc phù hợp với ngành, chẳng hạn nhu cầu giảm 10%, ASP giảm 15%, chi phí đầu vào tăng 20%, lãi suất tăng 150 điểm cơ bản, KRW biến động 10%, mất khách hàng lớn, nhà máy tăng sản lượng chậm hoặc bảo lãnh PF trở thành nghĩa vụ thực tế.

Sau đó lần theo tác động đến doanh thu, biên lợi nhuận, tiền mặt, điều khoản nợ và nhu cầu huy động vốn. Kiểm tra sức chịu đựng (stress test) nên tập trung vào biến có thể làm giả thuyết đổi bản chất, không chỉ làm EPS giảm vài phần trăm.

## Bước 20 — Xác định điều kiện làm giả thuyết sai

Mỗi phân tích nên ghi rõ 2–5 **điều kiện bác bỏ giả thuyết (thesis breakers)**. Ví dụ: thị phần HBM không tăng, nhà máy mới có tỷ lệ sử dụng dưới 60%, khách hàng lớn đổi nhà cung cấp, bảo lãnh PF trở thành nợ thực tế, phê duyệt pháp lý thất bại hoặc churn vượt ngưỡng.

Việc ghi trước các điều kiện này giúp chống thiên kiến xác nhận và tâm lý tiếc công đã bỏ ra.

## Bước 21 — Thực hiện pre-mortem

Giả sử hai năm sau phân tích sai hoàn toàn. Hãy hỏi nguyên nhân hợp lý có thể là gì: chu kỳ đảo chiều, công nghệ bị thay thế, mất khách hàng, phân bổ vốn sai, vấn đề quản trị, thay đổi quy định, khủng hoảng nguồn vốn hay chậm thực thi.

**Pre-mortem** là cách tìm rủi ro lớn trước khi chúng trở thành tiêu đề tin tức.

## Bước 22 — Nếu mục tiêu là nghề nghiệp, thêm lớp phân tích việc làm

Nếu công ty là nơi định ứng tuyển, cần xem độ ổn định của đơn vị kinh doanh, xu hướng nhân sự, tỷ lệ nghỉ việc, cấu trúc lương thưởng, hệ thống thăng tiến, tỷ lệ thuê ngoài, nguồn dự án, khả năng chuyển đổi kỹ năng, chất lượng quản lý và độ rộng/sâu của vai trò.

Một công ty tài chính mạnh chưa chắc cung cấp vai trò tốt cho sự nghiệp; một công ty nhỏ cũng chưa chắc có môi trường học tập kém. Xem [lao động và chức danh](./12_labor_titles_compensation_and_workplace.md) cùng [văn hóa doanh nghiệp](./13_business_culture_decision_making_and_communication.md).

## Thứ tự ưu tiên nguồn nghiên cứu

```text
Báo cáo đã kiểm toán trên DART
↓
Thông báo KIND / KRX
↓
IR và công bố kết quả của doanh nghiệp
↓
Cơ quan quản lý / dữ liệu chính phủ
↓
Dữ liệu ngành
↓
Tin tức
↓
Cộng đồng / đánh giá người dùng hoặc nhân viên
```

Nguồn ở tầng thấp không vô dụng. Đánh giá nhân viên có thể hữu ích để hiểu văn hóa; báo chí có thể cung cấp bối cảnh. Tuy nhiên số liệu tài chính nên quay về nguồn sơ cấp bất cứ khi nào có thể.

## Mẫu nghiên cứu có thể tái sử dụng

```markdown
# Tên doanh nghiệp

## 1. Pháp nhân và cấu trúc tập đoàn
## 2. Bối cảnh lịch sử
## 3. Động cơ doanh thu
## 4. Chuỗi giá trị / khách hàng / nhà cung cấp
## 5. Đơn vị kinh tế
## 6. Lợi thế cạnh tranh
## 7. Lịch sử tài chính
## 8. Dòng tiền và vốn lưu động
## 9. Bảng cân đối và nguồn vốn
## 10. Quản trị / bên liên quan
## 11. Phân bổ vốn
## 12. Phơi nhiễm ngành và kinh tế vĩ mô
## 13. Định giá / kỳ vọng hàm ý
## 14. Rủi ro / kiểm tra sức chịu đựng
## 15. Điều kiện bác bỏ giả thuyết / pre-mortem
## 16. Góc nhìn nghề nghiệp nếu cần
## Nguồn
```

## Mental Model — Mô hình tư duy

> Phân tích doanh nghiệp là quá trình chuyển từ **thương hiệu → pháp nhân → cỗ máy kinh tế → cỗ máy tài chính → quản trị → kỳ vọng thị trường**.

Một chuỗi câu hỏi ngắn có thể giữ trong đầu:

```text
Ai kiểm soát doanh nghiệp?
→ Doanh nghiệp bán gì?
→ Vì sao khách hàng trả tiền?
→ Vì sao đối thủ không dễ sao chép?
→ Lợi nhuận có chuyển thành tiền mặt không?
→ Tăng trưởng cần bao nhiêu vốn?
→ Rủi ro nằm ở bảng cân đối hay ngoài bảng cân đối?
→ Ban quản lý phân bổ vốn ra sao?
→ Giá hiện tại đang ngầm giả định điều gì?
→ Bằng chứng nào sẽ làm giả thuyết sai?
```

Khi trả lời được chuỗi này bằng bằng chứng thay vì cảm giác, ta đã chuyển từ “biết tên công ty” sang thực sự hiểu doanh nghiệp.
