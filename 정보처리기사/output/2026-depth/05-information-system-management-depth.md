# Môn 5 — 정보시스템 구축 관리: Deep Dive 2026

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. 소프트웨어 개발 방법론 활용 — Software Development Methodology** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. chất lượng (quality / 품질) và tiến trình (process / 프로세스) Maturity** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Mạch này dùng deep dive information systems làm owner, rồi nối methodology, quality, security, infrastructure và governance.

> Môn 5 có breadth rất lớn: methodology, estimation/dự án (project / 프로젝트) management, mạng (network / 네트워크)/SW/HW/DB construction, hạ tầng (infrastructure / 인프라), availability, secure software và hệ thống (system / 시스템) bảo mật (security / 보안). Đây là môn dễ 과락 nếu chỉ học bảo mật (security / 보안) hoặc chỉ học dự án (project / 프로젝트) management.

## 1. 소프트웨어 개발 방법론 활용 — Software Development Methodology

### 1.1 Methodology không phải vòng đời (lifecycle / 생명주기) mô hình (model / 모델) đơn thuần

Development methodology bao gồm tiến trình (process / 프로세스), role, sản phẩm tạo ra (artifact / 산출물), technique và quy tắc (rule / 규칙) để tổ chức việc phát triển. Waterfall, iterative/incremental, spiral, agile là các cách tổ chức vòng đời (lifecycle / 생명주기) khác nhau; một methodology cụ thể có thể dùng nhiều practice và sản phẩm tạo ra (artifact / 산출물).

Waterfall phù hợp khi yêu cầu (requirement / 요구사항) ổn định và cần phase/gate rõ, nhưng phản hồi (feedback / 피드백) muộn. Iterative phát triển qua nhiều vòng refinement. Incremental giao từng phần functionality. Spiral nhấn mạnh rủi ro (risk / 위험) phân tích (analysis / 분석) theo vòng lặp. Agile nhấn phản hồi (feedback / 피드백), adaptation và delivery ngắn.

### 1.2 Methodology Tailoring

Tailoring là điều chỉnh tiến trình (process / 프로세스) chuẩn theo quy mô, rủi ro (risk / 위험), regulation, nhóm (team / 팀), technology và đặc tả hợp đồng (contract / 계약) của dự án (project / 프로젝트). Tailoring không có nghĩa bỏ tùy tiện sản phẩm tạo ra (artifact / 산출물) khó chịu; thay đổi phải có lý do và vẫn bảo đảm quản trị (governance / 거버넌스)/chất lượng (quality / 품질) cần thiết.

Ví dụ dự án (project / 프로젝트) safety-critical có thể cần documentation, rà soát (review / 검토), traceability và xác minh (verification / 확인) mạnh hơn web nội bộ nhỏ.

### 1.3 Estimation

#### LOC

Lines of mã (code / 코드) estimation dễ hiểu nhưng phụ thuộc ngôn ngữ (language / 언어)/style và khó ước lượng sớm khi thiết kế (design / 설계) chưa rõ.

#### Hàm (function / 함수) điểm (point / 지점)

Hàm (function / 함수) điểm (point / 지점) đo functional kích thước (size / 크기) từ góc nhìn người dùng (user / 사용자), dựa các loại đầu vào (input / 입력)/đầu ra (output / 출력)/truy vấn (query / 쿼리)/tệp (file / 파일)/giao diện (interface / 인터페이스) và độ phức tạp (complexity / 복잡도) weight theo phương pháp cụ thể. Ưu điểm là ít phụ thuộc ngôn ngữ (language / 언어) hơn LOC.

Đề có thể hỏi EI, EO, EQ, ILF, EIF theo hàm (function / 함수) điểm (point / 지점). Cần hiểu category:

- EI: bên ngoài (external / 외부) đầu vào (input / 입력) — dữ liệu (data / 데이터)/điều khiển (control / 제어) vào làm thay đổi trạng thái nội bộ (internal state / 내부 상태).
- EO: bên ngoài (external / 외부) đầu ra (output / 출력) — đầu ra (output / 출력) có processing/derived thông tin (information / 정보).
- EQ: bên ngoài (external / 외부) Inquiry — đầu vào (input / 입력)+đầu ra (output / 출력) inquiry với processing hạn chế.
- ILF: nội bộ (internal / 내부) Logical tệp (file / 파일) — logical dữ liệu (data / 데이터) group do ứng dụng (application / 애플리케이션) quản lý.
- EIF: bên ngoài (external / 외부) giao diện (interface / 인터페이스) tệp (file / 파일) — dữ liệu (data / 데이터) lô-gic (logic / 논리) được ứng dụng (application / 애플리케이션) khác quản lý nhưng ứng dụng (application / 애플리케이션) này đọc/tham chiếu.

#### COCOMO

COCOMO là mô hình chi phí (cost / 비용) estimation dựa software kích thước (size / 크기) và dự án (project / 프로젝트) chế độ (mode / 모드)/parameter theo phiên bản (version / 버전). Các chế độ (mode / 모드) kinh điển: Organic, Semi-detached, Embedded.

Không cần biến COCOMO thành công thức thuộc lòng nếu chưa hiểu: kích thước (size / 크기) lớn hơn và ràng buộc (constraint / 제약조건) phức tạp hơn làm effort tăng phi tuyến theo mô hình (model / 모델).

### 1.4 Schedule mạng (network / 네트워크) — PERT/CPM

Đường găng (critical path / 임계 경로) là đường dẫn (path / 경로) có tổng duration dài nhất trong mạng (network / 네트워크) và quyết định minimum dự án (project / 프로젝트) duration theo mô hình (model / 모델). Activity trên đường găng (critical path / 임계 경로) có total float/slack bằng 0 trong setup cơ bản.

PERT expected thời gian (time / 시간) kinh điển:

`TE = (O + 4M + P) / 6`

O optimistic, M most likely, P pessimistic.

Đường găng (critical path / 임계 경로) không phải đường dẫn (path / 경로) có nhiều activity nhất, mà đường dẫn (path / 경로) có **tổng thời gian dài nhất**.

### 1.5 rủi ro (risk / 위험)

Rủi ro (risk / 위험) = bất định (uncertainty / 불확실성) có impact lên mục tiêu (objective / 목표). rủi ro (risk / 위험) management gồm identification, phân tích (analysis / 분석), phản hồi (response / 응답) planning, monitoring/điều khiển (control / 제어).

Threat phản hồi (response / 응답) thường gồm avoid, mitigate, transfer, accept. Opportunity phản hồi (response / 응답) có exploit, enhance, share, accept theo taxonomy dự án (project / 프로젝트) management phổ biến.

Issue khác rủi ro (risk / 위험): issue đã xảy ra; rủi ro (risk / 위험) chưa chắc xảy ra.

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **1. 소프트웨어 개발 방법론 활용 — Software Development Methodology** xác định đầu vào; **2. chất lượng (quality / 품질) và tiến trình (process / 프로세스) Maturity** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. IT 프로젝트 정보시스템 구축 관리 — IT dự án (project / 프로젝트) / thông tin (information / 정보) hệ thống (system / 시스템) Construction Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. chất lượng (quality / 품질) và tiến trình (process / 프로세스) Maturity

### 2.1 Software chất lượng (quality / 품질)

Chất lượng (quality / 품질) attribute thường gặp: functionality/suitability, độ tin cậy (reliability / 신뢰성), usability, efficiency/hiệu năng (performance / 성능), maintainability, portability, bảo mật (security / 보안), tính tương thích (compatibility / 호환성) tùy tiêu chuẩn (standard / 표준)/phiên bản (version / 버전).

ISO/IEC 9126 là mô hình (model / 모델) cũ thường xuất hiện trong đề/tài liệu lịch sử. ISO/IEC 25010 là mô hình (model / 모델) hiện đại hơn. Khi đề đưa đúng tên tiêu chuẩn (standard / 표준), trả theo taxonomy của tiêu chuẩn (standard / 표준) đó thay vì trộn các phiên bản (version / 버전).

### 2.2 CMMI

CMMI maturity levels truyền thống theo staged biểu diễn (representation / 표현):

1 Initial
2 Managed
3 Defined
4 Quantitatively Managed
5 Optimizing

Mục đích là tiến trình (process / 프로세스) maturity, không phải xếp hạng chất lượng từng sản phẩm cụ thể.

### 2.3 SPICE / ISO/IEC 15504

SPICE đánh giá tiến trình (process / 프로세스) năng lực (capability / 역량) theo mức (level / 수준). Đề có thể hỏi năng lực (capability / 역량)/tiến trình (process / 프로세스) assessment; đừng nhầm với sản phẩm (product / 제품) chất lượng (quality / 품질) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **2. chất lượng (quality / 품질) và tiến trình (process / 프로세스) Maturity** xác định đầu vào; **3. IT 프로젝트 정보시스템 구축 관리 — IT dự án (project / 프로젝트) / thông tin (information / 정보) hệ thống (system / 시스템) Construction Management** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3.1 mạng (network / 네트워크) Construction Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. IT 프로젝트 정보시스템 구축 관리 — IT dự án (project / 프로젝트) / thông tin (information / 정보) hệ thống (system / 시스템) Construction Management

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **3.1 mạng (network / 네트워크) Construction Management** tiếp nhận điểm tựa từ **3. IT 프로젝트 정보시스템 구축 관리 — IT dự án (project / 프로젝트) / thông tin (information / 정보) hệ thống (system / 시스템) Construction Management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3.2 Software Construction Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3.1 mạng (network / 네트워크) Construction Management

Mạng (network / 네트워크) thiết kế (design / 설계) cần topology, bandwidth, độ trễ (latency / 지연 시간), redundancy, segmentation, routing, addressing, bảo mật (security / 보안) zone, availability và manageability.

### Topology

Bus: dùng chung (shared / 공유) backbone, đơn giản nhưng fault backbone ảnh hưởng rộng. Star: nút (node / 노드) nối central thiết bị (device / 장치), dễ quản lý; central thiết bị (device / 장치) là trọng yếu (critical / 중요) điểm (point / 지점) nếu không redundant. Ring: nút (node / 노드) theo vòng. Mesh: nhiều đường redundancy nhưng chi phí (cost / 비용)/độ phức tạp (complexity / 복잡도) cao. cây (tree / 트리)/Hierarchical: phân tầng, phổ biến trong enterprise thiết kế (design / 설계).

### Redundancy

Redundancy loại single điểm (point / 지점) of thất bại (failure / 실패) nhưng cần giao thức (protocol / 프로토콜)/cơ chế failover. Chỉ mua hai thiết bị (device / 장치) chưa đủ high availability nếu cả hai phụ thuộc cùng power, switch, rack hoặc cấu hình (configuration / 구성) lỗi chung.

### VLAN

VLAN chia broadcast lĩnh vực (domain / 도메인) lô-gic (logic / 논리) trên switch hạ tầng (infrastructure / 인프라). VLAN không tự động là ranh giới bảo mật (security boundary / 보안 경계) hoàn chỉnh; inter-VLAN routing/firewall chính sách (policy / 정책) vẫn cần kiểm soát.

### QoS

Chất lượng (quality / 품질) of dịch vụ (service / 서비스) ưu tiên/điều tiết traffic theo yêu cầu (requirement / 요구사항) như độ trễ (latency / 지연 시간), jitter, bandwidth, mất mát (loss / 손실). Voice/video thường nhạy độ trễ (latency / 지연 시간)/jitter hơn tệp (file / 파일) transfer.

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **3.2 Software Construction Management** tiếp nhận điểm tựa từ **3.1 mạng (network / 네트워크) Construction Management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3.3 Hardware Construction Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3.2 Software Construction Management

Cần quản lý yêu cầu (requirement / 요구사항), kiến trúc (architecture / 아키텍처), phụ thuộc (dependency / 의존성), phiên bản (version / 버전), bản dựng (build / 빌드), kiểm thử (test / 테스트), bản phát hành (release / 릴리스), cấu hình (configuration / 구성) và triển khai (deployment / 배포).

COTS — Commercial Off-The-Shelf — mua sản phẩm có sẵn; giảm development thời gian (time / 시간) nhưng tăng phụ thuộc (dependency / 의존성)/vendor/customization ràng buộc (constraint / 제약조건). Open nguồn (source / 소스) cho quyền sử dụng/nguồn (source / 소스) theo license nhưng vẫn cần license compliance, maintenance và bảo mật (security / 보안) quản trị (governance / 거버넌스).

### Middleware

Middleware nằm giữa ứng dụng (application / 애플리케이션)/thành phần (component / 컴포넌트) để cung cấp communication/tích hợp (integration / 통합) dịch vụ (service / 서비스). Category có RPC, message-oriented middleware, giao dịch (transaction / 트랜잭션) monitor, đối tượng (object / 객체) broker, web/ứng dụng (application / 애플리케이션) máy chủ (server / 서버) và tích hợp (integration / 통합) middleware.

Middleware khác OS và khác nghiệp vụ (business / 비즈니스) ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **3.3 Hardware Construction Management** tiếp nhận điểm tựa từ **3.2 Software Construction Management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3.4 cơ sở dữ liệu (database / 데이터베이스) Construction Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3.3 Hardware Construction Management

### CPU / bộ nhớ (memory / 메모리) / lưu trữ (storage / 저장소)

CPU sức chứa (capacity / 용량) không chỉ clock speed; cốt lõi (core / 핵심), kiến trúc (architecture / 아키텍처), tải công việc (workload / 워크로드), bộ nhớ đệm (cache / 캐시) và tính đồng thời (concurrency / 동시성) ảnh hưởng thông lượng (throughput / 처리량). bộ nhớ (memory / 메모리) thiếu gây paging/swapping và hiệu năng (performance / 성능) collapse. lưu trữ (storage / 저장소) cần nhìn độ trễ (latency / 지연 시간), IOPS, thông lượng (throughput / 처리량), sức chứa (capacity / 용량), durability.

### RAID

RAID 0: striping, không redundancy; hiệu năng (performance / 성능)/sức chứa (capacity / 용량) tốt nhưng một disk thất bại (fail / 실패) có thể mất array.
RAID 1: mirroring, redundancy tốt, usable sức chứa (capacity / 용량) khoảng 50% với pair truyền thống.
RAID 5: striping + phân tán (distributed / 분산) single parity, chịu một disk thất bại (failure / 실패), ghi (write / 쓰기) penalty.
RAID 6: dual parity, chịu hai disk thất bại (failure / 실패), ghi (write / 쓰기) penalty cao hơn.
RAID 10: mirror + stripe, hiệu năng (performance / 성능) và redundancy tốt nhưng tốn sức chứa (capacity / 용량).

RAID không thay backup. RAID bảo vệ availability khi disk thất bại (failure / 실패); backup bảo vệ logical deletion, corruption, ransomware, disaster và historical restore tùy thiết kế (design / 설계).

### SAN vs NAS

SAN cung cấp khối (block / 블록) lưu trữ (storage / 저장소) qua lưu trữ (storage / 저장소) mạng (network / 네트워크). NAS cung cấp tệp (file / 파일) dịch vụ (service / 서비스) qua mạng (network / 네트워크). Đây là lớp trừu tượng (abstraction / 추상화) khác nhau: khối (block / 블록) vs tệp (file / 파일).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **3.3 Hardware Construction Management** nêu điều cần giải thích; **3.4 cơ sở dữ liệu (database / 데이터베이스) Construction Management** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3.5 Virtualization và Cloud** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3.4 cơ sở dữ liệu (database / 데이터베이스) Construction Management

Cơ sở dữ liệu (database / 데이터베이스) construction management ở Môn 5 thiên về sức chứa (capacity / 용량), HA, backup/khôi phục (recovery / 복구), hiệu năng (performance / 성능), bảo mật (security / 보안) và thao tác (operation / 연산) hơn normalization chi tiết của Môn 3.

Phải xem liên kết (connection / 연결) tải (load / 로드), giao dịch (transaction / 트랜잭션) thông lượng (throughput / 처리량), lưu trữ (storage / 저장소) growth, chỉ mục (index / 인덱스), backup cửa sổ (window / 윈도우), replication, failover, RPO/RTO và monitoring.

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **3.4 cơ sở dữ liệu (database / 데이터베이스) Construction Management** nêu điều cần giải thích; **3.5 Virtualization và Cloud** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Availability, DR, Backup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3.5 Virtualization và Cloud

### Virtual Machine vs bộ chứa (container / 컨테이너)

VM virtualize machine/hardware lớp trừu tượng (abstraction / 추상화) và mỗi VM thường có guest OS riêng. bộ chứa (container / 컨테이너) share host kernel và isolate tiến trình (process / 프로세스)/tài nguyên (resource / 자원), nên nhẹ hơn nhưng isolation mô hình (model / 모델) khác.

### IaaS / PaaS / SaaS

IaaS: người dùng (user / 사용자) quản OS/thời gian chạy (runtime / 런타임)/app nhiều hơn, provider quản hạ tầng (infrastructure / 인프라) vật lý (physical / 물리적)/virtualization. PaaS: provider quản nền tảng (platform / 플랫폼)/thời gian chạy (runtime / 런타임) nhiều hơn, người dùng (user / 사용자) tập trung ứng dụng (application / 애플리케이션)/dữ liệu (data / 데이터). SaaS: provider vận hành ứng dụng (application / 애플리케이션) hoàn chỉnh, người dùng (user / 사용자) chủ yếu sử dụng/configure.

### Công khai (public / 공개) / Private / Hybrid Cloud

Công khai (public / 공개) dùng provider dùng chung (shared / 공유) hạ tầng (infrastructure / 인프라)/dịch vụ (service / 서비스). Private dành cho một organization theo mô hình (model / 모델) riêng. Hybrid kết nối/combine private và công khai (public / 공개) môi trường (environment / 환경).

### Quy mô (scale / 규모) Up vs quy mô (scale / 규모) Out

Quy mô (scale / 규모) Up tăng tài nguyên (resource / 자원) của một nút (node / 노드). quy mô (scale / 규모) Out thêm nút (node / 노드). quy mô (scale / 규모) out thường cần ứng dụng (application / 애플리케이션)/dữ liệu (data / 데이터) thiết kế (design / 설계) hỗ trợ phân phối (distribution / 분포).

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **3.5 Virtualization và Cloud** cho ta quy tắc; **4. Availability, DR, Backup** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **5. 소프트웨어 개발 보안 구축 — Secure Software Development** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Availability, DR, Backup

### 4.1 Availability

Availability có thể biểu diễn gần đúng:

`Availability = MTBF / (MTBF + MTTR)`

MTBF tăng hoặc MTTR giảm thì availability tăng.

### 4.2 RTO vs RPO

RTO — khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표) — thời gian tối đa chấp nhận để khôi phục dịch vụ (service / 서비스) sau sự cố. RPO — khôi phục (recovery / 복구) điểm (point / 지점) mục tiêu (objective / 목표) — lượng mất dữ liệu tối đa tính theo thời gian.

Ví dụ RTO 2h, RPO 15m nghĩa dịch vụ (service / 서비스) cần khôi phục trong 2 giờ và dữ liệu (data / 데이터) mất mát (loss / 손실) không quá khoảng 15 phút theo mục tiêu (objective / 목표).

### 4.3 Backup Types

Full Backup sao chép toàn bộ selected dữ liệu (data / 데이터). Incremental sao chép thay đổi từ backup gần nhất bất kể loại; restore thường cần full + chuỗi incremental. Differential sao chép thay đổi kể từ full gần nhất; restore thường cần full + differential mới nhất.

### 4.4 DR Site

Cold Site có facility nhưng ít equipment/dữ liệu (data / 데이터) ready; khôi phục (recovery / 복구) chậm, chi phí (cost / 비용) thấp hơn. Warm Site có một phần hệ thống (system / 시스템)/dữ liệu (data / 데이터) ready. Hot Site gần môi trường vận hành (production / 운영 환경) replica và khôi phục (recovery / 복구) nhanh hơn nhưng chi phí (cost / 비용) cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **4. Availability, DR, Backup** cho ta quy tắc; **5. 소프트웨어 개발 보안 구축 — Secure Software Development** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **5.1 bảo mật (security / 보안) Goals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. 소프트웨어 개발 보안 구축 — Secure Software Development

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **5.1 bảo mật (security / 보안) Goals** tiếp nhận điểm tựa từ **5. 소프트웨어 개발 보안 구축 — Secure Software Development** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5.1 bảo mật (security / 보안) Goals

CIA triad:

- Confidentiality — chỉ thực thể (entity / 엔터티) được phép đọc.
- Integrity — dữ liệu không bị thay đổi trái phép.
- Availability — dịch vụ (service / 서비스)/dữ liệu (data / 데이터) sẵn sàng khi cần.

Thêm Authentication xác minh định danh (identity / 식별자), Authorization quyết định quyền, Accountability/Auditing ghi nhận hành động (action / 동작).

### 5.2 đầu vào (input / 입력) kiểm tra hợp lệ (validation / 검증)

Đầu vào (input / 입력) từ máy khách (client / 클라이언트), tệp (file / 파일), API, DB hay hệ thống bên ngoài (external system / 외부 시스템) đều không nên tin tưởng mặc định. kiểm tra hợp lệ (validation / 검증) dựa allowlist/kiểu (type / 타입)/phạm vi (range / 범위)/length/ngữ cảnh (context / 맥락); đầu ra (output / 출력) encoding tùy sink.

### 5.3 SQL Injection

SQL Injection xảy ra khi untrusted đầu vào (input / 입력) được ghép vào SQL làm thay đổi truy vấn (query / 쿼리) cấu trúc (structure / 구조). Defense chính: parameterized truy vấn (query / 쿼리)/prepared statement, ORM binding đúng cách, least privilege, kiểm tra hợp lệ (validation / 검증) bổ trợ.

Escape thủ công không nên là defense duy nhất.

### 5.4 XSS

Cross-Site Scripting đưa script/content độc hại vào ngữ cảnh (context / 맥락) trình duyệt (browser / 브라우저) của người dùng (user / 사용자). Loại thường gặp: Stored, Reflected, DOM-based.

Defense phụ thuộc ngữ cảnh (context / 맥락): đầu ra (output / 출력) encoding/escaping đúng ngữ cảnh (context / 맥락), template auto-escape, sanitize HTML khi cần cho phép markup, CSP như defense-in-depth.

SQL Injection nhắm truy vấn (query / 쿼리)/cơ sở dữ liệu (database / 데이터베이스); XSS nhắm trình duyệt (browser / 브라우저)/máy khách (client / 클라이언트) ngữ cảnh (context / 맥락). Đừng nhầm vì cả hai đều bắt đầu từ đầu vào (input / 입력) không tin cậy.

### 5.5 CSRF

CSRF lợi dụng trình duyệt (browser / 브라우저) của người dùng (user / 사용자) đã authenticated gửi yêu cầu (request / 요청) mà người dùng (user / 사용자) không mong muốn. Defense: anti-CSRF đơn vị từ (token / 토큰), SameSite cookie phù hợp, kiểm tra Origin/Referer trong ngữ cảnh (context / 맥락) thích hợp, re-authentication cho hành động (action / 동작) nhạy cảm.

CSRF khác XSS: CSRF lợi dụng trust máy chủ (server / 서버) dành cho trình duyệt (browser / 브라우저)/session; XSS inject mã (code / 코드) vào page/ngữ cảnh (context / 맥락) máy khách (client / 클라이언트).

### 5.6 đường dẫn (path / 경로) Traversal

Attacker dùng đường dẫn (path / 경로) như `../` để truy cập tệp (file / 파일) ngoài thư mục cho phép. Defense: canonicalization an toàn, allowlist identifier/đường dẫn (path / 경로), không ghép raw người dùng (user / 사용자) đường dẫn (path / 경로) vào filesystem truy cập (access / 접근).

### 5.7 Command Injection

Untrusted đầu vào (input / 입력) đi vào shell/hệ thống (system / 시스템) command có thể thay đổi command. Tránh shell khi có API trực tiếp, parameterize argument đúng cách, allowlist và least privilege.

### 5.8 bộ nhớ (memory / 메모리) an toàn (safety / 안전)

Buffer overflow, use-after-free, integer overflow có thể dẫn tới crash hoặc mã (code / 코드) thực thi (execution / 실행) trong low-level ngôn ngữ (language / 언어). Defense gồm bounds checking, safe thư viện (library / 라이브러리)/ngôn ngữ (language / 언어), trình biên dịch (compiler / 컴파일러) protection, ASLR/DEP như defense-in-depth.

### 5.9 lỗi (error / 오류) Handling

Không lộ dấu vết ngăn xếp (stack trace / 스택 트레이스), SQL detail, secret/đường dẫn (path / 경로) nội bộ cho máy khách (client / 클라이언트). Log đủ để điều tra nhưng không log password/đơn vị từ (token / 토큰)/private key hoặc sensitive dữ liệu (data / 데이터) không cần thiết.

### 5.10 Secure Session

Session ID phải unpredictable, rotate sau login/privilege thay đổi (change / 변경), expire hợp lý, cookie dùng Secure/HttpOnly/SameSite theo yêu cầu (requirement / 요구사항). Logout phải invalidate session phía máy chủ (server / 서버) khi kiến trúc (architecture / 아키텍처) yêu cầu.

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6. 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안)** tiếp nhận điểm tựa từ **5.1 bảo mật (security / 보안) Goals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.1 Threat, Vulnerability, rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.1 Threat, Vulnerability, rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **6. 시스템 보안 구축 — hệ thống (system / 시스템) bảo mật (security / 보안)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.2 Malware** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.1 Threat, Vulnerability, rủi ro (risk / 위험)

Asset là thứ có giá trị. Threat là nguồn/sự kiện có khả năng gây hại. Vulnerability là weakness. rủi ro (risk / 위험) liên quan likelihood và impact khi threat khai thác vulnerability.

Điều khiển (control / 제어) giảm likelihood/impact hoặc hỗ trợ detect/recover.

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.2 Malware** tiếp nhận điểm tựa từ **6.1 Threat, Vulnerability, rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.3 kiểm soát truy cập (access control / 접근 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.2 Malware

Virus cần host/tệp (file / 파일) và thường lây khi host chạy. Worm tự lan qua mạng (network / 네트워크). Trojan giả dạng hữu ích nhưng chứa hành vi độc hại. Ransomware mã hóa/khóa dữ liệu (data / 데이터) để tống tiền. Spyware thu thập thông tin. Rootkit che giấu/duy trì quyền sâu.

Botnet là tập compromised hosts bị điều khiển (control / 제어); DDoS có thể dùng botnet nhưng botnet không đồng nghĩa DDoS.

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.3 kiểm soát truy cập (access control / 접근 제어)** tiếp nhận điểm tựa từ **6.2 Malware** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.4 Authentication Factors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.3 kiểm soát truy cập (access control / 접근 제어)

DAC — Discretionary kiểm soát truy cập (access control / 접근 제어) — đơn vị sở hữu (owner / 오너)/tài nguyên (resource / 자원) controller quyết quyền. MAC — Mandatory kiểm soát truy cập (access control / 접근 제어) — chính sách (policy / 정책)/label bắt buộc, người dùng (user / 사용자) không tự ý thay đổi. RBAC — Role-Based kiểm soát truy cập (access control / 접근 제어) — quyền gắn role rồi người dùng (user / 사용자) nhận role.

Least Privilege: chỉ cấp quyền tối thiểu cần thiết. Separation of Duties: chia trách nhiệm nhạy cảm giữa nhiều actor. Need-to-Know: chỉ truy cập thông tin cần cho nhiệm vụ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.4 Authentication Factors** tiếp nhận điểm tựa từ **6.3 kiểm soát truy cập (access control / 접근 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.5 Cryptography** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.4 Authentication Factors

Something you know: password/PIN. Something you have: đơn vị từ (token / 토큰)/card/thiết bị (device / 장치). Something you are: biometric. Somewhere you are / something you do đôi khi được dùng thêm trong taxonomy.

Multi-factor cần ít nhất hai factor **khác loại**. Hai password không phải 2FA.

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.5 Cryptography** tiếp nhận điểm tựa từ **6.4 Authentication Factors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.6 PKI và Certificate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.5 Cryptography

### Symmetric Encryption

Cùng secret key hoặc key tương đương cho encrypt/decrypt. Nhanh, phù hợp bulk dữ liệu (data / 데이터) nhưng key phân phối (distribution / 분포) khó.

### Asymmetric Encryption

Công khai (public / 공개)/private key pair. Hỗ trợ key exchange, encryption use trường hợp (case / 사례) và digital signature. Chậm hơn symmetric cho bulk dữ liệu (data / 데이터).

### Băm (hash / 해시)

Băm (hash / 해시) tạo fixed-length digest, one-way theo mục tiêu thiết kế. Dùng integrity, password xác minh (verification / 확인) với password hashing scheme phù hợp, digital signature chuỗi xử lý (pipeline / 파이프라인). băm (hash / 해시) không phải encryption.

### Digital Signature

Signature dùng private key của signer để tạo signature trên dữ liệu (data / 데이터)/băm (hash / 해시) theo scheme; verifier dùng công khai (public / 공개) key xác minh authenticity/integrity và hỗ trợ non-repudiation trong ngữ cảnh (context / 맥락) phù hợp.

Encryption bằng công khai (public / 공개) key của receiver và signature bằng private key của sender phục vụ mục tiêu khác nhau.

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.6 PKI và Certificate** tiếp nhận điểm tựa từ **6.5 Cryptography** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.7 mạng (network / 네트워크) bảo mật (security / 보안) Devices** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.6 PKI và Certificate

PKI quản công khai (public / 공개) key/certificate/trust. CA ký certificate binding định danh (identity / 식별자)/lĩnh vực (domain / 도메인) với công khai (public / 공개) key. Certificate kiểm tra hợp lệ (validation / 검증) cần chuỗi (chain / 사슬) of trust, validity, hostname/chính sách (policy / 정책) và revocation/status theo hệ thống (system / 시스템).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.7 mạng (network / 네트워크) bảo mật (security / 보안) Devices** tiếp nhận điểm tựa từ **6.6 PKI và Certificate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.8 bảo mật (security / 보안) Protocols** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.7 mạng (network / 네트워크) bảo mật (security / 보안) Devices

Firewall filter traffic theo quy tắc (rule / 규칙). IDS detect suspicious activity và alert. IPS nằm inline/active hơn để khối (block / 블록)/prevent. WAF tập trung HTTP/web ứng dụng (application / 애플리케이션) attack mẫu (pattern / 패턴). Proxy trung gian yêu cầu (request / 요청); reverse proxy đứng trước máy chủ (server / 서버), có thể tải (load / 로드) balance/TLS termination/bảo mật (security / 보안) hàm (function / 함수).

VPN tạo protected tunnel qua untrusted mạng (network / 네트워크) bằng giao thức (protocol / 프로토콜)/cryptography phù hợp.

### IDS detection

Signature-based tốt với mẫu (pattern / 패턴) đã biết nhưng yếu với attack mới/biến thể. Anomaly-based phát hiện lệch baseline nhưng dễ false positive và cần tuning.

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.8 bảo mật (security / 보안) Protocols** tiếp nhận điểm tựa từ **6.7 mạng (network / 네트워크) bảo mật (security / 보안) Devices** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.9 AAA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.8 bảo mật (security / 보안) Protocols

TLS bảo vệ vận chuyển (transport / 전송) session của nhiều ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜); HTTPS là HTTP over TLS. SSH cung cấp secure remote login/tunneling. IPsec bảo vệ ở mạng (network / 네트워크) tầng (layer / 계층) concept, với AH/ESP trong taxonomy truyền thống. S/MIME/PGP liên quan email/content bảo mật (security / 보안).

Đừng học “giao thức (protocol / 프로토콜) nào an toàn” theo tên; hiểu tầng (layer / 계층) và mục tiêu bảo vệ.

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.9 AAA** tiếp nhận điểm tựa từ **6.8 bảo mật (security / 보안) Protocols** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.10 Logging, Monitoring, sự cố (incident / 인시던트) phản hồi (response / 응답)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.9 AAA

Authentication: bạn là ai? Authorization: bạn được làm gì? Accounting/Auditing: bạn đã làm gì/usage ra sao?

RADIUS/TACACS+ có thể xuất hiện trong ngữ cảnh (context / 맥락) AAA truy cập mạng (network access / 네트워크 접근)/admin. Không cần nhớ mọi chi tiết vendor-specific trước khi phân biệt ba chữ A.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.10 Logging, Monitoring, sự cố (incident / 인시던트) phản hồi (response / 응답)** tiếp nhận điểm tựa từ **6.9 AAA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Cặp dễ nhầm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.10 Logging, Monitoring, sự cố (incident / 인시던트) phản hồi (response / 응답)

Bảo mật (security / 보안) log cần timestamp đồng bộ, định danh (identity / 식별자), sự kiện (event / 이벤트), nguồn (source / 소스), kết quả (result / 결과) và ngữ cảnh (context / 맥락) cần thiết. Centralized logging/SIEM giúp correlation nhưng chất lượng phụ thuộc log nguồn (source / 소스) và quy tắc (rule / 규칙).

Sự cố (incident / 인시던트) phản hồi (response / 응답) luồng (flow / 흐름) thường gồm preparation, detection/phân tích (analysis / 분석), containment, eradication, khôi phục (recovery / 복구), lessons learned theo khung phần mềm (framework / 프레임워크) cụ thể. Thứ tự tên có thể khác giữa khung phần mềm (framework / 프레임워크) nhưng lô-gic (logic / 논리) là chuẩn bị → phát hiện → khống chế → loại bỏ → phục hồi → cải tiến.

> **Chuyển mạch:** Trong **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **6.10 Logging, Monitoring, sự cố (incident / 인시던트) phản hồi (response / 응답)** đã nêu tiêu chí phân biệt, còn **7. Cặp dễ nhầm** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Procedural drills** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Cặp dễ nhầm

| Cặp | Điểm tách |
|---|---|
| Methodology vs vòng đời (lifecycle / 생명주기) mô hình (model / 모델) | tiến trình (process / 프로세스) khung phần mềm (framework / 프레임워크) rộng vs luồng (flow / 흐름) phase |
| LOC vs hàm (function / 함수) điểm (point / 지점) | nguồn (source / 소스) kích thước (size / 크기) vs functional kích thước (size / 크기) |
| rủi ro (risk / 위험) vs Issue | chưa chắc xảy ra vs đã xảy ra |
| đường găng (critical path / 임계 경로) vs shortest đường dẫn (path / 경로) | longest duration dự án (project / 프로젝트) đường dẫn (path / 경로) vs đồ thị (graph / 그래프) routing concept |
| RAID vs Backup | disk availability vs historical/dữ liệu (data / 데이터) khôi phục (recovery / 복구) |
| SAN vs NAS | khối (block / 블록) vs tệp (file / 파일) lưu trữ (storage / 저장소) |
| VM vs bộ chứa (container / 컨테이너) | guest OS/hardware lớp trừu tượng (abstraction / 추상화) vs dùng chung (shared / 공유) kernel tiến trình (process / 프로세스) isolation |
| RTO vs RPO | thời gian restore dịch vụ (service / 서비스) vs lượng dữ liệu (data / 데이터) mất mát (loss / 손실) theo thời gian |
| Incremental vs Differential | từ backup gần nhất vs từ full gần nhất |
| Authentication vs Authorization | định danh (identity / 식별자) vs permission |
| SQLi vs XSS | truy vấn (query / 쿼리)/cơ sở dữ liệu (database / 데이터베이스) vs trình duyệt (browser / 브라우저)/máy khách (client / 클라이언트) |
| XSS vs CSRF | inject script vs forge authenticated yêu cầu (request / 요청) |
| IDS vs IPS | detect/alert vs inline khối (block / 블록)/prevent |
| băm (hash / 해시) vs Encryption | one-way digest vs reversible confidentiality |
| Symmetric vs Asymmetric | dùng chung (shared / 공유) secret nhanh vs key pair |
| Digital Signature vs Encryption | authenticity/integrity vs confidentiality |

> **Chuyển mạch:** Ở chặng này của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **7. Cặp dễ nhầm** đã nêu tiêu chí phân biệt, còn **8. Procedural drills** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. 과락 방지 checklist — Môn 5** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Procedural drills

### Drill 1 — PERT

Activity có O=4, M=7, P=16. Tính expected thời gian (time / 시간) theo PERT.

### Drill 2 — đường găng (critical path / 임계 경로)

Cho đường dẫn (path / 경로) A-B-D = 12 ngày và A-C-D = 15 ngày. đường dẫn (path / 경로) nào trọng yếu (critical / 중요) trong mạng (network / 네트워크) đơn giản và dự án (project / 프로젝트) duration tối thiểu là bao nhiêu?

### Drill 3 — RAID

Hệ thống (system / 시스템) cần survive đồng thời tối đa hai disk thất bại (failure / 실패) trong một parity array. RAID 5 hay RAID 6 phù hợp hơn? sự đánh đổi (trade-off / 트레이드오프) ghi (write / 쓰기) là gì?

### Drill 4 — RTO/RPO

Nghiệp vụ (business / 비즈니스) chấp nhận dịch vụ (service / 서비스) down tối đa 30 phút và mất dữ liệu (data / 데이터) tối đa 5 phút. Xác định RTO/RPO và giải thích vì sao backup mỗi ngày không đáp ứng RPO.

### Drill 5 — Backup

Full vào Chủ nhật, incremental mỗi ngày. Muốn restore thứ Tư sau backup: cần những backup nào? So sánh nếu Mon–Wed là differential.

### Drill 6 — SQL Injection

Mã (code / 코드) ghép `"SELECT * FROM users WHERE id='" + input + "'"`. Viết lại defense ở mức concept và giải thích tại sao allowlist đơn độc chưa tốt bằng parameter binding cho truy vấn (query / 쿼리) cấu trúc (structure / 구조).

### Drill 7 — XSS/CSRF

Người dùng (user / 사용자) comment chứa script và được kết xuất (render / 렌더링) cho người khác: XSS loại nào có khả năng? Một link độc hại khiến trình duyệt (browser / 브라우저) đang đăng nhập gửi transfer yêu cầu (request / 요청): thuộc loại nào?

### Drill 8 — kiểm soát truy cập (access control / 접근 제어)

Hospital gán quyền theo Doctor/Nurse/Billing role. Đây gần RBAC. Nếu quyền dựa bảo mật (security / 보안) label Secret/Top Secret do chính sách (policy / 정책) trung tâm bắt buộc thì gần mô hình (model / 모델) nào?

### Drill 9 — Crypto

Muốn gửi tệp (file / 파일) lớn bảo mật và xác minh người gửi: tại sao hệ thống thực tế thường dùng symmetric encryption cho bulk dữ liệu (data / 데이터) rồi asymmetric key/signature cho key/authentication thay vì encrypt toàn tệp (file / 파일) bằng RSA-style thành phần nguyên thủy (primitive / 기본 요소)?

### Drill 10 — Availability

Hệ thống (system / 시스템) có MTBF=999 giờ, MTTR=1 giờ. Tính availability gần đúng và giải thích cách MTTR ảnh hưởng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 5 — 정보시스템 구축 관리: Deep Dive 2026**, **9. 과락 방지 checklist — Môn 5** tiếp nhận điểm tựa từ **8. Procedural drills** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 9. 과락 방지 checklist — Môn 5

Phải tự làm được:

- phân biệt vòng đời (lifecycle / 생명주기)/methodology và tailoring;
- giải LOC, FP category, COCOMO concept;
- tính PERT đơn giản và xác định đường găng (critical path / 임계 경로);
- phân biệt rủi ro (risk / 위험)/issue và phản hồi (response / 응답) chiến lược (strategy / 전략);
- nhận diện chất lượng (quality / 품질) mô hình (model / 모델)/tiến trình (process / 프로세스) maturity concept;
- giải topology, redundancy, VLAN, QoS ở mức nền tảng;
- phân biệt COTS/open nguồn (source / 소스)/middleware;
- phân biệt RAID 0/1/5/6/10, SAN/NAS;
- phân biệt VM/bộ chứa (container / 컨테이너), IaaS/PaaS/SaaS, quy mô (scale / 규모) up/out;
- tính/giải availability, MTBF/MTTR, RTO/RPO;
- phân biệt full/incremental/differential và cold/warm/hot site;
- phân biệt SQLi/XSS/CSRF/đường dẫn (path / 경로) traversal/command injection;
- giải CIA, authn/authz, session, least privilege;
- phân biệt DAC/MAC/RBAC và MFA factors;
- phân biệt symmetric/asymmetric/băm (hash / 해시)/signature/PKI;
- phân biệt firewall/IDS/IPS/WAF/VPN;
- nhận diện malware category và sự cố (incident / 인시던트) phản hồi (response / 응답) luồng (flow / 흐름).

Môn 5 chỉ an toàn khi có thể chuyển nhanh giữa dự án (project / 프로젝트), hạ tầng (infrastructure / 인프라) và bảo mật (security / 보안) mà không bị mất ngữ cảnh (context / 맥락).

> **Bàn giao:** Sau **9. 과락 방지 checklist — Môn 5**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
