# 제어문 (Control Statements)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **제어문 (Control Statements)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

제어문

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 제어문 (Control Statements)
### 172. 단순 if문 (Simple if statement / Câu lệnh if đơn giản)
- 조건이 한 개일 때 사용하는 제어문이다. (Câu lệnh điều khiển khi chỉ có một điều kiện).
  - *Example / Ví dụ*: `if (a > b) printf("참"); else printf("거짓");`
  - 💡 *Mẹo ghi nhớ*: Nếu (if) đúng thì làm, nếu không (else) thì làm cái khác.

### 173. switch문 (switch statement / Câu lệnh switch)
- 조건에 따라 분기할 곳이 여러 곳인 경우 간단하게 처리할 수 있다. (Sử dụng khi có nhiều nhánh rẽ).
- break문이 생략되면 모든 문장이 실행된다. (Nếu thiếu `break`, các câu lệnh bên dưới cũng sẽ được chạy theo hiệu ứng rơi xuyên).
  - *Example / Ví dụ*: `switch(a) { case 1: printf("A"); break; }`
  - 💡 *Mẹo ghi nhớ*: Đừng quên `break`, nếu không nó sẽ trôi xuống tận dưới cùng.

### 174. for문 (for loop / Vòng lặp for)
- 초기값, 최종값, 증가값을 지정하여 정해진 횟수를 반복하는 제어문이다. (Vòng lặp với số lần xác định, bao gồm giá trị khởi tạo, điều kiện kết thúc và bước nhảy).
  - *Example / Ví dụ*: `for (i = 1; i <= 10 ; i++) sum = sum + i;`
  - 💡 *Mẹo ghi nhớ*: Dùng khi biết trước số lần lặp.

### 175. while문 (while loop / Vòng lặp while)
- 조건이 참인 동안 실행할 문장을 반복 수행한다. (Lặp lại chừng nào điều kiện còn đúng).
  - *Example / Ví dụ*: `while (i <= 10) { i++; }`
  - 💡 *Mẹo ghi nhớ*: Kiểm tra điều kiện trước, làm sau. Có thể không chạy lần nào nếu điều kiện sai ngay từ đầu.

### 176. do~while문 (do~while loop / Vòng lặp do~while)
- 무조건 한 번 실행한 다음 조건을 판단하여 탈출 여부를 결정한다. (Thực hiện ít nhất một lần, sau đó mới kiểm tra điều kiện).
  - *Example / Ví dụ*: `do { i++; } while (i <= 10);`
  - 💡 *Mẹo ghi nhớ*: Làm (do) trước, hỏi (while) sau. Chắc chắn chạy ít nhất 1 lần.
