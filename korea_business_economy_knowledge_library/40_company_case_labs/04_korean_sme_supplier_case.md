# Korean SME Supplier Case Lab — tập trung khách hàng, quyền thương lượng và chuyển đổi tiền mặt

Case này dùng một **doanh nghiệp giả lập** để mô phỏng cấu trúc thường gặp trong chuỗi cung ứng sản xuất tại Hàn Quốc. Dùng công ty giả lập giúp ta tập trung vào cơ chế kinh tế mà không biến bài học thành nhận xét về một SME cụ thể.

Giả sử `Hanbit Precision (한빛정밀)` sản xuất các module kim loại và nhựa chính xác cho hai khách hàng lớn trong ngành ô tô và điện tử. Công ty có một phần bí quyết quy trình riêng, nhưng bản vẽ và thông số kỹ thuật chủ yếu do khách hàng quyết định. Doanh thu tăng khá nhanh vì sản lượng của khách hàng tăng, trong khi thời hạn thanh toán dài và yêu cầu giảm giá hàng năm gây áp lực lên biên lợi nhuận.

Đây là case để hiểu một nghịch lý: **nhà cung cấp có thể tăng doanh thu và lợi nhuận kế toán nhưng dòng tiền vẫn xấu đi**.

## 1. Vị trí kinh tế trong chuỗi giá trị

Hanbit không bán trực tiếp cho người tiêu dùng cuối. Nhu cầu của công ty là **nhu cầu dẫn xuất (derived demand)**:

```text
Nhu cầu thị trường cuối
→ sản lượng OEM
→ đơn hàng Tier-1
→ đơn hàng của Hanbit
```

Mỗi lớp có thể truyền cú sốc xuống nhà cung cấp. Nếu OEM giảm sản lượng 10%, đơn hàng của nhà cung cấp có thể giảm hơn 10% nếu khách hàng đồng thời giảm tồn kho.

Nhà cung cấp còn chịu bất cân xứng quyền thương lượng: khách hàng lớn thường có nhiều lựa chọn nguồn cung hơn số lựa chọn khách hàng mà nhà cung cấp có.

## 2. Động lực doanh thu

Một mô hình đơn giản:

\[
Revenue = Customer\ Production\ Volume \times Content\ per\ Unit \times Unit\ Price
\]

Tăng trưởng có thể đến từ ba nguồn:

```text
sản lượng khách hàng tăng
lượng giá trị linh kiện trên mỗi sản phẩm tăng
thắng khách hàng hoặc chương trình mới
```

Giá bán đơn vị thường không phải động lực tăng trưởng mạnh vì khách hàng có thể đàm phán giảm giá định kỳ hàng năm.

Nếu doanh thu tăng chỉ vì một khách hàng mở nhà máy mới, **rủi ro tập trung khách hàng (customer concentration risk)** có thể tăng cùng lúc với tăng trưởng.

## 3. Giảm giá hàng năm và cuộc đua năng suất

Giả sử khách hàng yêu cầu giá giảm 3% mỗi năm. Nhà cung cấp chỉ giữ được biên lợi nhuận nếu cải thiện năng suất hoặc giảm chi phí ít nhất đủ bù phần giảm giá đó.

```text
Năm 1: giá đơn vị = 100
Năm 2: giảm giá 3% → 97
```

Nếu cải tiến quy trình giúp chi phí giảm từ 90 xuống 86:

```text
Năm 1: chênh lệch = 10
Năm 2: chênh lệch = 11
```

Biên lợi nhuận vẫn tốt hơn dù giá bán giảm.

Nhưng nếu chi phí lao động hoặc nguyên liệu tăng làm chi phí thành 92:

```text
Năm 2: chênh lệch = 5
```

Doanh thu có thể vẫn tăng nhờ sản lượng, trong khi giá trị kinh tế trên mỗi đơn vị sụt mạnh.

Vì vậy phân tích nhà cung cấp phải tách **tăng sản lượng (volume growth)** khỏi **giá trị kinh tế trên mỗi đơn vị**.

## 4. Tập trung khách hàng

Giả định cơ cấu doanh thu:

```text
Khách hàng A = 55%
Khách hàng B = 25%
Khác = 20%
```

Hai khách hàng lớn nhất chiếm 80%. Sự phụ thuộc này không chỉ nằm ở doanh thu mà còn ở khuôn–đồ gá, tiêu chuẩn chất lượng, đội kỹ thuật và vị trí nhà máy.

Nếu khách hàng A yêu cầu nhà cung cấp xây dây chuyền mới gần nhà máy của họ, Hanbit có thể phải bỏ CAPEX trước khi sản lượng được bảo đảm hoàn toàn.

Rủi ro tập trung nên được nhìn qua nhiều chiều:

```text
tập trung doanh thu
tập trung khoản phải thu
tập trung chương trình / mẫu xe
tập trung địa lý
tập trung công nghệ / thông số kỹ thuật
```

Một nhà cung cấp có 10 khách hàng nhưng 70% doanh thu vẫn đến từ một nền tảng hoặc một mẫu sản phẩm thì mức đa dạng hóa thực tế vẫn thấp.

## 5. Vốn lưu động: nơi tăng trưởng hút tiền mặt

Giả sử khách hàng thanh toán sau 90 ngày nhưng nhà cung cấp phải trả lương và nhiều loại nguyên vật liệu sau khoảng 30 ngày.

Chuỗi tiền mặt:

```text
nhận đơn hàng mới
→ mua nguyên liệu
→ hình thành sản phẩm dở dang
→ giao hàng
→ ghi nhận doanh thu / khoản phải thu
→ chờ 90 ngày
→ thu tiền
```

Lợi nhuận kế toán xuất hiện trước khi tiền mặt được thu.

Một chỉ số quan trọng là **chu kỳ chuyển đổi tiền mặt (Cash Conversion Cycle / CCC)**:

\[
CCC = DIO + DSO - DPO
\]

Nếu số ngày tồn kho `DIO = 45`, số ngày phải thu `DSO = 90` và số ngày phải trả `DPO = 40`:

\[
CCC = 45 + 90 - 40 = 95\ days
\]

Công ty phải tài trợ gần ba tháng chu kỳ hoạt động trước khi thu được tiền.

## 6. Ví dụ tăng trưởng nhưng thiếu tiền mặt

Năm A:

```text
Doanh thu = 10.000
Biên lợi nhuận hoạt động = 8%
Lợi nhuận hoạt động = 800
Khoản phải thu = 2.000
Tồn kho = 1.200
Khoản phải trả = 900
```

Năm B có đơn hàng tăng mạnh:

```text
Doanh thu = 13.000 (+30%)
Biên lợi nhuận hoạt động = 7%
Lợi nhuận hoạt động = 910
Khoản phải thu = 3.500
Tồn kho = 1.900
Khoản phải trả = 1.100
```

Vốn lưu động hoạt động ròng tăng từ:

```text
Năm A = 2.000 + 1.200 - 900 = 2.300
Năm B = 3.500 + 1.900 - 1.100 = 4.300
Mức tăng = 2.000
```

Công ty chỉ tạo thêm 110 lợi nhuận hoạt động nhưng cần thêm khoảng 2.000 vốn lưu động. Nếu không có dự trữ tiền mặt, nhà cung cấp phải vay thêm.

Đây là lý do một công ty tăng trưởng nhanh có thể đồng thời tăng đòn bẩy tài chính.

## 7. Tooling và CAPEX dành riêng cho khách hàng

Nhà cung cấp thường mua khuôn, die, jig, máy móc hoặc thiết bị kiểm tra cho một chương trình cụ thể. Câu hỏi quan trọng là ai sở hữu các tài sản tooling đó và chi phí được thu hồi bằng cách nào.

Các cấu trúc thường gặp:

```text
khách hàng trả trước chi phí tooling
nhà cung cấp sở hữu và khấu hao tooling
chi phí được gộp vào giá đơn vị
chi phí được hoàn lại khi đạt mốc dự án
```

Nếu nhà cung cấp bỏ CAPEX nhưng sản lượng thực tế thấp hơn dự báo, khấu hao vẫn tồn tại. Dự án có thể nhìn có lợi nhuận trên báo giá nhưng kém hiệu quả khi sản lượng thực tế không đạt kế hoạch.

## 8. Cơ chế chuyển giá nguyên liệu

Nếu giá kim loại hoặc nhựa tăng, nhà cung cấp có thể hoặc không thể chuyển phần tăng đó sang khách hàng.

Ba trường hợp:

```text
chuyển hoàn toàn → biên lợi nhuận tương đối được bảo vệ
chuyển có độ trễ → áp lực tạm thời lên biên lợi nhuận / vốn lưu động
không chuyển được → nhà cung cấp tự hấp thụ cú sốc
```

Điều khoản hợp đồng và quyền thương lượng quyết định kết quả kinh tế. Vì vậy mức phơi nhiễm với giá hàng hóa không thể suy ra chỉ từ loại nguyên liệu sử dụng.

## 9. Lỗi chất lượng và rủi ro đuôi khó nhìn

Nhà cung cấp sản xuất có thể chịu yêu cầu bồi thường lớn nếu lỗi linh kiện làm dừng dây chuyền của khách hàng hoặc dẫn tới triệu hồi sản phẩm.

Cấu trúc tổn thất có thể gồm:

```text
phế phẩm / làm lại
+ vận chuyển khẩn cấp
+ khoản khách hàng truy thu
+ bồi thường dừng dây chuyền
+ chi phí triệu hồi
+ mất đơn hàng tương lai
```

Một lỗi nhỏ về số lượng linh kiện vẫn có thể gây tổn thất kinh tế lớn nếu linh kiện nằm sâu trong một sản phẩm đã lắp ráp hoàn chỉnh.

Vì vậy chỉ số chất lượng là một **chỉ báo sớm (leading indicator)** của kết quả tài chính.

## 10. Lao động và thầu phụ

SME sản xuất thường chịu ràng buộc lao động mạnh hơn chaebol. Lạm phát tiền lương, làm thêm giờ, khả năng tuyển lao động nước ngoài và sử dụng thầu phụ đều tác động chi phí trên mỗi đơn vị.

Nếu doanh nghiệp tăng tỷ lệ thuê ngoài để đáp ứng nhu cầu đỉnh, độ linh hoạt chi phí biến đổi có thể tăng nhưng chất lượng, khả năng kiểm soát và chi phí đơn vị cũng có thể xấu đi.

Khi đọc chi phí bán hàng–quản lý và chi phí sản xuất, nên cố hiểu số lao động, mức làm thêm, quy trình thuê ngoài và đầu tư tự động hóa.

## 11. Khách hàng chuyển nhà máy và mở rộng ra nước ngoài

Khi OEM Hàn Quốc mở nhà máy ở Việt Nam, Mỹ, Mexico hoặc châu Âu, nhà cung cấp có thể được yêu cầu đi theo khách hàng.

Cây quyết định:

```text
Có đi theo khách hàng ra nước ngoài không?
├─ Có → CAPEX + tuyển dụng địa phương + tỷ giá + rủi ro thực thi
└─ Không → nguy cơ mất chương trình tương lai
```

FDI của nhà cung cấp vì vậy không chỉ là cơ hội tăng trưởng; đôi khi nó là **đầu tư phòng thủ để giữ quan hệ khách hàng**.

Đây là liên kết trực tiếp giữa [23_foreign_invested_companies_and_korea_entry](../23_foreign_invested_companies_and_korea_entry.md) và kinh tế SME.

## 12. Khả năng chịu nợ

Ngân hàng có thể tài trợ vốn lưu động và thiết bị, nhưng dòng tiền của nhà cung cấp biến động theo đơn hàng của khách hàng.

Cần theo dõi các khoản vay ngắn hạn, khả năng trả lãi, tài trợ dựa trên khoản phải thu, mức tập trung đáo hạn, mức tập trung khách hàng và tài sản bảo đảm.

Một công ty có tỷ lệ nợ thấp tại ngày cuối năm nhưng dùng lượng vay mùa vụ lớn trong năm vẫn có rủi ro thanh khoản.

## 13. Kịch bản mất khách hàng lớn

Giả định khách hàng A chiếm 55% doanh thu và giảm 40% sản lượng đặt hàng.

Chi phí không thể giảm cùng tỷ lệ doanh thu ngay vì lao động cố định, tiền thuê, khấu hao và thiết bị chuyên dụng vẫn tồn tại.

```text
cú sốc doanh thu
→ tỷ lệ sử dụng công suất ↓
→ chi phí cố định trên mỗi đơn vị ↑
→ biên lợi nhuận ↓ mạnh
→ rủi ro giảm giá tồn kho / WIP ↑
→ áp lực covenant và nợ ↑
```

Nếu thiết bị dành riêng cho khách hàng không thể dùng cho khách hàng khác, còn có thể xuất hiện **tổn thất suy giảm tài sản (asset impairment)**.

## 14. Kịch bản tăng trưởng quá nhanh

Giả định chương trình EV mới làm doanh thu tăng 50% nhưng thời hạn thanh toán của khách hàng là 120 ngày.

Báo cáo kết quả kinh doanh tích cực có thể đi cùng:

```text
tồn kho ↑
khoản phải thu ↑↑
CAPEX ↑
vay ngắn hạn ↑
chi phí lãi vay ↑
```

Nếu chương trình tăng sản lượng chậm hơn kế hoạch, doanh nghiệp có thể cùng lúc có tồn kho dư và nợ cao.

Vì vậy kiểm tra sức chịu đựng khi tăng trưởng cũng quan trọng không kém kiểm tra khi suy giảm.

## 15. Lợi thế cạnh tranh của nhà cung cấp

Lợi thế cạnh tranh không nhất thiết đến từ thương hiệu. Nó có thể nằm ở:

```text
bí quyết quy trình
tỷ lệ lỗi thấp
lịch sử chứng nhận
năng lực đồng thiết kế
phản ứng kỹ thuật nhanh
vị trí / tích hợp logistics
chi phí chuyển đổi / chứng nhận
bằng sáng chế hoặc vật liệu độc quyền
```

Nhưng quan hệ lâu năm không tự động là lợi thế bền vững nếu khách hàng có thể dùng hai nguồn cung hoặc thay nhà cung cấp dễ dàng.

Câu hỏi quan trọng là: **khách hàng mất gì nếu đổi nhà cung cấp?** Nếu câu trả lời gần bằng không, quyền thương lượng của nhà cung cấp vẫn yếu.

## 16. Kiểm tra điều tra tài chính

Các dấu hiệu cần xem sâu hơn gồm:

```text
khoản phải thu tăng nhanh hơn doanh thu
tồn kho tăng trong khi sản lượng khách hàng giảm
CFO thấp hơn lợi nhuận ròng nhiều năm
tái cấp vốn ngắn hạn thường xuyên
giao dịch với bên liên quan lớn
CAPEX tăng nhưng tỷ lệ sử dụng thấp
khách hàng trả trước giảm trong khi backlog được mô tả là mạnh
```

Một dấu hiệu cảnh báo không chứng minh gian lận. Nó chỉ cho biết khu vực cần điều tra kỹ hơn.

## 17. Logic định giá

SME supplier không nên được định giá chỉ bằng tốc độ tăng trưởng. **Chất lượng doanh thu** quan trọng hơn:

```text
đa dạng hóa khách hàng
độ bền biên lợi nhuận
khả năng chuyển lợi nhuận thành tiền mặt
quyền sở hữu công nghệ
sức chịu đựng bảng cân đối
độ rõ của chương trình / đơn hàng
```

Doanh thu tăng 30% nhưng FCF âm và mức tập trung khách hàng tăng có thể kém chất lượng hơn doanh thu tăng 8% với dòng tiền mạnh và khách hàng đa dạng.

## 18. Bài tập cuối case

Tạo một bảng đánh giá nhà cung cấp nhưng không cần tổng hợp thành một điểm số duy nhất. Chỉ ghi bằng chứng theo sáu chiều:

| Chiều phân tích | Bằng chứng cần tìm |
|---|---|
| Quyền lực khách hàng | tỷ trọng khách hàng lớn, hợp đồng, giảm giá hàng năm |
| Công nghệ | chứng nhận, bằng sáng chế / quy trình, chi phí chuyển đổi |
| Chuyển đổi tiền mặt | DSO, DIO, DPO, CFO/lợi nhuận ròng |
| CAPEX | tài sản dành riêng hay có thể tái sử dụng |
| Tài trợ | nợ ngắn hạn, lịch đáo hạn, khả năng trả lãi |
| Rủi ro giảm giá | mất khách hàng, lỗi chất lượng, di chuyển nhà máy |

Mục tiêu không phải xếp hạng nhà cung cấp mà là biết **rủi ro nằm ở đâu và truyền vào tiền mặt như thế nào**.

## Liên kết

Đọc cùng [06_sme_mid_sized_and_subcontracting_ecosystem](../06_sme_mid_sized_and_subcontracting_ecosystem.md), [02_trade_export_and_global_value_chains](../02_trade_export_and_global_value_chains.md), [23_foreign_invested_companies_and_korea_entry](../23_foreign_invested_companies_and_korea_entry.md) và [36_credit_ratings_bonds_default_and_restructuring](../36_credit_ratings_bonds_default_and_restructuring.md).