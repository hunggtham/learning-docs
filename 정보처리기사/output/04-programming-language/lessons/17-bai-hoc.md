# 제어문 심화 (Control Statements - Advanced)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **제어문 심화 (Control Statements - Advanced)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

제어문, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 제어문 심화 (Control Statements - Advanced)
### 252. 다중 if문 (Multi if statement / Câu lệnh if nhiều nhánh)
- 조건이 여러 개일 때 사용하는 제어문이다. (Sử dụng khi có nhiều điều kiện khác nhau).
- `if (조건1) ... else if (조건2) ... else ...`
  - *Example / Ví dụ*: `if(jum >= 90) printf("A"); else if(jum >= 80) printf("B"); else printf("F");`
  - 💡 *Mẹo ghi nhớ*: Xếp hạng hoặc các điều kiện loại trừ lẫn nhau thì dùng `else if`.

### 253. switch문 (switch statement / Câu lệnh switch - Bổ sung)
- `case`문의 레이블에는 상수만 지정할 수 있으며 변수는 지정할 수 없다. (Nhãn `case` chỉ chấp nhận hằng số, không dùng biến).
- `int`, `char`, `enum`형의 상수만 가능하다. (Chỉ dùng được số nguyên, ký tự, hoặc kiểu enum).
  - *Example / Ví dụ*: `switch (jum / 10) { case 10: case 9: printf("A"); break; ... }` (Chia cho 10 để tính điểm thập phân thành số nguyên).
  - 💡 *Mẹo ghi nhớ*: `switch` thích sự chính xác tuyệt đối (giá trị cụ thể), không thích sự so sánh lớn/nhỏ.

### 254. for문 (for loop / Vòng lặp for - Bổ sung)
- 처음부터 조건식을 만족하지 못하면 한 번도 수행하지 않는다. (Nếu điều kiện sai ngay từ đầu, vòng lặp không chạy lần nào).
- `for(초기값; 최종값조건; 증가값) { 실행문; }`

### 255. while문 (while loop / Vòng lặp while - Bổ sung)
- `while(조건) { 실행문; }`
- Điều kiện được kiểm tra trước, nếu sai từ đầu sẽ bỏ qua.
  - *Example / Ví dụ*: `while(a < 5) { a++; hap += a; }`

### 256. do~while문 (do~while loop / Vòng lặp do~while - Bổ sung)
- 실행할 문장을 무조건 한 번 실행한 다음 조건을 판단. (Thực hiện ít nhất 1 lần rồi mới kiểm tra điều kiện ở cuối).
- `do { 실행문; } while(조건);` (Nhớ có dấu chấm phẩy ở cuối `while`).

### 257. break, continue (Keywords / Từ khóa điều khiển vòng lặp)
- **break**: switch문이나 반복문 안에서 나오면 블록을 벗어난다. (Thoát ngay lập tức khỏi vòng lặp hoặc switch).
- **continue**: 이후의 문장을 실행하지 않고 반복문의 처음으로 옮긴다. (Bỏ qua các lệnh bên dưới và quay lại đầu vòng lặp để tiếp tục vòng lặp mới).
  - *Example / Ví dụ*: `if(a % 2 == 0) continue; hap += a;` (Bỏ qua số chẵn, chỉ cộng số lẻ).
  - 💡 *Mẹo ghi nhớ*: `break` = Phá vỡ (thoát ra). `continue` = Tiếp tục (bước tiếp).
