# Master Coverage kiểm tra (audit / 감사) — học tập (learning / 학습) Docs

> Bản đồ cấp repository để nối các thư viện chuẩn gốc (canonical / 정본), xác định đơn vị sở hữu (owner / 오너) của từng khái niệm và chọn đợt mở rộng tiếp theo. tệp (file / 파일) này không thay thế `COVERAGE_AUDIT.md` của từng lĩnh vực (domain / 도메인); nó trả lời câu hỏi **toàn bộ học tập (learning / 학습) hệ thống (system / 시스템) đang thiếu gì, nội dung nào đã đủ, và nên nối các lĩnh vực (domain / 도메인) theo thứ tự nào**.

## Trạng thái kiểm tra (audit / 감사)

- **Ngày kiểm tra:** 2026-09-28.
- **chuẩn gốc (canonical / 정본) map:** [`CATALOG.md`](./CATALOG.md).
- **lần ghi nhận (commit / 커밋) nền khi kiểm tra:** `043523f` (`main` và `origin/main` đang cùng trỏ tới commit này).
- **Phạm vi:** toàn bộ chuẩn gốc (canonical / 정본) entries trong `CATALOG.md`, README/điểm vào (entrypoint / 진입점), coverage kiểm tra (audit / 감사) hiện có và các thư mục liên kết (connection / 연결)/advanced/case-study liên quan.
- **Giới hạn:** đây là kiểm tra (audit / 감사) cấu trúc và phụ thuộc (dependency / 의존성) ở cấp repository; chiều sâu chuyên môn của từng topic tiếp tục do coverage kiểm tra (audit / 감사) của lĩnh vực (domain / 도메인) sở hữu. Không dùng tệp (file / 파일) này để nhân bản prose đã có.

Worktree đang có nhiều thay đổi chưa lần ghi nhận (commit / 커밋) từ các đợt biên soạn trước. kiểm tra (audit / 감사) này chỉ bổ sung bản đồ và không reset, xoá hoặc ghi đè các thay đổi đó.

## Kết luận điều hành

Repository đã vượt qua giai đoạn “thiếu lĩnh vực (domain / 도메인) cơ bản”. Các khối được gợi ý trong cuộc rà soát (review / 검토) đều đã có đơn vị sở hữu (owner / 오너) đáng tin cậy:

1. **Khoa học máy tính (computer science / 컴퓨터 과학) foundations:** kiến trúc (architecture / 아키텍처), algorithms, OS, programming languages, databases, networks/phân tán (distributed / 분산) các hệ thống (systems / 시스템들), software các hệ thống (systems / 시스템들) và bảo mật (security / 보안).
2. **Software kiến trúc (architecture / 아키텍처) / hệ thống (system / 시스템) thiết kế (design / 설계):** nằm ở giao điểm `computer_science/08_software_systems`, `06_networks_distributed_systems`, `10_backend/backend_core` và `devops_platform_engineering`.
3. **Linux + hạ tầng (infrastructure / 인프라) + cloud/DevOps:** `linux/` và `devops_platform_engineering/` đã là hai nhánh học (track / 트랙) chuẩn gốc (canonical / 정본) riêng.
4. **bảo mật (security / 보안) kỹ thuật (engineering / 엔지니어링):** có đơn vị sở hữu (owner / 오너) trong Khoa học máy tính (computer science / 컴퓨터 과학), Linux, backend định danh (identity / 식별자)/bảo mật (security / 보안) và DevOps bảo mật (security / 보안).
5. **cơ sở dữ liệu (database / 데이터베이스) kỹ thuật (engineering / 엔지니어링):** có ba lớp bổ trợ nhau: `computer_science/05_data_databases`, `sql/` và persistence/data-engineering tracks.
6. **AI/ML foundations:** `computer_science/02_artificial_intelligence/` đi cùng nền toán trong `mathematics/` và có nhánh dữ liệu (data / 데이터)/MLOps/LLMOps.
7. **kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링):** đã có vòng đời (lifecycle / 생명주기), chuỗi xử lý (pipeline / 파이프라인) ngữ nghĩa (semantics / 의미론), lưu trữ (storage / 저장소), phân tán (distributed / 분산)/streaming, orchestration, warehouse/lakehouse, quản trị (governance / 거버넌스) và môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) studies.
8. **Economics → finance → investment:** `economics/`, `investing/` và Korea nghiệp vụ (business / 비즈니스)/economy đã có ranh giới (boundary / 경계) rõ thay vì trộn lý thuyết (theory / 이론) với ứng dụng (application / 애플리케이션).
9. **xác suất (probability / 확률)/statistics:** đã có không gian tên (namespace / 네임스페이스) đầy đủ trong `mathematics/06_probability_statistics/`, econometrics trong Economics và research-design trong `research_methods/`.
10. **Psychology mở rộng ngoài Jung:** psychology đã có brain/mind, cognition, development, xã hội (social / 사회적), mental health, intervention, applied psychology và historical-theory ranh giới (boundary / 경계).
11. **Philosophy + lô-gic (logic / 논리) + epistemology:** đã có đơn vị sở hữu (owner / 오너) riêng và các liên kết (connection / 연결) sang science, mathematics, computation, psychology và AI.
12. **Practical life kiến thức (knowledge / 지식):** Korea law/civic life, investing, Korean nghiệp vụ (business / 비즈니스)/economy, psychology applied và PMP đã tạo nền; phần còn mỏng là một tuyến (route / 경로) tích hợp personal finance/healthcare/communication/career.

Vì vậy đợt tiếp theo không nên tạo thêm các lĩnh vực (domain / 도메인) trùng lặp. Giá trị cao nhất hiện nằm ở **liên kết (connection / 연결) tầng (layer / 계층), chuẩn gốc (canonical / 정본) quyền sở hữu (ownership / 소유권) và decision-oriented practice**.

## Ma trận coverage cấp repository

| Trục | đơn vị sở hữu (owner / 오너) chuẩn gốc (canonical / 정본) | Trạng thái hiện tại | Khoảng trống cần xử lý |
|---|---|---|---|
| Toán, xác suất, thống kê, tối ưu | `mathematics/` | **Mạnh**; xác suất (probability / 확률)/statistics, Bayesian, stochastic processes, tối ưu hóa (optimization / 최적화) và math connections đã có | Nối rõ hơn từ bất định (uncertainty / 불확실성)/calibration sang quyết định (decision / 결정) science và rủi ro (risk / 위험) practice ở cấp repository |
| Vật lý, hóa học, sinh học | `physics/`, `chemistry/`, `biology/` | **Mạnh**; mỗi lĩnh vực (domain / 도메인) có README và coverage kiểm tra (audit / 감사) | Chỉ mở rộng khi có phụ thuộc (dependency / 의존성) cụ thể từ EE, health, AI hoặc materials |
| Khoa học máy tính (computer science / 컴퓨터 과학) foundations | `computer_science/` | **Mạnh**; có basic, advanced và connections | Cần một tuyến (route / 경로) đọc xuyên tầng, không thêm không gian tên (namespace / 네임스페이스) mới |
| Backend, frontend, bản địa (native / 네이티브) | `10_backend/`, `10_frontend/`, `11_native/` | **Mạnh**; nhánh học khung phần mềm (framework track / 프레임워크 트랙) đứng trên hệ thống (system / 시스템)/nền tảng (platform / 플랫폼) foundations | Tiếp tục dùng owner-map để tránh lặp HTTP, auth, thời gian chạy (runtime / 런타임), hiệu năng (performance / 성능) ở nhiều nhánh học (track / 트랙) |
| Linux, nền tảng (platform / 플랫폼), cloud, SRE | `linux/`, `devops_platform_engineering/` | **Mạnh**; đã có thời gian chạy (runtime / 런타임), delivery, containers, Kubernetes, GitOps, khả năng quan sát (observability / 관측 가능성), bảo mật (security / 보안), sự cố (incident / 인시던트)/DR | Bổ sung lab/trường hợp (case / 사례) khi có dạng thất bại (failure mode / 실패 모드) thực tế; không mở thêm danh mục (catalog / 카탈로그) sản phẩm |
| cơ sở dữ liệu (database / 데이터베이스), SQL, dữ liệu (data / 데이터) | `computer_science/05_data_databases/`, `sql/`, `data_engineering/` | **Mạnh** về mô hình tư duy (mental model / 사고 모델) và môi trường vận hành (production / 운영 환경) boundaries | Làm một học tập (learning / 학습) tuyến (route / 경로) chung cho truy vấn (query / 쿼리) → giao dịch (transaction / 트랜잭션) → chuỗi xử lý (pipeline / 파이프라인) → analytical serving |
| AI/ML/LLM | `computer_science/02_artificial_intelligence/` + `mathematics/` | **Mạnh**; có mathematical foundations, ML, neural nets, LLM, RAG, agents, an toàn (safety / 안전) và MLOps | Tập trung evaluation, dữ liệu (data / 데이터)/experiment provenance và môi trường vận hành (production / 운영 환경) trường hợp (case / 사례) studies |
| Economics, econometrics, investing | `economics/`, `investing/` | **Mạnh**; ranh giới (boundary / 경계) lý thuyết (theory / 이론)/ứng dụng (application / 애플리케이션) đã được ghi rõ | Giữ point-in-time/bằng chứng (evidence / 증거) discipline; tránh thêm macro lý thuyết (theory / 이론) trùng lặp |
| Psychology, sociology, philosophy | `psychology/`, `sociology/`, `philosophy/` | **Mạnh**; có bằng chứng (evidence / 증거) ranh giới (boundary / 경계) và connections | Nối hành vi (behavior / 동작) → institutions → quyết định (decision / 결정)/rủi ro (risk / 위험), không biến historical theories thành scientific consensus |
| lịch sử (history / 이력), geography, Korean culture/law/nghiệp vụ (business / 비즈니스) | các lĩnh vực (domain / 도메인) `korean_*`, `world_*` | **Rộng** và đã có nhiều tuyến (route / 경로) chuẩn gốc (canonical / 정본) | Ưu tiên practical tuyến (route / 경로) và nguồn (source / 소스) refresh cho nội dung pháp lý/thời sự |
| Research, dự án (project / 프로젝트), học tập (learning / 학습) hạ tầng (infrastructure / 인프라) | `research_methods/`, `pmp/`, `learning-library/`, `planner/` | **Đủ nền tảng** | Dùng kiểm tra (audit / 감사)/kiểm tra hợp lệ (validation / 검증) để quản lý corpus, không tiếp tục sinh tệp (file / 파일) rời rạc |

### Gaps cấu trúc được auditor ghi nhận

`automation/repo_audit.py` không phát hiện lỗi danh mục (catalog / 카탈로그) hoặc link ở mức lỗi (error / 오류), nhưng còn các cảnh báo siêu dữ liệu (metadata / 메타데이터) cần xử lý dần:

- `physics/`, `10_backend/`, `11_native/`, `linux/`, `korean_history/`, `korea_business_economy_knowledge_library/`, `korea_law_civic_life/`, `world_geography/`, `정보처리기사/`, `sql/` và `korean_culture/kiip/` chưa có `COVERAGE_AUDIT.md` ngay tại gốc (root / 루트) chuẩn gốc (canonical / 정본) đường dẫn (path / 경로) (một số có audit ở thư mục con hoặc dùng entrypoint khác).
- `11_native/`, `정보처리기사/` và `sql/` dùng điểm vào (entrypoint / 진입점) hợp lệ nhưng không có gốc (root / 루트) `README.md`; đây là khác biệt cấu trúc, không phải kết luận rằng nội dung bị thiếu.
- Các warning `link.missing` còn lại nằm trong generated thư viện (library / 라이브러리)/raw capture cũ, chủ yếu là đường dẫn mã (code / 코드)/provenance tương đối; không phát sinh từ ba tệp (file / 파일) cập nhật ở đợt này.

Đây là backlog **P0 siêu dữ liệu (metadata / 메타데이터)**, nhưng chỉ nên tạo kiểm tra (audit / 감사)/README khi có đơn vị sở hữu (owner / 오너) và nội dung thực tế; không tạo tệp (file / 파일) rỗng để làm mất cảnh báo.

## Cross-domain spine được chốt

Các tuyến (route / 경로) dưới đây là trục ưu tiên của kiến thức (knowledge / 지식) đồ thị (graph / 그래프). Mũi tên biểu thị phụ thuộc (dependency / 의존성) hoặc ứng dụng (application / 애플리케이션) transfer, không có nghĩa mọi topic phải học tuần tự tuyệt đối.

```text
Mathematics: probability/statistics/calibration
    → Research Methods: question/design/measurement/evidence
    → Econometrics: identification/estimation/uncertainty
    → AI/ML evaluation và Investment risk/decision

Computer Architecture
    → Operating Systems + Linux
    → Networks / protocols
    → Backend request, data, persistence
    → Distributed Systems / System Design
    → Cloud, Platform, SRE, incident recovery

Database internals
    → SQL semantics
    → Backend transactions and concurrency
    → Data Engineering pipelines / warehouse / serving
    → Analytics, ML data and investment evidence

Logic + Epistemology + Philosophy of Science
    → Research design and causal boundaries
    → Statistical calibration / model evaluation
    → AI safety, governance and responsible decisions

Psychology + Sociology
    → Behavioral Economics
    → Decision Science / communication / institutions
    → Portfolio behavior, organizations and practical life choices
```

## Đối chiếu trực tiếp với 12 khuyến nghị trong cuộc rà soát (review / 검토)

| Khuyến nghị | đơn vị sở hữu (owner / 오너)/bằng chứng (evidence / 증거) hiện có | Quyết định cập nhật |
|---|---|---|
| CS foundations sâu hơn | `computer_science/01`–`09`, `basic/`, các `advanced/` | Không tạo lĩnh vực (domain / 도메인) mới. Duy trì phụ thuộc (dependency / 의존성) map và thêm trường hợp (case / 사례) khi một bất biến (invariant / 불변식) chưa có practice. |
| Software kiến trúc (architecture / 아키텍처) & hệ thống (system / 시스템) thiết kế (design / 설계) | `computer_science/06`, `08`; `10_backend/backend_core`; DevOps | Đã đủ đơn vị sở hữu (owner / 오너) phân tán. Ưu tiên một tuyến (route / 경로)/trường hợp (case / 사례) tích hợp yêu cầu (request / 요청) → trạng thái (state / 상태) → thất bại (failure / 실패) → khôi phục (recovery / 복구). |
| Linux + hạ tầng (infrastructure / 인프라) + Cloud/DevOps | `linux/`, `devops_platform_engineering/` | Đã là nhánh học (track / 트랙) chuẩn gốc (canonical / 정본). Mở rộng theo sự cố (incident / 인시던트)/sức chứa (capacity / 용량)/DR, không theo tên sản phẩm. |
| bảo mật (security / 보안) kỹ thuật (engineering / 엔지니어링) | CS bảo mật (security / 보안)/độ tin cậy (reliability / 신뢰성), Linux hardening, backend định danh (identity / 식별자), DevOps bảo mật (security / 보안) | Coverage nền tảng đã có. Gap chính là threat-model → điều khiển (control / 제어) → bằng chứng (evidence / 증거) trong các trường hợp (case / 사례) liên lĩnh vực (domain / 도메인). |
| cơ sở dữ liệu (database / 데이터베이스) kỹ thuật (engineering / 엔지니어링) | CS databases, `sql/`, backend persistence, kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) | Không lập `database/` thứ tư. Tạo tuyến (route / 경로) liên kết truy vấn (query / 쿼리) planner/giao dịch (transaction / 트랜잭션)/MVCC/WAL/replication với chuỗi xử lý (pipeline / 파이프라인)/serving. |
| AI/ML foundations | `computer_science/02_artificial_intelligence/`, Mathematics, kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) | Đã rộng. Ưu tiên evaluation, provenance, an toàn (safety / 안전) và môi trường vận hành (production / 운영 환경) ranh giới (boundary / 경계) trước khi thêm khung phần mềm (framework / 프레임워크). |
| kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) | `data_engineering/` | Coverage chuẩn gốc (canonical / 정본) đã có. Giữ dữ liệu (data / 데이터) chất lượng (quality / 품질), backfill, lineage, chi phí (cost / 비용) và khôi phục (recovery / 복구) làm bất biến (invariant / 불변식). |
| Economics → Finance → Investment | `economics/`, `investing/`, Korea nghiệp vụ (business / 비즈니스)/economy | ranh giới (boundary / 경계) đã đúng. Tiếp tục point-in-time research và rủi ro (risk / 위험)/portfolio ứng dụng (application / 애플리케이션); không duplicate lý thuyết (theory / 이론). |
| Statistics / xác suất (probability / 확률) / quyết định (decision / 결정) Science | Mathematics 06, Economics 05, Research Methods, Psychology quyết định (decision / 결정) | xác suất (probability / 확률)/statistics đã đủ nền; **quyết định (decision / 결정) Science chưa có đơn vị sở hữu (owner / 오너)/tuyến (route / 경로) cấp repository rõ**. Đây là gap P1 cần nối bằng liên kết (connection / 연결) chapter/trường hợp (case / 사례), không phải một math textbook mới. |
| Psychology ngoài Jung | Psychology 00–06, 90 connections; Sociology; Biology | Coverage đã vượt yêu cầu rà soát (review / 검토). Giữ Jung/Freud/Adler ở historical ranh giới (boundary / 경계); nối cognitive/xã hội (social / 사회적)/financial quyết định (decision / 결정) khi có use trường hợp (case / 사례). |
| Philosophy + lô-gic (logic / 논리) + Epistemology | Philosophy 00–07, 90 connections; Research Methods | Đã có đơn vị sở hữu (owner / 오너) mạnh. Dùng để kiểm tra claim/bằng chứng (evidence / 증거)/mô hình (model / 모델)/ethics thay vì mở thêm nhánh trùng. |
| Practical life kiến thức (knowledge / 지식) | Korea law/civic, investing, Korea nghiệp vụ (business / 비즈니스), Psychology applied, PMP | Nền đã có nhưng chưa có tuyến (route / 경로) tích hợp. Gap P2: personal finance–healthcare literacy–communication/career, có nguồn (source / 소스) chính sách (policy / 정책) và ngày kiểm tra rõ. |

## Gaps được ưu tiên

### P0 — Quản lý coverage trước khi viết thêm

- Dùng tệp (file / 파일) này cùng `CATALOG.md` làm rà soát (review / 검토) gate cho mọi lĩnh vực (domain / 도메인) mới.
- Mỗi lĩnh vực (domain / 도메인) chuẩn gốc (canonical / 정본) phải có: README/điểm vào (entrypoint / 진입점), trục học (learning spine / 학습 축), prerequisites, đơn vị sở hữu (owner / 오너) ranh giới (boundary / 경계), advanced/deep-dive tuyến (route / 경로), trường hợp (case / 사례) hoặc lab phù hợp và coverage kiểm tra (audit / 감사).
- Khi một khái niệm xuất hiện ở nhiều lĩnh vực (domain / 도메인), README phải chỉ rõ **đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자)** và link sang đơn vị sở hữu (owner / 오너) đó; không bản sao (copy / 복사) nguyên chapter.
- Sau thay đổi lớn, rebuild danh mục (catalog / 카탈로그)/thư viện (library / 라이브러리) nếu script của lĩnh vực (domain / 도메인) yêu cầu và chạy link/format kiểm tra (audit / 감사) trong phạm vi thay đổi.

### P1 — liên kết (connection / 연결) tầng (layer / 계층) có giá trị liên lĩnh vực (domain / 도메인) cao

1. Viết tuyến (route / 경로) **xác suất (probability / 확률)/Statistics → Calibration → quyết định (decision / 결정)/rủi ro (risk / 위험)** trong liên kết (connection / 연결) tầng (layer / 계층), trỏ tới Mathematics, Research Methods, Econometrics, AI evaluation và Investing.
2. Viết trường hợp (case / 사례) **yêu cầu (request / 요청) → lưu trữ (storage / 저장소) → hàng đợi (queue / 큐) → thất bại (failure / 실패) → khôi phục (recovery / 복구)** trỏ tới Khoa học máy tính (computer science / 컴퓨터 과학), Backend, Linux, cơ sở dữ liệu (database / 데이터베이스), kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링), DevOps và SRE.
3. Viết tuyến (route / 경로) **Threat mô hình (model / 모델) → định danh (identity / 식별자)/authorization → secret/dữ liệu (data / 데이터) ranh giới (boundary / 경계) → telemetry/bằng chứng (evidence / 증거)** nối bảo mật (security / 보안), Backend, Linux, DevOps và AI an toàn (safety / 안전).
4. Viết tuyến (route / 경로) **Macro/hành vi (behavior / 동작)/bằng chứng (evidence / 증거) → portfolio quyết định (decision / 결정)** nối Economics, Psychology, Research Methods, Mathematics và Investing.

### P2 — Thực hành và practical life

- Personal finance: ngân sách, nợ, bảo hiểm, thuế và rủi ro; cross-link Investing và Korea Law, không biến thành tư vấn cá nhân.
- Healthcare literacy: đọc nguồn y tế, rủi ro (risk / 위험)/benefit, screening, consent và khi nào cần chuyên gia; giữ ranh giới (boundary / 경계) với chẩn đoán/điều trị.
- Communication/negotiation/career: dùng Psychology, Sociology, PMP và Korea civic/workplace làm đơn vị sở hữu (owner / 오너); thêm trường hợp (case / 사례) có bằng chứng (evidence / 증거) thay vì danh sách mẹo.

### P3 — Chỉ mở rộng khi có phụ thuộc (dependency / 의존성) thực

Measure lý thuyết (theory / 이론), advanced stochastic calculus, advanced trình biên dịch (compiler / 컴파일러) hiện thực (implementation / 구현), vendor-specific cloud catalogs, frontier ML papers hoặc nhánh lịch sử/philosophy mới chỉ nên mở khi một tuyến (route / 경로) hiện tại bị chặn bởi phụ thuộc (dependency / 의존성) cụ thể. Độ dài corpus tự nó không phải completion criterion.

## Quy tắc tránh mở rộng sai hướng

- Không tạo `statistics/`, `system_design/`, `security/`, `database/` hoặc `decision_science/` mới nếu nội dung chỉ lặp lại đơn vị sở hữu (owner / 오너) hiện có.
- Không biến khung phần mềm (framework / 프레임워크)/công cụ (tool / 도구) danh mục (catalog / 카탈로그) thành nền tảng học tập; mô hình tư duy (mental model / 사고 모델) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) thuộc chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인).
- Không xem README có nhiều link là coverage sâu; cần kiểm tra cơ chế (mechanism / 메커니즘), bất biến (invariant / 불변식), ranh giới (boundary / 경계), bằng chứng (evidence / 증거) và practice.
- Không dùng nguồn exam/PDF/trường hợp (case / 사례) như prose chuẩn gốc (canonical / 정본) nếu chưa chuyển thành explanation có provenance.
- Với law, thị trường (market / 시장), cloud sản phẩm (product / 제품) và kỹ thuật thay đổi nhanh, ghi ngày kiểm tra và nguồn chính thức.

## Definition of done cho master kiểm tra (audit / 감사)

Một vòng rà soát (review / 검토) cấp repository chỉ được coi là hoàn tất khi:

1. `CATALOG.md` liệt kê đúng chuẩn gốc (canonical / 정본)/hỗ trợ (support / 지원) đơn vị sở hữu (owner / 오너) và điểm vào (entrypoint / 진입점) tồn tại.
2. Mỗi chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인) có README và ranh giới (boundary / 경계); coverage kiểm tra (audit / 감사) không mâu thuẫn với README.
3. Các tuyến (route / 경로) P1 có link hai chiều hoặc được ghi rõ đơn vị sở hữu (owner / 오너) một chiều để tránh duplicate.
4. Không có lĩnh vực (domain / 도메인) mới được thêm chỉ vì một khuyến nghị đã được coverage hiện tại đáp ứng.
5. `git diff --check` sạch cho thay đổi kiểm tra (audit / 감사); các script kiểm tra (audit / 감사)/bản dựng (build / 빌드) liên quan được chạy và báo rõ giới hạn.
6. Mỗi lần rà soát (review / 검토) sau cập nhật ngày kiểm tra và chỉ thay đổi gap/priority có bằng chứng mới.

> **Bàn giao:** Sau master kiểm tra (audit / 감사), bước tiếp theo hợp lý là thực hiện từng tuyến (route / 경로) P1 như một liên kết (connection / 연결)/trường hợp (case / 사례) có đơn vị sở hữu (owner / 오너) rõ ràng. Không mở rộng đồng thời cả 12 hướng; hoàn tất một tuyến (route / 경로), kiểm tra liên kết và bằng chứng (evidence / 증거), rồi mới chuyển sang tuyến (route / 경로) kế tiếp.
