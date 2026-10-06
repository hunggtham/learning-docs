# Quy ước ngôn ngữ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Quy ước ngôn ngữ**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. Bắt đầu ở **Quy ước ngôn ngữ** để mở đối tượng chính của file và câu hỏi cần theo dõi, rồi dùng kết luận đó khi quay về lộ trình rộng hơn.

Thư viện DevOps / kỹ thuật nền tảng (platform engineering / 플랫폼 엔지니어링) giải thích chủ yếu bằng tiếng Việt tự nhiên. Mỗi lần thuật ngữ quan trọng xuất hiện trong phần giải thích, dùng dạng `tiếng Việt (English term / 한국어 용어)`. Không dùng tiếng Anh thay cho phần giải thích tiếng Việt chỉ vì tài liệu kỹ thuật thường viết như vậy.

Tên sản phẩm, API, tài nguyên (resource / 자원) kind, command, identifier, giao thức và mã (code / 코드) giữ nguyên bản gốc. `Kubernetes`, `Pod`, `Deployment`, `Service`, `StatefulSet`, `Terraform`, `Dockerfile`, `systemd`, `HTTP`, `TLS`, `DNS`, `kubectl` và `git` không bị dịch thành tên tự chế.

Khi một câu có quá nhiều từ tiếng Anh, phải viết lại mô hình tư duy (mental model / 사고 모델) bằng tiếng Việt rồi chỉ giữ các từ khóa (keyword / 키워드) cần tra cứu trong ngoặc. Ví dụ, thay vì viết “chuỗi xử lý (pipeline / 파이프라인) trigger bản dựng (build / 빌드) rồi push sản phẩm tạo ra (artifact / 산출물) và deploy tải công việc (workload / 워크로드)”, ưu tiên “chuỗi xử lý (pipeline / 파이프라인) được kích hoạt để dựng bản bản dựng (build / 빌드), xuất bản hiện vật (artifact) bất biến rồi chuyển chính hiện vật đó qua các môi trường”.

Các từ như `desired state`, `actual state`, `reconciliation`, `drift`, `blast radius`, `golden path`, `guardrail`, `toil`, `runbook` thường không có một bản dịch duy nhất hoàn hảo. Mỗi lần xuất hiện đều cần giải thích bằng tiếng Việt rồi giữ English/한국어 ngay cạnh để đối chiếu tài liệu công việc.

Mục tiêu là người đọc có thể đọc liền mạch bằng tiếng Việt nhưng vẫn nhận ra thuật ngữ chuẩn khi đọc log, dashboard, RFC, tài liệu cloud provider hoặc trao đổi với nhóm (team / 팀) Hàn/Anh.

> **Bàn giao:** Sau **Quy ước ngôn ngữ**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
