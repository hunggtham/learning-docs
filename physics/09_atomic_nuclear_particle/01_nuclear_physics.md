# Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**. Route đi từ cấu trúc nhiều nucleon → năng lượng liên kết/độ hụt khối → phóng xạ và định luật bảo toàn → phản ứng hạt nhân → phân hạch/nhiệt hạch, để năng lượng nối với cơ chế.

## Hạt nhân là hệ nhiều hạt tương tác mạnh

Hạt nhân nguyên tử gồm proton và neutron, gọi chung là nucleon. Proton mang điện tích dương; neutron trung hòa điện tổng thể. Cả hai đều là trạng thái liên kết của quark và gluon, nhưng ở thang hạt nhân ta thường dùng nucleon như các bậc tự do hiệu dụng.

Bán kính hạt nhân gần đúng theo

```math
R\approx R_0A^{1/3},
```

với `R_0\approx1.2 fm` và `A` là số khối. Vì thể tích tỉ lệ `R^3`, mật độ vật chất hạt nhân gần như cùng bậc cho nhiều hạt nhân.

Điều này gợi ý lực hạt nhân có tính bão hòa: một nucleon tương tác mạnh chủ yếu với các nucleon lân cận thay vì với toàn bộ hạt nhân theo kiểu lực tầm xa.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, sau nội dung của **Hạt nhân là hệ nhiều hạt tương tác mạnh**, **Năng lượng liên kết và độ hụt khối** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình giọt chất lỏng và công thức bán thực nghiệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lượng liên kết và độ hụt khối

Năng lượng liên kết là

```math
E_b=\Delta mc^2,
```

với

```math
\Delta m=Zm_p+Nm_n-m_{nucleus}.
```

Khối lượng của hạt nhân liên kết nhỏ hơn tổng khối lượng các nucleon tự do vì trạng thái liên kết có năng lượng thấp hơn.

Năng lượng liên kết trên mỗi nucleon tăng nhanh với hạt nhân nhẹ, đạt cực đại gần vùng sắt–nickel rồi giảm chậm ở hạt nhân nặng. Hình dạng này giải thích vì sao cả nhiệt hạch của hạt nhẹ và phân hạch của hạt rất nặng đều có thể giải phóng năng lượng.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Mô hình giọt chất lỏng và công thức bán thực nghiệm** tiếp nhận điểm tựa từ **Năng lượng liên kết và độ hụt khối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình lớp hạt nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình giọt chất lỏng và công thức bán thực nghiệm

Một mô hình hữu ích xem hạt nhân giống một giọt chất lỏng gần không nén được. Năng lượng liên kết bán thực nghiệm thường viết

```math
B(A,Z)=a_vA-a_sA^{2/3}-a_c\frac{Z(Z-1)}{A^{1/3}}
-a_a\frac{(A-2Z)^2}{A}+\delta(A,Z).
```

Các hạng có ý nghĩa:

- `a_vA`: năng lượng thể tích do mỗi nucleon tương tác với láng giềng;
- `a_sA^{2/3}`: hiệu chỉnh bề mặt vì nucleon ở bề mặt có ít láng giềng hơn;
- hạng Coulomb: proton đẩy nhau;
- hạng bất đối xứng: Pauli làm cấu hình quá lệch proton–neutron tốn năng lượng;
- `\delta`: hiệu ứng ghép cặp nucleon.

Công thức này không mô tả chi tiết cấu trúc mức nhưng cho trực giác rất tốt về xu hướng ổn định và phân hạch.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Mô hình lớp hạt nhân** tiếp nhận điểm tựa từ **Mô hình giọt chất lỏng và công thức bán thực nghiệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Q-value của phản ứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình lớp hạt nhân

Một mô hình khác xem mỗi nucleon chuyển động trong một thế trung bình do các nucleon còn lại tạo ra. Các mức lượng tử tạo “lớp vỏ” tương tự nguyên tử nhưng với Hamiltonian khác.

Một số số nucleon đặc biệt như

```text
2, 8, 20, 28, 50, 82, 126
```

cho cấu hình đặc biệt bền và được gọi là số magic.

Spin–orbit coupling mạnh trong hạt nhân là thành phần quan trọng để tái tạo chuỗi số magic quan sát được.

Mô hình giọt chất lỏng và mô hình lớp không loại trừ nhau. Một cái mô tả tốt xu hướng tập thể, cái kia mô tả cấu trúc mức và hiệu ứng vỏ.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Q-value của phản ứng** tiếp nhận điểm tựa từ **Mô hình lớp hạt nhân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiết diện phản ứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Q-value của phản ứng

Với phản ứng

```text
a + A → b + B
```

Q-value là

```math
Q=(m_a+m_A-m_b-m_B)c^2.
```

Nếu `Q>0`, phản ứng giải phóng năng lượng nghỉ thành động năng hoặc photon. Nếu `Q<0`, cần cung cấp năng lượng tối thiểu.

Tuy nhiên ngưỡng năng lượng trong phòng thí nghiệm không nhất thiết chỉ bằng `|Q|` vì động lượng cũng phải bảo toàn. Một phần năng lượng đầu vào phải đi vào chuyển động tâm khối của sản phẩm.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Tiết diện phản ứng** tiếp nhận điểm tựa từ **Q-value của phản ứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Resonance hạt nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiết diện phản ứng

Xác suất phản ứng thường được mô tả bằng tiết diện (cross section) `\sigma`. Tốc độ phản ứng trong chùm hạt có dạng điển hình

```math
R\sim \Phi N\sigma,
```

trong đó `\Phi` là thông lượng hạt tới và `N` là số bia hiệu dụng.

Tiết diện không phải diện tích hình học đơn giản. Nó mã hóa xác suất lượng tử của quá trình và phụ thuộc mạnh vào năng lượng, spin, resonance và kênh phản ứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Resonance hạt nhân** tiếp nhận điểm tựa từ **Tiết diện phản ứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân rã phóng xạ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Resonance hạt nhân

Nếu năng lượng va chạm gần một trạng thái kích thích của hạt nhân hợp chất, tiết diện có thể tăng mạnh. Một dạng Breit–Wigner đơn giản gần resonance là

```math
\sigma(E)\propto
\frac{\Gamma^2/4}{(E-E_R)^2+\Gamma^2/4}.
```

Độ rộng `\Gamma` liên hệ thời gian sống của trạng thái resonance:

```math
\tau\sim\frac{\hbar}{\Gamma}.
```

Đây là cùng cấu trúc thời gian tồn tại (lifetime / 수명)–linewidth đã gặp trong quang phổ nguyên tử.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Phân rã phóng xạ** tiếp nhận điểm tựa từ **Resonance hạt nhân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân rã alpha và xuyên hầm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân rã phóng xạ

Nếu xác suất phân rã trên một đơn vị thời gian là hằng số,

```math
\frac{dN}{dt}=-\lambda N,
```

nên

```math
N(t)=N_0e^{-\lambda t}.
```

Chu kỳ bán rã:

```math
t_{1/2}=\frac{\ln2}{\lambda}.
```

Điểm quan trọng là không thể dự đoán chính xác một hạt nhân đơn lẻ sẽ phân rã lúc nào; mô hình cho phân bố xác suất của tập hợp lớn.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Phân rã alpha và xuyên hầm** tiếp nhận điểm tựa từ **Phân rã phóng xạ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân rã beta và tương tác yếu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân rã alpha và xuyên hầm

Hạt alpha nằm trong một thế hạt nhân sâu nhưng bị ngăn bởi hàng rào Coulomb. Cổ điển, nếu năng lượng thấp hơn đỉnh rào, nó không thể thoát. Lượng tử cho xác suất xuyên hầm hữu hạn.

Xác suất xuyên hầm rất nhạy với độ rộng và chiều cao rào, nên một thay đổi nhỏ năng lượng alpha có thể dẫn tới thay đổi rất lớn chu kỳ bán rã. Đây là cơ sở vật lý của quan hệ Geiger–Nuttall.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Phân rã beta và tương tác yếu** tiếp nhận điểm tựa từ **Phân rã alpha và xuyên hầm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân rã gamma** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân rã beta và tương tác yếu

Ví dụ beta âm:

```math
n\rightarrow p+e^-+\bar\nu_e.
```

Phổ electron liên tục vì năng lượng và động lượng được chia giữa electron, neutrino và hạt nhân giật lùi.

Sự tồn tại của neutrino được đề xuất lịch sử để bảo toàn năng lượng, động lượng và mômen động lượng trong phân rã beta.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Phân rã gamma** tiếp nhận điểm tựa từ **Phân rã beta và tương tác yếu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hoạt độ, liều hấp thụ và liều hiệu dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân rã gamma

Hạt nhân kích thích có thể phát photon gamma để chuyển xuống mức năng lượng thấp hơn. `A` và `Z` có thể giữ nguyên.

Cũng như nguyên tử, xác suất chuyển mức phụ thuộc multipole của bức xạ và quy tắc chọn mômen động lượng/parity.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Hoạt độ, liều hấp thụ và liều hiệu dụng** tiếp nhận điểm tựa từ **Phân rã gamma** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi phân rã** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hoạt độ, liều hấp thụ và liều hiệu dụng

Hoạt độ:

```math
A=\lambda N
```

đơn vị becquerel `Bq`.

Liều hấp thụ:

```math
D=\frac{E_{dep}}{m}
```

đơn vị gray `Gy=J/kg`.

Sievert `Sv` thêm trọng số sinh học theo loại bức xạ và mô. Vì vậy `Bq`, `Gy`, `Sv` không thể đổi qua lại chỉ bằng một hệ số phổ quát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Hoạt độ, liều hấp thụ và liều hiệu dụng** xác định đầu vào; **Chuỗi phân rã** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Phân hạch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi phân rã

Nếu một hạt nhân mẹ phân rã thành hạt nhân con cũng không bền, số hạt của mỗi loại thỏa hệ phương trình Bateman.

Trong trường hợp mẹ sống lâu hơn nhiều con, có thể xuất hiện cân bằng thế tục (secular equilibrium): hoạt độ của hạt con tiến gần hoạt độ của hạt mẹ dù số hạt khác nhau.

Khái niệm này quan trọng trong địa chất phóng xạ và quản lý nguồn bức xạ.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Chuỗi phân rã** xác định đầu vào; **Phân hạch** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Vì sao neutron hữu ích cho phản ứng hạt nhân?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân hạch

Hạt nhân nặng như uranium-235 có thể hấp thụ neutron, tạo hạt nhân hợp chất kích thích rồi tách thành hai mảnh nhẹ hơn, đồng thời giải phóng vài neutron và năng lượng.

Năng lượng đến chủ yếu từ việc sản phẩm có năng lượng liên kết trên nucleon lớn hơn hạt nhân ban đầu.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Vì sao neutron hữu ích cho phản ứng hạt nhân?** tiếp nhận điểm tựa từ **Phân hạch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phản ứng dây chuyền và hệ số nhân** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao neutron hữu ích cho phản ứng hạt nhân?

Neutron không mang điện nên không bị hàng rào Coulomb đẩy khi tiếp cận hạt nhân. Do đó neutron năng lượng thấp vẫn có thể bị hấp thụ hiệu quả bởi nhiều hạt nhân.

Đây là lý do neutron đóng vai trò trung tâm trong lò phản ứng phân hạch.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Phản ứng dây chuyền và hệ số nhân** tiếp nhận điểm tựa từ **Vì sao neutron hữu ích cho phản ứng hạt nhân?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vai trò của neutron trễ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản ứng dây chuyền và hệ số nhân

Một cách mô tả lò phản ứng là hệ số nhân neutron hiệu dụng `k_eff`:

```text
k_eff < 1  → dưới tới hạn
k_eff = 1  → tới hạn
k_eff > 1  → trên tới hạn
```

`k_eff` phụ thuộc xác suất neutron gây phân hạch, bị hấp thụ không phân hạch hoặc thoát khỏi vùng hoạt.

Trong lò phản ứng công suất ổn định, mục tiêu là giữ `k_eff` rất gần 1.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Vai trò của neutron trễ** tiếp nhận điểm tựa từ **Phản ứng dây chuyền và hệ số nhân** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chất làm chậm và thanh điều khiển** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vai trò của neutron trễ

Một phần nhỏ neutron được phát ra sau phân rã của các mảnh phân hạch thay vì tức thời. Dù tỉ lệ nhỏ, neutron trễ làm thang thời gian động lực học lò phản ứng chậm hơn rất nhiều, cho phép điều khiển kỹ thuật.

Nếu chỉ có neutron tức thời, việc kiểm soát công suất sẽ khó hơn đáng kể.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Chất làm chậm và thanh điều khiển** tiếp nhận điểm tựa từ **Vai trò của neutron trễ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phản hồi nhiệt độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chất làm chậm và thanh điều khiển

Neutron nhanh có thể được làm chậm bằng va chạm đàn hồi với vật liệu nhẹ như nước hoặc graphite. Trong một số nhiên liệu, tiết diện phân hạch tăng ở neutron nhiệt.

Thanh điều khiển chứa vật liệu hấp thụ neutron như boron hoặc cadmium để điều chỉnh quần thể neutron.

Lò phản ứng vì vậy là bài toán kết hợp vận chuyển (transport / 전송) neutron, nhiệt học, chất lưu và phản hồi vật liệu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Phản hồi nhiệt độ** tiếp nhận điểm tựa từ **Chất làm chậm và thanh điều khiển** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhiệt hạch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản hồi nhiệt độ

Một lò phản ứng an toàn thường được thiết kế để có các hệ số phản hồi âm quan trọng. Ví dụ nhiệt độ tăng có thể làm giảm mật độ chất làm chậm hoặc thay đổi resonance absorption, từ đó giảm reactivity.

Không thể đánh giá an toàn lò phản ứng chỉ bằng công thức phân hạch đơn lẻ; phải xét toàn hệ động lực học và phản hồi.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Nhiệt hạch** tiếp nhận điểm tựa từ **Phản hồi nhiệt độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gamow factor và Gamow peak** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiệt hạch

Hai hạt nhân nhẹ muốn phản ứng phải tiến đủ gần để tương tác hạt nhân mạnh chi phối. Nhưng trước đó chúng bị đẩy bởi hàng rào Coulomb.

Năng lượng Coulomb điển hình:

```math
V_C(r)\sim\frac{Z_1Z_2e^2}{4\pi\varepsilon_0r}.
```

Ở nhiệt độ sao, năng lượng nhiệt trung bình thường thấp hơn đỉnh rào cổ điển. Xuyên hầm lượng tử làm phản ứng vẫn xảy ra.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Gamow factor và Gamow peak** tiếp nhận điểm tựa từ **Nhiệt hạch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phản ứng D–T** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gamow factor và Gamow peak

Xác suất xuyên hầm qua hàng rào Coulomb giảm gần dạng mũ theo năng lượng. Trong plasma nhiệt, tốc độ phản ứng là kết quả cạnh tranh giữa:

- phân bố Maxwell–Boltzmann giảm mạnh ở năng lượng cao;
- xác suất xuyên hầm tăng mạnh ở năng lượng cao.

Tích hai hiệu ứng tạo vùng năng lượng gọi là Gamow peak, nơi phần lớn phản ứng nhiệt hạch xảy ra.

Điều này giải thích vì sao tốc độ nhiệt hạch rất nhạy với nhiệt độ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Phản ứng D–T** tiếp nhận điểm tựa từ **Gamow factor và Gamow peak** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiêu chuẩn Lawson** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản ứng D–T

Một phản ứng nhiệt hạch được nghiên cứu nhiều là

```math
^2H+^3H\rightarrow ^4He+n+17.6\,MeV.
```

Phần lớn năng lượng đi vào neutron. Điều này thuận lợi cho việc mang năng lượng ra ngoài plasma nhưng đồng thời tạo thách thức vật liệu vì neutron nhanh gây hư hỏng và kích hoạt phóng xạ.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Tiêu chuẩn Lawson** tiếp nhận điểm tựa từ **Phản ứng D–T** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nucleosynthesis trong sao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiêu chuẩn Lawson

Để nhiệt hạch có ý nghĩa năng lượng, plasma cần đủ nhiệt độ, mật độ và thời gian giam giữ. Một tiêu chí điển hình dùng

```math
nT\tau_E.
```

Do đó “đã tạo được plasma rất nóng” chưa đồng nghĩa với nhà máy điện nhiệt hạch đã đạt điều kiện năng lượng ròng.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Nucleosynthesis trong sao** gom các mảnh từ **Tiêu chuẩn Lawson** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nucleosynthesis trong sao

Trong Mặt Trời, chuỗi proton–proton chuyển hydro thành heli. Trong sao nặng hơn, chu trình CNO có thể quan trọng.

Các nguyên tố nặng hơn được tạo qua nhiều giai đoạn đốt hạt nhân và các quá trình bắt neutron như `s-process` và `r-process`.

Vật lý hạt nhân vì vậy trực tiếp giải thích nguồn gốc hóa học của vật chất trong vũ trụ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Nucleosynthesis trong sao** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hạt nhân là hệ nhiều nucleon nơi ba cấu trúc cùng tồn tại:

```text
xu hướng tập thể
+ cấu trúc lớp lượng tử
+ phản ứng và phân rã xác suất
```

Mô hình giọt chất lỏng giải thích xu hướng tập thể; shell mô hình (model / 모델) giải thích mức và số magic; reaction lý thuyết (theory / 이론) giải thích cách hệ chuyển giữa các cấu hình.

Năng lượng hạt nhân không đến từ “phá nguyên tử” một cách chung chung mà từ chênh lệch năng lượng liên kết giữa trạng thái đầu và cuối.

> **Chuyển mạch:** Trong **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Mọi hạt nhân có thể mô tả bằng cùng một mô hình đơn giản”

Không. Collective các mô hình (models / 모델들), shell mô hình (model / 모델) và reaction các mô hình (models / 모델들) nhấn mạnh các cấu trúc khác nhau.

### “Cross section là diện tích vật lý thật của hạt nhân”

Không. Nó là đại lượng xác suất hiệu dụng của quá trình lượng tử.

### “E=mc² nghĩa toàn bộ khối lượng biến thành năng lượng”

Thông thường chỉ chênh lệch khối lượng giữa trạng thái đầu và cuối được chuyển thành dạng năng lượng khác.

### “Fusion chỉ cần đạt nhiệt độ rất cao”

Không. Mật độ và thời gian giam giữ cũng thiết yếu.

### “trọng yếu (critical / 중요) reactor nghĩa sắp phát nổ”

Trong kỹ thuật lò phản ứng, `critical` chỉ có nghĩa `k_eff=1`, tức quần thể neutron duy trì ổn định qua các thế hệ.

> **Chuyển mạch:** Ở chặng này của **Vật lý hạt nhân: mô hình hạt nhân, phân rã, phản ứng, phân hạch và nhiệt hạch**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Các hệ lượng tử](../08_quantum/01_quantum_systems.md), [Động lực học lượng tử và tán xạ](../08_quantum/06_time_dependent_scattering.md), [Năng lượng tương đối tính](../07_relativity/00_special_relativity.md).

**Liên hệ tiếp:** [Bức xạ và detector](02_radiation_detection.md), [Plasma](../10_condensed_matter_devices/03_plasma_physics.md), [Vật lý sao](../11_astrophysics_cosmology/00_stars_compact_objects.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
