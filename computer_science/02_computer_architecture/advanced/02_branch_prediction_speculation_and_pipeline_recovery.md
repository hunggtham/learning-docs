# Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Điều khiển (control / 제어) phụ thuộc (dependency / 의존성) tạo bubble** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Predictor không chỉ đoán taken/not-taken** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một chuỗi xử lý (pipeline / 파이프라인) sâu cần biết instruction tiếp theo trước khi branch điều kiện (condition / 조건) thực sự được tính. Nếu CPU chờ mọi `if`, vòng lặp (loop / 루프) và indirect lời gọi (call / 호출) resolve rồi mới fetch tiếp, front-end sẽ thường xuyên đói instruction. **Branch prediction (분기 예측)** cho phép CPU đoán điều khiển (control / 제어) luồng (flow / 흐름) và tiếp tục fetch/execute speculative.

## Điều khiển (control / 제어) phụ thuộc (dependency / 의존성) tạo bubble

Ví dụ:

```c
if (x > 0) {
    y += a;
} else {
    y += b;
}
```

Instruction xác định `x > 0` có thể cần vài stage mới ra kết quả. Trong thời gian đó, fetch đơn vị (unit / 단위) phải chọn địa chỉ tiếp theo. Không đoán thì chuỗi xử lý (pipeline / 파이프라인) dừng; đoán thì có thể tiếp tục nhưng phải chịu chi phí (cost / 비용) nếu sai.

> **Chuyển mạch:** Trong **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Predictor không chỉ đoán taken/not-taken** tiếp nhận điểm tựa từ **Điều khiển (control / 제어) phụ thuộc (dependency / 의존성) tạo bubble** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ 1-bit predictor tới history-based predictors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Predictor không chỉ đoán taken/not-taken

CPU cần trả lời ít nhất hai câu hỏi: branch có taken không, và nếu taken thì mục tiêu (target / 대상) ở đâu.

**Branch mục tiêu (target / 대상) Buffer (BTB)** bộ nhớ đệm (cache / 캐시) mục tiêu (target / 대상) của branch đã thấy trước đó. Conditional predictor dự đoán direction. Return Address ngăn xếp (stack / 스택) giúp dự đoán `return`. Indirect branch predictor xử lý lời gọi (call / 호출)/jump có nhiều mục tiêu (target / 대상) như virtual dispatch hoặc hàm (function / 함수) pointer.

Các cấu trúc này phối hợp để front-end tạo một predicted instruction stream gần như liên tục.

> **Chuyển mạch:** Ở chặng này của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Từ 1-bit predictor tới history-based predictors** tiếp nhận điểm tựa từ **Predictor không chỉ đoán taken/not-taken** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Aliasing trong predictor trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ 1-bit predictor tới history-based predictors

Predictor đơn giản nhớ lần trước branch taken hay not taken. Nhưng vòng lặp (loop / 루프) có mẫu (pattern / 패턴) như `T T T T N`, khiến predictor 1-bit sai khi vòng lặp (loop / 루프) kết thúc rồi lại sai ở lần vào vòng lặp (loop / 루프) sau.

2-bit saturating counter cần nhiều bằng chứng (evidence / 증거) hơn để đổi độ lệch (bias / 편향) và xử lý vòng lặp (loop / 루프) tốt hơn.

Predictor hiện đại còn dùng **cục bộ (local / 로컬) lịch sử (history / 이력)**, **toàn cục (global / 전역) branch lịch sử (history / 이력)** và nhiều bảng/mẫu (pattern / 패턴) components. Ý tưởng chung: hành vi (behavior / 동작) của branch hiện tại có thể tương quan với chính lịch sử của nó hoặc những branch xảy ra trước đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Aliasing trong predictor trạng thái (state / 상태)** tiếp nhận điểm tựa từ **Từ 1-bit predictor tới history-based predictors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Speculation kéo dài hơn front-end** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Aliasing trong predictor trạng thái (state / 상태)

Predictor có bộ nhớ hữu hạn. Nhiều branch khác nhau có thể map vào cùng entry và làm nhiễu trạng thái (state / 상태) của nhau. Đây gọi là aliasing/interference.

Tăng bảng (table / 테이블) kích thước (size / 크기) giảm collision nhưng tốn transistor/power. Dùng lịch sử (history / 이력) dài hơn có thể bắt mẫu (pattern / 패턴) phức tạp nhưng làm indexing/huấn luyện (training / 학습) khó hơn. Predictor thiết kế (design / 설계) là bài toán accuracy–độ trễ (latency / 지연 시간)–năng lượng (energy / 에너지).

> **Chuyển mạch:** Trong **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Speculation kéo dài hơn front-end** tiếp nhận điểm tựa từ **Aliasing trong predictor trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Misprediction khôi phục (recovery / 복구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Speculation kéo dài hơn front-end

Sau khi branch được predict, các instruction trên đường dự đoán có thể decode, rename, issue và thậm chí complete trước khi branch resolve. Chúng chỉ chưa được retire nếu vẫn speculative.

Nếu dự đoán đúng, độ trễ (latency / 지연 시간) branch gần như được che. Nếu sai, CPU phải loại bỏ công việc (work / 작업) sai và khôi phục rename/front-end trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Misprediction khôi phục (recovery / 복구)** tiếp nhận điểm tựa từ **Speculation kéo dài hơn front-end** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Branchless mã (code / 코드) không phải luôn nhanh hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Misprediction khôi phục (recovery / 복구)

Khi branch resolve khác prediction:

```text
1. phát hiện mispredict
2. xác định correct target
3. squash younger speculative instructions
4. phục hồi rename/checkpoint state
5. redirect fetch
6. refill pipeline
```

Chi phí (cost / 비용) phụ thuộc chuỗi xử lý (pipeline / 파이프라인) độ sâu (depth / 깊이), front-end width, branch resolution độ trễ (latency / 지연 시간) và lượng speculative công việc (work / 작업) đã đi xa.

Một mispredict trên CPU rộng/sâu có thể mất hàng chục cycle effective opportunity, nên mã (code / 코드) với branch khó đoán có thể chậm đáng kể dù mỗi branch instruction nhìn rất nhỏ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Branchless mã (code / 코드) không phải luôn nhanh hơn** tiếp nhận điểm tựa từ **Misprediction khôi phục (recovery / 복구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Speculation và bộ nhớ (memory / 메모리) hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Branchless mã (code / 코드) không phải luôn nhanh hơn

Có thể thay branch bằng arithmetic, conditional move hoặc véc-tơ (vector / 벡터) mask. Điều này hữu ích khi branch gần 50/50 và khó predict.

Nhưng branch predictable gần như miễn phí tương đối, trong khi branchless phiên bản (version / 버전) có thể luôn thực hiện cả hai phía hoặc tạo phụ thuộc (dependency / 의존성) dài hơn. Vì vậy “tránh branch” không phải universal tối ưu hóa (optimization / 최적화).

Cần benchmark với tải công việc (workload / 워크로드) thật và hiểu predictor hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Speculation và bộ nhớ (memory / 메모리) hierarchy** tiếp nhận điểm tựa từ **Branchless mã (code / 코드) không phải luôn nhanh hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Indirect branches khó hơn conditional branches** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Speculation và bộ nhớ (memory / 메모리) hierarchy

Instruction speculative có thể phát sinh bộ nhớ đệm (cache / 캐시) lookup, TLB lookup, prefetch-like effects hoặc tranh chấp resources dù cuối cùng bị squash. Architectural kết quả (result / 결과) bị quay lui (rollback / 롤백) nhưng **microarchitectural side effects** không nhất thiết biến mất hoàn toàn.

Đây là nền tảng lập luận (reasoning / 추론) của Spectre-class attacks: attacker lợi dụng speculative thực thi (execution / 실행) để làm thay đổi bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태) rồi suy ra secret qua timing.

Vì vậy ranh giới “speculative trạng thái (state / 상태) không lần ghi nhận (commit / 커밋)” đủ cho functional tính đúng đắn (correctness / 정확성) nhưng không tự động đủ cho bảo mật (security / 보안).

> **Chuyển mạch:** Ở chặng này của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Indirect branches khó hơn conditional branches** tiếp nhận điểm tựa từ **Speculation và bộ nhớ (memory / 메모리) hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Front-end bandwidth và instruction bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Indirect branches khó hơn conditional branches

Virtual phương thức (method / 메서드) lời gọi (call / 호출), switch bảng (table / 테이블), trình thông dịch (interpreter / 인터프리터) dispatch hoặc JIT-generated mã (code / 코드) có thể tạo indirect branches với nhiều mục tiêu (target / 대상). Predictor phải đoán mục tiêu (target / 대상) dựa lịch sử (history / 이력)/ngữ cảnh (context / 맥락).

Tải công việc (workload / 워크로드) thời gian chạy (runtime / 런타임) động có thể làm BTB/indirect predictor pressure tăng, liên hệ trực tiếp với VM/JIT hiệu năng (performance / 성능).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Front-end bandwidth và instruction bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Indirect branches khó hơn conditional branches** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ranh giới bảo mật (security boundary / 보안 경계): Spectre intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Front-end bandwidth và instruction bộ nhớ đệm (cache / 캐시)

Branch predictor accuracy chỉ là một phần. CPU còn phải cung cấp đủ instruction bytes qua I-cache, instruction TLB, decode hoặc uop bộ nhớ đệm (cache / 캐시).

Mispredict làm lãng phí front-end bandwidth và làm chuỗi xử lý (pipeline / 파이프라인) refill. mã (code / 코드) bố cục (layout / 레이아웃), hot/cold splitting và inlining có thể tác động cả predictor lẫn I-cache footprint.

> **Chuyển mạch:** Trong **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Front-end bandwidth và instruction bộ nhớ đệm (cache / 캐시)** đã nêu tiêu chí phân biệt, còn **Ranh giới bảo mật (security boundary / 보안 경계): Spectre intuition** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới bảo mật (security boundary / 보안 경계): Spectre intuition

Một mẫu (pattern / 패턴) đơn giản:

```text
if (index < length) {
    value = array[index];
}
```

Nếu predictor đã quen điều kiện (condition / 조건) true, CPU có thể speculative tải (load / 로드) với `index` ngoài bounds trước khi check resolve. Architectural kết quả (result / 결과) sẽ bị squash, nhưng bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태) phụ thuộc secret-derived truy cập (access / 접근) có thể còn lại và được đo bằng timing.

Mitigation có thể cần fencing, masking, trình biên dịch (compiler / 컴파일러) transformations hoặc thay đổi hardware predictor/speculation chính sách (policy / 정책) tùy threat mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Ranh giới bảo mật (security boundary / 보안 경계): Spectre intuition** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Branch prediction biến điều khiển (control / 제어) bất định (uncertainty / 불확실성) thành **speculative công việc (work / 작업)**. Accuracy cao giúp chuỗi xử lý (pipeline / 파이프라인) luôn có việc; misprediction cần quay lui (rollback / 롤백); bảo mật (security / 보안) phải tính cả side tác động (effect / 효과) microarchitectural chứ không chỉ trạng thái (state / 상태) đã retire.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Prediction sai chỉ chạy nhầm vài instruction rồi thôi.”** Nó có thể gây chuỗi xử lý (pipeline / 파이프라인) flush lớn và để lại microarchitectural effects.

**“Branchless luôn nhanh.”** Chỉ đúng trong một số mẫu (pattern / 패턴)/tải công việc (workload / 워크로드); predictable branches thường rất hiệu quả.

**“quay lui (rollback / 롤백) xóa mọi dấu vết.”** quay lui (rollback / 롤백) architectural trạng thái (state / 상태) không đồng nghĩa quay lui (rollback / 롤백) bộ nhớ đệm (cache / 캐시)/TLB/predictor trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Branch prediction, speculation và chuỗi xử lý (pipeline / 파이프라인) khôi phục (recovery / 복구)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Chapter này nối [OoO execution và ROB](./01_out_of_order_execution_register_renaming_and_rob.md) với roadmap về microarchitectural side channels. Ở tầng trình biên dịch (compiler / 컴파일러), profile-guided tối ưu hóa (optimization / 최적화) và mã (code / 코드) bố cục (layout / 레이아웃) có thể cải thiện branch hành vi (behavior / 동작); ở tầng bảo mật (security / 보안), speculation trở thành một attack surface.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
