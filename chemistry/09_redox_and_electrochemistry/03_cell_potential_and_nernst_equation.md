# Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao phản ứng oxy hóa-khử tạo ra điện áp** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Điện thế chuẩn** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **Điện thế pin (cell potential / 전지 전위)** không phải một con số tách rời khỏi nhiệt động lực học. Nó biểu diễn mức công điện có thể thu được từ một phản ứng oxy hóa-khử. **Phương trình Nernst (Nernst equation / 네른스트 식)** mở rộng điện thế chuẩn sang điều kiện không chuẩn bằng cách đưa thương số phản ứng và hoạt độ vào mô hình.

## Vì sao phản ứng oxy hóa-khử tạo ra điện áp

Nếu oxy hóa và khử xảy ra trực tiếp trong cùng một bình, electron vẫn được truyền nhưng rất khó khai thác thành công điện có kiểm soát. Pin điện hóa tách hai bán phản ứng và buộc electron đi qua mạch ngoài.

Điện áp xuất hiện vì electron có thế hóa học hoặc thế điện hóa khác nhau tại hai điện cực. Mạch ngoài cho phép hệ giảm năng lượng tự do Gibbs bằng cách dịch chuyển điện tích có kiểm soát.

Mối liên hệ nền tảng là:

\[
\Delta G=-nFE
\]

trong đó:

- \(n\) là số mol electron được trao đổi theo phương trình đã cân bằng;
- \(F\) là hằng số Faraday;
- \(E\) là điện thế pin.

Nếu \(E>0\), phản ứng theo chiều đã viết có \(\Delta G<0\) và thuận lợi về mặt nhiệt động trong điều kiện đang xét.

> **Chuyển mạch:** Trong **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Điện thế chuẩn** tiếp nhận điểm tựa từ **Vì sao phản ứng oxy hóa-khử tạo ra điện áp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Suy ra phương trình Nernst** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điện thế chuẩn

Ở trạng thái chuẩn:

\[
\Delta G^\circ=-nFE^\circ
\]

Các **thế khử chuẩn (standard reduction potential)** được lập bảng tương đối so với điện cực hydro chuẩn. Vì chỉ đo được hiệu điện thế nên thế tuyệt đối của một điện cực đơn không thể được đo độc lập theo cách trực tiếp.

Điện thế chuẩn của pin:

\[
E^\circ_{cell}=E^\circ_{cathode}-E^\circ_{anode}
\]

Điều quan trọng là không nhân thế điện cực với hệ số hóa lượng. Điện thế là đại lượng cường độ; năng lượng tự do mới tăng theo lượng chất phản ứng.

> **Chuyển mạch:** Ở chặng này của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Suy ra phương trình Nernst** tiếp nhận điểm tựa từ **Điện thế chuẩn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thương số phản ứng phải dùng hoạt độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suy ra phương trình Nernst

Nhiệt động lực học cho:

\[
\Delta G=\Delta G^\circ+RT\ln Q
\]

Kết hợp với:

\[
\Delta G=-nFE
\]

và:

\[
\Delta G^\circ=-nFE^\circ
\]

suy ra:

\[
-nFE=-nFE^\circ+RT\ln Q
\]

nên:

\[
\boxed{E=E^\circ-\frac{RT}{nF}\ln Q}
\]

Ở 25 °C:

\[
E=E^\circ-\frac{0.05916}{n}\log_{10}Q
\]

Vì vậy phương trình Nernst không phải một công thức thực nghiệm tách biệt của điện hóa học. Nó chính là biểu thức Gibbs được viết lại theo đơn vị điện thế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Thương số phản ứng phải dùng hoạt độ** tiếp nhận điểm tựa từ **Suy ra phương trình Nernst** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phương trình Nernst cho biết chiều biến đổi như thế nào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thương số phản ứng phải dùng hoạt độ

Với phản ứng:

\[
aA+bB\rightleftharpoons cC+dD
\]

thương số phản ứng về mặt nhiệt động là:

\[
Q=\frac{a_C^ca_D^d}{a_A^aa_B^b}
\]

Chất rắn tinh khiết và chất lỏng tinh khiết có hoạt độ trạng thái chuẩn bằng 1 nên thường không xuất hiện trong biểu thức rút gọn.

Trong dung dịch loãng, người ta thường thay hoạt độ bằng nồng độ chuẩn hóa để tính gần đúng. Tuy nhiên với chất điện ly đậm đặc, lực ion lớn hoặc ion đa hóa trị, sai lệch khỏi điều kiện lý tưởng có thể đáng kể.

> **Chuyển mạch:** Trong **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Phương trình Nernst cho biết chiều biến đổi như thế nào** tiếp nhận điểm tựa từ **Thương số phản ứng phải dùng hoạt độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pin nồng độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phương trình Nernst cho biết chiều biến đổi như thế nào

Nếu \(Q<K\), phản ứng vẫn còn xu hướng nhiệt động theo chiều thuận. Nếu \(Q>K\), chiều nghịch được ưu tiên về mặt nhiệt động.

Tại cân bằng:

\[
\Delta G=0
\]

và với phản ứng tổng của cả pin:

\[
E=0
\]

Khi đó \(Q=K\), nên:

\[
0=E^\circ-\frac{RT}{nF}\ln K
\]

suy ra:

\[
\ln K=\frac{nFE^\circ}{RT}
\]

Đây là cầu nối trực tiếp giữa điện hóa học và cân bằng hóa học.

> **Chuyển mạch:** Ở chặng này của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Pin nồng độ** tiếp nhận điểm tựa từ **Phương trình Nernst cho biết chiều biến đổi như thế nào** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh hưởng của pH và chuyển electron ghép proton** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pin nồng độ

Hai bán pin có cùng loại phản ứng điện cực nhưng hoạt độ khác nhau vẫn có thể tạo ra điện áp. Động lực không đến từ việc hai chất khác nhau, mà đến từ xu hướng cân bằng thế hóa học giữa hai phía.

Ví dụ đơn giản:

```text
Cu | Cu2+(hoạt độ thấp) || Cu2+(hoạt độ cao) | Cu
```

Electron sẽ dịch chuyển theo chiều làm giảm chênh lệch nồng độ. Đây là ví dụ cho thấy **độ dốc (gradient / 기울기) thành phần (composition gradient)** cũng có thể tạo điện thế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Ảnh hưởng của pH và chuyển electron ghép proton** tiếp nhận điểm tựa từ **Pin nồng độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điện cực tham chiếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh hưởng của pH và chuyển electron ghép proton

Nếu \(H^+\) tham gia bán phản ứng, điện thế sẽ phụ thuộc pH thông qua phương trình Nernst.

Nếu một phản ứng có \(m\) proton và \(n\) electron, phần đóng góp của pH vào điện thế thường phụ thuộc tỉ số \(m/n\). Đây là lý do giản đồ Pourbaix có các đường điện thế theo pH và cũng giải thích vì sao phản ứng oxy hóa-khử trong sinh học rất nhạy với môi trường acid-base.

**Chuyển electron ghép proton (proton-coupled electron transfer, PCET)** là cơ chế trung tâm trong quang hợp, hô hấp, tạo hydrogen và nhiều chu trình xúc tác.

> **Chuyển mạch:** Trong **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, sau nội dung của **Ảnh hưởng của pH và chuyển electron ghép proton**, **Điện cực tham chiếu** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Quá thế — vì sao điện áp thực tế khác điện áp nhiệt động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điện cực tham chiếu

Trong thực nghiệm, cần một điện cực có thế ổn định và đã biết để đo điện cực làm việc. Các điện cực tham chiếu thường gặp gồm Ag/AgCl và điện cực calomel bão hòa.

Giá trị đo luôn phụ thuộc thang tham chiếu. Vì vậy khi báo cáo dữ liệu điện hóa, cần nêu rõ điện cực tham chiếu được sử dụng.

> **Chuyển mạch:** Ở chặng này của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Quá thế — vì sao điện áp thực tế khác điện áp nhiệt động** tiếp nhận điểm tựa từ **Điện cực tham chiếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên hệ với phương trình Butler–Volmer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quá thế — vì sao điện áp thực tế khác điện áp nhiệt động

Điện thế nhiệt động cho biết động lực cân bằng. Để phản ứng chạy với tốc độ hữu hạn, thường cần thêm một hiệu điện thế gọi là **quá thế (overpotential / 과전압)**.

Nguồn của quá thế có thể gồm:

- quá thế hoạt hóa do hàng rào chuyển electron;
- quá thế nồng độ do giới hạn vận chuyển khối;
- sụt áp ohmic do điện trở của chất điện ly, tiếp xúc và màng ngăn.

Vì vậy điện áp vận hành khi pin phóng điện có thể thấp hơn điện áp cân bằng hở mạch, còn điện phân thường cần điện áp đặt vào cao hơn giá trị thuận nghịch tối thiểu.

> Nhiệt động lực học cho biết **điện áp thuận nghịch tối thiểu hoặc tối đa có thể đạt**; động học và vận chuyển cho biết **điện áp vận hành thực tế**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Liên hệ với phương trình Butler–Volmer** tiếp nhận điểm tựa từ **Quá thế — vì sao điện áp thực tế khác điện áp nhiệt động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vận chuyển khối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên hệ với phương trình Butler–Volmer

Động học điện cực thường được mô tả bằng phương trình Butler–Volmer:

\[
j=j_0\left[\exp\left(\frac{\alpha nF\eta}{RT}\right)-\exp\left(-\frac{(1-\alpha)nF\eta}{RT}\right)\right]
\]

trong đó \(j\) là mật độ dòng điện, \(j_0\) là mật độ dòng trao đổi và \(\eta\) là quá thế.

Phương trình Nernst mô tả điện thế cân bằng. Butler–Volmer mô tả dòng điện khi hệ bị đẩy ra khỏi cân bằng. Hai phương trình không cạnh tranh với nhau; chúng trả lời hai câu hỏi khác nhau.

> **Chuyển mạch:** Trong **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Vận chuyển khối** tiếp nhận điểm tựa từ **Liên hệ với phương trình Butler–Volmer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điện áp hở mạch và điện áp khi có tải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vận chuyển khối

Phản ứng điện hóa tiêu thụ hoặc tạo chất ngay tại bề mặt điện cực. Nếu phản ứng bề mặt nhanh hơn tốc độ khuếch tán hoặc đối lưu cung cấp chất, nồng độ gần bề mặt sẽ khác nồng độ trong dung dịch khối và dòng điện bị giới hạn bởi vận chuyển.

Ba cơ chế vận chuyển chính gồm:

- khuếch tán do độ dốc (gradient / 기울기) nồng độ;
- di chuyển ion do điện trường;
- đối lưu do chuyển động của chất lỏng.

Chất điện ly nền (supporting electrolyte) thường được dùng để giảm đóng góp của sự di chuyển ion của chất phân tích và làm bài toán vận chuyển dễ phân tích hơn.

> **Chuyển mạch:** Ở chặng này của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Điện áp hở mạch và điện áp khi có tải** tiếp nhận điểm tựa từ **Vận chuyển khối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh hưởng của nhiệt độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điện áp hở mạch và điện áp khi có tải

**Điện áp hở mạch (open-circuit voltage, OCV)** gần giá trị cân bằng nhiệt động nếu pin được để nghỉ đủ lâu.

Khi có dòng điện chạy, điện áp thay đổi do quá thế và điện trở trong. Một biểu thức kỹ thuật đơn giản là:

\[
V_{terminal}\approx E_{eq}-\eta_{anode}-\eta_{cathode}-IR
\]

Quy ước dấu có thể khác nhau giữa tài liệu, nhưng ý chính là tổn thất vận hành xuất hiện từ động học và vận chuyển.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Ảnh hưởng của nhiệt độ** tiếp nhận điểm tựa từ **Điện áp hở mạch và điện áp khi có tải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh hưởng của nhiệt độ

Từ:

\[
\Delta G=\Delta H-T\Delta S=-nFE
\]

có thể thấy sự phụ thuộc của điện thế cân bằng vào nhiệt độ chứa thông tin về entropy của phản ứng. Trong nhiệt động điện hóa, \(dE/dT\) có thể liên hệ với entropy phản ứng.

Điều này quan trọng với pin vì nhiệt sinh ra không chỉ đến từ tổn thất điện trở mà còn có thành phần nhiệt thuận nghịch liên quan entropy.

> **Chuyển mạch:** Trong **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Những hiểu lầm thường gặp** tiếp nhận điểm tựa từ **Ảnh hưởng của nhiệt độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm thường gặp

### “E° dương nghĩa phản ứng luôn xảy ra nhanh”

Sai. Điện thế dương chỉ nói phản ứng thuận lợi về mặt nhiệt động; động học có thể vẫn rất chậm.

### “Nhân bán phản ứng với hệ số thì phải nhân E°”

Sai. Năng lượng tự do thay đổi theo lượng phản ứng; thế điện cực không được nhân theo hệ số hóa lượng.

### “Phương trình Nernst luôn dùng nồng độ trực tiếp”

Về mặt nghiêm ngặt, phương trình dùng hoạt độ.

### “Điện áp pin giảm chỉ vì chất phản ứng cạn dần”

Không. Phân cực, điện trở trong, vận chuyển khối, chuyển pha và nhiệt độ đều có thể đóng góp.

> **Chuyển mạch:** Ở chặng này của **Điện thế pin và phương trình Nernst — từ năng lượng tự do Gibbs đến điện áp thực tế**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Hãy xem thế điện hóa như **độ dốc nhiệt động cho dòng electron**. Phương trình Nernst cho biết độ dốc ở thành phần hiện tại; quá thế và vận chuyển cho biết cần đẩy hệ thêm bao nhiêu để tạo được dòng hữu hạn.

Xem tiếp: [Điện phân](./04_electrolysis.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
