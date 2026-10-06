# Mô hình toán học, phân tích thứ nguyên và scaling

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Mô hình toán học, phân tích thứ nguyên và scaling**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ hiện tượng đến biến số** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Đơn vị là một phần của toán học, không phải nhãn trang trí** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối mô hình toán với thứ nguyên, tỷ lệ và xấp xỉ, để biết khi nào một mô hình có thể mở rộng sang quy mô khác.

Toán học trở nên hữu ích khi ta biến một vấn đề trong thế giới thật thành một cấu trúc có thể suy luận. Quá trình đó gọi là **mô hình hóa toán học (Mathematical Modeling / 수학적 모델링)**. Một mô hình không phải bản sao hoàn hảo của thực tế. Nó là một lựa chọn có chủ đích: giữ lại những đại lượng và quan hệ quan trọng cho câu hỏi đang hỏi, đồng thời bỏ qua những chi tiết chưa cần thiết.

Nếu hỏi “một chiếc xe mất bao lâu để đi 120 km?”, ta có thể bắt đầu với mô hình cực đơn giản `distance = speed × time`. Nhưng nếu tốc độ thay đổi, đường có đèn đỏ, xe dừng nghỉ hoặc GPS đo sai, mô hình đó không còn đủ. Điều quan trọng không phải tìm một công thức “đúng tuyệt đối”, mà là biết giả định (assumption / 가정) nào khiến mô hình hợp lý và khi nào cần thay mô hình.

## Từ hiện tượng đến biến số

Bước đầu tiên của modeling là xác định **biến (Variable / 변수)**, **tham số (Parameter / 매개변수)** và **ràng buộc (Constraint / 제약조건)**. Biến là đại lượng có thể thay đổi trong bài toán. Tham số thường được xem như cố định trong một lần chạy mô hình nhưng có thể thay đổi giữa các trường hợp. ràng buộc (constraint / 제약조건) xác định những trạng thái được phép.

Ví dụ với quãng đường `d`, vận tốc `v` và thời gian `t`, quan hệ lý tưởng là

```math
d=vt.
```

Nếu `v` được xem là tốc độ trung bình đã biết, `t` là unknown cần tìm và `d` là dữ liệu đầu vào, thì `v` đang đóng vai trò parameter. Nhưng trong mô hình khác, `v(t)` lại là một hàm (function / 함수) thay đổi theo thời gian. Cùng một ký hiệu không quyết định vai trò; câu hỏi và mô hình quyết định.

> **Nối mạch:** Trong **Mô hình toán học, phân tích thứ nguyên và scaling**, **Đơn vị là một phần của toán học, không phải nhãn trang trí** nối từ **Từ hiện tượng đến biến số** sang **Dimensionless quantity và vì sao ratio mạnh đến vậy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đơn vị là một phần của toán học, không phải nhãn trang trí

**Thứ nguyên (Dimension / 차원)** mô tả loại đại lượng vật lý: chiều dài `[L]`, thời gian `[T]`, khối lượng `[M]` và các combination của chúng. **Đơn vị (Unit / 단위)** là cách cụ thể để đo thứ nguyên đó: mét, kilomet, giây, giờ, kilogram.

Vận tốc có dimension

```math
[L][T]^{-1}
```

vì nó là distance chia cho thời gian (time / 시간). Gia tốc có dimension

```math
[L][T]^{-2}.
```

Một phương trình vật lý hợp lệ phải **đồng nhất thứ nguyên (Dimensionally Consistent / 차원 일관성)**. Chẳng hạn

```math
d=vt
```

có vế phải mang dimension

```math
[L][T]^{-1}[T]=[L],
```

khớp với distance. Nếu ai đó viết `d=v+t`, biểu thức đó đã đáng nghi trước khi cần thay số, vì không thể cộng một velocity với một thời gian (time / 시간) như hai đại lượng cùng loại.

> Dimensional phân tích (analysis / 분석) là một kiểu (type / 타입) checker cho các mô hình định lượng. Nó không chứng minh công thức đúng, nhưng có thể loại bỏ rất nhiều công thức sai ngay lập tức.

Trong programming, mô hình tư duy (mental model / 사고 모델) này gần với kiểu (type / 타입) các hệ thống (systems / 시스템들). Cộng `LocalDate` với `BigDecimal` vô nghĩa không phải vì trình biên dịch (compiler / 컴파일러) “khó tính”, mà vì hai đối tượng (object / 객체) biểu diễn hai loại quantity khác nhau. Các thư viện units-of-measure cố đưa chính tư tưởng dimensional consistency vào mã (code / 코드).

> **Nối mạch:** Ở chặng này của **Mô hình toán học, phân tích thứ nguyên và scaling**, **Dimensionless quantity và vì sao ratio mạnh đến vậy** nối từ **Đơn vị là một phần của toán học, không phải nhãn trang trí** sang **Scaling: nếu kích thước tăng gấp đôi thì điều gì thực sự thay đổi?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dimensionless quantity và vì sao ratio mạnh đến vậy

Một đại lượng **không thứ nguyên (Dimensionless Quantity / 무차원량)** xuất hiện khi units triệt tiêu. Ví dụ strain trong mechanics là `ΔL/L`; xác suất (probability / 확률) là ratio; percentage là ratio nhân 100; cosine là ratio giữa lengths trong tam giác đồng dạng.

Dimensionless quantities đặc biệt quan trọng vì chúng dễ so sánh giữa các hệ thống (systems / 시스템들) có quy mô (scale / 규모) khác nhau. Một chiếc mô hình dài 10 cm và một cây cầu dài 100 m có thể chia sẻ một số dimensionless ratios dù kích thước tuyệt đối khác nhau. kỹ thuật (engineering / 엔지니어링) thường dùng các dimensionless numbers để xác định khi hai hệ thống có hành vi (behavior / 동작) tương tự.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mô hình toán học, phân tích thứ nguyên và scaling**, **Scaling: nếu kích thước tăng gấp đôi thì điều gì thực sự thay đổi?** nối từ **Dimensionless quantity và vì sao ratio mạnh đến vậy** sang **Thứ tự (order / 순서) of magnitude và ước lượng Fermi**, vì cơ chế trước tạo đầu vào cho bước sau.

## Scaling: nếu kích thước tăng gấp đôi thì điều gì thực sự thay đổi?

**Scaling / 스케일링** nghiên cứu cách một quantity thay đổi khi characteristic kích thước (size / 크기) thay đổi. Với một hình vuông cạnh `s`, perimeter tăng theo `s`, còn area tăng theo `s^2`:

```math
P=4s,
\qquad
A=s^2.
```

Nếu cạnh tăng gấp 2, perimeter tăng gấp 2 nhưng area tăng gấp 4. Với vật thể ba chiều, volume thường quy mô (scale / 규모) như `s^3`.

Điều này giải thích nhiều hiện tượng đời sống. Một animal lớn hơn không chỉ là animal nhỏ “phóng to”. Surface area và volume tăng theo powers khác nhau, nên heat mất mát (loss / 손실), structural stress và metabolic các ràng buộc (constraints / 제약조건들) thay đổi. Trong software, scaling cũng xuất hiện theo cách tương tự: nếu một thuật toán (algorithm / 알고리즘) so sánh mọi pair trong `n` records, công việc (work / 작업) quy mô (scale / 규모) gần `n^2`; doubling đầu vào (input / 입력) có thể làm công việc (work / 작업) tăng khoảng bốn lần.

> **Nối mạch:** Trong **Mô hình toán học, phân tích thứ nguyên và scaling**, **Thứ tự (order / 순서) of magnitude và ước lượng Fermi** nối từ **Scaling: nếu kích thước tăng gấp đôi thì điều gì thực sự thay đổi?** sang **Sensitivity: kết quả nhạy đến giả định (assumption / 가정) nào?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thứ tự (order / 순서) of magnitude và ước lượng Fermi

Trong nhiều tình huống, chính xác (exact / 정확한) dữ liệu (data / 데이터) không có sẵn. **Ước lượng bậc độ lớn (Order-of-Magnitude Estimate / 자릿수 규모 추정)** hỏi quantity nằm khoảng `10^2`, `10^3` hay `10^6`, thay vì đòi decimal chính xác giả tạo.

Một **Fermi estimate / 페르미 추정** phân rã câu hỏi lớn thành các factors dễ ước lượng hơn. Muốn ước lượng bao nhiêu ly cà phê được bán ở một quận mỗi ngày, ta có thể mô hình (model / 모델):

```math
\text{population}
\times
\text{fraction buying coffee}
\times
\text{cups per buyer per day}.
```

Mỗi factor có bất định (uncertainty / 불확실성), nhưng sản phẩm (product / 제품) vẫn có thể cho quy mô (scale / 규모) đủ tốt để kiểm tra feasibility hoặc detect một con số vô lý.

Đây cũng là kỹ năng quan trọng khi rà soát (review / 검토) hệ thống (system / 시스템) thiết kế (design / 설계). Nếu một dịch vụ (service / 서비스) có 2 triệu users, mỗi người dùng (user / 사용자) tạo 20 requests/ngày, traffic trung bình là khoảng

```math
\frac{2\times10^6\times20}{86400}
\approx 463\ \text{requests/s}.
```

Peak traffic có thể cao hơn nhiều, nhưng phép tính thô giúp ta biết mình đang nói về vài trăm, vài nghìn hay vài triệu requests/s.

> **Nối mạch:** Ở chặng này của **Mô hình toán học, phân tích thứ nguyên và scaling**, **Sensitivity: kết quả nhạy đến giả định (assumption / 가정) nào?** nối từ **Thứ tự (order / 순서) of magnitude và ước lượng Fermi** sang **Mô hình (model / 모델) kiểm tra hợp lệ (validation / 검증) và residual**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sensitivity: kết quả nhạy đến giả định (assumption / 가정) nào?

Một mô hình (model / 모델) thường phụ thuộc vào parameters `p_1,p_2,...`. **Phân tích độ nhạy (Sensitivity Analysis / 민감도 분석)** hỏi kết quả thay đổi bao nhiêu khi một parameter thay đổi.

Nếu

```math
R=pq,
```

thì small relative changes gần thỏa

```math
\frac{\Delta R}{R}
\approx
\frac{\Delta p}{p}+\frac{\Delta q}{q}.
```

Điều này cho thấy bất định (uncertainty / 불확실성) tương đối có xu hướng cộng trong sản phẩm (product / 제품) ở first-order approximation. Trong nghiệp vụ (business / 비즈니스) mô hình (model / 모델), một forecast revenue có thể phụ thuộc vào traffic, conversion tỷ lệ (rate / 비율) và average thứ tự (order / 순서) giá trị (value / 값). Nếu conclusion chỉ đúng khi conversion tỷ lệ (rate / 비율) chính xác đến 0.01%, mô hình (model / 모델) rất fragile.

Sensitivity nối trực tiếp với derivatives: derivative chính là cục bộ (local / 로컬) sensitivity. Với hàm (function / 함수) `y=f(x)`, quantity

```math
\frac{dy}{dx}
```

cho biết đầu ra (output / 출력) phản ứng cục bộ (local / 로컬) mạnh đến mức nào trước thay đổi đầu vào (input / 입력).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mô hình toán học, phân tích thứ nguyên và scaling**, **Mô hình (model / 모델) kiểm tra hợp lệ (validation / 검증) và residual** nối từ **Sensitivity: kết quả nhạy đến giả định (assumption / 가정) nào?** sang **Giả định (assumption / 가정), approximation và lĩnh vực (domain / 도메인) of validity**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mô hình (model / 모델) kiểm tra hợp lệ (validation / 검증) và residual

Sau khi dựng mô hình (model / 모델), ta phải so sánh prediction với observation. Difference giữa observed giá trị (value / 값) `y_i` và prediction `\hat y_i` thường gọi là **residual / 잔차**:

```math
r_i=y_i-\hat y_i.
```

Residual không chỉ là “lỗi (error / 오류) cần giảm”. mẫu (pattern / 패턴) trong residual có thể cho thấy giả định (assumption / 가정) sai. Nếu residual tăng dần theo thời gian (time / 시간), mô hình (model / 모델) có thể đang thiếu trend. Nếu variance của residual tăng cùng magnitude, noise có thể không homoscedastic. Statistics và machine học tập (learning / 학습) phát triển phần lớn từ chính câu hỏi: làm sao đánh giá mô hình (model / 모델) khi dữ liệu (data / 데이터) chứa bất định (uncertainty / 불확실성)?

> **Nối mạch:** Trong **Mô hình toán học, phân tích thứ nguyên và scaling**, **Giả định (assumption / 가정), approximation và lĩnh vực (domain / 도메인) of validity** nối từ **Mô hình (model / 모델) kiểm tra hợp lệ (validation / 검증) và residual** sang **Liên kết kiến thức (knowledge connection / 지식 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Giả định (assumption / 가정), approximation và lĩnh vực (domain / 도메인) of validity

Một approximation không phải false statement. Nó là statement đúng trong một regime nhất định. Ví dụ với `x` nhỏ,

```math
\sin x\approx x
```

khi `x` đo bằng radian. Đây là cục bộ (local / 로컬) approximation xuất phát từ Taylor series. Nếu `x=0.01`, approximation rất tốt; nếu `x=2`, nó không còn tốt. Vấn đề không phải “approximation sai”, mà là đã dùng ngoài lĩnh vực (domain / 도메인) of validity.

Khi đọc bất kỳ mô hình (model / 모델) nào, nên hỏi ba câu: what is being ignored, what quy mô (scale / 규모) are we operating at, and which variables are treated as independent even though reality may couple them?

> **Nối mạch:** Ở chặng này của **Mô hình toán học, phân tích thứ nguyên và scaling**, sau nội dung của **Giả định (assumption / 가정), approximation và lĩnh vực (domain / 도메인) of validity**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Modeling là nơi nhiều nhánh Toán gặp nhau. Algebra biểu diễn relationships; functions biến inputs thành outputs; calculus đo sensitivity và dynamics; xác suất (probability / 확률) biểu diễn bất định (uncertainty / 불확실성); statistics kiểm tra mô hình (model / 모델) bằng dữ liệu (data / 데이터); tối ưu hóa (optimization / 최적화) chọn parameters; numerical mathematics tính approximation trên máy tính.

Trong machine học tập (learning / 학습), một neural mạng (network / 네트워크) là một parameterized hàm (function / 함수) family. huấn luyện (training / 학습) là tối ưu hóa (optimization / 최적화); mất mát (loss / 손실) là mục tiêu (objective / 목표); regularization là ràng buộc (constraint / 제약조건)/penalty; kiểm tra hợp lệ (validation / 검증) kiểm tra khả năng generalize. Trong finance, discounted cash-flow mô hình (model / 모델) biến các giả định (assumptions / 가정들) về future cash luồng (flow / 흐름) và discount tỷ lệ (rate / 비율) thành present giá trị (value / 값). Trong physics, differential equations mô hình (model / 모델) laws of thay đổi (change / 변경). Những trường hợp này khác lĩnh vực (domain / 도메인) nhưng cùng một mental cấu trúc (structure / 구조).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Mô hình toán học, phân tích thứ nguyên và scaling**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Một mathematical mô hình (model / 모델) là một “máy suy luận có điều kiện”: nếu các các giả định (assumptions / 가정들) và relationships ta chọn đủ phù hợp với câu hỏi, mô hình (model / 모델) cho phép biến dữ liệu đầu vào thành prediction hoặc quyết định (decision / 결정). Dimensional phân tích (analysis / 분석) kiểm tra mô hình (model / 모델) có nói đúng loại quantity; scaling cho biết điều gì xảy ra khi kích thước thay đổi; sensitivity cho biết giả định (assumption / 가정) nào thực sự chi phối kết quả.

> **Nối mạch:** Trong **Mô hình toán học, phân tích thứ nguyên và scaling**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

Mô hình phức tạp hơn không tự động tốt hơn. độ phức tạp (complexity / 복잡도) chỉ hữu ích nếu nó mô tả cấu trúc (structure / 구조) cần cho câu hỏi và được dữ liệu (data / 데이터) hỗ trợ. Một mô hình (model / 모델) đơn giản với các giả định (assumptions / 가정들) rõ có thể đáng tin hơn mô hình (model / 모델) rất nhiều parameters nhưng không validate được.

Dimensional consistency cũng không chứng minh công thức đúng. `d=vt` và `d=2vt` đều dimensionally consistent, nhưng coefficient và relationship phải đến từ lập luận (reasoning / 추론) hoặc bằng chứng (evidence / 증거) khác.

Cuối cùng, precision không đồng nghĩa accuracy. Viết `12.384729%` từ những các giả định (assumptions / 가정들) chỉ chính xác khoảng 10% là false precision. Số chữ số phải phản ánh bất định (uncertainty / 불확실성) của mô hình (model / 모델), không phải khả năng máy tính in nhiều decimal places.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
