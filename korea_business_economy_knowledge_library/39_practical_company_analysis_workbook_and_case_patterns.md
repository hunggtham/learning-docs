# Workbook thực hành phân tích doanh nghiệp — từ báo cáo đến giả thuyết, kịch bản và quyết định (실전 기업분석 워크북)

Các chương trước giải thích lịch sử, kinh tế vĩ mô, ngành, kế toán, quản trị và nguồn vốn. Chương này biến các kiến thức đó thành một **bài thực hành tổng hợp (workbook)**. Mục tiêu là khi gặp một công ty Hàn Quốc mới, người đọc có thể mở DART/KIND/IR, tự dựng mô hình kinh tế, phát hiện những câu hỏi còn thiếu và viết một ghi chú nghiên cứu có thể kiểm chứng.

Đây không phải danh sách để đánh dấu cho xong. Nó là một trình tự giúp chuyển dữ liệu rời rạc thành **mô hình nhân quả (causal model)**.

## 1. Kết quả cuối cùng của một bài phân tích nên là gì?

Một bài phân tích tốt không nhất thiết dài hàng trăm trang. Nó cần trả lời rõ năm câu hỏi: doanh nghiệp thực sự kiếm tiền bằng cơ chế nào; những biến nào quyết định lợi nhuận và dòng tiền; bảng cân đối có chịu được kịch bản xấu hay không; quản trị và phân bổ vốn có bảo vệ giá trị cho cổ đông/chủ nợ không; và điều kiện nào khiến nhận định hiện tại sai.

Nếu chưa trả lời được năm câu này, thu thập thêm dữ liệu có thể chỉ làm tăng lượng thông tin chứ chưa tăng mức độ hiểu.

## 2. Tạo hồ sơ nhận dạng một trang

Trước khi mô hình hóa, ghi lại:

```text
Tên pháp nhân:
Mã chứng khoán:
Tập đoàn / công ty mẹ:
Công ty con chính:
Phân khúc chính:
Khu vực địa lý chính:
Khách hàng lớn nếu có công bố:
Đầu vào quan trọng:
Đối thủ chính:
Thị trường niêm yết:
Phạm vi hợp nhất báo cáo:
Năm tài chính:
```

Không bắt đầu bằng định giá. Nếu xác định sai pháp nhân, toàn bộ phân tích phía sau có thể sai theo.

## 3. Mô tả doanh nghiệp trong một câu

Cố gắng hoàn thành câu:

> Công ty X kiếm tiền bằng cách ___ cho ___; khả năng sinh lời chủ yếu phụ thuộc vào ___ và rủi ro bảng cân đối lớn nhất là ___.

Ví dụ, một nhà sản xuất bộ nhớ bán DRAM/NAND cho khách hàng thiết bị và trung tâm dữ liệu; lợi nhuận phụ thuộc vào ASP × lượng bit xuất bán × chi phí mỗi bit, còn rủi ro lớn nằm ở chu kỳ, CAPEX và chuyển đổi công nghệ.

Nếu vẫn không viết được câu này một cách cụ thể, nghĩa là chưa hiểu mô hình kinh doanh đủ sâu.

## 4. Vẽ cỗ máy kinh tế của doanh nghiệp

Khung chung:

```text
Động lực nhu cầu
    ↓
Sản lượng / mức hoạt động
    ×
Giá / khả năng kiếm tiền
    ↓
Doanh thu
    - chi phí biến đổi
    - chi phí cố định
    ↓
Lợi nhuận hoạt động
    ± thay đổi vốn lưu động
    - CAPEX
    ↓
Dòng tiền
```

Sau đó thay các biến bằng chỉ tiêu phù hợp với từng ngành.

## 5. Mẫu A — Bán dẫn

Một mô hình bán dẫn nên đi theo chuỗi:

```text
Nhu cầu cuối cùng
→ nhu cầu bit
→ tăng trưởng nguồn cung / công suất
→ tỷ lệ sử dụng công suất
→ ASP
→ doanh thu
→ biên lợi nhuận gộp
→ CAPEX / khấu hao
→ dòng tiền tự do
```

Cần hỏi cơ cấu nhu cầu AI/server/mobile/PC thay đổi thế nào; đối thủ thêm bao nhiêu công suất; yield thay đổi ra sao; chuyển đổi công nghệ ảnh hưởng chi phí mỗi bit thế nào; giá hợp đồng và giá giao ngay có bền không; và doanh nghiệp đang đầu tư ngược chu kỳ hay chạy theo đỉnh nhu cầu.

Một kịch bản cơ sở có thể giả định lượng bit xuất bán tăng 15%, ASP tăng 5% và chi phí mỗi bit giảm 10%. Kịch bản xấu có thể là lượng bit chỉ tăng 5%, ASP giảm 20% và chi phí mỗi bit chỉ giảm 5%.

Do chi phí cố định và khấu hao lớn, lợi nhuận hoạt động có thể biến động mạnh hơn doanh thu. Đây là **đòn bẩy hoạt động (operating leverage)**. Xem [bán dẫn](./14_semiconductors_electronics_display.md).

## 6. Mẫu B — Ô tô

Cơ chế kinh tế cơ bản:

```text
Số xe bán
× ASP / cơ cấu sản phẩm
= Doanh thu
- nguyên vật liệu
- lao động
- ưu đãi bán hàng
- bảo hành
= Lợi nhuận hoạt động ô tô
± kết quả của công ty tài chính nội bộ
```

Không chỉ nhìn số xe. Một doanh nghiệp bán ít xe hơn nhưng chuyển cơ cấu sang SUV hoặc xe cao cấp vẫn có thể tăng biên lợi nhuận. Ngược lại, sản lượng tăng nhờ ưu đãi bán hàng lớn có thể làm biên lợi nhuận giảm.

Các biến cần theo dõi gồm sản lượng toàn cầu, ASP/cơ cấu, ưu đãi, tỷ lệ sử dụng nhà máy, nguyên vật liệu, tỷ giá, bảo hành/triệu hồi, tổn thất tín dụng của công ty tài chính và CAPEX cho chuyển đổi EV.

Một bài kiểm tra sức chịu đựng có thể giả định sản lượng giảm 10%, ưu đãi tăng tương đương 2% ASP, KRW mạnh lên 8% và chi phí bảo hành tăng 30%, rồi lần theo tác động đến biên hoạt động, tiền mặt và công ty tài chính. Xem [ô tô và pin](./15_automotive_battery_mobility.md).

## 7. Mẫu C — Nền tảng số / Internet

Không nên chỉ nhìn số người dùng hoạt động hằng tháng (MAU). Chuỗi kinh tế phù hợp hơn là:

```text
Người dùng
× mức độ tương tác
× giao dịch hoặc lượng quảng cáo có thể bán
× tỷ lệ kiếm tiền
= Doanh thu
- chi phí thu hút lưu lượng
- nội dung / hoàn tất đơn hàng / thanh toán / đám mây
- R&D / bán hàng
= Lợi nhuận hoạt động
```

Cần phân biệt tăng trưởng người dùng với tăng khả năng kiếm tiền; xem tỷ lệ giữ chân; đánh giá việc tăng tỷ lệ thu phí có làm người bán hoặc người dùng phản ứng không; xác định hiệu ứng mạng lưới có thật hay người dùng dễ dùng nhiều nền tảng cùng lúc; và xem các mảng mới đang được trợ cấp bởi cỗ máy tạo tiền cốt lõi trong bao lâu.

Một dấu hiệu cảnh báo là doanh thu tăng cao nhưng chi phí marketing phải tăng nhanh hơn chỉ để giữ tốc độ tăng trưởng. Đó có thể là **tăng trưởng mua bằng tiền (paid growth)** chứ chưa phải hiệu ứng mạng lưới mạnh hơn. Xem [nền tảng và dịch vụ](./17_platform_telecom_content_retail_services.md).

## 8. Mẫu D — SI/SM và CNTT doanh nghiệp

Đây là mô hình đặc biệt quan trọng trong hệ sinh thái doanh nghiệp Hàn Quốc. Một công ty SI/SM thường có hỗn hợp gồm tích hợp hệ thống (SI), vận hành/bảo trì hệ thống (SM), đám mây và dịch vụ quản lý, cùng các dự án phần mềm, dữ liệu hoặc AI.

Với dự án tính theo nguồn lực:

\[
Doanh\ thu \approx Nhân\ lực\ có\ thể\ tính\ phí \times Tỷ\ lệ\ sử\ dụng \times Đơn\ giá
\]

Một số hợp đồng lại có giá cố định theo mốc bàn giao. SM/bảo trì thường có phần doanh thu lặp lại ổn định hơn.

Cần theo dõi tỷ lệ nhu cầu nội bộ tập đoàn, tỷ lệ khách hàng bên ngoài, tỷ lệ sử dụng lập trình viên, tỷ lệ thầu phụ, hợp đồng giá cố định so với tính theo thời gian–nguồn lực, đơn hàng tồn đọng, tài sản hợp đồng, lạm phát chi phí nhân sự, cơ cấu chuyển sang cloud và đóng góp của phần mềm/IP có biên cao.

Bẫy lớn là dự án giá cố định. Nếu dự án dự kiến doanh thu 100 và chi phí 85 thì lợi nhuận là 15. Nhưng nếu phạm vi công việc tăng khiến chi phí lên 105, kinh tế của cả dự án đổi dấu. Vì vậy cần đọc tài sản hợp đồng, dự phòng, lao động thuê ngoài và dự phòng lỗ dự án.

Nếu phân tích để chọn nơi làm việc, cần thêm các câu hỏi về phát triển cốt lõi hay điều phối, dự án nội bộ hay khách hàng ngoài, SI xây mới hay SM bảo trì, công nghệ hiện đại hay legacy, tầng thầu phụ, quyền ra quyết định và hệ thống đánh giá/thăng tiến. Xem [dịch vụ CNTT](./34_digital_fintech_cloud_and_it_services.md), [lao động](./12_labor_titles_compensation_and_workplace.md) và [văn hóa doanh nghiệp](./13_business_culture_decision_making_and_communication.md).

## 9. Mẫu E — Nhà cung cấp SME

Một nhà cung cấp SME Hàn Quốc có thể có lợi nhuận kế toán nhưng quyền thương lượng thấp.

```text
Sản lượng của khách hàng
× giá trị linh kiện trên mỗi đơn vị
× giá bán
= doanh thu
- nguyên vật liệu
- lao động
- khấu hao
= lợi nhuận hoạt động
± điều khoản thanh toán
= dòng tiền
```

Cần hỏi tỷ trọng doanh thu từ khách hàng lớn nhất, khả năng thay thế nhà cung cấp, áp lực giảm giá hằng năm, cơ chế chuyển giá nguyên liệu, gánh nặng khuôn/CAPEX, thời hạn thanh toán, quyền sở hữu công nghệ và rủi ro khách hàng chuyển nhà máy sang nước khác.

Một insight quan trọng: doanh thu tăng có thể tốt nhưng nhu cầu vốn lưu động tăng nhanh hơn nếu khách hàng thanh toán chậm. **Tăng trưởng có thể tiêu thụ tiền mặt.** Xem [SME và hệ sinh thái thầu phụ](./06_sme_mid_sized_and_subcontracting_ecosystem.md).

## 10. Mẫu F — Xây dựng và PF

Cần tách biên lợi nhuận xây dựng cốt lõi khỏi rủi ro PF có điều kiện.

```text
Đơn hàng
→ đơn hàng tồn đọng
→ tiến độ xây dựng
→ ghi nhận doanh thu
→ tài sản hợp đồng / khoản phải thu
→ thu tiền
```

Song song là chuỗi tài trợ:

```text
Chủ đầu tư / SPV
→ bảo lãnh hoặc hỗ trợ tín dụng
→ tái cấp vốn
→ bán trước
```

Một sổ đơn hàng khỏe không xóa được rủi ro bảo lãnh. Kịch bản xấu có thể gồm bán trước chậm, chi phí dự án tăng 15%, chênh lệch lãi suất tái cấp vốn tăng 300 điểm cơ bản, chậm hoàn thành sáu tháng và bảo lãnh trở thành nghĩa vụ thực tế. Xem [xây dựng và PF](./18_construction_real_estate_and_project_finance.md).

## 11. Mẫu G — Doanh nghiệp tài chính

Không nên dùng dòng tiền tự do kiểu doanh nghiệp công nghiệp cho ngân hàng hoặc bảo hiểm.

Với ngân hàng:

```text
Nền khoản vay / tiền gửi
× NIM
- chi phí vận hành
- tổn thất tín dụng
= lợi nhuận
```

Với công ty chứng khoán, cần nhìn phí môi giới, phí ngân hàng đầu tư, kết quả giao dịch/cấu trúc sản phẩm, chi phí vốn và tổn thất tín dụng. Với bảo hiểm, cần tách kết quả dịch vụ bảo hiểm và kết quả đầu tư. Luôn đọc lợi nhuận cùng mức đủ vốn. Xem [khu vực tài chính ngoài ngân hàng](./35_financial_sector_securities_insurance_asset_management.md).

## 12. Lập bảng tài chính 5 năm

Thay vì đọc từng báo cáo năm riêng lẻ, tạo một bảng:

| Chỉ tiêu | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Doanh thu | | | | | |
| Lợi nhuận hoạt động | | | | | |
| Biên hoạt động | | | | | |
| Lợi nhuận ròng | | | | | |
| CFO | | | | | |
| CAPEX | | | | | |
| FCF | | | | | |
| Nợ | | | | | |
| Tiền mặt | | | | | |
| Số cổ phiếu | | | | | |

Đánh dấu các sự kiện như mua lại, chia tách, mở nhà máy, khủng hoảng hoặc mất/giành khách hàng lớn. Mô hình nhiều năm quan trọng hơn một ảnh chụp tại một thời điểm.

## 13. Dựng cây động lực

Mỗi doanh nghiệp nên có một **cây động lực (driver tree)**:

```text
Lợi nhuận hoạt động
├─ Doanh thu
│  ├─ Sản lượng
│  └─ Giá / cơ cấu
└─ Chi phí
   ├─ Chi phí biến đổi
   ├─ Lao động
   ├─ Khấu hao
   └─ Chi phí cố định khác
```

Sau đó nối biến kinh tế vĩ mô vào đúng nhánh: KRW tác động giá xuất khẩu/biên lợi nhuận; lãi suất tác động chi phí lãi và nhu cầu; dầu tác động logistics/nguyên liệu; nhu cầu Trung Quốc tác động sản lượng. Đây là cầu nối với [cơ chế truyền dẫn vĩ mô](./21_economy_to_company_transmission.md).

## 14. Xây ba kịch bản xấu–cơ sở–tốt

Kịch bản không nhằm dự báo chính xác tuyệt đối mà để kiểm tra doanh nghiệp phụ thuộc vào biến nào.

| Động lực | Xấu | Cơ sở | Tốt |
|---|---:|---:|---:|
| Sản lượng | -10% | +3% | +10% |
| Giá | -8% | 0% | +5% |
| Biên lợi nhuận | 5% | 8% | 11% |
| CAPEX | cao | bình thường | kiểm soát tốt |

Khi chạy kịch bản, theo dõi FCF, nợ và định giá. Không nên tạo kịch bản xấu bằng cách cho mọi thứ cùng giảm 50%. Một kịch bản tốt phải có **tính nhất quán nhân quả (causal coherence)**.

Ví dụ khi bán dẫn suy giảm, ASP và tỷ lệ sử dụng công suất có thể giảm; sau một độ trễ, doanh nghiệp cũng có thể cắt CAPEX. Các biến phải kể được cùng một câu chuyện kinh tế.

## 15. Dùng bảng độ nhạy thay vì một giá mục tiêu duy nhất

Nếu định giá phụ thuộc mạnh vào tăng trưởng và biên lợi nhuận, tạo ma trận:

```text
                 Biên lợi nhuận
Tăng trưởng      6%     8%     10%
1%               ...    ...    ...
3%               ...    ...    ...
5%               ...    ...    ...
```

Mục tiêu là biết giả định nào chi phối giá trị mạnh nhất.

## 16. Đọc ngược kỳ vọng của thị trường

Thay vì chỉ dự báo, hãy hỏi mức định giá hiện tại đang ngầm giả định điều gì. Nếu vốn hóa thị trường chỉ hợp lý khi biên lợi nhuận tăng từ 5% lên 12% trong ba năm, cần tìm bằng chứng doanh nghiệp thực sự có con đường tới 12%.

Đây là **định giá ngược (reverse valuation / 역산 가치평가)**.

## 17. Kiến trúc của một giả thuyết tốt

Một giả thuyết nghiên cứu nên có cấu trúc:

```text
Quan sát
→ Cơ chế
→ Bằng chứng
→ Tác động tài chính
→ Điều thị trường có thể đang bỏ sót
→ Chất xúc tác / thời gian
→ Điều kiện bác bỏ giả thuyết
```

Không nên viết “công ty tốt vì AI tăng trưởng”. Cách tốt hơn là: nhu cầu AI làm tăng lượng HBM; nếu yield và công suất tăng đúng kế hoạch, cơ cấu sản phẩm sẽ nâng ASP và biên lợi nhuận; giả thuyết sai nếu chứng nhận sản phẩm bị chậm hoặc nguồn cung đối thủ tăng nhanh hơn nhu cầu.

## 18. Gắn nhãn bằng chứng

Mỗi ghi chú nên phân biệt:

- **F — Sự thật (Fact):** báo cáo đã kiểm toán hoặc hồ sơ pháp lý.
- **M — Tuyên bố của quản lý (Management Claim):** IR hoặc cuộc gọi kết quả kinh doanh.
- **I — Suy luận (Inference):** lập luận của người phân tích.
- **E — Bằng chứng bên ngoài (External Evidence):** dữ liệu ngành, chính phủ hoặc bên thứ ba.

Ví dụ:

```text
[F] CAPEX = 5 nghìn tỷ KRW
[M] Ban quản lý kỳ vọng dây chuyền mới cải thiện năng lực cạnh tranh
[I] Nếu tỷ lệ sử dụng dưới 60%, ROIC dự án có thể thấp hơn mục tiêu
```

Cách gắn nhãn này giúp tránh biến câu chuyện của ban quản lý thành sự thật đã được chứng minh.

## 19. Lập nhật ký nguồn

| Ngày | Nguồn | Dùng để chứng minh điều gì | Độ tin cậy |
|---|---|---|---|
| | Báo cáo năm DART | lịch đáo hạn nợ | Cao |
| | Tài liệu IR | mục tiêu của ban quản lý | Trung bình |
| | Nguồn ngành | tăng trưởng thị trường | Trung bình |

Nếu một kết luận quan trọng dựa trên nguồn yếu, đó là khoảng trống nghiên cứu cần bổ sung.

## 20. Đọc DART theo câu hỏi, không đọc như tiểu thuyết

Một thứ tự hiệu quả thường là:

```text
1. Tổng quan công ty và phân khúc
2. Báo cáo tài chính hợp nhất
3. Báo cáo lưu chuyển tiền tệ
4. Thuyết minh phân khúc
5. Nợ và lịch đáo hạn
6. Bên liên quan
7. Cam kết và bảo lãnh
8. Hợp đồng lớn / CAPEX
9. Cổ đông và quyền kiểm soát
10. Kiểm toán / điều chỉnh số liệu
```

Sau đó quay lại chính sách kế toán ở đúng nơi cần thiết. Không cần ghi nhớ mọi thuyết minh. Nếu CFO yếu, mở khoản phải thu, tồn kho và tài sản hợp đồng. Nếu nợ cao, mở lịch đáo hạn, điều khoản nợ và bảo lãnh.

## 21. Kết quả cuối cùng nên là một mô hình có thể bác bỏ

Một nghiên cứu tốt không kết thúc bằng “tôi thích công ty này”. Nó phải có dạng:

```text
Nếu A xảy ra
→ động lực B thay đổi
→ lợi nhuận / dòng tiền C thay đổi
→ bảng cân đối hoặc định giá D thay đổi.

Nếu bằng chứng E không xuất hiện trong khoảng thời gian T
→ giả thuyết phải được sửa hoặc bỏ.
```

## Mental Model — Mô hình tư duy

> Workbook này không dạy cách điền đủ mọi ô. Nó dạy cách biến một doanh nghiệp thành một **cỗ máy kinh tế có thể quan sát được**: nhu cầu đi vào đâu, doanh thu hình thành thế nào, chi phí và vốn bị tiêu ở đâu, lợi nhuận có chuyển thành tiền hay không, ai kiểm soát quyết định và điều gì có thể làm cỗ máy đó hỏng.

Khi đã dựng được mô hình đó, các chỉ số như P/E, ROE, FCF hay NIM không còn là những con số rời rạc; chúng trở thành kết quả của một cơ chế mà người đọc có thể giải thích và kiểm chứng.
