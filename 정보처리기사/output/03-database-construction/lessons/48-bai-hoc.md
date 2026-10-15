# 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc 4 khối phân vùng nền tảng của Hệ thống tệp UNIX/Linux: **Khối khởi động (`부트 블록 / Boot Block`)**, **Siêu khối (`슈퍼 블록 / Super Block`)**, **Khối I-node (`I-node 블록`)**, và **Khối dữ liệu (`데이터 블록 / Data Block`)**.
- Phân tích chi tiết thành phần và ý nghĩa của các trường siêu dữ liệu được lưu trữ bên trong cấu trúc **I-node (Index Node)**.
- Khắc ghi điểm bẫy đề thi kinh điển: **Tên tệp tin (`파일명`) TUYỆT ĐỐI KHÔNG nằm trong I-node**, mà được lưu trong Data Block của thư mục cha.
- Hiểu rõ cơ chế con trỏ gián tiếp (Direct, Indirect pointers) giúp UNIX quản lý các tệp tin có dung lượng lớn.

## 핵심 키워드 (Từ khóa)
- UNIX 파일 시스템 (Hệ thống tệp UNIX / UNIX File System)
- 부트 블록 (Khối khởi động / Boot Block)
- 슈퍼 블록 (Siêu khối / Super Block: 파일 시스템 전체 정보)
- I-node 블록 (Khối I-node / Index Node: 파일 메타데이터)
- 데이터 블록 (Khối dữ liệu / Data Block: 실제 데이터)
- BSID (Mẹo nhớ thứ tự 4 khối: Boot - Super - I-node - Data)
- 간접 포인터 (Con trỏ gián tiếp: Indirect Pointers)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([47-bai-hoc.md](47-bai-hoc.md)):** Khối I-node chính là cấu trúc hiện thực hóa danh sách kiểm soát quyền hạn (ACL) và quản lý khối đĩa của hệ điều hành.
- **Tiếp nối sang bài sau ([49-bai-hoc.md](49-bai-hoc.md)):** Các câu lệnh hệ thống UNIX như `chmod`, `chown`, `stat`, `ls -l` trực tiếp đọc và sửa đổi các trường thông tin bên trong khối I-node này.

## 읽는 방법 (Cách đọc)
- Học thuộc câu thần chú thứ tự 4 khối: **B - S - I - D (Boot $\rightarrow$ Super $\rightarrow$ I-node $\rightarrow$ Data)**.
- Nhớ câu phân biệt trắc nghiệm:
  - Thông tin dung lượng toàn bộ hệ thống tệp, số khối trống $\rightarrow$ **슈퍼 블록 (Super Block)**.
  - Thông tin quyền hạn, chủ sở hữu, thời gian tạo, con trỏ đĩa của từng tệp $\rightarrow$ **I-node 블록**.
  - **Tên tệp lưu ở đâu?** $\rightarrow$ Lưu tại **데이터 블록 của thư mục chứa nó**, KHÔNG nằm trong I-node!

---

## 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng 4 khối cấu tạo của Hệ thống tệp UNIX (UNIX 파일 시스템 4대 블록):**
  | Tên khối | Thuật ngữ tiếng Hàn & Anh | Chức năng kỹ thuật cốt lõi | Dấu hiệu nhận diện đề thi |
  |---|---|---|---|
  | **Khối khởi động** | `부트 블록` (Boot Block) | Nằm ở đầu đĩa; chứa mã chương trình nạp hệ điều hành (Bootstrap Loader) cần thiết khi bật máy tính. | Chứa mã nạp hệ điều hành (`부팅 시 필요한 코드`). |
  | **Siêu khối** | `슈퍼 블록` (Super Block) | Lưu trữ **thông tin tổng quan của toàn bộ hệ thống tệp** (Tổng số khối, số khối đĩa còn trống, tổng số I-node, số I-node còn trống). | Thông tin quản lý toàn hệ thống tệp (`전체 파일 시스템에 대한 정보`). |
  | **Khối I-node** | `I-node 블록` (Index Node Block) | Lưu trữ **toàn bộ Siêu dữ liệu (Metadata)** của từng tệp tin và thư mục (chủ sở hữu, quyền truy cập, kích thước, thời gian, danh sách con trỏ khối đĩa). | Chứa thông tin chi tiết từng tệp (`각 파일이나 디렉터리에 대한 정보`). |
  | **Khối dữ liệu** | `데이터 블록` (Data Block) | Lưu trữ **nội dung dữ liệu thực tế** của các tệp tin hoặc danh sách các tệp con nằm trong một thư mục. | Nơi lưu ruột dữ liệu thực sự (`실제 파일 데이터 저장`). |

- **2. Chi tiết cấu trúc I-node (I-node의 주요 저장 정보):**
  - **UID / GID:** Mã số định danh của chủ sở hữu tệp (`소유자 ID`) và nhóm người dùng.
  - **Quyền truy cập (File Permissions):** 9 bit quyền (rwxrwxrwx) cho User, Group, Others.
  - **Kích thước tệp (File Size):** Tính theo số byte.
  - **Nhãn thời gian (Time Stamps):** Thời gian truy cập cuối (atime), sửa đổi nội dung cuối (mtime), thay đổi inode cuối (ctime).
  - **Số lượng liên kết cứng (Link Count):** Số lượng tên tệp đang cùng trỏ vào I-node này.
  - **Địa chỉ con trỏ khối dữ liệu (Block Pointers):** Gồm 15 con trỏ (12 con trỏ trực tiếp Direct, 1 con trỏ gián tiếp đơn Single Indirect, 1 gián tiếp kép Double Indirect, 1 gián tiếp ba Triple Indirect).
  - **BẪY QUAN TRỌNG:** Tên tệp tin (`파일명`) **KHÔNG** được lưu trong I-node!
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Thứ tự sắp xếp các khối trong hệ thống tệp UNIX là gì?"* $\rightarrow$ Đáp án: **부트 블록 $\rightarrow$ 슈퍼 블록 $\rightarrow$ I-node 블록 $\rightarrow$ 데이터 블록 (BSID)**.
  - Đề hỏi: *"Thông tin nào sau đây KHÔNG được lưu trong I-node?"* $\rightarrow$ Đáp án: **파일명 (Tên tệp tin)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế phân cấp con trỏ trong I-node:**
  - 12 con trỏ trực tiếp (Direct Pointers): Trỏ thẳng đến 12 khối dữ liệu đầu tiên (truy xuất siêu tốc cho các tệp nhỏ).
  - 1 con trỏ Single Indirect: Trỏ đến 1 khối chứa danh sách địa chỉ của các khối dữ liệu tiếp theo.
  - 1 con trỏ Double Indirect: Trỏ đến khối chứa danh sách các khối Single Indirect.
  - 1 con trỏ Triple Indirect: Trỏ đến khối cấp 3, cho phép UNIX quản lý các tệp khổng lồ lên tới hàng Terabyte.

### 복습 체크리스트
- [ ] Thuộc lòng thứ tự 4 khối trong hệ thống tệp UNIX: Boot -> Super -> I-node -> Data (BSID).
- [ ] Phân biệt được nhiệm vụ của Super Block (toàn hệ thống) và I-node Block (từng tệp).
- [ ] Khẳng định được tên tệp (파일명) không nằm trong I-node.
- [ ] Kể tên các siêu dữ liệu lưu trong I-node (UID, GID, quyền, kích thước, thời gian, con trỏ).
