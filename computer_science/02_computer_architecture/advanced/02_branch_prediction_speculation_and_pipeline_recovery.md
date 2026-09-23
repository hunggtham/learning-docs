# Branch prediction, speculation và pipeline recovery

Một pipeline sâu cần biết instruction tiếp theo trước khi branch condition thực sự được tính. Nếu CPU chờ mọi `if`, loop và indirect call resolve rồi mới fetch tiếp, front-end sẽ thường xuyên đói instruction. **Branch prediction (분기 예측)** cho phép CPU đoán control flow và tiếp tục fetch/execute speculative.

## Control dependency tạo bubble

Ví dụ:

```c
if (x > 0) {
    y += a;
} else {
    y += b;
}
```

Instruction xác định `x > 0` có thể cần vài stage mới ra kết quả. Trong thời gian đó, fetch unit phải chọn địa chỉ tiếp theo. Không đoán thì pipeline dừng; đoán thì có thể tiếp tục nhưng phải chịu cost nếu sai.

## Predictor không chỉ đoán taken/not-taken

CPU cần trả lời ít nhất hai câu hỏi: branch có taken không, và nếu taken thì target ở đâu.

**Branch Target Buffer (BTB)** cache target của branch đã thấy trước đó. Conditional predictor dự đoán direction. Return Address Stack giúp dự đoán `return`. Indirect branch predictor xử lý call/jump có nhiều target như virtual dispatch hoặc function pointer.

Các cấu trúc này phối hợp để front-end tạo một predicted instruction stream gần như liên tục.

## Từ 1-bit predictor tới history-based predictors

Predictor đơn giản nhớ lần trước branch taken hay not taken. Nhưng loop có pattern như `T T T T N`, khiến predictor 1-bit sai khi loop kết thúc rồi lại sai ở lần vào loop sau.

2-bit saturating counter cần nhiều evidence hơn để đổi bias và xử lý loop tốt hơn.

Predictor hiện đại còn dùng **local history**, **global branch history** và nhiều bảng/pattern components. Ý tưởng chung: behavior của branch hiện tại có thể tương quan với chính lịch sử của nó hoặc những branch xảy ra trước đó.

## Aliasing trong predictor state

Predictor có bộ nhớ hữu hạn. Nhiều branch khác nhau có thể map vào cùng entry và làm nhiễu state của nhau. Đây gọi là aliasing/interference.

Tăng table size giảm collision nhưng tốn transistor/power. Dùng history dài hơn có thể bắt pattern phức tạp nhưng làm indexing/training khó hơn. Predictor design là bài toán accuracy–latency–energy.

## Speculation kéo dài hơn front-end

Sau khi branch được predict, các instruction trên đường dự đoán có thể decode, rename, issue và thậm chí complete trước khi branch resolve. Chúng chỉ chưa được retire nếu vẫn speculative.

Nếu dự đoán đúng, latency branch gần như được che. Nếu sai, CPU phải loại bỏ work sai và khôi phục rename/front-end state.

## Misprediction recovery

Khi branch resolve khác prediction:

```text
1. phát hiện mispredict
2. xác định correct target
3. squash younger speculative instructions
4. phục hồi rename/checkpoint state
5. redirect fetch
6. refill pipeline
```

Cost phụ thuộc pipeline depth, front-end width, branch resolution latency và lượng speculative work đã đi xa.

Một mispredict trên CPU rộng/sâu có thể mất hàng chục cycle effective opportunity, nên code với branch khó đoán có thể chậm đáng kể dù mỗi branch instruction nhìn rất nhỏ.

## Branchless code không phải luôn nhanh hơn

Có thể thay branch bằng arithmetic, conditional move hoặc vector mask. Điều này hữu ích khi branch gần 50/50 và khó predict.

Nhưng branch predictable gần như miễn phí tương đối, trong khi branchless version có thể luôn thực hiện cả hai phía hoặc tạo dependency dài hơn. Vì vậy “tránh branch” không phải universal optimization.

Cần benchmark với workload thật và hiểu predictor behavior.

## Speculation và memory hierarchy

Instruction speculative có thể phát sinh cache lookup, TLB lookup, prefetch-like effects hoặc tranh chấp resources dù cuối cùng bị squash. Architectural result bị rollback nhưng **microarchitectural side effects** không nhất thiết biến mất hoàn toàn.

Đây là nền tảng reasoning của Spectre-class attacks: attacker lợi dụng speculative execution để làm thay đổi cache state rồi suy ra secret qua timing.

Vì vậy ranh giới “speculative state không commit” đủ cho functional correctness nhưng không tự động đủ cho security.

## Indirect branches khó hơn conditional branches

Virtual method call, switch table, interpreter dispatch hoặc JIT-generated code có thể tạo indirect branches với nhiều target. Predictor phải đoán target dựa history/context.

Workload runtime động có thể làm BTB/indirect predictor pressure tăng, liên hệ trực tiếp với VM/JIT performance.

## Front-end bandwidth và instruction cache

Branch predictor accuracy chỉ là một phần. CPU còn phải cung cấp đủ instruction bytes qua I-cache, instruction TLB, decode hoặc uop cache.

Mispredict làm lãng phí front-end bandwidth và làm pipeline refill. Code layout, hot/cold splitting và inlining có thể tác động cả predictor lẫn I-cache footprint.

## Security boundary: Spectre intuition

Một pattern đơn giản:

```text
if (index < length) {
    value = array[index];
}
```

Nếu predictor đã quen condition true, CPU có thể speculative load với `index` ngoài bounds trước khi check resolve. Architectural result sẽ bị squash, nhưng cache state phụ thuộc secret-derived access có thể còn lại và được đo bằng timing.

Mitigation có thể cần fencing, masking, compiler transformations hoặc thay đổi hardware predictor/speculation policy tùy threat model.

## Mental Model

> Branch prediction biến control uncertainty thành **speculative work**. Accuracy cao giúp pipeline luôn có việc; misprediction cần rollback; security phải tính cả side effect microarchitectural chứ không chỉ state đã retire.

## Common Misconceptions

**“Prediction sai chỉ chạy nhầm vài instruction rồi thôi.”** Nó có thể gây pipeline flush lớn và để lại microarchitectural effects.

**“Branchless luôn nhanh.”** Chỉ đúng trong một số pattern/workload; predictable branches thường rất hiệu quả.

**“Rollback xóa mọi dấu vết.”** Rollback architectural state không đồng nghĩa rollback cache/TLB/predictor state.

## Kết nối

Chapter này nối [OoO execution và ROB](./01_out_of_order_execution_register_renaming_and_rob.md) với roadmap về microarchitectural side channels. Ở tầng compiler, profile-guided optimization và code layout có thể cải thiện branch behavior; ở tầng security, speculation trở thành một attack surface.
