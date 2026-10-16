# Quy trình Làm việc Hàng ngày của Kỹ sư Phát triển (Daily Developer Routine & Workbench)

Tài liệu này định hình các thói quen kỹ thuật thực chiến, quy trình điều phối tiến trình phát triển và tiêu chuẩn quản lý mã nguồn hàng ngày, giúp duy trì năng suất cao, giảm thiểu phân tâm và bảo đảm chất lượng code bền vững.

---

## 1. Khởi động Ngày Làm việc (Morning Startup Protocol)

Một ngày làm việc hiệu quả bắt đầu bằng việc thiết lập môi trường sạch và đồng bộ trạng thái mới nhất từ các kho mã nguồn:

```text
1. Đồng bộ Trạng thái Repository
   ├── git fetch origin
   ├── git status (kiểm tra thay đổi tồn đọng hoặc nhánh chưa hợp nhất)
   └── git pull --rebase (cập nhật nhánh chính)

2. Khởi tạo Môi trường Điều phối Tiến trình (mprocs / tmux)
   ├── Khởi chạy máy chủ phát triển cục bộ (Frontend / Backend)
   ├── Kiểm tra các dịch vụ hỗ trợ (Database, Redis, Worker)
   └── Khởi động môi trường ghi chú tri thức (Obsidian Vault)

3. Xác định Mục tiêu Trọng tâm (Top 3 Daily Deliverables)
   ├── Xác định 1 tính năng hoặc bài học kiến trúc quan trọng nhất
   ├── Xác định 1 bài toán kỹ thuật hoặc bug cần phân tích căn nguyên (RCA)
   └── Xác định 1 nhiệm vụ rà soát hoặc cải tiến tài liệu học tập
```

---

## 2. Quản lý Đa tiến trình với `mprocs`

Tệp cấu hình [`mprocs.yaml`](mprocs.yaml) tại thư mục này cho phép gom toàn bộ các tiến trình phát triển, build và dịch vụ nền vào một giao diện dòng lệnh tập trung duy nhất:

| Tiến trình (Process) | Lệnh thực thi | Mục đích sử dụng | Tự động chạy (Autostart) |
| :--- | :--- | :--- | :--- |
| `study-dev` | `npm run dev` | Khởi chạy máy chủ giao diện học tập React | `true` |
| `marker-app` | `python marker_app.py` | Ứng dụng trích xuất văn bản và tài liệu tự động | `false` |
| `marker-server` | `python marker_server.py` | Dịch vụ máy chủ API trích xuất tài liệu | `false` |
| `clone-drive` | `python drive_copy.py` | Tự động đồng bộ và sao lưu dữ liệu đám mây | `false` |

> [!TIP] Điều khiển mprocs tiện lợi:
> - Sử dụng phím tắt `q` để đóng mprocs sạch sẽ (gửi tín hiệu `SIGTERM` đến toàn bộ các tiến trình con).
> - Sử dụng phím `r` để khởi động lại nhanh một tiến trình đang chạy mà không cần mở tab terminal mới.

---

## 3. Quy trình Ghi chép Tri thức & Liên kết Tư duy (Obsidian Integration)

Thư mục này được tích hợp trực tiếp với **Obsidian Vault** (`.obsidian/`), đóng vai trò như một bộ não số thứ hai (Second Brain):

1. **Ghi chép tức thời (Fleeting Notes):**
   - Khi phát hiện một lỗi cú pháp, bẫy compiler hoặc kỹ thuật tối ưu mới trong ngày, ghi lại ngay dạng ghi chú thô kèm ví dụ thực tế.
2. **Chuẩn hóa & Tinh chế (Literature to Permanent Notes):**
   - Định kỳ cuối tuần, chuyển hóa các ghi chép thô thành bài giảng chuẩn mực, đưa về các thư mục lĩnh vực tương ứng (`10_backend/`, `10_frontend/`, `sql/`, `cert/`).
3. **Tuân thủ Tiêu chuẩn AGENTS.md:**
   - Không bịa đặt số liệu hay ví dụ; ghi chú phải luôn có dẫn chứng thực tế từ mã nguồn chạy được hoặc tài liệu chính thức.

---

## 4. Tổng kết & Bàn giao Cuối ngày (End-of-Day Handoff)

Trước khi kết thúc ngày làm việc, thực hiện 4 bước nghiệm thu bắt buộc:

1. **Rà soát Mã nguồn & Kiểm tra Chất lượng:**
   - Chạy `git diff --check` để bảo đảm không để lại khoảng trắng thừa (trailing whitespace) hay ký tự lạ.
   - Chạy test suite hoặc linting tương ứng (`npm run test` hoặc `python3 scripts/run_quality_audit.py`).
2. **Commit Rõ ràng & Có Ý nghĩa (Conventional Commits):**
   - Sử dụng tiền tố chuẩn: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`.
   - Tránh các commit chung chung như "update" hay "fix bug".
3. **Đẩy Mã nguồn Lên Remote:**
   - Đẩy nhánh làm việc lên remote an toàn (`git push origin <branch>`).
4. **Ghi chú Điểm tiếp nối Ngày hôm sau:**
   - Viết ngắn 2 dòng về điểm bắt đầu cho phiên làm việc tiếp theo để không mất thời gian tái nhập mạch tư duy (context switching).
