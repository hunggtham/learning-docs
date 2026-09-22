# BGP, routing policy, convergence và route security

Đọc trước phần foundation về IP/routing và BGP trong [`basic/06_networks_distributed_systems`](../../basic/06_networks_distributed_systems/), cùng [TCP/UDP và congestion](../../basic/06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md). Chapter này không học BGP như danh sách message type; mục tiêu là reasoning production khi **control plane quyết định route nào tồn tại, data plane forward theo route đó, policy giữa các Autonomous Systems (AS) thay đổi path, và failure có thể lan ra Internet dù từng router riêng lẻ vẫn hoạt động**.

Mental model:

```text
prefix ownership / reachability
→ route advertisement
→ policy + path selection
→ RIB
→ best routes installed into FIB
→ packet forwarding
→ observation from endpoints
```

## 1. Routing có control plane và data plane

**Control plane** học và chọn reachability. **Data plane** dùng forwarding table để chuyển packet ở tốc độ cao.

BGP chủ yếu là control-plane protocol. Khi BGP session thay đổi, router không “forward packet bằng BGP message”; nó recompute routes rồi cập nhật FIB hoặc equivalent hardware/software forwarding state.

Vì vậy sự cố có thể tồn tại ở ba lớp khác nhau:

```text
route không được học
route được học nhưng policy chọn path khác
route được chọn nhưng FIB/data plane không forward như mong đợi
```

## 2. Prefix và AS là hai abstraction khác nhau

IP prefix mô tả vùng địa chỉ. Autonomous System là domain quản trị routing có policy riêng. Một AS có thể originate nhiều prefixes; một prefix có thể được quảng bá qua nhiều upstreams.

BGP path-vector mang thông tin reachability và AS path. Nhưng mục tiêu không phải tìm “đường ngắn nhất toàn Internet” theo latency. Mỗi network áp policy kinh tế/kỹ thuật riêng.

Đây là invariant xã hội-kỹ thuật quan trọng: **global routing emergent từ policy local**, không từ một optimizer trung tâm.

## 3. eBGP và iBGP giải hai boundary khác nhau

External BGP trao routes giữa ASes. Internal BGP phân phối external reachability bên trong một AS lớn. IGP như OSPF/IS-IS thường giải reachability nội bộ tới next hop; BGP giữ policy/inter-domain path.

Một route có thể hợp lệ ở BGP layer nhưng next-hop nội bộ unreachable vì IGP/FIB issue. Vì vậy debugging phải tách BGP control state khỏi underlay reachability.

## 4. Best-path không đồng nghĩa shortest AS_PATH

AS_PATH là một signal quan trọng và giúp loop prevention, nhưng policy attributes có thể ưu tiên business relationship hoặc traffic engineering trước độ dài path.

Các implementation thường có concept như local preference, origin/path attributes, MED và tie-breakers. Chi tiết order khác ecosystem/vendor/version; mental model bền là:

```text
import policy
→ preference class
→ path characteristics
→ tie-break
→ best route
```

Không nên nhìn AS_PATH ngắn hơn rồi kết luận route đó chắc chắn được chọn.

## 5. Import/export policy quyết định Internet mà neighbor nhìn thấy

Router không nhất thiết quảng bá mọi route nó biết cho mọi neighbor. Export policy phản ánh relationship như customer/provider/peer và security controls.

Một cấu hình export sai có thể biến AS thành transit ngoài ý muốn hoặc leak routes học từ một provider sang provider khác. Vì vậy route leak thường là policy failure, không phải packet corruption.

## 6. RIB và FIB phải được phân biệt

Routing Information Base (RIB) giữ candidate/best routing state ở control plane. Forwarding Information Base (FIB) là state tối ưu cho packet lookup.

Nếu control plane hội tụ nhưng FIB programming thất bại/chậm, operator có thể thấy BGP route “đúng” mà traffic vẫn drop/blackhole.

Production evidence cần kiểm tra cả hai khi platform hỗ trợ.

## 7. Withdrawal và convergence tạo một khoảng thời gian bất định

Khi link/node/path hỏng, route withdrawal lan qua neighbors. Mỗi AS recompute theo policy rồi quảng bá state mới. Trong khoảng convergence, các vantage points khác nhau có thể thấy paths khác nhau.

Do đó Internet routing không có instant atomic update. Một failure có thể biểu hiện transient loss, path stretch hoặc asymmetric reachability trước khi ổn định.

Liveness của routing là eventual convergence; safety cần tránh loop/invalid reachability trong quá trình chuyển trạng thái.

## 8. Path exploration làm convergence tốn thời gian hơn một lần recompute

Sau khi path tốt nhất biến mất, routers có thể thử các alternatives rồi lần lượt nhận withdrawals mới. Control plane có thể “khám phá” nhiều path trước khi ổn định.

Route flap damping và policy suppression từng được dùng để giảm churn nhưng có thể kéo dài outage nếu suppress reachability hợp lệ. Đây là ví dụ điển hình của control chống instability nhưng có availability trade-off.

## 9. Route aggregation giảm state nhưng mở rộng failure blast radius

Aggregating nhiều specific prefixes thành supernet giảm routing-table size. Nhưng nếu aggregate vẫn được advertise khi một subprefix phía sau không reachable, traffic có thể đi vào AS rồi blackhole.

Do đó aggregate thường cần discard/null route hoặc reachability condition thích hợp để tránh loop. Aggregation là compression của routing state, và như mọi compression, nó làm mất chi tiết.

## 10. More-specific route thường thắng data-plane lookup

Longest-prefix match nghĩa route `/24` thường được ưu tiên hơn covering `/16` ở forwarding lookup. Vì vậy accidental hoặc malicious more-specific announcement có thể hút traffic khỏi origin rộng hơn nếu được Internet chấp nhận.

Đây là cơ chế nền của nhiều route hijack scenario: không cần “hack router của nạn nhân”; chỉ cần invalid reachability được propagated và selected.

## 11. Route leak và route hijack không hoàn toàn giống nhau

**Route leak** thường là route hợp lệ về origin/reachability nhưng được export qua relationship không nên export, tạo path policy bất thường.

**Route hijack** thường chỉ việc một AS originate/propagate prefix không được phép hoặc làm Internet chọn origin/path sai.

Từ endpoint, cả hai có thể trông như path đổi, latency tăng, traffic mất hoặc đi qua network lạ. Phân loại cần control-plane evidence.

## 12. RPKI origin validation bảo vệ một phần invariant

Resource Public Key Infrastructure (RPKI) cho phép publish Route Origin Authorization (ROA), nói AS nào được phép originate prefix với max length nhất định.

Router có thể classify route origin validation thành valid/invalid/not-found và áp policy tương ứng.

RPKI giúp chống nhiều origin hijack nhưng **không chứng minh toàn bộ AS path hợp lệ** và không tự ngăn mọi route leak. Security control phải được hiểu đúng scope.

## 13. Prefix filtering và max-prefix là containment controls

Neighbor policy có thể chỉ chấp nhận prefixes/AS paths phù hợp expectation. Max-prefix limit giúp ngăn một peer/customer vô tình đẩy hàng trăm nghìn routes làm control-plane/resource pressure.

Nhưng fail-closed mạnh quá có thể cắt legitimate traffic khi network tăng prefix count. Vì vậy threshold cần operational governance, không chỉ cấu hình một lần.

## 14. Communities là metadata policy, không phải routing guarantee

BGP communities cho phép gắn metadata để upstream/downstream áp action như preference, export scope hoặc blackholing. Semantics phụ thuộc agreement giữa networks.

Một community có ý nghĩa trong contract cụ thể, không phải global invariant. Khi debug phải biết ai set nó, ở boundary nào, và policy nào consume nó.

## 15. Anycast dựa vào routing để đưa cùng IP tới nhiều sites

Nhiều locations có thể advertise cùng prefix. Internet policy chọn path tới một site “gần” theo routing, không nhất thiết theo geographic distance.

Anycast cải thiện latency/resilience nhưng session/stateful behavior trở nên nhạy với route change. Khi path flips, request sau có thể tới site khác. Application layer cần thiết kế state, retry và idempotency phù hợp.

## 16. Asymmetric routing là bình thường hơn nhiều người nghĩ

Forward path và return path có thể đi qua ASes khác nhau do policy độc lập. Firewall/stateful middlebox assumptions có thể hỏng nếu topology yêu cầu symmetry.

Traceroute từ A tới B không mô tả reverse path. Debugging one-way loss cần vantage point hai phía hoặc telemetry trung gian.

## 17. ECMP phân phối traffic nhưng hash tạo hidden skew

Equal-Cost Multi-Path có thể hash flow theo 5-tuple hoặc fields khác. Tổng bandwidth còn dư nhưng một subset flows có thể dồn vào một member path nóng.

Một elephant flow không được chia nếu hash per-flow. Link utilization trung bình vì vậy có thể che micro-hotspot và packet loss trên một member.

## 18. BGP session health không chứng minh application reachability

TCP session BGP có thể `Established`, routes có thể present, nhưng packet vẫn fail do ACL, MTU, FIB, tunnel, congestion, next-hop reachability hoặc remote application.

Ngược lại, application có thể vẫn hoạt động trong lúc control-plane session flap nhờ stale/graceful-restart forwarding state tùy design.

Status ở một layer không thay proof ở layer khác.

## 19. Production evidence cần dựng lại route decision theo thời gian

Một incident routing tốt cần biết:

```text
prefix nào bị ảnh hưởng?
origin AS/path trước và sau là gì?
advertisement/withdrawal xuất hiện lúc nào?
neighbor nào học route nào?
import/export policy nào áp dụng?
RIB chọn gì?
FIB install gì?
packet loss/latency/path từ nhiều vantage points ra sao?
```

Looking glass, route collector, router telemetry, flow logs, packet counters và endpoint probes là các nguồn evidence khác nhau. Không nguồn nào một mình là “sự thật toàn Internet”.

## 20. Worked incident: more-specific route xuất hiện

Giả sử service prefix `203.0.112.0/20` bình thường originate từ AS A. Đột nhiên một AS B announce `203.0.113.0/24` và nhiều networks chấp nhận.

Endpoint trong `/24` đi theo B do longest-prefix match. BGP session của A vẫn healthy; phần còn lại `/20` vẫn normal. Nếu chỉ nhìn overall service availability, incident có thể trông regional/random.

Diagnosis cần prefix-level reachability và route-origin history. Containment có thể liên quan route filtering/RPKI/coordination với upstream; application retry không sửa authority của routing control plane.

## 21. Convergence pressure có thể trở thành CPU/memory pressure

Mass route churn tạo update storms, policy evaluation load, RIB/FIB programming pressure và telemetry volume. Control plane có thể chậm hơn đúng lúc network đang cần hội tụ nhanh.

Đây là feedback loop:

```text
failure/churn
→ route updates ↑
→ control-plane load ↑
→ convergence slower
→ inconsistency window kéo dài
```

Capacity planning cho router/control-plane state vì vậy là reliability concern.

## 22. Kết nối sang các chapter khác

BGP/routing nối trực tiếp với [HTTP/2, HTTP/3 và QUIC](../../basic/06_networks_distributed_systems/08_http2_http3_quic_and_modern_transport.md), [multi-region replication](./05_multi_region_replication_and_geo_distributed_tradeoffs.md), [load balancing/locality](../../08_software_systems/advanced/03_load_balancing_connection_pools_and_locality.md) và [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

Mental model cuối cùng: **routing incident phải được debug như một distributed policy state machine: advertisement → policy → selected route → forwarding state → observed traffic, không phải chỉ như “mạng chậm”.**