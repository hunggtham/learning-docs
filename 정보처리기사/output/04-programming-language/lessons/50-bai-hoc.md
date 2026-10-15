# 252. 다중 if문 (Multiple if Statement)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp và nguyên lý điều khiển luồng thực thi của câu lệnh rẽ nhánh đa tầng (다중 if문 - Multiple `if - else if - else` Statements) trong các ngôn ngữ lập trình C, Java, và Python (`elif`).
- Hiểu tính chất loại trừ lẫn nhau (Mutual Exclusivity): Các điều kiện được thẩm định tuần tự từ trên xuống dưới; ngay khi gặp điều kiện đầu tiên thỏa mãn Đúng (True), khối lệnh tương ứng sẽ được thực thi và chương trình **thoát ngay lập tức khỏi toàn bộ chuỗi `if`**, bỏ qua tất cả các nhánh bên dưới.
- Rèn luyện kỹ năng sắp xếp thứ tự các điều kiện logic để tránh bẫy mã nguồn chết (Dead Code) hoặc che khuất điều kiện (Condition Shadowing).

## 핵심 키워드 (Từ khóa)
- 다중 if문 (Multiple if-else if Statements)
- 순차적 조건 평가 (Sequential Evaluation)
- 상호 배타적 실행 (Mutually Exclusive Execution)
- else if문 vs elif문 (C/Java vs Python)
- 디폴트 else절 (Default Fallback else)
- 조건문 그림자 현상 (Condition Shadowing / Dead Code)

## 선행·연결 개념 (Kiến thức liên kết)
- [49-bai-hoc.md](49-bai-hoc.md): Địa chỉ IP, Subnetting và so sánh IPv4 vs IPv6.
- [51-bai-hoc.md](51-bai-hoc.md): Vòng lặp `for` nâng cao và các mẫu thuật toán lặp.
- [17-bai-hoc.md](17-bai-hoc.md): Căn bản về câu lệnh điều khiển rẽ nhánh `if` và `switch-case`.

## 읽는 방법 (Cách đọc)
- Phân biệt cấu trúc đa nhánh qua cơ chế thực thi:
  - Khi có $N$ điều kiện liên tiếp `if (...) ... else if (...) ... else`:
    - Chỉ có **tối đa duy nhất 1 khối lệnh** được thực thi.
    - Điều kiện nào viết ở trên sẽ được kiểm tra trước. Do đó, **các điều kiện cụ thể hoặc có phạm vi hẹp hơn phải được đặt ở trên**, các điều kiện rộng hơn phải đặt ở dưới.
    - Nếu viết điều kiện rộng ở trên (ví dụ: `if (score >= 60)`), thì điều kiện hẹp hơn ở dưới (`else if (score >= 90)`) sẽ vĩnh viễn không bao giờ được chạm tới (Code chết).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Cấu trúc cú pháp đa nhánh trên các ngôn ngữ:**

| Ngôn ngữ | Cú pháp chuẩn | Ký hiệu phân cách khối |
| :--- | :--- | :--- |
| **C / C++** | `if (조건1) { ... } else if (조건2) { ... } else { ... }` | Dấu ngoặc nhọn `{ }` |
| **Java** | `if (조건1) { ... } else if (조건2) { ... } else { ... }` | Dấu ngoặc nhọn `{ }` |
| **Python** | `if 조건1 : ... elif 조건2 : ... else : ...` | **Dấu hai chấm `:` và thụt lề Indentation** |

- **Bẫy thứ tự thẩm định điều kiện (Condition Shadowing):**
  - *Ví dụ đoạn mã bị lỗi logic:*
    ```c
    int score = 95;
    char grade;
    if (score >= 60) {
        grade = 'D';
    } else if (score >= 70) {
        grade = 'C';
    } else if (score >= 80) {
        grade = 'B';
    } else if (score >= 90) {
        grade = 'A'; // Không bao giờ chạm tới được!
    }
    ```
  - *Phân tích lỗi:* Vì $95 \ge 60$ là Đúng ngay ở câu `if` đầu tiên, biến `grade` bị gán thành `'D'` và thoát luôn khỏi chuỗi `if`. Toàn bộ các nhánh điểm cao phía dưới bị bỏ qua hoàn toàn.
  - *Cách sửa đúng:* Đảo ngược thứ tự từ cao xuống thấp: Kiểm tra $\ge 90$ trước, rồi đến $\ge 80$, $\ge 70$, $\ge 60$.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh `if - else if` với Chuỗi nhiều câu lệnh `if` độc lập:**
  - *Chuỗi `if` độc lập:*
    ```c
    if (x > 0) a = 1;
    if (x > 5) a = 2;
    ```
    $\rightarrow$ Cả 2 câu `if` đều được kiểm tra độc lập. Nếu $x = 10$, câu 1 chạy gán $a = 1$, sau đó câu 2 chạy gán đè $a = 2$.
  - *Chuỗi `if - else if`:*
    ```c
    if (x > 0) a = 1;
    else if (x > 5) a = 2;
    ```
    $\rightarrow$ Nếu $x = 10$, câu 1 đúng gán $a = 1$ và dừng ngay, câu 2 bị bỏ qua hoàn toàn $\rightarrow$ Giá trị cuối cùng của $a$ là 1.

### 복습 체크리스트
- [ ] Nhớ trong chuỗi `if - else if`, chỉ có duy nhất 1 khối lệnh được thực thi.
- [ ] Nhớ trong Python từ khóa là `elif`, không phải `else if`.
- [ ] Biết cách sắp xếp thứ tự điều kiện từ hẹp đến rộng (hoặc từ cao xuống thấp) để tránh Code chết.
- [ ] Phân biệt được chuỗi `if - else if` (loại trừ lẫn nhau) và nhiều câu `if` độc lập (chạy lần lượt).
