# 9. 암호화 기술 (Công nghệ Mã hóa)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **9. 암호화 기술 (Công nghệ Mã hóa)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **9. 암호화 기술 (Công nghệ Mã hóa)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **암호화 기법 (Encryption Techniques)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

암호화, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**에서 만든 기준을 이어받아 **9. 암호화 기술 (Công nghệ Mã hóa)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **9. 암호화 기술 (Công nghệ Mã hóa)** và nối nó với **암호화 기법 (Encryption Techniques)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 9. 암호화 기술 (Công nghệ Mã hóa)

Ở bước 34/86, **9. 암호화 기술 (Công nghệ Mã hóa)** xuất hiện như phần tiếp nối của **4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **9. 암호화 기술 (Công nghệ Mã hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)

Bây giờ ta đi vào nội dung của **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **개인키(대칭키) 암호화 (Private/Symmetric Key):**
  - **동일한 키**로 암호화/복호화. 속도가 빠름. 암호화 키 개수: n(n-1)/2.
  - 종류:
    - **블록 암호화:** DES, SEED, AES, ARIA, IDEA
    - **스트림 암호화:** LFSR, RC4
- **공개키(비대칭키) 암호화 (Public/Asymmetric Key):**
  - 암호화(공개키), 복호화(비밀키/개인키). 키 개수: **2n**.
  - 대표 알고리즘: **RSA** (소인수분해 기반).
- **Tiếng Việt:**
  - Khóa cá nhân (Đối xứng): Cùng 1 khóa, nhanh. (DES, AES, ARIA).
  - Khóa công khai (Bất đối xứng): 2 khóa (Public để mã hóa, Private để giải mã), an toàn nhưng chậm. (RSA).

Các bullet của **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **9.2 해시 및 기타 암호화 요소** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **9.2 해시 및 기타 암호화 요소**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 9.2 해시 및 기타 암호화 요소

Phần nguồn của **9.2 해시 및 기타 암호화 요소** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “9.2 해시 및 기타 암호화 요소” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **해시 (Hash):** 임의의 길이를 고정된 길이로 변환. 복호화가 불가한 **일방향 함수**. (종류: SHA, MD4, MD5 등).
- **솔트 (Salt):** 암호화 전 원문에 무작위 값을 덧붙이는 과정. (패스워드 보안 강화용).
- **Tiếng Việt:** Hash là hàm một chiều không thể giải mã (SHA, MD5). Salt là thêm chuỗi ngẫu nhiên trước khi mã hóa để chống tấn công từ điển.

Các bullet của **9.2 해시 및 기타 암호화 요소** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **9.2 해시 및 기타 암호화 요소** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **9. 암호화 기술 (Công nghệ Mã hóa)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **암호화 기법 (Encryption Techniques)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.