# Cloud Computing — “đám mây” thực ra chạy ở đâu?

Cloud không phải máy tính vô hình trên Internet. Nó là data center vật lý được chuẩn hóa thành resource có thể cấp phát bằng software/API. Giá trị cốt lõi của **điện toán đám mây (cloud computing / 클라우드 컴퓨팅)** là chuyển server, network, storage và platform capabilities thành pool programmable, elastic và metered.

## 1. Từ request của user tới physical server

```text
Phone / browser
     ↓ Internet
DNS / CDN / edge
     ↓
Load balancer
     ↓
Application instances
     ↓
Cache / message queue / database
     ↓
Storage

All of them ultimately run on:
Data center → racks → servers → NICs → disks → switches → power + cooling
```

“Serverless” không có nghĩa không có server; nó nghĩa customer không quản lý server lifecycle trực tiếp. Provider vẫn phải provision machines, schedule workloads và isolate tenants.

## 2. Virtualization tạo cloud primitive như thế nào?

Một physical server có CPU/RAM/NIC. **Máy ảo (Virtual Machine, VM / 가상머신)** dùng hypervisor để chia physical resources thành nhiều isolated virtual computers. Container chia sẻ host kernel nhiều hơn nhưng isolate process/filesystem/network namespaces.

```text
Physical server
├── Hypervisor
│   ├── VM A
│   ├── VM B
│   └── VM C
└── hardware

or

Host OS
├── Container A
├── Container B
└── Container C
```

Cloud scheduler đặt workload lên fleet dựa trên capacity, availability zone, affinity và failure domain. API như “create VM” thực chất là request tới control plane để chọn host, attach network/storage và configure identity.

## 3. Control plane và data plane

**Mặt điều khiển (control plane / 제어평면)** nhận intent: tạo VM, firewall rule, database, route. **Mặt dữ liệu (data plane / 데이터평면)** thực sự chuyển packet/read-write data/run workload.

Control plane outage có thể khiến bạn không tạo resource mới dù VM cũ vẫn chạy. Data-plane outage có thể làm application traffic chết dù console cloud vẫn mở được. Phân biệt này cực hữu ích khi debug.

## 4. Region và Availability Zone giải quyết failure domain

Provider chia infrastructure thành region và nhiều failure domains/availability zones tùy architecture. Deploy nhiều zone giảm rủi ro một power/network facility failure làm toàn application down.

```text
Region
├── Zone A: app + DB replica
├── Zone B: app + DB replica
└── Zone C: app + quorum/replica
```

Nhưng multi-zone không tự tạo high availability. Application phải support replication, failover, load balancing và state consistency.

## 5. Object, block và file storage khác nhau

**Block storage** giống virtual disk attach vào VM/database. **Object storage** quản lý object qua API với key/metadata, phù hợp backup, media, data lake. **File storage** cung cấp hierarchical filesystem shared qua network.

Chọn sai storage model gây cost/performance complexity. Object storage không phải “ổ cứng rất to”; semantics của update/list/consistency/access khác filesystem.

## 6. Managed database bán thứ gì ngoài database engine?

Managed database không chỉ bán CPU/RAM. Provider quản lý provisioning, patching, backup, monitoring, replication và một phần failover. Customer vẫn chịu schema design, query design, access control, data quality và nhiều reliability decisions.

Đây là mô hình **shared responsibility**: cloud provider bảo vệ/vận hành infrastructure theo service boundary; customer chịu trách nhiệm configuration, identity, application và data theo boundary đó.

## 7. Hàn Quốc: hyperscaler + domestic cloud + public-sector assurance

Korea có global hyperscalers cùng các domestic providers như Naver Cloud, KT Cloud và NHN Cloud. Domestic ecosystem mạnh nhờ enterprise/public-sector demand, local data centers, Korean-language SaaS/platform integration và regulation/security requirements.

Cloud Security Assurance Program (CSAP / 클라우드서비스 보안인증) vẫn là một layer quan trọng cho cloud services trong phạm vi public-sector/security assurance; KISA tiếp tục vận hành education/certification ecosystem trong 2026. Vì vậy market không chỉ cạnh tranh về compute price mà còn certification, data location, support, network peering và government procurement compatibility.

## 8. Việt Nam: data-center/cloud capacity tăng cùng digital economy

Việt Nam có domestic telecom/cloud providers như Viettel, VNPT và FPT cùng global cloud services được doanh nghiệp sử dụng qua regional/global infrastructure. Local data-center expansion quan trọng vì latency, regulated workloads, data-sovereignty concerns và demand của government/enterprise.

Năm 2025–2026, Việt Nam tiếp tục đẩy chiến lược National Data Center và national data infrastructure. Cần phân biệt **Trung tâm dữ liệu quốc gia** phục vụ state data architecture với commercial public cloud; hai hệ thống có thể dùng công nghệ tương tự nhưng mandate, tenancy và governance khác nhau.

## 9. Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Market structure | Global hyperscalers + strong domestic clouds | Global services + telecom-led/domestic cloud/data-center providers |
| Public-sector layer | CSAP và procurement/security rules tạo market boundary đáng kể | Government digital/data infrastructure và cybersecurity/data rules tạo nhu cầu local/sovereign deployment |
| Data-center maturity | Dense metro fiber, mature enterprise cloud demand | Rapid capacity expansion; Hanoi/HCMC and key industrial/economic regions concentrate demand |
| Customer migration | Legacy enterprise → hybrid/multi-cloud + cloud-native | On-prem/IDC → cloud/hybrid tăng nhanh, nhiều organization leapfrog trực tiếp sang managed services |
| Constraint | Energy, GPU capacity, security/compliance, vendor lock-in | Power/data-center capacity, skills, compliance, interconnect and cost predictability |

## 10. Public, private và hybrid cloud

**Public cloud** dùng provider multi-tenant infrastructure với logical isolation. **Private cloud** dành infrastructure/control domain cho một organization nhưng vẫn cố giữ automation/self-service characteristics. **Hybrid cloud** kết nối on-prem/private và public resources.

Không phải workload nhạy cảm nào cũng bắt buộc private cloud và không phải public cloud mặc định kém an toàn. Risk phụ thuộc architecture, identity, encryption, operation và regulatory boundary.

## 11. Tại sao cloud bill có thể tăng bất ngờ?

On-prem thường làm cost lộ ở capex và fixed capacity. Cloud biến nhiều cost thành usage-based:

```text
compute hours
+ storage GB-month
+ IOPS / requests
+ managed service premium
+ network egress
+ logs / observability
+ backup / snapshots
```

Elasticity là lợi thế nhưng cũng làm runaway workload tạo runaway bill. FinOps xuất hiện để nối engineering decisions với unit economics.

## 12. Autoscaling không giải mọi scalability problem

Nếu stateless app CPU-bound, thêm replicas có thể tăng throughput. Nếu bottleneck là một database lock, downstream API limit hoặc hot partition, scale app layer chỉ tạo thêm pressure.

```text
More app servers
        ↓
more DB connections
        ↓
DB becomes bottleneck faster
```

Cloud cung cấp primitives; architecture vẫn cần hiểu queueing, consistency, caching và backpressure.

## 13. Một outage region có thể lan như thế nào?

- Identity/control service failure làm deployment và token issuance lỗi.
- DNS issue làm healthy service không discover được.
- Network route error cô lập zones.
- Storage metadata service lỗi kéo theo databases/services.
- Customer automation có thể replicate bad config sang nhiều regions.

Multi-cloud cũng không miễn nhiễm: nếu cả hai cloud phụ thuộc cùng DNS provider, CI/CD credential hoặc application bug, common-mode failure vẫn tồn tại.

## 14. Cloud và semiconductor gặp nhau ở AI

AI workload gom GPU/accelerator thành clusters cần HBM, high-speed interconnect, storage throughput và rất nhiều power/cooling. Vì vậy cloud demand truyền ngược xuống [semiconductors](../semiconductors/README.md), [electricity-grid](../electricity-grid/README.md) và data-center construction.

Mental model:

```text
Cloud
= physical data centers
+ virtualization
+ programmable network/storage
+ control plane
+ managed services
+ metering
+ reliability engineering
```

Đọc [`../../devops_platform_engineering/`](../../devops_platform_engineering/README.md) cho cloud/Kubernetes/IaC production depth; [`../../computer_science/`](../../computer_science/README.md) cho distributed systems; chapter này giữ view từ user request xuống physical infrastructure và market Korea–Vietnam.

## Nguồn chính thức tham chiếu

- Korea Internet & Security Agency — 2026 CSAP program information: https://www.kisa.or.kr/401/form?lang_type=KO&postSeq=3760
- Vietnam Ministry of Science and Technology — national data infrastructure, 13 Apr 2026: https://mst.gov.vn/phat-trien-ha-tang-du-lieu-quoc-gia-nen-tang-cho-quan-tri-so-va-tang-truong-197260412011958982.htm
- NIST — Definition of Cloud Computing: https://csrc.nist.gov/publications/detail/sp/800-145/final
