# Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Dao động ghép và normal modes: từ hai lò xo đến phonon**. Route đi từ coupled equations → eigenmodes → normal coordinates → lattice limit → phonon interpretation, để chế độ riêng nối hệ hữu hạn với vật chất liên tục.

Một dao động tử điều hòa đơn chỉ có một bậc tự do và một tần số riêng. Nhưng phần lớn hệ vật lý thực có nhiều bậc tự do tương tác: hai con lắc nối nhau bằng lò xo, các nguyên tử trong phân tử, mạng tinh thể, các phần tử của một cây cầu, mạch LC ghép hoặc các chế độ (mode / 모드) của khoang cộng hưởng. Khi các bậc tự do ghép với nhau, câu hỏi không còn là “tần số riêng của vật này là bao nhiêu?” mà trở thành “toàn hệ có những kiểu chuyển động tự nhiên nào?”.

Những kiểu chuyển động đặc biệt đó gọi là **chế độ (mode / 모드) chuẩn (normal mode / 고유 모드)**. Mỗi chế độ (mode / 모드) chuẩn dao động với một tần số riêng và giữ nguyên hình dạng tương đối giữa các thành phần. Toán học của chế độ (mode / 모드) chuẩn chính là bài toán trị riêng (eigenvalue problem) của đại số tuyến tính.

## Từ hai vật riêng lẻ đến một hệ ghép

Xét hai vật có cùng khối lượng `m`. Mỗi vật nối với tường bằng lò xo có độ cứng `k`, đồng thời giữa hai vật có một lò xo ghép độ cứng `k_c`. Gọi `x_1` và `x_2` là độ dịch chuyển khỏi vị trí cân bằng.

Lực lên vật thứ nhất là

```math
m\ddot x_1=-(k+k_c)x_1+k_cx_2,
```

và vật thứ hai thỏa

```math
m\ddot x_2=k_cx_1-(k+k_c)x_2.
```

Điểm quan trọng là hai phương trình không độc lập: `x_1` xuất hiện trong phương trình của `x_2` và ngược lại. Đây chính là ý nghĩa của **ghép (coupling)**.

Ta viết gọn bằng ma trận:

```math
m\ddot{\mathbf x}+K\mathbf x=0,
```

với

```math
\mathbf x=
\begin{pmatrix}x_1\\x_2\end{pmatrix},
\qquad
K=
\begin{pmatrix}
k+k_c & -k_c\\
-k_c & k+k_c
\end{pmatrix}.
```

Thay vì cố giải hai phương trình cùng lúc bằng cách biến đổi trực tiếp, ta tìm một kiểu chuyển động mà cả hai tọa độ cùng dao động với một tần số `\omega`:

```math
\mathbf x(t)=\mathbf a e^{i\omega t}.
```

Thay vào phương trình cho

```math
(K-m\omega^2I)\mathbf a=0.
```

Muốn có nghiệm khác không, định thức phải bằng không:

```math
\det(K-m\omega^2I)=0.
```

Đây là phương trình trị riêng. Trị riêng liên hệ với `\omega^2`, còn vectơ riêng `\mathbf a` cho biết **hình dạng của chế độ (mode / 모드) (mode shape)**.

> **Nối mạch:** Trong **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Hai chế độ (mode / 모드) tự nhiên của hệ hai vật** nối từ **Từ hai vật riêng lẻ đến một hệ ghép** sang **Vì sao chế độ (mode / 모드) chuẩn “tách” bài toán?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hai chế độ (mode / 모드) tự nhiên của hệ hai vật

Chế độ (mode / 모드) thứ nhất có dạng

```math
\mathbf a_+=(1,1).
```

Hai vật dịch chuyển cùng hướng và cùng biên độ. Lò xo ghép giữa chúng gần như không bị kéo giãn, nên nó không đóng góp thêm lực hồi phục. Khi đó

```math
\omega_+^2=\frac{k}{m}.
```

Chế độ (mode / 모드) thứ hai có dạng

```math
\mathbf a_-=(1,-1).
```

Hai vật chuyển động ngược hướng. Lò xo ghép bị biến dạng mạnh hơn, nên lực hồi phục hiệu dụng lớn hơn:

```math
\omega_-^2=\frac{k+2k_c}{m}.
```

Ta rút ra một nguyên tắc tổng quát: **chế độ (mode / 모드) nào làm biến dạng các liên kết nhiều hơn thường có tần số cao hơn**, vì năng lượng thế tăng nhanh hơn khi biên độ thay đổi.

> **Nối mạch:** Ở chặng này của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Vì sao chế độ (mode / 모드) chuẩn “tách” bài toán?** nối từ **Hai chế độ (mode / 모드) tự nhiên của hệ hai vật** sang **Chuyển động tổng quát là chồng chập các chế độ (mode / 모드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao chế độ (mode / 모드) chuẩn “tách” bài toán?

Trong tọa độ ban đầu `x_1,x_2`, các phương trình bị ghép. Nhưng nếu định nghĩa tọa độ chế độ (mode / 모드)

```math
q_+=\frac{x_1+x_2}{\sqrt2},
\qquad
q_-=\frac{x_1-x_2}{\sqrt2},
```

thì phương trình trở thành hai dao động tử độc lập:

```math
\ddot q_+ +\omega_+^2q_+=0,
```

```math
\ddot q_- +\omega_-^2q_-=0.
```

Đây là ý nghĩa sâu của việc chéo hóa (diagonalization): ta đổi từ các tọa độ “gắn với từng vật” sang các tọa độ “gắn với chuyển động tự nhiên của toàn hệ”. Một hệ phức tạp có thể trở nên đơn giản nếu ta chọn đúng cơ sở.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Chuyển động tổng quát là chồng chập các chế độ (mode / 모드)** nối từ **Vì sao chế độ (mode / 모드) chuẩn “tách” bài toán?** sang **Hiện tượng nhịp và trao đổi năng lượng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chuyển động tổng quát là chồng chập các chế độ (mode / 모드)

Nếu hệ tuyến tính, mọi chuyển động nhỏ có thể viết thành tổng của các chế độ (mode / 모드) chuẩn:

```math
\mathbf x(t)
=c_+\mathbf a_+\cos(\omega_+t+\phi_+)
+c_-\mathbf a_-\cos(\omega_-t+\phi_-).
```

Các hệ số được xác định từ điều kiện ban đầu. Điều này giải thích vì sao một hệ có thể trông rất phức tạp trong không gian tọa độ ban đầu nhưng lại chỉ là tổng của một vài dao động đơn giản trong không gian chế độ (mode / 모드).

> **Nối mạch:** Trong **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Hiện tượng nhịp và trao đổi năng lượng** nối từ **Chuyển động tổng quát là chồng chập các chế độ (mode / 모드)** sang **Hệ nhiều bậc tự do**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hiện tượng nhịp và trao đổi năng lượng

Khi hai tần số riêng gần nhau, chồng chập có thể tạo hiện tượng **nhịp (beats)**. Biên độ của một phần hệ tăng rồi giảm chậm theo thời gian, như thể năng lượng chuyển qua lại giữa hai phần.

Nếu hai dao động có tần số `\omega_1` và `\omega_2` gần nhau, tần số nhịp xấp xỉ

```math
\omega_{beat}=|\omega_1-\omega_2|.
```

Trong hai con lắc ghép yếu, ta có thể quan sát một con lắc ban đầu dao động mạnh rồi chậm dần trong khi con kia mạnh lên, sau đó quá trình đảo lại. Tổng năng lượng gần như bảo toàn nhưng phân bố năng lượng giữa các bậc tự do thay đổi theo thời gian.

> **Nối mạch:** Ở chặng này của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Hệ nhiều bậc tự do** nối từ **Hiện tượng nhịp và trao đổi năng lượng** sang **Từ chuỗi lò xo đến sóng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hệ nhiều bậc tự do

Với `N` bậc tự do nhỏ quanh cân bằng, phương trình thường có dạng

```math
M\ddot{\mathbf x}+K\mathbf x=0,
```

trong đó `M` là ma trận khối lượng và `K` là ma trận độ cứng. Tìm nghiệm dạng

```math
\mathbf x=\mathbf a e^{i\omega t}
```

cho bài toán trị riêng tổng quát

```math
K\mathbf a=\omega^2M\mathbf a.
```

Mỗi nghiệm cho một tần số riêng và một hình dạng chế độ (mode / 모드). Trong kỹ thuật kết cấu, chính các chế độ (mode / 모드) này quyết định cách tòa nhà, cánh máy bay hoặc cầu phản ứng với động đất, gió và rung động máy móc.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Hệ nhiều bậc tự do** đặt đầu vào cho **Từ chuỗi lò xo đến sóng**, rồi **Từ mạng tinh thể đến phonon** mở rộng hệ quả hoặc giới hạn liên quan.

## Từ chuỗi lò xo đến sóng

Hãy tưởng tượng `N` khối lượng nối liên tiếp bằng lò xo. Khi `N` lớn, số chế độ (mode / 모드) tăng. Các chế độ (mode / 모드) có bước sóng dài biểu diễn nhiều khối chuyển động gần cùng pha, còn chế độ (mode / 모드) tần số cao có sự đổi dấu nhanh giữa các khối lân cận.

Khi khoảng cách giữa các khối tiến tới rất nhỏ và số phần tử rất lớn, chuỗi rời rạc chuyển dần thành môi trường liên tục và phương trình chế độ (mode / 모드) tiến tới phương trình sóng. Vì vậy **sóng có thể được hiểu như giới hạn liên tục của một hệ rất nhiều dao động tử ghép**.

> **Nối mạch:** Trong **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Từ chuỗi lò xo đến sóng** đặt đầu vào cho **Từ mạng tinh thể đến phonon**, rồi **Chế độ (mode / 모드) chuẩn và đối xứng** mở rộng hệ quả hoặc giới hạn liên quan.

## Từ mạng tinh thể đến phonon

Trong tinh thể, các nguyên tử dao động quanh vị trí cân bằng và tương tác với nguyên tử lân cận. Ở chế độ dao động nhỏ, bài toán cũng phân rã thành các chế độ (mode / 모드) chuẩn của mạng. Khi lượng tử hóa các chế độ (mode / 모드) đó, mỗi lượng tử kích thích được gọi là **phonon (포논)**.

Điều này tạo cầu nối trực tiếp:

```text
dao động ghép cổ điển
→ mode chuẩn
→ sóng mạng tinh thể
→ lượng tử hóa mode
→ phonon
```

Phonon đóng vai trò quan trọng trong nhiệt dung, độ dẫn nhiệt, tán xạ electron và siêu dẫn thông thường.

> **Nối mạch:** Ở chặng này của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Chế độ (mode / 모드) chuẩn và đối xứng** nối từ **Từ mạng tinh thể đến phonon** sang **Khi phương pháp chế độ (mode / 모드) chuẩn không còn đủ?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chế độ (mode / 모드) chuẩn và đối xứng

Đối xứng thường giúp đoán trước dạng chế độ (mode / 모드). Với hai vật giống nhau, hệ bất biến khi đổi chỗ hai vật. Vì vậy hai chế độ (mode / 모드) tự nhiên có thể chọn thành chế độ (mode / 모드) đối xứng `(1,1)` và phản đối xứng `(1,-1)`.

Trong hệ lớn hơn, đối xứng tinh thể hoặc hình học công trình có thể phân loại các chế độ (mode / 모드) thành những họ khác nhau. Đây là một ví dụ về việc đối xứng làm giảm độ phức tạp trước khi ta thực hiện toàn bộ phép tính.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Khi phương pháp chế độ (mode / 모드) chuẩn không còn đủ?** nối từ **Chế độ (mode / 모드) chuẩn và đối xứng** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khi phương pháp chế độ (mode / 모드) chuẩn không còn đủ?

Phân tích chế độ (mode / 모드) chuẩn dựa mạnh vào giả thiết tuyến tính hóa quanh cân bằng. Khi biên độ lớn, độ cứng phụ thuộc biến dạng hoặc các chế độ (mode / 모드) tương tác phi tuyến, năng lượng có thể truyền giữa các chế độ (mode / 모드) theo cách mà mô hình tuyến tính không dự đoán được.

Ngoài ra, tắt dần mạnh hoặc lực kích thích phi tuyến có thể làm các chế độ (mode / 모드) không còn độc lập. Khi đó cần dùng động lực học phi tuyến, lý thuyết nhiễu loạn hoặc mô phỏng số.

> **Nối mạch:** Trong **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Khi phương pháp chế độ (mode / 모드) chuẩn không còn đủ?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Chế độ (mode / 모드) chuẩn là “ngôn ngữ tự nhiên” của một hệ tuyến tính nhiều bậc tự do. Tọa độ gắn với từng vật giúp ta hình dung hình học, nhưng tọa độ chế độ (mode / 모드) giúp ta hiểu động lực học. Việc tìm chế độ (mode / 모드) tương đương với tìm một cơ sở trong đó hệ ghép trở thành gần như độc lập.

> **Nối mạch:** Ở chặng này của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, **Những ngộ nhận thường gặp (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Những ngộ nhận thường gặp (Common Misconceptions)

“chế độ (mode / 모드) chuẩn là một vật thể riêng trong hệ” là sai. chế độ (mode / 모드) là một mẫu chuyển động của **toàn hệ**.

“Mỗi phần tử có một tần số riêng nên hệ `N` phần tử chỉ cần dùng các tần số của từng phần tử” cũng sai. Khi có ghép, tần số riêng thuộc về toàn hệ và phụ thuộc cấu trúc ghép.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Dao động ghép và chế độ (mode / 모드) chuẩn: từ hai lò xo đến phonon**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Dao động, tắt dần và cộng hưởng](00_oscillations_resonance.md), [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Sóng và Fourier](01_waves_fourier_sound.md), [Tinh thể và dải năng lượng](../10_condensed_matter_devices/00_crystals_bands.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
