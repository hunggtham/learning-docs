# Power, thermal, DVFS và sustained hiệu năng (performance / 성능)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Power, thermal, DVFS và sustained hiệu năng (performance / 성능)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. động (dynamic / 동적) power bắt đầu từ switching** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Frequency không phải tài nguyên độc lập** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối power, thermal, DVFS và sustained performance, để benchmark được đọc cùng giới hạn năng lượng và nhiệt.

Hiệu năng của CPU/GPU không chỉ bị quyết định bởi số cốt lõi (core / 핵심), IPC hay xung nhịp tối đa được ghi trên thông số. Một hệ thống có thể benchmark rất nhanh trong vài giây đầu rồi chậm dần dù tải công việc (workload / 워크로드) không đổi. Lý do là phần cứng hiện đại hoạt động dưới nhiều **ràng buộc (constraint / 제약조건) đồng thời**: giới hạn công suất (power limit), nhiệt độ (thermal limit), dòng điện, độ ổn định điện áp, khả năng tản nhiệt và chính sách (policy / 정책) của firmware/OS.

Mô hình tư duy (mental model / 사고 모델) quan trọng của chapter này là:

```text
workload demand
→ activity / switching
→ power + heat generation
→ voltage/frequency operating point
→ thermal/power controller
→ DVFS / boost / throttling
→ sustained throughput + latency
```

Điều cần lập luận (reasoning / 추론) không phải “CPU chạy bao nhiêu GHz?”, mà là **operating điểm (point / 지점) nào có thể được duy trì trong khoảng thời gian tải công việc (workload / 워크로드) thực sự chạy**.

## 1. động (dynamic / 동적) power bắt đầu từ switching

Ở mức gần đúng, động (dynamic / 동적) power của lô-gic (logic / 논리) CMOS thường được lập luận (reasoning / 추론) bằng quan hệ:

```text
P_dynamic ∝ C × V² × f × activity
```

`C` đại diện capacitance hiệu dụng phải charge/discharge, `V` là điện áp, `f` là frequency và `activity` mô tả mức chuyển trạng thái của transistor. Công thức này không phải mô hình (model / 모델) đầy đủ cho mọi chip, nhưng nó giải thích một điều rất quan trọng: tăng frequency thường đòi tăng voltage để giữ timing margin, trong khi power tăng rất mạnh theo voltage.

Vì vậy “tăng clock thêm 10%” không có nghĩa chỉ trả thêm 10% năng lượng. Operating điểm (point / 지점) cao có thể đẩy chip vào vùng power/thermal ràng buộc (constraint / 제약조건) nhanh hơn, khiến boost chỉ tồn tại ngắn.

Ngoài động (dynamic / 동적) power còn có leakage/static power. Leakage thường tăng khi temperature và voltage tăng. Đây tạo vòng phản hồi (feedback loop / 피드백 루프):

```text
nhiệt độ tăng
→ leakage tăng
→ power tăng
→ nhiệt tăng thêm
```

Controller phải phá vòng lặp này bằng giảm voltage/frequency, giới hạn activity hoặc thay đổi scheduling.

Công suất động nối activity, điện áp và tần số, nên frequency không thể xem là một nút điều khiển miễn phí. DVFS chọn operating point dưới đường cong power đó; boost sử dụng phần headroom còn lại.

## 2. Frequency không phải tài nguyên độc lập

Một cốt lõi (core / 핵심) không thể tùy ý chạy ở bất kỳ frequency nào. Hardware thường hỗ trợ tập operating points gắn frequency với voltage và các ràng buộc (constraint / 제약조건) vật lý. Cơ chế **động (dynamic / 동적) Voltage and Frequency Scaling (DVFS)** thay đổi operating điểm (point / 지점) theo demand và ngân sách (budget / 예산).

Ở tải công việc (workload / 워크로드) nhẹ, hệ thống có thể tăng frequency của một vài cốt lõi (core / 핵심) để giảm độ trễ (latency / 지연 시간). Khi nhiều cốt lõi (core / 핵심) cùng active, tổng power tăng; frequency all-core có thể thấp hơn single-core boost. Khi véc-tơ (vector / 벡터) đơn vị (unit / 단위) hoặc accelerator hoạt động mạnh, power density và hiện tại (current / 현재) demand có thể thay đổi thêm.

Do đó hai tải công việc (workload / 워크로드) có cùng CPU utilization 100% chưa chắc có cùng frequency, power hoặc thông lượng (throughput / 처리량). Một tải công việc (workload / 워크로드) integer nhẹ và một tải công việc (workload / 워크로드) SIMD/FMA dày đặc có thể tạo pressure vật lý khác nhau.

DVFS ánh xạ nhu cầu tải vào một điểm frequency/voltage, nhưng điểm đó có thể chỉ là tạm thời khi nhiệt tích tụ. Vì vậy boost giống khoản vay từ thermal và electrical headroom; thermal resistance và inertia quyết định lúc phải trả lại khoản vay ấy.

## 3. Boost là borrowing từ headroom

Turbo/boost nên được hiểu như sử dụng **headroom** đang còn trống: thermal headroom, electrical headroom và power ngân sách (budget / 예산). Khi chip còn lạnh và ít cốt lõi (core / 핵심) active, controller có thể cho phép operating điểm (point / 지점) cao hơn. Sau một thời gian, heat tích tụ trong gói (package / 패키지) và cooling đường dẫn (path / 경로); sustained limit trở thành ràng buộc (constraint / 제약조건) thực.

Điều này giải thích benchmark ngắn dễ gây hiểu nhầm. Nếu đo 5 giây đầu rồi suy ra sức chứa (capacity / 용량) cho job chạy 30 phút, ta đang đo transient hành vi (behavior / 동작) thay vì steady trạng thái (state / 상태).

Một hiệu năng (performance / 성능) experiment tốt phải phân biệt:

```text
cold/transient phase
→ boost-heavy behavior

warm steady state
→ sustained operating point

thermal saturation
→ throttling / lower equilibrium
```

Thời gian boost phụ thuộc tốc độ nhiệt truyền tới package và cooling path. Khi thermal state vượt envelope, throttling là hành động của controller để giữ invariant vật lý an toàn.

## 4. Thermal resistance và thermal inertia

Nhiệt không rời silicon ngay lập tức. Heat phải đi qua die, gói (package / 패키지), thermal giao diện (interface / 인터페이스), heatsink rồi ra môi trường. Hệ thống vì thế có **thermal inertia**: temperature phản ứng chậm hơn thay đổi instruction activity.

Một spike CPU ngắn có thể kết thúc trước khi gói (package / 패키지) nóng đáng kể. Một tải công việc (workload / 워크로드) liên tục làm nhiệt tích tụ cho tới khi heat generation gần cân bằng với heat dissipation.

Đây là lý do cùng một mã (code / 코드) có thể có độ trễ (latency / 지연 시간) khác nhau tùy tải công việc (workload / 워크로드) trước đó. Máy vừa idle lâu có nhiều thermal headroom hơn máy vừa chạy bản dựng (build / 빌드) hoặc suy luận (inference / 추론) nặng.

Throttling chuyển bằng chứng về nhiệt hoặc power thành một operating point thấp hơn. Điểm thấp hơn có thể làm giảm throughput, nhưng cũng thay đổi energy cost để hoàn tất công việc; race-to-idle phải được đánh giá dưới sustained constraint đó.

## 5. Throttling là điều khiển (control / 제어) hành động (action / 동작), không phải bug bí ẩn

Khi ràng buộc (constraint / 제약조건) bị chạm, controller giảm hiệu năng (performance / 성능) để bảo vệ bất biến (invariant / 불변식) vật lý:

```text
temperature/current/power phải nằm trong safe envelope
```

Điều khiển (control / 제어) hành động (action / 동작) có thể là giảm frequency, giảm voltage, giới hạn boost residency hoặc thay đổi power allocation giữa CPU/GPU/accelerator. Từ góc nhìn ứng dụng (application / 애플리케이션), symptom thường là thông lượng (throughput / 처리량) giảm hoặc tail độ trễ (latency / 지연 시간) tăng mà không có tranh chấp khóa (lock contention / 잠금 경합) hay I/O bottleneck mới.

Nếu chỉ nhìn ứng dụng (application / 애플리케이션) metrics, ta dễ kết luận “mã (code / 코드) regression”. bằng chứng (evidence / 증거) phải đi xuống hardware tầng (layer / 계층): effective frequency, gói (package / 패키지) power, thermal trạng thái (state / 상태), throttling reason, residency trạng thái (state / 상태) và tải công việc (workload / 워크로드) mix.

Race-to-idle chỉ có ích khi frequency cao rút ngắn công việc đủ để tạo một khoảng idle có giá trị. Nếu memory bandwidth là bottleneck, frequency thêm chỉ tiêu hao headroom mà không mua được useful throughput; khi đó phải xét phase của workload và power pressure.

## 6. Race-to-idle không phải lúc nào cũng thắng

Một intuition phổ biến là chạy thật nhanh rồi idle sẽ tiết kiệm năng lượng. **Race to idle** có thể đúng khi hoàn thành sớm giúp hệ thống vào low-power trạng thái (state / 상태) đủ lâu. Nhưng nó không phải định luật.

Nếu frequency cao đòi voltage cao, năng lượng (energy / 에너지) per đơn vị (unit / 단위) công việc (work / 작업) có thể tăng. Nếu tải công việc (workload / 워크로드) liên tục không có idle cửa sổ (window / 윈도우), boost chỉ làm nhiệt tăng rồi bị throttle. Nếu bộ nhớ (memory / 메모리) bandwidth là bottleneck, tăng cốt lõi (core / 핵심) frequency có thể tăng power mà không tăng useful thông lượng (throughput / 처리량).

Vì vậy chỉ số (metric / 지표) nên là:

```text
energy per useful outcome
performance per watt
latency under sustained constraint
```

chứ không chỉ peak GHz.

Race-to-idle phụ thuộc compute hay memory đang giới hạn tiến độ. Workload memory-bound có thể bỏ trống compute headroom nhưng vẫn chạy lâu; khi đó heterogeneous cores và scheduler placement quyết định công việc nên chạy ở đâu.

## 7. Memory-bound tải công việc (workload / 워크로드) và power headroom

Khi CPU thường xuyên chờ DRAM, thực thi (execution / 실행) units không active tối đa. tải công việc (workload / 워크로드) có thể tiêu thụ ít cốt lõi (core / 핵심) power hơn compute-bound tải công việc (workload / 워크로드) dù wall-clock thời gian (time / 시간) dài. Tăng frequency trong trường hợp này thường cho diminishing return vì lower tầng (layer / 계층) quyết định thông lượng (throughput / 처리량) là bộ nhớ (memory / 메모리) độ trễ (latency / 지연 시간)/bandwidth.

Ngược lại, vectorized compute có arithmetic intensity cao có thể tận dụng thực thi (execution / 실행) units mạnh, nhưng tạo power density lớn. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) vì thế phải nối roofline-like lập luận (reasoning / 추론) với power/thermal ràng buộc (constraint / 제약조건): bottleneck có thể chuyển từ compute sang bộ nhớ (memory / 메모리), rồi từ bộ nhớ (memory / 메모리) sang thermal ngân sách (budget / 예산) tùy phase.

Scheduler placement biến workload và power headroom thành lựa chọn của toàn hệ thống: core nhanh có thể giảm latency, còn efficiency core có thể giữ budget. Ở quy mô fleet, cùng budget đó trở thành datacenter capacity thay vì policy của một core.

## 8. Heterogeneous cores và scheduling

Trong kiến trúc heterogeneous, cốt lõi (core / 핵심) không đồng nhất về hiệu năng (performance / 성능), năng lượng (energy / 에너지) efficiency và supported operating phạm vi (range / 범위). Scheduler phải quyết định tác vụ (task / 작업) nào cần độ trễ (latency / 지연 시간), tác vụ (task / 작업) nào có thể chạy trên efficiency cốt lõi (core / 핵심), đồng thời tránh di chuyển (migration / 마이그레이션) làm mất bộ nhớ đệm (cache / 캐시) locality.

Một scheduler quyết định (decision / 결정) tốt về fairness chưa chắc tốt về năng lượng (energy / 에너지). Ngược lại, packing tác vụ (task / 작업) để cho một cluster ngủ có thể tiết kiệm power nhưng tăng contention ở active cores. Đây là tương tác (interaction / 상호작용) giữa OS scheduling và hardware power management; không tầng (layer / 계층) nào tự mình sở hữu toàn bộ kết quả (outcome / 결과).

Heterogeneous scheduling tối ưu một máy dưới power envelope dùng chung. Datacenter thêm rack, cooling và concurrency; vì vậy lựa chọn cục bộ có thể tạo capacity failure toàn cục và làm service behavior đổi phase.

## 9. Datacenter: power là sức chứa (capacity / 용량) ràng buộc (constraint / 제약조건)

Ở quy mô fleet, giới hạn không còn chỉ là nhiệt độ một CPU. Rack, power phân phối (distribution / 분포) và cooling hạ tầng (infrastructure / 인프라) có ngân sách (budget / 예산) hữu hạn. Nếu mọi máy chủ (server / 서버) cùng chạy ở peak power, facility có thể vượt thiết kế (design / 설계) envelope.

Do đó sức chứa (capacity / 용량) planning phải phân biệt:

```text
installed compute capacity
≠ simultaneously usable peak compute
```

Power capping có thể tăng tổng thông lượng (throughput / 처리량) của datacenter nếu cho phép đặt nhiều machine hơn trong cùng power envelope, dù từng machine chậm hơn một chút. Đây là ví dụ điển hình nơi tối ưu cục bộ (local / 로컬) peak hiệu năng (performance / 성능) làm xấu toàn cục (global / 전역) efficiency.

Capacity planning làm lộ transient boost illusion, thermal throttling, power sharing và cooling degradation như các failure mode khác nhau. Để phân biệt, production evidence phải đối chiếu effective frequency, power, temperature và workload theo thời gian.

## 10. thất bại (failure / 실패) modes và phase changes

Power/thermal issue thường có các thất bại (failure / 실패) mẫu (pattern / 패턴) sau.

**Transient benchmark illusion:** benchmark ngắn luôn chạy trong boost cửa sổ (window / 윈도우), môi trường vận hành (production / 운영 환경) dài hơn nên chậm.

**Thermal throttling:** thông lượng (throughput / 처리량) giảm dần theo thời gian trong khi utilization vẫn cao.

**Frequency oscillation:** controller liên tục tăng/giảm operating điểm (point / 지점), tạo độ trễ (latency / 지연 시간) variance.

**Power sharing:** CPU và integrated GPU/accelerator tranh cùng gói (package / 패키지) ngân sách (budget / 예산); tăng tải (load / 로드) ở một bên làm bên kia chậm.

**Cooling degradation:** bụi, fan curve, ambient temperature hoặc thermal giao diện (interface / 인터페이스) làm sustained hiệu năng (performance / 성능) giảm dù software không đổi.

**Memory-bound overclocking:** power tăng nhưng useful công việc (work / 작업) gần như không tăng vì bottleneck nằm ở DRAM.

Failure mode là hypothesis phụ thuộc thời gian, không phải nhãn dán cho một lần chạy chậm. Production evidence kiểm tra chúng bằng cách đặt application latency cạnh requested/effective frequency, power-limit reason, thermal state và placement; controlled experiment sau đó mới cô lập được nguyên nhân.

## 11. bằng chứng vận hành (production evidence / 운영 증거)

Không chẩn đoán DVFS bằng một chỉ số (metric / 지표) đơn lẻ. Cần correlation theo timeline giữa:

```text
request/job throughput và latency
CPU/GPU utilization
requested vs effective frequency
package/device power
thermal sensors
throttling / power-limit reasons
memory bandwidth / cache miss evidence
scheduler placement
ambient hoặc cooling state nếu có
```

Điểm quan trọng là **effective frequency** hữu ích hơn nominal/max frequency. Nếu utilization cao nhưng effective clock giảm đúng lúc gói (package / 패키지) power hoặc temperature chạm limit, hypothesis thermal/power mạnh hơn hypothesis tranh chấp khóa (lock contention / 잠금 경합).

Nếu frequency cao nhưng IPC thấp và bộ nhớ (memory / 메모리) bandwidth đã saturated, bottleneck nhiều khả năng là bộ nhớ (memory / 메모리) đường dẫn (path / 경로). Khi đó tăng power ngân sách (budget / 예산) không giải quyết bất biến (invariant / 불변식) đang giới hạn thông lượng (throughput / 처리량).

Evidence chỉ trở nên hữu ích khi experiment kiểm soát warm-up, workload mix, hardware cohort và điều kiện môi trường. Số đo sustained thu được có thể nối ngược về owner của scheduler, NUMA, SIMD và fleet cost.

## 12. Experiment thiết kế (design / 설계)

Một experiment tốt cần warm-up đủ lâu để đạt steady trạng thái (state / 상태), giữ tải công việc (workload / 워크로드) mix ổn định, ghi lại ambient/hệ thống (system / 시스템) trạng thái (state / 상태) và so sánh cùng hardware cohort. Với laptop hoặc máy chủ (server / 서버) có fan điều khiển (control / 제어), cần tránh so benchmark cold machine với warm machine.

Đối với sức chứa (capacity / 용량) kiểm thử (test / 테스트), nên chạy đủ lâu để quan sát thermal equilibrium. Đối với latency-sensitive dịch vụ (service / 서비스), cần đo cả p50 và tail độ trễ (latency / 지연 시간) vì DVFS chuyển tiếp (transition / 전이), scheduler di chuyển (migration / 마이그레이션) và thermal oscillation có thể tác động tail mạnh hơn median.

Experiment khép vòng từ workload demand tới sustained behavior có thể đo được. Các kết nối cuối đặt vòng đó qua scheduler, memory topology, accelerator execution và fleet capacity, thay vì quy mọi slowdown cho riêng code.

## 13. Kết nối xuống và lên các tầng (layer / 계층)

Chapter này nối trực tiếp với [scheduler và run queue](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [NUMA/interconnect](./04_numa_interconnects_and_scalable_coherence.md), [SIMD/GPU execution](./06_simd_vector_isa_and_gpu_execution_model.md) và [fleet profiling/cost attribution](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).

Lập luận (reasoning / 추론) đường dẫn (path / 경로) cần giữ là:

```text
application demand
→ instruction/memory activity
→ microarchitectural utilization
→ power generation
→ thermal/electrical constraint
→ DVFS control action
→ scheduler/runtime-visible performance
→ service SLO và cost
```

Nếu bỏ qua power/thermal tầng (layer / 계층), ta có thể giải thích đúng peak hiệu năng (performance / 성능) nhưng sai hoàn toàn sustained môi trường vận hành (production / 운영 환경) hiệu năng (performance / 성능).

> **Bàn giao:** Sau **13. Kết nối xuống và lên các tầng (layer / 계층)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
