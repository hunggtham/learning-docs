# Đối xứng, bảo toàn, xấp xỉ và thang đo

Các chủ đề trong chương này trả lời một câu hỏi chung: **trong một hệ phức tạp, điều gì thực sự quan trọng và điều gì có thể bỏ qua?** Đối xứng giúp tìm cấu trúc không đổi, định luật bảo toàn giới hạn những gì hệ có thể làm, số vô thứ nguyên xác định chế độ vật lý, còn tư duy theo thang đo giúp chọn lý thuyết thích hợp.

## Đối xứng là gì?

Đối xứng (symmetry / 대칭성) nghĩa là ta thực hiện một phép biến đổi lên cách mô tả hệ nhưng các định luật chi phối vẫn giữ nguyên dạng. Ví dụ, nếu cùng một thí nghiệm cơ học được thực hiện hôm nay hay ngày mai trong cùng điều kiện mà định luật không đổi, ta nói lý thuyết có đối xứng tịnh tiến theo thời gian.

Đối xứng không chỉ là hình dạng đẹp như hình tròn hay hình cầu. Trong Vật lý, nó là một phát biểu về **tính bất biến (invariance)** của quy luật dưới một phép biến đổi.

## Định lý Noether: từ đối xứng đến bảo toàn

Định lý Noether thiết lập một liên hệ sâu giữa đối xứng liên tục và đại lượng bảo toàn. Nếu các định luật không thay đổi khi tịnh tiến thời gian, năng lượng được bảo toàn. Nếu chúng không thay đổi khi tịnh tiến toàn bộ hệ trong không gian, động lượng tuyến tính được bảo toàn. Nếu chúng không thay đổi khi quay hệ, mômen động lượng được bảo toàn.

Có thể tóm tắt cấu trúc này như sau:

```text
đối xứng tịnh tiến theo thời gian → bảo toàn năng lượng
đối xứng tịnh tiến trong không gian → bảo toàn động lượng
đối xứng quay → bảo toàn mômen động lượng
```

Điều này thay đổi cách nhìn các định luật bảo toàn. Chúng không phải ba mẹo giải bài tình cờ mà phản ánh những tính bất biến của không-thời gian.

Trong vật lý hạt, các đối xứng chuẩn (gauge symmetries) còn đóng vai trò tổ chức cấu trúc của các trường và tương tác. Tuy nhiên khái niệm đối xứng chuẩn tinh tế hơn đối xứng hình học thông thường và nên được học cùng lý thuyết trường lượng tử.

## Bảo toàn phụ thuộc vào cách chọn hệ

Một đại lượng chỉ được bảo toàn khi các điều kiện thích hợp được thỏa mãn. Động lượng của một vật riêng lẻ có thể thay đổi do ngoại lực, trong khi tổng động lượng của hệ lớn hơn gồm các vật tương tác có thể được bảo toàn.

Vì vậy trước khi dùng một định luật bảo toàn, cần hỏi: ranh giới hệ nằm ở đâu, có dòng đại lượng nào đi qua biên không, và có nguồn hoặc tác động bên ngoài nào không.

Đây là lý do tư duy về **hệ (system)** và **ranh giới (boundary)** quan trọng hơn việc ghi nhớ một câu như “động lượng luôn bảo toàn”.

## Xấp xỉ là một phần của Vật lý

Một mô hình vật lý thực tế thường được xây qua chuỗi

```text
hệ thực
→ chọn hệ con cần nghiên cứu
→ xác định hiệu ứng chi phối
→ tìm tham số nhỏ
→ bỏ các hạng bậc cao
→ giải mô hình gần đúng
→ ước lượng sai số và miền áp dụng
```

Ví dụ,

```math
\sin\theta\approx\theta
```

chỉ khi `|\theta|\ll1` rad. Trong thuyết tương đối,

```math
\gamma\approx1+\frac12\frac{v^2}{c^2}
```

chỉ hữu ích khi `v\ll c`.

Khí lý tưởng cũng là một xấp xỉ. Nó hoạt động tốt khi mật độ và tương tác giữa các phân tử nằm trong miền mà thể tích riêng cùng lực tương tác có thể được bỏ qua ở mức chính xác mong muốn.

Khả năng dùng xấp xỉ đúng chỗ là dấu hiệu của hiểu biết sâu. Câu hỏi quan trọng không phải “xấp xỉ có sai không?”—mọi xấp xỉ đều bỏ bớt thứ gì đó—mà là “sai số nhỏ đến đâu và khi nào phần bị bỏ qua trở nên quan trọng?”.

## Tham số nhỏ và bậc của sai số

Một xấp xỉ tốt thường có một tham số vô thứ nguyên nhỏ `\epsilon`. Nếu

```math
f(\epsilon)=f_0+f_1\epsilon+f_2\epsilon^2+\cdots,
```

thì bỏ các hạng từ `\epsilon^2` trở lên có thể hợp lý khi `|\epsilon|\ll1` và các hệ số không tăng bất thường.

Cách viết này giúp định lượng mức tin cậy. Ta không chỉ nói “vận tốc nhỏ” mà nói `v/c\ll1`; không chỉ nói “góc nhỏ” mà nói `|\theta|\ll1` rad. Việc biến một nhận xét định tính thành một tỉ số vô thứ nguyên là một kỹ năng cốt lõi của mô hình hóa.

## Thang đo và lý thuyết hiệu dụng

Ta không mô phỏng một điện thoại thông minh trực tiếp từ quark và gluon. Không phải vì Mô hình Chuẩn sai mà vì mô tả đó chứa quá nhiều chi tiết vi mô không liên quan trực tiếp tới câu hỏi ở cấp thiết bị.

Một chuỗi thang có thể hình dung như sau:

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
linh kiện
↓
mạch điện
↓
máy tính và phần mềm
```

Mỗi tầng dùng các bậc tự do hiệu dụng (effective degrees of freedom) riêng. Chi tiết của tầng thấp hơn được nén thành các tham số như khối lượng, điện tích, hằng số điện môi, điện trở, điện áp ngưỡng hoặc hệ số truyền nhiệt.

Đây là một ví dụ của lý thuyết hiệu dụng (effective theory): mô tả chỉ giữ những biến và tương tác quan trọng ở thang đang xét. Một mô hình có thể rất chính xác trong miền của nó dù không mô tả chi tiết cơ bản nhất của tự nhiên.

## Liên hệ với trừu tượng hóa trong kỹ nghệ phần mềm

Cách tổ chức theo tầng có nét tương đồng với trừu tượng hóa (abstraction) trong phần mềm. Một API không cần phơi bày cách transistor chuyển mạch, nhưng giới hạn phần cứng vẫn xuất hiện ở tầng cao dưới dạng độ trễ, băng thông, nhiệt và năng lượng.

Sự tương đồng này hữu ích để hình dung, nhưng không nên hiểu rằng một tầng vật lý chỉ là một API theo nghĩa đen. Trong Vật lý, việc chuyển giữa các thang còn liên quan tới thống kê, hiện tượng nổi lên và các tham số hiệu dụng được xác định từ lý thuyết hoặc thực nghiệm.

## Các số vô thứ nguyên xác định chế độ vật lý

Một số vô thứ nguyên so sánh hai cơ chế cạnh tranh mà không phụ thuộc hệ đơn vị. Ví dụ số Reynolds

```math
Re=\frac{\rho vL}{\mu}
```

so sánh ảnh hưởng của quán tính với độ nhớt trong dòng chất lưu.

Số Mach

```math
Ma=\frac{v}{c_s}
```

so sánh tốc độ dòng với tốc độ âm thanh, còn

```math
\beta=\frac{v}{c}
```

cho biết hiệu ứng tương đối tính có khả năng quan trọng đến mức nào.

Một con cá nhỏ và một tàu lớn có thể có hình dạng tương tự nhưng dòng chảy quanh chúng rất khác nếu số Reynolds khác nhau. Vì vậy trong thí nghiệm mô hình, chỉ thu nhỏ hình học là chưa đủ; cần duy trì các số vô thứ nguyên quan trọng để đạt tương tự động lực học (dynamic similarity).

## Phân tích thứ nguyên và định lý Buckingham Pi

Nếu một hiện tượng phụ thuộc nhiều đại lượng có đơn vị, ta thường có thể tổ hợp chúng thành một số ít nhóm vô thứ nguyên. Định lý Buckingham Pi cung cấp nền tảng toán học cho việc này.

Ví dụ chu kỳ `T` của con lắc đơn ở góc nhỏ phụ thuộc vào chiều dài `L`, gia tốc trọng trường `g` và có thể khối lượng `m`. Phân tích thứ nguyên cho thấy `m` không cần xuất hiện và tổ hợp có đơn vị thời gian là

```math
T\propto\sqrt{\frac{L}{g}}.
```

Phân tích thứ nguyên không xác định được hệ số `2\pi`, nhưng nó loại bỏ rất nhiều dạng công thức không thể đúng trước khi ta giải phương trình đầy đủ.

## Khi nào phải đổi mô hình?

Một mô hình không “hỏng” chỉ vì có một lý thuyết tổng quát hơn tồn tại. Ta cần đổi mô hình khi tham số kiểm soát rời khỏi miền mà xấp xỉ hiện tại đáng tin cậy.

Khi `v/c` không còn nhỏ, cơ học Newton cần được thay bằng tương đối tính. Khi bước sóng de Broglie trở nên so sánh được với kích thước hệ, mô tả cổ điển có thể không đủ. Khi quãng đường tự do trung bình của phân tử không còn rất nhỏ so với kích thước đặc trưng, giả thiết liên tục của chất lưu cần được xem xét lại.

Do đó câu hỏi “lý thuyết nào đúng?” thường nên được thay bằng câu hỏi chính xác hơn: **ở thang và chế độ này, lý thuyết nào giữ đúng các bậc tự do và hiệu ứng cần thiết với độ chính xác mong muốn?**

## Mô hình tư duy (Mental Model)

Đối xứng cho biết điều gì không thay đổi khi ta biến đổi cách mô tả. Bảo toàn cho biết đại lượng nào bị ràng buộc trong quá trình tiến hóa. Xấp xỉ cho phép loại bỏ hiệu ứng nhỏ một cách có kiểm soát. Các số vô thứ nguyên cho biết cơ chế nào đang chi phối. Thang đo quyết định những bậc tự do nào cần xuất hiện trong mô hình.

Khi kết hợp năm ý tưởng này, ta có một nguyên tắc mạnh: **không dùng mô hình phức tạp nhất có thể; dùng mô hình đơn giản nhất vẫn giữ đúng cấu trúc quan trọng của bài toán và biết rõ sai số của nó.**

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Tư duy Vật lý](00_physical_thinking.md), [Ngôn ngữ Toán học](03_mathematical_language.md).

**Liên hệ tiếp:** [Cơ học Lagrange và Hamilton](../01_mechanics/08_analytical_mechanics.md), [Các cấu trúc lặp lại trong Vật lý](../13_connections/00_knowledge_connections.md).
