# Dung dịch đệm — kiểm soát biến động của môi trường proton

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Dung dịch đệm — kiểm soát biến động của môi trường proton**. Route đi từ conjugate pair và capacity → Henderson–Hasselbalch → giới hạn pH/capacity → thiết kế buffer; công thức chỉ có nghĩa trong vùng mà các giả định cân bằng còn đúng.

> **Dung dịch đệm (buffer / 완충 용액)** là hệ chứa một cặp acid–cơ sở (base / 기반) liên hợp có khả năng hấp thụ một lượng giới hạn acid hoặc cơ sở (base / 기반) được thêm vào, làm pH thay đổi ít hơn so với dung dịch không có đệm.

Dung dịch đệm không “giữ pH cố định tuyệt đối”. Nó chỉ làm hệ ít nhạy hơn trước nhiễu loạn acid–cơ sở (base / 기반) trong một khoảng dung lượng hữu hạn.

## Cơ chế hoạt động của dung dịch đệm

Với cặp:

\[
HA/A^-
\]

`HA` là kho dự trữ có thể trung hòa cơ sở (base / 기반) mạnh, còn `A-` là kho dự trữ có thể nhận proton từ acid mạnh.

Khi thêm acid:

\[
A^-+H^+\rightarrow HA
\]

Khi thêm cơ sở (base / 기반):

\[
HA+OH^-\rightarrow A^-+H_2O
\]

Thay vì để toàn bộ `H+` hoặc `OH-` mới thêm tồn tại tự do, hệ chuyển chúng thành dạng acid hoặc cơ sở (base / 기반) yếu hơn. Kết quả là pH chỉ thay đổi theo sự thay đổi tỉ lệ `A-/HA`.

> **Chuyển mạch:** Cơ chế đệm biến acid hoặc base mạnh thành dạng liên hợp yếu hơn, nên pH phụ thuộc vào tỉ lệ (A^-/HA). **Phương trình Henderson–Hasselbalch** viết chính xác tỉ lệ đó thành công cụ tính; mục kế tiếp diễn giải khi nào phép xấp xỉ này hữu ích.

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

> **Chuyển mạch:** Từ (K_a), phương trình Henderson–Hasselbalch liên hệ pH với tỉ lệ base liên hợp/acid; khi tỉ lệ bằng 1 thì pH xấp xỉ (pK_a). **Ý nghĩa của phương trình** xác định cách đọc tỉ lệ và giới hạn trước khi chọn khoảng đệm thực hành.

## Ý nghĩa của phương trình

Nếu:

\[
[A^-]=[HA]
\]

thì:

\[
pH=pK_a
\]

Nếu tỉ lệ cơ sở (base / 기반)/acid tăng 10 lần, pH tăng khoảng 1 đơn vị trong điều kiện xấp xỉ phù hợp.

Vì sự phụ thuộc logarithm, dung dịch đệm có thể hấp thụ một lượng acid/cơ sở (base / 기반) đáng kể mà pH chỉ thay đổi vừa phải cho tới khi một thành phần gần cạn.

> **Chuyển mạch:** Phương trình cho biết tỉ lệ (A^-/HA) điều khiển pH; **Khoảng đệm** đặt tỉ lệ đó vào vùng khoảng (pK_a\pm1), nơi cả hai dạng còn đủ để phản ứng. Nhưng khoảng pH chưa nói hệ chịu được bao nhiêu acid/base, nên cần chuyển sang **Dung lượng đệm**.

## Khoảng đệm

Khoảng hoạt động hữu ích thường gần:

\[
pH\approx pK_a\pm1
\]

vì khi đó tỉ lệ:

\[
0.1\lesssim\frac{[A^-]}{[HA]}\lesssim10
\]

và cả hai kho acid/cơ sở (base / 기반) vẫn có lượng đáng kể.

Đây chỉ là hướng dẫn thực hành, không phải ranh giới vật lý cứng.

> **Chuyển mạch:** Khoảng đệm mô tả vùng pH hoạt động, còn **Dung lượng đệm** phụ thuộc lượng tuyệt đối của cả (HA) và (A^-), không chỉ tỉ lệ. Khi biết tải acid/base cần hấp thụ, **Thiết kế dung dịch đệm** sẽ chọn nồng độ và thể tích phù hợp.

## Dung lượng đệm

Hai dung dịch có cùng pH có thể chống lại lượng acid/cơ sở (base / 기반) thêm vào rất khác nhau.

Ví dụ:

```text
0.001 M HA + 0.001 M A−
```

và:

```text
1.0 M HA + 1.0 M A−
```

có cùng tỉ lệ và gần cùng pH, nhưng dung dịch thứ hai chứa lượng dự trữ acid/cơ sở (base / 기반) lớn hơn rất nhiều.

Đại lượng mô tả khả năng này là **dung lượng đệm (buffer capacity / 완충 용량)**.

Một định nghĩa vi phân thường dùng:

\[
\beta=\frac{dn_{cơ sở (base / 기반)\ mạnh}}{V\,d(pH)}
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

vì lúc đó cả dạng acid và cơ sở (base / 기반) đều hiện diện nhiều.

> **Chuyển mạch:** Ở chặng này của **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Thiết kế dung dịch đệm** tiếp nhận điểm tựa từ **Dung lượng đệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuẩn bị đệm bằng cách trộn cặp liên hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết kế dung dịch đệm

Để chọn đệm cho pH mục tiêu, trước hết chọn acid/cơ sở (base / 기반) liên hợp có:

\[
pK_a\approx pH_{mục\ tiêu}
\]

Sau đó dùng:

\[
\frac{[A^-]}{[HA]}=10^{pH-pK_a}
\]

để xác định tỉ lệ.

Tổng nồng độ được chọn dựa trên dung lượng đệm cần thiết, độ tan, lực ion và các ràng buộc thực nghiệm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Chuẩn bị đệm bằng cách trộn cặp liên hợp** tiếp nhận điểm tựa từ **Thiết kế dung dịch đệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thêm acid mạnh hoặc cơ sở (base / 기반) mạnh vào đệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuẩn bị đệm bằng cách trộn cặp liên hợp

Có thể trộn trực tiếp acid yếu và muối của cơ sở (base / 기반) liên hợp, chẳng hạn:

```text
CH3CO2H + CH3CO2Na
```

với tỉ lệ phù hợp.

Một cách khác là trung hòa một phần acid yếu bằng cơ sở (base / 기반) mạnh:

\[
HA+OH^-\rightarrow A^-+H_2O
\]

Nếu 40% acid bị trung hòa, sau phản ứng gần đúng:

```text
HA còn lại: 60%
A− tạo thành: 40%
```

Từ đó có thể tính tỉ lệ `A-/HA`.

> **Chuyển mạch:** Trong **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Thêm acid mạnh hoặc cơ sở (base / 기반) mạnh vào đệm** tiếp nhận điểm tựa từ **Chuẩn bị đệm bằng cách trộn cặp liên hợp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pha loãng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thêm acid mạnh hoặc cơ sở (base / 기반) mạnh vào đệm

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

Khi thêm cơ sở (base / 기반) mạnh:

\[
HA+OH^-\rightarrow A^-+H_2O
\]

thì điều chỉnh số mol theo chiều ngược lại.

### Giai đoạn 2: thiết lập lại cân bằng acid yếu

Dùng các lượng mới trong Henderson–Hasselbalch hoặc giải cân bằng chính xác hơn.

Không nên đưa trực tiếp lượng `H+` vừa thêm vào công thức Henderson–Hasselbalch mà bỏ qua bước stoichiometric.

> **Chuyển mạch:** Ở chặng này của **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Pha loãng** tiếp nhận điểm tựa từ **Thêm acid mạnh hoặc cơ sở (base / 기반) mạnh vào đệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hoạt độ và dung dịch đệm đậm đặc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Hoạt độ và dung dịch đệm đậm đặc** tiếp nhận điểm tựa từ **Pha loãng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh hưởng của nhiệt độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Ảnh hưởng của nhiệt độ** tiếp nhận điểm tựa từ **Hoạt độ và dung dịch đệm đậm đặc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ đệm sinh học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh hưởng của nhiệt độ

`K_a` và `K_w` đều phụ thuộc nhiệt độ nên pH của một dung dịch đệm có thể thay đổi khi nhiệt độ đổi dù thành phần hóa học không đổi.

Trong phép đo chính xác hoặc thí nghiệm sinh hóa, cần quan tâm **hệ số nhiệt độ của đệm (temperature coefficient)**.

> **Chuyển mạch:** Ở chặng này của **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Hệ đệm sinh học** tiếp nhận điểm tựa từ **Ảnh hưởng của nhiệt độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chọn đệm trong phòng thí nghiệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ đệm sinh học

### Hệ bicarbonate trong máu

Cặp `CO2/HCO3-` tham gia điều hòa pH máu.

Khác với cốc dung dịch đóng, cơ thể là hệ mở: phổi điều chỉnh `CO2`, còn thận điều chỉnh bicarbonate và proton. Vì vậy pH máu được điều khiển bởi một hệ phản hồi hóa học–sinh lý chứ không chỉ một cặp acid/cơ sở (base / 기반) tĩnh.

### Hệ phosphate

Cặp:

\[
H_2PO_4^-/HPO_4^{2-}
\]

quan trọng trong môi trường nội bào và hóa học thận.

### Protein

Các nhóm ion hóa trên protein, đặc biệt histidine trong một số vùng pH, cũng đóng góp vào khả năng đệm.

Protein là hệ đa proton chứ không phải một cặp `HA/A-` duy nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Chọn đệm trong phòng thí nghiệm** tiếp nhận điểm tựa từ **Hệ đệm sinh học** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các hiểu lầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Các hiểu lầm thường gặp** tiếp nhận điểm tựa từ **Chọn đệm trong phòng thí nghiệm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các hiểu lầm thường gặp

### “Dung dịch đệm giữ pH hoàn toàn không đổi”

Không. Nó chỉ giảm độ nhạy của pH cho tới khi dung lượng bị vượt quá.

### “Chỉ khi lượng acid và cơ sở (base / 기반) bằng nhau mới tạo đệm”

Không. Bất kỳ hỗn hợp có lượng đáng kể của cả hai dạng liên hợp đều có thể đệm; lượng bằng nhau chỉ cho `pH≈pKa`.

### “Henderson–Hasselbalch luôn chính xác tuyệt đối”

Không. Dạng nồng độ dựa trên xấp xỉ hoạt độ và thích hợp nhất khi cả hai dạng liên hợp có lượng đủ lớn.

> **Chuyển mạch:** Ở chặng này của **Dung dịch đệm — kiểm soát biến động của môi trường proton**, **Mô hình tư duy** gom các mảnh từ **Các hiểu lầm thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

Dung dịch đệm là **hai kho hóa học nối với nhau bằng trao đổi proton**. Tỉ lệ hai kho quyết định pH; tổng kích thước hai kho quyết định dung lượng đệm.

Xem tiếp: [Chuẩn độ acid–base](./04_titration.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
