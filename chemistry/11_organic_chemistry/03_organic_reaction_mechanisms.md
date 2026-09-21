# Cơ chế phản ứng hữu cơ — dòng electron, năng lượng và tính chọn lọc

> **Cơ chế phản ứng hữu cơ (organic reaction mechanism / 유기 반응 메커니즘)** là mô hình từng bước mô tả cách liên kết bị phá, liên kết mới hình thành, mật độ electron di chuyển và những chất trung gian/trạng thái chuyển tiếp nào nối chất phản ứng với sản phẩm. Cơ chế không phải một đoạn phim được ghi trực tiếp; nó là mô hình bị ràng buộc bởi động học, hóa lập thể, hiệu ứng đồng vị, phổ học, phân bố sản phẩm và cấu trúc điện tử.

Thói quen quan trọng nhất không phải học thuộc hàng trăm phản ứng có tên riêng, mà là học cách nhìn hóa hữu cơ như **nguồn giàu electron tương tác với vị trí nghèo electron trên một cảnh quan năng lượng tự do**.

## Mũi tên cong là quy tắc bảo toàn electron

Mũi tên cong đầu đầy theo dõi **một cặp electron**. Nó phải bắt đầu từ nơi thực sự có electron: cặp electron tự do, điện tích âm hoặc liên kết. Mũi tên kết thúc tại nơi cặp electron đó tham gia tạo liên kết mới hoặc trở thành cặp electron tự do.

Nếu mũi tên bắt đầu từ một nguyên tử không có cặp electron khả dụng, cách ghi sổ electron đã sai dù sản phẩm cuối trông quen thuộc.

Mũi tên nửa đầu hay **mũi tên lưỡi câu (fishhook arrow)** theo dõi một electron và dùng trong cơ chế gốc tự do.

Vì vậy đẩy mũi tên (arrow pushing) mã hóa hai ràng buộc bảo toàn:

- electron không tự sinh ra hoặc biến mất;
- thay đổi hóa trị/bậc liên kết phải tuân theo đường đi của electron.

## Cơ chế khác phương trình tổng

Một phương trình tổng có thể che giấu nhiều bước sơ cấp:

```text
Chất A + Chất B → Sản phẩm
```

Trong thực tế cơ chế có thể là:

```text
A + B ⇌ chất trung gian I
I → chất trung gian II
II + dung môi → sản phẩm
```

Mỗi bước sơ cấp có trạng thái chuyển tiếp và tốc độ riêng. Phương trình hóa lượng không thể tự cho biết liên kết nào bị phá trước, có chất trung gian hay không hoặc yếu tố nào quyết định độ chọn lọc.

## Nucleophile — chất cho cặp electron

**Tác nhân ái nhân (nucleophile / 친핵체)** cho mật độ electron vào orbital ái điện, thường là orbital phản liên kết năng lượng thấp như \(\sigma^*\) hoặc \(\pi^*\).

Các vị trí ái nhân thường gặp gồm:

- O, N, S, C mang điện tích âm;
- nguyên tử trung hòa có cặp electron tự do như amine;
- liên kết π;
- tâm carbon trong hợp chất cơ kim.

**Tính ái nhân (nucleophilicity)** là khái niệm động học: nó mô tả tốc độ một tiểu phân tấn công trong điều kiện cụ thể. Nó liên quan nhưng không đồng nhất với **độ base (basicity)**, vốn là đại lượng nhiệt động về ái lực với proton.

Ví dụ \(I^-\) có thể là nucleophile tốt trong dung môi proton nhưng là base yếu hơn nhiều so với alkoxide.

## Electrophile — nơi năng lượng thấp có thể nhận mật độ electron

**Tác nhân ái điện (electrophile / 친전자체)** nhận mật độ electron.

Các tâm ái điện thường gặp gồm carbocation, carbonyl carbon, carbon alkyl gắn nhóm rời, proton, boron acid Lewis và hệ π đã được hoạt hóa.

Điện tích dương hình thức giúp nhận diện một số electrophile, nhưng phân cực cũng rất quan trọng. Carbonyl carbon không mang điện tích dương hình thức nhưng vẫn ái điện vì oxygen kéo mật độ electron và orbital \(\pi^*_{C=O}\) dễ nhận electron.

## Góc nhìn HOMO–LUMO

Một mô hình orbital hữu ích là:

```text
HOMO của nucleophile → LUMO của electrophile
```

Phản ứng thuận lợi hơn khi hai orbital phù hợp về năng lượng, độ chồng phủ và định hướng không gian.

Điều này giải thích vì sao \(S_N2\) cần tấn công từ phía sau: nucleophile phải chồng phủ với thùy phía sau của orbital \(\sigma^*\) C–LG. Nó cũng giải thích vì sao định hướng lập thể-điện tử quan trọng trong phản ứng loại và cộng.

## Nhóm rời — sau khi rời phải tạo tiểu phân đủ bền

**Nhóm rời (leaving group / 이탈기)** rời đi cùng cặp electron liên kết.

Nhóm rời tốt thường tạo anion hoặc phân tử trung hòa tương đối bền. Base yếu thường là nhóm rời tốt vì không có xu hướng mạnh giữ lại cặp electron trong trạng thái năng lượng cao.

\(I^-\) thường là nhóm rời tốt hơn \(F^-\) trong phản ứng thế alkyl vì liên kết C–I yếu hơn và iodide lớn, dễ phân cực. \(OH^-\) thường là nhóm rời kém, nhưng proton hóa biến –OH thành H2O, một nhóm rời trung hòa rất tốt.

Vì vậy xúc tác acid thường tăng tốc bằng cách **thay đổi bản chất của nhóm rời**, không phải bằng một cơ chế “thần kỳ”.

## Giản đồ tọa độ phản ứng — bản đồ nằm dưới cơ chế

Khi biểu diễn năng lượng tự do Gibbs theo tọa độ phản ứng, đáy là các tiểu phân tương đối bền còn đỉnh là trạng thái chuyển tiếp.

Chất trung gian nằm ở cực tiểu cục bộ. Trạng thái chuyển tiếp không phải tiểu phân có thể cô lập; nó là cấu hình năng lượng cao nhất dọc một bước sơ cấp.

Tốc độ một bước phụ thuộc mạnh vào năng lượng tự do hoạt hóa:

\[
k \propto e^{-\Delta G^{\ddagger}/RT}
\]

Do đó chỉ một chênh lệch nhỏ của \(\Delta G^{\ddagger}\) cũng có thể tạo khác biệt lớn về tốc độ hoặc tỉ lệ sản phẩm.

## Tiên đề Hammond — trạng thái chuyển tiếp thường giống trạng thái gần nó về năng lượng

**Tiên đề Hammond (Hammond postulate)** nói định tính rằng trạng thái chuyển tiếp thường có cấu trúc giống tiểu phân bền gần nó nhất về năng lượng.

Với bước thu năng lượng mạnh, trạng thái chuyển tiếp thường giống sản phẩm hơn; với bước tỏa năng lượng mạnh, nó thường giống chất phản ứng hơn.

Điều này giúp giải thích vì sao độ bền carbocation ảnh hưởng mạnh tốc độ ở phản ứng có bước hình thành carbocation thu năng lượng và quyết định tốc độ.

Đây là quy tắc định tính, không phải định luật cấu trúc tuyệt đối.

# Cơ chế thế

## SN2 — một bước đồng thời

SN2 là viết tắt của **thế ái nhân hai phân tử (Substitution Nucleophilic Bimolecular)**.

Dạng tổng quát:

\[
Nu^- + R-LG \rightarrow R-Nu + LG^-
\]

Phương trình tốc độ điển hình:

\[
rate = k[Nu][R-LG]
\]

Cả hai tiểu phân đều tham gia trạng thái chuyển tiếp quyết định tốc độ.

### Vì sao phải tấn công từ phía sau?

Nucleophile phải cho electron vào orbital \(\sigma^*_{C-LG}\). Thùy nhận electron lớn nằm đối diện liên kết C–LG. Tấn công từ phía trước có độ chồng phủ kém hơn và đẩy electron mạnh hơn.

Khi nucleophile tiến vào, carbon đi qua hình học trạng thái chuyển tiếp gần dạng lưỡng tháp tam giác rồi nhóm rời đi.

Nếu carbon là tâm lập thể, cấu hình bị đảo — **đảo Walden (Walden inversion)**.

### Ảnh hưởng lập thể

SN2 rất nhạy với mức đông đúc quanh carbon ái điện:

```text
methyl > bậc một > bậc hai >> bậc ba
```

Điều này không có nghĩa carbon bậc ba “không phản ứng”; chỉ có nghĩa con đường SN2 bị cản rất mạnh và cơ chế khác có thể chiếm ưu thế.

### Ảnh hưởng dung môi

Dung môi phân cực không proton (polar aprotic solvent) thường làm nucleophile anion phản ứng mạnh hơn vì cation được solvat hóa tốt còn anion ít bị “nhốt” bởi mạng liên kết hydrogen hơn so với dung môi proton.

Vì vậy dung môi có thể thay đổi tính ái nhân hiệu dụng mà không làm thay đổi bản chất tiểu phân.

## SN1 — ion hóa rồi bắt giữ

SN1 là **thế ái nhân một phân tử (Substitution Nucleophilic Unimolecular)**.

Các bước đơn giản hóa:

1. liên kết C–LG ion hóa;
2. hình thành chất trung gian dạng carbocation;
3. nucleophile tấn công;
4. chuyển proton nếu cần để hoàn tất sản phẩm.

Phương trình tốc độ điển hình:

\[
rate = k[R-LG]
\]

Nồng độ nucleophile không xuất hiện nếu bước ion hóa là bước quyết định tốc độ.

### Độ bền carbocation

Carbocation được ổn định bởi siêu liên hợp, cộng hưởng và hiệu ứng cho electron. Carbocation bậc ba thường bền hơn bậc hai và bậc một. Carbocation allyl và benzyl có thể được cộng hưởng ổn định mạnh.

Vì vậy chất nền có khả năng tạo carbocation bền phù hợp hơn với SN1.

### Chuyển vị

Dịch chuyển hydride hoặc alkyl có thể tạo carbocation bền hơn trước khi nucleophile bắt giữ. Sản phẩm chuyển vị là bằng chứng cơ chế mạnh cho sự tồn tại của chất trung gian dạng carbocation.

### Hóa lập thể

Carbocation lý tưởng gần phẳng có thể bị tấn công từ hai mặt, gợi ý sự racemic hóa. Thực tế phản ứng có thể không racemic hoàn toàn vì nhóm rời, lồng dung môi hoặc cặp ion che một mặt.

# Cơ chế loại

## E2 — lấy proton và rời nhóm đồng thời

Trong E2, base lấy hydrogen β đồng thời liên kết C–LG bị phá và C=C được tạo trong cùng một bước sơ cấp.

Phương trình tốc độ điển hình:

\[
rate=k[base][substrate]
\]

### Yêu cầu anti-periplanar

Độ chồng phủ orbital tốt nhất xuất hiện khi C–H và C–LG ở hình học **đối phẳng (anti-periplanar)**. Điều này cho phép orbital \(\sigma_{C-H}\) cho electron vào \(\sigma^*_{C-LG}\) trong lúc liên kết π hình thành.

Yêu cầu hình học này làm E2 có tính **đặc hiệu lập thể (stereospecific)** trong hệ bị ràng buộc như cyclohexane. Đôi khi cần cấu hình trans-diaxial.

### Sản phẩm Zaitsev và Hofmann

Base nhỏ thường ưu tiên alkene thế nhiều hơn, bền nhiệt động hơn — xu hướng Zaitsev. Base cồng kềnh có thể lấy proton dễ tiếp cận hơn và tạo alkene ít thế hơn — sản phẩm Hofmann.

Đây không phải luật bất biến; hình học chất nền, nhóm rời và hiệu ứng điện tử có thể đảo xu hướng.

## E1 — carbocation rồi khử proton

E1 chia sẻ chất trung gian carbocation với SN1. Sau bước ion hóa, một base lấy hydrogen β để tạo alkene.

Vì SN1 và E1 thường có điều kiện và chất trung gian chung, hỗn hợp sản phẩm là phổ biến. Nhiệt độ cao có thể làm phản ứng loại được ưu tiên hơn một phần do entropy và số con đường tạo alkene.

# Chọn SN1/SN2/E1/E2 mà không học thuộc bảng tra

Một thứ tự suy luận hữu ích là:

1. Chất nền có thể tạo carbocation bền không?
2. Nucleophile/base mạnh hay yếu?
3. Carbon bị tấn công có dễ tiếp cận về lập thể không?
4. Dung môi là proton hay không proton và có khả năng ion hóa tốt không?
5. Có hydrogen β với hình học phù hợp không?
6. Nhiệt độ có làm phản ứng loại được ưu tiên hơn không?

Cơ chế là sự cạnh tranh giữa các hàng rào hoạt hóa, không phải nhãn cố định gắn với một thuốc thử.

# Phản ứng cộng vào liên kết π

Liên kết π giàu electron và electron π lộ ra ngoài hơn electron σ. Vì vậy electrophile dễ tấn công alkene và alkyne.

## Cộng ái điện và chọn lọc vị trí

Trong phản ứng cộng acid vào alkene không đối xứng, con đường proton hóa tạo chất trung gian hoặc trạng thái chuyển tiếp dạng carbocation bền hơn thường được ưu tiên. Quy tắc định hướng **Markovnikov** vì vậy là hệ quả của chênh lệch năng lượng các con đường, không phải luật độc lập.

Phản ứng cộng HBr có peroxide đi theo cơ chế gốc tự do và có thể đảo chọn lọc vị trí, cho thấy thay đổi cơ chế làm thay đổi “quy tắc”.

## Cộng halogen

Cộng \(Br_2\) thường tạo ion bromonium cầu nối thay vì carbocation tự do. Sau đó nucleophile tấn công từ phía sau và thường tạo cộng anti.

Mô hình này giải thích cả hóa lập thể lẫn việc ít xuất hiện chuyển vị điển hình của carbocation tự do.

# Logic phản ứng carbonyl

Liên kết C=O phân cực:

\[
C^{\delta+}=O^{\delta-}
\]

Nucleophile tấn công carbon; electron π chuyển lên oxygen, tạo chất trung gian tứ diện.

Với aldehyde/ketone, con đường thường là **cộng ái nhân (nucleophilic addition)** vì không có nhóm rời tốt gắn vào carbonyl carbon.

Với dẫn xuất acid carboxylic, chất trung gian tứ diện có thể sụp lại và đẩy nhóm rời ra, tạo **thế acyl ái nhân (nucleophilic acyl substitution)**.

Chỉ một khác biệt này tổ chức được một phần rất lớn hóa học carbonyl.

# Các bước acid-base bên trong cơ chế hữu cơ

Chuyển proton không phải bước “dọn dẹp” trang trí. Nó thay đổi tính ái nhân, ái điện và khả năng rời nhóm.

Ví dụ:

- proton hóa oxygen carbonyl làm carbon tăng tính ái điện;
- khử proton alcohol tạo alkoxide ái nhân mạnh hơn;
- proton hóa OH biến nhóm rời kém \(OH^-\) thành nước;
- tạo enolate biến carbon α ái nhân yếu thành nucleophile carbon mạnh.

Vì vậy cơ chế hữu cơ lặp đi lặp lại việc dùng hóa học acid-base để **lập trình lại mật độ electron**.

# Cơ chế gốc tự do

Phản ứng gốc tự do theo dõi electron đơn bằng mũi tên fishhook.

Một chuỗi điển hình gồm:

1. khơi mào (initiation) — tạo gốc tự do;
2. phát triển chuỗi (propagation) — gốc phản ứng và tạo gốc mới;
3. kết thúc chuỗi (termination) — các gốc kết hợp hoặc bị loại bỏ.

Halogen hóa alkane là ví dụ kinh điển. Độ bền gốc, năng lượng phân ly liên kết và cấu trúc trạng thái chuyển tiếp quyết định tính chọn lọc.

# Phản ứng pericyclic — khi nhiều liên kết tái tổ chức đồng thời

Không phải mọi cơ chế đều phân rã tự nhiên thành các bước ion nucleophile/electrophile. **Phản ứng pericyclic** như Diels–Alder gồm tái tổ chức electron theo vòng trong một trạng thái chuyển tiếp đồng thời.

Đối xứng orbital quyết định con đường nào được phép về nhiệt. Tương tác orbital biên giữa HOMO của diene và LUMO của dienophile là điểm vào trực quan để hiểu cơ chế.

Điều này nhắc rằng logic dòng electron rộng hơn việc chỉ theo dõi điện tích hình thức.

# Xúc tác

## Xúc tác acid

Acid có thể proton hóa chất nền, làm giảm năng lượng LUMO hoặc biến nhóm rời kém thành nhóm rời tốt. Chất xúc tác được tái sinh ở bước sau.

## Xúc tác base

Base có thể tạo nucleophile hoặc enolate phản ứng mạnh hơn bằng cách khử proton.

## Xúc tác kim loại

Kim loại chuyển tiếp có thể phối trí hệ π, thực hiện cộng oxy hóa/loại khử và ổn định chất trung gian bất thường. Ngôn ngữ cơ chế hữu cơ và vô cơ gặp nhau ở đây.

Chất xúc tác thay đổi con đường và hàng rào hoạt hóa, không thay đổi chênh lệch năng lượng tự do cân bằng giữa trạng thái đầu và cuối.

# Tính chọn lọc — hóa học là so sánh các hàng rào cạnh tranh

**Tính chọn lọc hóa học (chemoselectivity)** quyết định nhóm chức nào phản ứng.

**Tính chọn lọc vị trí (regioselectivity)** quyết định vị trí nào phản ứng.

**Tính chọn lọc lập thể (stereoselectivity)** quyết định đồng phân lập thể nào được ưu tiên.

**Tính đặc hiệu lập thể (stereospecificity)** nghĩa là các chất phản ứng lập thể khác nhau tạo ra các sản phẩm lập thể khác nhau theo một ánh xạ hình học do cơ chế áp đặt.

Ở mức sâu hơn, độ chọn lọc thường được quyết định bởi:

\[
\Delta\Delta G^{\ddagger}
\]

giữa các trạng thái chuyển tiếp cạnh tranh. Chỉ vài kJ/mol chênh lệch cũng có thể tạo tỉ lệ sản phẩm rất lớn.

# Kiểm soát động học và kiểm soát nhiệt động

Giả sử chất phản ứng có thể tạo sản phẩm A và B. A đi qua hàng rào thấp hơn nhưng B có năng lượng tự do cuối thấp hơn.

Ở nhiệt độ thấp, thời gian ngắn hoặc điều kiện gần không thuận nghịch, A có thể chiếm ưu thế: **sản phẩm động học (kinetic product)**.

Nếu các con đường thuận nghịch và hệ có đủ thời gian/nhiệt, thành phần có thể tiến tới cân bằng và B chiếm ưu thế: **sản phẩm nhiệt động (thermodynamic product)**.

Phân biệt này xuất hiện trong cộng diene liên hợp, tạo enolate và nhiều phản ứng chuyển vị.

# Cơ chế được kiểm chứng bằng thực nghiệm như thế nào

Cơ chế là mô hình phải được đối chiếu với nhiều bằng chứng độc lập.

### Phương trình tốc độ

Sự phụ thuộc tốc độ vào nồng độ cho biết tiểu phân nào tham gia trước hoặc trong trạng thái chuyển tiếp kiểm soát tốc độ.

### Hiệu ứng đồng vị

Thay H bằng D làm thay đổi năng lượng dao động điểm không. **Hiệu ứng đồng vị động học (kinetic isotope effect)** lớn có thể cho thấy phá liên kết C–H quan trọng trong bước quyết định tốc độ.

### Kết quả hóa lập thể

Đảo cấu hình, giữ cấu hình, cộng syn/anti và sản phẩm chuyển vị đều giới hạn những cơ chế có thể xảy ra.

### Bắt giữ chất trung gian

Nếu chất trung gian được đề xuất có thể bị bắt hóa học hoặc quan sát bằng phổ, độ tin cậy của cơ chế tăng.

### Hiệu ứng nhóm thế

Tương quan kiểu Hammett cho biết nhóm đẩy/hút electron ảnh hưởng thế nào đến sự hình thành điện tích trong trạng thái chuyển tiếp.

Một cơ chế tốt phải giải thích nhiều quan sát độc lập, không chỉ tạo được đúng sản phẩm cuối.

## Những hiểu lầm thường gặp

### “Mũi tên cong cho thấy nguyên tử di chuyển thế nào”

Không. Chúng theo dõi electron.

### “Một thuốc thử luôn đồng nghĩa một cơ chế”

Không. Chất nền, dung môi, nhiệt độ, nồng độ và con đường cạnh tranh đều quan trọng.

### “Sản phẩm bền nhất luôn hình thành nhanh nhất”

Không. Động học và nhiệt động là hai câu hỏi khác nhau.

### “Chuyển vị carbocation là ngẫu nhiên”

Không. Chuyển vị thường đi theo con đường dễ tiếp cận để tạo cấu trúc cation năng lượng thấp hơn.

### “Phản ứng có tên riêng là các sự kiện tách biệt”

Nhiều phản ứng có tên riêng chỉ là tổ hợp của một số mô-típ sơ cấp lặp lại: chuyển proton, tấn công ái nhân, rời nhóm, cộng, loại, chuyển electron và chuyển vị.

## Mô hình tư duy

> Giải cơ chế hữu cơ là **định tuyến electron có ràng buộc trên một cảnh quan năng lượng**. Hãy tìm nơi electron có thể xuất phát, orbital nhận năng lượng thấp nằm ở đâu, hình học nào cho chồng phủ tốt, tiểu phân nào có thể rời đi và trạng thái chuyển tiếp cạnh tranh nào thấp nhất.

Xem tiếp: [Alkane, alkene và alkyne](./04_alkanes_alkenes_and_alkynes.md), sau đó quay lại khung này khi học hóa học thơm và carbonyl.