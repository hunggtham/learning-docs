# Tính đúng đắn và bất biến của thuật toán

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tính đúng đắn và bất biến của thuật toán**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Trước khi chứng minh phải có specification** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Điều kiện trước và điều kiện sau** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**thuật toán (algorithm / 알고리즘) tính đúng đắn (correctness / 정확성) & Invariants / 알고리즘 정확성과 불변식**

Một thuật toán nhanh nhưng sai không có giá trị. Kiểm thử chỉ chứng minh chương trình hoạt động đúng trên những trường hợp đã chạy; nó không tự chứng minh rằng thuật toán đúng với mọi đầu vào hợp lệ. Vì vậy, một năng lực trung tâm của DSA là **lập luận về tính đúng đắn (correctness reasoning)**: biết mình được phép giả định điều gì, điều gì phải luôn đúng trong quá trình chạy, vì sao thuật toán tiến về điểm dừng và vì sao trạng thái cuối bắt buộc thỏa yêu cầu.

Chứng minh không nhất thiết phải là một văn bản toán học dài. Trong thực hành, chỉ cần xác định đúng specification, bất biến (invariant / 불변식) và progress measure thường đã đủ biến một đoạn mã (code / 코드) khó tin thành một chuỗi lập luận có thể kiểm tra.

## Trước khi chứng minh phải có specification

Một thuật toán chỉ “đúng” so với một **đặc tả (specification / 명세)** cụ thể.

Specification thường phải nói rõ:

```text
miền đầu vào hợp lệ
điều kiện trước
ngữ nghĩa đầu ra
điều kiện sau
tie-breaking nếu có
hành vi với input không hợp lệ
```

Ví dụ “tìm kiếm nhị phân (binary search / 이진 탐색)” có thể có nhiều specification khác nhau:

```text
trả một vị trí bất kỳ chứa target
trả vị trí đầu tiên chứa target
trả lower_bound
trả insertion point nếu không có target
```

Tên thuật toán giống nhau nhưng điều kiện sau khác nhau, nên bất biến và mã (code / 코드) cũng khác nhau.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Điều kiện trước và điều kiện sau** tiếp nhận điểm tựa từ **Trước khi chứng minh phải có specification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hoare triple: cách viết hợp đồng ngắn gọn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều kiện trước và điều kiện sau

**Điều kiện trước (precondition / 사전 조건)** là điều phải đúng trước khi thao tác bắt đầu. **Điều kiện sau (postcondition / 사후 조건)** là điều thao tác cam kết khi kết thúc bình thường.

Ví dụ `merge(left, right)` thường có precondition: hai dãy đầu vào đã được sắp xếp theo cùng comparator. Postcondition cần mạnh hơn câu “đầu ra đã sorted”; nó còn phải bảo toàn đúng đa tập phần tử của hai đầu vào.

```text
sorted(output)
multiset(output) = multiset(left) ∪ multiset(right)
```

Nếu chỉ chứng minh thứ tự mà không chứng minh bảo toàn phần tử, một hiện thực (implementation / 구현) làm mất hoặc nhân đôi dữ liệu vẫn có thể vượt qua nửa đầu specification.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Hoare triple: cách viết hợp đồng ngắn gọn** tiếp nhận điểm tựa từ **Điều kiện trước và điều kiện sau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partial tính đúng đắn (correctness / 정확성) và total tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hoare triple: cách viết hợp đồng ngắn gọn

Một cách ký hiệu hữu ích là:

\[
\{P\}\ C\ \{Q\}
\]

Trong đó `P` là precondition, `C` là đoạn chương trình và `Q` là postcondition.

Ví dụ:

```text
{ a đã sorted }
binarySearch(a, x)
{ trả vị trí hợp lệ của x hoặc xác nhận x không tồn tại }
```

Ta không cần formal xác minh (verification / 확인) hoàn chỉnh để hưởng lợi từ cách nghĩ này. Nó buộc ta tách rõ “được giả định gì” và “phải bảo đảm gì”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Partial tính đúng đắn (correctness / 정확성) và total tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **Hoare triple: cách viết hợp đồng ngắn gọn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bất biến vòng lặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partial tính đúng đắn (correctness / 정확성) và total tính đúng đắn (correctness / 정확성)

**Tính đúng đắn từng phần (partial correctness)** nói rằng: nếu thuật toán kết thúc thì kết quả đúng.

**Tính đúng đắn toàn phần (total correctness)** thêm yêu cầu thuật toán thực sự kết thúc trên mọi đầu vào (input / 입력) hợp lệ.

Một vòng lặp có thể giữ bất biến (invariant / 불변식) hoàn hảo nhưng không thu nhỏ không gian tìm kiếm, dẫn tới chạy vô hạn. Vì vậy chứng minh vòng lặp (loop / 루프) thường cần hai phần:

```text
safety: invariant luôn đúng
progress: một đại lượng tiến dần về điểm dừng
```

Đại lượng dùng để chứng minh tiến triển thường gọi là **variant** hoặc **ranking hàm (function / 함수)**.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Bất biến vòng lặp** tiếp nhận điểm tựa từ **Partial tính đúng đắn (correctness / 정확성) và total tính đúng đắn (correctness / 정확성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bất biến (invariant / 불변식) phải đủ mạnh nhưng không quá khó duy trì** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất biến vòng lặp

**Bất biến vòng lặp (loop invariant / 루프 불변식)** là một mệnh đề đúng tại một vị trí xác định của mọi vòng lặp.

Một mẫu chứng minh chuẩn có ba bước:

```text
Initialization: invariant đúng trước vòng đầu tiên.
Maintenance: nếu invariant đúng trước vòng hiện tại, thân vòng giữ nó đúng cho vòng sau.
Termination: invariant + điều kiện dừng suy ra postcondition.
```

### Ví dụ: tìm kiếm nhị phân (binary search / 이진 탐색)

Với đoạn ứng viên `[lo, hi]`, bất biến (invariant / 불변식) có thể là:

> Nếu mục tiêu (target / 대상) tồn tại thì mọi vị trí còn có khả năng chứa mục tiêu (target / 대상) đều nằm trong `[lo, hi]`.

```c
int binary_search(const int *a, int n, int target) {
    int lo = 0, hi = n - 1;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;

        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
}
```

Nếu `a[mid] < target`, tính sorted cho phép loại toàn bộ `[lo, mid]`. Không chỉ một phần tử bị loại; cả một vùng được chứng minh không còn khả năng chứa đáp án.

Progress measure là độ dài đoạn ứng viên. Mỗi vòng không trả kết quả đều làm đoạn ngắn hơn, nên thuật toán kết thúc.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Bất biến (invariant / 불변식) phải đủ mạnh nhưng không quá khó duy trì** tiếp nhận điểm tựa từ **Bất biến vòng lặp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bất biến bảo toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất biến (invariant / 불변식) phải đủ mạnh nhưng không quá khó duy trì

Một câu kiểu “mảng đang được xử lý đúng” không giúp chứng minh điều gì. bất biến (invariant / 불변식) tốt phải đủ mạnh để suy ra postcondition, nhưng đủ đơn giản để chứng minh maintenance.

Insertion Sort có bất biến (invariant / 불변식) mạnh:

> Trước vòng `i`, đoạn `a[0..i)` đã sorted và chứa đúng đa tập phần tử ban đầu của đoạn đó.

Hai phần đều quan trọng:

```text
order invariant
conservation invariant
```

Nếu thiếu conservation, ta chưa chứng minh thuật toán không làm mất hoặc nhân đôi phần tử.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Bất biến bảo toàn** tiếp nhận điểm tựa từ **Bất biến (invariant / 불변식) phải đủ mạnh nhưng không quá khó duy trì** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn (representation / 표현) bất biến (invariant / 불변식) của cấu trúc dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất biến bảo toàn

Nhiều thuật toán mutate dữ liệu, nên cần theo dõi cái gì phải được bảo toàn.

Sorting bảo toàn đa tập phần tử. vùng nhớ động (heap / 힙) giữ toàn bộ phần tử ngoài đúng phần tử vừa chèn/xóa. DSU bảo toàn partition của tập phần tử. đồ thị (graph / 그래프) traversal phải bảo đảm mọi trạng thái được đánh dấu thực sự reachable từ nguồn theo quy tắc chuyển tiếp (transition / 전이).

Một validator tốt hiếm khi chỉ kiểm tra một thuộc tính (property / 속성).

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Bất biến bảo toàn** nêu điều cần giải thích; **Biểu diễn (representation / 표현) bất biến (invariant / 불변식) của cấu trúc dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bất biến cục bộ và bất biến toàn cục** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn (representation / 표현) bất biến (invariant / 불변식) của cấu trúc dữ liệu

Cấu trúc dữ liệu thường có **bất biến biểu diễn (representation invariant)** mạnh hơn postcondition của từng thao tác.

Ví dụ nhị phân (binary / 이진) vùng nhớ động (heap / 힙):

```text
shape là complete binary tree
size phù hợp vùng hợp lệ của mảng
heap order đúng trên mọi cạnh cha-con
```

Red-Black cây (tree / 트리) có thêm các bất biến về màu và black-height. bảng băm (hash table / 해시 테이블) phải giữ quan hệ giữa trạng thái slot, số phần tử và quy tắc probing. Doubly Linked danh sách (list / 목록) phải giữ `next/prev` đối xứng.

Mỗi thao tác công khai (public / 공개) có thể được xem như:

```text
representation invariant trước thao tác
        ↓
thao tác
        ↓
representation invariant sau thao tác
```

Nếu bất biến (invariant / 불변식) được phục hồi trước khi API trả về, các thao tác sau có thể tiếp tục dựa trên nó.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Biểu diễn (representation / 표현) bất biến (invariant / 불변식) của cấu trúc dữ liệu** nêu điều cần giải thích; **Bất biến cục bộ và bất biến toàn cục** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ghost trạng thái (state / 상태): thông tin dùng để chứng minh nhưng không cần lưu trong thời gian chạy (runtime / 런타임)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất biến cục bộ và bất biến toàn cục

Một số bất biến (invariant / 불변식) có thể kiểm tra cục bộ. vùng nhớ động (heap / 힙) thứ tự (order / 순서) chỉ cần so mỗi cha với con. Nhưng BST không thể chỉ kiểm tra `left < parent < right` ở mỗi cạnh; một khóa sâu trong cây con trái vẫn phải nhỏ hơn toàn bộ cận trên từ tổ tiên.

Do đó validator BST nên truyền khoảng hợp lệ xuống:

```text
node.key ∈ (lowerBound, upperBound)
```

Đây là bài học tổng quát: **cục bộ (local / 로컬) consistency không luôn suy ra toàn cục (global / 전역) tính đúng đắn (correctness / 정확성)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Ghost trạng thái (state / 상태): thông tin dùng để chứng minh nhưng không cần lưu trong thời gian chạy (runtime / 런타임)** tiếp nhận điểm tựa từ **Bất biến cục bộ và bất biến toàn cục** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy nạp và đệ quy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ghost trạng thái (state / 상태): thông tin dùng để chứng minh nhưng không cần lưu trong thời gian chạy (runtime / 런타임)

Khi lập luận (reasoning / 추론), ta có thể dùng thông tin phụ không tồn tại trong hiện thực (implementation / 구현). Đây thường được gọi là **ghost trạng thái (state / 상태)** trong formal methods.

Ví dụ khi chứng minh sorting, ta có thể tưởng tượng một bản sao multiset của đầu vào (input / 입력) ban đầu để chứng minh conservation, dù mã (code / 코드) thực tế không lưu bản sao đó.

Trong BFS, ta có thể lập luận (reasoning / 추론) bằng “khoảng cách thật ngắn nhất” `δ(s,v)` dù hiện thực (implementation / 구현) chỉ lưu `dist[v]`.

Ghost trạng thái (state / 상태) giúp tách “thông tin cần để chứng minh” khỏi “thông tin cần để chạy hiệu quả”.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Quy nạp và đệ quy** tiếp nhận điểm tựa từ **Ghost trạng thái (state / 상태): thông tin dùng để chứng minh nhưng không cần lưu trong thời gian chạy (runtime / 런타임)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quy nạp mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy nạp và đệ quy

Thuật toán đệ quy thường được chứng minh bằng **quy nạp (induction / 수학적 귀납법)**.

Merge Sort:

```text
base: n <= 1 đã sorted
hypothesis: mọi lời gọi trên kích thước nhỏ hơn trả đúng
step: hai nửa được sort đúng + merge đúng => toàn bộ đúng
```

Với cây, **quy nạp cấu trúc (structural induction)** còn tự nhiên hơn. Nếu hàm trên nút chỉ phụ thuộc các cây con, ta giả sử các cây con trả đúng rồi chứng minh phép kết hợp ở nút cha đúng.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Quy nạp mạnh** tiếp nhận điểm tựa từ **Quy nạp và đệ quy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hợp đồng của hàm đệ quy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quy nạp mạnh

Động (dynamic / 동적) Programming thường cần **quy nạp mạnh (strong induction)** vì trạng thái hiện tại có thể phụ thuộc nhiều trạng thái nhỏ hơn, không chỉ đúng một trạng thái `n-1`.

Bottom-up DP về bản chất thực thi đúng thứ tự chứng minh: mọi prerequisite được tính trước khi chuyển tiếp (transition / 전이) hiện tại dùng tới chúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Hợp đồng của hàm đệ quy** tiếp nhận điểm tựa từ **Quy nạp mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chứng minh termination cho đệ quy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hợp đồng của hàm đệ quy

Khi gỡ lỗi (debug / 디버그) recursion, thay vì mô phỏng toàn bộ lời gọi (call / 호출) cây (tree / 트리), hãy viết đặc tả hợp đồng (contract / 계약) cho một lời gọi.

Ví dụ:

```text
solve(state) trả giá trị tối ưu đạt được từ state trở đi,
và khi trả về thì global mutable state đã được phục hồi như trước lời gọi.
```

Trong backtracking, phần “phục hồi trạng thái (state / 상태)” là cực kỳ quan trọng. Nếu `choose -> recurse -> unchoose` không đối xứng, lời gọi anh em có thể nhìn thấy trạng thái rác.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Chứng minh termination cho đệ quy** tiếp nhận điểm tựa từ **Hợp đồng của hàm đệ quy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Greedy và exchange argument** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chứng minh termination cho đệ quy

Có cơ sở (base / 기반) trường hợp (case / 사례) chưa đủ. Đối số đệ quy phải tiến gần cơ sở (base / 기반) trường hợp (case / 사례) theo một well-founded thứ tự (order / 순서).

Ví dụ:

```text
n giảm dần
số phần tử chưa xử lý giảm dần
chiều sâu còn lại giảm dần
kích thước cây con nhỏ hơn cây cha
```

Nếu recursion có thể quay lại trạng thái cũ mà không có visited/memoization hoặc progress chỉ số (metric / 지표), termination chưa được chứng minh.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Greedy và exchange argument** tiếp nhận điểm tựa từ **Chứng minh termination cho đệ quy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cut thuộc tính (property / 속성) và cycle thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Greedy và exchange argument

Greedy khóa lựa chọn cục bộ và không quay lại, vì vậy phải chứng minh lựa chọn đó an toàn.

Mẫu **exchange argument**:

```text
1. Lấy một lời giải tối ưu O.
2. Nếu O đã chứa lựa chọn greedy g, xong bước này.
3. Nếu chưa, thay một phần của O bằng g.
4. Chứng minh lời giải mới vẫn hợp lệ và không tệ hơn O.
5. Suy ra tồn tại lời giải tối ưu bắt đầu bằng g.
6. Lặp lại cho phần còn lại.
```

Trong interval scheduling, chọn interval kết thúc sớm nhất là an toàn vì thay interval đầu của một optimum bằng interval kết thúc sớm hơn không làm mất thêm không gian thời gian ở phía sau.

“Có vẻ hợp lý” không phải chứng minh greedy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Cut thuộc tính (property / 속성) và cycle thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **Greedy và exchange argument** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proof by contradiction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cut thuộc tính (property / 속성) và cycle thuộc tính (property / 속성)

Minimum Spanning cây (tree / 트리) có các mẫu chứng minh riêng nhưng rất tái sử dụng.

**Cut thuộc tính (property / 속성)** nói rằng dưới điều kiện phù hợp, cạnh nhẹ nhất cắt qua một cut là cạnh an toàn để thêm vào một MST.

**Cycle thuộc tính (property / 속성)** cho góc nhìn đối ngược: trong một cycle, một cạnh nặng nhất thích hợp có thể bị loại khỏi một MST nào đó.

Kruskal và Prim có hiện thực (implementation / 구현) khác nhau nhưng đều dựa vào cấu trúc chứng minh này.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Proof by contradiction** tiếp nhận điểm tựa từ **Cut thuộc tính (property / 속성) và cycle thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chứng minh bằng cực trị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proof by contradiction

Chứng minh phản chứng hữu ích khi thuật toán “finalize” một quyết định.

Dijkstra với cạnh không âm là ví dụ. Khi đỉnh `u` có tentative distance nhỏ nhất được lấy ra, giả sử vẫn có một đường ngắn hơn tới `u`. Trên đường đó phải tồn tại điểm đầu tiên đi từ vùng đã finalize sang vùng chưa finalize. Tính không âm của trọng số tạo một candidate không thể lớn hơn `dist[u]`, mâu thuẫn với việc `u` là candidate nhỏ nhất.

Lập luận này đồng thời chỉ ra vì sao cạnh âm phá điều kiện cốt lõi của Dijkstra.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Chứng minh bằng cực trị** tiếp nhận điểm tựa từ **Proof by contradiction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monotonicity và tìm kiếm nhị phân (binary search / 이진 탐색) on answer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chứng minh bằng cực trị

Một kỹ thuật khác là chọn “phản ví dụ nhỏ nhất”, “đỉnh đầu tiên vi phạm” hoặc “thời điểm đầu tiên bất biến (invariant / 불변식) bị phá”.

Giả sử một thuộc tính (property / 속성) đúng ban đầu nhưng cuối cùng sai. Xét bước đầu tiên nó trở thành sai. Ngay trước bước đó thuộc tính (property / 속성) còn đúng, nên ta chỉ cần phân tích thao tác vừa thực hiện.

Đây là cách rất mạnh để chứng minh bất biến (invariant / 불변식) của cấu trúc động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Monotonicity và tìm kiếm nhị phân (binary search / 이진 탐색) on answer** tiếp nhận điểm tựa từ **Chứng minh bằng cực trị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BFS: bất biến (invariant / 불변식) theo tầng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monotonicity và tìm kiếm nhị phân (binary search / 이진 탐색) on answer

Nếu predicate `P(x)` có dạng:

```text
false false false ... true true true
```

ta có thể tìm điểm chuyển bằng tìm kiếm nhị phân (binary search / 이진 탐색).

Nhưng trước khi viết mã (code / 코드) phải chứng minh **tính đơn điệu (monotonicity)**. Nếu `P(x)` có thể true rồi false trở lại, tìm kiếm nhị phân (binary search / 이진 탐색) on answer không có cơ sở đúng đắn.

Một lỗi phổ biến là thấy “đáp án là một số” rồi áp tìm kiếm nhị phân (binary search / 이진 탐색) mà chưa chứng minh predicate có cấu trúc đơn điệu.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **BFS: bất biến (invariant / 불변식) theo tầng** tiếp nhận điểm tựa từ **Monotonicity và tìm kiếm nhị phân (binary search / 이진 탐색) on answer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DFS: bất biến (invariant / 불변식) của ngăn xếp lời gọi (call stack / 호출 스택)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BFS: bất biến (invariant / 불변식) theo tầng

BFS có một bất biến (invariant / 불변식) quan trọng:

> Khi một đỉnh được lấy ra theo BFS chuẩn trên đồ thị không trọng số, `dist[v]` là độ dài đường đi ngắn nhất từ nguồn tới `v`.

Lý do hàng đợi (queue / 큐) xử lý đỉnh theo lớp khoảng cách không giảm. Mọi cạnh thêm đúng 1 bước. Một đường ngắn hơn tới `v` nếu tồn tại phải đi qua một lớp nhỏ hơn và đã được khám phá trước.

Điều này giải thích vì sao đánh dấu khi enqueue thường quan trọng: nó ngăn cùng một trạng thái (state / 상태) được đưa vào hàng đợi (queue / 큐) nhiều lần và giữ rõ nghĩa “đã phát hiện khoảng cách ngắn nhất”.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **DFS: bất biến (invariant / 불변식) của ngăn xếp lời gọi (call stack / 호출 스택)** tiếp nhận điểm tựa từ **BFS: bất biến (invariant / 불변식) theo tầng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DSU: bất biến (invariant / 불변식) của đại diện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DFS: bất biến (invariant / 불변식) của ngăn xếp lời gọi (call stack / 호출 스택)

Trong DFS đệ quy, ngăn xếp lời gọi (call stack / 호출 스택) biểu diễn đường đi hiện tại trong cây DFS. Với đồ thị có hướng dùng ba màu:

```text
WHITE = chưa thăm
GRAY  = đang nằm trên recursion stack
BLACK = đã hoàn tất
```

Một cạnh tới `GRAY` cho thấy có chu trình có hướng vì ta quay lại một tổ tiên đang hoạt động. Nếu chỉ dùng `visited` Boolean, thông tin “đang hoạt động” bị mất và không đủ cho chứng minh kiểu này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **DSU: bất biến (invariant / 불변식) của đại diện** tiếp nhận điểm tựa từ **DFS: bất biến (invariant / 불변식) của ngăn xếp lời gọi (call stack / 호출 스택)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vùng nhớ vùng nhớ động (heap / 힙): repair cục bộ (local / 로컬), preserve toàn cục (global / 전역)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DSU: bất biến (invariant / 불변식) của đại diện

Disjoint Set Union giữ một forest các parent pointer. bất biến (invariant / 불변식) ngữ nghĩa không phải “cây đẹp”, mà là:

```text
find(x) trả cùng representative khi và chỉ khi x thuộc cùng component theo các union đã áp dụng
```

Đường dẫn (path / 경로) compression thay đổi hình dạng cây mạnh nhưng không đổi partition lô-gic (logic / 논리). Đây là ví dụ một tối ưu hóa (optimization / 최적화) thay biểu diễn (representation / 표현) nhưng giữ ngữ nghĩa (semantics / 의미론).

Nếu có `size[root]` hoặc `rank[root]`, siêu dữ liệu (metadata / 메타데이터) chỉ có ý nghĩa ở gốc (root / 루트) và phải được cập nhật theo đúng union quy tắc (rule / 규칙).

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Vùng nhớ vùng nhớ động (heap / 힙): repair cục bộ (local / 로컬), preserve toàn cục (global / 전역)** tiếp nhận điểm tựa từ **DSU: bất biến (invariant / 불변식) của đại diện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Segment cây (tree / 트리): bất biến (invariant / 불변식) theo đoạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vùng nhớ vùng nhớ động (heap / 힙): repair cục bộ (local / 로컬), preserve toàn cục (global / 전역)

Khi chèn vào nhị phân (binary / 이진) vùng nhớ động (heap / 힙), shape bất biến (invariant / 불변식) được giữ bằng cách thêm ở cuối mảng. Chỉ heap-order trên đường từ nút (node / 노드) mới tới gốc (root / 루트) có thể bị phá.

Sift-up sửa đúng vùng có khả năng sai. Các cạnh ngoài đường đó không thay đổi nên bất biến (invariant / 불변식) vẫn đúng ở đó.

Đây là mẫu chứng minh cực kỳ phổ biến:

```text
một mutation chỉ có thể phá invariant trong một vùng nhỏ
=> sửa vùng đó
=> phần còn lại không cần kiểm tra lại
```

AVL/Red-Black rotation, Segment cây (tree / 트리) cập nhật (update / 업데이트) và nhiều cấu trúc tăng cường đều dựa trên tư duy này.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Segment cây (tree / 트리): bất biến (invariant / 불변식) theo đoạn** tiếp nhận điểm tựa từ **Vùng nhớ vùng nhớ động (heap / 힙): repair cục bộ (local / 로컬), preserve toàn cục (global / 전역)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Shortest đường dẫn (path / 경로) relaxation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Segment cây (tree / 트리): bất biến (invariant / 불변식) theo đoạn

Mỗi nút (node / 노드) Segment cây (tree / 트리) đại diện một đoạn và lưu aggregate của chính đoạn đó.

Bất biến (invariant / 불변식):

```text
tree[node] = combine(value của mọi phần tử trong interval(node))
```

Khi cập nhật một điểm, chỉ các nút (node / 노드) trên đường từ leaf đó tới gốc (root / 루트) có interval chứa điểm cập nhật. Do đó chỉ cần recompute đường này.

Tính đúng đắn đến từ việc các nút (node / 노드) không chứa vị trí cập nhật giữ nguyên giá trị đúng, còn các nút (node / 노드) có chứa nó được tính lại từ hai child đã đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Segment cây (tree / 트리): bất biến (invariant / 불변식) theo đoạn** xác định đầu vào; **Shortest đường dẫn (path / 경로) relaxation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bất biến (invariant / 불변식) giữa nhiều cấu trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Shortest đường dẫn (path / 경로) relaxation

Relaxation thường có dạng:

\[
dist[v] \leftarrow \min(dist[v], dist[u] + w(u,v))
\]

Một bất biến (invariant / 불변식) nền tảng là `dist[v]` luôn là chi phí của một đường đi thực sự đã biết tới `v` hoặc `∞`. Vì vậy nó là một **upper bound** trên shortest-path distance thật.

Các thuật toán shortest đường dẫn (path / 경로) khác nhau chủ yếu khác ở quy tắc chọn thứ tự relaxation và điều kiện cho phép ta kết luận bound đã trở thành chính xác.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Shortest đường dẫn (path / 경로) relaxation** xác định đầu vào; **Bất biến (invariant / 불변식) giữa nhiều cấu trúc** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Atomicity của thao tác phức hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất biến (invariant / 불변식) giữa nhiều cấu trúc

LRU bộ nhớ đệm (cache / 캐시) dùng băm (hash / 해시) Map + Doubly Linked danh sách (list / 목록). Mỗi cấu trúc có thể tự hợp lệ nhưng hệ thống vẫn sai nếu map và danh sách (list / 목록) không nhất quán.

Cần bất biến (invariant / 불변식) liên cấu trúc:

```text
map và list chứa cùng tập key
mỗi map entry trỏ đúng node trong list
size nhất quán
thứ tự list đúng recency semantics
```

Trong mã (code / 코드) môi trường vận hành (production / 운영 환경), đây thường là nơi bug khó xuất hiện nhất vì validator riêng lẻ của từng bộ chứa (container / 컨테이너) vẫn pass.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Atomicity của thao tác phức hợp** tiếp nhận điểm tựa từ **Bất biến (invariant / 불변식) giữa nhiều cấu trúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đồng thời (concurrency / 동시성) và linearizability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Atomicity của thao tác phức hợp

Một thao tác (operation / 연산) có thể gồm nhiều bước nội bộ. Nếu thất bại (failure / 실패) xảy ra giữa chừng, cấu trúc cần hoặc:

```text
rollback về trạng thái cũ
hoặc
đạt một trạng thái mới vẫn hợp lệ theo contract
```

Trong C, resize bảng băm (hash table / 해시 테이블) nên hoàn thành allocation/rehash bảng mới trước khi thay pointer chính. Đây là lập luận (reasoning / 추론) gần với giao dịch (transaction / 트랜잭션): không để công khai (public / 공개) trạng thái (state / 상태) ở trạng thái nửa cũ nửa mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Tính đồng thời (concurrency / 동시성) và linearizability** tiếp nhận điểm tựa từ **Atomicity của thao tác phức hợp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Arithmetic tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đồng thời (concurrency / 동시성) và linearizability

Trong môi trường nhiều luồng, bất biến (invariant / 불변식) có thể bị phá giữa hai dòng mã (code / 코드) dù từng dòng riêng lẻ đúng.

Ví dụ:

```text
if key absent:
    insert key
```

Hai luồng thực thi (thread / 스레드) có thể cùng thấy “absent” rồi cùng insert.

Một mô hình tính đúng đắn (correctness / 정확성) quan trọng là **tính tuyến tính hóa (linearizability / 선형화 가능성)**: mỗi thao tác (operation / 연산) concurrent phải có thể được xem như xảy ra tại một thời điểm nguyên tử nào đó giữa lúc gọi và lúc trả về.

Lock-free structures còn cần bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và bộ nhớ (memory / 메모리) reclamation lập luận (reasoning / 추론). “Dùng atomic pointer” tự nó chưa chứng minh thuật toán đúng.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Arithmetic tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **Tính đồng thời (concurrency / 동시성) và linearizability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Floating-point tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Arithmetic tính đúng đắn (correctness / 정확성)

Một proof toán học có thể giả sử số nguyên vô hạn, nhưng mã (code / 코드) chạy với kiểu hữu hạn.

Ví dụ:

```java
long candidate = dist[u] + weight;
```

Nếu `dist[u]` là sentinel gần `Long.MAX_VALUE`, phép cộng có thể overflow. Trong C, signed overflow có thể dẫn tới undefined hành vi (behavior / 동작). Trong JavaScript, `Number` mất tính chính xác số nguyên sau `2^53 - 1`.

Do đó proof của hiện thực (implementation / 구현) phải bao gồm miền giá trị của kiểu số.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Floating-point tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **Arithmetic tính đúng đắn (correctness / 정확성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Validator cho cấu trúc dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Floating-point tính đúng đắn (correctness / 정확성)

Số thực máy có sai số làm tròn. So sánh equality, predicate đơn điệu hoặc comparator dựa trên epsilon tùy tiện có thể không còn bắc cầu.

Nếu comparator vi phạm transitivity, sort hoặc balanced cây (tree / 트리) có thể có hành vi không đúng đặc tả hợp đồng (contract / 계약).

Với hình học (geometry / 기하학) và numerical algorithms, biểu diễn (representation / 표현) số là một phần của specification, không phải chi tiết hiện thực (implementation / 구현).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Floating-point tính đúng đắn (correctness / 정확성)** nêu điều cần giải thích; **Validator cho cấu trúc dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Differential testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Validator cho cấu trúc dữ liệu

Cấu trúc phức tạp nên có `validate()` trong kiểm thử (test / 테스트)/gỡ lỗi (debug / 디버그).

```text
BST        -> kiểm tra cận toàn cây, không chỉ cha-con
Red-Black  -> màu, root, red-red, black-height
Heap       -> shape và heap-order
Hash Table -> trạng thái slot, count, lookup mọi entry
DSU        -> parent hợp lệ, metadata ở root
LinkedList -> size và prev/next đối xứng
```

Validator không thay proof nhưng giúp phát hiện hiện thực (implementation / 구현) phá proof ở đâu.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Validator cho cấu trúc dữ liệu** nêu điều cần giải thích; **Differential testing** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Property-based testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differential testing

Một hiện thực (implementation / 구현) chậm nhưng rõ có thể làm **oracle** cho đầu vào (input / 입력) nhỏ.

```text
range query     -> so với quét tuyến tính
shortest path   -> so với Floyd–Warshall trên graph nhỏ
Top-K           -> so với sort toàn bộ
custom BST      -> so với TreeMap/TreeSet
custom heap     -> so chuỗi pop với mảng đã sort
```

Differential testing rất hiệu quả vì nó kiểm tra hàng nghìn chuỗi thao tác mà ta khó viết tay.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Property-based testing** tiếp nhận điểm tựa từ **Differential testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adversarial tests** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Property-based testing

Thay vì chỉ kiểm tra đầu ra (output / 출력) cụ thể, có thể kiểm tra thuộc tính (property / 속성):

```text
sort(output) phải có thứ tự và cùng multiset input
push rồi pop trên stack phải khôi phục state phù hợp
union(a,b) => find(a) == find(b)
heap poll liên tục phải cho dãy không giảm
serialize rồi deserialize phải bảo toàn cấu trúc
```

Đây là cách biến specification thành kiểm thử (test / 테스트) tự động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Adversarial tests** tiếp nhận điểm tựa từ **Property-based testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proof sketch trong rà soát mã (code review / 코드 리뷰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adversarial tests

Random kiểm thử (test / 테스트) không thay thế các trường hợp (case / 사례) biên được thiết kế có chủ đích:

```text
rỗng
một phần tử
tất cả bằng nhau
đã sorted / reverse sorted
nhiều duplicate
cây cực lệch
đồ thị rời rạc
self-loop / parallel edges
giá trị sát giới hạn kiểu số
input gây nhiều hash collision
```

Một proof tốt cho biết trường hợp (case / 사례) nào nằm trong lĩnh vực (domain / 도메인) hợp lệ và trường hợp (case / 사례) nào phải bị từ chối.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Proof sketch trong rà soát mã (code review / 코드 리뷰)** tiếp nhận điểm tựa từ **Adversarial tests** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một template chứng minh có thể tái sử dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proof sketch trong rà soát mã (code review / 코드 리뷰)

Với thuật toán khó, một proof sketch ngắn thường có giá trị hơn comment từng dòng.

Ví dụ Monotonic hàng đợi (queue / 큐) cho sliding-window maximum:

```text
Invariant 1: deque chỉ chứa index còn nằm trong window.
Invariant 2: value tại các index giảm dần từ front tới back.
Khi thêm i, mọi phần tử ở back có value <= a[i] bị loại vì i mới hơn
và không nhỏ hơn, nên chúng không thể trở thành maximum trong future window.
Front vì vậy luôn là maximum hiện tại.
```

Đây là loại comment giải thích “vì sao đúng”, giúp reviewer đánh giá thay đổi thuật toán.

> **Chuyển mạch:** Ở chặng này của **Tính đúng đắn và bất biến của thuật toán**, **Một template chứng minh có thể tái sử dụng** tiếp nhận điểm tựa từ **Proof sketch trong rà soát mã (code review / 코드 리뷰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một template chứng minh có thể tái sử dụng

Khi cần chứng minh thuật toán, có thể dùng khung:

```text
1. Specification là gì?
2. Preconditions là gì?
3. State nào đang được duy trì?
4. Invariant là gì?
5. Invariant đúng lúc khởi tạo không?
6. Mỗi transition có giữ invariant không?
7. Progress measure là gì?
8. Vì sao thuật toán phải dừng?
9. Khi dừng, invariant + stop condition suy ra postcondition thế nào?
10. Numeric/runtime assumptions nào proof đang dựa vào?
```

Với greedy, thêm exchange/cut argument. Với recursion, thêm induction. Với concurrent cấu trúc (structure / 구조), thêm linearization điểm (point / 지점) và memory-order lập luận (reasoning / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đúng đắn và bất biến của thuật toán**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Một template chứng minh có thể tái sử dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

“Pass mẫu (sample / 표본) tests là đã đúng” — sai; mẫu (sample / 표본) chỉ là bằng chứng hữu hạn.

“bất biến (invariant / 불변식) đúng ở cuối là đủ” — sai; phải đúng sau initialization và được duy trì qua mọi chuyển tiếp (transition / 전이).

“Có cơ sở (base / 기반) trường hợp (case / 사례) thì recursion sẽ dừng” — sai nếu đối số không tiến gần cơ sở (base / 기반) trường hợp (case / 사례).

“Greedy hợp lý theo trực giác” — không thay exchange argument hoặc structural proof.

“Cấu trúc vẫn trả vài truy vấn (query / 쿼리) đúng nên siêu dữ liệu (metadata / 메타데이터) chắc đúng” — sai; bất biến (invariant / 불변식) có thể đã hỏng và chỉ chưa chạm trường hợp (case / 사례) lộ lỗi.

“Đã chứng minh thuật toán nên mã (code / 코드) chắc đúng” — sai; overflow, aliasing, indexing và ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) có thể làm hiện thực (implementation / 구현) khác mô hình toán học.

> **Chuyển mạch:** Trong **Tính đúng đắn và bất biến của thuật toán**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Tính đúng đắn là một chuỗi lập luận: **specification** nói phải đạt gì; **precondition** nói được giả định gì; **bất biến (invariant / 불변식)** nói điều gì luôn được bảo vệ; **progress argument** nói vì sao thuật toán sẽ dừng; trạng thái khi dừng cộng với bất biến (invariant / 불변식) phải suy ra **postcondition**.

Khi gặp một thuật toán khó, đừng đọc mã (code / 코드) từng dòng trước. Hãy hỏi: **tập ứng viên hiện tại là gì, bất biến (invariant / 불변식) nào đang được giữ, mỗi chuyển tiếp (transition / 전이) loại bỏ hay bảo toàn thông tin nào, phần nào có thể bị phá bởi mutation, và vì sao khi dừng không còn trường hợp nào chưa được xử lý?**

Xem tiếp: [Problem Modeling](./00_dsa_as_problem_modeling.md), [Complexity Analysis](./02_complexity_analysis.md), [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md), [Greedy Algorithms](../04_algorithmic_paradigms/04_greedy_algorithms.md), [Dynamic Programming](../04_algorithmic_paradigms/05_dynamic_programming.md) và [Problem Solving Workflow](../90_connections/02_problem_solving_workflow.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
