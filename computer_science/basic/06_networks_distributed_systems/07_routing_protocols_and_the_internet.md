# Routing protocols và Internet

> **Mạch đọc:** Đọc **Routing protocols và Internet** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Forwarding khác routing** sang **Longest Prefix Match**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Biết subnetting chưa đủ để hiểu Internet. Router cần học **đường nào dẫn tới prefix nào**, và ở quy mô toàn cầu không một controller duy nhất biết/tin mọi thứ. Routing protocols chia bài toán thành routing nội bộ một administrative lĩnh vực (domain / 도메인) và routing giữa các autonomous các hệ thống (systems / 시스템들).

## Forwarding khác routing

Forwarding là per-packet thao tác (operation / 연산): nhìn destination address, chọn next hop/đầu ra (output / 출력) giao diện (interface / 인터페이스) từ forwarding bảng (table / 테이블).

Routing là control-plane tiến trình (process / 프로세스) xây/cập nhật thông tin để forwarding bảng (table / 테이블) tồn tại.

Tách mặt phẳng dữ liệu (data plane / 데이터 플레인) và điều khiển (control / 제어) plane giúp lập luận (reasoning / 추론): packet forwarding phải rất nhanh; tuyến (route / 경로) computation có thể phức tạp hơn và xảy ra ít thường xuyên hơn.


> **Chuyển mạch:** Từ **Forwarding khác routing**, ta sang **Longest Prefix Match** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Longest Prefix Match

Nếu bảng (table / 테이블) có routes `10.0.0.0/8` và `10.1.0.0/16`, destination `10.1.2.3` chọn `/16` vì prefix cụ thể hơn.

Hardware routers có thể dùng TCAM/trie-like structures để lookup tốc độ cao. Đây là liên kết (connection / 연결) trực tiếp với prefix dữ liệu (data / 데이터) structures.


> **Chuyển mạch:** Từ **Longest Prefix Match**, ta sang **Distance-vector intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Distance-vector intuition

Distance-vector protocols trao đổi với neighbors “tôi biết destination X cách bao nhiêu”. Bellman–Ford style relaxation cập nhật tuyến (route / 경로) từ neighbor advertisements.

Bài toán (problem / 문제) như count-to-infinity xuất hiện khi topology thất bại (failure / 실패) lan chậm. Split horizon/poison reverse là mitigation trong một số protocols.


> **Chuyển mạch:** Từ **Distance-vector intuition**, ta sang **Link-state intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Link-state intuition

Link-state protocols flood topology thông tin (information / 정보) trong area/lĩnh vực (domain / 도메인); mỗi router xây đồ thị (graph / 그래프) và chạy shortest-path thuật toán (algorithm / 알고리즘) như Dijkstra.

OSPF là ví dụ link-state IGP. Nó không đơn giản là “Internet shortest đường dẫn (path / 경로)”; nó hoạt động trong autonomous hệ thống (system / 시스템) với metrics/policies cụ thể.


> **Chuyển mạch:** Từ **Link-state intuition**, ta sang **Autonomous các hệ thống (systems / 시스템들) và BGP** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Autonomous các hệ thống (systems / 시스템들) và BGP

Internet được chia thành Autonomous các hệ thống (systems / 시스템들), mỗi AS có routing chính sách (policy / 정책) riêng. Border Gateway giao thức (protocol / 프로토콜) (BGP) trao đổi reachability giữa ASes.

BGP là path-vector giao thức (protocol / 프로토콜): tuyến (route / 경로) advertisements chứa AS đường dẫn (path / 경로) và attributes. Selection chịu chính sách (policy / 정책)/nghiệp vụ (business / 비즈니스) relationships chứ không chỉ shortest hop count.

Đây là insight quan trọng: Internet routing là technical + administrative/economic hệ thống (system / 시스템).


> **Chuyển mạch:** Từ **Autonomous các hệ thống (systems / 시스템들) và BGP**, ta sang **Convergence và transient inconsistency** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Convergence và transient inconsistency

Khi link thất bại (fail / 실패), routers không cập nhật đồng thời. Trong thời gian convergence có thể có packet mất mát (loss / 손실), loops hoặc tuyến (route / 경로) changes.

Phân tán (distributed / 분산) điều khiển (control / 제어) plane vì vậy có same problems về delayed thông tin (information / 정보) và partial kiến thức (knowledge / 지식) như phân tán (distributed / 분산) các hệ thống (systems / 시스템들) nói chung.


> **Chuyển mạch:** Từ **Convergence và transient inconsistency**, ta sang **Anycast** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Anycast

Nhiều locations quảng bá cùng IP prefix; routing đưa máy khách (client / 클라이언트) tới một location topology-wise phù hợp theo chính sách (policy / 정책). DNS resolvers/CDNs dùng anycast rộng rãi.

Anycast không đảm bảo “máy chủ (server / 서버) gần nhất theo km” hay độ trễ (latency / 지연 시간) tối thiểu tuyệt đối; nó follows routing decisions.


> **Chuyển mạch:** Từ **Anycast**, ta sang **tuyến (route / 경로) bảo mật (security / 보안)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tuyến (route / 경로) bảo mật (security / 보안)

BGP historically dựa nhiều trên trust giữa networks, nên tuyến (route / 경로) leaks/hijacks có thể xảy ra khi prefix advertisement sai. RPKI giúp cryptographically validate quyền origin AS quảng bá prefix, nhưng không giải quyết mọi chính sách (policy / 정책)/đường dẫn (path / 경로) issue.

Bảo mật (security / 보안) ở đây là supply-chain trust của routing thông tin (information / 정보), không chỉ encryption payload.


> **Chuyển mạch:** Từ **tuyến (route / 경로) bảo mật (security / 보안)**, ta sang **Traceroute và TTL/Hop Limit** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Traceroute và TTL/Hop Limit

IP TTL/Hop Limit giảm mỗi router; khi về 0 router gửi ICMP thời gian (time / 시간) exceeded. Traceroute tăng TTL dần để suy ra hops.

Kết quả traceroute không phải bản đồ tuyệt đối: routing có thể asymmetric, load-balanced và ICMP filtering.


> **Chuyển mạch:** Từ **Traceroute và TTL/Hop Limit**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Router luôn chọn đường ngắn nhất.”** tuyến (route / 경로) selection dựa metrics/chính sách (policy / 정책); BGP đặc biệt không chỉ tối ưu shortest đường dẫn (path / 경로).

**“Internet là một mạng (network / 네트워크) thống nhất.”** Nó là mạng (network / 네트워크) of autonomous networks với agreements và policies.

**“Routing bảng (table / 테이블) và forwarding bảng (table / 테이블) là cùng một thứ.”** Conceptually control-plane routing thông tin (information / 정보) được xử lý thành forwarding entries dùng mặt phẳng dữ liệu (data plane / 데이터 플레인).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Internet routing là phân tán (distributed / 분산) computation trên đồ thị (graph / 그래프) mà mỗi organization chỉ kiểm soát một phần và chính sách (policy / 정책) quan trọng ngang topology.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Xem [graph algorithms](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md), [IP/subnet](./01_ethernet_ip_subnetting_and_routing.md), [distributed time/failure](./04_distributed_systems_time_failure_and_consistency.md) và [CDN/load balancing](../08_software_systems/05_caching_load_balancing_and_cdns.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 network layers packets and encapsulation](./00_network_layers_packets_and_encapsulation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
