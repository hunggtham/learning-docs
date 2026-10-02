# 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối storage với distributed database, để cân bằng durability, locality, replication và chi phí truy cập trong hệ thống phân tán.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

스토리지와, 분산, 데이터베이스

> **Chuyển mạch:** Ở chặng này của **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**에서 만든 기준을 이어받아 **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)

Ở bước 37/54, **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** xuất hiện như phần tiếp nối của **197. 분산 데이터베이스의 장단점 (Distributed DB Pros/Cons)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **스토리지 (Storage - Thiết bị lưu trữ)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **스토리지 (Storage - Thiết bị lưu trữ)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 스토리지 (Storage - Thiết bị lưu trữ)

Bây giờ ta đi vào nội dung của **스토리지 (Storage - Thiết bị lưu trữ)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “스토리지 (Storage - Thiết bị lưu trữ)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **DAS (Direct Attached Storage):** Kết nối trực tiếp bằng cáp. Nhanh, an toàn nhưng khó mở rộng.
- **NAS (Network Attached Storage):** Kết nối qua mạng (Network-based, File-level). Mềm dẻo nhưng có thể nghẽn mạng.
- **SAN (Storage Area Network):** Dùng cáp quang (Fiber Channel), tốc độ cực cao, đắt tiền.
- **SDS (Software-defined Storage):** Quản lý toàn bộ tài nguyên lưu trữ bằng phần mềm (Ảo hóa lưu trữ).

Các bullet của **스토리지 (Storage - Thiết bị lưu trữ)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **스토리지 (Storage - Thiết bị lưu trữ)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **분산 데이터베이스 (Distributed Database - CSDL Phân tán)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 분산 데이터베이스 (Distributed Database - CSDL Phân tán)

Phần nguồn của **분산 데이터베이스 (Distributed Database - CSDL Phân tán)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

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

Như vậy, **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **18. 파티셔닝과 암호화 (Phân vùng và Mã hóa)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **17. 스토리지와 분산 데이터베이스 (Lưu trữ và CSDL Phân tán)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
