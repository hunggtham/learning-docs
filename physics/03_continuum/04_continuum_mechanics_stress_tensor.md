# Cơ học môi trường liên tục: tensor ứng suất, tensor biến dạng và quan hệ vật liệu

Trong cơ học chất điểm, ta thường thay cả vật bằng một điểm và chỉ quan tâm tổng lực. Nhưng khi vật có kích thước hữu hạn, câu hỏi “tổng lực là bao nhiêu?” không đủ. Một thanh bị kéo, một tấm kim loại bị uốn hay một dòng chất lỏng bị cắt đều phụ thuộc vào **lực được phân bố bên trong vật chất như thế nào**.

Cơ học môi trường liên tục (continuum mechanics / 연속체역학) xây dựng mô hình trong đó vật chất được xem là liên tục ở thang quan sát. Thay vì theo dõi từng nguyên tử, ta dùng các trường như mật độ `\rho(\mathbf x,t)`, vận tốc `\mathbf v(\mathbf x,t)`, độ dịch chuyển `\mathbf u(\mathbf x,t)`, nhiệt độ và ứng suất.

## Khi nào xấp xỉ liên tục hợp lý?

Giả thiết liên tục không có nghĩa vật chất thật sự không gồm nguyên tử. Nó nói rằng kích thước đặc trưng của bài toán lớn hơn nhiều khoảng cách vi mô, nên trung bình trên một thể tích nhỏ đã chứa đủ nhiều hạt để các đại lượng như mật độ và ứng suất thay đổi gần trơn.

Một tham số quan trọng trong khí là số Knudsen

```math
Kn=\frac{\lambda}{L},
```

trong đó `\lambda` là quãng đường tự do trung bình và `L` là kích thước đặc trưng. Khi `Kn\ll1`, mô hình liên tục thường tốt. Khi `Kn` không còn nhỏ, mô hình động học phân tử trở nên cần thiết.

## Lực trên một mặt cắt bên trong vật liệu

Tưởng tượng cắt một vật bằng một mặt rất nhỏ có vectơ pháp tuyến đơn vị `\mathbf n`. Phần vật liệu phía bên này tác dụng lên phần bên kia một lực trên đơn vị diện tích gọi là **vectơ lực mặt (traction)**:

```math
\mathbf t(\mathbf n).
```

Điểm quan trọng là traction phụ thuộc hướng của mặt cắt. Một mặt có pháp tuyến khác có thể chịu lực pháp tuyến và lực cắt khác.

Định lý Cauchy cho biết sự phụ thuộc này có thể biểu diễn tuyến tính bằng tensor ứng suất (stress tensor / 응력 텐서):

```math
\mathbf t(\mathbf n)=\boldsymbol\sigma\,\mathbf n.
```

## Tensor ứng suất

Trong hệ tọa độ Cartesian,

```math
\boldsymbol\sigma=
\begin{pmatrix}
\sigma_{xx} & \sigma_{xy} & \sigma_{xz}\\
\sigma_{yx} & \sigma_{yy} & \sigma_{yz}\\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz}
\end{pmatrix}.
```

Các phần tử đường chéo `\sigma_{xx}`, `\sigma_{yy}`, `\sigma_{zz}` là ứng suất pháp. Các phần tử ngoài đường chéo mô tả ứng suất cắt.

Tensor không phải chỉ là “một ma trận nhiều số”. Ý nghĩa hình học của nó là một ánh xạ từ hướng mặt `\mathbf n` sang vectơ lực mặt trên chính mặt đó.

Nếu không có mômen lực thể tích đặc biệt, bảo toàn mômen động lượng dẫn tới

```math
\sigma_{ij}=\sigma_{ji},
```

nên tensor ứng suất đối xứng.

## Áp suất là trường hợp đặc biệt của ứng suất

Trong chất lưu tĩnh lý tưởng, ứng suất không phụ thuộc hướng theo kiểu cắt; nó chỉ là áp suất đẳng hướng:

```math
\boldsymbol\sigma=-pI.
```

Dấu âm theo quy ước thường dùng cho biết áp suất gây nén. Đây là cách nhìn thống nhất: áp suất trong chất lưu không phải một khái niệm hoàn toàn tách khỏi ứng suất trong chất rắn; nó là một trường hợp đặc biệt của tensor ứng suất.

## Biến dạng: dịch chuyển chưa đủ

Trường độ dịch chuyển `\mathbf u(\mathbf x)` cho biết mỗi điểm vật chất đi đâu. Nhưng nếu toàn vật dịch chuyển cứng một khoảng giống nhau, vật không bị biến dạng.

Do đó ta cần đạo hàm của trường dịch chuyển. Với biến dạng nhỏ, tensor biến dạng (strain tensor / 변형률 텐서) là

```math
\varepsilon_{ij}
=\frac12\left(
\frac{\partial u_i}{\partial x_j}
+\frac{\partial u_j}{\partial x_i}
\right).
```

Phần đối xứng này loại bỏ quay cứng bậc nhất và giữ lại kéo dài, nén và cắt thật sự.

Trong kéo một chiều,

```math
\varepsilon_{xx}\approx\frac{\Delta L}{L}.
```

## Biến dạng thể tích và biến dạng cắt

Vết của tensor biến dạng

```math
\mathrm{tr}(\varepsilon)
=\varepsilon_{xx}+\varepsilon_{yy}+\varepsilon_{zz}
```

xấp xỉ độ biến thiên thể tích tương đối khi biến dạng nhỏ.

Phần không đổi thể tích còn lại mô tả thay đổi hình dạng. Phân tách này hữu ích vì nhiều vật liệu phản ứng khác nhau với nén thể tích và cắt.

## Quan hệ vật liệu: nơi “tính chất vật chất” đi vào phương trình

Các định luật bảo toàn không đủ để phân biệt thép, cao su, nước hay mật ong. Ta cần thêm **quan hệ cấu thành (constitutive relation / 구성방정식)** nối ứng suất với biến dạng, tốc độ biến dạng hoặc các biến nội tại khác.

Với vật rắn đàn hồi tuyến tính đẳng hướng,

```math
\sigma_{ij}
=\lambda\,\mathrm{tr}(\varepsilon)\delta_{ij}
+2\mu\varepsilon_{ij},
```

trong đó `\lambda` và `\mu` là các tham số Lamé, còn `\mu` cũng là môđun cắt.

Trong kéo một chiều, quan hệ quen thuộc là

```math
\sigma=E\varepsilon,
```

với `E` là môđun Young. Đây chỉ là một phiên bản đơn giản của quan hệ tensor ba chiều.

## Hệ số Poisson

Khi kéo một thanh theo phương `x`, nó thường co theo phương ngang. Hệ số Poisson

```math
\nu=-\frac{\varepsilon_{transverse}}{\varepsilon_{axial}}
```

mô tả mức co ngang so với giãn dọc.

`E` và `\nu` có thể được dùng thay cho các tham số Lamé trong vật liệu tuyến tính đẳng hướng. Không phải mọi vật liệu đều có `\nu` giống nhau; một số vật liệu đặc biệt còn có hệ số Poisson âm và nở ngang khi bị kéo.

## Phương trình cân bằng động lượng trong môi trường liên tục

Một thể tích nhỏ chịu lực thể tích `\rho\mathbf b` và lực do ứng suất trên biên. Dạng cục bộ của bảo toàn động lượng là

```math
\rho\frac{D\mathbf v}{Dt}
=\nabla\cdot\boldsymbol\sigma+\rho\mathbf b.
```

Phương trình này là phiên bản liên tục của `F=ma`.

Nếu vật ở cân bằng tĩnh,

```math
\nabla\cdot\boldsymbol\sigma+\rho\mathbf b=0.
```

Nếu vật là chất lưu Newton, quan hệ cấu thành của ứng suất dẫn ta tới phương trình Navier–Stokes.

## Từ đàn hồi học tới chất lưu

Với chất rắn đàn hồi, ứng suất phụ thuộc chủ yếu vào biến dạng. Với chất lưu Newton, phần ứng suất nhớt phụ thuộc vào **tốc độ biến dạng**:

```math
\boldsymbol\sigma=-pI+\boldsymbol\tau.
```

Trong trường hợp Newton đơn giản,

```math
\tau_{ij}\propto
\frac{\partial v_i}{\partial x_j}
+\frac{\partial v_j}{\partial x_i}.
```

Nhờ đó cơ học chất rắn và cơ học chất lưu có thể được nhìn trong cùng một khung: định luật bảo toàn giống nhau, nhưng quan hệ cấu thành khác nhau.

## Ứng suất chính

Vì tensor ứng suất đối xứng trong nhiều trường hợp, ta có thể chéo hóa nó. Các trị riêng là **ứng suất chính (principal stresses)** và các vectơ riêng cho các phương mà ứng suất cắt bằng không.

Bài toán trị riêng ở đây có cùng cấu trúc toán học với mode chuẩn trong dao động hoặc trạng thái riêng trong lượng tử, nhưng ý nghĩa vật lý khác hoàn toàn.

## Tiêu chuẩn phá hủy không chỉ dựa vào một thành phần ứng suất

Trong thiết kế vật liệu, vật không nhất thiết hỏng chỉ vì `\sigma_{xx}` vượt một giá trị đơn giản. Trạng thái ứng suất ba chiều có thể cần các tiêu chuẩn như von Mises hoặc Tresca để dự đoán chảy dẻo của kim loại.

Điều này giải thích vì sao một chi tiết chịu ứng suất tổng hợp cần phân tích tensor thay vì chỉ lấy “lực chia diện tích”.

## Sóng đàn hồi

Khi kết hợp bảo toàn động lượng với quan hệ đàn hồi tuyến tính, ta thu được phương trình sóng đàn hồi. Trong chất rắn ba chiều có thể có sóng dọc và sóng ngang vì vật liệu chống được cả nén và cắt.

Đây là nền tảng vật lý của sóng địa chấn P và S. Chất lỏng không có môđun cắt tĩnh nên không truyền sóng ngang đàn hồi như chất rắn trong cùng nghĩa.

## Khi mô hình tuyến tính thất bại?

Quan hệ `\sigma=E\varepsilon` chỉ tốt khi biến dạng nhỏ và vật liệu còn trong miền đàn hồi tuyến tính. Khi ứng suất lớn, vật liệu có thể chảy dẻo, nứt, nhớt–đàn hồi, phụ thuộc lịch sử hoặc thay đổi cấu trúc vi mô.

Cao su có thể chịu biến dạng lớn; polymer phụ thuộc thời gian; vật liệu sinh học có thể phi tuyến và dị hướng. Khi đó cần mô hình cấu thành phức tạp hơn.

## Mô hình tư duy (Mental Model)

Cơ học môi trường liên tục tách bài toán thành ba lớp:

```text
hình học và trường động học
→ định luật bảo toàn
→ quan hệ cấu thành của vật liệu
```

Định luật bảo toàn mang tính phổ quát, còn quan hệ cấu thành chứa “cá tính” của vật liệu. Tensor xuất hiện vì lực và biến dạng phụ thuộc hướng trong không gian ba chiều.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Ứng suất chỉ là lực chia diện tích”

Đó là hình ảnh một chiều. Trong ba chiều, ứng suất phụ thuộc hướng mặt cắt và cần tensor để mô tả đầy đủ.

### “Nếu vật dịch chuyển nhiều thì biến dạng phải lớn”

Không. Một vật có thể tịnh tiến hoặc quay cứng rất xa mà không biến dạng. Biến dạng liên quan chênh lệch dịch chuyển giữa các điểm lân cận.

### “Tensor chỉ là ma trận”

Ma trận là biểu diễn của tensor trong một hệ tọa độ. Tensor bản thân là đối tượng hình học không phụ thuộc cách ta chọn trục.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Cân bằng, đàn hồi và cơ học vật liệu](../01_mechanics/07_statics_elasticity_materials.md), [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Cơ học chất lưu](00_fluids.md), [Dòng rối, lưu biến và vật chất mềm](03_turbulence_rheology_soft_matter.md).
