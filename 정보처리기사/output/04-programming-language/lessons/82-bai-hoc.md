# 254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

반복문과, 제어, 키워드

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **253. switch문 (switch Statement)**에서 만든 기준을 이어받아 **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

> **Bàn giao:** Sau khi đọc, hãy tự nói lại điểm phân biệt quan trọng nhất của **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** và nối nó với **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)**; nếu không làm được, quay lại ví dụ thay vì học thuộc riêng định nghĩa.

---

## 254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)

Ở bước 82/91, **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** xuất hiện như phần tiếp nối của **253. switch문 (switch Statement)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **for문**, **while문**, **do~while문**, **break** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **for문**: 횟수가 정해진 반복(초기화, 조건검사, 증감식). 배열 순회에 주로 사용.
- **while문**: 조건이 참인 동안 반복(선행 판단). 조건이 항상 참이면 무한 루프 발생.
- **do~while문**: **최소 1번은 무조건 실행**한 후 조건을 검사(후행 판단).
- **break**: 현재 실행 중인 루프(블록)를 즉시 완전히 빠져나감.
- **continue**: 루프를 완전히 빠져나가지 않고, **다음 반복 회차로 건너뜀**.

**Giải thích (Vietnamese):**
- `for`: Biết trước số lần lặp (VD: đếm từ 1 đến 10).
- `while`: Lặp cho đến khi điều kiện sai (VD: lặp tới khi game over).
- `break`: Dừng cuộc chơi ngay lập tức, thoát ra ngoài.
- `continue`: Bỏ qua vòng lặp hiện tại, đi tới vòng lặp tiếp theo (VD: đếm từ 1 đến 10, nếu gặp số 5 thì `continue` -> in ra 1 2 3 4 6 7 8 9 10).

---

Như vậy, **254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **275 - 278. 프로그래밍 언어의 종류 (Types of Programming Languages)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.