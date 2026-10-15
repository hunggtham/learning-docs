# 11. 수식의 표기법 (Expression Notation)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 phương pháp biểu diễn biểu thức số học trong khoa học máy tính: Ký pháp trung tố (`중위 표기법 - Infix`), Ký pháp tiền tố (`전위 표기법 - Prefix`), và Ký pháp hậu tố (`후위 표기법 - Postfix`).
- Hiểu mối liên hệ mật thiết giữa Cây biểu thức (`수식 트리 - Expression Tree`) với các phép duyệt cây nhị phân (Inorder $\rightarrow$ Infix, Preorder $\rightarrow$ Prefix, Postorder $\rightarrow$ Postfix).
- Thành thạo kỹ thuật chuyển đổi từ Infix sang Postfix và thuật toán tính toán giá trị biểu thức Postfix bằng cấu trúc Ngăn xếp (Stack).

## 핵심 키워드 (Từ khóa)
- 수식 표기법 (Ký pháp biểu thức số học / Expression Notation)
- 중위 표기법 (Infix Notation: $A + B$)
- 전위 표기법 (Prefix Notation / Polish Notation: $+ A B$)
- 후위 표기법 (Postfix Notation / Reverse Polish Notation: $A B +$)
- 수식 트리 (Cây biểu thức / Expression Tree)
- 스택 연산 (Thao tác ngăn xếp tính biểu thức hậu tố)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([10. 이진 트리의 운행법 (Binary Tree Traversal)](53-bai-hoc.md)):** Sau khi thành thạo 3 phép duyệt cây nhị phân, bài này ứng dụng trực tiếp phép duyệt cây để biểu diễn các biểu thức toán học trong trình biên dịch.
- **Tiếp nối sang bài sau ([12. 외부 정렬 및 정렬 알고리즘](55-bai-hoc.md)):** Chuyển từ biểu diễn biểu thức sang các thuật toán sắp xếp dữ liệu (Sorting Algorithms).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc vị trí của toán tử: Infix toán tử ở giữa, Prefix toán tử ở đầu, Postfix toán tử ở sau; máy tính chuộng Postfix vì dùng Stack tính toán không cần dấu ngoặc.
- Đọc TẦNG B để làm chủ thuật toán tính toán biểu thức hậu tố bằng Stack (gặp số thì Push, gặp toán tử thì Pop 2 số ra tính rồi Push kết quả lại).

---

## 11. 수식의 표기법 (Expression Notation)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **3 dạng biểu diễn biểu thức số học:**
  1. **중위 표기법 (Infix Notation - Ký pháp trung tố):**
     - Toán tử nằm **ở giữa** hai toán hạng: $\mathbf{A + B}$.
     - Đây là cách con người quen đọc và viết trong đời sống hàng ngày.
     - *Nhược điểm đối với máy tính:* Bắt buộc phải có dấu ngoặc đơn `( )` và bảng quy tắc độ ưu tiên toán tử (nhân chia trước, cộng trừ sau), gây phức tạp cho trình biên dịch.
  2. **전위 표기법 (Prefix Notation / Polish Notation - Ký pháp tiền tố):**
     - Toán tử nằm **ở trước** hai toán hạng: $\mathbf{+ A B}$.
     - Tương ứng với kết quả phép **duyệt tiền thứ tự (전위 순회 - Preorder)** trên Cây biểu thức.
  3. **후위 표기법 (Postfix Notation / Reverse Polish Notation - Ký pháp hậu tố):**
     - Toán tử nằm **ở sau** hai toán hạng: $\mathbf{A B +}$.
     - Tương ứng với kết quả phép **duyệt hậu thứ tự (후위 순회 - Postorder)** trên Cây biểu thức.
     - **Ưu điểm vượt trội đối với máy tính:** **Hoàn toàn không cần dùng dấu ngoặc đơn `( )`** và không cần xét độ ưu tiên toán tử; trình biên dịch sử dụng cấu trúc **Ngăn xếp (Stack)** để tính giá trị biểu thức cực kỳ nhanh chóng và chính xác.
- **Thuật toán tính giá trị biểu thức hậu tố (Postfix) bằng Stack:**
  - Đọc chuỗi biểu thức từ trái sang phải:
    - Nếu gặp **Toán hạng (Con số)** $\rightarrow$ Đẩy (`Push`) vào Stack.
    - Nếu gặp **Toán tử (`+`, `-`, `*`, `/`)** $\rightarrow$ Rút (`Pop`) 2 toán hạng từ đỉnh Stack ra:
      - Số rút ra đầu tiên là toán hạng sau ($b$).
      - Số rút ra thứ hai là toán hạng trước ($a$).
      - Thực hiện phép tính $a \text{ [toán tử] } b$, sau đó đẩy kết quả (`Push`) ngược trở lại vào Stack.
  - Khi đọc hết chuỗi, phần tử duy nhất còn lại trong Stack chính là kết quả cuối cùng của biểu thức.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Máy tính và trình biên dịch thường chuyển đổi biểu thức trung tố Infix sang dạng nào để tính toán thuận tiện nhất?"* -> **후위 표기법 (Postfix Notation)**.
  - **Bẫy 2 (Thứ tự toán hạng khi Pop):** Khi gặp phép trừ `-` hoặc phép chia `/`, lưu ý số lấy ra trước là số bị trừ/chia, số lấy ra sau đứng trước. Ví dụ Pop ra $3$ rồi Pop ra $8$ thì phép tính là $8 - 3 = 5$, không phải $3 - 8$.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Infix ở giữa người đọc, Prefix ở trước, Postfix ở sau máy tính dùng Stack tính không cần ngoặc".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán mẫu trắc nghiệm chuyển đổi và tính toán:**
  - **Ví dụ 1: Chuyển biểu thức Infix sang Postfix:**
    - Cho biểu thức Infix: $(A + B) * (C - D)$
    - Bước 1: Xét trong ngoặc $(A + B) \rightarrow AB+$
    - Bước 2: Xét trong ngoặc $(C - D) \rightarrow CD-$
    - Bước 3: Đưa toán tử nhân $*$ ra sau cùng $\rightarrow \mathbf{A B + C D - *}$
  - **Ví dụ 2: Tính giá trị biểu thức Postfix bằng Stack:**
    - Cho chuỗi Postfix: `3 4 + 2 * 7 -`
    - Đọc `3` $\rightarrow$ Push(3). Stack: `[3]`
    - Đọc `4` $\rightarrow$ Push(4). Stack: `[3, 4]`
    - Đọc `+` $\rightarrow$ Pop 4, Pop 3 $\rightarrow$ Tính $3 + 4 = 7$ $\rightarrow$ Push(7). Stack: `[7]`
    - Đọc `2` $\rightarrow$ Push(2). Stack: `[7, 2]`
    - Đọc `*` $\rightarrow$ Pop 2, Pop 7 $\rightarrow$ Tính $7 * 2 = 14$ $\rightarrow$ Push(14). Stack: `[14]`
    - Đọc `7` $\rightarrow$ Push(7). Stack: `[14, 7]`
    - Đọc `-` $\rightarrow$ Pop 7, Pop 14 $\rightarrow$ Tính $14 - 7 = 7$ $\rightarrow$ Push(7). Stack: `[7]`
    - $\Longrightarrow$ Kết quả cuối cùng là **$\mathbf{7}$**.

### 복습 체크리스트
- [ ] Phân biệt được cấu trúc của Infix ($A+B$), Prefix ($+AB$), và Postfix ($AB+$).
- [ ] Giải thích tại sao máy tính sử dụng Postfix và Stack để tính giá trị biểu thức.
- [ ] Chuyển đổi thành thạo từ Infix sang Postfix.
- [ ] Tự tay tính đúng bài toán Stack của biểu thức hậu tố `3 4 + 2 * 7 -`.
