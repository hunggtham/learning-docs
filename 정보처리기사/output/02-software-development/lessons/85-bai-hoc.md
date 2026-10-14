# 핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)

## 핵심 113 & 114: 보조기억장치 및 디스크 접근 시간 (Auxiliary Memory & Disk Access Time)

### 보조기억장치 (Bộ nhớ phụ)
Phần “보조기억장치 (Bộ nhớ phụ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 주기억장치에 비해 속도는 느리지만 저장 용량이 크다. 전원이 차단되어도 내용이 그대로 유지된다. (Chậm hơn RAM nhưng dung lượng lớn, lưu trữ vĩnh viễn.)
- **자기 테이프 (Magnetic Tape - Băng từ):**
  - 순차처리(SASD)만 할 수 있는 대용량 저장매체. (Chỉ truy cập tuần tự, không nhảy cóc được.)
  - 자료의 백업용으로 많이 사용함. (Thường dùng để Backup.)
- **자기 디스크 (Magnetic Disk - Đĩa từ / HDD):**
  - 순차, 비순차(직접) 처리가 모두 가능한 DASD 방식. (Có thể truy cập trực tiếp ngẫu nhiên.)
  - **Track (Rãnh):** Vòng tròn đồng tâm.
  - **Sector (Cung):** Track chia nhỏ, là đơn vị lưu trữ cơ bản.
  - **Cylinder (Trụ):** Tập hợp các track cùng vị trí trên các mặt đĩa.

### 디스크의 Access Time (Thời gian truy cập đĩa)
Phần “디스크의 Access Time (Thời gian truy cập đĩa)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `Access Time = Seek Time + Latency Time (Rotational Delay) + Transmission Time`
- **Seek Time (Thời gian tìm rãnh):** Đầu đọc di chuyển đến đúng Track.
- **Latency Time (Thời gian chờ xoay):** Đợi đĩa xoay đúng đến Sector cần đọc.
- **Transmission Time (Thời gian truyền):** Đọc Sector và truyền vào RAM.

- **Vietnamese Explanation:** Tape giống như băng cassette (muốn nghe bài 5 phải tua qua bài 1,2,3,4). Disk giống như đĩa CD hoặc đĩa than, bạn có thể đặt kim đọc vào bất kỳ bài nào (DASD).
- 💡 **Mẹo ghi nhớ (Mnemonics):** Công thức tìm ổ cứng: SLT. **S**eek (Tìm Track) -> **L**atency (Đợi Sector xoay tới) -> **T**ransmission (Truyền đi).

---
