# Nhiệt động lực học: nhiệt, công, nội năng và các quá trình

## Nhiệt động lực học bắt đầu từ một nghịch lý về mô tả

Một cốc nước chứa cỡ `10^25` phân tử. Mỗi phân tử có vị trí và vận tốc riêng, tương tác với các phân tử khác và liên tục va chạm. Về nguyên tắc, nếu biết toàn bộ trạng thái vi mô cùng các định luật động lực học, ta có thể cố mô tả từng phân tử. Trong thực tế, cách làm đó không chỉ quá lớn về tính toán mà còn không phù hợp với những câu hỏi vĩ mô mà ta muốn trả lời.

Khi hỏi “nước nóng bao nhiêu?”, “khí có áp suất bao nhiêu?” hay “động cơ có thể biến nhiệt thành công hiệu quả đến mức nào?”, ta cần các đại lượng tập thể. Nhiệt động lực học (Thermodynamics / 열역학) xây dựng mô tả bằng nhiệt độ, áp suất, thể tích, nội năng, entropy và các đại lượng trạng thái khác mà không cần theo dõi quỹ đạo của từng phân tử.

Đây là một ví dụ điển hình của tính nổi lên (Emergence / 창발): quy luật ở cấp vĩ mô có thể đơn giản và hữu ích hơn rất nhiều so với mô tả đầy đủ của mọi thành phần vi mô.

## Hệ, môi trường và trạng thái

Phần thế giới được chọn để nghiên cứu gọi là hệ (System / 계); phần còn lại gọi là môi trường (Surroundings / 주위). Ranh giới hệ có thể cho phép năng lượng và, tùy loại hệ, vật chất đi qua.

Một trạng thái nhiệt động (Thermodynamic State / 열역학적 상태) có thể được đặc trưng bởi các biến trạng thái như:

```math
P,\quad V,\quad T,\quad N,\quad U,\quad S
```

Không phải tất cả các biến này đều độc lập. Phương trình trạng thái (Equation of State / 상태방정식) tạo quan hệ ràng buộc giữa chúng.

## Nhiệt độ không phải “lượng nhiệt”

Nhiệt độ (Temperature / 온도) là đại lượng trạng thái cho phép xác định chiều truyền nhiệt khi hai hệ được đặt trong tiếp xúc nhiệt. Nếu hai hệ có nhiệt độ khác nhau, năng lượng có xu hướng truyền dưới dạng nhiệt từ hệ có nhiệt độ cao hơn sang hệ có nhiệt độ thấp hơn cho đến khi đạt cân bằng nhiệt.

Định luật số không của nhiệt động lực học (Zeroth Law of Thermodynamics / 열역학 제0법칙) phát biểu: nếu hệ A cân bằng nhiệt với C và hệ B cũng cân bằng nhiệt với C, thì A và B cân bằng nhiệt với nhau. Tính bắc cầu này cho phép nhiệt độ trở thành một đại lượng trạng thái có thể đo bằng nhiệt kế.

Ở cấp vi mô, nhiệt độ liên hệ với cách năng lượng được phân bố giữa rất nhiều bậc tự do. Nó không có nghĩa mọi hạt trong hệ đều chuyển động với cùng một tốc độ.

## Thang Kelvin và độ không tuyệt đối

Thang Kelvin (Kelvin Scale / 켈빈 온도) là thang nhiệt độ tuyệt đối. Quan hệ với độ Celsius là:

```math
T(K)=T(^\circ C)+273.15
```

Nhiều quan hệ nhiệt động lực học chỉ có ý nghĩa đúng khi nhiệt độ được dùng trên thang tuyệt đối. Ví dụ phương trình khí lý tưởng và hiệu suất Carnot sử dụng nhiệt độ theo kelvin.

`0 K` là độ không tuyệt đối (Absolute Zero / 절대영도), một giới hạn nhiệt động lực học đặc biệt. Không nên hiểu nó đơn giản là “mọi chuyển động vi mô đều dừng hoàn toàn”, vì hệ lượng tử vẫn có thể có năng lượng điểm không và các dao động lượng tử.

## Nhiệt, công và nội năng

Nội năng (Internal Energy / 내부에너지), ký hiệu `U`, là năng lượng vi mô chứa trong hệ do chuyển động tịnh tiến, quay, dao động và tương tác giữa các thành phần, tùy cấu trúc của hệ.

Nhiệt (Heat / 열), ký hiệu `Q`, không phải một “chất” nằm sẵn trong vật. Nhiệt là **năng lượng được truyền qua ranh giới hệ do chênh lệch nhiệt độ**.

Công (Work / 일) cũng là một cách truyền năng lượng qua ranh giới hệ, nhưng thông qua những biến đổi có tổ chức ở cấp vĩ mô, chẳng hạn nén khí bằng pít-tông, công điện hoặc công quay của trục.

Sau khi quá trình truyền kết thúc, ta nói nội năng của hệ đã thay đổi; không nên nói hệ đang “chứa một lượng nhiệt” theo nghĩa nhiệt là một biến trạng thái.

## Định luật I: bảo toàn năng lượng cho hệ nhiệt động

Nếu quy ước `W` là công do hệ thực hiện lên môi trường, định luật I viết:

```math
\Delta U=Q-W
```

Nếu `Q>0`, năng lượng truyền vào hệ dưới dạng nhiệt. Nếu `W>0`, hệ truyền năng lượng ra môi trường bằng cách thực hiện công.

Một số giáo trình dùng quy ước `W` là công tác dụng **lên hệ**, khi đó viết:

```math
\Delta U=Q+W
```

Hai cách viết không mâu thuẫn về vật lý; điều quan trọng là phải xác định và giữ nhất quán quy ước dấu.

Định luật I chính là bảo toàn năng lượng được áp dụng cho hệ nhiệt động lực học.

## Công do khí thực hiện

Nếu một chất khí đẩy pít-tông trong quá trình gần tĩnh (quasi-static), phần công vi phân do khí thực hiện là:

```math
dW=P\,dV
```

Do đó:

```math
W=\int_{V_1}^{V_2}P\,dV
```

Trên đồ thị `P-V`, công là diện tích dưới đường biểu diễn quá trình, với dấu phụ thuộc chiều thay đổi thể tích và quy ước đang dùng.

Điểm quan trọng là công phụ thuộc đường đi (path dependent). Hai quá trình có cùng trạng thái đầu và cuối có thể có `Q` và `W` khác nhau, trong khi `\Delta U` vẫn giống nhau vì nội năng `U` là hàm trạng thái.

## Khí lý tưởng

Phương trình khí lý tưởng (Ideal Gas Law / 이상기체 상태방정식) có thể viết:

```math
PV=Nk_BT
```

hoặc:

```math
PV=nRT
```

Trong đó `N` là số phân tử, `k_B` là hằng số Boltzmann, `n` là số mol và `R=N_Ak_B`.

Mô hình khí lý tưởng giả định các hạt đủ thưa để thể tích riêng của từng hạt và tương tác thế giữa chúng có thể bỏ qua trong phần lớn thời gian, ngoại trừ các va chạm được lý tưởng hóa thích hợp.

### Áp suất từ va chạm phân tử

Trong mô hình khí lý tưởng đơn nguyên tử, lý thuyết động học dẫn tới:

```math
PV=\frac{2}{3}K_{trans,total}
```

So sánh với:

```math
PV=Nk_BT
```

suy ra động năng tịnh tiến trung bình của mỗi phân tử:

```math
\langle K_{trans}\rangle=\frac32k_BT
```

Vì vậy, trong mô hình này, nhiệt độ liên hệ trực tiếp với động năng tịnh tiến trung bình của các phân tử. Không nên mở rộng kết luận này máy móc sang mọi hệ, vì các bậc tự do và tương tác có thể phức tạp hơn nhiều.

## Định lý phân bố đều năng lượng và bậc tự do

Trong giới hạn cổ điển ở cân bằng nhiệt, định lý phân bố đều năng lượng (Equipartition Theorem / 에너지 등분배 정리) cho biết mỗi hạng tử bậc hai độc lập trong Hamiltonian đóng góp trung bình:

```math
\frac12k_BT
```

vào năng lượng.

Một khí lý tưởng đơn nguyên tử có ba bậc tự do tịnh tiến nên nhận đóng góp trung bình `3k_BT/2` cho mỗi hạt.

Phân tử còn có thể có các mode quay và dao động. Tuy nhiên hiệu ứng lượng tử có thể làm một số mode gần như không được kích thích nếu khoảng cách mức năng lượng lớn so với `k_BT`. Vì vậy nhiệt dung thực không phải lúc nào cũng tuân giá trị dự đoán bởi phân bố đều năng lượng cổ điển.

## Nhiệt dung

Nhiệt dung (Heat Capacity / 열용량) mô tả lượng năng lượng cần truyền dưới dạng nhiệt để thay đổi nhiệt độ theo một quá trình xác định. Ta thường viết:

```math
C=\frac{dQ}{dT}
```

Nhiệt dung riêng theo khối lượng là:

```math
c=\frac{1}{m}\frac{dQ}{dT}
```

Đối với chất khí, phải chỉ rõ điều kiện của quá trình. Hai đại lượng quan trọng là:

```math
C_V,\qquad C_P
```

Ở thể tích không đổi, khí không thực hiện công `P\,dV`. Ở áp suất không đổi, một phần năng lượng truyền vào có thể dùng cho sự giãn nở, nên với khí lý tưởng thông thường ta có `C_P>C_V`.

## Các quá trình cơ bản

### Đẳng tích (Isochoric / 등적 과정)

Nếu:

```math
V=constant
```

thì:

```math
W=0
```

và theo quy ước đang dùng:

```math
\Delta U=Q
```

### Đẳng áp (Isobaric / 등압 과정)

Nếu áp suất không đổi:

```math
W=P\Delta V
```

### Đẳng nhiệt của khí lý tưởng (Isothermal / 등온 과정)

Nếu:

```math
T=constant
```

thì nội năng của khí lý tưởng không đổi vì `U` chỉ phụ thuộc nhiệt độ trong mô hình này:

```math
\Delta U=0
```

Do đó:

```math
Q=W
```

Với quá trình đẳng nhiệt thuận nghịch:

```math
W=nRT\ln\frac{V_2}{V_1}
```

Logarithm xuất hiện từ tích phân `\int dV/V` vì `P=nRT/V`.

### Đoạn nhiệt (Adiabatic / 단열 과정)

Nếu không có truyền nhiệt qua ranh giới hệ:

```math
Q=0
```

nên:

```math
\Delta U=-W
```

Với khí lý tưởng trong quá trình đoạn nhiệt thuận nghịch:

```math
PV^\gamma=constant
```

trong đó:

```math
\gamma=\frac{C_P}{C_V}
```

## Mô hình tư duy (Mental Model)

> Nhiệt động lực học không cố mô tả từng phân tử đang làm gì. Nó tìm một số biến trạng thái và định luật bảo toàn đủ mạnh để dự đoán sự thay đổi ở cấp vĩ mô. Nhiệt và công mô tả **cách năng lượng đi qua ranh giới hệ**; nội năng mô tả một phần năng lượng thuộc trạng thái của hệ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Một vật chứa nhiệt”

Không theo ngôn ngữ nhiệt động lực học chính xác. Hệ có nội năng; nhiệt là năng lượng đang được truyền do chênh lệch nhiệt độ.

### “Nhiệt độ cao nghĩa mọi phân tử đều chuyển động nhanh hơn mọi phân tử của vật lạnh hơn”

Không. Nhiệt độ liên hệ với phân bố thống kê của năng lượng. Hai phân bố có thể chồng lấp mạnh, và một số hạt của hệ lạnh vẫn có thể có năng lượng lớn hơn một số hạt của hệ nóng.

### “Quá trình đoạn nhiệt luôn có nhiệt độ không đổi”

Không. Đoạn nhiệt nghĩa `Q=0`; nhiệt độ vẫn có thể thay đổi do công làm thay đổi nội năng. Đẳng nhiệt và đoạn nhiệt là hai điều kiện khác nhau.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Năng lượng](../01_mechanics/03_work_energy_power.md).

**Liên hệ tiếp:** [Entropy và cơ học thống kê](01_entropy_statistical_mechanics.md), [Ensemble và hàm phân hoạch](03_ensembles_partition_functions.md).
