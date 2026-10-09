# Nền tảng về cây

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Nền tảng về cây**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Cây có gốc và bất biến n − 1 cạnh** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **Cây là một đối tượng đệ quy** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối tree foundations với node, edge, root, depth và traversal, để mọi biến thể cây dùng cùng từ vựng nền.

**cây (tree / 트리) / 트리**

Cây là một trong những mô hình quan trọng nhất của Khoa học máy tính vì nó biểu diễn **quan hệ phân cấp (hierarchical relationship)**. Hệ thống tệp, DOM, AST, cây danh mục, chỉ mục cơ sở dữ liệu, cấu trúc định tuyến và cây quyết định đều có thể được nhìn dưới góc này.

Điểm cốt lõi không phải hình vẽ “một nút ở trên và nhiều nút ở dưới”, mà là tính đệ quy: mỗi phần con của cây lại có thể được xem như một cây nhỏ hơn. Chính tính chất đó làm cho đệ quy, quy nạp cấu trúc, chia bài toán theo cây con và quy hoạch động trên cây trở nên tự nhiên.

## Cây có gốc và bất biến n − 1 cạnh

Trong một **cây có gốc (rooted tree)**, có một nút được chọn làm gốc. Mỗi nút khác gốc có đúng một nút cha và có thể có nhiều nút con. Cây không chứa chu trình.

Nếu cây có `n` nút thì có đúng `n-1` cạnh. Lý do rất trực tiếp: mỗi nút ngoài gốc cần đúng một cạnh nối nó với cha. Không thể có thêm cạnh mà vẫn giữ đồng thời tính liên thông và không chu trình.

Bất biến này giúp phân biệt cây với đồ thị tổng quát, nơi một đỉnh có thể có nhiều đường quay lại hoặc nhiều quan hệ giống “cha”.

> **Mối nối:** Bất biến `n − 1` cạnh cho ta cấu trúc tối thiểu của cây; mục kế tiếp dùng chính cấu trúc đó để giải thích vì sao mỗi cây con lại là một bài toán cây hoàn chỉnh. Từ đây, độ sâu, chiều cao và kích thước cây con biến cách nhìn đệ quy thành những đại lượng đo được.

## Cây là một đối tượng đệ quy

Có thể định nghĩa:

```text
một cây = nút gốc + 0 hoặc nhiều cây con
```

Với cây nhị phân, mỗi nút có tối đa hai cây con trái/phải. Vì cây con vẫn là cây, một hàm trên cây thường có cấu trúc rất tự nhiên:

```java
int height(TreeNode node) {
    if (node == null) return 0;
    return 1 + Math.max(height(node.left), height(node.right));
}
```

Tính đúng đắn có thể chứng minh bằng **quy nạp cấu trúc (structural induction)**. Cây rỗng là trường hợp cơ sở. Ở bước quy nạp, giả sử kết quả của các cây con đã đúng; ta chỉ cần chứng minh cách kết hợp chúng ở nút hiện tại là đúng.

Đây là mô hình chứng minh lặp lại trong chiều cao, kích thước cây con, tổng cây con, kiểm tra BST và cây (tree / 트리) DP.

> **Mối nối:** Khi cây được xử lý theo các cây con, độ sâu và chiều cao cho biết chi phí nằm ở đâu, còn kích thước cho biết mỗi phần đóng góp bao nhiêu. Các khái niệm full, complete, perfect và balanced tiếp theo đặt những đại lượng ấy vào các bất biến hình dạng cụ thể.

## Độ sâu, chiều cao và kích thước cây con

**độ sâu (depth / 깊이)** của nút thường là số cạnh từ gốc tới nút. **Chiều cao (height)** là độ dài đường đi dài nhất từ nút xuống một lá. **Kích thước cây con (subtree size)** là số nút thuộc cây con có gốc tại nút đó.

Ba đại lượng phục vụ các câu hỏi khác nhau. Độ sâu xuất hiện trong LCA và khoảng cách. Chiều cao quyết định chi phí trường hợp xấu nhất của nhiều cây tìm kiếm. Kích thước cây con hỗ trợ rank, thứ tự (order / 순서) statistics và nhiều kỹ thuật rerooting.

Nếu cây nhị phân có chiều cao `h` với gốc ở độ sâu 0, số nút tối đa là:

\[
2^{h+1}-1
\]

Do đó cây có hình dạng cân bằng có chiều cao cỡ `O(log n)`, còn cây lệch có thể cao `O(n)`. Chính hình dạng cây quyết định nhiều bảo đảm hiệu năng.

> **Mối nối:** Những tên gọi full, complete, perfect và balanced chỉ có ý nghĩa khi gắn với bất biến hình dạng mà thuật toán cần giữ. Vì hình dạng quyết định thứ tự xử lý hiệu quả, phần kế tiếp chuyển sang các kiểu duyệt cây.

## Full, complete, perfect và balanced

Các thuật ngữ này mô tả các bất biến khác nhau.

**Full nhị phân (binary / 이진) cây (tree / 트리)**: mỗi nút có 0 hoặc 2 con.

**Complete nhị phân (binary / 이진) cây (tree / 트리)**: mọi tầng trước tầng cuối đầy đủ và tầng cuối được lấp từ trái sang phải. nhị phân (binary / 이진) vùng nhớ động (heap / 힙) dựa vào tính chất này để biểu diễn bằng mảng.

**Perfect nhị phân (binary / 이진) cây (tree / 트리)**: mọi nút trong có đúng hai con và mọi lá cùng độ sâu.

**Balanced cây (tree / 트리)**: chiều cao được kiểm soát đủ tốt, thường ở mức logarithmic. AVL và Red-Black cây (tree / 트리) dùng các bất biến khác nhau để đạt mục tiêu này.

Không nên học các tên này tách rời mục đích. vùng nhớ động (heap / 힙) cần complete shape; BST cần thứ tự khóa; AVL cần cân bằng chiều cao; B+cây (tree / 트리) cần hệ số phân nhánh lớn và mức lấp đầy phù hợp với trang lưu trữ.

> **Mối nối:** Hình dạng cây cho biết những phụ thuộc nào phải được tôn trọng, còn preorder, inorder, postorder và level-order quy định lúc ta xử lý chúng. Để hiểu vì sao các thứ tự này có thể viết bằng đệ quy, ta cần theo dõi trạng thái mà ngăn xếp lời gọi đang giữ.

## Duyệt cây là chọn thứ tự xử lý phụ thuộc

Ba thứ tự DFS kinh điển của cây nhị phân:

```text
Preorder:  root -> left -> right
Inorder:   left -> root -> right
Postorder: left -> right -> root
```

Preorder phù hợp khi cha phải được xử lý trước con, ví dụ truyền trạng thái từ trên xuống hoặc tuần tự hóa cấu trúc.

Postorder phù hợp khi cha cần kết quả của các con trước, ví dụ tính chiều cao, kích thước cây con, giá trị biểu thức hoặc giải phóng toàn bộ cây.

Inorder đặc biệt quan trọng với BST vì trả khóa theo thứ tự đã sắp xếp.

**Duyệt theo tầng (level-order traversal)** dùng BFS và hàng đợi (queue / 큐). Nó phù hợp với bài toán theo độ sâu, khoảng cách tính theo cạnh hoặc xử lý từng tầng.

> **Mối nối:** Mỗi lời gọi đệ quy lưu lại nút hiện tại và nhánh còn phải quay lại; đó chính là trạng thái ẩn của một phép duyệt. Khi trạng thái này trở nên lớn hoặc cần kiểm soát locality, cách biểu diễn cây trong bộ nhớ trở thành quyết định thiết kế tiếp theo.

## Đệ quy đang lưu trạng thái gì?

Trong inorder đệ quy, khi đi xuống cây con trái, ngăn xếp lời gọi (call stack / 호출 스택) đang nhớ những tổ tiên cần quay lại xử lý. Phiên bản lặp làm trạng thái này tường minh:

```java
Deque<TreeNode> stack = new ArrayDeque<>();
TreeNode cur = root;

while (cur != null || !stack.isEmpty()) {
    while (cur != null) {
        stack.push(cur);
        cur = cur.left;
    }

    cur = stack.pop();
    visit(cur);
    cur = cur.right;
}
```

Đệ quy không phải phép màu; thời gian chạy (runtime / 런타임) chỉ đang quản lý một ngăn xếp (stack / 스택) trạng thái thay cho ta. Hiểu điều này giúp chuyển thuật toán sang dạng lặp khi cây có thể quá sâu.

> **Mối nối:** Cách lưu con trái, con phải và các mảng chỉ mục quyết định chi phí vật lý của trạng thái lô-gic. Nếu thuật toán còn cần đi ngược từ nút lên tổ tiên, câu hỏi tự nhiên tiếp theo là có nên lưu thêm con trỏ cha hay truyền nó qua ngăn xếp.

## Biểu diễn cây trong bộ nhớ

C thường dùng con trỏ:

```c
typedef struct TreeNode {
    int value;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;
```

Java và JavaScript dùng tham chiếu (reference / 참조) được thời gian chạy (runtime / 런타임) quản lý. lô-gic (logic / 논리) topology có thể giống nhau nhưng chi phí vật lý khác nhau.

Một cây gồm hàng triệu đối tượng (object / 객체) rải rác trên vùng nhớ động (heap / 힙) có thể có locality kém hơn cách biểu diễn bằng các mảng `value[]`, `left[]`, `right[]`. Vì vậy cần phân biệt **cấu trúc lô-gic (logic / 논리)** với **bố trí vật lý**.

> **Mối nối:** Con trỏ cha đổi bộ nhớ lấy khả năng đi lên nhanh hơn, nhưng cũng thêm một bất biến phải cập nhật sau mỗi phép biến đổi. Khi chỉ cần truy vấn theo cây con, Euler Tour có thể biến quan hệ phân cấp ấy thành một đoạn liên tục mà không cần con trỏ cha.

## Có cần con trỏ cha không?

Nếu chỉ duyệt từ gốc xuống, parent có thể được truyền qua ngăn xếp (stack / 스택)/recursion. Nếu tải công việc (workload / 워크로드) thường xuyên cần predecessor, successor, đi lên hoặc truy vấn tổ tiên, lưu parent có thể hữu ích.

Đổi lại, mỗi nút tốn thêm bộ nhớ và mọi phép xoay/nối lại phải cập nhật parent đúng. Mỗi siêu dữ liệu (metadata / 메타데이터) mới là một bất biến mới phải duy trì.

> **Mối nối:** Euler Tour giữ nguyên quan hệ cây con nhưng mã hóa nó bằng khoảng thời gian vào-ra của DFS. Trên nền biểu diễn đó, bài toán tổ tiên chung thấp nhất có thể được giải như một truy vấn về đường đi và độ sâu.

## Euler Tour: biến cây con thành đoạn liên tục

Một DFS có thể gán `tin[u]` khi đi vào nút và `tout[u]` sau khi xử lý cây con. Nếu đánh số theo thời điểm vào, các nút của `subtree(u)` nằm liên tục trong thứ tự DFS:

```text
subtree(u) <-> [tin[u], tout[u]]
```

Đây là cầu nối mạnh từ cây sang bài toán truy vấn đoạn.

Ví dụ, nếu cần cập nhật giá trị một nút và truy vấn tổng toàn cây con, ta có thể flatten cây rồi dùng Fenwick cây (tree / 트리) hoặc Segment cây (tree / 트리) trên mảng Euler.

Một vấn đề phân cấp đã được chuyển thành bài toán khoảng mà vẫn giữ nguyên ngữ nghĩa cây con.

> **Mối nối:** LCA trả lời quan hệ giữa hai nút bằng cách khai thác tổ tiên và độ sâu; đó là bước nhìn cây theo đường đi thay vì từng cây con riêng lẻ. Khi mục tiêu là tối ưu một giá trị trên toàn cấu trúc, ta chuyển sang trạng thái DP truyền thông tin từ cây con lên cha.

## Lowest dùng chung (common / 공통) Ancestor

**Tổ tiên chung thấp nhất (Lowest Common Ancestor – LCA / 최소 공통 조상)** của hai nút là tổ tiên chung có độ sâu lớn nhất.

Nếu chỉ có ít truy vấn, có thể đưa hai nút lên theo parent. Với nhiều truy vấn, **nhị phân (binary / 이진) lifting** tiền xử lý:

```text
up[k][v] = tổ tiên của v cách 2^k cạnh
```

Khoảng cách bất kỳ có thể phân rã thành tổng các lũy thừa của 2, nên ta có thể nâng nút theo các bit của độ sâu. Tiền xử lý thường `O(n log n)`, mỗi truy vấn `O(log n)`.

Ý tưởng này cùng họ với Sparse bảng (table / 테이블) và exponentiation by squaring: tiền xử lý các khối kích thước tăng gấp đôi để ghép nhanh một bước lớn.

> **Mối nối:** Tree DP cố định một gốc để tách các cây con thành những phần không giao nhau, nhờ vậy trạng thái có thể được ghép từ dưới lên. Nếu đáp án phải đúng với nhiều gốc khác nhau, rerooting DP sẽ tái sử dụng phần thông tin đã tính thay vì chạy lại toàn bộ.

## Cây (tree / 트리) DP

Khi đã cố định parent, các cây con không giao nhau. Đây là điều kiện lý tưởng cho quy hoạch động.

Ví dụ tập độc lập cực đại trên cây:

```text
dp[u][0] = kết quả tốt nhất trong subtree(u) khi không chọn u
dp[u][1] = kết quả tốt nhất trong subtree(u) khi chọn u
```

Nếu chọn `u`, các con trực tiếp không được chọn. Nếu không chọn `u`, mỗi cây con có thể chọn trạng thái tốt hơn của nó.

Điểm quan trọng là trạng thái DP xuất phát từ **thông tin tối thiểu mà cây con cần biết về phía cha**, không phải từ việc “bài cây thì phải dùng dp[u]”.

> **Mối nối:** Rerooting cho thấy cùng một cấu trúc có thể được nhìn từ nhiều gốc bằng cách cập nhật ảnh hưởng qua một cạnh. Lý do phép truyền này đơn giản trên cây là cây là đồ thị có bất biến mạnh hơn: giữa hai nút chỉ có một đường đi đơn.

## Rerooting DP

Một số bài yêu cầu đáp án khi từng nút lần lượt được xem là gốc. Chạy DFS lại từ mỗi nút tốn `O(n²)`.

Rerooting tái sử dụng kết quả giữa hai gốc kề nhau:

```text
lượt 1: tổng hợp đóng góp từ con lên cha
lượt 2: truyền đóng góp của phần còn lại của cây từ cha xuống con
```

Đây là một ví dụ quan trọng của tư duy “đừng tính lại toàn bộ khi trạng thái mới chỉ khác trạng thái cũ bởi một cạnh”.

> **Mối nối:** Không chu trình và liên thông biến nhiều bài toán đồ thị thành quan hệ duy nhất giữa các nút trên cây. Từ bất biến ấy, khoảng cách trên cây có thể được phân tích bằng độ sâu, LCA hoặc một lần duyệt phù hợp.

## Cây là đồ thị có bất biến mạnh hơn

Mọi cây là đồ thị liên thông không chu trình. Giữa hai nút tồn tại đúng một đường đi đơn giản.

Vì vậy, nhiều bài toán đồ thị trở nên đơn giản hơn trên cây. Nếu đầu vào được bảo đảm là cây và DFS nhận parent, không cần một `visited` set tổng quát; chỉ cần tránh đi ngược lại parent.

Ngược lại, nếu dữ liệu chỉ “trông giống cây” nhưng có thể chứa chu trình hoặc nhiều parent, phải quay lại mô hình đồ thị tổng quát.

> **Mối nối:** Vì đường đi giữa hai nút là duy nhất, khoảng cách có thể cộng từ các đoạn trên đường đó. Cực đại của những khoảng cách này là đường kính, một đại lượng tóm tắt mức “dài” của toàn cây.

## Khoảng cách trên cây

Với cây không trọng số, nếu biết độ sâu và LCA:

\[
dist(u,v)=độ sâu (depth / 깊이)(u)+độ sâu (depth / 깊이)(v)-2\cdot độ sâu (depth / 깊이)(lca(u,v))
\]

Công thức xuất phát từ việc đường đi duy nhất từ `u` tới `v` đi từ `u` lên LCA rồi xuống `v`.

Nếu cạnh có trọng số, thay `depth` bằng tổng trọng số từ gốc tới nút.

> **Mối nối:** Đường kính mô tả hai đầu xa nhất, nhưng không cho biết điểm nào chia tải của cây cân bằng nhất. Centroid trả lời câu hỏi còn lại bằng cách đo kích thước các thành phần sau khi bỏ một nút.

## Đường kính cây

**Đường kính (diameter)** là đường đi dài nhất giữa hai nút. Với cây không trọng số hoặc trọng số không âm phù hợp, một kỹ thuật phổ biến là:

```text
chọn nút bất kỳ s
tìm nút a xa s nhất
từ a tìm nút b xa nhất
đường a-b là một đường kính
```

Một cách khác là DP hậu thứ tự, giữ hai nhánh sâu nhất đi xuống từ mỗi nút và xét tổng của chúng.

Hai cách thể hiện hai góc nhìn khác nhau: đường kính như hai lần tìm điểm cực xa, hoặc như việc ghép hai nhánh tốt nhất qua một nút.

> **Mối nối:** Centroid chia cây theo kích thước các thành phần, còn Heavy-Light Decomposition chia theo độ nặng của nhánh để biến truy vấn đường đi thành vài đoạn. Hai cách chia phục vụ hai kiểu truy vấn khác nhau và không nên đánh đồng.

## Centroid

**Centroid của cây** là nút mà khi loại bỏ nó, mọi thành phần còn lại có kích thước không quá `n/2`. Cây có một hoặc hai centroid.

Centroid quan trọng vì nó tạo điểm chia cân bằng theo kích thước, không phải theo chiều cao. **Centroid decomposition** liên tục chọn centroid rồi phân rã các thành phần, tạo một cây phân rã có chiều cao `O(log n)`.

Kỹ thuật này hữu ích cho truy vấn khoảng cách động trên cây và là ví dụ về việc xây một cấu trúc phụ để thay đổi không gian truy vấn.

> **Mối nối:** Heavy-Light Decomposition tổ chức cây để xử lý truy vấn đường đi hiệu quả, nhưng nút và cạnh vẫn mang ngữ nghĩa miền bài toán. Một ví dụ khác là cây biểu thức, nơi cấu trúc cây trực tiếp mã hóa thứ tự và phụ thuộc của phép tính.

## Heavy-Light Decomposition

Đường đi giữa hai nút không nhất thiết tạo một đoạn liên tục trong Euler thứ tự (order / 순서). **Heavy-Light Decomposition (HLD)** chia các cạnh thành heavy/light để một đường đi bất kỳ được biểu diễn bởi `O(log n)` đoạn liên tục trên các chuỗi (chain / 사슬).

Kết hợp HLD với Segment cây (tree / 트리)/Fenwick cây (tree / 트리) cho phép xử lý nhiều truy vấn/cập nhật trên đường đi.

Trực giác là chọn cho mỗi nút một con “heavy” có subtree lớn nhất. Mỗi lần đi qua cạnh light, kích thước subtree giảm ít nhất khoảng một nửa, nên số lần đổi chuỗi (chain / 사슬) trên một đường bị chặn logarithmic.

> **Mối nối:** Cây biểu thức cho thấy traversal có thể tạo ra các dạng biểu diễn khác nhau của cùng một cấu trúc. Khi cây cần được lưu, truyền hoặc phục hồi qua ranh giới tiến trình, serialization phải giữ đủ thông tin để tái tạo những quan hệ đó.

## Cây và biểu thức

AST và expression cây (tree / 트리) cho thấy traversal tương ứng trực tiếp với thứ tự đánh giá.

Postorder phù hợp để tính biểu thức vì toán hạng con phải được tính trước toán tử cha. Preorder có thể tạo dạng prefix; inorder liên hệ với dạng infix nhưng cần ngoặc để bảo toàn cấu trúc.

Đây là ví dụ cây không chỉ lưu dữ liệu mà còn mã hóa thứ tự phụ thuộc của phép tính.

> **Mối nối:** Serialization biến topology và dữ liệu của cây thành một dạng có thể di chuyển, nhưng mọi phép biến đổi đều có nguy cơ làm sai quan hệ cha-con. Vì vậy phần tiếp theo kiểm tra tính đúng đắn bằng bất biến trước và sau biến đổi.

## Serialization

Một serialization phải chứa đủ thông tin để khôi phục cả giá trị lẫn hình dạng.

Với cây nhị phân, preorder chỉ ghi giá trị thường không đủ. Có thể thêm marker cho nút null:

```text
1,2,#,#,3,#,#
```

Khi đó quá trình đọc lại có thể tái dựng duy nhất cấu trúc.

Nếu cây có thêm siêu dữ liệu (metadata / 메타데이터) như màu, chiều cao hoặc kích thước subtree, cần quyết định siêu dữ liệu (metadata / 메타데이터) nào được lưu và siêu dữ liệu (metadata / 메타데이터) nào có thể tính lại từ cấu trúc cơ sở.

> **Mối nối:** Một phép biến đổi đúng phải bảo toàn đúng những bất biến mà thuật toán phụ thuộc, không chỉ tạo ra một hình vẽ trông hợp lý. Cây tĩnh và cây động tiếp theo đặt cùng nguyên tắc ấy vào hai chế độ cập nhật khác nhau.

## Tính đúng đắn khi biến đổi cây

Các thao tác như rotation, split, merge hoặc transplant phải giữ những bất biến cụ thể.

Ví dụ rotation trong BST phải giữ thứ tự inorder. Trong AVL còn phải cập nhật chiều cao. Trong order-statistic cây (tree / 트리) còn phải cập nhật kích thước subtree.

Một phép biến đổi có thể đúng về topology nhưng sai siêu dữ liệu (metadata / 메타데이터). Vì vậy cách kiểm thử tốt là xác minh cả cấu trúc và mọi dữ liệu tăng cường sau chuỗi thao tác ngẫu nhiên.

> **Mối nối:** Cây tĩnh cho phép tối ưu bố trí và tiền xử lý, còn cây động phải trả chi phí cho mỗi lần chèn, xóa hoặc xoay. Những khác biệt đó giải thích vì sao các lỗi tư duy phổ biến thường xuất hiện khi ta mang bảo đảm của mô hình này sang mô hình kia.

## Cây tĩnh và cây động

Nếu cây không đổi sau khi xây dựng, ta có thể tiền xử lý mạnh: Euler tour, nhị phân (binary / 이진) lifting, HLD, prefix theo gốc. Nếu liên kết cạnh thay đổi thường xuyên, nhiều tiền xử lý trở nên không hợp lệ và cần cấu trúc động chuyên biệt như Link-Cut cây (tree / 트리) hoặc Euler Tour cây (tree / 트리).

Đây là một nguyên tắc tổng quát: **tính tĩnh của dữ liệu cho phép chuyển chi phí từ truy vấn sang tiền xử lý**.

> **Mối nối:** Các lỗi thường quy về việc quên hình dạng, bất biến hoặc mô hình chi phí mà cấu trúc cây đang giả định. Phần mô hình tư duy gom những ranh giới này thành vài câu hỏi có thể dùng lại khi chọn hoặc thiết kế một cấu trúc cây.

## Các lỗi tư duy phổ biến

“Cây luôn có chiều cao `O(log n)`” — sai; chỉ đúng khi hình dạng được kiểm soát.

“Đệ quy luôn là cách tốt nhất để duyệt cây” — không đúng nếu độ sâu có thể rất lớn.

“Cây con luôn là một đoạn liên tục trong mọi thứ tự duyệt” — không; tính chất này phụ thuộc cách flatten và loại truy vấn.

“Thêm parent/kích thước (size / 크기)/height chỉ là thêm dữ liệu” — mỗi trường mới tạo thêm bất biến phải được cập nhật ở mọi phép biến đổi.

“Cây và đồ thị là hai thế giới tách biệt” — cây là trường hợp đặc biệt của đồ thị với bất biến mạnh hơn.

> **Mối nối:** Hãy mang sang phần kế tiếp ba câu hỏi: bất biến nào cần giữ, thao tác nào cần nhanh, và hình dạng nào bảo đảm được chi phí đó? Chúng nối nền tảng cây với các biến thể tìm kiếm, cân bằng và truy vấn sẽ học tiếp.

## Mô hình tư duy

> Cây mạnh vì nó biến một hệ thống lớn thành các cây con độc lập được nối bằng quan hệ cha–con. Đệ quy, quy nạp, DP và nhiều phép tiền xử lý đều khai thác chính ranh giới này.

Khi gặp bài toán cây, hãy hỏi: **cây con cần trả thông tin gì cho cha, cha cần truyền thông tin gì xuống con, truy vấn nằm trên subtree hay đường dẫn (path / 경로), cây tĩnh hay động, hình dạng có được cân bằng không, và siêu dữ liệu (metadata / 메타데이터) nào phải trở thành bất biến?**

Xem tiếp: [Binary Search Trees](./01_binary_search_trees.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Heaps](./03_heaps.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
