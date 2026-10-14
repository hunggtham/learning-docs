# 083: 버블 정렬 (Bubble Sort)

## 083: 버블 정렬 (Bubble Sort)
Phần “083: 버블 정렬 (Bubble Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **인접한 두 개의 레코드** 키 값을 비교하여 크기에 따라 위치 교환(Swap). (So sánh 2 phần tử cạnh nhau, số to đẩy lùi về sau. Số to nhất sẽ "nổi bọt" chìm xuống cuối mảng sau vòng đầu tiên).
- **종료 조건:** 더 이상 교환이 일어나지 않으면 정렬 끝. 플래그 비트(Flag Bit) 사용. (Dùng cờ Flag, nếu chạy hết 1 vòng mà không có ai đổi chỗ nghĩa là đã sắp xếp xong).
- **시간 복잡도:** O(n²).

- 💡 **Mẹo ghi nhớ (Mnemonics):** Bubble (Nổi bọt) = Từ khóa **Hai phần tử kề nhau** (Hai cái kề nhau), **플래그 비트** (Flag bit).

---
