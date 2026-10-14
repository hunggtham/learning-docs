# 081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)

## 081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)
Phần “081: 삽입 정렬 (Insertion Sort - Sắp xếp chèn)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **이미 순서화된 파일(앞부분)**에 새로운 레코드를 **순서에 맞게 삽입**시켜 정렬. (Lấy phần tử hiện tại chèn vào đúng vị trí trong phần mảng đã sắp xếp phía trước nó).
- **Thời gian (Time Complexity):** O(n²) cho cả Trung bình và Tệ nhất.
- **Số vòng lặp (Pass):** Mảng có n phần tử thì chạy (n-1) vòng. Bắt đầu xét từ phần tử thứ 2.

- **Ví dụ (Example):** Xếp bài tá lả. Bạn rút một lá bài mới lên, xem trên tay bài đã xếp sẵn, thấy chỗ nào vừa thì "chèn" nó vào đó.
- 💡 **Mẹo ghi nhớ (Mnemonics):** 삽입 (Chèn) = Từ khóa "Đã được sắp xếp sẵn" (Đã sắp xếp sẵn). Luôn O(n²).
