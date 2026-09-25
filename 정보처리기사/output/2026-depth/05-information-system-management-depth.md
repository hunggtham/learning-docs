# Môn 5 — 정보시스템 구축 관리: Deep Dive 2026

> Môn 5 có breadth rất lớn: methodology, estimation/project management, network/SW/HW/DB construction, infrastructure, availability, secure software và system security. Đây là môn dễ 과락 nếu chỉ học security hoặc chỉ học project management.

## 1. 소프트웨어 개발 방법론 활용 — Software Development Methodology

### 1.1 Methodology không phải lifecycle model đơn thuần

Development methodology bao gồm process, role, artifact, technique và rule để tổ chức việc phát triển. Waterfall, iterative/incremental, spiral, agile là các cách tổ chức lifecycle khác nhau; một methodology cụ thể có thể dùng nhiều practice và artifact.

Waterfall phù hợp khi requirement ổn định và cần phase/gate rõ, nhưng feedback muộn. Iterative phát triển qua nhiều vòng refinement. Incremental giao từng phần functionality. Spiral nhấn mạnh risk analysis theo vòng lặp. Agile nhấn feedback, adaptation và delivery ngắn.

### 1.2 Methodology Tailoring

Tailoring là điều chỉnh process chuẩn theo quy mô, risk, regulation, team, technology và contract của project. Tailoring không có nghĩa bỏ tùy tiện artifact khó chịu; thay đổi phải có lý do và vẫn bảo đảm governance/quality cần thiết.

Ví dụ project safety-critical có thể cần documentation, review, traceability và verification mạnh hơn web nội bộ nhỏ.

### 1.3 Estimation

#### LOC

Lines of Code estimation dễ hiểu nhưng phụ thuộc language/style và khó ước lượng sớm khi design chưa rõ.

#### Function Point

Function Point đo functional size từ góc nhìn user, dựa các loại input/output/query/file/interface và complexity weight theo phương pháp cụ thể. Ưu điểm là ít phụ thuộc language hơn LOC.

Đề có thể hỏi EI, EO, EQ, ILF, EIF theo Function Point. Cần hiểu category:

- EI: External Input — data/control vào làm thay đổi internal state.
- EO: External Output — output có processing/derived information.
- EQ: External Inquiry — input+output inquiry với processing hạn chế.
- ILF: Internal Logical File — logical data group do application quản lý.
- EIF: External Interface File — data logic được application khác quản lý nhưng application này đọc/tham chiếu.

#### COCOMO

COCOMO là mô hình cost estimation dựa software size và project mode/parameter theo version. Các mode kinh điển: Organic, Semi-detached, Embedded.

Không cần biến COCOMO thành công thức thuộc lòng nếu chưa hiểu: size lớn hơn và constraint phức tạp hơn làm effort tăng phi tuyến theo model.

### 1.4 Schedule Network — PERT/CPM

Critical Path là path có tổng duration dài nhất trong network và quyết định minimum project duration theo model. Activity trên critical path có total float/slack bằng 0 trong setup cơ bản.

PERT expected time kinh điển:

`TE = (O + 4M + P) / 6`

O optimistic, M most likely, P pessimistic.

Critical path không phải path có nhiều activity nhất, mà path có **tổng thời gian dài nhất**.

### 1.5 Risk

Risk = uncertainty có impact lên objective. Risk management gồm identification, analysis, response planning, monitoring/control.

Threat response thường gồm avoid, mitigate, transfer, accept. Opportunity response có exploit, enhance, share, accept theo taxonomy project management phổ biến.

Issue khác risk: issue đã xảy ra; risk chưa chắc xảy ra.

## 2. Quality và Process Maturity

### 2.1 Software Quality

Quality attribute thường gặp: functionality/suitability, reliability, usability, efficiency/performance, maintainability, portability, security, compatibility tùy standard/version.

ISO/IEC 9126 là model cũ thường xuất hiện trong đề/tài liệu lịch sử. ISO/IEC 25010 là model hiện đại hơn. Khi đề đưa đúng tên standard, trả theo taxonomy của standard đó thay vì trộn các version.

### 2.2 CMMI

CMMI maturity levels truyền thống theo staged representation:

1 Initial  
2 Managed  
3 Defined  
4 Quantitatively Managed  
5 Optimizing

Mục đích là process maturity, không phải xếp hạng chất lượng từng sản phẩm cụ thể.

### 2.3 SPICE / ISO/IEC 15504

SPICE đánh giá process capability theo level. Đề có thể hỏi capability/process assessment; đừng nhầm với product quality model.

## 3. IT 프로젝트 정보시스템 구축 관리 — IT Project / Information System Construction Management

## 3.1 Network Construction Management

Network design cần topology, bandwidth, latency, redundancy, segmentation, routing, addressing, security zone, availability và manageability.

### Topology

Bus: shared backbone, đơn giản nhưng fault backbone ảnh hưởng rộng. Star: node nối central device, dễ quản lý; central device là critical point nếu không redundant. Ring: node theo vòng. Mesh: nhiều đường redundancy nhưng cost/complexity cao. Tree/Hierarchical: phân tầng, phổ biến trong enterprise design.

### Redundancy

Redundancy loại single point of failure nhưng cần protocol/cơ chế failover. Chỉ mua hai device chưa đủ high availability nếu cả hai phụ thuộc cùng power, switch, rack hoặc configuration lỗi chung.

### VLAN

VLAN chia broadcast domain logic trên switch infrastructure. VLAN không tự động là security boundary hoàn chỉnh; inter-VLAN routing/firewall policy vẫn cần kiểm soát.

### QoS

Quality of Service ưu tiên/điều tiết traffic theo requirement như latency, jitter, bandwidth, loss. Voice/video thường nhạy latency/jitter hơn file transfer.

## 3.2 Software Construction Management

Cần quản lý requirement, architecture, dependency, version, build, test, release, configuration và deployment.

COTS — Commercial Off-The-Shelf — mua sản phẩm có sẵn; giảm development time nhưng tăng dependency/vendor/customization constraint. Open Source cho quyền sử dụng/source theo license nhưng vẫn cần license compliance, maintenance và security governance.

### Middleware

Middleware nằm giữa application/component để cung cấp communication/integration service. Category có RPC, message-oriented middleware, transaction monitor, object broker, web/application server và integration middleware.

Middleware khác OS và khác business application.

## 3.3 Hardware Construction Management

### CPU / Memory / Storage

CPU capacity không chỉ clock speed; core, architecture, workload, cache và concurrency ảnh hưởng throughput. Memory thiếu gây paging/swapping và performance collapse. Storage cần nhìn latency, IOPS, throughput, capacity, durability.

### RAID

RAID 0: striping, không redundancy; performance/capacity tốt nhưng một disk fail có thể mất array.  
RAID 1: mirroring, redundancy tốt, usable capacity khoảng 50% với pair truyền thống.  
RAID 5: striping + distributed single parity, chịu một disk failure, write penalty.  
RAID 6: dual parity, chịu hai disk failure, write penalty cao hơn.  
RAID 10: mirror + stripe, performance và redundancy tốt nhưng tốn capacity.

RAID không thay backup. RAID bảo vệ availability khi disk failure; backup bảo vệ logical deletion, corruption, ransomware, disaster và historical restore tùy design.

### SAN vs NAS

SAN cung cấp block storage qua storage network. NAS cung cấp file service qua network. Đây là abstraction khác nhau: block vs file.

## 3.4 Database Construction Management

Database construction management ở Môn 5 thiên về capacity, HA, backup/recovery, performance, security và operation hơn normalization chi tiết của Môn 3.

Phải xem connection load, transaction throughput, storage growth, index, backup window, replication, failover, RPO/RTO và monitoring.

## 3.5 Virtualization và Cloud

### Virtual Machine vs Container

VM virtualize machine/hardware abstraction và mỗi VM thường có guest OS riêng. Container share host kernel và isolate process/resource, nên nhẹ hơn nhưng isolation model khác.

### IaaS / PaaS / SaaS

IaaS: user quản OS/runtime/app nhiều hơn, provider quản infrastructure physical/virtualization. PaaS: provider quản platform/runtime nhiều hơn, user tập trung application/data. SaaS: provider vận hành application hoàn chỉnh, user chủ yếu sử dụng/configure.

### Public / Private / Hybrid Cloud

Public dùng provider shared infrastructure/service. Private dành cho một organization theo model riêng. Hybrid kết nối/combine private và public environment.

### Scale Up vs Scale Out

Scale Up tăng resource của một node. Scale Out thêm node. Scale out thường cần application/data design hỗ trợ distribution.

## 4. Availability, DR, Backup

### 4.1 Availability

Availability có thể biểu diễn gần đúng:

`Availability = MTBF / (MTBF + MTTR)`

MTBF tăng hoặc MTTR giảm thì availability tăng.

### 4.2 RTO vs RPO

RTO — Recovery Time Objective — thời gian tối đa chấp nhận để khôi phục service sau sự cố. RPO — Recovery Point Objective — lượng mất dữ liệu tối đa tính theo thời gian.

Ví dụ RTO 2h, RPO 15m nghĩa service cần khôi phục trong 2 giờ và data loss không quá khoảng 15 phút theo objective.

### 4.3 Backup Types

Full Backup sao chép toàn bộ selected data. Incremental sao chép thay đổi từ backup gần nhất bất kể loại; restore thường cần full + chuỗi incremental. Differential sao chép thay đổi kể từ full gần nhất; restore thường cần full + differential mới nhất.

### 4.4 DR Site

Cold Site có facility nhưng ít equipment/data ready; recovery chậm, cost thấp hơn. Warm Site có một phần system/data ready. Hot Site gần production replica và recovery nhanh hơn nhưng cost cao.

## 5. 소프트웨어 개발 보안 구축 — Secure Software Development

## 5.1 Security Goals

CIA triad:

- Confidentiality — chỉ entity được phép đọc.
- Integrity — dữ liệu không bị thay đổi trái phép.
- Availability — service/data sẵn sàng khi cần.

Thêm Authentication xác minh identity, Authorization quyết định quyền, Accountability/Auditing ghi nhận action.

### 5.2 Input Validation

Input từ client, file, API, DB hay external system đều không nên tin tưởng mặc định. Validation dựa allowlist/type/range/length/context; output encoding tùy sink.

### 5.3 SQL Injection

SQL Injection xảy ra khi untrusted input được ghép vào SQL làm thay đổi query structure. Defense chính: parameterized query/prepared statement, ORM binding đúng cách, least privilege, validation bổ trợ.

Escape thủ công không nên là defense duy nhất.

### 5.4 XSS

Cross-Site Scripting đưa script/content độc hại vào context browser của user. Loại thường gặp: Stored, Reflected, DOM-based.

Defense phụ thuộc context: output encoding/escaping đúng context, template auto-escape, sanitize HTML khi cần cho phép markup, CSP như defense-in-depth.

SQL Injection nhắm query/database; XSS nhắm browser/client context. Đừng nhầm vì cả hai đều bắt đầu từ input không tin cậy.

### 5.5 CSRF

CSRF lợi dụng browser của user đã authenticated gửi request mà user không mong muốn. Defense: anti-CSRF token, SameSite cookie phù hợp, kiểm tra Origin/Referer trong context thích hợp, re-authentication cho action nhạy cảm.

CSRF khác XSS: CSRF lợi dụng trust server dành cho browser/session; XSS inject code vào page/context client.

### 5.6 Path Traversal

Attacker dùng path như `../` để truy cập file ngoài thư mục cho phép. Defense: canonicalization an toàn, allowlist identifier/path, không ghép raw user path vào filesystem access.

### 5.7 Command Injection

Untrusted input đi vào shell/system command có thể thay đổi command. Tránh shell khi có API trực tiếp, parameterize argument đúng cách, allowlist và least privilege.

### 5.8 Memory Safety

Buffer overflow, use-after-free, integer overflow có thể dẫn tới crash hoặc code execution trong low-level language. Defense gồm bounds checking, safe library/language, compiler protection, ASLR/DEP như defense-in-depth.

### 5.9 Error Handling

Không lộ stack trace, SQL detail, secret/path nội bộ cho client. Log đủ để điều tra nhưng không log password/token/private key hoặc sensitive data không cần thiết.

### 5.10 Secure Session

Session ID phải unpredictable, rotate sau login/privilege change, expire hợp lý, cookie dùng Secure/HttpOnly/SameSite theo requirement. Logout phải invalidate session phía server khi architecture yêu cầu.

## 6. 시스템 보안 구축 — System Security

## 6.1 Threat, Vulnerability, Risk

Asset là thứ có giá trị. Threat là nguồn/sự kiện có khả năng gây hại. Vulnerability là weakness. Risk liên quan likelihood và impact khi threat khai thác vulnerability.

Control giảm likelihood/impact hoặc hỗ trợ detect/recover.

## 6.2 Malware

Virus cần host/file và thường lây khi host chạy. Worm tự lan qua network. Trojan giả dạng hữu ích nhưng chứa hành vi độc hại. Ransomware mã hóa/khóa data để tống tiền. Spyware thu thập thông tin. Rootkit che giấu/duy trì quyền sâu.

Botnet là tập compromised hosts bị control; DDoS có thể dùng botnet nhưng botnet không đồng nghĩa DDoS.

## 6.3 Access Control

DAC — Discretionary Access Control — owner/resource controller quyết quyền. MAC — Mandatory Access Control — policy/label bắt buộc, user không tự ý thay đổi. RBAC — Role-Based Access Control — quyền gắn role rồi user nhận role.

Least Privilege: chỉ cấp quyền tối thiểu cần thiết. Separation of Duties: chia trách nhiệm nhạy cảm giữa nhiều actor. Need-to-Know: chỉ truy cập thông tin cần cho nhiệm vụ.

## 6.4 Authentication Factors

Something you know: password/PIN. Something you have: token/card/device. Something you are: biometric. Somewhere you are / something you do đôi khi được dùng thêm trong taxonomy.

Multi-factor cần ít nhất hai factor **khác loại**. Hai password không phải 2FA.

## 6.5 Cryptography

### Symmetric Encryption

Cùng secret key hoặc key tương đương cho encrypt/decrypt. Nhanh, phù hợp bulk data nhưng key distribution khó.

### Asymmetric Encryption

Public/private key pair. Hỗ trợ key exchange, encryption use case và digital signature. Chậm hơn symmetric cho bulk data.

### Hash

Hash tạo fixed-length digest, one-way theo mục tiêu thiết kế. Dùng integrity, password verification với password hashing scheme phù hợp, digital signature pipeline. Hash không phải encryption.

### Digital Signature

Signature dùng private key của signer để tạo signature trên data/hash theo scheme; verifier dùng public key xác minh authenticity/integrity và hỗ trợ non-repudiation trong context phù hợp.

Encryption bằng public key của receiver và signature bằng private key của sender phục vụ mục tiêu khác nhau.

## 6.6 PKI và Certificate

PKI quản public key/certificate/trust. CA ký certificate binding identity/domain với public key. Certificate validation cần chain of trust, validity, hostname/policy và revocation/status theo system.

## 6.7 Network Security Devices

Firewall filter traffic theo rule. IDS detect suspicious activity và alert. IPS nằm inline/active hơn để block/prevent. WAF tập trung HTTP/web application attack pattern. Proxy trung gian request; reverse proxy đứng trước server, có thể load balance/TLS termination/security function.

VPN tạo protected tunnel qua untrusted network bằng protocol/cryptography phù hợp.

### IDS detection

Signature-based tốt với pattern đã biết nhưng yếu với attack mới/biến thể. Anomaly-based phát hiện lệch baseline nhưng dễ false positive và cần tuning.

## 6.8 Security Protocols

TLS bảo vệ transport session của nhiều application protocol; HTTPS là HTTP over TLS. SSH cung cấp secure remote login/tunneling. IPsec bảo vệ ở network layer concept, với AH/ESP trong taxonomy truyền thống. S/MIME/PGP liên quan email/content security.

Đừng học “protocol nào an toàn” theo tên; hiểu layer và mục tiêu bảo vệ.

## 6.9 AAA

Authentication: bạn là ai? Authorization: bạn được làm gì? Accounting/Auditing: bạn đã làm gì/usage ra sao?

RADIUS/TACACS+ có thể xuất hiện trong context AAA network access/admin. Không cần nhớ mọi chi tiết vendor-specific trước khi phân biệt ba chữ A.

## 6.10 Logging, Monitoring, Incident Response

Security log cần timestamp đồng bộ, identity, event, source, result và context cần thiết. Centralized logging/SIEM giúp correlation nhưng chất lượng phụ thuộc log source và rule.

Incident response flow thường gồm preparation, detection/analysis, containment, eradication, recovery, lessons learned theo framework cụ thể. Thứ tự tên có thể khác giữa framework nhưng logic là chuẩn bị → phát hiện → khống chế → loại bỏ → phục hồi → cải tiến.

## 7. Cặp dễ nhầm

| Cặp | Điểm tách |
|---|---|
| Methodology vs Lifecycle model | process framework rộng vs flow phase |
| LOC vs Function Point | source size vs functional size |
| Risk vs Issue | chưa chắc xảy ra vs đã xảy ra |
| Critical Path vs shortest path | longest duration project path vs graph routing concept |
| RAID vs Backup | disk availability vs historical/data recovery |
| SAN vs NAS | block vs file storage |
| VM vs Container | guest OS/hardware abstraction vs shared kernel process isolation |
| RTO vs RPO | thời gian restore service vs lượng data loss theo thời gian |
| Incremental vs Differential | từ backup gần nhất vs từ full gần nhất |
| Authentication vs Authorization | identity vs permission |
| SQLi vs XSS | query/database vs browser/client |
| XSS vs CSRF | inject script vs forge authenticated request |
| IDS vs IPS | detect/alert vs inline block/prevent |
| Hash vs Encryption | one-way digest vs reversible confidentiality |
| Symmetric vs Asymmetric | shared secret nhanh vs key pair |
| Digital Signature vs Encryption | authenticity/integrity vs confidentiality |

## 8. Procedural drills

### Drill 1 — PERT

Activity có O=4, M=7, P=16. Tính expected time theo PERT.

### Drill 2 — Critical Path

Cho path A-B-D = 12 ngày và A-C-D = 15 ngày. Path nào critical trong network đơn giản và project duration tối thiểu là bao nhiêu?

### Drill 3 — RAID

System cần survive đồng thời tối đa hai disk failure trong một parity array. RAID 5 hay RAID 6 phù hợp hơn? Trade-off write là gì?

### Drill 4 — RTO/RPO

Business chấp nhận service down tối đa 30 phút và mất data tối đa 5 phút. Xác định RTO/RPO và giải thích vì sao backup mỗi ngày không đáp ứng RPO.

### Drill 5 — Backup

Full vào Chủ nhật, incremental mỗi ngày. Muốn restore thứ Tư sau backup: cần những backup nào? So sánh nếu Mon–Wed là differential.

### Drill 6 — SQL Injection

Code ghép `"SELECT * FROM users WHERE id='" + input + "'"`. Viết lại defense ở mức concept và giải thích tại sao allowlist đơn độc chưa tốt bằng parameter binding cho query structure.

### Drill 7 — XSS/CSRF

User comment chứa script và được render cho người khác: XSS loại nào có khả năng? Một link độc hại khiến browser đang đăng nhập gửi transfer request: thuộc loại nào?

### Drill 8 — Access Control

Hospital gán quyền theo Doctor/Nurse/Billing role. Đây gần RBAC. Nếu quyền dựa security label Secret/Top Secret do policy trung tâm bắt buộc thì gần model nào?

### Drill 9 — Crypto

Muốn gửi file lớn bảo mật và xác minh người gửi: tại sao hệ thống thực tế thường dùng symmetric encryption cho bulk data rồi asymmetric key/signature cho key/authentication thay vì encrypt toàn file bằng RSA-style primitive?

### Drill 10 — Availability

System có MTBF=999 giờ, MTTR=1 giờ. Tính availability gần đúng và giải thích cách MTTR ảnh hưởng.

## 9. 과락 방지 checklist — Môn 5

Phải tự làm được:

- phân biệt lifecycle/methodology và tailoring;
- giải LOC, FP category, COCOMO concept;
- tính PERT đơn giản và xác định critical path;
- phân biệt risk/issue và response strategy;
- nhận diện quality model/process maturity concept;
- giải topology, redundancy, VLAN, QoS ở mức nền tảng;
- phân biệt COTS/open source/middleware;
- phân biệt RAID 0/1/5/6/10, SAN/NAS;
- phân biệt VM/container, IaaS/PaaS/SaaS, scale up/out;
- tính/giải availability, MTBF/MTTR, RTO/RPO;
- phân biệt full/incremental/differential và cold/warm/hot site;
- phân biệt SQLi/XSS/CSRF/path traversal/command injection;
- giải CIA, authn/authz, session, least privilege;
- phân biệt DAC/MAC/RBAC và MFA factors;
- phân biệt symmetric/asymmetric/hash/signature/PKI;
- phân biệt firewall/IDS/IPS/WAF/VPN;
- nhận diện malware category và incident response flow.

Môn 5 chỉ an toàn khi có thể chuyển nhanh giữa project, infrastructure và security mà không bị mất context.
