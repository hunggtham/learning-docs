# 187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)

## 187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)
Phần “187-189. 트랜잭션의 상태와 특성 (Transaction State & ACID)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **상태 (188):** 활동(Active) -> [부분 완료(Partially Committed) -> 완료(Committed)] 또는 [실패(Failed) -> 철회(Aborted/Rollback)].
- **특성 (189):** 원자성(Atomicity - 전부 또는 전무), 일관성(Consistency), 독립성(Isolation - 병행 중 간섭 불가), 영속성(Durability).
- **VI (Vietnamese) (Tiếng Việt):** Trạng thái và tính chất giao dịch.
  - Trạng thái: Đang chạy -> Hoàn thành một phần -> Commit HOẶC Lỗi -> Rollback.
