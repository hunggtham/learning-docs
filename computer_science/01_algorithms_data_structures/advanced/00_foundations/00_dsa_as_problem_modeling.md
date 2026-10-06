# DSA như một bài toán mô hình hóa

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **DSA như một bài toán mô hình hóa**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Bắt đầu từ câu hỏi cần trả lời** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **Từ yêu cầu nghiệp vụ sang các thao tác nguyên thủy** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng foundations DSA làm owner của problem modeling, rồi nối abstraction, invariant, complexity và implementation.

**Cấu trúc dữ liệu và thuật toán (Data Structures & Algorithms / 자료구조와 알고리즘)**

DSA thường được học bằng tên cấu trúc và tên thuật toán: mảng, danh sách liên kết, bảng băm, cây, đồ thị, BFS, DFS, Dijkstra, quy hoạch động. Cách học này giúp nhận diện mẫu, nhưng chưa đủ để giải bài toán mới. Năng lực cốt lõi hơn là **mô hình hóa (problem modeling)**: biến một vấn đề thực tế thành một mô hình trạng thái có đầu vào, đầu ra, thao tác, bất biến và mô hình chi phí đủ rõ để lựa chọn cách biểu diễn phù hợp.

Một chương trình có thể được nhìn như hai thành phần lớn: **trạng thái (state / 상태)** và **phép biến đổi trạng thái (state transition)**. Cấu trúc dữ liệu quyết định trạng thái được biểu diễn và lưu sẵn như thế nào; thuật toán quyết định chuỗi biến đổi dẫn từ trạng thái ban đầu tới kết quả. Hiệu năng và tính đúng đắn không đến từ một thuật toán “mạnh” đứng riêng lẻ, mà từ mức độ phù hợp giữa mô hình, cách biểu diễn, các thao tác và tải công việc thực tế.

## Bắt đầu từ câu hỏi cần trả lời

Giả sử hệ thống có một triệu tài khoản. Nếu thao tác chính là “tìm tài khoản theo id”, quét tuyến tính là mô hình kém phù hợp. Bảng băm có thể đổi thêm bộ nhớ và chi phí băm để có tra cứu kỳ vọng gần `O(1)`. Nếu cần thêm `floor`, `ceiling`, truy vấn theo khoảng hoặc duyệt theo thứ tự, cây tìm kiếm cân bằng có thể phù hợp hơn vì thứ tự được duy trì như một bất biến.

Do đó, câu hỏi đầu tiên không phải “dùng HashMap hay TreeMap?”, mà là:

```text
Hệ thống phải trả lời những truy vấn nào?
Thao tác nào chiếm đa số?
Dữ liệu có thường xuyên thay đổi không?
Cần kết quả chính xác hay có thể xấp xỉ?
Cần worst-case guarantee hay expected guarantee là đủ?
Độ trễ, thông lượng hay bộ nhớ quan trọng hơn?
Dữ liệu có nằm hoàn toàn trong RAM không?
Có nhiều truy vấn hơn cập nhật, hay ngược lại?
```

Đây là **mô hình tải công việc (workload model)**. Cấu trúc dữ liệu chỉ có ý nghĩa khi đặt trong một tải công việc (workload / 워크로드) cụ thể.

> **Nối mạch:** **Từ yêu cầu nghiệp vụ sang các thao tác nguyên thủy** nối từ **Bắt đầu từ câu hỏi cần trả lời** sang **Kiểu dữ liệu trừu tượng trước cách triển khai**, vì cơ chế trước tạo đầu vào cho bước sau.

## Từ yêu cầu nghiệp vụ sang các thao tác nguyên thủy

Một yêu cầu nghiệp vụ nên được phân rã thành các thao tác cụ thể. Ví dụ hệ thống chat có thể cần:

```text
append(message)
getRecent(k)
findById(id)
delete(id)
searchByTime(from, to)
```

Nếu 95% lưu lượng là `append` và `getRecent`, việc tối ưu cực mạnh cho `delete(id)` nhưng làm hai thao tác chính chậm đi có thể là quyết định sai.

Có thể hình dung chi phí trung bình có trọng số:

\[
E[C] = \sum_i p_i C_i
\]

trong đó `p_i` là tần suất tương đối của thao tác `i`, còn `C_i` là chi phí của nó. Không phải lúc nào cũng cần tính chính xác công thức này; giá trị của nó nằm ở việc buộc ta suy nghĩ theo tỷ lệ sử dụng thay vì theo tên cấu trúc dữ liệu.

> **Nối mạch:** **Từ yêu cầu nghiệp vụ sang các thao tác nguyên thủy** đặt vấn đề; **Kiểu dữ liệu trừu tượng trước cách triển khai** kiểm tra bằng chứng, rồi **Cách biểu diễn chính là quyết định “thông tin nào được lưu sẵn”** mở rộng hệ quả.

## Kiểu dữ liệu trừu tượng trước cách triển khai

**Kiểu dữ liệu trừu tượng (Abstract Data Type – ADT / 추상 자료형)** mô tả ngữ nghĩa và hợp đồng thao tác, chưa quyết định biểu diễn vật lý.

Ngăn xếp (stack / 스택) cam kết LIFO với `push`, `pop`, `peek`. Nó có thể được cài bằng mảng động, danh sách liên kết hoặc vùng nhớ chuyên dụng. hàng đợi (queue / 큐) cam kết FIFO nhưng có thể được cài bằng ring buffer, linked danh sách (list / 목록) hoặc deque.

Tách ADT khỏi hiện thực (implementation / 구현) giúp phân biệt hai câu hỏi:

```text
Cấu trúc phải làm gì?
Cấu trúc sẽ làm điều đó bằng cách nào?
```

Hai hiện thực (implementation / 구현) có thể cùng ngữ nghĩa nhưng rất khác về locality, cấp phát, bộ nhớ, mất hiệu lực của iterator và chi phí theo từng thao tác.

> **Nối mạch:** **Kiểu dữ liệu trừu tượng trước cách triển khai** đặt vấn đề; **Cách biểu diễn chính là quyết định “thông tin nào được lưu sẵn”** kiểm tra bằng chứng, rồi **Chuỗi suy luận từ biểu diễn (representation / 표현) tới độ phức tạp (complexity / 복잡도)** mở rộng hệ quả.

## Cách biểu diễn chính là quyết định “thông tin nào được lưu sẵn”

Mỗi cấu trúc dữ liệu trả một chi phí nào đó để giữ sẵn một loại thông tin, nhờ đó một số truy vấn trở nên rẻ hơn.

Mảng đã sắp xếp giữ toàn bộ thứ tự nên tìm kiếm nhị phân nhanh, nhưng chèn giữa đắt. bảng băm (hash table / 해시 테이블) không giữ thứ tự nhưng giữ ánh xạ từ băm (hash / 해시) tới vị trí tìm kiếm. vùng nhớ động (heap / 힙) chỉ giữ đủ quan hệ thứ tự để phần tử cực trị ở gốc. Segment cây (tree / 트리) lưu sẵn kết quả tổng hợp của nhiều khoảng chuẩn. Trie lưu cấu trúc tiền tố để tránh so sánh lại phần tiền tố chung.

Có thể xem cấu trúc dữ liệu như một dạng **thông tin được vật chất hóa trước (materialized information)**. Ta bỏ công cập nhật và bộ nhớ để tránh tính lại từ đầu trong tương lai.

> **Nối mạch:** **Cách biểu diễn chính là quyết định “thông tin nào được lưu sẵn”** đặt đầu vào cho **Chuỗi suy luận từ biểu diễn (representation / 표현) tới độ phức tạp (complexity / 복잡도)**, rồi **Mô hình trạng thái: thông tin nào thực sự quyết định tương lai?** mở rộng hệ quả.

## Chuỗi suy luận từ biểu diễn (representation / 표현) tới độ phức tạp (complexity / 복잡도)

Một cách suy nghĩ ổn định là:

```text
representation
    ↓
invariant
    ↓
operation
    ↓
complexity
    ↓
trade-off và failure mode
```

Ví dụ nhị phân (binary / 이진) vùng nhớ động (heap / 힙) dùng mảng và hình dạng cây complete. Hình dạng đó bảo đảm chiều cao `O(log n)` và cho phép tính parent/child bằng chỉ số. Heap-order bất biến (invariant / 불변식) làm `peek-min` là `O(1)` và `insert/extract` là `O(log n)`, nhưng không cung cấp tìm kiếm khóa tùy ý nhanh.

Nếu yêu cầu vùng nhớ động (heap / 힙) phải trả lời mọi truy vấn mà Balanced BST hỗ trợ, vấn đề không nằm ở mã (code / 코드) vùng nhớ động (heap / 힙) “chưa đủ tốt”; vấn đề là ta đang dùng sai lớp trừu tượng (abstraction / 추상화).

> **Nối mạch:** **Chuỗi suy luận từ biểu diễn (representation / 표현) tới độ phức tạp (complexity / 복잡도)** đặt đầu vào cho **Mô hình trạng thái: thông tin nào thực sự quyết định tương lai?**, rồi **Quan hệ tương đương giữa các lịch sử** mở rộng hệ quả.

## Mô hình trạng thái: thông tin nào thực sự quyết định tương lai?

Một trạng thái đúng phải chứa đủ thông tin để mọi quyết định tương lai được xác định.

Giả sử đi trên lưới có cửa khóa. Hai lần đứng ở cùng `(row, col)` nhưng có bộ chìa khóa khác nhau không phải cùng một trạng thái, vì các hành động tiếp theo khác nhau. Trạng thái hợp lý có thể là:

```text
(row, col, keyMask)
```

Ngược lại, nếu hai lịch sử khác nhau dẫn tới cùng tập hành động hợp lệ và cùng chi phí tương lai, ta có thể gộp chúng vào một trạng thái.

Đây là một trong những tư tưởng sâu nhất của quy hoạch động:

> Trạng thái không phải là “lịch sử đầy đủ”; trạng thái là lượng thông tin tối thiểu từ lịch sử còn ảnh hưởng tới tương lai.

> **Nối mạch:** **Quan hệ tương đương giữa các lịch sử** nối từ **Mô hình trạng thái: thông tin nào thực sự quyết định tương lai?** sang **Đồ thị thực thể và đồ thị trạng thái**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quan hệ tương đương giữa các lịch sử

Có thể formalize trực giác trên bằng cách coi hai lịch sử `h1` và `h2` là tương đương nếu:

```text
mọi hành động tương lai hợp lệ từ h1 cũng hợp lệ từ h2
và
chi phí/kết quả tối ưu từ h1 và h2 là tương đương theo mục tiêu bài toán
```

Khi đó ta không cần lưu toàn bộ lịch sử; chỉ cần lưu lớp tương đương mà lịch sử thuộc về.

Ví dụ trong bài đường đi có tối đa `K` lần phá tường, trạng thái cần số lần phá đã dùng. Trong bài mà chỉ tổng parity của số bước quan trọng, toàn bộ số bước có thể được nén về một bit chẵn/lẻ.

**Nén trạng thái (state compression)** không phải mẹo bitmask đơn thuần; nó là kết quả của việc nhận ra phần nào của lịch sử không còn ảnh hưởng tới tương lai.

> **Nối mạch:** **Đồ thị thực thể và đồ thị trạng thái** nối từ **Quan hệ tương đương giữa các lịch sử** sang **Sản phẩm (product / 제품) đồ thị (graph / 그래프): ghép nhiều chiều trạng thái**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đồ thị thực thể và đồ thị trạng thái

Không phải mọi đỉnh của đồ thị đều là một “vật thể thật”.

Trong mạng xã hội, đỉnh có thể là người dùng. Trong phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), đỉnh là mô-đun (module / 모듈). Nhưng trong puzzle hoặc routing có ràng buộc, đỉnh có thể là trạng thái tổng hợp.

Ví dụ chuyến bay giới hạn tối đa `K` chặng:

```text
(airport, flightsUsed)
```

Nếu giá vé phụ thuộc thời điểm:

```text
(airport, timeSlot)
```

Nếu còn phụ thuộc loại vé:

```text
(airport, timeSlot, ticketType)
```

Đây là **đồ thị không gian trạng thái (state-space graph)**. Một thuật toán shortest đường dẫn (path / 경로) hoàn hảo trên mô hình trạng thái sai vẫn trả kết quả sai cho bài toán thật.

> **Nối mạch:** **Sản phẩm (product / 제품) đồ thị (graph / 그래프): ghép nhiều chiều trạng thái** nối từ **Đồ thị thực thể và đồ thị trạng thái** sang **Ràng buộc là dữ liệu đầu vào cho việc chọn thuật toán**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sản phẩm (product / 제품) đồ thị (graph / 그래프): ghép nhiều chiều trạng thái

Nhiều bài có thể được xem là tích của hai hoặc nhiều không gian trạng thái.

Ví dụ robot di chuyển trên grid và có hướng nhìn:

```text
(position) × (direction)
```

Một ô `(r,c)` không phải một trạng thái duy nhất; `(r,c,north)` và `(r,c,east)` có thể có tập thao tác khác nhau.

Tư duy **đồ thị tích (product graph)** giúp giải thích vì sao việc “thêm một dimension vào trạng thái (state / 상태)” thường làm số trạng thái tăng theo tích kích thước của các chiều.

Nếu grid có `R*C` ô và `M` trạng thái phụ, tổng trạng thái có thể là `O(R*C*M)`. Điều này phải được tính trước khi chọn BFS/DP.

> **Nối mạch:** **Sản phẩm (product / 제품) đồ thị (graph / 그래프): ghép nhiều chiều trạng thái** đặt vấn đề; **Ràng buộc là dữ liệu đầu vào cho việc chọn thuật toán** kiểm tra bằng chứng, rồi **Trước tiên phải xác định mục tiêu (objective / 목표)** mở rộng hệ quả.

## Ràng buộc là dữ liệu đầu vào cho việc chọn thuật toán

Cùng một câu hỏi nhưng các ràng buộc (constraints / 제약조건들) khác nhau có thể cần thuật toán hoàn toàn khác.

Shortest đường dẫn (path / 경로):

```text
không trọng số            -> BFS
trọng số chỉ 0/1          -> 0–1 BFS
trọng số không âm         -> Dijkstra
DAG                       -> relaxation theo topological order
có trọng số âm            -> cần mô hình/thuật toán khác
negative cycle đạt tới    -> có thể không tồn tại minimum hữu hạn
```

Subset bài toán (problem / 문제) với `n = 20` có thể duyệt `2^n`; với `n ≈ 40–50` có thể nghĩ tới meet-in-the-middle; với `n = 200000` thì exponential tìm kiếm (search / 검색) thường không còn khả thi và phải khai thác thêm cấu trúc.

Các ràng buộc (constraints / 제약조건들) không phải phần phụ cuối đề bài; chúng là một phần của định nghĩa bài toán.

> **Nối mạch:** **Ràng buộc là dữ liệu đầu vào cho việc chọn thuật toán** đặt vấn đề; **Trước tiên phải xác định mục tiêu (objective / 목표)** kiểm tra bằng chứng, rồi **Tách feasibility khỏi tối ưu hóa (optimization / 최적화)** mở rộng hệ quả.

## Trước tiên phải xác định mục tiêu (objective / 목표)

Một mô hình có thể đúng về trạng thái nhưng vẫn sai vì mục tiêu (objective / 목표) không rõ.

Các mục tiêu (objective / 목표) thường gặp:

```text
minimize cost
maximize value
count number of solutions
check existence
return lexicographically smallest solution
return any valid solution
minimize worst-case latency
minimize memory under latency bound
```

Hai bài có cùng trạng thái và chuyển tiếp (transition / 전이) nhưng mục tiêu (objective / 목표) khác nhau có thể cần cấu trúc dữ liệu hoặc thuật toán khác nhau.

Ví dụ “có đường đi hay không” có thể dùng BFS/DFS đơn giản; “đường đi ngắn nhất” cần thêm chỉ số (metric / 지표); “đường đi ngắn nhất rồi nhỏ nhất từ điển” còn cần tie-breaking và thứ tự duyệt phù hợp.

> **Nối mạch:** **Tách feasibility khỏi tối ưu hóa (optimization / 최적화)** nối từ **Trước tiên phải xác định mục tiêu (objective / 목표)** sang **Bài toán tĩnh, động, trực tuyến và ngoại tuyến**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tách feasibility khỏi tối ưu hóa (optimization / 최적화)

Một kỹ thuật mô hình hóa quan trọng là tách:

```text
Có tồn tại lời giải thỏa điều kiện không?
Giữa các lời giải hợp lệ, lời giải nào tối ưu?
```

Nhiều bài “tối ưu hóa trên đáp án” dùng tìm kiếm nhị phân (binary search / 이진 탐색) vì ta có một predicate đơn điệu:

```text
feasible(x) = có thể đạt mục tiêu với ngưỡng x hay không?
```

Khi `feasible(x)` chuyển từ false sang true theo một chiều, bài tối ưu có thể biến thành chuỗi bài kiểm tra khả thi.

Điều này cho thấy thuật toán tìm kiếm không nhất thiết tìm trực tiếp đáp án; đôi khi ta mô hình hóa bài tối ưu thành một quyết định Boolean dễ hơn.

> **Nối mạch:** **Bài toán tĩnh, động, trực tuyến và ngoại tuyến** nối từ **Tách feasibility khỏi tối ưu hóa (optimization / 최적화)** sang **Chính xác (exact / 정확한), approximate và probabilistic**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bài toán tĩnh, động, trực tuyến và ngoại tuyến

Bốn thuộc tính này thay đổi hoàn toàn không gian lựa chọn.

**Tĩnh (static)**: dữ liệu gần như không đổi. Có thể tiền xử lý mạnh, ví dụ Prefix Sum, Sparse bảng (table / 테이블), Suffix Array.

**động (dynamic / 동적)**: cập nhật xảy ra thường xuyên. Cần Fenwick cây (tree / 트리), Segment cây (tree / 트리), balanced cây (tree / 트리) hoặc cấu trúc động khác tùy bài.

**Trực tuyến (online)**: phải trả lời khi dữ liệu tới, không biết tương lai.

**Ngoại tuyến (offline)**: có toàn bộ truy vấn trước và có thể đổi thứ tự xử lý. Khi đó có thể dùng Mo’s thuật toán (algorithm / 알고리즘), sort queries, DSU offline hoặc nhiều kỹ thuật sweep.

Cùng một bộ truy vấn, quyền biết trước tương lai có thể làm bài toán dễ hơn đáng kể.

> **Nối mạch:** **Chính xác (exact / 정확한), approximate và probabilistic** nối từ **Bài toán tĩnh, động, trực tuyến và ngoại tuyến** sang **Deterministic guarantee và expected guarantee**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chính xác (exact / 정확한), approximate và probabilistic

Không phải mọi hệ thống đều cần kết quả chính xác tuyệt đối.

Bloom Filter chấp nhận false positive để giảm bộ nhớ. HyperLogLog ước lượng số phần tử phân biệt với sai số thống kê. Count-Min Sketch ước lượng tần suất với sai số một phía.

Vấn đề thiết kế là **ngân sách sai số (error budget)**:

```text
Sai số nào được phép?
Xác suất sai tối đa là bao nhiêu?
Sai theo hướng nào?
Sai có ảnh hưởng tính an toàn hay tiền bạc không?
```

Một Bloom Filter có thể hợp cho “có lẽ đã thấy URL này”, nhưng không phù hợp nếu false positive có thể từ chối quyền truy cập hợp lệ hoặc làm sai số dư tài chính.

> **Nối mạch:** **Deterministic guarantee và expected guarantee** nối từ **Chính xác (exact / 정확한), approximate và probabilistic** sang **Đầu vào (input / 입력) ngẫu nhiên, đầu vào (input / 입력) trung bình và đầu vào (input / 입력) đối kháng**, vì cơ chế trước tạo đầu vào cho bước sau.

## Deterministic guarantee và expected guarantee

Balanced BST có chiều cao worst-case `O(log n)`. Skip danh sách (list / 목록) có hiệu năng kỳ vọng `O(log n)` dưới mô hình ngẫu nhiên phù hợp. bảng băm (hash table / 해시 테이블) thường có tra cứu kỳ vọng gần `O(1)` nhưng có thể suy giảm trong trường hợp xấu.

Không có loại guarantee “luôn tốt hơn” độc lập bối cảnh. Với hệ thống độ trễ (latency / 지연 시간) cực nhạy hoặc đối mặt đầu vào (input / 입력) đối kháng, worst-case bound có thể quan trọng. Với tải công việc (workload / 워크로드) bình thường, expected hiệu năng (performance / 성능) có thể cho hiện thực (implementation / 구현) đơn giản và nhanh hơn.

> **Nối mạch:** **Đầu vào (input / 입력) ngẫu nhiên, đầu vào (input / 입력) trung bình và đầu vào (input / 입력) đối kháng** nối từ **Deterministic guarantee và expected guarantee** sang **Tiền xử lý là đổi chi phí theo thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đầu vào (input / 입력) ngẫu nhiên, đầu vào (input / 입력) trung bình và đầu vào (input / 입력) đối kháng

Một phân tích “trung bình” chỉ có ý nghĩa nếu phân phối (distribution / 분포) đầu vào được mô tả. Trong thực tế, dữ liệu thường không ngẫu nhiên đều.

ID có thể tăng dần. Timestamps gần như đã sắp xếp. Khóa băm (hash / 해시) có thể do người dùng kiểm soát. Đồ thị mạng xã hội thường có degree phân phối (distribution / 분포) rất lệch.

Do đó nên phân biệt:

```text
average-case theo distribution giả định
expected-case do randomness của thuật toán
worst-case trên mọi input hợp lệ
adversarial-case khi input cố tình phá assumption
```

Hai thuật toán có cùng Big-O trung bình nhưng hành vi khác hẳn dưới dữ liệu có cấu trúc hoặc đầu vào (input / 입력) độc hại.

> **Nối mạch:** **Tiền xử lý là đổi chi phí theo thời gian** nối từ **Đầu vào (input / 입력) ngẫu nhiên, đầu vào (input / 입력) trung bình và đầu vào (input / 입력) đối kháng** sang **Output-sensitive algorithms**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tiền xử lý là đổi chi phí theo thời gian

Giả sử có `Q` truy vấn. Tổng chi phí có thể được mô hình hóa:

\[
C_{total} = C_{bản dựng (build / 빌드)} + Q\cdot C_{truy vấn (query / 쿼리)}
\]

Nếu `Q` rất lớn, tiền xử lý đắt có thể đáng giá. Nếu chỉ một truy vấn, quét tuyến tính có thể tốt hơn xây một chỉ mục phức tạp.

Đây là nguyên lý đứng sau cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스), Prefix Sum, Sparse bảng (table / 테이블), Suffix Array và nhiều cấu trúc tìm kiếm.

> **Nối mạch:** **Output-sensitive algorithms** nối từ **Tiền xử lý là đổi chi phí theo thời gian** sang **Lower bound: có việc không thể tránh khỏi**, vì cơ chế trước tạo đầu vào cho bước sau.

## Output-sensitive algorithms

Không phải mọi độ phức tạp chỉ phụ thuộc kích thước đầu vào (input / 입력). Một số thuật toán phụ thuộc cả kích thước đầu ra (output / 출력).

Ví dụ truy vấn khoảng trong balanced BST có thể có chi phí gần:

\[
O(\log n + k)
\]

với `k` là số phần tử thực sự phải trả ra.

Nếu kết quả chứa một triệu phần tử thì không thuật toán nào có thể “trả” chúng với chi phí thấp hơn việc ít nhất xử lý một triệu đầu ra (output / 출력) theo mô hình thông thường.

Tư duy **output-sensitive** giúp tránh yêu cầu phi thực tế kiểu “trả tất cả kết quả trong O(log n)”.

> **Nối mạch:** **Lower bound: có việc không thể tránh khỏi** nối từ **Output-sensitive algorithms** sang **Reduction: biến bài toán lạ thành bài toán đã hiểu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lower bound: có việc không thể tránh khỏi

Trước khi cố tối ưu, nên hỏi liệu tồn tại cận dưới tự nhiên nào không.

Nếu cần đọc toàn bộ đầu vào (input / 입력) để biết có phần tử âm hay không, chi phí `Ω(n)` là không tránh khỏi trong mô hình truy cập thông thường. Comparison sort cần phân biệt `n!` thứ tự có thể có nên có cận dưới `Ω(n log n)` trong mô hình chỉ dùng so sánh.

Lower bound giúp phân biệt hai tình huống:

```text
implementation chưa tốt
vs
mô hình bài toán tự nó đòi lượng công việc đó
```

> **Nối mạch:** **Reduction: biến bài toán lạ thành bài toán đã hiểu** nối từ **Lower bound: có việc không thể tránh khỏi** sang **Từ miền bài toán sang miền khóa**, vì cơ chế trước tạo đầu vào cho bước sau.

## Reduction: biến bài toán lạ thành bài toán đã hiểu

Một kỹ năng mô hình hóa mạnh là **quy giảm (reduction)**: biến một bài toán thành bài khác sao cho lời giải của bài mới cho lời giải của bài cũ.

Ví dụ:

```text
subtree query -> Euler Tour -> range query
LCA -> Euler Tour/RMQ hoặc Binary Lifting
minimum spanning connectivity -> sort edges + DSU
path with state constraints -> state-space shortest path
interval overlap -> sweep line
```

Reduction giúp tái sử dụng cấu trúc dữ liệu và chứng minh đã biết.

Điểm quan trọng là phải chứng minh ánh xạ (mapping / 매핑) bảo toàn ngữ nghĩa. Nếu quá trình biến đổi làm mất một ràng buộc, thuật toán mới có thể giải một bài khác với bài gốc.

> **Nối mạch:** **Từ miền bài toán sang miền khóa** nối từ **Reduction: biến bài toán lạ thành bài toán đã hiểu** sang **Mô hình dữ liệu thưa và dày đặc**, vì cơ chế trước tạo đầu vào cho bước sau.

## Từ miền bài toán sang miền khóa

Nhiều lựa chọn cấu trúc phụ thuộc trực tiếp miền khóa.

Nếu khóa là số nguyên dày đặc `0..n-1`, một mảng có thể thay HashMap. Nếu khóa là chuỗi có prefix ngữ nghĩa (semantics / 의미론), Trie có thể phù hợp. Nếu khóa có thứ tự toàn phần và cần predecessor/successor, ordered cây (tree / 트리) phù hợp. Nếu khóa là tập con nhỏ, bitmask có thể biến cả trạng thái (state / 상태) thành một số nguyên.

Câu hỏi “khóa trông như thế nào?” thường quan trọng ngang “có bao nhiêu phần tử?”.

> **Nối mạch:** **Từ miền bài toán sang miền khóa** đặt vấn đề; **Mô hình dữ liệu thưa và dày đặc** kiểm tra bằng chứng, rồi **Dominance: loại trạng thái chắc chắn không còn hữu ích** mở rộng hệ quả.

## Mô hình dữ liệu thưa và dày đặc

Một ma trận `n x n` có thể lưu trực tiếp nếu phần lớn ô có dữ liệu. Nhưng nếu chỉ có `m << n²` cạnh, adjacency danh sách (list / 목록) hoặc CSR tiết kiệm hơn adjacency ma trận (matrix / 행렬).

Tương tự, DP có thể dùng array nếu trạng thái (state / 상태) không gian (space / 공간) dày đặc và có chỉ số tự nhiên; dùng HashMap nếu phần lớn trạng thái lý thuyết không bao giờ xuất hiện.

**Mật độ trạng thái (state density)** là một tín hiệu để chọn biểu diễn (representation / 표현).

> **Nối mạch:** **Mô hình dữ liệu thưa và dày đặc** đặt vấn đề; **Dominance: loại trạng thái chắc chắn không còn hữu ích** kiểm tra bằng chứng, rồi **Cấu trúc dữ liệu ghép và bất biến liên cấu trúc** mở rộng hệ quả.

## Dominance: loại trạng thái chắc chắn không còn hữu ích

Trong nhiều bài, một trạng thái có thể bị một trạng thái khác **chi phối (dominate)**.

Ví dụ hai trạng thái ở cùng vị trí:

```text
A: cost = 10, fuel = 5
B: cost = 12, fuel = 3
```

Nếu càng ít chi phí (cost / 비용) và càng nhiều fuel luôn tốt hơn, `B` không thể dẫn tới lời giải tốt hơn `A`. Ta có thể bỏ `B`.

Dominance pruning là một dạng nén trạng thái dựa trên quan hệ thứ tự từng phần. Nó xuất hiện trong DP, shortest đường dẫn (path / 경로) nhiều tiêu chí, branch-and-bound và tìm kiếm (search / 검색) trên Pareto frontier.

> **Nối mạch:** **Dominance: loại trạng thái chắc chắn không còn hữu ích** đặt vấn đề; **Cấu trúc dữ liệu ghép và bất biến liên cấu trúc** kiểm tra bằng chứng, rồi **Big-O chỉ là một mô hình chi phí** mở rộng hệ quả.

## Cấu trúc dữ liệu ghép và bất biến liên cấu trúc

Hệ thống thực tế thường ghép nhiều cấu trúc.

LRU bộ nhớ đệm (cache / 캐시) thường dùng băm (hash / 해시) Map + Doubly Linked danh sách (list / 목록). Dijkstra dùng adjacency biểu diễn (representation / 표현) + distance array/map + Priority hàng đợi (queue / 큐). Autocomplete có thể dùng prefix chỉ mục (index / 인덱스) + ranking cấu trúc (structure / 구조).

Khi ghép, ngoài bất biến của từng cấu trúc còn có **bất biến liên cấu trúc (cross-structure invariant)**.

Ví dụ LRU:

```text
mỗi key trong map trỏ đúng node trong list
mỗi node trong list tương ứng đúng một key trong map
head/tail phản ánh recency order
size(map) == size(list)
```

Nhiều bug môi trường vận hành (production / 운영 환경) không phá bất biến của một cấu trúc đơn lẻ mà phá quan hệ giữa hai cấu trúc.

> **Nối mạch:** **Cấu trúc dữ liệu ghép và bất biến liên cấu trúc** đặt vấn đề; **Big-O chỉ là một mô hình chi phí** kiểm tra bằng chứng, rồi **Bộ nhớ cũng cần mô hình thật** mở rộng hệ quả.

## Big-O chỉ là một mô hình chi phí

Hai thuật toán cùng `O(n)` có thể khác đáng kể do bộ nhớ đệm (cache / 캐시), cấp phát, branch prediction, GC hoặc I/O.

Nên suy nghĩ ít nhất ở hai tầng:

```text
mô hình tiệm cận: chi phí tăng thế nào khi input lớn dần
mô hình máy thật: dữ liệu được di chuyển và cấp phát ra sao
```

Trong cơ sở dữ liệu (database / 데이터베이스), page I/O có thể quan trọng hơn số phép so sánh. Trong hệ thống phân tán, một mạng (network / 네트워크) round-trip có thể đắt hơn hàng nghìn phép toán CPU. Trong Java, object-heavy biểu diễn (representation / 표현) có thể làm GC và bộ nhớ đệm (cache / 캐시) trở thành chi phí chính.

> **Nối mạch:** **Bộ nhớ cũng cần mô hình thật** nối từ **Big-O chỉ là một mô hình chi phí** sang **Mutability, quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bộ nhớ cũng cần mô hình thật

Hai cấu trúc cùng `O(n)` không gian (space / 공간) không nhất thiết tiêu tốn bộ nhớ gần nhau.

Mảng thành phần nguyên thủy (primitive / 기본 요소) khá gọn. Linked nodes có pointer/tham chiếu (reference / 참조) và đối tượng (object / 객체) header. bảng băm (hash table / 해시 테이블) cần dung lượng dư theo tải (load / 로드) factor. Trie có thể có rất nhiều nhánh rỗng nếu biểu diễn (representation / 표현) không phù hợp alphabet.

Dung lượng bộ nhớ còn ảnh hưởng tốc độ qua bộ nhớ đệm (cache / 캐시) và paging, vì vậy không gian (space / 공간) độ phức tạp (complexity / 복잡도) không tách rời thời gian (time / 시간) hiệu năng (performance / 성능) trên máy thật.

> **Nối mạch:** **Mutability, quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성)** nối từ **Bộ nhớ cũng cần mô hình thật** sang **Một quy trình mô hình hóa có thể tái sử dụng**, vì owner và lifetime quyết định cách mô hình hóa tiếp theo.

## Mutability, quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성)

Trong C, biểu diễn (representation / 표현) còn phải mô hình hóa ai sở hữu bộ nhớ, ai giải phóng và con trỏ nào chỉ được mượn. Trong Java, `equals/hashCode`, định danh (identity / 식별자) và GC reachability ảnh hưởng ngữ nghĩa (semantics / 의미론). Trong JavaScript, đối tượng (object / 객체) định danh (identity / 식별자), `Map`, `Number` và engine biểu diễn (representation / 표현) tạo thêm ràng buộc.

Tính đồng thời (concurrency / 동시성) bổ sung một chiều khác: cấu trúc đúng trong single-thread chưa chắc đúng khi nhiều luồng cập nhật. Khi đó cần thêm mô hình atomicity, synchronization và visibility. Lock-free cấu trúc (structure / 구조) còn cần lập luận (reasoning / 추론) về ABA, bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và reclamation.

Nói cách khác, “cùng một ADT” không có nghĩa cùng một hiện thực (implementation / 구현) phù hợp cho mọi thời gian chạy (runtime / 런타임) và mô hình đồng thời.

> **Nối mạch:** **Mutability, quyền sở hữu (ownership / 소유권) và tính đồng thời (concurrency / 동시성)** đặt đầu vào cho **Một quy trình mô hình hóa có thể tái sử dụng**, rồi **Những sai lầm tư duy phổ biến** mở rộng hệ quả.

## Một quy trình mô hình hóa có thể tái sử dụng

Khi gặp bài toán mới, có thể đi theo thứ tự sau:

```text
1. Viết chính xác input, output và objective.
2. Ghi rõ constraints và error model.
3. Liệt kê queries, updates và tỷ lệ xuất hiện.
4. Xác định static/dynamic, online/offline, exact/approximate.
5. Xác định state tối thiểu nhưng đủ thông tin cho tương lai.
6. Tìm quan hệ tương đương và dominance để nén state.
7. Chọn invariant giúp loại bỏ công việc lặp lại.
8. Chọn representation hiện thực invariant hiệu quả.
9. Chứng minh thao tác giữ invariant và đúng semantics.
10. Phân tích Big-O, memory footprint và machine-level costs.
11. Kiểm thử bằng oracle nhỏ, adversarial input và invariant validator.
12. Chỉ tối ưu tiếp khi profiling cho thấy nút thắt thật.
```

Đây là quy trình tổng quát hơn việc học thuộc “mẫu A dùng HashMap, mẫu B dùng vùng nhớ động (heap / 힙)”.

> **Nối mạch:** **Một quy trình mô hình hóa có thể tái sử dụng** đặt đầu vào cho **Những sai lầm tư duy phổ biến**, rồi **Mô hình tư duy** mở rộng hệ quả.

## Những sai lầm tư duy phổ biến

“Cấu trúc có Big-O tốt hơn thì luôn tốt hơn” — sai vì tải công việc (workload / 워크로드), locality, bộ nhớ và hệ số hằng khác nhau.

“Có thể chọn thuật toán trước rồi ép bài toán vào” — dễ dẫn tới trạng thái (state / 상태) thiếu thông tin hoặc mô hình (model / 모델) sai.

“`O(1)` nghĩa là chỉ một lệnh” — sai; nó chỉ nói chi phí không tăng theo `n` trong mô hình phân tích.

“Cấu trúc dữ liệu chỉ là bộ chứa (container / 컨테이너)” — sai; nó là bộ chứa (container / 컨테이너) + bất biến (invariant / 불변식) + ngữ nghĩa (semantics / 의미론) + chi phí (cost / 비용) đặc tả hợp đồng (contract / 계약).

“Nếu trạng thái (state / 상태) chứa càng nhiều thông tin thì càng an toàn” — sai; trạng thái (state / 상태) dư thừa có thể làm không gian tìm kiếm tăng theo tích nhiều chiều và biến bài khả thi thành không khả thi.

“Preprocessing luôn tốt” — sai; nó chỉ đáng khi số truy vấn hoặc yêu cầu độ trễ (latency / 지연 시간) biện minh cho chi phí bản dựng (build / 빌드) và bộ nhớ (memory / 메모리).

> **Nối mạch:** **Mô hình tư duy** tổng hợp từ **Những sai lầm tư duy phổ biến**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy

> Cấu trúc dữ liệu là một hợp đồng về **thông tin nào được giữ sẵn và bất biến nào phải luôn đúng**. Thuật toán là một hợp đồng về **trạng thái biến đổi như thế nào**. Mô hình hóa quyết định thông tin nào thực sự cần tồn tại để tương lai được xác định.

Khi gặp một bài DSA mới, hãy hỏi: **trạng thái thật sự là gì, phần nào của lịch sử còn ảnh hưởng tương lai, truy vấn nào phải rẻ, có thể tiền xử lý hay nén trạng thái (state / 상태) không, guarantee nào thật sự cần, và bất biến (invariant / 불변식) nào giúp loại bỏ phần công việc không cần thiết?**

Xem tiếp: [Correctness & Invariants](./01_algorithm_correctness_and_invariants.md), [Complexity Analysis](./02_complexity_analysis.md), [Memory Models](./03_memory_models_c_java_javascript.md), [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md), [Dynamic Programming](../04_algorithmic_paradigms/05_dynamic_programming.md) và [Problem Solving Workflow](../90_connections/02_problem_solving_workflow.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
