# Xây dựng & Project Finance Hàn Quốc — lợi nhuận nhà thầu, 시행사, bảo lãnh PF và rủi ro tái cấp vốn

Case này không dùng một công ty duy nhất mà dựng một **tình huống mô phỏng xây dựng/PF tại Hàn Quốc** để học một cấu trúc rủi ro xuất hiện khá phổ biến. Công ty xây dựng có thể báo cáo backlog và lợi nhuận kế toán ổn định trong khi rủi ro tài chính dự án lại nằm ở bảo lãnh, khoản vay cầu nối, căn hộ chưa bán hoặc các SPV liên quan.

Vì vậy case tập trung vào sự khác biệt giữa **hoạt động xây dựng cốt lõi** và **rủi ro tài chính dự án có điều kiện (contingent PF risk)**.

Xem [18_construction_real_estate_and_project_finance](../18_construction_real_estate_and_project_finance.md), [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md) và [38_forensic_accounting_red_flags_and_earnings_quality](../38_forensic_accounting_red_flags_and_earnings_quality.md).

## 1. Ai là ai trong một dự án phát triển bất động sản?

Người mới thường gọi tất cả là “công ty xây dựng”, nhưng một dự án có nhiều chủ thể kinh tế khác nhau.

**Chủ đầu tư phát triển (developer / 시행사)** tìm đất, cấu trúc dự án, xin giấy phép, thu xếp vốn và chịu phần lớn kinh tế phát triển dự án.

**Nhà thầu xây dựng (contractor / 시공사)** xây công trình theo hợp đồng. Tại Hàn Quốc, nhà thầu lớn đôi khi còn cung cấp hỗ trợ tín dụng hoặc tham gia sâu hơn một nhà thầu thuần túy.

**Bên cho vay PF** cung cấp vốn dựa trên dòng tiền dự án, tài sản bảo đảm và các hình thức hỗ trợ tín dụng.

**SPV/PFV** có thể là pháp nhân chuyên biệt nắm giữ tài sản và nghĩa vụ của dự án.

Công ty tín thác, công ty chứng khoán, ngân hàng tiết kiệm, công ty bảo hiểm hoặc các tổ chức tài chính khác cũng có thể tham gia cấu trúc vốn.

Nếu không xác định đúng vai trò, rất dễ nhầm nợ của SPV với nợ của nhà thầu — hoặc ngược lại bỏ qua bảo lãnh khiến nghĩa vụ của SPV cuối cùng quay về nhà thầu.

## 2. Project Finance khác khoản vay doanh nghiệp thông thường

Trong **tài chính doanh nghiệp (corporate finance)**, bên cho vay dựa nhiều vào dòng tiền và bảng cân đối của cả công ty.

Trong **tài chính dự án (Project Finance / PF / 프로젝트 파이낸싱)**, logic trả nợ tập trung vào dòng tiền của chính dự án.

```text
Đất / giấy phép
→ vốn cầu nối
→ xây dựng / 본PF
→ bán trước hoặc cho thuê
→ hoàn thành
→ khách hàng thanh toán / bán tài sản
→ trả nợ PF
```

Tuy nhiên “không truy đòi (non-recourse)” trong lý thuyết không có nghĩa mọi rủi ro PF ở Hàn Quốc đều tách hoàn toàn khỏi công ty mẹ. Bảo lãnh, nhận nợ thay, cam kết hoàn thành công trình hoặc hỗ trợ thanh khoản có thể nối rủi ro dự án trở lại nhà tài trợ hoặc nhà thầu.

## 3. Khoản vay cầu nối: giai đoạn rủi ro trước khi dự án đủ điều kiện 본PF

**Khoản vay cầu nối (bridge loan / 브릿지론)** tài trợ giai đoạn sớm như mua đất và chuẩn bị dự án trước khi đủ điều kiện chuyển sang PF chính.

Rủi ro cao vì:

```text
Giấy phép chưa hoàn tất
Xây dựng chưa bắt đầu
Bán trước chưa rõ
Lối ra phụ thuộc tái cấp vốn sang 본PF
```

Nếu lãi suất tăng hoặc tính khả thi của dự án xấu đi, khoản vay cầu nối có thể không tái cấp vốn được.

Đây là **rủi ro kỳ hạn và tái cấp vốn (maturity/refinancing risk)** điển hình.

## 4. Bán trước (분양) và mô hình dòng tiền

Dự án nhà ở Hàn Quốc thường sử dụng **bán trước (presale / 분양)**. Cam kết và các đợt thanh toán của người mua có thể hỗ trợ dòng tiền dự án.

\[
Doanh\ thu\ kỳ\ vọng = Số\ căn \times Giá\ bán\ kỳ\ vọng
\]

Nhưng tính khả thi phải trừ:

```text
Đất
Chi phí xây dựng
Chi phí tài chính
Marketing
Thuế / phí
Dự phòng rủi ro
```

Nếu giá bán bị giới hạn hoặc nhu cầu yếu trong khi chi phí xây dựng và lãi vay tăng, biên lợi nhuận của chủ đầu tư bị thu hẹp.

## 5. Backlog của nhà thầu không bảo đảm lợi nhuận

Backlog tạo khả năng dự báo doanh thu nhưng biên lợi nhuận phụ thuộc giả định chi phí ban đầu và lạm phát chi phí.

Ví dụ:

```text
Doanh thu hợp đồng = 1.000
Chi phí ước tính lúc ký = 900
Lợi nhuận kỳ vọng = 100
```

Nếu chi phí vật liệu và lao động tăng khiến tổng chi phí ước tính thành 1.020, dự án chuyển từ +100 sang -20.

Hợp đồng dài hạn vì vậy có **rủi ro ước tính (estimate risk)**. Tùy chuẩn mực và tình hình thực tế, kế toán có thể phải ghi nhận dự phòng hoặc tổn thất dự kiến trước khi công trình hoàn thành vật lý.

## 6. Ghi nhận theo tiến độ và tài sản hợp đồng

Doanh thu xây dựng thường được ghi nhận theo tiến độ khi đủ điều kiện kế toán.

Cần tách:

```text
Doanh thu kế toán đã ghi nhận
so với
Hóa đơn đã phát hành
so với
Tiền đã thu
```

Nếu doanh thu được ghi nhận trước khi lập hóa đơn hoặc thu tiền, **tài sản hợp đồng (contract asset / 계약자산)** có thể tăng.

Tài sản hợp đồng tăng không tự động là dấu hiệu xấu; có thể phù hợp với tiến độ thanh toán. Nhưng nếu tăng nhanh hơn doanh thu trong nhiều kỳ, cần kiểm tra giả định tiến độ, tranh chấp thanh toán và khả năng thu tiền.

## 7. Bảo lãnh: rủi ro có thể nằm ngoài con số nợ nổi bật

Một nhà thầu có thể có 2 nghìn tỷ won nợ doanh nghiệp nhưng đồng thời bảo lãnh nghĩa vụ PF của nhiều dự án. Nếu dự án thất bại và bảo lãnh bị kích hoạt, nghĩa vụ kinh tế có thể tăng đột ngột.

\[
Đòn\ bẩy\ kinh\ tế \neq Chỉ\ riêng\ nợ\ vay\ báo\ cáo
\]

Cần đọc:

```text
Khoản vay
+ trái phiếu
+ nợ thuê khi phù hợp
+ bảo lãnh / cam kết
+ nghĩa vụ nhận nợ thay
+ hỗ trợ thanh khoản
```

Không cộng tất cả một cách máy móc; phải phân loại điều kiện kích hoạt và xác suất.

## 8. Cam kết hoàn thành công trình (책임준공)

**Cam kết hoàn thành công trình (completion guarantee / 책임준공)** có thể buộc nhà thầu phải hoàn tất xây dựng dù chủ đầu tư gặp khó khăn, tùy điều khoản hợp đồng.

Nó có giá trị với bên cho vay vì giảm rủi ro dự án dở dang, nhưng chuyển một phần rủi ro sang nhà thầu.

Cần đọc chính xác nghĩa vụ pháp lý. Không nên coi mọi `책임준공` như bảo lãnh nợ, nhưng cũng không được bỏ qua chỉ vì nó không xuất hiện như khoản vay trên bảng cân đối.

## 9. Vòng xoáy tái cấp vốn

Dự án PF có thể rơi vào vòng xoáy bất lợi:

```text
Lãi suất tăng / nhu cầu bất động sản giảm
→ tỷ lệ bán trước yếu
→ giá trị và tính khả thi dự án giảm
→ bên cho vay đòi chênh lệch lãi cao hơn hoặc từ chối tái cấp vốn
→ chi phí tài chính tăng
→ tính khả thi xấu thêm
→ chủ đầu tư cần thêm vốn / hỗ trợ
→ áp lực thanh khoản lan rộng
```

Nếu nhiều dự án cùng gặp vấn đề, rủi ro có thể truyền sang nhà thầu và các công ty chứng khoán/tổ chức tài chính liên quan.

## 10. Căn chưa bán (미분양)

**Căn chưa bán (unsold units / 미분양)** là chỉ báo quan trọng nhưng cần bối cảnh.

Căn chưa bán trước khi hoàn thành vẫn có thể bán sau. Căn đã hoàn thành nhưng chưa bán thường nghiêm trọng hơn vì chi phí xây dựng đã phát sinh và chi phí tài chính vẫn tiếp tục.

Rủi ro phụ thuộc địa điểm, mức giá, chất lượng dự án và đòn bẩy. Không chỉ đếm số căn; cần hỏi giá bán kỳ vọng còn đủ trả nợ và chi phí còn lại hay không.

## 11. Khác biệt theo khu vực

Nhu cầu nhà ở tại Seoul và vùng lõi 수도권 có thể khác rất xa các dự án tỉnh.

Giá nhà trung bình toàn quốc có thể che tình trạng dư cung cục bộ.

Phân tích dự án cần xem:

```text
Dân số / hình thành hộ gia đình địa phương
Việc làm / giao thông
Nguồn cung cạnh tranh
Tốc độ hấp thụ bán trước
Giá bán so với thu nhập địa phương
Chi phí đất
```

Xây dựng/PF là một trong những lĩnh vực mà địa lý trở thành biến tài chính trực tiếp.

Xem [24_regional_clusters_and_industrial_geography](../24_regional_clusters_and_industrial_geography.md).

## 12. Ví dụ dự án mô phỏng

Giả sử:

```text
Doanh thu kỳ vọng: 1,5 nghìn tỷ KRW
Đất + xây dựng + chi phí khác: 1,2 nghìn tỷ
Biên lợi nhuận kỳ vọng trước chi phí tài chính: 0,3 nghìn tỷ
Nợ PF: 0,8 nghìn tỷ
```

Nếu giá bán và tốc độ hấp thụ yếu khiến doanh thu kỳ vọng giảm 10%:

\[
1,5T \times 0,9 = 1,35T
\]

Nếu chi phí xây dựng đồng thời tăng 8% trên phần chi phí xây dựng 0,8T, chi phí tăng thêm 0,064T. Bộ đệm lợi nhuận nhanh chóng bị thu hẹp.

Nếu chậm hoàn thành còn làm chi phí lãi vay tăng, phần vốn chủ sở hữu mỏng có thể gần như biến mất.

Bài học: **các cú sốc phần trăm nhỏ ở doanh thu và chi phí có thể phá hủy phần vốn chủ sở hữu mỏng vì đòn bẩy**.

## 13. Kiểm tra sức chịu đựng của nhà thầu

Một kịch bản nhân quả hợp lý:

```text
Nhu cầu nhà ở yếu
→ tỷ lệ bán trước thấp
→ tiền vào dự án chậm
→ chênh lệch lãi PF +300 bp
→ thanh khoản của 시행사 xấu đi
→ nhà thầu phải hỗ trợ theo bảo lãnh/cam kết
→ CFO của nhà thầu xấu đi
→ nợ ròng tăng
→ áp lực xếp hạng tín nhiệm
→ chi phí tái cấp vốn cấp doanh nghiệp tăng
```

Đây là vòng phản hồi giữa dự án và bảng cân đối của công ty mẹ/nhà thầu.

## 14. Mối liên hệ với công ty chứng khoán và tổ chức tài chính

Rủi ro PF không chỉ nằm ở nhà thầu. Công ty chứng khoán có thể thu xếp, bảo lãnh, phân phối hoặc nắm giữ các khoản liên quan đến PF.

Suy giảm bất động sản có thể truyền theo:

```text
Dự án bất động sản
→ 시행사
→ nhà thầu
→ công ty chứng khoán / ngân hàng tiết kiệm / bên cho vay
→ thị trường vốn ngắn hạn
```

Đây là lý do chapter xây dựng phải đọc cùng tài chính.

## 15. Thứ tự đọc DART cho nhà thầu

```text
1. Doanh thu theo mảng / backlog
2. Danh sách dự án lớn
3. Ước tính chi phí / dự phòng
4. Tài sản hợp đồng / khoản phải thu
5. Tồn kho / dự án chưa bán nếu có công bố
6. Nợ vay và kỳ hạn
7. Bảo lãnh / nghĩa vụ tiềm tàng
8. Hỗ trợ tín dụng liên quan PF
9. Bên liên quan / SPV
10. Dòng tiền và thanh khoản
```

Báo cáo kết quả kinh doanh chỉ là điểm bắt đầu.

## 16. Định giá: lợi nhuận chuẩn hóa + rủi ro tiềm tàng

P/E thấp của nhà thầu có thể phản ánh chu kỳ hoặc lo ngại PF chưa hiện rõ.

Có thể xây cầu phân tích:

```text
Lợi nhuận xây dựng chuẩn hóa
+ giá trị các mảng / tài sản khác
- nợ ròng cấp doanh nghiệp
- tổn thất PF tiềm tàng đã điều chỉnh xác suất
= khung giá trị vốn chủ sở hữu
```

Không cần giả vờ có độ chính xác tuyệt đối. Mục tiêu là không đặt rủi ro bảo lãnh bằng 0% hoặc 100% một cách máy móc.

## 17. Những nhầm lẫn thường gặp

### “Backlog lớn thì nhà thầu an toàn”

Sai vì biên lợi nhuận backlog và rủi ro tài chính dự án là hai lớp khác nhau.

### “Nợ PF nằm ở SPV nên công ty mẹ không liên quan”

Sai nếu có bảo lãnh, hỗ trợ thanh khoản hoặc nghĩa vụ chiến lược.

### “Bảo lãnh bằng nợ ngay lập tức”

Cũng sai. Bảo lãnh là nghĩa vụ có điều kiện; phải đọc điều kiện kích hoạt và xác suất.

### “Giá nhà toàn quốc ổn thì mọi dự án PF ổn”

Sai vì bất động sản mang tính địa phương rất cao.

## 18. Bài tập nghiên cứu

| Chỉ tiêu | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Đơn hàng mới | | | | | |
| Backlog | | | | | |
| Biên lợi nhuận xây dựng | | | | | |
| Tài sản hợp đồng | | | | | |
| Khoản phải thu | | | | | |
| Nợ doanh nghiệp | | | | | |
| Bảo lãnh PF | | | | | |
| CFO | | | | | |
| Chi phí lãi | | | | | |

Bên cạnh bảng, hãy lập **bản đồ phơi nhiễm dự án (project exposure map)** riêng thay vì chỉ ghi tổng giá trị bảo lãnh.

## Mô hình tư duy cuối

> Phân tích xây dựng/PF Hàn Quốc là bài toán **thời điểm dòng tiền + vốn chủ sở hữu dự án mỏng + nghĩa vụ truy đòi có điều kiện**. Nhà thầu có thể trông khỏe trên báo cáo lợi nhuận nhưng yếu nếu nhiều dự án cùng lúc cần hỗ trợ thanh khoản. Luôn đi theo chuỗi: **kinh tế dự án → cấu trúc tài trợ → nghĩa vụ pháp lý → thanh khoản doanh nghiệp**.

Case này hoàn tất một vòng quan trọng của lớp thực hành: từ bán dẫn, ô tô, nền tảng số, SME, SI/SM tới ngân hàng, pin, quốc phòng, thương mại/logistics và tài chính bất động sản. Khi gặp công ty mới, hãy chọn case có hàm sản xuất gần nhất rồi điều chỉnh cây động lực thay vì bắt đầu lại từ số 0.