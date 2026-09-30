# 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

집합연산자, 조인

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**에서 만든 기준을 이어받아 **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** và nối nó với **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)

Từ **6. DDL, DML, DCL 상세 (Chi tiết DDL, DML, DCL)**, ta đã có điểm tựa để bước vào **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 51/54 trước khi đi vào chi tiết.

Để đọc **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu. Trong khối này, **INNER JOIN**, **OUTER JOIN (LEFT, RIGHT, FULL)**, **SELF JOIN**, **CROSS JOIN** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **집합 연산자 (Toán tử tập hợp)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 집합 연산자 (Toán tử tập hợp)

Các ý ngay dưới **집합 연산자 (Toán tử tập hợp)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

Phần “집합 연산자 (Toán tử tập hợp)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- `UNION`: Hợp (Loại bỏ trùng lặp).
- `UNION ALL`: Hợp tất cả (Giữ nguyên trùng lặp).
- `INTERSECT`: Giao (Chỉ lấy phần chung).
- `MINUS` / `EXCEPT`: Hiệu (Lấy bảng 1 trừ đi các dòng có trong bảng 2).

Các bullet của **집합 연산자 (Toán tử tập hợp)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **집합 연산자 (Toán tử tập hợp)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **조인 (JOIN)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **조인 (JOIN)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 조인 (JOIN)

Bây giờ ta đi vào nội dung của **조인 (JOIN)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

Phần “조인 (JOIN)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **INNER JOIN**: Lấy các dòng có dữ liệu khớp nhau (Giao). `SELECT * FROM A INNER JOIN B ON A.id = B.id;`
- **OUTER JOIN (LEFT, RIGHT, FULL)**: Lấy cả dữ liệu không khớp. Bên thiếu dữ liệu sẽ điền NULL.
  - Cú pháp Oracle (+): `WHERE A.id = B.id(+)` (Đây là LEFT OUTER JOIN vì dấu (+) nằm ở bảng B, tức là bảng B thiếu cũng không sao).
- **SELF JOIN**: Bảng tự JOIN với chính nó. (Dùng `AS` để tạo bí danh).
- **CROSS JOIN**: Tích Đề-các (Cartesian product), bắt cặp tất cả các dòng của 2 bảng.

---

Với **조인 (JOIN)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

Điểm chốt của **조인 (JOIN)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Điểm chốt của **7. 집합연산자 및 조인 (Toán tử tập hợp và JOIN)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **15. 관계 데이터 언어 (Ngôn ngữ Dữ liệu Quan hệ - Đại số quan hệ)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.