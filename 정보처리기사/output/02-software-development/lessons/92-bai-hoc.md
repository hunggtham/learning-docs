# 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối reuse techniques với component, inheritance, library và trade-off, để tái sử dụng không che giấu coupling.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **088-2: 데이터베이스 (Database) & 089: DBMS** khi chuyển sang phần tiếp theo.

Mục tiêu vừa đặt reuse vào bài toán tiết kiệm công sức mà vẫn kiểm soát chất lượng. Phần **핵심 키워드 (Từ khóa)** sau đây giữ lại các thuật ngữ để nhận diện phần mềm có thể dùng lại và cách biến đổi nó.

## 핵심 키워드 (Từ khóa)

핵심, 재사용, 기법

Các từ khóa chỉ ra rằng reuse không đồng nghĩa với sao chép nguyên trạng: phải xét cấu trúc, chức năng và chi phí điều chỉnh. Phần **선행·연결 개념 (Kiến thức liên kết)** sẽ nối tiêu chí đó với cách thiết kế thuật toán ở bài trước.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**에서 만든 기준을 이어받아 **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Sau khi thấy reuse kế thừa tiêu chí về hiệu quả và chi phí, **읽는 방법 (Cách đọc)** sẽ hướng dẫn phân biệt phần được tái sử dụng, điều kiện chỉnh sửa và hệ quả đối với coupling, trước khi đọc các ý nguồn.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Với cách đọc vừa xác lập, phần **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** giải thích reuse bằng lợi ích và điều kiện kiểm soát, rồi bàn giao sang database/DBMS nơi các thành phần và quy tắc tiếp tục được tổ chức.

## 핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)

Sau khi đã đặt nền bằng **027: 알고리즘 설계 기법과 시간 복잡도 (Algorithm Design & Time Complexity)**, ta chuyển sang **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**. Đây là mắt xích 92/101 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **재사용 (Reuse):** 이미 개발되어 인정받았던 소프트웨어의 전체 또는 일부분을 다시 사용하는 기법. (Sử dụng lại code/phần mềm cũ đã được kiểm chứng để tiết kiệm thời gian, chi phí và giảm lỗi.)
- **Phân loại theo kỹ thuật:**
  - **분석 (Analysis):** Hiểu code cũ để chọn cái cần tái sử dụng.
  - **재구조 (Restructuring):** Đổi cấu trúc, không đổi chức năng.

---

Ta có thể khép mục **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **088-2: 데이터베이스 (Database) & 089: DBMS**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **핵심 034: 재사용 기법 (Reuse Techniques / Kỹ thuật tái sử dụng)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
