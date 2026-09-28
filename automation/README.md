# MVP tự động tạo giáo trình 정보처리기사

Luồng (flow / 흐름) này dùng GitHub cho cả đầu vào (input / 입력) và đầu ra (output / 출력). n8n trên home máy chủ (server / 서버) gọi worker; worker kéo hai tệp (file / 파일) Markdown hiện có, dùng OpenAI Responses API viết lại thành 5 phần giáo trình, kiểm tra chất lượng, rồi chỉ lần ghi nhận (commit / 커밋) khi `PUSH_CHANGES=true`.

## Đầu ra (output / 출력)

```text
output/정보처리기사/
├── 01_소프트웨어_설계.md
├── 02_소프트웨어_개발.md
├── 03_데이터베이스_구축.md
├── 04_프로그래밍_언어_활용.md
├── 05_정보시스템_구축관리.md
├── quality-report.md
└── manifest.json
```

Tài liệu không bị ép vào format cố định. AI được quyền đổi vị trí nguồn (source / 소스) để dễ hiểu, nhưng phải bảo toàn mã `핵심 001...`, không tự thêm fact thiếu căn cứ và đánh dấu phần chưa chắc chắn.

## Chuẩn bị một lần

1. Chuyển repository sang **private** nếu tiếp tục lưu tài liệu có bản quyền.
2. Tạo GitHub fine-grained đơn vị từ (token / 토큰) chỉ cho repo này, quyền `Contents: Read and write`. Không ghi đơn vị từ (token / 토큰) vào GitHub hoặc workflow JSON.
3. Tạo OpenAI dự án (project / 프로젝트) riêng, hard limit $30 và API key riêng. Chỉ lưu key trong Coolify secret.

## Deploy worker trong Coolify

Tạo Ứng dụng (application / 애플리케이션) từ repository này và chọn branch `docs/정보처리기사`:

- Cơ sở (base / 기반) directory: `/automation`
- Bản dựng (build / 빌드) pack: `Dockerfile`
- Cổng (port / 포트): `8090`
- Persistent lưu trữ (storage / 저장소): `/opt/learning-docs-worker` → `/data`

Môi trường (environment / 환경) variables lấy từ `.env.example`. Giá trị quan trọng:

```text
GITHUB_REPOSITORY=hunggtham/learning-docs
GITHUB_BRANCH=docs/정보처리기사
GITHUB_TOKEN=<token chỉ lưu trong Coolify>
OPENAI_API_KEY=<chỉ lưu trong Coolify>
OPENAI_DRAFT_MODEL=gpt-5.6-terra
OPENAI_QA_MODEL=gpt-5.6-sol
OPENAI_DRAFT_EFFORT=none
OPENAI_QA_EFFORT=low
MAX_RUN_USD=5
PUSH_CHANGES=false
```

Nếu bộ chứa (container / 컨테이너) không gọi được `host.docker.internal`, dùng IP LAN/Tailscale của home máy chủ (server / 서버). Không công khai (public / 공개) cổng (port / 포트) 8090 ra Internet; chỉ cho n8n gọi qua Docker mạng (network / 네트워크)/nội bộ (internal / 내부) URL.

Kiểm tra:

```bash
curl http://<worker-internal-url>:8090/health
```

## Import vào n8n

1. Import `automation/n8n/정보처리기사-textbook.json`.
2. Trong dịch vụ (service / 서비스) n8n, thêm môi trường (environment / 환경):

```text
TEXTBOOK_WORKER_URL=http://<tên-service-worker>:8090
```

3. Redeploy n8n.
4. Trong workflow, bấm `Execute Workflow` một lần để kiểm thử (test / 테스트).
5. Khi kiểm thử (test / 테스트) thành công, Activate. Schedule mặc định chạy mỗi giờ; manifest SHA-256 ngăn xử lý lại khi đầu vào (input / 입력) không đổi.

Lần chạy thử đầu tiên đặt `TARGET_PARTS=1`, `MAX_CHUNKS_PER_PART=1`, `MAX_API_CALLS=2`, `MAX_RUN_USD=1`, `PUSH_CHANGES=false`. Sau khi duyệt đầu ra (output / 출력) mới bỏ hai giới hạn mẫu và bật push.

## An toàn và khôi phục

- Đơn vị từ (token / 토큰) chỉ nằm trong secret/môi trường (environment / 환경) của Coolify.
- Worker reset cục bộ (local / 로컬) clone về branch GitHub trước mỗi lượt; GitHub vẫn là nguồn chuẩn (source of truth / 정본).
- Nếu AI lỗi, API trả HTTP 500 và không push đầu ra (output / 출력) dở lên GitHub.
- Xem `quality-report.md` trước khi dùng tài liệu để ôn thi.

---

## Repository QA — danh mục (catalog / 카탈로그) và Markdown links

Repo QA là luồng (flow / 흐름) độc lập với worker tạo giáo trình ở trên. Nó không gọi OpenAI, không gọi GitHub API và không cần secret; mục tiêu là phát hiện structural drift ngay trong working cây (tree / 트리) trước khi tài liệu được merge.

Các tệp (file / 파일) liên quan:

```text
automation/repo_audit.py
automation/test_repo_audit.py
.github/workflows/repo-audit.yml
```

### Auditor kiểm tra gì?

`repo_audit.py` dùng Python thư viện chuẩn (standard library / 표준 라이브러리) và kiểm tra hai lớp chính.

**Danh mục (catalog / 카탈로그) đặc tả hợp đồng (contract / 계약)** kiểm tra:

```text
CATALOG.md tồn tại
→ canonical domains parse được
→ domain id không trùng
→ domain path tồn tại
→ entrypoint tồn tại
→ last_reviewed có date hợp lệ
→ scope không bị bỏ trống
```

Auditor cũng report lĩnh vực (domain / 도메인) chưa có gốc (root / 루트) `README.md` hoặc `COVERAGE_AUDIT.md`, nhưng hai trường hợp này chỉ là thông tin vì một số lĩnh vực (domain / 도메인) có thể cố ý dùng điểm vào (entrypoint / 진입점) khác.

**Markdown cục bộ (local / 로컬) links** kiểm tra link nội bộ trỏ tới tệp (file / 파일)/đường dẫn (path / 경로) trong repository. Fragment như `#section` không cần tệp (file / 파일) lookup riêng; bên ngoài (external / 외부) URL không được gọi qua mạng (network / 네트워크).

Không kiểm tra live availability của website ngoài repository vì mạng (network / 네트워크) check dễ flaky, chậm và không phù hợp với nhiệm vụ chính là bảo toàn cấu trúc chuẩn gốc (canonical / 정본) nội bộ.

### Chuẩn gốc (canonical / 정본) docs và raw provenance

CI link gate chỉ áp dụng cho Markdown thuộc học tập (learning / 학습)/đầu ra (output / 출력)/điều hướng (navigation / 내비게이션) tầng (layer / 계층). Các đường dẫn (path / 경로) có segment sau được loại khỏi chuẩn gốc (canonical / 정본) link gate:

```text
raw/
raw_md/
workflow-output/
```

Đây là provenance/import/intermediate material có thể giữ nguyên cú pháp (syntax / 문법) hoặc link encoding từ nguồn bên ngoài. Không nên sửa nguồn thô chỉ để làm đẹp repository QA. Khi nội dung được chuyển thành chuẩn gốc (canonical / 정본) học tập (learning / 학습) document, link của bản chuẩn gốc (canonical / 정본) phải pass strict kiểm tra (audit / 감사).

`repo_audit.py` vẫn có thể được chạy trực tiếp trên toàn working cây (tree / 트리) khi cần forensic kiểm tra (audit / 감사); exclusion ở trên là chính sách (policy / 정책) của GitHub Actions chuẩn gốc (canonical / 정본) gate.

### Chạy cục bộ (local / 로컬)

Chạy đơn vị (unit / 단위) tests:

```bash
python -m unittest automation/test_repo_audit.py
```

Quét toàn bộ repository:

```bash
python automation/repo_audit.py --root .
```

Muốn broken cục bộ (local / 로컬) link trở thành lỗi blocking:

```bash
python automation/repo_audit.py --root . --strict-links
```

Có thể kiểm tra (audit / 감사) chỉ một tập tệp (file / 파일) Markdown bằng danh sách newline-separated:

```bash
python automation/repo_audit.py \
  --root . \
  --files-from /tmp/changed-markdown.txt \
  --strict-links
```

### GitHub Actions chính sách (policy / 정책)

Workflow `Repository audit` chạy đơn vị (unit / 단위) tests trước.

Trên **pull yêu cầu (request / 요청)**, workflow lấy các chuẩn gốc (canonical / 정본) Markdown tệp (file / 파일) thay đổi trong diff và kiểm tra cục bộ (local / 로컬) links ở `strict` chế độ (mode / 모드). Điều này ngăn một PR mới đưa broken nội bộ (internal / 내부) link vào repository mà không bắt toàn bộ legacy/provenance debt phải được sửa trong cùng PR.

Trên **push vào `main`** hoặc chạy thủ công, auditor quét toàn bộ chuẩn gốc (canonical / 정본) Markdown repository ở report chế độ (mode / 모드). Broken cục bộ (local / 로컬) links cũ được hiển thị như warning để tạo backlog; danh mục (catalog / 카탈로그) structural errors vẫn là lỗi vì chúng làm source-of-truth siêu dữ liệu (metadata / 메타데이터) không còn đáng tin.

Mô hình tư duy (mental model / 사고 모델) của chính sách (policy / 정책):

```text
New canonical change
→ must not introduce new broken structure

Existing canonical repository
→ continuously expose legacy debt
→ fix incrementally
→ tighten policy only after baseline is clean

Raw provenance
→ preserve source fidelity
→ do not block canonical CI on imported link syntax
```

Workflow chỉ có quyền `contents: read` và không thay đổi tệp (file / 파일) tự động. Fix vẫn phải đi qua branch/PR bình thường để diff có thể rà soát (review / 검토).
