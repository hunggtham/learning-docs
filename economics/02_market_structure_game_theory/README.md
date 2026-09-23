# 02 — Market Structure & Game Theory

**Trạng thái: roadmap / bản phác thảo chưa hoàn chỉnh.** File này đã có skeleton cơ chế cho các topic chính, nhưng chưa phải một module hoàn tất: cần bổ sung derivation có kiểm soát, worked examples, empirical evidence, policy boundary và links đầy đủ tới welfare/econometrics.

Market structure mô tả constraint mà firm đối mặt; game theory mô tả cách payoff của một tác nhân phụ thuộc vào hành động của tác nhân khác. Hai lớp nối nhau qua câu hỏi: market power đến từ đâu, hành động nào là best response, equilibrium nào tồn tại, và outcome khác benchmark cạnh tranh ra sao?

## Coverage roadmap

### 1. Perfect competition

Nhiều seller/buyer, sản phẩm đồng nhất, entry/exit và price-taking tạo benchmark trong đó firm chọn output tại `P = MC` trong vùng marginal cost tăng. Cần luôn nêu rõ đây là benchmark với assumptions mạnh, không phải mô tả mặc định của mọi thị trường.

### 2. Monopoly

Monopolist chọn output tại `MR = MC`, sau đó lấy price trên demand curve; welfare analysis phải tách consumer surplus, producer surplus, transfer và deadweight loss. Natural monopoly cần thêm cost structure, fixed cost và trade-off giữa price-at-MC, price-at-AC, subsidy và regulation.

### 3. Oligopoly

Cournot (quantity), Bertrand (price), differentiation, capacity, timing, cost asymmetry và information có thể cho các kết quả khác nhau. Không tồn tại một công thức “oligopoly price” độc lập với strategic environment.

### 4. Strategic interaction

Best response là mapping từ hành động của đối thủ tới hành động tối ưu của firm; Nash equilibrium là fixed point của các best responses, không đồng nghĩa với socially optimal. Cần nối simultaneous/sequential move, credible commitment, entry/exit và subgame-perfect reasoning. Threat chỉ có tác dụng nếu credible tại node thật sự xảy ra; backward induction giúp loại các threat không tối ưu nếu deviation xảy ra.

### 5. Repeated games

Lặp lại interaction có thể hỗ trợ cooperation, punishment hoặc price war, nhưng sustainability phụ thuộc discount factor, observability, deviation detection và commitment. Không gọi mọi hành vi lặp lại là collusion nếu chưa tách equilibrium, coordination, explicit agreement và evidence.

### 6. Auctions

Rule phân bổ và payment định hình incentive. First-price khiến bidder trade-off bid cao với surplus; second-price chỉ tạo truth-telling trong private-value setting và assumptions phù hợp. Common-value auction có winner’s curse, nên first-price, second-price và mọi auction khác phải được đọc cùng information structure, risk attitude và khả năng collusion.

### 7. Mechanism design

Mechanism design đi ngược từ social objective và incentive constraints để thiết kế rule. “Truthful” chỉ là kết luận trong một domain/type/budget/coalition cụ thể; cần nêu cả participation, budget và collusion assumptions, không coi đó là guarantee phổ quát.

## Checklist hoàn thiện module

Mỗi topic cần trả lời: market power hoặc strategic dependency được đo thế nào; state, choice và institutional constraint là gì; equilibrium nào được chọn và equilibrium khác có tồn tại không; welfare được phân phối cho ai; prediction nào kiểm tra được bằng dữ liệu; shock, entry, regulation hoặc information change làm kết luận đổi ra sao. Sau khi hoàn thiện, module này sẽ nối sang Industrial Organization trong Applied Economics và sang Econometrics để kiểm tra market-power claims.

Đọc trước: [01 — Microeconomics](../01_microeconomics/README.md), [00 — Economic reasoning](../00_foundations/00_economic_reasoning.md). Đọc tiếp theo route chung: [Economics README](../README.md).
