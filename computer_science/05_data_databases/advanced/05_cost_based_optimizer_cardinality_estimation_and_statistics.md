# Cost-based optimizer, cardinality estimation và statistics

SQL mô tả **what**, không buộc engine thực hiện **how**. Cùng một query có thể join theo nhiều orders, dùng index scan hoặc sequential scan, hash join hoặc nested loop. **Cost-Based Optimizer (CBO / 비용 기반 옵티마이저)** tìm plan có estimated cost thấp dựa trên statistics và cost model.

## Plan space tăng rất nhanh

Với nhiều tables, số join orders tăng combinatorially. Optimizer không thể thử mọi plan khi query lớn, nên dùng dynamic programming, heuristics hoặc search pruning.

Optimization vì thế cũng là algorithmic search problem dưới time budget.

## Cardinality là biến trung tâm

Nếu optimizer nghĩ filter trả 10 rows nhưng thực tế 10 triệu, mọi quyết định downstream có thể sai. Nested-loop join hợp lý với outer side nhỏ có thể thảm họa khi outer lớn.

**Cardinality estimation** cố dự đoán số rows sau scan/filter/join. Statistics thường gồm row count, distinct values, histograms, null fraction và correlation information.

## Independence assumption

Một lỗi phổ biến là giả định predicates độc lập. Nếu `city='Seoul'` và `country='KR'` tương quan mạnh, nhân hai selectivities như độc lập sẽ underestimate/overestimate.

Multi-column statistics giúp nhưng không thể capture mọi dependency trong dữ liệu.

## Cost model

Cost không phải milliseconds chính xác. Nó là relative model kết hợp I/O, CPU, random/sequential access và đôi khi parallelism. Hardware mới, cache state hoặc cloud storage có thể làm default constants lệch reality.

Optimizer cần model đủ tốt để rank plans, không cần tiên tri latency tuyệt đối.

## Sargability

Predicate có thể dùng index khi engine biến nó thành search condition phù hợp. Function bọc indexed column, implicit cast hoặc expression phức tạp có thể làm index khó dùng tùy DBMS.

Hiểu sargability tốt hơn việc học mẹo “index column này” vì nó giải thích optimizer có access path nào trong plan space.

## Parameter sensitivity

Prepared statement có parameter mà distribution skewed có thể cần plan khác nhau cho values khác nhau. Một plan tối ưu cho rare value không nhất thiết tốt cho hot value.

Các DBMS xử lý bằng generic/custom plans, bind peeking hoặc adaptive mechanisms khác nhau. Đây là nguồn của “query cùng SQL lúc nhanh lúc chậm”.

## Statistics stale

Data distribution thay đổi nhưng statistics cũ khiến estimator sai. Auto analyze giúp nhưng large tables, rapidly changing data và correlated columns vẫn cần diagnosis.

Khi đọc execution plan, cần so estimated rows với actual rows ở từng operator. Divergence sớm thường lan truyền xuống toàn plan.

## Optimizer và index design

Index không chỉ giảm lookup cost; nó thay plan space, ordering và join possibilities. Composite index order nên phản ánh access patterns, selectivity và required ordering, không phải quy tắc “column selective nhất luôn đứng trước”.

## Mental Model

> Query optimizer là planner ra quyết định dưới uncertainty. Statistics là perception, cardinality estimate là belief, cost model là utility function, execution plan là action. Khi plan xấu, hãy hỏi belief sai ở đâu trước khi ép hint.