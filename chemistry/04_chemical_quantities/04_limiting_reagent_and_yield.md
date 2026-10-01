# Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao xuất hiện chất phản ứng giới hạn?** làm rõ cặp khái niệm dễ lẫn và giới hạn của cách giải thích; sau đó sang **Xác định bằng mức tiến triển phản ứng** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **Chất phản ứng giới hạn (limiting reagent / 한계 반응물)** là chất phản ứng bị tiêu thụ trước theo yêu cầu stoichiometric và vì thế giới hạn mức tiến triển lý thuyết lớn nhất của phản ứng. Những chất còn lại sau khi phản ứng lý thuyết hoàn tất là **chất phản ứng dư (excess reagents)**.

## Vì sao xuất hiện chất phản ứng giới hạn?

Một phương trình phản ứng quy định tỉ lệ giữa các chất. Nếu lượng ban đầu không được cung cấp đúng theo tỉ lệ đó, hệ không thể dùng hết tất cả các chất cùng lúc.

Ví dụ:

\[
2H_2+O_2\rightarrow2H_2O
\]

Nếu có `3 mol H2` và `3 mol O2`, lượng hydrogen không đủ để dùng hết oxygen. Theo tỉ lệ phản ứng, `3 mol H2` chỉ cần `1.5 mol O2`, nên `H2` là chất giới hạn và còn `1.5 mol O2` dư.

> **Chuyển mạch:** Tỉ lệ stoichiometric xác định chất phản ứng giới hạn; biểu diễn mức tiến triển giúp kiểm tra chất nào cạn trước, rồi ví dụ nối giới hạn lý thuyết với hiệu suất thực tế.

## Xác định bằng mức tiến triển phản ứng

Thay vì dùng mẹo “chia số mol cho hệ số rồi chọn nhỏ nhất” mà không hiểu ý nghĩa, hãy xem đại lượng đó như giới hạn của **mức tiến triển phản ứng (extent of reaction)**.

Với chất phản ứng `i` có lượng ban đầu `n_i` và độ lớn hệ số stoichiometric `|ν_i|`:

\[
\xi_{max,i}=\frac{n_i}{|\nu_i|}
\]

Chất cho giá trị `ξ_max` nhỏ nhất sẽ giới hạn hệ.

Cách nhìn này mở rộng tốt sang những phản ứng phức tạp hơn.

> **Chuyển mạch:** Ở chặng này của **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Xác định bằng mức tiến triển phản ứng** cho ta quy tắc; **Ví dụ** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Hiệu suất lý thuyết, thực tế và phần trăm hiệu suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ

Phản ứng Haber:

\[
N_2+3H_2\rightarrow2NH_3
\]

Có `5.0 mol N2` và `12.0 mol H2`.

Với `N2`:

\[
\frac{5.0}{1}=5.0
\]

Với `H2`:

\[
\frac{12.0}{3}=4.0
\]

`H2` cho giới hạn nhỏ hơn nên là chất phản ứng giới hạn.

Lượng `NH3` lý thuyết:

\[
2\times4.0=8.0\,mol
\]

`N2` tiêu thụ `4.0 mol`, nên còn lại `1.0 mol`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Ví dụ** cho ta quy tắc; **Hiệu suất lý thuyết, thực tế và phần trăm hiệu suất** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Độ chuyển hóa và độ chọn lọc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu suất lý thuyết, thực tế và phần trăm hiệu suất

**Hiệu suất lý thuyết (theoretical yield)** là lượng sản phẩm tối đa theo hóa lượng với chất giới hạn, giả định phản ứng tổng đã chọn và chuyển hóa hoàn toàn.

**Hiệu suất thực tế (actual yield)** là lượng sản phẩm đo được sau thí nghiệm hoặc quá trình.

\[
\%\văn bản (text / 텍스트){hiệu suất}=\frac{\văn bản (text / 텍스트){thực tế}}{\văn bản (text / 텍스트){lý thuyết}}\times100\%
\]

Hiệu suất thấp có thể do cân bằng, động học, phản ứng cạnh tranh, phân hủy, tách không hoàn toàn hoặc thất thoát khi thao tác.

> **Chuyển mạch:** Trong **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Độ chuyển hóa và độ chọn lọc** tiếp nhận điểm tựa từ **Hiệu suất lý thuyết, thực tế và phần trăm hiệu suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao cố ý dùng chất dư?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ chuyển hóa và độ chọn lọc

Trong hóa học công nghiệp và hóa học hữu cơ, phần trăm hiệu suất một mình đôi khi không đủ.

**Độ chuyển hóa (conversion)** hỏi tỉ lệ chất phản ứng ban đầu đã thực sự phản ứng.

**Độ chọn lọc (selectivity)** hỏi trong phần đã phản ứng, bao nhiêu đi tới sản phẩm mong muốn thay vì sản phẩm phụ.

Một quá trình có độ chuyển hóa cao nhưng độ chọn lọc thấp vẫn gây lãng phí. Thiết kế chất xúc tác thường tập trung mạnh vào tăng độ chọn lọc, không chỉ tăng tốc độ phản ứng.

> **Chuyển mạch:** Ở chặng này của **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Vì sao cố ý dùng chất dư?** tiếp nhận điểm tựa từ **Độ chuyển hóa và độ chọn lọc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu quả nguyên tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao cố ý dùng chất dư?

Nhà hóa học thường dùng một chất phản ứng dư để:

- tăng mức tiêu thụ của chất quý hơn;
- dịch chuyển cân bằng;
- đơn giản hóa động học;
- kiểm soát sản phẩm.

Tuy nhiên dùng dư cũng có đánh đổi về chi phí, tinh chế, an toàn và chất thải.

Trong thiết kế quá trình, tỉ lệ tối ưu không nhất thiết chính là tỉ lệ stoichiometric.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Hiệu quả nguyên tử** tiếp nhận điểm tựa từ **Vì sao cố ý dùng chất dư?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khái niệm chất giới hạn ngoài phòng thí nghiệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu quả nguyên tử

**Hiệu quả nguyên tử (atom economy)** đánh giá phần khối lượng lý tưởng của chất phản ứng đi vào sản phẩm mong muốn:

\[
\văn bản (text / 텍스트){Hiệu quả nguyên tử}=\frac{M_{sản\ phẩm\ mong\ muốn}\times\văn bản (text / 텍스트){hệ số}}{\sum M_{chất\ phản\ ứng}\times\văn bản (text / 텍스트){hệ số}}\times100\%
\]

Khác với phần trăm hiệu suất, hiệu quả nguyên tử là tính chất của phương trình phản ứng và sản phẩm được chọn, không phải chất lượng của một lần thí nghiệm.

Hóa học xanh quan tâm cả hiệu suất lẫn hiệu quả nguyên tử vì một phản ứng đạt `99%` hiệu suất vẫn có thể tạo lượng lớn chất thải stoichiometric.

> **Chuyển mạch:** Trong **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Hiệu quả nguyên tử** đã nêu tiêu chí phân biệt, còn **Khái niệm chất giới hạn ngoài phòng thí nghiệm** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Các hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khái niệm chất giới hạn ngoài phòng thí nghiệm

Ý tưởng này xuất hiện trong nhiều bài toán kỹ thuật dưới dạng **nút thắt nguồn lực (bottleneck)**.

Nếu dây chuyền có 100 CPU nhưng chỉ 80 bo mạch chủ và mỗi máy tính cần một CPU cùng một bo mạch, tối đa chỉ lắp được 80 máy. Hệ số stoichiometric giống như định mức nguyên liệu của sản phẩm.

Trong chuyển hóa sinh học, chất dinh dưỡng có thể giới hạn sinh khối theo yêu cầu nguyên tố. Trong đốt cháy, hỗn hợp giàu nhiên liệu hoặc nghèo nhiên liệu cũng là bài toán mất cân bằng stoichiometric.

> **Chuyển mạch:** Ở chặng này của **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Khái niệm chất giới hạn ngoài phòng thí nghiệm** đã nêu tiêu chí phân biệt, còn **Các hiểu lầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các hiểu lầm thường gặp

### “Chất có khối lượng nhỏ nhất là chất giới hạn”

Sai. Phải so lượng chất tương đối với hệ số stoichiometric.

### “Chất giới hạn luôn được dùng hết trong thí nghiệm thật”

Mô hình stoichiometric giả định phản ứng tiến hoàn toàn theo phương trình; cân bằng hoặc động học có thể khiến vẫn còn chất giới hạn.

### “Hiệu suất phần trăm thấp nghĩa là phương trình cân bằng sai”

Không. Hiệu suất phản ánh quá trình thực tế; cân bằng phương trình là ràng buộc bảo toàn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng**, **Mô hình tư duy** gom các mảnh từ **Các hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Chất phản ứng giới hạn là **ràng buộc nguồn lực theo tỉ lệ công thức**. Mức tiến triển phản ứng tăng tới khi một nguồn lực bắt buộc chạm giới hạn; chất đó đặt trần lý thuyết cho lượng sản phẩm.

Xem tiếp: [Nồng độ dung dịch](./05_solution_concentration.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
