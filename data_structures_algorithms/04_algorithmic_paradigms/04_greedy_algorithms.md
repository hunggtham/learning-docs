# Greedy Algorithms
**Thuật toán tham lam (Greedy / 그리디 알고리즘)**

Greedy khóa một lựa chọn local và không quay lại sửa. Local best không tự động tạo global best; greedy chỉ đúng khi có property/proof cho phép lock decision.

## Interval scheduling

Muốn chọn số intervals không overlap nhiều nhất. Rule đúng là chọn interval có finish time sớm nhất, sau đó bỏ các intervals conflict. Chọn finish sớm để lại phần timeline còn lại lớn nhất.

Exchange argument: nếu optimal solution bắt đầu bằng interval khác finish muộn hơn, thay nó bằng greedy interval không làm giảm số intervals có thể chọn phía sau. Vì vậy tồn tại optimal solution chứa greedy choice.

## Greedy có thể sai

Coin set `[1,3,4]`, target `6`. Chọn coin lớn nhất trước cho `4+1+1` = 3 coins, nhưng optimal là `3+3` = 2 coins.

Do đó “chọn cái tốt nhất trước” không phải proof.

## Greedy trong graph

Kruskal/Prim đúng nhờ cut property. Dijkstra đúng với non-negative weights vì node có tentative distance nhỏ nhất có thể được finalized an toàn.

## Greedy vs DP

Nếu local choice có thể bị future information làm regret, DP thường cần giữ nhiều states/possibilities. Greedy mạnh khi có thể chứng minh một choice là safe và không cần reconsider.

## Mental Model

> Greedy là việc khóa một quyết định local vì có proof rằng vẫn tồn tại một global optimum tương thích với quyết định đó.

## Fractional vs 0/1 knapsack

Fractional knapsack cho phép lấy một phần item. Sort theo value/weight ratio rồi lấy greedily là optimal: nếu solution dùng capacity cho ratio thấp trong khi còn item ratio cao chưa lấy hết, exchange một lượng nhỏ sẽ tăng value.

0/1 knapsack không cho chia item; exchange argument đó vỡ. Greedy theo ratio có thể sai, DP thường cần thiết.

Hai problems gần giống câu chữ nhưng constraint “được chia hay không” làm thay đổi hoàn toàn mathematical structure.

## Huffman coding

Huffman repeatedly merge hai frequencies nhỏ nhất bằng min-heap. Greedy choice được chứng minh qua structure của optimal prefix code tree: hai least-frequent symbols có thể được đặt làm sibling deepest leaves trong một optimal tree.

Kết quả tạo prefix-free variable-length code tối ưu theo expected code length cho given frequencies.

Đây là ví dụ greedy + heap + tree cùng phối hợp.

## Interval scheduling proof sketch

Gọi `g` là interval finish sớm nhất. Có optimal solution `O` chọn interval đầu `o`. Vì `finish(g) <= finish(o)`, thay `o` bằng `g` không làm giảm không gian còn lại cho subsequent intervals. Do đó tồn tại optimal solution bắt đầu bằng `g`; recurse trên phần còn lại.

Đây chính là exchange argument ở dạng rõ ràng.

## Greedy checklist về proof, không phải dấu hiệu bề mặt

Việc problem yêu cầu min/max không đủ để greedy. Cần tìm local choice và chứng minh safe bằng exchange, cut property, matroid-like structure hoặc invariant đặc thù.

Nếu không proof được rằng decision có thể khóa mà không hối tiếc, hãy nghi ngờ greedy.
