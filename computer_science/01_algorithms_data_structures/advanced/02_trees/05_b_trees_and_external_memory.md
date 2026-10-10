# B-Tree, B+cây (tree / 트리) và cấu trúc dữ liệu cho bên ngoài bộ nhớ

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **B-Tree, B+cây (tree / 트리) và cấu trúc dữ liệu cho bên ngoài bộ nhớ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao cây nhị phân không lý tưởng cho disk/page lưu trữ?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **nút như một page-sized tìm kiếm (search / 검색) cấu trúc (structure / 구조)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối B-trees với external memory, block, fanout và I/O, để cấu trúc cây phù hợp storage lớn.

**B-Tree / B+cây (tree / 트리) / B 트리와 외부 메모리 자료구조**

B-Tree xuất hiện khi mô hình chi phí của BST trong RAM không còn phù hợp. Một cây tìm kiếm nhị phân giả định truy cập nút con con trỏ tương đối rẻ; nhưng khi nút nằm trên SSD, HDD, cơ sở dữ liệu page hoặc lưu trữ khối (block / 블록), chi phí lớn thường không phải vài phép so sánh mà là **I/O / 입출력**.

Vì vậy mục tiêu đổi từ “giảm số phép so sánh” sang:

```text
mỗi lần đọc storage block phải mang về nhiều information hữu ích
số tầng của tree phải thật thấp
các node nên khớp page/block size của storage system
```

Đây là ví dụ kinh điển cho một nguyên tắc rộng hơn của DSA: cấu trúc dữ liệu tốt phụ thuộc **mô hình chi phí của hardware và khối lượng công việc**, không chỉ Big-O trên RAM mô hình trừu tượng.

## Vì sao cây nhị phân không lý tưởng cho disk/page lưu trữ?

cây nhị phân có fan-out tối đa 2. Nếu có hàng triệu các khóa, chiều cao vẫn khoảng `log2(n)` dù balanced. Trong RAM, khoảng vài chục con trỏ dereference có thể chấp nhận được. Nhưng nếu mỗi tầng tương ứng một ngẫu nhiên page read, độ trễ (latency / 지연 시간) trở nên rất đắt.

B-tree tăng **hệ số phân nhánh (fan-out / 분기 계수)**. Một nút có thể chứa hàng chục, hàng trăm hoặc hàng nghìn khóa phân cách tùy kích thước trang và độ rộng khóa.

Ví dụ:

```text
[ 10 | 20 | 35 | 48 ]
 /     |     |     |     \
<10 10..20 20..35 35..48 >48
```

Một page read đưa về nhiều separators cùng lúc, cho phép chọn trong rất nhiều các nút con. Nếu effective hệ số phân nhánh là `B`, chiều cao xấp xỉ:

\[
O(\log_B n)
\]

Sự khác biệt giữa `log2(n)` và `log200(n)` cực lớn khi mỗi tầng là một I/O.

Binary tree có thể tạo nhiều pointer chase và page I/O khi lưu trên disk, trong khi một B-tree node gom nhiều key vào một page-sized search structure. Muốn đánh giá đúng, trước hết cần nắm các invariant giữ cây cân bằng.

## nút như một page-sized tìm kiếm (search / 검색) cấu trúc (structure / 구조)

Một B-tree nút thường chứa:

```text
sorted keys
child pointers/page ids
metadata cần thiết
```

Các khóa trong nút được sắp xếp. Có thể dùng tìm kiếm tuyến tính, tìm kiếm nhị phân hoặc cách tìm kiếm thân thiện với SIMD tùy kích thước nút và phần cứng. Ngay cả khi phải thực hiện thêm vài chục phép so sánh trong bộ nhớ, chi phí đó thường vẫn rẻ hơn một lần I/O lưu trữ bổ sung.

Do đó B-tree chủ động “làm nhiều việc trong một nút” để giảm chiều cao.

B-tree giữ node trong khoảng occupancy hợp lệ, các key có thứ tự và mọi leaf ở cùng độ sâu; internal separators phải phân hoạch đúng miền key. Từ các invariant đó, tìm kiếm chỉ cần đi qua một node ở mỗi level.

## B-tree bất biến (invariant / 불변식)

Có nhiều cách định nghĩa theo bậc (order) hoặc bậc tối thiểu (minimum degree), nhưng nguyên tắc cốt lõi giống nhau:

```text
keys trong mỗi node sorted
children partition key space theo separators
mọi leaves ở cùng depth
node không được quá đầy
node không-root không được quá rỗng
```

Nếu minimum degree là `t`, một formulation điển hình cho B-tree là:

```text
mỗi non-root node có ít nhất t-1 keys
mỗi node có nhiều nhất 2t-1 keys
internal node có #children = #keys + 1
```

chính xác convention khác nhau giữa sách và cách triển khai. Khi đọc mã (code / 코드), đừng học thuộc số trước; hãy xác định rõ “max các khóa”, “min các khóa”, “split threshold” mà cách triển khai dùng.

Search binary-search trong từng node rồi đi theo child tương ứng, nên chi phí chủ yếu là số page đọc và một lần tìm trong page. Insert phải giữ các invariant này khi node đầy bằng cách split và đẩy separator lên parent.

## Tìm kiếm (search / 검색)

Tìm kiếm (search / 검색) trong B-tree gồm hai lớp:

```text
1. search key position trong node hiện tại
2. nếu chưa thấy, chọn đúng child interval và đi xuống
```

Pseudo-code:

```text
node = root
while node exists:
    i = first position where key <= keys[i]
    if keys[i] == key:
        return found
    if node is leaf:
        return not found
    node = child[i]
```

Số page accesses là `O(height)`, trong khi phép so sánh count trong page có thể lớn hơn nhưng rẻ hơn nhiều.

Split chia node đầy thành các node hợp lệ và đưa một key phân cách lên level trên, có thể gây split dây chuyền đến root. Chính cơ chế này giữ mọi leaf cùng độ sâu, nên B-tree luôn balanced.

## Insert: tràn số và split

Chèn thường đi xuống nút lá giống như tìm kiếm. Vấn đề là nút lá có thể đã đầy.

Một chiến lược (strategy / 전략) phổ biến là **split full nút con trước khi descend**. Full nút được chia thành hai các nút và khóa phân cách trung vị được đẩy lên nút cha.

Ví dụ conceptual:

```text
[ 10 | 20 | 30 | 40 | 50 ]
             ^ median

split ->

[10 | 20]   30   [40 | 50]
```

Nếu nút cha cũng full, split có thể propagate lên trên. Nếu nút gốc full, nút gốc split và cây tăng chiều cao đúng 1.

Điểm quan trọng là split không phá sorted partition bất biến. Median trở thành separator giữa khoảng bên trái và khoảng bên phải.

Root split có thể tăng chiều cao thêm một level, nhưng không tạo leaf ở độ sâu khác nhau; đó là lý do insert không làm cây lệch. Delete khó hơn vì phải xử lý underflow và tái phân phối hoặc merge node.

## Tại sao B-tree luôn balanced theo độ sâu?

Insert chỉ split các nút; nó không thêm một nút lá sâu hơn riêng lẻ. Khi nút gốc split, toàn bộ cây tăng độ sâu đồng đều vì nút gốc mới nằm trên nút gốc cũ/sibling mới. Do đó mọi các nút lá vẫn cùng độ sâu.

Đây là khác biệt lớn với BST không cân bằng, nơi thứ tự chèn có thể làm một nhánh dài hơn rất nhiều so với các nhánh khác.

Delete có thể mượn key từ sibling qua parent hoặc merge hai node rồi kéo separator xuống; nếu root rỗng, chiều cao giảm. B+tree tách vai trò index và leaf để tối ưu scan, khác với B-tree nơi record có thể nằm ở internal node.

## Xóa khó hơn chèn

Xóa phải tránh tình trạng thiếu phần tử (underflow). Sau khi xóa khóa, nút không phải nút gốc không được có số phần tử thấp hơn mức lấp đầy tối thiểu.

Các thao tác chính là:

```text
borrow/rotate key từ sibling qua parent
merge với sibling khi cả hai đều quá ít keys
replace internal key bằng predecessor/successor rồi delete ở subtree
```

### Borrow từ sibling

Nếu nút con cần đi xuống đang ở minimum occupancy nhưng sibling có dư khóa, nút cha separator và sibling khóa có thể rotate để nút con nhận thêm một khóa.

### Merge

Nếu cả nút con và sibling đều minimum, ta kéo separator từ nút cha xuống và merge hai các nút thành một nút lớn hơn. nút cha mất một khóa và một nút con con trỏ.

Nếu nút gốc cuối cùng không còn khóa và chỉ có một nút con, nút con đó trở thành nút gốc, làm chiều cao giảm 1.

Mô hình tư duy của delete là: **trước khi đi xuống, đảm bảo nút con có đủ “room” để mất một khóa mà không vi phạm lower occupancy bound**.

B+tree giữ record hoặc pointer dữ liệu ở leaves và nối leaves theo thứ tự, còn internal nodes chỉ dẫn đường. Vì vậy equality lookup và range scan có cost profile khác nhau, dù cùng dựa trên tree height.

## B+cây (tree / 트리) khác B-tree ở đâu?

Trong **B+cây (tree / 트리) / B+ 트리**, nội bộ các nút chủ yếu giữ separator các khóa để routing; actual records hoặc row các con trỏ nằm ở các nút lá. các nút lá thường được linked theo thứ tự đã sắp xếp.

Conceptual cấu trúc (structure / 구조):

```text
            [20 | 50]
           /    |    \
      ...      ...      ...
       |        |        |
 leaf <-> leaf <-> leaf <-> leaf
```

Điều này có nhiều lợi ích.

nội bộ các nút nhỏ hơn vì không cần chứa full records, nên fan-out lớn hơn và chiều cao thấp hơn.

quét theo khoảng rất tự nhiên: tìm nút lá đầu tiên qua cây tìm kiếm (search / 검색) rồi quét nút lá links tuần tự.

Đây là lý do B+cây (tree / 트리) đặc biệt phù hợp cơ sở dữ liệu indexes.

Equality lookup thường dừng sau khi tìm một key, trong khi range scan tiếp tục đọc các leaf page liên tiếp; locality của leaves trở thành yếu tố quan trọng. Với table data, clustered và secondary index quyết định pointer phải đi thêm bao nhiêu bước.

## tra cứu theo quan hệ bằng nhau và quét theo khoảng có chi phí khác nhau

Equality truy vấn:

```sql
WHERE id = :id
```

có thể đi nút gốc → nội bộ → nút lá rồi dừng.

truy vấn khoảng (range query):

```sql
WHERE created_at >= :from
  AND created_at < :to
```

thường cần:

```text
1. seek tới leaf đầu bằng tree traversal
2. scan tuần tự các leaf entries tiếp theo
```

chi phí vì thế gần:

```text
seek cost + number of leaf pages scanned
```

Đây là lý do độ chọn lọc của khoảng ảnh hưởng tới kế hoạch truy vấn. Chỉ mục không thể làm một truy vấn trả về 80% bảng trở nên miễn phí; sau khi định vị vị trí bắt đầu, hệ thống vẫn phải đọc rất nhiều bản ghi hoặc trang.

Clustered index đặt thứ tự dữ liệu gần thứ tự key, còn secondary index thường phải truy tới row location; trade-off phụ thuộc workload đọc/ghi. Composite index mở rộng lựa chọn đó bằng lexicographic order của nhiều cột.

## Chỉ mục cụm và chỉ mục phụ

cơ sở dữ liệu engine cụ thể có ngữ nghĩa (semantics / 의미론) khác nhau, nhưng một mental mô hình hữu ích là:

**Clustered chỉ mục (index / 인덱스) / 클러스터형 인덱스** ảnh hưởng cách rows/dữ liệu (data / 데이터) pages được tổ chức theo khóa chính hoặc tương đương.

**Secondary chỉ mục (index / 인덱스) / 보조 인덱스** thường chứa secondary khóa cộng locator tới bản ghi (record / 레코드)/primary khóa.

Một secondary tra cứu có thể cần:

```text
secondary B+Tree lookup
→ lấy row locator / primary key
→ thêm lookup tới clustered data
```

Vì vậy một “chỉ mục (index / 인덱스) hit” không nhất thiết chỉ có một cây traversal.

Composite index dùng thứ tự từ điển: prefix cột đầu có thể được dùng để lọc hoặc range, nhưng điều kiện bỏ qua prefix thường không tận dụng tốt toàn bộ index. Nếu index chứa đủ cột cần trả về, nó trở thành covering index và tránh lookup dữ liệu.

## Composite chỉ mục (index / 인덱스) và thứ tự từ điển

Chỉ mục (index / 인덱스) trên `(a, b, c)` thường sắp theo thứ tự từ điển:

```text
(a1,b1,c1) < (a2,b2,c2)
```

nếu `a1<a2`, hoặc `a1==a2` và `b1<b2`, v.v.

Điều này giải thích **left-prefix hành vi** trong nhiều cơ sở dữ liệu indexes. truy vấn có điều kiện mạnh trên leading columns thường tận dụng contiguous phạm vi (range / 범위) tốt hơn truy vấn chỉ filter column phía sau.

Ví dụ chỉ mục (index / 인덱스) `(country, city, created_at)` tự nhiên hỗ trợ:

```text
country = 'KR'
country = 'KR' AND city = 'Seoul'
country = 'KR' AND city = 'Seoul' AND created_at range
```

Nhưng điều kiện `city = 'Seoul'` một mình không nhất thiết tạo thành một khoảng liên tiếp nhỏ trong thứ tự toàn cục của chỉ mục.

Covering index giảm random lookup và có thể chỉ đọc các leaf pages, nhưng làm index rộng hơn và tốn chi phí ghi. Khi page đầy, insert có thể gây page split và write amplification.

## Covering chỉ mục (index / 인덱스)

Nếu truy vấn chỉ cần các cột đã có đầy đủ trong nút lá của chỉ mục, cơ sở dữ liệu có thể tránh đọc thêm toàn bộ hàng hoặc trang dữ liệu. Đây là ý tưởng của **chỉ mục bao phủ (covering index)**.

Sự đánh đổi (trade-off / 트레이드오프) là chỉ mục (index / 인덱스) rộng hơn:

```text
fan-out giảm
storage tăng
write amplification tăng
cache residency có thể xấu hơn
```

Tối ưu chỉ mục (index / 인덱스) là balancing giữa read đường đi và ghi (write / 쓰기)/lưu trữ chi phí.

Page split tạo thêm page và có thể cập nhật parent, log, sibling links hoặc nhiều bản sao storage; đó là write amplification. Fill factor và occupancy là các nút điều chỉnh giữa khoảng trống dự phòng, fan-out và tần suất split.

## Page split và ghi (write / 쓰기) amplification

Insert vào nút lá full có thể gây split. Split tạo page mới, di chuyển các mục, cập nhật nút cha và có thể cascade.

Trong cơ sở dữ liệu thực, còn có logging, locking/latching, WAL và bộ đệm pool interactions. Vì vậy insert vào B+cây (tree / 트리) không chỉ là vài con trỏ assignments như BST trong RAM.

ngẫu nhiên inserts vào clustered khóa có thể gây split rải rác. Monotonic increasing khóa thường append vào rightmost các nút lá, giảm ngẫu nhiên split mẫu nhưng có thể tạo tranh chấp tài nguyên hotspot trong concurrent khối lượng công việc.

Fill factor thấp dành chỗ cho insert nhưng tăng kích thước index và số page cần đọc; occupancy cao tiết kiệm đọc nhưng dễ split khi workload ghi dồn. Buffer pool có thể làm chi phí thực tế khác xa số page lý thuyết.

## Fill factor và occupancy

Nếu pages luôn được đóng gói 100%, insert tương lai dễ split. Một số các hệ thống cho phép **fill factor / 채움 비율** để chủ động để trống không gian (space / 공간) trong nút lá pages.

Đây là sự đánh đổi:

```text
lower fill factor -> nhiều storage hơn nhưng có room cho future inserts
higher fill factor -> compact hơn nhưng split risk cao hơn
```

Không có một fill factor tối ưu cho mọi khối lượng công việc.

Buffer pool khiến page nóng có thể được phục vụ từ memory, trong khi page lạnh chịu I/O; vì vậy cost model phải tính cache hit, random access và scan bandwidth. Với range lớn, sequential scan đôi khi tốt hơn index scan.

## bộ đệm pool và effective mô hình chi phí

Không phải mọi page truy cập (access / 접근) đều ra disk. cơ sở dữ liệu bộ đệm pool/bộ nhớ đệm có thể giữ nút gốc và upper nội bộ các tầng gần như luôn trong RAM.

Do đó thực tế:

```text
root/internal top levels rất hot
leaf/data pages quyết định nhiều cache misses hơn
```

B+cây (tree / 트리) vẫn tốt vì shallow cấu trúc (structure / 구조) và page tính cục bộ (locality) giúp bộ nhớ đệm hierarchy hiệu quả.

Sequential scan đọc page theo dòng và tận dụng locality, còn index scan thắng khi predicate chọn ít row hoặc hỗ trợ range tốt. Hash index thường tốt cho equality nhưng không cung cấp thứ tự để range scan như B+tree.

## Sequential quét vs chỉ mục (index / 인덱스) quét

Nếu truy vấn cần phần lớn bảng, quét tuần tự có thể tốt hơn dùng chỉ mục rồi đọc ngẫu nhiên rất nhiều hàng.

Đây là một bài học quan trọng: cấu trúc chỉ mục mạnh không có nghĩa bộ tối ưu truy vấn luôn phải dùng chỉ mục.

truy vấn planner so sánh chi phí:

```text
index seek + random/page lookups
vs
sequential scan
```

DSA chỉ cung cấp thành phần nguyên thủy (primitive / 기본 요소); system-level quyết định (decision / 결정) còn phụ thuộc dữ liệu (data / 데이터) phân phối và I/O mẫu.

Hash index đổi equality lấy khả năng range và order, còn B+tree duy trì separator và leaves có thứ tự. Phân tích external-memory complexity tập trung vào số block/page transfer thay vì chỉ đếm phép so sánh CPU.

## chỉ mục băm vs B+cây (tree / 트리)

Băm (hash / 해시) cấu trúc (structure / 구조) mạnh với tra cứu theo quan hệ bằng nhau:

```text
key = X
```

Nhưng cấu trúc đó không giữ thứ tự toàn phần tự nhiên. Vì vậy truy vấn khoảng, duyệt theo thứ tự tiền tố, tìm phần tử liền trước/liền sau, `MIN/MAX` hoặc `ORDER BY` thường phù hợp hơn với B+cây (tree / 트리).

B+cây (tree / 트리) trả thêm `log_B n` điều hướng (navigation / 내비게이션) chi phí để đổi lấy ordered ngữ nghĩa.

Trong external-memory model, một phép I/O block đắt hơn nhiều phép tính trong memory; B-tree giảm số I/O nhờ fan-out lớn. LSM-tree lại gom ghi tuần tự và compaction, nên trade-off đọc/ghi khác B-tree.

## External-memory độ phức tạp (complexity / 복잡도)

Trong **bên ngoài mô hình bộ nhớ (memory model) / 외부 메모리 모델**, ta quan tâm số các lần truyền khối dữ liệu hơn số thành phần nguyên thủy (primitive / 기본 요소) các thao tác.

Nếu khối (block / 블록) chứa `B` các khóa, một cây tìm kiếm có fan-out lớn có thể đạt số I/O gần logarithmic theo cơ sở (base / 기반) `B`.

Sắp xếp, quét, phép nối và xử lý đồ thị cũng có các biến thể cho bộ nhớ ngoài nhằm tối ưu số lần truyền khối dữ liệu. Đây là cách mở rộng Big-O truyền thống sang mô hình gần phần cứng hơn.

B-tree cập nhật in-place và tối ưu point/range lookup ổn định, còn LSM tận dụng sequential writes nhưng phải compaction và có thể đọc nhiều tầng. Cả hai đều cần suy nghĩ về cache, dù một cấu trúc biết rõ block size còn cấu trúc kia cố thích nghi theo hierarchy.

## B-Tree vs LSM cây

Write-heavy lưu trữ engines thường dùng **Log-Structured Merge cây (LSM Tree / 로그 구조 병합 트리)** hoặc hybrid designs.

B+cây (tree / 트리) thường cập nhật pages in-place/logically in-place, thích hợp reads/phạm vi (range / 범위) và balanced mixed khối lượng công việc.

LSM gom các lần ghi thành các cấu trúc tuần tự rồi hợp nhất và nén theo từng tầng. Thiết kế này chấp nhận khuếch đại đọc và chi phí compaction để đạt thông lượng ghi (write throughput) cao.

So sánh mental mô hình:

```text
B+Tree: giữ sorted structure online, update đúng vị trí
LSM: buffer/append writes, rồi merge sorted runs về sau
```

Không có cấu trúc (structure / 구조) “tốt hơn tuyệt đối”; khối lượng công việc quyết định.

Cache-aware design chọn fan-out và layout dựa trên page/cache cụ thể; cache-oblivious design tìm layout hoạt động hợp lý trên nhiều tầng mà không hard-code một kích thước. Khi nhiều thread cùng truy cập, layout tốt vẫn cần protocol khóa hoặc latch đúng.

## Cache-aware và cache-oblivious thinking

B-tree là cache-aware ở mức ta thường thiết kế nút phù hợp page/khối (block / 블록) kích thước (size / 크기) cụ thể.

**Cache-oblivious các thuật toán / 캐시 비인지 알고리즘** cố đạt tính cục bộ tốt qua bố trí/recursive decomposition mà không hard-code khối (block / 블록) kích thước (size / 크기). Ví dụ van Emde Boas bố trí cho cây có thể cải thiện hierarchy tính cục bộ.

Ý tưởng tổng quát: cấu trúc dữ liệu hiệu năng có thể phụ thuộc cách byte được bố trí trên phân cấp bộ nhớ, không chỉ topology lô-gic (logic / 논리).

Concurrent B-tree thường khóa theo node hoặc latch-coupling khi đi xuống, đồng thời phải xử lý split/delete mà không làm reader thấy cấu trúc nửa cập nhật. Giảm kích thước separator bằng prefix/key compression có thể làm giảm I/O nhưng tăng logic giải mã.

## Tính đồng thời (concurrency / 동시성) và ghép khóa chốt

B+cây (tree / 트리) dùng trong cơ sở dữ liệu có xử lý đồng thời phải bảo vệ nút hoặc trang trong quá trình duyệt và tách/gộp. Một nhóm kỹ thuật là ghép khóa chốt (latch coupling/crabbing): giữ chốt ở nút cha trong khi lấy chốt ở nút con, sau đó nhả nút cha khi đã an toàn.

Hiện đại engines có nhiều tối ưu hóa (optimization / 최적화) phức tạp hơn, nhưng khóa insight là balancing thao tác như split không còn thuần cục bộ khi nhiều các luồng cùng modify cây.

Tính đồng thời (concurrency / 동시성) thêm các câu hỏi:

```text
reader thấy state nào trong lúc split?
separator update có atomic không?
lock/latch order có gây deadlock không?
```

Lô-gic (logic / 논리) cây bất biến và tính đồng thời (concurrency / 동시성) bất biến phải cùng đúng.

Prefix compression lưu phần khác biệt giữa các key liền kề, còn key compression có thể rút gọn separator trong internal node; cả hai phải vẫn so sánh được chính xác. Record có độ dài biến thiên thêm bài toán slot directory, overflow và split theo byte thay vì theo số record.

## Prefix compression và khóa compression

nội bộ separator các khóa có thể dài. cơ sở dữ liệu/chỉ mục (index / 인덱스) các cách triển khai đôi khi compress prefixes hoặc store minimal distinguishing separators để tăng fan-out.

Ví dụ nhiều URLs có tiền tố chung lớn; storing full strings trong mọi nội bộ mục lãng phí không gian trang.

Nén dữ liệu làm tăng công việc của CPU nhưng giảm kích thước trang và I/O — đây là một đánh đổi theo mô hình chi phí phần cứng.

Variable-length records khiến occupancy phải đo theo bytes, và một record lớn có thể cần overflow pages hoặc quy tắc split riêng. Những hiểu lầm về B-tree thường bắt đầu khi áp dụng mô hình node cố định một cách máy móc.

## Variable-length records

Nếu các khóa/records variable-length, “nút chứa tối đa K các khóa” không còn fixed đơn giản. Occupancy thường được đo bằng byte, ô directory hoặc free-space bố trí.

Do đó textbook B-tree với fixed number các khóa chỉ là conceptual cốt lõi (core / 핵심); hệ thống thực tế pages còn có ô các mảng, phân mảnh và compaction.

B-tree không làm mọi truy vấn nhanh như nhau, không loại bỏ chi phí ghi, và “balanced” không có nghĩa mọi page đầy như nhau. Kiểm thử implementation phải quan sát invariant, I/O boundary, split/merge và dữ liệu biến độ dài.

## Những hiểu lầm phổ biến

“B-tree là cây nhị phân nâng cấp” là sai; chữ B không nghĩa nhị phân (binary / 이진) và hệ số phân nhánh thường lớn hơn rất nhiều.

“B+cây (tree / 트리) nút lá linked chỉ để tiện cách triển khai” là sai; nút lá chaining trực tiếp hỗ trợ efficient quét theo khoảng.

“Chỉ mục luôn làm truy vấn nhanh hơn” là sai; truy vấn có độ chọn lọc thấp hoặc tải ghi lớn có thể khiến chi phí duy trì chỉ mục không đáng bỏ ra.

“B-tree tìm kiếm (search / 검색) O(log n) nên giống BST” bỏ qua mục tiêu thực sự: cơ sở (base / 기반) của logarithm/fan-out và số I/O mới là phần quan trọng.

“Page split chỉ tốn O(1)” đúng ở sự trừu tượng (abstraction) cục bộ nhưng hệ thống thực tế chi phí còn bao gồm logging, bộ nhớ đệm, locks và possible cascade.

Test nên kiểm tra search/insert/delete, split root, merge underflow, range scan, restart và tính đúng của parent/leaf links. Mô hình tư duy cuối bài sẽ nối các kiểm tra đó với workload external-memory.

## kiểm thử B-tree các cách triển khai

Một bộ xác minh tốt nên kiểm tra sau ngẫu nhiên inserts/deletes:

```text
keys trong node sorted
child count đúng quan hệ với key count
non-root occupancy nằm trong bounds
mọi leaves có cùng depth
mọi child key range khớp separators
search tất cả inserted keys đúng
inorder/leaf scan sorted
```

Xóa là nơi dễ phát sinh lỗi nhất; kiểm thử vi sai ngẫu nhiên với `TreeMap` hoặc mô hình tham chiếu đã sắp xếp rất hữu ích.

Mô hình tư duy của B-tree gồm page-sized nodes, invariant cân bằng, chi phí I/O, layout leaves, write amplification và protocol đồng thời. Các liên kết cuối bài giúp so sánh B-tree với heap, hash index, LSM và các cấu trúc lưu trữ khác.

## Mô hình tư duy

> B-tree/B+cây (tree / 트리) không tối ưu chủ yếu cho số các phép so sánh; chúng tối ưu cho **phân cấp bộ nhớ và I/O**. Một nút được làm rộng để một page read phân biệt nhiều ranges, khiến cây rất thấp. B+cây (tree / 트리) còn tách routing khỏi records và nối các nút lá để quét theo khoảng trở thành truy cập tuần tự.

Khi đánh giá một chỉ mục (index / 인덱스)/lưu trữ cây, hãy hỏi:

```text
Node/page size là bao nhiêu?
Fan-out thực tế là bao nhiêu?
Workload equality hay range?
Read/write ratio thế nào?
Key có monotonic hay random?
Index có cover query không?
Buffer pool giữ được bao nhiêu level?
Page split/merge và write amplification có đáng kể không?
Concurrency cần latch/lock semantics nào?
```

Từ đó B+cây (tree / 트리) trở thành cầu nối (bridge / 브리지) tự nhiên giữa DSA, cơ sở dữ liệu internals, lưu trữ engines và các hệ thống hiệu năng.

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Balanced Search Trees](./02_balanced_search_trees.md), [DSA trong Database & Systems](../90_connections/01_dsa_in_databases_networks_and_systems.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
