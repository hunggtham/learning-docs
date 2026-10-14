# 130-132. 트랜잭션 (Transaction)

## 130-132. 트랜잭션 (Transaction)
Phần “130-132. 트랜잭션 (Transaction)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 데이터베이스 상태를 변환시키는 논리적 작업의 단위.
- **ACID 특성:**
  - **Atomicity (원자성):** 모두 반영되거나(Commit) 전혀 반영되지 않아야 함(Rollback).
  - **Consistency (일관성):** 성공 시 일관성 있는 상태 유지.
  - **Isolation (독립성/격리성):** 다른 트랜잭션의 연산이 끼어들 수 없음.
  - **Durability (영속성):** 성공한 결과는 시스템 고장에도 영구 반영.
- **VI (Vietnamese) (Tiếng Việt):** Giao dịch (Transaction) & Tính chất ACID.
  - Atomicity (Tính nguyên tử): Tất cả hoặc không có gì.
  - Consistency (Tính nhất quán): Giữ trạng thái nhất quán.
  - Isolation (Tính độc lập): Không bị can thiệp bởi giao dịch khác.
  - Durability (Tính bền vững): Lưu trữ vĩnh viễn dù có lỗi hệ thống.
