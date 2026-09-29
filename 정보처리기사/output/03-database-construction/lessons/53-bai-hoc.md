# 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **22. 기타 주요 개념 (Các khái niệm quan trọng khác)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

데이터, 전환, 정제

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**에서 만든 기준을 이어받아 **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** và nối nó với **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)

Sau khi đã đặt nền bằng **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**, ta chuyển sang **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)**. Đây là mắt xích 53/54 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **데이터 전환 (Data Migration - Di chuyển dữ liệu)**. Hãy xác định **데이터 전환 (Data Migration - Di chuyển dữ liệu)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 데이터 전환 (Data Migration - Di chuyển dữ liệu)

Phần nguồn của **데이터 전환 (Data Migration - Di chuyển dữ liệu)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

Là quá trình chuyển dữ liệu từ hệ thống cũ sang hệ thống mới.
- **ETL 3 bước:**
  1. **E**xtraction (추출): Trích xuất từ nguồn.
  2. **T**ransformation (변환): Biến đổi cho phù hợp chuẩn mới.
  3. **L**oad (적재): Nạp vào hệ thống đích.

Các bullet của **데이터 전환 (Data Migration - Di chuyển dữ liệu)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **데이터 전환 (Data Migration - Di chuyển dữ liệu)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **오류 데이터 정제 (Error Data Cleansing)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **오류 데이터 정제 (Error Data Cleansing)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 오류 데이터 정제 (Error Data Cleansing)

Các ý ngay dưới **오류 데이터 정제 (Error Data Cleansing)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Quản lý trạng thái lỗi trong quá trình chuyển đổi:
- **Open (Mở):** Phát hiện lỗi, chưa phân tích.
- **Assigned (Đã giao):** Giao cho lập trình viên sửa.
- **Fixed (Đã sửa):** Đã sửa xong.
- **Closed (Đóng):** Đã test lại và xác nhận bình thường.
- **Deferred (Trì hoãn):** Quyết định chưa sửa lúc này (hoặc không phải lỗi).

---

Các bullet của **오류 데이터 정제 (Error Data Cleansing)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Điểm chốt của **오류 데이터 정제 (Error Data Cleansing)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Ta có thể khép mục **21. 데이터 전환 및 정제 (Chuyển đổi dữ liệu - ETL)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **22. 기타 주요 개념 (Các khái niệm quan trọng khác)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.