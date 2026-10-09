# SK hynix trường hợp (case / 사례) Lab — HBM, chu kỳ bộ nhớ và kinh tế của phân bổ công suất

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **SK hynix trường hợp (case / 사례) Lab — HBM, chu kỳ bộ nhớ và kinh tế của phân bổ công suất**. Route đi từ AI memory demand → HBM architecture và pricing → capacity allocation, yield và capex → DRAM/NAND cycle và normalization → customer concentration, cash flow và geopolitical risk.

SK hynix là một trường hợp phù hợp để học cách một công ty vẫn thuộc ngành bán dẫn bộ nhớ nhưng cơ cấu kinh tế có thể thay đổi mạnh khi hạ tầng AI làm HBM trở nên quan trọng hơn. Phân tích tốt phải tránh hai cực: coi bộ nhớ hoàn toàn là hàng hóa chu kỳ kiểu cũ, hoặc coi HBM là một mảng kinh doanh miễn nhiễm với chu kỳ.

SK hynix bán DRAM, NAND và các giải pháp bộ nhớ liên quan. Năm tài chính 2025 là một ảnh chụp đặc biệt mạnh: công ty công bố doanh thu khoảng 97,1 nghìn tỷ KRW và lợi nhuận hoạt động khoảng 47,2 nghìn tỷ KRW, với HBM và bộ nhớ AI giá trị cao là động lực quan trọng. Chính vì lợi nhuận ở mức rất cao, trường hợp (case / 사례) này đặc biệt hữu ích để học **chuẩn hóa lợi nhuận (normalization)**: lợi nhuận ở đỉnh chu kỳ hiện tại không được tự động kéo dài vô hạn sang tương lai.

## 1. Bắt đầu từ cấu trúc nhu cầu, không bắt đầu từ mã cổ phiếu

Nhu cầu bộ nhớ là **nhu cầu dẫn xuất (derived demand)**. Người dùng không mua DRAM chỉ vì muốn sở hữu DRAM; bộ nhớ được kéo bởi máy chủ, bộ tăng tốc AI, PC, điện thoại, hệ thống lưu trữ và nhiều hệ thống tính toán khác.

Với hạ tầng AI, chuỗi truyền dẫn có thể viết như sau:

```text
Khối lượng công việc AI
→ triển khai bộ tăng tốc / năng lực tính toán
→ nhu cầu băng thông bộ nhớ
→ lượng HBM trên mỗi bộ tăng tốc / hệ thống
→ nhu cầu HBM
→ nhu cầu wafer + công suất đóng gói
→ sản lượng bán / ASP / cơ cấu sản phẩm
→ doanh thu và biên lợi nhuận
```

Mỗi mũi tên đều có thể bị đứt. Tăng trưởng mô hình AI không tự động chuyển 1:1 thành doanh thu SK hynix nếu quá trình chứng nhận khách hàng, công suất đóng gói hoặc nguồn cung cạnh tranh thay đổi.

> **Tiếp theo:** Sau khi xác định cấu trúc nhu cầu thay vì bắt đầu từ mã cổ phiếu, phần **2. HBM không chỉ là “DRAM đắt hơn”** giải thích khác biệt kinh tế của sản phẩm. **3. Cây động lực của doanh nghiệp bộ nhớ** nối khác biệt đó với các biến vận hành.

## 2. HBM không chỉ là “DRAM đắt hơn”

HBM tạo **khác biệt kinh tế (economic differentiation)** nhờ băng thông, xếp chồng nhiều lớp chip, đóng gói tiên tiến, giới hạn nhiệt–điện, tỷ lệ thành phẩm và yêu cầu chứng nhận khách hàng. Vì sản phẩm phức tạp hơn, khả năng giữ lại giá trị có thể cao hơn DRAM thông thường trong một giai đoạn.

Khi phân tích cần hỏi bốn câu. Thứ nhất, bao nhiêu công suất wafer và đóng gói có thể chuyển sang HBM? Thứ hai, tỷ lệ thành phẩm (yield) thực tế trên đầu vào wafer và ngăn xếp (stack / 스택) là bao nhiêu? Thứ ba, khách hàng đã chứng nhận sản phẩm ở thế hệ nào? Thứ tư, HBM tăng có làm giảm lượng công suất dành cho DRAM thông thường và từ đó ảnh hưởng giá toàn ngành hay không?

Điểm cuối đặc biệt quan trọng. Phân bổ công suất cho HBM tạo **chi phí cơ hội (opportunity cost)** đối với DRAM thông thường.

> **Tiếp theo:** **3. Cây động lực của doanh nghiệp bộ nhớ** cho thấy nhu cầu, yield, ASP và công suất liên kết với nhau ra sao. Phần **4. Phân bổ công suất** đưa mối liên kết ấy vào quyết định vốn ở cấp fab.

## 3. Cây động lực của doanh nghiệp bộ nhớ

Một mô hình đơn giản:

\[
Revenue = \sum_i BitShipment_i \times ASP_i
\]

Trong đó `i` có thể là HBM, DRAM máy chủ, DRAM di động, NAND/eSSD và các nhóm sản phẩm khác.

Chi phí không chỉ gồm nguyên vật liệu. Một nhà sản xuất bán dẫn còn phải gánh:

```text
chi phí wafer / quy trình
+ khấu hao
+ đóng gói và kiểm thử
+ tổn thất do yield thấp
+ kỹ thuật / R&D
+ điện và tiện ích
```

Chi phí trên mỗi bit thường giảm nhờ chuyển sang tiến trình mới, tăng mật độ và cải thiện yield. Tuy nhiên ở giai đoạn chuyển đổi ban đầu, yield có thể thấp hoặc chi phí thiết bị–khấu hao tăng trước khi lợi thế chi phí xuất hiện.

> **Tiếp theo:** Quyết định công suất ở **4.** chỉ tạo giá trị nếu cơ cấu sản phẩm và chi phí cố định phù hợp. **5. Cơ cấu HBM và đòn bẩy hoạt động** kiểm tra chính điều kiện đó.

## 4. Phân bổ công suất là bài toán phân bổ vốn ở cấp fab

Giả sử một lượng công suất wafer có thể dùng cho sản phẩm A hoặc B. Công ty không chỉ hỏi sản phẩm nào có ASP cao hơn mà phải hỏi mức đóng góp sau khi tính yield, nút thắt đóng gói, chứng nhận khách hàng và giá trị quan hệ khách hàng dài hạn.

Ví dụ minh họa:

```text
DRAM thông thường:
Doanh thu tương đương / wafer = 100
Chi phí biến đổi + chuyển đổi = 60
Mức đóng góp = 40

HBM:
Doanh thu tiềm năng / wafer = 190
Chi phí quy trình / đóng gói / yield cao hơn = 105
Mức đóng góp = 85
```

Nếu HBM tạo mức đóng góp cao hơn thì chuyển wafer sang HBM có vẻ hợp lý. Nhưng nếu yield thực tế thấp làm chi phí tăng thêm 40, mức đóng góp chỉ còn 45. Vì vậy câu chuyện “HBM có giá bán cao” không thể thay thế năng lực thực thi sản xuất.

> **Tiếp theo:** **5. Cơ cấu HBM và đòn bẩy hoạt động** cho thấy cùng một công suất có thể tạo kết quả khác nhau theo yield và mix. **6. NAND và eSSD** mở rộng góc nhìn sang các mảng không nên bỏ qua khi đọc toàn bộ doanh nghiệp.

## 5. Cơ cấu HBM và đòn bẩy hoạt động

Khi tỷ trọng sản phẩm giá trị cao tăng, ASP bình quân và biên lợi nhuận có thể tăng nhanh hơn sản lượng bit. Điều này dễ khiến người phân tích kết luận rằng chu kỳ lịch sử đã biến mất.

Cần tách ba hiệu ứng:

```text
Hiệu ứng cấu trúc:
lượng bộ nhớ AI trên mỗi hệ thống tăng dài hạn

Hiệu ứng chu kỳ:
cung–cầu căng làm ASP và biên lợi nhuận tăng mạnh

Hiệu ứng thực thi:
công ty có yield hoặc khả năng chứng nhận tốt hơn đối thủ
```

Ba hiệu ứng cùng xuất hiện trong lợi nhuận nhưng ý nghĩa định giá khác nhau. Lợi thế cấu trúc có thể bền hơn; khan hiếm mang tính chu kỳ thường thu hút thêm công suất và cạnh tranh; lợi thế thực thi phải được chứng minh lại ở mỗi thế hệ sản phẩm mới.

> **Tiếp theo:** Sau khi đặt HBM cạnh NAND và eSSD, phần **7. CAPEX** hỏi khoản đầu tư đang mở rộng tăng trưởng hay chỉ duy trì năng lực hiện có.

## 6. NAND và eSSD không được bỏ qua

Khi thị trường tập trung câu chuyện vào HBM, NAND rất dễ bị xem như phần phụ. Tuy nhiên NAND vẫn ảnh hưởng tồn kho, mức sử dụng tài sản, dòng tiền và lợi nhuận hợp nhất.

Trung tâm dữ liệu AI cũng cần lưu trữ, nhưng kinh tế của NAND khác DRAM/HBM. Cần theo dõi cơ cấu SSD doanh nghiệp, chuyển đổi số lớp NAND, kỷ luật nguồn cung toàn ngành và mức tồn kho.

Một công ty có HBM rất mạnh vẫn có thể bị kéo giảm lợi nhuận nếu một phân khúc bộ nhớ khác rơi vào suy giảm sâu.

> **Tiếp theo:** **7. CAPEX** phân biệt đầu tư tăng trưởng với đầu tư duy trì. **8. Chuẩn hóa dòng tiền ở năm lợi nhuận cao** giúp tránh lấy một năm chu kỳ thuận lợi làm mức tiền mặt bền vững.

## 7. CAPEX: tăng trưởng hay duy trì năng lực?

Không phải toàn bộ chi tiêu vốn (CAPEX) đều tạo công suất mới. Một phần dùng cho chuyển đổi công nghệ, thay thế thiết bị, phòng sạch–hạ tầng và đóng gói.

Khi đọc công bố thông tin, nên tách:

```text
CAPEX duy trì / thay thế
CAPEX chuyển đổi công nghệ
CAPEX mở rộng công suất
CAPEX đóng gói tiên tiến
CAPEX địa lý chiến lược
```

Sau đó hỏi nguồn lợi nhuận kỳ vọng của từng nhóm. Một khoản đầu tư fab lớn có thể cần nhiều năm trước khi đạt tỷ lệ sử dụng công suất tối ưu, vì vậy mô hình phải có độ trễ giữa dòng tiền ra và phần lợi nhuận tạo ra sau đó.

> **Tiếp theo:** Khi CAPEX và dòng tiền đã được chuẩn hóa, **9. Ví dụ về chu kỳ** minh họa cách giá, utilization và công suất cùng đổi qua các pha.

## 8. Chuẩn hóa dòng tiền ở năm lợi nhuận cao

Khi biên lợi nhuận tăng mạnh, dòng tiền từ hoạt động kinh doanh (CFO) cũng có thể tăng rất nhanh. Nhưng doanh nghiệp bộ nhớ thường phải phân bổ dòng tiền giữa:

```text
CAPEX tương lai
+ củng cố bảng cân đối
+ trả nợ
+ cổ tức / mua lại / hủy cổ phiếu quỹ
+ đầu tư chiến lược
```

Năm 2025 của SK hynix là ví dụ hữu ích vì công ty đồng thời nói tới đầu tư tương lai, ổn định tài chính và hoàn vốn cho cổ đông. Câu hỏi phân tích không phải “trả tiền cho cổ đông hay đầu tư, cái nào tốt hơn”, mà là **lợi suất biên của từng cách sử dụng tiền mặt**.

Nếu công suất HBM tương lai tạo ROIC cao, đầu tư thiếu cũng có chi phí cơ hội. Nếu chu kỳ gần đỉnh và công suất được mở rộng quá mạnh, đầu tư quá mức có thể phá hủy giá trị.

> **Tiếp theo:** Ví dụ ở **9.** biến quy tắc chuẩn hóa dòng tiền thành một chuỗi diễn biến có thể kiểm tra. **10. Tập trung khách hàng và chứng nhận** bổ sung điều kiện thương mại quyết định doanh thu có lặp lại được hay không.

## 9. Ví dụ về chu kỳ

Giả sử doanh nghiệp có cơ cấu tổng hợp:

```text
Năm A:
Sản lượng bit = 100
ASP bình quân = 1,00
Chi phí/bit = 0,65

Năm B:
Sản lượng bit = 115
Tỷ trọng HBM ↑
ASP bình quân = 1,20
Chi phí/bit = 0,62
```

Doanh thu tăng từ `100` lên `138`. Mức đóng góp xấp xỉ tăng từ:

\[
100 \times (1.00 - 0.65) = 35
\]

thành:

\[
115 \times (1.20 - 0.62) = 66.7
\]

Doanh thu tăng 38% nhưng phần đóng góp gần gấp đôi. Đây là kết quả của **đòn bẩy hoạt động (operating leverage)** kết hợp với hiệu ứng cơ cấu sản phẩm.

Bây giờ thử một năm C căng thẳng:

```text
Sản lượng bit +10%
ASP -25%
Chi phí/bit -8%
```

Ngay cả khi khối lượng bán tiếp tục tăng, chênh lệch giá–chi phí vẫn có thể co rất mạnh. Vì vậy định giá phải kiểm tra độ nhạy với ASP và cơ cấu sản phẩm chứ không chỉ với tăng trưởng bit.

> **Tiếp theo:** **10. Tập trung khách hàng và chứng nhận** cho thấy tăng trưởng HBM có thể đi cùng phụ thuộc khách hàng và thời gian phê duyệt. **11. Tồn kho** dùng tín hiệu đó để đặt câu hỏi, không biến nó thành kết luận tự động.

## 10. Tập trung khách hàng và chứng nhận

HBM gắn chặt với lộ trình sản phẩm của các nền tảng và bộ tăng tốc AI. Việc chứng nhận chậm vài tháng có thể đẩy doanh thu sang quý hoặc thế hệ khác, đồng thời làm tồn kho và tỷ lệ sử dụng công suất lệch khỏi kỳ vọng.

Các câu hỏi cần đặt ra gồm: mức tập trung khách hàng là bao nhiêu, thế hệ sản phẩm nào đã được chứng nhận, cam kết sản lượng có tính ràng buộc hay chỉ là dự báo, nút thắt đóng gói nằm ở đâu, khách hàng có dùng hai nguồn cung hay không, và thế hệ tiếp theo có giữ được vị thế cạnh tranh hay không.

Không cần biết mọi chi tiết bí mật. Chỉ cần nhận ra rằng lộ trình khách hàng là một phần của kinh tế sản xuất.

> **Tiếp theo:** Tồn kho chỉ có ý nghĩa khi đặt cạnh đơn hàng, chứng nhận và vị trí trong chu kỳ. **12. Vĩ mô và địa chính trị** mở rộng phép kiểm tra sang nhu cầu toàn cầu và rủi ro chuỗi cung ứng.

## 11. Tồn kho là tín hiệu, không phải kết luận

Tồn kho tăng có thể là tín hiệu xấu nếu nhu cầu yếu và giá sắp giảm. Nhưng tồn kho tăng trước khi tăng sản lượng sản phẩm mới hoặc để đáp ứng nhu cầu đã cam kết lại có ý nghĩa khác.

Do đó nên đọc tam giác:

```text
Tăng tồn kho
so với tăng doanh thu
so với ASP / nhận định nhu cầu
```

Nếu tồn kho tăng nhanh hơn doanh thu trong khi ban lãnh đạo nói nhu cầu mạnh, cần kiểm tra cơ cấu sản phẩm, sản phẩm dở dang, thành phẩm và thời điểm chuyển đổi công nghệ trước khi kết luận.

> **Tiếp theo:** **12. Vĩ mô và địa chính trị** cho biết các cú sốc bên ngoài có thể truyền vào đơn hàng, giá và công suất như thế nào. **13. Phân tích kịch bản** biến các đường truyền đó thành những trường hợp để so sánh.

## 12. Vĩ mô và địa chính trị

Doanh nghiệp bộ nhớ chịu tác động của nhu cầu điện tử toàn cầu, CAPEX của hyperscaler, tỷ giá, chi tiêu công nghệ nhạy với lãi suất, kiểm soát xuất khẩu–thiết bị, chính sách địa điểm sản xuất và khả năng cung cấp năng lượng–hạ tầng.

Không nên biến địa chính trị thành khẩu hiệu. Hãy chuyển nó thành một trong năm kênh cụ thể:

```text
khả năng tiếp cận thị trường
khả năng tiếp cận khách hàng
khả năng tiếp cận thiết bị
địa điểm và chi phí sản xuất
CAPEX bắt buộc phải nhân đôi ở nhiều khu vực
```

Chỉ khi xác định được kênh truyền dẫn mới có thể đưa tác động vào mô hình tài chính.

> **Tiếp theo:** Các kịch bản ở **13.** tạo ra biên độ cho sản lượng, giá và vốn đầu tư. **14. Định giá ngược** dùng biên độ ấy để hỏi thị trường đang ngầm giả định điều gì.

## 13. Phân tích kịch bản

### Kịch bản tiêu cực (bear scenario)

Kịch bản tiêu cực kiểm tra rủi ro nhu cầu AI chậm lại, yield thấp hoặc công suất mới tạo dư cung. Mỗi yếu tố phải được nối tới ASP, margin, capex và cash flow.

```text
Tăng trưởng hạ tầng AI chậm lại
Nguồn cung HBM tăng nhanh
Mức premium của ASP HBM thu hẹp
ASP DRAM thông thường -20%
NAND phục hồi yếu
Cam kết CAPEX vẫn cao trong 12 tháng đầu
```

Chuỗi tác động:

```text
ASP bình quân ↓
→ biên lợi nhuận gộp ↓
→ CFO ↓
→ CAPEX/CFO ↑
→ FCF ↓
→ khả năng hoàn vốn cho cổ đông ↓
```

### Kịch bản lợi thế cấu trúc

Kịch bản này hỏi lợi thế HBM và năng lực đóng gói có đủ bền để vượt một chu kỳ hay không. Hãy phân biệt moat công nghệ với tailwind nhu cầu tạm thời.

```text
Lượng bộ nhớ AI trên mỗi hệ thống tiếp tục tăng
Chứng nhận thế hệ mới đúng lịch
Tỷ trọng HBM ↑
Yield cải thiện
Kỷ luật nguồn cung bộ nhớ thông thường được duy trì
```

Khi đó tăng trưởng lợi nhuận đến từ cả sản lượng, cơ cấu sản phẩm và chi phí. Tuy nhiên vẫn phải hỏi thị trường đã phản ánh bao nhiêu phần của kịch bản này vào giá cổ phiếu.

> **Tiếp theo:** **14. Định giá ngược** làm rõ mức tăng trưởng và biên lợi nhuận mà giá hiện tại đòi hỏi. **15. Những yếu tố có thể phá vỡ luận điểm đầu tư** kiểm tra xem các giả định đó dễ tổn thương ở đâu.

## 14. Định giá ngược (reverse valuation)

Thay vì hỏi “P/E bao nhiêu là hợp lý?”, hãy hỏi mức giá trị vốn chủ sở hữu hoặc giá trị doanh nghiệp hiện tại đòi hỏi mức lợi nhuận chuẩn hóa nào mới hợp lý.

Nếu định giá chỉ hợp lý khi biên lợi nhuận ở đỉnh hiện tại kéo dài nhiều năm, luận điểm phụ thuộc vào giả định rất mạnh. Nếu định giá vẫn hợp lý khi ASP và biên lợi nhuận giảm đáng kể về mức bình thường, cấu trúc rủi ro giảm giá sẽ khác.

Định giá ngược buộc người phân tích tách:

```text
lợi nhuận hiện tại
lợi nhuận chuẩn hóa
premium tăng trưởng cấu trúc
premium / discount theo chu kỳ
```

> **Tiếp theo:** Sau khi liệt kê các điểm dễ gãy ở **15.**, **16. Bài tập** yêu cầu người học tự kiểm tra luận điểm bằng chu kỳ, công suất, khách hàng và định giá.

## 15. Những yếu tố có thể phá vỡ luận điểm đầu tư

Một luận điểm tích cực có thể bị phá bởi thất bại chứng nhận, yield cải thiện chậm, đối thủ tăng công suất HBM nhanh, cú sốc tập trung khách hàng, dư cung toàn ngành hoặc lợi suất CAPEX thấp. Một luận điểm tiêu cực có thể bị phá bởi lượng bộ nhớ AI trên mỗi hệ thống tăng mạnh hơn dự kiến, hạn chế nguồn cung kéo dài, năng lực thực thi vượt trội hoặc chi phí giảm nhanh.

Trường hợp (case / 사례) này dạy một nguyên tắc quan trọng:

> **HBM có thể thay đổi hình dạng của chu kỳ bộ nhớ, nhưng không xóa kinh tế cơ bản của công suất, yield, giá, CAPEX và cạnh tranh.**

> **Tiếp theo:** Bài tập ở **16.** là điểm kiểm tra cuối của case. **Liên kết** dẫn tới các chương nền tảng để người học đối chiếu khái niệm và nguồn.

## 16. Bài tập

Tạo bảng năm năm gồm doanh thu, biên lợi nhuận hoạt động, CFO, CAPEX, tiền mặt/nợ ròng và tồn kho. Sau đó viết ba dòng cho mỗi năm theo ba lớp: `chu kỳ`, `cơ cấu sản phẩm`, `năng lực thực thi`. Mục tiêu là giải thích thay đổi lợi nhuận bằng ba lớp này thay vì chỉ sao chép nhận định của ban lãnh đạo.

> **Kết luận:** Hãy giữ lại chuỗi phân tích từ nhu cầu HBM, cơ cấu công suất và chu kỳ đến khách hàng, địa chính trị và định giá. **Liên kết** là điểm quay về khi cần kiểm tra từng mắt xích bằng tài liệu chuẩn.

## Liên kết

Đọc cùng [14_semiconductors_electronics_display](../14_semiconductors_electronics_display.md), [21_economy_to_company_transmission](../21_economy_to_company_transmission.md), [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md) và [39_practical_company_analysis_workbook_and_case_patterns](../39_practical_company_analysis_workbook_and_case_patterns.md).

> **Bàn giao:** Sau **Liên kết**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
