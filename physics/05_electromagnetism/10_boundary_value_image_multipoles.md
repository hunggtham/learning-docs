# Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**. Route đi từ Poisson/Laplace → boundary conditions → image charges → multipole expansion → far-field approximation, để thế điện giải quyết hình học phức tạp.

Định luật Coulomb cho trường của các điện tích điểm đã biết. Nhưng trong nhiều bài thực tế, phân bố điện tích bề mặt lại **không được biết trước**. Ta chỉ biết hình học của vật dẫn, điện thế trên biên hoặc tổng điện tích, rồi điện tích tự sắp xếp để thỏa điều kiện cân bằng điện tĩnh.

Vì vậy nhiều bài điện tĩnh nên được nhìn như **bài toán giá trị biên (boundary-value problem / 경계값 문제)**: tìm điện thế `\phi` thỏa phương trình Poisson hoặc Laplace cùng các điều kiện biên phù hợp.

## Từ định luật Gauss đến phương trình Poisson

Trong điện tĩnh,

```math
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0},
```

và

```math
\mathbf E=-\nabla\phi.
```

Thay vào,

```math
\nabla^2\phi=-\frac{\rho}{\varepsilon_0}.
```

Đây là phương trình Poisson.

Trong vùng không có điện tích,

```math
\rho=0,
```

nên

```math
\nabla^2\phi=0.
```

Đây là phương trình Laplace.

> **Chuyển mạch:** Trong **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Vì sao điện thế thường dễ giải hơn điện trường?** tiếp nhận điểm tựa từ **Từ định luật Gauss đến phương trình Poisson** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điều kiện biên Dirichlet và Neumann** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao điện thế thường dễ giải hơn điện trường?

Điện trường là vectơ có ba thành phần, trong khi điện thế là vô hướng. Khi giải được `\phi`, ta lấy độ dốc (gradient / 기울기) để thu lại điện trường:

```math
\mathbf E=-\nabla\phi.
```

Đặc biệt với hình học phức tạp, điều kiện biên trên vật dẫn thường được phát biểu tự nhiên bằng điện thế không đổi.

Trong trạng thái điện tĩnh, toàn bộ vật dẫn lý tưởng là một mặt đẳng thế. Thành phần tiếp tuyến của điện trường trên bề mặt phải bằng không; nếu không, điện tích tự do sẽ tiếp tục chuyển động.

> **Chuyển mạch:** Ở chặng này của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Điều kiện biên Dirichlet và Neumann** tiếp nhận điểm tựa từ **Vì sao điện thế thường dễ giải hơn điện trường?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Định lý duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều kiện biên Dirichlet và Neumann

Hai kiểu điều kiện biên thường gặp là:

- **Dirichlet:** biết giá trị `\phi` trên biên;
- **Neumann:** biết đạo hàm pháp tuyến `\partial\phi/\partial n`, tương ứng với thông tin về thành phần pháp tuyến của điện trường.

Bài toán thực cũng có thể dùng điều kiện hỗn hợp.

Điểm quan trọng là phương trình trường **chưa đủ**; điều kiện biên là một phần của bài toán vật lý. Cùng phương trình Laplace nhưng biên khác nhau sẽ cho các nghiệm hoàn toàn khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Định lý duy nhất** tiếp nhận điểm tựa từ **Điều kiện biên Dirichlet và Neumann** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phương pháp ảnh điện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Định lý duy nhất

Trong các điều kiện thích hợp, nghiệm của bài toán Poisson/Laplace với dữ liệu biên xác định là duy nhất.

Ý nghĩa thực tế rất mạnh: nếu ta tìm được một hàm điện thế thỏa đồng thời

```text
phương trình trường + điều kiện biên,
```

thì ta không cần tiếp tục tìm “một nghiệm vật lý khác tốt hơn”.

Định lý duy nhất là nền tảng lô-gic (logic / 논리) của nhiều kỹ thuật như phương pháp ảnh điện.

> **Chuyển mạch:** Trong **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Phương pháp ảnh điện** tiếp nhận điểm tựa từ **Định lý duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lực tác dụng lên điện tích thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phương pháp ảnh điện

Xét một điện tích điểm `q` ở độ cao `a` phía trên một mặt phẳng dẫn vô hạn nối đất tại `z=0`.

Điều kiện biên là

```math
\phi=0
```

trên toàn mặt phẳng.

Thay vì trực tiếp tìm phân bố điện tích cảm ứng trên mặt dẫn, ta bỏ mặt dẫn khỏi mô hình và đặt một **điện tích ảnh (image charge)** `-q` đối xứng qua mặt phẳng.

Trong nửa không gian `z>0`, điện thế là

```math
\phi(\mathbf r)=
\frac{1}{4\pi\varepsilon_0}
\left(
\frac{q}{|\mathbf r-\mathbf r_q|}
-
\frac{q}{|\mathbf r-\mathbf r_{im}|}
\right).
```

Trên `z=0`, khoảng cách tới điện tích thật và điện tích ảnh bằng nhau nên hai đóng góp triệt tiêu, cho `\phi=0`.

Vì nghiệm thỏa phương trình và điều kiện biên, định lý duy nhất bảo đảm nó chính là nghiệm vật lý trong miền `z>0`.

Điện tích ảnh không phải điện tích thật nằm bên trong vật dẫn. Nó là công cụ toán học tái tạo đúng ảnh hưởng của biên.

> **Chuyển mạch:** Ở chặng này của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Lực tác dụng lên điện tích thật** tiếp nhận điểm tựa từ **Phương pháp ảnh điện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mật độ điện tích cảm ứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lực tác dụng lên điện tích thật

Sau khi dùng điện tích ảnh để tìm trường trong miền vật lý, lực lên điện tích thật có thể tính như lực Coulomb do điện tích ảnh gây ra tại vị trí của điện tích thật.

Khoảng cách giữa hai điện tích là `2a`, nên độ lớn lực là

```math
F=
\frac{1}{4\pi\varepsilon_0}
\frac{q^2}{(2a)^2}
=
\frac{q^2}{16\pi\varepsilon_0a^2}.
```

Hướng lực về phía mặt dẫn.

Điều này cho thấy một điện tích gần vật dẫn trung hòa nối đất vẫn bị hút vì điện tích bề mặt tái phân bố.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Mật độ điện tích cảm ứng** tiếp nhận điểm tựa từ **Lực tác dụng lên điện tích thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phương pháp tách biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mật độ điện tích cảm ứng

Khi đã biết điện thế, điện trường pháp tuyến ngay ngoài mặt dẫn là

```math
E_n=-\frac{\partial\phi}{\partial n}.
```

Mật độ điện tích bề mặt là

```math
\sigma=\varepsilon_0E_n.
```

Quy trình chung là:

```text
hình học biên
→ giải điện thế
→ lấy gradient
→ tìm điện trường
→ suy ra điện tích cảm ứng
```

Đây là một cách tư duy mạnh hơn việc cố đoán phân bố điện tích ngay từ đầu.

> **Chuyển mạch:** Trong **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Phương pháp tách biến** tiếp nhận điểm tựa từ **Mật độ điện tích cảm ứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nguyên lý cực đại của hàm điều hòa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phương pháp tách biến

Khi hình học có đối xứng phù hợp, ta có thể tìm nghiệm Laplace bằng tách biến (separation of variables).

Ví dụ trong hình chữ nhật hai chiều,

```math
\frac{\partial^2\phi}{\partial x^2}
+
\frac{\partial^2\phi}{\partial y^2}=0.
```

Giả sử

```math
\phi(x,y)=X(x)Y(y).
```

Thay vào và chia cho `XY`:

```math
\frac{X''}{X}
=-\frac{Y''}{Y}
=-k^2.
```

Bài toán PDE được tách thành hai ODE:

```math
X''+k^2X=0,
```

```math
Y''-k^2Y=0.
```

Điều kiện biên chọn các giá trị `k` cho phép và các hệ số của chuỗi nghiệm.

Cấu trúc này giống bài toán chế độ (mode / 모드) chuẩn: điều kiện biên biến một phổ liên tục các hàm thử thành một tập chế độ (mode / 모드) được phép.

> **Chuyển mạch:** Ở chặng này của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Nguyên lý cực đại của hàm điều hòa** tiếp nhận điểm tựa từ **Phương pháp tách biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khai triển đa cực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguyên lý cực đại của hàm điều hòa

Nghiệm của phương trình Laplace là hàm điều hòa (harmonic function). Một tính chất quan trọng là nếu `\phi` không hằng, nó không thể có cực đại hoặc cực tiểu cục bộ thực sự bên trong miền không điện tích; các giá trị cực trị nằm trên biên.

Hệ quả trực giác là điện thế trong vùng không điện tích bị “kéo” bởi các giá trị biên và không tự tạo đỉnh hoặc đáy cô lập bên trong.

Điều này cũng liên quan tới định lý Earnshaw: không thể tạo cân bằng tĩnh ổn định cho một điện tích điểm chỉ bằng trường điện tĩnh trong chân không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Khai triển đa cực** tiếp nhận điểm tựa từ **Nguyên lý cực đại của hàm điều hòa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao đa cực là một lý thuyết theo thang đo?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khai triển đa cực

Ở rất xa một phân bố điện tích hữu hạn, ta không cần biết toàn bộ chi tiết vi mô. Điện thế có thể khai triển theo khoảng cách:

```math
\phi(\mathbf r)
=\frac{1}{4\pi\varepsilon_0}
\left[
\frac{Q}{r}
+
\frac{\mathbf p\cdot\hat{\mathbf r}}{r^2}
+
\text{các hạng bậc cao}
\right].
```

Hạng đầu phụ thuộc tổng điện tích

```math
Q=\sum_i q_i.
```

Hạng tiếp theo phụ thuộc mômen lưỡng cực

```math
\mathbf p=\sum_i q_i\mathbf r_i.
```

Các hạng sau gồm tứ cực và đa cực bậc cao.

> **Chuyển mạch:** Trong **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Vì sao đa cực là một lý thuyết theo thang đo?** tiếp nhận điểm tựa từ **Khai triển đa cực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ: lưỡng cực điện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao đa cực là một lý thuyết theo thang đo?

Ở khoảng cách rất xa so với kích thước nguồn,

```math
r\gg a,
```

các hạng giảm theo các lũy thừa ngày càng cao của `1/r`.

Nếu `Q\neq0`, hạng đơn cực `1/r` chi phối. Nếu `Q=0` nhưng `\mathbf p\neq0`, hạng lưỡng cực `1/r^2` trở thành quan trọng nhất.

Vì vậy từ rất xa, chi tiết nhỏ của nguồn bị “nén” thành một vài moment tổng quát. Đây là một ví dụ rõ của tư duy lý thuyết hiệu dụng theo thang.

> **Chuyển mạch:** Ở chặng này của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Vì sao đa cực là một lý thuyết theo thang đo?** cho ta quy tắc; **Ví dụ: lưỡng cực điện** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Tính phụ thuộc gốc tọa độ của moment đa cực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ: lưỡng cực điện

Với hai điện tích `+q` và `-q` cách nhau vectơ `\mathbf d`, mômen lưỡng cực là

```math
\mathbf p=q\mathbf d.
```

Ở xa nguồn,

```math
\phi(\mathbf r)
\approx
\frac{1}{4\pi\varepsilon_0}
\frac{\mathbf p\cdot\hat{\mathbf r}}{r^2}.
```

Điện trường lưỡng cực giảm như

```math
E\sim\frac{1}{r^3},
```

nhanh hơn trường của điện tích điểm `1/r^2`.

Đây là lý do một hệ trung hòa điện có thể vẫn tạo trường ở xa nhưng yếu nhanh hơn nguồn mang điện tích tổng khác không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Ví dụ: lưỡng cực điện** cho ta quy tắc; **Tính phụ thuộc gốc tọa độ của moment đa cực** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Từ điện tĩnh tới phương pháp số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính phụ thuộc gốc tọa độ của moment đa cực

Mômen lưỡng cực phụ thuộc cách chọn gốc nếu tổng điện tích `Q` khác không. Nhưng khi `Q=0`, `\mathbf p` không đổi dưới phép dời gốc.

Chi tiết này quan trọng vì các moment đa cực không chỉ là “các số tính thêm”; ý nghĩa bất biến của chúng phụ thuộc vào cấu trúc nguồn.

> **Chuyển mạch:** Trong **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Từ điện tĩnh tới phương pháp số** tiếp nhận điểm tựa từ **Tính phụ thuộc gốc tọa độ của moment đa cực** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ điện tĩnh tới phương pháp số

Khi biên quá phức tạp để giải giải tích, cùng bài toán Poisson/Laplace được giải bằng sai phân hữu hạn, phần tử hữu hạn hoặc phương pháp phần tử biên.

Điều này tạo cầu nối trực tiếp giữa điện từ học và vật lý tính toán: phương trình vật lý, hình học biên và thuật toán số cùng quyết định nghiệm.

> **Chuyển mạch:** Ở chặng này của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Từ điện tĩnh tới phương pháp số** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Điện tĩnh thực tế thường không phải bài “cộng các lực Coulomb”. Cách nhìn mạnh hơn là:

```text
nguồn + hình học + điều kiện biên
→ phương trình Poisson/Laplace
→ điện thế
→ điện trường
→ lực và điện tích cảm ứng
```

Phương pháp ảnh, tách biến và khai triển đa cực là ba chiến lược khác nhau cho ba loại cấu trúc: biên đặc biệt, hình học tách được và miền xa nguồn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Điện tích ảnh tồn tại thật bên trong vật dẫn”

Không. Nó chỉ là nguồn toán học bên ngoài miền vật lý dùng để tái tạo đúng điều kiện biên.

### “Biết phương trình Laplace là đủ để biết điện thế”

Không. Cần điều kiện biên để chọn nghiệm cụ thể.

### “Ở xa nguồn vẫn cần biết chính xác mọi điện tích”

Thường không. Khai triển đa cực cho thấy vài moment thấp bậc có thể chứa gần như toàn bộ thông tin trường xa cần thiết.

> **Chuyển mạch:** Trong **Điện tĩnh học dạng bài toán biên: phương pháp ảnh điện và khai triển đa cực**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Điện tĩnh học](00_electrostatics.md), [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Thế điện từ và tự do chuẩn](06_potentials_gauge.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
