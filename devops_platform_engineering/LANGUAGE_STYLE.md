# Quy ước ngôn ngữ

Thư viện DevOps / Platform Engineering giải thích chủ yếu bằng tiếng Việt tự nhiên. Thuật ngữ quan trọng được giới thiệu theo dạng `tiếng Việt (English term / 한국어 용어)` khi tiếng Hàn có giá trị nhận diện thực tế. Không dùng tiếng Anh thay cho phần giải thích tiếng Việt chỉ vì tài liệu kỹ thuật thường viết như vậy.

Tên sản phẩm, API, resource kind, command, identifier, giao thức và code giữ nguyên bản gốc. `Kubernetes`, `Pod`, `Deployment`, `Service`, `StatefulSet`, `Terraform`, `Dockerfile`, `systemd`, `HTTP`, `TLS`, `DNS`, `kubectl` và `git` không bị dịch thành tên tự chế.

Khi một câu có quá nhiều từ tiếng Anh, phải viết lại mental model bằng tiếng Việt rồi chỉ giữ các keyword cần tra cứu trong ngoặc. Ví dụ, thay vì viết “pipeline trigger build rồi push artifact và deploy workload”, ưu tiên “pipeline được kích hoạt để dựng bản build, xuất bản hiện vật (artifact) bất biến rồi chuyển chính hiện vật đó qua các môi trường”.

Các từ như `desired state`, `actual state`, `reconciliation`, `drift`, `blast radius`, `golden path`, `guardrail`, `toil`, `runbook` thường không có một bản dịch duy nhất hoàn hảo. Lần đầu xuất hiện cần giải thích bằng tiếng Việt; sau đó có thể giữ keyword gốc nếu nó giúp đối chiếu tài liệu công việc.

Mục tiêu là người đọc có thể đọc liền mạch bằng tiếng Việt nhưng vẫn nhận ra thuật ngữ chuẩn khi đọc log, dashboard, RFC, tài liệu cloud provider hoặc trao đổi với team Hàn/Anh.