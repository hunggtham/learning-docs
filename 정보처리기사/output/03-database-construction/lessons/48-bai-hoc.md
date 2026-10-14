# 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

## 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)
Phần “1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **부트 블록 (Boot Block - Khối khởi động):**
  - 부팅 시 필요한 코드를 저장하고 있는 블록.
  - _Giải thích VN:_ Khối lưu trữ mã cần thiết khi khởi động máy.
  - _Ví dụ:_ MBR (Master Boot Record) trong Windows, nhưng ở UNIX nó nằm ở Boot Block, chứa bootloader để nạp hệ điều hành.

- **슈퍼 블록 (Super Block - Siêu khối):**
  - 전체 파일 시스템에 대한 정보를 저장. 사용 가능한 I-node, 사용 가능한 디스크 블록의 개수 등을 포함.
  - _Giải thích VN:_ Chứa thông tin về toàn bộ hệ thống tệp: số lượng I-node trống, các khối đĩa trống. Mỗi hệ thống tệp có Super Block riêng.
  - _Ví dụ:_ Giống như mục lục tổng quát của một thư viện cho biết thư viện có bao nhiêu kệ sách và bao nhiêu sách chưa được mượn.

- **I-node 블록 (I-node Block - Khối I-node):**
  - 각 파일이나 디렉터리에 대한 모든 정보를 저장. (소유자 UID/GID, 파일 크기, 타입, 생성/변경 시기, 권한, 데이터 블록 시작 주소 등).
  - _Giải thích VN:_ Lưu trữ siêu dữ liệu (metadata) của tệp (chủ sở hữu, kích thước, quyền, địa chỉ bắt đầu của dữ liệu, thời gian tạo/sửa).
  - _Ví dụ:_ I-node giống như thẻ căn cước (ID card) của tệp, mọi thông tin quản lý đều nằm ở đây trừ tên tệp và nội dung thực sự.

- **데이터 블록 (Data Block - Khối dữ liệu):**
  - 실제 파일에 대한 데이터가 저장된 블록.
  - _Giải thích VN:_ Nơi lưu trữ nội dung thực tế của tệp hoặc danh sách các thư mục con.
  - _Ví dụ:_ Các trang sách chứa nội dung chữ bên trong thư viện.

> 💡 **Mẹo ghi nhớ (Mnemonics):**
> Thứ tự các khối: **B**oot -> **S**uper -> **I**-node -> **D**ata (**BSID** - Bác Sĩ I-node Dễ thương).

---
