# 081-2: 셸 정렬 (Shell Sort)

## 081-2: 셸 정렬 (Shell Sort)
Phần “081-2: 셸 정렬 (Shell Sort)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **삽입 정렬(Insertion Sort)을 보완/확장**한 알고리즘. (Phiên bản nâng cấp của Insertion Sort).
- 입력 파일을 매개변수 **h(간격)** 만큼 떨어진 레코드들끼리 묶어 서브파일을 구성하고, 각 서브파일을 삽입 정렬. (Chia mảng thành các nhóm con cách nhau một khoảng $h$, sắp xếp chèn từng nhóm. Sau đó giảm $h$ dần dần về 1).
- **시간 복잡도:** 평균 O(n^1.5), 최악 O(n²). 부분적으로 정렬되어 있는 경우에 매우 유리. (Nhanh hơn O(n²) thông thường. Rất hiệu quả nếu mảng đã "hơi hơi" có thứ tự).

- **Vietnamese Explanation:** Insertion Sort thường yếu khi số nhỏ nằm tuốt ở cuối mảng (phải nhích từng bước lên đầu). Shell Sort dùng khoảng cách $h$ (ví dụ nhảy 5 bước 1 lần) để đưa số nhỏ về đầu nhanh hơn.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Shell = Vỏ ốc (Xoáy từ rộng vào hẹp). Từ khóa: **h (Khoảng cách nhảy)**, **O(n^1.5)**.

---
