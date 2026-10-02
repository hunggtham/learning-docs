# Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ distance đến neighborhood** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Continuity dưới góc nhìn topology** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối topology với continuity, connectivity và invariants, để hình học được đọc qua quan hệ giữ nguyên khi biến dạng.

Hình học Euclid quan tâm distance, angle, length và area. Nhưng nhiều câu hỏi về shape không cần biết chính xác khoảng cách. Một vòng tròn bằng cao su có thể kéo thành ellipse mà không cắt hay dán; về một nghĩa rất sâu, hai đối tượng (object / 객체) đó vẫn có cùng kiểu connectivity. **Topology / 위상수학** nghiên cứu những tính chất được bảo toàn dưới các biến dạng liên tục kiểu kéo, uốn và co giãn, miễn là không xé rách hoặc dán những điểm vốn tách biệt.

Topology hiện đại là một ngành rất rộng. Chương này chỉ xây mô hình tư duy (mental model / 사고 모델) nền tảng để hiểu continuity, neighborhood, connectedness và vì sao các ideas đó xuất hiện trong calculus, đồ thị (graph / 그래프)/dữ liệu (data / 데이터) phân tích (analysis / 분석) và hình học (geometry / 기하학).

## Từ distance đến neighborhood

Trong chỉ số (metric / 지표) không gian (space / 공간), ta có **khoảng cách (Metric / 거리함수)** `d(x,y)`. Từ distance, ta định nghĩa một ball quanh điểm (point / 지점) `x`:

```math
B_r(x)=\{y\mid d(x,y)<r\}.
```

Một **lân cận (Neighborhood / 근방)** là vùng đủ gần quanh một điểm (point / 지점). Calculus đã dùng idea này khi nói `x` tiến tới `a`: ta không cần `x=a`, chỉ cần `x` nằm trong mọi neighborhood đủ nhỏ của `a`.

Topology trừu tượng hóa idea “nearby” mà không bắt buộc có numerical distance. Một topology chỉ định collections nào được xem là **tập mở (Open Set / 열린집합)**, sao cho chúng behave giống neighborhoods: union tùy ý của open sets vẫn open và finite intersection của open sets vẫn open.

Điểm quan trọng không phải học thuộc axioms, mà nhận ra: topology giữ cấu trúc (structure / 구조) tối thiểu cần để nói về continuity và connectivity ngay cả khi không có ruler.

> **Chuyển mạch:** Trong **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Continuity dưới góc nhìn topology** tiếp nhận điểm tựa từ **Từ distance đến neighborhood** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Connectedness: đối tượng (object / 객체) có thể tách thành hai phần rời không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuity dưới góc nhìn topology

Trong calculus, ta học hàm (function / 함수) `f` continuous tại `a` nếu small changes ở đầu vào (input / 입력) gây small changes ở đầu ra (output / 출력). Dạng epsilon-delta là

```math
\forall\varepsilon>0,\exists\delta>0:
|x-a|<\delta\Rightarrow |f(x)-f(a)|<\varepsilon.
```

Topology cho một formulation tổng quát hơn: một hàm (function / 함수) continuous nếu preimage của mọi open set là open. Câu này nghe abstract, nhưng bản chất vẫn là “regions không bị hàm (function / 함수) xé đột ngột”.

Nếu một continuous hàm (function / 함수) biến một connected interval thành đầu ra (output / 출력), đầu ra (output / 출력) ảnh (image / 이미지) cũng connected. Đây là cấu trúc (structure / 구조) đằng sau Intermediate giá trị (value / 값) Theorem. Khi một continuous hàm (function / 함수) đi từ negative giá trị (value / 값) sang positive giá trị (value / 값) trên interval, nó phải đi qua zero; nó không thể teleport qua zero nếu ảnh (image / 이미지) vẫn connected.

> **Chuyển mạch:** Ở chặng này của **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Connectedness: đối tượng (object / 객체) có thể tách thành hai phần rời không?** tiếp nhận điểm tựa từ **Continuity dưới góc nhìn topology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compactness: vô hạn nhưng vẫn kiểm soát được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Connectedness: đối tượng (object / 객체) có thể tách thành hai phần rời không?

Một không gian (space / 공간) **liên thông (Connected / 연결된)** nếu không thể chia nó thành hai open regions không rỗng, không giao nhau mà union lại là toàn không gian (space / 공간). Trực giác: đối tượng (object / 객체) “một mảnh”.

Interval `[0,1]` connected. Hai intervals `[0,1]∪[2,3]` không connected vì có gap giữa chúng.

Trong dữ liệu (data / 데이터) science, clustering thường cố phát hiện các regions có high density được separation bởi low-density gaps. Dù algorithms không nhất thiết dùng topology formal, intuition về components, neighborhoods và connectivity là rất gần.

Đồ thị (graph / 그래프) lý thuyết (theory / 이론) cũng có connected components, nhưng đồ thị (graph / 그래프) connectivity là discrete analogue: vertices connected nếu có đường dẫn (path / 경로). Topological connectedness và đồ thị (graph / 그래프) connectivity không giống hệt nhau, nhưng cùng một mô hình tư duy (mental model / 사고 모델) “có thể di chuyển trong cấu trúc (structure / 구조) mà không phải nhảy qua khoảng trống”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Compactness: vô hạn nhưng vẫn kiểm soát được** tiếp nhận điểm tựa từ **Connectedness: đối tượng (object / 객체) có thể tách thành hai phần rời không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Homeomorphism: cùng topology dù hình học (geometry / 기하학) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compactness: vô hạn nhưng vẫn kiểm soát được

Một khái niệm trung tâm khác là **compactness / 콤팩트성**. Trong Euclidean không gian (space / 공간), Heine–Borel theorem nói subset compact iff nó closed và bounded. Vì vậy closed interval `[a,b]` compact, còn `(a,b)` không compact.

Compactness mạnh vì nó biến nhiều statements cục bộ (local / 로컬) thành guarantees toàn cục (global / 전역). Continuous hàm (function / 함수) trên compact set đạt maximum và minimum. Điều này giải thích tại sao tối ưu hóa (optimization / 최적화) trên closed bounded feasible region thường có existence kết quả (result / 결과) tốt hơn tối ưu hóa (optimization / 최적화) trên open/unbounded lĩnh vực (domain / 도메인).

Một chuỗi (sequence / 시퀀스) trong compact set có convergent subsequence nằm lại trong set. Idea này xuất hiện khắp phân tích (analysis / 분석) và numerical mathematics: nếu các approximations không thể “chạy ra vô hạn” và không gian (space / 공간) có compactness thích hợp, ta có cơ hội trích ra convergent hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Homeomorphism: cùng topology dù hình học (geometry / 기하학) khác** tiếp nhận điểm tựa từ **Compactness: vô hạn nhưng vẫn kiểm soát được** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ranh giới (boundary / 경계), interior và closure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Homeomorphism: cùng topology dù hình học (geometry / 기하학) khác

Hai spaces **homeomorphic / 위상동형** nếu có một continuous bijection với continuous inverse giữa chúng. Homeomorphism nói chúng có cùng topological cấu trúc (structure / 구조).

Circle và ellipse homeomorphic. Một coffee mug có một handle và một torus thường được dùng làm analogy vì mỗi đối tượng (object / 객체) có một “hole” topologically, dù hình học (geometry / 기하학) cụ thể hoàn toàn khác.

Analogy này hữu ích nhưng phải cẩn thận: topology không nói mug và torus giống nhau về distance, curvature, material hay physics. Nó chỉ nói certain connectivity/hole cấu trúc (structure / 구조) có thể được bảo toàn dưới continuous deformation.

> **Chuyển mạch:** Ở chặng này của **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Homeomorphism: cùng topology dù hình học (geometry / 기하학) khác** đã nêu tiêu chí phân biệt, còn **Ranh giới (boundary / 경계), interior và closure** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Topology trong dữ liệu (data / 데이터) và computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới (boundary / 경계), interior và closure

Với set `A`, **interior / 내부** gồm các points có neighborhood hoàn toàn nằm trong `A`. **ranh giới (boundary / 경계) / 경계** gồm các points mà mọi neighborhood đều chạm cả `A` và phần ngoài `A`. **Closure / 폐포** là `A` cộng các limit points của nó.

Ví dụ với interval `(0,1)` trên real line:

```math
\operatorname{int}(A)=(0,1),
\qquad
\partial A=\{0,1\},
\qquad
\overline A=[0,1].
```

Concept này nối trực tiếp với feasible regions trong tối ưu hóa (optimization / 최적화), ranh giới (boundary / 경계) conditions trong differential equations và quyết định (decision / 결정) boundaries trong machine học tập (learning / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Ranh giới (boundary / 경계), interior và closure** đã nêu tiêu chí phân biệt, còn **Topology trong dữ liệu (data / 데이터) và computation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Topology trong dữ liệu (data / 데이터) và computation

**Topological dữ liệu (data / 데이터) phân tích (analysis / 분석)** nghiên cứu cấu trúc (structure / 구조) như connected components, loops và voids khi dữ liệu (data / 데이터) được nhìn ở nhiều distance scales. Persistent homology là một công cụ nổi tiếng của lĩnh vực này: thay vì tin vào một threshold distance duy nhất, ta theo dõi topological features tồn tại bền vững qua nhiều scales.

Trong robotics, cấu hình (configuration / 구성) không gian (space / 공간) có thể chứa obstacles; đường dẫn (path / 경로) planning trở thành câu hỏi về connected components và holes. Trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들), topology thường được dùng theo nghĩa mạng (network / 네트워크) topology, không phải topology toán học formal, nhưng idea về adjacency/connectivity vẫn gần nhau.

> **Chuyển mạch:** Trong **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Topology trong dữ liệu (data / 데이터) và computation** nêu điều cần giải thích; **Liên kết kiến thức (knowledge connection / 지식 연결)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Topology nối trực tiếp với limits và continuity: calculus trên real numbers dựa vào neighborhood cấu trúc (structure / 구조) dù textbook phổ thông thường che phần đó bằng absolute giá trị (value / 값). Nó nối với tối ưu hóa (optimization / 최적화) qua compactness và ranh giới (boundary / 경계); với differential equations qua domains và ranh giới (boundary / 경계) conditions; với đồ thị (graph / 그래프) lý thuyết (theory / 이론) qua connectivity; với hình học (geometry / 기하학) qua deformation và invariants.

Nó cũng giúp phân biệt hai loại thông tin. chỉ số (metric / 지표) hình học (geometry / 기하학) hỏi “bao xa, góc bao nhiêu, độ cong thế nào?”. Topology hỏi “có connected không, có ranh giới (boundary / 경계)/hole không, có thể deform liên tục thành nhau không?”. Khi đổi biểu diễn (representation / 표현), biết mình đang giữ loại cấu trúc (structure / 구조) nào là cực kỳ quan trọng.

> **Chuyển mạch:** Ở chặng này của **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> hình học (geometry / 기하학) cần một cây thước; topology trước hết cần khái niệm “ở gần nhau” và “có thể biến đổi liên tục”. Nó bỏ bớt distance để giữ lại connectivity và continuity. Vì vậy topology là ngôn ngữ để nói về shape ở mức cấu trúc (structure / 구조), không phải kích thước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhập môn topology: continuity, connectivity và shape không phụ thuộc thước đo**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

“Topology nói donut và coffee mug là một” chỉ đúng trong một equivalence quan hệ (relation / 관계) cụ thể: homeomorphism. Chúng không giống nhau về hình học (geometry / 기하학) hay vật lý.

Connected không đồng nghĩa path-connected trong mọi topological không gian (space / 공간), dù trong nhiều subsets quen thuộc của Euclidean không gian (space / 공간) hai notions thường đi cùng nhau. Cũng không nên suy từ đồ thị (graph / 그래프) connectivity sang topological connectedness một cách máy móc.

Cuối cùng, open/closed không có nghĩa “cửa mở/cửa đóng” hay “bounded/unbounded”. Một set có thể vừa open vừa closed trong một topology; `R` và empty set là ví dụ cơ bản.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
