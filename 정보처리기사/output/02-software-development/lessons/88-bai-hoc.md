# 핵심 118: 가상 기억장치 (Virtual Memory)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và nguyên lý hoạt động của bộ nhớ ảo (가상 기억장치 - Virtual Memory): kỹ thuật quản lý bộ nhớ của hệ điều hành cho phép thực thi các chương trình có kích thước lớn hơn dung lượng bộ nhớ vật lý thực tế (RAM) bằng cách tận dụng ổ lưu trữ phụ (DASD).
- Phân biệt rõ ràng giữa Địa chỉ ảo (가상 주소 - Virtual Address) trên không gian đĩa và Địa chỉ thực (실기억 주소 - Physical Address) trên thanh RAM.
- Hiểu sâu hiện tượng Lỗi trang (페이지 부재 - Page Fault), cơ chế ngắt và quy trình nạp trang từ đĩa vào RAM.
- So sánh hai phương thức quản lý bộ nhớ ảo kinh điển: Phân trang (페이징 - Paging / kích thước khối cố định) và Phân đoạn (세그멘테이션 - Segmentation / kích thước khối logic biến đổi).

## 핵심 키워드 (Từ khóa)
- 가상 기억장치 (Virtual Memory / 보조기억장치의 주기억장치화)
- DASD (Direct Access Storage Device / 하드디스크, SSD 필수)
- 가상 주소 vs 실기억 주소 (Virtual Address vs Physical Address)
- 페이지 vs 프레임 (Page vs Frame / 고정 크기 분할)
- 세그먼트 (Segment / 가변 크기 논리 분할)
- 페이지 부재 (Page Fault / 인터럽트 발생 및 디스크 I/O)
- 주소 변환 (Address Mapping / 사상 함수 / MMU, TLB)

## 선행·연결 개념 (Kiến thức liên kết)
- [87-bai-hoc.md](87-bai-hoc.md): Bộ nhớ đệm Cache Memory và các chính sách ghi.
- [89-bai-hoc.md](89-bai-hoc.md): Phân loại máy tính song song theo Flynn và kỹ thuật xử lý song song.
- [정보처리기사/output/04-programming-language/lessons/03-bai-hoc.md](../../04-programming-language/lessons/03-bai-hoc.md): Quản lý bộ nhớ ảo của hệ điều hành và các thuật toán thay thế trang (FIFO, LRU, LFU).

## 읽는 방법 (Cách đọc)
- Nắm vững cấu trúc đơn vị hoán đổi giữa Ổ cứng và RAM:
  - **Ở phía Ổ cứng (Không gian ảo):** Chia thành các khối kích thước bằng nhau gọi là **Trang (Page)**.
  - **Ở phía RAM thực tế (Không gian vật lý):** Chia thành các ô chứa kích thước y hệt gọi là **Khung trang (Page Frame hoặc Block)**.
  - **Page Fault (Lỗi trang):** Khi CPU yêu cầu một lệnh thuộc Page $k$ nhưng Page này chưa được nạp lên RAM thực tế, phần cứng MMU kích hoạt ngắt Page Fault Trap $\rightarrow$ CPU tạm ngưng tiến trình, hệ điều hành đọc khối từ ổ cứng đắp vào Frame trống trên RAM rồi mới tiếp tục chạy.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh hai kỹ thuật tổ chức Bộ nhớ ảo:**

| Tiêu chuẩn so sánh | 페이징 기법 (Paging) | 세그멘테이션 기법 (Segmentation) |
| :--- | :--- | :--- |
| **Kích thước khối** | **Cố định (고정 크기)**; thường là 4KB | **Biến đổi (가변 크기)**; theo đơn vị logic nghiệp vụ (hàm, mảng, cấu trúc) |
| **Hiện tượng phân mảnh** | **Phân mảnh nội vi (내부 단편화 - Internal Fragmentation)** ở trang cuối cùng | **Phân mảnh ngoại vi (외부 단편화 - External Fragmentation)** do các phân đoạn kích thước khác nhau chèn vào |
| **Bảng quản lý địa chỉ** | **Page Map Table (PMT):** Ánh xạ Page Number $\rightarrow$ Frame Number | **Segment Map Table (SMT):** Quản lý Segment Base Address và Limit (Độ dài phân đoạn) |
| **Bảo vệ và chia sẻ** | Khó phân quyền chi tiết vì cắt nhỏ theo kích thước cố định | Dễ dàng phân quyền bảo mật (Read/Write/Execute) và chia sẻ module dùng chung |

- **Quy trình xử lý biến cố Lỗi trang (Page Fault Flow):**
  1. CPU gửi địa chỉ ảo cần đọc.
  2. MMU tra cứu bảng trang (Page Table); phát hiện bit hợp lệ (Valid Bit) $= 0$ (nghĩa là trang không nằm trên RAM).
  3. Kích hoạt ngắt **Page Fault Interrupt**; CPU chuyển quyền cho Nhân hệ điều hành (Kernel).
  4. Hệ điều hành tìm một Page Frame còn trống trên RAM (nếu hết thì dùng giải thuật thay thế như LRU/FIFO để đẩy một trang cũ ra đĩa).
  5. Đọc Page cần thiết từ ổ lưu trữ DASD nạp vào Frame vừa chọn.
  6. Cập nhật lại Page Table (đổi Valid Bit $= 1$ và điền Frame Number); cho phép CPU thực thi lại câu lệnh bị gián đoạn.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hiện tượng Trì trệ hệ thống (Thrashing):**
  - Khi kích thước bộ nhớ RAM quá nhỏ hoặc thuật toán thay thế trang không hợp lý, CPU dành hầu hết thời gian chỉ để hoán đổi trang (Page In / Page Out) ra vào ổ cứng thay vì xử lý tính toán thực tế.
  - Hậu quả: Hiệu suất sử dụng CPU tụt dốc thê thảm. Giải pháp: Bổ sung thêm RAM hoặc sử dụng mô hình Working Set / PFF (Page Fault Frequency) để cấp phát đủ khung trang cho tiến trình.

### 복습 체크리스트
- [ ] Nhớ Virtual Memory dùng ổ cứng đóng giả làm bộ nhớ chính để chạy chương trình vượt dung lượng RAM.
- [ ] Nhớ thiết bị lưu trữ bắt buộc phải là DASD (ổ đĩa truy cập trực tiếp), không dùng được băng từ SASD.
- [ ] Phân biệt Paging (kích thước cố định, phân mảnh nội vi) và Segmentation (kích thước logic biến đổi, phân mảnh ngoại vi).
- [ ] Giải thích được nguyên nhân gây ra hiện tượng Page Fault và cách hệ thống xử lý.
