# Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Ensemble thống kê, partition function và thế nhiệt động lực học**. Route đi từ constraints/ensemble choice → partition function → thermodynamic potentials → fluctuations → canonical/grand-canonical predictions, để xác suất nối với đại lượng đo.

Nhiệt động lực học mô tả hệ bằng các đại lượng vĩ mô như nhiệt độ, áp suất, thể tích và entropy. Cơ học thống kê đặt câu hỏi sâu hơn: **những đại lượng vĩ mô đó xuất hiện như thế nào từ một số lượng khổng lồ trạng thái vi mô?**

Với một hệ chứa cỡ `10^{23}` hạt, theo dõi chính xác vị trí và động lượng của từng hạt gần như không khả thi và cũng không cần thiết. Ta thay câu hỏi “trạng thái vi mô chính xác là gì?” bằng “phân bố xác suất nào trên các trạng thái vi mô phù hợp với những ràng buộc vĩ mô mà ta biết?”.

## Ensemble là gì?

Ensemble thống kê (statistical ensemble / 통계 앙상블) là một tập hợp tưởng tượng gồm rất nhiều bản sao của cùng một hệ, mỗi bản sao có thể ở một trạng thái vi mô khác nhau nhưng cùng thỏa các điều kiện vĩ mô.

Ensemble không phải hàng triệu hệ thật đang tồn tại. Nó là công cụ toán học để biểu diễn sự bất định và thống kê của hệ nhiều hạt.

Ba ensemble quan trọng nhất là:

```text
microcanonical: E, V, N cố định
canonical: T, V, N cố định
grand canonical: T, V, μ cố định
```

Mỗi ensemble tương ứng với một kiểu tương tác khác nhau giữa hệ và môi trường.

> **Chuyển mạch:** Trong **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Ensemble vi chính tắc: hệ cô lập** tiếp nhận điểm tựa từ **Ensemble là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhiệt độ xuất hiện từ entropy như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ensemble vi chính tắc: hệ cô lập

Xét một hệ cô lập với năng lượng `E`, thể tích `V` và số hạt `N` cố định. Trong mô hình cân bằng, các trạng thái vi mô có thể tiếp cận được trong lớp năng lượng tương ứng được xem là có trọng số bằng nhau.

Nếu số trạng thái vi mô tương thích là `\Omega(E,V,N)`, entropy Boltzmann là

```math
S(E,V,N)=k_B\ln\Omega.
```

Công thức cho thấy entropy tăng khi số cách vi mô để hiện thực hóa trạng thái vĩ mô tăng.

> **Chuyển mạch:** Ở chặng này của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Nhiệt độ xuất hiện từ entropy như thế nào?** tiếp nhận điểm tựa từ **Ensemble vi chính tắc: hệ cô lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ensemble chính tắc: hệ tiếp xúc bể nhiệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiệt độ xuất hiện từ entropy như thế nào?

Trong ensemble vi chính tắc,

```math
\frac{1}{T}
=\left(\frac{\partial S}{\partial E}\right)_{V,N}.
```

Đây là một kết quả rất sâu. Nhiệt độ không cần được đưa vào như một khái niệm hoàn toàn độc lập; nó liên hệ với độ dốc của entropy theo năng lượng.

Xét hai hệ `A` và `B` có thể trao đổi năng lượng nhưng tổng năng lượng cố định:

```math
E_A+E_B=E_{tot}.
```

Entropy tổng là

```math
S_{tot}=S_A(E_A)+S_B(E_B).
```

Trạng thái cân bằng cực đại hóa entropy tổng. Điều kiện cực trị cho

```math
\frac{\partial S_A}{\partial E_A}
=
\frac{\partial S_B}{\partial E_B},
```

nên

```math
T_A=T_B.
```

Cân bằng nhiệt vì vậy xuất hiện như hệ quả của tối đa hóa số trạng thái vi mô có thể xảy ra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Ensemble chính tắc: hệ tiếp xúc bể nhiệt** tiếp nhận điểm tựa từ **Nhiệt độ xuất hiện từ entropy như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao hệ số Boltzmann có dạng hàm mũ?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ensemble chính tắc: hệ tiếp xúc bể nhiệt

Bây giờ xét một hệ nhỏ có thể trao đổi năng lượng với một bể nhiệt rất lớn ở nhiệt độ `T`. Năng lượng của hệ không còn cố định.

Xác suất hệ ở trạng thái `i` có năng lượng `E_i` là

```math
p_i=\frac{e^{-\beta E_i}}{Z},
\qquad
\beta=\frac{1}{k_BT}.
```

Trong đó

```math
Z=\sum_i e^{-\beta E_i}
```

là **hàm phân hoạch (partition function / 분배함수)**.

`Z` vừa chuẩn hóa xác suất, vừa chứa gần như toàn bộ thông tin nhiệt động lực học của hệ cân bằng chính tắc.

> **Chuyển mạch:** Trong **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Vì sao hệ số Boltzmann có dạng hàm mũ?** tiếp nhận điểm tựa từ **Ensemble chính tắc: hệ tiếp xúc bể nhiệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hàm phân hoạch là “máy phát” của nhiệt động lực học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao hệ số Boltzmann có dạng hàm mũ?

Xét toàn bộ “hệ nhỏ + bể nhiệt” như một hệ cô lập. Nếu hệ nhỏ có năng lượng `E_i`, bể còn năng lượng `E_{tot}-E_i`.

Số trạng thái của bể tỉ lệ với

```math
\Omega_R\propto e^{S_R/k_B}.
```

Khai triển entropy của bể quanh `E_{tot}`:

```math
S_R(E_{tot}-E_i)
\approx
S_R(E_{tot})-
\left(\frac{\partial S_R}{\partial E}\right)E_i.
```

Vì

```math
\frac{\partial S_R}{\partial E}=\frac1T,
```

ta có

```math
\Omega_R(E_{tot}-E_i)
\propto e^{-E_i/k_BT}.
```

Do đó xác suất của trạng thái hệ nhỏ tỉ lệ

```math
p_i\propto e^{-\beta E_i}.
```

Hệ số Boltzmann không phải một công thức được đoán ra tùy ý; nó xuất hiện từ entropy của bể và điều kiện tổng năng lượng được bảo toàn.

> **Chuyển mạch:** Ở chặng này của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Hàm phân hoạch là “máy phát” của nhiệt động lực học** tiếp nhận điểm tựa từ **Vì sao hệ số Boltzmann có dạng hàm mũ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ: hệ hai mức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàm phân hoạch là “máy phát” của nhiệt động lực học

Từ

```math
Z=\sum_i e^{-\beta E_i},
```

ta có năng lượng Helmholtz

```math
F=-k_BT\ln Z.
```

Năng lượng trung bình là

```math
\langle E\rangle
=-\frac{\partial\ln Z}{\partial\beta}.
```

Phương sai năng lượng là

```math
\langle(\Delta E)^2\rangle
=\frac{\partial^2\ln Z}{\partial\beta^2}.
```

Nhiệt dung ở thể tích không đổi liên hệ trực tiếp với thăng giáng năng lượng:

```math
C_V
=\frac{\langle(\Delta E)^2\rangle}{k_BT^2}.
```

Kết quả này nối một đại lượng đáp ứng vĩ mô với mức thăng giáng vi mô của hệ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Hàm phân hoạch là “máy phát” của nhiệt động lực học** cho ta quy tắc; **Ví dụ: hệ hai mức** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Hệ gồm nhiều phần độc lập** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ: hệ hai mức

Xét một hệ có hai mức năng lượng:

```math
E_0=0,
\qquad
E_1=\epsilon.
```

Hàm phân hoạch là

```math
Z=1+e^{-\beta\epsilon}.
```

Xác suất ở trạng thái kích thích là

```math
p_1=
\frac{e^{-\beta\epsilon}}
{1+e^{-\beta\epsilon}}.
```

Khi `T\to0`, `\beta\to\infty`, nên `p_1\to0`: hệ gần như luôn ở trạng thái cơ bản.

Khi `T\to\infty`, `\beta\to0`, hai trạng thái có xác suất gần bằng nhau:

```math
p_0\approx p_1\approx\frac12.
```

Năng lượng trung bình là

```math
\langle E\rangle
=\epsilon p_1.
```

Ví dụ nhỏ này cho thấy nhiệt độ điều khiển cách hệ phân bố trên các mức năng lượng như thế nào.

> **Chuyển mạch:** Trong **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Ví dụ: hệ hai mức** cho ta quy tắc; **Hệ gồm nhiều phần độc lập** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ensemble đại chính tắc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ gồm nhiều phần độc lập

Nếu hệ gồm hai phần độc lập `A` và `B` với

```math
E=E_A+E_B,
```

thì hàm phân hoạch nhân:

```math
Z=Z_AZ_B.
```

Do

```math
F=-k_BT\ln Z,
```

năng lượng tự do cộng:

```math
F=F_A+F_B.
```

Đây là lý do logarit xuất hiện tự nhiên trong nhiệt động lực học: nó biến cấu trúc nhân của số trạng thái thành đại lượng cộng ở quy mô vĩ mô.

> **Chuyển mạch:** Ở chặng này của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Ensemble đại chính tắc** tiếp nhận điểm tựa từ **Hệ gồm nhiều phần độc lập** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thế hóa học có ý nghĩa gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ensemble đại chính tắc

Nếu hệ có thể trao đổi cả năng lượng lẫn hạt với môi trường, số hạt `N` không cố định. Khi nhiệt độ `T`, thể tích `V` và thế hóa học `\mu` được cố định, ta dùng ensemble đại chính tắc (grand canonical ensemble).

Xác suất trạng thái có năng lượng `E_i` và số hạt `N_i` tỉ lệ

```math
p_i\propto
e^{-\beta(E_i-\mu N_i)}.
```

Hàm phân hoạch đại chính tắc là

```math
\Xi
=\sum_i e^{-\beta(E_i-\mu N_i)}.
```

Thế nhiệt động lực học tương ứng là

```math
\Omega_G=-k_BT\ln\Xi.
```

Ensemble này đặc biệt tự nhiên cho khí lượng tử, hệ hạt trao đổi với reservoir và nhiều bài toán vật chất ngưng tụ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Thế hóa học có ý nghĩa gì?** tiếp nhận điểm tựa từ **Ensemble đại chính tắc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các thế nhiệt động lực học không phải công thức rời rạc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thế hóa học có ý nghĩa gì?

Thế hóa học (chemical potential / 화학 퍼텐셜) đo gần đúng chi phí năng lượng tự do khi thêm một hạt vào hệ trong điều kiện xác định.

Trong nhiệt động lực học,

```math
\mu
=\left(\frac{\partial F}{\partial N}\right)_{T,V}.
```

Khi hai hệ có thể trao đổi hạt, cân bằng hạt đòi hỏi thế hóa học bằng nhau, tương tự cân bằng nhiệt đòi hỏi nhiệt độ bằng nhau.

Điều này cho thấy `T`, `P` và `\mu` đều là những biến cường độ có vai trò điều khiển trao đổi giữa các hệ.

> **Chuyển mạch:** Trong **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Các thế nhiệt động lực học không phải công thức rời rạc** tiếp nhận điểm tựa từ **Thế hóa học có ý nghĩa gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tương đương ensemble và giới hạn nhiệt động lực học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các thế nhiệt động lực học không phải công thức rời rạc

Mỗi thế phù hợp với một bộ biến điều khiển khác nhau:

```text
U(S,V,N)    nội năng
F(T,V,N)    Helmholtz free energy
H(S,P,N)    enthalpy
G(T,P,N)    Gibbs free energy
```

Các phép biến đổi Legendre cho phép đổi biến tự nhiên của mô tả. Ví dụ

```math
F=U-TS,
```

và

```math
G=U-TS+PV.
```

Vì vậy việc chọn thế nhiệt động lực học phù hợp tương tự chọn hệ tọa độ phù hợp: cùng một vật lý nhưng cách mô tả được tối ưu cho các đại lượng được giữ cố định trong bài toán.

> **Chuyển mạch:** Ở chặng này của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Các thế nhiệt động lực học không phải công thức rời rạc** đã nêu tiêu chí phân biệt, còn **Tương đương ensemble và giới hạn nhiệt động lực học** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Thăng giáng tương đối giảm khi hệ lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tương đương ensemble và giới hạn nhiệt động lực học

Với hệ lớn, tương tác ngắn hạn và không có các hiệu ứng bất thường, các ensemble thường cho cùng dự đoán vĩ mô trong giới hạn nhiệt động lực học.

Tuy nhiên ở hệ nhỏ, hệ có tương tác tầm xa hoặc gần một số chuyển pha, khác biệt giữa ensemble có thể trở nên quan trọng. Vì vậy “chọn ensemble nào cũng được” không phải quy tắc tuyệt đối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Tương đương ensemble và giới hạn nhiệt động lực học** đã nêu tiêu chí phân biệt, còn **Thăng giáng tương đối giảm khi hệ lớn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thăng giáng tương đối giảm khi hệ lớn

Với nhiều đại lượng cộng độc lập gần đúng, độ lệch chuẩn thường tăng như

```math
\sqrt N,
```

trong khi giá trị trung bình tăng như

```math
N.
```

Do đó thăng giáng tương đối giảm gần

```math
\frac{1}{\sqrt N}.
```

Đây là một lý do các đại lượng vĩ mô của hệ có `10^{23}` hạt rất ổn định dù chuyển động vi mô liên tục hỗn loạn.

> **Chuyển mạch:** Trong **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Thăng giáng tương đối giảm khi hệ lớn** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Cơ học thống kê không cố dự đoán quỹ đạo của từng hạt. Nó tổ chức không gian các trạng thái vi mô bằng xác suất, rồi dùng ràng buộc vĩ mô để xác định phân bố phù hợp.

Hàm phân hoạch là cầu nối từ **phổ năng lượng vi mô** tới **đại lượng nhiệt động lực học vĩ mô**. Các ensemble khác nhau không phải các lý thuyết khác nhau; chúng là những cách đặt điều kiện biên thống kê khác nhau cho cùng một hệ.

> **Chuyển mạch:** Ở chặng này của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Ensemble là một tập hợp rất nhiều hệ thật”

Không. Đó là một cấu trúc toán học để biểu diễn phân bố trạng thái có thể có.

### “Nhiệt độ chỉ là động năng trung bình”

Câu này chỉ đúng trong một số hệ đơn giản. Định nghĩa tổng quát hơn liên hệ nhiệt độ với đạo hàm entropy hoặc tham số `\beta` của phân bố cân bằng.

### “Hàm phân hoạch chỉ dùng để chuẩn hóa xác suất”

Nó còn sinh ra năng lượng tự do, năng lượng trung bình, entropy, nhiệt dung và nhiều đại lượng đáp ứng thông qua đạo hàm của `\ln Z`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ensemble thống kê, hàm phân hoạch và thế nhiệt động lực học**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Entropy và cơ học thống kê](01_entropy_statistical_mechanics.md), [Nhiệt động lực học](00_thermodynamics.md).

**Liên hệ tiếp:** [Hạt đồng nhất và thống kê lượng tử](../08_quantum/05_identical_particles_quantum_statistics.md), [Vận chuyển trong chất rắn](../10_condensed_matter_devices/02_transport_magnetism_superconductivity.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
