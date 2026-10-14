# 13. 검색 및 해싱 (Search & Hashing)

## 13. 검색 및 해싱 (Search & Hashing)
Phần “13. 검색 및 해싱 (Search & Hashing)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **이분 검색 / 이진 검색 (Binary Search)**:
  - Dữ liệu phải được sắp xếp (순서화).
  - Tìm kiếm bằng cách chia đôi: `M = (F + L) / 2` (F: Đầu, L: Cuối).
  - Cực kỳ nhanh do mỗi lần giảm một nửa phạm vi tìm kiếm.
- **해싱 (Hashing)**:
  - Tính toán địa chỉ (Home Address) qua hàm băm (Hash Function).
  - Cực nhanh, tốt cho thêm/xóa thường xuyên, nhưng tốn không gian.
  - **Thuật ngữ**:
    - **버킷 (Bucket)**: Khu vực lưu trữ, gồm nhiều Slot.
    - **슬롯 (Slot)**: Chỗ lưu 1 bản ghi (Record).
    - **Collision (충돌)**: 2 khóa ra cùng địa chỉ.
    - **Synonym**: Các khóa cùng địa chỉ.
    - **Overflow (오버플로)**: Hết chỗ lưu khi xảy ra Collision.
- 💡 **Mẹo ghi nhớ**: 해싱 용어: B/S/C/S/O (Bucket, Slot, Collision, Synonym, Overflow) -> **Bỏ Sót Con Sẽ Ôm**
