# 암호화 기법 (Encryption Techniques)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **암호화 기법 (Encryption Techniques)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **암호화 기법 (Encryption Techniques)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 암호화 기본 개념 (Concepts)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

암호화, 기법

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **9. 암호화 기술 (Công nghệ Mã hóa)**에서 만든 기준을 이어받아 **암호화 기법 (Encryption Techniques)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **암호화 기법 (Encryption Techniques)** và nối nó với **1. 암호화 기본 개념 (Concepts)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 암호화 기법 (Encryption Techniques)

Sau khi đã đặt nền bằng **9. 암호화 기술 (Công nghệ Mã hóa)**, ta chuyển sang **암호화 기법 (Encryption Techniques)**. Đây là mắt xích 35/86 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **암호화 기법 (Encryption Techniques)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **종류**, **종류**, **해시 (Hash)**, **솔트 (Salt)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)**. Hãy xác định **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)

Phần nguồn của **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Phần “1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 암호화와 복호화에 **동일한 키(비밀키)**를 사용합니다.
- 장점: 속도가 빠름 / 단점: 키 분배가 어렵고 키 개수가 많아짐.
- 필요한 키의 개수: `n(n-1) / 2`
- **종류**: DES, 3DES, AES, SEED(국내), ARIA(국내).

Các bullet của **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **1. 개인키 (대칭키) 암호화 (Private Key / Symmetric Key)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)

Các ý ngay dưới **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 암호화할 때는 공개키(Public Key), 복호화할 때는 비밀키(Private Key)를 사용합니다.
- 장점: 키 분배 용이, 키 개수 적음 / 단점: 암복호화 속도가 느림.
- 필요한 키의 개수: `2n`
- **종류**: RSA.

Các bullet của **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **2. 공개키 (비대칭키) 암호화 (Public Key / Asymmetric Key)**, đừng bắt đầu lại từ số không. **3. 해시(Hash)와 솔트(Salt)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **3. 해시(Hash)와 솔트(Salt)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 3. 해시(Hash)와 솔트(Salt)

Bây giờ ta đi vào nội dung của **3. 해시(Hash)와 솔트(Salt)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “3. 해시(Hash)와 솔트(Salt)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **해시 (Hash)**: 임의의 길이 데이터를 고정된 길이의 값으로 변환하는 일방향 함수다. 무결성 검증에 사용하며, 패스워드는 전용 password hashing/KDF와 salt를 사용해야 한다. 해시는 암호화처럼 복호화하지 않는다 (예: SHA-256, MD5).
- **솔트 (Salt)**: 암호화 전 원문에 덧붙이는 무작위 값. 동일한 패스워드라도 솔트가 다르면 해시값이 달라져 레인보우 테이블 공격을 방어합니다.

> **Vietnamese Explanation**:
> **Mã hóa đối xứng (Private Key)**: Dùng chung 1 chìa khóa để khóa và mở (nhanh nhưng khó chia sẻ chìa khóa an toàn).
> **Mã hóa bất đối xứng (Public Key)**: Dùng khóa công khai để khóa, khóa bí mật để mở (chậm hơn nhưng an toàn).
> **Hash (Băm)** là mã hóa 1 chiều (không dịch ngược được). **Salt (Muối)** là thêm chuỗi ngẫu nhiên vào mật khẩu trước khi băm để tăng độ khó.

Các bullet của **3. 해시(Hash)와 솔트(Salt)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **3. 해시(Hash)와 솔트(Salt)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **암호화 기법 (Encryption Techniques)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **1. 암호화 기본 개념 (Concepts)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.