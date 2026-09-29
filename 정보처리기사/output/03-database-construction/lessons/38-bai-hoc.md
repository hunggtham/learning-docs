# 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **201-203. 스토리지 시스템 (Storage Systems)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

스토리지와, 분산, 데이터베이스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**에서 만든 기준을 이어받아 **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** và nối nó với **201-203. 스토리지 시스템 (Storage Systems)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

Sau khi đã đặt nền bằng **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**, ta chuyển sang **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**. Đây là mắt xích 38/56 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **스토리지 (Storage - Thiết bị lưu trữ)**. Hãy xác định **스토리지 (Storage - Thiết bị lưu trữ)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 스토리지 (Storage - Thiết bị lưu trữ)

Phần nguồn của **스토리지 (Storage - Thiết bị lưu trữ)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **DAS (Direct Attached Storage):** Kết nối trực tiếp bằng cáp. Nhanh, an toàn nhưng khó mở rộng.
- **NAS (Network Attached Storage):** Kết nối qua mạng (Network-based, File-level). Mềm dẻo nhưng có thể nghẽn mạng.
- **SAN (Storage Area Network):** Dùng cáp quang (Fiber Channel), tốc độ cực cao, đắt tiền.
- **SDS (Software-defined Storage):** Quản lý toàn bộ tài nguyên lưu trữ bằng phần mềm (Ảo hóa lưu trữ).

Các bullet của **스토리지 (Storage - Thiết bị lưu trữ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **스토리지 (Storage - Thiết bị lưu trữ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 분산 데이터베이스 (Distributed Database - CSDL Phân tán)

Các ý ngay dưới **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Dữ liệu phân bố ở nhiều nơi (máy chủ khác nhau) nhưng người dùng cảm giác như đang dùng 1 CSDL duy nhất.
- **장점 (Ưu điểm):** Đáng tin cậy, dễ mở rộng, tính tự trị khu vực cao.
- **단점 (Nhược điểm):** Thiết kế khó, chi phí cao, bảo mật phức tạp.

**4대 투명성 (4 Đặc tính Trong suốt - Transparency):**
1. **위치 투명성 (Location):** Người dùng không cần biết dữ liệu nằm ở máy chủ nào.
2. **중복(복제) 투명성 (Replication):** Không cần biết dữ liệu được nhân bản ra sao.
3. **병행 투명성 (Concurrency):** Nhiều người truy cập cùng lúc vẫn không bị lỗi kết quả.
4. **장애 투명성 (Failure):** Một Node chết, toàn hệ thống vẫn hoạt động bình thường.

---

Các bullet của **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **201-203. 스토리지 시스템 (Storage Systems)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.