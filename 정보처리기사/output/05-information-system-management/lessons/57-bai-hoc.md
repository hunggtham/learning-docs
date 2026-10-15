# Windows와 UNIX 운영체제 (Hệ điều hành Windows & UNIX)

## 학습 목표 (Mục tiêu)
- Nắm vững 5 đặc trưng kiến trúc nổi bật của hệ điều hành Windows: GUI, Đa nhiệm ưu tiên (선점형 멀티태스킹 - Preemptive Multitasking), Cắm và chạy (PnP), Nhúng và liên kết đối tượng (OLE), Tên tệp dài 255 ký tự.
- Hiểu rõ các đặc tính nền tảng của hệ điều hành UNIX: Hệ thống phân chia thời gian (시분할 시스템 - TSS), Hệ thống mở (Open System), Tính khả chuyển nhờ ngôn ngữ C, Hệ thống tệp dạng cây (Tree Structure).
- Phân tích vai trò và cấu trúc của Khối điều khiển tệp (File Descriptor / File Control Block - FCB) trong việc quản lý tệp tin của hệ điều hành.

## 핵심 키워드 (Từ khóa)
- **Windows 특성**: GUI, 선점형 멀티태스킹 (Preemptive Multitasking), PnP (Plug and Play), OLE (Object Linking and Embedding), 긴 파일명 (255 ký tự).
- **UNIX 특성**: 시분할 시스템 (TSS), C언어 작성 (Tính khả chuyển Portability cao), 트리 구조 파일 시스템, 다중 사용자 (Multi-User) / 다중 작업 (Multi-Tasking).
- **파일 디스크립터 (File Descriptor / FCB)**: Khối chứa siêu dữ liệu tệp tin (Metadata), được nạp vào RAM khi mở tệp.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [56-bai-hoc.md](56-bai-hoc.md) (Mục đích và cấu trúc hệ điều hành).
- Liên kết với [58-bai-hoc.md](58-bai-hoc.md) (Kiến trúc các thành phần của UNIX).
- Liên kết với [64-bai-hoc.md](64-bai-hoc.md) (Các lệnh cơ bản và biến môi trường UNIX).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý các từ khóa nhận dạng:
  - "Tự động phát hiện và cấu hình phần cứng khi cắm vào máy tính" $\rightarrow$ **PnP (Plug and Play)**.
  - "Nhúng biểu đồ Excel vào tài liệu Word để tự cập nhật" $\rightarrow$ **OLE (Object Linking and Embedding)**.
  - "Hệ điều hành có quyền cưỡng chế ngắt quyền CPU của ứng dụng lỗi" $\rightarrow$ **선점형 멀티태스킹 (Preemptive)**.
  - "Phần lớn mã nguồn viết bằng ngôn ngữ nào giúp UNIX dễ dàng cài đặt lên nhiều phần cứng khác nhau?" $\rightarrow$ **Ngôn ngữ C**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Năm đặc trưng cốt lõi của Hệ điều hành Windows
| Đặc trưng (KR / EN) | Khái niệm kỹ thuật | Ý nghĩa đối với người dùng |
| :--- | :--- | :--- |
| **GUI (Graphical User Interface)** | Giao diện đồ họa tương tác trực quan qua chuột, biểu tượng icon, cửa sổ và menu | Thay thế giao diện dòng lệnh (CLI), dễ học và sử dụng |
| **선점형 멀티태스킹 / (Preemptive Multitasking)** | Hệ điều hành nắm quyền kiểm soát bộ lập lịch CPU, có thể cưỡng chế dừng một ứng dụng đang treo hoặc lỗi | Ngăn ngừa hiện tượng toàn bộ máy tính bị tê liệt khi một ứng dụng gặp sự cố |
| **PnP (Plug and Play)** | Cơ chế tự động nhận diện thiết bị ngoại vi mới cắm vào phần cứng và tự động nạp Driver thích hợp | Người dùng không cần cấu hình jumper hoặc cài đặt driver thủ công phức tạp |
| **OLE (Object Linking and Embedding)** | Công nghệ cho phép nhúng (Embed) hoặc tạo liên kết (Link) đối tượng từ ứng dụng này vào ứng dụng khác | Chèn bảng tính Excel vào tài liệu Word; khi sửa số liệu Excel thì Word tự cập nhật |
| **긴 파일명 (Long Filename)** | Hỗ trợ đặt tên tệp và thư mục có độ dài lên tới **255 ký tự** (bao gồm khoảng trắng và chữ có dấu) | Vượt trội hoàn toàn so với chuẩn cũ 8.3 ký tự của hệ điều hành DOS |

#### 2. Các đặc tính kiến trúc của Hệ điều hành UNIX
- **시분할 시스템 (Time Sharing System - TSS)**: Hệ thống chia nhỏ thời gian xử lý của CPU thành các lát thời gian (Time Slices) cực ngắn cấp phát luân phiên cho nhiều người dùng tương tác đồng thời qua các thiết bị đầu cuối (Terminals).
- **C언어 기반 작성 (Tính khả chuyển cao - Portability)**: Hơn 90% mã nguồn nhân UNIX được viết bằng ngôn ngữ lập trình C (chỉ phần giao tiếp thanh ghi phần cứng viết bằng Assembly). Nhờ đó, UNIX có thể dễ dàng được chuyển dịch (porting) sang bất kỳ nền tảng phần cứng CPU nào.
- **다중 사용자 (Multi-User) & 다중 작업 (Multi-Tasking)**: Hỗ trợ nhiều tài khoản người dùng đăng nhập đồng thời và mỗi người dùng có thể kích hoạt nhiều tiến trình chạy ngầm song song.
- **트리 구조 파일 시스템 (Tree-Structured File System)**: Toàn bộ các tệp tin, thư mục và cả các thiết bị ngoại vi phần cứng (bàn phím, đĩa, máy in) đều được trừu tượng hóa và quản lý thống nhất dưới dạng một cây phân cấp bắt đầu từ thư mục gốc Root (`/`).

#### 3. Khối điều khiển tệp (File Descriptor / FCB)
- **Định nghĩa**: Bảng thông tin siêu dữ liệu (Metadata) do hệ điều hành tạo ra và duy trì độc lập cho từng tệp tin để theo dõi và quản lý.
- **Thông tin lưu trữ trong FCB**:
  - Tên tệp tin và phần mở rộng.
  - Vị trí vật lý của tệp trên các cung đĩa (Track/Sector/Cluster).
  - Kích thước hiện tại và kích thước tối đa của tệp.
  - Thuộc tính và quyền truy cập (Read-only, Hidden, Owner Permissions).
  - Dấu thời gian (Timestamp: Ngày tạo, ngày chỉnh sửa, ngày truy cập gần nhất).
- **Vị trí lưu trữ**: Nằm trên bộ nhớ ngoài (ổ đĩa đính kèm cấu trúc thư mục); khi một tiến trình mở tệp bằng lời gọi hệ thống `open()`, FCB của tệp đó sẽ được nạp vào bộ nhớ chính (RAM).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. So sánh Preemptive Multitasking vs Non-Preemptive Multitasking
- **Non-Preemptive (Không ưu tiên / Hợp tác - như Windows 3.1)**: Một tiến trình một khi đã nhận CPU thì sẽ chiếm giữ cho đến khi nó tự nguyện nhả CPU hoặc kết thúc. Nếu tiến trình bị rơi vào vòng lặp vô tận, cả hệ thống sẽ bị treo cứng.
- **Preemptive (Ưu tiên / Chiếm đoạt - như Windows hiện đại & UNIX)**: Bộ đếm thời gian phần cứng (Hardware Timer) phát tín hiệu ngắt định kỳ. Hệ điều hành hoàn toàn có quyền cưỡng chế thu hồi CPU từ một tiến trình đang chạy để chuyển giao cho tiến trình có độ ưu tiên cao hơn.

---

### 복습 체크리스트
- [ ] Tính năng Plug and Play (PnP) của Windows giải quyết thao tác phức tạp nào khi lắp ráp phần cứng?
- [ ] Tại sao việc viết nhân hệ điều hành UNIX bằng ngôn ngữ C lại mang lại tính khả chuyển (Portability) cao?
- [ ] Phân biệt sự khác nhau giữa cơ chế đa nhiệm Preemptive và Non-Preemptive?
- [ ] File Descriptor (FCB) chứa những thông tin quản lý cốt lõi nào về một tệp tin?
