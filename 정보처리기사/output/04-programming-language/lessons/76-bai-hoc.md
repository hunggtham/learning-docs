# 232. 배치 프로그램 (Batch Program)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế vận hành và vai trò của chương trình xử lý hàng loạt (배치 프로그램 - Batch Processing Program) trong các hệ thống doanh nghiệp, tài chính ngân hàng.
- Thuộc lòng 5 yếu tố bắt buộc phải có của một chương trình Batch theo khẩu quyết kinh điển **대자견안성** (Đại dung lượng, Tự động hóa, Kiên cố, An định, Hiệu năng).
- Thấu hiểu sâu sắc tính kiên cố (견고성 - Robustness): Khả năng cách ly dữ liệu lỗi, ghi log và tiếp tục thực thi không gián đoạn nhằm bảo toàn luồng xử lý toàn cục.

## 핵심 키워드 (Từ khóa)
- 배치 프로그램 (Batch Processing Program)
- 일괄 처리 (Batch Execution / Non-interactive)
- 무인 자동화 (Unattended Automation)
- 배치 5대 필수 요소 (대용량, 자동화, 견고성, 안정성, 성능)
- 견고성 (Robustness - 오류 발생 시에도 중단 없는 처리)
- 배치 윈도우 (Batch Window - 야간 유휴 시간대 처리)
- 암기 공식 (대자견안성)

## 선행·연결 개념 (Kiến thức liên kết)
- [75-bai-hoc.md](75-bai-hoc.md): Tổng hợp kiến trúc nền tảng phần mềm ứng dụng.
- [77-bai-hoc.md](77-bai-hoc.md): Cấu trúc dữ liệu Struct trong ngôn ngữ lập trình C.
- [52-bai-hoc.md](52-bai-hoc.md): Vòng đời trạng thái dữ liệu lỗi và các thuộc tính Batch.

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Khái niệm: Là chương trình **xử lý khối lượng dữ liệu khổng lồ theo một thứ tự định trước một cách đồng loạt mà không cần sự can thiệp của người dùng**.
  - Khẩu quyết 5 yếu tố cốt lõi:
    $$\mathbf{대 \rightarrow 자 \rightarrow 견 \rightarrow 안 \rightarrow 성}$$
    - **대**용량 데이터 (Large Data Volume): Xử lý hàng triệu bản ghi.
    - **자**동화 (Automation): Chạy ngầm định kỳ (Cron/Scheduler), không người bấm nút.
    - **견**고성 (Robustness): Có lỗi ở một dòng dữ liệu thì **ghi nhận log lại rồi chạy tiếp**, tuyệt đối không được sập chương trình.
    - **안**정성 (Stability): Đảm bảo giao dịch toàn vẹn, có thể rollback khi có sự cố hệ thống.
    - **성**능 (Performance): Xong việc đúng khung giờ quy định (Batch Window).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân tích chi tiết 5 yếu tố bắt buộc của Batch Program:**

| Yếu tố bắt buộc | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Tiêu chí thiết kế |
| :--- | :--- | :--- |
| **1. Đại dung lượng** | **대용량 데이터** (Large Volume) | Có khả năng thu thập, tính toán và lưu trữ hàng trăm nghìn đến hàng triệu bản ghi dữ liệu mà không làm tràn bộ nhớ RAM (sử dụng kỹ thuật phân trang / Chunk). |
| **2. Tự động hóa** | **자동화** (Automation) | Được lập lịch kích hoạt hoàn toàn tự động bởi các trình quản trị tiến trình (như Crontab, Quartz Scheduler) mà không cần thao tác thủ công của quản trị viên. |
| **3. Tính kiên cố** | **견고성** (Robustness) | Khi gặp dữ liệu sai định dạng (ví dụ chia cho 0, chuỗi ký tự nằm trong trường số), chương trình **không bị Crash đột ngột** mà tự động ghi nhận mã lỗi vào nhật ký (Log) và tiếp tục xử lý các bản ghi kế tiếp. |
| **4. Tính ổn định** | **안정성 / 신뢰성** (Stability) | Ngăn ngừa việc thất thoát dữ liệu bằng các điểm kiểm tra trung gian (Checkpoints) và hỗ trợ khôi phục trạng thái (Rollback/Restart) chính xác từ điểm bị gián đoạn. |
| **5. Hiệu năng cao** | **성능** (Performance) | Tối ưu hóa câu truy vấn cơ sở dữ liệu, đa luồng song song (Multi-threading) để hoàn tất khối lượng xử lý trong khoảng thời gian cửa sổ cho phép (Batch Window, thường từ 0h - 5h sáng). |

- **2. Khác biệt giữa xử lý thời gian thực (Real-time OLTP) và Xử lý hàng loạt (Batch):**
  - **OLTP (Online Transaction Processing):** Tương tác người dùng trực tiếp, từng giao dịch đơn lẻ, yêu cầu phản hồi tức thì trong mili-giây (ví dụ: quẹt thẻ mua cà phê).
  - **Batch Processing:** Chạy nền không tương tác, gom dữ liệu của toàn bộ ngày/tháng để xử lý dồn một lần (ví dụ: tính lãi suất ngân hàng cuối ngày, chốt sao kê thẻ tín dụng cuối tháng, tính lương nhân viên).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế Skip và Retry trong kiến trúc Batch hiện đại (Spring Batch):**
  - *Skip:* Khi gặp bản ghi lỗi nghiệp vụ không nghiêm trọng, cấu hình cho phép bỏ qua tối đa $N$ dòng lỗi để không làm đình trệ toàn bộ tiến trình hàng triệu bản ghi còn lại.
  - *Retry:* Khi gặp sự cố mạng tạm thời (Deadlock DB hoặc Timeout), Batch tự động thử lại $K$ lần trước khi quyết định đánh dấu thất bại.

### 복습 체크리스트
- [ ] Đọc vanh vách khẩu quyết 5 yếu tố của Batch: **대자견안성** (Đại, Tự, Kiên, An, Tính).
- [ ] Nắm vững khái niệm 견고성 (Robustness): Lỗi ở 1 bản ghi không làm sập chương trình mà tiếp tục chạy.
- [ ] Hiểu rõ thời điểm chạy của Batch: Giờ thấp điểm/ban đêm để không cạnh tranh tài nguyên với OLTP.
- [ ] Phân biệt được bản chất giữa hệ thống OLTP (tức thời) và Batch (xử lý gom theo lô).
