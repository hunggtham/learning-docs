# Cơ học Hamilton nâng cao: ngoặc Poisson, biến đổi chính tắc và Hamilton–Jacobi

## Vì sao cơ học Hamilton còn đi xa hơn hai phương trình Hamilton?

Khi mới học cơ học Hamilton (Hamiltonian mechanics / 해밀턴 역학), ta thường bắt đầu với

```math
\dot q_i=\frac{\partial H}{\partial p_i},\qquad
\dot p_i=-\frac{\partial H}{\partial q_i}.
```

Điểm sâu hơn là không gian pha (phase space) không chỉ là nơi chứa các cặp biến `(q,p)`. Nó có một cấu trúc hình học đặc biệt quyết định những phép đổi biến nào giữ nguyên dạng của động lực học.

Trong cơ học Newton, đổi từ tọa độ Descartes sang tọa độ cực có thể làm bài toán quỹ đạo đơn giản hơn. Trong cơ học Hamilton, ta còn có thể đổi đồng thời cả tọa độ và động lượng bằng **biến đổi chính tắc (canonical transformation / 정준변환)**.

Mục tiêu không phải chỉ đổi ký hiệu. Ta muốn tìm cách biểu diễn trong đó chuyển động trở nên đơn giản hơn hoặc làm các đại lượng bảo toàn lộ rõ hơn.

## Ngoặc Poisson: ngôn ngữ của biến thiên trong không gian pha

Với hai đại lượng `A(q,p,t)` và `B(q,p,t)`, ngoặc Poisson (Poisson bracket / 푸아송 괄호) được định nghĩa bởi

```math
\{A,B\}
=\sum_i\left(
\frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i}
-\frac{\partial A}{\partial p_i}\frac{\partial B}{\partial q_i}
\right).
```

Nếu `A` không phụ thuộc thời gian một cách tường minh,

```math
\frac{dA}{dt}=\{A,H\}.
```

Hamiltonian vì vậy đóng vai trò là **phần tử sinh của tiến hóa theo thời gian** trong không gian pha.

Một đại lượng được bảo toàn khi

```math
\{A,H\}+\frac{\partial A}{\partial t}=0.
```

Điều này cho phép kiểm tra định luật bảo toàn trực tiếp từ cấu trúc đại số mà không nhất thiết phải giải toàn bộ quỹ đạo.

## Cầu nối sang cơ học lượng tử

Trong cơ học lượng tử, ngoặc Poisson có một quan hệ tương ứng khái niệm với commutator:

```math
\{A,B\}
\quad\longleftrightarrow\quad
\frac{1}{i\hbar}[\hat A,\hat B].
```

Không nên coi đây là quy tắc thay thế máy móc cho mọi hệ, nhưng nó cho thấy cơ học lượng tử kế thừa nhiều cấu trúc từ cơ học Hamilton cổ điển.

## Biến đổi chính tắc: đổi biến mà không phá cấu trúc động lực học

Giả sử ta đổi từ `(q,p)` sang `(Q,P)`. Một phép biến đổi là chính tắc nếu các phương trình Hamilton mới vẫn có dạng

```math
\dot Q_i=\frac{\partial K}{\partial P_i},\qquad
\dot P_i=-\frac{\partial K}{\partial Q_i},
```

với Hamiltonian mới `K(Q,P,t)`.

Các biến chính tắc phải giữ các quan hệ ngoặc Poisson cơ bản

```math
\{Q_i,Q_j\}=0,
```

```math
\{P_i,P_j\}=0,
```

```math
\{Q_i,P_j\}=\delta_{ij}.
```

`\delta_{ij}` là delta Kronecker.

Có thể so sánh với phép quay Euclid: phép quay giữ độ dài và góc; biến đổi chính tắc giữ cấu trúc symplectic của không gian pha.

## Hàm sinh: thiết kế biến đổi thay vì đoán trực tiếp

Một biến đổi chính tắc có thể được xây từ hàm sinh (generating function / 생성함수). Với một lựa chọn thường gặp `F_2(q,P,t)`, ta có

```math
p_i=\frac{\partial F_2}{\partial q_i},
\qquad
Q_i=\frac{\partial F_2}{\partial P_i},
```

và

```math
K=H+\frac{\partial F_2}{\partial t}.
```

Thay vì phải đoán độc lập cả `Q(q,p)` và `P(q,p)`, ta tìm một hàm vô hướng có các đạo hàm sinh ra phép đổi biến phù hợp.

Trong thực tế, hàm sinh giúp xây biến gắn với đại lượng bảo toàn, mode chuẩn hoặc tọa độ action–angle.

## Phương trình Hamilton–Jacobi

Phương trình Hamilton–Jacobi (Hamilton–Jacobi equation / 해밀턴-야코비 방정식) tìm hàm tác dụng chính `S(q,t)` sao cho

```math
H\left(q,\frac{\partial S}{\partial q},t\right)
+\frac{\partial S}{\partial t}=0.
```

Từ đó

```math
p_i=\frac{\partial S}{\partial q_i}.
```

Nếu tìm được `S`, ta có thể tái dựng động lực học.

Ý nghĩa sâu của phương pháp là biến bài toán tích phân nhiều phương trình ODE liên kết thành bài toán tìm một hàm sinh thích hợp. Trong trường hợp thuận lợi, phép biến đổi do `S` sinh ra có thể đưa Hamiltonian mới về dạng rất đơn giản.

## Liên hệ với quang hình học và giới hạn bán cổ điển

Hamilton–Jacobi là một cầu nối quan trọng giữa cơ học cổ điển, quang hình học và cơ học lượng tử.

Trong xấp xỉ bán cổ điển, hàm sóng thường được viết dưới dạng

```math
\psi\sim A e^{iS/\hbar}.
```

Ở bậc dẫn đầu khi tác dụng đặc trưng lớn hơn nhiều so với `\hbar`, phương trình cho pha `S` trở về phương trình Hamilton–Jacobi.

Điều này cho thấy quỹ đạo cổ điển có thể xuất hiện từ cấu trúc pha của trạng thái lượng tử trong giới hạn thích hợp.

## Biến action–angle

Với hệ tích phân được (integrable) có chuyển động liên kết và tuần hoàn, ta có thể định nghĩa biến action

```math
J_i=\frac{1}{2\pi}\oint p_i\,dq_i.
```

Nếu Hamiltonian chỉ phụ thuộc `J`,

```math
H=H(J),
```

thì biến góc `\theta_i` tiến hóa tuyến tính:

```math
\dot\theta_i=\omega_i(J).
```

Một quỹ đạo phức tạp trong không gian cấu hình có thể trở thành chuyển động đều trên một torus trong không gian pha.

Đây là một mô hình tư duy mạnh: đôi khi phần lớn độ phức tạp nằm ở cách chọn tọa độ, không nằm ở bản thân động lực học.

## Liên hệ với lượng tử hóa bán cổ điển

Các biến action cũng xuất hiện trong lượng tử hóa bán cổ điển. Trước cơ học lượng tử hiện đại, điều kiện Bohr–Sommerfeld có dạng gần

```math
\oint p\,dq\approx nh.
```

Dù không phải lý thuyết lượng tử hoàn chỉnh, nó cho thấy action trong không gian pha có liên hệ tự nhiên với thang lượng tử `h`.

## Định lý Liouville

Dòng Hamilton bảo toàn thể tích trong không gian pha. Nếu một tập các điều kiện ban đầu chiếm một thể tích nhỏ, dòng động lực học có thể kéo dãn và uốn tập đó nhưng không làm thể tích tổng tự co lại.

Đây là định lý Liouville (Liouville's theorem / 리우빌 정리), một nền tảng của cơ học thống kê.

Hệ quả quan trọng là ma sát thực không thể được mô tả như một hệ Hamilton kín đơn giản chỉ bằng các bậc tự do đang quan sát. Ma sát làm thể tích hiệu dụng trong không gian pha co lại. Muốn có mô tả Hamilton đầy đủ, phải mở rộng hệ để bao gồm môi trường nhận năng lượng.

## Ví dụ: dao động tử điều hòa trong biến action–angle

Xét

```math
H=\frac{p^2}{2m}+\frac12m\omega^2q^2.
```

Quỹ đạo trong không gian pha là một ellipse. Action bằng diện tích ellipse chia `2\pi`:

```math
J=\frac{E}{\omega}.
```

Do đó

```math
H=\omega J,
```

và

```math
\dot\theta=\frac{\partial H}{\partial J}=\omega.
```

Trong biến `(J,\theta)`, dao động tử không còn được mô tả như một vật đi qua đi lại mà như một góc quay đều với action không đổi.

## Khi nào formalism này đáng dùng?

Nếu bài toán chỉ là rơi tự do, ngôn ngữ Newton thường ngắn và trực tiếp hơn. Hamilton–Jacobi không làm kết quả “đúng hơn”.

Formalism nâng cao trở nên hữu ích khi bài toán có đối xứng, nhiều bậc tự do, nhiễu loạn nhỏ, chuyển động tuần hoàn, ensemble thống kê hoặc cần cầu nối sang cơ học lượng tử.

Với hệ không tích phân được, tọa độ action–angle toàn cục có thể không tồn tại. Khi nhiễu loạn phá tính tích phân được, một số torus bất biến có thể sống sót còn một số bị phá. Đây là cửa ngõ sang lý thuyết KAM và hỗn loạn.

## Giới hạn và giả định

Cơ học Hamilton cổ điển giả sử ta có thể mô tả hệ bằng các biến chính tắc và một Hamiltonian xác định. Với ràng buộc phi chuẩn, hệ tiêu tán mạnh hoặc trường chuẩn (gauge field), cấu trúc có thể tinh tế hơn.

Hamiltonian cũng không phải lúc nào đồng nhất đơn giản với “tổng động năng cộng thế năng”. Định nghĩa chính xác của nó đến từ biến đổi Legendre của Lagrangian và vai trò phần tử sinh của tiến hóa thời gian.

## Mô hình tư duy (Mental Model)

Cơ học Hamilton xem chuyển động như một dòng có cấu trúc hình học trong không gian pha. Biến đổi chính tắc là cách thay “hệ tọa độ của động lực học” mà vẫn giữ cấu trúc đó. Hamilton–Jacobi tìm cách chọn biến sao cho dòng càng đơn giản càng tốt.

Chuỗi tư duy hữu ích là

```text
Lagrangian
→ biến đổi Legendre
→ Hamiltonian
→ ngoặc Poisson
→ biến đổi chính tắc
→ Hamilton–Jacobi / action–angle
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Hamiltonian luôn bằng tổng năng lượng vật lý”

Không phải trong mọi cách mô tả. Với nhiều hệ chuẩn và không phụ thuộc thời gian, hai đại lượng trùng nhau; nhưng với ràng buộc phụ thuộc thời gian, ghép điện từ hoặc tọa độ đặc biệt, cần kiểm tra định nghĩa cụ thể.

### “Biến đổi chính tắc chỉ là đổi tọa độ thông thường”

Không. Nó đồng thời tổ chức lại tọa độ và động lượng sao cho cấu trúc symplectic được giữ nguyên.

### “Hamilton–Jacobi làm mọi hệ dễ giải”

Không. Tìm nghiệm đầy đủ của phương trình Hamilton–Jacobi có thể khó ngang bài toán ban đầu. Giá trị chính của formalism là bộc lộ cấu trúc, đối xứng và tạo nền cho các phương pháp xấp xỉ.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Cơ học giải tích](08_analytical_mechanics.md), [Đối xứng và bảo toàn](../00_foundations/04_symmetry_conservation_scale.md).

**Liên hệ tiếp:** [Động lực học phi tuyến và hỗn loạn](09_nonlinear_dynamics_chaos.md), [Ensemble thống kê](../04_thermal_statistical/03_ensembles_partition_functions.md), [Đối xứng và tích phân đường lượng tử](../08_quantum/07_symmetry_operator_path_integral.md).
