# Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron

> Cân bằng phản ứng oxy hóa–khử phải đồng thời thỏa **bảo toàn nguyên tử**, **bảo toàn điện tích** và **bảo toàn electron chuyển giao**. Phương pháp bán phản ứng (half-reaction method / 반쪽 반응법) biến một bài toán phức tạp thành hai bài toán ghi sổ electron rõ ràng rồi ghép chúng lại.

Cân bằng redox không chỉ là kỹ thuật bài tập. Các hệ số thu được quyết định lượng chất trong chuẩn độ, điện phân, pin, ăn mòn, xử lý nước và chuyển hóa sinh học.

## Vì sao phản ứng redox khó cân bằng hơn phản ứng thông thường?

Xét phản ứng permanganate oxy hóa `Fe²⁺` trong môi trường acid. Ta phải đồng thời xử lý:

- manganese;
- oxygen;
- hydrogen;
- điện tích;
- số electron mất và nhận.

Nếu chỉ thử hệ số bằng mắt, rất dễ cân bằng đúng nguyên tử nhưng sai điện tích.

Phương pháp bán phản ứng tách logic thành:

```text
bảo toàn nguyên tố
→ bảo toàn O/H bằng H2O, H+ hoặc OH−
→ bảo toàn điện tích bằng e−
→ ghép số electron mất = số electron nhận
```

## Electron trong bán phản ứng là công cụ ghi sổ

Khi viết:

\[
Fe^{2+}\rightarrow Fe^{3+}+e^-
\]

ta không nhất thiết khẳng định trong dung dịch tồn tại electron tự do lâu dài.

Phương trình chỉ ghi rằng oxidation state của Fe tăng và hệ đã mất một electron tương đương.

Trong pin, electron có thể đi qua dây dẫn. Trong phản ứng đồng thể, electron có thể chuyển trực tiếp hoặc qua nhiều bước trung gian.

Vì vậy bán phản ứng là **mô hình hạch toán**, không phải cơ chế đầy đủ.

## Bước 1: xác định quá trình oxy hóa và khử

Ví dụ:

\[
Zn+Cu^{2+}\rightarrow Zn^{2+}+Cu
\]

Kẽm:

\[
Zn\rightarrow Zn^{2+}+2e^-
\]

Đồng:

\[
Cu^{2+}+2e^-\rightarrow Cu
\]

Electron mất và nhận đã bằng nhau nên cộng hai bán phản ứng cho phương trình tổng.

Trong phản ứng phức tạp hơn, việc xác định oxidation state trước giúp nhận ra tiểu phần nào bị oxy hóa và tiểu phần nào bị khử.

## Thuật toán trong môi trường acid

Một quy trình chắc chắn:

1. tách phản ứng thành hai bán phản ứng;
2. cân bằng các nguyên tố ngoài H và O;
3. cân bằng O bằng `H2O`;
4. cân bằng H bằng `H+`;
5. cân bằng điện tích bằng `e−`;
6. nhân các bán phản ứng để số electron bằng nhau;
7. cộng và rút gọn;
8. kiểm tra lại nguyên tử và điện tích.

Điều quan trọng là hiểu từng bước đều xuất phát từ một định luật bảo toàn.

## Ví dụ đầy đủ: permanganate và Fe²⁺ trong acid

Bán phản ứng khử:

\[
MnO_4^-\rightarrow Mn^{2+}
\]

Manganese đã cân bằng.

Cân bằng oxygen bằng nước:

\[
MnO_4^-\rightarrow Mn^{2+}+4H_2O
\]

Cân bằng hydrogen bằng proton:

\[
8H^++MnO_4^-\rightarrow Mn^{2+}+4H_2O
\]

Điện tích vế trái là `+7`, vế phải `+2`. Thêm năm electron vào vế trái:

\[
8H^++MnO_4^-+5e^-
\rightarrow Mn^{2+}+4H_2O
\]

Bán phản ứng oxy hóa:

\[
Fe^{2+}\rightarrow Fe^{3+}+e^-
\]

Nhân bán phản ứng sắt với 5 rồi cộng:

\[
8H^++MnO_4^-+5Fe^{2+}
\rightarrow Mn^{2+}+4H_2O+5Fe^{3+}
\]

Kiểm tra điện tích:

```text
trái: +8 -1 +10 = +17
phải: +2 +15 = +17
```

Phương trình thỏa cả bảo toàn nguyên tử lẫn điện tích.

## Vì sao phải cân bằng O và H bằng H₂O/H⁺?

Trong dung dịch nước acid, nước và proton là các tiểu phần nền có thể tham gia cân bằng nguyên tố.

Ta không “bịa thêm chất” tùy ý. Ta đang viết phản ứng ròng trong một môi trường có sẵn `H2O` và `H+`.

Nếu môi trường khác, sản phẩm và cách cân bằng có thể khác.

Đó là lý do điều kiện phản ứng là một phần của phương trình hóa học thực tế.

## Môi trường base

Cách an toàn nhất:

1. cân bằng như môi trường acid;
2. thêm cùng số `OH−` vào cả hai vế để trung hòa `H+`;
3. chuyển `H+ + OH−` thành `H2O`;
4. rút gọn nước nếu xuất hiện ở cả hai vế.

Cách này tránh học hai thuật toán hoàn toàn tách biệt.

## Ví dụ base: permanganate tạo MnO₂

Xét bán phản ứng:

\[
MnO_4^-\rightarrow MnO_2
\]

Cân bằng trong acid trước:

\[
MnO_4^-+4H^++3e^-
\rightarrow MnO_2+2H_2O
\]

Thêm `4OH−` hai phía:

\[
MnO_4^-+4H^++4OH^-+3e^-
\rightarrow MnO_2+2H_2O+4OH^-
\]

Gộp `H+ + OH−`:

\[
MnO_4^-+4H_2O+3e^-
\rightarrow MnO_2+2H_2O+4OH^-
\]

Rút gọn nước:

\[
MnO_4^-+2H_2O+3e^-
\rightarrow MnO_2+4OH^-
\]

Kiểm tra điện tích hai vế đều bằng `−4`.

## Sản phẩm redox phụ thuộc môi trường

Permanganate là ví dụ rõ:

- trong acid mạnh thường có thể tạo `Mn²⁺`;
- trong điều kiện trung tính hoặc base nhẹ có thể tạo `MnO2`;
- trong base rất mạnh có thể xuất hiện manganate `MnO4²−` tùy hệ.

Do đó không thể nói một oxidant “luôn nhận đúng cùng số electron” nếu sản phẩm cuối thay đổi.

## Phương pháp số oxy hóa

Một cách khác là theo dõi thay đổi oxidation state.

Ví dụ carbon trong methane:

\[
CH_4\rightarrow CO_2
\]

C thay đổi:

\[
-4\rightarrow +4
\]

nghĩa là tăng 8 đơn vị oxidation state cho mỗi carbon.

Oxygen trong `O2`:

\[
0\rightarrow -2
\]

mỗi O nhận tương đương 2 electron.

Phương pháp số oxy hóa giúp chọn tỷ lệ electron nhanh, nhưng trong phản ứng ion nhiều H/O vẫn cần kiểm tra khối lượng và điện tích.

## Khi nào dùng phương pháp nào?

**Phương pháp bán phản ứng** mạnh khi:

- dung dịch ion;
- có H/O;
- acid hoặc base;
- chuẩn độ redox;
- electrochemistry.

**Phương pháp số oxy hóa** nhanh khi:

- phương trình phân tử tương đối đơn giản;
- thay đổi oxidation state rõ;
- ít ion và không cần nhiều bước H/O.

Hai phương pháp dựa trên cùng nguyên lý bảo toàn electron.

## Disproportionation

Trong **phản ứng tự oxy hóa–khử (disproportionation)**, cùng một nguyên tố ở trạng thái ban đầu vừa bị oxy hóa vừa bị khử.

Ví dụ peroxide:

\[
2H_2O_2\rightarrow2H_2O+O_2
\]

Oxygen trong peroxide có số oxy hóa `−1`.

Một phần chuyển xuống `−2` trong nước; phần khác tăng lên `0` trong `O2`.

Phản ứng vẫn cân bằng electron dù donor và acceptor ban đầu nằm trong cùng loại phân tử.

## Comproportionation

Chiều ngược là **comproportionation**, khi hai oxidation state khác nhau tạo trạng thái trung gian.

Ví dụ tổng quát:

\[
M^{high}+M^{low}\rightarrow 2M^{mid}
\]

Khả năng xảy ra phụ thuộc năng lượng tự do và thế redox của các cặp liên quan.

## Electron equivalent

Trong chuẩn độ redox, đôi khi hữu ích khi nghĩ theo **đương lượng electron (electron equivalent)**.

Nếu một mol chất nhận `z` mol electron:

\[
n_{e^-}=z\,n_{chất}
\]

Điều này nối trực tiếp phản ứng redox với điện lượng:

\[
Q=n_{e^-}F
\]

Do đó cùng hệ số electron được dùng trong:

- chuẩn độ;
- coulometry;
- điện phân;
- pin.

## Liên hệ với phương trình Nernst

Trong electrochemistry, bán phản ứng không chỉ dùng để cân bằng.

Số electron `n` xuất hiện trong:

\[
\Delta G=-nFE
\]

và phương trình Nernst:

\[
E=E^\circ-\frac{RT}{nF}\ln Q
\]

Nếu cân bằng sai số electron, điện thế và năng lượng tự do tính ra cũng sai.

Vì vậy hạch toán electron là cầu nối giữa stoichiometry và thermodynamics điện hóa.

## Liên hệ với sinh học

Nhiều phản ứng sinh học chuyển hai electron cùng proton, ví dụ các cặp `NAD+/NADH`, quinone/hydroquinone.

Trong protein, electron và proton có thể được ghép theo cơ chế **chuyển proton–electron ghép (proton-coupled electron transfer, PCET)**.

Viết bán phản ứng đúng giúp kiểm tra cân bằng khối lượng, điện tích và proton trong bioenergetics.

## Liên hệ với môi trường

Trong nước tự nhiên, oxygen, nitrate, manganese oxide, iron oxide và sulfate có thể đóng vai trò chất nhận electron ở các vùng redox khác nhau.

Cân bằng bán phản ứng giúp xây dựng các quá trình như:

- nitrification/denitrification;
- khử Fe(III);
- khử sulfate;
- methane formation.

Nhưng cân bằng stoichiometric không tự cho biết quá trình nào xảy ra nhanh hay vi sinh vật nào xúc tác.

## Liên hệ với hữu cơ

Trong hóa hữu cơ, oxidation state của carbon có thể thay đổi khi:

```text
alcohol → carbonyl → carboxylic acid
```

Dù cơ chế thường được mô tả bằng mũi tên electron cặp và nhóm chức, hạch toán oxidation state vẫn giúp nhận biết tổng thể một biến đổi là oxidation hay reduction.

Không nên dùng oxidation state thay cho cơ chế hữu cơ; hai lớp thông tin khác nhau.

## Cân bằng bằng đại số

Mọi phản ứng có thể được xem là hệ phương trình bảo toàn nguyên tố và điện tích.

Ta có thể tạo ma trận thành phần rồi tìm vector hệ số trong null space.

Với redox, bảo toàn điện tích đã ngầm chứa yêu cầu electron toàn hệ không tự sinh hay mất.

Cách đại số đặc biệt hữu ích trong phần mềm hoặc mạng phản ứng lớn, nhưng phương pháp bán phản ứng thường dễ hiểu hơn cho người học vì làm electron transfer hiện rõ.

## Giới hạn của số oxy hóa

Oxidation state là đại lượng hạch toán rất hữu ích nhưng không phải điện tích nguyên tử thực.

Trong:

- hợp chất cộng hóa trị rất phi định xứ;
- cluster kim loại;
- hợp chất organometallic;
- hệ mixed-valence;

việc gán oxidation state có thể là mô hình hình thức hơn là mô tả mật độ electron thật.

Phương trình vẫn có thể được cân bằng bằng nguyên tố và điện tích, nhưng không nên suy quá mức từ oxidation state sang phân bố electron đo được.

## Bán phản ứng không phải cơ chế

Nếu viết:

\[
MnO_4^-+8H^++5e^-\rightarrow Mn^{2+}+4H_2O
\]

không có nghĩa một ion permanganate nhất thiết nhận đồng thời năm electron trong một va chạm cơ bản.

Cơ chế thật có thể gồm nhiều trạng thái oxy hóa trung gian và nhiều bước proton/electron.

Phương trình bán phản ứng chỉ mô tả **chuyển đổi ròng**.

## Quy trình kiểm tra cuối

Sau khi cân bằng, luôn kiểm tra bốn lớp:

```text
1. số nguyên tử mỗi nguyên tố
2. tổng điện tích
3. electron mất = electron nhận
4. điều kiện môi trường và trạng thái chất có hợp lý không
```

Nếu dùng cho tính toán định lượng, kiểm tra thêm số electron `n` tương ứng với phương trình đã nhân hệ số.

## Các hiểu lầm thường gặp

### “Electron dùng để cân bằng nguyên tử”

Sai. Electron cân bằng điện tích sau khi nguyên tử đã được cân bằng.

### “Electron trong bán phản ứng phải tồn tại tự do trong dung dịch”

Không. Đó là công cụ hạch toán chuyển electron.

### “Oxidizing agent luôn nhận cùng số electron”

Không nếu sản phẩm phụ thuộc pH hoặc điều kiện.

### “Một phương trình cân bằng khối lượng thì chắc chắn đúng”

Không. Với ion phải cân bằng cả điện tích.

### “Số oxy hóa là điện tích thật trên nguyên tử”

Không. Nó là quy ước formal để ghi sổ electron.

### “Bán phản ứng mô tả cơ chế elementary”

Không. Nó mô tả biến đổi ròng.

## Mô hình tư duy

Cân bằng redox là **kế toán kép của vật chất và electron**.

```text
nguyên tử không mất
điện tích không mất
mỗi electron donor mất
= mỗi electron acceptor nhận
```

Sau khi phương trình đã đúng, cùng bộ hệ số electron đó tiếp tục đi vào stoichiometry, Nernst, `ΔG=-nFE`, điện phân và phân tích định lượng.

Xem tiếp: [Pin Galvani](./02_galvanic_cells.md), [Điện thế pin và Nernst](./03_cell_potential_and_nernst_equation.md) và [Điện phân](./04_electrolysis.md).