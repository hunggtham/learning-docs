# Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**. Route đi từ oxidation-number diagnosis → half-reaction bookkeeping → môi trường acid/base → ghép electron và kiểm tra atom/charge; kết quả là một phương trình có thể dùng tiếp cho stoichiometry hoặc electrochemistry.

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

Phương pháp bán phản ứng tách lô-gic (logic / 논리) thành:

```text
bảo toàn nguyên tố
→ bảo toàn O/H bằng H2O, H+ hoặc OH−
→ bảo toàn điện tích bằng e−
→ ghép số electron mất = số electron nhận
```

> **Nối mạch:** Redox balancing must conserve atoms, charge and electrons; half-reactions make the bookkeeping explicit, starting by identifying oxidation and reduction before combining them.

## Electron trong bán phản ứng là công cụ ghi sổ

Khi viết:

\[
Fe^{2+}\rightarrow Fe^{3+}+e^-
\]

ta không nhất thiết khẳng định trong dung dịch tồn tại electron tự do lâu dài.

Phương trình chỉ ghi rằng oxidation trạng thái (state / 상태) của Fe tăng và hệ đã mất một electron tương đương.

Trong pin, electron có thể đi qua dây dẫn. Trong phản ứng đồng thể, electron có thể chuyển trực tiếp hoặc qua nhiều bước trung gian.

Vì vậy bán phản ứng là **mô hình hạch toán**, không phải cơ chế đầy đủ.

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Bước 1: xác định quá trình oxy hóa và khử** nối từ **Electron trong bán phản ứng là công cụ ghi sổ** sang **Thuật toán trong môi trường acid**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Trong phản ứng phức tạp hơn, việc xác định oxidation trạng thái (state / 상태) trước giúp nhận ra tiểu phần nào bị oxy hóa và tiểu phần nào bị khử.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Thuật toán trong môi trường acid** nối từ **Bước 1: xác định quá trình oxy hóa và khử** sang **Ví dụ đầy đủ: permanganate và Fe²⁺ trong acid**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Thuật toán trong môi trường acid** nêu quy tắc; **Ví dụ đầy đủ: permanganate và Fe²⁺ trong acid** thử quy tắc trong tình huống, rồi **Vì sao phải cân bằng O và H bằng H₂O/H⁺?** mở rộng hệ quả.

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

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Ví dụ đầy đủ: permanganate và Fe²⁺ trong acid** nêu quy tắc; **Vì sao phải cân bằng O và H bằng H₂O/H⁺?** thử quy tắc trong tình huống, rồi **Môi trường cơ sở (base / 기반)** mở rộng hệ quả.

## Vì sao phải cân bằng O và H bằng H₂O/H⁺?

Trong dung dịch nước acid, nước và proton là các tiểu phần nền có thể tham gia cân bằng nguyên tố.

Ta không “bịa thêm chất” tùy ý. Ta đang viết phản ứng ròng trong một môi trường có sẵn `H2O` và `H+`.

Nếu môi trường khác, sản phẩm và cách cân bằng có thể khác.

Đó là lý do điều kiện phản ứng là một phần của phương trình hóa học thực tế.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Môi trường cơ sở (base / 기반)** nối từ **Vì sao phải cân bằng O và H bằng H₂O/H⁺?** sang **Ví dụ cơ sở (base / 기반): permanganate tạo MnO₂**, vì cơ chế trước tạo đầu vào cho bước sau.

## Môi trường cơ sở (base / 기반)

Cách an toàn nhất:

1. cân bằng như môi trường acid;
2. thêm cùng số `OH−` vào cả hai vế để trung hòa `H+`;
3. chuyển `H+ + OH−` thành `H2O`;
4. rút gọn nước nếu xuất hiện ở cả hai vế.

Cách này tránh học hai thuật toán hoàn toàn tách biệt.

> **Nối mạch:** Trong **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Môi trường cơ sở (base / 기반)** nêu quy tắc; **Ví dụ cơ sở (base / 기반): permanganate tạo MnO₂** thử quy tắc trong tình huống, rồi **Sản phẩm redox phụ thuộc môi trường** mở rộng hệ quả.

## Ví dụ cơ sở (base / 기반): permanganate tạo MnO₂

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

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Ví dụ cơ sở (base / 기반): permanganate tạo MnO₂** nêu quy tắc; **Sản phẩm redox phụ thuộc môi trường** thử quy tắc trong tình huống, rồi **Phương pháp số oxy hóa** mở rộng hệ quả.

## Sản phẩm redox phụ thuộc môi trường

Permanganate là ví dụ rõ:

- trong acid mạnh thường có thể tạo `Mn²⁺`;
- trong điều kiện trung tính hoặc cơ sở (base / 기반) nhẹ có thể tạo `MnO2`;
- trong cơ sở (base / 기반) rất mạnh có thể xuất hiện manganate `MnO4²−` tùy hệ.

Do đó không thể nói một oxidant “luôn nhận đúng cùng số electron” nếu sản phẩm cuối thay đổi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Phương pháp số oxy hóa** nối từ **Sản phẩm redox phụ thuộc môi trường** sang **Khi nào dùng phương pháp nào?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phương pháp số oxy hóa

Một cách khác là theo dõi thay đổi oxidation trạng thái (state / 상태).

Ví dụ carbon trong methane:

\[
CH_4\rightarrow CO_2
\]

C thay đổi:

\[
-4\rightarrow +4
\]

nghĩa là tăng 8 đơn vị oxidation trạng thái (state / 상태) cho mỗi carbon.

Oxygen trong `O2`:

\[
0\rightarrow -2
\]

mỗi O nhận tương đương 2 electron.

Phương pháp số oxy hóa giúp chọn tỷ lệ electron nhanh, nhưng trong phản ứng ion nhiều H/O vẫn cần kiểm tra khối lượng và điện tích.

> **Nối mạch:** Trong **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Khi nào dùng phương pháp nào?** nối từ **Phương pháp số oxy hóa** sang **Disproportionation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khi nào dùng phương pháp nào?

**Phương pháp bán phản ứng** mạnh khi:

- dung dịch ion;
- có H/O;
- acid hoặc cơ sở (base / 기반);
- chuẩn độ redox;
- electrochemistry.

**Phương pháp số oxy hóa** nhanh khi:

- phương trình phân tử tương đối đơn giản;
- thay đổi oxidation trạng thái (state / 상태) rõ;
- ít ion và không cần nhiều bước H/O.

Hai phương pháp dựa trên cùng nguyên lý bảo toàn electron.

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Disproportionation** nối từ **Khi nào dùng phương pháp nào?** sang **Comproportionation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Disproportionation

Trong **phản ứng tự oxy hóa–khử (disproportionation)**, cùng một nguyên tố ở trạng thái ban đầu vừa bị oxy hóa vừa bị khử.

Ví dụ peroxide:

\[
2H_2O_2\rightarrow2H_2O+O_2
\]

Oxygen trong peroxide có số oxy hóa `−1`.

Một phần chuyển xuống `−2` trong nước; phần khác tăng lên `0` trong `O2`.

Phản ứng vẫn cân bằng electron dù donor và acceptor ban đầu nằm trong cùng loại phân tử.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Comproportionation** nối từ **Disproportionation** sang **Electron equivalent**, vì cơ chế trước tạo đầu vào cho bước sau.

## Comproportionation

Chiều ngược là **comproportionation**, khi hai oxidation trạng thái (state / 상태) khác nhau tạo trạng thái trung gian.

Ví dụ tổng quát:

\[
M^{high}+M^{low}\rightarrow 2M^{mid}
\]

Khả năng xảy ra phụ thuộc năng lượng tự do và thế redox của các cặp liên quan.

> **Nối mạch:** Trong **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Electron equivalent** nối từ **Comproportionation** sang **Liên hệ với phương trình Nernst**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Liên hệ với phương trình Nernst** nối từ **Electron equivalent** sang **Liên hệ với sinh học**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Liên hệ với sinh học** nối từ **Liên hệ với phương trình Nernst** sang **Liên hệ với môi trường**, vì cơ chế trước tạo đầu vào cho bước sau.

## Liên hệ với sinh học

Nhiều phản ứng sinh học chuyển hai electron cùng proton, ví dụ các cặp `NAD+/NADH`, quinone/hydroquinone.

Trong protein, electron và proton có thể được ghép theo cơ chế **chuyển proton–electron ghép (proton-coupled electron transfer, PCET)**.

Viết bán phản ứng đúng giúp kiểm tra cân bằng khối lượng, điện tích và proton trong bioenergetics.

> **Nối mạch:** Trong **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Liên hệ với môi trường** nối từ **Liên hệ với sinh học** sang **Liên hệ với hữu cơ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Liên hệ với môi trường

Trong nước tự nhiên, oxygen, nitrate, manganese oxide, iron oxide và sulfate có thể đóng vai trò chất nhận electron ở các vùng redox khác nhau.

Cân bằng bán phản ứng giúp xây dựng các quá trình như:

- nitrification/denitrification;
- khử Fe(III);
- khử sulfate;
- methane formation.

Nhưng cân bằng stoichiometric không tự cho biết quá trình nào xảy ra nhanh hay vi sinh vật nào xúc tác.

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Liên hệ với hữu cơ** nối từ **Liên hệ với môi trường** sang **Cân bằng bằng đại số**, vì cơ chế trước tạo đầu vào cho bước sau.

## Liên hệ với hữu cơ

Trong hóa hữu cơ, oxidation trạng thái (state / 상태) của carbon có thể thay đổi khi:

```text
alcohol → carbonyl → carboxylic acid
```

Dù cơ chế thường được mô tả bằng mũi tên electron cặp và nhóm chức, hạch toán oxidation trạng thái (state / 상태) vẫn giúp nhận biết tổng thể một biến đổi là oxidation hay reduction.

Không nên dùng oxidation trạng thái (state / 상태) thay cho cơ chế hữu cơ; hai lớp thông tin khác nhau.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Cân bằng bằng đại số** nối từ **Liên hệ với hữu cơ** sang **Giới hạn của số oxy hóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cân bằng bằng đại số

Mọi phản ứng có thể được xem là hệ phương trình bảo toàn nguyên tố và điện tích.

Ta có thể tạo ma trận thành phần rồi tìm véc-tơ (vector / 벡터) hệ số trong null không gian (space / 공간).

Với redox, bảo toàn điện tích đã ngầm chứa yêu cầu electron toàn hệ không tự sinh hay mất.

Cách đại số đặc biệt hữu ích trong phần mềm hoặc mạng phản ứng lớn, nhưng phương pháp bán phản ứng thường dễ hiểu hơn cho người học vì làm electron transfer hiện rõ.

> **Nối mạch:** Trong **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Cân bằng bằng đại số** đặt tiêu chí; **Giới hạn của số oxy hóa** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Bán phản ứng không phải cơ chế** mở rộng hệ quả.

## Giới hạn của số oxy hóa

Oxidation trạng thái (state / 상태) là đại lượng hạch toán rất hữu ích nhưng không phải điện tích nguyên tử thực.

Trong:

- hợp chất cộng hóa trị rất phi định xứ;
- cluster kim loại;
- hợp chất organometallic;
- hệ mixed-valence;

việc gán oxidation trạng thái (state / 상태) có thể là mô hình hình thức hơn là mô tả mật độ electron thật.

Phương trình vẫn có thể được cân bằng bằng nguyên tố và điện tích, nhưng không nên suy quá mức từ oxidation trạng thái (state / 상태) sang phân bố electron đo được.

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Giới hạn của số oxy hóa** đặt tiêu chí; **Bán phản ứng không phải cơ chế** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Quy trình kiểm tra cuối** mở rộng hệ quả.

## Bán phản ứng không phải cơ chế

Nếu viết:

\[
MnO_4^-+8H^++5e^-\rightarrow Mn^{2+}+4H_2O
\]

không có nghĩa một ion permanganate nhất thiết nhận đồng thời năm electron trong một va chạm cơ bản.

Cơ chế thật có thể gồm nhiều trạng thái oxy hóa trung gian và nhiều bước proton/electron.

Phương trình bán phản ứng chỉ mô tả **chuyển đổi ròng**.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Bán phản ứng không phải cơ chế** đặt đầu vào cho **Quy trình kiểm tra cuối**, rồi **Các hiểu lầm thường gặp** mở rộng hệ quả hoặc giới hạn liên quan.

## Quy trình kiểm tra cuối

Sau khi cân bằng, luôn kiểm tra bốn lớp:

```text
1. số nguyên tử mỗi nguyên tố
2. tổng điện tích
3. electron mất = electron nhận
4. điều kiện môi trường và trạng thái chất có hợp lý không
```

Nếu dùng cho tính toán định lượng, kiểm tra thêm số electron `n` tương ứng với phương trình đã nhân hệ số.

> **Nối mạch:** Trong **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Quy trình kiểm tra cuối** đặt đầu vào cho **Các hiểu lầm thường gặp**, rồi **Mô hình tư duy** mở rộng hệ quả hoặc giới hạn liên quan.

## Các hiểu lầm thường gặp

### “Electron dùng để cân bằng nguyên tử”

Sai. Electron cân bằng điện tích sau khi nguyên tử đã được cân bằng.

### “Electron trong bán phản ứng phải tồn tại tự do trong dung dịch”

Không. Đó là công cụ hạch toán chuyển electron.

### “Oxidizing tác nhân (agent / 에이전트) luôn nhận cùng số electron”

Không nếu sản phẩm phụ thuộc pH hoặc điều kiện.

### “Một phương trình cân bằng khối lượng thì chắc chắn đúng”

Không. Với ion phải cân bằng cả điện tích.

### “Số oxy hóa là điện tích thật trên nguyên tử”

Không. Nó là quy ước formal để ghi sổ electron.

### “Bán phản ứng mô tả cơ chế elementary”

Không. Nó mô tả biến đổi ròng.

> **Nối mạch:** Ở chặng này của **Cân bằng phản ứng oxy hóa–khử — bảo toàn nguyên tử, điện tích và electron**, **Mô hình tư duy** tổng hợp từ **Các hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

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

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
