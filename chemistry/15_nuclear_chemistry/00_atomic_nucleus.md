# Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Hạt nhân không phải một quả cầu rắn thu nhỏ** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Ký hiệu hạt nhân** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **Hạt nhân nguyên tử (atomic nucleus / 원자핵)** chứa proton và neutron, gọi chung là **nucleon (핵자)**. Hóa học hạt nhân bắt đầu khi thang năng lượng chuyển từ các trạng thái electron cỡ eV sang các quá trình hạt nhân cỡ keV–MeV. Ở thang này, tương tác hạt nhân mạnh, lực Coulomb và cấu trúc lượng tử của nucleon cùng quyết định độ bền của nuclide.

Trước khi đi sâu, nên nối lại ba prerequisite:

- [nguyên tử, nguyên tố và đồng vị](../01_atomic_structure/00_atoms_elements_and_isotopes.md) để hiểu `Z`, `N`, `A` và nuclide;
- [mô hình lượng tử của nguyên tử](../01_atomic_structure/02_quantum_model_of_atom.md) để nhớ tư duy trạng thái lượng tử/lớp năng lượng;
- [bức xạ và lượng tử hóa](../01_atomic_structure/01_electromagnetic_radiation_and_quantization.md) để hiểu photon gamma và chênh lệch năng lượng.

Các mô hình hạt nhân không phải bản sao của mô hình electron. Chúng dùng cùng ngôn ngữ lượng tử nhưng với hạt, tương tác và thang năng lượng khác.

## Hạt nhân không phải một quả cầu rắn thu nhỏ

Hạt nhân là hệ nhiều hạt lượng tử hữu hạn. Nucleon chiếm các trạng thái lượng tử, tương tác tập thể và có thể tạo cấu trúc lớp, hình dạng biến dạng hoặc trạng thái kích thích.

Hai mô hình quan trọng là:

- **mô hình giọt lỏng (liquid-drop model)** — mạnh khi mô tả xu hướng tập thể và năng lượng liên kết;
- **mô hình lớp hạt nhân (nuclear shell model)** — mạnh khi mô tả lớp đóng, spin và số ma thuật.

Không mô hình nào bao phủ hoàn hảo mọi hạt nhân.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Ký hiệu hạt nhân** tiếp nhận điểm tựa từ **Hạt nhân không phải một quả cầu rắn thu nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao neutron quan trọng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ký hiệu hạt nhân

Một nuclide được viết:

\[
{}^A_ZX
\]

với:

- `Z`: số proton, đồng thời là số hiệu nguyên tử;
- `N`: số neutron;
- `A = Z + N`: số khối.

Bản sắc nguyên tố được quyết định bởi `Z`. Đồng vị có cùng `Z` nhưng khác `N`.

> **Chuyển mạch:** Ở chặng này của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Vì sao neutron quan trọng?** tiếp nhận điểm tựa từ **Ký hiệu hạt nhân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bán kính hạt nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao neutron quan trọng?

Proton đẩy nhau bằng lực Coulomb. Tương tác hạt nhân mạnh lại tạo lực hút hiệu dụng giữa các nucleon ở khoảng cách rất ngắn.

Neutron góp phần vào liên kết mạnh nhưng không làm lực đẩy Coulomb tăng.

Vì vậy khi `Z` tăng, các hạt nhân bền thường cần tỷ lệ `N/Z` lớn dần.

Hạt nhân quá giàu neutron hoặc quá giàu proton có xu hướng biến đổi theo những con đường làm năng lượng tổng giảm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Bán kính hạt nhân** tiếp nhận điểm tựa từ **Vì sao neutron quan trọng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khuyết khối và năng lượng liên kết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bán kính hạt nhân

Quan hệ thực nghiệm gần đúng:

\[
R\approx R_0A^{1/3}
\]

với:

\[
R_0\sim1.2\,\mathrm{fm}
\]

Do đó thể tích hạt nhân tăng gần tỷ lệ với `A`, gợi ý mật độ hạt nhân xấp xỉ không đổi cho nhiều nuclide.

Bán kính nguyên tử lớn hơn bán kính hạt nhân khoảng năm bậc độ lớn theo chiều dài, nên hạt nhân chứa gần toàn bộ khối lượng nhưng chiếm phần cực nhỏ thể tích nguyên tử.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, sau nội dung của **Bán kính hạt nhân**, **Khuyết khối và năng lượng liên kết** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Năng lượng liên kết trên mỗi nucleon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khuyết khối và năng lượng liên kết

Khối lượng hạt nhân liên kết nhỏ hơn tổng khối lượng proton và neutron tự do tương ứng:

\[
\Delta m=Zm_p+Nm_n-m_{nucleus}
\]

Chênh lệch này tương ứng với **năng lượng liên kết hạt nhân (nuclear binding energy)**:

\[
E_b=\Delta mc^2
\]

Không phải vật chất “biến mất”. Hệ liên kết có năng lượng tổng thấp hơn, và trong thuyết tương đối năng lượng chênh lệch được phản ánh bằng chênh lệch khối lượng.

> **Chuyển mạch:** Ở chặng này của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Năng lượng liên kết trên mỗi nucleon** tiếp nhận điểm tựa từ **Khuyết khối và năng lượng liên kết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình khối lượng bán thực nghiệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lượng liên kết trên mỗi nucleon

Đại lượng:

\[
\frac{E_b}{A}
\]

cho biết mức liên kết trung bình trên mỗi nucleon.

Đường cong tăng nhanh với hạt nhân nhẹ, đạt vùng cực đại gần Fe/Ni rồi giảm từ từ với hạt nhân rất nặng.

Điều này giải thích hai con đường giải phóng năng lượng:

```text
hạt nhân nhẹ
→ fusion
→ tiến về vùng liên kết mạnh hơn trên mỗi nucleon

hạt nhân rất nặng
→ fission
→ tiến về vùng liên kết mạnh hơn trên mỗi nucleon
```

Nhiệt hạch và phân hạch vì vậy không phải hai ngoại lệ rời rạc; chúng là hai phía của cùng một cảnh quan năng lượng liên kết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Mô hình khối lượng bán thực nghiệm** tiếp nhận điểm tựa từ **Năng lượng liên kết trên mỗi nucleon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thung lũng bền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình khối lượng bán thực nghiệm

Mô hình giọt lỏng tách năng lượng liên kết thành các đóng góp cạnh tranh:

```text
+ ổn định thể tích
− chi phí bề mặt
− lực đẩy Coulomb
− chi phí mất cân bằng neutron/proton
± hiệu ứng ghép cặp
```

Mô hình mô tả tốt xu hướng lớn nhưng không giải thích đầy đủ hiệu ứng lớp lượng tử.

### Thành phần thể tích

Tương tác mạnh có tầm ngắn nên mỗi nucleon chủ yếu tương tác với các hàng xóm gần.

Số tương tác hữu ích tăng gần tỷ lệ với `A`.

### Thành phần bề mặt

Nucleon ở bề mặt có ít hàng xóm hơn, nên mức liên kết giảm.

Số nucleon bề mặt tăng gần theo `A^(2/3)`.

### Thành phần Coulomb

Lực đẩy proton–proton tăng khi `Z` lớn. Với hạt nhân nặng, đóng góp Coulomb tích lũy trở thành yếu tố gây mất ổn định quan trọng.

### Thành phần bất đối xứng

Proton và neutron là fermion nên phải tuân Pauli.

Nếu một loại nucleon quá dư thừa, nó phải chiếm trạng thái năng lượng cao hơn. Điều này tạo chi phí năng lượng cho mất cân bằng `N/Z`.

### Thành phần ghép cặp

Các nuclide chẵn–chẵn thường bền hơn các trường hợp lẻ–lẻ tương ứng.

Đây là hiệu ứng ghép cặp lượng tử giữa nucleon, không phải “keo dính đôi” theo nghĩa cổ điển.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Thung lũng bền** tiếp nhận điểm tựa từ **Mô hình khối lượng bán thực nghiệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Số ma thuật và bằng chứng cho cấu trúc lớp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thung lũng bền

Nếu biểu diễn `N` theo `Z`, các nuclide bền tạo thành một dải gọi là **thung lũng bền (valley of stability)**.

Hạt nhân nhẹ bền thường có `N ≈ Z`; hạt nhân nặng bền cần `N > Z`.

Nuclide lệch khỏi vùng này thường có thể phân rã beta theo chiều làm tỉ lệ neutron/proton thuận lợi hơn.

> **Chuyển mạch:** Ở chặng này của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Thung lũng bền** nêu điều cần giải thích; **Số ma thuật và bằng chứng cho cấu trúc lớp** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình lớp hạt nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Số ma thuật và bằng chứng cho cấu trúc lớp

Các số proton hoặc neutron:

```text
2, 8, 20, 28, 50, 82, 126
```

liên hệ với độ bền tăng và được gọi là **số ma thuật (magic numbers / 마법수)**.

Chúng gợi ý nucleon cũng tạo các lớp lượng tử đóng.

Tương tự electron ở chỗ đều có trạng thái lượng tử, nhưng thế năng, tương tác spin–quỹ đạo và tương tác giữa hạt hoàn toàn khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Số ma thuật và bằng chứng cho cấu trúc lớp** nêu điều cần giải thích; **Mô hình lớp hạt nhân** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Chuyển động tập thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình lớp hạt nhân

Trong **mô hình lớp hạt nhân**, nucleon chuyển động trong một trường hiệu dụng trung bình và chiếm các orbital lượng tử.

Tương tác spin–quỹ đạo mạnh góp phần tạo thứ tự mức năng lượng phù hợp với các số ma thuật quan sát được.

Các lớp đóng thường liên hệ với độ bền cao và cấu trúc gần cầu hơn.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Chuyển động tập thể** tiếp nhận điểm tựa từ **Mô hình lớp hạt nhân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Spin hạt nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển động tập thể

Một số hạt nhân bị biến dạng và có các mức kích thích quay hoặc dao động.

Mô hình tập thể kết hợp hai trực giác:

```text
chuyển động hạt đơn
+
chuyển động phối hợp của toàn hạt nhân
```

Điều này giải thích vì sao không thể chỉ dùng một mô hình “nucleon độc lập” cho mọi trạng thái.

> **Chuyển mạch:** Ở chặng này của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Spin hạt nhân** tiếp nhận điểm tựa từ **Chuyển động tập thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trạng thái kích thích và photon gamma** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spin hạt nhân

Tổng mômen động lượng của các nucleon tạo **spin hạt nhân (nuclear spin)**, ký hiệu thường là `I`.

Hạt nhân có spin khác 0 có mômen từ và tương tác với từ trường ngoài.

Đây là nền của NMR và MRI. Trong NMR, người ta khai thác chênh lệch năng lượng spin mà không biến đổi hạt nhân sang nguyên tố khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Trạng thái kích thích và photon gamma** tiếp nhận điểm tựa từ **Spin hạt nhân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đồng phân hạt nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái kích thích và photon gamma

Hạt nhân có thể ở trạng thái kích thích:

\[
{}^A_ZX^*\rightarrow{}^A_ZX+\gamma
\]

Phát gamma làm năng lượng giảm nhưng không đổi `Z` hay `A`.

Photon gamma có năng lượng lớn hơn nhiều photon thường gặp trong hóa học phân tử, phản ánh chênh mức hạt nhân lớn hơn chênh mức electron hóa trị.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Đồng phân hạt nhân** tiếp nhận điểm tựa từ **Trạng thái kích thích và photon gamma** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân rã là quá trình xác suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồng phân hạt nhân

Một số trạng thái kích thích có thời gian sống tương đối dài và được gọi là **đồng phân hạt nhân (nuclear isomer / 핵 이성질체)**.

Technetium-99m là ví dụ quan trọng trong y học hạt nhân vì trạng thái siêu bền phát gamma hữu ích cho chẩn đoán trước khi chuyển về mức thấp hơn.

> **Chuyển mạch:** Ở chặng này của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Phân rã là quá trình xác suất** tiếp nhận điểm tựa từ **Đồng phân hạt nhân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao hạt nhân nặng khó bền?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân rã là quá trình xác suất

Một hạt nhân đơn lẻ không có “đồng hồ” cho biết chính xác khi nào phân rã.

Mỗi hạt nhân có xác suất phân rã trên đơn vị thời gian được đặc trưng bởi hằng số phân rã.

Do đó:

```text
một hạt riêng lẻ → thời điểm phân rã không dự đoán chính xác
quần thể lớn      → quy luật thống kê rất chính xác
```

Phần toán học của phân rã mũ được phát triển ở [Phóng xạ](./01_radioactivity.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Vì sao hạt nhân nặng khó bền?** tiếp nhận điểm tựa từ **Phân rã là quá trình xác suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao hóa học thông thường hầu như không đổi tốc độ phân rã?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao hạt nhân nặng khó bền?

Tương tác mạnh tạo lực hút lớn nhưng có tầm ngắn.

Lực Coulomb giữa proton có tầm xa hơn trong phạm vi hạt nhân và tích lũy theo số proton.

Khi `Z` tăng, chi phí Coulomb tăng trong khi mỗi nucleon chỉ hưởng tương tác mạnh với số hàng xóm hữu hạn.

Đây là một trong những lý do làm hạt nhân rất nặng trở nên dễ phân hạch hoặc phân rã hơn.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Vì sao hóa học thông thường hầu như không đổi tốc độ phân rã?** tiếp nhận điểm tựa từ **Vì sao hạt nhân nặng khó bền?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đồng vị và hiệu ứng đồng vị hóa học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao hóa học thông thường hầu như không đổi tốc độ phân rã?

Phản ứng hóa học tái sắp xếp electron hóa trị ở thang eV.

Chuyển mức hạt nhân thường ở keV–MeV, lớn hơn nhiều.

Do đó thay đổi liên kết hóa học thường chỉ ảnh hưởng rất nhỏ tới phân rã hạt nhân.

Một ngoại lệ đáng chú ý là **bắt electron (electron capture)**, nơi mật độ electron gần hạt nhân có thể tạo hiệu ứng nhỏ nhưng đo được.

> **Chuyển mạch:** Ở chặng này của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Đồng vị và hiệu ứng đồng vị hóa học** tiếp nhận điểm tựa từ **Vì sao hóa học thông thường hầu như không đổi tốc độ phân rã?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết hạt nhân và nguồn gốc nguyên tố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồng vị và hiệu ứng đồng vị hóa học

Các đồng vị cùng nguyên tố có cấu trúc electron gần giống nhau nhưng khác khối lượng.

Khác biệt khối lượng làm tần số dao động thay đổi và có thể ảnh hưởng tốc độ phản ứng.

Hydrogen/deuterium cho hiệu ứng đặc biệt rõ vì tỷ lệ khối lượng thay đổi lớn.

Xem thêm [hiệu ứng đồng vị động học trong cơ chế phản ứng](../06_chemical_kinetics/02_reaction_mechanisms.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Đồng vị và hiệu ứng đồng vị hóa học** nêu điều cần giải thích; **Liên kết hạt nhân và nguồn gốc nguyên tố** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ví dụ suy luận: vì sao fusion H có thể giải phóng năng lượng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết hạt nhân và nguồn gốc nguyên tố

Các ngôi sao tổng hợp hạt nhân nhẹ qua nhiệt hạch và các chuỗi bắt hạt.

Các nguyên tố nặng hơn vùng Fe/Ni cần các môi trường giàu neutron/proton hoặc sự kiện thiên văn năng lượng cao để xây dựng hạt nhân nặng rồi phân rã về các nuclide bền hơn.

Hóa học hạt nhân vì vậy nối trực tiếp với nguồn gốc nguyên tố trong vũ trụ.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Liên kết hạt nhân và nguồn gốc nguyên tố** cho ta quy tắc; **Ví dụ suy luận: vì sao fusion H có thể giải phóng năng lượng?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ví dụ suy luận: vì sao uranium có thể phân hạch còn iron thì không giải phóng năng lượng theo cùng cách?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ suy luận: vì sao fusion H có thể giải phóng năng lượng?

Các nucleon ban đầu ở hạt nhân rất nhẹ có năng lượng liên kết trên nucleon thấp hơn sản phẩm như helium.

Nếu sản phẩm có tổng năng lượng thấp hơn, phần chênh lệch xuất hiện dưới dạng động năng/bức xạ.

Không phải “do tạo hạt nhân lớn hơn” nói chung; động lực đến từ **đi về vùng binding năng lượng (energy / 에너지) per nucleon cao hơn**.

> **Chuyển mạch:** Ở chặng này của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Ví dụ suy luận: vì sao fusion H có thể giải phóng năng lượng?** cho ta quy tắc; **Ví dụ suy luận: vì sao uranium có thể phân hạch còn iron thì không giải phóng năng lượng theo cùng cách?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Những hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ suy luận: vì sao uranium có thể phân hạch còn iron thì không giải phóng năng lượng theo cùng cách?

Uranium nằm phía hạt nhân nặng của đường cong liên kết. Tách nó thành các mảnh trung bình có thể tăng năng lượng liên kết trên nucleon.

Iron/Ni đã gần đỉnh đường cong. Tách chúng thành hạt nhân nhỏ hơn thường không cho cùng lợi ích năng lượng.

Đây là lý do đường cong `Eb/A`, chứ không phải nhãn “nặng/nhẹ”, mới là mô hình tư duy (mental model / 사고 모델) nền.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Ví dụ suy luận: vì sao uranium có thể phân hạch còn iron thì không giải phóng năng lượng theo cùng cách?** cho ta quy tắc; **Những hiểu lầm thường gặp** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm thường gặp

### “Hạt nhân chiếm phần lớn thể tích nguyên tử”

Không. Hạt nhân chứa gần toàn bộ khối lượng nhưng chỉ chiếm phần rất nhỏ thể tích.

### “Neutron chỉ là keo trung hòa”

Không. Neutron tham gia đầy đủ vào cấu trúc lượng tử và tương tác mạnh.

### “Khuyết khối nghĩa là vật chất biến mất”

Không. Chênh lệch năng lượng liên kết được phản ánh thành chênh lệch khối lượng theo `E = mc²`.

### “Số ma thuật là số lớp electron”

Không. Đây là lớp đóng của nucleon với vật lý khác electron nguyên tử.

### “Mọi hạt nhân nặng đều tự phân hạch ngay”

Không. Tính thuận lợi năng lượng và hàng rào phân hạch là hai câu hỏi khác nhau; hạt nhân có thể metastable trong thời gian rất dài.

> **Chuyển mạch:** Trong **Hạt nhân nguyên tử — liên kết, độ bền và cấu trúc vượt ngoài electron**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Hãy xem hạt nhân như **một hệ nhiều fermion mật độ cao, nơi lực hút mạnh tầm ngắn cạnh tranh với Coulomb và ràng buộc lượng tử**:

```text
Z + N
→ cấu trúc lớp + pairing
→ binding energy
→ vị trí so với valley of stability
→ trạng thái bền / kích thích / phân rã
```

Năng lượng liên kết và cấu trúc lớp quyết định nuclide nào tồn tại lâu; động học phân rã quyết định chúng tồn tại lâu đến mức nào.

Xem tiếp: [Phóng xạ](./01_radioactivity.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
