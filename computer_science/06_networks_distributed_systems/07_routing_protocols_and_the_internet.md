# Routing protocols và Internet

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Routing protocols và Internet**. Route đi từ forwarding/longest-prefix match → distance-vector/link-state → autonomous systems/BGP → convergence/anycast → route security và traceroute, để control plane được phân biệt với data plane.

Biết subnetting chưa đủ để hiểu Internet. Router cần học **đường nào dẫn tới prefix nào**, và ở quy mô toàn cầu không một controller duy nhất biết/tin mọi thứ. Routing protocols chia bài toán thành routing nội bộ một administrative lĩnh vực (domain / 도메인) và routing giữa các autonomous các hệ thống (systems / 시스템들).

## Forwarding khác routing

Forwarding là per-packet thao tác (operation / 연산): nhìn destination address, chọn next hop/đầu ra (output / 출력) giao diện (interface / 인터페이스) từ forwarding bảng (table / 테이블).

Routing là control-plane tiến trình (process / 프로세스) xây/cập nhật thông tin để forwarding bảng (table / 테이블) tồn tại.

Tách mặt phẳng dữ liệu (data plane / 데이터 플레인) và điều khiển (control / 제어) plane giúp lập luận (reasoning / 추론): packet forwarding phải rất nhanh; tuyến (route / 경로) computation có thể phức tạp hơn và xảy ra ít thường xuyên hơn.

> **Nối mạch:** Routing computes paths, forwarding selects a next hop; longest-prefix match applies the most specific route, while distance-vector protocols learn paths through neighbor information.

## Longest Prefix Match

Nếu bảng (table / 테이블) có routes `10.0.0.0/8` và `10.1.0.0/16`, destination `10.1.2.3` chọn `/16` vì prefix cụ thể hơn.

Hardware routers có thể dùng TCAM/trie-like structures để lookup tốc độ cao. Đây là liên kết (connection / 연결) trực tiếp với prefix dữ liệu (data / 데이터) structures.

> **Nối mạch:** **Distance-vector intuition** nối từ **Longest Prefix Match** sang **Link-state intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Distance-vector intuition

Distance-vector protocols trao đổi với neighbors “tôi biết destination X cách bao nhiêu”. Bellman–Ford style relaxation cập nhật tuyến (route / 경로) từ neighbor advertisements.

Bài toán (problem / 문제) như count-to-infinity xuất hiện khi topology thất bại (failure / 실패) lan chậm. Split horizon/poison reverse là mitigation trong một số protocols.

> **Nối mạch:** **Link-state intuition** nối từ **Distance-vector intuition** sang **Autonomous các hệ thống (systems / 시스템들) và BGP**, vì cơ chế trước tạo đầu vào cho bước sau.

## Link-state intuition

Link-state protocols flood topology thông tin (information / 정보) trong area/lĩnh vực (domain / 도메인); mỗi router xây đồ thị (graph / 그래프) và chạy shortest-path thuật toán (algorithm / 알고리즘) như Dijkstra.

OSPF là ví dụ link-state IGP. Nó không đơn giản là “Internet shortest đường dẫn (path / 경로)”; nó hoạt động trong autonomous hệ thống (system / 시스템) với metrics/policies cụ thể.

> **Nối mạch:** **Autonomous các hệ thống (systems / 시스템들) và BGP** nối từ **Link-state intuition** sang **Convergence và transient inconsistency**, vì cơ chế trước tạo đầu vào cho bước sau.

## Autonomous các hệ thống (systems / 시스템들) và BGP

Internet được chia thành Autonomous các hệ thống (systems / 시스템들), mỗi AS có routing chính sách (policy / 정책) riêng. Border Gateway giao thức (protocol / 프로토콜) (BGP) trao đổi reachability giữa ASes.

BGP là path-vector giao thức (protocol / 프로토콜): tuyến (route / 경로) advertisements chứa AS đường dẫn (path / 경로) và attributes. Selection chịu chính sách (policy / 정책)/nghiệp vụ (business / 비즈니스) relationships chứ không chỉ shortest hop count.

Đây là insight quan trọng: Internet routing là technical + administrative/economic hệ thống (system / 시스템).

> **Nối mạch:** **Convergence và transient inconsistency** nối từ **Autonomous các hệ thống (systems / 시스템들) và BGP** sang **Anycast**, vì cơ chế trước tạo đầu vào cho bước sau.

## Convergence và transient inconsistency

Khi link thất bại (fail / 실패), routers không cập nhật đồng thời. Trong thời gian convergence có thể có packet mất mát (loss / 손실), loops hoặc tuyến (route / 경로) changes.

Phân tán (distributed / 분산) điều khiển (control / 제어) plane vì vậy có same problems về delayed thông tin (information / 정보) và partial kiến thức (knowledge / 지식) như phân tán (distributed / 분산) các hệ thống (systems / 시스템들) nói chung.

> **Nối mạch:** **Anycast** nối từ **Convergence và transient inconsistency** sang **Tuyến (route / 경로) bảo mật (security / 보안)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Anycast

Nhiều locations quảng bá cùng IP prefix; routing đưa máy khách (client / 클라이언트) tới một location topology-wise phù hợp theo chính sách (policy / 정책). DNS resolvers/CDNs dùng anycast rộng rãi.

Anycast không đảm bảo “máy chủ (server / 서버) gần nhất theo km” hay độ trễ (latency / 지연 시간) tối thiểu tuyệt đối; nó follows routing decisions.

> **Nối mạch:** **Tuyến (route / 경로) bảo mật (security / 보안)** nối từ **Anycast** sang **Traceroute và TTL/Hop Limit**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tuyến (route / 경로) bảo mật (security / 보안)

BGP historically dựa nhiều trên trust giữa networks, nên tuyến (route / 경로) leaks/hijacks có thể xảy ra khi prefix advertisement sai. RPKI giúp cryptographically validate quyền origin AS quảng bá prefix, nhưng không giải quyết mọi chính sách (policy / 정책)/đường dẫn (path / 경로) issue.

Bảo mật (security / 보안) ở đây là supply-chain trust của routing thông tin (information / 정보), không chỉ encryption payload.

> **Nối mạch:** **Tuyến (route / 경로) bảo mật (security / 보안)** đặt tiêu chí; **Traceroute và TTL/Hop Limit** dùng nó để kiểm tra ranh giới, rồi **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả.

## Traceroute và TTL/Hop Limit

IP TTL/Hop Limit giảm mỗi router; khi về 0 router gửi ICMP thời gian (time / 시간) exceeded. Traceroute tăng TTL dần để suy ra hops.

Kết quả traceroute không phải bản đồ tuyệt đối: routing có thể asymmetric, load-balanced và ICMP filtering.

> **Nối mạch:** **Traceroute và TTL/Hop Limit** đặt tiêu chí; **Dùng chung (common / 공통) Misconceptions** dùng nó để kiểm tra ranh giới, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Dùng chung (common / 공통) Misconceptions

**“Router luôn chọn đường ngắn nhất.”** tuyến (route / 경로) selection dựa metrics/chính sách (policy / 정책); BGP đặc biệt không chỉ tối ưu shortest đường dẫn (path / 경로).

**“Internet là một mạng (network / 네트워크) thống nhất.”** Nó là mạng (network / 네트워크) of autonomous networks với agreements và policies.

**“Routing bảng (table / 테이블) và forwarding bảng (table / 테이블) là cùng một thứ.”** Conceptually control-plane routing thông tin (information / 정보) được xử lý thành forwarding entries dùng mặt phẳng dữ liệu (data plane / 데이터 플레인).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Internet routing là phân tán (distributed / 분산) computation trên đồ thị (graph / 그래프) mà mỗi organization chỉ kiểm soát một phần và chính sách (policy / 정책) quan trọng ngang topology.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Xem [graph algorithms](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md), [IP/subnet](./01_ethernet_ip_subnetting_and_routing.md), [distributed time/failure](./04_distributed_systems_time_failure_and_consistency.md) và [CDN/load balancing](../08_software_systems/05_caching_load_balancing_and_cdns.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
