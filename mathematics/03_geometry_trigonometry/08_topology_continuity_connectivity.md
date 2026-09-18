# Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo

Hình học Euclid quan tâm distance, angle, length và area. Nhưng nhiều câu hỏi về shape không cần biết chính xác khoảng cách. Một vòng tròn bằng cao su có thể kéo thành ellipse mà không cắt hay dán; về một nghĩa rất sâu, hai object đó vẫn có cùng kiểu connectivity. **Topology / 위상수학** nghiên cứu những tính chất được bảo toàn dưới các biến dạng liên tục kiểu kéo, uốn và co giãn, miễn là không xé rách hoặc dán những điểm vốn tách biệt.

Topology hiện đại là một ngành rất rộng. Chương này chỉ xây mental model nền tảng để hiểu continuity, neighborhood, connectedness và vì sao các ideas đó xuất hiện trong calculus, graph/data analysis và geometry.

## Từ distance đến neighborhood

Trong metric space, ta có **khoảng cách (Metric / 거리함수)** `d(x,y)`. Từ distance, ta định nghĩa một ball quanh point `x`:

```math
B_r(x)=\{y\mid d(x,y)<r\}.
```

Một **lân cận (Neighborhood / 근방)** là vùng đủ gần quanh một point. Calculus đã dùng idea này khi nói `x` tiến tới `a`: ta không cần `x=a`, chỉ cần `x` nằm trong mọi neighborhood đủ nhỏ của `a`.

Topology trừu tượng hóa idea “nearby” mà không bắt buộc có numerical distance. Một topology chỉ định collections nào được xem là **tập mở (Open Set / 열린집합)**, sao cho chúng behave giống neighborhoods: union tùy ý của open sets vẫn open và finite intersection của open sets vẫn open.

Điểm quan trọng không phải học thuộc axioms, mà nhận ra: topology giữ structure tối thiểu cần để nói về continuity và connectivity ngay cả khi không có ruler.

## Continuity dưới góc nhìn topology

Trong calculus, ta học function `f` continuous tại `a` nếu small changes ở input gây small changes ở output. Dạng epsilon-delta là

```math
\forall\varepsilon>0,\exists\delta>0:
|x-a|<\delta\Rightarrow |f(x)-f(a)|<\varepsilon.
```

Topology cho một formulation tổng quát hơn: một function continuous nếu preimage của mọi open set là open. Câu này nghe abstract, nhưng bản chất vẫn là “regions không bị function xé đột ngột”.

Nếu một continuous function biến một connected interval thành output, output image cũng connected. Đây là structure đằng sau Intermediate Value Theorem. Khi một continuous function đi từ negative value sang positive value trên interval, nó phải đi qua zero; nó không thể teleport qua zero nếu image vẫn connected.

## Connectedness: object có thể tách thành hai phần rời không?

Một space **liên thông (Connected / 연결된)** nếu không thể chia nó thành hai open regions không rỗng, không giao nhau mà union lại là toàn space. Trực giác: object “một mảnh”.

Interval `[0,1]` connected. Hai intervals `[0,1]∪[2,3]` không connected vì có gap giữa chúng.

Trong data science, clustering thường cố phát hiện các regions có high density được separation bởi low-density gaps. Dù algorithms không nhất thiết dùng topology formal, intuition về components, neighborhoods và connectivity là rất gần.

Graph theory cũng có connected components, nhưng graph connectivity là discrete analogue: vertices connected nếu có path. Topological connectedness và graph connectivity không giống hệt nhau, nhưng cùng một mental model “có thể di chuyển trong structure mà không phải nhảy qua khoảng trống”.

## Compactness: vô hạn nhưng vẫn kiểm soát được

Một khái niệm trung tâm khác là **compactness / 콤팩트성**. Trong Euclidean space, Heine–Borel theorem nói subset compact iff nó closed và bounded. Vì vậy closed interval `[a,b]` compact, còn `(a,b)` không compact.

Compactness mạnh vì nó biến nhiều statements local thành guarantees global. Continuous function trên compact set đạt maximum và minimum. Điều này giải thích tại sao optimization trên closed bounded feasible region thường có existence result tốt hơn optimization trên open/unbounded domain.

Một sequence trong compact set có convergent subsequence nằm lại trong set. Idea này xuất hiện khắp analysis và numerical mathematics: nếu các approximations không thể “chạy ra vô hạn” và space có compactness thích hợp, ta có cơ hội trích ra convergent behavior.

## Homeomorphism: cùng topology dù geometry khác

Hai spaces **homeomorphic / 위상동형** nếu có một continuous bijection với continuous inverse giữa chúng. Homeomorphism nói chúng có cùng topological structure.

Circle và ellipse homeomorphic. Một coffee mug có một handle và một torus thường được dùng làm analogy vì mỗi object có một “hole” topologically, dù geometry cụ thể hoàn toàn khác.

Analogy này hữu ích nhưng phải cẩn thận: topology không nói mug và torus giống nhau về distance, curvature, material hay physics. Nó chỉ nói certain connectivity/hole structure có thể được bảo toàn dưới continuous deformation.

## Boundary, interior và closure

Với set `A`, **interior / 내부** gồm các points có neighborhood hoàn toàn nằm trong `A`. **Boundary / 경계** gồm các points mà mọi neighborhood đều chạm cả `A` và phần ngoài `A`. **Closure / 폐포** là `A` cộng các limit points của nó.

Ví dụ với interval `(0,1)` trên real line:

```math
\operatorname{int}(A)=(0,1),
\qquad
\partial A=\{0,1\},
\qquad
\overline A=[0,1].
```

Concept này nối trực tiếp với feasible regions trong optimization, boundary conditions trong differential equations và decision boundaries trong machine learning.

## Topology trong data và computation

**Topological Data Analysis (TDA / 위상 데이터 분석)** nghiên cứu structure như connected components, loops và voids khi data được nhìn ở nhiều distance scales. Persistent homology là một công cụ nổi tiếng của lĩnh vực này: thay vì tin vào một threshold distance duy nhất, ta theo dõi topological features tồn tại bền vững qua nhiều scales.

Trong robotics, configuration space có thể chứa obstacles; path planning trở thành câu hỏi về connected components và holes. Trong distributed systems, topology thường được dùng theo nghĩa network topology, không phải topology toán học formal, nhưng idea về adjacency/connectivity vẫn gần nhau.

## Knowledge Connection

Topology nối trực tiếp với limits và continuity: calculus trên real numbers dựa vào neighborhood structure dù textbook phổ thông thường che phần đó bằng absolute value. Nó nối với optimization qua compactness và boundary; với differential equations qua domains và boundary conditions; với graph theory qua connectivity; với geometry qua deformation và invariants.

Nó cũng giúp phân biệt hai loại thông tin. Metric geometry hỏi “bao xa, góc bao nhiêu, độ cong thế nào?”. Topology hỏi “có connected không, có boundary/hole không, có thể deform liên tục thành nhau không?”. Khi đổi representation, biết mình đang giữ loại structure nào là cực kỳ quan trọng.

## Mental Model

> Geometry cần một cây thước; topology trước hết cần khái niệm “ở gần nhau” và “có thể biến đổi liên tục”. Nó bỏ bớt distance để giữ lại connectivity và continuity. Vì vậy topology là ngôn ngữ để nói về shape ở mức structure, không phải kích thước.

## Common Misconceptions

“Topology nói donut và coffee mug là một” chỉ đúng trong một equivalence relation cụ thể: homeomorphism. Chúng không giống nhau về geometry hay vật lý.

Connected không đồng nghĩa path-connected trong mọi topological space, dù trong nhiều subsets quen thuộc của Euclidean space hai notions thường đi cùng nhau. Cũng không nên suy từ graph connectivity sang topological connectedness một cách máy móc.

Cuối cùng, open/closed không có nghĩa “cửa mở/cửa đóng” hay “bounded/unbounded”. Một set có thể vừa open vừa closed trong một topology; `R` và empty set là ví dụ cơ bản.
