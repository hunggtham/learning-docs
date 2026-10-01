# An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mối nguy, phơi nhiễm và rủi ro** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Hệ phân cấp kiểm soát** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **An toàn phòng thí nghiệm (laboratory safety / 실험실 안전)** không phải tập hợp các câu “đừng làm X”. Nó là một dạng **kỹ thuật quản lý rủi ro (risk engineering)**: nhận diện mối nguy, hiểu đường phơi nhiễm, thiết kế lại thao tác để khả năng hỏng thấp hơn và hậu quả nhỏ hơn nếu sự cố vẫn xảy ra. An toàn tốt bắt đầu trước khi mở chai hóa chất.

## Mối nguy, phơi nhiễm và rủi ro

**Mối nguy (hazard)** là khả năng nội tại gây hại.

**Phơi nhiễm (exposure)** mô tả đường tiếp xúc, cường độ và thời gian.

**rủi ro (risk / 위험)** phụ thuộc cả hai.

Một thuốc thử rất độc nhưng được giữ kín trong bình tương thích có thể tạo rủi ro thấp hơn cùng chất đó khi bị tạo aerosol trong lúc chuyển mẫu.

Vì vậy câu hỏi an toàn không chỉ là “chất này nguy hiểm không?” mà nên là:

```text
điều gì có thể xảy ra?
qua con đường nào?
hậu quả nghiêm trọng tới đâu?
xác suất thế nào?
hàng rào nào ngăn sự cố?
```

> **Chuyển mạch:** Hazard, exposure và risk mô tả vấn đề; hierarchy of controls chuyển mô tả đó thành lựa chọn can thiệp, bắt đầu từ elimination/substitution trước PPE.

## Hệ phân cấp kiểm soát

Thứ tự ưu tiên từ mạnh tới yếu thường là:

1. loại bỏ (**elimination**);
2. thay thế (**substitution**);
3. kiểm soát kỹ thuật (**engineering controls**);
4. kiểm soát hành chính (**administrative controls**);
5. phương tiện bảo vệ cá nhân (**PPE**).

PPE là hàng rào cuối, không phải giải pháp đầu tiên.

Nếu có thể thay quy trình hoặc thuốc thử bằng lựa chọn ít nguy hiểm hơn, thiết kế lại thường đáng tin cậy hơn chỉ dựa vào găng tay dày hơn.

> **Chuyển mạch:** The hierarchy ranks interventions by reliability; elimination or substitution changes the hazard at its source, while engineering controls contain the residual exposure when the chemistry cannot be replaced.

## Loại bỏ và thay thế

Tư duy thiết kế an toàn có thể gồm giảm quy mô, tránh gia nhiệt hoặc áp suất không cần thiết, chọn dung môi ít bay hơi hơn, thay thuốc thử độc khi hóa học cho phép hoặc tạo trung gian không bền ngay tại nơi sử dụng thay vì lưu trữ lâu.

Tuy nhiên thay thế chỉ có ý nghĩa sau khi kiểm tra mối nguy mới. Một vật liệu ít độc hơn có thể đồng thời dễ cháy hơn hoặc bền môi trường hơn.

> **Chuyển mạch:** Substitution can introduce a new hazard, so the revised exposure path must be checked; engineering controls then provide physical separation, with the fume hood as a concrete airflow barrier.

## Kiểm soát kỹ thuật

Kiểm soát kỹ thuật tạo rào cản vật lý giữa người và mối nguy.

Các ví dụ thường gặp gồm tủ hút, hút cục bộ, hộp găng, tấm chắn phù hợp, khóa liên động và hệ kiểm soát nhiệt độ/áp suất.

Các biện pháp này đáng tin cậy hơn việc chỉ yêu cầu “hãy cẩn thận”.

> **Chuyển mạch:** Engineering controls create the barrier; a fume hood manages vapors and aerosols through airflow, while gloveboxes change the atmosphere itself for air- or moisture-sensitive materials.

## Tủ hút — công cụ kiểm soát dòng khí, không phải tủ chứa đồ

Tủ hút hóa chất chủ yếu giảm phơi nhiễm hơi và aerosol nhờ dòng khí có kiểm soát.

Trong sử dụng thông thường cần giữ cửa chắn theo độ cao làm việc quy định, thao tác đủ sâu bên trong, tránh chất đồ quá nhiều, không che chắn luồng khí và kiểm tra chỉ báo lưu lượng.

Tủ hút không tự động bảo vệ khỏi mọi sự kiện năng lượng cao hoặc mọi loại nguy cơ nổ.

> **Chuyển mạch:** A fume hood removes airborne contaminants from the operator’s breathing zone; a glovebox controls oxygen and moisture but can accumulate incompatible chemicals, so PPE must still match the remaining substance and route of exposure.

## Hộp găng và khí quyển trơ

Hộp găng giúp kiểm soát oxygen và độ ẩm cho hóa chất nhạy không khí.

Tuy nhiên nó cũng là một không gian kín, nơi hóa chất không tương thích có thể làm hỏng hệ tinh lọc hoặc gây nhiễm bẩn kéo dài.

“Khí quyển trơ” không đồng nghĩa “an toàn”; chất tự cháy hoặc chất độc vẫn giữ nguyên mối nguy bên trong.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **PPE phải phù hợp với chất và đường phơi nhiễm** tiếp nhận điểm tựa từ **Hộp găng và khí quyển trơ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo vệ mắt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PPE phải phù hợp với chất và đường phơi nhiễm

PPE điển hình gồm áo blouse, bảo vệ mắt, găng và giày kín.

Khả năng bảo vệ của găng phụ thuộc chính hóa chất và thời gian tiếp xúc. Nitrile rất phổ biến nhưng không phải vật liệu chống mọi dung môi.

Một dung môi có thể thấm qua găng trước khi găng xuất hiện dấu hiệu hỏng bằng mắt, vì vậy phải dựa vào dữ liệu tương thích thay vì suy từ độ dày.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Bảo vệ mắt** tiếp nhận điểm tựa từ **PPE phải phù hợp với chất và đường phơi nhiễm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SDS — nguồn thông tin, không phải thủ tục hình thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo vệ mắt

Kính an toàn giúp chống nhiều mảnh văng và hạt. Kính chống bắn kín hơn khi có nguy cơ chất lỏng. Tấm che mặt bổ sung bảo vệ cho tình huống bắn tóe hoặc va đập lớn hơn.

Tấm che mặt thường là lớp bổ sung chứ không thay thế bảo vệ mắt chính.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Bảo vệ mắt** nêu điều cần giải thích; **SDS — nguồn thông tin, không phải thủ tục hình thức** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Nhãn GHS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SDS — nguồn thông tin, không phải thủ tục hình thức

**Phiếu dữ liệu an toàn (Safety data Sheet, SDS)** chứa thông tin về phân loại mối nguy, kiểm soát phơi nhiễm, tính chất vật lý, chất không tương thích, sơ cứu, ứng phó cháy, xử lý tràn và thải bỏ.

Cần đọc những phần liên quan trực tiếp tới thao tác thực tế trước khi bắt đầu thí nghiệm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **SDS — nguồn thông tin, không phải thủ tục hình thức** nêu điều cần giải thích; **Nhãn GHS** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tính tương thích hóa chất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhãn GHS

**Hệ thống hài hòa toàn cầu (GHS)** dùng biểu tượng để thể hiện các nhóm mối nguy như dễ cháy, chất oxy hóa, độc tính cấp, ăn mòn hoặc nguy hại môi trường.

Biểu tượng cho biết nhóm mối nguy chứ không phải toàn bộ đánh giá rủi ro. Nồng độ và thành phần hỗn hợp vẫn rất quan trọng.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Tính tương thích hóa chất** tiếp nhận điểm tựa từ **Nhãn GHS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính dễ cháy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính tương thích hóa chất

Lưu trữ nên tách theo nhóm không tương thích thay vì chỉ sắp mọi chai theo bảng chữ cái.

Các cặp cần chú ý ở cấp khái niệm gồm chất oxy hóa với nhiên liệu/chất khử; acid với cơ sở (base / 기반) hoặc kim loại phản ứng; chất phản ứng với nước với nguồn ẩm; acid với một số muối có thể giải phóng khí độc; và dung môi có nguy cơ tạo peroxide khi lưu trữ lâu.

Thông tin cụ thể trong SDS và quy trình của cơ sở luôn quan trọng hơn quy tắc tổng quát.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Tính dễ cháy** tiếp nhận điểm tựa từ **Tính tương thích hóa chất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Áp suất hơi và nguy cơ hít** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính dễ cháy

Một số khái niệm chính:

- **điểm chớp cháy (flash point)**: nhiệt độ thấp nhất mà hơi đạt đủ nồng độ để bắt cháy trong điều kiện thử;
- **nhiệt độ tự bốc cháy (autoignition temperature)**: nhiệt độ có thể tự cháy mà không cần nguồn lửa ngoài;
- **giới hạn cháy (flammable limits)**: khoảng nồng độ hơi có thể duy trì ngọn lửa.

Dung môi có điểm sôi cao vẫn có thể nguy hiểm về cháy khi được đun nóng đủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Áp suất hơi và nguy cơ hít** tiếp nhận điểm tựa từ **Tính dễ cháy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chất oxy hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Áp suất hơi và nguy cơ hít

Áp suất hơi cao nghĩa nhiều phân tử đi vào pha khí hơn.

Dung môi độc và dễ bay hơi có thể tạo phơi nhiễm đáng kể ngay cả từ lượng tràn tương đối nhỏ, nên độ bay hơi là biến quan trọng khi quyết định thông gió và điều kiện lưu trữ.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Chất oxy hóa** tiếp nhận điểm tựa từ **Áp suất hơi và nguy cơ hít** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chất ăn mòn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chất oxy hóa

Chất oxy hóa có thể không tự cháy nhưng làm vật liệu khác cháy nhanh hơn hoặc phản ứng mạnh hơn.

Vì vậy chúng cần được tách khỏi nhiên liệu hữu cơ, chất khử và vật liệu thấm hút đã bị nhiễm bẩn theo hướng dẫn tương thích của cơ sở.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Chất ăn mòn** tiếp nhận điểm tựa từ **Chất oxy hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pha loãng acid đậm đặc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chất ăn mòn

Acid và cơ sở (base / 기반) mạnh có thể làm tổn thương mô và vật liệu.

Một số acid đậm đặc còn có tính oxy hóa, khử nước hoặc dễ bay hơi, vì vậy nhãn “acid” che giấu nhiều mối nguy khác nhau.

Lưu trữ acid phải dựa trên tính tương thích cụ thể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Pha loãng acid đậm đặc** tiếp nhận điểm tựa từ **Chất ăn mòn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hóa chất phản ứng mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pha loãng acid đậm đặc

Pha loãng nhiều acid đậm đặc có thể tỏa nhiệt mạnh.

Nguyên tắc thêm acid từ từ vào lượng nước lớn hơn giúp phân tán nhiệt tốt hơn và giảm nguy cơ sôi cục bộ hoặc bắn tóe.

Câu nhớ “thêm acid vào nước” bắt nguồn từ kiểm soát truyền nhiệt chứ không phải một quy tắc ngôn từ tùy ý.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Hóa chất phản ứng mạnh** tiếp nhận điểm tựa từ **Pha loãng acid đậm đặc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nguy cơ khi tăng quy mô** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hóa chất phản ứng mạnh

Một số chất phản ứng mạnh với không khí hoặc nước, hoặc tự phân hủy tỏa nhiệt.

Đánh giá an toàn cần xét quy mô, tốc độ sinh nhiệt, khả năng sinh khí, tích tụ áp suất, cách dừng phản ứng và chất không tương thích.

Không nên suy thẳng từ kết quả thử rất nhỏ sang quy mô lớn nếu chưa xét khác biệt truyền nhiệt và truyền khối.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Nguy cơ khi tăng quy mô** tiếp nhận điểm tựa từ **Hóa chất phản ứng mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ áp suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguy cơ khi tăng quy mô

Thể tích tăng theo \(L^3\), trong khi diện tích bề mặt chỉ tăng theo \(L^2\).

Do đó khi tăng quy mô, khả năng tạo nhiệt có thể tăng nhanh hơn khả năng thoát nhiệt.

Một phản ứng ổn định ở 1 mL không tự động an toàn ở 1 L. Đây là lý do nền tảng của kỹ thuật hóa học khiến mọi lần scale-up cần đánh giá lại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Hệ áp suất** tiếp nhận điểm tựa từ **Nguy cơ khi tăng quy mô** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ chân không** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ áp suất

Bình kín kết hợp gia nhiệt hoặc sinh khí có thể làm áp suất tăng nguy hiểm.

Chỉ sử dụng thiết bị được đánh giá cho áp suất và cơ chế kiểm soát/phân áp phù hợp với quy trình.

Không thể kết luận bình thủy tinh chịu được áp suất chỉ vì thành bình trông dày.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Hệ chân không** tiếp nhận điểm tựa từ **Hệ áp suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chất làm lạnh sâu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ chân không

Chân không tạo nguy cơ **nổ sập vào trong (implosion)** do áp suất bên ngoài, khác với nổ do áp suất nội.

Cần dùng dụng cụ được thiết kế cho chân không, kiểm tra nứt/xước và áp dụng che chắn theo quy trình của cơ sở.

Bẫy lạnh có thể giúp bảo vệ bơm và hạn chế hơi đi vào hệ xả.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Chất làm lạnh sâu** tiếp nhận điểm tựa từ **Hệ chân không** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bình khí nén** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chất làm lạnh sâu

Nitrogen lỏng và các chất cryogenic có thể tạo bỏng lạnh, làm giảm oxygen trong không gian, sinh áp suất nếu bị nhốt kín và trong một số tình huống làm giàu oxygen ngưng tụ.

Chất lỏng cryogenic không được nhốt trong bình không có đường thoát áp phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Bình khí nén** tiếp nhận điểm tựa từ **Chất làm lạnh sâu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khí độc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bình khí nén

Khí nén lưu trữ lượng cơ năng đáng kể.

Các nguyên tắc chung gồm cố định bình, dùng bộ điều áp đúng loại, bảo vệ van khi không kết nối, tách khí không tương thích và dùng xe vận chuyển phù hợp.

Hư hỏng van có thể biến bình thành vật thể chuyển động nguy hiểm.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Khí độc** tiếp nhận điểm tựa từ **Bình khí nén** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bột và aerosol** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khí độc

Nguy cơ của khí phụ thuộc độc tính, tốc độ giải phóng và thông gió.

Công việc với khí độc cần hệ kiểm soát kỹ thuật, phát hiện và kế hoạch khẩn cấp theo quy định của cơ sở; không nên ứng biến hệ chứa hoặc xử lý.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Bột và aerosol** tiếp nhận điểm tựa từ **Khí độc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tam giác cháy và giới hạn của mô hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bột và aerosol

Bột mịn có thể trở thành nguy cơ hít và, nếu cháy được, còn có thể tạo nguy cơ cháy bụi.

Cách thao tác nên giảm phát sinh bụi trong không khí.

Bột nano cần được đánh giá thận trọng hơn vì hành vi trong không khí và hoạt tính bề mặt có thể khác vật liệu khối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Bột và aerosol** đã nêu tiêu chí phân biệt, còn **Tam giác cháy và giới hạn của mô hình** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Ứng phó tràn đổ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tam giác cháy và giới hạn của mô hình

Cháy thông thường cần nhiên liệu, chất oxy hóa và nguồn mồi. Loại bỏ một yếu tố có thể ngăn quá trình cháy.

Tuy nhiên một số đám cháy hóa chất phản ứng cần phương tiện dập chuyên dụng; nước không phải tác nhân phù hợp cho mọi loại cháy.

Phải biết phân loại bình chữa cháy và hướng dẫn của cơ sở trước khi làm việc.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Tam giác cháy và giới hạn của mô hình** đã nêu tiêu chí phân biệt, còn **Ứng phó tràn đổ** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Vòi rửa mắt và tắm khẩn cấp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ứng phó tràn đổ

Cách xử lý phụ thuộc bản chất chất, lượng và khả năng phơi nhiễm.

Tràn nhỏ, ít nguy hiểm có thể được xử lý theo quy trình nội bộ; tràn lớn, độc hoặc phản ứng mạnh có thể cần sơ tán và đội ứng phó đã được đào tạo.

Không nên “lau trước, xác định chất sau”.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Vòi rửa mắt và tắm khẩn cấp** tiếp nhận điểm tựa từ **Ứng phó tràn đổ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân loại chất thải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vòi rửa mắt và tắm khẩn cấp

Cần biết vị trí và đường tiếp cận trước khi làm thí nghiệm, đồng thời giữ thiết bị không bị chắn.

Với phơi nhiễm hóa chất, khử nhiễm nhanh thường rất quan trọng; quy trình cụ thể phải theo hướng dẫn của cơ sở và thông tin an toàn của chất liên quan.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Phân loại chất thải** tiếp nhận điểm tựa từ **Vòi rửa mắt và tắm khẩn cấp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Không trộn chất thải không rõ thành phần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân loại chất thải

Bình chất thải phải tương thích hóa học và được ghi nhãn rõ.

Các dòng không tương thích phải được tách. Cách phân loại có thể gồm dung môi halogen hóa/không halogen, chất thải nước acid/cơ sở (base / 기반), kim loại nặng, chất oxy hóa/phản ứng hoặc chất rắn nhiễm bẩn.

Nhóm cụ thể phụ thuộc quy định địa phương và hệ thống của cơ sở.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Không trộn chất thải không rõ thành phần** tiếp nhận điểm tựa từ **Phân loại chất thải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dung môi có thể tạo peroxide** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Không trộn chất thải không rõ thành phần

Trộn chất thải không rõ có thể tạo nhiệt, áp suất hoặc khí độc.

Nếu thành phần không chắc chắn, cần cô lập và liên hệ người phụ trách an toàn/chất thải thay vì thử trộn để “xem phản ứng”.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Dung môi có thể tạo peroxide** tiếp nhận điểm tựa từ **Không trộn chất thải không rõ thành phần** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ghi nhãn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dung môi có thể tạo peroxide

Một số ether và dung môi liên quan có thể tạo peroxide khi tiếp xúc oxygen trong thời gian lưu trữ.

Nguy cơ tăng theo tuổi và khi dung môi bị cô đặc trong quá trình bay hơi hoặc chưng cất.

Phòng thí nghiệm cần có quy định theo dõi ngày mở, kiểm tra và xử lý phù hợp, đồng thời tránh cô đặc dung môi nghi ngờ chứa peroxide.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Ghi nhãn** tiếp nhận điểm tựa từ **Dung môi có thể tạo peroxide** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sắp xếp nơi làm việc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ghi nhãn

Bình phụ nên ghi tên hóa chất, nồng độ khi cần, mối nguy và ngày/người chuẩn bị theo quy định.

“Một chai chất lỏng trong suốt không rõ là gì” vừa là lỗi an toàn vừa là lỗi toàn vẹn dữ liệu.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Sắp xếp nơi làm việc** tiếp nhận điểm tựa từ **Ghi nhãn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá rủi ro trước thí nghiệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sắp xếp nơi làm việc

Bừa bộn làm tăng xác suất tràn, cản luồng khí, tăng khả năng các chất không tương thích tiếp xúc và làm chậm tiếp cận thiết bị khẩn cấp.

Tổ chức tốt là một dạng kiểm soát kỹ thuật đối với sai sót con người.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Đánh giá rủi ro trước thí nghiệm** tiếp nhận điểm tựa từ **Sắp xếp nơi làm việc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân tích “điều gì xảy ra nếu...?”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đánh giá rủi ro trước thí nghiệm

Trước khi bắt đầu, cần hình dung hoặc ghi lại:

```text
thuốc thử → mối nguy gì?
điều kiện → có nhiệt, áp suất hoặc khí không?
thao tác → có bắn tóe, aerosol hay vật sắc không?
kiểm soát → tủ hút, chắn, PPE nào cần?
sự cố → nếu mất khuấy/làm mát thì sao?
dừng → có thể dừng an toàn bằng cách nào?
chất thải → vật liệu cuối cùng đi đâu?
```

Cách suy luận này hữu ích hơn lời nhắc “hãy cẩn thận” chung chung.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Phân tích “điều gì xảy ra nếu...?”** tiếp nhận điểm tựa từ **Đánh giá rủi ro trước thí nghiệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự cố suýt xảy ra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tích “điều gì xảy ra nếu...?”

Cần nghĩ trước các tình huống như thêm chất quá nhanh, hệ làm mát mất, nước condenser dừng, đường ống tắc, dùng nhầm thuốc thử hoặc mất điện.

An toàn xuất hiện từ việc dự đoán các chế độ hỏng hợp lý và đặt hàng rào trước khi chúng xảy ra.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Sự cố suýt xảy ra** tiếp nhận điểm tựa từ **Phân tích “điều gì xảy ra nếu...?”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Yếu tố con người** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự cố suýt xảy ra

**Near miss** là tình huống có khả năng gây hại nhưng may mắn chưa tạo hậu quả.

Báo cáo và phân tích near miss cho phép sửa hệ thống trước khi có sự cố nghiêm trọng.

Văn hóa chỉ tập trung đổ lỗi thường làm mất dữ liệu học tập; tư duy hệ thống hỏi hàng rào nào đã thất bại và thiết kế nào cần cải thiện.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Yếu tố con người** tiếp nhận điểm tựa từ **Sự cố suýt xảy ra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **An toàn và hóa học xanh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Yếu tố con người

Mệt mỏi, mất tập trung, nhãn khó hiểu, bố trí kém và áp lực thời gian đều làm xác suất lỗi tăng.

Thiết kế tốt khiến hành động đúng dễ thực hiện và hành động sai khó xảy ra, ví dụ dùng đầu nối chuyên biệt, nhãn rõ, checklist cho chuỗi thao tác phức tạp và kiểm tra độc lập ở bước có hậu quả cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **An toàn và hóa học xanh** tiếp nhận điểm tựa từ **Yếu tố con người** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## An toàn và hóa học xanh

Giảm lượng tồn trữ hóa chất nguy hiểm, giảm dung môi và giảm mức khắc nghiệt của phản ứng thường đồng thời cải thiện an toàn người lao động và tác động môi trường.

Thiết kế lại quy trình có thể giải quyết cả hai mục tiêu cùng lúc.

> **Chuyển mạch:** Trong **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Những hiểu lầm thường gặp** tiếp nhận điểm tựa từ **An toàn và hóa học xanh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm thường gặp

### “Có PPE thì thao tác nguy hiểm trở thành an toàn”

Không. PPE chỉ là hàng rào cuối; kiểm soát ở nguồn nên được ưu tiên.

### “Lượng nhỏ thì không nguy hiểm”

Không luôn đúng. Một số vật liệu độc hoặc phản ứng mạnh ngay ở lượng nhỏ, và thể tích kín nhỏ vẫn có thể tạo áp suất đáng kể.

### “Có tủ hút thì mọi phản ứng đều an toàn”

Không. Tủ hút kiểm soát phơi nhiễm qua không khí nhưng không tự động xử lý mọi sự kiện năng lượng cao.

### “Lần trước không có sự cố nên quy trình an toàn”

Không. Thành công trong quá khứ không loại bỏ các chế độ hỏng xác suất thấp nhưng hậu quả lớn.

> **Chuyển mạch:** Ở chặng này của **An toàn phòng thí nghiệm — suy luận về mối nguy trước khi làm thí nghiệm**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Làm việc an toàn trong phòng thí nghiệm là **thiết kế nhiều lớp hàng rào quanh một hệ có năng lượng hóa học và đường phơi nhiễm**. Hãy nhận diện chế độ hỏng, giảm mối nguy ngay từ nguồn, bao chứa phần còn lại, làm sai lệch trở nên dễ phát hiện và bảo đảm có cách dừng thí nghiệm an toàn khi điều kiện không còn như dự kiến.

Xem tiếp: [Dụng cụ thủy tinh và thiết bị](./01_glassware_and_instruments.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
