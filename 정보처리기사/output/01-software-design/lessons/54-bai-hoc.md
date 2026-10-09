# 11. 수식의 표기법 (Expression Notation)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **11. 수식의 표기법 (Expression Notation)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối expression notation với infix, prefix, postfix và evaluation stack, để biểu thức chuyển thành thứ tự thực thi.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **11. 수식의 표기법 (Expression Notation)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **11. 수식의 표기법 (Expression Notation)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)** khi chuyển sang phần tiếp theo.

Mục tiêu xác định infix, prefix, postfix và evaluation stack biến biểu thức thành thứ tự thực thi ra sao; từ khóa khoanh vùng các dạng biểu diễn.

## 핵심 키워드 (Từ khóa)

수식의, 표기법

Kiến thức liên kết đặt expression notation trên nền traversal và stack; cách đọc tiếp theo giúp tách cú pháp khỏi thứ tự đánh giá.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **10. 이진 트리의 운행법 (Binary Tree Traversal)**에서 만든 기준을 이어받아 **11. 수식의 표기법 (Expression Notation)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

Cách đọc đã đặt khung đối tượng–điều kiện–hệ quả; phần expression notation dùng khung đó để nối biểu diễn với evaluation.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

Phần này khép lại bằng quy tắc ưu tiên và stack evaluation; khi sang sorting/searching, hãy giữ lại cách biểu diễn dependency.

## 11. 수식의 표기법 (Expression Notation)

Từ **10. 이진 트리의 운행법 (Binary Tree Traversal)**, ta đã có điểm tựa để bước vào **11. 수식의 표기법 (Expression Notation)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 54/69 trước khi đi vào chi tiết.

Để đọc **11. 수식의 표기법 (Expression Notation)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “11. 수식의 표기법 (Expression Notation)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- Prefix, Infix, Postfix.
- Chuyển đổi qua lại (Infix -> Postfix/Prefix) bằng cách đóng ngoặc và di chuyển toán tử.

Điểm chốt của **11. 수식의 표기법 (Expression Notation)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **12. 외부 정렬 및 정렬 알고리즘 (External Sort & Sorting Algorithms)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **11. 수식의 표기법 (Expression Notation)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
