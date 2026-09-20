# Recursion và Backtracking
**Đệ quy và quay lui / 재귀와 백트래킹**

Recursion mô tả một problem bằng phiên bản nhỏ hơn của chính nó. Backtracking dùng recursion/stack để explore decision tree, rồi hoàn tác lựa chọn nếu branch không phù hợp.

## Recursive contract

Một recursion đúng cần base case, recursive case tiến gần base case và state đủ mô tả subproblem. Tree traversal là ví dụ tự nhiên hơn factorial vì tree tự mang recursive shape.

## Backtracking là DFS trên implicit state tree

Permutations:

```js
function permutations(nums) {
  const ans = [], path = [];
  const used = Array(nums.length).fill(false);

  function dfs() {
    if (path.length === nums.length) {
      ans.push([...path]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.push(nums[i]);
      dfs();
      path.pop();
      used[i] = false;
    }
  }
  dfs();
  return ans;
}
```

`path.push` là choose, recursive call là explore, `path.pop` là undo.

## Pruning

Nếu partial state đã vi phạm constraint, không cần generate descendants. N-Queens có thể giữ sets/bitmasks của columns và diagonals để reject invalid placements ngay.

Pruning không thay worst-case exponential nature trong mọi problem, nhưng có thể giảm search space thực tế rất lớn.

## Khi backtracking chuyển thành DP

Nếu nhiều histories khác nhau dẫn tới cùng state và future từ state đó giống nhau, việc giải lặp lại là waste. Memoization cache result theo state và biến search tree thành state graph được reuse.

## Recursion depth

C, Java và JavaScript đều có stack limit thực tế. Deep tree/graph có thể cần explicit stack. JavaScript đặc biệt không nên giả định tail-call optimization portable.

## Mental Model

> Backtracking = chọn → khám phá → hoàn tác. Nếu cùng state xuất hiện lại từ nhiều đường, hãy nghĩ tới memoization/DP.

## Subsets và decision tree

Mỗi element có hai choices: include hoặc exclude. Depth `n`, branching factor 2, nên có `2^n` leaves.

```java
void subsets(int i, int[] a, List<Integer> cur) {
    if (i == a.length) {
        output(cur);
        return;
    }

    subsets(i + 1, a, cur);

    cur.add(a[i]);
    subsets(i + 1, a, cur);
    cur.remove(cur.size() - 1);
}
```

Order include/exclude không ảnh hưởng completeness, nhưng pruning heuristics có thể ảnh hưởng performance lớn.

## Combination generation và duplicate control

Nếu input có duplicate values, sorting trước rồi skip equal choices ở **cùng recursion depth** tránh duplicate combinations. Skip sai level có thể loại legitimate reuse/path. Vì vậy rule phải xuất phát từ definition “hai branches này có tạo cùng choice set tại state hiện tại không?”.

## Constraint propagation

Sudoku/N-Queens nhanh hơn nhiều nếu state lưu available candidates bằng bitsets/sets thay vì mỗi lần scan toàn board. Backtracking performance phụ thuộc cost check và pruning quality, không chỉ recursion syntax.

## Choose-constrain-explore-unchoose

Một template tốt:

```text
choose candidate
apply constraints / mutate state
recurse
undo exactly mutations
```

Undo phải đối xứng hoàn toàn. Nếu recursion return sớm, cần bảo đảm state được restore hoặc dùng immutable/copy semantics có chủ đích.

## Branch ordering

Nếu muốn tìm một solution nhanh, thử candidate “có khả năng fail sớm” thường giúp pruning. Constraint satisfaction gọi idea này minimum remaining values: chọn variable ít candidates nhất trước.

Algorithm worst-case vẫn exponential, nhưng search tree thực tế có thể nhỏ đi rất nhiều.
