# Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**. Route đi từ governing equations → discretization → numerical stability/error → Monte Carlo/sampling → inverse computation, để tính toán giữ được ý nghĩa vật lý.

## Vì sao cần vật lý tính toán?

Nhiều mô hình vật lý có phương trình chính xác nhưng không có nghiệm giải tích thuận tiện. Khi hình học phức tạp, hệ có nhiều bậc tự do, phương trình phi tuyến hoặc dữ liệu thực nghiệm lớn, ta phải chuyển bài toán liên tục thành một bài toán số mà máy tính có thể xử lý. Quá trình đó gọi là rời rạc hóa (discretization).

Một mô phỏng vì vậy là **mô hình của một mô hình**. Trước hết ta chọn mô hình vật lý, sau đó chọn cách biểu diễn số cho mô hình ấy. Sai số có thể xuất hiện ở cả hai tầng.

> **Nối mạch:** Trong **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Tích phân số theo thời gian** nối từ **Vì sao cần vật lý tính toán?** sang **Độ ổn định số và bước thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tích phân số theo thời gian

Với chuyển động một chiều,

```math
\frac{dx}{dt}=v,\qquad \frac{dv}{dt}=a,
```

phương pháp Euler tiến (forward Euler) dùng

```math
x_{n+1}=x_n+v_n\Delta t,
```

```math
v_{n+1}=v_n+a_n\Delta t.
```

Phương pháp này đơn giản nhưng sai số tích lũy và miền ổn định có thể kém. Các phương pháp Runge–Kutta đánh giá đạo hàm tại nhiều điểm trong một bước để đạt bậc chính xác cao hơn.

Với các hệ Hamilton, bộ tích phân bảo toàn cấu trúc (symplectic integrator) thường có lợi cho mô phỏng dài hạn vì nó tôn trọng hình học của không gian pha tốt hơn. Một phương pháp có sai số cục bộ nhỏ nhất chưa chắc là phương pháp tốt nhất cho mọi cấu trúc vật lý.

> **Nối mạch:** Ở chặng này của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Độ ổn định số và bước thời gian** nối từ **Tích phân số theo thời gian** sang **Rời rạc hóa phương trình vi phân riêng phần**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ ổn định số và bước thời gian

Một hệ vật lý ổn định vẫn có thể cho nghiệm số phát nổ nếu bước thời gian quá lớn. Độ ổn định số (numerical stability) là tính chất của thuật toán rời rạc, không phải chỉ của hệ vật lý ban đầu.

Dao động tử điều hòa là ví dụ điển hình. Euler tiến có thể làm năng lượng tăng giả tạo theo thời gian. Khi nhìn một quỹ đạo số tăng biên độ, cần phân biệt đó là bất ổn thật của hệ hay chỉ là nhiễu giả số (numerical artifact).

Bước thời gian phải đủ nhỏ để phân giải các thang thời gian quan trọng. Trong nhiều phương trình sóng và chất lưu, điều kiện kiểu Courant–Friedrichs–Lewy (CFL) liên hệ bước thời gian với kích thước lưới và tốc độ truyền tín hiệu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Rời rạc hóa phương trình vi phân riêng phần** nối từ **Độ ổn định số và bước thời gian** sang **Hội tụ và kiểm tra lưới**, vì cơ chế trước tạo đầu vào cho bước sau.

## Rời rạc hóa phương trình vi phân riêng phần

Phương trình nhiệt

```math
\frac{\partial T}{\partial t}=\alpha\nabla^2T
```

và phương trình sóng

```math
\frac{\partial^2u}{\partial t^2}=c^2\nabla^2u
```

là các phương trình vi phân riêng phần (partial differential equations, PDE). Navier–Stokes và các phương trình Maxwell cũng thuộc nhóm này.

Các họ phương pháp phổ biến gồm sai phân hữu hạn (finite difference), thể tích hữu hạn (finite volume), phần tử hữu hạn (finite element) và phương pháp phổ (spectral method). Mỗi phương pháp chọn một cách biểu diễn không gian khác nhau và có ưu điểm riêng về hình học, độ chính xác, tính bảo toàn và chi phí tính toán.

Thể tích hữu hạn đặc biệt tự nhiên cho các định luật bảo toàn vì nó tính dòng thông lượng qua biên của từng ô. Phần tử hữu hạn mạnh khi hình học phức tạp. Phương pháp phổ có thể đạt độ chính xác rất cao với nghiệm đủ trơn.

> **Nối mạch:** Trong **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Hội tụ và kiểm tra lưới** nối từ **Rời rạc hóa phương trình vi phân riêng phần** sang **Phương pháp Monte Carlo**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hội tụ và kiểm tra lưới

Nếu giảm kích thước lưới `\Delta x` hoặc bước thời gian `\Delta t`, kết quả phải tiến tới một giới hạn ổn định trong miền mà phương pháp hội tụ. Nếu kết quả thay đổi mạnh khi tinh chỉnh lưới, mô phỏng chưa đủ độ phân giải để đưa ra kết luận chắc chắn.

Kiểm tra hội tụ (convergence test) không chứng minh mô hình vật lý đúng, nhưng nó giúp tách sai số rời rạc hóa khỏi sai số mô hình.

> **Nối mạch:** Ở chặng này của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Phương pháp Monte Carlo** nối từ **Hội tụ và kiểm tra lưới** sang **Bài toán thuận và bài toán ngược**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phương pháp Monte Carlo

Monte Carlo dùng lấy mẫu ngẫu nhiên để ước lượng tích phân, phân bố hoặc giá trị kỳ vọng. Với lấy mẫu độc lập đơn giản, sai số thống kê thường giảm theo

```math
\sim\frac{1}{\sqrt N}.
```

Tốc độ này chậm, nhưng lợi thế là nó không suy giảm quá nhanh khi số chiều tăng. Vì vậy Monte Carlo xuất hiện trong vận chuyển hạt, cơ học thống kê, suy luận Bayes và nhiều bài toán có không gian trạng thái rất lớn.

Trong đồ họa máy tính, dò tia (ray tracing) và lấy mẫu đường đi (path tracing) cũng dùng ý tưởng Monte Carlo để ước lượng phương trình truyền ánh sáng. Đây là một ví dụ rõ về cùng một cấu trúc toán học xuất hiện ở vật lý và kỹ thuật phần mềm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Bài toán thuận và bài toán ngược** nối từ **Phương pháp Monte Carlo** sang **Sai số dấu phẩy động**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bài toán thuận và bài toán ngược

Bài toán thuận (forward problem) đi từ tham số mô hình tới quan sát:

```text
tham số → mô hình → dữ liệu dự đoán
```

Bài toán ngược (inverse problem) đi theo hướng ngược lại:

```text
dữ liệu quan sát → suy ra tham số hoặc cấu trúc nguồn
```

Chụp cắt lớp CT, MRI, địa chấn học, kính hiển vi và thiên văn học đều chứa các bài toán ngược. Chúng thường không chỉnh (ill-posed): một thay đổi nhỏ của dữ liệu có thể làm nghiệm thay đổi lớn, hoặc nhiều cấu hình nguồn khác nhau có thể tạo dữ liệu gần giống nhau.

Chuẩn hóa (regularization) và thông tin tiên nghiệm (prior information) giúp ổn định nghiệm, nhưng đồng thời đưa thêm giả định vào kết quả. Vì vậy cần tách rõ điều gì đến từ dữ liệu và điều gì đến từ giả định của phương pháp.

> **Nối mạch:** Trong **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Sai số dấu phẩy động** nối từ **Bài toán thuận và bài toán ngược** sang **Khả năng tái lập và nguồn gốc kết quả**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sai số dấu phẩy động

Máy tính không biểu diễn chính xác mọi số thực. Số dấu phẩy động (floating-point number) có phạm vi và độ chính xác hữu hạn. Các phép trừ hai số gần nhau, cộng một lượng rất nhỏ vào một số rất lớn hoặc lặp phép tính hàng triệu lần có thể làm sai số làm tròn tích lũy.

Không phải mọi sai lệch số đều được giải quyết bằng cách dùng kiểu dữ liệu có nhiều bit hơn. Cách sắp xếp thuật toán, điều kiện bài toán và độ nhạy của mô hình cũng quan trọng.

> **Nối mạch:** Ở chặng này của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Sai số dấu phẩy động** đặt vấn đề; **Khả năng tái lập và nguồn gốc kết quả** đối chiếu bằng chứng, rồi **Đơn vị trong mã nguồn** mở rộng hệ quả hoặc giới hạn liên quan.

## Khả năng tái lập và nguồn gốc kết quả

Một kết quả tính toán khoa học nên cho phép người khác xác định nó được tạo ra như thế nào. Cần lưu phiên bản dữ liệu, mã nguồn và lần ghi nhận (commit / 커밋), tham số cấu hình, môi trường chạy, thư viện phụ thuộc, hạt giống ngẫu nhiên khi cần, đơn vị và các bước tiền xử lý.

Đây là điểm vật lý tính toán gặp trực tiếp kỹ nghệ phần mềm (software engineering / 소프트웨어 공학). Git, kiểm thử, bộ chứa (container / 컨테이너) và tích hợp liên tục không chỉ là tiện ích phát triển; chúng giúp bảo vệ khả năng truy vết và tái lập kết quả khoa học.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Khả năng tái lập và nguồn gốc kết quả** đặt vấn đề; **Đơn vị trong mã nguồn** đối chiếu bằng chứng, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

## Đơn vị trong mã nguồn

Sai đơn vị có thể phá hỏng một mô hình dù mọi phép tính số học đều đúng. Vì vậy đơn vị nên được xem như một phần của hợp đồng kiểu dữ liệu, không phải chỉ là chú thích.

Sự cố Mars Climate Orbiter thường được nhắc như một ví dụ lịch sử về hậu quả của việc dùng không nhất quán hệ đơn vị trong giao diện dữ liệu. Bài học tổng quát là: một giá trị số không có ý nghĩa vật lý đầy đủ nếu thiếu đơn vị và quy ước.

> **Nối mạch:** Trong **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, các dấu vết trong **Đơn vị trong mã nguồn** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Một mô phỏng đi qua hai lần trừu tượng hóa:

```text
hệ vật lý thực
→ mô hình vật lý
→ mô hình số
→ thuật toán
→ kết quả máy tính
```

Vì vậy “chương trình chạy được” không đồng nghĩa với “vật lý đúng”. Cần kiểm tra mô hình, điều kiện biên, độ ổn định, hội tụ, sai số làm tròn và tính hợp lý vật lý của kết quả.

> **Nối mạch:** Ở chặng này của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, **Những ngộ nhận thường gặp (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Giảm bước thời gian luôn làm kết quả đúng”

Giảm bước thời gian chỉ giảm một thành phần sai số nếu phương pháp hội tụ và mô hình vật lý phù hợp. Sai điều kiện biên hoặc sai mô hình không được sửa bằng lưới mịn hơn.

### “Phương pháp bậc cao luôn tốt hơn”

Không nhất thiết. Bài toán cứng (stiff), hệ Hamilton, phương trình bảo toàn hoặc bài toán có sốc có thể cần phương pháp được thiết kế cho cấu trúc riêng của chúng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vật lý tính toán: rời rạc hóa, độ ổn định, Monte Carlo và bài toán ngược**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Ngôn ngữ toán học](../00_foundations/03_mathematical_language.md), [Vật lý thực nghiệm](00_measurement_experiment.md).

**Liên hệ tiếp:** [Động lực học phi tuyến và hỗn loạn](../01_mechanics/09_nonlinear_dynamics_chaos.md), [Vật lý plasma](../10_condensed_matter_devices/03_plasma_physics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
