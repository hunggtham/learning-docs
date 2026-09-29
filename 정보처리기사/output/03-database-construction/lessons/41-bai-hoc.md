# 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **106-107. 튜플(Tuple)과 속성(Attribute)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

암호화, 기법과, 접근, 통제

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**에서 만든 기준을 이어받아 **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

Sau khi đã đặt nền bằng **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, ta chuyển sang **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**. Đây là mắt xích 41/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)**. Hãy xác định **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)

Phần nguồn của **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **개념 (Khái niệm):** Dùng **CÙNG MỘT KHÓA** để mã hóa và giải mã (단일키 - Khóa đơn).
- **장점 (Ưu điểm):** Tốc độ xử lý cực kỳ nhanh.
- **단점 (Nhược điểm):** Khó phân phối và quản lý khóa khi có quá nhiều người dùng.
- **종류 (Thuật toán tiêu biểu):** DES, AES, SEED, ARIA. (Chia làm 2 dạng: Block - theo khối, Stream - theo luồng bit).

> 💡 **Mẹo ghi nhớ:** **Đối-Cá-Nhanh-Khó** (Khóa Đối xứng = Khóa Cá nhân = Nhanh = Khó quản lý khóa).

Với **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Ta vừa chốt **개인키 암호 방식 (Private Key / Symmetric Key - Mã hóa Khóa đối xứng)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)

Các ý ngay dưới **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

| 종류 (Loại) | 기준 (Tiêu chí) | 특징 (Đặc điểm VN) |
|---|---|---|
| **DAC (임의 접근통제)** | 소유자 (Chủ sở hữu) | Chủ dữ liệu tự do cấp/thu quyền (GRANT/REVOKE). |
| **MAC (강제 접근통제)** | 보안 등급 (Mức độ bảo mật) | Hệ thống ép buộc dựa trên cấp độ bảo mật (VD: Top Secret). |
| **RBAC (역할기반 접근통제)** | 역할 (Vai trò) | Quyền gắn với chức vụ (VD: Manager, Staff). Đổi chức vụ = tự đổi quyền. |

Khi đọc **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu.

Sau khi đọc **접근통제 기술 (Access Control - Kỹ thuật kiểm soát truy cập)**, đừng bắt đầu lại từ số không. **MAC 보안 모델 (Các mô hình bảo mật của MAC)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **MAC 보안 모델 (Các mô hình bảo mật của MAC)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### MAC 보안 모델 (Các mô hình bảo mật của MAC)

Bây giờ ta đi vào nội dung của **MAC 보안 모델 (Các mô hình bảo mật của MAC)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **벨-라파듈라 (Bell-LaPadula):** Tập trung vào **기밀성 (Tính Bảo mật / Kín đáo)** (Quân đội). Không đọc lên trên, Không ghi xuống dưới.
- **비바 (Biba):** Tập trung vào **무결성 (Tính Toàn vẹn)**. Ngăn chặn việc sửa đổi trái phép.
- **클락-윌슨 (Clark-Wilson):** Dành cho thương mại, chỉ cho phép sửa qua phần mềm được ủy quyền.
- **만리장성 (Chinese Wall):** Tránh xung đột lợi ích (người xem hồ sơ công ty A thì không được xem của đối thủ B).

---

Các bullet của **MAC 보안 모델 (Các mô hình bảo mật của MAC)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **MAC 보안 모델 (Các mô hình bảo mật của MAC)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **106-107. 튜플(Tuple)과 속성(Attribute)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.