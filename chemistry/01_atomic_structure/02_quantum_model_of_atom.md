# Mô hình lượng tử của nguyên tử

> **Mô hình cơ học lượng tử (quantum mechanical model / 양자역학적 원자 모형)** không mô tả electron như một hạt nhỏ bay trên quỹ đạo xác định quanh hạt nhân. Thay vào đó, trạng thái của electron được mô tả bằng **hàm sóng (wavefunction)** \(\psi\), và từ hàm sóng ta tính được xác suất tìm thấy electron trong các vùng không gian khác nhau.

Nếu mô hình Bohr trả lời bằng các quỹ đạo có bán kính xác định, cơ học lượng tử đặt một câu hỏi sâu hơn: với một trạng thái electron nhất định, phân bố xác suất trong không gian có hình dạng ra sao, năng lượng bị lượng tử hóa như thế nào, và những đại lượng nào có thể được biết đồng thời?

## Vì sao mô hình cổ điển không đủ

Trong cơ học cổ điển, nếu biết vị trí và vận tốc của một vật tại một thời điểm, về nguyên tắc ta có thể dự đoán quỹ đạo của nó về sau. Cách nghĩ này hoạt động rất tốt với vật thể vĩ mô. Nhưng electron không cư xử như một quả cầu nhỏ chuyển động trên một đường đi xác định. Các thí nghiệm giao thoa, quang phổ nguyên tử và hiệu ứng quang điện buộc vật lý phải chấp nhận rằng ở thang nguyên tử, các khái niệm cổ điển “hạt” và “sóng” chỉ là những mô hình giới hạn.

Một trạng thái lượng tử có cấu trúc riêng; tùy phép đo mà kết quả quan sát có thể mang đặc trưng giống hạt hoặc giống sóng.

Xem lại: [Bức xạ điện từ và lượng tử hóa](./01_electromagnetic_radiation_and_quantization.md).

## Hàm sóng và phương trình Schrödinger

Trung tâm của cơ học lượng tử phi tương đối tính là **phương trình Schrödinger (Schrödinger equation / 슈뢰딩거 방정식)**. Với trạng thái dừng, dạng quan trọng trong hóa học là:

\[
\hat{H}\psi=E\psi
\]

Ở đây:

- \(\hat H\) là **toán tử Hamilton (Hamiltonian operator)**, biểu diễn tổng năng lượng của hệ;
- \(\psi\) là hàm sóng;
- \(E\) là năng lượng của trạng thái.

Phương trình có cấu trúc giống một bài toán trị riêng trong đại số tuyến tính:

\[
A\mathbf v=\lambda\mathbf v
\]

Trong cơ học lượng tử, ma trận được thay bằng toán tử, vector được thay bằng hàm sóng, còn trị riêng trở thành giá trị vật lý có thể đo như năng lượng.

Đối với nguyên tử hydrogen, Hamiltonian gồm động năng của electron và thế năng Coulomb giữa electron với proton. Giải phương trình Schrödinger không tạo ra một quỹ đạo; nó tạo ra một họ trạng thái có năng lượng và hình dạng không gian khác nhau. Những nghiệm này dẫn trực tiếp tới khái niệm obitan.

## Hàm sóng không phải mật độ vật chất

Hàm sóng \(\psi\) có thể nhận giá trị dương, âm hoặc phức. Vì vậy bản thân \(\psi\) không phải xác suất. Theo **quy tắc Born (Born rule)**, đại lượng có ý nghĩa xác suất là:

\[
|\psi|^2
\]

\(|\psi|^2\) là **mật độ xác suất (probability density / 확률 밀도)**. Xác suất tìm electron trong một phần tử thể tích nhỏ \(dV\) tỉ lệ với:

\[
|\psi|^2dV
\]

Đây là lý do obitan thường được vẽ như “đám mây electron”. Hình vẽ không nói electron bị nhòe thành vật chất liên tục; nó trực quan hóa vùng có xác suất tìm thấy electron cao.

> **Mô hình tư duy:** obitan không phải đường đi của electron. Obitan là một trạng thái lượng tử có phân bố xác suất trong không gian.

## Chuẩn hóa xác suất

Vì electron phải được tìm thấy ở đâu đó nếu ta khảo sát toàn bộ không gian, hàm sóng hợp lệ phải thỏa:

\[
\int |\psi|^2dV=1
\]

Điều kiện này gọi là **chuẩn hóa (normalization)**. Nó cho thấy xác suất trong cơ học lượng tử không phải phép ẩn dụ; nó được ràng buộc bằng toán học rõ ràng.

## Obitan và các số lượng tử

Khi giải nguyên tử hydrogen, nghiệm được mô tả bằng các **số lượng tử (quantum numbers / 양자수)**. Chúng xuất hiện từ điều kiện toán học để hàm sóng là nghiệm hợp lệ, chứ không phải những con số được đặt ra tùy ý.

### Số lượng tử chính \(n\)

**Số lượng tử chính (principal quantum number / 주양자수)** nhận các giá trị:

\[
n=1,2,3,\dots
\]

Nó liên hệ chủ yếu với mức năng lượng và kích thước đặc trưng của obitan. Với hydrogen:

\[
E_n=-\frac{13.6\;\mathrm{eV}}{n^2}
\]

Khi \(n\) tăng, năng lượng tiến gần 0 từ phía âm, nghĩa là electron bị liên kết yếu hơn với hạt nhân.

### Số lượng tử phụ \(l\)

Với mỗi \(n\):

\[
l=0,1,2,\dots,n-1
\]

Các giá trị tương ứng với các phân lớp:

| \(l\) | Ký hiệu | Phân lớp |
|---:|---|---|
| 0 | s | s |
| 1 | p | p |
| 2 | d | d |
| 3 | f | f |

\(l\) liên quan tới dạng góc của hàm sóng và mômen động lượng quỹ đạo (**orbital angular momentum**).

### Số lượng tử từ \(m_l\)

Với một \(l\) cho trước:

\[
m_l=-l,\dots,0,\dots,+l
\]

Do đó số obitan trong một phân lớp là:

\[
2l+1
\]

Ví dụ, phân lớp p có ba obitan.

### Số lượng tử spin \(m_s\)

Electron còn có **spin (스핀)**, một tính chất lượng tử nội tại không nên hình dung như quả cầu tự quay quanh trục. Khi đo một thành phần spin, electron có hai khả năng:

\[
m_s=+\frac12\quad\text{hoặc}\quad-\frac12
\]

Spin là nền tảng để hiểu nguyên lý loại trừ Pauli, ghép đôi electron, từ tính và cấu hình electron.

## Hình dạng obitan

### Obitan s

Obitan s có đối xứng cầu. Điều này không nghĩa electron nằm trên một mặt cầu; nó nghĩa mật độ xác suất không phụ thuộc hướng mà chủ yếu phụ thuộc khoảng cách tới hạt nhân.

Obitan `1s` có mật độ xác suất lớn gần hạt nhân. Các obitan s có \(n\) lớn hơn xuất hiện thêm **nút xuyên tâm (radial nodes / 방사형 마디)**, là những bán kính mà hàm sóng bằng 0.

### Obitan p

Obitan p thường được minh họa bằng hai thùy đối nhau. Giữa hai thùy là một **mặt nút (nodal plane)** nơi hàm sóng bằng 0.

Hai màu khác nhau thường dùng để biểu diễn **pha của hàm sóng (wavefunction phase)**, không phải điện tích dương và âm.

Pha trở nên đặc biệt quan trọng khi các obitan kết hợp thành obitan phân tử: cùng pha có thể tạo giao thoa tăng cường, trái pha có thể tạo giao thoa triệt tiêu.

### Obitan d và f

Obitan d và f có cấu trúc không gian phức tạp hơn. Trong hóa học vô cơ và hóa học phối trí, hướng của obitan d quyết định cách chúng tương tác với phối tử, từ đó ảnh hưởng màu sắc, từ tính và độ bền của phức chất kim loại chuyển tiếp.

## Nút và cấu trúc hàm sóng

**Nút (node / 마디)** là vùng mà hàm sóng bằng 0. Với obitan kiểu hydrogen:

\[
\text{tổng số nút}=n-1
\]

Trong đó:

\[
\text{số nút góc}=l
\]

và:

\[
\text{số nút xuyên tâm}=n-l-1
\]

Ví dụ, obitan `2p` có một nút góc và không có nút xuyên tâm. Obitan `3s` có hai nút xuyên tâm.

Nút không phải chi tiết trang trí của hình vẽ; chúng phản ánh bản chất sóng của trạng thái lượng tử và ảnh hưởng tới năng lượng, độ chồng phủ obitan và liên kết.

## Mật độ xác suất và xác suất theo bán kính

Mật độ xác suất tại một điểm và xác suất tìm electron ở một khoảng cách nhất định không phải cùng một đại lượng.

Với obitan s, \(|\psi|^2\) có thể lớn nhất tại hạt nhân. Nhưng thể tích của một lớp cầu mỏng ở bán kính \(r\) tăng theo \(4\pi r^2\). Vì vậy **phân bố xác suất theo bán kính (radial probability distribution)** phải tính cả yếu tố hình học này.

Đây là ví dụ đẹp cho việc hình học và xác suất kết hợp trong hóa học lượng tử.

## Trạng thái suy biến

Hai trạng thái khác nhau nhưng có cùng năng lượng gọi là **trạng thái suy biến (degenerate states / 축퇴 상태)**.

Trong nguyên tử hydrogen lý tưởng, các obitan có cùng \(n\) có cùng năng lượng. Nhưng trong nguyên tử nhiều electron, lực đẩy electron–electron và hiệu ứng che chắn làm năng lượng phụ thuộc cả \(n\) và \(l\), nên thứ tự năng lượng phức tạp hơn.

## Vì sao nguyên tử nhiều electron khó hơn hydrogen?

Hydrogen chỉ có một electron nên bài toán chủ yếu là tương tác Coulomb giữa electron và hạt nhân. Trong nguyên tử nhiều electron, mỗi electron vừa bị hạt nhân hút vừa đẩy các electron khác. Chuyển động của chúng liên hệ với nhau nên không còn lời giải đóng đơn giản như hydrogen.

Vì vậy hóa học dùng các **phương pháp xấp xỉ (approximations)** như mô hình obitan, Hartree–Fock, lý thuyết phiếm hàm mật độ (**density functional theory, DFT**) và nhiều phương pháp hóa học tính toán khác.

Điều quan trọng là các obitan nguyên tử quen thuộc trong hóa học tuần hoàn là những mô hình hiệu dụng rất mạnh, nhưng không nên đồng nhất chúng với “đường bay” thật của từng electron.

## Che chắn và khả năng xuyên thấu

Trong nguyên tử nhiều electron, electron lớp trong **che chắn (shielding)** một phần điện tích hạt nhân đối với electron lớp ngoài. Vì vậy electron ngoài không cảm nhận toàn bộ điện tích `+Z`.

Ta thường dùng khái niệm **điện tích hạt nhân hiệu dụng (effective nuclear charge, \(Z_{eff}\))**.

Các obitan cũng khác nhau về **khả năng xuyên thấu (penetration)** vào vùng gần hạt nhân. Với cùng \(n\), obitan s thường xuyên thấu mạnh hơn p, p mạnh hơn d, và d mạnh hơn f. Khả năng xuyên thấu cao hơn thường làm electron cảm nhận lực hút hạt nhân mạnh hơn và có năng lượng thấp hơn.

Đây là cơ sở để hiểu thứ tự năng lượng trong cấu hình electron và xu hướng tuần hoàn.

## Nguyên lý loại trừ Pauli

**Nguyên lý loại trừ Pauli (Pauli exclusion principle / 파울리 배타 원리)** nói rằng hai electron trong cùng một nguyên tử không thể có cùng toàn bộ bốn số lượng tử.

Hệ quả quen thuộc là mỗi obitan chỉ chứa tối đa hai electron và nếu có hai electron thì spin của chúng phải đối nhau.

Pauli không phải quy tắc “electron ghét nhau”; nó xuất phát từ tính chất lượng tử của fermion và cấu trúc phản đối xứng của hàm sóng nhiều electron.

## Từ mô hình lượng tử sang cấu hình electron

Bây giờ ta đã có các mảnh ghép cần thiết:

```text
mức năng lượng
+ obitan
+ spin
+ Pauli
+ che chắn/xuyên thấu
→ cấu hình electron
```

Cấu hình electron cho phép ta nối mô hình lượng tử với hóa học thực tế: bảng tuần hoàn, hóa trị, liên kết và khả năng phản ứng.

## Các hiểu lầm thường gặp

### “Obitan là quỹ đạo electron”

Không. Obitan là trạng thái lượng tử có phân bố xác suất, không phải đường chuyển động cổ điển.

### “Hai thùy p mang điện tích trái dấu”

Không. Dấu khác nhau biểu diễn pha của hàm sóng.

### “Spin là electron tự quay như quả cầu”

Không. Spin là đại lượng lượng tử nội tại; hình ảnh tự quay chỉ là phép so sánh rất hạn chế.

### “Hàm sóng là đám mây vật chất thật”

Không. Hàm sóng là đối tượng toán học; \(|\psi|^2\) cho mật độ xác suất.

### “Các số lượng tử là quy tắc ghi nhớ tùy ý”

Không. Chúng xuất hiện từ cấu trúc nghiệm của phương trình lượng tử và các điều kiện biên.

## Mô hình tư duy

Nguyên tử lượng tử không phải một hệ mặt trời thu nhỏ. Hãy hình dung nó như một **hệ các trạng thái sóng lượng tử bị ràng buộc bởi trường Coulomb của hạt nhân và bởi tương tác electron–electron**. Các trạng thái có hình dạng, năng lượng và tính đối xứng khác nhau; electron phân bố vào các trạng thái đó theo các nguyên lý lượng tử.

Xem tiếp: [Cấu hình electron](./03_electron_configuration.md).