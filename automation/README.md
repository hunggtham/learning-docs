# MVP tự động tạo giáo trình 정보처리기사

Flow này dùng GitHub cho cả input và output. n8n trên home server gọi worker; worker kéo hai file Markdown hiện có, dùng OpenAI Responses API viết lại thành 5 phần giáo trình, kiểm tra chất lượng, rồi chỉ commit khi `PUSH_CHANGES=true`.

## Output

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

Tài liệu không bị ép vào format cố định. AI được quyền đổi vị trí source để dễ hiểu, nhưng phải bảo toàn mã `핵심 001...`, không tự thêm fact thiếu căn cứ và đánh dấu phần chưa chắc chắn.

## Chuẩn bị một lần

1. Chuyển repository sang **private** nếu tiếp tục lưu tài liệu có bản quyền.
2. Tạo GitHub fine-grained token chỉ cho repo này, quyền `Contents: Read and write`. Không ghi token vào GitHub hoặc workflow JSON.
3. Tạo OpenAI project riêng, hard limit $30 và API key riêng. Chỉ lưu key trong Coolify secret.

## Deploy worker trong Coolify

Tạo Application từ repository này và chọn branch `docs/정보처리기사`:

- Base directory: `/automation`
- Build pack: `Dockerfile`
- Port: `8090`
- Persistent storage: `/opt/learning-docs-worker` → `/data`

Environment variables lấy từ `.env.example`. Giá trị quan trọng:

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

Nếu container không gọi được `host.docker.internal`, dùng IP LAN/Tailscale của home server. Không public port 8090 ra Internet; chỉ cho n8n gọi qua Docker network/internal URL.

Kiểm tra:

```bash
curl http://<worker-internal-url>:8090/health
```

## Import vào n8n

1. Import `automation/n8n/정보처리기사-textbook.json`.
2. Trong service n8n, thêm environment:

```text
TEXTBOOK_WORKER_URL=http://<tên-service-worker>:8090
```

3. Redeploy n8n.
4. Trong workflow, bấm `Execute Workflow` một lần để test.
5. Khi test thành công, Activate. Schedule mặc định chạy mỗi giờ; manifest SHA-256 ngăn xử lý lại khi input không đổi.

Lần chạy thử đầu tiên đặt `TARGET_PARTS=1`, `MAX_CHUNKS_PER_PART=1`, `MAX_API_CALLS=2`, `MAX_RUN_USD=1`, `PUSH_CHANGES=false`. Sau khi duyệt output mới bỏ hai giới hạn mẫu và bật push.

## An toàn và khôi phục

- Token chỉ nằm trong secret/environment của Coolify.
- Worker reset local clone về branch GitHub trước mỗi lượt; GitHub vẫn là source of truth.
- Nếu AI lỗi, API trả HTTP 500 và không push output dở lên GitHub.
- Xem `quality-report.md` trước khi dùng tài liệu để ôn thi.
