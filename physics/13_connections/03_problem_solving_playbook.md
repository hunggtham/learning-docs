# Cẩm nang giải bài Vật lý: từ mô hình đến kiểm chứng

Một bài Vật lý tốt hiếm khi được giải chỉ bằng cách nhớ đúng công thức. Kỹ năng quan trọng hơn là biến một tình huống thực thành **mô hình vật lý (physical model)** đủ đơn giản để tính toán nhưng vẫn giữ được cơ chế chi phối. Quy trình dưới đây có thể dùng từ cơ học cơ bản tới nhiệt, điện từ, lượng tử và mô phỏng số.

## 1. Bắt đầu bằng hệ vật lý, không bắt đầu bằng công thức

Trước khi viết phương trình, hãy xác định **ranh giới của hệ (system boundary)**. Ta đang theo dõi một vật, một tập hợp hạt, một thể tích chất lưu, một trường điện từ hay toàn bộ hệ kín? Việc chọn hệ quyết định đại lượng nào là nội tại và đại lượng nào đi qua biên dưới dạng lực, công, nhiệt, dòng khối lượng hay thông lượng.

Ví dụ, với một vật trượt xuống mặt phẳng nghiêng, nếu hệ chỉ gồm vật thì trọng lực là ngoại lực. Nếu hệ gồm vật và Trái Đất, thế năng hấp dẫn có thể được xem là năng lượng của hệ. Hai cách mô hình hóa đều hợp lệ nhưng dẫn tới cách tổ chức phương trình khác nhau.

Sau đó xác định **biến trạng thái (state variables)** và **bậc tự do (degrees of freedom)**. Chất điểm trong không gian cần tọa độ vị trí; con lắc lý tưởng chỉ cần một góc; khí lý tưởng ở cân bằng có thể mô tả bằng `P, V, T, N`; trạng thái lượng tử cần vectơ trạng thái hoặc hàm sóng. Chọn quá nhiều biến làm bài toán nặng không cần thiết, còn chọn quá ít có thể làm mất cơ chế quan trọng.

## 2. Vẽ hình và chọn hệ tọa độ theo đối xứng

Hệ tọa độ nên phục vụ vật lý. Với mặt phẳng nghiêng, một trục song song mặt phẳng thường làm phương trình lực đơn giản hơn. Bài có đối xứng tròn hợp với tọa độ cực hoặc trụ; phân bố cầu thường hợp với tọa độ cầu.

Trước khi tính, hãy tìm **đối xứng (symmetry)**. Đối xứng có thể làm một đại lượng không phụ thuộc tọa độ nào đó, giảm số biến hoặc gợi ý một định luật bảo toàn. Ở mức sâu hơn, đối xứng thời gian liên hệ với bảo toàn năng lượng, đối xứng tịnh tiến không gian với bảo toàn động lượng và đối xứng quay với bảo toàn mômen động lượng.

## 3. Viết rõ giả thiết và miền hiệu lực

Mọi mô hình đều có **miền hiệu lực (domain of validity)**. Cơ học Newton rất tốt khi vận tốc nhỏ so với `c` và hiệu ứng lượng tử không đáng kể. Khí lý tưởng phù hợp khi tương tác phân tử đủ yếu. Quang hình học phù hợp khi bước sóng nhỏ hơn nhiều kích thước đặc trưng. Mô hình liên tục phù hợp khi thang quan sát lớn hơn thang vi mô.

Do đó, hãy viết rõ những giả thiết như bỏ qua lực cản không khí, dây không dãn, vật là chất điểm, trường đều, quá trình gần tĩnh (quasi-static), môi trường tuyến tính hoặc nhiệt độ không đổi. Giả thiết không chỉ làm bài dễ hơn; nó xác định chính xác bài toán đang được giải.

## 4. Chọn định luật chi phối

Sau khi có mô hình, hãy hỏi cơ chế nào quyết định hành vi. Với động lực học có thể dùng `F=ma`; với hệ đủ cô lập có thể dùng bảo toàn động lượng; với quá trình không tản mát có thể dùng bảo toàn cơ năng; với mạch điện dùng Kirchhoff; với trường điện từ dùng Maxwell; với lượng tử dùng Schrödinger.

Khi có thể, định luật bảo toàn (conservation law) thường là lựa chọn mạnh vì nó bỏ qua nhiều chi tiết trung gian. Trong va chạm, nếu chỉ cần trạng thái trước và sau, ta không nhất thiết phải biết lực tiếp xúc biến thiên từng microsecond.

## 5. Phân tích thứ nguyên trước khi thế số

Phân tích thứ nguyên (dimensional analysis) là một bộ lọc lỗi rất hiệu quả. Hai vế của một phương trình vật lý phải có cùng thứ nguyên. Nếu kết quả được gọi là vận tốc nhưng có đơn vị `m²/s`, lời giải chắc chắn có vấn đề.

Phân tích thứ nguyên còn dự đoán dạng nghiệm. Chu kỳ con lắc đơn ở góc nhỏ phụ thuộc chiều dài `L` và gia tốc `g`; tổ hợp có thứ nguyên thời gian phải tỉ lệ với

```math
\sqrt{\frac{L}{g}}.
```

Hệ số `2\pi` chỉ xuất hiện sau khi giải chi tiết.

Ở bài nâng cao, các tham số vô thứ nguyên (dimensionless parameters) như số Reynolds, số Mach hay số Knudsen thường cho biết chế độ vật lý quan trọng hơn bản thân giá trị có đơn vị.

## 6. Ước lượng bậc độ lớn

Trước khi tính chính xác, hãy ước lượng bậc độ lớn (order of magnitude). Nếu bài toán ô tô cho kết quả `10^6 m/s`, vấn đề không nằm ở vài chữ số thập phân mà ở mô hình hoặc phép tính.

Ước lượng Fermi chia một câu hỏi lớn thành nhiều yếu tố có thể ước lượng. Đây là kỹ năng đặc biệt hữu ích khi kiểm tra kết quả mô phỏng, dữ liệu cảm biến hoặc đầu ra của phần mềm.

## 7. Giải bằng ký hiệu trước, thế số sau

Giữ biến dưới dạng ký hiệu càng lâu càng tốt. Công thức

```math
v=\sqrt{2gh}
```

cho thấy ngay vận tốc tăng theo căn bậc hai của độ cao và không phụ thuộc khối lượng trong mô hình rơi tự do lý tưởng. Nếu thế số quá sớm, cấu trúc này dễ bị che bởi phép tính số học.

Nghiệm ký hiệu cũng giúp kiểm tra **trường hợp giới hạn (limiting case)**. Khi ma sát tiến về không, nghiệm có trở về trường hợp không ma sát không? Khi `v/c→0`, biểu thức tương đối tính có trở về cơ học Newton không? Khi nhiệt độ rất cao, phân bố lượng tử có tiến gần giới hạn cổ điển không?

## 8. Phân biệt đẳng thức và xấp xỉ

Dấu `≈` mang thông tin vật lý quan trọng. Xấp xỉ góc nhỏ

```math
\sin\theta\approx\theta
```

không phải đẳng thức cho mọi `\theta`. Khai triển Taylor, tuyến tính hóa (linearization), lý thuyết nhiễu loạn (perturbation theory) và xấp xỉ liên tục đều bỏ bớt chi tiết để lấy mô hình dễ xử lý hơn.

Khi dùng xấp xỉ, luôn hỏi: tham số nhỏ là gì, sai số có bậc nào, và điều gì xảy ra khi tham số đó không còn nhỏ.

## 9. Điều kiện đầu và điều kiện biên là một phần của bài toán

Phương trình vi phân thường không xác định nghiệm duy nhất nếu thiếu **điều kiện ban đầu (initial condition)** hoặc **điều kiện biên (boundary condition)**. Cùng phương trình sóng có thể tạo sóng đứng hoặc sóng truyền tùy điều kiện biên. Cùng phương trình Laplace có thể cho các trường điện thế hoàn toàn khác nhau tùy giá trị trên biên.

Trong điện từ, chất lưu, lượng tử và truyền nhiệt, hình học cùng điều kiện biên thường quyết định cấu trúc nghiệm không kém bản thân phương trình.

## 10. Với dữ liệu thực nghiệm, tách mô hình khỏi phép đo

Một giá trị đo không đơn giản là “giá trị thật cộng một sai số”. Cần phân biệt độ bất định ngẫu nhiên, sai số hệ thống, độ phân giải thiết bị, hiệu chuẩn và giả định của mô hình đo.

Nếu khớp dữ liệu bằng `y=ax+b`, đừng chỉ nhìn `R²`. Hãy kiểm tra phần dư (residual), độ bất định của tham số, tương quan giữa các tham số và xem mô hình tuyến tính có hợp lý trên toàn miền dữ liệu hay không.

## 11. Quy trình chuẩn cho một bài mới

Một quy trình có thể tái sử dụng là:

1. Xác định câu hỏi vật lý thật sự cần trả lời.
2. Chọn hệ và ranh giới của hệ.
3. Vẽ hình và chọn hệ tọa độ.
4. Liệt kê biến trạng thái, dữ kiện và đại lượng chưa biết.
5. Viết rõ giả thiết và miền hiệu lực.
6. Tìm đối xứng và các định luật bảo toàn.
7. Chọn phương trình chi phối.
8. Phân tích thứ nguyên và ước lượng bậc độ lớn.
9. Giải bằng ký hiệu trước khi thế số.
10. Kiểm tra dấu, đơn vị, giới hạn đặc biệt và giả thiết sau khi có nghiệm.

Danh sách này là quy trình kiểm tra, không phải khuôn cứng. Với bài đơn giản, nhiều bước diễn ra gần như đồng thời trong đầu.

## 12. Ví dụ: vật trượt trên mặt phẳng nghiêng có ma sát

Xét vật khối lượng `m` trên mặt phẳng nghiêng góc `\theta`. Chọn trục `x` song song mặt phẳng, chiều dương hướng xuống. Phản lực pháp tuyến là

```math
N=mg\cos\theta.
```

Nếu vật đang trượt xuống, ma sát trượt có độ lớn

```math
f_k=\mu_kN=\mu_kmg\cos\theta
```

và hướng lên dốc. Phương trình Newton theo phương dốc là

```math
ma=mg\sin\theta-\mu_kmg\cos\theta.
```

Suy ra

```math
a=g(\sin\theta-\mu_k\cos\theta).
```

Khối lượng triệt tiêu, phù hợp với trực giác rằng trong mô hình ma sát Coulomb đơn giản, gia tốc không phụ thuộc `m`. Khi `\mu_k→0`, kết quả trở về trường hợp không ma sát. Nếu biểu thức trong ngoặc không dương, cần kiểm tra lại giả thiết rằng vật thực sự bắt đầu trượt và xét ma sát tĩnh.

Ví dụ nhỏ này cho thấy lời giải không kết thúc ở phép biến đổi đại số; ta phải đọc lại nghiệm bằng vật lý.

## 13. Kết nối giữa các lĩnh vực

Cùng một cấu trúc xuất hiện nhiều lần. Thế năng trong cơ học nối với điện thế và thế trong phương trình Schrödinger. Mode chuẩn của hệ dao động nối với phonon trong chất rắn và mode của trường điện từ. Phương trình khuếch tán xuất hiện trong truyền nhiệt, chuyển khối và nhiều quá trình ngẫu nhiên. Bài toán trị riêng xuất hiện trong dao động, lượng tử, quang học và phân tích ổn định.

Mục tiêu khi học không phải sở hữu hàng nghìn công thức độc lập. Mục tiêu là nhận ra những cấu trúc lặp lại như trạng thái, đối xứng, bảo toàn, trường, thế, mode, cân bằng, thăng giáng, vận chuyển, thang đo và xấp xỉ.

## 14. Tự kiểm tra sau khi giải

Trước khi chấp nhận kết quả, hãy hỏi: đơn vị có đúng không; dấu có hợp lý không; bậc độ lớn có thực tế không; các giới hạn đặc biệt có đúng không; giả thiết ban đầu có còn phù hợp với nghiệm cuối không; và nếu đây là dữ liệu thực nghiệm, độ bất định có đủ nhỏ để kết luận có ý nghĩa không.

Một lời giải hoàn chỉnh không kết thúc ở con số. Nó kết thúc khi ta giải thích được **vì sao kết quả có dạng đó, điều kiện nào làm nó đúng và điều gì sẽ thay đổi khi mô hình thay đổi**.

## Liên kết kiến thức (Knowledge Connection)

**Đọc cùng:** [Các cấu trúc lặp lại trong Vật lý](00_knowledge_connections.md), [Các ngộ nhận và giới hạn mô hình](04_common_misconceptions_and_model_limits.md).
