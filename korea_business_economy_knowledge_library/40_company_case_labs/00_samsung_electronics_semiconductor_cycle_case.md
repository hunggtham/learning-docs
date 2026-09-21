# Samsung Electronics — từ công ty hợp nhất đến từng cỗ máy kinh tế

Samsung Electronics là bài thực hành rất tốt để học một lỗi phổ biến trong phân tích doanh nghiệp: **một pháp nhân có thể chứa nhiều mảng kinh doanh có hàm sản xuất hoàn toàn khác nhau**. Nếu chỉ nhìn doanh thu hợp nhất, lợi nhuận hoạt động và P/E, người đọc dễ bỏ qua việc bán dẫn, điện thoại, màn hình và điện tử ô tô phản ứng với chu kỳ theo những cách khác nhau.

Theo cấu trúc công bố của Samsung Electronics, công ty có các mảng lớn như DX (Device eXperience), DS (Device Solutions), SDC và Harman. DX gồm nhiều sản phẩm hoàn chỉnh như điện thoại, TV và đồ gia dụng; DS gồm Memory, Foundry và System LSI.

Vì vậy câu “lợi nhuận Samsung tăng” chưa phải lời giải thích. Câu hỏi đúng là: **cỗ máy nào tạo ra thay đổi, nó đang ở pha nào của chu kỳ và dòng tiền còn bền sau CAPEX hay không?**

Số liệu FY2025 chỉ nên dùng như ảnh chụp lịch sử để luyện phân tích, không được biến thành giả định mặc định cho năm sau.

## 1. Xác định đúng pháp nhân trước khi lập mô hình

“Samsung” là tên tập đoàn, còn bài này phân tích **Samsung Electronics Co., Ltd.** Samsung Electronics hợp nhất nhiều công ty con, nhưng không có nghĩa mọi công ty mang thương hiệu Samsung đều nằm trong phạm vi báo cáo của Samsung Electronics.

Trên DART, bước đầu phải kiểm tra tên pháp nhân, công ty con hợp nhất và thuyết minh phân khúc. Nếu nhầm ranh giới tập đoàn với ranh giới kế toán, người phân tích có thể gán tài sản, nợ hoặc lợi nhuận của pháp nhân khác cho Samsung Electronics.

```text
Samsung Group
   ├─ Samsung Electronics ← pháp nhân đang phân tích
   │    ├─ DX
   │    ├─ DS
   │    ├─ SDC
   │    └─ Harman
   └─ các công ty liên kết độc lập khác
```

## 2. Không có một “biên lợi nhuận Samsung” duy nhất

DX và DS khác nhau từ gốc. DX bán sản phẩm hoàn chỉnh. Kinh tế điện thoại chịu ảnh hưởng của số máy bán, cơ cấu sản phẩm, chi phí linh kiện, marketing, tồn kho kênh phân phối và chu kỳ thay máy.

DS bán dẫn lại có **cường độ chi phí cố định (fixed-cost intensity)** rất cao. Fab vẫn phải gánh khấu hao và chi phí kỹ thuật ngay cả khi tỷ lệ sử dụng công suất thấp.

Với DX có thể bắt đầu từ:

\[
Doanh\ thu_{DX} \approx Số\ lượng\ bán \times ASP
\]

Lợi nhuận sau đó phụ thuộc chi phí linh kiện, sản xuất, marketing, R&D và SG&A.

Với bán dẫn, cần mô hình khác:

```text
Nhu cầu bit
→ lượng bit xuất bán
× ASP
→ doanh thu
- chi phí sản xuất
- khấu hao lớn
→ lợi nhuận hoạt động
```

Do đó cùng mức doanh thu giảm 10% có thể tạo tác động lợi nhuận rất khác giữa điện thoại và bộ nhớ.

## 3. Bộ nhớ: giá, lượng bit và chi phí mỗi bit

Một cách đơn giản để đọc bộ nhớ:

\[
Doanh\ thu \approx Lượng\ bit\ xuất\ bán \times Giá\ bán\ mỗi\ bit
\]

Lợi nhuận phụ thuộc thêm chi phí mỗi bit. Khi công nghệ quy trình tốt hơn, yield tăng và mật độ chip cao hơn, chi phí mỗi bit có thể giảm.

Nhưng giá bán bộ nhớ có tính chu kỳ mạnh. Nếu toàn ngành tăng công suất quá nhanh, nguồn cung vượt nhu cầu và ASP giảm. Vì khấu hao fab vẫn tồn tại, lợi nhuận có thể giảm nhanh hơn doanh thu.

Đây là **đòn bẩy hoạt động (operating leverage)**.

```text
ASP ↑ + tỷ lệ sử dụng ↑
→ biên lợi nhuận tăng rất nhanh

ASP ↓ + tỷ lệ sử dụng ↓
→ khấu hao phân bổ trên ít sản lượng hơn
→ biên lợi nhuận giảm rất nhanh
```

## 4. HBM làm cơ cấu bộ nhớ khác trước

HBM không nên được đọc đơn giản như “DRAM giá cao hơn”. Nó yêu cầu xếp chồng chip, đóng gói phức tạp, kiểm soát nhiệt, yield tốt và quá trình chứng nhận với khách hàng AI.

Vì vậy cần hỏi:

- tỷ trọng HBM trong cơ cấu sản phẩm tăng bao nhiêu;
- yield và năng lực đóng gói thế nào;
- khách hàng đã chứng nhận sản phẩm chưa;
- công suất wafer được chuyển từ DRAM truyền thống sang HBM ra sao;
- ASP cao hơn có bù được chi phí và độ phức tạp cao hơn không.

HBM có thể nâng giá trị mỗi wafer nhưng cũng tạo **chi phí cơ hội công suất**: wafer dùng cho HBM không thể đồng thời dùng cho sản phẩm khác.

## 5. Foundry: không thể chỉ nhìn công suất danh nghĩa

Foundry có chi phí cố định rất cao nhưng khác bộ nhớ ở chỗ sản phẩm được sản xuất theo thiết kế của khách hàng. Công suất danh nghĩa không có nhiều ý nghĩa nếu khách hàng không đặt đủ wafer hoặc yield thấp.

Một mô hình đơn giản:

```text
Công suất danh nghĩa
× tỷ lệ sử dụng
× yield kinh tế
× giá mỗi wafer
→ doanh thu có chất lượng
```

Nếu công suất tăng nhưng tỷ lệ sử dụng thấp, khấu hao trên mỗi wafer tăng. Nếu yield thấp, doanh nghiệp tiêu cùng lượng vật liệu và thời gian máy nhưng thu được ít chip đạt chuẩn hơn.

Vì vậy cần phân biệt “đã xây fab” với “fab đang tạo lợi nhuận”.

## 6. System LSI: thiết kế chip có kinh tế khác foundry

System LSI tập trung nhiều hơn vào thiết kế và sản phẩm logic. Cơ chế giá trị nằm ở IP, kiến trúc chip, khả năng tích hợp và nhu cầu sản phẩm cuối.

Một doanh nghiệp có thể có foundry mạnh nhưng thiết kế sản phẩm yếu, hoặc ngược lại. Không nên gộp tất cả “semiconductor” thành một khối.

## 7. DX: điện thoại không chỉ là số lượng máy

Với smartphone, doanh thu phụ thuộc số máy bán và ASP, nhưng lợi nhuận còn phụ thuộc cơ cấu giữa flagship và tầm trung, chi phí bộ nhớ/màn hình/chip, marketing và mức tồn kho tại kênh bán.

```text
Số máy bán
× ASP
= doanh thu
- linh kiện
- sản xuất
- marketing
- R&D
- SG&A
= lợi nhuận hoạt động
```

Một năm số máy không tăng nhưng tỷ trọng flagship cao hơn vẫn có thể cải thiện lợi nhuận. Ngược lại, tăng sản lượng bằng khuyến mại mạnh có thể làm doanh thu tăng nhưng biên giảm.

## 8. Tích hợp dọc tạo cả lợi thế và xung đột kinh tế

Samsung Electronics có nhiều năng lực nội bộ về bộ nhớ, màn hình và linh kiện. Tích hợp dọc có thể giúp phối hợp sản phẩm, bảo đảm nguồn cung và học công nghệ nhanh.

Nhưng không nên mặc định “tự cung cấp linh kiện luôn tốt”. Nếu linh kiện nội bộ đắt hơn hoặc kém cạnh tranh hơn nguồn ngoài, việc ưu tiên nội bộ có thể làm giảm hiệu quả kinh tế.

Do đó cần phân biệt **lợi ích chiến lược của tích hợp** với **hiệu quả tài chính của từng giao dịch**.

## 9. SDC và Harman: hai cỗ máy khác nữa

Samsung Display chịu chu kỳ màn hình, công nghệ OLED, công suất và khách hàng lớn. Harman lại liên quan điện tử ô tô, âm thanh và hệ thống kết nối, với chu kỳ hợp đồng dài hơn smartphone.

Điều này làm Samsung Electronics giống một danh mục nhiều doanh nghiệp hơn là một công ty đơn ngành.

Khi phân tích hợp nhất, nên hỏi mỗi mảng đóng góp bao nhiêu vào doanh thu, lợi nhuận, CAPEX và biến động chu kỳ.

## 10. CAPEX: chi tiền hôm nay để giữ quyền cạnh tranh ngày mai

Bán dẫn cần CAPEX rất lớn. Nhưng CAPEX không phải chi phí được ghi hết ngay vào báo cáo kết quả kinh doanh. Tiền mặt ra trước, sau đó tài sản được khấu hao qua nhiều năm.

```text
CAPEX hôm nay
→ tài sản cố định tăng
→ khấu hao các năm sau tăng
→ công suất tương lai tăng
```

Vì vậy một năm lợi nhuận tốt chưa chắc dòng tiền tự do cao nếu doanh nghiệp đang đầu tư cực lớn.

Cần đọc cùng lúc:

```text
Lợi nhuận hoạt động
→ CFO
→ CAPEX
→ FCF
```

## 11. Khấu hao làm chu kỳ bán dẫn khó đọc

Khi fab mới đi vào hoạt động, khấu hao tăng ngay cả khi tỷ lệ sử dụng chưa đạt mức tối ưu. Điều này có thể làm lợi nhuận ngắn hạn xấu trước khi công suất mới tạo doanh thu đầy đủ.

Ngược lại, khi fab cũ đã khấu hao nhiều, chi phí kế toán có thể thấp hơn nhưng tài sản lại gần thời điểm cần nâng cấp.

Do đó không nên đánh giá bán dẫn chỉ bằng EBITDA hoặc lợi nhuận một năm. Phải nhìn tuổi tài sản, CAPEX và thế hệ công nghệ.

## 12. Tồn kho: tín hiệu quan trọng của chu kỳ

Tồn kho bộ nhớ tăng nhanh có thể cho thấy sản xuất vượt nhu cầu. Nhưng tồn kho tăng cũng có thể do doanh nghiệp chuẩn bị cho sản phẩm mới hoặc thay đổi chuỗi cung ứng.

Cần đọc tồn kho cùng ASP, sản lượng, tỷ lệ sử dụng và hướng dẫn của ban quản lý.

```text
Nhu cầu yếu
→ tồn kho tăng
→ cắt sản xuất
→ nguồn cung tương lai giảm
→ giá có thể ổn định sau độ trễ
```

Đây là một trong những cơ chế tự điều chỉnh của chu kỳ bộ nhớ.

## 13. Tiền mặt lớn không có nghĩa vốn nhàn rỗi hoàn toàn

Samsung Electronics thường có lượng tiền và tài sản tài chính lớn. Nhưng một phần tiền cần để tài trợ CAPEX, vốn lưu động, R&D, M&A và chống chịu chu kỳ.

Khi đánh giá phân bổ vốn, cần hỏi:

- tiền mặt tối thiểu cần cho vận hành là bao nhiêu;
- CAPEX duy trì và CAPEX tăng trưởng khác nhau thế nào;
- cổ tức/mua lại cổ phiếu có bền không;
- doanh nghiệp có đang giữ quá nhiều tiền với lợi suất thấp không;
- M&A có tạo ROIC tốt hơn hoàn vốn cho cổ đông không.

## 14. Tỷ giá: doanh thu toàn cầu và chi phí toàn cầu

Samsung bán sản phẩm toàn cầu và cũng mua nhiều đầu vào bằng ngoại tệ. KRW yếu có thể nâng doanh thu quy đổi nhưng cũng làm một số chi phí nhập khẩu tăng.

Không nên dùng câu “won yếu tốt cho Samsung” mà không phân tích phơi nhiễm ròng.

Cần xem doanh thu theo khu vực, địa điểm sản xuất, đồng tiền chi phí và chính sách phòng hộ.

## 15. Chu kỳ điện thoại và chu kỳ bộ nhớ có thể không đồng pha

Điện thoại có thể yếu trong khi HBM mạnh. Bộ nhớ truyền thống có thể giảm giá trong khi màn hình OLED cải thiện. Harman có thể hưởng đơn hàng ô tô dài hạn trong lúc smartphone chậm.

Đây là lý do lợi nhuận hợp nhất có thể che nhiều chu kỳ đối nghịch.

Một mô hình tốt nên tách ít nhất:

```text
DX
DS - Memory
DS - Foundry / System LSI
SDC
Harman
```

## 16. Từ DART đến mô hình phân tích

Khi mở DART hoặc báo cáo năm, không nên đọc từ trang đầu đến cuối. Hãy tìm theo câu hỏi:

1. Phạm vi hợp nhất gồm những công ty nào?
2. Phân khúc được công bố thế nào?
3. Mảng nào tạo phần lớn lợi nhuận?
4. CAPEX tập trung ở đâu?
5. Tồn kho và khoản phải thu thay đổi ra sao?
6. Dòng tiền hoạt động có theo lợi nhuận không?
7. Các cam kết đầu tư lớn là gì?
8. Giao dịch bên liên quan có đáng kể không?

Sau đó mới quay lại thuyết minh chi tiết.

## 17. Kịch bản chu kỳ bộ nhớ

Một bài tập đơn giản:

### Kịch bản xấu

```text
ASP bộ nhớ giảm mạnh
+ tỷ lệ sử dụng công suất giảm
+ HBM tăng chậm hơn kỳ vọng
→ biên DS giảm
→ CFO giảm
→ CAPEX vẫn cao
→ FCF chịu áp lực
```

### Kịch bản cơ sở

```text
ASP ổn định
+ lượng bit tăng vừa phải
+ cơ cấu HBM cải thiện
→ biên lợi nhuận phục hồi
→ CFO đủ tài trợ phần lớn CAPEX
```

### Kịch bản tốt

```text
Nhu cầu AI mạnh
+ HBM được chứng nhận nhanh
+ yield cải thiện
+ bộ nhớ truyền thống không dư cung
→ ASP và cơ cấu cùng tốt
→ lợi nhuận tăng nhanh hơn doanh thu
```

Mục tiêu không phải đoán đúng con số mà là hiểu biến nào làm kết quả đổi hướng.

## 18. Định giá: không nên dùng một P/E cho mọi pha chu kỳ

P/E thấp ở đỉnh lợi nhuận bộ nhớ có thể là bẫy vì mẫu số đang ở mức bất thường cao. P/E cao ở đáy chu kỳ có thể không có nghĩa cổ phiếu đắt nếu lợi nhuận chuẩn hóa cao hơn nhiều.

Do đó cần ước lượng **lợi nhuận chuẩn hóa (normalized earnings)**, tách giá trị tiền mặt ròng và xem mỗi mảng có cơ chế khác nhau.

Một cách khác là định giá ngược: giá thị trường hiện tại đang ngầm giả định ASP, biên DS, tăng trưởng HBM và ROIC bao nhiêu?

## 19. Điều kiện bác bỏ giả thuyết

Một giả thuyết tích cực về Samsung có thể sai nếu:

- HBM chậm chứng nhận hoặc mất thị phần;
- foundry duy trì tỷ lệ sử dụng/yield thấp trong thời gian dài;
- CAPEX tăng nhưng ROIC không cải thiện;
- smartphone cao cấp mất thị phần hoặc phải tăng khuyến mại;
- chu kỳ bộ nhớ truyền thống dư cung kéo dài.

Viết trước các điều kiện này giúp tránh thay đổi câu chuyện sau khi kết quả xấu xuất hiện.

## Mental Model — Mô hình tư duy

> Samsung Electronics không phải một “công ty điện tử” duy nhất. Nó là nhiều cỗ máy kinh tế nằm trong cùng một pháp nhân hợp nhất. Phân tích tốt phải tách từng cỗ máy, hiểu động lực riêng rồi mới ghép lại thành doanh thu, lợi nhuận, dòng tiền và định giá hợp nhất.

Chuỗi cần giữ trong đầu:

```text
Phân khúc nào thay đổi?
→ động lực sản lượng / giá / cơ cấu nào thay đổi?
→ chi phí cố định và tỷ lệ sử dụng phản ứng ra sao?
→ lợi nhuận chuyển thành CFO thế nào?
→ CAPEX lấy đi bao nhiêu tiền?
→ FCF còn lại bao nhiêu?
→ thị trường đang định giá chu kỳ hay thay đổi cấu trúc?
```
