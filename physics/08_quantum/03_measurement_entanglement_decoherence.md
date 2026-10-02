# Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phép đo, entanglement, density matrix và decoherence**. Route đi từ state/observable → measurement probabilities → density matrices → entanglement correlations → environment-induced decoherence, để phép đo nối formalism với mất thông tin pha.

Cơ học lượng tử không chỉ khác cơ học cổ điển ở việc năng lượng bị lượng tử hóa. Khác biệt sâu hơn nằm ở cách trạng thái được biểu diễn, cách các hệ hợp thành với nhau và cách kết quả phép đo xuất hiện từ một trạng thái có thể chứa nhiều khả năng chồng chập.

Chương này tập trung vào bốn cấu trúc liên hệ chặt chẽ: **phép đo (measurement / 측정)**, **rối lượng tử (entanglement / 양자 얽힘)**, **ma trận mật độ (density matrix / 밀도 행렬)** và **mất kết hợp lượng tử (decoherence / 결어긋남)**.

## Trạng thái chồng chập và phép đo

Nếu một trạng thái được khai triển theo các trạng thái riêng của toán tử quan sát `\hat A`,

```math
|\psi\rangle=\sum_n c_n|a_n\rangle,
```

với

```math
\hat A|a_n\rangle=a_n|a_n\rangle,
```

thì quy tắc Born cho xác suất thu được kết quả `a_n` là

```math
P(a_n)=|c_n|^2.
```

Điều này khác một hỗn hợp xác suất cổ điển. Trong chồng chập lượng tử, các hệ số `c_n` là biên độ phức và pha tương đối giữa chúng có thể ảnh hưởng trực tiếp tới giao thoa.

> **Chuyển mạch:** Trong **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Giá trị kỳ vọng và phương sai** tiếp nhận điểm tựa từ **Trạng thái chồng chập và phép đo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phép đo lý tưởng và projector** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giá trị kỳ vọng và phương sai

Với trạng thái thuần,

```math
\langle A\rangle
=
\langle\psi|\hat A|\psi\rangle.
```

Độ phân tán của phép đo được đặc trưng bởi

```math
(\Delta A)^2
=
\langle A^2\rangle-\langle A\rangle^2.
```

Quan hệ bất định tổng quát

```math
\Delta A\,\Delta B
\ge
\frac12|\langle[\hat A,\hat B]\rangle|
```

cho thấy độ bất định không chỉ đến từ máy đo. Nó phản ánh cấu trúc không giao hoán của các toán tử lượng tử.

> **Chuyển mạch:** Ở chặng này của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Phép đo lý tưởng và projector** tiếp nhận điểm tựa từ **Giá trị kỳ vọng và phương sai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **POVM: phép đo tổng quát hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phép đo lý tưởng và projector

Trong mô hình phép đo chiếu (projective measurement), nếu đo đại lượng có các projector `P_n`, xác suất kết quả `n` là

```math
P(n)=\langle\psi|P_n|\psi\rangle.
```

Sau khi thu được kết quả đó, trạng thái được cập nhật thành

```math
|\psi\rangle
\rightarrow
\frac{P_n|\psi\rangle}
{\sqrt{\langle\psi|P_n|\psi\rangle}}.
```

Quy tắc cập nhật này thường được gọi là “sụp đổ hàm sóng”. Tuy nhiên cần phân biệt rõ **formalism dự đoán kết quả đo** với **cách diễn giải bản thể học** xem sự sụp đổ là quá trình vật lý thực, cập nhật thông tin hay hiện tượng nổi lên từ tương tác hệ–môi trường.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **POVM: phép đo tổng quát hơn** tiếp nhận điểm tựa từ **Phép đo lý tưởng và projector** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ hợp thành và tensor sản phẩm (product / 제품)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## POVM: phép đo tổng quát hơn

Không phải mọi phép đo thực tế đều tương ứng với một tập projector trực giao lý tưởng. Một mô tả tổng quát hơn dùng các toán tử dương `E_i` thỏa

```math
E_i\ge0,
```

và

```math
\sum_iE_i=I.
```

Xác suất kết quả `i` là

```math
P(i)=\mathrm{Tr}(\rho E_i).
```

Cấu trúc này gọi là phép đo POVM (positive operator-valued measure). Nó rất hữu ích khi detector có hiệu suất hữu hạn, kết quả không hoàn toàn phân biệt được hoặc phép đo chỉ trích xuất một phần thông tin.

> **Chuyển mạch:** Trong **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Hệ hợp thành và tensor sản phẩm (product / 제품)** tiếp nhận điểm tựa từ **POVM: phép đo tổng quát hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ma trận mật độ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ hợp thành và tensor sản phẩm (product / 제품)

Nếu có hai hệ `A` và `B`, không gian trạng thái toàn hệ là tích tensor

```math
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B.
```

Một trạng thái tách được có dạng

```math
|\Psi\rangle=|\psi_A\rangle\otimes|\psi_B\rangle.
```

Nhưng không phải mọi trạng thái đều phân tích được như vậy. Ví dụ trạng thái Bell

```math
|\Phi^+\rangle
=
\frac{1}{\sqrt2}
(|00\rangle+|11\rangle)
```

là trạng thái rối.

Trong trạng thái này, không thể gán một trạng thái thuần độc lập cho từng qubit mà vẫn giữ toàn bộ thông tin của hệ.

> **Chuyển mạch:** Ở chặng này của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Ma trận mật độ** tiếp nhận điểm tựa từ **Hệ hợp thành và tensor sản phẩm (product / 제품)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trạng thái thuần và hỗn hợp khác nhau thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận mật độ

Với trạng thái thuần,

```math
\rho=|\psi\rangle\langle\psi|.
```

Với hỗn hợp thống kê,

```math
\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|.
```

Giá trị kỳ vọng của toán tử `\hat A` là

```math
\langle A\rangle=\mathrm{Tr}(\rho\hat A).
```

Ma trận mật độ là ngôn ngữ tự nhiên khi hệ con rối với môi trường hoặc khi ta không biết hệ đang ở trạng thái thuần nào trong một tập hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Trạng thái thuần và hỗn hợp khác nhau thế nào?** tiếp nhận điểm tựa từ **Ma trận mật độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partial dấu vết (trace / 추적) và trạng thái của hệ con** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái thuần và hỗn hợp khác nhau thế nào?

Với trạng thái thuần,

```math
\rho^2=\rho,
```

và

```math
\mathrm{Tr}(\rho^2)=1.
```

Với hỗn hợp thực sự,

```math
\mathrm{Tr}(\rho^2)<1.
```

Đại lượng `\mathrm{Tr}(\rho^2)` gọi là độ tinh khiết (purity). Nó cho biết trạng thái gần thuần hay bị trộn mạnh đến mức nào.

> **Chuyển mạch:** Trong **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Partial dấu vết (trace / 추적) và trạng thái của hệ con** tiếp nhận điểm tựa từ **Trạng thái thuần và hỗn hợp khác nhau thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bell inequality và giới hạn của mô hình biến ẩn cục bộ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partial dấu vết (trace / 추적) và trạng thái của hệ con

Nếu toàn hệ `AB` có ma trận mật độ `\rho_{AB}`, trạng thái hiệu dụng của riêng hệ `A` là

```math
\rho_A=\mathrm{Tr}_B(\rho_{AB}).
```

Ví dụ với trạng thái Bell, toàn hệ ở trạng thái thuần nhưng từng qubit riêng lẻ có

```math
\rho_A=\frac12I.
```

Đây là một kết quả rất quan trọng: **toàn hệ có thể biết hoàn toàn nhưng hệ con vẫn được mô tả như một trạng thái trộn** vì thông tin nằm trong tương quan giữa các phần.

> **Chuyển mạch:** Ở chặng này của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Partial dấu vết (trace / 추적) và trạng thái của hệ con** đã nêu tiêu chí phân biệt, còn **Bell inequality và giới hạn của mô hình biến ẩn cục bộ** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **No-signalling: vì sao entanglement không truyền thông tin tức thời?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bell inequality và giới hạn của mô hình biến ẩn cục bộ

Rối lượng tử tạo các tương quan mạnh hơn những gì một lớp rộng các lý thuyết biến ẩn cục bộ cho phép. Bất đẳng thức Bell cung cấp một tiêu chuẩn thực nghiệm để phân biệt.

Trong dạng CHSH, một số mô hình cục bộ thỏa giới hạn

```math
|S|\le2,
```

trong khi cơ học lượng tử cho phép tới

```math
|S|\le2\sqrt2.
```

Nhiều thí nghiệm đã quan sát vi phạm bất đẳng thức Bell phù hợp với dự đoán lượng tử.

Điều này không có nghĩa thông tin có thể được gửi nhanh hơn ánh sáng. Các tương quan chỉ được xác nhận sau khi so sánh dữ liệu bằng kênh cổ điển.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Bell inequality và giới hạn của mô hình biến ẩn cục bộ** đã nêu tiêu chí phân biệt, còn **No-signalling: vì sao entanglement không truyền thông tin tức thời?** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mất kết hợp lượng tử bắt đầu từ đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## No-signalling: vì sao entanglement không truyền thông tin tức thời?

Giả sử Alice và Bob chia sẻ một trạng thái rối. Việc Alice chọn phép đo khác nhau có thể thay đổi tương quan thống kê chung, nhưng phân bố kết quả cục bộ mà Bob nhìn thấy một mình vẫn không cho biết Alice đã chọn gì.

Về mặt ma trận mật độ, phép biến đổi cục bộ của Alice không cho Bob một cách điều khiển `\rho_B` để mã hóa tín hiệu tùy ý vượt tốc độ ánh sáng.

Đây là khác biệt quan trọng giữa **tương quan phi cổ điển** và **khả năng truyền thông tin có kiểm soát**.

> **Chuyển mạch:** Trong **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Mất kết hợp lượng tử bắt đầu từ đâu?** tiếp nhận điểm tựa từ **No-signalling: vì sao entanglement không truyền thông tin tức thời?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao phần tử ngoài đường chéo quan trọng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mất kết hợp lượng tử bắt đầu từ đâu?

Một hệ thực hiếm khi cô lập hoàn toàn. Giả sử trạng thái ban đầu là

```math
(\alpha|0\rangle+\beta|1\rangle)|E_0\rangle.
```

Sau tương tác với môi trường,

```math
\alpha|0\rangle|E_0'\rangle
+
\beta|1\rangle|E_1'\rangle.
```

Nếu hai trạng thái môi trường trở nên gần trực giao,

```math
\langle E_0'|E_1'\rangle\approx0,
```

thì khi lấy partial dấu vết (trace / 추적) trên môi trường, các phần tử ngoài đường chéo của ma trận mật độ hệ giảm mạnh.

Đó là cơ chế cốt lõi của decoherence.

> **Chuyển mạch:** Ở chặng này của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Vì sao phần tử ngoài đường chéo quan trọng?** tiếp nhận điểm tựa từ **Mất kết hợp lượng tử bắt đầu từ đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pointer states và cơ sở ưu tiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao phần tử ngoài đường chéo quan trọng?

Xét

```math
\rho=
\begin{pmatrix}
|\alpha|^2 & \alpha\beta^*\\
\alpha^*\beta & |\beta|^2
\end{pmatrix}.
```

Các phần tử ngoài đường chéo mang thông tin pha kết hợp. Khi chúng suy giảm,

```math
\rho
\rightarrow
\begin{pmatrix}
|\alpha|^2 & 0\\
0 & |\beta|^2
\end{pmatrix},
```

hệ bắt đầu có hành vi giống hỗn hợp cổ điển đối với các phép đo trong cơ sở tương ứng.

Decoherence vì vậy giải thích tại sao giao thoa giữa các trạng thái vĩ mô khó quan sát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Pointer states và cơ sở ưu tiên** tiếp nhận điểm tựa từ **Vì sao phần tử ngoài đường chéo quan trọng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decoherence không tự giải quyết toàn bộ đo lường (measurement / 측정) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pointer states và cơ sở ưu tiên

Tương tác với môi trường không làm mất coherence như nhau trong mọi cơ sở. Một số trạng thái ổn định hơn dưới tương tác môi trường và trở thành **trạng thái con trỏ (pointer states)**.

Ví dụ vị trí thường được môi trường “theo dõi” mạnh thông qua photon, phân tử khí và tương tác khác, nên các chồng chập giữa vị trí vĩ mô khác nhau mất coherence cực nhanh.

Đây là một lý do thế giới vĩ mô biểu hiện gần cổ điển trong các biến quen thuộc.

> **Chuyển mạch:** Trong **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Pointer states và cơ sở ưu tiên** nêu điều cần giải thích; **Decoherence không tự giải quyết toàn bộ đo lường (measurement / 측정) bài toán (problem / 문제)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Open quantum các hệ thống (systems / 시스템들) và phương trình Lindblad** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decoherence không tự giải quyết toàn bộ đo lường (measurement / 측정) bài toán (problem / 문제)

Decoherence giải thích vì sao interference giữa các nhánh trở nên không quan sát được thực tế và vì sao một cơ sở gần cổ điển xuất hiện.

Nhưng từ ma trận mật độ gần chéo không tự động suy ra tại sao một phép đo cụ thể chỉ cho **một** kết quả mà người quan sát trải nghiệm. Câu hỏi đó phụ thuộc vào cách diễn giải cơ học lượng tử.

Do đó không nên nói “decoherence đã chứng minh Copenhagen” hay “decoherence tự động sinh collapse thật”.

> **Chuyển mạch:** Ở chặng này của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Decoherence không tự giải quyết toàn bộ đo lường (measurement / 측정) bài toán (problem / 문제)** nêu điều cần giải thích; **Open quantum các hệ thống (systems / 시스템들) và phương trình Lindblad** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **T1 và T2 trong qubit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Open quantum các hệ thống (systems / 시스템들) và phương trình Lindblad

Khi không theo dõi chi tiết môi trường, tiến hóa của hệ con thường không còn unitary. Một mô hình Markov phổ biến là phương trình Lindblad

```math
\frac{d\rho}{dt}
=
-\frac{i}{\hbar}[H,\rho]
+
\sum_k
\left(
L_k\rho L_k^\dagger
-
\frac12\{L_k^\dagger L_k,\rho\}
\right).
```

Phần đầu là tiến hóa Schrödinger quen thuộc; các toán tử `L_k` mô tả các kênh mất coherence, relaxation hoặc noise.

Đây là cầu nối trực tiếp tới qubit thực, laser, cộng hưởng từ, quantum sensing và vật lý chất rắn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **T1 và T2 trong qubit** tiếp nhận điểm tựa từ **Open quantum các hệ thống (systems / 시스템들) và phương trình Lindblad** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên hệ với tính toán lượng tử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## T1 và T2 trong qubit

Trong thực nghiệm lượng tử, hai thời gian đặc trưng thường xuất hiện:

- `T_1`: thời gian thư giãn năng lượng;
- `T_2`: thời gian mất coherence pha.

Thông thường

```math
T_2\le2T_1.
```

Một qubit có `T_1` dài nhưng `T_2` ngắn vẫn không hữu ích cho thuật toán lượng tử dài vì thông tin pha bị mất trước khi năng lượng suy giảm nhiều.

> **Chuyển mạch:** Trong **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Liên hệ với tính toán lượng tử** tiếp nhận điểm tựa từ **T1 và T2 trong qubit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên hệ với tính toán lượng tử

Một qubit có dạng

```math
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle.
```

Thuật toán lượng tử không đơn giản “thử mọi đáp án song song rồi đọc tất cả”. Phép đo chỉ trả lượng thông tin cổ điển hữu hạn. Lợi thế lượng tử đến từ việc điều khiển biên độ và pha bằng phép biến đổi unitary sao cho giao thoa tăng xác suất của thông tin cần rút ra.

Rối lượng tử là tài nguyên quan trọng trong nhiều giao thức, nhưng không phải mọi speedup đều có thể giải thích bằng một câu đơn giản “vì có entanglement”. Cấu trúc thuật toán, oracle, interference và độ phức tạp đều quan trọng.

> **Chuyển mạch:** Ở chặng này của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Những ngộ nhận thường gặp (Common Misconceptions)** tiếp nhận điểm tựa từ **Liên hệ với tính toán lượng tử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Ý thức con người làm hàm sóng sụp đổ”

Formalism chuẩn không cần đưa ý thức thành một biến vật lý. Thiết bị và môi trường có thể tạo entanglement cùng decoherence trước khi con người đọc kết quả.

### “Mixed trạng thái (state / 상태) chỉ là do ta không biết đủ thông tin”

Không phải mọi trạng thái trộn chỉ là thiếu hiểu biết cổ điển. Trạng thái của một hệ con rối với phần còn lại có thể là mixed dù trạng thái toàn hệ đã biết chính xác.

### “Entanglement cho phép truyền tin nhanh hơn ánh sáng”

Không. Nó tạo tương quan phi cổ điển nhưng vẫn tuân nguyên lý no-signalling.

### “Decoherence biến một superposition thành một kết quả duy nhất”

Decoherence làm mất khả năng quan sát coherence giữa các nhánh đối với hệ con, nhưng không tự chọn một kết quả (outcome / 결과) duy nhất trong mọi cách diễn giải.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Những ngộ nhận thường gặp (Common Misconceptions)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phép đo lượng tử không nên được hình dung chỉ là “nhìn vào hạt”. Nó là một chuỗi:

```text
hệ lượng tử
→ tương tác với thiết bị
→ entanglement hệ–thiết bị
→ tương tác với môi trường
→ decoherence
→ tín hiệu vĩ mô có thể ghi lại
```

Ma trận mật độ là ngôn ngữ giúp mô tả chuỗi này mà không cần giả vờ rằng hệ con luôn có một hàm sóng thuần độc lập.

> **Chuyển mạch:** Trong **Phép đo, rối lượng tử, ma trận mật độ và mất kết hợp**, **Liên kết kiến thức (knowledge connection / 지식 연결)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Nền tảng lượng tử](00_quantum_foundations.md), [Spin và mômen động lượng](02_angular_momentum_spin.md), [Hạt đồng nhất và thống kê lượng tử](05_identical_particles_quantum_statistics.md).

**Liên hệ tiếp:** [Lượng tử phụ thuộc thời gian và tán xạ](06_time_dependent_scattering.md), [Entropy và thông tin](../13_connections/00_knowledge_connections.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
