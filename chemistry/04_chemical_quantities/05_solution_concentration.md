# Nồng độ dung dịch — các cách định lượng thành phần

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Nồng độ dung dịch — các cách định lượng thành phần**. Route đi từ solute/solvent basis → molarity/molality/mass fraction/ppm → dilution và mixing → temperature/measurement caveats, để chọn thang nồng độ theo câu hỏi và điều kiện đo.

> **Nồng độ (concentration / 농도)** mô tả lượng chất tan tương đối với một lượng dung dịch hoặc dung môi được chọn. Không có một định nghĩa duy nhất; mỗi thang nồng độ được thiết kế cho một kiểu suy luận hoặc thí nghiệm khác nhau.

## Vì sao có nhiều cách biểu diễn nồng độ?

Trong phòng thí nghiệm, thể tích thường dễ đo nên nồng độ mol rất phổ biến. Nhiệt động lực học đôi khi cần đại lượng ít phụ thuộc nhiệt độ hơn nên nồng độ molan hữu ích. Phân tích môi trường có thể dùng phần khối lượng, ppm hoặc ppb. Cân bằng khí–lỏng thường dùng phần mol.

Chọn đơn vị nồng độ là chọn cách biểu diễn phù hợp với bài toán.

> **Chuyển mạch:** Nồng độ mol dùng thể tích dung dịch để tính molarity; molality dùng khối lượng dung môi nên bền hơn trước thay đổi nhiệt độ, tạo nền cho việc chọn thước đo phù hợp.

## Nồng độ mol

**Nồng độ mol (molarity / 몰 농도)**:

\[
M=\frac{n_{chất\ tan}}{V_{dung\ dịch}}
\]

Đơn vị thường là `mol/L`.

Điểm quan trọng: mẫu số là **thể tích cuối của dung dịch**, không phải thể tích dung môi ban đầu.

Ví dụ `0.500 mol NaCl` trong `2.00 L` dung dịch:

\[
M=0.250\,M
\]

Nồng độ mol phụ thuộc nhiệt độ vì thể tích chất lỏng thay đổi do giãn nở nhiệt.

> **Chuyển mạch:** Ở chặng này của **Nồng độ dung dịch — các cách định lượng thành phần**, **Nồng độ molan** tiếp nhận điểm tựa từ **Nồng độ mol** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phần mol** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nồng độ molan

**Nồng độ molan (molality / 몰랄 농도)**:

\[
m=\frac{n_{chất\ tan}}{m_{dung\ môi}(kg)}
\]

Mẫu số là khối lượng dung môi nên molality gần như không phụ thuộc nhiệt độ nếu không mất vật chất.

Các phương trình tính chất tập hợp thường dùng molality vì khối lượng dung môi ổn định hơn thể tích dung dịch theo nhiệt độ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nồng độ dung dịch — các cách định lượng thành phần**, **Phần mol** tiếp nhận điểm tựa từ **Nồng độ molan** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phần khối lượng, phần trăm khối lượng, ppm và ppb** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phần mol

**Phần mol (mole fraction / 몰 분율)**:

\[
x_i=\frac{n_i}{\sum_j n_j}
\]

Phần mol không có đơn vị và tổng các phần mol bằng 1.

Trong hỗn hợp khí lý tưởng:

\[
P_i=x_iP_{total}
\]

Trong dung dịch lỏng, phần mol xuất hiện trong định luật Raoult và các biểu thức thế hóa học.

> **Chuyển mạch:** Trong **Nồng độ dung dịch — các cách định lượng thành phần**, **Phần khối lượng, phần trăm khối lượng, ppm và ppb** tiếp nhận điểm tựa từ **Phần mol** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pha loãng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phần khối lượng, phần trăm khối lượng, ppm và ppb

**Phần khối lượng (mass fraction)**:

\[
w_i=\frac{m_i}{m_{total}}
\]

Phần trăm khối lượng là:

\[
100w_i\%
\]

Với hỗn hợp rất loãng, `ppm` thường biểu diễn phần `10^-6` và `ppb` biểu diễn phần `10^-9`, nhưng cần chỉ rõ cơ sở là khối lượng/khối lượng, thể tích/thể tích hay mol/mol khi ngữ cảnh chưa rõ.

Trong dung dịch nước loãng có khối lượng riêng gần `1.00 kg/L`, `mg/L` đôi khi có giá trị số gần `ppm` theo khối lượng. Đây chỉ là xấp xỉ trong điều kiện phù hợp, không phải đồng nhất thức phổ quát.

> **Chuyển mạch:** Ở chặng này của **Nồng độ dung dịch — các cách định lượng thành phần**, **Pha loãng** tiếp nhận điểm tựa từ **Phần khối lượng, phần trăm khối lượng, ppm và ppb** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pha dung dịch từ chất rắn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pha loãng

Khi chỉ thêm dung môi tinh khiết và lượng chất tan được bảo toàn:

\[
n_{trước}=n_{sau}
\]

Nếu dùng nồng độ mol:

\[
M_1V_1=M_2V_2
\]

Phương trình này không phải một định luật độc lập; nó chỉ là biểu diễn của bảo toàn số mol chất tan dưới giả định không có phản ứng hay thất thoát.

Ví dụ muốn pha `250.0 mL` dung dịch `0.100 M` từ dung dịch gốc `1.00 M`:

\[
V_1=\frac{M_2V_2}{M_1}=25.0\,mL
\]

Lấy `25.0 mL` dung dịch gốc rồi thêm dung môi tới thể tích cuối `250.0 mL`.

Nếu cần độ chính xác cao, không nên đơn giản đo và thêm `225.0 mL` dung môi vì thể tích của các chất lỏng khi trộn không phải lúc nào cũng cộng tuyến tính tuyệt đối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nồng độ dung dịch — các cách định lượng thành phần**, **Pha dung dịch từ chất rắn** tiếp nhận điểm tựa từ **Pha loãng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nồng độ và hoạt độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pha dung dịch từ chất rắn

Muốn pha `V` lít dung dịch có nồng độ mol `M`, cần số mol:

\[
n=MV
\]

Khối lượng chất tan:

\[
m=nM_{molar}
\]

Trong phòng thí nghiệm, thường hòa tan chất rắn trong một phần dung môi trước, chuyển định lượng vào bình định mức rồi thêm dung môi đến vạch hiệu chuẩn.

Cách này kiểm soát thể tích cuối tốt hơn việc đo riêng một thể tích dung môi rồi giả định thể tích sau hòa tan không đổi.

> **Chuyển mạch:** Trong **Nồng độ dung dịch — các cách định lượng thành phần**, **Nồng độ và hoạt độ** tiếp nhận điểm tựa từ **Pha dung dịch từ chất rắn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đo nồng độ trong hóa học phân tích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nồng độ và hoạt độ

Trong dung dịch loãng gần lý tưởng, nồng độ thường là xấp xỉ tốt trong các biểu thức cân bằng. Ở lực ion cao hoặc hệ không lý tưởng, hành vi nhiệt động được mô tả tốt hơn bằng **hoạt độ (activity)**:

\[
a_i=\gamma_i\frac{c_i}{c^\circ}
\]

trong đó `γ_i` là **hệ số hoạt độ (activity coefficient)**.

Điều này giải thích vì sao pH về mặt nhiệt động được định nghĩa qua hoạt độ ion hydrogen, không đơn giản bằng nồng độ mol thô.

> **Chuyển mạch:** Ở chặng này của **Nồng độ dung dịch — các cách định lượng thành phần**, **Đo nồng độ trong hóa học phân tích** tiếp nhận điểm tựa từ **Nồng độ và hoạt độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đo nồng độ trong hóa học phân tích

Nồng độ thường không được “nhìn thấy” trực tiếp mà được suy ra từ một đại lượng có thể đo, chẳng hạn:

- độ hấp thụ theo định luật Beer–Lambert;
- thế điện cực;
- thể tích chất chuẩn độ;
- diện tích đỉnh trong sắc ký;
- tín hiệu khối phổ.

Do đó phép đo nồng độ luôn gắn với mô hình hiệu chuẩn và độ không đảm bảo.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nồng độ dung dịch — các cách định lượng thành phần**, **Các hiểu lầm thường gặp** tiếp nhận điểm tựa từ **Đo nồng độ trong hóa học phân tích** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các hiểu lầm thường gặp

### “1 M nghĩa là 1 mol chất tan trong 1 L dung môi”

Sai. `1 M` nghĩa là 1 mol chất tan trên 1 L **dung dịch**.

### “Công thức pha loãng dùng cho mọi trường hợp trộn”

Không. Nó chỉ áp dụng khi lượng chất tan được bảo toàn và cách định nghĩa nồng độ phù hợp.

### “ppm luôn bằng mg/L”

Chỉ gần đúng trong một số dung dịch nước loãng có khối lượng riêng gần `1 kg/L`.

> **Chuyển mạch:** Trong **Nồng độ dung dịch — các cách định lượng thành phần**, **Mô hình tư duy** gom các mảnh từ **Các hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Nồng độ là **một tỉ số có mẫu số được chọn theo mục đích**. Trước khi tính, luôn hỏi: đại lượng gì nằm ở tử số, đại lượng tham chiếu nào nằm ở mẫu số, và đại lượng đó có thay đổi theo nhiệt độ hoặc quá trình trộn hay không?

Xem tiếp: [Năng lượng, nhiệt và công](../05_thermodynamics/00_energy_heat_and_work.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
