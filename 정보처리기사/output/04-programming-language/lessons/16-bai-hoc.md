# 제어문 (Control Statements)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **제어문 (Control Statements)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **제어문 (Control Statements)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **제어문 심화 (Control Statements - Advanced)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

제어문

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**에서 만든 기준을 이어받아 **제어문 (Control Statements)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **제어문 (Control Statements)** và nối nó với **제어문 심화 (Control Statements - Advanced)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 제어문 (Control Statements)

Ở bước 16/78, **제어문 (Control Statements)** xuất hiện như phần tiếp nối của **246 - 249. 입출력 함수와 포맷 (I/O Functions & Formats)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **제어문 (Control Statements)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)

Bây giờ ta đi vào nội dung của **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 조건이 한 개일 때 사용하는 제어문이다. (Câu lệnh điều khiển khi chỉ có một điều kiện).
  - *Example / Ví dụ*: `if (a > b) printf("참"); else printf("거짓");`
  - 💡 *Mẹo ghi nhớ*: Nếu (if) đúng thì làm, nếu không (else) thì làm cái khác.

Các ý về **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **173. switch문 (switch statement / Câu lệnh switch)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **173. switch문 (switch statement / Câu lệnh switch)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 173. switch문 (switch statement / Câu lệnh switch)

Phần nguồn của **173. switch문 (switch statement / Câu lệnh switch)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 조건에 따라 분기할 곳이 여러 곳인 경우 간단하게 처리할 수 있다. (Sử dụng khi có nhiều nhánh rẽ).
- break문이 생략되면 모든 문장이 실행된다. (Nếu thiếu `break`, các câu lệnh bên dưới cũng sẽ được chạy theo hiệu ứng rơi xuyên).
  - *Example / Ví dụ*: `switch(a) { case 1: printf("A"); break; }`
  - 💡 *Mẹo ghi nhớ*: Đừng quên `break`, nếu không nó sẽ trôi xuống tận dưới cùng.

Các ý về **173. switch문 (switch statement / Câu lệnh switch)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Sau khi đọc **173. switch문 (switch statement / Câu lệnh switch)**, đừng bắt đầu lại từ số không. **174. for문 (for loop / Vòng lặp for)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **174. for문 (for loop / Vòng lặp for)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 174. for문 (for loop / Vòng lặp for)

Các ý ngay dưới **174. for문 (for loop / Vòng lặp for)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 초기값, 최종값, 증가값을 지정하여 정해진 횟수를 반복하는 제어문이다. (Vòng lặp với số lần xác định, bao gồm giá trị khởi tạo, điều kiện kết thúc và bước nhảy).
  - *Example / Ví dụ*: `for (i = 1; i <= 10 ; i++) sum = sum + i;`
  - 💡 *Mẹo ghi nhớ*: Dùng khi biết trước số lần lặp.

Với **174. for문 (for loop / Vòng lặp for)**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ.

**174. for문 (for loop / Vòng lặp for)** vừa cho ta cách đặt câu hỏi. Bây giờ **175. while문 (while loop / Vòng lặp while)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **175. while문 (while loop / Vòng lặp while)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 175. while문 (while loop / Vòng lặp while)

Bây giờ ta đi vào nội dung của **175. while문 (while loop / Vòng lặp while)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 조건이 참인 동안 실행할 문장을 반복 수행한다. (Lặp lại chừng nào điều kiện còn đúng).
  - *Example / Ví dụ*: `while (i <= 10) { i++; }`
  - 💡 *Mẹo ghi nhớ*: Kiểm tra điều kiện trước, làm sau. Có thể không chạy lần nào nếu điều kiện sai ngay từ đầu.

Các ý về **175. while문 (while loop / Vòng lặp while)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **175. while문 (while loop / Vòng lặp while)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **176. do~while문 (do~while loop / Vòng lặp do~while)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **176. do~while문 (do~while loop / Vòng lặp do~while)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 176. do~while문 (do~while loop / Vòng lặp do~while)

Phần nguồn của **176. do~while문 (do~while loop / Vòng lặp do~while)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- 무조건 한 번 실행한 다음 조건을 판단하여 탈출 여부를 결정한다. (Thực hiện ít nhất một lần, sau đó mới kiểm tra điều kiện).
  - *Example / Ví dụ*: `do { i++; } while (i <= 10);`
  - 💡 *Mẹo ghi nhớ*: Làm (do) trước, hỏi (while) sau. Chắc chắn chạy ít nhất 1 lần.

Các ý về **176. do~while문 (do~while loop / Vòng lặp do~while)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Điểm chốt của **176. do~while문 (do~while loop / Vòng lặp do~while)** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.

Như vậy, **제어문 (Control Statements)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **제어문 심화 (Control Statements - Advanced)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.