# 9. 암호화 기술 (Công nghệ Mã hóa)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **9. 암호화 기술 (Công nghệ Mã hóa)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **9. 암호화 기술 (Công nghệ Mã hóa)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

암호화, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**에서 만든 기준을 이어받아 **9. 암호화 기술 (Công nghệ Mã hóa)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 9. 암호화 기술 (Công nghệ Mã hóa)

Từ **10. 해킹 및 보안 위협 (Các hình thức tấn công & Đe dọa bảo mật)**, ta đã có điểm tựa để bước vào **9. 암호화 기술 (Công nghệ Mã hóa)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 15/18 trước khi đi vào chi tiết.

Để đọc **9. 암호화 기술 (Công nghệ Mã hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)

Các ý ngay dưới **9.1 개인키 vs 공개키 암호화 (대칭키 vs 비대칭키)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

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
Ở đoạn **9.2 해시 및 기타 암호화 요소**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 9.2 해시 및 기타 암호화 요소

Bây giờ ta đi vào nội dung của **9.2 해시 및 기타 암호화 요소**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **해시 (Hash):** 임의의 길이를 고정된 길이로 변환. 복호화가 불가한 **일방향 함수**. (종류: SHA, MD4, MD5 등).
- **솔트 (Salt):** 암호화 전 원문에 무작위 값을 덧붙이는 과정. (패스워드 보안 강화용).
- **Tiếng Việt:** Hash là hàm một chiều không thể giải mã (SHA, MD5). Salt là thêm chuỗi ngẫu nhiên trước khi mã hóa để chống tấn công từ điển.

Các bullet của **9.2 해시 및 기타 암호화 요소** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **9.2 해시 및 기타 암호화 요소** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **9. 암호화 기술 (Công nghệ Mã hóa)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 소프트웨어 공학 기법 (Kỹ thuật Công nghệ Phần mềm)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.