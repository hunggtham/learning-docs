# Hiện tượng tới hạn, tính phổ quát và nhóm tái chuẩn hóa

## Vì sao chuyển pha không chỉ là “đổi trạng thái”?

Nước sôi là ví dụ chuyển pha quen thuộc, nhưng nhiều hệ như nam châm sắt từ gần nhiệt độ Curie hoặc chất lưu gần điểm tới hạn cho thấy một hiện tượng sâu hơn: các dao động xuất hiện đồng thời trên rất nhiều thang chiều dài.

Hiện tượng tới hạn (critical phenomena / 임계현상) là vùng mà chi tiết vi mô có thể trở nên kém quan trọng hơn đối xứng, số chiều và tương quan tập thể.

## Tham số trật tự

Tham số trật tự (order parameter / 질서변수) là đại lượng dùng để phân biệt các pha.

Với hệ sắt từ, từ hóa `M` là một lựa chọn tự nhiên. Khi không có từ trường ngoài:

- trên nhiệt độ tới hạn, giá trị trung bình `M=0`;
- dưới nhiệt độ tới hạn, hệ có thể chọn `M>0` hoặc `M<0`.

Các phương trình có đối xứng `M\to -M`, nhưng trạng thái cân bằng cụ thể chọn một nhánh. Đây là **phá vỡ đối xứng tự phát (spontaneous symmetry breaking / 자발적 대칭 깨짐)**.

Trong chuyển pha lỏng–khí, chênh lệch mật độ có thể đóng vai tham số trật tự. Trong siêu dẫn, tham số trật tự là một trường phức liên hệ với condensate kết hợp.

## Mô hình Landau cho năng lượng tự do

Gần chuyển pha, ta có thể khai triển năng lượng tự do theo tham số trật tự:

```math
F(M)=F_0+a(T-T_c)M^2+bM^4-hM+\cdots,
```

với `b>0` để năng lượng bị chặn dưới.

Khi `T>T_c`, hệ số bậc hai dương và minimum ở `M=0`. Khi `T<T_c`, hệ số bậc hai âm và năng lượng tự do phát triển hai minimum đối xứng ở `\pm M_0`.

Với `h=0`, điều kiện cân bằng là

```math
\frac{\partial F}{\partial M}=0,
```

nên

```math
2a(T-T_c)M+4bM^3=0.
```

Ngoài nghiệm `M=0`, dưới `T_c` ta có

```math
M^2\propto(T_c-T).
```

Do đó lý thuyết trường trung bình dự đoán

```math
M\propto(T_c-T)^{1/2}.
```

Số mũ `1/2` là một số mũ tới hạn của mô hình trường trung bình. Trong nhiều hệ thực, đặc biệt ở số chiều thấp, dao động không gian làm số mũ thực nghiệm khác giá trị này.

## Độ dài tương quan

Hàm tương quan mô tả mức độ trạng thái ở hai điểm cách nhau `r` còn liên hệ với nhau đến đâu.

Xa điểm tới hạn, tương quan thường giảm trên một thang chiều dài đặc trưng `\xi`. Gần điểm tới hạn,

```math
\xi\sim|T-T_c|^{-\nu}.
```

Khi `T\to T_c`, `\xi` tăng rất lớn. Hệ không còn một thang vi mô duy nhất chi phối; các vùng từ rất nhỏ đến rất lớn trở nên tương quan.

Hiện tượng opalescence tới hạn là ví dụ quang học: dao động mật độ trên nhiều thang làm ánh sáng nhìn thấy bị tán xạ mạnh.

## Tính phổ quát

Điều đáng ngạc nhiên là nhiều hệ có cấu trúc vi mô hoàn toàn khác nhau lại có cùng số mũ tới hạn.

Ví dụ, điểm tới hạn lỏng–khí và một số hệ từ có thể thuộc cùng một lớp phổ quát (universality class).

Lý do là khi quan sát ở thang đủ lớn, nhiều chi tiết vi mô trở thành không quan trọng. Các yếu tố còn chi phối thường là:

- số chiều không gian;
- đối xứng của tham số trật tự;
- số thành phần của tham số trật tự;
- phạm vi tương tác.

Đây là một bài học quan trọng của vật lý hiện đại: **cùng một lý thuyết hiệu dụng có thể nổi lên từ những hệ vi mô rất khác nhau**.

## Nhóm tái chuẩn hóa: vật lý khi thay đổi thang đo

Nhóm tái chuẩn hóa (renormalization group, RG / 재규격화군) nghiên cứu cách các tham số của mô hình thay đổi khi ta coarse-grain hệ và đổi thang chiều dài.

Một quy trình tư duy điển hình là:

1. gom các bậc tự do vi mô thành block lớn hơn;
2. trung bình hoặc tích phân các dao động ở thang nhỏ;
3. co giãn tọa độ để so sánh mô hình mới với mô hình cũ;
4. theo dõi các coupling “chảy” trong không gian tham số.

Một điểm bất động (fixed point) là nơi mô hình giữ cùng dạng sau phép đổi thang. Điểm tới hạn thường gắn với fixed point bất biến theo thang.

Các coupling có thể được phân thành:

- **relevant**: tăng ảnh hưởng khi đi lên thang lớn;
- **irrelevant**: giảm dần ảnh hưởng, làm hệ quên chi tiết vi mô;
- **marginal**: cần phân tích bậc cao hơn để biết xu hướng.

Tính phổ quát xuất hiện vì nhiều mô hình vi mô khác nhau có thể chảy về cùng một fixed point.

## Bất biến theo thang và quy luật lũy thừa

Khi không còn một thang chiều dài đặc trưng, quy luật mũ suy giảm thường được thay bằng quy luật lũy thừa:

```math
C(r)\sim r^{-\alpha}.
```

Quy luật lũy thừa cũng xuất hiện trong dòng rối, percolation và nhiều hệ phức tạp khác. Tuy nhiên, nhìn thấy một power law không tự động chứng minh hệ đang ở critical point; cần kiểm tra cơ chế, miền thang đo và hiệu ứng kích thước hữu hạn.

## Chuyển pha bậc nhất và chuyển pha liên tục

Không phải mọi chuyển pha đều có hiện tượng tới hạn.

Chuyển pha bậc nhất thường có ẩn nhiệt và đồng tồn tại pha. Tham số trật tự nhảy gián đoạn.

Chuyển pha liên tục có tham số trật tự thay đổi liên tục nhưng susceptibility hoặc độ dài tương quan có thể phân kỳ.

RG đặc biệt quan trọng đối với các chuyển pha liên tục, nơi dao động đa thang quyết định hành vi gần critical point.

## Mô hình Ising

Mô hình Ising đặt spin `s_i=\pm1` trên mạng với Hamiltonian

```math
H=-J\sum_{\langle ij\rangle}s_is_j-h\sum_i s_i.
```

Dù cực kỳ đơn giản, mô hình nắm bắt cạnh tranh giữa tương tác muốn các spin lân cận cùng hướng và entropy muốn nhiều cấu hình có thể xảy ra.

Trong 2D, mô hình Ising có nghiệm tới hạn chính xác và cho số mũ khác lý thuyết trường trung bình. Nó là “phòng thí nghiệm lý thuyết” cho phá vỡ đối xứng, phổ quát, Monte Carlo và RG.

## Các số mũ tới hạn và quan hệ scaling

Gần chuyển pha liên tục, nhiều đại lượng tuân theo luật lũy thừa. Ví dụ với

```math
t=\frac{T-T_c}{T_c},
```

độ dài tương quan có thể viết

```math
\xi\sim|t|^{-\nu}.
```

Từ hóa, susceptibility và nhiệt dung cũng có các số mũ riêng.

Các số mũ không hoàn toàn độc lập. Các giả thuyết scaling tạo quan hệ giữa chúng, nhờ đó đo một số đại lượng có thể dùng để kiểm tra tính nhất quán của lớp phổ quát.

## Khi nào trường trung bình thất bại?

Lý thuyết Landau giả sử dao động quanh tham số trật tự trung bình không quá mạnh.

Gần critical point, `\xi` tăng lớn và dao động xuất hiện trên nhiều thang. Ở số chiều thấp, chúng có thể làm xấp xỉ trường trung bình không còn đúng.

Tiêu chuẩn Ginzburg (Ginzburg criterion / 긴즈부르크 기준) ước lượng miền nhiệt độ nơi dao động trở nên đủ mạnh để field theory trung bình mất độ tin cậy.

## Finite-size scaling trong mô phỏng

Mô phỏng máy tính luôn dùng hệ hữu hạn. Nếu độ dài tương quan `\xi` tiến gần kích thước hộp `L`, singularity của hệ vô hạn bị làm tròn.

Finite-size scaling khai thác phụ thuộc theo `L` để ngoại suy giới hạn nhiệt động và ước lượng nhiệt độ tới hạn cùng các số mũ tới hạn.

Đây là cầu nối trực tiếp giữa RG trừu tượng và phân tích dữ liệu Monte Carlo thực tế.

## Liên hệ với khoa học máy tính

Mô phỏng Metropolis và các phương pháp Monte Carlo cho phép khảo sát hệ tới hạn lớn.

Gần critical point, **critical slowing down** làm các thuật toán cập nhật cục bộ mất tương quan rất chậm, nên cần các thuật toán cluster như Wolff hoặc Swendsen–Wang.

Trong machine learning, coarse-graining và latent representation đôi khi được so sánh với RG. So sánh này hữu ích ở mức trực giác “loại bỏ bậc tự do không quan trọng theo thang”, nhưng RG là một khung toán–lý cụ thể chứ không đồng nghĩa với giảm chiều dữ liệu.

## Miền áp dụng và giới hạn

Khai triển Landau hoạt động tốt khi tham số trật tự thay đổi chậm và dao động không quá mạnh. Nó không tự động dự đoán đúng số mũ tới hạn thực tế.

RG cung cấp mô tả sâu hơn nhưng việc tính flow chính xác có thể khó. Trong nhiều hệ cần dùng khai triển nhiễu loạn, mô phỏng lattice hoặc phương pháp số chuyên dụng.

## Mô hình tư duy (Mental Model)

Điểm tới hạn là nơi hệ mất một thang đặc trưng. Dao động ở nhiều kích thước cùng quan trọng. RG hỏi điều gì còn tồn tại khi ta liên tục “zoom out”.

Chi tiết biến mất khi coarse-grain là irrelevant; cấu trúc sống sót quyết định lớp phổ quát.

Một chuỗi tư duy hữu ích là

```text
microscopic model
→ order parameter
→ correlation length
→ coarse-graining
→ RG flow
→ fixed point
→ universality class
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Tính phổ quát nghĩa mọi chuyển pha đều giống nhau”

Không. Các hệ được chia thành nhiều lớp phổ quát khác nhau theo đối xứng, số chiều và cấu trúc tương tác.

### “Tái chuẩn hóa chỉ là mẹo xử lý vô cực trong QFT”

Không. Ý tưởng tái chuẩn hóa rộng hơn nhiều; trong critical phenomena, trọng tâm là sự phụ thuộc theo thang và lý thuyết hiệu dụng.

### “Trường trung bình sai nên vô dụng”

Không. Nó vẫn cho trực giác về tham số trật tự, symmetry breaking và phase diagram; trong nhiều hệ số chiều cao hoặc tương tác tầm xa, kết quả còn khá tốt.

### “Mọi power law đều chứng minh criticality”

Không. Cần kiểm tra cơ chế, phạm vi scaling, finite-size effect và các mô hình thay thế.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Chuyển pha](02_phase_transitions_heat_transfer.md), [Ensemble thống kê](03_ensembles_partition_functions.md).

**Liên hệ tiếp:** [Vật chất tô pô và khuyết tật](../10_condensed_matter_devices/04_phonons_defects_topological_matter.md), [Trường lượng tử](../09_atomic_nuclear_particle/05_quantum_fields_symmetry_interactions.md), [Dòng rối](../03_continuum/03_turbulence_rheology_soft_matter.md).
