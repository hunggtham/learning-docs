# 핵심 118: 가상 기억장치 (Virtual Memory)

## 핵심 118: 가상 기억장치 (Virtual Memory)
Phần “핵심 118: 가상 기억장치 (Virtual Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 기억 용량이 작은 주기억장치를 마치 큰 용량을 가진 것처럼 사용할 수 있도록 하는 운영체제의 메모리 운영 기법. (Lấy một phần ổ cứng ảo hóa thành RAM, giúp máy tính chạy được các chương trình nặng hơn dung lượng RAM thực tế.)
- 보조기억장치는 디스크 같은 DASD 장치이어야 한다. (Bắt buộc dùng đĩa từ / HDD / SSD - DASD, không dùng băng từ được.)
- **주소의 사용 (Địa chỉ):**
  - **가상 주소 (Virtual Address):** Địa chỉ ảo trên ổ cứng. Đơn vị thay thế là Page (Trang).
  - **실기억 주소 (Physical Address):** Địa chỉ thực trên RAM. Đơn vị thay thế là Block / Frame.
- **페이지 부재 (Page Fault):** 가상 페이지가 주기억장치에 없는 경우. 프로그램 수행이 중단된다. (Khi dữ liệu cần tìm không có trong RAM mà nằm trên đĩa, CPU phải tạm dừng để lấy vào.)
- **주소 매핑 (Address Mapping):** 가상주소를 실기억주소로 변환하는 작업이다. 사상함수가 사용된다. (Đổi địa chỉ Ảo thành địa chỉ Thực qua hàm ánh xạ.)

- **Vietnamese Explanation:** Khi RAM 4GB nhưng game nặng 10GB, HĐH dùng ổ cứng làm RAM ảo. RAM ảo chia thành các "Trang" (Page). Khi CPU cần 1 trang mà nó chưa nằm trong RAM thực, nó bị "Page Fault", máy sẽ hơi khựng lại để tải từ ổ cứng lên.
- 💡 **Mẹo ghi nhớ (Mnemonics):** Virtual = Đĩa cứng đóng giả làm RAM. Page Fault (Lỗi trang) = Trang chưa nạp, phải đợi.

---
