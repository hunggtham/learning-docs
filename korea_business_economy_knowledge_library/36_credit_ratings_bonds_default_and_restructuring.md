# Xếp hạng tín nhiệm, trái phiếu, vỡ nợ và tái cấu trúc tại doanh nghiệp Hàn Quốc (Credit Risk / 신용위험·회사채·구조조정)

Một doanh nghiệp có thể vẫn báo lợi nhuận hoạt động nhưng rơi vào khủng hoảng nếu nợ đáo hạn trước khi tiền mặt về. Vì vậy khi phân tích doanh nghiệp, đặc biệt là xây dựng, công nghiệp nặng, hàng không, bán lẻ, công ty mẹ có đòn bẩy cao hoặc doanh nghiệp dự án, phải tách **rủi ro lợi nhuận** khỏi **rủi ro tín dụng (credit risk / 신용위험)**.

Phân tích tín dụng không hỏi đầu tiên “doanh nghiệp có tăng trưởng không?”. Nó hỏi: **doanh nghiệp có đủ tiền để trả đúng nghĩa vụ, đúng thời điểm, trong một phạm vi kịch bản hợp lý hay không?**

Chapter này nối kế toán, tài trợ doanh nghiệp, thị trường trái phiếu và tái cấu trúc thành một chuỗi duy nhất.

## 1. Rủi ro tín dụng là gì?

**Rủi ro tín dụng (credit risk / 신용위험)** là khả năng người vay hoặc tổ chức phát hành không thực hiện đầy đủ nghĩa vụ hợp đồng như trả lãi, gốc hoặc các khoản thanh toán khác.

Ba khái niệm nên tách:

- **Xác suất vỡ nợ (Probability of Default / PD / 부도확률):** xác suất người vay vỡ nợ.
- **Mức tổn thất khi vỡ nợ (Loss Given Default / LGD / 부도시손실률):** nếu vỡ nợ thì chủ nợ mất bao nhiêu sau thu hồi.
- **Dư nợ tại thời điểm vỡ nợ (Exposure at Default / EAD / 부도시익스포저):** mức phơi nhiễm tại thời điểm xảy ra vỡ nợ.

Có thể gần đúng:

\[
Tổn\ thất\ tín\ dụng\ kỳ\ vọng \approx PD \times LGD \times EAD
\]

Nhà phân tích tín dụng không chỉ quan tâm vỡ nợ có xảy ra hay không mà còn quan tâm giá trị thu hồi nếu nó xảy ra.

## 2. Cổ đông và chủ nợ nhìn cùng một doanh nghiệp khác nhau thế nào?

Cổ đông hưởng phần tăng giá trị sau khi mọi nghĩa vụ cố định được trả. Chủ nợ thường chỉ nhận gốc và lãi theo hợp đồng; phần tăng giá trị bị giới hạn nhưng lại chịu tổn thất nếu doanh nghiệp không trả được nợ.

Vì vậy cổ đông có thể thích mở rộng mạnh nếu kỳ vọng tăng trưởng lớn. Chủ nợ thường quan tâm nhiều hơn tới sự ổn định dòng tiền, tài sản bảo đảm, điều khoản nợ và khả năng bảo vệ trong kịch bản xấu.

Một dự án có NPV dương nhưng biến động rất cao có thể hấp dẫn cổ đông nhưng không hấp dẫn chủ nợ nếu làm đòn bẩy tăng quá mạnh.

## 3. Trái phiếu doanh nghiệp hoạt động thế nào?

Khi doanh nghiệp phát hành **trái phiếu doanh nghiệp (corporate bond / 회사채)**, nhà đầu tư cho doanh nghiệp vay theo các điều khoản như mệnh giá, lãi suất coupon, ngày đáo hạn, thứ tự ưu tiên và covenant.

Giá trái phiếu và lợi suất di chuyển ngược chiều. Nếu thị trường yêu cầu lợi suất cao hơn do lãi suất chuẩn hoặc chênh lệch tín dụng tăng, giá của trái phiếu cũ giảm.

Có thể hình dung:

\[
Lợi\ suất\ trái\ phiếu\ doanh\ nghiệp \approx Lợi\ suất\ chuẩn\ chính\ phủ + Chênh\ lệch\ tín\ dụng + Phần\ bù\ thanh\ khoản + Phần\ bù\ kỳ\ hạn
\]

**Chênh lệch tín dụng (credit spread)** phản ánh phần bù mà nhà đầu tư yêu cầu cho rủi ro riêng của tổ chức phát hành, rủi ro vỡ nợ và bất định.

## 4. Chênh lệch tín dụng là tín hiệu thị trường, không phải chẩn đoán hoàn chỉnh

Nếu chênh lệch tín dụng tăng nhanh, thị trường đang yêu cầu phần bù cao hơn. Nhưng vẫn phải hỏi nguyên nhân:

```text
Lãi suất chuẩn tăng?
Rủi ro ngành tăng?
Đòn bẩy doanh nghiệp tăng?
Thanh khoản thị trường giảm?
Rủi ro sự kiện?
Toàn thị trường chuyển sang né rủi ro?
```

Spread có thể phản ứng trước xếp hạng tín nhiệm, nhưng cũng có thể tăng quá mức trong giai đoạn hoảng loạn.

## 5. Xếp hạng tín nhiệm là gì?

**Xếp hạng tín nhiệm (credit rating / 신용등급)** là đánh giá có cấu trúc về mức độ tín nhiệm tương đối. Tổ chức xếp hạng thường xem xét rủi ro kinh doanh, vị thế cạnh tranh, chính sách tài chính, đòn bẩy, khả năng trả lãi, thanh khoản, hỗ trợ của tập đoàn và rủi ro sự kiện.

Xếp hạng không phải bảo đảm. Nhãn AAA không có nghĩa xác suất tổn thất bằng 0; xếp hạng thấp cũng không có nghĩa chắc chắn sẽ vỡ nợ.

Điều quan trọng là **hướng đi của xếp hạng**:

```text
Ổn định → triển vọng tiêu cực → hạ bậc
```

hoặc:

```text
Kinh doanh yếu → giảm nợ → khả năng trả nợ tốt hơn → có thể nâng bậc
```

Hướng thay đổi đôi khi quan trọng hơn mức xếp hạng tại một thời điểm.

## 6. Hạng đầu tư và hạng đầu cơ

Thị trường thường chia rộng giữa **hạng đầu tư (investment grade)** và **hạng đầu cơ/lợi suất cao (speculative grade / high yield)**. Ranh giới cụ thể phụ thuộc thang điểm và phương pháp xếp hạng.

Khi tổ chức phát hành bị hạ qua một ngưỡng quan trọng, tập nhà đầu tư có thể thay đổi. Một số quỹ hoặc tổ chức chỉ được nắm chứng khoán từ mức xếp hạng nhất định trở lên. Vì vậy hạ bậc có thể làm spread tăng mạnh hơn mức thay đổi cơ bản của doanh nghiệp.

Đây là **hiệu ứng bán bắt buộc (forced-seller effect)**.

## 7. Khả năng trả lãi

Một chỉ số cơ bản:

\[
Khả\ năng\ trả\ lãi = \frac{EBIT}{Chi\ phí\ lãi}
\]

Nếu EBIT = 300 tỷ KRW và chi phí lãi = 100 tỷ, tỷ lệ là 3 lần.

Nhưng 3 lần không phải ngưỡng an toàn chung cho mọi ngành. Doanh nghiệp chu kỳ cần bộ đệm lớn hơn doanh nghiệp ổn định kiểu hạ tầng. Ngoài ra EBIT không phải tiền mặt.

Vì vậy phải xem thêm CFO, vốn lưu động và CAPEX.

## 8. Nợ ròng và đòn bẩy

\[
Nợ\ ròng = Tổng\ nợ - Tiền\ mặt
\]

\[
Nợ\ ròng/EBITDA
\]

Các chỉ số này hữu ích nhưng có bẫy. Tiền mặt có thể bị hạn chế sử dụng. EBITDA có thể đang ở đỉnh chu kỳ. Nợ thuê hoặc bảo lãnh có thể chưa phản ánh đầy đủ.

Do đó tỷ lệ nợ ròng chỉ là điểm bắt đầu.

## 9. Lịch đáo hạn nợ

Phân tích tín dụng phải có **thang đáo hạn (maturity ladder / 만기구조)**.

Ví dụ:

```text
Năm 1: 1,2 nghìn tỷ KRW
Năm 2: 0,4 nghìn tỷ KRW
Năm 3: 0,3 nghìn tỷ KRW
Năm 4+: 2,0 nghìn tỷ KRW
```

Tổng nợ là 3,9 nghìn tỷ nhưng áp lực tái cấp vốn ngay lập tức tập trung chủ yếu ở năm 1.

Hai doanh nghiệp có cùng đòn bẩy nhưng kỳ hạn tập trung khác nhau sẽ có rủi ro thanh khoản rất khác.

## 10. Rủi ro tái cấp vốn

**Rủi ro tái cấp vốn (refinancing risk / 차환위험)** xuất hiện khi doanh nghiệp phụ thuộc vào phát hành nợ mới để trả nợ cũ.

Tái cấp vốn bình thường không xấu. Nhiều doanh nghiệp trưởng thành liên tục quay vòng nợ. Vấn đề xảy ra khi thị trường đóng đúng lúc doanh nghiệp có lượng nợ đáo hạn lớn.

```text
Lợi nhuận yếu
→ lo ngại xếp hạng
→ spread tăng
→ chi phí tái cấp vốn tăng
→ khả năng trả lãi xấu đi
→ niềm tin nhà đầu tư giảm
→ khả năng tiếp cận thị trường bị thu hẹp
```

Đây là vòng xoáy tín dụng tự củng cố.

## 11. Nguồn thanh khoản và nhu cầu thanh khoản

Một cách thực tế là dựng bảng 12–24 tháng.

**Nguồn** có thể gồm tiền mặt, CFO kỳ vọng, hạn mức tín dụng cam kết, bán tài sản và thu hồi khoản phải thu.

**Nhu cầu** gồm nợ đáo hạn, lãi, CAPEX, vốn lưu động, cổ tức và các khoản bắt buộc khác.

\[
Bộ\ đệm\ thanh\ khoản = Nguồn\ khả\ dụng - Nhu\ cầu\ ngắn\ hạn
\]

Nếu bộ đệm chỉ dương trong kịch bản cơ sở nhưng âm khi doanh thu giảm 10%, doanh nghiệp có cấu trúc thanh khoản mong manh.

## 12. Hạn mức cam kết và không cam kết

Không nên coi mọi hạn mức tín dụng chưa sử dụng như tiền mặt.

**Hạn mức cam kết (committed line)** thường chắc chắn hơn nhưng vẫn có điều kiện. **Hạn mức không cam kết (uncommitted line)** có thể bị ngân hàng giảm hoặc hủy dễ hơn.

Trong khủng hoảng, chất lượng nguồn thanh khoản quan trọng hơn con số tiêu đề.

## 13. Covenant

**Điều khoản bảo vệ chủ nợ (covenant / 재무약정)** giới hạn một số hành vi của người vay hoặc yêu cầu duy trì chỉ tiêu tài chính.

Ví dụ:

- đòn bẩy tối đa;
- khả năng trả lãi tối thiểu;
- vốn chủ sở hữu tối thiểu;
- giới hạn vay thêm;
- giới hạn cổ tức;
- yêu cầu tài sản bảo đảm.

Nếu vi phạm, kết quả có thể từ miễn trừ tạm thời tới tăng lãi suất, bổ sung tài sản bảo đảm hoặc yêu cầu trả nợ sớm.

Vi phạm covenant không đồng nghĩa phá sản nhưng có thể làm quyền thương lượng chuyển sang chủ nợ.

## 14. Nợ có bảo đảm và không bảo đảm

**Nợ có bảo đảm (secured debt / 담보부채무)** có quyền đối với tài sản cụ thể. **Nợ không bảo đảm (unsecured debt / 무담보채무)** dựa nhiều hơn vào năng lực tín dụng chung của doanh nghiệp.

Khi vỡ nợ, mức thu hồi phụ thuộc thứ tự pháp lý, giá trị tài sản bảo đảm và điều khoản tái cấu trúc.

Vì vậy phải đọc số nợ cùng **thứ tự ưu tiên (seniority / 변제순위)**.

## 15. Nợ ưu tiên, nợ thứ cấp và mezzanine

Nợ ưu tiên được trả trước nợ thứ cấp. **Vốn mezzanine** nằm giữa nợ và vốn chủ sở hữu về mức rủi ro/lợi nhuận, thường có coupon cao hơn hoặc quyền chọn.

Có thể hình dung:

```text
Nợ ưu tiên có bảo đảm
Nợ ưu tiên không bảo đảm
Nợ thứ cấp / mezzanine
Cổ phần ưu đãi
Cổ phần phổ thông
```

Càng xuống dưới, cơ hội tăng giá có thể lớn hơn nhưng mức bảo vệ khi doanh nghiệp gặp khó khăn yếu hơn.

## 16. Trái phiếu chuyển đổi và trái phiếu kèm quyền mua cổ phiếu

**Trái phiếu chuyển đổi (Convertible Bond / CB / 전환사채)** cho người nắm giữ quyền chuyển trái phiếu thành cổ phiếu theo điều kiện nhất định. **Trái phiếu kèm quyền mua cổ phiếu (Bond with Warrants / BW / 신주인수권부사채)** gắn quyền mua cổ phiếu mới.

Đây là chứng khoán lai: vừa có quyền đòi nợ vừa có quyền chọn tăng giá của cổ phiếu.

Doanh nghiệp có thể dùng chúng vì lãi suất coupon thấp hơn nợ thông thường hoặc vì nhà đầu tư muốn thêm cơ hội tăng giá. Nhưng cổ đông hiện hữu cần theo dõi khả năng pha loãng.

## 17. Bảo lãnh và nghĩa vụ tiềm tàng

Doanh nghiệp có thể không thể hiện đầy đủ đòn bẩy kinh tế chỉ qua nợ vay nếu đã bảo lãnh nợ cho công ty con hoặc SPV.

Nếu bên được bảo lãnh không trả được nợ, nghĩa vụ tiềm tàng có thể trở thành dòng tiền ra thực tế.

Vì vậy phải đọc thuyết minh về:

- bảo lãnh thanh toán;
- bảo lãnh nợ;
- bảo lãnh PF;
- thư tín dụng;
- cam kết;
- kiện tụng.

Xem [`09_disclosure_accounting_dart_kind.md`](./09_disclosure_accounting_dart_kind.md).

## 18. Cross-default và yêu cầu trả nợ trước hạn

Hợp đồng nợ có thể chứa **điều khoản vỡ nợ chéo (cross-default)**: vi phạm ở một nghĩa vụ có thể kích hoạt vi phạm ở nghĩa vụ khác.

**Yêu cầu trả nợ trước hạn (acceleration)** cho phép chủ nợ đòi thanh toán sớm sau một sự kiện được quy định.

Điều này khiến một vi phạm nhỏ đôi khi lan thành khủng hoảng thanh khoản lớn.

## 19. Vỡ nợ kỹ thuật và vỡ nợ thanh toán

Doanh nghiệp có thể vi phạm covenant dù vẫn trả lãi đúng hạn. Đây là **vỡ nợ kỹ thuật (technical default)**.

**Vỡ nợ thanh toán (payment default)** là không trả gốc hoặc lãi đúng hợp đồng.

Vỡ nợ kỹ thuật vẫn nghiêm trọng vì bên cho vay có thể yêu cầu đàm phán lại hoặc bổ sung bảo vệ.

## 20. Khó khăn tài chính không đồng nghĩa phá sản ngay lập tức

Khi doanh nghiệp gặp khó khăn, có nhiều con đường:

```text
Cải thiện hoạt động
Bán tài sản
Tăng vốn chủ sở hữu
Gia hạn nợ
Xin miễn covenant
Đổi nợ thành cổ phần
Workout
Phục hồi theo tòa án
Thanh lý
```

Từ “khó khăn” tới “phá sản” có nhiều trạng thái trung gian.

## 21. Workout (워크아웃)

**Workout** thường là tái cấu trúc được phối hợp với chủ nợ ngoài quy trình thanh lý đầy đủ. Mục tiêu là giữ giá trị của doanh nghiệp đang hoạt động nếu hoạt động cốt lõi vẫn khả thi nhưng cấu trúc vốn quá nặng.

Chủ nợ có thể gia hạn kỳ hạn, giảm lãi suất, cấp thêm thanh khoản hoặc đổi nợ thành cổ phần.

> Nếu giá trị doanh nghiệp đang hoạt động lớn hơn giá trị thanh lý, tái cấu trúc có thể tốt hơn phá sản ngay.

## 22. Phục hồi theo tòa án (회생절차)

Quy trình phục hồi dưới sự giám sát của tòa giúp đóng băng hoặc phối hợp các yêu cầu của chủ nợ và xây kế hoạch để doanh nghiệp tiếp tục hoạt động trong khi nợ được tái cấu trúc.

Câu hỏi cốt lõi là **khả năng tồn tại (viability)**. Nếu hoạt động cốt lõi tạo tiền nhưng gánh nợ quá lớn, phục hồi có lý do kinh tế. Nếu mô hình kinh doanh đã mất khả năng tồn tại, tái cấu trúc chỉ trì hoãn thanh lý.

## 23. Đổi nợ thành cổ phần

Khi chủ nợ đổi nợ lấy cổ phiếu:

```text
Nợ giảm
Vốn chủ sở hữu tăng
Chi phí lãi giảm
Pha loãng cổ đông cũ tăng
```

Doanh nghiệp có thể khỏe hơn sau tái cấu trúc nhưng cổ đông cũ không nhất thiết được hưởng lợi tương ứng.

## 24. Bán tài sản và giảm đòn bẩy

Bán tài sản không cốt lõi tạo tiền để trả nợ. Đây là công cụ tái cấu trúc đơn giản nhưng có đánh đổi.

Nếu phải bán tài sản chất lượng cao ở giá thấp trong khủng hoảng, bảng cân đối tốt hơn ngắn hạn nhưng khả năng tạo lợi nhuận tương lai giảm.

Vì vậy giảm đòn bẩy phải xét **chất lượng tài sản đã bán**, không chỉ số nợ giảm.

## 25. Tăng vốn khi doanh nghiệp gặp khó khăn

Phát hành thêm cổ phiếu có thể cứu khả năng thanh toán hoặc thanh khoản nhưng gây pha loãng lớn nếu giá phát hành thấp.

Doanh nghiệp có thể sống sót trong khi giá trị của cổ đông cũ bị suy giảm mạnh.

Đây là lý do mức thu hồi của chủ nợ và lợi suất của cổ đông không giống nhau.

## 26. Phân tích mức thu hồi

Khi rủi ro vỡ nợ cao, hãy hỏi:

```text
Giá trị doanh nghiệp trong trạng thái khó khăn?
Giá trị tài sản bảo đảm?
Thứ tự ưu tiên của từng quyền đòi?
Chi phí hành chính / tái cấu trúc?
Giá trị tiếp tục hoạt động so với giá trị thanh lý?
```

Thứ tự đơn giản:

```text
Giá trị doanh nghiệp khi khó khăn
→ chủ nợ có bảo đảm
→ nợ ưu tiên không bảo đảm
→ nợ thứ cấp
→ cổ phần ưu đãi
→ cổ phần phổ thông
```

Cổ phần phổ thông chỉ nhận phần còn lại sau các quyền đòi ưu tiên.

## 27. Bẫy EBITDA ở đỉnh chu kỳ

Nếu tính đòn bẩy bằng nợ chia EBITDA đang ở đỉnh chu kỳ, tỷ lệ có thể trông rất thấp đúng lúc điều kiện tốt nhất.

Ví dụ nợ = 4T, EBITDA đỉnh = 2T → 2 lần. Nếu EBITDA chuẩn hóa = 1T → 4 lần.

Nhà phân tích tín dụng phải chuẩn hóa chu kỳ, đặc biệt với bán dẫn, hóa chất, vận tải biển, thép, xây dựng và hàng hóa cơ bản.

## 28. Cú sốc vốn lưu động

Khủng hoảng tín dụng không chỉ đến từ thua lỗ hoạt động.

Nếu khách hàng trả chậm, tồn kho tăng và nhà cung cấp đòi thanh toán sớm hơn:

```text
DSO tăng
DIO tăng
DPO giảm
→ chu kỳ chuyển đổi tiền mặt dài hơn
→ nhu cầu tài trợ tăng
```

Doanh nghiệp có thể vẫn báo lãi nhưng hết tiền.

## 29. Ngưỡng xếp hạng và yêu cầu bổ sung tài sản bảo đảm

Một số hợp đồng thay đổi điều khoản khi xếp hạng giảm: phải bổ sung tài sản bảo đảm, tăng ký quỹ phái sinh hoặc mất khả năng tiếp cận một số nguồn vốn.

Do đó hạ bậc có thể tạo **nhu cầu tiền mặt phi tuyến (nonlinear cash need)**.

## 30. Hỗ trợ từ tập đoàn: có thể có nhưng không được mặc định

Công ty con thuộc chaebol lớn có thể hưởng hỗ trợ ngầm hoặc chính thức từ tập đoàn. Nhưng phải phân biệt:

- bảo lãnh pháp lý;
- tỷ lệ sở hữu của công ty mẹ;
- mức quan trọng chiến lược;
- lịch sử hỗ trợ;
- giới hạn pháp lý.

Tên thương hiệu lớn không đồng nghĩa có bảo lãnh.

## 31. Doanh nghiệp công và cảm nhận gần giống rủi ro quốc gia

Một số cơ quan công có mức kỳ vọng hỗ trợ cao hơn doanh nghiệp tư nhân, nhưng vẫn phải đọc khung pháp lý và cơ chế hỗ trợ thực tế.

Không nên tự động coi mọi tổ chức liên quan nhà nước là rủi ro quốc gia.

Xem [`25_public_enterprises_and_state_owned_companies.md`](./25_public_enterprises_and_state_owned_companies.md).

## 32. Kiểm tra sức chịu đựng tín dụng

Một kịch bản có thể dùng:

```text
Doanh thu -15%
Biên lợi nhuận -3 điểm %
DSO +20 ngày
Lãi suất +150 bp
Chênh lệch tái cấp vốn +250 bp
KRW mất giá 10%
Tiền bán tài sản thấp hơn giá sổ sách 30%
```

Sau đó tính:

- CFO;
- khả năng trả lãi;
- nợ/EBITDA;
- bộ đệm thanh khoản;
- khoảng an toàn covenant;
- khoảng thiếu hụt đáo hạn.

Mục tiêu không phải dự đoán chính xác khủng hoảng mà tìm ngưỡng nơi cấu trúc vốn bắt đầu thất bại.

## 33. Quy trình phân tích tín dụng

```text
1. Độ ổn định kinh doanh
2. Tính chu kỳ của lợi nhuận
3. Chuyển đổi lợi nhuận thành tiền
4. Nợ và nghĩa vụ ẩn
5. Lịch đáo hạn
6. Độ nhạy với lãi suất và tỷ giá
7. Nguồn thanh khoản
8. Covenant / tài sản bảo đảm
9. Hỗ trợ tập đoàn
10. Kịch bản căng thẳng
11. Mức thu hồi nếu vỡ nợ
```

## Mô hình tư duy

> Phân tích cổ phiếu hỏi **phần tăng giá còn bao nhiêu**. Phân tích tín dụng hỏi **mức giảm tới đâu trước khi chủ nợ bắt đầu mất tiền**.

Rủi ro tín dụng là giao điểm của:

```text
Biến động kinh doanh
× đòn bẩy
× mức tập trung kỳ hạn
× thanh khoản
× khả năng tiếp cận thị trường
× thứ tự pháp lý
```

Một doanh nghiệp kinh doanh tốt nhưng cấu trúc vốn xấu vẫn có thể vỡ nợ. Một doanh nghiệp trung bình nhưng nợ thấp và thanh khoản mạnh có thể tồn tại rất lâu.

## Những nhầm lẫn thường gặp

**“Có lãi thì không vỡ nợ.”** Sai. Vỡ nợ là vấn đề tiền mặt và thời điểm.

**“Nợ/EBITDA thấp là an toàn.”** Chưa đủ. EBITDA có thể đang ở đỉnh chu kỳ và kỳ hạn nợ có thể tập trung.

**“Tổ chức xếp hạng đã đánh giá rồi nên không cần tự phân tích.”** Sai. Xếp hạng là đầu vào, không thay thế phân tích.

**“Tái cấu trúc tốt cho doanh nghiệp thì tốt cho cổ đông.”** Không nhất thiết. Đổi nợ thành cổ phần hoặc phát hành thêm có thể cứu doanh nghiệp nhưng pha loãng cổ đông cũ rất mạnh.

**“Tập đoàn mẹ lớn sẽ luôn cứu công ty con.”** Không thể mặc định nếu không có động lực pháp lý hoặc kinh tế rõ ràng.

## Liên kết tiếp theo

- [`09_disclosure_accounting_dart_kind.md`](./09_disclosure_accounting_dart_kind.md) — đọc nghĩa vụ và thuyết minh.
- [`10_capital_markets_kospi_kosdaq_konex.md`](./10_capital_markets_kospi_kosdaq_konex.md) — bối cảnh thị trường trái phiếu/cổ phiếu.
- [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md) — cấu trúc tài trợ.
- [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md) — rủi ro PF.
- [`20_how_to_analyze_a_korean_company.md`](./20_how_to_analyze_a_korean_company.md) — khung phân tích doanh nghiệp.