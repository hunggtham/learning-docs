# Không gian, thời gian, vectơ (vector) và hệ quy chiếu

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Không gian, thời gian, vector và hệ quy chiếu**. Route đi từ coordinates/frames → vectors → position/displacement → velocity/acceleration → frame transformations, để chuyển động được đọc độc lập với cách chọn tọa độ.

## Vì sao phải định nghĩa “ở đâu” trước khi nói về chuyển động?

Chuyển động chỉ có nghĩa khi ta có cách mô tả vị trí và một đối tượng dùng làm mốc. Một người ngồi trên tàu có thể đứng yên đối với ghế nhưng chuyển động với vận tốc hàng trăm km/h so với mặt đất. Vì vậy vị trí và vận tốc không phải thuộc tính tuyệt đối tách khỏi bối cảnh; chúng được xác định trong một hệ quy chiếu (Reference Frame / 기준계, 좌표계).

Trong cơ học cổ điển, một hệ quy chiếu thường gồm một gốc tọa độ, các trục không gian và một cách đo thời gian. Ta có thể gắn trục `x` dọc theo đường, `y` ngang đường, `z` theo phương thẳng đứng.

> **Nối mạch:** Trong **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Tọa độ và vị trí** nối từ **Vì sao phải định nghĩa “ở đâu” trước khi nói về chuyển động?** sang **Độ dời khác quãng đường**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tọa độ và vị trí

Trong một chiều, vị trí có thể biểu diễn bằng số `x`. Trong ba chiều, vị trí cần vectơ:

```math
\vec r = (x,y,z)
```

vectơ vị trí (Position Vector / 위치벡터) không chỉ nói “cách gốc bao xa” mà còn mã hóa hướng.

### vô hướng (Scalar) và vectơ

Đại lượng vô hướng (Scalar / 스칼라) chỉ cần độ lớn: khối lượng, nhiệt độ, năng lượng. Đại lượng vectơ (Vector / 벡터) có độ lớn và hướng: độ dời, vận tốc, gia tốc, lực.

Sự khác nhau này không phải vấn đề ký hiệu. Nếu hai lực `10 N` ngược chiều, tổng bằng `0 N`; nếu chỉ cộng độ lớn ta sẽ nhận `20 N` và sai hoàn toàn.

vectơ thường viết:

```math
\vec A = A_x\hat i + A_y\hat j + A_z\hat k
```

trong đó `\hat i,\hat j,\hat k` là vectơ đơn vị theo ba trục.

Độ lớn:

```math
|\vec A| = \sqrt{A_x^2+A_y^2+A_z^2}
```

Công thức này là định lý Pythagoras mở rộng sang ba chiều. Nó cho thấy hình học Euclid nằm trực tiếp bên trong ngôn ngữ vectơ.

> **Nối mạch:** Ở chặng này của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Độ dời khác quãng đường** nối từ **Tọa độ và vị trí** sang **Cộng vectơ như hợp thành ảnh hưởng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ dời khác quãng đường

Độ dời (Displacement / 변위) là vectơ nối vị trí đầu tới vị trí cuối:

```math
\Delta \vec r = \vec r_2-\vec r_1
```

Quãng đường (Distance Traveled / 이동거리) là tổng chiều dài đường thực tế đã đi.

Nếu đi một vòng 400 m quanh sân vận động và trở lại vị trí ban đầu, quãng đường là 400 m nhưng độ dời bằng không (zero). Khác biệt này sẽ quyết định cách định nghĩa tốc độ và vận tốc.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Cộng vectơ như hợp thành ảnh hưởng** nối từ **Độ dời khác quãng đường** sang **Tích vô hướng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cộng vectơ như hợp thành ảnh hưởng

Nếu đi 3 m về Đông rồi 4 m về Bắc, độ dời tổng không phải 7 m theo một hướng nào đó. Hai chuyển động diễn ra theo hai trục độc lập:

```math
\vec r = 3\hat i + 4\hat j
```

Độ lớn:

```math
|\vec r|=\sqrt{3^2+4^2}=5\,m
```

Trong đồ họa máy tính (Computer Graphics), cùng nguyên lý dùng để dịch chuyển vật thể (object) trong 2D/3D. Trong kỹ thuật robot (robotics), vị trí, vận tốc, lực và mômen (moment) đều được mô tả bằng vectơ hoặc tensor vì hướng là phần không thể tách khỏi đại lượng.

> **Nối mạch:** Trong **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Tích vô hướng** nối từ **Cộng vectơ như hợp thành ảnh hưởng** sang **Tích có hướng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tích vô hướng

Tích vô hướng (Dot Product / 내적) được định nghĩa:

```math
\vec A\cdot\vec B = |\vec A||\vec B|\cos\theta
```

hoặc theo thành phần:

```math
\vec A\cdot\vec B=A_xB_x+A_yB_y+A_zB_z
```

Tại sao cosine xuất hiện? Dot sản phẩm (product / 제품) đo mức một vectơ “nằm theo hướng” của vectơ kia. `|B|cos\theta` chính là projection của `B` lên hướng `A`.

Điều này sẽ xuất hiện tự nhiên trong công:

```math
W=\vec F\cdot\Delta\vec r
```

Chỉ thành phần lực cùng hướng chuyển động mới truyền năng lượng cơ học qua độ dịch chuyển (displacement) đó.

Trong học máy (Machine Learning), cosine similarity dùng cùng hình học để đo hướng tương tự giữa embedding các vectơ (vectors). Đây là một liên hệ (connection) trực tiếp: “hai vectơ gần cùng hướng” có thể nghĩa hai lực gần cùng hướng, hoặc hai embedding biểu diễn ngữ nghĩa gần nhau.

> **Nối mạch:** Ở chặng này của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Tích có hướng** nối từ **Tích vô hướng** sang **Thời gian và sự kiện**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tích có hướng

Tích có hướng (Cross Product / 외적) tạo ra vectơ vuông góc với mặt phẳng chứa hai vectơ:

```math
|\vec A\times\vec B|=|\vec A||\vec B|\sin\theta
```

Nó xuất hiện trong mômen lực:

```math
\vec \tau=\vec r\times\vec F
```

và lực từ:

```math
\vec F=q\vec v\times\vec B
```

Sine xuất hiện vì chỉ thành phần vuông góc mới tạo quay (rotation) hoặc lực từ theo dạng này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Thời gian và sự kiện** nối từ **Tích có hướng** sang **Hệ quy chiếu quán tính**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thời gian và sự kiện

Trong cơ học Newton, thời gian (Time / 시간) được giả định là một tham số tuyệt đối giống nhau cho mọi người quan sát (observer). Một sự kiện có thể mô tả bằng `(t,x,y,z)`.

Thuyết tương đối sẽ thay đổi giả định (assumption / 가정) này: các người quan sát chuyển động tương đối có thể đo khác nhau về khoảng thời gian và độ dài. Tuy nhiên ở vận tốc đời thường, sai khác cực nhỏ nên thời gian Newton là mô hình rất tốt.

> **Nối mạch:** Trong **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Hệ quy chiếu quán tính** nối từ **Thời gian và sự kiện** sang **Đổi hệ tọa độ và bất biến (invariant / 불변식)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hệ quy chiếu quán tính

Hệ quy chiếu quán tính (Inertial Frame / 관성계) là hệ mà vật không chịu tổng lực sẽ chuyển động thẳng đều. Đây là ngữ cảnh (context / 맥락) tự nhiên của định luật Newton.

Một xe đang tăng tốc không phải hệ quy chiếu quán tính (inertial frame) lý tưởng. Người trong xe cảm thấy “bị đẩy lùi” dù không có một vật nào ở phía sau kéo họ. Trong hệ xe, ta phải đưa thêm lực quán tính giả để viết phương trình theo dạng quen thuộc.

> **Nối mạch:** Ở chặng này của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Đổi hệ tọa độ và bất biến (invariant / 불변식)** nối từ **Hệ quy chiếu quán tính** sang **Ví dụ: vận tốc tương đối cổ điển**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đổi hệ tọa độ và bất biến (invariant / 불변식)

Nếu quay hệ trục, các thành phần vectơ thay đổi nhưng độ lớn của vectơ không thay đổi. Đây là ví dụ đơn giản về bất biến (Invariant / 불변량): thứ không phụ thuộc vào cách ta chọn tọa độ.

Vật lý hiện đại tìm kiếm các đại lượng bất biến rất sâu. Trong tương đối hẹp, khoảng không-thời gian là bất biến dù người quan sát khác nhau đo thời gian và khoảng cách riêng lẻ khác nhau. Trong lý thuyết chuẩn (gauge theory), nhiều biểu diễn toán học khác nhau có thể mô tả cùng trạng thái vật lý.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Đổi hệ tọa độ và bất biến (invariant / 불변식)** nêu quy tắc; **Ví dụ: vận tốc tương đối cổ điển** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Ví dụ: vận tốc tương đối cổ điển

Một người đi về phía trước trong tàu với `2 m/s`, tàu đi `20 m/s` so với mặt đất. Trong cơ học Galilei:

```math
v_{person,ground}=v_{person,train}+v_{train,ground}=22\,m/s
```

Quy tắc cộng này hoạt động cực tốt ở vận tốc nhỏ. Nhưng nếu thay tàu bằng ánh sáng, ta không thể cộng như vậy; thuyết tương đối sẽ thay công thức để giữ tốc độ ánh sáng `c` như bất biến.

> **Nối mạch:** Trong **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Ví dụ: vận tốc tương đối cổ điển** nêu quy tắc; **Mô hình tư duy (mental model / 사고 모델)** thử quy tắc trong tình huống, rồi **Những ngộ nhận thường gặp (Common Misconceptions)** mở rộng hệ quả.

## Mô hình tư duy (mental model / 사고 모델)

Tọa độ là nhãn do ta chọn; vectơ là đối tượng hình học không phụ thuộc nhãn đó. Một đại lượng vật lý tốt thường được diễn đạt sao cho khi đổi hệ tọa độ, cách viết có thể đổi nhưng quan hệ vật lý cốt lõi vẫn được bảo toàn.

> **Nối mạch:** Ở chặng này của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, **Những ngộ nhận thường gặp (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Những ngộ nhận thường gặp (Common Misconceptions)

vectơ không phải chỉ là “mảng số”. Mảng số là các thành phần (component / 컴포넌트) của vectơ trong một cơ sở (basis) cụ thể; đổi cơ sở thì thành phần đổi nhưng vectơ hình học không nhất thiết đổi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian, thời gian, vectơ (vector) và hệ quy chiếu**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Liên hệ tiếp:** [Động học](../01_mechanics/00_kinematics.md), [Thuyết tương đối hẹp](../07_relativity/00_special_relativity.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
