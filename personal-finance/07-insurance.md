# 07 — Bảo hiểm và chuyển giao rủi ro (Insurance / 보험)

## Định vị

[06 — Loans & Debt](./06-loans-debt.md) cho thấy một nghĩa vụ cố định có thể làm dòng tiền mong manh trước cú sốc. Bảo hiểm (insurance / 보험) tồn tại vì một số tổn thất có xác suất không cao nhưng hậu quả tài chính quá lớn để cá nhân tự hấp thụ. Chapter này giải thích pooling, premium, deductible, coverage, exclusions và cách đặt bảo hiểm vào hệ thống tài chính cá nhân.

Chi tiết sản phẩm, quyền lợi bắt buộc và luật bảo hiểm thay đổi mạnh theo quốc gia. Ở đây chỉ xây mô hình tư duy; trước khi mua hoặc hủy hợp đồng phải đọc policy wording và nguồn chính thức của jurisdiction.

## Bảo hiểm không phải công cụ làm giàu

Bảo hiểm hoạt động bằng cách gom rủi ro (risk pooling / 위험공동화): nhiều người đóng phí (premium / 보험료), quỹ chung chi trả cho số người gặp sự kiện đủ điều kiện. Người mua trả một chi phí tương đối nhỏ và biết trước để tránh một tổn thất lớn, không chắc chắn.

Vì vậy việc “tôi đóng nhiều năm mà không nhận lại gì” không tự chứng minh bảo hiểm vô ích. Nếu sự kiện không xảy ra, giá trị nhận được là việc chuyển giao rủi ro trong thời gian được bảo vệ. Ngược lại, một sản phẩm đắt và coverage kém cũng không tốt chỉ vì mang tên bảo hiểm.

## Expected loss và tail risk

Nếu một sự kiện có xác suất `p` và tổn thất `L`, tổn thất kỳ vọng (expected loss / 기대손실) đơn giản là:

```text
Expected loss = p × L
```

Nhưng cá nhân không chỉ quan tâm expected value. Một tổn thất 100 triệu với xác suất 1% có expected loss 1 triệu, nhưng nếu 100 triệu đủ làm hộ gia đình phá sản thì rủi ro đuôi (tail risk / 꼬리위험) quan trọng hơn con số 1 triệu.

Bảo hiểm có ý nghĩa nhất với những sự kiện **ít xảy ra nhưng khó tự gánh**. Những chi phí nhỏ, thường xuyên và dự đoán được đôi khi hiệu quả hơn nếu tự lập quỹ thay vì chuyển giao, tùy sản phẩm và luật.

## Premium, deductible, limit và exclusion

Phí bảo hiểm (premium / 보험료) là giá phải trả để duy trì coverage. Mức khấu trừ (deductible / 자기부담금) là phần người được bảo hiểm phải tự chịu trước hoặc trong cơ chế chi trả theo hợp đồng. Giới hạn bảo hiểm (coverage limit / 보상한도) là mức tối đa insurer chịu theo điều kiện. Điều khoản loại trừ (exclusion / 면책사항) mô tả những trường hợp không được bảo vệ.

Một policy rẻ có thể rẻ vì deductible cao, limit thấp hoặc nhiều exclusions. Vì vậy so sánh phải giữ cùng cấu trúc:

```text
premium
+ deductible / co-pay
+ coverage limit
+ exclusions
+ waiting period
+ renewal conditions
+ claims process
```

Chỉ so premium giống như so loan chỉ bằng monthly payment.

## Liability: bảo vệ khỏi trách nhiệm với người khác

Bảo hiểm trách nhiệm (liability insurance / 배상책임보험) bảo vệ trước một số nghĩa vụ bồi thường với bên thứ ba theo hợp đồng và luật áp dụng. Đây là một lớp dễ bị đánh giá thấp vì người mua thường nghĩ đến “tài sản của mình” trước.

Một tai nạn gây thiệt hại cho người khác có thể lớn hơn giá trị món tài sản gây ra sự cố. Vì thế khi đánh giá car, home hoặc professional exposure, cần phân biệt coverage cho **tài sản của mình** và coverage cho **trách nhiệm với người khác**.

## Các nhóm rủi ro thường gặp

Tùy quốc gia và hoàn cảnh, cá nhân có thể gặp bảo hiểm sức khỏe (health insurance / 건강보험), nhân thọ (life insurance / 생명보험), xe (auto insurance / 자동차보험), nhà/tài sản (property insurance / 재산보험), disability/income protection và liability coverage.

Cách nghĩ đúng không phải “mua đủ tất cả loại”, mà là lập bản đồ:

```text
Sự kiện nào có thể xảy ra?
→ tổn thất tối đa hợp lý là bao nhiêu?
→ phần nào tự chịu được bằng cash/emergency fund?
→ phần nào cần transfer?
→ hợp đồng thực sự chi trả trong tình huống nào?
```

Điều này nối trực tiếp sang [12 — Emergency Fund](./12-emergency-fund.md): quỹ dự phòng xử lý các cú sốc nhỏ/trung bình và deductible; bảo hiểm xử lý các tổn thất vượt khả năng tự tài trợ.

## Underinsurance và overinsurance

Thiếu bảo hiểm (underinsurance / 과소보험) xảy ra khi coverage không đủ với exposure. Ví dụ tài sản tăng giá nhưng limit không được cập nhật, hoặc liability limit quá thấp so với rủi ro.

Bảo hiểm quá mức (overinsurance / 과잉보험) xảy ra khi mua coverage trùng lặp hoặc chuyển giao những rủi ro nhỏ với premium cao đến mức làm dòng tiền xấu đi. Một sản phẩm có yếu tố đầu tư cũng phải được tách thành hai câu hỏi: cost of insurance và economics of investment. Không nên chấp nhận sự pha trộn khiến cả hai khó đánh giá.

## Adverse selection và moral hazard

Lựa chọn bất lợi (adverse selection / 역선택) xảy ra khi người có rủi ro cao có động cơ mua coverage nhiều hơn, làm insurer khó định giá nếu thiếu thông tin. Rủi ro đạo đức (moral hazard / 도덕적 해이) xảy ra khi có bảo hiểm làm hành vi sau đó thay đổi theo hướng tăng rủi ro hoặc claim.

Deductible, underwriting, waiting period, exclusions và monitoring một phần tồn tại để quản lý các vấn đề này. Hiểu cơ chế giúp người mua đọc điều khoản như cấu trúc kinh tế, không phải chỉ “chữ nhỏ gây khó”.

## Bảo hiểm nhân thọ: câu hỏi về người phụ thuộc

Bảo hiểm nhân thọ (life insurance / 생명보험) về bản chất bảo vệ tài chính cho người phụ thuộc hoặc nghĩa vụ còn lại khi người được bảo hiểm qua đời. Câu hỏi trung tâm không phải “một người trưởng thành có nên mua không?”, mà là:

```text
Ai phụ thuộc vào thu nhập/dịch vụ của người này?
Nghĩa vụ nào còn tồn tại nếu người này mất?
Tài sản hiện có bù được bao nhiêu?
Coverage cần kéo dài bao lâu?
```

Người không có dependent và có đủ tài sản có bài toán khác hoàn toàn người có con nhỏ và mortgage dài hạn.

## Claims risk và operational risk

Có policy không đồng nghĩa claim chắc chắn được chi trả. Tổn thất phải thuộc coverage, khai báo đúng, đáp ứng thời hạn và quy trình. Vì vậy lưu hợp đồng, chứng từ, inventory tài sản quan trọng và thông tin người thụ hưởng là một phần của quản trị rủi ro.

Cũng cần xác minh insurer và agent qua cơ quan chính thức để tránh sản phẩm giả hoặc sales practice gây nhầm. [13 — Financial Scams](./13-financial-scams.md) sẽ mở rộng khía cạnh này.

## Kết luận và hướng đọc tiếp

Bảo hiểm (insurance / 보험) là công cụ **chuyển một phần rủi ro tài chính lớn từ cá nhân sang pool** đổi lấy premium. Một hệ thống bền vững thường kết hợp cash buffer cho rủi ro nhỏ, insurance cho tail risk và quản lý hành vi để giảm xác suất tổn thất.

Sau khi biết cách bảo vệ downside, cần hiểu một nghĩa vụ gần như chắc chắn xuất hiện trong phần lớn đời sống tài chính: thuế. [08 — Taxes](./08-taxes.md) sẽ xây các khái niệm gross/net, marginal/effective rate và tax timing mà không giả định luật của một nước là chuẩn toàn cầu.
