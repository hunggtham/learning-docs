# Dung dịch đệm — kiểm soát biến động của môi trường proton

> **Dung dịch đệm (buffer / 완충 용액)** là hệ chứa một cặp acid–base liên hợp có khả năng hấp thụ một lượng giới hạn acid hoặc base được thêm vào, làm pH thay đổi ít hơn so với dung dịch không có đệm.

Dung dịch đệm không “giữ pH cố định tuyệt đối”. Nó chỉ làm hệ ít nhạy hơn trước nhiễu loạn acid–base trong một khoảng dung lượng hữu hạn.

## Cơ chế hoạt động của dung dịch đệm

Với cặp:

\[
HA/A^-
\]

`HA` là kho dự trữ có thể trung hòa base mạnh, còn `A-` là kho dự trữ có thể nhận proton từ acid mạnh.

Khi thêm acid:

\[
A^-+H^+\rightarrow HA
\]

Khi thêm base:

\[
HA+OH^-\rightarrow A^-+H_2O
\]

Thay vì để toàn bộ `H+` hoặc `OH-` mới thêm tồn tại tự do, hệ chuyển chúng thành dạng acid hoặc base yếu hơn. Kết quả là pH chỉ thay đổi theo sự thay đổi tỉ lệ `A-/HA`.

## Suy ra phương trình Henderson–Hasselbalch

Bắt đầu từ:

\[
K_a=\frac{[H^+][A^-]}{[HA]}
\]

Sắp xếp lại:

\[
[H^+]=K_a\frac{[HA]}{[A^-]}
\]

Lấy âm logarithm:

\[
pH=pK_a+\log\frac{[A^-]}{[HA]}
\]

Đây là **phương trình Henderson–Hasselbalch (Henderson–Hasselbalch equation)**.

Dạng dùng nồng độ là xấp xỉ của biểu thức nhiệt động đầy đủ dùng hoạt độ.

## Ý nghĩa của phương trình

Nếu:

\[
[A^-]=[HA]
\]

thì:

\[
pH=pK_a
\]

Nếu tỉ lệ base/acid tăng 10 lần, pH tăng khoảng 1 đơn vị trong điều kiện xấp xỉ phù hợp.

Vì sự phụ thuộc logarithm, dung dịch đệm có thể hấp thụ một lượng acid/base đáng kể mà pH chỉ thay đổi vừa phải cho tới khi một thành phần gần cạn.

## Khoảng đệm

Khoảng hoạt động hữu ích thường gần:

\[
pH\approx pK_a\pm1
\]

vì khi đó tỉ lệ:

\[
0.1\lesssim\frac{[A^-]}{[HA]}\lesssim10
\]

và cả hai kho acid/base vẫn có lượng đáng kể.

Đây chỉ là hướng dẫn thực hành, không phải ranh giới vật lý cứng.

## Dung lượng đệm

Hai dung dịch có cùng pH có thể chống lại lượng acid/base thêm vào rất khác nhau.

Ví dụ:

```text
0.001 M HA + 0.001 M A−
```

và:

```text
1.0 M HA + 1.0 M A−
```

có cùng tỉ lệ và gần cùng pH, nhưng dung dịch thứ hai chứa lượng dự trữ acid/base lớn hơn rất nhiều.

Đại lượng mô tả khả năng này là **dung lượng đệm (buffer capacity / 완충 용량)**.

Một định nghĩa vi phân thường dùng:

\[
\beta=\frac{dn_{base\ mạnh}}{V\,d(pH)}
\]

với quy ước dấu tương ứng khi thêm acid.

Với hệ một acid yếu lý tưởng, đóng góp của cặp đệm có dạng gần:

\[
\beta\approx2.303C_T\frac{K_a[H^+]}{(K_a+[H^+])^2}
\]

Dung lượng đệm đạt cực đại gần:

\[
pH=pK_a
\]

vì lúc đó cả dạng acid và base đều hiện diện nhiều.

## Thiết kế dung dịch đệm

Để chọn đệm cho pH mục tiêu, trước hết chọn acid/base liên hợp có:

\[
pK_a\approx pH_{mục\ tiêu}
\]

Sau đó dùng:

\[
\frac{[A^-]}{[HA]}=10^{pH-pK_a}
\]

để xác định tỉ lệ.

Tổng nồng độ được chọn dựa trên dung lượng đệm cần thiết, độ tan, lực ion và các ràng buộc thực nghiệm.

## Chuẩn bị đệm bằng cách trộn cặp liên hợp

Có thể trộn trực tiếp acid yếu và muối của base liên hợp, chẳng hạn:

```text
CH3CO2H + CH3CO2Na
```

với tỉ lệ phù hợp.

Một cách khác là trung hòa một phần acid yếu bằng base mạnh:

\[
HA+OH^-\rightarrow A^-+H_2O
\]

Nếu 40% acid bị trung hòa, sau phản ứng gần đúng:

```text
HA còn lại: 60%
A− tạo thành: 40%
```

Từ đó có thể tính tỉ lệ `A-/HA`.

## Thêm acid mạnh hoặc base mạnh vào đệm

Cách giải nên gồm hai giai đoạn.

### Giai đoạn 1: phản ứng stoichiometric gần hoàn toàn

Khi thêm acid mạnh:

\[
A^-+H^+\rightarrow HA
\]

Nếu thêm `n_H` mol:

\[
n_{A^-}'=n_{A^-}-n_H
\]

\[
n_{HA}'=n_{HA}+n_H
\]

Khi thêm base mạnh:

\[
HA+OH^-\rightarrow A^-+H_2O
\]

thì điều chỉnh số mol theo chiều ngược lại.

### Giai đoạn 2: thiết lập lại cân bằng acid yếu

Dùng các lượng mới trong Henderson–Hasselbalch hoặc giải cân bằng chính xác hơn.

Không nên đưa trực tiếp lượng `H+` vừa thêm vào công thức Henderson–Hasselbalch mà bỏ qua bước stoichiometric.

## Pha loãng

Nếu cả `HA` và `A-` cùng bị pha loãng bởi một hệ số:

\[
\frac{[A^-]}{[HA]}
\]

gần như không đổi nên pH có thể thay đổi rất ít trong mô hình lý tưởng.

Nhưng tổng nồng độ giảm nên **dung lượng đệm giảm**.

Vì vậy:

```text
pH gần như không đổi ≠ khả năng đệm không đổi
```

## Hoạt độ và dung dịch đệm đậm đặc

Dạng nhiệt động đầy đủ phải dùng hoạt độ:

\[
pH=pK_a+\log\frac{a_{A^-}}{a_{HA}}
\]

Ở lực ion đáng kể:

\[
a_i=\gamma_i\frac{c_i}{c^\circ}
\]

nên hệ số hoạt độ có thể làm pH thực khác dự đoán chỉ từ tỉ lệ nồng độ.

Điều này quan trọng trong dịch sinh học, nước biển và dung dịch đệm đậm đặc.

## Ảnh hưởng của nhiệt độ

`K_a` và `K_w` đều phụ thuộc nhiệt độ nên pH của một dung dịch đệm có thể thay đổi khi nhiệt độ đổi dù thành phần hóa học không đổi.

Trong phép đo chính xác hoặc thí nghiệm sinh hóa, cần quan tâm **hệ số nhiệt độ của đệm (temperature coefficient)**.

## Hệ đệm sinh học

### Hệ bicarbonate trong máu

Cặp `CO2/HCO3-` tham gia điều hòa pH máu.

Khác với cốc dung dịch đóng, cơ thể là hệ mở: phổi điều chỉnh `CO2`, còn thận điều chỉnh bicarbonate và proton. Vì vậy pH máu được điều khiển bởi một hệ phản hồi hóa học–sinh lý chứ không chỉ một cặp acid/base tĩnh.

### Hệ phosphate

Cặp:

\[
H_2PO_4^-/HPO_4^{2-}
\]

quan trọng trong môi trường nội bào và hóa học thận.

### Protein

Các nhóm ion hóa trên protein, đặc biệt histidine trong một số vùng pH, cũng đóng góp vào khả năng đệm.

Protein là hệ đa proton chứ không phải một cặp `HA/A-` duy nhất.

## Chọn đệm trong phòng thí nghiệm

Ngoài `pKa`, cần xét:

- độ tan;
- khả năng tạo phức với kim loại;
- độ hấp thụ UV;
- độc tính sinh học;
- ảnh hưởng tới enzyme/protein;
- độ nhạy theo nhiệt độ;
- đóng góp vào lực ion.

Các đệm sinh hóa như phosphate, Tris, HEPES, MES hay MOPS có ưu và nhược điểm khác nhau. Không có dung dịch đệm nào hoàn toàn “trơ” trong mọi thí nghiệm.

## Các hiểu lầm thường gặp

### “Dung dịch đệm giữ pH hoàn toàn không đổi”

Không. Nó chỉ giảm độ nhạy của pH cho tới khi dung lượng bị vượt quá.

### “Chỉ khi lượng acid và base bằng nhau mới tạo đệm”

Không. Bất kỳ hỗn hợp có lượng đáng kể của cả hai dạng liên hợp đều có thể đệm; lượng bằng nhau chỉ cho `pH≈pKa`.

### “Henderson–Hasselbalch luôn chính xác tuyệt đối”

Không. Dạng nồng độ dựa trên xấp xỉ hoạt độ và thích hợp nhất khi cả hai dạng liên hợp có lượng đủ lớn.

## Mô hình tư duy

Dung dịch đệm là **hai kho hóa học nối với nhau bằng trao đổi proton**. Tỉ lệ hai kho quyết định pH; tổng kích thước hai kho quyết định dung lượng đệm.

Xem tiếp: [Chuẩn độ acid–base](./04_titration.md).