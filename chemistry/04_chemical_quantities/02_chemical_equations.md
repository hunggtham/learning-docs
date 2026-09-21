# Phương trình hóa học — bảo toàn và ngôn ngữ định lượng của phản ứng

> **Phương trình hóa học (chemical equation / 화학 반응식)** là cách biểu diễn một biến đổi hóa học. Nó phải bảo toàn nguyên tử và tổng điện tích, còn các hệ số trong phương trình cân bằng cung cấp tỉ lệ stoichiometric giữa chất phản ứng và sản phẩm.

## Phương trình là mô hình của biến đổi

Phương trình:

\[
2H_2+O_2\rightarrow2H_2O
\]

không mô tả cơ chế của từng va chạm. Nó mô tả **biến đổi tổng (net transformation)**: bao nhiêu tiểu phần bị tiêu thụ và tạo ra theo các định luật bảo toàn.

Vì vậy phương trình cân bằng là một lớp hạch toán vĩ mô, không phải “bộ phim phân tử”.

## Vì sao phải cân bằng?

Trong phản ứng hóa học thông thường, hạt nhân và electron được tái sắp xếp nhưng các nguyên tố hóa học không tự được tạo hoặc phá hủy. Số nguyên tử của mỗi nguyên tố phải bằng nhau ở hai phía.

Tổng điện tích cũng phải được bảo toàn.

Do đó cân bằng phương trình là hệ quả của **định luật bảo toàn (conservation laws)**, không phải quy ước ký hiệu tùy ý.

## Hệ số và hệ số stoichiometric

Hệ số 2 trước `H2` nghĩa là hai tiểu phần hoặc hai mol `H2` theo tỉ lệ phản ứng. Nó không biến `H2` thành `H4`.

Có thể viết phản ứng tổng quát:

\[
aA+bB\rightarrow cC+dD
\]

Các hệ số xác định **vector stoichiometric (stoichiometric vector)**. Khi phản ứng tiến triển, lượng mỗi tiểu phần thay đổi theo cùng một mức tiến triển chung.

Trong nhiệt động lực học, ý tưởng này được mô tả bằng **mức tiến triển phản ứng (extent of reaction, \(\xi\))**:

\[
dn_i=\nu_i d\xi
\]

với `ν_i` âm cho chất phản ứng và dương cho sản phẩm.

## Cân bằng bằng suy luận trực tiếp

Với phương trình đơn giản, suy luận theo số nguyên tử được bảo toàn thường hiệu quả nhất.

Ví dụ phản ứng cháy propane:

\[
C_3H_8+O_2\rightarrow CO_2+H_2O
\]

Cân bằng carbon trước thành `3CO2`, cân bằng hydrogen thành `4H2O`. Phía sản phẩm có `3×2+4=10` nguyên tử oxygen nên cần `5O2`:

\[
C_3H_8+5O_2\rightarrow3CO_2+4H_2O
\]

Thứ tự cân bằng không phải luật cứng, nhưng trong phản ứng cháy thường thuận tiện khi xử lý các nguyên tố xuất hiện ít vị trí trước rồi mới tới oxygen và hydrogen.

## Cân bằng như một bài đại số tuyến tính

Mỗi nguyên tố tạo một phương trình bảo toàn tuyến tính. Nếu các hệ số là ẩn số, cân bằng phản ứng có thể được xem như tìm một vector khác 0 trong **không gian nghiệm không (null space)** của ma trận thành phần.

Đây là liên hệ trực tiếp giữa Hóa học và **đại số tuyến tính (linear algebra)**. Phần mềm có thể cân bằng phản ứng bằng khử ma trận thay vì dùng các mẹo ghi nhớ của con người.

## Phương trình ion

Trong hóa học dung dịch nước, **phương trình ion đầy đủ (complete ionic equation)** tách các chất điện ly mạnh tan tốt thành ion.

Các ion xuất hiện không đổi ở cả hai phía gọi là **ion khán (spectator ions)**.

Ví dụ phản ứng kết tủa:

\[
AgNO_3(aq)+NaCl(aq)\rightarrow AgCl(s)+NaNO_3(aq)
\]

Phương trình ion rút gọn:

\[
Ag^+(aq)+Cl^-(aq)\rightarrow AgCl(s)
\]

Dạng ion rút gọn làm lộ sự kiện hóa học cốt lõi thay vì hạch toán cả các ion không trực tiếp tham gia biến đổi.

## Ký hiệu trạng thái

Các ký hiệu `(s)`, `(l)`, `(g)`, `(aq)` chứa thông tin quan trọng. `CaCO3(s)` và các tiểu phần calcium/carbonate trong dung dịch không phải cùng trạng thái vật lý; cân bằng, động học và cơ chế có thể khác.

Trong hóa học thực tế, dung môi và pha có thể quyết định con đường phản ứng, nên ký hiệu trạng thái không phải phần trang trí.

## Phản ứng thuận nghịch

Ký hiệu:

\[
\rightleftharpoons
\]

biểu diễn phản ứng có cả con đường thuận và nghịch đáng kể.

Ở cân bằng, cả hai vẫn diễn ra nhưng thành phần vĩ mô không đổi khi tốc độ hai chiều bằng nhau.

Không nên đọc mũi tên hai chiều như “phản ứng chưa hoàn thành”; nó biểu diễn tính thuận nghịch và hành vi cân bằng.

## Phân loại phản ứng chỉ là cách tổ chức kiến thức

Tổng hợp, phân hủy, cháy, kết tủa, acid–base và oxi hóa–khử là các **nhóm phân loại (taxonomy)** hữu ích, nhưng không nên dùng chúng thay cho cơ chế.

Một phản ứng có thể đồng thời thuộc nhiều nhóm. Ví dụ phản ứng cháy hydrocarbon vừa là phản ứng oxi hóa–khử vừa là một biến đổi hóa học tỏa nhiệt mạnh.

## Các hiểu lầm thường gặp

### “Cân bằng bằng cách đổi chỉ số dưới”

Không được. Đổi chỉ số dưới làm thay đổi bản sắc chất; cân bằng chỉ điều chỉnh hệ số.

### “Phương trình cân bằng cho biết phản ứng chắc chắn xảy ra”

Không. Cân bằng chỉ thỏa điều kiện bảo toàn. Nhiệt động lực học và động học mới quyết định phản ứng có thuận lợi và nhanh hay không.

### “Tỉ lệ hệ số luôn là tỉ lệ khối lượng”

Không. Hệ số cho tỉ lệ số hạt hoặc số mol; muốn đổi sang tỉ lệ khối lượng phải dùng khối lượng mol.

## Mô hình tư duy

Phương trình cân bằng là **hợp đồng bảo toàn** giữa chất phản ứng và sản phẩm. Nó cho phép hạch toán tỉ lệ, nhưng không tự nói phản ứng thuận lợi, nhanh hay hoàn toàn tới mức nào.

Xem tiếp: [Hóa lượng](./03_stoichiometry.md).