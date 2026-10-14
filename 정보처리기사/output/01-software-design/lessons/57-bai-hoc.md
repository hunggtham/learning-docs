# 14. 파일 편성 방식 (File Organization)

## 14. 파일 편성 방식 (File Organization)
Phần “14. 파일 편성 방식 (File Organization)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **순차 파일 (Sequential File)**: Lưu nối tiếp. Phù hợp băng từ (Magnetic Tape). Nhanh khi xử lý tuần tự, chậm khi thêm/xóa/tìm kiếm.
- **색인 순차 파일 (Indexed Sequential File / ISAM)**:
  - Vừa tuần tự vừa ngẫu nhiên (Sequential + Random).
  - Gồm 3 vùng: **기본 구역 (Prime Area)**, **색인 구역 (Index Area)**, **오버플로 구역 (Overflow Area)**.
  - Dễ dàng chèn/xóa, nhưng tốn dung lượng cho Index/Overflow và chậm hơn File ngẫu nhiên thuần.
- 💡 **Mẹo ghi nhớ**: ISAM 3 구역 (P/I/O - Prime, Index, Overflow) -> **Phải In Ô**

---
# 1과목 Chapter 1. 요구사항 확인 (Requirements)
