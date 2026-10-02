# 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối UNIX commands với filesystem, process, text stream và exit status, để chọn lệnh theo đối tượng cần thao tác.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

주요, 명령어

> **Chuyển mạch:** Ở chặng này của **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**에서 만든 기준을 이어받아 **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

Ở bước 49/54, **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** xuất hiện như phần tiếp nối của **1. UNIX 파일 시스템의 구조 (Cấu trúc hệ thống tệp UNIX)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. UNIX의 주요 명령어 (Các lệnh UNIX chính)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 명령어 (Command) | 의미 (Ý nghĩa) | Giải thích & Ví dụ (VN) |
|---|---|---|
| `fork` | 새로운 프로세스 생성 (Tạo tiến trình con/nhân bản tiến trình). | Giống như phân thân. Ví dụ: Tiến trình cha gọi `fork` tạo ra một tiến trình con y hệt để làm việc song song. |
| `exec` | 새로운 프로세스 수행 (Thực thi tiến trình mới). | Thay thế tiến trình hiện tại bằng tiến trình mới. Ví dụ: Dùng `exec` để mở chương trình máy tính (calculator). |
| `&` | 백그라운드 처리 (Chạy nền). | Đặt ở cuối lệnh. Ví dụ: `find / -name test.txt &` (Tìm kiếm ngầm, cho phép gõ tiếp lệnh khác). |
| `wait` | 하위 프로세스 종료 대기 (Đợi tiến trình con kết thúc). | Ví dụ: Tiến trình cha đứng đợi (wait) tiến trình con hoàn thành công việc mới tiếp tục. |
| `exit` | 프로세스 수행 종료 (Kết thúc tiến trình). | Ví dụ: Gõ `exit` để đóng terminal. |
| `cat` | 파일 내용 표시 (Hiển thị nội dung tệp, giống `TYPE` trong DOS). | Ví dụ: `cat file.txt` (In nội dung file.txt ra màn hình). |
| `chmod` | 파일 권한 지정 (Thay đổi quyền truy cập tệp). | Ví dụ: `chmod 777 file.sh` (Cấp toàn quyền đọc, ghi, chạy). |
| `chown` | 소유자 변경 (Thay đổi chủ sở hữu). | Ví dụ: `chown root file.txt` (Đổi chủ tệp thành root). |
| `mount` | 파일 시스템 마운팅 (Gắn hệ thống tệp). | Ví dụ: Cắm USB vào và dùng `mount` để hệ thống nhận diện nội dung USB. |
| `mkfs` | 파일 시스템 생성 (Tạo hệ thống tệp). | Format ổ đĩa. Ví dụ: `mkfs.ext4 /dev/sda1`. |
| `chdir` / `cd` | 디렉터리 위치 변경 (Thay đổi thư mục). | Ví dụ: `cd /home`. |
| `fsck` | 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi hệ thống tệp). | Giống chkdsk trong Windows. Ví dụ: `fsck /dev/sda1`. |
| `rmdir` | 디렉터리 삭제 (Xóa thư mục rỗng). | Ví dụ: `rmdir empty_folder`. |
| `ls` | 파일 목록 확인 (Xem danh sách tệp). | Ví dụ: `ls -l` (Xem danh sách chi tiết). |
| `getpid` / `getppid` | 자신의 / 부모 프로세스 ID 획득 (Lấy PID / Parent PID). | ID tiến trình để quản lý (vd: dùng kill để tắt). |
| `cp` / `mv` / `rm`| 복사 (Copy) / 이동 및 이름 변경 (Move/Rename) / 삭제 (Remove). | `cp a.txt b.txt`, `mv old.txt new.txt`, `rm a.txt`. |
| `finger` | 사용자 정보 표시 (Hiển thị thông tin người dùng). | Xem ai đang đăng nhập vào hệ thống. |

---

# CHAPTER 01 SQL 응용 (Ứng dụng SQL)

Như vậy, **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **2. UNIX의 주요 명령어 (Các lệnh UNIX chính)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
