# Ethernet, IP, subnetting và routing

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Ethernet, IP, subnetting và routing**. Route đi từ local link/ARP-ND → IP prefix/subnet → routing table/longest-prefix match → TTL, NAT và ICMP, để forwarding được nối với boundary của từng mạng.

Để packet đi từ một host tới host khác, hệ thống (system / 시스템) phải giải hai bài toán: delivery trong cục bộ (local / 로컬) link và forwarding qua nhiều networks. Ethernet/Wi‑Fi và IP giải ở scopes khác nhau.

## Ethernet và cục bộ (local / 로컬) link

Ethernet frame có nguồn (source / 소스)/destination MAC addresses và EtherType cùng payload/FCS. Switch học ánh xạ (mapping / 매핑) MAC → cổng (port / 포트) từ nguồn (source / 소스) addresses và forward frames trong Layer-2 broadcast lĩnh vực (domain / 도메인).

MAC address không phải toàn cục (global / 전역) routing định danh (identity / 식별자) Internet. Router tách Layer-2 domains; mỗi hop có thể dùng frame headers khác trong khi IP nguồn (source / 소스)/destination thường end-to-end hơn (trừ NAT/tunnels).

> **Nối mạch:** Ethernet cung cấp local link; ARP/Neighbor Discovery ánh xạ địa chỉ mạng sang link-layer, rồi IP prefix/subnet quyết định host nào cùng mạng và gói tin cần route.

## ARP và Neighbor Discovery

IPv4 host cần map next-hop IP tới MAC trên cục bộ (local / 로컬) Ethernet, dùng ARP. IPv6 dùng Neighbor Discovery qua ICMPv6. Khi gửi tới remote subnet, host resolve MAC của default gateway, không MAC của remote final host.

Đây là distinction quan trọng giữa **next hop** và **final destination**.

> **Nối mạch:** **IP prefix và subnet** nối từ **ARP và Neighbor Discovery** sang **Routing bảng (table / 테이블) và longest-prefix match**, vì cơ chế trước tạo đầu vào cho bước sau.

## IP prefix và subnet

IPv4 address 32 bits. CIDR prefix `/n` nói n high bits thuộc mạng (network / 네트워크) prefix. Ví dụ `192.168.1.0/24` có 24 prefix bits, còn 8 host bits.

Subnetting không chỉ bài toán đổi nhị phân (binary / 이진); nó xác định routing aggregation và broadcast/locality boundaries. Prefix longer = mạng (network / 네트워크) cụ thể hơn, fewer addresses.

IPv6 address 128 bits, dùng hexadecimal và prefixes; operational conventions khác IPv4 nhưng same prefix-routing idea.

> **Nối mạch:** **Routing bảng (table / 테이블) và longest-prefix match** nối từ **IP prefix và subnet** sang **Static và động (dynamic / 동적) routing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Routing bảng (table / 테이블) và longest-prefix match

Router có routes `prefix → next hop/interface`. Khi destination match nhiều prefixes, longest-prefix match chọn tuyến (route / 경로) cụ thể nhất. Default tuyến (route / 경로) `/0` match everything nếu không có specific tuyến (route / 경로).

Routing bảng (table / 테이블) mặt phẳng dữ liệu (data plane / 데이터 플레인) forwarding khác routing protocols điều khiển (control / 제어) plane học routes.

> **Nối mạch:** **Static và động (dynamic / 동적) routing** nối từ **Routing bảng (table / 테이블) và longest-prefix match** sang **TTL/Hop Limit**, vì cơ chế trước tạo đầu vào cho bước sau.

## Static và động (dynamic / 동적) routing

Trong small mạng (network / 네트워크) có static routes. Large networks dùng protocols. OSPF/IS-IS are link-state within autonomous các hệ thống (systems / 시스템들); BGP trao đổi reachability/chính sách (policy / 정책) giữa ASes và large networks.

BGP không đơn giản chọn geographic shortest đường dẫn (path / 경로); chính sách (policy / 정책), AS đường dẫn (path / 경로) và attributes matter. Internet routing là phân tán (distributed / 분산) chính sách (policy / 정책) hệ thống (system / 시스템).

> **Nối mạch:** **Static và động (dynamic / 동적) routing** đặt tiêu chí; **TTL/Hop Limit** dùng nó để kiểm tra ranh giới, rồi **NAT** mở rộng hệ quả.

## TTL/Hop Limit

IP header có TTL (IPv4) hoặc Hop Limit (IPv6), decrement mỗi router. Khi về 0 packet discarded và thường ICMP message returned. Điều này ngăn routing vòng lặp (loop / 루프) giữ packet mãi.

`traceroute` khai thác TTL expiry để infer hops, nhưng đường dẫn (path / 경로)/asymmetric/firewall hành vi (behavior / 동작) có thể làm đầu ra (output / 출력) không hoàn hảo.

> **Nối mạch:** **TTL/Hop Limit** đặt tiêu chí; **NAT** dùng nó để kiểm tra ranh giới, rồi **ICMP** mở rộng hệ quả.

## NAT

Mạng (network / 네트워크) Address Translation rewrite addresses/ports, thường cho private IPv4 hosts share công khai (public / 공개) address. NAT giúp address conservation và topology hiding phần nào nhưng phá pure end-to-end addressing, complicates inbound connections và protocols.

NAT không thay firewall bảo mật (security / 보안) mô hình (model / 모델). Stateful NAT often coexists firewall hành vi (behavior / 동작), nhưng translation bản thân không phải full access-control chính sách (policy / 정책).

> **Nối mạch:** **ICMP** nối từ **NAT** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## ICMP

ICMP mang điều khiển (control / 제어)/lỗi (error / 오류) diagnostics như destination unreachable, thời gian (time / 시간) exceeded, echo yêu cầu (request / 요청)/reply. Blocking all ICMP có thể phá đường dẫn (path / 경로) MTU discovery hoặc diagnostics; bảo mật (security / 보안) chính sách (policy / 정책) nên hiểu message types thay vì assume ICMP vô ích.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **ICMP**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Host trước tiên hỏi: destination có cục bộ (local / 로컬) prefix không? Nếu cục bộ (local / 로컬), resolve neighbor; nếu remote, gửi frame tới gateway. Router lặp **longest-prefix match → next hop** cho tới destination mạng (network / 네트워크).

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“Switch và router đều chuyển packets nên giống nhau.”** Switch primarily forwards link-layer frames trong lĩnh vực (domain / 도메인); router forwards IP packets giữa networks.

**“Subnet mask chỉ chia IP đẹp hơn.”** Nó quyết định local-vs-routed hành vi (behavior / 동작) và tuyến (route / 경로) aggregation.

**“NAT là firewall.”** NAT rewrites mappings; firewall enforces chính sách (policy / 정책), dù devices thường combine cả hai.

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

[Graph shortest-path ideas](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md) giúp hiểu routing nhưng Internet chính sách (policy / 정책) phức tạp hơn pure shortest đường dẫn (path / 경로). [TCP/UDP](./02_transport_tcp_udp_and_congestion.md) chạy trên IP; [DNS/HTTP/TLS](./03_dns_http_tls_and_web_request.md) dùng routing đường dẫn (path / 경로) này.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
