# Entropy — số cách phân bố năng lượng, vật chất và thông tin vi mô

> **Entropy (\(S\) / 엔트로피)** là hàm trạng thái nhiệt động mô tả mức độ năng lượng và vật chất có thể được phân bố giữa các cấu hình vi mô tương thích với trạng thái vĩ mô. Cách gọi entropy là “độ hỗn loạn” chỉ là phép so sánh rất thô và thường gây hiểu sai.

Một cách nhìn sâu hơn là: entropy đo **độ rộng của không gian trạng thái vi mô có thể tiếp cận** dưới những ràng buộc vĩ mô nhất định. Khi một hệ có nhiều cách hơn để phân bố năng lượng và hạt mà vẫn tạo cùng trạng thái vĩ mô, entropy của trạng thái đó lớn hơn.

## Vì sao định luật thứ nhất chưa đủ?

Bảo toàn năng lượng chỉ nói tổng năng lượng không tự sinh ra hay biến mất. Nó không nói quá trình nào có chiều tự nhiên.

Một cốc cà phê nóng về mặt định luật thứ nhất có thể nhận nhiệt từ căn phòng lạnh hơn nếu căn phòng mất đúng lượng năng lượng đó. Nhưng ta không quan sát quá trình này tự xảy ra.

Chiều tự nhiên xuất hiện từ xu hướng thống kê: các trạng thái vĩ mô tương ứng với số lượng cấu hình vi mô lớn hơn có xác suất áp đảo.

Nói cách khác, định luật thứ nhất là **điều kiện bảo toàn**, còn định luật thứ hai cung cấp **mũi tên thời gian thống kê** cho hệ vĩ mô.

## Trạng thái vĩ mô và vi trạng thái

Một **trạng thái vĩ mô (macrostate)** được mô tả bằng các đại lượng như:

- nhiệt độ;
- áp suất;
- thể tích;
- số hạt;
- thành phần.

Một **vi trạng thái (microstate)** mô tả chi tiết hơn cách các hạt cụ thể chiếm các vị trí và trạng thái năng lượng.

Rất nhiều vi trạng thái khác nhau có thể tạo ra cùng một trạng thái vĩ mô.

Ví dụ, nếu có các phân tử khí phân bố trong một hộp, trạng thái “khí gần như đều trong toàn hộp” có số cách sắp xếp lớn hơn cực nhiều so với trạng thái “mọi phân tử cùng nằm ở góc trái”. Vì vậy trạng thái phân bố đều áp đảo về xác suất.

## Hệ thức Boltzmann

Cơ học thống kê liên hệ entropy với số vi trạng thái \(W\):

\[
S=k_B\ln W
\]

Trong đó \(k_B\) là hằng số Boltzmann.

Logarithm rất quan trọng vì nếu hai hệ độc lập có:

\[
W_{total}=W_AW_B
\]

thì:

\[
S_{total}=k_B\ln(W_AW_B)=S_A+S_B
\]

Nhờ vậy entropy trở thành đại lượng cộng được ở thang vĩ mô.

## Từ số vi trạng thái tới xác suất

Nếu tất cả vi trạng thái khả dĩ có xác suất như nhau trong mô hình vi chính tắc, trạng thái vĩ mô có nhiều vi trạng thái hơn cũng có xác suất lớn hơn.

Tuy nhiên trong nhiều hệ nhiệt độ cố định, các trạng thái năng lượng khác nhau không có xác suất như nhau. Phân bố Boltzmann cho:

\[
p_i=\frac{e^{-E_i/(k_BT)}}{Z}
\]

Trong đó \(Z\) là **hàm phân hoạch (partition function)**:

\[
Z=\sum_i e^{-E_i/(k_BT)}
\]

Hàm phân hoạch là cầu nối rất mạnh giữa mức năng lượng lượng tử và nhiệt động lực học vĩ mô.

Từ \(Z\), về nguyên tắc có thể suy ra năng lượng trung bình, entropy, năng lượng tự do và nhiều đại lượng khác.

## Entropy không đơn giản là “mức độ lộn xộn”

Khí thường có entropy cao hơn chất lỏng cùng chất chủ yếu vì phân tử khí có nhiều trạng thái chuyển động tịnh tiến khả dĩ hơn. Trộn hai khí làm entropy tăng vì các hạt có nhiều cách phân bố hơn trong thể tích lớn hơn.

Một tinh thể có thể có nhiều khuyết tật và nhìn “lộn xộn”, nhưng vẫn có entropy thấp hơn chất lỏng ở cùng điều kiện.

Từ “hỗn loạn” thiếu định nghĩa định lượng và không mô tả đầy đủ sự phân bố năng lượng.

Một cách nói tốt hơn là:

> entropy tăng khi số cách khả dĩ để hệ phân bố vật chất và năng lượng tăng dưới cùng các ràng buộc vĩ mô.

## Định nghĩa Clausius

Với quá trình truyền nhiệt thuận nghịch:

\[
dS=\frac{\delta q_{rev}}{T}
\]

Với biến đổi đẳng nhiệt thuận nghịch hữu hạn:

\[
\Delta S=\frac{q_{rev}}{T}
\]

Đây là định nghĩa nhiệt động cho biến thiên entropy. Nó không có nghĩa quá trình thật bắt buộc phải thuận nghịch; con đường thuận nghịch chỉ là một con đường toán học thuận tiện để tính chênh lệch của hàm trạng thái.

## Quá trình không thuận nghịch và entropy sinh ra

Trong quá trình thật, có thể viết khái niệm:

\[
\Delta S_{system}=\int\frac{\delta q}{T_{boundary}}+S_{gen}
\]

với:

\[
S_{gen}\ge0
\]

**Entropy sinh ra (entropy generation)** xuất hiện do các quá trình không thuận nghịch như:

- truyền nhiệt qua chênh lệch nhiệt độ hữu hạn;
- khuếch tán;
- ma sát nhớt;
- phản ứng hóa học không cân bằng;
- trộn tự phát;
- dòng điện qua điện trở.

Trong quá trình lý tưởng thuận nghịch:

\[
S_{gen}=0
\]

Khái niệm này rất quan trọng trong kỹ thuật hóa học và phân tích hiệu suất năng lượng.

## Định luật thứ hai

Đối với một vũ trụ cô lập:

\[
\Delta S_{universe}\ge0
\]

Quá trình tự diễn ra không thuận nghịch có tổng entropy tăng; trạng thái cân bằng tương ứng với cực đại entropy dưới các ràng buộc phù hợp.

Entropy của một hệ con riêng lẻ có thể giảm nếu entropy của môi trường tăng nhiều hơn.

Ví dụ nước đông thành băng làm entropy của nước giảm, nhưng giải phóng nhiệt ra môi trường. Dưới nhiệt độ đông đặc, tổng biến thiên entropy của hệ + môi trường vẫn có thể dương.

## Vì sao nhiệt tự truyền từ nóng sang lạnh?

Giả sử một lượng nhiệt \(q\) truyền từ vật nóng ở \(T_h\) sang vật lạnh ở \(T_c\), với:

\[
T_h>T_c
\]

Biến thiên entropy tổng gần đúng:

\[
\Delta S_{total}=-\frac{q}{T_h}+\frac{q}{T_c}
\]

Vì:

\[
\frac1{T_c}>\frac1{T_h}
\]

nên:

\[
\Delta S_{total}>0
\]

Đây là cách định lượng cho chiều truyền nhiệt tự nhiên.

## Entropy mol chuẩn

Khác với enthalpy tạo thành chuẩn, **entropy mol chuẩn (standard molar entropy)** của nguyên tố tinh khiết ở `298 K` không được quy ước bằng 0.

Giá trị entropy tuyệt đối có thể được xây dựng từ định luật thứ ba bằng cách tích phân khả năng nhiệt và cộng entropy của các chuyển pha.

## Định luật thứ ba của nhiệt động lực học

Với tinh thể hoàn hảo có trạng thái cơ bản duy nhất:

\[
S\rightarrow0\quad khi\quad T\rightarrow0\;K
\]

Lý do thống kê là khi chỉ còn một vi trạng thái cơ bản:

\[
W=1
\]

nên:

\[
S=k_B\ln1=0
\]

Định luật thứ ba tạo điểm gốc cho entropy tuyệt đối.

## Entropy dư

Một số tinh thể vẫn có nhiều cách sắp xếp tương đương ngay gần 0 K nếu hệ bị “đóng băng” trong trạng thái mất trật tự cấu hình.

Khi đó có thể tồn tại **entropy dư (residual entropy)**.

Ví dụ kinh điển là sự định hướng phân tử trong một số tinh thể hoặc băng, nơi nhiều cấu hình vi mô vẫn tương thích với năng lượng rất gần nhau.

Điều này cho thấy điều kiện “tinh thể hoàn hảo, trạng thái cơ bản duy nhất” trong định luật thứ ba là quan trọng.

## Nhiệt dung và entropy

Khi hệ được nung thuận nghịch từ \(T_1\) đến \(T_2\):

\[
\Delta S=\int_{T_1}^{T_2}\frac{C}{T}\,dT
\]

Ở áp suất không đổi dùng \(C_p\), còn thể tích không đổi dùng \(C_V\) tùy con đường.

Công thức này cho thấy nhiệt dung liên hệ trực tiếp với số mức năng lượng có thể tiếp cận khi nhiệt độ thay đổi.

## Entropy của chuyển pha

Ở chuyển pha thuận nghịch tại nhiệt độ cân bằng:

\[
\Delta S_{transition}=\frac{\Delta H_{transition}}{T_{transition}}
\]

Ví dụ entropy nóng chảy:

\[
\Delta S_{fus}=\frac{\Delta H_{fus}}{T_m}
\]

Chất lỏng thường có entropy cao hơn chất rắn vì có nhiều cấu hình khả dĩ hơn.

## Một số xu hướng entropy

Với cùng một chất và điều kiện tương đương, thường có xu hướng:

\[
S(gas)>S(liquid)>S(solid)
\]

Phân tử phức tạp hơn thường có entropy mol lớn hơn vì có nhiều dạng quay và dao động.

Phản ứng làm tăng số mol khí thường có xu hướng tạo \(\Delta S\) dương.

Tuy nhiên đây chỉ là các quy tắc kinh nghiệm; khi cần độ chính xác phải dùng dữ liệu nhiệt động thực.

## Entropy trộn

Trộn lý tưởng tạo **entropy cấu hình (configurational entropy)** ngay cả khi năng lượng tương tác gần như không thay đổi.

Với hỗn hợp lý tưởng:

\[
\Delta S_{mix}=-R\sum_i n_i\ln x_i
\]

Vì:

\[
0<x_i<1
\]

nên:

\[
\Delta S_{mix}>0
\]

Đây là một lý do entropy đóng vai trò lớn trong sự hòa tan và trộn khí.

## Ý nghĩa vi mô của entropy trộn

Trước khi trộn, phân tử A chỉ có thể nằm trong vùng A và phân tử B trong vùng B. Sau khi bỏ vách ngăn, mỗi phân tử có nhiều vị trí khả dĩ hơn.

Số cách phân bố tăng rất mạnh dù không cần thay đổi đáng kể năng lượng tương tác.

Đây là ví dụ điển hình cho một quá trình được thúc đẩy chủ yếu bởi entropy.

## Nghịch lý Gibbs và tính phân biệt của hạt

Nếu trộn hai khí hoàn toàn giống nhau, không có entropy trộn thực sự quan sát được vì trạng thái trước và sau không phân biệt về mặt vật lý.

Điều này dẫn tới **nghịch lý Gibbs (Gibbs paradox)** trong cách đếm cổ điển và được giải quyết khi tính đúng tính không phân biệt của các hạt đồng nhất trong cơ học lượng tử/thống kê.

Đây là một ví dụ sâu cho thấy cách đếm vi trạng thái phải tuân bản chất vật lý của hệ.

## Entropy và phản ứng hóa học

Với phản ứng:

\[
\sum_i \nu_i A_i=0
\]

biến thiên entropy phản ứng chuẩn:

\[
\Delta S^\circ_{rxn}=\sum_i\nu_iS_i^\circ
\]

Entropy đóng góp vào động lực phản ứng qua:

\[
\Delta G=\Delta H-T\Delta S
\]

Ở nhiệt độ cao, hạng \(T\Delta S\) có thể trở nên rất quan trọng.

Một phản ứng không thuận lợi về enthalpy vẫn có thể thuận lợi về Gibbs nếu entropy tăng đủ mạnh.

## Entropy và thế hóa học

Trong hỗn hợp, entropy trộn làm thế hóa học phụ thuộc thành phần.

Với dung dịch lý tưởng:

\[
\mu_i=\mu_i^\circ+RT\ln x_i
\]

Hạng logarithm thành phần có nguồn gốc sâu từ entropy cấu hình của sự trộn.

Đây là cầu nối từ entropy sang:

- cân bằng pha;
- áp suất thẩm thấu;
- định luật Raoult;
- cân bằng hóa học;
- thế điện hóa.

## Entropy và thông tin

Entropy Shannon trong **lý thuyết thông tin (information theory)** có dạng:

\[
H=-\sum_i p_i\log p_i
\]

Dạng tổng quát của entropy Gibbs trong cơ học thống kê là:

\[
S=-k_B\sum_i p_i\ln p_i
\]

Hai biểu thức có cấu trúc toán học gần như giống nhau vì đều đo mức phân tán của một phân bố xác suất.

Tuy nhiên không nên tùy tiện đồng nhất “bit thông tin” với entropy nhiệt động. Muốn nối hai khái niệm phải xác định rõ hệ vật lý, trạng thái và đơn vị.

## Entropy trong sinh học không vi phạm định luật thứ hai

Sinh vật tạo cấu trúc có tổ chức cao và có thể làm entropy cục bộ giảm. Nhưng sinh vật là hệ mở: chúng lấy năng lượng tự do từ thức ăn hoặc ánh sáng và thải nhiệt cùng sản phẩm phân hủy ra môi trường.

Tổng entropy của hệ rộng hơn vẫn tăng.

Vì vậy “sự sống tạo trật tự” không mâu thuẫn với nhiệt động lực học.

## Entropy và tính không thuận nghịch trong công nghệ

Trong thiết bị thật, entropy sinh ra càng lớn thì càng nhiều năng lượng có khả năng sinh công bị mất.

Các nguồn gồm:

- trao đổi nhiệt qua chênh lệch nhiệt độ lớn;
- giảm áp;
- ma sát;
- trộn dòng có thành phần khác nhau;
- phản ứng quá xa cân bằng.

Trong kỹ thuật, phân tích entropy giúp tìm nơi hệ tiêu tán **khả năng sinh công (exergy)**.

## Các hiểu lầm thường gặp

### “Entropy luôn tăng trong mọi vật”

Không. Tổng entropy của một hệ cô lập không giảm; entropy của một hệ con có thể giảm nếu môi trường bù lại nhiều hơn.

### “Entropy chỉ là độ ngẫu nhiên”

Cách nói này quá mơ hồ. Mô hình tốt hơn là số cấu hình vi mô có thể tiếp cận và cách năng lượng/vật chất được phân bố.

### “Nếu entropy tăng thì phản ứng chắc chắn tự xảy ra”

Chỉ đúng khi xét tổng entropy của toàn hệ cô lập; ở nhiệt độ và áp suất không đổi thường thuận tiện hơn khi kết hợp entropy với enthalpy qua năng lượng tự do Gibbs.

### “Entropy cao nghĩa hệ có năng lượng cao”

Không. Entropy và năng lượng là hai đại lượng khác nhau. Một trạng thái có thể có entropy cao nhưng năng lượng thấp hoặc ngược lại.

### “Entropy chỉ có ý nghĩa trong khí”

Không. Entropy có vai trò trong chất rắn, chất lỏng, dung dịch, phản ứng, vật liệu, sinh học và thông tin thống kê.

## Mô hình tư duy

Entropy đo **độ rộng của không gian các khả năng vi mô** dưới những ràng buộc xác định. Khi hệ tiến hóa tự nhiên, nó có xu hướng đi tới các trạng thái có số cách phân bố năng lượng và vật chất lớn hơn, trừ khi các ràng buộc năng lượng tạo ra sự đánh đổi khác. Ở cấp nhiệt động, entropy cung cấp mũi tên cho chiều tự nhiên; ở cấp thống kê, nó xuất hiện từ cách các xác suất phân bố trên không gian trạng thái.

Xem tiếp: [Năng lượng tự do Gibbs](./03_gibbs_free_energy.md).