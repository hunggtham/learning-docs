# Routing protocols và Internet

Biết subnetting chưa đủ để hiểu Internet. Router cần học **đường nào dẫn tới prefix nào**, và ở quy mô toàn cầu không một controller duy nhất biết/tin mọi thứ. Routing protocols chia bài toán thành routing nội bộ một administrative domain và routing giữa các autonomous systems.

## Forwarding khác routing

Forwarding là per-packet operation: nhìn destination address, chọn next hop/output interface từ forwarding table.

Routing là control-plane process xây/cập nhật thông tin để forwarding table tồn tại.

Tách data plane và control plane giúp reasoning: packet forwarding phải rất nhanh; route computation có thể phức tạp hơn và xảy ra ít thường xuyên hơn.

## Longest Prefix Match

Nếu table có routes `10.0.0.0/8` và `10.1.0.0/16`, destination `10.1.2.3` chọn `/16` vì prefix cụ thể hơn.

Hardware routers có thể dùng TCAM/trie-like structures để lookup tốc độ cao. Đây là connection trực tiếp với prefix data structures.

## Distance-vector intuition

Distance-vector protocols trao đổi với neighbors “tôi biết destination X cách bao nhiêu”. Bellman–Ford style relaxation cập nhật route từ neighbor advertisements.

Problem như count-to-infinity xuất hiện khi topology failure lan chậm. Split horizon/poison reverse là mitigation trong một số protocols.

## Link-state intuition

Link-state protocols flood topology information trong area/domain; mỗi router xây graph và chạy shortest-path algorithm như Dijkstra.

OSPF là ví dụ link-state IGP. Nó không đơn giản là “Internet shortest path”; nó hoạt động trong autonomous system với metrics/policies cụ thể.

## Autonomous Systems và BGP

Internet được chia thành Autonomous Systems (AS / 자율 시스템), mỗi AS có routing policy riêng. Border Gateway Protocol (BGP) trao đổi reachability giữa ASes.

BGP là path-vector protocol: route advertisements chứa AS path và attributes. Selection chịu policy/business relationships chứ không chỉ shortest hop count.

Đây là insight quan trọng: Internet routing là technical + administrative/economic system.

## Convergence và transient inconsistency

Khi link fail, routers không cập nhật đồng thời. Trong thời gian convergence có thể có packet loss, loops hoặc route changes.

Distributed control plane vì vậy có same problems về delayed information và partial knowledge như distributed systems nói chung.

## Anycast

Nhiều locations quảng bá cùng IP prefix; routing đưa client tới một location topology-wise phù hợp theo policy. DNS resolvers/CDNs dùng anycast rộng rãi.

Anycast không đảm bảo “server gần nhất theo km” hay latency tối thiểu tuyệt đối; nó follows routing decisions.

## Route security

BGP historically dựa nhiều trên trust giữa networks, nên route leaks/hijacks có thể xảy ra khi prefix advertisement sai. RPKI giúp cryptographically validate quyền origin AS quảng bá prefix, nhưng không giải quyết mọi policy/path issue.

Security ở đây là supply-chain trust của routing information, không chỉ encryption payload.

## Traceroute và TTL/Hop Limit

IP TTL/Hop Limit giảm mỗi router; khi về 0 router gửi ICMP time exceeded. Traceroute tăng TTL dần để suy ra hops.

Kết quả traceroute không phải bản đồ tuyệt đối: routing có thể asymmetric, load-balanced và ICMP filtering.

## Common Misconceptions

**“Router luôn chọn đường ngắn nhất.”** Route selection dựa metrics/policy; BGP đặc biệt không chỉ tối ưu shortest path.

**“Internet là một network thống nhất.”** Nó là network of autonomous networks với agreements và policies.

**“Routing table và forwarding table là cùng một thứ.”** Conceptually control-plane routing information được xử lý thành forwarding entries dùng data plane.

## Mental Model

> Internet routing là distributed computation trên graph mà mỗi organization chỉ kiểm soát một phần và policy quan trọng ngang topology.

## Kết nối

Xem [graph algorithms](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md), [IP/subnet](./01_ethernet_ip_subnetting_and_routing.md), [distributed time/failure](./04_distributed_systems_time_failure_and_consistency.md) và [CDN/load balancing](../08_software_systems/05_caching_load_balancing_and_cdns.md).