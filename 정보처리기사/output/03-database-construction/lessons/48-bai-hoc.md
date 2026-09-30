# 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

UNIX, 파일, 시스템의, 구조

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**에서 만든 기준을 이어받아 **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** và nối nó với **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)

Từ **148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)**, ta đã có điểm tựa để bước vào **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 48/54 trước khi đi vào chi tiết.

Để đọc **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

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

Điểm chốt của **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.