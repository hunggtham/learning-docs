# 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

파티셔닝과, 암호화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**에서 만든 기준을 이어받아 **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** và nối nó với **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)

Sau khi đã đặt nền bằng **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, ta chuyển sang **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**. Đây là mắt xích 38/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **파티셔닝 (Partitioning)**. Hãy xác định **파티셔닝 (Partitioning)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 파티셔닝 (Partitioning)

Phần nguồn của **파티셔닝 (Partitioning)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Chia các bảng lớn thành các phần nhỏ (Partition) để dễ quản lý và tăng hiệu suất.
- **범위 분할 (Range):** Phân chia theo khoảng (VD: Tháng 1, Tháng 2).
- **해시 분할 (Hash):** Dùng hàm băm để chia đều. Dữ liệu phân bố đều nhưng khó tìm theo khoảng.
- **목록 분할 (List):** Phân chia theo danh sách giá trị (VD: Nước: VN, KR, US).
- **조합 분할 (Composite):** Kết hợp các phương pháp trên.
- **라운드 로빈 (Round Robin):** Chia xoay vòng đều nhau tuần tự (Không cần khóa).

Các bullet của **파티셔닝 (Partitioning)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **파티셔닝 (Partitioning)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **데이터베이스 암호화 (Mã hóa CSDL)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **데이터베이스 암호화 (Mã hóa CSDL)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 데이터베이스 암호화 (Mã hóa CSDL)

Các ý ngay dưới **데이터베이스 암호화 (Mã hóa CSDL)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “데이터베이스 암호화 (Mã hóa CSDL)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **암호화 (Encryption):** Biến 평문 (Plaintext - Văn bản gốc) thành 암호문 (Ciphertext - Bản mã).
- **복호화 (Decryption):** Giải mã từ Ciphertext về Plaintext.
- **키 (Key):** Chìa khóa dùng để mã hóa và giải mã.
---

Các bullet của **데이터베이스 암호화 (Mã hóa CSDL)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **데이터베이스 암호화 (Mã hóa CSDL)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.