# Nền tảng về cây

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Nền tảng về cây**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Cây có gốc và bất biến n − 1 cạnh** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **Cây là một đối tượng đệ quy** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối tree foundations với node, edge, root, depth và traversal, để mọi biến thể cây dùng cùng từ vựng nền.

**cây (tree / 트리) / 트리**

Cây là một trong những mô hình quan trọng nhất của Khoa học máy tính vì nó biểu diễn **quan hệ phân cấp (hierarchical relationship)**. Hệ thống tệp, DOM, AST, cây danh mục, chỉ mục cơ sở dữ liệu, cấu trúc định tuyến và cây quyết định đều có thể được nhìn dưới góc này.

Điểm cốt lõi không phải hình vẽ “một nút ở trên và nhiều nút ở dưới”, mà là tính đệ quy: mỗi phần con của cây lại có thể được xem như một cây nhỏ hơn. Chính tính chất đó làm cho đệ quy, quy nạp cấu trúc, chia bài toán theo cây con và quy hoạch động trên cây trở nên tự nhiên.

## Cây có gốc và bất biến n − 1 cạnh

Trong một **cây có gốc (rooted tree)**, có một nút được chọn làm gốc. Mỗi nút khác gốc có đúng một nút cha và có thể có nhiều nút con. Cây không chứa chu trình.

Nếu cây có `n` nút thì có đúng `n-1` cạnh. Lý do rất trực tiếp: mỗi nút ngoài gốc cần đúng một cạnh nối nó với cha. Không thể có thêm cạnh mà vẫn giữ đồng thời tính liên thông và không chu trình.

Bất biến này giúp phân biệt cây với đồ thị tổng quát, nơi một đỉnh có thể có nhiều đường quay lại hoặc nhiều quan hệ giống “cha”.

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Cây là một đối tượng đệ quy** tiếp nhận điểm tựa từ **Cây có gốc và bất biến n − 1 cạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ sâu, chiều cao và kích thước cây con** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Nền tảng về cây**, **Độ sâu, chiều cao và kích thước cây con** tiếp nhận điểm tựa từ **Cây là một đối tượng đệ quy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Full, complete, perfect và balanced** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ sâu, chiều cao và kích thước cây con

**độ sâu (depth / 깊이)** của nút thường là số cạnh từ gốc tới nút. **Chiều cao (height)** là độ dài đường đi dài nhất từ nút xuống một lá. **Kích thước cây con (subtree size)** là số nút thuộc cây con có gốc tại nút đó.

Ba đại lượng phục vụ các câu hỏi khác nhau. Độ sâu xuất hiện trong LCA và khoảng cách. Chiều cao quyết định chi phí trường hợp xấu nhất của nhiều cây tìm kiếm. Kích thước cây con hỗ trợ rank, thứ tự (order / 순서) statistics và nhiều kỹ thuật rerooting.

Nếu cây nhị phân có chiều cao `h` với gốc ở độ sâu 0, số nút tối đa là:

\[
2^{h+1}-1
\]

Do đó cây có hình dạng cân bằng có chiều cao cỡ `O(log n)`, còn cây lệch có thể cao `O(n)`. Chính hình dạng cây quyết định nhiều bảo đảm hiệu năng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng về cây**, **Full, complete, perfect và balanced** tiếp nhận điểm tựa từ **Độ sâu, chiều cao và kích thước cây con** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Duyệt cây là chọn thứ tự xử lý phụ thuộc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Full, complete, perfect và balanced

Các thuật ngữ này mô tả các bất biến khác nhau.

**Full nhị phân (binary / 이진) cây (tree / 트리)**: mỗi nút có 0 hoặc 2 con.

**Complete nhị phân (binary / 이진) cây (tree / 트리)**: mọi tầng trước tầng cuối đầy đủ và tầng cuối được lấp từ trái sang phải. nhị phân (binary / 이진) vùng nhớ động (heap / 힙) dựa vào tính chất này để biểu diễn bằng mảng.

**Perfect nhị phân (binary / 이진) cây (tree / 트리)**: mọi nút trong có đúng hai con và mọi lá cùng độ sâu.

**Balanced cây (tree / 트리)**: chiều cao được kiểm soát đủ tốt, thường ở mức logarithmic. AVL và Red-Black cây (tree / 트리) dùng các bất biến khác nhau để đạt mục tiêu này.

Không nên học các tên này tách rời mục đích. vùng nhớ động (heap / 힙) cần complete shape; BST cần thứ tự khóa; AVL cần cân bằng chiều cao; B+cây (tree / 트리) cần hệ số phân nhánh lớn và mức lấp đầy phù hợp với trang lưu trữ.

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Duyệt cây là chọn thứ tự xử lý phụ thuộc** tiếp nhận điểm tựa từ **Full, complete, perfect và balanced** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đệ quy đang lưu trạng thái gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Nền tảng về cây**, **Đệ quy đang lưu trạng thái gì?** tiếp nhận điểm tựa từ **Duyệt cây là chọn thứ tự xử lý phụ thuộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn cây trong bộ nhớ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng về cây**, **Biểu diễn cây trong bộ nhớ** tiếp nhận điểm tựa từ **Đệ quy đang lưu trạng thái gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Có cần con trỏ cha không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Có cần con trỏ cha không?** tiếp nhận điểm tựa từ **Biểu diễn cây trong bộ nhớ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Euler Tour: biến cây con thành đoạn liên tục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Có cần con trỏ cha không?

Nếu chỉ duyệt từ gốc xuống, parent có thể được truyền qua ngăn xếp (stack / 스택)/recursion. Nếu tải công việc (workload / 워크로드) thường xuyên cần predecessor, successor, đi lên hoặc truy vấn tổ tiên, lưu parent có thể hữu ích.

Đổi lại, mỗi nút tốn thêm bộ nhớ và mọi phép xoay/nối lại phải cập nhật parent đúng. Mỗi siêu dữ liệu (metadata / 메타데이터) mới là một bất biến mới phải duy trì.

> **Chuyển mạch:** Ở chặng này của **Nền tảng về cây**, **Euler Tour: biến cây con thành đoạn liên tục** tiếp nhận điểm tựa từ **Có cần con trỏ cha không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lowest dùng chung (common / 공통) Ancestor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Euler Tour: biến cây con thành đoạn liên tục

Một DFS có thể gán `tin[u]` khi đi vào nút và `tout[u]` sau khi xử lý cây con. Nếu đánh số theo thời điểm vào, các nút của `subtree(u)` nằm liên tục trong thứ tự DFS:

```text
subtree(u) <-> [tin[u], tout[u]]
```

Đây là cầu nối mạnh từ cây sang bài toán truy vấn đoạn.

Ví dụ, nếu cần cập nhật giá trị một nút và truy vấn tổng toàn cây con, ta có thể flatten cây rồi dùng Fenwick cây (tree / 트리) hoặc Segment cây (tree / 트리) trên mảng Euler.

Một vấn đề phân cấp đã được chuyển thành bài toán khoảng mà vẫn giữ nguyên ngữ nghĩa cây con.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng về cây**, **Lowest dùng chung (common / 공통) Ancestor** tiếp nhận điểm tựa từ **Euler Tour: biến cây con thành đoạn liên tục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cây (tree / 트리) DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lowest dùng chung (common / 공통) Ancestor

**Tổ tiên chung thấp nhất (Lowest Common Ancestor – LCA / 최소 공통 조상)** của hai nút là tổ tiên chung có độ sâu lớn nhất.

Nếu chỉ có ít truy vấn, có thể đưa hai nút lên theo parent. Với nhiều truy vấn, **nhị phân (binary / 이진) lifting** tiền xử lý:

```text
up[k][v] = tổ tiên của v cách 2^k cạnh
```

Khoảng cách bất kỳ có thể phân rã thành tổng các lũy thừa của 2, nên ta có thể nâng nút theo các bit của độ sâu. Tiền xử lý thường `O(n log n)`, mỗi truy vấn `O(log n)`.

Ý tưởng này cùng họ với Sparse bảng (table / 테이블) và exponentiation by squaring: tiền xử lý các khối kích thước tăng gấp đôi để ghép nhanh một bước lớn.

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Cây (tree / 트리) DP** tiếp nhận điểm tựa từ **Lowest dùng chung (common / 공통) Ancestor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rerooting DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cây (tree / 트리) DP

Khi đã cố định parent, các cây con không giao nhau. Đây là điều kiện lý tưởng cho quy hoạch động.

Ví dụ tập độc lập cực đại trên cây:

```text
dp[u][0] = kết quả tốt nhất trong subtree(u) khi không chọn u
dp[u][1] = kết quả tốt nhất trong subtree(u) khi chọn u
```

Nếu chọn `u`, các con trực tiếp không được chọn. Nếu không chọn `u`, mỗi cây con có thể chọn trạng thái tốt hơn của nó.

Điểm quan trọng là trạng thái DP xuất phát từ **thông tin tối thiểu mà cây con cần biết về phía cha**, không phải từ việc “bài cây thì phải dùng dp[u]”.

> **Chuyển mạch:** Ở chặng này của **Nền tảng về cây**, **Rerooting DP** tiếp nhận điểm tựa từ **Cây (tree / 트리) DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cây là đồ thị có bất biến mạnh hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rerooting DP

Một số bài yêu cầu đáp án khi từng nút lần lượt được xem là gốc. Chạy DFS lại từ mỗi nút tốn `O(n²)`.

Rerooting tái sử dụng kết quả giữa hai gốc kề nhau:

```text
lượt 1: tổng hợp đóng góp từ con lên cha
lượt 2: truyền đóng góp của phần còn lại của cây từ cha xuống con
```

Đây là một ví dụ quan trọng của tư duy “đừng tính lại toàn bộ khi trạng thái mới chỉ khác trạng thái cũ bởi một cạnh”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng về cây**, **Cây là đồ thị có bất biến mạnh hơn** tiếp nhận điểm tựa từ **Rerooting DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khoảng cách trên cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cây là đồ thị có bất biến mạnh hơn

Mọi cây là đồ thị liên thông không chu trình. Giữa hai nút tồn tại đúng một đường đi đơn giản.

Vì vậy, nhiều bài toán đồ thị trở nên đơn giản hơn trên cây. Nếu đầu vào được bảo đảm là cây và DFS nhận parent, không cần một `visited` set tổng quát; chỉ cần tránh đi ngược lại parent.

Ngược lại, nếu dữ liệu chỉ “trông giống cây” nhưng có thể chứa chu trình hoặc nhiều parent, phải quay lại mô hình đồ thị tổng quát.

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Khoảng cách trên cây** tiếp nhận điểm tựa từ **Cây là đồ thị có bất biến mạnh hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đường kính cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khoảng cách trên cây

Với cây không trọng số, nếu biết độ sâu và LCA:

\[
dist(u,v)=độ sâu (depth / 깊이)(u)+độ sâu (depth / 깊이)(v)-2\cdot độ sâu (depth / 깊이)(lca(u,v))
\]

Công thức xuất phát từ việc đường đi duy nhất từ `u` tới `v` đi từ `u` lên LCA rồi xuống `v`.

Nếu cạnh có trọng số, thay `depth` bằng tổng trọng số từ gốc tới nút.

> **Chuyển mạch:** Ở chặng này của **Nền tảng về cây**, **Đường kính cây** tiếp nhận điểm tựa từ **Khoảng cách trên cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Centroid** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng về cây**, **Centroid** tiếp nhận điểm tựa từ **Đường kính cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Heavy-Light Decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Centroid

**Centroid của cây** là nút mà khi loại bỏ nó, mọi thành phần còn lại có kích thước không quá `n/2`. Cây có một hoặc hai centroid.

Centroid quan trọng vì nó tạo điểm chia cân bằng theo kích thước, không phải theo chiều cao. **Centroid decomposition** liên tục chọn centroid rồi phân rã các thành phần, tạo một cây phân rã có chiều cao `O(log n)`.

Kỹ thuật này hữu ích cho truy vấn khoảng cách động trên cây và là ví dụ về việc xây một cấu trúc phụ để thay đổi không gian truy vấn.

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Heavy-Light Decomposition** tiếp nhận điểm tựa từ **Centroid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cây và biểu thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Heavy-Light Decomposition

Đường đi giữa hai nút không nhất thiết tạo một đoạn liên tục trong Euler thứ tự (order / 순서). **Heavy-Light Decomposition (HLD)** chia các cạnh thành heavy/light để một đường đi bất kỳ được biểu diễn bởi `O(log n)` đoạn liên tục trên các chuỗi (chain / 사슬).

Kết hợp HLD với Segment cây (tree / 트리)/Fenwick cây (tree / 트리) cho phép xử lý nhiều truy vấn/cập nhật trên đường đi.

Trực giác là chọn cho mỗi nút một con “heavy” có subtree lớn nhất. Mỗi lần đi qua cạnh light, kích thước subtree giảm ít nhất khoảng một nửa, nên số lần đổi chuỗi (chain / 사슬) trên một đường bị chặn logarithmic.

> **Chuyển mạch:** Ở chặng này của **Nền tảng về cây**, **Cây và biểu thức** tiếp nhận điểm tựa từ **Heavy-Light Decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Serialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cây và biểu thức

AST và expression cây (tree / 트리) cho thấy traversal tương ứng trực tiếp với thứ tự đánh giá.

Postorder phù hợp để tính biểu thức vì toán hạng con phải được tính trước toán tử cha. Preorder có thể tạo dạng prefix; inorder liên hệ với dạng infix nhưng cần ngoặc để bảo toàn cấu trúc.

Đây là ví dụ cây không chỉ lưu dữ liệu mà còn mã hóa thứ tự phụ thuộc của phép tính.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng về cây**, **Serialization** tiếp nhận điểm tựa từ **Cây và biểu thức** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đúng đắn khi biến đổi cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Serialization

Một serialization phải chứa đủ thông tin để khôi phục cả giá trị lẫn hình dạng.

Với cây nhị phân, preorder chỉ ghi giá trị thường không đủ. Có thể thêm marker cho nút null:

```text
1,2,#,#,3,#,#
```

Khi đó quá trình đọc lại có thể tái dựng duy nhất cấu trúc.

Nếu cây có thêm siêu dữ liệu (metadata / 메타데이터) như màu, chiều cao hoặc kích thước subtree, cần quyết định siêu dữ liệu (metadata / 메타데이터) nào được lưu và siêu dữ liệu (metadata / 메타데이터) nào có thể tính lại từ cấu trúc cơ sở.

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Tính đúng đắn khi biến đổi cây** tiếp nhận điểm tựa từ **Serialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cây tĩnh và cây động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đúng đắn khi biến đổi cây

Các thao tác như rotation, split, merge hoặc transplant phải giữ những bất biến cụ thể.

Ví dụ rotation trong BST phải giữ thứ tự inorder. Trong AVL còn phải cập nhật chiều cao. Trong order-statistic cây (tree / 트리) còn phải cập nhật kích thước subtree.

Một phép biến đổi có thể đúng về topology nhưng sai siêu dữ liệu (metadata / 메타데이터). Vì vậy cách kiểm thử tốt là xác minh cả cấu trúc và mọi dữ liệu tăng cường sau chuỗi thao tác ngẫu nhiên.

> **Chuyển mạch:** Ở chặng này của **Nền tảng về cây**, **Cây tĩnh và cây động** tiếp nhận điểm tựa từ **Tính đúng đắn khi biến đổi cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các lỗi tư duy phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cây tĩnh và cây động

Nếu cây không đổi sau khi xây dựng, ta có thể tiền xử lý mạnh: Euler tour, nhị phân (binary / 이진) lifting, HLD, prefix theo gốc. Nếu liên kết cạnh thay đổi thường xuyên, nhiều tiền xử lý trở nên không hợp lệ và cần cấu trúc động chuyên biệt như Link-Cut cây (tree / 트리) hoặc Euler Tour cây (tree / 트리).

Đây là một nguyên tắc tổng quát: **tính tĩnh của dữ liệu cho phép chuyển chi phí từ truy vấn sang tiền xử lý**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng về cây**, **Các lỗi tư duy phổ biến** tiếp nhận điểm tựa từ **Cây tĩnh và cây động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các lỗi tư duy phổ biến

“Cây luôn có chiều cao `O(log n)`” — sai; chỉ đúng khi hình dạng được kiểm soát.

“Đệ quy luôn là cách tốt nhất để duyệt cây” — không đúng nếu độ sâu có thể rất lớn.

“Cây con luôn là một đoạn liên tục trong mọi thứ tự duyệt” — không; tính chất này phụ thuộc cách flatten và loại truy vấn.

“Thêm parent/kích thước (size / 크기)/height chỉ là thêm dữ liệu” — mỗi trường mới tạo thêm bất biến phải được cập nhật ở mọi phép biến đổi.

“Cây và đồ thị là hai thế giới tách biệt” — cây là trường hợp đặc biệt của đồ thị với bất biến mạnh hơn.

> **Chuyển mạch:** Trong **Nền tảng về cây**, **Mô hình tư duy** gom các mảnh từ **Các lỗi tư duy phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Cây mạnh vì nó biến một hệ thống lớn thành các cây con độc lập được nối bằng quan hệ cha–con. Đệ quy, quy nạp, DP và nhiều phép tiền xử lý đều khai thác chính ranh giới này.

Khi gặp bài toán cây, hãy hỏi: **cây con cần trả thông tin gì cho cha, cha cần truyền thông tin gì xuống con, truy vấn nằm trên subtree hay đường dẫn (path / 경로), cây tĩnh hay động, hình dạng có được cân bằng không, và siêu dữ liệu (metadata / 메타데이터) nào phải trở thành bất biến?**

Xem tiếp: [Binary Search Trees](./01_binary_search_trees.md), [Balanced Search Trees](./02_balanced_search_trees.md), [Heaps](./03_heaps.md), [Augmented Trees](./06_augmented_trees_and_order_statistics.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
