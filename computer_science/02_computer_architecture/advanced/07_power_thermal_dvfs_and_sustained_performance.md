# Power, thermal, DVFS và sustained performance

Hiệu năng của CPU/GPU không chỉ bị quyết định bởi số core, IPC hay xung nhịp tối đa được ghi trên thông số. Một hệ thống có thể benchmark rất nhanh trong vài giây đầu rồi chậm dần dù workload không đổi. Lý do là phần cứng hiện đại hoạt động dưới nhiều **constraint đồng thời**: giới hạn công suất (power limit), nhiệt độ (thermal limit), dòng điện, độ ổn định điện áp, khả năng tản nhiệt và policy của firmware/OS.

Mental model quan trọng của chapter này là:

```text
workload demand
→ activity / switching
→ power + heat generation
→ voltage/frequency operating point
→ thermal/power controller
→ DVFS / boost / throttling
→ sustained throughput + latency
```

Điều cần reasoning không phải “CPU chạy bao nhiêu GHz?”, mà là **operating point nào có thể được duy trì trong khoảng thời gian workload thực sự chạy**.

## 1. Dynamic power bắt đầu từ switching

Ở mức gần đúng, dynamic power của logic CMOS thường được reasoning bằng quan hệ:

```text
P_dynamic ∝ C × V² × f × activity
```

`C` đại diện capacitance hiệu dụng phải charge/discharge, `V` là điện áp, `f` là frequency và `activity` mô tả mức chuyển trạng thái của transistor. Công thức này không phải model đầy đủ cho mọi chip, nhưng nó giải thích một điều rất quan trọng: tăng frequency thường đòi tăng voltage để giữ timing margin, trong khi power tăng rất mạnh theo voltage.

Vì vậy “tăng clock thêm 10%” không có nghĩa chỉ trả thêm 10% năng lượng. Operating point cao có thể đẩy chip vào vùng power/thermal constraint nhanh hơn, khiến boost chỉ tồn tại ngắn.

Ngoài dynamic power còn có leakage/static power. Leakage thường tăng khi temperature và voltage tăng. Đây tạo feedback loop:

```text
nhiệt độ tăng
→ leakage tăng
→ power tăng
→ nhiệt tăng thêm
```

Controller phải phá vòng lặp này bằng giảm voltage/frequency, giới hạn activity hoặc thay đổi scheduling.

## 2. Frequency không phải tài nguyên độc lập

Một core không thể tùy ý chạy ở bất kỳ frequency nào. Hardware thường hỗ trợ tập operating points gắn frequency với voltage và các constraint vật lý. Cơ chế **Dynamic Voltage and Frequency Scaling (DVFS)** thay đổi operating point theo demand và budget.

Ở workload nhẹ, hệ thống có thể tăng frequency của một vài core để giảm latency. Khi nhiều core cùng active, tổng power tăng; frequency all-core có thể thấp hơn single-core boost. Khi vector unit hoặc accelerator hoạt động mạnh, power density và current demand có thể thay đổi thêm.

Do đó hai workload có cùng CPU utilization 100% chưa chắc có cùng frequency, power hoặc throughput. Một workload integer nhẹ và một workload SIMD/FMA dày đặc có thể tạo pressure vật lý khác nhau.

## 3. Boost là borrowing từ headroom

Turbo/boost nên được hiểu như sử dụng **headroom** đang còn trống: thermal headroom, electrical headroom và power budget. Khi chip còn lạnh và ít core active, controller có thể cho phép operating point cao hơn. Sau một thời gian, heat tích tụ trong package và cooling path; sustained limit trở thành constraint thực.

Điều này giải thích benchmark ngắn dễ gây hiểu nhầm. Nếu đo 5 giây đầu rồi suy ra capacity cho job chạy 30 phút, ta đang đo transient behavior thay vì steady state.

Một performance experiment tốt phải phân biệt:

```text
cold/transient phase
→ boost-heavy behavior

warm steady state
→ sustained operating point

thermal saturation
→ throttling / lower equilibrium
```

## 4. Thermal resistance và thermal inertia

Nhiệt không rời silicon ngay lập tức. Heat phải đi qua die, package, thermal interface, heatsink rồi ra môi trường. Hệ thống vì thế có **thermal inertia**: temperature phản ứng chậm hơn thay đổi instruction activity.

Một spike CPU ngắn có thể kết thúc trước khi package nóng đáng kể. Một workload liên tục làm nhiệt tích tụ cho tới khi heat generation gần cân bằng với heat dissipation.

Đây là lý do cùng một code có thể có latency khác nhau tùy workload trước đó. Máy vừa idle lâu có nhiều thermal headroom hơn máy vừa chạy build hoặc inference nặng.

## 5. Throttling là control action, không phải bug bí ẩn

Khi constraint bị chạm, controller giảm performance để bảo vệ invariant vật lý:

```text
temperature/current/power phải nằm trong safe envelope
```

Control action có thể là giảm frequency, giảm voltage, giới hạn boost residency hoặc thay đổi power allocation giữa CPU/GPU/accelerator. Từ góc nhìn application, symptom thường là throughput giảm hoặc tail latency tăng mà không có lock contention hay I/O bottleneck mới.

Nếu chỉ nhìn application metrics, ta dễ kết luận “code regression”. Evidence phải đi xuống hardware layer: effective frequency, package power, thermal state, throttling reason, residency state và workload mix.

## 6. Race-to-idle không phải lúc nào cũng thắng

Một intuition phổ biến là chạy thật nhanh rồi idle sẽ tiết kiệm năng lượng. **Race to idle** có thể đúng khi hoàn thành sớm giúp hệ thống vào low-power state đủ lâu. Nhưng nó không phải định luật.

Nếu frequency cao đòi voltage cao, energy per unit work có thể tăng. Nếu workload liên tục không có idle window, boost chỉ làm nhiệt tăng rồi bị throttle. Nếu memory bandwidth là bottleneck, tăng core frequency có thể tăng power mà không tăng useful throughput.

Vì vậy metric nên là:

```text
energy per useful outcome
performance per watt
latency under sustained constraint
```

chứ không chỉ peak GHz.

## 7. Memory-bound workload và power headroom

Khi CPU thường xuyên chờ DRAM, execution units không active tối đa. Workload có thể tiêu thụ ít core power hơn compute-bound workload dù wall-clock time dài. Tăng frequency trong trường hợp này thường cho diminishing return vì lower layer quyết định throughput là memory latency/bandwidth.

Ngược lại, vectorized compute có arithmetic intensity cao có thể tận dụng execution units mạnh, nhưng tạo power density lớn. Performance engineering vì thế phải nối roofline-like reasoning với power/thermal constraint: bottleneck có thể chuyển từ compute sang memory, rồi từ memory sang thermal budget tùy phase.

## 8. Heterogeneous cores và scheduling

Trong kiến trúc heterogeneous, core không đồng nhất về performance, energy efficiency và supported operating range. Scheduler phải quyết định task nào cần latency, task nào có thể chạy trên efficiency core, đồng thời tránh migration làm mất cache locality.

Một scheduler decision tốt về fairness chưa chắc tốt về energy. Ngược lại, packing task để cho một cluster ngủ có thể tiết kiệm power nhưng tăng contention ở active cores. Đây là interaction giữa OS scheduling và hardware power management; không layer nào tự mình sở hữu toàn bộ outcome.

## 9. Datacenter: power là capacity constraint

Ở quy mô fleet, giới hạn không còn chỉ là nhiệt độ một CPU. Rack, power distribution và cooling infrastructure có budget hữu hạn. Nếu mọi server cùng chạy ở peak power, facility có thể vượt design envelope.

Do đó capacity planning phải phân biệt:

```text
installed compute capacity
≠ simultaneously usable peak compute
```

Power capping có thể tăng tổng throughput của datacenter nếu cho phép đặt nhiều machine hơn trong cùng power envelope, dù từng machine chậm hơn một chút. Đây là ví dụ điển hình nơi tối ưu local peak performance làm xấu global efficiency.

## 10. Failure modes và phase changes

Power/thermal issue thường có các failure pattern sau.

**Transient benchmark illusion:** benchmark ngắn luôn chạy trong boost window, production dài hơn nên chậm.

**Thermal throttling:** throughput giảm dần theo thời gian trong khi utilization vẫn cao.

**Frequency oscillation:** controller liên tục tăng/giảm operating point, tạo latency variance.

**Power sharing:** CPU và integrated GPU/accelerator tranh cùng package budget; tăng load ở một bên làm bên kia chậm.

**Cooling degradation:** bụi, fan curve, ambient temperature hoặc thermal interface làm sustained performance giảm dù software không đổi.

**Memory-bound overclocking:** power tăng nhưng useful work gần như không tăng vì bottleneck nằm ở DRAM.

## 11. Production evidence

Không chẩn đoán DVFS bằng một metric đơn lẻ. Cần correlation theo timeline giữa:

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

Điểm quan trọng là **effective frequency** hữu ích hơn nominal/max frequency. Nếu utilization cao nhưng effective clock giảm đúng lúc package power hoặc temperature chạm limit, hypothesis thermal/power mạnh hơn hypothesis lock contention.

Nếu frequency cao nhưng IPC thấp và memory bandwidth đã saturated, bottleneck nhiều khả năng là memory path. Khi đó tăng power budget không giải quyết invariant đang giới hạn throughput.

## 12. Experiment design

Một experiment tốt cần warm-up đủ lâu để đạt steady state, giữ workload mix ổn định, ghi lại ambient/system state và so sánh cùng hardware cohort. Với laptop hoặc server có fan control, cần tránh so benchmark cold machine với warm machine.

Đối với capacity test, nên chạy đủ lâu để quan sát thermal equilibrium. Đối với latency-sensitive service, cần đo cả p50 và tail latency vì DVFS transition, scheduler migration và thermal oscillation có thể tác động tail mạnh hơn median.

## 13. Kết nối xuống và lên các layer

Chapter này nối trực tiếp với [scheduler và run queue](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [NUMA/interconnect](./04_numa_interconnects_and_scalable_coherence.md), [SIMD/GPU execution](./06_simd_vector_isa_and_gpu_execution_model.md) và [fleet profiling/cost attribution](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).

Reasoning path cần giữ là:

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

Nếu bỏ qua power/thermal layer, ta có thể giải thích đúng peak performance nhưng sai hoàn toàn sustained production performance.