# 4. 병행 제어 (Concurrency Control)

## 4. 병행 제어 (Concurrency Control)
Phần “4. 병행 제어 (Concurrency Control)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Concept)**: Điều khiển sự tương tác giữa các giao dịch chạy đồng thời để bảo vệ tính 일관성 (nhất quán).
- **문제점 (Problems)**:
  - **갱신 분실 (Lost Update)**: Mất bản cập nhật.
  - **비완료 의존성 (Uncommitted Dependency)**: Phụ thuộc vào giao dịch chưa commit (Dirty Read).
  - **모순성 (Inconsistency)**: Mâu thuẫn dữ liệu.
  - **연쇄 복귀 (Cascading Rollback)**: Phải rollback dây chuyền.
- **로킹 (Locking)**: Khóa dữ liệu để sử dụng 상호 배타적 (độc quyền - Mutual Exclusion).
  - **로킹 단위 (Locking Granularity)**: Đơn vị khóa.
    - Đơn vị 크면 (lớn) -> ít khóa, dễ quản lý, nhưng mức đồng thời thấp (낮은 병행성).
    - Đơn vị 작으면 (nhỏ) -> ngược lại.
- **Ví dụ**: Hai người cùng rút tiền từ một tài khoản, Locking giúp chỉ 1 người được rút tại 1 thời điểm.
- 💡 **Mẹo ghi nhớ**: Vấn đề đồng thời: L/U/I/C (Lost, Uncommitted, Inconsistency, Cascading) -> **Làm Út In Cười**
