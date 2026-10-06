# 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối encryption với access control, để phân biệt bảo mật dữ liệu khi lưu/truyền với quyền ai được phép sử dụng dữ liệu.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **106-107. 튜플(Tuple)과 속성(Attribute)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

암호화, 기법과, 접근, 통제

> **Nối mạch:** Ở chặng này của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**에서 만든 기준을 이어받아 **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

Từ **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, ta đã có điểm tựa để bước vào **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/54 trước khi đi vào chi tiết.

Để đọc **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)

Các ý ngay dưới **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để đối chiếu cách hiểu.

Phần “개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개념 (Khái niệm):** Dùng **CÙNG MỘT KHÓA** để mã hóa và giải mã (단일키 - Khóa đơn).
- **장점 (Ưu điểm):** Tốc độ xử lý cực kỳ nhanh.
- **단점 (Nhược điểm):** Khó phân phối và quản lý khóa khi có quá nhiều người dùng.
- **종류 (Thuật toán tiêu biểu):** DES, AES, SEED, ARIA. (Chia làm 2 dạng: Block - theo khối, Stream - theo luồng bit).

> 💡 **Mẹo ghi nhớ:** **Đối-Cá-Nhanh-Khó** (Khóa Đối xứng = Khóa Cá nhân = Nhanh = Khó quản lý khóa).

Với **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)

Bây giờ ta đi vào nội dung của **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 종류 (Loại) | 기준 (Tiêu chí) | 특징 (Đặc điểm VN) |
|---|---|---|
| **DAC (임의 접근통제)** | 소유자 (Chủ sở hữu) | Chủ dữ liệu tự do cấp/thu quyền (GRANT/REVOKE). |
| **MAC (강제 접근통제)** | 보안 등급 (Mức độ bảo mật) | Hệ thống ép buộc dựa trên cấp độ bảo mật (VD: Top Secret). |
| **RBAC (역할기반 접근통제)** | 역할 (Vai trò) | Quyền gắn với chức vụ (VD: Manager, Staff). Đổi chức vụ = tự đổi quyền. |

Khi đọc **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Sau khi đọc **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, đừng bắt đầu lại từ số không. **MAC 보안 모델 (Các mô hình bảo mật của MAC)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **MAC 보안 모델 (Các mô hình bảo mật của MAC)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### MAC 보안 모델 (Các mô hình bảo mật của MAC)

Phần nguồn của **MAC 보안 모델 (Các mô hình bảo mật của MAC)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “MAC 보안 모델 (Các mô hình bảo mật của MAC)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **벨-라파듈라 (Bell-LaPadula):** Tập trung vào **기밀성 (Tính Bảo mật / Kín đáo)** (Quân đội). Không đọc lên trên, Không ghi xuống dưới.
- **비바 (Biba):** Tập trung vào **무결성 (Tính Toàn vẹn)**. Ngăn chặn việc sửa đổi trái phép.
- **클락-윌슨 (Clark-Wilson):** Dành cho thương mại, chỉ cho phép sửa qua phần mềm được ủy quyền.
- **만리장성 (Chinese Wall):** Tránh xung đột lợi ích (người xem hồ sơ công ty A thì không được xem của đối thủ B).

---

Các bullet của **MAC 보안 모델 (Các mô hình bảo mật của MAC)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **MAC 보안 모델 (Các mô hình bảo mật của MAC)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **106-107. 튜플(Tuple)과 속성(Attribute)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
