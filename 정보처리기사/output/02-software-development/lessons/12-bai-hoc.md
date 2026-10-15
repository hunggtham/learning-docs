# 5. 수식의 표기법 변환 (Expression Notation Conversion)

## 학습 목표 (Mục tiêu)
- Định nghĩa ba phương pháp biểu diễn biểu thức số học: Trung tố (Infix / 중위 표기법), Tiền tố (Prefix / 전위 표기법) và Hậu tố (Postfix / 후위 표기법).
- Nắm vững quy trình chuyển đổi biểu thức từ Infix sang Prefix và Postfix bằng phương pháp đóng ngoặc ưu tiên và dịch chuyển toán tử.
- Hiểu lý do khoa học máy tính ưa chuộng biểu thức Postfix kết hợp với cấu trúc dữ liệu Stack để tối ưu hóa tốc độ thực thi trong trình biên dịch.

## 핵심 키워드 (Từ khóa)
- 수식 표기법 (Expression Notation)
- 중위 표기법 (Infix Notation)
- 전위 표기법 (Prefix Notation)
- 후위 표기법 (Postfix Notation / Reverse Polish)
- 연산자 우선순위 (Operator Precedence)
- 스택 기반 연산 (Stack-based Evaluation)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): 스택 (Stack - LIFO) và cơ chế tính toán biểu thức hậu tố.
- [06-bai-hoc.md](06-bai-hoc.md): Ánh xạ duyệt cây nhị phân (Preorder $\rightarrow$ Prefix, Inorder $\rightarrow$ Infix, Postorder $\rightarrow$ Postfix).
- [13-bai-hoc.md](13-bai-hoc.md): Phương pháp chi tiết và thuật toán tính giá trị biểu thức Postfix.

## 읽는 방법 (Cách đọc)
- Nhớ vị trí của **Toán tử (Operator: $+ - * /$)** đối với **Toán hạng (Operand: $A, B, C$)**:
  - **Infix (Trung tố):** Toán tử nằm **Ở GIỮA** hai toán hạng ($A + B$).
  - **Prefix (Tiền tố):** Toán tử dịch ra **PHÍA TRƯỚC** ($+ A B$).
  - **Postfix (Hậu tố):** Toán tử dịch ra **PHÍA SAU** ($A B +$).
- Kỹ thuật 3 bước đổi biểu thức không bao giờ sai: Đóng ngoặc $\rightarrow$ Dời dấu $\rightarrow$ Xóa ngoặc.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **So sánh 3 dạng biểu diễn biểu thức toán học:**

| Dạng biểu thức | Tên tiếng Hàn & Anh | Cú pháp mẫu | Ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **Trung tố** | **중위 표기법 (Infix)** | `A + B` | Dạng hiển thị thông thường cho con người đọc và viết |
| **Tiền tố** | **전위 표기법 (Prefix / Polish)** | `+ A B` | Tương ứng với phép duyệt tiền thứ tự (Preorder Traversal) |
| **Hậu tố** | **후위 표기법 (Postfix / Reverse Polish)** | `A B +` | **Trình biên dịch và máy tính sử dụng** (kết hợp với Stack để tính toán không cần ngoặc) |

- **Thuật toán 3 bước chuyển đổi Infix sang Postfix / Prefix:**
  - **Bước 1 (Đóng ngoặc):** Dựa vào thứ tự ưu tiên của toán tử (ngoặc tròn $\rightarrow$ lũy thừa $\rightarrow$ nhân/chia $\rightarrow$ cộng/trừ), đóng ngoặc đầy đủ cho từng cặp phép tính.
  - **Bước 2 (Dời dấu toán tử):**
    - Chuyển sang **Postfix**: Kéo toán tử ra ngay sau dấu đóng ngoặc `)` tương ứng của cặp đó.
    - Chuyển sang **Prefix**: Kéo toán tử ra ngay trước dấu mở ngoặc `(` tương ứng của cặp đó.
  - **Bước 3 (Xóa ngoặc):** Xóa toàn bộ các dấu ngoặc đơn, thu được chuỗi kết quả cuối cùng.

- **Ví dụ thực hành mẫu:**
  - Đề bài: Chuyển biểu thức Infix sau sang Postfix: $A / B * (C + D)$
    - *Bước 1:* Đóng ngoặc theo độ ưu tiên: $((A / B) * (C + D))$
    - *Bước 2:* Dời toán tử ra sau ngoặc: $((A B /) (C D +) *)$
    - *Bước 3:* Xóa ngoặc: **`A B / C D + *`**
  - Chuyển cùng biểu thức trên sang Prefix:
    - *Dời dấu ra trước:* $(*(/ A B) (+ C D))$
    - *Xóa ngoặc:* **`* / A B + C D`**

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế tính biểu thức Postfix bằng Stack (Stack Evaluation):**
  - Trình biên dịch đọc chuỗi Postfix từ trái sang phải:
    - Nếu gặp **Toán hạng (Số)**: Đẩy (`PUSH`) vào Stack.
    - Nếu gặp **Toán tử (Dấu phép tính)**: Lấy (`POP`) 2 toán hạng trên đỉnh Stack ra, thực hiện phép tính (lưu ý: toán hạng lấy ra trước nằm bên phải phép toán), rồi `PUSH` kết quả ngược trở lại Stack.
    - Sau khi đọc hết chuỗi, giá trị duy nhất còn lại trên đỉnh Stack chính là kết quả cuối cùng của toàn biểu thức.

### 복습 체크리스트
- [ ] Phân biệt được vị trí của toán tử trong Infix (ở giữa), Prefix (phía trước) và Postfix (phía sau).
- [ ] Thuần thục 3 bước chuyển đổi: Đóng ngoặc $\rightarrow$ Dời dấu toán tử $\rightarrow$ Xóa ngoặc.
- [ ] Giải thích được tại sao máy tính ưa chuộng Postfix (không cần dấu ngoặc, tính trực tiếp bằng Stack).
- [ ] Tính đúng kết quả một biểu thức mẫu từ Infix sang Postfix và Prefix.
