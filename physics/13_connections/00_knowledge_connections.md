# Các liên kết kiến thức: những cấu trúc lặp lại xuyên suốt Vật lý

Vật lý có rất nhiều lĩnh vực, nhưng các lĩnh vực đó không phải những hòn đảo tách rời. Cùng một số cấu trúc toán học và mô hình tư duy xuất hiện lặp lại trong cơ học, nhiệt, điện từ, lượng tử, vật chất ngưng tụ và vật lý thiên văn. Nhận ra các cấu trúc này giúp học kiến thức mới bằng cách nối nó với điều đã hiểu thay vì ghi nhớ thêm một tập công thức độc lập.

## 1. Trạng thái → tiến hóa → quan sát

Một lý thuyết vật lý thường cần ba lớp. **Trạng thái (state)** cho biết hệ đang ở đâu trong không gian các khả năng. **Quy luật tiến hóa (evolution law)** cho biết trạng thái thay đổi theo thời gian như thế nào. **Quy tắc quan sát (observation rule)** cho biết từ trạng thái đó ta dự đoán được đại lượng đo nào.

Trong cơ học cổ điển của một chất điểm,

```math
\text{state}=(\vec r,\vec p).
```

Các phương trình Newton hoặc Hamilton quyết định tiến hóa. Trong cơ học lượng tử,

```math
\text{state}=|\psi\rangle\quad\text{hoặc}\quad\rho,
```

và phương trình Schrödinger mô tả tiến hóa của hệ kín, còn các toán tử cùng quy tắc Born nối trạng thái với xác suất phép đo. Trong cơ học chất lưu, trạng thái lại là các trường như `\rho(\vec r,t)`, `\vec v(\vec r,t)` và `P(\vec r,t)`.

Cấu trúc này có nét tương đồng với một hệ phần mềm có trạng thái: cần cách biểu diễn trạng thái, quy tắc chuyển trạng thái và đầu ra quan sát được. Điểm khác là trong vật lý, các quy tắc phải phù hợp với thí nghiệm và các đối xứng của tự nhiên.

## 2. Đạo hàm: ngôn ngữ của tốc độ biến thiên

Đạo hàm xuất hiện bất cứ khi nào ta hỏi một đại lượng thay đổi nhanh đến mức nào:

```math
v=\frac{dx}{dt},\qquad
a=\frac{dv}{dt},
```

```math
I=\frac{dQ}{dt},\qquad
F=\frac{dp}{dt},\qquad
P=\frac{dE}{dt}.
```

Vận tốc, gia tốc, dòng điện, lực và công suất có nội dung vật lý khác nhau, nhưng cùng dùng một ý tưởng toán học: tốc độ thay đổi của một đại lượng theo một biến khác.

## 3. Tích phân: cộng dồn những biến thiên nhỏ

Nếu đạo hàm cho biết tốc độ thay đổi cục bộ, tích phân cộng dồn các thay đổi đó:

```math
\Delta x=\int v\,dt,
```

```math
\Delta p=\int F\,dt,
```

```math
W=\int\vec F\cdot d\vec r,
```

```math
Q=\int I\,dt,
```

```math
\Phi_B=\int\vec B\cdot d\vec A.
```

Tích phân đường, mặt và thể tích khác nhau ở miền cộng dồn. Trong dữ liệu rời rạc, phép tổng `SUM` có thể được xem là họ hàng của tích phân khi ta cộng nhiều phần tử nhỏ.

## 4. Bảo toàn: thay đổi bên trong gắn với dòng qua biên

Nhiều định luật bảo toàn có dạng cục bộ

```math
\frac{\partial\rho}{\partial t}+\nabla\cdot\vec J=s,
```

trong đó `\rho` là mật độ của đại lượng đang xét, `\vec J` là thông lượng (flux) và `s` là nguồn hoặc hố.

Bảo toàn khối lượng trong chất lưu có dạng

```math
\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)=0,
```

còn bảo toàn điện tích là

```math
\frac{\partial\rho_q}{\partial t}+\nabla\cdot\vec J=0.
```

Mô hình tư duy chung là: lượng chứa trong một vùng thay đổi vì nó đi qua biên hoặc vì có nguồn bên trong. Vì vậy lựa chọn **ranh giới của hệ (system boundary)** là một kỹ năng nền tảng. Một vật riêng lẻ có thể không bảo toàn động lượng do ngoại lực, nhưng một hệ lớn hơn chứa cả các vật tương tác có thể bảo toàn tổng động lượng.

## 5. Đối xứng và định luật bảo toàn

Định lý Noether cho một liên hệ sâu giữa đối xứng liên tục và đại lượng bảo toàn. Đối xứng theo tịnh tiến thời gian liên hệ với bảo toàn năng lượng; đối xứng tịnh tiến không gian liên hệ với bảo toàn động lượng; đối xứng quay liên hệ với bảo toàn mômen động lượng.

Nhờ đó, các định luật bảo toàn không còn giống ba công thức tình cờ. Chúng phản ánh cấu trúc đối xứng của không-thời gian và của lý thuyết. Trong vật lý hạt, đối xứng chuẩn (gauge symmetry) còn tổ chức cách các trường và tương tác được mô tả.

## 6. Trường: mô tả vật lý tại từng điểm

Trường (field) gán một đại lượng cho mỗi điểm trong không gian và thời gian. Ví dụ:

```math
\vec g(\vec r),\qquad
\vec E(\vec r,t),\qquad
\vec B(\vec r,t),
```

```math
T(\vec r,t),\qquad
\vec v(\vec r,t).
```

Thay vì chỉ hỏi “vật A tác dụng lên vật B thế nào?”, cách nhìn theo trường hỏi “tại điểm này, môi trường vật lý có giá trị gì?”. Lý thuyết trường lượng tử (quantum field theory) đẩy ý tưởng này xa hơn: các hạt cơ bản được mô tả như những kích thích lượng tử của trường.

## 7. Gradient: dòng và lực thường phản ứng với độ chênh không gian

Nhiều quan hệ vật lý có cùng cấu trúc:

```math
\vec F=-\nabla U,
```

```math
\vec E=-\nabla V,
```

```math
\vec q=-k\nabla T,
```

```math
\vec J=-D\nabla n.
```

Gradient (gradient) chỉ hướng tăng nhanh nhất của một trường vô hướng. Dấu âm trong các ví dụ trên cho biết lực hoặc dòng hướng về phía giá trị thấp hơn của thế, nhiệt độ hay nồng độ.

Trong học máy, hạ gradient (gradient descent) cũng dùng cùng hình học để di chuyển trong không gian tham số theo hướng làm giảm hàm mất mát. Đây là sự tương đồng toán học, không có nghĩa gradient trong tối ưu hóa là một lực vật lý.

## 8. Thế năng, độ cong và cân bằng ổn định

Một cân bằng ổn định thường nằm gần cực tiểu của thế năng:

```math
\nabla U=0.
```

Gần cực tiểu trơn, khai triển Taylor cho

```math
U\approx U_0+\frac12kx^2.
```

Vì vậy dao động điều hòa xuất hiện ở rất nhiều hệ khác nhau. Không phải tự nhiên “ưa thích lò xo”, mà vì hàm trơn gần một cực tiểu thường có hạng bậc hai chi phối.

Trong tối ưu hóa, ma trận Hessian cũng mô tả độ cong gần cực tiểu. Đây là một ví dụ rõ về cùng cấu trúc toán học xuất hiện ở hai lĩnh vực khác nhau.

## 9. Tuyến tính hóa và nguyên lý chồng chập

Nhiều phương trình của tự nhiên là phi tuyến, nhưng gần một trạng thái cân bằng hoặc khi nhiễu loạn nhỏ,

```math
f(x_0+\delta x)\approx f(x_0)+f'(x_0)\delta x.
```

Xấp xỉ tuyến tính cho phép dùng nguyên lý chồng chập, đại số tuyến tính, trị riêng và biến đổi Fourier. Đây là lý do các dao động nhỏ, sóng, mạch điện tuyến tính và nhiều bài toán lượng tử chia sẻ nhiều công cụ toán học.

Khi nhiễu loạn không còn nhỏ, các hạng phi tuyến có thể tạo điều hòa bậc cao, ghép mode, sốc, dòng rối hoặc hỗn loạn.

## 10. Trị riêng và mode tự nhiên

Bài toán trị riêng có dạng

```math
A\vec v=\lambda\vec v.
```

Vectơ riêng (eigenvector) giữ hướng dưới tác động của phép biến đổi tuyến tính, còn trị riêng (eigenvalue) cho hệ số tỉ lệ. Trong dao động, mode chuẩn (normal mode) có tần số riêng. Trong cơ học lượng tử,

```math
\hat H|E_n\rangle=E_n|E_n\rangle,
```

các trạng thái riêng của Hamiltonian có năng lượng xác định.

Câu hỏi chung là: “những dạng tự nhiên nào của hệ có thể tiến hóa hoặc đáp ứng tương đối độc lập?”.

## 11. Sóng, Fourier và thông tin

Một tín hiệu `x(t)` trong miền thời gian có thể được biểu diễn bằng phổ `X(f)` trong miền tần số. Biến đổi Fourier (Fourier transform) đổi cơ sở từ mô tả cục bộ theo thời gian hoặc không gian sang các thành phần hình sin.

Nhiễu xạ trong quang học, phân tích phổ âm thanh, thông tin vô tuyến và quan hệ vị trí–động lượng trong lượng tử đều dùng cấu trúc Fourier. Một xung càng tập trung theo thời gian thì phổ tần số thường càng rộng. Trong lượng tử,

```math
\Delta x\Delta p\gtrsim\hbar,
```

còn trong xử lý tín hiệu tồn tại quan hệ đánh đổi tương tự giữa độ tập trung theo thời gian và tần số. Hai quan hệ không có cùng diễn giải vật lý, nhưng chia sẻ nền toán học Fourier.

## 12. Hàm mũ: tốc độ thay đổi tỉ lệ với lượng hiện có

Phương trình

```math
\frac{dx}{dt}=-kx
```

có nghiệm

```math
x(t)=x_0e^{-kt}.
```

Cấu trúc này xuất hiện trong phân rã phóng xạ, phóng điện RC, bao tắt dần, hấp thụ trong một số chế độ và xấp xỉ làm nguội Newton. Khi dấu đổi thành dương, ta có tăng trưởng hàm mũ.

Điểm quan trọng không phải ghi nhớ từng công thức riêng mà nhận ra cơ chế: tốc độ biến thiên hiện tại tỉ lệ với lượng đang còn lại.

## 13. Quy luật nghịch đảo bình phương và hình học ba chiều

Một nguồn điểm đẳng hướng phát thông lượng bảo toàn qua mặt cầu diện tích `4\pi r^2` tạo mật độ thông lượng tỉ lệ

```math
\frac{1}{r^2}.
```

Cấu trúc này xuất hiện trong trường hấp dẫn Newton, điện trường Coulomb và cường độ bức xạ của nguồn điểm đẳng hướng trong không gian tự do. Không phải mọi lực đều giảm theo `1/r^2`; quy luật này gắn với nguồn điểm, không gian ba chiều và bảo toàn thông lượng.

## 14. Các số vô thứ nguyên quyết định chế độ vật lý

Số Reynolds

```math
Re=\frac{\rho vL}{\mu},
```

số Mach

```math
Ma=\frac{v}{c_s},
```

và tỉ số tương đối tính

```math
\beta=\frac{v}{c}
```

đều không có đơn vị. Chúng cho biết tỉ lệ giữa các cơ chế cạnh tranh. Hai hệ có cùng hình dạng nhưng các số vô thứ nguyên khác nhau có thể có hành vi rất khác.

Đây là cơ sở của tương tự động lực học (dynamic similarity) trong mô hình thí nghiệm và kỹ thuật.

## 15. Xấp xỉ là một phần của lý thuyết

Một quy trình mô hình hóa thường có dạng

```text
hệ thực
→ chọn hệ con
→ xác định cơ chế chi phối
→ tìm tham số nhỏ
→ bỏ các hạng bậc cao
→ giải mô hình gần đúng
→ kiểm tra sai số và miền áp dụng
```

Ví dụ,

```math
\sin\theta\approx\theta
```

chỉ đúng khi `|\theta|\ll1` rad. Tương tự,

```math
\gamma\approx1+\frac12\frac{v^2}{c^2}
```

chỉ hữu ích khi `v\ll c`.

Trưởng thành trong vật lý không có nghĩa tránh xấp xỉ, mà là biết mình đã bỏ qua điều gì và khi nào phần bị bỏ qua trở nên quan trọng.

## 16. Thang đo và lý thuyết hiệu dụng

Không ai mô phỏng điện thoại thông minh trực tiếp từ quark và gluon. Không phải vì Mô hình Chuẩn sai, mà vì mô tả đó quá vi mô cho bài toán cần giải.

```text
quark và gluon
↓
nucleon
↓
hạt nhân và electron
↓
nguyên tử và phân tử
↓
vật liệu
↓
thiết bị
↓
mạch điện
↓
máy tính và phần mềm
```

Mỗi tầng dùng các bậc tự do hiệu dụng (effective degrees of freedom) và nén chi tiết tầng dưới thành các tham số như khối lượng, điện tích, hằng số điện môi, điện trở hay điện áp ngưỡng. Cách tư duy này gần với trừu tượng hóa trong kỹ nghệ phần mềm: một API che chi tiết thấp hơn nhưng vẫn bị giới hạn bởi chúng.

## 17. Xác suất cổ điển và xác suất lượng tử

Trong cơ học thống kê cổ điển, xác suất thường biểu diễn sự thiếu thông tin về trạng thái vi mô hoặc mô tả một tập hợp thống kê. Trong cơ học lượng tử, xác suất xuất hiện trong quy tắc Born ngay cả khi trạng thái thuần đã được xác định đầy đủ.

Hai trường hợp dùng nhiều công cụ xác suất giống nhau nhưng không có cùng cách diễn giải vật lý. Vì vậy không nên giản lược lượng tử thành “cổ điển cộng thêm ngẫu nhiên”.

## 18. Entropy và thông tin

Entropy Boltzmann

```math
S=k_B\ln\Omega
```

và entropy Shannon

```math
H=-\sum_i p_i\log p_i
```

đều dùng logarit để biến số lượng trạng thái hoặc xác suất nhân với nhau thành đại lượng có tính cộng. Liên hệ giữa nhiệt động lực học và lý thuyết thông tin rất sâu, nhưng hai khái niệm không nên bị đồng nhất khi chưa chỉ rõ hệ vật lý và cách ánh xạ trạng thái.

## 19. Nhân quả và tốc độ truyền tín hiệu

Trong các mô hình cơ học cổ điển lý tưởng, đôi khi ràng buộc được viết như thể tác động xảy ra tức thời. Điện từ học và thuyết tương đối buộc ta xét tốc độ truyền hữu hạn của ảnh hưởng vật lý, với giới hạn nhân quả liên quan đến `c`.

Trong hệ phân tán của khoa học máy tính, độ trễ mạng cũng làm khái niệm “trạng thái toàn cục tức thời” trở nên khó. Đây không phải cùng hiện tượng với tương đối tính, nhưng là một phép liên hệ hữu ích: thông tin luôn cần một cơ chế truyền.

## 20. Nhiễu, thăng giáng và phép đo

Mọi cảm biến thực đều có nhiễu. Chuyển động nhiệt tạo nhiễu Johnson–Nyquist; thống kê photon tạo nhiễu bắn (shot noise); các hệ lượng tử có thêm những giới hạn gắn với trạng thái và phép đo.

Một phép đo tốt không chỉ trả về một giá trị. Nó phải đi kèm mô hình đáp ứng của thiết bị, hiệu chuẩn, độ bất định và các nguồn sai lệch có thể có.

## 21. Nguyên lý biến phân và tối ưu hóa có ràng buộc

Trong cơ học Lagrange, tác dụng

```math
S=\int L\,dt,
```

với

```math
L=T-U,
```

thỏa điều kiện tác dụng dừng

```math
\delta S=0.
```

Từ đó suy ra phương trình Euler–Lagrange

```math
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}
-\frac{\partial L}{\partial q_i}=0.
```

Cấu trúc này liên hệ trực tiếp với phép tính biến phân (calculus of variations). Tuy nhiên không nên nhân cách hóa rằng tự nhiên “chạy một thuật toán tối ưu”; nguyên lý biến phân là một cách mã hóa toán học cô đọng cho động lực học.

## 22. Tọa độ suy rộng giúp hấp thụ ràng buộc hình học

Con lắc đơn có thể được mô tả bằng `x,y` kèm ràng buộc hình tròn, nhưng dùng một góc `\theta` sẽ tự nhiên hơn. Khi đó

```math
T=\frac12m\ell^2\dot\theta^2,
```

```math
U=mg\ell(1-\cos\theta),
```

và phương trình Euler–Lagrange cho

```math
\ddot\theta+\frac{g}{\ell}\sin\theta=0.
```

Với góc nhỏ, `\sin\theta\approx\theta`, ta thu được dao động điều hòa. Một ví dụ duy nhất nối cơ học giải tích, ràng buộc, xấp xỉ, phi tuyến và dao động.

## 23. Hamiltonian nối cơ học cổ điển với lượng tử

Trong cơ học Hamilton,

```math
\dot q_i=\frac{\partial H}{\partial p_i},
```

```math
\dot p_i=-\frac{\partial H}{\partial q_i}.
```

Hamiltonian thường liên hệ với năng lượng toàn phần trong các hệ chuẩn. Trong cơ học lượng tử, Hamiltonian trở thành toán tử sinh tiến hóa theo thời gian. Đây là một cầu nối toán học quan trọng từ cơ học cổ điển sang lượng tử.

## 24. Cùng phương trình không có nghĩa cùng hiện tượng

Phương trình

```math
\ddot x+\omega^2x=0
```

có thể mô tả khối lượng–lò xo, con lắc góc nhỏ, điện tích trong mạch LC hoặc dao động phân tử gần cân bằng. Cấu trúc nghiệm giống nhau vì toán học giống nhau, nhưng ý nghĩa của biến và cơ chế vật lý khác nhau.

Kỹ năng quan trọng là nhận ra sự đẳng cấu toán học (mathematical isomorphism) mà không đánh đồng bản chất vật lý.

## 25. Khung giải quyết một hiện tượng mới

Khi gặp một hiện tượng chưa quen, hãy lần lượt hỏi: hệ và ranh giới của nó là gì; biến trạng thái nào thực sự cần; thang đo nào đang chi phối; có đối xứng nào giúp giảm số biến; định luật bảo toàn nào áp dụng; tương tác nên mô tả bằng lực, trường hay thế; có tham số nhỏ nào cho phép xấp xỉ; phương trình chi phối là gì; điều kiện đầu và điều kiện biên ra sao; kết quả có đúng thứ nguyên, đúng giới hạn và đúng bậc độ lớn không; cuối cùng, đại lượng nào có thể đo để kiểm tra mô hình.

Đây không phải một danh sách công thức. Nó là cách tổ chức tư duy để chuyển từ hiện tượng sang mô hình và từ mô hình trở lại quan sát.

## Mô hình tư duy (Mental Model)

> Vật lý tìm những cấu trúc ổn định trong một thế giới luôn thay đổi: trạng thái, đối xứng, định luật bảo toàn, trường, mode, xác suất và thang đo. Khi chọn đúng cách biểu diễn, một hiện tượng tưởng rất phức tạp thường lộ ra cấu trúc quen thuộc.

> Hiểu sâu không có nghĩa luôn dùng lý thuyết phức tạp nhất. Hiểu sâu là biết vì sao mô hình hiện tại đủ dùng, giả định nào làm nó hợp lệ và dấu hiệu nào cho biết cần chuyển sang mô hình khác.

## Liên kết kiến thức (Knowledge Connection)

**Liên hệ tiếp:** [Thuật ngữ và điều hướng](01_glossary_navigation.md), [Cẩm nang giải bài](03_problem_solving_playbook.md).
