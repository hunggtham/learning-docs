# 수식 표기법과 스택 활용 (Ký pháp biểu thức và ứng dụng ngăn xếp)

## 학습 목표
- Nắm vững 3 dạng ký pháp toán học: Trung tố (`중위 표기법 / Infix`), Tiền tố (`전위 표기법 / Prefix`), Hậu tố (`후위 표기법 / Postfix`), và lý do trình biên dịch ưu tiên dùng Postfix.
- Làm chủ quy trình 3 bước chuyển đổi chuẩn tắc từ biểu thức Infix sang Postfix và Prefix (Đóng ngoặc theo độ ưu tiên $\rightarrow$ Dời toán tử $\rightarrow$ Xóa ngoặc).
- Mô phỏng chính xác giải thuật tính toán giá trị biểu thức Postfix sử dụng cấu trúc Ngăn xếp (Stack).
- Nhận diện chính xác bẫy thứ tự toán hạng trong phép trừ và phép chia ($A - B$ và $A / B$), tránh đảo ngược thứ tự khi `POP`.
- Ánh xạ 1-1 giữa các phép duyệt cây nhị phân với các dạng ký pháp: Preorder $\leftrightarrow$ Prefix, Inorder $\leftrightarrow$ Infix, Postorder $\leftrightarrow$ Postfix.

## 핵심 키워드
- 수식 표기법 (Ký pháp biểu thức / Expression Notation)
- 중위 표기법 (Trung tố / Infix)
- 전위 표기법 (Tiền tố / Prefix / Polish Notation)
- 후위 표기법 (Hậu tố / Postfix / Reverse Polish Notation)
- 스택 연산 (Thao tác ngăn xếp / Stack Evaluation / PUSH, POP)
- 연산자 우선순위 (Độ ưu tiên toán tử / Operator Precedence)
- 수식 이진 트리 (Cây biểu thức nhị phân / Binary Expression Tree)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [01-cau-truc-du-lieu-tuyen-tinh.md](01-cau-truc-du-lieu-tuyen-tinh.md), chúng ta đã làm chủ nguyên lý hoạt động vào sau ra trước (LIFO) của cấu trúc Ngăn xếp (Stack).
- **Đang giải quyết gì (Current Problem):** Con người quen đọc biểu thức trung tố có dấu ngoặc ($A + B \times C$), nhưng máy tính lại không thể quét tới quét lui để giải quyết độ ưu tiên. Bài học này giải quyết việc chuyển đổi biểu thức sang dạng Hậu tố (Postfix) và dùng Stack để tính toán giá trị biểu thức trong 1 lượt duyệt duy nhất.
- **Dùng đi đâu (Forward Handoff):** Mô hình cây biểu thức nhị phân mở ra cánh cửa bước sang cấu trúc phi tuyến với [03-cay-va-duyet-cay-nhi-phan.md](03-cay-va-duyet-cay-nhi-phan.md) để khảo sát các giải thuật duyệt cây nhị phân toàn diện.

## 읽는 방법
- Đọc TẦNG A để nắm vững thuật toán 3 bước chuyển đổi nhanh, bảng so sánh 3 dạng biểu thức và bảng bẫy đề thi kinh điển khi lấy toán tử trừ và chia trong Stack ($A - B$ chứ không phải $B - A$).
- Đọc TẦNG B để theo dõi chi tiết 2 bài tập ví dụ mẫu, bảng trace từng bước nạp Stack và mối liên kết trực quan với Cây biểu thức nhị phân.

---

## 수식 표기법과 스택 활용

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 3 dạng biểu diễn biểu thức toán học
| Ký pháp | Tên tiếng Hàn & Anh | Vị trí toán tử | Cú pháp mẫu | Ứng dụng & Ánh xạ duyệt cây |
| :--- | :--- | :--- | :---: | :--- |
| **Trung tố** | **중위 표기법 (Infix)** | Nằm **ở giữa** hai toán hạng | `A + B` | Con người đọc; cần dấu ngoặc và bảng ưu tiên; tương ứng **Inorder** |
| **Tiền tố** | **전위 표기법 (Prefix)** | Nằm **ở phía trước** hai toán hạng | `+ A B` | Do Jan Łukasiewicz đề xuất; tương ứng phép duyệt **Preorder** |
| **Hậu tố** | **후위 표기법 (Postfix)** | Nằm **ở phía sau** hai toán hạng | `A B +` | **Trình biên dịch sử dụng cùng Stack**; không cần ngoặc; tương ứng **Postorder** |

#### 2. Quy trình 3 bước chuyển đổi Infix sang Postfix / Prefix
```
[ Bước 1: Đóng ngoặc ] ──> [ Bước 2: Dời toán tử ] ──> [ Bước 3: Xóa ngoặc ]
(Theo độ ưu tiên toán tử)    (Postfix: ra sau dấu ')'    (Thu được chuỗi kết quả)
                              Prefix: ra trước dấu '(')
```
- Ví dụ nhanh: Biểu thức $A / B \times (C + D) - E$
  - Bước 1 (Đóng ngoặc): $(((A / B) \times (C + D)) - E)$
  - Bước 2 (Dời toán tử sang Postfix): $(((A\ B\ /)\ (C\ D\ +)\ \times)\ E\ -)$
  - Bước 3 (Xóa ngoặc): **`A B / C D + * E -`**

#### 3. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Thứ tự toán tử trừ và chia trong Stack:**
  - Phần tử POP ra đầu tiên là $B$ (nằm ở đỉnh Top).
  - Phần tử POP ra thứ hai là $A$ (nằm dưới $B$).
  - Phép tính bắt buộc phải là: $\mathbf{A - B}$ và $\mathbf{A / B}$ (Lấy phần tử ra sau TRỪ ĐI hoặc CHIA CHO phần tử ra trước).
  - Lấy nhầm $B - A$ sẽ đổi dấu kết quả (như trong bài toán dưới sẽ thành $8 - 6 = 2$, sai hoàn toàn).
- **Bẫy 2: Ánh xạ duyệt cây nhị phân:**
  - **Preorder (Tiền thứ tự)** cho ra biểu thức **Prefix**.
  - **Inorder (Trung thứ tự)** cho ra biểu thức **Infix**.
  - **Postorder (Hậu thứ tự)** cho ra biểu thức **Postfix**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lý do trình biên dịch tối ưu hóa với Postfix
- Trong biểu thức Trung tố như $A + B \times C$, máy tính không thể thực hiện tuần tự từ trái qua phải vì phép nhân có độ ưu tiên cao hơn phép cộng. Máy tính sẽ phải quét nhiều lượt qua chuỗi, phân tích cặp ngoặc và duy trì bảng ưu tiên rất tốn bộ nhớ.
- Khi chuyển sang Hậu tố $A\ B\ C\ \times\ +$, **thứ tự xuất hiện của các toán tử chính là thứ tự thực thi phép tính thực tế**. Trình biên dịch chỉ cần duyệt chuỗi đúng 1 lượt từ trái qua phải, gặp số thì đẩy vào Stack, gặp dấu thì rút 2 số ra tính rồi đẩy kết quả vào lại.

#### 2. Chi tiết thuật toán và 2 bài tập ví dụ mẫu

##### Quy trình 3 bước chuẩn tắc:
1. **Bước 1 (Đóng ngoặc theo độ ưu tiên):**
   - Xác định thứ tự ưu tiên của các toán tử: Lũy thừa ($^\wedge$) $\rightarrow$ Nhân/Chia ($\times, /$) $\rightarrow$ Cộng/Trừ ($+, -$).
   - Nếu cùng độ ưu tiên thì đóng ngoặc từ trái sang phải.
   - Đóng ngoặc đơn đầy đủ cho từng cặp phép toán nhị phân.
2. **Bước 2 (Dời vị trí toán tử):**
   - **Nếu đổi sang Postfix (Hậu tố):** Kéo toán tử của cặp ngoặc đó ra **ngay sau dấu đóng ngoặc `)` tương ứng**.
   - **Nếu đổi sang Prefix (Tiền tố):** Kéo toán tử của cặp ngoặc đó ra **ngay trước dấu mở ngoặc `(` tương ứng**.
3. **Bước 3 (Xóa ngoặc):** Xóa toàn bộ tất cả các dấu ngoặc đơn, thu được chuỗi kết quả cuối cùng.

##### Ví dụ thực hành mẫu 1: Đổi sang Postfix
**Đề bài:** Chuyển biểu thức Infix sau sang dạng Postfix: $A / B \times (C + D) - E$
- *Bước 1 (Đóng ngoặc):*
  - Phép chia $A / B$ làm trước: $(A / B)$
  - Phép cộng trong ngoặc: $(C + D)$
  - Phép nhân hai cụm trên: $((A / B) \times (C + D))$
  - Phép trừ với $E$: $(((A / B) \times (C + D)) - E)$
- *Bước 2 (Dời toán tử sang Postfix):*
  - $(((A\ B\ /)\ (C\ D\ +)\ \times)\ E\ -)$
- *Bước 3 (Xóa ngoặc):*
  - Kết quả Postfix: **`A B / C D + * E -`**

##### Ví dụ thực hành mẫu 2: Đổi sang Prefix
**Đề bài:** Chuyển cùng biểu thức trên sang dạng Prefix: $A / B \times (C + D) - E$
- *Dời toán tử sang Prefix:*
  - $(- (* (/ A B) (+ C D)) E)$
- *Xóa ngoặc:*
  - Kết quả Prefix: **`- * / A B + C D E`**

#### 3. Bảng trace mô phỏng tính giá trị Postfix bằng Stack
Bài toán: Tính giá trị biểu thức Postfix `6 2 / 3 + 4 2 * -`

| Bước | Ký tự đọc | Thao tác trên Stack | Trạng thái Stack (Đỉnh Top bên phải) |
| :---: | :---: | :--- | :--- |
| 1 | `6` | PUSH(6) | `[6]` |
| 2 | `2` | PUSH(2) | `[6, 2]` |
| 3 | `/` | POP ra 2 và 6 $\rightarrow$ Tính: $6 / 2 = 3 \rightarrow$ PUSH(3) | `[3]` |
| 4 | `3` | PUSH(3) | `[3, 3]` |
| 5 | `+` | POP ra 3 và 3 $\rightarrow$ Tính: $3 + 3 = 6 \rightarrow$ PUSH(6) | `[6]` |
| 6 | `4` | PUSH(4) | `[6, 4]` |
| 7 | `2` | PUSH(2) | `[6, 4, 2]` |
| 8 | `*` | POP ra 2 và 4 $\rightarrow$ Tính: $4 \times 2 = 8 \rightarrow$ PUSH(8) | `[6, 8]` |
| 9 | `-` | POP ra 8 và 6 $\rightarrow$ Tính: $\mathbf{6 - 8 = -2} \rightarrow$ PUSH(-2) | `[-2]` (Kết quả cuối cùng) |

#### 4. Cây biểu thức nhị phân (Binary Expression Tree)
- Mối quan hệ giữa cây và biểu thức:
  - Các nút bên trong (`Internal Nodes`): Luôn luôn là **Toán tử** ($+, -, \times, /$).
  - Các nút lá (`Leaf Nodes`): Luôn luôn là **Toán hạng** (Hằng số hoặc Biến số).
- Sơ đồ cây biểu thức của `(6 / 2 + 3) - (4 * 2)`:
  ```
            [-]
           /   \
         [+]   [*]
         / \   / \
       [/]  3 4   2
       / \
      6   2
  ```
- Ánh xạ giữa duyệt cây và ký pháp:
  - **Duyệt tiền thứ tự (Preorder — Root $\rightarrow$ Left $\rightarrow$ Right):** Cho ra biểu thức **Prefix** (`- + / 6 2 3 * 4 2`).
  - **Duyệt trung thứ tự (Inorder — Left $\rightarrow$ Root $\rightarrow$ Right):** Cho ra biểu thức **Infix** (`(6 / 2 + 3) - (4 * 2)`).
  - **Duyệt hậu thứ tự (Postorder — Left $\rightarrow$ Right $\rightarrow$ Root):** Cho ra biểu thức **Postfix** (`6 2 / 3 + 4 2 * -`).

---

### 복습 체크리스트
- [ ] Phân biệt vị trí của toán tử trong 중위 (Infix), 전위 (Prefix), 후위 (Postfix).
- [ ] Giải thích tại sao trình biên dịch ưu tiên dùng Postfix (không cần ngoặc, duyệt 1 chiều với Stack).
- [ ] Nằm lòng quy trình 3 bước: Đóng ngoặc theo độ ưu tiên $\rightarrow$ Dời toán tử $\rightarrow$ Xóa ngoặc.
- [ ] Chuyển đổi thành thạo từ Infix sang Postfix và Prefix trong vòng 60 giây.
- [ ] Mô phỏng chuẩn xác từng bước PUSH và POP của giải thuật tính giá trị biểu thức Postfix.
- [ ] Nhớ chính xác thứ tự: Phần tử POP ra sau nằm bên trái phép trừ và phép chia ($A - B$, $A / B$).
- [ ] Nhớ mối liên hệ ánh xạ: Preorder $\leftrightarrow$ Prefix, Inorder $\leftrightarrow$ Infix, Postorder $\leftrightarrow$ Postfix.
