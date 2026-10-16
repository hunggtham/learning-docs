# Môn 2 · Bài 02 — Ký pháp biểu thức và ứng dụng ngăn xếp

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Tiếp nối [Bài 01: Cấu trúc dữ liệu tuyến tính](01-cau-truc-du-lieu-tuyen-tinh.md), bài học này đào sâu vào ứng dụng kỹ thuật quan trọng bậc nhất của cấu trúc Ngăn xếp (Stack) trong khoa học máy tính: **Biểu diễn ký pháp toán học và đánh giá biểu thức trong trình biên dịch**. Nội dung này thiết lập chiếc cầu nối trực tiếp giữa cấu trúc dữ liệu tuyến tính (Stack) và cấu trúc phi tuyến kế tiếp (Cây biểu thức nhị phân).

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `12-bai-hoc.md` và `13-bai-hoc.md` (tương ứng với các mục 5 và 080 trong tài liệu chuẩn gốc). Toàn bộ thuật toán chuyển đổi và trace từng bước trên ngăn xếp được đối chiếu với các dạng câu hỏi tính toán thực chiến của HRDK.

> **Mạch kiến thức:** Con người quen đọc biểu thức trung tố có dấu ngoặc ($A + B \times C$), nhưng máy tính lại không thể quét tới quét lui để giải quyết độ ưu tiên toán tử. Bài học này giải quyết ba vấn đề kỹ thuật: (1) Ba dạng ký pháp Infix, Prefix, Postfix khác nhau ra sao về mặt cấu trúc và tương ứng thế nào với các phép duyệt cây nhị phân? (2) Thuật toán 3 bước chuyển đổi biểu thức từ Infix sang Postfix/Prefix thực hiện như thế nào để không bao giờ nhầm lẫn? (3) Cơ chế ngăn xếp (Stack) thực thi tính toán biểu thức hậu tố từng bước ra sao và bẫy thứ tự toán hạng trong phép trừ/phép chia nằm ở đâu?

---

## 1. Ba dạng ký pháp biểu thức toán học — 수식 표기법

Trong khoa học máy tính, một biểu thức số học gồm hai thành phần: **Toán hạng (피연산자 / Operand — các biến hoặc hằng số như $A, B, 1, 2$)** và **Toán tử (연산자 / Operator — các phép tính như $+ - \times /$)**. Tùy thuộc vào vị trí tương đối của toán tử so với toán hạng, ta có 3 dạng ký pháp:

### Bảng so sánh 3 dạng biểu diễn biểu thức toán học

| Ký pháp | Tên tiếng Hàn & Anh | Vị trí toán tử | Cú pháp mẫu | Ứng dụng và Đặc tính kỹ thuật |
| :--- | :--- | :--- | :--- | :--- |
| **Trung tố** | **중위 표기법 (Infix)** | Nằm **ở giữa** hai toán hạng | `A + B` | Dạng hiển thị thông thường cho con người; cần dấu ngoặc đơn `()` và bảng độ ưu tiên toán tử |
| **Tiền tố** | **전위 표기법 (Prefix / Polish)** | Nằm **ở phía trước** hai toán hạng | `+ A B` | Do nhà toán học Jan Łukasiewicz đề xuất; tương ứng với phép duyệt tiền thứ tự (Preorder) |
| **Hậu tố** | **후위 표기법 (Postfix / Reverse Polish)** | Nằm **ở phía sau** hai toán hạng | `A B +` | **Trình biên dịch và máy tính sử dụng**; kết hợp với Stack để tính toán trực tiếp mà không cần ngoặc |

### Tại sao máy tính và trình biên dịch ưa chuộng Postfix?
- Trong biểu thức Infix như $A + B \times C$, máy tính không thể tính tuần tự từ trái sang phải vì phép nhân có độ ưu tiên cao hơn phép cộng. Máy tính phải quét nhiều lần, phân tích dấu ngoặc và duy trì bảng ưu tiên rất phức tạp.
- Ngược lại, trong biểu thức Postfix $A\ B\ C\ \times\ +$, **thứ tự xuất hiện của các toán tử chính là thứ tự thực hiện phép tính thực tế**. Máy tính chỉ cần duyệt chuỗi đúng **một lần duy nhất từ trái sang phải** kết hợp với cấu trúc ngăn xếp (Stack) là tính ra ngay kết quả mà không cần bất kỳ dấu ngoặc đơn nào.

---

## 2. Thuật toán chuyển đổi Infix sang Postfix và Prefix

Trong các kỳ thi trắc nghiệm Kỹ sư Xử lý Thông tin, bài toán chuyển đổi biểu thức trung tố (Infix) sang hậu tố (Postfix) hoặc tiền tố (Prefix) xuất hiện với tần suất 100%. Áp dụng thuật toán 3 bước chuẩn xác sau đây sẽ giúp giải nhanh và tuyệt đối không bao giờ nhầm lẫn:

### Quy trình 3 bước chuyển đổi chuẩn tắc
1. **Bước 1 (Đóng ngoặc theo độ ưu tiên):**
   - Xác định thứ tự ưu tiên của các toán tử: Lũy thừa ($^\wedge$) $\rightarrow$ Nhân/Chia ($\times, /$) $\rightarrow$ Cộng/Trừ ($+, -$).
   - Nếu cùng độ ưu tiên thì đóng ngoặc từ trái sang phải.
   - Đóng ngoặc đơn đầy đủ cho từng cặp phép toán nhị phân.
2. **Bước 2 (Dời vị trí toán tử):**
   - **Nếu đổi sang Postfix (Hậu tố):** Kéo toán tử của cặp ngoặc đó ra **ngay sau dấu đóng ngoặc `)` tương ứng**.
   - **Nếu đổi sang Prefix (Tiền tố):** Kéo toán tử của cặp ngoặc đó ra **ngay trước dấu mở ngoặc `(` tương ứng**.
3. **Bước 3 (Xóa ngoặc):** Xóa toàn bộ tất cả các dấu ngoặc đơn, thu được chuỗi kết quả cuối cùng.

### Ví dụ thực hành mẫu 1
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

### Ví dụ thực hành mẫu 2
**Đề bài:** Chuyển cùng biểu thức trên sang dạng Prefix: $A / B \times (C + D) - E$
- *Dời toán tử sang Prefix:*
  - $(- (* (/ A B) (+ C D)) E)$
- *Xóa ngoặc:*
  - Kết quả Prefix: **`- * / A B + C D E`**

---

## 3. Giải thuật tính toán giá trị biểu thức Postfix bằng Stack

Khi gặp bài toán yêu cầu: *"Tính giá trị số thực tế của một chuỗi biểu thức hậu tố Postfix"*, ta mô phỏng hoạt động của trình biên dịch bằng một ngăn xếp (Stack) duy nhất theo giải thuật sau:

### Giải thuật Stack Evaluation
1. Quét chuỗi Postfix lần lượt từng phần tử từ trái sang phải:
2. Nếu gặp **Toán hạng (Con số)**: Đẩy (**`PUSH`**) con số đó vào đỉnh Stack.
3. Nếu gặp **Toán tử (Dấu phép tính $+ - \times /$)**:
   - Lấy (**`POP`**) phần tử trên cùng ra khỏi Stack $\rightarrow$ Đây là **Toán hạng thứ hai ($B$)**.
   - Lấy (**`POP`**) phần tử tiếp theo ra khỏi Stack $\rightarrow$ Đây là **Toán hạng thứ nhất ($A$)**.
   - Thực hiện phép toán: $A \text{ [Toán tử] } B$.
   - Đẩy (**`PUSH`**) kết quả vừa tính ngược trở lại đỉnh Stack.
4. Lặp lại cho đến khi đọc hết chuỗi. Giá trị duy nhất còn lại trong Stack chính là kết quả cuối cùng.

### ⚠️ Bẫy đề thi kinh điển: Thứ tự toán hạng trong phép trừ và phép chia
Trong phép cộng ($A + B = B + A$) và phép nhân ($A \times B = B \times A$), tính chất giao hoán làm cho thứ tự không ảnh hưởng. Tuy nhiên, **phép trừ và phép chia không có tính giao hoán**:
- Phần tử bị `POP` ra đầu tiên là $B$ (nằm ở đỉnh Top).
- Phần tử bị `POP` ra thứ hai là $A$ (nằm dưới $B$).
- Phép tính bắt buộc phải là: $\mathbf{A - B}$ và $\mathbf{A / B}$ (Lấy phần tử lấy ra sau TRỪ ĐI hoặc CHIA CHO phần tử lấy ra trước). Lấy ngược $B - A$ hay $B / A$ sẽ dẫn đến đáp án sai ngay lập tức!

### Bảng trace mô phỏng từng bước chi tiết
**Bài toán:** Tính giá trị biểu thức Postfix: `6 2 / 3 + 4 2 * -`

| Bước | Ký tự đọc | Loại phần tử | Thao tác trên Stack | Trạng thái Stack (Đỉnh bên phải) |
| :---: | :---: | :---: | :--- | :--- |
| **1** | `6` | Số | PUSH(6) | `[6]` |
| **2** | `2` | Số | PUSH(2) | `[6, 2]` |
| **3** | `/` | Toán tử | POP ra 2 và 6 $\rightarrow$ Tính: $6 / 2 = 3 \rightarrow$ PUSH(3) | `[3]` |
| **4** | `3` | Số | PUSH(3) | `[3, 3]` |
| **5** | `+` | Toán tử | POP ra 3 và 3 $\rightarrow$ Tính: $3 + 3 = 6 \rightarrow$ PUSH(6) | `[6]` |
| **6** | `4` | Số | PUSH(4) | `[6, 4]` |
| **7** | `2` | Số | PUSH(2) | `[6, 4, 2]` |
| **8** | `*` | Toán tử | POP ra 2 và 4 $\rightarrow$ Tính: $4 \times 2 = 8 \rightarrow$ PUSH(8) | `[6, 8]` |
| **9** | `-` | Toán tử | POP ra 8 và 6 $\rightarrow$ Tính: $\mathbf{6 - 8 = -2} \rightarrow$ PUSH(-2) | `[-2]` |

**Kết quả cuối cùng:** **`-2`**.

---

## 4. Tương quan giữa Ký pháp biểu thức và Cây biểu thức nhị phân

Cấu trúc biểu thức số học có mối tương quan đối ngẫu hoàn hảo với Cây nhị phân (Binary Expression Tree):
- Mỗi **Toán tử** là một **Nút cha (Internal Node)**.
- Hai **Toán hạng** là hai **Cây con bên trái (Left Child) và bên phải (Right Child)**.
- Các hằng số/biến số ở dưới đáy là các **Nút lá (Terminal / Leaf Nodes)**.

```
          [-]
         /   \
       [+]   [*]
       / \   / \
     [/]  3 4   2
     / \
    6   2
```

Ánh xạ giữa duyệt cây và ký pháp:
- **Duyệt tiền thứ tự (Preorder — Root $\rightarrow$ Left $\rightarrow$ Right):** Cho ra biểu thức **Prefix** (`- + / 6 2 3 * 4 2`).
- **Duyệt trung thứ tự (Inorder — Left $\rightarrow$ Root $\rightarrow$ Right):** Cho ra biểu thức **Infix** (`(6 / 2 + 3) - (4 * 2)`).
- **Duyệt hậu thứ tự (Postorder — Left $\rightarrow$ Right $\rightarrow$ Root):** Cho ra biểu thức **Postfix** (`6 2 / 3 + 4 2 * -`).

---

## 5. Nối mạch kiến thức sang bài tiếp theo

Từ việc quan sát cây biểu thức nhị phân ở trên, người học nhận thấy rằng để biểu diễn các mối quan hệ phân nhánh phức tạp, cấu trúc dữ liệu tuyến tính đã bộc lộ giới hạn.

Để xử lý dữ liệu phân cấp, phân loại thư mục và tối ưu hóa cây tìm kiếm nhị phân, chúng ta chính thức bước sang nhóm cấu trúc phi tuyến với **[Bài 03: Cấu trúc phi tuyến — Cây và duyệt cây nhị phân](03-cay-va-duyet-cay-nhi-phan.md)**, nơi ta sẽ làm chủ thuật ngữ cây (Degree, Leaf, Depth), các dạng cây nhị phân và ba thuật ngữ duyệt cây kinh điển Preorder, Inorder, Postorder.

---

## 6. 복습 체크리스트 (Checklist ôn tập)

- [ ] Phân biệt vị trí của toán tử trong 중위 (Infix), 전위 (Prefix), 후위 (Postfix).
- [ ] Giải thích tại sao trình biên dịch ưu tiên dùng Postfix (không cần ngoặc, quét 1 chiều bằng Stack).
- [ ] Nằm lòng 3 bước chuyển đổi: Đóng ngoặc ưu tiên $\rightarrow$ Dời dấu toán tử $\rightarrow$ Xóa ngoặc.
- [ ] Chuyển đổi thành thạo từ Infix sang Postfix và Prefix trong vòng 90 giây.
- [ ] Mô phỏng chuẩn xác từng bước PUSH và POP của giải thuật tính giá trị biểu thức Postfix.
- [ ] Chú ý đúng thứ tự: Phần tử POP ra sau nằm bên trái phép trừ và phép chia ($A - B$, $A / B$).
- [ ] Nhớ mối liên hệ ánh xạ: Preorder $\leftrightarrow$ Prefix, Inorder $\leftrightarrow$ Infix, Postorder $\leftrightarrow$ Postfix.
