# Chất phản ứng giới hạn và hiệu suất — ràng buộc nguồn lực của phản ứng

> **Chất phản ứng giới hạn (limiting reagent / 한계 반응물)** là chất phản ứng bị tiêu thụ trước theo yêu cầu stoichiometric và vì thế giới hạn mức tiến triển lý thuyết lớn nhất của phản ứng. Những chất còn lại sau khi phản ứng lý thuyết hoàn tất là **chất phản ứng dư (excess reagents)**.

## Vì sao xuất hiện chất phản ứng giới hạn?

Một phương trình phản ứng quy định tỉ lệ giữa các chất. Nếu lượng ban đầu không được cung cấp đúng theo tỉ lệ đó, hệ không thể dùng hết tất cả các chất cùng lúc.

Ví dụ:

\[
2H_2+O_2\rightarrow2H_2O
\]

Nếu có `3 mol H2` và `3 mol O2`, lượng hydrogen không đủ để dùng hết oxygen. Theo tỉ lệ phản ứng, `3 mol H2` chỉ cần `1.5 mol O2`, nên `H2` là chất giới hạn và còn `1.5 mol O2` dư.

## Xác định bằng mức tiến triển phản ứng

Thay vì dùng mẹo “chia số mol cho hệ số rồi chọn nhỏ nhất” mà không hiểu ý nghĩa, hãy xem đại lượng đó như giới hạn của **mức tiến triển phản ứng (extent of reaction)**.

Với chất phản ứng `i` có lượng ban đầu `n_i` và độ lớn hệ số stoichiometric `|ν_i|`:

\[
\xi_{max,i}=\frac{n_i}{|\nu_i|}
\]

Chất cho giá trị `ξ_max` nhỏ nhất sẽ giới hạn hệ.

Cách nhìn này mở rộng tốt sang những phản ứng phức tạp hơn.

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

## Hiệu suất lý thuyết, thực tế và phần trăm hiệu suất

**Hiệu suất lý thuyết (theoretical yield)** là lượng sản phẩm tối đa theo hóa lượng với chất giới hạn, giả định phản ứng tổng đã chọn và chuyển hóa hoàn toàn.

**Hiệu suất thực tế (actual yield)** là lượng sản phẩm đo được sau thí nghiệm hoặc quá trình.

\[
\%\text{hiệu suất}=\frac{\text{thực tế}}{\text{lý thuyết}}\times100\%
\]

Hiệu suất thấp có thể do cân bằng, động học, phản ứng cạnh tranh, phân hủy, tách không hoàn toàn hoặc thất thoát khi thao tác.

## Độ chuyển hóa và độ chọn lọc

Trong hóa học công nghiệp và hóa học hữu cơ, phần trăm hiệu suất một mình đôi khi không đủ.

**Độ chuyển hóa (conversion)** hỏi tỉ lệ chất phản ứng ban đầu đã thực sự phản ứng.

**Độ chọn lọc (selectivity)** hỏi trong phần đã phản ứng, bao nhiêu đi tới sản phẩm mong muốn thay vì sản phẩm phụ.

Một quá trình có độ chuyển hóa cao nhưng độ chọn lọc thấp vẫn gây lãng phí. Thiết kế chất xúc tác thường tập trung mạnh vào tăng độ chọn lọc, không chỉ tăng tốc độ phản ứng.

## Vì sao cố ý dùng chất dư?

Nhà hóa học thường dùng một chất phản ứng dư để:

- tăng mức tiêu thụ của chất quý hơn;
- dịch chuyển cân bằng;
- đơn giản hóa động học;
- kiểm soát sản phẩm.

Tuy nhiên dùng dư cũng có đánh đổi về chi phí, tinh chế, an toàn và chất thải.

Trong thiết kế quá trình, tỉ lệ tối ưu không nhất thiết chính là tỉ lệ stoichiometric.

## Hiệu quả nguyên tử

**Hiệu quả nguyên tử (atom economy)** đánh giá phần khối lượng lý tưởng của chất phản ứng đi vào sản phẩm mong muốn:

\[
\text{Hiệu quả nguyên tử}=\frac{M_{sản\ phẩm\ mong\ muốn}\times\text{hệ số}}{\sum M_{chất\ phản\ ứng}\times\text{hệ số}}\times100\%
\]

Khác với phần trăm hiệu suất, hiệu quả nguyên tử là tính chất của phương trình phản ứng và sản phẩm được chọn, không phải chất lượng của một lần thí nghiệm.

Hóa học xanh quan tâm cả hiệu suất lẫn hiệu quả nguyên tử vì một phản ứng đạt `99%` hiệu suất vẫn có thể tạo lượng lớn chất thải stoichiometric.

## Khái niệm chất giới hạn ngoài phòng thí nghiệm

Ý tưởng này xuất hiện trong nhiều bài toán kỹ thuật dưới dạng **nút thắt nguồn lực (bottleneck)**.

Nếu dây chuyền có 100 CPU nhưng chỉ 80 bo mạch chủ và mỗi máy tính cần một CPU cùng một bo mạch, tối đa chỉ lắp được 80 máy. Hệ số stoichiometric giống như định mức nguyên liệu của sản phẩm.

Trong chuyển hóa sinh học, chất dinh dưỡng có thể giới hạn sinh khối theo yêu cầu nguyên tố. Trong đốt cháy, hỗn hợp giàu nhiên liệu hoặc nghèo nhiên liệu cũng là bài toán mất cân bằng stoichiometric.

## Các hiểu lầm thường gặp

### “Chất có khối lượng nhỏ nhất là chất giới hạn”

Sai. Phải so lượng chất tương đối với hệ số stoichiometric.

### “Chất giới hạn luôn được dùng hết trong thí nghiệm thật”

Mô hình stoichiometric giả định phản ứng tiến hoàn toàn theo phương trình; cân bằng hoặc động học có thể khiến vẫn còn chất giới hạn.

### “Hiệu suất phần trăm thấp nghĩa là phương trình cân bằng sai”

Không. Hiệu suất phản ánh quá trình thực tế; cân bằng phương trình là ràng buộc bảo toàn.

## Mô hình tư duy

Chất phản ứng giới hạn là **ràng buộc nguồn lực theo tỉ lệ công thức**. Mức tiến triển phản ứng tăng tới khi một nguồn lực bắt buộc chạm giới hạn; chất đó đặt trần lý thuyết cho lượng sản phẩm.

Xem tiếp: [Nồng độ dung dịch](./05_solution_concentration.md).