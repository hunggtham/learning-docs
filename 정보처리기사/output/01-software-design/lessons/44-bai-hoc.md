# 1. 회복 (Recovery)

## 1. 회복 (Recovery)
Phần “1. 회복 (Recovery)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Concept)**: 트랜잭션 도중 장애 발생 시 정상 상태로 복구 (Phục hồi về trạng thái bình thường khi có lỗi).
- **장애의 유형 (Types of Failures)**:
  - **트랜잭션 장애 (Transaction Failure)**: Lỗi nội bộ của giao dịch (ví dụ: dữ liệu sai).
  - **시스템 장애 (System Failure)**: Lỗi phần cứng/phần mềm ảnh hưởng đến tất cả giao dịch.
  - **미디어 장애 (Media Failure)**: Lỗi vật lý của thiết bị lưu trữ (ví dụ: hỏng đĩa).
- **회복 기법 (Recovery Techniques)**: 연기 갱신 (Deferred Update), 즉각 갱신 (Immediate Update), 그림자 페이지 (Shadow Paging), 검사점 (Check Point).
- **Ví dụ**: Hệ thống ngân hàng bị sập khi đang chuyển tiền (hệ thống lỗi), cần hoàn tác (Undo) hoặc chạy lại để khôi phục.
- 💡 **Mẹo ghi nhớ**: 장애 유형: T/S/M (Transaction, System, Media) -> **Tưởng Sợ Ma**
