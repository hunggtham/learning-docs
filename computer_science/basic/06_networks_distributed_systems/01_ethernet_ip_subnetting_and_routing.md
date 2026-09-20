# Ethernet, IP, subnetting và routing

Để packet đi từ một host tới host khác, system phải giải hai bài toán: delivery trong local link và forwarding qua nhiều networks. Ethernet/Wi‑Fi và IP giải ở scopes khác nhau.

## Ethernet và local link

Ethernet frame có source/destination MAC addresses và EtherType cùng payload/FCS. Switch học mapping MAC → port từ source addresses và forward frames trong Layer-2 broadcast domain.

MAC address không phải global routing identity Internet. Router tách Layer-2 domains; mỗi hop có thể dùng frame headers khác trong khi IP source/destination thường end-to-end hơn (trừ NAT/tunnels).

## ARP và Neighbor Discovery

IPv4 host cần map next-hop IP tới MAC trên local Ethernet, dùng ARP. IPv6 dùng Neighbor Discovery qua ICMPv6. Khi gửi tới remote subnet, host resolve MAC của default gateway, không MAC của remote final host.

Đây là distinction quan trọng giữa **next hop** và **final destination**.

## IP prefix và subnet

IPv4 address 32 bits. CIDR prefix `/n` nói n high bits thuộc network prefix. Ví dụ `192.168.1.0/24` có 24 prefix bits, còn 8 host bits.

Subnetting không chỉ bài toán đổi binary; nó xác định routing aggregation và broadcast/locality boundaries. Prefix longer = network cụ thể hơn, fewer addresses.

IPv6 address 128 bits, dùng hexadecimal và prefixes; operational conventions khác IPv4 nhưng same prefix-routing idea.

## Routing table và longest-prefix match

Router có routes `prefix → next hop/interface`. Khi destination match nhiều prefixes, longest-prefix match chọn route cụ thể nhất. Default route `/0` match everything nếu không có specific route.

Routing table data plane forwarding khác routing protocols control plane học routes.

## Static và dynamic routing

Trong small network có static routes. Large networks dùng protocols. OSPF/IS-IS are link-state within autonomous systems; BGP trao đổi reachability/policy giữa ASes và large networks.

BGP không đơn giản chọn geographic shortest path; policy, AS path và attributes matter. Internet routing là distributed policy system.

## TTL/Hop Limit

IP header có TTL (IPv4) hoặc Hop Limit (IPv6), decrement mỗi router. Khi về 0 packet discarded và thường ICMP message returned. Điều này ngăn routing loop giữ packet mãi.

`traceroute` khai thác TTL expiry để infer hops, nhưng path/asymmetric/firewall behavior có thể làm output không hoàn hảo.

## NAT

Network Address Translation rewrite addresses/ports, thường cho private IPv4 hosts share public address. NAT giúp address conservation và topology hiding phần nào nhưng phá pure end-to-end addressing, complicates inbound connections và protocols.

NAT không thay firewall security model. Stateful NAT often coexists firewall behavior, nhưng translation bản thân không phải full access-control policy.

## ICMP

ICMP mang control/error diagnostics như destination unreachable, time exceeded, echo request/reply. Blocking all ICMP có thể phá path MTU discovery hoặc diagnostics; security policy nên hiểu message types thay vì assume ICMP vô ích.

## Mental Model

> Host trước tiên hỏi: destination có local prefix không? Nếu local, resolve neighbor; nếu remote, gửi frame tới gateway. Router lặp **longest-prefix match → next hop** cho tới destination network.

## Common Misconceptions

**“Switch và router đều chuyển packets nên giống nhau.”** Switch primarily forwards link-layer frames trong domain; router forwards IP packets giữa networks.

**“Subnet mask chỉ chia IP đẹp hơn.”** Nó quyết định local-vs-routed behavior và route aggregation.

**“NAT là firewall.”** NAT rewrites mappings; firewall enforces policy, dù devices thường combine cả hai.

## Kết nối

[Graph shortest-path ideas](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md) giúp hiểu routing nhưng Internet policy phức tạp hơn pure shortest path. [TCP/UDP](./02_transport_tcp_udp_and_congestion.md) chạy trên IP; [DNS/HTTP/TLS](./03_dns_http_tls_and_web_request.md) dùng routing path này.
